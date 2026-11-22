# Moan-fix REVIEW — 日々姫h2_洗って大丈夫なスーツ.txt.toml (moan-hibikih2-aratte-daijoubu-na-suitsu)

File H cuối cùng (64/64). Hibiki ngủ gật ở phòng thị trưởng, Soutetsu bế về, cởi bộ vest "giặt được" rồi làm tình trước gương lớn — H-scene dài, rên nhiều, SFX phun dồn.

## §1. Xác minh file

- File: `02_Hibiki/日々姫h2_洗って大丈夫なスーツ.txt.toml` — TOML md5 `406a1ba5a7f06dc38f49413d0fbe2d47`, 50.630 byte, UTF-8 BOM + CRLF (599 CRLF).
- CSV3: 1 bộ duy nhất, 290 dòng, 0 key trùng, toàn section `script`. TOML flat-match CSV3: 290/290 (không có dual-set).
- Audit: 16 dòng sai (audit-hibikih2-aratte-daijoubu-na-suitsu-wrong.json) — gasp 4, moan 6, nguyên âm dài 3, nghĩa 2, bịa 1. Đọc 290/290 dòng.
- Sweep: 4 mục cho file này — áp nguyên 3 (1085, 1086, 1283, đều đã nằm trong audit); mục 1071 là `already-rendered` (gasp đã diễn bằng Ưm, không sửa gasp). Audit tự tìm thêm 1 gasp sweep bỏ sót (843 「っ――」→"Ư——"). Không đụng dòng gasp Ư nào; không đổi dòng "Kh" nào (file này không có dòng "Kh").
- Không có thẻ %l nào trong file (B19 không liên quan).

## §2. Kho rên (98 dòng xét)

- Độc thoại SFX trong （ ）: 35 dòng (thrust, spurt, co thắt, sờ nắn…).
- Thoại có token rên (ふぁ/ふあ/ふぇ/ふや/ひゃ/きゃ/んきゅ/くひゅ/んうう/ふぅ/ぅぅ/えへへ/すぅ…): 24 dòng.
- Thoại chỉ có gasp っ (んっ/あっ/はっ/うっ/っ――): 39 dòng.
- Đổi 8 dòng (5 thoại rên + 1 thoại gasp mất âm + 1 SFX độc thoại + 1 đuôi moan dài). 90 dòng giữ nguyên.

## §3. Các dòng sửa (8 dòng)

### 1064 — 日々姫 — moan (mất âm かっ)

- JP: 「ひゃっ！　あっ――すごっ――これっ――\nかっ――はっ――あっ――息っ――とまっちゃ――うっ」
- TW: 「呀！啊――這樣――好厲害――啊――呼――啊――要窒息――了」
- VN cũ (CSV3): 「Hya! A——Khủng quá——Cái này——Hơ——A——Sắp tắt——thở——mất.」
- Sửa: 「Hya! A——Khủng quá——Cái này——Ka——Hơ——A——Sắp tắt——thở——mất.」
- Lý do: かっ (tiếng nghẹn "ka" khi Hibiki nín thở) bị mất hẳn trong VN — audit §4(2) cờ cho vòng moan (TW cũng bỏ). Khôi phục bằng romaji "Ka" (đúng thứ tự JP, giữa "Cái này——" và "Hơ——"); hàng này đã dùng romaji "Hya" cho ひゃっ nên "Ka" hợp phong cách. Không phải gasp Ư (か có phụ âm mora, không phải っ trơ).

### 1071 — 日々姫 — romaji (đuôi moan dài)

- JP: 「きゃっ！？　射精っ――私、おちんちん、オナニーでっ\n――びゅうって、射精――んっ――んううううう～っ！」
- TW: 「呀！？射了――我用雞雞、自慰――噗噗地射出來了――嗯――嗯啊～！」
- VN cũ (audit): 「Kya!? Xuất tinh rồi——Em, dùng cậu nhỏ, thủ dâm——mà, phụt——xuất tinh——Ưm——Ưm~~~!」
- Sửa: 「Kya!? Xuất tinh rồi——Em, dùng cậu nhỏ, thủ dâm——mà, phụt——xuất tinh——Ưm——Nuuuuu!」
- Lý do: đuôi moan んううううう～っ = ん + う×5 → "Nuuuuu" (5u, đếm bằng máy). Audit §4(1) để vòng moan quyết hình thức cuối ("~~~ thay cho nguyên âm dài"). Tiền lệ ハチロクh3 1064 んうううううう → "Nuuuuuu" (6u). きゃっ→"Kya" và びゅうって→"phụt" của audit giữ nguyên; んっ giữa dòng → "Ưm" giữ nguyên (token riêng).

### 1079 — 日々姫 — fa/fu → romaji

- JP: 「ふあっ！　あんっ！　んっ――\nにぃにっ――にぃにぃっ！」
- TW: 「呼！啊！嗯――阿哥――阿哥！」
- VN cũ (audit): 「Phùa! A! Ưm——Anh hai——Anh hai!」
- Sửa: 「Fua! A! Ưm——Anh hai——Anh hai!」
- Lý do: ふあっ trong rên → romaji "Fua" theo quy tắc romaji fallback (Hieu duyệt 21/11). Tiền lệ: lr_日々姫h2 (5/5 Fua), 日々姫h3 (toàn romaji), ハチロクh3 (ふあっ→"Fua"). Audit đổi "Phù"→"Phùa" để giữ mora あ (đúng theo quy tắc khóa), nhưng "Phùa" nghe ngượng trong rên → moan pass chuyển romaji.

### 1123 — 日々姫 — fa/fu → romaji

- JP: 「んッ――ふあっ――あんっ！」
- TW: 「嗯――—呼――啊！」
- VN cũ (audit): 「Ưm——Phùa——A!」
- Sửa: 「Ưm——Fua——A!」
- Lý do: như 1079 — ふあっ → "Fua".

### 1126 — 日々姫 — romaji (んきゅっ)

- JP: 「んきゅっ――ふっ――あっ――あかちゃんの――へやっ、\nにぃにの――おちん、ちん――ぐいって――く――はっ」
- TW: 「嗯――呼――啊――阿哥的――雞雞――撞上了――小寶寶的――房間――唔――呼」
- VN cũ (CSV3): 「Ưm kyu——Phù——A——Căn phòng——của em bé, bị cậu, nhỏ——của anh hai——thúc mạnh——Ư——Hơ.」
- Sửa: 「Nkyu——Phù——A——Căn phòng——của em bé, bị cậu, nhỏ——của anh hai——thúc mạnh——Ư——Hơ.」
- Lý do: んきゅっ là MỘT token ("nkyu"), VN cũ tách thành "Ưm kyu" (Ưm + kyu) là diễn tách — vi phạm một token = một cách diễn. → "Nkyu" (tiền lệ trực tiếp ハチロクh3 1218 んきゅっ→"Nkyu"; quy tắc 3b んひゅ→"Nhyu"). ふっ→"Phù" GIỮ (xem cờ F2); く――→"Ư" giữ (ngắt lời giữa chừng, không phải token rên).

### 1138 — 日々姫 — romaji (んきゅ dài, 12u)

- JP: 「んきゅうううううううぅぅぅぅっ！！！」
- TW: 「嗯啊啊啊！！！」
- VN cũ (audit): 「Ưm kyuuuuuuuuuuuu!!!」
- Sửa: 「Nkyuuuuuuuuuuuu!!!」
- Lý do: một token ん + きゅ + う×7 + ぅ×4 = 12 nguyên âm u (đếm bằng máy; audit đã sửa số lượng 8u→12u đúng công thức, nhưng giữ cách diễn tách "Ưm kyu..."). Gộp thành một token romaji "Nkyu" + 11u = 12u. Tiền lệ 1139/1126 cùng file + quy tắc 3b.

### 1139 — 日々姫 — romaji (んきゅんっ)

- JP: 「んきゅんっ！」
- TW: 「嗯啊！」
- VN cũ (CSV3): 「Ưm kyun!」
- Sửa: 「Nkyun!」
- Lý do: như 1126 — んきゅんっ là một token → "Nkyun" (tiền lệ quy tắc 3b んひゅん→"Nhyun").

### 1770 — monologue — sfx (びゅくっ)

- JP: （びゅくっ――びゅっ！　びゅうっ！　どびゅっ！）
- TW: （噗嚕――噗噗！噗噗！噗嚕！）
- VN cũ (CSV3): （Giật——Phụt! Phụt! Phụt!）
- Sửa: （Phụt——Phụt! Phụt! Phụt!）
- Lý do: びゅくっ là tiếng phun (TW toàn 噗噗 = phun); "Giật" diễn thành co giật cơ thể thay vì tiếng phun — audit §4(3) cờ cho vòng moan. Ba tiếng sau đã là "Phụt!", chuỗi phun phải đồng nhất.

## §4. Các dòng rên giữ nguyên (đáng chú ý)

- Gasp Ư của audit giữ: 843 「Ư——」, 1085 「Ê hê hê, anh hai~Ư」, 1086 「Ê hê hê~Ư」, 1283 「Ư!?」 (sweep 3/4 + audit tự tìm 843).
- Audit sửa đúng, giữ: 1074 くはっ→"Kuha——A——" (khôi phục は); 1077 ふぅぅぅぅぅぅぅぅんっっ → "Fuuuuuuuuun!" (9u = ふ + 8ぅ, đếm bằng máy); 1078 あ×8 → "Aaaaaaan" (8a, đếm bằng máy); 1081 ふやんっ → "Phuyan!!" (theo quy tắc khóa ふや→"phuya"; xem cờ F3).
- Họ ひゃ/きゃ đã romaji đúng: 1058/1064 ひゃっ→"Hya", 1062/1069 ひゃんっ→"Hyan", 1070 くひゅんっ→"Kuhyun!!!", 1061 きゃふううっ→"Kyafuuu!" (3u = ふ + 2う).
- ふっ → "Phù" giữ (1096, 1126, 1133, 1263) — xem cờ F2.
- 1076 ふあ……ぁ…… → "Phù... a..." GIỮ theo lý do rõ ràng của audit §3 (diễn đủ cả hai mora ふ và あ, khác 1079/1123 ふあっ→"Phù" làm mất あ; ngữ cảnh là tiếng thở dài nhẹ nhàng, không ngượng) — xem cờ F7.
- Cười: 1082 んへへ→"Nhehe", 1084/1085/1086 えへへ→"Ê hê hê" (cười, không phải rên); ngủ 846/1256 すぅ→"Khò... khò".
- ちゅ: 1122 toàn bộ ちゅっ/ちゅうっ/ちゅむっ → "Chụt".
- ぷっ → "Phù" (1125, tiếng phụt ngắn); （つ――ぷっ） → （Phậ——p） (1790).
- SFX phun giữ đồng nhất "Phụt!" (1764/1766/1771/1772) — xem cờ F6.
- 1044 どぴゅどぴゅって → "bắn thật nhiều" (cụm động từ, diễn theo nghĩa, giữ).
- 1073 くあっ → "Kua!" (đúng Hepburn).
- Gasp っ còn lại (んっ/あっ/はっ/うっ trong thoại) đều đã diễn đúng (Ưm/A/Hơ/Ư) — audit đã quét cơ học toàn bộ 176 dòng JP có っ, không còn gasp mất.

## §5. Cờ đợt thống nhất

- F1 — họ や: やっ/やんっ/や……ぁ…… → "A"/"Á"/"Yan" vs "Ya" — quyết định toàn dự án vẫn mở (h3 F5). Các dòng: 1055 (audit cố ý tách: やっ→"A" thốt ngắn, やんっ→"Yan" giữ ん — lý do audit chỉ nói về ん, không nói về y), 1060 や……ぁ……→"A... á...", 1066/1067/1220 やっ→"Á". TW đều dùng 呀 (ya) cho cả hai dạng.
- F2 — ふっ: file này "Phù" (1096, 1126, 1133, 1263) vs 日々姫h3 "Fu" (h3 F2) — tách, cần thống nhất một dạng.
- F3 — ふや: 1081 "Phuyan" (audit, theo quy tắc khóa) vs "Fuya" (lr_凪h1 moan) — đã cờ từ 凪h1 F2; file này theo quy tắc khóa.
- F4 — độ dài SFX diễn bằng phụ âm t/c (1787 "Trượtttttt", 1797/1798 "Siết chặtttt") — công thức đếm t/c vẫn mở (lr_日々姫h2 F1); giữ nguyên kiểu SFX theo audit §3.
- F5 — くっ trong SFX tả: 1757 くっ→"chụt" (trong chuỗi ちゅ、くっ――しにゅっ――くにゅっ――) vs h3 F5 ("Ngoáy"/"hự") vs 凪h1 F6 ("Ku" thoại vs "Ư" SFX tả) — cần thống nhất.
- F6 — SFX phun dồn: 1764/1766/1771 đều （Phụt! Phụt! Phụt! Phụt!） (audit §4(4)); giữ — 4 biến thể びゅ chỉ khác độ dài/mạnh, lặp "Phụt!" đã diễn đúng chuỗi phun.
- F7 — 1076 "Phù... a..." giữ vs 1079/1123 "Fua": nếu đợt thống nhất muốn một dạng duy nhất cho mọi ふあ, xem lại 1076.
- F8 — fa/fu "Phùa" vs "Fua" (audit §4(5)): đã chốt CHO FILE NÀY ở vòng moan (1079/1123 → "Fua"); cờ thống nhất còn lại cho các dòng audit ngoài file H.

## §6. Lượt soát 2

Đọc lại toàn bộ 8 giá trị sửa đối chiếu JP (+TW): **8/8 tái kiểm chứng, 0 bỏ, 0 sửa.**
- Đếm nguyên âm bằng máy: 1071 んう×5 → 5u ("Nuuuuu"); 1138 きゅ + 7う + 4ぅ → 12u ("Nkyuuuuuuuuuuuu"); 1077 9u / 1078 8a (audit đúng, giữ).
- JSON 8/8: jp/tw/old_vn khớp CSV3 (old_vn = giá trị audit cho 1071/1079/1123/1138, = CSV3 cho 1064/1126/1139/1770); khối TOML 8 khóa parse OK, 0 sai lệch với JSON.
- Sweep kiểm tra trực tiếp 4/4 mục — 3 nằm trong audit (gasp), 1 already-rendered (1071, không sửa gasp); không đụng dòng gasp Ư nào; không đổi dòng "Kh" nào.
- Không sửa dòng đại từ/thuật ngữ/nghĩa nào (1107, 1186, 1414 thuộc audit, không thuộc vòng moan).

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
1064 = "「Hya! A——Khủng quá——Cái này——Ka——Hơ——A——Sắp tắt——thở——mất.」"
1071 = "「Kya!? Xuất tinh rồi——Em, dùng cậu nhỏ, thủ dâm——mà, phụt——xuất tinh——Ưm——Nuuuuu!」"
1079 = "「Fua! A! Ưm——Anh hai——Anh hai!」"
1123 = "「Ưm——Fua——A!」"
1126 = "「Nkyu——Phù——A——Căn phòng——của em bé, bị cậu, nhỏ——của anh hai——thúc mạnh——Ư——Hơ.」"
1138 = "「Nkyuuuuuuuuuuuu!!!」"
1139 = "「Nkyun!」"
1770 = "（Phụt——Phụt! Phụt! Phụt!）"
```

Kết bài

File 日々姫h2_洗って大丈夫なスーツ.txt.toml: đọc 290/290 dòng, xét 98 dòng rên/SFX, đổi 8 dòng (fa/fu→romaji 2, んきゅ→romaji 3, đuôi moan dài 1, mất âm かっ 1, SFX phun 1). Đây là file H cuối cùng — vòng sửa rên hoàn tất khi gộp file này.
