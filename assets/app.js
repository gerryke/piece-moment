(function () {
  // ---------------- 文案字典（en / zh 简 / zht 繁 / ja 日） ----------------
  var I18N = {
    "nav.dl":        { en:"Download on the", zh:"前往", zht:"前往", ja:"ダウンロード" },

    "hero.eyebrow":  { en:"Relaxing Jigsaw Puzzles", zh:"轻松拼一张图", zht:"放鬆療癒的拼圖", ja:"静かに楽しむ癒しのパズル" },
    "hero.h1":       { en:"Slow down.<br>One piece <em>at&nbsp;a&nbsp;time.</em>", zh:"慢下来，<br>一次<em>拼一张图。</em>", zht:"慢一點，<br>一次<em>拼一張圖。</em>", ja:"ゆっくりと。<br>一片ずつ、<em>自分のペースで。</em>" },
    "hero.lead":     { en:"Choose a picture, relax for a moment, and enjoy putting it back together at your own pace. No ads. No network. Just a quiet little break in your day.", zh:"选一张喜欢的图片，慢慢拼一会儿。没有广告，无需网络——只是给一天里的自己，留一个安静的片刻。", zht:"選一張喜歡的圖片，慢慢拼一會兒。沒有廣告，不需網路——只是給一天裡的自己，留一個安靜的片刻。", ja:"好きな写真を選んで、ゆっくり組み立てる。広告なし、ネット接続も不要。一日の中の、静かなひとときを。" },
    "hero.m1":       { en:"No ads", zh:"无广告", zht:"無廣告", ja:"広告なし" },
    "hero.m2":       { en:"Offline", zh:"可离线", zht:"可離線", ja:"オフライン" },
    "hero.m3":       { en:"Free to start", zh:"免费开始", zht:"免費開始", ja:"無料で開始" },

    "man.h":         { en:"A relaxing jigsaw puzzle for the small, quiet spaces in your day. <span class='soft'>Not about speed or scores — just the calm of watching a picture come back together.</span>", zh:"一款安静放松的拼图，陪你度过一天里那些小小的空隙。<span class='soft'>无关速度，无关分数——只享受画面重新完整起来的那份平静。</span>", zht:"一款安靜放鬆的拼圖，陪你度過一天裡那些小小的空隙。<span class='soft'>無關速度，無關分數——只享受畫面重新完整起來的那份平靜。</span>", ja:"忙しい一日の、小さな静かなすき間のためのパズル。<span class='soft'>速さも点数も関係なく、ただ絵が元に戻っていく穏やかさを。</span>" },

    "feat.eyebrow":  { en:"Made to feel calm", zh:"为放松而设计", zht:"為放鬆而設計", ja:"心が落ち着く設計" },
    "feat.h":        { en:"Everything here slows you down", zh:"这里的一切，都让你慢下来", zht:"這裡的一切，都讓你慢下來", ja:"ここにあるすべてが、あなたをゆっくりに" },

    "c1.h":          { en:"Calm collections", zh:"柔和图库", zht:"柔和圖庫", ja:"やさしい画像コレクション" },
    "c1.p":          { en:"Gentle, themed picture collections — seasons, nature, food, and more. There's always one to match your mood.", zh:"柔和的主题图库——四季、自然、美食……总有一张，合你此刻的心情。", zht:"柔和的主題圖庫——四季、自然、美食……總有一張，合你此刻的心情。", ja:"四季・自然・食べ物など、やさしいテーマの画像コレクション。今の気分に合う一枚がきっと見つかります。" },
    "c2.h":          { en:"Play your way", zh:"你的节奏", zht:"你的節奏", ja:"自分のペースで" },
    "c2.p":          { en:"Easy or challenging grids, three piece shapes. Move each piece without pressure — your pace, your rules.", zh:"从简单到挑战的格子，三种拼图形状。不用赶时间，一片一片慢慢放——你的节奏，你说了算。", zht:"從簡單到挑戰的格子，三種拼圖形狀。不用趕時間，一片一片慢慢放——你的節奏，你說了算。", ja:"やさしい難易度から手ごたえのあるものまで、ピースの形は3種類。急がず一片ずつ、あなたのペースで。" },
    "c3.h":          { en:"Calm by design", zh:"纯净体验", zht:"純淨體驗", ja:"静けさのための設計" },
    "c3.p":          { en:"No ads. No network needed. No rush. Open it anytime, anywhere, and just breathe for a minute.", zh:"没有广告，无需联网，不必着急。随时随地打开，给自己一分钟，好好呼吸。", zht:"沒有廣告，不需連網，不必著急。隨時隨地打開，給自己一分鐘，好好呼吸。", ja:"広告なし、ネット接続不要、急ぐ必要もなし。いつでもどこでも開いて、ひと息つきましょう。" },
    "c4.h":          { en:"Your own moments", zh:"你自己的记忆", zht:"你自己的記憶", ja:"あなただけの思い出" },
    "c4.p":          { en:"Bring in your own photos. A child's drawing, a favorite meal, a travel snapshot — turn it into a puzzle to return to.", zh:"导入你自己的照片。孩子的一幅画、喜欢的一餐、旅途的一张照片——都能变成一张值得回来拼的拼图。", zht:"匯入你自己的照片。孩子的一幅畫、喜歡的一餐、旅途的一張照片——都能變成一張值得回來拼的拼圖。", ja:"自分の写真を取り込んで。子どもの絵、お気に入りの食事、旅先の一枚を、また戻ってきたくなるパズルに。" },

    "gal.eyebrow":   { en:"A look inside", zh:"进去看看", zht:"進去看看", ja:"中をのぞいてみる" },
    "gal.h":         { en:"Quiet to look at. Quiet to play.", zh:"看着安静，玩着也安静。", zht:"看著安靜，玩著也安靜。", ja:"見ても、遊んでも、静か。" },

    "bt.eyebrow":    { en:"The little beauty of it", zh:"它细微的美", zht:"它細微的美", ja:"その小さな美しさ" },
    "bt.h":          { en:"Every picture is a small study in texture, color, and calm.", zh:"每一张图，都是一次关于质地、色彩与安宁的小小凝视。", zht:"每一張圖，都是一次關於質地、色彩與安寧的小小凝視。", ja:"どの一枚も、質感と色と静けさをめぐる小さな観察。" },
    "bt.p":          { en:"Piece it together, one quiet minute at a time — and keep the finished moment, with a title and a note, if you like.", zh:"一片一片，拼回属于你的安静几分钟——若你愿意，还能为完成的那一刻，留下一个名字和一句话。", zht:"一片一片，拼回屬於你的安靜幾分鐘——若你願意，還能為完成的那一刻，留下一個名字和一句話。", ja:"一片ずつ、静かな数分を組み立てて。よければ、完成したその瞬間に、タイトルとひとことを残せます。" },

    "dl.h":          { en:"Take a little <em>Piece Moment.</em>", zh:"给自己，留一个<em>片刻。</em>", zht:"給自己，留一個<em>片刻。</em>", ja:"ほんの少し、<em>Piece&nbsp;Moment&nbsp;を。</em>" },
    "dl.p":          { en:"One picture at a time. Free to start on the App Store.", zh:"一次拼一张图。在 App Store 免费开始。", zht:"一次拼一張圖。在 App Store 免費開始。", ja:"一度に一枚ずつ。App Store で無料で始められます。" },

    "f.support":     { en:"Support", zh:"支持", zht:"支援", ja:"サポート" },
    "f.privacy":     { en:"Privacy", zh:"隐私政策", zht:"隱私權政策", ja:"プライバシー" },
    "f.contact":     { en:"Contact", zh:"联系我们", zht:"聯絡我們", ja:"お問い合わせ" },
    "f.copy":        { en:"© 2026 Piece Moment. One picture. One moment.", zh:"© 2026 Piece Moment · 片刻. 一次，拼一张图。", zht:"© 2026 Piece Moment · 片刻拼圖. 一次，拼一張圖。", ja:"© 2026 Piece Moment. 一度に一枚、ひとときを。" },

    // ---- 隐私政策页 ----
    "pv.back":       { en:"Back to home", zh:"返回首页", zht:"返回首頁", ja:"ホームに戻る" },
    "pv.title":      { en:"Privacy Policy", zh:"隐私政策", zht:"隱私權政策", ja:"プライバシーポリシー" },
    "pv.updated":    { en:"Last updated: June 2026", zh:"最后更新：2026 年 6 月", zht:"最後更新：2026 年 6 月", ja:"最終更新：2026年6月" },
    "pv.lead":       { en:"Piece Moment is designed to be calm — and that includes how it treats your privacy. The short version: we don't collect your personal data, we don't show ads, and the app works fully offline.", zh:"片刻被设计得很安静——这也包括它对待你隐私的方式。一句话版本：我们不收集你的个人数据，不展示广告，App 完全可以离线使用。", zht:"片刻拼圖被設計得很安靜——這也包括它對待你隱私的方式。一句話版本：我們不收集你的個人資料，不顯示廣告，App 完全可以離線使用。", ja:"Piece Moment は静けさを大切にしています。それはプライバシーの扱いも同じです。ひとことで言えば、個人データを収集せず、広告も表示せず、アプリは完全にオフラインで動作します。" },
    "pv.s1.h":       { en:"Information we collect", zh:"我们收集的信息", zht:"我們收集的資訊", ja:"収集する情報" },
    "pv.s1.p":       { en:"None. Piece Moment does not require an account, does not ask for your name or email, and does not collect analytics or usage tracking. We have no servers that store your information.", zh:"没有。片刻不需要注册账号，不索取你的姓名或邮箱，也不收集分析或使用行为追踪。我们没有任何存储你信息的服务器。", zht:"沒有。片刻拼圖不需要註冊帳號，不索取你的姓名或電子郵件，也不收集分析或使用行為追蹤。我們沒有任何儲存你資訊的伺服器。", ja:"ありません。Piece Moment はアカウント登録を必要とせず、氏名やメールアドレスを尋ねることもなく、分析や利用状況のトラッキングも行いません。あなたの情報を保存するサーバーもありません。" },
    "pv.s2.h":       { en:"Your photos stay on your device", zh:"你的照片只留在你的设备上", zht:"你的照片只留在你的裝置上", ja:"写真は端末内にとどまります" },
    "pv.s2.p":       { en:"When you turn a personal photo into a puzzle, the image is read from your photo library and processed entirely on your device. It is never uploaded to us or anyone else. Granting photo access is optional and only used to let you pick a picture.", zh:"当你把自己的照片做成拼图时，图片只在你的设备上被读取和处理，绝不会上传给我们或任何第三方。是否授权访问照片完全可选，且仅用于让你挑选图片。", zht:"當你把自己的照片做成拼圖時，圖片只在你的裝置上被讀取與處理，絕不會上傳給我們或任何第三方。是否授權存取照片完全可選，且僅用於讓你挑選圖片。", ja:"個人の写真をパズルにするとき、画像は写真ライブラリから読み込まれ、すべて端末内で処理されます。私たちや第三者にアップロードされることは一切ありません。写真へのアクセス許可は任意で、画像を選ぶためだけに使われます。" },
    "pv.s3.h":       { en:"No network required", zh:"无需网络", zht:"不需網路", ja:"ネット接続は不要" },
    "pv.s3.p":       { en:"Normal play needs no internet connection. The app does not send your gameplay, photos, or any personal data over the network.", zh:"正常游玩不需要联网。App 不会通过网络发送你的游戏数据、照片或任何个人信息。", zht:"正常遊玩不需要連網。App 不會透過網路傳送你的遊戲資料、照片或任何個人資訊。", ja:"通常のプレイにインターネット接続は必要ありません。アプリがプレイ内容や写真、個人データをネットワーク経由で送信することはありません。" },
    "pv.s4.h":       { en:"Children", zh:"儿童", zht:"兒童", ja:"お子さまについて" },
    "pv.s4.p":       { en:"Piece Moment is family-friendly: no ads, no purchases that target children, and no data collection — making it safe for players of all ages.", zh:"片刻适合全家使用：没有广告、没有针对儿童的购买项目、也不收集数据——适合各个年龄段的玩家。", zht:"片刻拼圖適合全家使用：沒有廣告、沒有針對兒童的購買項目，也不收集資料——適合各個年齡層的玩家。", ja:"Piece Moment は家族みんなで楽しめます。広告や子ども向けの課金はなく、データ収集も行わないため、あらゆる年齢の方が安心して遊べます。" },
    "pv.s5.h":       { en:"Changes to this policy", zh:"政策的变更", zht:"政策的變更", ja:"本ポリシーの変更" },
    "pv.s5.p":       { en:"If this policy ever changes, we'll update this page. Since we don't collect contact information, please check back here for the latest version.", zh:"如果本政策有任何变更，我们会更新此页面。由于我们不收集联系方式，请回到本页查看最新版本。", zht:"如果本政策有任何變更，我們會更新此頁面。由於我們不收集聯絡方式，請回到本頁查看最新版本。", ja:"本ポリシーを変更する場合は、このページを更新します。連絡先情報を収集していないため、最新版はこのページでご確認ください。" },
    "pv.s6.h":       { en:"Contact", zh:"联系我们", zht:"聯絡我們", ja:"お問い合わせ" },
    "pv.s6.p":       { en:"Questions about privacy? Email us at <a href='mailto:keyipeng@gmail.com'>keyipeng@gmail.com</a>.", zh:"关于隐私有任何疑问？请发邮件至 <a href='mailto:keyipeng@gmail.com'>keyipeng@gmail.com</a>。", zht:"關於隱私有任何疑問？請來信 <a href='mailto:keyipeng@gmail.com'>keyipeng@gmail.com</a>。", ja:"プライバシーに関するご質問は <a href='mailto:keyipeng@gmail.com'>keyipeng@gmail.com</a> までご連絡ください。" }
  };

  var HTMLLANG = { en:"en", zh:"zh-Hans", zht:"zh-Hant", ja:"ja" };
  var LANGS = ["en","zh","zht","ja"];

  // ---------------- 语言切换 ----------------
  var saved = localStorage.getItem("pm_lang");
  if (LANGS.indexOf(saved) < 0) saved = "en";

  function apply(lang) {
    document.documentElement.lang = HTMLLANG[lang] || "en";
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var entry = I18N[el.getAttribute("data-i18n")];
      if (entry && entry[lang] != null) el.innerHTML = entry[lang];
    });
    document.querySelectorAll("#lang button").forEach(function (b) {
      b.classList.toggle("on", b.dataset.lang === lang);
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
