# 🚀 FlowStock - 智慧雙軌 AI 進銷存與商業分析系統

一款基於 Flutter 開發的輕量化、在地優先（Local-First）智慧進銷存管理應用程式。本系統專為**中小型商家與個人自由創業者**設計，旨在極低硬體與營運成本下，提供高追溯性的庫存流水帳管理、財務報表視覺化，以及完全免 API 成本的 AI 經營策略生成建議。

---

## ✨ 為什麼選 FlowStock（優勢與實務痛點）

傳統 ERP 太重、試算表太散、記帳 App 又管不好庫存。FlowStock 對準中小店「一手機、當場做完」的節奏，把進銷存做成可追溯、可離線、可升級的日常工具。

### 能解決的實務問題

| 現場情境 | FlowStock 怎麼解 |
| :--- | :--- |
| 臨時進新品，庫存頁還沒建檔 | **進貨單品項旁一鍵新增商品**，存完自動選入該列，再填數量與進價 |
| 新品還沒進貨，不知道成本填多少 | **期初庫存 = 0 時單價成本可留空**；第一次確認入庫後自動寫入／更新成本 |
| 貨還沒到就以為庫存變了 | **訂單驅動**：先「待收貨／待出庫」，確認後才寫流水、動庫存 |
| 用箱進、用瓶賣，帳算不清 | **多量詞換算 + 各量詞當筆定價**；成本永遠歸一到基準量詞加權平均 |
| 想查「這筆進貨後來怎麼了」 | **流水帳 + 訂單詳情**可互相跳轉；作廢／刪除可反向庫存（不足則歸零並警告） |
| 每天開店想先看賺賠與該補什麼 | **儀表板**：今日營收／毛利／進貨支出可點進明細；低庫存警示與一鍵重新訂購（Pro） |
| 資料在自己裝置、怕斷網不能用 | **Local-First（Isar）**；AI 亦可端側優先，雲端為備援 |
| 想要經營建議又不想養一套 IT | **雙軌 AI 顧問**（端側 Nano → 雲端／Proxy）；無 Key 時仍有本地規則洞察 |
| Excel 有一批舊品項要上系統 | **試算表匯入（Pro）**：全量驗證後原子寫入，失敗不半套入帳 |
| 怕訂閱扣款沒注意到 | **扣款前 3 天起每日推播**；訂閱頁一鍵跳轉商店管理 |

### 產品優勢速覽

- **現場優先**：進貨當下可建檔；成本跟「有沒有貨」走，不逼你猜價。
- **帳能對得起來**：庫存異動必經流水；進銷走訂單狀態機，減少誤觸。
- **成本只有一本帳**：基準量詞加權平均；開單預設只是快捷鍵，不是第二套成本。
- **離線也能做生意**：核心進銷存在本機；雲端能力按需開啟。
- **AI 可負擔**：端側優先、Proxy 配額可控、BYOK 不限 App 配額。
- **免費也能上手**：核心進銷存免費可用（商品上限 30）；Pro 解鎖低庫存、匯入、通訊錄、AI 等進階能力。

---

## 📌 核心功能模組 (Core Features)

本系統跳脫傳統 ERP 厚重的設計思維，聚焦於實用模組與高附加價值的 AI 分析：

1. **📦 商品與庫存管理**
   - 商品建檔：名稱、SKU（可留空自動產生 `AUTO-*`）、國際條碼、**自訂分類**、**庫存量詞**（個 / 件 / 箱 / 自訂等）。
   - **建檔成本規則**：有期初庫存時「單價成本」必填；**期初 = 0（新品）可留空**，第一次進貨確認入庫後寫入真實成本。
   - **多量詞換算**：可設定 `1 箱 = N 個` 等換算表；進銷貨表單支援多量詞輸入，系統自動換算為基準量詞並顯示拆解（如 `3箱+3打` 換行 `(共數量15打)`）。
   - **多量詞換算與定價**：換算區只設倍率；**庫存成本僅基準量詞一個數**（加權平均）。進銷開單預設（選填）可設換算量詞預設進價／各量詞預設定價；當筆成交價在進銷表單填寫，小計為 `Σ(數量×該量詞單價)`；詳情顯示拆解（如 `1箱×140 + 2瓶×15 = 170`）。
   - **分類篩選與管理**：庫存列表 ChoiceChip 篩選；`tune` 圖示開啟分類管理（重命名／刪除，刪除時商品改為未分類）。
   - **條碼掃描**：行動端相機掃描（`mobile_scanner`）；Web 可手動輸入回退。
   - 即時庫存、安全庫存設定；**低庫存警示與一鍵聯絡供應商（Pro）**。
   - **進貨加權平均成本**：確認入庫時依移動加權平均更新商品「單價成本」（無庫存時直接採本次進價）；作廢進貨訂單或刪除進貨流水時反向還原；每筆進貨真實單價仍保留於流水帳。
   - **交易歷史分頁**：流水帳列表、篩選（日期／類型／商品／聯絡人）、分頁載入、進出庫摘要；可 deep link 至全屏流水帳。
   - **JSON 備份**：Schema 遷移、設定頁手動匯出 / 匯入（含 `category`、`unitConversions`、各量詞進價／售價、`unitEntries`；`share_plus` 分享）。

2. **📥 進貨管理（採購入庫）**
   - **訂單驅動流程（作法 A）**：建立 `StockOrder`（待收貨）→ 確認後才寫入流水帳並更新庫存。
   - **進貨單內新增商品**：品項列旁「＋」開啟建檔表單，儲存後自動選入該品項（適合現場進新品，不必先回庫存頁）。
   - 多品項訂單、供應商關聯；多量詞可為箱、瓶分別填**當筆進價**（可從開單預設帶入）；確認收貨後以實際小計換算基準量詞有效均價並更新加權平均成本（SnackBar 提示）；列表點選進入**訂單詳情**（含金額拆解、關聯流水）。
   - **待收貨可取消**；**已完成可刪除**（作廢訂單、反向庫存；不足時夾到 0 並先警告確認）。

3. **📤 銷貨管理（出庫銷售）**
   - 待出庫 → 確認出庫後自動扣減庫存；支援多品項與客戶關聯；多量詞商品可為箱、瓶分別填售價；**訂單詳情**含金額拆解與流水追溯。
   - **待出庫可取消**；**已完成可刪除**（作廢訂單、反向庫存並移除關聯流水）。

4. **👥 聯絡人**
   - 供應商 / 客戶獨立管理；進銷貨 AppBar 快速進入。
   - **裝置通訊錄（Pro）**（`flutter_contacts`）：第三分頁瀏覽通訊錄、一鍵指派為供應商或客戶；已連結聯絡人隨裝置更新同步。

5. **📒 交易流水帳**
   - 庫存頁「交易歷史」分頁；商品卡／聯絡人表單可帶 filter 開啟全屏流水帳。
   - **交易詳情**：品項、數量、單價或金額拆解、關聯聯絡人與訂單跳轉。
   - **調整／損耗可刪除**：無關聯訂單的流水可從詳情刪除並反向庫存；有關聯訂單者提示改刪整張訂單。

6. **📊 儀表板與報表**
   - **今日營收**、**今日毛利**（營收 − 今日進貨支出）、**今日進貨支出**、總庫存（免費）；三張 KPI 卡皆可點擊進入**日報明細**（單日／區間、CSV／PDF 匯出）。
   - **營收／進貨支出明細**：當日交易列表、區間彙總表；點列表項可進 `TransactionDetailScreen`；底部可「在交易歷史查看完整紀錄」。
   - **毛利明細**：單日摘要卡（營收／進貨／毛利）+ 可折疊的當日銷貨／進貨列表；區間模式為每日三欄表 + 區間合計；單日 CSV／PDF 匯出包含摘要、當日銷貨逐筆明細、當日進貨逐筆明細。
   - **低庫存統計與重點庫存清單（Pro）**；與庫存「交易歷史」分頁互補（儀表板偏當日／區間 KPI，交易歷史偏全類型稽核與篩選）。
   - YTD 折線圖、商品毛利長條圖（AI 顧問頁，Pro）；圖表資料於 Cubit 預聚合，串流生成時不重繪圖表。

7. **📋 試算表匯入（Pro）**
   - CSV / Excel 全量驗證 → 原子寫入；庫存 AppBar 進入。

8. **🤖 AI 經營顧問（Pro）**
   - **雙軌推理**：端側優先（`flutter_local_ai` / Gemini Nano）→ 雲端 Gemini（BYOK 或代管 Proxy）；無 Key／離線時降級為本地規則備援。
   - 去識別化 payload、PDF 匯出（含繁中字型）。
   - **多語言洞察**：依 AppBar 所選語系（繁中 / 簡中 / English）生成對應語言的顧問文字；切換語言時自動重新生成。
   - 代管雲端 Proxy（Cloudflare Workers + RevenueCat 驗證 + 每日配額）。

9. **💳 訂閱與帳戶**
   - RevenueCat 三方案（免費 / Pro / 生態系組合包）；**Pro 14 天免費試用**（UI 後備文案；實際天數以商店 metadata 為準）。
   - 訂閱頁方案清單與程式閘門對齊（見下方 [商業模式](#-商業模式與定價策略-monetization)）。
   - **防負評**：扣款前 3 天起每日本機推播（試用結束首次扣款、續訂扣款）；`flutter_local_notifications` + 通知權限檢查；一鍵跳轉商店管理訂閱。

10. **🌐 多語系**
    - 繁體中文 / 簡體中文 / English（AppBar `translate` 選單即時切換）。
    - AI 顧問生成文字同步跟隨所選語言（`responseLanguage` → 端側 / 雲端雙軌；無 AI 時本地規則備援）。

11. **📢 啟動公告**
    - 優先從 Advisor Proxy 拉取遠端公告（`GET /v1/announcements/current`）；無遠端或離線時回退內建 i18n 文案。
    - 可勾選「不再顯示」；Worker 以 `ANNOUNCEMENT_JSON` 下發，更新 `id` 即可推新公告。

12. **⭐ In-App Review 評價引導**
    - 達條件時呼叫 Google Play 原生 In-App Review（`in_app_review`）：首次開啟滿 3 天、確認進／銷達 5 筆、或商品達 10 個（任一即可）。
    - 每次嘗試後冷卻 90 天；設定頁仍保留「到 Google Play 評分」手動入口。

13. **🎬 教學中心**
    - AppBar 左上角 `help_outline` 開啟全屏教學中心（操作總覽、10 個主題、四類分類標籤）。
    - 「操作總覽」簡述常用步驟與必讀說明；各主題可「播放影片」。錄影用逐鏡腳本見 [docs/tutorials/](docs/tutorials/)。影片上架後於 `lib/app/tutorial_video_urls.dart` 設定 YouTube 網址，App 內以外部瀏覽器開啟。

14. **🛡️ Android 發版簽章、混淆與 Play Integrity**
    - `android/app/build.gradle.kts` 已支援 `key.properties` 讀取 release 簽章，缺少檔案時回退 debug 簽章以利本機測試。
    - Release：R8 minify + Dart `--obfuscate --split-debug-info=build/symbols`。
    - 雲端 Advisor Proxy（Android）：App 以 Play Integrity Standard API 取 token，Worker 向 Google `decodeIntegrityToken` 驗證（`PLAY_RECOGNIZED` + `MEETS_DEVICE_INTEGRITY` + requestHash）。詳見 [workers/advisor-proxy/README.md](workers/advisor-proxy/README.md)。
    - Android adaptive icon 資源已更新（`mipmap-anydpi-v26` + `drawable-*` 前景圖）。

---

## 🏗️ 軟體工程架構 (Software Architecture)

本專案嚴格遵循 **Clean Architecture** 並內嵌 **MVVM 模式**（Bloc/Cubit 作為 ViewModel），將系統切分為 Data、Domain、Presentation 三層，確保商業邏輯、資料來源與 UI 完全解耦。

### 📂 專案目錄結構 (Directory Structure)

```text
lib/
├── app/                        # 全域配置（主題、DI、建置旗標、秘密解析）
│   ├── di/                     # get_it 註冊（IO / Web 分流）
│   └── secrets/                # AppSecrets（Gemini / RevenueCat / Proxy URL）
├── data/                       # 資料層
│   ├── datasources/            # Isar、AI 推理、試算表解析、Proxy
│   ├── models/                 # Isar @collection + toDomain()
│   ├── repositories/           # Repository 實作
│   └── export/                 # PDF、使用者檔案匯出分享
├── domain/                     # 純 Dart 業務層
│   ├── entities/
│   ├── repositories/           # 抽象介面
│   ├── subscription/           # 扣款前推播排程（PaymentReminderPlanner）
│   └── usecases/
└── presentation/
    ├── viewmodels/             # Bloc / Cubit（含 TransactionLedger、DeviceContacts）
    ├── navigation/             # 訂單作廢／交易刪除確認流程
    └── views/                  # 14 個 screen + 共用 sheet / dialog

workers/advisor-proxy/          # Cloudflare Worker：Gemini Proxy + RC 驗證 + KV 限流
design/stitch/                  # Stitch UI 原型對照
.agents/skills/                 # 專案 Agent Skills（dev-workflow、ux、performance、motion…）
docs/                           # Play 封閉測試員 onboarding、教學影片腳本
assets/tutorials/               # 教學縮圖等靜態資產（影片托管於 YouTube）
```

---

## 🛠️ 技術棧選型與套件 (Tech Stack & Packages)

| 系統層級 / 模組 | 技術與套件 | 定位 |
| :--- | :--- | :--- |
| **跨平台框架** | Flutter 3.12+ | 行動端優先；Web / Desktop 可延伸 |
| **狀態管理** | `flutter_bloc` | ViewModel；InventoryBloc、AdvisorCubit、SubscriptionCubit |
| **在地資料庫** | `isar_community` | Local-First；Web 使用記憶體 DB 分流 |
| **相依性注入** | `get_it` | Service Locator |
| **圖表** | `fl_chart` | 儀表板 / AI 顧問圖表 |
| **試算表** | `excel` / `csv` / `file_picker` | Pro 批量匯入 |
| **訂閱** | `purchases_flutter` | RevenueCat |
| **本機推播** | `flutter_local_notifications`、`permission_handler` | 試用／續訂扣款前提醒 |
| **AI** | `flutter_local_ai`、`google_generative_ai` | 端側 + 雲端雙軌 |
| **Proxy HTTP** | `http` | `CloudAdvisorProxyDataSource` |
| **PDF** | `pdf` + NotoSansTC 字型 | AI 顧問報告匯出 |
| **條碼** | `mobile_scanner` | 行動端掃描 |
| **通訊錄** | `flutter_contacts` | 裝置通訊錄指派供應商／客戶 |
| **安全儲存** | `flutter_secure_storage` | API 金鑰、公告關閉狀態 |
| **分享** | `share_plus` | 備份 / PDF 分享 |
| **i18n** | `flutter_localizations` + ARB | 繁中 / 簡中 / English |

---

## 💾 資料庫核心實體設計 (Database Entities)

全面遵循**交易流水帳（Transaction Log）**概念：庫存異動經 `StockTransaction` 追溯，進銷貨可走 `StockOrder` + `OrderLine` 訂單流程。

### 1. Product (商品表)

- `id`、`name`、`sku`、`barcode`
- `currentStock`、`safetyStock`
- `unitPrice`：基準單價成本（進貨確認入庫時依**移動加權平均**更新；無庫存時直接採本次進價。建檔時若期初庫存為 0 可留空／為 0；流水帳仍記錄每筆進貨真實單價）
- `sellingPrice`：基準量詞預設售價（可選）
- `stockUnit`：基準庫存量詞（預設「個」）
- `category`：自訂商品分類（可空）
- `unitConversions`：多量詞換算表（`1 {unit} = rateToBase` 個基準量詞；可選 `purchasePrice` / `sellingPrice` 為**開單預設**，非第二套庫存成本）
- `defaultSupplierId`：預設供應商（低庫存 Reorder）
- `targetStock`：低庫存進度條目標（可選）

### 2. StockTransaction (庫存變動紀錄)

- `productId`、`type`（進貨 / 銷貨 / 調整 / 損耗）
- `quantity`、`unitPrice`、`timestamp`
- `unitEntries`：多量詞金額拆解（`[{unit, quantity, unitPrice}, …]`，可選；新資料才有）
- `contactId`：關聯供應商／客戶（可選）
- `orderId`：關聯進銷訂單（可選；確認入庫／出庫後寫入）

### 3. StockOrder + OrderLine (進銷貨訂單)

- 訂單狀態 `pending` → 確認後寫入流水帳；支援多品項；`OrderLine` 含 `unitEntries` 與有效均價 `unitPrice`。
- 待處理訂單可 `cancel`；已完成訂單可 `voidCompleted`（反向庫存、移除關聯流水）。

### 4. Contact (往來對象)

- 供應商 / 客戶；姓名、電話。
- `deviceContactId`：連結裝置通訊錄聯絡人（可選）。

---

## 🤖 AI 核心架構：智慧雙軌分流機制 (Hybrid Inference)

Data 層的 `AiPredictDataSource` 採用端雲雙軌分流推理：

1. **軌道一（優先）**：`flutter_local_ai` → 裝置支援 Gemini Nano 時本地推理，資料不上雲；失敗時自動 fallback 至軌道二。
2. **軌道二（備援）**：雲端 Gemini（BYOK 直連或代管 Proxy）；模型 **`gemini-3.1-flash-lite`**。
3. **降級備援（非 AI 軌道）**：無 API Key、無 Proxy、端側不可用時，走本地規則分析（`local_rules_insight_generator`）；UI 仍會標示為第三種來源，但本質為規則式輸出而非 LLM 推理。

### 防幻覺 Pipeline

- 本地聚合 + 去識別化（`BuildAdvisorAnalyticsPayloadUseCase`）
- `responseLanguage`（BCP-47）注入 prompt；雲端 / 端側 / 本地規則皆依語系輸出
- Server 端 System Prompt（Proxy）或 client 注入
- 串流 UI：`AdvisorCubit` + `TypewriterText`；洞察改為**手動**「產生洞察／重新生成」（進頁與切換語系不自動產生）
- **圖表與串流拆樹**：`BlocSelector` + `RepaintBoundary`；`AdvisorChartLayout` 預聚合軸範圍；`fl_chart` 切換動畫（`chart_motion.dart`）

### 代管雲端 Proxy（Pro 每日 3 次）

Pro 用戶可走 Cloudflare Worker（`workers/advisor-proxy/`）；Gemini 失敗時 **rollback 配額**。同一 Worker 亦提供遠端公告 API。詳見 [PROGRESS.md](PROGRESS.md) 的 Worker URL 與建置參數。

```powershell
copy .secrets.example.json .secrets.json
# 編輯 ADVISOR_API_BASE_URL、SUBSCRIPTION_DEV_PRO=true
flutter run --dart-define-from-file=.secrets.json
```

App 內有設定 **Proxy URL** 時，且未使用 BYOK，預設走代管雲端；BYOK（設定 → API 金鑰）直連 Google、無 App 配額限制。

---

## 🛑 防負評訂閱機制 (Notification & UX Flow)

1. 訂閱頁「絕不產生非預期費用」區塊說明取消方式與扣款前推播承諾（**僅推播，不發郵件**）。
2. 試用結束或續訂扣款前 **3 天起，每天上午 9:00 推播一次**（最多 3 則：剩 3／2／1 天）；由 `PaymentReminderPlanner` + `TrialExpiryReminderRepository` 排程。
3. 觸發條件：`SubscriptionCubit` 在 `isTrial` 或 `willRenew` 且已授權通知時同步排程；關閉提醒、取消續訂或權限被拒則取消。
4. 進入訂閱頁時 `checkNotificationPermissionBeforeExpiry` 檢查權限；遭拒絕則彈出禮貌阻斷對話框。
5. 訂閱頁底部固定「管理訂閱」→ Google Play / App Store deep-link。

> 商店後台試用天數須與 App 文案一致（目前為 **14 天**）；RevenueCat Test Store 商品為 `pro_monthly_14d`（`trial_duration=P14D`）。

---

## 💰 商業模式與定價策略 (Monetization)

### 基礎免費版 ($0)

| 功能 | 說明 |
| :--- | :--- |
| 庫存管理 | 最多 **30** 個庫存品項；達 **24** 項起於庫存頁顯示用量橫幅並提示升級 |
| 進銷存 | 進貨、銷貨、訂單、交易流水帳 |
| 聯絡人 | 供應商／客戶手動管理 |
| 儀表板 | 總覽、今日營收、今日毛利、今日進貨支出 |
| **儀表板 KPI 明細** | 營收／進貨支出／毛利日報（單日列表或摘要、區間表、CSV／PDF 匯出；毛利單日匯出含銷貨／進貨逐筆明細） |
| 備份 | JSON 匯出／匯入（仍受 30 品項上限約束） |

### 專業訂閱版 (NT$ 150 / 月)

| 功能 | 說明 |
| :--- | :--- |
| 無限品項 | 突破 30 品項上限 |
| AI 經營顧問 | 含營收／毛利趨勢圖表；代管雲端每日 3 次，BYOK 無 App 配額 |
| 試算表匯入 | Excel／CSV 批量匯入商品 |
| 裝置通訊錄 | 同步匯入供應商／客戶 |
| 低庫存警示 | 儀表板統計、重點庫存、進貨頁警示橫幅 |
| 免費試用 | **14 天**（須於 Google Play / App Store / RevenueCat 後台同步設定） |

### 生態系大禮包

多款商業工具 App 聯播訂閱同捆（RevenueCat `ecosystem` entitlement）。

### Pro 功能閘門

`SubscriptionState` getter：`canUseAiAdvisor`、`canUseSpreadsheetImport`、`canUseDeviceContactsSync`、`canUseLowStockAlerts`；未訂閱時由 `ProFeatureGate` / `ProLockedScreen` 或鎖定 UI 引導至訂閱頁。封測建置以邀請碼解鎖（預設 `FLOWSTOCK20`）。

### Firebase Analytics（轉換漏斗）

已整合 `firebase_core` + `firebase_analytics`。免費版用量橫幅、達上限攔截、訂閱頁導覽會記錄自訂事件；未設定 Firebase 時自動降級為 NoOp。

**首次設定（已完成）：**

- Firebase 專案：`flowstock-ainventory`
- Android App ID：`1:954943230755:android:6a68c328242d97b2daf296`
- iOS App ID：`1:954943230755:ios:54fa8cb709fd11cedaf296`
- 設定檔：`lib/firebase_options.dart`、`android/app/google-services.json`、`ios/Runner/GoogleService-Info.plist`

若需重新產生設定，請執行：

```powershell
flutterfire configure --project=flowstock-ainventory --platforms=android,ios -y
```

（需已安裝全域 `firebase-tools`：`npm install -g firebase-tools`）

在 [Firebase Console → 專案設定 → 整合](https://console.firebase.google.com/project/flowstock-ainventory/settings/integrations) 確認 **Google Analytics** 已啟用，報表才會完整顯示。

| 事件 | 參數 | 說明 |
|------|------|------|
| `upgrade_cta_tap` | `source` | 點擊升級 CTA |
| `product_limit_reached` | `product_count`, `source` | 達 30 項上限 |
| `product_usage_warning` | `product_count`, `level`, `surface` | 用量橫幅（≥24 項） |
| `subscription_screen_open` | `source` | 開啟訂閱頁 |

**2026-07-09 實機驗證（RFCT314EAHE）**

- 驗證目的：免費版品項上限與轉換事件漏斗（當時 49 → 50 → 51；2026-07-11 起上限改為 30，建議改測 29 → 30 → 31）。
- 建置方式（避免誤用 `SUBSCRIPTION_DEV_PRO=true`）：

```powershell
# 2026-07-09 實測（當時上限 50）
flutter build apk --debug --dart-define=SEED_MOCK_PRODUCTS=49 --dart-define=SUBSCRIPTION_DEV_PRO=false

# 現行上限 30 建議改用
flutter build apk --debug --dart-define=SEED_MOCK_PRODUCTS=29 --dart-define=SUBSCRIPTION_DEV_PRO=false
adb -s RFCT314EAHE uninstall com.flowstock.ainventory
adb -s RFCT314EAHE install build\app\outputs\flutter-apk\app-debug.apk
adb -s RFCT314EAHE shell am start -n com.flowstock.ainventory/.MainActivity
```

- 結果（2026-07-09，當時上限 50）：
  - 啟動後自動種入 49 筆（`SEED_MOCK_PRODUCTS: imported 49 products.`）
  - 49 筆時觸發 `product_usage_warning`
  - 新增第 50 筆成功（無阻擋事件）
  - 嘗試第 51 筆時觸發 `product_limit_reached`（`product_count=50`）並導向 `subscription_screen_open`
  - Firebase 上傳回應為 `Network upload successful ... 204`

**DebugView 空白／破圖排查**

- 若 Firebase Console 可開，但 DebugView 內容空白，請先檢查 DNS：
  - `nslookup analytics.google.com`
  - 若回 `0.0.0.0`，通常是路由器 DNS/擋廣告規則造成，非 App 事件未上報。
- 可改用公共 DNS（`8.8.8.8` / `1.1.1.1`）後 `ipconfig /flushdns` 再重試。

---

## 🚀 快速開始 (Quick Start)

### 環境需求

- Flutter SDK ^3.12、Dart ^3.12
- Android Studio / Xcode（行動端建置）

### 本地執行

```powershell
flutter pub get
copy .secrets.example.json .secrets.json
# 選填：GEMINI_API_KEY、REVENUECAT_API_KEY、ADVISOR_API_BASE_URL
flutter run --dart-define-from-file=.secrets.json
```

建置版本（Debug / Release / 封測）與測試方式詳見下方 [📦 建置版本與測試指南](#-建置版本與測試指南)。

### App 圖示重新產生

```powershell
dart run flutter_launcher_icons
```

### Android release 簽章設定

```powershell
copy android\key.properties.example android\key.properties
# 填入 keyAlias / keyPassword / storeFile / storePassword
```

---

## 📦 建置版本與測試指南

本專案以 **`--dart-define-from-file`** 搭配不同秘密檔區分建置用途。下表涵蓋 Debug、Release 與 Play 封測等建置情境。

### 建置版本總覽

| 版本 | 用途 | 秘密檔 | 典型建置命令 | 產物 |
| :--- | :--- | :--- | :--- | :--- |
| **Debug** | 日常開發、hot reload、本機除錯 | `.secrets.json` | `flutter run --dart-define-from-file=.secrets.json -d <device>` | 裝置上即時執行（不產獨立 APK） |
| **Debug APK** | 快速裝到實機、不需常駐開發連線 | `.secrets.json` | `flutter build apk --debug --dart-define-from-file=.secrets.json` | `build/app/outputs/flutter-apk/app-debug.apk` |
| **Release** | 上架前驗證、Play 內測、正式發布 | `.secrets.pro-build.json` | `flutter build apk --release --obfuscate --split-debug-info=build/symbols --dart-define-from-file=.secrets.pro-build.json` | `app-release.apk` |
| **Play 封測** | Google Play 封閉測試（外部測試員） | `.secrets.closed-test.json` | `.\scripts\build-closed-test.ps1` | `build/app/outputs/bundle/release/app-release.aab` |

#### Debug（開發版）

- RevenueCat 使用 **Test Store** 金鑰（`test_…`）；僅適用 **debug** 建置。
- 可設 `SUBSCRIPTION_DEV_PRO=true` 強制 Pro，不經商店驗證；Proxy 預設送固定 `dev-pro-user`。
- Advisor Proxy 建議指向 **staging**（略過 RC 驗證、方便本機整合）。
- 缺少 `android/key.properties` 時，release 建置會回退 **debug 簽章**（僅限本機，不可上架）。

```powershell
copy .secrets.example.json .secrets.json
# 選填：GEMINI_API_KEY、REVENUECAT_API_KEY、ADVISOR_API_BASE_URL、SUBSCRIPTION_DEV_PRO
flutter run --dart-define-from-file=.secrets.json -d <deviceId>
```

#### 常用實機測試指令（免費版 / Pro）

- **免費版 30 品項上限測試（建議）**

  ```powershell
  # 先清除裝置上的舊資料（只需做一次或版本切換時）
  adb -s <deviceId> shell pm clear com.flowstock.ainventory

  # 免費版：SUBSCRIPTION_DEV_PRO=false，走免費上限邏輯
  flutter run --dart-define-from-file=.secrets.json --dart-define=SUBSCRIPTION_DEV_PRO=false -d <deviceId>
  ```

  - 適用情境：驗證 24/30 上限、`product_usage_warning`、`product_limit_reached` 等免費版行為。
  - 若需要事先種入 29 筆商品，可改用前文「2026-07-09 實機驗證」中的 build + install 流程，再用 `flutter run` 做互動測試。

- **Pro 版功能／訂閱流程測試**

  ```powershell
  # 使用 debug secrets（含 Test Store RC key）
  flutter run --dart-define-from-file=.secrets.json --dart-define=SUBSCRIPTION_DEV_PRO=true -d <deviceId>
  ```

  - 適用情境：快速解鎖 Pro 功能（AI 顧問、試算表匯入、裝置通訊錄、低庫存統計）做 UI / UX 驗證。
  - 僅限本機開發測試；封測與正式版請改用對應 secrets 與商店訂閱流程。

- **AI 顧問每日配額測試（每次開 App 重置 3 次）**

  ```powershell
  # ADVISOR_DEV_RESET_QUOTA=true：每次冷啟動換唯一 App User ID，等同重置 staging 每日 3 次額度
  flutter run --dart-define-from-file=.secrets.json --dart-define=SUBSCRIPTION_DEV_PRO=true --dart-define=ADVISOR_DEV_RESET_QUOTA=true -d <deviceId>
  ```

  - 僅在 `SUBSCRIPTION_DEV_PRO=true` 時生效；且須連 **staging** Proxy（`.secrets.json` 的 `ADVISOR_API_BASE_URL`）。
  - 重置時機為**每次 App 冷啟動**（同一次執行內第 4 次仍會 429）。
  - **勿**寫入 `.secrets.pro-build.json` / 封測 secrets，也**勿**用於 release／production 建置。

#### Release（正式版）

- RevenueCat 使用 **Google Play Public API Key**（`goog_…`）；**release APK/AAB 必須使用此金鑰**。
- `ADVISOR_API_BASE_URL` 指向 **production** Worker；走真實 RC Pro 驗證與每日配額。
- **勿**帶 `CLOSED_TEST_BUILD`、`TESTER_BACKDOOR_ENABLED`、`SUBSCRIPTION_DEV_PRO`、`ADVISOR_DEV_RESET_QUOTA`。
- 需 `android/key.properties` 正式簽章才能上傳 Play。

```powershell
# 自行建立 .secrets.pro-build.json（gitignore），範例：
# { "REVENUECAT_API_KEY": "goog_…", "ADVISOR_API_BASE_URL": "https://flowstock-advisor-proxy.weiying98012.workers.dev" }
flutter build apk --release `
  --obfuscate `
  --split-debug-info=build/symbols `
  --dart-define-from-file=.secrets.pro-build.json
flutter install -d <deviceId>   # 可選：裝到實機驗證
```

> Release 預設啟用 Android R8（`minifyEnabled`）與 Dart `--obfuscate`；符號檔在 `build/symbols/`（已 gitignore），保留以利還原 crash。

#### Play 封測版（封閉測試）

- 建置旗標：`CLOSED_TEST_BUILD=true` + `TESTER_BACKDOOR_ENABLED=true`（腳本與 `.secrets.closed-test.json` 已內含）。
- **UI 與功能與 release 相同**；Pro 功能（AI 顧問、試算表匯入、通訊錄同步、低庫存警示）由測試員在設定頁輸入邀請碼解鎖（預設 `FLOWSTOCK20`）。
- **勿**在封測 secrets 使用 `SUBSCRIPTION_DEV_PRO`。
- Advisor Proxy 建議 **staging**；目前封測版本 **`0.1.0+6`**。

```powershell
copy .secrets.closed-test.example.json .secrets.closed-test.json
# 編輯 goog_… RevenueCat Public Key
.\scripts\build-closed-test.ps1
# 產物：build\app\outputs\bundle\release\app-release.aab
```

測試員說明：[docs/CLOSED_TEST_TESTER_ONBOARDING.md](docs/CLOSED_TEST_TESTER_ONBOARDING.md) · [英文版](docs/CLOSED_TEST_TESTER_ONBOARDING.en.md)

GitHub Actions：`.github/workflows/flutter-release.yml` 可手動觸發，勾選 **Play closed testing build** 產出封測 AAB/APK。

### 該用哪版做什麼測試

| 測試目的 | 建議建置 | 說明 |
| :--- | :--- | :--- |
| 功能開發、UI 調整 | **Debug** + `flutter run` | hot reload、Test Store、`SUBSCRIPTION_DEV_PRO` 可快速驗 Pro 功能 |
| 提交前回歸、CI | **不綁建置** | 跑 `flutter analyze` + `flutter test`（366 項）即可 |
| 訂閱／RevenueCat／Proxy 整合 | **Debug** 或 **Release** | Debug 用 Test Store + staging；上架前須用 Release + `goog_…` + production Proxy |
| 相機、條碼、通訊錄等原生能力 | **Debug APK** 或 **Debug run** | 模擬器不支援的功能需實機 |
| 上架前最終驗證 | **Release** | 與商店環境一致：正式 RC、production Proxy、release 簽章 |
| 外部測試員（Play 封閉測試） | **Play 封測 AAB** | 上傳 Play Console；測試員用邀請碼解鎖 Pro |

> `.secrets.json`、`.secrets.pro-build.json`、`.secrets.closed-test.json` 皆已 gitignore；範本見 `.secrets.example.json` / `.secrets.closed-test.example.json`。

### 測試的兩種方法

#### 方法一：自動化測試（本機／CI）

適用於**每次改碼後、提交 PR 前**的品質閘門，不需裝到實機。

```powershell
flutter analyze
dart run build_runner build --delete-conflicting-outputs
flutter test
```

- Flutter client 目前 **366 項**測試：架構耦合、庫存併發 invariant、訂單 confirm/cancel/作廢競態、加權平均成本、**多量詞獨立定價**、流水帳分頁、**儀表板 KPI 明細（營收／進貨／毛利，含毛利單日匯出逐筆明細）**、**In-App Review 資格／冷卻**、**免費版品項上限 30（匯入／備份／分類搬移）**、AI 雙軌 fallback、圖表預聚合、試算表匯入原子性、訂閱扣款前推播排程等。
- Worker：`cd workers/advisor-proxy && npm test`；staging live E2E 見 [PROGRESS.md § 測試概況](PROGRESS.md#測試概況)。
- CI：`.github/workflows/ci.yml`（analyze + test + Isar 產生檔檢查）。

#### 方法二：實機測試（手動驗證）

適用於**相機掃碼、訂閱流程、觸控體驗、Play 商店整合**等自動化測試無法覆蓋的情境。實機測試有兩種常用做法：

**2a. 開發連線（`flutter run`）** — 日常除錯首選

```powershell
flutter run --dart-define-from-file=.secrets.json -d <deviceId>
```

- 支援 **hot reload / hot restart**，改 UI 或邏輯最快。
- 使用 **Debug** 秘密檔（Test Store、`SUBSCRIPTION_DEV_PRO` 等）。

**2b. 建置後安裝（`build` + `install`）** — 驗證「裝完即用」體驗

```powershell
# Debug：快速裝機
flutter build apk --debug --dart-define-from-file=.secrets.json
flutter install -d <deviceId>

# Release：上架前實機驗證
flutter build apk --release --dart-define-from-file=.secrets.pro-build.json
flutter install -d <deviceId>
```

- 建置完成即退出，**不常駐 log**；適合確認啟動速度、權限流程、與 release 行為一致。
- 封測 AAB 則上傳 Play Console，由測試員從 Play 安裝（見封測 onboarding 文件）。

| | 自動化測試 | 實機 `flutter run` | 實機 `build` + `install` |
| :--- | :--- | :--- | :--- |
| 速度 | 最快（秒～分鐘） | 中（常駐開發連線） | 較慢（需完整編譯） |
| 適用階段 | 每次 commit | 開發中 | 發版前、封測前 |
| Pro／訂閱驗證 | 多為 mock | Debug secrets | Release 或封測 secrets |
| 建議建置 | 無 | Debug | Debug / Release / 封測 |

---

## ⚠️ 開發與部署重要注意事項 (Important Notices)

1. **Google AI Studio**：開發用免費專案**不要綁定信用卡**，以免失去免費額度。
2. **RevenueCat**：多 App 同捆請共用同一 Project，以 Entitlements 區分權限。
3. **Secret 管理**：`.secrets.json`、`.secrets.pro-build.json`、`.secrets.closed-test.json` 已 gitignore；金鑰可改由 App 內「設定 → API 金鑰與整合」安全儲存。
4. **Web 平台**：Isar 不可用（dart2js 限制），使用記憶體 DB；訂閱為 stub。

---

## 🔍 Google Stitch UI 相容性

架構與 Stitch 原型 **100% 對齊**，已完成資料閉環：

- 條碼掃描 ↔ `Product.barcode` / `sku`
- 交易流水帳 ↔ `StockTransaction` + 訂單／聯絡人 filter + 調整／損耗刪除
- 訂單作廢 ↔ `voidCompleted` 反向庫存 + 關聯流水移除
- Reorder ↔ `defaultSupplierId` + `Contact`
- 加權平均成本 ↔ 確認入庫以 `totalAmount / quantity` 更新 `unitPrice`、作廢反向還原
- 多量詞定價 ↔ 換算倍率 + 基準量詞成本；開單預設進價／售價、進銷表單小計、訂單／流水金額拆解
- 儀表板三 KPI ↔ `DailyMetricScreen`（`DashboardDailyMetric`）+ 與 `GetInventorySummaryUseCase` 數字一致
- 進銷貨 AppBar 聯絡人 + 設定圖示
- 訂閱中心 ↔ `SubscriptionCubit` 防負評推播排程 + 方案清單
