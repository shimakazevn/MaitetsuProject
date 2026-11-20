# Audit lr_ふかみh2 — lr_ふかみh2_セックスの意味.txt.toml

**Ngày kiểm toán:** 20/11/2026
**Tệp TOML:** `07_Nagi_Fukami/lr_#U3075#U304b#U307fh2_#U30bb#U30c3#U30af#U30b9#U306e#U610f#U5473.txt.toml` — md5 `896562ad2c4430d5219eef5d177b99c5`, BOM + CRLF, `[selections]` rỗng, **không có bản sao trùng** (chỉ 1 copy trong 227 tệp TOML; 11 nhóm trùng của dự án không chứa file này).
**Nguồn CSV:** "Trang tính 3" — **BẪY dual-set (đã tránh):** CSV3 có HAI bộ hàng cho file này, mỗi bộ 291 hàng, cùng dải key 757–1775. Bộ ghi thư mục `07_Nagi_Fukami` là STALE (khớp phẳng với TOML chỉ 5/291); bộ ghi thư mục `11_Other` là bộ tốt (khớp phẳng 291/291) — audit CHỈ dùng bộ `11_Other`. Hàng đợi ghi 582 dòng là tổng hai bộ, không phải số dòng thực của file.
**Kết quả: 52/291 dòng sai (17,9%), 0 dòng chưa chắc chắn, 0 dòng lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo file, 0 dòng chưa dịch, 0 key trùng.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| Đại từ Soutetsu "tôi"→"anh" với Fukami | 13 |
| SFX hơi thở fa/fu (quy tắc đã chốt 19/11) | 24 |
| Gasp っ bị mất | 14 |
| Đếm nguyên âm SFX dài (1124) | 1 |
| **Tổng** | **52** |

Key 1063 mang cả hai lỗi gasp + fa/fu (tính vào nhóm SFX trong bảng); tổng số dòng chạm vào gasp là 15. Key 1086 và 1126 mang cả gasp + đếm nguyên âm (tính vào nhóm gasp). Key 1016 mang cả fa/fu (tính vào nhóm SFX).

**Theo loại dòng:** thoại 49/162 sai (30,2%), độc thoại 3/129 sai (2,3%). **Theo nhân vật:** ふかみ (Fukami) 31/95, 双鉄 (Soutetsu) 18/67, monologue 3/129.

File này sạch về cấu trúc — 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng, 0 dòng chưa chắc chắn. Lỗi tập trung ở ba lỗi hệ thống: (1) Soutetsu tự xưng "tôi" trong toàn bộ thoại đầu file với Fukami (13/13 lần tự xưng trước key 1290 đều sai — từ key 1224 trở đi đã dùng đúng "anh"); (2) toàn bộ tiếng thở ふぁ/ふあ của Fukami đều dịch thành "Ha"/"Ah" mất âm f (24 dòng); (3) gasp っ trần/cuối dòng rên bị mất (15 dòng chạm gasp, trong đó sweep bỏ sót 12). Toàn bộ 52 lỗi đều sửa được tại chỗ, không cần dịch lại.

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục. TOML md5 `896562ad2c4430d5219eef5d177b99c5`, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng trong 227 tệp.
- **CSV vs TOML:** bộ tốt `11_Other` khớp phẳng 291/291 với TOML; bộ stale `07_Nagi_Fukami` chỉ khớp 5/291 — đã loại bỏ, không audit. JP comment trong TOML khớp CSV3 291/291 (so sánh multiset). Giá trị TOML: 128 khớp tuyệt đối + 163 khớp sau khi gộp `\n` thành khoảng trắng, 0 khác biệt thực chất — toàn bộ là hiện tượng gộp `\n` trong TOML-2. CSV3 là bản chuẩn cho fix list.
- **Sweep っ (gasp):** kiểm tra trực tiếp sweep-raw-gasp-wrong.json — file này CÓ 21 mục (xem §4). Quét bổ sung toàn bộ 291 dòng JP chứa っ: bắt thêm 12 gasp sweep bỏ sót (1068, 1069, 1072, 1085, 1086, 1099, 1107, 1125, 1126, 1127, 1588, 1598). Không còn gasp っ trần nào khác bị mất.
- **Thẻ %l:** JP 0 thẻ, VN 0 thẻ — không có thẻ nào trong file này.
- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng: 0), không có VN mồ côi (orphan: 0 — đã đối chiếu VN file qua chỉ mục VN toàn dự án, 0 lần trùng VN trong file với JP khác nhau), không có key trùng, không có hàng VN == TW, không có hàng VN == JP. 1 cặp VN trùng trong file (1068/1105 đều là 「!!」) đều là JP giống hệt nhau (「っ！！」) — lặp hợp lệ, không phải lệch dòng.
- **Đại từ:** Soutetsu tự xưng "tôi" trong 13/13 dòng thoại có đại từ ở đầu file với Fukami — sai theo quy tắc đã sửa 20/11 ("anh" với Fukami); độc thoại dùng "tôi" nhất quán (narrator, đúng); Fukami tự xưng "em" nhất quán, gọi Soutetsu "anh Soutetsu" nhất quán. Địa chỉ người nghe xác định từ nội dung dòng + mạch hội thoại (cả file chỉ có Soutetsu + Fukami, Nagi không xuất hiện); không dùng key kề nhau theo thứ tự số.
- **Thuật ngữ đã chốt:** 0 "Ohimitera", 0 "Yui", 0 "Teitetsu" sai dạng, 0 "cô" xưng hô sai. 1 dòng "Migita System" (1406) — chờ đợt thống nhất, KHÔNG tính sai (xem §6).

## 3. Các lỗi đã sửa (52 dòng)

### 987 — ふかみ — sfx

**JP:** 「いらくらっ、ん――痛くないれしゅっ――けどっ――⏎ふあっ――あっ！　かんじ――感じすぎちゃって――っ」
**TW:** 「不痛……啊嗯……不痛啦……但是……蛤啊！啊啊！感覺……太刺激了」
**VN cũ:** 「Khôn đao, ưm——không đau đâu ạ——nhưng mà——⏎ha——a! Cảm nhận——cảm nhận rõ quá——」
**Fix:** 「Khôn đao, ưm——không đau đâu ạ——nhưng mà——⏎phù——a! Cảm nhận——cảm nhận rõ quá——」
Quy tắc fa/fu: ふあっ → "phù". "Khôn đao" giữ nguyên — xem §6.

### 989 — 双鉄 — pronoun

**JP:** 「例え話にとどまらず。そろそろ僕らも、⏎子供を作っていい時期ではないかと、僕は思う」
**TW:** 「不要只停留在比喻。其實我也覺得，我們差不多該要個孩子了」
**VN cũ:** 「Không chỉ dừng lại ở những câu chuyện ví von. Tôi nghĩ,⏎cũng đã đến lúc chúng ta nên có một đứa con rồi.」
**Fix:** 「Không chỉ dừng lại ở những câu chuyện ví von. Anh nghĩ,⏎cũng đã đến lúc chúng ta nên có một đứa con rồi.」
Đại từ Soutetsu: "tôi" → "anh" với Fukami (quy tắc đã sửa 20/11; thoại, đối tượng Fukami — cả file chỉ có Soutetsu + Fukami, Nagi không xuất hiện).

### 990 — 双鉄 — pronoun

**JP:** 「かもしれんな。僕はもう、あまり飲む機会もないが」
**TW:** 「也許是吧。雖然我沒什麼機會喝酒」
**VN cũ:** 「Có lẽ vậy. Dù tôi không có nhiều cơ hội để uống nữa.」
**Fix:** 「Có lẽ vậy. Dù anh không có nhiều cơ hội để uống nữa.」
Đại từ Soutetsu: "tôi" → "anh" với Fukami (như 989).

### 1016 — ふかみ — sfx

**JP:** 「ゃぁぁぁぁぁっ！　かはっ！　はっ！　あっ！　また！⏎奥っ！　子宮っ！　ごりゅごりゅ！　えぐるの！　ふぁ」
**TW:** 「呀啊啊啊！蛤啊！又來了！小穴深處！子宮！一直被撞擊……蛤啊！」
**VN cũ:** 「Ahhh! Haa! Haa! Ah! Lại nữa!⏎Sâu quá! Tử cung! Bị cọ xát! Bị khoét sâu! Ah」
**Fix:** 「Ahhh! Haa! Haa! Ah! Lại nữa!⏎Sâu quá! Tử cung! Bị cọ xát! Bị khoét sâu! Phà」
Quy tắc fa/fu: ふぁ cuối dòng (không っ) → "phà".

### 1030 — ふかみ — sfx

**JP:** 「ひゃふっ！？　ふあっ！　そこっ！？　なにっ――⏎わたし――わたし――こんなの――はじ、めてっ――！」
**TW:** 「呀啊？！蛤啊！這裡，怎麼回事……我……我第一次有這種感覺！」
**VN cũ:** 「Hyafu!? Ha! Chỗ đó!? Gì vậy——⏎em——em——cảm giác này——lần đầu, tiên——!」
**Fix:** 「Hyaphù!? Phù! Chỗ đó!? Gì vậy——⏎em——em——cảm giác này——lần đầu, tiên——!」
Quy tắc fa/fu: ひゃふっ → "Hyaphù" (tiền lệ きゃふっ → "Kyaphù"); ふあっ → "phù".

### 1039 — ふかみ — sfx

**JP:** 「ふあっ！」
**TW:** 「哇！」
**VN cũ:** 「Ha!」
**Fix:** 「Phù!」
Quy tắc fa/fu: ふあっ → "phù".

### 1063 — ふかみ — sfx

**JP:** 「おにいひゃっ――はうっ――そうてつ、おにいさ――⏎あっ――ふっ――あっ――あっ――ん～～～っっっ！」
**TW:** 「哥哥……啊嗚……雙鐵哥哥。啊……唔……啊嗯！」
**VN cũ:** 「Anh——hau——Soutetsu, anh——⏎A——fu——a——a——ưm~~~!!!」
**Fix:** 「Anh——hau——Soutetsu, anh——⏎A——phù——a——a——ưm~~~ƯƯƯ!!!」
Sweep lost-gasp-trailing: ん～～～っっっ → ưm~~~ƯƯƯ (áp nguyên phần gasp); fa/fu: ふっ → "phù" — khác giá trị sweep ở đúng token "fu" → "phù" (sweep chỉ sửa gasp, không chạm fa/fu).

### 1068 — 双鉄 — gasp

**JP:** 「っ！！」
**TW:** 「唔！！」
**VN cũ:** 「!!」
**Fix:** 「Ư!!」
Gasp sweep bỏ sót: っ trần cả dòng → Ư (quét bổ sung toàn bộ dòng JP chứa っ).

### 1069 — 双鉄 — gasp

**JP:** 「っ！！！」
**TW:** 「唔！！！」
**VN cũ:** 「!!!」
**Fix:** 「Ư!!!」
Gasp sweep bỏ sót: っ trần cả dòng → Ư.

### 1072 — 双鉄 — gasp

**JP:** 「っ――」
**TW:** 「啊……」
**VN cũ:** 「——」
**Fix:** 「Ư――」
Gasp sweep bỏ sót: っ trần giữa dòng ("っ――") → Ư―― (tiền lệ lr_凪h2 key 1185).

### 1085 — ふかみ — gasp

**JP:** 「あぁぁぁぁぁぁぁぁああああああああああっっ！！！」
**TW:** 「啊啊啊啊啊啊啊啊！！！」
**VN cũ:** 「Aaaaaaaaaaaaaaaaaa!!!」
**Fix:** 「AaaaaaaaaaaaaaaaaaƯƯ!!!」
Gasp sweep bỏ sót: っっ cuối dòng rên → ƯƯ. Đếm âm a (JP 19 / VN 18, lệch 1) giữ nguyên — xem §6.

### 1086 — ふかみ — gasp

**JP:** 「んゆぅぅぅぅぅぅぅぅぅ～～～～っ！！！」
**TW:** 「啊啊啊啊嗯！！！」
**VN cũ:** 「Ư ah~~~~!!!」
**Fix:** 「Ư yuuuuuuuuuu~~~~Ư!!!」
Gasp sweep bỏ sót: っ cuối dòng rên → Ư; đồng thời sửa âm: んゆぅ (ゆ+9ぅ = 10 âm u) → "Ư yuuuuuuuuuu" — VN cũ "Ư ah" sai loại âm (a thay vì u) và thiếu độ dài.

### 1087 — ふかみ — sfx

**JP:** 「ふやんっ！！！」
**TW:** 「啊啊！！！」
**VN cũ:** 「Ahhh!!!」
**Fix:** 「Phuyan!!!」
Quy tắc fa/fu: ふやんっ → "Phuyan".

### 1094 — ふかみ — sfx

**JP:** 「ひゃうっ！　あっ！　あっ！　ふあっ！　ねっ！！⏎もっと――もっと――もっと――もっとぉっ！！」
**TW:** 「啊嗯！啊！蛤啊！啊啊！！繼續……用力、用力插我！！」
**VN cũ:** 「Ah! Ah! Ah! Ah! Nữa đi!!⏎Nữa đi——nữa đi——nữa đi——nữa đi!!」
**Fix:** 「Ah! Ah! Ah! Phù! Nữa đi!!⏎Nữa đi——nữa đi——nữa đi——nữa đi!!」
Quy tắc fa/fu: ふあっ → "phù" (token thứ 4 trong dòng; ひゃうっ đầu dòng → "Ah" giữ nguyên — xem §6).

### 1099 — ふかみ — gasp

**JP:** 「～～～～～～～～～～～～～～～～～～っ！！！！！」
**TW:** 「啊嗯～～～～～～～～～～～～～～～～～～！！！！！」
**VN cũ:** 「~~~~~~~~~~~~!!!!!」
**Fix:** 「~~~~~~~~~~~~Ư!!!!!」
Gasp (sweep needs-file-audit): ～～～っ cuối dòng rên → thêm Ư. Đếm dấu ~ (JP 18 / VN 12) giữ nguyên — không có quy tắc đếm ~.

### 1101 — ふかみ — sfx

**JP:** 「ふあっ！！？」⏎「ひゃうっ！！？」
**TW:** 「啊！」⏎「啊嗯！」
**VN cũ:** 「Á!!?」⏎「Ah!!?」
**Fix:** 「Phù!!?」⏎「Ah!!?」
Quy tắc fa/fu: ふあっ → "phù" (dòng 1). Dòng 2 ひゃうっ → "Ah" giữ nguyên — xem §6.

### 1104 — ふかみ — sfx

**JP:** 「あっ！　ふあっ！　ぞくぞくって、ぞくぞくってする、⏎んっ！　おつゆ、よだれ、やらっ――たれちゃう――ん」
**TW:** 「啊！蛤啊！都起雞皮疙瘩了……啊嗯……嘴巴和下面……都要流口水了……啊嗯」
**VN cũ:** 「A! Ha! Rùng mình, rùng mình quá,⏎ưm! Nước dâm, nước dãi, các thứ——chảy ra mất——ưm.」
**Fix:** 「A! Phù! Rùng mình, rùng mình quá,⏎ưm! Nước dâm, nước dãi, các thứ——chảy ra mất——ưm.」
Quy tắc fa/fu: ふあっ → "phù".

### 1105 — 双鉄 — gasp

**JP:** 「っ！！」
**TW:** 「啊！！」
**VN cũ:** 「!!」
**Fix:** 「Ư!!」
Sweep lost-gasp-whole áp nguyên: っ！！ → Ư!!.

### 1107 — 双鉄 — gasp

**JP:** 「っ！！！！！！」
**TW:** 「啊！！！！！！」
**VN cũ:** 「!!!!!!」
**Fix:** 「Ư!!!!!!」
Gasp (sweep needs-file-audit): っ trần cả dòng → Ư.

### 1124 — ふかみ — sfx

**JP:** 「ぢゅぼおおおおおおおおおおおおおおおおっ！！！」
**TW:** 「啾嚕嚕嚕嚕嚕嚕嚕！！！」
**VN cũ:** 「Chubooooooooooooooooooo!!!」
**Fix:** 「Chuboooooooooooooooo!!!」
Đếm nguyên âm: ぢゅぼお×16 (1+15) → "Chub" + 16 âm o — VN cũ 19 âm o, thừa 3.

### 1125 — ふかみ — gasp

**JP:** 「きゅゃぁぁぁぁぁっぁぁぁぁぁぁぁぁぁぁうっっ！！」
**TW:** 「嗚啊啊啊啊啊！！」
**VN cũ:** 「Á á á á á á á á á á á á á á á á á á!!」
**Fix:** 「Á á á á á á á á á á á á á á á á á áƯƯ!!」
Gasp sweep bỏ sót: うっっ cuối dòng → ƯƯ. Đếm âm á (VN 18 / JP 16 âm a + 1 âm u) giữ nguyên — xem §6.

### 1126 — ふかみ — gasp

**JP:** 「んひゅううううううううううううううっっっっっ！！」
**TW:** 「嗚嗚嗚嗚嗚！！」
**VN cũ:** 「Ưm hyuuuuuuuuuuuuuuuuu!!」
**Fix:** 「Ưm hyuuuuuuuuuuuuuuuƯƯƯƯƯ!!」
Gasp sweep bỏ sót: っ×5 cuối dòng → Ư×5; đồng thời sửa đếm nguyên âm: ひゅ+14う = 15 âm u — VN cũ 17 âm u, thừa 2.

### 1127 — ふかみ — gasp

**JP:** 「～～～～～～～～～っ！！！」
**TW:** 「嗚嗚～～～～～～～～～！！！」
**VN cũ:** 「~~~~~~~~~!!!」
**Fix:** 「~~~~~~~~~Ư!!!」
Gasp sweep bỏ sót: ～～～っ cuối dòng rên → Ư. Đếm dấu ~ khớp (9/9).

### 1147 — 双鉄 — pronoun

**JP:** 「ああ。いま――最終の、確認中だ――」
**TW:** 「嗯，正在做最後的確認」
**VN cũ:** 「À. Bây giờ——tôi đang, kiểm tra lần cuối——」
**Fix:** 「À. Bây giờ——anh đang, kiểm tra lần cuối——」
Đại từ Soutetsu: "tôi" → "anh" với Fukami (như 989).

### 1168 — 双鉄 — pronoun

**JP:** 「わかった。丁寧に、確認させていただこう」
**TW:** 「好，那就讓我仔細確認一下吧」
**VN cũ:** 「Tôi hiểu rồi. Tôi sẽ kiểm tra thật cẩn thận.」
**Fix:** 「Anh hiểu rồi. Anh sẽ kiểm tra thật cẩn thận.」
Đại từ Soutetsu: "tôi" → "anh" với Fukami (×2 trong dòng).

### 1175 — 双鉄 — pronoun

**JP:** 「素晴らしい密閉性だな。指にぴったり貼り付いてくる。⏎それに――ん――圧も強く、て――申し分、ない」
**TW:** 「密封性很好啊，緊緊貼著我的手指。而且……壓力也很強，無可挑剔」
**VN cũ:** 「Độ kín tuyệt vời thật đấy. Bám chặt lấy ngón tay tôi.⏎Hơn nữa——ưm——áp lực cũng mạnh——không có gì, để chê cả.」
**Fix:** 「Độ kín tuyệt vời thật đấy. Bám chặt lấy ngón tay anh.⏎Hơn nữa——ưm——áp lực cũng mạnh——không có gì, để chê cả.」
Đại từ Soutetsu: "ngón tay tôi" → "ngón tay anh" với Fukami.

### 1179 — ふかみ — sfx

**JP:** 「おまんこ、いまっ――双鉄おにいさん、かたち、に――⏎双鉄おにいさんの、ため、だけの――ふ……ぁ……嬉し」
**TW:** 「小穴……變成了雙鐵哥哥的形狀……變成只屬於雙鐵哥哥的東西了……好開心」
**VN cũ:** 「Âm đạo, bây giờ——đã biến thành, hình dạng——của anh Soutetsu——⏎Chỉ dành, cho——anh Soutetsu, thôi——ah……vui quá」
**Fix:** 「Âm đạo, bây giờ——đã biến thành, hình dạng——của anh Soutetsu——⏎Chỉ dành, cho——anh Soutetsu, thôi——phà……vui quá」
Quy tắc fa/fu: ふ……ぁ…… (ふぁ ngắt bởi …… ) → "phà" (sweep needs-file-audit).

### 1191 — ふかみ — sfx

**JP:** 「なにこれ――なに、これっ――ふあっ――精子――⏎なかだし――あつい――いつもと、おんなじ、なのにぃ」
**TW:** 「怎麼回事……怎麼回事……蛤啊……精子……射在裡面……好熱……明明和平時沒有區別」
**VN cũ:** 「Gì thế này——gì, thế này——ah——tinh trùng——⏎bắn vào trong——nóng quá——rõ ràng là, giống như mọi khi, mà」
**Fix:** 「Gì thế này——gì, thế này——phù——tinh trùng——⏎bắn vào trong——nóng quá——rõ ràng là, giống như mọi khi, mà」
Quy tắc fa/fu: ふあっ → "phù".

### 1205 — 双鉄 — pronoun

**JP:** 「僕の種麹は、もう少し熟成させてほしいらしい。⏎それと――[こうじむろ,1]麹室を――」
**TW:** 「我還想讓種麴再發酵一下。用你的麴室……」
**VN cũ:** 「Có vẻ như men giống của tôi muốn được ủ thêm một chút nữa.⏎Và——căn phòng ủ men——」
**Fix:** 「Có vẻ như men giống của anh muốn được ủ thêm một chút nữa.⏎Và——căn phòng ủ men——」
Đại từ Soutetsu: "men giống của tôi" → "của anh" với Fukami.

### 1207 — 双鉄 — pronoun

**JP:** 「だから――僕の種麹を、ふかみの蒸留器――⏎ふかみのおまんこの、最奥に――」
**TW:** 「所以，把我的種麴……放到你的蒸餾器……你的小穴最深處」
**VN cũ:** 「Vì vậy——hãy để men giống của tôi, vào tận cùng thiết bị chưng cất của Fukami——⏎vào tận cùng âm đạo của Fukami——」
**Fix:** 「Vì vậy——hãy để men giống của anh, vào tận cùng thiết bị chưng cất của Fukami——⏎vào tận cùng âm đạo của Fukami——」
Đại từ Soutetsu: "men giống của tôi" → "của anh" với Fukami.

### 1214 — 双鉄 — pronoun

**JP:** 「そうか。ならばひとまとめにし――っ！？」
**TW:** 「是嗎，那就一起……啊？！」
**VN cũ:** 「Vậy sao. Nếu thế thì tôi gộp lại nhé——!?」
**Fix:** 「Vậy sao. Nếu thế thì anh gộp lại nhé——!?」
Đại từ Soutetsu: "tôi" → "anh" với Fukami. Gasp っ sau し―― giữ nguyên — xem §6.

### 1215 — 双鉄 — pronoun

**JP:** 「そうか。なら、もっともっと垂らしてほしい」
**TW:** 「是嗎，那就儘管流出來吧」
**VN cũ:** 「Vậy sao. Nếu thế thì tôi muốn em chảy ra nhiều hơn nữa.」
**Fix:** 「Vậy sao. Nếu thế thì anh muốn em chảy ra nhiều hơn nữa.」
Đại từ Soutetsu: "tôi" → "anh" với Fukami.

### 1241 — 双鉄 — pronoun

**JP:** 「僕の種が、ふかみのおまんこで蒸留され――⏎その精髄たる一滴が、子宮に達し、熟成される」
**TW:** 「用你的小穴，蒸餾我的種子，那最為精華的一滴精液抵達子宮，發酵成熟」
**VN cũ:** 「Hạt giống của tôi, được chưng cất trong âm đạo của Fukami——⏎và giọt tinh túy nhất, sẽ chạm đến tử cung, rồi được ủ chín.」
**Fix:** 「Hạt giống của anh, được chưng cất trong âm đạo của Fukami——⏎và giọt tinh túy nhất, sẽ chạm đến tử cung, rồi được ủ chín.」
Đại từ Soutetsu: "Hạt giống của tôi" → "của anh" với Fukami (sweep needs-file-audit — trong JP không có っ, lỗi duy nhất là đại từ).

### 1243 — 双鉄 — pronoun

**JP:** 「こどもを作ろうというセックスだ。⏎普段のものより、感じ、緩んでくれねば困る」
**TW:** 「畢竟我們是要造小寶寶。如果還不如平時刺激，那就不好了」
**VN cũ:** 「Đây là lần làm tình để tạo ra em bé mà.⏎Nếu em không cảm thấy sướng và nới lỏng hơn bình thường thì khó cho tôi lắm.」
**Fix:** 「Đây là lần làm tình để tạo ra em bé mà.⏎Nếu em không cảm thấy sướng và nới lỏng hơn bình thường thì khó cho anh lắm.」
Đại từ Soutetsu: "khó cho tôi" → "khó cho anh" với Fukami.

### 1250 — 双鉄 — pronoun

**JP:** 「確かに甘さを感じた気がした。⏎それとわずかな――酒粕独特のアルコール感も」
**TW:** 「確實甜甜的。而且還有一股淡淡的……酒糟特有的酒精味道」
**VN cũ:** 「Đúng là tôi có cảm thấy vị ngọt.⏎Và một chút——vị cồn đặc trưng của bã rượu nữa.」
**Fix:** 「Đúng là anh có cảm thấy vị ngọt.⏎Và một chút——vị cồn đặc trưng của bã rượu nữa.」
Đại từ Soutetsu: "tôi" → "anh" với Fukami.

### 1260 — ふかみ — sfx

**JP:** 「ふぁ……あ――双鉄、おにいさんの――おちんちんの、⏎さきっぽ――ん――いっつも、よりも――ふくれ、てて」
**TW:** 「蛤啊……啊……雙鐵哥哥的……肉棒……龜頭……變得比平時……還要大……」
**VN cũ:** 「Ha…… a——phần đầu——dương vật, của anh Soutetsu——⏎ưm——căng phồng, hơn——mọi khi.」
**Fix:** 「Phà…… a——phần đầu——dương vật, của anh Soutetsu——⏎ưm——căng phồng, hơn——mọi khi.」
Quy tắc fa/fu: ふぁ → "phà" (sweep needs-file-audit).

### 1262 — ふかみ — sfx

**JP:** 「ふあっ――あんっ――」
**TW:** 「蛤啊……啊嗯」
**VN cũ:** 「Ha——an——」
**Fix:** 「Phù——an——」
Quy tắc fa/fu: ふあっ → "phù".

### 1264 — ふかみ — sfx

**JP:** 「はぁっ――はぁ――はあっ――はあっ――（ごくっ）⏎ん……ふっ――あっ――はあっ――はあっ――はあっ」
**TW:** 「蛤啊……蛤啊……蛤啊……（咽口水）。嗯……蛤啊……蛤啊……」
**VN cũ:** 「Ha——ha——ha——ha——(Ực)⏎Ưm…… fu——a——ha——ha——ha.」
**Fix:** 「Ha——ha——ha——ha——(Ực)⏎Ưm…… phù——a——ha——ha——ha.」
Quy tắc fa/fu: ふっ → "phù". (はぁっ → "Ha" giữ nguyên theo tiền lệ lr_凪h2 — xem §6.)

### 1266 — ふかみ — sfx

**JP:** 「ふぁっ――これ……妊娠――受精……届いて、るっ――⏎んっ――感じ、するっ――なに――これ――しゅご、い」
**TW:** 「蛤啊……這就是懷孕、受精……怎麼會這樣……這樣……好棒」
**VN cũ:** 「Ah——thế này……mang thai——thụ tinh……đến, nơi rồi——⏎ưm——cảm nhận, được rồi——gì thế——này——tuyệt, quá」
**Fix:** 「Phà——thế này……mang thai——thụ tinh……đến, nơi rồi——⏎ưm——cảm nhận, được rồi——gì thế——này——tuyệt, quá」
Quy tắc fa/fu: ふぁっ → "phà".

### 1267 — ふかみ — sfx

**JP:** 「ふぁっ――あ……それ、なら――よかった――です。⏎ん……っ――ね？　なら……双鉄、おにい、さん」
**TW:** 「蛤啊……那就好。嗯……這樣的話……雙鐵哥哥」
**VN cũ:** 「Ha——a…… Nếu, vậy thì——tốt quá——rồi.⏎Ưm…… đúng không? Nếu vậy…… anh, Soutetsu.」
**Fix:** 「Phà——a…… Nếu, vậy thì——tốt quá——rồi.⏎Ưm…… đúng không? Nếu vậy…… anh, Soutetsu.」
Quy tắc fa/fu: ふぁっ → "phà".

### 1268 — ふかみ — sfx

**JP:** 「ふああああああんっ！！」
**TW:** 「蛤啊啊啊啊！！」
**VN cũ:** 「Haaaaaaaaan!!」
**Fix:** 「Phùaaaaaan!!」
Quy tắc fa/fu: ふああああああんっ (ふ+6あ) → "Phùaaaaaan" (giữ 7 nguyên âm: ù+6a+n — tiền lệ lr_凪h2 key 1278).

### 1269 — ふかみ — sfx

**JP:** 「ふあっ！　あっ！　あっ！　あっ！　わらひっ――⏎もうっ！　らめっ――もう、イキ、すぎ、てっ――」
**TW:** 「蛤啊啊！啊啊！我……我不行了……高潮太多次了……」
**VN cũ:** 「Ah! Ah! Ah! Ah! Em——⏎Không được! Không được——em, lên đỉnh, nhiều quá, rồi——」
**Fix:** 「Phù! Ah! Ah! Ah! Em——⏎Không được! Không được——em, lên đỉnh, nhiều quá, rồi——」
Quy tắc fa/fu: ふあっ → "phù".

### 1270 — ふかみ — sfx

**JP:** 「ふあっ！　あっ！　あっ！　あっ！　あっ！！⏎ひっ！　あっ！　しょこっ！　んっ――ぁ――ふうっ」
**TW:** 「蛤啊！啊啊啊啊！！呀啊！啊！啊啊啊！啊嗯！」
**VN cũ:** 「Ha! A! A! A! A!!⏎Hí! A! Chỗ đó! Ưm——a——fuu.」
**Fix:** 「Phù! A! A! A! A!!⏎Hí! A! Chỗ đó! Ưm——a——fuu.」
Quy tắc fa/fu: ふあっ → "phù". (ふうっ → "fuu" giữ nguyên — ふう không thuộc quy tắc fa/fu.)

### 1272 — ふかみ — sfx

**JP:** 「はっ！　あっ！　しょれっ！　こきざみっ！　ぁっ！⏎んっ！　んっ！　んっ！　んっ！　ふぁっ！　あっ！」
**TW:** 「蛤啊！啊啊！這麼快！啊啊啊！嗯！嗯！嗯啊啊啊！」
**VN cũ:** 「Ah! Ah! Chỗ đó! Nhanh lên! Ah!⏎Ưm! Ưm! Ưm! Ưm! Ah! Ah!」
**Fix:** 「Ah! Ah! Chỗ đó! Nhanh lên! Ah!⏎Ưm! Ưm! Ưm! Ưm! Phà! Ah!」
Quy tắc fa/fu: ふぁっ → "phà" (token thứ 5 dòng 2).

### 1273 — ふかみ — sfx

**JP:** 「ふあっ！　あっっ！　あっ！　ンッ――くっ――⏎あっ！　わたし、なかっ――えぐれ――んうううっ！」
**TW:** 「蛤啊！啊！啊！啊嗯！啊！插到我的……裡面吧！」
**VN cũ:** 「Ha! A! A! Ưm——hự——⏎A! Bên trong, em——bị khoét sâu——ưmuuu!」
**Fix:** 「Phù! A! A! Ưm——hự——⏎A! Bên trong, em——bị khoét sâu——ưmuuu!」
Quy tắc fa/fu: ふあっ → "phù".

### 1275 — ふかみ — sfx

**JP:** 「ふぁっ！　あっ！　来てるっ！　んっ！⏎ちょっと、ずつ――ふぁっ――や、ぁ――熱っ、くて」
**TW:** 「蛤啊！啊！進來了！嗯！一點點地……蛤啊……啊……好熱」
**VN cũ:** 「Ha! A! Đang vào! Ưm!⏎Từng chút, một——ha——a, a——nóng, quá.」
**Fix:** 「Phà! A! Đang vào! Ưm!⏎Từng chút, một——phà——a, a——nóng, quá.」
Quy tắc fa/fu: ふぁっ → "phà" (×2 trong dòng).

### 1276 — ふかみ — sfx

**JP:** 「ふぁっ！　それっ！　そこっ！　おくっ！　しゅき！⏎おくっ！　しきゅう！　もっとぉっ！！！」
**TW:** 「蛤啊！就是那裡，插到深處……好舒服！深處……好舒服……我還要！！！」
**VN cũ:** 「Ah! Đúng rồi! Chỗ đó! Sâu nữa! Thích quá!⏎Sâu nữa! Tử cung! Nữa đi!!!」
**Fix:** 「Phà! Đúng rồi! Chỗ đó! Sâu nữa! Thích quá!⏎Sâu nữa! Tử cung! Nữa đi!!!」
Quy tắc fa/fu: ふぁっ → "phà".

### 1277 — ふかみ — sfx

**JP:** 「ふあっ！！」
**TW:** 「蛤啊！！」
**VN cũ:** 「Ha!!」
**Fix:** 「Phù!!」
Quy tắc fa/fu: ふあっ → "phù".

### 1290 — 双鉄 — pronoun

**JP:** 「ならば僕はその最奥に、ふかみの大事な大事な卵子に。⏎僕の一番強く賢い精子を届け――受精させよう」
**TW:** 「那我就得把我最強壯最優秀的精子，射進最深處，射進你最寶貴的卵子裡，讓你受精」
**VN cũ:** 「Vậy thì tôi sẽ đưa tinh trùng mạnh nhất, thông minh nhất của tôi.⏎Vào tận cùng bên trong, vào trứng vô cùng quan trọng của Fukami——để thụ tinh.」
**Fix:** 「Vậy thì anh sẽ đưa tinh trùng mạnh nhất, thông minh nhất của anh.⏎Vào tận cùng bên trong, vào trứng vô cùng quan trọng của Fukami——để thụ tinh.」
Đại từ Soutetsu: "tôi" → "anh" với Fukami (×2 trong dòng).

### 1558 — monologue — gasp

**JP:** 熱い吐息を吹き込みながら、ふかみは舌を割入らせてくる。⏎確かに、甘い――酒の香も、極めてわずかだ――っ！！
**TW:** 深美呼出溫熱的氣息，將舌頭深入我的口中。確實很甜，還有股淡淡的酒香……唔！！
**VN cũ:** Vừa phả ra hơi thở nóng hổi, Fukami vừa luồn lưỡi vào.⏎Đúng là, ngọt thật——hương rượu cũng cực kỳ nhạt——!!
**Fix:** Vừa phả ra hơi thở nóng hổi, Fukami vừa luồn lưỡi vào.⏎Đúng là, ngọt thật——hương rượu cũng cực kỳ nhạt——Ư!!
Sweep lost-gasp-trailing áp nguyên: ――っ！！ cuối độc thoại → Ư!!.

### 1588 — monologue — gasp

**JP:** ふかみがいきなり深くまで――⏎僕の勃起の全部を一気に口いっぱいに収めてくれ――っ！
**TW:** 深美突然用力，把我的肉棒一口氣全部含進嘴裡……唔！
**VN cũ:** Đột nhiên Fukami ngậm sâu vào——⏎Thu trọn toàn bộ sự cương cứng của tôi vào miệng cùng một lúc——!
**Fix:** Đột nhiên Fukami ngậm sâu vào——⏎Thu trọn toàn bộ sự cương cứng của tôi vào miệng cùng một lúc——Ư!
Gasp (sweep "uncertain", giải quyết theo tiền lệ 1558): くれ――っ！ cuối độc thoại tả cảm giác mạnh → Ư.

### 1598 — monologue — gasp

**JP:** あまりに強い勢いに、亀頭が喉奥にあたってしまう。⏎背徳感と快感が、背骨を通じ脳までぐらぐら――っ！！！
**TW:** 激烈的口交之下，龜頭甚至感覺頂到了她的喉嚨。背德感與快感通過脊椎直達大腦，讓我感覺頭暈目眩……唔！！！
**VN cũ:** Do lực quá mạnh, quy đầu đâm thẳng vào tận cùng cổ họng.⏎Cảm giác tội lỗi và khoái cảm chạy dọc sống lưng lên não khiến tôi choáng váng——!!!
**Fix:** Do lực quá mạnh, quy đầu đâm thẳng vào tận cùng cổ họng.⏎Cảm giác tội lỗi và khoái cảm chạy dọc sống lưng lên não khiến tôi choáng váng——Ư!!!
Gasp sweep bỏ sót: ぐらぐら――っ！！！ cuối độc thoại → Ư (cùng mẫu 1558).

## 4. Đối chiếu đợt quét gasp っ

Sweep có 21 mục cho file này (lost-gasp-whole 1, lost-gasp-trailing 2, already-rendered 4, needs-file-audit 12, uncertain 2):

- **Áp nguyên đã kiểm chứng (3):** 1105 (lost-gasp-whole, っ！！ → Ư!!), 1558 (lost-gasp-trailing, ――っ！！ → Ư!!), 1063 (lost-gasp-trailing, ん～～～っっっ → ưm~~~ƯƯƯ — phần gasp áp nguyên; token ふっ sửa thêm "fu" → "phù" theo quy tắc fa/fu, xem §3).
- **Needs-file-audit (12) — đã giải quyết hết:** sửa 5 (1099, 1107, 1179, 1260 — gasp/fa-fu; 1241 — trong JP không có っ, lỗi duy nhất là đại từ Soutetsu "của tôi" → "của anh"); giữ nguyên 7 (1027 — っ nhấn mạnh cuối câu gắn với なっちゃう, tiền lệ 1474; 1120 — SFX onomatopoeia đã diễn đủ âm; 1423, 1479 — độc thoại, không có っ bị mất; 1717, 1733, 1760 — SFX trong ngoặc đã diễn đủ âm).
- **Uncertain (2):** 1078 giữ nguyên (「く――あ……ふか、み――」 không có っ cuối, VN "Kh——a…… Fuka, mi——" đã diễn đủ); 1588 sửa (くれ――っ！ cuối độc thoại → Ư, theo tiền lệ 1558).
- **Already-rendered (4) — đã kiểm chứng:** 1029 (んひゅっ → "Ưm hyu"), 1035 (うあっ → "Ư ah"), 1070 (くっ → "Hự"), 1763 (くっ――ぐっ―― → "Phập——hự——", diễn lỏng nhưng đủ âm).
- **Sweep bỏ sót (12) — bắt được khi quét bổ sung:** 1068, 1069, 1072, 1085, 1086, 1099, 1107, 1125, 1126, 1127, 1588, 1598 (1099/1107/1588 đã nằm trong needs-file-audit/uncertain của sweep; 9 dòng còn lại sweep không liệt kê).
- **っ nhấn mạnh cuối câu — KHÔNG sửa (tiền lệ 1474, 2428, 2588):** っ gắn trực tiếp với từ trong thoại: 987 (感じすぎちゃって――っ), 1022 (かえられ、ちゃうっ――っ), 1023 (すぐっ), 1027 (なっちゃうっ), 1030 (はじ、めてっ――), 1092 (知らないの――っ), 1162 (ならば――っ), 1203 (かっ), 1214 (し――っ！？), 1230 (ふかみっ――), 1257 (のか――っ！), 1285 (精子――っ！), 1445 (けれどっ――), 1463 (ふかみをっ――). Chỉ sửa っ khi nó là gasp trần cả dòng, gasp cuối dòng rên, hoặc っ tách bởi ―― trong độc thoại tả cảm giác mạnh (1558/1588/1598).

## 5. Lượt soát 2 (second pass)

- Đọc lại toàn bộ 52 giá trị fix đối chiếu JP: **52/52 tái kiểm chứng, 0 bỏ, 3 sửa** (1269, 1270, 1273 — đã viết nhầm "Phà" cho token ふあっ; sửa thành "Phù" theo đúng phân biệt ふぁ (ぁ nhỏ) → "phà" / ふあ (あ đầy) + っ → "phù").
- JSON 52 khóa chuỗi, dạng chuẩn list-of-dicts (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 52/52; diff-sanity: mọi fix chỉ khác VN cũ ở đúng chỗ sửa nhắm tới (kiểm tra bằng difflib — 0 fix viết lại lớn); 0 giá trị fix chứa ký tự xuống dòng thật.
- Khối TOML parse OK (tomllib), 52 khóa, 0 sai lệch giá trị so với JSON. Khóa TOML viết dạng `"key" = "value"`, `\n` trong khối là literal backslash-n (đúng quy ước review).

## 6. Phán đoán ghi chú / chưa chắc chắn / chờ Hieu

- **1406 "Migita System" — KHÔNG tính sai, chờ đợt thống nhất:** JP 右田一, TW 右田一. Quyết định 19/11: brewery = "Migita Ichi" ("Migita System" không tồn tại); đợt thống nhất đang chờ (15 dòng toàn dự án). Không tự sửa trong audit này.
- **987 "Khôn đao" — giữ nguyên:** "いらくらっ" là nói ngọng của "không đau" (TW: 不痛); VN "Khôn đao" là cách diễn ngọng có chủ ý (bỏ "g"/"u" của "không đau"), không phải lỗi chính tả.
- **Âm ひゃ đầu tiếng rên giữ nguyên:** 1018 (ひゃっう → "Á"), 1019 (ひゃうっ → "Ah"), 1094 dòng 1 (ひゃうっ → "Ah"), 1101 dòng 2 (ひゃうっ → "Ah"). "Ah"/"Á" là cách diễn rên tự nhiên, giữ nguyên âm đệm; không có quy tắc đã chốt nào về âm ひゃ (quy tắc fa/fu chỉ bao ふぁ/ふあ/ふぇ/ふや/ふっ). Tiền lệ trong file: 1097 ひゃうっ → "Hyau" — không thống nhất ngược vì đây là SFX ngẫu hứng theo Hieu 19/11 22:05.
- **はぁっ → "Ha" giữ nguyên:** tiền lệ lr_凪h2 (dòng 「ふぁっ！ はぁっ！ はぁ！…」 chỉ sửa ふぁっ → "Phà", giữ nguyên toàn bộ "Ha"). Không áp dụng "Hà" (tiền lệ khác file, mâu thuẫn — theo file cùng route mới nhất).
- **っ nhấn mạnh trong thoại giữ nguyên:** xem danh sách §4 — っ gắn với từ hoặc sau ―― trong thoại là nhấn mạnh/ngắt lời, không phải gasp (tiền lệ 1474, 2428, 2588).
- **Đếm âm giữ nguyên (chỉ thêm gasp):** 1085 (JP 19 âm a / VN 18, lệch 1); 1125 (VN 18 âm á / JP 16 âm a + 1 âm u — cách tách âm tiết không rõ ràng); 1099/1127 (đếm dấu ~ JP 18/VN 12 và 9/9 — không có quy tắc đếm ~).
- **Giữ nguyên, không tính sai:** 1463 "Tôi muốn Fukami" (khớp TW "我不禁想把深美……"); 1295 "blowjob" (loanword, dùng nhất quán trong cảnh H); 1014 "đang mò mẫm——bên trong, âm đạo" (hơi vụng về nhưng đúng nghĩa); 1207 "hãy để" (bổ sung tự nhiên cho câu JP dở dang, không bịa thêm nội dung); 1568 "Bởi vì!" (dịch sát mảnh câu JP "ゆえ！"); 1271 くはっ → "ah" (diễn lỏng, âm còn); 1270 ふうっ → "fuu" (ふう không thuộc quy tắc fa/fu).
- **0 dòng chưa chắc chắn.** Không có câu hỏi thuật ngữ mới nào cho Hieu trong file này.

## 7. Khối TOML (đã kiểm chứng parse)

```toml
[script]
"987" = "「Khôn đao, ưm——không đau đâu ạ——nhưng mà——\\nphù——a! Cảm nhận——cảm nhận rõ quá——」"
"989" = "「Không chỉ dừng lại ở những câu chuyện ví von. Anh nghĩ,\\ncũng đã đến lúc chúng ta nên có một đứa con rồi.」"
"990" = "「Có lẽ vậy. Dù anh không có nhiều cơ hội để uống nữa.」"
"1016" = "「Ahhh! Haa! Haa! Ah! Lại nữa!\\nSâu quá! Tử cung! Bị cọ xát! Bị khoét sâu! Phà」"
"1030" = "「Hyaphù!? Phù! Chỗ đó!? Gì vậy——\\nem——em——cảm giác này——lần đầu, tiên——!」"
"1039" = "「Phù!」"
"1063" = "「Anh——hau——Soutetsu, anh——\\nA——phù——a——a——ưm~~~ƯƯƯ!!!」"
"1068" = "「Ư!!」"
"1069" = "「Ư!!!」"
"1072" = "「Ư――」"
"1085" = "「AaaaaaaaaaaaaaaaaaƯƯ!!!」"
"1086" = "「Ư yuuuuuuuuuu~~~~Ư!!!」"
"1087" = "「Phuyan!!!」"
"1094" = "「Ah! Ah! Ah! Phù! Nữa đi!!\\nNữa đi——nữa đi——nữa đi——nữa đi!!」"
"1099" = "「~~~~~~~~~~~~Ư!!!!!」"
"1101" = "「Phù!!?」\\n「Ah!!?」"
"1104" = "「A! Phù! Rùng mình, rùng mình quá,\\nưm! Nước dâm, nước dãi, các thứ——chảy ra mất——ưm.」"
"1105" = "「Ư!!」"
"1107" = "「Ư!!!!!!」"
"1124" = "「Chuboooooooooooooooo!!!」"
"1125" = "「Á á á á á á á á á á á á á á á á á áƯƯ!!」"
"1126" = "「Ưm hyuuuuuuuuuuuuuuuƯƯƯƯƯ!!」"
"1127" = "「~~~~~~~~~Ư!!!」"
"1147" = "「À. Bây giờ——anh đang, kiểm tra lần cuối——」"
"1168" = "「Anh hiểu rồi. Anh sẽ kiểm tra thật cẩn thận.」"
"1175" = "「Độ kín tuyệt vời thật đấy. Bám chặt lấy ngón tay anh.\\nHơn nữa——ưm——áp lực cũng mạnh——không có gì, để chê cả.」"
"1179" = "「Âm đạo, bây giờ——đã biến thành, hình dạng——của anh Soutetsu——\\nChỉ dành, cho——anh Soutetsu, thôi——phà……vui quá」"
"1191" = "「Gì thế này——gì, thế này——phù——tinh trùng——\\nbắn vào trong——nóng quá——rõ ràng là, giống như mọi khi, mà」"
"1205" = "「Có vẻ như men giống của anh muốn được ủ thêm một chút nữa.\\nVà——căn phòng ủ men——」"
"1207" = "「Vì vậy——hãy để men giống của anh, vào tận cùng thiết bị chưng cất của Fukami——\\nvào tận cùng âm đạo của Fukami——」"
"1214" = "「Vậy sao. Nếu thế thì anh gộp lại nhé——!?」"
"1215" = "「Vậy sao. Nếu thế thì anh muốn em chảy ra nhiều hơn nữa.」"
"1241" = "「Hạt giống của anh, được chưng cất trong âm đạo của Fukami——\\nvà giọt tinh túy nhất, sẽ chạm đến tử cung, rồi được ủ chín.」"
"1243" = "「Đây là lần làm tình để tạo ra em bé mà.\\nNếu em không cảm thấy sướng và nới lỏng hơn bình thường thì khó cho anh lắm.」"
"1250" = "「Đúng là anh có cảm thấy vị ngọt.\\nVà một chút——vị cồn đặc trưng của bã rượu nữa.」"
"1260" = "「Phà…… a——phần đầu——dương vật, của anh Soutetsu——\\nưm——căng phồng, hơn——mọi khi.」"
"1262" = "「Phù——an——」"
"1264" = "「Ha——ha——ha——ha——(Ực)\\nƯm…… phù——a——ha——ha——ha.」"
"1266" = "「Phà——thế này……mang thai——thụ tinh……đến, nơi rồi——\\nưm——cảm nhận, được rồi——gì thế——này——tuyệt, quá」"
"1267" = "「Phà——a…… Nếu, vậy thì——tốt quá——rồi.\\nƯm…… đúng không? Nếu vậy…… anh, Soutetsu.」"
"1268" = "「Phùaaaaaan!!」"
"1269" = "「Phù! Ah! Ah! Ah! Em——\\nKhông được! Không được——em, lên đỉnh, nhiều quá, rồi——」"
"1270" = "「Phù! A! A! A! A!!\\nHí! A! Chỗ đó! Ưm——a——fuu.」"
"1272" = "「Ah! Ah! Chỗ đó! Nhanh lên! Ah!\\nƯm! Ưm! Ưm! Ưm! Phà! Ah!」"
"1273" = "「Phù! A! A! Ưm——hự——\\nA! Bên trong, em——bị khoét sâu——ưmuuu!」"
"1275" = "「Phà! A! Đang vào! Ưm!\\nTừng chút, một——phà——a, a——nóng, quá.」"
"1276" = "「Phà! Đúng rồi! Chỗ đó! Sâu nữa! Thích quá!\\nSâu nữa! Tử cung! Nữa đi!!!」"
"1277" = "「Phù!!」"
"1290" = "「Vậy thì anh sẽ đưa tinh trùng mạnh nhất, thông minh nhất của anh.\\nVào tận cùng bên trong, vào trứng vô cùng quan trọng của Fukami——để thụ tinh.」"
"1558" = "Vừa phả ra hơi thở nóng hổi, Fukami vừa luồn lưỡi vào.\\nĐúng là, ngọt thật——hương rượu cũng cực kỳ nhạt——Ư!!"
"1588" = "Đột nhiên Fukami ngậm sâu vào——\\nThu trọn toàn bộ sự cương cứng của tôi vào miệng cùng một lúc——Ư!"
"1598" = "Do lực quá mạnh, quy đầu đâm thẳng vào tận cùng cổ họng.\\nCảm giác tội lỗi và khoái cảm chạy dọc sống lưng lên não khiến tôi choáng váng——Ư!!!"
```

Kết bài
