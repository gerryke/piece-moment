# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Marketing + privacy site for **Piece Moment**（中文「片刻」），一款**付费**（非免费）的 iOS 拼图游戏。游戏源码在另一个仓库 `/Users/keyipeng/Dev/jigsaw_test`（Swift/UIKit）。本仓库只是它的官网。

纯静态站，**无框架、无构建步骤、无依赖**。`index.html` + `privacy.html` + 语言分享页 + `assets/`（共享 `style.css`、`app.js`、图片）即全部。

## 本地预览

```bash
python3 -m http.server 4321
# http://localhost:4321/
```
没有 lint / test / build。改完直接刷新浏览器即可。

## 部署

- GitHub Pages，仓库 `gerryke/piece-moment`（项目页），线上 **https://gerryke.github.io/piece-moment/**，`main` 分支 push 即自动发布（约 30–60s）。
- 刻意放在 `/piece-moment/` 子路径而非根域名（根域名留给将来的其他 App）。**因此站内所有路径必须是相对路径**（`assets/...`、`privacy.html`），不能用 `/assets/...` 这种绝对路径，否则换到子路径会 404。绝对 URL 只用于跨站链接和 og:image。
- **缓存破除**：`style.css` / `app.js` / 复用文件名的图片（如 `rank-chart.jpg`）在引用时带 `?v=N` 版本号。改了这些文件后**把版本号 +1**，否则浏览器/CDN 会继续吃旧缓存（症状：用户说"没变化"）。

## i18n 架构（改文案前必读）

四语：`en` / `zh`(简) / `zht`(繁) / `ja`(日)。

- **唯一文案真源是 `assets/app.js` 里的 `I18N` 字典**。每条 key 含 `{en, zh, zht, ja}` 四个值（值可含 HTML，会用 `innerHTML` 注入）。
- 页面元素用 `data-i18n="key"` 引用；`app.js` 在加载时按当前语言替换内容、切换 `<html lang>`、高亮语言按钮。
- 改文案 = 改字典对应 key 即可，两个页面自动生效。**不要**在 HTML 里散落硬编码译文。
- HTML 里 `data-i18n` 元素内的文字是**英文静态兜底**（给爬虫 / 关闭 JS 的访客看）。改某条英文文案时，**字典和该处兜底两边都要改**，保持一致。
- 语言优先级：URL 参数 `?lang=zh|zht|ja`（或 `#zh`）> `localStorage` 记忆 > 默认 `en`。

## 社交分享 / 微信预览（关键陷阱）

微信、Twitter 等爬虫**不执行 JS、不看页面语言切换**，只读 HTML 里写死的 `<meta>` / `og:` 标签。因此：

- 根 `index.html` 的 og 标签是**英文**（英文分享用）。
- `zh.html` / `zht.html` / `ja.html` 是**轻量分享入口页**：头部是对应语言的静态 `og:title/description/locale` + `og:image`（爬虫读到正确语言），`<body>` 一句 JS `location.replace('./?lang=XX')` 把真人跳到对应语言正式页。
- **改首页标题/简介文案时，记得同步改这 4 个文件的 og 标签**（它们不走 i18n 字典，是各自写死的）。
- App Store Connect 各语言的 Marketing/Support URL 也用这套带 `?lang=` 或 `.html` 的链接区分语言。

## 内容约束

- **这是付费 App**：任何文案都不能出现 "Free / 免费 / 无料で始" 之类暗示免费下载的措辞（卖点用「无广告 / 无账号 / 可离线」）。
- 四语文案的语气对齐 App Store 上架文案：`/Users/keyipeng/Dev/jigsaw_test/screenshots/app-store/app-store-listing-copy.md`（含简/繁/日官方描述）。
- 排名成就（付费榜 #7 等）如实表述为"曾登上"的过去战绩，数字来自 App Store 真实截图。

## 图片

源图（App 截图、品牌图）来自 `jigsaw_test/screenshots/`，体积大（5–10MB）。放进本站前一律用 `sips` 压到网页尺寸放入 `assets/img/`。社交缩略图 `assets/img/share.jpg` 为 1200×630。

## 设计基调

安静、留白、低饱和（奶白/雾霾蓝/灰绿）、零销售压迫感。字体 Fraunces（拉丁标题）+ Hanken Grotesk（正文）+ Noto Sans JP（日）+ Noto Serif SC（中），均走 Google Fonts。动效尊重 `prefers-reduced-motion`。设计决策记录在 `docs/superpowers/specs/`。

## 其他

- `concepts/` 是早期主视觉 A/B/C 方向对比稿，仅供内部参考（也一并部署了）。
- 提交信息按需附 `Co-Authored-By` 行；不要主动 commit/push，除非是在执行用户明确要求的"上线/部署"动作。
