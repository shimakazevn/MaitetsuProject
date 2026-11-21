# Moan-fix れいなh4 — れいなh4_ふたりっきりのハロウィン.txt.toml

**Ngày:** 21/11/2026

**Tệp TOML:** `04_Reina/れいなh4_ふたりっきりのハロウィン.txt.toml` — md5 `43ddc25620d65d8d021ab6e6572b5caa` (khớp md5 audit), 115.354 byte, BOM + CRLF, `[selections]` rỗng, **không có bản sao trùng** (audit đã kiểm tra md5 toàn bộ 227 tệp).

**Nguồn CSV:** "Trang tính 3" — bộ hàng duy nhất `04_Reina`, 584 hàng `[script]`, key 54–3291, 0 VN rỗng, 0 key trùng. VN khớp TOML 584/584 sau chuẩn hóa `\n` (audit đã kiểm chứng; kiểm tra lại bằng máy ở đợt này: flat-match 584/584, 0 khác biệt thực chất).

**Kết quả: 43 dòng rên đổi** (34 romaji fa/fu + 9 sửa mới: 5 đếm nguyên âm + 2 gasp audit bỏ sót + 2 đếm ちゅ). Audit trước đó: 59/584 sai — đợt moan này chỉ chạm phần rên; các fix nghĩa/thuật ngữ/xưng hô của audit giữ nguyên, không đụng.

## 1. Xác minh tệp

- TOML md5 khớp audit (`43ddc25620d65d8d021ab6e6572b5caa`); không có bản trùng — fix áp cho 1 bản duy nhất.
- CSV3: 1 bộ duy nhất, không bẫy dual-set. Đã đọc 584/584 dòng (toàn bộ file, không chỉ dòng ứng viên).
- Sweep っ: kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` — file này có 5 mục (1963, 1990, 2022, 2972, 3095), cả 5 audit đã áp nguyên và kiểm chứng đúng — đợt moan KHÔNG đụng dòng nào. Audit tìm thêm 1 gasp sweep bỏ sót (1962, cả dòng っ――！) — cũng đúng, không đụng.
- Không dòng "Kh" nào trong file (kiểm tra bằng máy: 0 dòng chứa "Kh" là rên っ) — không có gì để giữ/đổi theo quyết định khóa 21/11.

## 2. Kiểm kê rên (đã đọc 584/584 dòng)

Các nhóm chồng lấn nhau; tổng dòng rên/SFX xét ~200 dòng:

| Nhóm | Dòng | Đổi | Giữ |
|---|---|---|---|
| fa/fu (ふぁ/ふあ/ふぇ/ふや/ふっ/ふ、) | 34 dòng / 46 token (audit §3.1) | 34 (về romaji) | 0 |
| ひゃ/ひあ/ひゅ/きゃ/きゅ | 35 | 2 (1885, 1999: ひあ "Hya"→"Hia") | 33 |
| Gasp Ư (sweep 5 + audit 1962) | 6 | 0 (đã đúng) | 6 |
| Gasp audit bỏ sót | 2 | 2 (1988, 2459-final) | 0 |
| Cười うふふぅ/えへへ | 15 | 0 (3 dòng audit đã sửa "Ufufu~" đúng; còn lại đã đúng) | 15 |
| Rên dài đếm nguyên âm (あ/う chains) | 20 | 4 (1979, 1984, 2044, 2155) + 3 trong nhóm fa/fu (1967, 1986, 2458) | 13 |
| SFX miệng ちゅ/れる/ぺろ/かぷ | 30 | 3 (1994, 2043, 2047) | 27 |
| SFX độc thoại （ ） | 30 | 0 (giữ theo quy ước file, xem cờ F3) | 30 |
| Hơi thở tập thở すう/はあ (không phải rên) | 5 | 0 (xem cờ F4) | 5 |

**Quyết định chung cho 34 dòng fa/fu:** toàn bộ 34 dòng đều nằm trong cảnh H (key 1784–2459, Reina đang rên) — "phà/phùa/phuê/phuya/phù" trong chuỗi rên cao trào nghe ngượng, nên đưa TẤT CẢ về romaji theo quy tắc fallback Hieu duyệt 21/11 ~01:56. Bản VN cũ vốn đã là La-tinh ("Fua"/"fua"/"Fe"/"Fuya") — audit (trước quy tắc romaji) đã Việt hoá chúng; đợt moan này hoàn lại dạng La-tinh, KHÔNG phải dịch mới. Dùng Hepburn chặt Fa (ふぁ) / Fua (ふあ) / Pa (ぷぁ) / Pua (ぷあ) / Fue (ふぇ) / Fuya (ふや), theo đa số tiền lệ đã gộp (凪h2, lr-h2, lr_ふかみh1, lr-h1, h7, lr-jiekei) — khác h8 (dùng "Fua" cho cả ふぁ), xem cờ F1. 5 dòng hoàn lại đúng VN cũ từng chữ (2015, 2452, 2453, 2454, 2457 — audit chỉ đổi đúng token fa/fu); các dòng còn lại khác VN cũ ở đếm nguyên âm hoặc ở token ひあ (xem §3).

## 3. Chi tiết từng dòng sửa (43 dòng)

Ký hiệu: ⏎ = ký tự xuống dòng dạng backslash-n trong JSON/TOML (game tự wrap).

### 3a. Romaji fa/fu — 34 dòng (đổi ngược fix audit về La-tinh)

Bảng này ghi token rên của từng dòng; giá trị fix đầy đủ xem `moan-reinah4-futarikkiri-halloween-wrong.json` + khối TOML §7. Tất cả các fix chỉ khác giá trị audit ở đúng token rên (đã kiểm chứng bằng difflib 34/34), trừ 4 dòng có sửa thêm đếm/gasp (1967, 1986, 2458, 2459 — xem §3b).

| Key | JP (token rên) | TW | Token audit | Token moan | Ghi chú |
|---|---|---|---|---|---|
| 1784 | ふあっ | 蛤啊 | phù | Fua | |
| 1835 | ふあっ | 蛤啊啊啊啊 | phù | Fua | |
| 1885 | ひあっ + ふあっ | 呀啊啊 | Hya + phù | Hia + Fua | ひあ→Hia theo quy tắc họ ひゃ 21/11 |
| 1890 | ふぇっ | 咦 | Phuê | Fue | VN cũ "E" sai âm |
| 1894 | ふぇ？ + ふぁぁっ | 咦？啊……哇 | Phuê? + phàa | Fue? + Faa | ふぁぁっ = 2a |
| 1936 | ふっ | 哈嗯……啊 | phù | Fu | |
| 1938 | ふぇ――ふやっ | 哎呀…… | Phuê——phuya | Fue——Fuya | |
| 1967 | ふあっ + ふやぁ | 蛤啊……啊啊啊 | phù + phuya | Fua + Fuyaa | ふやぁ = 2a, audit "phuya" thiếu 1a (xem §3b) |
| 1969 | ふぁ…… | 啊…… | Phà…… | Fa…… | Hơi thở mềm giữa cảnh H, vẫn là rên |
| 1976 | ふぇ + ふ、あ | 蛤啊、好舒服 | phuê + phù, a | Fue + Fu, a | ふ、あ là 2 hơi riêng, giữ tách |
| 1978 | ふあ | 啊啊啊啊 | phùa | Fua | |
| 1983 | ふやあああんっ + ふぁ | 蛤啊，現在也是 | Phuyaaaan + Phà | Fuyaaaan + Fa | ふやあああ = 4a + n |
| 1986 | ふあっ + ふぁぁぁっん | 啊啊啊 | Phù + Phàaan | Fua + Faaaan | ふぁぁぁっん = 3a + n, VN cũ thừa 1a (xem §3b) |
| 1999 | ひあっ + ふぁ | 啊嗯……嗯 | Hya + phà | Hia + Fa | ひあ→Hia theo quy tắc họ ひゃ 21/11 |
| 2000 | ふあっ | 蛤啊……啊 | phù | Fua | Giữ "Fuyu" (ふゆっ) và "hyu" (ひゅっ) |
| 2001 | ふあ ×2 | 蛤啊……蛤啊 | phùa ×2 | Fua ×2 | |
| 2004 | ふあっ | 蛤啊……啊 | phù | Fua | |
| 2005 | ふっ + ふ、あ | 蛤啊……啊嗯 | phù + phù, a | Fu + Fu, a | |
| 2013 | ふあっ | 蛤啊……啊 | phù | Fua | Giữ "Á"/"á" cho あっ (không phụ âm mora) |
| 2015 | ふっ | 啊啊啊……嗚嗚 | Phù | Fu | Hoàn lại đúng VN cũ; giữ "Kyufu" (きゅふっ) |
| 2017 | ふあっ | 蛤啊 | phù | Fua | |
| 2088 | ふっ + ふあっ | 蛤啊、啊 | phù + phù | Fu + Fua | |
| 2134 | ふっ | 好……好激烈 | phù | Fu | Giữ "n-a" cho んあっ |
| 2172 | ふあっ | 蛤啊啊 | phù | Fua | |
| 2202 | ふあっ | 蛤啊啊 | phù | Fua | |
| 2451 | ふぁ―― | 蛤啊……不行 | Phà | Fa | |
| 2452 | ふあっ | 蛤啊 | Phù | Fua | Hoàn lại đúng VN cũ |
| 2453 | ふあっ | 蛤啊……啊 | Phù | Fua | Hoàn lại đúng VN cũ |
| 2454 | ふあぁ | 蛤啊 | Phùaa | Fuaa | ふあぁ = 2a; hoàn lại đúng VN cũ |
| 2455 | ふやっ + ふあっ | 蛤啊……蛤啊 | Phuya + phù | Fuya + Fua | |
| 2456 | ふぁあっ | 蛤啊 | Phàa | Faa | ふぁあっ = 2a |
| 2457 | ふあ……ぁ……ぁ | 蛤啊啊啊、啊啊啊 | Phùa……a……a | Fua……a……a | Giữ "a……a……ya" cho ぁ……ぁ……やぁ |
| 2458 | ふあああぁぁぁ + ふああ | 蛤啊啊啊啊 | Phùaaaaaa + Phùaa | Fuaaaaaa + Fuaa | Token 1 = 6a, VN cũ chỉ 5a (xem §3b) |
| 2459 | ふあっ！ + ふあっ――あっ | 蛤啊！啊！…蛤啊啊 | Phù! + phù——a | Fua! + Fua——aƯ | あっ cuối dòng → aƯ (xem §3b) |

### 3b. Sửa mới + sửa thêm đếm/gasp trong nhóm fa/fu (13 dòng)

**1967 [れいな] — romaji + đếm nguyên âm**
JP: 「や――れいな――おしっ、こ――おもら、し――⏎ふあっ――あっ――まだ――出ちゃ、う――ふやぁ」
TW: 「啊……玲奈……蛤啊……又要尿出來了……啊啊啊」
Cũ: 「A——Reina——tè, dầm——mất, rồi——⏎fua——a——vẫn——còn ra, nữa——fuya」
Mới: 「A——Reina——tè, dầm——mất, rồi——⏎Fua——a——vẫn——còn ra, nữa——Fuyaa」
Lý do: ふあっ→"Fua"; ふやぁ = ふ+や+ぁ = 2 âm a → "Fuyaa". Giá trị audit "phuya" (1a) và VN cũ "fuya" (1a) đều thiếu 1 âm a theo công thức đếm (tiền lệ audit §5: ふあぁ→"Phùaa" 2a).

**1979 [れいな] — đếm nguyên âm**
JP: 「ひゅああああああああああああぁぁぁぁんっ！！！」
TW: 「啊啊啊啊啊啊啊啊啊！！！」
Cũ: 「Hyuaaaaaaaaaaaaaaaaaan!!!」
Mới: 「Hyuaaaaaaaaaaaaaaaan!!!」
Lý do: JP = ひゅ (1u) + あ×12 + ぁ×4 = 16 âm a + ん. VN cũ có 18 âm a (đếm bằng máy), thừa 2 → bớt 2 âm a. "!!!" diễn っ (tiền lệ lr-h3 1224).

**1984 [れいな] — đếm nguyên âm**
JP: 「ふゅぅぅぅぅううんっ！！！」
TW: 「啊啊啊啊啊！！！」
Cũ: 「Fyuuuuuun!!!」
Mới: 「Fyuuuuuuun!!!」
Lý do: JP = ふゅ (1u) + ぅ×4 + う×2 = 7 âm u + ん. VN cũ có 6 âm u (đếm bằng máy), thiếu 1 → thêm 1 âm u.

**1986 [れいな] — romaji + đếm nguyên âm**
JP: 「ひゃっ！　うっ！　ふあっ！　これっ！　これっ！⏎しゅごっ――んっ――ひっ――ふぁぁぁっん！！！」
TW: 「啊啊啊！啊啊！啊啊啊！這樣……好舒服……呀啊啊！！！」
Cũ: 「Hya! Ư! Fua! Cái này! Cái này!⏎Tuyệt quá——ưm——hi——fuaaaan!!!」
Mới: 「Hya! Ư! Fua! Cái này! Cái này!⏎Tuyệt quá——ưm——hi——Faaaan!!!」
Lý do: ふあっ→"Fua"; ふぁぁぁっん = ふぁ (1a) + ぁ×2 = 3 âm a + ん → "Faaaan". VN cũ "fuaaaan" có 4 âm a (thừa 1); audit "Phàaan" đếm đúng 3a — đợt moan giữ đúng số đếm của audit, chỉ đổi token sang romaji.

**1988 [れいな] — gasp (audit bỏ sót)**
JP: 「はぅうっ」
TW: 「啊嗚」
Cũ: 「Hauu」
Mới: 「HauuƯ」
Lý do: っ cuối tuyệt đối, không dấu câu sau — âm っ mất hẳn trong VN cũ ("Hauu"). Theo ranh giới gasp đã khóa (chỉ thêm Ư khi っ hoàn toàn mất) + tiền lệ lr-h2 1567 (moan thêm gasp audit sót "aƯ", parent đã giữ lúc gộp). Quét cơ học toàn bộ dòng JP kết thúc bằng っ trần: chỉ 1988 và 2459-final là rên mất gasp (2459 xem riêng dưới) — các dòng khác là っ nhấn mạnh trên từ nội dung (1813 へっ, 2356 にっ, 2426 たくさんっ — tiền lệ sweep 1474: không thêm Ư) hoặc đã có dấu diễn (1989 はうう！→"Hauu!").

**1994 [れいな] — đếm nguyên âm (chuỗi hôn)**
JP: 「アムッ――ちゅっ――ちゅっ――ちゅううっ！」
TW: 「啊嗯……啾……啾！」
Cũ: 「Am——chụt——chụt——chụt!」
Mới: 「Am——chụt——chụt——chụụụt!」
Lý do: ちゅううっ = ちゅ (1u) + う×2 = 3 âm u → "chụụụt". VN cũ "chụt" mất 2 âm u. Tiền lệ Paulette h3 đã gộp (931/933/942: ちゅううっ→"chụụụt"). 2 token ちゅっ đầu giữ "chụt" (1u + t diễn っ, đúng).

**2021 [れいな] — đếm nguyên âm (số ん)**
JP: 「んひゃんっっっ！！！」
TW: 「啊嗯！！！」
Cũ: 「Nhyannn!!!」
Mới: 「Nhyan!!!」
Lý do: JP = ん + ひゃ + ん = 2 âm ん → "Nhyan" (2 chữ n). VN cũ "Nhyannn" có 4 chữ n (thừa 2). っ×3 diễn bằng "!!!" (tiền lệ lr-h3 1224: ふあっっっっ→"Fua!!!!!"). Tiền lệ んひゅん→"Nhyun" (凪h2 2512).

**2043 [れいな] — đếm nguyên âm (chuỗi hôn)**
JP: 「ぺろっ――ちゅううっ――ぺろぺろ――かぷっ！」
TW: 「啾嚕……啾嚕嚕……啊呜！」
Cũ: 「Liếm——chụt——liếm liếm——cạp!」
Mới: 「Liếm——chụụụt——liếm liếm——cạp!」
Lý do: Như 1994: ちゅううっ = 3 âm u → "chụụụt". Các token còn lại giữ nguyên (ぺろっ→"Liếm", ぺろぺろ→"liếm liếm", かぷっ→"cạp!" — diễn nghĩa đã chốt trong file).

**2044 [れいな] — đếm nguyên âm**
JP: 「きゅふううううううううんっ！！！」
TW: 「嗚嗚嗚嗚嗚！！！」
Cũ: 「Kyufuuuuuuuun!!!」
Mới: 「Kyufuuuuuuuuun!!!」
Lý do: JP = きゅ (1u) + ふ (1u) + う×8 = 10 âm u + ん. VN cũ có 9 âm u (đếm bằng máy), thiếu 1 → thêm 1 âm u.

**2047 [れいな] — đếm nguyên âm (chuỗi hôn)**
JP: 「ん……ちゅっ――ちゅうっ――ちゅむっ――ん……⏎しゅき……んっ――ちゅっ――ほうへふ……はぁん」
TW: 「嗯……啾……啾嚕……愛你……嗯……啾……哈嗯」
Cũ: 「Ưm……chụt——chụt——chụt——ưm……⏎yêu……ưm——chụt——Soutetsu……haan」
Mới: 「Ưm……chụt——chụụt——chumu——ưm……⏎yêu……ưm——chụt——Soutetsu……haan」
Lý do: Ba âm JP khác nhau bị diễn giống hệt "chụt" — mất âm: ちゅうっ = 2u → "chụụt"; ちゅむっ → "chumu" (mất hẳn む trong "chụt"). Tiền lệ Paulette h3 đã gộp (914/931: ちゅむっ→"chumu"; ちゅうっ→"chụụt"). Giữ "Soutetsu" cho ほうへふ (nói ngọng, audit giữ) và "haan" cho はぁん (2a, đúng).

**2155 [れいな] — đếm nguyên âm (tiếng rên thất vọng, ngoài cảnh H)**
JP: 「おばけ！　やっぱり、かそうって……⏎ううう、れいな、でも、もったいないって思うです」
TW: 「妖怪！化裝果然是要………嗚嗚嗚……可是玲奈覺得好捨不得」
Cũ: 「Ma! Quả nhiên, hóa trang thì……⏎Uuuu, nhưng mà, Reina thấy tiếc lắm ạ~」
Mới: 「Ma! Quả nhiên, hóa trang thì……⏎Uuu, nhưng mà, Reina thấy tiếc lắm ạ~」
Lý do: JP ううう = 3 âm u; VN cũ "Uuuu" có 4 âm u, thừa 1 → bớt 1.

**2458 [れいな] — romaji + đếm nguyên âm**
JP: 「ふあああぁぁぁ――れいな、そうてつ、さんの――⏎おくち、に――んきゅっ！？　ふああ――あんっ！！」
TW: 「蛤啊啊啊啊……玲奈……往雙鐵先生的嘴裡……啊啊啊啊！！」
Cũ: 「Fuaaaaa——Reina, vào miệng——⏎anh Soutetsu——nkyu!? Fuaa——an!!」
Mới: 「Fuaaaaaa——Reina, vào miệng——⏎anh Soutetsu——nkyu!? Fuaa——an!!」
Lý do: Token 1: ふあああぁぁぁ = ふあ (1a) + あ×2 + ぁ×3 = 6 âm a → "Fuaaaaaa". VN cũ "Fuaaaaa" chỉ 5a (thiếu 1); audit "Phùaaaaaa" đếm đúng 6a — đợt moan giữ đúng số đếm của audit, chỉ đổi token sang romaji. Token 2: ふああ = 2a → "Fuaa" (đúng, giữ).

**2459 [れいな] — romaji + gasp (audit bỏ sót)**
JP: 「ふあっ！　あっ！　きもち、いっ――きもち、いい。⏎んっ――あっ――はっ――あっ――ふあっ――あっ」
TW: 「蛤啊！啊！好舒服……好舒服。啊啊啊、啊啊……蛤啊啊」
Cũ: 「Fua! A! Sướng, quá——sướng, quá.⏎Ưm——a——ha——a——fua——a」
Mới: 「Fua! A! Sướng, quá——sướng, quá.⏎Ưm——a——ha——a——Fua——aƯ」
Lý do: 2 token ふあっ→"Fua"; あっ cuối tuyệt đối dòng (không dấu câu sau) → "aƯ" — âm っ mất hẳn trong VN cũ. Tiền lệ lr-h2 1433 đã gộp ("Fa! A! A! AƯ!!!"). Các あっ giữa dòng giữ "a——" (dấu —— diễn っ).

## 4. Những dòng rên đã kiểm tra và GIỮ NGUYÊN (đáng chú ý)

- **Gasp Ư của sweep/audit (6 dòng — KHÔNG đụng):** 1962 "Ư——!" (cả dòng っ――！, audit tìm thêm), 1963 "Ư!!!", 1990 "Hauuuu~Ư!!" (はうぅぅぅ = 4u, đúng công thức), 2022 "Ư!", 2972 "——Ư!?", 3095 "——Ư!!?". Tất cả đã đúng.
- **Cười (15 dòng):** 2099/2104/2111 audit đã sửa đúng "Ufufu~" (うふふぅ là cười, không phải rên); 2089/2102/2103 trong file đã đúng "Ufufu~"; 2091/2093/2095/2097/2106/2108/2110 えっへへー→"E he he"/"Ehehe~" đúng (cười, không phải rên).
- **Họ ひゃ đã romaji sẵn (33 dòng):** 1887 "Hyaaaaaaaaaan" (10a, đếm bằng máy đúng), 1888 "Kyau!!?", 1902 "Hyawawa!?", 1905 "Hyauuu" (3u), 1981 "Hyaaan!" (3a), 2002 "Hya", 2006 "Hyaun", 2007 "Hyaan!" (2a), 2009 "Hyauuuun!" (4u), 2016 "Hyau!", 2019 "Hiyaaan!" (3a), 2020 "Nhyu!!", 1978 "Hyaauun!" (2a+2u). Không còn dòng "Á" nào cho họ ひゃ/ひゅ/ひあ/きゃ sau đợt này.
- **Rên dài đếm đúng (đếm lại bằng máy):** 1989 はうう→"Hauu!" (2u), 1990 (xem trên), 2017 ふみゅぅぅぅんっ→"Fumyuuuun!" (5u), 1983 ふやあああんっ→"Fuyaaaan" (4a), 2454 ふあぁ→"Fuaa" (2a), 2456 ふぁあっ→"Faa" (2a — chỉ đổi dạng, không đổi số), 1894 ふぁぁっ→"Faa" (2a).
- **Hơi thở ngắn "phù"/"fu" đứng riêng + ふゆ/ふわ:** 2000 "Fuyu" (ふゆっ — ngoài họ fa/fu, tiền lệ Mayami giữ), 2015 "Kyufu" (きゅふっ — cả từ SFX giữ nguyên), 2525 "fuwawa" (ふわわ — ngoài họ fa/fu), 1897 "Fue?" (ふえ？ — thán từ ngạc nhiên, không phải ふぇっ).
- **んっ → "Ưm"/"ưm" (45 dòng có んっ):** nhất quán toàn file, đúng — vd. 2045 "Ưm——", 2170 "ưm", 2391 "ưm", 2542 "ưm!". 2005 ンッ→"ư" giữa dòng giữ (dấu —— sau đó diễn っ).
- **SFX độc thoại （ ） (30 dòng):** giữ nguyên theo quy ước file — vd. 3254 （ぷちゅっ）→"（Chụt）", 3267 （ちゅむっ――れるっ――れろっ――ちゅむっ）→"（Chụt——liếm——liếm——chụt）", 3268 （ちゅぷううっ）→"（Chụt）", 3269 （ちょおおおおおおっ）→"（chooooooo）" (7o, đúng), 3279 （くぱあああっ）→"（Tách ra）", 3289 （きゅううううううんっ）→"（Siết chặt!!!）", 3255 （ごきゅっ×2…）→"（Ực——ực——ực——ực）". Chưa áp công thức đếm nguyên âm cho nhóm này — xem cờ F3.
- **Nói lắp/nói ngọng:** 2047 ほうへふ→"Soutetsu" (audit giữ), 1903 れてっ→"ra rồi", 1849 こすっ――っって→"cọ, xát!!", 2237 か、かわいい→"K-Không phải" — đều là lời thoại ngọng/lắp, không phải rên, giữ nguyên.
- **っ nhấn mạnh trên từ nội dung (không thêm Ư):** 1813 へっ, 2356 にっ, 2426 たくさんっ, 2901 ためっ!, 2016 おまんこっ, 2202 とこっ, 2172 にっ, 2015 だめえっ, 2453 せつっ — tiền lệ sweep loại 1474 (っ nhấn mạnh cuối câu không phải gasp).

## 5. Cờ cho đợt thống nhất / vòng audit (không quyết ở đây)

- **F1 — Fa/Fua chặt vs h8:** file này dùng Hepburn chặt (ふぁ→"Fa", ふあ→"Fua", ぷぁ→"Pa", ぷあ→"Pua"), theo đa số đã gộp (凪h2, lr-h2, lr_ふかみh1, lr-h1, h7, lr-jiekei). h8 đã gộp dùng "Fua" cho cả ふぁ (2049/2167/2212) và "Pua" cho cả ぷぁ (2279) — cần quyết MỘT dạng duy nhất toàn dự án ở đợt thống nhất (cờ F4 của lr-h1).
- **F2 — ふっ → "Fu" hay "phù":** đợt này đổi 5 dòng (1936, 2005, 2015, 2088, 2134) sang "Fu" (tiền lệ h9 2089; VN cũ vốn là "fu"). h8 đã gộp giữ "phù" cho ふっ; lr-h2 giữ "Phù" cho ふーっ (1905/2056). Cần quyết một dạng toàn dự án.
- **F3 — họ ちゅう(っ) và SFX （ ）:** 1994/2043/2047 áp công thức đếm (chụụụt/chụụt/chumu) theo tiền lệ Paulette h3 đã gộp; h7 đã gộp GIỮ "chụt"/"chùn chụt" cho họ này và cờ lại — mâu thuẫn giữa 2 file đã gộp, cần quyết một dạng. SFX độc thoại （ ） (3266/3267/3268/3254…) chưa áp công thức đếm — cùng câu hỏi như cờ h9/lr-h2.
- **F4 — hơi thở tập thở (không phải rên):** 1883 すぅ――――、はぁ―――― → "Hít vàooooo, thở raaaaaa"; 2533 すううううううう。はあああああ → "Hít vàooooooooo. Thở raaaaaa"; 2562 すうう、はああ → "hít vàoooo, thở raaaa". Số nguyên âm kéo dài không khớp công thức (vd. 2533: 8u → 9 chữ o; 2562: 3u → 4 chữ o) nhưng đây là từ tiếng Việt kéo dài theo dấu —— (hơi thở duy trì), không phải rên romaji — KHÔNG sửa ở đợt này, ghi cờ cho đợt thống nhất.
- **F5 — 2 gasp thêm mới (1988 "HauuƯ", 2459-final "aƯ"):** audit đã quét toàn bộ dòng っ và chỉ tìm thêm 1962 — 2 dòng này audit bỏ sót (hoặc cố ý giữ). Thêm theo đúng ranh giới gasp + tiền lệ lr-h2 1567/1433 đã gộp — parent kiểm tra lại lúc gộp.
- **F6 — 2021 "Nhyan!!!":** VN cũ "Nhyannn" thừa 2 chữ n (JP chỉ 2 âm ん); っ×3 → "!!!" theo tiền lệ lr-h3 1224. Nếu Hieu muốn giữ n dài làm nhấn mạnh thì lùi lại ở đợt thống nhất.
- **F7 — đếm audit sửa lại trong đợt này:** 1967 "phuya" (audit) thiếu 1a → "Fuyaa"; 2458 "Fuaaaaa" (VN cũ) thiếu 1a → "Fuaaaaaa"; 1986 "fuaaaan" (VN cũ) thừa 1a → "Faaaan". Đếm của audit ở 1986/2458 đã đúng (chỉ đổi token), ở 1967 audit đếm sai.
- **F8 — 2288 (audit, không phải rên):** chủ ngữ といっていた không xác định được — giữ nguyên, chờ Hieu kiểm tra trong game (ghi lại từ audit).

## 6. Lượt soát 2

Đọc lại toàn bộ 43 fix đối chiếu từng JP (+TW) lần thứ hai: **43 tổng / 43 tái kiểm chứng / 0 loại bỏ / 0 sửa lại.** Kiểm tra cơ học: JSON 43 mục, khóa string; jp/tw/old_vn khớp CSV3 tuyệt đối 43/43; difflib so với fix audit: 34/34 dòng trùng audit chỉ khác đúng token rên (cộng 3 sửa đếm + 1 thêm gasp trong đó); 9 dòng mới không trùng audit; 5 dòng fix == VN cũ (2015, 2452, 2453, 2454, 2457 — hoàn lại đúng token audit đã đổi, tiền lệ lr-jiekei 12 dòng); khối TOML parse bằng tomllib: 43 khóa, 0 sai lệch giá trị. Đếm nguyên âm kiểm chứng độc lập bằng máy: 1979 (16a), 2044 (10u), 1984 (7u), 2458 (6a), 1986 (3a), 2021 (2n), 1967 (2a), 2155 (3u), 1994/2043 (3ụ), 2047 (2ụ + chumu) — 10/10 đúng.

## 7. Khối TOML (đã kiểm chứng parse)

Khối TOML dưới đây parse được bằng tomllib, **43 key, 0 sai lệch giá trị so với JSON**. Giá trị fix nào chứa ký tự xuống dòng dạng backslash-n thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON.

```toml
[script]
"1784" = "「Cùng nhau——cùng nhau——ưm——Fua——\\nReina cũng——cùng nhau——muốn cùng nhau, ạ~」"
"1835" = "「Đến rồi——đang tới——Fua——a——a!\\nNóng quá——nóng quá——của anh——Soutetsu」"
"1885" = "「Hia——a——ngoáy——vào——rồi\\n——ưm——Fua——a——trong bụng——cọ, cọ」"
"1890" = "「Fue」"
"1894" = "「Fue? A——……Faa」"
"1936" = "「Ưm——Fu——a——phần, đầu——ưm,\\nphần đỉnh, của——chỗ——to——thôi——」"
"1938" = "「Fue——Fuya」"
"1967" = "「A——Reina——tè, dầm——mất, rồi——\\nFua——a——vẫn——còn ra, nữa——Fuyaa」"
"1969" = "「Fa……từ, phía sau——làm, tình——\\nquan hệ, sao ạ~?」"
"1976" = "「Ua——a——giật, giật——mất rồi——\\nFue——a——sướng——sướng, quá——Fu, a」"
"1978" = "「Hyaauun! Anh, Soutetsu——Fua\\n——Reina, sắp——sắp rồi!!」"
"1979" = "「Hyuaaaaaaaaaaaaaaaan!!!」"
"1983" = "「Fuyaaaan! ——Fa, a, bây giờ cũng——\\nrung lên, ngực, đang run rẩy, mồ hôi, ướt nhẹp」"
"1984" = "「Fyuuuuuuun!!!」"
"1986" = "「Hya! Ư! Fua! Cái này! Cái này!\\nTuyệt quá——ưm——hi——Faaan!!!」"
"1988" = "「HauuƯ」"
"1994" = "「Am——chụt——chụt——chụụụt!」"
"1999" = "「Hia——an——ưm——lưỡi——phần đầu, đang,\\nchạm, chạm——vào, Reina, cái đó, Fa」"
"2000" = "「Fuyu——ưm——Fua——a——hyu,\\nưm——a——anh Soutetsu——anh Soutetsu」"
"2001" = "「Hyau, ư——ưm——Fua——ưm——\\nmông——ưm——núm vú, nữa——Fua」"
"2004" = "「Hyan——ưm——Fua——a——nữa đi,\\nnữa đi, ngực. Reina, tất cả——nữa đi~」"
"2005" = "「Nkyu——ư——a——Fu——phần đỉnh\\n——núm, vú——tê rần, lên, rồi——Fu, a」"
"2013" = "「Hyaun! Á——Fua, á——Reina,\\nhậu môn——hậu môn, trở nên kỳ lạ mất rồi ạ~」"
"2015" = "「Kyufu——ưm! ~~~! Fu——ku——\\nưm——không được——vẫn, chưa——chỗ đó, chưa được」"
"2017" = "「Fumyuuuun! Hôn kìa——Fua——\\nanh Soutetsu——hôn, chỗ, đó, kìa」"
"2021" = "「Nhyan!!!」"
"2043" = "「Liếm——chụụụt——liếm liếm——cạp!」"
"2044" = "「Kyufuuuuuuuuun!!!」"
"2047" = "「Ưm……chụt——chụụt——chumu——ưm……\\nyêu……ưm——chụt——Soutetsu……haan」"
"2088" = "「Ehe, he~——Reina——được, khen——Fu\\n——Fua——a——vui, lắm——ạ~——ưm」"
"2134" = "「Ha——mãnh, liệt——quá——Fu——n-a——\\nbụng, của——Rei, na——đang, quặn, lại」"
"2155" = "「Ma! Quả nhiên, hóa trang thì……\\nUuu, nhưng mà, Reina thấy tiếc lắm ạ~」"
"2172" = "「Chỗ, đó——như tan, chảy——bám chặt, lấy\\n——Fua——cọ——cọ xát——cùng, nhau」"
"2202" = "「Chầm chậm——chỗ, đó——bị, đào bới\\n——Fua——a——chỗ——thắt, lại」"
"2451" = "「Fa——không được——chỗ, đó——vẫn chưa, được.\\nCùng nhau——với anh, Soutetsu——cùng, nhau」"
"2452" = "「Fua——lưỡi——lưỡi, sướng lắm ạ~——\\nưm——chỗ đó——tất cả——hãy liếm láp đi ạ」"
"2453" = "「Fua——a——Reina——tè dầm, mất——ưm,\\ntrực, tiếp——vào miệng——anh, Soutetsu」"
"2454" = "「Fuaa——ngực——núm vú——vuốt, vuốt——\\nxoa——xoa——ưm! Sướng, quá, ạ~」"
"2455" = "「Fuya——Fua——anh Soutetsu」"
"2456" = "「Faa」"
"2457" = "「Fua……a……a……ya——ưm——\\nchỗ đó——tinh dịch——đang tràn——ra ngoài」"
"2458" = "「Fuaaaaaa——Reina, vào miệng——\\nanh Soutetsu——nkyu!? Fuaa——an!!」"
"2459" = "「Fua! A! Sướng, quá——sướng, quá.\\nƯm——a——ha——a——Fua——aƯ」"
```

## Kết bài

File れいなh4_ふたりっきりのハロウィン.txt.toml (584 dòng) đã đọc toàn bộ từng dòng đối chiếu JP + TW: **43 dòng rên đổi** — 34 dòng fa/fu đưa về romaji theo quy tắc fallback (audit trước đó đã Việt hoá chúng), 2 dòng ひあ sửa "Hya"→"Hia", 4 dòng đếm nguyên âm rên dài, 2 dòng gasp audit bỏ sót, 3 dòng chuỗi hôn ちゅ, 1 dòng rên thất vọng. 3 tiếng cười audit sửa "Ufufu~" và 6 gasp Ư của sweep/audit đã kiểm chứng đúng, không sửa lại. Không dòng "Kh" nào bị đổi. Không còn dòng "Á" nào cho họ ひゃ/ひゅ/ひあ/きゃ sau đợt này. Sau file này, tổng cộng **18 file / 420 dòng sai (moan)** (cơ sở 17 file / 377 dòng + 43 file này).
