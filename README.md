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
marketing-assets/       # App Store 上架图、视频制作素材、官网图片源素材
concepts/               # 主视觉方向探索稿（A/B/C 对比，内部参考）
docs/superpowers/specs/ # 设计 spec
```

## 特性

- 四语切换：EN / 简 / 繁 / 日（右上角，localStorage 记忆）。所有文案集中在 `assets/app.js` 的 `I18N` 字典，元素用 `data-i18n="key"` 引用。
- 移动端与桌面端同等优化
- 滚动揭示动效，尊重 `prefers-reduced-motion`
- 字体：Fraunces（拉丁标题）+ Hanken Grotesk（正文）+ Noto Sans JP（日文）+ Noto Serif SC（中文）

## 文案来源

四语文案语气对齐 App Store 上架文案（见本仓库 `marketing-assets/app-store/app-store-listing-copy.md`）。

## 上架与宣传素材

`marketing-assets/` 是 Piece Moment 后续营销素材的主目录：

- `marketing-assets/app-store/`：App Store 上架叙事图、横版图、上架文案，以及当前官网截图的高分辨率源图。
- `marketing-assets/app-store/upload-ready/`：当前 App Store 叙事图的 6.9 寸 iPhone 原始上传图（1320×2868）。
- `marketing-assets/upload-ready/`：6.9 寸 iPhone 原始上传图（1320×2868），不放旧的加工导出版。
- `marketing-assets/ipad-upload-ready/`：13 寸 iPad 原始上传图（2064×2752），不放旧的加工导出版。
- `marketing-assets/legacy-1284x2778/`：旧的 1284×2778 加工导出版，仅作归档，不作为当前上传源。
- `marketing-assets/legacy-ipad-2048x2732/`：旧的 2048×2732 iPad 图，仅作归档，不作为当前上传源。
- `marketing-assets/current-used/`：当前线上官网和当前 App Store 素材基线，方便新版重做时对照。
- `marketing-assets/next-version-prep/`：新版上架图与宣传视频筹备区，`sources/` 放候选原图，`drafts/` 放英文营销展示图草稿。

官网实际加载的图片仍放在 `assets/img/`，并压到网页尺寸；从 `marketing-assets/` 复用文件生成网页图时，记得同步更新引用版本号（例如 `?v=5`）。

当前 App Store 与营销素材尺寸固定为：

- iPhone：6.9 寸竖图，1320×2868。
- iPad：13 寸竖图，2064×2752。
- App preview / 宣传视频：按同一设备族输出，iPhone 用 6.9 寸竖版比例，iPad 用 13 寸竖版比例。
- 新版营销展示图：统一英文，字体风格跟官网一致（Fraunces 标题 + Hanken Grotesk 正文），屏幕图裁掉状态栏等多余系统信息。

## 部署

GitHub Pages（项目页），线上地址 **https://gerryke.github.io/piece-moment/**，`main` 分支每次 push 自动发布。仓库刻意放在子路径而非根域名，方便将来不同 App 各占一个子文件夹。

### 语言直达

URL 追加 `?lang=zh`（简）/ `?lang=zht`（繁）/ `?lang=ja`（日）可直达指定语言，优先级高于浏览器记忆。用于 App Store Connect 各语言 Marketing URL。
