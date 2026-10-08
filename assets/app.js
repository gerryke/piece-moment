(function () {
  // ---------------- 文案字典（en / zh 简 / zht 繁 / ja 日） ----------------
  var I18N = {
    "nav.dl":        { en:"Download on the", zh:"前往", zht:"前往", ja:"ダウンロード" },

    "hero.eyebrow":  { en:"Cozy Jigsaw", zh:"片刻：休闲拼图", zht:"片刻：休閒拼圖", ja:"片刻：癒しのジグソーパズル" },
    "hero.h1":       { en:"Antistress puzzles<br><em>for short breaks.</em>", zh:"碎片时间里的<br><em>放松解压。</em>", zht:"零碎時間裡的<br><em>放鬆紓壓。</em>", ja:"すきま時間に<br><em>ストレス解消。</em>" },
    "hero.lead":     { en:"Open it for a short break, a long wait, travel, or bedtime. Browse gentle picture collections, pick a difficulty, and finish at your own pace — no account, no ads, no network needed.", zh:"适合碎片时间、旅途、等待、等餐或睡前打开。浏览柔和的图片收藏，挑选拼图难度，按照自己的节奏慢慢完成——不需登录账号，没有广告，也不需要联网。", zht:"適合零碎時間、旅途、等待、等餐或睡前打開。瀏覽柔和的圖片收藏，挑選拼圖難度，按照自己的節奏慢慢完成——不需登入帳號，沒有廣告，也不需網路連線。", ja:"すきま時間、旅先、待ち時間、食事待ち、寝る前に。やさしい画像コレクションから選び、難易度を決めて、自分のペースで仕上げる——アカウント不要、広告なし、ネット接続も不要。" },
    "hero.m1":       { en:"No ads", zh:"无广告", zht:"無廣告", ja:"広告なし" },
    "hero.m2":       { en:"Offline", zh:"可离线", zht:"可離線", ja:"オフライン" },
    "hero.m3":       { en:"No account", zh:"无需账号", zht:"不需帳號", ja:"アカウント不要" },

    "man.h":         { en:"A cozy jigsaw for travel, waiting, bedtime, and the small breaks in between. <span class='soft'>No scores to chase — just focus, calm, and a picture coming back together.</span>", zh:"一款适合旅途、等待、睡前和各种碎片时间的休闲拼图。<span class='soft'>没有分数要追赶——只有专注、平静，和画面重新完整起来的过程。</span>", zht:"一款適合旅途、等待、睡前和各種零碎時間的休閒拼圖。<span class='soft'>沒有分數要追趕——只有專注、平靜，和畫面重新完整起來的過程。</span>", ja:"旅先、待ち時間、寝る前、日々のすきま時間に開きたい癒しのジグソーパズル。<span class='soft'>競う点数はなく、あるのは集中と、静けさと、絵が戻っていく時間だけ。</span>" },

    "feat.eyebrow":  { en:"Made for calm breaks", zh:"为碎片时间而设计", zht:"為零碎時間而設計", ja:"すきま時間のために" },
    "feat.h":        { en:"Everything here helps you unwind", zh:"这里的一切，都让你轻松下来", zht:"這裡的一切，都讓你輕鬆下來", ja:"少しずつ、気持ちがほどけていく" },

    "c1.h":          { en:"Calm collections", zh:"柔和图库", zht:"柔和圖庫", ja:"やさしい画像コレクション" },
    "c1.p":          { en:"Gentle, themed picture collections — seasons, nature, food, and more. There's always one to match your mood.", zh:"柔和的主题图库——四季、自然、美食……总有一张，合你此刻的心情。", zht:"柔和的主題圖庫——四季、自然、美食……總有一張，合你此刻的心情。", ja:"四季・自然・食べ物など、やさしいテーマの画像コレクション。今の気分に合う一枚がきっと見つかります。" },
    "c2.h":          { en:"Play your way", zh:"你的节奏", zht:"你的節奏", ja:"自分のペースで" },
    "c2.p":          { en:"Easy or challenging grids, two piece shapes. Move each piece without pressure — and your progress saves automatically.", zh:"从简单到挑战的格子，两种拼图形状。不用赶时间，一片一片慢慢放——进度还会自动保存。", zht:"從簡單到挑戰的格子，兩種拼圖形狀。不用趕時間，一片一片慢慢放——進度還會自動保存。", ja:"やさしい難易度から手ごたえのあるものまで、ピースの形は2種類。急がず一片ずつ。進行状況は自動で保存されます。" },
    "c3.h":          { en:"Calm by design", zh:"纯净体验", zht:"純淨體驗", ja:"静けさのための設計" },
    "c3.p":          { en:"No ads, no account, no network needed. Open it anytime, anywhere, and just breathe for a minute.", zh:"没有广告，不需账号，不需联网。随时随地打开，给自己一分钟，好好呼吸。", zht:"沒有廣告，不需帳號，不需連網。隨時隨地打開，給自己一分鐘，好好呼吸。", ja:"広告なし、アカウント不要、ネット接続も不要。いつでもどこでも開いて、ひと息つきましょう。" },
    "c4.h":          { en:"Your own moments", zh:"你自己的记忆", zht:"你自己的記憶", ja:"あなただけの思い出" },
    "c4.p":          { en:"Bring in your own photos. A child's drawing, a favorite meal, a travel snapshot — turn it into a puzzle to return to.", zh:"导入你自己的照片。孩子的一幅画、喜欢的一餐、旅途的一张照片——都能变成一张值得回来拼的拼图。", zht:"匯入你自己的照片。孩子的一幅畫、喜歡的一餐、旅途的一張照片——都能變成一張值得回來拼的拼圖。", ja:"自分の写真を取り込んで。子どもの絵、お気に入りの食事、旅先の一枚を、また戻ってきたくなるパズルに。" },

    "gal.eyebrow":   { en:"A look inside", zh:"进去看看", zht:"進去看看", ja:"中をのぞいてみる" },
    "gal.h":         { en:"Calm to look at. Easy to play.", zh:"看着平静，玩着轻松。", zht:"看著平靜，玩著輕鬆。", ja:"見て落ち着き、気軽に遊べる。" },
    "ipad.eyebrow":  { en:"On iPad", zh:"在 iPad 上", zht:"在 iPad 上", ja:"iPad でも" },
    "ipad.h":        { en:"More room to relax and focus.", zh:"更大的画面，也更容易放松专注。", zht:"更大的畫面，也更容易放鬆專注。", ja:"広い画面で、リラックスして集中。" },

    "bt.eyebrow":    { en:"The little beauty of it", zh:"它细微的美", zht:"它細微的美", ja:"その小さな美しさ" },
    "bt.h":          { en:"Every picture is a small study in texture, color, and calm.", zh:"每一张图，都是一次关于质地、色彩与安宁的小小凝视。", zht:"每一張圖，都是一次關於質地、色彩與安寧的小小凝視。", ja:"どの一枚も、質感と色と静けさをめぐる小さな観察。" },
    "bt.p":          { en:"Piece it together, one calm minute at a time — and keep the finished moment, with a title and a note, if you like.", zh:"一片一片，拼回属于你的平静几分钟——若你愿意，还能为完成的那一刻，留下一个名字和一句话。", zht:"一片一片，拼回屬於你的平靜幾分鐘——若你願意，還能為完成的那一刻，留下一個名字和一句話。", ja:"一片ずつ、落ち着いた数分を組み立てて。よければ、完成したその瞬間に、タイトルとひとことを残せます。" },

    "pf.eyebrow":    { en:"Ranked on the App Store", zh:"曾登上 App Store 付费榜", zht:"曾登上 App Store 付費榜", ja:"App Store 有料ランキング実績" },
    "pf.h":          { en:"Alongside App Store classics on the paid charts.", zh:"在付费榜上，与多款经典游戏同列。", zht:"在付費榜上，與多款經典遊戲同列。", ja:"有料ランキングで、名作ゲームと並びました。" },
    "pf.s1l":        { en:"Paid Family Games", zh:"付费家庭游戏榜", zht:"付費家庭遊戲榜", ja:"有料ファミリー" },
    "pf.s2l":        { en:"Top Paid iPad Apps", zh:"付费 iPad App 榜", zht:"付費 iPad App 榜", ja:"有料 iPad App" },
    "pf.s3n":        { en:"Top 50", zh:"前 50", zht:"前 50", ja:"Top 50" },
    "pf.s3l":        { en:"App Store Family chart", zh:"App Store 家庭榜", zht:"App Store 家庭榜", ja:"ファミリー総合" },
    "pf.note":       { en:"Ranked alongside Monument Valley, Hitman GO, and Rusty Lake.", zh:"与《纪念碑谷》《Hitman GO》《Rusty Lake》等经典同列。", zht:"與《紀念碑谷》《Hitman GO》《Rusty Lake》等經典同列。", ja:"『Monument Valley』『Hitman GO』『Rusty Lake』など名作と並びました。" },
    "pf.cap":        { en:"Paid iPad Apps · App Store", zh:"付费 iPad App 排行 · App Store", zht:"付費 iPad App 排行 · App Store", ja:"有料 iPad App ランキング · App Store" },

    "dl.h":          { en:"Take a little <em>Pieceful Moment.</em>", zh:"给自己，留一个<em>片刻。</em>", zht:"給自己，留一個<em>片刻。</em>", ja:"ほんの少し、<em>片刻</em>を。" },
    "dl.p":          { en:"Use a short break to relax, focus, and piece a picture back together.", zh:"用一小段碎片时间，放松、专注，慢慢拼回眼前的画面。", zht:"用一小段零碎時間，放鬆、專注，慢慢拼回眼前的畫面。", ja:"すきま時間にリラックスして、目の前の絵をゆっくり戻していく。" },

    "f.support":     { en:"Support", zh:"支持", zht:"支援", ja:"サポート" },
    "f.privacy":     { en:"Privacy", zh:"隐私政策", zht:"隱私權政策", ja:"プライバシー" },
    "f.contact":     { en:"Contact", zh:"联系我们", zht:"聯絡我們", ja:"お問い合わせ" },
    "f.copy":        { en:"© 2026 Pieceful Moment. Cozy jigsaw breaks.", zh:"© 2026 Pieceful Moment · 片刻. 碎片时间，放松解压。", zht:"© 2026 Pieceful Moment · 片刻. 零碎時間，放鬆紓壓。", ja:"© 2026 Pieceful Moment · 片刻. すきま時間にストレス解消。" },

    // ---- 隐私政策页 ----
    "pv.back":       { en:"Back to home", zh:"返回首页", zht:"返回首頁", ja:"ホームに戻る" },
    "pv.title":      { en:"Privacy Policy", zh:"隐私政策", zht:"隱私權政策", ja:"プライバシーポリシー" },
    "pv.updated":   { en:"Last updated: October 2026", zh:"最后更新：2026 年 10 月", zht:"最後更新：2026 年 10 月", ja:"最終更新：2026年10月" },
    "pv.lead":      { en:"Pieceful Moment is designed to be calm — and that calm extends to your privacy: no account, no tracking across other apps, and ads appear only when you choose to watch one.", zh:"片刻被设计得很安静——这份安静也包括它对待你隐私的方式：不需要账号，不跨 App 追踪你，广告只在你主动选择观看时才出现。", zht:"片刻拼圖被設計得很安靜——這份安靜也包括它對待你隱私的方式：不需要帳號，不跨 App 追蹤你，廣告只在你主動選擇觀看時才出現。", ja:"Pieceful Moment は静けさを大切にしています——その静けさは、プライバシーの扱いにも表れています。アカウントは不要で、他のアプリをまたいだ追跡も行わず、広告はあなたが自分で見ると選んだときだけ表示されます。" },
    "pv.s1.h":       { en:"Information we collect", zh:"我们收集的信息", zht:"我們收集的資訊", ja:"収集する情報" },
    "pv.s1.p":      { en:"We do not collect personal data ourselves. Pieceful Moment does not require an account, does not ask for your name or email, and has no analytics or servers that store your information. The one exception is advertising, which is provided by Google as described below. Purchases are processed by Apple; we never receive your payment details.", zh:"我们自己不收集个人数据。片刻不需要注册账号，不索取你的姓名或邮箱，没有分析工具，也没有任何存储你信息的服务器。唯一的例外是广告，由 Google 提供，详见下文。购买由 Apple 处理，我们不会收到你的支付信息。", zht:"我們自己不收集個人資料。片刻拼圖不需要註冊帳號，不索取你的姓名或電子郵件，沒有分析工具，也沒有任何儲存你資訊的伺服器。唯一的例外是廣告，由 Google 提供，詳見下文。購買由 Apple 處理，我們不會收到你的付款資訊。", ja:"私たち自身は個人データを収集しません。Pieceful Moment はアカウント登録を必要とせず、氏名やメールアドレスを尋ねることもなく、分析ツールやあなたの情報を保存するサーバーもありません。唯一の例外は広告で、下記のとおり Google が提供します。購入は Apple が処理し、お支払い情報を私たちが受け取ることはありません。" },
    "pv.s2.h":       { en:"Your photos stay on your device", zh:"你的照片只留在你的设备上", zht:"你的照片只留在你的裝置上", ja:"写真は端末内にとどまります" },
    "pv.s2.p":       { en:"When you turn a personal photo into a puzzle, the image is read from your photo library and processed entirely on your device. It is never uploaded to us or anyone else. Granting photo access is optional and only used to let you pick a picture.", zh:"当你把自己的照片做成拼图时，图片只在你的设备上被读取和处理，绝不会上传给我们或任何第三方。是否授权访问照片完全可选，且仅用于让你挑选图片。", zht:"當你把自己的照片做成拼圖時，圖片只在你的裝置上被讀取與處理，絕不會上傳給我們或任何第三方。是否授權存取照片完全可選，且僅用於讓你挑選圖片。", ja:"個人の写真をパズルにするとき、画像は写真ライブラリから読み込まれ、すべて端末内で処理されます。私たちや第三者にアップロードされることは一切ありません。写真へのアクセス許可は任意で、画像を選ぶためだけに使われます。" },
    "pv.s3.h":      { en:"Works offline", zh:"可离线游玩", zht:"可離線遊玩", ja:"オフラインでも遊べます" },
    "pv.s3.p":      { en:"Normal play needs no internet connection. The app does not send your gameplay, photos, or any personal data to us. An internet connection is only needed if you choose to watch an ad.", zh:"正常游玩不需要联网。App 不会向我们发送你的游戏数据、照片或任何个人信息。只有当你选择观看广告时才需要网络。", zht:"正常遊玩不需要連網。App 不會向我們傳送你的遊戲資料、照片或任何個人資訊。只有當你選擇觀看廣告時才需要網路。", ja:"通常のプレイにインターネット接続は必要ありません。アプリがプレイ内容や写真、個人データを私たちに送信することはありません。広告を見ることを選んだときだけ、ネット接続が必要です。" },
    "pv.s7.h":      { en:"Optional ads", zh:"可选的广告", zht:"可選的廣告", ja:"任意で見られる広告" },
    "pv.s7.p":      { en:"You can choose to watch one rewarded ad to unlock a single puzzle. Ads are shown only when you tap that button — never at launch, during play, or between puzzles. Ads are provided by Google AdMob. When an ad is requested, Google may collect and use information such as device identifiers, IP address, approximate location, ad interactions and diagnostics to deliver and measure ads and to prevent fraud. We do not ask for App Tracking Transparency permission and do not use the advertising identifier (IDFA) to track you across other companies' apps and websites. In the European Economic Area, the UK and some other regions, a consent message is shown before ads are requested, and you can change your choice any time from Privacy Options in the app's Settings, when it is shown. Buying the full version removes the ad option. Learn more in the <a href='https://policies.google.com/technologies/ads' target='_blank' rel='noopener'>Google</a> ads policy.", zh:"你可以选择观看一次激励广告，来解锁单张拼图。广告只在你点击该按钮时才出现，不会在启动时、游玩中或拼图之间弹出。广告由 Google AdMob 提供。请求广告时，Google 可能会收集并使用设备标识符、IP 地址、大致位置、广告互动和诊断信息等，用于投放与衡量广告以及防止欺诈。我们不请求 App 跟踪透明度授权，也不使用广告标识符（IDFA）在其他公司的 App 和网站之间追踪你。在欧洲经济区、英国及部分其他地区，请求广告之前会先显示同意说明；你可以随时在 App 设置的“隐私选项”（显示时）中更改选择。购买完整版后将不再提供观看广告的选项。更多信息请参阅 <a href='https://policies.google.com/technologies/ads' target='_blank' rel='noopener'>Google</a> 的广告政策。", zht:"你可以選擇觀看一次獎勵廣告，來解鎖單張拼圖。廣告只在你點擊該按鈕時才出現，不會在啟動時、遊玩中或拼圖之間彈出。廣告由 Google AdMob 提供。請求廣告時，Google 可能會收集並使用裝置識別碼、IP 位址、大致位置、廣告互動與診斷資訊等，用於投放與衡量廣告以及防止詐欺。我們不請求 App 追蹤透明度授權，也不使用廣告識別碼（IDFA）在其他公司的 App 與網站之間追蹤你。在歐洲經濟區、英國及部分其他地區，請求廣告之前會先顯示同意說明；你可以隨時在 App 設定的「隱私選項」（顯示時）中更改選擇。購買完整版後將不再提供觀看廣告的選項。更多資訊請參閱 <a href='https://policies.google.com/technologies/ads' target='_blank' rel='noopener'>Google</a> 的廣告政策。", ja:"1回分の報酬型広告を見ることで、パズル1枚を解放できます。広告は、そのボタンをタップしたときだけ表示され、起動時、プレイ中、パズルの合間に表示されることはありません。広告は Google AdMob が提供します。広告のリクエスト時に、Google は広告の配信・効果測定・不正防止のため、デバイス識別子、IPアドレス、おおよその位置情報、広告の操作履歴や診断情報などを収集・利用する場合があります。当アプリは App Tracking Transparency の許可を求めず、広告用識別子（IDFA）を使って他社のアプリやウェブサイトをまたいであなたを追跡することもありません。欧州経済領域、英国など一部の地域では、広告をリクエストする前に同意メッセージが表示され、表示される場合はアプリの設定にある「プライバシー設定」からいつでも選択を変更できます。フルバージョンを購入すると、広告を見る選択肢は表示されなくなります。詳しくは <a href='https://policies.google.com/technologies/ads' target='_blank' rel='noopener'>Google</a> の広告ポリシーをご覧ください。" },
    "pv.s4.h":       { en:"Children", zh:"儿童", zht:"兒童", ja:"お子さまについて" },
    "pv.s4.p":      { en:"Pieceful Moment is a general-audience puzzle app and is not directed at children under 13. We do not knowingly collect personal information from children. We limit ad content to general-audience ratings, and ads are only shown when a player chooses to watch one.", zh:"片刻是面向一般受众的拼图 App，并非专门面向 13 岁以下儿童。我们不会有意收集儿童的个人信息。我们将广告内容限制在适合一般受众的分级内，且广告只在玩家主动选择观看时才展示。", zht:"片刻拼圖是面向一般大眾的拼圖 App，並非專門面向 13 歲以下兒童。我們不會有意收集兒童的個人資訊。我們將廣告內容限制在適合一般大眾的分級內，且廣告只在玩家主動選擇觀看時才顯示。", ja:"Pieceful Moment は一般向けのパズルアプリで、13歳未満のお子さまを対象としたものではありません。お子さまの個人情報を意図的に収集することはありません。広告の内容は一般向けの区分に限定しており、広告はプレイヤーが自分で見ると選んだときだけ表示されます。" },
    "pv.s5.h":       { en:"Changes to this policy", zh:"政策的变更", zht:"政策的變更", ja:"本ポリシーの変更" },
    "pv.s5.p":       { en:"If this policy ever changes, we'll update this page. Since we don't collect contact information, please check back here for the latest version.", zh:"如果本政策有任何变更，我们会更新此页面。由于我们不收集联系方式，请回到本页查看最新版本。", zht:"如果本政策有任何變更，我們會更新此頁面。由於我們不收集聯絡方式，請回到本頁查看最新版本。", ja:"本ポリシーを変更する場合は、このページを更新します。連絡先情報を収集していないため、最新版はこのページでご確認ください。" },
    "pv.s6.h":       { en:"Contact", zh:"联系我们", zht:"聯絡我們", ja:"お問い合わせ" },
    "pv.s6.p":       { en:"Questions about privacy? Email us at <a href='mailto:keyipeng@gmail.com'>keyipeng@gmail.com</a>.", zh:"关于隐私有任何疑问？请发邮件至 <a href='mailto:keyipeng@gmail.com'>keyipeng@gmail.com</a>。", zht:"關於隱私有任何疑問？請來信 <a href='mailto:keyipeng@gmail.com'>keyipeng@gmail.com</a>。", ja:"プライバシーに関するご質問は <a href='mailto:keyipeng@gmail.com'>keyipeng@gmail.com</a> までご連絡ください。" }
  };

  var HTMLLANG = { en:"en", zh:"zh-Hans", zht:"zh-Hant", ja:"ja" };
  var LANGS = ["en","zh","zht","ja"];

  // ---------------- 语言切换 ----------------
  // 优先级：URL 参数（?lang= 或 #lang）> localStorage 记忆 > 默认英文
  var saved = localStorage.getItem("pm_lang");
  if (LANGS.indexOf(saved) < 0) saved = "en";
  try {
    var qp = new URLSearchParams(location.search).get("lang");
    var hl = (location.hash || "").replace(/^#/, "");
    var urlLang = LANGS.indexOf(qp) >= 0 ? qp : (LANGS.indexOf(hl) >= 0 ? hl : null);
    if (urlLang) saved = urlLang;
  } catch (e) {}

  function apply(lang) {
    document.documentElement.lang = HTMLLANG[lang] || "en";
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var entry = I18N[el.getAttribute("data-i18n")];
      if (entry && entry[lang] != null) el.innerHTML = entry[lang];
    });
    document.querySelectorAll("#lang button").forEach(function (b) {
      b.classList.toggle("on", b.dataset.lang === lang);
    });
    document.querySelectorAll("[data-localized-shot]").forEach(function (img) {
      var shotNumber = Number(img.dataset.localizedShot);
      var version = lang !== "en" && shotNumber <= 3 ? 6 : 5;
      img.src = "assets/img/shots/v8/" + lang + "/" + img.dataset.localizedShot + ".jpg?v=" + version;
    });
    document.querySelectorAll("[data-localized-ipad-shot]").forEach(function (img) {
      img.src = "assets/img/shots/v113-ipad/" + lang + "/" + img.dataset.localizedIpadShot + ".jpg?v=1";
    });
    localStorage.setItem("pm_lang", lang);
  }
  document.querySelectorAll("#lang button").forEach(function (b) {
    b.addEventListener("click", function () { apply(b.dataset.lang); });
  });
  apply(saved);

  // ---------------- 导航吸顶 ----------------
  var nav = document.getElementById("nav");
  if (nav) {
    var onScroll = function () { nav.classList.toggle("solid", window.scrollY > 30); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // ---------------- 滚动揭示 ----------------
  var reduce = window.matchMedia("(prefers-reduced-motion:reduce)").matches;
  var els = document.querySelectorAll(".reveal");
  if (reduce) {
    els.forEach(function (e) { e.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.14 });
    els.forEach(function (e) { io.observe(e); });
  }
})();
