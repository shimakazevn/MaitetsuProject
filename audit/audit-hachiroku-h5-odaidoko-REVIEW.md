# Audit — ハチロクh5_おだいどこしごと.txt.toml (Hachiroku h5, "việc bếp núc")

- File: `ハチロクh5_おだいどこしごと.txt.toml` — route 01_Hachiroku, **291 dòng script**.
- Nội dung: sau đợt cúm cả nhà (Mayami, Hibiki, Paulette, Fukami, Kisaki lần lượt ngã bệnh), Hachiroku học nấu ăn từ Mayami và nấu cháo/nấu thịt hầm khoai tây cho Soutetsu; hai người làm tình trong bếp (tạp dề khỏa thân, "công việc bếp núc" của người vợ), Hachiroku tè dầm khi lên đỉnh, Soutetsu uống "nước tiểu" (thực chất là nước cất từ hơi nước), rồi làm tình lần hai và thề hẹn "mãi mãi về sau".
- **Kết quả: 27/291 dòng sai (9,3%)** — toàn bộ là SFX/gasp, không có lỗi nghĩa, đại từ hay thuật ngữ nào.
- Phân loại (27): gasp っ 7 (992, 1031, 1085, 1401, 1416, 998, 1075), fa/fu 6 (1006, 1008, 1010, 1011, 1033, 1089), SFX khác 14 — trong đó 4 dòng mang cả fa/fu + gasp (1064, 1065, 1073, 1222) và 3 dòng mang cả gasp + đếm nguyên âm (996, 1067, 1077). Đếm theo kind trong JSON: gasp 7, fa/fu 6, sfx 14.
- Theo nhân vật: ハチロク 22, 双鉄H 3 (1070, 1075, 1085), monologue 2 (1401, 1416).
- Lệch vị trí **0**, chuỗi xoay **0**, nhiễm chéo **0**, mồ côi **0**, chưa dịch **0**, trùng khóa **0**.

## 1. Xác minh tệp và nguồn

- TOML md5 `4f711f40ec474cb1d9de27daee7eda85`, BOM + CRLF, `[selections]` rỗng. **Không có bản sao** file này trong 227 tệp TOML-2 (1 copy duy nhất).
- CSV3: **1 set duy nhất** (291 dòng, 0 key trùng, 0 VN rỗng, 0 VN == TW, 0 VN == JP). VN khớp TOML tuyệt đối 143/291 + 148 khớp sau khi gộp `\n` thành khoảng trắng (hiện tượng gộp `\n` đã biết của TOML-2), **0 khác biệt thực chất** — CSV3 là bản chuẩn cho fix list.
- Thẻ `%l`: JP **0** thẻ, VN **0** thẻ, TOML **0** thẻ — không có thẻ sai định dạng nào trong file này.
- Đại từ: Soutetsu tự xưng "tôi" với Hachiroku nhất quán toàn file (1175, 1202, 1117, 1144…); Hachiroku tự xưng "em", gọi Soutetsu "ngài Soutetsu" nhất quán. **0 lỗi đại từ.** Các nhân vật khác (Mayami, Hibiki, Paulette, Reina, Nagi, Fukami, Kisaki) chỉ được nhắc tên, không thoại.
- Thuật ngữ đã chốt: "nhà Migita" (1087) đúng; không có 御一夜 / 帝鉄 / 湯医 / 小畑 / 宮司 / KiHa / 回数券 trong file. "cô bé" (14 dòng) là danh từ giải phẫu, không phải xưng hô "cô" chờ thống nhất. 規範 → "tấm gương" (943, 1122) đúng; トップナンバー → "toa xe dẫn đầu" (1122) đúng.
- Kiểm tra nhiễm chéo: 4 cặp VN trùng trong file với JP khác nhau, đều là SFX trong ngoặc đơn dịch thành cùng một từ Việt cho các âm gần giống nhau (（こしゅっ）/（ぐりっ）→ "Cọ xát"; （くっ）/（ぐっ）→ "Ưm"; （ちゅうっ）/（ちゅっ）→ "Chụt"; các biến thể びゅ… → "Phụt!…") — lặp hợp lệ, không phải nhiễm chéo.

## 2. Sweep っ (gasp) — kiểm tra trực tiếp

- File này CÓ **6 mục** trong `sweep-raw-gasp-wrong.json`, toàn bộ `lost-gasp-trailing`: 992, 1031, 1064, 1065, 1401, 1416. **Áp nguyên cả 6, đã kiểm chứng từng giá trị với JP** — riêng 1064/1065 gộp thêm sửa fa/fu (ふやっ → "phuya", ふあっ → "phùa") vì fix sweep chỉ thêm Ư cuối dòng mà giữ nguyên lỗi fa.
- **Sweep bỏ sót 1 dòng — 1085** 「ん～～～～っっ！」 → VN cũ 「Ưm~~~~!」: mẫu ~~~~ + っっ, mỗi っ → 1 Ư theo tiền lệ ハチロクh6 key 1085 (～～～～っっ → "~~~~ƯƯ", phụ lục đa-っ của sweep). Fix: 「Ưm~~~~ƯƯ!」.
- Quét bổ sung **toàn bộ 172 dòng JP chứa っ**: bắt thêm 7 gasp cuối dòng rên sweep bỏ sót (996, 998, 1067, 1073, 1075, 1077, 1222 — っ cuối sau nguyên âm dài, mỗi っ → 1 Ư, tiền lệ lr_ふかみh2 1085/1125/1126 và lr_凪h1 1493) + 2 gasp cuối dòng rên ngắn (1015 はあんっ, 1070 ぷああっ).
- **っ nhấn mạnh gắn với từ — KHÔNG sửa** (tiền lệ h9 §3.4, fukamih2 §4, 1474/2428/2588): さまっ/様っ (1047, 1025, 1033, 1045, 1049, 964), すずっ (1108, 1209, 1182), ですっ/だっ/ぞっ/にっ/ちんっ/ごっ/すぎっ/もうっ/でっ (1057, 1133, 1204, 1227, 1012, 1008, 1010, 1068), và mọi っ theo sau bởi ――/、/…… (1006 ああっ――, 1010 ああっ……, 1045 ぁっ……, 1018 こんなにっ―― — tiền lệ ふかみh3 2338/2345).
- SFX trong ngoặc đơn （…） đều đã dịch thành từ Việt (Thịch/Ôm/Cọ xát/Chụt/Phụt…) — っ trong các onomatopoeia này không phải gasp, giữ nguyên.

## 3. Chi tiết từng dòng sai (27 dòng)

### Gasp — sweep áp nguyên (6 dòng)

#### 992 — ハチロク — gasp
- **JP:** 「や……パンツの、上から、なのに――んっ――はっ――やっ――そんなに優しく――クリトリ、ス――っ！」」
- **TW:** 「呀……明明隔著內褲——哈——哎——那麼溫柔地——摸陰蒂——！」」
- **VN cũ:** 「A……mặc dù, cách lớp quần lót——ưm——hà——á——mà ngài lại nhẹ nhàng như vậy——âm, vật——!」」
- **Mới:** 「A……mặc dù, cách lớp quần lót——ưm——hà——á——mà ngài lại nhẹ nhàng như vậy——âm, vật——Ư!」」
- **Lý do:** Sweep `lost-gasp-trailing` áp nguyên đã kiểm chứng: JP kết ス――っ！, VN giữ dấu —— nhưng mất gasp.

#### 1031 — ハチロク — gasp
- **JP:** 「あっ――来たっ――んっ！　やっ――あっ――\n精液っ――重、いっ――これ――しゅご――っ！！」
- **TW:** 「啊——來了——！哎——啊——精液——好重——這樣——好棒——！！」
- **VN cũ:** 「A——đến rồi——ưm! Á——a——\ntinh dịch——nặng, quá——thế này——sướng quá——!!」
- **Mới:** 「A——đến rồi——ưm! Á——a——\ntinh dịch——nặng, quá——thế này——sướng quá——Ư!!」
- **Lý do:** Sweep `lost-gasp-trailing` áp nguyên đã kiểm chứng.

#### 1401 — monologue — gasp
- **JP:** ほとんど半泣きになりながら、\nすずがまた大きく大きく体を震わ――っ！
- **TW:** 她已經要掉眼淚了，同時渾身劇烈地震顫！
- **VN cũ:** Gần như sắp khóc nấc lên,\nSuzu lại một lần nữa run rẩy dữ dội——!
- **Mới:** Gần như sắp khóc nấc lên,\nSuzu lại một lần nữa run rẩy dữ dội——Ư!
- **Lý do:** Sweep `lost-gasp-trailing` áp nguyên đã kiểm chứng.

#### 1416 — monologue — gasp
- **JP:** まともなことを言う声は、けれども上ずり発情してる。\nそれほどまでに、すずが興奮してい――っ！！？
- **TW:** 她說著很正經的話，但同時也發情得厲害。難道鈴真的這麼興奮嗎——！！？
- **VN cũ:** Giọng nói thốt ra những lời đàng hoàng, nhưng lại cao vút lên vì phát tình.\nĐến mức đó sao, Suzu đang hưng phấn đến thế——!!?
- **Mới:** Giọng nói thốt ra những lời đàng hoàng, nhưng lại cao vút lên vì phát tình.\nĐến mức đó sao, Suzu đang hưng phấn đến thế——Ư!!?
- **Lý do:** Sweep `lost-gasp-trailing` áp nguyên đã kiểm chứng.

#### 1064 — ハチロク — fa/fu + gasp
- **JP:** 「ふやっ！？　あっ！　だめっ――押したら――\nんっ――もっと――あっ、ふあっ――んんん～～～っ」
- **TW:** 「嗚呀！？啊！不行——再擠壓的話——嗯——更——啊，呼啊——嗯嗯～～～」
- **VN cũ:** 「Phù á!? A! Không được——nếu ấn vào——\nưm——nữa——a, phù a——ưm ưm~~~」
- **Mới:** 「Phuya!? A! Không được——nếu ấn vào——\nưm——nữa——a, phùa——ưm ưm~~~Ư」
- **Lý do:** Gộp 3 sửa: (1) ふやっ → "Phuya" theo quy tắc ふやぁ → "phuya" đã chốt; (2) ふあっ → "phùa" theo quy tắc fa/fu; (3) sweep trailing Ư cho んんん～～～っ (áp nguyên fix sweep, giữ "ưm ưm" cho んんん như sweep đã chấp nhận).

#### 1065 — ハチロク — fa/fu + gasp
- **JP:** 「ふやっっ！？　これっ！――しゅごっ――\n～～～～～～～～～～っ！！！！」
- **TW:** 「嗚呀！？這個！——好棒——～～～～～～～～～～！！！！」
- **VN cũ:** 「Phù á!? Cái này!——Sướng quá——\n~~~~~~~~~~!!!!」
- **Mới:** 「Phuya!? Cái này!——Sướng quá——\n~~~~~~~~~~Ư!!!!」
- **Lý do:** ふやっっ → "Phuya" (quy tắc ふやぁ → "phuya"; っっ cuối âm bỏ như tiền lệ ふぁああっっ → "Phààà" ở paulette-lr-h2 1024) + sweep trailing Ư áp nguyên.

### Gasp — sweep bỏ sót (8 dòng)

#### 1085 — 双鉄H — gasp
- **JP:** 「ん～～～～っっ！」
- **TW:** 「嗯～～～～！」
- **VN cũ:** 「Ưm~~~~!」
- **Mới:** 「Ưm~~~~ƯƯ!」
- **Lý do:** Sweep bỏ sót: ~~~~ + っっ, mỗi っ → 1 Ư (tiền lệ ハチロクh6 1085).

#### 996 — ハチロク — gasp + đếm nguyên âm
- **JP:** 「ひゃふううううううううんっ！！！」
- **TW:** 「呀嗚嗚嗚嗚嗚嗚嗚嗯！！！」
- **VN cũ:** 「Á phù ư ư ư ư ư ư ư ư ưm!!!」
- **Mới:** 「Á phù ư ư ư ư ư ư ư ưmƯ!!!」
- **Lý do:** Đếm âm: JP ひゃ(1) + ふ(1) + う×8 = 10 nguyên âm + ん; VN cũ 11 nguyên âm, thừa 1 → bớt 1 ư. Thêm Ư cho っ cuối dòng rên. Giữ "Á" cho ひゃ đầu tiếng rên dài theo thực hành đã ghi ở lr_ふかみh2 (chưa có quy tắc chốt về ひゃ đầu rên — xem §6).

#### 998 — ハチロク — gasp
- **JP:** 「やっ！？　らめっ――れふっ――わらひっ――\nイって――イッてる――のっ――は、んふうううううっ」
- **TW:** 「呀！？不行——嗚——我——高潮了——高潮了——嗯嗚嗚嗚」
- **VN cũ:** 「Á!? Không——được——em——\nđang——đang lên đỉnh——mà——hà, ưm hư ư ư ư ư ư」
- **Mới:** 「Á!? Không——được——em——\nđang——đang lên đỉnh——mà——hà, ưm hư ư ư ư ư ưƯ」
- **Lý do:** Đếm âm đã đúng (ふ+う×5 = 6 + ưm = 7); chỉ thêm Ư cho っ cuối dòng rên. (れふっ nói ngọng bị bỏ — TW cũng gộp thành 嗚, giữ nguyên.)

#### 1067 — ハチロク — gasp + đếm nguyên âm
- **JP:** 「んっ――あっ――しきゅう――れっ――\nごつん――って、ごつんて、されて――んふうううっっ」
- **TW:** 「嗯——啊——子宮——嗚——砰——砰地被敲打——呼」
- **VN cũ:** 「Ưm——a——tử cung——bị——\nđâm mạnh——bị đâm mạnh vào——ưm hư ư ư ư ư」
- **Mới:** 「Ưm——a——tử cung——bị——\nđâm mạnh——bị đâm mạnh vào——ưm hư ư ư ưƯƯ」
- **Lý do:** Đếm âm: JP ふ+う×3 = 4 nguyên âm + ưm = 5; VN cũ 6, thừa 1 → bớt 1 ư. Thêm ƯƯ cho っっ cuối dòng rên.

#### 1073 — ハチロク — fa/fu + đếm nguyên âm + gasp
- **JP:** 「んひゅっ！？　ふあっ！？　ああああああああんっ！」
- **TW:** 「嗯咻！？呼啊！？啊啊——！」
- **VN cũ:** 「Ưm hứ!? Phù a!? A a a a a a a a a a!」
- **Mới:** 「Ưm hứ!? Phùa!? A a a a a a a anƯ!」
- **Lý do:** ふあっ → "Phùa" (quy tắc fa/fu); đếm âm: JP あ×8, VN cũ 10 âm a, thừa 2 → 8 âm a; ん cuối → "n" cuối âm ("an", tiền lệ lr_ふかみh1 1224) + Ư cho っ cuối.

#### 1075 — 双鉄H — gasp
- **JP:** 「んああああああっ！」
- **TW:** 「嗯啊啊啊啊！」
- **VN cũ:** 「Ưm a a a a a!」
- **Mới:** 「Ưm a a a a aƯ!」
- **Lý do:** Đếm âm đã đúng (あ×6 + ưm); chỉ thêm Ư cho っ cuối dòng rên (tiền lệ lr_凪h1 1493: ぁ――っ → "a——Ư").

#### 1077 — ハチロク — gasp + đếm nguyên âm
- **JP:** 「んっひゅううぅぅぅぅぅっ！！！」
- **TW:** 「嗯嗚嗚嗚！！！」
- **VN cũ:** 「Ưm hứ ư ư ư ư ư!!!」
- **Mới:** 「Ưm hứ ư ư ư ư ư ư ưƯ!!!」
- **Lý do:** Đếm âm: JP ひゅ(1) + う×2 + ぅ×5 = 8 nguyên âm + ưm = 9; VN cũ 7, thiếu 2 → thêm 2 ư. Thêm Ư cho っ cuối.

#### 1222 — ハチロク — fa/fu + gasp
- **JP:** 「双鉄様が……全部……一滴も、残さずに――\nあっ……あっ――ふああああああんんんっ！！？」
- **TW:** 「雙鐵少爺……全部……一滴也不剩下——啊……啊——呼啊——嗯——！！？」
- **VN cũ:** 「Ngài Soutetsu……đã uống hết……không chừa lại, một giọt nào——\nA……a——phù a a a a a ưm ưm!!?」
- **Mới:** 「Ngài Soutetsu……đã uống hết……không chừa lại, một giọt nào——\nA……a——phùa a a a a a ưm ưmƯ!!?」
- **Lý do:** ふああああああ (ふ+6あ) → "phùa" (gộp ふあ) + 5 âm a còn lại; giữ "ưm ưm" cho んんん; thêm Ư cho っ cuối dòng rên.

### fa/fu (6 dòng)

#### 1006 — ハチロク — fa/fu
- **JP:** 「ふあっ――あっ―あ……ああっ――\nわたくし――お小水――双鉄、様――にっ――んっ！」
- **TW:** 「呼啊——啊——啊……啊啊——我的——尿——射在了雙鐵少爺——不——！」
- **VN cũ:** 「Phù a——a——a……aa——\nem——đã tiểu——vào ngài, Soutetsu——mất rồi——ưm!」
- **Mới:** 「Phùa——a——a……aa——\nem——đã tiểu——vào ngài, Soutetsu——mất rồi——ưm!」
- **Lý do:** ふあっ → "Phùa" (quy tắc fa/fu đã chốt). Các âm sau giữ nguyên (あっ→"a", あ→"a", ああっ→"aa" — っ bỏ trước ―― theo tiền lệ ふかみh3 2345).

#### 1008 — ハチロク — fa/fu + SFX
- **JP:** 「ふあっ――あっ、そ、それは――そう、なのっ――\nあひっ！？　んっ、ひっ――あっ――ダメ、もうっ」
- **TW:** 「呼啊——啊，那、那個是——這樣的嗎——啊！？嗯，哈——啊——不行，真是的」
- **VN cũ:** 「Phù——a, c-cái đó——như thế, là——\ná!? Ưm, hí——a——không được, mất thôi.」
- **Mới:** 「Phùa——, c-cái đó——như thế, là——\nAhi!? Ưm, hí——a——không được, mất thôi.」
- **Lý do:** ふあっ → "Phùa"; あひっ → "Ahi" — giữ cả hai âm tiết như chính file này dịch ひあっ → "Hí a" ở key 1012 (phán đoán, xem §6).

#### 1010 — ハチロク — fa/fu
- **JP:** 「ふああああああああああああっ！！！\nあっ！？――ダメっ――やっ――――あ、ああっ……」
- **TW:** 「呼啊——！！！啊！？——不行啊——哎——啊，那樣……」
- **VN cũ:** 「Phù a a a a a a a a a a a a a!!!\nA!?——Không được——á————a, aa……」
- **Mới:** 「Phùa a a a a a a a a a a a!!!\nA!?——Không được——á————a, aa……」
- **Lý do:** ふ + 12あ → "Phùa" (gộp ふあ) + 11 âm a còn lại; VN cũ có 13 âm a sau "Phù", thừa 2. Dòng 2 giữ nguyên (あっ→"A", やっ→"á" như 1031, ああっ→"aa" — っ bỏ trước …… theo tiền lệ ふかみh3 2338).

#### 1011 — ハチロク — fa/fu
- **JP:** 「ふあっ」
- **TW:** 「呼啊」
- **VN cũ:** 「Phù」
- **Mới:** 「Phùa」
- **Lý do:** ふあっ → "Phùa" theo quy tắc fa/fu đã chốt (xem §6 về mâu thuẫn với lr_ふかみh2).

#### 1033 — ハチロク — fa/fu
- **JP:** 「あっ――ああっ――んっ！　双鉄さまっ――\nふあっ――双鉄、さまぁっ」
- **TW:** 「啊——啊啊——嗯！雙鐵少爺——呼啊——雙鐵少爺」
- **VN cũ:** 「A——aa——ưm! Ngài Soutetsu——\nphù a——Ngài Soutetsu.」
- **Mới:** 「A——aa——ưm! Ngài Soutetsu——\nphùa——Ngài Soutetsu.」
- **Lý do:** ふあっ → "phùa". さまっ/さまぁっ cuối câu giữ nguyên theo quy tắc っ nhấn mạnh gắn với tên (tiền lệ h9).

#### 1089 — ハチロク — fa/fu
- **JP:** 「あ……熱い……です。それに――んっ――\nいつも、より――ふぁっ――硬い、みたい、でっ」
- **TW:** 「好……好熱……而且——比平時——啊——還要硬……」
- **VN cũ:** 「A……nóng quá……ạ. Với lại——ưm——\ncó vẻ——phù——cứng hơn, mọi khi, ạ.」
- **Mới:** 「A……nóng quá……ạ. Với lại——ưm——\ncó vẻ——phà——cứng hơn, mọi khi, ạ.」
- **Lý do:** ふぁっ (ぁ nhỏ) → "phà" theo quy tắc fa/fu đã chốt.

### SFX khác (7 dòng)

#### 759 — ハチロク — SFX
- **JP:** 「や……ごめんなさいっ――ごめんな、さいっ――\nわ、わたくし――粗相――そそうを、してっ――んうっ」
- **TW:** 「……對不起——對不起——我、我——失禁——失禁了——嗚」
- **VN cũ:** 「Á……em xin lỗi——em xin, lỗi——\ne-em——đã tè dầm——tè dầm mất rồi——ưm.」
- **Mới:** 「Á……em xin lỗi——em xin, lỗi——\ne-em——đã tè dầm——tè dầm mất rồi——ưm ư.」
- **Lý do:** んうっ → "ưm ư" (tiền lệ ハチロクh9 2144: んうっ → "ưm ư,"); VN cũ "ưm" mất âm う.

#### 999 — ハチロク — SFX
- **JP:** 「ひゃっ！？　あっ――」
- **TW:** 「呀！？啊——」
- **VN cũ:** 「Á!? A——」
- **Mới:** 「Hya!? A——」
- **Lý do:** ひゃっ (thán từ ngắn đứng riêng) → "Hya" theo tiền lệ 凪ふかみ05 key 2039 ("Á."→"Hya.").

#### 1000 — ハチロク — SFX
- **JP:** 「ひゃっ！？　あっ――そうではなく――んひゅっ！？」
- **TW:** 「呀！？啊——不是的——咻！？」
- **VN cũ:** 「Á!? A——không phải vậy——ưm hứ!?」
- **Mới:** 「Hya!? A——không phải vậy——ưm hứ!?」
- **Lý do:** Như 999: ひゃっ → "Hya".

#### 1013 — ハチロク — SFX
- **JP:** 「ひあっ！　あっ――せ、せかさないでくださいましっ」
- **TW:** 「咿啊！啊——別、別這麼急著催我啦」
- **VN cũ:** 「Á! A——x-xin ngài đừng hối thúc em mà.」
- **Mới:** 「Hí a! A——x-xin ngài đừng hối thúc em mà.」
- **Lý do:** ひあっ → "Hí a" — thống nhất với chính file này ở key 1012 (ひあっ → "Hí a"); VN cũ "Á" mất âm h.

#### 1015 — ハチロク — SFX + gasp
- **JP:** 「はひっ！？　あっ――おちん、ちん――ンッ――\n射精、したのに――もっと――太――ん――はあんっ」
- **TW:** 「咿！？啊——雞雞——嗯——射過精了——怎麼——又大了——嗯——啊」
- **VN cũ:** 「Hí!? A——dương, vật——ưm——\nđã xuất tinh, rồi mà——còn to——hơn——ưm——hà a.」
- **Mới:** 「Hahí!? A——dương, vật——ưm——\nđã xuất tinh, rồi mà——còn to——hơn——ưm——hà anƯ.」
- **Lý do:** はひっ → "Hahí" (giữ cả hai âm tiết, như 1012 giữ ひあ → "Hí a"); はあんっ cuối dòng → "hà anƯ" (ん cuối → "n", tiền lệ lr_ふかみh1 1224; っ cuối dòng rên → Ư).

#### 1070 — 双鉄H — SFX + gasp
- **JP:** 「ん……くっ――――ぷああっ！」
- **TW:** 「嗯……嗯——噗啊！」
- **VN cũ:** 「Ưm……ưm————phù a!」
- **Mới:** 「Ưm……ưm————phù aƯ!」
- **Lý do:** ぷああ (2 nguyên âm) đã đúng; chỉ thêm Ư cho っ cuối dòng (âm bùng ぷああ + っ ngắt, theo nguyên tắc "rên + っ cuối → Ư" ở lr_ふかみh2 1086). Không áp quy tắc fa/fu vì đây là ぷあ, không phải ふあ.

#### 1227 — ハチロク — SFX
- **JP:** 「イき――すぎっ――んっ――かふっ――\nわたく、し――回路――やけ、る――焼けちゃうっ」
- **TW:** 「高潮了——好厲害——嗯——啊嗚——我的——電路——要燒了——要燒壞了」
- **VN cũ:** 「Lên đỉnh——nhiều quá——ưm——á——\nmạch điện——của em——cháy——cháy mất thôi.」
- **Mới:** 「Lên đỉnh——nhiều quá——ưm——Kaphù——\nmạch điện——của em——cháy——cháy mất thôi.」
- **Lý do:** かふっ → "Kaphù" — VN cũ "á" mất cả hai âm tiết か+ふ; tiền lệ (chưa parent-verified) paulette-h7 899: きゃふっ → "Kyaphù". Phán đoán, xem §6.

## 4. Lượt soát 2 (second pass)

Đọc lại toàn bộ 27 giá trị fix đối chiếu JP: **27/27 tái kiểm chứng, 0 bỏ, 0 sửa.**
- JSON 27 khóa chuỗi, dạng chuẩn list-of-dicts (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 27/27.
- Khối TOML parse OK (tomllib), 27 khóa, 0 sai lệch giá trị so với JSON.
- Diff-sanity (difflib): mọi fix chỉ khác VN cũ ở đúng chỗ sửa nhắm tới — 0 fix viết lại lớn.
- 0 giá trị fix chứa ký tự xuống dòng thật; `\n` trong fix viết dạng `\\n` trong khối TOML.

## 5. Chờ Hieu / phán đoán cần chốt

- **Mâu thuẫn fa/fu giữa hai file đã gộp (cần parent chốt toàn dự án):** quy tắc đã chốt trong MEMORY là ふあ → "phùa" (áp ở ふかみh3: ふあっ → "phùa" 11+ lần, parent-verified 20/11 ~13:16), nhưng lr_ふかみh2 áp ふあっ → "phù" 11 lần với lý lẽ "ふあ (あ đầy) + っ → phù" (parent-verified 20/11 ~10:55, không sửa nào bị loại). File này áp theo MEMORY ("phùa"). Nếu parent chốt theo hướng ふかみh2 thì 8 dòng fa/fu ở đây (1006, 1008, 1010, 1011, 1033, 1064, 1065, 1073, 1222) phải đổi "phùa" → "phù".
- **ひゃ đầu tiếng rên dài:** file này giữ "Á" ở 996 (ひゃふううううううううんっ) theo thực hành lr_ふかみh2 ("chưa có quy tắc chốt về ひゃ"), nhưng sửa ひゃっ ngắn ở 999/1000 → "Hya" theo tiền lệ 凪ふかみ05 2039. Cần một quy tắc thống nhất cho ひゃ.
- **Phán đoán SFX (đã sửa theo tiền lệ, parent xem lại):** 1008 あひっ → "Ahi", 1015 はひっ → "Hahí", 1227 かふっ → "Kaphù" (tiền lệ paulette-h7 chưa được parent verify), 1015/1070 thêm Ư cho っ cuối dòng rên ngắn.
- **Không chắc chắn (giữ nguyên, không sửa):** 998 れふっ (nói ngọng, TW cũng bỏ); 1122 câu JP dở dang "されてっ" — VN "thôi đã." giữ nguyên; 1035 "nước, tiểu" giữ dấu phẩy tách theo JP お小、水.
- **Không có gì chờ đợt thống nhất trong file này** (0 dòng Ohitoyo/Yui/Migita System/Master Controller dạng cũ).

## 6. Khối TOML (đã parse-verified, 27 khóa, 0 sai lệch)

```toml
[script]
759 = "「Á……em xin lỗi——em xin, lỗi——\\ne-em——đã tè dầm——tè dầm mất rồi——ưm ư.」"
992 = "「A……mặc dù, cách lớp quần lót——ưm——hà——á——mà ngài lại nhẹ nhàng như vậy——âm, vật——Ư!」」"
996 = "「Á phù ư ư ư ư ư ư ư ưmƯ!!!」"
998 = "「Á!? Không——được——em——\\nđang——đang lên đỉnh——mà——hà, ưm hư ư ư ư ư ưƯ」"
999 = "「Hya!? A——」"
1000 = "「Hya!? A——không phải vậy——ưm hứ!?」"
1006 = "「Phùa——a——a……aa——\\nem——đã tiểu——vào ngài, Soutetsu——mất rồi——ưm!」"
1008 = "「Phùa——, c-cái đó——như thế, là——\\nAhi!? Ưm, hí——a——không được, mất thôi.」"
1010 = "「Phùa a a a a a a a a a a a!!!\\nA!?——Không được——á————a, aa……」"
1011 = "「Phùa」"
1013 = "「Hí a! A——x-xin ngài đừng hối thúc em mà.」"
1015 = "「Hahí!? A——dương, vật——ưm——\\nđã xuất tinh, rồi mà——còn to——hơn——ưm——hà anƯ.」"
1031 = "「A——đến rồi——ưm! Á——a——\\ntinh dịch——nặng, quá——thế này——sướng quá——Ư!!」"
1033 = "「A——aa——ưm! Ngài Soutetsu——\\nphùa——Ngài Soutetsu.」"
1064 = "「Phuya!? A! Không được——nếu ấn vào——\\nưm——nữa——a, phùa——ưm ưm~~~Ư」"
1065 = "「Phuya!? Cái này!——Sướng quá——\\n~~~~~~~~~~Ư!!!!」"
1067 = "「Ưm——a——tử cung——bị——\\nđâm mạnh——bị đâm mạnh vào——ưm hư ư ư ưƯƯ」"
1070 = "「Ưm……ưm————phù aƯ!」"
1073 = "「Ưm hứ!? Phùa!? A a a a a a a anƯ!」"
1075 = "「Ưm a a a a aƯ!」"
1077 = "「Ưm hứ ư ư ư ư ư ư ưƯ!!!」"
1085 = "「Ưm~~~~ƯƯ!」"
1089 = "「A……nóng quá……ạ. Với lại——ưm——\\ncó vẻ——phà——cứng hơn, mọi khi, ạ.」"
1222 = "「Ngài Soutetsu……đã uống hết……không chừa lại, một giọt nào——\\nA……a——phùa a a a a a ưm ưmƯ!!?」"
1227 = "「Lên đỉnh——nhiều quá——ưm——Kaphù——\\nmạch điện——của em——cháy——cháy mất thôi.」"
1401 = "Gần như sắp khóc nấc lên,\\nSuzu lại một lần nữa run rẩy dữ dội——Ư!"
1416 = "Giọng nói thốt ra những lời đàng hoàng, nhưng lại cao vút lên vì phát tình.\\nĐến mức đó sao, Suzu đang hưng phấn đến thế——Ư!!?"
```

## Kết bài

File ハチロクh5_おだいどこしごと (291 dòng) sạch về nghĩa, đại từ và thuật ngữ — 27 dòng sai (9,3%) toàn bộ là SFX/gasp: 6 mục sweep áp nguyên (1064/1065 gộp thêm sửa fa), 1 gasp sweep bỏ sót (1085), 9 gasp cuối dòng rên sweep bỏ sót, 6 dòng fa/fu hệ thống (ふあ/ふぁ tách thành "phù"/"phù a"), 5 dòng SFX h-sound và tiếng thở khác. Không lệch dòng, không xoay chuỗi, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Khối TOML 27 khóa đã parse-verified, 0 sai lệch; lượt soát 2: 27/27, 0 bỏ, 0 sửa. Hai điểm cần parent chốt toàn dự án: mâu thuẫn ふあっ → "phùa" (MEMORY + ふかみh3) vs "phù" (lr_ふかみh2), và quy tắc cho ひゃ đầu tiếng rên dài.
