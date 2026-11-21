# Moan-fix: 日々姫h5_白濁絵の具の射精会.txt.toml — 3/343

## 0. Xác minh file

- File: `日々姫h5_白濁絵の具の射精会.txt.toml` — route 02_Hibiki.
- TOML-2: `sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59ebh5_#U767d#U6fc1#U7d75#U306e#U5177#U306e#U5c04#U7cbe#U4f1a.txt.toml`, md5 `52d2c33f2e0191177011d33230bc20e6` (khớp audit), UTF-8 BOM + CRLF, 343 key script. 1 bản TOML duy nhất.
- CSV3: 1 set duy nhất, 343/343 key khớp TOML; 0 dòng VN trống.
- Audit đã gộp (39 sai, ROUTE-AUDIT.md 22/11 ~02:40): gasp 11, moan 21, nguyên âm 6, sai nghĩa 1 (1674, không phải dòng moan — không đụng). Key 1153 đã bị parent LOẠI khỏi fix audit (agent ghi 10 a, JP có 9 a; giá trị đúng 9 a ghi trong review audit — vòng moan-fix này áp dụng).
- Nội dung: H-scene "hội bắn tinh bằng màu vẽ trắng đục" — Hibiki dùng cơ thể làm toan vẽ. Nhân vật: monologue 194, 日々姫 95, 双鉄 54.

## 1. Kho rên — đã xét

- Đã đọc 343/343 dòng (JP + TW + VN).
- Dòng rên/thở/gasp/SFX đã xét: **153 dòng** (thoại 105 + monologue 48, gồm 44 dòng SFX trong （）) — quét theo mẫu âm rên/thở/SFX rồi đọc từng dòng.
- Đổi **3 dòng** (nguyên âm 1, moan 2), giữ **150 dòng** rên/SFX.
- Đồng ý với toàn bộ 37 fix moan/gasp/nguyên âm còn hiệu lực của audit (38 trừ 1153 đã loại); phán lại 2 phán đoán của audit: 1264 "Nukyu" và 1154 "Po" — cả hai ĐỒNG Ý (xem §3).
- Không có dòng ふぇ/ふや nào trong file; không có dòng cười (ふふっ/うふふ/んふふ) nào.
- Không dòng gasp Ư nào bị xem lại; không dòng "Kh" nào bị đổi.
- Sweep gasp: 13 mục đã được audit áp/kiểm chứng (11 fix + 2 nhãn already-rendered 1166/1241 đúng) — không đụng lại.

## 2. Từng dòng sửa

### 1153 [日々姫] — nguyên âm (áp lại fix audit đã bị loại, với giá trị ĐÚNG 9 a)

- JP: 「ひゅっ！　あああああああああんっ！！？」
- TW: 「呀！啊啊啊！！？」
- Cũ: 「Hyu! Aaaaaaaaaaaan!!?」
- Mới: 「Hyu! Aaaaaaaaan!!?」
- Lý do: JP có あ×9 + ん (đếm bằng máy: 9 a, 1 n); VN cũ có 12 a (đếm bằng máy). Fix audit cũ ghi 10 a là sai — parent đã loại. Giá trị đúng 9 a + n, đúng như review audit đã ghi ("để đợt thống nhất / vòng moan-fix áp dụng"). ひゅっ→"Hyu!" giữ nguyên.

### 1215 [日々姫] — moan (はっ diễn thành "A" — mất phụ âm h)

- JP: 「はっ！　来たっ！　また、これっ――チュって――\nあまくてっ――おなかの、おくが――じんて、してっ」
- TW: 「啊！來了！又是這個――吸了上去――很舒服――肚子裡面――癢癢的」
- Cũ: 「A! Đến rồi! Lại, cái này――Hôn nhau――\nNgọt ngào quá――Sâu trong, bụng――râm ran, quá」
- Mới: 「Hà! Đến rồi! Lại, cái này――Hôn nhau――\nNgọt ngào quá――Sâu trong, bụng――râm ran, quá」
- Lý do: はっ là hơi thở "ha", không phải "a". Toàn file này quy ước はっ/はぁ trong thoại Hibiki đều diễn "Hà"/"hà" (1162, 1168, 1172, 1175, 1192, 1195, 1257, 1325, 1144) — 1215 là ngoại lệ duy nhất, làm mất phụ âm h ("don't lose the sound"). TW 啊 không phân biệt được あ/は — JP quyết định. Chỉ đổi "A!"→"Hà!", còn lại giữ nguyên.

### 1255 [日々姫] — moan (âm ぅ bị mất hoàn toàn)

- JP: 「ん……わかっ、た――は……ふ、ぅ……まんべんなく\n――まんべん、なく――ならっ」
- TW: 「嗯……好的――呼……呼……徹底潤濕――要徹底的話」
- Cũ: 「Ưm……em hiểu, rồi――hà……phù……Làm ướt đều\n――Làm ướt, đều――thì」
- Mới: 「Ưm……em hiểu, rồi――hà……phù, u……Làm ướt đều\n――Làm ướt, đều――thì」
- Lý do: JP có ふ、ぅ tách dấu phẩy — hai mora riêng; VN cũ chỉ diễn ふ ("phù"), làm mất hẳn ぅ. Tiền lệ cùng file 1190: ふ、ぁ → "phù, a" (audit giữ) — song song thì ふ、ぅ → "phù, u". TW cũng diễn thành hai tiếng 呼……呼, ủng hộ việc giữ cả hai âm.

## 3. Đã kiểm chứng đúng — giữ nguyên (phán lại + đếm lại bằng máy)

- **1264 "Nukyu" — PHÁN LẠI, ĐỒNG Ý với audit.** JP んうきゅっ = 3 mora ん-う-きゅ; VN cũ "Ưm kyu" chỉ còn 2 nguyên âm u, làm mất mora う ở giữa. Romaji "Nukyu" diễn đủ 3 mora (n-u-k-y-u: 2 u + 1 n, đếm bằng máy khớp JP). Tiền lệ 1212 んきゅ→"Nkyu". Không đổi.
- **1154 "Po" — PHÁN LẠI, ĐỒNG Ý với audit.** JP おちん――ぽッ: ぽッ là âm tiết cuối của おちんぽ bị cắt ngang; VN cũ "ưm" là âm mũi không có trong JP. "Po" diễn đúng âm tiết đó. TW 雞雞. Không đổi. (Cùng dòng: ひあっ→"Hia!" và ふあっ→"Fua" của audit cũng đúng, giữ.)
- **1180 — gasp Ư giữ, moan đồng ý.** Gasp cuối dòng (～っ) đã thêm Ư theo sweep — KHÔNG xem lại. Phần moan ふあ→"Fua" của audit đúng, giữ.
- **Đếm nguyên âm kiểm tra lại bằng máy từ JP gốc (công thức: số nguyên âm = 1 + số う/ぅ; với chuỗi あ/ぁ đếm trực tiếp):** 1151 "Hyaaaaaaaann" 8a/2n ✓; 1156 "Hyaaaaaaaaaa" 10a ✓; 1157 "Hyaun" 1a/1u/1n ✓; 1152 "Kyafunn" 1a/1u/2n ✓; 1158 "Hyan" 1a/1n ✓; 1160 "Hikyu"/"Kuha"/"Ya" ✓; 1212 "Nkyuuuuuuuuuuuunnnnn" 12u/6n ✓; 1213 "Kyufuuuuuuuu" 9u ✓; 1228 "Juzoooooooooooooooooo" 18o ✓; 1261 "Ưm muuu" 3u ✓; 1265 "Ưm buuuuuu" 6u ✓; 1269 "Zojuuu" 3u ✓; 1226 "Zuryuryuryuryu" 5u ✓; 1271 "Hii" 2i ✓; 1195 "Naaaa" 4a/1n ✓; 1174 "aa" 2a ✓; 1218 "Aaa" 3a ✓; 1172 "Aa" 2a ✓; 1240 "Bojun" 1o/1u/1n ✓ (ぢ="ji", không phải "sh").
- **Họ fa/fu còn lại — giữ đúng quy tắc:** ふっ→"phù" giữ toàn file (1162, 1171, 1179, 1182, 1184, 1190, 1240, 1241, 1243, 1245, 1246, 1250, 1253, 1262, 1269, 1271, 1347); ふ……ぁ / ふ、ぁ tách dấu phẩy → "phù……a" / "phù, a" giữ (928, 1129, 1190, 1191, 1192); ふうっ→"phuu" 2u đúng (1179); ふぎゅっ→"Fugyu" đúng (1262).
- **ひゃ-family — giữ đúng quy tắc 3b:** ひゃ→"Hya" (1151, 1156, 1157), ひあ→"Hia" (1148, 1150, 1154 — audit), ひゅ→"Hyu" (1153, 1172), きゃ→"Kya" (1152). Không còn "Á" nào cho họ này trong file.
- **SFX trong （） (2045–2108, 44 dòng) — giữ toàn bộ:** đã diễn thành từ tiếng Việt nhất quán theo quy ước file (Trượt/Phụt/Thúc/Xuyên thấu/Siết...). Các SFX ちゅむううううっ→"Chùn chụt" (2062), じゅぶううううっっっ→"Phập" (2058), きゅううううううんっ→"Siết chặt" (2096), ずにゅううううううっ→"Xuyên thấu" (2091) là diễn-nghĩa, không đếm theo công thức moan — giữ theo quy ước audit đã chốt.
- **Các âm khác đã xét, giữ:** 1201/1259 ああ→"Ừ" (lời đáp, không phải rên — TW 嗯); 1205 ぃ――ぁ→"I――a" ✓; 1206 ぁあ→"Aa" ✓; 1214/1165 くあっ→"Kua" ✓; 1227 ずずっ→"zuzu!", えむっ→"emu!", ろるっ→"Roru" ✓; 1238 れるううっ→"liếm" (diễn-nghĩa) ✓; 1241 ん～～～っ→"ưm~~~" ✓ (sweep already-rendered); 1166 くっ――っ→"Hự――!" ✓; 1283 ぉぉっ→"Ồ" ✓; 1219/1202/1236/1249 くっ→"hự" ✓; 1266 んぷっ→"Ưm phụt" ✓; 1273 ぢゅぶるるっ→"Jubururu" ✓; 1191 むぃ――ぃ～→"anh――hai~" (nói ngọng, giữ như 1234).
- **1234 — giữ (nói ngọng, không phải dòng moan):** JP ひゅひ……らい……ひゅひ là tiếng nói ngọng; VN theo TW "rất thích" — quyết định giữ đã ghi trong MEMORY 22/11 ~02:47.
- **1145 — giữ:** "いったら" mơ hồ; VN theo TW "Rút ra, không được, đâu" — quyết định giữ đã ghi trong MEMORY 22/11 ~02:47.
- **1573 — giữ, đã xét:** JP あーんと、口が開かれる → VN "há to miệng, phát ra tiếng 'Aaa'". Audit giữ với lý do "don't lose the sound"; ん cuối trong あーん là mũi hoá của âm há miệng, "Aaa" là cách diễn tự nhiên trong lời dẫn — không ép thành "Aan". Ghi nhận đã xét, không sửa.

## 4. Cờ cho vòng thống nhất / Hieu (không quyết ở đây)

- **F1 — 1189 (KHÔNG phải dòng moan, chỉ ghi nhận):** MEMORY 22/11 ~02:47 đã quyết — BỎ phần bịa "đã bao phủ" (JP cụt ở がっ, 1190 là dòng rên mới, không tiếp nối), VN mới đã ghi trong MEMORY, áp dụng ở đợt thống nhất. Vòng moan không đụng.
- **F2 — 1215 "Hà!" (fix mới của vòng này):** là ngoại lệ duy nhất của quy ước はっ→"Hà" trong file; nếu parent thấy "A!" là diễn tự nhiên có chủ ý thì loại fix này ở lúc gộp.
- Không có cờ mới nào cần Hieu quyết trong các dòng moan của file này.

## 5. Kiểm chứng cơ học (sau sửa)

- JSON 3 mục (key chuỗi, list-of-dicts), khối TOML 3 khóa, 0 sai lệch giá trị so với JSON.
- jp/tw/old_vn khớp CSV3 tuyệt đối 3/3 (1 bộ duy nhất, 343 dòng, 0 key trùng).
- Mỗi fix chỉ khác old_vn ở đúng chỗ thay đổi mục tiêu (diff-sanity 3/3: 1153 bớt 3 chữ a; 1215 "A"→"Hà"; 1255 chèn ", u").
- Kiểm tra cơ học bắt 1 lỗi mã hoá trong bản nháp JSON (1215/1255 dùng newline thật thay vì `\n` chữ trong jp/tw/old_vn) — đã dựng lại JSON từ CSV3, khớp tuyệt đối.
- Đếm nguyên âm kiểm tra lại bằng máy cho mọi chuỗi moan dài trong file (xem §3) — tất cả khớp, kể cả các fix audit cũ.

## 6. Lượt soát 2

- **3/3/0/0:** đọc lại toàn bộ 3 fix với JP lần hai; 3 tái kiểm chứng, 0 bỏ, 0 sửa.
- Đọc lại toàn bộ 153 dòng rên/SFX lần hai theo JP: không phát hiện thêm dòng sai nào ngoài 3 dòng trên.

## 7. Khối TOML (đã kiểm chứng parse)

```toml
[script]
1153 = "「Hyu! Aaaaaaaaan!!?」"
1215 = "「Hà! Đến rồi! Lại, cái này――Hôn nhau――\\nNgọt ngào quá――Sâu trong, bụng――râm ran, quá」"
1255 = "「Ưm……em hiểu, rồi――hà……phù, u……Làm ướt đều\\n――Làm ướt, đều――thì」"
```

## Kết bài

File 日々姫h5 (343 dòng) đọc hết từng dòng với JP + TW: **3 dòng moan sai** — nguyên âm 1 (1153: 12 a → 9 a, áp lại fix audit đã bị loại với giá trị đúng), moan 2 (1215: はっ "A"→"Hà"; 1255: ぅ bị mất, "phù"→"phù, u"). Đồng ý toàn bộ 37 fix moan/gasp/nguyên âm còn hiệu lực của audit; phán lại và đồng ý cả hai phán đoán của audit (1264 "Nukyu", 1154 "Po"). Không dòng gasp Ư nào bị xem lại, không dòng "Kh" nào bị đổi. Đếm nguyên âm kiểm tra lại bằng máy cho mọi chuỗi moan dài — tất cả khớp. Chi tiết đầy đủ: `moan-hibikih5-hakudaku-enogu-wrong.json` (3 mục, khối TOML 3 khóa, 0 sai lệch, jp/tw/old_vn khớp CSV3 tuyệt đối 3/3; lượt soát 2: 3/3/0/0).
