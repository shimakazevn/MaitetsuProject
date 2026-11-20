# Kiểm tra bản dịch — 05_Mayami lr真闇追加01: 新婚旅行のリクエスト

File: `lr真闇追加01_新婚旅行のリクエスト.txt.toml` — route 05_Mayami, file thêm (追加) về tuần trăng mật của Soutetsu và Mayami: bàn lịch trình trên Navi, chọn hướng dẫn viên (Reina), hồi tưởng về căn phòng cũ.
Đây là kiểm tra ĐẦY ĐỦ (full audit) — đọc toàn bộ 300 dòng script đối chiếu JP + TW.

## §1. Tổng quan

- Tổng số dòng script: **300** (monologue 71, hội thoại 229).
- Số dòng sai: **142/300 (47,3%)** — hội thoại 109/229 (47,6%), độc thoại 33/71 (46,5%). Đây là file bẩn thứ nhì toàn dự án (sau Hibiki 03: 86,2%; ngang obasan 56% — nhưng obasan chỉ 455 dòng, file này 300 dòng với 142 sai).
- Phân loại: misaligned 125 (123 thu hồi từ key khác + 1 dịch mới 1036 + 1 lặp hợp lệ 1175), terminology 8, pronoun 7, gasp 2.
- TOML md5: `c9305bfbbddbafeb4404d1b65789ce46` (68.118 byte, BOM + CRLF 628, `[selections]` rỗng, `[info]` 0 trống, bản duy nhất — không có file trùng).
- CSV↔TOML: 76 dòng khớp tuyệt đối + 223 dòng chỉ khác ở chỗ TOML-2 làm phẳng ký tự `\n` thành khoảng trắng — **1 khác biệt thực chất**: key 1264 (TOML giữ nguyên văn TW làm placeholder, CSV để trống — đây chính là dòng chưa dịch).
- Thẻ `%l`: JP 0, VN 0 — không có thẻ nào trong file.
- **Rotation: 2 chuỗi xoay** — chuỗi A dài 114 mắt xích (đầu: bản của 1036 → 1177 → 1092 → … → 1736, đuôi trùng bản đúng của 1199), chuỗi B dài 9 mắt xích (đầu: bản lặp "À" của 1175 → 1283 → 1641 → 1292 → 1040 → 1190 → 1332 → 1159 → 1744 → 1264). Cả hai chuỗi đều khép kín trong file: mọi bản dịch cũ đều được dùng đúng 1 lần làm fix, không còn dòng mồ côi.
- **0 contamination** (chỉ mục VN toàn dự án: 0/142 bản cũ xuất hiện ở file khác) / **0 orphan** / **1 untranslated** (1264 — đã thu hồi bản đúng từ key 1744, không cần dịch mới; dòng chưa dịch còn lại toàn dự án nằm ở lr真闇追加02) / **0 duplicate key**.
- **0 dòng uncertain.**
- Ohitoyo trong file: 13 dòng đã sửa (7 thuật ngữ thuần + 6 trong bản thu hồi) — còn **0 Ohimitera/Ohito**. Yui→Yunoi: 2 dòng (1156, 1494) — còn 0. Migita System→Migita Ichi: 1 dòng (1376) — còn 0. "dồn toa": 1 dòng (1494, bỏ theo quyết định 1027 của Hieu 20/11) — còn 0.

## §2. Bảng fix (142 dòng)

### 669 — monologue — misaligned
- JP: ……ポーレットはあまりに多忙すぎるし、\n頼んでしまえば無理をしてでも引き受けてくれそう――あ
- TW: ……波萊特工作特別忙，要是拜託她的話她肯定會擠出時間接受。對了——
- Cũ: 「Em cũng nghĩ vậy.\nVậy thì cũng không thể nhờ Nagi được. Đối mặt với khách quen sẽ rất ngại」
- Mới: ……Paulette thì quá bận rộn,\nnếu nhờ vả, cô ấy có thể sẽ cố sức nhận lời——a
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1376 — lấy nguyên văn về đây.

### 692 — れいな — misaligned
- JP: 「……れいなちょっと残念ですぅ。かとうすずめさんには、\n声、とどかなかったんですかねぇ」
- TW: 「……玲奈感覺有點遺憾。加藤雀先生沒能聽到我的聲音吧」
- Cũ: Câu trả lời của một đứa trẻ ngoan. Tiếp đó là nhịp thở đầy háo hức.\nNhưng rồi, nó lại biến thành một giọng nói có chút xịu xuống.
- Mới: 「……Reina hơi tiếc một chút ạ. Chắc là anh Kato Suzume,\nkhông nghe thấy tiếng rồi nhỉ」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1168 — lấy nguyên văn về đây.

### 700 — 双鉄 — misaligned
- JP: 「……そうか」
- TW: 「……這樣啊」
- Cũ: 「Nếu không làm vậy nữa, thì kiểu gì cũng sẽ buông tay thôi.\nTrong lúc còn nắm tay nhau, bao bọc quá mức cũng tốt mà」
- Mới: 「……Vậy sao」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1731 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: bản thu hồi '……Vậy sao' khớp JP '……そうか'.

### 1007 — 真闇 — misaligned
- JP: 「30分やら1時間やらならどーとでもなるけん。\nほんなら、一緒ね。もし引き受けてもらえたら」
- TW: 「三十分鐘或者一個小時還是拿得出來的。不如我們一起談，前提是她願意接受的話」
- Cũ: 「Tất nhiên rồi. Nếu chị Mayami có thời gian」
- Mới: 「30 phút hay 1 tiếng thì lúc nào cũng xoay sở được.\nVậy thì, cùng nhau nhé. Nếu em ấy nhận lời」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1379 — lấy nguyên văn về đây.

### 1010 — 真闇 — misaligned
- JP: 「次から大きな出す時には、\nあらかじめいうてくれたらそれでよかけん」
- TW: 「下次要大聲喊的時候，記得要提前說一聲」
- Cũ: 「Hau. Em xin lỗi ạ. Reina, chỉ là,\nnghĩ nếu có thể nói chuyện với anh Kato Suzume trên trời thì tốt biết mấy」
- Mới: 「Lần sau muốn hét to,\nthì báo trước cho chị một tiếng là được rồi」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1213 — lấy nguyên văn về đây.

### 1016 — 真闇 — misaligned
- JP: 「ううん、双ちゃん。時間がもっとたっぷりあっても、\nおねえちゃん、必ず御一夜旅行ばお願いしてた」
- TW: 「不是的，小雙。就算時間再充裕一些，姐姐也想要來一次御一夜旅行」
- Cũ: 「Vậy mà, chị thực sự muốn đi 『Du lịch Ohimitera』 sao?\nNếu vì lý do thời gian, em có thể dời lại thêm nữa」
- Mới: 「Không đâu, Sou-chan. Dù có nhiều thời gian hơn nữa,\nchị cũng nhất định sẽ xin đi du lịch Ohitoyo」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1737 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: Ohimitera→Ohitoyo.

### 1019 — 真闇 — misaligned
- JP: 「それより、ね？　れーちゃんにもしガイドば頼めるなら。\n細かな打ち合わせには、おねーちゃんも参加してよか？」
- TW: 「不說這個啦，如果要讓小玲當嚮導的話，商量細節的時候也讓姐姐參加好嗎？」
- Cũ: Chị Mayami dĩ nhiên không có kinh nghiệm nuôi dạy con cái.\nVậy thì đây hẳn là những suy nghĩ dành cho Hibiki, tôi chợt nhận ra.
- Mới: 「Hơn nữa, nè? Nếu có thể nhờ bé Reina làm hướng dẫn viên.\nChị cũng có thể tham gia vào buổi bàn bạc chi tiết được không?」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1364 — lấy nguyên văn về đây.

### 1026 — 双鉄 — misaligned
- JP: 「確かにだ。せっかくの新婚旅行。\nリラックスして楽しめなければもったいないものな」
- TW: 「也是啊。寶貴的新婚旅行不好好放鬆一下就太浪費了」
- Cũ: 「Hướng dẫn viên của Phòng Thương mại thì hơi...\nChị chắc chắn sẽ thấy gượng gạo lắm」
- Mới: 「Đúng vậy. Đã cất công đi tuần trăng mật.\nNếu không thể thư giãn và tận hưởng thì thật lãng phí」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1792 — lấy nguyên văn về đây.

### 1033 — 真闇 — misaligned
- JP: 「そーせんでよーなったら、どうしたって手ば離れるけん。\n手ぇつないでくれとる間は、過保護がよかよ」
- TW: 「以後孩子總會離開身邊。趁著孩子還在身邊的時候溺愛一下沒什麼不好」
- Cũ: Quả quyết. Nhẹ nhàng.\nLời khẳng định đó, không chút gượng gạo hay màu mè.
- Mới: 「Nếu không làm vậy nữa, thì kiểu gì cũng sẽ buông tay thôi.\nTrong lúc còn nắm tay nhau, bao bọc quá mức cũng tốt mà」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 700 — lấy nguyên văn về đây.

### 1036 — れいな — misaligned
- JP: 「むりして飛んでこなくていいですよー！\n後でパンくずあげるから、いい子で待ってて下さいねー」
- TW: 「你不用勉強自己飛過來！等一下會給你吃麵包渣，你乖乖在下面等著」
- Cũ: 「Ừ. Được thôi」
- Mới: 「Không cần cố bay qua đây đâu ạ! Lát nữa Reina cho ăn vụn bánh mì, ngoan ngoãn chờ ở dưới đó nha」
- Lý do: Dòng này bị lệch (bản cũ 'Ừ. Được thôi' là của key 1177); không có 'bánh mì'/'vụn bánh' ở bất cứ đâu trong file — dịch mới từ JP/TW (Reina nói với chim sẻ: đừng cố bay qua, lát cho ăn vụn bánh mì, ngoan chờ ở dưới).

### 1039 — 真闇 — misaligned
- JP: 「双ちゃんが栄えさせてくれると？\nおねえちゃんと一緒に」
- TW: 「你會讓家庭興旺嗎？和姐姐一起」
- Cũ: Lời nói đầy lý trí của tôi, chỉ bằng một tiếng hùa theo đầy gợi cảm,\nđã mang theo hơi ấm sống động đến chân thực.
- Mới: 「Sou-chan sẽ làm cho gia đình hưng thịnh sao?\nCùng với chị」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1295 — lấy nguyên văn về đây.

### 1040 — 真闇 — misaligned
- JP: 「自分で気づいておらんかったと？\nふふって、双ちゃん笑ったの。思い出し笑いみたいに」
- TW: 「你自己沒發現嗎？你剛才笑了，像是想起了什麼有趣的事情」
- Cũ: 「Hửm? Vậy tại sao」
- Mới: 「Em không tự nhận ra sao?\nEm vừa cười khúc khích đấy, Sou-chan. Như đang nhớ lại chuyện gì vui vậy」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1292 — lấy nguyên văn về đây.

### 1048 — 双鉄 — misaligned
- JP: 「なのに、本当に『御一夜旅行』が希望でいいのか？\nもしも時間の都合だったら、僕はさらに先に伸ばしても」
- TW: 「光是“御一夜旅行”真的就行了嗎？如果是因為時間不夠的話，旅行再推遲一段時間我也沒關係」
- Cũ: Nhắc mới nhớ, chị Mayami vẫn chưa từng ngồi Navi.\nLần này nhất định phải để chị ấy đi thử, nhưng chuyện đó tính sau.
- Mới: 「Vậy mà, chị thực sự muốn đi 『Du lịch Ohitoyo』 sao?\nNếu vì lý do thời gian, tôi có thể dời lại thêm nữa」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1016 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: 'em'→'tôi' (Soutetsu tự xưng với Mayami) và Ohimitera→Ohitoyo.

### 1053 — れいな — terminology
- JP: 「それぞれ17:27、18:34、19:41の御一夜駅発ですね。\n[たらぎはいえき,3]鱈木廃駅臨時停車が、18:04と19:11と20:18でぇす」
- TW: 「分別是１７：２７、１８：３４、１９：４１御一夜出發的車次。在鱈木廢站臨時停車的時間是１８：０４、１９：１１和２０：１８」
- Cũ: 「Lần lượt là 17:27, 18:34, 19:41 xuất phát từ ga Ohimitera ạ.\nDừng đỗ tạm thời tại ga bỏ hoang Taragi lúc 18:04, 19:11 và 20:18 nha」
- Mới: 「Lần lượt là 17:27, 18:34, 19:41 xuất phát từ ga Ohitoyo ạ.\nDừng đỗ tạm thời tại ga bỏ hoang Taragi lúc 18:04, 19:11 và 20:18 nha」
- Lý do: Chỉ sai thuật ngữ: Ohimitera→Ohitoyo (御一夜 đã chốt).

### 1059 — 双鉄 — misaligned
- JP: 「なるほど。面白いものかもしれんな。生まれ育って、\n知り尽くした気さえする地元であるゆえ、かえって」
- TW: 「原來如此，想想確實很有意思。正因為是生在那裡長在那裡的故鄉，所以反而會更有趣」
- Cũ: Tôi chợt nhớ đến thị trấn nhỏ nơi tôi sinh ra.\nNơi đó cũng được coi là một thị trấn có khách du lịch đến thăm, nhưng——
- Mới: 「Ra vậy. Có thể sẽ thú vị đấy. Vì là quê hương nơi mình sinh ra và lớn lên,\ntưởng chừng như đã biết rõ mọi ngóc ngách, nên ngược lại」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1170 — lấy nguyên văn về đây.

### 1061 — 双鉄 — misaligned
- JP: 「なるほどな。ではそうしよう」
- TW: 「原來如此，那就這麼辦」
- Cũ: 「Chuyện đó, đợi bị từ chối rồi hẵng nghĩ.\nNếu có phương án dự phòng, tự nhiên sẽ thấy chùn bước mà」
- Mới: 「Ra vậy. Vậy cứ quyết định thế đi」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1164 — lấy nguyên văn về đây.

### 1071 — 双鉄 — misaligned
- JP: 「しかし、今夜は――というかしばらくは控えておきたい。\nなにせ、新婚旅行のための休暇が」
- TW: 「可是今晚——應該說最近一段時間還是不要了。畢竟我們還有新婚旅行的假期」
- Cũ: Bất chợt, tôi ngửi thấy mùi hương của chị Mayami. Một mùi hương quá đỗi quen thuộc,\nnhưng một khi đã ý thức được, nó lại ngọt ngào đến mức nguy hiểm.
- Mới: 「Nhưng, đêm nay——hay nói đúng hơn là một thời gian tới, tôi muốn kiềm chế lại.\nDù sao thì, kỳ nghỉ cho tuần trăng mật cũng」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1194 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: 'em'→'tôi' (Soutetsu tự xưng với Mayami).

### 1073 — 真闇 — misaligned
- JP: 「ばってん、れーちゃんも忙しいんじゃなかと？\nもしも少しでも無理ばさせちゃうようだったら」
- TW: 「可是小玲也很忙吧？可能會讓她忙不過來」
- Cũ: Ngay khoảnh khắc nghe thấy, giọng nói vui vẻ reo lên,\nđủ để xác định luôn đây là ứng cử viên số một.
- Mới: 「Nhưng mà, bé Reina cũng bận lắm đúng không?\nNếu làm em ấy phải cố sức dù chỉ một chút」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1490 — lấy nguyên văn về đây.

### 1077 — 双鉄 — gasp
- JP: 「っ！」
- TW: 「呃！」
- Cũ: 「!」
- Mới: 「Ư!」
- Lý do: Sweep lost-gasp-whole (đã kiểm chứng trực tiếp trong sweep-raw-gasp-wrong.json): JP 'っ！' là tiếng thở hắt cả dòng, bản cũ chỉ còn dấu '!' — thêm Ư.

### 1080 — 真闇 — misaligned
- JP: 「うふふっ」
- TW: 「呵呵」
- Cũ: 「Trên đùi của phu nhân Mayami, không phải là trang bị tiêu chuẩn của cỗ máy này」
- Mới: 「Ufufu」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1798 — lấy nguyên văn về đây.

### 1084 — 真闇 — misaligned
- JP: 「うふふっ、のんびり遊覧飛行も、\nそいばそいで、楽しか新婚旅行になりそおねぇ」
- TW: 「呵呵，悠哉的飛行遊覽也不錯，也會是一段快樂的新婚旅行」
- Cũ: 「Nhưng, chúng ta có Navi. Nếu ở trong nội địa Hinomoto,\nthì lịch trình này đủ để đi bất cứ đâu」
- Mới: 「Ufufu, bay lượn ngắm cảnh thong dong,\nnhư vậy cũng sẽ là một tuần trăng mật vui vẻ nhỉ」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1768 — lấy nguyên văn về đây.

### 1092 — れいな — misaligned
- JP: 「わわわ！　れいな知らなくて！\nあの、まくらさん、れいな、大きな声だしますねぇ」
- TW: 「哇哇哇！玲奈完全不知道！那個，真暗小姐，玲奈要大聲喊了」
- Cũ: 「Là vậy đó.\nDù có nghe thấy, chắc anh ấy cũng không bay lên được độ cao này đâu」
- Mới: 「Wawawa! Reina không biết luôn!\nÀ này, chị Mayami, Reina, sắp hét to nha」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1177 — lấy nguyên văn về đây.

### 1096 — れいな — misaligned
- JP: 「わぁいわぁい！　聞こえますかぁ、ポーレットぉ！\nれいな、お空から呼んでるんですよぉ」
- TW: 「哇哇！能聽到嗎，波萊特！玲奈從天上叫你呢」
- Cũ: 「Nghĩa là, Kumagin ở đằng kia——\nA, thấy xưởng rượu nhà mình rồi」
- Mới: 「Waai waai! Có nghe thấy không, chị Paulette!\nReina, đang gọi từ trên trời đó nha」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1131 — lấy nguyên văn về đây.

### 1097 — れいな — misaligned
- JP: 「わああっ」
- TW: 「哇啊啊」
- Cũ: 「Đã rõ. Tiến hành xoay vòng」
- Mới: 「Waaa」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1800 — lấy nguyên văn về đây.

### 1101 — れいな — misaligned
- JP: 「わあぁ！　すごいですぅ！\n御一夜の町が、とってもちっちゃくなってますぅ」
- TW: 「哇！好壯觀！御一夜看起來好小」
- Cũ: Để dễ dàng ngắm nhìn cảnh sắc bên dưới,\nNavi nghiêng thân máy bay một cách vô cùng mượt mà.
- Mới: 「Waaa! Tuyệt quá đi ạ!\nThành phố Ohitoyo, trở nên nhỏ xíu luôn ạ」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1181 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: Ohimitera→Ohitoyo.

### 1114 — 双鉄 — misaligned
- JP: 「ふふっ。きっと聞こえていることだろう。\nポーレットにも、日々姫にもハチロクにも」
- TW: 「哈哈。她們一定聽見了，波萊特、日日姬、八六都聽見了」
- Cũ: 「Ây da, hay quá nhỉ. Chị cũng bắt chước thử xem.\nHii-chan, Haa-chan, có nghe thấy không~?」
- Mới: 「Fufu. Chắc chắn là nghe thấy rồi.\nCả Paulette, Hibiki và Hachiroku nữa」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1140 — lấy nguyên văn về đây.

### 1116 — 双鉄 — misaligned
- JP: 「ふふっ、真闇姉のものいいを聞いていると、\n過保護がとても良いことに思える」
- TW: 「哈哈，聽你這麼一說，都讓人覺得溺愛是好事了」
- Cũ: 「A——ufufu. Đúng thế, chắc chắn rồi.\nPau-chan, có vẻ bao bọc quá mức nhỉ」
- Mới: 「Fufu, nghe cách nói của chị Mayami,\nlại thấy việc bao bọc quá mức là một điều rất tốt」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1366 — lấy nguyên văn về đây.

### 1119 — 真闇 — misaligned
- JP: 「あらまぁ」
- TW: 「哎呀」
- Cũ: 「Em hy vọng sự biến đổi này cũng là một niềm hạnh phúc đối với căn phòng.\nEm cứ vẩn vơ suy nghĩ những điều như vậy」
- Mới: 「Chà chà」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1746 — lấy nguyên văn về đây.

### 1125 — 真闇 — misaligned
- JP: 「あらあられーちゃん、\nそぎゃん大きなお声ば、おねえちゃんびっくりしちゃう」
- TW: 「哎呀小玲，你突然這麼大聲，嚇了姐姐一跳」
- Cũ: Đột nhiên Reina hét lớn.\nSự bối rối trong chốc lát đó, không biết là do tôi hay Navi nữa.
- Mới: 「Ây da ây da bé Reina,\nhét to như vậy, làm chị giật cả mình đó」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1149 — lấy nguyên văn về đây.

### 1131 — 真闇 — misaligned
- JP: 「あら、よかねぇ。おねえちゃんも真似しちゃお。\nひーちゃん、はーちゃん、聞こゆるやー？」
- TW: 「哎呀，這樣不錯。我也來喊一喊。小日，小八，你們都聽到了嗎？」
- Cũ: 「Waai waai! Có nghe thấy không, chị Paulette!\nReina, đang gọi từ trên trời đó nha」
- Mới: 「Ây da, hay quá nhỉ. Chị cũng bắt chước thử xem.\nHii-chan, Haa-chan, có nghe thấy không~?」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1114 — lấy nguyên văn về đây.

### 1136 — れいな — misaligned
- JP: 「えへへぇ、さすが特等席は違いますねぇ。\nさいっこうにふかふかでふわふわでぇす」
- TW: 「哎嘿嘿，特等座就是不一樣。真的是又棉又軟」
- Cũ: Lời nói đó có chứa đựng cảm xúc đặc biệt nào không,\nmà sự phấn khích của Reina lại tăng thêm một bậc.
- Mới: 「Ehehe, đúng là ghế đặc biệt có khác nha.\nCực kỳ êm ái và mềm mại luôn ạ」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1619 — lấy nguyên văn về đây.

### 1140 — れいな — misaligned
- JP: 「えへへぇ、だったらうれしいですぅ。\nあ！　そうだ、かとうすずめさーん！　きこえますかぁ」
- TW: 「哎嘿嘿，那我就很高興了。啊！對了，加藤雀先生！你能聽見嗎」
- Cũ: 「Fufu. Chắc chắn là nghe thấy rồi.\nCả Paulette, Hibiki và Hachiroku nữa」
- Mới: 「Ehehe, nếu vậy thì vui quá ạ.\nA! Đúng rồi, anh Kato Suzume~! Có nghe thấy không ạ」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1685 — lấy nguyên văn về đây.

### 1144 — 真闇 — misaligned
- JP: 「ああ――うふふっ。そうね、絶対。\nぽーちゃん、過保護そうだものねぇ」
- TW: 「啊——呵呵。是啊，一定是這樣。畢竟波萊特很溺愛她」
- Cũ: 「Về chuyện đó chị cứ yên tâm.\nNếu có chút gì quá sức, Paulette sẽ không cho nhận đâu」
- Mới: 「A——ufufu. Đúng thế, chắc chắn rồi.\nPau-chan, có vẻ bao bọc quá mức nhỉ」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1116 — lấy nguyên văn về đây.

### 1149 — れいな — misaligned
- JP: 「はぅ。ごめんなさぁい。れいな、ただ、\nかとうすずめさんとお空でお話できたらいいなぁって」
- TW: 「啊嗚。對不起。玲奈隻是覺得能跟加藤雀先生在天上聊天就好了」
- Cũ: 「Ây da ây da bé Reina,\nhét to như vậy, làm chị giật cả mình đó」
- Mới: 「Hau. Em xin lỗi ạ. Reina, chỉ là,\nnghĩ nếu có thể nói chuyện với anh Kato Suzume trên trời thì tốt biết mấy」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1010 — lấy nguyên văn về đây.

### 1156 — 双鉄 — terminology
- JP: 「ああ、列車番号だ。\n御一夜発が奇数。湯医発が偶数になる」
- TW: 「啊，我說的是車次編號。御一夜出發的是奇數，湯醫出發的是偶數」
- Cũ: 「À, số hiệu tàu đấy.\nXuất phát từ Ohimitera là số lẻ. Xuất phát từ Yui là số chẵn」
- Mới: 「À, số hiệu tàu đấy.\nXuất phát từ Ohitoyo là số lẻ. Xuất phát từ Yunoi là số chẵn」
- Lý do: Chỉ sai thuật ngữ: Ohimitera→Ohitoyo và Yui→Yunoi (湯医 đã chốt).

### 1159 — 双鉄 — misaligned
- JP: 「ああ、すまん、\n起こしてしまったか？」
- TW: 「啊，抱歉。我把你吵醒了嗎？」
- Cũ: Giọng nói dịu dàng của chị Mayami vang lên ngay bên cạnh.\nKéo tôi từ những suy nghĩ hạnh phúc trở về với thực tại ngập tràn hạnh phúc.
- Mới: 「A, xin lỗi,\ntôi làm chị thức giấc à?」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1332 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: 'em'→'tôi' (Soutetsu tự xưng với Mayami).

### 1164 — 真闇 — misaligned
- JP: 「ん……」
- TW: 「嗯……」
- Cũ: 「Ra vậy. Vậy cứ quyết định thế đi」
- Mới: 「Ưm……」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1616 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: bản thu hồi 'Ưm……' khớp JP 'ん……'.

### 1166 — 双鉄 — pronoun
- JP: 「ふむ。……どうだろう。\n僕は特には思いつかんが――」
- TW: 「嗯……怎麼辦呢。我想不到該去哪裡——」
- Cũ: 「Hừm. ……Làm sao đây.\nAnh thì không nghĩ ra chỗ nào đặc biệt cả——」
- Mới: 「Hừm. ……Làm sao đây.\nTôi thì không nghĩ ra chỗ nào đặc biệt cả——」
- Lý do: Soutetsu tự xưng 'Anh' với Mayami — phải là 'tôi' (quy tắc đã sửa: 'tôi' với Mayami).

### 1168 — 透 — misaligned
- JP: 「ううむ……それは――」
- TW: 「嗯……這個嘛——」
- Cũ: 「……Reina hơi tiếc một chút ạ. Chắc là anh Kato Suzume,\nkhông nghe thấy tiếng rồi nhỉ」
- Mới: 「Ưm……Chuyện đó thì——」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1287 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: bản thu hồi 'Ưm……Chuyện đó thì——' khớp JP 'ううむ……それは――'.

### 1170 — 真闇 — misaligned
- JP: 「うん。観光客になって訪ねてみたら、\nおねえちゃんがまだ知らん御一夜ば見れるかなぁって」
- TW: 「嗯。作為觀光客去感受的話，我想應該能看到另一種模樣的御一夜」
- Cũ: 「Ra vậy. Có thể sẽ thú vị đấy. Vì là quê hương nơi mình sinh ra và lớn lên,\ntưởng chừng như đã biết rõ mọi ngóc ngách, nên ngược lại」
- Mới: 「Ừ. Nếu thử đóng vai du khách đến thăm,\nchị nghĩ mình sẽ thấy được một Ohitoyo mà chị chưa từng biết」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1285 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: Ohimitera→Ohitoyo.

### 1175 — 真闇 — misaligned
- JP: 「あぁ」
- TW: 「嗯」
- Cũ: 「Em chỉ đang mải suy nghĩ thôi.\nCăn phòng này, trong thời gian ngắn đã thay đổi công năng bao nhiêu lần rồi nhỉ」
- Mới: 「À」
- Lý do: Dòng này bị lệch (bản cũ là của key 1283); JP chỉ là 'あぁ' — dùng lại 'À' như key 1199 (lặp hợp lệ, cùng một tiếng cảm thán).

### 1177 — 真闇 — misaligned
- JP: 「うん。よかよ」
- TW: 「嗯，好啊」
- Cũ: 「Wawawa! Reina không biết luôn!\nÀ này, chị Mayami, Reina, sắp hét to nha」
- Mới: 「Ừ. Được thôi」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1036 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: bản thu hồi 'Ừ. Được thôi' khớp JP 'うん。よかよ'.

### 1181 — 真闇 — misaligned
- JP: 「うん、まっことすごかとねぇ。\nおねーちゃんも、こぎゃん景色は初めて見ると」
- TW: 「嗯，是真的很壯觀。我還是第一次看到這樣的景色」
- Cũ: 「Waaa! Tuyệt quá đi ạ!\nThành phố Ohimitera, trở nên nhỏ xíu luôn ạ」
- Mới: 「Ừ, thật sự tuyệt vời quá nhỉ.\nChị cũng, lần đầu tiên nhìn thấy cảnh sắc như thế này đó」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1457 — lấy nguyên văn về đây.

### 1190 — 双鉄 — misaligned
- JP: 「ん？　それならば何故」
- TW: 「嗯？為什麼啊」
- Cũ: 「Không đâu.\nChị vẫn chưa ngủ, chỉ nhắm mắt thôi」
- Mới: 「Hửm? Vậy tại sao」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1040 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: bản thu hồi 'Hửm? Vậy tại sao' khớp JP 'ん？ それならば何故'.

### 1194 — 真闇 — misaligned
- JP: 「んふふっ、ようやく、もうすぐよねぇ。\nごめんね？　おねえちゃんが待たせる形になっちゃって」
- TW: 「嘻嘻，終於快要到了。對不起啦，要讓你等一等了」
- Cũ: 「Nhưng, đêm nay——hay nói đúng hơn là một thời gian tới, em muốn kiềm chế lại.\nDù sao thì, kỳ nghỉ cho tuần trăng mật cũng」
- Mới: 「Ưm fufu, cuối cùng, cũng sắp đến rồi nhỉ.\nXin lỗi em nhé? Chị lại bắt em phải chờ đợi rồi」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1271 — lấy nguyên văn về đây.

### 1196 — れいな — misaligned
- JP: 「うふふぅ、そうてつさんも楽しそう！\n楽しいですもんねぇ、お空。こぉんなに広いんですねぇ」
- TW: 「嘻嘻，雙鐵先生也很開心的樣子！飛在天上真的很開心啊，天空這麼大」
- Cũ: Có tựa đầu siêu cao cấp thế kia, tất nhiên rồi.\nKhoảnh khắc nghĩ vậy, tôi tự nhận thức được sự ghen tị thoáng qua, rồi bật cười.
- Mới: 「Ufufuu, anh Soutetsu trông cũng vui quá kìa!\nVui lắm đúng không ạ, bầu trời. Rộng lớn đến nhường này cơ mà」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1311 — lấy nguyên văn về đây.

### 1197 — れいな — misaligned
- JP: 「うふふぅ、乗り心地最高でぇす。\nさすが、そうてつさんごじまんのナビさんですねぇ」
- TW: 「嘿嘿，坐起來真舒服。不愧是雙鐵先生引以為傲的Ｎａｖｉ小姐」
- Cũ: Giọng nói lần này, mang theo sự nũng nịu và vòi vĩnh.\nĐáp lại điều đó, tôi lặng lẽ trao một nụ hôn chúc ngủ ngon.
- Mới: 「Ufufuu, cảm giác ngồi tuyệt vời quá đi ạ.\nĐúng là Navi mà anh Soutetsu luôn tự hào có khác nha」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1372 — lấy nguyên văn về đây.

### 1203 — 双鉄 — misaligned
- JP: 「空もいいが、眼下の景色もすばらしいぞ。\nいつもの町も、地上から見るのとはまるで違う」
- TW: 「天空自然漂亮，下面的景色也不遜色。平時住的地方從天上看會有完全不一樣的感覺」
- Cũ: Dù nụ cười của tôi có phần tự trào, nhưng Reina\nlại đón nhận nó một cách rất tích cực. Vậy thì cứ ngoan ngoãn hùa theo thôi.
- Mới: 「Bầu trời cũng đẹp, nhưng cảnh sắc bên dưới cũng tuyệt vời lắm đấy.\nThị trấn quen thuộc, nhìn từ trên cao hoàn toàn khác biệt so với dưới mặt đất」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1306 — lấy nguyên văn về đây.

### 1207 — 双鉄 — misaligned
- JP: 「しかし、僕らにはナビもある。日ノ本国内であれば、\nどこへでもいける日程だとも考えられる」
- TW: 「好在我們還有Ｎａｖｉ。只要是在日本國內，哪裡都可以去」
- Cũ: 「Chúng ta chỉ chắc chắn có thể cùng nhau nghỉ phép trong hai ngày.\nRõ ràng là không thể đi du lịch dài ngày được」
- Mới: 「Nhưng, chúng ta có Navi. Nếu ở trong nội địa Hinomoto,\nthì lịch trình này đủ để đi bất cứ đâu」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1084 — lấy nguyên văn về đây.

### 1209 — 双鉄 — misaligned
- JP: 「わかった。であらば僕に否やはない。\nが――なぜ御一夜に？」
- TW: 「好的。既然如此我也不會有異議。但是為什麼選在御一夜？」
- Cũ: Nhẹ nhàng. Nhưng đầy kiên quyết.\nGiọng nói của chị Mayami vẫn như mọi khi, không chút do dự.
- Mới: 「Tôi hiểu rồi. Nếu vậy tôi không có ý kiến gì.\nNhưng——tại sao lại là Ohitoyo?」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1402 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: 'Em'→'Tôi' ×2 (Soutetsu tự xưng với Mayami) và Ohimitera→Ohitoyo.

### 1213 — れいな — misaligned
- JP: 「はぁい。れいな必ずそうしまぁす」
- TW: 「好的，玲奈下次會記得的」
- Cũ: 「Lần sau muốn hét to,\nthì báo trước cho chị một tiếng là được rồi」
- Mới: 「Vâng ạ. Reina nhất định sẽ làm vậy ạ」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1671 — lấy nguyên văn về đây.

### 1214 — 真闇 — misaligned
- JP: 「お家やらお部屋やらにもしも気持ちがあるんなら、\nそりゃあ幸せに決まっとるでしょお」
- TW: 「如果住宅和房間有感情的話，它們一定會感覺很幸福」
- Cũ: Chị Mayami cười khúc khích, nhẹ nhàng vuốt ve má tôi.
- Mới: 「Nếu nhà cửa hay phòng ốc mà có cảm xúc,\nthì chắc chắn chúng sẽ thấy hạnh phúc rồi」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1448 — lấy nguyên văn về đây.

### 1219 — 真闇 — terminology
- JP: 「おねえちゃん的には、お風呂もご飯も御一夜ですませて。\nお宿ばついたら、寝るのだけを堪能したいかなぁって」
- TW: 「姐姐想在御一夜泡澡吃飯，到了旅館就只睡覺了」
- Cũ: 「Theo ý chị thì, cứ tắm rửa và ăn tối xong xuôi ở Ohimitera đi.\nĐến nhà trọ rồi thì chỉ muốn tận hưởng giấc ngủ thôi」
- Mới: 「Theo ý chị thì, cứ tắm rửa và ăn tối xong xuôi ở Ohitoyo đi.\nĐến nhà trọ rồi thì chỉ muốn tận hưởng giấc ngủ thôi」
- Lý do: Chỉ sai thuật ngữ: Ohimitera→Ohitoyo.

### 1227 — 双鉄 — misaligned
- JP: 「栄えていく、か。\n姉弟が夫婦になれば、その可能性はふくらむな」
- TW: 「家庭興旺啊。姐弟結成夫妻之後，就有人丁興旺的可能性了」
- Cũ: Gật đầu rồi tôi chợt thấy kỳ lạ.\nTừ khi Hachiroku gia nhập, số lượng thành viên trong gia đình đâu có tăng thêm.
- Mới: 「Hưng thịnh, sao.\nChị em trở thành vợ chồng, khả năng đó sẽ lớn dần lên nhỉ」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1504 — lấy nguyên văn về đây.

### 1241 — 真闇 — misaligned
- JP: 「れーちゃん！\nうふふっ、かわゆかガイドさんしてくれそうね」
- TW: 「小玲！嘿嘿，她做嚮導一定很可愛」
- Cũ: 「Chị Mayami. Trong số những người không có bất kỳ mối quan hệ làm ăn nào với xưởng rượu Migita System,\nchúng ta thử nhờ Reina làm hướng dẫn viên thì sao?」
- Mới: 「Bé Reina!\nUfufu, chắc em ấy sẽ là một hướng dẫn viên đáng yêu lắm đây」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1764 — lấy nguyên văn về đây.

### 1243 — 双鉄 — misaligned
- JP: 「物であるハチロクが、確かな魂をもつように。\nあるいはこの部屋も、もしも魂をもつものならば」
- TW: 「就像八六作為物件卻有著靈魂，這房間或許也有靈魂」
- Cũ: Khi còn là phòng của tôi và Hachiroku, mùi sắt khá nồng,\nnhưng giờ tôi cảm giác nó đã chuyển thành hương men kōji thoang thoảng.
- Mới: 「Giống như Hachiroku, dù là đồ vật nhưng lại có linh hồn.\nCó lẽ căn phòng này, nếu nó cũng có linh hồn」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1769 — lấy nguyên văn về đây.

### 1245 — れいな — terminology
- JP: 「ですですぅ。その点、鉄道だったら、御一夜鉄道自慢の\nキハ07sが臨時停車で、らくらくつれていきますよぉ」
- TW: 「就是啊。在這個問題上利用鐵路的話，坐著御一夜鐵路引以為傲的Ｋｉｈａ０７Ｓ，然後臨時停車就能輕鬆抵達了」
- Cũ: 「Đúng rồi ạ. Về điểm này, nếu đi tàu thì\nKiha 07S tự hào của Đường sắt Ohito sẽ dừng đỗ tạm thời, đưa anh chị đến nơi dễ dàng luôn nha」
- Mới: 「Đúng rồi ạ. Về điểm này, nếu đi tàu thì\nKiha 07S tự hào của Đường sắt Ohitoyo sẽ dừng đỗ tạm thời, đưa anh chị đến nơi dễ dàng luôn nha」
- Lý do: Chỉ sai thuật ngữ: 'Đường sắt Ohito'→'Đường sắt Ohitoyo'.

### 1247 — 双鉄 — misaligned
- JP: 「とのことだ。\n聞こえていても、この高さまでは飛んでこれんのだろう」
- TW: 「就是這樣。就算它能聽見，也飛不到這個高度」
- Cũ: Quả là một chiếc thuyền cứu sinh kịp thời——à không, máy bay cứu sinh mới đúng.
- Mới: 「Là vậy đó.\nDù có nghe thấy, chắc anh ấy cũng không bay lên được độ cao này đâu」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1092 — lấy nguyên văn về đây.

### 1249 — 双鉄 — misaligned
- JP: 「この変遷が部屋にとっても幸せなものであって欲しいと。\nそのようなことを、なんともぼんやり考えていた」
- TW: 「希望這些變遷對於這房間來說也是一件幸福的事情。我剛才呆呆地想著這個」
- Cũ: Vừa nói ra tôi đã thấy mình như đang lảm nhảm,\nnhưng chị Mayami lại gật gù, vui vẻ hùa theo.
- Mới: 「Tôi hy vọng sự biến đổi này cũng là một niềm hạnh phúc đối với căn phòng.\nTôi cứ vẩn vơ suy nghĩ những điều như vậy」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1119 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: 'Em'→'Tôi' ×2 (độc thoại Soutetsu, tự xưng với Mayami).

### 1257 — 真闇 — misaligned
- JP: 「いままで一度も旅したことない、大評判の観光地。\nやけん、『観光旅行』ばしてみたかとよ」
- TW: 「御一夜是備受好評的觀光地，我卻從來沒在那裡旅遊過。所以我想來一次觀光旅行」
- Cũ: Ngay cả khi đã trở thành vợ chồng,\ncách xưng hô giữa tôi và chị Mayami vẫn không hề thay đổi.
- Mới: 「Một địa điểm du lịch nổi tiếng mà chị chưa từng đến thăm bao giờ.\nNên, chị muốn thử đi 『Du lịch ngắm cảnh』 xem sao」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1417 — lấy nguyên văn về đây.

### 1264 — 真闇 — misaligned
- JP: 「どぎゃんしたと、双ちゃん？」
- TW: 「怎麼啦，小雙？」
- Cũ: 
- Mới: 「Sao thế, Sou-chan?」
- Lý do: Dòng CHƯA DỊCH (VN trống — 1 trong 2 dòng chưa dịch còn lại toàn dự án); bản dịch đúng 'Sao thế, Sou-chan?' nằm ở key 1744 — thu hồi về đây, không dịch mới.

### 1271 — 双鉄 — misaligned
- JP: 「お互い様だ。\n僕もまったく、スケジュールの調整がきかなかった」
- TW: 「我也一樣。我也完全沒能調整好日程」
- Cũ: 「Ưm fufu, cuối cùng, cũng sắp đến rồi nhỉ.\nXin lỗi em nhé? Chị lại bắt em phải chờ đợi rồi」
- Mới: 「Cả hai đều vậy mà.\nTôi cũng hoàn toàn không thể sắp xếp được lịch trình」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1634 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: 'Em'→'Tôi' (Soutetsu tự xưng với Mayami).

### 1273 — 双鉄 — misaligned
- JP: 「僕もそのように考えていた。\nとなると凪にも頼めんな。常連さん相手は気をつかう」
- TW: 「我也是這麼想的。那也不能拜託凪了，面對常客也會有顧慮」
- Cũ: 「Nếu được cho xem bên trong ngân hàng thì chắc sẽ vui lắm,\nnhưng chuyện đó để dịp khác ngoài tuần trăng mật cũng được nhỉ」
- Mới: 「Tôi cũng nghĩ vậy.\nVậy thì cũng không thể nhờ Nagi được. Đối mặt với khách quen sẽ rất ngại」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 669 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: 'Em'→'Tôi' (Soutetsu tự xưng với Mayami).

### 1280 — 双鉄 — misaligned
- JP: 「確実にふたり一緒に休みを取れるのは二日間。\n長期の旅行が無理な日程であることは確かだが」
- TW: 「我們能一起休兩天時間。這樣肯定就不能長期旅行了」
- Cũ: Cuối cùng thì lịch trình của cả hai cũng khớp nhau.\nDo đó, việc chuẩn bị cho tuần trăng mật hầu như vẫn chưa tiến triển gì.
- Mới: 「Chúng ta chỉ chắc chắn có thể cùng nhau nghỉ phép trong hai ngày.\nRõ ràng là không thể đi du lịch dài ngày được」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1207 — lấy nguyên văn về đây.

### 1281 — 双鉄 — pronoun
- JP: 「せっかく空の上にいるのだ。町を見ながら、\n新婚旅行のコースについてを考えたいのだが」
- TW: 「我們飛到了天上，要利用這個機會看著御一夜，考慮一下新婚旅行的路線」
- Cũ: 「Nhân lúc đang ở trên không. Vừa ngắm nhìn thị trấn,\nem muốn bàn về lịch trình cho tuần trăng mật」
- Mới: 「Nhân lúc đang ở trên không. Vừa ngắm nhìn thị trấn,\ntôi muốn bàn về lịch trình cho tuần trăng mật」
- Lý do: Soutetsu tự xưng 'em' với Mayami — phải là 'tôi'.

### 1283 — 双鉄 — misaligned
- JP: 「物思いにふけっていただけなのだ。\nこの部屋も、短い時間に何度も用途がかわったものだと」
- TW: 「我只是陷入了沉思而已。我想到了這房間在短時間內用途變化了好幾次」
- Cũ: Cơ thể tôi ngập tràn hạnh phúc đến mức tự động bật cười.\nNhận ra điều đó, khuôn mặt tôi lại giãn ra.
- Mới: 「Tôi chỉ đang mải suy nghĩ thôi.\nCăn phòng này, trong thời gian ngắn đã thay đổi công năng bao nhiêu lần rồi nhỉ」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1175 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: 'Em'→'Tôi' (Soutetsu tự xưng với Mayami).

### 1285 — 双鉄 — misaligned
- JP: 「了解だ。\nとなると、ガイド選びが重要になるな」
- TW: 「我明白了。那讓誰來做嚮導就很重要了」
- Cũ: 「Ừ. Nếu thử đóng vai du khách đến thăm,\nchị nghĩ mình sẽ thấy được một Ohimitera mà chị chưa từng biết」
- Mới: 「Đã rõ.\nVậy thì, việc chọn hướng dẫn viên sẽ rất quan trọng đây」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1770 — lấy nguyên văn về đây.

### 1287 — ナビ — misaligned
- JP: 「御一夜の町を一望できるこの高度では、\n飛翔している雀を見ることは全くありません」
- TW: 「我沒在這個能把御一夜盡收眼底的高度看到過麻雀」
- Cũ: 「Ưm……Chuyện đó thì——」
- Mới: 「Ở độ cao có thể bao quát toàn cảnh thành phố Ohitoyo này,\nhoàn toàn không thể nhìn thấy chim sẻ đang bay đâu ạ」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1789 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: Ohimitera→Ohitoyo.

### 1289 — 双鉄 — pronoun
- JP: 「僕は無論、真闇姉のペースにあわせるが」
- TW: 「我當然是配合真闇姐」
- Cũ: 「Anh thì dĩ nhiên là theo nhịp độ của chị Mayami rồi」
- Mới: 「Tôi thì dĩ nhiên là theo nhịp độ của chị Mayami rồi」
- Lý do: Soutetsu tự xưng 'Anh' với Mayami — phải là 'tôi'.

### 1290 — 真闇 — misaligned
- JP: 「えっと、線路ば最初に見つけて」
- TW: 「我看看，先找到鐵路」
- Cũ: 「Nè, nè. Chị Mayami.\nCửa hàng đường sắt ở đâu vậy ạ?」
- Mới: 「Để xem, trước tiên tìm đường ray đã」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1487 — lấy nguyên văn về đây.

### 1292 — 双鉄 — misaligned
- JP: 「笑っていたか。そんな自覚はなかったのだが――」
- TW: 「我笑了啊。我自己沒發現——」
- Cũ: 「Em không tự nhận ra sao?\nEm vừa cười khúc khích đấy, Sou-chan. Như đang nhớ lại chuyện gì vui vậy」
- Mới: 「Tôi cười sao. Tôi không nhận ra luôn đấy——」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1641 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: 'Em'→'Tôi' ×2 (Soutetsu tự xưng với Mayami).

### 1295 — 双鉄 — misaligned
- JP: 「無論、いつでも望むところだ」
- TW: 「我隨時願意」
- Cũ: 「Sou-chan sẽ làm cho gia đình hưng thịnh sao?\nCùng với chị」
- Mới: 「Tất nhiên, lúc nào tôi cũng sẵn sàng」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1732 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: 'em'→'tôi' (Soutetsu tự xưng với Mayami).

### 1306 — ナビ — misaligned
- JP: 「かしこまりました。旋回します」
- TW: 「明白了，開始旋迴」
- Cũ: 「Bầu trời cũng đẹp, nhưng cảnh sắc bên dưới cũng tuyệt vời lắm đấy.\nThị trấn quen thuộc, nhìn từ trên cao hoàn toàn khác biệt so với dưới mặt đất」
- Mới: 「Đã rõ. Tiến hành xoay vòng」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1097 — lấy nguyên văn về đây.

### 1311 — 双鉄 — misaligned
- JP: 「だな」
- TW: 「是啊」
- Cũ: 「Ufufuu, anh Soutetsu trông cũng vui quá kìa!\nVui lắm đúng không ạ, bầu trời. Rộng lớn đến nhường này cơ mà」
- Mới: 「Đúng vậy」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1647 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: bản thu hồi 'Đúng vậy' (lặp hợp lệ như key 1231) khớp JP 'だな'.

### 1324 — 真闇 — misaligned
- JP: 「家族あってのおうちやけん。\n栄えていくんは、願ったり叶ったりでしょお」
- TW: 「有家人才有家。住宅肯定也喜歡家庭興旺」
- Cũ: Nhà, và tổ ấm. Lần đầu tiên nghe hai từ này đặt cạnh nhau,\ntôi mới hiểu ra sự khác biệt giữa một công trình kiến trúc và một gia đình.
- Mới: 「Có gia đình mới thành tổ ấm.\nSự hưng thịnh, chẳng phải là điều mà chúng hằng mong ước sao」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1447 — lấy nguyên văn về đây.

### 1331 — 真闇 — misaligned
- JP: 「んーん、さっきも言うたよ？\nおねーちゃん、寝てなかったけん」
- TW: 「沒有，我剛才也說過啦，我沒有睡著」
- Cũ: 「Thật tốt khi có thể bàn bạc theo một cách không ngờ tới.\nNhưng, thật sự xin lỗi vì đã đánh thức chị」
- Mới: 「Không đâu, nãy chị cũng nói rồi mà?\nChị, vẫn chưa ngủ đâu」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1443 — lấy nguyên văn về đây.

### 1332 — 真闇 — misaligned
- JP: 「ううん。\nまだ寝入らんで目ば閉じとっただけやったけん」
- TW: 「沒有，我還沒睡，只是閉上眼睛而已」
- Cũ: 「A, xin lỗi,\nem làm chị thức giấc à?」
- Mới: 「Không đâu.\nChị vẫn chưa ngủ, chỉ nhắm mắt thôi」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1190 — lấy nguyên văn về đây.

### 1333 — 双鉄 — pronoun
- JP: 「なのだ。ゆえにこの急な土砂降りは気を使うなと、\nれいなと話していたのだが――」
- TW: 「沒錯。所以我剛才和玲奈說一下這麼大雨得注意了——」
- Cũ: 「Đúng vậy. Thế nên anh mới nói với Reina rằng\ncơn mưa xối xả đột ngột này sẽ rất mệt mỏi đấy——」
- Mới: 「Đúng vậy. Thế nên tôi mới nói với Reina rằng\ncơn mưa xối xả đột ngột này cần phải cẩn thận đấy——」
- Lý do: Soutetsu tự xưng 'anh' với Mayami — phải là 'tôi'; đồng thời '気を使う' bị dịch sai thành 'sẽ rất mệt mỏi' — JP nói 'cần phải chú ý/cẩn thận' (TW: '得注意了').

### 1335 — 真闇 — misaligned
- JP: 「そうよ、れーちゃん。\nおねえちゃんのお膝の上ば、今日はれーちゃんの特等席」
- TW: 「沒錯，小玲。今天姐姐的腿上就是小玲的特等座」
- Cũ: Sự đính chính nghiêm túc của Navi, khiến chị Mayami nở nụ cười ấm áp.
- Mới: 「Đúng rồi đó, bé Reina.\nTrên đùi chị, hôm nay là ghế đặc biệt của bé Reina đó」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1351 — lấy nguyên văn về đây.

### 1344 — 真闇 — misaligned
- JP: 「はーちゃんがやってきて。\nはーちゃんはひーちゃんの部屋におひっこしして」
- TW: 「然後八六來了。八六又搬到了小日的房間」
- Cũ: 「Đầu tiên là phòng sách của ông Taito.\nSau đó em được dùng làm phòng riêng」
- Mới: 「Rồi Haa-chan đến.\nSau đó Haa-chan lại chuyển sang phòng của Hii-chan」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1399 — lấy nguyên văn về đây.

### 1351 — れいな — misaligned
- JP: 「とくとうせき！」
- TW: 「特等座！」
- Cũ: 「Đúng rồi đó, bé Reina.\nTrên đùi chị, hôm nay là ghế đặc biệt của bé Reina đó」
- Mới: 「Ghế đặc biệt!」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1788 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: bản thu hồi 'Ghế đặc biệt!' khớp JP 'とくとうせき！'.

### 1360 — 双鉄 — pronoun
- JP: 「今は代わりなど務めていない。日々姫も僕のいもうとだ、\n妻の妹という意味ではなくて、僕自身のいもうとだから」
- TW: 「現在我也不是代替照顧她。日日姬是我的妹妹，不是我妻子妹妹的意思，而是我自己的妹妹」
- Cũ: 「Bây giờ em không làm người thay thế nữa. Hibiki cũng là em gái của em,\nkhông phải với tư cách là em gái của vợ, mà là em gái của chính em」
- Mới: 「Bây giờ tôi không làm người thay thế nữa. Hibiki cũng là em gái của tôi,\nkhông phải với tư cách là em gái của vợ, mà là em gái của chính tôi」
- Lý do: Soutetsu tự xưng 'em' ×3 với Mayami — phải là 'tôi'.

### 1361 — 双鉄 — misaligned
- JP: 「思わぬ形で打ち合わせができてよかった。\nが、起こしてしまったのは本当にすまなかった」
- TW: 「用意想不到的方式商量了一下問題是好事。但是把你吵醒真的是很抱歉」
- Cũ: Giống như hùa theo, lại giống như nói mớ.\nGiọng nói cho thấy cơn buồn ngủ đã quay trở lại.
- Mới: 「Thật tốt khi có thể bàn bạc theo một cách không ngờ tới.\nNhưng, thật sự xin lỗi vì đã đánh thức chị」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1331 — lấy nguyên văn về đây.

### 1363 — 双鉄 — pronoun
- JP: 「あのころは――あのころの僕ならば、うん。確かに\n"代わり”を義務として果たしていたかもしれんが……」
- TW: 「當時——當時的我，確實可能做到了“代替”的職責……」
- Cũ: 「Hồi đó thì——nếu là em của hồi đó, ừm. Chắc chắn là\nem đã làm "người thay thế" như một nghĩa vụ, nhưng……」
- Mới: 「Hồi đó thì——nếu là tôi của hồi đó, ừm. Chắc chắn là\ntôi đã làm "người thay thế" như một nghĩa vụ, nhưng……」
- Lý do: Soutetsu tự xưng 'em' ×2 với Mayami — phải là 'tôi'.

### 1364 — 双鉄 — misaligned
- JP: 「無論だ。真闇姉の時間がとれるのであれば」
- TW: 「當然了。如果你有時間的話」
- Cũ: 「Hơn nữa, nè? Nếu có thể nhờ bé Reina làm hướng dẫn viên.\nChị cũng có thể tham gia vào buổi bàn bạc chi tiết được không?」
- Mới: 「Tất nhiên rồi. Nếu chị Mayami có thời gian」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1007 — lấy nguyên văn về đây.

### 1365 — 真闇 — misaligned
- JP: 「そんなん。[いえ]家ゆーもんは、おうちやけんね」
- TW: 「當然因為住宅就是家啊」
- Cũ: 「Chị khẳng định thế sao. Rốt cuộc là vì lý do gì」
- Mới: 「Thì đó. Nhà, là tổ ấm mà」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1576 — lấy nguyên văn về đây.

### 1366 — 真闇 — misaligned
- JP: 「もちろんとっても素敵なことよ。\n過保護も、親ばかも、子煩悩も」
- TW: 「當然是好事啊。不管是溺愛，過於疼愛小孩，還是一心只想著孩子都是好事」
- Cũ: 「Fufu, nghe cách nói của chị Mayami,\nlại thấy việc bao bọc quá mức là một điều rất tốt」
- Mới: 「Tất nhiên là một điều rất tuyệt vời rồi.\nDù là bao bọc quá mức, nuông chiều con cái, hay yêu thương con hết mực」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1778 — lấy nguyên văn về đây.

### 1372 — ナビ — misaligned
- JP: 「真闇様のお膝の上は、当機の標準装備ではありません」
- TW: 「真暗女士大腿上的位置不是本機的標準配置」
- Cũ: 「Ufufuu, cảm giác ngồi tuyệt vời quá đi ạ.\nĐúng là Navi mà anh Soutetsu luôn tự hào có khác nha」
- Mới: 「Trên đùi của phu nhân Mayami, không phải là trang bị tiêu chuẩn của cỗ máy này」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1080 — lấy nguyên văn về đây.

### 1376 — 双鉄 — misaligned
- JP: 「真闇姉。右田一酒造元と一切の取引関係が無い中でなら、\nれいなにガイドを頼んでみるのはどうであろうか」
- TW: 「真闇姐。在右田一釀酒廠完全沒有生意來往的人裡，讓玲奈來做嚮導怎麼樣」
- Cũ: ……Paulette thì quá bận rộn,\nnếu nhờ vả, cô ấy có thể sẽ cố sức nhận lời——a
- Mới: 「Chị Mayami. Trong số những người không có bất kỳ mối quan hệ làm ăn nào với xưởng rượu Migita Ichi,\nchúng ta thử nhờ Reina làm hướng dẫn viên thì sao?」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1241 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: Migita System→Migita Ichi (thuật ngữ đã chốt).

### 1379 — 双鉄 — misaligned
- JP: 「心得た。が、確実に引き受けてもらえるとは限らん。\nダメだったときの第二候補はどうしよう」
- TW: 「知道了。但是她不一定能接受。不行的話要準備一個第二候補」
- Cũ: 「30 phút hay 1 tiếng thì lúc nào cũng xoay sở được.\nVậy thì, cùng nhau nhé. Nếu em ấy nhận lời」
- Mới: 「Đã rõ. Nhưng, không chắc chắn là em ấy sẽ nhận lời đâu.\nNếu không được thì ứng cử viên thứ hai sẽ là ai đây」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1456 — lấy nguyên văn về đây.

### 1390 — 双鉄 — misaligned
- JP: 「稀咲、ふかみあたりも……\n蔵の方との絡みもあるから気を使ってしまうだろうな」
- TW: 「稀咲和深美也不行……因為她們和酒藏有關係，會有所顧慮」
- Cũ: Nếu vậy thì……ừm. Loại Hibiki và Hachiroku khỏi danh sách ứng cử viên thôi.\nChuyến du lịch gia đình có cả hai người họ nên để dịp khác.
- Mới: 「Cỡ Kisaki, hay Fukami thì……\ncũng có liên quan đến xưởng rượu nên chắc sẽ ngại ngùng nhỉ」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1415 — lấy nguyên văn về đây.

### 1399 — 双鉄 — misaligned
- JP: 「そうして今は、僕ら夫婦の寝室だ」
- TW: 「而現在，它是我們夫妻的臥室」
- Cũ: 「Rồi Haa-chan đến.\nSau đó Haa-chan lại chuyển sang phòng của Hii-chan」
- Mới: 「Và bây giờ, nó là phòng ngủ của vợ chồng mình」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1791 — lấy nguyên văn về đây.

### 1402 — 真闇 — misaligned
- JP: 「あんね？　双ちゃん。\n理由はとっても簡単なの」
- TW: 「聽我說，小雙。理由非常簡單」
- Cũ: 「Em hiểu rồi. Nếu vậy em không có ý kiến gì.\nNhưng——tại sao lại là Ohimitera?」
- Mới: 「Biết không? Sou-chan.\nLý do rất đơn giản」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1585 — lấy nguyên văn về đây.

### 1415 — 真闇 — misaligned
- JP: 「銀行さんの中見せてもらえるとかなら楽しそうばってん、\nそいば新婚旅行とは別の機会でよかとよね」
- TW: 「要是能參觀一下銀行裡面應該會很有趣，不過那等到新婚旅行之外的機會吧」
- Cũ: 「Cỡ Kisaki, hay Fukami thì……\ncũng có liên quan đến xưởng rượu nên chắc sẽ ngại ngùng nhỉ」
- Mới: 「Nếu được cho xem bên trong ngân hàng thì chắc sẽ vui lắm,\nnhưng chuyện đó để dịp khác ngoài tuần trăng mật cũng được nhỉ」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1273 — lấy nguyên văn về đây.

### 1417 — 双鉄 — misaligned
- JP: 「観光旅行、か」
- TW: 「觀光旅行啊」
- Cũ: 「Một địa điểm du lịch nổi tiếng mà chị chưa từng đến thăm bao giờ.\nNên, chị muốn thử đi 『Du lịch ngắm cảnh』 xem sao」
- Mới: 「Du lịch ngắm cảnh, sao」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1649 — lấy nguyên văn về đây.

### 1422 — 真闇 — misaligned
- JP: 「商工会とかのガイドさんはちょっと。\nおねえちゃん、きっと妙に気を使っちゃいそうやけん」
- TW: 「讓商工會來做嚮導不太好。我肯定會有些顧慮」
- Cũ: Vừa dứt lời, chị Mayami cựa quậy nhích người lại gần.
- Mới: 「Hướng dẫn viên của Phòng Thương mại thì hơi...\nChị chắc chắn sẽ thấy gượng gạo lắm」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1026 — lấy nguyên văn về đây.

### 1443 — 双鉄 — misaligned
- JP: 「そうか、ならば今度こそ眠ろう。\nお互い、朝の早い仕事だ」
- TW: 「這樣啊，那現在就去睡吧。我們的工作都需要早起」
- Cũ: 「Không đâu, nãy chị cũng nói rồi mà?\nChị, vẫn chưa ngủ đâu」
- Mới: 「Vậy sao, vậy thì lần này ngủ thật nhé.\nCả hai ta, đều có công việc phải dậy sớm mà」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1790 — lấy nguyên văn về đây.

### 1446 — 双鉄 — misaligned
- JP: 「一番最初は汰斗さんの書庫だった。\nそれを僕の私室として使わせてもらって」
- TW: 「這裡最開始是汰斗先生的書房。之後用作我的房間」
- Cũ: Giọng nói vui vẻ.\nViệc tâm tư được thấu hiểu khiến tôi cũng thấy vui lây.
- Mới: 「Đầu tiên là phòng sách của ông Taito.\nSau đó tôi được dùng nó làm phòng riêng」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1344 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: 'em'→'tôi' và thêm 'nó' — bản cũ 'được dùng làm phòng riêng' gây nhầm chủ ngữ (Soutetsu bị dùng làm phòng).

### 1447 — 双鉄 — misaligned
- JP: 「言われてみれば、確かにそうだな」
- TW: 「這麼一說是有道理」
- Cũ: 「Có gia đình mới thành tổ ấm.\nSự hưng thịnh, chẳng phải là điều mà chúng hằng mong ước sao」
- Mới: 「Nghe chị nói vậy, đúng là thế thật」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1654 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: bản thu hồi 'Nghe chị nói vậy, đúng là thế thật' khớp JP '言われてみれば、確かにそうだな'.

### 1448 — 双鉄 — misaligned
- JP: 「断言か。それはいったいどうした理由で」
- TW: 「這麼肯定嗎。為什麼這麼說？」
- Cũ: 「Nếu nhà cửa hay phòng ốc mà có cảm xúc,\nthì chắc chắn chúng sẽ thấy hạnh phúc rồi」
- Mới: 「Chị khẳng định thế sao. Rốt cuộc là vì lý do gì」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1365 — lấy nguyên văn về đây.

### 1456 — 真闇 — misaligned
- JP: 「そぎゃんこつは、断られてから考えればよかよ。\n抑えばあると、どこか気がぬけてしまうもんやけん」
- TW: 「那個就等她拒絕了再想吧。要是先想好了，可能就會洩氣了」
- Cũ: 「Đã rõ. Nhưng, không chắc chắn là em ấy sẽ nhận lời đâu.\nNếu không được thì ứng cử viên thứ hai sẽ là ai đây」
- Mới: 「Chuyện đó, đợi bị từ chối rồi hẵng nghĩ.\nNếu có phương án dự phòng, tự nhiên sẽ thấy chùn bước mà」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1061 — lấy nguyên văn về đây.

### 1457 — れいな — misaligned
- JP: 「ね、ね。まくらさん。\nレールショップはどこですかぁ？」
- TW: 「那個，真暗小姐，鐵路商店在哪裡呀？」
- Cũ: 「Ừ, thật sự tuyệt vời quá nhỉ.\nChị cũng, lần đầu tiên nhìn thấy cảnh sắc như thế này đó」
- Mới: 「Nè, nè. Chị Mayami.\nCửa hàng đường sắt ở đâu vậy ạ?」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1290 — lấy nguyên văn về đây.

### 1460 — 双鉄 — pronoun
- JP: 「ならば、鉄道で確定しよう。ポーレットが単独乗務する\nキハ07sに、乗ってみたくも思うしな」
- TW: 「那就用鐵路吧。正好也想坐坐波萊特單獨乘務的Ｋｉｈａ０７Ｓ」
- Cũ: 「Vậy thì chốt đi tàu nhé. Em cũng muốn thử đi\nKiha 07S do Paulette lái một mình xem sao」
- Mới: 「Vậy thì chốt đi tàu nhé. Tôi cũng muốn thử đi\nKiha 07S do Paulette lái một mình xem sao」
- Lý do: Soutetsu tự xưng 'Em' với Mayami — phải là 'tôi'.

### 1462 — 真闇 — terminology
- JP: 「じゃ、そこばガイドさんにおまかせで。\nガイドさんおすすめの、いっとう御一夜らしかとこ」
- TW: 「那就讓嚮導小姐來決定吧。我們去嚮導小姐覺得最有御一夜特色的地方」
- Cũ: 「Vậy thì, chỗ đó giao cho cô hướng dẫn viên đấy.\nMột nơi đậm chất Ohimitera nhất mà hướng dẫn viên đề xuất」
- Mới: 「Vậy thì, chỗ đó giao cho cô hướng dẫn viên đấy.\nMột nơi đậm chất Ohitoyo nhất mà hướng dẫn viên đề xuất」
- Lý do: Chỉ sai thuật ngữ: Ohimitera→Ohitoyo.

### 1474 — 真闇 — misaligned
- JP: 「ってことは、隈銀があれやけん――\nああ、うちん蔵も見えた」
- TW: 「那隈元銀行就在那邊了——啊，我家酒廠也看到了」
- Cũ: 「Đường ray đường ray……a! Kia rồi nha.\nVậy thì vậy thì——thấy rồi! Cửa hàng đường sắt!!」
- Mới: 「Nghĩa là, Kumagin ở đằng kia——\nA, thấy xưởng rượu nhà mình rồi」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1096 — lấy nguyên văn về đây.

### 1487 — れいな — misaligned
- JP: 「線路線路……あ！　あれですねぇ。\nそれならそれなら――あった！　レールショップぅ！！」
- TW: 「鐵路鐵路……啊！在那裡。然後然後——找到了！鐵路商店！！」
- Cũ: 「Để xem, trước tiên tìm đường ray đã」
- Mới: 「Đường ray đường ray……a! Kia rồi nha.\nVậy thì vậy thì——thấy rồi! Cửa hàng đường sắt!!」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1474 — lấy nguyên văn về đây.

### 1490 — 双鉄 — misaligned
- JP: 「そこは安心してくれて構わない。\n少しでも無理があるなら、ポーレットが引受けさせない」
- TW: 「關於這個就放心吧。只要她稍微有點處理不來，波萊特就不會讓她接受」
- Cũ: 「Nhưng mà, bé Reina cũng bận lắm đúng không?\nNếu làm em ấy phải cố sức dù chỉ một chút」
- Mới: 「Về chuyện đó chị cứ yên tâm.\nNếu có chút gì quá sức, Paulette sẽ không cho nhận đâu」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1144 — lấy nguyên văn về đây.

### 1494 — 双鉄 — terminology
- JP: 「その二箇所以外だと、8620牽引客車への乗車となるかな。\n湯医往復とはなってしまうが、投炭体験などもできる」
- TW: 「除了這兩個地方之外，還有８６２０牽引客車的搭車體驗吧。雖然這樣會變成湯醫往返，但還可以體驗加煤」
- Cũ: 「Ngoài hai nơi đó ra, chắc là đi tàu khách do 8620 kéo nhỉ.\nDù sẽ phải đi khứ hồi đến Yui, nhưng cũng có thể trải nghiệm xúc than dồn toa nữa」
- Mới: 「Ngoài hai nơi đó ra, chắc là đi tàu khách do 8620 kéo nhỉ.\nDù sẽ phải đi khứ hồi đến Yunoi, nhưng cũng có thể trải nghiệm xúc than nữa」
- Lý do: Yui→Yunoi; đồng thời bỏ 'dồn toa' — cụm này không có trong JP lẫn TW (cùng lỗi chèn thêm như quyết định 1027 của Hieu 20/11: bỏ 'dồn toa'). Gloss 'xúc than' cho 投炭 giữ nguyên (đa số trong file).

### 1504 — 双鉄 — misaligned
- JP: 「！」
- TW: 「！」
- Cũ: 「Hưng thịnh, sao.\nChị em trở thành vợ chồng, khả năng đó sẽ lớn dần lên nhỉ」
- Mới: 「!」
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1650 — lấy nguyên văn về đây. Đã chỉnh trong bản thu hồi: bản thu hồi '!' (lặp hợp lệ như key 1077/1650) khớp JP '！'.

### 1505 — 双鉄 — terminology
- JP: 「27Dだと最終列車になるな。\n21:35御一夜温泉駅発で、鱈木廃駅臨時停車が22:09」
- TW: 「２７Ｄ的話就是最後一班了。２１：３５從御一夜溫泉站出發，２２：０９在鱈木廢站臨時停車」
- Cũ: 「27D thì sẽ là chuyến tàu cuối cùng đấy.\nXuất phát từ ga Suối nước nóng Ohimitera lúc 21:35, dừng đỗ tạm thời tại ga bỏ hoang Taragi lúc 22:09」
- Mới: 「27D thì sẽ là chuyến tàu cuối cùng đấy.\nXuất phát từ ga Suối nước nóng Ohitoyo lúc 21:35, dừng đỗ tạm thời tại ga bỏ hoang Taragi lúc 22:09」
- Lý do: Chỉ sai thuật ngữ: Ohimitera→Ohitoyo.

### 1576 — monologue — misaligned
- JP: 家と、うち。両者の差異を並べて言われてみて初めて、\n建築物と家庭の差異かと理解する。
- TW: 住宅和家。把這兩個詞放在一起，就能體會出建築物和家庭的差異。
- Cũ: 「Thì đó. Nhà, là tổ ấm mà」
- Mới: Nhà, và tổ ấm. Lần đầu tiên nghe hai từ này đặt cạnh nhau,\ntôi mới hiểu ra sự khác biệt giữa một công trình kiến trúc và một gia đình.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1324 — lấy nguyên văn về đây.

### 1585 — monologue — misaligned
- JP: 夫と妻になったいまでも、\n真闇姉と僕の間の呼称はまったく変わらない。
- TW: 即使是結成了夫妻關係，真闇姐和我互相的稱呼也沒有發生任何改變。
- Cũ: 「Biết không? Sou-chan.\nLý do rất đơn giản」
- Mới: Ngay cả khi đã trở thành vợ chồng,\ncách xưng hô giữa tôi và chị Mayami vẫn không hề thay đổi.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1257 — lấy nguyên văn về đây.

### 1610 — monologue — terminology
- JP: 真闇姉の強い希望で、れいなは業務でガイドを受けた。\n御一夜鉄道観光部への、正式な依頼受注という形で。
- TW: 在真闇姐的強烈要求下，玲奈接受了嚮導的工作。我們是對御一夜鐵道觀光部提交了正式委託。
- Cũ: Thể theo nguyện vọng mạnh mẽ của chị Mayami, Reina đã nhận công việc hướng dẫn viên.\nDưới hình thức là một đơn đặt hàng chính thức gửi đến Bộ phận Du lịch của Đường sắt Ohito.
- Mới: Thể theo nguyện vọng mạnh mẽ của chị Mayami, Reina đã nhận công việc hướng dẫn viên.\nDưới hình thức là một đơn đặt hàng chính thức gửi đến Bộ phận Du lịch của Đường sắt Ohitoyo.
- Lý do: Chỉ sai thuật ngữ: 'Đường sắt Ohito'→'Đường sắt Ohitoyo'.

### 1616 — monologue — misaligned
- JP: 相槌のようで、うわごとのような。\n眠たさが戻ってきたなと感じる声。
- TW: 她好像是在附和我，又好像是在說夢話。她似乎又有睡意了。
- Cũ: 「Ưm……」
- Mới: Giống như hùa theo, lại giống như nói mớ.\nGiọng nói cho thấy cơn buồn ngủ đã quay trở lại.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1361 — lấy nguyên văn về đây.

### 1619 — monologue — misaligned
- JP: 超極上のヘッドレストがついているゆえ、当然だろう。\n思った瞬間、僅かな嫉妬を自覚し、笑ってしまう。
- TW: 她的座下可是個超高級的頭枕，當然會感覺軟了。這個念頭掠過我的腦海，我察覺到自己有點嫉妒，不由地苦笑起來。
- Cũ: 「Ehehe, đúng là ghế đặc biệt có khác nha.\nCực kỳ êm ái và mềm mại luôn ạ」
- Mới: Có tựa đầu siêu cao cấp thế kia, tất nhiên rồi.\nKhoảnh khắc nghĩ vậy, tôi tự nhận thức được sự ghen tị thoáng qua, rồi bật cười.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1196 — lấy nguyên văn về đây.

### 1634 — monologue — misaligned
- JP: それがぽこん、と一致した。\nゆえ、新婚旅行の準備はまだほとんど進んでいない。
- TW: 我們的日程正好撞到一起。所以我們還完全沒做新婚旅行的準備。
- Cũ: 「Cả hai đều vậy mà.\nEm cũng hoàn toàn không thể sắp xếp được lịch trình」
- Mới: Cuối cùng thì lịch trình của cả hai cũng khớp nhau.\nDo đó, việc chuẩn bị cho tuần trăng mật hầu như vẫn chưa tiến triển gì.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1280 — lấy nguyên văn về đây.

### 1641 — monologue — misaligned
- JP: 身体が勝手に笑うほど、僕は幸せに満ち満ちている。\n実感すれば、顔がふたたび緩んでしまう。
- TW: 我已經幸福到了身體會不由自主地笑出來的程度。這麼一想，我的嘴角又揚了起來。
- Cũ: 「Em cười sao. Em không nhận ra luôn đấy——」
- Mới: Cơ thể tôi ngập tràn hạnh phúc đến mức tự động bật cười.\nNhận ra điều đó, khuôn mặt tôi lại giãn ra.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1283 — lấy nguyên văn về đây.

### 1647 — monologue — misaligned
- JP: どちらかといえば自嘲めいていた笑みを、けれどれいなは\n実に前向きに捉えてくれた。ならば素直に乗っかろう。
- TW: 我的笑容中其實帶著一些自嘲，但是玲奈卻從積極的角度來理解了。那我就按她說的做吧。
- Cũ: 「Đúng vậy」
- Mới: Dù nụ cười của tôi có phần tự trào, nhưng Reina\nlại đón nhận nó một cách rất tích cực. Vậy thì cứ ngoan ngoãn hùa theo thôi.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1203 — lấy nguyên văn về đây.

### 1649 — monologue — misaligned
- JP: 生家のあった小さな町をふと思い出す。\nあそこも一応、観光客の来る町だったが――
- TW: 我腦海裡浮現出我出生的那座小鎮。那裡的確是觀光客會去的地方——
- Cũ: 「Du lịch ngắm cảnh, sao」
- Mới: Tôi chợt nhớ đến thị trấn nhỏ nơi tôi sinh ra.\nNơi đó cũng được coi là một thị trấn có khách du lịch đến thăm, nhưng——
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1059 — lấy nguyên văn về đây.

### 1650 — monologue — misaligned
- JP: 理屈だけだった僕の言葉が、艶めいた相槌ひとつで、\n生々しいまでの温度を帯びる。
- TW: 我說的話本來只是陳述事實，可是加上真闇姐一聲嬌艷的回應，它就有了非常現實的感覺了。
- Cũ: 「!」
- Mới: Lời nói đầy lý trí của tôi, chỉ bằng một tiếng hùa theo đầy gợi cảm,\nđã mang theo hơi ấm sống động đến chân thực.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1039 — lấy nguyên văn về đây.

### 1654 — monologue — misaligned
- JP: うなずいてふと不思議に思う。\nハチロクが加わって以降、家族の人数は増えてない。
- TW: 我點點頭，又覺得有點不對。自從八六來了以後，家庭成員就沒有再增加了。
- Cũ: 「Nghe chị nói vậy, đúng là thế thật」
- Mới: Gật đầu rồi tôi chợt thấy kỳ lạ.\nTừ khi Hachiroku gia nhập, số lượng thành viên trong gia đình đâu có tăng thêm.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1227 — lấy nguyên văn về đây.

### 1657 — monologue — gasp
- JP: 思わぬところにれいなが食いつく。\n真闇姉は待ってましたとばかりに――っ！
- TW: 沒想到玲奈對這個提起興趣了。真闇姐則是一副“就等這句話了”的表情——
- Cũ: Reina lại hứng thú với một chủ đề không ngờ tới.\nChị Mayami như chỉ chờ có thế——!
- Mới: Reina lại hứng thú với một chủ đề không ngờ tới.\nChị Mayami như chỉ chờ có thế——Ư!
- Lý do: Sweep lost-gasp-trailing (đã kiểm chứng trực tiếp): JP kết bằng '――っ！', bản cũ giữ dấu gạch nhưng mất tiếng thở — thêm Ư sau gạch.

### 1671 — monologue — misaligned
- JP: よい子のお返事。つづくワクワクした呼吸。\nけれどもそれが、少ししょぼんとした声になる。
- TW: 玲奈乖巧地回應道。她依然興奮地喘著氣，但是聲音卻有點消沉了。
- Cũ: 「Vâng ạ. Reina nhất định sẽ làm vậy ạ」
- Mới: Câu trả lời của một đứa trẻ ngoan. Tiếp đó là nhịp thở đầy háo hức.\nNhưng rồi, nó lại biến thành một giọng nói có chút xịu xuống.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 692 — lấy nguyên văn về đây.

### 1685 — monologue — misaligned
- JP: いきなりれいなの大きな声。\nほんの一瞬動揺したのが、僕だかナビだかわからぬほどの。
- TW: 玲奈突然大聲喊道。也不知道是我還是Ｎａｖｉ被嚇得搖了一下。
- Cũ: 「Ehehe, nếu vậy thì vui quá ạ.\nA! Đúng rồi, anh Kato Suzume~! Có nghe thấy không ạ」
- Mới: Đột nhiên Reina hét lớn.\nSự bối rối trong chốc lát đó, không biết là do tôi hay Navi nữa.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1125 — lấy nguyên văn về đây.

### 1731 — monologue — misaligned
- JP: 真闇姉には無論、子育ての経験なぞない。\nならばこれは、日々姫への思いなのかとふっと感じる。
- TW: 真闇姐當然沒有養育小孩的經驗。這應該是她和日日姬相處的感受吧。
- Cũ: 「……Vậy sao」
- Mới: Chị Mayami dĩ nhiên không có kinh nghiệm nuôi dạy con cái.\nVậy thì đây hẳn là những suy nghĩ dành cho Hibiki, tôi chợt nhận ra.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1019 — lấy nguyên văn về đây.

### 1732 — monologue — misaligned
- JP: 真闇姉の匂いを不意に感じる。慣れきっていて、\nけれども意識をしたならば、危ういほどに甘い匂いを。
- TW: 真闇姐的味道飄進了我的鼻腔。我非常熟悉這個味道，但一旦往那方面想，這香甜的氣息就有些誘人衝動了。
- Cũ: 「Tất nhiên, lúc nào em cũng sẵn sàng」
- Mới: Bất chợt, tôi ngửi thấy mùi hương của chị Mayami. Một mùi hương quá đỗi quen thuộc,\nnhưng một khi đã ý thức được, nó lại ngọt ngào đến mức nguy hiểm.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1071 — lấy nguyên văn về đây.

### 1736 — monologue — misaligned
- JP: 嬉しげな声。\n伝わったことで僕もまた嬉しくさせられる。
- TW: 真闇姐的聲音聽起來很開心。她的理解也讓我很欣喜。
- Cũ: 「À」
- Mới: Giọng nói vui vẻ.\nViệc tâm tư được thấu hiểu khiến tôi cũng thấy vui lây.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1446 — lấy nguyên văn về đây.

### 1737 — monologue — misaligned
- JP: ふんわり。しかし決然と。\n迷いを一切感じない、いつもどおりの真闇姉の声。
- TW: 真闇姐的聲音軟綿綿的，其中卻帶著堅定的決心。她的聲音中沒有絲毫猶豫，就跟平時一樣。
- Cũ: 「Không đâu, Sou-chan. Dù có nhiều thời gian hơn nữa,\nchị cũng nhất định sẽ xin đi du lịch Ohimitera」
- Mới: Nhẹ nhàng. Nhưng đầy kiên quyết.\nGiọng nói của chị Mayami vẫn như mọi khi, không chút do dự.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1209 — lấy nguyên văn về đây.

### 1744 — monologue — misaligned
- JP: すぐ隣から、ふうわりとした真闇姉の声。\n幸せな考えごとから、幸せ極まる現実へと引き戻される。
- TW: 真闇姐綿軟的聲音從我身邊傳來，把我的思緒從幸福的思考中拉回到幸福至極的現實。
- Cũ: 「Sao thế, Sou-chan?」
- Mới: Giọng nói dịu dàng của chị Mayami vang lên ngay bên cạnh.\nKéo tôi từ những suy nghĩ hạnh phúc trở về với thực tại ngập tràn hạnh phúc.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1159 — lấy nguyên văn về đây.

### 1746 — monologue — misaligned
- JP: 小さく笑って、真闇姉はそうっと僕の頬を撫ぜる。
- TW: 真闇姐輕笑一聲，撫摸著我的臉龐。
- Cũ: 「Chà chà」
- Mới: Chị Mayami cười khúc khích, nhẹ nhàng vuốt ve má tôi.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1214 — lấy nguyên văn về đây.

### 1764 — monologue — misaligned
- JP: 聞いた瞬間、第一候補と確定するほど、\n実に楽しげにはずむ声。
- TW: 聽我這麼一說，真闇姐顯得興致勃勃，第一候補直接定下來了。
- Cũ: 「Bé Reina!\nUfufu, chắc em ấy sẽ là một hướng dẫn viên đáng yêu lắm đây」
- Mới: Ngay khoảnh khắc nghe thấy, giọng nói vui vẻ reo lên,\nđủ để xác định luôn đây là ứng cử viên số một.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1073 — lấy nguyên văn về đây.

### 1768 — monologue — misaligned
- JP: そういえば、真闇姉はまだナビに乗ったことがない。\n今回ぜひとも乗ってもらおうと思うが、それはそれとして。
- TW: 說來真闇姐還沒坐過Ｎａｖｉ。下次一定要讓她坐坐，這個先不說。
- Cũ: 「Ufufu, bay lượn ngắm cảnh thong dong,\nnhư vậy cũng sẽ là một tuần trăng mật vui vẻ nhỉ」
- Mới: Nhắc mới nhớ, chị Mayami vẫn chưa từng ngồi Navi.\nLần này nhất định phải để chị ấy đi thử, nhưng chuyện đó tính sau.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1048 — lấy nguyên văn về đây.

### 1769 — monologue — misaligned
- JP: 口にしたなら世迷い言だと自分で感じてしまうけれども、\n真闇姉はうんうんと、楽しげに相槌を打ってくれてる。
- TW: 說出這句話後我自己也覺得莫名其妙，但是真闇姐卻愉快地附和著我。
- Cũ: 「Giống như Hachiroku, dù là đồ vật nhưng lại có linh hồn.\nCó lẽ căn phòng này, nếu nó cũng có linh hồn」
- Mới: Vừa nói ra tôi đã thấy mình như đang lảm nhảm,\nnhưng chị Mayami lại gật gù, vui vẻ hùa theo.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1249 — lấy nguyên văn về đây.

### 1770 — monologue — misaligned
- JP: 言えばもぞりと、真闇姉が体を寄せてくる。
- TW: 說著，真闇姐湊了過來。
- Cũ: 「Đã rõ.\nVậy thì, việc chọn hướng dẫn viên sẽ rất quan trọng đây」
- Mới: Vừa dứt lời, chị Mayami cựa quậy nhích người lại gần.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1422 — lấy nguyên văn về đây.

### 1778 — monologue — misaligned
- JP: きっぱり。ふんわり。\nその断言にも、なんの力みもてらいも無い。
- TW: 軟綿綿的聲音中帶著堅定。她下這個結論的時候也像是理所當然一樣。
- Cũ: 「Tất nhiên là một điều rất tuyệt vời rồi.\nDù là bao bọc quá mức, nuông chiều con cái, hay yêu thương con hết mực」
- Mới: Quả quyết. Nhẹ nhàng.\nLời khẳng định đó, không chút gượng gạo hay màu mè.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1033 — lấy nguyên văn về đây.

### 1788 — monologue — misaligned
- JP: その言葉になにか特別な想いでもあるのか、\nれいなのテンションが一段あがる。
- TW: 這個詞似乎對玲奈有著特別的意義，她越來越興奮了。
- Cũ: 「Ghế đặc biệt!」
- Mới: Lời nói đó có chứa đựng cảm xúc đặc biệt nào không,\nmà sự phấn khích của Reina lại tăng thêm một bậc.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1136 — lấy nguyên văn về đây.

### 1789 — monologue — misaligned
- JP: なんと時宜を得た助け舟――いや、助け飛行機だろうか。
- TW: 這救援船——不對，救援飛機來得真及時。
- Cũ: 「Ở độ cao có thể bao quát toàn cảnh thành phố Ohimitera này,\nhoàn toàn không thể nhìn thấy chim sẻ đang bay đâu ạ」
- Mới: Quả là một chiếc thuyền cứu sinh kịp thời——à không, máy bay cứu sinh mới đúng.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1247 — lấy nguyên văn về đây.

### 1790 — monologue — misaligned
- JP: 今度の声は、甘えとおねだり。\nそれに応えて、静かにおやすみのキスをする。
- TW: 這次她的聲音裡帶著一點撒嬌的意味。我回應著她，輕輕地給她一個晚安吻。
- Cũ: 「Vậy sao, vậy thì lần này ngủ thật nhé.\nCả hai ta, đều có công việc phải dậy sớm mà」
- Mới: Giọng nói lần này, mang theo sự nũng nịu và vòi vĩnh.\nĐáp lại điều đó, tôi lặng lẽ trao một nụ hôn chúc ngủ ngon.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1197 — lấy nguyên văn về đây.

### 1791 — monologue — misaligned
- JP: ハチロクとの部屋だった頃にはかなり濃かった鉄分が、\nいまではほのかな麹の香りに変わった気もする。
- TW: 這裡用作我和八六的房間時充滿了鐵的氣息，而現在感覺變成了酒麴的香味。
- Cũ: 「Và bây giờ, nó là phòng ngủ của vợ chồng mình」
- Mới: Khi còn là phòng của tôi và Hachiroku, mùi sắt khá nồng,\nnhưng giờ tôi cảm giác nó đã chuyển thành hương men kōji thoang thoảng.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1243 — lấy nguyên văn về đây.

### 1792 — monologue — misaligned
- JP: ならば……うむ。日々姫ハチロクを候補から外そう。\nふたりも一緒の家族旅行は、別の機会にするべきゆえ。
- TW: 這麼說的話……嗯。日日姬和八六也不作考慮了。帶著她們的家庭旅行等另外的機會再說。
- Cũ: 「Đúng vậy. Đã cất công đi tuần trăng mật.\nNếu không thể thư giãn và tận hưởng thì thật lãng phí」
- Mới: Nếu vậy thì……ừm. Loại Hibiki và Hachiroku khỏi danh sách ứng cử viên thôi.\nChuyến du lịch gia đình có cả hai người họ nên để dịp khác.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1390 — lấy nguyên văn về đây.

### 1798 — monologue — misaligned
- JP: ナビの律儀な訂正は、真闇姉から暖かな笑みを引き出す。
- TW: Ｎａｖｉ一本正經的訂正讓真闇姐嫣然一笑。
- Cũ: 「Ufufu」
- Mới: Sự đính chính nghiêm túc của Navi, khiến chị Mayami nở nụ cười ấm áp.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1335 — lấy nguyên văn về đây.

### 1800 — monologue — misaligned
- JP: 眼下を眺めやすいよう、\nナビは機体を、実になめらかに傾ける。
- TW: Ｎａｖｉ讓機身傾斜了一個角度，方便我們看下方的風景。
- Cũ: 「Waaa」
- Mới: Để dễ dàng ngắm nhìn cảnh sắc bên dưới,\nNavi nghiêng thân máy bay một cách vô cùng mượt mà.
- Lý do: Lệch hàng: bản dịch đúng của dòng này đang nằm ở key 1101 — lấy nguyên văn về đây.

## Kết bài

File lr真闇追加01 — file thêm về tuần trăng mật — có **142/300 dòng sai (47,3%)**, gần một nửa file, và gần như toàn bộ là lỗi lệch hàng: hai chuỗi xoay khổng lồ (114 + 9 mắt xích) cuốn gần hết các dòng thoại và độc thoại, đúng kiểu "lỗi dán rải rác" nhưng ở quy mô lớn nhất từ trước tới nay trong một file (chuỗi A một mình đã dài hơn cả file h3). Ngoài chuỗi xoay, chỉ có 8 lỗi thuật ngữ thuần (Ohitoyo 7, Yui 2, Migita 1 — một số dòng gộp 2 lỗi), 7 lỗi xưng hô Soutetsu "em/anh"→"tôi" với Mayami (trong đó 1 lỗi do lượt quét đại từ bắt được mà lần đọc đầu bỏ sót: 1281), 2 gasp theo sweep, và 1 dòng chưa dịch (1264) may mắn thu hồi được nguyên văn từ key 1744. Không có lỗi cấu trúc ngoài chuỗi xoay, không có dòng mồ côi, không có nhiễm chéo file khác, không có dòng nào cần Hieu quyết — kể cả dòng 1036 phải dịch mới (Reina nói với chim sẻ) cũng dịch trực tiếp từ JP/TW, không mơ hồ. Sau file này, Mayami còn 11 file; dòng chưa dịch còn lại toàn dự án chỉ còn 1 (ở lr真闇追加02).

### Khối TOML (đã kiểm chứng parse)

```toml
[script]
"669" = "……Paulette thì quá bận rộn,\\nnếu nhờ vả, cô ấy có thể sẽ cố sức nhận lời——a"
"692" = "「……Reina hơi tiếc một chút ạ. Chắc là anh Kato Suzume,\\nkhông nghe thấy tiếng rồi nhỉ」"
"700" = "「……Vậy sao」"
"1007" = "「30 phút hay 1 tiếng thì lúc nào cũng xoay sở được.\\nVậy thì, cùng nhau nhé. Nếu em ấy nhận lời」"
"1010" = "「Lần sau muốn hét to,\\nthì báo trước cho chị một tiếng là được rồi」"
"1016" = "「Không đâu, Sou-chan. Dù có nhiều thời gian hơn nữa,\\nchị cũng nhất định sẽ xin đi du lịch Ohitoyo」"
"1019" = "「Hơn nữa, nè? Nếu có thể nhờ bé Reina làm hướng dẫn viên.\\nChị cũng có thể tham gia vào buổi bàn bạc chi tiết được không?」"
"1026" = "「Đúng vậy. Đã cất công đi tuần trăng mật.\\nNếu không thể thư giãn và tận hưởng thì thật lãng phí」"
"1033" = "「Nếu không làm vậy nữa, thì kiểu gì cũng sẽ buông tay thôi.\\nTrong lúc còn nắm tay nhau, bao bọc quá mức cũng tốt mà」"
"1036" = "「Không cần cố bay qua đây đâu ạ! Lát nữa Reina cho ăn vụn bánh mì, ngoan ngoãn chờ ở dưới đó nha」"
"1039" = "「Sou-chan sẽ làm cho gia đình hưng thịnh sao?\\nCùng với chị」"
"1040" = "「Em không tự nhận ra sao?\\nEm vừa cười khúc khích đấy, Sou-chan. Như đang nhớ lại chuyện gì vui vậy」"
"1048" = "「Vậy mà, chị thực sự muốn đi 『Du lịch Ohitoyo』 sao?\\nNếu vì lý do thời gian, tôi có thể dời lại thêm nữa」"
"1053" = "「Lần lượt là 17:27, 18:34, 19:41 xuất phát từ ga Ohitoyo ạ.\\nDừng đỗ tạm thời tại ga bỏ hoang Taragi lúc 18:04, 19:11 và 20:18 nha」"
"1059" = "「Ra vậy. Có thể sẽ thú vị đấy. Vì là quê hương nơi mình sinh ra và lớn lên,\\ntưởng chừng như đã biết rõ mọi ngóc ngách, nên ngược lại」"
"1061" = "「Ra vậy. Vậy cứ quyết định thế đi」"
"1071" = "「Nhưng, đêm nay——hay nói đúng hơn là một thời gian tới, tôi muốn kiềm chế lại.\\nDù sao thì, kỳ nghỉ cho tuần trăng mật cũng」"
"1073" = "「Nhưng mà, bé Reina cũng bận lắm đúng không?\\nNếu làm em ấy phải cố sức dù chỉ một chút」"
"1077" = "「Ư!」"
"1080" = "「Ufufu」"
"1084" = "「Ufufu, bay lượn ngắm cảnh thong dong,\\nnhư vậy cũng sẽ là một tuần trăng mật vui vẻ nhỉ」"
"1092" = "「Wawawa! Reina không biết luôn!\\nÀ này, chị Mayami, Reina, sắp hét to nha」"
"1096" = "「Waai waai! Có nghe thấy không, chị Paulette!\\nReina, đang gọi từ trên trời đó nha」"
"1097" = "「Waaa」"
"1101" = "「Waaa! Tuyệt quá đi ạ!\\nThành phố Ohitoyo, trở nên nhỏ xíu luôn ạ」"
"1114" = "「Fufu. Chắc chắn là nghe thấy rồi.\\nCả Paulette, Hibiki và Hachiroku nữa」"
"1116" = "「Fufu, nghe cách nói của chị Mayami,\\nlại thấy việc bao bọc quá mức là một điều rất tốt」"
"1119" = "「Chà chà」"
"1125" = "「Ây da ây da bé Reina,\\nhét to như vậy, làm chị giật cả mình đó」"
"1131" = "「Ây da, hay quá nhỉ. Chị cũng bắt chước thử xem.\\nHii-chan, Haa-chan, có nghe thấy không~?」"
"1136" = "「Ehehe, đúng là ghế đặc biệt có khác nha.\\nCực kỳ êm ái và mềm mại luôn ạ」"
"1140" = "「Ehehe, nếu vậy thì vui quá ạ.\\nA! Đúng rồi, anh Kato Suzume~! Có nghe thấy không ạ」"
"1144" = "「A——ufufu. Đúng thế, chắc chắn rồi.\\nPau-chan, có vẻ bao bọc quá mức nhỉ」"
"1149" = "「Hau. Em xin lỗi ạ. Reina, chỉ là,\\nnghĩ nếu có thể nói chuyện với anh Kato Suzume trên trời thì tốt biết mấy」"
"1156" = "「À, số hiệu tàu đấy.\\nXuất phát từ Ohitoyo là số lẻ. Xuất phát từ Yunoi là số chẵn」"
"1159" = "「A, xin lỗi,\\ntôi làm chị thức giấc à?」"
"1164" = "「Ưm……」"
"1166" = "「Hừm. ……Làm sao đây.\\nTôi thì không nghĩ ra chỗ nào đặc biệt cả——」"
"1168" = "「Ưm……Chuyện đó thì——」"
"1170" = "「Ừ. Nếu thử đóng vai du khách đến thăm,\\nchị nghĩ mình sẽ thấy được một Ohitoyo mà chị chưa từng biết」"
"1175" = "「À」"
"1177" = "「Ừ. Được thôi」"
"1181" = "「Ừ, thật sự tuyệt vời quá nhỉ.\\nChị cũng, lần đầu tiên nhìn thấy cảnh sắc như thế này đó」"
"1190" = "「Hửm? Vậy tại sao」"
"1194" = "「Ưm fufu, cuối cùng, cũng sắp đến rồi nhỉ.\\nXin lỗi em nhé? Chị lại bắt em phải chờ đợi rồi」"
"1196" = "「Ufufuu, anh Soutetsu trông cũng vui quá kìa!\\nVui lắm đúng không ạ, bầu trời. Rộng lớn đến nhường này cơ mà」"
"1197" = "「Ufufuu, cảm giác ngồi tuyệt vời quá đi ạ.\\nĐúng là Navi mà anh Soutetsu luôn tự hào có khác nha」"
"1203" = "「Bầu trời cũng đẹp, nhưng cảnh sắc bên dưới cũng tuyệt vời lắm đấy.\\nThị trấn quen thuộc, nhìn từ trên cao hoàn toàn khác biệt so với dưới mặt đất」"
"1207" = "「Nhưng, chúng ta có Navi. Nếu ở trong nội địa Hinomoto,\\nthì lịch trình này đủ để đi bất cứ đâu」"
"1209" = "「Tôi hiểu rồi. Nếu vậy tôi không có ý kiến gì.\\nNhưng——tại sao lại là Ohitoyo?」"
"1213" = "「Vâng ạ. Reina nhất định sẽ làm vậy ạ」"
"1214" = "「Nếu nhà cửa hay phòng ốc mà có cảm xúc,\\nthì chắc chắn chúng sẽ thấy hạnh phúc rồi」"
"1219" = "「Theo ý chị thì, cứ tắm rửa và ăn tối xong xuôi ở Ohitoyo đi.\\nĐến nhà trọ rồi thì chỉ muốn tận hưởng giấc ngủ thôi」"
"1227" = "「Hưng thịnh, sao.\\nChị em trở thành vợ chồng, khả năng đó sẽ lớn dần lên nhỉ」"
"1241" = "「Bé Reina!\\nUfufu, chắc em ấy sẽ là một hướng dẫn viên đáng yêu lắm đây」"
"1243" = "「Giống như Hachiroku, dù là đồ vật nhưng lại có linh hồn.\\nCó lẽ căn phòng này, nếu nó cũng có linh hồn」"
"1245" = "「Đúng rồi ạ. Về điểm này, nếu đi tàu thì\\nKiha 07S tự hào của Đường sắt Ohitoyo sẽ dừng đỗ tạm thời, đưa anh chị đến nơi dễ dàng luôn nha」"
"1247" = "「Là vậy đó.\\nDù có nghe thấy, chắc anh ấy cũng không bay lên được độ cao này đâu」"
"1249" = "「Tôi hy vọng sự biến đổi này cũng là một niềm hạnh phúc đối với căn phòng.\\nTôi cứ vẩn vơ suy nghĩ những điều như vậy」"
"1257" = "「Một địa điểm du lịch nổi tiếng mà chị chưa từng đến thăm bao giờ.\\nNên, chị muốn thử đi 『Du lịch ngắm cảnh』 xem sao」"
"1264" = "「Sao thế, Sou-chan?」"
"1271" = "「Cả hai đều vậy mà.\\nTôi cũng hoàn toàn không thể sắp xếp được lịch trình」"
"1273" = "「Tôi cũng nghĩ vậy.\\nVậy thì cũng không thể nhờ Nagi được. Đối mặt với khách quen sẽ rất ngại」"
"1280" = "「Chúng ta chỉ chắc chắn có thể cùng nhau nghỉ phép trong hai ngày.\\nRõ ràng là không thể đi du lịch dài ngày được」"
"1281" = "「Nhân lúc đang ở trên không. Vừa ngắm nhìn thị trấn,\\ntôi muốn bàn về lịch trình cho tuần trăng mật」"
"1283" = "「Tôi chỉ đang mải suy nghĩ thôi.\\nCăn phòng này, trong thời gian ngắn đã thay đổi công năng bao nhiêu lần rồi nhỉ」"
"1285" = "「Đã rõ.\\nVậy thì, việc chọn hướng dẫn viên sẽ rất quan trọng đây」"
"1287" = "「Ở độ cao có thể bao quát toàn cảnh thành phố Ohitoyo này,\\nhoàn toàn không thể nhìn thấy chim sẻ đang bay đâu ạ」"
"1289" = "「Tôi thì dĩ nhiên là theo nhịp độ của chị Mayami rồi」"
"1290" = "「Để xem, trước tiên tìm đường ray đã」"
"1292" = "「Tôi cười sao. Tôi không nhận ra luôn đấy——」"
"1295" = "「Tất nhiên, lúc nào tôi cũng sẵn sàng」"
"1306" = "「Đã rõ. Tiến hành xoay vòng」"
"1311" = "「Đúng vậy」"
"1324" = "「Có gia đình mới thành tổ ấm.\\nSự hưng thịnh, chẳng phải là điều mà chúng hằng mong ước sao」"
"1331" = "「Không đâu, nãy chị cũng nói rồi mà?\\nChị, vẫn chưa ngủ đâu」"
"1332" = "「Không đâu.\\nChị vẫn chưa ngủ, chỉ nhắm mắt thôi」"
"1333" = "「Đúng vậy. Thế nên tôi mới nói với Reina rằng\\ncơn mưa xối xả đột ngột này cần phải cẩn thận đấy——」"
"1335" = "「Đúng rồi đó, bé Reina.\\nTrên đùi chị, hôm nay là ghế đặc biệt của bé Reina đó」"
"1344" = "「Rồi Haa-chan đến.\\nSau đó Haa-chan lại chuyển sang phòng của Hii-chan」"
"1351" = "「Ghế đặc biệt!」"
"1360" = "「Bây giờ tôi không làm người thay thế nữa. Hibiki cũng là em gái của tôi,\\nkhông phải với tư cách là em gái của vợ, mà là em gái của chính tôi」"
"1361" = "「Thật tốt khi có thể bàn bạc theo một cách không ngờ tới.\\nNhưng, thật sự xin lỗi vì đã đánh thức chị」"
"1363" = "「Hồi đó thì——nếu là tôi của hồi đó, ừm. Chắc chắn là\\ntôi đã làm \"người thay thế\" như một nghĩa vụ, nhưng……」"
"1364" = "「Tất nhiên rồi. Nếu chị Mayami có thời gian」"
"1365" = "「Thì đó. Nhà, là tổ ấm mà」"
"1366" = "「Tất nhiên là một điều rất tuyệt vời rồi.\\nDù là bao bọc quá mức, nuông chiều con cái, hay yêu thương con hết mực」"
"1372" = "「Trên đùi của phu nhân Mayami, không phải là trang bị tiêu chuẩn của cỗ máy này」"
"1376" = "「Chị Mayami. Trong số những người không có bất kỳ mối quan hệ làm ăn nào với xưởng rượu Migita Ichi,\\nchúng ta thử nhờ Reina làm hướng dẫn viên thì sao?」"
"1379" = "「Đã rõ. Nhưng, không chắc chắn là em ấy sẽ nhận lời đâu.\\nNếu không được thì ứng cử viên thứ hai sẽ là ai đây」"
"1390" = "「Cỡ Kisaki, hay Fukami thì……\\ncũng có liên quan đến xưởng rượu nên chắc sẽ ngại ngùng nhỉ」"
"1399" = "「Và bây giờ, nó là phòng ngủ của vợ chồng mình」"
"1402" = "「Biết không? Sou-chan.\\nLý do rất đơn giản」"
"1415" = "「Nếu được cho xem bên trong ngân hàng thì chắc sẽ vui lắm,\\nnhưng chuyện đó để dịp khác ngoài tuần trăng mật cũng được nhỉ」"
"1417" = "「Du lịch ngắm cảnh, sao」"
"1422" = "「Hướng dẫn viên của Phòng Thương mại thì hơi...\\nChị chắc chắn sẽ thấy gượng gạo lắm」"
"1443" = "「Vậy sao, vậy thì lần này ngủ thật nhé.\\nCả hai ta, đều có công việc phải dậy sớm mà」"
"1446" = "「Đầu tiên là phòng sách của ông Taito.\\nSau đó tôi được dùng nó làm phòng riêng」"
"1447" = "「Nghe chị nói vậy, đúng là thế thật」"
"1448" = "「Chị khẳng định thế sao. Rốt cuộc là vì lý do gì」"
"1456" = "「Chuyện đó, đợi bị từ chối rồi hẵng nghĩ.\\nNếu có phương án dự phòng, tự nhiên sẽ thấy chùn bước mà」"
"1457" = "「Nè, nè. Chị Mayami.\\nCửa hàng đường sắt ở đâu vậy ạ?」"
"1460" = "「Vậy thì chốt đi tàu nhé. Tôi cũng muốn thử đi\\nKiha 07S do Paulette lái một mình xem sao」"
"1462" = "「Vậy thì, chỗ đó giao cho cô hướng dẫn viên đấy.\\nMột nơi đậm chất Ohitoyo nhất mà hướng dẫn viên đề xuất」"
"1474" = "「Nghĩa là, Kumagin ở đằng kia——\\nA, thấy xưởng rượu nhà mình rồi」"
"1487" = "「Đường ray đường ray……a! Kia rồi nha.\\nVậy thì vậy thì——thấy rồi! Cửa hàng đường sắt!!」"
"1490" = "「Về chuyện đó chị cứ yên tâm.\\nNếu có chút gì quá sức, Paulette sẽ không cho nhận đâu」"
"1494" = "「Ngoài hai nơi đó ra, chắc là đi tàu khách do 8620 kéo nhỉ.\\nDù sẽ phải đi khứ hồi đến Yunoi, nhưng cũng có thể trải nghiệm xúc than nữa」"
"1504" = "「!」"
"1505" = "「27D thì sẽ là chuyến tàu cuối cùng đấy.\\nXuất phát từ ga Suối nước nóng Ohitoyo lúc 21:35, dừng đỗ tạm thời tại ga bỏ hoang Taragi lúc 22:09」"
"1576" = "Nhà, và tổ ấm. Lần đầu tiên nghe hai từ này đặt cạnh nhau,\\ntôi mới hiểu ra sự khác biệt giữa một công trình kiến trúc và một gia đình."
"1585" = "Ngay cả khi đã trở thành vợ chồng,\\ncách xưng hô giữa tôi và chị Mayami vẫn không hề thay đổi."
"1610" = "Thể theo nguyện vọng mạnh mẽ của chị Mayami, Reina đã nhận công việc hướng dẫn viên.\\nDưới hình thức là một đơn đặt hàng chính thức gửi đến Bộ phận Du lịch của Đường sắt Ohitoyo."
"1616" = "Giống như hùa theo, lại giống như nói mớ.\\nGiọng nói cho thấy cơn buồn ngủ đã quay trở lại."
"1619" = "Có tựa đầu siêu cao cấp thế kia, tất nhiên rồi.\\nKhoảnh khắc nghĩ vậy, tôi tự nhận thức được sự ghen tị thoáng qua, rồi bật cười."
"1634" = "Cuối cùng thì lịch trình của cả hai cũng khớp nhau.\\nDo đó, việc chuẩn bị cho tuần trăng mật hầu như vẫn chưa tiến triển gì."
"1641" = "Cơ thể tôi ngập tràn hạnh phúc đến mức tự động bật cười.\\nNhận ra điều đó, khuôn mặt tôi lại giãn ra."
"1647" = "Dù nụ cười của tôi có phần tự trào, nhưng Reina\\nlại đón nhận nó một cách rất tích cực. Vậy thì cứ ngoan ngoãn hùa theo thôi."
"1649" = "Tôi chợt nhớ đến thị trấn nhỏ nơi tôi sinh ra.\\nNơi đó cũng được coi là một thị trấn có khách du lịch đến thăm, nhưng——"
"1650" = "Lời nói đầy lý trí của tôi, chỉ bằng một tiếng hùa theo đầy gợi cảm,\\nđã mang theo hơi ấm sống động đến chân thực."
"1654" = "Gật đầu rồi tôi chợt thấy kỳ lạ.\\nTừ khi Hachiroku gia nhập, số lượng thành viên trong gia đình đâu có tăng thêm."
"1657" = "Reina lại hứng thú với một chủ đề không ngờ tới.\\nChị Mayami như chỉ chờ có thế——Ư!"
"1671" = "Câu trả lời của một đứa trẻ ngoan. Tiếp đó là nhịp thở đầy háo hức.\\nNhưng rồi, nó lại biến thành một giọng nói có chút xịu xuống."
"1685" = "Đột nhiên Reina hét lớn.\\nSự bối rối trong chốc lát đó, không biết là do tôi hay Navi nữa."
"1731" = "Chị Mayami dĩ nhiên không có kinh nghiệm nuôi dạy con cái.\\nVậy thì đây hẳn là những suy nghĩ dành cho Hibiki, tôi chợt nhận ra."
"1732" = "Bất chợt, tôi ngửi thấy mùi hương của chị Mayami. Một mùi hương quá đỗi quen thuộc,\\nnhưng một khi đã ý thức được, nó lại ngọt ngào đến mức nguy hiểm."
"1736" = "Giọng nói vui vẻ.\\nViệc tâm tư được thấu hiểu khiến tôi cũng thấy vui lây."
"1737" = "Nhẹ nhàng. Nhưng đầy kiên quyết.\\nGiọng nói của chị Mayami vẫn như mọi khi, không chút do dự."
"1744" = "Giọng nói dịu dàng của chị Mayami vang lên ngay bên cạnh.\\nKéo tôi từ những suy nghĩ hạnh phúc trở về với thực tại ngập tràn hạnh phúc."
"1746" = "Chị Mayami cười khúc khích, nhẹ nhàng vuốt ve má tôi."
"1764" = "Ngay khoảnh khắc nghe thấy, giọng nói vui vẻ reo lên,\\nđủ để xác định luôn đây là ứng cử viên số một."
"1768" = "Nhắc mới nhớ, chị Mayami vẫn chưa từng ngồi Navi.\\nLần này nhất định phải để chị ấy đi thử, nhưng chuyện đó tính sau."
"1769" = "Vừa nói ra tôi đã thấy mình như đang lảm nhảm,\\nnhưng chị Mayami lại gật gù, vui vẻ hùa theo."
"1770" = "Vừa dứt lời, chị Mayami cựa quậy nhích người lại gần."
"1778" = "Quả quyết. Nhẹ nhàng.\\nLời khẳng định đó, không chút gượng gạo hay màu mè."
"1788" = "Lời nói đó có chứa đựng cảm xúc đặc biệt nào không,\\nmà sự phấn khích của Reina lại tăng thêm một bậc."
"1789" = "Quả là một chiếc thuyền cứu sinh kịp thời——à không, máy bay cứu sinh mới đúng."
"1790" = "Giọng nói lần này, mang theo sự nũng nịu và vòi vĩnh.\\nĐáp lại điều đó, tôi lặng lẽ trao một nụ hôn chúc ngủ ngon."
"1791" = "Khi còn là phòng của tôi và Hachiroku, mùi sắt khá nồng,\\nnhưng giờ tôi cảm giác nó đã chuyển thành hương men kōji thoang thoảng."
"1792" = "Nếu vậy thì……ừm. Loại Hibiki và Hachiroku khỏi danh sách ứng cử viên thôi.\\nChuyến du lịch gia đình có cả hai người họ nên để dịp khác."
"1798" = "Sự đính chính nghiêm túc của Navi, khiến chị Mayami nở nụ cười ấm áp."
"1800" = "Để dễ dàng ngắm nhìn cảnh sắc bên dưới,\\nNavi nghiêng thân máy bay một cách vô cùng mượt mà."
```
