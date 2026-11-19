# Pilot sửa bản dịch — 00_Common file 01 (共通01_右田双鉄の帰還)

File gốc: `#U5171#U901a01_#U53f3#U7530#U53cc#U9244#U306e#U5e30#U9084.txt.toml` — Chương 1 Common Route, "Sự trở về của Migita Soutetsu".
File đã sửa đính kèm: cùng tên file, chỉ thay 35/155 dòng trong `[script]`. Toàn bộ `# JP:` comment, `[characters]`, `[character_subs]`, thẻ `%l`, BOM và CRLF giữ nguyên. File parse lại bằng TOML OK.

## 35 dòng đã sửa (trong tổng 155 dòng script)

### [992] — Định dạng
- **JP:** …………………………………………………………………… / ……………………………………………………………………
- **Cũ:** …………………………………………………………………… ……………………………………………………………………
- **Mới:** ……………………………………………………………………
……………………………………………………………………
- **Lý do:** Sai định dạng: bản Nhật ngắt dòng (\n) giữa hai hàng dấu chấm, bản Việt gộp thành một dòng có khoảng trắng.

### [996] — Dấu câu + xưng hô
- **JP:** …………なんで、こんなに眠いんだ―― / さっきまで、僕……寝てた、の、に…………
- **Cũ:** …………Tại sao, lại buồn ngủ thế này—— Rõ ràng, lúc nãy mình……vẫn còn đang……ngủ, cơ, mà…………
- **Mới:** …………Sao mà buồn ngủ thế này—— Rõ ràng lúc nãy tôi……vẫn còn đang……ngủ cơ mà…………
- **Lý do:** Dấu phẩy kiểu máy dịch trước "cơ, mà"; xưng hô Soutetsu thống nhất là "tôi" theo locations doc.

### [1000] — Sai nghĩa
- **JP:** ……ダメ、だ。 / 聞いてること、意味、わからない。
- **Cũ:** ……Không, được rồi. Những gì mình nghe thấy, chẳng, hiểu gì cả.
- **Mới:** ……Không ổn rồi. Những gì tôi nghe thấy, chẳng hiểu gì cả.
- **Lý do:** Sai nghĩa: ダメ、だ = "Không ổn rồi", không phải "Không, được rồi"; bỏ dấu phẩy thừa; "mình" → "tôi".

### [1004] — Dấu câu + xưng hô
- **JP:** ……出血、僕の、頭……から。 / なら、このまま――けど……………………
- **Cũ:** ……Chảy máu, từ……đầu, của mình. Vậy thì, cứ thế này——nhưng mà……………………
- **Mới:** ……Máu chảy từ……đầu tôi. Vậy thì, cứ thế này——nhưng mà……………………
- **Lý do:** Dấu phẩy kiểu máy dịch; "mình" → "tôi" theo locations doc.

### [1009] — Dấu câu
- **JP:** ……物との会話。 / あるいは、ただの独り言。
- **Cũ:** ……Trò chuyện với đồ vật. Hay có lẽ, chỉ là độc thoại.
- **Mới:** ……Trò chuyện với đồ vật. Hay có lẽ chỉ là độc thoại.
- **Lý do:** Bỏ dấu phẩy thừa sau "có lẽ".

### [1012] — Văn phong
- **JP:** ……声、誰かの声が聞こえる。 / ……感じる……手……誰かが、僕を……ゆすってる。
- **Cũ:** ……Tiếng nói, tôi nghe thấy tiếng ai đó. ……Cảm nhận được……bàn tay……ai đó, đang……lay tôi.
- **Mới:** ……Tôi nghe thấy tiếng ai đó. ……Cảm nhận được……bàn tay……ai đó đang……lay tôi.
- **Lý do:** Câu trùng lặp "Tiếng nói, tôi nghe thấy tiếng ai đó"; gọn lại, bỏ dấu phẩy thừa.

### [1023] — Sai nghĩa
- **JP:** 「\x%l制動;#00ffc040;制動%l;#;了解。この速度から\x%l非常;#00ffc040;非常%l;#;は無理――よね」
- **Cũ:** 「Đã rõ \x%l制動;#00ffc040;hãm phanh%l;#;. Với tốc độ này thì \x%l非常;#00ffc040;phanh khẩn cấp%l;#; là không thể——rồi.」
- **Mới:** 「Đã rõ, \x%l制動;#00ffc040;hãm phanh%l;#;. Với tốc độ này thì \x%l非常;#00ffc040;phanh khẩn cấp%l;#; là không thể——nhỉ.」
- **Lý do:** よね = "nhỉ", không phải "rồi"; thêm dấu phẩy sau "Đã rõ".

### [1041] — Sai nghĩa
- **JP:** 「……これ以上は\x%l滑走;#00ffc040;滑走%l;#;します。 / 限界です。制動力は足りません」
- **Cũ:** 「……Hơn nữa sẽ bị \x%l滑走;#00ffc040;trượt bánh%l;#; mất. Đến giới hạn rồi. Lực hãm phanh không đủ.」
- **Mới:** 「……Cứ thế này nữa sẽ bị \x%l滑走;#00ffc040;trượt bánh%l;#; mất. Đến giới hạn rồi. Lực hãm phanh không đủ.」
- **Lý do:** これ以上 = "cứ thế này nữa", không phải "hơn nữa".

### [1047] — Thì
- **JP:** 「……やむなしね。 / [しずおか,1]靜岡での\x%l接続;#00ffc040;接続%l;#;は遅らせたくなかったんだけど」
- **Cũ:** 「……Hết cách rồi. Tôi không muốn làm chậm trễ việc \x%l接続;#00ffc040;kết nối chuyển tàu%l;#; ở Shizuoka đâu.」
- **Mới:** 「……Hết cách rồi. Tôi đã không muốn làm chậm việc \x%l接続;#00ffc040;kết nối chuyển tàu%l;#; ở Shizuoka đâu.」
- **Lý do:** 遅らせたくなかった là ý muốn trong quá khứ: "đã không muốn làm chậm".

### [1160] — Sai nghĩa
- **JP:** 「いや、転覆だ！　\x%l脱線転覆;#00ffc040;脱線転覆%l;#;！！ / だが、全滅よりはよほどマシだっ！！」
- **Cũ:** 「Không, lật rồi! \x%l脱線転覆;#00ffc040;Trật bánh lật tàu%l;#;!! Nhưng thế này vẫn còn tốt chán so với bị diệt vong toàn bộ!!」
- **Mới:** 「Không, là lật tàu! \x%l脱線転覆;#00ffc040;Trật bánh lật tàu%l;#;!! Nhưng thế này vẫn còn tốt hơn nhiều so với tất cả cùng chết!!」
- **Lý do:** 転覆だ = "là lật tàu"; 全滅 = "tất cả cùng chết", không phải "bị diệt vong toàn bộ".

### [1166] — Văn phong
- **JP:** 「お客様、ご着席大丈夫でしょうか」
- **Cũ:** 「Hành khách, không biết đã ngồi vững hết chưa.」
- **Mới:** 「Quý khách đã ngồi vào chỗ ổn cả chưa ạ.」
- **Lý do:** お客様 → "Quý khách" cho đúng kính ngữ; câu cũ lủng củng.

### [1168] — Văn phong
- **JP:** 「そうだな、着水前に一度上から見ておこう」
- **Cũ:** 「Cũng được, trước khi hạ cánh xuống nước thì nhìn từ trên cao một chút vậy.」
- **Mới:** 「Ừ, trước khi hạ cánh xuống nước thì nhìn từ trên cao một lượt vậy.」
- **Lý do:** そうだな = "Ừ", không phải "Cũng được".

### [1173] — Thêm từ + câu cụt
- **JP:** 「\x%l車掌;#00ffc040;車掌%l;#;・[せき]関、\x%l車販;#00ffc040;車販%l;#;・[まゆずみ]黛のコンビでしょ？ / やってるわ。きちんと、彼女たちの仕事を」
- **Cũ:** 「Hôm nay là bộ đôi \x%l車掌;#00ffc040;trưởng tàu%l;#; Seki và \x%l車販;#00ffc040;nhân viên bán hàng%l;#; Mayuzumi mà nhỉ? Họ đang làm đấy. Chắc chắn họ sẽ hoàn thành tốt công việc của mình.」
- **Mới:** 「Là bộ đôi \x%l車掌;#00ffc040;trưởng tàu%l;#; Seki và \x%l車販;#00ffc040;nhân viên bán hàng%l;#; Mayuzumi mà nhỉ? Họ đang làm việc đấy. Cứ để họ làm công việc của mình cho tử tế.」
- **Lý do:** Bỏ "Hôm nay" (không có trong gốc); câu cuối là câu cụt trong gốc (きちんと、彼女たちの仕事を) nên dịch theo ngữ pháp, cần Hieu check ngữ cảnh.

### [1185] — Sai nghĩa
- **JP:** 「やってやるわよ。一世一代の仕事をね！」
- **Cũ:** 「Làm thôi. Đánh cược cả đời vào lần này!」
- **Mới:** 「Làm thôi! Đây là công việc cả đời mới có một lần đấy!」
- **Lý do:** 一世一代 = "cả đời mới có một lần", không phải "đánh cược cả đời".

### [1217] — Dấu câu
- **JP:** 「停止、以外――。 / でしたら、逆に！」
- **Cũ:** 「Ngoài việc, dừng lại——. Nếu vậy thì, làm ngược lại!」
- **Mới:** 「Ngoài việc dừng lại ra——. Vậy thì, làm ngược lại!」
- **Lý do:** Bỏ dấu phẩy thừa; 停止以外 = "ngoài việc dừng lại ra".

### [1260] — Sai nghĩa
- **JP:** 「矛盾の判断には大きな演算能力を必要とし、 / その負荷が双鉄様の安全を脅かすという……双鉄様？」
- **Cũ:** 「Việc đưa ra quyết định trong sự mâu thuẫn đòi hỏi năng lực tính toán lớn, và khối lượng công việc đó sẽ đe dọa đến sự an toàn của ngài Soutetsu…… Ngài Soutetsu?」
- **Mới:** 「Việc phán đoán trong mâu thuẫn đòi hỏi năng lực tính toán rất lớn, và gánh nặng đó sẽ đe dọa sự an toàn của ngài Soutetsu…… Ngài Soutetsu?」
- **Lý do:** 負荷 = "gánh nặng", không phải "khối lượng công việc"; 判断 = "phán đoán".

### [1262] — Thêm từ
- **JP:** 「ここだ！　落ちてない！　落ちてないぞっ！」
- **Cũ:** 「Ở đây! Không bị rơi! Không bị rơi xuống sông!」
- **Mới:** 「Ở đây! Không rơi! Không rơi đâu!」
- **Lý do:** Bỏ "xuống sông" (không có trong gốc); 落ちてない = "không rơi đâu".

### [1308] — Sai nghĩa
- **JP:** 「お前のように優秀なナビを、 / 敵に回したくはないからな」
- **Cũ:** 「Bởi vì tôi không muốn đối đầu với một hệ thống dẫn đường xuất sắc như cô đâu.」
- **Mới:** 「Vì tôi chẳng muốn biến một Navi xuất sắc như cô thành kẻ địch đâu.」
- **Lý do:** 敵に回したくない = "không muốn biến thành kẻ địch", không phải "không muốn đối đầu với hệ thống dẫn đường".

### [1329] — Văn phong
- **JP:** 「はい。ご息女です。 / しかし、行政手腕は遺伝しなかったとの評判です」
- **Cũ:** 「Vâng. Là con gái của ngài ấy. Tuy nhiên, có nhiều đánh giá cho rằng năng lực hành chính không được di truyền.」
- **Mới:** 「Vâng. Là con gái của ngài ấy. Nhưng nghe nói năng lực hành chính thì không được di truyền.」
- **Lý do:** 評判 = "nghe nói", gọn câu.

### [1335] — Văn phong
- **JP:** 「状況未確定の事故報告。\x%l発報;#00ffc040;発報%l;#;は[キュウロクヨンニイ,3]9642\x%lレイルロオド;#00ffc040;レイルロオド%l;#;。 / \x%l帝鉄貨物;#00ffc040;帝鉄貨物%l;#;。十五両\x%l編成;#00ffc040;編成%l;#;。全車両喪失の可能性あり」
- **Cũ:** 「Báo cáo sự cố tình trạng chưa xác định. \x%l発報;#00ffc040;Phát tín hiệu báo động%l;#; từ \x%lレイルロオド;#00ffc040;Railord%l;#; 9642. \x%l帝鉄貨物;#00ffc040;Vận tải hàng hóa Đường sắt Hoàng gia%l;#;. \x%l編成;#00ffc040;Đoàn tàu%l;#; mười lăm toa. Có khả năng toàn bộ toa xe đã bị tổn thất.」
- **Mới:** 「Báo cáo sự cố tình trạng chưa xác định. \x%l発報;#00ffc040;Phát tín hiệu báo động%l;#; từ \x%lレイルロオド;#00ffc040;Railord%l;#; 9642. \x%l帝鉄貨物;#00ffc040;Vận tải hàng hóa Đường sắt Hoàng gia%l;#;. \x%l編成;#00ffc040;Đoàn tàu%l;#; mười lăm toa. Có khả năng mất toàn bộ toa xe.」
- **Lý do:** 全車両喪失 = "mất toàn bộ toa xe", gọn hơn "đã bị tổn thất".

### [1337] — Sót nghĩa
- **JP:** 「当機に停止の手段無し。\x%l制動;#00ffc040;制動%l;#;力を最大限適正にとっても……七五秒後、止まりきれずに――」
- **Cũ:** 「Chuyến tàu này đã không còn cách dừng lại. Dù có dùng lực \x%l制動;#00ffc040;hãm phanh%l;#; tối đa đi chăng nữa…… thì 75 giây sau, cũng không thể dừng hẳn lại mà——」
- **Mới:** 「Chuyến tàu này đã không còn cách dừng lại. Dù có dùng lực \x%l制動;#00ffc040;hãm phanh%l;#; tối đa một cách hợp lý nhất…… 75 giây sau, cũng không dừng hẳn được mà——」
- **Lý do:** 適正に = "một cách hợp lý nhất" (bị bỏ sót); 止まりきれず = "không dừng hẳn được".

### [1397] — Dấu câu
- **JP:** 「そうですね。 / わたくしたちも、わたくしたちの」
- **Cũ:** 「Nói cũng phải. Chúng ta cũng phải, làm tốt công việc của chúng ta.」
- **Mới:** 「Nói cũng phải. Chúng ta cũng phải làm tốt công việc của mình.」
- **Lý do:** Bỏ dấu phẩy thừa; câu gốc bị cụt nên hoàn thiện tối thiểu.

### [1398] — Sai nghĩa
- **JP:** 「報告なさい。何の方法？　報告が一秒遅れるだけで、 / 危険が何メートル近づくかわかってるでしょうに」
- **Cũ:** 「Báo cáo đi. Hết cách gì? Báo cáo chậm một giây thôi là nguy hiểm sẽ tiến gần thêm bao nhiêu mét, cô biết rõ mà.」
- **Mới:** 「Báo cáo đi. Phương pháp gì cơ? Báo cáo chậm một giây thôi là nguy hiểm tiến gần thêm bao nhiêu mét, cô biết rõ mà.」
- **Lý do:** 何の方法？ = "Phương pháp gì cơ?", không phải "Hết cách gì?".

### [1404] — Sai nghĩa
- **JP:** 「お客様乗せてんのよ、無理でも止めるっ！！ / 再減速！　そっち主導で！！」
- **Cũ:** 「Trên tàu vẫn còn hành khách, không thể cũng phải dừng lại!! Tiếp tục giảm tốc! Cô làm chủ đạo đi!!」
- **Mới:** 「Trên tàu còn có hành khách đấy, dù không thể cũng phải dừng lại!! Giảm tốc lại! Cô chủ đạo đi!!」
- **Lý do:** 再減速 = "giảm tốc lại", không phải "tiếp tục giảm tốc"; gọn câu.

### [1430] — Sai nghĩa
- **JP:** 「再減速了解。\x%l圧;#00ffc040;[あつ,4]ブレーキ力%l;#;、強めます――っ！」
- **Cũ:** 「Đã rõ tiếp tục giảm tốc. \x%l圧;#00ffc040;Áp suất%l;#; hãm phanh, tăng cường——っ!」
- **Mới:** 「Đã rõ, giảm tốc lại. \x%l圧;#00ffc040;Áp suất%l;#; hãm phanh, tăng thêm——っ!」
- **Lý do:** 再減速了解 = "Đã rõ, giảm tốc lại"; 強めます = "tăng thêm".

### [1434] — Thêm từ
- **JP:** 「ならどうしろとっ！！」
- **Cũ:** 「Vậy cậu bảo phải làm sao!!」
- **Mới:** 「Vậy thì phải làm sao đây!!」
- **Lý do:** どうしろと = "phải làm sao đây", bỏ "cậu bảo" (không có trong gốc).

### [1438] — Thêm từ
- **JP:** 「だったら他っ！　停止以外の方策をっ！ / 手段は問わない！　目標は転落回避っ！！！」
- **Cũ:** 「Thế thì cách khác! Tìm cách khác ngoài việc dừng tàu đi! Cách gì cũng được! Mục tiêu là tránh rơi xuống sông!!!」
- **Mới:** 「Thế thì cách khác! Tìm cách khác ngoài việc dừng tàu đi! Cách gì cũng được! Mục tiêu là tránh bị rơi xuống!!!」
- **Lý do:** 転落回避 = "tránh bị rơi xuống", bỏ "xuống sông" (không có trong gốc).

### [1440] — Dấu câu
- **JP:** 「もちろんです！　 / ですが――、一刻も早く病院につれていかないとっ」
- **Cũ:** 「Tất nhiên rồi! Nhưng mà——, phải đưa đến bệnh viện càng sớm càng tốt.」
- **Mới:** 「Tất nhiên rồi! Nhưng mà——phải đưa đến bệnh viện càng sớm càng tốt.」
- **Lý do:** Bỏ dấu phẩy thừa sau "——".

### [1450] — Khó hiểu
- **JP:** 「[ひない,1]雛衣というと、前の市長の？」
- **Cũ:** 「Hinai à, là của thị trưởng tiền nhiệm sao?」
- **Mới:** 「Hinai à, là con gái thị trưởng tiền nhiệm sao?」
- **Lý do:** 前の市長の雛衣 = "con gái thị trưởng tiền nhiệm", câu cũ gây khó hiểu.

### [1457] — Thừa từ
- **JP:** 「9642\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は『鉄橋崩落』と――断末魔の\x%l共感;#00ffc040;共感%l;#;で。 / ……[ふじがわ,2]冨士川[きょうりょう,1]橋梁が崩落したと」
- **Cũ:** 「\x%lレイルロオド;#00ffc040;Railord%l;#; 9642 truyền đạt qua \x%l共感;#00ffc040;cộng cảm%l;#; lúc hấp hối rằng 『Cầu sắt sập』. ……Nội dung là cầu sắt Fujikawa đã sập.」
- **Mới:** 「\x%lレイルロオド;#00ffc040;Railord%l;#; 9642 truyền đạt qua \x%l共感;#00ffc040;cộng cảm%l;#; lúc hấp hối rằng 『Cầu sắt sập』. ……Cầu sắt Fujikawa đã sập.」
- **Lý do:** Bỏ "Nội dung là" thừa (đã có "truyền đạt rằng" ở đầu câu).

### [1601] — Sai nghĩa
- **JP:** 機体姿勢を即座に戻し、けれど航路は変更しない。
- **Cũ:** Ngay lập tức điều chỉnh lại tư thế máy bay, nhưng không thay đổi đường bay.
- **Mới:** Ngay lập tức lấy lại tư thế thân máy, nhưng không thay đổi đường bay.
- **Lý do:** 機体姿勢を戻し = "lấy lại tư thế thân máy", không phải "điều chỉnh lại tư thế máy bay".

### [1628] — Dấu câu
- **JP:** そうして、[おひとよ,2]御一夜―― / 眼下に広がるこの町も、僕を間違いなく救ってくれた。
- **Cũ:** Và lúc này, Ohimitera—— thành phố trải dài dưới tầm mắt kia, cũng đã từng cứu rỗi tôi.
- **Mới:** Và lúc này, Ohimitera——thành phố trải dài dưới tầm mắt kia, cũng đã từng cứu rỗi tôi.
- **Lý do:** Bỏ khoảng trắng thừa sau "——".

### [1637] — Thuật ngữ
- **JP:** ナビという物品。\x%lエアクラ;#00ffc040;エアクラ%l;#;・ナビ。 / \x%lエアクラ;#00ffc040;エアクラ%l;#;とともに急発展し、一般にまで普及した擬似知能。
- **Cũ:** Vật phẩm mang tên Navi. \x%lエアクラ;#00ffc040;Aircra%l;#; Navi. Trí tuệ nhân tạo phát triển nhanh chóng cùng với \x%lエアクラ;#00ffc040;Aircra%l;#;, và đã trở nên phổ biến trong đại chúng.
- **Mới:** Vật phẩm mang tên Navi. \x%lエアクラ;#00ffc040;Aircra%l;#; Navi. Trí tuệ giả lập phát triển nhanh chóng cùng với \x%lエアクラ;#00ffc040;Aircra%l;#;, và đã trở nên phổ biến trong đại chúng.
- **Lý do:** 擬似知能 = "trí tuệ giả lập", không phải "trí tuệ nhân tạo".

### [1647] — Xưng hô
- **JP:** なら、僕……生きてる…… / 僕だけ……僕の、はんぶんは――
- **Cũ:** Vậy ra, mình……vẫn còn sống…… Chỉ có mình……còn, một nửa của mình——
- **Mới:** Vậy ra, tôi……vẫn còn sống…… Chỉ có tôi……một nửa của tôi——
- **Lý do:** "mình" → "tôi" theo locations doc; bỏ dấu phẩy thừa.

### [1652] — Xưng hô
- **JP:** それじゃあ、みちが―― / 僕を、突き飛ばしてくれた[いもうと,1]路子が――
- **Cũ:** Như thế thì, Michi—— Michiko, đứa em gái đã đẩy mình ra sẽ——
- **Mới:** Thế thì, Michi——Michiko, đứa em gái đã đẩy tôi ra, sẽ——
- **Lý do:** "mình" → "tôi" theo locations doc; gọn dấu câu.

## Các lỗi mẫu rút ra (áp dụng cho cả 95.838 dòng còn lại)

1. **Dấu phẩy kiểu máy dịch:** dấu phẩy chèn trước "cơ, mà", "chẳng, hiểu", "có lẽ," — gặp ở 996, 1000, 1004, 1009, 1217, 1397, 1440. Quét toàn dự án bằng pattern `, (cơ|mà|chẳng|nữa|thôi|đâu|rồi|nhỉ)` sẽ bắt được nhiều.
2. **Xưng hô Soutetsu không nhất quán:** trong cùng một đoạn độc thoại, lúc "mình" (996, 1000, 1004, 1647, 1652) lúc "tôi" (1012). Theo `locations_and_characters.md` §2.1, Soutetsu xưng **"Tôi"** — pilot đã thống nhất về "Tôi".
3. **Thêm từ không có trong gốc:** "xuống sông" (1262, 1438), "Hôm nay" (1173), "cậu bảo" (1434), "Nội dung là" (1457).
4. **Sai nghĩa từ đơn:** ダメ (1000), これ以上 (1041), 全滅 (1160), 一世一代 (1185), 何の方法 (1398), 敵に回す (1308), 擬似知能 (1637), 機体姿勢 (1601).
5. **Sót nghĩa:** 適正に trong 1337 bị bỏ qua.

## Đã giữ nguyên theo đúng docs Hieu gửi (không sửa)

- **Aircra** (エアクラ): giữ nguyên cả trong text lẫn gloss `%l` — là thuật ngữ chuẩn của dự án, xuất hiện 405 lần, docs dùng xuyên suốt.
- **Migita System** (1170, 1634): giữ theo `locations_and_characters.md` §2.6 — Mayami điều hành "nhà máy rượu Migita System". "Migita Ichi" là tên loại rượu shochu, không phải tên xưởng.
- **Đường sắt Hoàng gia (Teitetsu)** (1335): theo `locations_and_characters.md` §1 — 帝鉄 = Đường sắt Hoàng gia (Teitetsu).
- **"Phun cát dồn toa"** (1027): giữ y nguyên vì chính ví dụ mẫu trong `ai_translation_prompt.md` dùng câu này — xem câu hỏi (1) bên dưới.
- **"——っ" cuối câu** (1247, 1317, 1375, 1382, 1430): giữ theo `sfx_and_emoticons.md` §3 — tài liệu cho phép giữ "——っ".
- **"Tu! Tuuu!…"** (1668): giữ theo `sfx_and_emoticons.md` §1.1 — còi tàu có hai phương án Uúú… / Tuúú…, bản dịch đang dùng phương án Tuúú… là đúng chuẩn.
- **"A Di Đà Phật!!!"** (1443): giữ — bản địa hoá cho 南無三 (tiếng niệm Phật lúc hoảng hốt).
- **Cộng cảm** (共感): giữ theo `chapter_context.md` — "Cộng cảm (Sympathy)".

## Câu hỏi cần Hieu chốt (ảnh hưởng toàn dự án, không chỉ pilot)

1. **"dồn toa" trong "phun cát dồn toa" (1027):** từ này không có trong gốc Nhật (砂撒きを進言します) lẫn bản Trung (建議放沙), nhưng chính ví dụ mẫu trong `ai_translation_prompt.md` của Hieu lại dùng "Kiến nghị phun cát dồn toa". Giữ như hiện tại, hay bỏ "dồn toa" → "Kiến nghị phun cát."?
2. **Gloss của 帝鉄 không nhất quán toàn dự án:** 57 chỗ giữ nguyên "帝鉄", 50 chỗ "Đường sắt Hoàng gia", 7 chỗ "Teitetsu", 2 chỗ "Đường sắt Hoàng gia (Teitetsu)". Chốt một dạng cho cả 95.838 dòng? (Khuyến nghị: "Đường sắt Hoàng gia (Teitetsu)" lần đầu, "Đường sắt Hoàng gia" sau đó — hoặc giữ "Teitetsu" như tên riêng vì nhân vật đã dùng "Nhân viên Teitetsu".)
3. **Câu 1173 bị cụt trong gốc:** 「きちんと、彼女たちの仕事を」 — không có động từ, pilot dịch tạm là "Cứ để họ làm công việc của mình cho tử tế." Hieu check ngữ cảnh trong game giúp: ai đang nói với ai ở đây?
4. **Soutetsu xưng "Tôi" hay "mình" trong độc thoại?** Docs của Hieu nói "Tôi" (locations §2.1) nên pilot thống nhất "Tôi". Nếu Hieu muốn độc thoại thân mật hơn bằng "mình" thì đổi lại toàn bộ — chỉ cần nói một câu.
5. **Route tiếp theo:** sau pilot này, Hieu muốn sửa route nào trước — route nào Hieu thấy tệ nhất? (Common còn 15 file, Hachiroku 46 file là nhiều nhất.)

## Audit file zip mới (translation_toml-2.zip)

- Vẫn 227 file, đúng số lượng từng route như README (16/46/37/37/13/12/13/28/5/11/8/1).
- Tổng 95.838 entries (characters + subs + script); riêng script: 93.159 dòng.
- **Bản Việt trong zip mới giống hệt 100% bản Việt trong zip cũ** (0 dòng khác nhau) — zip mới chỉ bổ sung thêm dòng `# JP:` (câu gốc tiếng Nhật) trước mỗi dòng dịch.
- Độ phủ `# JP:`: 93.153/93.159 dòng script (100%). 6 dòng thiếu `# JP:` đều là lựa chọn trong menu (Common file 16: 3 dòng "Tham khảo ý kiến của…"; Nagi_Fukami file 07: 3 dòng tên nhân vật) — không phải lỗi.
- Nhờ có `# JP:` mà từ giờ sửa được đối chiếu trực tiếp từng câu, không còn phải đoán nghĩa.
