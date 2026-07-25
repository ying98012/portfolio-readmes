---
title: 校園導航與資訊整合平台
slug: 校園導航與資訊整合平台
updatedAt: 2026-07-25
---
# 校園導航與資訊整合平台

> 校園室內導航 + AI 校園助手 Android App，以 Kotlin + Jetpack Compose 打造。

![Platform](https://img.shields.io/badge/platform-Android-3DDC84)
![Language](https://img.shields.io/badge/Kotlin-2.2.10-7F52FF)
![minSdk](https://img.shields.io/badge/minSdk-26-blue)
![License](https://img.shields.io/badge/license-MIT-green)

「校園導航與資訊整合平台」 結合「自建室內路網 + Dijkstra」、「WiFi / ESP32 雙模式樓層偵測（含手機氣壓輔助）」、「Mapbox 自訂 Tileset」與「AI 校園助手」，解決一般地圖 App 在校園多樓教學大樓內 **GPS 飄移、無樓層（Z 軸）、戶外路網無室內走廊** 三大失效情境。

> **實作範圍**：以國立勤益科技大學（NCUT）工程館為驗證場域，目前實作涵蓋 **B1、1F~7F 共 8 個樓層**（floor 編碼 −1、1~7）。尚未實作 B2 與 8F；`assets/indoor_graph.json` 與各樓 Mapbox Tileset 僅涵蓋此範圍。

---

## 功能特色

- **室內導航**：自建 `indoor_graph.json` 室內路網，以決定性 Dijkstra（節點 ID 字典序 tie-breaking）計算最短路徑，相同輸入永遠產生相同路線。
- **豎井三段式跨樓**：以 `shaft_id` 識別物理樓梯/電梯，跨樓路線拆成「起點→豎井入口→垂直穿越→豎井出口→終點」，保證「走樓梯」「搭電梯」全程使用**單一豎井**，不混用。
- **雙模式樓層偵測**：設定頁可切換 **WiFi RSSI** 或 **ESP32 感測器**（已移除「自動模式」）；WiFi 以 `wifi_ap_floors.json` BSSID/SSID 對照 + 硬規則 + 加權 RSSI，並可與手機氣壓雙源融合加速切樓；ESP32 以 BMP280 氣壓 + 手機內建氣壓輔助，投票防抖與動態門檻避免邊界區跳樓層。
- **GPS 視覺穩定**：兩段式吸附（教室中心 + 走廊投影），即使 accuracy 達 20~30 m，藍點仍貼著走廊移動、不穿牆。
- **導航 PDR 後備**：室內 GPS 失訊時，以步數沿路網弧長推進（ESP32 累積步數或手機 `TYPE_STEP_DETECTOR`）；可信 GPS 僅做漸進校正，避免定位點凍結。
- **跨樓路線選擇**：不同樓層可並列「走樓梯」「搭電梯」選項，各自獨立 Dijkstra + 豎井三段式，不混用垂直通道。
- **眾包路網**：自動足跡採集 → Pending Edge → Promote，使用者正常步行即可累積並擴充路網樣本。
- **AI 校園助手**：五層分流（資工系 `csie_news` RTDB → 校級 `ncut_homepage_tabs` RTDB → Gemini Grounding 公告類 → Firebase FAQ → Gemini 一般對話，保留最近 10 輪上下文）；每帳號 Gemini 額度存於 Firebase `user_quotas`（預設 50 次，可於設定頁覆寫個人 API Key）。
- **帳號系統**：Firebase Authentication（Email/Password + Google Sign-In + 註冊驗證 + 忘記密碼）。

### 主要畫面


| 畫面 | 說明 |
| ---- | ----------------------------- |
| 首頁 | 入口與功能導覽 |
| 校園導航 | Mapbox 底圖 + 室內路線 / 樓層圖層 |
| 聊天助手 | FAQ / 公告 / Gemini 五層分流 |
| 樓層偵測 | WiFi 或 ESP32 偵測狀態與除錯資訊 |
| 節點收集 | 現場節點採集輔助 |
| 設定 | 偵測模式、足跡開關、Gemini 額度 / API Key |


---

## 技術棧


| 項目 | 技術 / 版本 |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 語言 | Kotlin 2.2.10 |
| Android | minSdk 26 / targetSdk 36 / compileSdk 36 / JavaVersion 21 / AGP 9.1.0 |
| UI | Jetpack Compose（Material 3，無 XML 佈局） |
| 架構 | MVVM + StateFlow / Flow + Coroutine |
| 地圖 | Mapbox Maps SDK `android-ndk27:11.18.2` + `maps-compose-ndk27:11.18.2` |
| 室內路徑 | 自建 `IndoorGraph` + Dijkstra + 豎井三段式（未使用 Mapbox Directions） |
| 樓層偵測 | WiFi、ESP32 BLE + BMP280、手機 `Sensor.TYPE_PRESSURE` |
| 導航位移後備 | ESP32 韌體步數 / 手機計步器（`PhoneStepReader`）+ 弧長進度融合（`MapViewModel`） |
| 定位 | `play-services-location:21.3.0` |
| 登入 / 即時資料 | Firebase Auth + Realtime Database（BOM 34.10.0）；路徑含 `school_faq`、`user_quotas`、`ncut_homepage_tabs(_index)`、`csie_news(_index)` |
| AI | `generativeai:0.9.0`（Gemini）+ REST（Gemini Grounding）；每帳號預設 50 次額度 |
| 本機儲存 | Room 2.7.2（足跡）+ SharedPreferences（偵測模式、聊天偏好） |
| 校網爬蟲 | Python（requests / BeautifulSoup / Playwright）+ GitHub Actions 每小時 cron |


---

## 架構（MVVM 三層）


| 層 | 角色 | 代表性檔案 |
| ---------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **View（`ui/`）** | Jetpack Compose 純 UI，不含業務邏輯 | `HomeScreen`、`MapScreen`、`ChatAssistantScreen`、`SettingsScreen`、`FloorDetectionScreen`、`NodeCollectorScreen`、`LoginScreen` |
| **ViewModel（`viewmodel/`）** | 業務邏輯、StateFlow 狀態 | `MapViewModel`、`BleViewModel`、`ChatViewModel`、`AuthViewModel`、`SettingsViewModel`、`NodeCollectorViewModel` |
| **Model / Data（`data/`、`model/`）** | 感測器、Firebase、Room、地圖路網 | `IndoorGraph`、`WifiScanner`、`WiFiFloorResolver`、`BleService`、`SensorFloorResolver`、`PhoneBarometerReader`、`PhoneStepReader`、`FirebaseRepository`、`HomepageTabRepository`、`CsieNewsRepository`、`FootprintRepository` |


```text
com.example.schoolgps/
├── MainActivity.kt           # 啟動入口；依登入狀態切 Auth/Main NavGraph
├── ui/                       # View 層（Compose）：screens/、map/、theme/
├── viewmodel/                # ViewModel 層
├── data/                     # Model 層：indoor/、mapbox/、ble/、footprint/、Firebase、Gemini、WiFi
├── model/                    # Data Classes（POJO）
├── utils/                    # 共享工具（如 DebugFileLogger）
├── core/、domain/、di/       # 預留擴充分層（多為 .keep 占位）
└── assets/                   # indoor_graph.json、wifi_ap_floors.json、room_link_hints.json
```

---

## 開始使用

### 環境需求

- Android Studio Ladybug+（compileSdk 36 / JDK 21）

### 設定金鑰

1. **Mapbox 下載 Token** → 專案根目錄 `gradle.properties`：
  ```properties
   MAPBOX_DOWNLOADS_TOKEN=sk.eyJ1Ijo...（你的 Mapbox secret token）
  ```
2. **Gemini API Key**（可選）→ `local.properties`（亦可於 App 設定頁輸入個人 key 覆蓋）：
  ```properties
   GEMINI_API_KEY=AIza...
  ```
3. 將 Firebase Console 下載的 `google-services.json` 放到 `app/`。

### 建置與執行

Android Studio → Sync Project → Run。

> **安全提醒**：`gradle.properties` 預設受 git 追蹤，`MAPBOX_DOWNLOADS_TOKEN` 會進入版本歷史。如需避免，請改放 user-level `~/.gradle/gradle.properties` 或加入 `.gitignore`。

---

## 室內路網（`assets/indoor_graph.json`）

- **節點命名**（以工程館為例）：走廊交叉口 `eng_corridor_<floor>f_jct_<a|b|...>`、走廊補充點 `*_cor_*`、樓梯 `*_stair_*`（須有 `shaft_id`）、電梯 `*_elv_*`（`shaft_id` 以 `ELV` 開頭）；教室節點 `node_<floor>f_<classroom>` 由 Mapbox Studio 動態注入，不寫死於 JSON。
- **權重**：JSON 的 `weight` 欄位忽略，執行時以 Haversine 距離重算（下限 0.5 m）。
- **跨樓邊**：禁止手寫，一律由 `shaft_id` + 三段式規劃處理。
- **眾包輸出**：`files/indoor_graph_promoted.json` 啟動時優先載入，否則 fallback 到 `assets/indoor_graph.json`。Promote 門檻：`uniqueSegmentCount ≥ 3`、`avgAccuracy < 12 m`、`confidence ≥ 0.6`。

### 路網治理腳本（`scripts/`，不部署到 App）

完整盤點見 `[scripts/README.md](scripts/README.md)`；治理規則見 `.cursor/rules/scripts-governance.mdc`。


| 腳本 | 用途 | 是否改檔 |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ------------------- |
| `verify_graph_health.py` / `verify_path_health.py` / `verify_shaft_integrity.py` | 結構 / 路徑成功率 / 豎井完整性檢查 | ❌ |
| `run_floor_planning_check.py` | 一鍵執行樓層路徑規劃檢查固定流程 | ❌ |
| `mcp_task_router.py` | 依任務描述建議 MCP 呼叫順序（Pandas → GIS → Mapbox） | ❌ |
| `diagnose_route_fork.py` / `debug_planning_failures.py` | 路徑分叉 / 規劃失敗診斷 | ❌ |
| `enforce_corridor_chain_rules.py` / `simplify_floor_corridor.py` / `cleanup_unreasonable_nodes.py` / `force_connect_same_floor_components.py` | 走廊鏈 / 簡化 / 噪點清理 / 連通性修補 | dry-run / `--apply` |
| `fix_long_corridor_edges.py` / `fix_3f_jcta_corridor_link.py` | 長捷徑邊修剪 / 3F jct_a 走廊鏈專用修補 | dry-run / `--apply` |
| `check_user_graph.py` / `fix_user_graph.py` / `merge_into_indoor_graph.py` / `merge_promoted_graph.py` | 外部 / Promote JSON 清理與合併 | ❌ / `--apply` |
| `fetch_ncut_homepage_tabs.py` | 校網 nav-tabs 爬蟲 → RTDB `ncut_homepage_tabs/` | 寫 Firebase |
| `fetch_csie_news.py` | 資工系 ajax 公告爬蟲 → RTDB `csie_news/` | 寫 Firebase |


GitHub Actions：`.github/workflows/ncut_tabs_cron.yml` 每小時執行上述兩支爬蟲（`workflow_dispatch` 可手動觸發）。

---

## Firebase RTDB 資料路徑


| 路徑 | 用途 | 寫入來源 |
| ------------------------------------------------- | --------------- | ----------------------------- |
| `school_faq` | 常見問答 | Firebase Console（唯讀給 App） |
| `user_quotas/$uid` | 每帳號 Gemini 剩餘額度 | App 讀寫 |
| `ncut_homepage_tabs` / `ncut_homepage_tabs_index` | 校級首頁 tab 結構化內容 | `fetch_ncut_homepage_tabs.py` |
| `csie_news` / `csie_news_index` | 資工系各分類公告 | `fetch_csie_news.py` |


規則範本見 `[scripts/_rtdb_rules.current.json](scripts/_rtdb_rules.current.json)`（需部署至 Firebase Console）。

---

## 設計原則

- **Single Source of Truth**：教室在 Mapbox Studio、登入狀態在 `AuthViewModel`、校網 / 系所公告在 Firebase RTDB。
- **室內外路由完全分離**：室內 100% 採自建 `IndoorGraph` + Dijkstra；未啟用 Mapbox Directions / Navigation SDK，僅用 Maps SDK 提供底圖與向量圖層。
- **可離線運作**：無網路也能查教室、規劃路線（僅 AI 助手與 FAQ 需網路）。
- **決定性演算法**：Dijkstra + ID 字典序 tie-breaking，方便除錯與回測。
- **嚴格 MVVM**：UI 不寫業務邏輯、ViewModel 不引用 View、Model 不依賴 Compose。
- **Logcat 一律英文**（新增/修改部分）。

---

## 文件

- 問題追蹤與修復記錄：`[bug.md](bug.md)`（共 50 筆，BUG-001 ~ BUG-050）
- 採集與工作流程：`[docs/footprint_to_graph_workflow.md](docs/footprint_to_graph_workflow.md)`、`[docs/node_collector_operation_guide.md](docs/node_collector_operation_guide.md)`
- 目錄擴充建議：`[docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md)`
- WiFi 現場量測：`[docs/wifi_rssi_fieldwork.md](docs/wifi_rssi_fieldwork.md)`
- 路網腳本盤點：`[scripts/README.md](scripts/README.md)`

---

## License

本專案採用 MIT License；地圖數據版權歸 Mapbox 與國立勤益科技大學所有。