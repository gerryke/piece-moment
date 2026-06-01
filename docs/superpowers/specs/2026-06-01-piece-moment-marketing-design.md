# Piece Moment 营销官网 · 设计 Spec

日期：2026-06-01
负责人：Gerry Ke
状态：方向已确认，进入实现

## 1. 目标与背景

为已上架 App Store 的拼图游戏 **Piece Moment**（中文名「片刻」）做一个营销落地页。

- **主 CTA**：引导下载 App Store
- **核心体验目标**：访客一进来就感到放松、舒服、被治愈——零销售压迫感
- **语言**：中英双语，可切换（默认英文，与 App/App Store 一致）
- **设备**：桌面与手机端体验同等重要（移动优先验证）
- **关系**：本营销站是设计主导；现有 support 站（github.io/piece-moment-support）后续将改版跟随本站风格，最终同域名下两个入口。

## 2. 品牌与调性（既有，沿用）

- 名称：**Piece Moment** ／ 中文 **片刻**
- 副标题：Relaxing Jigsaw Puzzles ／ 轻松拼一张图
- 标语：*One picture. One moment.* / *Slow down. One piece at a time.*
- 卖点：无广告、离线可玩、慢节奏、治愈、可导入自己的照片
- 视觉识别：陶瓷质感双拼图图标；奶白/雾霾蓝/灰绿低饱和色系；柔和渐变；大量留白；优雅衬线标题
- App 主 ID：6770564963（App Store 链接待最终确认）

## 3. 视觉方向（已确认）

**以方向 C「拼合·此刻」为主结构，融合 A 的留白与优雅衬线、B 的唯美大图。**

- 第一屏（Hero）促转化：左文案 + 右真机画面 + 利益点（无广告/离线）+ App Store 按钮
- 往下滚动给美感：用 B 的大图与诗意文案营造氛围
- 背景：A 式干净留白渐变（浅蓝→暖白），非满版照片
- 字体：**Fraunces**（优雅光学衬线，标题）+ **Hanken Grotesk**（正文）+ Noto Serif SC（中文）

## 4. 页面结构（单页滚动）

| # | 区块 | 内容 |
|---|---|---|
| 0 | 顶部导航 | Piece Moment logo · 中/EN 切换 · App Store 按钮（滚动后浮现/吸顶） |
| 1 | Hero | 衬线大标题 + 一句 lead + CTA + 利益点；右侧真机（画廊截图），漂浮陶瓷碎片 |
| 2 | 主张 manifesto | 大留白一句话定位（"a relaxing puzzle for the small quiet spaces in your day"） |
| 3 | 特性 features | 3–4 张卡：四季画廊 / 多难度·三种形状 / 无广告·离线 / 导入自己的照片 |
| 4 | 截图画廊 | 真机竖版截图横向滚动（02/03/04/06/07/08） |
| 5 | 内容之美 | B 式唯美大图 banner + 诗意短句（强调"美"与"自己的记忆"） |
| 6 | 下载 CTA | 再一次大按钮（后续可加扫码二维码） |
| 7 | 页脚 | 版权 / 隐私 / Support 链接 / 联系邮箱 |

## 5. 技术与部署

- **纯静态站**：单个 `index.html` + `/assets`（图片、内联 CSS/JS）。无构建步骤、无框架，加载快，最契合静态托管。
- **i18n**：每个可翻译元素带 `data-en` / `data-zh`，JS 切换 `textContent`，`localStorage` 记忆选择。
- **无障碍/动效**：尊重 `prefers-reduced-motion`；语义化标签；图片 alt。
- **部署**：先 localhost 验证 → 新建 GitHub repo → 自动部署（Cloudflare Pages 或 GitHub Pages，与 support 同域名归并由后续决定）→ push 即更新。
- **图片**：原始大图（5–10MB）已用 sips 压到网页尺寸；整站资源 < 3MB。

## 6. 范围之外（YAGNI）

- 后端、表单、分析、A/B（已上架，主 CTA 是下载，无需邮件候补）
- 多页路由（单页足够）
- 扫码二维码：v1 先不做，待 App Store 链接确认后作为轻量增量加入

## 7. 待确认

1. App Store 真实链接（暂用 `https://apps.apple.com/app/id6770564963` 占位）
2. 默认语言（暂定英文）
3. 页脚联系邮箱与隐私政策链接
