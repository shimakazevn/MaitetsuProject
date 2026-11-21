# Audit — 日々姫08_開きかけのつぼみ.txt.toml (02_Hibiki)

- **File:** `02_Hibiki/日々姫08_開きかけのつぼみ.txt.toml` — route Hibiki, "nụ hồng đang hé nở" (bài kiểm tra chạy thử + cuộc bầu cử thị trưởng + cảnh tắm chung bàn kế hoạch giảm tải cho Hibiki).
- **Slug:** hibiki08-hirakikake-no-tsubomi
- **Phương pháp:** đọc đủ từng dòng đối chiếu JP + TW (CSV3 "Trang tính 3"), theo AUDIT-BRIEF.md + skill aligned_translation_audit. Không dùng heuristic thay cho đọc tay.
- **Số dòng đã đọc: 397 / 397. Số dòng sai: 12 (3,0%).**
- **Cơ sở tổng:** 185 file / 8.837 dòng sai (đã kiểm chứng trực tiếp từ ROUTE-AUDIT.md — khớp với con số parent giao).

## 1. Phân loại lỗi (12)

| Loại | Số dòng | Keys |
|---|---|---|
| Đại từ/xưng hô | 4 | 1738, 2164, 2192, 2193 |
| Hơi thở っ bị mất (gasp) — cả 5 từ sweep | 5 | 1731, 2052, 2399, 2400, 3073 |
| Thẻ %l VN tự thêm (gỡ thẻ, giữ chữ) | 2 | 2039, 2186 |
| Sai nghĩa / mất cấu trúc câu | 1 | 2608 |

## 2. Kiểm tra cấu trúc — 0 lỗi hệ thống

- **Lệch dòng (misaligned): 0.** Cột Việt đứng đúng chỗ ở cả 397 dòng; JP và TW đồng thuận ở mọi dòng đã kiểm tra.
- **Chuỗi xoay (rotation): 0. Nhiễm chéo (contamination): 0. Dòng mồ côi (orphan): 0.** Không có dòng Việt nào không khớp JP của chính key đó.
- **Dòng chưa dịch (untranslated): 0.** Không có ô Việt trống nào; không có dòng Việt == TW (placeholder tiếng Trung).
- **Trùng key (duplicate keys): 0** — CSV3 1 set duy nhất, 397 dòng, 0 key trùng; key TOML = key CSV3 tuyệt đối (0 key chỉ-có-TOML, 0 key chỉ-có-CSV).
- **TOML md5: `90b0da495fd9c973b837e83dfa7c4063`** (84.964 byte). Không có bản sao TOML trùng tên trong dự án (chỉ 1 file) — không thuộc 11 nhóm duplicate.
- **Chênh VN TOML vs CSV3:** 258 dòng chỉ khác ở chỗ TOML-2 làm phẳng `\n` literal thành khoảng trắng (đã kiểm chứng cơ học: 256 dòng khớp đúng sau khi thay `\n`→khoảng trắng; 2 dòng còn lại 1971, 2767 chỉ khác thêm 1 khoảng trắng thừa trước `\n` trong CSV — cùng một hiện tượng). CSV3 là bản authoritative cho fix list.
- **Thẻ `%l`:** JP = VN ở mọi dòng ngoại trừ 2 dòng VN tự thêm thẻ (2039, 2186 — đã sửa, xem §4). **0 thẻ thiếu dấu `;` đóng** trong VN. Dòng 1706: cấu trúc thẻ dị dạng là của phía JP (`\x%l逆転機;…%l;\x%lミッドギア;#;…` — thiếu `;` sau `%l` ở giữa), VN chỉ sao y cấu trúc JP — theo brief, thẻ dị dạng phía JP mà VN đã giữ nguyên thì KHÔNG phải lỗi VN, không sửa. Không có ký tự っ thô nào trong text hiển thị Việt (lần khớp duy nhất là chữ ッ trong tên thuật ngữ JP ミッドギア nằm trong thẻ %l).
- **`[characters]`:** 5 mục (2498 Reina, 2507 Hachiroku, 2521 Paulette, 2650 Soutetsu, 2852 Hibiki) — không có vấn đề tên gọi. **`[selections]`:** rỗng (0 mục). Không có `[selections]` cần dịch.

## 3. Kiểm tra sweep っ-gasp cho file này

Đã tra trực tiếp `sweep-raw-gasp-wrong.json`: file này có **5 mục** (1731, 2052, 2399, 2400, 3073) — cả 5 đều đúng, đã áp nguyên giá trị sweep (xem §4). 6 mục còn lại khi tìm "日々姫08" thuộc file khác (`日々姫08_とれいん食堂.txt.toml` — 2181, 2196, 2201, 2213, 2783, 2785), không liên quan file này.

Các dòng っ khác đã xem xét và GIỮ nguyên theo ranh giới gasp đã chốt (chỉ thêm Ư khi âm っ hoàn toàn biến mất; không render kép âm đã được render):

- 1710 「――うんっ」 → "Vâng." — dấu chấm đã thể hiện sự cụt; sweep không bắt.
- 2046 「ははっ――」 → "haha――" — tiền lệ あっ――→"A——": dấu gạch đã giữ âm cụt.
- 2047 「ぷはっ！」 → "Phụt!" — tiếng bật cười đã diễn thành âm bật, giữ theo ngẫu hứng SFX.
- 3212/3213 （ざばぁっ）/（ザバザバザバザバっ！） → "Rào rào"/"Ào ào ào ào!" — SFX hành động (tiếng nước), tiền lệ ごちゅっ→"Phập": không thêm Ư.
- 3231 （ゴ――――トっ） → "Cạch————" — dấu gạch đã giữ âm cụt.
- 3204/3240 "mình" trong độc thoại nội tâm (trong ngoặc đơn) — GIỮ: tiền lệ 凪ふかみ01 1691 phân biệt độc thoại nội tâm với thoại nói ra; "mình" chỉ sai khi là thoại (như 1738).

## 4. Danh sách sửa (12 dòng)

### [1731] — gasp (sweep lost-gasp-trailing) — 日々姫

- **JP:** 「……っ」
- **TW:** 「……」
- **VN cũ:** 「……」
- **Fix:** 「……Ư」
- **Lý do:** JP có gasp っ cuối dòng sau "……"; VN chỉ giữ dấu ba chấm, mất hẳn âm — thêm Ư theo đúng giá trị sweep.

### [1738] — đại từ: Soutetsu "mình" → "anh" — 双鉄

- **JP:** 「……バカな、酒など[ひとしずく,1]一滴もいれておらんのに」
- **TW:** 「……怎麼可能，我又沒有喝酒」
- **VN cũ:** 「……Vớ vẩn, mình chưa uống lấy một giọt rượu nào cơ mà.」
- **Fix:** 「……Vớ vẩn, anh chưa uống lấy một giọt rượu nào cơ mà.」
- **Lý do:** Đây là thoại nói ra (trong 「」), không phải độc thoại nội tâm nên ngoại lệ "mình" không áp dụng. Người nghe là Hibiki: câu này bác lại thuyết "máu nóng lên như say rượu" — chính là thuyết của Hibiki (2201 trong file này: "Trước đây, Hibiki từng nói… 『Vì là anh em đang tuổi cập kê…』"), và ngay dòng sau 1739 Soutetsu cũng xưng "Anh" với cùng một người nghe ("Anh hỏi lại lần nữa"). Soutetsu với Hibiki = "anh" theo quy tắc đã sửa. Nếu người nghe là Hachiroku thì cả 1738 lẫn 1739 đều phải là "tôi" — nhưng bằng chứng 2201 + 1739 nghiêng về Hibiki nên sửa 1738 cho khớp 1739.

### [2039] — thẻ %l VN tự thêm — ハチロク

- **JP:** 「[じょし,1]助士。ブロア[トメベン,1]止弁開放」
- **TW:** 「司爐。打開風管止回閥」
- **VN cũ:** 「Phụ lái tàu. Mở van khóa \x%lブロア;#00ffc040;thiết bị thổi gió%l;#;.」
- **Fix:** 「Phụ lái tàu. Mở van khóa thiết bị thổi gió.」
- **Lý do:** JP và TW đều không có thẻ %l ở đây; VN tự gắn thêm thẻ gloss cho ブロア. Theo tiền lệ gỡ gloss VN tự thêm (機関士 ở Hachiroku 12, 3 thẻ ở reina02, 2693 ở 00_Common02) — gỡ thẻ, giữ chữ "thiết bị thổi gió" thành text thường (từ ブロア vẫn phải được dịch, chỉ bỏ markup tooltip thừa).

### [2052] — gasp (sweep lost-gasp-trailing) — ポーレット

- **JP:** 「え？　あ、あはははははは！\nあれ、誤解！　絶対、すっごい誤解してる～っ」
- **TW:** 「哎？啊、啊哈哈哈哈哈！她誤會了！她肯定是誤會了～」
- **VN cũ:** 「Hả? A, a ha ha ha ha ha ha!\nCái đó, là hiểu lầm! Chắc chắn là em ấy đang hiểu lầm cực kỳ nghiêm trọng luôn~」
- **Fix:** 「Hả? A, a ha ha ha ha ha ha!\nCái đó, là hiểu lầm! Chắc chắn là em ấy đang hiểu lầm cực kỳ nghiêm trọng luôn~Ư」
- **Lý do:** JP kết bằng ～っ; VN giữ dấu ~ nhưng mất gasp — thêm Ư cuối dòng theo đúng giá trị sweep.

### [2164] — đại từ: Paulette tự xưng "em" → "chị" (với Hibiki) — ポーレット

- **JP:** 「わかりました。喜んでお引き受けします。\nただ――」
- **TW:** 「我明白了。我樂意接受。只是——」
- **VN cũ:** 「Em hiểu rồi. Em rất sẵn lòng nhận lời.\nChỉ là――」
- **Fix:** 「Chị hiểu rồi. Chị rất sẵn lòng nhận lời.\nChỉ là――」
- **Lý do:** Paulette đang trả lời Hibiki (2160 Hibiki nhờ "Xin chị Paulette hãy cho em mượn sức mạnh"; 2161 Paulette đáp Hibiki bằng "chị mới là người phải cảm ơn"; 2294 trong file này Paulette với Hibiki cũng xưng "chị": "Nếu có việc gì chị làm được…"). Paulette lớn hơn Hibiki, xưng "chị" với Hibiki — "Em" ở đây sai, sửa cả 2 lần.

### [2186] — thẻ %l VN tự thêm — 日々姫

- **JP:** 「ブロア[トメベン,1]止弁開放！」
- **TW:** 「打開風管止回閥！」
- **VN cũ:** 「Mở van khóa \x%lブロア;#00ffc040;thiết bị thổi gió%l;#;!」
- **Fix:** 「Mở van khóa thiết bị thổi gió!」
- **Lý do:** Cùng thẻ ブロア VN tự thêm như 2039 (cùng một thẻ, xuất hiện 2 lần trong file); JP không có thẻ. Gỡ thẻ, giữ chữ — cùng tiền lệ.

### [2192] — đại từ: Soutetsu "anh" → "tôi" (với Hachiroku) — 双鉄

- **JP:** 「すまんな、ハチロク。\nならば、そうさせてもらうとしよう」
- **TW:** 「抱歉，八六。那就這麼辦吧」
- **VN cũ:** 「Xin lỗi em nhé, Hachiroku.\nNếu vậy thì, cho phép anh làm thế nhé.」
- **Fix:** 「Xin lỗi em nhé, Hachiroku.\nNếu vậy thì, cho phép tôi làm thế nhé.」
- **Lý do:** Soutetsu gọi đích danh Hachiroku; Soutetsu với Hachiroku = "tôi" (cô ấy gọi anh là 双鉄様/"ngài Soutetsu"). Chỉ sửa tự xưng "anh"→"tôi" ở câu sau; "Xin lỗi em nhé" GIỮ nguyên — cặp tôi/em là chuẩn khi Soutetsu nói với Hachiroku.

### [2193] — đại từ: Soutetsu "Anh" → "Tôi" (với Hachiroku) — 双鉄

- **JP:** 「案は了解。大賛成だ。\nが、現状のままでは、その案は空疎なものとなる」
- **TW:** 「方案我明白了。我十分贊成。問題是現在這個方案的條件尚不齊全」
- **VN cũ:** 「Anh đã hiểu phương án này. Hoàn toàn tán thành.\nNhưng, với tình hình hiện tại, phương án đó chỉ là lời nói suông thôi.」
- **Fix:** 「Tôi đã hiểu phương án này. Hoàn toàn tán thành.\nNhưng, với tình hình hiện tại, phương án đó chỉ là lời nói suông thôi.」
- **Lý do:** Nối tiếp ngay 2192, cùng cuộc trao đổi với Hachiroku về "phương án" giảm tải — phương án này là của Hachiroku + Paulette đề ra (2230 Hachiroku xác nhận: "Cả em――và cô Paulette, đều đang đưa ra phương án giảm bớt gánh nặng cho Hibiki"), không phải của Hibiki. Soutetsu với Hachiroku = "tôi".

### [2399] — gasp (sweep lost-gasp-whole) — 双鉄

- **JP:** 「っ！」
- **TW:** 「！」
- **VN cũ:** 「!」
- **Fix:** 「Ư!」
- **Lý do:** Cả dòng JP chỉ là gasp っ + dấu "!"; VN cũ chỉ còn dấu câu — thêm Ư theo đúng giá trị sweep.

### [2400] — gasp (sweep lost-gasp-whole) — 双鉄

- **JP:** 「っ！！？」
- **TW:** 「！！？」
- **VN cũ:** 「!!?」
- **Fix:** 「Ư!!?」
- **Lý do:** Như 2399 — cả dòng chỉ là gasp + dấu câu; thêm Ư theo đúng giá trị sweep.

### [2608] — sai nghĩa: mất cấu trúc điều kiện なら — monologue

- **JP:** だというのに、体がカっと熱くならない、\n血に濃い酒が混じってこないというのなら――
- **TW:** 儘管如此，我的身體卻沒有發熱，也沒那種血液中含有高濃度酒精的感覺。
- **VN cũ:** Thế mà cơ thể tôi lại không nóng bừng lên,\nmáu cũng không bị pha lẫn với rượu đặc――
- **VN mới:** Thế mà, nếu cơ thể tôi không nóng bừng lên,\nmáu cũng không bị pha lẫn với rượu đặc――
- **Lý do:** JP là câu điều kiện (…というのなら―― "nếu… thì――"), mở ra cho dòng sau 2609 ("Và rồi cuối cùng―― Tôi cũng có thể quay lại đối mặt với Hibiki"). VN cũ dịch thành câu trần thuật khẳng định ("cơ thể tôi lại không nóng…"), làm mất khung điều kiện if–then nối 2608→2609. Sửa lại dạng điều kiện với "nếu", giữ nguyên phần còn lại.

### [3073] — gasp (sweep lost-gasp-trailing) — monologue

- **JP:** 胸の上、鎖骨とともに真っ白な喉が上下する。\nまるでツバでも飲んだみたいに――っ！
- **TW:** 胸部上方，鎖骨和白皙的喉嚨一起起伏。就好像在咽口水——！
- **VN cũ:** Bên trên bầu ngực, yết hầu trắng ngần cùng xương quai xanh chuyển động lên xuống.\nCứ như thể em ấy vừa nuốt nước bọt vậy――!
- **Fix:** Bên trên bầu ngực, yết hầu trắng ngần cùng xương quai xanh chuyển động lên xuống.\nCứ như thể em ấy vừa nuốt nước bọt vậy――Ư!
- **Lý do:** JP kết bằng ――っ！; VN giữ dấu gạch + "!" nhưng mất gasp — thêm Ư theo đúng giá trị sweep.

## 5. Để vào đợt thống nhất (KHÔNG sửa trong audit này)

Theo quy ước các file gộp gần đây (ハチロク11, ポーレット03 obasan — parent đã chốt đưa vào đợt thống nhất thay vì sửa lẻ trong audit), các biến thể thuật ngữ toàn dự án dưới đây chỉ ghi nhận, không sửa ở đây:

- **"Ohimitera" → "Ohitoyo" (JP 御一夜):** 2172, 2260, 2369, 2778 (4 dòng; 2260 còn kèm Yui — xem dưới).
- **"Yui" → "Yunoi" (JP 湯医/湯医線):** 2260 ("chỉ có hai ga là Ohimitera và Yui"), 2302 ("tuyến Yui").
- **Gloss 列車 "tàu" → "đoàn tàu":** 3052 ("thành \x%l列車;#00ffc040;tàu%l;#; du lịch") — quyết định 21/11: quét các gloss 列車 khác trong đợt thống nhất.
- **Gloss 機関士 "người lái tàu":** 2155, 2299, 2838 (gloss %l), 2626 (text thường trong độc thoại: "người lái tàu Kiyomi") — toàn dự án chia nhiều dạng ("người lái tàu"/"lái tàu"/"thợ lái đầu máy"); tiền lệ ハチロク11 đã đưa dạng này vào đợt thống nhất.

## 6. Cờ chờ Hieu (KHÔNG tự quyết — ghi nhận, không sửa)

- **[2102] — người nghe mơ hồ (Paulette):** 「その後に悩むようなことがあったら、何でも聞いてね？わたし、教えてあげるから」 → VN: "Sau đó mà có chuyện gì phiền muộn, thì cứ hỏi em bất cứ điều gì nhé? Em sẽ chỉ cho anh." — Chủ đề là gánh nặng của Hibiki sau khi thành thị trưởng (nối 2100 Soutetsu nói với Hibiki) nên người nghe có vẻ là Hibiki → khi đó "Em sẽ chỉ cho anh" sai cả tự xưng lẫn xưng hô (phải là "Chị… cho em"). Nhưng cặp em/anh trong VN lại nhất quán nội bộ với người nghe là Soutetsu (Paulette→Soutetsu là em/anh), và "その後に" cũng có thể hiểu là Soutetsu lo cho Hibiki. Không đủ bằng chứng để chốt người nghe — GIỮ nguyên VN, chờ Hieu/parent quyết.
- **[2114] — Hibiki tự xưng "chị" mơ hồ:** 「そ、そうだね。ごめん――土嚢様は、お客っ、様……」 → VN: "Đ-Đúng vậy nhỉ. Chị xin lỗi――Bao cát-sama, là hành khách-sama……" — "Chị xin lỗi" đáng ngờ: Hibiki với Soutetsu/Hachiroku đều xưng "em" (nghiêng về "Em xin lỗi", người nghe là Hachiroku — người đã sửa cô ở 1942 — hoặc Soutetsu sau bài nói 2113). Nhưng "ごめん" cũng có thể là lời xin lỗi hướng tới chính các bao cát/hành khách mà cô đang tập gọi đúng cách, nên chưa chốt được người nghe — GIỮ nguyên VN, chờ Hieu/parent quyết.
- **B19 vẫn park:** không có dòng nào trong file này liên quan tới kiểm tra in-game Paulette 13 1596 hay sweep thẻ %l.

## 7. Lượt soát 2 (second pass — bắt buộc, đọc lại toàn bộ fix đối chiếu JP)

- **Tổng số fix: 12 / đọc lại đối chiếu JP: 12 / loại bỏ: 0 / sửa lại: 0.**
- Đã kiểm chứng lại từng fix: 5 gasp khớp sweep + JP (1731, 2052, 2399, 2400, 3073); 4 đại từ kiểm chứng theo dòng kề (1738 theo 2201 + 1739; 2164 theo 2160/2161/2294; 2192 gọi đích danh Hachiroku; 2193 nối tiếp 2192 + phương án của Hachiroku/Paulette ở 2230); 2 thẻ VN tự thêm khớp tiền lệ "gỡ thẻ, giữ chữ" (2039, 2186); 1 câu điều kiện khớp JP なら + TW (2608).
- JSON: 12 mục, key dạng chuỗi, list-of-dicts (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn lấy trực tiếp từ CSV3. Khối TOML: 12 khóa, parse bằng tomllib, **0 sai lệch giá trị** so với JSON. Mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (đã kiểm tra diff từng dòng: chỉ thêm Ư / đổi đại từ / gỡ markup thẻ / khôi phục "nếu").

## 8. Khối TOML đã kiểm chứng parse (tomllib)

```toml
[script]
1731 = "「……Ư」"
1738 = "「……Vớ vẩn, anh chưa uống lấy một giọt rượu nào cơ mà.」"
2039 = "「Phụ lái tàu. Mở van khóa thiết bị thổi gió.」"
2052 = "「Hả? A, a ha ha ha ha ha ha!\\nCái đó, là hiểu lầm! Chắc chắn là em ấy đang hiểu lầm cực kỳ nghiêm trọng luôn~Ư」"
2164 = "「Chị hiểu rồi. Chị rất sẵn lòng nhận lời.\\nChỉ là――」"
2186 = "「Mở van khóa thiết bị thổi gió!」"
2192 = "「Xin lỗi em nhé, Hachiroku.\\nNếu vậy thì, cho phép tôi làm thế nhé.」"
2193 = "「Tôi đã hiểu phương án này. Hoàn toàn tán thành.\\nNhưng, với tình hình hiện tại, phương án đó chỉ là lời nói suông thôi.」"
2399 = "「Ư!」"
2400 = "「Ư!!?」"
2608 = "Thế mà, nếu cơ thể tôi không nóng bừng lên,\\nmáu cũng không bị pha lẫn với rượu đặc――"
3073 = "Bên trên bầu ngực, yết hầu trắng ngần cùng xương quai xanh chuyển động lên xuống.\\nCứ như thể em ấy vừa nuốt nước bọt vậy――Ư!"
```

## Kết bài

File 日々姫08_開きかけのつぼみ là một file sạch về cấu trúc (397/397 dòng đọc đủ, 0 lệch dòng, 0 xoay, 0 nhiễm chéo, 0 mồ côi, 0 chưa dịch, 0 trùng key) với tỷ lệ sai thấp **12/397 = 3,0%** — lỗi tập trung ở đại từ Soutetsu/Paulette (4), gasp っ bị mất (5, đều đã có trong sweep), thẻ %l VN tự thêm (2) và một câu điều kiện bị dịch thành trần thuật (1). Hai dòng 2102 và 2114 còn mơ hồ về người nghe nên giữ nguyên chờ quyết định, không tự sửa. Bốn nhóm thuật ngữ (Ohimitera, Yui, gloss 列車 "tàu", gloss 機関士 "người lái tàu") để vào đợt thống nhất theo quy ước hiện hành. Sau file này tổng là **186 file / 8.849 dòng sai**.
