# Moan-fix — 凪ふかみh2_みずあそび.txt.toml (07_Nagi_Fukami)

File: `07_Nagi_Fukami/凪ふかみh2_みずあそび.txt.toml` — H-scene ba người (Soutetsu + Nagi + Fukami, chơi đùa ở bãi sông).
Phương pháp: đọc từng dòng đối chiếu JP + TW (CSV3), rà lại toàn bộ 34 fix rên romaji của audit + 5 gasp sweep, xét lại mọi dòng rên/SFX còn lại theo quy tắc romaji (MOAN-BRIEF.md).

## 1. Tổng kết
- Đọc: **350/350 dòng** (key 1008–2184).
- Xét: **135 dòng rên/SFX** (86 thoại rên/thở/gasp/cười + 43 SFX độc thoại trong ngoặc + 3 độc thoại gasp + 2 độc thoại thở + 1 độc thoại （おおお）).
- Đổi: **5 dòng** (2 romaji + 2 đếm nguyên âm + 1 sai âm).
- Giữ: **130 dòng rên/SFX**.
- Không sửa dòng nào ngoài rên (không đại từ/thuật ngữ/nghĩa; 1258 sai nghĩa, 1528 thẻ %69 + sai nghĩa, 1852 thuật ngữ 水棹 để nguyên cho vòng audit/thống nhất).

## 2. Kiểm tra file
- TOML md5: `dc5ff6dcb84a35650fb89a8465df9fe0` (khớp md5 audit). Không có bản trùng.
- **Lưu ý đường dẫn:** disk path ghi trong brief (`#U51eah2_#U304a#U3068#U306a#U306e#U6c34#U7740.txt.toml`) thực ra là file **凪h2_おとなの水着** (md5 `a581ef85...`), KHÔNG phải file này. File đúng là `#U51ea#U3075#U304b#U307fh2_#U307f#U305a#U3042#U305d#U3073.txt.toml` (giải mã: 凪ふかみh2_みずあそび) — đã dùng file đúng, md5 khớp.
- CSV3: 1 bộ duy nhất, 350 dòng, key trùng khớp TOML 350/350. JP trong comment TOML khớp CSV3 JP 350/350 (kể cả 2 dòng CSV3 bị mojibake: 1319 JP thực là 「っ！」, 1386 JP thực là 「ああ。わかってる―― / だから、僕もっ！」 — đã kiểm chứng qua TOML).
- JSON: 5 mục, key dạng chuỗi, list-of-dicts (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 5/5. Fix values dùng `\n` literal (không newline thật) theo chuẩn CSV3.
- Khối TOML: 5 khóa, parse bằng tomllib OK, 0 sai lệch giá trị so với JSON. Mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm tra diff cơ học 5/5).

## 3. Kiểm tra lại fix rên của audit (34 dòng)
Audit đã áp romaji đúng quy tắc cho cả 34 dòng rên — **không cần sửa lại dòng nào**:
- ひゃ/ひゅ/ひあ/きゃ → Hya/Hyu/Hia/Kya (1267, 1272, 1273, 1278, 1279, 1280, 1299, 1378, 1428); ひっ → Hi/Hí (1266, 1269, 1283, 1335); ふあ/ふぁ → Fua/Fa (1295, 1310, 1314, 1322, 1328, 1353, 1530); ふきゅ → Fukyu (1276 — xem Cờ F1); ふぎゅ → Fugyu (1303); ふゅ → Fyu (1367); ふぁい → Fai (1372); ぷぁ → Pua (1405); えう → Eu (1374); えむ → Emu (1346); あん → An (1344); いっ → Í (1271); ひえ → Hả (1284, + Fuan).
- Đếm nguyên âm đã kiểm chứng lại độc lập bằng máy: 1274 Ky+14u (きゅ+13う, 1ん), 1277 Hi+ky+9u+nn (1+8う, 2ん) — khớp kiểm chứng của parent lúc merge audit; 1297 Euuu (え+3う = 4 vần).
- 5 gasp sweep (1015, 1294, 1865, 1946, 2019) không đụng, trừ 1294 (xem §4 — chỉ bổ sung đếm nguyên âm, giữ nguyên Ư của audit). 5 already-rendered (1291, 1319, 1330, 1373, 1382) giữ nguyên.
- Không có dòng "Kh" (glottal-stop っ) nào trong file này — "Kh..." ở 1412 là từ "khủng" bị lắp, không phải quy tắc Kh.

## 4. Danh sách sửa (5 dòng)
### 1294 [ふかみ] — đếm nguyên âm (thay thế giá trị audit cùng key)
- JP: 「はぁ……はぁ……はぁっ――は――ああ～っ」
- TW: 「呼……呼……呼……呼……啊」
- Cũ (CSV3): 「Hà... hà... hà——hà——a~」
- Giá trị audit đã gộp: 「Hà... hà... hà——hà——a~Ư」
- Sửa (moan): 「Hàà... hàà... hàà——hà——aa~Ư」
- Lý do: はぁ = 2 mora a mỗi hơi (×3), ああ～ = 2 a — VN cũ chỉ có 1 a mỗi hơi. Tiền lệ: ハチロクh9 2055 はあっ→"haa", lr-mikuro-h 1917 はぁ→"Haa", lr-ハチロクh2 2200 はあっ→2a. Giữ nguyên Ư cuối dòng của audit (gasp sweep) và "hà——" cho は―― (1 mora, đúng). Áp MỘT giá trị moan cho key này ở đợt thống nhất, không áp cả hai.

### 1300 [凪] — romaji (fa tách nhịp)
- JP: 「ふ、あ……太か……ばいっ――んっ――にーさん、 / で――おまん、こ――みちみちっ……いっ、ぱい……で」
- TW: 「呼……好大……嗯……大哥哥……在裡面……滿滿的……」
- Cũ: 「Phù, a... to quá... nha——ưm——anh hai, / đang——lấp đầy... âm, đạo——chật ních... rồi」
- Sửa: 「Fu, a... to quá... nha——ưm——anh hai, / đang——lấp đầy... âm, đạo——chật ních... rồi」
- Lý do: ふ、あ là cặp mora ふあ bị tách bởi dấu phẩy — "phù" sai vần cho ふ (chính audit file này đã lý luận như vậy ở 1295: ふあ là Fua, không phải "phù"). Tiền lệ: ハチロクh9 đổi 5 dòng ふ、あっ→"Fu, a"; lr-ポーレットh1 dùng "Fu, a" cho ふ、あ. Xem Cờ F3 (ハチロクh7 giữ "phù——a", chờ quyết thống nhất).

### 1302 [ふかみ] — đếm nguyên âm
- JP: 「はぁぁぁぁ～～」
- TW: 「呼」
- Cũ: 「Hàààà~~」
- Sửa: 「Hààààà~~」
- Lý do: は+4ぁ = 5 mora a; VN cũ chỉ có 4 a (thiếu 1). Đếm lại bằng máy: 5 a.

### 1326 [ふかみ] — romaji (mất phụ âm mora)
- JP: 「へっ！？　やっ――指っ！？　双鉄さんの―― / 指……先っ――おしり――にっ！？」
- TW: 「哎！？呀……是手指！？是雙鐵先生的……指尖……在屁股……」
- Cũ: 「Hả!? Á——ngón tay!? Của anh Soutetsu—— / đầu... ngón tay——ở hậu môn——sao!?」
- Sửa: 「Hả!? Ya——ngón tay!? Của anh Soutetsu—— / đầu... ngón tay——ở hậu môn——sao!?」
- Lý do: やっ → "Ya" — "Á" làm mất hẳn phụ âm y. Tiền lệ ポーレットh3: "Á" cho やっ là lỗi mất phụ âm mora; や→"Ya"/"Yaa" (890/893/894/897). Giữ "Hả!?" cho へっ (tiếng giật mình, TW 哎).

### 1397 [双鉄H] — sai âm (mất phụ âm)
- JP: 「くおっ！」
- TW: 「噢！」
- Cũ: 「Ư!」
- Sửa: 「Kuo!」
- Lý do: くおっ có phụ âm k rõ ràng — "Ư!" làm mất hẳn. Tiền lệ ポーレットh3 906 くっ→"Ku"; ハチロクh8 2228 ぐ――ぅっ→"Guu". Dấu "!" diễn っ cắt.

## 5. Giữ nguyên có lý do (không sửa — các dòng đáng chú ý)
- **Audit romaji đã đúng (34 dòng, §3):** giữ nguyên toàn bộ giá trị audit, kể cả 1276 "Fukyu" (xem Cờ F1) và 1299 "Hyafa/Hyan" (baby-talk にゅゅーっへ giữ "ưm" — xem Cờ F2).
- **Hơi thở ふっ/ふうっ → "phù":** giữ theo quy ước chung của file (audit §6: không phân biệt độ dài ふ/ふう) — 1271, 1298, 1329, 1369, 1371. Chỉ sửa ふあ/ふぁ (họ fa), không đụng hơi thở ふ đơn.
- **SFX miệng → động từ Việt:** れる/れろ → "liếm" (1030, 1357), họ ちゅ → "chụt" (1358, 1328), れるうっ → "liếm" — quy ước toàn dự án, giữ.
- **Gằn của Soutetsu:** ぬっ――むっ―― → "Hự——ưm——" (1288), うぐっ → "Hự!" (1290) — giữ.
- **Cười là cười:** うふふ → "Ư hứ hứ" (1390, 1391), にへへ～ → "Ni hê hê~" (1395) — tiếng cười tiếng Việt tự nhiên, giữ (không phải rên).
- **Giật mình / ngượng:** ふえっ → "Hả!?" (1324, TW 哎), ふぇ → "he" (1403, TW 哎 — audit giữ), いやぁんっ → "Ối!!" (1323, TW 哎呀 là thán từ).
- **Gasp đã thể hiện:** 1319 っ！ → "Á!" (sweep already-rendered, audit giữ); 1330 むうう～っ → "Ưmmmm~"; 1381 んぐっ → "Ưm" (tiền lệ 凪h2 2428); 1382 んぶううっ → "Ưm!?" (sweep already-rendered; "Mbuuu" không rõ ràng hơn).
- **Nói ngọng / lắp (không phải rên):** ひょははい → "Vâng nha!" (1421), はふぁっふぁ！ ほーはひっ！！ → "Vâng ạ! Không vấn đề gì nha!!" (1455, TW diễn nghĩa).
- **Thán từ ああ:** 1341 ああ…… → "A..." (thán từ "à, ra là vậy", dấu ... diễn độ dài), 1327 ああ → "À." — giữ, phân biệt với hơi thở はぁ ở 1294 (rên thở dốc, đếm theo công thức).
- **わ → "oa" đúng:** 1412 す……ご……わ…… → "Kh... khủng... oa..." (JP là わ, khác hẳn ふあ → "Oa" sai ở 1310/1314/1322 mà audit đã sửa).
- **SFX độc thoại （ ） (43 dòng):** giữ theo quy ước onomatopoeia Việt của file (Phụt/Phập/Trượt/Cọ/Tũm...) — xem Cờ F5 về quy ước độ dài.
- **Không sửa:** 1293 あのっ → "cái đó——" (っ ngắt câu đã thể hiện bằng ——); 1027 ふかみっ――凪っ (っ gắn tên riêng); 1337 あちゅっ → "nóng quá" (audit: diễn ý "nóng"); 1370 ふにゅっ → "mềm" (diễn nghĩa); 1373 ぐっ → "ực" (tiếng nuốt); 1290/1288 đã nêu trên.

## 6. Kiểm tra sweep gasp
Đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`: file này có **10 mục** — 5 fix Ư đã áp qua audit (1015, 1294, 1865, 1946, 2019) và 5 already-rendered (1291, 1319, 1330, 1373, 1382). Không đụng dòng gasp Ư nào, trừ 1294 (chỉ thêm nguyên âm, giữ Ư — §4). Không có dòng "Kh" nào bị đổi.

## 7. Lượt soát 2 (bắt buộc)
- Đã đọc lại toàn bộ 5 fix đối chiếu từng JP: **5/5 tái kiểm chứng, 0 bỏ, 0 sửa**.
- Đếm nguyên âm kiểm chứng lại bằng máy: 1294 tổng 9 chữ a/à (2+2+2+1+2, khớp JP はぁ×3 + は + ああ); 1302 tổng 5 chữ a (khớp は+4ぁ).
- Lỗi bắt được trước lượt soát 2: 2 fix ban đầu dùng newline thật thay vì `\n` literal (1300, 1326) — đã sửa về `\n` literal theo chuẩn CSV3 trước khi soát 2; diff sau sửa chỉ còn đúng token rên (1300: "Phù"→"Fu"; 1326: "Á"→"Ya").

## 8. Cờ cho Hieu / đợt thống nhất (không quyết)
- **F1 — 1276 ふきゅっ→"Fukyu" vs "Phù kiu":** giữ giá trị audit "Fukyu" (Hepburn đúng; tiền lệ 3 file moan đã gộp: Hachiroku h6 824, h7 750, Fukami h3 2287). Câu hỏi gốc từ audit, chờ Hieu — nếu Hieu chọn "Phù kiu" thì đợt thống nhất sửa lại.
- **F2 — 1299 baby-talk:** にゅゅーっへ (tiếng líu nhí miệng đầy) giữ "ưm" theo audit — ghi nhận, không quyết thêm.
- **F3 — dạng tách fa:** 1300 đã đổi sang romaji "Fu, a" (theo h9 + lr-h1), NHƯNG ハチロクh7 giữ "phù——a"/"phù, a" (11 dòng, theo tiền lệ audit trong file đó) — cần quyết MỘT dạng duy nhất toàn dự án ở đợt thống nhất.
- **F4 — 1350 び，あっ！:** âm び bị rơi hẳn trong cả TW (啊) lẫn VN ("Á!") — không rõ び là mảnh âm hay từ bị cắt dở; không tự sửa, cần vòng audit quyết.
- **F5 — quy ước độ dài SFX độc thoại （ ）:** 9 dòng JP rên dài bị diễn ngắn hoặc kéo bằng phụ âm: 2132 びゅるうううっ→"Phụttttt!", 2141 ぬろおおおおおおおおおおおっ→"Trơn tuộtttt!", 2149/2150 ずるうううううううううううっ→"Rútttt!!"/"Rúttttt!", 2154 ずぶううっ→"Phậppppp!", 2155 ずぬうううううううううっ→"Phập!" (mất hẳn độ dài 9 mora), 2160 うにゅうううううううううううっ→"Nhu động!!", 2174 ぬろおおおおおおおっ→"Trơn tuột!", 2182 ずろおおおおおおおおおおっ→"Trượt vào!", 2165 キチチチチっ→"Chít chít chít" (4 チ → 3 lần). Cùng nhóm cờ với h9/h3 (SFX （ ） chưa áp công thức đếm) — cần quyết quy ước toàn dự án, không sửa lẻ từng dòng.
- **F6 — 1294 thay thế giá trị audit vừa gộp:** audit (gộp 22/11 ~02:25) thêm Ư; moan giữ Ư và thêm đếm nguyên âm. Áp MỘT giá trị moan cho key này ở đợt thống nhất; parent kiểm chứng lại khi merge.
- **F7 — brief ghi sai disk path:** đường dẫn trong task trỏ tới 凪h2_おとなの水着 (md5 `a581ef85...`); file đúng đã dùng là `#U51ea#U3075#U304b#U307fh2_#U307f#U305a#U3042#U305d#U3073.txt.toml`, md5 `dc5ff6dc...` đã kiểm chứng.

## 9. Khối TOML (đã kiểm chứng parse)
```toml
"1294" = "「Hàà... hàà... hàà——hà——aa~Ư」"
"1300" = "「Fu, a... to quá... nha——ưm——anh hai,\\nđang——lấp đầy... âm, đạo——chật ních... rồi」"
"1302" = "「Hààààà~~」"
"1326" = "「Hả!? Ya——ngón tay!? Của anh Soutetsu——\\nđầu... ngón tay——ở hậu môn——sao!?」"
"1397" = "「Kuo!」"
```

## Kết bài
Đã moan-fix xong 凪ふかみh2_みずあそび.txt.toml: 350 dòng đọc, 135 dòng rên/SFX xét, đổi 5 dòng (2 romaji: 1300 "Fu, a", 1326 "Ya"; 2 đếm nguyên âm: 1294 thêm 4 a, 1302 thêm 1 a; 1 sai âm: 1397 "Kuo!"), giữ 130 dòng. Audit đã làm rất kỹ họ romaji cho file này (34/34 dòng đúng, đếm nguyên âm 1274/1277 đã kiểm chứng lại) nên đợt moan này chủ yếu bắt các dòng audit bỏ sót. Không đụng dòng gasp Ư nào (trừ giữ Ư của audit ở 1294), không đổi dòng "Kh" nào (file không có), không sửa ngoài phạm vi rên. Lượt soát 2: 5/5 tái kiểm chứng, 0 bỏ, 0 sửa. Khối TOML 5 khóa parse OK, 0 sai lệch. Cơ sở tổng đã kiểm chứng lại từ moans/ROUTE-MOANS.md (47 file / 1239 dòng); sau file này: 48 file / 1244 dòng sai (moan).
