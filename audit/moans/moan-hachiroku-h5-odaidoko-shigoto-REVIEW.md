# Moan fix — ハチロクh5_おだいどこしごと.txt.toml (moan-hachiroku-h5-odaidoko-shigoto)

- File: `ハチロクh5_おだいどこしごと.txt.toml` — route 01_Hachiroku, **291 dòng script**.
- Nội dung: Hachiroku học nấu ăn, làm tình trong bếp với Soutetsu (tạp dề khỏa thân), tè dầm khi lên đỉnh, làm tình lần hai, thề hẹn "mãi mãi về sau" (theo audit).
- Audit của file: 27/291 dòng sai (9,3%), toàn bộ SFX/gasp — xem `audit-hachiroku-h5-odaidoko-REVIEW.md`.

## 1. Xác minh tệp và nguồn

- TOML md5 `4f711f40ec474cb1d9de27daee7eda85` (khớp md5 audit), BOM + CRLF, `[selections]` rỗng. Không có bản sao trong 227 tệp TOML-2.
- CSV3: **1 set duy nhất** (291 dòng, 0 key trùng). VN khớp TOML tuyệt đối sau khi gộp `\n` thành khoảng trắng ở 148 dòng (hiện tượng TOML-2 đã biết, audit §1) — 0 khác biệt thực chất. **Lưu ý:** tên file trên đĩa dùng `#U3053` (ど) — đường dẫn trong lệnh spawn ghi `#U3069` là sai chính tả, file thật đã xác minh bằng md5.
- Sweep: **6 mục** cho file trong `sweep-raw-gasp-wrong.json` (992, 1031, 1064, 1065, 1401, 1416 — toàn `lost-gasp-trailing`), audit đã áp nguyên cả 6. Moan-pass này **không đụng** 6 mục đó: 992/1031/1064/1065 giữ nguyên Ư cuối dòng; 1401/1416 không đổi.
- Không có dòng "Kh" nào trong file (quét toàn file: chỉ có từ Việt chứa "kh" như "không", "Kh-Không").
- Cơ sở tổng moan (đọc trực tiếp `moans/ROUTE-MOANS.md`): **33 file / 771 dòng**.

## 2. Danh sách rên (moan inventory)

- Đã đọc **291/291 dòng**; xét **134 dòng rên/SFX** (87 dòng thoại có âm rên/SFX + 47 dòng SFX độc thoại （）); **sửa 28, giữ 106**.
- Phân loại 28 dòng sửa: romaji 25, SFX 3. Theo token (một dòng có thể mang nhiều token, các nhóm chồng nhau): họ fa/fu → romaji 12 dòng (1006, 1008, 1010, 1011, 1033, 1064, 1065, 1070 ぷあ, 1073, 1089, 1178, 1222); họ ひゃ/ひゅ/ひあ → romaji 6 dòng (996, 1000, 1012, 1013, 1073, 1077); rên dài một hơi gộp từ dạng tách mảnh 8 dòng (996, 998, 1010, 1067, 1073, 1075, 1077, 1222); mất phụ âm mora や/く/か/んふ 10 dòng (759, 992, 995, 998, 1020, 1031, 1070, 1074, 1181, 1227).
- Theo nhân vật: ハチロク 25, 双鉄H 3 (1070, 1075, 1181).
- 16/28 key trùng với fix audit — fix moan **thay thế** fix audit ở đúng token rên (giữ nguyên phần còn lại của fix audit). 12 key audit không chạm (995, 1012, 1020, 1074, 1178, 1181 + 759/992/998/1031/1064/1065 chỉ đổi token や/fa trong fix audit) — xem chi tiết từng dòng.

## 3. Chi tiết từng dòng sửa (28 dòng)

#### 759 — ハチロク — や…… → "Ya……"
- **JP:** 「や……ごめんなさいっ――ごめんな、さいっ――\nわ、わたくし――粗相――そそうを、してっ――んうっ」
- **TW:** 「……對不起——對不起——我、我——失禁——失禁了——嗚」
- **VN cũ (CSV3):** 「Á……em xin lỗi——em xin, lỗi——\ne-em——đã tè dầm——tè dầm mất rồi——ưm.」
- **Mới:** 「Ya……em xin lỗi——em xin, lỗi——⏎ e-em——đã tè dầm——tè dầm mất rồi——ưm ư.」
- **Lý do:** や mất phụ âm y trong "Á" — tiền lệ paulette-h5 927 や→"Ya". Phần còn lại giữ nguyên fix audit (んうっ→"ưm ư").

#### 992 — ハチロク — や……/やっ → "Ya……"/"ya"
- **JP:** 「や……パンツの、上から、なのに――んっ――はっ――やっ――そんなに優しく――クリトリ、ス――っ！」」
- **TW:** 「呀……明明隔著內褲——哈——哎——那麼溫柔地——摸陰蒂——！」」
- **VN cũ (CSV3):** 「A……mặc dù, cách lớp quần lót——ưm——hà——á——mà ngài lại nhẹ nhàng như vậy——âm, vật——!」」
- **Mới:** 「Ya……mặc dù, cách lớp quần lót——ưm——hà——ya——mà ngài lại nhẹ nhàng như vậy——âm, vật——Ư!」」
- **Lý do:** や mất phụ âm y trong "A"/"á" — tiền lệ paulette-h5. Giữ Ư cuối dòng của sweep (992 là 1 trong 6 mục sweep, đã áp nguyên).

#### 995 — ハチロク — やあっ → "Yaa"; んふっ → "Nfu"
- **JP:** 「やあっ！？　恥ずかしいっ、わたくし――こんなっ――\nんふっ！！？」
- **TW:** 「呀啊！？好難為情，我——這樣的——嗯呼！！？」
- **VN cũ (CSV3):** 「Á!? Xấu hổ quá, em——thế này——\nưm hứ!!?」
- **Mới:** 「Yaa!? Xấu hổ quá, em——thế này——⏎ Nfu!!?」
- **Lý do:** やあっ một hơi: "Á" mất y — tiền lệ paulette-h5 862 やあっ→"Yaa". んふっ một hơi bị tách "ưm hứ" (mất f) → romaji "Nfu" (n + f + 1u).

#### 996 — ハチロク — ひゃふううううううううんっ → "Hyafuuuuuuuuun"
- **JP:** 「ひゃふううううううううんっ！！！」
- **TW:** 「呀嗚嗚嗚嗚嗚嗚嗚嗯！！！」
- **VN cũ (CSV3):** 「Á phù ư ư ư ư ư ư ư ư ưm!!!」
- **Mới:** 「Hyafuuuuuuuuun!!!」
- **Lý do:** Một hơi rên dài bị tách thành 10 mảnh rời ("Á phù ư ư ư ư ư ư ư ưmƯ") — gộp romaji một hơi theo quy tắc ふかみh1. ひゃ→"Hya" (quy tắc 3b, "Á" mất phụ âm hy). Đếm: ひゃ(1a) + ふ(1u) + う×8 = 9 u + n; っ cuối ngầm trong romaji (tiền lệ "Hyaaann"). Ư của audit ở đây là Ư audit tự thêm (không phải mục sweep), nên bỏ theo dạng romaji — xem §6.

#### 998 — ハチロク — やっ → "Ya"; んふうううううっ → "Nfuuuuuu"
- **JP:** 「やっ！？　らめっ――れふっ――わらひっ――\nイって――イッてる――のっ――は、んふうううううっ」
- **TW:** 「呀！？不行——嗚——我——高潮了——高潮了——嗯嗚嗚嗚」
- **VN cũ (CSV3):** 「Á!? Không——được——em——\nđang——đang lên đỉnh——mà——hà, ưm hư ư ư ư ư ư」
- **Mới:** 「Ya!? Không——được——em——⏎ đang——đang lên đỉnh——mà——hà, NfuuuuuuƯ」
- **Lý do:** やっ→"Ya" (tiền lệ paulette-h5). Đuôi rên một hơi んふううううう bị tách 7 mảnh "ưm hư ư ư ư ư ư" → romaji "Nfuuuuuu" (n + f + 6u: ふ=1u + う×5) + Ư của audit giữ lại (parent sửa khi gộp: っ cuối dòng tuyệt đối, không dấu câu sau — không giữ Ư thì gasp mất hẳn; xem §6). れふっ nói ngọng giữ nguyên theo audit.

#### 1000 — ハチロク — んひゅっ → "Nhyu"
- **JP:** 「ひゃっ！？　あっ――そうではなく――んひゅっ！？」
- **TW:** 「呀！？啊——不是的——咻！？」
- **VN cũ (CSV3):** 「Á!? A——không phải vậy——ưm hứ!?」
- **Mới:** 「Hya!? A——không phải vậy——Nhyu!?」
- **Lý do:** Quy tắc 3b: んひゅ→"Nhyu". Audit (20/11, trước quy tắc 3b) dịch "ưm hứ". ひゃっ→"Hya" của audit giữ nguyên.

#### 1006 — ハチロク — ふあっ → "Fua"
- **JP:** 「ふあっ――あっ―あ……ああっ――\nわたくし――お小水――双鉄、様――にっ――んっ！」
- **TW:** 「呼啊——啊——啊……啊啊——我的——尿——射在了雙鐵少爺——不——！」
- **VN cũ (CSV3):** 「Phù a——a——a……aa——\nem——đã tiểu——vào ngài, Soutetsu——mất rồi——ưm!」
- **Mới:** 「Fua——a——a……aa——⏎ em——đã tiểu——vào ngài, Soutetsu——mất rồi——ưm!」
- **Lý do:** Họ fa/fu → romaji (tiền lệ paulette-h5 848 ふあっ→"Fua"). Các âm ngắn sau (あっ→"a", ああっ→"aa") giữ nguyên.

#### 1008 — ハチロク — ふあっ → "Fua"
- **JP:** 「ふあっ――あっ、そ、それは――そう、なのっ――\nあひっ！？　んっ、ひっ――あっ――ダメ、もうっ」
- **TW:** 「呼啊——啊，那、那個是——這樣的嗎——啊！？嗯，哈——啊——不行，真是的」
- **VN cũ (CSV3):** 「Phù——a, c-cái đó——như thế, là——\ná!? Ưm, hí——a——không được, mất thôi.」
- **Mới:** 「Fua——, c-cái đó——như thế, là——⏎ Ahi!? Ưm, hí——a——không được, mất thôi.」
- **Lý do:** Như 1006. あひっ→"Ahi" của audit đã là romaji, giữ nguyên.

#### 1010 — ハチロク — ふああああああああああああっ → "Fuaaaaaaaaaaaa"; やっ → "ya"
- **JP:** 「ふああああああああああああっ！！！\nあっ！？――ダメっ――やっ――――あ、ああっ……」
- **TW:** 「呼啊——！！！啊！？——不行啊——哎——啊，那樣……」
- **VN cũ (CSV3):** 「Phù a a a a a a a a a a a a a!!!\nA!?——Không được——á————a, aa……」
- **Mới:** 「Fuaaaaaaaaaaaa!!!⏎ A!?——Không được——ya————a, aa……」
- **Lý do:** Rên dài một hơi (ふ+12あ) bị tách 13 mảnh "Phù a a a …" → romaji một hơi, 12 a (đếm bằng máy: あ×12). Dòng 2: やっ→"ya" (tiền lệ paulette-h5); あっ→"A", ああっ→"aa" giữ nguyên.

#### 1011 — ハチロク — ふあっ → "Fua"
- **JP:** 「ふあっ」
- **TW:** 「呼啊」
- **VN cũ (CSV3):** 「Phù」
- **Mới:** 「Fua」
- **Lý do:** Như 1006.

#### 1012 — ハチロク — ひあっ → "Hia"; あちゅっ → "Achu"
- **JP:** 「ひあっ――あっ――あちゅっ――しゅ、ごっ」
- **TW:** 「咿啊——啊——啊啾——好棒」
- **VN cũ (CSV3):** 「Hí a——a——nóng quá——sướng, quá.」
- **Mới:** 「Hia——a——Achu——sướng, quá.」
- **Lý do:** ひあっ→"Hia" theo quy tắc 3b (audit dịch "Hí a" — tách 2 mảnh). あちゅっ: VN cũ "nóng quá" mất hẳn âm hôn (JP a-chu, TW 啊啾) — lỗi mất âm mà audit bỏ sót; sửa romaji "Achu" (một hơi, cùng dạng với "Ahi" ở 1008). Phán đoán moan-pass, xem cờ F1.

#### 1013 — ハチロク — ひあっ → "Hia"
- **JP:** 「ひあっ！　あっ――せ、せかさないでくださいましっ」
- **TW:** 「咿啊！啊——別、別這麼急著催我啦」
- **VN cũ (CSV3):** 「Á! A——x-xin ngài đừng hối thúc em mà.」
- **Mới:** 「Hia! A——x-xin ngài đừng hối thúc em mà.」
- **Lý do:** Quy tắc 3b. Audit dịch "Hí a" (tách 2 mảnh).

#### 1020 — ハチロク — くっ → "Ku"
- **JP:** 「はっ――あっ！　くっ――ごツンッ――て、\nしきゅ――うっ――ひっ――強っ――しゅ、ごっ」
- **TW:** 「哈——啊！嗯——插得——嗚——哈——力氣好大——好棒」
- **VN cũ (CSV3):** 「Hà——a! Ưm——đâm mạnh——vào,\ntử cung——ưm——hí——mạnh quá——sướng, quá.」
- **Mới:** 「Hà——a! Ku——đâm mạnh——vào,⏎ tử cung——ưm——hí——mạnh quá——sướng, quá.」
- **Lý do:** くっ trong chuỗi rên bị dịch "Ưm" (đó là âm của ん) — mất phụ âm k. Tiền lệ paulette-h5: くっ→"Ku" trong dòng rên (870/883/886/940). Phán đoán, xem cờ F2 (câu hỏi mở "Ku" vs "Hự" vs "Ư").

#### 1031 — ハチロク — やっ → "Ya"
- **JP:** 「あっ――来たっ――んっ！　やっ――あっ――\n精液っ――重、いっ――これ――しゅご――っ！！」
- **TW:** 「啊——來了——！哎——啊——精液——好重——這樣——好棒——！！」
- **VN cũ (CSV3):** 「A——đến rồi——ưm! Á——a——\ntinh dịch——nặng, quá——thế này——sướng quá——!!」
- **Mới:** 「A——đến rồi——ưm! Ya——a——⏎ tinh dịch——nặng, quá——thế này——sướng quá——Ư!!」
- **Lý do:** やっ→"Ya" (tiền lệ paulette-h5). Giữ Ư cuối dòng của sweep (1031 là mục sweep, đã áp nguyên).

#### 1033 — ハチロク — ふあっ → "fua"
- **JP:** 「あっ――ああっ――んっ！　双鉄さまっ――\nふあっ――双鉄、さまぁっ」
- **TW:** 「啊——啊啊——嗯！雙鐵少爺——呼啊——雙鐵少爺」
- **VN cũ (CSV3):** 「A——aa——ưm! Ngài Soutetsu——\nphù a——Ngài Soutetsu.」
- **Mới:** 「A——aa——ưm! Ngài Soutetsu——⏎ fua——Ngài Soutetsu.」
- **Lý do:** Họ fa/fu → romaji; viết thường giữa dòng theo VN cũ ("phùa" → "fua").

#### 1064 — ハチロク — ふやっ → "Fuya"; ふあっ → "fua"
- **JP:** 「ふやっ！？　あっ！　だめっ――押したら――\nんっ――もっと――あっ、ふあっ――んんん～～～っ」
- **TW:** 「嗚呀！？啊！不行——再擠壓的話——嗯——更——啊，呼啊——嗯嗯～～～」
- **VN cũ (CSV3):** 「Phù á!? A! Không được——nếu ấn vào——\nưm——nữa——a, phù a——ưm ưm~~~」
- **Mới:** 「Fuya!? A! Không được——nếu ấn vào——⏎ ưm——nữa——a, fua——ưm ưm~~~Ư」
- **Lý do:** ふやっ: romaji "Fuya" (một dòng = một cách diễn — không trộn "Phuya" Việt với "fua" romaji). ふあっ→"fua". Giữ "ưm ưm~~~Ư" của sweep cho んんん～～～っ (1064 là mục sweep).

#### 1065 — ハチロク — ふやっっ → "Fuya"
- **JP:** 「ふやっっ！？　これっ！――しゅごっ――\n～～～～～～～～～～っ！！！！」
- **TW:** 「嗚呀！？這個！——好棒——～～～～～～～～～～！！！！」
- **VN cũ (CSV3):** 「Phù á!? Cái này!——Sướng quá——\n~~~~~~~~~~!!!!」
- **Mới:** 「Fuya!? Cái này!——Sướng quá——⏎ ~~~~~~~~~~Ư!!!!」
- **Lý do:** Như 1064. Giữ "~~~~~~~~~~Ư" của sweep cho ～～～っ (1065 là mục sweep).

#### 1067 — ハチロク — んふうううっっ → "Nfuuuu"
- **JP:** 「んっ――あっ――しきゅう――れっ――\nごつん――って、ごつんて、されて――んふうううっっ」
- **TW:** 「嗯——啊——子宮——嗚——砰——砰地被敲打——呼」
- **VN cũ (CSV3):** 「Ưm——a——tử cung——bị——\nđâm mạnh——bị đâm mạnh vào——ưm hư ư ư ư ư」
- **Mới:** 「Ưm——a——tử cung——bị——⏎ đâm mạnh——bị đâm mạnh vào——NfuuuuƯƯ」
- **Lý do:** Đuôi rên một hơi (ん+ふ+う×3) bị tách 5 mảnh "ưm hư ư ư ư" → romaji "Nfuuuu" (4u) + ƯƯ của audit giữ lại (parent sửa khi gộp: っっ cuối dòng tuyệt đối, không dấu câu sau — không giữ ƯƯ thì gasp mất hẳn; xem §6).

#### 1070 — 双鉄H — くっ → "Ku"; ぷああっ → "Puaa"
- **JP:** 「ん……くっ――――ぷああっ！」
- **TW:** 「嗯……嗯——噗啊！」
- **VN cũ (CSV3):** 「Ưm……ưm————phù a!」
- **Mới:** 「Ưm……Ku————Puaa!」
- **Lý do:** ぷああっ→"Puaa" (tiền lệ paulette-h5 888/893 ぷあっ→"Pua"). くっ→"Ku" như 1020 (xem cờ F2). Ư của audit cho っ cuối bỏ theo dạng romaji (§6).

#### 1073 — ハチロク — �んひゅっ → "Nhyu"; ふあっ → "Fua"; ああああああああんっ → "Aaaaaaaan"
- **JP:** 「んひゅっ！？　ふあっ！？　ああああああああんっ！」
- **TW:** 「嗯咻！？呼啊！？啊啊——！」
- **VN cũ (CSV3):** 「Ưm hứ!? Phù a!? A a a a a a a a a a!」
- **Mới:** 「Nhyu!? Fua!? Aaaaaaaan!」
- **Lý do:** �んひゅっ→"Nhyu" (quy tắc 3b). ふあっ→"Fua". Rên dài あ×8+ん bị tách 9 mảnh "A a a a a a a an" → romaji một hơi "Aaaaaaaan" (8a + n). Ư của audit bỏ theo dạng romaji (§6). (Parent sửa khi gộp: agent viết thừa 1 a — xem §6b.)

#### 1074 — ハチロク — んふうっ → "Nfuu"
- **JP:** 「んひっ――あっっ！？　だ、ダメっ――んふうっ」
- **TW:** 「嗯咿——啊！？不、不行——呼」
- **VN cũ (CSV3):** 「Ưm hí——á!? Kh-Không được——ưm hự」
- **Mới:** 「Ưm hí——á!? Kh-Không được——Nfuu」
- **Lý do:** Một hơi んふうっ bị tách "ưm hự" (mất f, "hự" là âm grunt) → romaji "Nfuu" (n + f + 2u). んひっ→"Ưm hí" giữ nguyên (tiền lệ paulette-h5 F3: ひ/ひっ→"hí" giữ).

#### 1075 — 双鉄H — んああああああっ → "Naaaaaa"
- **JP:** 「んああああああっ！」
- **TW:** 「嗯啊啊啊啊！」
- **VN cũ (CSV3):** 「Ưm a a a a a!」
- **Mới:** 「Naaaaaa!」
- **Lý do:** Một hơi (ん+あ×6) bị tách 6 mảnh "Ưm a a a a a" → romaji "Naaaaaa" (6a). Ư của audit bỏ theo dạng romaji (§6).

#### 1077 — ハチロク — んっひゅううぅぅぅぅぅっ → "Nhyuuuuuuuu"
- **JP:** 「んっひゅううぅぅぅぅぅっ！！！」
- **TW:** 「嗯嗚嗚嗚！！！」
- **VN cũ (CSV3):** 「Ưm hứ ư ư ư ư ư!!!」
- **Mới:** 「Nhyuuuuuuuu!!!」
- **Lý do:** Một hơi dài (ん+ひゅ+う×2+ぅ×5) bị tách 8 mảnh "Ưm hứ ư ư ư ư ư ư ư" → romaji "Nhyuuuuuuuu" (8u: ひゅ=1u + う×2 + ぅ×5). Ư của audit bỏ theo dạng romaji (§6).

#### 1089 — ハチロク — ふぁっ → "Fa"
- **JP:** 「あ……熱い……です。それに――んっ――\nいつも、より――ふぁっ――硬い、みたい、でっ」
- **TW:** 「好……好熱……而且——比平時——啊——還要硬……」
- **VN cũ (CSV3):** 「A……nóng quá……ạ. Với lại——ưm——\ncó vẻ——phù——cứng hơn, mọi khi, ạ.」
- **Mới:** 「A……nóng quá……ạ. Với lại——ưm——⏎ có vẻ——Fa——cứng hơn, mọi khi, ạ.」
- **Lý do:** Họ fa/fu → romaji (tiền lệ paulette-h5 864/884 ふぁ→"Fa").

#### 1178 — ハチロク — ふ、あっ → "Fu, a" (×2)
- **JP:** 「おなか……おまん、まん――たぷたぷ……ふ、あっ、\nおまんまん――精液で、ふ、あっ――おぼれ、ちゃうっ」
- **TW:** 「肚子裡……小妹妹——滿滿的……呼、啊，小妹妹——精液，呼、啊——感覺要淹死了……」
- **VN cũ (CSV3):** 「Bụng em……cô bé——đầy ắp rồi……phù, a,\ncô bé——sắp chết đuối, trong tinh dịch——phù, a——mất thôi.」
- **Mới:** 「Bụng em……cô bé——đầy ắp rồi……Fu, a,⏎ cô bé——sắp chết đuối, trong tinh dịch——Fu, a——mất thôi.」
- **Lý do:** Dạng tách fa trong chuỗi rên → romaji một hơi, giữ dấu phẩy tách theo JP (tiền lệ mikuro: ふ、あっ → "Fu, a"). Cả 2 lần xuất hiện.

#### 1181 — 双鉄H — かはっ → "Kaha"
- **JP:** 「かはっ！」
- **TW:** 「蛤啊！」
- **VN cũ (CSV3):** 「Hự!」
- **Mới:** 「Kaha!」
- **Lý do:** VN cũ "Hự!" mất cả hai âm tiết か+は. Song song với 1227 (かふっ→"Kaphù" audit đã sửa từ "á"). Romaji "Kaha" giữ đủ 2 mora. Phán đoán moan-pass, xem cờ F3.

#### 1222 — ハチロク — ふああああああんんんっ → "Fuaaaaaannn"
- **JP:** 「双鉄様が……全部……一滴も、残さずに――\nあっ……あっ――ふああああああんんんっ！！？」
- **TW:** 「雙鐵少爺……全部……一滴也不剩下——啊……啊——呼啊——嗯——！！？」
- **VN cũ (CSV3):** 「Ngài Soutetsu……đã uống hết……không chừa lại, một giọt nào——\nA……a——phù a a a a a ưm ưm!!?」
- **Mới:** 「Ngài Soutetsu……đã uống hết……không chừa lại, một giọt nào——⏎ A……a——Fuaaaaaannn!!?」
- **Lý do:** Một hơi dài (ふ+あ×6+ん×3) bị tách "phùa a a a a a ưm ưm" → romaji "Fuaaaaaannn" (6a + 3n). Ư của audit bỏ theo dạng romaji (§6).

#### 1227 — ハチロク — かふっ → "Kafu"
- **JP:** 「イき――すぎっ――んっ――かふっ――\nわたく、し――回路――やけ、る――焼けちゃうっ」
- **TW:** 「高潮了——好厲害——嗯——啊嗚——我的——電路——要燒了——要燒壞了」
- **VN cũ (CSV3):** 「Lên đỉnh——nhiều quá——ưm——á——\nmạch điện——của em——cháy——cháy mất thôi.」
- **Mới:** 「Lên đỉnh——nhiều quá——ưm——Kafu——⏎ mạch điện——của em——cháy——cháy mất thôi.」
- **Lý do:** "Kaphù" của audit là dạng Việt hoá của かふ; theo quy tắc romaji fallback → "Kafu" (một hơi, giữ đủ 2 mora). Phán đoán moan-pass (tiền lệ paulette-h7 899 きゃふっ→"Kyaphù" mà audit viện dẫn chưa được parent verify), xem cờ F3.


## 4. Dòng rên giữ nguyên (ghi chú đáng kể)

- **Gasp Ư khóa (không đụng):** 992/1031/1064/1065 (4/6 mục sweep — Ư giữ nguyên trong fix moan), 1401/1416 (monologue, audit đã sửa Ư, không đổi), 1085 ん～～～～っっ → "Ưm~~~~ƯƯ!" (audit), 998/1067/1073/1075/1077/1222/1070 xem §6 (Ư của audit bỏ theo dạng romaji, không phải Ư sweep).
- **fa tách "phù——a" giữ (1047):** ふっ――あっ――え？ là hơi thở + gasp xen trong câu thoại, các âm tách nhau bằng ―― (không phải một hơi rên liền) — giữ "phù——a——hả?" theo tiền lệ hachiroku-h7 (dạng tách fa giữ nguyên). Khác với 1178 (ふ、あっ trong chuỗi rên → romaji).
- **Hơi thở ふ/ふっ đứng riêng giữ "phù":** 756 ふだ → "Phù." (tiền lệ mikuro: hơi thở không đi kèm あ thì giữ "phù").
- **ひ/ひっ → "hí" giữ:** 1015 はひっ→"Hahí!?" (thán từ ngắn, tự nhiên), 1074 んひっ→"Ưm hí" (tiền lệ paulette-h5 F3: ひ/ひっ không thuộc họ ひゃ).
- **あっ/ああ ngắn giữ:** 1018/1025/1035/1037/1039/1045/1049/1057/1063/1068/1133/1134/1204 ("A"/"a"/"À"/"Ừ" — không mất phụ âm, không tách mảnh).
- **SFX miệng ちゅ giữ dạng Việt của file:** 753 ちゅうっ→"chụt", ちゅううっ→"chùttt"; 1223 ちゅっ→"chụt", ちゅむっ→"chụm" (xem cờ F4 — họ ちゅ là câu hỏi mở toàn dự án).
- **SFX độc thoại （） giữ nguyên (47 dòng):** toàn bộ SFX hành động trong ngoặc (Thịch/Ôm/Cọ xát/Chụt/Phụt…) giữ dạng động từ Việt theo phong cách file đã chốt ở audit §1 — tiền lệ paulette-h5 (giữ 33 dòng SFX trong ngoặc). Không áp công thức đếm nguyên âm cho nhóm này.
- **Cười giữ:** 1004 うふふ→"Ufufu", 1602 うふふ→"ufufu" (tiếng cười, không phải rên).
- **Nuốt giữ:** 1069 ごくっ→"Ực", ぷっ→"phù"; 1076 んぶっ――ングッ――ごくっ――こくっ→"Ưm——ừng ực——ực——ực" (SFX hành động, không phải rên).
- **759 んうっ→"ưm ư" giữ** (fix audit, đếm đúng, ngắn, tự nhiên); **1015 はあんっ→"hà anƯ" giữ** (fix audit + Ư gasp); **1070 ん……→"Ưm……" giữ**.

## 5. Lượt soát 2 (second pass)

Đọc lại toàn bộ 28 giá trị fix đối chiếu JP (+TW): **28/28 tái kiểm chứng, 0 bỏ, 0 sửa. Parent sửa khi gộp (xem §6b): 1073 đếm thừa 1 a (9a→8a), 998 +Ư, 1067 +ƯƯ — JSON + khối TOML đã sửa theo, tổng vẫn 28 dòng.**
- Đếm nguyên âm kiểm chứng độc lập bằng máy: 996 9u (1+8), 998 6u (1+5), 1010 12a, 1067 4u (1+3), 1073 8a, 1075 6a, 1077 8u (1+2+5), 1222 6a + 3n.
- JSON 28 khóa chuỗi, dạng chuẩn list-of-dicts (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 28/28 (old_vn lấy trực tiếp từ CSV3 bằng script).
- Khối TOML parse OK (tomllib), 28 khóa, 0 sai lệch giá trị so với JSON.
- Diff-sanity: mọi fix chỉ khác VN cũ ở đúng token rên nhắm tới (trừ 7 dòng §6, trong đó Ư audit tự thêm bỏ theo dạng romaji — đã ghi rõ).
- 0 giá trị fix chứa ký tự xuống dòng thật; `\n` trong fix viết dạng `\\n` trong khối TOML.

## 6. Ghi chú về Ư bị bỏ trong 7 dòng romaji (không vi phạm khóa gasp)

8 dòng sau có Ư do **audit tự thêm** (không phải 6 mục sweep của file — sweep chỉ có 992/1031/1064/1065/1401/1416): 996, 998, 1067, 1070, 1073, 1075, 1077, 1222. Khi toàn bộ token rên chuyển sang romaji, っ cuối được diễn ngầm trong dạng romaji (tiền lệ fukamih1 "Hyaaann", paulette-h5 ふあっ→"Fua", くぅんっ→"Kuun" — không Ư) — âm không bị mất, chỉ đổi cách diễn. Không có Ư sweep nào bị bỏ: 992/1031/1064/1065 giữ Ư, 1401/1416 không đổi.


**§6b — Parent sửa khi gộp (21/11 ~18:05):** §6 của agent đúng cho 6/8 dòng (996, 1070, 1073, 1075, 1077, 1222 — っ cuối có dấu !/?/!!! diễn cắt, tiền lệ h7 836/837 đã chốt "っ cắt diễn bằng !", nên bỏ Ư audit là hợp lệ). Nhưng **998 và 1067 KHÔNG có dấu câu sau っ cuối dòng** (kết bằng 」) — theo quy tắc gasp đã khóa, Ư chỉ thêm khi っ mất hẳn, và đây đúng là trường hợp đó; audit đã thêm Ư/ƯƯ đúng quy tắc, nên moan fix phải giữ: 998 "Nfuuuuuu"→"NfuuuuuuƯ", 1067 "Nfuuuu"→"NfuuuuƯƯ". Ngoài ra **1073 agent đếm thừa 1 a** (JP あ×8 nhưng fix viết 9 a — "Aaaaaaaaan") → sửa thành "Aaaaaaaan" (8a). JSON + khối TOML §8 đã sửa theo; tổng vẫn 28 dòng.

## 7. Cờ (flags — cho đợt thống nhất / parent xem lại)

- **F1 — 1012 あちゅっ→"Achu":** phán đoán moan-pass (audit bỏ sót — VN cũ "nóng quá" mất hẳn âm hôn). Nếu parent muốn giữ phong cách ちゅ→"chụt" của file thì đổi thành "a chụt".
- **F2 — くっ → "Ku" (1020, 1070):** câu hỏi mở toàn dự án (paulette-h5 F2): "Ku" (rên) vs "Hự" (grunt) vs "Ư". File này áp "Ku" theo paulette-h5 đã gộp.
- **F3 — かはっ→"Kaha" (1181), かふっ→"Kafu" (1227):** phán đoán moan-pass (giữ đủ 2 mora); tiền lệ audit viện cho 1227 (paulette-h7 899 きゃふっ→"Kyaphù") chưa được parent verify.
- **F4 — họ ちゅ giữ dạng Việt (753, 1223):** ちゅむっ→"chụm" vs tiền lệ h3/paulette-h5 942 "chumu" — cần quyết toàn dự án (paulette-h5 F4). Không đổi trong file này.
- **F5 — dạng tách fa 1047 giữ "phù——a":** đối chiếu 1178 → romaji "Fu, a" (tiền lệ mikuro) — ranh giới "chuỗi rên" vs "hơi thở xen thoại" cần parent chốt nếu muốn thống nhất.
- **F6 — 998 れふっ nói ngọng:** giữ nguyên theo audit (TW cũng bỏ) — không thuộc moan-pass.
- **F7 — 1015 はひっ→"Hahí" giữ:** dạng Việt có dấu, chưa chuyển romaji "Hahi" — rên ngắn, tự nhiên; ghi lại nếu đợt thống nhất muốn đổi.

## 8. Khối TOML (đã parse-verified, 28 khóa, 0 sai lệch)

```toml
[script]
759 = "「Ya……em xin lỗi——em xin, lỗi——\ne-em——đã tè dầm——tè dầm mất rồi——ưm ư.」"
992 = "「Ya……mặc dù, cách lớp quần lót——ưm——hà——ya——mà ngài lại nhẹ nhàng như vậy——âm, vật——Ư!」」"
995 = "「Yaa!? Xấu hổ quá, em——thế này——\nNfu!!?」"
996 = "「Hyafuuuuuuuuun!!!」"
998 = "「Ya!? Không——được——em——\nđang——đang lên đỉnh——mà——hà, NfuuuuuuƯ」"
1000 = "「Hya!? A——không phải vậy——Nhyu!?」"
1006 = "「Fua——a——a……aa——\nem——đã tiểu——vào ngài, Soutetsu——mất rồi——ưm!」"
1008 = "「Fua——, c-cái đó——như thế, là——\nAhi!? Ưm, hí——a——không được, mất thôi.」"
1010 = "「Fuaaaaaaaaaaaa!!!\nA!?——Không được——ya————a, aa……」"
1011 = "「Fua」"
1012 = "「Hia——a——Achu——sướng, quá.」"
1013 = "「Hia! A——x-xin ngài đừng hối thúc em mà.」"
1020 = "「Hà——a! Ku——đâm mạnh——vào,\ntử cung——ưm——hí——mạnh quá——sướng, quá.」"
1031 = "「A——đến rồi——ưm! Ya——a——\ntinh dịch——nặng, quá——thế này——sướng quá——Ư!!」"
1033 = "「A——aa——ưm! Ngài Soutetsu——\nfua——Ngài Soutetsu.」"
1064 = "「Fuya!? A! Không được——nếu ấn vào——\nưm——nữa——a, fua——ưm ưm~~~Ư」"
1065 = "「Fuya!? Cái này!——Sướng quá——\n~~~~~~~~~~Ư!!!!」"
1067 = "「Ưm——a——tử cung——bị——\nđâm mạnh——bị đâm mạnh vào——NfuuuuƯƯ」"
1070 = "「Ưm……Ku————Puaa!」"
1073 = "「Nhyu!? Fua!? Aaaaaaaan!」"
1074 = "「Ưm hí——á!? Kh-Không được——Nfuu」"
1075 = "「Naaaaaa!」"
1077 = "「Nhyuuuuuuuu!!!」"
1089 = "「A……nóng quá……ạ. Với lại——ưm——\ncó vẻ——Fa——cứng hơn, mọi khi, ạ.」"
1178 = "「Bụng em……cô bé——đầy ắp rồi……Fu, a,\ncô bé——sắp chết đuối, trong tinh dịch——Fu, a——mất thôi.」"
1181 = "「Kaha!」"
1222 = "「Ngài Soutetsu……đã uống hết……không chừa lại, một giọt nào——\nA……a——Fuaaaaaannn!!?」"
1227 = "「Lên đỉnh——nhiều quá——ưm——Kafu——\nmạch điện——của em——cháy——cháy mất thôi.」"
```

## Kết bài

File ハチロクh5_おだいどこしごと (291 dòng) đã đọc hết: xét 134 dòng rên/SFX, sửa 28 dòng (25 romaji + 3 SFX) — họ fa/fu về romaji 12 dòng, họ ひゃ/ひゅ/ひあ về romaji 6 dòng, rên dài một hơi gộp từ dạng tách mảnh 8 dòng, mất phụ âm mora 10 dòng (các nhóm chồng nhau). 16/28 fix thay thế fix audit ở đúng token rên; 6 Ư sweep giữ nguyên; không dòng "Kh" nào bị đổi; không đụng đại từ/thuật ngữ/nghĩa. Khối TOML 28 khóa đã parse-verified, 0 sai lệch; lượt soát 2: 28/28, 0 bỏ, 0 sửa. 7 cờ cho đợt thống nhất/parent (F1–F7).
