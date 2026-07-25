# Portfolio READMEs

這個 repo 用於公開展示作品說明文件（README-only）。

- 不包含完整原始碼
- 使用 Jekyll（`github-pages`）產生靜態頁面
- 每個專案提供一個獨立閱讀頁
- 透過 GitHub Actions 自動部署到 GitHub Pages
- 支援 Pages CMS 管理（`index.md` + `_projects/*.md`）
- 支援匯入「純 Markdown」到 `_projects/`（無 front matter 也可，依賴 `jekyll-optional-front-matter`）

## 公開頁面

- <https://ying98012.github.io/portfolio-readmes/>
- <https://ying98012.github.io/portfolio-readmes/%E6%A0%A1%E5%9C%92%E6%99%BA%E6%85%A7%E8%81%8A%E5%A4%A9%E5%8A%A9%E6%89%8B/>

## 內容結構

- `index.md`：首頁文案與 Hero 區塊設定（`layout: home`）
- `_projects/*.md`：每個專案 README 展示頁內容
- `_layouts/default.html`：共用 HTML 殼層
- `_layouts/home.html`：首頁專案列表
- `_layouts/project.html`：專案閱讀頁
- `styles.css`：全站樣式（深色閱讀主題）
- `_config.yml`：Jekyll 站點設定（含 `url` / `baseurl`、`projects` collection）
- `.github/workflows/deploy-pages.yml`：Pages 部署 workflow
- `Gemfile` / `Gemfile.lock`：Jekyll 與 GitHub Pages 相依套件
- `.pages.yml`：Pages CMS 欄位設定

## 專案頁（Markdown 匯入）

專案頁已統一為 Markdown 驅動，只要新增或匯入 `_projects/*.md` 即可發布。

網址規則：

- 有 `slug` 的 collection 專案：`/{slug}/`
- 純 Markdown（無 front matter）：`/{檔名不含副檔名}/`

### A. 純 Markdown（推薦，零設定）

把檔案直接放進 `_projects/`，不需要 front matter：

```md
# 專案標題

這裡直接寫 README 內容...
```

系統會自動套用 `layout: project`、產生獨立頁，首頁也會自動出現卡片。

目前專案：`_projects/校園智慧聊天助手.md`（🎓 SchoolGPS - 校園智慧助手）

### B. 結構化欄位（可選）

若你需要「專案摘要 / 技術棧 / 重點功能 / 主站連結」等額外資訊，可使用 front matter（與 `.pages.yml` 對齊）：

```yaml
---
title: 專案名稱
slug: project-slug
updatedAt: 2026-05-31
---
```

可選欄位（不填也可正常顯示）：

- `summary`：專案摘要（首頁卡片與專案頁）
- `projectUrl`：主站作品集專案頁連結
- `techStack`：技術棧（字串陣列）
- `features`：重點功能（字串陣列）

`layout: project` 可由 `_config.yml` defaults 自動套用，通常不必手寫。

## Markdown 模板建議

目前頁面樣式已針對長文 README 優化（以 `校園智慧聊天助手.md` 類型為模板），建議內容結構：

- `#` 專案標題
- `##` 主章節（專案簡介、架構、技術棧、流程、設計原則）
- 表格（技術棧、模組對照）
- 程式區塊（流程與範例）
- `---` 分隔段落

以上元素都會套用現有深色主題樣式（表格、程式碼、引用、標題層級都已優化）。

## 本機開發（可選）

建議使用：

- Ruby `3.3`（與 workflow 一致）
- Bundler `2.5.x`

安裝依賴並啟動：

```bash
bundle install
bundle exec jekyll serve
```

預設網址：

- `http://127.0.0.1:4000/portfolio-readmes/`

## 部署流程

- push 到 `main` 後，會觸發 `Deploy Jekyll site to Pages`
- 也可手動執行 `workflow_dispatch`
- workflow 會以 Ruby `3.3` 執行 `bundle exec jekyll build`，並部署 `_site` 到 GitHub Pages
