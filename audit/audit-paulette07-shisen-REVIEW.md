# Audit: Paulette 07_支線 — 25 dòng Việt sai (đã đối chiếu JP + TW)

**Kết quả: 25/358 dòng sai (7,0%)** — 0 lệch vị trí, 0 chưa dịch, 0 cụt câu, 0 chưa chắc chắn. File sạch về cấu trúc, nhưng là file nặng nhất về xưng hô từ trước tới nay theo một nghĩa đặc biệt: **17/17 lần Soutetsu tự xưng trong thoại đều là "anh", 0 lần "tôi"** — tức là người dịch đã chọn "anh" một cách hệ thống cho cả file, trái với docs. Đây là file Paulette 07 thứ hai (cảnh khảo sát lại tuyến nhánh/bỏ hoang với ông Minokasa, Reina, Paulette; Soutetsu suy ngẫm về chuyện làm cha).

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 358 dòng script** (thoại 207, lời dẫn 151) đối chiếu JP + TW từ CSV "Trang tính 3", target là TOML-2. TW chỉ là nhân chứng thứ hai; chỗ nào JP và TW mâu thuẫn thì theo JP (quy tắc Hieu đặt 19/11).
- Heuristic thoại↔lời dẫn báo **0 dòng** — bắt được 0/25. Toàn bộ lỗi đều là cùng-loại (xưng hô, thuật ngữ) nên heuristic không thấy được; đây là bằng chứng mạnh nhất từ trước tới nay rằng heuristic chỉ là cận dưới.
- Không có key-shift sạch (shift −5..+5 đều ~1,000 vì key thưa — không có ý nghĩa, không áp dụng).
- TOML và CSV giống hệt nhau về nội dung (220 dòng khác chỉ ở `\n`/khoảng trắng, 0 khác nội dung). Không có dòng CSV trống nào; VN==TW 1 dòng duy nhất là 1265 「……」 (chỉ dấu câu, đúng, không tính lỗi).
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Thẻ `%l`: 45 dòng có thẻ, không dòng nào lệch thẻ (1664 giữ nguyên thẻ, chỉ đổi gloss).
- Phân loại lỗi: xưng hô 17 dòng, thuật ngữ 8 dòng (1952 mang cả hai lỗi nên tổng số dòng là 25, không phải 26). Theo người nói: Soutetsu 18, Reina 2, Minokasa 2, Paulette 1, lời dẫn 2; Nagi 0. Lỗi tập trung ở nửa đầu file (19/25 dòng nằm ở key < 2015).
- Về "mình" trong độc thoại: file có 8 dòng lời dẫn chứa "mình", tất cả đều đúng (sở hữu cách phản thân: "sự yếu đuối của mình" 2439, "cảm xúc của mình" 2648; thành ngữ "giật mình" 2406, "chỉ mình tôi" 2528, "tự mình" 2519; "mình" = "chúng ta" 2525; "mình" thuộc về Paulette 2412) — không tính sai dòng nào.

## Kết luận về cơ chế lỗi

Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương, không có trùng lặp nội bộ sai — đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục). Cơ chế lỗi ở đây khác hẳn các file "rối": không phải lỗi dán nhầm dòng, mà là **hai lựa chọn dịch hệ thống của người dịch, trái với docs**:

1. **Soutetsu xưng "anh" trong toàn bộ file** (17/17 lần, 0 lần "tôi") — trong khi docs locations §2.1 ghi rõ Soutetsu xưng "Tôi" ("Anh" chỉ khi nói với Hibiki), và trong file này Hibiki không xuất hiện lần nào. Cả 17 dòng đều phải đổi "anh" → "tôi" (1963 "bọn anh" → "bọn tôi"). Lưu ý: "mình" trong mệnh đề phụ ("chuyện mình có muốn…", "mình đang ép em…", "đằng nào mình cũng sẽ chết") được GIỮ NGUYÊN theo tiền lệ Hachiroku 12 — đó là dạng "Tôi… mình…" chuẩn trong mệnh đề phụ, không phải lỗi.
2. **御一夜 dịch "Ohimitera" trong toàn bộ file** (8/8 lần, 0 lần "Ohitoyo") — trái quyết định 19/11. Cả 8 dòng đều phải đổi sang "Ohitoyo".

Ngoài ra 1 dòng thuật ngữ riêng: 1664 整備体 → "thân chính" (gộp chung với 運転ボディ — xem mục đề xuất cập nhật context).

## Chi tiết 25 dòng sai

### A. Xưng hô — Soutetsu tự xưng "anh" thay vì "Tôi" (17 dòng)

**1528 [双鉄]** — Soutetsu tự xưng "anh"; docs: "Tôi" ("Anh" chỉ với Hibiki). Trong file này Soutetsu KHÔNG có lần nào xưng "tôi" trong thoại — 17/17 lần tự xưng đều là "anh", tức là cách dịch hệ thống của file, trái docs.

- JP: 「けれど今は……なってみたいと感じる気持ちもある。\nそれと同時に、とても怖いという気持ちも」
- TW: 「不過現在……我也有點想嘗試的心情。但與此同時又感到很害怕」
- Cũ: 「Nhưng bây giờ…… anh cũng có cảm giác muốn thử trở thành một người cha.\nVà đồng thời, cũng có cảm giác rất sợ hãi nữa」
- Sửa: 「Nhưng bây giờ…… tôi cũng có cảm giác muốn thử trở thành một người cha. Và đồng thời, cũng có cảm giác rất sợ hãi nữa」

**1638 [双鉄]** — Soutetsu tự xưng "Anh" với Paulette; docs: "Tôi".

- JP: 「ああ、すまん。\n僕は――これより他に褒めようを知らぬ」
- TW: 「啊，抱歉。我——只會用這種方式表達誇讚」
- Cũ: 「À, xin lỗi.\nAnh——chẳng biết cách khen ngợi nào khác ngoài cách này」
- Sửa: 「À, xin lỗi. Tôi——chẳng biết cách khen ngợi nào khác ngoài cách này」

**1668 [双鉄]** — Soutetsu tự xưng "anh"; docs: "Tôi".

- JP: 「――発電所を見た時も思ったのだが」
- TW: 「在找到發電廠的時候，我也有這種感覺」
- Cũ: 「——Lúc nhìn thấy nhà máy điện anh cũng đã nghĩ thế này」
- Sửa: 「——Lúc nhìn thấy nhà máy điện tôi cũng đã nghĩ thế này」

**1733 [双鉄]** — Soutetsu tự xưng "anh"; docs: "Tôi". "một nửa của mình" giữ nguyên — sở hữu cách phản thân, đúng tiếng Việt (tiền lệ Hachiroku 12).

- JP: 「事故を、僕は経験して。自分のふたごを――\n半身を亡くしてしまっているから」
- TW: 「我曾經在那場事故中，失去了雙胞胎妹妹——也就是自己的另一半」
- Cũ: 「Vì anh đã trải qua vụ tai nạn đó. Và mất đi người em sinh đôi——\nmất đi một nửa của mình」
- Sửa: 「Vì tôi đã trải qua vụ tai nạn đó. Và mất đi người em sinh đôi——mất đi một nửa của mình」

**1736 [双鉄]** — Soutetsu tự xưng "anh"; docs: "Tôi". "mình" trong mệnh đề phụ ("chuyện mình có muốn…") giữ nguyên — dạng "Tôi… mình…" trong mệnh đề phụ là chuẩn (tiền lệ Hachiroku 12).

- JP: 「僕は今まで――、一度たりとも、\n父になりたいかどうかなど、考えたこともなかった」
- TW: 「我至今為止，還沒考慮過要不要當爸爸這個問題」
- Cũ: 「Từ trước đến nay——, chưa một lần nào,\nanh nghĩ đến chuyện mình có muốn làm cha hay không」
- Sửa: 「Từ trước đến nay——, chưa một lần nào, tôi nghĩ đến chuyện mình có muốn làm cha hay không」

**1742 [双鉄]** — Soutetsu tự xưng "Anh" 2 lần; docs: "Tôi". "mình" trong mệnh đề phụ giữ nguyên (xem 1736).

- JP: 「だから、ときおり不安になるのだ。\n無理を、させすぎているのではないかと思ってしまう」
- TW: 「所以我有時候會感覺是不是在勉強你，這讓我非常不安」
- Cũ: 「Thế nên, thỉnh thoảng anh lại thấy bất an.\nAnh cứ nghĩ có phải mình đang ép em làm việc quá sức hay không」
- Sửa: 「Thế nên, thỉnh thoảng tôi lại thấy bất an. Tôi cứ nghĩ có phải mình đang ép em làm việc quá sức hay không」

**1743 [双鉄]** — Soutetsu tự xưng "anh" 2 lần; docs: "Tôi". "mình" trong mệnh đề phụ giữ nguyên (xem 1736).

- JP: 「だから自分もいつか死ぬと、それまでの生と考えて。\n父となる、子をなすことなど、想像もしていなかった」
- TW: 「所以我認為自己此刻生存在世，只是為了迎接將來某一天的死亡。生兒女、為人父這樣的事，我從來沒考慮過」
- Cũ: 「Nên anh cứ nghĩ rằng đằng nào mình cũng sẽ chết, và sống chỉ để chờ đến lúc đó.\nAnh chưa từng tưởng tượng đến việc trở thành một người cha, hay sinh con đẻ cái」
- Sửa: 「Nên tôi cứ nghĩ rằng đằng nào mình cũng sẽ chết, và sống chỉ để chờ đến lúc đó. Tôi chưa từng tưởng tượng đến việc trở thành một người cha, hay sinh con đẻ cái」

**1797 [双鉄]** — Soutetsu tự xưng "Anh" giữa câu ("Anh có cảm giác"); docs: "Tôi". Dễ sót vì không đứng đầu câu.

- JP: 「そうだな。今考えてみれば、坑道自体も同じかもしれん。\n設備のほとんどは、そのまま残されていたような気が」
- TW: 「是啊。現在想想，礦洞裡也是一樣。感覺裡面的設備都被好好原樣保存著」
- Cũ: 「Đúng vậy. Giờ nghĩ lại, bản thân hầm mỏ có lẽ cũng thế.\nAnh có cảm giác hầu hết các thiết bị đều được giữ nguyên như vậy」
- Sửa: 「Đúng vậy. Giờ nghĩ lại, bản thân hầm mỏ có lẽ cũng thế. Tôi có cảm giác hầu hết các thiết bị đều được giữ nguyên như vậy」

**1872 [双鉄]** — Soutetsu tự xưng "Anh"; docs: "Tôi".

- JP: 「ポーレットは、本当にすごいと思う。\n視野の広さも、怠らず手当をすることも」
- TW: 「波萊特真的很厲害。不僅視野寬廣，工作上還這麼勤奮」
- Cũ: 「Anh thấy Paulette thực sự rất tuyệt vời.\nCả về tầm nhìn rộng mở, lẫn sự chăm lo không hề chểnh mảng」
- Sửa: 「Tôi thấy Paulette thực sự rất tuyệt vời. Cả về tầm nhìn rộng mở, lẫn sự chăm lo không hề chểnh mảng」

**1892 [双鉄]** — Soutetsu tự xưng "anh"; docs: "Tôi".

- JP: 「発電所の状態も思っていたよりずっと良かった。\nあれならあるいは、再稼働さえ可能であるかもしれん」
- TW: 「發電廠的情況也比預想的要好得多。甚至說不定能將它再次啟動」
- Cũ: 「Tình trạng của nhà máy điện cũng tốt hơn anh nghĩ nhiều.\nNhư thế thì có khi còn có thể tái khởi động lại được ấy chứ」
- Sửa: 「Tình trạng của nhà máy điện cũng tốt hơn tôi nghĩ nhiều. Như thế thì có khi còn có thể tái khởi động lại được ấy chứ」

**1929 [双鉄]** — Soutetsu tự xưng "anh"; docs: "Tôi".

- JP: 「蓑笠さんなら、きっとその方面にもツテがあろう。\n出来れば、ご紹介を願いたいものだな」
- TW: 「蓑笠爺爺應該有這方面的人脈。希望他能幫我們介紹一下」
- Cũ: 「Nếu là ông Minokasa thì chắc chắn sẽ có mối quan hệ trong lĩnh vực đó.\nNếu được, anh rất muốn nhờ ông ấy giới thiệu」
- Sửa: 「Nếu là ông Minokasa thì chắc chắn sẽ có mối quan hệ trong lĩnh vực đó. Nếu được, tôi rất muốn nhờ ông ấy giới thiệu」

**1935 [双鉄]** — Soutetsu tự xưng "anh" khi nói với Reina; docs: "Tôi" ("Anh" chỉ với Hibiki).

- JP: 「抱っこはどうだ？　必要ならば、言ってくれ」
- TW: 「要我抱你嗎？如果需要的話儘管開口」
- Cũ: 「Có cần anh bế không? Nếu cần thì cứ nói nhé」
- Sửa: 「Có cần tôi bế không? Nếu cần thì cứ nói nhé」

**1945 [双鉄]** — Soutetsu tự xưng "anh" 3 lần; docs: "Tôi".

- JP: 「苦しいことがあるなら、僕に聞かせて欲しい。\n僕は、ポーレットを支えたい」
- TW: 「要是有什麼痛苦，就告訴我。我想成為波萊特你的依靠」
- Cũ: 「Nếu có chuyện gì đau khổ, anh muốn em hãy nói cho anh nghe.\nAnh muốn được trở thành chỗ dựa cho Paulette」
- Sửa: 「Nếu có chuyện gì đau khổ, tôi muốn em hãy nói cho tôi nghe. Tôi muốn được trở thành chỗ dựa cho Paulette」

**1952 [双鉄]** — Hai lỗi trong một dòng: Soutetsu tự xưng "Anh" → "Tôi" (docs), và 御一夜 "Ohimitera" → "Ohitoyo" (quyết định 19/11).

- JP: 「設計が出来たとして、作る方は？\n御一夜で出来れば一番良いと思うのだが」
- TW: 「設計好了之後，要在哪裡製作呢？最好是能在御一夜當地製作」
- Cũ: 「Cho là có thiết kế rồi, vậy còn người làm thì sao?\nAnh nghĩ tốt nhất là nên làm ở Ohimitera」
- Sửa: 「Cho là có thiết kế rồi, vậy còn người làm thì sao? Tôi nghĩ tốt nhất là nên làm ở Ohitoyo」

**1963 [双鉄]** — Soutetsu tự xưng "bọn anh" (số nhiều, nói thay cả nhóm); docs: "Tôi" → "bọn tôi".

- JP: 「うっかりしたのは僕らのほうだ」
- TW: 「走神的是我們才對」
- Cũ: 「Bất cẩn là bọn anh mới đúng」
- Sửa: 「Bất cẩn là bọn tôi mới đúng」

**2002 [双鉄]** — Soutetsu tự xưng "anh" với Paulette; docs: "Tôi".

- JP: 「ならば、疲れたら言ってくれ。ポーレットには、\n議会も社長業もあるのだからな」
- TW: 「那如果累了就說一聲。畢竟你還有市長和社長的工作」
- Cũ: 「Vậy thì nếu mệt cứ bảo anh nhé. Dù sao Paulette\ncũng còn công việc ở hội đồng và chức giám đốc nữa mà」
- Sửa: 「Vậy thì nếu mệt cứ bảo tôi nhé. Dù sao Paulette cũng còn công việc ở hội đồng và chức giám đốc nữa mà」

**2014 [双鉄]** — Soutetsu tự xưng "anh"; docs: "Tôi".

- JP: 「これは配慮が足りなかったな。\n僕らには小さな障害も、れいなの歩幅では――」
- TW: 「都怪我想的不周到。就算對我們來說只是小小的障礙，但以玲奈的步幅來衡量的話——」
- Cũ: 「Là do anh thiếu chu đáo rồi.\nChướng ngại nhỏ đối với chúng ta, nhưng với sải chân của Reina thì——」
- Sửa: 「Là do tôi thiếu chu đáo rồi. Chướng ngại nhỏ đối với chúng ta, nhưng với sải chân của Reina thì——」

### B. Thuật ngữ theo quyết định mới — 御一夜 = "Ohitoyo" (8 dòng, trong đó 1952 đã liệt kê ở mục A vì mang cả hai lỗi)

**1249 [ポーレット]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 「\x%l架台;#00ffc040;架台%l;#;の方は、蓑笠さんに相談ですね。\n宝箱は……もともと、御一夜は木工も盛んですし」
- TW: 「\x%l架台;#00ffc040;底座%l;#;就去找蓑笠先生商量一下。寶箱的話……原本御一夜的木工水準就很高」
- Cũ: 「Về phần \x%l架台;#00ffc040;bệ đỡ%l;#; thì phải bàn với ông Minokasa thôi.\nCòn rương kho báu…… vốn dĩ nghề mộc ở Ohimitera cũng rất thịnh vượng mà」
- Sửa: 「……vốn dĩ nghề mộc ở Ohitoyo cũng rất thịnh vượng mà」

**1696 [双鉄]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 「持ち帰りを、普段づかいもできるような箱とすれば、\n御一夜の木工・竹工の生きた宣伝にもなるはずです」
- TW: 「將小寶箱做成平時也能使用的樣式，應該還能宣傳御一夜的木工藝和竹工藝」
- Cũ: 「Nếu chiếc rương mang về được thiết kế để có thể sử dụng thường ngày,\nthì nó sẽ trở thành một cách quảng bá sống động cho nghề mộc và thủ công mỹ nghệ tre của Ohimitera」
- Sửa: 「……cho nghề mộc và thủ công mỹ nghệ tre của Ohitoyo」

**1781 [蓑笠]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 「そぎゃんとですな。\n御一夜の[たけゆみ,1]竹弓ば、日ノ本中から求められとりますよ」
- TW: 「是咧。御一夜的竹弓在整個日本都是很有名的咧」
- Cũ: 「Đúng vậy đó.\nCung tre của Ohimitera được săn lùng khắp cả Hinomoto đấy」
- Sửa: 「Cung tre của Ohitoyo được săn lùng khắp cả Hinomoto đấy」

**1856 [蓑笠]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 「で。市長さんのおっしゃられるとおり、\n御一夜は、木工、[ちっこう,1]竹工にも古か歴史を持つ町とです」
- TW: 「正如市長所說，御一夜的木工竹工也有悠久的歷史」
- Cũ: 「Vậy đó. Đúng như lời cô Thị trưởng nói,\nOhimitera là một thị trấn có lịch sử lâu đời về nghề mộc và nghề thủ công mỹ nghệ tre」
- Sửa: 「Ohitoyo là một thị trấn có lịch sử lâu đời về nghề mộc và nghề thủ công mỹ nghệ tre」

**1942 [れいな]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 「[ハチロク,3]8620にも\x%l客車;#00ffc040;客車%l;#;がついたら、\n御一夜鉄道、すごくにぎやかになりますねぇ」
- TW: 「要是八六也裝上了\x%l客車;#00ffc040;客運車廂%l;#;，御一夜鐵路一下子就會變得熱鬧起來啦」
- Cũ: 「Nếu 8620 cũng được gắn \x%l客車;#00ffc040;toa hành khách%l;#;,\nthì Đường sắt Ohimitera sẽ nhộn nhịp lắm đây nha~」
- Sửa: 「……thì Đường sắt Ohitoyo sẽ nhộn nhịp lắm đây nha~」

**2311 [monologue]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 戻りの\x%l列車;#00ffc040;列車%l;#;を御一夜にまで運んだあとで、\n\x%l8620;#00ffc040;8620%l;#;は転車し、術仙洞廃駅で待っててくれる。
- TW: 回程的\x%l列車;#00ffc040;列車%l;#;會在御一夜放下客人，然後\x%l8620;#00ffc040;８６２０%l;#;進行轉車，前往術仙煤礦廢車站等我們。
- Cũ: Sau khi đưa \x%l列車;#00ffc040;chuyến tàu%l;#; chiều về đến Ohimitera,\n\x%l8620;#00ffc040;8620%l;#; sẽ quay đầu và đợi chúng tôi ở ga bỏ hoang Jutsu-sen.
- Sửa: 「Sau khi đưa chuyến tàu chiều về đến Ohitoyo,」

**2366 [monologue]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: この計画が上手く行き、御一夜が発展の途を進むとして、\nしかし、宝箱は置き去りになる。
- TW: 就算我們的計劃成功，御一夜迎來了繁榮的發展。而寶箱卻會被就此棄置不管。
- Cũ: Cho dù kế hoạch này thành công, Ohimitera tiếp tục phát triển,\nnhưng những chiếc rương kho báu sẽ bị bỏ lại đó.
- Sửa: 「Cho dù kế hoạch này thành công, Ohitoyo tiếp tục phát triển,」

### C. Thuật ngữ — 整備体 (1 dòng, đề xuất chưa chốt)

**1664 [れいな]** — 整備体 bị dịch thành "thân chính" — gộp chung với 運転ボディ, trong khi JP phân biệt hai thân (整備体 = thân bảo trì, 運転ボディ = thân vận hành). Đề xuất dùng "thân bảo trì" theo tiền lệ Hachiroku 12 再開発 (3195/3021) — CHƯA được Hieu chốt, ghi là đề xuất. Thẻ %l giữ nguyên, chỉ đổi gloss.

- JP: 「整備[ボディ]体では――だっこ、\nほとんどされることってないですからぁ」
- TW: 「因為玲奈在使用整備體的的時候，好像還沒有被人抱起來過呢」
- Cũ: 「Tại vì trong \x%l整備体;#00ffc040;thân chính%l;#;——\nReina hiếm khi được bế lắm ạ~」
- Sửa: 「Tại vì trong \\x%l整備体;#00ffc040;thân bảo trì%l;#;——Reina hiếm khi được bế lắm ạ~」

## Các cặp trùng lặp / lệch vị trí đã xác nhận

**0 cặp.** Không có dòng nào bị lệch vị trí, không có chuỗi xoay vòng, không có dòng nào mang bản dịch của dòng khác (kiểm chứng bằng chỉ mục Việt toàn dự án). Các cặp trùng lặp nội bộ đều là câu cảm thán ngắn hợp lệ, không tính lỗi.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)

- 御一夜 → "Ohitoyo" trong các bản sửa (quyết định 19/11; sau khi sửa file không còn "Ohimitera" nào; file đã có sẵn 1 "Ohitoyo" đúng ở 2307).
- 整備体 → "thân bảo trì" (đề xuất, xem dưới); 運転ボディ → "cơ thể lái tàu" ở 2512 được giữ nguyên (dịch đúng, chỉ ghi nhận là chưa thống nhất với đề xuất "thân vận hành" — xem dưới).
- 帝鉄, 湯医, 冥国, 冥軍, 小畑, 大畑, コン, 駿袋鉄道 không xuất hiện trong file này.
- Soutetsu gọi Reina bằng "em" và xưng "tôi" khi nói với Reina (1935, 2014 sau khi sửa); Soutetsu gọi ông Minokasa bằng "ông", tự xưng "cháu" (1949, 2010, 2012 — đúng, không sửa).
- Không có bản sao file này ở thư mục khác (đã kiểm tra md5 toàn bộ 227 file TOML-2).

## Đề xuất cập nhật context (chưa quyết định — cần Hieu chốt)

1. **整備体 / 運転ボディ — cần một cặp tên phân biệt (key 1664, 2512):** JP phân biệt hai thân của Railord: 整備体 (thân dùng để bảo trì/sửa chữa) và 運転ボディ (thân dùng để lái tàu). Bản dịch hiện tại gộp 整備体 thành "thân chính" (1664 — đã sửa thành "thân bảo trì" theo đề xuất) trong khi 運転ボディ được dịch "cơ thể lái tàu" (2512 — dịch đúng nghĩa nhưng khác hệ tên). Đề xuất: **整備体 = "thân bảo trì", 運転ボディ = "thân vận hành"** (theo tiền lệ Hachiroku 12 再開発: 3195/3021 dùng "thân bảo trì", 3285 dùng "thân vận hành"). Nếu Hieu chốt cặp này, 2512 cũng cần đổi "cơ thể lái tàu" → "thân vận hành" để thống nhất toàn dự án. Hiện tại 2512 KHÔNG tính là lỗi (dịch đúng nghĩa), chỉ ghi nhận để thống nhất sau.

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)

Lưu ý khi chép: các bản sửa viết liền một dòng, không chèn `\n` thủ công — theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng. Khối này đã kiểm tra bằng máy: trích khối từ chính file review, parse bằng tomllib — **25/25 key** khớp đúng tập dòng sai, không thừa không thiếu, giá trị sau khi parse khớp đúng bản sửa.

```toml
1249 = "「……vốn dĩ nghề mộc ở Ohitoyo cũng rất thịnh vượng mà」"
1528 = "「Nhưng bây giờ…… tôi cũng có cảm giác muốn thử trở thành một người cha. Và đồng thời, cũng có cảm giác rất sợ hãi nữa」"
1638 = "「À, xin lỗi. Tôi——chẳng biết cách khen ngợi nào khác ngoài cách này」"
1664 = "「Tại vì trong \\x%l整備体;#00ffc040;thân bảo trì%l;#;——Reina hiếm khi được bế lắm ạ~」"
1668 = "「——Lúc nhìn thấy nhà máy điện tôi cũng đã nghĩ thế này」"
1696 = "「……cho nghề mộc và thủ công mỹ nghệ tre của Ohitoyo」"
1733 = "「Vì tôi đã trải qua vụ tai nạn đó. Và mất đi người em sinh đôi——mất đi một nửa của mình」"
1736 = "「Từ trước đến nay——, chưa một lần nào, tôi nghĩ đến chuyện mình có muốn làm cha hay không」"
1742 = "「Thế nên, thỉnh thoảng tôi lại thấy bất an. Tôi cứ nghĩ có phải mình đang ép em làm việc quá sức hay không」"
1743 = "「Nên tôi cứ nghĩ rằng đằng nào mình cũng sẽ chết, và sống chỉ để chờ đến lúc đó. Tôi chưa từng tưởng tượng đến việc trở thành một người cha, hay sinh con đẻ cái」"
1781 = "「Cung tre của Ohitoyo được săn lùng khắp cả Hinomoto đấy」"
1797 = "「Đúng vậy. Giờ nghĩ lại, bản thân hầm mỏ có lẽ cũng thế. Tôi có cảm giác hầu hết các thiết bị đều được giữ nguyên như vậy」"
1856 = "「Ohitoyo là một thị trấn có lịch sử lâu đời về nghề mộc và nghề thủ công mỹ nghệ tre」"
1872 = "「Tôi thấy Paulette thực sự rất tuyệt vời. Cả về tầm nhìn rộng mở, lẫn sự chăm lo không hề chểnh mảng」"
1892 = "「Tình trạng của nhà máy điện cũng tốt hơn tôi nghĩ nhiều. Như thế thì có khi còn có thể tái khởi động lại được ấy chứ」"
1929 = "「Nếu là ông Minokasa thì chắc chắn sẽ có mối quan hệ trong lĩnh vực đó. Nếu được, tôi rất muốn nhờ ông ấy giới thiệu」"
1935 = "「Có cần tôi bế không? Nếu cần thì cứ nói nhé」"
1942 = "「……thì Đường sắt Ohitoyo sẽ nhộn nhịp lắm đây nha~」"
1945 = "「Nếu có chuyện gì đau khổ, tôi muốn em hãy nói cho tôi nghe. Tôi muốn được trở thành chỗ dựa cho Paulette」"
1952 = "「Cho là có thiết kế rồi, vậy còn người làm thì sao? Tôi nghĩ tốt nhất là nên làm ở Ohitoyo」"
1963 = "「Bất cẩn là bọn tôi mới đúng」"
2002 = "「Vậy thì nếu mệt cứ bảo tôi nhé. Dù sao Paulette cũng còn công việc ở hội đồng và chức giám đốc nữa mà」"
2014 = "「Là do tôi thiếu chu đáo rồi. Chướng ngại nhỏ đối với chúng ta, nhưng với sải chân của Reina thì——」"
2311 = "「Sau khi đưa chuyến tàu chiều về đến Ohitoyo,」"
2366 = "「Cho dù kế hoạch này thành công, Ohitoyo tiếp tục phát triển,」"
```

## Việc tiếp theo

- Không có dòng nào chưa chắc chắn trong file này — mọi lỗi đều đã có bản sửa.
- Chờ Hieu chốt đề xuất cặp thuật ngữ 整備体/運転ボディ ("thân bảo trì" / "thân vận hành"): nếu chốt, 2512 cần đổi theo; nếu không chốt, 1664 vẫn giữ "thân bảo trì" như một bản sửa cục bộ hay quay lại "thân chính"? — cần quyết định rõ vì "thân chính" gộp hai khái niệm khác nhau.
- Câu hỏi mở từ các file trước vẫn chưa liên quan thêm: Soutetsu gọi Paulette "cô" hay "em" — trong file này Soutetsu không gọi Paulette bằng "cô"/"em" lần nào, nên không có thêm bằng chứng.

## Kết bài

File 支線 là một trường hợp đặc biệt: sạch hoàn toàn về cấu trúc (0 lệch vị trí) nhưng nặng về xưng hô theo kiểu hệ thống — người dịch đã nhất quán dùng "anh" cho Soutetsu trong cả file, và nhất quán dùng "Ohimitera" cho 御一夜. Hai sự nhất quán này đều trái với docs/quyết định đã chốt, nên 25 bản sửa tuy nhiều nhưng đều là sửa cơ học, không có chỗ nào phải đắn đo về nghĩa. Sau khi áp 25 bản sửa (và chờ chốt cặp thuật ngữ 整備体/運転ボディ), file coi như xong. Hai file Paulette 07 cùng nhau cho thấy một quy luật đã lặp lại nhiều lần: hai file cùng một chương có thể khác nhau hoàn toàn về bản chất lỗi — うさぎ nhẹ và rải rác (2,8%), 支線 nặng về xưng hô hệ thống (7,0%) — không thể đoán loại lỗi từ file bên cạnh.
