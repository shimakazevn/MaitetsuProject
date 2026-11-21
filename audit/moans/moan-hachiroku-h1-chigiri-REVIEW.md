# Moan-fix REVIEW — ハチロクh1_契り.txt.toml (moan-hachiroku-h1-chigiri)

File H-scene đầu tiên của Hachiroku (phong ấn được giải trừ, kết lời thề nguyện hai kiếp và làm tình lần đầu). Nhân vật: monologue 175, ハチロク 107, 双鉄H 71.

## 1. Xác minh file

- File: `ハチロクh1_契り.txt.toml` — route `01_Hachiroku`.
- Disk: `sources/toml2/translation_toml/01_Hachiroku/#U30cf#U30c1#U30ed#U30afh1_#U5951#U308a.txt.toml`
- TOML md5: `ea6d9621d4124d9a966b6842fe53b602` (khớp với md5 lúc audit; không có bản trùng — md5 xuất hiện 1 lần trong toàn bộ `sources/toml2/`).
- TOML: UTF-8 BOM + CRLF (725 CRLF, 0 LF lẻ); `[selections]` rỗng.
- CSV3: 1 bộ duy nhất, 353 dòng, 0 key trùng, 0 VN trống; flat-match VN với TOML: 353/353.
- Đã đọc 353/353 dòng (CSV3 + TOML-2, đối chiếu từng dòng).
- Lưu ý: audit file này đã áp romaji fallback rất kỹ (40 dòng moan) và được parent kiểm chứng 21/11 ~11:00 — nên vòng moan-fix này là kiểm tra nhẹ + xét lại các dòng rên còn giữ, không phải sửa hàng loạt.

## 2. Moan inventory — 101 dòng rên/SFX đã xét

- Thoại rên (ハチロク + 双鉄H): 63 dòng — rên dài (あ/は/ふ/ひゃ/ひあ/きゅう…), hơi thở (ふっ/ふ/はぁ/ん…), SFX miệng (ちゅ/じゅ/れる…), nói ngọng/lắp (そ、/せ、/さ、), tiếng đáp (ああ/うむ — không tính là rên, xem mục 5).
- SFX trong ngoặc （） ở độc thoại: 38 dòng (2124–2184).
- Tổng: 101 dòng rên/SFX. Đổi 1 dòng (1248), giữ 100 dòng.
- Ngoài ra đã kiểm tra 5 dòng độc thoại có từ tượng thanh trong văn xuôi (1829 きゅうくつ, 1889 キュッキュ, 1925 カチカチ, 1945 ごくり, 2001 とさっ) — đều đã diễn đúng theo nghĩa, giữ nguyên, không tính vào 101 dòng trên.

## 3. Dòng sửa (1 dòng — 1248, 2 lỗi trong cùng 1 dòng)

### 1248 — romaji + đếm nguyên âm (ハチロク)

- JP: 「あっ――ひっ――んううっ――双鉄、様っ――\nそれ――すごすぎ――って、んひゅっ――ひうううっ！」
- TW: 「啊——咿——嗯嗚——雙鐵少爺——太——太厲害了——嗯呀——嗚嗚嗚！」
- VN cũ (TOML): 「A――hi――ưm ư――Ngài, Soutetsu――\nCái đó――sướng quá――ưm hyu――hiưưư!」
- VN mới: 「A――hi――ưm ưư――Ngài, Soutetsu――\nCái đó――sướng quá――Nhyu――Hiuuu!」
- Lý do (2 lỗi riêng biệt trong cùng 1 dòng):
  - (a) Đếm nguyên âm — んううっ → "Ưm ưư" (VN cũ "Ưm ư" chỉ có 1 ư, JP có 2 う — thiếu 1 ư). Audit đã áp sai tiền lệ h9 2144 (んうっ, CHỈ 1 う → "ưm ư") cho dòng này (2 う). Đối chiếu trong chính file này: 1288 んううううううっ → "Ưm ưưưưưư" (6 ư cho 6 う, audit xác nhận đúng) — mẫu "Ưm + ư×n" của file đòi 2 ư ở đây. TW viết 嗯嗚 (1 u) nhưng JP 2 う là chuẩn — JP thắng TW.
  - (b) Romaji họ ひゅ — んひゅっ → "Nhyu" (VN cũ "ưm hyu"). Quy tắc 3b quyết 21/11 ~11:55: んひゅ → "Nhyu" (ghi rõ trong quy tắc). Tiền lệ vòng moan-fix: h7 836 んひゅん→"Nhyun" / 837 んひゅっ→"Nhyu"; 稀咲h3 2277 đã sửa "Ưm hưu"→"Nhyun"; 凪h2 2512 んひゅ→"Nhyu". Audit giữ "ưm hyu" với lý do "tiền lệ h8 2187" — ĐÃ KIỂM CHỨNG: h8 KHÔNG có key 2187 (không có trong CSV3 của h8 lẫn audit wrong.json của h8; tiền lệ viện dẫn không tồn tại). Hơn nữa quyết định 3b (11:55) ra SAU khi audit được parent kiểm chứng (11:00) — lúc audit giữ "ưm hyu", quy tắc んひゅ→"Nhyu" chưa được ghi rõ.
- Lưu ý hợp nhất: fix này THAY THẾ fix audit cùng key 1248 ở đợt thống nhất — khác fix audit CHỈ ở 2 chỗ rên trên ("Hiuuu" cho ひうううっ và toàn bộ phần còn lại giữ nguyên giá trị audit). Đã kiểm chứng cơ học bằng diff: audit-fix vs moan-fix chỉ khác 2 chuỗi đó.

## 4. Đồng ý với audit — 39/40 dòng moan của audit kiểm chứng lại là đúng

Audit file này đã sửa 40 dòng moan (romaji 19 + sai âm 15 + đếm nguyên âm 6; gasp 6 riêng). Kiểm chứng lại từng dòng, đồng ý 39/40 (chỉ thay thế 1248, mục 3):

- Romaji fa/fu (đã đúng, giữ nguyên giá trị audit): 1214, 1251, 1257, 1266, 1267, 1268, 1269, 1270, 1271, 1302 — ふあ/ふぁ → "Fua/Fuaa" (đã kiểm chứng cơ học: toàn bộ 10 dòng JP có ふあ/ふぁ trong file đều đã là "Fua", không còn "Phua"/"phua"/"ư a" nào).
- Romaji họ ひゃ/ひゅ/ひあ/きゃ (đã đúng): 1222 ひあっ→"Hia", 1225 きゃふう→"Kyafuu", 1226 ひゃうん→"Hyaun", 1229 ひあっ→"Hia", 1265 あひゅん→"Ahyun". (1227 ひあっ→"Hia" đã đúng sẵn trong TOML, audit không cần sửa.)
- Romaji khác (đã đúng): 1219/1229 んふっ→"Ưm fu" (tiền lệ kisaki-h3 2207); 1238 いっ→"I", んくう→"Nkuu"; 1241 くふううううん→"Kufuuuuun" (6 u, đếm lại đúng); 1248 ひううう→"Hiuuu" (3 u, đúng — chỉ sửa 2 chỗ còn lại của dòng này, mục 3); 1278 んちゅっ→"Ưm chụt", れるっ→"Reru"; 1282 んきゅうううう→"Ưm kyuuuuu" (5 u, đúng); 1286 んふう→"Ưm phuu" (2 u), 1287 んふうう→"Ưm phuuu" (3 u).
- Đếm nguyên âm audit đã đúng (đếm cơ học lại): 1245 んうっ→"Ưm ư" (1 u); 1253 あああ→"Aaa" (3 a); 1263/1264 ああ→"Aa"; 1290 んんう→"Ưmm ư"; 1291 んん→"Ưmm".
- SFX ngoặc sai âm audit đã sửa (đã đúng): 2128 ぴゅぴゅっ→"Phụt phụt"; 2132 じゅちゅっ→"Juchu", じゅるっ→"Juru"; 2138 しにゅっ→"Shinyu", すりゅっ→"Suryu"; 2139 くりゅっ→"Kuryu"; 2144 じゅるっ→"Juru", じゅにゅっ→"Junyu"; 2145 じゅりゅ→"Juryu"; 2147 ちゅむっ→"Chumu"; 2149 じゅるっ→"Juru"; 2153 ぼびゅうっ→"Bobyuu"; 2179 じゅるるうるるる→"Jururuurururu" (13 ký tự, đếm lại đúng).
- Gasp Ư (sweep/audit, KHÔNG đụng lại): 1242, 1371, 1376, 1463, 1508, 1519 + 1271, 1293 (2 gasp sweep bỏ sót, audit đã thêm đúng).

## 5. Ghi chú các dòng rên giữ nguyên (đáng chú ý)

- Hệ SFX trong ngoặc （） diễn theo nghĩa hành động — QUYẾT ĐỊNH GIỮ NGUYÊN HỆ NÀY (trả lời cờ của audit: "vòng moan-fix sẽ phán lại hệ này"): theo tiền lệ moan-fix h8 (quyết giữ hệ diễn theo nghĩa hành động, và h8 viện chính audit file này làm tiền lệ). Audit đã sửa 10 chỗ sai hẳn âm (mục 4); 23 dòng còn lại đã xét từng dòng, đều là cách diễn hành động đúng với JP:
  - 2124 ほじっ→"Ngoáy"; 2125/2129/2170 きゅ→"Siết (chặt)"; 2126 こつっ→"Cộc"; 2127 ぐりゅっ→"Ngoáy", こしゅっ→"sột" (こす = cọ xát — "sột" diễn tiếng cọ, khác すりゅっ ở 2138 vốn là tiếng trượt/liếm nên mới đổi sang "Suryu"); 2133 れるっ→"Sượt"; 2135 うわっ→"Oái"; 2136 おっと→"Ối"; 2140 ちぃぃぃぃっ→"Xoạt"; 2141 ズパンっ→"Phập"; 2151 びゅ→"Phụt" (nhất quán 2128/2153); 2154 こくんっ→"Ực"; 2159/2166 くちっ/くちぃっ→"Nhóp nhép" (nhất quán cặp đôi); 2160/2165 つぷっ→"Phập" (TW đều ghi "chèn vào"); 2164 くりゅっ→"Nắn nắn" (TW 捏 = bóp/nắn — khác ngữ cảnh 2139, TW 哧溜 = tiếng trượt/liếm, nên 2139 dùng "Kuryu" còn đây dùng nghĩa hành động là đúng); 2168 さすっ→"Xoa xoa"; 2176 みちみち→"Siết chặt siết chặt"; 2177 ずぶ→"Phập", プツっ→"Bục"; 2180 ぴとっ→"Chạm nhẹ"; 2184 ずるううううううっ→"Phập phập phập!".
  - Độ dài kéo chữ của các từ hành động ("siết chặttttt", "Phập phập phập!") là phong cách kéo chữ nghệ thuật, không áp công thức đếm nguyên âm — theo tiền lệ moan-fix h8.
- Họ や → "Nhá"/"A"/"á" giữ nguyên theo tiền lệ đã chốt: 1214 やぁっ→"Nhá", 1217/1245 やっ→"A", 1222 やっ→"á", 1224 やあアッ→"Aaa" (3 a, đếm đúng). "Á" duy nhất trong file là cho やっ (1222), KHÔNG có dòng "Á" nào cho họ ひゃ/ひゅ/ひあ/きゃ — đã kiểm chứng cơ học.
- ふっ → "phù" giữ nguyên theo đa số tiền lệ (1217, 1276); ふっ ngắn không bắt buộc romaji — chỉ ふあ/ふぁ mới bắt buộc.
- "Kh" cho glottal-stop っ GIỮ NGUYÊN, không đổi sang Ư (quy tắc đã khóa): 1144 いえっ→"kh,", 1210 せ、→"Ch,", 1315 は、→"kh,".
- Mẫu "Ưm + X" cho ん+X giữ nguyên toàn file: 1245 んうっ→"Ưm ư", 1278 んちゅっ→"Ưm chụt", 1282 んきゅうううう→"Ưm kyuuuuu", 1288 んううううううっ→"Ưm ưưưưưư" (6 ư, đếm đúng), 1290 んんう→"Ưmm ư", 1291 んん→"Ưmm".
- Tiếng đáp ああ/うむ KHÔNG phải rên, giữ nguyên: 1275, 1281, 1296, 1298, 1312, 1390, 1394, 1397, 1399, 1401 (ああ→"Ừ"/"À"); 1300 うむ？→"Ưm?" (audit đã ghi nhận không nhất quán chính tả "Ưm" vs "Ừm" ở 1385/1394 — không thuộc phạm vi moan, không sửa).
- っ nhấn mạnh được diễn bằng dấu câu, không thêm Ư (đúng quy tắc gasp boundary): 1314 様っ→"Soutetsu——", 1514 さまぁっ/そこっ/頭っ→dấu "――", 1515 様っ！→"Soutetsu!".
- 956 「……ぁっ」→"……A."; 1239 くっ→"Hự"; 1240 うあ→"Ư a"; 1243 あっ→"A"; 1255 あ……→"A……a……"; 1258 あ……ん……は……んっ→"A……ưm……ha……ưm."; 1260–1262 あっ→"A"; 1273 んっ→"Ưm"; 1280 ん……→"Ưm……"; 1354/1431 んっ→"ưm" — tất cả giữ nguyên, âm đã diễn đúng, số lượng đúng.

## 6. Kiểm chứng sweep gasp

- Sweep có 6 mục cho ĐÚNG file này (đọc trực tiếp `sweep-raw-gasp-wrong.json`, lọc theo `file`): 1242 (lost-gasp-whole), 1371/1376/1463/1508 (raw-tsu), 1519 (lost-gasp-whole) — cả 6 audit đã áp đúng, kiểm chứng lại đúng, KHÔNG đụng lại. (18 mục sweep khác chứa "契り" thuộc về file lr_ハチロクh1_今ひとたびの契り.txt.toml — file khác, không liên quan.)
- 2 gasp sweep bỏ sót audit đã thêm (1271 っ…… giữa dòng, 1293 っ！？ đầu dòng) — kiểm chứng lại đúng.
- Không có dòng "Kh" nào bị đổi sang Ư. Không có dòng gasp Ư nào bị xem lại. Không còn っ thô nào trong VN (kiểm chứng cơ học: 0 dòng).

## 7. Cờ cho Hieu / cho đợt thống nhất

### 1238 — cờ CHO HIEU (audit đã cờ, giữ nguyên — không tự quyết)

- JP: 「いっ――あっ――んくうっっっっっっっ！！！」
- Fix audit (giữ nguyên ở đây): 「I——a——Nkuu!!!」
- Audit phán đoán いっ → "I" (nguyên âm i, không phải "Á"; tiền lệ h9 2101). Nếu Hieu thấy "Á!" tự nhiên hơn trong tiếng Việt thì trả về "Á" — một dòng, dễ revert. Vòng moan-fix KHÔNG quyết thay Hieu.

### 1248 — lưu ý hợp nhất (không phải cờ)

- Fix moan ở đây THAY THẾ fix audit cùng key ở đợt thống nhất (áp giá trị moan, không áp giá trị audit, cho key 1248). Khác fix audit chỉ ở 2 chỗ rên (mục 3).

### 1300 — ghi nhận nhỏ (không phải cờ)

- うむ？ → "Ưm?" vs 1385/1394 うむ → "Ừm": không nhất quán chính tả "Ưm"/"Ừm" trong file (audit đã ghi nhận). Không thuộc phạm vi moan, để đợt thống nhất chuẩn hóa nếu muốn.

## 8. Lượt soát 2 (second pass)

- Đọc lại toàn bộ 1 giá trị fix so với JP + TW sau lượt đầu, kèm đếm cơ học lại các dòng đếm nguyên âm audit đã sửa (1269: 10 a; 1241: 6 u; 1282: 5 u; 1286: 2 u; 1287: 3 u; 1253: 3 a; 1266: haa = 2 a; 2179: 13 ký tự; 1288: 6 ư; 1248: んうう = 2 ư, ひううう = 3 u — đều đúng).
- Tổng: 1 / tái kiểm chứng: 1 / bỏ: 0 / sửa: 0.

## 9. Khối TOML (parse-verified bằng tomllib: 1 khóa, 0 sai lệch giá trị so với wrong.json)

```toml
[script]
"1248" = "「A――hi――ưm ưư――Ngài, Soutetsu――\\nCái đó――sướng quá――Nhyu――Hiuuu!」"
```

Lưu ý: trong khối TOML trên, `\\n` là ký tự xuống dòng đã escape (giá trị thực trong JSON/TOML là `\n` literal như CSV3).

## Kết bài

File ハチロクh1_契り: đã đọc 353/353 dòng, xét 101 dòng rên/SFX, đổi 1 dòng (1248: んううっ thiếu 1 ư + んひゅっ "ưm hyu"→"Nhyu" theo quy tắc 3b) — audit file này đã áp romaji fallback rất kỹ từ trước (39/40 dòng moan của audit kiểm chứng lại là đúng, chỉ thay thế 1248). Hệ SFX trong ngoặc diễn theo nghĩa hành động được GIỮ NGUYÊN theo tiền lệ moan-fix h8. 1 cờ cho Hieu: 1238 ("I" hay "Á"). Không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào.
