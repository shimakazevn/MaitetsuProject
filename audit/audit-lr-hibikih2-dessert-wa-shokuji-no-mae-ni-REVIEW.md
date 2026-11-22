# Audit: lr_日々姫h2_デザートは食事の前に.txt.toml — 42/288 (14,6%)

- File: `02_Hibiki/lr_日々姫h2_デザートは食事の前に.txt.toml` (route 02_Hibiki, 288 dòng script; monologue 127, 日々姫 94, 双鉄 67). Nội dung: H-scene Hibiki — "món tráng miệng trước bữa ăn": sau 3 ngày làm việc liên tục, Hibiki đòi "ăn" Soutetsu trước khi ăn cơm thật; xen kẽ đối thoại, độc thoại Soutetsu và SFX dài (đặc biệt cụm SFX trong ngoặc 1651–1693).
- TOML md5 278bb98599c53cd1d22db62a29101c26, không có bản trùng (md5 không nằm trong 11 nhóm trùng của toml2); CSV3 1 bộ 288 dòng, key khớp tuyệt đối, VN khớp TOML 288/288 (chỉ khác dạng làm phẳng `\n`→khoảng trắng), 0 dòng VN trống. [selections] rỗng; 1 tag %l (1199, đúng quy ước — xem dưới); 0 tag lệch.
- Phân loại (42): gasp 13 (sweep 13, áp nguyên văn), moan 26 (đếm nguyên âm/phụ âm theo công thức 1 + số kana kéo dài), sai nghĩa 3 (1000 mất mora ん, 1060 いただきます thiếu đối tượng, 1352 イってた sai thì).
- Sweep gasp: 16 mục đã kiểm tra trực tiếp — áp nguyên văn 13 mục lost-gasp; 973 already-rendered nhưng đếm nguyên âm sai → sửa phần đếm (Guuu); 1079 + 1663 already-rendered đúng, giữ nguyên; +0 gasp sweep bỏ sót (quét cơ học toàn bộ dòng JP có っ: absolute-final và line-initial đã rà hết; các っ còn lại đều đã render thành âm VN hoặc gắn từ nội dung).
- Đại từ: không sửa dòng nào — Soutetsu "anh" với Hibiki nhất quán (6 dòng "anh", 0 dòng "tôi" sai), độc thoại "tôi" nhất quán (1423 "người anh" là danh từ vai trò "兄として", không phải tự xưng), Hibiki "em"/"anh hai" nhất quán (15 dòng "anh hai").
- Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. VN trùng duy nhất: 1000/1005 cùng "「A!」" — đã sửa 1000 → "An!" (JP khác nhau: あんっ vs あ). Không còn っ thô trong VN (quét toàn file: 0). Không rò rỉ CJK/Hàn trong VN (chỉ thuật ngữ JP trong tag %l ở 1199).
- Lượt soát 2: 42/42 tái kiểm chứng, 0 bỏ, 0 sửa. JSON 42 mục (key chuỗi); khối TOML 42 khóa parse OK, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 42/42; mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (trừ 1060 thêm "thưởng thức" và 1352 đổi thì).
- Chi tiết đầy đủ: `audit-lr-hibikih2-dessert-wa-shokuji-no-mae-ni-REVIEW.md`; danh sách sửa: `audit-lr-hibikih2-dessert-wa-shokuji-no-mae-ni-wrong.json` (42 mục).
- Cờ cho Hieu: (1) fa/fu "Fa"/"fa"/"famu"/"pua" (romaji) nhất quán toàn file (1106, 1172–1176, 1038, 1051, 1089) — "Phùa" vs "Fua" chưa chốt → đợt thống nhất; (2) おちんちん → "chỗ đó" (943) và "thứ cứng ngắc đó" (1157) — cùng uyển ngữ "chỗ đó" dùng cho cả おまんこ, có cần phân biệt không? (3) 1057 ふぇひあふぁれ → "meshiagare" (romaji, nói ngọng vì miệng đầy) — giữ nguyên, phán đoán audit; (4) 1304 giữ nguyên "tôi ngã xuống người em ấy" — JP cụt (僕は日々姫へ――) nhưng 1420 (倒れる) xác nhận hành động ngã; (5) SFX dài/dồn trong ngoặc → vòng moan: 1665/1666/1668 (độ dài render bằng chữ t: "Phụtttt"), 1676 ("chụtttt"), 1679 ("Kétttt"), 1681 ("Xoètttttt" cho ちいいいいいいっ), 1683 ("sụccc" cho しぃこっ); (6) っ giữa câu → vòng moan: 939 (ふっ→"fu", あっ→"a"), 984 (はぁっ→"ha"), 994 (中っ); (7) 942 わらひとっ → "Cùng nhau!" — わらひ (tôi, nói ngọng) gộp vào "cùng nhau", giữ nguyên; (8) 936 でぇっ → "tuyệt." — JP cụt, TW "也好舒服" ủng hộ, giữ nguyên; (9) 1199: JP [アペリティフ,2] → VN tag %l "rượu khai vị" — đúng quy ước (JP dùng ngoặc [term,N], VN render tag %l), không tính sai; (10) B19 vẫn park.

## Chi tiết từng dòng sửa

### 675 [monologue] — gasp

- JP: ――それでも一気に行ってくれない。\nまたも亀頭の先端だけを――っ！！？
- TW: ——但她還是沒有直接含住肉棒。又是隻愛撫龜頭……啊？！
- Cũ: ——Dù vậy em ấy vẫn không làm một mạch.\nLại chỉ ngậm mỗi phần đầu——!!?
- Mới: ——Dù vậy em ấy vẫn không làm một mạch.\nLại chỉ ngậm mỗi phần đầu——Ư!!?
- JP kết bằng またも亀頭の先端だけを――っ！！？ — っ tuyệt đối cuối dòng bị mất, VN chỉ còn "——!!?". Áp nguyên văn sweep lost-gasp-trailing.

### 691 [monologue] — gasp

- JP: ……日々姫は、多少綺麗にはこぼしているものの、\nそれでも全部、残さず飲みきってくれ――っ！
- TW: ……雖然多少漏了一點出來，但她還是把精液全喝了下去……唔！
- Cũ: ……Dù có hơi tràn ra một chút,\nnhưng Hibiki vẫn uống cạn toàn bộ, không chừa lại giọt nào——!
- Mới: ……Dù có hơi tràn ra một chút,\nnhưng Hibiki vẫn uống cạn toàn bộ, không chừa lại giọt nào——Ư!
- JP kết bằng 飲みきってくれ――っ！ — っ tuyệt đối cuối dòng bị mất. Áp nguyên văn sweep lost-gasp-trailing.

### 937 [日々姫] — moan

- JP: 「ひゅぁぁぁぁぁぁぁぁぁぁぁぁっぁぁんんっっ！！！」
- TW: 「呀啊啊啊啊啊啊啊！！！」
- Cũ: 「Hyuaaaaaaaaaaaaaaaaaannnnn!!!」
- Mới: 「Hyuaaaaaaaaaaaaaann!!!」
- JP: ひゅぁ×12 + っぁぁ = 14 a, んん = 2 n. VN thừa 4 a (18) và 3 n (5) → 14 a + nn. Công thức đếm nguyên âm: số lượng kana.

### 971 [双鉄] — gasp

- JP: 「～～～っっっ！！」
- TW: 「唔！！」
- Cũ: 「~~~!!!」
- Mới: 「~~~ƯƯƯ!!!」
- JP 「～～～っっっ！！」 — 3 っ cuối dòng bị mất. Áp nguyên văn sweep: 3 Ư.

### 972 [双鉄] — gasp

- JP: 「っ！！！」
- TW: 「唔！！！」
- Cũ: 「!!!」
- Mới: 「Ư!!!」
- JP 「っ！！！」 toàn dòng là っ — VN chỉ còn "!!!". Áp nguyên văn sweep.

### 973 [双鉄] — moan

- JP: 「ぐうぅ～～～っっっっ！！！！」
- TW: 「唔！！！！」
- Cũ: 「Guuuuu~~~~!!!!」
- Mới: 「Guuu~~~~!!!!」
- JP ぐうぅ = 3 u (ぐ + う + ぅ). VN "Guuuuu" 5 u → "Guuu". Sweep đã xếp already-rendered (っ đã render) nhưng đếm nguyên âm sai — sửa phần đếm.

### 996 [日々姫] — moan

- JP: 「じゅびゅっ！　ずぼっ！　じゅぶっ！　ぢゅむっ！\nぢゅぽっ！　じゅばっ！　じゅううっ！　ぐぽっ！」
- TW: 「啊嗯……啊嗚……啾、啾嚕……啾嚕……嗚……咕嘟……噗！」
- Cũ: 「Jubyu! Zubo! Jubu! Jyumu!\nJyupo! Juba! Juuuu! Gupo!」
- Mới: 「Jubyu! Zubo! Jubu! Jyumu!\nJyupo! Juba! Juuu! Gupo!」
- JP じゅううっ = 3 u (じゅ + うう). VN "Juuuu" 4 u → "Juuu".

### 1000 [日々姫] — meaning

- JP: 「あんっ！」
- TW: 「啊嗯！」
- Cũ: 「A!」
- Mới: 「An!」
- JP 「あんっ！」 — mora ん bị mất: VN "A!" → "An!". Đồng thời giải quyết VN trùng với 1005 (「あ！」→ "A!" đúng).

### 1001 [日々姫] — moan

- JP: 「んっっっ！！！きゅぅぅぅぅぅぅぅぅぅんんっ！！！」
- TW: 「啊嗯！呀啊啊啊啊！！！」
- Cũ: 「Ưm!!! Kyuuuuuuuuun!!!」
- Mới: 「Ưm!!! Kyuuuuuuuuuunn!!!」
- JP きゅ + ぅ×9 = 10 u, んん = 2 n. VN 9 u + 1 n → 10 u + nn.

### 1004 [日々姫] — moan

- JP: 「んきゅんんんっ！！！！」
- TW: 「啊嗯！！！！」
- Cũ: 「Nkyunnnn!!!!」
- Mới: 「Nkyunnn!!!!」
- JP んきゅんんんっ — んんん = 3 n. VN "Nkyunnnn" 4 n → "Nkyunnn".

### 1006 [双鉄] — gasp

- JP: 「っ！！」
- TW: 「啊！！」
- Cũ: 「!!」
- Mới: 「Ư!!」
- JP 「っ！！」 toàn dòng là っ — VN chỉ còn "!!". Áp nguyên văn sweep.

### 1009 [日々姫] — gasp

- JP: 「っ！！！！！」
- TW: 「啊！！！！！」
- Cũ: 「!!!!!」
- Mới: 「Ư!!!!!」
- JP 「っ！！！！！」 toàn dòng là っ — VN chỉ còn "!!!!!". Áp nguyên văn sweep.

### 1010 [双鉄] — gasp

- JP: 「っ！！！！！！」
- TW: 「啊！！！！！！」
- Cũ: 「!!!!!!」
- Mới: 「Ư!!!!!!」
- JP 「っ！！！！！！」 toàn dòng là っ — VN chỉ còn "!!!!!!". Áp nguyên văn sweep.

### 1013 [双鉄] — gasp

- JP: 「っ！？」
- TW: 「啊？！」
- Cũ: 「!?」
- Mới: 「Ư!?」
- JP 「っ！？」 toàn dòng là っ — VN chỉ còn "!?". Áp nguyên văn sweep.

### 1016 [日々姫] — moan

- JP: 「ちゅむっ――れるうっ――ちゅっ――ちゅっ、ちゅっ、\nれりゅううっ――れろっ――ちゅうううううううっ！！」
- TW: 「啾……啾……啾嚕嚕嚕……啾嚕……啾嚕……咕嘟……啾！！！」
- Cũ: 「Chụt——reruu——chụt——chụt, chụt,\nreryuu——rero——chuuuuuuu!!」
- Mới: 「Chụt——reruu——chụt——chụt, chụt,\nreryuuu——rero——chuuuuuuuu!!」
- JP れりゅううっ = 3 u → "reryuuu" (VN 2 u); ちゅうううううううっ = 8 u (ちゅ + う×7) → "chuuuuuuuu" (VN 7 u).

### 1017 [日々姫] — moan

- JP: 「んぶっ！？　んっ――あ"っ――ぐっ――んっ！\nでゅぼっ！　ぢゅるっ！　ずびゅっ！　ぢゅぼおっ！」
- TW: 「啾……啾……啾嚕嚕嚕啾嚕……啾嚕……咕嘟……啾！」
- Cũ: 「Nbu!? Ưm——a——hự——ưm!\nDyubo! Jyuru! Zubyu! Jyubooo!」
- Mới: 「Nbu!? Ưm——a——hự——ưm!\nDyubo! Jyuru! Zubyu! Jyuboo!」
- JP ぢゅぼおっ = 2 o (ぼ + お). VN "Jyubooo" 3 o → "Jyuboo".

### 1035 [日々姫] — moan

- JP: 「ぺろっっ――ふふっ、ちょこっとしょっぱいチーズ味？\nクセばあるけど――これはこれで――ん～～れろおおっ」
- TW: 「啾嚕……嘿嘿，感覺像鹹鹹的起司味。味道挺特別的，不過也不錯……嗯……啾嚕嚕」
- Cũ: 「Liếm——fufu, vị phô mai hơi mặn mặn?\nHơi kén người ăn đấy——nhưng thế này cũng——ưm~~ reroo」
- Mới: 「Liếm——fufu, vị phô mai hơi mặn mặn?\nHơi kén người ăn đấy——nhưng thế này cũng——ưm~~ rerooo」
- JP れろおおっ = 3 o (ろ + おお). VN "reroo" 2 o → "rerooo".

### 1036 [日々姫] — moan

- JP: 「あ～～――ん～――れるっ――ぺりゅっ――ん……\nれりゅうううっ――れるっ――ぺろっ――れちゅんっ」
- TW: 「啾嚕、啾啾……啾嚕嚕嚕！啾嚕嚕……啾嚕……咕啾」
- Cũ: 「A~~——ưm~——liếm——nhóp nhép——ưm……\nReryuuu——liếm——liếm nhẹ——rechun」
- Mới: 「A~~——ưm~——liếm——nhóp nhép——ưm……\nReryuuuu——liếm——liếm nhẹ——rechun」
- JP れりゅうううっ = 4 u (りゅ + ううう). VN "Reryuuu" 3 u → "Reryuuuu".

### 1037 [日々姫] — moan

- JP: 「でゅるっ！　ぢゅぼっ！　じゅっ！　ぢゅううっっ！\nぼぢゅっ！　ちゅりゅっ！　ぢゅぼっ！　ぢゅばっ！！」
- TW: 「啾嚕、啾啾……啾嚕嚕嚕！啾嚕嚕……啾嚕……咕啾！！」
- Cũ: 「Dyuru! Jyubo! Ju! Jyuuuu!\nBojyu! Churyu! Jyubo! Jyuba!!」
- Mới: 「Dyuru! Jyubo! Ju! Jyuuu!\nBojyu! Churyu! Jyubo! Jyuba!!」
- JP ぢゅううっっ = 3 u (ぢゅ + うう). VN "Jyuuuu" 4 u → "Jyuuu".

### 1038 [日々姫] — gasp

- JP: 「はむっ――れるっ――あむっ――ちゅうっ――はむっ、\nちゅっ――ふぁむっ――ちゅうっ――んっ――っ！！！」
- TW: 「啾嚕、啾啾……啾嚕嚕嚕！啾嚕嚕……啾嚕……咕啾！！！！」
- Cũ: 「Hamu——reru——amu——chuu——hamu,\nChu——famu——chuu——ưm——!!!」
- Mới: 「Hamu——reru——amu——chuu——hamu,\nChu——famu——chuu——ưm——Ư!!!」
- JP kết bằng ちゅうっ――んっ――っ！！！ — っ cuối bị mất. Áp nguyên văn sweep (khôi phục \n theo CSV3).

### 1042 [日々姫] — moan

- JP: 「ん……はぁ――んっ――ちゅむっ――れろっ――ちゅっ、\nれりゅううっ――れろっ――しゃぶっ――れるううっ」
- TW: 「啾嚕嚕嚕……啾嚕……啾嚕……咕嘟。啾、啾嚕、啾嚕嚕……啾嚕嚕嚕」
- Cũ: 「Ưm…… ha——ưm——chụt——rero——chụt,\nreryuu——rero——mút——reruuu」
- Mới: 「Ưm…… ha——ưm——chụt——rero——chụt,\nreryuuu——rero——mút——reruuu」
- JP れりゅううっ = 3 u. VN "reryuu" 2 u → "reryuuu". (れるううっ = 3 u đã đúng "reruuu".)

### 1043 [日々姫] — moan

- JP: 「ぢゅぼおおおおおおおおおおおっ！！　ぢゅみゅっ！」
- TW: 「啾嚕嚕嚕嚕嚕嚕！啾！」
- Cũ: 「Jyubooooooooooooo!! Jyumu!」
- Mới: 「Jyuboooooooooooo!! Jyumu!」
- JP ぢゅぼ + お×11 = 12 o. VN 13 o → 12 o.

### 1044 [日々姫] — moan

- JP: 「ちゅむっ――ちゅううっ――れりゅっ――れろおおっ\nちゅっ、ちゅっ、ちゅっ、ちゅっ！　ちろっ、ちろおっ」
- TW: 「啾嚕！啾噗！啾嚕嚕嚕！咕啾、啾、啾、啾……噗啾」
- Cũ: 「Chụt——chuuuu——reryu——rerooo\nChụt, chụt, chụt, chụt! Chiro, chiroo」
- Mới: 「Chụt——chuuu——reryu——rerooo\nChụt, chụt, chụt, chụt! Chiro, chiroo」
- JP ちゅううっ = 3 u. VN "chuuuu" 4 u → "chuuu". (ちろおっ = 2 o đã đúng "chiroo".)

### 1045 [日々姫] — moan

- JP: 「ちゅううううううっ！　んっ……ごくっ――ふ、あ\n――れるっ――れろおおっ――チュむっ――ちゅううっ」
- TW: 「啾嚕！啾噗！啾嚕嚕嚕！咕嘟……啾、啾、啾……噗啾！」
- Cũ: 「Chuuuuuuu! Ưm…… ực——fu, a\n——liếm——rerooo——chụt——chuuuu」
- Mới: 「Chuuuuuuu! Ưm…… ực——fu, a\n——liếm——rerooo——chụt——chuuu」
- JP ちゅううっ (dòng 2) = 3 u. VN "chuuuu" 4 u → "chuuu". (Dòng 1 ちゅううううううっ = 7 u đã đúng "Chuuuuuuu".)

### 1046 [日々姫] — moan

- JP: 「れっるっ――ぺろっ――ちゅっ――ちゅううっ――\nん……ぺろっ――れりゅっ――ぺろっ――じゅずうっ！」
- TW: 「啾嚕！啾噗！啾嚕嚕嚕！咕嘟……啾、啾、啾、啾嚕嚕嚕！！」
- Cũ: 「Liếm——liếm nhẹ——chụt——chuuuu——\nƯm…… liếm nhẹ——reryu——liếm nhẹ——juzuu!」
- Mới: 「Liếm——liếm nhẹ——chụt——chuuu——\nƯm…… liếm nhẹ——reryu——liếm nhẹ——juzuu!」
- JP ちゅううっ = 3 u. VN "chuuuu" 4 u → "chuuu".

### 1060 [日々姫] — meaning

- JP: 「う、うん。あの――いただきます」
- TW: 「嗯……我開動了」
- Cũ: 「Ư, vâng. Vậy——em xin phép.」
- Mới: 「Ư, vâng. Vậy——em xin phép thưởng thức.」
- JP いただきます (trước bữa ăn) — VN "em xin phép" thiếu đối tượng. Sửa "em xin phép thưởng thức" cho nhất quán với 1117 (cùng いただきます) và TW 我開動了.

### 1066 [日々姫] — moan

- JP: 「んっ！　ぢゅりゅううううううううっっっっっっ！！」
- TW: 「嗯！啾嚕嚕嚕嚕嚕！」
- Cũ: 「Ưm! Jyuryuuuuuuuuuuuu!!」
- Mới: 「Ưm! Jyuryuuuuuuuuu!!」
- JP ぢゅりゅ + う×8 = 10 u. VN 13 u → 10 u ("Jyury" + 9 u).

### 1070 [日々姫] — moan

- JP: 「うん。結構匂うとよ？　けどね？　にぃにの匂いやけん。\n（すーーーーーーーーーーーーーーーーーーっ）」
- TW: 「嗯，味道挺大的。不過這是阿哥的味道嘛。（深呼吸）」
- Cũ: 「Vâng. Khá là nặng mùi đấy? Nhưng mà nhé? Là mùi của anh hai mà.\n（Hítttttttttttttttttttttttt）」
- Mới: 「Vâng. Khá là nặng mùi đấy? Nhưng mà nhé? Là mùi của anh hai mà.\n（Híttttttttttttttttttt）」
- JP （す + ー×18) = 19 đơn vị. VN "Hít" + t×24 (24 t) → t×19.

### 1077 [日々姫] — moan

- JP: 「んっ！？　んんんん～っ！　んっ――！　ふっ！\nごきゅっ！　ごくっ！　ぐきゅっ！！　ごきゅん！」
- TW: 「嗯？！嗚嗚嗚……嗚！嗚嗚……咕嘟、咕嘟……啊嗚！」
- Cũ: 「Ưm!? Ưmmmmm~! Ưm——! Fu!\nGokyu! Ực! Gukyu!! Gokyun!」
- Mới: 「Ưm!? Ưmmmm~! Ưm——! Fu!\nGokyu! Ực! Gukyu!! Gokyun!」
- JP �んんんん = 4 m (～ là dấu kéo dài riêng). VN "Ưmmmmm" 5 m → "Ưmmmm".

### 1081 [日々姫] — moan

- JP: 「えへへへへ！　ありがとにぃに！\n私、うれしかーーーーっ！」
- TW: 「嘿嘿！謝謝阿哥！我好開心！」
- Cũ: 「Ehehehehe! Cảm ơn anh hai!\nEm vui lắmmmm!」
- Mới: 「Ehehehehe! Cảm ơn anh hai!\nEm vui lắmmmmm!」
- JP うれしか + ー×4 → 5 m (1 gốc trong "lắm" + 4). VN 4 m → 5 m.

### 1083 [日々姫] — moan

- JP: 「えへへへっ！　ありがと！　うれしかとーーっ！！」
- TW: 「嘿嘿，謝謝！我好開心！！」
- Cũ: 「Ehehehe! Cảm ơn anh! Em vui lắmmmm!!」
- Mới: 「Ehehehe! Cảm ơn anh! Em vui lắmmm!!」
- JP うれしかと + ー×2 → 3 m. VN 4 m → 3 m. (Chú ý: 1081 và 1083 cũ đều "lắmmmm" — một trong hai chắc chắn sai theo số ー.)

### 1088 [日々姫] — moan

- JP: 「（ふはーーーーーっ）……んふふっ、えへへへっ！\n私には、ね？　世界で一番、美味しそうな匂いやけん」
- TW: 「噗哈……哼哼，哎嘿嘿！對我來說呀，這就是世界上最好聞的氣味」
- Cũ: 「（Fuhaaaaa）……Nfufu, ehehehe!\nVới em, nhé? Là mùi hương thơm ngon nhất thế giới đó.」
- Mới: 「（Fuhaaaaaa）……Nfufu, ehehehe!\nVới em, nhé? Là mùi hương thơm ngon nhất thế giới đó.」
- JP ふは + ー×5 = 6 a. VN "Fuhaaaaa" 5 a → "Fuhaaaaaa".

### 1146 [双鉄] — gasp

- JP: 「日々姫――日々姫――一緒に、一緒にっ――っ！！！」
- TW: 「日日姬……日日姬，我們一起！！！」
- Cũ: 「Hibiki——Hibiki——cùng nhau, cùng nhau nhé——!!!」
- Mới: 「Hibiki——Hibiki——cùng nhau, cùng nhau nhé——Ư!!!」
- JP kết bằng 一緒にっ――っ！！！ — っ cuối bị mất. Áp nguyên văn sweep.

### 1168 [日々姫] — gasp

- JP: 「は――あ――なに、これっ――！　――とま、って、て\n――も――にぃに――膣内に――いる、だけで――っ」
- TW: 「蛤啊……怎麼回事……就、就算停下來……阿哥的肉棒……放在小穴裡就感覺好舒服」
- Cũ: 「Ha——a——gì, thế này——! ——Dù, dừng, lại\n——thì——anh hai——chỉ cần, ở bên trong——thôi, là——」
- Mới: 「Ha——a——gì, thế này——! ——Dù, dừng, lại\n——thì——anh hai——chỉ cần, ở bên trong——thôi, là——Ư」
- JP kết bằng いる、だけで――っ — っ tuyệt đối cuối dòng bị mất. Áp nguyên văn sweep.

### 1352 [monologue] — meaning

- JP: イキたい。イってた。絞られていた。今喉を動かしている\n強い思いが――切なる願いが、もしも欠けていたのなら。
- TW: 好想射出來，小穴緊緊鎖住了肉棒。但心中的強烈情感與真摯願望，驅動著我說了出來。
- Cũ: Muốn xuất tinh. Sắp xuất tinh. Bị vắt kiệt. Những suy nghĩ mãnh liệt\nđang rung lên trong cổ họng——nếu thiếu đi khao khát cháy bỏng này.
- Mới: Muốn xuất tinh. Đang lên đỉnh. Bị vắt kiệt. Những suy nghĩ mãnh liệt\nđang rung lên trong cổ họng——nếu thiếu đi khao khát cháy bỏng này.
- JP イってた (quá khứ/tiếp diễn: đang lên đỉnh) ≠ "Sắp xuất tinh" (sắp — thì tương lai). Sửa "Đang lên đỉnh". TW không dịch trực tiếp cụm này.

### 1572 [monologue] — gasp

- JP: いうなりふっと、日々姫の瞳が柔ら――っ！？
- TW: 話音未落，日日姬的眼神裡就充滿了柔情……唔？！
- Cũ: Vừa dứt lời, ánh mắt Hibiki bỗng trở nên dịu dàng——!?
- Mới: Vừa dứt lời, ánh mắt Hibiki bỗng trở nên dịu dàng——Ư!?
- JP kết bằng 柔ら――っ！？ — っ tuyệt đối cuối dòng bị mất. Áp nguyên văn sweep.

### 1594 [monologue] — gasp

- JP: 日々姫の喉奥に僕の亀頭が口づけ――っ！！！？
- TW: 龜頭頂到了日日姬的喉嚨深處……啊！
- Cũ: Phần đầu của tôi hôn lên sâu trong cổ họng Hibiki——!!!?
- Mới: Phần đầu của tôi hôn lên sâu trong cổ họng Hibiki——Ư!!!?
- JP kết bằng 口づけ――っ！！！？ — っ tuyệt đối cuối dòng bị mất. Áp nguyên văn sweep.

### 1658 [monologue] — moan

- JP: （ぶぢゅ！　ずびゅううっ――ぐうううっ！　ごちゅ！）
- TW: （咕啾、咕啾！）
- Cũ: （Bạch! Trượt vàooo——hựựự! Hự!）
- Mới: （Bạch! Trượt vàooo——hựựựự! Hự!）
- JP ぐうううっ = 4 u (ぐ + ううう). VN "hựựự" 3 ự → "hựựựự". (ずびゅううっ = 3 o đã đúng "vàooo".)

### 1660 [monologue] — moan

- JP: （きゅうううううっ！）
- TW: （咕啾！）
- Cũ: （Thắt chặt lạiiiii!）
- Mới: （Thắt chặt lạiiiiii!）
- JP きゅうううううっ = 6 u (きゅ + う×5). VN 5 i → 6 i.

### 1686 [monologue] — moan

- JP: （きゅううううううううううんんっっっっっ！！！）
- TW: （縮緊！！！）
- Cũ: （Thắt chặt lạiiiiiiiiiiiii!!!）
- Mới: （Thắt chặt lạiiiiiiiiiii!!!）
- JP きゅ + う×10 = 11 u. VN 13 i → 11 i.

### 1687 [monologue] — moan

- JP: （じゅりゅうううううううううっっっっっっっ！！）
- TW: （縮緊！！）
- Cũ: （Trượt vàooooooooooo!!）
- Mới: （Trượt vàoooooooooo!!）
- JP りゅ + う×9 = 10 u. VN 11 o → 10 o.

### 1688 [monologue] — moan

- JP: （きゅううううっ！）
- TW: （縮緊！）
- Cũ: （Siết chặt lạiii!）
- Mới: （Siết chặt lạiiiii!）
- JP きゅ + う×4 = 5 u. VN 3 i → 5 i.

## Khối TOML (đã parse-kiểm chứng: 42 khóa, 0 sai lệch)

```toml
[script]
"675" = "——Dù vậy em ấy vẫn không làm một mạch.\\nLại chỉ ngậm mỗi phần đầu——Ư!!?"
"691" = "……Dù có hơi tràn ra một chút,\\nnhưng Hibiki vẫn uống cạn toàn bộ, không chừa lại giọt nào——Ư!"
"937" = "「Hyuaaaaaaaaaaaaaann!!!」"
"971" = "「~~~ƯƯƯ!!!」"
"972" = "「Ư!!!」"
"973" = "「Guuu~~~~!!!!」"
"996" = "「Jubyu! Zubo! Jubu! Jyumu!\\nJyupo! Juba! Juuu! Gupo!」"
"1000" = "「An!」"
"1001" = "「Ưm!!! Kyuuuuuuuuuunn!!!」"
"1004" = "「Nkyunnn!!!!」"
"1006" = "「Ư!!」"
"1009" = "「Ư!!!!!」"
"1010" = "「Ư!!!!!!」"
"1013" = "「Ư!?」"
"1016" = "「Chụt——reruu——chụt——chụt, chụt,\\nreryuuu——rero——chuuuuuuuu!!」"
"1017" = "「Nbu!? Ưm——a——hự——ưm!\\nDyubo! Jyuru! Zubyu! Jyuboo!」"
"1035" = "「Liếm——fufu, vị phô mai hơi mặn mặn?\\nHơi kén người ăn đấy——nhưng thế này cũng——ưm~~ rerooo」"
"1036" = "「A~~——ưm~——liếm——nhóp nhép——ưm……\\nReryuuuu——liếm——liếm nhẹ——rechun」"
"1037" = "「Dyuru! Jyubo! Ju! Jyuuu!\\nBojyu! Churyu! Jyubo! Jyuba!!」"
"1038" = "「Hamu——reru——amu——chuu——hamu,\\nChu——famu——chuu——ưm——Ư!!!」"
"1042" = "「Ưm…… ha——ưm——chụt——rero——chụt,\\nreryuuu——rero——mút——reruuu」"
"1043" = "「Jyuboooooooooooo!! Jyumu!」"
"1044" = "「Chụt——chuuu——reryu——rerooo\\nChụt, chụt, chụt, chụt! Chiro, chiroo」"
"1045" = "「Chuuuuuuu! Ưm…… ực——fu, a\\n——liếm——rerooo——chụt——chuuu」"
"1046" = "「Liếm——liếm nhẹ——chụt——chuuu——\\nƯm…… liếm nhẹ——reryu——liếm nhẹ——juzuu!」"
"1060" = "「Ư, vâng. Vậy——em xin phép thưởng thức.」"
"1066" = "「Ưm! Jyuryuuuuuuuuu!!」"
"1070" = "「Vâng. Khá là nặng mùi đấy? Nhưng mà nhé? Là mùi của anh hai mà.\\n（Híttttttttttttttttttt）」"
"1077" = "「Ưm!? Ưmmmm~! Ưm——! Fu!\\nGokyu! Ực! Gukyu!! Gokyun!」"
"1081" = "「Ehehehehe! Cảm ơn anh hai!\\nEm vui lắmmmmm!」"
"1083" = "「Ehehehe! Cảm ơn anh! Em vui lắmmm!!」"
"1088" = "「（Fuhaaaaaa）……Nfufu, ehehehe!\\nVới em, nhé? Là mùi hương thơm ngon nhất thế giới đó.」"
"1146" = "「Hibiki——Hibiki——cùng nhau, cùng nhau nhé——Ư!!!」"
"1168" = "「Ha——a——gì, thế này——! ——Dù, dừng, lại\\n——thì——anh hai——chỉ cần, ở bên trong——thôi, là——Ư」"
"1352" = "Muốn xuất tinh. Đang lên đỉnh. Bị vắt kiệt. Những suy nghĩ mãnh liệt\\nđang rung lên trong cổ họng——nếu thiếu đi khao khát cháy bỏng này."
"1572" = "Vừa dứt lời, ánh mắt Hibiki bỗng trở nên dịu dàng——Ư!?"
"1594" = "Phần đầu của tôi hôn lên sâu trong cổ họng Hibiki——Ư!!!?"
"1658" = "（Bạch! Trượt vàooo——hựựựự! Hự!）"
"1660" = "（Thắt chặt lạiiiiii!）"
"1686" = "（Thắt chặt lạiiiiiiiiiii!!!）"
"1687" = "（Trượt vàoooooooooo!!）"
"1688" = "（Siết chặt lạiiiii!）"
```

## Kết bài

File lr_日々姫h2_デザートは食事の前に.txt.toml: 288 dòng đã đọc đủ, 42 dòng sai (14,6%) — 13 gasp theo sweep, 26 moan đếm nguyên âm/phụ âm, 3 sai nghĩa. Không lệch dòng, không nhiễm chéo, không dòng mồ côi/chưa dịch/trùng khóa; đại từ Soutetsu–Hibiki nhất quán; sweep gasp đã rà trực tiếp 16 mục. Lượt soát 2: 42/42 tái kiểm chứng, 0 bỏ, 0 sửa. Đây là 1 trong 3 file H cuối cùng chưa audit; vòng moan sẽ nhận file này sau khi merge để rà các SFX dài và っ giữa câu đã cờ ở trên.
