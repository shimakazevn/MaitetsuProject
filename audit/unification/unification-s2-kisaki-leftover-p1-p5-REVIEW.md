# Unification U16 — §2 P1 + P5 (Kisaki-cluster pronoun leftovers)

Batch U16, quyết 22/11 ~13:47 (từ cờ U8 F1/F2, mở 22/11 ~12:40). Chuỗi: 160 mục / 2.731 dòng đã gộp (U14a/b/c).

## §1. Phạm vi

**P1 — Soutetsu tự xưng "Anh"→"Tôi" với Kisaki, toàn dự án.** Quy tắc khóa (21/11 ~19:45 + 22/11 ~03:32): Soutetsu là "Tôi" với Kisaki (nguyên tắc xưng hô đối ứng; cô là tiền bối của anh; Kisaki→Soutetsu dùng tên trần "Soutetsu", không "anh Soutetsu"). Quét TẤT CẢ file có Kisaki nói chuyện + kiểm tra độc thoại — xem §2.

**P5 — Kisaki tự xưng, quy tắc theo ngữ cảnh (khóa 21/11 ~19:45):** công việc/quyết đoán → "tôi", thân mật/dễ tổn thương → "em" (JP luôn ボク). Nhánh U8 chưa bao quát: **Kisaki03** (lr稀咲追加03) + **稀咲02**. U8 đã quyết tsuika01 (6 dòng → "em", 1516 giữ "tôi") và tsuika02 (0 dòng — 22 dòng "Tôi" đều chế độ công việc). tsuika01 1564 GIỮ "Em" đã do coordinator quyết (trò chuyện thân mật bữa tối) — không quyết lại.

## §2. Phương pháp

- Bản đồ old_vn theo thứ tự ưu tiên: unification đã gộp (theo thứ tự gộp) > moan fix > audit fix > CSV3 good set (87.833 dòng sau khi bỏ 3.898 dòng stale). Chỉ dùng wrong.json của các batch ĐÃ GỘP trong `unification/` (kiểm tra queue.json status=merged; chuỗi hiện tại 160 mục / 2.731 dòng, gồm U14a/b/c). Bỏ qua audit entry có fix null.
- Liệt kê P1: (1) mọi dòng 双鉄/双鉄H có Anh/anh trong 12 file trọng tâm Kisaki + đọc cửa sổ ±3; (2) bộ lọc cửa sổ (±5, chỉ Kisaki, không nữ chính khác) trên các file còn lại; (3) bộ lọc kề (Kisaki trong ±2 dòng VÀ VN chứa cô/Kisaki hoặc JP chứa 稀咲/キミ/君); (4) kiểm tra file chỉ có 2 người nói ⊆ {Soutetsu, Kisaki} (5 file — đều đã bao quát); (5) quét độc thoại toàn dự án.
- Liệt kê P5: mọi dòng 稀咲 có Tôi/tôi/Em/em trong VN hiện tại ở 2 file + mọi dòng Kisaki có JP ボク (để bắt dòng VN không có đại từ tự xưng).
- **Bài học liệt kê (ghi lại để các batch sau khỏi lặp):** lần liệt kê đầu dùng regex `\b[Tt]ôi\b|\b[Ee]m\b|\b[Aa]nh\b` trên giá trị JSON thô đã BỎ SÓT các dòng mà đại từ đứng ngay sau `\n` dạng chữ (hai ký tự `\`+`n`) — vì `\b` không khớp giữa `n` và chữ cái. Liệt kê lại với văn bản đã chuẩn hóa (`\n` → khoảng trắng) tìm thêm **41 dòng P1** (5 dòng sửa) và **7 dòng P5** (1 dòng sửa). Liệt kê hiện tại là đầy đủ đối với mọi file có Kisaki nói chuyện.
- Mỗi fix đều đọc JP (+TW; JP thắng khi mâu thuẫn) và cửa sổ đối thoại; quyết theo ủy quyền của Hieu, ghi bằng chứng + lý do từng dòng. Không sửa hàng loạt bằng script.
- F5 (coordinator 22/11 ~12:50): token SFX romaji viết hoa ở MỌI vị trí trong giá trị fix mới — áp dụng ở 1900 ("fufu" → "Fufu").

## §3. Các dòng sửa (JP / TW / old_vn / fix)

### 稀咲h2_プライベートルーム.txt.toml — 18 dòng

**key 912** (P1) — nguồn old_vn: csv3
- JP: 「っ――あ――…………うむ。\n呼吸や顔が変わっていたとは、気付かなかったが」
- TW: 「――啊――…………嗯。我都沒注意到自己表情和呼吸的變化」
- old_vn: 「A――ờ――………… ừm.\nAnh không nhận ra là hơi thở hay nét mặt của mình đã thay đổi đâu」
- fix: 「A――ờ――………… ừm.\nTôi không nhận ra là hơi thở hay nét mặt của mình đã thay đổi đâu」
- Lý do: 1-on-1 H-scene với Kisaki; Soutetsu tự xưng → "Tôi" (P1, quy tắc khóa 21/11 ~19:45).

**key 915** (P1) — nguồn old_vn: csv3
- JP: 「――わざと、見せたのか？」
- TW: 「――所以你是故意露的嗎？」
- old_vn: 「――Em cố tình, cho anh xem sao?」
- fix: 「――Em cố tình, cho tôi xem sao?」
- Lý do: 1-on-1 H-scene với Kisaki.

**key 932** (P1) — nguồn old_vn: csv3
- JP: 「……せっかく教えてもらったことだが」
- TW: 「……這是你教會我的寶貴知識」
- old_vn: 「……Mặc dù đã cất công dạy cho anh」
- fix: 「……Mặc dù đã cất công dạy cho tôi」
- Lý do: 1-on-1 H-scene với Kisaki; "dạy cho anh" = dạy cho Soutetsu (người được dạy, JP 教えてもらった).

**key 933** (P1) — nguồn old_vn: unif:unification-s2-niiroku-tsuika-cluster-wrong.json
- JP: 「……言われてみれば――\n確かに、そうした傾向はあるかもしれんな」
- TW: 「……這麼說來――的確是有這方面的傾向吧」
- old_vn: 「……Nghe cô nói vậy thì――\nCó lẽ anh đúng là có khuynh hướng như thế thật」
- fix: 「……Nghe cô nói vậy thì――\nCó lẽ tôi đúng là có khuynh hướng như thế thật」
- Lý do: GHÉP trên fix U8 (P3 "cô"); chỉ đổi "anh"→"tôi". 1-on-1 H-scene với Kisaki.

**key 1207** (P1) — nguồn old_vn: csv3
- JP: 「ああ――僕だって限界だ」
- TW: 「嗯――我也到極限了」
- old_vn: 「Ừm――anh cũng đến giới hạn rồi」
- fix: 「Ừm――tôi cũng đến giới hạn rồi」
- Lý do: 1-on-1 H-scene với Kisaki; JP 僕だって.

**key 1226** (P1) — nguồn old_vn: csv3
- JP: 「ああ、挿れたい。\nその指と、僕のペニスを交換してしまいたいほどだ」
- TW: 「嗯，很想插進去。好想你的手指和我的陰莖對調一下」
- old_vn: 「Ừm, anh muốn đưa vào.\nĐến mức muốn tráo đổi ngón tay đó với dương vật của anh luôn」
- fix: 「Ừm, tôi muốn đưa vào.\nĐến mức muốn tráo đổi ngón tay đó với dương vật của tôi luôn」
- Lý do: 1-on-1 H-scene với Kisaki; ×2 "anh"→"tôi" (cả tân ngữ "dương vật của anh").

**key 1230** (P1) — nguồn old_vn: csv3
- JP: 「うん、稀咲――イク、からっ」
- TW: 「嗯，稀咲――我要射了」
- old_vn: 「Ừm, Kisaki――anh ra, đây」
- fix: 「Ừm, Kisaki――tôi ra, đây」
- Lý do: 1-on-1 H-scene với Kisaki.

**key 1233** (P1) — nguồn old_vn: csv3
- JP: 「ああ、欲しい。\n稀咲が想像しているよりも、ずっと激しく狂おしく」
- TW: 「嗯，非常想。比稀咲的想像中要激烈難以抑制得多」
- old_vn: 「Ừm, anh muốn.\nMãnh liệt và điên cuồng hơn nhiều so với những gì Kisaki đang tưởng tượng đấy」
- fix: 「Ừm, tôi muốn.\nMãnh liệt và điên cuồng hơn nhiều so với những gì Kisaki đang tưởng tượng đấy」
- Lý do: 1-on-1 H-scene với Kisaki.

**key 1236** (P1) — nguồn old_vn: csv3
- JP: 「ふむ？ この部屋が僕の表れか？」
- TW: 「嗯？ 這個房間就是我的體現嗎？」
- old_vn: 「Hừm? Căn phòng này phản chiếu con người anh sao?」
- fix: 「Hừm? Căn phòng này phản chiếu con người tôi sao?」
- Lý do: 1-on-1 H-scene với Kisaki; JP 僕の表れ.

**key 1265** (P1) — nguồn old_vn: csv3
- JP: 「だったらボクもだ。\n一緒にイキたい。イカせてほしい」
- TW: 「我也一樣。我想和你一起高潮，請幫我射精吧」
- old_vn: 「Vậy thì anh cũng thế.\nAnh muốn cùng nhau ra. Hãy làm cho anh ra đi」
- fix: 「Vậy thì tôi cũng thế.\nTôi muốn cùng nhau ra. Hãy làm cho tôi ra đi」
- Lý do: 1-on-1 H-scene với Kisaki; ×3 "anh"→"tôi". LƯU Ý: JP dùng ボク katakana trong dòng 双鉄H — dị thường; TW xác nhận người nói nam ("我想和你一起高潮，請幫我射精吧").

**key 1271** (P1) — nguồn old_vn: csv3
- JP: 「テレビなど居間で見ればいい。真闇姉にも言ったのだが、\n『部屋にあったら便利やけん』と、押し付けられてな」
- TW: 「我在起居室看電視就夠了。這話我跟真闇姐說的時候，她非說“房間裡有一台方便”，然後就硬塞給了我」
- old_vn: 「Tivi thì xem ở phòng khách là được rồi. Anh cũng từng nói với chị Mayami như vậy,\nnhưng chị ấy cứ nằng nặc ép anh nhận với lý do 『Có trong phòng thì sẽ tiện hơn mà』」
- fix: 「Tivi thì xem ở phòng khách là được rồi. Tôi cũng từng nói với chị Mayami như vậy,\nnhưng chị ấy cứ nằng nặc ép tôi nhận với lý do 『Có trong phòng thì sẽ tiện hơn mà』」
- Lý do: 1-on-1 H-scene với Kisaki; ×2 "anh"→"tôi" ("nói với chị Mayami" + "ép anh nhận").

**key 1273** (P1) — nguồn old_vn: csv3
- JP: 「記憶にあるかぎりは、一度も無い。\n裏庭だし、従業員が通るような場所でもない」
- TW: 「我沒有人走過的印象。後院也不是工作人員會經過的地方」
- old_vn: 「Theo những gì anh nhớ thì chưa từng có ai cả.\nĐây là sân sau, cũng không phải là nơi nhân viên thường đi lại」
- fix: 「Theo những gì tôi nhớ thì chưa từng có ai cả.\nĐây là sân sau, cũng không phải là nơi nhân viên thường đi lại」
- Lý do: 1-on-1 H-scene với Kisaki.

**key 1275** (P1) — nguồn old_vn: csv3
- JP: 「僕らしい、とは？」
- TW: 「我的風格是什麼？」
- old_vn: 「Mang phong cách của anh, là sao?」
- fix: 「Mang phong cách của tôi, là sao?」
- Lý do: 1-on-1 H-scene với Kisaki; JP 僕らしい.

**key 1278** (P1) — nguồn old_vn: csv3
- JP: 「やり方はわかったし。稀咲のことを想えばいつでも、\n間違いなく、一人でイケる手応えはある」
- TW: 「我知道做法了啊。現在只要想著稀咲，我任何時候都能一個人擼出來了」
- old_vn: 「Anh đã biết cách làm rồi. Chỉ cần nghĩ về Kisaki, thì bất cứ lúc nào,\nchắc chắn anh cũng có thể tự mình ra được」
- fix: 「Tôi đã biết cách làm rồi. Chỉ cần nghĩ về Kisaki, thì bất cứ lúc nào,\nchắc chắn tôi cũng có thể tự mình ra được」
- Lý do: 1-on-1 H-scene với Kisaki; ×2 "anh"→"tôi".

**key 1302** (P1) — nguồn old_vn: csv3
- JP: 「そうだったのか？ 気付かなかったが」
- TW: 「是這樣嗎？ 我真的沒有注意到」
- old_vn: 「Vậy sao? Anh hoàn toàn không nhận ra đấy」
- fix: 「Vậy sao? Tôi hoàn toàn không nhận ra đấy」
- Lý do: 1-on-1 H-scene với Kisaki.

**key 1313** (P1) — nguồn old_vn: csv3
- JP: 「目を奪い……\n惹きつけるため――か？」
- TW: 「為了吸走我的視線……為了勾引我――對嗎？」
- old_vn: 「Để thu hút ánh nhìn……\nđể quyến rũ anh――sao?」
- fix: 「Để thu hút ánh nhìn……\nđể quyến rũ tôi――sao?」
- Lý do: 1-on-1 H-scene với Kisaki; "quyến rũ anh" = quyến rũ Soutetsu.

**key 1321** (P1) — nguồn old_vn: csv3
- JP: 「が、今は二人だ。僕は稀咲をイカせたいし、稀咲に僕を\nイカせて欲しいと思ってる。その方が、オナニーよりも」
- TW: 「現在我們是兩個人，我想讓你高潮，所以稀咲可以幫我射精嗎？肯定比自慰要好多了吧」
- old_vn: 「Nhưng, hiện tại chúng ta đang ở cùng nhau. Anh muốn làm cho Kisaki ra, và anh cũng muốn Kisaki\nlàm cho anh ra. Như thế, sẽ tốt hơn là thủ dâm」
- fix: 「Nhưng, hiện tại chúng ta đang ở cùng nhau. Tôi muốn làm cho Kisaki ra, và tôi cũng muốn Kisaki\nlàm cho tôi ra. Như thế, sẽ tốt hơn là thủ dâm」
- Lý do: 1-on-1 H-scene với Kisaki; ×3 "anh"→"tôi" (JP 僕は…僕を).

**key 1334** (P1) — nguồn old_vn: unif:unification-s2-niiroku-tsuika-cluster-wrong.json
- JP: 「稀咲――イクなら、一緒にイキたい」
- TW: 「稀咲――要高潮的話，我想跟你一起」
- old_vn: 「Kisaki――Nếu ra, anh muốn ra cùng cô」
- fix: 「Kisaki――Nếu ra, tôi muốn ra cùng cô」
- Lý do: GHÉP trên fix U8 (P3 "cô"); chỉ đổi "anh"→"tôi". 1-on-1 H-scene với Kisaki.

### lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml — 4 dòng

**key 1229** (P1) — nguồn old_vn: csv3
- JP: 「何度も何度もセックスしよう。\n僕らのこどもを授かるまで。僕もそれを望んでいるゆえ」
- TW: 「我們來一次又一次地做愛，直到你懷上我們的孩子為止。我也希望你能懷上」
- old_vn: 「Chúng ta hãy làm tình hết lần này đến lần khác nhé.\nCho đến khi em mang thai đứa con của chúng ta. Bởi vì anh cũng mong muốn điều đó.」
- fix: 「Chúng ta hãy làm tình hết lần này đến lần khác nhé.\nCho đến khi em mang thai đứa con của chúng ta. Bởi vì tôi cũng mong muốn điều đó.」
- Lý do: 1-on-1 H-scene với Kisaki; JP 僕もそれを望んでいる.

**key 1287** (P1) — nguồn old_vn: csv3
- JP: 「わかった。\n稀咲が満足するまで、このまま抜かず、動かずいるが」
- TW: 「知道了。我不拔出來也不動，直到你滿意為止」
- old_vn: 「Anh hiểu rồi.\nCho đến khi em thỏa mãn, anh sẽ không rút ra, cũng không cử động.」
- fix: 「Tôi hiểu rồi.\nCho đến khi em thỏa mãn, tôi sẽ không rút ra, cũng không cử động.」
- Lý do: 1-on-1 H-scene với Kisaki; ×2 "anh"→"tôi".

**key 1290** (P1) — nguồn old_vn: csv3
- JP: 「承った。乳首は、特に丹念に洗わせていただこう」
- TW: 「知道了。那我就重點洗洗你的乳頭」
- old_vn: 「Tuân lệnh. Anh sẽ rửa nhũ hoa cho em thật cẩn thận.」
- fix: 「Tuân lệnh. Tôi sẽ rửa nhũ hoa cho em thật cẩn thận.」
- Lý do: 1-on-1 H-scene với Kisaki.

**key 1317** (P1) — nguồn old_vn: csv3
- JP: 「それをいうなら、僕のほうこそ、だ」
- TW: 「要說的話是我要謝你」
- old_vn: 「Nếu nói vậy thì, anh mới là người phải cảm ơn.」
- fix: 「Nếu nói vậy thì, tôi mới là người phải cảm ơn.」
- Lý do: 1-on-1 H-scene với Kisaki; JP 僕のほうこそ.

### 稀咲01_金と人.txt.toml — 13 dòng

**key 1499** (P1) — nguồn old_vn: csv3
- JP: 「いや。暗算自体をあまりしないので。\n電卓を使ったほうが、確実だ」
- TW: 「不。其實我很少心算。我覺得用計算器來得準確一些」
- old_vn: 「Không. Bản thân anh ít khi tính nhẩm.\nDùng máy tính vẫn chắc chắn hơn.」
- fix: 「Không. Bản thân tôi ít khi tính nhẩm.\nDùng máy tính vẫn chắc chắn hơn.」
- Lý do: Đối thoại với Kisaki ở ngân hàng (cô hỏi về tính nhẩm; 1524 cô tiếp mạch máy tính/lỗi nhập liệu).

**key 1503** (P1) — nguồn old_vn: audit
- JP: 「すまない態度を見せてしまった。言葉の真意もわからず、\n金が大事と聞いただけで、君を守銭奴のように誤解した」
- TW: 「不好意思，剛才我太膚淺了。我沒有理解你真正的意思，聽你說金錢很重要，就把你誤解成了守財奴」
- old_vn: 「Xin lỗi vì thái độ lúc nãy của anh. Chưa hiểu rõ ý nghĩa thực sự trong lời nói của em,\nchỉ nghe nói tiền quan trọng, anh đã hiểu lầm em là một kẻ hám tiền.」
- fix: 「Xin lỗi vì thái độ lúc nãy của tôi. Chưa hiểu rõ ý nghĩa thực sự trong lời nói của em,\nchỉ nghe nói tiền quan trọng, tôi đã hiểu lầm em là một kẻ hám tiền.」
- Lý do: Xin lỗi trực tiếp Kisaki ("lời nói của em", "hiểu lầm em"); 1501 cô xin lỗi về bố mình ngay trước. Nguồn audit (audit giữ "anh").

**key 1514** (P1) — nguồn old_vn: csv3
- JP: 「いや、大学の友人に数学の得意なものがいて――\nそれに習った」
- TW: 「不，只是我在大學有位朋友很擅長數學——所以就跟他學了一點」
- old_vn: 「Không, hồi đại học anh có một người bạn giỏi toán――\nanh học được từ cậu ấy thôi.」
- fix: 「Không, hồi đại học tôi có một người bạn giỏi toán――\ntôi học được từ cậu ấy thôi.」
- Lý do: Đối thoại với Kisaki ở ngân hàng (1512 cô nói về nghiệp vụ giao dịch; 1524 cô tiếp mạch).

**key 1515** (P1) — nguồn old_vn: csv3
- JP: 「いや、豪勢な食事ではなく――いうなれば家庭料理をだ。\n野菜の煮物だの、ひじきだの」
- TW: 「不，我並不是說要吃得多豐盛——我指的是家常菜。比如煮青菜或者羊栖菜之類的」
- old_vn: 「Không, ý anh không phải là những bữa ăn sang trọng――mà là những bữa cơm gia đình cơ.\nVí dụ như rau củ hầm, rong biển Hijiki chẳng hạn.」
- fix: 「Không, ý tôi không phải là những bữa ăn sang trọng――mà là những bữa cơm gia đình cơ.\nVí dụ như rau củ hầm, rong biển Hijiki chẳng hạn.」
- Lý do: Đối thoại với Kisaki ở ngân hàng (cùng mạch 1514; 1524 cô tiếp mạch).

**key 1559** (P1) — nguồn old_vn: audit
- JP: 「謝られるようなこととは思わん。\n実際、良い話し合いをさせてもらった」
- TW: 「你不需要為此道歉。我們之間的交流確實很有意義」
- old_vn: 「Anh không nghĩ em cần phải xin lỗi đâu.\nThực tế thì, chúng ta đã có một cuộc thảo luận rất tốt mà.」
- fix: 「Tôi không nghĩ em cần phải xin lỗi đâu.\nThực tế thì, chúng ta đã có một cuộc thảo luận rất tốt mà.」
- Lý do: Trả lời Kisaki: 1557 cô phản đối với tư cách Giám đốc chi nhánh; "em cần phải xin lỗi" = Kisaki. Nguồn audit.

**key 1611** (P1) — nguồn old_vn: csv3
- JP: 「ピザが手軽か？\n食べ辛いもののように思うが……」
- TW: 「吃披薩很方便嗎？我覺得吃起來還挺麻煩的……」
- old_vn: 「Pizza mà dễ ăn á?\nAnh thấy nó khó ăn mới đúng……」
- fix: 「Pizza mà dễ ăn á?\nTôi thấy nó khó ăn mới đúng……」
- Lý do: Trao đổi Soutetsu↔Kisaki về pizza/bữa ăn (1606/1609 cô nói; 1612 cô đáp "Là do cách nói của em không tốt rồi").

**key 1753** (P1) — nguồn old_vn: csv3
- JP: 「主張をぶつけあうだけでない、\n実りある話し合いが出来れば――と願っている」
- TW: 「希望這次協商不要還只是各說各話，而是能得到些共識」
- old_vn: 「Anh mong rằng chúng ta không chỉ dừng lại ở việc bảo vệ quan điểm của mình,\nmà có thể có một cuộc thảo luận thực sự mang lại kết quả.」
- fix: 「Tôi mong rằng chúng ta không chỉ dừng lại ở việc bảo vệ quan điểm của mình,\nmà có thể có một cuộc thảo luận thực sự mang lại kết quả.」
- Lý do: Tiếp nối lời anh nói với Kisaki ở 1740/1741 ("Houshou Kisaki, em——"); 1751/1757 cô tiếp mạch.

**key 1796** (P1) — nguồn old_vn: audit
- JP: 「だろうと僕は確信している。すぐには影響が出なくても\nいずれは徐々に、確実に」
- TW: 「我確信如此。影響就算不會馬上發生，也一定會慢慢顯現」
- old_vn: 「Anh tin chắc là vậy. Dù không có ảnh hưởng ngay lập tức\nnhưng dần dần, chắc chắn sẽ xảy ra.」
- fix: 「Tôi tin chắc là vậy. Dù không có ảnh hưởng ngay lập tức\nnhưng dần dần, chắc chắn sẽ xảy ra.」
- Lý do: Trả lời trực tiếp câu hỏi của Kisaki ở 1789 về lập trường phản đối của anh. Tin cậy trung-cao: Mototada/Hibiki xen vào ở 1791–1793 nhưng mạch hỏi–đáp là Kisaki→Soutetsu. Nguồn audit.

**key 1810** (P1) — nguồn old_vn: csv3
- JP: 「すまん。気になってしまってな」
- TW: 「抱歉。我只是稍微有些在意」
- old_vn: 「Xin lỗi. Tự nhiên anh thấy tò mò thôi.」
- fix: 「Xin lỗi. Tự nhiên tôi thấy tò mò thôi.」
- Lý do: Trả lời Kisaki (1804/1805/1809 cô hỏi dồn về kế hoạch và tiền tệ); 1815 Mototada mới xen vào.

**key 1828** (P1) — nguồn old_vn: csv3
- JP: 「だろうな。僕も、税金やら保険料やらを、\n銀行で取り扱ってもらうことがある」
- TW: 「是啊。我也在銀行繳納過稅金、辦理過保險」
- old_vn: 「Chắc là vậy. Anh cũng có lúc phải\nnhờ ngân hàng xử lý tiền thuế hay tiền bảo hiểm.」
- fix: 「Chắc là vậy. Tôi cũng có lúc phải\nnhờ ngân hàng xử lý tiền thuế hay tiền bảo hiểm.」
- Lý do: Trả lời Kisaki 1822 ("Cửu khứ pháp à. Anh có hay dùng không?").

**key 1863** (P1) — nguồn old_vn: csv3
- JP: 「いや。こだわらん。お任せしよう」
- TW: 「沒事，我不挑，點什麼都可以」
- old_vn: 「Không sao. Anh không kén chọn đâu. Tùy em quyết định.」
- fix: 「Không sao. Tôi không kén chọn đâu. Tùy em quyết định.」
- Lý do: Trả lời Kisaki 1862 ("Anh không cần phải xin lỗi đâu. Em rất vui vì được anh quan tâm"); "Tùy em quyết định" = Kisaki.

**key 1945** (P1) — nguồn old_vn: audit
- JP: 「それに加えて、宝生稀咲――君の助力まで得られるのだ。\n損得でいえば、むしろ僕らの得点の方が多いと思う」
- TW: 「而且我們還得到了你——寶生稀咲的幫助。要權衡得失的話，不如說我們反而賺多了」
- old_vn: 「Thêm vào đó, Houshou Kisaki――còn có được sự giúp đỡ của em nữa.\nNếu nói về được mất, anh nghĩ điểm số của chúng ta còn cao hơn đấy.」
- fix: 「Thêm vào đó, Houshou Kisaki――còn có được sự giúp đỡ của em nữa.\nNếu nói về được mất, tôi nghĩ điểm số của chúng ta còn cao hơn đấy.」
- Lý do: Nói với Kisaki: 1942 cô giảng về sai số; "còn có được sự giúp đỡ của em nữa" = Kisaki. Nguồn audit.

**key 2002** (P1) — nguồn old_vn: csv3
- JP: 「では、『僕の場合は、電卓の方が確実だ』と言い直そう。\n暗算ミスなら、入力ミスの十倍は起こしてしまいそうだ」
- TW: 「那就當做是“對我來說，還是用計算器更準確”吧。我覺得自己心算的話，錯誤會有輸入錯誤的十倍那麼多」
- old_vn: 「Vậy để anh sửa lại là 『Trong trường hợp của anh, dùng máy tính chắc chắn hơn』.\nNếu tính nhẩm, có lẽ anh sẽ mắc lỗi gấp mười lần lỗi nhập liệu mất.」
- fix: 「Vậy để tôi sửa lại là 『Trong trường hợp của tôi, dùng máy tính chắc chắn hơn』.\nNếu tính nhẩm, có lẽ tôi sẽ mắc lỗi gấp mười lần lỗi nhập liệu mất.」
- Lý do: Nhắc lại câu máy tính của anh, mạch quay về câu hỏi tính nhẩm của Kisaki ở 1660. Tin cậy trung: mạch dài, nhưng không có người nghe khác xen vào mạch này.

### 稀咲03_純白のレール.txt.toml — 4 dòng

**key 1335** (P1) — nguồn old_vn: csv3
- JP: 「――そんな未来は、迎えたくない。\nそのことだけは、つくづく思うよ」
- TW: 「——我唯一能確定的是，自己不希望事情變成那樣」
- old_vn: 「——Anh không muốn đón nhận một tương lai như thế.\nAnh chỉ nghĩ đến điều đó một cách sâu sắc thôi.」
- fix: 「——Tôi không muốn đón nhận một tương lai như thế.\nTôi chỉ nghĩ đến điều đó một cách sâu sắc thôi.」
- Lý do: Người nghe là Kisaki hoặc Hachiroku — cả hai đều theo quy tắc "tôi" nên fix đúng theo cả hai cách đọc. Cùng cảnh 1338 anh đã dùng "tôi" ("Tôi đã nghe Kisaki kể lại").

**key 1932** (P1) — nguồn old_vn: csv3
- JP: 「一枚もらうぞ」
- TW: 「我吃一塊」
- old_vn: 「Cho anh một miếng nhé.」
- fix: 「Cho tôi một miếng nhé.」
- Lý do: Ngay sau lời tỏ tình của Kisaki ở 1930 ("Soutetsu, anh biết không? … Kisaki thích cậu đấy"); 1936 anh tỏ tình lại.

**key 1938** (P1) — nguồn old_vn: audit
- JP: 「僕が、どうかしたか？」
- TW: 「我怎麼了？」
- old_vn: 「Anh làm sao thế?」
- fix: 「Tôi làm sao thế?」
- Lý do: Tiếp nối lời tỏ tình của anh với Kisaki ở 1936 ("Tôi muốn, Kisaki. Cô hãy luôn ở bên cạnh tôi"). Tin cậy trung-cao. Nguồn audit.

**key 1999** (P1) — nguồn old_vn: csv3
- JP: 「いえ、ご連絡はいただきましたし。\n[せんだい,1]千内からわざわざ、こちらこそすみません」
- TW: 「沒關係，事先不是聯絡過了嗎。麻煩您專程從川內大老遠跑過來，我才應該道歉」
- old_vn: 「Không đâu, anh đã liên lạc trước rồi mà. Cất công từ Sendai đến tận đây, tôi mới là người phải xin lỗi.」
- fix: 「Không đâu, tôi đã liên lạc trước rồi mà. Cất công từ Sendai đến tận đây, tôi mới là người phải xin lỗi.」
- Lý do: Trả lời Kisaki 1998 ("Muốn anh phải là người nói ra trước"); đã có "tôi" ở câu sau cùng dòng. Tin cậy trung: có yếu tố Sendai/Urakami trong cảnh, nhưng mạch hỏi–đáp trực tiếp là Kisaki→Soutetsu.

### 日々姫10_稀咲の未来図、日々姫の未来図.txt.toml — 3 dòng

**key 2450** (P1) — nguồn old_vn: csv3
- JP: 「ああ、それは理解してる。\nレイアウトとは――このジオラマのことか？」
- TW: 「啊，這個我知道。場景模型就是指這個微縮景觀模型嗎？」
- old_vn: 「À, cái đó thì anh hiểu.\\nCòn sa bàn——là mô hình này sao?」
- fix: 「À, cái đó thì tôi hiểu.\nCòn sa bàn——là mô hình này sao?」
- Lý do: Hỏi–đáp trực tiếp với Kisaki 2444 (cô hỏi anh có nghĩ đây là đề xuất của cô không).

**key 2587** (P1) — nguồn old_vn: csv3
- JP: 「そう思うし――\n誰もが本当はわかっているとも思うのだ」
- TW: 「我既這麼想——也認為不論是誰其實都懂這個道理」
- old_vn: 「Anh nghĩ vậy——\\nvà anh cũng tin rằng thực ra ai cũng hiểu điều đó.」
- fix: 「Tôi nghĩ vậy——\nvà tôi cũng tin rằng thực ra ai cũng hiểu điều đó.」
- Lý do: Đồng tình ngay với câu của Kisaki ở 2585 về chính quyền thành phố.

**key 2653** (P1) — nguồn old_vn: csv3
- JP: 「僕の配慮が不足していた。\n申し訳ない」
- TW: 「是我考慮不周了。真對不起」
- old_vn: 「Là do anh thiếu chu đáo.\nAnh xin lỗi.」
- fix: 「Là do tôi thiếu chu đáo.\nTôi xin lỗi.」
- Lý do: Trả lời trực tiếp Kisaki 2652 ("xin mời anh xem qua cái này").

### グランドリライト06_稀咲.txt.toml — 3 dòng

**key 2238** (P1) — nguồn old_vn: csv3
- JP: 「残念ながら、そのとおりだな。\n交換用のレールも、もう入手困難だと聞いている」
- TW: 「很遺憾，就是這樣。聽說連替換用的鐵軌都已經很難得到了」
- old_vn: 「Rất tiếc, đúng là vậy.\nAnh nghe nói đường ray để thay thế giờ cũng rất khó kiếm.」
- fix: 「Rất tiếc, đúng là vậy.\nTôi nghe nói đường ray để thay thế giờ cũng rất khó kiếm.」
- Lý do: Trao đổi Soutetsu↔Kisaki khi kiểm tra đường ray (2236 cô nhận xét "Nhẵn nhụi thật. Nhưng cũng có vết xước"; 2239 cô tiếp mạch). Tin cậy trung-cao (Akai có mặt nhưng không tham gia mạch này).

**key 2445** (P1) — nguồn old_vn: csv3
- JP: 「間違いなかろう。線路さえつなげられるのなら。\n重量物大量輸送こそが、鉄道の原点で本領だと聞く」
- TW: 「沒有錯，只要線路連接上了，大量運輸重物正是鐵路的原點和本領所在」
- old_vn: 「Chắc chắn là vậy. Miễn là đường ray được kết nối.\nAnh nghe nói vận chuyển hàng hóa nặng với số lượng lớn chính là khởi điểm và thế mạnh của đường sắt.」
- fix: 「Chắc chắn là vậy. Miễn là đường ray được kết nối.\nTôi nghe nói vận chuyển hàng hóa nặng với số lượng lớn chính là khởi điểm và thế mạnh của đường sắt.」
- Lý do: Trả lời trực tiếp câu hỏi của Kisaki ở 2444 ("Không sản xuất nữa sao? Hoàn toàn luôn á?"); cùng cảnh 2443 anh đã dùng "tôi" ("Tôi không rõ tình hình ở các địa phương khác").

**key 2510** (P1) — nguồn old_vn: csv3
- JP: 「無論、構わん。が――その方面で、\n僕が稀咲を助けられるようなことが、なにかあるのか？」
- TW: 「當然可以。可是……我在這方面有幫得上你的地方嗎？」
- old_vn: 「Tất nhiên là được. Nhưng――trong lĩnh vực đó,\nanh có thể giúp gì được cho Kisaki sao?」
- fix: 「Tất nhiên là được. Nhưng――trong lĩnh vực đó,\ntôi có thể giúp gì được cho Kisaki sao?」
- Lý do: Trả lời mạch của Kisaki ở 2507 (cô hỏi về thói quen gặp riêng của anh); 2513 cô đáp lại. Fix đúng theo cả hai cách đọc người nghe (Kisaki hoặc bố cô — cả hai đều "tôi").

### lr稀咲追加01_仲国視察の誘い.txt.toml — 1 dòng

**key 1488** (P1) — nguồn old_vn: unif:unification-s2-kisaki-address-tsuika-lr-wrong.json
- JP: 「準備のほんの一部分。双鉄は閃くタイプじゃないか。\n予想外の事態を、むしろ発展のチャンスにできる」
- TW: 「竟是這樣的準備啊」
- old_vn: 「Chỉ là một phần nhỏ của sự chuẩn bị thôi. Soutetsu thuộc tuýp người hay nảy ra ý tưởng bất chợt mà.\nAnh có thể biến những tình huống ngoài dự kiến thành cơ hội phát triển.」
- fix: 「Chỉ là một phần nhỏ của sự chuẩn bị thôi. Soutetsu thuộc tuýp người hay nảy ra ý tưởng bất chợt mà.\nSoutetsu có thể biến những tình huống ngoài dự kiến thành cơ hội phát triển.」
- Lý do: KHÔNG phải Soutetsu tự xưng: đây là Kisaki nói về Soutetsu, JP chủ ngữ là 双鉄 ("Anh" trần = bare "anh" U7b để lại). Theo P4 (Kisaki→Soutetsu dùng tên trần): "Anh" → "Soutetsu". Chỉ đổi câu 2; câu 1 đã dùng tên "Soutetsu" sẵn. GHÉP trên fix U7b.

### lr稀咲追加02_仲国視察.txt.toml — 1 dòng

**key 1084** (P1) — nguồn old_vn: unif:unification-s2-kisaki-address-tsuika-lr-wrong.json
- JP: 「ニワトリタマゴになってるよ？ 双鉄。\n建築限界が何かを、ボクに説明してくれてるんだよね」
- TW: 「先有雞還是先有蛋囉？雙鐵。應該先給我解釋一下建築限界是什麼才對吧」
- old_vn: 「Anh đang bị vòng luẩn quẩn 'con gà hay quả trứng có trước' rồi đấy? Soutetsu.\nAnh đang định giải thích cho tôi giới hạn kiến trúc là gì cơ mà.」
- fix: 「Anh đang bị vòng luẩn quẩn 'con gà hay quả trứng có trước' rồi đấy? Soutetsu.\nSoutetsu đang định giải thích cho tôi giới hạn kiến trúc là gì cơ mà.」
- Lý do: KHÔNG phải Soutetsu tự xưng: Kisaki nói với Soutetsu, JP chủ ngữ là 双鉄 (câu 2). Theo P4: "Anh" → "Soutetsu". Chỉ đổi câu 2; câu 1 giữ "Anh" (đã có tên "Soutetsu" cuối câu — đổi nữa sẽ lặp tên trong cùng một câu). GHÉP trên fix U7b.

### 稀咲02_新事業案.txt.toml — 4 dòng

**key 1900** (P5) — nguồn old_vn: csv3
- JP: 「ああ――ふふっ、なんだ、\nボクの食生活をそこまで心配してくれたんだ」
- TW: 「啊——呵呵，原來你這麼擔心我的飲食呀」
- old_vn: 「A——fufu, gì chứ,\nhóa ra anh lại lo lắng cho chế độ ăn uống của tôi đến thế sao.」
- fix: 「A——Fufu, gì chứ,\nhóa ra anh lại lo lắng cho chế độ ăn uống của em đến thế sao.」
- Lý do: Nhánh thân mật: cô vui vì anh lo cho chế độ ăn của mình (2073 xác nhận anh lo "Một cô gái trẻ mà toàn ăn đồ ăn làm sẵn"); cười "fufu" + ngạc nhiên thích thú — tương tự tiền lệ tsuika01 1024 (được khen → "em"). F5: "fufu" → "Fufu" (romaji SFX viết hoa mọi vị trí).

**key 2067** (P5) — nguồn old_vn: csv3
- JP: 「ボ、ボ、ボクが緊張！？ す、するわけ、ないよっ。\nな、納得をして、入ってるんだし――全然、へ、平気っ」
- TW: 「我、我、我會緊張！？怎、怎麼、會呢。我、我是同意之後、才進來的——完全、沒、沒關係」
- old_vn: 「T, t, tôi mà căng thẳng á!? L, làm gì, có chuyện đó.\nT, tôi đã đồng ý, rồi mới vào mà——hoàn toàn, kh, không sao cả.」
- fix: 「T, t, em mà căng thẳng á!? L, làm gì, có chuyện đó.\nT, em đã đồng ý, rồi mới vào mà——hoàn toàn, kh, không sao cả.」
- Lý do: Nhánh thân mật/dễ tổn thương: cô lắp bắp phủ nhận sự căng thẳng khi ở trong bồn tắm với anh (2047 anh trêu "cô sợ lửa à?"; JP な、納得をして、入ってるんだし — "đã đồng ý rồi mới vào"). Ngượng ngùng trước mặt anh, không phải bàn công việc.

**key 2068** (P5) — nguồn old_vn: csv3
- JP: 「わ、わかったよ」
- TW: 「我、我知道了」
- old_vn: 「T, tôi hiểu rồi.」
- fix: 「T, em hiểu rồi.」
- Lý do: Tiếp nối 2067 (cùng cơn lắp bắp ngượng ngùng); đồng nhất "em" với 2067.

**key 2339** (P5) — nguồn old_vn: csv3
- JP: 「そんな欲なら素敵だね。\n業務を抜きに、応援したくなってしまうよ」
- TW: 「這種欲望很值得讚揚啊。就算拋開工作不談，我也不由得想為你加油打氣了」
- old_vn: 「Một sự tham lam như vậy thật tuyệt vời.\nBỏ qua công việc sang một bên, tôi cũng bất giác muốn ủng hộ anh rồi đấy.」
- fix: 「Một sự tham lam như vậy thật tuyệt vời.\nBỏ qua công việc sang một bên, em cũng bất giác muốn ủng hộ anh rồi đấy.」
- Lý do: Nhánh thân mật: JP tự ghi rõ chuyển chế độ — 業務を抜きに ("bỏ qua công việc sang một bên") — cô bước ra khỏi chế độ công việc để bày tỏ sự ngưỡng mộ/ủng hộ cá nhân. "anh" (tân ngữ, JP không có キミ) giữ nguyên — ngoài phạm vi P5.

### lr稀咲追加03_新事業案.txt.toml — 1 dòng

**key 906** (P5) — nguồn old_vn: audit
- JP: 「フィジカルなイチャイチャとおんなじくらい。\nボクはね、ロジカルなイチャイチャも大好きなんだ」
- TW: 「不止是彼此身體的親熱，心靈的纏綿也是我的最愛」
- old_vn: 「Cũng giống như việc tình tứ về mặt thể xác.\nEm ấy nhé, cũng rất thích việc tình tứ về mặt logic nữa.」
- fix: 「Cũng giống như việc tình tứ về mặt thể xác.\nEm nhé, cũng rất thích việc tình tứ về mặt logic nữa.」
- Lý do: Nhánh thân mật: JP ボク ngôi thứ nhất, nói về イチャイチャ (tình tứ) với chồng; VN cũ "Em ấy nhé" là ngôi thứ ba ("cô ấy") — không thỏa quy tắc P5 ("em"). Đổi "Em ấy" → "Em". LƯU Ý: U8 §5 O2 đã xác nhận dòng này là "em đúng" — nhưng văn bản thực tế là "Em ấy", không phải "Em"; quyết này sửa lại hình thức cho đúng phán đoán đó. Nguồn audit.

## §4. Giữ nguyên / đã đúng (đã kiểm chứng, không sửa)

### P1 — GIỮ "anh" (người nghe xác định được là người khác, hoặc nhóm/không xác định được)

- **h2 1295:** 『Anh/chị muốn tham quan xưởng ạ?』 là lời nhân viên nói với khách lạ (trích dẫn), không phải Soutetsu tự xưng.
- **稀咲01 1649/1655:** địa chỉ nhóm — 1655 nói rõ "hai người" (Kisaki+Hibiki); "anh" là dạng dùng với Hibiki, đã qua audit; đổi thành "tôi" sẽ xưng hô sai với Hibiki. **1799/1800:** phát biểu chung trước phòng họp (Mototada vào ở 1798; 1800 dùng "chúng ta"); khác 1796 (trả lời trực tiếp Kisaki). **1988/1989:** mơ hồ — Kisaki đang đưa tiền cho Hibiki, Soutetsu xen vào; người nghe không xác định được. **Độc thoại 2325/2413/2415/2525:** "anh Urakami" / "anh ấy" ngôi thứ ba, không phải tự xưng.
- **稀咲02:** 0 dòng P1. Đối thoại 1782/1891/2194/2337 đều là "anh Urakami" ngôi thứ ba; Soutetsu trong file này đã dùng "tôi" (vd. 1791, 2205).
- **稀咲03:** 1627 ("anh Urakami"; "tôi" đã đúng), 1694 (nghe là Hibiki — 1689 cô hỏi anh), 1876 (nghe là Hibiki — 1862 cô xin câu trả lời của anh làm tham khảo), 1928 ("anh Urakami"), 1947 (nghe là Hibiki — 1940 cô muốn dùng làm tham khảo), 1950 ("anh Urakami"), 1974 (cảnh ăn mừng, nhóm), 2038 ("anh" là người được cảm ơn, ngôi thứ hai, người nghe chưa xác định — cờ P4, xem §6), 2057 ("anh Urakami"; "Cô" = Kisaki), 2093 (họp nhóm Mototada/Urakami/Paulette), 2135 (cảnh ăn mừng; tiếp nối Hibiki 2134 chúc mừng).
- **日々姫10:** 2256 (nói với Hibiki 2253), 2338 (nói với Hibiki), 2374 (nói với Hibiki), 2593 (nhóm, trọng tâm Hibiki — "Anh tất nhiên là ủng hộ Hibiki rồi", cô đáp ở 2595), 2606 (nói về Hibiki, cô đáp ở 2607), 2651 (đồng tình với Mayami/Nagi — nhóm, không hướng về Kisaki), 2691 (nói với Paulette rõ ràng — "anh" đúng theo P1), 2737 (cảnh triển lãm nhóm), 2895 (nhóm, trọng tâm Hibiki — tiếp nối 2892/2894 nói với Hibiki).
- **lr_稀咲h1 1033:** "anh Soutetsu" trong lời trích dẫn của người khác — tham chiếu ngôi thứ ba, không phải tự xưng.
- **日々姫02:** 2101 (nghe là Hibiki), 2108 (nghe là Hibiki; "cô ấy" = Kisaki ngôi thứ ba), 2111/2114/2118 (nghe là Hibiki), 2160 (nghe là Hibiki), 2179 (nghe là Hibiki — "Anh và Kisaki là người quen từ xưa rồi"), 2203 (nghe là chủ tiệm giặt ủi — "Phong cách làm việc của em" = công việc của bà ấy).
- **日々姫07 2097:** tự giới thiệu với Kuma Kuma (đứa trẻ gấu); không phải Kisaki. **日々姫16 1672/1849/2096:** đều nói với Hibiki. **ポーレット14 1549:** "anh" tự xưng với Paulette — đúng theo P1. **凪ふかみ08c 2065:** người nghe là Nagi/Fukami. **Grand11 2513:** suy ngẫm nhóm, trọng tâm Hibiki.
- **41 dòng tìm thêm sau khi sửa regex (xem §2):** lrれいな追加02 1505/1692 (độc thoại/narration, không có người nghe — xem cờ F-U16-5), Grand07 2589 (nhóm Mayami/Michiko/Paulette/Hachiroku) + 2663 (nói với Reina), Grand08 1248 (nói với Fukami), Grand11 2167/2383/2404 (nhóm/Reina) + 2807 (nói với Michiko), ハチロク02 2685 (nhóm), ハチロク07 2418 (nói với Olivy), ハチロク09 2159/2230 (cảnh hội đồng), ハチロク12 2132 (quan sát kỹ thuật, có thể nói với Hachiroku/nhóm; 2128 cùng cảnh đã dùng "tôi"), 凪ふかみ05 1930 (nói về Nagi, nhóm), 凪ふかみ08a 1527/1546 (nói với Nagi), 凪ふかみ08c 1848/1849/2264/2435 (nói với Nagi+Fukami / gia đình các em), 日々姫01 1757 (nói với Hibiki), 日々姫05 1525/2334 (nói với Hibiki), 日々姫07 1668/1812 (nói với Hibiki), 日々姫07姉 2098 (nói với Hibiki), 日々姫09 1725/1865 (Hibiki), 日々姫13 1456/1504 (nói với Hibiki) + 1378 (người nghe KHÔNG xác định được — cảnh tranh luận, Kisaki+Hibiki đều đang nói; cờ cho coordinator, xem §6), 日々姫14 1945 (nói với Hibiki).

### P5 — GIỮ nguyên (đã kiểm chứng)

**Kisaki03 (lr稀咲追加03):** 633 ("em ấy" = Nagi, ngôi thứ ba), 896 (audit "em" — đã xác nhận đúng, thân mật/tự giễu), 940 (audit "tôi" — đã xác nhận giữ, quyết đoán), 973 ("chúng tôi" số nhiều), 1007 (audit "em" — đã xác nhận), 1023 ("Tôi hiểu rồi" — bàn công việc), 1026 (audit "em" — đã xác nhận), 1053 ("Tôi cũng có ấn tượng…" — bàn về tính bảo thủ của ngành đường sắt, công việc), 1057 ("Ufufu, hôm qua lúc nhận phòng, tôi cũng có cùng cảm nhận…" — ấn tượng nhận phòng thông thường, trung tính, không thân mật/dễ tổn thương), 1189 ("Em và cậu…" — "em" đã đúng, thân mật), 1194 ("Tôi cũng nghĩ vậy" — chuyến công tác), 1216 (trấn an hành lý thông thường — trung tính, nhánh "em" không kích hoạt), 1247/1368/1403 ("em" = người nghe/Suika, ngôi thứ hai), 1412 ("Tôi không rành…" — bàn kinh doanh). Các dòng JP ボク không có đại từ tự xưng số ít: 953/969/1021/1183/1314 (đều "chúng ta" số nhiều).

**稀咲02:** 1674 GIỮ "tôi" (giật mình vì lửa lò — phản ứng tình huống trong chuyến thăm lò, không phải thân mật; đối lập 2067 ngượng ngùng → "em"), 1702 ("tôi định lát nữa bàn xong chuyện sẽ ăn tạm" — công việc), 2065 ("Điều tôi đang nghĩ đến là…" — chứng khoán hóa, công việc), 2080/2081 (suy ngẫm công việc), 2099 GIỮ "tôi" (câu hỏi phân tích "Tôi đã kích thích Soutetsu như thế nào?" — thảo luận phản tư), 2101/2105/2118 ("tôi phải đền đáp bằng công việc" — công việc), 2133 GIỮ "tôi" (xin anh dạy về đường sắt ngày mai — ấm áp nhưng chủ đề công việc, không phơi bày cảm xúc; lưu ý "anh" ở đây là キミ → cờ P6, xem §6), 2233 (phân tích kinh doanh), 2286 ("không phải là tôi" — thảo luận công việc, ai đã kích thích Soutetsu; lưu ý "anh" là キミ → cờ P6), 2297 (phân tích phản tư "thứ tôi cảm nhận được là dục vọng" — thẳng thắn nhưng mang tính phân tích, không phơi bày trong khoảnh khắc), 2345 (giờ làm việc/việc cá nhân — công việc). Các dòng còn lại trong 28 ứng viên đã rà: "tôi" đúng trong bàn luận công việc, hoặc "em ấy" là ngôi thứ ba (= Hibiki).

## §5. Quyết định các mục (theo ủy quyền của Hieu)

- **P1 (quyết 22/11):** Soutetsu tự xưng với Kisaki → "Tôi" toàn dự án. **47 dòng đổi** (18 h2 + 4 lr稀咲追加h + 13 稀咲01 + 4 稀咲03 + 3 日々姫10 + 3 Grand06 + 2 tsuika theo P4). Trong đó 4 dòng GHÉP trên fix đã gộp (h2 933/1334 trên U8; tsuika01 1488 + tsuika02 1084 trên U7b) — chỉ đổi token mới, không cộng lại dòng. Nguyên tắc quyết: chỉ sửa khi người nghe xác định được là Kisaki (1-on-1, hỏi–đáp trực tiếp, hoặc "em/cô" = Kisaki trong cùng dòng); GIỮ khi người nghe xác định được là người khác hoặc thực sự là nhóm/hỗn hợp (tiền lệ giữ-có-lý-do của U6).
- **P5 (quyết 22/11):** Kisaki tự xưng theo ngữ cảnh. **5 dòng đổi:** 稀咲02 1900/2067/2068/2339 → "em" (thân mật/dễ tổn thương); Kisaki03 906 "Em ấy" → "Em" (sửa hình thức ngôi thứ ba thành ngôi thứ nhất thân mật). Các dòng còn lại đã rà đều giữ (xem §4).
- **Quyết 1488/1084 theo P4, không phải P1:** hai dòng này là Kisaki gọi Soutetsu (JP chủ ngữ 双鉄), không phải Soutetsu tự xưng; đổi "Anh" trần → "Soutetsu" theo hướng U8 F-P3-1 đã đề xuất. Chỉ đổi câu 2 ở mỗi dòng (câu 1 đã có tên "Soutetsu" — đổi nữa sẽ lặp tên). Các dòng "anh" trần khác của Kisaki (vd. 稀咲01 1822, 1992; 稀咲03 2141, 2145) KHÔNG sửa trong batch này — cần quyết chung, xem §6.

## §6. Cờ cho coordinator

- **F-U16-1 (P4-adjacent, cần quyết chung — ứng viên U15):** các dòng "anh" trần Kisaki→Soutetsu mà U7b để lại: 稀咲01 1822 ("Anh có hay dùng không?"), 1992 ("Không, anh bảo là thảo luận tốt á." — Kisaki trích lời Soutetsu), 稀咲03 2141 ("Anh đang nói lời yếu đuối gì vậy, Soutetsu."), 2145 ("quan hệ giữa tôi và anh mà"), cộng 8 dòng dạng tên tách của U7b F-P4-1 ("Anh, Soutetsu" / "Anh Sou, tetsu") và các dòng "anh" trần khác U7b để lại (lr稀咲追加h 1000/1104/1307/1815).
- **F-U16-2 (P6 còn sót, ngoài phạm vi U16 — ứng viên U15):** Kisaki キミ "anh"→"cậu" chưa sửa: Grand06 2507 ("anh đều có ý thức tăng thời gian gặp riêng…"), 稀咲02 2133 ("Ngày mai anh sẽ dạy cho tôi…"), 稀咲02 2286 ("tạo ra cơ hội cho anh").
- **F-U16-3:** 稀咲03 2038 "Cảm ơn anh rất nhiều về quỹ My Rail kỳ 1" — "anh" được cảm ơn là ngôi thứ hai, người nghe chưa xác định (P4-adjacent).
- **F-U16-4 (ranh giới địa chỉ nhóm):** nếu coordinator muốn thống nhất các câu họp thành "tôi" (tranh luận do Kisaki dẫn dắt), các ứng viên: 稀咲01 1649/1655, 1799/1800, 1988/1989; 稀咲03 1974, 2135; 日々姫10 2651, 2737, 2895; 日々姫13 1378 (người nghe không xác định được).
- **F-U16-5 (giọng narration):** Soutetsu narration dùng "anh" (lrれいな追加02 1505 "Anh cảm thấy rằng…", 1692 "Anh có cảm giác…" — audit đã giữ). Ngoài phạm vi P1 (đối thoại); cần quyết chung có thống nhất narration thành "tôi" không.
- **F-U16-6:** h2 1265 — JP dùng ボク katakana trong dòng 双鉄H (dị thường); TW xác nhận người nói nam. Đã ghi chú, không đổi fix.
- **F-U16-7:** Kisaki03 906 — U8 §5 O2 đã xác nhận "em đúng" nhưng văn bản thực tế là "Em ấy" (ngôi thứ ba); U16 sửa hình thức thành "Em". Coordinator xác nhận việc hiệu chỉnh phán đoán U8 này.
- **F-U16-8 (kiểm tra chồng lấn U15a/U15b):** đã đối chiếu 52 dòng của batch với phạm vi hai batch chạy song song (U15a §4 gloss + moan leftovers; U15b flags sweep) — không có (file,key) nào trùng (không dòng nào là gloss/moan). Nếu U15 chạm cùng key, coordinator ghép lúc gộp.
- **F-U16-9 (bản đồ ưu tiên):** tổng cặp audit 9.242 vs con số hợp nhất 9.190 (chênh nhỏ, có thể do trùng lặp nhóm duplicate); 3 file audit/moan có 0 fix entry đã bỏ qua (audit-00common-matsubi, audit-obasan, moan-lr-hibikih1-kagami-no-naka-hibiki).
- **F-U16-10 (bài học liệt kê):** regex `\b` trên giá trị JSON thô bỏ sót đại từ sau `\n` dạng chữ — xem §2. Các batch sau nên chuẩn hóa `\n` → khoảng trắng trước khi dùng regex ranh giới từ.

## §7. Lượt soát 2 (bắt buộc — đọc lại toàn bộ fix đối chiếu JP)

**52/52 tái kiểm chứng, 0 loại, 0 sửa.** Đọc lại từng fix đối chiếu JP (kèm TW và cửa sổ đối thoại đã đọc ở §3): mọi "anh"→"tôi" đều khớp JP 僕/ボク ngôi thứ nhất của Soutetsu với Kisaki là người nghe; hai dòng tsuika đổi đúng câu 2 theo P4 (JP chủ ngữ 双鉄); bốn dòng P5 đổi đúng nhánh thân mật (1900 vui vì anh lo cho chế độ ăn; 2067/2068 lắp bắp ngượng ngùng trong bồn tắm; 2339 JP tự ghi 業務を抜きに; 906 JP ボク ngôi thứ nhất, sửa "Em ấy" ngôi thứ ba thành "Em"). Không dòng nào phải loại hay sửa sau lượt soát 2. Kiểm chứng máy: JSON 52 mục (8 trường, key dạng chuỗi, jp/tw khớp CSV3 modulo U+3000, old_vn khớp bản đồ ưu tiên, 0 fix==old_vn, 0 newline thực, 0 `\\n` kép); 10 khối TOML / 52 key parse lại bằng tomllib, mọi giá trị bằng đúng fix trong JSON.

## §8. Khối TOML (parse-verified)

### 稀咲h2_プライベートルーム.txt.toml

```toml
[script]
"912" = "「A――ờ――………… ừm.\\nTôi không nhận ra là hơi thở hay nét mặt của mình đã thay đổi đâu」"
"915" = "「――Em cố tình, cho tôi xem sao?」"
"932" = "「……Mặc dù đã cất công dạy cho tôi」"
"933" = "「……Nghe cô nói vậy thì――\\nCó lẽ tôi đúng là có khuynh hướng như thế thật」"
"1207" = "「Ừm――tôi cũng đến giới hạn rồi」"
"1226" = "「Ừm, tôi muốn đưa vào.\\nĐến mức muốn tráo đổi ngón tay đó với dương vật của tôi luôn」"
"1230" = "「Ừm, Kisaki――tôi ra, đây」"
"1233" = "「Ừm, tôi muốn.\\nMãnh liệt và điên cuồng hơn nhiều so với những gì Kisaki đang tưởng tượng đấy」"
"1236" = "「Hừm? Căn phòng này phản chiếu con người tôi sao?」"
"1265" = "「Vậy thì tôi cũng thế.\\nTôi muốn cùng nhau ra. Hãy làm cho tôi ra đi」"
"1271" = "「Tivi thì xem ở phòng khách là được rồi. Tôi cũng từng nói với chị Mayami như vậy,\\nnhưng chị ấy cứ nằng nặc ép tôi nhận với lý do 『Có trong phòng thì sẽ tiện hơn mà』」"
"1273" = "「Theo những gì tôi nhớ thì chưa từng có ai cả.\\nĐây là sân sau, cũng không phải là nơi nhân viên thường đi lại」"
"1275" = "「Mang phong cách của tôi, là sao?」"
"1278" = "「Tôi đã biết cách làm rồi. Chỉ cần nghĩ về Kisaki, thì bất cứ lúc nào,\\nchắc chắn tôi cũng có thể tự mình ra được」"
"1302" = "「Vậy sao? Tôi hoàn toàn không nhận ra đấy」"
"1313" = "「Để thu hút ánh nhìn……\\nđể quyến rũ tôi――sao?」"
"1321" = "「Nhưng, hiện tại chúng ta đang ở cùng nhau. Tôi muốn làm cho Kisaki ra, và tôi cũng muốn Kisaki\\nlàm cho tôi ra. Như thế, sẽ tốt hơn là thủ dâm」"
"1334" = "「Kisaki――Nếu ra, tôi muốn ra cùng cô」"
```

### lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml

```toml
[script]
"1229" = "「Chúng ta hãy làm tình hết lần này đến lần khác nhé.\\nCho đến khi em mang thai đứa con của chúng ta. Bởi vì tôi cũng mong muốn điều đó.」"
"1287" = "「Tôi hiểu rồi.\\nCho đến khi em thỏa mãn, tôi sẽ không rút ra, cũng không cử động.」"
"1290" = "「Tuân lệnh. Tôi sẽ rửa nhũ hoa cho em thật cẩn thận.」"
"1317" = "「Nếu nói vậy thì, tôi mới là người phải cảm ơn.」"
```

### 稀咲01_金と人.txt.toml

```toml
[script]
"1499" = "「Không. Bản thân tôi ít khi tính nhẩm.\\nDùng máy tính vẫn chắc chắn hơn.」"
"1503" = "「Xin lỗi vì thái độ lúc nãy của tôi. Chưa hiểu rõ ý nghĩa thực sự trong lời nói của em,\\nchỉ nghe nói tiền quan trọng, tôi đã hiểu lầm em là một kẻ hám tiền.」"
"1514" = "「Không, hồi đại học tôi có một người bạn giỏi toán――\\ntôi học được từ cậu ấy thôi.」"
"1515" = "「Không, ý tôi không phải là những bữa ăn sang trọng――mà là những bữa cơm gia đình cơ.\\nVí dụ như rau củ hầm, rong biển Hijiki chẳng hạn.」"
"1559" = "「Tôi không nghĩ em cần phải xin lỗi đâu.\\nThực tế thì, chúng ta đã có một cuộc thảo luận rất tốt mà.」"
"1611" = "「Pizza mà dễ ăn á?\\nTôi thấy nó khó ăn mới đúng……」"
"1753" = "「Tôi mong rằng chúng ta không chỉ dừng lại ở việc bảo vệ quan điểm của mình,\\nmà có thể có một cuộc thảo luận thực sự mang lại kết quả.」"
"1796" = "「Tôi tin chắc là vậy. Dù không có ảnh hưởng ngay lập tức\\nnhưng dần dần, chắc chắn sẽ xảy ra.」"
"1810" = "「Xin lỗi. Tự nhiên tôi thấy tò mò thôi.」"
"1828" = "「Chắc là vậy. Tôi cũng có lúc phải\\nnhờ ngân hàng xử lý tiền thuế hay tiền bảo hiểm.」"
"1863" = "「Không sao. Tôi không kén chọn đâu. Tùy em quyết định.」"
"1945" = "「Thêm vào đó, Houshou Kisaki――còn có được sự giúp đỡ của em nữa.\\nNếu nói về được mất, tôi nghĩ điểm số của chúng ta còn cao hơn đấy.」"
"2002" = "「Vậy để tôi sửa lại là 『Trong trường hợp của tôi, dùng máy tính chắc chắn hơn』.\\nNếu tính nhẩm, có lẽ tôi sẽ mắc lỗi gấp mười lần lỗi nhập liệu mất.」"
```

### 稀咲03_純白のレール.txt.toml

```toml
[script]
"1335" = "「——Tôi không muốn đón nhận một tương lai như thế.\\nTôi chỉ nghĩ đến điều đó một cách sâu sắc thôi.」"
"1932" = "「Cho tôi một miếng nhé.」"
"1938" = "「Tôi làm sao thế?」"
"1999" = "「Không đâu, tôi đã liên lạc trước rồi mà. Cất công từ Sendai đến tận đây, tôi mới là người phải xin lỗi.」"
```

### 日々姫10_稀咲の未来図、日々姫の未来図.txt.toml

```toml
[script]
"2450" = "「À, cái đó thì tôi hiểu.\\nCòn sa bàn——là mô hình này sao?」"
"2587" = "「Tôi nghĩ vậy——\\nvà tôi cũng tin rằng thực ra ai cũng hiểu điều đó.」"
"2653" = "「Là do tôi thiếu chu đáo.\\nTôi xin lỗi.」"
```

### グランドリライト06_稀咲.txt.toml

```toml
[script]
"2238" = "「Rất tiếc, đúng là vậy.\\nTôi nghe nói đường ray để thay thế giờ cũng rất khó kiếm.」"
"2445" = "「Chắc chắn là vậy. Miễn là đường ray được kết nối.\\nTôi nghe nói vận chuyển hàng hóa nặng với số lượng lớn chính là khởi điểm và thế mạnh của đường sắt.」"
"2510" = "「Tất nhiên là được. Nhưng――trong lĩnh vực đó,\\ntôi có thể giúp gì được cho Kisaki sao?」"
```

### lr稀咲追加01_仲国視察の誘い.txt.toml

```toml
[script]
"1488" = "「Chỉ là một phần nhỏ của sự chuẩn bị thôi. Soutetsu thuộc tuýp người hay nảy ra ý tưởng bất chợt mà.\\nSoutetsu có thể biến những tình huống ngoài dự kiến thành cơ hội phát triển.」"
```

### lr稀咲追加02_仲国視察.txt.toml

```toml
[script]
"1084" = "「Anh đang bị vòng luẩn quẩn 'con gà hay quả trứng có trước' rồi đấy? Soutetsu.\\nSoutetsu đang định giải thích cho tôi giới hạn kiến trúc là gì cơ mà.」"
```

### 稀咲02_新事業案.txt.toml

```toml
[script]
"1900" = "「A——Fufu, gì chứ,\\nhóa ra anh lại lo lắng cho chế độ ăn uống của em đến thế sao.」"
"2067" = "「T, t, em mà căng thẳng á!? L, làm gì, có chuyện đó.\\nT, em đã đồng ý, rồi mới vào mà——hoàn toàn, kh, không sao cả.」"
"2068" = "「T, em hiểu rồi.」"
"2339" = "「Một sự tham lam như vậy thật tuyệt vời.\\nBỏ qua công việc sang một bên, em cũng bất giác muốn ủng hộ anh rồi đấy.」"
```

### lr稀咲追加03_新事業案.txt.toml

```toml
[script]
"906" = "「Cũng giống như việc tình tứ về mặt thể xác.\\nEm nhé, cũng rất thích việc tình tứ về mặt logic nữa.」"
```

## Kết bài

- **Đã quyết (2 mục): P1** — Soutetsu tự xưng với Kisaki → "Tôi": **47 dòng** (h2 18, lr稀咲追加h 4, 稀咲01 13, 稀咲03 4, 日々姫10 3, Grand06 3, tsuika 2 theo P4); trong đó 4 dòng GHÉP trên fix đã gộp (h2 933/1334 trên U8, tsuika01 1488 + tsuika02 1084 trên U7b). **P5** — Kisaki tự xưng theo ngữ cảnh: **5 dòng** → "em" (稀咲02 1900/2067/2068/2339; Kisaki03 906 "Em ấy"→"Em").
- **Dòng mới cộng vào chuỗi: 48** (52 dòng chạm − 4 dòng GHÉP). Tổng sau đợt này: **162 mục / 2.779 dòng** (cơ sở 160 mục / 2.731 dòng + 2 mục / 48 dòng mới).
- **GIỮ (có lý do, xem §4):** P1 — h2 1295 (lời trích dẫn); nhóm/không xác định được (稀咲01 1649/1655, 1799/1800, 1988/1989; 稀咲03 1974, 2135; 日々姫10 2593/2651/2737/2895; 日々姫13 1378); người nghe là Hibiki/Paulette/Reina/Olivy/Nagi/Fukami/Michiko (nhiều dòng, liệt kê §4); "anh Urakami"/"anh ấy" ngôi thứ ba; narration không người nghe (lrれいな追加02 1505/1692). P5 — mọi dòng Kisaki03/稀咲02 còn lại: "tôi" đúng trong bàn luận công việc (1053/1057/1194/1216/1412, 1702/2065/2080/2081/2099/2133/2233/2286/2297/2345…), "em" đã đúng ở nhánh thân mật (896/1007/1026/1189), số nhiều "chúng ta" (953/969/1021/1183/1314/973), "em ấy"/"em" ngôi thứ hai/thứ ba (633/1247/1368/1403).
- **Cờ cho coordinator (10 cờ, xem §6):** F-U16-1 "anh" trần Kisaki→Soutetsu còn lại (1822/1992/2141/2145 + F-P4-1); F-U16-2 P6 còn sót (Grand06 2507, 稀咲02 2133/2286); F-U16-3 稀咲03 2038; F-U16-4 ranh giới địa chỉ nhóm; F-U16-5 giọng narration dùng "anh"; F-U16-6 h2 1265 (JP ボク katakana); F-U16-7 hiệu chỉnh xác nhận U8 O2 ở Kisaki03 906; F-U16-8 không trùng (file,key) với U15a/U15b; F-U16-9 caveat bản đồ ưu tiên; F-U16-10 bài học regex `\n`.
- **Lượt soát 2: 52/52 tái kiểm chứng, 0 loại, 0 sửa.** Nguồn old_vn: CSV3 42 / audit 6 / unification đã gộp 4.
