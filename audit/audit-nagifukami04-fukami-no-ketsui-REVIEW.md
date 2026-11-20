# Audit — 凪ふかみ04_ふかみの決意.txt.toml (07_Nagi_Fukami)

- File: `凪ふかみ04_ふかみの決意.txt.toml` — route 07_Nagi_Fukami, 1 bản duy nhất.
- Disk: `sources/toml2/translation_toml/07_Nagi_Fukami/#U51ea#U3075#U304b#U307f04_#U3075#U304b#U307f#U306e#U6c7a#U610f.txt.toml`
- md5: `cb4cdb1d355ee5b597970e389848a97d` — không có file trùng (file 04 chỉ xuất hiện 1 lần trong thư mục 07_Nagi_Fukami; không nằm trong 11 nhóm trùng của dự án).
- Nội dung: ngày đầu tiên Fukami làm nhân viên nhà ga ở Ohitoyo — buổi sáng làm nhiệm vụ cùng Soutetsu và Nagi, học việc, dọn nhà vệ sinh và bàn chuyện “nhìn nhà vệ sinh là biết nhà ga”, chiếc ghế đá bên bờ biển Yatsushiro, hồi tưởng chuyến đi đường sắt Mikan, Fukami xin được trở thành “người đồng đội thực sự của đường sắt Ohitoyo — trưởng tàu!”, kết bằng độc thoại về việc muốn bước vào chữ “chúng ta” của Soutetsu và Nagi.
- Phương pháp: đọc từng dòng 474/474 đối chiếu JP + TW (CSV3), kiểm chứng sweep gasp, kiểm tra %l, kiểm tra trùng khóa / lệch dòng / mồ côi / chưa dịch / nhiễm chéo.

## 1. Tổng quan

- Dòng script: **474** (độc thoại 151, Fukami 149, Soutetsu 44, Nagi 43, Hibiki 29, Reina 28, Paulette 21, ông già 4, nhân viên công ty 2, trẻ em 2, ông chú 1).
- CSV3: 1 set duy nhất, 474 khóa, 0 trùng khóa, 0 VN trống. TOML parse được, 474 khóa khớp CSV3 tuyệt đối về khóa; VN trong TOML khớp CSV3 tuyệt đối (0 lệch, kể cả dạng làm phẳng `\n` — file này không có dòng nào bị TOML-2 làm phẳng).
- `[selections]`: rỗng `{}`. Thẻ `%l`: đúng định dạng, không thiếu dấu `;` đóng; 1 thẻ có trong TW + VN nhưng vắng trong JP (2451 — giữ, xem §5); 2 gloss “Kiha 07S” đã sửa thành “KiHa 07S” (3101, 3131).
- **Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.**

## 2. Kết quả: 94/474 (19,8%)

Phân loại (94):

- Đại từ: **79** — độc thoại Fukami tôi/em→mình 67; đối thoại 12 (Fukami tự xưng “chị” sai 4: 2137, 2143, 2165, 2240; Fukami “em” với Nagi 2: 2158, 2178; nhóm “bọn chị”/“bọn em” sai 3: 2262, 2438, 2478; Fukami “em” với Reina 2: 2442, 2514; nhất quán trong dòng 1: 2622).
- Thuật ngữ (đã quyết trong dự án): **13** — Ohito→Ohitoyo 7 dòng / 8 lần (2086 ×2, 2111, 2221, 2283, 2416, 2433, 2569); 定期券 “vé tháng”→“vé định kỳ” 3 (1526, 2499, 2572); 凪さま “Nagi này”→“bổn tiểu thư này” 1 (2460); まいてつ “giới đường sắt”→“giới chủ tàu” 1 (2664); gloss “Kiha”→“KiHa” 1 (3101; 3131 gộp trong dòng đại từ).
- Dịch sai nghĩa: **2** — 2596 (bịa thêm “ảnh hưởng”), 3296 (mất chuyển chủ ngữ).

13 dòng thuật ngữ sửa trực tiếp trong audit (theo tiền lệ ハチロク03/ハチロク07/ハチロク09_採決) — KHÔNG thêm lại các key này vào hàng đợi thống nhất.

## 3. Danh sách sửa (94)

### 3.1. Thuật ngữ

**Key 1526 [monologue] — terminology.** JP: `……ポーレットさん、お会計しながらも、\\n他のお客さんのきっぷを受け取って、定期券も見てる。` / TW: `……波萊特小姐一邊算帳，一邊接過其他乘客的車票，同時還認真檢查了定期票。` — Cũ: `...Chị Paulette, vừa thanh toán,\\nvừa nhận vé của khách khác, vừa kiểm tra vé tháng nữa.` → Mới: `...Chị Paulette, vừa thanh toán,\\nvừa nhận vé của khách khác, vừa kiểm tra vé định kỳ nữa.`. (定期券 = “vé định kỳ” (đã quyết; “vé tháng” là cách gọi khác, không đúng thuật ngữ dự án).)

**Key 2086 [双鉄] — terminology.** JP: `「念のためですが、御一夜鉄道[ゆのいせん,2]湯医線には、\\n現在、御一夜と湯医の二駅しかありませんので――」` / TW: `「先向您確認一下，御一夜鐵路湯醫線現在只有御一夜和湯醫兩個站點——」` — Cũ: `「Để chắc chắn thì, tuyến Yunoi của đường sắt Ohito,\\nhiện tại chỉ có hai ga là Ohito và Yunoi thôi ạ——」` → Mới: `「Để chắc chắn thì, tuyến Yunoi của đường sắt Ohitoyo,\\nhiện tại chỉ có hai ga là Ohitoyo và Yunoi thôi ạ——」`. (御一夜 = “Ohitoyo” (đã quyết; “Ohito” là dạng cũ). Một dòng mang 2 lần Ohito (đường sắt + ga).)

**Key 2111 [双鉄] — terminology.** JP: `「道場だ。御一夜の町の、剣道場」` / TW: `「到她去道場的時間了，御一夜的劍道道場」` — Cũ: `「Đạo đường. Đạo đường kiếm đạo ở thị trấn Ohito」` → Mới: `「Đạo đường. Đạo đường kiếm đạo ở thị trấn Ohitoyo」`. (御一夜 = “Ohitoyo” (đã quyết).)

**Key 2221 [ポーレット] — terminology.** JP: `「あ！　それいい！　うん。ふかみちゃんに、\\n御一夜鉄道沿線の魅力、もう一度チェックしてもらって」` / TW: `「啊！　好主意！　嗯，讓小深再發掘一次御一夜鐵路沿線的魅力」` — Cũ: `「A! Ý hay đấy! Ừ. Nhờ Fukami\\nkiểm tra lại sức hấp dẫn dọc tuyến đường sắt Ohito một lần nữa」` → Mới: `「A! Ý hay đấy! Ừ. Nhờ Fukami\\nkiểm tra lại sức hấp dẫn dọc tuyến đường sắt Ohitoyo một lần nữa」`. (御一夜 = “Ohitoyo” (đã quyết).)

**Key 2283 [れいな] — terminology.** JP: `「うふふぅ、ふかみさん、すごいですねぇ。\\nね、ポーレットぉ、御一夜鉄道にもし、次の観光列車が」` / TW: `「嘿嘿，小深，你可真厲害。波萊特，如果御一夜鐵路下次再新增觀光列車……」` — Cũ: `「Ufufu, chị Fukami, giỏi quá đi.\\nNày chị Paulette, nếu đường sắt Ohito có chuyến tàu du lịch tiếp theo」` → Mới: `「Ufufu, chị Fukami, giỏi quá đi.\\nNày chị Paulette, nếu đường sắt Ohitoyo có chuyến tàu du lịch tiếp theo」`. (御一夜 = “Ohitoyo” (đã quyết).)

**Key 2416 [ふかみ] — terminology.** JP: `「だから、わたしを――御一夜鉄道のほんとの仲間に。\\n――車掌さんに！　してくださいっ！！！」` / TW: `「所以請讓我真正成為御一夜鐵路的一員。——讓我成為一名列車長吧！！！」` — Cũ: `「Vì thế, xin hãy cho em——trở thành một người đồng đội thực sự của đường sắt Ohito.\\n——Trở thành trưởng tàu! Đi ạ!!!」` → Mới: `「Vì thế, xin hãy cho em——trở thành một người đồng đội thực sự của đường sắt Ohitoyo.\\n——Trở thành trưởng tàu! Đi ạ!!!」`. (御一夜 = “Ohitoyo” (đã quyết).)

**Key 2433 [ふかみ] — terminology.** JP: `「でしょ？　だから、誰か一人の力でじゃなくて。\\n御一夜鉄道で――組織で改善していくべきって思うの」` / TW: `「是吧？　所以我覺得不能只靠某一個人的努力，而是要靠御一夜鐵路改善整個組織架構」` — Cũ: `「Đúng không? Vì vậy, không phải chỉ dựa vào sức của một người.\\nMà đường sắt Ohito——phải cải thiện vấn đề này với tư cách là một tổ chức」` → Mới: `「Đúng không? Vì vậy, không phải chỉ dựa vào sức của một người.\\nMà đường sắt Ohitoyo——phải cải thiện vấn đề này với tư cách là một tổ chức」`. (御一夜 = “Ohitoyo” (đã quyết).)

**Key 2460 [凪] — terminology.** JP: `「そうばい！　そしたらきっと凪さま！\\nふかみちゃんに、もっと綺麗な景色ば見せるけん！」` / TW: `「是嘞！　到時候本小姐一定會讓你看到更漂亮的景色！」` — Cũ: `「Đúng vậy! Nếu thế thì chắc chắn Nagi này!\\nSẽ cho Fukami thấy những cảnh sắc đẹp hơn nữa!」` → Mới: `「Đúng vậy! Nếu thế thì chắc chắn bổn tiểu thư này!\\nSẽ cho Fukami thấy những cảnh sắc đẹp hơn nữa!」`. (凪さま = “Bổn tiểu thư” (tiền lệ 凪ふかみ01: 8 dòng 凪さま→“Bổn tiểu thư”); “Nagi này” làm mất sắc thái tự xưng trang trọng của Nagi.)

**Key 2499 [ポーレット] — terminology.** JP: `「[ゆのい,1]湯医からの片道で、690円になります。\\n定期券の更新は、レールショップでおねがいします」` / TW: `「湯醫到御一夜單程６９０日元。請您到鐵路商店給定期票續期」` — Cũ: `「Vé một chiều từ Yunoi là 690 yên ạ.\\nQuý khách vui lòng gia hạn vé tháng ở Cửa hàng đường sắt nhé」` → Mới: `「Vé một chiều từ Yunoi là 690 yên ạ.\\nQuý khách vui lòng gia hạn vé định kỳ ở Cửa hàng đường sắt nhé」`. (定期券 = “vé định kỳ” (đã quyết).)

**Key 2569 [双鉄] — terminology.** JP: `「あちらに渡りまして、レールショップで、\\n『御一夜[ひとよ,1]一夜きっぷ』をお求めください」` / TW: `「請到那邊的鐵路商店購買“御一夜一夜車票”」` — Cũ: `「Bà đi qua bên kia, đến Cửa hàng đường sắt,\\nrồi hỏi mua 『Vé Ohito Một Đêm』 nhé」` → Mới: `「Bà đi qua bên kia, đến Cửa hàng đường sắt,\\nrồi hỏi mua 『Vé Ohitoyo Một Đêm』 nhé」`. (御一夜一夜きっぷ = “Vé Ohitoyo Một Đêm” (御一夜 = “Ohitoyo”).)

**Key 2572 [ポーレット] — terminology.** JP: `「ありがとうござ――あ！\\nお客様？　定期券の期限が」` / TW: `「謝謝……哎呀，這位乘客，　您的定期票到期了」` — Cũ: `「Cảm ơn quý kh——a!\\nQuý khách ơi? Vé tháng của quý khách hết hạn rồi ạ」` → Mới: `「Cảm ơn quý kh——a!\\nQuý khách ơi? Vé định kỳ của quý khách hết hạn rồi ạ」`. (定期券 = “vé định kỳ” (đã quyết).)

**Key 2664 [ポーレット] — terminology.** JP: `「バーベキュー客車の改装、まいてつ界隈で評判なの。\\nそれで、よろしければ是非デザインをっていうことで」` / TW: `「ＢＢＱ列車的改造在掌車人之間很受好評。所以對方就來請我們幫忙設計一下」` — Cũ: `「Việc cải tạo toa hành khách BBQ đang rất nổi tiếng trong giới đường sắt đấy.\\nThế nên họ mới ngỏ ý nhờ chúng ta thiết kế giúp」` → Mới: `「Việc cải tạo toa hành khách BBQ đang rất nổi tiếng trong giới chủ tàu đấy.\\nThế nên họ mới ngỏ ý nhờ chúng ta thiết kế giúp」`. (まいてつ界隈 = “giới chủ tàu” (まいてつ = “chủ tàu” đã quyết; TW 掌車人 “người chủ tàu” xác nhận; “giới đường sắt” làm mất nghĩa chuyên ngành).)

**Key 3101 [monologue] — terminology.** JP: `いた、ポーレットさん。\\n\x%lキハ07s;#00ffc040;キハ07s%l;#;、ちょうど戻ってきたとこみたい。` / TW: `找到她了。\x%lキハ07s;#00ffc040;Ｋｉｈａ０７Ｓ%l;#;似乎剛好到站。` — Cũ: `Thấy rồi, chị Paulette.\\n\x%lキハ07s;#00ffc040;Kiha 07S%l;#;, có vẻ vừa mới quay lại.` → Mới: `Thấy rồi, chị Paulette.\\n\x%lキハ07s;#00ffc040;KiHa 07S%l;#;, có vẻ vừa mới quay lại.`. (Gloss %l: “KiHa” là cách viết chính thức (JR) đã quyết; “Kiha” sai chính tả trong thẻ chú giải.)

### 3.2. Đại từ — đối thoại

**Key 2137 [ふかみ] — pronoun.** JP: `「えと……だってそれ――うちのお仕事。\\nクマ川くだりでも、結構、おんなじことかも、だから」` / TW: `「呃……因為這和我家的生意——隈河漂流，有很多共同點」` — Cũ: `「Ờm... vì đó——cũng là công việc nhà chị.\\nChèo thuyền trên sông Kuma cũng khá giống vậy, nên là」` → Mới: `「Ờm... vì đó——cũng là công việc nhà mình.\\nChèo thuyền trên sông Kuma cũng khá giống vậy, nên là」`. (Fukami tự xưng “chị” — sai: Fukami không bao giờ là “chị” của ai trong cảnh này (người nghe là Nagi, cùng tuổi). うちのお仕事 = công việc của nhà mình → “nhà mình”.)

**Key 2143 [ふかみ] — pronoun.** JP: `「ん……と。\\nやっぱり出直した方がいいかな？」` / TW: `「呃……我還是下次再來吧？」` — Cũ: `「Ưm... ờm.\\nHay là chị nên quay lại sau nhỉ?」` → Mới: `「Ưm... ờm.\\nHay là em nên quay lại sau nhỉ?」`. (Fukami tự xưng “chị” — sai (người nghe là Hibiki/Soutetsu, lớn tuổi hơn). Đổi “chị”→“em”.)

**Key 2158 [ふかみ] — pronoun.** JP: `「ひえっ！？　わたっ、わたし、の――\\nわたしの、なにが――さすが――ですっ！？」` / TW: `「咦！？　我……我我我……我哪裡厲害了！？」` — Cũ: `「Hiee!? E, em, thì——\\nem có gì——mà giỏi——ạ!?」` → Mới: `「Hiee!? E, tớ, thì——\\ntớ có gì——mà giỏi——ạ!?」`. (Fukami tự xưng “em” với Nagi — sai: hai người cùng tuổi, bạn bè; trong file Fukami xưng “tớ” với Nagi (2043, 2128). Đổi “em”→“tớ” (2 lần).)

**Key 2165 [ふかみ] — pronoun.** JP: `「え？　わたし、別になにも――」` / TW: `「咦？　我什麼都沒做呀」` — Cũ: `「Hả? Chị có làm gì đâu——」` → Mới: `「Hả? Em có làm gì đâu——」`. (Fukami tự xưng “chị” — sai (người nghe là Hibiki, 2161–2162). Đổi “chị”→“em”.)

**Key 2178 [ふかみ] — pronoun.** JP: `「は……はぅ……\\nそ、そんな……わたっ――」` / TW: `「哇……哪、哪有……我——」` — Cũ: `「Ha... hau...\\nK, không có... em——」` → Mới: `「Ha... hau...\\nK, không có... tớ——」`. (Fukami tự xưng “em” với Nagi (đang đáp lại lời khen của Nagi, 2180) — sai, cùng tuổi. Đổi “em”→“tớ”.)

**Key 2240 [ふかみ] — pronoun.** JP: `「あ、うん。――はい。\\n覚えてる――覚えてます、です」` / TW: `「啊，對……我記得，嗯」` — Cũ: `「A, ừ. ——Vâng.\\nChị nhớ——chị nhớ chứ, ạ」` → Mới: `「A, ừ. ——Vâng.\\nCháu nhớ——cháu nhớ chứ, ạ」`. (Fukami tự xưng “chị” — sai: người nghe là khách lớn tuổi (2237 Fukami gọi “bác”; 覚えてる→覚えてます là lối nói lễ phép với khách). Fukami với người lớn tuổi xưng “cháu”. Đổi “chị”→“cháu” (2 lần).) [Parent 20/11 ~22:05: đã sửa chú thích — từ “ご老人” không có trong file này; bằng chứng là “bác” ở 2237.]

**Key 2262 [ふかみ] — pronoun.** JP: `「うん。海が見えたし――と、そっか。\\nそこから先は、オリヴィちゃんが話しかけてくれたから」` / TW: `「嗯，因為看到了大海嘛。啊，然後奧莉薇就和我們聊起來了」` — Cũ: `「Ừ. Vừa thấy biển——à, đúng rồi.\\nTừ lúc đó trở đi, bé Olivy đã bắt chuyện với bọn chị mà」` → Mới: `「Ừ. Vừa thấy biển——à, đúng rồi.\\nTừ lúc đó trở đi, bé Olivy đã bắt chuyện với bọn tớ mà」`. (Nhóm tự xưng “bọn chị” — sai: nhóm là Fukami + Nagi (cùng tuổi), không ai là “chị”. Đổi “bọn chị”→“bọn tớ” (khớp “Bọn tớ” của Nagi ở 2169).)

**Key 2438 [ふかみ] — pronoun.** JP: `「ですです。[せんだい,1]千内まではエアクラで、\\n千内からも、ずっと列車に乗りっぱなしで――」` / TW: `「是呀是呀。我們先乘空凝機到川內，然後就一直坐在車上——」` — Cũ: `「Đúng rồi ạ. Bọn em đi Aircra đến Sendai,\\nrồi từ Sendai lại cứ ngồi tàu suốt——」` → Mới: `「Đúng rồi ạ. Bọn mình đi Aircra đến Sendai,\\nrồi từ Sendai lại cứ ngồi tàu suốt——」`. (Nhóm tự xưng “Bọn em” — sai: nhóm đi Sendai là Fukami + Soutetsu + Nagi (2359 Hibiki xác nhận cả ba cùng đi); có Soutetsu (“anh”) trong nhóm nên “Bọn em” không bao quát. Đổi “Bọn em”→“Bọn mình” (dạng trung tính).)

**Key 2442 [ふかみ] — pronoun.** JP: `「ですです。だからおトイレ、掃除してよかったです」` / TW: `「是呀是呀，所以打掃一下洗手間挺好的」` — Cũ: `「Đúng vậy ạ. Thế nên em dọn dẹp nhà vệ sinh là đúng rồi」` → Mới: `「Đúng vậy ạ. Thế nên chị dọn dẹp nhà vệ sinh là đúng rồi」`. (Fukami tự xưng “em” — sai: đang đối thoại với Reina (chuỗi ですです 2436–2443); Fukami lớn hơn Reina, xưng “chị” (tiền lệ 2512 “Chị đã hiểu” với Reina). Đổi “em”→“chị”.)

**Key 2478 [ふかみ] — pronoun.** JP: `「例えば、川くだりだと、歌、歌うんです。\\n話してばっかりだと、お客さん聞いてくれなくなるから」` / TW: `「比如漂流的時候就會唱歌。如果光是說話，客人會不耐煩的」` — Cũ: `「Ví dụ như lúc chèo thuyền xuôi dòng, bọn em sẽ hát.\\nCứ nói mãi thì khách sẽ không muốn nghe nữa」` → Mới: `「Ví dụ như lúc chèo thuyền xuôi dòng, bọn mình sẽ hát.\\nCứ nói mãi thì khách sẽ không muốn nghe nữa」`. (Nhóm tự xưng “bọn em” — sai: nhóm hát trên thuyền là đội chèo thuyền Kuma (Fukami + các bác lái đò); “Bọn em” không bao quát các bác lớn tuổi. Đổi “bọn em”→“bọn mình”.)

**Key 2514 [ふかみ] — pronoun.** JP: `「えと、わたしまだ駅のことほとんどわからないし――\\nだからおトイレ、しっかり細かくみたかったから」` / TW: `「畢竟我還不是很了解車站，所以想仔細觀察一下洗手間的情況」` — Cũ: `「Ờm, em vẫn chưa biết gì nhiều về nhà ga——\\nNên em muốn xem xét nhà vệ sinh thật kỹ càng」` → Mới: `「Ờm, chị vẫn chưa biết gì nhiều về nhà ga——\\nNên chị muốn xem xét nhà vệ sinh thật kỹ càng」`. (Fukami tự xưng “em” — sai: đang đối thoại với Reina (2511 Reina cảm ơn Fukami; 2512 Fukami xưng “chị” với Reina ngay trước đó). Đổi “em”→“chị” (2 lần).)

**Key 2622 [ふかみ] — pronoun.** JP: `「だったら、わたし。\\n少しは役にたてるかもって、思います」` / TW: `「那我……應該能幫上一點忙」` — Cũ: `「Nếu vậy thì, em.\\nNghĩ là mình có thể giúp ích được một chút」` → Mới: `「Nếu vậy thì, em.\\nNghĩ là em có thể giúp ích được một chút」`. (Nhất quán đại từ trong dòng: vế đầu “em”, vế sau “mình” — người nghe là Hibiki (2618 Hibiki hỏi Fukami) nên “em” đúng; đổi vế sau “mình”→“em”.)

### 3.3. Đại từ — độc thoại (Fukami tự xưng “mình”)

**Key 1522 [monologue] — pronoun.** JP: `……緑の旗と赤の旗、\\n結局、一度もふらないですんだ。` / TW: `……最後我完全沒有用上手中的綠旗和紅旗。` — Cũ: `...Cờ xanh và cờ đỏ,\\nrốt cuộc tôi chẳng phải phất lần nào.` → Mới: `...Cờ xanh và cờ đỏ,\\nrốt cuộc mình chẳng phải phất lần nào.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2881 [monologue] — pronoun.** JP: `けど……いいたくて、伝えたくって――\\nずっと、あこがれてたことだから。` / TW: `但我一直嚮往著……想要對他們說出這句話。` — Cũ: `Nhưng... tôi muốn nói, muốn truyền đạt——\\nVì đó là điều tôi luôn ao ước.` → Mới: `Nhưng... mình muốn nói, muốn truyền đạt——\\nVì đó là điều mình luôn ao ước.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2882 [monologue] — pronoun.** JP: `だけど、わたしもおんなじ気持ち。\\n１５分なんて、ほんの一瞬――――って、あ！` / TW: `但我也有同感，十五分鐘簡直轉眼就過去了……對了！` — Cũ: `Nhưng mà, tôi cũng có cùng cảm giác.\\n15 phút, chỉ như một cái chớp mắt——ơ, a!` → Mới: `Nhưng mà, mình cũng có cùng cảm giác.\\n15 phút, chỉ như một cái chớp mắt——ơ, a!`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2885 [monologue] — pronoun.** JP: `けど、こんなチャンスって二度とない。\\nいま言わなくちゃ、わたし一生、きっと言えない！` / TW: `但機會僅此一次。如果現在不說，那我一輩子都說不出口了！` — Cũ: `Nhưng, cơ hội thế này sẽ không có lần thứ hai.\\nNếu bây giờ không nói, chắc chắn cả đời này tôi sẽ không thể nói ra!` → Mới: `Nhưng, cơ hội thế này sẽ không có lần thứ hai.\\nNếu bây giờ không nói, chắc chắn cả đời này mình sẽ không thể nói ra!`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2887 [monologue] — pronoun.** JP: `だけど。だから。\\n見えてるものが違うから、わたしが入れる“僕ら”もある。` / TW: `但正因為擁有不同的視野，我也能以另一種方式成為他們的同伴。` — Cũ: `Nhưng. Vì thế.\\nVì nhìn thấy những thứ khác nhau, nên cũng có chữ "chúng ta" mà tôi có thể bước vào.` → Mới: `Nhưng. Vì thế.\\nVì nhìn thấy những thứ khác nhau, nên cũng có chữ "chúng ta" mà mình có thể bước vào.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2888 [monologue] — pronoun.** JP: `いつも綺麗にしておくことが、どれほど大事なことなのか、\\nわたし自身も、体で知ってることだから。` / TW: `保持乾淨整潔有多重要，我對其深有體會。` — Cũ: `Việc luôn giữ gìn sạch sẽ quan trọng đến mức nào,\\nbản thân tôi cũng tự cảm nhận được.` → Mới: `Việc luôn giữ gìn sạch sẽ quan trọng đến mức nào,\\nbản thân mình cũng tự cảm nhận được.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2891 [monologue] — pronoun.** JP: `もしもわたしが話しかけやすい駅員さんなら、\\nどんな質問にだって、ちゃんと答えられるようになりたい。` / TW: `假如乘客們覺得我比較親切，那我應該鞏固一下相關知識，方便解答乘客的疑問。` — Cũ: `Nếu tôi là một nhân viên nhà ga dễ bắt chuyện,\\ntôi muốn mình có thể trả lời thỏa đáng mọi câu hỏi.` → Mới: `Nếu mình là một nhân viên nhà ga dễ bắt chuyện,\\nmình muốn mình có thể trả lời thỏa đáng mọi câu hỏi.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”. “mình muốn mình có thể” giữ nguyên cấu trúc câu, chỉ đổi đại từ.)

**Key 2961 [monologue] — pronoun.** JP: `けど――けど！　みかん鉄道の旅で思って、\\nそれからずっと、しっかり考えてきたこと。……だし。` / TW: `可、可是在橙鐵路的旅行之後，我就一直在認真琢磨這件事。` — Cũ: `Nhưng——nhưng mà! Nghĩ về chuyến đi đường sắt Mikan,\\ntừ lúc đó đến giờ, tôi đã suy nghĩ rất kỹ rồi... cơ mà.` → Mới: `Nhưng——nhưng mà! Nghĩ về chuyến đi đường sắt Mikan,\\ntừ lúc đó đến giờ, mình đã suy nghĩ rất kỹ rồi... cơ mà.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2968 [monologue] — pronoun.** JP: `あ――今、ちょっとだけ胸、ズキってしちゃった。\\n“僕ら”の中に、わたし、ここでは入れないから。` / TW: `啊……胸口忽然刺痛了一下。因為雙鐵哥哥還是沒有把我算進他們中的一員。` — Cũ: `A——vừa nãy, tim tôi hơi nhói lên một chút.\\nVì trong chữ "chúng ta" đó, không có tôi ở đây.` → Mới: `A——vừa nãy, tim mình hơi nhói lên một chút.\\nVì trong chữ "chúng ta" đó, không có mình ở đây.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2972 [monologue] — pronoun.** JP: `だって、クマ川下りがわたしの全部の始まりだから。` / TW: `因為隈河漂流是我一切的起點。` — Cũ: `Vì chèo thuyền trên sông Kuma là khởi đầu cho mọi thứ của tôi mà.` → Mới: `Vì chèo thuyền trên sông Kuma là khởi đầu cho mọi thứ của mình mà.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2974 [monologue] — pronoun.** JP: `川のこと、生態系のことを勉強した時、\\nシステムについても教わった。` / TW: `在學習河流與生態系統的知識時，我也學到了系統的概念。` — Cũ: `Khi học về sông ngòi, về hệ sinh thái,\\ntôi cũng được dạy về hệ thống.` → Mới: `Khi học về sông ngòi, về hệ sinh thái,\\nmình cũng được dạy về hệ thống.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2979 [monologue] — pronoun.** JP: `嬉しい、すごく。\\nみんながわたしを気遣ってくれて。` / TW: `大家都這麼關心我，我好開心。` — Cũ: `Vui quá, thực sự rất vui.\\nMọi người đều quan tâm đến tôi.` → Mới: `Vui quá, thực sự rất vui.\\nMọi người đều quan tâm đến mình.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2985 [monologue] — pronoun.** JP: `ほっとする。\\nちょっと、自信がわいてくる。` / TW: `太好了，這下我就有點自信了。` — Cũ: `Nhẹ nhõm quá.\\nTôi bắt đầu thấy tự tin hơn chút.` → Mới: `Nhẹ nhõm quá.\\nMình bắt đầu thấy tự tin hơn chút.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2988 [monologue] — pronoun.** JP: `ポーレットさんも日々姫さんももう知ってるみたいだけど、\\n一応は、わたしが見たことを全部残らず話しとく。` / TW: `她們倆好像已經知道這件事了，但我還是一五一十將自己的經歷全部說了出來。` — Cũ: `Có vẻ như chị Paulette và chị Hibiki đã biết chuyện rồi,\\nnhưng tôi vẫn kể lại không sót chữ nào những gì mình đã thấy.` → Mới: `Có vẻ như chị Paulette và chị Hibiki đã biết chuyện rồi,\\nnhưng mình vẫn kể lại không sót chữ nào những gì mình đã thấy.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”. Trong dòng đã lẫn “tôi” (vế đầu) và “mình” (vế sau) — thống nhất về “mình”.)

**Key 2994 [monologue] — pronoun.** JP: `それだけでなんだかわかっちゃう。\\nだって……双鉄おにいさんと、凪ちゃんだし。` / TW: `她說到一半我就明白了。畢竟雙鐵哥哥和小凪都是那副性子嘛。` — Cũ: `Chỉ thế thôi là tôi cũng lờ mờ hiểu ra.\\nVì... là anh Soutetsu và Nagi mà.` → Mới: `Chỉ thế thôi là mình cũng lờ mờ hiểu ra.\\nVì... là anh Soutetsu và Nagi mà.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2997 [monologue] — pronoun.** JP: `わたしの好み、\\nレモンティーにして砂糖はなしも、覚えてくれてる。` / TW: `她還記得我喜歡不加糖的檸檬茶。` — Cũ: `Sở thích của tôi,\\ntrà chanh không đường, em ấy cũng nhớ nữa.` → Mới: `Sở thích của mình,\\ntrà chanh không đường, em ấy cũng nhớ nữa.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 2999 [monologue] — pronoun.** JP: `車掌さんになれれば、\\nふたりと一緒にレールの向こうに走っていけるのに。` / TW: `如果成為列車長，就能和他們一起在鐵軌上馳騁了。` — Cũ: `Nếu trở thành trưởng tàu,\\ntôi có thể cùng hai người họ chạy về phía bên kia đường ray.` → Mới: `Nếu trở thành trưởng tàu,\\nmình có thể cùng hai người họ chạy về phía bên kia đường ray.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3003 [monologue] — pronoun.** JP: `クマ川下りがなかったら、\\n凪ちゃんとも、双鉄おにいさんとも会えてないから。` / TW: `如果沒有隈河漂流，我就不會跟小凪和雙鐵哥哥相遇。` — Cũ: `Nếu không có chèo thuyền trên sông Kuma,\\ntôi đã không gặp được Nagi và anh Soutetsu.` → Mới: `Nếu không có chèo thuyền trên sông Kuma,\\nmình đã không gặp được Nagi và anh Soutetsu.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3016 [monologue] — pronoun.** JP: `そうだ、わたし、そのお話を――\\nううん、お願いをしにきたんだった。` / TW: `對了，我是來提這件事的——不，我是來請求她們的。` — Cũ: `Đúng rồi, tôi đến đây là để nói chuyện đó——\\nKhông, là để nhờ vả.` → Mới: `Đúng rồi, mình đến đây là để nói chuyện đó——\\nKhông, là để nhờ vả.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3017 [monologue] — pronoun.** JP: `双鉄おにいさんに、凪ちゃんに、おかあさんやみんなに、\\nとってもとっても失礼だって、わかったから。` / TW: `對雙鐵哥哥、小凪、媽媽以及大家而言，都是一種侮辱。` — Cũ: `Với anh Soutetsu, với Nagi, với mẹ và mọi người,\\nnhư vậy là vô cùng, vô cùng thất lễ, tôi hiểu điều đó.` → Mới: `Với anh Soutetsu, với Nagi, với mẹ và mọi người,\\nnhư vậy là vô cùng, vô cùng thất lễ, mình hiểu điều đó.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3019 [monologue] — pronoun.** JP: `凪ちゃん、抱きついてきてくれる。\\n尻尾をふってる子犬みたいに！` / TW: `小凪一把抱了過來，就像隻搖晃著尾巴的小狗！` — Cũ: `Nagi lao đến ôm chầm lấy tôi.\\nNhư một chú cún con đang vẫy đuôi vậy!` → Mới: `Nagi lao đến ôm chầm lấy mình.\\nNhư một chú cún con đang vẫy đuôi vậy!`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3021 [monologue] — pronoun.** JP: `凪ちゃんはまた、わたしを強くぎゅーってして――\\nそしたら、顔も引き締まる。` / TW: `小凪又用力抱了我一下，然後便擺出一副嚴肅的表情。` — Cũ: `Nagi lại ôm chặt lấy tôi một lần nữa——\\nRồi sau đó, nét mặt em ấy trở nên nghiêm túc.` → Mới: `Nagi lại ôm chặt lấy mình một lần nữa——\\nRồi sau đó, nét mặt em ấy trở nên nghiêm túc.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3023 [monologue] — pronoun.** JP: `凪ちゃんが手を振ってくるから、\\nほとんど条件反射みたいに。` / TW: `小凪將手揮過來，我就條件反射般跟她擊了一下掌。` — Cũ: `Nagi vung tay ra,\\nnên tôi cũng đập tay lại gần như phản xạ có điều kiện.` → Mới: `Nagi vung tay ra,\\nnên mình cũng đập tay lại gần như phản xạ có điều kiện.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3029 [monologue] — pronoun.** JP: `びっくりしちゃう。\\nいきなり後ろから声かけられて――って、あ。` / TW: `小凪突然從身後向我搭話，嚇了我一跳……哎呀。` — Cũ: `Làm tôi giật cả mình.\\nĐột nhiên bị gọi từ phía sau——ơ, a.` → Mới: `Làm mình giật cả mình.\\nĐột nhiên bị gọi từ phía sau——ơ, a.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3067 [monologue] — pronoun.** JP: `わ、わ。どうしよ。\\nいざとなったら、やっぱり、足がすくんじゃう。` / TW: `怎、怎麼辦。事到臨頭我又怯場了。` — Cũ: `Oa, oa. Làm sao đây.\\nĐến lúc quan trọng, quả nhiên chân tôi lại chùn bước.` → Mới: `Oa, oa. Làm sao đây.\\nĐến lúc quan trọng, quả nhiên chân mình lại chùn bước.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3070 [monologue] — pronoun.** JP: `だって、わたし……\\n連れていってもらうだけ――じゃ、ない、の？` / TW: `我……我不就是請她帶我去找波萊特小姐而已嗎？` — Cũ: `Bởi vì, tôi...\\nchỉ là được dẫn đi cùng thôi——mà, nhỉ?` → Mới: `Bởi vì, mình...\\nchỉ là được dẫn đi cùng thôi——mà, nhỉ?`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3074 [monologue] — pronoun.** JP: `『わたしなんて』って言いかけたのを、グって飲み込む。\\nそんなこと言ったら、わたしの大事なひとたちに――` / TW: `我剛要開口貶低自己，又將話咽了回去。如果說出這種話，對我最愛的人們——` — Cũ: `Tôi nuốt ực câu 『Cỡ như em thì』 đang chực trào ra.\\nNếu nói thế, sẽ thật có lỗi với những người quan trọng của tôi——` → Mới: `Mình nuốt ực câu 『Cỡ như mình thì』 đang chực trào ra.\\nNếu nói thế, sẽ thật có lỗi với những người quan trọng của mình——`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”. Cả “Tôi” đầu câu lẫn “Cỡ như em thì” trong ngoặc trích わたしなんて đều là Fukami tự nhủ — đổi về “mình”.)

**Key 3080 [monologue] — pronoun.** JP: `凪ちゃんだから、からかったりなんて絶対してない。\\nけど――` / TW: `我很了解小凪，她當然不是在說假話捉弄我。可是——` — Cũ: `Vì là Nagi nên chắc chắn không phải đang trêu chọc tôi.\\nNhưng——` → Mới: `Vì là Nagi nên chắc chắn không phải đang trêu chọc mình.\\nNhưng——`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3082 [monologue] — pronoun.** JP: `わかった。わたしがした――ううん、\\nいつもと同じにしていたら、結果的にはできてたお仕事。` / TW: `我懂了，只要像以前那樣——不對，像平時一樣就能做好這份工作了。` — Cũ: `Tôi hiểu rồi. Điều tôi đã làm——không,\\nlàm như mọi khi, kết quả là công việc đã hoàn thành.` → Mới: `Mình hiểu rồi. Điều mình đã làm——không,\\nlàm như mọi khi, kết quả là công việc đã hoàn thành.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3084 [monologue] — pronoun.** JP: `おっかないし、恥ずかしい。\\n今さら……って、自分の中でも声が聴こえる。` / TW: `我既緊張又害怕，不好意思開這個口，甚至能感受到心中有另一股想法在勸自己放棄。` — Cũ: `Sợ hãi, và xấu hổ.\\nĐến giờ này rồi còn... một giọng nói vang lên trong tôi.` → Mới: `Sợ hãi, và xấu hổ.\\nĐến giờ này rồi còn... một giọng nói vang lên trong mình.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3086 [monologue] — pronoun.** JP: `そしたら、お話したいのに、\\nあたまがぽーって、ふわふわしてきて……` / TW: `我明明想回應他幾句，但腦袋迷迷糊糊……` — Cũ: `Thế rồi, tôi muốn nói chuyện lắm,\\nnhưng đầu óc cứ lâng lâng, mơ màng...` → Mới: `Thế rồi, mình muốn nói chuyện lắm,\\nnhưng đầu óc cứ lâng lâng, mơ màng...`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3088 [monologue] — pronoun.** JP: `どうやってお話切り出そうって悩んでたけど――\\nでも、日々姫さんが一緒なら。なら！` / TW: `我正煩惱著該怎麼提出來呢，但是有日日姬小姐陪我就沒問題了！` — Cũ: `Tôi đang đau đầu không biết mở lời thế nào——\\nNhưng, nếu có chị Hibiki đi cùng. Thì!` → Mới: `Mình đang đau đầu không biết mở lời thế nào——\\nNhưng, nếu có chị Hibiki đi cùng. Thì!`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3090 [monologue] — pronoun.** JP: `胸がドキドキしはじめて――\\nそれでも、まだじいっと見ていてくれてる。` / TW: `我的心跳忽然開始加速，雙鐵哥哥依然沒有移開視線。` — Cũ: `Tim tôi bắt đầu đập thình thịch——\\nDù vậy, anh ấy vẫn nhìn tôi chăm chú.` → Mới: `Tim mình bắt đầu đập thình thịch——\\nDù vậy, anh ấy vẫn nhìn mình chăm chú.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3092 [monologue] — pronoun.** JP: `安心、なんて、わたし全然してないのに。\\nドキドキ、こんなにしちゃってるのに。` / TW: `我的心都怦怦直跳了，一點也不放鬆啊。` — Cũ: `An tâm gì chứ, tôi hoàn toàn không thấy vậy mà.\\nTim tôi đang đập thình thịch thế này cơ mà.` → Mới: `An tâm gì chứ, mình hoàn toàn không thấy vậy mà.\\nTim mình đang đập thình thịch thế này cơ mà.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3097 [monologue] — pronoun.** JP: `でも、だからこそ、わたし、一生懸命探してた。` / TW: `所以我才拚命地尋找。` — Cũ: `Nhưng, chính vì thế, em đã cố gắng tìm kiếm.` → Mới: `Nhưng, chính vì thế, mình đã cố gắng tìm kiếm.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”. “em” trong độc thoại → “mình”.)

**Key 3104 [monologue] — pronoun.** JP: `あと、これも。\\nご案内も、わたしにできるお手伝い。` / TW: `指路也是我力所能及的事情。` — Cũ: `Còn nữa, cái này.\\nHướng dẫn cho khách cũng là sự giúp đỡ mà tôi có thể làm.` → Mới: `Còn nữa, cái này.\\nHướng dẫn cho khách cũng là sự giúp đỡ mà mình có thể làm.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3106 [monologue] — pronoun.** JP: `いいこいいこって頭を撫でたら、\\nごろごろいって、今度はまるで子猫みたい！` / TW: `摸摸她的小腦袋後，又在我懷裡扭起身子，彷彿化身成了小貓。` — Cũ: `Tôi vuốt ve đầu khen ngoan ngoãn,\\nthì em ấy lại rừ rừ, giờ thì giống hệt mèo con luôn!` → Mới: `Mình vuốt ve đầu khen ngoan ngoãn,\\nthì em ấy lại rừ rừ, giờ thì giống hệt mèo con luôn!`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3120 [monologue] — pronoun.** JP: `っていうか多分日々姫さん、\\n意識して、わざとそうしてくれたんだ。` / TW: `日日姬小姐應該是故意這麼說話，想讓我放鬆下來吧。` — Cũ: `Hay nói đúng hơn, có lẽ chị Hibiki,\\nđã cố tình làm vậy để giúp tôi.` → Mới: `Hay nói đúng hơn, có lẽ chị Hibiki,\\nđã cố tình làm vậy để giúp mình.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3126 [monologue] — pronoun.** JP: `たった一日のことなのに、昨日よりもっと、ずうっと、\\n“仲間”になれたような気がする！` / TW: `明明只過了一天，我卻感覺自己更加融入了這個大集體之中。` — Cũ: `Dù chỉ mới một ngày, nhưng tôi cảm thấy mình đã trở thành\\n"đồng đội" hơn ngày hôm qua rất nhiều!` → Mới: `Dù chỉ mới một ngày, nhưng mình cảm thấy mình đã trở thành\\n"đồng đội" hơn ngày hôm qua rất nhiều!`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”. Trong dòng đã lẫn “tôi cảm thấy mình” — thống nhất về “mình”.)

**Key 3128 [monologue] — pronoun.** JP: `納得したら、ふしぎになる。\\nそれなら、わたしのことだって――` / TW: `明白他的意思之後，我又有些疑惑。既然要坐Ｎａｖｉ——` — Cũ: `Hiểu ra rồi, tôi lại thấy kỳ lạ.\\nNếu vậy, việc đưa tôi về cũng——` → Mới: `Hiểu ra rồi, mình lại thấy kỳ lạ.\\nNếu vậy, việc đưa mình về cũng——`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3131 [monologue] — pronoun.** JP: `本当は、\x%lキハ07s;#00ffc040;キハ07s%l;#;の戻ってくるのを待って、\\n改札までお手伝いしていきたかったんだけど――` / TW: `本來還想等\x%lキハ07s;#00ffc040;Ｋｉｈａ０７Ｓ%l;#;回來，幫忙分擔一下檢票工作——` — Cũ: `Thực ra, tôi muốn đợi \x%lキハ07s;#00ffc040;Kiha 07S%l;#; quay lại,\\nđể giúp soát vé luôn cơ, nhưng mà——` → Mới: `Thực ra, mình muốn đợi \x%lキハ07s;#00ffc040;KiHa 07S%l;#; quay lại,\\nđể giúp soát vé luôn cơ, nhưng mà——`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”. Đồng thời sửa gloss %l “Kiha 07S”→“KiHa 07S” (cách viết chính thức).)

**Key 3143 [monologue] — pronoun.** JP: `ううん、それでも構わない、\\nそれまでの時間の双鉄おにいさんに甘えちゃおう。` / TW: `沒關係，還是專心享受屬於我們的獨處時間吧。` — Cũ: `Không, dù vậy cũng không sao,\\ntôi sẽ làm nũng với anh Soutetsu trong khoảng thời gian đó.` → Mới: `Không, dù vậy cũng không sao,\\nmình sẽ làm nũng với anh Soutetsu trong khoảng thời gian đó.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3153 [monologue] — pronoun.** JP: `その理由、ポーレットさんは、\\nすごく丁寧に、納得して取り組めるように教えてくれた。` / TW: `波萊特小姐細心地將其中的理由告訴了我。` — Cũ: `Lý do đó, chị Paulette đã\\ndạy cho tôi rất cẩn thận, để tôi có thể hiểu và bắt tay vào làm.` → Mới: `Lý do đó, chị Paulette đã\\ndạy cho mình rất cẩn thận, để mình có thể hiểu và bắt tay vào làm.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3161 [monologue] — pronoun.** JP: `事実かどうかなんて関係なくて――双鉄おにいさんが、\\nそういう風に思ってくれたのがすごくうれしい！！` / TW: `無論他說的是不是事實，有這個想法就很讓我高興了！` — Cũ: `Dù có phải là sự thật hay không cũng không quan trọng——Anh Soutetsu,\\nnghĩ về tôi như vậy khiến tôi vô cùng hạnh phúc!!` → Mới: `Dù có phải là sự thật hay không cũng không quan trọng——Anh Soutetsu,\\nnghĩ về mình như vậy khiến mình vô cùng hạnh phúc!!`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3165 [monologue] — pronoun.** JP: `そうしたら、双鉄おにいさん――\\nきっと、わたしの瞳を見つめて、肩とか、抱いて――` / TW: `然後雙鐵哥哥就會注視著我的眼睛，摟住我的肩膀——` — Cũ: `Lúc đó, anh Soutetsu——\\nchắc chắn sẽ nhìn sâu vào mắt tôi, rồi ôm lấy vai tôi——` → Mới: `Lúc đó, anh Soutetsu——\\nchắc chắn sẽ nhìn sâu vào mắt mình, rồi ôm lấy vai mình——`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3166 [monologue] — pronoun.** JP: `隈元弁。\\n凪ちゃんが話しかけてくれるみたいで、少し落ち着く。` / TW: `熟悉的隈元話讓我想起小凪，便稍稍安心了一些。` — Cũ: `Tiếng Kumamoto.\\nCứ như Nagi đang nói chuyện với tôi vậy, tôi thấy bình tĩnh hơn chút.` → Mới: `Tiếng Kumamoto.\\nCứ như Nagi đang nói chuyện với mình vậy, mình thấy bình tĩnh hơn chút.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3177 [monologue] — pronoun.** JP: `ふんわり、れいなちゃんの声。\\nそれだけでもう、ほっとする。` / TW: `玲奈輕聲向我搭話。聽到她的聲音，我的心情就放鬆下來了。` — Cũ: `Giọng nói êm ái của Reina.\\nChỉ vậy thôi cũng đủ làm tôi nhẹ nhõm.` → Mới: `Giọng nói êm ái của Reina.\\nChỉ vậy thôi cũng đủ làm mình nhẹ nhõm.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3188 [monologue] — pronoun.** JP: `すごい、な、ホントに。\\nいっつものことだから、全然気がつかなかったけど……` / TW: `真是好厲害啊。她平日裡就很精明能幹，所以我才一直沒有注意到……` — Cũ: `Giỏi thật đấy, thực sự luôn.\\nVì là chuyện thường ngày nên tôi hoàn toàn không để ý...` → Mới: `Giỏi thật đấy, thực sự luôn.\\nVì là chuyện thường ngày nên mình hoàn toàn không để ý...`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3190 [monologue] — pronoun.** JP: `うらやましいなって、やっぱり思う。\\nわたしも――仲間に、本当の仲間になりたいな、って。` / TW: `真羨慕她們的關係。我也想成為她們真正的同伴。` — Cũ: `Quả nhiên tôi thấy ghen tị.\\nTôi cũng——muốn trở thành đồng đội, một người đồng đội thực sự.` → Mới: `Quả nhiên mình thấy ghen tị.\\nMình cũng——muốn trở thành đồng đội, một người đồng đội thực sự.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3191 [monologue] — pronoun.** JP: `嬉しい、これって。いっしょに運転できなくっても、\\nわたし、自分から、“僕ら”に入れた！` / TW: `真開心，就算我不能一起參與火車的行駛工作，還是成為了他們的同伴！` — Cũ: `Vui quá, cảm giác này. Dù không thể cùng nhau lái tàu,\\nnhưng tự tôi, đã bước vào "chúng ta" rồi!` → Mới: `Vui quá, cảm giác này. Dù không thể cùng nhau lái tàu,\\nnhưng tự mình, đã bước vào "chúng ta" rồi!`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3196 [monologue] — pronoun.** JP: `お礼をいわれて、きょとんとしちゃう。` / TW: `突如其來的道謝讓我不禁愣住了。` — Cũ: `Được cảm ơn, tôi ngẩn tò te.` → Mới: `Được cảm ơn, mình ngẩn tò te.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3200 [monologue] — pronoun.** JP: `だめ、これはわたしにはわからない。` / TW: `糟糕，這我就真不明白了。` — Cũ: `Chết rồi, cái này thì tôi không biết.` → Mới: `Chết rồi, cái này thì mình không biết.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3208 [monologue] — pronoun.** JP: `さらさらさらって、川の音。\\nわたしの、一番好きな音。` / TW: `耳邊傳來悅耳的水流聲，是我最喜歡的聲音。` — Cũ: `Tiếng nước róc rách.\\nÂm thanh mà tôi thích nhất.` → Mới: `Tiếng nước róc rách.\\nÂm thanh mà mình thích nhất.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3214 [monologue] — pronoun.** JP: `あ、やだ。胸、しゅんとして、ズキンってしちゃう。\\n双鉄おにいさん、わたしをほめてくれているのに――` / TW: `胸口忽然傳來揪心的失落感。即使得到了雙鐵哥哥的誇獎，我卻早就知道……` — Cũ: `A, không. Ngực tôi chợt hẫng đi, nhói đau.\\nAnh Soutetsu đang khen tôi, vậy mà——` → Mới: `A, không. Ngực mình chợt hẫng đi, nhói đau.\\nAnh Soutetsu đang khen mình, vậy mà——`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3222 [monologue] — pronoun.** JP: `自分でいった、わかりきってることなのに――\\n双鉄おにいさんの“僕ら”に、わたし、入ってなくて。` / TW: `自己還是沒有擠進雙鐵哥哥心中那塊屬於同伴的位置。` — Cũ: `Chính tôi đã nói ra, một điều hiển nhiên——\\nTrong chữ "chúng ta" của anh Soutetsu, không có tôi.` → Mới: `Chính mình đã nói ra, một điều hiển nhiên——\\nTrong chữ "chúng ta" của anh Soutetsu, không có mình.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3227 [monologue] — pronoun.** JP: `待たされてると……ああ……やだ、だめ。だけど――\\n『やっぱりわたしなんて』って、思えてきちゃう。` / TW: `被撂在這裡等了這麼久……唉，雖然明知不能這麼想——但還是漸漸開始覺得我對她們不過如此而已。` — Cũ: `Bị bắt chờ thế này thì... a... không được, không được nghĩ vậy. Nhưng——\\nTôi lại bắt đầu nghĩ 『Quả nhiên mình chẳng là gì cả』.` → Mới: `Bị bắt chờ thế này thì... a... không được, không được nghĩ vậy. Nhưng——\\nMình lại bắt đầu nghĩ 『Quả nhiên mình chẳng là gì cả』.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”. “Tôi” đầu câu; phần trích trong dòng đã dùng “mình” đúng.)

**Key 3239 [monologue] — pronoun.** JP: `このままずーっとお茶してたいなって、\\nそんな気持ちも正直感じる――けど……` / TW: `說實話，真想一直享受下去，但是……` — Cũ: `Cứ muốn uống trà thế này mãi thôi,\\nthành thật mà nói tôi cũng có cảm giác đó——nhưng...` → Mới: `Cứ muốn uống trà thế này mãi thôi,\\nthành thật mà nói mình cũng có cảm giác đó——nhưng...`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3255 [monologue] — pronoun.** JP: `わたしのためにも、\\nきっと、あとで役にたつことっても思うし。` / TW: `這也是為了我自己，之後應該會派上用場的。` — Cũ: `Vì bản thân tôi nữa,\\ntôi nghĩ chắc chắn sau này nó sẽ có ích.` → Mới: `Vì bản thân mình nữa,\\nmình nghĩ chắc chắn sau này nó sẽ có ích.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3257 [monologue] — pronoun.** JP: `なんでなんだろ？\\nポーレットさん、わたしの顔……まじまじ……見てる。` / TW: `這是怎麼了？波萊特小姐目不轉睛地看著我。` — Cũ: `Sao thế nhỉ?\\nChị Paulette... cứ nhìn chằm chằm... vào mặt tôi.` → Mới: `Sao thế nhỉ?\\nChị Paulette... cứ nhìn chằm chằm... vào mặt mình.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3258 [monologue] — pronoun.** JP: `言われたらちょっと思い出す。そうだ、わたし――\\n歩きながら、いろいろなこと教えてもらって……` / TW: `這麼一說好像有些印象。對了，我邊走邊聽雙鐵哥哥教我……` — Cũ: `Nghe anh ấy nói tôi mới nhớ ra một chút. Đúng rồi, tôi——\\nvừa đi vừa được anh ấy dạy cho rất nhiều thứ...` → Mới: `Nghe anh ấy nói mình mới nhớ ra một chút. Đúng rồi, mình——\\nvừa đi vừa được anh ấy dạy cho rất nhiều thứ...`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3262 [monologue] — pronoun.** JP: `お風呂にもまだ入らないまま、\\nわたしと凪ちゃんのために頑張ってくれちゃう匂いが。` / TW: `還未洗去的這股氣味，代表著他為我和小凪所付出的努力。` — Cũ: `Vẫn chưa kịp đi tắm,\\nmùi hương của sự cố gắng vì tôi và Nagi.` → Mới: `Vẫn chưa kịp đi tắm,\\nmùi hương của sự cố gắng vì mình và Nagi.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3269 [monologue] — pronoun.** JP: `単なる偶然って思うけど、\\nでももしもそうなら、わたし、そこだって活かしたい。` / TW: `雖然感覺只是湊巧來向我打聽而已，但如果是真的，我想要運用上這份長處。` — Cũ: `Dù nghĩ đó chỉ là sự tình cờ,\\nnhưng nếu thực sự là vậy, tôi cũng muốn tận dụng ưu điểm đó.` → Mới: `Dù nghĩ đó chỉ là sự tình cờ,\\nnhưng nếu thực sự là vậy, mình cũng muốn tận dụng ưu điểm đó.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3270 [monologue] — pronoun.** JP: `わかってたけど――\\nううん、わかってるから、頑張らなくちゃ！` / TW: `雖然我心裡早就明白……不，既然明白，我就更應該努力！` — Cũ: `Tôi biết chứ——\\nKhông, vì biết nên mới phải cố gắng!` → Mới: `Mình biết chứ——\\nKhông, vì biết nên mới phải cố gắng!`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3272 [monologue] — pronoun.** JP: `言って、双鉄おにいさんがわたしを見てくれる。\\n頭のてっぺんから靴の先まで。` / TW: `雙鐵哥哥一邊說，一邊將我從頭到腳打量了一遍。` — Cũ: `Nói rồi, anh Soutetsu nhìn tôi.\\nTừ đỉnh đầu đến mũi giày.` → Mới: `Nói rồi, anh Soutetsu nhìn mình.\\nTừ đỉnh đầu đến mũi giày.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3276 [monologue] — pronoun.** JP: `わたし、起きたのバレちゃった。\\nバレちゃったけど――このままでいいって、言ってくれた。` / TW: `雙鐵哥哥已經發現我醒了。但他還是讓我繼續這樣待著。` — Cũ: `Tôi bị phát hiện là đã thức dậy rồi.\\nBị phát hiện rồi——nhưng anh ấy bảo cứ thế này cũng được.` → Mới: `Mình bị phát hiện là đã thức dậy rồi.\\nBị phát hiện rồi——nhưng anh ấy bảo cứ thế này cũng được.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3277 [monologue] — pronoun.** JP: `双鉄おにいさんが、深く頷く。\\nそれからじ――って、わたしの目を見る。` / TW: `雙鐵哥哥感慨地點點頭，然後直直注視我的雙眼。` — Cũ: `Anh Soutetsu gật gù.\\nRồi nhìn chằm chằm——vào mắt tôi.` → Mới: `Anh Soutetsu gật gù.\\nRồi nhìn chằm chằm——vào mắt mình.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

**Key 3280 [monologue] — pronoun.** JP: `クスって、双鉄お兄さんが笑う。背中で。\\nだから、ぎゅうってしがみついちゃう。` / TW: `雙鐵哥哥輕聲笑出來，引得後背都抖了抖。於是我更加用力地抓緊他。` — Cũ: `Anh Soutetsu bật cười khúc khích. Ở trên lưng.\\nNên tôi lại ôm chặt lấy anh ấy hơn.` → Mới: `Anh Soutetsu bật cười khúc khích. Ở trên lưng.\\nNên mình lại ôm chặt lấy anh ấy hơn.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02: 18 dòng độc thoại Fukami tôi→mình). VN cũ dùng “tôi”/“em”.)

### 3.4. Dịch sai nghĩa

**Key 2596 [ふかみ] — meaning.** JP: `「それは……はい、です。\\nやっぱり、あるって思います」` / TW: `「這個嘛……是啊，嗯。我也這麼覺得」` — Cũ: `「Chuyện đó... vâng, ạ.\\nEm nghĩ là, đúng là có ảnh hưởng ạ」` → Mới: `「Chuyện đó... vâng, ạ.\\nEm nghĩ là, đúng là có đấy ạ」`. (VN cũ bịa thêm “ảnh hưởng”: JP それは……はい、です。やっぱり、あるって思います chỉ khẳng định mơ hồ “đúng là có”; TW cũng chỉ “是啊，我也這麼覺得”. Bỏ “ảnh hưởng”, giữ khẳng định mơ hồ.)

**Key 3296 [monologue] — meaning.** JP: `8620が機関庫からでたら機関庫に入って、\\nそして、発車前の整備をするんだ。` / TW: `８６２０要從機車庫進出，所以她是去做發車前的整備工作吧。` — Cũ: `8620 ra khỏi xưởng thì sẽ vào xưởng,\\nvà tiến hành bảo dưỡng trước khi xuất phát.` → Mới: `8620 ra khỏi xưởng thì mình sẽ vào xưởng,\\nvà tiến hành bảo dưỡng trước khi xuất phát.`. (VN cũ làm mất chuyển chủ ngữ: JP “8620 ra khỏi xưởng → (Fukami) vào xưởng, bảo dưỡng trước khi xuất phát”; VN cũ để 8620 vừa ra vừa vào xưởng — vô nghĩa. Thêm chủ ngữ “mình” cho vế sau.)

## 4. Kiểm tra sweep gasp

- Sweep có **0 mục** cho file này (đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` — không có mục nào mang tên file 凪ふかみ04_ふかみの決意).
- Quét máy bổ sung các đoạn JP kết bằng っ: 6 đoạn (2130 反対側っ, 2131 きゃっ, 2148 むっ, 2167 わたしっ, 2322 ですっ, 2644 だからっ) — tất cả đã được diễn đạt sẵn (2130 → “mà”, 2131 → “Á”, 2148 → “Ưm”, 2167 → “mình thật là”, 2322 → “Ạ”, 2644 → “Thế nên”); theo quy tắc khóa 20/11 thì っ nhấn mạnh trên từ nội dung không phải tiếng nấc, không thêm Ư. **0 gasp sweep bỏ sót.**
- Không có dòng cười ふふ/うふふ nào bị dịch thành tiếng rên (うふふぅ→“Ufufu” đúng, 2278–2290). Không có っ thô trong VN hiển thị (chữ ッ duy nhất ở 2451 nằm trong thuật ngữ JP của thẻ %l ビュッフェ, không phải text hiển thị).
- 1 dòng fa/fu (2177 ふぁ……→“Oa...”) — KHÔNG sửa trong audit, cờ cho đợt thống nhất (§6.6).

## 5. Các dòng giữ nguyên (đã kiểm tra, không sai)

- **2451** thẻ %l trên ビュッフェ có trong TW và VN, vắng trong JP — giữ (thẻ gloss đúng định dạng, gloss “buffet” đúng; TW xác nhận thẻ này; JP thiếu thẻ là đặc tính pipeline, không phải lỗi VN).
- **2070/2631** Soutetsu “bọn anh” — dạng nhóm, không chịu quy tắc số ít; giữ.
- **2428** Nagi trích lời Hibiki “bọn chị” — giữ (nhóm của Hibiki nhìn từ phía Nagi; Hibiki là “chị” với Nagi).
- **2169** Nagi “Bọn tớ” — giữ.
- **2062** Nagi “Cậu đang làm gì thế?” — giữ (người nghe là Fukami; “cậu” là đại từ Nagi→Fukami đã dùng nhất quán trong file, cf. 2247, 2355).
- **2204** ông già “Cảm ơn cậu” — giữ (JP không có từ xưng hô; “cậu” là cách gọi thân mật chung, không sai nghĩa).
- **2075/2297/2636** ベンチ→“ghế đá” — giữ (cách gọi tự nhiên trong tiếng Việt cho ghế dài ở ga/bờ biển; nhất quán cả file).
- **2512** Fukami “Chị đã hiểu” với Reina — giữ (đúng: Fukami là “chị” với Reina; đây là căn cứ cho các sửa 2442/2514).
- **2646** Fukami tự sửa “Anh Soutetsu”→“Anh Migita! Lái tàu Migita!!” — giữ (diễn đạt đúng sự tự sửa sang gọi trang trọng 右田さん/右田機関士).
- **2300/2316/2613** Nagi tự xưng “em” với Soutetsu (にーさん) — giữ, đúng.
- **1993/1997/2144/2200/2206/2389/2404/2411/2547/2570/2610/2612/2617** Fukami tự xưng “em” với Hibiki/Soutetsu/Paulette — giữ, đúng.
- **2131/2132** きゃっ→“Á”, **2133** ひゃん→“Á”, **2158** ひえっ→“Hiee”, **2108** 前っ→“trướcccc”, **2322** ですっ→“Ạ”, **2644** だからっ→“Thế nên”, **2493** にっ/をっ→“——”, **2320** はいっ→“Vâng ạ!!”, **2326** 御迷惑っ→“mất!”, **2416** してくださいっ→“Đi ạ!!!”, **2130** 反対側っ→“mà”, **2199** 大丈夫っ→“Không sao đâu” — っ nhấn mạnh trên từ nội dung, đã diễn đạt, không thêm Ư (quy tắc khóa 20/11); giữ.
- **3290/3291** パンっ→“Bốp”, **3292** ぶーっ→“Buuu”, **3293** くいくいっ→“Kéo kéo” — SFX hành động/còi đã diễn đạt; giữ.
- **2190** ふわっ→“Oa!?”, **2028** ふわっ→“Oa, hả!?” — SFX ngẫu hứng theo ngữ cảnh; giữ.
- **2230** Reina “Chị Fukami”, **2283/2285/2290** Reina “chị Fukami”, **2436** Reina “chị Nagi” — giữ, đúng.
- **2305/2245** trẻ em gọi Fukami “chị” — giữ, đúng.
- VN trùng nhau: 「Hả?」 ×3 (2031/2166/2377, JP đều え？) và 「A——」 ×2 (2208 あ―― / 2209 あー) — giữ (JP giống nhau / khác biệt không đáng kể).

## 6. Cờ cho Hieu (không tự quyết)

1. **Chuyện ghế đá — Fukami tự xưng “em” ở 2294, 2296, 2407.** Đúng nếu Soutetsu có mặt trong cảnh (nhóm ba người cùng nghe chuyện ghế đá), sai thành “tớ”/“mình” nếu chỉ nói với Nagi. Giữ nguyên, chờ Hieu/xác minh ngữ cảnh.
2. **2309 “Nhờ em nhé”.** Đúng chỉ khi người nghe là Reina; nếu là Soutetsu thì phải là “Nhờ anh nhé”. Giữ nguyên.
3. **2393 “Chị xin phép” (いただきます).** Đúng chỉ khi Fukami ăn cùng Reina (Fukami là “chị” với Reina); nếu ăn cùng Hibiki/Soutetsu thì phải là “Em xin phép”. Giữ nguyên.
4. **2174 Nagi “Em đợi anh nhaaaa!”.** Đúng chỉ khi Nagi đợi Soutetsu (にーさん); nếu đợi Fukami thì phải là “Tớ đợi cậu”. Giữ nguyên.
5. **3294 ぷぁん → “Tuýt!”.** JP ぷぁん mơ hồ (tiếng bật/còi); TW dịch 砰 (tiếng nổ/bụp), VN dịch “Tuýt!” (tiếng còi/hú). Giữ nguyên, chờ Hieu chốt: “Bụp!” hay “Tuýt!”.
6. **2177 ふぁ…… → “Oa...” — dòng fa/fu, KHÔNG sửa trong audit; thêm vào hàng đợi thống nhất** (ふぁ→“phà” theo quy tắc đã quyết; tiền lệ: ふかみh1 7 dòng, ハチロクh6 14 dòng đều để đợt thống nhất).

## 7. Lượt soát 2

- Tổng: **94** / kiểm chứng lại: **94** / bỏ: **0** / sửa: **1** (3190: “Tôi cũng” đầu câu sau `\n` bị sót trong lượt đầu vì chỉ thay “tôi” thường — đã sửa thành “Mình cũng” và quét lại toàn bộ: không còn “tôi”/“Tôi” nào sót trong các dòng độc thoại).
- Đã đọc lại toàn bộ 94 giá trị fix đối chiếu JP (+TW khi cần): 67 độc thoại tôi/em→mình + 12 đối thoại đại từ + 13 thuật ngữ + 2 nghĩa — tất cả đúng JP. Kiểm chứng cơ học: JSON 94 mục, khối TOML 94 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 94/94; mỗi fix chỉ khác VN cũ ở đúng chỗ sửa.

## 8. Khối TOML (đã kiểm chứng parse)

```toml
"1522" = "...Cờ xanh và cờ đỏ,\\nrốt cuộc mình chẳng phải phất lần nào."
"1526" = "...Chị Paulette, vừa thanh toán,\\nvừa nhận vé của khách khác, vừa kiểm tra vé định kỳ nữa."
"2086" = "「Để chắc chắn thì, tuyến Yunoi của đường sắt Ohitoyo,\\nhiện tại chỉ có hai ga là Ohitoyo và Yunoi thôi ạ——」"
"2111" = "「Đạo đường. Đạo đường kiếm đạo ở thị trấn Ohitoyo」"
"2137" = "「Ờm... vì đó——cũng là công việc nhà mình.\\nChèo thuyền trên sông Kuma cũng khá giống vậy, nên là」"
"2143" = "「Ưm... ờm.\\nHay là em nên quay lại sau nhỉ?」"
"2158" = "「Hiee!? E, tớ, thì——\\ntớ có gì——mà giỏi——ạ!?」"
"2165" = "「Hả? Em có làm gì đâu——」"
"2178" = "「Ha... hau...\\nK, không có... tớ——」"
"2221" = "「A! Ý hay đấy! Ừ. Nhờ Fukami\\nkiểm tra lại sức hấp dẫn dọc tuyến đường sắt Ohitoyo một lần nữa」"
"2240" = "「A, ừ. ——Vâng.\\nCháu nhớ——cháu nhớ chứ, ạ」"
"2262" = "「Ừ. Vừa thấy biển——à, đúng rồi.\\nTừ lúc đó trở đi, bé Olivy đã bắt chuyện với bọn tớ mà」"
"2283" = "「Ufufu, chị Fukami, giỏi quá đi.\\nNày chị Paulette, nếu đường sắt Ohitoyo có chuyến tàu du lịch tiếp theo」"
"2416" = "「Vì thế, xin hãy cho em——trở thành một người đồng đội thực sự của đường sắt Ohitoyo.\\n——Trở thành trưởng tàu! Đi ạ!!!」"
"2433" = "「Đúng không? Vì vậy, không phải chỉ dựa vào sức của một người.\\nMà đường sắt Ohitoyo——phải cải thiện vấn đề này với tư cách là một tổ chức」"
"2438" = "「Đúng rồi ạ. Bọn mình đi Aircra đến Sendai,\\nrồi từ Sendai lại cứ ngồi tàu suốt——」"
"2442" = "「Đúng vậy ạ. Thế nên chị dọn dẹp nhà vệ sinh là đúng rồi」"
"2460" = "「Đúng vậy! Nếu thế thì chắc chắn bổn tiểu thư này!\\nSẽ cho Fukami thấy những cảnh sắc đẹp hơn nữa!」"
"2478" = "「Ví dụ như lúc chèo thuyền xuôi dòng, bọn mình sẽ hát.\\nCứ nói mãi thì khách sẽ không muốn nghe nữa」"
"2499" = "「Vé một chiều từ Yunoi là 690 yên ạ.\\nQuý khách vui lòng gia hạn vé định kỳ ở Cửa hàng đường sắt nhé」"
"2514" = "「Ờm, chị vẫn chưa biết gì nhiều về nhà ga——\\nNên chị muốn xem xét nhà vệ sinh thật kỹ càng」"
"2569" = "「Bà đi qua bên kia, đến Cửa hàng đường sắt,\\nrồi hỏi mua 『Vé Ohitoyo Một Đêm』 nhé」"
"2572" = "「Cảm ơn quý kh——a!\\nQuý khách ơi? Vé định kỳ của quý khách hết hạn rồi ạ」"
"2596" = "「Chuyện đó... vâng, ạ.\\nEm nghĩ là, đúng là có đấy ạ」"
"2622" = "「Nếu vậy thì, em.\\nNghĩ là em có thể giúp ích được một chút」"
"2664" = "「Việc cải tạo toa hành khách BBQ đang rất nổi tiếng trong giới chủ tàu đấy.\\nThế nên họ mới ngỏ ý nhờ chúng ta thiết kế giúp」"
"2881" = "Nhưng... mình muốn nói, muốn truyền đạt——\\nVì đó là điều mình luôn ao ước."
"2882" = "Nhưng mà, mình cũng có cùng cảm giác.\\n15 phút, chỉ như một cái chớp mắt——ơ, a!"
"2885" = "Nhưng, cơ hội thế này sẽ không có lần thứ hai.\\nNếu bây giờ không nói, chắc chắn cả đời này mình sẽ không thể nói ra!"
"2887" = "Nhưng. Vì thế.\\nVì nhìn thấy những thứ khác nhau, nên cũng có chữ \"chúng ta\" mà mình có thể bước vào."
"2888" = "Việc luôn giữ gìn sạch sẽ quan trọng đến mức nào,\\nbản thân mình cũng tự cảm nhận được."
"2891" = "Nếu mình là một nhân viên nhà ga dễ bắt chuyện,\\nmình muốn mình có thể trả lời thỏa đáng mọi câu hỏi."
"2961" = "Nhưng——nhưng mà! Nghĩ về chuyến đi đường sắt Mikan,\\ntừ lúc đó đến giờ, mình đã suy nghĩ rất kỹ rồi... cơ mà."
"2968" = "A——vừa nãy, tim mình hơi nhói lên một chút.\\nVì trong chữ \"chúng ta\" đó, không có mình ở đây."
"2972" = "Vì chèo thuyền trên sông Kuma là khởi đầu cho mọi thứ của mình mà."
"2974" = "Khi học về sông ngòi, về hệ sinh thái,\\nmình cũng được dạy về hệ thống."
"2979" = "Vui quá, thực sự rất vui.\\nMọi người đều quan tâm đến mình."
"2985" = "Nhẹ nhõm quá.\\nMình bắt đầu thấy tự tin hơn chút."
"2988" = "Có vẻ như chị Paulette và chị Hibiki đã biết chuyện rồi,\\nnhưng mình vẫn kể lại không sót chữ nào những gì mình đã thấy."
"2994" = "Chỉ thế thôi là mình cũng lờ mờ hiểu ra.\\nVì... là anh Soutetsu và Nagi mà."
"2997" = "Sở thích của mình,\\ntrà chanh không đường, em ấy cũng nhớ nữa."
"2999" = "Nếu trở thành trưởng tàu,\\nmình có thể cùng hai người họ chạy về phía bên kia đường ray."
"3003" = "Nếu không có chèo thuyền trên sông Kuma,\\nmình đã không gặp được Nagi và anh Soutetsu."
"3016" = "Đúng rồi, mình đến đây là để nói chuyện đó——\\nKhông, là để nhờ vả."
"3017" = "Với anh Soutetsu, với Nagi, với mẹ và mọi người,\\nnhư vậy là vô cùng, vô cùng thất lễ, mình hiểu điều đó."
"3019" = "Nagi lao đến ôm chầm lấy mình.\\nNhư một chú cún con đang vẫy đuôi vậy!"
"3021" = "Nagi lại ôm chặt lấy mình một lần nữa——\\nRồi sau đó, nét mặt em ấy trở nên nghiêm túc."
"3023" = "Nagi vung tay ra,\\nnên mình cũng đập tay lại gần như phản xạ có điều kiện."
"3029" = "Làm mình giật cả mình.\\nĐột nhiên bị gọi từ phía sau——ơ, a."
"3067" = "Oa, oa. Làm sao đây.\\nĐến lúc quan trọng, quả nhiên chân mình lại chùn bước."
"3070" = "Bởi vì, mình...\\nchỉ là được dẫn đi cùng thôi——mà, nhỉ?"
"3074" = "Mình nuốt ực câu 『Cỡ như mình thì』 đang chực trào ra.\\nNếu nói thế, sẽ thật có lỗi với những người quan trọng của mình——"
"3080" = "Vì là Nagi nên chắc chắn không phải đang trêu chọc mình.\\nNhưng——"
"3082" = "Mình hiểu rồi. Điều mình đã làm——không,\\nlàm như mọi khi, kết quả là công việc đã hoàn thành."
"3084" = "Sợ hãi, và xấu hổ.\\nĐến giờ này rồi còn... một giọng nói vang lên trong mình."
"3086" = "Thế rồi, mình muốn nói chuyện lắm,\\nnhưng đầu óc cứ lâng lâng, mơ màng..."
"3088" = "Mình đang đau đầu không biết mở lời thế nào——\\nNhưng, nếu có chị Hibiki đi cùng. Thì!"
"3090" = "Tim mình bắt đầu đập thình thịch——\\nDù vậy, anh ấy vẫn nhìn mình chăm chú."
"3092" = "An tâm gì chứ, mình hoàn toàn không thấy vậy mà.\\nTim mình đang đập thình thịch thế này cơ mà."
"3097" = "Nhưng, chính vì thế, mình đã cố gắng tìm kiếm."
"3101" = "Thấy rồi, chị Paulette.\\n\\x%lキハ07s;#00ffc040;KiHa 07S%l;#;, có vẻ vừa mới quay lại."
"3104" = "Còn nữa, cái này.\\nHướng dẫn cho khách cũng là sự giúp đỡ mà mình có thể làm."
"3106" = "Mình vuốt ve đầu khen ngoan ngoãn,\\nthì em ấy lại rừ rừ, giờ thì giống hệt mèo con luôn!"
"3120" = "Hay nói đúng hơn, có lẽ chị Hibiki,\\nđã cố tình làm vậy để giúp mình."
"3126" = "Dù chỉ mới một ngày, nhưng mình cảm thấy mình đã trở thành\\n\"đồng đội\" hơn ngày hôm qua rất nhiều!"
"3128" = "Hiểu ra rồi, mình lại thấy kỳ lạ.\\nNếu vậy, việc đưa mình về cũng——"
"3131" = "Thực ra, mình muốn đợi \\x%lキハ07s;#00ffc040;KiHa 07S%l;#; quay lại,\\nđể giúp soát vé luôn cơ, nhưng mà——"
"3143" = "Không, dù vậy cũng không sao,\\nmình sẽ làm nũng với anh Soutetsu trong khoảng thời gian đó."
"3153" = "Lý do đó, chị Paulette đã\\ndạy cho mình rất cẩn thận, để mình có thể hiểu và bắt tay vào làm."
"3161" = "Dù có phải là sự thật hay không cũng không quan trọng——Anh Soutetsu,\\nnghĩ về mình như vậy khiến mình vô cùng hạnh phúc!!"
"3165" = "Lúc đó, anh Soutetsu——\\nchắc chắn sẽ nhìn sâu vào mắt mình, rồi ôm lấy vai mình——"
"3166" = "Tiếng Kumamoto.\\nCứ như Nagi đang nói chuyện với mình vậy, mình thấy bình tĩnh hơn chút."
"3177" = "Giọng nói êm ái của Reina.\\nChỉ vậy thôi cũng đủ làm mình nhẹ nhõm."
"3188" = "Giỏi thật đấy, thực sự luôn.\\nVì là chuyện thường ngày nên mình hoàn toàn không để ý..."
"3190" = "Quả nhiên mình thấy ghen tị.\\nMình cũng——muốn trở thành đồng đội, một người đồng đội thực sự."
"3191" = "Vui quá, cảm giác này. Dù không thể cùng nhau lái tàu,\\nnhưng tự mình, đã bước vào \"chúng ta\" rồi!"
"3196" = "Được cảm ơn, mình ngẩn tò te."
"3200" = "Chết rồi, cái này thì mình không biết."
"3208" = "Tiếng nước róc rách.\\nÂm thanh mà mình thích nhất."
"3214" = "A, không. Ngực mình chợt hẫng đi, nhói đau.\\nAnh Soutetsu đang khen mình, vậy mà——"
"3222" = "Chính mình đã nói ra, một điều hiển nhiên——\\nTrong chữ \"chúng ta\" của anh Soutetsu, không có mình."
"3227" = "Bị bắt chờ thế này thì... a... không được, không được nghĩ vậy. Nhưng——\\nMình lại bắt đầu nghĩ 『Quả nhiên mình chẳng là gì cả』."
"3239" = "Cứ muốn uống trà thế này mãi thôi,\\nthành thật mà nói mình cũng có cảm giác đó——nhưng..."
"3255" = "Vì bản thân mình nữa,\\nmình nghĩ chắc chắn sau này nó sẽ có ích."
"3257" = "Sao thế nhỉ?\\nChị Paulette... cứ nhìn chằm chằm... vào mặt mình."
"3258" = "Nghe anh ấy nói mình mới nhớ ra một chút. Đúng rồi, mình——\\nvừa đi vừa được anh ấy dạy cho rất nhiều thứ..."
"3262" = "Vẫn chưa kịp đi tắm,\\nmùi hương của sự cố gắng vì mình và Nagi."
"3269" = "Dù nghĩ đó chỉ là sự tình cờ,\\nnhưng nếu thực sự là vậy, mình cũng muốn tận dụng ưu điểm đó."
"3270" = "Mình biết chứ——\\nKhông, vì biết nên mới phải cố gắng!"
"3272" = "Nói rồi, anh Soutetsu nhìn mình.\\nTừ đỉnh đầu đến mũi giày."
"3276" = "Mình bị phát hiện là đã thức dậy rồi.\\nBị phát hiện rồi——nhưng anh ấy bảo cứ thế này cũng được."
"3277" = "Anh Soutetsu gật gù.\\nRồi nhìn chằm chằm——vào mắt mình."
"3280" = "Anh Soutetsu bật cười khúc khích. Ở trên lưng.\\nNên mình lại ôm chặt lấy anh ấy hơn."
"3296" = "8620 ra khỏi xưởng thì mình sẽ vào xưởng,\\nvà tiến hành bảo dưỡng trước khi xuất phát."
```

## Kết bài

File 凪ふかみ04_ふかみの決意.txt.toml: 474 dòng đã đọc hết, **94 dòng sai (19,8%)** — không lệch dòng, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch. Lỗi tập trung ở đại từ độc thoại của Fukami (67/94: VN cũ dùng “tôi” thay cho “mình”) + 12 đại từ đối thoại + 13 thuật ngữ đã quyết + 2 nghĩa. 6 cờ cho Hieu (§6) — chuyện ghế đá (3 dòng), 2309, 2393, 2174, 3294 SFX, và 1 dòng fa/fu cho đợt thống nhất. Khối TOML 94 khóa đã parse-kiểm chứng, 0 sai lệch giá trị.

Kết bài
