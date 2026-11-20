# Kiểm tra bản dịch — 05_Mayami lr真闇追加03: ブルートレインの夜

File: `lr真闇追加03_ブルートレインの夜.txt.toml` — route 05_Mayami, file thêm (追加) về đêm trên tàu giường nằm loại B: Soutetsu, Mayami và Reina tắm chung, kỳ lưng cho nhau, kể chuyện cũ (phòng của Hibiki, xưởng rượu, chuyến tàu cuối).
Đây là kiểm tra ĐẦY ĐỦ (full audit) — đọc toàn bộ 337 dòng script đối chiếu JP + TW.

## §1. Tổng quan

- Tổng số dòng script: **337** (monologue 108, hội thoại 229).
- Số dòng sai: **56/337 (16,6%)** — hội thoại 32/229 (14,0%), độc thoại 24/108 (22,2%).
- Phân loại: pronoun 48 (đối thoại với Mayami 24 + với Reina 1 + độc thoại 23), mistranslation 4, gasp 3, fa/fu 1.
- TOML md5: `0e396cf29d7c10c3c402f7122140d687` (bản duy nhất — không có file trùng; 11 nhóm trùng của dự án không chứa file này).
- CSV↔TOML: 112 dòng khớp tuyệt đối + 225 dòng chỉ khác ở chỗ TOML-2 làm phẳng ký tự `\n` thành khoảng trắng — **0 khác biệt thực chất**. CSV3 là bộ đơn (single-set), không có bộ đôi.
- Thẻ `%l`: JP 0, VN 0 — không có thẻ nào trong file.
- **Rotation: 0 chuỗi xoay** — không có dòng lệch hàng nào: 4 lỗi mistranslation đều là dịch sai tại chỗ (đọc sai phủ định, đọc sai te-form, bịa thêm), không có bản dịch đúng nằm ở key khác trong file. Đã kiểm tra trùng lặp VN: chỉ 2 cặp trùng (1120/1532 — đã hết trùng sau khi sửa 1120 thành 「Ư!」; 1365/1446 — cùng "Đúng vậy" cho 2 JP khác nhau, hợp lệ).
- **0 contamination** (chỉ mục VN toàn dự án: 0/56 bản cũ xuất hiện ở file khác) / **0 orphan** / **0 untranslated** (0 ô VN trống) / **0 duplicate key**.
- **0 dòng uncertain** (mọi phán đoán người nghe đều có bằng chứng từ dòng kề — xem ghi chú từng dòng).
- Ohitoyo trong file: 3 dòng còn dạng cũ "Ohimitera" (1044, 1381, 1768) — **không sửa trong audit này, để dành cho đợt thống nhất thuật ngữ** (chờ Hieu). "dồn toa": 1 dòng (1893, bỏ theo quyết định 1027 của Hieu 20/11) — còn 0.
- Sweep っ: file có 2 mục trong sweep-raw-gasp-wrong.json (1120, 1121) — cả 2 đều đúng, đã áp nguyên. Ngoài ra phát hiện thêm 1 gasp sweep bỏ sót: 905 (JP 「っ」 đứng một mình, VN chỉ còn "!").
- Strong candidates: 10 dòng (731, 1045, 1310, 1327, 1355, 1384, 1433, 1447, 1504, 1521) — chỉ **1/10 xác nhận sai (731)**; 9/10 còn lại đúng, đã đọc kỹ.

## §2. Bảng fix (56 dòng)

### 689 — 真闇 — dịch sai
- JP: 「――そぎゃんね。おねえちゃんも眩しいみたいに感じた。\nひーちゃんのこと、あの列車ばみて」
- TW: 「——是啊，我都覺得有些耀眼了。現在的小日看起來，就好像那個火車站一樣 」
- Cũ: 「——Đúng vậy nhỉ. Chị cũng cảm thấy chói lóa.\nHii-chan, nhìn chuyến tàu đó」
- Mới: 「——Đúng vậy nhỉ. Chị cũng cảm thấy chói lóa.\nNhìn Hii-chan, rồi nhìn chuyến tàu đó」
- Lý do: JP 「ひーちゃんのこと、あの列車ばみて」 là dạng te-form tiếp nối câu trước ("nhìn Hii-chan, nhìn chuyến tàu đó mà thấy chói lóa"), không phải câu mệnh lệnh. Bản cũ "Hii-chan, nhìn chuyến tàu đó" đọc như Mayami bảo Hii-chan nhìn tàu — sai hẳn.

### 717 — 双鉄 — đại từ xưng hô
- JP: 「……だろうな。\n日々姫の才は、そういう才だと僕も感じる」
- TW: 「……也是。我也覺得日日姬的才華確實出類拔萃」
- Cũ: 「……Chắc là vậy.\nTài năng của Hibiki, anh cũng cảm thấy đó là một tài năng như vậy」
- Mới: 「……Chắc là vậy.\nTài năng của Hibiki, tôi cũng cảm thấy đó là một tài năng như vậy」
- Lý do: Soutetsu nói với Mayami → tự xưng "tôi" theo quy tắc đã sửa ("tôi" với Mayami). Bản cũ "anh" sai.

### 731 — れいな — dịch sai
- JP: 「……もしもそうなら、そうだって、\nポーレットにもわかってもらえたらいいんですけど」
- TW: 「……雖然你們這麼說，但是，波萊特她可能並不這麼看啊」
- Cũ: "「……Nếu đúng là vậy, thì phải chi\nPaulette cũng hiểu được lòng Reina thì tốt biết mấy.」"
- Mới: "「……Nếu đúng là vậy, thì phải chi\nPaulette cũng hiểu được điều đó thì tốt biết mấy.」"
- Lý do: JP そうだって = "là như vậy" (điều vừa nói). Bản cũ thêm "lòng Reina" không có trong JP — bịa thêm nghĩa. TW cũng lệch ("Paulette có thể không nghĩ vậy"), lấy JP làm chuẩn.

### 905 — 双鉄 — mất tiếng gasp っ
- JP: 「っ」
- TW: 「っ」
- Cũ: "「!」"
- Mới: "「Ư」"
- Lý do: JP 「っ」 đứng một mình là tiếng hít hơi/gasp; bản cũ chỉ còn dấu "!" làm mất âm. Sweep không liệt kê dòng này (chỉ 1120/1121) — bổ sung theo quy tắc っ → Ư, không có dấu câu trong JP nên không thêm "!".

### 1043 — 双鉄 — đại từ xưng hô
- JP: 「張り切っていたし、はしゃいでもいたな。\n果たしてどんなガイドになるか、正直危ぶんでもいたが」
- TW: 「不僅幹勁十足，而且興奮無比。其實對她能成為一個怎樣的導遊，我原本還挺擔心的」
- Cũ: 「Đã căng sức, lại còn phấn khích nữa.\nNói thật là anh cũng từng lo không biết em ấy sẽ làm hướng dẫn viên thế nào」
- Mới: 「Đã căng sức, lại còn phấn khích nữa.\nNói thật là tôi cũng từng lo không biết em ấy sẽ làm hướng dẫn viên thế nào」
- Lý do: Soutetsu nói với Mayami → "tôi". Bản cũ "anh" sai.

### 1058 — 双鉄 — đại từ xưng hô
- JP: 「そうか、僕が――僕らが、\n僕らの家族を、僕らの家庭を育てていくのか」
- TW: 「也是，要由我——由我們，來經營這個小小的家庭啊」
- Cũ: "「Ra là vậy, em——chúng ta,\nsẽ nuôi dưỡng gia đình của chúng ta, tổ ấm của chúng ta sao.」"
- Mới: "「Ra là vậy, tôi——chúng ta,\nsẽ nuôi dưỡng gia đình của chúng ta, tổ ấm của chúng ta sao.」"
- Lý do: Soutetsu nói với Mayami → "tôi". Bản cũ "em" sai.

### 1064 — 双鉄 — đại từ xưng hô
- JP: 「なんと。ぜひとも見てみたかったな」
- TW: 「什麼，這可一定得讓我看看啊」
- Cũ: 「Trời ạ. Nhất định anh phải xem mới được」
- Mới: 「Trời ạ. Nhất định tôi phải xem mới được」
- Lý do: Soutetsu nói với Mayami → "tôi". Bản cũ "anh" sai.

### 1114 — 双鉄 — đại từ xưng hô
- JP: 「願わくば、僕の旅路の最後まで。\n真闇姉――一緒に旅をしてほしい」
- TW: 「只願，直到我旅途的終點，還能有你的陪伴」
- Cũ: "「Chỉ mong rằng, cho đến tận cuối hành trình của em.\nChị Mayami——hãy cùng em đi hết chuyến đi này.」"
- Mới: "「Chỉ mong rằng, cho đến tận cuối hành trình của tôi.\nChị Mayami——hãy cùng tôi đi hết chuyến đi này.」"
- Lý do: Soutetsu nói với Mayami → "tôi" (2 chỗ). Bản cũ "em" sai.

### 1120 — 真闇 — mất tiếng gasp っ
- JP: 「っ！」
- TW: 「呃！」
- Cũ: 「!」
- Mới: 「Ư!」
- Lý do: Sweep lost-gasp-whole: JP 「っ！", TW 「呃！", bản cũ chỉ còn "!". Áp nguyên fix của sweep, đã kiểm chứng vs JP.

### 1121 — 双鉄 — mất tiếng gasp っ
- JP: 「っ！！！！」
- TW: 「呃！！！！」
- Cũ: 「!!!!」
- Mới: 「Ư!!!!」
- Lý do: Sweep lost-gasp-whole: JP 「っ！！！！", TW 「呃！！！！", bản cũ chỉ còn "!!!!". Áp nguyên fix của sweep, đã kiểm chứng vs JP.

### 1135 — 双鉄 — đại từ xưng hô
- JP: 「少しずつ少しずつ家族になって。\nその幸せな日々の中から、さらに大きな幸せを得た」
- TW: 「和大家一點點成為家人，在這幸福的每一天裡，我獲得了更大的幸福」
- Cũ: "「Từng chút, từng chút một trở thành gia đình.\nTừ trong những tháng ngày hạnh phúc đó, em lại có được một hạnh phúc to lớn hơn nữa.」"
- Mới: "「Từng chút, từng chút một trở thành gia đình.\nTừ trong những tháng ngày hạnh phúc đó, tôi lại có được một hạnh phúc to lớn hơn nữa.」"
- Lý do: Soutetsu nói với Mayami (Reina đang ngủ ở 1133) → "tôi". Bản cũ "em" sai.

### 1204 — 双鉄 — đại từ xưng hô
- JP: 「うむ？　僕もか」
- TW: 「嗯？我也來？」
- Cũ: "「Hửm? Cả em nữa à?」"
- Mới: "「Hửm? Cả tôi nữa à?」"
- Lý do: Soutetsu đáp lời mời "洗いっこ" của Mayami ở 1146 ("Sou-chan thì sao? Có muốn kỳ cọ cho nhau không?") → người nghe là Mayami → "tôi". Bản cũ "em" sai.

### 1228 — 双鉄 — đại từ xưng hô
- JP: 「あどけないと言いたくなるほどはしゃいでいたな。\nれいなも、真闇姉と――僕らと遊んでいたのかもだな」
- TW: 「她今天吵鬧得也太孩子氣了。可能玲奈她自己也一直想和真闇姐——也想和我們一起玩吧」
- Cũ: "「Nhí nhảnh đến mức em muốn dùng từ ngây thơ để miêu tả luôn.\nCó lẽ Reina cũng đã chơi đùa cùng chị Mayami——cùng chúng ta đấy.」"
- Mới: "「Nhí nhảnh đến mức tôi muốn dùng từ ngây thơ để miêu tả luôn.\nCó lẽ Reina cũng đã chơi đùa cùng chị Mayami——cùng chúng ta đấy.」"
- Lý do: Soutetsu kể với Mayami về Reina (ngôi thứ ba) → "tôi". Bản cũ "em" sai.

### 1283 — 双鉄 — đại từ xưng hô
- JP: 「こそこそするのは、伝わっているからこそだろう。\n解っているけど改善できない、その申し訳無さゆえだ」
- TW: 「就是因為你的心意傳達到了她才偷偷摸摸啊。她明白你的擔心但又無力改變現狀，對你感到抱歉才這樣的」
- Cũ: 「Lén lút là vì chị ấy đã hiểu được tâm ý của em đó.\nHiểu nhưng không thể sửa đổi được, nên mới thấy có lỗi」
- Mới: 「Lén lút là vì chị ấy đã hiểu được tâm ý của anh đó.\nHiểu nhưng không thể sửa đổi được, nên mới thấy có lỗi」
- Lý do: Soutetsu giải thích cho Reina (người nghe là Reina, 1280 Reina kể chuyện cãi nhau với Paulette) → "anh". Bản cũ "em" sai — ngược chiều với các fix Mayami.

### 1288 — 真闇 — dịch sai
- JP: 「蔵いう鳥籠ば入ってきても、入り口を塞がんどけば……\nただそれだけで、きっと勝手にまた飛んだのに――」
- TW: 「就算她掉進工坊這個牢籠裡，就算入口被人強行堵塞……就這點阻礙，她肯定可以靠自己的力量展翅高飛才對——」
- Cũ: 「Dù có bước vào chiếc lồng chim mang tên xưởng rượu, thì nếu cứ bịt kín lối vào……\nChỉ cần vậy thôi, chắc chắn con bé sẽ tự mình bay đi mất——」
- Mới: 「Dù có bước vào chiếc lồng chim mang tên xưởng rượu, thì chỉ cần đừng bịt kín lối vào……\nChỉ cần vậy thôi, chắc chắn con bé sẽ tự mình bay đi——」
- Lý do: Đảo phủ định: JP 入り口を塞がんどけば = "nếu lối vào KHÔNG bị bịt" (塞がない + どく = để ngỏ). Bản cũ "nếu cứ bịt kín lối vào" ngược nghĩa hoàn toàn.

### 1302 — 双鉄 — đại từ xưng hô
- JP: 「真闇姉と結ばれて、結婚できて。\nそうしたらまた、僕の『家族』はふわふわしてきた」
- TW: 「得以和真闇姐結為連理。就這樣，我又輕飄飄地獲得了新的“家人”」
- Cũ: "「Được gắn kết với chị Mayami, được kết hôn với chị.\nTừ đó, 『Gia đình』 của em lại bắt đầu bồng bềnh lên.」"
- Mới: "「Được gắn kết với chị Mayami, được kết hôn với chị.\nTừ đó, 『Gia đình』 của tôi lại bắt đầu bồng bềnh lên.」"
- Lý do: Soutetsu nói với Mayami → "tôi". Bản cũ "em" sai.

### 1322 — 双鉄 — đại từ xưng hô
- JP: 「わからん。僕は日々姫ではない。ただ僕自身の経験を、\n日々姫の上の投影してみているだけにすぎない」
- TW: 「我不清楚，因為我並不是日日姬本人。我只是把自己的經驗投射到日日姬身上得出了這個結論罷了」
- Cũ: 「Anh không biết. Anh không phải là Hibiki. Chỉ là anh đang thử phóng chiếu\nkinh nghiệm của chính mình lên Hibiki mà thôi」
- Mới: 「Tôi không biết. Tôi không phải là Hibiki. Chỉ là tôi đang thử phóng chiếu\nkinh nghiệm của chính mình lên Hibiki mà thôi」
- Lý do: Soutetsu trả lời Mayami (1320/1324 đều là Mayami) → "tôi" (3 chỗ). Bản cũ "anh" sai.

### 1330 — 双鉄 — đại từ xưng hô
- JP: 「れいなのガイドが可能かどうかを訪ねたときなど、\nポーレットもれいなも、普段どおりに見えたものだが」
- TW: 「我在諮詢能否由玲奈做導遊的時候，你們兩個看起來不是和平時一樣嗎」
- Cũ: 「Lúc anh hỏi xem Reina có thể làm hướng dẫn viên được không,\ncả Paulette và Reina trông vẫn như bình thường mà」
- Mới: 「Lúc tôi hỏi xem Reina có thể làm hướng dẫn viên được không,\ncả Paulette và Reina trông vẫn như bình thường mà」
- Lý do: Soutetsu kể với Mayami về Paulette + Reina (ngôi thứ ba) → "tôi". Bản cũ "anh" sai.

### 1331 — 双鉄 — đại từ xưng hô
- JP: 「愛している、真闇姉。\nそうして、深く――深く深く深く感謝している」
- TW: 「我愛你，真闇姐。以及，我深切地——無比深切地感謝你」
- Cũ: 「Anh yêu em, chị Mayami.\nVà, anh vô cùng——vô cùng vô cùng vô cùng biết ơn em」
- Mới: 「Tôi yêu em, chị Mayami.\nVà, tôi vô cùng——vô cùng vô cùng vô cùng biết ơn em」
- Lý do: Soutetsu nói trực tiếp với Mayami ("chị Mayami") → "tôi" (2 chỗ). "em" ở đây là cách gọi Mayami, giữ nguyên. Bản cũ "anh" sai.

### 1333 — 双鉄 — đại từ xưng hô
- JP: 「僕は一度、僕自身の愚かさゆえに家族を失い。\nけれど、家族を失うことで、新しい家族の一員となれた」
- TW: 「我曾一度因為自己的愚蠢而失去了家人。然而，正因我失去了原本的家人，卻讓我成了新家庭的一員」
- Cũ: "「Em đã từng một lần đánh mất gia đình vì sự ngu ngốc của bản thân.\nNhưng chính nhờ việc đánh mất gia đình đó, em mới trở thành một thành viên của gia đình mới.」"
- Mới: "「Tôi đã từng một lần đánh mất gia đình vì sự ngu ngốc của bản thân.\nNhưng chính nhờ việc đánh mất gia đình đó, tôi mới trở thành một thành viên của gia đình mới.」"
- Lý do: Soutetsu nói với Mayami → "tôi" (2 chỗ). Bản cũ "em" sai.

### 1375 — 双鉄 — đại từ xưng hô
- JP: 「れいながガイドしてくれたから、\n僕は、あらためて深く実感できたのだ」
- TW: 「正因為有玲奈給我們做導遊，我才有了更深刻的感悟」
- Cũ: 「Vì có Reina làm hướng dẫn viên,\nnên anh mới có thể cảm nhận sâu sắc đến vậy」
- Mới: 「Vì có Reina làm hướng dẫn viên,\nnên tôi mới có thể cảm nhận sâu sắc đến vậy」
- Lý do: Soutetsu nói với Mayami → "tôi". Bản cũ "anh" sai.

### 1379 — 双鉄 — đại từ xưng hô
- JP: 「いいや、すばらしいガイドをしてくれた。\nれいなのおかげで、僕は魅力を再確認できた」
- TW: 「沒事，你已經做得非常好了。多虧了你的導遊，我再次感受到了這裡的魅力」
- Cũ: 「Không đâu, em đã làm hướng dẫn viên rất tuyệt vời.\nNhờ có Reina, anh đã có thể một lần nữa cảm nhận sâu sắc sức hấp dẫn đó」
- Mới: 「Không đâu, em ấy đã làm hướng dẫn viên rất tuyệt vời.\nNhờ có Reina, tôi đã có thể một lần nữa cảm nhận sâu sắc sức hấp dẫn đó」
- Lý do: Người nghe là Mayami: "いいや" đáp lại 1378 của Mayami; "れいなのおかげで" nhắc Reina ở ngôi thứ ba (đã có tiền lệ song song ở 1375 cũng nói với Mayami). Nên "em" (gọi thẳng Reina) → "em ấy", "anh" → "tôi".

### 1381 — 双鉄 — đại từ xưng hô
- JP: 「だな。『れいなにとっての御一夜』は、\nまことひだまりのような場所なのだなぁと、僕も感じた」
- TW: 「沒錯。在我的感受中，“玲奈眼裡的御一夜”簡直就像沐浴在溫暖陽光的地方一樣」
- Cũ: 「Đúng vậy. Anh cũng cảm nhận được rằng, 『Ohimitera trong mắt Reina』,\nquả thực là một nơi ấm áp như ánh nắng mặt trời」
- Mới: 「Đúng vậy. Tôi cũng cảm nhận được rằng, 『Ohimitera trong mắt Reina』,\nquả thực là một nơi ấm áp như ánh nắng mặt trời」
- Lý do: Soutetsu nói với Mayami → "tôi". "Ohimitera" giữ nguyên — thuộc diện thống nhất thuật ngữ (chờ Hieu). Bản cũ "anh" sai.

### 1422 — 双鉄 — đại từ xưng hô
- JP: 「れいなの背中が、あまりにも小さくなものと感じて。\n――けれども路子は、もっと小さな背中だったと」
- TW: 「當時我感受著玲奈的後背，覺得實在是過於嬌小——然而記憶中路子的後背，比玲奈的還要再小些」
- Cũ: 「Anh cảm thấy tấm lưng của Reina quá đỗi nhỏ bé.\n——Nhưng tấm lưng của Michiko, còn nhỏ bé hơn thế nữa」
- Mới: 「Tôi cảm thấy tấm lưng của Reina quá đỗi nhỏ bé.\n——Nhưng tấm lưng của Michiko, còn nhỏ bé hơn thế nữa」
- Lý do: Soutetsu kể với Mayami (nhắc Reina ở ngôi thứ ba + hồi tưởng về Michiko, chuyện riêng tư vợ chồng) → "tôi". Bản cũ "anh" sai.

### 1453 — 双鉄 — đại từ xưng hô
- JP: 「好循環だな。それゆえ、僕は――\n僕などは……」
- TW: 「良性循環啊。反倒是我——我這種人……」
- Cũ: 「Một vòng tuần hoàn tốt đẹp. Vì thế, anh——\nNgười như anh thì……」
- Mới: 「Một vòng tuần hoàn tốt đẹp. Vì thế, tôi——\nNgười như tôi thì……」
- Lý do: Soutetsu nói với Mayami → "tôi" (2 chỗ). Bản cũ "anh" sai.

### 1465 — 双鉄 — đại từ xưng hô
- JP: 「もっと優しくできればよかった……\nそんなことをふと、思ってしまったりもした」
- TW: 「要是當時能再溫柔些就好了……忽然之間，我產生了這樣的想法」
- Cũ: 「Giá như anh có thể dịu dàng hơn……\nBất chợt, anh đã nghĩ như vậy」
- Mới: 「Giá như tôi có thể dịu dàng hơn……\nBất chợt, tôi đã nghĩ như vậy」
- Lý do: Soutetsu hồi tưởng về Michiko với Mayami → "tôi" (2 chỗ). Bản cũ "anh" sai.

### 1470 — れいな — romanisation fa/fu
- JP: 「ふあっ！？　あ！？　わあ、れいな寝ちゃって！？\nごめんなさい、ガイド、れいな途中なのに」
- TW: 「話？！啊？！哇啊，玲奈是不是睡著了！？對不起，明明玲奈是在做嚮導」
- Cũ: 「Fua!? A!? Waa, Reina ngủ quên mất rồi!?\nXin lỗi ạ, rõ ràng Reina đang làm hướng dẫn viên mà」
- Mới: 「Phùa!? A!? Waa, Reina ngủ quên mất rồi!?\nXin lỗi ạ, rõ ràng Reina đang làm hướng dẫn viên mà」
- Lý do: Quy tắc fa/fu đã chốt: ふあ → "phùa", không romanisation. Bản cũ "Fua" là romanisation. Dấu っ cuối chỉ nhấn mạnh, giữ bằng "!?".

### 1471 — 双鉄 — đại từ xưng hô
- JP: 「言葉などではとても足りない。\n僕の時間の全てを捧げ、なお足り得るのかわからない」
- TW: 「語言無法表達我感謝之情的萬一。就算把我全部的時間都奉獻給你，都不知道夠不夠」
- Cũ: 「Lời nói là không bao giờ đủ.\nDù có dâng hiến toàn bộ thời gian của mình, anh cũng không biết có đủ hay không」
- Mới: 「Lời nói là không bao giờ đủ.\nDù có dâng hiến toàn bộ thời gian của mình, tôi cũng không biết có đủ hay không」
- Lý do: Soutetsu bày tỏ lòng biết ơn với Mayami → "tôi". Bản cũ "anh" sai.

### 1490 — 双鉄 — đại từ xưng hô
- JP: 「そうか。であれば僕は上段におさまろう」
- TW: 「這樣，那我睡上面吧」
- Cũ: "「Vậy sao. Nếu vậy thì em sẽ nằm tầng trên.」"
- Mới: "「Vậy sao. Nếu vậy thì tôi sẽ nằm tầng trên.」"
- Lý do: Soutetsu nói với Mayami → "tôi". Bản cũ "em" sai.

### 1499 — 双鉄 — đại từ xưng hô
- JP: 「すべてが今、真闇姉とこうしている時間のためには、\n必要不可欠だったのだと思う。ゆえに、僕はしあわせだ」
- TW: 「那些事，在現在看來，都是我如今和真闇姐共處所不可或缺的一部分。所以我可以說，我很幸福」
- Cũ: 「Tất cả những điều đó, đối với khoảng thời gian được ở bên chị Mayami lúc này,\nanh nghĩ là điều không thể thiếu. Vì vậy, anh đang rất hạnh phúc」
- Mới: 「Tất cả những điều đó, đối với khoảng thời gian được ở bên chị Mayami lúc này,\ntôi nghĩ là điều không thể thiếu. Vì vậy, tôi đang rất hạnh phúc」
- Lý do: Soutetsu nói với Mayami → "tôi" (2 chỗ). Bản cũ "anh" sai.

### 1509 — 双鉄 — đại từ xưng hô
- JP: 「ならば僕もだ。\n弱すぎる強すぎるなどあったら知らせてくれ」
- TW: 「那我也開始了。要是太輕或是太重要告訴我哦」
- Cũ: "「Vậy anh cũng bắt đầu đây.\nNếu mạnh quá hay yếu quá thì nhớ bảo anh nhé.」"
- Mới: "「Vậy tôi cũng bắt đầu đây.\nNếu mạnh quá hay yếu quá thì nhớ bảo tôi nhé.」"
- Lý do: Soutetsu đáp Mayami (1506/1511 đều Mayami) → "tôi" (2 chỗ). Bản cũ "anh" sai.

### 1526 — 双鉄 — đại từ xưng hô
- JP: 「それは確かにそうかもしれん。\nが、鳥籠から日々姫は飛び立たなかったかもとも感じる」
- TW: 「雖然確實有那個可能，但我感覺日日姬也可能無法從鳥籠中展翅高飛」
- Cũ: 「Điều đó đúng là có thể xảy ra.\nNhưng, anh cũng cảm thấy Hibiki có thể đã không bay khỏi lồng chim」
- Mới: 「Điều đó đúng là có thể xảy ra.\nNhưng, tôi cũng cảm thấy Hibiki có thể đã không bay khỏi lồng chim」
- Lý do: Soutetsu nói với Mayami (1523/1527 đều Mayami) → "tôi". Bản cũ "anh" sai.

### 1673 — monologue — đại từ xưng hô
- JP: 列車の中だと、旅の途中だと強く感じる。\nこのB寝台客車はもう、レールを走りはしないけれども。
- TW: 因為在車廂裡，所以能強烈感受到我們身在旅途這一事實。雖然這普通臥鋪的客車現在並沒有在軌道上飛馳。
- Cũ: Em cảm nhận sâu sắc rằng mình đang ở trên một chuyến tàu, đang trên một hành trình.\nDù toa giường nằm hạng B này đã không còn lăn bánh trên đường ray nữa.
- Mới: Tôi cảm nhận sâu sắc rằng mình đang ở trên một chuyến tàu, đang trên một hành trình.\nDù toa giường nằm hạng B này đã không còn lăn bánh trên đường ray nữa.
- Lý do: Độc thoại của Soutetsu dùng "tôi" xuyên suốt file (656–1705) — đoạn 1673 về sau đổi sang "em" là sai, không phải ngoại lệ "mình" (chỉ dùng khi tự vấn cảm xúc). Bản cũ "em" sai.

### 1676 — monologue — đại từ xưng hô
- JP: 慣れてきたなられいなの動きのリズムがわかる。\nそれにあわせて、僕もアカスリをゆるゆる動かす。
- TW: 在習慣之後就可以掌握玲奈動作的節奏，配合著這個節奏，我也開始幫玲奈擦起了背。
- Cũ: Khi đã quen, em có thể nắm bắt được nhịp điệu chuyển động của Reina.\nNương theo đó, em cũng chầm chậm đưa miếng bọt biển.
- Mới: Khi đã quen, tôi có thể nắm bắt được nhịp điệu chuyển động của Reina.\nNương theo đó, tôi cũng chầm chậm đưa miếng bọt biển.
- Lý do: Độc thoại Soutetsu → "tôi" (2 chỗ). Bản cũ "em" sai.

### 1686 — monologue — đại từ xưng hô
- JP: 気持ちはわかる。\nポーレットのものも、れいなのものも。
- TW: 她們的心情我能理解。她們雙方都有各自的想法。
- Cũ: Em hiểu cảm giác đó.\nCả của Paulette, và cả của Reina nữa.
- Mới: Tôi hiểu cảm giác đó.\nCả của Paulette, và cả của Reina nữa.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

### 1727 — monologue — đại từ xưng hô
- JP: 安心すれば、どっと疲れがわいてくる。\n僕らも今日は、一日動いて、ずっとはしゃいでいたゆえに。
- TW: 感到安心的瞬間，疲憊就湧了上來。因為我們今天一整天都在活動，一直都保持著高昂的情緒。
- Cũ: Vừa an tâm một cái là bao nhiêu mệt mỏi lập tức ùa về.\nBọn em hôm nay cũng đã vận động cả ngày, lại còn liên tục đùa giỡn nữa.
- Mới: Vừa an tâm một cái là bao nhiêu mệt mỏi lập tức ùa về.\nBọn tôi hôm nay cũng đã vận động cả ngày, lại còn liên tục đùa giỡn nữa.
- Lý do: Độc thoại, nhóm Soutetsu + Mayami (+Reina): "bọn tôi" là dạng nhóm trung tính; "bọn em" sai (Soutetsu không phải "em" với Reina, và với Mayami là "tôi").

### 1735 — monologue — đại từ xưng hô
- JP: そうして僕らの列車は進む。
- TW: 我們的列車就這樣繼續前行。
- Cũ: Và thế là, chuyến tàu của chúng em tiếp tục lăn bánh.
- Mới: Và thế là, chuyến tàu của chúng tôi tiếp tục lăn bánh.
- Lý do: Độc thoại, nhóm 僕ら → "chúng tôi" trung tính. Bản cũ "chúng em" sai (lý do như 1727).

### 1738 — monologue — đại từ xưng hô
- JP: 真闇姉とは夫婦ゆえ。れいなとは乗務後に鉢合わせた折。\nそれぞれ幾度も、一緒に風呂に入っている。
- TW: 我和真闇姐是夫妻關係，而玲奈則是在乘務之後的偶遇。我們各自一起洗過幾次澡。
- Cũ: Với chị Mayami thì vì là vợ chồng. Còn với Reina thì vì thỉnh thoảng chạm mặt sau giờ làm.\nEm đã tắm chung với mỗi người không biết bao nhiêu lần rồi.
- Mới: Với chị Mayami thì vì là vợ chồng. Còn với Reina thì vì thỉnh thoảng chạm mặt sau giờ làm.\nTôi đã tắm chung với mỗi người không biết bao nhiêu lần rồi.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

### 1742 — monologue — đại từ xưng hô
- JP: 思い返せば思い返すほど、印象は一色にまとまっていく。
- TW: 我在腦海裡反覆回想，玲奈的印象漸漸統一。
- Cũ: Càng ngẫm nghĩ lại, ấn tượng của em càng gom lại thành một màu duy nhất.
- Mới: Càng ngẫm nghĩ lại, ấn tượng của tôi càng gom lại thành một màu duy nhất.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

### 1743 — monologue — đại từ xưng hô
- JP: 自身の部屋を思い出す。\nその変遷に、つかの間思いを馳せたことに。
- TW: 我想起了自己的房間。在腦海中瞬間閃過房間的變遷。
- Cũ: Em nhớ lại căn phòng của chính mình.\nVà thoáng nghĩ về những thăng trầm của nó.
- Mới: Tôi nhớ lại căn phòng của chính mình.\nVà thoáng nghĩ về những thăng trầm của nó.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

### 1750 — monologue — đại từ xưng hô
- JP: 手をにぎる。\nそのまま静かに――誓いの、祈りの――キスをする。
- TW: 我握緊真闇姐的手，然後靜靜地——在她的唇上留下誓約和祈禱的吻。
- Cũ: Em nắm lấy tay chị.\nCứ thế lặng lẽ——trao một nụ hôn của lời thề, của sự cầu nguyện.
- Mới: Tôi nắm lấy tay chị.\nCứ thế lặng lẽ——trao một nụ hôn của lời thề, của sự cầu nguyện.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

### 1754 — monologue — đại từ xưng hô
- JP: じっと、真闇姉の顔を見る。\n幼いころから無意識に、憧れ続けてきた瞳を見つめる。
- TW: 我靜靜注視著真闇姐的臉龐，注視著這我從小時候起就無意中愛戀至今的雙眸。
- Cũ: Em nhìn chằm chằm vào khuôn mặt chị Mayami.\nNhìn vào đôi mắt mà từ nhỏ em đã luôn khao khát một cách vô thức.
- Mới: Tôi nhìn chằm chằm vào khuôn mặt chị Mayami.\nNhìn vào đôi mắt mà từ nhỏ tôi đã luôn khao khát một cách vô thức.
- Lý do: Độc thoại Soutetsu → "tôi" (2 chỗ). Bản cũ "em" sai.

### 1763 — monologue — đại từ xưng hô
- JP: なで、なで、なで。れいなを優しく撫ぜていた手が、\n今度は僕を――僕を穏やかに許してくれる。
- TW: 撫摸、撫摸、撫摸。原本溫柔撫摸著玲奈的手，如今撫摸著我——她正溫和地縱容著我。
- Cũ: Xoa, xoa, xoa. Bàn tay nãy giờ vẫn dịu dàng vuốt ve Reina,\ngiờ lại chuyển sang anh——ôn tồn bao dung lấy anh.
- Mới: Xoa, xoa, xoa. Bàn tay nãy giờ vẫn dịu dàng vuốt ve Reina,\ngiờ lại chuyển sang tôi——ôn tồn bao dung lấy tôi.
- Lý do: Độc thoại Soutetsu (僕を = tôi) → "tôi" (2 chỗ). Bản cũ "anh" sai.

### 1768 — monologue — đại từ xưng hô
- JP: 日々姫の姉で、僕の義姉で――\nだけでなく、御一夜全体の姉であるような気さえする。
- TW: 既是日日姬的姐姐，也是我的義姐——不僅如此，我甚至覺得她還是御一夜全體人員的姐姐。
- Cũ: Là chị gái của Hibiki, là chị nuôi của em——\nKhông chỉ vậy, em còn có cảm giác chị ấy như là chị lớn của cả Ohimitera này.
- Mới: Là chị gái của Hibiki, là chị nuôi của tôi——\nKhông chỉ vậy, tôi còn có cảm giác chị ấy như là chị lớn của cả Ohimitera này.
- Lý do: Độc thoại Soutetsu → "tôi" (2 chỗ). "Ohimitera" giữ nguyên — thuộc diện thống nhất thuật ngữ. "chị nuôi" giữ nguyên (義姉, Soutetsu được nhận nuôi — xem 1745). Bản cũ "em" sai.

### 1774 — monologue — đại từ xưng hô
- JP: いまならようやく、僕も素直に頷ける。\n路子も父さんも母さんも、僕を許してくれていると。
- TW: 時至今日，我終於能發自內心地點頭承認。承認路子、父親、母親，他們都會原諒我這一事實。
- Cũ: Đến bây giờ em mới có thể chân thành gật đầu đồng ý.\nRằng Michiko, bố và mẹ, đều đã tha thứ cho em.
- Mới: Đến bây giờ tôi mới có thể chân thành gật đầu đồng ý.\nRằng Michiko, bố và mẹ, đều đã tha thứ cho tôi.
- Lý do: Độc thoại Soutetsu → "tôi" (2 chỗ: "tôi mới…", "tha thứ cho tôi"). Bản cũ "em" sai.

### 1778 — monologue — đại từ xưng hô
- JP: 一度失ったものゆえに、その尊さを、\n僕は恐らく、いくらかは理解できている。
- TW: 正因為曾經失去過，才更懂得它的珍貴。可能我終於對這句話有所理解了。
- Cũ: Vì đã từng một lần đánh mất, nên em\ncó lẽ cũng hiểu được phần nào sự quý giá của nó.
- Mới: Vì đã từng một lần đánh mất, nên tôi\ncó lẽ cũng hiểu được phần nào sự quý giá của nó.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

### 1780 — monologue — đại từ xưng hô
- JP: あらためてそう言われると、\n実に不思議な言葉というか、概念だなと感じてしまう。
- TW: 此刻再聽到這個詞，實在是一個讓人感到不可思議的詞語，或者說是概念。
- Cũ: Được nghe lại từ đó,\nem chợt cảm thấy nó quả thực là một từ ngữ, hay đúng hơn là một khái niệm thật kỳ diệu.
- Mới: Được nghe lại từ đó,\ntôi chợt cảm thấy nó quả thực là một từ ngữ, hay đúng hơn là một khái niệm thật kỳ diệu.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

### 1792 — monologue — đại từ xưng hô
- JP: れいなの声は、けれどはっきり晴れてくれない。\n行き違いは、思ったより深いものなのかもしれん。
- TW: 然而，玲奈的聲音卻並沒有開朗起來。看來她倆的矛盾比我們想像得要更加深刻。
- Cũ: Thế nhưng, giọng Reina vẫn chưa thực sự vui vẻ trở lại.\nCó lẽ sự hiểu lầm này sâu sắc hơn em tưởng.
- Mới: Thế nhưng, giọng Reina vẫn chưa thực sự vui vẻ trở lại.\nCó lẽ sự hiểu lầm này sâu sắc hơn tôi tưởng.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

### 1796 — monologue — đại từ xưng hô
- JP: れいなのぱあっと華やいだ声。\nこれを曇らせてしまうなど、まさか出来ようはずもない。
- TW: 玲奈的嗓音清脆嘹亮。又有誰能夠忍心讓這麼明媚的聲音籠上陰霾呢。
- Cũ: Giọng nói bừng sáng rạng rỡ của Reina.\nLàm sao em nỡ lòng nào dập tắt sự hào hứng đó được chứ.
- Mới: Giọng nói bừng sáng rạng rỡ của Reina.\nLàm sao tôi nỡ lòng nào dập tắt sự hào hứng đó được chứ.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

### 1799 — monologue — đại từ xưng hô
- JP: れいなの声が急にしおれる。\nこういう話題で軽口を叩くべきではなかったのかもしれん。
- TW: 玲奈的聲音忽然消沉下去，看來這種話題不該隨口亂說才是。
- Cũ: Giọng Reina bỗng xìu xuống.\nCó lẽ em không nên đùa cợt về chủ đề này.
- Mới: Giọng Reina bỗng xìu xuống.\nCó lẽ tôi không nên đùa cợt về chủ đề này.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

### 1842 — monologue — đại từ xưng hô
- JP: 真闇姉とれいなののんびりとしたやりとりは、\nどこまでだって和やかで、むしろ落ち着こうものなのに。
- TW: 真闇姐和玲奈的互動，卻一直都是悠閒又和緩的，甚至可以說讓人心境平和。
- Cũ: Cuộc trò chuyện nhàn nhã giữa chị Mayami và Reina\nrõ ràng là rất hòa thuận, đáng lẽ ra phải khiến em thấy bình tâm mới phải.
- Mới: Cuộc trò chuyện nhàn nhã giữa chị Mayami và Reina\nrõ ràng là rất hòa thuận, đáng lẽ ra phải khiến tôi thấy bình tâm mới phải.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

### 1843 — monologue — đại từ xưng hô
- JP: 先頭が真闇姉、真ん中がれいな、最後尾が僕。\n椅子を並べて腰掛けたなら、れいなは早速泡だて始める。
- TW: 真闇姐在最前面，玲奈在中間，我在最後面。我們一坐上椅子，玲奈就搓起了泡泡。
- Cũ: Chị Mayami ngồi trước, Reina ở giữa, còn em ở cuối.\nKhi ba chiếc ghế đã được xếp ngay ngắn, Reina liền bắt đầu tạo bọt xà phòng.
- Mới: Chị Mayami ngồi trước, Reina ở giữa, còn tôi ở cuối.\nKhi ba chiếc ghế đã được xếp ngay ngắn, Reina liền bắt đầu tạo bọt xà phòng.
- Lý do: Độc thoại Soutetsu (最後尾が僕) → "tôi". Bản cũ "em" sai.

### 1891 — monologue — đại từ xưng hô
- JP: いってふと、\nあながちそれが冗談でないかもとも思ってしまう。
- TW: 話一出口，我忽然感覺她說的可能並不是玩笑話。
- Cũ: Nói rồi em chợt nghĩ,\nchưa chắc đó đã là lời nói đùa.
- Mới: Nói rồi tôi chợt nghĩ,\nchưa chắc đó đã là lời nói đùa.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

### 1892 — monologue — đại từ xưng hô
- JP: 言葉を出した瞬間に、\nそれでは足りぬと理解する。
- TW: 說出口的瞬間，我明白光是這樣說還不足以讓人理解。
- Cũ: Khoảnh khắc thốt ra những lời đó,\nem nhận ra như thế vẫn chưa đủ.
- Mới: Khoảnh khắc thốt ra những lời đó,\ntôi nhận ra như thế vẫn chưa đủ.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

### 1893 — monologue — dịch sai
- JP: 言われてみるとそうかもしれん。クマ川下り、包丁づくり、\n投炭練習に酒造見学。どれも僕は経験済みだが――
- TW: 說起來可能真的是這樣。隈河漂流、菜刀製作、加煤練習以及參觀釀酒。雖然每一樣我都曾體驗過——
- Cũ: Nghe chị ấy nói vậy, có lẽ là thế thật. Xuôi dòng sông Kuma, rèn dao,\ntập xúc than dồn toa, tham quan xưởng rượu. Dù tất cả anh đều đã trải qua——
- Mới: Nghe chị ấy nói vậy, có lẽ là thế thật. Xuôi dòng sông Kuma, rèn dao,\ntập xúc than, tham quan xưởng rượu. Dù tất cả tôi đều đã trải qua——
- Lý do: Hai lỗi trong một dòng: (1) "dồn toa" bịa thêm — 投炭練習 chỉ là "tập xúc than" (xúc than vào lò), không có "dồn toa" nào trong JP; bỏ theo quyết định 1027 của Hieu 20/11. (2) Độc thoại Soutetsu → "tôi", bản cũ "anh" sai.

### 1907 — monologue — đại từ xưng hô
- JP: ふたりくっついて寝たくもあるが、\nそうするにはあまりに狭すぎる。
- TW: 雖然我也想兩個人靠在一起睡，不過那樣也太擠了。
- Cũ: Em cũng muốn hai đứa nằm ngủ ôm nhau,\nnhưng giường này quá chật để làm thế.
- Mới: Tôi cũng muốn hai đứa nằm ngủ ôm nhau,\nnhưng giường này quá chật để làm thế.
- Lý do: Độc thoại Soutetsu → "tôi". Bản cũ "em" sai.

## §3. Second pass (đọc lại toàn bộ fix đối chiếu JP)

- Tổng số fix: **56** / đã đọc lại: **56** / loại bỏ: **0** / sửa lại: **29**.
- 29 dòng sửa lại trong second pass: toàn bộ là lỗi phiên âm khi chép fix — đã làm rơi dấu ngoặc 「 」 (và dấu `"` bao ngoài ở 11 dòng: 731, 905, 1058, 1114, 1135, 1204, 1228, 1302, 1333, 1490, 1509) của bản cũ. Kiểm tra diff cơ học phát hiện: sau khi khôi phục đúng khung ngoặc của bản cũ, mọi fix chỉ còn khác bản cũ đúng ở chỗ cần sửa (đổi đại từ / thêm Ư / sửa phủ định / bỏ "dồn toa" / "Fua"→"Phùa"). Không fix nào bị loại — mọi phán đoán ở vòng 1 đều đứng vững sau khi đọc lại.
- Kiểm tra diff từng fix vs bản cũ (sau khi chuẩn hoá `\n`): pronoun 48/48 chỉ đổi đúng token đại từ; mistranslation 4/4 chỉ đổi đúng chỗ sai; gasp 3/3 chỉ thêm Ư; fa/fu 1/1 chỉ đổi "Fu"→"Phù".
- Ghi chú của parent (20/11 ~07:50, khi gộp): 48 giá trị fix trong `audit-lr-mayami-tsuika03-wrong.json` ban đầu chứa newline thực (do ghi `\n` dạng JSON escape) thay vì literal `\n` theo quy ước CSV3/TOML, nên không khớp khối TOML (khối TOML đúng). Parent đã chuẩn hóa mã hóa 48 giá trị đó sang literal `\n` — nội dung fix không đổi; bản JSON gốc lưu ở `audit-lr-mayami-tsuika03-wrong.json.orig-2026-11-20`. Sau chuẩn hóa, kiểm chứng lại: khối TOML 56 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 56/56.

## §4. Các điểm đã kiểm tra và giữ nguyên (không sửa)

- **"Ưm fufu" cho んふふっ (1125, 1127, 1128, 1130, 1132, 1182, 1264 — 7 dòng): GIỮ NGUYÊN.** Đây là tiếng cười ("fufu" vẫn còn), "Ưm" diễn tả âm mũi ん — không phải tiếng rên. Khác với tiền lệ h8 ("Ư hự" thay cho tiếng cười).
- **"Ưm" cho ん/ううむ (722, 1154, 1155): GIỮ NGUYÊN.** File dùng "Ừm" cho うん/うむ nhưng "Ưm" cho ん/ううむ một cách nhất quán — có thể là lựa chọn có chủ ý của người dịch (ư gần với âm う không tròn môi của tiếng Nhật). Không đủ chắc để sửa.
- **"Dzo" / "Dô ta, dô tà" cho うんしょ、よいしょっ (1139, 1208, 1355, 1412): GIỮ NGUYÊN.** Cách diễn tiếng rặn sức của người dịch, nhất quán trong file (2 biến thể của cùng một âm).
- **"Funyaa" (1173), "Fuwaaaaaaaa" (1157), "Nmyu" (1157), "Ufufu" (1180, 1183, 1207, 1210, 1714), "Ehehe" (1149, 1150): GIỮ NGUYÊN.** Giữ sát tiếng Nhật theo hướng dẫn của Hieu; quy tắc fa/fu chỉ áp cho ふぁ/ふあ/ふぇ/ふやぁ, không áp cho ふわ/ふにゃ.
- **"chị nuôi" cho 義姉 (1768) và "bố nuôi, mẹ nuôi" cho 義父さん/義母さん (1838): GIỮ NGUYÊN.** Soutetsu được nhận nuôi (1745: "từ sau khi tôi được nhận nuôi"), nên 義 ở đây là quan hệ nuôi dưỡng thật — đúng với ngoại lệ đã ghi trong skill (kiểm tra TW trước khi gắn cờ 義).
- **"Makura" (1210, 1240, 1416): GIỮ NGUYÊN.** Reina gọi Mayami là まくらさん — giữ nguyên tên gọi như trong game, chưa có thuật ngữ đã chốt cho biệt danh này.
- **"Tororyu-yu" (1620): GIỮ NGUYÊN.** Tên riêng nhà tắm 登呂流湯, giữ nguyên dạng romanised.
- **"xưởng rượu" cho 蔵 (687, 1177, 1272, 1288, 1351…): GIỮ NGUYÊN.** 蔵 trong ngữ cảnh nhà máy rượu Migita; TW dùng 工坊 (xưởng) — "xưởng rượu" là cách diễn hợp lý, không sửa.
- **"sống mòn" (1177): GIỮ NGUYÊN.** Thêm nhẹ so với JP ("không thể để Hii-chan sống ở xưởng rượu") nhưng diễn đúng ý (sống mòn trong xưởng sẽ phí hoài đời con bé); TW "不能讓小日在作坊裡長大" ủng hộ.
- **1044 "thành phố Ohimitera": KHÔNG SỬA trong audit này.** Ngoài dạng cũ "Ohimitera" (thuộc diện thống nhất), 市 ở đây (御一夜市) là "chợ/phiên chợ" chứ không phải "thành phố" — cả hai đều chờ đợt thống nhất thuật ngữ, đã ghi vào §5.

## §5. Ghi chú cho Hieu (cần quyết, không tự quyết)

- **Thống nhất thuật ngữ trong file này:** "Ohimitera" còn 3 dòng (1044, 1381, 1768) → "Ohitoyo"; riêng 1044 còn sai "thành phố" cho 御一夜市 (đúng ra là "chợ Ohitoyo" / "phiên chợ Ohitoyo"). Chờ đợt thống nhất chung.
- **Người nghe của 3 dòng Soutetsu (suy luận từ dòng kề, đã ghi rõ lý do trong §2):** 1204 ("Hửm? Cả tôi nữa à?" — đáp lời mời "洗いっこ" của Mayami ở 1146), 1379 ("Không đâu, em ấy…" — "いいや" đáp 1378 của Mayami; "れいなのおかげで" nhắc Reina ngôi thứ ba), 1422 ("Tôi cảm thấy tấm lưng của Reina…" — nhắc Reina ngôi thứ ba + hồi tưởng Michiko). Nếu Hieu thấy người nghe thực tế khác (ví dụ 1379 nói thẳng với Reina), báo lại để sửa.
- **1283 là fix ngược chiều duy nhất:** Soutetsu với Reina phải là "anh" ("tâm ý của anh"), trong khi 24 fix đối thoại còn lại đều là "anh"/"em" → "tôi" với Mayami. Đã kiểm chứng người nghe là Reina (1280 Reina kể chuyện cãi nhau với Paulette).

## §6. Khối TOML (56 khóa, đã parse-kiểm chứng: 0 sai lệch giá trị)

```toml
[script]
"689" = "「——Đúng vậy nhỉ. Chị cũng cảm thấy chói lóa.\\nNhìn Hii-chan, rồi nhìn chuyến tàu đó」"
"717" = "「……Chắc là vậy.\\nTài năng của Hibiki, tôi cũng cảm thấy đó là một tài năng như vậy」"
"731" = "\"「……Nếu đúng là vậy, thì phải chi\\nPaulette cũng hiểu được điều đó thì tốt biết mấy.」\""
"905" = "\"「Ư」\""
"1043" = "「Đã căng sức, lại còn phấn khích nữa.\\nNói thật là tôi cũng từng lo không biết em ấy sẽ làm hướng dẫn viên thế nào」"
"1058" = "\"「Ra là vậy, tôi——chúng ta,\\nsẽ nuôi dưỡng gia đình của chúng ta, tổ ấm của chúng ta sao.」\""
"1064" = "「Trời ạ. Nhất định tôi phải xem mới được」"
"1114" = "\"「Chỉ mong rằng, cho đến tận cuối hành trình của tôi.\\nChị Mayami——hãy cùng tôi đi hết chuyến đi này.」\""
"1120" = "「Ư!」"
"1121" = "「Ư!!!!」"
"1135" = "\"「Từng chút, từng chút một trở thành gia đình.\\nTừ trong những tháng ngày hạnh phúc đó, tôi lại có được một hạnh phúc to lớn hơn nữa.」\""
"1204" = "\"「Hửm? Cả tôi nữa à?」\""
"1228" = "\"「Nhí nhảnh đến mức tôi muốn dùng từ ngây thơ để miêu tả luôn.\\nCó lẽ Reina cũng đã chơi đùa cùng chị Mayami——cùng chúng ta đấy.」\""
"1283" = "「Lén lút là vì chị ấy đã hiểu được tâm ý của anh đó.\\nHiểu nhưng không thể sửa đổi được, nên mới thấy có lỗi」"
"1288" = "「Dù có bước vào chiếc lồng chim mang tên xưởng rượu, thì chỉ cần đừng bịt kín lối vào……\\nChỉ cần vậy thôi, chắc chắn con bé sẽ tự mình bay đi——」"
"1302" = "\"「Được gắn kết với chị Mayami, được kết hôn với chị.\\nTừ đó, 『Gia đình』 của tôi lại bắt đầu bồng bềnh lên.」\""
"1322" = "「Tôi không biết. Tôi không phải là Hibiki. Chỉ là tôi đang thử phóng chiếu\\nkinh nghiệm của chính mình lên Hibiki mà thôi」"
"1330" = "「Lúc tôi hỏi xem Reina có thể làm hướng dẫn viên được không,\\ncả Paulette và Reina trông vẫn như bình thường mà」"
"1331" = "「Tôi yêu em, chị Mayami.\\nVà, tôi vô cùng——vô cùng vô cùng vô cùng biết ơn em」"
"1333" = "\"「Tôi đã từng một lần đánh mất gia đình vì sự ngu ngốc của bản thân.\\nNhưng chính nhờ việc đánh mất gia đình đó, tôi mới trở thành một thành viên của gia đình mới.」\""
"1375" = "「Vì có Reina làm hướng dẫn viên,\\nnên tôi mới có thể cảm nhận sâu sắc đến vậy」"
"1379" = "「Không đâu, em ấy đã làm hướng dẫn viên rất tuyệt vời.\\nNhờ có Reina, tôi đã có thể một lần nữa cảm nhận sâu sắc sức hấp dẫn đó」"
"1381" = "「Đúng vậy. Tôi cũng cảm nhận được rằng, 『Ohimitera trong mắt Reina』,\\nquả thực là một nơi ấm áp như ánh nắng mặt trời」"
"1422" = "「Tôi cảm thấy tấm lưng của Reina quá đỗi nhỏ bé.\\n——Nhưng tấm lưng của Michiko, còn nhỏ bé hơn thế nữa」"
"1453" = "「Một vòng tuần hoàn tốt đẹp. Vì thế, tôi——\\nNgười như tôi thì……」"
"1465" = "「Giá như tôi có thể dịu dàng hơn……\\nBất chợt, tôi đã nghĩ như vậy」"
"1470" = "「Phùa!? A!? Waa, Reina ngủ quên mất rồi!?\\nXin lỗi ạ, rõ ràng Reina đang làm hướng dẫn viên mà」"
"1471" = "「Lời nói là không bao giờ đủ.\\nDù có dâng hiến toàn bộ thời gian của mình, tôi cũng không biết có đủ hay không」"
"1490" = "\"「Vậy sao. Nếu vậy thì tôi sẽ nằm tầng trên.」\""
"1499" = "「Tất cả những điều đó, đối với khoảng thời gian được ở bên chị Mayami lúc này,\\ntôi nghĩ là điều không thể thiếu. Vì vậy, tôi đang rất hạnh phúc」"
"1509" = "\"「Vậy tôi cũng bắt đầu đây.\\nNếu mạnh quá hay yếu quá thì nhớ bảo tôi nhé.」\""
"1526" = "「Điều đó đúng là có thể xảy ra.\\nNhưng, tôi cũng cảm thấy Hibiki có thể đã không bay khỏi lồng chim」"
"1673" = "Tôi cảm nhận sâu sắc rằng mình đang ở trên một chuyến tàu, đang trên một hành trình.\\nDù toa giường nằm hạng B này đã không còn lăn bánh trên đường ray nữa."
"1676" = "Khi đã quen, tôi có thể nắm bắt được nhịp điệu chuyển động của Reina.\\nNương theo đó, tôi cũng chầm chậm đưa miếng bọt biển."
"1686" = "Tôi hiểu cảm giác đó.\\nCả của Paulette, và cả của Reina nữa."
"1727" = "Vừa an tâm một cái là bao nhiêu mệt mỏi lập tức ùa về.\\nBọn tôi hôm nay cũng đã vận động cả ngày, lại còn liên tục đùa giỡn nữa."
"1735" = "Và thế là, chuyến tàu của chúng tôi tiếp tục lăn bánh."
"1738" = "Với chị Mayami thì vì là vợ chồng. Còn với Reina thì vì thỉnh thoảng chạm mặt sau giờ làm.\\nTôi đã tắm chung với mỗi người không biết bao nhiêu lần rồi."
"1742" = "Càng ngẫm nghĩ lại, ấn tượng của tôi càng gom lại thành một màu duy nhất."
"1743" = "Tôi nhớ lại căn phòng của chính mình.\\nVà thoáng nghĩ về những thăng trầm của nó."
"1750" = "Tôi nắm lấy tay chị.\\nCứ thế lặng lẽ——trao một nụ hôn của lời thề, của sự cầu nguyện."
"1754" = "Tôi nhìn chằm chằm vào khuôn mặt chị Mayami.\\nNhìn vào đôi mắt mà từ nhỏ tôi đã luôn khao khát một cách vô thức."
"1763" = "Xoa, xoa, xoa. Bàn tay nãy giờ vẫn dịu dàng vuốt ve Reina,\\ngiờ lại chuyển sang tôi——ôn tồn bao dung lấy tôi."
"1768" = "Là chị gái của Hibiki, là chị nuôi của tôi——\\nKhông chỉ vậy, tôi còn có cảm giác chị ấy như là chị lớn của cả Ohimitera này."
"1774" = "Đến bây giờ tôi mới có thể chân thành gật đầu đồng ý.\\nRằng Michiko, bố và mẹ, đều đã tha thứ cho tôi."
"1778" = "Vì đã từng một lần đánh mất, nên tôi\\ncó lẽ cũng hiểu được phần nào sự quý giá của nó."
"1780" = "Được nghe lại từ đó,\\ntôi chợt cảm thấy nó quả thực là một từ ngữ, hay đúng hơn là một khái niệm thật kỳ diệu."
"1792" = "Thế nhưng, giọng Reina vẫn chưa thực sự vui vẻ trở lại.\\nCó lẽ sự hiểu lầm này sâu sắc hơn tôi tưởng."
"1796" = "Giọng nói bừng sáng rạng rỡ của Reina.\\nLàm sao tôi nỡ lòng nào dập tắt sự hào hứng đó được chứ."
"1799" = "Giọng Reina bỗng xìu xuống.\\nCó lẽ tôi không nên đùa cợt về chủ đề này."
"1842" = "Cuộc trò chuyện nhàn nhã giữa chị Mayami và Reina\\nrõ ràng là rất hòa thuận, đáng lẽ ra phải khiến tôi thấy bình tâm mới phải."
"1843" = "Chị Mayami ngồi trước, Reina ở giữa, còn tôi ở cuối.\\nKhi ba chiếc ghế đã được xếp ngay ngắn, Reina liền bắt đầu tạo bọt xà phòng."
"1891" = "Nói rồi tôi chợt nghĩ,\\nchưa chắc đó đã là lời nói đùa."
"1892" = "Khoảnh khắc thốt ra những lời đó,\\ntôi nhận ra như thế vẫn chưa đủ."
"1893" = "Nghe chị ấy nói vậy, có lẽ là thế thật. Xuôi dòng sông Kuma, rèn dao,\\ntập xúc than, tham quan xưởng rượu. Dù tất cả tôi đều đã trải qua——"
"1907" = "Tôi cũng muốn hai đứa nằm ngủ ôm nhau,\\nnhưng giường này quá chật để làm thế."
```

**Tổng cộng sau file này: 71 file / 3.819 dòng sai** (cơ sở 70 file / 3.763 + 56 file này)

## Kết bài

File lr真闇追加03_ブルートレインの夜.txt.toml (05_Mayami, 337 dòng) đã kiểm tra xong toàn bộ: **56 dòng sai (16,6%)** — gần như toàn bộ là lỗi đại từ xưng hô của Soutetsu (48/56): bản dịch cũ để Soutetsu xưng "anh"/"em" với Mayami và trong độc thoại, trong khi quy tắc đã chốt là "tôi" với Mayami và "tôi" trong độc thoại; chỉ có 1 dòng ngược chiều (1283, với Reina phải là "anh"). 4 lỗi dịch sai tại chỗ gồm 1 lỗi đảo phủ định nghiêm trọng (1288: "nếu cứ bịt kín lối vào" ngược hẳn JP "nếu lối vào không bị bịt"), 1 lỗi đọc sai te-form thành mệnh lệnh (689), 1 lỗi bịa thêm "lòng Reina" (731) và 1 lỗi bịa "dồn toa" + sai đại từ (1893). 3 tiếng gasp っ bị mất (905, 1120, 1121 — trong đó 905 là sweep bỏ sót) và 1 lỗi romanisation fa/fu (1470: "Fua"→"Phùa"). Không có dòng lệch hàng, không có chuỗi xoay, không có dòng mồ côi hay chưa dịch. Second pass: 56/56 đã đọc lại, 0 loại bỏ, 29 sửa lại (khôi phục dấu ngoặc 「 」 bị rơi khi chép). Khối TOML 56 khóa đã parse-kiểm chứng, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 56/56. Còn chờ Hieu: thống nhất "Ohimitera" (3 dòng, trong đó 1044 còn sai "thành phố" cho 御一夜市) và xác nhận người nghe của 3 dòng 1204/1379/1422.
