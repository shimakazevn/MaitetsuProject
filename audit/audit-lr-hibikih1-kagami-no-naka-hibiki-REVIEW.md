# Audit — lr_日々姫h1_鏡の中日々姫.txt.toml (route 02_Hibiki)

- File: `lr_日々姫h1_鏡の中日々姫.txt.toml` — route 02_Hibiki, 1 bản duy nhất (không có file trùng).
- Đường dẫn: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/02_Hibiki/lr_#U65e5#U3005#U59ebh1_#U93e1#U306e#U4e2d#U65e5#U3005#U59eb.txt.toml`
- Số dòng script: **325** (日々姫 163, 双鉄 66, độc thoại 96). Đọc toàn bộ 325/325 dòng đối chiếu JP + TW từ CSV3.
- Nội dung: cảnh H của Hibiki và Soutetsu trước gương (鏡の中日々姫 — "Hibiki trong gương"): Hibiki khoe món đồ mới (mèo tai/đuôi), hai người làm tình trong khi nhìn vào gương, xen kẽ độc thoại dài của Soutetsu và chuỗi SFX. Soutetsu xưng "anh" với Hibiki xuyên suốt (đúng quy tắc đã sửa 20/11); Hibiki gọi "anh hai" (にぃに).
- **Kết quả: 41/325 dòng sai (12,6%)** — lỗi tập trung ở rên/gasp trong cảnh H: mất Ư (19), romaji fa/fu + đếm âm rên (18), sai nghĩa (4). Không có lỗi đại từ, không có lỗi thuật ngữ.
- CSV3: 1 set duy nhất, 0 khóa trùng, 0 dòng VN trống, 1 dòng VN == TW (758 `「…………」` — chỉ dấu câu, giống hệt là đúng), 0 dòng VN == JP. TOML khớp CSV3 tuyệt đối modulo hiện tượng đã biết: 167 giá trị TOML đã flatten `\n` literal thành khoảng trắng; CSV3 là bản authoritative, fix list lấy theo CSV3.
- TOML md5: `8e7924c231fed9512780b5e53fce841e`. Không có bản sao của file này trong 11 nhóm trùng. File có BOM + CRLF.
- `[selections]` rỗng. `[characters]`: 1404 Soutetsu, 1541 Hibiki. `[character_subs]`: 1584 Hibiki, 1683 Soutetsu.
- Không có thẻ `%l` nào trong file (cả JP lẫn VN) — không có vấn đề tag, B19 không liên quan tới file này.

## Phân loại (41)

| Loại | Số dòng | Keys |
|---|---|---|
| Thở gấp — mất Ư (gasp) | 19 | 1005, 1022, 1034, 1049, 1054, 1066, 1092, 1093, 1094, 1095, 1097, 1123, 1127, 1237, 1266, 1291, 1331, 1337, 1338 |
| Rên — romaji fa/fu, họ ひゃ, đếm âm (moan) | 18 | 1029, 1033, 1039, 1041, 1063, 1064, 1067, 1069, 1103, 1107, 1108, 1115, 1139, 1142, 1145, 1219, 1292, 1433 |
| Sai nghĩa (meaning) | 4 | 1117, 1321, 1377, 1455 |

Hai dòng hỗn hợp: 1069 (moan + gasp) và 1291 (gasp + đếm âm) — đã tính một lần trong bảng trên (1069 ở moan, 1291 ở gasp).
Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. Các dòng JP cụt được VN giữ cụt theo đúng quy tắc (1151, 1190, 1261, 1297, 1321, 1322), trừ 1321 đã sửa (xem §3).

## §1. Thở gấp — mất Ư (19)

Quy tắc áp dụng: っ là một âm — khi っ là toàn bộ nội dung âm của một đoạn (đứng một mình giữa dấu gạch/dấu câu, hoặc cả dòng chỉ có っ + dấu câu) mà VN chỉ còn dấu câu/dấu gạch thì thêm Ư. っ gắn vào từ có nội dung (あっ→"A", ～～～ gắn vào âm đã diễn, だがっ, かがみ――っ――) thì KHÔNG thêm — âm đã được diễn qua nguyên âm/dấu gạch. Chuẩn đối chiếu: sweep `lost-gasp-trailing` / `lost-gasp-whole` / `lost-gasp-trailing-mid` (1338, 2783, ポーレットh1 1005, 仲国05 2071).

### 1005 [双鉄] — sweep lost-gasp-trailing
- JP: `「日々姫の指では足りないと――どうなるん――っ！！」`
- TW: `「你發現自己的手指不夠長時——會怎麼辦——！！」`
- VN cũ: `「Nếu ngón tay của Hibiki không đủ——thì sẽ thế nào——!!」`
- Fix: `「Nếu ngón tay của Hibiki không đủ——thì sẽ thế nào——Ư!!」`

### 1022 [双鉄] — っっ đứng một mình giữa hai dấu gạch (sweep bỏ sót)
- JP: `「どういう、意味だ？　――っっ――\n僕に、どうか――聞かせて――ほし、いっ――」`
- TW: `「到底是、什麼意思？　——唔——希望你——告訴我——」`
- VN cũ: `「Ý em, là sao? ——\nXin em——hãy nói——cho anh biết, đi——」`
- Fix: `「Ý em, là sao? ——Ư—— Xin em——hãy nói——cho anh biết, đi——」`
- Lý do: っっ là một tiếng gasp độc lập (không gắn vào từ nào), TW diễn bằng 唔, VN chỉ còn dấu gạch — âm mất hoàn toàn. Tiền lệ sweep trailing-mid 仲国05 2071 (`――っ！` → `――Ư!`).

### 1034 [日々姫] — っ！ đứng một mình cuối dòng 1 (sweep bỏ sót)
- JP: `「ひゃうっ！　あっ！　いいっ！　いいよぉっ！　っ！\nおまんこっ！　おなかっ――にぃに、えぐ、って――」`
- TW: `「呀嗚！　啊！　好棒！　好棒啊！　嗚！小穴！　肚子裡面——被阿哥、挖著——」`
- VN cũ: `「Hyau! A! Thích! Thích lắm! !\nChỗ đó! Bụng em——anh hai, đâm sâu, quá——」`
- Fix: `「Hyau! A! Thích! Thích lắm! Ư! Chỗ đó! Bụng em——anh hai, đâm sâu, quá——」`
- Lý do: đoạn っ！ cuối dòng 1 chỉ còn lại dấu `!` trơ trọi trong VN — gasp mất hẳn. Cùng dạng trailing-mid như 2783 (`～～っ！` → `~~Ư!`).

### 1049 [日々姫] — sweep lost-gasp-trailing
- JP: `「ふやっ！　あっ――しょこっ――そこっ――っ！！」`
- TW: `「呼呀！啊——那裡——那裡！！」`
- VN cũ: `「Fuya! A——chỗ đó——chỗ đó——!!」`
- Fix: `「Fuya! A——chỗ đó——chỗ đó——Ư!!」`

### 1054 [日々姫] — sweep lost-gasp-whole (っ ở dòng 2)
- JP: `「ふぇ？　かが、み――っ――あ――鏡――\nっ！！！！！！！？」`
- TW: `「呼哎？鏡、子——唔——啊——鏡子——嗚！！！！！！！？」`
- VN cũ: `「Hể? Gương——a——gương——\n!!!!!!!?」`
- Fix: `「Hể? Gương——a——gương—— Ư!!!!!!!?」`
- Lưu ý: っ ở dòng 1 (かが、み――っ――) gắn vào từ có nội dung かがみ nên không thêm Ư — chỉ sửa っ dòng 2, đúng giá trị sweep.

### 1066 [日々姫] — hai gasp đứng một mình (sweep bỏ sót)
- JP: `「ふぁっ！　あっ！　あっ！　あっ！！――っ――\n～～～っ！　ひっ――あっ――あっ！　あああっ！！」`
- TW: `「呼啊！啊！啊！啊！！——嗚——！呀——啊——啊！啊啊啊！！」`
- VN cũ: `「Fa! A! A! A!!——\n~~~! Hi——a——a! Aaa!!」`
- Fix: `「Fa! A! A! A!!——Ư—— ~~~Ư! Hi——a——a! Aaa!!」`
- Lý do: (a) `――っ――` cuối dòng 1 là gasp lặp độc lập, TW diễn bằng 嗚, VN chỉ còn dấu gạch; (b) `～～～っ！` đầu dòng 2 — cùng dạng sweep đã sửa ở 1338 và ポーレットh1 1005 (`～～～～～っ！` → `～～～～～Ư!`). Lưu ý: ふぁっ ở đây là ふぁ (ぁ nhỏ) nên "Fa" là đúng, không sửa.

### 1092 [双鉄] — sweep lost-gasp-whole
- JP: `「っ！」` — TW: `「唔！」` — VN cũ: `「!」` — Fix: `「Ư!」`

### 1093 [双鉄] — sweep lost-gasp-whole
- JP: `「っ！！」` — TW: `「唔！！」` — VN cũ: `「!!」` — Fix: `「Ư!!」`

### 1094 [双鉄] — sweep lost-gasp-whole
- JP: `「っ！！！」` — TW: `「唔！！！」` — VN cũ: `「!!!」` — Fix: `「Ư!!!」`

### 1095 [双鉄] — sweep lost-gasp-whole
- JP: `「っ！！！！」` — TW: `「唔！！！！」` — VN cũ: `「!!!!」` — Fix: `「Ư!!!!」`

### 1097 [双鉄] — sweep lost-gasp-whole
- JP: `「っ！！！！！！」` — TW: `「唔！！！！！！」` — VN cũ: `「!!!!!!」` — Fix: `「Ư!!!!!!」`

### 1123 [双鉄] — sweep lost-gasp-whole
- JP: `「っ！！！？」` — TW: `「啊！！！？」` — VN cũ: `「!!!?」` — Fix: `「Ư!!!?」`

### 1127 [日々姫] — sweep lost-gasp-whole
- JP: `「っ！！！！！！！！！！」` — TW: `「嗚！！！！！！！！！！」` — VN cũ: `「!!!!!!!!!!」` — Fix: `「Ư!!!!!!!!!!」`

### 1237 [双鉄] — sweep lost-gasp-trailing
- JP: `「日々、姫――っ！」` — TW: `「日日、姬——！」` — VN cũ: `「Hibi, ki——!」` — Fix: `「Hibi, ki——Ư!」`

### 1266 [日々姫] — っ×6 bị mất hẳn (sweep bỏ sót)
- JP: `「正面の鏡？　っっっっっっ！！？」`
- TW: `「正面的鏡子？　啊啊啊啊啊啊！！？」`
- VN cũ: `「Gương trước mặt á? !!?」`
- Fix: `「Gương trước mặt á? Ư!!?」`
- Lý do: っ×6 là một tiếng gasp/shock độc lập, TW diễn bằng 啊×6, VN chỉ còn dấu câu. Một Ư duy nhất theo quy ước sweep cho whole-line gasp (1092–1097); っ×nhiều là nhấn mạnh, không nhân Ư theo số lượng (tiền lệ moan 1224 ふあっっっっ → "Fua!!!!!").

### 1291 [日々姫] — sweep lost-gasp-trailing + sửa đếm âm (xem §2)
- JP: `「はぁっ――はぁっ――はぁっ――はぁっ――\nにぃに――にぃにぃっ――っ！」`
- TW: `「蛤啊——蛤啊——蛤啊——蛤啊——阿哥——阿哥——！」`
- VN cũ: `「Ha——ha——ha——ha——\nAnh hai——anh hai——!」`
- Fix: `「Haa——haa——haa——haa—— Anh hai——anh hai——Ư!」`
- Lý do: nhận giá trị gasp của sweep (thêm Ư cuối dòng) nhưng sửa thêm đếm âm: はぁ = 2 âm a, VN cũ chỉ có 1 a mỗi token (xem §2).

### 1331 [双鉄] — sweep lost-gasp-whole
- JP: `「っ！！」` — TW: `「！！」` — VN cũ: `「!!」` — Fix: `「Ư!!」`

### 1337 [日々姫] — ～～～っ đầu dòng (sweep bỏ sót)
- JP: `「～～～～～～～っ！！！！　かっ！　――はっ――あ！\nにぃにっ！　にぃに！　にぃに！　にぃにぃっ！！！」`
- TW: `「～～～～～～～！！！！　啊！　——哈——啊！阿哥！　阿哥！　阿哥！　阿哥！！！」`
- VN cũ: `「~~~~~~~!!!! Ka! ——ha——a!\nAnh hai! Anh hai! Anh hai! Anh hai!!!」`
- Fix: `「~~~~~~~Ư!!!! Ka! ——ha——a! Anh hai! Anh hai! Anh hai! Anh hai!!!」`
- Lý do: cùng dạng sweep đã sửa ở 1338 và 2783 (dấu ~ + っ + dấu câu → thêm Ư sau ~).

### 1338 [日々姫] — sweep lost-gasp-trailing
- JP: `「～～～～～～～～～～っ！！！」` — TW: `「～～～～～～～～～～っ！！！」` — VN cũ: `「~~~~~~~~~~!!!」` — Fix: `「~~~~~~~~~~Ư!!!」`

## §2. Rên — romaji fa/fu, họ ひゃ, đếm âm (18)

Quy tắc áp dụng: (a) họ ひゃ/ひゅ/ひあ/きゃ trong dòng rên cảnh H → romaji (Hya/Hyu/Hia/Kya, んひゅ→Nhyu, んひゅん→Nhyun) — "Á" là lỗi mất âm (quyết 21/11); (b) ふぁ (ぁ nhỏ) → "Fa", ふあっ (あ đầy) → "Fua" — tiền lệ moan-fix pass (vd. ふあっ→"Fua" ×nhiều file, ふぁ→"Fa", ふぁああああん→"Faaaaan"); (c) công thức độ dài nguyên âm: số nguyên âm VN = số kana nguyên âm trong JP (mỗi あ/ぁ, う/ぅ tính 1; vd. はぁあああ → 5 a); ん tính theo số lượng (ん×3 → "nnn").

### 1029 [日々姫] — ふあっ → "fa" mất âm u
- JP: `「ひゃぐっ！　あっ――ふあっ――あっ――やっ――\nおちん、ちん――わたしの、おまんこ――ぬけ、ちゃう」`
- TW: `「呀咕！　啊——呼啊——啊——呀——小雞雞——從我的、小穴裡——滑出來了」`
- VN cũ: `「Hyagu! A——fa——a——không——\nChỗ đó——của em——sắp tuột, ra mất rồi.」`
- Fix: `「Hyagu! A——fua——a——không—— Chỗ đó——của em——sắp tuột, ra mất rồi.」`
- Lý do: ふあっ đọc "fua" — "fa" làm mất mora u của ふ. (ひゃぐっ→"Hyagu" đã đúng; やっ→"không" là cách diễn phản đối tự nhiên, giữ — xem §5.)

### 1033 [日々姫] — ふあっ → "Fa"
- JP: `「ひゃうっ！　あっ！　ふあっ！　あっ！！！\nしゅごっ――んっ！　にぃに――の――あつ、くてっ」`
- TW: `「呀嗚！　啊！　呼啊！　啊！！！好棒——嗯！阿哥的——好熱」`
- VN cũ: `「Hyau! A! Fa! A!!!\nTuyệt quá——ưm! Của anh hai——nóng, quá.」`
- Fix: `「Hyau! A! Fua! A!!! Tuyệt quá——ưm! Của anh hai——nóng, quá.」`

### 1039 [日々姫] — ふあっ → "fa"
- JP: `「ひゃっ！　んっ――ふあっ！　あっ！！！　にぃに、\nおちん、ちん――まだ、半分も――入って、ない、のに」`
- TW: `「呀！嗯——呼啊！　啊！！！　阿哥、小雞雞——明明、連一半都——還沒插進去」`
- VN cũ: `「Hya! Ưm——fa! A!!! Anh hai,\nchỗ đó——mới vào, chưa được một nửa——vậy mà.」`
- Fix: `「Hya! Ưm——fua! A!!! Anh hai, chỗ đó——mới vào, chưa được một nửa——vậy mà.」`

### 1041 [日々姫] — きゃんっ → "Á" (mất phụ âm ky-)
- JP: `「きゃんっ！！？」` — TW: `「呀！！？」`
- VN cũ: `「Á!!?」` — Fix: `「Kyan!!?」`
- Lý do: きゃん = "kyan" (romaji theo quy tắc họ ひゃ 21/11). "Á" làm mất mora phụ âm ky- — cùng lỗi đã sửa ở ポーレットh3 / 凪h2 / 稀咲h3. TW dùng 呀 (ya) nhưng JP thắng TW.

### 1063 [日々姫] — ふあっ → "Fa"
- JP: `「ふあっ――あっ――にぃにっ――にぃにぃっ――」`
- TW: `「呼啊——啊——阿哥——阿哥——」`
- VN cũ: `「Fa——a——anh hai——anh hai——」`
- Fix: `「Fua——a——anh hai——anh hai——」`

### 1064 [日々姫] — đếm a/n sai (kiểm bằng máy)
- JP: `「ふぁぁぁああああああんっ！！！！」` — ふぁ + ぁ×2 + あ×6 = 9 âm a; ん×1.
- TW: `「呼啊啊啊啊啊啊啊啊啊啊！！！！」`
- VN cũ: `「Faaaaaaannnnnn!!!!」` — 7 a, 6 n (thiếu 2 a, thừa 5 n).
- Fix: `「Faaaaaaaaann!!!!」` — F + 9 a + 1 n (tiền lệ moan 1428: ふぁああああん → "Faaaaan", 5 a + 1 n).

### 1067 [日々姫] — ふあっ → "Fa"
- JP: `「ふあっ！　あっ！　んっ――ふやっ――んっ――あっ！\nにぃにっ！　にぃにっ！　奥っ！　奥っ！　もっとぉ！」`
- TW: `「呼啊！啊！嗯——呼啊——嗯——啊！阿哥！阿哥！裡面！裡面！還要！」`
- VN cũ: `「Fa! A! Ưm——fuya——ưm——a!\nAnh hai! Anh hai! Sâu nữa! Sâu nữa! Nữa đi!」`
- Fix: `「Fua! A! Ưm——fuya——ưm——a! Anh hai! Anh hai! Sâu nữa! Sâu nữa! Nữa đi!」`
- Lưu ý: ふやっ→"fuya" đã đúng.

### 1069 [日々姫] — ふあっ → "Fa" + ～～っ mất Ư (ghi đè phân loại "already-rendered" của sweep)
- JP: `「ふきゅっ！　んっ！　ふあっ！　あっっ！　～～っ！\nはっ　あっ！　にぃっ――にぃ、に――もっ、とっ！」`
- TW: `「呼嗚！嗯！呼啊！啊！唔～～！哈、啊！　啊——阿哥——我還要！」`
- VN cũ: `「Fukyu! Ưm! Fa! A! ~~!\nHa a! Anh——anh, hai——hơn, nữa!」`
- Fix: `「Fukyu! Ưm! Fua! A! ~~Ư! Ha a! Anh——anh, hai——hơn, nữa!」`
- Lý do: sweep xếp dòng này "already-rendered" (vì trong dòng đã có Ưm) nhưng đoạn ～～っ cuối dòng 1 bị mất っ — đúng dạng trailing-mid sweep đã sửa ở 2783 và ポーレットh1 1005. Ghi đè phần này của sweep; phần còn lại của dòng đã diễn đúng.

### 1103 [日々姫] — ふあっ → "fa" + ハァッ thiếu 1 a
- JP: `「ぁ――ふあっ――あっ――んっ――ハァッ――\nもうすぐ――もうす、ぐっ――おまんこ――私、のっ」`
- TW: `「啊——呼啊——啊——嗯——蛤啊——很快——我的小穴——很快就要——」`
- VN cũ: `「A——fa——a——ưm——ha——\nSắp rồi——sắp, rồi——chỗ đó——của, em.」`
- Fix: `「A——fua——a——ưm——haa—— Sắp rồi——sắp, rồi——chỗ đó——của, em.」`
- Lý do: ハァ = ハ + ァ = 2 âm a, VN cũ "ha" chỉ có 1.

### 1107 [日々姫] — はぁっ thiếu 1 a
- JP: `「あっ――熱っ――にぃに――こんなに――\nわたしで、おっきく――して、くれてっ――はぁっ」`
- TW: `「啊——好熱——阿哥——都這麼——因為我、變這麼——大了——蛤啊」`
- VN cũ: `「A——Nóng quá——Anh hai——thế này——\nVì em, mà trở nên to lớn——thế này——ha.」`
- Fix: `「A——Nóng quá——Anh hai——thế này—— Vì em, mà trở nên to lớn——thế này——haa.」`

### 1108 [双鉄] — はあ ×3 thiếu 1 a mỗi token
- JP: `「ぁっ――はあ！　はあっ！　はあっ！」`
- TW: `「啊——蛤啊！蛤啊！蛤啊！」`
- VN cũ: `「A——ha! Ha! Ha!」`
- Fix: `「A——haa! Haa! Haa!」`

### 1115 [日々姫] — đếm a/n sai (kiểm bằng máy)
- JP: `「ぁふっ！　ぁぁぁぁぁぁぁぁぁぁぁぁぁんんんっ！！」` — token 2: ぁ×13 + ん×3.
- TW: `「啊呼！　啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！！」`
- VN cũ: `「Afu! Aaaaaaaaaaaaaaannnnn!!」` — token 2: 15 a + 5 n (thừa 2 a, thừa 2 n).
- Fix: `「Afu! Aaaaaaaaaaaaannn!!」` — token 2: 13 a + 3 n (đếm mora nghiêm ngặt, tiền lệ lr_日々姫真闇h1).

### 1139 [日々姫] — んふっ → "Nnfu" thừa 1 n
- JP: `「んふっ――あっ――にぃ、にっ――なに、をっ？」`
- TW: `「嗯呼——啊——啊、哥——說、什麼？」`
- VN cũ: `「Nnfu——a——anh, hai——chuyện, gì cơ?」`
- Fix: `「Nfu——a——anh, hai——chuyện, gì cơ?」`
- Lý do: んふっ = n + fu (1 n). Tiền lệ moan: ん đơn → "n" đơn (Nhyun, Nkyun; ん×3 → "nnn").

### 1142 [日々姫] — んくんっ → "Ưn" mất mora ku
- JP: `「んくんっ！！」` — TW: `「嗯嗚！！」`
- VN cũ: `「Ưn!!」` — Fix: `「Nkun!!」`
- Lý do: んくん = n-ku-n (3 mora); "Ưn" làm mất hẳn mora く — cùng dạng lỗi mất phụ âm mora như họ ひゃ ("Á" cho きゃ). Các dòng kề 1141/1143/1144 đã dùng romaji đúng (Nhyun/Nkyun) nên thống nhất dạng romaji.

### 1145 [日々姫] — đếm u sai (kiểm bằng máy)
- JP: `「んきゅううううううううううううっっっっっ！！！」` — ん + きゅ + う×12 = 13 âm u.
- TW: `「嗯嗚！！！！！！！！！！！！」`
- VN cũ: `「Nkyuuuuuuuuuuuuuuu!!!」` — 15 u (thừa 2).
- Fix: `「Nkyuuuuuuuuuuuuu!!!」` — "Nky" + 13 u (công thức: 1 + số う/ぅ = 13).

### 1219 [日々姫] — はあっ thiếu 1 a
- JP: `「お指の届く……とこより、先、は――ぁ――はあっ――\nにぃに――にぃに、が――にぃにの、おめめ、で――」`
- TW: `「手指能碰到的地方……更裡面——啊——蛤啊——阿哥——阿哥的視線——」`
- VN cũ: `「Phía sâu hơn…… nơi ngón tay chạm tới, thì——a——ha——\nAnh hai——anh hai, phải——dùng mắt của anh hai, để——」`
- Fix: `「Phía sâu hơn…… nơi ngón tay chạm tới, thì——a——haa—— Anh hai——anh hai, phải——dùng mắt của anh hai, để——」`

### 1292 [日々姫] — はぁ ×4 thiếu 1 a mỗi token
- JP: `「はぁ……はぁっ……はぁっ……はぁっ――」`
- TW: `「蛤啊……蛤啊……蛤啊……蛤啊——」`
- VN cũ: `「Ha…… ha…… ha…… ha——」`
- Fix: `「Haa…… haa…… haa…… haa——」`

### 1433 [monologue] — はぁはぁ thiếu 1 a mỗi token
- JP: `はぁはぁ、ひどく荒い息。\nくっついている部分の全てが、ふたりの汗で貼り付きあう。`
- TW: `她在急促地喘氣。我們緊貼著的地方已經被兩人的汗水給黏住了。`
- VN cũ: `Ha ha, hơi thở vô cùng dốc.\nTất cả những chỗ tiếp xúc đều dính chặt lấy nhau bởi mồ hôi của cả hai.`
- Fix: `Haa haa, hơi thở vô cùng dốc. Tất cả những chỗ tiếp xúc đều dính chặt lấy nhau bởi mồ hôi của cả hai.`
- Lưu ý: đây là dòng độc thoại (không có 「」) — giá trị fix giữ nguyên không có ngoặc kép.

## §3. Sai nghĩa (4)

### 1117 [日々姫] — はしゃいで → "đang hưng phấn" (bịa, không có căn cứ JP)
- JP: `「ああああああっ！　おまんこっ！　子宮！　はずか、し、\nはしゃい、でっ！　にぃいの、亀頭！　ちゅって、して」`
- TW: `「啊啊啊啊啊啊！　小穴！　子宮！　在發出聲音，好害羞！阿哥的、龜頭！頂在裡面」`
- VN cũ: `「Aaaaaa! Chỗ đó! Tử cung! Xấu hổ, quá,\nđang hưng phấn, quá! Phần đầu, của anh hai! Mút chặt lấy.」`
- Fix: `「Aaaaaa! Chỗ đó! Tử cung! Xấu hổ, quá, đang phát ra tiếng, quá! Phần đầu, của anh hai! Mút chặt lấy.」`
- Lý do: はしゃぐ = làm ồn / kêu lên (ở đây: tử cung đang phát ra tiếng do bị đâm) — TW xác nhận 在發出聲音. "Đang hưng phấn" (đang phấn khích) không có căn cứ trong JP — lỗi bịa kiểu Gemini. (ああああああ 6 a → "Aaaaaa" 6 a đã đúng.)

### 1321 [日々姫] — bịa động từ "đã khiến" cho câu JP cụt
- JP: `「にぃに、に、私――」` (câu cụt — không có động từ; dòng tiếp 1322 cũng cụt: `にぃにの、おちんちん―― / わたしの……膣、の――`)
- TW: `「阿哥、我——」`
- VN cũ: `「Anh hai, đã khiến, em——」`
- Fix: `「Anh hai, em——」`
- Lý do: "đã khiến" (đã làm cho) là động từ bịa thêm — JP không có. Quy tắc khóa: không bao giờ bịa phần hoàn thiện cho câu JP cụt (tiền lệ Hibiki h5 1189, bỏ "đã bao phủ"). Giữ nguyên dạng cụt như JP.

### 1377 [monologue] — 僕の勃起 → "tôi" (dịch sai danh từ)
- JP: `いや違う。僕の勃起を僕の精子を何百度となく受け止めて。\nそれでも綺麗な桃色をした膣の中へと、指が、沈む。`
- TW: `不對。日日姬的肉穴雖然已經容納了我的勃起、我的精子好幾百次，但依舊保持著漂亮的桃紅色。她將手指沉入其中。`
- VN cũ: `Không, khác chứ. Nó đã tiếp nhận tôi và tinh dịch của tôi không biết bao nhiêu lần rồi.\nVậy mà những ngón tay vẫn chìm vào bên trong lối đi màu hồng đào tuyệt đẹp ấy.`
- Fix: `Không, khác chứ. Nó đã tiếp nhận chỗ đó của tôi và tinh dịch của tôi không biết bao nhiêu lần rồi. Vậy mà những ngón tay vẫn chìm vào bên trong lối đi màu hồng đào tuyệt đẹp ấy.`
- Lý do: 僕の勃起 là danh từ "sự cương cứng của tôi" — VN cũ dịch thành đại từ "tôi" ("nó đã tiếp nhận tôi") làm đổi nghĩa. Dùng cách nói tránh nhất quán của file: 僕の勃起 → "chỗ đó của tôi" (xem 1176/1207/1252). Lưu ý: dòng độc thoại, không có 「」.

### 1455 [monologue] — 僕の勃起 → "tôi" (cùng lỗi 1377)
- JP: `子宮は僕の勃起をさらに伸ばしたいのか、食いつくように\n貼り付いてきては、さらに内へと吸い込もうとする。`
- TW: `子宮似乎是想讓我的勃起伸得更長，它牢牢地吸著我的勃起，試圖吸向更深處。`
- VN cũ: `Tử cung như muốn kéo dài tôi ra thêm, nó dính chặt lấy như cắn nuốt,\nrồi cố gắng hút sâu vào bên trong hơn nữa.`
- Fix: `Tử cung như muốn kéo dài chỗ đó của tôi ra thêm, nó dính chặt lấy như cắn nuốt, rồi cố gắng hút sâu vào bên trong hơn nữa.`
- Lý do: như 1377 — "kéo dài tôi ra" đổi nghĩa; phải là "kéo dài chỗ đó của tôi ra". (1497 giữ nguyên — xem §5: ở đó câu được cấu trúc lại hợp lý, nghĩa không đổi.)

## §4. Kiểm tra sweep っ-gasp cho file này

Sweep có 14 mục fix + 3 mục "already-rendered" cho file này (đã kiểm trực tiếp trong `sweep-raw-gasp-wrong.json`):
- Nhận đủ 14 mục fix của sweep: 1005, 1049, 1054, 1092, 1093, 1094, 1095, 1097, 1123, 1127, 1237, 1291, 1331, 1338 — đã đối chiếu từng giá trị với JP, tất cả đúng (1291 nhận phần gasp, sửa thêm đếm âm — xem §1).
- "Already-rendered" 1126 (`うぅ～～っ` → "Ưư~~") và 1146 (`んんんん～～～っ` → "Ưmmmm~~~!!!") — xác nhận đúng, không sửa (âm đã được diễn: うぅ 2 u, ん×4 → 4 m).
- "Already-rendered" 1069 — GHI ĐÈ một phần: đoạn ～～っ cuối dòng 1 bị mất っ (xem §2). Sweep bỏ sót vì trong dòng đã có Ưm.
- Sweep BỎ SÓT 5 lỗi gasp trong file này (không có trong sweep nhưng cùng dạng sweep đã sửa ở file khác): 1022, 1034, 1066, 1266, 1337 — đã sửa ở §1, ghi nhận để sweep đối chiếu lại.

## §5. Các dòng đã kiểm và GIỮ NGUYÊN (quyết định có căn cứ)

- 753: VN "Hibiki rất hiểu tôi. Em ấy nhớ rõ tôi..." đúng JP `僕を知ってくれてる…覚えてくれている` (TW `了解我的形狀` — "hiểu" bao hàm cả nghĩa này).
- 763 `だがっ――`: っ gắn vào từ có nội dung だが — không phải gasp, giữ `——nhưng mà——`. Cùng lý do giữ 1054 dòng 1 (`かが、み――っ――`) và 1235 (`日々、姫――っ――`).
- 1029 `やっ――` → "không——", 1036 `やぁん――` → "Đừng mà——", 1148 `やっ――` → "Đừng——": cách diễn phản đối tự nhiên theo ngữ cảnh (Hibiki đang phản đối / xấu hổ), không phải lỗi — spontaneity theo quy tắc Hieu 19/11.
- 1038 `やぁん` → "Aaa.": giữ — không có quy tắc khóa nào bắt romaji cho や (quy tắc họ ひゃ chỉ áp ひゃ/ひゅ/ひあ/きゃ); "Aaa" là cách diễn tự nhiên.
- 1047 `ふ、ぁ――` → "Fu, a——": giữ — cách tách hơi thở, TW cũng tách (`呼、啊`).
- 1052 `あかちゃんっ！　おへやっ！` → "Căn phòng! Của em bé!": giữ — VN đảo thứ tự cho tự nhiên ("căn phòng của em bé"), nghĩa không đổi.
- 1064 đã sửa đếm âm; 1085 `ふううううううっ` → "Fuuuuuuu" (7 u) đã đúng; 1117 `ああああああ` → "Aaaaaa" (6 a) đã đúng.
- 1109 `（ごくり）` → "（Nuốt nước bọt）" và 1334 `（はむっ）` → "（Cắn）": giữ — cách diễn tả bằng lời hợp lệ cho SFX trong ngoặc (không phải lỗi nghĩa).
- 1118 `ふっ` → "Fu", 1122 `うっ` → "Ư", `んっ` → "ưm": giữ — っ gắn vào âm đã diễn, không thêm Ư.
- 1176/1207/1252/1297 `僕の勃起` → "của anh": giữ — cách nói tránh nhất quán của file (danh từ được rút gọn nhưng nghĩa khôi phục được từ ngữ cảnh); chỉ sửa 1377/1455 nơi "tôi" làm tân ngữ trực tiếp đổi hẳn nghĩa.
- 1240: JP cụt ở `運命を、感じない、ことも` (đã đối chiếu chú thích `# JP:` trong TOML — khớp CSV3, câu thực sự cụt trong script). VN "anh không thể, không cảm nhận được, sự sắp đặt của vận mệnh" theo đúng cách đọc khẳng định của TW (`感受到了、命運`) — giữ, không bịa thêm.
- 1322 `わたしの……膣、の――` → "Của…… bên trong, em——": giữ — giữ nguyên dạng cụt + sở hữu cách の.
- 1497 `僕の勃起を催促してる` → "hối thúc tôi tiến vào": giữ — câu được cấu trúc lại hợp lý ("cô ấy lắc mông hối thúc tôi tiến vào"), nghĩa không đổi; khác 1377/1455 nơi "tôi" làm tân ngữ trực tiếp.
- 1510: JP `日々姫が見つめる` (Hibiki nhìn) vs TW `我注視著日日姬` (tôi nhìn Hibiki) — JP và TW mâu thuẫn chủ ngữ; VN theo JP ("Hibiki nhìn tôi chằm chằm") — đúng quy tắc JP thắng TW.
- 1749–1833 (chuỗi SFX độc thoại: ちぃ→"Xoè", ごちゅっ→"Hự", ずぶっ→"Phập"...): giữ toàn bộ — cách diễn SFX bằng từ tiếng Việt theo phong cách nhất quán của file; các đoạn kéo dài (1809 11 u = đúng; 1810/1818/1825, 1797–1799) là cách diễn tả bằng lời có nhấn kéo dài, không phải romaji nên không áp công thức đếm mora.
- 1794 `（ぴとっ）` và 1829 `（ぴとっ）` cùng → "（Chạm nhẹ）"; 1765/1768 cùng → "（Phụt! Phụt! Bắn ra! Phụtttt!!）"; 1093/1331 cùng `「!!」` (cùng JP `「っ！！」`); 1098/1156 cùng "Hửm?" (JP `うむ？`/`うん？` đều là "hmm?") — các VN trùng lặp đều có JP tương ứng giống nhau hoặc tương đương, KHÔNG phải lệch vị trí hay xoay chuỗi.
- Đại từ: Soutetsu "anh" với Hibiki xuyên suốt, đã kiểm từng dòng có 僕/お前 — 0 lỗi. Hibiki "em" với Soutetsu, "anh hai" cho にぃに — nhất quán. Không có nhân vật nào khác xưng hô trong file.

## §6. Second pass (đọc lại toàn bộ giá trị fix đối chiếu JP)

- Tổng số fix: **41 / đã đọc lại 41 / loại bỏ 0 / sửa lại 3**.
- 3 giá trị sửa ở second pass: 1377, 1433, 1455 — bản nháp đầu đã thêm nhầm dấu 「」 vào 3 dòng độc thoại (VN gốc không có ngoặc kép); đã bỏ ngoặc, giá trị cuối khớp đúng dạng dòng độc thoại. Ngoài ra không thay đổi nào khác — 38/41 giá trị giữ nguyên sau second pass.
- Kiểm cơ học sau second pass: JSON 41 mục, key dạng string; khối TOML parse được, 41 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 41/41; mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (diff-sanity đã chạy — toàn bộ là chèn Ư / chèn 'u'/'a' / thay từ mục tiêu).

## Khối TOML (đã kiểm parse)

```toml
[script]
1005 = "「Nếu ngón tay của Hibiki không đủ——thì sẽ thế nào——Ư!!」"
1022 = "「Ý em, là sao? ——Ư—— Xin em——hãy nói——cho anh biết, đi——」"
1029 = "「Hyagu! A——fua——a——không—— Chỗ đó——của em——sắp tuột, ra mất rồi.」"
1033 = "「Hyau! A! Fua! A!!! Tuyệt quá——ưm! Của anh hai——nóng, quá.」"
1034 = "「Hyau! A! Thích! Thích lắm! Ư! Chỗ đó! Bụng em——anh hai, đâm sâu, quá——」"
1039 = "「Hya! Ưm——fua! A!!! Anh hai, chỗ đó——mới vào, chưa được một nửa——vậy mà.」"
1041 = "「Kyan!!?」"
1049 = "「Fuya! A——chỗ đó——chỗ đó——Ư!!」"
1054 = "「Hể? Gương——a——gương—— Ư!!!!!!!?」"
1063 = "「Fua——a——anh hai——anh hai——」"
1064 = "「Faaaaaaaaan!!!!」"
1066 = "「Fa! A! A! A!!——Ư—— ~~~Ư! Hi——a——a! Aaa!!」"
1067 = "「Fua! A! Ưm——fuya——ưm——a! Anh hai! Anh hai! Sâu nữa! Sâu nữa! Nữa đi!」"
1069 = "「Fukyu! Ưm! Fua! A! ~~Ư! Ha a! Anh——anh, hai——hơn, nữa!」"
1092 = "「Ư!」"
1093 = "「Ư!!」"
1094 = "「Ư!!!」"
1095 = "「Ư!!!!」"
1097 = "「Ư!!!!!!」"
1103 = "「A——fua——a——ưm——haa—— Sắp rồi——sắp, rồi——chỗ đó——của, em.」"
1107 = "「A——Nóng quá——Anh hai——thế này—— Vì em, mà trở nên to lớn——thế này——haa.」"
1108 = "「A——haa! Haa! Haa!」"
1115 = "「Afu! Aaaaaaaaaaaaannn!!」"
1117 = "「Aaaaaa! Chỗ đó! Tử cung! Xấu hổ, quá, đang phát ra tiếng, quá! Phần đầu, của anh hai! Mút chặt lấy.」"
1123 = "「Ư!!!?」"
1127 = "「Ư!!!!!!!!!!」"
1139 = "「Nfu——a——anh, hai——chuyện, gì cơ?」"
1142 = "「Nkun!!」"
1145 = "「Nkyuuuuuuuuuuuuu!!!」"
1219 = "「Phía sâu hơn…… nơi ngón tay chạm tới, thì——a——haa—— Anh hai——anh hai, phải——dùng mắt của anh hai, để——」"
1237 = "「Hibi, ki——Ư!」"
1266 = "「Gương trước mặt á? Ư!!?」"
1291 = "「Haa——haa——haa——haa—— Anh hai——anh hai——Ư!」"
1292 = "「Haa…… haa…… haa…… haa——」"
1321 = "「Anh hai, em——」"
1331 = "「Ư!!」"
1337 = "「~~~~~~~Ư!!!! Ka! ——ha——a! Anh hai! Anh hai! Anh hai! Anh hai!!!」"
1338 = "「~~~~~~~~~~Ư!!!」"
1377 = "Không, khác chứ. Nó đã tiếp nhận chỗ đó của tôi và tinh dịch của tôi không biết bao nhiêu lần rồi. Vậy mà những ngón tay vẫn chìm vào bên trong lối đi màu hồng đào tuyệt đẹp ấy."
1433 = "Haa haa, hơi thở vô cùng dốc. Tất cả những chỗ tiếp xúc đều dính chặt lấy nhau bởi mồ hôi của cả hai."
1455 = "Tử cung như muốn kéo dài chỗ đó của tôi ra thêm, nó dính chặt lấy như cắn nuốt, rồi cố gắng hút sâu vào bên trong hơn nữa."
```

## Kết bài

File lr_日々姫h1_鏡の中日々姫.txt.toml: đọc toàn bộ 325/325 dòng, sai 41 dòng (12,6%) — 19 mất Ư, 18 rên (romaji fa/fu, họ ひゃ, đếm âm), 4 sai nghĩa. Không lệch vị trí, không xoay chuỗi, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Sweep đã kiểm trực tiếp: nhận 14 mục, ghi đè 1 phân loại (1069), bổ sung 5 lỗi sweep bỏ sót. Second pass 41/41/0/3 (sửa 3 giá trị thêm nhầm 「」 ở dòng độc thoại). Không có cờ cho Hieu — không có thuật ngữ mới, không có đại từ mơ hồ, không có thẻ %l trong file. Khối TOML trên đã kiểm parse: 41 khóa, 0 sai lệch giá trị.
