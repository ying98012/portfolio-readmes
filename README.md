# Portfolio READMEs

這個 repo 用於公開展示作品說明文件（README-only）。

- 不包含完整原始碼
- 每個專案提供一個獨立閱讀頁
- 用 GitHub Pages 對外發布
- 支援 Pages CMS 管理（`index.md` + `_projects/*.md`）

## 公開頁面

- https://ying98012.github.io/portfolio-readmes/ai-ops-dashboard/
- https://ying98012.github.io/portfolio-readmes/developer-cms-kit/
- https://ying98012.github.io/portfolio-readmes/vibrant-insight-player/

## 內容結構

- `index.md`：首頁文案與 Hero 區塊設定
- `_projects/*.md`：每個專案 README 展示頁內容
- `_layouts/*.html`：Jekyll 版型
- `.pages.yml`：Pages CMS 欄位設定

## 本機測試（可選）

若你本機有 Ruby + Bundler，可用 Jekyll 測試：

```bash
bundle exec jekyll serve
```

預設網址通常是：

- `http://127.0.0.1:4000/portfolio-readmes/`
