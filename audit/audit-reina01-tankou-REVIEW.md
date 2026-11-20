# Audit — れいな01_炭鉱探索 (04_Reina)

- File: `04_Reina/れいな01_炭鉱探索.txt.toml` — route Reina 01, khảo sát mỏ than bỏ hoang (術仙廃炭鉱): Soutetsu, Reina và Paulette khảo sát mỏ, Reina giảng về mỏ than (quặng pirit, axit sunfuric, celluloid, đường sắt mỏ, tàu hỗn hợp, xe goòng chở người); cảnh "chơi trò gia đình" ở ký túc xá; kết bằng việc Paulette và Reina được giải phóng khỏi chuyến chạy định kỳ.
- Đọc: **403/403 dòng script** (key 1065–2632), đối chiếu từng dòng với JP + TW (CSV3). Không lấy mẫu. Nhân vật: monologue 145, 双鉄 120, れいな 94, ポーレット 44 — không có Hachiroku/Mayami/Minokasa/Kisaki nói thoại trong file, nên mọi thoại của Soutetsu đều hướng tới Reina hoặc Paulette (cả hai đều là "anh").
- TOML md5: `945c238f9039b7edc88998a761c5cdb8`; **1 bản duy nhất, không trùng lặp** (không có file trùng tên trong toml2). CSV3 1 bộ duy nhất 403 dòng, key khớp tuyệt đối 403/403, 0 ô VN trống, 0 trùng key. `[selections]` rỗng.
- Lưu ý: 266 chênh lệch VN giữa TOML và CSV3 đều là kiểu đã biết — TOML-2 làm phẳng `\n` thật thành khoảng trắng (264 chỗ `\n`→khoảng trắng + 2 chỗ gộp khoảng trắng kề); CSV3 (literal `\n`) là chuẩn. Không có chênh lệch nội dung nào khác.
- Cơ sở tổng cộng (đã kiểm chứng với ROUTE-AUDIT.md dòng cuối): **106 file / 4.936 dòng sai** — khớp đúng số parent giao.

## §1. Kết quả

**35 dòng sai / 403 dòng = 8,7%.** Thoại 32/258 (12,4%), độc thoại 3/145 (2,1%). Không có lệch vị trí, không có chuỗi xoay vòng, không có nhiễm chéo file khác, không có dòng mồ côi, không có dòng chưa dịch, không có trùng khóa.

Phân loại:

| Loại | Số dòng | Key |
|---|---|---|
| Đại từ | 20 | 1559, 1582, 1599, 1601, 1606, 1610, 1611, 1614, 1615, 1691, 1742, 1745, 1747, 1763, 1769, 1775, 1833, 1862, 2006, 2019 |
| SFX (tiếng cười) | 7 | 1538, 1624, 1626, 1629, 1630, 1633, 1634 |
| Gasp っ (sweep) | 1 | 2035 |
| Sai nghĩa | 4 | 1580, 1643, 1663, 2348 |
| Thuật ngữ | 3 | 1644, 2218, 2349 |

## §2. Chi tiết từng dòng sai

### Đại từ — Soutetsu tự xưng "tôi"→"anh" và gọi Paulette "cô"→"em" (20 dòng)

- **1559 [双鉄]** — JP 「ああ――それは、僕も以前に聞いたな。しかし、 ゆえに、配線類は全て厳重に絶縁してあるのだろう？」 / TW 「啊——這個我也聽說過。不過，配線不是為此經過了絕緣處理嗎？」 / Cũ: 「À――chuyện đó, trước đây tôi cũng từng nghe nói. Nhưng mà,
chính vì thế nên tất cả các loại dây điện đều được cách điện nghiêm ngặt rồi mà nhỉ?」 → **「À――chuyện đó, trước đây anh cũng từng nghe nói. Nhưng mà,
chính vì thế nên tất cả các loại dây điện đều được cách điện nghiêm ngặt rồi mà nhỉ?」** (Soutetsu nói với Paulette (dòng 1556 Paulette nói trước, anh đáp lại câu của cô) → tự xưng "anh" theo quy tắc đã sửa ("anh" với Paulette).)
- **1582 [双鉄]** — JP 「ああ、やはり邪魔をしてしまったか」 / TW 「啊，我果然打擾到你了」 / Cũ: 「À, quả nhiên là tôi làm phiền cô rồi.」 → **「À, quả nhiên là anh làm phiền em rồi.」** (Soutetsu nói với Paulette (dòng 1585 Paulette đáp lại) → tự xưng "anh", gọi Paulette "em".)
- **1599 [双鉄]** — JP 「うむ。キハ[レイナナ,1]07を運転してみてよくわかった。 ポーレットが、[ハチロク,3]8620は観光向きだと言った理由が」 / TW 「嗯。在嘗試駕駛Ｋｉｈａ０７之後我明白了，波萊特為什麼說８６２０適合觀光」 / Cũ: 「Ừm. Lái thử KiHa 07 rồi tôi mới hiểu rõ.
Lý do Paulette nói 8620 phù hợp với du lịch.」 → **「Ừm. Lái thử KiHa 07 rồi anh mới hiểu rõ.
Lý do Paulette nói 8620 phù hợp với du lịch.」** (Soutetsu giải thích với Paulette (anh kể lại chuyện vừa lái KiHa 07 cho cô nghe) → "anh". Char là 双鉄 (thoại), không phải monologue.)
- **1601 [双鉄]** — JP 「ああ。多分、驚いたんだろうな。 こんなに小さな\x%lレイルロオド;#00ffc040;レイルロオド%l;#;が、貨物をか――と」 / TW 「嗯。或許是因為我當時很吃驚吧。想著這麼小的一個\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，竟然要運送貨物」 / Cũ: 「Ừ. Chắc là vì tôi đã rất ngạc nhiên.
Một \x%lレイルロオド;#00ffc040;Railord%l;#; nhỏ bé thế này, mà lại đi chở hàng hóa sao――」 → **「Ừ. Chắc là vì anh đã rất ngạc nhiên.
Một \x%lレイルロオド;#00ffc040;Railord%l;#; nhỏ bé thế này, mà lại đi chở hàng hóa sao――」** (Cùng đoạn giải thích với Paulette như 1599 → "anh".)
- **1606 [双鉄]** — JP 「うむ。よろしく頼む」 / TW 「嗯。拜託了」 / Cũ: 「Ừm. Trăm sự nhờ cô.」 → **「Ừm. Trăm sự nhờ em.」** (Soutetsu nhờ Paulette (cô nhận việc giấy phép/quyền lợi ở 1748) → gọi "em".)
- **1610 [双鉄]** — JP 「ああ、任せておいてくれ」 / TW 「嗯，包在我身上」 / Cũ: 「Ừ, cứ giao cho tôi.」 → **「Ừ, cứ giao cho anh.」** (Soutetsu đáp Paulette (1608) → "anh".)
- **1611 [双鉄]** — JP 「ああ、僕も聞いたことがある。品質と価格競争とで負け、 国内の炭鉱はことごとく閉鎖においやられたと」 / TW 「嗯，我也有所耳聞。國內煤礦在品質及價格競爭中敗下陣來，接連關閉」 / Cũ: 「À, tôi cũng từng nghe nói. Vì thua kém về chất lượng và cạnh tranh giá cả,
nên các mỏ than trong nước đều bị đẩy đến bờ vực đóng cửa.」 → **「À, anh cũng từng nghe nói. Vì thua kém về chất lượng và cạnh tranh giá cả,
nên các mỏ than trong nước đều bị đẩy đến bờ vực đóng cửa.」** (Soutetsu nói với Paulette (tiếp tục bàn về than nội địa) → "anh".)
- **1614 [ポーレット]** — JP 「うん、頑張る。 それと――双鉄くん」 / TW 「嗯，我會加油的。還有——雙鐵君」 / Cũ: 「Ừ, chị sẽ cố gắng.
Và――anh Soutetsu.」 → **「Ừ, em sẽ cố gắng.
Và――anh Soutetsu.」** (Paulette nói với Soutetsu mà tự xưng "chị" thì mâu thuẫn ngay trong cùng một dòng với "anh Soutetsu" (khóa B4). Tiền lệ: Paulette tự xưng "em" với Soutetsu (ROUTE-AUDIT: P-file 1997 "chị"→"em" khi nói với Soutetsu; "Paulette tự xưng theo người nghe: 'em' với Soutetsu").)
- **1615 [双鉄]** — JP 「うむ、楽しみにさせてもらおう」 / TW 「嗯，真讓人期待呀」 / Cũ: 「Ừm, tôi sẽ mong đợi lắm đấy.」 → **「Ừm, anh sẽ mong đợi lắm đấy.」** (Soutetsu đáp Paulette (1614) → "anh".)
- **1691 [双鉄]** — JP 「ああ、聞きたいことがある。 この炭鉱は、まだ石炭埋蔵量を残しているのか？」 / TW 「對，我有事想問你。這座煤礦，煤炭儲量還多不多？」 / Cũ: 「À, tôi có chuyện muốn hỏi.
Mỏ than này, liệu trữ lượng than có còn không?」 → **「À, anh có chuyện muốn hỏi.
Mỏ than này, liệu trữ lượng than có còn không?」** (Soutetsu hỏi Reina — dòng 1690 gọi thẳng tên "ちなみに、れいな" → "anh".)
- **1742 [双鉄]** — JP 「プラスアルファのアイディアを求める意味でも、 [じゅつせん,1]術仙廃炭鉱近辺の追加調査を重ねたいのだが――」 / TW 「我想再次對術仙廢煤礦周邊進行調查。就算是為了尋找額外的賣點，也有這麼做的必要……」 / Cũ: 「Để tìm kiếm những ý tưởng cộng thêm đó,
tôi muốn tiến hành thêm các cuộc khảo sát quanh mỏ than bỏ hoang Jussen――」 → **「Để tìm kiếm những ý tưởng cộng thêm đó,
anh muốn tiến hành thêm các cuộc khảo sát quanh mỏ than bỏ hoang Jutsu-sen――」** (Soutetsu nói với Paulette (cô nhận việc ở 1748) → "anh". Đồng thời: 術仙 = "Jutsu-sen" (tiền lệ: file viết thiếu "t" thành "Jussen"; ROUTE-AUDIT 165).)
- **1745 [双鉄]** — JP 「わかっている、そのために、 \x%lキハ07;#00ffc040;キハ07%l;#;の運転を教えてもらったのではないか」 / TW 「我明白。不正是因為這個，才請你教了我\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;的駕駛方法嗎」 / Cũ: 「Tôi hiểu mà, chính vì thế,
nên tôi mới nhờ cô dạy lái \x%lキハ07;#00ffc040;KiHa 07%l;#; mà.」 → **「Anh hiểu mà, chính vì thế,
nên anh mới nhờ em dạy lái \x%lキハ07;#00ffc040;KiHa 07%l;#; mà.」** (Soutetsu nói với Paulette — chính cô dạy anh lái KiHa 07 → "anh... em".)
- **1747 [双鉄]** — JP 「運転も調査も、事故なく行う。 その上で――きっと、何かを掴んでくるさ」 / TW 「我會保證行駛與調查過程零事故。並且——我一定會找到頭緒的」 / Cũ: 「Lái tàu và khảo sát, tôi sẽ thực hiện không để xảy ra sự cố nào.
Hơn thế nữa――chắc chắn, tôi sẽ tìm ra được manh mối gì đó.」 → **「Lái tàu và khảo sát, anh sẽ thực hiện không để xảy ra sự cố nào.
Hơn thế nữa――chắc chắn, anh sẽ tìm ra được manh mối gì đó.」** (Soutetsu nói với Paulette → "anh" (2 lần trong dòng).)
- **1763 [双鉄]** — JP 「すまん、ポーレット。 考え事の最中か？」 / TW 「抱歉，波萊特。你在想事情嗎？」 / Cũ: 「Xin lỗi nhé, Paulette.
Cô đang mải suy nghĩ gì à?」 → **「Xin lỗi nhé, Paulette.
Em đang mải suy nghĩ gì à?」** (Gọi thẳng tên Paulette ("すまん、ポーレット") → "em".)
- **1769 [双鉄]** — JP 「余裕を持てる分、注視にも集中できる。利便性では、 ディーゼル機関は蒸気機関を遥かに上回っているな」 / TW 「操作方便，也就能更專注地進行觀察。單從便利性來說，柴油動車遠勝於蒸汽機車啊」 / Cũ: 「Nhờ có sự dư dả thời gian, tôi có thể tập trung quan sát hơn. Về tính tiện lợi,
động cơ diesel vượt xa động cơ hơi nước.」 → **「Nhờ có sự dư dả thời gian, anh có thể tập trung quan sát hơn. Về tính tiện lợi,
động cơ diesel vượt xa động cơ hơi nước.」** (Soutetsu nói với Reina (đoạn 1765 Reina giải thích hầm ngang, anh bình luận tiếp) → "anh".)
- **1775 [双鉄]** — JP 「可能性がゼロでないなら、検討してみて損はない。 僕はそう教わったし、ずっとそうして来ているだけだ」 / TW 「既然不是完全沒有可能，那麼探討一下也沒有壞處。我就是受到了這樣的教育，一直以來也都是這麼做的」 / Cũ: 「Nếu khả năng không phải là không, thì cứ thử xem xét cũng chẳng mất gì.
Tôi được dạy như vậy, và tôi chỉ luôn làm theo như thế thôi.」 → **「Nếu khả năng không phải là không, thì cứ thử xem xét cũng chẳng mất gì.
Anh được dạy như vậy, và anh chỉ luôn làm theo như thế thôi.」** (Soutetsu nói với Reina (giải thích cách làm việc của mình cho cô) → "anh".)
- **1833 [双鉄]** — JP 「そうなのか――あれはなにか、プラスチックの類で…… 石油か何かから作っているのかと思っていたが」 / TW 「是這樣啊——我還以為那個屬於塑膠類……是用石油之類的東西製成的」 / Cũ: 「Vậy sao——cái đó là một loại nhựa dẻo mà...
tôi cứ tưởng người ta làm từ dầu mỏ hay gì đó chứ.」 → **「Vậy sao——cái đó là một loại nhựa dẻo mà...
anh cứ tưởng người ta làm từ dầu mỏ hay gì đó chứ.」** (Soutetsu đáp lời Reina (cô vừa giải thích celluloid ở 1829–1834) → "anh".)
- **1862 [双鉄]** — JP 「ああ。もっと大規模な―― そうでなくては、再稼働を果たせん気がする」 / TW 「沒錯。更大規模——我覺得不這樣的話，礦山就無法恢復運作」 / Cũ: 「Đúng vậy. Ở quy mô lớn hơn nhiều——
Nếu không thì, tôi có cảm giác sẽ không thể nào tái hoạt động được.」 → **「Đúng vậy. Ở quy mô lớn hơn nhiều——
Nếu không thì, anh có cảm giác sẽ không thể nào tái hoạt động được.」** (Soutetsu nói với Reina (1859/1864 đều là Reina) → "anh".)
- **2006 [双鉄]** — JP 「それは何よりだ。が、済まなかったな。 歩くペースが速すぎたよな」 / TW 「那就太好了。真對不起啊，是我走得太快了」 / Cũ: 「Vậy thì tốt quá rồi. Nhưng mà xin lỗi em nhé.
Tôi đi nhanh quá phải không.」 → **「Vậy thì tốt quá rồi. Nhưng mà xin lỗi em nhé.
Anh đi nhanh quá phải không.」** (Soutetsu xin lỗi Reina — nhịp bước là của Reina (cf. độc thoại 2310: anh đi theo nhịp của mình mà không nghĩ đến bước chân của Reina) → "anh".)
- **2019 [双鉄]** — JP 「では、採炭を再開することは可能か？ つまり、権利や許認可関係において」 / TW 「那麼，能否重新開採煤炭？從權限和許可角度來說可行嗎」 / Cũ: 「Vậy thì, có khả năng khai thác than trở lại không?
Ý tôi là, về mặt quyền lợi và giấy phép các thứ.」 → **「Vậy thì, có khả năng khai thác than trở lại không?
Ý anh là, về mặt quyền lợi và giấy phép các thứ.」** (Soutetsu hỏi Paulette — về quyền/giấy phép, đúng mảng việc của cô (1748, 2004) → "anh".)

### SFX — tiếng cười bị diễn thành tiếng rên (7 dòng)

- **1538 [れいな]** — JP 「わぁぁ、うれしいですよぉ。えへへぇ、そうてつさん、 そんなことまで、覚えてくれてるんですねぇ」 / TW 「哇，好高興。哎嘿嘿，沒想到雙鐵先生連這種小事都記得呀」 / Cũ: 「Oaaa, Reina vui lắm ạ. E hèm~, anh Soutetsu,
nhớ cả những chuyện như vậy luôn đó hả~」 → **「Oaaa, Reina vui lắm ạ. Ehehe~, anh Soutetsu,
nhớ cả những chuyện như vậy luôn đó hả~」** (えへへぇ là tiếng cười khúc khích, không phải tiếng đằng hắng — "E hèm" trong tiếng Việt là hắng giọng. Tiền lệ: えへへっ→"Ehehe" (Grand 02), "Ehehe~!" (Grand 01).)
- **1624 [れいな]** — JP 「うふふぅ、おしごと、おつかれさまですぅ」 / TW 「嘻嘻嘻，上班辛苦啦」 / Cũ: 「Ư hự hự, mình đi làm vất vả rồi ạ~」 → **「Ufufu, mình đi làm vất vả rồi ạ~」** (うふふぅ là tiếng cười — "Ư hự" là tiếng rên, sai quy tắc Hieu 19/11 22:05 (tiếng cười diễn thành tiếng cười, KHÔNG thành tiếng rên). Tiền lệ: うふふ→"Ufufu" (nhiều file), h8 bãi bỏ "Ư hự" cho tiếng cười.)
- **1626 [れいな]** — JP 「うふふぅ、気にいってもらえてうれしいですよぉ」 / TW 「嘻嘻嘻，很高興雙鐵先生能喜歡」 / Cũ: 「Ư hự hự, anh thích là Reina vui rồi ạ~」 → **「Ufufu, anh thích là Reina vui rồi ạ~」** (Như 1624: うふふぅ → "Ufufu".)
- **1629 [れいな]** — JP 「うふふぅ、不思議ですよねぇ」 / TW 「嘿嘿嘿，很神奇對吧」 / Cũ: 「Ư hự hự, kỳ lạ anh nhỉ~」 → **「Ufufu, kỳ lạ anh nhỉ~」** (Như 1624: うふふぅ → "Ufufu".)
- **1630 [れいな]** — JP 「うふふぅ、そうですよぉ」 / TW 「嘿嘿嘿，沒錯啊」 / Cũ: 「Ư hự hự, đúng vậy đó ạ~」 → **「Ufufu, đúng vậy đó ạ~」** (Như 1624: うふふぅ → "Ufufu".)
- **1633 [れいな]** — JP 「うふふぅ、 おいしそうに食べてもらえて嬉しいですよぉ」 / TW 「嘿嘿嘿，看你吃得這麼津津有味，玲奈好高興哦」 / Cũ: 「Ư hự hự,
Thấy mình ăn ngon miệng thế này em vui lắm đó nha~」 → **「Ufufu,
Thấy mình ăn ngon miệng thế này em vui lắm đó nha~」** (Như 1624: うふふぅ → "Ufufu".)
- **1634 [れいな]** — JP 「うふふーぅ、そうてつさん、そうてつさんなのに、 ちょっとヘンなこといってますよぉ？」 / TW 「嘿嘿嘿，雙鐵先生平時那麼聰明，剛才卻說了很奇怪的話哦」 / Cũ: 「Ư hự hự~, anh Soutetsu, rõ ràng là anh Soutetsu mà,
lại nói chuyện hơi kỳ lạ rồi đó ạ~?」 → **「Ufufu~, anh Soutetsu, rõ ràng là anh Soutetsu mà,
lại nói chuyện hơi kỳ lạ rồi đó ạ~?」** (うふふーぅ → "Ufufu~" (thêm ~ cho trường âm ーぅ; tiền lệ うふふぉ→"Ufufu~").)

### Gasp っ — sweep (1 dòng)

- **2035 [双鉄]** — JP 「っ！」 / TW 「！」 / Cũ: 「!」 → **「Ư!」** (Sweep fix nguyên văn (lost-gasp-whole): JP 「っ！" toàn dòng là một tiếng nấc, VN chỉ còn dấu "!" — thêm Ư theo sweep.)

### Sai nghĩa (4 dòng)

- **1580 [双鉄]** — JP 「ああ、そうか！　 鉱山は、鉱山――つまり、山なのだな」 / TW 「啊，對啊！礦山就是礦山——也就是說，它是山」 / Cũ: 「À, ra vậy! 
Mỏ trên núi là mỏ trên núi――nghĩa là nó nằm trên núi.」 → **「À, ra vậy! 
Mỏ trên núi là mỏ trên núi――nghĩa là, nó chính là một ngọn núi.」** (JP/TW đều nói "mỏ chính là núi": JP 「鉱山は、鉱山――つまり、山なのだな」, TW 「礦山就是礦山——也就是說，它是山」. "Nó nằm trên núi" đổi quan hệ đồng nhất (mỏ = núi) thành quan hệ vị trí — mất đúng điểm ngộ ra của câu đùa chữ.)
- **1643 [れいな]** — JP 「れいなも、キハ[レイナナ,1]07も、力持ちさんですから」 / TW 「因為玲奈和Ｋｉｈａ０７都是大力士」 / Cũ: 「Cả Reina và KiHa 07 đều là những người khỏe mạnh mà lị~」 → **「Cả Reina và KiHa 07 đều khỏe mạnh mà lị~」** (KiHa 07 là toa tàu, không phải "người" — "đều là những người khỏe mạnh" gán nhầm phạm trù. Bỏ "là những người" là đủ.)
- **1663 [れいな]** — JP 「はぁい、今日は、肉じゃがと、 おネギとお麩のお味噌汁ですよぉ」 / TW 「好的，今天有馬鈴薯燉肉，還有蔥和麵筋熬成的味噌湯哦」 / Cũ: 「Vâng ạ, hôm nay có thịt hầm khoai tây,
và súp miso nấu với hành và váng đậu đó nha~」 → **「Vâng ạ, hôm nay có thịt hầm khoai tây,
và súp miso nấu với hành và phù đó nha~」** (お麩 là phù (mì căn — TW 麵筋 xác nhận), KHÔNG phải váng đậu (yuba — đậu phụ lá, món khác hẳn).)
- **2348 [monologue]** — JP 夏草を踏み、完全に[うず]埋もれているかつてのレールに、 その役割を思い出させる。 / TW 「Chẳng có gì lạ khi một mỏ than có nhà máy điện riêng. Reina chỉ tìm thử trên bản đồ thôi ạ」 / Cũ: Đạp lên đám cỏ dại mùa hè, trên đường ray cũ đã hoàn toàn bị vùi lấp,
tôi nhớ lại vai trò của nó. → **Đạp lên đám cỏ dại mùa hè, tôi gợi cho đường ray cũ đã hoàn toàn bị vùi lấp nhớ lại vai trò của nó.** (思い出させる là thể sai khiến: Soutetsu nhắc ĐƯỜNG RAY nhớ lại vai trò của nó — VN cũ đảo chiều chủ ngữ thành "tôi nhớ lại". (TW dòng này là bản sao nhầm của TW 1950 — lấy JP làm chuẩn.))

### Thuật ngữ đã chốt (3 dòng)

- **1644 [れいな]** — JP 「整備[ボディ]体では――だっこ、 ほとんどされることってないですからぁ」 / TW 「因為玲奈在使用整備體的的時候，沒怎麼被人抱起來過呢」 / Cũ: 「Vì ở hình dạng cơ thể bảo dưỡng——
hầu như chẳng bao giờ Reina được bế cả ạ.」 → **「Vì ở thân bảo trì——
hầu như chẳng bao giờ Reina được bế cả ạ.」** (整備体 = "thân bảo trì" (thuật ngữ đã chốt; tiền lệ sửa trong file: 00common11 key 2227). "Hình dạng cơ thể bảo dưỡng" chỉ là diễn giải, không phải thuật ngữ chuẩn.)
- **2218 [monologue]** — JP 確かに、いつも抱っこするハチロクは 運転ボディ――人形サイズの方の体だ。 / TW 但轉念一想，我平時的確只抱過八六的駕駛體——只有人偶大小的身體。 / Cũ: Đúng là, Hachiroku mà tôi vẫn thường hay bế
là ở hình dạng lái tàu——tức là cơ thể cỡ búp bê. → **Đúng là, Hachiroku mà tôi vẫn thường hay bế
là ở thân vận hành――tức là cơ thể cỡ búp bê.** (運転ボディ = "thân vận hành" (thuật ngữ đã chốt; "hình dạng lái tàu" chỉ là diễn giải).)
- **2349 [monologue]** — JP 御一夜-湯医間だけで孤立している僕らの線路が、 そのまま販路の、象徴のように思えてしまう。 / TW 我們那張被孤立於御一夜至湯醫之間的鐵路網，直接反映了目前的銷路情況。 / Cũ: Tuyến đường sắt của chúng tôi bị cô lập chỉ giữa Ohimitera và Yui,
cứ như thể là biểu tượng cho kênh phân phối của chúng tôi vậy. → **Tuyến đường sắt của chúng tôi bị cô lập chỉ giữa Ohitoyo và Yunoi,
cứ như thể là biểu tượng cho kênh phân phối của chúng tôi vậy.** (御一夜 = "Ohitoyo" (không phải "Ohimitera"), 湯医 = "Yunoi" (không phải "Yui") — thuật ngữ đã chốt; tiền lệ sửa trong file (00common11: Ohimitera→Ohitoyo 30 dòng, Yui→Yunoi 4 dòng).)

## §3. Kiểm tra sweep っ-gasp

- Sweep có **1 mục** cho file này: key **2035** (lost-gasp-whole, JP 「っ！", fix 「Ư!"), đã áp nguyên văn sau khi kiểm chứng đúng JP.
- Quét máy toàn bộ っ trong JP của file: không còn gasp nào bị mất. Các っ còn lại đều là っ trong từ (ちょっと, きっと, 抱っこ...), っ nhấn mạnh cuối từ không thêm Ư theo đúng quy tắc sweep (2040 れいなっ!? → "Reina!?", 2374 届かずっ―― → "với không tới——", 1546 えっ!? → "Hả!?", 1585 あ、いえっ → "A, không ạ."), hoặc đã diễn đúng (2629 （ひょいっ） → "Nhẹ nhàng nhấc bổng", 2631 （がしっ） → "Chộp lấy", 2632 （すてんっ） → "Phịch").
- Các tiếng cười khác trong file đã đúng, giữ nguyên: 1525 ふふっ → "Fufu", 2555 ふふっ → "cười khúc khích".

## §4. Lượt soát 2 + kiểm chứng cơ học

- Lượt soát 2: đọc lại toàn bộ **35/35** fix đối chiếu JP (in ở trên) — **35 tái xác nhận, 0 bỏ, 0 sửa**.
- Trước lượt soát 2, bước kiểm tra diff-sanity cơ học đã bắt được **3 lỗi do chính agent đưa vào** (thêm ngoặc 「」 vào 3 fix độc thoại vốn không có ngoặc: 2218, 2348, 2349) — đã sửa trước khi soát 2. Sau khi sửa, mọi fix chỉ khác VN cũ ở đúng chỗ cần sửa (xem diff ở §2).
- JSON `audit-reina01-tankou-wrong.json`: 35 mục dạng chuẩn list-of-dicts, khóa chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 35/35.
- Khối TOML dưới đây: 35 khóa, parse được bằng tomllib, **0 sai lệch giá trị** so với JSON.

## §5. Khối TOML đã kiểm chứng (35 khóa)

```toml
"1538" = "「Oaaa, Reina vui lắm ạ. Ehehe~, anh Soutetsu,\\nnhớ cả những chuyện như vậy luôn đó hả~」"
"1559" = "「À――chuyện đó, trước đây anh cũng từng nghe nói. Nhưng mà,\\nchính vì thế nên tất cả các loại dây điện đều được cách điện nghiêm ngặt rồi mà nhỉ?」"
"1580" = "「À, ra vậy! \\nMỏ trên núi là mỏ trên núi――nghĩa là, nó chính là một ngọn núi.」"
"1582" = "「À, quả nhiên là anh làm phiền em rồi.」"
"1599" = "「Ừm. Lái thử KiHa 07 rồi anh mới hiểu rõ.\\nLý do Paulette nói 8620 phù hợp với du lịch.」"
"1601" = "「Ừ. Chắc là vì anh đã rất ngạc nhiên.\\nMột \\x%lレイルロオド;#00ffc040;Railord%l;#; nhỏ bé thế này, mà lại đi chở hàng hóa sao――」"
"1606" = "「Ừm. Trăm sự nhờ em.」"
"1610" = "「Ừ, cứ giao cho anh.」"
"1611" = "「À, anh cũng từng nghe nói. Vì thua kém về chất lượng và cạnh tranh giá cả,\\nnên các mỏ than trong nước đều bị đẩy đến bờ vực đóng cửa.」"
"1614" = "「Ừ, em sẽ cố gắng.\\nVà――anh Soutetsu.」"
"1615" = "「Ừm, anh sẽ mong đợi lắm đấy.」"
"1624" = "「Ufufu, mình đi làm vất vả rồi ạ~」"
"1626" = "「Ufufu, anh thích là Reina vui rồi ạ~」"
"1629" = "「Ufufu, kỳ lạ anh nhỉ~」"
"1630" = "「Ufufu, đúng vậy đó ạ~」"
"1633" = "「Ufufu,\\nThấy mình ăn ngon miệng thế này em vui lắm đó nha~」"
"1634" = "「Ufufu~, anh Soutetsu, rõ ràng là anh Soutetsu mà,\\nlại nói chuyện hơi kỳ lạ rồi đó ạ~?」"
"1643" = "「Cả Reina và KiHa 07 đều khỏe mạnh mà lị~」"
"1644" = "「Vì ở thân bảo trì——\\nhầu như chẳng bao giờ Reina được bế cả ạ.」"
"1663" = "「Vâng ạ, hôm nay có thịt hầm khoai tây,\\nvà súp miso nấu với hành và phù đó nha~」"
"1691" = "「À, anh có chuyện muốn hỏi.\\nMỏ than này, liệu trữ lượng than có còn không?」"
"1742" = "「Để tìm kiếm những ý tưởng cộng thêm đó,\\nanh muốn tiến hành thêm các cuộc khảo sát quanh mỏ than bỏ hoang Jutsu-sen――」"
"1745" = "「Anh hiểu mà, chính vì thế,\\nnên anh mới nhờ em dạy lái \\x%lキハ07;#00ffc040;KiHa 07%l;#; mà.」"
"1747" = "「Lái tàu và khảo sát, anh sẽ thực hiện không để xảy ra sự cố nào.\\nHơn thế nữa――chắc chắn, anh sẽ tìm ra được manh mối gì đó.」"
"1763" = "「Xin lỗi nhé, Paulette.\\nEm đang mải suy nghĩ gì à?」"
"1769" = "「Nhờ có sự dư dả thời gian, anh có thể tập trung quan sát hơn. Về tính tiện lợi,\\nđộng cơ diesel vượt xa động cơ hơi nước.」"
"1775" = "「Nếu khả năng không phải là không, thì cứ thử xem xét cũng chẳng mất gì.\\nAnh được dạy như vậy, và anh chỉ luôn làm theo như thế thôi.」"
"1833" = "「Vậy sao——cái đó là một loại nhựa dẻo mà...\\nanh cứ tưởng người ta làm từ dầu mỏ hay gì đó chứ.」"
"1862" = "「Đúng vậy. Ở quy mô lớn hơn nhiều——\\nNếu không thì, anh có cảm giác sẽ không thể nào tái hoạt động được.」"
"2006" = "「Vậy thì tốt quá rồi. Nhưng mà xin lỗi em nhé.\\nAnh đi nhanh quá phải không.」"
"2019" = "「Vậy thì, có khả năng khai thác than trở lại không?\\nÝ anh là, về mặt quyền lợi và giấy phép các thứ.」"
"2035" = "「Ư!」"
"2218" = "Đúng là, Hachiroku mà tôi vẫn thường hay bế\\nlà ở thân vận hành――tức là cơ thể cỡ búp bê."
"2348" = "Đạp lên đám cỏ dại mùa hè, tôi gợi cho đường ray cũ đã hoàn toàn bị vùi lấp nhớ lại vai trò của nó."
"2349" = "Tuyến đường sắt của chúng tôi bị cô lập chỉ giữa Ohitoyo và Yunoi,\\ncứ như thể là biểu tượng cho kênh phân phối của chúng tôi vậy."
```

## §6. Giữ nguyên (phán đoán có ghi chú)

- **Paulette tự xưng "tôi" với Soutetsu ở 4 dòng công việc trang trọng (1717, 1748, 1920, 1987) — giữ nguyên.** Tiền lệ ROUTE-AUDIT: "Paulette tự xưng theo người nghe: 'tôi' ở hội đồng, 'em' với Soutetsu" — các dòng này đều là bàn việc (giấy phép, ngân hàng, hiệu quả chi phí), đúng ngữ cảnh trang trọng. Chỉ sửa 1614 vì "chị" mâu thuẫn với "anh Soutetsu" trong cùng dòng.
- **ふわわっ → "Phù oa" (1527, 1669) — giữ nguyên.** Nằm trong khoảng các tiền lệ ("ơ ơ" ở ハチロク06; "Oa oa oa" giữ theo TW ở lr-reina-tsuika01 1103); giữ cả âm ふ đầu lẫn わわ, không rõ ràng sai.
- **Tag %l bị bỏ ở 1070 (8620, キハ07, 客車) và 2539 (機関士) — giữ nguyên, không tính sai.** Gloss bằng chính thuật ngữ (8620→8620, キハ07→KiHa 07) hoặc đã diễn inline (客車→"toa hành khách", 機関士→"lái tàu"); không mất thông tin (tiền lệ ROUTE-AUDIT 625). Toàn file không có tag %l nào hỏng (0 tag sai định dạng).
- **1099 "để nhiệt điện" — giữ nguyên** (ngắn gọn kiểu điện báo nhưng nghĩa rõ). **1959 "Tự nhiên phát nổ?" — giữ nguyên** (câu hỏi lửng, "phát nổ" ngầm hiểu từ ngữ cảnh). **1551/1554/1594 các "Hửm?"/"Chà." — giữ nguyên.**

## §7. Dị thường nguồn + chờ Hieu (không tự quyết, không tính sai)

- **2415 — ô JP chứa tiếng Việt (dị thường nguồn, KHÔNG sửa được):** JP Original là "Bước đi xạo xạc." (tiếng Việt, không phải tiếng Nhật), TW là bản sao nhầm của TW 1917, và comment `# JP:` trong TOML cũng là "Bước đi xạo xạc." — dữ liệu gốc hỏng ở cả CSV3 lẫn TOML-2. VN "Bước đi xạo xạc." khớp đúng ô JP như hiện có. JP thật không rõ (nhiều khả năng là một dòng SFX tiếng bước chân) — cần nguồn gốc/Hieu mới sửa được.
- **2348 — TW là bản sao nhầm của TW 1950** ("Chẳng có gì lạ khi một mỏ than có nhà máy điện riêng...") — lấy JP làm chuẩn; fix theo JP.
- **1804 — TW là bản sao nhầm của một dòng khác** ("哦？礦山都是會專門配備發電廠的嗎" trong khi JP là 「そうですね。ちょっと盲点でした」) — VN theo JP là đúng, không sửa.
- **1726 — ô JP của CSV3 bị lỗi mã hóa** ("���再稼働、って？") nhưng comment `# JP:` trong TOML sạch (「再稼働、って？」); VN "Tái hoạt động, là sao cơ?" đúng — lỗi chỉ ở CSV, không tính sai.

## Kết bài

File れいな01_炭鉱探索: 403 dòng đã đọc hết, **35 dòng sai (8,7%)** — nặng nhất là cụm đại từ Soutetsu (20 dòng "tôi"/"cô" sai với Reina/Paulette, trong đó có 2 dòng "cô" cho Paulette và 1 dòng Paulette tự xưng "chị" mâu thuẫn khóa B4), tiếp theo là 7 tiếng cười うふふぅ/えへへぇ bị diễn thành tiếng rên, 4 sai nghĩa, 3 thuật ngữ đã chốt, 1 gasp sweep. Không có lệch vị trí/xoay vòng/nhiễm chéo/mồ côi/chưa dịch/trùng khóa. Lượt soát 2: 35/35 tái xác nhận, 0 bỏ, 0 sửa. Khối TOML 35 khóa parse đạt, 0 sai lệch. 1 dị thường nguồn (2415) chờ Hieu.
