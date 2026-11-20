# Audit — 日々姫04_カフェキッチン.txt.toml (02_Hibiki)

**File:** `02_Hibiki/日々姫04_カフェキッチン.txt.toml` — quán cà phê + bếp (Hibiki làm bồi bàn tập sự, cả nhóm bàn menu / trang trí cửa hàng đường sắt).
**TOML md5:** `4a1938affa114a330c4ec8a2c57c55e9` — 1 bản duy nhất (không có file trùng; file 04 còn lại trong thư mục là 同乗, khác file).
**Đọc:** 406/406 dòng script, đọc từng dòng đối chiếu JP + TW (CSV3). CSV3 1 bộ duy nhất cho file này, 0 key trùng, 0 ô VN trống.
**Kết quả: 42 dòng sai / 406 (10,3%).**

## §1. Phân loại

| Loại | Số dòng | Keys |
|---|---|---|
| Lệch dòng (VN không khớp JP của chính dòng đó) | 24 | 1720, 1726, 1894, 1956, 2011, 2093, 2101, 2106, 2191, 2240, 2303, 2305, 2461, 2464, 2469, 2480, 2505, 2603, 2665, 2668, 2670, 2746, 2763, 2781 |
| Bịa thêm (tự hoàn thiện câu JP cụt) | 1 | 1938 |
| SFX cười うふふ dịch thành tiếng rên 'Ư hư hư' | 6 | 1828, 1831, 1833, 1836, 1837, 2273 |
| Mất tiếng thở っ (sweep) | 2 | 1306, 1909 |
| Đại từ Soutetsu 'tôi' → 'anh' | 2 | 1708, 1721 |
| Thuật ngữ カフェ/喫茶店 → 'quán giải khát' | 5 | 1808, 1903, 1970, 2261, 2527 |
| Màu 柿色 → 'màu hồng vàng' | 2 | 2125, 2219 |
| **Tổng** | **42** | |

## §2. Nhiễm chéo và lệch dòng

- **15 dòng nhiễm chéo từ tư liệu Mikuro/D51:** 1720, 1726, 1956, 2011, 2093, 2101, 2191, 2240, 2305, 2603, 2668, 2670, 2746, 2763, 2781. VN cũ nói về Mikuro, D51 1031 ở Yufuin, sở thú Omuta, tòa thị chính Omuta, 'cỗ máy tơi tả' — không liên quan gì tới cảnh quán cà phê. Đã kiểm tra toàn bộ CSV3: các chuỗi VN này CHỈ xuất hiện ở chính các key đó trong file này (không có ở file nào khác); JP tương ứng của chúng nằm ở các file Hibiki 03 (湯富院), Hibiki 06 (みくろ、来訪) và Grand 09 — tức là VN đã bị dán chéo file trong lúc dịch bằng Sheets.
- **9 dòng lệch rời rạc (VN là đoạn văn/mảnh câu không khớp JP, không tìm thấy JP nguồn nào trong file):** 1894 (narration về giọng Hibiki), 2106 (narration về 'vinh dự'), 2303 ('Tại sao'), 2461 ('Ra vậy, thảo nào lại hợp ý tôi'), 2464 ('Làm gương?'), 2469 ('Hô.'), 2480 ('Chắc là vậy rồi.'), 2505 ('Ra vậy.'), 2665 ('À——').
- **Key 2480 (đã được flag từ audit trước): ĐÃ XÁC NHẬN lệch dòng.** JP: 'Thực ra, có bàn với ghế thì tốt thật, nhưng nhà mình không có, nên cũng đành chịu thôi.' — VN cũ 'Chắc là vậy rồi.' không liên quan. JP và TW khớp nhau hoàn toàn.
- **Không có rotation chain trong file:** đã kiểm tra — không có VN đúng nào nằm sai key trong file này; các dòng sai đều phải dịch mới từ JP, không thể hoán đổi key để sửa. Không có dòng orphan theo nghĩa 'VN không có JP nguồn ở đâu trong dự án' ngoài 15 dòng nhiễm chéo trên (JP nguồn của chúng ở file Hibiki 03/06/Grand 09).
- **0 dòng chưa dịch, 0 key trùng, 0 tag %l hỏng.** File có 1 tag %l duy nhất (key 2219, キハ07s) — được giữ nguyên vẹn, chỉ sửa màu.

## §3. Từng dòng sai

### 1306 [monologue] — Mất tiếng thở っ (sweep)
JP: ……ねぇね。ねぇねぇ――っ！？
TW: ……阿姐。阿姐——？！
VN cũ: ……Chị. Chị hai——!?
Fix: ……Chị. Chị hai——Ư!?
Ghi chú: Adopt nguyên fix của sweep (lost-gasp-trailing): JP kết bằng ――っ！？, VN cũ giữ dấu gạch nhưng mất tiếng thở.

### 1708 [双鉄] — Đại từ Soutetsu (tôi → anh)
JP: 「すまんな、助かる。\nその言葉に甘えすぎぬよう、頼らせてもらう」
TW: 「不好意思，那就先謝謝你了。我會儘量不給你多添麻煩的」
VN cũ: 「Cảm ơn cô, giúp được tôi nhiều lắm.\nTôi sẽ nhờ vả cô, nhưng sẽ cố gắng không ỷ lại quá nhiều vào lời nói đó.」
Fix: Cảm ơn cô, giúp được anh nhiều lắm. Anh sẽ nhờ vả cô, nhưng sẽ cố gắng không ỷ lại quá nhiều vào lời nói đó.
Ghi chú: Soutetsu nói trực tiếp với Paulette (dòng 1707 là Paulette nói với Soutetsu) → 'anh' theo quy tắc đã sửa. JP không có 僕 nhưng VN diễn xưng hô ngôi thứ nhất — sửa theo địa chỉ.

### 1720 [日々姫] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 「『ぼくでよければ、かまわんぞ』って！\nにぃに、やさしかよねー？　くまくま！」
TW: 「不過阿哥跟我說“你不介意的話，我可以當客人哦”！他很溫柔吧，熊熊！」
VN cũ: 「Là chị Hachiroku——là mọi người ở Đường sắt Ohimitera ạ.\nNhìn thấy chị ấy, Mikuro nghĩ rằng, biết đâu mình cũng có thể làm được.」
Fix: 「『Nếu em không ngại anh thì anh làm cũng được』đó! Anh hai tốt bụng nhỉ? Kumakuma!」
Ghi chú: VN cũ là narration về Mikuro/Hachiroku — thuộc tư liệu Mikuro/D51 (nhiễm chéo từ file Hibiki 03/06). Fix mới dịch đúng JP (Hibiki trích lời Soutetsu).

### 1721 [双鉄] — Đại từ Soutetsu (tôi → anh)
JP: 「いや、僕はむしろ――」
TW: 「不，我的意思是——」
VN cũ: 「Không, tôi ngược lại còn——」
Fix: Không, anh ngược lại còn——
Ghi chú: Soutetsu đáp lại Hibiki (dòng 1720 là Hibiki nói về Soutetsu) → 'anh'.

### 1726 [日々姫] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 「きれいく　かざりつけ　できたとばい！\nね？　くまくま」
TW: 「並且～裝點得～漂漂亮亮的！對吧，熊熊？」
VN cũ: Nếu không có doanh thu, thì cũng không có dư dả tiền bạc để bảo dưỡng cỗ máy bảo tồn.\nMikuro ít nhất vẫn đang cố gắng dọn dẹp xung quanh, nhưng...
Fix: Trang trí xong đẹp đẽ rồi đây! Nhỉ? Kumakuma!

### 1808 [双鉄] — Thuật ngữ カフェ/喫茶店 → quán giải khát
JP: 「そうとも言えるし、そうでないとも言える。\n話したとおり、このカフェの集客についてなのだが」
TW: 「可以說是，也可以說不是。是我們剛才說到的，有關這間咖啡廳攬客的事情」
VN cũ: 「Nói vậy cũng đúng, mà không phải cũng đúng.\nNhư đã nói, là về việc thu hút khách hàng cho quán giải khát này.」
Fix: Nói vậy cũng đúng, mà không phải cũng đúng. Như đã nói, là về việc thu hút khách hàng cho quán cà phê này.

### 1828 [真闇] — SFX cười (うふふ) dịch thành tiếng rên
JP: 「うふふ……何年ぶりかねぇ。\nひーちゃんを、こぎゃんとしてあげるとは」
TW: 「呵呵……好多年沒有讓你枕在我腿上了啊」
VN cũ: 「Ư hư hư……Mấy năm rồi nhỉ.\nMới lại làm thế này với bé Hii.」
Fix: Ufufu……Mấy năm rồi nhỉ. Mới lại làm thế này với bé Hii.

### 1831 [れいな] — SFX cười (うふふ) dịch thành tiếng rên
JP: 「うふふぅ、おあついですねぇ」
TW: 「呵呵，兩位還真是熱乎呀」
VN cũ: 「Ư hư hư~, hai người nồng nhiệt quá nha~」
Fix: Ufufuu~, hai người nồng nhiệt quá nha~

### 1833 [ハチロク] — SFX cười (うふふ) dịch thành tiếng rên
JP: 「うふふ、責任重大でございますね。\nどうぞご安心しておまかせください、双鉄様」
TW: 「呵呵，我真是責任重大啊。請您放心，雙鐵少爺」
VN cũ: 「Ư hư hư, trách nhiệm nặng nề quá nhỉ.\nXin ngài Soutetsu cứ yên tâm giao cho em ạ.」
Fix: Ufufu, trách nhiệm nặng nề quá nhỉ. Xin ngài Soutetsu cứ yên tâm giao cho em ạ.

### 1836 [れいな] — SFX cười (うふふ) dịch thành tiếng rên
JP: 「うふふぅ。だからこーんなに、\nメニュー案、たくさんたくさんになっちゃいましたぁ」
TW: 「呵呵，所以菜品的方案才會多出這麼多」
VN cũ: 「Ư hư hư~. Thế nên mới có nhiều,\nthật nhiều đề xuất menu như thế này đó ạ~」
Fix: Ufufuu~. Thế nên mới có nhiều, thật nhiều đề xuất menu như thế này đó ạ~

### 1837 [れいな] — SFX cười (うふふ) dịch thành tiếng rên
JP: 「うふふぅ、平気ですよぉ。\nそういう暑さじゃないですからぁ」
TW: 「呵呵，沒事啦。我不是指這種熱」
VN cũ: 「Ư hư hư~, không sao đâu ạ.\nKhông phải nóng kiểu đó đâu ạ~」
Fix: Ufufuu~, không sao đâu ạ. Không phải nóng kiểu đó đâu ạ~

### 1894 [双鉄] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 「ああ、うん。僕はお客さんなのだよな」
TW: 「啊，嗯，我是客人啊」
VN cũ: Giọng nói của Hibiki, quả nhiên vẫn rất cứng rắn.\nKhi tôi vội vàng nhìn sang, biểu cảm của em ấy cũng đang căng cứng.
Fix: À, ừm. Anh là khách mà nhỉ.
Ghi chú: VN cũ là đoạn narration về giọng nói của Hibiki — không có JP nào trong file này khớp với nó (đã kiểm tra toàn file). Fix mới dịch đúng JP, đại từ Soutetsu → 'anh' (đang nói với Hibiki).

### 1903 [双鉄] — Thuật ngữ カフェ/喫茶店 → quán giải khát
JP: 「ああ、確かに。\nホテルのカフェには、それでも人が入っているな」
TW: 「啊，確實。即便如此，賓館的咖啡廳還是會有人啊」
VN cũ: 「À, đúng thật.\nQuán giải khát của khách sạn vẫn có người vào mà.」
Fix: À, đúng thật. Quán cà phê của khách sạn vẫn có người vào mà.

### 1909 [日々姫] — Mất tiếng thở っ (sweep)
JP: 「っ！！！？」
TW: 「啊？！」
VN cũ: 「!!!?」
Fix: 「Ư!!!?」
Ghi chú: Adopt nguyên fix của sweep (lost-gasp-whole): JP cả dòng chỉ là っ！！！？, VN cũ chỉ còn dấu câu.

### 1938 [日々姫] — Bịa thêm — tự hoàn thiện câu JP bị cụt
JP: 「うん！　だってねぇねに」
TW: 「嗯！我想親手給阿姐泡檸檬茶」
VN cũ: 「Vâng! Tại vì chị hai bảo」
Fix: Vâng! Tại vì là cho chị hai…
Ghi chú: JP bị cụt giữa chừng (だってねぇねに). VN cũ tự bịa phần hoàn thiện ('chị hai bảo') — không có cơ sở trong JP. Fix giữ nguyên dạng cụt. TW hoàn thiện thành 'tự tay pha trà chanh cho chị hai' (xem §6 — chờ Hieu chốt).

### 1956 [日々姫] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 「えへへー」
TW: 「嘿嘿嘿」
VN cũ: Mikuro đang kể cho chúng tôi nghe. "D51 ở một khu du lịch"\nTrước tiên, phải thu hút sự chú ý vào chiếc D51 số 1031 ở Yufuin này.
Fix: Hì hì~

### 1970 [日々姫] — Thuật ngữ カフェ/喫茶店 → quán giải khát
JP: 「だって！　いっとう最初は\nカフェもキッチンも計画なかったけん」
TW: 「因為，最開始是不打算要咖啡廳和廚房的嘛」
VN cũ: 「Tại vì! Ban đầu\nhoàn toàn không có kế hoạch làm quán giải khát hay nhà bếp mà.」
Fix: Tại vì! Ban đầu hoàn toàn không có kế hoạch làm quán cà phê hay nhà bếp mà.

### 2011 [日々姫] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 「そうだ！　みだしなみ！　きれいくしないと！\nせっかくにぃにが、おきゃくさんやけん！！」
TW: 「對了！打扮！得打扮得漂亮點才行！難得阿哥要來當客人！！」
VN cũ: 「Vì vậy Mikuro, đã suy nghĩ rất nhiều.\nVí dụ như, nếu là D51 ở một khu du lịch, thì có lẽ sẽ thu hút sự chú ý chăng.」
Fix: Đúng rồi! Phải ăn mặc cho chỉnh tề! Phải làm cho thật đẹp mới được! Hiếm khi anh hai làm khách thế này!!

### 2093 [日々姫] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 「あとは、にぃにを　まてばよかとねー。\nえ？　なぁに？　くまくま？」
TW: 「接下來，等阿哥來就好囉。哎？怎麼啦？熊熊」
VN cũ: Dù có dọn dẹp xung quanh cỗ máy tơi tả sạch sẽ đến đâu,\nthì sự tơi tả của cỗ máy lại càng trở nên nổi bật hơn——
Fix: Sau đó, chỉ cần đợi anh hai đến là được nhỉ. Hả? Gì vậy? Kumakuma?

### 2101 [日々姫] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 「ひびきちゃん……えへへ～！　とってもよかと！\nウェイトレスさん、におーとるばい！！」
TW: 「日日姬……嘿嘿嘿～！老好看了！特別像女服務員！！」
VN cũ: 「Nếu làm được như vậy, nếu thành công. Thì tòa thị chính Omuta\nvà người dân thành phố, chắc chắn cũng sẽ đến xem 38696 ạ.」
Fix: Hibiki-chan……hì hì~! Hợp lắm luôn! Trông đúng là cô bồi bàn rồi!!

### 2106 [双鉄] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 「日々姫？　僕だ。入ってもいいのか？」
TW: 「日日姬，是我。我可以進來嗎？」
VN cũ: 「Nếu vậy thì, thật là một điều vô cùng vinh dự.\nVề phía chúng tôi, nếu có việc gì có thể giúp được」
Fix: Hibiki? Anh đây. Anh vào được không?
Ghi chú: VN cũ là đoạn narration về 'vinh dự' — không có JP nào trong file khớp. Fix mới dịch đúng JP, đại từ Soutetsu → 'anh' (đang nói với Hibiki).

### 2125 [れいな] — Màu 柿色 dịch sai
JP: 「はぁい、そおですよぉ。ベージュが普通のプリンで、\n柿色のとこはイチゴ味ってききましたぁ」
TW: 「是啊是啊。聽說米黃色的是普通的布丁，赤褐色的是草莓味的」
VN cũ: 「Vâng, đúng rồi nha. Màu be là bánh flan bình thường,\ncòn phần màu hồng vàng là vị dâu tây đó ạ.」
Fix: Vâng, đúng rồi nha. Màu be là bánh flan bình thường, còn phần màu vàng cam là vị dâu tây đó ạ.
Ghi chú: TW ghi 柿色 là 赤褐色 (nâu đỏ); JP 柿色 = màu quả hồng — 'vàng cam' là cách diễn gần nhất trong tiếng Việt. Xem §6.

### 2191 [日々姫] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 「おさら、よかと。クッキー、よかと」
TW: 「盤子，準備好嘞。餅乾，準備好嘞」
VN cũ: ...Sở thú Omuta, có vẻ như đang vô cùng chật vật\nvì lượng khách tham quan sụt giảm.
Fix: Đĩa, xong rồi. Bánh quy, xong rồi.

### 2219 [ハチロク] — Màu 柿色 dịch sai
JP: 「ひょっとして――ベージュと柿色。\n\x%lキハ07s;#00ffc040;キハ07s%l;#;の二色の塗り分けに、ですか？」
TW: 「該不會……是代表\x%lキハ07s;#00ffc040;Ｋｉｈａ０７Ｓ%l;#;的米黃色和赤褐色吧？」
VN cũ: 「Có khi nào là——màu be và màu hồng vàng.\nĐược sơn thành hai màu của \x%lキハ07s;#00ffc040;Kiha 07S%l;#; sao ạ?」
Fix: Có khi nào là——màu be và màu vàng cam. Được sơn thành hai màu của \x%lキハ07s;#00ffc040;Kiha 07S%l;#; sao ạ?
Ghi chú: Tag %l được giữ nguyên vẹn như VN cũ; chỉ sửa 'màu hồng vàng' → 'màu vàng cam'. TW ghi 柿色 là 赤褐色 (nâu đỏ) — xem §6.

### 2240 [日々姫] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 「ねぇねぇの ゆってくれた とおりとー！\nおあつらえしてもろーたみたいに、ぴったりばい！」
TW: 「跟阿姐說得一樣！就像是為我量身訂製的一樣，老合適啦！」
VN cũ: 「...Dù có nghĩ ra, thì cũng rất khó để bắt tay vào thực hiện.\nMikuro, em thực sự rất tích cực và chủ động đấy.」
Fix: Đúng như chị hai đã nói luôn! Như thể được đặt làm riêng cho em vậy, vừa khít luôn!

### 2261 [真闇] — Thuật ngữ カフェ/喫茶店 → quán giải khát
JP: 「ここば、噂の喫茶店？\nんー、雰囲気よさそうなお店やねぇ」
TW: 「這裡就是傳聞中的咖啡廳？嗯，氣氛還不錯嘛」
VN cũ: 「Đây là quán giải khát trong lời đồn sao?\nHừm, quán có vẻ có bầu không khí tốt nhỉ.」
Fix: Đây là quán cà phê trong lời đồn sao? Hừm, quán có vẻ có bầu không khí tốt nhỉ.

### 2273 [真闇] — SFX cười (うふふ) dịch thành tiếng rên
JP: 「なら、もう１５分。\nうふふ、おねえちゃんも臨時休憩」
TW: 「那就再休息１５分鐘。呵呵，姐姐也來臨時休息一會」
VN cũ: 「Vậy thì, 15 phút nữa.\nƯ hư hư, chị cũng tạm thời nghỉ ngơi một chút.」
Fix: Vậy thì, 15 phút nữa. Ufufu, chị cũng tạm thời nghỉ ngơi một chút.

### 2303 [日々姫] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 「にぃに！　あ、じゃなくて、ええとね！\n『いらっしゃいませー！』」
TW: 「阿哥！啊，不對，搞錯了！歡迎光臨！」
VN cũ: 「Tại sao」
Fix: 「Anh hai! A, không phải, ừm nè! 『Kính chào quý khách—!』」

### 2305 [日々姫] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 「ひとりでお湯ばわかしたらダメって、ねぇねぇに\nいわれてるし……ううう……早くきてほしかとよぉ」
TW: 「阿姐也吩咐過我不要一個人燒熱水……嗚嗚嗚……阿哥趕緊來啊」
VN cũ: Kế hoạch mà Mikuro đưa ra, chính là một biến thể của những gì chúng tôi đã làm cho đến nay,\ncủa việc khôi phục và mở rộng tuyến đường với Hachiroku làm ngọn cờ đầu.
Fix: Chị hai đã dặn là không được tự mình đun nước sôi……ư ư ư……mong anh mau đến quá.

### 2461 [monologue] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: でも……うーん、ちょっとにぃにぃおそくない？\nまほうびんのお湯、さめちゃうかも。
TW: 但是……嗯，阿哥來得是不是有點晚啊？保溫瓶裡的熱水可能會冷掉的。
VN cũ: Ra vậy, thảo nào lại hợp ý tôi đến thế.
Fix: Nhưng mà……ừm, anh hai có hơi đến muộn không nhỉ? Nước nóng trong bình giữ nhiệt có khi nguội mất.

### 2464 [monologue] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: おきゃくさん……でも、\nだれもこないと、さみしすぎってこわかったけど。
TW: 但是……如果一個客人都沒有的話就太冷清了，我有點害怕。
VN cũ: 「Làm gương?」
Fix: Khách hàng……nhưng mà, nếu không có ai đến thì buồn lắm, mình đã sợ như thế.

### 2469 [monologue] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: ばってん、かがみん前まで走らんでよか。\nだって、わたしには　こいばあるけん。
TW: 但是，我沒有必要跑到鏡子前。因為，我還有這個東西。
VN cũ: 「Hô.」
Fix: Nhưng mà, mình không cần phải chạy đến trước gương đâu. Vì mình đã có cái này rồi.

### 2480 [monologue] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 本当は、テーブルと おいすが よかばってん、\nうちにはなかけん、しかたなかとよ。
TW: 其實，如果家裡有餐桌和椅子的話就好了，但咱家沒有，所以沒辦法。
VN cũ: 「Chắc là vậy rồi.」
Fix: Thực ra, có bàn với ghế thì tốt thật đấy, nhưng nhà mình không có, nên cũng đành chịu thôi.
Ghi chú: Key đã được flag từ audit trước là có thể lệch dòng — ĐÃ XÁC NHẬN: VN cũ ('Chắc là vậy rồi.') không liên quan gì tới JP (bàn ghế ở nhà). JP/TW khớp nhau.

### 2505 [monologue] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: あかいじんじゃさんのお祭りで、\nこども会のみんなでだした、おみせやさん。
TW: 在赤井神社的祭典上，兒童會的小伙伴們曾經一起玩過開店遊戲。
VN cũ: 「Ra vậy.」
Fix: Ở lễ hội đền Akai, bọn trẻ trong hội thiếu nhi đã cùng nhau mở một gian hàng.

### 2527 [monologue] — Thuật ngữ カフェ/喫茶店 → quán giải khát
JP: くつろげるカフェを選ぶなら、\n選択基準の一番最初に来るのは、やはり――
TW: 如果要選能讓人放鬆的咖啡廳，首要的選擇標準果然還是……
VN cũ: Nếu phải chọn một quán giải khát để thư giãn,\nthì tiêu chí lựa chọn đầu tiên, quả nhiên là——
Fix: Nếu phải chọn một quán cà phê để thư giãn, thì tiêu chí lựa chọn đầu tiên, quả nhiên là——

### 2603 [monologue] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: やけん、ウェイトレスさん　してみたくって、\nきっさてんば、じぶんでひらいてみたくって。
TW: 所以我想試著當一當女服務員，想試著自己開一間咖啡廳。
VN cũ: 「Mikuro, không được như vậy đâu ạ. Có thể hành động, chỉ là vì,\nem ngưỡng mộ——và muốn lấy làm gương thôi ạ.」
Fix: Nên mình muốn thử làm cô bồi bàn, muốn thử tự mình mở một quán cà phê.

### 2665 [monologue] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 『そうてつくんは　やさしいよね』って、\nくまくまもゆーてくれてる！
TW: 熊熊也說“雙鐵好溫柔”！
VN cũ: 「À——」
Fix: 『Anh Soutetsu hiền lành nhỉ』, Kumakuma cũng nói với mình như thế đó!

### 2668 [monologue] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: ざたくのむかいのざぶとんの上、\nくまくまが『できたね！』ってにこにこしとる。
TW: 熊熊在在矮桌另一頭的坐墊上微笑著說“你做得太棒了！”。
VN cũ: 「Mikuro nhận ra rằng, nếu cứ thế này thì sẽ dần lụi tàn mất thôi.」
Fix: Trên tấm đệm ngồi đối diện bàn thấp, Kumakuma cười tươi nói 『Làm được rồi nhỉ!』.

### 2670 [monologue] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: くまくまの目、なにか言っとー\n『ひびきちゃんの　みだしなみは？』って――！
TW: 熊熊的雙眼似乎在說——“日日姬，你不用打扮一下嗎？”！
VN cũ: Cảm giác tội lỗi mà người ta có thể cảm nhận được khi nhìn thấy cảnh tượng đó,\ntôi không nghĩ những vị khách đến xem sở thú lại muốn trải qua.
Fix: Đôi mắt Kumakuma, dường như đang muốn nói gì đó——『Trang phục của Hibiki-chan thì sao?』——!

### 2746 [monologue] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: 帰りにバザーで　かってもらったこんふくば、\nわたしには かわゆかすぎかもって思うとったけど。
TW: 這件在回家路上路過義賣會上買的衣服，對我來說似乎有點太過可愛了。
VN cũ: Lấy ví dụ thành công làm ngọn cờ đầu, rồi lan truyền nó ra xung quanh.\nCách tư duy này, tôi rất [hiểu, 1]hiểu, và cũng rất hợp ý tôi.
Fix: Bộ đồ được mua cho mình ở hội chợ trên đường về, mình đã nghĩ có lẽ nó hơi dễ thương quá so với mình.

### 2763 [monologue] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: ふすまばあけて、にいにがはいってくる。
TW: 阿哥拉開拉門進來了。
VN cũ: 「Vì lý do gì, mà đứa bé này lại bị bỏ lại ở đây?\nTại sao, lại không có ai chăm sóc cho đứa bé này?」
Fix: Mở cửa kéo ra, anh hai bước vào.

### 2781 [monologue] — Lệch dòng — VN không khớp JP của chính dòng đó
JP: ねぇねぇにもらったコンパクト！\nおもちゃのじゃなか、おねーさんば使うやつ！
TW: 阿姐給我的帶鏡粉盒！不是玩具，而是姐姐用過的！
VN cũ: Dọn dẹp, kêu gọi tình nguyện viên,\nphục hồi nó trở lại trạng thái sạch đẹp, biến nó thành một điểm thu hút khách du lịch.
Fix: Hộp phấn mà chị hai tặng mình! Không phải đồ chơi đâu, là loại mà các chị hay dùng đó!

## §4. Sweep っ-gasp

- Sweep có đúng 2 entry cho file này (1306 lost-gasp-trailing, 1909 lost-gasp-whole) — cả 2 đều đúng, đã adopt nguyên fix của sweep.
- Các っ gắn liền từ ở cuối câu (1716 やだっ → 'Không chịu', 1886 きゃっ → 'á', 2028 ひーちゃんっっ, 2029 双ちゃんっ/そん手っ, 2104 危ないっ) được giữ nguyên theo quy tắc 'っ nhấn mạnh cuối câu không phải tiếng thở' — sweep cũng không flag các dòng này, nhất quán.

## §5. Lượt soát 2 (second pass)

- **Tổng: 42 / tái kiểm chứng: 42 / bỏ: 0 / sửa: 1.**
- 1 sửa trong lượt soát 2: key 2273 — bản fix đầu đã làm rơi câu đầu 'Vậy thì, 15 phút nữa.' (chỉ được sửa tiếng cười, không được bỏ câu); đã khôi phục đủ cả 2 câu rồi mới đối chiếu lại với JP.
- JSON 42 khóa chuỗi, dạng chuẩn list-of-dicts (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 42/42 (kiểm tra bằng máy).
- Khối TOML parse OK (tomllib), 42 khóa, 0 sai lệch giá trị so với JSON. Tất cả fix đều 1 dòng, không có `\n` thủ công (game tự ngắt dòng). Tag %l ở 2219 được escape đúng (`\\x%l…`) nên parse ra đúng giá trị `\x%l…`.
- Diff-sanity: các fix loại terminology/color/pronoun/sfx chỉ sửa đúng chỗ cần sửa; các fix loại misaligned/fabrication viết lại toàn dòng vì toàn bộ VN cũ đều sai (đã đối chiếu từng dòng với JP/TW).

## §6. Phán đoán ghi chú — CẦN HIEU (không tự quyết)

- **1938 (câu JP cụt):** JP 'うん！　だってねぇねに' cụt giữa chừng; fix giữ dạng cụt ('Vâng! Tại vì là cho chị hai…'). TW hoàn thiện thành 'em muốn tự tay pha trà chanh cho chị hai' — có cơ sở ngữ cảnh (Hibiki đang thái chanh ở 1906, trà chanh xuất hiện ở 2207). Hieu chốt có lấy phần hoàn thiện của TW không.
- **2125 / 2219 (柿色):** fix 'màu vàng cam'. TW ghi 柿色 là 赤褐色 (nâu đỏ). Nếu Hieu muốn theo TW thì đổi thành 'màu nâu đỏ' — để Hieu chốt.
- **Đại từ Soutetsu giữ nguyên 'tôi' (đã kiểm tra, không sửa):** 1811/1813 (nói với cả nhóm trong quán, có Hibiki nhưng cũng có Paulette/Kisaki/Yamazaki — theo tiền lệ Paulette 14 key 1544, địa chỉ nhóm → 'tôi'); 1862 (không rõ hỏi ai — Hibiki hay Yamazaki — giữ nguyên); 1940/1941 (nói về Paulette với cả nhóm, địa chỉ không rõ); 1892 ('Tôi đi một mình' — JP không có 僕, 'tôi' là thêm vào, không sai); 2279 ('để tôi chọn' — JP không có 僕). Kisaki giữ nguyên 'tôi' ở 1759/2015 (nói với nhóm gồm Soutetsu + Yamazaki / cả nhóm — địa chỉ hỗn hợp, tiền lệ nhóm → 'tôi').
- **Không sửa (ghi chú, không tính sai):** 御一夜 → 'Ohimitera' (1882, 2017, 2310 — chờ đợt thống nhất Ohitoyo); 帝都 → 'thủ đô' ở 2134 (chưa có thuật ngữ chốt cho 帝都); 機関助士 → 'phụ lái tàu' (2067, 2501 — nhất quán trong file; TW là 司爐 'lính đốt lò', có thể bàn lại sau); ruby [ハチロク,3]8620 bị lược ở 1918/2012 (TW giữ 八六 — chỉ mất biệt danh của đầu máy, không mất nghĩa); 1974 'Ác mộng á!' cho 夢って (ngữ cảnh: Mayami hỏi 'gặp ác mộng à?' ở 2025); 1821 thêm 'vắng vẻ' (ngữ cảnh quán vắng, TW không thêm nhưng JP hàm ý); 1845 Hibiki tự xưng 'chị' với Reina (Reina nhỏ tuổi hơn); 2213 'bị gọi đến đây ạ?' (thiếu chủ ngữ, viết thường chữ đầu — nghĩa vẫn đủ); 2807 tiếng bíp 4 → 3 ('Bíp bíp bíp'); 2814 còi xe cứu thương diễn thành lời miêu tả thay vì âm thanh ('Tiếng còi xe cứu thương').
- **'(Hibiki)' / '(Soutetsu)' ở đầu một số VN monologue** (2456, 2536, 2666, 2714): nhãn người kể do dịch giả thêm vào — không sai nghĩa, giữ nguyên.

## §7. Khối TOML (đã parse-verified: 42 khóa, 0 sai lệch)

```toml
[script]
# JP: ……ねぇね。ねぇねぇ――っ！？
"1306" = "……Chị. Chị hai——Ư!?"
# JP: 「すまんな、助かる。\\nその言葉に甘えすぎぬよう、頼らせてもらう」
"1708" = "Cảm ơn cô, giúp được anh nhiều lắm. Anh sẽ nhờ vả cô, nhưng sẽ cố gắng không ỷ lại quá nhiều vào lời nói đó."
# JP: 「『ぼくでよければ、かまわんぞ』って！\\nにぃに、やさしかよねー？　くまくま！」
"1720" = "「『Nếu em không ngại anh thì anh làm cũng được』đó! Anh hai tốt bụng nhỉ? Kumakuma!」"
# JP: 「いや、僕はむしろ――」
"1721" = "Không, anh ngược lại còn——"
# JP: 「きれいく　かざりつけ　できたとばい！\\nね？　くまくま」
"1726" = "Trang trí xong đẹp đẽ rồi đây! Nhỉ? Kumakuma!"
# JP: 「そうとも言えるし、そうでないとも言える。\\n話したとおり、このカフェの集客についてなのだが」
"1808" = "Nói vậy cũng đúng, mà không phải cũng đúng. Như đã nói, là về việc thu hút khách hàng cho quán cà phê này."
# JP: 「うふふ……何年ぶりかねぇ。\\nひーちゃんを、こぎゃんとしてあげるとは」
"1828" = "Ufufu……Mấy năm rồi nhỉ. Mới lại làm thế này với bé Hii."
# JP: 「うふふぅ、おあついですねぇ」
"1831" = "Ufufuu~, hai người nồng nhiệt quá nha~"
# JP: 「うふふ、責任重大でございますね。\\nどうぞご安心しておまかせください、双鉄様」
"1833" = "Ufufu, trách nhiệm nặng nề quá nhỉ. Xin ngài Soutetsu cứ yên tâm giao cho em ạ."
# JP: 「うふふぅ。だからこーんなに、\\nメニュー案、たくさんたくさんになっちゃいましたぁ」
"1836" = "Ufufuu~. Thế nên mới có nhiều, thật nhiều đề xuất menu như thế này đó ạ~"
# JP: 「うふふぅ、平気ですよぉ。\\nそういう暑さじゃないですからぁ」
"1837" = "Ufufuu~, không sao đâu ạ. Không phải nóng kiểu đó đâu ạ~"
# JP: 「ああ、うん。僕はお客さんなのだよな」
"1894" = "À, ừm. Anh là khách mà nhỉ."
# JP: 「ああ、確かに。\\nホテルのカフェには、それでも人が入っているな」
"1903" = "À, đúng thật. Quán cà phê của khách sạn vẫn có người vào mà."
# JP: 「っ！！！？」
"1909" = "「Ư!!!?」"
# JP: 「うん！　だってねぇねに」
"1938" = "Vâng! Tại vì là cho chị hai…"
# JP: 「えへへー」
"1956" = "Hì hì~"
# JP: 「だって！　いっとう最初は\\nカフェもキッチンも計画なかったけん」
"1970" = "Tại vì! Ban đầu hoàn toàn không có kế hoạch làm quán cà phê hay nhà bếp mà."
# JP: 「そうだ！　みだしなみ！　きれいくしないと！\\nせっかくにぃにが、おきゃくさんやけん！！」
"2011" = "Đúng rồi! Phải ăn mặc cho chỉnh tề! Phải làm cho thật đẹp mới được! Hiếm khi anh hai làm khách thế này!!"
# JP: 「あとは、にぃにを　まてばよかとねー。\\nえ？　なぁに？　くまくま？」
"2093" = "Sau đó, chỉ cần đợi anh hai đến là được nhỉ. Hả? Gì vậy? Kumakuma?"
# JP: 「ひびきちゃん……えへへ～！　とってもよかと！\\nウェイトレスさん、におーとるばい！！」
"2101" = "Hibiki-chan……hì hì~! Hợp lắm luôn! Trông đúng là cô bồi bàn rồi!!"
# JP: 「日々姫？　僕だ。入ってもいいのか？」
"2106" = "Hibiki? Anh đây. Anh vào được không?"
# JP: 「はぁい、そおですよぉ。ベージュが普通のプリンで、\\n柿色のとこはイチゴ味ってききましたぁ」
"2125" = "Vâng, đúng rồi nha. Màu be là bánh flan bình thường, còn phần màu vàng cam là vị dâu tây đó ạ."
# JP: 「おさら、よかと。クッキー、よかと」
"2191" = "Đĩa, xong rồi. Bánh quy, xong rồi."
# JP: 「ひょっとして――ベージュと柿色。\\n\x%lキハ07s;#00ffc040;キハ07s%l;#;の二色の塗り分けに、ですか？」
"2219" = "Có khi nào là——màu be và màu vàng cam. Được sơn thành hai màu của \\x%lキハ07s;#00ffc040;Kiha 07S%l;#; sao ạ?"
# JP: 「ねぇねぇの ゆってくれた とおりとー！\\nおあつらえしてもろーたみたいに、ぴったりばい！」
"2240" = "Đúng như chị hai đã nói luôn! Như thể được đặt làm riêng cho em vậy, vừa khít luôn!"
# JP: 「ここば、噂の喫茶店？\\nんー、雰囲気よさそうなお店やねぇ」
"2261" = "Đây là quán cà phê trong lời đồn sao? Hừm, quán có vẻ có bầu không khí tốt nhỉ."
# JP: 「なら、もう１５分。\\nうふふ、おねえちゃんも臨時休憩」
"2273" = "Vậy thì, 15 phút nữa. Ufufu, chị cũng tạm thời nghỉ ngơi một chút."
# JP: 「にぃに！　あ、じゃなくて、ええとね！\\n『いらっしゃいませー！』」
"2303" = "「Anh hai! A, không phải, ừm nè! 『Kính chào quý khách—!』」"
# JP: 「ひとりでお湯ばわかしたらダメって、ねぇねぇに\\nいわれてるし……ううう……早くきてほしかとよぉ」
"2305" = "Chị hai đã dặn là không được tự mình đun nước sôi……ư ư ư……mong anh mau đến quá."
# JP: でも……うーん、ちょっとにぃにぃおそくない？\\nまほうびんのお湯、さめちゃうかも。
"2461" = "Nhưng mà……ừm, anh hai có hơi đến muộn không nhỉ? Nước nóng trong bình giữ nhiệt có khi nguội mất."
# JP: おきゃくさん……でも、\\nだれもこないと、さみしすぎってこわかったけど。
"2464" = "Khách hàng……nhưng mà, nếu không có ai đến thì buồn lắm, mình đã sợ như thế."
# JP: ばってん、かがみん前まで走らんでよか。\\nだって、わたしには　こいばあるけん。
"2469" = "Nhưng mà, mình không cần phải chạy đến trước gương đâu. Vì mình đã có cái này rồi."
# JP: 本当は、テーブルと おいすが よかばってん、\\nうちにはなかけん、しかたなかとよ。
"2480" = "Thực ra, có bàn với ghế thì tốt thật đấy, nhưng nhà mình không có, nên cũng đành chịu thôi."
# JP: あかいじんじゃさんのお祭りで、\\nこども会のみんなでだした、おみせやさん。
"2505" = "Ở lễ hội đền Akai, bọn trẻ trong hội thiếu nhi đã cùng nhau mở một gian hàng."
# JP: くつろげるカフェを選ぶなら、\\n選択基準の一番最初に来るのは、やはり――
"2527" = "Nếu phải chọn một quán cà phê để thư giãn, thì tiêu chí lựa chọn đầu tiên, quả nhiên là——"
# JP: やけん、ウェイトレスさん　してみたくって、\\nきっさてんば、じぶんでひらいてみたくって。
"2603" = "Nên mình muốn thử làm cô bồi bàn, muốn thử tự mình mở một quán cà phê."
# JP: 『そうてつくんは　やさしいよね』って、\\nくまくまもゆーてくれてる！
"2665" = "『Anh Soutetsu hiền lành nhỉ』, Kumakuma cũng nói với mình như thế đó!"
# JP: ざたくのむかいのざぶとんの上、\\nくまくまが『できたね！』ってにこにこしとる。
"2668" = "Trên tấm đệm ngồi đối diện bàn thấp, Kumakuma cười tươi nói 『Làm được rồi nhỉ!』."
# JP: くまくまの目、なにか言っとー\\n『ひびきちゃんの　みだしなみは？』って――！
"2670" = "Đôi mắt Kumakuma, dường như đang muốn nói gì đó——『Trang phục của Hibiki-chan thì sao?』——!"
# JP: 帰りにバザーで　かってもらったこんふくば、\\nわたしには かわゆかすぎかもって思うとったけど。
"2746" = "Bộ đồ được mua cho mình ở hội chợ trên đường về, mình đã nghĩ có lẽ nó hơi dễ thương quá so với mình."
# JP: ふすまばあけて、にいにがはいってくる。
"2763" = "Mở cửa kéo ra, anh hai bước vào."
# JP: ねぇねぇにもらったコンパクト！\\nおもちゃのじゃなか、おねーさんば使うやつ！
"2781" = "Hộp phấn mà chị hai tặng mình! Không phải đồ chơi đâu, là loại mà các chị hay dùng đó!"
```

## Kết bài

File 日々姫04_カフェキッチン: 406 dòng đã đọc, 42 dòng sai (10,3%). Nặng nhất là nhiễm chéo tư liệu Mikuro/D51 (15 dòng) và 9 dòng lệch rời rạc — trong đó có key 2480 đã xác nhận lệch như flag trước đó. Còn lại là 6 tiếng cười うふふ bị dịch thành tiếng rên, 2 tiếng thở っ bị mất (theo sweep), 2 đại từ Soutetsu, 5 lần カフェ/喫茶店 dịch thành 'quán giải khát', 2 lần màu 柿色 dịch sai. Không có rotation chain trong file, không có dòng chưa dịch hay key trùng. Hai điểm chờ Hieu: phần hoàn thiện câu cụt ở 1938 (TW: tự tay pha trà chanh cho chị hai) và màu 柿色 (TW: nâu đỏ).
