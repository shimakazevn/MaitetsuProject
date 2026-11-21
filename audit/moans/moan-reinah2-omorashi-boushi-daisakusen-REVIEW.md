# Moan-fix REVIEW — れいなh2_おもらし防止大作戦.txt.toml (moan-reinah2-omorashi-boushi-daisakusen)

Route 04_Reina. H-scene "đặc huấn nhịn tè dầm" (Reina + Soutetsu).

## §1. Kiểm chứng file

- TOML: `sources/toml2/translation_toml/04_Reina/#U308c#U3044#U306ah2_#U304a#U3082#U3089#U3057#U9632#U6b62#U5927#U4f5c#U6226.txt.toml`
- TOML md5: `141739546028af97fdbac1c3ffe9ab6e` (UTF-8 BOM + CRLF, 589 CRLF, 0 LF lẻ). `[script]` 284 khóa. Không có bản trùng (11 nhóm trùng của dự án không chứa file này).
- CSV3: 1 set duy nhất, 284 dòng, 0 trùng khóa, khóa 767–1771. VN khớp TOML 284/284 sau khi chuẩn hoá `\n`→khoảng trắng (TOML-2 flatten `\n` thành khoảng trắng như mọi file; CSV3 là bản chính).
- Audit đã gộp: 23 dòng sai (ROUTE-AUDIT.md). Phân loại audit: gasp 4 (1031, 1070, 1071, 1215 — cả 4 từ sweep), fa/fu 14, SFX cười 2 (1104, 1108), bịa thêm 2 (1118, 1628), sai nghĩa 1 (1465). TOML trên đĩa vẫn giữ VN gốc (fix audit chưa áp vào TOML — đúng mô hình amendment); bản moan này xây trên **giá trị fix của audit** ở 14 key trùng, và trên VN CSV3 ở 23 key mới.
- Sweep: 4 mục cho file, đã kiểm chứng trực tiếp — cả 4 đều là fix gasp Ư của audit (1031, 1070, 1071, 1215), đã nhận. Đợt moan này KHÔNG đụng dòng gasp Ư nào (quy tắc khóa: không xem lại).
- Quét gasp lại ở đợt moan này (mọi dòng JP kết bằng っ trước `」`): không còn gasp nào sót — các っ còn lại đều đã diễn (はっ→"Ha", �んっ→"ưm", ふっ→"phù", ごくっ→"Ực", ちゅっ→"chụt", くっ→"Ku" sau fix này, んうっ→"ưm" theo quy ước file) hoặc là っ nhấn mạnh gắn từ nội dung (1101 よいしょっ→"hây dô", 1186 はっっっ→"Ha", 1210 もっ→"cũng", 1065 くてっ→"quá") — giữ nguyên theo quy tắc sweep. Ngoại lệ duy nhất: 1026 やぁっ — xem cờ F1.

## §2. Kho rên (moan inventory)

- Đã đọc 284/284 dòng; xét 196 dòng ứng viên rên/SFX (193 lọc máy theo JP chứa っ/tiểu kana/（/ー + 3 dòng VN-only 1095/1098/1100 — ふむ/うむ→"Hừm"/"Ưm"); sửa 37, giữ 159.
- Phân loại 37 dòng sửa:

| Nhóm | Số dòng | Key |
|---|---|---|
| fa/fu → romaji (ふぁ→Fa, ふあ→Fua, ふぇ→Fue, ぷあ→Pua, ぷは→Puha) | 13 | 1001, 1027, 1036, 1052, 1065, 1081, 1114, 1174, 1180, 1182, 1183, 1184, 1185 |
| họ ひゃ/ひゅ/ひあ → romaji (Hyau/Hia/Nhyu/Hyafu/Hyapu/Uhyu/Ahyu) | 11 | 1042, 1045, 1046, 1047, 1049, 1056, 1057, 1061, 1062, 1068, 1210 |
| romaji mất phụ âm mora (くっ→Ku, んくっ→Nku, んぷっ→Npu, んぶっ→Nbu, んきゅっ→Ưm kyu, きゅふうっ→Kyufuu, ふっ→Phù) | 8 | 1003, 1030, 1053, 1064, 1077, 1087, 1088, 1090 |
| đếm nguyên âm (vowel formula) | 5 | 779, 1002, 1040, 1089, 1216 |

- 14/37 key trùng audit — kiểm chứng bằng máy: giá trị moan chỉ khác fix audit ở đúng token rên (xem chi tiết từng dòng). 23 key mới (audit bỏ sót).
- 9 key audit KHÔNG đụng ở đợt moan: gasp Ư 1031/1070/1071/1215 (khóa, không xem lại), cười 1104/1108 (fix audit "Fufu~"/"Ufufu~" đã đúng), phi-moan 1118/1465/1628.

## §3. Từng dòng sửa (37 dòng)

### 779 [双鉄H] — đếm nguyên âm (ふぅ)
- JP: `「――ん……ふぅ。\n見事だ。これで、特訓は大成功だな」`
- TW: `「……嗯。很好，這樣特訓就完美成功了」`
- VN cũ: `「——Ưm……phù.\nTuyệt lắm. Vậy là, đặc huấn đã thành công mỹ mãn rồi.」`
- Mới: `「——Ưm……phùu.\nTuyệt lắm. Vậy là, đặc huấn đã thành công mỹ mãn rồi.」`
- Lý do: ふぅ = ふ + ぅ = 2 nguyên âm u (công thức 1 + 1); VN cũ "phù" chỉ 1 u — thiếu 1. Tiền lệ paulette-h6 (ふだっ→"Phùu"), lr-nagifukami (ふぅ→"fuu"), hachiroku-h8 (ふぅ→"phuu" giữ đúng). Xem cờ F2 (mâu thuẫn với tiền lệ paulette-h8 giữ "phù" theo quy ước file).

### 1001 [れいな] — fa/fu + đếm ん + mất phụ âm (ya)
- JP: `「ひゃっ――あっ――んっ――んんっ――ふあっ――\nやっ――したっ――ぬりゅう、って――ふあ――あっ」`
- TW: `「呀啊……啊、嗯……啊嗯……蛤啊……啊嗯……下面……變濕了……啊啊啊」`
- VN cũ: `「Hya——a——ưm——ưm——ha——\nÁ——bên dưới——nhầy nhụa, rồi——ha——a」`
- Mới: `「Hya——a——ưm——ưmm——Fua——\nYa——bên dưới——nhầy nhụa, rồi——Fua——a」`
- Lý do: xây trên fix audit (phùa ×2, "Á"). んんっ (2 mora ん) → "ưmm" (tiền lệ reinah3 1061, mikuro); ふあっ/ふあ → "Fua" (romaji fallback, thay "phùa" của audit); やっ → "Ya" ("Á" mất hẳn y — tiền lệ ポーレットh3 "'Á' cho きゃっ/ひゃっ/やっ" là lỗi mất phụ âm). ひゃっ→"Hya", あっ→"a", んっ→"ưm" đã đúng — giữ.

### 1002 [れいな] — đếm nguyên âm
- JP: `「ひゃあああんっ」`
- TW: `「呀啊啊啊啊」`
- VN cũ: `「Hyaaaaaan」`
- Mới: `「Hyaaaan」`
- Lý do: JP ひゃ + あ×3 = 4 nguyên âm a; VN cũ 6 a — thừa 2. Đếm lại độc lập bằng máy (codepoint). GHI CHÚ: audit §4 ghi giữ "Hyaaaaaan" (lý do: dạng romaji nhất quán toàn dự án) — quyết giữ đó nói về KIỂU diễn (romaji), không đếm số lượng; đợt moan sửa số lượng theo công thức đếm đã khóa. Xem cờ F6.

### 1003 [双鉄H] — romaji mất phụ âm mora
- JP: `「くっ――ふっ――」`
- TW: `「呃啊……」`
- VN cũ: `「Ư——phù——」`
- Mới: `「Ku——phù——」`
- Lý do: くっ → "Ku" ("Ư" mất hẳn k — tiền lệ reinah3 1043/1045, ポーレットh3 "'Ư' cho くっ"). ふっ→"phù" giữ (quy ước file).

### 1027 [れいな] — fa/fu
- JP: `「はっ――んっ――ふあッ――んっ――\nもっと――もっと――ね、そうてつ――さぁ、んっ――」`
- TW: `「哈嗯……啊嗯……繼續……繼續嘛，雙鐵先生……」`
- VN cũ: `「Ha——ưm——ha——ưm——\nNữa đi——nữa đi——nha, anh Soutetsu——ưm——」`
- Mới: `「Ha——ưm——Fua——ưm——\nNữa đi——nữa đi——nha, anh Soutetsu——ưm——」`
- Lý do: xây trên fix audit "phùa" → "Fua" (romaji fallback). Các token khác đã đúng.

### 1030 [双鉄H] — romaji mất phụ âm mora
- JP: `「んくっ――くっ――くっ」`
- TW: `「唔……」`
- VN cũ: `「Ưm——ư——ư」`
- Mới: `「Nku——Ku——Ku」`
- Lý do: んくっ → "Nku", くっ → "Ku" ×2 (tiền lệ reinah3: んくっ→"Nku", くっ→"Ku" đã đúng trong file đó). "Ưm——ư——ư" diễn được 3 tiếng rên nhưng làm mất phụ âm k ở cả 3 token. Xem cờ F3 (tiền lệ ngược nagih2 2501 giữ んくっ→"Ư" trong chuỗi nuốt — chuỗi này là tiếng gầm của Soutetsu, không phải nuốt).

### 1036 [れいな] — fa/fu
- JP: `「あ――ふあっ――」`
- TW: `「啊……蛤啊……」`
- VN cũ: `「A——ha——」`
- Mới: `「A——Fua——」`
- Lý do: xây trên fix audit "phùa" → "Fua".

### 1040 [れいな] — đếm nguyên âm (sai nguyên âm)
- JP: `「ひゃうううううっ！！？」`
- TW: `「啊啊啊啊啊！！？」`
- VN cũ: `「Hyaaaaaa!!?」`
- Mới: `「Hyauuuuu!!?」`
- Lý do: JP = ひゃ (1 a) + う×5 (5 u); VN cũ 6 a, 0 u — sai hẳn nguyên âm (u thành a). Đếm lại độc lập bằng máy. っ cuối được "!!?" diễn cắt ngang.

### 1042 [れいな] — họ ひゃ/ひゅ
- JP: `「ひゃうっ！　あっ！　いきっ――なりっ――あっ！\nんひゅっ！　ひゃっ――おなか――ささっ――って――」`
- TW: `「啊啊啊啊！這麼突然……啊嗯！啊嗯！呀啊！插到肚子裡面了……」`
- VN cũ: `「Hya! A! Đột——nhiên——a!\nƯm! Hya——bụng——bị đâm——rồi——」`
- Mới: `「Hyau! A! Đột——nhiên——a!\nNhyu! Hya——bụng——bị đâm——rồi——」`
- Lý do: ひゃうっ → "Hyau" (thiếu mora う trong "Hya" — tiền lệ nagih2, paulette-h8, kisaki-h3); んひゅっ → "Nhyu" (quy tắc 3b: んひゅ→"Nhyu/Nhyun"; "Ưm" mất hẳn hyu). GHI CHÚ: audit §4 ghi giữ んひゅっ→"Ưm!" (nén nhất quán trong file) — quyết đó ra đời TRƯỚC quy tắc 3b (21/11 ~11:55) và mâu thuẫn trực tiếp với nó; đợt moan áp quy tắc 3b. Xem cờ F6.

### 1045 [れいな] — họ ひゃ (mất ぷ)
- JP: `「ひゃぷっ――んっ――あっ？　あ――んうっっ」`
- TW: `「啊嗯……啊……啊嗯！」`
- VN cũ: `「Hya——ưm——a? A——ưm」`
- Mới: `「Hyapu——ưm——a? A——ưm」`
- Lý do: ひゃぷっ → "Hyapu" ("Hya" làm mất ぷ — tiền lệ nagifukamih1 1226 ひゃぷっ→"Hyapu"). んうっっ→"ưm" giữ (tiền lệ fukamih1 964).

### 1046 [れいな] — họ ひゅ + đếm nguyên âm (ふう)
- JP: `「んひゅ――あっ――おくちっ――んっ――ふうっ」`
- TW: `「啊嗯……啊……嘴巴……」`
- VN cũ: `「Ưm——a——miệng——ưm——phù」`
- Mới: `「Nhyu——a——miệng——ưm——phùu」`
- Lý do: んひゅ → "Nhyu" (quy tắc 3b); ふうっ = 2 u → "phùu" (cũ 1 u). Xem cờ F2/F6.

### 1047 [れいな] — họ ひゃ (mất ふ, mất う)
- JP: `「ひゃふっ――あっ――おくっ――いちばん――\nおな、か――いちばん――ぐりぐり、され――ひゃう！」`
- TW: `「啊嗯……啊……肚子裡面……最裡面……被插來插去的！」`
- VN cũ: `「Hya——a——sâu bên trong——tận cùng——\nbụng——tận cùng——bị ngoáy, ngoáy——hya!」`
- Mới: `「Hyafu——a——sâu bên trong——tận cùng——\nbụng——tận cùng——bị ngoáy, ngoáy——Hyau!」`
- Lý do: ひゃふっ → "Hyafu" ("Hya" mất ふ); ひゃう → "Hyau" ("hya" mất う; viết hoa "Hyau!" theo quy ước romaji viết hoa cả khi ở giữa dòng — tiền lệ reinah3 1014 "——Fa", reinah4 1999 "Fa" giữa dòng). おくっ→"sâu bên trong" là diễn nghĩa, audit chấp nhận — giữ.

### 1049 [れいな] — họ ひゃ
- JP: `「ひゃうっ――あっ――べろっ――べろぉっ――んっ、\nそうてつ、さんの、べろ――べろ――がぁっ」`
- TW: `「啊嗯……啊……舔來舔去的……雙鐵先生……在裡面……舔來舔去……」`
- VN cũ: `「Hya——a——liếm——liếm——ưm,\nlưỡi——của anh——Soutetsu——lưỡi——」`
- Mới: `「Hyau——a——liếm——liếm——ưm,\nlưỡi——của anh——Soutetsu——lưỡi——」`
- Lý do: ひゃうっ → "Hyau" (thiếu mora う).

### 1052 [れいな] — fa/fu
- JP: `「ひゃん――んっ――わきばら――くすぐったいで――\nふあっ――んっ！」`
- TW: `「啊嗯……嗯……側腹好癢哦……蛤啊……嗯！」`
- VN cũ: `「Hyan——ưm——mạn sườn——nhột quá——\nHa——ưm!」`
- Mới: `「Hyan——ưm——mạn sườn——nhột quá——\nFua——ưm!」`
- Lý do: xây trên fix audit "Phùa" → "Fua". ひゃんっ→"Hyan" đã đúng — giữ.

### 1053 [れいな] — romaji (んきゅっ)
- JP: `「んきゅっ――ふっ――あっ――れいな――れいなぁ――\nおしっこの、あな――つんつん、ぺろぺろ――され、て」`
- TW: `「啊嗯……蛤啊……啊……玲奈……玲奈……尿尿的洞……被舔著……」`
- VN cũ: `「Ưm——phù——a——Reina——Reina——\nlỗ tiểu——bị chọc chọc, liếm liếm——rồi」`
- Mới: `「Ưm kyu——phù——a——Reina——Reina——\nlỗ tiểu——bị chọc chọc, liếm liếm——rồi」`
- Lý do: んきゅっ → "Ưm kyu" ("Ưm" mất hẳn きゅ — tiền lệ kisaki-h3 2278 んきゅっ→"Ưm kyu!?", reinah3 1095 んきゅううっ→"Ưm kyuu!": ん→"Ưm" + phần còn lại romaji).

### 1056 [れいな] — họ ひゃ
- JP: `「ひゃうっ」`
- TW: `「啊嗯」`
- VN cũ: `「Hya」`
- Mới: `「Hyau」`
- Lý do: ひゃうっ → "Hyau" (thiếu mora う).

### 1057 [れいな] — họ ひゃ
- JP: `「ひゃうっ！」`
- TW: `「啊嗯！」`
- VN cũ: `「Hya!」`
- Mới: `「Hyau!」`
- Lý do: như 1056.

### 1061 [れいな] — họ ひあ + fa/fu
- JP: `「ひあっ！　あっ！　あうっ――ふあっ――\nそうてつ、さんっ――そうてつ、さぁんっ！」`
- TW: `「啊嗯！啊、啊、啊啊啊……雙鐵先生……雙鐵先生！」`
- VN cũ: `「Hya! A! Au——ha——\nAnh Soutetsu——anh Soutetsu!」`
- Mới: `「Hia! A! Au——Fua——\nAnh Soutetsu——anh Soutetsu!」`
- Lý do: xây trên fix audit ("Hya", "phùa"). ひあっ → "Hia" ("Hya" là romaji của ひゃ, sai âm — quy tắc 3b; tiền lệ 凪h2 sửa ひあ "Hya"→"Hia" ×5); ふあっ → "Fua".

### 1062 [れいな] — họ ひゃ
- JP: `「ひゃうっ！　あっ！　おくっ――おくぅっ――\nごんっって――されて――さきっぽ――さき、でぇ」`
- TW: `「啊嗯！啊！好深……好深……龜頭……撞到最深處了……」`
- VN cũ: `「Hya! A! Sâu bên trong——sâu bên trong——\nBị đâm——bạch bạch——phần đỉnh——đỉnh, ấy」`
- Mới: `「Hyau! A! Sâu bên trong——sâu bên trong——\nBị đâm——bạch bạch——phần đỉnh——đỉnh, ấy」`
- Lý do: ひゃうっ → "Hyau". おくぅっ→"sâu bên trong" là diễn nghĩa, audit chấp nhận — giữ.

### 1064 [れいな] — romaji (mất ふう)
- JP: `「きゅふうっ！　んっ――ふううううっ――んっ！\nそこ――ざらざら、の――はっ――きもち――い、いっ」`
- TW: `「啊嗯！嗚嗚嗚嗚……啊嗯！那裡……澀澀的……好舒服……」`
- VN cũ: `「Kyu! Ưm——fuuuuu——ưm!\nChỗ đó——nham nhám——ha——sướng——quá」`
- Mới: `「Kyufuu! Ưm——fuuuuu——ưm!\nChỗ đó——nham nhám——ha——sướng——quá」`
- Lý do: きゅふうっ = kyu + fuu (2 u) → "Kyufuu!" ("Kyu!" làm mất ふう; tiền lệ hachiroku-h9 きゅふっ→"Kyuhu!"). ふううううっ→"fuuuuu" (5 u ✓ — audit §4 ghi giữ, đếm lại đúng) — giữ.

### 1065 [れいな] — fa/fu
- JP: `「ひゃっ！　あっ――おなか――めくれっ――るっ！――\nふあっ――ささる――の――ふかいっ――ふか、くてっ」`
- TW: `「啊嗯！在肚子裡……插來插去……蛤啊……插得……好深……好深」`
- VN cũ: `「Hya! A——bụng——như bị lộn ngược——ra!——\nHa——đâm vào——sâu——sâu, quá」`
- Mới: `「Hya! A——bụng——như bị lộn ngược——ra!——\nFua——đâm vào——sâu——sâu, quá」`
- Lý do: xây trên fix audit "Phùa" → "Fua".

### 1068 [れいな] — họ ひゅ
- JP: `「ひゃんっ！　うひゅっ――あっ――ぞり、って――\nそこっ――そこ、されちゃうと――れいな――れいなぁ」`
- TW: `「啊嗯，呀啊啊啊……啊啊啊嗯……那裡、那裡被摩擦的話……玲奈……玲奈……」`
- VN cũ: `「Hyan! Ư——a——bị cọ xát——\nChỗ đó——bị làm chỗ đó thì——Reina——Reina」`
- Mới: `「Hyan! Uhyu——a——bị cọ xát——\nChỗ đó——bị làm chỗ đó thì——Reina——Reina」`
- Lý do: うひゅっ = u + hyu → "Uhyu" ("Ư" mất hẳn hyu — quy tắc 3b). Audit §4 ghi giữ "Ư" (nén nhất quán) — quyết trước quy tắc 3b; đợt moan áp 3b. Xem cờ F6.

### 1077 [れいな] — romaji (mất ん)
- JP: `「あ～～んっ」`
- TW: `「啊～～」`
- VN cũ: `「A~~」`
- Mới: `「A~~n」`
- Lý do: あ～～んっ = a + ～～ + ん + っ; VN cũ mất mora �ん. "A~~n" giữ lại n (tiền lệ paulette-h8 ひゃうんんっ→"Hyaunn" giữ n; reinah3 1040 やぁん→"Yaan"). っ cuối ngầm hiểu (không dấu câu trong JP). Audit §4 ghi giữ "A~~" (kiểu romaji) — đợt moan chỉ thêm mora bị mất, xem cờ F6.

### 1081 [れいな] — fa/fu
- JP: `「ふぁっ――あ――ちゅっ！――ちゅうう――ちゅっ――\nれるっ――れりゅ――ちゅっ――ちゅうう――ちゅっ！」`
- TW: `「啾、啾、啾……噗啾！啾、啾嚕……啾、啾嚕！」`
- VN cũ: `「Ha——a——chụt!——chụt——chụt——\nChụt——chụt——chụt——chụt——chụt!」`
- Mới: `「Fa——a——chụt!——chụt——chụt——\nChụt——chụt——chụt——chụt——chụt!」`
- Lý do: xây trên fix audit "Phà" → "Fa" (romaji fallback; "Phà" là phiên âm Việt của ふぁ). Chuỗi ちゅ→"chụt" giữ (quy ước file).

### 1087 [れいな] — romaji + đếm nguyên âm (ふぅ/ふー)
- JP: `「ふっ――んっ――んっ……\nんくっ…………ふぅっ――ふっ……ふーっ――ふーっ」`
- TW: `「嗚嗚……嗯……嗯……啊嗯……呼……呼……呼……」`
- VN cũ: `「Ư——ưm——ưm……\nƯm…………phù——phù……phù——phù」`
- Mới: `「Phù——ưm——ưm……\nNku…………phùu——phù……phùu——phùu」`
- Lý do: ふっ → "Phù" (cũ "Ư" mất hẳn fu — quy ước file ふっ→"phù"); んくっ → "Nku" (xem F3); ふぅっ → "phùu" (2 u, cũ 1 u); ふっ → "phù" giữ; ふーっ → "phùu" ×2 (ふー = 2 u). Xem cờ F2.

### 1088 [れいな] — romaji (んぷっ, んんっ)
- JP: `「んぷっ――んっ――んんっ」`
- TW: `「嗚嗚……嗯、啊嗯……」`
- VN cũ: `「Ưm——ưm——ưm」`
- Mới: `「Npu——ưm——ưmm」`
- Lý do: んぷっ → "Npu" ("Ưm" mất hẳn p — cùng mẫu reinah3 んむっ→"nmu", んくっ→"Nku"); んんっ → "ưmm" (2 mora ん — tiền lệ reinah3 1061, mikuro).

### 1089 [れいな] — đếm nguyên âm (u dài + ん cuối)
- JP: `「ひゅふぅぅぅぅぅぅぅぅぅぅぅぅぅぅっんっ！」`
- TW: `「嗚嗚嗚嗚嗚！」`
- VN cũ: `「Hyuuuuuuuuuuuuuuuuu!」`
- Mới: `「Hyuuuuuuuuuuuuuuuun!」`
- Lý do: đếm lại độc lập bằng codepoint: JP = ひゅ (1 u) + ふ (1 u) + ぅ×14 = 16 u; VN cũ 17 u — thừa 1. Thêm "n" cuối cho mora ん trong っんっ (cũ mất n; "!" diễn っ cắt ngang). Audit §4 ghi giữ dạng romaji (kiểu diễn) — đợt moan chỉ sửa số lượng + mora bị mất, xem cờ F6. Đã xác minh bằng máy: fix có đúng 16 u + 1 n.

### 1090 [れいな] — romaji (んぶっ)
- JP: `「んぶっ！！？」`
- TW: `「嗚嗚！！？」`
- VN cũ: `「Ưm!!?」`
- Mới: `「Nbu!!?」`
- Lý do: んぶっ → "Nbu" (tiền lệ reinah3 1092 んぶっ→"Nbu" đã đúng trong file đó).

### 1114 [れいな] — fa/fu + pu + đếm nguyên âm (はぁっ)
- JP: `「ひゃいれふぅ――んッ――れろおおおおおおっ――\nんむっ――ぷあっ！　ぷはっ！　はぁっ……はぁっ」`
- TW: `「好的……嗯……啾嚕嚕嚕……嗯……噗哈！蛤啊、蛤啊……」`
- VN cũ: `「Vâng ạ——ưm——chụt——\nƯm——phù! Phù! Ha……ha」`
- Mới: `「Vâng ạ——ưm——chụt——\nƯm——Pua! Puha! Haa……Haa」`
- Lý do: xây trên fix audit ("phùa!", "Phù!", "Ha……ha"). ぷあっ → "Pua" (cũ "phù" sai hẳn phụ âm p; tiền lệ lr-fukamih2, kisaki-h3 2207); ぷはっ → "Puha!" (cũ "Phù!" sai âm — ぷは là pu-ha, không phải ふ); はぁっ → "Haa" ×2 (は + ぁ = 2 a; tiền lệ paulette-h3 948 はぁっ→"hàà"). ひゃいれふぅ là nói ngọng miệng đầy (garbled speech) → "Vâng ạ" là diễn nghĩa, KHÔNG phải dòng rên (quy tắc 3b) — giữ, để audit. んむっ→"Ưm" giữ theo audit §4 (xem §4).

### 1174 [れいな] — fa/fu
- JP: `「おもいっきり――おもいっきり――ふあっ――\nそうてつ、さんの――おもい、きり――」`
- TW: `「盡情……盡情地……蛤啊……雙鐵先生……盡情地……」`
- VN cũ: `「Mạnh bạo——mạnh bạo——ha——\ncủa anh, Soutetsu——mạnh, bạo——」`
- Mới: `「Mạnh bạo——mạnh bạo——Fua——\ncủa anh, Soutetsu——mạnh, bạo——」`
- Lý do: xây trên fix audit "phùa" → "Fua".

### 1180 [れいな] — fa/fu
- JP: `「ひゃっ――あっ――ふあっ――あっ――おまた――\nきもち――いい――です、よぉっ――んうっ」`
- TW: `「蛤啊……啊……蛤啊啊……下面……好舒服……啊嗯」`
- VN cũ: `「Hya——a——ha——a——bên dưới——\nsướng——quá——ạ~——ưm」`
- Mới: `「Hya——a——Fua——a——bên dưới——\nsướng——quá——ạ~——ưm」`
- Lý do: xây trên fix audit "phùa" → "Fua". んうっ→"ưm" giữ (tiền lệ fukamih1 964).

### 1182 [双鉄H] — fa/fu (pu)
- JP: `「ぷあっ――あっ――れいな。いいか？」`
- TW: `「蛤啊……玲奈，可以嗎？」`
- VN cũ: `「Phù——a——Reina. Được chứ?」`
- Mới: `「Pua——a——Reina. Được chứ?」`
- Lý do: xây trên fix audit "Phùa" → "Pua" (ぷあ là pu-a; "Phù/Phùa" sai phụ âm p).

### 1183 [れいな] — fa/fu + đếm nguyên âm (はぅぅ)
- JP: `「ふぇっ――ふあっ――はっ――はぅぅ――」`
- TW: `「蛤啊……蛤啊……」`
- VN cũ: `「Fe——ha——ha——hau——」`
- Mới: `「Fue——Fua——ha——hauu——」`
- Lý do: xây trên fix audit ("Phuê", "phùa"). ふぇっ → "Fue", ふあっ → "Fua"; はぅぅ = ha + u×2 → "hauu" (cũ "hau" thiếu 1 u).

### 1184 [れいな] — fa/fu
- JP: `「ふあっ――あっ――おっぱい――――んっ――ふっ」`
- TW: `「蛤啊、啊……胸部……啊嗯」`
- VN cũ: `「Ha——a——ngực————ưm——phù」`
- Mới: `「Fua——a——ngực————ưm——phù」`
- Lý do: xây trên fix audit "Phùa" → "Fua".

### 1185 [れいな] — fa/fu + đếm nguyên âm (はあっ, ふぁぁっ)
- JP: `「ふぁっ――はあっ――あっ――ふぁぁっ――」`
- TW: `「蛤啊、蛤啊、啊啊啊啊」`
- VN cũ: `「Ha——ha——a——ha——」`
- Mới: `「Fa——haa——a——Faa——」`
- Lý do: xây trên fix audit ("Phà", "ha", "phàà"). ふぁっ → "Fa"; はあっ = ha + a = 2 a → "haa" (audit giữ "ha" — bỏ sót đếm); ふぁぁっ = fa + a = 2 a → "Faa" (audit "phàà" đếm đúng 2 a, chỉ đổi dạng romaji).

### 1210 [れいな] — họ ひゅ
- JP: `「そう、てつ――さぁ、んっ――ひっ――あひゅっ――\nんっ――れいなっ――れいな――もっ」`
- TW: `「雙鐵先生……啊……啊嗯……嗯……玲奈……玲奈也是……」`
- VN cũ: `「Anh, Soutetsu——ưm——hi——a——\nƯm——Reina——Reina——cũng」`
- Mới: `「Anh, Soutetsu——ưm——hi——Ahyu——\nƯm——Reina——Reina——cũng」`
- Lý do: あひゅっ = a + hyu → "Ahyu" ("a" mất hẳn hyu — quy tắc 3b). Audit §4 ghi giữ "a" (nén nhất quán) — quyết trước quy tắc 3b; đợt moan áp 3b. Xem cờ F6. ひっ→"hi" đã đúng — giữ.

### 1216 [れいな] — đếm nguyên âm
- JP: `『「ぬっ！？」\n「ひゃああんっ！」』`
- TW: `『“咦？！”“哎呀！”』`
- VN cũ: `『「Hả!?」\n「Hyaaaan!」』`
- Mới: `『「Hả!?」\n「Hyaaan!」』`
- Lý do: JP ひゃ + あ×2 = 3 nguyên âm a; VN cũ 4 a — thừa 1. Đếm lại độc lập bằng máy.

## §4. Các dòng rên đã xét mà giữ nguyên (ghi chú đáng kể)

- **Gasp Ư của audit/sweep — không đụng:** 1031, 1070, 1071, 1215 (fix audit đã thêm Ư; quy tắc khóa: không xem lại dòng gasp Ư).
- **んむっ → "A ưm" / "a ưm" / "ưm" / "Ưm" — GIỮ (1043, 1093, 1094, 1114):** audit §4 quyết giữ rõ ràng ("diễn rên ngẫu hứng theo quy tắc Hieu 19/11; âm mũi ん được diễn thành 'A ưm' nhất quán trong file"). Đợt moan tôn trọng quyết này — không đổi thành "Nmu" dù reinah3 dùng "nmu" (file khác, quy ước khác).
- **ふっ → "phù" — giữ toàn bộ file** (trừ 1087 token đầu ふっ→"Ư" bị mất âm, đã sửa thành "Phù"): 1003, 1026, 1030? không — 1030 không có ふっ; 1053, 1087 (token giữa), 1110, 1184. Câu hỏi mở "phù" hay "Fu" (reinah4 F2) để đợt thống nhất quyết, không đổi ở đây.
- **Họ ん → "ưm" — quy ước file, giữ:** 786 ん→"Ưm", 1001 んっ→"ưm", 1045/1180 んうっ→"ưm" (tiền lệ fukamih1 964), 1181 むっ→"ưm" (tiền lệ kisaki-h3 2214 む→"Ưm"), 1095 うむ→"Ừm", 1098 ふむ→"Hừm", 1100 うむ→"Ưm".
- **Chuỗi nuốt ごくっ/こくっ/ごきゅっ/きゅむっ → "Ực" — giữ** (1008/1009): đồng nhất toàn file, đúng quy ước SFX nuốt.
- **Chuỗi hôn/mút ちゅ/じゅ/れろ/れる → "chụt" — giữ** (1079, 1081, 1084, 1085, 1110, 1181): đồng nhất toàn file.
- **SFX trong （ ） — giữ toàn bộ dạng động từ Việt** (tiền lệ ふかみh3 F4, reinah3 F4 — chưa áp công thức đếm ở đợt moan): 1730–1771 （ぬぶううう…）→"（Phậpppppppppp——bạch）", 1731–1744 （びゅっ…）→"（Phụt!…）", 1747 （ごっ…）→"（Bạch!…）", 1748 （ぷちっ）→"（Tách——tách——）", 1749 （ばちんっ）→"（Bốp!）", 1755–1759 （れりゅ…）→"（Chụt…）", 1760–1761 （ちょろ…）→"（Róc rách…）", 1764–1771 （ぐい…/きゅむ…）→"（Phậpppppp!!）/（Siết chặt!）". Xem cờ F4.
- **Romaji đã đúng, giữ:** 1001 ひゃっ→"Hya", 1052/1065/1180 ひゃっ→"Hya", 1032 あーーーーー→"Aaaaaa" (6 a ✓), 1064 ふううううっ→"fuuuuu" (5 u ✓), 1026/1054 はうっ→"Hau", 1173 あーー→"aaa" (3 a ✓), 1210 ひっ→"hi", 1035/1106 えへへ→"E he he" (cười), 1102 えへへぇ→"E he he~".
- **Cười — giữ:** 1104/1108 audit đã sửa đúng "Fufu~"/"Ufufu~" (うふふぉ là cười, không phải rên); 1106 えへへぇ→"E he he~" đã đúng.
- **Nói ngọng miệng đầy (garbled speech) — KHÔNG phải dòng rên, giữ:** 1114 ひゃいれふぅ→"Vâng ạ" (diễn nghĩa), 1199 ほーへふぁん…→"Như vầy ạ…/Tiếp tục đi ạ…" (diễn nghĩa), 1104 ふふぅっへひへひ…→"sướng chứ ạ~/chụt chụt chụt" (chỉ token cười đầu đã sửa bởi audit) — để audit.
- **786 しゅき/だいしゅきい → "thích……thích nhất" — giữ** (audit §4, tiền lệ ふかみh3 2394: tiếng ngọng cute không có tương đương Việt tự nhiên). さぁんっ→"anh Soutetsu~" (độ dài さぁ hút vào "~" sau tên; audit chấp nhận) — giữ. Tương tự 1027 さぁ、んっ→"anh Soutetsu——ưm——" và 1061 さぁんっ→"anh Soutetsu!" — giữ.
- **1067 ひゃ――ん！！→"Hya——n!!" — giữ:** dấu ―― có sẵn trong JP (không phải lỗi tách như paulette-h8 ひゃうんんっ); ひゃっ→"hya" viết thường là không nhất quán hoa/thường (mỹ thuật) — giữ, xem cờ F5.
- **1026 はうっ→"Hau", あうっ→"Au", はっ→"Ha", ん→"ưm", ふっ→"phù" — giữ;** chỉ flag token やぁっ (xem F1). 1047/1062 おくっ/おくぅっ→"sâu bên trong" là diễn nghĩa, audit chấp nhận — giữ.
- **1101 よいしょっ→"hây dô" — giữ** (audit §3: tiếng lấy đà, っ cuối chỉ ngắt). **1120 ごろーーーーん→"Nằm xuống" — giữ** (audit §4: diễn âm lăn người thành hành động). **1202/1203 あの……→"Ưm……" — giữ** (あの là ngập ngừng, diễn thành "Ưm" hợp lý).

## §5. Cờ (flag — để parent / đợt thống nhất / audit, không thuộc phạm vi moan)

- **F1 — 1026 [れいな] (không sửa — やぁっ là rên hay từ "không"?):** JP `「はうっ――あっ――はがれ――ちゃうっ――ん、ふっ、\nあうっ――いっちゃ――や、らっ――やぁっ――」` / TW `「哈嗚……啊……啊嗯……身體……都要被插壞了……啊嗯……啊……要去了……」` / VN `「Hau——a——như bị bong——ra——ưm, phù,\nAu——sắp ra——không, được——không——」` — やぁっ đang được diễn thành từ "không"; nhưng TW diễn cả dòng thành tiếng rên, và tiền lệ reinah3 1040 やぁん→"Yaan" coi やぁん là rên. Ngược lại, "や、らっ" là lời nói lắp (có thể là mảnh của "yada"), audit đã chấp nhận cách đọc "không, được——không". Thêm nữa "được" cho らっ không có căn cứ JP rõ — đó là vấn đề nghĩa/bịa, thuộc audit, không thuộc moan. Park cho parent quyết: giữ "không" hay sửa thành "Yaa".
- **F2 — ふぅ/ふう/ふー → "phùu" hay giữ "phù" (câu hỏi mở):** đợt này sửa 779/1046/1087 sang 2 u theo công thức đếm (tiền lệ paulette-h6 ふぅっ→"Phùu", lr-nagifukami ふぅ→"fuu", hachiroku-h8 ふぅ→"phuu" giữ đúng). Mâu thuẫn với tiền lệ paulette-h8 ("chuỗi ふう → 'phù', quy ước file, không áp công thức đếm"). Đợt thống nhất quyết một dạng cho toàn dự án.
- **F3 — んくっ → "Nku" hay giữ "Ưm" (1030, 1087):** đợt này sửa sang romaji theo reinah3 (んくっ→"Nku", くっ→"Ku"). Tiền lệ ngược: nagih2 2501 giữ んくっ→"Ư" trong chuỗi nuốt (ごくっ đi kèm). Chuỗi ở đây là tiếng gầm/thở (Soutetsu 1030, Reina 1087), không phải nuốt — nhưng nếu đợt thống nhất chọn "Ưm" cho んくっ thì hoàn lại 2 dòng này.
- **F4 — SFX trong （ ） chưa áp công thức đếm (đợt thống nhất):** 1730–1771 giữ dạng động từ Việt theo tiền lệ ふかみh3 F4 / reinah3 F4 (vd. 1757 （ぐりいいいいいいいいいいいっ！！！）→"（Phậpppppppppp!!!）" đếm bằng lặp phụ âm p, không phải nguyên âm). Đợt thống nhất quyết có áp công thức đếm cho SFX （ ） hay không.
- **F5 — 1067 ひゃっ→"hya" viết thường (mỹ thuật):** không nhất quán hoa/thường với "Hya" ở các dòng khác trong file. Đợt moan giữ nguyên (không phải lỗi âm); đợt thống nhất có thể chuẩn hoá.
- **F6 — Các quyết giữ của audit §4 bị đợt moan ghi đè (ghi rõ để parent kiểm):** (a) 1042 んひゅっ→"Ưm!", 1068 うひゅっ→"Ư", 1210 あひゅっ→"a" — audit giữ vì "nén nhất quán trong file", nhưng quyết đó ra đời TRƯỚC quy tắc 3b (21/11 ~11:55) và mâu thuẫn với nó (んひゅ→"Nhyu" là tiền lệ đã khóa h7/稀咲h3/凪h2); (b) 1002 "Hyaaaaaan" (6 a), 1089 "Hyuuuu…!" (17 u), 1077 "A~~" (mất ん) — audit giữ vì KIỂU romaji nhất quán, không đếm số lượng; đợt moan chỉ sửa số lượng/mora theo công thức đếm đã khóa, không đổi kiểu diễn. Nếu parent cho rằng quyết giữ của audit bao gồm cả số lượng thì hoàn lại 1002/1089/1077 (và 1042/1068/1210 nếu cho rằng 3b không áp dụng ngược).
- **F7 — 1043/1093/1094/1114 んむっ GIỮ theo audit (không phải cờ sửa):** ghi lại để parent khỏi sửa lại ở đợt thống nhất: audit §4 đã quyết giữ "A ưm"/"a ưm"/"ưm"/"Ưm" cho んむっ (diễn ngẫu hứng, nhất quán trong file); đợt moan tôn trọng, KHÔNG đổi thành "Nmu" (dù reinah3 dùng "nmu").

## §6. Lượt soát 2 (second pass)

- Tổng 37 / tái kiểm chứng 37 / bỏ 0 / sửa 0.
- Đã đọc lại toàn bộ 37 giá trị fix đối chiếu từng JP (+TW): đếm nguyên âm kiểm chứng độc lập bằng máy (codepoint) cho 779 (2 u), 1002 (4 a), 1040 (1 a + 5 u), 1064 (ふううううっ 5 u ✓ giữ), 1089 (16 u + 1 n), 1114 (はぁっ 2 a ×2), 1183 (はぅぅ 2 u), 1185 (はあっ 2 a, ふぁぁっ 2 a), 1216 (3 a).
- Kiểm chứng chéo với fix audit bằng máy: 14 key trùng audit chỉ khác đúng token rên (1001: ưm→ưmm, phùa→Fua ×2, Á→Ya; 1061: Hya→Hia, phùa→Fua; 1114: phùa!→Pua!, Phù!→Puha!, Ha→Haa ×2; 1183: Phuê→Fue, phùa→Fua, hau→hauu; 1185: Phà→Fa, ha→haa, phàà→Faa; còn lại chỉ 1 token phùa/phà→Fua/Fa). 23 key mới không trùng audit.
- JSON 37 mục, khóa string, jp/tw/old_vn khớp CSV3 37/37 (good set duy nhất, VN flat-match TOML 284/284 sau chuẩn hoá \n).
- Khối TOML parse bằng tomllib: 37 khóa, 0 sai lệch giá trị. Mỗi fix chỉ khác VN cũ ở đúng token rên (kiểm chứng bằng máy: số dòng \n bằng nhau, không đổi token ngoài rên).

## §7. Khối TOML (đã parse-kiểm chứng: 37 khóa, 0 sai lệch)
```toml
[script]
"779" = "「——Ưm……phùu.\\nTuyệt lắm. Vậy là, đặc huấn đã thành công mỹ mãn rồi.」"
"1001" = "「Hya——a——ưm——ưmm——Fua——\\nYa——bên dưới——nhầy nhụa, rồi——Fua——a」"
"1002" = "「Hyaaaan」"
"1003" = "「Ku——phù——」"
"1027" = "「Ha——ưm——Fua——ưm——\\nNữa đi——nữa đi——nha, anh Soutetsu——ưm——」"
"1030" = "「Nku——Ku——Ku」"
"1036" = "「A——Fua——」"
"1040" = "「Hyauuuuu!!?」"
"1042" = "「Hyau! A! Đột——nhiên——a!\\nNhyu! Hya——bụng——bị đâm——rồi——」"
"1045" = "「Hyapu——ưm——a? A——ưm」"
"1046" = "「Nhyu——a——miệng——ưm——phùu」"
"1047" = "「Hyafu——a——sâu bên trong——tận cùng——\\nbụng——tận cùng——bị ngoáy, ngoáy——Hyau!」"
"1049" = "「Hyau——a——liếm——liếm——ưm,\\nlưỡi——của anh——Soutetsu——lưỡi——」"
"1052" = "「Hyan——ưm——mạn sườn——nhột quá——\\nFua——ưm!」"
"1053" = "「Ưm kyu——phù——a——Reina——Reina——\\nlỗ tiểu——bị chọc chọc, liếm liếm——rồi」"
"1056" = "「Hyau」"
"1057" = "「Hyau!」"
"1061" = "「Hia! A! Au——Fua——\\nAnh Soutetsu——anh Soutetsu!」"
"1062" = "「Hyau! A! Sâu bên trong——sâu bên trong——\\nBị đâm——bạch bạch——phần đỉnh——đỉnh, ấy」"
"1064" = "「Kyufuu! Ưm——fuuuuu——ưm!\\nChỗ đó——nham nhám——ha——sướng——quá」"
"1065" = "「Hya! A——bụng——như bị lộn ngược——ra!——\\nFua——đâm vào——sâu——sâu, quá」"
"1068" = "「Hyan! Uhyu——a——bị cọ xát——\\nChỗ đó——bị làm chỗ đó thì——Reina——Reina」"
"1077" = "「A~~n」"
"1081" = "「Fa——a——chụt!——chụt——chụt——\\nChụt——chụt——chụt——chụt——chụt!」"
"1087" = "「Phù——ưm——ưm……\\nNku…………phùu——phù……phùu——phùu」"
"1088" = "「Npu——ưm——ưmm」"
"1089" = "「Hyuuuuuuuuuuuuuuuun!」"
"1090" = "「Nbu!!?」"
"1114" = "「Vâng ạ——ưm——chụt——\\nƯm——Pua! Puha! Haa……Haa」"
"1174" = "「Mạnh bạo——mạnh bạo——Fua——\\ncủa anh, Soutetsu——mạnh, bạo——」"
"1180" = "「Hya——a——Fua——a——bên dưới——\\nsướng——quá——ạ~——ưm」"
"1182" = "「Pua——a——Reina. Được chứ?」"
"1183" = "「Fue——Fua——ha——hauu——」"
"1184" = "「Fua——a——ngực————ưm——phù」"
"1185" = "「Fa——haa——a——Faa——」"
"1210" = "「Anh, Soutetsu——ưm——hi——Ahyu——\\nƯm——Reina——Reina——cũng」"
"1216" = "『「Hả!?」\\n「Hyaaan!」』"
```
File れいなh2_おもらし防止大作戦.txt.toml: đã đọc 284/284 dòng, xét 196 dòng ứng viên rên/SFX, **sửa 37 dòng** (13 romaji họ fa/fu + 11 romaji họ ひゃ/ひゅ/ひあ + 8 romaji mất phụ âm mora + 5 đếm nguyên âm; 14 key trùng audit chỉ khác đúng token rên, 23 key mới), giữ 159 dòng. Lỗi tập trung ở họ fa/fu bị audit Việt hoá ("phà"/"phùa") trước quy tắc romaji, họ ひゃう bị đọc thành "Hya" (mất mora う), và rên dài đếm sai nguyên âm. Mọi gasp Ư và dòng "Kh" đều giữ nguyên (file không có "Kh"). Lượt soát 2: 37/37, 0 bỏ, 0 sửa; khối TOML parse đúng, 0 sai lệch. Cờ còn lại: F1 (1026 やぁっ "không" hay "Yaa"), F2 (ふぅ "phùu" hay "phù"), F3 (んくっ "Nku" hay "Ưm"), F4 (SFX （ ） chưa đếm), F5 (1067 "hya" viết thường), F6 (các quyết giữ audit §4 bị ghi đè theo quy tắc 3b/công thức đếm), F7 (んむっ giữ theo audit — không sửa) — tất cả chờ parent / đợt thống nhất / audit, không thuộc phạm vi moan.

Kết bài
