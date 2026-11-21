# Moan-fix review — lr_日々姫真闇h1_三人家族.txt.toml (moan-lr-hibiki-mayami-h1-sannin-kazoku)

File H-scene route 02_Hibiki: Hibiki + Mayami, "gia đình ba người" (Soutetsu + Hibiki + Mayami). Audit đã merge trước đó: 60/436 sai (ROUTE-AUDIT.md).

## §1. Kiểm chứng file

- File TOML: `sources/toml2/translation_toml/02_Hibiki/lr_#U65e5#U3005#U59eb#U771f#U95c7h1_#U4e09#U4eba#U5bb6#U65cf.txt.toml`
- TOML md5: `d8f257e11854179d1a64585836ad9112` (UTF-8 BOM + CRLF, 900 dòng). Không có bản trùng (chỉ 1 file trên đĩa, không thuộc nhóm 11 duplicate).
- Script: 436 dòng (monologue 184, 日々姫 88, 真闇 85, 双鉄 79). Key 36–2484 (thưa).
- CSV3: 1 bộ duy nhất (`translation_toml\02_Hibiki\lr_日々姫真闇h1_三人家族.txt.toml`), 436 dòng, 0 key trùng.
- VN khớp TOML: 435/436. 1 dòng còn lại (1420) chỉ khác TOML-2 làm phẳng `\n` literal thành khoảng trắng (đã biết, không phải lỗi).
- Audit file này đã merge 60 fix (xem `audit-lr-hibikimayami-h1-san-nin-kazoku-wrong.json`), trong đó 37 fix rên/gasp/đếm nguyên âm — moan pass này kiểm chứng lại toàn bộ, không sửa trùng trừ 2 dòng nêu ở §5.

## §2. Kiểm kê rên (moan inventory)

- Đã đọc 436/436 dòng; xét 248 dòng rên/SFX/gasp:
  - Thoại rên: 169 dòng (真闇 64, 双鉄 50, 日々姫 49 + 6 dòng VN có render rên) — rên dài, hơi thở, gasp っ, họ ふぁ/ふあ/ふや, họ ひゃ/ひゅ/ひあ/きゃ, cười ふふ/んふふ, SFX liếm/mút/chụt.
  - Độc thoại SFX trong （ ）: 79 dòng (chủ yếu ずりゅっ/むにゅっ/ぢゅるっ/びゅるっ/きゅううう… và さすっ/なぜぇ… — đã diễn bằng từ Việt theo quy ước file: "Trơn tuột", "Phụt", "Co thắt", "Vuốt", "Xoa xoa"…).
- Đổi 3 dòng: 1 tách âm rên (1550) + 2 đếm nguyên âm (1555, 1619).
- Giữ 245 dòng rên/SFX (chi tiết §4).

## §3. Các dòng sửa (3 dòng)

### 1550 — 双鉄 — tách âm rên (moan-fragment)

- JP: 「ああああああっ！！！」
- TW: 「啊啊啊啊啊啊！！！」
- VN cũ: 「A a a a a a!!!」
- VN mới: 「Aaaaaa!!!」
- Lý do: JP là MỘT âm rên dài duy nhất (あ×6 + っ, không có 、 hay dấu ngắt nào); TW cũng liền một mạch. VN cũ tách thành 6 mảnh rời "A a a a a a" — đọc thành 6 tiếng kêu ngắn riêng biệt, sai nhịp. Gộp thành một cách diễn romaji duy nhất "Aaaaaa" (6 a = đúng số mora JP; っ cắt cuối đã diễn bằng !!! — tiền lệ 1559 ああっ→"Aa!!!!!", 1471 ああっっ→"aa!!"). Tiền lệ lỗi tách âm: ふかみh1 ("Hya ah ưm", "Hi ah" → gộp romaji).

### 1555 — 日々姫 — đếm nguyên âm (vowel-count) — THAY THẾ phần đếm của fix audit

- JP: 「あっ！　ふあっ！　あっ！！！　んウゥゥぅ～っ！！」
- TW: 「啊！呼啊！啊！！！嗯唔唔唔唔～！！」
- VN cũ: 「A! Fua! A!!! Nguuuuu~!!」
- VN mới: 「A! Fua! A!!! Nguuuu~Ư!!」
- Lý do: JP んウゥゥぅ = ウ + ゥ + ゥ + ぅ = 4 âm u (đếm mora nghiêm ngặt); TW xác nhận 嗯 + 4×唔. VN cũ có 5 u ("Nguuuuu") — thừa 1 u. Audit đã sửa dòng này dạng lost-gasp-trailing (thêm Ư cuối) nhưng GIỮ NGUYÊN 5 u — kiểm chứng độc lập ở đây phát hiện thừa. Giá trị moan giữ phần Ư của audit, chỉ sửa số u 5→4. Cờ cho đợt thống nhất (§5).

### 1619 — 日々姫 — đếm nguyên âm (vowel-count) — THAY THẾ giá trị audit

- JP: 「はぁい。ねぇね。あ、喉、絡むから気をつけてね？\nん……『あーーーーーーん』」
- TW: 「好了，阿姐。啊，會有些黏喉嚨，要注意一點哦？嗯……“啊————嗯”」
- VN cũ: 「Đây. Chị hai. A, coi chừng vướng ở cổ họng nhé?\nƯm…… 'Aaaaaan'」
- VN mới: 「Đây. Chị hai. A, coi chừng vướng ở cổ họng nhé?\nƯm…… 'Aaaaaaan'」
- Lý do: JP 『あーーーーーーん』 = あ + 6×ー = 7 mora a. VN cũ 'Aaaaaan' = 6 a (thiếu 1). Audit sửa thành 'Aaaaaaaan' = 8 a (thừa 1) — audit áp cùng giá trị 8 a cho cả 1579 (JP あ+7ー = 8, đúng) lẫn 1619 (JP あ+6ー = 7, sai). Đếm lại từng ký tự: 1619 có 6 dấu ー, 1579 có 7 dấu ー. Giá trị đúng duy nhất: 7 a ('Aaaaaaan'). Cờ cho đợt thống nhất (§5).

## §4. Giữ nguyên (không tính sai)

- **Họ ひゃ/ひゅ/ひあ/きゃ đã romaji đúng, không có "Á"**: 1452 きゃっ→"Kya!?", 1449 きゃうっ→"Kyau", 1434 きゃふうううっっ→"Kyafuuuu" (4 u = ふ+う×3), 1438 ひゃきゅっ→"Hyakyu", 1612 ひゃきゅんっ→"Hyakyun", 1445 ひあっつ→"Hiat" (t cuối diễn っつ, âm không mất), 1454 ひあっ→"Hia!?", 1450/1443/1427/1441 ひゃっ/ひゃあああっ→"Hya"/"Hyaaaa" (4 a), 1431 ひゃぐっ→"Hyagu", 1432 ひゃうううううう→"Hyauuuuuu" (6 u), 1440 ひゅあ…あん→"Hyua…aaan" (19 a, audit đã sửa đúng), 1439 ひゅっ→"Hyu". Không có dòng nào trong file dùng "Á" cho họ này.
- **Họ ふぁ/ふあ/ふや đã romaji đúng**: ふあっ→"Fua" (1480, 1476, 1474, 1805, 1447, 1441, 1555), ふぁっ→"Fua" (1476), ふぁんっ→"Fuan" (1481), ふやっ→"Fuya" (1471), ふやぁぁぁっ→"Fuyaaaa" (1467, audit đã sửa đúng 4 a), ふぁぁ…→"Fua…" dài (1477/1478/1479, audit đã sửa đúng 19/18/14 a), ぷあっ/ぷぁ→"Pua"/"pua" (1607, 1577, 1581, 1583, 1621, 1608), くあっ→"Kua" (1460–1463, 1520), くはっ→"Kuha" (1485, 1651), くっ→"Ku" (1464–1466, audit đã sửa くっ→"Ku" ở 1390/1513/1615 từ "Ư"/"ư" — đúng, giữ).
- **Tách âm theo JP — JP tách thì VN tách theo, KHÔNG gộp** (tiền lệ moan-lr-mayamih1 1436 + parent-verified "audit gán sai 'phà, a' cho ふ tách riêng, phải là 'Fu, a'"): 1450 ふ、あっ、→"Fu, a,"; 1471 ふ、ぁっ→"fu, a"; 1484 ふ、ぁ――→"Fu, a――" — JP có dấu 、 ngắt nhịp, VN tách theo là đúng. Chỉ 1550 là tách sai (JP không có dấu ngắt nào).
- **Đếm nguyên âm của audit kiểm chứng độc lập — 8/9 đúng**: 1440 19 a, 1441 6 a, 1446 20 u (きゅ+ぅ×14+う×5), 1467 4 a, 1477 19 a, 1478 18 a, 1479 14 a, 1611 10 o — đều khớp JP (đếm từng ký tự). Chỉ 1619 sai (xem §3). 1579 (không nằm trong 9 fix a-run của audit) cũng đúng: 『あーーーーーーーん』 8 a → 'Aaaaaaaan'.
- **Cười là tiếng cười**: んふふ→"Nfufu" (1598), んふふふふっ→"Nfufufufu" (1599), うふふっ→"Ufufu" (1517).
- **んっ/うん/む → "Ưm/Ừm/Mư"**: 1580, 1574, 1761, 1523/1605, 1524, 1515, 1512, 1586, 1605 — đều tự nhiên, giữ.
- **はぁっ/はあっ → "Hà"**: 1789, 1786, 1788, 1790, 1785, 1787, 1496 (audit đã thêm Ư cuối), 1619 — giữ.
- **SFX độc thoại diễn bằng từ Việt** (quy ước file, audit §5 giữ): 36/2461/2462/2464/2465/2407/2386/2400/2405/2409/2410/2416/2417/2419/2420/2426/2428/2432/2433/2435/2438–2446/2451–2454/2458/2459/2463/2467/2473–2476/2481/2483/2484 (Trơn tuột, Phụt, Co thắt, Mềm mại, Vuốt, Xoa xoa, Cọ xát, Nảy lên…) — độ dài "tttt"/"aaaa" trong từ Việt chỉ là nhấn nhá, không áp công thức đếm mora nghiêm ngặt (tiền lệ moan-lr-mayamih1 §4: chỉ sửa khi vượt xa tiền lệ).
- **Gasp Ư đã sửa — KHÔNG đụng lại**: toàn bộ 24 mục sweep audit đã áp (1042, 1044, 1061, 1439, 1458, 1496, 1508, 1525, 1530, 1551–1553, 1557, 1561–1566, 1571, 1608, 1712, 1736) — xem §6.
- **"Kh"**: file này không có dòng "Kh" nào (くっ đã được audit sửa thành "Ku" ở 1390/1513/1615 — không phải "Kh", không đụng).
- **1493 KEEP "em"** (quyết định audit 21/11 ~18:55 — Mayami gọi Soutetsu là "em"): đây là đại từ, không thuộc phạm vi moan; dòng này không có âm rên nào nên không chạm tới.

## §5. Cờ cho đợt thống nhất (2 cờ — cả 2 đều THAY THẾ phần đếm nguyên âm của giá trị audit)

### Cờ 1 — 1555: dùng giá trị moan 「A! Fua! A!!! Nguuuu~Ư!!」 (4 u), KHÔNG dùng fix audit 「A! Fua! A!!! Nguuuuu~Ư!!」 (5 u)

- JP んウゥゥぅ = 4 u; TW 嗯唔唔唔唔 = 4 唔. Audit chỉ thêm Ư, bỏ qua số u. Giữ Ư của audit, sửa 5 u → 4 u.

### Cờ 2 — 1619: dùng giá trị moan 「…Ưm…… 'Aaaaaaan'」 (7 a), KHÔNG dùng fix audit 「…Ưm…… 'Aaaaaaaan'」 (8 a)

- JP 『あーーーーーーん』 = あ + 6×ー = 7 a (đếm từng ký tự; khác 1579 là あ + 7×ー = 8 a). Audit áp nhầm cùng giá trị 8 a cho cả hai dòng.

## §6. Kiểm chứng sweep gasp

- Sweep có **26 mục** cho file này (đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`):
  - **24 mục audit đã áp nguyên, kiểm chứng đúng, không đụng lại**: 1042, 1044, 1061, 1439, 1458, 1496, 1508, 1525, 1530, 1551, 1552, 1553, 1555 (chỉ phần Ư — phần đếm u xem §3/§5), 1557, 1561, 1562, 1563, 1564, 1565, 1566, 1571, 1608, 1712, 1736. So sánh cơ học: fix audit = fix sweep 24/24, 0 sai lệch.
  - **2 mục already-rendered, kiểm chứng đúng, không sửa**: 1432 (ひゃうううううう～～～っ giữa dòng, sau đó có ！？ diễn độ cắt — っ không mất hẳn) và 1723 (ん～～～～～～っ cuối dòng, âm cuối là ん → "ưm" — phụ âm cuối m đã diễn độ cắt, tiền lệ ハチロク01 2319 んあーんっ → không thêm Ư).
- Không có dòng "Kh" nào trong file bị đổi sang Ư. Không có dòng gasp Ư nào bị xem lại.

## §7. Lượt soát 2 (second pass)

- Đọc lại toàn bộ 3 giá trị fix so với JP + TW sau lượt đầu, kèm đếm cơ học lại từng ký tự: 1550 (JP あ×6 = 6 a, TW 啊×6 liền mạch), 1555 (JP ウ+ゥ+ゥ+ぅ = 4 u, TW 4×唔), 1619 (JP あ+6×ー = 7 a; đối chiếu 1579 あ+7×ー = 8 a để khỏi nhầm).
- Tổng: 3 / tái kiểm chứng: 3 / bỏ: 0 / sửa: 0.
- JSON 3 mục, khóa string, jp/tw/old_vn khớp CSV3 3/3. Khối TOML parse bằng tomllib: 3 khóa, 0 sai lệch giá trị.

## §8. Khối TOML (parse-verified bằng tomllib: 3 khóa, 0 sai lệch giá trị so với wrong.json)

```toml
[script]
"1550" = "「Aaaaaa!!!」"
"1555" = "「A! Fua! A!!! Nguuuu~Ư!!」"
"1619" = "「Đây. Chị hai. A, coi chừng vướng ở cổ họng nhé?\\nƯm…… 'Aaaaaaan'」"
```

Lưu ý: trong khối TOML trên, `\\n` là ký tự xuống dòng đã escape (giá trị thực trong JSON/TOML là `\n` literal như CSV3).

## Kết bài

File lr_日々姫真闇h1_三人家族: đã đọc 436/436 dòng, xét 248 dòng rên/SFX/gasp, đổi 3 dòng (1550 gộp 1 âm rên dài bị tách thành 6 mảnh "A a a a a a" → "Aaaaaa"; 1555 sửa đếm u 5→4 theo JP んウゥゥぅ + TW 4×唔; 1619 sửa đếm a 8→7 theo JP あ+6ー — cả hai đều thay thế phần đếm nguyên âm của fix audit). Audit file này đã làm rất kỹ (37 fix rên/gasp, kiểm chứng độc lập đúng 8/9 đếm nguyên âm + 24/24 sweep), nên moan pass chỉ còn 3 lỗi lẻ tẻ. 2 cờ cho đợt thống nhất (1555 + 1619, đều thay thế giá trị audit về số nguyên âm). Không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào (file không có "Kh").
