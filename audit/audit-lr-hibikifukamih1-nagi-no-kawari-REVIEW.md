# Audit — lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml

**File:** `lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml` — route 02_Hibiki (Hibiki route, H-scene Hibiki + Fukami, "thay cho bé Nagi")
**Đường dẫn TOML:** `sources/toml2/translation_toml/02_Hibiki/lr_#U65e5#U3005#U59eb#U3075#U304b#U307fh1_#U51ea#U3061#U3083#U3093#U306e#U4ee3#U308f#U308a.txt.toml`
**MD5 TOML:** `1975c8fad55084e81cc0031905781f87` — 1 bản duy nhất, không có file trùng (11 nhóm trùng của dự án không chứa file này).
**CSV3:** 1 bộ duy nhất (485 dòng, File = `translation_toml\02_Hibiki\lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml`), 0 khóa trùng, 0 VN trống. Khớp phẳng VN với TOML 485/485 (sau chuẩn hoá `\n`→khoảng trắng của TOML-2). Cảnh báo dual-set trong task KHÔNG xảy ra với file này — không có bộ stale 07_Nagi_Fukami cho file này.

## Kết quả tổng

- **Đã đọc: 485/485 dòng script** (độc thoại 210, Soutetsu 85, Hibiki 96, Fukami 94), đọc từng dòng đối chiếu JP + TW.
- **Sai: 68 dòng (14,0%)**.
- **Phân loại:**
  - っ thô còn sót trong VN (raw-tsu): 39
  - gasp っ bị mất (lost-gasp): 8
  - bịa quan hệ huyết thống (義→nuôi) (kinship-fabrication): 8
  - bịa quan hệ huyết thống + gasp っ bị mất (kinship-fabrication+lost-gasp): 1
  - sai số lượng nguyên âm (rên) (vowel-count): 6
  - dịch sai nghĩa (mistranslation): 3
  - sai sắc thái (câu trần thuật thay vì câu hỏi) (meaning): 1
  - tách sai từ (にいさん) (word-split): 1
  - mất âm mora (ん) (sound-loss): 1
- **Lệch dòng (misaligned): 0.** Không có dòng VN nào thuộc về key khác, không có chuỗi xoay (rotation). JP↔TW khớp nhau xuyên suốt file; các lỗi đều là lỗi cục bộ trong từng dòng (gasp, nguyên âm, bịa từ), không phải lệch hàng.
- **Nhiễm chéo (contamination): 0.** Không có dòng VN nào lấy từ file khác.
- **Mồ côi (orphan): 0.** Mọi dòng VN đều có JP tương ứng.
- **Chưa dịch (untranslated): 0.** Không có VN trống.
- **Khóa trùng (duplicate keys): 0.** 485 khóa duy nhất, khớp tuyệt đối với TOML (485 khóa).
- **Tag %l: 0 vấn đề.** File này không có tag %l nào trong JP lẫn VN. Có 3 ruby JP ([だ,1] key 1526, [とど] key 1658, [にじ] key 2226) — VN bỏ đúng, không phải lỗi.
- **[characters] / [character_subs]: đúng.** 1834=Fukami, 1916=Soutetsu, 2096=Hibiki; subs 2141=Hibiki, 2217=Fukami, 2309=Soutetsu. [selections] rỗng.
- **Đại từ Soutetsu: đúng toàn file.** Soutetsu xưng "anh" với Hibiki và Fukami (đúng quy tắc đã sửa: "anh" với Hibiki/Michiko/Paulette/Reina/Fukami/Nagi), không có dòng nào cần sửa đại từ.
- **Cặp Nagi–Fukami: đúng.** Không có "chị"/"em" sai cho cặp này trong file (Nagi→Fukami "bé", Fukami→Nagi "cậu" giữ đúng ở các dòng nhắc tới).

## Đối chiếu sweep っ-gasp

- Sweep có **45 mục** cho file này (`sweep-raw-gasp-wrong.json`); đã kiểm từng mục với JP: **45/45 đúng, nhận hết** (39 raw-tsu + 6 lost-gasp, gồm 1305/1390/1777/1785/2316).
- **10 mục sweep có old_vn lệch với CSV3** (1305, 1408, 1431, 1777, 1900, 1968, 2226, 2230, 2316, 2318): sweep lưu dạng TOML đã flatten `\n`→khoảng trắng; fix trong JSON này đã dựng lại từ VN CSV3 (giữ `\n` nguyên), chỉ thay đổi đúng chỗ gasp. CSV3 là chuẩn theo brief.
- **Sweep bỏ sót 3 gasp**, audit bắt thêm: 1327 (ひゃっうっ → "HyauƯ"), 1384 (はうっっ → "HauƯ"), 1700 (っ đầu dòng 2 → "Ư!!"). Cả ba đều là っ tuyệt đối-cuối/đầu-dòng không dấu câu, theo đúng quy tắc gasp đã khóa 20/11 (tiền lệ nêu tên: はうっ).
- Đã quét toàn file bằng máy cho mọi đoạn kết bằng っ (sau khi lột 」 và !?！？。…): các trường hợp còn lại đều đã được diễn (dấu ―― / ! / . / xuống dòng), hoặc là っ gắn với từ nội dung (tên riêng, だっ, わわっ, くれてっ — xem "Giữ nguyên có lý do").

## Từng dòng sai (68)

### Key 933 — 日々姫 — raw-tsu
- JP: `「っ――っ――～～～っ！　――ぁ――はぁっ、はぁっ」`
- TW: `「——嗚～～～！　——啊——蛤啊，蛤啊」`
- VN cũ: `「っ――っ――~~~っ! ――A――hà, hà」`
- Sửa: `「Ư――Ư――~~~Ư! ――A――hà, hà」`
- Lý do: Sweep raw-tsu: 3 lần っ thô trong VN → Ư. Đuôi はぁっ→"hà" giữ nguyên (っ sau はぁ có dấu 、 theo sau, không phải cuối tuyệt đối).

### Key 962 — 双鉄 — meaning
- JP: `「……日々姫の膣に、子宮に。僕の精子を注ぎ込んでも」`
- TW: `「……我可以把精液射在你的陰道、子宮裡嗎」`
- VN cũ: `「……Vào âm đạo, vào tử cung của Hibiki. Dù anh có rót tinh trùng của mình vào.」`
- Sửa: `「……Vào âm đạo, vào tử cung của Hibiki. Anh có thể rót tinh trùng của mình vào được không?」`
- Lý do: JP kết bằng 〜ても (câu hỏi bỏ lửng), TW dịch rõ là câu hỏi (我可以……嗎). VN cũ là câu trần thuật ("Dù anh có...") → sửa thành câu hỏi.

### Key 1261 — 日々姫 — word-split
- JP: `「ううん――まだ――です。まだ――です、にい、さん」`
- TW: `「不——還沒有。還沒有——哥哥」`
- VN cũ: `「Không――vẫn chưa――đâu. Vẫn chưa――đâu, anh, trai.」`
- Sửa: `「Không――vẫn chưa――đâu. Vẫn chưa――đâu, anh, hai.」`
- Lý do: にい、さん bị tách thành "anh, trai" — "trai" không phải từ tách của "anh hai" (にいさん = anh hai). Sửa "trai"→"hai", giữ dấu phẩy ngắt.

### Key 1305 — 双鉄 — lost-gasp
- JP: `「いま、僕の亀頭は、ふかみの膣の最奥、にっ――っ――\n子宮口に、あたって――っ！！！？」`
- TW: `「剛剛，我的龜頭碰到了深美陰道的最深處——碰到子宮口——！！！？」`
- VN cũ: `「Bây giờ, quy đầu của anh, đang chạm vào nơi sâu nhất trong âm đạo của Fukami――\nchạm vào, cổ tử cung――!!!?」`
- Sửa: `「Bây giờ, quy đầu của anh, đang chạm vào nơi sâu nhất trong âm đạo của Fukami――\nchạm vào, cổ tử cung――Ư!!!?」`
- Lý do: Sweep lost-gasp-trailing: っ cuối sau ―― bị mất hoàn toàn → thêm Ư. Fix dựng lại từ VN CSV3 (giữ \n).

### Key 1327 — 日々姫 — lost-gasp
- JP: `「ひゃっうっ」`
- TW: `「呀嗚」`
- VN cũ: `「Hyau」`
- Sửa: `「HyauƯ」`
- Lý do: Sweep BỎ SÓT: ひゃっうっ là tiếng rên, っ cuối tuyệt đối không dấu câu theo sau → mất hoàn toàn. Theo quy tắc gasp (はうっ là tiền lệ nêu tên trong brief) → thêm Ư.

### Key 1332 — 日々姫 — raw-tsu
- JP: `「っ！！！！！」`
- TW: `「呀！！！！！」`
- VN cũ: `「っ!!!!!」`
- Sửa: `「Ư!!!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1333 — 日々姫 — sound-loss
- JP: `「ひゃんっ！！！？」`
- TW: `「呀！！！？」`
- VN cũ: `「Hya!!!?」`
- Sửa: `「Hyan!!!?」`
- Lý do: ひゃんっ → "Hya" làm mất mora ん. So sánh 1328 (～～～んっ → "~~~n" giữ n). Sửa "Hya"→"Hyan".

### Key 1338 — 双鉄 — raw-tsu
- JP: `「っ！」`
- TW: `「呃！」`
- VN cũ: `「っ!」`
- Sửa: `「Ư!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1339 — 双鉄 — raw-tsu
- JP: `「っ！！　～～～っ――。いくぞ、日々姫」`
- TW: `「呃！！　我要來了，日日姬」`
- VN cũ: `「っ!! ~~~っ――. Bắt đầu nhé, Hibiki.」`
- Sửa: `「Ư!! ~~~Ư――. Bắt đầu nhé, Hibiki.」`
- Lý do: Sweep raw-tsu: 2 lần っ thô → Ư.

### Key 1341 — 双鉄 — raw-tsu
- JP: `「っ！！！！！」`
- TW: `「呃！！！！！」`
- VN cũ: `「っ!!!!!」`
- Sửa: `「Ư!!!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1342 — 双鉄 — raw-tsu
- JP: `「っ！！！！？」`
- TW: `「呃！！！！？」`
- VN cũ: `「っ!!!!?」`
- Sửa: `「Ư!!!!?」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1343 — 双鉄 — raw-tsu
- JP: `「～～～っ！！！」`
- TW: `「呃～～～！！！」`
- VN cũ: `「~~~っ!!!」`
- Sửa: `「~~~Ư!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1344 — 双鉄 — raw-tsu
- JP: `「～～～～っ！！」`
- TW: `「呃～～～～！！」`
- VN cũ: `「~~~~っ!!」`
- Sửa: `「~~~~Ư!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1355 — 双鉄 — raw-tsu
- JP: `「ふぁっ――あっ――っ――あっ――あっ！！」`
- TW: `「呼啊——啊——啊——啊！！」`
- VN cũ: `「Fua――a――っ――a――a!!」`
- Sửa: `「Fua――a――Ư――a――a!!」`
- Lý do: Sweep raw-tsu: っ đứng một mình giữa hai dấu ―― → Ư.

### Key 1357 — ふかみ — vowel-count
- JP: `「ふぁぁぁぁぁぁぁぁぁぁぁぁぁっぁあっぁぁぁんっ！」`
- TW: `「呼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！」`
- VN cũ: `「Fuaaaaaaaaaaaaaaaaaaaaaaan!」`
- Sửa: `「Fuaaaaaaaaaaaaaaaaaan!」`
- Lý do: Đếm nguyên âm bằng máy: JP có 18 mora a (ふぁ + ぁ×13 + あ + あ + ぁ×2), VN cũ có 23 chữ a → thừa 5. Sửa về 18 a.

### Key 1358 — ふかみ — vowel-count
- JP: `「ふぁふゅぅぅぅぅぅぅぅぅぅぅぅぅぅっんんっ！！」`
- TW: `「呼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！！」`
- VN cũ: `「Fuafyuuuuuuuuuuuuuuuưm!!」`
- Sửa: `「Fuafyuuuuuuuuuuuuuuưm!!」`
- Lý do: Đếm nguyên âm bằng máy: JP có ぅ×13 sau ふぁふゅ, VN cũ có 14 u trong dãy chạy → thừa 1. Sửa dãy u về 13 (giữ "ưm" cho んんっ).

### Key 1359 — 日々姫 — vowel-count
- JP: `「ふやぁぁぁぁああああっ！」`
- TW: `「呼啊啊啊啊啊啊啊啊！」`
- VN cũ: `「Fuyaaaaaaaa!」`
- Sửa: `「Fuyaaaaaaaaa!」`
- Lý do: Đếm nguyên âm bằng máy: JP có 9 mora a (や + ぁ×4 + あ×4), VN cũ có 8 chữ a → thiếu 1. Thêm 1 a.

### Key 1384 — 日々姫 — lost-gasp
- JP: `「はうっっ」`
- TW: `「哈嗚」`
- VN cũ: `「Hau」`
- Sửa: `「HauƯ」`
- Lý do: Sweep BỎ SÓT: はうっっ là tiếng rên, っ cuối tuyệt đối không dấu câu theo sau → mất hoàn toàn. Brief nêu đích danh はうっ là gasp cần thêm Ư → "HauƯ" (1 Ư cho cả っ kép).

### Key 1390 — 日々姫 — lost-gasp
- JP: `「っ！？」`
- TW: `「哎！？」`
- VN cũ: `「!?」`
- Sửa: `「Ư!?」`
- Lý do: Sweep lost-gasp-whole: cả dòng chỉ có っ+!? mà VN chỉ còn dấu câu → thêm Ư.

### Key 1400 — ふかみ — raw-tsu
- JP: `「っ！！」`
- TW: `「唔！！」`
- VN cũ: `「っ!!」`
- Sửa: `「Ư!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1401 — 双鉄 — raw-tsu
- JP: `「っ！！！」`
- TW: `「唔！！！」`
- VN cũ: `「っ!!!」`
- Sửa: `「Ư!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1402 — 双鉄 — raw-tsu
- JP: `「っ！！！！」`
- TW: `「唔！！！！」`
- VN cũ: `「っ!!!!」`
- Sửa: `「Ư!!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1403 — 双鉄 — raw-tsu
- JP: `「っ！！！！！」`
- TW: `「唔！！！！！」`
- VN cũ: `「っ!!!!!」`
- Sửa: `「Ư!!!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1404 — 日々姫 — raw-tsu
- JP: `「っ！！！！！！」`
- TW: `「唔！！！！！！」`
- VN cũ: `「っ!!!!!!」`
- Sửa: `「Ư!!!!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1405 — 日々姫 — raw-tsu
- JP: `「っ！！！？」`
- TW: `「唔！！！？」`
- VN cũ: `「っ!!!?」`
- Sửa: `「Ư!!!?」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1406 — 双鉄 — raw-tsu
- JP: `「っ！！？　――あ、あぁ」`
- TW: `「唔！！？　——啊，嗯」`
- VN cũ: `「っ!!? ――A, ừm」`
- Sửa: `「Ư!!? ――A, ừm」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1407 — 双鉄 — raw-tsu
- JP: `「っ！！？」`
- TW: `「唔！！？」`
- VN cũ: `「っ!!?」`
- Sửa: `「Ư!!?」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1408 — 日々姫 — raw-tsu
- JP: `「っ！！？　ぁっ――んっ――（ごくっ）――\nぁっ――！　――すーー、はーー、すーー、はーーー」`
- TW: `「唔！！？啊——嗯——（咽口水）——啊——！嘶————哈————嘶————哈————」`
- VN cũ: `「っ!!? A――ưm――（Ực）――\nA――! ――Hít, thở, hít, thở――」`
- Sửa: `「Ư!!? A――ưm――（Ực）――\nA――! ――Hít, thở, hít, thở――」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư. Fix dựng lại từ VN CSV3 (giữ \n).

### Key 1409 — 双鉄 — raw-tsu
- JP: `「っ！？」`
- TW: `「唔！？」`
- VN cũ: `「っ!?」`
- Sửa: `「Ư!?」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư. Lưu ý: JP trong CSV3 bị mojibake ('���！？'), TOML # JP: xác nhận JP thật là 「っ！？」.

### Key 1410 — ふかみ — raw-tsu
- JP: `「～～～～～～～っ！！！！」`
- TW: `「唔～～～～～～～！！！！」`
- VN cũ: `「~~~~~~~っ!!!!」`
- Sửa: `「~~~~~~~Ư!!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1411 — 日々姫 — raw-tsu
- JP: `「～～～～～～～～っ！！！」`
- TW: `「唔～～～～～～～～！！！」`
- VN cũ: `「~~~~~~~~っ!!!」`
- Sửa: `「~~~~~~~~Ư!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1412 — 双鉄 — raw-tsu
- JP: `「～～～～～～～～っ！！！！！」`
- TW: `「唔～～～～～～～～！！！！！」`
- VN cũ: `「~~~~~~~~っ!!!!!」`
- Sửa: `「~~~~~~~~Ư!!!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1413 — 日々姫 — raw-tsu
- JP: `「～～～～～～～～～～～っ！！！」`
- TW: `「唔～～～～～～～～～～～！！！」`
- VN cũ: `「~~~~~~~~~~~っ!!!」`
- Sửa: `「~~~~~~~~~~~Ư!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1423 — 双鉄 — raw-tsu
- JP: `「ぁ――っ――ぁ――はぁっ――んっ」`
- TW: `「啊——啊——蛤啊——嗯」`
- VN cũ: `「A――っ――a――hà――ưm」`
- Sửa: `「A――Ư――a――hà――ưm」`
- Lý do: Sweep raw-tsu: っ đứng một mình giữa hai dấu ―― → Ư.

### Key 1431 — 日々姫 — raw-tsu
- JP: `「あっ――。\n――――っ――」`
- TW: `「啊——嗚——」`
- VN cũ: `「A――.\n――――っ――」`
- Sửa: `「A――.\n――――Ư――」`
- Lý do: Sweep raw-tsu: っ ở đầu dòng 2 (sau \n) → Ư. Fix dựng lại từ VN CSV3 (giữ \n).

### Key 1447 — 日々姫 — vowel-count
- JP: `「ああっ！！！！」`
- TW: `「啊啊！！！！」`
- VN cũ: `「A!!!!」`
- Sửa: `「Aa!!!!」`
- Lý do: Đếm nguyên âm bằng máy: JP ああっ có 2 mora a, VN cũ chỉ có 1 chữ "A" → thiếu 1. Sửa "A"→"Aa".

### Key 1449 — 日々姫 — raw-tsu
- JP: `「！――っ！――っ！！？」`
- TW: `「啊！嗯——！嗯——！！！？」`
- VN cũ: `「!――っ!――っ!!?」`
- Sửa: `「!――Ư!――Ư!!?」`
- Lý do: Sweep raw-tsu: 2 lần っ thô → Ư.

### Key 1451 — 日々姫 — raw-tsu
- JP: `「っ！！！」`
- TW: `「啊！！！」`
- VN cũ: `「っ!!!」`
- Sửa: `「Ư!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1452 — 双鉄 — raw-tsu
- JP: `「っ！！！！」`
- TW: `「啊！！！！」`
- VN cũ: `「っ!!!!」`
- Sửa: `「Ư!!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1453 — 双鉄 — raw-tsu
- JP: `「っ！！！！！」`
- TW: `「啊！！！！！」`
- VN cũ: `「っ!!!!!」`
- Sửa: `「Ư!!!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1454 — 日々姫 — raw-tsu
- JP: `「っ！！！！！！！！！！！」`
- TW: `「啊！！！！！！！！！！！」`
- VN cũ: `「っ!!!!!!!!!!!」`
- Sửa: `「Ư!!!!!!!!!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1455 — 双鉄 — raw-tsu
- JP: `「っ！！？」`
- TW: `「啊！！？」`
- VN cũ: `「っ!!?」`
- Sửa: `「Ư!!?」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1462 — ふかみ — mistranslation
- JP: `「うっわ……いやらしい――\nなんですか、これ――いつも以上じゃないですか」`
- TW: `「嗚哇……好下流——這不是——比平時還要下流嗎」`
- VN cũ: `「Uwa…… dâm đãng quá――\nGì thế này――còn to hơn mọi khi nữa.」`
- Sửa: `「Uwa…… dâm đãng quá――\nGì thế này――còn dâm đãng hơn mọi khi nữa.」`
- Lý do: Dịch sai: JP いつも以上 ("hơn mọi khi") chỉ mức độ いやらしい (dâm đãng) ở dòng trên; TW nói rõ 比平時還要下流 (dâm hơn bình thường). VN cũ "còn to hơn mọi khi" bịa ra "to" (lớn) không có căn cứ → sửa "to"→"dâm đãng".

### Key 1463 — 双鉄 — vowel-count
- JP: `「ぅぁぁあああああああああっ！！！？」`
- TW: `「嗚啊啊啊啊啊啊啊啊啊啊啊！！！？」`
- VN cũ: `「Ư a a a a a a a a a a!!!?」`
- Sửa: `「Ư a a a a a a a a a a a!!!?」`
- Lý do: Đếm nguyên âm bằng máy: JP có 11 mora a (ぁ×2 + あ×9), VN cũ có 10 chữ a → thiếu 1. Thêm 1 a.

### Key 1465 — 双鉄 — raw-tsu
- JP: `「っ！！！！！！！！！」`
- TW: `「嗚！！！！！！！！！」`
- VN cũ: `「っ!!!!!!!!!」`
- Sửa: `「Ư!!!!!!!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1475 — ふかみ — vowel-count
- JP: `「ん――ちゅっ――ちゅむっ――ちゅう――れるっ――\nれりゅううっ――じゅるっ――じゅ――ずりゅ――るっ」`
- TW: `「嗯——啾——啾唔——啾嗚——滋溜——滋溜——啾嚕——啾——滋溜——滋溜」`
- VN cũ: `「Ưm――chụt――chùn chụt――chụt――rê ru――\nrê ryu――chùn chụt――chu――zuryu――ru」`
- Sửa: `「Ưm――chụt――chùn chụt――chụt――rê ru――\nrê ryuu――chùn chụt――chu――zuryu――ru」`
- Lý do: Đếm nguyên âm bằng máy: JP れりゅううっ có う×2 sau りゅ ("ryuu"), VN cũ "rê ryu" chỉ có 1 u → thiếu 1. Sửa "ryu"→"ryuu".

### Key 1481 — 日々姫 — raw-tsu
- JP: `「うん。えと――お願い、しま――っ！！！！！！」`
- TW: `「嗯。呃——拜託——！！！！！！」`
- VN cũ: `「Vâng. Ừm――xin anh, hãy――っ!!!!!!」`
- Sửa: `「Vâng. Ừm――xin anh, hãy――Ư!!!!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1518 — 日々姫 — raw-tsu
- JP: `「痛っ――ぐっ～～～～～～～っ！！！！！！」`
- TW: `「好痛——咕～～～～～～～！！！！！！」`
- VN cũ: `「Đau――gu~~~~~~~っ!!!!!!」`
- Sửa: `「Đau――gu~~~~~~~Ư!!!!!!」`
- Lý do: Sweep raw-tsu: っ cuối sau ～～～ → Ư. (痛っ―― → "Đau――" giữ nguyên, っ được dấu ―― diễn.)

### Key 1553 — 双鉄 — kinship-fabrication
- JP: `「凪の代わりなどではなく。日々姫を――お前を――\n僕の大事な義妹を――僕は、今宵一晩だけ――」`
- TW: `「我不是將你視為凪的替代品。而是把你——把我重要的妹妹——在今天晚上——」`
- VN cũ: `「Không phải là người thay thế Nagi. Mà là Hibiki――là em――\ncô em gái nuôi quan trọng của anh――Anh, chỉ đêm nay thôi――」`
- Sửa: `「Không phải là người thay thế Nagi. Mà là Hibiki――là em――\ncô em gái quan trọng của anh――Anh, chỉ đêm nay thôi――」`
- Lý do: Bịa quan hệ huyết thống: 義妹 → "em gái nuôi". Brief liệt kê đích danh 義妹→"em gái nuôi" là mẫu bịa của Gemini (義 ≠ 養); TW chỉ nói 妹妹 (em gái). Trong chính file này key 1262 đã dịch 義妹 là "em gái" đúng. Sửa bỏ "nuôi".

### Key 1700 — 双鉄 — lost-gasp
- JP: `「ふかみ――もう少しっ――もう少し、だけっ――\nっ！！　僕もっ――僕もっ――もうすぐ、だからっ――」`
- TW: `「深美——還差一點——還差一點——！！我也要——我也要——很快就要來了——」`
- VN cũ: `「Fukami――một chút nữa thôi――chỉ một chút, nữa thôi――\n!! Anh cũng――anh cũng――sắp ra, rồi――」`
- Sửa: `「Fukami――một chút nữa thôi――chỉ một chút, nữa thôi――\nƯ!! Anh cũng――anh cũng――sắp ra, rồi――」`
- Lý do: Sweep BỎ SÓT: っ ở ĐẦU dòng 2 (sau \n) → VN chỉ còn "!!", gasp mất hoàn toàn. Theo quy tắc gasp (line-initial → thêm Ư) → "Ư!!".

### Key 1721 — 日々姫 — mistranslation
- JP: `「精液。精子――これが、にぃにの――（くんっ、くん）\nあつくて――くさい――ゆめに、まで、見たっ――」`
- TW: `「精液。精子——這就是、阿哥的——（嗅、嗅）好熱——好臭——夢想過，無數次的——」`
- VN cũ: `「Tinh dịch. Tinh trùng――đây là, của anh hai――（Khịt, khịt）\nNóng quá――hôi quá――đến cả trong mơ, em cũng muốn thấy――」`
- Sửa: `「Tinh dịch. Tinh trùng――đây là, của anh hai――（Khịt, khịt）\nNóng quá――hôi quá――đến cả trong mơ, em cũng đã thấy――」`
- Lý do: Dịch sai thì/thể: JP 見た (đã thấy, quá khứ), TW 夢想過 (đã mơ thấy). VN cũ "muốn thấy" (muốn, chưa xảy ra) thêm "muốn" không có trong JP/TW → sửa "muốn thấy"→"đã thấy".

### Key 1777 — 日々姫 — lost-gasp
- JP: `「にぃにの、亀頭っ――おちんちんの、先っ――っ！\nわたしのっ――子宮、にっ――キス、して、くれてっ」`
- TW: `「阿哥的、龜頭——小雞雞的、前面——！在親吻——我的——子宮」`
- VN cũ: `「Quy đầu của, anh hai――phần đầu của, chim――!\nĐang――hôn vào――tử cung, của em――」`
- Sửa: `「Quy đầu của, anh hai――phần đầu của, chim――Ư!\nĐang――hôn vào――tử cung, của em――」`
- Lý do: Sweep lost-gasp-trailing: っ giữa dòng (先っ――っ！) → Ư. Fix dựng lại từ VN CSV3 (giữ \n). (っ cuối dòng くれてっ KHÔNG sửa — xem mục "Giữ nguyên có lý do".)

### Key 1784 — 日々姫 — raw-tsu
- JP: `「っ！！！」`
- TW: `「！！！」`
- VN cũ: `「っ!!!」`
- Sửa: `「Ư!!!」`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư.

### Key 1785 — 双鉄 — lost-gasp
- JP: `「っ！？」`
- TW: `「！？」`
- VN cũ: `「!?」`
- Sửa: `「Ư!?」`
- Lý do: Sweep lost-gasp-whole: cả dòng chỉ có っ+!? mà VN chỉ còn dấu câu → thêm Ư.

### Key 1900 — monologue — raw-tsu
- JP: `なのに、一瞬で甘くなる。\n日々姫が笑顔の花を咲かせた、それだけで――っ！！？`
- TW: `但是，這個吻一瞬間就變得甜蜜起來。日日姬露出了燦爛的笑容，光是這樣——！！？`
- VN cũ: `Thế nhưng, trong nháy mắt nó lại trở nên ngọt ngào.\nChỉ vì Hibiki nở một nụ cười rạng rỡ――っ!!?`
- Sửa: `Thế nhưng, trong nháy mắt nó lại trở nên ngọt ngào.\nChỉ vì Hibiki nở một nụ cười rạng rỡ――Ư!!?`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư. Fix dựng lại từ VN CSV3 (giữ \n).

### Key 1920 — monologue — mistranslation
- JP: `射精をすれば、抜きさえすれば冷静になれる。\n卑怯な逃げでしかないのであろう発想に、けれども僕は`
- TW: `只要射精了，就能冷靜下來。雖然這種想法是卑鄙的逃避，但我還是——`
- VN cũ: `Chỉ cần xuất tinh, chỉ cần xả ra là tôi sẽ bình tĩnh lại được.\nMột suy nghĩ chẳng khác nào sự trốn chạy hèn nhát, nhưng tôi lại...`
- Sửa: `Chỉ cần xuất tinh, chỉ cần rút ra là tôi sẽ bình tĩnh lại được.\nMột suy nghĩ chẳng khác nào sự trốn chạy hèn nhát, nhưng tôi lại...`
- Lý do: Dịch sai: 抜く = rút ra (rút dương vật ra), VN cũ "xả ra" (xả = discharge) sai động từ. JP có hai điều kiện song song (射精 / 抜く); TW bỏ 抜く nhưng JP là chuẩn. Sửa "xả ra"→"rút ra".

### Key 1968 — monologue — kinship-fabrication+lost-gasp
- JP: `はずかしい。義妹の前で。日々姫の前で。\n自分の射精が間近だと、告白させられてしまっ――っ！？`
- TW: `好羞恥。居然要在妹妹、日日姬的面前坦白自己要射精了——！？`
- VN cũ: `Thật xấu hổ. Trước mặt em gái nuôi. Trước mặt Hibiki.\nBị ép phải thú nhận rằng mình sắp xuất tinh rồ――っ!?`
- Sửa: `Thật xấu hổ. Trước mặt em gái. Trước mặt Hibiki.\nBị ép phải thú nhận rằng mình sắp xuất tinh rồ――Ư!?`
- Lý do: Hai lỗi trong một dòng: (1) 義妹 → "em gái nuôi" (bịa, như 1553; TW: 妹妹); (2) sweep raw-tsu: っ cuối → Ư. Sửa cả hai.

### Key 2002 — monologue — kinship-fabrication
- JP: `激しい恥辱が更に全身を加熱する。けれど宣言しなければ、\nどろどろに濃い精液を、日々姫に、義妹に、かけてしまう。`
- TW: `強烈的恥辱讓全身越來越燥熱。但若是我不事先聲張的話，黏稠的精液會飛灑在日日姬——在妹妹的身上。`
- VN cũ: `Sự sỉ nhục mãnh liệt càng làm toàn thân tôi nóng rực. Nhưng nếu không báo trước,\ntôi sẽ bắn tinh dịch đặc sệt lên người Hibiki, lên người em gái nuôi của mình mất.`
- Sửa: `Sự sỉ nhục mãnh liệt càng làm toàn thân tôi nóng rực. Nhưng nếu không báo trước,\ntôi sẽ bắn tinh dịch đặc sệt lên người Hibiki, lên người em gái của mình mất.`
- Lý do: Bịa quan hệ huyết thống: 義妹 → "em gái nuôi" (như 1553; TW: 妹妹). Sửa bỏ "nuôi".

### Key 2011 — monologue — kinship-fabrication
- JP: `快感が背徳感と入り混じり背筋から脳に突き抜ける。\n日々姫が――僕の義妹が――小さかったあの日々姫が――`
- TW: `快感和背德感混雜在一起穿過大腦。日日姬——我的妹妹——那個小小的日日姬——`
- VN cũ: `Khoái cảm lẫn lộn với cảm giác tội lỗi chạy dọc sống lưng lên tận não.\nHibiki――em gái nuôi của tôi――Hibiki bé bỏng ngày nào――`
- Sửa: `Khoái cảm lẫn lộn với cảm giác tội lỗi chạy dọc sống lưng lên tận não.\nHibiki――em gái của tôi――Hibiki bé bỏng ngày nào――`
- Lý do: Bịa quan hệ huyết thống: 義妹 → "em gái nuôi" (như 1553; TW: 妹妹). Sửa bỏ "nuôi".

### Key 2033 — monologue — kinship-fabrication
- JP: `義理の家族で、同じ物を食べ、同じ空間で生活し、\nおんなじものを見て笑い、おんなじような失敗をして――`
- TW: `我們是無血緣關係的家人，吃同樣的食物，在同樣的空間中生活，看著同樣的事物歡笑，犯同樣的失敗——`
- VN cũ: `Là gia đình nuôi, cùng ăn một món, sống trong cùng một không gian,\ncùng nhìn một thứ rồi cười, cùng mắc những sai lầm giống nhau――`
- Sửa: `Là gia đình không cùng huyết thống, cùng ăn một món, sống trong cùng một không gian,\ncùng nhìn một thứ rồi cười, cùng mắc những sai lầm giống nhau――`
- Lý do: Bịa quan hệ huyết thống: 義理の家族 → "gia đình nuôi". 義理 = quan hệ bên vợ/chồng (không cùng huyết thống), không phải 養 (nuôi); TW nói rõ 無血緣關係的家人 (gia đình không cùng huyết thống). Sửa theo TW.

### Key 2038 — monologue — kinship-fabrication
- JP: `名を呼ぶ。大事な義妹の名を。\n世界にふたりしかいない。僕の。大切な。いもうとの名を。`
- TW: `我呼叫著我重要的妹妹的名字。我在這個世上僅有兩人的，我重要的妹妹的名字。`
- VN cũ: `Tôi gọi tên. Tên cô em gái nuôi quan trọng.\nChỉ có hai người trên thế giới này. Tên cô em gái. Quan trọng. Của tôi.`
- Sửa: `Tôi gọi tên. Tên cô em gái quan trọng.\nChỉ có hai người trên thế giới này. Tên cô em gái. Quan trọng. Của tôi.`
- Lý do: Bịa quan hệ huyết thống: 義妹 → "em gái nuôi" (như 1553; TW: 妹妹). Sửa bỏ "nuôi".

### Key 2069 — monologue — kinship-fabrication
- JP: `ようやく日々姫に向き直れる。発情している女にではなく、\n僕の大事な――大事な義妹――右田日々姫に。その人に。`
- TW: `我總算重新看向了日日姬。不是將她視為一個發情的女性，而是視為我重要的——重要的妹妹——右田日日姬。`
- VN cũ: `Cuối cùng tôi cũng có thể đối diện với Hibiki. Không phải với một người phụ nữ đang phát tình,\nmà là với cô em gái nuôi quan trọng của tôi――Migita Hibiki. Với chính con người em ấy.`
- Sửa: `Cuối cùng tôi cũng có thể đối diện với Hibiki. Không phải với một người phụ nữ đang phát tình,\nmà là với cô em gái quan trọng của tôi――Migita Hibiki. Với chính con người em ấy.`
- Lý do: Bịa quan hệ huyết thống: 義妹 → "em gái nuôi" (như 1553; TW: 妹妹). Sửa bỏ "nuôi".

### Key 2083 — monologue — kinship-fabrication
- JP: `だから優しく、大丈夫だよと思いをこめて、呼び直す。\nどこまでだって可愛くて愛おしい、僕の大事な義妹の名を。`
- TW: `所以我溫柔地，用不讓她產生任何不安的聲音重新叫了一次我那可愛又寶貴的妹妹的名字。`
- VN cũ: `Vì thế tôi gọi lại tên em ấy thật dịu dàng, với ý muốn truyền đạt rằng không sao đâu.\nTên của cô em gái nuôi quan trọng, vô cùng đáng yêu và đáng mến của tôi.`
- Sửa: `Vì thế tôi gọi lại tên em ấy thật dịu dàng, với ý muốn truyền đạt rằng không sao đâu.\nTên của cô em gái quan trọng, vô cùng đáng yêu và đáng mến của tôi.`
- Lý do: Bịa quan hệ huyết thống: 義妹 → "em gái nuôi" (như 1553; TW: 妹妹). Sửa bỏ "nuôi".

### Key 2226 — monologue — raw-tsu
- JP: `ふかみが[にじ]躙る。僕の股間を、その足で。\n日々姫が見ている眼の前――っ！！？`
- TW: `深美用腳蹂躪著我的股間。而且就在日日姬的眼前——！！？`
- VN cũ: `Fukami chà đạp. Dùng chân chà đạp lên hạ bộ của tôi.\nNgay trước mắt Hibiki――っ!!?`
- Sửa: `Fukami chà đạp. Dùng chân chà đạp lên hạ bộ của tôi.\nNgay trước mắt Hibiki――Ư!!?`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư. Fix dựng lại từ VN CSV3 (giữ \n). ([にじ] là ruby JP, VN bỏ đúng.)

### Key 2230 — monologue — raw-tsu
- JP: `ふかみの瞳が、声が堅い。思いつめてる気さえする。\nならば今は、理由を問うよりまずは従いっ――っ！！？`
- TW: `深美的眼神和聲音很堅定。甚至令人感覺到了一股狠勁。那現在比起詢問理由，最好還是先聽話——！！？`
- VN cũ: `Ánh mắt và giọng nói của Fukami rất kiên định. Thậm chí có cảm giác như em ấy đang rất quyết tâm.\nVậy thì bây giờ, thay vì hỏi lý do, tốt nhất là cứ làm the――っ!!?`
- Sửa: `Ánh mắt và giọng nói của Fukami rất kiên định. Thậm chí có cảm giác như em ấy đang rất quyết tâm.\nVậy thì bây giờ, thay vì hỏi lý do, tốt nhất là cứ làm the――Ư!!?`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư. Fix dựng lại từ VN CSV3 (giữ \n).

### Key 2272 — monologue — kinship-fabrication
- JP: `精液を、日々姫に。大切な義妹にかけてしまっている。\n妻たるふかみの、その足指に導かれ――`
- TW: `精液在我的妻子，深美的腳趾的引導下，飛灑在日日姬——我重要的妹妹身上。`
- VN cũ: `Tinh dịch, bắn lên người Hibiki. Bắn lên người em gái nuôi quan trọng của tôi.\nDưới sự dẫn dắt của những ngón chân của người vợ Fukami――`
- Sửa: `Tinh dịch, bắn lên người Hibiki. Bắn lên người em gái quan trọng của tôi.\nDưới sự dẫn dắt của những ngón chân của người vợ Fukami――`
- Lý do: Bịa quan hệ huyết thống: 義妹 → "em gái nuôi" (như 1553; TW: 妹妹). Sửa bỏ "nuôi".

### Key 2316 — monologue — lost-gasp
- JP: `亀頭にぴたり吸い付いてくる子宮口を剥がしてはまた\n吸付けて。繰り返す度快感の波は大きくなって――っ！`
- TW: `龜頭好不容易與子宮口分開，但下一秒它又吸了上來。這種交互每進行一次，快感的波浪就變得更大——！`
- VN cũ: `Dứt quy đầu ra khỏi cổ tử cung đang bám chặt lấy rồi lại\nđể nó mút vào. Mỗi lần lặp lại, những làn sóng khoái cảm lại càng lớn hơn――!`
- Sửa: `Dứt quy đầu ra khỏi cổ tử cung đang bám chặt lấy rồi lại\nđể nó mút vào. Mỗi lần lặp lại, những làn sóng khoái cảm lại càng lớn hơn――Ư!`
- Lý do: Sweep lost-gasp-trailing: っ cuối sau ―― bị mất hoàn toàn → thêm Ư. Fix dựng lại từ VN CSV3 (giữ \n).

### Key 2318 — monologue — raw-tsu
- JP: `亀頭全部を先走り汁で余すところ無く無理潰していく。\n亀頭の割れ目もカリ首裏も、本当に余すところな――っ！`
- TW: `龜頭的每一處角落都強行被預射液所覆蓋。龜頭的裂縫，冠狀溝背，沒有一處遺漏——！`
- VN cũ: `Tô kín toàn bộ quy đầu bằng chất bôi trơn không chừa chỗ nào.\nTừ rãnh quy đầu đến mặt dưới, thực sự không chừa một chỗ nà――っ!`
- Sửa: `Tô kín toàn bộ quy đầu bằng chất bôi trơn không chừa chỗ nào.\nTừ rãnh quy đầu đến mặt dưới, thực sự không chừa một chỗ nà――Ư!`
- Lý do: Sweep raw-tsu: っ thô trong VN → Ư. Fix dựng lại từ VN CSV3 (giữ \n).

## Kiểm chứng cơ học

- JSON 68 mục, key dạng chuỗi, đúng shape list-of-dicts (key, jp, tw, old_vn, fix, kind, character).
- jp/tw/old_vn khớp CSV3 tuyệt đối 68/68.
- Khối TOML bên dưới parse được bằng tomllib: 68 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\\n` trong khối parse về `\n` đúng).
- Diff-sanity: mọi fix chỉ khác VN cũ ở đúng chỗ sửa (kiểm bằng difflib từng dòng; ngoại trừ 962 đổi cả mệnh đề sau vì đổi câu trần thuật→câu hỏi, và 2033 thay cụm "gia đình nuôi"→"gia đình không cùng huyết thống" — cả hai đều là thay đổi có chủ đích đã nêu).
- Đếm nguyên âm rên kiểm độc lập từ JP bằng máy: 1357 (18 a), 1358 (ぅ×13), 1359 (9 a), 1447 (2 a), 1463 (11 a), 1475 (りゅう = 2 u), 1328 (ぅ×16, VN khớp — không sửa).

## Lượt soát 2 (đọc lại toàn bộ fix đối chiếu JP)

- **Tổng: 68 / tái kiểm chứng: 68 / bỏ: 0 / sửa: 0.**
- Không có fix nào bị loại hay sửa lại ở lượt soát 2.

## Giữ nguyên có lý do (đã kiểm, không sửa — không phải bỏ sót)

- **"Chị Hibiki" (Fukami→Hibiki) ĐÚNG, giữ nguyên** — kể cả 1546 (Hibiki tự xưng "chị" với Fukami), 1686 ("chị" chỉ Hibiki), 1729 (Hibiki gọi Fukami là "bé Fukami"). Bằng chứng trong chính file này, key 2175: JP 「年下のふかみと比してなお" ("so với Fukami nhỏ tuổi hơn"), TW "年長的她" ("cô ấy, người lớn tuổi hơn" — chỉ Hibiki). Hibiki lớn tuổi hơn Fukami nên "chị" là đúng.
- **"Nagi-chan" ×3 (1445, 1581, 1658) giữ nguyên, không sửa.** Trong file này "bé Nagi" dùng 9 lần, "Nagi-chan" 3 lần — không thống nhất nội bộ, NHƯNG "Nagi-chan" là biến thể đã được chấp nhận toàn dự án: 109 lần trong 11 file, và các file đã gộp vẫn giữ nguyên (凪ふかみ02_凪の大会初挑戦！ 57 lần, ハチロク08/09, 日々姫10/11/12, 凪ふかみ03/08, Grand 08). Không có thuật ngữ đã quyết nào cho 凪ちゃん trong brief; nếu Hieu muốn thống nhất thì đó là việc của đợt unification (cần quyết chọn 1 dạng), không phải lỗi audit. Ghi chú lại đây để parent quyết.
- **1777 — っ cuối dòng くれてっ giữ nguyên.** VN kết bằng "――" đã diễn sự ngắt lời. っ gắn với động từ nội dung (くれる) ở cuối tuyệt đối thuộc ngoại lệ "content word" trong quy tắc gasp đã khóa (tiền lệ ブロワーっ). Sweep cũng không sửa chỗ này.
- **932 (あっ → "A"), 1271 (だっ → "mà."), 1351 (わわっ → "wawa"), 1709 (ふかみっ → "Fukami"), 1530/1466 (っ cuối dòng có xuống dòng theo sau): giữ nguyên.** っ gắn với thán từ/từ nội dung/tên riêng, từ vẫn còn nguyên và dấu câu/xuống dòng đã diễn sự ngắt — không phải gasp bị mất hoàn toàn theo quy tắc đã khóa.
- **1493 ("Em cũng――sắp, rồi"), 1569 ("Nên mới làm"), 1674 ("Sẽ hạnh phúc mà!"): giữ nguyên.** Đây là vị ngữ hiển nhiên theo ngữ cảnh cho câu JP bỏ lửng (1493: わたしも…ですっ = "em cũng [sắp ra]"; 1569: だから。だ; 1674: なれると trả lời 幸せになれるのか ở 1739). Không phải bịa nội dung mới — chỉ bổ sung vị ngữ mà ngữ pháp tiếng Việt bắt buộc. Ghi lại để parent biết đã cân nhắc.
- **Các dòng SFX ( ) độc thoại (2402–2480, vd. ずりゅううう→"Trơn tuột", ぎゅううう→"Phập!"): giữ nguyên.** Đây là hiệu ứng âm thanh hành động, VN đã dịch bằng từ SFX tiếng Việt cố định ("Phụt", "Trơn tuột", "Tuốt"...); độ dài nguyên âm chỉ được diễn lỏng qua dấu câu/phụ âm lặp — theo quy tắc "ngẫu hứng" của Hieu cho SFX và công thức đếm nguyên âm chỉ áp dụng cho tiếng rên có giọng (đã kiểm chặt ở 1357/1358/1359/1447/1463/1475).
- **912 "Nagi Fukami Route Another": giữ nguyên.** Nhãn tên route, dịch sát TW (凪&深美路線Ａｎｏｔｈｅｒ); không có quy tắc đặt tên route nào khác trong brief.
- **CSV3 bị mojibake JP ở 2 key (1409: '���！？', 1443: '���っ'):** TOML # JP: xác nhận JP thật là 1409 = 「っ！？", 1443 = 「あっ". VN không bị ảnh hưởng. Ghi chú để parent biết CSV3 có lỗi font ở 2 dòng này (không sửa CSV3 trong đợt audit).

## Mục cho đợt unification (đã quyết, KHÔNG sửa trong audit này — ghi lại để đợt sau làm)

- **Key 1689: 御一夜 → "Ohimitera" → "Ohitoyo".** JP: 団体での御一夜視察. Theo đúng lệ các file đã gộp (67 dòng Ohimitera cũ đang chờ unification), không sửa trong audit.
- **"Nagi-chan" ×3 (1445, 1581, 1658):** ứng viên thống nhất nếu Hieu quyết chọn 1 dạng cho 凪ちゃん (xem mục trên — chưa quyết, chỉ ghi chú).

## Khối TOML (đã kiểm parse, 68 khóa, 0 sai lệch)

```toml
[script]
933 = "「Ư――Ư――~~~Ư! ――A――hà, hà」"
962 = "「……Vào âm đạo, vào tử cung của Hibiki. Anh có thể rót tinh trùng của mình vào được không?」"
1261 = "「Không――vẫn chưa――đâu. Vẫn chưa――đâu, anh, hai.」"
1305 = "「Bây giờ, quy đầu của anh, đang chạm vào nơi sâu nhất trong âm đạo của Fukami――\\nchạm vào, cổ tử cung――Ư!!!?」"
1327 = "「HyauƯ」"
1332 = "「Ư!!!!!」"
1333 = "「Hyan!!!?」"
1338 = "「Ư!」"
1339 = "「Ư!! ~~~Ư――. Bắt đầu nhé, Hibiki.」"
1341 = "「Ư!!!!!」"
1342 = "「Ư!!!!?」"
1343 = "「~~~Ư!!!」"
1344 = "「~~~~Ư!!」"
1355 = "「Fua――a――Ư――a――a!!」"
1357 = "「Fuaaaaaaaaaaaaaaaaaan!」"
1358 = "「Fuafyuuuuuuuuuuuuuuưm!!」"
1359 = "「Fuyaaaaaaaaa!」"
1384 = "「HauƯ」"
1390 = "「Ư!?」"
1400 = "「Ư!!」"
1401 = "「Ư!!!」"
1402 = "「Ư!!!!」"
1403 = "「Ư!!!!!」"
1404 = "「Ư!!!!!!」"
1405 = "「Ư!!!?」"
1406 = "「Ư!!? ――A, ừm」"
1407 = "「Ư!!?」"
1408 = "「Ư!!? A――ưm――（Ực）――\\nA――! ――Hít, thở, hít, thở――」"
1409 = "「Ư!?」"
1410 = "「~~~~~~~Ư!!!!」"
1411 = "「~~~~~~~~Ư!!!」"
1412 = "「~~~~~~~~Ư!!!!!」"
1413 = "「~~~~~~~~~~~Ư!!!」"
1423 = "「A――Ư――a――hà――ưm」"
1431 = "「A――.\\n――――Ư――」"
1447 = "「Aa!!!!」"
1449 = "「!――Ư!――Ư!!?」"
1451 = "「Ư!!!」"
1452 = "「Ư!!!!」"
1453 = "「Ư!!!!!」"
1454 = "「Ư!!!!!!!!!!!」"
1455 = "「Ư!!?」"
1462 = "「Uwa…… dâm đãng quá――\\nGì thế này――còn dâm đãng hơn mọi khi nữa.」"
1463 = "「Ư a a a a a a a a a a a!!!?」"
1465 = "「Ư!!!!!!!!!」"
1475 = "「Ưm――chụt――chùn chụt――chụt――rê ru――\\nrê ryuu――chùn chụt――chu――zuryu――ru」"
1481 = "「Vâng. Ừm――xin anh, hãy――Ư!!!!!!」"
1518 = "「Đau――gu~~~~~~~Ư!!!!!!」"
1553 = "「Không phải là người thay thế Nagi. Mà là Hibiki――là em――\\ncô em gái quan trọng của anh――Anh, chỉ đêm nay thôi――」"
1700 = "「Fukami――một chút nữa thôi――chỉ một chút, nữa thôi――\\nƯ!! Anh cũng――anh cũng――sắp ra, rồi――」"
1721 = "「Tinh dịch. Tinh trùng――đây là, của anh hai――（Khịt, khịt）\\nNóng quá――hôi quá――đến cả trong mơ, em cũng đã thấy――」"
1777 = "「Quy đầu của, anh hai――phần đầu của, chim――Ư!\\nĐang――hôn vào――tử cung, của em――」"
1784 = "「Ư!!!」"
1785 = "「Ư!?」"
1900 = "Thế nhưng, trong nháy mắt nó lại trở nên ngọt ngào.\\nChỉ vì Hibiki nở một nụ cười rạng rỡ――Ư!!?"
1920 = "Chỉ cần xuất tinh, chỉ cần rút ra là tôi sẽ bình tĩnh lại được.\\nMột suy nghĩ chẳng khác nào sự trốn chạy hèn nhát, nhưng tôi lại..."
1968 = "Thật xấu hổ. Trước mặt em gái. Trước mặt Hibiki.\\nBị ép phải thú nhận rằng mình sắp xuất tinh rồ――Ư!?"
2002 = "Sự sỉ nhục mãnh liệt càng làm toàn thân tôi nóng rực. Nhưng nếu không báo trước,\\ntôi sẽ bắn tinh dịch đặc sệt lên người Hibiki, lên người em gái của mình mất."
2011 = "Khoái cảm lẫn lộn với cảm giác tội lỗi chạy dọc sống lưng lên tận não.\\nHibiki――em gái của tôi――Hibiki bé bỏng ngày nào――"
2033 = "Là gia đình không cùng huyết thống, cùng ăn một món, sống trong cùng một không gian,\\ncùng nhìn một thứ rồi cười, cùng mắc những sai lầm giống nhau――"
2038 = "Tôi gọi tên. Tên cô em gái quan trọng.\\nChỉ có hai người trên thế giới này. Tên cô em gái. Quan trọng. Của tôi."
2069 = "Cuối cùng tôi cũng có thể đối diện với Hibiki. Không phải với một người phụ nữ đang phát tình,\\nmà là với cô em gái quan trọng của tôi――Migita Hibiki. Với chính con người em ấy."
2083 = "Vì thế tôi gọi lại tên em ấy thật dịu dàng, với ý muốn truyền đạt rằng không sao đâu.\\nTên của cô em gái quan trọng, vô cùng đáng yêu và đáng mến của tôi."
2226 = "Fukami chà đạp. Dùng chân chà đạp lên hạ bộ của tôi.\\nNgay trước mắt Hibiki――Ư!!?"
2230 = "Ánh mắt và giọng nói của Fukami rất kiên định. Thậm chí có cảm giác như em ấy đang rất quyết tâm.\\nVậy thì bây giờ, thay vì hỏi lý do, tốt nhất là cứ làm the――Ư!!?"
2272 = "Tinh dịch, bắn lên người Hibiki. Bắn lên người em gái quan trọng của tôi.\\nDưới sự dẫn dắt của những ngón chân của người vợ Fukami――"
2316 = "Dứt quy đầu ra khỏi cổ tử cung đang bám chặt lấy rồi lại\\nđể nó mút vào. Mỗi lần lặp lại, những làn sóng khoái cảm lại càng lớn hơn――Ư!"
2318 = "Tô kín toàn bộ quy đầu bằng chất bôi trơn không chừa chỗ nào.\\nTừ rãnh quy đầu đến mặt dưới, thực sự không chừa một chỗ nà――Ư!"
```

## Kết bài

File lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml đã đọc hết 485/485 dòng, sai 68 dòng (14,0%) — phần lớn là gasp っ (48 dòng, gồm 45 mục sweep đã xác nhận + 3 mục sweep bỏ sót), tiếp theo là cụm bịa quan hệ huyết thống 義→"nuôi" (9 dòng, trong đó 7 lần 義妹 và 1 lần 義理の家族), 6 lỗi đếm nguyên âm ở tiếng rên, và 4 lỗi dịch sai nghĩa. Không có lệch dòng, nhiễm chéo, mồ côi, chưa dịch hay khóa trùng. Hai điểm đã xác minh chắc chắn trong file này: "Chị Hibiki" là đúng (Hibiki lớn tuổi hơn Fukami — bằng chứng key 2175), và "Nagi-chan" là biến thể được chấp nhận toàn dự án nên không sửa. Một mục Ohimitera (1689) để lại cho đợt unification theo lệ. Lượt soát 2: 68/68 tái kiểm chứng, 0 bỏ, 0 sửa. Khối TOML 68 khóa parse được, 0 sai lệch giá trị.
Kết bài