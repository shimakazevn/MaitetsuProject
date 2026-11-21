# Audit: 真闇03_ひとしずく.txt.toml (05_Mayami)

File route 05_Mayami — “một giọt” (ひとしずく): Hitoshizuku đạt hạng 8 ISC, Soutetsu tỏ tình Mayami (và Hibiki tỏ tình Soutetsu), rồi cả nhà nâng ly chúc mừng kép — giải 8 ISC và tình yêu của Soutetsu với Mayami đơm hoa kết trái.

## 1. Kiểm chứng file

- **TOML:** md5 `5a9b6f7e85500efac9bfe8b54d5937a9`, 1 bản duy nhất (không có bản trùng trong 227 file; 11 nhóm trùng md5 toàn dự án đều là file khác), UTF-8 BOM + CRLF, 419 key script. `[selections]` rỗng. `[characters]` 8 key (2125 Fukami, 2133 Reina, 2140 Hachiroku, 2148 Paulette, 2265 Nagi, 2280 Soutetsu, 2510 Hibiki, 2584 Mayami); `[character_subs]` chỉ chứa key siêu dữ liệu (2250/2519/2526/2545/2550/2570/2718/2719/2757) không tương ứng dòng script nào — không có gì để kiểm tra ở đó.
- **CSV3:** 1 bộ duy nhất (`translation_toml\\05_Mayami\\真闇03_ひとしずく.txt.toml`), 419 dòng, 0 key trùng, 0 VN trống, 0 key thiếu ở cả hai chiều. TOML khớp CSV3 tuyệt đối sau khi chuẩn hoá `\n` literal (TOML-2 làm phẳng thành khoảng trắng — 258 dòng chỉ khác ở đó, 0 dòng khác nội dung).
- **Nhân vật:** độc thoại 177, 双鉄 98, 真闇 54, 日々姫 51, 凪 12, ハチロク 10, ふかみ 8, ポーレット 6, れいな 3. Key 1150–2756 (thưa).
- **Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.** 1 cặp VN trùng nhau là câu lặp hợp lệ (1626/1674 cùng “Hửm?” cho うむ？/ん？).
- **Sweep っ:** 9 entry cho file này; 8 nhận nguyên văn sau khi kiểm chứng JP, 1 bác (2746) — xem §3.

## 2. Đại từ xưng hô — 47 dòng

Soutetsu với Mayami phải là “tôi” (quy tắc đã khóa: Mayami gọi 双ちゃん 366×, chị gái; tiền lệ 真闇02/lr_日々姫真闇h1 đã sửa cùng mẫu), với Hibiki phải là “anh”. File này VN cũ dùng “em” tràn lan cho Soutetsu ở cả hai đối tượng: 16 dòng thoại với Mayami sai thành “em”, 2 dòng sai thành “anh” (1791), 6 dòng với Hibiki sai thành “em”; cộng 23 dòng độc thoại Soutetsu dùng “em”/“mình” thay “tôi”. Đã kiểm chứng từng dòng theo người nghe từ dòng kề (không theo người được nhắc tới).

### 2a. Thoại — 24 dòng

### Key 1203 — [双鉄] — pronoun

- JP: `「……お前には、いつも本当に助けられるな。\n感謝している」`
- TW: `「……我真是得到了你很多幫助啊。真得很感謝你」`
- VN cũ: `「……Anh lúc nào cũng được em giúp đỡ thật nhiều nhỉ.\nAnh rất biết ơn em.」`
- VN mới: `「……Tôi lúc nào cũng được chị giúp đỡ thật nhiều nhỉ.\nTôi rất biết ơn chị.」`
- Lý do: Soutetsu với Mayami phải là “tôi”; Mayami là “chị”, không phải “em” (quy tắc đã khóa: Mayami gọi 双ちゃん 366×, chị gái).

### Key 1207 — [双鉄] — pronoun

- JP: `「……思うところが、何かあるのか？」`
- TW: `「……有什麼想法嗎？」`
- VN cũ: `「……Có chuyện gì, khiến em phải bận tâm sao?」`
- VN mới: `「……Có chuyện gì, khiến chị phải bận tâm sao?」`
- Lý do: Người nghe là Mayami (tiếp nối 1200/1203, đều gọi 真闇姉) — gọi “chị”, không phải “em”.

### Key 1494 — [双鉄] — pronoun

- JP: `「が――真闇姉。少しだけ祝杯を待って欲しい。\n酒が入ったら、話せぬ話をしたいんだ」`
- TW: `「不過——真闇姐，能不能把慶祝稍微放一下。我有件喝了酒之後就說不出口的事要跟你說」`
- VN cũ: `「Nhưng mà―― chị Mayami. Khoan hãy nâng ly đã.\nEm có chuyện muốn nói, chuyện mà nếu có men rượu vào thì em sẽ không thể nói được.」`
- VN mới: `「Nhưng mà―― chị Mayami. Khoan hãy nâng ly đã.\nTôi có chuyện muốn nói, chuyện mà nếu có men rượu vào thì tôi sẽ không thể nói được.」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1668 — [双鉄] — pronoun

- JP: `「うん。いいな」`
- TW: `「嗯。是啊」`
- VN cũ: `「Vâng. Tuyệt đấy.」`
- VN mới: `「Ừ. Tuyệt đấy.」`
- Lý do: Người nghe là Hibiki (1670 Hibiki đáp lời ngay sau) — Soutetsu nói “Ừ”, không nói “Vâng” với em gái.

### Key 1686 — [双鉄] — pronoun

- JP: `「それで僕は疑問に思った。何故僕は、\n真闇姉にだけ、頼らずいようと、思っていたかを」`
- TW: `「因此我產生了疑問。我為什麼唯獨不想依賴真闇姐呢」`
- VN cũ: `「Và rồi em tự hỏi. Tại sao em,\nlại luôn nghĩ rằng mình không được dựa dẫm vào chị Mayami chứ.」`
- VN mới: `「Và rồi anh tự hỏi. Tại sao anh,\nlại luôn nghĩ rằng mình không được dựa dẫm vào chị Mayami chứ.」`
- Lý do: Nói về Mayami ở ngôi thứ ba → người nghe là Hibiki → “anh”.

### Key 1689 — [双鉄] — pronoun

- JP: `「右田が、恩が理由であるなら。\n真闇姉だけじゃなく自分も、願いを叶えて欲しいと」`
- TW: `「因為右田對我有恩。她希望不僅是真闇姐，而是讓我也能實現她的願望」`
- VN cũ: `「Nếu ân huệ của nhà Migita là lý do.\nThì không chỉ chị Mayami, em ấy cũng muốn được em thực hiện ước nguyện của mình.」`
- VN mới: `「Nếu ân huệ của nhà Migita là lý do.\nThì không chỉ chị Mayami, em ấy cũng muốn được tôi thực hiện ước nguyện của mình.」`
- Lý do: Soutetsu thuật lại lời Hibiki cho Mayami nghe → người nghe là Mayami → “tôi”; “em ấy” là Hibiki (ngôi thứ ba) giữ nguyên.

### Key 1691 — [双鉄] — pronoun

- JP: `「日々姫が僕に、恋愛の――\n恋心の告白をしてくれた」`
- TW: `「因為日日姬跟我坦白了——她對我的心意」`
- VN cũ: `「Hibiki đã tỏ tình――\nthổ lộ tình cảm với em.」`
- VN mới: `「Hibiki đã tỏ tình――\nthổ lộ tình cảm với tôi.」`
- Lý do: Soutetsu kể cho Mayami nghe về lời tỏ tình của Hibiki → người nghe là Mayami → “tôi”.

### Key 1694 — [双鉄] — pronoun

- JP: `「一緒に酒を作っていて。たくさん話して、強く感じた。\n僕は真闇姉のことをもっと知りたい。近くに行きたい」`
- TW: `「在和你一起釀酒、和你說了這麼多話後，我迫切覺得想要更多地了解真闇姐、想要接近你」`
- VN cũ: `「Cùng nhau làm rượu. Nói chuyện rất nhiều, và em cảm nhận rất rõ.\nEm muốn biết nhiều hơn về chị Mayami. Muốn đến gần chị hơn.」`
- VN mới: `「Cùng nhau làm rượu. Nói chuyện rất nhiều, và anh cảm nhận rất rõ.\nAnh muốn biết nhiều hơn về chị Mayami. Muốn đến gần chị hơn.」`
- Lý do: Nói về Mayami ở ngôi thứ ba → người nghe là Hibiki → “anh”.

### Key 1699 — [双鉄] — pronoun

- JP: `「輸出か。僕はまったく未経験だが――\n浅野酒造さんが、確か[めいこく,1]冥国に出荷してるよな」`
- TW: `「外銷啊。雖然我完全沒有經驗——記得淺野釀酒有往美國外銷吧」`
- VN cũ: `「Xuất khẩu sao. Em hoàn toàn chưa có kinh nghiệm trong chuyện này――\nNhưng hình như hãng rượu Asano có xuất hàng sang Meikoku (Mỹ) thì phải.」`
- VN mới: `「Xuất khẩu sao. Tôi hoàn toàn chưa có kinh nghiệm trong chuyện này――\nNhưng hình như hãng rượu Asano có xuất hàng sang Minh Quốc thì phải.」`
- Lý do: Người nghe là Mayami (cảnh ở xưởng rượu, 1696/1698 Mayami đang dạy việc) → “tôi”; 冥国 theo thuật ngữ đã khóa là “Minh Quốc”, không phải “Meikoku (Mỹ)” (JP có ruby めいこく, không phải メリケン).

### Key 1776 — [双鉄] — pronoun

- JP: `「僕もわからん。が、ポーレット、ハチロク、れいなは、\n『Ｆ・スコッティ』という\x%lレイルロオド;#00ffc040;レイルロオド%l;#;を推していた」`
- TW: `「我也不知道。但是，波萊特、八六、玲奈都推薦一個叫“Ｆ·斯科蒂”的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;」`
- VN cũ: `「Em cũng không rõ. Nhưng mà, Paulette, Hachiroku và Reina,\nđều đề cử một 『F. Scotty』.」`
- VN mới: `「Tôi cũng không rõ. Nhưng mà, Paulette, Hachiroku và Reina,\nđều đề cử một \x%lレイルロオド;#00ffc040;Railord%l;#; 『F. Scotty』.」`
- Lý do: Người nghe là Mayami (1779 gọi “chị”) → “tôi”; VN cũ bỏ mất từ Railord + thẻ %l của JP — khôi phục cả từ lẫn thẻ.

### Key 1778 — [双鉄] — pronoun

- JP: `「手配しておこう。\nっと……ひとまずはこんなところかな」`
- TW: `「我來安排。嗯……那就先這樣吧」`
- VN cũ: `「Để em sắp xếp cho.\nỪm……trước mắt thì chắc là đến đây thôi.」`
- VN mới: `「Để tôi sắp xếp cho.\nỪm……trước mắt thì chắc là đến đây thôi.」`
- Lý do: Người nghe là Mayami → “tôi”.

### Key 1779 — [双鉄] — pronoun

- JP: `「代わるか？\n掃除番の仕事であれば、僕にも教えられる」`
- TW: `「我來幫你做吧？打掃工作的話我也可以教」`
- VN cũ: `「Để em thay chị nhé?\nNếu là việc hướng dẫn dọn dẹp thì em cũng làm được.」`
- VN mới: `「Để tôi thay chị nhé?\nNếu là việc hướng dẫn dọn dẹp thì tôi cũng làm được.」`
- Lý do: Người nghe là Mayami (“chị”) → “tôi”.

### Key 1785 — [双鉄] — pronoun

- JP: `「僕の前では、どんな我慢もしてほしくない。\n僕は――真闇姉が大好きだから、甘やかしたい」`
- TW: `「我希望你在我面前不要忍耐。因為我——喜歡真闇姐，所以我想嬌縱你」`
- VN cũ: `「Trước mặt em, em không muốn chị phải kìm nén bất cứ điều gì.\nVì em――rất thích chị Mayami, nên em muốn chiều chuộng chị.」`
- VN mới: `「Trước mặt tôi, tôi không muốn chị phải kìm nén bất cứ điều gì.\nVì tôi――rất thích chị Mayami, nên tôi muốn chiều chuộng chị.」`
- Lý do: Soutetsu tỏ tình với Mayami → “tôi” (3 chỗ).

### Key 1786 — [双鉄] — pronoun

- JP: `「出来る男と思われたいし、格好いいと感じて欲しい。\nだから僕は、真闇姉には、頼っちゃだめだと思ってた」`
- TW: `「我希望你認為我是有能力的男人，希望你覺得我帥氣。所以我覺得不能依賴真闇姐」`
- VN cũ: `「Em muốn được chị nghĩ là một người đàn ông có năng lực, muốn được chị thấy em thật ngầu.\nVì thế nên em mới nghĩ rằng, mình không được phép dựa dẫm vào chị Mayami.」`
- VN mới: `「Tôi muốn được chị nghĩ là một người đàn ông có năng lực, muốn được chị thấy tôi thật ngầu.\nVì thế nên tôi mới nghĩ rằng, mình không được phép dựa dẫm vào chị Mayami.」`
- Lý do: Như trên → “tôi” (3 chỗ); “mình” phản thân giữ nguyên.

### Key 1791 — [双鉄] — pronoun

- JP: `「僕は右田の養子で、真闇姉に守ってもらった恩がある。\nそれを返すのは、ごく当然のことだろう」`
- TW: `「我是右田家的養子，真闇姐對我也有守護之恩。報恩不是理所當然的嗎」`
- VN cũ: `「Anh là con nuôi của nhà Migita, mang ơn chị Mayami đã che chở cho anh.\nNên việc đền đáp lại ân huệ đó, là chuyện hết sức hiển nhiên thôi.」`
- VN mới: `「Tôi là con nuôi của nhà Migita, mang ơn chị Mayami đã che chở cho tôi.\nNên việc đền đáp lại ân huệ đó, là chuyện hết sức hiển nhiên thôi.」`
- Lý do: Như trên → “Tôi” (2 chỗ); “con nuôi” giữ nguyên (JP 養子, nói rõ).

### Key 1794 — [双鉄] — pronoun

- JP: `「好きというのは、異性として、側にいたいという好きだ。\n何故そう思うようになったかというと、気づいたからだ」`
- TW: `「我說的喜歡，是作為異性的、能夠長相廝守的那種喜歡。因為我已經發現，自己為什麼會有這樣的念頭了」`
- VN cũ: `「Thích ở đây là tình cảm nam nữ, là mong muốn được ở bên cạnh chị.\nLý do em bắt đầu nghĩ như vậy, là vì em đã nhận ra.」`
- VN mới: `「Thích ở đây là tình cảm nam nữ, là mong muốn được ở bên cạnh chị.\nLý do tôi bắt đầu nghĩ như vậy, là vì tôi đã nhận ra.」`
- Lý do: Như trên → “tôi” (2 chỗ).

### Key 1795 — [双鉄] — pronoun

- JP: `「帰った。ナビにも送らせた」`
- TW: `「我讓Ｎａｖｉ送她們回去了」`
- VN cũ: `「Về hết rồi. Em cũng bảo Navi đưa họ về rồi.」`
- VN mới: `「Về hết rồi. Tôi cũng bảo Navi đưa họ về rồi.」`
- Lý do: Như trên → “Tôi”.

### Key 1829 — [双鉄] — pronoun

- JP: `「大事な話なんだ。\nつまり――僕は、真闇姉を好きだという」`
- TW: `「是很重要的事。也就是——我喜歡真闇姐」`
- VN cũ: `「Là một chuyện rất quan trọng.\nNói tóm lại―― em thích chị Mayami.」`
- VN mới: `「Là một chuyện rất quan trọng.\nNói tóm lại―― anh thích chị Mayami.」`
- Lý do: Nói về Mayami ở ngôi thứ ba (“僕は、真闇姉を好きだ”) → người nghe là Hibiki → “anh”.

### Key 1870 — [双鉄] — pronoun

- JP: `「それで、気づいた。義理だの恩だの関係なしに。\n僕は、真闇姉に。僕を認めてもらいたいんだ」`
- TW: `「然後，我發現了。這和人情啊恩義啊之類的無關。我希望能得到真闇姐的認可」`
- VN cũ: `「Thế nên, em đã nhận ra. Chẳng liên quan gì đến nghĩa lý hay ân huệ cả.\nEm, muốn được chị Mayami. Muốn được chị công nhận.」`
- VN mới: `「Thế nên, anh đã nhận ra. Chẳng liên quan gì đến nghĩa lý hay ân huệ cả.\nAnh, muốn được chị Mayami. Muốn được chị công nhận.」`
- Lý do: Như 1686 (tiếp nối mạch kể với Hibiki; 1873 Hibiki hỏi lại) → “anh”.

### Key 1893 — [双鉄] — pronoun

- JP: `「真闇姉。\n僕は真闇姉に、僕の恋人になって欲しいと望んでいる」`
- TW: `「真闇姐，我希望你成為我的戀人」`
- VN cũ: `「Chị Mayami.\nEm mong chị Mayami sẽ trở thành người yêu của em.」`
- VN mới: `「Chị Mayami.\nTôi mong chị Mayami sẽ trở thành người yêu của tôi.」`
- Lý do: Tỏ tình trực tiếp với Mayami (“真闇姉。” xưng hô trực tiếp) → “Tôi”.

### Key 1953 — [双鉄] — pronoun

- JP: `「そんなことなら、僕も同じだ。\n面倒でややこしくても、僕は、真闇姉と恋をしたい」`
- TW: `「這個我也一樣。哪怕又麻煩又煩人，也不會打消我想和真闇姐談戀愛的想法」`
- VN cũ: `「Chuyện đó thì em cũng giống chị thôi.\nDù có phiền phức và rắc rối, em vẫn muốn yêu chị Mayami.」`
- VN mới: `「Chuyện đó thì anh cũng giống em thôi.\nDù có phiền phức và rắc rối, anh vẫn muốn yêu chị Mayami.」`
- Lý do: Người nghe là Hibiki (1952 Hibiki vừa nói) → “anh”; “giống chị” sai — Hibiki là “em” với Soutetsu.

### Key 1970 — [双鉄] — pronoun

- JP: `「そのとき、日々姫は問うてきた。\n右田というなら、自分も同じじゃないのか――と」`
- TW: `「那個時候，日日姬問我。既然都是姓右田，那麼她自己不也是一樣的嗎——」`
- VN cũ: `「Lúc đó, Hibiki đã hỏi em.\nNếu lý do là vì nhà Migita, thì chẳng phải bản thân em ấy cũng giống vậy sao――」`
- VN mới: `「Lúc đó, Hibiki đã hỏi tôi.\nNếu lý do là vì nhà Migita, thì chẳng phải bản thân em ấy cũng giống vậy sao――」`
- Lý do: Soutetsu kể cho Mayami nghe về câu hỏi của Hibiki → “tôi”; “em ấy” là Hibiki giữ nguyên.

### Key 1977 — [双鉄] — pronoun

- JP: `「それでは、ひとしずくのＩＳＣ８位入賞と、\n僕と真闇姉との恋愛成就とを祝って、乾杯！」`
- TW: `「那麼，為凝露獲得ＩＳＣ第八名和我與真闇姐成為戀人，乾杯！」`
- VN cũ: `「Vậy thì, chúc mừng Hitoshizuku đạt giải 8 tại ISC, và\nchúc mừng tình yêu của em và chị Mayami đã đơm hoa kết trái, cạn ly!」`
- VN mới: `「Vậy thì, chúc mừng Hitoshizuku đạt giải 8 tại ISC, và\nchúc mừng tình yêu của tôi và chị Mayami đã đơm hoa kết trái, cạn ly!」`
- Lý do: Lời chúc mừng tập thể trước cả phòng → “tôi” (dạng trung lập khi nói với nhóm; tiền lệ Paulette 14 key 1544).

### Key 1999 — [双鉄] — pronoun

- JP: `「ナビが？　ああ……そうか――\n僕はおそらく、わかりやすい類の人間なのだな」`
- TW: `「Ｎａｖｉ？啊……是嗎——我或許真是很好懂的那一類人啊」`
- VN cũ: `「Navi á? A……Ra vậy――\nCó lẽ em thuộc tuýp người dễ đoán quá nhỉ.」`
- VN mới: `「Navi á? A……Ra vậy――\nCó lẽ anh thuộc tuýp người dễ đoán quá nhỉ.」`
- Lý do: Người nghe suy luận là Hibiki (1994 Soutetsu nói với Hibiki; 1995/1997 Hibiki ngạc nhiên kẹp giữa) → “anh”.

### 2b. Độc thoại Soutetsu — 23 dòng

### Key 2221 — [monologue] — pronoun

- JP: `が――それが真闇姉の願いなら、\nもちろん、僕は叶えるのみだ。`
- TW: `但——既然是真闇姐的願望，那麼我當然也只能去實現了。`
- VN cũ: `Nhưng――nếu đó là mong muốn của chị Mayami,\ntất nhiên, em chỉ có việc đáp ứng thôi.`
- VN mới: `Nhưng――nếu đó là mong muốn của chị Mayami,\ntất nhiên, tôi chỉ có việc đáp ứng thôi.`
- Lý do: Độc thoại của Soutetsu (僕) — quy tắc chung là “tôi”.

### Key 2227 — [monologue] — pronoun

- JP: `だけれどやっぱり笑顔の方が見たくって、\n言葉を慌てて継ぎ足していく。`
- TW: `但我想看的果然還是她的笑容，因此我急忙繼續補充道。`
- VN cũ: `Nhưng mà em vẫn muốn nhìn thấy nụ cười của chị hơn,\nnên vội vàng nói tiếp.`
- VN mới: `Nhưng mà tôi vẫn muốn nhìn thấy nụ cười của chị hơn,\nnên vội vàng nói tiếp.`
- Lý do: Độc thoại của Soutetsu (kẹp giữa 2225/2229 đều là độc thoại Soutetsu, cùng cảnh tỏ tình) — “tôi”.

### Key 2229 — [monologue] — pronoun

- JP: `けど、真闇姉だけ……\nずっと、例外だと感じてたのは――`
- TW: `但是唯獨真闇姐……我一直覺得她是例外的理由是——`
- VN cũ: `Nhưng, chỉ riêng chị Mayami……\nEm đã luôn cảm thấy chị là một ngoại lệ, là bởi vì――`
- VN mới: `Nhưng, chỉ riêng chị Mayami……\nTôi đã luôn cảm thấy chị là một ngoại lệ, là bởi vì――`
- Lý do: Độc thoại của Soutetsu (僕, 真闇姉) — “tôi”.

### Key 2243 — [monologue] — pronoun

- JP: `が、今は昼間で、蔵の中。\n真闇姉の望みにすぐには、応えられない。から――`
- TW: `但現在是白天，還是在酒窖裡。我沒辦法立刻回應真闇姐的期望。那麼——`
- VN cũ: `Nhưng, bây giờ đang là ban ngày, lại ở trong xưởng rượu.\nEm không thể đáp ứng mong muốn của chị Mayami ngay lập tức được. Thế nên――`
- VN mới: `Nhưng, bây giờ đang là ban ngày, lại ở trong xưởng rượu.\nTôi không thể đáp ứng mong muốn của chị Mayami ngay lập tức được. Thế nên――`
- Lý do: Độc thoại của Soutetsu (応えられない — “tôi không thể đáp ứng”) — “tôi”.

### Key 2378 — [monologue] — pronoun

- JP: `耳打ち。\n途端、耳から僕は酔わされる。`
- TW: `她在我耳邊低語。瞬間，我就被她弄得意亂神迷。`
- VN cũ: `Chị ấy thì thầm vào tai em.\nNgay lập tức, em như bị chuốc say từ đôi tai.`
- VN mới: `Chị ấy thì thầm vào tai tôi.\nNgay lập tức, tôi như bị chuốc say từ đôi tai.`
- Lý do: Độc thoại của Soutetsu (僕は酔わされる) — “tôi” (2 chỗ).

### Key 2384 — [monologue] — pronoun

- JP: `がっかりした声。\nそれにぞわぞわ、心が弾む。`
- TW: `她氣餒的聲音讓我覺得萬分激動。`
- VN cũ: `Giọng điệu thất vọng của chị ấy.\nLại làm trái tim em rộn ràng, xao xuyến.`
- VN mới: `Giọng điệu thất vọng của chị ấy.\nLại làm trái tim tôi rộn ràng, xao xuyến.`
- Lý do: Độc thoại của Soutetsu (khối 2378–2391 đều là Soutetsu quan sát Mayami) — “tôi”.

### Key 2400 — [monologue] — pronoun

- JP: `“右田”であることが理由なら、\n日々姫にだって、僕は頼らずいたはずだ。`
- TW: `如果理由是因為“右田”的話，那我應該也不會依賴日日姬的。`
- VN cũ: `Nếu lý do là vì "nhà Migita",\nthì đáng ra em cũng không được dựa dẫm vào Hibiki mới phải.`
- VN mới: `Nếu lý do là vì "nhà Migita",\nthì đáng ra tôi cũng không được dựa dẫm vào Hibiki mới phải.`
- Lý do: Độc thoại của Soutetsu (僕) — “tôi”.

### Key 2419 — [monologue] — pronoun

- JP: `履歴書、というか身上書。\n分厚い束をまとめて渡せば、真闇姉の目が丸くなる。`
- TW: `履歷書，不，更應該說是簡介吧。我將一捆厚厚的紙張遞過去，結果真闇姐瞪大了眼睛。`
- VN cũ: `Sơ yếu lý lịch, hay đúng hơn là hồ sơ cá nhân.\nKhi em đưa cho chị Mayami một xấp dày cộp, mắt chị ấy tròn xoe.`
- VN mới: `Sơ yếu lý lịch, hay đúng hơn là hồ sơ cá nhân.\nKhi tôi đưa cho chị Mayami một xấp dày cộp, mắt chị ấy tròn xoe.`
- Lý do: Độc thoại của Soutetsu (渡せば — “tôi đưa”) — “tôi”.

### Key 2442 — [monologue] — pronoun

- JP: `伝わる。\nだから、僕も受け取る。`
- TW: `感受到了。所以我也接受了。`
- VN cũ: `Đã truyền đạt được.\nVì vậy, em cũng đón nhận.`
- VN mới: `Đã truyền đạt được.\nVì vậy, tôi cũng đón nhận.`
- Lý do: Độc thoại của Soutetsu (僕も受け取る) — “tôi”.

### Key 2448 — [monologue] — pronoun

- JP: `その中僕は、\nひとり一気にコップの中身を口へと移す。`
- TW: `我一下子將杯中的酒含入口中。`
- VN cũ: `Trong lúc đó, em\nmột mình uống cạn ly rượu vào miệng.`
- VN mới: `Trong lúc đó, tôi\nmột mình uống cạn ly rượu vào miệng.`
- Lý do: Độc thoại của Soutetsu (僕は) — “tôi”.

### Key 2455 — [monologue] — pronoun

- JP: `唇同士を密着させて、\nゆるゆる、僕は流しこむ。`
- TW: `我和她的嘴唇貼在一起，慢慢地將酒傳入她口中。`
- VN cũ: `Hai đôi môi dính chặt vào nhau,\nem từ từ, truyền rượu sang.`
- VN mới: `Hai đôi môi dính chặt vào nhau,\ntôi từ từ, truyền rượu sang.`
- Lý do: Độc thoại của Soutetsu (僕は流しこむ) — “tôi”.

### Key 2475 — [monologue] — pronoun

- JP: `震えている、あの真闇姉が。\nそれでも少しも、瞳は僕から逸らさずにいる。`
- TW: `我的那位真闇姐居然在顫抖。儘管如此，她的視線也沒有從我身上離開。`
- VN cũ: `Chị Mayami đang run rẩy.\nDù vậy, ánh mắt chị ấy không hề rời khỏi em.`
- VN mới: `Chị Mayami đang run rẩy.\nDù vậy, ánh mắt chị ấy không hề rời khỏi tôi.`
- Lý do: Độc thoại của Soutetsu (瞳は僕から) — “tôi”.

### Key 2490 — [monologue] — pronoun

- JP: `胸と胸とがくっつきそうな近くまで。\n真闇姉はそのまま僕を、見上げてくれる。`
- TW: `接近到胸口都要貼在一起的距離。真闇姐沒有動，只是抬頭看著我。`
- VN cũ: `Gần đến mức ngực hai người sắp chạm vào nhau.\nChị Mayami cứ thế ngước lên nhìn em.`
- VN mới: `Gần đến mức ngực hai người sắp chạm vào nhau.\nChị Mayami cứ thế ngước lên nhìn tôi.`
- Lý do: Độc thoại của Soutetsu (僕を、見上げてくれる) — “tôi”.

### Key 2505 — [monologue] — pronoun

- JP: `確かに、来ている。\n僕らの想像していたよりも、ずっと大きく、強い流れが。`
- TW: `新的潮流確實在到來。比我們想像中更加巨大，更加劇烈的潮流。`
- VN cũ: `Chắc chắn là nó đang đến.\nMột luồng gió lớn và mạnh mẽ hơn rất nhiều so với những gì chúng em từng tưởng tượng.`
- VN mới: `Chắc chắn là nó đang đến.\nMột luồng gió lớn và mạnh mẽ hơn rất nhiều so với những gì chúng tôi từng tưởng tượng.`
- Lý do: Độc thoại của Soutetsu (僕ら) — dạng nhóm trung lập là “chúng tôi”.

### Key 2563 — [monologue] — pronoun

- JP: `熱っぽい唇はそのままそっと、\n僕の耳元によせられる。`
- TW: `熾熱的紅唇就這樣慢慢地靠近我的耳邊。`
- VN cũ: `Đôi môi nóng hổi ấy cứ thế nhẹ nhàng,\nghé sát vào tai em.`
- VN mới: `Đôi môi nóng hổi ấy cứ thế nhẹ nhàng,\nghé sát vào tai tôi.`
- Lý do: Độc thoại của Soutetsu (僕の耳元) — “tôi”.

### Key 2601 — [monologue] — pronoun

- JP: `くったりと、真闇姉が僕に体を預けてくる。\n……この忙しさだ、無理もなかろう。`
- TW: `真闇姐將身體靠在我身上。……畢竟這麼忙，也是沒辦法的。`
- VN cũ: `Chị Mayami mệt mỏi dựa hẳn người vào em.\n……Bận rộn đến mức này, cũng không trách được.`
- VN mới: `Chị Mayami mệt mỏi dựa hẳn người vào tôi.\n……Bận rộn đến mức này, cũng không trách được.`
- Lý do: Độc thoại của Soutetsu (僕に体を預けてくる) — “tôi”.

### Key 2619 — [monologue] — pronoun

- JP: `本当にそうだと、しみじみ感じる。\n僕というひとしずく、真闇姉というひとしずく。`
- TW: `確實如此啊，我深有體會。“我”這一滴凝露，還有“真闇姐”這一滴凝露。`
- VN cũ: `Em cảm nhận sâu sắc rằng điều đó hoàn toàn đúng.\nMột giọt mang tên em, một giọt mang tên chị Mayami.`
- VN mới: `Tôi cảm nhận sâu sắc rằng điều đó hoàn toàn đúng.\nMột giọt mang tên tôi, một giọt mang tên chị Mayami.`
- Lý do: Độc thoại của Soutetsu (僕というひとしずく) — “tôi” (2 chỗ).

### Key 2626 — [monologue] — pronoun

- JP: `不意に、猛烈に飲みたくなる。\n恥ずかしいし、いたたまれないし、息苦しい。`
- TW: `突然很想猛幹一口酒。我現在又害羞又緊張，幾乎無法呼吸，簡直想找個洞鑽進去。`
- VN cũ: `Đột nhiên, em muốn uống một ngụm rượu thật mạnh.\nEm đang rất xấu hổ, bồn chồn và gần như nghẹt thở.`
- VN mới: `Đột nhiên, tôi muốn uống một ngụm rượu thật mạnh.\nTôi đang rất xấu hổ, bồn chồn và gần như nghẹt thở.`
- Lý do: Độc thoại của Soutetsu (TW “我”) — “tôi” (2 chỗ).

### Key 2671 — [monologue] — pronoun

- JP: `今度は僕からキスをして、\n真闇姉へと、言葉の代わりの答えを返す。`
- TW: `這次我主動親吻了她，以作為對真闇姐那句話的回答。`
- VN cũ: `Lần này em chủ động hôn,\nnhư một câu trả lời thay cho lời nói gửi đến chị Mayami.`
- VN mới: `Lần này tôi chủ động hôn,\nnhư một câu trả lời thay cho lời nói gửi đến chị Mayami.`
- Lý do: Độc thoại của Soutetsu (僕からキス) — “tôi”.

### Key 2712 — [monologue] — pronoun

- JP: `蔵人たちの目は気になるが、\n後ろ頭をゆっくり撫でる。`
- TW: `雖然很在意旁邊工作人員的眼神，不過我還是慢慢地輕撫著她的後腦勺。`
- VN cũ: `Dù hơi để ý ánh mắt của những người thợ nấu rượu,\nnhưng em vẫn nhẹ nhàng xoa đầu chị ấy.`
- VN mới: `Dù hơi để ý ánh mắt của những người thợ nấu rượu,\nnhưng tôi vẫn nhẹ nhàng xoa đầu chị ấy.`
- Lý do: Độc thoại của Soutetsu (xoa đầu Mayami, “chị ấy”) — “tôi”.

### Key 2731 — [monologue] — pronoun

- JP: `頷き。それだけ。\nだけど、受け入れてもらえた気がして、一歩近づく。`
- TW: `點頭。僅此而已。但我覺得她接受了我，於是我靠近了一步。`
- VN cũ: `Gật đầu. Chỉ có vậy.\nNhưng em cảm giác như đã được chấp nhận, nên bước tới một bước.`
- VN mới: `Gật đầu. Chỉ có vậy.\nNhưng tôi cảm giác như đã được chấp nhận, nên bước tới một bước.`
- Lý do: Độc thoại của Soutetsu (TW “我覺得她接受了我”) — “tôi”.

### Key 2747 — [monologue] — pronoun

- JP: `（今日。だ。たとえどのようなものであれ――\n結果が出たなら、伝えるのだ）`
- TW: `（就是今天。不管結果如何——只要結果出來，我就要表白）`
- VN cũ: `（Hôm nay. Chính là hôm nay. Dù cho kết quả có ra sao――\nChỉ cần có kết quả, mình sẽ nói ra.）`
- VN mới: `（Hôm nay. Chính là hôm nay. Dù cho kết quả có ra sao――\nChỉ cần có kết quả, tôi sẽ nói ra.）`
- Lý do: Độc thoại Soutetsu — “mình” chỉ đúng trong ngoại lệ tự vấn nội tâm; đây là lời quyết tâm (“tôi sẽ nói ra”), không phải tự vấn → “tôi”.

### Key 2750 — [monologue] — pronoun

- JP: `（僕も……日々姫を見習おう）`
- TW: `（我……也要以日日姬為榜樣）`
- VN cũ: `（Mình cũng…… phải học tập Hibiki thôi.）`
- VN mới: `（Tôi cũng…… phải học tập Hibiki thôi.）`
- Lý do: Như trên — lời quyết tâm (“tôi cũng phải học tập Hibiki”), không phải tự vấn → “Tôi”.

## 3. Gasp (sweep っ) — 8 dòng

Sweep có 9 entry cho file này; 8 nhận nguyên văn sau khi đối chiếu JP, 1 bác:

- **2746 BÁC:** （し～っ） → sweep đề xuất “（Suỵt~Ư）”. Không nhận: phụ âm cuối -t của “Suỵt” đã diễn tiếng っ ngắt (suỵt = shush + ngắt); thêm Ư sẽ diễn trùng âm, trái quy tắc “không diễn trùng っ đã diễn”. Giữ “（Suỵt~）”.

### Key 1484 — [日々姫] — gasp

- JP: `「どういたしまして――っ！」`
- TW: `「不客氣——！」`
- VN cũ: `「Không có chi――!」`
- VN mới: `「Không có chi――Ư!」`
- Lý do: Sweep っ: っ cuối tuyệt đối sau ――, âm bị mất hoàn toàn → thêm Ư (đã kiểm chứng JP).

### Key 1565 — [双鉄] — gasp

- JP: `「なるほど、果報は寝て待て――っ！！？」`
- TW: `「原來如此，有福不用忙——！！？」`
- VN cũ: `「Ra là vậy, há miệng chờ sung――!!?」`
- VN mới: `「Ra là vậy, há miệng chờ sung――Ư!!?」`
- Lý do: Như trên (――っ).

### Key 1621 — [双鉄] — gasp

- JP: `「うむ？　――っ！」`
- TW: `「唔——呃！」`
- VN cũ: `「Hửm? ――!」`
- VN mới: `「Hửm? ――Ư!」`
- Lý do: Như trên (――っ).

### Key 1995 — [日々姫] — gasp

- JP: `「っ！」`
- TW: `「！」`
- VN cũ: `「!」`
- VN mới: `「Ư!」`
- Lý do: Sweep っ: cả dòng chỉ là っ + dấu câu → “Ư!”.

### Key 1996 — [真闇] — gasp

- JP: `「っ！！！」`
- TW: `「！！！」`
- VN cũ: `「!!!」`
- VN mới: `「Ư!!!」`
- Lý do: Như trên → “Ư!!!”.

### Key 1997 — [日々姫] — gasp

- JP: `「っ！！？」`
- TW: `「！！？」`
- VN cũ: `「!!?」`
- VN mới: `「Ư!!?」`
- Lý do: Như trên → “Ư!!?”.

### Key 2675 — [monologue] — gasp

- JP: `なら、ねぇねぇも？\nけど……そぎゃんと素振り、いっかいも――っ！`
- TW: `那麼，阿姐也是？不過……她從來沒表現出來過——！`
- VN cũ: `Vậy thì, cả chị Mayami cũng?\nNhưng…… thái độ như vậy, chưa một lần nào――!`
- VN mới: `Vậy thì, cả chị Mayami cũng?\nNhưng…… thái độ như vậy, chưa một lần nào――Ư!`
- Lý do: Sweep っ: っ cuối tuyệt đối sau ―― → thêm Ư.

### Key 2713 — [monologue] — gasp

- JP: `私がそうしてって言ったけど、\nそれでもやっぱり本当は――っ！！？`
- TW: `雖然我嘴上是這麼說的，但我其實還是——！！？`
- VN cũ: `Rõ ràng là do tôi bảo anh ấy làm vậy,\nnhưng sự thật là tôi vẫn――!!?`
- VN mới: `Rõ ràng là do tôi bảo anh ấy làm vậy,\nnhưng sự thật là tôi vẫn――Ư!!?`
- Lý do: Như trên (――っ).

Quét máy toàn file: không còn っ thô nào khác trong VN — các っ còn lại đều là giữa từ (ちょっと/まったく/やっぱり…), nhấn mạnh cuối từ nội dung (よしっ/おっと/にぃにっ — không thêm Ư theo quy tắc), hoặc âm đã diễn (んっ→“Ưm”, もがっ→“ưm”, プツっ→“Tút”, ドドドドドっ→“Rầm”×5, あはっ→“Aha”, えへへ～っ→“Hehehe~”).

## 4. Thuật ngữ / tên riêng — 2 dòng (+1 kèm ở 1699)

### Key 1656 — [真闇] — terminology

- JP: `「はい、もしもし、右田一――あー……んん？\nWait.待って？　Please」`
- TW: `「喂，你好，我是右田一——啊……嗯？Ｗａｉｔ．能等等嗎？Ｐｌｅａｓｅ」`
- VN cũ: `「Vâng, a lô, Migita―― a…… hửm?\nWait. Đợi đã? Please.」`
- VN mới: `「Vâng, a lô, Migita Ichi―― a…… hửm?\nWait. Đợi đã? Please.」`
- Lý do: 右田一 = Migita Ichi (tên đầy đủ; quy tắc đã khóa “Migita Ichi”; VN cũ bỏ mất “Ichi”).

### Key 1657 — [真闇] — terminology

- JP: `「はい、もしもし、右田一――\nYes,Here is a brewery of “ひとしずく”」`
- TW: `「喂，你好，我是右田一——Ｙｅｓ，ｈｅｒｅ　ｉｓ　ａ　ｂｒｅｗｅｒｙ　ｏｆ　“凝露”」`
- VN cũ: `「Vâng, a lô, Migita――\nYes, Here is a brewery of "Hitoshizuku".」`
- VN mới: `「Vâng, a lô, Migita Ichi――\nYes, Here is a brewery of "Hitoshizuku".」`
- Lý do: Như trên.

Key **1699** kèm sửa 冥国 → “Minh Quốc” (xem §2a) — JP có ruby めいこく, không phải メリケン nói, nên theo thuật ngữ đã khóa phải là “Minh Quốc”.

## 5. Sai nghĩa / SFX — 4 dòng

### Key 1586 — [れいな] — sfx

- JP: `「すやぁ～　むにゃあ～」`
- TW: `「呼呀～唔呀～」`
- VN cũ: `「Khò khò~ nhóp nhép~」`
- VN mới: `「Khò khò~ lầm bầm~」`
- Lý do: むにゃあ là lẩm bẩm trong giấc ngủ, không phải chép miệng (“nhóp nhép”).

### Key 1912 — [凪] — vowel

- JP: `「はぁあ――\nざぁんねん。優勝ばできんかったとかー」`
- TW: `「蛤啊啊——真遺憾。不是冠軍啊」`
- VN cũ: `「Haaaa――\nTiếc thật đấy. Không vô địch được sao.」`
- VN mới: `「Haaa――\nTiếc thật đấy. Không vô địch được sao.」`
- Lý do: はぁあ = 3 mora → “Haaa” (VN cũ thừa 1 nguyên âm).

### Key 1947 — [双鉄] — meaning

- JP: `「な――あっ――」`
- TW: `「這——啊——」`
- VN cũ: `「Chuyện――á――」`
- VN mới: `「Nà――á――」`
- Lý do: な――あっ―― chỉ là tiếng ấp úng, không có chữ “Chuyện” nào trong JP — VN cũ bịa thêm (theo TW 這 mà suy ra).

### Key 2458 — [monologue] — meaning

- JP: `一応は携帯を確認し、\n真闇姉は大丈夫だと、ゆったり頷き返してやる。`
- TW: `我姑且確認了一下手機，真闇姐慢慢地點頭，表示沒關係。`
- VN cũ: `Chị Mayami cẩn thận kiểm tra lại điện thoại,\nvà từ tốn gật đầu đáp lại rằng không sao cả.`
- VN mới: `Tôi cẩn thận kiểm tra lại điện thoại,\nchị Mayami từ tốn gật đầu đáp lại rằng không sao cả.`
- Lý do: TW xác nhận “我” (tôi = Soutetsu) kiểm tra điện thoại; Mayami chỉ gật đầu đáp lại — VN cũ gán cả hai hành động cho Mayami.

## 6. Lần soát thứ hai

- Tổng: **61** / tái kiểm chứng: **61** / loại bỏ: **0** / sửa lại: **0**.
- Đã đọc lại từng giá trị fix so với JP sau khi viết xong; 0 sửa bị loại, 0 sửa lại. Kiểm chứng máy: JSON 61 mục (key chuỗi, list-of-dicts), khối TOML 61 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 61/61; diff-sanity: 0 fix viết lại lớn (mọi fix chỉ khác VN cũ ở chỗ sửa có chủ đích).

## 7. Chờ Hieu / ghi chú giữ nguyên

- **Đợt thống nhất (không tính sai):** “Ohimitera” 1928 → “Ohitoyo”; gloss 列車 “tàu” 1708/1735/1768 → “đoàn tàu” (quyết định 19:45); 詠国 không thống nhất trong file — “Anh Quốc” 1662/1905 vs “Eikoku (Vương quốc Anh)” 1687/1833/2533.
- **Giữ nguyên có căn cứ:** 義妹 “em gái nuôi” 2168/2509 và 義父 “cha nuôi” 1496/2278/2478/2730 — theo quyết định 19:45, 義 “nuôi” đã chốt đúng cho nhà Migita (Soutetsu là con nuôi 養子); 2007 きゃっ → “Á” (tiếng giật mình ngoài H-scene, không áp quy tắc romaji H-scene); 1603/1633 tiếng cười cụt (âm đã diễn, sweep không gắn cờ); 2746 sweep bị bác (xem §3).
- **Không chắc — giữ nguyên, chờ Hieu:** **2484** “hỏi em ấy” — người nghĩ có thể là Hibiki (hỏi Mayami → phải là “chị ấy”) hoặc Soutetsu (hỏi Hibiki → “em ấy” đúng); mạch 2441 gợi ý Hibiki nhưng chưa đủ chắc nên không sửa. **1999** người nghe suy luận là Hibiki (ghi rõ lý do ở §2a). **2747/2750** áp dụng hẹp ngoại lệ “mình” (chỉ tự vấn nội tâm) — parent kiểm chứng lại. **1977** tiệc tập thể → “tôi” theo tiền lệ nhóm (Paulette 14 1544).
- **%l:** chỉ 1 lỗi duy nhất toàn file — 1776 thiếu thẻ Railord (đã sửa ở §2a). Các thẻ khác nguyên vẹn; không có thẻ nào VN tự thêm. Không có thẻ thiếu dấu `;` trong file này.
- **Cơ sở tổng đã rebase:** task giao cơ sở 176 file / 8.005 dòng sai, nhưng ROUTE-AUDIT.md lúc viết snippet đã là **177 file / 8.022 dòng sai** (một file 17 dòng sai vừa được gộp lúc ~19:55) — snippet dùng cơ sở 177/8.022 đã kiểm chứng.

## 8. Khối TOML (parse-verified)

Khối 61 khóa, parse bằng tomllib OK, 0 sai lệch giá trị so với JSON. Lưu ý: `\n` literal trong giá trị fix được viết `\\n` trong khối (raw text) để parse ra đúng literal backslash-n như CSV3.

```toml

"1203" = "「……Tôi lúc nào cũng được chị giúp đỡ thật nhiều nhỉ.\\nTôi rất biết ơn chị.」"
"1207" = "「……Có chuyện gì, khiến chị phải bận tâm sao?」"
"1484" = "「Không có chi――Ư!」"
"1494" = "「Nhưng mà―― chị Mayami. Khoan hãy nâng ly đã.\\nTôi có chuyện muốn nói, chuyện mà nếu có men rượu vào thì tôi sẽ không thể nói được.」"
"1565" = "「Ra là vậy, há miệng chờ sung――Ư!!?」"
"1586" = "「Khò khò~ lầm bầm~」"
"1621" = "「Hửm? ――Ư!」"
"1656" = "「Vâng, a lô, Migita Ichi―― a…… hửm?\\nWait. Đợi đã? Please.」"
"1657" = "「Vâng, a lô, Migita Ichi――\\nYes, Here is a brewery of \"Hitoshizuku\".」"
"1668" = "「Ừ. Tuyệt đấy.」"
"1686" = "「Và rồi anh tự hỏi. Tại sao anh,\\nlại luôn nghĩ rằng mình không được dựa dẫm vào chị Mayami chứ.」"
"1689" = "「Nếu ân huệ của nhà Migita là lý do.\\nThì không chỉ chị Mayami, em ấy cũng muốn được tôi thực hiện ước nguyện của mình.」"
"1691" = "「Hibiki đã tỏ tình――\\nthổ lộ tình cảm với tôi.」"
"1694" = "「Cùng nhau làm rượu. Nói chuyện rất nhiều, và anh cảm nhận rất rõ.\\nAnh muốn biết nhiều hơn về chị Mayami. Muốn đến gần chị hơn.」"
"1699" = "「Xuất khẩu sao. Tôi hoàn toàn chưa có kinh nghiệm trong chuyện này――\\nNhưng hình như hãng rượu Asano có xuất hàng sang Minh Quốc thì phải.」"
"1776" = "「Tôi cũng không rõ. Nhưng mà, Paulette, Hachiroku và Reina,\\nđều đề cử một \\x%lレイルロオド;#00ffc040;Railord%l;#; 『F. Scotty』.」"
"1778" = "「Để tôi sắp xếp cho.\\nỪm……trước mắt thì chắc là đến đây thôi.」"
"1779" = "「Để tôi thay chị nhé?\\nNếu là việc hướng dẫn dọn dẹp thì tôi cũng làm được.」"
"1785" = "「Trước mặt tôi, tôi không muốn chị phải kìm nén bất cứ điều gì.\\nVì tôi――rất thích chị Mayami, nên tôi muốn chiều chuộng chị.」"
"1786" = "「Tôi muốn được chị nghĩ là một người đàn ông có năng lực, muốn được chị thấy tôi thật ngầu.\\nVì thế nên tôi mới nghĩ rằng, mình không được phép dựa dẫm vào chị Mayami.」"
"1791" = "「Tôi là con nuôi của nhà Migita, mang ơn chị Mayami đã che chở cho tôi.\\nNên việc đền đáp lại ân huệ đó, là chuyện hết sức hiển nhiên thôi.」"
"1794" = "「Thích ở đây là tình cảm nam nữ, là mong muốn được ở bên cạnh chị.\\nLý do tôi bắt đầu nghĩ như vậy, là vì tôi đã nhận ra.」"
"1795" = "「Về hết rồi. Tôi cũng bảo Navi đưa họ về rồi.」"
"1829" = "「Là một chuyện rất quan trọng.\\nNói tóm lại―― anh thích chị Mayami.」"
"1870" = "「Thế nên, anh đã nhận ra. Chẳng liên quan gì đến nghĩa lý hay ân huệ cả.\\nAnh, muốn được chị Mayami. Muốn được chị công nhận.」"
"1893" = "「Chị Mayami.\\nTôi mong chị Mayami sẽ trở thành người yêu của tôi.」"
"1912" = "「Haaa――\\nTiếc thật đấy. Không vô địch được sao.」"
"1947" = "「Nà――á――」"
"1953" = "「Chuyện đó thì anh cũng giống em thôi.\\nDù có phiền phức và rắc rối, anh vẫn muốn yêu chị Mayami.」"
"1970" = "「Lúc đó, Hibiki đã hỏi tôi.\\nNếu lý do là vì nhà Migita, thì chẳng phải bản thân em ấy cũng giống vậy sao――」"
"1977" = "「Vậy thì, chúc mừng Hitoshizuku đạt giải 8 tại ISC, và\\nchúc mừng tình yêu của tôi và chị Mayami đã đơm hoa kết trái, cạn ly!」"
"1995" = "「Ư!」"
"1996" = "「Ư!!!」"
"1997" = "「Ư!!?」"
"1999" = "「Navi á? A……Ra vậy――\\nCó lẽ anh thuộc tuýp người dễ đoán quá nhỉ.」"
"2221" = "Nhưng――nếu đó là mong muốn của chị Mayami,\\ntất nhiên, tôi chỉ có việc đáp ứng thôi."
"2227" = "Nhưng mà tôi vẫn muốn nhìn thấy nụ cười của chị hơn,\\nnên vội vàng nói tiếp."
"2229" = "Nhưng, chỉ riêng chị Mayami……\\nTôi đã luôn cảm thấy chị là một ngoại lệ, là bởi vì――"
"2243" = "Nhưng, bây giờ đang là ban ngày, lại ở trong xưởng rượu.\\nTôi không thể đáp ứng mong muốn của chị Mayami ngay lập tức được. Thế nên――"
"2378" = "Chị ấy thì thầm vào tai tôi.\\nNgay lập tức, tôi như bị chuốc say từ đôi tai."
"2384" = "Giọng điệu thất vọng của chị ấy.\\nLại làm trái tim tôi rộn ràng, xao xuyến."
"2400" = "Nếu lý do là vì \"nhà Migita\",\\nthì đáng ra tôi cũng không được dựa dẫm vào Hibiki mới phải."
"2419" = "Sơ yếu lý lịch, hay đúng hơn là hồ sơ cá nhân.\\nKhi tôi đưa cho chị Mayami một xấp dày cộp, mắt chị ấy tròn xoe."
"2442" = "Đã truyền đạt được.\\nVì vậy, tôi cũng đón nhận."
"2448" = "Trong lúc đó, tôi\\nmột mình uống cạn ly rượu vào miệng."
"2455" = "Hai đôi môi dính chặt vào nhau,\\ntôi từ từ, truyền rượu sang."
"2458" = "Tôi cẩn thận kiểm tra lại điện thoại,\\nchị Mayami từ tốn gật đầu đáp lại rằng không sao cả."
"2475" = "Chị Mayami đang run rẩy.\\nDù vậy, ánh mắt chị ấy không hề rời khỏi tôi."
"2490" = "Gần đến mức ngực hai người sắp chạm vào nhau.\\nChị Mayami cứ thế ngước lên nhìn tôi."
"2505" = "Chắc chắn là nó đang đến.\\nMột luồng gió lớn và mạnh mẽ hơn rất nhiều so với những gì chúng tôi từng tưởng tượng."
"2563" = "Đôi môi nóng hổi ấy cứ thế nhẹ nhàng,\\nghé sát vào tai tôi."
"2601" = "Chị Mayami mệt mỏi dựa hẳn người vào tôi.\\n……Bận rộn đến mức này, cũng không trách được."
"2619" = "Tôi cảm nhận sâu sắc rằng điều đó hoàn toàn đúng.\\nMột giọt mang tên tôi, một giọt mang tên chị Mayami."
"2626" = "Đột nhiên, tôi muốn uống một ngụm rượu thật mạnh.\\nTôi đang rất xấu hổ, bồn chồn và gần như nghẹt thở."
"2671" = "Lần này tôi chủ động hôn,\\nnhư một câu trả lời thay cho lời nói gửi đến chị Mayami."
"2675" = "Vậy thì, cả chị Mayami cũng?\\nNhưng…… thái độ như vậy, chưa một lần nào――Ư!"
"2712" = "Dù hơi để ý ánh mắt của những người thợ nấu rượu,\\nnhưng tôi vẫn nhẹ nhàng xoa đầu chị ấy."
"2713" = "Rõ ràng là do tôi bảo anh ấy làm vậy,\\nnhưng sự thật là tôi vẫn――Ư!!?"
"2731" = "Gật đầu. Chỉ có vậy.\\nNhưng tôi cảm giác như đã được chấp nhận, nên bước tới một bước."
"2747" = "（Hôm nay. Chính là hôm nay. Dù cho kết quả có ra sao――\\nChỉ cần có kết quả, tôi sẽ nói ra.）"
"2750" = "（Tôi cũng…… phải học tập Hibiki thôi.）"

```

## Kết bài

Đã đọc đủ **419/419 dòng** của 真闇03_ひとしずく.txt.toml (độc thoại 177, thoại 242) so với JP + TW. Sai **61 dòng (14,6%)**: đại từ xưng hô 47 (thoại 24 + độc thoại 23 — Soutetsu “em”/“anh”/“mình” sai đối tượng tràn lan, cùng mẫu với 真闇02/lr_日々姫真闇h1), gasp 8 (sweep, 1 entry bị bác), thuật ngữ 2 (Migita Ichi), sai nghĩa/SFX 4. Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Lần soát thứ hai: 61/61 tái kiểm chứng, 0 loại bỏ, 0 sửa lại. Một điểm không chắc giữ nguyên chờ Hieu (2484 “em ấy”); các mục đợt thống nhất ghi ở §7.
