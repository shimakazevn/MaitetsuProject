# Unification U13b — §1 OPEN T67–T81 (E2): thuật ngữ mở + SFX chụt/rộp/Phập — REVIEW

## 1. Phạm vi

Batch U13b áp các mục §1 OPEN đã QUYẾT của coordinator (22/11 ~12:25, theo uỷ quyền Hieu): T67, T68, T69, T70, T71, T72, T73, T74, T75, T77, T78 (a/b), T79, T81 — **13 mục**. T76 (parked, chờ Hieu) và T80 (parked, chờ kiểm tra trong game B19) KHÔNG đụng. Nguồn: báo cáo điều tra E2 (`investigation-open-terminology-t67-t81-REPORT.md`, 6.021 dòng) + `UNIFICATION-LIST.md` §0 + §1 (trích dẫn trong list SAI một phần — §2 liệt kê hiệu chỉnh; tin E2, không tin list).

**Kết quả: 304 dòng sửa** (T68 6, T71 11, T72 18, T73 3, T74 1, T75 71, T77 188, T78a 21, T78b 2, T79 1; T67/T69/T70/T81 0 dòng — đã đúng, chỉ kiểm chứng). **16 dòng GHÉP** với batch đã gộp (old_vn = fix đã gộp, không cộng lại vào tổng) → **288 dòng mới**. Chuỗi tổng sau đợt này: **100 mục / 2.686 dòng** (cơ sở 87/2.398 + 13 mục mới + 288 dòng mới — xem snippet).

Nguồn old_vn của 304 dòng sửa: CSV3 194 / moan 41 / audit 30 / audit(norm) 13 / moan(norm) 10 / unification đã gộp 16 (s3-moan-dialogue 6, s3-sfx-counting 5, s3-fa-fu 3, t1-ohimitera-00-02 1, t1-ohito-t2-06-11 1).

## 2. Hiệu chỉnh (list sai, nhãn E2 đảo, số đếm T77)

- **List sai file T74**: list ghi 日々姫h2 — đúng là **凪h2_おとなの水着 1766** (E2 §0).
- **Nhãn E2 đảo ở T78**: trong file báo cáo E2, bảng mang nhãn T78a là ぬぶ (10 dòng), bảng T78b là ずぶ (25 dòng) — ngược với quyết của coordinator. Toàn bộ đợt này dùng **nhãn của task: T78a = ずぶ, T78b = ぬぶ**.
- **T73 1508 không có gloss cần sửa**: E2 CUR hiển thị gloss "(Người phụ nữ Nhật Bản truyền thống)" — nhưng old_vn thực tế (audit, có chuẩn hoá) là 「Niiroku cũng là Yamato Nadeshiko nhỉ~!\nThích thật đấy, tóc đen! Ghen tị quá đi!!」 — KHÔNG có gloss. Chỉ đổi "Yamato Nadeshiko" → "Hinomoto Nadeshiko". Đã kiểm chứng full OLD trước khi kết.
- **Số đếm T77 (hiệu chỉnh)**: phụ lục E2 T77 có **251 dòng**. Trong đó **205 dòng chứa token SFX れる/るっ** (204 + biến thể lắp れっるっ lr_日々姫h2 1046); **188 dòng đổi**; 17 dòng có token nhưng không đổi (16 đã "rộp" từ trước + 1 động từ trong hội thoại れいなh4 2452 れるれるって "hãy liếm láp đi ạ" — KHÔNG phải token SFX). 46 dòng còn lại chỉ có れろ/れりゅ — không thuộc T77 (trong đó 2 dòng đổi vì T75: ハチロクh9 2133, lr_稀咲h1 1068). Con số 229 của E2 BAO GỒM れろ nên KHÔNG phải tổng T77. Tổng phụ lục: 188 đổi T77 + 2 đổi T75-only + 61 không đổi = 251.
- **T68 2749**: full OLD đã kiểm chứng — kết "thời kỳ \x%l正和;#00ffc040;Showa%l;#;." — đã "Showa", không đổi. T68 真闇01 1621 cũng đã "Showa" (chỉ khác CUR do fix gloss U3 T3b "Đường sắt Đế quốc"→"Đường sắt Teitetsu").
- **CUR của E2 làm phẳng `\n` thành khoảng trắng** ở một số dòng hiển thị; giá trị thật chứa literal backslash-n — old_vn trong JSON này lấy từ disk, không từ CUR.

## 3. Phương pháp

- Map giá trị hiện tại xây từ disk lúc chạy, chỉ load unification `*-wrong.json` có batch status "merged" trong `queue.json` / `ROUTE-UNIFICATION.md` (21 file, 2.365 key duy nhất — đã rebuild giữa đợt khi U8/U10b/U11b gộp: +60 key; rebuild kiểm chứng **0 old_vn đổi** so với bản trước). Thứ tự ưu tiên old_vn: unification đã gộp (theo thứ tự gộp) > moan > audit > CSV3 VN (good set 87.833 dòng sau khi bỏ 3.898 dòng stale). Bỏ audit fix: null (凪ふかみ08a 2426, ポーレット13 1357).
- Mọi fix đọc tay từng dòng JP (+TW); JP thắng TW; không bịa phần hoàn thiện cho JP cụt; không đụng dòng gasp-Ư hay "Kh" (không dòng nào trong đợt thuộc hai nhóm đó); không sửa lại dòng đã đúng.
- Công thức độ dài (đã kiểm chứng với tiền lệ U12b/M14): **nguyên âm kéo dài: tổng = 1 + số う/ぅ/ー** (vd. れる+13う → 14 ô; ちゅううっ → "chụụụt" 3 ụ); **phụ âm kéo dài: tổng = max(1, số う/ぅ/ー)** (vd. ずぶ+11う → 11 p; ぬぶ+11う → 11 t). Chữ hoa/thường theo token cũ (`cap_like`).
- GHÉP: dòng chia sẻ với batch đã gộp thì old_vn = fix đã gộp, fix = giá trị kết hợp cả hai thay đổi, kiểm chứng hai chiều. Không có dòng nào chia sẻ với batch ĐANG CHẠY (lúc chạy chỉ U13b chạy; U8/U10b/U11b đã gộp trước khi kết — map đã rebuild).
- Đổi theo token trong chuỗi SFX chéo mục (T75+T77+T78 cùng dòng): chỉ đổi đúng token, giữ token khác và delimiter.
- Lượt soát 2 đọc lại toàn bộ 304 fix đối chiếu JP (xem §7) — bao gồm kiểm tra tự động multiset chụt/rộp + đếm độ dài từng từ kéo dài từ JP. Phát hiện và sửa 5 lỗi lệch chỉ số của lượt 1 (xem §7).
- Chuẩn hoá newline: 4 dòng ハチロクh6 (838/884/887/934) có old_vn/fix chứa newline THẬT do CSV export; giá trị parse từ TOML trên disk là literal backslash-n (2 ký tự) — đã chuẩn hoá về literal backslash-n trong JSON + khối TOML (khớp tiền lệ U10b; TOML basic string không chứa được newline thật).

## 4. Các dòng SỬA (304 dòng, kind="unification")

### 4.1. T68 — 6 dòng (4 file). Niên hiệu 正和 → 'Showa' (1397: 正和貝石油, chơi chữ 昭和シェル石油 → 'Dầu mỏ Showa Shell').

#### lrれいな追加01_はじめての冬.txt.toml — 1 dòng

**1397** — JP 「ハイオクだったら、れいなは[しょうわかいせきゆ,4]正和貝石油の、\nえっくすぱわーが一番口にあいますねぇ」; TW 「說到高能量汽油，玲奈最喜歡的是正和貝石油的貨」; old_vn (CSV3) 「Nếu là xăng chỉ số octane cao, Reina thấy X-Power\ncủa Dầu mỏ Showakai là hợp khẩu vị nhất nha~」; **fix = 「Nếu là xăng chỉ số octane cao, Reina thấy X-Power\ncủa Dầu mỏ Showa Shell là hợp khẩu vị nhất nha~」**. Đổi: bỏ [showakai] → thêm [showa, shell].

#### ハチロク03_冥国式レイルロオド.txt.toml — 2 dòng

**2176** — JP 「あ……いえ、それでも――[しょうわ,1]正和11年までは走ってますね。\nそれから、[つるみせいてつぞうせん,5]鶴巳製鉄造船の専用線に移籍してます」; TW 「啊……不對——在那邊還是一直開到了正和１１年。之後轉去了鶴見製鐵造船的專用線工作」; old_vn (CSV3) 「A…… không, dù vậy——cô ấy vẫn chạy cho đến năm Chiêu Hòa 11.\nSau đó mới chuyển sang tuyến chuyên dụng của Tsurumi Seitetsu Zosen.」; **fix = 「A…… không, dù vậy——cô ấy vẫn chạy cho đến năm Showa 11.\nSau đó mới chuyển sang tuyến chuyên dụng của Tsurumi Seitetsu Zosen.」**. Đổi: bỏ [chiêu, hòa] → thêm [showa].

**2550** — JP 「そこでは、正和49年までを――長いですよね、本当に」; TW 「而後在那裡一直到正和４９年——倒還真是做得蠻久的」; old_vn (CSV3) 「Ở đó, cô ấy làm việc đến tận năm Chiêu Hòa 49——thực sự rất lâu nhỉ.」; **fix = 「Ở đó, cô ấy làm việc đến tận năm Showa 49——thực sự rất lâu nhỉ.」**. Đổi: bỏ [chiêu, hòa] → thêm [showa].

#### ハチロクh9_コノフクハキルコト.txt.toml — 1 dòng

**1410** — JP 「……明智末期から正和十年代までが揃っているか。\nこれなら、ポーレットの要求を満たそう」; TW 「……從明治末期到正和十多年間都有啊？滿足波萊特的要求了」; old_vn (CSV3) 「……Có đầy đủ từ cuối thời Minh Trị (Meiji) đến những năm đầu thời Chính Hòa (Showa) sao.\nThế này thì đáp ứng được yêu cầu của Paulette rồi.」; **fix = 「……Có đầy đủ từ cuối thời Minh Trị (Meiji) đến những năm đầu thời Showa sao.\nThế này thì đáp ứng được yêu cầu của Paulette rồi.」**. Đổi: bỏ [chính, hòa] → thêm [].

#### 仲国02_北琴の鉄道.txt.toml — 2 dòng

**2492** — JP 「正和59年！ って！！！！」; TW 「正和５９年！這！！！！」; old_vn (CSV3) 「Năm Chính Hà 59! Trời ơi!!!!」; **fix = 「Năm Showa 59! Trời ơi!!!!」**. Đổi: bỏ [chính, hà] → thêm [showa].

**2617** — JP 「真新しい。の範囲内だと西瓜も思います。最新の\n改築工事は2004年。日ノ本暦だと、正和59年のことです」; TW 「西瓜認為的確可以算是全新的。最近的一次改建工程是在２００４年，按日本的曆法，就是正和５９年」; old_vn (CSV3) 「Suika cũng nghĩ nó nằm trong phạm vi mới toanh.\nCông trình cải tạo mới nhất là vào năm 2004. Theo lịch Hinomoto là năm Chính Hà 59.」; **fix = 「Suika cũng nghĩ nó nằm trong phạm vi mới toanh.\nCông trình cải tạo mới nhất là vào năm 2004. Theo lịch Hinomoto là năm Showa 59.」**. Đổi: bỏ [chính, hà] → thêm [showa].

### 4.2. T71 — 11 dòng (3 file). とれいん食堂 / とれ食 → 'Tàu nhà hàng'.

#### 日々姫07_姉の想い。妹の想い.txt.toml — 2 dòng

**1358** — JP 『とれいん食堂』; TW “列車食堂”; old_vn (CSV3) 『Toa ăn Train (Toa ăn Tàu hỏa)』; **fix = 『Tàu nhà hàng』**. Đổi: bỏ [toa, toa, ăn, ăn, train, hỏa] → thêm [nhà, hàng]. Bỏ gloss '(Toa ăn Tàu hỏa)' — gloss cho từ 'Train'; tên đã đổi 'Tàu nhà hàng' nên gloss thừa.

**2572** — JP 僕らの『とれいん食堂』と繋がっていく、\n最初のレールとなってもらおう。; TW 希望他願意成為與我們的“列車食堂”相連的第一根鐵軌。; old_vn (CSV3) Hãy nhờ bác ấy trở thành thanh ray đầu tiên,\nkết nối với 'Toa ăn Train' của chúng tôi.; **fix = Hãy nhờ bác ấy trở thành thanh ray đầu tiên,\nkết nối với 'Tàu nhà hàng' của chúng tôi.**. Đổi: 'toa → 'tàu ; ăn → nhà ; train' → hàng'.

#### 日々姫08_とれいん食堂.txt.toml — 8 dòng

**1572** — JP 「“とれいん食堂”の乗車受付、開始するみたい」; TW 「“列車食堂”好像要開始檢票登車了」; old_vn (CSV3) 「Có vẻ như việc đón khách lên 'Toa ăn Train' bắt đầu rồi」; **fix = 「Có vẻ như việc đón khách lên 'Tàu nhà hàng' bắt đầu rồi」**. Đổi: 'toa → 'tàu ; ăn → nhà ; train' → hàng'.

**2082** — JP 「凪とふかみの、『とれいん食堂』Ａチーム。\n思い切った人員配置ではあるが――」; TW 「凪和深美是“列車食堂”的Ａ班組。儘管選擇她們可以說是一種大膽嘗試」; old_vn (CSV3) 「Đội A của 'Toa ăn Train' gồm Nagi và Fukami.\nDù là một sự bố trí nhân sự táo bạo nhưng——」; **fix = 「Đội A của 'Tàu nhà hàng' gồm Nagi và Fukami.\nDù là một sự bố trí nhân sự táo bạo nhưng——」**. Đổi: 'toa → 'tàu ; ăn → nhà ; train' → hàng'.

**2258** — JP 「とれいん食堂全停車駅での、最高の料理と観光。\nそう断言できる要素をいただけたからの、デザインです」; TW 「因為我得到了最權威的資訊作為要素，知道了列車食堂所有停靠車站的最佳料理和風景，才設計出這輛列車」; old_vn (CSV3) 「Ẩm thực và du lịch tuyệt vời nhất tại mọi ga dừng của Toa ăn Train.\nNhờ có được những yếu tố có thể khẳng định như vậy nên mới có thiết kế này ạ」; **fix = 「Ẩm thực và du lịch tuyệt vời nhất tại mọi ga dừng của Tàu nhà hàng.\nNhờ có được những yếu tố có thể khẳng định như vậy nên mới có thiết kế này ạ」**. Đổi: toa → tàu ; ăn → nhà ; train → hàng.

**2431** — JP 「はい。もしもし。とれいん食堂、早瀬です。\nえ？ あ――はい。遅延――ああ、はい。了解です」; TW 「是。喂喂。我是列車食堂的早瀨。唉？啊，好的。延誤……啊，是。明白了」; old_vn (CSV3) 「Vâng. Alo. Hayase của Toa ăn Train xin nghe.\nHả? A——vâng. Chậm trễ——a, vâng. Cháu hiểu rồi ạ」; **fix = 「Vâng. Alo. Hayase của Tàu nhà hàng xin nghe.\nHả? A——vâng. Chậm trễ——a, vâng. Cháu hiểu rồi ạ」**. Đổi: toa → tàu ; ăn → nhà ; train → hàng.

**3038** — JP とれいん食堂レイルロオドは、\n改装前からの引き継ぎとなる冥国製――; TW 列車食堂沿用了原本的美國式鐵路人偶。; old_vn (audit) Railord của Toa ăn Train, được kế thừa từ trước khi cải tạo, là hàng do Minh Quốc sản xuất——; **fix = Railord của Tàu nhà hàng, được kế thừa từ trước khi cải tạo, là hàng do Minh Quốc sản xuất——**. Đổi: toa → tàu ; ăn → nhà ; train → hàng.

**3319** — JP 日々姫と僕からプレゼントした、\nとれいん食堂一号列車の往復全線乗車券。; TW 日日姬和我將列車食堂一號列車的全線往返車票送給了真闇姐。; old_vn (CSV3) Vé trọn gói khứ hồi của Toa ăn Train chuyến số 1,\nmón quà mà tôi và Hibiki đã tặng.; **fix = Vé trọn gói khứ hồi của Tàu nhà hàng chuyến số 1,\nmón quà mà tôi và Hibiki đã tặng.**. Đổi: toa → tàu ; ăn → nhà ; train → hàng.

**3608** — JP “とれいん食堂”のアイディアを気に入った栃木さんは、その人脈を、惜しまず僕らに紹介してくださったから。; TW 這都得感謝櫪木先生，對“列車食堂”的點子特別中意的他，毫不吝惜地把自己的人脈都介紹給了我們。; old_vn (CSV3) Vì bác Tochigi rất thích ý tưởng 'Toa ăn Train', nên bác ấy đã không ngần ngại giới thiệu các mối quan hệ của mình cho chúng tôi.; **fix = Vì bác Tochigi rất thích ý tưởng 'Tàu nhà hàng', nên bác ấy đã không ngần ngại giới thiệu các mối quan hệ của mình cho chúng tôi.**. Đổi: 'toa → 'tàu ; ăn → nhà ; train' → hàng'.

**3652** — JP 右田日々姫デザイン。食堂気動車『とれいん食堂』。\n車籍は肥颯みかん鉄道に置く、\x%lHSMK;#00ffc040;HSMK%l;#;114と\x%lHSMK;#00ffc040;HSMK%l;#;116。; TW 餐車動車“列車食堂”由右田日日姬設計，車籍是肥薩橙鐵路的\x%lHSMK;#00ffc040;ＨＳＭＫ%l;#;１１４和\x%lHSMK;#00ffc040;ＨＳＭＫ%l;#;１１６。; old_vn (CSV3) Thiết kế bởi Migita Hibiki. Toa ăn tự hành 'Toa ăn Train'.\nĐăng ký xe thuộc Đường sắt Hisatsu Mikan, \x%lHSMK;#00ffc040;HSMK%l;#;114 và \x%lHSMK;#00ffc040;HSMK%l;#;116.; **fix = Thiết kế bởi Migita Hibiki. Toa ăn tự hành 'Tàu nhà hàng'.\nĐăng ký xe thuộc Đường sắt Hisatsu Mikan, \x%lHSMK;#00ffc040;HSMK%l;#;114 và \x%lHSMK;#00ffc040;HSMK%l;#;116.**. Đổi: ăn → 'tàu ; 'toa → nhà ; train' → hàng'. Chỉ đổi tên trong ngoặc kép; 'Toa ăn tự hành' (食堂気動車) giữ nguyên.

#### 日々姫09_run_with_our_dreams.txt.toml — 1 dòng

**1753** — JP 「え？ あれ！？ \n明日のとれいん食堂に乗るって」; TW 「哎？咦？！你不是說要坐明天的列車食堂」; old_vn (CSV3) 「Hả? Ơ!? \nRõ ràng bảo ngày mai sẽ đi nhà ăn trên tàu mà.」; **fix = 「Hả? Ơ!? \nRõ ràng bảo ngày mai sẽ đi Tàu nhà hàng mà.」**. Đổi: bỏ [ăn, trên] → thêm [hàng].

### 4.3. T72 — 18 dòng (3 file). 扇形 (tính từ) 'hình ngành' → 'hình quạt'; danh từ Gara/nhà chứa không đụng.

#### 日々姫06_みくろ、来訪.txt.toml — 1 dòng

**3059** — JP 蒸気機関車と組み合わされば、\n\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;の観光価値も更にあがろう。; TW 若是和蒸汽機車組合起來，\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;的觀光價值就更高了。; old_vn (CSV3) Nếu kết hợp với đầu máy hơi nước,\ngiá trị du lịch của \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#; sẽ càng tăng cao hơn nữa.; **fix = Nếu kết hợp với đầu máy hơi nước,\ngiá trị du lịch của \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; sẽ càng tăng cao hơn nữa.**. Đổi: ngành%l;# → quạt%l;#.

#### 日々姫07_姉の想い。妹の想い.txt.toml — 5 dòng

**1428** — JP 「……[ぶんごもり,2]文庫森のボランティアさんが言っていた。\n[せんけい,1]扇形機関庫は、シンボルなのだと」; TW 「……豐後森的志願者也說過，扇形機車庫是豐後森的標誌」; old_vn (audit) 「……Tình nguyện viên ở Bungomori đã nói.\nGara đầu máy hình ngành là một biểu tượng」; **fix = 「……Tình nguyện viên ở Bungomori đã nói.\nGara đầu máy hình quạt là một biểu tượng」**. Đổi: ngành → quạt.

**1892** — JP 「実際、ワシらも思うとったとですよ。\n\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;に\x%l蒸機;#00ffc040;蒸機%l;#;のなかとは、まっことしまらん、と」; TW 「實際上我們也是這麼想的。\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;裡沒有\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;的話，實在太不像樣了」; old_vn (CSV3) 「Thực ra, chúng tôi cũng nghĩ vậy.\n\x%l扇形機関庫;#00ffc040;Gara đầu máy hình ngành%l;#; mà không có \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; thì thật sự không ra thể thống gì」; **fix = 「Thực ra, chúng tôi cũng nghĩ vậy.\n\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#; mà không có \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; thì thật sự không ra thể thống gì」**. Đổi: ngành%l;# → quạt%l;#.

**2263** — JP 「強いていうなら――旅行中に、リゾート食堂列車ば、\n[せんけい,1]扇形機関庫に入れてやって欲しかと思いますの」; TW 「非要說的話，我希望在旅行時，觀光餐車能駛進扇形機車庫來」; old_vn (CSV3) 「Nếu phải nói thì——trong chuyến du lịch, tôi muốn toa ăn du lịch nghỉ dưỡng\nđược đưa vào \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#;」; **fix = 「Nếu phải nói thì——trong chuyến du lịch, tôi muốn toa ăn du lịch nghỉ dưỡng\nđược đưa vào \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;」**. Đổi: ngành%l;# → quạt%l;#.

**2575** — JP \x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;を内側からみて、後進、\nターンテーブルを経て、また本線へと舞い戻る――; TW 從內部遊覽\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;之後，倒車出庫，經\x%l転車台;#00ffc040;[Ｔｕｒｎ Ｔａｂｌｅ,2]轉車盤%l;#;回到幹線。; old_vn (CSV3) Ngắm nhìn \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#; từ bên trong, lùi lại,\nqua \x%l転車台;#00ffc040;bàn quay đầu máy%l;#;, rồi lại quay về tuyến chính——; **fix = Ngắm nhìn \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; từ bên trong, lùi lại,\nqua \x%l転車台;#00ffc040;bàn quay đầu máy%l;#;, rồi lại quay về tuyến chính——**. Đổi: ngành%l;# → quạt%l;#.

**2609** — JP 文庫森の\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;を尋ねれば、\n木本老技師が、僕らを再び、暖かく迎えてくれる。; TW 我們造訪了豐後森的\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;，木本老技工再次親切地招待了我們。; old_vn (CSV3) Khi chúng tôi ghé thăm \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#; ở Bungomori,\nkỹ sư lão thành Kimoto lại nồng nhiệt chào đón chúng tôi một lần nữa.; **fix = Khi chúng tôi ghé thăm \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; ở Bungomori,\nkỹ sư lão thành Kimoto lại nồng nhiệt chào đón chúng tôi một lần nữa.**. Đổi: ngành%l;# → quạt%l;#.

#### 日々姫08_とれいん食堂.txt.toml — 12 dòng

**1521** — JP ……そわそわしている。気持ちはわかる。\nけれどもここは、文庫森の\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;。公共の場だ。; TW ……她有些心神不寧。我理解她的心情。不過這裡是豐後森的\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;，是公共場所。; old_vn (CSV3) ……Em ấy đang bồn chồn. Tôi hiểu cảm giác đó.\nNhưng đây là \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#; Bungomori. Là nơi công cộng.; **fix = ……Em ấy đang bồn chồn. Tôi hiểu cảm giác đó.\nNhưng đây là \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; Bungomori. Là nơi công cộng.**. Đổi: ngành%l;# → quạt%l;#.

**1619** — JP 「……\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;いうんは凄かとですねぇ。\n御一夜では見たこともなかとでしたが」; TW 「……這個\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;真厲害啊。在御一夜就從來沒見過」; old_vn (unification đã gộp t1-ohimitera-00-02) 「……\x%l扇形機関庫;#00ffc040;Gara đầu máy hình ngành%l;#; tuyệt thật đấy nhỉ.\nỞ Ohitoyo tôi chưa từng thấy bao giờ.」; **fix = 「……\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#; tuyệt thật đấy nhỉ.\nỞ Ohitoyo tôi chưa từng thấy bao giờ.」**. Đổi: ngành%l;# → quạt%l;#. GHÉP với U1a — old_vn đã là fix U1a (có 'Ohitoyo' dòng 2); chỉ đổi tính từ. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

**2032** — JP 「[じゅうはちじよんじゅっぷん,3]1840まで、\n\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;観光停車を延長するってことですね？」; TW 「也就是說把\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;的停車觀光行程延長到[六點四十分,3]１８４０嗎？」; old_vn (CSV3) 「Nghĩa là chúng ta sẽ kéo dài thời gian dừng xe tham quan ở \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#; đến 18:40 đúng không ạ?」; **fix = 「Nghĩa là chúng ta sẽ kéo dài thời gian dừng xe tham quan ở \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; đến 18:40 đúng không ạ?」**. Đổi: ngành%l;# → quạt%l;#.

**2117** — JP 「本来予定では、1800に文庫森駅着。\n\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;入庫体験と転車台体験を経て、1830発だな」; TW 「原本的計劃是１８００到達豐後森站，讓乘客體驗完\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;入庫和\x%l転車台;#00ffc040;轉車盤%l;#;之後，於１８３０發車」; old_vn (audit) 「Theo dự kiến ban đầu, 18:00 sẽ đến ga Bungomori. Sau khi trải nghiệm đưa xe vào \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#; và trải nghiệm bàn quay đầu máy, 18:30 sẽ xuất phát.」; **fix = 「Theo dự kiến ban đầu, 18:00 sẽ đến ga Bungomori. Sau khi trải nghiệm đưa xe vào \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; và trải nghiệm bàn quay đầu máy, 18:30 sẽ xuất phát.」**. Đổi: ngành%l;# → quạt%l;#.

**2264** — JP 「\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;内で、20分間の観光下車があります。\nその間に、\x%lギャレー;#00ffc040;ギャレー%l;#;の準備の予定でした」; TW 「在\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;內有２０分鐘的下車觀光行程，原計劃是在這段時間裡進行\x%lギャレー;#00ffc040;廚房%l;#;的準備」; old_vn (CSV3) 「Sẽ có 20 phút xuống xe tham quan bên trong \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#;.\nTheo dự kiến, chúng ta sẽ chuẩn bị \x%lギャレー;#00ffc040;bếp trên tàu%l;#; trong khoảng thời gian đó ạ.」; **fix = 「Sẽ có 20 phút xuống xe tham quan bên trong \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;.\nTheo dự kiến, chúng ta sẽ chuẩn bị \x%lギャレー;#00ffc040;bếp trên tàu%l;#; trong khoảng thời gian đó ạ.」**. Đổi: ngành%l;# → quạt%l;#.

**2292** — JP 「15分遅延となると、\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;観光停車中の\n\x%lギャレー;#00ffc040;ギャレー%l;#;準備はかなり難しくなるな」; TW 「如果延遲１５分鐘的話，要在\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;的停車觀光行程中進行\x%lギャレー;#00ffc040;廚房%l;#;的準備就比較難了」; old_vn (CSV3) 「Nếu chậm trễ 15 phút, thì việc chuẩn bị \x%lギャレー;#00ffc040;bếp trên tàu%l;#; trong lúc dừng xe tham quan ở \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#; sẽ khá là khó khăn đấy.」; **fix = 「Nếu chậm trễ 15 phút, thì việc chuẩn bị \x%lギャレー;#00ffc040;bếp trên tàu%l;#; trong lúc dừng xe tham quan ở \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; sẽ khá là khó khăn đấy.」**. Đổi: ngành%l;# → quạt%l;#.

**2296** — JP 「[じゅうはちじにじゅっぷん,3]1820に料理がついたとして、20分の準備で、\n1840\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;出庫――そのまま15分遅延となるか」; TW 「如果說晚餐在[六點二十分,3]１８２０送到，花２０分鐘準備，讓列車在[六點四十分,3]１８４０駛出\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;……要順延１５分鐘啊」; old_vn (CSV3) 「Giả sử 18:20 món ăn được đưa đến, mất 20 phút chuẩn bị,\n18:40 đưa xe ra khỏi \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#;――vậy là vẫn bị chậm 15 phút à.」; **fix = 「Giả sử 18:20 món ăn được đưa đến, mất 20 phút chuẩn bị,\n18:40 đưa xe ra khỏi \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;――vậy là vẫn bị chậm 15 phút à.」**. Đổi: ngành%l;# → quạt%l;#.

**2730** — JP 「と、いうことだ。凪はすまんが、文庫森――\n\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;に“5分早着”可能かを聞いてきてくれ」; TW 「那就得拜託凪去問一下了，看能不能提早５分鐘到豐後森——也就是\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;」; old_vn (CSV3) 「Là vậy đó. Nagi, xin lỗi em nhưng,\nhãy hỏi xem Bungomori――\x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#; có thể “đến sớm 5 phút” được không nhé.」; **fix = 「Là vậy đó. Nagi, xin lỗi em nhưng,\nhãy hỏi xem Bungomori――\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; có thể “đến sớm 5 phút” được không nhé.」**. Đổi: ngành%l;# → quạt%l;#.

**2734** — JP 「ならば1755文庫森着。1800から\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;見学。\n1820分に\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;を出庫して、転車台体験」; TW 「那就是１７５５到豐後森。１８００開始參觀\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;。１８２０駛出\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;，體驗轉車盤」; old_vn (CSV3) 「Vậy thì 17:55 đến Bungomori. Từ 18:00 tham quan \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#;.\n18:20 đưa xe ra khỏi \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#; và trải nghiệm bàn quay đầu máy.」; **fix = 「Vậy thì 17:55 đến Bungomori. Từ 18:00 tham quan \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;.\n18:20 đưa xe ra khỏi \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; và trải nghiệm bàn quay đầu máy.」**. Đổi: ngành%l;# → quạt%l;# ; ngành%l;# → quạt%l;#.

**3052** — JP 1805\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;入庫、1825\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;出庫が\n本来の予定なのだから……; TW 原本的計劃是１８０５駛入\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;，１８２５駛出\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;……; old_vn (CSV3) Vì dự kiến ban đầu là 18:05 đưa xe vào \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#;, 18:25 đưa xe ra khỏi \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#; mà……; **fix = Vì dự kiến ban đầu là 18:05 đưa xe vào \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;, 18:25 đưa xe ra khỏi \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; mà……**. Đổi: ngành%l;# → quạt%l;# ; ngành%l;# → quạt%l;#.

**3089** — JP \x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;の奥の方、目隠しにかけられているシートが\nこんもりと、人の形に盛り上がる。; TW 在\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;的另一頭，遮擋視線的塑膠布上透出了一道人影。; old_vn (CSV3) Phía trong cùng của \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#;, tấm bạt che chắn\nnhô lên một khối hình người.; **fix = Phía trong cùng của \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;, tấm bạt che chắn\nnhô lên một khối hình người.**. Đổi: ngành%l;# → quạt%l;#.

**3392** — JP 食事三回、ティータイム一回。\n更に\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;入庫まで体験できるフルボリューム。; TW 正餐三次，午茶一次。而且還能體驗到\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;入庫，旅程安排得滿滿當當。; old_vn (CSV3) Ba bữa ăn chính, một bữa tiệc trà.\nHơn nữa còn được trải nghiệm việc đưa vào \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#;, một lịch trình dày đặc.; **fix = Ba bữa ăn chính, một bữa tiệc trà.\nHơn nữa còn được trải nghiệm việc đưa vào \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;, một lịch trình dày đặc.**. Đổi: ngành%l;# → quạt%l;#.

### 4.4. T73 — 3 dòng (2 file). 日ノ本撫子 / ヒノモトナデシコ → 'Hinomoto Nadeshiko'.

#### ハチロク09_もくもくオリヴィ.txt.toml — 2 dòng

**1508** — JP 「ニイロクもヒノモトナデシコなんだね～！\nいいな、クロカミ！ うらやましい！！」; TW 「二六也是大和撫子呀！黑髮真漂亮！好羨慕哦！！」; old_vn (audit) 「Niiroku cũng là Yamato Nadeshiko nhỉ~!\nThích thật đấy, tóc đen! Ghen tị quá đi!!」; **fix = 「Niiroku cũng là Hinomoto Nadeshiko nhỉ~!\nThích thật đấy, tóc đen! Ghen tị quá đi!!」**. Đổi: yamato → hinomoto.

**1879** — JP 「だからⅨ号機関車は。日ノ本撫子のハチロクよりも、\nちょっとだけジャジャ馬なのかもしれませんね」; TW 「所以九號機車比起大和撫子八六，可能多少有些烈馬的感覺」; old_vn (CSV3) 「Chính vì vậy Đầu máy số 9. So với Yamato Nadeshiko Hachiroku,\ncó lẽ mang một chút gì đó của ngựa chứng hoang dã nhỉ.」; **fix = 「Chính vì vậy Đầu máy số 9. So với Hinomoto Nadeshiko Hachiroku,\ncó lẽ mang một chút gì đó của ngựa chứng hoang dã nhỉ.」**. Đổi: yamato → hinomoto.

#### ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml — 1 dòng

**993** — JP 「すずの中身も、よくわかる。\n清純な日ノ本撫子のお前の[なか,1]膣内が――」; TW 「我也很了解你的裡面。你一個純潔的賢淑女性的陰道——」; old_vn (CSV3) 「Bên trong Suzu, tôi cũng hiểu rất rõ.\nBên trong âm đạo của một Yamato Nadeshiko thanh thuần như em——」; **fix = 「Bên trong Suzu, tôi cũng hiểu rất rõ.\nBên trong âm đạo của một Hinomoto Nadeshiko thanh thuần như em——」**. Đổi: yamato → hinomoto.

### 4.5. T74 — 1 dòng (1 file). まいてつ契約 → 'hợp đồng chủ tàu'.

#### 凪h2_おとなの水着.txt.toml — 1 dòng

**1766** — JP ……8620が完全復活し、僕も御一夜鉄道と、\n一般的なまいてつ契約を締結するようになった。; TW ……８６２０已經徹底恢復，我與御一夜鐵路也簽訂了正常的掌車人契約。; old_vn (unification đã gộp t1-ohito-t2-06-11) ……8620 đã hoàn toàn hồi sinh, và tôi cũng đã ký kết hợp đồng Maitetsu thông thường\nvới Đường sắt Ohitoyo.; **fix = ……8620 đã hoàn toàn hồi sinh, và tôi cũng đã ký kết hợp đồng chủ tàu thông thường\nvới Đường sắt Ohitoyo.**. Đổi: bỏ [maitetsu] → thêm [chủ, tàu]. GHÉP với U2b — chỉ đổi token T74, giữ 'Đường sắt Ohitoyo' của U2b. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

### 4.6. T75 — 53 dòng (16 file). Âm hôn trần → họ 'chụt' theo công thức nguyên âm (VN = 1 + số う/ぅ): ちゅっ→'chụt', ちゅうっ→'chụụt', ちゅむっ/ちゅるっ/ちゅろっ/ちゅぷっ/ちゅぱっ/ちゅぶっ→'chụt'.

#### lr_ハチロクh1_今ひとたびの契り.txt.toml — 4 dòng

**1234** — JP 「あ……――んっ――ちゅむっ――ちゅうっ――っ」; TW 「啊……嗯——啾——啾——」; old_vn (moan) 「A……——ưm——chumu——chuu——Ư」; **fix = 「A……——ưm——chụt——chụụt——Ư」**. Đổi: chumu → chụt ; chuu → chụụt.

**1241** — JP 「あむっ――ふっ――んっ――れうっ――りゅっ――\nちゅむっ――ちゅうっ――じゅりゅっ――」; TW 「啊嗚……呼……唔……啾……啾唔——啾——啾嚕——」; old_vn (moan) 「Amu——fu——ưm——reu——ryu——\nChumu——chuu——juryu——」; **fix = 「Amu——fu——ưm——reu——ryu——\nChụt——chụụt——juryu——」**. Đổi: chumu → chụt ; chuu → chụụt.

**2008** — JP （ちゅむっ――ぷりゅっ）; TW （輕搖柔擺）; old_vn (moan) （Chumu——puryu）; **fix = （Chụt——puryu）**. Đổi: chumu → chụt.

**2011** — JP （ぷっ――ちゅうっ――）; TW （輕柔貼附）; old_vn (CSV3) （Pu——chuu——）; **fix = （Pu——chụụt——）**. Đổi: chuu → chụụt.

#### lr_凪h1_痛いの痛いの飛んでけばい.txt.toml — 5 dòng

**1158** — JP 「んくっ！ ふあ――あっ――んっ――（はむっ！）\nじゅるっ――ちゅぶっ！ じゅる！ じゅばっ！！」; TW 「唔！啊……啊……嗯……（含！）啾……啾！啾！啾！！」; old_vn (moan) 「Ưm ku! Fua――á――ưm――（Ngoạm!）\nJuru――chubu! Juru! Juba!!」; **fix = 「Ưm ku! Fua――á――ưm――（Ngoạm!）\nJuru――chụt! Juru! Juba!!」**. Đổi: chubu → chụt.

**1162** — JP 「んくっ！？ ぷっ――ふぁっ――ンッ――じゅる！\nじゅぼっ！ じゅぶっ！ じゅばっ！ ちゅううっ」; TW 「唔？！噗……啊……嗯……啾！啾！啾！啾！啾」; old_vn (moan) 「Ưm ku!? Pu――fa――ưm――juru!\nJubo! Jubu! Juba! Chuuuu」; **fix = 「Ưm ku!? Pu――fa――ưm――juru!\nJubo! Jubu! Juba! Chụụụt」**. Đổi: chuuuu → chụụụt.

**1218** — JP 「じゅむっ！ じゅぶっ！ じゅぼっ！ じゅばっ！\nじゅっ！ ちゅるっ！ ちゅぼっ！ じゅばっ！！」; TW 「啾！啾！啾！啾！啾！啾！啾！啾！」; old_vn (CSV3) 「Jumu! Jubu! Jubo! Juba!\nJu! Churu! Chubo! Juba!!」; **fix = 「Jumu! Jubu! Jubo! Juba!\nJu! Chụt! Chụt! Juba!!」**. Đổi: churu → chụt ; chubo → chụt.

**1219** — JP 「ぐぽっ！ ぢゅぼっ！ ちゅぶっ！ ちゅううっ！\nくっ！ りゅっ！ ちゅううっ！ （はみっ！！）」; TW 「啾！啾！啾！啾！啾！啾！啾！（咬）」; old_vn (moan) 「Gupo! Jubo! Chubu! Chuuuu!\nKu! Ryu! Chuuuu! （Ngoạm!!）」; **fix = 「Gupo! Jubo! Chụt! Chụụụt!\nKu! Ryu! Chụụụt! （Ngoạm!!）」**. Đổi: chubu → chụt ; chuuuu → chụụụt ; chuuuu → chụụụt.

**1220** — JP 「じゅるっ！ れるうううっ！ れろっ！ ちゅぱっ！\nんっ！ じゅぶっ！ じゅぼっ！ じゅっ！ じゅぶ！」; TW 「啾！啾！啾！啾！嗯！啾！啾！啾！啾！」; old_vn (moan) 「Juru! Reruuuu! Rero! Chupa!\nƯm! Jubu! Jubo! Ju! Jubu!」; **fix = 「Juru! Reruuuu! Rero! Chụt!\nƯm! Jubu! Jubo! Ju! Jubu!」**. Đổi: chupa → chụt.

#### lr_日々姫h2_デザートは食事の前に.txt.toml — 3 dòng

**998** — JP 「でゅぼっ！ じゅ！！ ぢゅるるっ！ ちゅ、ばっ！\nんっ――ぢゅぼっ！ ちゅうっ！ じゅるっ！ じゅぶ」; TW 「啊嗯……啾，啾嚕……啊嗯……啾……啾嚕……啾嚕嚕」; old_vn (CSV3) 「Dyubo! Ju!! Jyururu! Chu, ba!\nƯm——jyubo! Chuu! Juru! Jubu」; **fix = 「Dyubo! Ju!! Jyururu! Chụt, ba!\nƯm——jyubo! Chụụt! Juru! Jubu」**. Đổi: chu → chụt ; chuu → chụụt.

**1041** — JP 「ちゅるっ――もむっ！ はむっ――あむっ――\nん……はむっ――かぷっ――もぷっ――あむっ――」; TW 「啾嚕、啾嚕嚕嚕……咕啾！嗯……啾……啾嚕……咕啾！」; old_vn (CSV3) 「Churu——momu! Hamu——amu——\nƯm…… hamu——kapu——mopu——amu——」; **fix = 「Chụt——momu! Hamu——amu——\nƯm…… hamu——kapu——mopu——amu——」**. Đổi: churu → chụt.

**1056** — JP 「ぐぽっ！ ぐぱっ！ ちゅぶっ！ じゅずっ！ ずっ！\nじゅるるるっ！ ぢゅぼっ！ れるっ！ ぶちゅう！」; TW 「嗯……啾、啾……啾嚕……啾嚕……啾嚕……啾……啾噗！」; old_vn (CSV3) 「Gupo! Gupa! Chubu! Juzu! Zu!\nJurururu! Jyubo! Reru! Buchuu!」; **fix = 「Gupo! Gupa! Chụt! Juzu! Zu!\nJurururu! Jyubo! Reru! Buchuu!」**. Đổi: chubu → chụt.

#### lr_稀咲h1_おしおきとごほうび.txt.toml — 9 dòng

**1023** — JP 「あーーーん……（はぷっ）――ちゅっ――ちゅううっ、\nちゅるっ――ずっ――――――（こくっ）――ぷぁっ」; TW 「啊嗯……啊嗚……啾、啾嚕……啾嚕……嗚……咕嘟……噗」; old_vn (moan) 「Aaaan……(hapu)――chu――chuuu,\nchuru――zu――――――(koku)――pua.」; **fix = 「Aaaan……(hapu)――chụt――chụụụt,\nchụt――zu――――――(koku)――pua.」**. Đổi: chu → chụt ; chuuu → chụt ; churu → chụụụt.

**1046** — JP 「ちゅっ」; TW 「啾」; old_vn (CSV3) 「Chu.」; **fix = 「Chụt.」**. Đổi: chu → chụt.

**1053** — JP 「ちゅぶっ――ちゅばっ――ちゅむっ――ちゅううっ。\nふっ――はっ――ちゅむっ――ちゅぶっ――ぢゅるっ」; TW 「啾嚕……啾噗噗……啾啪……啾、啾、啾噗……啾嚕」; old_vn (CSV3) 「Chubu――chuba――chumu――chuuu.\nPhù――há――chumu――chubu――juru.」; **fix = 「Chụt――chụt――chụt――chụụụt.\nPhù――há――chụt――chụt――juru.」**. Đổi: chubu → chụt ; chubu → chụt ; chuba → chụt ; chumu → chụt ; chumu → chụt ; chuuu → chụụụt. ちゅばっ — cặp hữu thanh của ちゅぱっ (đã liệt kê trong quyết); áp 'chụt' theo cùng quy tắc.

**1055** — JP 「れりゅうぅぅ――れりゅっ――ぬりゅっ――（こくっ）\nちゅっ――ちゅむっ――ちゅううっ――ちゅうううっ」; TW 「啾嚕嚕嚕……啾嚕……啾嚕……咕嘟。啾、啾嚕、啾嚕嚕……啾嚕嚕嚕」; old_vn (audit) 「Reryuuuu――reryu――nuryu――(koku)\nchu――chumu――chuuu――chuuuu.」; **fix = 「Reryuuuu――reryu――nuryu――(koku)\nchụt――chụt――chụụụt――chụụụụt.」**. Đổi: chu → chụt ; chumu → chụt ; chuuu → chụụụt ; chuuuu → chụụụụt.

**1058** — JP 「ぢゅむっ！ ぢゅぼっ！ ぼっ！ ぢゅうううううっ！\nずびゅっ――ちゅ――れるっ――ずぼっ！ ぼちゅっ！」; TW 「啾嚕！啾噗！啾嚕嚕嚕！啾、啾、啾……噗啾！」; old_vn (audit) 「Jumu! Jubo! Bo! Juuuuuu!\nZubyu――chu――reru――zubo! Bochu!」; **fix = 「Jumu! Jubo! Bo! Juuuuuu!\nZubyu――chụt――reru――zubo! Bochu!」**. Đổi: chu → chụt.

**1068** — JP 「ん……ちゅっ――ちゅむっ――ちゅ……れ――りゅっ、\nれりゅっ――ちゅうっ――ちゅるるっ――れりゅうう」; TW 「嗯……啾、啾……啾嚕……啾嚕……啾嚕……啾……啾噗」; old_vn (CSV3) 「Ưm……chu――chumu――chu……re――ryu,\nreryu――chuu――chururu――reryuuu.」; **fix = 「Ưm……chụt――chụt――chụt……re――ryu,\nreryu――chụụt――chụt――reryuuu.」**. Đổi: chu → chụt ; chu → chụt ; chumu → chụt ; chuu → chụt ; chururu → chụụt. Chỉ đổi T75; chỉ có token れりゅ trong dòng — không thuộc T77.

**1069** — JP 「ん……ふっ――ちゅぷっ――ちゅぱっ――\nちゅっ――ぢゅっ――ぢゅぷっ――ぢゅばっ――」; TW 「嗯……啾噗噗……啾啪……啾、啾、啾噗……」; old_vn (CSV3) 「Ưm……phù――chupu――chupa――\nchu――ju――jupu――juba――」; **fix = 「Ưm……phù――chụt――chụt――\nchụt――ju――jupu――juba――」**. Đổi: chupu → chụt ; chupa → chụt ; chu → chụt.

**1133** — JP 「ここ。だ。（ちゅっ！）」; TW 「就是因為這裡……啾！」; old_vn (audit) 「Chỗ này đây. (Chu!)」; **fix = 「Chỗ này đây. Chụt!)」**. Đổi: chu → chụt.

**1688** — JP （すにゅっ――くちゅっ――ちゅくっ――ちゅっ）; TW （咕啾、咕啾、咕啾、咕啾）; old_vn (CSV3) （Sunyu――kuchu――chuku――chu）; **fix = （Sunyu――kuchu――chuku――chụt）**. Đổi: chu → chụt.

#### lr_稀咲ポーレットh1_悪い大人の契約.txt.toml — 6 dòng

**993** — JP 「……。うん、稀咲。\n―えと―んっ！ ―ちゅむっ―（さわっ）」; TW 「……嗯，稀咲。——呃——嗯！ ——啾嗯——（摸）」; old_vn (CSV3) 「……Ừm, Kisaki.\n——Ưm——ưm! ——Chu mu——（Chạm nhẹ）」; **fix = 「……Ừm, Kisaki.\n——Ưm——ưm! ——Chụt——（Chạm nhẹ）」**. Đổi: bỏ [chu, mu] → thêm [chụt].

**1397** — JP 「セックス―セックス。双鉄くんと、稀咲と、セックス。\n三人で……ふぁっ―ちゅむっ―ちゅぅぅっ―」; TW 「做愛——做愛。和雙鐵君，和稀咲，一起做愛。三個人一起……呼啊——啾——啾——」; old_vn (moan) 「Làm tình——làm tình. Làm tình với anh Soutetsu và Kisaki. Ba người cùng nhau……Fa——chu mu——chuu u——」; **fix = 「Làm tình——làm tình. Làm tình với anh Soutetsu và Kisaki. Ba người cùng nhau……Fa——chụt——chụụụt——」**. Đổi: bỏ [chu, mu, chuu, u] → thêm [chụt, chụụụt].

**1584** — JP 「ちゅううっ―ん……ちゅぱっ。ふぁ……\nえと、稀咲…………。あの、ね？ ―ありがとう」; TW 「啾——嗯……啾。呼啊……呃，稀咲……。那個…… ——謝謝」; old_vn (unification đã gộp s3-fa-fu) 「Chuu u——ưm……chu pa. Fa……Ưm, Kisaki………… Nè? ——Cảm ơn em.」; **fix = 「Chụụụt——ưm……chụt. Fa……Ưm, Kisaki………… Nè? ——Cảm ơn em.」**. Đổi: bỏ [chuu, u, chu, pa] → thêm [chụụụt, chụt]. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

**2537** — JP （ちゅぶっ―ちゅるっ―ちゅぢゅっ―ちゅくっ）; TW （啾噗——啾——啾啾——啾）; old_vn (CSV3) （Chu bu——chu ru——chu ju——chu ku）; **fix = （Chụt——chụt——chu ju——chu ku）**. Đổi: bỏ [chu, chu, bu, ru] → thêm [chụt, chụt].

**2547** — JP （しっっ―ちゅくっ―ちゅぶっ―ぢゅるっ―）; TW （噗哧——咕啾——啾噗——咕啾——）; old_vn (CSV3) （Cọ——chu ku——chu bu——ju ru——）; **fix = （Cọ——chu ku——chụt——ju ru——）**. Đổi: bỏ [chu, bu] → thêm [chụt].

**2560** — JP （ふにゅっ―ちゅるっ！ ちゅぶっ！ ぢゅぶっ！）; TW （按壓——啾啾！ 啾噗！ 啾噗！）; old_vn (CSV3) （Nhào nặn——chu ru! Chu bu! Ju bu!）; **fix = （Nhào nặn——chụt! chụt! Ju bu!）**. Đổi: bỏ [chu, chu, ru, bu] → thêm [chụt, chụt].

#### れいなh1_おかあさんのレッスン.txt.toml — 1 dòng

**2351** — JP （ちゅうううっ！）; TW （啾！）; old_vn (CSV3) （Chuuuu!）; **fix = （Chụụụụt!）**. Đổi: chuuuu → chụụụụt.

#### れいなh3_おもらし自由化大作戦.txt.toml — 1 dòng

**1083** — JP 「ふにゃっ――んっ――ちゅ――ちゅうっ――\nちゅ――ちゅむっ――ふぁっ――ん～――ちゅるっ」; TW 「啾……啾……嗯……啊嗯……啾嚕」; old_vn (moan) 「Funya——ưm——chu——chuu——\nChu——chumu——Fa——n~——churu」; **fix = 「Funya——ưm——chụt——chụụt——\nChụt——chụt——Fa——n~——chụt」**. Đổi: chu → chụt ; chu → chụt ; chuu → chụt ; chumu → chụt ; churu → chụụt.

#### ハチロクh1_契り.txt.toml — 1 dòng

**2147** — JP （ちゅむっ）; TW （啾嚕）; old_vn (audit) （Chumu）; **fix = （Chụt）**. Đổi: chumu → chụt.

#### ハチロクh2_お勉強の成果.txt.toml — 1 dòng

**1021** — JP 「ちゅるっ！」; TW 「啾嚕！」; old_vn (CSV3) 「Chu mút!」; **fix = 「Chụt!」**. Đổi: bỏ [chu, mút] → thêm [chụt].

#### ハチロクh8_桜色のひめごと.txt.toml — 1 dòng

**794** — JP 「ちゅ……むっ――ん――ぷぁ――あっ！ 双鉄、様……\nさっき――あれほど、お出しに、なったの……に――ん」; TW 「啾……姆——噗啊——啊！雙鐵少爺……剛才——還出來那麼多的……——嗯」; old_vn (CSV3) 「Chu……mu——ưm——pua——a! Ngài Soutetsu……\nLúc nãy——ngài vừa mới xuất, nhiều đến thế……mà——ưm」; **fix = 「Chụt……——ưm——pua——a! Ngài Soutetsu……\nLúc nãy——ngài vừa mới xuất, nhiều đến thế……mà——ưm」**. Đổi: bỏ [chu, mu] → thêm [chụt]. ちゅ……むっ tách bởi …… trong JP — giữ nhịp ngắt, 'Chụt……' (1 token = 1 rendering).

#### ハチロクh9_コノフクハキルコト.txt.toml — 9 dòng

**2033** — JP 「ふっ……んっ――――（ごくんっ）\nずっ――ちゅるっ――じゅううっ――（ごくっ）」; TW 「呼……——（嗯）呲——啾嚕——吱嗚——（嗯）」; old_vn (unification đã gộp s3-moan-dialogue) 「Fu……ưm————（Ực）\nZu——churu——juuu——（Ực）」; **fix = 「Fu……ưm————（Ực）\nZu——chụt——juuu——（Ực）」**. Đổi: churu → chụt. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

**2124** — JP 「ちゅっ――ちゅむっ――ちゅるうぅ――（ごくっ）」; TW 「啾——啾姆——啾嚕——（咕嚕）」; old_vn (CSV3) 「Chu——chumu——churuuu——（Ực）」; **fix = 「Chụt——chụt——chụụụt——（Ực）」**. Đổi: chu → chụt ; chumu → chụt ; churuuu → chụụụt.

**2127** — JP 「ぢゅうううううっ！ ぢゅぼ！ ちゅっ！ じゅぶ、\nじゅぼっ！ ちゅうっ！ ぢゅるっ！ ぢゅ！ ぼ！」; TW 「啾嗚嗚嗚！啾啵！啾！啾，啾啵！啾嗚！啾嚕！呲啾！啵！」; old_vn (CSV3) 「Juuuuu! Jubo! Chu! Jubu,\njubo! Chuu! Juru! Ju! Bo!」; **fix = 「Juuuuu! Jubo! Chụt! Jubu,\njubo! Chụụt! Juru! Ju! Bo!」**. Đổi: chu → chụt ; chuu → chụụt.

**2128** — JP 「ちゅうっ！ じゅっ！ ぢゅるるっ！ じゅぼっ！\nんっ――ちゅうっ！ ぢゅっ！ ぢゅぼ！ ぢゅ！」; TW 「啾嗚！啾！啾嚕嚕！啾啵！嗯——啾嗚！呲啾！啾啵！呲啾！」; old_vn (CSV3) 「Chuu! Ju! Jururu! Jubo!\nƯm——chuu! Ju! Jubo! Ju!」; **fix = 「Chụụt! Ju! Jururu! Jubo!\nƯm——chụụt! Ju! Jubo! Ju!」**. Đổi: chuu → chụụt ; chuu → chụụt.

**2133** — JP 「ちゅるうっ――ちゅ、ずっ――ぺろ、ぺろ、ぺろっ、\nちゅるうっ、ちゅっ――れろっ――ぺろ、ぺろおっっ」; TW 「啾嚕——啾，呲——呸嚕，呸嚕，呸嚕，啾嚕，啾——咻嚕——呸嚕，呸嚕」; old_vn (CSV3) 「Churuu——chu, zu——pero, pero, pero,\nchuruu, chu——rero——pero, perooo」; **fix = 「Chụụt——chụt, zu——pero, pero, pero,\nchụụt, chụt——rero——pero, perooo」**. Đổi: churuu → chụụt ; churuu → chụụt ; chu → chụt ; chu → chụt. Chỉ đổi T75; れろっ duy nhất trong dòng — không thuộc T77.

**2145** — JP 「んっ――ちゅっ――ちゅぼっ！ じゅぼっ！\nじゅ！ じゅぼっ！ じゅりゅうう！ じゅ、ぼっ！」; TW 「嗯——啾——啾啵！啾啵！呲啾！啾啵！呲啾！啾，啵！」; old_vn (CSV3) 「Ưm——chu——chubo! Jubo!\nJu! Jubo! Juryuuu! Ju, bo!」; **fix = 「Ưm——chụt——chụt! Jubo!\nJu! Jubo! Juryuuu! Ju, bo!」**. Đổi: chu → chụt ; chubo → chụt.

**2147** — JP 「んっ――ちゅむっ！ じゅっ！ じゅぼっ！ じゅ、\nぢゅちゅっ！ ちゅむっ！ ぢゅるっ！ じゅぶ！」; TW 「嗯——啾姆！啾！啾啵！呲啾，呲啾！啾姆！啾嚕！啾！」; old_vn (CSV3) 「Ưm——chumu! Ju! Jubo! Ju,\njuchu! Chumu! Juru! Jubu!」; **fix = 「Ưm——chụt! Ju! Jubo! Ju,\njuchu! Chụt! Juru! Jubu!」**. Đổi: chumu → chụt ; chumu → chụt.

**2153** — JP 「んっ――はむっ――ちゅっ――ちゅううっ、ちゅ」; TW 「嗯——姆——啾——啾嗚，啾」; old_vn (CSV3) 「Ưm——hamu——chu——chuuu, chu」; **fix = 「Ưm——hamu——chụt——chụụụt, chụt」**. Đổi: chu → chụt ; chu → chụt ; chuuu → chụụụt.

**2182** — JP 「んむっ！？ んっ――ちゅぼっ――じゅっ！\nぢゅぶっ！ ぢゅむっ！ ふっ――ちゅむ、じゅっ！」; TW 「嗯姆！？嗯——啾啵——啾！啾噗！呲啾姆！呼——啾嗯，啾！」; old_vn (unification đã gộp s3-moan-dialogue) 「Ưm mu!? Ưm——chubo——ju!\nJubu! Jumu! Fu——chumu, ju!」; **fix = 「Ưm mu!? Ưm——chụt——ju!\nJubu! Jumu! Fu——chụt, ju!」**. Đổi: chubo → chụt ; chumu → chụt. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

#### ポーレットh4_クリーム＆クリーム.txt.toml — 1 dòng

**1576** — JP （ちゅむっ――）; TW （啾噗）; old_vn (moan) （Chumu——）; **fix = （Chụt——）**. Đổi: chumu → chụt.

#### 真闇h1_長期熟成.txt.toml — 1 dòng

**1094** — JP 「んっ！ んぷ――ちゅ――んっ、ちゅる――ちゅむっ」; TW 「嗯！ 嗯唔――啾――嗯、啾嚕――啾唔」; old_vn (audit) 「Ưm! Npu――Chu――ưm, Churu――Chumu.」; **fix = 「Ưm! Npu――Chụt――ưm, Chụt――Chụt.」**. Đổi: chu → chụt ; churu → chụt ; chumu → chụt.

#### 真闇h2_無濾過.txt.toml — 1 dòng

**1078** — JP 「はぷっ――んっ――ちゅう――」; TW 「啊嗚――嗯――啾――」; old_vn (moan) 「Hapu――ưm――chuu――」; **fix = 「Hapu――ưm――chụụt――」**. Đổi: chuu → chụụt.

#### 真闇h3_補習授業の廃校舎.txt.toml — 8 dòng

**2276** — JP 「はむっ――ちゅっ――ちゅるっ――ころっ――\nん……ちゅるっ――れろっ、ころっっ――こりゅ」; TW 「啊嗚――啾――啾――咕溜――嗯……啾――舔、咕嘍――咕溜」; old_vn (CSV3) 「Hamu――chu――churu――koro――\nưm……churu――rero, koro――koryu.」; **fix = 「Hamu――chụt――chụt――koro――\nưm……chụt――rero, koro――koryu.」**. Đổi: chu → chụt ; churu → chụt ; churu → chụt.

**2288** — JP 「ちゅうっ――ちゅっ――はむっ、あむっ――んっ\nちゅろおっ、ちゅろ、ころっ――ちゅうううううっ」; TW 「啾――啾――啊嗚、啊嗚――嗯啾囉、啾囉、咕溜――啾」; old_vn (moan) 「Chuu――chu――hamu, amu――ưm\nchuroo, churo, koro――chuuuuuu.」; **fix = 「Chụụt――chụt――hamu, amu――ưm\nchụt, chụt, koro――chụụụụụụt.」**. Đổi: chuu → chụụt ; chu → chụt ; churoo → chụt ; churo → chụt ; chuuuuuu → chụụụụụụt. ちゅろおっ: お kéo dài KHÔNG tính theo công thức (chỉ う/ぅ) → 'chụt'.

**2294** — JP 「じゅぼっ！ ぼぢゅっ！ じゅぼっ！ じゅばっ！\nじゅ！ ちゅぼっ！ じゅぼっ！ じゅるっ！！」; TW 「啾啵！ 啵啾！ 啾啵！ 啾叭！啾！ 啾啵！ 啾啵！ 啾嚕！！」; old_vn (CSV3) 「Jubo! Boju! Jubo! Juba!\nJu! Chubo! Jubo! Juru!!」; **fix = 「Jubo! Boju! Jubo! Juba!\nJu! Chụt! Jubo! Juru!!」**. Đổi: chubo → chụt.

**2295** — JP 「じゅぼっ！ じゅぶっ！ じゅっ！ じゅぶぶっ！\nじゅぼっ！ ちゅううううっ！ じゅ！ じゅばっ！」; TW 「啾啵！ 啾噗！ 啾！ 啾噗！啾啵！ 啾！ 啾！ 啾叭！」; old_vn (moan) 「Jubo! Jubu! Ju! Jububu!\nJubo! Chuuuuuu! Ju! Juba!」; **fix = 「Jubo! Jubu! Ju! Jububu!\nJubo! Chụụụụụt! Ju! Juba!」**. Đổi: chuuuuuu → chụụụụụt.

**2332** — JP 「ん……ちゅっ――んちゅ――ちゅっ――ちゅうっ、\nちゅっ――ちゅ、むっ――んっ――れる――ぷあっ」; TW 「嗯……啾――嗯啾――啾――啾、啾――啾、唔――嗯――嚕溜――噗啊」; old_vn (CSV3) 「Ưm……chu――ưm chu――chu――chuu,\nchu――chu, mu――ưm――reru――pua.」; **fix = 「Ưm……chụt――ưm chụt――chụt――chụụt,\nchụt――chụt, mu――ưm――reru――pua.」**. Đổi: chu → chụt ; chu → chụt ; chu → chụt ; chu → chụt ; chu → chụt ; chuu → chụụt.

**2334** — JP 「ん……ちゅっ――んんっ――ぷあっ――\nおいしくは、なかけど――ん――ちゅるっ（ごくっ）」; TW 「嗯……啾――嗯嗯――噗啊――雖然不太好喝啦――嗯――啾（咕嘟）」; old_vn (moan) 「Ưm……chu――ưmm――pua――\nDù không, ngon lắm――ưm――churu（ực）」; **fix = 「Ưm……chụt――ưmm――pua――\nDù không, ngon lắm――ưm――chụt（ực）」**. Đổi: chu → chụt ; churu → chụt.

**2336** — JP 「ん……チュッ――ずろっ――ちゅる、るう、るっ」; TW 「嗯……啾――蹭――啾嚕、嚕、嚕」; old_vn (CSV3) 「Ưm……chu――zuro――churu, ruu, ru.」; **fix = 「Ưm……chụt――zuro――chụt, ruu, ru.」**. Đổi: chu → chụt ; churu → chụt.

**2424** — JP 「ぴちょ、ぺちょ――ちゅうっ――ぺろろろっ！」; TW 「噗啾、呸啾――啾――呸囉！」; old_vn (CSV3) 「Picho, pecho――chuu――perororo!」; **fix = 「Picho, pecho――chụụt――perororo!」**. Đổi: chuu → chụụt.

#### 稀咲h2_プライベートルーム.txt.toml — 1 dòng

**1250** — JP 「そう、なんだ――だか、ら……んっ――ふあっ――\n特に……先っぽ――は――ねっ？ ――ん――ちゅぷっ」; TW 「就是這樣――所以呢……嗯――嗚啊――尤其是……頂端――知――道嗎？ ――嗯――啾噗」; old_vn (CSV3) 「Đúng, là vậy đó――Cho, nên…… ưm――fua――\nĐặc biệt là…… phần đỉnh――đó――nha? ――Ưm――chu pu」; **fix = 「Đúng, là vậy đó――Cho, nên…… ưm――fua――\nĐặc biệt là…… phần đỉnh――đó――nha? ――Ưm――chụt」**. Đổi: bỏ [chu, pu] → thêm [chụt].

### 4.7. T75+T77 — 18 dòng (8 file). GHÉP T75 + T77 trong cùng dòng — đổi từng token.

#### lr_ハチロクh1_今ひとたびの契り.txt.toml — 1 dòng

**1213** — JP 「ん……ちゅむっ――ちゅずっ――じゅっ――（こくっ）\n――ちゅむっ――れるっ――れろっ――ちゅりゅっ」; TW 「唔……啾唔——啾嘶——啾——（咽）啾唔——唔——唔——啾嚕」; old_vn (moan) 「Ưm…… chumu——chuzu——ju——(ực)\n——chumu——reru——rero——churyu」; **fix = 「Ưm…… chụt——chuzu——ju——(ực)\n——chụt——rộp——rero——churyu」**. Đổi: chumu → chụt ; chumu → chụt ; reru → rộp.

#### lr_日々姫h2_デザートは食事の前に.txt.toml — 2 dòng

**991** — JP 「あむっ――ちゅるっ――はむっ――ちゅっ――むっ――\nかぷっ――れるっ――あむっ――ぢゅるっ――はむっ！」; TW 「啊嗚……啾嚕、啾啾……啾嚕嚕嚕！啾嚕嚕……啾嚕……哈嗚！」; old_vn (CSV3) 「Amu——churu——hamu——chu——mu——\nKapu——reru——amu——juru——hamu!」; **fix = 「Amu——chụt——hamu——chụt——mu——\nKapu——rộp——amu——juru——hamu!」**. Đổi: churu → chụt ; chu → chụt ; reru → rộp.

**1038** — JP 「はむっ――れるっ――あむっ――ちゅうっ――はむっ、\nちゅっ――ふぁむっ――ちゅうっ――んっ――っ！！！」; TW 「啾嚕、啾啾……啾嚕嚕嚕！啾嚕嚕……啾嚕……咕啾！！！！」; old_vn (audit) 「Hamu——reru——amu——chuu——hamu,\nChu——famu——chuu——ưm——Ư!!!」; **fix = 「Hamu——rộp——amu——chụụt——hamu,\nChụt——famu——chụụt——ưm——Ư!!!」**. Đổi: reru → rộp ; chuu → chụụt ; chuu → chụụt ; chu → chụt.

#### lr_日々姫真闇h1_三人家族.txt.toml — 1 dòng

**1522** — JP 「むちゅっ――ちゅうっ――ぺろっ――れりゅっ――ちゅ\n――れるううっ――ぬろっ――じゅううっ――む、ちゅ」; TW 「唔啾——啾唔——滋溜——滋嚕——啾——滋嚕嚕——嚕唔——滋嚕嚕——唔、啾」; old_vn (CSV3) 「Muchu――chuu――pero――reryu――chu\n――reruuu――nuro――juuu――mu, chu」; **fix = 「Muchu――chụụt――pero――reryu――chụt\n――rộộộp――nuro――juuu――mu, chụt」**. Đổi: chuu → chụụt ; chu → chụt ; chu → chụt ; reruuu → rộộộp.

#### lr_稀咲h1_おしおきとごほうび.txt.toml — 3 dòng

**1041** — JP 「れりゅっ――ぺろっ――ちゅっ――ちゅむっ――\n（ぷあっ）、ん――ちゅうっ――ずちゅうっ――れるっ」; TW 「啾……啾嚕……啾……咕啾……噗哈……嗯……啾嚕、啾……」; old_vn (CSV3) 「Reryu――pero――chu――chumu――\n(pua), ưm――chuu――zuchuu――reru.」; **fix = 「Reryu――pero――chụt――chụt――\n(pua), ưm――chụụt――zuchuu――rộp.」**. Đổi: chu → chụt ; chumu → chụt ; chuu → chụụt ; reru → rộp.

**1054** — JP 「れる――れりゅっ――んっ――ぢゅずっ――（こくっ）\nぷぁ――好き――好き、好き――ん――ちゅ――ちゅう」; TW 「啾嚕……啾嚕……咕嘟……蛤啊……好喜歡你……喜歡……喜歡……啾」; old_vn (CSV3) 「Reru――reryu――ưm――juzu――(koku)\npua――thích――thích lắm, thích――ưm――chu――chuu.」; **fix = 「Rộp――reryu――ưm――juzu――(koku)\npua――thích――thích lắm, thích――ưm――chụt――chụụt.」**. Đổi: reru → rộp ; chu → chụt ; chuu → chụụt.

**1056** — JP 「ちゅうううううっ！ ずりゅっっっ！ ぢゅぼっ！\nれるっ――れろおおおおおっ！ ちゅうっ！ ぢゅっ！」; TW 「啾嚕嚕嚕！啾噗、啾！啾嚕嚕嚕……啾！啾！」; old_vn (unification đã gộp s3-moan-dialogue) 「Chuuuuu! Juryu! Jubo!\nReru――Reroooooo! Chuu! Ju!」; **fix = 「Chụụụụụụt! Juryu! Jubo!\nRộp――Reroooooo! Chụụt! Ju!」**. Đổi: chuuuuu → chụụụụụụt ; reru → rộp ; chuu → chụụt. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

#### ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml — 1 dòng

**838** — JP 「れるっ――ちゅううっ――んっ――ふっ――んっ――\nふっ――っん！ ふうっ！ んっ んんっ！！！」; TW 「咻嚕——啾嗚——嗯——呼——呼——嗯！呼！嗯嗯嗯！！！」; old_vn (moan) 「Mút——Chuuu——ưm——phù——ưm——\nphù——ưm! Phù! Ưm ưm ưm!!!」; **fix = 「Rộp——Chụụụt——ưm——phù——ưm——\nphù——ưm! Phù! Ưm ưm ưm!!!」**. Đổi: mút → rộp ; chuuu → chụụụt.

#### ハチロクh9_コノフクハキルコト.txt.toml — 3 dòng

**2122** — JP 「ちゅっ――じゅっ――じゅるっ――じゅううっ――\nんっ――れろおおっ――れるっ――れるううううっ」; TW 「啾——啾——啾嚕——吱吱嗚——嗯——嗯哦——咻嚕——咻嚕嗚嗚嗚」; old_vn (moan) 「Chu——ju——juru——juuu——\nƯm——rerooo——reru——reruuuuu」; **fix = 「Chụt——ju——juru——juuu——\nƯm——rerooo——rộp——rộộộộộp」**. Đổi: chu → chụt ; reru → rộp ; reruuuuu → rộộộộộp.

**2138** — JP 「ちゅむっ！ じゅっ！ じゅぼっ――んっ、ふっ、\nれるっ――ぢゅっ！ ぢゅぼっ！ じゅるううっ！」; TW 「啾姆！啾！呲啾——呼，咻嚕——呲啾！啾啵！啾嚕！」; old_vn (unification đã gộp s3-moan-dialogue) 「Chumu! Ju! Jubo——ưm, Fu,\nreru——ju! Jubo! Juruuu!」; **fix = 「Chụt! Ju! Jubo——ưm, Fu,\nrộp——ju! Jubo! Juruuu!」**. Đổi: chumu → chụt ; reru → rộp. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

**2140** — JP 「ちゅむっ、れるっ――ちゅううっ、ちゅるるっ――\nズズッ――んっ――ちゅっ――れろっ、れるうっ」; TW 「啾姆，咻嚕——啾嗚，啾嚕嚕——吹吹——啾——嗯，咻嚕」; old_vn (CSV3) 「Chumu, reru——chuuu, chururu——\nZuzu——ưm——chu——rero, reruu」; **fix = 「Chụt, rộp——chụụụt, chụt——\nZuzu——ưm——chụt——rero, rộộp」**. Đổi: chumu → chụt ; reru → chụt ; chuuu → chụt ; chururu → rộp ; chu → chụụụt ; reruu → rộộp.

#### 真闇h1_長期熟成.txt.toml — 1 dòng

**1048** — JP 「はぷっ――ンッ――れるっ――ちゅうっ――れろんっ」; TW 「啊嗚――嗯――舔――啾――舔」; old_vn (audit) 「Hapu――ưm――rột――chuu――rột.」; **fix = 「Hapu――ưm――rộp――chụụt――rột.」**. Đổi: rột → rộp ; chuu → chụụt.

#### 真闇h3_補習授業の廃校舎.txt.toml — 6 dòng

**2198** — JP 「ぺろっ――れろおおおっ――ぺろっ、ぺちゅっ。\nチュルッ――ちゅっ――れろおおおおっ――れるっ」; TW 「呸嘍――呸嘍――呸囉、呸啾。啾嚕――啾――呸嘍――舔」; old_vn (moan) 「Pero――reroooo――pero, pechu.\nChuru――chu――rerooooo――reru.」; **fix = 「Pero――reroooo――pero, pechu.\nChụt――chụt――rerooooo――rộp.」**. Đổi: churu → chụt ; chu → chụt ; reru → rộp.

**2290** — JP 「ちゅっ――れ、るっ――ちゅうっ――ちゅっ、ちゅむ\nちゅるうっ――ちゅるっ――れろっ――れるううっ」; TW 「啾――嚕、溜――啾――啾、啾啾嚕――啾――舔――嚕唔唔」; old_vn (CSV3) 「Chu――re, ru――chuu――chu, chumu\nchuruu――churu――rero――reruuu.」; **fix = 「Chụt――re, rộp――chụụt――chụt, chụt\nchụụt――chụt――rero――rộộộp.」**. Đổi: chu → chụt ; chu → chụt ; ru → chụt ; chuu → chụt ; chumu → rộp ; churuu → chụụt ; churu → chụụt ; reruuu → rộộộp. 「れ、るっ」 tách — giữ mảnh 're', chỉ đổi 'ru'→'rộp' (quy ước file giữ mảnh tách riêng).

**2292** — JP 「ちゅっっ――れるっ――れろ――ちゅる、る――\nん……すごか……ずっしり……ずっしり重かと」; TW 「啾――舔――嚕溜――啾嚕、溜――嗯……好厲害……好重……居然變得這麼重了」; old_vn (CSV3) 「Chu――reru――rero――churu, ru――\nưm……kinh quá……nặng trĩu……nặng trịch luôn.」; **fix = 「Chụt――rộp――rero――chụt, ru――\nưm……kinh quá……nặng trĩu……nặng trịch luôn.」**. Đổi: chu → chụt ; reru → chụt ; churu → rộp.

**2316** — JP 「んっ――ちゅっ――チュむっ――ちゅうっ――んっ\nれるっ――ちゅうっ――ちゅぱっ――ちゅ、むっ――」; TW 「嗯――啾――啾――啾――嗯舔――啾――啾啪――啾、唔――」; old_vn (CSV3) 「Ưm――chu――chumu――chuu――ưm\nreru――chuu――chupa――chu, mu――」; **fix = 「Ưm――chụt――chụt――chụụt――ưm\nrộp――chụụt――chụt――chụt, mu――」**. Đổi: chu → chụt ; chu → chụt ; chumu → chụt ; chuu → chụt ; chuu → chụụt ; reru → chụụt ; chupa → rộp.

**2348** — JP 「んふっ――んっ――はぁっ――ん――ちゅうっ――\nれるっ、れろおっ――ちゅ、ちゅむ――（かりっ！）」; TW 「嗯唔――嗯――哈――嗯――啾――舔、舔――啾、啾――（咬！）」; old_vn (CSV3) 「Ưm phư――ưm――haa――ưm――chu――\nrột, rero――chu, chumu――(Cắn!)」; **fix = 「Ưm phư――ưm――haa――ưm――chụụt――\nrộp, rero――chụt, chụt――(Cắn!)」**. Đổi: chu → chụụt ; chu → rộp ; rột → chụt ; chumu → chụt.

**2350** — JP 「んぷっ――んっ――れろっ――れろ、ずっ――じゅ、\nちゅっ――ちゅるう――ちゅ、れろっ――れるうっ」; TW 「嗯唔――嗯――舔――嚕囉、吱――啾、啾――啾嚕――啾、舔――舔」; old_vn (CSV3) 「Ưmpu――ưm――rero――rero, zu――ju,\nchu――churuu――chu, rero――reruu.」; **fix = 「Ưmpu――ưm――rero――rero, zu――ju,\nchụt――chụụt――chụt, rero――rộộp.」**. Đổi: chu → chụt ; chu → chụt ; churuu → chụụt ; reruu → rộộp.

### 4.8. T77 — 170 dòng (48 file). Token SFX れる/るっ → 'rộp' theo công thức (r + ộ×(1+số う/ぅ/ー) + p); れろ KHÔNG thuộc phạm vi (giữ theo F1-M68, U12a).

#### lr_れいなh1_レディ・れいな.txt.toml — 2 dòng

**1251** — JP 「あむっ――れるっ――ちゅるっ――ちゅっ――ちゅっ\n――ちゅむ。ん……今日はちょっとしょっぱいですねぇ」; TW 「啊唔——舔——啾——啾——啾——啾。嗯……今天有點鹹呢」; old_vn (CSV3) 「A mút——liếm——chu~——chụt——chụt\n——chu mút. Ưm…… hôm nay có hơi mặn một chút nha~」; **fix = 「A mút——rộp——chu~——chụt——chụt\n——chu mút. Ưm…… hôm nay có hơi mặn một chút nha~」**. Đổi: liếm → rộp.

**1266** — JP 「じゅぼっ！ ぼちゅっ！ じゅっ！ じゅろぉっ！\nれるっ――れりゅうっ！ ずっ！ ちゅばっ！ じゅぼ」; TW 「啾嗚噗啾！啾！刺溜！舔——舔舔！！ 呲溜！！ 啾啪！！ 啾嗚」; old_vn (CSV3) 「Chu mút! Chụt mút! Chụt! Chu mút t!\nLiếm——liếm m! Sụt! Chụt mút! Chu mút」; **fix = 「Chu mút! Chụt mút! Chụt! Chu mút t!\nRộp——liếm m! Sụt! Chụt mút! Chu mút」**. Đổi: liếm → rộp.

#### lr_ハチロクh2_新しい服。新しい旅.txt.toml — 2 dòng

**1715** — JP 「（れるううううううっ）――きゅぷっ！ ちゅぱっ――\nじゅぼっ！ じゅっ！ じゅぶっ！ ぶっ！ じゅち！」; TW 「（呲溜————）啾噗！啾啪、啾噗！啾！啾噗！噗！啾溜！」; old_vn (moan) 「（Reruuuuuuu）——Chụt! Chụt——\nChụt! Chụt! Chụt! Phụt! Chụt!」; **fix = 「（Rộộộộộộộp）——Chụt! Chụt——\nChụt! Chụt! Chụt! Phụt! Chụt!」**. Đổi: reruuuuuuu → rộộộộộộộp.

**1716** — JP 「（ぬとおおおっ――れるっ――じゅるるるるっ）\nじゅぶっ！ ぼちゅっ！ じゅぶっ！ じゅばっ！」; TW 「（溜、溜、啾溜）啾噗！噗啾！啾噗！啾啪！」; old_vn (audit) 「（Nụtọooo——liếm——Chùn chụt）\nChụt! Phụt! Chụt! Phụt!」; **fix = 「（Nụtọooo——rộp——Chùn chụt）\nChụt! Phụt! Chụt! Phụt!」**. Đổi: liếm → rộp.

#### lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml — 3 dòng

**1278** — JP 「ちゅうっ――ちゅうっ――れるっ――ちゅうっ――\nちゅむっ――れるっ――ちゅむっ――れりゅんっ！」; TW 「啾、啾、溜、啾、啾、溜、啾唔、溜！」; old_vn (audit) 「Chụụt——chụụt——liếm——chụụt——chụt——liếm——chụt——liếm!」; **fix = 「Chụụt——chụụt——rộp——chụụt——chụt——rộp——chụt——liếm!」**. Đổi: liếm → rộp ; liếm → rộp.

**1281** — JP 「ちゅっ――ちゅむっ――ちゅっ――ぺろっ――\nれろっ――ちゅうっ――れろっ――れるっ」; TW 「啾、啾唔、啾、溜、溜、啾嗚、溜、溜」; old_vn (audit) 「Chụt——chụt——chụt——liếm—— liếm——chụụt——liếm——liếm」; **fix = 「Chụt——chụt——chụt——liếm—— liếm——chụụt——liếm——rộp」**. Đổi: liếm → rộp.

**1283** — JP 「ちゅむっ――ちゅうっ――ちゅるっ――ちゅっ――\nちゅむっ――れろっ――れるうっ――ちゅうう～～」; TW 「啾、啾唔、啾溜、啾、啾嗚、溜、溜……啾嗚～～」; old_vn (audit) 「Chụt——chụụt——chụt——chụt—— chụt——liếm——liếm——chụụụ~~」; **fix = 「Chụt——chụụt——chụt——chụt—— chụt——liếm——rộộp——chụụụ~~」**. Đổi: liếm → rộộp.

#### lr_凪h2_虎さんの交尾.txt.toml — 13 dòng

**1282** — JP 「ちゅっ――ちゅむうっ――れるっ――れりゅううう――\nちゅむっ――れるっ――ちゅっ――ちゅううっ――ん」; TW 「啾……啾……啾……啾……啾……啾……啾……啾……」; old_vn (CSV3) 「Chụt——chụt——liếm——liếm——\nchụt——liếm——chụt——chụt——ưm」; **fix = 「Chụt——chụt——rộp——liếm——\nchụt——rộp——chụt——chụt——ưm」**. Đổi: liếm → rộp ; liếm → rộp.

**1283** — JP 「れるっ――れろっ――にゅぶっ――じゅるっ――\nんっ――～～～～～～――んっ――ちゅうっ――れるっ」; TW 「啾……啾……啾……啾……嗯……嗯……啾……啾」; old_vn (CSV3) 「Liếm——liếm——nhóp nhép——nhóp nhép——\nưm——~~~~~~——ưm——chụt——liếm」; **fix = 「Rộp——liếm——nhóp nhép——nhóp nhép——\nưm——~~~~~~——ưm——chụt——rộp」**. Đổi: liếm → rộp ; liếm → rộp.

**1285** — JP 「ちゅうっ――ちゅむっ――れるっ――れろおっ――\nじゅ――ずじゅうううっ――（こくっ）――ぷあっ」; TW 「啾……啾，啾，啾……啾，啾……（咕咚）啊……」; old_vn (CSV3) 「Chụt——chụt——liếm——liếm——\nju——zujuuu——（Ực）——pua」; **fix = 「Chụt——chụt——rộp——liếm——\nju——zujuuu——（Ực）——pua」**. Đổi: liếm → rộp.

**1288** — JP 「ちゅ！ ん――ちゅるっ――にゅぶ――にゅっ――\nれろっ――れるうっ――にゅりゅううう――！！！？」; TW 「啾！嗯……啾……啾……啾……啾……啾……啾……」; old_vn (CSV3) 「Chụt! Ưm——chụt——nhóp nhép——nhóp nhép——\nliếm——liếm——nhóp nhép——!!!?」; **fix = 「Chụt! Ưm——chụt——nhóp nhép——nhóp nhép——\nliếm——rộộp——nhóp nhép——!!!?」**. Đổi: liếm → rộộp.

**1290** — JP 「ん……ひーはむ……ンっ――ひゅき――ちゅっ――\nれるっ――ちゅうう――れるうううっ――ちゅむっ」; TW 「嗯……啊唔……嗯……嘶……啾……啾，啾……啾……啾」; old_vn (CSV3) 「Ưm……hi-hamu……ưm——hyuki——chụt——\nliếm——chụt——liếm——chụt」; **fix = 「Ưm……hi-hamu……ưm——hyuki——chụt——\nrộp——chụt——rộộộộp——chụt」**. Đổi: liếm → rộp ; liếm → rộộộộp.

**1292** — JP 「ンッ――ちゅっ――ちゅむっ――ちゅうっ――\nれろっ――れりゅっ――れろっ――れるうっ」; TW 「嗯……啾，啾，啾……啾，啾，啾，啾」; old_vn (CSV3) 「Ưm——chụt——chụt——chụt——\nliếm——liếm——liếm——liếm」; **fix = 「Ưm——chụt——chụt——chụt——\nliếm——liếm——liếm——rộộp」**. Đổi: liếm → rộộp.

**1308** — JP 「んへへ――にぃさぁん――ちゅっ！ ちゅむっ――\nれろっ――れるううっ――にゅちゅっ――ちゅうっ！」; TW 「嘿嘿嘿……大哥哥，親一個！啾……啾，啾，啾！」; old_vn (CSV3) 「Nhehe——anh Soutetsu——chụt! Chụt——\nliếm——liếm——nhóp nhép——chụt!」; **fix = 「Nhehe——anh Soutetsu——chụt! Chụt——\nrộộộp——liếm——nhóp nhép——chụt!」**. Đổi: liếm → rộộộp.

**1804** — JP （にゅぶうううっ――れるっ――れろおお――くりゅ）; TW （吸溜，啾，啾，啾）; old_vn (unification đã gộp s3-sfx-counting) （Nhóp nhéppp——liếm——liếm——ngoáy）; **fix = （Nhóp nhéppp——rộp——liếm——ngoáy）**. Đổi: liếm → rộp. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

**1808** — JP （はむっ！ ちゅうううっ！ ちゅるっ！ れるっ！）; TW （咬！吻！吸！舔！）; old_vn (unification đã gộp s3-sfx-counting) （Ngoạm! Chụttt! Mút! Liếm!）; **fix = （Ngoạm! Chụttt! Mút! Rộp!）**. Đổi: liếm → rộp. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

**1846** — JP （れるっ――くりゅ！ れろおっ――くりゅん！！）; TW （舔……轉！舔……轉！）; old_vn (CSV3) （Liếm——ngoáy! Liếm——ngoáy!!）; **fix = （Rộp——ngoáy! Liếm——ngoáy!!）**. Đổi: liếm → rộp.

**1848** — JP （れるううっっっ！ くりゅんっ！！！！！！）; TW （舔！轉！！！）; old_vn (unification đã gộp s3-sfx-counting) （Liếmm! Ngoáy!!!!!!）; **fix = （Rộộộp! Ngoáy!!!!!!）**. Đổi: liếmm → rộộộp. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

**1851** — JP （れるっっ――れろおおっ――くりゅ！ ちゅ、ちゅっ）; TW （舔，舔……轉！舔，舔）; old_vn (CSV3) （Liếm——liếm——ngoáy! Chụt, chụt）; **fix = （Rộp——liếm——ngoáy! Chụt, chụt）**. Đổi: liếm → rộp.

**1853** — JP （ちゅむっ――ちゅうっ――れるっ――ちゅぱっ）; TW （舔，舔，舔，舔）; old_vn (CSV3) （Chụt——chụt——liếm——chụt）; **fix = （Chụt——chụt——rộp——chụt）**. Đổi: liếm → rộp.

#### lr_凪ふかみh1_じぇいけい！.txt.toml — 11 dòng

**1403** — JP 「かわい。凪ちゃん――ちゅっ――れるっ――れろっ――\nちゅむ――ちゅうっ――ぺろっ――れるっ――じゅるっ」; TW 「你真可愛，小凪。啾……啾……啾……啾，啾，啾，啾，啾」; old_vn (CSV3) 「Dễ thương quá. Nagi——chụt——liếm——liếm——\nchụt——chụt——liếm——liếm——mút」; **fix = 「Dễ thương quá. Nagi——chụt——rộp——liếm——\nchụt——chụt——liếm——rộp——mút」**. Đổi: liếm → rộp ; liếm → rộp.

**1513** — JP 「ふぁ――ふかみちゃん、ふかみちゃん……ん……\nちゅっ――れるっ――れろっ――ん――ちゅう――ちゅ」; TW 「哇……小深，小深……嗯……啾，啾，啾，嗯……啾，啾」; old_vn (moan) 「Fa——Fukami, Fukami……ưm……\nChụt——liếm——liếm——ưm——chụt——chụt」; **fix = 「Fa——Fukami, Fukami……ưm……\nChụt——rộp——liếm——ưm——chụt——chụt」**. Đổi: liếm → rộp.

**1630** — JP 「れろっ――れるっ――くりゅっ――くりゅんっ――\nちゅ――ぺろっ――ん……れるうっ――れろ、れりゅっ」; TW 「啾……啾，啾，啾……（吻，舔）唔……啾……啾，啾」; old_vn (CSV3) 「Liếm——liếm——ngoáy——ngoáy——\nchụt——liếm——ưm……liếm——liếm, liếm」; **fix = 「Liếm——rộp——ngoáy——ngoáy——\nchụt——liếm——ưm……rộộp——liếm, liếm」**. Đổi: liếm → rộp ; liếm → rộộp.

**1641** — JP 「れろっ――くりゅっ――れろっ――つうぅぅぅぅっ――\nれるうっ――れろっ！ ――れりゅつっ――くちゅっ！」; TW 「啾，啾，啾，啾……啾，啾！啾……啾！」; old_vn (CSV3) 「Liếm——ngoáy——liếm——mút——\nliếm——liếm! ——Liếm——nhóp nhép!」; **fix = 「Liếm——ngoáy——liếm——mút——\nrộộp——liếm! ——Liếm——nhóp nhép!」**. Đổi: liếm → rộộp.

**1643** — JP 「れろっ――じゅりゅっ――ぺろっ――れるっ――\nじゅっ――じゅりゅううううう――（こくっ）――ぷぁ」; TW 「啾，啾，啾，啾，啾，啾……（咕咚）哇」; old_vn (CSV3) 「Liếm——mút——liếm——liếm——\nmút——mútttttt——（Ực）——pua」; **fix = 「Liếm——mút——liếm——rộp——\nmút——mútttttt——（Ực）——pua」**. Đổi: liếm → rộp.

**1644** — JP 「れりゅっ――ちゅっ――んチュッ――ちゅるっ――\nん……ちゅむっ――ちゅうっ――れるっ――じゅりゅっ」; TW 「啾，啾，啾，啾，嗯……啾，啾，啾，啾」; old_vn (CSV3) 「Liếm——chụt——ưm chụt——mút——\nưm……chụt——chụt——liếm——mút」; **fix = 「Liếm——chụt——ưm chụt——mút——\nưm……chụt——chụt——rộp——mút」**. Đổi: liếm → rộp.

**1646** — JP 「ちゅむっ――ちゅっ――れるっ――れろっ――んっ――\nじゅ――ずっ――ずじゅううううっ――こくっ――ぷぁ」; TW 「啾，啾，啾，啾，嗯，啾，滋，滋，咕咚……哇」; old_vn (CSV3) 「Chụt——chụt——liếm——liếm——ưm——\nju——zu——zujuuuuu——（Ực）——pua」; **fix = 「Chụt——chụt——rộp——liếm——ưm——\nju——zu——zujuuuuu——（Ực）——pua」**. Đổi: liếm → rộp.

**1647** — JP 「れるっ――れろっ――れりゅっ――じゅりゅ――\n（こくっ）――ぷは、精液、結構たくさんとね～」; TW 「啾，啾，啾，啾，（咕咚）哇，好多的精液啊」; old_vn (CSV3) 「Liếm——liếm——liếm——mút——\n（Ực）——Puha, tinh dịch, nhiều phết đấy nhỉ~」; **fix = 「Rộp——liếm——liếm——mút——\n（Ực）——Puha, tinh dịch, nhiều phết đấy nhỉ~」**. Đổi: liếm → rộp.

**1660** — JP 「ん……れろおっ――れりゅうっ――レロおっ――\nふっ――んっ――れろおっ――れるううっ――れろおお」; TW 「嗯……啾，啾，啾……呼……嗯……啾，啾，啾」; old_vn (CSV3) 「Ưm……liếm——liếm——liếm——\nfu——ưm——liếm——liếm——liếm」; **fix = 「Ưm……liếm——liếm——liếm——\nfu——ưm——liếm——rộộộp——liếm」**. Đổi: liếm → rộộộp.

**1661** — JP 「ん……ちゅっ――ちゅむっ――ちゅううっ――れるっ、\nれろっ、れりゅっ――ちゅむっ――ちゅっ、ちゅっ」; TW 「嗯……啾，啾，啾，啾，啾，啾，啾，啾，啾」; old_vn (CSV3) 「Ưm……chụt——chụt——chụt——liếm,\nliếm, liếm——chụt——chụt, chụt」; **fix = 「Ưm……chụt——chụt——chụt——rộp,\nliếm, liếm——chụt——chụt, chụt」**. Đổi: liếm → rộp.

**1670** — JP 「うん――ちゅっ――ちゅうっ――れるっ――れろっ」; TW 「嗯，啾，啾，啾，啾」; old_vn (CSV3) 「Ừm——chụt——chụt——liếm——liếm」; **fix = 「Ừm——chụt——chụt——rộp——liếm」**. Đổi: liếm → rộp.

#### lr_日々姫h2_デザートは食事の前に.txt.toml — 9 dòng

**1016** — JP 「ちゅむっ――れるうっ――ちゅっ――ちゅっ、ちゅっ、\nれりゅううっ――れろっ――ちゅうううううううっ！！」; TW 「啾……啾……啾嚕嚕嚕……啾嚕……啾嚕……咕嘟……啾！！！」; old_vn (audit) 「Chụt——reruu——chụt——chụt, chụt,\nreryuuu——rero——chuuuuuuuu!!」; **fix = 「Chụt——rộộp——chụt——chụt, chụt,\nreryuuu——rero——chuuuuuuuu!!」**. Đổi: reruu → rộộp.

**1033** — JP 「れるっ――じゅぶっ――じゅむっ――るっ――ぶっ――\n『ひゃばば、ばふぃっ』、ぷぁっ――ぷっ――じゅるっ」; TW 「啾嚕……啾噗……啾嚕……對不起了……啾……啾嚕」; old_vn (CSV3) 「Liếm——nhóp nhép——mút——liếm——phập——\n『Hyababa, bafi』, pua——pu——nhóp nhép.」; **fix = 「Rộp——nhóp nhép——mút——rộp——phập——\n『Hyababa, bafi』, pua——pu——nhóp nhép.」**. Đổi: liếm → rộp ; liếm → rộp. るっ BIÊN: TW toàn âm miệng + CUR 'liếm' → xếp LICKING; nhưng kề ぶっ (thrust) — coordinator xem lại nếu cần.

**1036** — JP 「あ～～――ん～――れるっ――ぺりゅっ――ん……\nれりゅうううっ――れるっ――ぺろっ――れちゅんっ」; TW 「啾嚕、啾啾……啾嚕嚕嚕！啾嚕嚕……啾嚕……咕啾」; old_vn (audit) 「A~~——ưm~——liếm——nhóp nhép——ưm……\nReryuuuu——liếm——liếm nhẹ——rechun」; **fix = 「A~~——ưm~——rộp——nhóp nhép——ưm……\nReryuuuu——rộp——liếm nhẹ——rechun」**. Đổi: liếm → rộp ; liếm → rộp.

**1039** — JP 「ぺろっ――れるっ――んちゅっ――れるっ――ぺろっ、\nれりゅ――ちゅむっ――ちゅっ――ちゅううううっ！」; TW 「啾嚕、啾嚕、啾嚕……咕啾、啾……啾噗……啾嚕嚕嚕！」; old_vn (CSV3) 「Liếm——liếm——nchu——liếm——liếm nhẹ,\nreryu——chụt——chụt——chuuuuu!」; **fix = 「Liếm——rộp——nchu——rộp——liếm nhẹ,\nreryu——chụt——chụt——chuuuuu!」**. Đổi: liếm → rộp ; liếm → rộp.

**1042** — JP 「ん……はぁ――んっ――ちゅむっ――れろっ――ちゅっ、\nれりゅううっ――れろっ――しゃぶっ――れるううっ」; TW 「啾嚕嚕嚕……啾嚕……啾嚕……咕嘟。啾、啾嚕、啾嚕嚕……啾嚕嚕嚕」; old_vn (audit) 「Ưm…… ha——ưm——chụt——rero——chụt,\nreryuuu——rero——mút——reruuu」; **fix = 「Ưm…… ha——ưm——chụt——rero——chụt,\nreryuuu——rero——mút——rộộộp」**. Đổi: reruuu → rộộộp.

**1045** — JP 「ちゅううううううっ！ んっ……ごくっ――ふ、あ\n――れるっ――れろおおっ――チュむっ――ちゅううっ」; TW 「啾嚕！啾噗！啾嚕嚕嚕！咕嘟……啾、啾、啾……噗啾！」; old_vn (unification đã gộp s3-fa-fu) 「Chuuuuuuu! Ưm…… ực——Fu, a\n——liếm——rerooo——chụt——chuuu」; **fix = 「Chuuuuuuu! Ưm…… ực——Fu, a\n——rộp——rerooo——chụt——chuuu」**. Đổi: liếm → rộp. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

**1046** — JP 「れっるっ――ぺろっ――ちゅっ――ちゅううっ――\nん……ぺろっ――れりゅっ――ぺろっ――じゅずうっ！」; TW 「啾嚕！啾噗！啾嚕嚕嚕！咕嘟……啾、啾、啾、啾嚕嚕嚕！！」; old_vn (audit) 「Liếm——liếm nhẹ——chụt——chuuu——\nƯm…… liếm nhẹ——reryu——liếm nhẹ——juzuu!」; **fix = 「Rộp——liếm nhẹ——chụt——chuuu——\nƯm…… liếm nhẹ——reryu——liếm nhẹ——juzuu!」**. Đổi: liếm → rộp. れっるっ — biến thể lắp của るっ → 'Rộp'.

**1053** — JP 「ちゅろおおおおっ――れるっ――ちゅっ、チュッ――\nちゅむっ――れるっ――ちゅずっ――ず、ずうううっ」; TW 「嗯……啾……啾嚕……啾……啾嚕嚕……啾嚕……」; old_vn (CSV3) 「Churooooo——liếm——chụt, chụt——\nChụt——liếm——chuzu——zu, zuuuu」; **fix = 「Churooooo——rộp——chụt, chụt——\nChụt——rộp——chuzu——zu, zuuuu」**. Đổi: liếm → rộp ; liếm → rộp.

**1675** — JP （ぷりゅっ！ れるっ！ じゅぶっ！ ぷりゅんっっ！）; TW （啾嚕、啾嚕、啾嚕、啾嚕！）; old_vn (CSV3) （Bật ra! Liếm! Nhóp nhép! Bật ra!）; **fix = （Bật ra! Rộp! Nhóp nhép! Bật ra!）**. Đổi: liếm → rộp.

#### lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml — 2 dòng

**1475** — JP 「ん――ちゅっ――ちゅむっ――ちゅう――れるっ――\nれりゅううっ――じゅるっ――じゅ――ずりゅ――るっ」; TW 「嗯——啾——啾唔——啾嗚——滋溜——滋溜——啾嚕——啾——滋溜——滋溜」; old_vn (moan) 「Ưm――chụt――chùn chụt――chụt――rê ru――\nrê ryuuu――chùn chụt――chu――zuryu――ru」; **fix = 「Ưm――chụt――chùn chụt――chụt――rộp――\nrê ryuuu――chùn chụt――chu――zuryu――ru」**. Đổi: bỏ [rê, ru] → thêm [rộp]. るっ cuối: chuỗi thrust/slide (ずりゅ) → thuộc T78, GIỮ 'ru'; chỉ đổi れるっ → 'rộp'.

**1477** — JP 「ん――れるっ――れろっ――ちゅむっ――ちゅっ――\nん……ちゅうっ――じゅるっ――（こくっ）――ぷ、あ」; TW 「嗯——滋溜——滋溜——啾唔——啾——嗯……啾唔——啾嚕——（嚥下）——噗、啊」; old_vn (CSV3) 「Ưm――rê ru――rê rô――chùn chụt――chụt――\nƯm…… chụt――chùn chụt――（Ực）――pu, a」; **fix = 「Ưm――rộp――rê rô――chùn chụt――chụt――\nƯm…… chụt――chùn chụt――（Ực）――pu, a」**. Đổi: bỏ [rê, ru] → thêm [rộp].

#### lr_日々姫真闇h1_三人家族.txt.toml — 3 dòng

**1573** — JP 「ちゅっ――んっ――れるっ――れりゅっ――ちゅりゅっ、\nちゅ――むちゅうっ――れりゅうっ――ちゅ、ちゅずっ」; TW 「啾——嗯——滋溜——滋咧——啾溜，啾——唔啾——滋溜——啾，啾茲」; old_vn (CSV3) 「Chụt――ưm――rê ru――rê ryu――churyu,\nchu――muchuu――reryuu――chu, chuzu」; **fix = 「Chụt――ưm――rộp――rê ryu――churyu,\nchu――muchuu――reryuu――chu, chuzu」**. Đổi: bỏ [rê, ru] → thêm [rộp].

**1579** — JP 「ん……『あーーーーーーーん』 あむっ――っ――\nちゅるっ――れるっ――れるっ――ちゅぶっ――れりゅ」; TW 「嗯……“啊————嗯”啊嗯——唔——啾嚕——滋溜——滋溜——啾噗——滋溜」; old_vn (audit) 「Ưm…… 'Aaaaaaaan' Amu――Ư――\nChụt――rê ru――rê ru――chùn chụt――rê ryu」; **fix = 「Ưm…… 'Aaaaaaaan' Amu――Ư――\nChụt――rộp――rộp――chùn chụt――rê ryu」**. Đổi: bỏ [rê, rê, ru, ru] → thêm [rộp, rộp].

**1585** — JP 「ん……ちゅっ――れりゅっ――ちゅるっ――じゅゆうっ\n――れるうっ――れろっ――ちゅっ――ちゅずっ、ずっ」; TW 「嗯……啾——滋溜——啾嚕——啾唔唔——滋溜——滋溜——啾——啾滋、滋」; old_vn (CSV3) 「Ưm…… chụt――reryu――chụt――juyuu\n――reruu――rero――chụt――chuzu, zu」; **fix = 「Ưm…… chụt――reryu――chụt――juyuu\n――rộộp――rero――chụt――chuzu, zu」**. Đổi: reruu → rộộp.

#### lr_真闇h1_僕のおねえちゃん.txt.toml — 3 dòng

**1477** — JP 「ちゅっ――ちゅむっ――ちゅうっ――れるっ――\nれろおっ、れりゅっ――ちゅう――ずっ――ぷあっ」; TW 「啾——啾嗯——啾——舔舔——舔舔，啾啾——啾啾，啾——呼啊」; old_vn (CSV3) 「Chụt——chụt——chụt——rột——\nrột, rột——chụt——chụt——phuha」; **fix = 「Chụt——chụt——chụt——rộp——\nrột, rột——chụt——chụt——phuha」**. Đổi: rột → rộp.

**1507** — JP 「んっ――れるっ――んちゅっ――れりゅんっ！」; TW 「嗯——舔——嗯——啾！」; old_vn (CSV3) 「Ưm——liếm——nchu——liếm!」; **fix = 「Ưm——rộp——nchu——liếm!」**. Đổi: liếm → rộp.

**1655** — JP 「れるうううっ――ちゅっ――く、りゅ――ずりゅっ！\nむちょっ――ぺろっ――くりゅっ、く――ずりゅん！！」; TW 「舔舔舔舔……啾——……轉動——滋溜……！啾啾——舔舔——轉動——滋溜！！」; old_vn (CSV3) 「Liếm——chụt——ku, ryu——trơn tuột!\nChụt——liếm——xoay, ku——trơn tuột!!」; **fix = 「Rộộộộp——chụt——ku, ryu——trơn tuột!\nChụt——liếm——xoay, ku——trơn tuột!!」**. Đổi: liếm → rộộộộp.

#### lr_稀咲ポーレットh1_悪い大人の契約.txt.toml — 4 dòng

**1585** — JP 「ちゅっ―れるっ―ちゅうっ―ちゅむっ―\nちゅぱっ―ちゅうっ！ ちゅぶっ！ ちゅううっ！」; TW 「啾——舔——啾——啾——啾啪——啾！ 啾噗！ 啾啾！」; old_vn (CSV3) 「Chụt——rê ru——chuu u——chu mu——\nchu pa——chuu u! Chu bu! Chuu u!」; **fix = 「Chụt——rộp——chuu u——chu mu——\nchu pa——chuu u! Chu bu! Chuu u!」**. Đổi: bỏ [rê, ru] → thêm [rộp].

**1587** — JP 「ちゅううっ、ちゅっ―んっ―れるっ―れりゅっ、\nちゅううううっ―ずちゅううっ―れるっ、れりゅっ」; TW 「啾啾、啾——嗯——舔——舔舔、啾啾啾——滋啾——舔舔、舔舔」; old_vn (CSV3) 「Chuu u, chụt——ưm——rê ru——rê ryu,\nchuu u uu——zu chuu u——rê ru, rê ryu」; **fix = 「Chuu u, chụt——ưm——rộp——rê ryu,\nchuu u uu——zu chuu u——rộp, rê ryu」**. Đổi: bỏ [rê, rê, ru, ru] → thêm [rộp, rộp].

**1820** — JP 「れりゅっ―ちゅっ―ちゅうううっ―れるっ―\nれるっ―ぺろおおっ―ちゅっ―ちゅううううっ」; TW 「舔——啾——啾啾啾——舔舔——舔舔——啾啾——啾啾——啾——啾啾啾」; old_vn (CSV3) 「Rê ryu——chụt——chuu u uu——rê ru——\nrê ru——pê ro oo——chụt——chuu u uu」; **fix = 「Rê ryu——chụt——chuu u uu——rộp——\nrộp——pê ro oo——chụt——chuu u uu」**. Đổi: bỏ [rê, rê, ru, ru] → thêm [rộp, rộp].

**1821** — JP 「れるっ―れろっ―れりゅっ―りゅっ―\nちゅうっ―ちゅっ―ぺろっっ―ぺちゅっ―」; TW 「舔——舔——啾——啾——啾——啾——舔——舔——」; old_vn (CSV3) 「Rê ru——rê ro——rê ryu——ryu——\nchuu u——chụt——pê ro——pê chu——」; **fix = 「Rộp——rê ro——rê ryu——ryu——\nchuu u——chụt——pê ro——pê chu——」**. Đổi: bỏ [rê, ru] → thêm [rộp].

#### lrれいな追加h_夜の花嫁修業.txt.toml — 2 dòng

**1138** — JP 「あむっ――ちゅ――ちゅうっ――ちゅぶっ――ん……\nれるっ――れろっ――ちゅむっ――ちゅうっ――れるっ」; TW 「啊嗚——啾——啾唔——啾噗——嗯……咧溜——滋溜——啾唔——啾——咧溜」; old_vn (CSV3) 「Ngoạm——chụt——chụt——chụt——ưm……\nLiếm——liếm——chụt——chụt——liếm」; **fix = 「Ngoạm——chụt——chụt——chụt——ưm……\nRộp——liếm——chụt——chụt——rộp」**. Đổi: liếm → rộp ; liếm → rộp.

**1152** — JP 「ちゅうっ――ちゅむっ――じゅずっ――（こくっ）\nれるっ、れろっ――れりゅううっ――（ごくんっ）」; TW 「啾——啾唔——滋溜——（吞嚥）咧溜、滋溜——滋溜溜——（吞嚥））」; old_vn (CSV3) 「Chụt——chụt——sụp soạp——（Ực）\nLiếm, liếm——liếm——（Ực）」; **fix = 「Chụt——chụt——sụp soạp——（Ực）\nRộp, liếm——liếm——（Ực）」**. Đổi: liếm → rộp.

#### lr真闇追加h_赤ちゃん、欲しか.txt.toml — 7 dòng

**1135** — JP 「れりゅううっ――ちゅっ――ちゅずずっ――（ごくっ）\nん……ちゅっ――ちゅううっ――れるっ――れりゅうう」; TW 「啾嚕——啾——啾噗——咕嚕——嗯……啾——啾——啾嚕——啾噗」; old_vn (audit) "「Liếm liếm——chụt——chùn chụt——（Ực）\nƯm……chụt——chụụụt——liếm——liếm liếm.」"; **fix = "「Liếm liếm——chụt——chùn chụt——（Ực）\nƯm……chụt——chụụụt——rộp——liếm liếm.」"**. Đổi: liếm → rộp.

**1162** — JP 「んむっ――ちゅっ――れるっ――れるうっっ」; TW 「嗯唔——啾——啾嚕——啾嚕」; old_vn (CSV3) "「Ưm——chụt——liếm——liếm liếm.」"; **fix = "「Ưm——chụt——rộp——rộộp.」"**. Đổi: bỏ [liếm, liếm, liếm] → thêm [rộp, rộộp].

**1817** — JP （れるっ――れろっ――にゅるうっ――ぬじゅるっっ）; TW （反覆舔舐）; old_vn (CSV3) （Liếm——liếm——nhóp nhép——nhóp nhép）; **fix = （Rộp——liếm——nhóp nhép——nhóp nhép）**. Đổi: liếm → rộp.

**1818** — JP （ん――ちゅぶっ――れるっ――れるれるれるれるっ）; TW （吸來吸去）; old_vn (CSV3) （Ưm——chụt——liếm——liếm liếm liếm liếm）; **fix = （Ưm——chụt——rộp——rộp rộp rộp rộp）**. Đổi: liếm → rộp ; liếm → rộp ; liếm → rộp ; liếm → rộp ; liếm → rộp.

**1861** — JP （ちゅっ――ちゅうっ――れるっ――ちゅむっ）; TW （用力吸吮）; old_vn (CSV3) （Chụt——chùn chụt——liếm——chụt）; **fix = （Chụt——chùn chụt——rộp——chụt）**. Đổi: liếm → rộp.

**1877** — JP （れろっ――ちゅっ――ちゅうっ――れるうううっっ）; TW （舔來舔去）; old_vn (unification đã gộp s3-sfx-counting) （Liếm——chụt——chùn chụt——liếm liếmmm）; **fix = （Liếm——chụt——chùn chụt——rộộộộp）**. Đổi: bỏ [liếm, liếmmm] → thêm [rộộộộp]. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

**1879** — JP （れるっ）; TW （舔動）; old_vn (CSV3) （Liếm）; **fix = （Rộp）**. Đổi: liếm → rộp.

#### lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml — 1 dòng

**1819** — JP （ぺろっ――れるっ――ちゅむっ――ずちゅううううっ）; TW （反覆舔拭）; old_vn (moan) （Liếm――liếm――chụt――Zuchuuuuu）; **fix = （Liếm――rộp――chụt――Zuchuuuuu）**. Đổi: liếm → rộp.

#### lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml — 3 dòng

**1527** — JP 「ちゅぶっ――ちゅうっ――れるっ――れりゅうっ――\nちゅうっ――ちゅっ――ちゅむむぅっ――ぷあっ」; TW 「嗯……啾——咧溜——滋溜——嗯啾——啾——啾——啾嚕嚕」; old_vn (moan) 「Chubu——Chuu——Reru——Reryuu——\nChuu——chụt——Chumumuu——Pua」; **fix = 「Chubu——Chuu——Rộp——Reryuu——\nChuu——chụt——Chumumuu——Pua」**. Đổi: reru → rộp.

**2184** — JP 「ん……ちゅっ――れるっ――れろっ――んっ――\nちゅむっ――ちゅうっ――ちゅっ――じゅるるうっ」; TW 她們深情地吻在了一起，激烈程度與剛才的簡直有著天壤之別——; old_vn (moan) 「Ưm……chụt——Reru——Rero——ưm——\nChumu——Chuu——chụt——Jururuu」; **fix = 「Ưm……chụt——Rộp——Rero——ưm——\nChumu——Chuu——chụt——Jururuu」**. Đổi: reru → rộp.

**2331** — JP 「ちゅっ――れるっ――じゅぶっ――ちゅぼおおおっ――\nちゅるっ――れるっ――くぷうううううっ――ぷあっ」; TW 電車公主含著假陽具的同時前後搖頭……表情看過去似乎有點痛苦——但不知為何這幅場景卻美如畫。; old_vn (moan) 「Chụt——Reru——Jubu——Chuboooo——\nChuru——Reru——Kupuuuuuu——Pua」; **fix = 「Chụt——Rộp——Jubu——Chuboooo——\nChuru——Rộp——Kupuuuuuu——Pua」**. Đổi: reru → rộp ; reru → rộp.

#### ふかみh1_ともはり練習.txt.toml — 4 dòng

**1035** — JP 「ちゅむっ――ちゅっ――ちゅうう――ちゅるっ――\nれるっ――れろっ――れろおおっ――ちゅううっ」; TW 「啾……啾……啾……啾……啾……啾……啾……啾」; old_vn (CSV3) 「Chụt bụp——chụt——chụt——chụt——\nLiếm——liếm——liếm liếm liếm——chụt」; **fix = 「Chụt bụp——chụt——chụt——chụt——\nRộp——liếm——liếm liếm liếm——chụt」**. Đổi: liếm → rộp.

**1036** — JP 「れるっ――ぢゅっ！ ぢゅぼっ！ ぼちゅっ！\nじゅるっ！ じゅっ！ じゅうっ！ じゅるんっ！！」; TW 「啾……啾！啾！啾！啾！啾！啾！啾嗯！！」; old_vn (CSV3) 「Liếm——chụt! Nhóp nhép! Bụp!\nChụt rột! Chụt! Chụt! Chụt rột!!」; **fix = 「Rộp——chụt! Nhóp nhép! Bụp!\nChụt rột! Chụt! Chụt! Chụt rột!!」**. Đổi: liếm → rộp.

**1037** — JP 「じゅっ！ じゅるっ！ でゅぶっ！ じゅうっ！\nんっ――れろっ――れるっ――れろおおっ――ぢゅぶ！」; TW 「啾！啾！噗！啾！嗯……啾……啾……啾……噗！」; old_vn (CSV3) 「Chụt! Chụt rột! Rột! Chụt!\nƯm——liếm——liếm——liếm liếm liếm——nhóp nhép!」; **fix = 「Chụt! Chụt rột! Rột! Chụt!\nƯm——liếm——rộp——liếm liếm liếm——nhóp nhép!」**. Đổi: liếm → rộp.

**1553** — JP （れるっ！ れろっ――じゅうううっ――はむっ！」; TW 要被……啾……啾……啊嗚！」; old_vn (audit) （Liếm! Liếm——chụt——ngoạm!）; **fix = （Rộp! Liếm——chụt——ngoạm!）**. Đổi: liếm → rộp.

#### ふかみh2_homesweethome.txt.toml — 1 dòng

**1002** — JP 「えむっ――んっ――れるっ――れろっ――\nれろおっっ――ふっ――んっ――すっ――すひっ」; TW 「唔，嗯，啾，啾，啾，唔，嗯，呼，呼」; old_vn (CSV3) 「E mu——ưm——liếm——liếm——\nLiếm m m——phù——ưm——sụt——sụt hi」; **fix = 「E mu——ưm——rộp——liếm——\nLiếm m m——phù——ưm——sụt——sụt hi」**. Đổi: liếm → rộp.

#### れいなh2_おもらし防止大作戦.txt.toml — 3 dòng

**1081** — JP 「ふぁっ――あ――ちゅっ！――ちゅうう――ちゅっ――\nれるっ――れりゅ――ちゅっ――ちゅうう――ちゅっ！」; TW 「啾、啾、啾……噗啾！啾、啾嚕……啾、啾嚕！」; old_vn (moan) 「Fa——a——chụt!——chụt——chụt——\nChụt——chụt——chụt——chụt——chụt!」; **fix = 「Fa——a——chụt!——chụt——chụt——\nRộp——chụt——chụt——chụt——chụt!」**. Đổi: chụt → rộp.

**1093** — JP 「ん……んむっ――れろっ――れるううっ」; TW 「嗯……啊嗯……啾嚕」; old_vn (CSV3) 「Ưm……a ưm——chụt——chụt」; **fix = 「Ưm……a ưm——chụt——rộộộp」**. Đổi: chụt → rộộộp.

**1756** — JP （れろっ――れるっ――つんっ――ちゅぷうっ）; TW （啾嚕、啾嚕、啾嚕）; old_vn (CSV3) （Chụt——chụt——chụt——chụt）; **fix = （Chụt——rộp——chụt——chụt）**. Đổi: chụt → rộp.

#### れいなh3_おもらし自由化大作戦.txt.toml — 4 dòng

**1089** — JP 「れるっ――ぺろっ――ちゅっ――ちゅううっ――\nんっ……あむ～～～～んっ――」; TW 「啾嚕……啾嚕……嗯……啊嗯……」; old_vn (CSV3) 「Chụt——liếm——chụt——chụt——\nƯm……ammmmm——」; **fix = 「Rộp——liếm——chụt——chụt——\nƯm……ammmmm——」**. Đổi: chụt → rộp.

**1090** — JP 「んっ……ンッ――んむっ――んうっ――\nれるっ――れろっ――ちゅぷっ――ちゅぼっ」; TW 「啾嚕、啾啾……啾嚕嚕嚕啾、啾嚕、啾嚕嚕……啾嚕嚕」; old_vn (audit) 「Ưm……Ưm——ưm——ưm——\nChụt——chụt——chụt——chụt」; **fix = 「Ưm……Ưm——ưm——ưm——\nRộp——chụt——chụt——chụt」**. Đổi: chụt → rộp.

**1091** — JP 「んむっ――んふっ――れるっ――るっ――\nちゅっ――ちゅむ――ちゅるっ――ちゅううううっ」; TW 「啾嚕嚕……啾嚕……咕啾，啾嚕、啾啾……啾嚕嚕嚕」; old_vn (CSV3) 「Ưm——nfu——chụt——chụt——\nChụt——chụt——chụt——chụtttttt」; **fix = 「Ưm——nfu——rộp——rộp——\nChụt——chụt——chụt——chụtttttt」**. Đổi: chụt → rộp ; chụt → rộp.

**1101** — JP 「ふっ……んっ――チュっ……ちゅろっ――\nえむッ――れるっ――れろっ――んむっ」; TW 「嗯……嗯……啾、啾嚕……啾、啾、啾、啾」; old_vn (CSV3) 「Phù……ưm——chụt……chụt——\nE mu——chụt——chụt——ưm」; **fix = 「Phù……ưm——chụt……chụt——\nE mu——rộp——chụt——ưm」**. Đổi: chụt → rộp.

#### れいなh4_ふたりっきりのハロウィン.txt.toml — 1 dòng

**3267** — JP （ちゅむっ――れるっ――れろっ――ちゅむっ）; TW （啾嚕、啾嚕）; old_vn (CSV3) （Chụt——liếm——liếm——chụt）; **fix = （Chụt——rộp——liếm——chụt）**. Đổi: liếm → rộp.

#### ハチロクh1_契り.txt.toml — 3 dòng

**2132** — JP （れるっ――れろっ――じゅちゅっ――じゅるっ）; TW （咻嚕——咻嚕——啾——啾嚕）; old_vn (audit) （Sượt——sượt——Juchu——Juru）; **fix = （Rộp——sượt——Juchu——Juru）**. Đổi: sượt → rộp.

**2133** — JP （れるっ）; TW （咻嚕）; old_vn (CSV3) （Sượt）; **fix = （Rộp）**. Đổi: sượt → rộp.

**2149** — JP （ツ――れるっ――れろっ――じゅっ――じゅるっ――）; TW （嗅——呸嚕——呸囉——啾——啾嚕——）; old_vn (audit) （Liếm――liếm láp――liếm láp――chụt――Juru――）; **fix = （Liếm――rộp――liếm láp――chụt――Juru――）**. Đổi: bỏ [liếm, láp] → thêm [rộp].

#### ハチロクh2_お勉強の成果.txt.toml — 1 dòng

**1206** — JP 「れるっ――るっ――れろっ――じゅるるっ――\nんっ――んちゅっ――ちゅっ――ちゅううううっ」; TW 「（舔）——（舔）——（舔）——啾——嗯——嗯啾——啾——啾」; old_vn (moan) 「Liếm——liếm——liếm——chu mút——\nưm——ưm chụt——chụt——chuuuuu」; **fix = 「Rộp——rộp——liếm——chu mút——\nưm——ưm chụt——chụt——chuuuuu」**. Đổi: liếm → rộp ; liếm → rộp.

#### ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml — 1 dòng

**987** — JP 「ちゅっ――むっ――れるっ――ちゅうっ――れろっ、\nちゅむっ――にゅりゅっ――ちゅううっ」; TW 「啾——姆——咻嚕——啾嗚——嗯，啾姆——嗚嗚——啾嗚」; old_vn (moan) 「Chụt——ưm——liếm——chụụt——liếm láp,\nchu mút——trượt——chụụụt」; **fix = 「Chụt——ưm——rộp——chụụt——liếm láp,\nchu mút——trượt——chụụụt」**. Đổi: liếm → rộp.

#### ハチロクh5_おだいどこしごと.txt.toml — 1 dòng

**1743** — JP （れろっ――れるっ――しゃぶっ――こくんっ）; TW （舔來舔去）; old_vn (CSV3) （Liếm——mút——mút——ực）; **fix = （Liếm——rộp——mút——ực）**. Đổi: mút → rộp.

#### ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml — 6 dòng

**834** — JP 「ふうっ！ んっ――んっ！ んっ！ んっ！ ふうっ！\nれるっ――れろっ――れちゅっ――じゅるっ――ごくっ」; TW 「呼！嗯——！嗯！嗯！呼！咻嚕——嗯——嗯啾——啾嚕——嗯」; old_vn (CSV3) 「Phù! Ưm——ưm! Ưm! Ưm! Phù!\nMút——liếm——chụt——rột——ực」; **fix = 「Phù! Ưm——ưm! Ưm! Ưm! Phù!\nRộp——liếm——chụt——rột——ực」**. Đổi: mút → rộp.

**884** — JP 「ん――ふっ――ふうっ――ふ――っ――れろっ――\nれるっ――ちゅくっ――ふぁ」; TW 「嗯——呼——呼——呼——嗯——咻嚕——啾嗯——嗚啊」; old_vn (moan) 「Ưm——phù——phù——phù——ư——liếm——\nmút——chụt——Fa.」; **fix = 「Ưm——phù——phù——phù——ư——liếm——\nrộp——chụt——Fa.」**. Đổi: mút → rộp.

**887** — JP 「んっ――ふっ――れるっ――るっ――んっ――\nちゅっ――んくっ――ふっ――ふううっ！」; TW 「嗯——呼——咻嚕——嚕——啾——嗯——呼——呼！」; old_vn (moan) 「Ưm——phù——mút——mút——ưm——\nchụt——ưm ku——phù——phù ư ư!」; **fix = 「Ưm——phù——rộp——rộp——ưm——\nchụt——ưm ku——phù——phù ư ư!」**. Đổi: mút → rộp ; mút → rộp.

**894** — JP 「んっ――あっ――ちゅっ――んっ――チュムッ――\nちゅっ――れるっ――れろっ――ふ……ん……ちゅっ」; TW 「嗯——啊——咕啾——啾嗯——啾——咻嚕——嗯——呼……啾」; old_vn (CSV3) 「Ưm——a——chụt——ưm——chụm——\nchụt——mút——liếm——phù……ưm……chụt」; **fix = 「Ưm——a——chụt——ưm——chụm——\nchụt——rộp——liếm——phù……ưm……chụt」**. Đổi: mút → rộp.

**899** — JP 「んっ――ぷっ――んむっ――こくっ――ずじゅっ！\nごくっ！ れるっ――じゅっ――こくっ――ごくんっ！」; TW 「嗯——噗——咕——咕——呲啾！嗯！咻嚕——啾——咕嚕——嗯！」; old_vn (CSV3) 「Ưm——phù——ưm——ực——chụt!\nỰc! Mút——chụt——ực——ực!」; **fix = 「Ưm——phù——ưm——ực——chụt!\nỰc! Rộp——chụt——ực——ực!」**. Đổi: mút → rộp.

**934** — JP 「んんんん～～～っ！！ んっ、ふっ――ん！ ふうっ、\nん、れるっ――れろっ――じゅうう――ずじゅじゅ～！」; TW 「嗯嗯嗯嗯～～～！！嗯，呼——！呼，嗯，咻嚕——嗯——吱吱嗯——呲啾呲啾～！」; old_vn (moan) 「Ưm ưm ưm ưm~~~!! Ưm, phù——ưm! Phù,\nưm, mút——liếm——Juuu——rột rột~!」; **fix = 「Ưm ưm ưm ưm~~~!! Ưm, phù——ưm! Phù,\nưm, rộp——liếm——Juuu——rột rột~!」**. Đổi: mút → rộp.

#### ハチロクh7_レトロモダンメイクラヴ.txt.toml — 5 dòng

**791** — JP 「あ……ん……ちゅっ――ちゅむっ――ンッ――\nふ――っぁ……れろっ――れるっ――ちゅる――ちゅ」; TW 「啊……啾——啾姆——嗯——呼——啊……嗯——咻嚕——啾嚕——啾」; old_vn (unification đã gộp s3-fa-fu) 「A……ưm……chụt——chụm——ưm——\nFu——a……liếm——mút——chụt——chụt」; **fix = 「A……ưm……chụt——chụm——ưm——\nFu——a……liếm——rộp——chụt——chụt」**. Đổi: mút → rộp. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

**793** — JP 「あ……むっ――んっ――ん……チュッ……れるっ――\nンッ――ちゅっ――ちゅうっ――れるっ――れろっ」; TW 「啊……姆——嗯——……啾……咻嚕——n——啾——啾嗚——咻嚕——嗯」; old_vn (CSV3) 「A……ưm——ưm——ưm……chụt……mút——\nưm——chụt——chùn chụt——mút——liếm」; **fix = 「A……ưm——ưm——ưm……chụt……rộp——\nưm——chụt——chùn chụt——rộp——liếm」**. Đổi: mút → rộp ; mút → rộp.

**810** — JP 「チュッ――んっ……チュルッ――れるっ――るっ――\nんっ！？ こくっ――れろっ――れるっ――ちゅるっ」; TW 「啾——……啾嚕——咻嚕——嚕——嗯！？唔唔——嗯——咻嚕——啾嚕」; old_vn (CSV3) 「Chụt——ưm……chụt——mút——mút——\nưm!? Ực——liếm——mút——chụt」; **fix = 「Chụt——ưm……chụt——rộp——rộp——\nưm!? Ực——liếm——rộp——chụt」**. Đổi: mút → rộp ; mút → rộp ; mút → rộp.

**1878** — JP （れろっ――れるっ――れろおおおお――はぷっ！）; TW （嗯——咻嚕——咻嚕——哈噗！）; old_vn (unification đã gộp s3-moan-dialogue) （Liếm——liếm——Rerooooo——ngoạm!）; **fix = （Liếm——rộp——Rerooooo——ngoạm!）**. Đổi: liếm → rộp. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

**1944** — JP （ぺろっ――れろっ――れるっ――ぺりゅっ）; TW （舔來舔去）; old_vn (audit) （Liếm——liếm——liếm——liếm）; **fix = （Liếm——liếm——rộp——liếm）**. Đổi: liếm → rộp.

#### ハチロクh8_桜色のひめごと.txt.toml — 9 dòng

**805** — JP 「ちむっ――れろっ――れるっ――るっ――ちゅむ――\nちゅうっ――はむっ――れろっ――れるる――ずじゅっ」; TW 「啾姆——嗯——咻嚕——嚕——啾嗯——啾嗚——姆——嗯——咻嚕——呲啾」; old_vn (CSV3) 「Chụt——liếm——mút——mút——chụt——\nchụttttt——ngoạm——liếm——mút mát——nhóp nhép」; **fix = 「Chụt——liếm——rộp——rộp——chụt——\nchụttttt——ngoạm——liếm——rộp——nhóp nhép」**. Đổi: bỏ [mút, mút, mút, mát] → thêm [rộp, rộp, rộp].

**809** — JP 「ちゅっ！ ちゅむっ！ んっ――ちゅうっ――ふっ！\nれるっ――れろっ――ちゅううっ――ちゅむ、ちゅ！」; TW 「啾！啾姆！嗯——啾嗚——呼！咻嚕——嗯——啾嗚——啾嗯，啾！」; old_vn (audit) （Chụt! Chụt! Ưm——chụt——phù!\nLiếm——liếm——chụttttt——chụt, chụt!）; **fix = （Chụt! Chụt! Ưm——chụt——phù!\nRộp——liếm——chụttttt——chụt, chụt!）**. Đổi: liếm → rộp.

**825** — JP 「ん……ちゅっ――れろっ――れるっ――ちゅっ――\nちゅむ……ん……ぺろっ――れろっ――ちゅううっ！」; TW 「嗯……啾——嗯——咻嚕——啾——啾嗯……（舔）——嗯——啾嗚！」; old_vn (CSV3) 「Ưm……chụt——liếm——mút——chụt——\nchụt……ưm……liếm láp——mút mát——chụttttt!」; **fix = 「Ưm……chụt——liếm——rộp——chụt——\nchụt……ưm……liếm láp——mút mát——chụttttt!」**. Đổi: mút → rộp.

**827** — JP 「ん……ちゅっ――んんんっ――ふあっ――ふっ――\nちゅっ――チュムッ――れるっ、れろおっ、ん、ちゅっ」; TW 「嗯……啾——嗯嗯——呼啊——呼——啾——啾嗯——咻嚕，嗯，嗯，啾」; old_vn (moan) 「Ưm……chụt——ưm ưm ưm——Fua——phù——\nchụt——chụt——liếm, mút mát, ưm, chụt」; **fix = 「Ưm……chụt——ưm ưm ưm——Fua——phù——\nchụt——chụt——rộp, mút mát, ưm, chụt」**. Đổi: liếm → rộp.

**829** — JP 「ん……ちゅるっ――ちゅ――れるっ――れろ……ぺろっ\n――ふ……ん……ハムッ――はむっ――ちゅ、ちゅるる」; TW 「嗯……啾嚕——啾——咻嚕——嗯……——呼……啊姆——姆——啾，啾嚕嚕」; old_vn (audit) 「Ưm……chụt——chụt——liếm——mút……liếm láp\n——phù……ưm……Ngậm——ngoạm——chụt, chụt chụt」; **fix = 「Ưm……chụt——chụt——rộp——mút……liếm láp\n——phù……ưm……Ngậm——ngoạm——chụt, chụt chụt」**. Đổi: liếm → rộp.

**1547** — JP （れるううううううううううううっ！！！）; TW （咻嚕——！！！）; old_vn (CSV3) （Liếm lútttttttttttttttttt!!!）; **fix = （Rộộộộộộộộộộộộộộp!!!）**. Đổi: bỏ [liếm, lútttttttttttttttttt] → thêm [rộộộộộộộộộộộộộộp]. れる+13う → 14 ô (đếm bằng máy từ JP).

**1548** — JP （れるっ！ じゅぢゅっ！ れろんっ！ ずうりゅっ！）; TW （咻嚕！呲啾呲啾！嗯嗯！呲溜！）; old_vn (CSV3) （Liếm! Nhóp nhép! Mút mát! Chóp chép!）; **fix = （Rộp! Nhóp nhép! Mút mát! Chóp chép!）**. Đổi: liếm → rộp.

**1549** — JP （れるっ！ れろっ！ じゅぶっ！ じゅるるるうっ！）; TW （咻嚕！嗯！啾噗！啾嚕——！）; old_vn (CSV3) （Liếm! Mút! Nhóp nhép! Chóp chépppp!）; **fix = （Rộp! Mút! Nhóp nhép! Chóp chépppp!）**. Đổi: liếm → rộp.

**1575** — JP （ぴちゃ――ぺちゅっ――ちゅぶ――れるっ――）; TW （噗沙——呸啾——啾噗——咻嚕——）; old_vn (CSV3) （Chóp chép——nhóp nhép——chụt——liếm láp——）; **fix = （Chóp chép——nhóp nhép——chụt——rộp——）**. Đổi: bỏ [liếm, láp] → thêm [rộp].

#### ハチロクh9_コノフクハキルコト.txt.toml — 4 dòng

**2035** — JP 「ふっ……あっ――んっ――れるるっ――ちゅっ――\nれろっ――れりゅうっ――るっ――ん――むちゅっ」; TW 「呼……啊——咻嚕——啾——嗯——嗚啾嗚——嚕——姆啾」; old_vn (CSV3) 「Hu……a——ưm——liếm——chụt——\nliếm láp——mút mát——ưm——ưm——mu chu」; **fix = 「Hu……a——ưm——rộp——chụt——\nliếm láp——mút mát——rộp——ưm——mu chu」**. Đổi: ưm → rộp ; liếm → rộp.

**2043** — JP 「れるっ――るっ――るうううっ――じゅ、ずっ――\nずっ――れろ――れるううっ――ずずっ――ずうっ」; TW 「咻嚕——嚕——嚕嗚——呲啾，呲——呲——嗯——咻嚕嗚——慢慢——嗚」; old_vn (CSV3) 「Reru——ru——ruuu——ju, zu——\nzu——rero——reruuu——zuzu——zuu」; **fix = 「Rộp——rộp——rộộộộp——ju, zu——\nzu——rero——rộộộp——zuzu——zuu」**. Đổi: reru → rộp ; ru → rộp ; ruuu → rộộộộp ; reruuu → rộộộp. Chuỗi romaji âm miệng (TW 咻嚕…): đổi cả るっ→'rộp' và るうううっ→'rộộộộp'; chuỗi thành hỗn hợp romaji+VN — ghi chú, không đổi toàn chuỗi.

**2120** — JP 「ちゅっ――れるっ――れろっ――ちゅううう――\nちゅるっ――（こくっ）――んっ――ちゅっ、ちゅむ」; TW 「啾——咻嚕——嗯——啾——啾嚕——（咕嚕）——啾，啾嗯」; old_vn (moan) 「Chụt——liếm——mút——chuuuu——\nchóp chép——（Ực）——ưm——chụt, chụt」; **fix = 「Chụt——rộp——mút——chuuuu——\nchóp chép——（Ực）——ưm——chụt, chụt」**. Đổi: liếm → rộp.

**2156** — JP 「ん……ちゅっ――ちゅむっ――ちゅっ――んっ――\nれるっ――れろっ――じゅるる――れるっ――ちゅぷ」; TW 「嗯……啾——啾姆——啾——咻嚕——嗯——啾嚕嚕——咻嚕——啾噗」; old_vn (moan) 「Ưm……chụt——chumu——chụt——ưm——\nliếm——liếm láp——chóp chép——liếm——chu pu」; **fix = 「Ưm……chụt——chumu——chụt——ưm——\nrộp——liếm láp——chóp chép——rộp——chu pu」**. Đổi: liếm → rộp ; liếm → rộp.

#### ポーレットh1_ファーストセックス.txt.toml — 4 dòng

**1010** — JP 「じゅッ――じゅるるっ――んっ――\nれろっ――れるっ――じゅるるうっ――こくんっ」; TW 「啾――啾嚕嚕――嗯――啾嚕——啾嚕——啾嚕嚕——嗯呼」; old_vn (CSV3) 「Chụt——chùn chụt——ưm——\nliếm——liếm——chùn chụt——ực.」; **fix = 「Chụt——chùn chụt——ưm——\nliếm——rộp——chùn chụt——ực.」**. Đổi: liếm → rộp.

**1012** — JP 「はぷっ――れるっ――れろっ――じゅっ――\nじゅるっ――じゅぷっ――じゅうっ――こくっ」; TW 「啾噗——啾嚕——啾嚕——啾啾——啾嚕——啾嚕——啾噗——噗嚕」; old_vn (CSV3) 「Ngoạm——liếm——liếm——chụt——\nchụt——chùn chụt——chuút——ực.」; **fix = 「Ngoạm——rộp——liếm——chụt——\nchụt——chùn chụt——chuút——ực.」**. Đổi: liếm → rộp.

**1016** — JP 「チュッ――ちるっ――れろっ――れるうううっ――」; TW 「啾嚕——啾嚕——啾嚕——啾嚕嚕——」; old_vn (CSV3) 「Chụt——chùn chụt——liếm——liếmmmmm——」; **fix = 「Chụt——chùn chụt——liếm——rộộộộp——」**. Đổi: liếmmmmm → rộộộộp.

**1019** — JP 「んっ――ふっ――んっ――れろっ――れるっ――\nんっ――ちゅっ――ちゅるるっ――ちゅぞおおおおっ」; TW 「嗯——呼——嗯——啾嚕——啾嚕——嗯——啾——啾嚕嚕——啾嚕嚕」; old_vn (moan) 「Ưm——phù——ưm——liếm——liếm——\nưm——chụt——chùn chụt——chuzooooo.」; **fix = 「Ưm——phù——ưm——liếm——rộp——\nưm——chụt——chùn chụt——chuzooooo.」**. Đổi: liếm → rộp.

#### ポーレットh2_制服変更？.txt.toml — 1 dòng

**1639** — JP （じゅずうううっ――ごくっ――れろっ――れるっ――）; TW （啾嚕——啾嚕——啾噗——啾噗——）; old_vn (CSV3) （Chuúúúút——ực——liếm——liếm——）; **fix = （Chuúúúút——ực——liếm——rộp——）**. Đổi: liếm → rộp.

#### ポーレットh3_誘惑アイスコーヒー.txt.toml — 2 dòng

**933** — JP 「あむっ――ん――ちゅぶっ――ちゅるっ――\nぺろっ――れるっ――れろろっ――ちゅううっ」; TW 「唔——嗯——啾嚕——啾嚕——啾嚕——啾嚕——啾嚕——啾嚕」; old_vn (moan) 「Ngoạm——ưm——chubu——chụt——\nliếm——liếm——liếm——chụụụt」; **fix = 「Ngoạm——ưm——chubu——chụt——\nliếm——rộp——liếm——chụụụt」**. Đổi: liếm → rộp.

**942** — JP 「はむっ――んっ――ん～～っ――\nれるっ、れろっ――ちゅむつ――ちゅうっ」; TW 「啊——嗯——嗯～～啾嚕、啾嚕——嗯——啾嚕」; old_vn (moan) 「Ngoạm——ưm——ưm～～\nliếm, liếm——chumu——chụụt」; **fix = 「Ngoạm——ưm——ưm～～\nrộp, liếm——chumu——chụụt」**. Đổi: liếm → rộp.

#### ポーレットh4_クリーム＆クリーム.txt.toml — 1 dòng

**932** — JP 「～っ――んっ！ んっ――ちゅっ――ちゅむうっ――\nんっ――ふうっ――れるっ――れろっ――れろおおっ」; TW 「啊——嗯！嗯――啾嚕――啾噗――嗯——呼——啾嚕——啾嚕——啾噗」; old_vn (moan) 「～——ưm! Ưm——chụt——Chumuu——\nƯm——Phùu——liếm——liếm——liếmmmm」; **fix = 「～——ưm! Ưm——chụt——Chumuu——\nƯm——Phùu——liếm——rộp——liếmmmm」**. Đổi: liếm → rộp.

#### ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml — 4 dòng

**938** — JP 「んーむっ――ちゅ――はむ――ちゅるっ――ちろ、\nちるる――れろっ――れるうっ――」; TW 「嗯——唔——啾嚕——啾嚕——啾噗——啾噗——啾嚕——啾嚕——啾噗——」; old_vn (moan) 「Ưm ưm——chụt——ngoạm——chụt——liếm, liếm——liếm——liếmmmm——」; **fix = 「Ưm ưm——chụt——ngoạm——chụt——liếm, liếm——rộộp——liếmmmm——」**. Đổi: liếm → rộộp.

**942** — JP 「んっ……ちゅっ――ちゅむっ――ちゅうう――ちゅっ\n――ぷ、あっ――ん――れろっ――れるっ――れろおっ」; TW 「嗯……啾——啾嚕——啾啾——啾嚕——呼、啊——嗯——啾嚕——啾嚕——啾噗」; old_vn (moan) 「Ưm……chụt——chumu——chụtttt——chụt ——Phù, a——ưm——liếm——liếm——liếmmmm」; **fix = 「Ưm……chụt——chumu——chụtttt——chụt ——Phù, a——ưm——liếm——rộp——liếmmmm」**. Đổi: liếm → rộp.

**1696** — JP （ぺろっ！ れるっ！ れろおっ！ ぬろおおおっ――）; TW （啾嚕——啾嚕——咕啾——咕啾）; old_vn (CSV3) （Liếm! Liếm! Liếmmmm! Trơn tuộtttttt——）; **fix = （Liếm! Rộp! Liếmmmm! Trơn tuộtttttt——）**. Đổi: liếm → rộp.

**1726** — JP （ぴちゃっ――ぬちゃっ――にちゃっ――れるっ――）; TW （舔來舔去）; old_vn (CSV3) （Lách tách——nhóp nhép——nhóp nhép——liếm——）; **fix = （Lách tách——nhóp nhép——nhóp nhép——rộp——）**. Đổi: liếm → rộp.

#### ポーレットh6_あなたとふたりの学園エッチ.txt.toml — 2 dòng

**828** — JP 「はみゅっ――んっ――ちゅっ――ちゅるるっ――\nれろっ――れるっ――じゅるっ――はぷっ！」; TW 「啾噗——嗯——啾嚕——啾嚕——啾嚕——啾嚕——啾噗——啾噗！」; old_vn (CSV3) 「Ngoạm——ưm——chụt——chụtttt——\nliếm——liếm——sụt——ngoạm!」; **fix = 「Ngoạm——ưm——chụt——chụtttt——\nliếm——rộp——sụt——ngoạm!」**. Đổi: liếm → rộp.

**856** — JP 「ん……ちゅっ……ちゅう……ちゅむっ……ふっ――\nんっ――ちゅるっ――ちゅっ――れろっ――れるっ――」; TW 「嗯……啾……啾……啾嚕……呼——嗯——啾嚕——啾噗——啾嚕——啾嚕——」; old_vn (audit) 「Ưm……chụt……chụt……chụt……phù—— Ưm——chụt——chụt——liếm——liếm——」; **fix = 「Ưm……chụt……chụt……chụt……phù—— Ưm——chụt——chụt——liếm——rộp——」**. Đổi: liếm → rộp.

#### ポーレットh7_残業エッチもyシャツで.txt.toml — 5 dòng

**872** — JP 「あんむっ――んっ――ちゅっ――ちゅううっ――\nちゅずっ――れろっ――れるうっ――ちゅるっ！」; TW 「啊——嗯——啾——啾嚕——啾嚕——啾嚕——啾噗——啾噗！」; old_vn (moan) 「Anmu——ưm——chụt——chụt—— chụt——rộp——rộp——chụt!」; **fix = 「Anmu——ưm——chụt——chụt—— chụt——rộp——rộộp——chụt!」**. Đổi: rộp → rộộp.

**911** — JP 「ん……ちゅっ――ぺろっ、れろっ――ん……\nれる……れろっ――ぺろおっ――れるんっ！」; TW 「嗯……啾——啾嚕、啾嚕——嗯……啾嚕……啾嚕——啾噗——啾噗！」; old_vn (CSV3) 「Ưm……chụt——liếm, rộp——ưm……\nliếm……rộp——liếm——rộp!」; **fix = 「Ưm……chụt——liếm, rộp——ưm……\nrộp……rộp——liếm——rộp!」**. Đổi: liếm → rộp.

**1675** — JP （ずりゅっ！ もみゅっ！ れる！ ずちゅん！）; TW （揉來揉去、舔來舔去）; old_vn (CSV3) （Trượt! Nắn! Liếm! Phập!）; **fix = （Trượt! Nắn! Rộp! Phập!）**. Đổi: liếm → rộp.

**1690** — JP （じゅる！ れろっ！ みゅりゅ！ んっ――るうっ！）; TW （舔來舔去）; old_vn (CSV3) （Rột! Liếm! Rột! Ưm——rột!）; **fix = （Rột! Liếm! Rột! Ưm——rộộp!）**. Đổi: rột → rộộp. TW （舔來舔去） = liếm qua lại → LICKING, るうっ→'rộộp'.

**1692** — JP （れるううううっ）; TW （舔舐）; old_vn (unification đã gộp s3-sfx-counting) （Liếmmmm）; **fix = （Rộộộộộp）**. Đổi: liếmmmm → rộộộộộp. — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

#### 凪h1_ふたりっきりのデート.txt.toml — 1 dòng

**1118** — JP 「ん……ちゅっ――ちゅうっ――ちゅ――ちゅむっ――\nちゅうっ――れるっ――ちゅううっ――ちゅ――ぷあっ」; TW 「啾……啾……啾……啾……啾……啾……啾……啾……呼」; old_vn (moan) 「Ưm……Chụt——Chụt——Chụt——Chụt——\nChụt——Chụt——Chụt——Chụt——Pua」; **fix = 「Ưm……Chụt——Chụt——Chụt——Chụt——\nChụt——Rộp——Chụt——Chụt——Pua」**. Đổi: chụt → rộp.

#### 凪h2_おとなの水着.txt.toml — 7 dòng

**2425** — JP 「ふっ――んっ――ちゅ――ちゅうっ――れるっ――\nちゅむっ――れろっ――れるっ――るっ――ちゅむ」; TW 「呼……嗯……啾，啾，啾，啾，啾，啾，啾，啾」; old_vn (CSV3) 「Phù——Ưm——Chụt——Chụt——Ngoáy——\nChụt——Ngoáy——Ngoáy——Ngoáy——Chụt」; **fix = 「Phù——Ưm——Chụt——Chụt——Rộp——\nChụt——Ngoáy——Rộp——Rộp——Chụt」**. Đổi: ngoáy → rộp ; ngoáy → rộp ; ngoáy → rộp.

**2496** — JP 「ひょはひょほー――んっ――れる、れろっ、ちゅむ、\nちゅっ――ぺろおっ、ちゅむ――ずっ――ちゅるるっ」; TW 「唔唔唔……嗯……啾，啾，啾，啾，啾，啾，滋……啾」; old_vn (CSV3) 「Hyo ha hyo ho——Ưm——Ngoáy, ngoáy, chụt,\nchụt——liếmm, chụt——sụt——chụt chụt」; **fix = 「Hyo ha hyo ho——Ưm——rộp, ngoáy, chụt,\nchụt——liếmm, chụt——sụt——chụt chụt」**. Đổi: ngoáy → rộp.

**2558** — JP 「ん……ふ、ふ――れるっ――ちゅっ、ずううううっ\nずじゅ――ごくっ――んっ……ちゅむ――れる、れろ」; TW 「嗯……呼，呼……啾，啾，滋，滋，咕咚，嗯……啾，啾，啾」; old_vn (CSV3) 「Ưm……Phù, phù——Ngoáy——Chụt, sụtttttt\nSụt sịt——Ực——Ưm……Chụt——Ngoáy, ngoáy」; **fix = 「Ưm……Phù, phù——Rộp——Chụt, sụtttttt\nSụt sịt——Ực——Ưm……Chụt——Rộp, ngoáy」**. Đổi: ngoáy → rộp ; ngoáy → rộp.

**2559** — JP 「ん……ちゅっ――ぺろっ――れるっ――ちゅ、\nちゅずっ――ずっ、するっ――ちゅる、れろ」; TW 「嗯……啾……啾，啾，啾，啾……滋，滋……啾，啾」; old_vn (CSV3) 「Ưm……Chụt——Liếm——Ngoáy——Chụt,\nChụt sụt——Sụt, tuột——Chụt, ngoáy」; **fix = 「Ưm……Chụt——Liếm——Rộp——Chụt,\nChụt sụt——Sụt, tuột——Chụt, ngoáy」**. Đổi: ngoáy → rộp.

**2561** — JP 「ん……ちゅ――ちゅうっ――ちゅむっ――ちゅるる、\nちゅ――ごくっ――ちゅ、むっ――れろっ、れるうう」; TW 「嗯……啾，啾，啾，啾，啾，咕咚，啾，啾，啾」; old_vn (CSV3) 「Ưm……Chụt——Chụttt——Chụt——Chụt chụt,\nChụt——Ực——Chụt, chụt——Ngoáy, ngoáyyyy」; **fix = 「Ưm……Chụt——Chụttt——Chụt——Chụt chụt,\nChụt——Ực——Chụt, chụt——Ngoáy, Rộộộp」**. Đổi: ngoáyyyy → rộộộp.

**2562** — JP 「ん……ちゅっ――ちゅむっ――ちゅうっ、ちゅっ、\nぺろっ、ぺろっ――れるっ――れろおっ――ちゅっ」; TW 「嗯……啾，啾，啾，啾，啾，啾，啾，啾，啾」; old_vn (CSV3) 「Ưm……Chụt——Chụt——Chụttt, chụt,\nLiếm, liếm——Ngoáy——Ngoáyyy——Chụt」; **fix = 「Ưm……Chụt——Chụt——Chụttt, chụt,\nLiếm, liếm——Rộp——Ngoáyyy——Chụt」**. Đổi: ngoáy → rộp.

**2563** — JP 「ん……ちゅううっ――ちゅっ――んっ――ぷっ、\nふぁっ――れろっ――れるっ――ぺろぺろ、ちゅっ」; TW 「嗯……啾，啾，嗯……噗，哇，啾，啾，啾，啾」; old_vn (moan) 「Ưm……Chụttt——Chụt——Ưm——Phụt,\nFa——Ngoáy——Ngoáy——Liếm liếm, chụt」; **fix = 「Ưm……Chụttt——Chụt——Ưm——Phụt,\nFa——Ngoáy——Rộp——Liếm liếm, chụt」**. Đổi: ngoáy → rộp.

#### 凪ふかみh1_修学旅行の夜.txt.toml — 6 dòng

**1237** — JP 「ふぁっ――あっ――ちゅっ――んむっ――\nちゅるっ――れろっ――れるっ――れろおっ――」; TW 「呼……啊……啾……嗯唔……啾……啾……啾……啾……」; old_vn (moan) 「Fa——a——chụt——ưm——\nrột——liếm——liếm——liếm——」; **fix = 「Fa——a——chụt——ưm——\nrột——liếm——rộp——liếm——」**. Đổi: liếm → rộp.

**1289** — JP 「れるっ――れろっ――ちゅっ――ちゅるっ――\nちゅろっ――ろっ――れるう――れろっ――ふっ」; TW 「啾……啾……啾……啾……啾……啾……啾……啾……呼」; old_vn (CSV3) 「Liếm——liếm——chụt——rột——\nchụt——liếm——liếm——liếm——phù」; **fix = 「Rộp——liếm——chụt——rột——\nchụt——liếm——rộộp——liếm——phù」**. Đổi: liếm → rộp ; liếm → rộộp.

**1290** — JP 「れるっ――ちゅむっ――ぺろ――ぺろおっ――ちゅっ、\nちゅむっ、ちゅうっ――ぺろっ――ぺろっ――れろん！」; TW 「啾……啾……啾……啾……啾，啾，啾……啾……啾……啾！」; old_vn (CSV3) 「Liếm——chụt——liếm——liếm——chụt,\nchụt, chu——liếm——liếm——liếm!」; **fix = 「Rộp——chụt——liếm——liếm——chụt,\nchụt, chu——liếm——liếm——liếm!」**. Đổi: liếm → rộp.

**1291** — JP 「れるっ――ちゅっ――ちゅむっ――んっ――ひっはひ\n――ひほひひょふはっへ――ふっ――ふらはい――へ？」; TW 「啾……啾……啾……嗯……沒關係……舒服起來就行了」; old_vn (CSV3) 「Liếm——chụt——chụt——ưm——c-cứ\n——thấy sướng là được——phù——ạ——nhỉ?」; **fix = 「Rộp——chụt——chụt——ưm——c-cứ\n——thấy sướng là được——phù——ạ——nhỉ?」**. Đổi: liếm → rộp.

**1294** — JP 「れるっ――ちゅっ――んっ！？ わ、ふかみちゃん！\nにーさん、先っぽ、ぷくってしてきよったと！」; TW 「啾……啾……嗯！？哇，小深！大哥哥的尖尖好像有什麼冒出來了！」; old_vn (CSV3) 「Liếm——chụt——ưm!? Oa, Fukami!\nPhần đầu của anh hai, đang phồng lên kìa!」; **fix = 「Rộp——chụt——ưm!? Oa, Fukami!\nPhần đầu của anh hai, đang phồng lên kìa!」**. Đổi: liếm → rộp.

**1301** — JP 「ん……ちゅっ――れるっ――れろっ――しゃぶっ――\nちゅぶっ――ちゅっ――れろおっ――じゅるっ――ぺろ」; TW 「嗯啾……啾……啾……嗯……嗯……啾……啾……啾……舔」; old_vn (CSV3) 「Ưm... chụt——liếm——liếm——mút——\nchụt——chụt——liếm——rột——liếm」; **fix = 「Ưm... chụt——rộp——liếm——mút——\nchụt——chụt——liếm——rột——liếm」**. Đổi: liếm → rộp.

#### 凪ふかみh2_みずあそび.txt.toml — 5 dòng

**1030** — JP 「……れ……るっ――ふっ――んっ――るろっ――\nろっ――れるうっ――れろっ――れろおおおお」; TW 「……舔……呼……嗯……舔……舔……啾……啾……啾」; old_vn (unification đã gộp s3-moan-dialogue) 「...Liếm... liếm——phù——ưm——liếm——\nliếm——liếm——liếm——Rerooooo」; **fix = 「...Liếm... rộp——phù——ưm——liếm——\nliếm——rộộp——liếm——Rerooooo」**. Đổi: liếm → rộp ; liếm → rộộp. 9 token JP = 9 từ VN 1:1 — đổi るっ (từ 2) và れるうっ (từ 7); giữ れ/るろっ/ろっ/れろっ/れろおおおお (U12a). — **GHÉP** với batch đã gộp (old_vn = fix đã gộp)

**1346** — JP 「えむっ――れるっ――るっ――れりゅうっ」; TW 「啊嗚……啾……啾……啾」; old_vn (audit) 「Emu——liếm——liếm——liếm」; **fix = 「Emu——rộp——rộp——liếm」**. Đổi: liếm → rộp ; liếm → rộp.

**1357** — JP 「れるっ――れろおっ――しゅぶっ――しゃぶぅっ」; TW 「啾……啾……啾……啾」; old_vn (CSV3) 「Liếm——liếm——mút——mút」; **fix = 「Rộp——liếm——mút——mút」**. Đổi: liếm → rộp.

**1374** — JP 「えうっ――んっ――ちゅ……ちゅずっ――じゅるっ――\nんう……れろ――れるっ――ちゅうっ――ずじゅっ」; TW 「嗯……嗯……啾……啾……啾……嗯……啾……啾……啾……啾」; old_vn (audit) 「Eu——ưm——chụt... chụt——rột——\nưm... liếm——liếm——chu——chụt」; **fix = 「Eu——ưm——chụt... chụt——rột——\nưm... liếm——rộp——chu——chụt」**. Đổi: liếm → rộp.

**1428** — JP 「凪ちゃんの指――んっ――おいひい――ひょぉ……ん、\nちゅっ――ちゅう――れろっ――れるうっ」; TW 「小凪的手指……嗯……真好吃……嗯，啾……啾……啾……啾」; old_vn (audit) 「Ngón tay của bé Nagi——ưm——ngon quá——Hyo... ưm,\nchụt——chu——liếm——liếm」; **fix = 「Ngón tay của bé Nagi——ưm——ngon quá——Hyo... ưm,\nchụt——chu——liếm——rộộộp」**. Đổi: liếm → rộộộp.

#### 日々姫h1_マッサージの続き.txt.toml — 6 dòng

**1055** — JP 「ちゅっ――れるっ――ちゅむっ――ちゅるっ――」; TW 「啾――啾嚕――啾噗――啾噗――」; old_vn (CSV3) 「Chụt——Liếm——Chụt——Chụt——」; **fix = 「Chụt——Rộp——Chụt——Chụt——」**. Đổi: liếm → rộp.

**1056** — JP 「あむっ――っ――れるっ――れろっ――むちゅうっ」; TW 「啾――啾嚕――啾嚕――啾噗」; old_vn (audit) 「Ngoạm——Ư——Liếm——Liếm——Mút.」; **fix = 「Ngoạm——Ư——Rộp——Liếm——Mút.」**. Đổi: liếm → rộp.

**1061** — JP 「んっ――むっ――じゅるっ――むうっ――ンッ――\nれるっ――じゅるるっ――むうっ――はぷっ」; TW 「嗯――唔――啾噗――唔――嗯――啾嚕――啾噗――嗯――啾噗」; old_vn (CSV3) 「Ưm——Ưm——Chụt——Ưm——Ưm——Liếm——Chụt chụt——Ưm——Ngoạm.」; **fix = 「Ưm——Ưm——Chụt——Ưm——Ưm——Rộp——Chụt chụt——Ưm——Ngoạm.」**. Đổi: liếm → rộp.

**1065** — JP 「んふっ――ちゅっ――ぺろっ――ちゅるっ――ぺろおっ\n――れろれろ――れるーーーっっ――――――ぱくっ！」; TW 「嗯――啾――啾嚕――哧溜――吸溜――啾嚕――啾嚕――（咬住）！」; old_vn (moan) 「Nfu——Chụt——Liếm——Chụt——Liếm——Liếm liếm——Liếmmm————Ngoạm!」; **fix = 「Nfu——Chụt——Liếm——Chụt——Liếm——Liếm liếm——rộộộộp————Ngoạm!」**. Đổi: liếmmm → rộộộộp.

**1873** — JP （ずちゅっ！ れるうううううっつっ！）; TW （啾噗！咕啾！）; old_vn (CSV3) （Chụt! Liếmmmmmm!）; **fix = （Chụt! Rộộộộộộp!）**. Đổi: liếmmmmmm → rộộộộộộp.

**1905** — JP （ちゅむっ――はむっ――れろっ――れるっ）; TW （親上――咬住――舔舐――舔舐）; old_vn (CSV3) （Chụt——Ngoạm——Liếm——Liếm）; **fix = （Chụt——Ngoạm——Liếm——Rộp）**. Đổi: liếm → rộp.

#### 日々姫h3_汚れてしまった制服で.txt.toml — 1 dòng

**1793** — JP （れるっ――れろっ――じゅぶっ――ぢゅうっ）; TW （來回舔舐）; old_vn (CSV3) （Liếm——Liếm——Chụt——Chụt）; **fix = （Rộp——Liếm——Chụt——Chụt）**. Đổi: liếm → rộp.

#### 日々姫h4_いもうとタオル.txt.toml — 1 dòng

**1024** — JP 「ちゅうっ――んっ――れるっ――じゅるっ――――\n（じゃりっ！） っ！！？」; TW 「啾――嗯――啾嚕――啾嚕――（嘎嘣！）嗯！！？」; old_vn (audit) 「Chụt――ưm――liếm――chùn chụt――――\n（Rắc!） Ư!!?」; **fix = 「Chụt――ưm――rộp――chùn chụt――――\n（Rắc!） Ư!!?」**. Đổi: liếm → rộp.

#### 日々姫h5_白濁絵の具の射精会.txt.toml — 5 dòng

**1204** — JP 「はむっ――ちゅっ――ちゅろっ――れるっ――るっ――\nれろろっ――はむっ――ぷっ――はむうッ――んっ」; TW 「唔――啾――啾嚕――啾嚕――嚕――啾嚕嚕――唔――噗――唔――嗯」; old_vn (CSV3) 「Ngoạm――chụt――chụt――liếm――liếm――\nLiếm liếm――ngoạm――phụt――ngoạm――ưm」; **fix = 「Ngoạm――chụt――chụt――rộp――rộp――\nLiếm liếm――ngoạm――phụt――ngoạm――ưm」**. Đổi: liếm → rộp ; liếm → rộp.

**1221** — JP 「ちゅっ――ちゅむっ――ちゅろっ――ちゅろっ――\nれるっ――れろっ――れるうっ！ にゅろんっ！！」; TW 「啾――啾噗――啾嚕――啾嚕――啾噗――啾噗――啾嚕！ 啾噗！！」; old_vn (CSV3) 「Chụt――chùn chụt――chụt――chụt――\nLiếm――liếm――liếm! Trơn tuột!!」; **fix = 「Chụt――chùn chụt――chụt――chụt――\nRộp――liếm――rộộp! Trơn tuột!!」**. Đổi: liếm → rộp ; liếm → rộộp.

**1226** — JP 「っろっ――れるうっ――れろっ――じゅぶっ！ じゅ！\nずりゅりゅりゅりゅ！ ん――れろっ――ぬろんっ！」; TW 「啾嚕――啾嚕――啾嚕――啾噗！啾！啾嚕啾嚕！嗯――啾嚕――啾噗！」; old_vn (CSV3) 「Rót――liếm――liếm――chụt! Chụt!\nZuryuryuryuryu! Ưm――liếm――trơn tuột!」; **fix = 「Rót――rộộp――liếm――chụt! Chụt!\nZuryuryuryuryu! Ưm――liếm――trơn tuột!」**. Đổi: liếm → rộộp.

**1238** — JP 「んっ――ちゅっ――むっ――れろ――れるううっ。\nれろっ――ぺろっ――ちゅくっ――ちゅむうっ！」; TW 「嗯――啾――唔――啾嚕――啾嚕嚕、啾嚕――咕啾――啾嚕――啾噗！」; old_vn (CSV3) 「Ưm――chụt――ưm――liếm――liếm.\nLiếm――liếm――chụt――chùn chụt!」; **fix = 「Ưm――chụt――ưm――liếm――rộộộp.\nLiếm――liếm――chụt――chùn chụt!」**. Đổi: liếm → rộộộp.

**1253** — JP 「ん……ぷっ――んっ！ ちゅうっ――ずぢゅ！ ごくっ\n――ふっ――あむっ――れろっ――れるっ――こしゅん」; TW 「嗯……噗――嗯！啾――啾嚕！咕嚕――呼――唔――啾嚕――啾嚕――咕啾」; old_vn (CSV3) 「Ưm……phụt――ưm! Chụt――zuju! Ực\n――phù――ngoạm――liếm――liếm――koshun」; **fix = 「Ưm……phụt――ưm! Chụt――zuju! Ực\n――phù――ngoạm――liếm――rộp――koshun」**. Đổi: liếm → rộp.

#### 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml — 1 dòng

**2172** — JP 「はむっ――ンッ――れるっ――れろっ――ねろっ\n――ねるうううっ――ちゅずずうっ――ず、ごくっ」; TW 「唔――嗯――啾嚕――啾嚕――啾嚕――啾嚕嚕――啾噗――噗滋」; old_vn (CSV3) 「Ngoạm――ưm――liếm――liếm――liếm\n――liếm――chụt――ực」; **fix = 「Ngoạm――ưm――rộp――liếm――liếm\n――liếm――chụt――ực」**. Đổi: liếm → rộp.

#### 真闇h1_長期熟成.txt.toml — 1 dòng

**1056** — JP 「ちゅっ――んっ……んちゅっ――れるっ――れろっ\n――ん……んふっ……ふっ」; TW 「啾――嗯……嗯啾――舔――舔――嗯……嗯唔……呼」; old_vn (audit) 「Chụt――ưm……ưm chụt――liếm――liếm\n――ưm……ưm fu……fu」; **fix = 「Chụt――ưm……ưm chụt――rộp――liếm\n――ưm……ưm fu……fu」**. Đổi: liếm → rộp.

#### 真闇h2_無濾過.txt.toml — 3 dòng

**1083** — JP 「ちゅっ――れるっ――ちゅるっ――ちゅううっっ」; TW 「啾――舔――啾――啾」; old_vn (audit) 「Chụt――rột――rột――chuuu.」; **fix = 「Chụt――rộp――rột――chuuu.」**. Đổi: rột → rộp.

**1103** — JP 「ん……れるっ――ちゅっ――れろっ」; TW 「嗯……舔――啾――舔」; old_vn (CSV3) 「Ưm……rột――chụt――rột.」; **fix = 「Ưm……rộp――chụt――rột.」**. Đổi: rột → rộp.

**1845** — JP （ちゅるっ――ちゅっ――れるっ――ちゅむうっ）; TW （啾――啾――舔――啾）; old_vn (CSV3) （Rột――chụt――rột――chumuu）; **fix = （Rột――chụt――rộp――chumuu）**. Đổi: rột → rộp.

#### 真闇h3_補習授業の廃校舎.txt.toml — 2 dòng

**2299** — JP 「じゅううっ！ じゅぼっ！ じゅるる～～にゅぼっ！\nじゅるううっ――れるううっ――じゅぼ！ がぼっ！」; TW 「啾！ 啾啵！ 啾嚕～～呶啵！啾唔唔――嚕唔唔――啾啵！ 咳！」; old_vn (CSV3) 「Juuu! Jubo! Jururu~~nyubo!\nJuruuu――reruuu――jubo! Gabo!」; **fix = 「Juuu! Jubo! Jururu~~nyubo!\nJuruuu――rộộộp――jubo! Gabo!」**. Đổi: reruuu → rộộộp.

**2363** — JP 「んっ！？ ふっ――あむっ――れろっ――ちゅるっ、\nちゅっ――れるっ――じゅむっ――ちゅ、ちゅううっ」; TW 「嗯！？ 呼――啊嗚――舔――啾、啾――舔――啾――啾、啾」; old_vn (moan) 「Ưm!? Phư――amu――rột――churu,\nchụt――rột――jumu――chu, chuuu.」; **fix = 「Ưm!? Phư――amu――rột――churu,\nchụt――rộp――jumu――chu, chuuu.」**. Đổi: rột → rộp.

#### 稀咲h1_性生活.txt.toml — 1 dòng

**1297** — JP 「ん……ちゅっ――ちゅむっ――あムッ――\nん……れろっ――れるっ――ちゅうっ――しゃぶっ」; TW 「嗯……啾――啾――啊嗚――嗯……舔――舔――啾――咻嚕」; old_vn (CSV3) 「Ưm…… chụt――chu mu――a mu――\nưm…… liếm――liếm――chụt――mút」; **fix = 「Ưm…… chụt――chu mu――a mu――\nưm…… liếm――rộp――chụt――mút」**. Đổi: liếm → rộp.

#### 稀咲h3_チャイナドレスでおもてなし.txt.toml — 3 dòng

**2269** — JP 「ん……ちゅっ――ふっ――ちゅむっ――ちゅっ、\nちゅるっ――れろっ――れるうっ――ちゅむっ」; TW 「嗯……啾――呼――啾唔――啾、啾――舔――舔――啾唔」; old_vn (moan) 「Ưm……chụt――phu――chụt――chụt,\nchụt――rero――Reroo――chụt」; **fix = 「Ưm……chụt――phu――chụt――chụt,\nchụt――rero――Rộộp――chụt」**. Đổi: reroo → rộộp.

**2816** — JP 「（れるっ――れろっ――ねろおっ）」; TW 「（舔――舔――舔）」; old_vn (CSV3) 「（Liếm――liếm――liếm）」; **fix = 「（Rộp――liếm――liếm）」**. Đổi: liếm → rộp.

**3816** — JP （れるっ）; TW （舔）; old_vn (CSV3) （Liếm）; **fix = （Rộp）**. Đổi: liếm → rộp.

### 4.9. T78a — 21 dòng (8 file). ずぶ (SFX) → 'Phập' theo công thức phụ âm (tổng số p = max(1, số う/ぅ)); chỉ đổi token ずぶ, giữ token khác trong chuỗi.

#### lr_ハチロクh1_今ひとたびの契り.txt.toml — 3 dòng

**1947** — JP （じゅぽっ――ずぶうううううううっ！ ぐりっっっ！）; TW （噴湧）; old_vn (audit) （Jupo——zubuuuuuuuu! Guri!!!）; **fix = （Jupo——phậppppppp! Guri!!!）**. Đổi: zubuuuuuuuu → phậppppppp.

**1949** — JP （ぱんっ！ ずぶっ！ ずばっ！ じゅぶうっ！！！）; TW （大力撻伐）; old_vn (CSV3) （Pan! Zubu! Zuba! Jubuu!!!）; **fix = （Pan! Phập! Zuba! Jubuu!!!）**. Đổi: zubu → phập.

**2000** — JP （ずぶうううううううううううっ！ ごつっ！！！）; TW （緩慢抽出，而後猛然插入）; old_vn (audit) （Zubuuuuuuuuuuuu! Gotsu!!!）; **fix = （Phậppppppppppp! Gotsu!!!）**. Đổi: zubuuuuuuuuuuuu → phậppppppppppp.

#### lr_ポーレットh2_デコレーション＆ミルク.txt.toml — 1 dòng

**1770** — JP （ずぶうううううううううううっ――――ごつっっ！！）; TW （用力頂入——到底！！）; old_vn (CSV3) （Đâm sâu uuuuuuuuuuu――――kịch!!）; **fix = （Phậppppppppppp――――kịch!!）**. Đổi: bỏ [đâm, sâu, uuuuuuuuuuu] → thêm [phậppppppppppp]. Span 3 từ ('Đâm sâu uuuuuuuuuuu') → 1 từ 'Phậ…' (11 p theo JP).

#### lr_稀咲h1_おしおきとごほうび.txt.toml — 1 dòng

**1705** — JP （ずぶううううううううううっっ！！！ ごちゅっ！！）; TW （啾嚕嚕嚕嚕嚕！！！咕啾！！）; old_vn (audit) （Zubuuuuuuuuuuu!!! Gochu!!）; **fix = （Phậpppppppppp!!! Gochu!!）**. Đổi: zubuuuuuuuuuuu → phậpppppppppp.

#### lr_稀咲ポーレットh1_悪い大人の契約.txt.toml — 9 dòng

**2535** — JP （じゅばっ！ ばちゅっ！ ずぶっ！ ぱつっ！！！）; TW （啾啪！ 啪啾！ 滋噗！ 啪噗！！！）; old_vn (CSV3) （Ju ba! Ba chu! Zu bu! Pa tsu!!!）; **fix = （Ju ba! Ba chu! Phập! Pa tsu!!!）**. Đổi: bỏ [zu, bu] → thêm [phập].

**2540** — JP （ずぶううううううううううううううっ！ ごちゅっ！）; TW （啾噗！！！ 咕啾！）; old_vn (audit) （Zu buuuuuuuuuuuuuuu! Go chu!）; **fix = （Phậpppppppppppppp! Go chu!）**. Đổi: bỏ [zu, buuuuuuuuuuuuuuu] → thêm [phậpppppppppppppp].

**2597** — JP （ずっ―ずぶっ―じゅぶっ―じゅびゅっ―）; TW （滋——噗——啾——啾噗——）; old_vn (CSV3) （Thọc——lún——ju bu——ju byu——）; **fix = （Thọc——phập——ju bu——ju byu——）**. Đổi: lún → phập. 'lún' → 'phập' (chữ thường, giữa chuỗi).

**2599** — JP （ずぶううううううううっっっっっっっっっ！！！！）; TW （滋噗————————！！！！）; old_vn (audit) （Zu buuuuuuuuu!!!!）; **fix = （Phậpppppppp!!!!）**. Đổi: bỏ [zu, buuuuuuuuu] → thêm [phậpppppppp].

**2600** — JP （ずぶっ！ ごちゅっ！ ぞりゅうっ！ ばちゅっ！！）; TW （滋噗！ 咕啾！ 呲溜！ 啪啾！！）; old_vn (CSV3) （Zu bu! Go chu! Zo ryuu! Ba chu!!）; **fix = （Phập! Go chu! Zo ryuu! Ba chu!!）**. Đổi: bỏ [zu, bu] → thêm [phập].

**2602** — JP （ずぶっ！ ばちゅっ！ じゅばっ！ ごちゅっ！！）; TW （滋噗！ 啪啾！ 啾啪！ 咕啾！！）; old_vn (CSV3) （Zu bu! Ba chu! Ju ba! Go chu!!）; **fix = （Phập! Ba chu! Ju ba! Go chu!!）**. Đổi: bỏ [zu, bu] → thêm [phập].

**2603** — JP （ずぶっ！ ばちゅっ！ ぢゅぶっ！ ずびゅっつ！！）; TW （滋噗！ 啪啾！ 啾噗！ 滋啾！！）; old_vn (CSV3) （Zu bu! Ba chu! Ju bu! Zu byu tsu!!）; **fix = （Phập! Ba chu! Ju bu! Zu byu tsu!!）**. Đổi: bỏ [zu, bu] → thêm [phập].

**2605** — JP （ずぶっ！ ずばっ！ ばちゅっ！ ずぱんっ！！！）; TW （滋噗！ 滋啪！ 啪啾！ 滋啪！）; old_vn (CSV3) （Zu bu! Zu ba! Ba chu! Zu pan!!!）; **fix = （Phập! Zu ba! Ba chu! Zu pan!!!）**. Đổi: bỏ [zu, bu] → thêm [phập].

**2608** — JP （ずぶうううううううううううううっ！ ごちゅんっ！）; TW （用力插入！ 抽插！）; old_vn (audit) （Zu buuuuuuuuuuuuuu! Go chun!）; **fix = （Phậppppppppppppp! Go chun!）**. Đổi: bỏ [zu, buuuuuuuuuuuuuu] → thêm [phậppppppppppppp].

#### ハチロクh3_磨き洗い.txt.toml — 1 dòng

**1835** — JP （ずぶうううううううううううっ！）; TW （插——！）; old_vn (moan) （Zubuuuuuuuuuuuu!!!）; **fix = （Phậppppppppppp!!!）**. Đổi: zubuuuuuuuuuuuu → phậppppppppppp.

#### ポーレットh7_残業エッチもyシャツで.txt.toml — 4 dòng

**1672** — JP （ぞっ――ずぶっ――ずるううっ――ずぽっ！）; TW （挖來挖去）; old_vn (CSV3) （Thọc——thọc——tuột——phụt!）; **fix = （Thọc——phập——tuột——phụt!）**. Đổi: thọc → phập. Chỉ đổi token ずぶっ (từ 2, chữ thường); ぞっ giữ 'Thọc'.

**1684** — JP （ずぶううううううううっ！）; TW （插入）; old_vn (audit) （Thọc sâuuuuuuuu!）; **fix = （Phậpppppppp!）**. Đổi: bỏ [thọc, sâuuuuuuuu] → thêm [phậpppppppp]. Span 2 từ ('Thọc sâuuuuuuuu') → 1 từ 'Phậ…' (8 p theo JP).

**1700** — JP （ずぶううううううううううううっ！ ごつっ！！！）; TW （進進出出）; old_vn (CSV3) （Thọc sâuuuuuuuu! Cộp!!!）; **fix = （Phậpppppppppppp! Cộp!!!）**. Đổi: bỏ [thọc, sâuuuuuuuu] → thêm [phậpppppppppppp]. Span 2 từ → 1 từ 'Phậ…' (12 p theo JP).

**1701** — JP （ずぶうううううううううっ！）; TW （頂入）; old_vn (CSV3) （Thọc sâuuuuuuuu!）; **fix = （Phậppppppppp!）**. Đổi: bỏ [thọc, sâuuuuuuuu] → thêm [phậppppppppp]. Span 2 từ → 1 từ 'Phậ…' (9 p theo JP).

#### 日々姫h4_いもうとタオル.txt.toml — 1 dòng

**1757** — JP （ずぶうううううううううっ！！！）; TW （噗呲！！！）; old_vn (moan) （Zubuuuuuuuuuu!!!）; **fix = （Phậppppppppp!!!）**. Đổi: zubuuuuuuuuuu → phậppppppppp.

#### 真闇h2_無濾過.txt.toml — 1 dòng

**1820** — JP （ずぶうううううううっ！）; TW （吱噗！）; old_vn (moan) （Zubuuuuuuuu!）; **fix = （Phậppppppp!）**. Đổi: zubuuuuuuuu → phậppppppp.

### 4.10. T78b — 2 dòng (2 file). ぬぶ — không quy tắc chung, từng dòng (xem ghi chú).

#### れいなh2_おもらし防止大作戦.txt.toml — 1 dòng

**1730** — JP （ぬぶうううううううううううっ――くぽっ）; TW （咕啾……咕啾！）; old_vn (CSV3) （Phậpppppppppp——bạch）; **fix = （Rúttttttttttt——bạch）**. Đổi: phậpppppppppp → rúttttttttttt. JP ぬぶ+11う → 11 t ('Rúttttttttttt'); CUR audit 'Phậpppppppppp' (10 p) và quyết gốc 'Rútttttttttt' (10 t) đều thiếu 1 — hiệu chỉnh theo M14 (tổng = 1 + số dấu kéo dài).

#### 真闇h2_無濾過.txt.toml — 1 dòng

**1830** — JP （ずぶっ――ずるっ――ぬぶぶぶぶっ）; TW （呲噗――擦――噗噗噗）; old_vn (CSV3) （Phập――trượt――phụt phụt phụt phụt）; **fix = （Phập――trượt――Rút rút rút rút）**. Đổi: phụt → rút ; phụt → rút ; phụt → rút ; phụt → rút. ぬぶぶぶぶっ = 4 mora ぶ → 'Rút rút rút rút'; ずぶっ giữ 'Phập'.

### 4.11. T79 — 1 dòng (1 file). きゃふ → romaji 'Kyafu' theo công thức nguyên âm.

#### 稀咲h3_チャイナドレスでおもてなし.txt.toml — 1 dòng

**1988** — JP 「らめっ！ そこっ！ おんなじとこ――きゃふっ！\nあたま――チカ、チカ――ひっ――らめに、なるっ」; TW 「不行！ 那裡！ 是一樣的地方――呀嗚！大腦――星星、星星――感覺冒金星了」; old_vn (CSV3) 「Không được! Chỗ đó! Vẫn chỗ đó――kya phu!\nĐầu em――chớp, chớp――hí――không xong, mất」; **fix = 「Không được! Chỗ đó! Vẫn chỗ đó――Kyafu!\nĐầu em――chớp, chớp――hí――không xong, mất」**. Đổi: bỏ [kya, phu] → thêm [kyafu]. 'kya phu' → 'Kyafu' (romaji, công thức nguyên âm).

## 5. Các dòng GIỮ (đã đúng hoặc ngoài phạm vi — có lý do)

### 5.1. T67 / T69 / T70 / T81 — GIỮ toàn bộ (đã đúng)

- **T67** (KEEP "buổi bình chọn", 0 dòng đổi): 日々姫07 2114/1883 — JP ひんぴょー会, VN đã "buổi bình chọn"; không có dòng 評議会 nào.
- **T69** (KEEP "Khách sạn Teio", 0 dòng đổi): グランドリライト08_ふかみ 1628/1858/1895/2155 — đã "Khách sạn Teio".
- **T70** (KEEP "Niigata", 0 dòng đổi): 稀咲h3 2648 — đã "Niigata" (audit đã sửa Ohimitera→Ohitoyo trong cùng dòng).
- **T81** (KEEP "Fukutake", 0 dòng đổi): ポーレットh8 2462 — audit đã sửa từ "Fukuoka" của Gemini thành "Fukutake".

### 5.2. Đã đúng trong phụ lục (không đổi)

- **T68**: 19/25 dòng phụ lục đã "Showa" (ハチロク12 2015; 日々姫03 2002/2749/2118; グランドリライト04 1910; lrれいな追加01 1778; グランドリライト05 1770; グランドリライト07 1549; 真闇01 1049/1966/1749/1750/1621/1610; ニイロク01 1514/1713/1765/1677; ニイロク02 1796).
- **T71**: 13/24 dòng đã "Tàu nhà hàng" (日々姫08 3343/3600/3090/2198/2501/2405/2944/2135/3574/2094/2270/3739/3736 — 3 dòng sau old_vn = fix U1a Ohitoyo).
- **T72**: 6/24 dòng đã "hình quạt" (日々姫02 1831/1706/1832/1617/1833; 日々姫03 2177).
- **T79**: 24/25 dòng đã romaji "Kyafu" (chỉ 1988 đổi "kya phu" → "Kyafu"; 2 dòng khác old_vn so với CUR do fix đã gộp: ハチロクh8 703 U11a "Fua"→"Fa", lr_稀咲ポーレットh1 1442 U7b P4 — cả hai đã "Kyafu").

### 5.3. T75 — 7 dòng GIỮ

- **2 dòng biên (đọc lại cảnh, KHÔNG phải hôn trần)**: 日々姫h6 3707 (ちゅぶっ → "Nhóp nhép" — các dòng kề 3702/3706/3708 là chuỗi SFX mô tả thrust/penetration; ちゅぶっ là tiếng ướt "pop", giống 3708 ぢゅぶっ → "Nhóp nhép"); ポーレットh3 967 (ちゅる―― → "Churu" — JP 「ちゅる――んっ……」 + câu nếm syrup; không có っ, kéo dài ――, ngữ cảnh liếm trượt, KHÔNG phải hôn).
- **5 dòng chỉ có token ngoài phạm vi** (quyết liệt kê token — ちゅず/ちゅく/ちゅりゅ không nằm trong danh sách; thực hành đa số là romaji chuzu/chuku/churyu, không phải "chụt"): ハチロクh9 2031 (ちゅずううっ), lr_日々姫h2 1037 (ちゅりゅっ), lr_日々姫h2 1652 (ちゅくっ), lr_稀咲ポーレットh1 2534 (ちゅくうううっ), 真闇h3 2357 (ちゅずっ) — cắm cờ cho coordinator (Kết bài).

### 5.4. T77 — 61 dòng trong phụ lục KHÔNG đổi + 2 dòng chỉ đổi T75

- **16 dòng token れる/るっ đã "rộp" từ trước** (audit/moan): lr_ポーレットh1 1203/1025/1043/1220/1060; lr_ポーレットh2 1020/1315/1105/1107; ポーレットh8 2289/2292/2203; れいなh1 1359/2341/2342/2350.
- **1 dòng động từ trong hội thoại**: れいなh4 2452 れるれるって "hãy liếm láp đi ạ" — KHÔNG phải token SFX, GIỮ.
- **44 dòng chỉ có れろ/れりゅ** (không có token れる/るっ SFX): xem danh sách đầy đủ ở §2 (tổng 61 = 44 + 16 + 1). Lưu ý: một số dòng đã có れろっ render "rộp" từ audit/moan (vd. lr_ポーレットh1 1065/1203/1089/1220; れいなh1 1358) — không nhất quán với F1-M68 ("liếm") nhưng れろ ngoài phạm vi T77 nên để nguyên, ghi chú tại đây.
- **2 dòng trong phụ lục T77 nhưng chỉ đổi T75**: ハチロクh9 2133 (chỉ có れろっ), lr_稀咲h1 1068 (chỉ có れりゅっ/れりゅうう).

### 5.5. T78 — các dòng loại trừ / GIỮ

- **T78a (ずぶ) — 4 dòng trong phụ lục không đổi**: lr_日々姫h1 1261, ポーレットh7 881, ふかみh1 971 (động từ trong hội thoại), 凪ふかみ07 3140 (mô tả ずぶずぶ). Ngoài phụ lục: lr_ハチロクh2 1466 (mô tả ずぶずぶ) cũng GIỮ. ずぶ濡れ/ずぶぬれ, ずぶつける không có dòng nào trong phụ lục. 真闇h2 1830: token ずぶっ đã "Phập" nên không đổi ở T78a — dòng đổi chỉ vì ぬぶ (T78b).
- **T78b (ぬぶ) — 8 dòng GIỮ theo quyết từng dòng**: 日々姫h3 1838, ポーレットh4 1609 (giữ "Rút" của audit — TW tự mâu thuẫn về ぬぶ), ポーレットh4 1604, れいなh2 1079, lr稀咲追加h 1828, lr_ふかみh2 1122 (xem dưới), lr追加 1505, ふかみh3 3926.
- **lr_ふかみh2 1122 (ぬぶっ → "Nubu!", GIỮ — quyết biên)**: các dòng kề 1118–1124 là cảnh miệng (Fukami: じゅぶっ/ぢゅぼっ/れるウウッ/ぺちゅううっ; JP 1122 「れりゅうっ――ずろおおおおおおっっ――じゅぶっ！\nん――ぺろっ、ペロッ――じゅうぅぅっ！――ぬぶっ！」, TW toàn âm miệng) — ぬぶっ là tiếng trượt trong miệng, hướng không xác định: không phải rút ra, cũng không phải đâm sâu. "Rút" sẽ khẳng định một chiều rút mà cảnh không hỗ trợ.

## 6. Quyết định trong đợt này

Tất cả quyết dưới đây là của coordinator (22/11 ~12:25, theo uỷ quyền Hieu) — worker chỉ áp, không tự quyết. Các mục "hiệu chỉnh lượt soát 2" là sửa lỗi kỹ thuật của lượt 1 (sai chỉ số từ), không phải quyết dịch mới.

- T67 KEEP "buổi bình chọn"; T69 KEEP "Khách sạn Teio"; T70 KEEP "Niigata"; T81 KEEP "Fukutake" (0 dòng).
- T68 "Showa" (6 dòng); T71 "Tàu nhà hàng" (11 dòng); T72 "hình quạt" tính từ (18 dòng); T73 "Hinomoto Nadeshiko" (3 dòng); T74 "hợp đồng chủ tàu" (1 dòng, GHÉP U2b); T79 "Kyafu" (1 dòng).
- T75 họ "chụt" cho MỌI âm hôn trần, theo token, công thức nguyên âm (71 dòng đổi / 78 phụ lục). Ngoại lệ: âm ướt có tiền tố, ちゅん (chim), ちゅるん (trượt), dạng động từ, phương ngữ, diễn đạt mô tả.
- T77 (ĐÃ SỬA so với khuyến nghị E2): "rộp" cho token SFX れる/るっ — **れろ LOẠI** (giữ theo F1-M68/U12a). ぺろ giữ "liếm"; じゅるっ giữ "rột" (chỉ đổi token れ). るっ trong chuỗi THRUST thuộc T78, trong chuỗi LICKING thuộc T77 — phân biệt bằng token kề.
- T78a ずぶ (SFX) → "Phập" (21 dòng; chỉ đổi token ずぶ trong chuỗi romaji, giữ token khác). T78b ぬぶ — không quy tắc chung, từng dòng (2 dòng đổi: 1730, 1830; 8 dòng giữ). Sau đổi từ T78 trên dòng U12b, kiểm lại tổng số chữ kéo dài M14 (đã làm — xem §7).
- **Hiệu chỉnh lượt soát 2 (5 dòng, §7)**: lr_凪h2 1290, lr真闇追加h 1162/1135, lr_凪ふかみh1 1644, ハチロクh6 934 — lượt 1 thay nhầm từ kề (chụt/mút/Ưc) do lệch chỉ số; lượt 2 sửa về đúng token れる/るっ.
- **Không áp F5 vào token romaji được GIỮ trong đợt này**: quyết coordinator 22/11 ~12:50 (romaji SFX viết hoa MỌI VỊ TRÍ) ngoài phạm vi T67–T81 — các token romaji còn lại trong dòng đã sửa (vd. "chuuuuu", "chuu u", "Reruuuu", "reru", "Juru", "Zubu") được GIỮ nguyên chữ hoa/thường, cắm cờ cho coordinator định tuyến (nhiều khả năng U15). Từ mới trong đợt là tiếng Việt ("chụt"/"rộp"/"Phập"/"Rút"), trừ "Kyafu" (T79, đã viết hoa — nhất quán F5).

## 7. Lượt soát 2 (second pass)

**Tổng: 304 dòng / tái kiểm chứng đúng 299 / sửa 5 / loại 0.** Mọi fix đọc lại từng giá trị đối chiếu JP (token-by-token), đặc biệt các dòng hand-corrected và mọi từ kéo dài (đếm lại số ô trong từng từ rộ…p, số p trong từng từ Phậ…p, số t trong Rút…t từ dấu JP). Parse-check một mình không đủ — lượt này bắt được lỗi mà parse-check không thấy.

### 7.1. Lỗi lệch chỉ số tìm được (5 dòng — đã sửa, xem §6)

Nguyên nhân gốc: `split_pieces` (aligner3) đếm ký tự `"` ASCII đầu giá trị thành 1 "từ", trong khi người đếm tay bỏ qua nó; và generator trên các dòng align=FAIL ánh xạ chỉ số JP → VN lệch 1 khi cụm VN gộp nhiều token JP (vd. "Ưm……hi-hamu……ưm" = 3 token JP). Hậu quả: từ kề bị thay nhầm thay vì token れる/るっ.

- **lr_凪h2 1290**: lượt 1 đổi ちゅっ→"rộp" và ちゅうう→"rộộộộp", để nguyên 2 từ "liếm" (れるっ/れるうううっ). Sửa: 「…hyuki——chụt——\nrộp——chụt——rộộộộp——chụt」.
- **lr真闇追加h 1162**: lượt 1 đổi ちゅっ→"rộp", れるっ→"rộộp", "liếm liếm"→"liếm". Sửa: 「Ưm——chụt——rộp——rộộp.」 (chỉ れるっ→"rộp"; れるうっっ "liếm liếm" → 1 từ "rộộp").
- **lr真闇追加h 1135**: lượt 1 đổi ちゅううっ "chụụụt"→"rộp", để nguyên "liếm" (れるっ). Sửa: chỉ れるっ→"rộp", giữ "chụụụt". (Ghi chú trong tóm tắt lượt 1 nói "liếm word 9→rộộộp" là SAI cả chỉ số lẫn độ dài — れるっ không có う nên là "rộp", không phải "rộộộp".)
- **lr_凪ふかみh1 1644**: lượt 1 đổi ちゅううっ "chụt"→"rộp", để nguyên "liếm" (れるっ). Sửa: chỉ れるっ→"rộp".
- **ハチロクh6 934**: lượt 1 đổi れろっ "liếm"→"Rộp", để nguyên "mút" (れるっ); chỉ số hand-correction [10] trỏ nhầm từ 10. Sửa: "mút"→"rộp" (chữ thường theo token cũ), giữ "liếm" (れろっ).

Kiểm tra hệ thống sau khi sửa: chỉ 2 dòng trong toàn đợt có old_vn bắt đầu bằng `"` ASCII (1162, 1135 — cả hai đã sửa); 70 dòng bắt đầu bằng （ không bị ảnh hưởng (`（` là delimiter, không tính là từ). Kiểm tra multiset chụt/rộp toàn đợt sau khi sửa: còn 8 dòng chụt giảm — tất cả ĐÃ kiểm chứng đúng (OLD render れる/るっ thành "chụt": れいなh2 1093/1081/1756, れいなh3 1089/1090/1091/1101, 凪h1 1118). Kiểm tra diff từng từ T75: 0 từ ngoài họ chu bị đổi, 0 từ ngoài họ chụt được thêm (8 dòng span split-romaji "Chu mu"/"chuu u"/"chu pa"/"chu ru"/"Chu bu"/"chu pu" gộp thành 1 từ — đúng quy tắc).

### 7.2. Đếm độ dài đã kiểm chứng lại (mẫu dài — đếm bằng máy từ JP)

- T77 1547: れる+13う → 14 ô. T77 1715: れる+7う → 8 ô. T77 1692: れる+4う → 5 ô. T77 1873: れる+5う → 6 ô.
- T78a ずぶ (số p = số う JP): 2000: 11; 1947: 7; 1835: 11; 1757: 9; 1770: 11; 2540: 14; 2599: 8; 2608: 13; 1684: 8; 1701: 9; 1700: 12; 1820: 7; 1705: 10. (Số u trong romaji cũ thường lệch ±2 so với JP — vd. 1700 OLD "sâuuuuuuuu" 8 u vs JP 12う; lấy JP làm chuẩn.)
- T78b 1730: 11 t (hiệu chỉnh M14 — xem ghi chú §4.10). T78b 1830: 4 mora ぶ → 4 từ "Rút".
- T75 dài: 1055 ちゅうううっ → "chụụụụt" (4 ụ); 2295 ちゅううううっ → "chụụụụụt" (5 ụ); 2351 ちゅうううっ → "chụụụụt"; 1056 ちゅうううううっ → "chụụụụụụt" (6 ụ).

### 7.3. Mâu thuẫn số liệu moan (ghi chú, không ảnh hưởng đợt này)

Map load 1.516 mục moan duy nhất (66 file, 1.535 fix); tổng kết cuối của coordinator là 1.512 dòng (64/64 file, gồm supplement ハチロクh3 +4) — chênh 4 dòng, chưa điều tra; old_vn từng dòng đã kiểm chứng riêng nên không ảnh hưởng U13b.

## 8. Khối TOML (parse-verified, theo file)

63 file / 304 key. Literal `\n` trong fix viết `\\n` trong khối; key là string. Đã parse-verified bằng `tomllib` — mọi giá trị parse ra khớp JSON.

# lrれいな追加01_はじめての冬.txt.toml
```toml
[script]
"1397" = "「Nếu là xăng chỉ số octane cao, Reina thấy X-Power\\ncủa Dầu mỏ Showa Shell là hợp khẩu vị nhất nha~」"
```

# ハチロク03_冥国式レイルロオド.txt.toml
```toml
[script]
"2176" = "「A…… không, dù vậy——cô ấy vẫn chạy cho đến năm Showa 11.\\nSau đó mới chuyển sang tuyến chuyên dụng của Tsurumi Seitetsu Zosen.」"
"2550" = "「Ở đó, cô ấy làm việc đến tận năm Showa 49——thực sự rất lâu nhỉ.」"
```

# ハチロクh9_コノフクハキルコト.txt.toml
```toml
[script]
"1410" = "「……Có đầy đủ từ cuối thời Minh Trị (Meiji) đến những năm đầu thời Showa sao.\\nThế này thì đáp ứng được yêu cầu của Paulette rồi.」"
"2033" = "「Fu……ưm————（Ực）\\nZu——chụt——juuu——（Ực）」"
"2124" = "「Chụt——chụt——chụụụt——（Ực）」"
"2127" = "「Juuuuu! Jubo! Chụt! Jubu,\\njubo! Chụụt! Juru! Ju! Bo!」"
"2128" = "「Chụụt! Ju! Jururu! Jubo!\\nƯm——chụụt! Ju! Jubo! Ju!」"
"2133" = "「Chụụt——chụt, zu——pero, pero, pero,\\nchụụt, chụt——rero——pero, perooo」"
"2145" = "「Ưm——chụt——chụt! Jubo!\\nJu! Jubo! Juryuuu! Ju, bo!」"
"2147" = "「Ưm——chụt! Ju! Jubo! Ju,\\njuchu! Chụt! Juru! Jubu!」"
"2153" = "「Ưm——hamu——chụt——chụụụt, chụt」"
"2182" = "「Ưm mu!? Ưm——chụt——ju!\\nJubu! Jumu! Fu——chụt, ju!」"
"2122" = "「Chụt——ju——juru——juuu——\\nƯm——rerooo——rộp——rộộộộộp」"
"2138" = "「Chụt! Ju! Jubo——ưm, Fu,\\nrộp——ju! Jubo! Juruuu!」"
"2140" = "「Chụt, rộp——chụụụt, chụt——\\nZuzu——ưm——chụt——rero, rộộp」"
"2035" = "「Hu……a——ưm——rộp——chụt——\\nliếm láp——mút mát——rộp——ưm——mu chu」"
"2043" = "「Rộp——rộp——rộộộộp——ju, zu——\\nzu——rero——rộộộp——zuzu——zuu」"
"2120" = "「Chụt——rộp——mút——chuuuu——\\nchóp chép——（Ực）——ưm——chụt, chụt」"
"2156" = "「Ưm……chụt——chumu——chụt——ưm——\\nrộp——liếm láp——chóp chép——rộp——chu pu」"
```

# 仲国02_北琴の鉄道.txt.toml
```toml
[script]
"2492" = "「Năm Showa 59! Trời ơi!!!!」"
"2617" = "「Suika cũng nghĩ nó nằm trong phạm vi mới toanh.\\nCông trình cải tạo mới nhất là vào năm 2004. Theo lịch Hinomoto là năm Showa 59.」"
```

# 日々姫07_姉の想い。妹の想い.txt.toml
```toml
[script]
"1358" = "『Tàu nhà hàng』"
"2572" = "Hãy nhờ bác ấy trở thành thanh ray đầu tiên,\\nkết nối với 'Tàu nhà hàng' của chúng tôi."
"1428" = "「……Tình nguyện viên ở Bungomori đã nói.\\nGara đầu máy hình quạt là một biểu tượng」"
"1892" = "「Thực ra, chúng tôi cũng nghĩ vậy.\\n\\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#; mà không có \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; thì thật sự không ra thể thống gì」"
"2263" = "「Nếu phải nói thì——trong chuyến du lịch, tôi muốn toa ăn du lịch nghỉ dưỡng\\nđược đưa vào \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;」"
"2575" = "Ngắm nhìn \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; từ bên trong, lùi lại,\\nqua \\x%l転車台;#00ffc040;bàn quay đầu máy%l;#;, rồi lại quay về tuyến chính——"
"2609" = "Khi chúng tôi ghé thăm \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; ở Bungomori,\\nkỹ sư lão thành Kimoto lại nồng nhiệt chào đón chúng tôi một lần nữa."
```

# 日々姫08_とれいん食堂.txt.toml
```toml
[script]
"1572" = "「Có vẻ như việc đón khách lên 'Tàu nhà hàng' bắt đầu rồi」"
"2082" = "「Đội A của 'Tàu nhà hàng' gồm Nagi và Fukami.\\nDù là một sự bố trí nhân sự táo bạo nhưng——」"
"2258" = "「Ẩm thực và du lịch tuyệt vời nhất tại mọi ga dừng của Tàu nhà hàng.\\nNhờ có được những yếu tố có thể khẳng định như vậy nên mới có thiết kế này ạ」"
"2431" = "「Vâng. Alo. Hayase của Tàu nhà hàng xin nghe.\\nHả? A——vâng. Chậm trễ——a, vâng. Cháu hiểu rồi ạ」"
"3038" = "Railord của Tàu nhà hàng, được kế thừa từ trước khi cải tạo, là hàng do Minh Quốc sản xuất——"
"3319" = "Vé trọn gói khứ hồi của Tàu nhà hàng chuyến số 1,\\nmón quà mà tôi và Hibiki đã tặng."
"3608" = "Vì bác Tochigi rất thích ý tưởng 'Tàu nhà hàng', nên bác ấy đã không ngần ngại giới thiệu các mối quan hệ của mình cho chúng tôi."
"3652" = "Thiết kế bởi Migita Hibiki. Toa ăn tự hành 'Tàu nhà hàng'.\\nĐăng ký xe thuộc Đường sắt Hisatsu Mikan, \\x%lHSMK;#00ffc040;HSMK%l;#;114 và \\x%lHSMK;#00ffc040;HSMK%l;#;116."
"1521" = "……Em ấy đang bồn chồn. Tôi hiểu cảm giác đó.\\nNhưng đây là \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; Bungomori. Là nơi công cộng."
"1619" = "「……\\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#; tuyệt thật đấy nhỉ.\\nỞ Ohitoyo tôi chưa từng thấy bao giờ.」"
"2032" = "「Nghĩa là chúng ta sẽ kéo dài thời gian dừng xe tham quan ở \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; đến 18:40 đúng không ạ?」"
"2117" = "「Theo dự kiến ban đầu, 18:00 sẽ đến ga Bungomori. Sau khi trải nghiệm đưa xe vào \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; và trải nghiệm bàn quay đầu máy, 18:30 sẽ xuất phát.」"
"2264" = "「Sẽ có 20 phút xuống xe tham quan bên trong \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;.\\nTheo dự kiến, chúng ta sẽ chuẩn bị \\x%lギャレー;#00ffc040;bếp trên tàu%l;#; trong khoảng thời gian đó ạ.」"
"2292" = "「Nếu chậm trễ 15 phút, thì việc chuẩn bị \\x%lギャレー;#00ffc040;bếp trên tàu%l;#; trong lúc dừng xe tham quan ở \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; sẽ khá là khó khăn đấy.」"
"2296" = "「Giả sử 18:20 món ăn được đưa đến, mất 20 phút chuẩn bị,\\n18:40 đưa xe ra khỏi \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;――vậy là vẫn bị chậm 15 phút à.」"
"2730" = "「Là vậy đó. Nagi, xin lỗi em nhưng,\\nhãy hỏi xem Bungomori――\\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; có thể “đến sớm 5 phút” được không nhé.」"
"2734" = "「Vậy thì 17:55 đến Bungomori. Từ 18:00 tham quan \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;.\\n18:20 đưa xe ra khỏi \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; và trải nghiệm bàn quay đầu máy.」"
"3052" = "Vì dự kiến ban đầu là 18:05 đưa xe vào \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;, 18:25 đưa xe ra khỏi \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; mà……"
"3089" = "Phía trong cùng của \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;, tấm bạt che chắn\\nnhô lên một khối hình người."
"3392" = "Ba bữa ăn chính, một bữa tiệc trà.\\nHơn nữa còn được trải nghiệm việc đưa vào \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#;, một lịch trình dày đặc."
```

# 日々姫09_run_with_our_dreams.txt.toml
```toml
[script]
"1753" = "「Hả? Ơ!? \\nRõ ràng bảo ngày mai sẽ đi Tàu nhà hàng mà.」"
```

# 日々姫06_みくろ、来訪.txt.toml
```toml
[script]
"3059" = "Nếu kết hợp với đầu máy hơi nước,\\ngiá trị du lịch của \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; sẽ càng tăng cao hơn nữa."
```

# ハチロク09_もくもくオリヴィ.txt.toml
```toml
[script]
"1508" = "「Niiroku cũng là Hinomoto Nadeshiko nhỉ~!\\nThích thật đấy, tóc đen! Ghen tị quá đi!!」"
"1879" = "「Chính vì vậy Đầu máy số 9. So với Hinomoto Nadeshiko Hachiroku,\\ncó lẽ mang một chút gì đó của ngựa chứng hoang dã nhỉ.」"
```

# ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml
```toml
[script]
"993" = "「Bên trong Suzu, tôi cũng hiểu rất rõ.\\nBên trong âm đạo của một Hinomoto Nadeshiko thanh thuần như em——」"
"838" = "「Rộp——Chụụụt——ưm——phù——ưm——\\nphù——ưm! Phù! Ưm ưm ưm!!!」"
"834" = "「Phù! Ưm——ưm! Ưm! Ưm! Phù!\\nRộp——liếm——chụt——rột——ực」"
"884" = "「Ưm——phù——phù——phù——ư——liếm——\\nrộp——chụt——Fa.」"
"887" = "「Ưm——phù——rộp——rộp——ưm——\\nchụt——ưm ku——phù——phù ư ư!」"
"894" = "「Ưm——a——chụt——ưm——chụm——\\nchụt——rộp——liếm——phù……ưm……chụt」"
"899" = "「Ưm——phù——ưm——ực——chụt!\\nỰc! Rộp——chụt——ực——ực!」"
"934" = "「Ưm ưm ưm ưm~~~!! Ưm, phù——ưm! Phù,\\nưm, rộp——liếm——Juuu——rột rột~!」"
```

# 凪h2_おとなの水着.txt.toml
```toml
[script]
"1766" = "……8620 đã hoàn toàn hồi sinh, và tôi cũng đã ký kết hợp đồng chủ tàu thông thường\\nvới Đường sắt Ohitoyo."
"2425" = "「Phù——Ưm——Chụt——Chụt——Rộp——\\nChụt——Ngoáy——Rộp——Rộp——Chụt」"
"2496" = "「Hyo ha hyo ho——Ưm——rộp, ngoáy, chụt,\\nchụt——liếmm, chụt——sụt——chụt chụt」"
"2558" = "「Ưm……Phù, phù——Rộp——Chụt, sụtttttt\\nSụt sịt——Ực——Ưm……Chụt——Rộp, ngoáy」"
"2559" = "「Ưm……Chụt——Liếm——Rộp——Chụt,\\nChụt sụt——Sụt, tuột——Chụt, ngoáy」"
"2561" = "「Ưm……Chụt——Chụttt——Chụt——Chụt chụt,\\nChụt——Ực——Chụt, chụt——Ngoáy, Rộộộp」"
"2562" = "「Ưm……Chụt——Chụt——Chụttt, chụt,\\nLiếm, liếm——Rộp——Ngoáyyy——Chụt」"
"2563" = "「Ưm……Chụttt——Chụt——Ưm——Phụt,\\nFa——Ngoáy——Rộp——Liếm liếm, chụt」"
```

# lr_ハチロクh1_今ひとたびの契り.txt.toml
```toml
[script]
"1234" = "「A……——ưm——chụt——chụụt——Ư」"
"1241" = "「Amu——fu——ưm——reu——ryu——\\nChụt——chụụt——juryu——」"
"2008" = "（Chụt——puryu）"
"2011" = "（Pu——chụụt——）"
"1213" = "「Ưm…… chụt——chuzu——ju——(ực)\\n——chụt——rộp——rero——churyu」"
"1947" = "（Jupo——phậppppppp! Guri!!!）"
"1949" = "（Pan! Phập! Zuba! Jubuu!!!）"
"2000" = "（Phậppppppppppp! Gotsu!!!）"
```

# lr_凪h1_痛いの痛いの飛んでけばい.txt.toml
```toml
[script]
"1158" = "「Ưm ku! Fua――á――ưm――（Ngoạm!）\\nJuru――chụt! Juru! Juba!!」"
"1162" = "「Ưm ku!? Pu――fa――ưm――juru!\\nJubo! Jubu! Juba! Chụụụt」"
"1218" = "「Jumu! Jubu! Jubo! Juba!\\nJu! Chụt! Chụt! Juba!!」"
"1219" = "「Gupo! Jubo! Chụt! Chụụụt!\\nKu! Ryu! Chụụụt! （Ngoạm!!）」"
"1220" = "「Juru! Reruuuu! Rero! Chụt!\\nƯm! Jubu! Jubo! Ju! Jubu!」"
```

# lr_日々姫h2_デザートは食事の前に.txt.toml
```toml
[script]
"998" = "「Dyubo! Ju!! Jyururu! Chụt, ba!\\nƯm——jyubo! Chụụt! Juru! Jubu」"
"1041" = "「Chụt——momu! Hamu——amu——\\nƯm…… hamu——kapu——mopu——amu——」"
"1056" = "「Gupo! Gupa! Chụt! Juzu! Zu!\\nJurururu! Jyubo! Reru! Buchuu!」"
"991" = "「Amu——chụt——hamu——chụt——mu——\\nKapu——rộp——amu——juru——hamu!」"
"1038" = "「Hamu——rộp——amu——chụụt——hamu,\\nChụt——famu——chụụt——ưm——Ư!!!」"
"1016" = "「Chụt——rộộp——chụt——chụt, chụt,\\nreryuuu——rero——chuuuuuuuu!!」"
"1033" = "「Rộp——nhóp nhép——mút——rộp——phập——\\n『Hyababa, bafi』, pua——pu——nhóp nhép.」"
"1036" = "「A~~——ưm~——rộp——nhóp nhép——ưm……\\nReryuuuu——rộp——liếm nhẹ——rechun」"
"1039" = "「Liếm——rộp——nchu——rộp——liếm nhẹ,\\nreryu——chụt——chụt——chuuuuu!」"
"1042" = "「Ưm…… ha——ưm——chụt——rero——chụt,\\nreryuuu——rero——mút——rộộộp」"
"1045" = "「Chuuuuuuu! Ưm…… ực——Fu, a\\n——rộp——rerooo——chụt——chuuu」"
"1046" = "「Rộp——liếm nhẹ——chụt——chuuu——\\nƯm…… liếm nhẹ——reryu——liếm nhẹ——juzuu!」"
"1053" = "「Churooooo——rộp——chụt, chụt——\\nChụt——rộp——chuzu——zu, zuuuu」"
"1675" = "（Bật ra! Rộp! Nhóp nhép! Bật ra!）"
```

# lr_稀咲h1_おしおきとごほうび.txt.toml
```toml
[script]
"1023" = "「Aaaan……(hapu)――chụt――chụụụt,\\nchụt――zu――――――(koku)――pua.」"
"1046" = "「Chụt.」"
"1053" = "「Chụt――chụt――chụt――chụụụt.\\nPhù――há――chụt――chụt――juru.」"
"1055" = "「Reryuuuu――reryu――nuryu――(koku)\\nchụt――chụt――chụụụt――chụụụụt.」"
"1058" = "「Jumu! Jubo! Bo! Juuuuuu!\\nZubyu――chụt――reru――zubo! Bochu!」"
"1068" = "「Ưm……chụt――chụt――chụt……re――ryu,\\nreryu――chụụt――chụt――reryuuu.」"
"1069" = "「Ưm……phù――chụt――chụt――\\nchụt――ju――jupu――juba――」"
"1133" = "「Chỗ này đây. Chụt!)」"
"1688" = "（Sunyu――kuchu――chuku――chụt）"
"1041" = "「Reryu――pero――chụt――chụt――\\n(pua), ưm――chụụt――zuchuu――rộp.」"
"1054" = "「Rộp――reryu――ưm――juzu――(koku)\\npua――thích――thích lắm, thích――ưm――chụt――chụụt.」"
"1056" = "「Chụụụụụụt! Juryu! Jubo!\\nRộp――Reroooooo! Chụụt! Ju!」"
"1705" = "（Phậpppppppppp!!! Gochu!!）"
```

# lr_稀咲ポーレットh1_悪い大人の契約.txt.toml
```toml
[script]
"993" = "「……Ừm, Kisaki.\\n——Ưm——ưm! ——Chụt——（Chạm nhẹ）」"
"1397" = "「Làm tình——làm tình. Làm tình với anh Soutetsu và Kisaki. Ba người cùng nhau……Fa——chụt——chụụụt——」"
"1584" = "「Chụụụt——ưm……chụt. Fa……Ưm, Kisaki………… Nè? ——Cảm ơn em.」"
"2537" = "（Chụt——chụt——chu ju——chu ku）"
"2547" = "（Cọ——chu ku——chụt——ju ru——）"
"2560" = "（Nhào nặn——chụt! chụt! Ju bu!）"
"1585" = "「Chụt——rộp——chuu u——chu mu——\\nchu pa——chuu u! Chu bu! Chuu u!」"
"1587" = "「Chuu u, chụt——ưm——rộp——rê ryu,\\nchuu u uu——zu chuu u——rộp, rê ryu」"
"1820" = "「Rê ryu——chụt——chuu u uu——rộp——\\nrộp——pê ro oo——chụt——chuu u uu」"
"1821" = "「Rộp——rê ro——rê ryu——ryu——\\nchuu u——chụt——pê ro——pê chu——」"
"2535" = "（Ju ba! Ba chu! Phập! Pa tsu!!!）"
"2540" = "（Phậpppppppppppppp! Go chu!）"
"2597" = "（Thọc——phập——ju bu——ju byu——）"
"2599" = "（Phậpppppppp!!!!）"
"2600" = "（Phập! Go chu! Zo ryuu! Ba chu!!）"
"2602" = "（Phập! Ba chu! Ju ba! Go chu!!）"
"2603" = "（Phập! Ba chu! Ju bu! Zu byu tsu!!）"
"2605" = "（Phập! Zu ba! Ba chu! Zu pan!!!）"
"2608" = "（Phậppppppppppppp! Go chun!）"
```

# れいなh1_おかあさんのレッスン.txt.toml
```toml
[script]
"2351" = "（Chụụụụt!）"
```

# れいなh3_おもらし自由化大作戦.txt.toml
```toml
[script]
"1083" = "「Funya——ưm——chụt——chụụt——\\nChụt——chụt——Fa——n~——chụt」"
"1089" = "「Rộp——liếm——chụt——chụt——\\nƯm……ammmmm——」"
"1090" = "「Ưm……Ưm——ưm——ưm——\\nRộp——chụt——chụt——chụt」"
"1091" = "「Ưm——nfu——rộp——rộp——\\nChụt——chụt——chụt——chụtttttt」"
"1101" = "「Phù……ưm——chụt……chụt——\\nE mu——rộp——chụt——ưm」"
```

# ハチロクh1_契り.txt.toml
```toml
[script]
"2147" = "（Chụt）"
"2132" = "（Rộp——sượt——Juchu——Juru）"
"2133" = "（Rộp）"
"2149" = "（Liếm――rộp――liếm láp――chụt――Juru――）"
```

# ハチロクh2_お勉強の成果.txt.toml
```toml
[script]
"1021" = "「Chụt!」"
"1206" = "「Rộp——rộp——liếm——chu mút——\\nưm——ưm chụt——chụt——chuuuuu」"
```

# ハチロクh8_桜色のひめごと.txt.toml
```toml
[script]
"794" = "「Chụt……——ưm——pua——a! Ngài Soutetsu……\\nLúc nãy——ngài vừa mới xuất, nhiều đến thế……mà——ưm」"
"805" = "「Chụt——liếm——rộp——rộp——chụt——\\nchụttttt——ngoạm——liếm——rộp——nhóp nhép」"
"809" = "（Chụt! Chụt! Ưm——chụt——phù!\\nRộp——liếm——chụttttt——chụt, chụt!）"
"825" = "「Ưm……chụt——liếm——rộp——chụt——\\nchụt……ưm……liếm láp——mút mát——chụttttt!」"
"827" = "「Ưm……chụt——ưm ưm ưm——Fua——phù——\\nchụt——chụt——rộp, mút mát, ưm, chụt」"
"829" = "「Ưm……chụt——chụt——rộp——mút……liếm láp\\n——phù……ưm……Ngậm——ngoạm——chụt, chụt chụt」"
"1547" = "（Rộộộộộộộộộộộộộộp!!!）"
"1548" = "（Rộp! Nhóp nhép! Mút mát! Chóp chép!）"
"1549" = "（Rộp! Mút! Nhóp nhép! Chóp chépppp!）"
"1575" = "（Chóp chép——nhóp nhép——chụt——rộp——）"
```

# ポーレットh4_クリーム＆クリーム.txt.toml
```toml
[script]
"1576" = "（Chụt——）"
"932" = "「～——ưm! Ưm——chụt——Chumuu——\\nƯm——Phùu——liếm——rộp——liếmmmm」"
```

# 真闇h1_長期熟成.txt.toml
```toml
[script]
"1094" = "「Ưm! Npu――Chụt――ưm, Chụt――Chụt.」"
"1048" = "「Hapu――ưm――rộp――chụụt――rột.」"
"1056" = "「Chụt――ưm……ưm chụt――rộp――liếm\\n――ưm……ưm fu……fu」"
```

# 真闇h2_無濾過.txt.toml
```toml
[script]
"1078" = "「Hapu――ưm――chụụt――」"
"1083" = "「Chụt――rộp――rột――chuuu.」"
"1103" = "「Ưm……rộp――chụt――rột.」"
"1845" = "（Rột――chụt――rộp――chumuu）"
"1820" = "（Phậppppppp!）"
"1830" = "（Phập――trượt――Rút rút rút rút）"
```

# 真闇h3_補習授業の廃校舎.txt.toml
```toml
[script]
"2276" = "「Hamu――chụt――chụt――koro――\\nưm……chụt――rero, koro――koryu.」"
"2288" = "「Chụụt――chụt――hamu, amu――ưm\\nchụt, chụt, koro――chụụụụụụt.」"
"2294" = "「Jubo! Boju! Jubo! Juba!\\nJu! Chụt! Jubo! Juru!!」"
"2295" = "「Jubo! Jubu! Ju! Jububu!\\nJubo! Chụụụụụt! Ju! Juba!」"
"2332" = "「Ưm……chụt――ưm chụt――chụt――chụụt,\\nchụt――chụt, mu――ưm――reru――pua.」"
"2334" = "「Ưm……chụt――ưmm――pua――\\nDù không, ngon lắm――ưm――chụt（ực）」"
"2336" = "「Ưm……chụt――zuro――chụt, ruu, ru.」"
"2424" = "「Picho, pecho――chụụt――perororo!」"
"2198" = "「Pero――reroooo――pero, pechu.\\nChụt――chụt――rerooooo――rộp.」"
"2290" = "「Chụt――re, rộp――chụụt――chụt, chụt\\nchụụt――chụt――rero――rộộộp.」"
"2292" = "「Chụt――rộp――rero――chụt, ru――\\nưm……kinh quá……nặng trĩu……nặng trịch luôn.」"
"2316" = "「Ưm――chụt――chụt――chụụt――ưm\\nrộp――chụụt――chụt――chụt, mu――」"
"2348" = "「Ưm phư――ưm――haa――ưm――chụụt――\\nrộp, rero――chụt, chụt――(Cắn!)」"
"2350" = "「Ưmpu――ưm――rero――rero, zu――ju,\\nchụt――chụụt――chụt, rero――rộộp.」"
"2299" = "「Juuu! Jubo! Jururu~~nyubo!\\nJuruuu――rộộộp――jubo! Gabo!」"
"2363" = "「Ưm!? Phư――amu――rột――churu,\\nchụt――rộp――jumu――chu, chuuu.」"
```

# 稀咲h2_プライベートルーム.txt.toml
```toml
[script]
"1250" = "「Đúng, là vậy đó――Cho, nên…… ưm――fua――\\nĐặc biệt là…… phần đỉnh――đó――nha? ――Ưm――chụt」"
```

# lr_日々姫真闇h1_三人家族.txt.toml
```toml
[script]
"1522" = "「Muchu――chụụt――pero――reryu――chụt\\n――rộộộp――nuro――juuu――mu, chụt」"
"1573" = "「Chụt――ưm――rộp――rê ryu――churyu,\\nchu――muchuu――reryuu――chu, chuzu」"
"1579" = "「Ưm…… 'Aaaaaaaan' Amu――Ư――\\nChụt――rộp――rộp――chùn chụt――rê ryu」"
"1585" = "「Ưm…… chụt――reryu――chụt――juyuu\\n――rộộp――rero――chụt――chuzu, zu」"
```

# lr_れいなh1_レディ・れいな.txt.toml
```toml
[script]
"1251" = "「A mút——rộp——chu~——chụt——chụt\\n——chu mút. Ưm…… hôm nay có hơi mặn một chút nha~」"
"1266" = "「Chu mút! Chụt mút! Chụt! Chu mút t!\\nRộp——liếm m! Sụt! Chụt mút! Chu mút」"
```

# lr_ハチロクh2_新しい服。新しい旅.txt.toml
```toml
[script]
"1715" = "「（Rộộộộộộộp）——Chụt! Chụt——\\nChụt! Chụt! Chụt! Phụt! Chụt!」"
"1716" = "「（Nụtọooo——rộp——Chùn chụt）\\nChụt! Phụt! Chụt! Phụt!」"
```

# lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml
```toml
[script]
"1278" = "「Chụụt——chụụt——rộp——chụụt——chụt——rộp——chụt——liếm!」"
"1281" = "「Chụt——chụt——chụt——liếm—— liếm——chụụt——liếm——rộp」"
"1283" = "「Chụt——chụụt——chụt——chụt—— chụt——liếm——rộộp——chụụụ~~」"
```

# lr_凪h2_虎さんの交尾.txt.toml
```toml
[script]
"1282" = "「Chụt——chụt——rộp——liếm——\\nchụt——rộp——chụt——chụt——ưm」"
"1283" = "「Rộp——liếm——nhóp nhép——nhóp nhép——\\nưm——~~~~~~——ưm——chụt——rộp」"
"1285" = "「Chụt——chụt——rộp——liếm——\\nju——zujuuu——（Ực）——pua」"
"1288" = "「Chụt! Ưm——chụt——nhóp nhép——nhóp nhép——\\nliếm——rộộp——nhóp nhép——!!!?」"
"1290" = "「Ưm……hi-hamu……ưm——hyuki——chụt——\\nrộp——chụt——rộộộộp——chụt」"
"1292" = "「Ưm——chụt——chụt——chụt——\\nliếm——liếm——liếm——rộộp」"
"1308" = "「Nhehe——anh Soutetsu——chụt! Chụt——\\nrộộộp——liếm——nhóp nhép——chụt!」"
"1804" = "（Nhóp nhéppp——rộp——liếm——ngoáy）"
"1808" = "（Ngoạm! Chụttt! Mút! Rộp!）"
"1846" = "（Rộp——ngoáy! Liếm——ngoáy!!）"
"1848" = "（Rộộộp! Ngoáy!!!!!!）"
"1851" = "（Rộp——liếm——ngoáy! Chụt, chụt）"
"1853" = "（Chụt——chụt——rộp——chụt）"
```

# lr_凪ふかみh1_じぇいけい！.txt.toml
```toml
[script]
"1403" = "「Dễ thương quá. Nagi——chụt——rộp——liếm——\\nchụt——chụt——liếm——rộp——mút」"
"1513" = "「Fa——Fukami, Fukami……ưm……\\nChụt——rộp——liếm——ưm——chụt——chụt」"
"1630" = "「Liếm——rộp——ngoáy——ngoáy——\\nchụt——liếm——ưm……rộộp——liếm, liếm」"
"1641" = "「Liếm——ngoáy——liếm——mút——\\nrộộp——liếm! ——Liếm——nhóp nhép!」"
"1643" = "「Liếm——mút——liếm——rộp——\\nmút——mútttttt——（Ực）——pua」"
"1644" = "「Liếm——chụt——ưm chụt——mút——\\nưm……chụt——chụt——rộp——mút」"
"1646" = "「Chụt——chụt——rộp——liếm——ưm——\\nju——zu——zujuuuuu——（Ực）——pua」"
"1647" = "「Rộp——liếm——liếm——mút——\\n（Ực）——Puha, tinh dịch, nhiều phết đấy nhỉ~」"
"1660" = "「Ưm……liếm——liếm——liếm——\\nfu——ưm——liếm——rộộộp——liếm」"
"1661" = "「Ưm……chụt——chụt——chụt——rộp,\\nliếm, liếm——chụt——chụt, chụt」"
"1670" = "「Ừm——chụt——chụt——rộp——liếm」"
```

# lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml
```toml
[script]
"1475" = "「Ưm――chụt――chùn chụt――chụt――rộp――\\nrê ryuuu――chùn chụt――chu――zuryu――ru」"
"1477" = "「Ưm――rộp――rê rô――chùn chụt――chụt――\\nƯm…… chụt――chùn chụt――（Ực）――pu, a」"
```

# lr_真闇h1_僕のおねえちゃん.txt.toml
```toml
[script]
"1477" = "「Chụt——chụt——chụt——rộp——\\nrột, rột——chụt——chụt——phuha」"
"1507" = "「Ưm——rộp——nchu——liếm!」"
"1655" = "「Rộộộộp——chụt——ku, ryu——trơn tuột!\\nChụt——liếm——xoay, ku——trơn tuột!!」"
```

# lrれいな追加h_夜の花嫁修業.txt.toml
```toml
[script]
"1138" = "「Ngoạm——chụt——chụt——chụt——ưm……\\nRộp——liếm——chụt——chụt——rộp」"
"1152" = "「Chụt——chụt——sụp soạp——（Ực）\\nRộp, liếm——liếm——（Ực）」"
```

# lr真闇追加h_赤ちゃん、欲しか.txt.toml
```toml
[script]
"1135" = "\"「Liếm liếm——chụt——chùn chụt——（Ực）\\nƯm……chụt——chụụụt——rộp——liếm liếm.」\""
"1162" = "\"「Ưm——chụt——rộp——rộộp.」\""
"1817" = "（Rộp——liếm——nhóp nhép——nhóp nhép）"
"1818" = "（Ưm——chụt——rộp——rộp rộp rộp rộp）"
"1861" = "（Chụt——chùn chụt——rộp——chụt）"
"1877" = "（Liếm——chụt——chùn chụt——rộộộộp）"
"1879" = "（Rộp）"
```

# lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml
```toml
[script]
"1819" = "（Liếm――rộp――chụt――Zuchuuuuu）"
```

# lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml
```toml
[script]
"1527" = "「Chubu——Chuu——Rộp——Reryuu——\\nChuu——chụt——Chumumuu——Pua」"
"2184" = "「Ưm……chụt——Rộp——Rero——ưm——\\nChumu——Chuu——chụt——Jururuu」"
"2331" = "「Chụt——Rộp——Jubu——Chuboooo——\\nChuru——Rộp——Kupuuuuuu——Pua」"
```

# ふかみh1_ともはり練習.txt.toml
```toml
[script]
"1035" = "「Chụt bụp——chụt——chụt——chụt——\\nRộp——liếm——liếm liếm liếm——chụt」"
"1036" = "「Rộp——chụt! Nhóp nhép! Bụp!\\nChụt rột! Chụt! Chụt! Chụt rột!!」"
"1037" = "「Chụt! Chụt rột! Rột! Chụt!\\nƯm——liếm——rộp——liếm liếm liếm——nhóp nhép!」"
"1553" = "（Rộp! Liếm——chụt——ngoạm!）"
```

# ふかみh2_homesweethome.txt.toml
```toml
[script]
"1002" = "「E mu——ưm——rộp——liếm——\\nLiếm m m——phù——ưm——sụt——sụt hi」"
```

# れいなh2_おもらし防止大作戦.txt.toml
```toml
[script]
"1081" = "「Fa——a——chụt!——chụt——chụt——\\nRộp——chụt——chụt——chụt——chụt!」"
"1093" = "「Ưm……a ưm——chụt——rộộộp」"
"1756" = "（Chụt——rộp——chụt——chụt）"
"1730" = "（Rúttttttttttt——bạch）"
```

# れいなh4_ふたりっきりのハロウィン.txt.toml
```toml
[script]
"3267" = "（Chụt——rộp——liếm——chụt）"
```

# ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml
```toml
[script]
"987" = "「Chụt——ưm——rộp——chụụt——liếm láp,\\nchu mút——trượt——chụụụt」"
```

# ハチロクh5_おだいどこしごと.txt.toml
```toml
[script]
"1743" = "（Liếm——rộp——mút——ực）"
```

# ハチロクh7_レトロモダンメイクラヴ.txt.toml
```toml
[script]
"791" = "「A……ưm……chụt——chụm——ưm——\\nFu——a……liếm——rộp——chụt——chụt」"
"793" = "「A……ưm——ưm——ưm……chụt……rộp——\\nưm——chụt——chùn chụt——rộp——liếm」"
"810" = "「Chụt——ưm……chụt——rộp——rộp——\\nưm!? Ực——liếm——rộp——chụt」"
"1878" = "（Liếm——rộp——Rerooooo——ngoạm!）"
"1944" = "（Liếm——liếm——rộp——liếm）"
```

# ポーレットh1_ファーストセックス.txt.toml
```toml
[script]
"1010" = "「Chụt——chùn chụt——ưm——\\nliếm——rộp——chùn chụt——ực.」"
"1012" = "「Ngoạm——rộp——liếm——chụt——\\nchụt——chùn chụt——chuút——ực.」"
"1016" = "「Chụt——chùn chụt——liếm——rộộộộp——」"
"1019" = "「Ưm——phù——ưm——liếm——rộp——\\nưm——chụt——chùn chụt——chuzooooo.」"
```

# ポーレットh2_制服変更？.txt.toml
```toml
[script]
"1639" = "（Chuúúúút——ực——liếm——rộp——）"
```

# ポーレットh3_誘惑アイスコーヒー.txt.toml
```toml
[script]
"933" = "「Ngoạm——ưm——chubu——chụt——\\nliếm——rộp——liếm——chụụụt」"
"942" = "「Ngoạm——ưm——ưm～～\\nrộp, liếm——chumu——chụụt」"
```

# ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml
```toml
[script]
"938" = "「Ưm ưm——chụt——ngoạm——chụt——liếm, liếm——rộộp——liếmmmm——」"
"942" = "「Ưm……chụt——chumu——chụtttt——chụt ——Phù, a——ưm——liếm——rộp——liếmmmm」"
"1696" = "（Liếm! Rộp! Liếmmmm! Trơn tuộtttttt——）"
"1726" = "（Lách tách——nhóp nhép——nhóp nhép——rộp——）"
```

# ポーレットh6_あなたとふたりの学園エッチ.txt.toml
```toml
[script]
"828" = "「Ngoạm——ưm——chụt——chụtttt——\\nliếm——rộp——sụt——ngoạm!」"
"856" = "「Ưm……chụt……chụt……chụt……phù—— Ưm——chụt——chụt——liếm——rộp——」"
```

# ポーレットh7_残業エッチもyシャツで.txt.toml
```toml
[script]
"872" = "「Anmu——ưm——chụt——chụt—— chụt——rộp——rộộp——chụt!」"
"911" = "「Ưm……chụt——liếm, rộp——ưm……\\nrộp……rộp——liếm——rộp!」"
"1675" = "（Trượt! Nắn! Rộp! Phập!）"
"1690" = "（Rột! Liếm! Rột! Ưm——rộộp!）"
"1692" = "（Rộộộộộp）"
"1672" = "（Thọc——phập——tuột——phụt!）"
"1684" = "（Phậpppppppp!）"
"1700" = "（Phậpppppppppppp! Cộp!!!）"
"1701" = "（Phậppppppppp!）"
```

# 凪h1_ふたりっきりのデート.txt.toml
```toml
[script]
"1118" = "「Ưm……Chụt——Chụt——Chụt——Chụt——\\nChụt——Rộp——Chụt——Chụt——Pua」"
```

# 凪ふかみh1_修学旅行の夜.txt.toml
```toml
[script]
"1237" = "「Fa——a——chụt——ưm——\\nrột——liếm——rộp——liếm——」"
"1289" = "「Rộp——liếm——chụt——rột——\\nchụt——liếm——rộộp——liếm——phù」"
"1290" = "「Rộp——chụt——liếm——liếm——chụt,\\nchụt, chu——liếm——liếm——liếm!」"
"1291" = "「Rộp——chụt——chụt——ưm——c-cứ\\n——thấy sướng là được——phù——ạ——nhỉ?」"
"1294" = "「Rộp——chụt——ưm!? Oa, Fukami!\\nPhần đầu của anh hai, đang phồng lên kìa!」"
"1301" = "「Ưm... chụt——rộp——liếm——mút——\\nchụt——chụt——liếm——rột——liếm」"
```

# 凪ふかみh2_みずあそび.txt.toml
```toml
[script]
"1030" = "「...Liếm... rộp——phù——ưm——liếm——\\nliếm——rộộp——liếm——Rerooooo」"
"1346" = "「Emu——rộp——rộp——liếm」"
"1357" = "「Rộp——liếm——mút——mút」"
"1374" = "「Eu——ưm——chụt... chụt——rột——\\nưm... liếm——rộp——chu——chụt」"
"1428" = "「Ngón tay của bé Nagi——ưm——ngon quá——Hyo... ưm,\\nchụt——chu——liếm——rộộộp」"
```

# 日々姫h1_マッサージの続き.txt.toml
```toml
[script]
"1055" = "「Chụt——Rộp——Chụt——Chụt——」"
"1056" = "「Ngoạm——Ư——Rộp——Liếm——Mút.」"
"1061" = "「Ưm——Ưm——Chụt——Ưm——Ưm——Rộp——Chụt chụt——Ưm——Ngoạm.」"
"1065" = "「Nfu——Chụt——Liếm——Chụt——Liếm——Liếm liếm——rộộộộp————Ngoạm!」"
"1873" = "（Chụt! Rộộộộộộp!）"
"1905" = "（Chụt——Ngoạm——Liếm——Rộp）"
```

# 日々姫h3_汚れてしまった制服で.txt.toml
```toml
[script]
"1793" = "（Rộp——Liếm——Chụt——Chụt）"
```

# 日々姫h4_いもうとタオル.txt.toml
```toml
[script]
"1024" = "「Chụt――ưm――rộp――chùn chụt――――\\n（Rắc!） Ư!!?」"
"1757" = "（Phậppppppppp!!!）"
```

# 日々姫h5_白濁絵の具の射精会.txt.toml
```toml
[script]
"1204" = "「Ngoạm――chụt――chụt――rộp――rộp――\\nLiếm liếm――ngoạm――phụt――ngoạm――ưm」"
"1221" = "「Chụt――chùn chụt――chụt――chụt――\\nRộp――liếm――rộộp! Trơn tuột!!」"
"1226" = "「Rót――rộộp――liếm――chụt! Chụt!\\nZuryuryuryuryu! Ưm――liếm――trơn tuột!」"
"1238" = "「Ưm――chụt――ưm――liếm――rộộộp.\\nLiếm――liếm――chụt――chùn chụt!」"
"1253" = "「Ưm……phụt――ưm! Chụt――zuju! Ực\\n――phù――ngoạm――liếm――rộp――koshun」"
```

# 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml
```toml
[script]
"2172" = "「Ngoạm――ưm――rộp――liếm――liếm\\n――liếm――chụt――ực」"
```

# 稀咲h1_性生活.txt.toml
```toml
[script]
"1297" = "「Ưm…… chụt――chu mu――a mu――\\nưm…… liếm――rộp――chụt――mút」"
```

# 稀咲h3_チャイナドレスでおもてなし.txt.toml
```toml
[script]
"2269" = "「Ưm……chụt――phu――chụt――chụt,\\nchụt――rero――Rộộp――chụt」"
"2816" = "「（Rộp――liếm――liếm）」"
"3816" = "（Rộp）"
"1988" = "「Không được! Chỗ đó! Vẫn chỗ đó――Kyafu!\\nĐầu em――chớp, chớp――hí――không xong, mất」"
```

# lr_ポーレットh2_デコレーション＆ミルク.txt.toml
```toml
[script]
"1770" = "（Phậppppppppppp――――kịch!!）"
```

# ハチロクh3_磨き洗い.txt.toml
```toml
[script]
"1835" = "（Phậppppppppppp!!!）"
```

## Kết bài

Đợt U13b áp 13 mục §1 OPEN đã quyết (T67–T81, trừ T76/T80 parked): **304 dòng sửa** trên 63 file — T75 71 dòng họ "chụt", T77 188 dòng họ "rộp" (205 dòng có token れる/るっ trong phụ lục 251 dòng), T78a 21 dòng "Phập", T78b 2 dòng "Rút", T68/T71/T72/T73/T74/T79 33 dòng thuật ngữ; T67/T69/T70/T81 0 dòng (đã đúng). **16 dòng GHÉP** với batch đã gộp (288 dòng mới). Lượt soát 2: **304/304 đọc lại, 299 đúng, 5 sửa** (1290, 1162, 1135, 1644, 934 — lỗi lệch chỉ số lượt 1), **0 loại**. Khối TOML 63 file / 304 key parse-verified, khớp JSON.

Còn nợ coordinator: 5 dòng T75 ngoài phạm vi (ちゅず/ちゅく/ちゅりゅ — 2031/1037/1652/2534/2357); ứng viên sót T75 trong phụ lục T77/T78 (ハチロクh2 1206, lr_日々姫h2 1039/1045, lr_稀咲ポーレットh1 1585/1821/1589, lr_れいなh1 1271, ハチロクh8 825, lr_れいなh1 1266 "Chụt mút"); 5 ứng viên sót T77 trong phụ lục T75 (lr_日々姫h2 1056 れるっ→"Reru", 真闇h3 2332 れる→"reru", lr_稀咲h1 1058 れるっ→"reru", lr_凪h1 1220 れるうううっ→"Reruuuu", 真闇h3 2336 るっ cuối chuỗi trượt 「ちゅる、るう、るっ」 — nhiều khả năng KHÔNG phải token licking); mơ hồ るっ ở lr_日々姫h2 1033 (đã xếp LICKING, kề ぶっ); chuẩn hoá chữ hoa/thường token romaji còn lại theo F5 (U15); mục mới U15: địa danh 帝央 — "Teio" (đa số ~15 dòng) vs "Teiou" (共通06 2112, ニイロク03 1570) vs "Trung tâm Hoàng gia" (仲国05 2032).
