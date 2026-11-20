# Audit — 日々姫03_客車手配.txt.toml (02_Hibiki)

- File: `02_Hibiki/日々姫03_客車手配.txt.toml` — 504 dòng, audit 504/504 (đọc từng dòng đối chiếu JP + TW).
- Kết quả: **41/504 dòng sai (8,1%)**.
- Phân loại: terminology 27, pronoun 5, rotation 3, gasp 3, mistranslation 2, sfx 1.
- Thoại 32/273 (11,7%), độc thoại 9/231 (3,9%). Theo nhân vật: ポーレット 11, monologue 9, 双鉄 7, 日々姫 5, ハチロク 5, れいな 2, ふかみ 1, 凪 1.
- 0 contamination / 0 orphan / 0 untranslated / 0 duplicate key / 2 uncertain (2530, 2603 — xem § Phán đoán).
- Nội dung file: Soutetsu, Hibiki, Paulette, Hachiroku, Reina, Nagi, Fukami bàn chuyện tìm mua toa hành khách cho 8620 — vay trái phiếu đường sắt thời Teitetsu, nhờ Đường sắt Suntai nhượng lại toa cải tạo từ toa xe tự hành, vận chuyển từ Shizuoka về Ohitoyo; xen kẽ cảnh pha trà (sadou/doesu) và Hibiki học về toa xe.

## §1 — Xoay vòng 3 dòng (2447 / 3220 / 3662) — phát hiện chính của file

Ba giá trị VN bị xoay vòng theo chu trình 3 dòng, đã kiểm chứng bằng tìm kiếm toàn dự án (CSV3 + toàn bộ TOML):

- 2447 [双鉄] JP 「ああ、真闇姉のところだ」 ("À, chị ấy đang ở chỗ chị Mayami") — VN hiện tại là "Giọng nói của Hibiki lại khiến tôi thở phào một lần nữa." — đó chính là bản dịch của JP 3662 (日々姫の声に、またホっとする).
- 3220 [monologue] JP 「が、理由を思えばどうどうめぐりだ。意識せぬよう、とにかく言葉を続けてしまう。」 — VN hiện tại là "「À, cô ấy đang ở chỗ chị Mayami.」" — đó chính là bản dịch của JP 2447.
- 3662 [monologue] JP 「日々姫の声に、またホっとする。」 — VN hiện tại là "Nhưng nếu cứ nghĩ về lý do thì sẽ lại luẩn quẩn mất. / Để không phải bận tâm đến nó, tôi đành tiếp tục câu chuyện." — đó chính là bản dịch của JP 3220.

Cách sửa: dời mỗi giá trị VN nguyên văn về đúng key của nó (2447 ← giá trị đang ở 3220; 3220 ← giá trị đang ở 3662; 3662 ← giá trị đang ở 2447). Không dòng nào cần dịch mới; không còn dòng nào "mồ côi" sau khi sửa. Chuỗi "thở phào một lần nữa" chỉ xuất hiện duy nhất ở 2447 trong toàn bộ TOML, và không có bản dịch nào khác của JP 3220 tồn tại trong dự án — chứng tỏ đây là một vòng xoay khép kín 3 dòng, không phải lỗi rải rác.

## §2 — Thuật ngữ (27 dòng)

Hệ thống: toàn file dùng tên cũ, chưa theo thuật ngữ đã chốt 19–20/11.

- 御一夜 → "Ohitoyo" (không phải "Ohimitera"): 14 dòng, 16 lần xuất hiện — 2249, 2317, 2327, 2356, 2463, 2529, 2542 (2 lần), 2626 (2 lần), 2659, 2862, 3142, 3307, 3706, 3755.
- 帝鉄 → "Teitetsu" (không phải "Đường sắt Hoàng gia"): 5 dòng — 2354, 2505, 2694, 2748, 3683.
- 駿袋鉄道 → "Suntai" (không phải "Suntay"): 6 dòng, 7 lần — 2356, 2680, 2743, 2886, 2911, 3724 (3724 sửa cả 2: tuyến 駿袋線 "tuyến Surukawa" → "tuyến Suntai" và "Đường sắt Suntay" → "Đường sắt Suntai").
- 湯医 → "Yunoi" (không phải "Yui"): 2 dòng — 2659, 2862.
- 機関士: 3 dòng — 1897, 2711 dùng dạng rút gọn đối thoại "lái tàu" (thay "người lái tàu"); 3604 là độc thoại nên dùng dạng đầy đủ "thợ lái đầu máy". 機関助士 "phụ lái tàu" giữ nguyên (chưa có dạng chốt, TW 司爐).

## §3 — Đại từ (5 dòng)

- 2384 Paulette 「うふふ、ありがとう、双鉄くん」 — "cảm ơn cậu, Soutetsu" → "cảm ơn anh, Soutetsu" (khóa B4: Paulette→Soutetsu là "anh Soutetsu").
- 2637 Paulette 「どうでしょうか？　双鉄くん」 — "Cậu thấy sao? Soutetsu." → "Anh thấy sao? Soutetsu." (khóa B4).
- 2458 Soutetsu qua điện thoại 「もしもし、僕だ、双鉄だ」 — "Alo, tôi đây" → "Alo, anh đây": cùng một cuộc gọi với 2455 (đã dùng "anh"), người gọi báo tin tìm thấy toa xe là Paulette — người đang đi tìm toa xe (2581, 2883, 2885).
- 2482 Paulette 「うん、あのね？」 — "Ừm, em nghe này?" → "Ừm, anh nghe này?": Paulette đang báo cáo với Soutetsu (cảnh 2479 Soutetsu → 2482 Paulette → 2484 Hibiki "Vâng, thưa anh"), xưng hô ngược "em" với Soutetsu là sai. Parent sửa thêm "của chị"→"của em" (xem §9): Paulette tự xưng "em" với Soutetsu (9× trong file) nên câu cũ mâu thuẫn nội bộ ("anh nghe này?" + "của chị").
- 2675 Paulette (PARENT THÊM 20/11 ~11:50 — agent bỏ sót): JP 「そうなの。なかなか電話のタイミングがあわなくて。一度、レールショップでご相談できれば、って」 — "Chị mãi không tìm được..." → "Em mãi không tìm được..." (2× "Chị"→"Em"): Paulette đáp trực tiếp câu hỏi của Soutetsu (2671 Soutetsu hỏi về trà đạo → 2673 Paulette "Vâng" → 2675 tiếp lời); tự xưng "em" với Soutetsu, cùng lỗi với 2482.

## §4 — Dịch sai nghĩa / bịa thêm (2 dòng)

- 2487 Paulette: 車輌輸送 = vận chuyển phương tiện, không phải sản xuất — "họ vẫn đang sản xuất phương tiện đường sắt" → "họ vẫn đang vận chuyển phương tiện đường sắt" (TW 車輛運送 xác nhận).
- 2543 Fukami 「ええとね？　凪ちゃん」 ("Ừm, này, bé Nagi") — VN cũ "Ừm, em hiểu chưa? Bé Nagi." bịa thêm câu hỏi "em hiểu chưa?" không có trong JP/TW; đồng thời "em" xưng hô ngược với Nagi (Fukami→Nagi là "cậu").

## §5 — SFX / gasp (4 dòng)

- 2389 Reina 「ふぁぁ」 — "Oaaa" mất âm f, vi phạm quy tắc fa/fu đã chốt → "Phàaa".
- Gasp っ (áp nguyên sweep, đã kiểm chứng với JP): 2322 (～～っ → á~~Ư), 2427 (dòng 2 「っ！！」 → 「Ư!!」, dòng 1 ひゃうんっ giữ "Á á!!?"), 2894 (――っ！？ → ——Ư!?).
- Quét bổ sung toàn bộ 192 dòng JP có っ: không còn gasp nào sót. Các っ còn lại đều đã diễn đúng hoặc là っ nhấn mạnh cuối câu / phương ngữ (1930/2700 ばいっ, 2251 にぃにっ, 2518 よしっ, 2578 お早くっ, 2584 やけんっ, 2612 わたっ, 2619 ええっ, 2884 あっ), tiếng thốt (2400 ええっ → "Hả!?"), hoặc đã diễn bằng cách khác (2328 にゅ～っ → "phụt~", sweep đã ghi already-rendered; 2402 んんっ → "Ưm"; 3841 さっ → "Xoẹt").

## §6 — Kiểm chứng cơ học

- CSV3: bộ duy nhất 504 dòng, 0 key trùng, 0 VN trống, 0 VN == TW. CSV↔TOML: 504 key khớp; 176 khớp tuyệt đối + 325 gộp \n thành khoảng trắng + 3 dòng TOML làm phẳng \n đầu dòng (2442, 2486, 2858) — 0 khác biệt giá trị thực. Comment # JP trong [script] 504/504 khớp CSV3.
- TOML md5 a066fd1ca4854418d892c78d87384a78, BOM + CRLF, [selections] rỗng, không bản sao trùng (11 nhóm file trùng nội dung toàn dự án, file này không thuộc nhóm nào).
- Cặp VN trùng duy nhất trong file: 2417/2438 cùng "「À」" — JP cả hai đều là 「ああ」, trùng hợp lệ, không phải contamination.
- Thẻ %l: JP = VN ở mọi dòng trừ 3 dòng chuyển ruby [furigana] của JP thành thẻ %l (2354, 2679, 2828) — chữ hiển thị dịch đúng, chỉ khác cơ chế hiển thị, không tính sai. Không marker ruby nào còn sót trong VN. Không dòng nào JP có thẻ %l mà VN thiếu.
- Sweep: 4 mục cho file này — 3 áp nguyên đã kiểm chứng (2322, 2427, 2894), 1 already-rendered giữ nguyên (2328). 3 mục còn lại trong file sweep thuộc file khác (日々姫03_湯富院), không liên quan.
- Lượt soát 2: 40/40 tái kiểm chứng, 0 bỏ, 1 sửa (2543 thiếu dấu 「」 trong bản nháp, đã sửa). Parent kiểm chứng 20/11 ~11:50: 1 fix sửa lại (2482 "của chị"→"của em" — Paulette tự xưng "em" với Soutetsu, xem §7), 1 fix thêm (2675 Paulette "Chị"→"Em" với Soutetsu — cùng lỗi, agent bỏ sót; đã kiểm chứng JP/TW/CSV3 + dòng kề 2671→2673→2675). JSON 41 khóa chuỗi; khối TOML parse OK, 41 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 41/41; diff-sanity: mọi fix chỉ khác old VN ở đúng chỗ sửa mục tiêu (trừ 3 dòng xoay vòng là dời nguyên văn).

## §7 — Phán đoán ghi chú (giữ nguyên, không sửa)

- 2530, 2603 (uncertain, không tính sai): Soutetsu "tôi ra ngay đây" / "Tôi ra ngay!" — đang đáp lại người gọi ngoài cảnh (có thể là Hachiroku → "tôi" đúng, hoặc Paulette → "anh"); dòng kề không xác định được người nghe, giữ nguyên theo quy tắc "nghi ngờ thì giữ và ghi chú".
- 1936 Soutetsu "Ý em là, anh hãy làm..." giữ (diễn đạt lại というわけか thành câu hỏi xác nhận, nghĩa đúng).
- 2249 駿川市 giữ "Surukawa" (đọc thẳng JP; TW 駿河市 là tên thật khác, JP thắng TW).
- 2834 乗員 "phi hành đoàn" giữ — theo quy ước sẵn có của dự án cho họ 乗務 (câu hỏi về gloss 乗務鞄 vẫn đang chờ Hieu).
- 3764 義兄 "anh trai nuôi" giữ — TW dùng 義兄, đúng tiền lệ file 14 (義 + TW 義 = được dùng "nuôi").
- 3809/3829/3852 độc thoại nội tâm Soutetsu "mình" giữ (ngoại lệ độc thoại tự vấn).
- 2608, 2873, 2266 Paulette tự xưng "mình" giữ — dạng xưng hô mềm, trung tính, không vi phạm rõ ràng quy tắc đại từ; ghi chú để Hieu biết có sự không nhất quán nhỏ với "em" ở các dòng khác.
- 2482 — PARENT ĐÃ KIỂM CHỨNG 20/11 ~11:50: người nghe là Soutetsu (Paulette đáp "うん" của Soutetsu 2479; báo cáo nguồn tin toa xe cho người quyết định; Hibiki 2484/2486 đáp Soutetsu "兄さん"; tiền lệ Paulette→Soutetsu "anh" 2384/2637 trong file). Fix "anh nghe này?" giữ; parent sửa thêm "của chị"→"của em" để câu nhất quán (Paulette tự xưng "em" với Soutetsu).
- 2402 んんっ → "Ưm", 2426 ふぅむ → "Hừm", 2386 ぷはぁ → "Phù" giữ theo tiền lệ.
- 2354/2679/2828 chuyển ruby JP thành thẻ %l: chữ hiển thị đúng, ghi chú mỹ thuật, không tính sai.

## §8 — Chờ Hieu (không tự quyết, không tính sai)

- "ông nội" ở 2368 (Fukami) và 2607 (Fukami): おじいちゃんたち — câu hỏi toàn dự án Seki gọi "ông nội" hay "ông ngoại" vẫn chưa chốt, giữ nguyên cả 2 dòng.
- 日ノ本 "Hinomoto" ở 2561 vs "Hinamoto" đã giữ ở Hibiki08 — cần chốt một cách viết chung (đã ghi chú từ file ハチロク08).
- Paulette tự xưng "mình" (2266, 2608, 2873) vs "em" ở các dòng khác — có thống nhất thành "em" không (đợt thống nhất)?
- 2530, 2603: Soutetsu "tôi" khi đáp lại người gọi ngoài cảnh — xác nhận người nghe là ai trong game.

## §9 — Danh sách fix (41 dòng)

### 1897 [双鉄] — terminology
- JP: 「\x%l8620;#00ffc040;8620%l;#;の再整備は完了した。\n\x%lレイルロオド;#00ffc040;レイルロオド%l;#;、\x%l機関士;#00ffc040;機関士%l;#;、\x%l機関助士;#00ffc040;機関助士%l;#;は揃った」
- TW: 「\x%l8620;#00ffc040;８６２０%l;#;的再檢修結束了。\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;、\x%l機関士;#00ffc040;司機%l;#;、\x%l機関助士;#00ffc040;司爐%l;#;也都到齊了」
- Cũ: 「Việc đại tu \x%l8620;#00ffc040;8620%l;#; đã hoàn tất.\n\x%lレイルロオド;#00ffc040;Railord%l;#;, \x%l機関士;#00ffc040;người lái tàu%l;#;, \x%l機関助士;#00ffc040;phụ lái tàu%l;#; đều đã tập hợp đủ.」
- Mới: 「Việc đại tu \x%l8620;#00ffc040;8620%l;#; đã hoàn tất.\n\x%lレイルロオド;#00ffc040;Railord%l;#;, \x%l機関士;#00ffc040;lái tàu%l;#;, \x%l機関助士;#00ffc040;phụ lái tàu%l;#; đều đã tập hợp đủ.」

### 2249 [ポーレット] — terminology
- JP: 「ううん、人じゃなくって、場所の縁です。\n御一夜市と駿川市とには、旧縁があるらしくって」
- TW: 「不不，不是人的緣，而是地方的緣。御一夜市和駿河市聽說有著舊緣」
- Cũ: 「Không, không phải con người, mà là mối duyên về địa lý.\nThành phố Ohimitera và thành phố Surukawa dường như có một mối duyên từ xưa.」
- Mới: 「Không, không phải con người, mà là mối duyên về địa lý.\nThành phố Ohitoyo và thành phố Surukawa dường như có một mối duyên từ xưa.」

### 2317 [ポーレット] — terminology
- JP: 「御一夜城の異名……別名って知っていますか？」
- TW: 「你們知道御一夜城的異名……也就是別名嗎？」
- Cũ: 「Biệt danh của thành cổ Ohimitera... mọi người có biết tên gọi khác của nó không?」
- Mới: 「Biệt danh của thành cổ Ohitoyo... mọi người có biết tên gọi khác của nó không?」

### 2322 [日々姫] — gasp
- JP: 「用事がなくちゃ来ちゃダメみたいな言い方～～っ」
- TW: 「你這話說得就像沒有什麼事就不能來找你似的～～」
- Cũ: 「Anh nói cứ như thể không có việc gì thì không được đến tìm anh vậy á~~」
- Mới: 「Anh nói cứ như thể không có việc gì thì không được đến tìm anh vậy á~~Ư」

### 2327 [日々姫] — terminology
- JP: 「そのお仲間さんのお仲間さんと、\n御一夜の誰かとに縁が？」
- TW: 「你那個朋友的朋友和御一夜的誰有緣嗎？」
- Cũ: 「Bạn của bạn chị,\ncó mối liên hệ nào với ai đó ở Ohimitera sao?」
- Mới: 「Bạn của bạn chị,\ncó mối liên hệ nào với ai đó ở Ohitoyo sao?」

### 2354 [ハチロク] — terminology
- JP: 「あの時期の\x%l帝鉄;#00ffc040;帝鉄%l;#;の[てつどうさい,2]鉄道債でも、飛ぶように売れました。\n大赤字を垂れ流していたにもかかわらず、です」
- TW: 「即使是那個時期的\x%l帝鉄;#00ffc040;帝國鐵路%l;#;債券，也依舊賣得飛快。明明他們可是一直背負著巨大的赤字」
- Cũ: 「Ngay cả \x%l鉄道債;#00ffc040;trái phiếu đường sắt%l;#; của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; thời kỳ đó cũng bán đắt như tôm tươi.\nMặc dù họ đang gánh chịu những khoản lỗ khổng lồ.」
- Mới: 「Ngay cả \x%l鉄道債;#00ffc040;trái phiếu đường sắt%l;#; của \x%l帝鉄;#00ffc040;Teitetsu%l;#; thời kỳ đó cũng bán đắt như tôm tươi.\nMặc dù họ đang gánh chịu những khoản lỗ khổng lồ.」

### 2356 [双鉄] — terminology
- JP: 「なるほど。つまり、相樂氏の縁で、\n御一夜と駿袋鉄道とは繋がっているのか」
- TW: 「原來如此。也就是說御一夜和駿遠鐵路是由相良氏的緣而聯繫在一起的嗎？」
- Cũ: 「Ra vậy. Tức là, nhờ mối duyên của gia tộc Sagara,\nmà Ohimitera và Đường sắt Suntay được kết nối với nhau sao.」
- Mới: 「Ra vậy. Tức là, nhờ mối duyên của gia tộc Sagara,\nmà Ohitoyo và Đường sắt Suntai được kết nối với nhau sao.」

### 2384 [ポーレット] — pronoun
- JP: 「うふふ、ありがとう、双鉄くん」
- TW: 「呵呵呵，謝謝你，雙鐵君」
- Cũ: 「Fufufu, cảm ơn cậu, Soutetsu.」
- Mới: 「Fufufu, cảm ơn anh, Soutetsu.」

### 2389 [れいな] — sfx
- JP: 「ふぁぁ」
- TW: 「哇啊……」
- Cũ: 「Oaaa」
- Mới: 「Phàaa」

### 2427 [日々姫] — gasp
- JP: 「ひゃうんっ！！？」\n「っ！！」
- TW: 「唔哇！！？」\n「！！」
- Cũ: 「Á á!!?」\n「!!」
- Mới: 「Á á!!?」\n「Ư!!」

### 2447 [双鉄] — rotation
- JP: 「ああ、真闇姉のところだ」
- TW: 「啊，她在真闇姐那裡」
- Cũ: Giọng nói của Hibiki lại khiến tôi thở phào một lần nữa.
- Mới: 「À, cô ấy đang ở chỗ chị Mayami.」

### 2458 [双鉄] — pronoun
- JP: 「もしもし、僕だ、双鉄だ。\n\x%l客車;#00ffc040;客車%l;#;か？　――やはりか！ 見つかったのか！！」
- TW: 「喂，是我，雙鐵。\x%l客車;#00ffc040;客運車廂%l;#;嗎？——果然嗎！找到了啊！！」
- Cũ: 「Alo, tôi đây, Soutetsu đây.\n\x%l客車;#00ffc040;Toa hành khách%l;#; sao? ——Quả nhiên là vậy! Tìm thấy rồi sao!!」
- Mới: 「Alo, anh đây, Soutetsu đây.\n\x%l客車;#00ffc040;Toa hành khách%l;#; sao? ——Quả nhiên là vậy! Tìm thấy rồi sao!!」

### 2463 [れいな] — terminology
- JP: 「はわわ！　れいな、御一夜鉄道の子だから、\nきょうとにいかないのです。どえす、言わないのです」
- TW: 「嗚哇哇！玲奈是御一夜鐵路的人，才不想去京都呢。玲奈不說“是也”了」
- Cũ: 「Oa oa! Reina là con của Đường sắt Ohimitera,\nnên sẽ không đi Kyoto đâu. Sẽ không nói doesu nữa đâu」
- Mới: 「Oa oa! Reina là con của Đường sắt Ohitoyo,\nnên sẽ không đi Kyoto đâu. Sẽ không nói doesu nữa đâu」

### 2482 [ポーレット] — pronoun
- JP: 「うん、あのね？　この話、わたしの\x%lまいてつ;#00ffc040;まいてつ%l;#;仲間さんの\nさらに\x%lまいてつ;#00ffc040;まいてつ%l;#;仲間さんからの紹介なんだけど」
- TW: 「嗯，你聽我說呀。這個消息是我\x%lまいてつ;#00ffc040;掌車人%l;#;朋友的\x%lまいてつ;#00ffc040;掌車人%l;#;朋友給我介紹的」
- Cũ: 「Ừm, em nghe này? Chuyện này, là do bạn \x%lまいてつ;#00ffc040;chủ tàu%l;#; của chị,\nđược bạn \x%lまいてつ;#00ffc040;chủ tàu%l;#; của người đó giới thiệu cho đấy.」
- Mới: 「Ừm, anh nghe này? Chuyện này, là do bạn \x%lまいてつ;#00ffc040;chủ tàu%l;#; của em,\nđược bạn \x%lまいてつ;#00ffc040;chủ tàu%l;#; của người đó giới thiệu cho đấy.」

### 2487 [ポーレット] — mistranslation
- JP: 「はい、鉄道産業が生き延びてるとこも多くて。\nブラディルなんかは、車輌輸送もやってます」
- TW: 「嗯，很多地方的鐵路產業還繼續存活著。巴西那邊還在做車輛運送呢」
- Cũ: 「Vâng, có rất nhiều nơi ngành công nghiệp đường sắt vẫn còn tồn tại.\nVí dụ như ở Brazil, họ vẫn đang sản xuất phương tiện đường sắt đấy.」
- Mới: 「Vâng, có rất nhiều nơi ngành công nghiệp đường sắt vẫn còn tồn tại.\nVí dụ như ở Brazil, họ vẫn đang vận chuyển phương tiện đường sắt đấy.」

### 2505 [ハチロク] — terminology
- JP: 「\x%l帝鉄;#00ffc040;帝鉄%l;#;末期には、機関車を失った\x%l客車;#00ffc040;客車%l;#;など、\nごろごろ転がっておりましたのに――」
- TW: 「在\x%l帝鉄;#00ffc040;帝國鐵路%l;#;時代的末期可是有一大堆沒了機車的\x%l客車;#00ffc040;客運車廂%l;#;的呢——」
- Cũ: 「Vào cuối thời kỳ \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;, những \x%l客車;#00ffc040;toa hành khách%l;#; mất đi đầu máy,\nđã nằm lăn lóc khắp nơi vậy mà——」
- Mới: 「Vào cuối thời kỳ \x%l帝鉄;#00ffc040;Teitetsu%l;#;, những \x%l客車;#00ffc040;toa hành khách%l;#; mất đi đầu máy,\nđã nằm lăn lóc khắp nơi vậy mà——」

### 2529 [ポーレット] — terminology
- JP: 「そう。眉月は、御一夜市の市章のモチーフで、\nその元をたどると、[さがら,1]相樂氏の旗印なんです」
- TW: 「對。御一夜市的市章就是以眉月為原型創作的，要究其根源的話，可以追溯到相良氏的旗幟圖案」
- Cũ: 「Đúng vậy. Mayuzuki là họa tiết trên huy hiệu của thành phố Ohimitera,\nnếu truy tìm nguồn gốc thì đó là cờ hiệu của gia tộc Sagara.」
- Mới: 「Đúng vậy. Mayuzuki là họa tiết trên huy hiệu của thành phố Ohitoyo,\nnếu truy tìm nguồn gốc thì đó là cờ hiệu của gia tộc Sagara.」

### 2542 [日々姫] — terminology
- JP: 「旧藩主ですよ、兄さん。御一夜はもともと御一夜藩。\n鎌倉時代からずっと[さがら,1]相樂氏の領地なんです」
- TW: 「就是舊藩主啦，哥哥。御一夜原本叫御一夜藩。從鎌倉時代開始就一直是相良氏的領地了」
- Cũ: 「Là cựu lãnh chúa đấy, anh trai. Ohimitera vốn dĩ là phiên Ohimitera.\nTừ thời Kamakura đã luôn là lãnh địa của gia tộc Sagara rồi.」
- Mới: 「Là cựu lãnh chúa đấy, anh trai. Ohitoyo vốn dĩ là phiên Ohitoyo.\nTừ thời Kamakura đã luôn là lãnh địa của gia tộc Sagara rồi.」

### 2543 [ふかみ] — mistranslation
- JP: 「ええとね？　凪ちゃん」
- TW: 「就是說，小凪」
- Cũ: 「Ừm, em hiểu chưa? Bé Nagi.」
- Mới: 「Ừm, này, bé Nagi.」

### 2626 [双鉄] — terminology
- JP: 「お忙しいところすみません。こちら、\n御一夜市の御一夜鉄道株式会社のものですが――」
- TW: 「抱歉在百忙中打擾了。這裡是御一夜市的御一夜鐵路股份公司——」
- Cũ: 「Xin lỗi đã làm phiền lúc anh đang bận rộn. Đây là\nCông ty Đường sắt Ohimitera của thành phố Ohimitera——」
- Mới: 「Xin lỗi đã làm phiền lúc anh đang bận rộn. Đây là\nCông ty Đường sắt Ohitoyo của thành phố Ohitoyo——」

### 2637 [ポーレット] — pronoun
- JP: 「って、いう希望が入ってるんですけど――\nどうでしょうか？　双鉄くん」
- TW: 「於是有人提這個小願望了——你覺得呢？雙鐵君」
- Cũ: 「Có người đưa ra nguyện vọng như vậy đấy——\nCậu thấy sao? Soutetsu.」
- Mới: 「Có người đưa ra nguyện vọng như vậy đấy——\nAnh thấy sao? Soutetsu.」

### 2659 [ポーレット] — terminology
- JP: 「湯医から先の\x%l客車;#00ffc040;客車%l;#;の話。\n御一夜まで、ひとまずは\x%l8620;#00ffc040;8620%l;#;に引いてもらって戻るから」
- TW: 「是到了湯醫線後怎麼拉\x%l客車;#00ffc040;客運車廂%l;#;的事。因為到時候是打算用\x%l8620;#00ffc040;８６２０%l;#;把車廂拉回御一夜」
- Cũ: 「Chuyện về \x%l客車;#00ffc040;toa hành khách%l;#; sau khi đến ga Yui.\nTrước mắt, chúng ta sẽ nhờ \x%l8620;#00ffc040;8620%l;#; kéo nó về Ohimitera.」
- Mới: 「Chuyện về \x%l客車;#00ffc040;toa hành khách%l;#; sau khi đến ga Yunoi.\nTrước mắt, chúng ta sẽ nhờ \x%l8620;#00ffc040;8620%l;#; kéo nó về Ohitoyo.」

### 2675 [ポーレット] — pronoun (PARENT THÊM 20/11 ~11:50 — agent bỏ sót)
- JP: 「そうなの。なかなか電話のタイミングがあわなくて。\n一度、レールショップでご相談できれば、って」
- TW: 「是的。我總是找不到機會打電話。希望能請他們來鐵路商店商談一次」
- Cũ: 「Đúng vậy. Chị mãi không tìm được lúc nào gọi điện thoại cho tiện.\nNên chị nghĩ, hay là bàn bạc một lần ở cửa hàng đường sắt luôn.」
- Mới: 「Đúng vậy. Em mãi không tìm được lúc nào gọi điện thoại cho tiện.\nNên em nghĩ, hay là bàn bạc một lần ở cửa hàng đường sắt luôn.」

### 2680 [ポーレット] — terminology
- JP: 「そうなんです。相樂町の町長さんが駿袋鉄道の\n大株主さんだそうで、その辺の歴史にお詳しくて」
- TW: 「是的。相良町的町長據說是駿遠鐵路的大股東，對這方面的歷史很熟悉呢」
- Cũ: 「Đúng vậy. Nghe nói Thị trưởng thị trấn Sagara là\ncổ đông lớn của Đường sắt Suntay, và ông ấy rất am hiểu lịch sử khu vực đó.」
- Mới: 「Đúng vậy. Nghe nói Thị trưởng thị trấn Sagara là\ncổ đông lớn của Đường sắt Suntai, và ông ấy rất am hiểu lịch sử khu vực đó.」

### 2694 [ハチロク] — terminology
- JP: 「乱発していたのです。末期の\x%l帝鉄;#00ffc040;帝鉄%l;#;が、鉄道債を。\nなんとしても、電化を推進しようとして」
- TW: 「末期的\x%l帝鉄;#00ffc040;帝國鐵路%l;#;，可是在完全濫發鐵路債券。聽說他們那時激進地想推進鐵路電氣化來著」
- Cũ: 「Họ đã phát hành bừa bãi đấy ạ. Vào thời kỳ cuối của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;, họ đã phát hành trái phiếu đường sắt một cách vô tội vạ.\nĐể bằng mọi giá thúc đẩy quá trình điện khí hóa.」
- Mới: 「Họ đã phát hành bừa bãi đấy ạ. Vào thời kỳ cuối của \x%l帝鉄;#00ffc040;Teitetsu%l;#;, họ đã phát hành trái phiếu đường sắt một cách vô tội vạ.\nĐể bằng mọi giá thúc đẩy quá trình điện khí hóa.」

### 2711 [ハチロク] — terminology
- JP: 「と、清美機関士はわたくしに説明してくださいました。\n説明、というより……グチ、だったのかもしれませんが」
- TW: 「清美司機就是這樣跟我說明的。與其說是說明……不如說是牢騷更為妥當吧」
- Cũ: 「Người lái tàu Kiyomi đã giải thích cho tôi như vậy ạ.\nThay vì nói là giải thích... có lẽ giống như lời than vãn hơn.」
- Mới: 「Lái tàu Kiyomi đã giải thích cho tôi như vậy ạ.\nThay vì nói là giải thích... có lẽ giống như lời than vãn hơn.」

### 2743 [ポーレット] — terminology
- JP: 「相樂町、[すんたい,1]駿袋鉄道の沿線なんです」
- TW: 「相良町就在駿遠鐵路的沿線」
- Cũ: 「Thị trấn Sagara, nằm dọc theo tuyến Đường sắt Suntay đấy.」
- Mới: 「Thị trấn Sagara, nằm dọc theo tuyến Đường sắt Suntai đấy.」

### 2748 [双鉄] — terminology
- JP: 「見越していたのか。\x%l帝鉄;#00ffc040;帝鉄%l;#;が破綻してしまっても、\n国が、その債権を保障してくれると」
- TW: 「看來他們是看準了。就算\x%l帝鉄;#00ffc040;帝國鐵路%l;#;破產，還有國家在保障這部分債權」
- Cũ: 「Là họ đã lường trước được sao. Cho dù \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; có phá sản,\nthì nhà nước vẫn sẽ bảo lãnh cho những khoản nợ đó.」
- Mới: 「Là họ đã lường trước được sao. Cho dù \x%l帝鉄;#00ffc040;Teitetsu%l;#; có phá sản,\nthì nhà nước vẫn sẽ bảo lãnh cho những khoản nợ đó.」

### 2862 [凪] — terminology
- JP: 「なら決まりとね！　湯医から御一夜の最初の\x%l列車;#00ffc040;列車%l;#;、\n予約一番はウチとふかみちゃんとばい！」
- TW: 「那就這麼決定啦！咱和小深第一個預約從湯醫開到御一夜的第一輛\x%l列車;#00ffc040;列車%l;#;！」
- Cũ: 「Vậy là quyết định rồi nhé! Chuyến \x%l列車;#00ffc040;tàu%l;#; đầu tiên từ Yui về Ohimitera,\nngười đặt chỗ số 1 là em và Fukami nha!」
- Mới: 「Vậy là quyết định rồi nhé! Chuyến \x%l列車;#00ffc040;tàu%l;#; đầu tiên từ Yunoi về Ohitoyo,\nngười đặt chỗ số 1 là em và Fukami nha!」

### 2886 [ハチロク] — terminology
- JP: 「なら、その子の機関車が廃棄になったのですね？\nそれで浮いた\x%l客車;#00ffc040;客車%l;#;を、[すんたい,1]駿袋鉄道が購入した」
- TW: 「那麼，那孩子的機車也就被同時廢棄了吧？然後空出來的\x%l客車;#00ffc040;客運車廂%l;#;被駿遠鐵路購入了……」
- Cũ: 「Vậy thì, đầu máy của đứa bé đó cũng bị phế thải luôn sao?\nSau đó \x%l客車;#00ffc040;toa hành khách%l;#; dư ra được Đường sắt Suntay mua lại...」
- Mới: 「Vậy thì, đầu máy của đứa bé đó cũng bị phế thải luôn sao?\nSau đó \x%l客車;#00ffc040;toa hành khách%l;#; dư ra được Đường sắt Suntai mua lại...」

### 2894 [日々姫] — gasp
- JP: 「電話ですね、こんな時間に――っ！？」
- TW: 「都這麼晚了還有電話呀——啊！？」
- Cũ: 「Là điện thoại nhỉ, giờ này mà còn——!?」
- Mới: 「Là điện thoại nhỉ, giờ này mà còn——Ư!?」

### 2911 [双鉄] — terminology
- JP: 「靜岡[すんたい,1]駿袋鉄道？」
- TW: 「靜岡駿袋鐵路？」
- Cũ: 「Đường sắt Shizuoka Suntay?」
- Mới: 「Đường sắt Shizuoka Suntai?」

### 3142 [monologue] — terminology
- JP: その能力を活かし、\n御一夜鉄道の\x%l保線;#00ffc040;保線%l;#;ボランティアも務めてくれている。
- TW: 他們經常活用自己的專業能力擔任御一夜鐵路的\x%l保線;#00ffc040;巡線%l;#;志願者。
- Cũ: Tận dụng khả năng đó,\nhọ cũng đang làm tình nguyện viên \x%l保線;#00ffc040;bảo trì đường ray%l;#; cho Đường sắt Ohimitera.
- Mới: Tận dụng khả năng đó,\nhọ cũng đang làm tình nguyện viên \x%l保線;#00ffc040;bảo trì đường ray%l;#; cho Đường sắt Ohitoyo.

### 3220 [monologue] — rotation
- JP: が、理由を思えばどうどうめぐりだ。\n意識せぬよう、とにかく言葉を続けてしまう。
- TW: 可若要去想具體的原因，那就要繞個沒完了。我試著不去在意它，繼續說下去。
- Cũ: 「À, cô ấy đang ở chỗ chị Mayami.」
- Mới: Nhưng nếu cứ nghĩ về lý do thì sẽ lại luẩn quẩn mất.\nĐể không phải bận tâm đến nó, tôi đành tiếp tục câu chuyện.

### 3307 [monologue] — terminology
- JP: \x%l客車;#00ffc040;客車%l;#;を入手し損ねるなら、\x%l8620;#00ffc040;8620%l;#;の復活と、\n御一夜の観光復権とをつなげ損なうのは明白だ。
- TW: 如果不能順利拿到\x%l客車;#00ffc040;客運車廂%l;#;的話，\x%l8620;#00ffc040;８６２０%l;#;的復活和御一夜的觀光復興也就連帶著命懸一線了。
- Cũ: Nếu không thể có được \x%l客車;#00ffc040;toa hành khách%l;#;, thì rõ ràng sự hồi sinh của \x%l8620;#00ffc040;8620%l;#;\nvà sự phục hưng du lịch của Ohimitera sẽ bị đứt đoạn.
- Mới: Nếu không thể có được \x%l客車;#00ffc040;toa hành khách%l;#;, thì rõ ràng sự hồi sinh của \x%l8620;#00ffc040;8620%l;#;\nvà sự phục hưng du lịch của Ohitoyo sẽ bị đứt đoạn.

### 3604 [monologue] — terminology
- JP: \x%l機関士;#00ffc040;機関士%l;#;として認められた今、\n僕はハチロクのオーナーであり、マスターだ。
- TW: 現在我既然被正式承認為\x%l機関士;#00ffc040;司機%l;#;，那我就是八六的主人兼司機了。
- Cũ: Bây giờ, khi đã được công nhận là một \x%l機関士;#00ffc040;người lái tàu%l;#;,\ntôi là chủ sở hữu và cũng là Master của Hachiroku.
- Mới: Bây giờ, khi đã được công nhận là một \x%l機関士;#00ffc040;thợ lái đầu máy%l;#;,\ntôi là chủ sở hữu và cũng là Master của Hachiroku.

### 3662 [monologue] — rotation
- JP: 日々姫の声に、またホっとする。
- TW: 聽到日日姬的聲音我又感到一陣安心。
- Cũ: Nhưng nếu cứ nghĩ về lý do thì sẽ lại luẩn quẩn mất.\nĐể không phải bận tâm đến nó, tôi đành tiếp tục câu chuyện.
- Mới: Giọng nói của Hibiki lại khiến tôi thở phào một lần nữa.

### 3683 [monologue] — terminology
- JP: \x%l帝鉄;#00ffc040;帝鉄%l;#;が破綻をしてしまえば、\n約束された利率も全ては反故になる。
- TW: 要是\x%l帝鉄;#00ffc040;帝國鐵路%l;#;破產的話，約定好的利率也會全部打水漂。
- Cũ: Nếu \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; phá sản,\nthì mọi mức lãi suất đã cam kết đều sẽ trở thành giấy lộn.
- Mới: Nếu \x%l帝鉄;#00ffc040;Teitetsu%l;#; phá sản,\nthì mọi mức lãi suất đã cam kết đều sẽ trở thành giấy lộn.

### 3706 [monologue] — terminology
- JP: 御一夜と相樂町との姉妹都市提携の話までもが出てくる、\n極めて良好な話し合い。
- TW: 討論過程十分融洽，還提到了要讓御一夜和相良町互相結成姐妹城市的事。
- Cũ: Cuộc trò chuyện diễn ra vô cùng tốt đẹp,\nthậm chí còn đề cập đến việc kết nghĩa thành phố kết nghĩa giữa Ohimitera và thị trấn Sagara.
- Mới: Cuộc trò chuyện diễn ra vô cùng tốt đẹp,\nthậm chí còn đề cập đến việc kết nghĩa thành phố kết nghĩa giữa Ohitoyo và thị trấn Sagara.

### 3724 [monologue] — terminology
- JP: 譲渡される\x%l客車;#00ffc040;客車%l;#;は当然、引いてもらえれば走行できる。\nそれでそのまま、駿袋鉄道駿袋線の相樂駅へと。
- TW: 轉讓來的\x%l客車;#00ffc040;客運車廂%l;#;當然只要牽引著就能在線路上跑。然後就這樣一路把它牽引到駿遠鐵路駿遠線的相良站。
- Cũ: \x%l客車;#00ffc040;Toa hành khách%l;#; được nhượng lại đương nhiên có thể chạy được nếu có đầu máy kéo.\nCứ thế, nó sẽ được kéo đến ga Sagara của tuyến Surukawa thuộc Đường sắt Suntay.
- Mới: \x%l客車;#00ffc040;Toa hành khách%l;#; được nhượng lại đương nhiên có thể chạy được nếu có đầu máy kéo.\nCứ thế, nó sẽ được kéo đến ga Sagara của tuyến Suntai thuộc Đường sắt Suntai.

### 3755 [monologue] — terminology
- JP: かかるコストは、靜岡-御一夜間の何十倍――\nいや、何百倍にも達してしまうかもしれん。
- TW: 這產生的費用說不定是靜岡-御一夜間的數十倍——不，數百倍也有可能。
- Cũ: Chi phí phải bỏ ra, gấp mấy chục lần đoạn Shizuoka - Ohimitera——\nkhông, có khi lên đến mấy trăm lần cũng nên.
- Mới: Chi phí phải bỏ ra, gấp mấy chục lần đoạn Shizuoka - Ohitoyo——\nkhông, có khi lên đến mấy trăm lần cũng nên.

## §10 — Khối TOML (đã parse-kiểm chứng: 41 khóa, 0 sai lệch)

```toml
[script]
1897 = "「Việc đại tu \\x%l8620;#00ffc040;8620%l;#; đã hoàn tất.\\n\\x%lレイルロオド;#00ffc040;Railord%l;#;, \\x%l機関士;#00ffc040;lái tàu%l;#;, \\x%l機関助士;#00ffc040;phụ lái tàu%l;#; đều đã tập hợp đủ.」"
2249 = "「Không, không phải con người, mà là mối duyên về địa lý.\\nThành phố Ohitoyo và thành phố Surukawa dường như có một mối duyên từ xưa.」"
2317 = "「Biệt danh của thành cổ Ohitoyo... mọi người có biết tên gọi khác của nó không?」"
2322 = "「Anh nói cứ như thể không có việc gì thì không được đến tìm anh vậy á~~Ư」"
2327 = "「Bạn của bạn chị,\\ncó mối liên hệ nào với ai đó ở Ohitoyo sao?」"
2354 = "「Ngay cả \\x%l鉄道債;#00ffc040;trái phiếu đường sắt%l;#; của \\x%l帝鉄;#00ffc040;Teitetsu%l;#; thời kỳ đó cũng bán đắt như tôm tươi.\\nMặc dù họ đang gánh chịu những khoản lỗ khổng lồ.」"
2356 = "「Ra vậy. Tức là, nhờ mối duyên của gia tộc Sagara,\\nmà Ohitoyo và Đường sắt Suntai được kết nối với nhau sao.」"
2384 = "「Fufufu, cảm ơn anh, Soutetsu.」"
2389 = "「Phàaa」"
2427 = "「Á á!!?」\\n「Ư!!」"
2447 = "「À, cô ấy đang ở chỗ chị Mayami.」"
2458 = "「Alo, anh đây, Soutetsu đây.\\n\\x%l客車;#00ffc040;Toa hành khách%l;#; sao? ——Quả nhiên là vậy! Tìm thấy rồi sao!!」"
2463 = "「Oa oa! Reina là con của Đường sắt Ohitoyo,\\nnên sẽ không đi Kyoto đâu. Sẽ không nói doesu nữa đâu」"
2482 = "「Ừm, anh nghe này? Chuyện này, là do bạn \\x%lまいてつ;#00ffc040;chủ tàu%l;#; của em,\\nđược bạn \\x%lまいてつ;#00ffc040;chủ tàu%l;#; của người đó giới thiệu cho đấy.」"
2487 = "「Vâng, có rất nhiều nơi ngành công nghiệp đường sắt vẫn còn tồn tại.\\nVí dụ như ở Brazil, họ vẫn đang vận chuyển phương tiện đường sắt đấy.」"
2505 = "「Vào cuối thời kỳ \\x%l帝鉄;#00ffc040;Teitetsu%l;#;, những \\x%l客車;#00ffc040;toa hành khách%l;#; mất đi đầu máy,\\nđã nằm lăn lóc khắp nơi vậy mà——」"
2529 = "「Đúng vậy. Mayuzuki là họa tiết trên huy hiệu của thành phố Ohitoyo,\\nnếu truy tìm nguồn gốc thì đó là cờ hiệu của gia tộc Sagara.」"
2542 = "「Là cựu lãnh chúa đấy, anh trai. Ohitoyo vốn dĩ là phiên Ohitoyo.\\nTừ thời Kamakura đã luôn là lãnh địa của gia tộc Sagara rồi.」"
2543 = "「Ừm, này, bé Nagi.」"
2626 = "「Xin lỗi đã làm phiền lúc anh đang bận rộn. Đây là\\nCông ty Đường sắt Ohitoyo của thành phố Ohitoyo——」"
2637 = "「Có người đưa ra nguyện vọng như vậy đấy——\\nAnh thấy sao? Soutetsu.」"
2659 = "「Chuyện về \\x%l客車;#00ffc040;toa hành khách%l;#; sau khi đến ga Yunoi.\\nTrước mắt, chúng ta sẽ nhờ \\x%l8620;#00ffc040;8620%l;#; kéo nó về Ohitoyo.」"
2675 = "「Đúng vậy. Em mãi không tìm được lúc nào gọi điện thoại cho tiện.\\nNên em nghĩ, hay là bàn bạc một lần ở cửa hàng đường sắt luôn.」"
2680 = "「Đúng vậy. Nghe nói Thị trưởng thị trấn Sagara là\\ncổ đông lớn của Đường sắt Suntai, và ông ấy rất am hiểu lịch sử khu vực đó.」"
2694 = "「Họ đã phát hành bừa bãi đấy ạ. Vào thời kỳ cuối của \\x%l帝鉄;#00ffc040;Teitetsu%l;#;, họ đã phát hành trái phiếu đường sắt một cách vô tội vạ.\\nĐể bằng mọi giá thúc đẩy quá trình điện khí hóa.」"
2711 = "「Lái tàu Kiyomi đã giải thích cho tôi như vậy ạ.\\nThay vì nói là giải thích... có lẽ giống như lời than vãn hơn.」"
2743 = "「Thị trấn Sagara, nằm dọc theo tuyến Đường sắt Suntai đấy.」"
2748 = "「Là họ đã lường trước được sao. Cho dù \\x%l帝鉄;#00ffc040;Teitetsu%l;#; có phá sản,\\nthì nhà nước vẫn sẽ bảo lãnh cho những khoản nợ đó.」"
2862 = "「Vậy là quyết định rồi nhé! Chuyến \\x%l列車;#00ffc040;tàu%l;#; đầu tiên từ Yunoi về Ohitoyo,\\nngười đặt chỗ số 1 là em và Fukami nha!」"
2886 = "「Vậy thì, đầu máy của đứa bé đó cũng bị phế thải luôn sao?\\nSau đó \\x%l客車;#00ffc040;toa hành khách%l;#; dư ra được Đường sắt Suntai mua lại...」"
2894 = "「Là điện thoại nhỉ, giờ này mà còn——Ư!?」"
2911 = "「Đường sắt Shizuoka Suntai?」"
3142 = "Tận dụng khả năng đó,\\nhọ cũng đang làm tình nguyện viên \\x%l保線;#00ffc040;bảo trì đường ray%l;#; cho Đường sắt Ohitoyo."
3220 = "Nhưng nếu cứ nghĩ về lý do thì sẽ lại luẩn quẩn mất.\\nĐể không phải bận tâm đến nó, tôi đành tiếp tục câu chuyện."
3307 = "Nếu không thể có được \\x%l客車;#00ffc040;toa hành khách%l;#;, thì rõ ràng sự hồi sinh của \\x%l8620;#00ffc040;8620%l;#;\\nvà sự phục hưng du lịch của Ohitoyo sẽ bị đứt đoạn."
3604 = "Bây giờ, khi đã được công nhận là một \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#;,\\ntôi là chủ sở hữu và cũng là Master của Hachiroku."
3662 = "Giọng nói của Hibiki lại khiến tôi thở phào một lần nữa."
3683 = "Nếu \\x%l帝鉄;#00ffc040;Teitetsu%l;#; phá sản,\\nthì mọi mức lãi suất đã cam kết đều sẽ trở thành giấy lộn."
3706 = "Cuộc trò chuyện diễn ra vô cùng tốt đẹp,\\nthậm chí còn đề cập đến việc kết nghĩa thành phố kết nghĩa giữa Ohitoyo và thị trấn Sagara."
3724 = "\\x%l客車;#00ffc040;Toa hành khách%l;#; được nhượng lại đương nhiên có thể chạy được nếu có đầu máy kéo.\\nCứ thế, nó sẽ được kéo đến ga Sagara của tuyến Suntai thuộc Đường sắt Suntai."
3755 = "Chi phí phải bỏ ra, gấp mấy chục lần đoạn Shizuoka - Ohitoyo——\\nkhông, có khi lên đến mấy trăm lần cũng nên."
```

Kết bài
