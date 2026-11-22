# Moan-fix REVIEW — lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml (06_Kisaki)

## 1. Xác minh file

- TOML: `sources/toml2/translation_toml/06_Kisaki/lr#U7a00#U54b2#U8ffd#U52a0h_#U304a#U98a8#U5442#U306f#U65e5#U30ce#U672c#U5f0f#U306b#U9650#U308b#U306d.txt.toml`, md5 `947b7e40987a5d77e8a0f963aed53302`, UTF-8 BOM + CRLF (658 CRLF). `[script]` 320 keys; `[selections]` rỗng. Không nằm trong 11 nhóm file trùng.
- CSV3: 1 bộ duy nhất, 320 dòng script, 0 key trùng, 0 VN trống. CSV3 VN khớp TOML (đã kiểm tra flat-match qua audit).
- Audit của file này: 30 dòng sai (`audit-lr-kisaki-tsuikah-ofuro-hinomoto-wrong.json`), trong đó 29 dòng là moan/gasp/romaji/vowel-count, 1 dòng meaning (1319 — không thuộc phạm vi moan). Old VN của moan pass = giá trị audit fix với các key audit đã đổi, còn lại = CSV3 VN.
- Sweep: đọc trực tiếp `sweep-raw-gasp-wrong.json` — 8 mục cho file này (775, 800, 1079, 1124, 1133, 1134, 1135, 1473), tất cả đã được audit áp nguyên văn, đều là dòng Ư gasp đã khóa — KHÔNG sửa lại.
- Đã đọc toàn bộ 320 dòng (JP + TW + VN).

## 2. Kiểm kê tiếng rên

- Tổng số dòng rên đã xét: **137 dòng** (92 dòng thoại + 45 dòng SFX độc thoại 1806–1883).
- Đổi: **25 dòng** — fa/fu 7, romaji 9, vowel-count 6, sfx 3.
- Giữ: 112 dòng.

## 3. Các dòng sửa (25)

### 782 — 稀咲 — fa/fu
- JP: 「――んっ――ふっ――あ。毎晩、みたいに――こんなに――エッチに――たくさん――もん、で――ん」
- TW: 「——嗯——呼——啊。就像每天晚上那樣——你揉得——那麼煽情——嗯」
- Cũ: 「——Ưm——Phù——A. Giống như, mỗi đêm——\nanh nhào nặn——nhiều thế này——dâm đãng thế này——ưm.」
- Mới: 「——Ưm——Fu——A. Giống như, mỗi đêm——\nanh nhào nặn——nhiều thế này——dâm đãng thế này——ưm.」
- Lý do: ふっ → "Fu" theo hướng romaji của các file đã gộp (日々姫h3 1013/1109/1142, ハチロクh3); "Phù" là dạng Việt gây ngượng trong chuỗi rên.

### 784 — 双鉄 — romaji
- JP: 「――ぷあ。うむ。確かになめても刺激などは一切ないな。無味無臭で……ゼリーのような、水まんじゅうのような」
- TW: 「——噗啊。嗯，的確是舔了之後也沒有刺激性的味道。沒有味道和氣味……就像是果凍或者水饅頭一樣」
- Cũ: 「――Phù. Ừm. Đúng là liếm vào cũng không thấy kích thích gì cả.\nKhông mùi không vị……Giống như thạch, hay giống như bánh Mizu Manju vậy.」
- Mới: 「――Pua. Ừm. Đúng là liếm vào cũng không thấy kích thích gì cả.\nKhông mùi không vị……Giống như thạch, hay giống như bánh Mizu Manju vậy.」
- Lý do: ぷあ là âm bật môi "pua", bản cũ "Phù" sai hẳn âm (đó là ふ). Tiền lệ ぷあっ→"Pua" (日々姫h3 1056/1111/1114).

### 1074 — 稀咲 — fa/fu
- JP: 「やっ――あっ――ふあっ――そう、てつぅっ」
- TW: 「呀——啊——呼——雙鐵」
- Cũ (audit fix): 「Ya——A——Phùa——Anh Sou, tetsu.」
- Mới: 「Ya——A——Fua——Anh Sou, tetsu.」
- Lý do: ふあっ → "Fua" (romaji fallback; CSV3 gốc đã là "Fua", audit đổi thành "Phùa" theo luật fa/fu lúc đó — moan pass đổi lại). "Ya" của audit giữ nguyên (やっ đúng).

### 1085 — 稀咲 — fa/fu
- JP: 「ふうぅ」
- TW: 「呼」
- Cũ (audit fix): 「Phùuu.」
- Mới: 「Fuuu.」
- Lý do: ふうぅ = ふ + う + ぅ = 3 u → romaji "Fuuu". Họ fu → romaji (tiền lệ んふううう…→"Nfuuuu…" ハチロクh3 1063, 日々姫h3 1124).

### 1100 — 稀咲 — fa/fu
- JP: 「っ――ぁっ――ぁっ――ぁっ――\nぁ――ぁぁっ――んっ――ふあっ――」
- TW: 「啊——啊——啊——啊——啊——啊——嗯——呼啊」
- Cũ (audit fix): 「Ư——A——A——A——\nA——Aa——Ưm——Phùa——」
- Mới: 「Ư——A——A——A——\nA——Aa——Ưm——Fua——」
- Lý do: ふあっ → "Fua" (như 1074; CSV3 gốc đã là "Fua").

### 1110 — 双鉄 — vowel-count
- JP: 「ああ――確かにだ。言われてみれば」
- TW: 「啊——確實。這麼一說還真是」
- Cũ: 「A――Đúng thật. Nghe em nói mới để ý.」
- Mới: 「Aa――Đúng thật. Nghe em nói mới để ý.」
- Lý do: ああ = 2 mora a → "Aa"; bản cũ mất 1 a. Cùng luật đếm audit đã áp trong file này (1111 ぁあ→"Aa", 1122 ああっっ→"Aa").

### 1112 — 稀咲 — fa/fu
- JP: 「あ……ふっ――ふあっ――ね、双鉄――乳首――んっ\n――乳首……それ、ね？　もっと――もっと、して？」
- TW: 「啊……呼——呼啊——我說，雙鐵——乳頭——嗯……那個，你多摸一摸——好嗎」
- Cũ (audit fix): 「A……Phù――Phùa――Này, anh Soutetsu――Nhũ hoa――Ưm\n――Nhũ hoa……Cái đó, nhé? Thêm nữa――Làm thêm nữa đi?」
- Mới: 「A……Fu――Fua――Này, anh Soutetsu――Nhũ hoa――Ưm\n――Nhũ hoa……Cái đó, nhé? Thêm nữa――Làm thêm nữa đi?」
- Lý do: ふっ → "Fu", ふあっ → "Fua" (họ fu → romaji; xem 782/1074).

### 1114 — 稀咲 — romaji
- JP: 「あ……はっ――ん。おっぱい――\n双鉄の手、ぬらぬらで――んうっ！！」
- TW: 「啊……哈——嗯。胸部——你的手——滑滑的——嗯！！」
- Cũ: 「A……Hà――Ưm. Ngực――\nTay của anh Soutetsu, trơn tuột――Ưm!!」
- Mới: 「A……Hà――Ưm. Ngực――\nTay của anh Soutetsu, trơn tuột――Nu!!」
- Lý do: んうっ = ん + う + っ → "Nu" (1 u; quy tắc F6: tổng = số mora phát âm, ん không tính thêm). "Ưm" làm mất hẳn nguyên âm う. Tiền lệ んううっ→"Nuu" (日々姫h3 1010), んうううううう→"Nuuuuuu" (ハチロクh3 1064).

### 1121 — 双鉄 — vowel-count
- JP: 「ぁぁあっ――ううっ――く、あ――気持ち、いい――\n確かにぞわぞわ――気持ちいいのは、確か――なのだが」
- TW: 「啊啊啊——嗯——呃、啊——好舒服——雖然會讓人心急——舒服還是舒服——」
- Cũ: 「Aaa——Ư——Ku, a——Sướng, quá——\nĐúng là râm ran——sướng thì, có sướng thật——nhưng mà.」
- Mới: 「Aaa——Uu——Ku, a——Sướng, quá——\nĐúng là râm ran——sướng thì, có sướng thật——nhưng mà.」
- Lý do: ううっ = う + う + っ → "Uu" (2 u); bản cũ "Ư" chỉ còn 1 nguyên âm, mất 1 u. (Ư đơn lẻ cho うっ đơn thì đúng — xem 1140 giữ.)

### 1144 — 稀咲 — fa/fu
- JP: 「う……ん。ふ、ふっ――ありがと、双鉄」
- TW: 「嗯……呼、呼——謝謝你，雙鐵」
- Cũ: 「Ư……m. Phù, phù——cảm ơn anh, Soutetsu.」
- Mới: 「Ư……m. Fu, fu——cảm ơn anh, Soutetsu.」
- Lý do: ふ、ふっ → "Fu, fu" (họ fu → romaji).

### 1147 — 稀咲 — fa/fu
- JP: 「ん……ふ、あっ――キスじゃなくって、\nべろべろチュウチュウ――首筋、されるの新鮮かも」
- TW: 「嗯……呼、啊——脖子不是被親到，而是被這樣舔著——感覺很新鮮」
- Cũ: 「Ưm……Phù, a――Không phải là hôn,\nmà là bị liếm láp mút mát――ở gáy, cảm giác cũng mới mẻ thật.」
- Mới: 「Ưm……Fu, a――Không phải là hôn,\nmà là bị liếm láp mút mát――ở gáy, cảm giác cũng mới mẻ thật.」
- Lý do: ふ → "Fu" (dạng tách "Fu, a" như 日々姫h3 1018/1021/1112).

### 1162 — 稀咲 — romaji
- JP: 「んあっ！？」
- TW: 「嗯啊！？」
- Cũ: 「Ưm a!?」
- Mới: 「Na!?」
- Lý do: んあっ là MỘT âm ("na"); bản cũ tách thành hai mảnh "Ưm a". Tiền lệ: んあっ→"Na" (lr真闇追加h 1103, 真闇h1, ポーレットh4 — đều đã gộp), んぁ→"Na" (ハチロクh6 843). Xem cờ F3 về phạm vi còn mở.

### 1180 — 双鉄 — vowel-count
- JP: 「ああ、そうか。はじめてのセックスのときにも、そんなことを言っていたな」
- TW: 「噢，這樣啊。我們第一次做愛的時候你也說過類似的話」
- Cũ: 「A, ra vậy. Lúc làm tình lần đầu tiên,\nem cũng từng nói như thế nhỉ.」
- Mới: 「Aa, ra vậy. Lúc làm tình lần đầu tiên,\nem cũng từng nói như thế nhỉ.」
- Lý do: ああ = 2 a → "Aa" (như 1110). Xem cờ F4.

### 1265 — 稀咲 — romaji
- JP: 「ローションをお口にいれても――あむっ。\nん……ちゅくっ――ちゅっ――ぺちゅううっ――ぷあ」
- TW: 「潤滑液還可以含在嘴裡——唔。嗯……啾嚕——啾——咕啾——呼啊」
- Cũ: 「Dù có cho lotion vào miệng cũng――ngoạm.\nƯm……chụt――chụt――chụt――phù.」
- Mới: 「Dù có cho lotion vào miệng cũng――ngoạm.\nƯm……chụt――chụt――chụụụt――Pua.」
- Lý do: (1) ぺちゅううっ = ちゅ + う + う = 3 u → "chụụụt" (bản cũ "chụt" mất 2 u; tiền lệ ちゅろぉぉぉっ→"Chụụụụt" ハチロクh3 1813). (2) ぷあ → "Pua" (như 784; bản cũ "phù" sai âm).

### 1296 — 双鉄 — romaji
- JP: 「稀咲――っ――これは――気持ちはいい、が――\n確かに、ぞわぞわ――もどかし、すぎ、てっ――んうっ」
- TW: 「稀咲——啊——這樣——雖然感覺舒服——但又感覺好心急——心裡癢癢的——嗯」
- Cũ: 「Kisaki——Cái này——Sướng thì sướng thật, nhưng——\nĐúng là, râm ran——nôn nóng, quá, đi mất——Ưm.」
- Mới: 「Kisaki——Cái này——Sướng thì sướng thật, nhưng——\nĐúng là, râm ran——nôn nóng, quá, đi mất——Nu.」
- Lý do: んうっ → "Nu" (như 1114).

### 1819 — monologue — romaji
- JP: （ぺろっ――れるっ――ちゅむっ――ずちゅううううっ）
- TW: （反覆舔拭）
- Cũ: 「（Liếm――liếm――chụt――chụt）」
- Mới: 「（Liếm――liếm――chụt――Zuchuuuuu）」
- Lý do: ずちゅううううっ = ず(u) + ちゅ(u) + う×4 = 6 u → romaji "Zuchuuuuu" (6 u, đếm bằng máy). SFX dài không diễn độ dài ("chụt") → romaji (tiền lệ ハチロクh3 1832 ずるううううっ→"Zuruuuuu").

### 1823 — monologue — romaji
- JP: （にちゃあああああああっ――ぬぢゅんっ！！）
- TW: （套弄）
- Cũ: 「（Nhóp nhép――trơn tuột!!）」
- Mới: 「（Nichaaaaaaaa――trơn tuột!!）」
- Lý do: にちゃあああああああっ = ちゃ(a) + あ×7 = 8 a → romaji "Nichaaaaaaaa" (8 a, đếm bằng máy). SFX dài mất hẳn độ dài trong "Nhóp nhép" → romaji (như 1819).

### 1828 — monologue — sfx
- JP: （にゅるっ――ぬぶっ――にゅっ――じゅくっ――）
- TW: （扭來扭去）
- Cũ: 「（Trơn tuột――nhóp nhép――nhão nhoét――）」
- Mới: 「（Trơn tuột――nhóp nhép――nhão nhoét――Nhóp nhép）」
- Lý do: 4 âm JP nhưng VN chỉ diễn 3 âm — じゅくっ bị mất hẳn (vi phạm "không để mất âm"). Thêm "Nhóp nhép" cho じゅくっ (âm ướt dính; lặp lại được — tiền lệ 1808 hai âm cùng "Nhóp nhép").

### 1834 — monologue — vowel-count
- JP: （ぞりゅうううううううううっっっっっっっっ！！！）
- TW: （抽出）
- Cũ: 「(Sùng sụcccccccc!!!)」
- Mới: 「(Sùng sụccccccccc!!!)」
- Lý do: ぞりゅ + う×9 → chuỗi "sụ" + 9 c (bản cũ 8 c, thiếu 1). Quy ước đếm c = số う kéo dài (chứng: 1830 8う→8c giữ nguyên trong ハチロクh3).

### 1839 — monologue — sfx
- JP: （くりっっ――くりゅっ――しこっ――しにゅっ――）
- TW: （揉來揉去）
- Cũ: 「（Cọ xát――trơn tuột――nhóp nhép――）」
- Mới: 「（Cọ xát――trơn tuột――Sột soạt――nhóp nhép）」
- Lý do: 4 âm JP, VN chỉ diễn 3 — しこっ bị mất. Thêm "Sột soạt" cho しこっ (âm cọ xát; くりっっ→"Cọ xát", くりゅっ→"trơn tuột", しにゅっ→"nhóp nhép" giữ nguyên thứ tự). Ghi chú: JP có くりっっ (2 っ) — không phải lỗi mojibake, đã kiểm tra byte gốc CSV3 + TOML.

### 1848 — monologue — sfx
- JP: （にゅるっ――こしゅっ――きゅりゅっ――しゅちゅっ）
- TW: （搓來搓去）
- Cũ: 「（Trơn tuột――cọ xát――nhóp nhép――）」
- Mới: 「（Trơn tuột――cọ xát――nhóp nhép――Nhóp nhép）」
- Lý do: 4 âm JP, VN chỉ diễn 3 — しゅちゅっ bị mất. Thêm "Nhóp nhép" cho しゅちゅっ (âm ướt; tiền lệ 1822 じゅちゅっ→"Nhóp nhép").

### 1857 — monologue — romaji
- JP: （にゅるうううううううううっっ）
- TW: （滑落）
- Cũ: 「（Trơn tuột）」
- Mới: 「（Nyuruuuuuuuuuu）」
- Lý do: にゅるううううううううう = にゅ(u) + る(u) + う×9 = 11 u → romaji "Nyuruuuuuuuuuu" (11 u, đếm bằng máy). SFX dài không diễn độ dài → romaji (như 1819/1823).

### 1867 — monologue — vowel-count
- JP: （じゅるるうううううううううううううううっっっ！）
- TW: （直搗黃龍）
- Cũ: 「(Sùng sụccccccccccccc!)」
- Mới: 「(Sùng sụccccccccccccccc!)」
- Lý do: じゅるる + う×15 → chuỗi "sụ" + 15 c (bản cũ 13 c, thiếu 2). Cùng quy ước đếm như 1834.

### 1880 — monologue — vowel-count
- JP: （じゅぶううううううううううっっ！！　ごりゅっ！！）
- TW: （長驅直入）
- Cũ: 「(Sùng sụcccccccc!! Cục!!)」
- Mới: 「(Sùng sụcccccccccc!! Cục!!)」
- Lý do: じゅぶ + う×10 → chuỗi "sụ" + 10 c (bản cũ 9 c, thiếu 1). Cùng quy ước đếm như 1834. (Cẩn thận: "Cục" chứa 1 c riêng — đếm chuỗi kéo dài, không đếm tổng c.)

### 1883 — monologue — romaji
- JP: （くちいいいっっっっっ）
- TW: （頂上）
- Cũ: 「(Nhóp nhép)」
- Mới: 「(Kuchiiii)」
- Lý do: くちいいい = ち(i) + い×3 = 4 i → romaji "Kuchiiii" (4 i, đếm bằng máy). SFX dài mất hẳn độ dài trong "Nhóp nhép" → romaji (như 1819/1823/1857).

## 4. Các dòng rên giữ nguyên (ghi chú đáng chú ý)

- **Ư gasp đã khóa (không đụng):** 775 (――っ→"Ư"), 800 ("…………Ư"), 1079 ("Ư——Kuh!!"), 1080 ("Ư!?"), 1124 ("ƯƯƯƯƯƯ!!"), 1133/1134/1135, 1473 (audit fix "——Ư!!!"). Sweep 8 mục đều đã áp — kiểm chứng xong.
- **Audit đã romaji đúng:** 1071 "Hia——Yaa" (ひあっ/やあっ), 1075 "Hyan." (ひゃんっ), 1077 "Yaaa" (やぁあっ = 3 a), 1078 "Kyaa!!?" (きゃあっ = 2 a), 1116 "Kua.", 1154 "Nhyu!!", 1158 "Nku!!", 1160 "Ngyu!!!", 1161 "Nkyun!!!!", 1163 "Nyu!!", 1159 "Nhyuuuuuuuuuuu!!!" (đếm bằng máy: 11 u = ひゅ + う×10, đúng).
- **Họ fu đã romaji sẵn:** 1093 "Fu…… a", 1104 "Fu, a", 1112 (phần ふっ đã sửa — xem §3), 1138 audit "Fu", 1140 "Fu", 1195 "Fu——A", 1315 "Fu", 1353 "Fu".
- **Cười:** 1170/1175 "Fufu", 1173 "Nfufu" (んふふっ — viết hoa đầu câu, đúng).
- **Grunt "Hự" giữ:** 778/780/1130/1148 くっ→"Hự" (quy ước grunt đã chốt; tiền lệ 日々姫h3 1018 giữ "hự" cho うっ). 1836 （ぐくっ！）→"(Hự!)" giữ.
- **Ưm cho ん/うん:** 1025/1039/1115/1142/1143/1151/1165/1277/1286/1307/1314/1315/1328/1349/1355/1356/1361 — んっ/うんっ/ん…… đều diễn đủ âm, không mất.
- **はうん→"Ha ưm" giữ (1125/1127):** は + う + ん cả 3 mora đều có mặt ("Ha" + "ưm"); khác んうっ (1114/1296) chỉ còn "Ưm" mất hẳn う.
- **Ư đơn cho うっ đơn (1140) giữ; "Ư ư" cho うぅっっ (1137, audit) giữ — đủ 2 nguyên âm; riêng ううっ (1121) bản cũ chỉ còn 1 "Ư" nên đã sửa thành "Uu".**
- **SFX ngắn giữ nguyên VN:** 1806–1818, 1822, 1826, 1827, 1840, 1843, 1845 (ぐちゅうう, 2 extender — dưới ngưỡng romaji), 1846, 1847, 1850, 1851, 1856, 1858, 1870–1882 (trừ các dòng đã sửa). 1830 "Sùng sụcccccccc" giữ (8c = 8 extender, đúng). 1860 "Phụtụtụtụtụt" giữ (5ụ = 5 extender, đúng; trùng hệt ハチロクh3 1860 đã gộp). 1868 "Phập bập bập bập bập!!" giữ (trùng hệt ハチロクh3 1868 đã gộp).
- **Không phải rên / nội dung:** các っ gắn từ nội dung (1049/1058/1059/1197/1244/1260/1274/1356…), 1023 ho "khụ! Khụ!", 1351 （ぺろっ）→"（Liếm nhẹ）", 1827 （きゅっ！）→"(Siết!)" (ngắn, dạng động từ được chấp nhận), 1838 （くぱあっ）→"(Tách ra)".
- **1124 "ra rồiiiii":** audit giữ dạng Việt của âm lên đỉnh — là từ ("ra rồi"), không phải âm thuần — giữ.
- **1071 もっとおおおっ → "Nữa đi!!!":** độ dài ooo không diễn — nhưng đây là kéo dài nhấn mạnh trên TỪ (もっと), không phải âm rên; audit để vậy — giữ (cờ F7).

## 5. Cờ (flags — cho unification pass)

- **F1 — 1861** ぞにゅううううううううううう → "Thọc sâubbbbbbbbbbbbbbbbb" (17 b so với 11 extender): dạng động từ + kéo dài tạo hình, GIỮ. Cùng lớp với cờ F1 của lr_日々姫h2 (công thức đếm độ dài SFX). Nếu unification quyết romaji cho lớp này → "Zonyuuuuuuuuuuuu" (12 u).
- **F2 — 1865** きゅううううううううううううう → "Siết chặtttttttttttttttttttt" (21 t so với 13 extender): cùng lớp F1. Lưu ý ハチロクh3 1836 đã đổi cùng dạng JP (7 u) "Siết chặt!!!"→"Kyuuuuuuu" khi VN KHÔNG kéo dài; ở đây VN có kéo dài nên giữ. Nếu quyết romaji → "Kyuuuuuuuuuuuuuu" (14 u).
- **F3 — 1162 んあっ→"Na!?":** đã đổi theo tiền lệ 3 file đã gộp, nhưng ROUTE-MOANS.md cờ F8 ghi phạm vi んあっ→"Na" vẫn còn mở, và lr-kisakih1 giữ quy ước nội file "Ưn" cho ん+nguyên âm. Unification xác nhận toàn dự án.
- **F4 — 1110/1180 ああ→"Aa":** sửa đếm nguyên âm trên tiếng thở dài giao tiếp (không phải rên hẳn); audit để "A". Nếu unification muốn dạng lỏng "A" cho ああ giao tiếp thì hoàn lại 2 dòng này.
- **F5 — 1820/1845:** じゅりゅうう / ぐちゅうう (2 extender) → "Sùng sục" giữ không kéo dài — dưới ngưỡng 4-extender của ハチロクh3; biên, unification có thể xem lại.
- **F6 — 1817:** むにいいっ→"Nắn bóp", くりゅん→"Sột soạt" — dạng động từ lỏng, giữ; biên về độ khớp âm.
- **F7 — 1071:** xem §4 (もっとおおおっ).
- **F8 — 1860:** "Phụtụtụtụtụt" giữ (đếm đúng 5ụ = 5 extender); trùng hệt ハチロクh3 1860 — nếu unification đổi cách đếm lớp này thì đổi cả hai file cùng lúc.
- **F9 — 1124:** xem §4 ("ra rồiiiii").

## 6. Second pass

- Tổng số fix: **25** / đã đọc lại toàn bộ **25** / loại bỏ **0** / sửa lại trong lúc kiểm chứng **2**:
  - 1819: đếm lại bằng máy phát hiện thiếu 1 u (ず cũng tính: ず+ちゅ+う×4 = 6 u, không phải 5) — sửa "Zuchuuuu" (5u) → "Zuchuuuuu" (6u).
  - 1112: phát hiện dấu gạch trong giá trị sửa bị đổi (――→——) — sửa lại "Fu——Fua" → "Fu――Fua", giữ nguyên kiểu gạch của dòng gốc.
- Kiểm chứng bằng máy: JSON 25 = TOML block 25; jp/tw/old_vn/character khớp CSV3 (old_vn = audit fix với 4 key audit đã đổi — 1074/1085/1100/1112 — còn lại = CSV3 VN) — 0 lệch; TOML block parse được, 0 mismatch; mỗi fix chỉ khác old_vn ở đúng token rên (kiểm tra diff từng dòng); số lượng nguyên âm dài đếm bằng máy cho 1819 (6u), 1823 (8a), 1857 (11u), 1883 (4i), 1834 (9c), 1867 (15c), 1880 (10c); dash trong fix giữ nguyên kiểu của dòng gốc (file gốc trộn cả ―― và ——).

## 7. TOML block (đã parse-verified: 25 keys, 0 mismatch)

```toml
782 = "「——Ưm——Fu——A. Giống như, mỗi đêm——\\nanh nhào nặn——nhiều thế này——dâm đãng thế này——ưm.」"
784 = "「――Pua. Ừm. Đúng là liếm vào cũng không thấy kích thích gì cả.\\nKhông mùi không vị……Giống như thạch, hay giống như bánh Mizu Manju vậy.」"
1074 = "「Ya——A——Fua——Anh Sou, tetsu.」"
1085 = "「Fuuu.」"
1100 = "「Ư——A——A——A——\\nA——Aa——Ưm——Fua——」"
1110 = "「Aa――Đúng thật. Nghe em nói mới để ý.」"
1112 = "「A……Fu――Fua――Này, anh Soutetsu――Nhũ hoa――Ưm\\n――Nhũ hoa……Cái đó, nhé? Thêm nữa――Làm thêm nữa đi?」"
1114 = "「A……Hà――Ưm. Ngực――\\nTay của anh Soutetsu, trơn tuột――Nu!!」"
1121 = "「Aaa——Uu——Ku, a——Sướng, quá——\\nĐúng là râm ran——sướng thì, có sướng thật——nhưng mà.」"
1144 = "「Ư……m. Fu, fu——cảm ơn anh, Soutetsu.」"
1147 = "「Ưm……Fu, a――Không phải là hôn,\\nmà là bị liếm láp mút mát――ở gáy, cảm giác cũng mới mẻ thật.」"
1162 = "「Na!?」"
1180 = "「Aa, ra vậy. Lúc làm tình lần đầu tiên,\\nem cũng từng nói như thế nhỉ.」"
1265 = "「Dù có cho lotion vào miệng cũng――ngoạm.\\nƯm……chụt――chụt――chụụụt――Pua.」"
1296 = "「Kisaki——Cái này——Sướng thì sướng thật, nhưng——\\nĐúng là, râm ran——nôn nóng, quá, đi mất——Nu.」"
1819 = "（Liếm――liếm――chụt――Zuchuuuuu）"
1823 = "（Nichaaaaaaaa――trơn tuột!!）"
1828 = "（Trơn tuột――nhóp nhép――nhão nhoét――Nhóp nhép）"
1834 = "(Sùng sụccccccccc!!!)"
1839 = "（Cọ xát――trơn tuột――Sột soạt――nhóp nhép）"
1848 = "（Trơn tuột――cọ xát――nhóp nhép――Nhóp nhép）"
1857 = "（Nyuruuuuuuuuuu）"
1867 = "(Sùng sụccccccccccccccc!)"
1880 = "(Sùng sụcccccccccc!! Cục!!)"
1883 = "(Kuchiiii)"
```

Kết bài

Moan-fix xong file lr稀咲追加h_お風呂は日ノ本式に限るね (06_Kisaki): đọc 320/320 dòng, xét 137 dòng rên, đổi 25 dòng (fa/fu 7, romaji 9, vowel-count 6, sfx 3). JSON 25 = TOML block 25, kiểm chứng máy 0 lệch. 9 cờ F1–F9 gửi kèm unification pass. Không đụng dòng Ư gasp đã khóa; không sửa pronoun/thuật ngữ/nghĩa.
