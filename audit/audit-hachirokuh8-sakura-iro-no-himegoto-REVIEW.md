# Kiểm tra file ハチロクh8_桜色のひめごと — 63/332 sai (19,0%)

- File: `ハチロクh8_桜色のひめごと.txt.toml` — route 01_Hachiroku, 332 dòng script (monologue 176, ハチロク 98, 双鉄 58). Nội dung: cảnh H thứ tám của Hachiroku (lễ hội Hinamatsuri, rượu ngọt/amazake, wakame-zake và wareme-zake) — Soutetsu và Hachiroku làm tình, xen kẽ độc thoại Soutetsu và một đoạn dài SFX trong ngoặc （） (1524–1594: tiếng cọ xát, mút, xuất tinh).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, 332 dòng, 0 key trùng, 0 VN trống. TOML và CSV3 khớp tuyệt đối ngoài 183 dòng chênh ở `\n` literal bị TOML-2 làm phẳng thành khoảng trắng (CSV3 là chuẩn, đã kiểm chứng cơ học: 0 lệch ngoài flatten). TOML md5 `818002990fb400412684b19303c9839c`, BOM + CRLF, `[selections]` rỗng, không bản sao trùng (md5 xuất hiện 1 lần trong toàn bộ toml2). Thẻ `%l`: JP 0 dòng, VN 0 dòng. Không có tag ruby nào trong VN (861 có `[なか,1]` ở JP — VN đã chuẩn hóa, bỏ tag, không tính lỗi).
- Phân loại (63): romaji 34, đại từ 12, gasp 9, đếm nguyên âm 5, nghĩa 3. Theo nhân vật: ハチロク 39/98 (39,8%), 双鉄 17/58 (29,3%), monologue 7/176 (4,0%). Thoại 56/156 (35,9%), độc thoại 7/176 (4,0%). Lỗi tập trung ở tiếng rên/moans (34 romaji + 5 đếm nguyên âm + 9 gasp = 48/63), đúng với bản chất file H-scene.
- Gasp sweep: 8 mục fix cho file này — áp nguyên 7/8 (467, 749, 951, 952, 1225, 1274, 1276) và sửa lại 1 mục (953: sweep ghi 9 dấu ~, JP chỉ có 7 ~). Thêm 2 gasp sweep bỏ sót: 706 (おっぱい――っ giữa dòng) và 835 (っ đầu dòng + đếm u sai). Đã quét cơ học toàn bộ dòng JP có っ: các っ còn lại đều là っ nhấn mạnh gắn từ có nội dung (1150 やめずにっ, 1317, 1418), っ ngắt nguyên âm (あっ/ああっ → "A"/"Aa", tiền lệ h1 1251/1263/1264 — không thêm Ư), hoặc âm đã diễn (ちゅっ→"Chụt", んっ→"Ưm", んくっ→"Ưn ku", ごくんっ→"Ực", くっ→"khục").
- Đại từ 12: Soutetsu "anh"→"tôi" với Hachiroku — 9 dòng thoại 双鉄 (870, 871, 872, 874, 876, 885, 905, 929, 936) + 3 dòng độc thoại (1253, 1300, 1304 — trích lời/ý nghĩ tự nhủ, trong đó 1253 mâu thuẫn nội bộ "Anh… tôi" ngay trong một câu). Đã quét cơ học sau khi sửa: file không còn dòng Soutetsu nào tự xưng "anh" (chỉ còn "Hoa anh đào" 899 và các "anh" trong từ ghép, không phải đại từ).
- Romaji 34 — một lỗi hệ thống: bản dịch cũ diễn mọi ふ/ふぁ/ふあ thành "hu/hua/huaa" (phụ âm h thay vì f). Sửa theo romaji fallback + tiền lệ h1 (ふあっ→"Fua", ふああっ→"Fuaa") và tiền lệ giữ "phù" cho ふっ/ふ (h1; file này 767 đã dùng "phù"): ふぁ/ふあ→"Fua/Fuaa" (19 dòng), ふっ/ふ→"Phù/phù" (13 dòng, kể cả trong từ nói ngọng ほーへふ/わらふ/はふぁ), きゃふっ→"Kyafu" (703). ひあ/ひゃ đã đúng romaji sẵn ("Hia/Hya/Hyua/Hyagyu") — không sửa.
- Đếm nguyên âm 5 (709, 736, 782, 811, 836): đối chiếu cơ học từng âm kéo dài với JP theo công thức (số nguyên âm VN = số kana tương ứng trong JP). Sửa lớn nhất: 836 "Ưn kyuuuu…" 26 chữ u → 12 chữ u; 811 15 chữ i → 10 chữ i.
- Thuật ngữ trong file: わかめ酒/われめ酒/甘酒 đã dịch đúng ("rượu rong biển/khe hở/ngọt", kèm chú thích romaji trong ngoặc — giữ nguyên, là phong cách nhất quán của file); không có 御一夜 / 帝鉄 / 湯医 / まいてつ / 宮司 / 日ノ本 / 乗員 / 乗務鞄 nào — không có mục mới cho đợt unification từ file này.
- Moans 48 (romaji 34 + đếm nguyên âm 5 + gasp 9): xem chi tiết dưới đây. SFX trong ngoặc （） diễn theo nghĩa hành động (きゅ→"Siết chặt", れる→"Liếm", ずぶ→"Phập", びゅ→"Phụt") chỉ sửa chỗ sai hẳn âm (798); độ dài kéo chữ của các từ hành động ("mátttt…", "chépppp…") giữ nguyên theo tiền lệ h1 — công thức đếm nguyên âm chỉ áp cho tiếng rên dạng romaji/âm thanh.

## Chi tiết từng dòng sai (63)

### 467 — gasp (双鉄)
- JP: 「――っ！！！！」
- TW: 「——！！！！」
- VN cũ: 「——!!!!」
- VN mới: 「——Ư!!!!」
- Lý do: Gasp bị mất: JP là một tiếng gasp độc lập (――っ) — VN chỉ giữ dấu gạch, rớt mất っ. Thêm Ư sau gạch theo sweep (mục lost-gasp-trailing).

### 703 — romaji (ハチロク)
- JP: 「きゃふっ！？　あっ！　おまん、まんっ――んっ！！\nわたく、し――わたくしの――おまん、まんっ――ふぁ」
- TW: 「呀呼！？啊！小妹妹——！！我——我的——小妹妹——嗚啊」
- VN cũ: 「Kya hu!? A! Tiểu huyệt——ưm!!\nEm——tiểu huyệt——của em——hua」
- VN mới: 「Kyafu!? A! Tiểu huyệt——ưm!!\nEm——tiểu huyệt——của em——Fua」
- Lý do: きゃふっ = "Kyafu" (romaji, một âm — không tách "Kya" + "hu"); ふぁ cuối dòng = "Fua" theo romaji fallback (tiền lệ h1 1214/1251: ふあっ → "Fua"). Phụ âm ふ là f, không phải h.

### 705 — romaji (ハチロク)
- JP: 「ひゅあっ！？　んっ――ビクって！　ぷくって！！　\n双鉄さま――のっ――おちん――ちんっ！！　ふあ！」
- TW: 「呀啊！？嗯——又抖了！又脹了！！雙鐵少爺的——雞——雞！！呼啊！」
- VN cũ: 「Hyua!? Ưm——giật giật! Phồng lên rồi!!\nCôn thịt——của Ngài Soutetsu!! Hua!」
- VN mới: 「Hyua!? Ưm——giật giật! Phồng lên rồi!!\nCôn thịt——của Ngài Soutetsu!! Fua!」
- Lý do: ふあ！ = "Fua!" theo romaji fallback (tiền lệ h1). ひゅあっ → "Hyua" và んっ → "Ưm" giữ nguyên.

### 706 — romaji (ハチロク)
- JP: 「ひゃぎゅっ！？　ふっ――ふあっ！？　あっ――\nおっぱい――っ！　やっ、ちくびっ――くりゅ、ん、ふ」
- TW: 「呀嗚！？呼——呼啊！？啊——乳房——！呀，乳頭——揉，嗯，呼」
- VN cũ: 「Hyagyu!? Hu——huaa!? A——\nnhũ hoa——! A, núm vú——kích thích, ưm, hu」
- VN mới: 「Hyagyu!? Phù——Fua!? A——\nnhũ hoa——Ư! A, núm vú——kích thích, ưm, phù」
- Lý do: ふっ → "Phù" (tiền lệ h1 giữ "phù" cho ふっ; file này 767 đã dùng "phù"); ふあっ → "Fua" (1 nguyên âm a, VN cũ "huaa" thừa 1 a); おっぱい――っ là gasp sweep bỏ sót (giữa dòng, không phải cuối dòng) — thêm Ư; ふ cuối dòng → "phù".

### 708 — romaji (ハチロク)
- JP: 「ひゃっ！　あっ！？　吸われ――おまめっ…ふぁっ！\nおまんまん――ぁ……じゅるじゅる――音、やっ――ん」
- TW: 「呀！啊！？吸——小豆豆…嗚啊！小妹妹——啊……啾嚕啾嚕的——聲音，啊——」
- VN cũ: 「Hya! A!? Bị mút rồi——hạt đậu... huaa!\nTiểu huyệt——a……tiếng——chóp chép——xấu hổ, quá——ưm」
- VN mới: 「Hya! A!? Bị mút rồi——hạt đậu... Fua!\nTiểu huyệt——a……tiếng——chóp chép——xấu hổ, quá——ưm」
- Lý do: ふぁっ → "Fua" (1 a; VN cũ "huaa" thừa 1 a) theo romaji fallback.

### 709 — đếm nguyên âm (ハチロク)
- JP: 「ヒュあっ！！？　しょ、しょこおおおおっ！！」
- TW: 「呀！！？好、好棒！！」
- VN cũ: 「Hyua!!? Ch, chỗ đóoooooo!!」
- VN mới: 「Hyua!!? Ch, chỗ đóoooo!!」
- Lý do: Đếm nguyên âm: JP しょこおおおおっ có 5 âm o (こ + お×4); VN cũ "đóoooooo" có 7 chữ o — thừa 2. Sửa thành 5 chữ o.

### 724 — romaji (ハチロク)
- JP: 「ほーへふはふぁっ――ん……ほーほ、\nわらふひひ……はふぁふぁぇ、ほ――」
- TW: 「呼—呼呼啊——……呼—呼，我……哈呼哈呼，呼——」
- VN cũ: 「Ho he hu ha hua——ưm……ho ho,\nwa ra hu hi hi……ha hua hua e, ho——」
- VN mới: 「Ho he phu ha fua——ưm……ho ho,\nwa ra phu hi hi……ha fua fua e, ho——」
- Lý do: Câu nói ngọng (say/xúc động): mọi ふ đều diễn thành "hu" — sửa về phụ âm f: ふ→"phu", ふぁっ→"Fua", ふぁふぁ→"fua fua". Giữ nguyên cách ngắt âm tiết của bản dịch cũ.

### 726 — romaji (ハチロク)
- JP: 「ふああっ！！！」
- TW: 「呼哈！！！」
- VN cũ: 「Huaa!!!」
- VN mới: 「Fuaa!!!」
- Lý do: ふああっ → "Fuaa" (2 a theo JP ああ) theo romaji fallback.

### 728 — romaji (ハチロク)
- JP: 「ふあっ――あっ――あっ――あっ――双鉄、さま、\n双鉄さま――そうてつさまぁっ！！」
- TW: 「呼啊——啊——啊——啊——雙鐵少爺，雙鐵少爺——雙鐵少爺！！」
- VN cũ: 「Huaa——a——a——a——Ngài, Soutetsu,\nNgài Soutetsu——Ngài Soutetsu!!」
- VN mới: 「Fua——a——a——a——Ngài, Soutetsu,\nNgài Soutetsu——Ngài Soutetsu!!」
- Lý do: ふあっ → "Fua" (1 a; VN cũ "huaa" thừa 1 a).

### 729 — romaji (双鉄)
- JP: 「ふあっ！」
- TW: 「呼啊！」
- VN cũ: 「Huaa!」
- VN mới: 「Fua!」
- Lý do: ふあっ → "Fua" (1 a; VN cũ "huaa" thừa 1 a).

### 731 — romaji (ハチロク)
- JP: 「ふあっ！　あっ――ふっ――双鉄、さまっ――\n双鉄――さまぁっ！」
- TW: 「呼啊！啊——呼——雙鐵少爺——雙鐵少爺——啊！」
- VN cũ: 「Huaa! A——hu——Ngài Soutetsu——\nNgài Soutetsu——!」
- VN mới: 「Fua! A——phù——Ngài Soutetsu——\nNgài Soutetsu——!」
- Lý do: ふあっ → "Fua"; ふっ → "Phù" (tiền lệ h1).

### 732 — romaji (ハチロク)
- JP: 「ふあっ！？　そこっ！　あっ――あっ――んっ――！\nんく～～～～～～～～～～～～～～～～～っ！！！」
- TW: 「呼啊！？那裡！啊——啊——！嗯～～～～～～～～～～～～～～～～～！！！」
- VN cũ: 「Huaa!? Chỗ đó! A——a——ưm——!\nƯn ku~~~~~~~~~~~~~~~~~!!!」
- VN mới: 「Fua!? Chỗ đó! A——a——ưm——!\nƯn ku~~~~~~~~~~~~~~~~~!!!」
- Lý do: ふあっ → "Fua" (1 a; VN cũ "huaa" thừa 1 a). Gasp cuối dòng (んく～～～っ) giữ nguyên theo sweep (already-rendered: dấu ~ đã diễn).

### 734 — romaji (双鉄)
- JP: 「ふうううううっ！？」
- TW: 「呼嗚——！？」
- VN cũ: 「Huuuuuu!?」
- VN mới: 「Phuuuuuu!?」
- Lý do: ふうううううっ → "Phuuuuuu" (6 u đúng số lượng; chỉ sửa phụ âm h→ph, tiền lệ h1 giữ "phù" cho ふ).

### 736 — đếm nguyên âm (ハチロク)
- JP: 「ぃっ――きゅうううううううううううっっっ！！！！」
- TW: 「咿——嗯嗚——！！！！」
- VN cũ: 「I——kyuuuuuuuuuuuuuuu!!!!」
- VN mới: 「I——kyuuuuuuuuuuuu!!!!」
- Lý do: Đếm nguyên âm: JP きゅううううううううううう = きゅ + う×11 → 12 chữ u; VN cũ "kyuuuuuuuuuuuuuuu" có 15 chữ u — thừa 3.

### 737 — romaji (ハチロク)
- JP: 「ひあっ！　あっ――ア――んくっ！！　ふっ！」
- TW: 「咿啊！啊——啊——嗯！！呼！」
- VN cũ: 「Hia! A——a——ưn ku!! Hu!」
- VN mới: 「Hia! A——a——ưn ku!! Phù!」
- Lý do: ふっ → "Phù" (tiền lệ h1). ひあっ → "Hia" giữ nguyên (đã đúng romaji).

### 743 — romaji (ハチロク)
- JP: 「ひあっ！？　いやですぅ――わざと――ふ、ぁっ――\nんっ――わざと、そのようなっ――下品な、音――く！」
- TW: 「咿啊！？討厭——故意——呼，啊——嗯——故意，那樣——粗俗的，聲音——！
- VN cũ: 「Hia!? Không chịu đâu——cố tình——hu, a——\nƯm——cố tình, tạo ra âm thanh——dâm đãng, như vậy——khục!」
- VN mới: 「Hia!? Không chịu đâu——cố tình——phu, a——\nƯm——cố tình, tạo ra âm thanh——dâm đãng, như vậy——khục!」
- Lý do: ふ、ぁっ → "phu, a" (chỉ sửa phụ âm ふ: hu→phu).

### 746 — romaji (ハチロク)
- JP: 「いぅん！？　あ――吸、吸って――ひ――きゅ！　ふぁ\n――おもら、し――全部――残りも――吸いだされ、て」
- TW: 「咿嗯！？啊——吸，吸——咿——嗯呀！嗚啊——小便——全部——一點不剩地——被吸掉了」
- VN cũ: 「Iun!? A——Hút, hút mất rồi——hi——kyu! Hua\n——Nước, tiểu——tất cả——cả phần còn lại——cũng bị hút ra, hết」
- VN mới: 「Iun!? A——Hút, hút mất rồi——hi——kyu! Fua\n——Nước, tiểu——tất cả——cả phần còn lại——cũng bị hút ra, hết」
- Lý do: ふぁ → "Fua" theo romaji fallback.

### 749 — gasp (ハチロク)
- JP: 「ぃぃぃぃぃぃぃぃぃぃぃぃぃ～～～～～っ！！！！」
- TW: 「咿～～～～～！！！！」
- VN cũ: 「Iiiiiiiiiiiiiii~~~~~!!!!」
- VN mới: 「Iiiiiiiiiiiii~~~~~Ư!!!!」
- Lý do: Gasp sweep + đếm nguyên âm: JP ぃ×13, ～×5, っ. VN cũ có 15 chữ i — thừa 2 (sửa về 13 i); thêm Ư sau dấu ~ cho っ cuối dòng theo sweep (đã kiểm chứng lại số lượng, sweep chỉ giữ nguyên số i sai của VN cũ).

### 751 — romaji (ハチロク)
- JP: 「はっ――あむっ――ちゅっ――ちゅむうっ――ん……\nしゅ、きっ――ほーへふ……はふぁ、しゅき、しゅきぃ」
- TW: 「哈——啊姆——啾——啾嗯嗚——……喜歡——喜歡您……嗚啊，喜歡、喜歡」
- VN cũ: 「Ha——a mu——chụt——chu muu——ưm……\nyêu, ngài——ho he hu……ha hua, yêu, yêu ngài lắm」
- VN mới: 「Ha——a mu——chụt——chu muu——ưm……\nyêu, ngài——ho he phu……ha fua, yêu, yêu ngài lắm」
- Lý do: ふ trong ほーへふ → "phu"; ふぁ trong はふぁ → "fua".

### 754 — romaji (ハチロク)
- JP: 「はむっ！？　ん――ひゅっ――ん……れるっ――ろっ、\nちゅ――ちゅむっ――ほーへふ……んっ――はふぁぁ」
- TW: 「哈姆！？嗯——咻——……咻嚕——嚕，啾——啾姆——嗯—呼……——嗚啊啊」
- VN cũ: 「Ha mu!? Ưm——hyu——ưm……liếm——liếm,\nchu——chụt——ho he hu……ưm——ha huaa」
- VN mới: 「Ha mu!? Ưm——hyu——ưm……liếm——liếm,\nchu——chụt——ho he phu……ưm——ha fuaa」
- Lý do: ふ trong ほーへふ → "phu"; ふぁぁ → "fuaa" (2 a theo JP ぁぁ).

### 759 — romaji (ハチロク)
- JP: 「あ――出てッ――んっ――熱、い――んくっ――ふ――\n双鉄、さまの――精子――あつい、のっ――ふ、ふぁ」
- TW: 「啊——出來了——好熱——嗯——呼——雙鐵少爺的——精子——好熱——呼，嗚啊」
- VN cũ: 「A——ra rồi——ưm——nóng, quá——ưn ku——hu——\nTinh trùng——của Ngài Soutetsu——nóng, quá——hu, hua」
- VN mới: 「A——ra rồi——ưm——nóng, quá——ưn ku——phù——\nTinh trùng——của Ngài Soutetsu——nóng, quá——phù, fua」
- Lý do: ふ―― → "phù——"; ふ、ふぁ → "phù, fua".

### 761 — romaji (双鉄)
- JP: 「ぁ――ふあっ――」
- TW: 「啊——呼啊——」
- VN cũ: 「A——huaa——」
- VN mới: 「A——Fua——」
- Lý do: ふあっ → "Fua" (1 a; VN cũ "huaa" thừa 1 a).

### 762 — romaji (ハチロク)
- JP: 「あ――はっ――ひっ――いいっ！　きもちっ――ふ、あ\nきもちいっ――あ――おっぱい、も――おまんまん、も」
- TW: 「啊——哈——哈——好！舒服——呼，啊舒服——啊——乳房，和——小妹妹，都是」
- VN cũ: 「A——ha——hi——thích quá! Sướng——hu, a\nsướng quá——a——nhũ hoa, cũng——tiểu huyệt, cũng」
- VN mới: 「A——ha——hi——thích quá! Sướng——phù, a\nsướng quá——a——nhũ hoa, cũng——tiểu huyệt, cũng」
- Lý do: ふ、あ → "phù, a" (chỉ sửa phụ âm ふ).

### 771 — romaji (ハチロク)
- JP: 「あ……きゅっ――んっ――ふあっ――あっ――そうてつ、さまっ――わたくし――わたくしの――だんな、さまっ」
- TW: 「啊……呀——嗯——啊——雙鐵少爺——我——我的——夫君」
- VN cũ: 「A……kyu——ưm——huaa——a——Ngài Soutetsu——em——phu quân——của em」
- VN mới: 「A……kyu——ưm——Fua——a——Ngài Soutetsu——em——phu quân——của em」
- Lý do: ふあっ → "Fua" (1 a; VN cũ "huaa" thừa 1 a).

### 774 — romaji (双鉄)
- JP: 「あ……んっ――ふ……ん…………んっ」
- TW: 「啊……嗯——呼…………嗯」
- VN cũ: 「A……ưm——hu……ưm…………ưm」
- VN mới: 「A……ưm——phù……ưm…………ưm」
- Lý do: ふ…… → "phù……" (chỉ sửa phụ âm ふ).

### 780 — romaji (ハチロク)
- JP: 「は……むっ――ちゅ――ん――ほまはへふははひ、\nん……れるっ――ほーへふ……はまっ――ちゅっ！」
- TW: 「啊……姆——啾——齋一赤，嗯……咻嚕——讓偶——呼……來——啾！」
- VN cũ: 「Ha……ngoạm——chụt——ưm——ho ma ha he hu ha ha hi,\nƯm……liếm——ho he hu……ngoạm——chụt!」
- VN mới: 「Ha……ngoạm——chụt——ưm——ho ma ha he phu ha ha hi,\nƯm……liếm——ho he phu……ngoạm——chụt!」
- Lý do: ふ trong ほまはへふははひ và ほーへふ → "phu" (2 chỗ).

### 782 — đếm nguyên âm (双鉄)
- JP: 「ァぁっ――ン――くっ」
- TW: 「啊啊——嗯——嗯」
- VN cũ: 「Aaa——ưm——khục」
- VN mới: 「Aa——ưm——khục」
- Lý do: Đếm nguyên âm: JP ァぁ = 2 âm a (TW 啊啊 xác nhận); VN cũ "Aaa" có 3 chữ a — thừa 1. くっ → "khục" giữ nguyên (quy tắc "Kh" đã khóa).

### 798 — nghĩa (ハチロク)
- JP: 「じゅぼっ！　じゅぶっ！　れるっ！　れろおっ！\nじゅるるっ！　じゅ！　じゅぼっ！　ぶぢゅ！！」
- TW: 「啾啵！啾！咻嚕！嗯！啾嚕！啾！啾啵！噗啾！！」
- VN cũ: 「Nhóp nhép! Nhóp nhép! Liếm! Mút mát!\nChóp chép! Nhóp! Nhóp nhép! Bạch!!」
- VN mới: 「Nhóp nhép! Nhóp nhép! Liếm! Mút mát!\nChóp chép! Nhóp! Nhóp nhép! Bụp!!」
- Lý do: Sai âm SFX: ぶぢゅ là tiếng nút ướt (buju), không phải tiếng tát — "Bạch" sai hẳn âm; sửa thành "Bụp" (tiếng bật/nổ ướt, hợp chuỗi nhóp nhép/chóp chép).

### 809 — romaji (ハチロク)
- JP: 「ちゅっ！　ちゅむっ！　んっ――ちゅうっ――ふっ！\nれるっ――れろっ――ちゅううっ――ちゅむ、ちゅ！」
- TW: 「啾！啾姆！嗯——啾嗚——呼！咻嚕——嗯——啾嗚——啾嗯，啾！」
- VN cũ: （Chụt! Chụt! Ưm——chụt——hu!\nLiếm——liếm——chụttttt——chụt, chụt!）
- VN mới: （Chụt! Chụt! Ưm——chụt——phù!\nLiếm——liếm——chụttttt——chụt, chụt!）
- Lý do: ふっ → "phù" (tiền lệ h1). Dòng này VN dùng （） thay 「」 — giữ nguyên (xem mục giữ nguyên).

### 811 — đếm nguyên âm (ハチロク)
- JP: 「くひぃぃぃぃぃぃぃぃぃぃっ！！！」
- TW: 「嗚咿——！！！」
- VN cũ: 「Kuhiiiiiiiiiiiiiii!!!」
- VN mới: 「Kuhiiiiiiiiii!!!」
- Lý do: Đếm nguyên âm: JP くひぃぃぃぃぃぃぃぃぃぃ = く + ひ (1 i) + ぃ×9 → 10 chữ i; VN cũ "Kuhiiiiiiiiiiiiiii" có 15 chữ i — thừa 5.

### 812 — romaji (ハチロク)
- JP: 「ふぁ……あ…………あまざけ、い、っぱい――上の、\nおくちも……した、の……おくち、も――ふぁ」
- TW: 「嗚啊……啊……滿滿都是甜米酒——然後又親了……親過了——嗚啊」
- VN cũ: 「Hua……a…………đầy, ắp, rượu ngọt——Cái miệng,\nở trên……cái miệng, ở……dưới, cũng——hua」
- VN mới: 「Fua……a…………đầy, ắp, rượu ngọt——Cái miệng,\nở trên……cái miệng, ở……dưới, cũng——fua」
- Lý do: ふぁ → "Fua" (2 chỗ: đầu và cuối dòng).

### 813 — romaji (ハチロク)
- JP: 「ふぁ……ぁァ――――――あっ……全部……ぜん、ぶ\n――わたくし――全部を――旦那様、の――おくち、に」
- TW: 「嗚啊……啊啊——啊……全部……哦嗯，噗——我——全部——向夫君——口腔」
- VN cũ: 「Hua……aa——————a……Tất cả……toàn, bộ\n——Em——tất cả——vào miệng, của——phu quân」
- VN mới: 「Fua……aa——————a……Tất cả……toàn, bộ\n——Em——tất cả——vào miệng, của——phu quân」
- Lý do: ふぁ → "Fua". ぁァ → "aa" giữ nguyên (đúng 2 a).

### 821 — romaji (ハチロク)
- JP: 「ん……ふあっ――あっ――んくっ――おまん、まん――\nんっ――ひ――くっ――ぞりって――する、とこっ――」
- TW: 「嗯……呼啊——啊——嗯——小妹妹——嗯——咿——抽緊——被插的——部位——」
- VN cũ: 「Ưm……huaa——a——ưn ku——tiểu, huyệt——\nưm——hi——khục——bị chà xát——rồi——」
- VN mới: 「Ưm……Fua——a——ưn ku——tiểu, huyệt——\nưm——hi——khục——bị chà xát——rồi——」
- Lý do: ふあっ → "Fua" (1 a; VN cũ "huaa" thừa 1 a).

### 827 — romaji (ハチロク)
- JP: 「ん……ちゅっ――んんんっ――ふあっ――ふっ――\nちゅっ――チュムッ――れるっ、れろおっ、ん、ちゅっ」
- TW: 「嗯……啾——嗯嗯——呼啊——呼——啾——啾嗯——咻嚕，嗯，嗯，啾」
- VN cũ: 「Ưm……chụt——ưm ưm——huaa——hu——\nchụt——chụt——liếm, mút mát, ưm, chụt」
- VN mới: 「Ưm……chụt——ưm ưm——Fua——phù——\nchụt——chụt——liếm, mút mát, ưm, chụt」
- Lý do: ふあっ → "Fua"; ふっ → "phù".

### 829 — romaji (ハチロク)
- JP: 「ん……ちゅるっ――ちゅ――れるっ――れろ……ぺろっ\n――ふ……ん……ハムッ――はむっ――ちゅ、ちゅるる」
- TW: 「嗯……啾嚕——啾——咻嚕——嗯……——呼……啊姆——姆——啾，啾嚕嚕」
- VN cũ: 「Ưm……chụt——chụt——liếm——mút……liếm láp\n——hu……ưm……Ngậm——ngoạm——chụt, chụt chụt」
- VN mới: 「Ưm……chụt——chụt——liếm——mút……liếm láp\n——phù……ưm……Ngậm——ngoạm——chụt, chụt chụt」
- Lý do: ふ…… → "phù……" (chỉ sửa phụ âm ふ).

### 830 — romaji (ハチロク)
- JP: 「ん……ふぅ――。うふふ、ごちそうさまでした。\n大変、結構なお点前で」
- TW: 「嗯……嗚——。呵呵，承蒙款待。真是美酒啊」
- VN cũ: 「Ưm……huu——. Ufufu, cảm ơn ngài vì bữa ăn.\nQuả là một thức uống tuyệt hảo.」
- VN mới: 「Ưm……phuu——. Ufufu, cảm ơn ngài vì bữa ăn.\nQuả là một thức uống tuyệt hảo.」
- Lý do: ふぅ → "phuu" (2 u đúng số lượng; chỉ sửa phụ âm h→ph). うふふ → "Ufufu" giữ nguyên (tiếng cười, không phải rên).

### 831 — romaji (ハチロク)
- JP: 「ん……でゅほっ――ちゅっ――ふっ――ろーろ――ん、\nふっ――ほふ、ひひ――ちゅむっ――ほーへふ、ははっ」
- TW: 「嗯……嗚嗯——啾——呼——嚕—嚕——呼——嘿，嘿嘿——啾姆——嗚—呼，哈」
- VN cũ: 「Ưm……dyu ho——chụt——hu——ro ro——ưm,\nhu——ho hu, hi hi——chụt——ho he hu, ha ha」
- VN mới: 「Ưm……dyu ho——chụt——phù——ro ro——ưm,\nphù——ho phu, hi hi——chụt——ho he phu, ha ha」
- Lý do: ふっ → "phù" (2 chỗ); ふ trong ほふ và ほーへふ → "phu" (2 chỗ).

### 835 — gasp (ハチロク)
- JP: 「っきゅううううううっっ！！」
- TW: 「嗯嗚——！！」
- VN cũ: 「Kyuuuuuu!!」
- VN mới: 「ƯKyuuuuuuu!!」
- Lý do: Gasp + đếm nguyên âm: JP mở đầu bằng っ (gasp đầu dòng, sweep bỏ sót — tiền lệ sweep lr_稀咲追加h 1124: mỗi っ đầu dòng → một Ư) nên thêm Ư; きゅうううううう = きゅ + う×6 → 7 chữ u, VN cũ "Kyuuuuuu" chỉ có 6 — thiếu 1. っっ cuối dòng bỏ theo tiền lệ h1 1238 (っ sau nguyên âm dài không diễn Ư).

### 836 — đếm nguyên âm (ハチロク)
- JP: 「んきゅうううううううううううっっっっっ！！！！」
- TW: 「嗯嗚——！！！！」
- VN cũ: 「Ưn kyuuuuuuuuuuuuuuuuuuuuuuuuuu!!!!」
- VN mới: 「Ưn kyuuuuuuuuuuuu!!!!」
- Lý do: Đếm nguyên âm: JP んきゅううううううううううう = きゅ + う×11 → 12 chữ u; VN cũ có 26 chữ u — thừa 14. っっっっっ cuối dòng bỏ theo tiền lệ h1 1238.

### 843 — romaji (ハチロク)
- JP: 「んむっ！？　ん……ふ……ん――ごく――ごく――\nじゅうう――じゅる――ごくっ――ごくんっ！　ごくっ」
- TW: 「嗯姆！？嗯……呼……——嗚——嗚——啾嗚——啾嚕——嗯——嗯！嗯」
- VN cũ: 「Ưm mu!? Ưm……hu……ưm——ực——ực——\nchụttttt——chóp chép——ực——ực! Ực」
- VN mới: 「Ưm mu!? Ưm……phù……ưm——ực——ực——\nchụttttt——chóp chép——ực——ực! Ực」
- Lý do: ふ…… → "phù……" (chỉ sửa phụ âm ふ).

### 855 — romaji (ハチロク)
- JP: 「しょこ――しゅご――んっ――ふあっ――すご――\nすご――すぎって――んうっ――わたく、し――回路っ」
- TW: 「好棒——好棒——呼啊——好棒啊——太厲害了——嗚——我的——迴路」
- VN cũ: 「Chỗ đó——tuyệt quá——ưm——huaa——tuyệt quá——\ntuyệt quá——mất——ưm u——em——mạch điện」
- VN mới: 「Chỗ đó——tuyệt quá——ưm——Fua——tuyệt quá——\ntuyệt quá——mất——ưm u——em——mạch điện」
- Lý do: ふあっ → "Fua" (1 a; VN cũ "huaa" thừa 1 a).

### 857 — romaji (ハチロク)
- JP: 「お、まん、まん――ふぁ――おぼれ――おぼれ、りゅっ\n――んっ！　双鉄、さまの――精子、で、たぷたぷっ」
- TW: 「小妹妹——嗚啊——泡——泡在精液裡——！雙鐵少爺的——精子，滿滿的都是」
- VN cũ: 「Tiểu huyệt——hua——ngập——ngập, rồi\n——Ưm! Tinh trùng——của Ngài Soutetsu, đầy ăm ắp」
- VN mới: 「Tiểu huyệt——Fua——ngập——ngập, rồi\n——Ưm! Tinh trùng——của Ngài Soutetsu, đầy ăm ắp」
- Lý do: ふぁ → "Fua".

### 870 — đại từ (双鉄)
- JP: 「文献で読んだのだがな。\nこれは、わかめ酒という行為らしい」
- TW: 「我在文獻裡讀到過，這個好像叫裙帶菜酒」
- VN cũ: 「Anh có đọc được trong tài liệu.\nHành động này, có vẻ được gọi là rượu rong biển (Wakame-zake) đấy.」
- VN mới: 「Tôi có đọc được trong tài liệu.\nHành động này, có vẻ được gọi là rượu rong biển (Wakame-zake) đấy.」
- Lý do: Đại từ: Soutetsu nói với Hachiroku → xưng "tôi" (quy tắc đã sửa 20/11: "tôi" với Hachiroku; "anh" chỉ với Hibiki/Michiko/Paulette/Reina/Fukami/Nagi).

### 871 — đại từ (双鉄)
- JP: 「わかっているさ」
- TW: 「我明白」
- VN cũ: 「Anh biết mà.」
- VN mới: 「Tôi biết mà.」
- Lý do: Đại từ: như 870 — Soutetsu với Hachiroku → "tôi".

### 872 — đại từ (双鉄)
- JP: 「可愛いな。僕の姫君は」
- TW: 「我的小公主，你真可愛」
- VN cũ: 「Đáng yêu quá. Công chúa của anh」
- VN mới: 「Đáng yêu quá. Công chúa của tôi」
- Lý do: Đại từ: 僕の姫君 = "công chúa của tôi" — sở hữu cách cũng theo quy tắc xưng hô với Hachiroku.

### 874 — đại từ (双鉄)
- JP: 「知っている。ゆえ、飲むのは僕だが――\nすずにもたっぷり、楽しんで欲しいと思っている」
- TW: 「我知道，所以就我喝。但我也想讓你好好享受」
- VN cũ: 「Anh biết. Vì thế, người uống là anh nhưng——\nAnh cũng muốn Suzu được tận hưởng trọn vẹn.」
- VN mới: 「Tôi biết. Vì thế, người uống là tôi nhưng——\nTôi cũng muốn Suzu được tận hưởng trọn vẹn.」
- Lý do: Đại từ: 3 chỗ "anh" trong cùng một dòng Soutetsu → "tôi" (với Hachiroku).

### 876 — đại từ (双鉄)
- JP: 「抉って、こすって、射精するまで止まらない。\nすずのちいさなおまんまんを、僕の形に変えてしまう」
- TW: 「我要鑽進去、摩擦下去，不射精不停止。讓你的小妹妹，變成我的形狀」
- VN cũ: 「Khoét sâu, cọ xát, sẽ không dừng lại cho đến khi xuất tinh.\nAnh sẽ biến tiểu huyệt nhỏ bé của Suzu thành hình dạng của anh.」
- VN mới: 「Khoét sâu, cọ xát, sẽ không dừng lại cho đến khi xuất tinh.\nTôi sẽ biến tiểu huyệt nhỏ bé của Suzu thành hình dạng của tôi.」
- Lý do: Đại từ: "Anh sẽ biến… thành hình dạng của anh" → "Tôi sẽ biến… thành hình dạng của tôi" (với Hachiroku).

### 878 — nghĩa (ハチロク)
- JP: 「すずは、全部を――双鉄、さま――にっ――んっ！\n染めて――作り変えて――いただき、たい――ですっ！」
- TW: 「我，的全部——都是您的——嗯——！讓我——染上您的色彩——變成您的模樣吧——！」
- VN cũ: 「Suzu muốn, tất cả——Ngài Soutetsu——ưm!\nNhuốm màu——tạo hình lại——cho em——!」
- VN mới: 「Suzu muốn, tất cả——Ngài Soutetsu——!\nNhuốm màu——tạo hình lại——cho em——!」
- Lý do: Nghĩa: にっ là tiểu từ に + っ nhấn mạnh (câu chưa dứt, tiếp nối ở dòng sau), không phải tiếng rên — VN cũ diễn thành "ưm" là bịa thêm âm; gỡ "ưm", chỉ giữ dấu gạch diễn chỗ ngắt.

### 885 — đại từ (双鉄)
- JP: 「そうだな――僕もだ。\n僕も、お前に恋をしている」
- TW: 「是啊——我也是。我也是那麼得喜歡你」
- VN cũ: 「Đúng vậy nhỉ——Anh cũng thế.\nAnh cũng, đang yêu em say đắm.」
- VN mới: 「Đúng vậy nhỉ——Tôi cũng thế.\nTôi cũng, đang yêu em say đắm.」
- Lý do: Đại từ: 僕もだ ×2 → "Tôi cũng thế / Tôi cũng, đang yêu em" (với Hachiroku).

### 905 — đại từ (双鉄)
- JP: 「焼ききって、新しい線をつないでしまえ」
- TW: 「燒掉了就再重新接線吧」
- VN cũ: 「Cháy rụi luôn đi, rồi anh sẽ nối lại dây mới cho em.」
- VN mới: 「Cháy rụi luôn đi, rồi tôi sẽ nối lại dây mới cho em.」
- Lý do: Đại từ: "anh sẽ nối lại dây mới cho em" — Soutetsu tự xưng với Hachiroku → "tôi".

### 929 — đại từ (双鉄)
- JP: 「溺れてしまえ。僕に――どこまでも――どこまでもっ」
- TW: 「那就沉溺吧。沉溺在我的精液裡，永遠永遠」
- VN cũ: 「Cứ ngập chìm đi. Trong anh——mãi mãi——mãi mãi」
- VN mới: 「Cứ ngập chìm đi. Trong tôi——mãi mãi——mãi mãi」
- Lý do: Đại từ: 僕に溺れてしまえ = "chìm đắm trong tôi" — "Trong anh" → "Trong tôi" (với Hachiroku).

### 936 — đại từ (双鉄)
- JP: 「すず――頼むっ」
- TW: 「鈴——拜託了」
- VN cũ: 「Suzu——Anh xin em đấy」
- VN mới: 「Suzu——Tôi xin em đấy」
- Lý do: Đại từ: Soutetsu xin Hachiroku → "Tôi xin em đấy".

### 946 — romaji (ハチロク)
- JP: 「そうてつ――さまっ――ふぁっ――双鉄、さまあっ！」
- TW: 「雙鐵少爺——嗚啊——雙鐵少爺！」
- VN cũ: 「Ngài Soutetsu——huaa——Ngài Soutetsu!」
- VN mới: 「Ngài Soutetsu——Fua——Ngài Soutetsu!」
- Lý do: ふぁっ → "Fua" (1 a; VN cũ "huaa" thừa 1 a).

### 951 — gasp (双鉄)
- JP: 「っ！」
- TW: 「！」
- VN cũ: 「っ!」
- VN mới: 「Ư!」
- Lý do: Gasp sweep: JP chỉ có một っ (raw-tsu) — VN cũ còn giữ nguyên chữ っ Nhật; sửa thành "Ư!" theo sweep.

### 952 — gasp (双鉄)
- JP: 「っ！！？」
- TW: 「！！？」
- VN cũ: 「!!?」
- VN mới: 「Ư!!?」
- Lý do: Gasp sweep: JP là gasp toàn dòng (っ！！？) — VN cũ chỉ có dấu câu; thêm Ư theo sweep (lost-gasp-whole).

### 953 — gasp (ハチロク)
- JP: 「っっっっっ～～～～～～～っ！！！」
- TW: 「～～～～～～～！！！」
- VN cũ: 「~~~~~~~~~!!!」
- VN mới: 「ƯƯƯƯƯ~~~~~~~Ư!!!」
- Lý do: Gasp sweep (đã sửa lại số lượng): JP っ×5 + ～×7 + っ — sweep ghi 9 dấu ~ là sai (VN cũ cũng sai 9); sửa thành 5 Ư + 7 ~ + 1 Ư.

### 1162 — nghĩa (monologue)
- JP: 唾液にさえも、酔わされていく。\n体温と匂いに、散らされていく。
- TW: 唾液使我沉醉。體溫和氣味讓我升天。
- VN cũ: Ngay cả nước bọt cũng làm tôi say đắm.\nTôi đang bị phân tâm bởi nhiệt độ cơ thể và mùi hương.
- VN mới: Ngay cả nước bọt cũng làm tôi say đắm.\nTôi đang tan ra bởi nhiệt độ cơ thể và mùi hương.
- Lý do: Nghĩa: 体温と匂いに、散らされていく = "bị nhiệt độ cơ thể và mùi hương làm tan ra/rã ra" (TW 升天 — ngây ngất, tan biến); VN cũ "bị phân tâm" (分心) là diễn khác động từ 散らす — sửa thành "tan ra", khôi phục song song với dòng trên ("làm tôi say đắm").

### 1225 — gasp (monologue)
- JP: 気持ち良すぎて、もっと気持ちよくなりたくて、\n僕の全部が、もうカラカラに乾いてしまっ――っ！！？
- TW: 實在是太舒服了，我甚至還想要更舒服，我全身都飢渴難耐了——嗯！！？
- VN cũ: Quá sung sướng, muốn được sung sướng hơn nữa,\ntoàn bộ cơ thể tôi đã khô khốc cả rồi——!!?
- VN mới: Quá sung sướng, muốn được sung sướng hơn nữa,\ntoàn bộ cơ thể tôi đã khô khốc cả rồi——Ư!!?
- Lý do: Gasp sweep: JP しまっ――っ — っ gasp sau gạch bị rớt; thêm Ư theo sweep (lost-gasp-trailing). しまっ là っ nhấn mạnh gắn từ có nội dung, không thêm Ư.

### 1253 — đại từ (monologue)
- JP: 僕もだ、と、言葉のかわりに舌を動かし、\nすずの小さな口内の、すみずみまでを舐めまくる。
- TW: 我也不說話，而是用舌頭舔遍了她小嘴裡的每一個角落。
- VN cũ: Anh cũng vậy, thay vì dùng lời nói, tôi cử động lưỡi,\nliếm láp khắp mọi ngóc ngách trong khoang miệng nhỏ bé của Suzu.
- VN mới: Tôi cũng vậy, thay vì dùng lời nói, tôi cử động lưỡi,\nliếm láp khắp mọi ngóc ngách trong khoang miệng nhỏ bé của Suzu.
- Lý do: Đại từ: độc thoại Soutetsu — "Anh cũng vậy" mâu thuẫn với "tôi cử động lưỡi" ngay trong cùng câu; độc thoại luôn xưng "tôi" → "Tôi cũng vậy".

### 1274 — gasp (monologue)
- JP: 言われたことを理解して、\nぶわりよろこびが膨れ上がって――っ！！？
- TW: 我懂她嘟嘟囔囔說了什麼，心裡的高興勁一下湧上了天——！！？
- VN cũ: Hiểu được những gì em nói,\nniềm sung sướng trong tôi chợt trào dâng mạnh mẽ——!!?
- VN mới: Hiểu được những gì em nói,\nniềm sung sướng trong tôi chợt trào dâng mạnh mẽ——Ư!!?
- Lý do: Gasp sweep: JP 膨れ上がって――っ — thêm Ư theo sweep (lost-gasp-trailing).

### 1276 — gasp (monologue)
- JP: 満足感と達成感とに満ち満ちながら、\n収縮してる膣道が、緩むまでじっと動かずに――っ！？
- TW: 我懷著無比的滿足感和成就感，收縮的陰道一動也不動了好一會——
- VN cũ: Tràn ngập cảm giác thỏa mãn và thành tựu,\ntôi nằm yên bất động cho đến khi đường âm đạo đang co thắt nới lỏng ra——!?
- VN mới: Tràn ngập cảm giác thỏa mãn và thành tựu,\ntôi nằm yên bất động cho đến khi đường âm đạo đang co thắt nới lỏng ra——Ư!?
- Lý do: Gasp sweep: JP 動かずに――っ — thêm Ư theo sweep (lost-gasp-trailing).

### 1300 — đại từ (monologue)
- JP: 承知の上だ、とこたえる代わりに、舌の動きを強くする。
- TW: 我知道，所以我才要這麼做啊。我舌頭的動作更用力了。
- VN cũ: Thay cho câu trả lời "Anh biết rõ điều đó mà", tôi cử động lưỡi mạnh bạo hơn.
- VN mới: Thay cho câu trả lời "Tôi biết rõ điều đó mà", tôi cử động lưỡi mạnh bạo hơn.
- Lý do: Đại từ: độc thoại trích lời tự nhủ của Soutetsu (承知の上だ = "tôi biết rõ") — "Anh biết rõ điều đó mà" → "Tôi biết rõ điều đó mà".

### 1304 — đại từ (monologue)
- JP: 本気で行くぞ、の思いを込めて、\n舌でクリトリスに軽く触れれば、可愛い声が応じてくれる。
- TW: 我舔了舔她的陰蒂，告訴她“我要認真了”。她很可愛地驚叫了一下，看來是知道。
- VN cũ: Chứa đựng ý nghĩ "Anh sẽ làm thật đấy",\ntôi khẽ chạm lưỡi vào âm vật, và một giọng nói đáng yêu đã đáp lại.
- VN mới: Chứa đựng ý nghĩ "Tôi sẽ làm thật đấy",\ntôi khẽ chạm lưỡi vào âm vật, và một giọng nói đáng yêu đã đáp lại.
- Lý do: Đại từ: độc thoại trích ý nghĩ của Soutetsu (本気で行くぞ = "tôi sẽ làm thật") — "Anh sẽ làm thật đấy" → "Tôi sẽ làm thật đấy".

## Khối TOML đã kiểm chứng (63 khóa, parse OK, 0 sai lệch giá trị)

```toml
[script]
"467" = "「——Ư!!!!」"
"703" = "「Kyafu!? A! Tiểu huyệt——ưm!!\\nEm——tiểu huyệt——của em——Fua」"
"705" = "「Hyua!? Ưm——giật giật! Phồng lên rồi!!\\nCôn thịt——của Ngài Soutetsu!! Fua!」"
"706" = "「Hyagyu!? Phù——Fua!? A——\\nnhũ hoa——Ư! A, núm vú——kích thích, ưm, phù」"
"708" = "「Hya! A!? Bị mút rồi——hạt đậu... Fua!\\nTiểu huyệt——a……tiếng——chóp chép——xấu hổ, quá——ưm」"
"709" = "「Hyua!!? Ch, chỗ đóoooo!!」"
"724" = "「Ho he phu ha fua——ưm……ho ho,\\nwa ra phu hi hi……ha fua fua e, ho——」"
"726" = "「Fuaa!!!」"
"728" = "「Fua——a——a——a——Ngài, Soutetsu,\\nNgài Soutetsu——Ngài Soutetsu!!」"
"729" = "「Fua!」"
"731" = "「Fua! A——phù——Ngài Soutetsu——\\nNgài Soutetsu——!」"
"732" = "「Fua!? Chỗ đó! A——a——ưm——!\\nƯn ku~~~~~~~~~~~~~~~~~!!!」"
"734" = "「Phuuuuuu!?」"
"736" = "「I——kyuuuuuuuuuuuu!!!!」"
"737" = "「Hia! A——a——ưn ku!! Phù!」"
"743" = "「Hia!? Không chịu đâu——cố tình——phu, a——\\nƯm——cố tình, tạo ra âm thanh——dâm đãng, như vậy——khục!」"
"746" = "「Iun!? A——Hút, hút mất rồi——hi——kyu! Fua\\n——Nước, tiểu——tất cả——cả phần còn lại——cũng bị hút ra, hết」"
"749" = "「Iiiiiiiiiiiii~~~~~Ư!!!!」"
"751" = "「Ha——a mu——chụt——chu muu——ưm……\\nyêu, ngài——ho he phu……ha fua, yêu, yêu ngài lắm」"
"754" = "「Ha mu!? Ưm——hyu——ưm……liếm——liếm,\\nchu——chụt——ho he phu……ưm——ha fuaa」"
"759" = "「A——ra rồi——ưm——nóng, quá——ưn ku——phù——\\nTinh trùng——của Ngài Soutetsu——nóng, quá——phù, fua」"
"761" = "「A——Fua——」"
"762" = "「A——ha——hi——thích quá! Sướng——phù, a\\nsướng quá——a——nhũ hoa, cũng——tiểu huyệt, cũng」"
"771" = "「A……kyu——ưm——Fua——a——Ngài Soutetsu——em——phu quân——của em」"
"774" = "「A……ưm——phù……ưm…………ưm」"
"780" = "「Ha……ngoạm——chụt——ưm——ho ma ha he phu ha ha hi,\\nƯm……liếm——ho he phu……ngoạm——chụt!」"
"782" = "「Aa——ưm——khục」"
"798" = "「Nhóp nhép! Nhóp nhép! Liếm! Mút mát!\\nChóp chép! Nhóp! Nhóp nhép! Bụp!!」"
"809" = "（Chụt! Chụt! Ưm——chụt——phù!\\nLiếm——liếm——chụttttt——chụt, chụt!）"
"811" = "「Kuhiiiiiiiiii!!!」"
"812" = "「Fua……a…………đầy, ắp, rượu ngọt——Cái miệng,\\nở trên……cái miệng, ở……dưới, cũng——fua」"
"813" = "「Fua……aa——————a……Tất cả……toàn, bộ\\n——Em——tất cả——vào miệng, của——phu quân」"
"821" = "「Ưm……Fua——a——ưn ku——tiểu, huyệt——\\nưm——hi——khục——bị chà xát——rồi——」"
"827" = "「Ưm……chụt——ưm ưm——Fua——phù——\\nchụt——chụt——liếm, mút mát, ưm, chụt」"
"829" = "「Ưm……chụt——chụt——liếm——mút……liếm láp\\n——phù……ưm……Ngậm——ngoạm——chụt, chụt chụt」"
"830" = "「Ưm……phuu——. Ufufu, cảm ơn ngài vì bữa ăn.\\nQuả là một thức uống tuyệt hảo.」"
"831" = "「Ưm……dyu ho——chụt——phù——ro ro——ưm,\\nphù——ho phu, hi hi——chụt——ho he phu, ha ha」"
"835" = "「ƯKyuuuuuuu!!」"
"836" = "「Ưn kyuuuuuuuuuuuu!!!!」"
"843" = "「Ưm mu!? Ưm……phù……ưm——ực——ực——\\nchụttttt——chóp chép——ực——ực! Ực」"
"855" = "「Chỗ đó——tuyệt quá——ưm——Fua——tuyệt quá——\\ntuyệt quá——mất——ưm u——em——mạch điện」"
"857" = "「Tiểu huyệt——Fua——ngập——ngập, rồi\\n——Ưm! Tinh trùng——của Ngài Soutetsu, đầy ăm ắp」"
"870" = "「Tôi có đọc được trong tài liệu.\\nHành động này, có vẻ được gọi là rượu rong biển (Wakame-zake) đấy.」"
"871" = "「Tôi biết mà.」"
"872" = "「Đáng yêu quá. Công chúa của tôi」"
"874" = "「Tôi biết. Vì thế, người uống là tôi nhưng——\\nTôi cũng muốn Suzu được tận hưởng trọn vẹn.」"
"876" = "「Khoét sâu, cọ xát, sẽ không dừng lại cho đến khi xuất tinh.\\nTôi sẽ biến tiểu huyệt nhỏ bé của Suzu thành hình dạng của tôi.」"
"878" = "「Suzu muốn, tất cả——Ngài Soutetsu——!\\nNhuốm màu——tạo hình lại——cho em——!」"
"885" = "「Đúng vậy nhỉ——Tôi cũng thế.\\nTôi cũng, đang yêu em say đắm.」"
"905" = "「Cháy rụi luôn đi, rồi tôi sẽ nối lại dây mới cho em.」"
"929" = "「Cứ ngập chìm đi. Trong tôi——mãi mãi——mãi mãi」"
"936" = "「Suzu——Tôi xin em đấy」"
"946" = "「Ngài Soutetsu——Fua——Ngài Soutetsu!」"
"951" = "「Ư!」"
"952" = "「Ư!!?」"
"953" = "「ƯƯƯƯƯ~~~~~~~Ư!!!」"
"1162" = "Ngay cả nước bọt cũng làm tôi say đắm.\\nTôi đang tan ra bởi nhiệt độ cơ thể và mùi hương."
"1225" = "Quá sung sướng, muốn được sung sướng hơn nữa,\\ntoàn bộ cơ thể tôi đã khô khốc cả rồi——Ư!!?"
"1253" = "Tôi cũng vậy, thay vì dùng lời nói, tôi cử động lưỡi,\\nliếm láp khắp mọi ngóc ngách trong khoang miệng nhỏ bé của Suzu."
"1274" = "Hiểu được những gì em nói,\\nniềm sung sướng trong tôi chợt trào dâng mạnh mẽ——Ư!!?"
"1276" = "Tràn ngập cảm giác thỏa mãn và thành tựu,\\ntôi nằm yên bất động cho đến khi đường âm đạo đang co thắt nới lỏng ra——Ư!?"
"1300" = "Thay cho câu trả lời \"Tôi biết rõ điều đó mà\", tôi cử động lưỡi mạnh bạo hơn."
"1304" = "Chứa đựng ý nghĩ \"Tôi sẽ làm thật đấy\",\\ntôi khẽ chạm lưỡi vào âm vật, và một giọng nói đáng yêu đã đáp lại."
```

## Giữ nguyên có lý do

- あっ/ああっ/はっ bare → "A"/"Aa" (không thêm Ư): tiền lệ h1 1251/1257/1263/1264 — っ ngắt nguyên âm đã diễn bằng dấu câu/gạch (787, 790, 752, 761, 886, 764).
- っ nhấn mạnh gắn từ có nội dung, không thêm Ư: 1150 やめずにっ, 1317 刺激してくれるっ, 1418 変化させっ, 890 望みますっ, 922 おもらし――してっ (tiền lệ sweep: ブロワーっ).
- っ cuối dòng sau nguyên âm dài (っっ/っっっっっ) bỏ, không thêm Ư: 722, 736, 836, 1581, 1588 (tiền lệ h1 1238 んくうっっっっっっっ → "Nkuu").
- 732 んく～～～っ → "Ưn ku~~~~~" giữ nguyên theo sweep (already-rendered); 1584 (もみゅ！むにゅっ！にゅるっ！さすすす～～っ) giữ nguyên theo sweep.
- ひあ/ひゃ → romaji sẵn: "Hia/Hya/Hyua/Hyagyu" (705, 709, 711, 713, 715, 737, 738, 740, 742, 743, 816, 927); ひうっ → "hiu" (927); ひぎゅううっ → "Higyuuu" (748, đúng 3 u); くあああっ → "Kuaaa" (784, đúng 3 a).
- "Kh" tắc thanh quản giữ: 782 くっ → "khục" (quy tắc đã khóa, không đổi thành Ư).
- ふっ → "phù" đã đúng sẵn ở 767 — giữ nguyên.
- 681 は――ふ、か―― → "hu, a" giữ nguyên: nói ngọng, không đối chiếu được từng âm tiết (TW cũng nén thành một âm tiết 呼).
- 776 câu JP cụt (お顔があまり…) — VN hoàn thiện theo TW ("không nhìn rõ mặt phu quân") — TW đồng ý, không phải bịa.
- 796/809 VN dùng （） thay 「」 cho dòng thuần SFX — giữ nguyên (ghi chú định dạng, không phải lỗi nội dung).
- 798 ぶぢゅ đã sửa; các SFX ngoặc còn lại diễn đúng âm/nghĩa (1524–1594).
- 1152 "Nhịp hít vào thở ra của em" giữ nguyên: chủ ngữ "của em" (Suzu) suy từ mạch văn (1150 nói về lưỡi Suzu), không mâu thuẫn JP/TW.
- 1162 đã sửa; 1213 "thè lưỡi liếm lấy nó" giữ nguyên (ぺろりと hỗ trợ); 1424 "trần âm đạo" giữ nguyên (天井 = vách trên); 1452 chủ ngữ "em" giữ nguyên (TW xác nhận Suzu là chủ ngữ).
- 861 tag ruby JP `[なか,1]` — VN bỏ tag, dịch đúng "bên trong âm đạo" (chuẩn hóa, không tính lỗi); 908/913/870 chú thích romaji trong ngoặc (Hinamatsuri/Amazake/Wareme-zake/Wakame-zake) giữ nguyên — đúng romaji, phong cách nhất quán của file.
- 783/815 ああ → "À" giữ nguyên: tiếng thở dài của Soutetsu diễn thành thán từ Việt, không phải rên cần đếm âm.
- 709 đã sửa đếm o; 1541 ちょおお… → "tràoooooooooooo" đúng 12 chữ o — giữ nguyên.
- 1552 ぺたっ → "Khựng lại" giữ nguyên: diễn theo sự kiện (dòng chảy dừng lại), trong phạm vi tự do của SFX.

## Cờ cho Hieu

- 798 ぶぢゅ → "Bụp": phán đoán âm thanh (tiếng nút ướt) — nếu muốn giữ "Bạch" thì nói lại.
- 1162 散らされていく → "tan ra": phán đoán nghĩa ("bị phân tâm" cũ diễn khác động từ gốc) — có TW 升天 hỗ trợ.
- 878 gỡ "ưm" ở にっ: phán đoán theo tiền lệ (tiểu từ + っ thì bỏ, không diễn thành tiếng rên) — nếu muốn giữ tiếng rên ngắt câu thì nói lại.
- B19 vẫn park (kiểm tra trong game tại Paulette 13 key 1596 trước đợt quét thẻ %l).

## Lượt soát 2

- 63/63 tái kiểm chứng đối chiếu JP, 0 bỏ, 0 sửa. (Lượt 1: đọc toàn bộ 332 dòng; lượt 2: đọc lại toàn bộ 63 fix kèm JP/TW, đối chiếu đếm nguyên âm bằng cơ học.)

## Kiểm chứng

- JSON 63 mục dạng chuẩn (list of dicts), khóa chuỗi; khối TOML 63 khóa, parse OK (tomllib), 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 63/63; mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (đã kiểm chứng bằng diff cơ học).
- Cơ sở tổng đã xác minh lại từ ROUTE-AUDIT.md: 150 file / 6.658 dòng sai.

## Kết bài

File ハチロクh8_桜色のひめごと: 332 dòng đã đọc hết, 63 dòng sai (19,0%) — lỗi tập trung ở tiếng rên (48/63: romaji 34, gasp 9, đếm nguyên âm 5) với một lỗi hệ thống (mọi ふ/ふぁ diễn thành "hu/hua"), 12 dòng đại từ Soutetsu "anh"→"tôi" với Hachiroku, 3 dòng nghĩa. Không lệch vị trí, không xoay chuỗi, không nhiễm chéo, không mồ côi, không dòng chưa dịch, không trùng khóa. Không có mục mới cho đợt unification. Cơ sở tổng đã xác minh lại từ ROUTE-AUDIT.md: 150 file / 6.658 dòng sai.

**Tổng cộng sau file này: 151 file / 6.721 dòng sai** (cơ sở 150 file / 6.658 dòng sai + 63 file này)
