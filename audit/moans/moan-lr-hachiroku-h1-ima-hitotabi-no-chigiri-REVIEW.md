# Moan-fix REVIEW — lr_ハチロクh1_今ひとたびの契り.txt.toml (moan-lr-hachiroku-h1-ima-hitotabi-no-chigiri)

File H-scene "lời thề một lần nữa" của Hachiroku — sau buổi chụp hình Shiromuku ở đền Akai Aso. Nhân vật: monologue 162, ハチロク 114, 双鉄 82.

## 1. Xác minh file

- File: `lr_ハチロクh1_今ひとたびの契り.txt.toml` — route `01_Hachiroku`.
- Disk: `sources/toml2/translation_toml/01_Hachiroku/lr_#U30cf#U30c1#U30ed#U30afh1_#U4eca#U3072#U3068#U305f#U3073#U306e#U5951#U308a.txt.toml`
- TOML md5: `8f78fbd3c8217603ed8dc08dc2eeea3d` (khớp với md5 lúc audit; không có bản trùng — md5 xuất hiện 1 lần trong toàn bộ `sources/toml2/`).
- TOML: UTF-8 BOM + CRLF; `[selections]` rỗng.
- CSV3: 1 bộ duy nhất, 358 dòng, 0 key trùng, 0 VN trống; flat-match VN với TOML: 358/358 (ngoại trừ 181 dòng chênh ở `\n` literal bị TOML-2 làm phẳng thành khoảng trắng — CSV3 là chuẩn, như audit đã kiểm chứng).
- Đã đọc 358/358 dòng (CSV3 + TOML-2, đối chiếu từng dòng).
- Lưu ý: audit file này đã áp romaji fallback khá kỹ (34 dòng moan) và được parent kiểm chứng 22/11 ~02:05 — nên vòng moan-fix này là kiểm tra lại toàn bộ + bắt các dòng audit bỏ sót, không phải sửa hàng loạt. KHÔNG phải file `ハチロクh1_契り.txt.toml` (đã moan-fix trước, 1 dòng) — file này có tiền tố `lr_` và tựa đầy đủ 今ひとたびの契り.

## 2. Moan inventory — 180 dòng rên/SFX đã xét

- Thoại rên (ハチロク + 双鉄): 123 dòng — gasp/っ độc lập 77, fa/fu 14, ん+X 10, họ ひゃ/ひゅ/ひあ/きゃ 9, ちゅむ 4, はぁ/はあ 3, SFX trong ngoặc ở thoại 1, rên khác 5.
- SFX trong ngoặc （） ở độc thoại: 57 dòng (1931–2024).
- Tổng: 180 dòng rên/SFX. Đổi 9 dòng, giữ 171 dòng.
- Ngoài ra đã kiểm tra 41 dòng độc thoại văn xuôi có từ tượng thanh/っ trong câu (ぱっと, ぴくん, ぎゅうぎゅう, みちみち, くぱくぱ, どろどろ, ぼたぼた, ぐりゅり, じゅぶり, にゅるにゅる, ぴたり, こくり, ほうっと, ぽかぽか, ぶわぶわ, ふっと, じわり, がくがく, ヒクつく, ぶわり…) — đều đã diễn đúng theo nghĩa, giữ nguyên, không tính vào 180 dòng trên.
- Phân loại 9 dòng đổi: đếm nguyên âm 3 (1163, 1170, 1245), romaji 6 (1149, 1213, 1234, 1241, 1252, 2008). Toàn bộ 9 dòng đều là ハチロク, trừ 2008 (monologue).

## 3. Dòng sửa (9 dòng)

### 1149 — romaji, んうっ thiếu nguyên âm (ハチロク)

- JP: 「ひゃっ！？　ぁっ――あっ――んうっ！　ふっ……ぁ、\nじ、焦らさないでくださいましっ、んっ！　双鉄さまっ」
- TW: 「呀！？啊——啊——嗯嗚！呼……請、請不要挑弄我了，嗯！雙鐵少爺」
- VN cũ (TOML): 「Hya!? A——a——ưm! Fu…… a,\nx-xin ngài đừng trêu chọc em nữa, ưm! Ngài Soutetsu.」
- VN mới: 「Hya!? A——a——ưm ư! Fu…… a,\nx-xin ngài đừng trêu chọc em nữa, ưm! Ngài Soutetsu.」
- Lý do: JP んうっ: VN cũ "ưm" làm mất nguyên âm う (ư trong "ưm" là âm của ん). Theo mẫu "Ưm + X" đã chốt của file (1102, 1173, 1194, 1198, 1262 — audit đã áp): "ưm ư". Viết thường giữa dòng, khớp tiền lệ 1249 ("ưm ư" giữa dòng, audit đã áp).

### 1163 — đếm nguyên âm, はぁっ thiếu 1 a (ハチロク)

- JP: 「ふえっ！？　がまっ――がまんっ――ん、ふっ、\nはぁっ――はっ――ふっ、あんっ！　も、もうっ我慢っ」
- TW: 「咦！？忍耐——忍耐——嗯，呼，哈——哈——呼，嗯！忍、不住了」
- VN cũ (TOML): 「Fue!? Nhịn——nhịn——ưm, fu,\nha——ha——fu, an! Kh-không nhịn được nữa đâu.」
- VN mới: 「Fue!? Nhịn——nhịn——ưm, fu,\nhaa——ha——fu, an! Kh-không nhịn được nữa đâu.」
- Lý do: JP はぁっ = は + ぁ = 2 âm a; VN cũ "ha" chỉ 1 a. Tiền lệ audit 1174: はあっ → "Haa". Đoạn thứ hai はっ → "ha" giữ nguyên (1 a, đúng). "Kh-không" là nói lắp chữ Kh (không phải render っ — xem mục 5).

### 1170 — đếm nguyên âm, はぁ ×3 thiếu 1 a mỗi đoạn (ハチロク)

- JP: 「はぁ――はぁ――はぁ――（ごくっ）\nそうてつ、さま――だんな、さま」
- TW: 「哈——哈——哈——（咽）雙鐵、少爺——夫、君」
- VN cũ (TOML): 「Ha——ha——ha——(ực)\nSou, tetsu, sama——phu, quân.」
- VN mới: 「Haa——haa——haa——(ực)\nSou, tetsu, sama——phu, quân.」
- Lý do: Mỗi はぁ = 2 âm a; VN cũ mỗi đoạn chỉ 1 a. Cùng lỗi như 1163, cùng tiền lệ 1174 (はあっ → "Haa"). （ごくっ） → "(ực)" giữ nguyên.

### 1213 — romaji, ちゅむっ ×2 thiếu nguyên âm cuối (ハチロク)

- JP: 「ん……ちゅむっ――ちゅずっ――じゅっ――（こくっ）\n――ちゅむっ――れるっ――れろっ――ちゅりゅっ」
- TW: 「唔……啾唔——啾嘶——啾——（咽）啾唔——唔——唔——啾嚕」
- VN cũ (TOML): 「Ưm…… chum——chuzu——ju——(ực)\n——chum——reru——rero——churyu」
- VN mới: 「Ưm…… chumu——chuzu——ju——(ực)\n——chumu——reru——rero——churyu」
- Lý do: JP ちゅむっ = chu-mu (2 âm u); VN cũ "chum" rớt nguyên âm của む. Tiền lệ: audit file h1_契り 2147 ちゅむっ → "Chumu" (parent-verified); các moan-fix trước đổi "chu"/"chụt" → "chumu" cho ちゅむっ (h9 1358, paulette-h4 1576/1579, paulette-h3 914/942/946/970). Quy ước của chính file này cũng giữ nguyên âm cuối trước っ: じゅっ → "ju", れるっ → "reru", ちゅうっ → "chuu", くいっ → "kui". Cả 2 chỗ ちゅむっ trong dòng đều sửa.

### 1234 — romaji, ちゅむっ thiếu nguyên âm cuối (ハチロク) — THAY THẾ fix audit

- JP: 「あ……――んっ――ちゅむっ――ちゅうっ――っ」
- TW: 「啊……嗯——啾——啾——」
- VN cũ (TOML): 「A……——ưm——chum——chuu——」
- VN mới: 「A……——ưm——chumu——chuu——Ư」
- Lý do: ちゅむっ → "chumu" (như 1213). Fix này THAY THẾ fix audit cùng key 1234 ở đợt thống nhất — khác fix audit CHỈ ở "chum"→"chumu"; giữ nguyên "——Ư" cuối dòng của audit (gasp sweep lost-gasp-trailing, đã đúng). Đã kiểm chứng cơ học bằng diff: moan-fix vs audit-fix chỉ khác 1 chuỗi "chum"→"chumu".

### 1241 — romaji, ちゅむっ thiếu nguyên âm cuối (ハチロク)

- JP: 「あむっ――ふっ――んっ――れうっ――りゅっ――\nちゅむっ――ちゅうっ――じゅりゅっ――」
- TW: 「啊嗚……呼……唔……啾……啾唔——啾——啾嚕——」
- VN cũ (TOML): 「Amu——fu——ưm——reu——ryu——\nChum——chuu——juryu——」
- VN mới: 「Amu——fu——ưm——reu——ryu——\nChumu——chuu——juryu——」
- Lý do: ちゅむっ → "Chumu" (như 1213; viết hoa đầu dòng). Các âm còn lại đã đúng: あむっ → "Amu", れうっ → "reu", りゅっ → "ryu", ちゅうっ → "chuu", じゅりゅっ → "juryu".

### 1245 — đếm nguyên âm, はあっ thiếu 1 a (ハチロク)

- JP: 「あっ！　あっ！　あっ！　あっ！　あっ　あっ！\nあっ！　あっ！　んっ！　はあっ！　んっ！　ふっ！」
- TW: 「啊！啊！啊！啊！啊！啊！啊！啊！嗯！哈！嗯！呼！」
- VN cũ (TOML): 「A! A! A! A! A! A!\nA! A! Ưm! Ha! Ưm! Fu!」
- VN mới: 「A! A! A! A! A! A!\nA! A! Ưm! Haa! Ưm! Fu!」
- Lý do: JP はあっ = は + あ = 2 âm a; VN cũ "Ha!" chỉ 1 a. Tiền lệ audit 1174 (はあっ → "Haa") và 1238 (ああ → "Aa"). Các あっ → "A" và んっ → "Ưm" đã đúng.

### 1252 — romaji, ちゅむっ thiếu nguyên âm cuối (ハチロク)

- JP: 「ん……ちゅっ――ん……ふ……ぁ……\nふっ――ちゅむっ――ちゅうっ――れるっ」
- TW: 「嗯……啾……呼……啊……呼——啾唔——啾……唔」
- VN cũ (TOML): 「Ưm…… chụt——ưm…… fu…… a……\nFu——chum——chuu——reru」
- VN mới: 「Ưm…… chụt——ưm…… fu…… a……\nFu——chumu——chuu——reru」
- Lý do: ちゅむっ → "chumu" (như 1213). ちゅっ → "chụt" giữ nguyên (đã diễn đúng theo ranh giới gasp: ちゅっ → "Chụt", âm đã diễn).

### 2008 — romaji, ちゅむっ thiếu nguyên âm cuối (monologue)

- JP: （ちゅむっ――ぷりゅっ）
- TW: （輕搖柔擺）
- VN cũ (TOML): （Chum——puryu）
- VN mới: （Chumu——puryu）
- Lý do: ちゅむっ → "Chumu" (như 1213). ぷりゅっ → "puryu" đã đúng.

## 4. Đồng ý với audit — 34/34 dòng moan của audit kiểm chứng lại là đúng

Audit file này đã sửa 34 dòng moan (romaji 8 + gasp 18 + đếm nguyên âm 8). Kiểm chứng lại từng dòng bằng đếm cơ học theo mora, đồng ý 34/34 — chỉ thay thế 1234 (mục 3, khác audit đúng 1 chuỗi "chum"→"chumu"):

- Romaji ん+X (đã đúng, giữ nguyên giá trị audit): 1102 んぅっ → "ưm ư", 1173 んうっ → "Ưm ư", 1194 んうっ → "Ưm ư", 1198 んぅっ → "Ưm ư", 1247 んぅぅ → "Ưm ưư" (2 ư cho 2 ぅ), 1249 んうっっ → "ưm ư" (giữ chữ thường giữa dòng), 1262 んぅっ → "Ưm ư" + んっ → "Ưm".
- Romaji họ ひゃ/きゃ (đã đúng): 1145 きゃっ → "Kya!?" (quy tắc 3b). Không còn dòng "Á" nào cho họ ひゃ/ひゅ/ひあ/きゃ trong file — đã kiểm chứng cơ học (chỉ còn "Á" ở 1145 cũ + 2 "Ánh mắt" trong văn xuôi).
- Đếm nguyên âm audit đã đúng (đếm cơ học lại theo mora): 1142 ひゃぅ×13+う = 14 u → "Hyauuuuuuuuuuuuuu" (14 u; sweep ghi 16 u là sai, audit đã sửa); 1174 はあっ ×4 → "Haa" (2 a); 1238 ああ → "Aa"; 1263 んゅう×11 = 12 u → "Nyuuuuuuuuuuuu" (12 u); 1264 ん×4+ぅ×4 → "Nnnnuuuu" (4 n + 4 u; sweep ghi 6 n + 5 u là sai, audit đã sửa); 1937 （ああ） → "（Aa）"; 1947 ずぶう×7 = 9 u → "zubuuuuuuuu" (9 u); 1998 きゅう×9 = 10 u → "Kyuuuuuuuuuu" (10 u); 1999 きゅう×11 = 12 u → "Kyuuuuuuuuuuuu" (12 u); 2000 ずぶう×11 = 13 u → "Zubuuuuuuuuuuuu" (13 u) + ごつっ → "Gotsu".
- Gasp Ư (sweep/audit, KHÔNG đụng lại): 1152, 1156 (sweep bỏ sót, audit thêm đúng), 1195, 1216, 1219, 1220, 1221, 1222, 1223, 1234 (giữ Ư, chỉ sửa "chum"), 1265, 1330, 1430, 1435, 1437, 1810 + 1314 (needs-file-audit, xem cờ F1).
- Fa/fu toàn file đã là romaji "Fua/Fuaa/Fuya/Fue" — không còn "phà"/"phùa"/"phuê" nào (kiểm chứng cơ học, 0 dòng).

## 5. Ghi chú các dòng rên giữ nguyên (đáng chú ý)

- Hệ SFX trong ngoặc （） diễn theo nghĩa hành động — GIỮ NGUYÊN HỆ NÀY (theo quyết định của moan-fix file h1_契り, viện tiền lệ moan-fix h8): 1934 （とさっ）→ "Phịch", 1935/1984 （ぴちゅっ）→ "Lép nhép", 1944/1983 （ぴゅっ）→ "Phụt", 1964 （がしっ）→ "Chộp lấy", 1966 （ぴゅる――じゅわっ）→ "Phụt——ào", 1973 （つぬっ）→ "Sụt", 1976/2012 しにゅう → "xâm——nhập", 1978 （とん――とん――とん――とん）→ "Cốc——cốc——cốc——cốc", 1990/2003 （くっ）→ "Hự", 1994 （さすっ）→ "Vuốt ve", 1995 （さわっ、さすっ）→ "Sờ nhẹ, vuốt ve", 2004 （くちっ）→ "Nhóp nhép", 2007 （ぴとっ）→ "Chạm nhẹ", 2010 （とんっ）→ "Cốc", 2013 （くにっ）→ "Chạm nhẹ". Các SFX romaji còn lại trong （） đã xét từng dòng, đếm nguyên âm đúng (kiểm chứng cơ học toàn khối: u/a khớp JP, trừ các dòng audit đã sửa ở mục 4).
- 1965 （しにゅううううううううううううっっっっ）→ "Xâm nhậpppppppppppppppppppppppppppp" — TRẢ LỜI CỜ CỦA AUDIT: GIỮ NGUYÊN. しにゅう là SFX hành động (chuyển động ra/vào — TW 抽回), file này diễn "xâm nhập" nhất quán (1976, 1982); chuỗi "p" kéo dài (28 chữ p cho 12 âm u của JP) là phong cách kéo chữ nghệ thuật của chính file, không áp công thức đếm nguyên âm — theo tiền lệ moan-fix h8 ("siết chặttttt", "Phập phập phập!"). Không đổi sang romaji "Shinyuuuuuuuuuuuu" vì dòng này thuộc hệ diễn-nghĩa, đổi một mình nó sẽ phá vỡ tính nhất quán của dòng (một dòng = một cách diễn).
- 1982 （しゅるうっ――しにゅうっ――ちゅむうっ――）→ "Sột soạt——xâm nhập——chụt——" — GIỮ NGUYÊN, cùng lý do hệ diễn-nghĩa: cả dòng diễn bằng tiếng Việt, ちゅむうっ → "chụt" là cách diễn tiếng hôn/mút trong hệ này. Khác với tiền lệ h1_契り 2147 ("Chụt"→"Chumu") vì 2147 nằm trong ngữ cảnh romaji, còn đây nằm trong ngữ cảnh diễn-nghĩa. Ghi nhận để đợt thống nhất cân nhắc nếu muốn chuẩn hóa (xem cờ F3).
- 1278 んうっ―― → "N u——" — GIỮ NGUYÊN, cố ý: kiểu nói lắp tách chữ cái của chính dòng này ("n a!" cho んぁっ! ở cùng dòng; audit đã ghi nhận và giữ). Không áp mẫu "Ưm ư" ở đây vì sẽ phá vỡ nét nói lắp của dòng.
- 1992 （じゅぶりゅうううううううっっっっ！）→ "Juburyuuuuuuuu!" — GIỮ NGUYÊN: đếm chính xác theo mora: じゅ(1) + ぶ(1) + りゅ(1) + う×7 = 10 âm u; VN có 10 chữ u. (Lần đếm nháp đầu tiên đếm nhầm chuỗi う là 6 — đã bắt bằng đếm cơ học ký tự, không sửa.)
- 1139 ひゃああああっっ → "Hyaaaaa" (5 a: ひゃ 1 + あ×4, đúng); 1143 ひゃう → "hyau" (đúng); 1147 ひゃっっ → "Hya!?" (dấu !? diễn っ kép); 1154 ぷぁ → "Pua"; 1176 あひゅうっ → "ahyuu" (2 u) + あひゅいのっ → "nóng quá" (あひゅい là cách nói ngọng của あつい "nóng" — TW 好熱 xác nhận, diễn theo nghĩa là đúng); 1185 はひゅんっ → "Hahyun"; 1428 （じゅうううううっ）→ "(Juuuuuu)" (6 u, đúng).
- 1434 ～～～～～～っ！！！！――ぁ――はっ――あっ！ → "~~~~~~!!!! ——a——ha——a!" — GIỮ NGUYÊN, không thêm Ư: っ ở đây ở GIỮA dòng (còn moan tiếp sau), không phải cuối dòng như 1195/1430/1435/1437 (sweep lost-gasp-trailing chỉ áp cho っ cuối dòng); độ ngắt được diễn bằng "!!!!". Khớp ranh giới gasp đã chốt và kiểm chứng 0-bỏ-sót của audit.
- Các っ cuối dòng gắn từ có âm đã diễn — GIỮ NGUYÊN, không thêm Ư (khớp sweep + audit): 1158 ふぁっ → "fua.", 1160 ふあっ → "Fua.", 1186 はうぅっ → "Hauu.", 1199 ふああっ！！！ → "Fuaa!!!", 1242 はうっ → "Hau." — âm đã diễn đầy đủ, độ ngắt được diễn bằng dấu câu. Sweep không liệt kê các dòng này (chỉ liệt kê っ đứng một mình, sau ~~~~/――, hoặc đầu dòng) và audit đã quét cơ học xác nhận 0 bỏ sót.
- Cười うふふっ → "Ufufu" (1269, 1270) — là tiếng cười, không phải rên. ふっ → "fu" trong chuỗi rên (1153, 1194, 1245, 1249, 1252) giữ nguyên theo đa số tiền lệ; chỉ ふあ/ふぁ mới bắt buộc romaji.
- ふぇ → romaji "Fue" (1163, 1202) — thán từ ngạc nhiên, giữ nguyên (tiền lệ moan-fix: "Fue" nằm đầu chuỗi rên; khác "Hả" cho えっ độc lập ở 1162/1164).
- Họ や → "ya"/"Ya"/"Nhá" giữ nguyên: 1150 やっ → "Ya", 1232/1237 や―― → "ya", 1377 や…… → "Không……." (diễn theo nghĩa "không", audit đã giữ).
- Không có dòng "Kh" nào cho glottal-stop っ trong file (chỉ có "Kh-không" nói lắp ở 1163) — không đổi dòng "Kh" nào sang Ư. Không dòng gasp Ư nào bị xem lại.

## 6. Kiểm chứng sweep gasp

- Sweep có 18 mục cho ĐÚNG file này (đọc trực tiếp `sweep-raw-gasp-wrong.json`, lọc theo `file`): 1142, 1152, 1195, 1216, 1219, 1220, 1221, 1222, 1223, 1234, 1264, 1265, 1330, 1430, 1435, 1437, 1810 (17 mục có fix — audit đã áp, kiểm chứng lại đúng; riêng 1142 và 1264 audit đã sửa lại số đếm của sweep: 1142 sweep 16 u → audit 14 u đúng; 1264 sweep 6 n + 5 u → audit 4 n + 4 u đúng) + 1314 needs-file-audit (audit đã xử lý: đại từ + gasp "rồi——Ư!", xem cờ F1).
- 1 gasp sweep bỏ sót audit đã thêm (1156 っ！！ cuối dòng 1) — kiểm chứng lại đúng.
- Không có dòng "Kh" nào bị đổi sang Ư. Không có dòng gasp Ư nào bị xem lại. Không còn っ thô nào trong VN (kiểm chứng cơ học: 0 dòng).

## 7. Cờ cho Hieu / cho đợt thống nhất

### F1 — 1314 cờ CHO HIEU (audit đã cờ, giữ nguyên — không tự quyết)

- JP: 「わかっている、すず。\n僕も――こみあげ――きって――いるっ――っ！」
- Fix audit (giữ nguyên ở đây): 「Tôi biết rồi, Suzu.\nTôi cũng——đang trào dâng——đến giới hạn——rồi——Ư!」
- Audit phán đoán っ cuối sau —— là gasp độc lập → thêm "——Ư" (sweep ghi "needs-file-audit" rồi chuyển cho audit quyết). Nếu Hieu thấy "rồi——Ư!" nghe gượng thì bỏ Ư, giữ "rồi!". Vòng moan-fix KHÔNG quyết thay Hieu.

### F2 — 1234 lưu ý hợp nhất (không phải cờ)

- Fix moan ở đây THAY THẾ fix audit cùng key ở đợt thống nhất (áp giá trị moan, không áp giá trị audit, cho key 1234). Khác fix audit chỉ ở 1 chuỗi "chum"→"chumu" (mục 3).

### F3 — 1982 ghi nhận (không phải cờ)

- ちゅむうっ → "chụt" được giữ theo hệ diễn-nghĩa của file (mục 5), trong khi tiền lệ h1_契り 2147 đổi "Chụt"→"Chumu" cho ちゅむっ trong ngữ cảnh romaji. Nếu đợt thống nhất muốn chuẩn hóa ちゅむ → "Chumu" toàn dự án thì 1982 (và các dòng "chụt" cho ちゅむ trong hệ diễn-nghĩa) cần quyết một lần.

### F4 — そうてつさま không nhất quán (audit đã cờ, giữ nguyên)

- そうてつさま hiragana có lúc romaji ("Sou, tetsu, sama" 1139/1417) có lúc "Ngài Soutetsu" (1190/1421); さまぁっ có lúc "~" (1178) có lúc mất hẳn (1190/1421). Ứng viên cho đợt thống nhất, không thuộc phạm vi moan.

## 8. Lượt soát 2 (second pass)

- Đọc lại toàn bộ 9 giá trị fix so với JP + TW sau lượt đầu, kèm đếm cơ học lại từng dòng đếm nguyên âm (1163: はぁ = 2 a; 1170: はぁ ×3 = 2 a mỗi đoạn; 1245: はあ = 2 a; 1213/1234/1241/1252/2008: ちゅむ = 2 u; 1149: んう = ưm + ư) và diff cơ học fix-vs-old-VN (9/9 chỉ khác đúng chỗ cần sửa, toàn là chèn thêm — 0 xóa, 0 thay thế ngoài mục tiêu).
- Tổng: 9 / tái kiểm chứng: 9 / bỏ: 0 / sửa: 0.
- Trong lượt soát 2 đã bắt và loại 1 lỗi đếm nháp: lần đếm đầu đếm nhầm chuỗi う ở 1992 là 6 (định sửa "Juburyuuuuuuuu" → bớt 1 u); đếm lại bằng ký tự cho thấy JP có 7 う = 10 âm u, khớp đúng VN 10 u — KHÔNG sửa 1992.

## 9. Khối TOML (parse-verified bằng tomllib: 9 khóa, 0 sai lệch giá trị so với wrong.json)

```toml
[script]
"1149" = "「Hya!? A——a——ưm ư! Fu…… a,\\nx-xin ngài đừng trêu chọc em nữa, ưm! Ngài Soutetsu.」"
"1163" = "「Fue!? Nhịn——nhịn——ưm, fu,\\nhaa——ha——fu, an! Kh-không nhịn được nữa đâu.」"
"1170" = "「Haa——haa——haa——(ực)\\nSou, tetsu, sama——phu, quân.」"
"1213" = "「Ưm…… chumu——chuzu——ju——(ực)\\n——chumu——reru——rero——churyu」"
"1234" = "「A……——ưm——chumu——chuu——Ư」"
"1241" = "「Amu——fu——ưm——reu——ryu——\\nChumu——chuu——juryu——」"
"1245" = "「A! A! A! A! A! A!\\nA! A! Ưm! Haa! Ưm! Fu!」"
"1252" = "「Ưm…… chụt——ưm…… fu…… a……\\nFu——chumu——chuu——reru」"
"2008" = "（Chumu——puryu）"
```

Lưu ý: trong khối TOML trên, `\\n` là ký tự xuống dòng đã escape (giá trị thực trong JSON/TOML là `\n` literal như CSV3).

## Kết bài

File lr_ハチロクh1_今ひとたびの契り: đã đọc 358/358 dòng, xét 180 dòng rên/SFX, đổi 9 dòng (đếm nguyên âm 3: 1163, 1170, 1245 — はぁ/はあ thiếu 1 a; romaji 6: 1149 んうっ thiếu ư, 1213/1234/1241/1252/2008 ちゅむっ → "chumu") — audit file này đã áp romaji fallback khá kỹ từ trước (34/34 dòng moan của audit kiểm chứng lại là đúng, chỉ thay thế 1234). Hệ SFX trong ngoặc diễn theo nghĩa hành động được GIỮ NGUYÊN theo tiền lệ moan-fix h8/h1_契り (trả lời cờ audit ở 1965: giữ "Xâm nhậpppp..."). 4 cờ/ghi nhận: F1 1314 "rồi——Ư!" chờ Hieu, F2 1234 thay thế fix audit, F3 1982 "chụt" cho ちゅむうっ, F4 そうてつさま không nhất quán. Không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào.
