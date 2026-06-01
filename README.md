# Piece Moment — Marketing Site

[Piece Moment（片刻）](https://apps.apple.com/app/id6770564963) 拼图游戏的营销官网。

一个**纯静态单页站**：无框架、无构建步骤，`index.html` + `/assets` 即全部内容。加载快，最契合静态托管，一推送即更新。

## 本地预览

```bash
python3 -m http.server 4321
# 打开 http://localhost:4321/
```

## 结构

```
index.html              # 营销主页
privacy.html            # 隐私政策页（同风格）
assets/style.css        # 共享样式
assets/app.js           # 共享逻辑：i18n 字典 + 导航吸顶 + 滚动揭示
assets/img/             # 图标、截图、主视觉（已压到网页尺寸）
concepts/               # 主视觉方向探索稿（A/B/C 对比，内部参考）
docs/superpowers/specs/ # 设计 spec
```

## 特性

- 四语切换：EN / 简 / 繁 / 日（右上角，localStorage 记忆）。所有文案集中在 `assets/app.js` 的 `I18N` 字典，元素用 `data-i18n="key"` 引用。
- 移动端与桌面端同等优化
- 滚动揭示动效，尊重 `prefers-reduced-motion`
- 字体：Fraunces（拉丁标题）+ Hanken Grotesk（正文）+ Noto Sans JP（日文）+ Noto Serif SC（中文）

## 文案来源

四语文案语气对齐 App Store 上架文案（见 jigsaw 源码仓库 `screenshots/app-store/app-store-listing-copy.md`）。

## 部署

GitHub Pages（项目页），线上地址 **https://gerryke.github.io/piece-moment/**，`main` 分支每次 push 自动发布。仓库刻意放在子路径而非根域名，方便将来不同 App 各占一个子文件夹。

### 语言直达

URL 追加 `?lang=zh`（简）/ `?lang=zht`（繁）/ `?lang=ja`（日）可直达指定语言，优先级高于浏览器记忆。用于 App Store Connect 各语言 Marketing URL。
