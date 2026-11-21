# lr_ハチロクh1_今ひとたびの契り.txt.toml — 64/358 sai (17,9%)

- File: `01_Hachiroku/lr_ハチロクh1_今ひとたびの契り.txt.toml` — route 01_Hachiroku, 358 dòng script (monologue 162, ハチロク 114, 双鉄 82). Nội dung: cảnh H "lời thề một lần nữa" của Hachiroku — sau buổi chụp hình Shiromuku ở đền Akai Aso, Soutetsu và Suzu kết lại lời thề hai kiếp, xen độc thoại giải thích về cơ thể Railord và hiện tượng triều xuy. Đây KHÔNG phải file ハチロクh1_契り.txt.toml (đã audit trước, 57 sai) — file này có tiền tố `lr_` và tựa đầy đủ 今ひとたびの契り, audit mới hoàn toàn, không tái dùng fix của file kia.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 bộ duy nhất, 358 dòng, 0 key trùng, 0 VN trống. TOML và CSV3 khớp tuyệt đối ngoài 181 dòng chênh ở `\n` literal bị TOML-2 làm phẳng thành khoảng trắng (CSV3 là chuẩn, đã kiểm chứng cơ học: 0 lệch ngoài flatten). TOML md5 `8f78fbd3c8217603ed8dc08dc2eeea3d`, BOM + CRLF, `[selections]` rỗng, không bản sao trùng (md5 xuất hiện 1 lần trong toàn bộ toml2). Thẻ `%l`: JP 0, VN 0 — file không có thẻ `%l` nào.
- Phân loại (64): xưng hô 22, gasp 18, romaji 9, đếm nguyên âm 7, thuật ngữ 3, sai nghĩa 3, khác 2. Theo nhân vật: 双鉄 30/82 (36,6%), ハチロク 24/114 (21,1%), monologue 10/162 (6,2%). Thoại 54/196 (27,6%), độc thoại 10/162 (6,2%).
- Gasp sweep: 18 mục cho file này — 17 mục có fix: áp nguyên văn 15 (1152, 1195, 1216, 1219, 1220, 1221, 1222, 1223, 1234, 1265, 1330, 1430, 1435, 1437, 1810), 2 mục gộp thêm sửa đếm nguyên âm (1142, 1264); 1 mục "needs-file-audit" (1314) đã xử lý trong audit (đại từ + gasp). Thêm 2 gasp sweep bỏ sót: 1156 (đoạn っ！！ cuối dòng) và gasp trong 1314. Đã quét cơ học toàn bộ dòng JP có っ: các っ còn lại đều là っ nhấn mạnh gắn từ có nội dung, っ trong thân từ, っ sau dấu câu (theo ranh giới gasp đã chốt), hoặc âm đã diễn (kh, ưm, phù, chụt) — 0 gasp bị bỏ sót thêm.
- Đại từ 22: Soutetsu "anh"→"tôi" với Hachiroku — tất cả 22 dòng Soutetsu còn tự xưng "anh" trong file; sau khi sửa, file không còn dòng Soutetsu nào tự xưng "anh" (đã quét cơ học). Tiền lệ: file h1_契り đã sửa 5 dòng cùng quy tắc (parent-verified 21/11). Độc thoại trong file đã dùng "tôi" nhất quán — thoại "anh" là lỗi không nhất quán của Gemini.
- Thuật ngữ 3: 御一夜 "Ohimitera"→"Ohitoyo" ×2 (1294, 1790); 潮吹き "squirting"→"triều xuy" (1256, theo chuẩn nội bộ file ở 1326/1342). Không có 帝鉄 / 湯医 / 宮司 / 日ノ本 / 乗員 / 乗務鞄 nào trong file — không có mục mới cho đợt unification từ file này.
- Moans: romaji 9 + đếm nguyên âm 7 + gasp 18 = 34/64 liên quan tiếng rên/SFX/gasp. Mẫu "Ưm + X" cho ん+X theo tiền lệ đã chốt của file h1_契り (んうっ → "Ưm ư", moan-fix xác nhận); họ ひゃ/ひゅ/ひあ/きゃ trong cảnh H → romaji theo quy tắc 21/11.
- Giữ nguyên có lý do: romaji "Sou, tetsu, sama" cho そうてつさま nói lắp (1139, 1417, 1228) — thói quen của file; "Nfu"/"nfu" cho んふっ (1187, 1262) — đếm 1:1 đúng; んくっ → "Nku" (1192), んひゅっ → "Nhyu" (1258, quy tắc 3b); っ sau dấu câu (!, ?, 。) không thêm Ư (1159, 1192, 1194, 1243) theo ranh giới gasp đã chốt; っ gắn từ có nội dung không thêm Ư (1187 それっっ, 1333 強さでっ); 1965 "Xâm nhậpppp..." theo cách diễn "xâm nhập" cho しにゅう của chính file (1976, 1982) — để vòng moan-fix phán lại; 1097 giữ cách diễn mottainai "quá lãng phí" của VN cũ (chỉ sửa đại từ); 1796 "しきり" không diễn riêng (TW cũng lược); 1416 "S-Soutetsu-sama" kiểu nói lắp chỉ lấy phụ âm đầu, khớp 1278 "H-hahi"; 861/1188 câu JP cắt ngang được VN giữ nguyên dạng cắt; 1278 "n a!"/"N u——" kiểu nói lắp tách chữ cái, giữ.
- Cờ cho Hieu: (1) 1314 gasp "rồi——Ư!" là phán đoán của audit (sweep ghi "needs-file-audit" rồi chuyển cho audit quyết) — nếu nghe gượng thì bỏ Ư, giữ "rồi!". (2) 1401 "Zuzu!" giữ cách gọi biến giọng ずず — phán đoán theo thói quen giữ nét nói vấp của file. (3) 1277 giữ dấu cắt "ạ—" thay vì viết trọn câu. (4) Không nhất quán nội bộ: そうてつさま hiragana có lúc romaji ("Sou, tetsu, sama" 1139/1417) có lúc "Ngài Soutetsu" (1190/1421) — để nguyên, ứng viên cho đợt thống nhất. (5) 1965 SFX "Xâm nhậpppp..." để vòng moan-fix phán lại. (6) B19 vẫn park.
- Lượt soát 2: 64/64 tái kiểm chứng, 0 bỏ, 0 sửa. (Trước lượt soát 2, bước kiểm tra diff cơ học đã bắt và sửa 13 lỗi chép tay trong bản nháp fix: 4 dấu 。 Nhật thay cho "." (853, 854, 1090, 1096) và 9 cặp ngoặc 「」 thừa ở các dòng monologue (1641, 1790, 1810, 1869, 1937, 1947, 1998, 1999, 2000) — đã sửa xong trước khi soát 2.)
- Kiểm chứng: JSON 64 mục dạng chuẩn, khóa chuỗi; khối TOML 64 khóa, parse OK, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 64/64; mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (đã kiểm tra diff cơ học).

## Chi tiết từng dòng sai (64)

### 853 — xưng hô (双鉄)
- JP: 「……挿入する際の潤滑を助けるためとの説が、\n有力であるとも書物でよんだ」
- TW: 「……我在書裡看到，它能在插入時起到潤滑效果的說法」
- VN cũ: 「……Anh từng đọc trong sách rằng giả thuyết nó giúp bôi trơn khi chèn vào\nlà có cơ sở nhất.」
- VN mới: 「……Tôi từng đọc trong sách rằng giả thuyết nó giúp bôi trơn khi chèn vào\nlà có cơ sở nhất.」
- Lý do: Soutetsu tự xưng "anh" với Hachiroku → "tôi" (quy tắc đã chốt; Hachiroku gọi "ngài Soutetsu"; độc thoại trong file dùng "tôi").

### 854 — xưng hô (双鉄)
- JP: 「……勃起はひどく繊細なものと思っていたが――\n指先は、なお鋭敏な感覚を持つものかもしれんな」
- TW: 「……我覺得陰莖是頗為敏感的組織——但想不到指尖竟似乎更加敏感」
- VN cũ: 「……Anh cứ nghĩ cương cứng là một thứ cực kỳ nhạy cảm——\nNhưng có lẽ đầu ngón tay còn có cảm giác nhạy bén hơn nữa.」
- VN mới: 「……Tôi cứ nghĩ cương cứng là một thứ cực kỳ nhạy cảm——\nNhưng có lẽ đầu ngón tay còn có cảm giác nhạy bén hơn nữa.」
- Lý do: Soutetsu "anh" → "tôi" với Hachiroku (như 853).

### 1090 — xưng hô (双鉄)
- JP: 「今日は、お前から契って欲しい」
- TW: 「今天的誓言，我希望能由你開始」
- VN cũ: 「Hôm nay, anh muốn em là người chủ động trao lời thề.」
- VN mới: 「Hôm nay, tôi muốn em là người chủ động trao lời thề.」
- Lý do: Soutetsu "anh" → "tôi" với Hachiroku.

### 1096 — xưng hô (双鉄)
- JP: 「僕の勃起を自由に使って、\nお前の体の求めるままに、思う存分擦るがいい」
- TW: 「你就自由使用我的勃起吧，就依你身體所願，盡情摩擦吧」
- VN cũ: 「Cứ tự do sử dụng sự cương cứng của anh,\nchà xát thỏa thích theo những gì cơ thể em khao khát đi.」
- VN mới: 「Cứ tự do sử dụng sự cương cứng của tôi,\nchà xát thỏa thích theo những gì cơ thể em khao khát đi.」
- Lý do: Soutetsu "của anh" → "của tôi" với Hachiroku.

### 1097 — xưng hô (双鉄)
- JP: 「すずは、本当に賢いな。\n僕にはもったいないほどだ。ん……」
- TW: 「你真是善解人意。真讓我自愧不如，愧感難當。嗯……」
- VN cũ: 「Suzu, em thật sự rất thông minh.\nĐến mức quá lãng phí đối với anh. Ưm……」
- VN mới: 「Suzu, em thật sự rất thông minh.\nĐến mức quá lãng phí đối với tôi. Ưm……」
- Lý do: Soutetsu "đối với anh" → "đối với tôi" với Hachiroku.

### 1102 — romaji (ハチロク)
- JP: 「求めるままに――\n一番、気持ちよくなるようにっ――んぅっ！！」
- TW: 「依我所願——最最、舒服的——嗯！！」
- VN cũ: 「Theo những gì em khao khát——\nĐể trở nên sung sướng nhất——ưm!!」
- VN mới: 「Theo những gì em khao khát——\nĐể trở nên sung sướng nhất——ưm ư!!」
- Lý do: JP んぅっ: VN cũ "ưm" làm mất nguyên âm う. Tiền lệ h1_契り: んうっ → "Ưm ư" (moan-fix xác nhận mẫu "Ưm + ư×n").

### 1118 — xưng hô (双鉄)
- JP: 「なるほど、ざらざら――いや、ツブツブとしているな。\nこれが僕の勃起を刺激してくれているのか」
- TW: 「原來如此，是這樣略顯粗澀——不，應該說是一粒粒的感覺。往常就是這些在刺激我的勃起啊」
- VN cũ: 「Ra là vậy, ram ráp——không, là sần sùi nhỉ.\nĐây là thứ kích thích sự cương cứng của anh sao.」
- VN mới: 「Ra là vậy, ram ráp——không, là sần sùi nhỉ.\nĐây là thứ kích thích sự cương cứng của tôi sao.」
- Lý do: Soutetsu "của anh" → "của tôi" với Hachiroku.

### 1142 — gasp (ハチロク)
- JP: 「ひゃぅぅぅぅぅぅぅうぅぅぅぅぅぅ～～～っ！！！」
- TW: 「呀嗚～～～！！！」
- VN cũ: 「Hyauuuuuuuuuuuuuuuu~~~!!!」
- VN mới: 「Hyauuuuuuuuuuuuuu~~~Ư!!!」
- Lý do: Sweep: っ cuối sau ~~~ bị rớt → thêm Ư. Đồng thời đếm nguyên âm: JP ひゃぅ×13+う = 14 âm u, VN cũ 16 u (thừa 2) → 14 u.

### 1145 — romaji (ハチロク)
- JP: 「きゃっ！？」
- TW: 「呀！？」
- VN cũ: 「Á!?」
- VN mới: 「Kya!?」
- Lý do: JP きゃっ: VN cũ "Á" là lỗi mất âm (rớt phụ âm ky-). Quy tắc 21/11: họ ひゃ/ひゅ/ひあ/きゃ trong cảnh H → romaji (Hya/Hyu/Hia/Kya).

### 1152 — gasp (ハチロク)
- JP: 「っ！！？」
- TW: 「呃！！？」
- VN cũ: 「!!?」
- VN mới: 「Ư!!?」
- Lý do: Sweep (lost-gasp-whole): JP cả dòng chỉ là っ+punct, VN chỉ còn punctuation → thêm Ư.

### 1156 — gasp (ハチロク)
- JP: 「ふやっ！　あっ！　あっ！　あっ！　あっ！　っ！！\nそうてつ！　さまっ！　わらくひっ！　わたくしっ！」
- TW: 「呼呀！啊！啊！啊！啊！唔！！雙鐵！少爺！我已經！我已經！」
- VN cũ: 「Fuya! A! A! A! A! !!\nSou, tetsu! Sama! E-em! Em!」
- VN mới: 「Fuya! A! A! A! A! Ư!!\nSou, tetsu! Sama! E-em! Em!」
- Lý do: Gasp sweep bỏ sót: đoạn cuối dòng 1 "っ！！" là gasp độc lập ở cuối dòng, VN cũ chỉ còn "!!" → thêm Ư (tiền lệ h1_契り 1271: っ…… giữa dòng → Ư; 1293: っ đầu dòng → Ư).

### 1173 — romaji (ハチロク)
- JP: 「ふぁっ――あっ――あっ――んうっ！！！？」
- TW: 「哈——啊——啊——嗯嗚！！！？」
- VN cũ: 「Fua——a——a——ưm!!!?」
- VN mới: 「Fua——a——a——Ưm ư!!!?」
- Lý do: JP んうっ: VN cũ "ưm" làm mất nguyên âm う → "Ưm ư" (tiền lệ h1_契り んうっ → "Ưm ư").

### 1174 — đếm nguyên âm (ハチロク)
- JP: 「ふあっ――あっ――あっ――（ごくっ）――\nはあっ――はあっ――はあっ――はあっ――」
- TW: 「哈——啊——啊——（咽口水）哈——哈——哈——哈——」
- VN cũ: 「Fua——a——a——(ực)——\nHa——ha——ha——ha——」
- VN mới: 「Fua——a——a——(ực)——\nHaa——haa——haa——haa——」
- Lý do: JP はあっ ×4: は+あ = 2 âm a mỗi đoạn; VN cũ "Ha" chỉ 1 a → "Haa" (tiền lệ h9 2054: はぁっ → "haa").

### 1194 — romaji (ハチロク)
- JP: 「ふあっ！　あっ！　あっ！　あっ！\nんうっ！　あっ！　ふっ！　ふやっ！！」
- TW: 「哈！啊！啊！啊！嗯嗚！啊！呼！呀！！」
- VN cũ: 「Fua! A! A! A!\nNnu! A! Fu! Fuya!!」
- VN mới: 「Fua! A! A! A!\nƯm ư! A! Fu! Fuya!!」
- Lý do: JP んうっ: VN cũ "Nnu" thừa 1 n (1 ん chỉ 1 n) và viết kiểu romaji; theo mẫu đã chốt của file h1_契り (ん+X → "Ưm + X"): "Ưm ư".

### 1195 — gasp (ハチロク)
- JP: 「ふあっ！　あっ！　あっ！　～～～～っ！！！」
- TW: 「哈！啊！啊！～～～～唔！！！」
- VN cũ: 「Fua! A! A! ~~~~!!!」
- VN mới: 「Fua! A! A! ~~~~Ư!!!」
- Lý do: Sweep (lost-gasp-trailing): ~~~~っ cuối dòng bị rớt → thêm Ư sau ~~~~.

### 1198 — romaji (ハチロク)
- JP: 「ふぁっ！　んぅっ――」
- TW: 「哈！嗯——」
- VN cũ: 「Fua! Nnu——」
- VN mới: 「Fua! Ưm ư——」
- Lý do: JP んぅっ: VN cũ "Nnu" thừa 1 n; theo mẫu "Ưm + X": "Ưm ư".

### 1206 — xưng hô (双鉄)
- JP: 「からかってなど」
- TW: 「哪有戲弄啊」
- VN cũ: 「Anh đâu có trêu.」
- VN mới: 「Tôi đâu có trêu.」
- Lý do: Soutetsu "Anh" → "Tôi" với Hachiroku.

### 1216 — gasp (双鉄)
- JP: 「――っっっ」
- TW: 「唔唔」
- VN cũ: 「——」
- VN mới: 「——ƯƯƯ」
- Lý do: Sweep (đa-っ): JP "――っっっ", mỗi っ → 1 Ư.

### 1219 — gasp (双鉄)
- JP: 「っ！！」
- TW: 「唔！！」
- VN cũ: 「!!」
- VN mới: 「Ư!!」
- Lý do: Sweep (lost-gasp-whole): JP "っ！！" → "Ư!!".

### 1220 — gasp (双鉄)
- JP: 「っ！！！」
- TW: 「唔！！！」
- VN cũ: 「!!!」
- VN mới: 「Ư!!!」
- Lý do: Sweep (lost-gasp-whole): JP "っ！！！" → "Ư!!!".

### 1221 — gasp (双鉄)
- JP: 「っ！！！！」
- TW: 「唔！！！！」
- VN cũ: 「!!!!」
- VN mới: 「Ư!!!!」
- Lý do: Sweep (lost-gasp-whole): JP "っ！！！！" → "Ư!!!!".

### 1222 — gasp (ハチロク)
- JP: 「っ！！！！！」
- TW: 「唔！！！！！」
- VN cũ: 「!!!!!」
- VN mới: 「Ư!!!!!」
- Lý do: Sweep (lost-gasp-whole): JP "っ！！！！！" → "Ư!!!!!".

### 1223 — gasp (双鉄)
- JP: 「っ！！！？」
- TW: 「唔！！！？」
- VN cũ: 「!!!?」
- VN mới: 「Ư!!!?」
- Lý do: Sweep (lost-gasp-whole): JP "っ！！！？" → "Ư!!!?".

### 1234 — gasp (ハチロク)
- JP: 「あ……――んっ――ちゅむっ――ちゅうっ――っ」
- TW: 「啊……嗯——啾——啾——」
- VN cũ: 「A……——ưm——chum——chuu——」
- VN mới: 「A……——ưm——chum——chuu——Ư」
- Lý do: Sweep (lost-gasp-trailing): ちゅうっ――っ cuối dòng bị rớt → thêm Ư cuối.

### 1238 — đếm nguyên âm (双鉄)
- JP: 「ああ」
- TW: 「啊」
- VN cũ: 「A.」
- VN mới: 「Aa.」
- Lý do: JP ああ = 2 âm a; VN cũ "A." chỉ 1 → "Aa." (tiền lệ h1_契り 1264: ああっ → "Aa").

### 1247 — romaji (ハチロク)
- JP: 「んぅぅ――くっ――ぁっ――」
- TW: 「嗯——唔——啊——」
- VN cũ: 「Nnuu——ku——a——」
- VN mới: 「Ưm ưư——ku——a——」
- Lý do: JP んぅぅ: VN cũ "Nnuu" thừa 1 n; theo mẫu "Ưm + ư×n": "Ưm ưư" (2 ư cho 2 ぅ).

### 1249 — romaji (ハチロク)
- JP: 「んっ――ぁっ――んうっっ――ふっ――やっ――」
- TW: 「嗯——啊——嗯嗚——呼——呀——」
- VN cũ: 「Ưm——a——nnu——fu——ya——」
- VN mới: 「Ưm——a——ưm ư——fu——ya——」
- Lý do: JP んうっっ: VN cũ "nnu" thừa 1 n; theo mẫu "Ưm + X" (giữ chữ thường giữa dòng): "ưm ư".

### 1253 — xưng hô (双鉄)
- JP: 「ああ。ここから先は、僕も動こう。\nおまえと、僕と――僕はふたりで、契りたい」
- TW: 「嗯。接下來我也要動了。希望你和我，共同立下誓言」
- VN cũ: 「Ừ. Từ đây trở đi, anh cũng sẽ chuyển động.\nEm, và anh——anh muốn hai chúng ta cùng nhau trao lời thề.」
- VN mới: 「Ừ. Từ đây trở đi, tôi cũng sẽ chuyển động.\nEm, và tôi——tôi muốn hai chúng ta cùng nhau trao lời thề.」
- Lý do: Soutetsu "anh" ×3 → "tôi" với Hachiroku.

### 1256 — thuật ngữ (双鉄)
- JP: 「ああ。潮吹きという現象らしい」
- TW: 「嗯。這好像就是所謂的潮吹」
- VN cũ: 「Ừ. Hình như gọi là hiện tượng squirting (triều xuy).」
- VN mới: 「Ừ. Hình như đó là hiện tượng gọi là triều xuy.」
- Lý do: JP 潮吹き: file này đã chuẩn "triều xuy" (1326, 1342); VN cũ chèn tiếng Anh "squirting" không nhất quán → dùng "triều xuy".

### 1262 — romaji (ハチロク)
- JP: 「んぅっ！　んっ！　あっ！　んふっ！\n双鉄、さま――そうてつさまぁ」
- TW: 「嗯唔！嗯！啊！嗯呼！雙鐵，少爺——雙鐵少爺」
- VN cũ: 「Nn! Nn! A! Nfu!\nNgài Soutetsu——Ngài Soutetsu~」
- VN mới: 「Ưm ư! Ưm! A! Nfu!\nNgài Soutetsu——Ngài Soutetsu~」
- Lý do: JP んぅっ → VN cũ "Nn" làm mất nguyên âm u; んっ → "Nn" trái mẫu của chính file (んっ → "Ưm" ở 1245/1266/1268). Theo mẫu "Ưm + X": "Ưm ư! Ưm!".

### 1263 — đếm nguyên âm (ハチロク)
- JP: 「んゅうううううううううううっっっっ！」
- TW: 「嗯嗚～～！！！」
- VN cũ: 「Nyuuuuuuuuuuu!」
- VN mới: 「Nyuuuuuuuuuuuu!」
- Lý do: JP んゅう×11: んゅ (1 u) + 11 う = 12 âm u; VN cũ 11 u (thiếu 1) → 12 u.

### 1264 — gasp (ハチロク)
- JP: 「んんんんぅぅぅぅ～～～～～っ！！！」
- TW: 「嗯嗚～～～！！！」
- VN cũ: 「Nnnnnnuuuuu~~~~~!!!」
- VN mới: 「Nnnnuuuu~~~~~Ư!!!」
- Lý do: Sweep: ~~~~~っ cuối dòng → thêm Ư. Đồng thời đếm: JP ん×4+ぅ×4, VN cũ 6 n + 5 u (thừa 2 n, thừa 1 u) → 4 n + 4 u theo đếm 1:1 (tiền lệ h1_契り: あああ → "Aaa", 3 a).

### 1265 — gasp (ハチロク)
- JP: 「んん～～～～～～っ！！！！」
- TW: 「嗯嗯～～～～～～！！！！」
- VN cũ: 「Nn~~~~~~!!!!」
- VN mới: 「Nn~~~~~~Ư!!!!」
- Lý do: Sweep (lost-gasp-trailing): ~~~~~~っ cuối dòng → thêm Ư. Đếm đã đúng: ん×2 → "Nn".

### 1274 — xưng hô (双鉄)
- JP: 「わかった。もう少し長く大きく動かそう」
- TW: 「好吧，那就稍微加大點動作吧」
- VN cũ: 「Anh hiểu rồi. Anh sẽ di chuyển dài và mạnh hơn một chút nhé.」
- VN mới: 「Tôi hiểu rồi. Tôi sẽ di chuyển dài và lớn hơn một chút nhé.」
- Lý do: Soutetsu "Anh" ×2 → "Tôi" với Hachiroku. Đồng thời 長く大きく: "mạnh" → "lớn" (大きく = lớn, không phải mạnh; TW "加大點動作").

### 1277 — khác (ハチロク)
- JP: 「はいっ！　はいっ！\nわたくし、うれしゅうございま」
- TW: 「好的！好的！我好高興……」
- VN cũ: 「Vâng! Vâng!\nEm, rất vui ạ.」
- VN mới: 「Vâng! Vâng!\nEm, rất vui ạ—」
- Lý do: JP "うれしゅうございま" bị cắt ngang giữa từ (thiếu す); VN cũ viết trọn câu là bịa phần hoàn thiện → giữ dấu cắt bằng "—" (tiền lệ ハチロク06 1654: giữ nguyên dạng cắt).

### 1283 — xưng hô (双鉄)
- JP: 「このまま達して、かわいい姿を見せてくれ」
- TW: 「就這樣高潮吧，把你最可愛的樣子展現給我吧」
- VN cũ: 「Cứ thế này mà lên đỉnh đi, cho anh xem dáng vẻ đáng yêu của em nào.」
- VN mới: 「Cứ thế này mà lên đỉnh đi, cho tôi xem dáng vẻ đáng yêu của em nào.」
- Lý do: Soutetsu "cho anh xem" → "cho tôi xem" với Hachiroku.

### 1290 — xưng hô (双鉄)
- JP: 「すずのおまんまんに入るのは……\n僕のおちんちんか舌かのどちらかだけだものな。普段は」
- TW: 「往常，進入鈴私處的……只有我的分身和舌頭吧」
- VN cũ: 「Bình thường, những thứ đi vào cô bé của Suzu……\nchỉ có dương vật hoặc lưỡi của anh thôi nhỉ.」
- VN mới: 「Bình thường, những thứ đi vào cô bé của Suzu……\nchỉ có dương vật hoặc lưỡi của tôi thôi nhỉ.」
- Lý do: Soutetsu "lưỡi của anh" → "lưỡi của tôi" với Hachiroku.

### 1294 — thuật ngữ (双鉄)
- JP: 「御一夜の象徴のひとつ、赤井阿蘇神社の社殿と、\n白無垢のすず。伝えたい事を端的に示し、実に良かった」
- TW: 「御一夜地標之一的赤井阿蘇神社大殿，與身著白無垢禮服的鈴。開門見山直奔主題，著實是很不錯的表現方式」
- VN cũ: 「Ngôi đền Akai Aso, một trong những biểu tượng của Ohimitera,\nvà Suzu trong trang phục Shiromuku. Thể hiện trực tiếp thông điệp muốn truyền tải, thật sự rất tuyệt.」
- VN mới: 「Ngôi đền Akai Aso, một trong những biểu tượng của Ohitoyo,\nvà Suzu trong trang phục Shiromuku. Thể hiện trực tiếp thông điệp muốn truyền tải, thật sự rất tuyệt.」
- Lý do: JP 御一夜: VN cũ "Ohimitera" → "Ohitoyo" (quy tắc đã chốt).

### 1308 — xưng hô (双鉄)
- JP: 「動いていない――っ――勃起が勝手に――\n喜んで――そうして、震えてしまっているのだ」
- TW: 「我沒有動——是它擅自——它太高興了——所以在不住顫抖」
- VN cũ: 「Anh không có cử động——sự cương cứng tự ý——\nvui sướng——rồi run rẩy lên đấy chứ.」
- VN mới: 「Tôi không có cử động——sự cương cứng tự ý——\nvui sướng——rồi run rẩy lên đấy chứ.」
- Lý do: Soutetsu "Anh" → "Tôi" với Hachiroku.

### 1314 — xưng hô (双鉄)
- JP: 「わかっている、すず。\n僕も――こみあげ――きって――いるっ――っ！」
- TW: 「我知道，鈴。我也——快要——到極限——了！」
- VN cũ: 「Anh biết rồi, Suzu.\nAnh cũng——đang trào dâng——đến giới hạn——rồi!」
- VN mới: 「Tôi biết rồi, Suzu.\nTôi cũng——đang trào dâng——đến giới hạn——rồi——Ư!」
- Lý do: Soutetsu "Anh" ×2 → "Tôi" với Hachiroku. Gasp (sweep ghi "needs-file-audit"): JP kết "いるっ――っ！" — っ cuối sau —— là gasp độc lập, VN cũ "rồi!" làm mất → thêm "——Ư" (phán đoán của audit, ghi cờ).

### 1316 — xưng hô (双鉄)
- JP: 「僕は、お前と[にせ,1]二世の[ちぎ]契りを結びたい。\n白無垢姿のお前を抱いて――今一度深く、刻みたい」
- TW: 「我願與你立白頭偕老誓言。擁你著白無垢入懷——誓言更深鐫心間」
- VN cũ: 「Anh muốn kết duyên vợ chồng với em.\nÔm em trong bộ Shiromuku này——khắc ghi thật sâu một lần nữa.」
- VN mới: 「Tôi muốn cùng em kết lời thề duyên hai kiếp.\nÔm em trong bộ Shiromuku này——khắc ghi thật sâu một lần nữa.」
- Lý do: Soutetsu "Anh" → "Tôi". Đồng thời JP 二世の契り: VN cũ "kết duyên vợ chồng" làm mất "hai kiếp" → "kết lời thề duyên hai kiếp" (khớp 1327 trong file).

### 1320 — xưng hô (双鉄)
- JP: 「股を大きく、開いて欲しい」
- TW: 「把腿大張開來，好嗎」
- VN cũ: 「Anh muốn em, mở rộng hai chân ra.」
- VN mới: 「Tôi muốn em, mở rộng hai chân ra.」
- Lý do: Soutetsu "Anh" → "Tôi" với Hachiroku.

### 1322 — xưng hô (双鉄)
- JP: 「股を。大きく。開いて。欲しい。」
- TW: 「把腿，大張開來，好嗎」
- VN cũ: 「Anh muốn. Em mở rộng. Hai chân ra.」
- VN mới: 「Tôi muốn. Em mở rộng. Hai chân ra.」
- Lý do: Soutetsu "Anh" → "Tôi" với Hachiroku.

### 1330 — gasp (双鉄)
- JP: 「ゆえ、にっ――っ！！！！」
- TW: 「既然，這樣！！！！」
- VN cũ: 「Vì, vậy——!!!!」
- VN mới: 「Vì, vậy——Ư!!!!」
- Lý do: Sweep (lost-gasp-trailing): にっ――っ cuối dòng → thêm Ư sau —— (っ gắn に là từ có nội dung đã diễn bằng "vậy"; っ cuối sau —— là gasp).

### 1346 — xưng hô (双鉄)
- JP: 「無論だ。\nそれは、僕の望みだ」
- TW: 「當然。那也是我畢生所願」
- VN cũ: 「Tất nhiên rồi.\nĐó cũng là tâm nguyện của anh.」
- VN mới: 「Tất nhiên rồi.\nĐó cũng là tâm nguyện của tôi.」
- Lý do: Soutetsu "của anh" → "của tôi" với Hachiroku.

### 1351 — xưng hô (双鉄)
- JP: 「そこまで照れさせてしまったか。\n夢中になるうち度を越したらしいな。申し訳ない」
- TW: 「竟這麼讓你害羞啊。我沉醉其中卻不知失了分寸，抱歉」
- VN cũ: 「Làm em xấu hổ đến vậy sao.\nCó vẻ như mải mê quá nên anh hơi quá đà rồi. Xin lỗi em.」
- VN mới: 「Làm em xấu hổ đến vậy sao.\nCó vẻ như mải mê quá nên tôi hơi quá đà rồi. Xin lỗi em.」
- Lý do: Soutetsu "anh" → "tôi" với Hachiroku.

### 1388 — xưng hô (双鉄)
- JP: 「ならば、その珍しさを楽しもう。\n僕も、お前も――ゆっくりゆっくり」
- TW: 「那我們就一同來享受這難得的機會吧。我們來一起細細品味」
- VN cũ: 「Vậy thì, hãy cùng tận hưởng sự mới mẻ này.\nCả anh, và cả em——từ từ, chầm chậm thôi.」
- VN mới: 「Vậy thì, hãy cùng tận hưởng sự mới mẻ này.\nCả tôi, và cả em——từ từ, chầm chậm thôi.」
- Lý do: Soutetsu "Cả anh" → "Cả tôi" với Hachiroku.

### 1391 — xưng hô (双鉄)
- JP: 「ならば嬉しい。僕はお前の、\n羞恥に震える姿も美しく可憐と感じるゆえに」
- TW: 「那我就更開心了。你這樣因感到羞恥而戰慄的樣子，讓我更覺美麗而憐愛」
- VN cũ: 「Thế thì anh rất vui. Bởi vì,\ndáng vẻ run rẩy vì xấu hổ của em, anh cũng thấy vô cùng xinh đẹp và đáng yêu.」
- VN mới: 「Thế thì tôi rất vui. Bởi vì,\ndáng vẻ run rẩy vì xấu hổ của em, tôi cũng thấy vô cùng xinh đẹp và đáng yêu.」
- Lý do: Soutetsu "anh" ×2 → "tôi" với Hachiroku.

### 1398 — xưng hô (双鉄)
- JP: 「な？　すず。\n僕のかわいい、僕だけのすず」
- TW: 「鈴。可愛的鈴，只屬於我的鈴」
- VN cũ: 「Phải không? Suzu.\nSuzu đáng yêu của anh, Suzu của riêng anh.」
- VN mới: 「Phải không? Suzu.\nSuzu đáng yêu của tôi, Suzu của riêng tôi.」
- Lý do: Soutetsu "của anh" ×2 → "của tôi" với Hachiroku.

### 1401 — khác (双鉄)
- JP: 「すずっ！　ずずっ！　すずっ！　すずっ！！！」
- TW: 「鈴！鈴！鈴！鈴！！！」
- VN cũ: 「Suzu! Suzu! Suzu! Suzu!!!」
- VN mới: 「Suzu! Zuzu! Suzu! Suzu!!!」
- Lý do: JP "ずずっ" là cách Soutetsu gọi tên bị biến giọng (voiced) giữa chuỗi gọi tên; VN cũ "Suzu" chuẩn hoá làm mất nét này → "Zuzu" (khớp thói quen giữ nét nói lắp/nói vấp của file: 1396 "Su, zu——", 1278 "H-hahi").

### 1403 — xưng hô (双鉄)
- JP: 「すず？　そのまま指に集中するんだ」
- TW: 「鈴，集中精神感覺我的手指」
- VN cũ: 「Suzu? Cứ thế tập trung vào ngón tay anh đi.」
- VN mới: 「Suzu? Cứ thế tập trung vào ngón tay tôi đi.」
- Lý do: Soutetsu "ngón tay anh" → "ngón tay tôi" với Hachiroku.

### 1423 — sai nghĩa (ハチロク)
- JP: 「双鉄さまのっ、おっきくっ、くびれて、いらっしゃる、\nとこっ――がっ――ぁっ！　ぐいって、ぐいってっ」
- TW: 「雙鐵少爺，好大，緊緊地，包裹著，的地方——啊！頂到了，頂到了」
- VN cũ: 「Chỗ, to lớn, thắt lại, của ngài Soutetsu,\nchỗ đó——đang——a! Cọ xát, cọ xát.」
- VN mới: 「Chỗ, to lớn, thắt lại, của ngài Soutetsu,\nchỗ đó——đang——a! Thúc vào, thúc vào.」
- Lý do: JP ぐいって: "thúc/đâm vào" (TW 頂到了 = chạm tới/đâm tới); VN cũ "Cọ xát" (chà xát) sai nghĩa động tác.

### 1430 — gasp (ハチロク)
- JP: 「～～～っ」
- TW: 「～～～唔」
- VN cũ: 「~~~」
- VN mới: 「~~~Ư」
- Lý do: Sweep (lost-gasp-trailing): JP "～～～っ" → thêm Ư.

### 1435 — gasp (ハチロク)
- JP: 「～～～～～～っ」
- TW: 「～～～～～～嗚」
- VN cũ: 「~~~~~~」
- VN mới: 「~~~~~~Ư」
- Lý do: Sweep (lost-gasp-trailing): JP "～～～～～～っ" → thêm Ư.

### 1437 — gasp (ハチロク)
- JP: 「～～～～～～～～～～～～っ！！！！！！」
- TW: 「～～～～～～～～～～～～唔！！！！！！」
- VN cũ: 「~~~~~~~~~~~~!!!!!!」
- VN mới: 「~~~~~~~~~~~~Ư!!!!!!」
- Lý do: Sweep (lost-gasp-trailing): JP "～～～～～～～～～～～～っ！！！！！！" → thêm Ư.

### 1641 — sai nghĩa (monologue)
- JP: 黒髪に何度も何度も口づけて、鼻を心地よくくすぐられ。\n同時に指を、割れ目の可愛い筋に幾度も滑らせる。
- TW: 我不停地親吻著她烏黑的秀髮，鼻腔洋溢著她髮絲間飄逸的芬芳。同時，手指也在她可愛的蜜隙上徜徉。
- VN cũ: Tôi hôn đi hôn lại lên mái tóc đen nhánh, chiếc mũi được cọ xát thật dễ chịu.\nĐồng thời, tôi trượt ngón tay nhiều lần trên đường rãnh đáng yêu của khe hở.
- VN mới: Tôi hôn đi hôn lại lên mái tóc đen nhánh, chiếc mũi được cù nhẹ thật dễ chịu.\nĐồng thời, tôi trượt ngón tay nhiều lần trên đường rãnh đáng yêu của khe hở.
- Lý do: JP 鼻をくすぐられ: くすぐる = cù/nhột; VN cũ "được cọ xát" (chà xát) sai cảm giác → "được cù nhẹ".

### 1790 — thuật ngữ (monologue)
- JP: レイルロオドの戸籍創出・婚姻特区。\n御一夜市の新しい魅力をPRするための、ポスター撮影。
- TW: 這次拍攝是為了製作海報，宣傳的是御一夜市“鐵路人偶戶籍、婚姻登記特區”這一嶄新魅力。
- VN cũ: Đặc khu thiết lập hộ tịch và hôn nhân cho Railord.\nBuổi chụp hình áp phích nhằm quảng bá cho sức hấp dẫn mới của thành phố Ohimitera.
- VN mới: Đặc khu thiết lập hộ tịch và hôn nhân cho Railord.\nBuổi chụp hình áp phích nhằm quảng bá cho sức hấp dẫn mới của thành phố Ohitoyo.
- Lý do: JP 御一夜市: VN cũ "thành phố Ohimitera" → "thành phố Ohitoyo" (quy tắc đã chốt).

### 1810 — gasp (monologue)
- JP: きゅうううんと一気に膣がしまっ――っ！！？？
- TW: 鈴的蜜穴猛地夾緊——！！？？
- VN cũ: Âm đạo đột ngột siết chặt lại——!!??
- VN mới: Âm đạo đột ngột siết chặt lại——Ư!!??
- Lý do: Sweep (lost-gasp-trailing): JP "しまっ――っ！！？？" — っ cuối sau —— là gasp, VN cũ chỉ còn "——!!??" → thêm Ư.

### 1869 — sai nghĩa (monologue)
- JP: 僕が指差した場所ではなく、一番奥のくぱくぱに、\n亀頭をぐいっと深く押し当て――
- TW: 龜頭長驅直入，卻不是向著我剛才指的位置，而是頂在了最深處的那處柔軟之上。
- VN cũ: Không phải chỗ tôi chỉ, mà là phần mở ra đóng lại ở tít sâu bên trong,\nem ấy ấn mạnh quy đầu vào thật sâu——
- VN mới: Không phải chỗ tôi chỉ, mà là phần mở ra đóng lại ở tít sâu bên trong,\ntôi ấn mạnh quy đầu vào thật sâu——
- Lý do: Đổi chủ ngữ: JP "亀頭をぐいっと深く押し当て" chủ ngữ là 僕 (Soutetsu, tiếp nối "僕が指差した場所ではなく"); TW cũng xác nhận quy đầu của Soutetsu đâm vào. VN cũ "em ấy ấn mạnh quy đầu" gán sai cho Suzu.

### 1937 — đếm nguyên âm (monologue)
- JP: （ああ）
- TW: （啊）
- VN cũ: （A）
- VN mới: （Aa）
- Lý do: JP （ああ） = 2 âm a; VN cũ "（A）" chỉ 1 → "（Aa）".

### 1947 — đếm nguyên âm (monologue)
- JP: （じゅぽっ――ずぶうううううううっ！　ぐりっっっ！）
- TW: （噴湧）
- VN cũ: （Jupo——zubuuuuuuu! Guri!!!）
- VN mới: （Jupo——zubuuuuuuuu! Guri!!!）
- Lý do: JP ずぶう×7: ぶ + 7 う = 8 âm u ở âm tiết đó; VN cũ "zubuuuuuuu" chỉ 7 u ở âm tiết đó (tổng 8, cần 9) → thêm 1 u.

### 1998 — đếm nguyên âm (monologue)
- JP: （きゅうううううううううっ！）
- TW: （緊緊包裹）
- VN cũ: （Kyuuuuuuuuu!）
- VN mới: （Kyuuuuuuuuuu!）
- Lý do: JP きゅう×9: きゅ (1 u) + 9 う = 10 âm u; VN cũ 9 u (thiếu 1) → 10 u.

### 1999 — đếm nguyên âm (monologue)
- JP: （きゅうううううううううううっっ！！！！）
- TW: （緊緊束縛）
- VN cũ: （Kyuuuuuuuuuuu!!!!）
- VN mới: （Kyuuuuuuuuuuuu!!!!）
- Lý do: JP きゅう×11: きゅ (1 u) + 11 う = 12 âm u; VN cũ 11 u (thiếu 1) → 12 u.

### 2000 — đếm nguyên âm (monologue)
- JP: （ずぶうううううううううううっ！　ごつっ！！！）
- TW: （緩慢抽出，而後猛然插入）
- VN cũ: （Zubuuuuuuuuuuu! Gotsu!!!）
- VN mới: （Zubuuuuuuuuuuuu! Gotsu!!!）
- Lý do: JP ずぶう×11: ぶ + 11 う = 12 âm u ở âm tiết đó (tổng 13 kể cả ず); VN cũ 12 u tổng (thiếu 1) → 13 u.

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
853 = "「……Tôi từng đọc trong sách rằng giả thuyết nó giúp bôi trơn khi chèn vào\\nlà có cơ sở nhất.」"
854 = "「……Tôi cứ nghĩ cương cứng là một thứ cực kỳ nhạy cảm——\\nNhưng có lẽ đầu ngón tay còn có cảm giác nhạy bén hơn nữa.」"
1090 = "「Hôm nay, tôi muốn em là người chủ động trao lời thề.」"
1096 = "「Cứ tự do sử dụng sự cương cứng của tôi,\\nchà xát thỏa thích theo những gì cơ thể em khao khát đi.」"
1097 = "「Suzu, em thật sự rất thông minh.\\nĐến mức quá lãng phí đối với tôi. Ưm……」"
1102 = "「Theo những gì em khao khát——\\nĐể trở nên sung sướng nhất——ưm ư!!」"
1118 = "「Ra là vậy, ram ráp——không, là sần sùi nhỉ.\\nĐây là thứ kích thích sự cương cứng của tôi sao.」"
1142 = "「Hyauuuuuuuuuuuuuu~~~Ư!!!」"
1145 = "「Kya!?」"
1152 = "「Ư!!?」"
1156 = "「Fuya! A! A! A! A! Ư!!\\nSou, tetsu! Sama! E-em! Em!」"
1173 = "「Fua——a——a——Ưm ư!!!?」"
1174 = "「Fua——a——a——(ực)——\\nHaa——haa——haa——haa——」"
1194 = "「Fua! A! A! A!\\nƯm ư! A! Fu! Fuya!!」"
1195 = "「Fua! A! A! ~~~~Ư!!!」"
1198 = "「Fua! Ưm ư——」"
1206 = "「Tôi đâu có trêu.」"
1216 = "「——ƯƯƯ」"
1219 = "「Ư!!」"
1220 = "「Ư!!!」"
1221 = "「Ư!!!!」"
1222 = "「Ư!!!!!」"
1223 = "「Ư!!!?」"
1234 = "「A……——ưm——chum——chuu——Ư」"
1238 = "「Aa.」"
1247 = "「Ưm ưư——ku——a——」"
1249 = "「Ưm——a——ưm ư——fu——ya——」"
1253 = "「Ừ. Từ đây trở đi, tôi cũng sẽ chuyển động.\\nEm, và tôi——tôi muốn hai chúng ta cùng nhau trao lời thề.」"
1256 = "「Ừ. Hình như đó là hiện tượng gọi là triều xuy.」"
1262 = "「Ưm ư! Ưm! A! Nfu!\\nNgài Soutetsu——Ngài Soutetsu~」"
1263 = "「Nyuuuuuuuuuuuu!」"
1264 = "「Nnnnuuuu~~~~~Ư!!!」"
1265 = "「Nn~~~~~~Ư!!!!」"
1274 = "「Tôi hiểu rồi. Tôi sẽ di chuyển dài và lớn hơn một chút nhé.」"
1277 = "「Vâng! Vâng!\\nEm, rất vui ạ—」"
1283 = "「Cứ thế này mà lên đỉnh đi, cho tôi xem dáng vẻ đáng yêu của em nào.」"
1290 = "「Bình thường, những thứ đi vào cô bé của Suzu……\\nchỉ có dương vật hoặc lưỡi của tôi thôi nhỉ.」"
1294 = "「Ngôi đền Akai Aso, một trong những biểu tượng của Ohitoyo,\\nvà Suzu trong trang phục Shiromuku. Thể hiện trực tiếp thông điệp muốn truyền tải, thật sự rất tuyệt.」"
1308 = "「Tôi không có cử động——sự cương cứng tự ý——\\nvui sướng——rồi run rẩy lên đấy chứ.」"
1314 = "「Tôi biết rồi, Suzu.\\nTôi cũng——đang trào dâng——đến giới hạn——rồi——Ư!」"
1316 = "「Tôi muốn cùng em kết lời thề duyên hai kiếp.\\nÔm em trong bộ Shiromuku này——khắc ghi thật sâu một lần nữa.」"
1320 = "「Tôi muốn em, mở rộng hai chân ra.」"
1322 = "「Tôi muốn. Em mở rộng. Hai chân ra.」"
1330 = "「Vì, vậy——Ư!!!!」"
1346 = "「Tất nhiên rồi.\\nĐó cũng là tâm nguyện của tôi.」"
1351 = "「Làm em xấu hổ đến vậy sao.\\nCó vẻ như mải mê quá nên tôi hơi quá đà rồi. Xin lỗi em.」"
1388 = "「Vậy thì, hãy cùng tận hưởng sự mới mẻ này.\\nCả tôi, và cả em——từ từ, chầm chậm thôi.」"
1391 = "「Thế thì tôi rất vui. Bởi vì,\\ndáng vẻ run rẩy vì xấu hổ của em, tôi cũng thấy vô cùng xinh đẹp và đáng yêu.」"
1398 = "「Phải không? Suzu.\\nSuzu đáng yêu của tôi, Suzu của riêng tôi.」"
1401 = "「Suzu! Zuzu! Suzu! Suzu!!!」"
1403 = "「Suzu? Cứ thế tập trung vào ngón tay tôi đi.」"
1423 = "「Chỗ, to lớn, thắt lại, của ngài Soutetsu,\\nchỗ đó——đang——a! Thúc vào, thúc vào.」"
1430 = "「~~~Ư」"
1435 = "「~~~~~~Ư」"
1437 = "「~~~~~~~~~~~~Ư!!!!!!」"
1641 = "Tôi hôn đi hôn lại lên mái tóc đen nhánh, chiếc mũi được cù nhẹ thật dễ chịu.\\nĐồng thời, tôi trượt ngón tay nhiều lần trên đường rãnh đáng yêu của khe hở."
1790 = "Đặc khu thiết lập hộ tịch và hôn nhân cho Railord.\\nBuổi chụp hình áp phích nhằm quảng bá cho sức hấp dẫn mới của thành phố Ohitoyo."
1810 = "Âm đạo đột ngột siết chặt lại——Ư!!??"
1869 = "Không phải chỗ tôi chỉ, mà là phần mở ra đóng lại ở tít sâu bên trong,\\ntôi ấn mạnh quy đầu vào thật sâu——"
1937 = "（Aa）"
1947 = "（Jupo——zubuuuuuuuu! Guri!!!）"
1998 = "（Kyuuuuuuuuuu!）"
1999 = "（Kyuuuuuuuuuuuu!!!!）"
2000 = "（Zubuuuuuuuuuuuu! Gotsu!!!）"
```

## Kết bài

File lr_ハチロクh1_今ひとたびの契り.txt.toml đã đọc đủ 358/358 dòng, sai 64 dòng (17,9%): xưng hô 22, gasp 18, romaji 9, đếm nguyên âm 7, thuật ngữ 3, sai nghĩa 3, khác 2. Lỗi tập trung ở thoại Soutetsu (30/82 dòng còn tự xưng "anh" với Hachiroku) và tiếng rên/gasp của Hachiroku — đúng với bản chất file H-scene. Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Thẻ %l: 0 lệch (file không có thẻ nào). Không còn っ thô trong VN. Lượt soát 2: 64/64, 0 bỏ, 0 sửa. Khối TOML 64 khóa đã parse-kiểm chứng, 0 sai lệch giá trị so với JSON.
