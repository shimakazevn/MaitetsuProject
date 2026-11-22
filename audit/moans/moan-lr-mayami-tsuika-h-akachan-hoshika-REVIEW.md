# Moan-fix — lr真闇追加h_赤ちゃん、欲しか.txt.toml (05_Mayami) — 21 dòng

- **File:** `lr真闇追加h_赤ちゃん、欲しか.txt.toml` — route 05_Mayami, H-scene (Mayami muốn có em bé; sau tuần trăng mật, tập cho con bú → làm tình trong phòng ngủ vợ chồng).
- **Đọc:** 316/316 dòng (toàn bộ, đối chiếu JP + TW, CSV3); xét 183 dòng rên/SFX (103 thoại + 26 độc thoại rên + 54 SFX （ ）); **đổi 21 dòng** (18 romaji + 3 đếm nguyên âm: 1103 có 2 token trong 1 dòng; 1097 có 3 token trong 1 dòng).
- **Xây trên giá trị audit:** 7/21 dòng (1097, 1098, 1106, 1107, 1112, 1152, 1186 — chỉ đổi đúng token rên, giữ nguyên các phần khác của audit); 14 dòng audit bỏ sót (1013, 1067, 1078, 1087, 1093, 1094, 1103, 1127, 1184, 1185, 1276, 1292, 1805, 1843).
- **Không đụng:** 11 dòng gasp Ư của audit (§5 — 8 sweep + 3 sweep bỏ sót); 0 dòng "Kh" trong file (không có token Kh độc lập nào trong VN); không dòng nào chồng lên sửa đại từ/nghĩa của audit (1224, 1234 không bị sửa).

## 1. Kiểm chứng file

- **TOML:** md5 `7968856545fdf8d9adb32df40193a073` khớp audit; 1 bản duy nhất, UTF-8 BOM + CRLF, 316 key script; không có tag `%l` trong file.
- **CSV3:** 1 bộ duy nhất, 316 dòng, 316 key duy nhất, 0 VN trống; jp/tw/old_vn khớp CSV3 tuyệt đối 21/21 (old_vn trong JSON là VN gốc CSV3; fix là giá trị cuối cùng — xem §4).
- **Audit:** 132 dòng sai (41,8%) — đại từ 88 · rên 31 (§4) · gasp 11 (§5) · nghĩa 2. Moan-fix này chỉ xét lại phần rên.
- **Sweep gasp:** kiểm trực tiếp `sweep-raw-gasp-wrong.json` — 9 entry cho file này (1016, 1108, 1125, 1128, 1129, 1130, 1141, 1254, 1542), audit đã nhận cả 9; cả 9 đều là dòng Ư — không đụng, không đổi.

## 2. Kiểm kê rên (183 dòng đã xét)

- **Họ fa/fu (ふぁ/ふあ/ぷあ/ぷぁ):** 10 token (9 dòng) — 9 token chuyển romaji (§3a 7 dòng + §3e 1 dòng với 2 token ở 1106), 1 dòng đã đúng dạng romaji của audit (1100 "Fua…17a…n").
- **Họ く (くっ/んくっ/く/くはっ/かはっ/きうっ/んぎゅ):** 14 token (11 dòng) chuyển romaji (§3b); くっ diễn bằng TỪ hành động giữ nguyên (1840, 1841 — xem §4).
- **Họ や (やっ/やあっ):** 2 token — chuyển romaji (§3c).
- **Đếm nguyên âm:** 1 dòng audit bỏ sót (1103 はあっ→"Haa"; 4 dòng dài 1071/1072/1100/1163 audit đã đếm đúng — kiểm lại bằng máy: 19a / 17u+n / 17a+n / 9u+n, khớp công thức).
- **SFX （ ） (54 dòng, key 1800–1890):** diễn bằng từ VN (Trượt/Phập/Bóp/Xoáy/Phụt/Bạch…) — giữ nguyên toàn bộ trừ 2 token くっ diễn bằng âm (§3b: 1805, 1843). Độ dài lặp trong từ SFX xem cờ F1.
- **Cười (ふふっ/んふふ):** 1187, 1179, 1181, 1183, 1283, 1132 — "Ưm fufu"/"Fufu" đúng (cười, không phải rên) — giữ nguyên.

## 3. Các dòng đã sửa (21 dòng)

### 3a. Họ fa/fu → romaji (7 dòng — quy tắc duyệt 21/11 ~01:56; "phà"/"phùa" nghe gượng trong rên; tiền lệ ふかみh1/h2/h3, ハチロクh5/h6/h9, lr_ニイロクh)

#### Key 1097 — [双鉄] — moan

JP: `「ふあっ――んっっ――んくっ――く――はっ」`

TW: `「呼啊——嗯——嗯——呼——啊」`

VN cũ: `"「Phù——ưm——hự——ư——ha.」"` (giá trị audit: `"「Phùa——ưm——hự——ư——ha.」"`)

Fix: `"「Fua——ưm——ưm ku——Ku——ha.」"`

Lý do: 3 token trong 1 dòng: ふあっ → "Fua" (fa/fu → romaji); んくっ → "ưm ku" (tiền lệ ハチロクh6 852: んっ――んくっ → "ưm——ưm ku"); く → "Ku" (tiền lệ ハチロクh6 1052: く → "Ku"). Giữ "ưm" cho んっっ, "ha" cho はっ.

#### Key 1098 — [真闇] — moan

JP: `「ふあっ――ん、もうっ……まっこと、双ちゃん、\nエッチな吸い方――ばっかりで」`

TW: `「呼啊——嗯，真是的……真拿你沒辦法，吸的時候這麼色」`

VN cũ: `"「Phù——ưm, thật tình……Sou-chan,\ntoàn mút kiểu hư hỏng——không à.」"` (giá trị audit: `"「Phùa——ưm, thật tình……Sou-chan,\ntoàn mút kiểu hư hỏng——không à.」"`)

Fix: `"「Fua——ưm, thật tình……Sou-chan,\ntoàn mút kiểu hư hỏng——không à.」"`

Lý do: ふあっ → "Fua" (fa/fu → romaji).

#### Key 1106 — [真闇] — moan

JP: `「ふぁ！！――あっ！　あっ――んっ――ふ、あっ――\nそ、ちゃんっ――ン――おね、ちゃんの、くり、とりす」`

TW: `「呼啊！！——啊！啊――嗯――呼、啊――小雙——嗯——姐姐的、陰蒂」`

VN cũ: `"「Phù!!——A! A——ưm——phù, a——\nSou, chan——ưm——âm, vật, của, chị.」"` (giá trị audit: `"「Phùa!!——A! A——ưm——phù, a——\nSou, chan——ưm——âm, vật, của, chị.」"`)

Fix: `"「Fua!!——A! A——ưm——Fu, a——\nSou, chan——ưm——âm, vật, của, chị.」"`

Lý do: 2 token: ふぁ → "Fua"; dạng tách ふ、あっ → "Fu, a" (tiền lệ lr_ニイロクh 1274/1339/1392/1569, ハチロクh9 1356 — xem cờ F9 về "Fu, a" vs ハチロクh7 "phù, a").

#### Key 1107 — [真闇] — moan

JP: `「ふあっ！！！」`

TW: `「呼啊！！！」`

VN cũ: `"「Phù!!!」"` (giá trị audit: `"「Phùa!!!」"`)

Fix: `"「Fua!!!」"`

Lý do: ふあっ → "Fua" (fa/fu → romaji).

#### Key 1112 — [真闇] — moan

JP: `「あらあら、そぎゃんよかと？　ほんなら……んっ――\n…………ぷあ。よだればたっぷり、たっぷり絡めて」`

TW: `「哎呀哎呀，讓你很舒服嗎？既然這樣……嗯…………噗啊。淋上好多好多口水」`

VN cũ: `"「Ôi chà, sướng đến thế cơ à? Vậy thì……ưm——\n…………Phù. Bôi thật nhiều, thật nhiều nước bọt vào nhé.」"` (giá trị audit: `"「Ôi chà, sướng đến thế cơ à? Vậy thì……ưm——\n…………Phùa. Bôi thật nhiều, thật nhiều nước bọt vào nhé.」"`)

Fix: `"「Ôi chà, sướng đến thế cơ à? Vậy thì……ưm——\n…………Pua. Bôi thật nhiều, thật nhiều nước bọt vào nhé.」"`

Lý do: ぷあ → "Pua" (fa/fu dạng ぷ → romaji; giữ hoa P vì đầu câu sau dấu …………).

#### Key 1152 — [真闇] — moan

JP: `「ん……ぷあっ――チュッ――ちゅううっ――チュッ――\nちゅうっ――チュッ――ちゅっ――ちゅっ」`

TW: `「嗯……噗哈——啾——啾——啾——啾——啾——啾——啾」`

VN cũ: `"「Ưm……phù——chụt——chùn chụt——chụt——\nChùn chụt——chụt——chụt——chụt.」"` (giá trị audit: `"「Ưm……phùa——chụt——chụụụt——chụt——\nChùn chụt——chụt——chụt——chụt.」"`)

Fix: `"「Ưm……pua——chụt——chụụụt——chụt——\nChùn chụt——chụt——chụt——chụt.」"`

Lý do: ぷあっ → "pua" (fa/fu → romaji; giữ thường p vì giữa câu sau "Ưm……", theo quy tắc hoa/thường của lr_ニイロクh). Giữ "chụụụt" của audit cho ちゅううっ (3u).

#### Key 1186 — [双鉄] — moan

JP: `「ぷあっ！」`

TW: `「噗啊！」`

VN cũ: `"「Phù!」"` (giá trị audit: `"「Phùa!」"`)

Fix: `"「Pua!」"`

Lý do: ぷあっ → "Pua" (fa/fu dạng ぷ → romaji).

### 3b. Họ く/くは/かは/きう → romaji (11 dòng — quy tắc ハチロクh6 §3c: くっ/んくっ trong chuỗi rên → "Ku"/"Ưm ku"; "Hự" mất phụ âm k)

#### Key 1078 — [双鉄] — moan

JP: `「くはっ！」`

TW: `「啊！」`

VN cũ: `"「Hự!」"`

Fix: `"「Kuha!」"`

Lý do: くはっ = ku + ha — "Hự" mất cả hai phụ âm. Tương tự かはっ → "Kaha" (tiền lệ ハチロクh5 1181: cùng JP 「かはっ！」, "Hự!" → "Kaha!") — xem cờ F3.

#### Key 1087 — [双鉄] — moan

JP: `「ふっ――きうっ――」`

TW: `「呼——啊」`

VN cũ: `"「Phù——hự——」"`

Fix: `"「Phù——Kiu——」"`

Lý do: きうっ = ki + u — "hự" mất hẳn "ki". Sửa romaji "Kiu" theo tương tự くっ → "Ku" (h6 §3c). Giữ "Phù" cho ふっ độc lập (xem §4). Không có tiền lệ trực tiếp cho きうっ — xem cờ F2.

#### Key 1093 — [双鉄] — moan

JP: `「ふっ――くっ――！！！」`

TW: `「呼——啊！！！」`

VN cũ: `"「Phù——hự——!!!」"`

Fix: `"「Phù——Ku——!!!」"`

Lý do: くっ trong chuỗi rên → "Ku" (h6 §3c; tiền lệ ハチロクh6 897: ん――くっ → "Ưm——Ku!"). Giữ "Phù" cho ふっ độc lập.

#### Key 1094 — [双鉄] — moan

JP: `「く……ふっ――あっ」`

TW: `「啊……呼——啊」`

VN cũ: `"「Ư……phù——a.」"`

Fix: `"「Ku……phù——a.」"`

Lý do: く…… → "Ku……" ("ư" mất phụ âm k; tiền lệ ハチロクh6 §3c + ハチロクh7 485: く…… → "Ku……"). Giữ "phù" cho ふっ, "a" cho あっ.

#### Key 1127 — [真闇] — moan

JP: `「はっ！　んぎゅ！　くっ――は――杭打ち、され、て、\nおね、ちゃんっ――刻印っ――双ちゃん――にっっ」`

TW: `「呼！嗯呀！啊——被打樁、了、姐、姐——刻印——小雙——」`

VN cũ: `"「Ha! Ưm! Hự——ha——bị đóng cọc, rồi,\nchị——được khắc dấu ấn——của Sou-chan——rồi.」"`

Fix: `"「Ha! Ngyu! Ku——ha——bị đóng cọc, rồi,\nchị——được khắc dấu ấn——của Sou-chan——rồi.」"`

Lý do: 2 token: んぎゅ → "Ngyu" (tiền lệ ポーレットh2 928: んぎゅっ → "Ngyu"); くっ → "Ku" (h6 §3c). Giữ "Ha" cho はっ.

#### Key 1184 — [双鉄] — moan

JP: `「かはっ！！」`

TW: `「咳！！」`

VN cũ: `"「Hự!!」"`

Fix: `"「Kaha!!」"`

Lý do: かはっ = ka + ha — "Hự" mất cả hai phụ âm. Tiền lệ trực tiếp: ハチロクh5 1181, cùng JP 「かはっ！」, "Hự!" → "Kaha!".

#### Key 1185 — [双鉄] — moan

JP: `「くはっ！！！！！！」`

TW: `「咳！！！！！！」`

VN cũ: `"「Hự!!!!!!」"`

Fix: `"「Kuha!!!!!!」"`

Lý do: くはっ = ku + ha — "Hự" mất cả hai phụ âm. Tương tự かはっ → "Kaha" (h5 1181) — xem cờ F3.

#### Key 1292 — [双鉄] — moan

JP: `「真闇姉も、だっ――くっ――はっ――\nじゅくじゅくで、どろ、どろ、で――」`

TW: `「真闇姐也是、啊——嗯——呼——濕漉漉的、黏糊糊的、」`

VN cũ: `"「Chị Mayami cũng, vậy——hự——ha——\nƯớt sũng, nhầy, nhụa, rồi——」"`

Fix: `"「Chị Mayami cũng, vậy——Ku——ha——\nƯớt sũng, nhầy, nhụa, rồi——」"`

Lý do: くっ trong chuỗi rên → "Ku" (h6 §3c; tiền lệ ハチロクh6 514: んっ――くっ → "ưm——Ku"). Giữ "ha" cho はっ.

#### Key 1805 — [monologue] — SFX

JP: `（む。くっ――ぷりっ！　む。――くっ――ぷりゅん！）`

TW: `（嗚。嗯——噗！嗚。——嗯——噗！）`

VN cũ: `（Mút. Hự——nhả! Mút.——Hự——bật ra!）`

Fix: `（Mút. Ku——nhả! Mút.——Ku——bật ra!）`

Lý do: くっ ×2 diễn bằng âm → "Ku" (tiền lệ ポーレットh5 1733: SFX （ぐッ――ぐりゅっ――くっ――んっ――） → "（Hự——ngoáy——Ku——ưm——）"). Giữ các từ hành động "Mút/nhả/bật ra" cho む/ぷりっ/ぷりゅん (xem §4).

#### Key 1843 — [monologue] — SFX

JP: `（ずっ――りゅっ――くっ――むにゅっっ）`

TW: `（滋——溜——嗯——扭）`

VN cũ: `（Lún——trượt——hự——mềm）`

Fix: `（Lún——trượt——Ku——mềm）`

Lý do: くっ diễn bằng âm → "Ku" (cùng tiền lệ ポーレットh5 1733). Giữ các từ hành động "Lún/trượt/mềm".

### 3c. Họ や → romaji (2 dòng — tiền lệ ハチロクh6 816: や → "Ya")

#### Key 1013 — [真闇] — moan

JP: `「だめっ――やっ、めっ――イっちゃうの――やあっ！\nおねえ、ちゃん――双ちゃんっ――双ちゃんとぉぉ！」`

TW: `「不行——呀、嗎——要去了——呀！姐、姐——小雙——小雙！！」`

VN cũ: `"「Không được——dừng, lại——ra mất——á!\nChị——Sou-chan——cùng với Sou-chan cơ!」"`

Fix: `"「Không được——dừng, lại——ra mất——yaa!\nChị——Sou-chan——cùng với Sou-chan cơ!」"`

Lý do: やあっ (tiếng thét lên đỉnh) → "yaa" (ya + a = 2 a theo công thức; "á" mất phụ âm y). Giữ "dừng, lại" cho やっ、めっ (đó là từ やめる tách ra, diễn bằng nghĩa — đúng). Hoa/thường theo VN cũ ("á" thường → "yaa" thường).

#### Key 1067 — [真闇] — moan

JP: `「やっ――らめっ――そう、ちゃんっ――ッッ――\nもう、おね、ちゃん――できあがっとる――けんっっ」`

TW: `「呀——別——小雙——嗯——我、姐、姐——已經準備好了——」`

VN cũ: `"「A——không được——Sou, chan——\nChị——đã sẵn sàng——lắm rồi——」"`

Fix: `"「Ya——không được——Sou, chan——\nChị——đã sẵn sàng——lắm rồi——」"`

Lý do: やっ (thán từ "ya!") → "Ya" (tiền lệ ハチロクh6 816). Giữ "không được" cho らめっ. ッッ―― sau そう、ちゃんっ xem cờ F5 (gasp, không sửa ở đây).

### 3d. Đếm nguyên âm (1 dòng audit bỏ sót)

#### Key 1103 — [真闇] — moan

JP: `「はあっ！　んっ！　ひゅっ――んあっ！！\nきたっ！　きたっ！　きたっ！　きたあっ！！！！」`

TW: `「呼啊！嗯！咻——嗯啊！！來了！來了！來了！來了！！！！」`

VN cũ: `"「Ha! Ưm! Hyu——ưm a!!\nĐến rồi! Đến rồi! Đến rồi! Đến rồi!!!!」"`

Fix: `"「Haa! Ưm! Hyu——Na!!\nĐến rồi! Đến rồi! Đến rồi! Đến rồi!!!!」"`

Lý do: 2 token: はあっ (2 a) → "Haa" (VN cũ "Ha" mất 1 a); んあっ → "Na" (một âm "na"; tiền lệ ハチロクh6 843: んぁ → "Na", bản cũ "ưm a" tách mảnh). Giữ "Hyu" cho ひゅっ (đã đúng romaji).

### 3e. Dạng tách fa (1 dòng audit bỏ sót)

#### Key 1276 — [真闇] — moan

JP: `「準備――ん……っふ、あ――\nおね、ちゃんの――からだも――こころ、も――」`

TW: `「準備——嗯……呼、啊——姐、姐的——身體也——心、也——」`

VN cũ: `"「Chuẩn bị——ưm……phù, a——\nCơ thể——của chị——cả trái tim, nữa——」"`

Fix: `"「Chuẩn bị——ưm……Fu, a——\nCơ thể——của chị——cả trái tim, nữa——」"`

Lý do: dạng tách ふ、あ → "Fu, a" (cùng tiền lệ §3a 1106; lr_ニイロクh, ハチロクh9). っ trước ふ xem cờ F4 (gasp, không sửa ở đây).

## 4. Đã kiểm chứng và giữ nguyên (không sửa)

- **Audit §4 đã đúng, giữ nguyên toàn bộ giá trị audit (24 dòng):** 1070 "Kya.", 1071 "Uya" 19a ✓ (đếm máy: あ×18 + "ya" = 19 a), 1072 "Hyau…17u…n" ✓ (đếm máy: う/ぅ×17 + ん), 1073 "Kyafu!!!!", 1076 "Kyan!", 1077 "Kya!?", 1096 "Haa" ×4 (2a mỗi cái), 1100 "Fua…17a…n" ✓ (đếm máy: あ/ぁ×17 + ん), 1121 "Afu!!!", 1124 "An.", 1135/1136/1145 "chụụụt" (ちゅううっ 3u, tiền lệ ハチロクh3), 1140 "Phùu!!" (ふうっ 2u), 1143 "Muuu." (むううっ 3u), 1147 "chụụụụt" (ちゅるううっっ 4u), 1148 "haa." (はぁっ 2a), 1156 "Nkyu!!!!!", 1163 "Nkyuuuuuuuuun!!!!" ✓ (đếm máy: んきゅ + う×8 = 9 u + ん), 1164 "Nuuu.", 1165 "Nmuu.", 1166 "phùu." (ふうっ 2u), 1313 "Phùuu!!!" (ふううっ 3u), 1318 "Uu" (ううっ 2u).
- **Đã đúng dạng romaji từ VN gốc (2 dòng):** 1075 ひゃうんっ → "Hyaun!", 1168 んひゅっっっ → "Nhyu!!!!!!".
- **Grunt ngắn giữ nguyên theo quy ước của file (audit §7):** ふっ/フッ độc lập → "phù" (1086, 1087, 1093, 1094, 1095, 1102, 1148, 1149, 1160, 1166, 1193, 1214, 1218 — chỉ sửa khi là dạng tách fa hoặc trong chuỗi có くっ); むっ/うっ → "hự"/"Ưm" (1139, 1140, 1142, 1143, 1160, 1166, 1169, 1170); んう/んむ/んフ → "Ưm" (1160, 1162, 1167, 1170, 1171); ぐっ → "Hự" (1018, 1816, 1889 — tiền lệ ポーレットh5 1733 giữ ぐッ → "Hự"); くっ diễn bằng TỪ hành động → giữ (1840 "Bóp——nắn——xoa", 1841 "Nắn——bóp——nhào", 1804 "Tuốt——tuốt——chà——tuột——").
- **Họ ちゅう / れる giữ nguyên:** ちゅうっ (2u) → "chùn chụt" (2u, khớp đếm — 1820, 1821, 1861, 1152); ちゅぶっ/ちゅむっ/ちゅずずっ → "chụt"/"chùn chụt"; れる/れろ → "liếm" (1135, 1145, 1162, 1177, 1879).
- **Thán từ / từ có sẵn:** あ/ぁ → "A" (1119, 1120); ん → "Ưm" (1155, 1175, 1275, 819, 1219); はぁい → "Vâng ạ" (1187 — từ はい, không phải rên); あはっ → "Aha" (1123); ああ đầu câu → "A" (1132); ふふっ/んふふ → "Fufu"/"Ưm fufu" (1179, 1181, 1183, 1283, 1132 — cười).
- **Gasp Ư (audit §5):** 11 dòng không đụng — 1016, 1086, 1108, 1125, 1128, 1129, 1130, 1141, 1214, 1217, 1254.
- **Không có dòng "Kh" nào trong file; không có dòng rên nào chồng lên sửa đại từ/nghĩa của audit.**

## 5. Lượt soát 2 (second pass)

- Đọc lại **21/21** fix value đối chiếu JP (+TW làm chứng): đếm nguyên âm kiểm lại bằng máy cho 1071 (19a), 1072 (17u+n), 1100 (17a+n), 1163 (9u+n), 1103 (はあっ 2a), 1127/1097/1292 (くっ → Ku), 1013 (やあっ 2a).
- Kiểm tra diff cơ học 21/21: mỗi fix chỉ khác VN cũ ở đúng token rên cần sửa (xem §3); 7 dòng chồng audit — diff với giá trị audit cũng chỉ chạm đúng token rên.
- **Lượt soát 2: 21 tổng / 21 tái kiểm chứng / 0 bỏ / 0 sửa.** (1139 đã loại ở lượt 1 — đọc nhầm với 1140: 1139 là 「むっ――うっ――」 không có ふうっ; 1140 đã được audit sửa "Phùu".)

## 6. Cờ cho đợt thống nhất / parent xác nhận

- **F1 — Độ dài lặp trong SFX （ ） diễn bằng từ:** audit §7 đã ghi (1824 "Siết" + 32 t cho 18 mora u; 1850 "dàiiiiiiiii" 10 i cho 7 u; 1815 10 i cho 11 u; 1877 れるうううっっ → "liếm liếm" mất độ dài; 1162 れるうっっ → "liếm liếm"; 1818 れるれるれるれるっ → "liếm liếm liếm liếm") — giữ nguyên ở đây theo tiền lệ lr_ニイロクh F1 (diễn bằng lời cảm tính, chưa có quy tắc khóa cho số lần lặp phụ âm/nguyên âm trong từ SFX).
- **F2 — 1087 きうっ → "Kiu":** chỉ có tương tự (くっ → "Ku", h6 §3c), không có tiền lệ trực tiếp cho きうっ trong các file moan đã gộp. Parent xác nhận.
- **F3 — 1078/1185 くはっ → "Kuha":** tương tự かはっ → "Kaha" (h5 1181, tiền lệ trực tiếp cho dạng ka); dạng ku chưa có tiền lệ trực tiếp. Parent xác nhận.
- **F4 — 1276 っふ:** っ trước ふ có thể là gasp bị mất (VN không có Ư) — audit §7 giữ 1095 với lý do tương tự ("dấu gạch sau đã diễn sự ngắt"). Đây là câu hỏi gasp, không sửa ở vòng moan.
- **F5 — 1067 ッッ――:** sau そう、ちゃんっ — có thể là gasp nghẹn bị mất; audit §5 không gồm dòng này. Câu hỏi gasp, không sửa ở vòng moan.
- **F6 — Ranh giới grunt-vs-rên (họ く):** audit §7 giữ quy ước grunt "hự" cho く/む ngắn; vòng moan này đã ghi đè cho các token くっ/んくっ/く/くはっ/かはっ/きうっ DIỄN BẰNG ÂM trong chuỗi rên (theo h6 §3c + h5 1181 + ポーレットh5 1733), nhưng giữ "hự"/"Ưm" cho grunt thuần (むっ/うっ/ぐっ/んう/んむ/んフ) và cho くっ diễn bằng TỪ hành động (1840/1841). Ranh giới này chờ quyết chung ở đợt thống nhất.
- **F7 — Dạng tách fa "Fu, a" vs ハチロクh7 "phù, a":** đã cờ ở lr_ニイロクh F2, vẫn mở — file này dùng "Fu, a" (1106, 1276) theo đa số file đã gộp.
- **F8 — 1103 んあっ → "Na" + 1013/1067 や → "Ya"/"Yaa":** theo tiền lệ h6 843 (んぁ → "Na") và h6 816 (や → "Ya"); họ や chưa nằm trong quy tắc khóa ひゃ-family 21/11 — parent xác nhận phạm vi.
- **F9 — 7 dòng thay thế giá trị audit cùng key:** 1097, 1098, 1106, 1107, 1112, 1152, 1186 — áp MỘT giá trị moan cho mỗi key ở đợt build, không áp cả hai.
- **F10 — 1095:** audit §7 giữ nguyên (っ kết thúc âm ん…… dài, dấu gạch sau đã diễn sự ngắt) — không sửa, ghi nhận theo quyết định của audit.

## 7. Khối TOML đã parse-kiểm chứng (21 khóa, 0 sai lệch giá trị so với JSON)

Khối TOML bên dưới đã được parse bằng tomllib: 21 khóa, 0 sai lệch giá trị so với JSON fix. Các `\n` trong value là ký tự xuống dòng thật của CSV3 (TOML escape `\\n`).

```toml
[script]
1013 = "\"「Không được——dừng, lại——ra mất——yaa!\\nChị——Sou-chan——cùng với Sou-chan cơ!」\""
1067 = "\"「Ya——không được——Sou, chan——\\nChị——đã sẵn sàng——lắm rồi——」\""
1078 = "\"「Kuha!」\""
1087 = "\"「Phù——Kiu——」\""
1093 = "\"「Phù——Ku——!!!」\""
1094 = "\"「Ku……phù——a.」\""
1097 = "\"「Fua——ưm——ưm ku——Ku——ha.」\""
1098 = "\"「Fua——ưm, thật tình……Sou-chan,\\ntoàn mút kiểu hư hỏng——không à.」\""
1103 = "\"「Haa! Ưm! Hyu——Na!!\\nĐến rồi! Đến rồi! Đến rồi! Đến rồi!!!!」\""
1106 = "\"「Fua!!——A! A——ưm——Fu, a——\\nSou, chan——ưm——âm, vật, của, chị.」\""
1107 = "\"「Fua!!!」\""
1112 = "\"「Ôi chà, sướng đến thế cơ à? Vậy thì……ưm——\\n…………Pua. Bôi thật nhiều, thật nhiều nước bọt vào nhé.」\""
1127 = "\"「Ha! Ngyu! Ku——ha——bị đóng cọc, rồi,\\nchị——được khắc dấu ấn——của Sou-chan——rồi.」\""
1152 = "\"「Ưm……pua——chụt——chụụụt——chụt——\\nChùn chụt——chụt——chụt——chụt.」\""
1184 = "\"「Kaha!!」\""
1185 = "\"「Kuha!!!!!!」\""
1186 = "\"「Pua!」\""
1276 = "\"「Chuẩn bị——ưm……Fu, a——\\nCơ thể——của chị——cả trái tim, nữa——」\""
1292 = "\"「Chị Mayami cũng, vậy——Ku——ha——\\nƯớt sũng, nhầy, nhụa, rồi——」\""
1805 = "（Mút. Ku——nhả! Mút.——Ku——bật ra!）"
1843 = "（Lún——trượt——Ku——mềm）"
```

## 8. Kết bài

File lr真闇追加h_赤ちゃん、欲しか.txt.toml: 316 dòng đã đọc toàn bộ đối chiếu JP + TW, 183 dòng rên/SFX đã xét, **đổi 21 dòng** — 7 dòng xây trên giá trị audit (chỉ đổi đúng token rên: fa/fu → romaji), 14 dòng audit bỏ sót (họ く 8 dòng, họ や 2 dòng, đếm nguyên âm 1 dòng, dạng tách fa 1 dòng, SFX くっ 2 dòng — 1097 tính 1 dòng cho cả 3 token; tổng 27 token rên đã đổi). Không lệch dòng, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Sweep gasp kiểm tra trực tiếp 9/9 mục — đều là dòng Ư của audit, không đụng. Không dòng "Kh" nào bị đổi (file không có). JSON 21 mục, khóa string, khối TOML 21 khóa parse OK, 0 sai lệch; jp/tw/old_vn khớp CSV3 21/21; lượt soát 2: 21/21/0/0. 10 cờ cho đợt thống nhất (F1–F10, xem §6).
