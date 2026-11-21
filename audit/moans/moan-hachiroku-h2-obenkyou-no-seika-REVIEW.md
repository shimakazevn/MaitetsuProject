# Moan-fix review — ハチロクh2_お勉強の成果.txt.toml

## 1. Xác minh file

- File: `ハチロクh2_お勉強の成果.txt.toml` — route 01_Hachiroku, 312 dòng script. Nội dung: cảnh H của Hachiroku (Suzu) — "bài học" thực hành: oral, quan hệ lần đầu trong tư thế mới, xuất tinh trong; xen kẽ trò chuyện về cảm giác đau/lần đầu và lời hứa "vợ chồng".
- TOML md5 `76334dd708ac74656eebf9f65c140e97` (khớp md5 audit), 1 bản duy nhất, BOM+CRLF, `[selections]` rỗng, 0 tag `%l`.
- CSV3: 1 bộ duy nhất, 312/312 key khớp TOML, 0 key trùng, 0 VN trống.
- Audit đã merge: 46/312 sai (14,7%) — trong đó 8 dòng moan/SFX (1053, 1055, 964, 973, 974, 1045, 972, 1148) + 13 gasp Ư (sweep 8 + sweep bỏ sót 3 + tên+っ 2 + 1 gộp trong 1112). Xem §6 về kiểm chứng lại các dòng moan của audit.
- Sweep gasp: 9 mục cho file này (1083, 1112, 1156, 1201, 1565, 717, 721, 976, 987) — tất cả đã áp qua audit, không đụng lại ở đây.

## 2. Kho rên (đọc 312/312 dòng)

Quét máy theo mẫu rên/SFX tìm được 120 dòng ứng viên; đã xét từng dòng. Đổi 27 dòng, giữ 93 dòng.

- Họ fa/fu (ふぁ/ふあ/ふぇ/ふや/ぷあ): 12 dòng (10 dòng quét máy: 1004, 1038, 1014, 1003, 973, 974, 1001, 1006, 976, 996 — cộng 1011/1036 có ふ，ngăn cách bằng 、) — 1014 là lời nói ngọng (không phải dòng rên, giữ giá trị audit).
- Họ ひゃ/ひゅ/ひあ/きゃ/きゅ: 11 dòng (1109, 968, 1055, 1734, 965, 1729, 966, 1053, 1733, 1519, 964) — 1109/1734/1733/1519/1729 là SFX hành động hoặc trích dẫn trong văn xuôi, giữ.
- やっ/やあ: 3 dòng (961, 960, 1466) — 1466 là trần thuật ("Cuối cùng, khi cơn xuất tinh lắng xuống"), không phải rên.
- ん+X: 16 dòng (1136, 981, 1054, 1410, 1206, 1039, 1173, 1051, 1036, 1120, 1115, 1055, 993, 1053, 1056, 964).
- Chuỗi nguyên âm dài (≥3 cùng nguyên âm): 7 dòng (1206, 1038, 1019, 973, 1030, 1717, 964) — 1717 là SFX trong ngoặc, giữ theo quy ước file.
- Hôn/mút (ちゅ/じゅ/れる/れろ/ごく/こく): 35 dòng ứng viên (kể cả trần thuật) — chỉ đổi các token dài (1019, 1020, 1038, 1206), còn lại giữ quy ước "chụt/chu mút/liếm" của file cho token ngắn.
- Cười (ふふ/うふ/んふ): 4 dòng (1148, 972, 1051, 1036) — 1148/972 đã là "Ufufu" (audit), giữ.
- SFX trong （ ）: 36 dòng độc thoại — giữ nguyên hệ diễn theo nghĩa hành động (tiền lệ moan-fix h1/h8).
- Thán từ ngắn (あっ/はっ/うっ/んっ/えっ): 58 dòng ứng viên — hầu hết đã đúng ("A", "Ha", "Ưm"), chỉ đổi các dòng tách mảnh/mất âm trong §3.

## 3. Các dòng sửa (27)

Quy tắc áp dụng: rên một hơi mà bản VN tách thành nhiều mảnh rời ("Hya fư", "Hí u", "Hyu a", "Phù a") thì gộp lại thành MỘT cách diễn romaji, độ dài nguyên âm theo công thức (số nguyên âm = 1 + số う/ぅ; với あ lặp thì đếm số あ trong JP). Một dòng = một cách diễn (VN hoặc romaji, không trộn). Tiền lệ: ふかみh1 ("Hya ah ưm"→"Hyaaann", "Phù ah"→"Fua"), hachiroku-h7 (10 dòng fa/fu về romaji), paulette-h3 (ぅあっ→"Ua", ぷあっ→"Pua").

### 3.1 Romaji họ fa/fu — "phù a"/"Phù a" tách mảnh → romaji

#### 974 — ハチロク — romaji (thay thế giá trị audit ở đúng token này)
- JP: 「ふあっ――あっ――あんっ！　んっ――」
- TW: 「呼啊——啊——啊！嗯——」
- Cũ (CSV3): 「Phù a——a——a! Ưm——」 — giá trị audit: 「Phù a——a——an! Ưm——」
- Mới: 「Fua——a——an! Ưm——」
- Lý do: ふあっ là một âm duy nhất; "Phù a" tách thành hai từ Việt, nghe gượng (tiền lệ h7/fukamih1). Giữ "an" cho あんっ và "Ưm" của audit.

#### 976 — ハチロク — romaji (thay thế giá trị audit ở đúng token này)
- JP: 「ふあっ――すごっ――んっ――あっ――ああっ！\nくっ――来ますっ――まっしろなっ――おっきい、のっ」
- TW: 「呼啊——好厲害——啊——啊啊！嗯——來了——雪白——好大的」
- Cũ (CSV3): 「Phù a——tuyệt quá——ưm——a——a a!\nHự——đến đây——thứ gì đó trắng xóa——to lớnっ」 — giá trị audit chỉ đổi っ cuối thành Ư.
- Mới: 「Fua——tuyệt quá——ưm——a——a a!\nHự——đến đây——thứ gì đó trắng xóa——to lớnƯ」
- Lý do: ふあっ → "Fua" (như 974). Giữ "a a" cho ああっ (xem §4), "Hự" cho くっ (quy ước file, §4), Ư cuối dòng của audit.

#### 996 — ハチロク — romaji
- JP: 「あ……んっ――ふっ――ふあっ――」
- TW: 「啊……——呼——呼啊——」
- Cũ: 「A……ưm——phù——phù a——」
- Mới: 「A……ưm——Fu——Fua——」
- Lý do: chuỗi hơi んっ――ふっ――ふあっ―― trong cao trào; ふあっ → "Fua", ふっ trước nó cùng nhịp thở → "Fu" (một hệ romaji cho cả nhịp thở; tiền lệ paulette-h3/h9).

#### 1001 — ハチロク — romaji
- JP: 「あ……ふあっ――あっ――双鉄、様の、手……\nおっき、くっ、って――あったか、――く、て」
- TW: 「啊……呼啊——啊——雙鐵少爺的，手……好大——好溫暖——」
- Cũ: 「A……phù a——a——Bàn tay, của ngài Soutetsu……\nthật to, lớn——và thật, ấm, áp」
- Mới: 「A……Fua——a——Bàn tay, của ngài Soutetsu……\nthật to, lớn——và thật, ấm, áp」
- Lý do: ふあっ → "Fua" (như 974).

#### 1003 — ハチロク — romaji
- JP: 「あ……んっ――ごくんっ。ぷあ――あっ――\nあっ！？　そ、双鉄様、失礼しました」
- TW: 「啊……嗯——嗚嗯。噗啊——啊——啊！？雙鐵少爺，失禮了」
- Cũ: 「A……ưm——ực. Phù a——a——\nA!? Ngài, ngài Soutetsu, em thất lễ rồi」
- Mới: 「A……ưm——ực. Pua——a——\nA!? Ngài, ngài Soutetsu, em thất lễ rồi」
- Lý do: ぷあ―― → "Pua——" (romaji, phân biệt ぷ/ふ; tiền lệ paulette-h3). Giữ dấu —— sau Pua như JP.

#### 1004 — ハチロク — romaji
- JP: 「あ……ぷあっ」
- TW: 「啊……噗哈」
- Cũ: 「A……phù a」
- Mới: 「A……Pua」
- Lý do: ぷあっ = "pua" một âm; bản cũ vừa sai phụ âm (p → ph/f) vừa tách thành hai (tiền lệ paulette-h3).

#### 1006 — ハチロク — romaji
- JP: 「あ……ぷあっ……あ――キス――好き……」
- TW: 「啊……噗啊……啊——接吻——喜歡……」
- Cũ: 「A……phù a……a——Hôn——thích quá……」
- Mới: 「A……Pua……a——Hôn——thích quá……」
- Lý do: ぷあっ → "Pua" (như 1004).

#### 1011 — ハチロク — romaji
- JP: 「ああっ――わかる――わかりますっ！　子宮――\nおなか――んっ――あついの――ひろがって――ふ、あ」
- TW: 「啊啊——明白——我明白！子宮——肚子——嗯——熱熱的——好多——呼，啊」
- Cũ: 「A a——em hiểu——em hiểu rồi! Tử cung——\nbụng em——ưm——nóng quá——đang lan tỏa ra——phù, a」
- Mới: 「A a——em hiểu——em hiểu rồi! Tử cung——\nbụng em——ưm——nóng quá——đang lan tỏa ra——Fu, a」
- Lý do: ふ、あ → "Fu, a" (giữ dấu phẩy = giữ nhịp 2 nhịp của JP; tiền lệ ふかみh1 1223/1379/1458 "Fu, a"). Giữ "A a" cho ああっ (xem §4).

#### 1036 — ハチロク — romaji (2 token)
- JP: 「んっ――んふっ――ふ、あっ」
- TW: 「嗯——呼——呼，啊」
- Cũ: 「Ưm——ưm hưm——phù, a」
- Mới: 「Ưm——ưm fu——Fu, a」
- Lý do: んふっ → "ưm fu" (tiền lệ hachiroku-h1 1219/1229, kisaki-h3 2207: んふっ→"Ưm fu"; "hưm" sai phụ âm f→h); ふ、あっ → "Fu, a" (như 1011).

#### 1038 — ハチロク — romaji + đếm nguyên âm (2 token)
- JP: 「ん――ちゅっ――ちゅるっ――んっ――こくっ――\nぷあっ――んっ――じゅ――れろおおおっ」
- TW: 「嗯——啾——啾——嗯——嗚——噗哈——嗯——啾——（舔）」
- Cũ: 「Ưm——chụt——chu mút——ưm——ực——\nphù a——ưm——chụt——liếm」
- Mới: 「Ưm——chụt——chu mút——ưm——ực——\nPua——ưm——chụt——Reroooo」
- Lý do: ぷあっ → "Pua" (như 1004); れろおおおっ = れろ(1 o) + お×3 = 4 o → "Reroooo" (bản cũ "liếm" mất hẳn âm và độ dài; tiền lệ paulette-h3 れろおおおっ→"Reroooo", h9 2122 れろおおっ→"rerooo").

### 3.2 Romaji họ ひゃ/ひゅ/ひあ/きゃ + やっ — "Á"/tách mảnh mất phụ âm mora

#### 719 — 双鉄H — romaji
- JP: 「――ぅあっ」
- TW: 「——啊」
- Cũ: 「——ư a」
- Mới: 「——Ua」
- Lý do: ぅあっ → "Ua" (một âm; bản cũ "ư a" tách thành hai; tiền lệ paulette-h3 ぅあっ→"Ua", kisaki-h3 2197 ひあっ "I a"→"Hia").

#### 960 — ハチロク — romaji
- JP: 「やっ――っ――おっぱい……気持ち、いっ」
- TW: 「呀——乳房……好舒服」
- Cũ: 「Á——ư——ngực……sướng, quá」
- Mới: 「Ya——ư——ngực……sướng, quá」
- Lý do: やっ → "Ya" (や có phụ âm mora y; "Á" mất hẳn phụ âm y — tiền lệ ポーレットh3 "'Á' cho きゃっ/ひゃっ/やっ" là lỗi mất phụ âm, Hibiki h6 2082 やっ "a"→"Ya"). Giữ "ư" cho っ đứng riêng (âm đã được diễn, không mất — không thêm Ư).

#### 961 — ハチロク — romaji
- JP: 「やっ」
- TW: 「呀」
- Cũ: 「Á」
- Mới: 「Ya」
- Lý do: như 960.

#### 964 — ハチロク — romaji (thay thế giá trị audit ở đúng token này)
- JP: 「ひゅあっ！？\nんっ――んきゅううううううううううっ！！！」
- TW: 「呀啊！？嗯——嗯嗚嗚嗚嗚嗚嗚嗚嗚嗚！！！」
- Cũ (CSV3): 「Hyu a!?\nƯm——ưm kyaaaa!!!」 — giá trị audit: 「Hyu a!?\nƯm——Nkyuuuuuuuuuu!!!」
- Mới: 「Hyua!?\nƯm——Nkyuuuuuuuuuu!!!」
- Lý do: ひゅあっ = "hyua" một hơi; bản audit tách thành "Hyu a" (quy tắc ふかみh1 liệt kê đích danh "Hyu a" là dạng tách mảnh cần gộp). Giữ "Nkyuuuuuuuuuu" của audit: んきゅうううううううううう = きゅ(1 u) + う×9 = 10 u, đếm lại bằng máy đúng 10 u.

#### 965 — ハチロク — romaji
- JP: 「ひゃふっ！？」
- TW: 「呀嗚！？」
- Cũ: 「Hya fư!?」
- Mới: 「Hyafu!?」
- Lý do: ひゃふっ = "hyafu" một hơi; "Hya fư" tách thành hai mảnh và trộn romaji + Việt. Gộp thành một cách diễn romaji (tiền lệ ふかみh1; paulette-h1 きゃふっ→"Kyafu", h7 1442).

#### 966 — ハチロク — romaji (2 token)
- JP: 「ひゃんっ！　んっ！　あたって――あっ！\nコツって――奥っ――あふっ――おまんまん、のっ」
- TW: 「呀嗯！嗯！碰上——啊！一直——再往裡頭——啊呼——小妹妹的」
- Cũ: 「Hya! Ưm! Chạm rồi——a!\nCộc một cái——sâu quá——a phù——cô bé, của em」
- Mới: 「Hyan! Ưm! Chạm rồi——a!\nCộc một cái——sâu quá——Afu——cô bé, của em」
- Lý do: ひゃんっ → "Hyan!" (ん cuối bị mất trong bản cũ; tiền lệ hachiroku-h9 968 ひゃんっ→"Hyan!"); あふっ → "Afu" (một hơi "afu"; bản cũ "a phù" tách thành hai mảnh trộn La-tinh + Việt).

#### 977 — ハチロク — romaji
- JP: 「ひうっ！？」
- TW: 「咿！？」
- Cũ: 「Hí u!?」
- Mới: 「Hiu!?」
- Lý do: ひうっ = "hiu" một hơi; "Hí u" tách thành hai mảnh (tiền lệ ふかみh1 "Hi ah"→gộp; h1 1248 ひううう→"Hiuuu").

#### 995 — ハチロク — romaji
- JP: 「あひっ――んっ！　双鉄様っ！　双鉄さまぁっ！\nすごっ――奥っ――あたってっ――ごつんっって！」
- TW: 「啊——！雙鐵少爺！雙鐵少爺！插得——好深——好用力！」
- Cũ: 「A hi——ưm! Ngài Soutetsu! Ngài Soutetsu!\nTuyệt quá——sâu quá——chạm vào rồi——cộc một cái!」
- Mới: 「Ahi——ưm! Ngài Soutetsu! Ngài Soutetsu!\nTuyệt quá——sâu quá——chạm vào rồi——cộc một cái!」
- Lý do: あひっ = "ahi" một hơi; "A hi" tách thành hai mảnh (cùng mẫu 965/977). Các っ trên tên 双鉄様っ/双鉄さまぁっ không đụng — xem cờ §5.

### 3.3 ん+X — khôi phục âm mora bị mất

#### 1039 — ハチロク — romaji
- JP: 「ん――こくっ――んくっ――ごくっ」
- TW: 「嗯——嗚——嗯——嗯」
- Cũ: 「Ưm——ực——ưm——ực」
- Mới: 「Ưm——ực——ưm ku——ực」
- Lý do: んくっ → "ưm ku" (く bị mất hẳn trong bản cũ; mẫu "Ưm + X" của file h1 1245 んうっ→"Ưm ư", 1278 んちゅっ→"Ưm chụt"; h8 839 んくっ→"Ưn ku"). Giữ "ực" cho こくっ/ごくっ (tiếng nuốt, đã đúng).

#### 1051 — ハチロク — romaji
- JP: 「んふっ！」
- TW: 「嗯呼！」
- Cũ: 「Ưm hưm!」
- Mới: 「Ưm fu!」
- Lý do: んふっ → "Ưm fu" (tiền lệ h1 1219/1229, kisaki-h3 2207; "hưm" sai phụ âm f→h). Như 1036.

#### 1054 — 双鉄H — romaji
- JP: 「んむっ！」
- TW: 「嗯嗚！」
- Cũ: 「Ưm!」
- Mới: 「Ưm mư!」
- Lý do: んむっ = ん+む hai mora; bản cũ chỉ diễn ん, mất む. Mẫu "Ưm + X" (h1 1245 んうっ→"Ưm ư"); trong chính file này 993 んむっ đã là "ưm mư" đúng — 1054 không nhất quán với 993 nên sửa cho khớp.

### 3.4 Chuỗi rên dài → romaji + đếm nguyên âm

#### 1019 — ハチロク — romaji + đếm
- JP: 「じゅるるうううううううううっ！」
- TW: 「啾嚕——！」
- Cũ: 「Chu mút!!!」
- Mới: 「Jururuuuuuuuuuu!」
- Lý do: じゅるるうううううううううっ = じゅ(1 u) + る(1 u) + る(1 u) + う×9 = 12 u → "Jururu" + 9 u = "Jururuuuuuuuuuu" (đếm lại bằng máy: う×9, tổng 12 u). Bản cũ "Chu mút!!!" mất hẳn chuỗi dài 12 mora (tiền lệ h9 2135 じゅるうううううっ→"Juruuuuu" 7 u, 2120 ちゅううう→"chuuuu").

#### 1020 — ハチロク — romaji + đếm (phán đoán — xem cờ §5)
- JP: 「じゅにゅるるるるるるるるっ！！」
- TW: 「啾嚕——！！」
- Cũ: 「Chu mút!!」
- Mới: 「Junyururururururururu!!」
- Lý do: じゅにゅる×8 = ju-nyu-ru×8 (đếm lại bằng máy: る×8) → romaji nguyên dạng "Junyururururururururu" (tiền lệ h1 2179 じゅるるうるるる→"Jururuurururu" 13 ký tự, diễn đúng từng mora). Bản cũ "Chu mút!!" mất hẳn hình âm của chuỗi 14 mora (chỉ còn "!!" gợi độ dài).

#### 1030 — ハチロク — romaji + đếm
- JP: 「くふうううううんっ！」
- TW: 「嗚嗚嗚嗯！」
- Cũ: 「Ư hưm!!!」
- Mới: 「Kufuuuuuun!」
- Lý do: くふうううううんっ = く(1 u) + ふ(1 u) + う×5 + ん = 7 u → "Kufuuuuuun" (đếm lại bằng máy: う×5, tổng 7 u; tiền lệ h1 1241 くふううううん→"Kufuuuuun" 6 u). Bản cũ "Ư hưm!!!" sai hoàn toàn: mất く, thu chuỗi 7 u thành "hưm" 1 u, sai phụ âm f→h. TW 嗚嗚嗚嗯 xác nhận tiếng dài.

#### 1206 — ハチロク — romaji + đếm
- JP: 「れるっ――るっ――れろっ――じゅるるっ――\nんっ――んちゅっ――ちゅっ――ちゅううううっ」
- TW: 「（舔）——（舔）——（舔）——啾——嗯——嗯啾——啾——啾」
- Cũ: 「Liếm——liếm——liếm——chu mút——\nưm——ưm chụt——chụt——chu mút」
- Mới: 「Liếm——liếm——liếm——chu mút——\nưm——ưm chụt——chụt——chuuuuu」
- Lý do: ちゅううううっ = ちゅ(1 u) + う×4 = 5 u → "chuuuuu" (tiền lệ h9 2120 ちゅううう→"chuuuu" 4 u, 2078 ちゅうっ→"chuu" 2 u). Chỉ đổi token cuối; các token ngắn giữ quy ước "liếm/chu mút" của file.

### 3.5 Đếm nguyên âm

#### 1056 — ハチロク — đếm
- JP: 「んああっ！　おちん、ちんっ――ごりって、\nおまんまん、して、くれる、おちんちん、もっ！」
- TW: 「嗯嗯！雞，雞——鑽進來，我也喜歡肯插入我小妹妹的雞雞！」
- Cũ: 「Ưm a! Cậu, bé——cậu bé đang, ngoáy mạnh\ntrong cô bé, của em, em cũng thích!」
- Mới: 「Ưm aa! Cậu, bé——cậu bé đang, ngoáy mạnh\ntrong cô bé, của em, em cũng thích!」
- Lý do: んああっ = ん + あ×2 → "Ưm aa" (bản cũ 1 a, thiếu 1 a; đếm lại bằng máy: あ×2. Tiền lệ h1 1253 あああ→"Aaa" 3 a, Paulette h2 929 んううっ→"Nuu").

#### 1120 — ハチロク — đếm
- JP: 「は、はい。『お前は僕の女だ』と、双鉄様、に――\n刻印っ、して、いただけたような気が――んうっ！」
- TW: 「是、是。彷彿是您在我身上刻下了『你是我的女人』幾個字一樣——嗚！」
- Cũ: 「Vâ, vâng. Cảm giác như ngài Soutetsu, đã khắc ghi——\n'Em là người phụ nữ của anh' lên người em vậy——ưm!」
- Mới: 「Vâ, vâng. Cảm giác như ngài Soutetsu, đã khắc ghi——\n'Em là người phụ nữ của anh' lên người em vậy——ưm ư!」
- Lý do: んうっ = ん + う(1 u) → "ưm ư" (bản cũ "ưm" mất hẳn う; mẫu "Ưm + ư×n" — tiền lệ h1 1245 �んうっ→"Ưm ư" 1 u, 1248 んううっ→"Ưm ưư" 2 u; h9 giữ "ưm ư" cho んうっ).

## 4. Các dòng giữ (đáng chú ý)

- **Fix moan của audit — đồng ý 6/8, thay thế 2 ở đúng 1 token:** giữ 973 ふあああんっ→"Fuaaan!" (あ×3, đếm lại đúng), 1053 んひゅっ→"Nhyu!", 1055 んきゅっ→"Nkyu!!", 1045 れろっ→"liếm" (token ngắn, cách diễn nghĩa của audit), 972/1148 うふふ→"Ufufu" (tiếng cười là tiếng cười, không phải rên). Thay thế: 964 "Hyu a"→"Hyua" (§3.2), 974 "Phù a"→"Fua" (§3.1) — chỉ đổi đúng token rên, phần còn lại giữ nguyên giá trị audit (964 giữ "Nkyuuuuuuuuuu" 10 u; 974 giữ "an" cho あんっ; 976 giữ Ư cuối dòng của audit).
- **"a a"/"A a" cho ああっ — giữ (976, 1011):** cùng một nguyên âm lặp lại, đủ số lượng (2 a), không mất âm. Tiền lệ kisaki-h3 giữ "a a"/"á á" cho ああっ (audit đã khóa ở hachiroku-h5/fukamih3); audit file này cũng giữ "a a" ở 976 trong lúc sửa cùng dòng. Chỉ gộp các mảnh KHÁC âm ("Hya fư", "Hí u", "Hyu a") — không gộp lặp cùng nguyên âm. Nếu parent muốn "Aa", sửa 1 ký tự ở đợt thống nhất (xem cờ §5).
- **"chụt"/"chu mút"/"liếm" cho token hôn/mút ngắn — giữ:** quy ước của file cho ちゅっ/じゅるっ/れるっ/れろっ ngắn (1013, 1021, 1022, 1024, 993, 1045, 1206-phần đầu). Chỉ các token DÀI mới về romaji + đếm (1019, 1020, 1038, 1206-cuối).
- **"Hự" cho くっ — giữ (976, 1041):** quy ước tiếng gằn của file, nhất quán cả 2 dòng; tiền lệ lr_reinah1 1225 (くっ→"Ư") chỉ ghi là chưa chắc chắn, không phải fix.
- **Gasp Ư — không đụng:** 14 dòng gasp của sweep/audit (717, 720, 721, 985, 987, 990, 1112, 1156, 1189, 1201, 1202, 1083, 1565 + っ cuối 976) giữ nguyên giá trị audit. Không có dòng "Kh" khóa nào trong file (các match "kh" chỉ là từ Việt thường: không/khi/khác...).
- **1031 んっっ → "Ưm" — giữ:** tiền lệ kisaki-h3 2261 (んっっ → "Ưm"); っ kép là nhấn cắt, đã có "——" diễn đạt.
- **1014 nói ngọng — giữ giá trị audit:** 「はふはむはふはむおはひひははひ、ほーふぇふはま」 là lời nói ngọng khi miệng đang bận, KHÔNG phải dòng rên (quy tắc 3b MOAN-BRIEF) — để audit.
- **960 "ư" cho っ đứng riêng — giữ:** âm đã được diễn thành "ư", không mất — không thêm Ư (quy tắc gasp: chỉ thêm Ư khi âm mất hẳn).
- **SFX trong （ ） — giữ nguyên hệ diễn theo nghĩa hành động:** 36 dòng độc thoại (ぴとっ→"Chạm nhẹ", びゅっ→"Phụt", ず――ううううううっ→"Phập——phập phập phập phập", きゅんっ→"Siết"...) theo tiền lệ moan-fix h1/h8; 1717 giữ dù JP có う×6 (dung sai chuỗi SFX, tiền lệ lr_reinah1).
- **Thán từ ngắn đã đúng — giữ:** 997/988/989/998/1165 あ……→"A……", 1007 あっ→"A", 979 はっ→"Ha", 986/1029 う……→"Ư……", 1043 ん……あっ→"Ưm……a", 983/984 えっ/え→"Hả", 980 まぁっ→"Ái chà", 1012 ああ→"À" (câu đáp, không phải chuỗi rên), 1047 ああ……→"Ừm……" (câu đáp).
- **993 んむっ → "ưm mư" — đã đúng, giữ** (mẫu cho 1054 sửa theo).

## 5. Cờ (không tự quyết — để parent/đợt thống nhất)

- **995 双鉄様っ！/双鉄さまぁっ！:** audit chỉ thêm Ư cho tên+っ ở 990/1189 (すずっ→"SuzuƯ") mà không thêm ở 995 (双鉄様っ！, 双鉄さまぁっ！ giữa dòng, sau có "!"). Đây là quyết định gasp thuộc về audit — vòng moan không tự thêm Ư. Parent xem lại có cần Ư ở 995 không.
- **1020 "Junyururururururururu!!":** phán đoán của agent (romaji nguyên dạng theo tiền lệ h1 2179); TW cũng thu gọn thành một 啾嚕. Nếu parent thấy "Chu mút!!" đã đủ, hoàn lại ở đợt thống nhất.
- **976/1011 "a a"/"A a":** giữ theo tiền lệ kisaki-h3 (xem §4). Nếu parent muốn thống nhất thành "Aa", sửa ở đợt thống nhất.
- **1030 "Kufuuuuuun!":** 7 u đã đếm lại bằng máy (く1 + ふ1 + う×5); TW 嗚嗚嗚嗯 ủng hộ tiếng dài. Không có gì cần hỏi thêm.

## 6. Kiểm chứng audit (moan)

- Audit sửa 8 dòng moan/SFX: 1053, 1055, 964, 973, 974, 1045, 972, 1148. Kiểm chứng lại từng dòng: 6/8 đúng nguyên (973, 1053, 1055, 1045, 972, 1148); 2/8 thay thế ở đúng 1 token rên (964 "Hyu a"→"Hyua", 974 "Phù a"→"Fua" — xem §3, §4).
- Đếm nguyên âm của audit kiểm chứng lại độc lập bằng máy: 964 んきゅう×9 → 10 u ("Nkyuuuuuuuuuu" ✓), 973 ふあああん → 3 a ("Fuaaan" ✓), 1055 んきゅ → "Nkyu" ✓, 1053 んひゅ → "Nhyu" ✓.
- Audit ghi chú "họ fa/fu 'Phù a' giữ nguyên trong audit này, chờ xem xét romaji ở vòng moan / đợt thống nhất" — vòng moan này đã xem xét: 10 dòng "phù a"/"Phù a" (974, 976, 996, 1001, 1003, 1004, 1006, 1011, 1036, 1038 — 11 token fa/fu) đều về romaji; ghi chú thống nhất cho các dòng đó được thay thế bằng fix này.

## 7. Lượt soát 2 + kiểm chứng máy

- Lượt soát 2: đọc lại toàn bộ 27 giá trị fix đối chiếu JP (+TW khi cần), kèm đếm cơ học lại các dòng đếm nguyên âm (1019: 12 u; 1020: る×8; 1030: 7 u; 1206: 5 u; 1038: 4 o; 964: 10 u; 1056: 2 a; 1120: 1 u; 973-giữ: 3 a) — đều đúng.
- Tổng: 27 / tái kiểm chứng: 27 / bỏ: 0 / sửa: 0.
- Kiểm chứng máy: JSON 27 mục dạng chuẩn (key string, list-of-dicts: key/jp/tw/old_vn/fix/kind/character); jp/tw/old_vn khớp CSV3 tuyệt đối 27/27 (1 bộ duy nhất, 312 dòng); khối TOML 27 khóa parse bằng tomllib, 0 sai lệch giá trị so với JSON; mỗi fix chỉ khác giá trị gốc (old_vn, hoặc giá trị audit với 964/974/976) đúng ở token rên mục tiêu (kiểm chứng bằng diff); không dòng gasp Ư nào bị đụng (976 chỉ đổi token ふあっ, giữ Ư cuối dòng của audit); không dòng "Kh" nào bị đổi (file không có dòng "Kh" khóa).
- Lưu ý: bản nháp đầu viết tay thiếu dấu 「」 ở cả 27 giá trị fix — kiểm chứng máy so diff đã bắt được và sửa lại toàn bộ TRƯỚC lượt soát 2; lượt soát 2 đọc lại 27 giá trị đã sửa, không phát hiện thêm lỗi nào.

## 8. Khối TOML (parse-verified bằng tomllib: 27 khóa, 0 sai lệch giá trị so với wrong.json)

```toml
[script]
"719" = "「——Ua」"
"960" = "「Ya——ư——ngực……sướng, quá」"
"961" = "「Ya」"
"964" = "「Hyua!?\\nƯm——Nkyuuuuuuuuuu!!!」"
"965" = "「Hyafu!?」"
"966" = "「Hyan! Ưm! Chạm rồi——a!\\nCộc một cái——sâu quá——Afu——cô bé, của em」"
"974" = "「Fua——a——an! Ưm——」"
"976" = "「Fua——tuyệt quá——ưm——a——a a!\\nHự——đến đây——thứ gì đó trắng xóa——to lớnƯ」"
"977" = "「Hiu!?」"
"995" = "「Ahi——ưm! Ngài Soutetsu! Ngài Soutetsu!\\nTuyệt quá——sâu quá——chạm vào rồi——cộc một cái!」"
"996" = "「A……ưm——Fu——Fua——」"
"1001" = "「A……Fua——a——Bàn tay, của ngài Soutetsu……\\nthật to, lớn——và thật, ấm, áp」"
"1003" = "「A……ưm——ực. Pua——a——\\nA!? Ngài, ngài Soutetsu, em thất lễ rồi」"
"1004" = "「A……Pua」"
"1006" = "「A……Pua……a——Hôn——thích quá……」"
"1011" = "「A a——em hiểu——em hiểu rồi! Tử cung——\\nbụng em——ưm——nóng quá——đang lan tỏa ra——Fu, a」"
"1019" = "「Jururuuuuuuuuuu!」"
"1020" = "「Junyururururururururu!!」"
"1030" = "「Kufuuuuuun!」"
"1036" = "「Ưm——ưm fu——Fu, a」"
"1038" = "「Ưm——chụt——chu mút——ưm——ực——\\nPua——ưm——chụt——Reroooo」"
"1039" = "「Ưm——ực——ưm ku——ực」"
"1051" = "「Ưm fu!」"
"1054" = "「Ưm mư!」"
"1056" = "「Ưm aa! Cậu, bé——cậu bé đang, ngoáy mạnh\\ntrong cô bé, của em, em cũng thích!」"
"1120" = "「Vâ, vâng. Cảm giác như ngài Soutetsu, đã khắc ghi——\\n'Em là người phụ nữ của anh' lên người em vậy——ưm ư!」"
"1206" = "「Liếm——liếm——liếm——chu mút——\\nưm——ưm chụt——chụt——chuuuuu」"
```
Lưu ý: trong khối TOML trên, `\\n` là ký tự xuống dòng đã escape (giá trị thực trong JSON/TOML là `\n` literal như CSV3).

## Kết bài

File ハチロクh2_お勉強の成果.txt.toml: đã đọc 312/312 dòng, xét 120 dòng ứng viên rên/SFX, đổi 27 dòng (20 romaji + 5 romaji-đếm + 2 đếm nguyên âm), giữ 93 dòng. Lỗi rên tập trung ở một kiểu hệ thống của bản dịch cũ: tách một âm rên duy nhất thành nhiều mảnh rời ("phù a", "Hya fư", "Hí u", "Hyu a", "A hi", "ư a") — đã gộp lại thành một cách diễn romaji theo đúng quy tắc Hieu duyệt 21/11; cộng thêm các dòng mất phụ âm mora (やっ→"Ya" ×2, んくっ/んむっ/んふっ) và 5 chuỗi dài đếm lại đúng số nguyên âm. 3 giá trị audit được thay thế ở đúng 1 token rên (964, 974, 976); 6/8 fix moan của audit giữ nguyên. Không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào. 4 cờ để parent/đợt thống nhất (§5). Sau file này tổng moan là 26 file / 588 dòng (cơ sở 25 file / 561 dòng + 27 file này — đã kiểm chứng trực tiếp dòng tổng cuối của ROUTE-MOANS.md).
