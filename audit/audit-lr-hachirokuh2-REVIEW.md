# Audit: lr_ハチロクh2_新しい服。新しい旅.txt.toml (01_Hachiroku)

- File: `translation_toml/01_Hachiroku/lr_ハチロクh2_新しい服。新しい旅.txt.toml`
- TOML md5: `7b0a3c5d1db89046c9b50bee2ff0e6f5` — không có bản trùng (md5 duy nhất trong 227 file TOML).
- Đọc: **327/327 dòng script** (key 41–2210), đối chiếu từng dòng với JP + TW từ CSV3. CSV3 chỉ có 1 bộ cho file này (không có bộ stale). 173 lệch TOML/CSV3 đều chỉ là `\n` bị flatten thành khoảng trắng trong TOML-2 (CSV3 là chuẩn).
- **Sai: 63/327 (19,3%)**.
- Phân loại: xưng hô 22 (20 thuần + 2 gộp gasp) · thở gấp 29 chỗ (27 dòng riêng + 2 dòng gộp trong nhóm xưng hô) · tiếng cười 7 · sai nghĩa 3 · SFX 3 · thuật ngữ 1.
- Lệch vị trí: **0** · chuỗi xoay vòng: **0** · dòng mồ côi: **0** · chưa dịch: **0** (1113 chỉ là 「……」 cả 3 cột) · trùng key: **0** · thẻ %l: **0** trong file · `[selections]` rỗng.
- Cơ sở tổng: **114 file / 5.308 dòng sai** (xác minh từ ROUTE-AUDIT.md, dòng tổng cuối cùng). Sau file này: **115 file / 5.371 dòng sai**.

## §1. Xưng hô — Soutetsu tự xưng "anh" → "tôi" với Hachiroku (22 dòng)

Quy tắc đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi "ngài Soutetsu" 753× 双鉄様). File này thoại Soutetsu có 24 dòng xưng hô: 22 sai "anh", chỉ 2 đúng "tôi" (1364, 1579 — giữ). Độc thoại "tôi" đúng toàn bộ, không sửa. Thay bằng regex word-boundary để không chạm "thanh" (1402 "thanh khiết" nguyên vẹn).

- **1120** [双鉄] JP: 「――僕を焦かせて乾かして。お前が欲しいと抱きたいと。\nここまで熱く、昂ぶらせたのだ」 / Cũ: 「——Làm anh cháy bỏng, làm anh khao khát. Rằng anh muốn em, muốn ôm lấy em.\nĐã khiến anh nóng bỏng và hưng phấn đến nhường này.」 / Mới: 「——Làm tôi cháy bỏng, làm tôi khao khát. Rằng tôi muốn em, muốn ôm lấy em.\nĐã khiến tôi nóng bỏng và hưng phấn đến nhường này.」 (4× "anh" → "tôi")
- **1358** [双鉄] JP: 「たとえ壊れてしまっても――僕は必ず、お前を直す」 / Cũ: 「Cho dù có hỏng đi chăng nữa——anh nhất định, sẽ sửa lại cho em」 / Mới: 「Cho dù có hỏng đi chăng nữa——tôi nhất định, sẽ sửa lại cho em」
- **1361** [双鉄] JP: 「お前がだ、すず。ここから見上げたお前の体が。\nお前の熱が、あるはずもない体臭が――」 / Cũ: 「Là em đấy, Suzu. Cơ thể em khi anh ngước nhìn từ đây.\nSức nóng của em, và cả mùi cơ thể lẽ ra không tồn tại——」 / Mới: 「Là em đấy, Suzu. Cơ thể em khi tôi ngước nhìn từ đây.\nSức nóng của em, và cả mùi cơ thể lẽ ra không tồn tại——」 (dòng này quét máy bắt được — đọc tay đã sót)
- **1402** [双鉄] JP: 「お前のおまんまんは、はじめて目にしたときと同じく。\n極めて清楚な姿を今も、変わらず見せてくれるのだな」 / Cũ: 「Cô bé của em, vẫn giống hệt như lần đầu tiên anh nhìn thấy.\nVẫn cho anh thấy vẻ thanh khiết tột cùng không đổi thay」 / Mới: 「Cô bé của em, vẫn giống hệt như lần đầu tiên tôi nhìn thấy.\nVẫn cho tôi thấy vẻ thanh khiết tột cùng không đổi thay」 (dòng này quét máy bắt được — đọc tay đã sót)
- **1507** [双鉄] JP: 「ああ、わかっている。僕も一緒だ」 / Cũ: 「Aa, anh biết rồi. Anh cũng cùng em」 / Mới: 「Aa, tôi biết rồi. Tôi cũng cùng em」
- **1513** [双鉄] JP: 「お前という魂の、僕がもっとも愛するものの、\nその内面に調和した、これほど美しい器なのだから」 / Cũ: 「Linh hồn của em, thứ mà anh yêu thương nhất,\nđây là một vỏ bọc vô cùng xinh đẹp, hoàn toàn hài hòa với nội tâm đó.」 / Mới: 「Linh hồn của em, thứ mà tôi yêu thương nhất,\nđây là một vỏ bọc vô cùng xinh đẹp, hoàn toàn hài hòa với nội tâm đó.」
- **1516** [双鉄] JP: 「僕の目には、な。\n描き出されるごくごく微細な陰影さえも」 / Cũ: 「Trong mắt anh thì là vậy.\nNgay cả những bóng đen vô cùng nhỏ bé được vẽ ra.」 / Mới: 「Trong mắt tôi thì là vậy.\nNgay cả những bóng đen vô cùng nhỏ bé được vẽ ra.」
- **1539** [双鉄] JP: 「ああ、僕は勃起している」 / Cũ: 「Ừ, anh đang cương cứng.」 / Mới: 「Ừ, tôi đang cương cứng.」
- **1557** [双鉄] JP: 「僕もだ、すずっ。だから――っ！！！？」 / Cũ: 「Anh cũng vậy, Suzu. Thế nên——!!!?」 / Mới: 「Tôi cũng vậy, Suzu. Thế nên——Ư!!!?」 (gộp: xưng hô + gasp sweep)
- **1560** [双鉄] JP: 「僕もだ。お前が大好きだ」 / Cũ: 「Anh cũng vậy. Anh rất yêu em」 / Mới: 「Tôi cũng vậy. Tôi rất yêu em」
- **1566** [双鉄] JP: 「夫婦で、つれあいで、パートナーだもの。\nお前と共に、[おんな]同じように、ふたりで変化をしたいのだ」 / Cũ: 「Vì chúng ta là vợ chồng, là bạn đời, là đối tác.\nCùng với em, như một người phụ nữ, anh muốn cả hai cùng nhau thay đổi」 / Mới: 「Vì chúng ta là vợ chồng, là bạn đời, là đối tác.\nCùng với em, như một người phụ nữ, tôi muốn cả hai cùng nhau thay đổi」 ([おんな] ruby đã diễn đúng "như một người phụ nữ", giữ)
- **1574** [双鉄] JP: 「お前の性器。おまんまんがだ。\n幾度も幾度も、僕を受け入れすっかり僕の形になって」 / Cũ: 「Bộ phận sinh dục của em. Cô bé của em ấy.\nĐã đón nhận anh hết lần này đến lần khác và hoàn toàn mang hình dáng của anh」 / Mới: 「Bộ phận sinh dục của em. Cô bé của em ấy.\nĐã đón nhận tôi hết lần này đến lần khác và hoàn toàn mang hình dáng của tôi」
- **1578** [双鉄] JP: 「僕の望みは――常なる望みは――お前とともに――」 / Cũ: 「Mong muốn của anh là——mong muốn không bao giờ thay đổi là——cùng với em——」 / Mới: 「Mong muốn của tôi là——mong muốn không bao giờ thay đổi là——cùng với em——」
- **1595** [双鉄] JP: 「ならば、すず。僕の望みを、理解してくれ」 / Cũ: 「Nếu vậy, Suzu. Hãy hiểu mong muốn của anh」 / Mới: 「Nếu vậy, Suzu. Hãy hiểu mong muốn của tôi」
- **1599** [双鉄] JP: 「完全な大人の――おんなのものに、\n僕専用のおんなの性器に、その内側を変えたというのに」 / Cũ: 「Dù bên trong đã thay đổi thành của một người phụ nữ——trưởng thành hoàn toàn,\nthành bộ phận sinh dục nữ dành riêng cho anh」 / Mới: 「Dù bên trong đã thay đổi thành của một người phụ nữ——trưởng thành hoàn toàn,\nthành bộ phận sinh dục nữ dành riêng cho tôi」
- **1619** [双鉄] JP: 「だな。当然だ。\n僕とお前と、一緒に重ねる旅なのだから」 / Cũ: 「Nhỉ. Đương nhiên rồi.\nVì là chuyến đi mà anh và em, cùng nhau trải qua mà」 / Mới: 「Nhỉ. Đương nhiên rồi.\nVì là chuyến đi mà tôi và em, cùng nhau trải qua mà」
- **1623** [双鉄] JP: 「だが、見た目にだって、いつも僕は、\n蕩かされ魅了されているよ」 / Cũ: 「Nhưng mà, ngay cả vẻ bề ngoài, anh vẫn luôn,\nbị tan chảy và mê hoặc đấy.」 / Mới: 「Nhưng mà, ngay cả vẻ bề ngoài, tôi vẫn luôn,\nbị tan chảy và mê hoặc đấy.」
- **1624** [双鉄] JP: 「もちろん僕は、お前の体が――\n見た目以上に僕を蕩かすものだと深く、知っている」 / Cũ: 「Tất nhiên anh biết rất rõ, cơ thể của em——\nCòn làm anh tan chảy hơn cả vẻ bề ngoài của nó.」 / Mới: 「Tất nhiên tôi biết rất rõ, cơ thể của em——\nCòn làm tôi tan chảy hơn cả vẻ bề ngoài của nó.」
- **1648** [双鉄] JP: 「僕はこの部屋で、新しい経験を、旅を得た。\nお前もそうであったのならば――」 / Cũ: 「Anh đã có một trải nghiệm mới, một chuyến đi trong căn phòng này.\nNếu em cũng vậy thì——」 / Mới: 「Tôi đã có một trải nghiệm mới, một chuyến đi trong căn phòng này.\nNếu em cũng vậy thì——」
- **1669** [双鉄] JP: 「いますぐにここで――僕の上で流せばいい」 / Cũ: 「Ngay bây giờ ở đây——tắm trên người anh là được.」 / Mới: 「Ngay bây giờ ở đây——tắm trên người tôi là được.」
- **1671** [双鉄] JP: 「僕と同じだ」 / Cũ: 「Giống như anh thôi」 / Mới: 「Giống như tôi thôi」
- **1681** [双鉄] JP: 「す、ずっ。ダメだ。\n――このままだと、もうっ――っ！？」 / Cũ: 「Su, zu. Không được đâu.\n——Cứ thế này thì, anh——!?」 / Mới: 「Su, zu. Không được đâu.\n——Cứ thế này thì, tôi——Ư!?」 (gộp: xưng hô + gasp sweep)

## §2. Thở gấp — sweep (17) + mới (12)

Quy tắc áp dụng (quyết định 20/11 ~17:50, đã ghi MEMORY): っ trên từ âm thanh (ああ/はう/ひゃう/ゆぅん…) LÀ gasp, phải thêm Ư — không phải nhấn mạnh. Chỉ áp cho っ cuối tuyệt đối / đầu dòng (ranh giới theo tiền lệ lr_れいな追加h). Phán đoán "giữ あっ→'A', はうっ→'Hau'" của file lr_ふかみh1 ra trước quyết định này nên không áp nữa; 仲国01 đã sửa はうっ→"HaƯ" theo quyết định mới.

### 2a. Từ sweep — áp nguyên sau khi kiểm chứng với JP (17 mục)

- **1414** [双鉄] JP: 「っ」 / Cũ: 「っ」 / Mới: 「Ư」
- **1415** [双鉄] JP: 「っ！！！」 / Cũ: 「っ!!!」 / Mới: 「Ư!!!」
- **1416** [双鉄] JP: 「っ！！！！」 / Cũ: 「っ!!!!」 / Mới: 「Ư!!!!」
- **1417** [双鉄] JP: 「っ！？」 / Cũ: 「!?」 / Mới: 「Ư!?」
- **1418** [双鉄] JP: 「っ――あっ――すず、すずっ！」 / Cũ: 「っ——a——Suzu, Suzu!」 / Mới: 「Ư——a——Suzu, Suzu!」 (chỉ っ đầu dòng → Ư; あっ giữa dòng và すずっ tên người giữ)
- **1456** [双鉄] JP: 「っ！！！！」 / Cũ: 「っ!!!!」 / Mới: 「Ư!!!!」
- **1457** [双鉄] JP: 「っ！！！！！！」 / Cũ: 「っ!!!!!!」 / Mới: 「Ư!!!!!!」
- **1458** [双鉄] JP: 「っ！！！！！！！！」 / Cũ: 「っ!!!!!!!!」 / Mới: 「Ư!!!!!!!!」
- **1459** [双鉄] JP: 「っ！！！？」 / Cũ: 「!!!?」 / Mới: 「Ư!!!?」
- **1462** [双鉄] JP: 「ぁ――ぁっ――っ――」 / Cũ: 「A——a——っ——」 / Mới: 「A——a——Ư——」 (chỉ っ đầu đoạn cuối → Ư; ぁっ giữa dòng giữ)
- **1474** [ハチロク] JP: 「ぇ～～～～っ」 / Cũ: 「A~~~~」 / Mới: 「A~~~~Ư」
- **1483** [双鉄] JP: 「っ――！！！！」 / Cũ: 「っ——!!!!」 / Mới: 「Ư——!!!!」
- **1557** [双鉄] — xem §1 (gộp xưng hô).
- **1583** [ハチロク] JP: 「わらひっ！　もうっ――あうっ――限界、限界っ！\nっ――けど――いっしょ、いっしょに、ね、いっしょ」 / Cũ: 「Em! Không——a ư——giới hạn, giới hạn rồi!\nっ——nhưng mà——cùng, cùng nhau, nhé, cùng nhau」 / Mới: 「Em! Không——a ư——giới hạn, giới hạn rồi!\nƯ——nhưng mà——cùng, cùng nhau, nhé, cùng nhau」 (chỉ っ đầu dòng → Ư; っ giữa dòng và っ nhấn mạnh trên từ nội dung giữ)
- **1681** [双鉄] — xem §1 (gộp xưng hô).
- **2009** [monologue] JP: 「ひどく淫靡な仕草をけれど、\nあどけない笑顔で彩って――っ！！」 / Cũ: 「Một hành động vô cùng dâm đãng, nhưng lại được tô điểm bằng nụ cười ngây thơ——!!」 / Mới: 「Một hành động vô cùng dâm đãng, nhưng lại được tô điểm bằng nụ cười ngây thơ——Ư!!」
- **2109** [monologue] JP: 「すずの動きが単調になる。射精を促すそのためだけの――\nこんなにも直線的で単純で暴力的で動物的で機――っ！？」 / Cũ: 「Chuyển động của Suzu trở nên đơn điệu. Chỉ để thúc giục tôi xuất tinh——\nsự thẳng thừng, đơn giản, bạo lực, mang tính động vật và máy móc này——!?」 / Mới: 「Chuyển động của Suzu trở nên đơn điệu. Chỉ để thúc giục tôi xuất tinh——\nsự thẳng thừng, đơn giản, bạo lực, mang tính động vật và máy móc này——Ư!?」

### 2b. Mới — っ cuối tuyệt đối trên từ âm thanh mà sweep không bắt (12 dòng)

- **1105** [双鉄] JP: 「――あっ」 / TW: 「——啊」 / Cũ: 「——A」 / Mới: 「——AƯ」
- **1407** [ハチロク] JP: 「ひゃうっ！！！！」 / Cũ: 「Hya!!!!」 / Mới: 「HyauƯ!!!!」 (đồng thời sửa số nguyên âm: ひゃう có 1 う → 2 nguyên âm "Hyau" theo công thức 1+う; cách viết "Hyau" giữ theo tiền lệ lr_ふかみh1)
- **1408** [ハチロク] JP: 「ひゃうううっ！！！？」 / Cũ: 「Hyauuu!!!?」 / Mới: 「HyauuuƯ!!!?」 (số nguyên âm đã đúng 4 = 1+3)
- **1410** [ハチロク] JP: 「ひあっ！　んっ！　ふあっ！　ゆぅんっ！！！」 / Cũ: 「Hya! Ưm! Haa! Yuun!!!」 / Mới: 「Hya! Ưm! Haa! YuunƯ!!!」 (chỉ phần tử cuối ゆぅんっ → Ư; ひあっ giữ nguyên chờ quyết ひあ/ひゃ; んっ đã diễn "Ưm"; ふあっ cờ đợt thống nhất fa/fu)
- **1411** [ハチロク] JP: 「ひゃうっ！！！！」 / Cũ: 「Hya!!!!」 / Mới: 「HyauƯ!!!!」 (cùng JP với 1407 — VN trùng là đúng, không lệch dòng)
- **1429** [ハチロク] JP: 「ふあっ！　あっ！　あひっ！　あひゅっ！！！」 / Cũ: 「Haa! A! Ahi! Ahyu!!!」 / Mới: 「Haa! A! Ahi! AhyuƯ!!!」 (chỉ phần tử cuối あひゅっ → Ư; ふあっ cờ fa/fu; あっ/あひっ giữa dòng giữ)
- **1433** [ハチロク] JP: 「ふぁ！　あっ！　あっ！　あっ！！！」 / Cũ: 「Haa! A! A! A!!!」 / Mới: 「Haa! A! A! AƯ!!!」 (chỉ あっ cuối → Ư; ふぁ cờ fa/fu)
- **1463** [双鉄] JP: 「ぁ、ぁ、ぁ、あっ」 / Cũ: 「A, a, a, a」 / Mới: 「A, a, a, aƯ」 (chỉ あっ cuối chuỗi → Ư)
- **1470** [双鉄] JP: 「ぁぁぁぁぁあああっ」 / Cũ: 「Aaaaaa」 / Mới: 「AaaaaaƯ」 (độ dài あ giữ quy ước lỏng theo tiền lệ 仲国05; chỉ thêm Ư cho っ cuối)
- **1472** [ハチロク] JP: 「はうっ」 / TW: 「啊嗚」 / Cũ: 「Hau.」 / Mới: 「HauƯ.」 (はうっ là gasp theo quyết định 仲国05; tiền lệ 仲国01: はうっ→"HaƯ")
- **1486** [双鉄] JP: 「ん――くっ――ぁっ！」 / Cũ: 「Ưm——ư——a!」 / Mới: 「Ưm——ư——aƯ!」 (chỉ ぁっ cuối → Ư; くっ giữa dòng đã diễn "ư", giữ)
- **1527** [双鉄] JP: 「ああっ！」 / Cũ: 「Aa!」 / Mới: 「AaƯ!」 (ああっ là gasp theo quyết định 仲国05; phân biệt với 1471 「ぁぁあ！」→"Aa!" giữ — không có っ)

## §3. Tiếng cười diễn thành tiếng rên (7 dòng)

Quy tắc Hieu 19/11 22:05: ふふっ/うふふ/んふふ là TIẾNG CƯỜI, diễn thành tiếng cười, KHÔNG diễn thành tiếng rên ("Ư hừ"). Cả 7 dòng TW đều xác nhận là cười (嘻嘻/呵呵/嘿嘿).

- **1423** [ハチロク] JP: 「んふふっ」 / TW: 「呵呵」 / Cũ: 「Ưm hừm」 / Mới: 「Nfufu」
- **1424** [ハチロク] JP: 「ふぁ――あ……あ……ん――。\nふっ――うふっ――うふふふふっ」 / TW: 「呼啊……啊……啊……嗯……呼……嘿嘿……哎嘿嘿」 / Cũ: 「Haa——a……a……ưm——.\nHư——ư hừ——ư hừ hừ hừ」 / Mới: 「Haa——a……a……ưm——.\nHư——Ufu——Ufufufufu」 (ふっ giữ "Hư" — hơi thở, không phải cười; ふぁ cờ fa/fu)
- **1447** [ハチロク] JP: 「まぁ、双鉄さまったら。けど――そうですね。ふふっ」 / TW: 「哎呀，您這麼說可真是……不過，的確是這個道理，嘻嘻」 / Cũ: 「Trời ạ, ngài Soutetsu thật là. Nhưng mà——đúng vậy nhỉ. Hừ hừ」 / Mới: 「Trời ạ, ngài Soutetsu thật là. Nhưng mà——đúng vậy nhỉ. Fufu」
- **1508** [ハチロク] JP: 「んふふっ。上手に飲めました」 / TW: 「嘻嘻，我都喝乾淨了」 / Cũ: 「Ưm hừm. Em uống ngoan chứ」 / Mới: 「Nfufu. Em uống ngoan chứ」
- **1511** [ハチロク] JP: 「うふふっ、当然でございましょう？　だってふたりの。\n双鉄さまとわたくしの、旅なのですから」 / TW: 「嘻嘻，這不是理所當然的嘛，畢竟這可是只屬於我們的旅程」 / Cũ: 「Ư hừ hừ, đương nhiên rồi ạ? Vì là của hai người mà.\nVì là chuyến đi của ngài Soutetsu và em mà」 / Mới: 「Ufufu, đương nhiên rồi ạ? Vì là của hai người mà.\nVì là chuyến đi của ngài Soutetsu và em mà」
- **1547** [ハチロク] JP: 「ですよね、うふふっ」 / TW: 「您果然也是這樣認為，嘻嘻」 / Cũ: 「Đúng không ạ, ư hừ hừ」 / Mới: 「Đúng không ạ, Ufufu」
- **1606** [ハチロク] JP: 「はい。うふふっ。ですのでわたくし、このお洋服。\n昨日よりももっと気に入りました」 / TW: 「是的，嘻嘻，所以我現在相比昨天，更加喜愛這身衣服了」 / Cũ: 「Vâng. Ư hừ hừ. Thế nên em, bộ quần áo này.\nEm thích nó hơn ngày hôm qua rồi」 / Mới: 「Vâng. Ufufu. Thế nên em, bộ quần áo này.\nEm thích nó hơn ngày hôm qua rồi」

## §4. Sai nghĩa (3 dòng)

- **1436** [ハチロク] JP: 「ふあっ！　あっ！　ひもひひっ――そうへふ、はまっ！\nんっ！　わらくっ、わたくしっ、これ、しゅごっ――！」 / TW: 「呼啊！啊！好酥胡……雙鐵，少爺！嗯！我，我……這樣，好厲害！」 / Cũ: 「Haa! A! Sướng quá——ngài Soutetsu, sâu quá!\nƯm! Của em, của em, cái này, sướng quá——!」 / Mới: 「Haa! A! Sướng quá——ngài Soutetsu!\nƯm! Em, em, cái này, sướng quá——!」 — (1) はまっ là さまっ nói ngọng (s→h, cùng mẫu そうへふ=そうてつ; TW chỉ có 雙鐵少爺, không có "sâu") nên "sâu quá" là bịa — gỡ. (2) わらくっ = わたくし nói ngọng ("tôi/em"), không phải sở hữu — "Của em" sai → "Em" (TW: 我，我).
- **1593** [ハチロク] JP: 「次にはどんなお洋服で、どんな新しい旅をしたいと。\nね？　双鉄さま。今、お考えになられてますか？」 / TW: 「等到下一次，您又想看到我身著什麼樣的衣服，與我共度怎樣的全新旅途呢？」 / Cũ: 「Lần tới ngài muốn mặc bộ quần áo nào, và muốn có chuyến đi mới như thế nào.\nNhỉ? Ngài Soutetsu. Ngài đang nghĩ gì vậy?」 / Mới: 「Lần tới ngài muốn em mặc bộ quần áo nào, và muốn có chuyến đi mới như thế nào.\nNhỉ? Ngài Soutetsu. Ngài đang nghĩ gì vậy?」 — Chủ ngữ sai: TW nói rõ là quần áo ngài muốn thấy EM mặc, không phải ngài mặc.
- **1836** [monologue] JP: 「このままお仕置きして欲しい――強く望みもするけれど、\n誤解を抱えられたまま、すずとの愛を交わしたく無い。」 / TW: 「儘管我心頭也萌生出一種衝動——渴望任鈴處置的衝動」 / Cũ: 「（Mặc dù tôi cũng rất muốn cứ thế này mà trừng phạt em ấy——\nnhưng tôi không muốn ân ái với Suzu trong khi em ấy vẫn còn hiểu lầm.）」 / Mới: 「Mặc dù tôi cũng rất muốn cứ thế này mà được em ấy trừng phạt——\nnhưng tôi không muốn ân ái với Suzu trong khi em ấy vẫn còn hiểu lầm.」 — お仕置きして欲しい = muốn ĐƯỢC trừng phạt (ngược hướng); TW 任鈴處置 xác nhận. Đồng thời gỡ cặp ngoặc （ ） do dịch giả tự thêm (JP không có; đây là dòng duy nhất trong file có ngoặc tự thêm).

## §5. SFX (3 dòng)

- **1714** [ハチロク] JP: 「（ぐぽおおおおおおっ）――ん……んっ！」 / TW: 「（含住）嗯……嗯！」 / Cũ: 「（Ngậm lấy）——ưm……ưm!」 / Mới: 「（Gupoooooooo）——ưm……ưm!」 — ぐぽ là tiếng nuốt/ực, toàn dự án đều diễn thành âm thanh ("Gupo!", "Ục!!", "Ực!"), không diễn thành động tác; VN cũ theo TW mà mất âm. 8 nguyên âm o = 1+7 theo công thức độ dài.
- **1716** [ハチロク] JP: 「（ぬとおおおっ――れるっ――じゅるるるるっ）\nじゅぶっ！　ぼちゅっ！　じゅぶっ！　じゅばっ！」 / Cũ: 「（Liếm——liếm——liếm）\nChụt! Phụt! Chụt! Phụt!」 / Mới: 「（Nụtọooo——liếm——Chùn chụt）\nChụt! Phụt! Chụt! Phụt!」 — ぬと (dính) diễn thành âm "Nụtọooo" (4 o = 1+3); れる giữ "liếm" theo tiền lệ lr追加_みくろ＆日々姫h 2069; じゅるるるるっ → "Chùn chụt" theo tiền lệ 日々姫h3 1794/1796/1802.
- **1718** [ハチロク] JP: 「へふかは――へ？　……んふっ。\nじゅぶううっ！　じゅぶっ！　じゅぼっ！　じゅぶっ！」 / TW: 「ｓｕｏｙｉｓｈｕｏ……嗯嗚、啾溜！啾噗！啾啪！啾啪！」 / Cũ: 「Vì thế……ưm.\nChụt! Chụt! Chụt! Chụt!」 / Mới: 「Vì thế……ưm.\nChụụụt! Chụt! Chụt! Chụt!」 — じゅぶううっ có 2 う → 3 nguyên âm theo công thức (tiền lệ file khác: じゅぶううううっ→"Phậậậậập" 5 nguyên âm); chỉ sửa token đầu, 3 token sau không có う nên giữ "Chụt!".

## §6. Thuật ngữ (1 dòng)

- **1440** [ハチロク] JP: 「ふぁっ！　あらま、タブレット、ぜんぶ、おかひく――\nまっひろになるっ、んっ！　チカチカって、しへっ」 / Cũ: 「Haa! Chết mất, Tablet, kỳ lạ hết rồi——\nTrắng xóa mất, ưm! Chớp nháy, liên tục」 / Mới: 「Haa! Chết mất, máy tính bảng, kỳ lạ hết rồi——\nTrắng xóa mất, ưm! Chớp nháy, liên tục」 — タブレット = "máy tính bảng" (thuật ngữ đã chốt; 仲国01 đã sửa gloss タブレット → "máy tính bảng"). Toàn dự án còn 17 dòng "Tablet" vs 21 "máy tính bảng" — ghi chú cho đợt thống nhất. (ふぁっ → "Haa!" cờ fa/fu, không sửa ở đây.)

## §7. Kiểm chứng sweep cho file này (20 mục)

- Áp nguyên 17 mục (1414, 1415, 1416, 1417, 1418, 1456, 1457, 1458, 1459, 1462, 1474, 1483, 1557, 1583, 1681, 2009, 2109) — đã kiểm chứng từng giá trị với JP; 1557/1681 gộp thêm sửa xưng hô (xem §1).
- **1104** already-rendered — giữ: JP 「――っ」 → VN 「——Ưm」 đã diễn gasp, không sửa.
- **1720** needs-file-audit — GIẢI QUYẾT, không sửa: JP 「～～～～～～～～っ」 (8 ~ + っ), VN 「~~~~~~~~ưm」 (8 ~ + "ưm") — không lệch dòng (JP/VN khớp), っ cuối đã diễn bằng "ưm" mềm.
- **2103** needs-file-audit — GIẢI QUYẾT, không sửa: JP 2 dòng, VN 2 dòng khớp nhau, không lệch; っ cuối 「――っ。」 diễn bằng "ư" mềm (cùng nguyên âm với "Ư", chỉ khác hoa/thường). Giữ nguyên.

## §8. Giữ nguyên có chủ đích

- **1121** [ハチロク] あなた → "anh": giữ. あなた là cách gọi thân mật ("với anh"), phân biệt với 双鉄様 = "ngài Soutetsu" trong cùng dòng; quy tắc xưng hô chỉ quản Soutetsu tự xưng, không quản Hachiroku gọi Soutetsu.
- **1112** JP nói ngọng/mồm đầy, TW là pinyin giải mã ("cứ thế bắn vào trong miệng em đi") — VN theo TW, giữ.
- **1320/1677–1680/1482** すずっ → "Suzu": giữ — っ trên tên riêng là nhấn mạnh, không phải gasp.
- **1104/1326/1452/1484/1490/1491/1498/1501/1541** んっ/くっ → "Ưm"/"ư": giữ — đã diễn bằng cách khác.
- **1905/2056** ふーっ/ふーーーーっ → "Phù——": giữ — hơi thở đã diễn, dấu —— đánh dấu ngắt; sweep cũng không cờ.
- **1495/1496** số nguyên âm ĐÃ ĐÚNG theo công thức khi tính cả "Ưm": 1495 んふううううううっ (7 う) → "Ưm huuuuuuu" = Ư(1)+7u = 8 = 1+7 ✓; 1496 んひゅうううううううっ (7 う) → "Ưm hyuuuuuuu" = 8 ✓. Không sửa.
- **1477** じゅぶううううううっ → "Chụtttttt": giữ — phong cách lặp phụ âm, 6 t = 6 う, đúng trong phong cách của nó (tiền lệ lr_ふかみh1 giữ phong cách lặp, không sửa theo công thức đếm âm).
- **2202/2209** （きゅうううううううっっ）/（ぐりゅうううううううっ） → "（Siết chặtttttt）": giữ — SFX ướt dài trong độc thoại ngoặc đơn, giữ phong cách lặp phụ âm theo tiền lệ lr_ふかみh1 (1919–1965); không sửa theo công thức.
- **2166–2210** SFX độc thoại ngoặc đơn diễn đồng nhất "Phập/Phụt/Chụt": giữ — quy ước của file cho nhóm SFX này (JP các dòng đều là âm thúc/đâm tương tự; VN trùng nhau không phải lệch dòng — đã kiểm tra từng JP).
- **1432** "Nóng quá! Thật nhiều, của ngài, Soutetsu!": giữ — JP không nói rõ 精液, TW thêm vào; VN giữ mức ám chỉ như JP.
- **1548** thứ tự mảnh câu đảo ("Với, cô bé, của em, của em"): giữ — JP cũng rời rạc, đủ nghĩa ("dương vật ngài Soutetsu với cô bé của em").
- **1604** "Là để đón nhận……": giữ — TW 是為了 ủng hộ; JP là mảnh câu kết bằng を, VN thêm liên từ nhẹ theo TW, không thêm sự kiện mới.
- **2101** "phong ấn——sealing": giữ — JP dùng katakana シーリング làm gloss cho 封印; VN giữ nguyên từ tiếng Anh như JP (không phải thẻ %l — file này 0 thẻ %l).
- **1427** marker giọng [マイ・マスター,4] bỏ qua: đúng lệ toàn dự án (marker giọng nói đều bỏ).
- **1958** "tâm trí" cho 芯まで: giữ — lệch sắc thái nhẹ, nghĩa cảnh không đổi.
- **1470/1471** độ dài あ: giữ — quy ước lỏng cho あ (tiền lệ 仲国05: mỗi nhóm ああ → "A").
- **1460/1461** cùng VN "A——" cho JP khác nhau (ぁー…… / ぁあ――): giữ — cả hai đều là tiếng "A" dài.
- **1502** 「！！？」 → "!!?": giữ — JP chỉ có dấu câu, TW thêm 嗯 nhưng JP thắng TW.
- **1836** đã sửa ở §4; các độc thoại còn lại đọc kỹ đều đúng.

## §9. Chờ Hieu (không tự quyết)

1. **Fa/fu — đợt thống nhất (14 dòng)**: 1410, 1424, 1425, 1427, 1428, 1429, 1432, 1433, 1434, 1436, 1438, 1440, 1442, 1443 — ふぁ/ふあ đều diễn "Haa/Haaaa" (la-tinh hoá). Quy tắc đã chốt ふぁ→"phà", ふあ→"phùa"; áp dụng cùng đợt với ハチロクh6 (14 dòng) + lr_ふかみh2. (1112 không tính — lời ngọng, không phải SFX.)
2. **Mâu thuẫn ひあ/ひゃ toàn dự án**: 1410 ひあっ→"Hya!" giữ nguyên chờ quyết chung ("Hya" vs "Hia" vs "Á"). 1407/1408/1411 ひゃう giữ "Hyau" theo tiền lệ lr_ふかみh1; chỉ sửa số nguyên âm + thêm Ư.
3. **Ranh giới gasp giữa dòng**: audit chỉ thêm Ư cho っ cuối tuyệt đối/đầu dòng (tiền lệ lr_れいな追加h + quyết định 仲国05). Còn ~11 dòng / ~25 token っ giữa dòng trên từ âm thanh mà VN không diễn bằng Ư (chủ yếu あっ/ふぁっ trong chuỗi rên 1410–1443: 1427, 1432, 1433, 1434, 1436, 1438, 1442 + 1473 ぁうっ + 1410/1429) — nếu Hieu muốn "không để mất âm" tuyệt đối thì sửa thêm. Phần lớn nằm trong các dòng fa/fu đã cờ ở mục 1, nên đợt thống nhất là chỗ tự nhiên để chốt luôn.
4. **Hibiki 03 key 2360 mâu thuẫn tiền lệ**: file đó sửa ふふっ "Fufu" → "Ư hự" (diễn cười thành rên), ngược quy tắc Hieu + TW ở file này (7 dòng §3 đều có TW 嘻嘻/呵呵/嘿嘿 ủng hộ cười). Audit file này theo quy tắc Hieu; cần Hieu xác nhận 2360 có phải ngoại lệ theo ngữ cảnh không.
5. **"Tablet" còn 17 dòng toàn dự án** (vs 21 "máy tính bảng") — file này sửa 1 dòng 1440 theo thuật ngữ đã chốt; 16 dòng còn lại chờ đợt thống nhất.
6. **1121** "anh" cho あなた — giữ (xem §8); nếu Hieu muốn Hachiroku chỉ dùng "ngài Soutetsu" tuyệt đối thì báo lại.

## §10. Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 63 giá trị fix đối chiếu JP (+TW) lần 2, sau khi ráp JSON/TOML: **tổng 63 / kiểm chứng lại 63 / gỡ bỏ 0 / sửa lại 0**. Không có fix nào bị gỡ hay sửa trong lượt 2. (Quét máy đã bắt thêm 2 dòng xưng hô 1361/1402 mà đọc tay lượt 1 sót — đã đưa vào trước lượt 2.)

## §11. Kiểm chứng kỹ thuật

- JSON: 63 mục, dạng chuẩn list-of-dicts, key chuỗi, đủ 7 trường (key/jp/tw/old_vn/fix/kind/character); jp/tw/old_vn khớp CSV3 63/63 (lấy trực tiếp từ CSV3, fix ráp bằng thay thế có kiểm đếm).
- Diff-sanity: mọi fix chỉ khác old_vn ở đúng chỗ sửa (kiểm bằng difflib — xem log build); không có viết lại toàn dòng ngoài chỗ sửa, trừ 1836 (đổi hướng + gỡ ngoặc) và 1716 (3 token SFX).
- Khối TOML: parse được (tomllib), 63 key, **0 sai lệch giá trị** so với JSON.
- Không sửa ROUTE-AUDIT.md, không gửi file cho Hieu.

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
1105 = "「——AƯ」"
1120 = "「——Làm tôi cháy bỏng, làm tôi khao khát. Rằng tôi muốn em, muốn ôm lấy em.\\nĐã khiến tôi nóng bỏng và hưng phấn đến nhường này.」"
1358 = "「Cho dù có hỏng đi chăng nữa——tôi nhất định, sẽ sửa lại cho em」"
1361 = "「Là em đấy, Suzu. Cơ thể em khi tôi ngước nhìn từ đây.\\nSức nóng của em, và cả mùi cơ thể lẽ ra không tồn tại——」"
1402 = "「Cô bé của em, vẫn giống hệt như lần đầu tiên tôi nhìn thấy.\\nVẫn cho tôi thấy vẻ thanh khiết tột cùng không đổi thay」"
1407 = "「HyauƯ!!!!」"
1408 = "「HyauuuƯ!!!?」"
1410 = "「Hya! Ưm! Haa! YuunƯ!!!」"
1411 = "「HyauƯ!!!!」"
1414 = "「Ư」"
1415 = "「Ư!!!」"
1416 = "「Ư!!!!」"
1417 = "「Ư!?」"
1418 = "「Ư——a——Suzu, Suzu!」"
1423 = "「Nfufu」"
1424 = "「Haa——a……a……ưm——.\\nHư——Ufu——Ufufufufu」"
1429 = "「Haa! A! Ahi! AhyuƯ!!!」"
1433 = "「Haa! A! A! AƯ!!!」"
1436 = "「Haa! A! Sướng quá——ngài Soutetsu!\\nƯm! Em, em, cái này, sướng quá——!」"
1440 = "「Haa! Chết mất, máy tính bảng, kỳ lạ hết rồi——\\nTrắng xóa mất, ưm! Chớp nháy, liên tục」"
1447 = "「Trời ạ, ngài Soutetsu thật là. Nhưng mà——đúng vậy nhỉ. Fufu」"
1456 = "「Ư!!!!」"
1457 = "「Ư!!!!!!」"
1458 = "「Ư!!!!!!!!」"
1459 = "「Ư!!!?」"
1462 = "「A——a——Ư——」"
1463 = "「A, a, a, aƯ」"
1470 = "「AaaaaaƯ」"
1472 = "「HauƯ.」"
1474 = "「A~~~~Ư」"
1483 = "「Ư——!!!!」"
1486 = "「Ưm——ư——aƯ!」"
1507 = "「Aa, tôi biết rồi. Tôi cũng cùng em」"
1508 = "「Nfufu. Em uống ngoan chứ」"
1511 = "「Ufufu, đương nhiên rồi ạ? Vì là của hai người mà.\\nVì là chuyến đi của ngài Soutetsu và em mà」"
1513 = "「Linh hồn của em, thứ mà tôi yêu thương nhất,\\nđây là một vỏ bọc vô cùng xinh đẹp, hoàn toàn hài hòa với nội tâm đó.」"
1516 = "「Trong mắt tôi thì là vậy.\\nNgay cả những bóng đen vô cùng nhỏ bé được vẽ ra.」"
1527 = "「AaƯ!」"
1539 = "「Ừ, tôi đang cương cứng.」"
1547 = "「Đúng không ạ, Ufufu」"
1557 = "「Tôi cũng vậy, Suzu. Thế nên——Ư!!!?」"
1560 = "「Tôi cũng vậy. Tôi rất yêu em」"
1566 = "「Vì chúng ta là vợ chồng, là bạn đời, là đối tác.\\nCùng với em, như một người phụ nữ, tôi muốn cả hai cùng nhau thay đổi」"
1574 = "「Bộ phận sinh dục của em. Cô bé của em ấy.\\nĐã đón nhận tôi hết lần này đến lần khác và hoàn toàn mang hình dáng của tôi」"
1578 = "「Mong muốn của tôi là——mong muốn không bao giờ thay đổi là——cùng với em——」"
1583 = "「Em! Không——a ư——giới hạn, giới hạn rồi!\\nƯ——nhưng mà——cùng, cùng nhau, nhé, cùng nhau」"
1593 = "「Lần tới ngài muốn em mặc bộ quần áo nào, và muốn có chuyến đi mới như thế nào.\\nNhỉ? Ngài Soutetsu. Ngài đang nghĩ gì vậy?」"
1595 = "「Nếu vậy, Suzu. Hãy hiểu mong muốn của tôi」"
1599 = "「Dù bên trong đã thay đổi thành của một người phụ nữ——trưởng thành hoàn toàn,\\nthành bộ phận sinh dục nữ dành riêng cho tôi」"
1606 = "「Vâng. Ufufu. Thế nên em, bộ quần áo này.\\nEm thích nó hơn ngày hôm qua rồi」"
1619 = "「Nhỉ. Đương nhiên rồi.\\nVì là chuyến đi mà tôi và em, cùng nhau trải qua mà」"
1623 = "「Nhưng mà, ngay cả vẻ bề ngoài, tôi vẫn luôn,\\nbị tan chảy và mê hoặc đấy.」"
1624 = "「Tất nhiên tôi biết rất rõ, cơ thể của em——\\nCòn làm tôi tan chảy hơn cả vẻ bề ngoài của nó.」"
1648 = "「Tôi đã có một trải nghiệm mới, một chuyến đi trong căn phòng này.\\nNếu em cũng vậy thì——」"
1669 = "「Ngay bây giờ ở đây——tắm trên người tôi là được.」"
1671 = "「Giống như tôi thôi」"
1681 = "「Su, zu. Không được đâu.\\n——Cứ thế này thì, tôi——Ư!?」"
1714 = "「（Gupoooooooo）——ưm……ưm!」"
1716 = "「（Nụtọooo——liếm——Chùn chụt）\\nChụt! Phụt! Chụt! Phụt!」"
1718 = "「Vì thế……ưm.\\nChụụụt! Chụt! Chụt! Chụt!」"
1836 = "Mặc dù tôi cũng rất muốn cứ thế này mà được em ấy trừng phạt——\\nnhưng tôi không muốn ân ái với Suzu trong khi em ấy vẫn còn hiểu lầm."
2009 = "Một hành động vô cùng dâm đãng, nhưng lại được tô điểm bằng nụ cười ngây thơ——Ư!!"
2109 = "Chuyển động của Suzu trở nên đơn điệu. Chỉ để thúc giục tôi xuất tinh——\\nsự thẳng thừng, đơn giản, bạo lực, mang tính động vật và máy móc này——Ư!?"
```

## Kết bài

File lr_ハチロクh2_新しい服。新しい旅 — 327 dòng đọc hết, **63 dòng sai (19,3%)**. Lỗi lớn nhất là xưng hô: Soutetsu tự xưng "anh" 22/24 dòng thoại với Hachiroku (chỉ 2 dòng "tôi" đúng sẵn) — đúng mẫu các file Hachiroku khác. Tiếp theo là thở gấp 29 chỗ (17 từ sweep + 12 mới theo quyết định 仲国05) và 7 tiếng cười bị diễn thành rên. Không lệch vị trí, không xoay vòng, không dòng mồ côi, không dòng chưa dịch. Sweep kiểm chứng xong: 17 áp nguyên, 3 mục còn lại đã diễn rồi (1104, 1720, 2103). Còn chờ Hieu: đợt thống nhất fa/fu (14 dòng) + ひあ/ひゃ, ranh giới gasp giữa dòng (~11 dòng), và mâu thuẫn tiền lệ Hibiki 03 key 2360.
