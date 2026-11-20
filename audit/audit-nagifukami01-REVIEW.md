# Audit — 凪ふかみ01_凪の成長、ふかみの成長.txt.toml

- File: `凪ふかみ01_凪の成長、ふかみの成長.txt.toml` — route 07_Nagi_Fukami, 347 dòng script (78 thoại Nagi, 64 thoại Soutetsu, 49 thoại Fukami, 20 thoại Hachiroku, 8 thoại Paulette, 4 thoại Reina, 124 độc thoại Nagi).
- Nội dung: Nagi xin dự Đại hội Rèn luyện kiếm đạo (錬成大会) — Hachiroku kiểm tra kỹ thuật xúc than của Nagi trên 8620; Fukami đợi ở ga với lời nhắn của sư phụ Nagi; cả nhóm bàn về triết lý đầu máy của Minh Quốc (tuổi thọ 10 năm, sản xuất hàng loạt, giữ lại cá thể tốt) đối lập với Hinomoto/Đức (30–100 năm); Soutetsu chạy đi xin chữ ký hiệu trưởng và ông Minokasa để kịp nộp đơn; cuối file sư phụ cho phép Nagi dự giải. Không có H-scene.
- **Kết quả: 33/347 dòng sai (9,5%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. Bằng chứng: không có giá trị VN nào lặp lại ở 2 key (quét toàn file); mọi VN đều khớp nghĩa JP của chính key đó; CSV3 1 set duy nhất (347 dòng, 0 khóa trùng, 0 ô VN trống, 0 dòng VN == TW).
- VN khớp TOML tuyệt đối 347/347 key (0 lệch thực chất — 208 dòng chỉ khác ở chỗ TOML-2 làm phẳng dấu `\n` thành khoảng trắng, đã biết, không phải lỗi). `[selections]` rỗng (0 mục). Số thẻ `%l` JP vs VN bằng nhau ở mọi dòng (0 lệch); không có thẻ VN tự thêm, không có thẻ sai định dạng.
- TOML md5 `e6e70075e3d125fe3c9b1191aebf5104`; không có bản sao file này (md5 duy nhất trong toàn bộ 227 file — không thuộc 11 nhóm trùng).
- Đại từ: Soutetsu \"anh\" với Nagi/Fukami/Paulette/Reina đúng toàn file; \"tôi\" chỉ 2 dòng, cả 2 đều nói với Hachiroku (1776, 1964 — đúng quy tắc). Soutetsu gọi Nagi/Fukami là \"em\" đúng. Nagi gọi Fukami \"cậu\" (7 lần: 1688, 1739, 1741, 1744, 1757, 1874, 1930 — dạng ngang hàng, đúng); không có \"chị\" cho Fukami ở đâu. Fukami tự xưng \"tớ\" với Nagi, \"em\" với Soutetsu — đúng. Độc thoại Nagi dùng \"mình\" ~15 lần, chỉ 6 dòng lạc sang \"em\" (đã sửa, §2).
- Thuật ngữ: 湯医→\"Yunoi\" 3/3 đúng; 帝鉄→\"Teitetsu\" 1/1 đúng; エアクラ→\"Aircra\" 2/2 đúng; 投炭→\"xúc than dồn toa\" 13/13 nhất quán; 機関士→\"lái tàu\" 10/10; 御一夜 1 dòng \"Ohimitera\" (đã sửa 1968); 冥国 14 dòng (13 \"Mỹ\" đã sửa, 1 \"Minh Quốc\" 2394 đúng sẵn); 日ノ本→\"Hinomoto\" 9 dòng — chờ Hieu chốt \"Hinomoto\" vs \"Hinamoto\", không tính sai (§5).

## §2. Danh sách sửa (33 dòng)

Phân loại: terminology 22 (冥国→"Minh Quốc" 13 dòng: 1511, 1587, 1593, 1664, 1698, 1708, 1777, 1792, 1796, 1914, 1950, 1955, 1965; 凪さま→"Bổn tiểu thư" 8 dòng: 1485, 1571, 1685, 1708, 1839, 1886, 2347, 2452 — 1708/2452 mang 2 lỗi; 御一夜→"Ohitoyo" 1: 1968; "Kiha 07S"→"KiHa 07S" 2: 1673, 1688), pronoun 6 (độc thoại Nagi "em"→"mình": 2155, 2216, 2227, 2288, 2389, 2431), gasp 2 (1620, 2452 — cả 2 từ sweep, đã kiểm chứng), mistranslation 2 (1630 "Tin diu?"→"Tin vui?", 1979 "Dòng lọi"→"Vòng loại"), sfx 1 (1589 ふぁっ "Oa."→"Phà.").

### 1485 — Nagi — terminology
- JP: 「代わらんでよか！　凪さまひとりでやれると！！」
- TW: 「不必了！本小姐一個人可以！！」
- VN cũ: 「Không cần đổi đâu á! Nagi-sama một mình làm được á!!」
- Sửa: 「Không cần đổi đâu á! Bổn tiểu thư một mình làm được á!!」
- Lý do: JP 凪さま, TW 本小姐: Nagi tự xưng → "Bổn tiểu thư" (tiền lệ P01 1683, file JK 9/9 đã parent-verified). VN cũ "Nagi-sama" giữ tên riêng.

### 1511 — Hachiroku — terminology
- JP: 「『10年後には新技術・新素材でより優れた物を作れる』。\nそれゆえ、冥国の方は長く使うことを好まない、と」
- TW: 「他們認為十年後的新技術、新材料可以製造出更棒的產品。因此美國人不喜歡把服役年限拉得太長」
- VN cũ: 「『10 năm sau có thể tạo ra những thứ tốt hơn bằng công nghệ và vật liệu mới』.\nVì vậy, người Mỹ không thích sử dụng một món đồ quá lâu ạ.」
- Sửa: 「『10 năm sau có thể tạo ra những thứ tốt hơn bằng công nghệ và vật liệu mới』.\nVì vậy, người Minh Quốc không thích sử dụng một món đồ quá lâu ạ.」
- Lý do: JP 冥国の方, TW 美國人: thuật ngữ đã chốt 19/11 → "Minh Quốc" (tiền lệ 日々姫08 2585/3038, ハチロク06 1851/2023/2575). File này còn 1 dòng đã đúng sẵn (2394 "Minh Quốc") nên 13 dòng "Mỹ" là không nhất quán nội bộ.

### 1571 — Nagi — terminology
- JP: 「お師匠さんが許可くれなかっただけばい！\n凪さまなら、全国優勝も夢じゃなかとよー！」
- TW: 「只是師父一直不准咱參加而已！以本小姐的實力甚至可以奪得全國總冠軍！」
- VN cũ: 「Chỉ là sư phụ không cho phép thôi!\nVới Nagi-sama thì vô địch toàn quốc cũng không phải là giấc mơ đâu nha!」
- Sửa: 「Chỉ là sư phụ không cho phép thôi!\nVới Bổn tiểu thư thì vô địch toàn quốc cũng không phải là giấc mơ đâu nha!」
- Lý do: JP 凪さまなら, TW 本小姐: như 1485 — Nagi tự xưng → "Bổn tiểu thư".

### 1587 — Nagi — terminology
- JP: 「確か、蒸気機関車って、日ノ本よりずうっと前から、\n[えいこく,1]詠国やら[めいこく,1]冥国やら[どっこく,1]髑国にはあったんでしょお？」
- TW: 「咱記得英國、美國、德國早就有蒸汽機車了，應該比日本還要早得多吧？」
- VN cũ: 「Em nhớ là, đầu máy hơi nước đã có ở Anh, Mỹ và Đức\ntừ rất lâu trước cả Hinomoto rồi phải không?」
- Sửa: 「Em nhớ là, đầu máy hơi nước đã có ở Anh, Minh Quốc và Đức\ntừ rất lâu trước cả Hinomoto rồi phải không?」
- Lý do: JP [えいこく]詠国・[めいこく]冥国・[どっこく]髑国, TW 英國、美國、德國: chỉ 冥国 đổi theo quyết định 19/11 → "Minh Quốc"; 詠国→"Anh", 髑国→"Đức" giữ nguyên theo quy ước thế giới hư cấu (tiền lệ Paulette file).

### 1589 — Nagi — sfx
- JP: 「ふぁっ」
- TW: 「哇」
- VN cũ: 「Oa.」
- Sửa: 「Phà.」
- Lý do: JP ふぁっ: ふぁ→"phà" theo quy tắc fa/fu đã chốt (tiền lệ file 日々姫11: ふぁ "Oa"→"Phà"). VN cũ "Oa." làm mất âm ph.

### 1593 — Hachiroku — terminology
- JP: 「うふふ、確かに。\n冥国式は、凪と相性がよさそうですね」
- TW: 「哈哈，確實，感覺美國人的做法挺適合凪的」
- VN cũ: 「Fufufu, đúng thật.\nPhong cách của Mỹ có vẻ rất hợp với Nagi nhỉ.」
- Sửa: 「Fufufu, đúng thật.\nPhong cách của Minh Quốc có vẻ rất hợp với Nagi nhỉ.」
- Lý do: JP 冥国式, TW 美國式: → "Minh Quốc" như 1511 (tiền lệ 仲国01: 冥国式→"kiểu Minh Quốc").

### 1620 — Nagi — gasp
- JP: 「っ！！！」
- TW: 「啊！！！」
- VN cũ: 「っ!!!」
- Sửa: 「Ư!!!」
- Lý do: Sweep raw-tsu: っ trần còn sót trong VN → "Ư" (tiền lệ Hachiroku 12 2103/2537). Đã kiểm chứng khớp sweep.

### 1630 — Nagi — mistranslation
- JP: 「ろーほー？」
- TW: 「喜訊？」
- VN cũ: 「Tin diu?」
- Sửa: 「Tin vui?」
- Lý do: JP ろーほー = 朗報 (tin vui), TW 喜訊. VN cũ "Tin diu?" vô nghĩa — lỗi đánh máy/bịa của Gemini (cùng file 2281 dịch đúng ろーほー là "tin vui").

### 1664 — Soutetsu — terminology
- JP: 「ああ！　そうか、仕様は日ノ本側でオーダーだものな。\nそうなれば、日ノ本コンセプトで冥国の工業力を使える」
- TW: 「噢！明白了，技術規範是依照日本要求的。這樣一來，就是按照日本的理念運用美國的工業技術」
- VN cũ: 「A! Đúng rồi, thông số kỹ thuật là do phía Hinomoto đặt hàng mà.\nNếu vậy, chúng ta có thể sử dụng sức mạnh công nghiệp của Mỹ theo ý tưởng của Hinomoto.」
- Sửa: 「A! Đúng rồi, thông số kỹ thuật là do phía Hinomoto đặt hàng mà.\nNếu vậy, chúng ta có thể sử dụng sức mạnh công nghiệp của Minh Quốc theo ý tưởng của Hinomoto.」
- Lý do: JP 冥国の工業力, TW 美國的工業技術: → "Minh Quốc" như 1511.

### 1673 — Fukami — terminology
- JP: 「\x%lキハ07s;#00ffc040;キハ07s%l;#;の中で。\n山に修行にいくとかいってた」
- TW: 「在\x%lキハ07s;#00ffc040;Ｋｉｈａ０７Ｓ%l;#;上。她說要去山裡修行」
- VN cũ: 「Ở trên \x%lキハ07s;#00ffc040;Kiha 07S%l;#;.\nCô ấy nói là đi lên núi tu luyện hay gì đó.」
- Sửa: 「Ở trên \x%lキハ07s;#00ffc040;KiHa 07S%l;#;.\nCô ấy nói là đi lên núi tu luyện hay gì đó.」
- Lý do: Gloss thẻ %l "Kiha 07S" → "KiHa 07S" (cách viết chính thức của JR, đã chốt; tiền lệ 日々姫09 3167/3276). Chỉ đổi gloss, thẻ %l và term JP giữ nguyên.

### 1685 — Nagi — terminology
- JP: 「にーさんの、最高っ！\n凪さまがっ――ささえて――あげるけんっ！　ねっ！！」
- TW: 「大哥哥，你的盡善盡美！本小姐——會——全力幫忙！實現的！！」
- VN cũ: 「Tuyệt đỉnh của anh hai!\nNagi-sama sẽ——hỗ trợ——cho á! Nhé!!」
- Sửa: 「Tuyệt đỉnh của anh hai!\nBổn tiểu thư sẽ——hỗ trợ——cho á! Nhé!!」
- Lý do: JP 凪さまがっ, TW 本小姐: như 1485 — Nagi tự xưng → "Bổn tiểu thư".

### 1688 — Nagi — terminology
- JP: 「よかことばい！\nそいで、朝イチの\x%lキハ07s;#00ffc040;キハ07s%l;#;で来たと？」
- TW: 「太好咧！那麼你是坐早上第一班\x%lキハ07s;#00ffc040;Ｋｉｈａ０７Ｓ%l;#;來的？」
- VN cũ: 「Tuyệt quá! \nVậy cậu đến đây bằng chuyến \x%lキハ07s;#00ffc040;Kiha 07S%l;#; đầu tiên vào buổi sáng hả?」
- Sửa: 「Tuyệt quá! \nVậy cậu đến đây bằng chuyến \x%lキハ07s;#00ffc040;KiHa 07S%l;#; đầu tiên vào buổi sáng hả?」
- Lý do: Như 1673: gloss thẻ %l "Kiha 07S" → "KiHa 07S".

### 1698 — Hachiroku — terminology
- JP: 「[めいこく,1]冥国では、物に対する考え方がまるで違うと。\n日ノ本や[どっこく,1]髑国では、三十年先の運用のことも考えますが」
- TW: 「她說美國人的思維方式不一樣。日本和德國往往會考慮能夠讓產品保持三十年以上的使用年限」
- VN cũ: 「Ở Mỹ, cách suy nghĩ về đồ vật hoàn toàn khác biệt ạ.\nỞ Hinomoto hay Đức, người ta thường tính đến việc sử dụng trong 30 năm tới,」
- Sửa: 「Ở Minh Quốc, cách suy nghĩ về đồ vật hoàn toàn khác biệt ạ.\nỞ Hinomoto hay Đức, người ta thường tính đến việc sử dụng trong 30 năm tới,」
- Lý do: JP [めいこく]冥国では, TW 美國人: → "Ở Minh Quốc" như 1511.

### 1708 — Nagi — terminology
- JP: 「かっこよかばい！　ハイテクばい！！\n凪さま、冥国の考え方気にいったばい！！」
- TW: 「好帥！高科技咧！！本小姐喜歡美國人的思維方式！！」
- VN cũ: 「Ngầu quá đi! Công nghệ cao nha!!\nNagi-sama thích cách suy nghĩ của nước Mỹ rồi đó!!」
- Sửa: 「Ngầu quá đi! Công nghệ cao nha!!\nBổn tiểu thư thích cách suy nghĩ của nước Minh Quốc rồi đó!!」
- Lý do: Hai lỗi một dòng: 凪さま → "Bổn tiểu thư" (TW 本小姐) + 冥国の考え方 → "của nước Minh Quốc" (như 1511).

### 1777 — Hachiroku — terminology
- JP: 「その考え方が妥当でしょうね。\nわたくしの聞く冥国は、そのような国と思われます」
- TW: 「應該和你說的差不多。就我道聽途說的印象，美國應該就是這樣一個國家」
- VN cũ: 「Cách suy nghĩ đó khá hợp lý đấy.\nNước Mỹ mà tôi nghe kể, có vẻ đúng là một quốc gia như vậy.」
- Sửa: 「Cách suy nghĩ đó khá hợp lý đấy.\nNước Minh Quốc mà tôi nghe kể, có vẻ đúng là một quốc gia như vậy.」
- Lý do: JP 冥国, TW 美國: → "Nước Minh Quốc" như 1511.

### 1792 — Nagi — terminology
- JP: 「やけん、冥国には、\n蒸気機関車ばもう残っとらんのかも知れんの？？」
- TW: 「所以，美國可能已經沒有蒸汽機車了嗎？？」
- VN cũ: 「Vậy là, ở Mỹ,\ncó khi không còn lại đầu máy hơi nước nào nữa sao??」
- Sửa: 「Vậy là, ở Minh Quốc,\ncó khi không còn lại đầu máy hơi nước nào nữa sao??」
- Lý do: JP 冥国には, TW 美國: → "ở Minh Quốc" như 1511.

### 1796 — Hachiroku — terminology
- JP: 「すばらしい考察です。凪。\n冥国式の考え方は、本当に凪には馴染むようですね」
- TW: 「推理得很棒，凪。看來美國式的思維方式確實很適合你」
- VN cũ: 「Suy luận tuyệt vời lắm, Nagi.\nCách suy nghĩ kiểu Mỹ, có vẻ thực sự rất hợp với em nhỉ.」
- Sửa: 「Suy luận tuyệt vời lắm, Nagi.\nCách suy nghĩ kiểu Minh Quốc, có vẻ thực sự rất hợp với em nhỉ.」
- Lý do: JP 冥国式, TW 美國式: → "kiểu Minh Quốc" như 1593.

### 1839 — Nagi — terminology
- JP: 「凪さま――\n凪さま、機関士になれると！！？」
- TW: 「本小姐——本小姐能當司機！！？」
- VN cũ: 「Nagi-sama——\nNagi-sama, sắp được làm lái tàu rồi sao!!?」
- Sửa: 「Bổn tiểu thư——\nBổn tiểu thư, sắp được làm lái tàu rồi sao!!?」
- Lý do: JP 凪さま ×2, TW 本小姐 ×2: như 1485 — cả hai lần → "Bổn tiểu thư".

### 1886 — Nagi — terminology
- JP: 「もーにーさんより凪さまの方が、\n投炭！　うまかけんね！！」
- TW: 「現在本小姐加煤比大哥哥更熟練！！」
- VN cũ: 「Bây giờ Nagi-sama xúc than dồn toa!\nCòn giỏi hơn cả anh hai nữa á!!」
- Sửa: 「Bây giờ Bổn tiểu thư xúc than dồn toa!\nCòn giỏi hơn cả anh hai nữa á!!」
- Lý do: JP 凪さま, TW 本小姐: như 1485 — Nagi tự xưng → "Bổn tiểu thư".

### 1914 — Hachiroku — terminology
- JP: 「冥国では、一〇年の耐用で充分と考えるそうです」
- TW: 「而美國人覺得服役年限有十年就夠了」
- VN cũ: 「Còn ở Mỹ, họ cho rằng tuổi thọ 10 năm là đủ rồi ạ.」
- Sửa: 「Còn ở Minh Quốc, họ cho rằng tuổi thọ 10 năm là đủ rồi ạ.」
- Lý do: JP 冥国では, TW 美國人: → "Còn ở Minh Quốc" như 1511.

### 1950 — Soutetsu — terminology
- JP: 「その辺の事情は……どうなのかな。\n冥国はエアクラ発祥の地でもあるし――ハチロク？」
- TW: 「這個……就很難說了。空凝機也是發源於美國的……八六你知道嗎？」
- VN cũ: 「Tình hình bên đó thì……thế nào nhỉ.\nMỹ cũng là nơi khởi nguồn của Aircra mà——Hachiroku?」
- Sửa: 「Tình hình bên đó thì……thế nào nhỉ.\nMinh Quốc cũng là nơi khởi nguồn của Aircra mà——Hachiroku?」
- Lý do: JP 冥国はエアクラ発祥の地, TW 空凝機發源於美國: → "Minh Quốc" như 1511.

### 1955 — Soutetsu — terminology
- JP: 「冥国式に作られた車両は、海外には売れん気がする。\nが、実際、日ノ本にも冥国出身の輸入\x%l蒸機;#00ffc040;蒸機%l;#;は多いよな？」
- TW: 「這樣的話，感覺美國造的車輛沒辦法出口海外啊。可是日本的確有很多從美國進口的\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;」
- VN cũ: 「Anh cảm giác những toa xe được chế tạo theo kiểu Mỹ sẽ không bán được ra nước ngoài.\nNhưng thực tế, ở Hinomoto cũng có rất nhiều \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; nhập khẩu từ Mỹ đúng không?」
- Sửa: 「Anh cảm giác những toa xe được chế tạo theo kiểu Minh Quốc sẽ không bán được ra nước ngoài.\nNhưng thực tế, ở Hinomoto cũng có rất nhiều \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; nhập khẩu từ Minh Quốc đúng không?」
- Lý do: JP 冥国式 + 冥国出身, TW 美國造 + 從美國進口: cả hai → "Minh Quốc" như 1511.

### 1965 — Nagi — terminology
- JP: 「やったら、冥国には日ノ本よりずうっとたくさん、\n蒸気機関車があるんじゃなかと？」
- TW: 「那麼，美國那邊的蒸汽機車應該比日本多很多吧？」
- VN cũ: 「Vậy thì, ở Mỹ chắc chắn phải có nhiều đầu máy hơi nước\nhơn Hinomoto rất nhiều đúng không?」
- Sửa: 「Vậy thì, ở Minh Quốc chắc chắn phải có nhiều đầu máy hơi nước\nhơn Hinomoto rất nhiều đúng không?」
- Lý do: JP 冥国には, TW 美國: → "ở Minh Quốc" như 1511.

### 1968 — Fukami — terminology
- JP: 「[このこ,3]8620の……バーベキュー列車のおかげ。\n御一夜が元気を取り戻せたの、本当に」
- TW: 「都要感謝８６２０……感謝ＢＢＱ列車。御一夜終於真正恢復了活力」
- VN cũ: 「Nhờ có 8620……và đoàn tàu BBQ.\nOhimitera đã thực sự lấy lại được sức sống rồi.」
- Sửa: 「Nhờ có 8620……và đoàn tàu BBQ.\nOhitoyo đã thực sự lấy lại được sức sống rồi.」
- Lý do: JP 御一夜 → "Ohitoyo" (quyết định 19/11). VN cũ "Ohimitera" là dạng cũ.

### 1979 — Nagi — mistranslation
- JP: 「よせん……って――何の予選ばい？？？」
- TW: 「預賽……什麼預賽？？？」
- VN cũ: 「Dòng lọi……là sao——Vòng loại gì cơ???」
- Sửa: 「Vòng loại……là sao——Vòng loại gì cơ???」
- Lý do: JP よせん = 予選 (vòng loại), TW 預賽. VN cũ "Dòng lọi" vô nghĩa — lỗi đánh máy (d/v) của "Vòng loại" (Nagi lặp lại từ vừa nghe).

### 2155 — Độc thoại (Nagi) — pronoun
- JP: 2分で60。発車直後のいつものペースで、\nきっちり投炭しとるばってん――
- TW: 兩分鐘六十鏟。雖然咱在發車後按照平時的節奏，加了足夠的煤炭……
- VN cũ: 2 phút 60 xẻng. Với nhịp độ thường ngày ngay sau khi xuất phát,\nem đang xúc than dồn toa rất chuẩn xác nhưng——
- Sửa: 2 phút 60 xẻng. Với nhịp độ thường ngày ngay sau khi xuất phát,\nmình đang xúc than dồn toa rất chuẩn xác nhưng——
- Lý do: Độc thoại Nagi (CHAR monologue): tự xưng "em" không nhất quán với quy ước độc thoại của file ("mình" ~15 lần: 2138, 2201, 2219, 2223, 2235, 2237, 2309, 2315, 2320, 2331, 2337, 2355). Trong độc thoại không có người nghe để xưng "em". Sửa về "mình".

### 2216 — Độc thoại (Nagi) — pronoun
- JP: うちもあわせてワンスコ置いてブロアを開いて通風とって。\n水ばごくごく！　がんばっとったカマに飲ませてあげる。
- TW: 咱也放下公斤鍬打開風管通風。滾燙的窯咕嘟咕嘟地喝著水！
- VN cũ: Em cũng phối hợp bỏ xẻng xuống, mở thiết bị thổi gió để thông gió.\nNước ừng ực! Cho lò hơi nãy giờ đang cố gắng uống nước á.
- Sửa: Mình cũng phối hợp bỏ xẻng xuống, mở thiết bị thổi gió để thông gió.\nNước ừng ực! Cho lò hơi nãy giờ đang cố gắng uống nước á.
- Lý do: Như 2155: độc thoại Nagi tự xưng "Em" → "Mình".

### 2227 — Độc thoại (Nagi) — pronoun
- JP: わかっとるけん、余計に燃える。\n絶対、合格するって思う。
- TW: 咱明白，而且這樣更讓人興奮。會讓咱下定決心，一定要通過考試。
- VN cũ: Em biết mà, thế nên lại càng hừng hực khí thế hơn.\nEm nhất định sẽ thi đậu.
- Sửa: Mình biết mà, thế nên lại càng hừng hực khí thế hơn.\nMình nhất định sẽ thi đậu.
- Lý do: Như 2155: độc thoại Nagi tự xưng "Em" ×2 → "Mình" ×2.

### 2288 — Độc thoại (Nagi) — pronoun
- JP: ドキンって、胸ば跳ね上がる。\n信じて貰えて嬉しくなるけん！　元気出てくる！！
- TW: 害咱心裡小鹿亂撞的。他信任了咱！好開心！！
- VN cũ: Thình thịch, ngực em đập rộn ràng.\nĐược anh tin tưởng em vui lắm á! Cảm thấy tràn đầy năng lượng luôn!!
- Sửa: Thình thịch, ngực mình đập rộn ràng.\nĐược anh tin tưởng mình vui lắm á! Cảm thấy tràn đầy năng lượng luôn!!
- Lý do: Như 2155: độc thoại Nagi — "ngực em" + "em vui" → "ngực mình" + "mình vui".

### 2347 — Độc thoại (Nagi) — terminology
- JP: 凪さま、ううん、うち――わたし、も！
- TW: 本小姐——不對，咱——不是的，我也要！
- VN cũ: Nagi-sama, à không, mình——tớ, cũng vậy!
- Sửa: Bổn tiểu thư, à không, mình——tớ, cũng vậy!
- Lý do: JP 凪さま、ううん、うち――わたし、も！, TW 本小姐——不對，咱——不是的，我也要！: 凪さま → "Bổn tiểu thư" (như 1485); chuỗi tự sửa "mình——tớ" giữ nguyên theo TW.

### 2389 — Độc thoại (Nagi) — pronoun
- JP: そしたら、うちもゆるんじゃう。\nゆるんだら汗ば、ぶわあぁって出る。
- TW: 看著他這樣，咱也放鬆了下來。然後汗水就一下子湧出來了。
- VN cũ: Thế là, em cũng thư giãn theo á.\nThư giãn rồi thì mồ hôi, lại túa ra như tắm á.
- Sửa: Thế là, mình cũng thư giãn theo á.\nThư giãn rồi thì mồ hôi, lại túa ra như tắm á.
- Lý do: Như 2155: độc thoại Nagi tự xưng "em" → "mình".

### 2431 — Độc thoại (Nagi) — pronoun
- JP: この隙にウチも給水！\n水筒の水ばごっくごっく飲む。
- TW: 趁這個閒暇咱也要補充水分！於是咱打開水壺大口大口喝了起來。
- VN cũ: Tranh thủ lúc này em cũng tiếp nước!\nUống ừng ực nước trong bình á.
- Sửa: Tranh thủ lúc này mình cũng tiếp nước!\nUống ừng ực nước trong bình á.
- Lý do: Như 2155: độc thoại Nagi tự xưng "em" → "mình".

### 2452 — Độc thoại (Nagi) — gasp
- JP: 気分よかとー！\nなんだか凪さま、頭のよーなった気分――っ！！！
- TW: 開心！感覺本小姐變聰明了！！！
- VN cũ: Vui quá đi!\nCảm giác Nagi-sama tự nhiên thông minh hẳn ra——っ!!!
- Sửa: Vui quá đi!\nCảm giác Bổn tiểu thư tự nhiên thông minh hẳn ra——Ư!!!
- Lý do: Hai lỗi một dòng: sweep raw-tsu (——っ!!! → ——Ư!!!, đã kiểm chứng khớp sweep) + 凪さま → "Bổn tiểu thư" (TW 本小姐).

## §3. Đối chiếu sweep っ

- Sweep có đúng 2 mục cho file này (1620 raw-tsu, 2452 raw-tsu) — cả 2 đã áp nguyên sau khi kiểm chứng JP, không mục nào sai.
- Tự quét toàn bộ っ trong JP (mọi ngữ cảnh っ): không còn gasp nào sweep bỏ sót. Các っ còn lại đều đã được diễn đúng: 1582 ぷはぁっ→\"Phù!\", 1584 くはーーーーっ→\"Khàaaaa\", 1594 ひえっ→\"Hả\", 1595 ふえっ→\"Hả\", 1619 っ→\"A\", các っ nhấn mạnh cuối từ nội dung (1685, 1715, 1734, 1752, 1765, 1852, 1858, 2239, 2343) đã diễn bằng \"á\"/\"Nhé\"/\"luôn\", SFX trong ngoặc 2475–2488 đều có âm tương ứng.
- Fa/fu: chỉ 1 dòng ふぁっ (1589) — đã sửa theo quy tắc; các âm khác đúng sẵn: 1591 ふふっ→\"Fufu\" (cười), 1601 ふっ→\"Hứ\" (hừ đắc ý), 2159 ふふふ→\"Fufufu\", 2266 ふっ→\"Phụt\" (cười khẽ), 2301 ふって là phó từ \"chợt\" (không phải tiếng thở). 1595 ふえっ→\"Hả\" giữ (ふえ với え đầy, không thuộc quy tắc ふぇ; TW 哎); 1975 ふわぁ→\"Oa\" giữ (không phải ふぁ/ふあ; TW 哇).

## §4. Khối TOML (đã parse-kiểm chứng)

```toml
"1485" = "「Không cần đổi đâu á! Bổn tiểu thư một mình làm được á!!」"
"1511" = "「『10 năm sau có thể tạo ra những thứ tốt hơn bằng công nghệ và vật liệu mới』.\\nVì vậy, người Minh Quốc không thích sử dụng một món đồ quá lâu ạ.」"
"1571" = "「Chỉ là sư phụ không cho phép thôi!\\nVới Bổn tiểu thư thì vô địch toàn quốc cũng không phải là giấc mơ đâu nha!」"
"1587" = "「Em nhớ là, đầu máy hơi nước đã có ở Anh, Minh Quốc và Đức\\ntừ rất lâu trước cả Hinomoto rồi phải không?」"
"1589" = "「Phà.」"
"1593" = "「Fufufu, đúng thật.\\nPhong cách của Minh Quốc có vẻ rất hợp với Nagi nhỉ.」"
"1620" = "「Ư!!!」"
"1630" = "「Tin vui?」"
"1664" = "「A! Đúng rồi, thông số kỹ thuật là do phía Hinomoto đặt hàng mà.\\nNếu vậy, chúng ta có thể sử dụng sức mạnh công nghiệp của Minh Quốc theo ý tưởng của Hinomoto.」"
"1673" = "「Ở trên \\x%lキハ07s;#00ffc040;KiHa 07S%l;#;.\\nCô ấy nói là đi lên núi tu luyện hay gì đó.」"
"1685" = "「Tuyệt đỉnh của anh hai!\\nBổn tiểu thư sẽ——hỗ trợ——cho á! Nhé!!」"
"1688" = "「Tuyệt quá! \\nVậy cậu đến đây bằng chuyến \\x%lキハ07s;#00ffc040;KiHa 07S%l;#; đầu tiên vào buổi sáng hả?」"
"1698" = "「Ở Minh Quốc, cách suy nghĩ về đồ vật hoàn toàn khác biệt ạ.\\nỞ Hinomoto hay Đức, người ta thường tính đến việc sử dụng trong 30 năm tới,」"
"1708" = "「Ngầu quá đi! Công nghệ cao nha!!\\nBổn tiểu thư thích cách suy nghĩ của nước Minh Quốc rồi đó!!」"
"1777" = "「Cách suy nghĩ đó khá hợp lý đấy.\\nNước Minh Quốc mà tôi nghe kể, có vẻ đúng là một quốc gia như vậy.」"
"1792" = "「Vậy là, ở Minh Quốc,\\ncó khi không còn lại đầu máy hơi nước nào nữa sao??」"
"1796" = "「Suy luận tuyệt vời lắm, Nagi.\\nCách suy nghĩ kiểu Minh Quốc, có vẻ thực sự rất hợp với em nhỉ.」"
"1839" = "「Bổn tiểu thư——\\nBổn tiểu thư, sắp được làm lái tàu rồi sao!!?」"
"1886" = "「Bây giờ Bổn tiểu thư xúc than dồn toa!\\nCòn giỏi hơn cả anh hai nữa á!!」"
"1914" = "「Còn ở Minh Quốc, họ cho rằng tuổi thọ 10 năm là đủ rồi ạ.」"
"1950" = "「Tình hình bên đó thì……thế nào nhỉ.\\nMinh Quốc cũng là nơi khởi nguồn của Aircra mà——Hachiroku?」"
"1955" = "「Anh cảm giác những toa xe được chế tạo theo kiểu Minh Quốc sẽ không bán được ra nước ngoài.\\nNhưng thực tế, ở Hinomoto cũng có rất nhiều \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; nhập khẩu từ Minh Quốc đúng không?」"
"1965" = "「Vậy thì, ở Minh Quốc chắc chắn phải có nhiều đầu máy hơi nước\\nhơn Hinomoto rất nhiều đúng không?」"
"1968" = "「Nhờ có 8620……và đoàn tàu BBQ.\\nOhitoyo đã thực sự lấy lại được sức sống rồi.」"
"1979" = "「Vòng loại……là sao——Vòng loại gì cơ???」"
"2155" = "2 phút 60 xẻng. Với nhịp độ thường ngày ngay sau khi xuất phát,\\nmình đang xúc than dồn toa rất chuẩn xác nhưng——"
"2216" = "Mình cũng phối hợp bỏ xẻng xuống, mở thiết bị thổi gió để thông gió.\\nNước ừng ực! Cho lò hơi nãy giờ đang cố gắng uống nước á."
"2227" = "Mình biết mà, thế nên lại càng hừng hực khí thế hơn.\\nMình nhất định sẽ thi đậu."
"2288" = "Thình thịch, ngực mình đập rộn ràng.\\nĐược anh tin tưởng mình vui lắm á! Cảm thấy tràn đầy năng lượng luôn!!"
"2347" = "Bổn tiểu thư, à không, mình——tớ, cũng vậy!"
"2389" = "Thế là, mình cũng thư giãn theo á.\\nThư giãn rồi thì mồ hôi, lại túa ra như tắm á."
"2431" = "Tranh thủ lúc này mình cũng tiếp nước!\\nUống ừng ực nước trong bình á."
"2452" = "Vui quá đi!\\nCảm giác Bổn tiểu thư tự nhiên thông minh hẳn ra——Ư!!!"
```
Khối trên parse OK bằng tomllib: 33 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô).

## §5. Lượt soát 2 + Chờ Hieu

- Lượt soát 2: 33/33 fix đọc lại đối chiếu JP — 33 giữ nguyên, 0 bỏ, 0 sửa.
- Đã kiểm tra và không tính sai: 2188 シュッシュッ→\"xình xịch\" (tiếng xả hơi xi-lanh, chấp nhận được); 2476 ざくっ/がっ đều →\"Phập!\" (làm phẳng 2 âm khác nhau nhưng đủ 4 âm, giữ); 1701 \"Tụi em rõ rồi ạ\" (dạng nhóm Fukami+Nagi nói với Hachiroku, đúng); 1517 Nagi tự xưng \"em\" nói với Fukami (1 lần duy nhất; xem mục chờ Hieu số 4); 1858 \"Mở van tiết lưuuuuuuu!\" (kéo dài đặt ở \"lưu\", giữ — lựa chọn phong cách).
- Chờ Hieu (không tự quyết):
  1. 日ノ本 \"Hinomoto\" vs \"Hinamoto\" — 9 dòng trong file này (1209, 1585, 1587, 1664, 1698, 1795, 1816, 1955, 1965), giữ nguyên chờ chốt chung toàn dự án.
  2. Key 1884 — じーちゃん → \"Ông nội\" (ông nội của Nagi): câu hỏi \"ông nội\" vs \"ông ngoại\" toàn dự án (từ 凪ふかみ08c) vẫn chờ Hieu chốt, giữ nguyên.
  3. Key 1955 — Soutetsu tự xưng \"Anh cảm giác...\": người nghe mơ hồ (Hachiroku — chuyên gia đường sắt, vừa được hỏi ở 1950 — hay cả nhóm gồm Nagi/Fukami); nếu nói với Hachiroku thì phải là \"tôi\". Giữ nguyên, cần Hieu/Muse xác nhận người nghe.
  4. Key 1517 — Nagi tự xưng \"em\" nói với Fukami (\"Được khen như vậy, em ngại lắm đó nha!\"): bạn cùng tuổi, file này Nagi thường tự xưng \"tớ\"/\"mình\" với Fukami (1749, 1860, 1930); \"em\" ở đây có thể chỉ là biến thể tự nhiên. Giữ nguyên, Hieu quyết có thống nhất về \"tớ\"/\"mình\" hay không.
  5. Ghi chú về 冥国: một review file Paulette từng ghi quy ước thế giới hư cấu là \"冥国=Mỹ\"; nhưng quyết định 19/11 trong AUDIT-BRIEF.md là \"Minh Quốc\", các file đã parent-verified đều sửa về \"Minh Quốc\", và chính file này đã có sẵn 1 dòng \"Minh Quốc\" đúng (2394). Đã sửa theo brief; ghi lại mâu thuẫn để Hieu biết nếu muốn xem lại.

## Kết bài

File 凪ふかみ01_凪の成長、ふかみの成長 đã audit xong toàn bộ 347 dòng: 33 dòng sai (9,5%) — terminology 22 (冥国→\"Minh Quốc\" 13, 凪さま→\"Bổn tiểu thư\" 8, Ohimitera→Ohitoyo 1, \"Kiha 07S\"→\"KiHa 07S\" 2), pronoun 6 (độc thoại Nagi \"em\"→\"mình\"), gasp 2 (sweep), mistranslation 2 (\"Tin diu?\", \"Dòng lọi\"), sfx 1 (ふぁっ→\"Phà\"). Không lệch dòng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 33 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 33/33, 0 bỏ, 0 sửa. Chờ Hieu: 日ノ本 \"Hinomoto\" vs \"Hinamoto\" (9 dòng), 1884 \"Ông nội\", 1955 người nghe của Soutetsu, 1517 Nagi tự xưng \"em\" với Fukami.
