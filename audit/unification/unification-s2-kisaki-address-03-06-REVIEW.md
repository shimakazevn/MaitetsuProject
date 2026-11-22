# Unification — §2 P4: Kisaki → Soutetsu "anh Soutetsu" → "Soutetsu" (batch U7a, folders 03_Paulette + 06_Kisaki)

**Phạm vi:** §2 P4 (DECIDED 21/11 ~19:45, Muse theo uỷ quyền — Kisaki là senpai của Soutetsu, JP là 双鉄 trần trong mọi dòng đã kiểm chứng; cách gọi của Kisaki với Soutetsu là tên trần "Soutetsu", không bao giờ "anh Soutetsu") của `UNIFICATION-LIST.md`. Chỉ các file KHÔNG phải lr/tsuika trong 2 folder CSV3 03_Paulette + 06_Kisaki. Các file lr/tsuika và 11_Other thuộc batch U7b — không đụng.
**Không đụng:** các mục P khác (P2/P3/P5/P6…), §1/§3–§6, tag sweep (§5). Không sửa `ROUTE-UNIFICATION.md`, `MEMORY.md`, hay bất kỳ file audit/moans nào. Không gửi gì cho Hieu.
**Nguồn:** CSV3 good-set (87.833 dòng; đã loại 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`), `audit-*-wrong.json` (9.194 mục map được; 46 mục không map — toàn bộ là file `audit-lr-nagih2-wrong.json` dạng dict key→fix không có JP, không thuộc phạm vi batch này), `moans/moan-*-wrong.json` (1.516 mục), TOML-2 (chỉ dùng để quét gap — 0 dòng gap, xem §2), các đợt unification đã gộp (656 mục; 0 dòng trùng với batch này, xem §5).

## Phương pháp

- `old_vn` theo quy ước bắt buộc: giá trị moan nếu (file,key) có trong moan list, nếu không thì giá trị audit fix, nếu không thì giá trị unification đã gộp, nếu không thì VN CSV3 good-set. Trong 126 dòng này: CSV3 114 dòng, audit fix 8 dòng (稀咲02 2008; 稀咲03 1750; 稀咲h1 1357/1373/1376/1398; 稀咲h3 2003/2468), moan fix 2 dòng (稀咲h3 2254/2360), unification đã gộp 2 dòng (1416 — fix T60; 2203 — fix M17 — GHÉP bởi coordinator 22/11, xem ghi chú §7). Không có dòng nào nằm trong cả audit/moan list lẫn unification list đã gộp, nên hai thứ tự ưu tiên (moan > audit > unification > CSV3 theo task, và unification > moan > audit > CSV3 theo thứ tự rebuild) cho cùng kết quả ở batch này. (Toàn dự án có 44 dòng mà hai thứ tự cho khác nhau — không dòng nào thuộc batch này.)
- **Liệt kê:** quét toàn bộ CSV3 good-set, lấy mọi dòng có folder 03_Paulette/06_Kisaki, basename KHÔNG bắt đầu bằng `lr`, speaker là Kisaki (Character `稀咲`), mà giá trị hiện tại chứa "anh Soutetsu" (không phân biệt hoa/thường, regex `anh soutetsu`): **124 dòng**, toàn bộ trong 5 file 06_Kisaki (稀咲02: 15; 稀咲03: 8; 稀咲h1: 34; 稀咲h2: 22; 稀咲h3: 45). Folder 03_Paulette (file không lr): **0 dòng** — kể cả quét VN CSV3 thô cũng 0 dòng. Cộng **2 dòng rên tách tên** "anh Sou――tetsu" (稀咲h2 1166/1205, xem Quyết định D1) → **tổng 126 dòng sửa, 132 lần xuất hiện** ("anh Soutetsu" 94 lần + "Anh Soutetsu" 36 lần + "anh Sou――tetsu" 2 lần).
- **Kiểm chứng từng dòng:** đọc JP (+TW) và 3–5 dòng kề của cả 126 dòng: người nói là Kisaki (Character `稀咲`), người nghe là Soutetsu (cảnh 2 người, hoặc Soutetsu đáp ở dòng kề; các dòng 1956/1969/2731/2793 tuy "anh Soutetsu" đứng ở vị trí ngữ pháp ngôi ba nhưng người nghe vẫn là Soutetsu — xem Quyết định D2). JP của 124 dòng đều chứa 双鉄 trần (0 dòng có 双鉄さん/くん/様/ちゃん); 2 dòng rên tách tên thì JP cũng tách tên tương ứng (双――て、つっ / 双っ――鉄っ). Không dòng nào có "anh Soutetsu" trong thẻ gloss `%l` (0 dòng).
- **Quét gap TOML-2:** grep giá trị `[script]` chứa "anh Soutetsu" trong cả 40 file TOML đích (5 file Kisaki + 35 file 03_Paulette không lr): mọi hit đều có key trong CSV3 (0 dòng gap). Đối chiếu chéo: 稀咲02 TOML 16 hit vs ứng viên 15 — thừa 1 là key 2376 của Hibiki (đã sửa trong audit, xem §3); 稀咲03 TOML 9 hit vs ứng viên 8 — thừa 1 là key 2137 của Reina (xem §3); h1/h2/h3 khớp tuyệt đối (34/22/45).
- **Không sửa bulk bằng script:** mọi giá trị fix đều do đọc JP (+TW + dòng kề) rồi quyết; script chỉ dùng để liệt kê, lắp khối TOML và kiểm chứng cơ học (span-diff `old_vn` → `fix` cho 126/126 dòng chỉ gồm đúng phép bỏ "anh" trước "Soutetsu"/"Sou――tetsu" — xem §4).

## 1. P4 — 稀咲02_新事業案.txt.toml (15 dòng)

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1716 | 「だろうね。土地が絡むことだし。\nっていうか、なら双鉄もそのことを？」 | 「也是啊。畢竟還關係到土地。這麼說的話，你也想到過這個？」 | 「Chắc là vậy rồi. Vì còn liên quan đến đất đai nữa mà.\nMà nói vậy tức là, anh Soutetsu cũng đã nghĩ đến chuyện đó?」 | 「Chắc là vậy rồi. Vì còn liên quan đến đất đai nữa mà.\nMà nói vậy tức là, Soutetsu cũng đã nghĩ đến chuyện đó?」 | JP 双鉄も — hỏi Soutetsu (Soutetsu 1704 vừa đáp). |
| 1755 | 「双鉄もか。やっぱり、誰でも感じるよね。\nあんなに短い区間を往復するだけじゃもったいない」 | 「你也有啊。果然每個人都會有這種感覺呢。只在這麼短的路段內往返，太浪費了」 | 「Cả anh Soutetsu cũng vậy sao. Quả nhiên, ai cũng sẽ cảm thấy như thế nhỉ.\nNếu chỉ chạy đi chạy lại trên một đoạn đường ngắn như vậy thì thật lãng phí.」 | 「Cả Soutetsu cũng vậy sao. Quả nhiên, ai cũng sẽ cảm thấy như thế nhỉ.\nNếu chỉ chạy đi chạy lại trên một đoạn đường ngắn như vậy thì thật lãng phí.」 | JP 双鉄もか — hỏi Soutetsu (Soutetsu 1748 vừa nói). |
| 1768 | 「古風だねぇ、双鉄は。\nうちの父より、よっぽど古い考え方だ」 | 「你還真是個傳統的人。比家父還要傳統得多了」 | 「Anh Soutetsu cổ hủ thật đấy.\nSuy nghĩ còn cổ hủ hơn cả bố tôi nhiều.」 | 「Soutetsu cổ hủ thật đấy.\nSuy nghĩ còn cổ hủ hơn cả bố tôi nhiều.」 | JP 双鉄は — nói với Soutetsu (Soutetsu 1762/1764 đáp). |
| 1858 | 「ひうっ！？　な、な、なんだい、双鉄っ」 | 「呀嗚！？什、什、什麼事，雙鐵」 | 「Hya!? Ch, ch, chuyện gì vậy, anh Soutetsu.」 | 「Hya!? Ch, ch, chuyện gì vậy, Soutetsu.」 | JP 双鉄っ — gọi Soutetsu (giật mình). |
| 1919 | 「って、双鉄？　どこへいくんだい？」 | 「啊，雙鐵？你去哪？」 | 「Ơ, anh Soutetsu? Anh đi đâu vậy?」 | 「Ơ, Soutetsu? Anh đi đâu vậy?」 | JP 双鉄？どこへいくんだい？ — hỏi Soutetsu đi đâu. |
| 1956 | 「あの熱に焼かれた後の、この風が。\nきっと、ね。双鉄――キミの何かを、変えたのさ」 | 「在經歷過炎熱後的這陣風，一定改變了雙鐵——改變了你的某些部分」 | 「Chính là cơn gió này, sau khi bị thiêu đốt bởi hơi nóng kia.\nChắc chắn là vậy. Nó đã thay đổi——một phần nào đó trong anh Soutetsu.」 | 「Chính là cơn gió này, sau khi bị thiêu đốt bởi hơi nóng kia.\nChắc chắn là vậy. Nó đã thay đổi——một phần nào đó trong Soutetsu.」 | JP 双鉄――キミの何か — nói với Soutetsu về chính anh (キミ = Soutetsu); không phải ngôi ba với người khác. |
| 2008 | 「双鉄が[ハチロク,3]8620を所有し、走らせ、利益の分配を受ける。\n同じことを、レールを使って、大人数でやるってことさ」 | 「就像雙鐵擁有[八六,3]８６２０，可以讓８６２０行駛並得到分紅一樣。就是讓更多的人來參與鐵路運營的意思」 | 「Giống như anh Soutetsu sở hữu \x%l8620;#00ffc040;8620%l;#, cho chạy tàu, và nhận được phần lợi nhuận được chia. Ý tôi là làm điều tương tự với đường ray, nhưng với số lượng người tham gia lớn hơn.」 | 「Giống như Soutetsu sở hữu \x%l8620;#00ffc040;8620%l;#, cho chạy tàu, và nhận được phần lợi nhuận được chia. Ý tôi là làm điều tương tự với đường ray, nhưng với số lượng người tham gia lớn hơn.」 | JP 双鉄が8620を所有 — giải thích cho Soutetsu (old_vn là audit fix; giữ thẻ %l 8620). |
| 2099 | 「ボクが、双鉄にどんな刺激を？」 | 「我給你帶來了什麼刺激？」 | 「Tôi, đã kích thích anh Soutetsu như thế nào?」 | 「Tôi, đã kích thích Soutetsu như thế nào?」 | JP 双鉄にどんな刺激を — hỏi Soutetsu. |
| 2142 | 「双鉄が」 | 「是你做的？」 | 「Anh Soutetsu làm á?」 | 「Soutetsu làm á?」 | JP 双鉄が — hỏi Soutetsu có phải anh làm không. |
| 2292 | 「ともあれ、隈銀と\x%lエアクラ;#00ffc040;エアクラ%l;#;社との現状について、\n双鉄が興味を持ってくれたみたいで、嬉しいよ」 | 「總而言之，你能對隈元銀行和\x%lエアクラ;#00ffc040;空凝機%l;#;公司的現狀產生興趣，我也很高興」 | 「Dù sao thì, tôi rất vui vì anh Soutetsu có vẻ đã hứng thú\nvới tình trạng hiện tại của Kumagin và công ty \x%lエアクラ;#00ffc040;Aircra%l;#;.」 | 「Dù sao thì, tôi rất vui vì Soutetsu có vẻ đã hứng thú\nvới tình trạng hiện tại của Kumagin và công ty \x%lエアクラ;#00ffc040;Aircra%l;#;.」 | JP 双鉄が興味を持ってくれた — nói với Soutetsu. |
| 2297 | 「刺激っていうか――僕が感じたのは欲さ。\nだから、双鉄の変化のきっかけになったと思った」 | 「與其說是刺激——不如說，我感覺到的是欲望。所以我想，這或許是你產生變化的契機」 | 「Nói là kích thích thì——thứ tôi cảm nhận được là dục vọng.\nThế nên, tôi nghĩ đó chính là cơ hội để anh Soutetsu thay đổi.」 | 「Nói là kích thích thì——thứ tôi cảm nhận được là dục vọng.\nThế nên, tôi nghĩ đó chính là cơ hội để Soutetsu thay đổi.」 | JP 双鉄の変化 — nói với Soutetsu về sự thay đổi của anh. |
| 2382 | 「そ、そ、そ、双鉄。\nそ、そ、そんなに、緊張、しないで、くれない、かな」 | 「雙、雙、雙、雙鐵。能、能、能別那麼、緊、緊、張、嗎」 | 「A, a, a, anh Soutetsu.\nA, a, anh, có thể, đừng, căng, thẳng, như, vậy, được, không.」 | 「A, a, a, Soutetsu.\nA, a, anh, có thể, đừng, căng, thẳng, như, vậy, được, không.」 | JP 双鉄 — gọi Soutetsu, bảo đừng căng thẳng. |
| 2383 | 「双鉄。それだ。それで行こう」 | 「雙鐵。就是這個。就用這個辦法吧」 | 「Anh Soutetsu. Chính là cái này. Hãy làm theo cách đó đi.」 | 「Soutetsu. Chính là cái này. Hãy làm theo cách đó đi.」 | JP 双鉄 — gọi Soutetsu. |
| 2385 | 「おかえり双鉄、どうだった？」 | 「雙鐵，你回來了，怎麼樣？」 | 「Anh Soutetsu về rồi à, sao rồi?」 | 「Soutetsu về rồi à, sao rồi?」 | JP おかえり双鉄 — chào Soutetsu về. |
| 2386 | 「双鉄も、その辺を気にするほう？」 | 「雙鐵，你是在意這些的人？」 | 「Anh Soutetsu cũng là người bận tâm đến mấy chuyện đó sao?」 | 「Soutetsu cũng là người bận tâm đến mấy chuyện đó sao?」 | JP 双鉄も — hỏi Soutetsu. |

## 2. P4 — 稀咲03_純白のレール.txt.toml (8 dòng)

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1750 | 「うふふっ、双鉄」 | 「呵呵呵，雙鐵」 | 「Ufufu, anh Soutetsu.」 | 「Ufufu, Soutetsu.」 | JP うふふっ、双鉄 — gọi Soutetsu (old_vn là audit fix; ngay sau lời tỏ tình 1744). |
| 1760 | 「わ！？　双鉄？　どうしたのさ、怖い顔して」 | 「哇！？雙鐵？怎麼了，表情那麼嚇人」 | 「Oa!? Anh Soutetsu? Có chuyện gì vậy, sao mặt mũi đáng sợ thế.」 | 「Oa!? Soutetsu? Có chuyện gì vậy, sao mặt mũi đáng sợ thế.」 | JP 双鉄？ — hỏi Soutetsu. |
| 1930 | 「キミが、ボクを好きになってくれるずっと前から。\n双鉄、ボクはね？　キミを好きだよ」 | 「我可是在你喜歡上我好久之前，就喜歡上你了啊，雙鐵」 | 「Từ rất lâu trước khi anh bắt đầu thích em.\nAnh Soutetsu, anh biết không? Em đã thích anh rồi đấy.」 | 「Từ rất lâu trước khi anh bắt đầu thích em.\nSoutetsu, anh biết không? Em đã thích anh rồi đấy.」 | JP 双鉄、ボクはね？キミを好きだよ — tỏ tình với Soutetsu. |
| 1979 | 「そうだね、双鉄。\nもちろんボクも、一緒だよ？」 | 「是啊，雙鐵。我也一樣」 | 「Đúng vậy, anh Soutetsu.\nTất nhiên em cũng sẽ, đồng hành cùng anh chứ?」 | 「Đúng vậy, Soutetsu.\nTất nhiên em cũng sẽ, đồng hành cùng anh chứ?」 | JP 双鉄 — nói với Soutetsu. |
| 1980 | 「そうだね、双鉄。そろそろ時間だ」 | 「是啊，雙鐵，時間快到了」 | 「Đúng vậy, anh Soutetsu. Sắp đến giờ rồi.」 | 「Đúng vậy, Soutetsu. Sắp đến giờ rồi.」 | JP 双鉄 — nói với Soutetsu. |
| 2050 | 「細目はこれから精査して詰めるとして――\nどうだろう、双鉄。こんな感じの募集説明で」 | 「細節部分可以慢慢確定。雙鐵，你覺得這樣的集資說明可以嗎」 | 「Chi tiết cụ thể thì từ giờ sẽ kiểm tra kỹ lưỡng và chốt lại sau——\nAnh thấy sao, anh Soutetsu. Một bản giải trình huy động vốn mang cảm giác thế này.」 | 「Chi tiết cụ thể thì từ giờ sẽ kiểm tra kỹ lưỡng và chốt lại sau——\nAnh thấy sao, Soutetsu. Một bản giải trình huy động vốn mang cảm giác thế này.」 | JP 双鉄 — hỏi ý Soutetsu về bản giải trình huy động vốn. |
| 2125 | 「だったら、何に。\n双鉄は、そんなに真剣になっているのさ？」 | 「那雙鐵你是為了什麼而如此認真？」 | 「Nếu vậy thì, với chuyện gì.\nMà anh Soutetsu lại trở nên nghiêm túc đến vậy?」 | 「Nếu vậy thì, với chuyện gì.\nMà Soutetsu lại trở nên nghiêm túc đến vậy?」 | JP 双鉄は — hỏi Soutetsu (dù Hibiki/Mototada có mặt, câu hỏi hướng về Soutetsu). |
| 2141 | 「何を弱気なことを言っているんだい、双鉄」 | 「雙鐵，你在說什麼洩氣話呢」 | 「Anh đang nói lời yếu đuối gì vậy, anh Soutetsu.」 | 「Anh đang nói lời yếu đuối gì vậy, Soutetsu.」 | JP 双鉄 — nói với Soutetsu. |

## 3. P4 — 稀咲h1_性生活.txt.toml (34 dòng)

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1014 | 「……うん。やっぱり好きになれそうだ。\nそれに、双鉄も気持ちよさそうだしね？」 | 「……嗯，我真的會喜歡上這種味道的。而且雙鐵也很高興吧？」 | 「……Ưm. Quả nhiên là em có thể thích nó.\nHơn nữa, anh Soutetsu trông cũng có vẻ rất sướng đúng không?」 | 「……Ưm. Quả nhiên là em có thể thích nó.\nHơn nữa, Soutetsu trông cũng có vẻ rất sướng đúng không?」 | JP 双鉄も — nói với Soutetsu. |
| 1016 | 「……ここ、だよ？　双鉄。ヴァギナ――膣。\nこの穴に、双鉄のペニスを挿れるんだ」 | 「……就是這裡喔，雙鐵。Vāgīna――小穴。雙鐵的陰莖就要插進這裡來喔」 | 「……Là ở đây, nè? Anh Soutetsu. Vagina――âm đạo.\nAnh sẽ đưa dương vật của mình vào cái lỗ này đó」 | 「……Là ở đây, nè? Soutetsu. Vagina――âm đạo.\nAnh sẽ đưa dương vật của mình vào cái lỗ này đó」 | JP 双鉄 — gọi Soutetsu (chỉ chỗ). |
| 1192 | 「事故の傷が――双鉄に性を嫌悪させていたんだね」 | 「事故落下的傷――讓你對性有了厭惡感吧」 | 「Vết thương từ vụ tai nạn——đã khiến anh Soutetsu cảm thấy ghê tởm tình dục nhỉ.」 | 「Vết thương từ vụ tai nạn——đã khiến Soutetsu cảm thấy ghê tởm tình dục nhỉ.」 | JP 双鉄に — nói với Soutetsu về vết thương của anh. |
| 1216 | 「ボクも、教えてもらってるんだよ？\n双鉄に――恋のこと、セックスのこと、男の子のこと」 | 「其實你也在告訴我很多我不知道的事呢。關於戀愛啊，做愛啊，還有男孩子的事」 | 「Em cũng được anh dạy cho nhiều điều mà?\nTừ anh Soutetsu――về tình yêu, về tình dục, và về con trai nữa」 | 「Em cũng được anh dạy cho nhiều điều mà?\nTừ Soutetsu――về tình yêu, về tình dục, và về con trai nữa」 | JP 双鉄に — nói với Soutetsu (học từ anh). |
| 1247 | 「きゃっ！？　双鉄っ！！？」 | 「呀！？　雙鐵！！？」 | 「Kya!? Anh Soutetsu!!?」 | 「Kya!? Soutetsu!!?」 | JP 双鉄っ — gọi Soutetsu. |
| 1252 | 「ふふっ。嬉しいな。\n双鉄が、ボクと同じ気持ちでいてくれて」 | 「呵呵，我很高興。雙鐵能和我有一樣的心情，好高興」 | 「Fufu. Em vui lắm.\nVì anh Soutetsu cũng có cùng cảm xúc với em」 | 「Fufu. Em vui lắm.\nVì Soutetsu cũng có cùng cảm xúc với em」 | JP 双鉄が — nói với Soutetsu. |
| 1317 | 「うん。だから、一緒に勉強しよう？　双鉄と、ボクの\n――きっとありきたりで、だけど特別な、セックスを」 | 「嗯，所以一起來學習吧？　我和雙鐵的――平凡卻又無比特別的做愛」 | 「Ừm. Vậy nên, chúng ta cùng nhau học nhé? Tình dục của anh Soutetsu và em\n――chắc chắn sẽ rất bình dị, nhưng cũng vô cùng đặc biệt」 | 「Ừm. Vậy nên, chúng ta cùng nhau học nhé? Tình dục của Soutetsu và em\n――chắc chắn sẽ rất bình dị, nhưng cũng vô cùng đặc biệt」 | JP 双鉄と、ボクの — nói với Soutetsu. |
| 1319 | 「うん。双鉄」 | 「嗯，雙鐵」 | 「Vâng. Anh Soutetsu」 | 「Vâng. Soutetsu」 | JP 双鉄 — gọi Soutetsu. |
| 1321 | 「ん？　なんだい？　なにか後ろ暗いことでも――\nあ、というか。なんで双鉄がこんな時間の支店長室に？」 | 「嗯？　怎麼了？　難不成做了什麼虧心事――對了，你怎麼會在這種時候待在支行長室裡？」 | 「Hửm? Gì vậy? Có chuyện gì mờ ám sao——\nà, mà này. Sao anh Soutetsu lại ở trong phòng giám đốc chi nhánh vào giờ này?」 | 「Hửm? Gì vậy? Có chuyện gì mờ ám sao——\nà, mà này. Sao Soutetsu lại ở trong phòng giám đốc chi nhánh vào giờ này?」 | JP 双鉄が — hỏi Soutetsu sao ở phòng giám đốc giờ này. |
| 1333 | 「いいよ。双鉄。\n……見てて、ね？　脱ぐとこ」 | 「好啊，雙鐵。……看好了哦？　內褲脫下的位置」 | 「Được thôi. Anh Soutetsu.\n……Nhìn cho kỹ, nhé? Cảnh em cởi ra ấy」 | 「Được thôi. Soutetsu.\n……Nhìn cho kỹ, nhé? Cảnh em cởi ra ấy」 | JP 双鉄 — gọi Soutetsu. |
| 1344 | 「DVDで勉強できるのは、誰か他人のセックスだから。\nボクのセックスは、双鉄からしか学べないから」 | 「從DVD裡只能看來別人做的愛。屬於我的做愛只有雙鐵能教會我」 | 「Vì học qua DVD thì đó cũng chỉ là tình dục của người khác thôi.\nCòn tình dục của riêng em, thì em chỉ có thể học từ anh Soutetsu mà thôi」 | 「Vì học qua DVD thì đó cũng chỉ là tình dục của người khác thôi.\nCòn tình dục của riêng em, thì em chỉ có thể học từ Soutetsu mà thôi」 | JP 双鉄からしか — nói với Soutetsu (chỉ học từ anh). |
| 1349 | 「なんだ……双鉄――ンッ――はっ――おっぱい――\nもみもみ――した、かった――んっ――の？」 | 「怎麼……雙鐵――嗯――哈――你早就想――揉一揉――胸部了――嗯――嗎？」 | 「Gì vậy…… anh Soutetsu――ưm――ha――ngực em――\nanh muốn――nắn bóp――lắm――ưm――sao?」 | 「Gì vậy…… Soutetsu――ưm――ha――ngực em――\nanh muốn――nắn bóp――lắm――ưm――sao?」 | JP 双鉄 — hỏi Soutetsu. |
| 1350 | 「どう……かな、双鉄……\n他に、して欲しいことは、ないかい？」 | 「怎麼樣啊……雙鐵……還有什麼想讓我為你做的嗎？」 | 「Thế nào…… hả, anh Soutetsu……\nAnh còn muốn em làm gì khác nữa không?」 | 「Thế nào…… hả, Soutetsu……\nAnh còn muốn em làm gì khác nữa không?」 | JP 双鉄 — hỏi Soutetsu. |
| 1357 | 「性は――セックスは嫌悪をするべきものじゃない。\nボクが、双鉄にそれを教えてあげる」 | 「性事――做愛不是什麼應該厭惡的事。我會手把手教會你這一點的」 | 「Tình dục——tình dục không phải là thứ đáng bị ghê tởm.\nEm sẽ dạy cho anh Soutetsu điều đó.」 | 「Tình dục——tình dục không phải là thứ đáng bị ghê tởm.\nEm sẽ dạy cho Soutetsu điều đó.」 | JP 双鉄に — nói với Soutetsu (old_vn là audit fix). |
| 1368 | 「ボクも、大好き、だし……これも、好きになれそう、\nかな？　双鉄の――先走りの――汁――んっ――ぺろっ」 | 「我也最喜歡你了……可能這個也可以喜歡上吧？雙鐵的――預射液――嗯――舔」 | 「Em cũng, yêu anh lắm…… và cả cái này nữa, chắc em cũng sẽ thích nó\nchứ nhỉ? Dịch――nhờn rỉ ra――của anh Soutetsu――ưm――liếm」 | 「Em cũng, yêu anh lắm…… và cả cái này nữa, chắc em cũng sẽ thích nó\nchứ nhỉ? Dịch――nhờn rỉ ra――của Soutetsu――ưm――liếm」 | JP 双鉄の — nói với Soutetsu (dịch của anh). |
| 1373 | 「わかっているよ、双鉄」 | 「我懂的，雙鐵」 | 「Em hiểu mà, anh Soutetsu.」 | 「Em hiểu mà, Soutetsu.」 | JP 双鉄 — nói với Soutetsu (old_vn là audit fix). |
| 1376 | 「ボクの気持ちとおんなじに、\nボクの体も、双鉄とくっつきあえて喜んでるんだ」 | 「我的心情很愉悅，身體也因為接觸到你而愉悅不已呢」 | 「Giống hệt như tâm trạng của em,\ncơ thể em cũng đang rất vui sướng vì được gắn kết với anh Soutetsu đấy.」 | 「Giống hệt như tâm trạng của em,\ncơ thể em cũng đang rất vui sướng vì được gắn kết với Soutetsu đấy.」 | JP 双鉄と — nói với Soutetsu (old_vn là audit fix). |
| 1380 | 「だから、怖がることはないし……\n恥ずかしがることも、遠慮をすることも無いんだ、双鉄」 | 「所以我沒什麼好怕的……不用難為情也不用顧慮什麼的，雙鐵」 | 「Vì thế, không có gì phải sợ cả……\nCũng không cần phải xấu hổ, hay ngại ngùng gì đâu, anh Soutetsu」 | 「Vì thế, không có gì phải sợ cả……\nCũng không cần phải xấu hổ, hay ngại ngùng gì đâu, Soutetsu」 | JP 双鉄 — nói với Soutetsu. |
| 1385 | 「ごめんね？　双鉄。\nちょっと、お勉強、詰め込みすぎちゃったかな」 | 「抱歉，雙鐵。好像學得有點過火了」 | 「Xin lỗi anh nhé? Anh Soutetsu.\nHình như em, nhồi nhét bài học, hơi quá tay rồi nhỉ」 | 「Xin lỗi anh nhé? Soutetsu.\nHình như em, nhồi nhét bài học, hơi quá tay rồi nhỉ」 | JP 双鉄 — xin lỗi Soutetsu. |
| 1396 | 「そうだね……ボクも、自分で知らなかったよ。\nこれも、双鉄がボクに教えてくれたことになるね」 | 「是啊……我自己以前都不知道。這又是雙鐵教會我的新知識了」 | 「Đúng vậy nhỉ…… chính em cũng không biết đâu.\nĐây cũng xem như là điều anh Soutetsu đã dạy cho em đấy」 | 「Đúng vậy nhỉ…… chính em cũng không biết đâu.\nĐây cũng xem như là điều Soutetsu đã dạy cho em đấy」 | JP 双鉄が — nói với Soutetsu (anh dạy em). |
| 1398 | 「そう……だね。ボクも、乳首が気持ちいい。\n双鉄の体に触れてる部分、全部、溶けそうに気持ちいい」 | 「是啊……是的，我的乳頭也很敏感。碰到雙鐵身體的每一處都舒服得要融化了」 | 「Đúng…… vậy. Em cũng, thấy sướng ở núm vú.\nNhững phần chạm vào cơ thể anh Soutetsu, tất cả, đều sướng đến mức như sắp tan chảy ra vậy.」 | 「Đúng…… vậy. Em cũng, thấy sướng ở núm vú.\nNhững phần chạm vào cơ thể Soutetsu, tất cả, đều sướng đến mức như sắp tan chảy ra vậy.」 | JP 双鉄の体 — nói với Soutetsu (old_vn là audit fix). |
| 1409 | 「最悪の……想像、よりは――ずうっと――楽――んっ\n……だから、双鉄――動い、て――ひゃんっ！？」 | 「比我……最壞的想像――要好――得多――嗯……所以雙鐵――動起來吧――呀嗯！？」 | 「So với…… tưởng tượng tồi tệ nhất, thì――nhẹ nhàng――hơn nhiều――ưm\n……Vậy nên, anh Soutetsu――cử động, đi――hyan!?」 | 「So với…… tưởng tượng tồi tệ nhất, thì――nhẹ nhàng――hơn nhiều――ưm\n……Vậy nên, Soutetsu――cử động, đi――hyan!?」 | JP 双鉄 — gọi Soutetsu (bảo cử động). |
| 1416 | 「いや、慣れっこさ。\n双鉄は巻き込まれただけ。首謀者は父――頭取だ」 | 「沒事，我都習慣了。你只是被捲進來的，罪魁禍首是爸爸――行長」 | 「Không sao, em quen rồi.\nAnh Soutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——tổng giám đốc ngân hàng cơ.」 | 「Không sao, em quen rồi.\nSoutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——tổng giám đốc ngân hàng cơ.」 | JP 双鉄は — nói với Soutetsu (old_vn là audit fix). |
| 1421 | 「む、無理くらいする、よ。――うぇ――えっ。\nだって、双鉄の目――んっ――飲んで、欲しいって」 | 「當、當然要逼著自己喝下去了。――唔――哎。因為你的眼睛在說話――嗯――它說想要我吞下去呢」 | 「P-Phải cố một chút chứ. ――Oẹ――e.\nTại vì, ánh mắt của anh Soutetsu――ưm――như đang muốn em nuốt nó mà」 | 「P-Phải cố một chút chứ. ――Oẹ――e.\nTại vì, ánh mắt của Soutetsu――ưm――như đang muốn em nuốt nó mà」 | JP 双鉄の目 — nói với Soutetsu. |
| 1465 | 「それは聞き捨てならないね、双鉄」 | 「這我可不能聽過就算了，雙鐵」 | 「Câu đó không thể làm ngơ được đâu nhé, anh Soutetsu.」 | 「Câu đó không thể làm ngơ được đâu nhé, Soutetsu.」 | JP 双鉄 — nói với Soutetsu. |
| 1471 | 「今度は、ボクが教える番かな――\nね？　双鉄、どこにペニスを挿れるか、わかる？」 | 「那這次當老師的得是我了――對吧？　雙鐵，你知道哪裡是陰莖插入的部位嗎？」 | 「Lần này, đến lượt em làm giáo viên nhỉ――\nNè? Anh Soutetsu, anh có biết phải đưa dương vật vào đâu không?」 | 「Lần này, đến lượt em làm giáo viên nhỉ――\nNè? Soutetsu, anh có biết phải đưa dương vật vào đâu không?」 | JP 双鉄 — hỏi Soutetsu; giữ đại từ "anh" sau tên (đó là ngôi 2, không phải xưng hô bằng tên). |
| 1473 | 「気持よく……そうか、ふふふ。\n双鉄は、気持ちよく、目覚めたんだね」 | 「醒來的感覺嗎……這樣啊，呵呵。你這麼想就好了」 | 「Tâm trạng sảng khoái…… vậy sao, fufu.\nAnh Soutetsu, thức dậy với tâm trạng sảng khoái nhỉ.」 | 「Tâm trạng sảng khoái…… vậy sao, fufu.\nSoutetsu, thức dậy với tâm trạng sảng khoái nhỉ.」 | JP 双鉄は — nói với Soutetsu. |
| 1476 | 「そ、双鉄。お、おはよう。や、やっと起きたね」 | 「雙、雙鐵，早、早安，你、你終於醒了啊」 | 「A, anh Soutetsu. Ch, chào buổi sáng. C, cuối cùng anh cũng tỉnh rồi nhỉ.」 | 「A, Soutetsu. Ch, chào buổi sáng. C, cuối cùng anh cũng tỉnh rồi nhỉ.」 | JP 双鉄 — chào buổi sáng Soutetsu. |
| 1477 | 「双鉄……キミは――――\nふふっ……ちゅっ――ちゅっ――ちゅっ」 | 「雙鐵……你啊――――呵呵……啾――啾――啾」 | 「Anh Soutetsu…… anh đúng là――――\nFufu…… chụt――chụt――chụt」 | 「Soutetsu…… anh đúng là――――\nFufu…… chụt――chụt――chụt」 | JP 双鉄……キミは — nói với Soutetsu. |
| 1478 | 「双鉄のペニスも、正直になってくれているしね」 | 「雙鐵的陰莖也懂得誠實了啊」 | 「Dương vật của anh Soutetsu, cũng đã trở nên thành thật rồi nhỉ.」 | 「Dương vật của Soutetsu, cũng đã trở nên thành thật rồi nhỉ.」 | JP 双鉄のペニス — nói với Soutetsu. |
| 1479 | 「双鉄？　起きて欲しいんだけど」 | 「雙鐵？　你該起來了吧」 | 「Anh Soutetsu? Anh nên dậy đi thôi.」 | 「Soutetsu? Anh nên dậy đi thôi.」 | JP 双鉄？ — gọi Soutetsu dậy. |
| 1480 | 「双鉄？　それ以上はちょっとヤボかな」 | 「雙鐵？　再說下去就有點敗氣氛了喔」 | 「Anh Soutetsu? Nói thêm nữa thì hơi mất hứng đấy nhé」 | 「Soutetsu? Nói thêm nữa thì hơi mất hứng đấy nhé」 | JP 双鉄？ — nói với Soutetsu. |
| 1482 | 「先走り……の……汁……んっ――ふふっ、\n双鉄のペニスは、ボクの髪のこと――好き、みたいだね」 | 「預射……液……嗯――呵呵、雙鐵的陰莖好像很喜歡――我的頭髮啊」 | 「Dịch…… nhờn rỉ ra…… ưm――fufu,\nDương vật của anh Soutetsu có vẻ――rất thích mái tóc của em nhỉ」 | 「Dịch…… nhờn rỉ ra…… ưm――fufu,\nDương vật của Soutetsu có vẻ――rất thích mái tóc của em nhỉ」 | JP 双鉄のペニス — nói với Soutetsu. |
| 2093 | （セックスのことも、その先も――\n双鉄、一緒に、一生学ぼう？） | （無論是做愛，還是未來――雙鐵，我們都一起學一輩子吧？） | （Cả chuyện tình dục, lẫn những chuyện sau này――\nAnh Soutetsu, chúng ta hãy cùng nhau học hỏi suốt đời nhé?） | （Cả chuyện tình dục, lẫn những chuyện sau này――\nSoutetsu, chúng ta hãy cùng nhau học hỏi suốt đời nhé?） | Độc thoại Kisaki hướng về Soutetsu (JP 双鉄、一緒に; các dòng kề đều là monologue). |

## 4. P4 — 稀咲h2_プライベートルーム.txt.toml (24 dòng)

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 922 | 「……は……あ…………ん。\nうん――うん。ボクも――だ――双鉄」 | 「……哈……啊…………嗯。嗯――嗯，我也――是――雙鐵」 | 「……Ha…… a………… ưm.\nỪm――ừm. Em cũng――vậy――anh Soutetsu」 | 「……Ha…… a………… ưm.\nỪm――ừm. Em cũng――vậy――Soutetsu」 | JP ボクも――だ――双鉄 — nói với Soutetsu. |
| 1116 | 「でも、さ、双鉄。ボクたちはお互いに忙しい。\n毎日は、会ってイチャイチャもできないよね？」 | 「但是雙鐵啊，我們都是大忙人。每天見了面也不能如膠似漆吧？」 | 「Nhưng mà, anh Soutetsu này. Cả hai chúng ta đều bận rộn.\nĐâu thể ngày nào cũng gặp nhau rồi âu yếm được, đúng không?」 | 「Nhưng mà, Soutetsu này. Cả hai chúng ta đều bận rộn.\nĐâu thể ngày nào cũng gặp nhau rồi âu yếm được, đúng không?」 | JP 双鉄 — gọi Soutetsu. |
| 1117 | 「でも、双鉄はセックスを知った。\n性の喜びを覚えたばかりで、きっと、毎日したくなる」 | 「但是雙鐵知道做愛的滋味了。剛體驗過性的美好，肯定每天都想嘗試」 | 「Nhưng mà, anh Soutetsu đã biết đến tình dục rồi.\nVừa mới nếm trải niềm vui sướng của tình dục, chắc chắn ngày nào anh cũng sẽ muốn làm」 | 「Nhưng mà, Soutetsu đã biết đến tình dục rồi.\nVừa mới nếm trải niềm vui sướng của tình dục, chắc chắn ngày nào anh cũng sẽ muốn làm」 | JP 双鉄は — nói với Soutetsu. |
| 1120 | 「顔……双鉄……溶けちゃってる……よ？\n……あっ――ふっ――んっ……」 | 「你的……表情……已經亂了……喔……啊――呼――嗯……」 | 「Khuôn mặt…… của anh Soutetsu…… tan chảy ra rồi…… kìa?\n……A――fu――ưm……」 | 「Khuôn mặt…… của Soutetsu…… tan chảy ra rồi…… kìa?\n……A――fu――ưm……」 | JP 双鉄 — nói với Soutetsu (mặt anh). |
| 1124 | 「来て、双鉄」 | 「來吧，雙鐵」 | 「Lại đây, anh Soutetsu」 | 「Lại đây, Soutetsu」 | JP 双鉄 — gọi Soutetsu (lại đây). |
| 1136 | 「さっき――双鉄はここを見てくれてたね。\n息を荒くして……顔も、体も赤くなってた」 | 「剛剛――雙鐵就在看這個部位吧。呼吸粗重……表情和身體都發紅的」 | 「Lúc nãy――anh Soutetsu đã nhìn vào đây nhỉ.\nHơi thở trở nên gấp gáp…… khuôn mặt, và cả cơ thể đều đỏ ửng lên」 | 「Lúc nãy――Soutetsu đã nhìn vào đây nhỉ.\nHơi thở trở nên gấp gáp…… khuôn mặt, và cả cơ thể đều đỏ ửng lên」 | JP 双鉄は — nói với Soutetsu. |
| 1166 | 「ひっ――あっ――っ――ふっ――双――て、つっ――\nんっ――ゆる――してっ――ボクっ――ボク――もうっ」 | 「咿――啊――嗚――雙――鐵――嗯――放過――我吧――我――我――不行了」 | 「Hi――a――ưm――fu――anh Sou――tetsu――\nƯm――tha――cho em――em――em――không chịu nổi nữa rồi」 | 「Hi――a――ưm――fu――Sou――tetsu――\nƯm――tha――cho em――em――em――không chịu nổi nữa rồi」 | JP 双――て、つっ — gọi tên Soutetsu trong rên; "anh Sou――tetsu" là cùng dạng xưng hô, chỉ bị gạch rên tách tên ra — bỏ "anh", giữ "Sou――tetsu" (xem Quyết định D1). |
| 1190 | 「あ……んふっ――強引だね、双鉄。\nそれほど、ボクが――」 | 「啊……嗯哼――好強硬啊，雙鐵。就這麼想和我――」 | 「A…… ưm fu――Anh mạnh bạo quá đấy, anh Soutetsu.\nĐến mức đó, em đã――」 | 「A…… ưm fu――Anh mạnh bạo quá đấy, Soutetsu.\nĐến mức đó, em đã――」 | JP 双鉄 — nói với Soutetsu. |
| 1193 | 「あ……すごい……双鉄――双鉄が、\nボクで、オナニー……ん……して、くれて、る……」 | 「啊……好厲害……雙鐵――雙鐵，在想著我而自慰……嗯……」 | 「A…… tuyệt quá…… anh Soutetsu――anh Soutetsu đang,\nthủ dâm…… vì em…… ưm…… vì em……」 | 「A…… tuyệt quá…… Soutetsu――Soutetsu đang,\nthủ dâm…… vì em…… ưm…… vì em……」 | JP 双鉄――双鉄が (×2) — nói với Soutetsu; cả 2 lần đều bỏ "anh". |
| 1205 | 「んっ――はっ――あっ――双っ――鉄っ――」 | 「嗯――哈――啊――雙――鐵――」 | 「Ưm――ha――a――anh Sou――tetsu――」 | 「Ưm――ha――a――Sou――tetsu――」 | JP 双っ――鉄っ — gọi tên Soutetsu trong rên; như 1166 (xem D1). |
| 1223 | 「うん！　双鉄っ――双鉄、もも――って、え？」 | 「嗯！　雙鐵――雙鐵也是――哎？」 | 「Vâng! Anh Soutetsu――Anh Soutetsu, cũng――ơ, hả?」 | 「Vâng! Soutetsu――Soutetsu, cũng――ơ, hả?」 | JP 双鉄っ――双鉄 (×2) — gọi Soutetsu; cả 2 lần đều bỏ "anh". |
| 1243 | 「そうだよ、だから……\n今までもボクは双鉄に、わざとパンツや胸元を見せてた」 | 「對啊，所以呢……我才三番兩次地讓你看到胸部和內褲」 | 「Đúng vậy, cho nên……\nTừ trước đến nay em cũng đã cố tình để lộ quần lót và vòng ngực cho anh Soutetsu thấy đó」 | 「Đúng vậy, cho nên……\nTừ trước đến nay em cũng đã cố tình để lộ quần lót và vòng ngực cho Soutetsu thấy đó」 | JP 双鉄に — nói với Soutetsu. |
| 1246 | 「ヴァギナ、は……双鉄に、開けられる……まで……\nんっ――自分で――イジって――なかった――けどっ」 | 「小穴……在被你打開……之前……嗯――我就沒有――玩弄過――它――一下」 | 「Vagina, thì…… cho đến khi…… được anh Soutetsu, mở ra……\nƯm――em chưa từng――tự mình――đụng chạm――vào nó――đâu」 | 「Vagina, thì…… cho đến khi…… được Soutetsu, mở ra……\nƯm――em chưa từng――tự mình――đụng chạm――vào nó――đâu」 | JP 双鉄に — nói với Soutetsu. |
| 1260 | 「ボク……一回、イっとかない――と――んっ――\n双鉄に、今、挿れられ、たら――狂っちゃ――からっ」 | 「我……一定要先高潮――一下――嗯――要是直接給你插進來――會壞掉――的」 | 「Em…… phải ra, một lần――đã――ưm――\nNếu để anh Soutetsu, đưa vào ngay bây giờ, thì――em sẽ phát điên――mất」 | 「Em…… phải ra, một lần――đã――ưm――\nNếu để Soutetsu, đưa vào ngay bây giờ, thì――em sẽ phát điên――mất」 | JP 双鉄に — nói với Soutetsu. |
| 1268 | 「ボクは観察してたから。今日の双鉄は、\nパンツを見せたらどんな反応をしてくれるかって」 | 「我在觀察你啊，我想知道今天讓你看到內褲會有什麼反應呢」 | 「Bởi vì em đã quan sát anh mà. Rằng hôm nay anh Soutetsu,\nsẽ phản ứng thế nào nếu em cho anh xem quần lót của em」 | 「Bởi vì em đã quan sát anh mà. Rằng hôm nay Soutetsu,\nsẽ phản ứng thế nào nếu em cho anh xem quần lót của em」 | JP 双鉄は — nói với Soutetsu. |
| 1284 | 「だから嬉しい。双鉄が今日は気づいてくれて。\nボクを欲しがってくれていて」 | 「所以我才高興啊，你今天終於注意到了。終於對我有欲望了」 | 「Vì thế nên em mới vui. Vì hôm nay anh Soutetsu đã nhận ra.\nVà khao khát em」 | 「Vì thế nên em mới vui. Vì hôm nay Soutetsu đã nhận ra.\nVà khao khát em」 | JP 双鉄が — nói với Soutetsu. |
| 1286 | 「だから、双鉄に教えてあげる。一人でも出来るセックス。\nボクのことを想いながらの、オナニーのやり方を」 | 「所以我要教教雙鐵，什麼是一個人能做的愛。如何一邊腦海裡想著我，一邊自慰」 | 「Vì vậy, em sẽ dạy cho anh Soutetsu. Cách làm tình có thể thực hiện một mình.\nCách thủ dâm, trong khi nghĩ về em」 | 「Vì vậy, em sẽ dạy cho Soutetsu. Cách làm tình có thể thực hiện một mình.\nCách thủ dâm, trong khi nghĩ về em」 | JP 双鉄に — nói với Soutetsu (dạy anh). |
| 1299 | 「そうだね。実に、双鉄らしい部屋だ。\nま、お金の使い方からも想像はついていたけれど」 | 「是啊，真的很有你的風格。雖然從你的開銷上，我已經猜到會是這樣的了」 | 「Đúng vậy. Quả thực là một căn phòng rất mang phong cách của anh Soutetsu.\nMà, nhìn vào cách anh tiêu tiền thì em cũng đoán được phần nào rồi」 | 「Đúng vậy. Quả thực là một căn phòng rất mang phong cách của Soutetsu.\nMà, nhìn vào cách anh tiêu tiền thì em cũng đoán được phần nào rồi」 | JP 双鉄らしい部屋だ — nói với Soutetsu về phòng của anh. |
| 1325 | 「そう……だよ……会えない、ときとか、は……んっ、\nボク、も――双鉄を、思って――オナニー、する、よ？」 | 「當然……會啊……比如見不到你的時候……嗯，我也――會想著你――然後自慰的哦？」 | 「Đúng…… vậy đó…… những lúc, không gặp được anh, thì…… ưm,\nEm, cũng――nghĩ về anh Soutetsu――và thủ dâm, đó?」 | 「Đúng…… vậy đó…… những lúc, không gặp được anh, thì…… ưm,\nEm, cũng――nghĩ về Soutetsu――và thủ dâm, đó?」 | JP 双鉄を — nói với Soutetsu. |
| 1359 | 「貴重な機会だからこそ、双鉄の部屋をじっくりたっぷり\n見たかったのさ。部屋は、その人の表れだから」 | 「趁著寶貴的機會，我才想仔仔細細看遍你房間的每一個角落啊。房間可以體現出一個人嘛」 | 「Chính vì là cơ hội quý giá, nên em mới muốn ngắm nghía thật kỹ\ncăn phòng của anh Soutetsu. Bởi vì căn phòng chính là tấm gương phản chiếu con người mà」 | 「Chính vì là cơ hội quý giá, nên em mới muốn ngắm nghía thật kỹ\ncăn phòng của Soutetsu. Bởi vì căn phòng chính là tấm gương phản chiếu con người mà」 | JP 双鉄の部屋 — nói với Soutetsu. |
| 1374 | 「それなら。\n安心して双鉄に教えてあげられる、かな？」 | 「那好吧。我可以放心地教一教雙鐵了吧？」 | 「Nếu vậy thì.\nEm có thể yên tâm dạy cho anh Soutetsu rồi, nhỉ?」 | 「Nếu vậy thì.\nEm có thể yên tâm dạy cho Soutetsu rồi, nhỉ?」 | JP 双鉄に — nói với Soutetsu. |
| 1382 | 「双鉄――イって！！　ボク、ボクっ――んっ！」 | 「雙鐵――射吧！！　我、我――嗯！」 | 「Anh Soutetsu――ra đi!! Em, em――ưm!」 | 「Soutetsu――ra đi!! Em, em――ưm!」 | JP 双鉄 — gọi Soutetsu (bảo ra). |
| 1384 | 「双鉄……なんでオナニー、止めているのさ」 | 「雙鐵……你為什麼自慰停下來了啊」 | 「Anh Soutetsu…… sao anh lại dừng thủ dâm rồi」 | 「Soutetsu…… sao anh lại dừng thủ dâm rồi」 | JP 双鉄 — hỏi Soutetsu. |
| 1386 | 「甘えん坊で、正直者だね。双鉄は。\nおちんちん、ここに[い]挿れたいんだよね？」 | 「雙鐵真愛撒嬌，也好誠實啊。你很想把小雞雞插進這裡來是吧？」 | 「Anh Soutetsu đúng là, thích làm nũng và thật thà nhỉ.\nAnh muốn đưa chim vào đây đúng không?」 | 「Soutetsu đúng là, thích làm nũng và thật thà nhỉ.\nAnh muốn đưa chim vào đây đúng không?」 | JP 双鉄は — nói với Soutetsu. |

## 5. P4 — 稀咲h3_チャイナドレスでおもてなし.txt.toml (45 dòng)

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1540 | 「――うん。確かに。\nボクの夢はいつの間にか、双鉄の夢と重なったよね」 | 「――嗯，是啊。我的夢不知不覺就跟你的夢重疊在了一起」 | 「――Ừm. Đúng vậy thật.\nƯớc mơ của em từ lúc nào, đã hòa làm một với ước mơ của anh Soutetsu rồi nhỉ」 | 「――Ừm. Đúng vậy thật.\nƯớc mơ của em từ lúc nào, đã hòa làm một với ước mơ của Soutetsu rồi nhỉ」 | JP 双鉄の夢 — nói với Soutetsu về ước mơ của anh. |
| 1587 | 「……双鉄」 | 「……雙鐵」 | 「……Anh Soutetsu」 | 「……Soutetsu」 | JP 双鉄 — gọi Soutetsu. |
| 1969 | 「妹さんと双鉄の、きっと、日常のひとこまだった。\nそういう距離を、あたたかさを、感じた気がした」 | 「一定是妹妹和雙鐵最平凡的互動之一了。我能感受到，我們之間的距離已經那麼近、關係已經那麼溫暖了」 | 「Đó chắc chắn là một khoảnh khắc thường ngày giữa anh Soutetsu và em gái.\nEm có cảm giác như mình đã chạm đến được khoảng cách đó, sự ấm áp đó」 | 「Đó chắc chắn là một khoảnh khắc thường ngày giữa Soutetsu và em gái.\nEm có cảm giác như mình đã chạm đến được khoảng cách đó, sự ấm áp đó」 | JP 妹さんと双鉄の — nói với Soutetsu về kỷ niệm của anh với em gái (người nghe là Soutetsu; không phải ngôi ba với người khác). |
| 1994 | 「無理じゃないよ？　双鉄が必ず。覚えてるから。\n今は例え、心のどこかに、閉じ込めてても」 | 「並不是不可能哦？　你肯定也記得的。就算現在還封閉在心底裡」 | 「Không phải là không thể đâu? Anh Soutetsu chắc chắn. Vẫn còn nhớ mà.\nCho dù hiện tại, nó đang bị nhốt ở một góc nào đó trong trái tim anh」 | 「Không phải là không thể đâu? Soutetsu chắc chắn. Vẫn còn nhớ mà.\nCho dù hiện tại, nó đang bị nhốt ở một góc nào đó trong trái tim anh」 | JP 双鉄が必ず — nói với Soutetsu. |
| 2003 | 「乳首……双鉄、に……なでられ――て……っ……\nそれだけ、で――こんなに、あつく――かたく――」 | 「乳頭……在雙鐵……的撫摸下……就會――這麼熾熱――這麼堅挺――」 | 「Đầu vú…… được, anh Soutetsu…… vuốt ve――……Ư\nChỉ cần vậy, thôi――đã nóng ran――và cứng lại, thế này――」 | 「Đầu vú…… được, Soutetsu…… vuốt ve――……Ư\nChỉ cần vậy, thôi――đã nóng ran――và cứng lại, thế này――」 | JP 双鉄、に — nói với Soutetsu (old_vn là audit fix). |
| 2041 | 「けど、双鉄は」 | 「但是雙鐵呢」 | 「Nhưng mà, anh Soutetsu thì sao」 | 「Nhưng mà, Soutetsu thì sao」 | JP 双鉄は — hỏi Soutetsu. |
| 2053 | 「理性。しっかり保ってるよね？\n双鉄の理性を壊せるほどには、魅力、無い？」 | 「你好像還保持著理智呢？我沒有足夠的魅力破壞你的理智嗎？」 | 「Lý trí. Anh vẫn đang giữ vững đúng không?\nChẳng lẽ em không đủ sức hấp dẫn, để phá vỡ lý trí của anh Soutetsu sao?」 | 「Lý trí. Anh vẫn đang giữ vững đúng không?\nChẳng lẽ em không đủ sức hấp dẫn, để phá vỡ lý trí của Soutetsu sao?」 | JP 双鉄の理性 — nói với Soutetsu. |
| 2070 | 「シニヨンを見て、かわいいって！\n双鉄だなってすごく思って、嬉しくて」 | 「你看著髮髻會覺得超可愛！這一點特別有雙鐵的感覺，我聽了也很高興」 | 「Nhìn kiểu tóc búi chignon của em, anh khen đáng yêu!\nEm thấy đúng chuẩn anh Soutetsu luôn, nên em vui lắm」 | 「Nhìn kiểu tóc búi chignon của em, anh khen đáng yêu!\nEm thấy đúng chuẩn Soutetsu luôn, nên em vui lắm」 | JP 双鉄だなって — nói với Soutetsu (đúng chuẩn anh). |
| 2185 | 「うふふっ、いいよ？\nそれならボクは、双鉄をクッションにしちゃうから」 | 「呵呵，好啊。我就拿雙鐵當彈簧墊吧」 | 「Ufufu, được thôi?\nNếu vậy em sẽ lấy anh Soutetsu làm gối nệm đấy」 | 「Ufufu, được thôi?\nNếu vậy em sẽ lấy Soutetsu làm gối nệm đấy」 | JP 双鉄をクッションに — nói với Soutetsu. |
| 2187 | 「ふふ、そうだね……っ――双鉄の精液だから……\nおぼれないよう……ちゃんと、優しくしてくれるしね」 | 「呵呵，是啊……――那是雙鐵的精液啊……一定會很溫柔的……不會悶著她的」 | 「Fufu, đúng nhỉ……――Vì là tinh dịch của anh Soutetsu……\nChắc chắn sẽ dịu dàng……để không bị chết đuối nhỉ」 | 「Fufu, đúng nhỉ……――Vì là tinh dịch của Soutetsu……\nChắc chắn sẽ dịu dàng……để không bị chết đuối nhỉ」 | JP 双鉄の精液 — nói với Soutetsu. |
| 2191 | 「あれ？　意外。\n双鉄はあまり、パーティーに出る方では無かった？」 | 「咦？真讓我意外，難道你平時很少出席宴會之類的嗎？」 | 「Ủa? Bất ngờ thật đấy.\nAnh Soutetsu không hay tham gia các buổi tiệc tùng sao?」 | 「Ủa? Bất ngờ thật đấy.\nSoutetsu không hay tham gia các buổi tiệc tùng sao?」 | JP 双鉄は — hỏi Soutetsu. |
| 2193 | 「あれあれ？　双鉄は残念そうだね」 | 「咦？聽你的口氣好像挺遺憾的啊」 | 「Ủa ủa? Trông anh Soutetsu có vẻ tiếc nuối nhỉ」 | 「Ủa ủa? Trông Soutetsu có vẻ tiếc nuối nhỉ」 | JP 双鉄は — nói với Soutetsu. |
| 2203 | 「は……んっ――ふ、ぁ……手……双鉄の、手――\nあったか――ふっ……はぁ……はふっ」 | 「哈……嗯――呼、啊……手……雙鐵的手――熱呼呼的――呼……蛤啊……哈呼」 | 「Ha…… ưm――Fu, a…… tay…… tay của, anh Soutetsu――\nấm quá――fu…… ha…… ha fu」 | 「Ha…… ưm――Fu, a…… tay…… tay của, Soutetsu――\nấm quá――fu…… ha…… ha fu」 | JP 双鉄の、手 — nói với Soutetsu. |
| 2211 | 「え？　あ――いや、ね？　その……\n双鉄も少し、酔ってくれてるのかな？　とか思ってさ」 | 「哎？　啊――沒什麼啦，只是……雙鐵好像也有點醉了吧？」 | 「Hả? À――không, chỉ là? Chuyện đó……\nEm đang nghĩ, liệu có phải anh Soutetsu cũng hơi say rồi không?」 | 「Hả? À――không, chỉ là? Chuyện đó……\nEm đang nghĩ, liệu có phải Soutetsu cũng hơi say rồi không?」 | JP 双鉄も — nói với Soutetsu. |
| 2246 | 「ああ、そうだったっけ。\n双鉄には貫禄があるから、ついつい、ね」 | 「啊，對哦。看你總是威風凜凜的，總是不由自主就那麼想了」 | 「À, đúng rồi nhỉ.\nTại anh Soutetsu có phong thái chững chạc quá, nên em cứ vô tình nghĩ vậy」 | 「À, đúng rồi nhỉ.\nTại Soutetsu có phong thái chững chạc quá, nên em cứ vô tình nghĩ vậy」 | JP 双鉄には貫禄がある — nói với Soutetsu. |
| 2248 | 「やっ――双鉄、そんな恥ずかしいことっ」 | 「喂――雙鐵，別說得這麼色嘛」 | 「Này――anh Soutetsu, đừng nói chuyện đáng xấu hổ như thế」 | 「Này――Soutetsu, đừng nói chuyện đáng xấu hổ như thế」 | JP 双鉄 — gọi Soutetsu. |
| 2250 | 「双鉄を好きになって。双鉄と恋ができて。\n本当に幸せで――ただ、それだけだよ」 | 「喜歡上你，和你交往，我很幸福――就這麼簡單」 | 「Thích anh Soutetsu. Yêu anh Soutetsu.\nThực sự rất hạnh phúc――chỉ vậy thôi」 | 「Thích Soutetsu. Yêu Soutetsu.\nThực sự rất hạnh phúc――chỉ vậy thôi」 | JP 双鉄を好きになって。双鉄と恋ができて (×2) — nói với Soutetsu; cả 2 lần đều bỏ "anh". |
| 2254 | 「ふあっ！　ペニスっ――すごい――双鉄っ――\nこんなに、硬くっ――て――ふ、あっ――熱いっ」 | 「嗚啊！　陰莖――好棒――雙鐵――已經這麼硬了――呼、啊――好熱」 | 「Fua! Dương vật――tuyệt quá――anh Soutetsu――\nCứng――như thế này――phu, á――nóng quá」 | 「Fua! Dương vật――tuyệt quá――Soutetsu――\nCứng――như thế này――phu, á――nóng quá」 | JP 双鉄っ — gọi Soutetsu (old_vn là moan fix). |
| 2296 | 「うん。双鉄を、誰にも取られたくないからね」 | 「嗯，這樣你才不會被人搶走」 | 「Ừm. Vì em không muốn anh Soutetsu bị ai khác cướp mất đâu」 | 「Ừm. Vì em không muốn Soutetsu bị ai khác cướp mất đâu」 | JP 双鉄を — nói với Soutetsu. |
| 2326 | 「いいね！　双鉄。それでいこう。\nそうだよ、ボクたちは正式な婚約者なんだから」 | 「好啊！　雙鐵。我們走吧。這就對了，我們已經是正式的未婚夫妻了」 | 「Hay đấy! Anh Soutetsu. Cứ quyết định vậy đi.\nĐúng rồi, chúng ta đã là hôn phu hôn thê chính thức của nhau rồi mà」 | 「Hay đấy! Soutetsu. Cứ quyết định vậy đi.\nĐúng rồi, chúng ta đã là hôn phu hôn thê chính thức của nhau rồi mà」 | JP 双鉄 — gọi Soutetsu. |
| 2327 | 「いいよ？　なら見せてあげる。\n行こ？　双鉄」 | 「好啊，我穿給你看。走吧？　雙鐵」 | 「Được thôi? Vậy em sẽ cho anh xem.\nĐi nào? Anh Soutetsu」 | 「Được thôi? Vậy em sẽ cho anh xem.\nĐi nào? Soutetsu」 | JP 双鉄 — gọi Soutetsu (đi nào). |
| 2360 | 「おまん、こ――いっぱい――ぜんぶ、双鉄っ――\nそうてつ、の、――おちんちん、にぃっ――ふあっ！」 | 「小穴――都是――都是雙鐵――雙鐵的――小雞雞――嗚啊！」 | 「Âm đạo――đầy ắp――tất cả, anh Soutetsu――\ndương vật, của, ――anh Soutetsu――Fua!」 | 「Âm đạo――đầy ắp――tất cả, Soutetsu――\ndương vật, của, ――Soutetsu――Fua!」 | JP 双鉄っ――そうてつ、の (×2) — nói với Soutetsu (old_vn là moan fix); cả 2 lần đều bỏ "anh". |
| 2388 | 「なんだい双鉄」 | 「怎麼了，雙鐵」 | 「Sao thế anh Soutetsu」 | 「Sao thế Soutetsu」 | JP 双鉄 — hỏi Soutetsu (sao thế). |
| 2390 | 「そんなの！　双鉄が構わないなら、構わないよ？\nこのドレスは、双鉄にしか見せないものだし」 | 「怎麼會呢！　只要你不介意，我也不介意啦。只有雙鐵見過這件旗袍啊」 | 「Chuyện đó! Nếu anh Soutetsu không bận tâm thì em cũng không sao đâu?\nBộ váy này, em chỉ cho một mình anh Soutetsu xem thôi mà」 | 「Chuyện đó! Nếu Soutetsu không bận tâm thì em cũng không sao đâu?\nBộ váy này, em chỉ cho một mình Soutetsu xem thôi mà」 | JP 双鉄が / 双鉄にしか (×2) — nói với Soutetsu; cả 2 lần đều bỏ "anh". |
| 2407 | 「ボクもだ双鉄。わかったよ。ふたりで求め合う方が、\n一方的に求められるより、ずっと幸せで気持ちいい」 | 「我也是，雙鐵，我明白。兩個人互相纏綿，比單方面地被索取，要幸福快樂得多」 | 「Em cũng vậy, anh Soutetsu. Em hiểu rồi. Hai người cùng khao khát nhau,\nsẽ hạnh phúc và sướng hơn nhiều so với việc bị đòi hỏi một chiều」 | 「Em cũng vậy, Soutetsu. Em hiểu rồi. Hai người cùng khao khát nhau,\nsẽ hạnh phúc và sướng hơn nhiều so với việc bị đòi hỏi một chiều」 | JP 双鉄 — nói với Soutetsu. |
| 2422 | 「双鉄に、思い切り好きにして欲しいんだ。\n双鉄のしたい、セックスを」 | 「我就想雙鐵能對我為所欲為呢。想試試雙鐵心目中的性愛」 | 「Em muốn anh Soutetsu, cứ thoải mái làm theo ý mình.\nLàm tình, theo cách mà anh Soutetsu muốn」 | 「Em muốn Soutetsu, cứ thoải mái làm theo ý mình.\nLàm tình, theo cách mà Soutetsu muốn」 | JP 双鉄に / 双鉄のしたい (×2) — nói với Soutetsu; cả 2 lần đều bỏ "anh". |
| 2426 | 「知りたいんだ。双鉄は、ボクの外観だけでも――\nボクを好きになって、興奮してくれるのかなって」 | 「我很想知道，雙鐵能不能只對我的外表就能喜歡上我，就能興奮起來呢」 | 「Em muốn biết. Liệu anh Soutetsu, chỉ cần vẻ bề ngoài của em thôi――\ncũng có thể yêu thích em, và cảm thấy hưng phấn không」 | 「Em muốn biết. Liệu Soutetsu, chỉ cần vẻ bề ngoài của em thôi――\ncũng có thể yêu thích em, và cảm thấy hưng phấn không」 | JP 双鉄は — nói với Soutetsu. |
| 2432 | 「頑張ってるから。\n双鉄のためにも、自分のためにも」 | 「我很用心的。為了你，也為了自己」 | 「Vì em đã rất cố gắng mà.\nVì anh Soutetsu, và cũng vì chính bản thân em nữa」 | 「Vì em đã rất cố gắng mà.\nVì Soutetsu, và cũng vì chính bản thân em nữa」 | JP 双鉄のためにも — nói với Soutetsu. |
| 2437 | 「ボクにとって最高の式は、\n新郎席に、双鉄がいてくれるだけで作れるよ？」 | 「我心目中最棒的婚禮，只要雙鐵站在新郎席上就好了哦？」 | 「Đối với em, một hôn lễ tuyệt vời nhất,\nchỉ cần có anh Soutetsu đứng ở vị trí chú rể là đủ rồi mà?」 | 「Đối với em, một hôn lễ tuyệt vời nhất,\nchỉ cần có Soutetsu đứng ở vị trí chú rể là đủ rồi mà?」 | JP 新郎席に、双鉄が — nói với Soutetsu. |
| 2465 | 「普通は、体を見ると思う。男でも、女でさえも。\nでも、双鉄は真っ先にボクの顔を見て――うふふっ」 | 「我覺得一般人都會瞅著身體看，無論男女。但是你就只盯著我的臉看――呵呵」 | 「Bình thường thì, người ta sẽ nhìn vào cơ thể. Dù là đàn ông, hay thậm chí là phụ nữ.\nNhưng mà, anh Soutetsu lại nhìn vào mặt em đầu tiên――ufufu」 | 「Bình thường thì, người ta sẽ nhìn vào cơ thể. Dù là đàn ông, hay thậm chí là phụ nữ.\nNhưng mà, Soutetsu lại nhìn vào mặt em đầu tiên――ufufu」 | JP 双鉄は — nói với Soutetsu. |
| 2468 | 「『飲ませてくれる』んじゃないのかい？\n双鉄が、ボクに」 | 「我說了，要『給我喝』的啊，忘了嗎？要由你餵我喝」 | 「Chẳng phải anh bảo là 『cho em uống』 sao?\nAnh Soutetsu, cho em」 | 「Chẳng phải anh bảo là 『cho em uống』 sao?\nSoutetsu, cho em」 | JP 双鉄が、ボクに — nói với Soutetsu (old_vn là audit fix). |
| 2556 | 「いいや。双鉄だなぁって思ってさ。\n嬉しくって、愛しくって。それでつい、ね」 | 「沒有，感覺這才是你嘛。高興啊，疼愛啊，然後就會…你懂的」 | 「Không đâu. Em chỉ nghĩ, đúng là anh Soutetsu có khác.\nVui quá, đáng yêu quá. Nên em lỡ cười thôi」 | 「Không đâu. Em chỉ nghĩ, đúng là Soutetsu có khác.\nVui quá, đáng yêu quá. Nên em lỡ cười thôi」 | JP 双鉄だなぁって — nói với Soutetsu. |
| 2656 | 「それに――ボクは、ボクはね？　双鉄」 | 「而且――你知道嗎，我呢……」 | 「Hơn nữa――em, em này? Anh Soutetsu」 | 「Hơn nữa――em, em này? Soutetsu」 | JP 双鉄 — gọi Soutetsu. |
| 2666 | 「時間をかけて、思い出してよ。\nボクは必ず、その味を双鉄に食べさせてあげる」 | 「花時間慢慢回憶吧。我一定會做出那個味道讓你品嘗的」 | 「Hãy dành thời gian, để nhớ lại đi nhé.\nEm nhất định, sẽ nấu lại hương vị đó cho anh Soutetsu ăn」 | 「Hãy dành thời gian, để nhớ lại đi nhé.\nEm nhất định, sẽ nấu lại hương vị đó cho Soutetsu ăn」 | JP 双鉄に — nói với Soutetsu. |
| 2726 | 「それは――双鉄。それは、凄く嬉しい……ん――\nだけ、どっ……」 | 「這個――雙鐵，我聽了是很高興……嗯――但是……」 | 「Chuyện đó――anh Soutetsu. Nghe vậy, em rất vui…… ưm――\nnhưng, mà……」 | 「Chuyện đó――Soutetsu. Nghe vậy, em rất vui…… ưm――\nnhưng, mà……」 | JP 双鉄 — gọi Soutetsu. |
| 2731 | 「ボクが、双鉄の日常になれた瞬間だもの。\n見せびらかすより、ふたりだけのヒミツにしたい」 | 「這是我走入雙鐵日常的一瞬間啊。我想留作我們之間的秘密，可不想到處炫耀呀」 | 「Đó là khoảnh khắc em trở thành một phần cuộc sống thường ngày của anh Soutetsu mà.\nThay vì khoe khoang, em muốn giữ nó làm bí mật của riêng hai chúng ta hơn」 | 「Đó là khoảnh khắc em trở thành một phần cuộc sống thường ngày của Soutetsu mà.\nThay vì khoe khoang, em muốn giữ nó làm bí mật của riêng hai chúng ta hơn」 | JP 双鉄の日常 — nói với Soutetsu về cuộc sống thường ngày của anh. |
| 2732 | 「双鉄が飲ませてくれたからね？\n最高に甘くて美味しかった……といいたいけれど」 | 「這是雙鐵餵給我喝的，所以甜蜜極了、美味極了……以上只是我美好的預想」 | 「Vì là anh Soutetsu cho em uống mà?\nNên em rất muốn nói là nó ngọt ngào và ngon tuyệt vời…… nhưng mà」 | 「Vì là Soutetsu cho em uống mà?\nNên em rất muốn nói là nó ngọt ngào và ngon tuyệt vời…… nhưng mà」 | JP 双鉄が飲ませてくれた — nói với Soutetsu. |
| 2739 | 「ここが、双鉄の家だから」 | 「這裡是雙鐵的家」 | 「Bởi vì nơi này, là nhà của anh Soutetsu」 | 「Bởi vì nơi này, là nhà của Soutetsu」 | JP 双鉄の家 — nói với Soutetsu. |
| 2750 | 「つまり、見たいんだね？\n双鉄は、ボクの、チャイナドレスが」 | 「那你就是想看囉？想看我穿旗袍的樣子」 | 「Tóm lại là, anh muốn xem đúng không?\nAnh Soutetsu, muốn xem em mặc, sườn xám」 | 「Tóm lại là, anh muốn xem đúng không?\nSoutetsu, muốn xem em mặc, sườn xám」 | JP 双鉄は、ボクの、チャイナドレスが — hỏi Soutetsu. |
| 2753 | 「覚えておいて？　双鉄。民族衣装は、\n“自国のもの”しか、礼服としては扱えないよ？」 | 「那你記好了哦？　雙鐵。民族服飾只有“自己國家的人”才能穿在身上當禮服喔？」 | 「Anh nhớ kỹ nhé? Anh Soutetsu. Trang phục truyền thống,\nchỉ có “của nước mình” thì mới được coi là lễ phục thôi đó?」 | 「Anh nhớ kỹ nhé? Soutetsu. Trang phục truyền thống,\nchỉ có “của nước mình” thì mới được coi là lễ phục thôi đó?」 | JP 双鉄 — gọi Soutetsu. |
| 2781 | 「なら、双鉄の理性は、さ――」 | 「那雙鐵的理智已經――」 | 「Vậy thì, lý trí của anh Soutetsu, đã――」 | 「Vậy thì, lý trí của Soutetsu, đã――」 | JP 双鉄の理性 — nói với Soutetsu. |
| 2793 | 「双鉄の――[そごう,1]十川の家の味だから」 | 「雙鐵的――十川家的味道啦」 | 「Hương vị của nhà Sogou――gia đình của anh Soutetsu cơ」 | 「Hương vị của nhà Sogou――gia đình của Soutetsu cơ」 | JP 双鉄の――十川の家の味 — nói với Soutetsu về vị nhà Sogou của anh. |
| 2794 | 「双鉄、ね？　指しゃぶりなんて、してないで」 | 「雙鐵，不要含手指頭喔」 | 「Anh Soutetsu này? Đừng có mút ngón tay nữa」 | 「Soutetsu này? Đừng có mút ngón tay nữa」 | JP 双鉄、ね？ — gọi Soutetsu. |
| 2795 | 「双鉄。着たよ？」 | 「雙鐵，我們到了」 | 「Anh Soutetsu. Em mặc xong rồi nè?」 | 「Soutetsu. Em mặc xong rồi nè?」 | JP 双鉄 — gọi Soutetsu. |
| 2796 | 「双鉄、食べる？\nチーズクリーム、気にいったみたいだったから」 | 「雙鐵，要嚐嚐嗎？你好像挺喜歡奶油乳酪的」 | 「Anh Soutetsu, ăn không?\nCó vẻ anh khá thích kem phô mai mà」 | 「Soutetsu, ăn không?\nCó vẻ anh khá thích kem phô mai mà」 | JP 双鉄、食べる？ — hỏi Soutetsu. |

## 3. Giữ nguyên / đã kiểm chứng nhưng KHÔNG sửa

- **稀咲h3 2195 — GIỮ:** Kisaki nói, JP 「そうっ――てつ――すきっ――すき――すきぃ」, giá trị hiện tại (moan fix) là 「Hia――á――á――Fua――á á――\nSou――tetsu――yêu anh――yêu anh――yêu anh」 — tên đã ở dạng trần "Sou――tetsu" (chỉ tách bằng gạch rên), không có "anh" trước tên. P4 đã thỏa; không đụng. (Đại từ "anh" trong "yêu anh" là ngôi 2, không phải xưng hô bằng tên — giữ.)
- **稀咲02 2376 — KHÔNG PHẢI Kisaki (đã sửa trong audit):** người nói là 日々姫 (Hibiki), JP 「にぃにっ――兄さん？」 ("anh hai"), VN CSV3 là 「Anh hai——anh Soutetsu?」 nhưng audit đã sửa thành 「Anh hai——anh trai?」 — giá trị hiện tại không còn "anh Soutetsu". Không đụng.
- **稀咲03 2137 — KHÔNG PHẢI Kisaki:** người nói là れいな (Reina): 「Anh Soutetsu và chị Kisaki, sắp kết hôn rồi đúng không ạ!\nThật sự, xin chúc mừng hai người nha!」 — Reina DÙNG "anh Soutetsu" là đúng (cô ấy gọi Soutetsu là "anh"). Không đụng.
- **Folder 03_Paulette (file không lr) — 0 dòng:** quét cả VN CSV3 thô lẫn giá trị hiện tại đều không có dòng nào Kisaki nói "anh Soutetsu". Các dòng Kisaki "anh Soutetsu" của route Paulette nằm trong file lr (`lr_稀咲ポーレットh1`, 31 dòng) — thuộc U7b.
- **Đại từ "anh" ngôi 2 của Kisaki — GIỮ khắp nơi:** Kisaki gọi Soutetsu là "anh" ở vị trí đại từ (vd. h1 1471 "Soutetsu, anh có biết…", h2 1268 "nếu em cho anh xem…", h3 2750 "Anh Soutetsu, muốn xem…" → "Soutetsu, muốn xem…") là cách xưng hô ngôi 2 bình thường, KHÔNG phải dạng "anh Soutetsu" mà P4 cấm. Chỉ bỏ "anh" khi nó đứng ngay trước tên "Soutetsu"; các "anh" khác trong cùng dòng được giữ nguyên.
- **Cờ U6 Grand 08 key 1702 — KIỂM CHỨNG, KHÔNG CÓ GÌ ĐỂ SỬA CHO P4 (nợ coordinator — xem §5):** tra toàn bộ CSV3: key 1702 của グランドリライト08_ふかみ.txt.toml ở good-set (09_Grand) là Kisaki nói, JP 「キミは、それで――」, VN 「Cậu, như vậy thì――」 — KHÔNG chứa "anh Soutetsu". Batch sau (09_Grand) KHÔNG cần sửa dòng này cho P4. (Dòng cùng key ở stale-set 07_Nagi_Fukami là một dòng khác hẳn — Paulette nói 「――Yên tâm đi, Kisaki. Cậu Soutetsu.」 — thuộc tập stale đã loại, không đụng.)

## 4. Quyết định (theo uỷ quyền của Hieu — điều tra JP+TW+ngữ cảnh rồi quyết, không park)

- **D1 — 2 dòng rên tách tên "anh Sou――tetsu" (稀咲h2 1166/1205) ĐƯỢC ĐƯA VÀO batch:** cùng dạng xưng hô "anh Soutetsu", chỉ bị các gạch rên tách tên ra (VN "anh Sou――tetsu", JP cũng tách tên tương ứng: 双――て、つっ / 双っ――鉄っ; TW 雙――鐵). Fix chỉ bỏ "anh " và giữ nguyên "Sou――tetsu" (kể cả gạch nối và nhịp rên). Nếu bỏ qua, Kisaki vẫn gọi "anh Sou――tetsu" trong bản rebuild — P4 áp dụng dở dang. Dòng tương tự h3 2195 ("Sou――tetsu" không có "anh") đã đúng nên giữ (xem §3).
- **D2 — Tiêu chí người nghe (không phải vai trò ngữ pháp):** sửa khi "anh Soutetsu" chỉ Soutetsu với tư cách NGƯỜI NGHE — kể cả khi nó đứng ở vị trí chủ ngữ/sở hữu trong câu nói với anh (vd. 1956 "một phần nào đó trong anh Soutetsu", JP キミ; 1969 "giữa anh Soutetsu và em gái", 2731 "cuộc sống thường ngày của anh Soutetsu", 2793 "gia đình của anh Soutetsu" — đều là Kisaki nói VỚI Soutetsu về chính anh). Chỉ giữ khi Kisaki nói với NGƯỜI KHÁC về Soutetsu (ngôi ba thật sự) — trong batch này không có dòng nào như vậy (cả 126 dòng đều có Soutetsu là người nghe; 0 dòng giữ vì ngôi ba).
- **D3 — Đối chiếu số đếm trong list (§2 P4, chỉ là ước lượng):** 稀咲h1 list ghi 41 → thực tế 34 (+2 tách tên = 36); 稀咲h2 list ghi 37 (15 "anh Soutetsu" + 12 "Anh Sou…" + 10 "anh" trần) → thực tế 22 (+2 tách tên = 24; 12 "Anh Sou…" là các dạng viết hoa đầu câu + 2 dòng tách tên đã tính riêng, 10 "anh" trần là đại từ ngôi 2 — ngoài phạm vi P4); 稀咲h3 list ghi 33× → thực tế 45; Kisaki03 list ghi "9 + 1793" → thực tế 8 (key 1793 là Kisaki nói 「ああ！久しぶり、本当に来てくれたんだね」/「A! Lâu rồi không gặp, anh đến thật này.」 — chỉ có đại từ "anh", không có "anh Soutetsu"; list ghi nhầm).

## 5. Lượt soát 2 (bắt buộc — đọc lại toàn bộ fix theo JP)

- **Tổng số fix đưa vào lượt soát 2: 126 dòng. Tái kiểm chứng: 126/126. Loại bỏ: 0. Sửa lại: 0.**
- Mỗi fix đã đọc lại đối chiếu JP (+TW khi cần): JP đều là 双鉄 trần (124 dòng) hoặc tách tên trong rên (2 dòng); fix chỉ bỏ "anh" trước tên, giữ nguyên toàn bộ phần còn lại — kể cả đại từ "anh" ngôi 2 sau tên (h1 1471, h2 1268, h3 2750…), thẻ `%l` (2008 giữ `\x%l8620;#00ffc040;8620%l;#;`, 2292 giữ `%lエアクラ…Aircra%l;`), dấu câu, nhịp rên và literal `\n`. Không dòng nào đổi nghĩa khác; không đụng dòng gasp Ư hay dòng "Kh" nào.
- Kiểm chứng cơ học bổ sung: span-diff `old_vn` → `fix` cho 126/126 dòng chỉ gồm đúng phép thay đã định ("anh Soutetsu"→"Soutetsu" 94 lần, "Anh Soutetsu"→"Soutetsu" 36 lần, "anh Sou――tetsu"→"Sou――tetsu" 2 lần); không còn "anh Soutetsu" (mọi dạng hoa/thường, kể cả tách tên) trong bất kỳ fix nào; `jp`/`tw` trong JSON khớp CSV3 từng dòng; 0 key trùng với các file unification đã gộp (kiểm tra (file,key) với 656 mục đã gộp).
- Nguồn `old_vn`: CSV3 115 dòng, audit fix 9 dòng, moan fix 2 dòng, unification đã gộp 0 dòng (xem Phương pháp).

## 6. Khối TOML (parse-verified, theo file)

Mỗi khối có header `[script]`, key dạng chuỗi, giá trị là fix. Trong khối TOML, backslash được escape (`\` → `\\`, `"` → `\"`), nên literal `\n` trong giá trị viết thành `\\n`. Đã parse-verify bằng tomllib: mọi khối parse được và giá trị parse ra khớp fix từng key (**5 khối / 126 key**).

```toml
# 稀咲02_新事業案.txt.toml
[script]
"1716" = "「Chắc là vậy rồi. Vì còn liên quan đến đất đai nữa mà.\\nMà nói vậy tức là, Soutetsu cũng đã nghĩ đến chuyện đó?」"
"1755" = "「Cả Soutetsu cũng vậy sao. Quả nhiên, ai cũng sẽ cảm thấy như thế nhỉ.\\nNếu chỉ chạy đi chạy lại trên một đoạn đường ngắn như vậy thì thật lãng phí.」"
"1768" = "「Soutetsu cổ hủ thật đấy.\\nSuy nghĩ còn cổ hủ hơn cả bố tôi nhiều.」"
"1858" = "「Hya!? Ch, ch, chuyện gì vậy, Soutetsu.」"
"1919" = "「Ơ, Soutetsu? Anh đi đâu vậy?」"
"1956" = "「Chính là cơn gió này, sau khi bị thiêu đốt bởi hơi nóng kia.\\nChắc chắn là vậy. Nó đã thay đổi——một phần nào đó trong Soutetsu.」"
"2008" = "「Giống như Soutetsu sở hữu \\x%l8620;#00ffc040;8620%l;#, cho chạy tàu, và nhận được phần lợi nhuận được chia. Ý tôi là làm điều tương tự với đường ray, nhưng với số lượng người tham gia lớn hơn.」"
"2099" = "「Tôi, đã kích thích Soutetsu như thế nào?」"
"2142" = "「Soutetsu làm á?」"
"2292" = "「Dù sao thì, tôi rất vui vì Soutetsu có vẻ đã hứng thú\\nvới tình trạng hiện tại của Kumagin và công ty \\x%lエアクラ;#00ffc040;Aircra%l;#;.」"
"2297" = "「Nói là kích thích thì——thứ tôi cảm nhận được là dục vọng.\\nThế nên, tôi nghĩ đó chính là cơ hội để Soutetsu thay đổi.」"
"2382" = "「A, a, a, Soutetsu.\\nA, a, anh, có thể, đừng, căng, thẳng, như, vậy, được, không.」"
"2383" = "「Soutetsu. Chính là cái này. Hãy làm theo cách đó đi.」"
"2385" = "「Soutetsu về rồi à, sao rồi?」"
"2386" = "「Soutetsu cũng là người bận tâm đến mấy chuyện đó sao?」"

# 稀咲03_純白のレール.txt.toml
[script]
"1750" = "「Ufufu, Soutetsu.」"
"1760" = "「Oa!? Soutetsu? Có chuyện gì vậy, sao mặt mũi đáng sợ thế.」"
"1930" = "「Từ rất lâu trước khi anh bắt đầu thích em.\\nSoutetsu, anh biết không? Em đã thích anh rồi đấy.」"
"1979" = "「Đúng vậy, Soutetsu.\\nTất nhiên em cũng sẽ, đồng hành cùng anh chứ?」"
"1980" = "「Đúng vậy, Soutetsu. Sắp đến giờ rồi.」"
"2050" = "「Chi tiết cụ thể thì từ giờ sẽ kiểm tra kỹ lưỡng và chốt lại sau——\\nAnh thấy sao, Soutetsu. Một bản giải trình huy động vốn mang cảm giác thế này.」"
"2125" = "「Nếu vậy thì, với chuyện gì.\\nMà Soutetsu lại trở nên nghiêm túc đến vậy?」"
"2141" = "「Anh đang nói lời yếu đuối gì vậy, Soutetsu.」"

# 稀咲h1_性生活.txt.toml
[script]
"1014" = "「……Ưm. Quả nhiên là em có thể thích nó.\\nHơn nữa, Soutetsu trông cũng có vẻ rất sướng đúng không?」"
"1016" = "「……Là ở đây, nè? Soutetsu. Vagina――âm đạo.\\nAnh sẽ đưa dương vật của mình vào cái lỗ này đó」"
"1192" = "「Vết thương từ vụ tai nạn——đã khiến Soutetsu cảm thấy ghê tởm tình dục nhỉ.」"
"1216" = "「Em cũng được anh dạy cho nhiều điều mà?\\nTừ Soutetsu――về tình yêu, về tình dục, và về con trai nữa」"
"1247" = "「Kya!? Soutetsu!!?」"
"1252" = "「Fufu. Em vui lắm.\\nVì Soutetsu cũng có cùng cảm xúc với em」"
"1317" = "「Ừm. Vậy nên, chúng ta cùng nhau học nhé? Tình dục của Soutetsu và em\\n――chắc chắn sẽ rất bình dị, nhưng cũng vô cùng đặc biệt」"
"1319" = "「Vâng. Soutetsu」"
"1321" = "「Hửm? Gì vậy? Có chuyện gì mờ ám sao——\\nà, mà này. Sao Soutetsu lại ở trong phòng giám đốc chi nhánh vào giờ này?」"
"1333" = "「Được thôi. Soutetsu.\\n……Nhìn cho kỹ, nhé? Cảnh em cởi ra ấy」"
"1344" = "「Vì học qua DVD thì đó cũng chỉ là tình dục của người khác thôi.\\nCòn tình dục của riêng em, thì em chỉ có thể học từ Soutetsu mà thôi」"
"1349" = "「Gì vậy…… Soutetsu――ưm――ha――ngực em――\\nanh muốn――nắn bóp――lắm――ưm――sao?」"
"1350" = "「Thế nào…… hả, Soutetsu……\\nAnh còn muốn em làm gì khác nữa không?」"
"1357" = "「Tình dục——tình dục không phải là thứ đáng bị ghê tởm.\\nEm sẽ dạy cho Soutetsu điều đó.」"
"1368" = "「Em cũng, yêu anh lắm…… và cả cái này nữa, chắc em cũng sẽ thích nó\\nchứ nhỉ? Dịch――nhờn rỉ ra――của Soutetsu――ưm――liếm」"
"1373" = "「Em hiểu mà, Soutetsu.」"
"1376" = "「Giống hệt như tâm trạng của em,\\ncơ thể em cũng đang rất vui sướng vì được gắn kết với Soutetsu đấy.」"
"1380" = "「Vì thế, không có gì phải sợ cả……\\nCũng không cần phải xấu hổ, hay ngại ngùng gì đâu, Soutetsu」"
"1385" = "「Xin lỗi anh nhé? Soutetsu.\\nHình như em, nhồi nhét bài học, hơi quá tay rồi nhỉ」"
"1396" = "「Đúng vậy nhỉ…… chính em cũng không biết đâu.\\nĐây cũng xem như là điều Soutetsu đã dạy cho em đấy」"
"1398" = "「Đúng…… vậy. Em cũng, thấy sướng ở núm vú.\\nNhững phần chạm vào cơ thể Soutetsu, tất cả, đều sướng đến mức như sắp tan chảy ra vậy.」"
"1409" = "「So với…… tưởng tượng tồi tệ nhất, thì――nhẹ nhàng――hơn nhiều――ưm\\n……Vậy nên, Soutetsu――cử động, đi――hyan!?」"
"1416" = "「Không sao, em quen rồi.\\nSoutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——tổng giám đốc ngân hàng cơ.」"
"1421" = "「P-Phải cố một chút chứ. ――Oẹ――e.\\nTại vì, ánh mắt của Soutetsu――ưm――như đang muốn em nuốt nó mà」"
"1465" = "「Câu đó không thể làm ngơ được đâu nhé, Soutetsu.」"
"1471" = "「Lần này, đến lượt em làm giáo viên nhỉ――\\nNè? Soutetsu, anh có biết phải đưa dương vật vào đâu không?」"
"1473" = "「Tâm trạng sảng khoái…… vậy sao, fufu.\\nSoutetsu, thức dậy với tâm trạng sảng khoái nhỉ.」"
"1476" = "「A, Soutetsu. Ch, chào buổi sáng. C, cuối cùng anh cũng tỉnh rồi nhỉ.」"
"1477" = "「Soutetsu…… anh đúng là――――\\nFufu…… chụt――chụt――chụt」"
"1478" = "「Dương vật của Soutetsu, cũng đã trở nên thành thật rồi nhỉ.」"
"1479" = "「Soutetsu? Anh nên dậy đi thôi.」"
"1480" = "「Soutetsu? Nói thêm nữa thì hơi mất hứng đấy nhé」"
"1482" = "「Dịch…… nhờn rỉ ra…… ưm――fufu,\\nDương vật của Soutetsu có vẻ――rất thích mái tóc của em nhỉ」"
"2093" = "（Cả chuyện tình dục, lẫn những chuyện sau này――\\nSoutetsu, chúng ta hãy cùng nhau học hỏi suốt đời nhé?）"

# 稀咲h2_プライベートルーム.txt.toml
[script]
"922" = "「……Ha…… a………… ưm.\\nỪm――ừm. Em cũng――vậy――Soutetsu」"
"1116" = "「Nhưng mà, Soutetsu này. Cả hai chúng ta đều bận rộn.\\nĐâu thể ngày nào cũng gặp nhau rồi âu yếm được, đúng không?」"
"1117" = "「Nhưng mà, Soutetsu đã biết đến tình dục rồi.\\nVừa mới nếm trải niềm vui sướng của tình dục, chắc chắn ngày nào anh cũng sẽ muốn làm」"
"1120" = "「Khuôn mặt…… của Soutetsu…… tan chảy ra rồi…… kìa?\\n……A――fu――ưm……」"
"1124" = "「Lại đây, Soutetsu」"
"1136" = "「Lúc nãy――Soutetsu đã nhìn vào đây nhỉ.\\nHơi thở trở nên gấp gáp…… khuôn mặt, và cả cơ thể đều đỏ ửng lên」"
"1166" = "「Hi――a――ưm――fu――Sou――tetsu――\\nƯm――tha――cho em――em――em――không chịu nổi nữa rồi」"
"1190" = "「A…… ưm fu――Anh mạnh bạo quá đấy, Soutetsu.\\nĐến mức đó, em đã――」"
"1193" = "「A…… tuyệt quá…… Soutetsu――Soutetsu đang,\\nthủ dâm…… vì em…… ưm…… vì em……」"
"1205" = "「Ưm――ha――a――Sou――tetsu――」"
"1223" = "「Vâng! Soutetsu――Soutetsu, cũng――ơ, hả?」"
"1243" = "「Đúng vậy, cho nên……\\nTừ trước đến nay em cũng đã cố tình để lộ quần lót và vòng ngực cho Soutetsu thấy đó」"
"1246" = "「Vagina, thì…… cho đến khi…… được Soutetsu, mở ra……\\nƯm――em chưa từng――tự mình――đụng chạm――vào nó――đâu」"
"1260" = "「Em…… phải ra, một lần――đã――ưm――\\nNếu để Soutetsu, đưa vào ngay bây giờ, thì――em sẽ phát điên――mất」"
"1268" = "「Bởi vì em đã quan sát anh mà. Rằng hôm nay Soutetsu,\\nsẽ phản ứng thế nào nếu em cho anh xem quần lót của em」"
"1284" = "「Vì thế nên em mới vui. Vì hôm nay Soutetsu đã nhận ra.\\nVà khao khát em」"
"1286" = "「Vì vậy, em sẽ dạy cho Soutetsu. Cách làm tình có thể thực hiện một mình.\\nCách thủ dâm, trong khi nghĩ về em」"
"1299" = "「Đúng vậy. Quả thực là một căn phòng rất mang phong cách của Soutetsu.\\nMà, nhìn vào cách anh tiêu tiền thì em cũng đoán được phần nào rồi」"
"1325" = "「Đúng…… vậy đó…… những lúc, không gặp được anh, thì…… ưm,\\nEm, cũng――nghĩ về Soutetsu――và thủ dâm, đó?」"
"1359" = "「Chính vì là cơ hội quý giá, nên em mới muốn ngắm nghía thật kỹ\\ncăn phòng của Soutetsu. Bởi vì căn phòng chính là tấm gương phản chiếu con người mà」"
"1374" = "「Nếu vậy thì.\\nEm có thể yên tâm dạy cho Soutetsu rồi, nhỉ?」"
"1382" = "「Soutetsu――ra đi!! Em, em――ưm!」"
"1384" = "「Soutetsu…… sao anh lại dừng thủ dâm rồi」"
"1386" = "「Soutetsu đúng là, thích làm nũng và thật thà nhỉ.\\nAnh muốn đưa chim vào đây đúng không?」"

# 稀咲h3_チャイナドレスでおもてなし.txt.toml
[script]
"1540" = "「――Ừm. Đúng vậy thật.\\nƯớc mơ của em từ lúc nào, đã hòa làm một với ước mơ của Soutetsu rồi nhỉ」"
"1587" = "「……Soutetsu」"
"1969" = "「Đó chắc chắn là một khoảnh khắc thường ngày giữa Soutetsu và em gái.\\nEm có cảm giác như mình đã chạm đến được khoảng cách đó, sự ấm áp đó」"
"1994" = "「Không phải là không thể đâu? Soutetsu chắc chắn. Vẫn còn nhớ mà.\\nCho dù hiện tại, nó đang bị nhốt ở một góc nào đó trong trái tim anh」"
"2003" = "「Đầu vú…… được, Soutetsu…… vuốt ve――……Ư\\nChỉ cần vậy, thôi――đã nóng ran――và cứng lại, thế này――」"
"2041" = "「Nhưng mà, Soutetsu thì sao」"
"2053" = "「Lý trí. Anh vẫn đang giữ vững đúng không?\\nChẳng lẽ em không đủ sức hấp dẫn, để phá vỡ lý trí của Soutetsu sao?」"
"2070" = "「Nhìn kiểu tóc búi chignon của em, anh khen đáng yêu!\\nEm thấy đúng chuẩn Soutetsu luôn, nên em vui lắm」"
"2185" = "「Ufufu, được thôi?\\nNếu vậy em sẽ lấy Soutetsu làm gối nệm đấy」"
"2187" = "「Fufu, đúng nhỉ……――Vì là tinh dịch của Soutetsu……\\nChắc chắn sẽ dịu dàng……để không bị chết đuối nhỉ」"
"2191" = "「Ủa? Bất ngờ thật đấy.\\nSoutetsu không hay tham gia các buổi tiệc tùng sao?」"
"2193" = "「Ủa ủa? Trông Soutetsu có vẻ tiếc nuối nhỉ」"
"2203" = "「Ha…… ưm――Fu, a…… tay…… tay của, Soutetsu――\\nấm quá――fu…… ha…… ha fu」"
"2211" = "「Hả? À――không, chỉ là? Chuyện đó……\\nEm đang nghĩ, liệu có phải Soutetsu cũng hơi say rồi không?」"
"2246" = "「À, đúng rồi nhỉ.\\nTại Soutetsu có phong thái chững chạc quá, nên em cứ vô tình nghĩ vậy」"
"2248" = "「Này――Soutetsu, đừng nói chuyện đáng xấu hổ như thế」"
"2250" = "「Thích Soutetsu. Yêu Soutetsu.\\nThực sự rất hạnh phúc――chỉ vậy thôi」"
"2254" = "「Fua! Dương vật――tuyệt quá――Soutetsu――\\nCứng――như thế này――phu, á――nóng quá」"
"2296" = "「Ừm. Vì em không muốn Soutetsu bị ai khác cướp mất đâu」"
"2326" = "「Hay đấy! Soutetsu. Cứ quyết định vậy đi.\\nĐúng rồi, chúng ta đã là hôn phu hôn thê chính thức của nhau rồi mà」"
"2327" = "「Được thôi? Vậy em sẽ cho anh xem.\\nĐi nào? Soutetsu」"
"2360" = "「Âm đạo――đầy ắp――tất cả, Soutetsu――\\ndương vật, của, ――Soutetsu――Fua!」"
"2388" = "「Sao thế Soutetsu」"
"2390" = "「Chuyện đó! Nếu Soutetsu không bận tâm thì em cũng không sao đâu?\\nBộ váy này, em chỉ cho một mình Soutetsu xem thôi mà」"
"2407" = "「Em cũng vậy, Soutetsu. Em hiểu rồi. Hai người cùng khao khát nhau,\\nsẽ hạnh phúc và sướng hơn nhiều so với việc bị đòi hỏi một chiều」"
"2422" = "「Em muốn Soutetsu, cứ thoải mái làm theo ý mình.\\nLàm tình, theo cách mà Soutetsu muốn」"
"2426" = "「Em muốn biết. Liệu Soutetsu, chỉ cần vẻ bề ngoài của em thôi――\\ncũng có thể yêu thích em, và cảm thấy hưng phấn không」"
"2432" = "「Vì em đã rất cố gắng mà.\\nVì Soutetsu, và cũng vì chính bản thân em nữa」"
"2437" = "「Đối với em, một hôn lễ tuyệt vời nhất,\\nchỉ cần có Soutetsu đứng ở vị trí chú rể là đủ rồi mà?」"
"2465" = "「Bình thường thì, người ta sẽ nhìn vào cơ thể. Dù là đàn ông, hay thậm chí là phụ nữ.\\nNhưng mà, Soutetsu lại nhìn vào mặt em đầu tiên――ufufu」"
"2468" = "「Chẳng phải anh bảo là 『cho em uống』 sao?\\nSoutetsu, cho em」"
"2556" = "「Không đâu. Em chỉ nghĩ, đúng là Soutetsu có khác.\\nVui quá, đáng yêu quá. Nên em lỡ cười thôi」"
"2656" = "「Hơn nữa――em, em này? Soutetsu」"
"2666" = "「Hãy dành thời gian, để nhớ lại đi nhé.\\nEm nhất định, sẽ nấu lại hương vị đó cho Soutetsu ăn」"
"2726" = "「Chuyện đó――Soutetsu. Nghe vậy, em rất vui…… ưm――\\nnhưng, mà……」"
"2731" = "「Đó là khoảnh khắc em trở thành một phần cuộc sống thường ngày của Soutetsu mà.\\nThay vì khoe khoang, em muốn giữ nó làm bí mật của riêng hai chúng ta hơn」"
"2732" = "「Vì là Soutetsu cho em uống mà?\\nNên em rất muốn nói là nó ngọt ngào và ngon tuyệt vời…… nhưng mà」"
"2739" = "「Bởi vì nơi này, là nhà của Soutetsu」"
"2750" = "「Tóm lại là, anh muốn xem đúng không?\\nSoutetsu, muốn xem em mặc, sườn xám」"
"2753" = "「Anh nhớ kỹ nhé? Soutetsu. Trang phục truyền thống,\\nchỉ có “của nước mình” thì mới được coi là lễ phục thôi đó?」"
"2781" = "「Vậy thì, lý trí của Soutetsu, đã――」"
"2793" = "「Hương vị của nhà Sogou――gia đình của Soutetsu cơ」"
"2794" = "「Soutetsu này? Đừng có mút ngón tay nữa」"
"2795" = "「Soutetsu. Em mặc xong rồi nè?」"
"2796" = "「Soutetsu, ăn không?\\nCó vẻ anh khá thích kem phô mai mà」"
```

## 7. Cờ va chạm merge-order phát hiện SAU lượt soát 2 (cần coordinator xử lý trước khi gộp)

- Trong lúc đợt này chạy, một batch song song đã xuất hiện: `unification-t1-open-t56-t66-wrong.json` (171 mục, tạo 22/11 ~11:33 +07 — sau khi map hiện trạng của đợt này được build, nên không có trong 656 mục đã kiểm tra trùng ở lượt soát 2). Batch đó CHƯA gộp vào chuỗi ROUTE-UNIFICATION (đầu chuỗi vẫn là U2b 21/662).
- **Va chạm duy nhất (1 key) trên toàn bộ các file unification-*.json hiện có trên đĩa (kiểm tra lại toàn bộ 13 file, trừ file của đợt này): 稀咲h1_性生活.txt.toml key 1416.**
  - `old_vn` của cả hai bên giống hệt nhau (giá trị audit): 「Không sao, em quen rồi.\nAnh Soutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——giám đốc ngân hàng cơ.」
  - Fix của batch T56–T66 (T60 頭取 → "Tổng giám đốc"): 「Không sao, em quen rồi.\nAnh Soutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——tổng giám đốc ngân hàng cơ.」 — giữ "Anh Soutetsu".
  - Fix của đợt này (P4): 「Không sao, em quen rồi.\nSoutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——giám đốc ngân hàng cơ.」 — giữ "giám đốc ngân hàng".
  - Giá trị gộp ĐÚNG (cả hai thay đổi cùng áp dụng): 「Không sao, em quen rồi.\nSoutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——tổng giám đốc ngân hàng cơ.」
- **Nguy cơ:** cả hai fix đều là thay toàn bộ giá trị, build trên cùng một `old_vn`. Bên nào gộp sau trong rebuild (áp dụng theo thứ tự merge) sẽ GHI ĐÈ thay đổi của bên kia trên dòng 1416 — hoặc mất P4, hoặc mất T60. Coordinator phải xử lý trước khi gộp: hoặc gộp một bên rồi sửa `old_vn`/`fix` của bên còn lại thành giá trị gộp đúng, hoặc áp dụng giá trị gộp đúng trực tiếp. Đợt này KHÔNG tự sửa JSON của mình thành giá trị gộp (đó là giả định về thứ tự merge — thuộc về coordinator).
- Lượt soát 2 (126/126, 0 loại, 0 sửa) vẫn đứng nguyên: va chạm này không làm sai bất kỳ fix nào của đợt này theo trạng thái lúc build; nó chỉ là vấn đề thứ tự gộp.

## **Ghi chú điều phối (coordinator, 22/11 ~12:05 — 2 dòng ghép):** 1416 trùng U13a (T60) và 2203 trùng U11a (M17) ở token khác nhau — đã GHÉP theo quy tắc composition: old_vn := fix batch đã gộp, fix := giá trị kết hợp (1416 = fix T60 bỏ "Anh " trước Soutetsu; 2203 = fix M17 bỏ "anh " trước Soutetsu). Mỗi giá trị ghép kiểm chứng 2 chiều: bằng fix batch kia + đổi của đợt này, và bằng fix đợt này + đổi của batch kia — cả hai chiều trùng nhau tuyệt đối. §7 trên mô tả va chạm 1416 ở trạng thái TRƯỚC khi gộp; JSON + bảng §3 + khối TOML nay mang giá trị kết hợp.

Kết bài

Đợt U7a sửa **126 dòng (P4)** trong 5 file 06_Kisaki (稀咲02: 15; 稀咲03: 8; 稀咲h1: 34; 稀咲h2: 24 — gồm 2 dòng rên tách tên; 稀咲h3: 45): Kisaki gọi Soutetsu thống nhất thành tên trần "Soutetsu", bỏ "anh" trước tên (132 lần xuất hiện). Folder 03_Paulette (file không lr) 0 dòng. Đã đọc kiểm chứng từng dòng kèm 3–5 dòng kề (JP đều là 双鉄 trần; 0 dòng ngôi ba với người khác); giữ 1 dòng đã đúng (h3 2195 "Sou――tetsu"), không đụng 2 dòng của người nói khác (稀咲02 2376 Hibiki — đã sửa trong audit; 稀咲03 2137 Reina — dùng "anh Soutetsu" là đúng). Lượt soát 2: 126/126 tái kiểm chứng, 0 loại, 0 sửa. Khối TOML 5 file / 126 key parse-verified. Nợ coordinator: (1) cờ U6 Grand 08 key 1702 đã kiểm chứng là KHÔNG có gì để sửa cho P4 (Kisaki nói 「キミは、それで――」/「Cậu, như vậy thì――」) — batch 09_Grand không cần đụng dòng này; (2) U7b ĐÃ chạy xong trong lúc đợt này chạy — file `unification-s2-kisaki-address-tsuika-lr-wrong.json` (51 mục, ít hơn 62 dòng đếm thô của đợt này — chênh lệch do U7b đọc từng dòng và loại sau kiểm chứng; lưu ý lr_稀咲ポーレットh1 còn 37 dòng Paulette "anh Soutetsu" là ĐÚNG, không được sửa theo P4); 11_Other 0 dòng Kisaki "anh Soutetsu"; (3) **va chạm merge-order — xử lý trước khi gộp (xem §7): 稀咲h1 key 1416 trùng với batch T56–T66 (`unification-t1-open-t56-t66-wrong.json`); giá trị gộp đúng là 「Không sao, em quen rồi.\nSoutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——tổng giám đốc ngân hàng cơ.」**
