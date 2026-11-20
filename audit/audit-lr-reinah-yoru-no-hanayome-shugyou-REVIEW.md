# Audit — lrれいな追加h_夜の花嫁修業 (04_Reina)

- File: `lrれいな追加h_夜の花嫁修業.txt.toml` — route 04_Reina, cảnh H: Reina trình diễn "khóa học làm dâu bí mật" do Paulette hướng dẫn (gel bôi trơn, kích thích lỗ hậu, tư thế cún, "thêm một ngón nữa", mười lần), xen kẽ độc thoại Soutetsu về cảm giác mới lạ và sự đồng thuận "trò nào cũng thử, không hợp thì dừng".
- Đọc: **365/365 dòng script** (key 710–1942), đối chiếu từng dòng với JP + TW (CSV3). Không lấy mẫu.
- TOML md5: `b6d6a52b2213d8bc98351a0f14d5ae91`; **1 bản duy nhất, không trùng lặp**. CSV3 1 bộ 365 dòng, key khớp tuyệt đối 365/365, 0 ô VN trống. VN khớp TOML tuyệt đối 365/365 (chỉ khác kiểu đã biết: TOML làm phẳng `\n` thật thành khoảng trắng; CSV3 là chuẩn). `[selections]` rỗng.
- Cơ sở tổng cộng (đã kiểm chứng với ROUTE-AUDIT.md): **111 file / 5.225 dòng sai**. LƯU Ý: base được giao lúc spawn là 110/5.203 đã cũ — trong lúc audit, file 仲国01 đã gộp xong (+22) nên ROUTE-AUDIT.md hiện kết ở 111/5.225; snippet dùng cơ sở này.

## §1. Kết quả

**33 dòng sai / 365 dòng = 9,0%.** Không có chuỗi xoay vòng, không có dòng mồ côi, không có dòng chưa dịch, không có trùng key, không có tràn file khác.

Phân loại:

| Loại | Số dòng | Key |
|---|---|---|
| Gasp っ (sweep đã liệt kê, kiểm chứng đúng) | 10 | 727, 1233, 1321, 1331, 1332, 1335, 1337, 1475, 1572, 1923 |
| Gasp っ (sweep bỏ sót, audit tìm thêm) | 9 | 723, 1060, 1075, 1092, 1122, 1126, 1132, 1175, 1942 |
| Tiếng cười diễn thành tiếng rên | 5 | 1056, 1059, 1185, 1186, 1251 |
| Sai nghĩa / bịa thêm | 3 | 1007, 1135, 1163 |
| Độ dài nguyên âm SFX | 6 | 1063, 1077, 1117, 1133, 1157, 1189 |

Theo người nói: Reina 16, Soutetsu 13, độc thoại 4. Thoại 29, lời dẫn 4.

## §2. Chi tiết từng dòng sai

### Gasp っ — sweep đã liệt kê, áp nguyên đã kiểm chứng (10 dòng)

- **727 [双鉄]** — JP 「――っ！！！！！」/ TW 「——！！！！！」/ Cũ: 「——っ!!!!!」 → **「——Ư!!!!!」** (raw-tsu).
- **1233 [れいな]** — JP 「花嫁、修行、の――っ――せいか――おもったより、すごく、ってっ――――。んしょ！」/ TW 「新娘課程的——學習成果——比想像中還要優秀——嘿咻！」/ Cũ: 「Khóa học, làm dâu, của——っ——thành quả——hơn cả mong đợi, tuyệt vời, quá——. Ưm!」 → **「Khóa học, làm dâu, của——Ư——thành quả——hơn cả mong đợi, tuyệt vời, quá——. Ưm!」** (chỉ thay っ thô thành Ư; giữ nguyên phần còn lại kể cả 「ってっ」→"quá" — って là trợ từ, không thêm Ư — và んしょ→"Ưm!" theo đúng giá trị sweep).
- **1321 [双鉄]** — JP 「ならばっ――もっとっ――っ！」/ TW 「那我就再激烈一點——！」/ Cũ: 「Nếu vậy thì——nhiều hơn nữa——!」 → **「Nếu vậy thì——nhiều hơn nữa——Ư!」** (chỉ っ đứng một mình cuối dòng được Ư; ならばっ/もっとっ là từ nội dung, không Ư).
- **1331 [双鉄]** — JP 「っ！！！」/ Cũ: 「っ!!!」 → **「Ư!!!」**.
- **1332 [双鉄]** — JP 「っ！！！！　――ぁくっ！」/ TW 「！！！！——啊唔！」/ Cũ: 「っ!!!! ——A hự!」 → **「Ư!!!! ——A hự!」** (ぁくっ→"A hự" đã đúng, giữ nguyên).
- **1335 [双鉄]** — JP 「～～～～～っっっ」/ Cũ: 「~~~~~っっっ」 → **「~~~~~ƯƯƯ」** (1 Ư cho mỗi っ, theo quy ước sweep).
- **1337 [双鉄]** — JP 「～～～～～～～～っ！！！」/ Cũ: 「~~~~~~~~!!!」 → **「~~~~~~~~Ư!!!」**.
- **1475 [monologue]** — JP 「っ！」/ Cũ: 「っ!」 → **「Ư!」**.
- **1572 [monologue]** — JP 「気づかなかった。れいなは手で亀頭をつつむようにして、精液を受け止めてくれている――っ！？」/ TW 「我現在才發現，難不成剛才玲奈的手包裹住了我的龜頭，全盤接納了迸射而出的精液——？！」/ Cũ: 「Tôi không hề nhận ra. Reina đang dùng tay bao lấy quy đầu, và hứng lấy toàn bộ tinh dịch——!?」 → **「...tinh dịch——Ư!?」**.
- **1923 [monologue]** — JP 「（尻穴を刺激されてるせいなのか……っ――ごく単純な勃起への刺激が、いつもより何倍も――）」/ Cũ: 「（Là do lỗ hậu đang bị kích thích sao……っ——Một kích thích đơn thuần lên dương vật thôi mà lại mạnh gấp mấy lần bình thường——）」 → **「（Là do lỗ hậu đang bị kích thích sao……Ư——Một kích thích đơn thuần lên dương vật thôi mà lại mạnh gấp mấy lần bình thường——）」**.

### Gasp っ — sweep bỏ sót, audit tìm thêm (9 dòng)

Quy tắc áp dụng (đã chốt 20/11, tiền lệ 仲国05 1956/2254 + 仲国05 1946): っ gắn với **từ-âm thanh** (vocalization) ở **cuối tuyệt đối của dòng, không có dấu câu theo sau** là gasp → thêm Ư; っ ở **đầu dòng** cũng là gasp → thêm Ư. Ngược lại KHÔNG sửa: っ gắn với từ nội dung (すきっ, もっとっ, tên riêng, động từ — vd. 1155, 1223, 1276, 1586), っ giữa dòng đã được diễn (あっ――→"A——", ふあっ――→"Phu a——" — tiền lệ 仲国05 §4: あっ→"A." giữ nguyên), っ đã được diễn bằng phụ âm cuối dứt khoát của VN (-t/-p/-c, "Hự", "Ực" — vd. ちゅっ→"Chụt", くっ→"Hự"), っ đơn sau âm mũi ん (んっ→"Ưm" — phụ âm mũi đóng âm tiết đã là điểm dừng), và SFX hành động dạng từ tượng thanh (ごちゅっ→"Phập", くりゅっ→"Xoay vòng" — っ hấp thụ vào cách diễn hành động). Một cụm っ (2+) cuối tuyệt đối được 1 Ư cho mỗi っ (theo sweep 1335: っっっ→ƯƯƯ).

- **723 [双鉄]** — JP 「――くっ――っふ――んぁっ」/ TW 「——唔——呼——嗯啊」/ Cũ: 「——Hự——ưm——a」 → **「——Hự——ưm——aƯ」** (んぁっ cuối tuyệt đối; くっ→"Hự" và っふ→"ưm" đã diễn, giữ nguyên).
- **1060 [双鉄]** — JP 「ふっ――あっ――あっ――くあっ」/ TW 「呼——啊——啊——唔啊」/ Cũ: 「Phù——a——a——ư a」 → **「Phù——a——a——ư aƯ」** (chỉ くあっ cuối dòng được Ư; các あっ giữa dòng giữ nguyên).
- **1075 [れいな]** — JP 「ふあああああああんっっっ」/ TW 「呼啊啊——」/ Cũ: 「Phu a a a a a a an」 → **「Phu a a a a a a anƯƯƯ」** (cụm っっっ cuối tuyệt đối; độ dài 7 nguyên âm a đã đúng — xem §2 cuối).
- **1092 [れいな]** — JP 「っひゅあっ！！？　ぢゅるって！　どちゅって！！」/ TW 「咿呀？！！滋滋的！啾啾的！！」/ Cũ: 「Hyu a!!? Sục vào! Đâm phập vào!!」 → **「ƯHyu a!!? Sục vào! Đâm phập vào!!」** (っ đầu dòng bị mất — cùng mẫu 仲国05 1946; っ cuối ひゅあっ có "!!?" theo sau nên giữ nguyên; なかにっ cuối dòng 2 là từ nội dung, giữ nguyên).
- **1122 [双鉄]** — JP 「あああああっ」/ TW 「啊——」/ Cũ: 「A a a a a」 → **「A a a a aƯ」**.
- **1126 [双鉄]** — JP 「あ――あっ――あっ」/ TW 「啊——啊——啊」/ Cũ: 「A——a——a」 → **「A——a——aƯ」** (chỉ あっ cuối dòng).
- **1132 [双鉄]** — JP 「あああっ」/ TW 「啊啊啊」/ Cũ: 「A a a」 → **「A a aƯ」**.
- **1175 [双鉄]** — JP 「んあっ」/ TW 「嗯啊」/ Cũ: 「Ư a」 → **「Ư aƯ」** (âm kết bằng あ, không phải ん, nên không áp dụng ngoại lệ mũi).
- **1942 [monologue]** — JP 「（びゅっ――びゅうっ――びゅるっ――ぶ――ぷっ）」/ TW 「（餘韻悠長）」/ Cũ: 「（Phụt——phụt——phụt——phù——phù）」 → **「（Phụt——phụt——phụt——phù——phùƯ）」** (ぷっ cuối tuyệt đối; 3 âm trước đã có -t, ぶ không có っ nên "phù" đúng).

### Tiếng cười diễn thành tiếng rên (5 dòng)

Quy tắc Hieu 19/11 22:05: tiếng cười (ふふっ/うふふ/んふふ) phải diễn thành tiếng cười, KHÔNG thành tiếng rên ("Ư hự"). Toàn bộ 6 dòng "Ư hư hư" trong file đều sai dạng này (1135 gộp vào mục sai nghĩa dưới đây vì còn lỗi nghĩa).

- **1056 [れいな]** — JP 「うふふぅ、次はぁ――ん……」/ TW 「呵呵，接下來……」/ Cũ: 「Ư hư hư~, tiếp theo là~——ưm……」 → **「Ufufu~, tiếp theo là~——ưm……」**.
- **1059 [れいな]** — JP 「うふふぅ。そうしたら、よごれないようにぃ」/ TW 「呵呵，這樣做就不怕被弄髒啦」/ Cũ: 「Ư hư hư~. Sau đó thì, để không bị bẩn nha~」 → **「Ufufu~. Sau đó thì, để không bị bẩn nha~」**.
- **1185 [れいな]** — JP 「うふふぅ。ええっとですねぇ、マニアックなプレイをふたりで一緒に楽しむほどに、夫婦の絆は深くなるって」/ TW 「嘻嘻。是這樣的，她說兩人可以用一些更刺激的玩法...」/ Cũ: 「Ư hư hư~. Ừm thì nha~, cô ấy bảo là hai người cùng nhau tận hưởng những trò chơi kỳ quái, thì tình cảm vợ chồng sẽ càng thêm gắn kết nha~」 → **「Ufufu~. Ừm thì nha~, ...」** (chỉ đổi tiếng cười).
- **1186 [れいな]** — JP 「んっふふぅ」/ TW 「嘻嘻嘻」/ Cũ: 「Ư hư hư~」 → **「Nfufu~」** (んっふふ = cười khúc khích bị nén: N + fufu + ~ cho ぅ).
- **1251 [れいな]** — JP 「"男の子も女の子も気持ちよくなれる"ってポーレットが。うふふぅ、そうてつさんも一緒なんですねぇ」/ TW 「波萊特說這個地方男生女生都很敏感也會很舒服。呵呵，雙鐵先生也是一樣的呢」/ Cũ: 「Chị Paulette bảo là "Cả con trai và con gái đều có thể sướng ở đây". Ư hư hư~, anh Soutetsu cũng giống vậy nhỉ.」 → **「... Ufufu~, anh Soutetsu cũng giống vậy nhỉ.」**.

### Sai nghĩa / bịa thêm (3 dòng)

- **1007 [れいな]** — JP là lời ngọng khi ngậm (「ほーへふひゃふほはははひ ひははひほほはふへふぁぃへふひょぉ」 — không giải mã được trực tiếp) / TW 「不會髒啦，雙鐵身上沒有髒的地方」(= "không bẩn đâu; trên người Soutetsu chẳng có chỗ nào bẩn") / Cũ: 「Anh Soutetsu không có bẩn đâu nha~ / Lúc nào cũng tắm rửa sạch sẽ mà nha~」 → **「Anh Soutetsu không có bẩn đâu nha~ / Trên người anh thì có chỗ nào bẩn đâu nha~」** (dòng 2 cũ bịa thêm "lúc nào cũng tắm rửa sạch sẽ" — không có trong JP lẫn TW; sửa theo TW).
- **1135 [れいな]** — JP 「はぁああん！　あっ――こんなに、きもち――いいこと、どうして――もっと、はやくっ――――んふふうっっ」/ TW 「啊啊啊啊嗯！啊——這麼、舒服——的事情，為什麼——不早點——嗯呼——」/ Cũ: 「Hà a a an! A——sướng——quá, sao lại——nhanh hơn, nữa đi————ưm hư hư」 → **「Hà a a an! A——chuyện sướng——thế này, sao——không làm sớm hơn——NfufuuƯƯ」** (3 lỗi gộp: "nhanh hơn, nữa đi" dịch sai nghĩa — TW rõ là "sao không làm sớm hơn" (vì sao không làm chuyện sướng thế này sớm hơn), không phải "đi nhanh hơn"; んふふうっっ là cười khúc khích, không phải rên — "Nfufuu" (N + fufu + u dài cho う) + ƯƯ cho cụm っっ cuối tuyệt đối; あっ giữa dòng giữ nguyên "A").
- **1163 [れいな]** — JP 「ん、ひょっ」/ TW 「嗯、嘿咻」/ Cũ: 「Ưm, hihi」 → **「Ưm, hự.」** (ひょっ là tiếng nhún/bật người khi gắng sức — TW 嘿咻 = "hây hố" — không phải tiếng cười; "hihi" biến âm thanh vận động thành cười, sai).

### Độ dài nguyên âm SFX (6 dòng)

Quy tắc đã chốt: số nguyên âm VN = 1 (âm gốc) + số ký tự う/ぅ trong token JP (tiền lệ h7 1651: う×10 → 11 u; lr_h2 1770: う×11 → 12 u, VN cũ đúng nên bị loại khỏi danh sách sửa). Áp dụng tương tự cho token あ/ぁ dài (âm gốc + số あ/ぁ kéo dài). Chỉ sửa token SFX thuần (rên dài); không sửa thán từ dạng từ (やぁ→"ya", わぁ→"Oa") hay SFX hành động đã Việt hoá (Phập, Trơn tuột...).

- **1063 [れいな]** — JP 「ふっ、きゅうううううううっっっっっっっっっっ！！」: token きゅううううううう = gốc きゅ (1 u) + う×7 = 8 u. Cũ "kyu" + 15 u = 16 u (gấp đôi). → **「Phù, kyu u u u u u u u!!」** (8 u; cụm っ có "!!" theo sau nên không thêm Ư).
- **1077 [れいな]** — JP 「ふああああああんっっっっ」: ふぁ gốc (1 a) + あ×5 = 6 a; cũ có 7 a (trùng hệt VN của 1075 dù JP ngắn hơn 1 âm — hai dòng gần giống nhau mà VN không phân biệt được). → **「Phu a a a a a anƯƯƯƯ」** (6 a + Ư×4 cho っっっっ).
- **1117 [双鉄]** — JP 「くあ……あっ――あっ――あぁぁ……」/ TW 「唔啊……啊——啊——啊啊啊……」: token cuối あぁぁ = gốc あ (1) + ぁ×2 = 3 a; cũ "a a" chỉ 2. → **「Kua……a——a——a a a……」**.
- **1133 [れいな]** — JP 「ひゅあああああああああああああああああぁんっ！！」: ひゅあ gốc (1 a) + あ×16 + ぁ×1 = 18 a; cũ 16 a (thiếu 2). → **「Hyu a a a a a a a a a a a a a a a a a an!!」** (18 a; っ có "!!" theo sau nên không thêm Ư).
- **1157 [れいな]** — JP 「んううううううっ――...」: token んうううううう = ん (0 nguyên âm) + う×6 = 6 u; cũ 7 u (thừa 1). → **「Ưm u u u u u u——anh Soutetsu, anh Soutetsu, nữa đi——nữa đi~——nè, anh Soutetsu ơi~」**.
- **1189 [れいな]** — JP 「ひっきゅううううううううぅぅぅぅぅぅぅぅぅん！！」: gốc きゅ (1 u) + う×9 + ぅ×8 = 18 u; cũ 16 u (thiếu 2). → **「Hi kyu u u u u u u u u u u u u u u u u u n!!」** (18 u).

## §3. Kiểm tra sweep っ cho file này

- `sweep-raw-gasp-wrong.json` có **10 mục** cho file này, cả 10 đều kiểm chứng đúng với JP và được áp dụng nguyên giá trị: 727, 1233, 1321, 1331, 1332, 1335, 1337, 1475, 1572, 1923 (§2). Lưu ý: 2 giá trị sweep (1572, 1923) đã làm phẳng `\n` của CSV3 thành khoảng trắng trong file sweep; audit đã khôi phục `\n` từ CSV3 để mỗi fix chỉ khác VN cũ đúng chỗ cần sửa.
- Audit tìm thêm **9 gasp** sweep bỏ sót (§2): 723, 1060, 1075, 1092, 1122, 1126, 1132, 1175, 1942 — đều là っ cuối tuyệt đối / đầu dòng mà mẫu sweep không liệt kê (sweep chủ yếu bắt っ thô còn sót trong VN và っ đứng một mình).
- Không có mục sweep nào sai cần loại.

## §4. Kiểm tra cấu trúc

- 0 dòng lệch vị trí / chuỗi xoay vòng (đọc toàn file, mạch hội thoại liền mạch; không có VN nào thuộc về key khác), 0 dòng mồ côi (mọi VN đều có JP/TW tương ứng), 0 dòng chưa dịch (0 ô VN trống; chỉ có 739 「♪」 trùng TW vì là ký tự nhạc), 0 trùng key (365 key duy nhất), 0 tràn file khác.
- 2 giá trị VN trùng nhau nhưng KHÔNG phải lệch dòng: 1075/1077 cùng 「Phu a a a a a a an」 (JP gần giống nhau, chỉ khác độ dài — 1077 đã sửa độ dài, xem §2); 1860/1905 cùng 「（Phụt! Phụt! Phụt! Phụt!）」 (cả hai JP đều là 4 âm phụt liên tiếp, cách diễn chung là hợp lệ).
- Tag %l: số lượng `\x` JP = VN trên mọi dòng, 0 mất cân bằng; 0 dấu 「 」 lệch. File này không dùng thẻ %l gloss nào.
- Đại từ: 12 dòng thoại Soutetsu có đại từ tự xưng, tất cả đều là "anh" (đúng với Reina); 0 lần "tôi" trong thoại Soutetsu (77 dòng còn lại là SFX/rên không có đại từ). Reina gọi "anh Soutetsu" nhất quán. Paulette được gọi "chị Paulette" nhất quán. Không sửa đại từ nào.
- Các dòng đã kiểm tra kỹ nhưng giữ nguyên (không tính sai):
  - **っ trên từ nội dung** (không thêm Ư): 1011 かっ, 1155 すきっ/そうてつさんっ, 1223 だっ, 1254 おくっ/ふかくっ, 1276 ほしいっ, 1586 通過するっ, 720 ではなくっ, 1446 ほしくてっ, 1574 とっ, 1644 ものはっ, 1705/1729 động từ + っ.
  - **っ giữa dòng đã được diễn**: 1125 あっ――→"A——", 1067/1068/1069 ふあっ――→"Phu a——", 1136/1137 ああっ!→"A a!", 1078 ふあ…あんっっ!!!! (có "!!!!" theo sau), 1081 ああっっっ!!! (có "!!!" theo sau), 1086 ヒャンっ――, 1090 ひゃうっ!, 1104 はっ!/ひゃうっ!, 1202 ふあっ――, 1259 あっ――, 1294 ふあっ――, 1474 ふあっ――/あっ――, 1868 あっ―― — theo tiền lệ 仲国05 §4 (thán từ đã được diễn, không mất âm).
  - **っ đã diễn bằng phụ âm cuối VN**: ちゅっ→"Chụt", くっ→"Hự", んくっ→"Ư hự", （ごくっっ）→"（Ực）", toàn bộ khối SFX độc thoại 1830–1941 (Phập/Chụt/Sụp soạp/Trơn tuột... đều có -t/-p/-c hoặc -m/-n đóng âm tiết).
  - **っ đơn sau ん** (phụ âm mũi đã đóng âm tiết): 736 んんっ→"ưm ưm", 1174 �んむっ/んっ→"Ưm", 1183 んっ→"Ưm", 1169 んくっ→"Ư hự".
  - **1160 んしょ→"ừm"**: giữ nguyên — sweep dùng "Ưm!" cho んしょ ở 1233, "ừm" là cùng cách diễn (chỉ khác chữ hoa/dấu câu), không tính sai.
  - **1110 ふぇひ→"Đây này!"**: giữ nguyên — lời ngọng không giải mã được, TW cũng chỉ gộp ý; "Đây này!" là thán từ hợp cảnh, không bịa nghĩa rõ.
  - **1006 "Không——không——hơn, thế nữa"** (JP 「いや――いやっ――それ、より」): giữ nguyên — lời nói lắp ngắt quãng, "hơn, thế nữa" đọc được thành "hơn thế nữa", khớp TW "不是這個" ở mức chấp nhận được.
  - **1011 "Kh, không——sướng, thì——đúng, nhưng"** (JP 「い、いや――気持ちいい、と――いう、かっ」): giữ nguyên — ngập ngừng phủ nhận/đính chính, khớp mạch TW.
  - **1073 "nhiều, thế này"** (JP 「こん、なにっ」= こんなに nói lắp): giữ nguyên — diễn đúng "nhiều thế này".
  - **"Phu a" cho ふぁ/ふあ/ぷあ** (~40 dòng, vd. 736, 1061, 1067): KHÔNG sửa trong audit này — chờ đợt thống nhất fa/fu (xem §6). Quy tắc đã chốt là ふぁ→"phà"/ふあ→"phùa", nhưng tiền lệ ハチロクh6 (14 dòng fa/fu) và lr_ふかみh2 đã đưa nhóm này vào đợt thống nhất sau khi audit xong toàn bộ, tránh sửa rời rạc từng file.
  - **ひあ→"Hi a" / ひゃ→"Hya"** (vd. 1087, 1104): giữ nguyên quy ước trong file; mâu thuẫn toàn dự án ("Hya" vs "Hia" vs "Á") đã được flag từ れいなh1, chờ Hieu chốt (xem §6).

## §5. Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 33 fix đối chiếu JP lần 2: **33 tổng / 33 kiểm chứng lại / 0 bỏ / 1 sửa**. Lượt 2 bắt được 1 lỗi ở fix 1135: bản sửa đầu đã làm mất 2 dấu gạch ngang (JP 「はやくっ――――んふふう」 có 4 gạch; bản sửa chỉ còn 2) — đã khôi phục đủ 4 gạch: "...không làm sớm hơn————NfufuuƯƯ".

Kiểm chứng cơ học: JSON 33 mục dạng chuẩn (key dạng string, đủ jp/tw/old_vn/fix/kind/character); jp/tw/old_vn khớp CSV3 tuyệt đối 33/33; khối TOML 33 khóa, parse được bằng tomllib, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô, kể cả `\n` literal); mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm tra diff từng dòng: 19 chèn Ư, 5 thay tiếng cười, 6 sửa độ dài nguyên âm, 3 sửa nghĩa).

## §6. Chờ Hieu (không tính sai, không tự quyết)

1. **Thống nhất fa/fu toàn file**: ~40 dòng dùng "Phu a" cho ふぁ/ふあ/ぷあ (vd. 736, 1061, 1067, 1073, 1074, 1081, 1102, 1202, 1294, 1474...). Theo quy tắc đã chốt thì ふぁ→"phà", ふあ→"phùa", nhưng nhóm này đã được đưa vào đợt thống nhất (cùng ハチロクh6 14 dòng + lr_ふかみh2) — cần Hieu chốt thời điểm/phạm vi đợt thống nhất.
2. **ひあ/ひゃ**: file này dùng "Hi a" cho ひあ (1087) và "Hya u" cho ひゃう (1051, 1104) — mâu thuẫn toàn dự án ("Hya" vs "Hia" vs "Á") đã flag từ れいなh1, chưa chốt.
3. **Ranh giới quy tắc gasp đã áp dụng trong file này** (ghi lại để parent/Hieu rà soát): chỉ thêm Ư cho っ cuối tuyệt đối không dấu câu theo sau (tiền lệ 仲国05 1956/2254) và っ đầu dòng (tiền lệ 1946); っ giữa dòng hoặc có dấu câu theo sau mà âm đã được diễn thì giữ nguyên (tiền lệ 仲国05 §4). Nếu Hieu muốn "không để mất âm" tuyệt đối (thêm Ư cho cả はっ→"Ha" giữa dòng), thì còn ~50 dòng nữa trong file này — đó là quyết định phạm vi, không phải lỗi sót.
4. **1163 ひょっ→"hự"**: cách diễn tiếng nhún người ("Hự" vs "Hây") là lựa chọn cảm tính theo ngữ cảnh; nếu Hieu có cách diễn chuẩn cho ひょっ thì ghi chú để thống nhất.

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
"723" = "「——Hự——ưm——aƯ」"
"727" = "「——Ư!!!!!」"
"1007" = "「Anh Soutetsu không có bẩn đâu nha~\\nTrên người anh thì có chỗ nào bẩn đâu nha~」"
"1056" = "「Ufufu~, tiếp theo là~——ưm……\\nChụt——chụt——chụt——liếm」"
"1059" = "「Ufufu~. Sau đó thì, để không bị bẩn nha~」"
"1060" = "「Phù——a——a——ư aƯ」"
"1063" = "「Phù, kyu u u u u u u u!!」"
"1075" = "「Phu a a a a a a anƯƯƯ」"
"1077" = "「Phu a a a a a anƯƯƯƯ」"
"1092" = "「ƯHyu a!!? Sục vào! Đâm phập vào!!\\nNóng quá! Nóng quá ập vào một lúc! Bên trong Reina」"
"1117" = "「Kua……a——a——a a a……」"
"1122" = "「A a a a aƯ」"
"1126" = "「A——a——aƯ」"
"1132" = "「A a aƯ」"
"1133" = "「Hyu a a a a a a a a a a a a a a a a a an!!」"
"1135" = "「Hà a a an! A——chuyện sướng——thế này, sao——không làm sớm hơn————NfufuuƯƯ」"
"1157" = "「Ưm u u u u u u——anh Soutetsu, anh Soutetsu,\\nnữa đi——nữa đi~——nè, anh Soutetsu ơi~」"
"1163" = "「Ưm, hự.」"
"1175" = "「Ư aƯ」"
"1185" = "「Ufufu~. Ừm thì nha~, cô ấy bảo là hai người cùng nhau\\ntận hưởng những trò chơi kỳ quái, thì tình cảm vợ chồng sẽ càng thêm gắn kết nha~」"
"1186" = "「Nfufu~」"
"1189" = "「Hi kyu u u u u u u u u u u u u u u u u u n!!」"
"1233" = "「Khóa học, làm dâu, của——Ư——thành quả——hơn cả mong đợi,\\ntuyệt vời, quá——. Ưm!」"
"1251" = "「Chị Paulette bảo là \\\"Cả con trai và con gái đều có thể sướng ở đây\\\".\\nUfufu~, anh Soutetsu cũng giống vậy nhỉ.」"
"1321" = "「Nếu vậy thì——nhiều hơn nữa——Ư!」"
"1331" = "「Ư!!!」"
"1332" = "「Ư!!!! ——A hự!」"
"1335" = "「~~~~~ƯƯƯ」"
"1337" = "「~~~~~~~~Ư!!!」"
"1475" = "Ư!"
"1572" = "Tôi không hề nhận ra. Reina đang dùng tay bao lấy quy đầu,\\nvà hứng lấy toàn bộ tinh dịch——Ư!?"
"1923" = "（Là do lỗ hậu đang bị kích thích sao……Ư——\\nMột kích thích đơn thuần lên dương vật thôi mà lại mạnh gấp mấy lần bình thường——）"
"1942" = "（Phụt——phụt——phụt——phù——phùƯ）"
```

## Kết bài

File lrれいな追加h_夜の花嫁修業: đọc 365 dòng, sai 33 dòng (9,0%) — file sạch về cấu trúc, lỗi tập trung ở gasp っ (19/33, trong đó 10 từ sweep + 9 sweep bỏ sót) và SFX (11/33: 5 tiếng cười diễn thành tiếng rên + 6 sai độ dài nguyên âm), còn lại 3 sai nghĩa. Không có lỗi hệ thống (xoay vòng, mồ côi, tràn file). Đại từ đúng toàn file (Soutetsu "anh" 12/12 dòng có đại từ, 0 lần "tôi" trong thoại). 4 điểm chờ Hieu đã ghi ở §6, trong đó quan trọng nhất là đợt thống nhất fa/fu (~40 dòng "Phu a") và ranh giới quy tắc gasp giữa dòng.
