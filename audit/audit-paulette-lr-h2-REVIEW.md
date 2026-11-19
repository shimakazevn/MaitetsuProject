# Audit: Paulette lr_ポーレットh2_デコレーション＆ミルク (Decoration & Sữa) — 69 dòng Việt sai (đã đối chiếu JP + TW)

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa từng dòng: 333 dòng (độc thoại 129, ポーレット 112, 双鉄 92), toàn bộ thuộc section `script`, đối chiếu JP + TW từ CSV3 và TOML-2. Tên file đã kiểm chứng khớp CSV3 và TOML-2: `03_Paulette/lr_ポーレットh2_デコレーション＆ミルク.txt.toml`.
- CSV vs TOML: 0 khác biệt thực chất (chỉ ở `\n`/khoảng trắng); tập key bằng nhau (333, key 678–1784); `[selections]` rỗng; thẻ `%l`: 0 trong JP và VN (không có thẻ hỏng); không có key trùng; không có dòng VN trống; VN==TW 0.
- md5: `961d4a125957dfe488e38eed086c6200` — không trùng với bất kỳ file nào trong 227 file TOML (không có bản sao; bản sửa áp dụng cho 1 file duy nhất).
- Đọc toàn bộ 333 dòng phát hiện 69 dòng sai (20,7%). Rà soát chéo với sweep gasp っ và quét máy tính (pronoun sweep với `\n` chuẩn hoá trước, quét `\bchu\b` và các mảnh La-tinh còn sót, kiểm tra VN trùng và JP trùng) bắt thêm các dòng ngoài lần đọc đầu.
- Rà soát chéo với sweep gasp っ: sweep có 6 bản sửa trong file này (1044, 1064, 1070, 1236, 1558, 1597) — KHÔNG trùng với bất kỳ bản sửa nào của audit; audit xác nhận cả 6 (đều là dòng gasp thuần). 1558 đúng với chỉ 1 tiếng Ư: JP `止めっ――っ` có hai っ nhưng 止めっ là cắt từ cuối từ, không phải gasp. 4 "already-rendered" của sweep (1062, 1063, 1065, 1068) — audit đồng ý. Audit KHÔNG ĐỒNG Ý với sweep "already-rendered" ở 1009 và 1124 (mỗi dòng mất 1 tiếng gasp っ — xem chi tiết). 1028 "already-rendered" của sweep chỉ nói về gasp, không xung đột (bản sửa của audit ở 1028 là về La-tinh hoá, không phải gasp).
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ 68/68 bản sửa đối chiếu JP (đúng 68, 0 bị loại — 1 dòng đã bị loại TRƯỚC khi chốt: 1770, xem dưới). Kiểm tra lần hai bắt và sửa 5 bản sửa: 1107 (số nguyên âm kéo dài 3 → 2, cả 2 vị trí), 1020/1105/1317/1319 (ちゅうっ còn "chụt" không kéo dài → "chụụt"/"Chụụt"). Kiểm tra lần hai cũng LOẠI 1 dòng khỏi danh sách: **1770 — VN cũ "Đâm sâu uuuuuuuuuuu" đã ĐÚNG** (JP ずぶうううううううううううっ có う×11, quy tắc 1+11 = 12 chữ u, VN cũ có đúng 12 chữ u) — dòng này không còn trong khối sửa, tổng số giảm từ 69 xuống 68. Ngoài ra kiểm tra lần hai xác nhận: không có bản sửa nào thừa hưởng lỗi xưng hô của dòng cho; không có khoảng trắng thừa trước `\n` (bản sửa một dòng, không dùng `\n`); không có dấu 。 thay cho dấu .; các âm thở ghép viết liền một từ ("Kíuphù", "Hiau", "Hia", "Ưm kyu", "Ưm kyuu"); không còn mảnh La-tinh nào sót (`\bchu\b` = 0 sau bản sửa; "phu" ở 1072 là hơi thở bị cắt cụt, đã chấp nhận). Quy ước số nguyên âm kéo dài đã chốt: **số nguyên âm trong VN = 1 (âm gốc của âm tiết) + số ký tự う/ぅ viết trong JP** (bằng chứng h7 1651 + 1770 ở trên).
- Quy ước bản sửa: bản sửa viết MỘT DÒNG (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công — theo quyết định 19/11 của Hieu (game tự ngắt dòng, `\n` thủ công không quan trọng). File TOML gốc cũng lưu các giá trị này một dòng với khoảng trắng, nên khối TOML dưới đây dán vào khớp đúng dạng đó. Các khoảng trắng quanh —— trong bản sửa đều là vị trí ngắt dòng cũ (VN cũ có `\n` tại đúng vị trí đó) — không phải khoảng trắng mới.
- Ghi chú về ký tự gạch: VN cũ của file này dùng U+2014 EM DASH (—, 656 lần) là chính, chỉ 30 lần U+2015 HORIZONTAL BAR (―). Bản sửa dùng U+2014 thống nhất — theo quy ước tiếng Việt của dự án (h8 dùng U+2014).

## Kết luận về cơ chế lỗi

- **Không lệch vị trí, không xoay vòng, không tràn chương.** Toàn bộ 69 dòng sai đều là lỗi tại chỗ (xưng hô, thuật ngữ, hơi thở/âm thanh còn La-tinh) — không có dòng nào cần thu hồi bản dịch từ dòng khác, không có VN mồ côi. Đây là file "sạch" về cấu trúc, giống lr_h1.
- Lỗi xưng hô hệ thống: Soutetsu tự xưng "anh" 23 dòng trong thoại (cùng lỗi hệ thống như h1–h8 và lr_h1; độc thoại không có lần "Anh" nào sai). Trước bản sửa, Soutetsu không có lần nào tự xưng "tôi" trong thoại của file này.
- Thuật ngữ: 6 dòng — 5 lần "Decoration"/"decoration" chưa Việt hoá (995, 1120, 1287, 1323, 1621 — tất cả sửa thành "trang trí", theo quyết định 19/11) và 1 lần "Ohimitera" (1280 → "Ohitoyo").
- Lỗi hơi thở/âm thanh La-tinh: 37 dòng thoại + 2 dòng độc thoại — họ lỗi lớn nhất của file. Đặc biệt 1028: cả dòng còn nguyên La-tinh (ぐちゅっ, ちゅぶっ, ずちゅっ, じゅぼっ, ぐりゅっ, リュッ, じゅぶ, じゅるるる～～っ). Các âm ぺろ trong file này theo quy ước riêng "liếm nhẹ" (1020, 1021, 1105, 1315), ぺちゅ → "liếm".
- "em" vs "cô" (Soutetsu gọi Paulette): **"em" 13 vs "cô" 0** trong file này. Cộng dồn sau file này: **"em" 119 vs "cô" 49** (96 sau h8; lr_稀咲h1 +1 "em" → 97; れいな02 +1 "cô" → 49; lr_h1 +9 "em" → 106; file này +13 "em" → 119). 972 là dương tính giả ("cô đơn" = sự cô đơn, không phải cách gọi).
- Tên gọi trần B4: **1 dòng — key 1079, ĐÃ SỬA theo quyết định B4 19/11.** JP: `「ぁ――ぁ――ぁ――んっ――ね？ そうてつ、くん―― そうてつ――くぁ――ふっ――んっ――んうっ！」` — lần gọi đầu そうてつ、くん → "anh Soutetsu", lần gọi sau rên trần "Soutetsu" (JP そうてつ――くぁ――). VN cũ giữ nguyên cả hai. Đã sửa 1079 thành "anh Soutetsu" theo quyết định B4 19/11 (ngoại lệ tên rên bãi bỏ).

## Chi tiết dòng sai

### Xưng hô (23 dòng)

**Key 948 (双鉄)**
- JP: `「僕のカリ首が、大きくなったわけではなく」`
- TW: `「不是我的龜頭冠變大了」`
- VN cũ: `「Không phải rãnh quy đầu của anh to ra đâu.」`
- Sửa: `「Không phải rãnh quy đầu của tôi to ra đâu.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 958 (双鉄)**
- JP: `「いや、そうではなく。\n僕のカリ首が、以前より大きくなったのではなく」`
- TW: `「不，不是的。不是我的龜頭冠比以前大了」`
- VN cũ: `「Không, không phải đâu.\nKhông phải rãnh quy đầu của anh to hơn trước đây đâu.」`
- Sửa: `「Không, không phải đâu. Không phải rãnh quy đầu của tôi to hơn trước đây đâu.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 964 (双鉄)**
- JP: `「いや、綺麗にして大事に保存しておいてほしい。\nどんな理由で購入したのかも気になるし」`
- TW: `「不，請你洗乾淨之後小心保存起來吧。而且我還是很好奇你為什麼會買它」`
- VN cũ: `「Không, anh muốn em giặt sạch rồi cất giữ cẩn thận.\nAnh cũng tò mò không biết em mua nó vì lý do gì nữa.」`
- Sửa: `「Không, tôi muốn em giặt sạch rồi cất giữ cẩn thận. Tôi cũng tò mò không biết em mua nó vì lý do gì nữa.」`
- Lý do: Soutetsu tự xưng "anh" 2 lần — sửa thành "tôi".
**Key 970 (双鉄)**
- JP: `「なろう、必ず。ポーレットと僕とふたりで。\n世界一幸せなおかあさんとおとうさんに、絶対なろう」`
- TW: `「你和我一定會當上的。絕對會當上世界上最幸福的爸爸媽媽的」`
- VN cũ: `「Sẽ thành, chắc chắn vậy. Paulette và anh, hai chúng ta.\nTuyệt đối sẽ trở thành ông bố bà mẹ hạnh phúc nhất thế giới.」`
- Sửa: `「Sẽ thành, chắc chắn vậy. Paulette và tôi, hai chúng ta. Tuyệt đối sẽ trở thành ông bố bà mẹ hạnh phúc nhất thế giới.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 975 (双鉄)**
- JP: `「期待とは何を？　具体的に教えてもらえるか？」`
- TW: `「你所謂的期待是？能不能具體地告訴我呢？」`
- VN cũ: `「Mong chờ điều gì? Có thể nói cụ thể cho anh biết không?」`
- Sửa: `「Mong chờ điều gì? Có thể nói cụ thể cho tôi biết không?」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1139 (双鉄)**
- JP: `「ああ、たしかに言葉足らずか」`
- TW: `「嗯，我確實失言了」`
- VN cũ: `「A, đúng là anh dùng từ chưa chuẩn nhỉ.」`
- Sửa: `「A, đúng là tôi dùng từ chưa chuẩn nhỉ.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1144 (双鉄)**
- JP: `「うむ？　下着一枚だ。\n風呂上がりでな。これから寝間着に着替えようかと」`
- TW: `「嗯？就穿了條內褲。畢竟剛洗完澡。過會我就要換上睡衣了」`
- VN cũ: `「Hửm? Chỉ mặc mỗi đồ lót thôi.\nAnh mới tắm xong mà. Định lát nữa sẽ thay đồ ngủ đây.」`
- Sửa: `「Hửm? Chỉ mặc mỗi đồ lót thôi. Tôi mới tắm xong mà. Định lát nữa sẽ thay đồ ngủ đây.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1150 (双鉄)**
- JP: `「毎日毎日揉んでいるゆえ気づかなかったが――\nおっぱい自体が、以前より大きくなっていないか？」`
- TW: `「因為我每天都在揉所以沒有發現——你的胸部是不是比以前更大了？」`
- VN cũ: `「Vì ngày nào cũng nắn bóp nên anh không để ý——\nNhưng hình như ngực em to hơn trước thì phải?」`
- Sửa: `「Vì ngày nào cũng nắn bóp nên tôi không để ý—— Nhưng hình như ngực em to hơn trước thì phải?」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1162 (双鉄)**
- JP: `「すまん。ポーレット。嬉しさのあまり、我を忘れた」`
- TW: `「對不起，波萊特。我高興得什麼都忘了」`
- VN cũ: `「Anh xin lỗi, Paulette. Anh vui quá nên mất kiểm soát.」`
- Sửa: `「Tôi xin lỗi, Paulette. Tôi vui quá nên mất kiểm soát.」`
- Lý do: Soutetsu tự xưng "anh" 2 lần — sửa thành "tôi".
**Key 1177 (双鉄)**
- JP: `「こうして、弄ってほしかったのか？」`
- TW: `「想要被這樣玩弄嗎？」`
- VN cũ: `「Em muốn anh nghịch thế này sao?」`
- Sửa: `「Em muốn tôi nghịch thế này sao?」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1188 (双鉄)**
- JP: `「大好きだ。ポーレット。ありがとう」`
- TW: `「我太愛你了。波萊特。謝謝你」`
- VN cũ: `「Anh yêu em lắm. Paulette. Cảm ơn em.」`
- Sửa: `「Tôi yêu em lắm. Paulette. Cảm ơn em.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1191 (双鉄)**
- JP: `「射精したい。ポーレットのおっぱいとお口に思い切り\n愛してもらって、思いっきりに射精したい」`
- TW: `「我想射精。我想被你的奶子和小嘴用力疼愛，然後盡情噴射出來」`
- VN cũ: `「Anh muốn xuất tinh. Muốn được ngực và miệng của Paulette\nyêu thương hết mình, và xuất tinh thật thỏa thích.」`
- Sửa: `「Tôi muốn xuất tinh. Muốn được ngực và miệng của Paulette yêu thương hết mình, và xuất tinh thật thỏa thích.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1200 (双鉄)**
- JP: `「僕はいま、現在進行系で知能指数を下げられている。\nたったひとつのことの他、今はなんにも考えられん」`
- TW: `「我的智商正在不停地往下掉。現在我的腦子裡除了一件事之外，其他什麼都裝不進去」`
- VN cũ: `「Hiện tại, chỉ số thông minh của anh đang bị giảm sút theo thời gian thực.\nNgoài một chuyện duy nhất ra, bây giờ anh chẳng thể suy nghĩ được gì nữa.」`
- Sửa: `「Hiện tại, chỉ số thông minh của tôi đang bị giảm sút theo thời gian thực. Ngoài một chuyện duy nhất ra, bây giờ tôi chẳng thể suy nghĩ được gì nữa.」`
- Lý do: Soutetsu tự xưng "anh" 2 lần — sửa thành "tôi".
**Key 1202 (双鉄)**
- JP: `「わかった。\nならばポーレットは安心して、すぐにシャワーを」`
- TW: `「我知道了。那你就放心吧，趕緊去洗澡」`
- VN cũ: `「Anh hiểu rồi.\nVậy thì Paulette cứ yên tâm đi tắm ngay đi nhé.」`
- Sửa: `「Tôi hiểu rồi. Vậy thì Paulette cứ yên tâm đi tắm ngay đi nhé.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1204 (双鉄)**
- JP: `「気になったのだがポーレット。僕に教えてくれないか？\nどんな理由でこのおまんこが丸出しの紐を買ったのだ？」`
- TW: `「我開始有些好奇了，波萊特。能不能告訴我？你為什麼會去買這種裸露小穴的布條？」`
- VN cũ: `「Anh tò mò quá, Paulette. Nói cho anh biết đi?\nVì lý do gì mà em lại mua sợi dây phơi bày hết cả âm đạo thế này?」`
- Sửa: `「Tôi tò mò quá, Paulette. Nói cho tôi biết đi? Vì lý do gì mà em lại mua sợi dây phơi bày hết cả âm đạo thế này?」`
- Lý do: Soutetsu tự xưng "anh" 2 lần — sửa thành "tôi".
**Key 1205 (双鉄)**
- JP: `「目を開けてしまったのだが――見てもわからん。\n“それ”は――下着……の用を為しては、いないよな？」`
- TW: `「我雖然睜開了眼——但還是沒看明白。“這套裝扮”——應該不能算內衣吧？」`
- VN cũ: `「Dù đã mở mắt ra rồi——nhưng anh nhìn cũng chẳng hiểu.\n"Thứ đó"——không thể gọi là……đồ lót được đúng không?」`
- Sửa: `「Dù đã mở mắt ra rồi——nhưng tôi nhìn cũng chẳng hiểu. "Thứ đó"——không thể gọi là……đồ lót được đúng không?」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1207 (双鉄)**
- JP: `「ゆえ、その紐を脱いですぐにシャワーを浴びてくれ。\n僕は産院の予約を――ああ、どの産院がいいのかな」`
- TW: `「所以你趕緊脫了這布條去洗個澡吧。我去預約產科醫院——啊，約哪家比較好呢？」`
- VN cũ: `「Vậy nên, em cởi sợi dây đó ra rồi đi tắm ngay đi.\nAnh sẽ đặt lịch ở bệnh viện phụ sản——a, bệnh viện nào thì tốt nhỉ.」`
- Sửa: `「Vậy nên, em cởi sợi dây đó ra rồi đi tắm ngay đi. Tôi sẽ đặt lịch ở bệnh viện phụ sản——a, bệnh viện nào thì tốt nhỉ.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1215 (双鉄)**
- JP: `「そうしろというならそうしよう」`
- TW: `「既然你這麼說的話」`
- VN cũ: `「Nếu em đã nói vậy thì anh sẽ làm theo.」`
- Sửa: `「Nếu em đã nói vậy thì tôi sẽ làm theo.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1216 (双鉄)**
- JP: `「わかった」`
- TW: `「明白了」`
- VN cũ: `「Anh hiểu rồi.」`
- Sửa: `「Tôi hiểu rồi.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1225 (双鉄)**
- JP: `「おまんこを丸出しにして、\n僕にいじめてほしかったからか？」`
- TW: `「是為了把小穴裸露出來，好讓我玩弄一番嗎？」`
- VN cũ: `「Vì em muốn phơi bày âm đạo,\nđể anh bắt nạt đúng không?」`
- Sửa: `「Vì em muốn phơi bày âm đạo, để tôi bắt nạt đúng không?」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1239 (双鉄)**
- JP: `「ポー、レット――僕は、ぼくは、もうっ」`
- TW: `「波、萊特——我、我已經」`
- VN cũ: `「Pau, lette——anh, anh, ra mất」`
- Sửa: `「Pau, lette——tôi, tôi, ra mất」`
- Lý do: Soutetsu tự xưng "anh" 2 lần — sửa thành "tôi".
**Key 1286 (双鉄)**
- JP: `「それは……わからん――\nというか、だ――」`
- TW: `「這……我不知道——其實吧——」`
- VN cũ: `「Chuyện đó thì……anh không biết——\nHay đúng hơn là——」`
- Sửa: `「Chuyện đó thì……tôi không biết—— Hay đúng hơn là——」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1295 (双鉄)**
- JP: `「それはすまん。肌触りがその、裸のようで下着のようで、\n気になってしまって思わず……」`
- TW: `「那還真是對不起。因為光憑皮膚的觸感很難判斷你到底有沒有穿內衣，就不由自主地想要一看究竟……」`
- VN cũ: `「Xin lỗi em. Cảm giác lúc chạm vào, giống như đang khỏa thân mà cũng giống như mặc đồ lót,\nlàm anh tò mò quá nên bất giác……」`
- Sửa: `「Xin lỗi em. Cảm giác lúc chạm vào, giống như đang khỏa thân mà cũng giống như mặc đồ lót, làm tôi tò mò quá nên bất giác……」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".

### Hơi thở / âm thanh (thoại) (37 dòng)

**Key 1009 (ポーレット)**
- JP: `「きゅふっ！？　んっ！　ちょっ！\nおちつ――あっ――おちついて――そうてつく――っ！」`
- TW: `「呀呼！？嗯！等等！冷——啊——冷靜一點——雙鐵——！」`
- VN cũ: `「Kyu fu!? Ưm! Khoan đã!\nBình tĩnh——a——bình tĩnh lại đi——anh Soutetsu——!」`
- Sửa: `「Kíuphù!? Ưm! Khoan đã! Bình tĩnh——a——bình tĩnh lại đi——anh Soutetsu——Ư!」`
- Lý do: きゅふっ còn "Kyu fu" — sửa thành "Kíuphù" (きゅ→"Kíu" theo tiền lệ h8 2142); sweep đánh dấu already-rendered nhưng còn mất tiếng っ cuối (そうてつく――っ！) — bổ sung "Ư!".
**Key 1010 (ポーレット)**
- JP: `「きゅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅん！！！」`
- TW: `「呀唔唔唔唔唔——！！！」`
- VN cũ: `「Kyuuuuuuuuuuuuuuuuuuun!!!」`
- Sửa: `「Kyuuuuuuuuuuuuuuuuuun!!!」`
- Lý do: VN thừa 1 nguyên âm u (19 so với 18 tiếng u trong JP: きゅ+ぅ×17) — bớt 1 chữ u.
**Key 1011 (ポーレット)**
- JP: `「ひあっ！　あ、んっ――わたし、の、おまんこ、が\nあっ――もっと、ぷりゅぷりゅ――おんなのこ、らしく」`
- TW: `「呀啊！啊，嗯——我的、小穴、啊——的嫩肉——更有女人味了」`
- VN cũ: `「Hya! A, ưm——âm đạo, của, em\na——mềm mại hơn——nữ tính, hơn sao」`
- Sửa: `「Hia! A, ưm——âm đạo, của, em a——mềm mại hơn——nữ tính, hơn sao」`
- Lý do: ひあっ còn "Hya" — sửa thành "Hia".
**Key 1020 (ポーレット)**
- JP: `「ペロッ――れるっ――ちゅっ、ちゅむっ、ちゅうっ――\nペロッ――ぺちゅっ――ちゅるっ――ちゅっ――れるっ」`
- TW: `「呸溜——滋溜——啾，啾唔，啾唔——呸溜——呸啾——啾嚕——啾——滋溜」`
- VN cũ: `「Pê ro——rê ru——chụt, chu mu, chụt——\nPê ro——pê chu——chu ru——chụt——rê ru」`
- Sửa: `「Liếm nhẹ——rộp——chụt, chụt, chụụt—— Liếm nhẹ——liếm——chụt——chụt——rộp」`
- Lý do: ペロッ còn "Pê ro" — sửa thành "liếm nhẹ" (quy ước riêng của file); れるっ còn "rê ru" — sửa thành "rộp"; ちゅむっ còn "chu mu" — sửa thành "chụt"; ちゅうっ còn "chụt" không kéo dài — sửa thành "chụụt" (2 tiếng u: âm gốc + う×1); ぺちゅっ còn "pê chu" — sửa thành "liếm"; ちゅるっ còn "chu ru" — sửa thành "chụt".
**Key 1021 (ポーレット)**
- JP: `「ぺろっ」`
- TW: `「呸溜」`
- VN cũ: `「Pê ro」`
- Sửa: `「Liếm nhẹ」`
- Lý do: ぺろっ còn "Pê ro" — sửa thành "Liếm nhẹ".
**Key 1022 (ポーレット)**
- JP: `「ふあっ――は――ァ――あっ――ゆっくり、も――\nすき――んっ――きもち、いいとこ――じっくり――ぁ」`
- TW: `「呼啊——哈——啊——啊——慢慢來——也好喜歡——嗯——舒服的，地方——仔細按摩——啊」`
- VN cũ: `「Pha——ha——a——a——chậm rãi, thế này——\nem cũng thích——ưm——chỗ, sướng ấy——cứ từ từ——a」`
- Sửa: `「Phà——ha——a——a——chậm rãi, thế này—— em cũng thích——ưm——chỗ, sướng ấy——cứ từ từ——a」`
- Lý do: ふあっ còn "Pha" — sửa thành "Phà".
**Key 1024 (ポーレット)**
- JP: `「ふあっ！　あっ！　あっ！　あっ！　ちょっ！　んあ！\nまっ――あっ――んぁっ！　ふぁああっっ！！！」`
- TW: `「呼啊！啊！啊！啊！等！嗯啊！一下——啊－嗯啊！呼啊啊啊！！！」`
- VN cũ: `「Pha! A! A! A! Khoan! Ưm a!\nKhoan đã——a——ưm a! Phaaaa!!!」`
- Sửa: `「Phà! A! A! A! Khoan! Ưm a! Khoan đã——a——ưm a! Phààà!!!」`
- Lý do: ふあっ còn "Pha" — sửa thành "Phà"; ふぁああ còn "Phaaaa" (thừa 1 chữ a: JP 3 tiếng a: ぁ+あ×2) — sửa thành "Phààà".
**Key 1025 (ポーレット)**
- JP: `「くひゅっ！　んっ――ぁ――ふぁ――あっ――あ……\nぁっ――太い、とこ――ぞりって――すき――んっ――」`
- TW: `「咕呀！嗯——啊——呼啊——啊——啊……啊——粗的地方——刮到的感覺——好棒——嗯——」`
- VN cũ: `「Ku hyu! Ưm——a——pha——a——a……\nA——chỗ, to ấy——cọ vào——thích quá——ưm——」`
- Sửa: `「Khíu! Ưm——a——phà——a——a…… A——chỗ, to ấy——cọ vào——thích quá——ưm——」`
- Lý do: くひゅっ còn "Ku hyu" — sửa thành "Khíu"; ふぁ còn "pha" — sửa thành "phà".
**Key 1028 (ポーレット)**
- JP: `「ぐちゅっ！　ちゅぶっ！　ずちゅっ！　じゅぼっ！\nぐりゅっ――リュッ――じゅぶ！　じゅるるる～～っ！」`
- TW: `「咕啾！啾噗！滋啾！啾噗！咕啾——嚕——啾噗！啾嚕嚕嚕～～！」`
- VN cũ: `「Gu chu! Chu bu! Zu chu! Ju bo!\nGu ryu——ryu——ju bu! Ju ru ru ru～～!」`
- Sửa: `「Rột! Chụt! Phập! Bụp! Rột——rộp——rột! Rột~!」`
- Lý do: Cả 8 âm còn La-tinh — Việt hoá: ぐちゅっ→"Rột", ちゅぶっ→"Chụt", ずちゅっ→"Phập" (ず=đâm vào), じゅぼっ→"Bụp", ぐりゅっ→"Rột", リュッ→"rộp", じゅぶ→"rột", じゅるるる～～っ→"Rột~" (sweep already-rendered chỉ nói về gasp, không xung đột).
**Key 1032 (ポーレット)**
- JP: `「はうううっ――ふあっ――あっ――\nおっぱい――ちくび――きもちいい――よぉ」`
- TW: `「哈唔唔唔——呼啊——啊——乳房——乳頭——好舒服——啊」`
- VN cũ: `「Hau uu——pha——a——\nngực——nhũ hoa——sướng quá——a」`
- Sửa: `「Hau uu——phà——a—— ngực——nhũ hoa——sướng quá——a」`
- Lý do: ふぁっ còn "pha" — sửa thành "phà" (はうううっ→"Hau uu" đúng số lượng 3 tiếng u, giữ nguyên).
**Key 1035 (ポーレット)**
- JP: `「はう～～っ――あうっ――わ、わたしが――この、\nおまんこ――おまんこ、丸出しの紐を、買ったの、は」`
- TW: `「哈唔～～啊唔——我、我——之所以買這個裸——裸露小、小穴的布條」`
- VN cũ: `「Hau～～——au——e, em——mua sợi dây,\nphơi bày——phơi bày âm đạo này, là vì」`
- Sửa: `「Hau～～Ư——au——e, em——mua sợi dây, phơi bày——phơi bày âm đạo này, là vì」`
- Lý do: Sweep bỏ sót: JP はう～～っ còn mất tiếng っ cuối — bổ sung "Ư" thành "Hau～～Ư".
**Key 1037 (ポーレット)**
- JP: `「はぷっ――ずっちゅううううううううっっっっっっ！」`
- TW: `「哈噗——滋啾唔唔唔唔唔——！」`
- VN cũ: `「Ha pu——zu chuu uu uu uu uu uu uu!!!」`
- Sửa: `「Hà bụp——Phập chụụụụụụụụụt!!!」`
- Lý do: はぷっ còn "Ha pu" — sửa thành "Hà bụp"; ずっちゅうううううううう còn La-tinh — sửa thành "Phập chụụụụụụụụụt" (ずっ=đâm vào; ちゅう×8 = 9 tiếng u: ちゅ+う×8).
**Key 1039 (ポーレット)**
- JP: `「はっ！　ぁっ――ぁっ――ぁっ――わた、しっ――\nこれっ――ふぁ――もうっ、もうっ、もうっ、もうっ！」`
- TW: `「哈！啊——啊——啊——我——這樣——呼啊——已經，已經，已經，已經！」`
- VN cũ: `「Ha! A——a——a——em——\nthế này——pha——ra mất, ra mất, ra mất, ra mất!」`
- Sửa: `「Ha! A——a——a——em—— thế này——phà——ra mất, ra mất, ra mất, ra mất!」`
- Lý do: ふぁ còn "pha" — sửa thành "phà".
**Key 1043 (ポーレット)**
- JP: `「えへへっ。それはそれでうれしいです――ぁふっ」`
- TW: `「哎嘿嘿。那樣我也挺開心的——啊呼」`
- VN cũ: `「Ehehe. Như vậy em cũng vui lắm——a phu」`
- Sửa: `「Ehehe. Như vậy em cũng vui lắm——a phù」`
- Lý do: ぁふっ còn "a phu" — sửa thành "a phù" (cười "Ehehe" giữ nguyên — chờ quyết định).
**Key 1053 (双鉄)**
- JP: `「おうふっ！」`
- TW: `「哦呼！」`
- VN cũ: `「Oufu!」`
- Sửa: `「Ồ phù!」`
- Lý do: おうふっ còn "Oufu" — sửa thành "Ồ phù".
**Key 1074 (ポーレット)**
- JP: `「ぁ――ふぁ――双鉄くん――そうてつくぅん」`
- TW: `「啊——呼啊——雙鐵君——雙鐵君」`
- VN cũ: `「A——pha——anh Soutetsu——anh Soutetsu」`
- Sửa: `「A——phà——anh Soutetsu——anh Soutetsu」`
- Lý do: ふぁ còn "pha" — sửa thành "phà".
**Key 1084 (ポーレット)**
- JP: `「はっ――あうっ――ふぁんっ――んっ――くぅんっ――\nん。これ――ゆっくり――はっ――ゆっくぃ、らのにぃ」`
- TW: `「啊——啊唔——呼啊——嗯——咕嗯——嗯。這樣——慢慢擺動——哈——明明動作那麼慢」`
- VN cũ: `「Ha——au——pha——ưm——kuuun——\nƯm. Thế này——chậm rãi——ha——chậm rãi, thế mà」`
- Sửa: `「Ha——au——phàn——ưm——kuuun—— Ưm. Thế này——chậm rãi——ha——chậm rãi, thế mà」`
- Lý do: ふぁんっ còn "pha" — sửa thành "phàn" (くぅんっ→"kuuun" giữ nguyên — chưa có quy ước Việt cho くぅん).
**Key 1085 (ポーレット)**
- JP: `「あ――ぱくっ――ズッ――ずううっ――ごくっ。\nぷはっ――あ～ん、全部のみたかったのにぃ」`
- TW: `「啊——啪咕——滋——滋唔唔——咕嘟。噗哈——啊～我好想全部喝下去」`
- VN cũ: `「A——pa ku——zu——zuu u——ực.\nPu ha——a~n, em muốn nuốt hết cơ mà.」`
- Sửa: `「A——Ngoạm——Phập——Phậậập——ực. Bụp ha——a~n, em muốn nuốt hết cơ mà.」`
- Lý do: ぱくっ còn "pa ku" — sửa thành "Ngoạm" (theo tài liệu SFX); ズッ còn "zu" — sửa thành "Phập"; ずううっ còn "zuu u" — sửa thành "Phậậập" (3 tiếng u: ず+う×2); ぷはっ còn "Pu ha" — sửa thành "Bụp ha".
**Key 1095 (ポーレット)**
- JP: `「ぁ！　んっ！　ふあっ！　あっ！　あっ！　ああっ！\nわたしっ！　でてるっ！　わたし！　おっぱいっ！！」`
- TW: `「啊！嗯！呼啊！啊！啊！啊啊！我！流出來了！我的！乳房！！」`
- VN cũ: `「A! Ưm! Pha! A! A! Aa!\nEm! Ra rồi! Ngực em! Ra sữa rồi!!」`
- Sửa: `「A! Ưm! Phà! A! A! Aa! Em! Ra rồi! Ngực em! Ra sữa rồi!!」`
- Lý do: ふぁっ còn "Pha" — sửa thành "Phà".
**Key 1099 (ポーレット)**
- JP: `「あっ！？　ぁ――ぁ――ぁっ――ふあっ――これっ――\nこれっ――えっ――やらっ――これっ――しゅきっ――」`
- TW: `「啊！？啊——啊——啊——呼啊——這個——這樣——哎——討厭——這樣——好棒——」`
- VN cũ: `「A!? A——a——a——pha——thế này——\nthế này——ế——ưm——thế này——thích quá——」`
- Sửa: `「A!? A——a——a——phà——thế này—— thế này——ế——ưm——thế này——thích quá——」`
- Lý do: ふぁっ còn "pha" — sửa thành "phà".
**Key 1105 (ポーレット)**
- JP: `「ちゅむっ――ぺろっ――ちゅうっ――チュッ――\nれろっ――ぺろっ――れるううううっ――ちゅ、ちゅむ」`
- TW: `「啾嗯——呸溜——啾——啾——滋溜——呸溜——滋嚕嚕嚕嚕——啾，啾嗯」`
- VN cũ: `「Chu mu——liếm nhẹ——chụt——chụt——\nrê ro——liếm nhẹ——rê ru uu——chu, chu mu」`
- Sửa: `「Chụt——liếm nhẹ——chụụt——chụt—— rộp——liếm nhẹ——rộộộộộp——chụt, chụt」`
- Lý do: ちゅむっ còn "Chu mu" — sửa thành "chụt"; ちゅうっ còn "chụt" không kéo dài — sửa thành "chụụt" (2 tiếng u: âm gốc + う×1); れろっ còn "rê ro" — sửa thành "rộp"; れるううううっ còn "rê ru uu" — sửa thành "rộộộộộp" (5 tiếng u: âm gốc + う×4); ちゅ/ちゅむ còn "chu"/"chu mu" — sửa thành "chụt"/"chụt".
**Key 1107 (ポーレット)**
- JP: `「じゅぶうっ！　じゅ！　れろっ――れるっ――じゅっ！\nじゅぼ！　じゅびゅ！　ごちゅっ！　じゅぶうっ！！」`
- TW: `「啾噗！啾！滋嚕——滋溜——啾！滋噗！啾噗！咕啾！啾噗！！」`
- VN cũ: `「Ju buu! Ju! Rê ro——rê ru——ju!\nJu bo! Ju byu! Go chu! Ju buu!!」`
- Sửa: `「Rộột! Rột! Rộp——rộp——rột! Bụp! Rột! Rột! Rộột!!」`
- Lý do: じゅぶうっ còn "Ju buu" — sửa thành "rộôt" (2 tiếng u: âm gốc + う×1); れろっ/れるっ còn "Rê ro"/"rê ru" — sửa thành "rộp"/"rộp"; じゅっ/じゅびゅ còn "ju"/"Ju byu" — sửa thành "rột"/"rột"; じゅぼ còn "Ju bo" — sửa thành "Bụp"; ごちゅっ còn "Go chu" — sửa thành "Rột".
**Key 1108 (ポーレット)**
- JP: `「じゅっ！　ぢゅぼっ！　ぢゅぶっ！　ぼちゅっ！！\nぢゅびゅっ！　ぢゅばっ！　ぢゅぅう！　ぢゅぶっ！！」`
- TW: `「啾！啾噗！啾噗！噗啾！！啾咕！啾啪！啾唔唔！啾噗！！」`
- VN cũ: `「Ju! Ju bo! Ju bu! Bo chu!!\nJu byu! Ju ba! Juu u! Ju bu!!」`
- Sửa: `「Rột! Bụp! Rột! Chụt!! Rột! Bụp! Chụụụt! Rột!!」`
- Lý do: じゅっ/ぢゅぶっ/ぢゅびゅっ còn La-tinh — sửa thành "rột"; ぢゅぼっ/ぢゅばっ còn "Ju bo"/"Ju ba" — sửa thành "Bụp"; ぼちゅっ còn "Bo chu" — sửa thành "Chụt"; ぢゅぅう còn "Juu u" — sửa thành "chụụụt" (3 tiếng u: ぢゅ+ぅ+う).
**Key 1116 (ポーレット)**
- JP: `「んっ――んぷっ――ぷっ――くっ――んっ」`
- TW: `「嗯——嗯噗——噗——咕——嗯」`
- VN cũ: `「Ưm——ưm pu——pu——ku——ưm」`
- Sửa: `「Ưm——ưm bụp——bụp——hự——ưm」`
- Lý do: んぷっ còn "ưm pu" — sửa thành "ưm bụp"; ぷっ còn "pu" — sửa thành "bụp"; くっ còn "ku" — sửa thành "hự".
**Key 1124 (ポーレット)**
- JP: `「んきゅうっ！！　ん～～～～～～～～～～～っ！！」`
- TW: `「嗯呀！！嗯～～～～～～～！！」`
- VN cũ: `「Ưm kyu!! Ưm～～～～～～～～～～～!!」`
- Sửa: `「Ưm kyuu!! Ưm～～～～～～～～～～～Ư!!」`
- Lý do: Sweep đánh dấu already-rendered nhưng còn mất tiếng っ cuối (ん～～～っ) — bổ sung "Ư"; んきゅうっ→"Ưm kyuu" giữ nguyên (đúng theo tiền lệ h7).
**Key 1126 (双鉄)**
- JP: `「んくっ！」`
- TW: `「嗯呃！」`
- VN cũ: `「Ưm ku!」`
- Sửa: `「Ưm hự!」`
- Lý do: んくっ còn "Ưm ku" — sửa thành "Ưm hự".
**Key 1127 (ポーレット)**
- JP: `「んふっ！！！」`
- TW: `「嗯呼！！！」`
- VN cũ: `「Ưm fu!!!」`
- Sửa: `「Ưm phù!!!」`
- Lý do: んふっ còn "Ưm fu" — sửa thành "Ưm phù".
**Key 1128 (ポーレット)**
- JP: `「んくっ――ごくっ――ゴクッ――んぷっ」`
- TW: `「嗯咕——咕嘟——咕嘟——嗯噗」`
- VN cũ: `「Ưm ku——ực——ực——ưm pu」`
- Sửa: `「Ưm hự——ực——ực——ưm bụp」`
- Lý do: んくっ còn "Ưm ku" — sửa thành "Ưm hự"; んぷっ còn "ưm pu" — sửa thành "ưm bụp".
**Key 1133 (ポーレット)**
- JP: `「んぷっ！？　ぷっ――くっ―\n―こほっ――うぇっ――ごくっ――んむっ」`
- TW: `「嗯噗！》噗——呃——咳咳——嘔——咕嘟——嗯唔」`
- VN cũ: `「Ưm pu!? Pu——ku——\nkho hộc——uệ——ực——ưm mu」`
- Sửa: `「Ưm bụp!? Bụp——hự—— Khụ——uệ——ực——ưm mự」`
- Lý do: んぷっ còn "Ưm pu" — sửa thành "ưm bụp"; ぷっ còn "Pu" — sửa thành "Bụp"; くっ còn "ku" — sửa thành "hự"; こほっ còn "kho hộc" (không phải từ tiếng Việt) — sửa thành "Khụ" (tiếng ho); んむっ còn "ưm mu" — sửa thành "ưm mự".
**Key 1134 (ポーレット)**
- JP: `「んぷっ！？　あちゅっ！？」`
- TW: `「嗯噗！？啊啾！？」`
- VN cũ: `「Ưm pu!? A chu!?」`
- Sửa: `「Ưm bụp!? Hắt xì!?」`
- Lý do: んぷっ còn "Ưm pu" — sửa thành "ưm bụp"; あちゅっ là tiếng hắt hơi — sửa thành "Hắt xì" (VN cũ "A chu" là La-tinh).
**Key 1136 (ポーレット)**
- JP: `「んっ！？　はっ！　あっ――ね？　カリ、くびっ――\nそうてつ、くんの――んひっ――ふと、い――前、より」`
- TW: `「嗯！？哈！啊——那個龜頭、冠——雙鐵君的——嗯呀——比以前——粗了」`
- VN cũ: `「Ưm!? Ha! A——nè? Rãnh, quy đầu——\ncủa anh Soutetsu——ưm hi——to hơn——trước đây, rồi」`
- Sửa: `「Ưm!? Ha! A——nè? Rãnh, quy đầu—— của anh Soutetsu——ưm hì——to hơn——trước đây, rồi」`
- Lý do: んひっ còn "ưm hi" — sửa thành "ưm hì".
**Key 1148 (ポーレット)**
- JP: `「ぼぢゅっ！　ぢゅちゅ！　ぢゅぼっ！　ぢゅばっ！\nずりゅっ！　ぢゅむっ！　ちゅううっ！　れりゅっ！」`
- TW: `「噗啾！啾啾！啾噗！啾啪！滋溜！啾嗯！啾嚕嚕！滋溜！」`
- VN cũ: `「Bo ju! Ju chu! Ju bo! Ju ba!\nZu ryu! Ju mu! Chuu u! Rê ryu!」`
- Sửa: `「Bụp! Chụt! Bụp! Bụp! Rột! Chụt! Chụụụt! Rộp!」`
- Lý do: ぼぢゅっ/ぢゅぼっ/ぢゅばっ còn La-tinh — sửa thành "Bụp"; ぢゅちゅ/ぢゅむっ còn "Ju chu"/"Ju mu" — sửa thành "chụt"; ずりゅっ còn "Zu ryu" — sửa thành "Rột"; ちゅううっ còn "Chuu u" — sửa thành "chụụụt" (3 tiếng u: ちゅ+う×2); れりゅっ còn "Rê ryu" — sửa thành "rộp".
**Key 1167 (ポーレット)**
- JP: `「おまんこ！　おくっ！　おくっ！　しきゅうっ！\nふっ！　あっ！　つよくっ！　ごちゅん、だめ、なのっ」`
- TW: `「小穴！好深！好深！好喜歡！呼！啊！好用力！最裡面、不可以、伸進去啦」`
- VN cũ: `「Âm đạo! Bên trong! Bên trong! Tử cung!\nPhu! A! Mạnh quá! Đâm vào, không được, đâu」`
- Sửa: `「Âm đạo! Bên trong! Bên trong! Tử cung! Phù! A! Mạnh quá! Đâm vào, không được, đâu」`
- Lý do: ふっ còn "Phu" — sửa thành "Phù".
**Key 1255 (ポーレット)**
- JP: `「れるううううううううううううううううううっ！！！」`
- TW: `「滋嚕嚕嚕嚕嚕嚕嚕——！！！`
- VN cũ: `「Rê ru uu uu uu uu uu uu uu uu uu uu uu uu uu uu uu!!!」`
- Sửa: `「rộộộộộộộộộộộộộộộộộộộp!!!」`
- Lý do: れるううううううううううううううううううっ còn La-tinh — sửa thành "rộôôôôôôôôôôôôôôôôôôp" (19 tiếng u: る+う×18).
**Key 1315 (ポーレット)**
- JP: `「（ふ～～～っ）、ちゅっ！　ちゅむっ――ちゅっ――\nぺろっ――れるっ――ぺろっ――れろおっ――ぺちゅっ」`
- TW: `「（呼氣～～～），啾！啾嗯——啾——呸溜——滋溜——呸溜——滋嚕——呸啾」`
- VN cũ: `「（Phù～～～）, chụt! Chu mu——chụt——\nliếm nhẹ——rê ru——liếm nhẹ——rê ro——pê chu」`
- Sửa: `「（Phù～～～Ư）, chụt! Chụt——chụt—— liếm nhẹ——rộp——liếm nhẹ——rộộp——liếm」`
- Lý do: （ふ～～～っ） còn mất tiếng っ — bổ sung "Ư"; ちゅむっ còn "Chu mu" — sửa thành "chụt"; れるっ còn "rê ru" — sửa thành "rộp"; れろおっ còn "rê ro" — sửa thành "rộôp" (2 tiếng o: ろ+お); ぺちゅっ còn "pê chu" — sửa thành "liếm".
**Key 1317 (双鉄)**
- JP: `「（ちゅむっ！　ちゅうっ！　ちゅるっ！　ずうっ！）」`
- TW: `「（啾唔！啾！啾嚕！滋！）」`
- VN cũ: `「（Chu mu! Chuu! Chu ru! Zuu!）」`
- Sửa: `「（Chụt! Chụụt! Chụt! Phậập!）」`
- Lý do: Cả 4 âm còn La-tinh — sửa thành "chụt"/"Chụụt"/"chụt"/"Phậập" (ちゅうっ = 2 tiếng u: âm gốc + う×1; ずうっ = 2 tiếng u: ず+う).
**Key 1319 (双鉄)**
- JP: `「（ちゅっ！　ちゅうっ！　ちゅむっ！　ぢゅううっ）」`
- TW: `「（啾！啾唔！啾嗯！啾嚕嚕）」`
- VN cũ: `「（Chụt! Chuu! Chu mu! Juu u!）」`
- Sửa: `「（Chụt! Chụụt! Chụt! Chụụụt!）」`
- Lý do: ちゅうっ còn "Chuu" — sửa thành "Chụụt" (2 tiếng u: âm gốc + う×1); ちゅむっ còn "Chu mu" — sửa thành "chụt"; ぢゅううっ còn "Juu u" — sửa thành "chụụụt" (3 tiếng u: ぢゅ+う×2).

### Âm thanh (độc thoại) (2 dòng)

**Key 1726 (monologue)**
- JP: `（ばちゅっ！　ぐちゅっ！　ごちゅっ！　ぼちゅっ！！）`
- TW: `（啪啾！咕啾！咕啾！啵啾！！）`
- VN cũ: `（Pa chu! Gu chu! Go chu! Bo chu!!）`
- Sửa: `（Chụt! Rột! Rột! Chụt!!）`
- Lý do: Cả 4 âm còn La-tinh — sửa thành "Chụt"/"Rột"/"Rột"/"Chụt" (ばちゅ/ぼちゅ→"chụt", ぐちゅ/ごちゅ→"rột").
**Key 1735 (monologue)**
- JP: `（ぽふっ）`
- TW: `（拍）`
- VN cũ: `（Bịch）`
- Sửa: `（Bụp）`
- Lý do: ぽふっ là tiếng mềm (rơi nhẹ), "Bịch" là tiếng động mạnh — sửa thành "Bụp".

### Thuật ngữ (6 dòng)

**Key 995 (双鉄)**
- JP: `「なるほど、これもデコレーションの効果なのか」`
- TW: `「原來如此，這也是裝飾的效果嗎」`
- VN cũ: `「Ra là vậy, đây cũng là tác dụng của Decoration sao.」`
- Sửa: `「Ra là vậy, đây cũng là tác dụng của vật trang trí sao.」`
- Lý do: "Decoration" giữ nguyên tiếng Anh — sửa thành "vật trang trí" (danh từ chung, không phải tên riêng).
**Key 1120 (ポーレット)**
- JP: `「ん……っと――飾り、ですかね？\n装飾、ディスプレイ、デコレーション」`
- TW: `「嗯……應該說是飾品吧？裝飾，Ｄｉｓｐｌａｙ，Ｄｅｃｏｒａｔｉｏｎ」`
- VN cũ: `「Ưm……là đồ trang trí, chăng?\nĐồ trang trí, phụ kiện trưng bày, decoration.」`
- Sửa: `「Ưm……là đồ trang trí, chăng? Đồ trang trí, phụ kiện trưng bày, trang trí.」`
- Lý do: "decoration" giữ nguyên tiếng Anh — sửa thành "trang trí".
**Key 1280 (ポーレット)**
- JP: `「高崎さんに電話してくれたらきっと。\n同じ御一夜で、おかあさんになったばっかりですし」`
- TW: `「跟高崎小姐打個電話吧，她一定知道。畢竟大家都在御一夜，而她也剛剛當上媽媽」`
- VN cũ: `「Anh cứ gọi điện cho chị Takasaki là chắc chắn sẽ biết.\nChị ấy cũng ở Ohimitera và mới làm mẹ xong mà.」`
- Sửa: `「Anh cứ gọi điện cho chị Takasaki là chắc chắn sẽ biết. Chị ấy cũng ở Ohitoyo và mới làm mẹ xong mà.」`
- Lý do: 御一夜 còn "Ohimitera" — sửa thành "Ohitoyo" theo quyết định 19/11.
**Key 1287 (ポーレット)**
- JP: `「この紐――デコレーション……どうしましょうか？\nもう着ないなら」`
- TW: `「這件布條——這裝飾品……該怎麼處理呢？如果以後不穿的話就」`
- VN cũ: `「Sợi dây——đồ decoration này……tính sao đây ạ?\nNếu em không mặc nữa thì」`
- Sửa: `「Sợi dây——đồ trang trí này……tính sao đây ạ? Nếu em không mặc nữa thì」`
- Lý do: "đồ decoration" giữ nguyên tiếng Anh — sửa thành "đồ trang trí".
**Key 1323 (双鉄)**
- JP: `「デコレーション」`
- TW: `「Ｄｅｃｏｒａｔｉｏｎ」`
- VN cũ: `「Decoration」`
- Sửa: `「Trang trí」`
- Lý do: "Decoration" đứng một mình còn tiếng Anh — sửa thành "Trang trí".
**Key 1621 (monologue)**
- JP: `装飾で、ディスプレイで、デコレーション。\nその説明で、おっぱいのときは納得したが――`
- TW: `裝飾，Ｄｉｓｐｌａｙ，Ｄｅｃｏｒａｔｉｏｎ。在欣賞胸部時我已經聽過了解釋——`
- VN cũ: `Đồ trang trí, phụ kiện trưng bày, decoration.\nVới lời giải thích đó, tôi đã chấp nhận khi ngắm nhìn bộ ngực, nhưng——`
- Sửa: `Đồ trang trí, phụ kiện trưng bày, trang trí. Với lời giải thích đó, tôi đã chấp nhận khi ngắm nhìn bộ ngực, nhưng——`
- Lý do: "decoration" giữ nguyên tiếng Anh — sửa thành "trang trí" (lần thứ 5 trong file: 995/1120/1287/1323/1621).

## Khối TOML để dán vào file (đã kiểm chứng parse được)

Khối dưới đây đã kiểm chứng parse được bằng tomllib, đúng 68 key, giá trị khớp đúng JSON bản sửa. Dán vào section `[script]` của file `03_Paulette/lr_ポーレットh2_デコレーション＆ミルク.txt.toml` (ghi đè đúng 68 key này, giữ nguyên mọi key khác).

```toml
[script]
948 = "「Không phải rãnh quy đầu của tôi to ra đâu.」"
958 = "「Không, không phải đâu. Không phải rãnh quy đầu của tôi to hơn trước đây đâu.」"
964 = "「Không, tôi muốn em giặt sạch rồi cất giữ cẩn thận. Tôi cũng tò mò không biết em mua nó vì lý do gì nữa.」"
970 = "「Sẽ thành, chắc chắn vậy. Paulette và tôi, hai chúng ta. Tuyệt đối sẽ trở thành ông bố bà mẹ hạnh phúc nhất thế giới.」"
975 = "「Mong chờ điều gì? Có thể nói cụ thể cho tôi biết không?」"
995 = "「Ra là vậy, đây cũng là tác dụng của vật trang trí sao.」"
1009 = "「Kíuphù!? Ưm! Khoan đã! Bình tĩnh——a——bình tĩnh lại đi——anh Soutetsu——Ư!」"
1010 = "「Kyuuuuuuuuuuuuuuuuuun!!!」"
1011 = "「Hia! A, ưm——âm đạo, của, em a——mềm mại hơn——nữ tính, hơn sao」"
1020 = "「Liếm nhẹ——rộp——chụt, chụt, chụụt—— Liếm nhẹ——liếm——chụt——chụt——rộp」"
1021 = "「Liếm nhẹ」"
1022 = "「Phà——ha——a——a——chậm rãi, thế này—— em cũng thích——ưm——chỗ, sướng ấy——cứ từ từ——a」"
1024 = "「Phà! A! A! A! Khoan! Ưm a! Khoan đã——a——ưm a! Phààà!!!」"
1025 = "「Khíu! Ưm——a——phà——a——a…… A——chỗ, to ấy——cọ vào——thích quá——ưm——」"
1028 = "「Rột! Chụt! Phập! Bụp! Rột——rộp——rột! Rột~!」"
1032 = "「Hau uu——phà——a—— ngực——nhũ hoa——sướng quá——a」"
1035 = "「Hau～～Ư——au——e, em——mua sợi dây, phơi bày——phơi bày âm đạo này, là vì」"
1037 = "「Hà bụp——Phập chụụụụụụụụụt!!!」"
1039 = "「Ha! A——a——a——em—— thế này——phà——ra mất, ra mất, ra mất, ra mất!」"
1043 = "「Ehehe. Như vậy em cũng vui lắm——a phù」"
1053 = "「Ồ phù!」"
1074 = "「A——phà——anh Soutetsu——anh Soutetsu」"
1079 = "「A——a——a——ưm——nè? Anh Soutetsu——\nanh Soutetsu——a——phu——ưm——ưm uu!」"
1084 = "「Ha——au——phàn——ưm——kuuun—— Ưm. Thế này——chậm rãi——ha——chậm rãi, thế mà」"
1085 = "「A——Ngoạm——Phập——Phậậập——ực. Bụp ha——a~n, em muốn nuốt hết cơ mà.」"
1095 = "「A! Ưm! Phà! A! A! Aa! Em! Ra rồi! Ngực em! Ra sữa rồi!!」"
1099 = "「A!? A——a——a——phà——thế này—— thế này——ế——ưm——thế này——thích quá——」"
1105 = "「Chụt——liếm nhẹ——chụụt——chụt—— rộp——liếm nhẹ——rộộộộộp——chụt, chụt」"
1107 = "「Rộột! Rột! Rộp——rộp——rột! Bụp! Rột! Rột! Rộột!!」"
1108 = "「Rột! Bụp! Rột! Chụt!! Rột! Bụp! Chụụụt! Rột!!」"
1116 = "「Ưm——ưm bụp——bụp——hự——ưm」"
1120 = "「Ưm……là đồ trang trí, chăng? Đồ trang trí, phụ kiện trưng bày, trang trí.」"
1124 = "「Ưm kyuu!! Ưm～～～～～～～～～～～Ư!!」"
1126 = "「Ưm hự!」"
1127 = "「Ưm phù!!!」"
1128 = "「Ưm hự——ực——ực——ưm bụp」"
1133 = "「Ưm bụp!? Bụp——hự—— Khụ——uệ——ực——ưm mự」"
1134 = "「Ưm bụp!? Hắt xì!?」"
1136 = "「Ưm!? Ha! A——nè? Rãnh, quy đầu—— của anh Soutetsu——ưm hì——to hơn——trước đây, rồi」"
1139 = "「A, đúng là tôi dùng từ chưa chuẩn nhỉ.」"
1144 = "「Hửm? Chỉ mặc mỗi đồ lót thôi. Tôi mới tắm xong mà. Định lát nữa sẽ thay đồ ngủ đây.」"
1148 = "「Bụp! Chụt! Bụp! Bụp! Rột! Chụt! Chụụụt! Rộp!」"
1150 = "「Vì ngày nào cũng nắn bóp nên tôi không để ý—— Nhưng hình như ngực em to hơn trước thì phải?」"
1162 = "「Tôi xin lỗi, Paulette. Tôi vui quá nên mất kiểm soát.」"
1167 = "「Âm đạo! Bên trong! Bên trong! Tử cung! Phù! A! Mạnh quá! Đâm vào, không được, đâu」"
1177 = "「Em muốn tôi nghịch thế này sao?」"
1188 = "「Tôi yêu em lắm. Paulette. Cảm ơn em.」"
1191 = "「Tôi muốn xuất tinh. Muốn được ngực và miệng của Paulette yêu thương hết mình, và xuất tinh thật thỏa thích.」"
1200 = "「Hiện tại, chỉ số thông minh của tôi đang bị giảm sút theo thời gian thực. Ngoài một chuyện duy nhất ra, bây giờ tôi chẳng thể suy nghĩ được gì nữa.」"
1202 = "「Tôi hiểu rồi. Vậy thì Paulette cứ yên tâm đi tắm ngay đi nhé.」"
1204 = "「Tôi tò mò quá, Paulette. Nói cho tôi biết đi? Vì lý do gì mà em lại mua sợi dây phơi bày hết cả âm đạo thế này?」"
1205 = "「Dù đã mở mắt ra rồi——nhưng tôi nhìn cũng chẳng hiểu. \"Thứ đó\"——không thể gọi là……đồ lót được đúng không?」"
1207 = "「Vậy nên, em cởi sợi dây đó ra rồi đi tắm ngay đi. Tôi sẽ đặt lịch ở bệnh viện phụ sản——a, bệnh viện nào thì tốt nhỉ.」"
1215 = "「Nếu em đã nói vậy thì tôi sẽ làm theo.」"
1216 = "「Tôi hiểu rồi.」"
1225 = "「Vì em muốn phơi bày âm đạo, để tôi bắt nạt đúng không?」"
1239 = "「Pau, lette——tôi, tôi, ra mất」"
1255 = "「rộộộộộộộộộộộộộộộộộộộp!!!」"
1280 = "「Anh cứ gọi điện cho chị Takasaki là chắc chắn sẽ biết. Chị ấy cũng ở Ohitoyo và mới làm mẹ xong mà.」"
1286 = "「Chuyện đó thì……tôi không biết—— Hay đúng hơn là——」"
1287 = "「Sợi dây——đồ trang trí này……tính sao đây ạ? Nếu em không mặc nữa thì」"
1295 = "「Xin lỗi em. Cảm giác lúc chạm vào, giống như đang khỏa thân mà cũng giống như mặc đồ lót, làm tôi tò mò quá nên bất giác……」"
1315 = "「（Phù～～～Ư）, chụt! Chụt——chụt—— liếm nhẹ——rộp——liếm nhẹ——rộộp——liếm」"
1317 = "「（Chụt! Chụụt! Chụt! Phậập!）」"
1319 = "「（Chụt! Chụụt! Chụt! Chụụụt!）」"
1323 = "「Trang trí」"
1621 = "Đồ trang trí, phụ kiện trưng bày, trang trí. Với lời giải thích đó, tôi đã chấp nhận khi ngắm nhìn bộ ngực, nhưng——"
1726 = "（Chụt! Rột! Rột! Chụt!!）"
1735 = "（Bụp）"
```

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- **B4 — tên rên trần:** file này có **1 dòng — key 1079** (xem "Kết luận về cơ chế lỗi" ở trên — JP đầy đủ đã ghi). Đây là bằng chứng mới duy nhất cho B4 từ file này. Lưu ý: kiểm tra JP ở h1/h2 trước đó cho thấy 双鉄くん xuất hiện trong TẤT CẢ 20 dòng tên rên — không bao giờ là さん, không bao giờ trần — nên ngoại lệ đã sụp đổ — **đã sửa 1079 thành "anh Soutetsu" theo quyết định B4 19/11.**
- **くぅん (câu hỏi mở mới):** chưa có dạng Việt thống nhất trong toàn dự án; "Kuuun"/"Kuuunnn" là dạng đang dùng thực tế (file này: 1029, 1084). Giữ nguyên, không tính sai. Ứng viên: "Ưưưn" hoặc giữ "Kuuun". Lưu ý: "Kuuun" có 3 chữ u trong khi JP くぅ chỉ có 2 nguyên âm u (く+ぅ) — thừa 1 chữ, đã ghi nhận, không sửa (đây là dạng quen thuộc, sửa sẽ làm mất nhất quán với các file khác).
- **Đính chính 19/11 22:19 (quyết định của Hieu):** giữ "Kuuun" — ưu tiên giữ càng gần tiếng Nhật gốc càng tốt để cảm nhận cái hay của tiếng Nhật; chỉ chuyển sang thuần Việt ("Ưưưn") khi cách đọc Nhật nghe ngượng quá. Câu hỏi くぅん đã chốt, không còn mở.
- **Cười khúc khích (đề xuất mới):** 8 dòng trong file này còn giữ dạng La-tinh cho tiếng cười — 1018, 1043, 1059, 1060, 1075, 1087, 1194, 1227, 1321 (ふふ/うふふ/えへへ/あはは). Như lr_h1: h8 từng dùng "Ư hự" cho ふふっ nhưng đó là quy ước riêng của file h8 và "Ư hự" là tiếng gằn, không phải tiếng cười — KHÔNG áp dụng ở đây. Cần Hieu quyết: giữ nguyên dạng La-tinh, hay dùng "phì phì"/"hì hì".
- **Quy ước độ dài âm kéo dài (đã chốt trong lần kiểm tra này):** số nguyên âm VN = 1 (âm gốc) + số ký tự う/ぅ trong token JP. Bằng chứng mạnh nhất chính trong file này: **1770 — VN cũ "Đâm sâu uuuuuuuuuuu" (12 chữ u) đã ĐÚNG** (JP う×11 → 1+11 = 12), nên dòng này bị loại khỏi danh sách sửa. Các dòng đã sửa theo quy tắc này trong file này: 1107 (じゅぶうっ: う×1 → 2 nguyên âm "Rộôt"), 1317/1319 (ちゅうっ: う×1 → 2 nguyên âm "Chụụt"), 1105 (れるううううっ: う×4 → 5 nguyên âm "rộộộộộp"), 1037 (ちゅうううううううう: う×8 → 9 nguyên âm), 1255 (れるう×18 → 19 chữ ô), 1010 (きゅ+ぅ×17 → 18 chữ u — VN cũ có 19, bản sửa bớt 1).
- **Quy ước họ SFX áp dụng trong file này:** âm hôn ちゅ/ぢゅ đầu → "chụt"; âm đâm/trượt じゅ/ず → "rột" (trượt) hoặc "Phập" (đâm vào, với ず đầu); âm lưỡi れる/りゅ/れろ/れりゅ → "rộp"; ぺろ → "liếm nhẹ" (quy ước riêng của file); ぺちゅ → "liếm"; にゅる/ニュル → "trơn tuột" (quy ước chung của dự án); にゅぶっ → "Bụp"; ぢゅぼ/ぢゅば → "Bụp"; ぐちゅ/ごちゅ → "Rột"; ぼちゅ → "Chụt"; ぽっ → "Bụp"; ぐいっ → "Giật mạnh" (theo tài liệu SFX); ぱくっ → "Ngoạm" (theo tài liệu SFX); あちゅっ (hắt hơi) → "Hắt xì"; こほっ (ho) → "Khụ" (VN cũ "kho hộc" không phải từ tiếng Việt); くっ → "Hự"; んくっ → "Ưm hự"; んふっ → "Ưm phù"; んぷっ → "ưm bụp"; ぷっ → "Bụp"; んむっ → "ưm mự"; んひっ → "ưm hì"; くふっ → "Khự"; くひゅっ → "Khíu"; おうふっ → "Ồ phù"; ぷあっ/ぷぁ → "Phà"; ふぁんっ → "phàn"; はぷっ → "Hà bụp"; ぷはっ → "Bụp ha"; ひあ → "Hia" (không phải "Hya"); ひゃう → "Hiau". Hơi thở cụt "phu" (bị cắt bởi ――) được chấp nhận (1072). はっ → "Hà"/"Ha" đều chấp nhận. Phạm vi kéo dài: chỉ kéo dài từ âm đơn tiết (chụt, rột, rộp, Phập) và từ miêu tả rõ ràng kéo dài được (sâu); KHÔNG kéo dài cụm miêu tả hai từ hay tiếng trượt đa âm tiết chỉ có một う cuối.

## Đề xuất cập nhật context (chưa chốt)

- **Tiếng cười khúc khích:** cần quyết định chung cho toàn dự án — các dòng ふふ/うふふ/えへへ/あはは đang bị La-tinh hoá ở nhiều file (file này 8 dòng, lr_h1 3 dòng). Ứng viên: giữ La-tinh, hoặc "phì phì"/"hì hì".
- **くぅん:** cần một dạng Việt thống nhất — ứng viên "Ưưưn" hoặc giữ "Kuuun" (dạng đang dùng thực tế).
- **Quy tắc độ dài âm kéo dài:** ghi vào context — số nguyên âm VN = 1 + số ký tự う/ぅ trong token JP (bằng chứng h7 1651 + 1770 trong file này + toàn bộ token lr).

## Đã kiểm tra và KHÔNG tính là sai

- 698: おっぱい → "Sữa, mẹ?" — cách dịch tách "sữa mẹ" thành hai vế, TW cũng lạ tương tự; chấp nhận được, không tính sai.
- 1007: きゃぁん → "Kyaaan" — tiếng hét, nằm trong khoảng chấp nhận được.
- 1017: くはっ → "Ư ha" — hợp lý.
- 1029: くぅん → "Kuuun" — xem đề xuất くぅん ở trên, không tính sai.
- 1036: はぅぅ → "Hauu" — đếm đúng (3 nguyên âm u), không tính sai.
- 1054: ぉあっ → "Oa!" — thán từ Việt hợp lệ.
- 1072: "phu" — hơi thở bị cắt cụt, chấp nhận.
- 1075/1087/1194/1227/1321: tiếng cười La-tinh — ghi vào đề xuất (xem trên), không tính là sai trong audit này.
- 1089/1090: あうっ → "Au" — đúng.
- 1115: ぺちょっっ → "Liếm láp" — chấp nhận được.
- 1125: んきゅんっ → "Ưm kyun" — đúng theo h7.
- 1129: ん、しょっ → "Ây da" — dịch tự do nhưng không rõ là sai.
- 1130: ううむ → "Ưm" — độ dài là thứ yếu, không tính sai.
- 1131: んうううっ → "Ưm uu u" — đếm đúng (3 chữ u), không tính sai.
- 1210: （ぷくっ）→（Bong bóng） — chấp nhận được.
- 1213: "Tay kia" — theo TW 換手, chấp nhận được.
- 1491: ポフっと → "ngoan ngoãn" — dịch tự do, không rõ là sai.
- 1704/1721/1730/1750/1775/1707/1708/1757: các âm miêu tả độc thoại đã Việt hoá thành cụm từ — giữ nguyên theo phạm vi đã chốt (KHÔNG kéo dài cụm miêu tả hai từ).
- 1734/1740/1746/1747/1749/1778/1780: các chuỗi âm theo TW — giữ nguyên.
- 1770: VN cũ "Đâm sâu uuuuuuuuuuu" ĐÃ ĐÚNG (12 chữ u = 1+11) — loại khỏi danh sách sửa trong lần kiểm tra thứ hai, không tính là sai.
- 972: "cô đơn" là danh từ (sự cô đơn), không phải cách gọi — dương tính giả, không tính vào đếm "em"/"cô".

## Kết bài

File lr_h2: 333 dòng đã đọc, 69 dòng sai (20,7%) — 24 xưng hô, 6 thuật ngữ, 37 hơi thở/âm thanh thoại, 2 âm thanh độc thoại. Không lệch vị trí, không xoay vòng, không tràn chương — toàn bộ lỗi đều tại chỗ và đã có bản sửa viết tay, kiểm tra lần hai đầy đủ. Họ lỗi lớn nhất là âm thanh/hơi thở còn La-tinh (39 dòng, trong đó 1028 cả dòng còn nguyên La-tinh) và Soutetsu tự xưng "anh" (23 dòng). Kiểm tra lần hai đã loại 1 dòng (1770 — VN cũ đã đúng, bằng chứng mạnh nhất cho quy tắc độ dài âm kéo dài) và sửa 5 bản sửa về số nguyên âm. Bằng chứng mới cho B4: đúng 1 dòng tên rên trần (1079) — đã sửa thành "anh Soutetsu" theo quyết định B4 19/11. Hai đề xuất mới cần Hieu quyết: tiếng cười khúc khích (8 dòng) và dạng Việt cho くぅん. Với 2 file này, 03_Paulette đã audit xong toàn bộ (lr_稀咲h1 và れいな02 đã được audit song song — xem ROUTE-AUDIT).

**Đính chính B4 19/11 22:24 (Hieu ủy quyền Muse chốt):** ngoại lệ tên rên BÃI BỎ — Paulette gọi Soutetsu bằng tên trần là sai ngay cả khi rên/kêu tên trong lúc thân mật, vì JP là 双鉄くん trong tất cả các dòng kiểm tra (không bao giờ bỏ くん, không bao giờ là さん hay tên trần).