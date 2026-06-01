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
index.html              # 营销主页（双语，内联 CSS/JS）
assets/img/             # 图标、截图、主视觉（已压到网页尺寸）
concepts/               # 主视觉方向探索稿（A/B/C 对比，内部参考）
docs/superpowers/specs/ # 设计 spec
```

## 特性

- 中英双语切换（右上角 EN / 中，localStorage 记忆）
- 移动端与桌面端同等优化
- 滚动揭示动效，尊重 `prefers-reduced-motion`
- 字体：Fraunces（标题）+ Hanken Grotesk（正文）+ Noto Serif SC（中文）

## 待替换占位

- App Store 链接：当前用 `https://apps.apple.com/app/id6770564963`（需确认）
- 页脚隐私政策链接、联系邮箱

## 部署

静态托管即可（GitHub Pages / Cloudflare Pages）。连接本仓库后，`main` 分支每次 push 自动构建发布。
