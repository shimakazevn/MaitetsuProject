# Audit: Paulette 15_求人難 — 36 dòng Việt sai (đã đối chiếu JP + TW)

**Kết quả: 36/408 dòng sai (8.8%)** — 0 lệch vị trí, 0 chưa dịch, 0 cụt câu, 0 chưa chắc chắn. Cảnh: cuộc chiến tuyển người — phe nhà máy Aircra trả lương cao cướp thợ, Soutetsu phải đi nhờ vả Mayami, Minokasa, Akai; Reina khôi phục dữ liệu xong; Paulette mời Soutetsu ở lại qua đêm.

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 408 dòng script** (thoại 250: Soutetsu 124, Paulette 43, Mayami 23, Reina 17, Fukami 15, Minokasa 13, Nagi 12, Hibiki 3; lời dẫn 158) đối chiếu JP + TW từ CSV "Trang tính 3", target là TOML-2. TW chỉ là nhân chứng thứ hai; chỗ nào JP và TW mâu thuẫn thì theo JP (quy tắc Hieu đặt 19/11).
- Heuristic thoại↔lời dẫn báo **0 dòng** — bắt được 0/36. Toàn bộ lỗi đều là cùng-loại (thuật ngữ, xưng hô, tiếng hít) nên heuristic không thấy được; thêm một bằng chứng nữa rằng heuristic chỉ là cận dưới.
- Không có key-shift sạch (shift 0: 408/408; các shift khác 140/140–165/165 — không có ý nghĩa vì key thưa và lỗi không phải lệch vị trí, không áp dụng).
- TOML và CSV giống hệt nhau về nội dung (265 dòng khác chỉ ở `\n`/khoảng trắng, 0 khác nội dung). Không có dòng CSV trống nào; VN==TW 0 dòng. `[selections]` rỗng (0 mục). Thẻ `%l`: 27 dòng có thẻ trong VN (JP có 24) — **0 thẻ thiếu dấu `;` đóng**; 3 dòng VN có thẻ JP không có (1786, 1849, 1958 — đều là thẻ gloss cho ruby có sẵn trong JP: [かんそう,1], [いっとき,1], [ハチロク,3], không phải bịa thêm).
- Phân loại lỗi: thuật ngữ 9 dòng (御一夜 8; 術仙 1 "Jutsusen" thiếu gạch nối); xưng hô 23 dòng (Soutetsu tự xưng "em" 14 dòng + "anh" 6 dòng trong thoại, "Mình" 1 dòng trong thoại 1527, "Em" 2 dòng trong độc thoại 1062/2359); mất tiếng hít っ 4 dòng (1903, 1976, 1977, 1978). Tổng 9 + 23 + 4 = 36 dòng sai. Theo người nói: Soutetsu 27, lời dẫn 4, Fukami 2, Minokasa 2, Paulette 1. **Chưa chắc chắn 0 dòng.**
- Thoại sai 32/250 (12,8%), lời dẫn sai 4/158 (2,5%).
- Về xưng hô Soutetsu trong thoại: quét toàn bộ file bằng máy (đã chuẩn hoá `\n` thành khoảng trắng trước khi chạy regex `\b`, theo bài học Paulette 08) — "tôi/Tôi" 9 dòng, "anh/Anh" tự xưng **6 dòng** (1483, 1580, 1619, 1686, 1718, 1943 — tất cả đều sai), "em/Em" tự xưng **14 dòng** (1103, 1396, 1398, 1410, 1514, 1631, 1640, 1641, 1646, 1702, 1729, 1774, 1801, 1819 — tất cả đều sai; cộng 1527 "Mình" 1 dòng). "Em" ngôi hai 8 lần đều gọi người khác (Reina, Paulette) — đúng. Đây là file đầu tiên mà "em" tự xưng áp đảo "anh" (15 vs 6) — người dịch file này chọn "em" làm dạng tự xưng mặc định của Soutetsu khi nói với Mayami và các bậc trên.
- Về "mình" trong độc thoại: 6 dòng chứa "mình" — **tất cả đều đúng** (sở hữu cách "cơ thể của mình" 2122, "của mình" 2481, phản thân "tự mình" 2552, "giật nảy mình" 2477, "mình đang bị dồn ép" 2547, và "mình đã cố gắng" ở 2359 — giữ theo mẫu "Tôi… mình…" sau khi sửa "Em" thành "Tôi"). 2 dòng sai về xưng hô trong độc thoại là 1062 và 2359 (đều là "Em" tự xưng, đã đưa vào danh sách).
- Không có file trùng lặp: file này chỉ tồn tại ở 03_Paulette/ (đã kiểm tra tên trong cả 227 file TOML-2).

## Kết luận về cơ chế lỗi

Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương, không có dòng mồ côi — đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục): 33/36 dòng sai chỉ xuất hiện đúng 1 lần trong toàn dự án, tại chính key của nó. 3 ngoại lệ đều là chuỗi ngắn chung chung của mẫu lỗi hệ thống mất tiếng hít っ:

- **1976 ("!")**: 206 lần; **1977 ("!!")**: 54 lần; **1978 ("!?")**: 68 lần trong toàn dự án — đều là cùng một lỗi mất tiếng hít っ lặp lại ở hàng trăm dòng, không phải câu của dòng khác.

Cơ chế lỗi ở đây là **xưng hô hệ thống (23/36) + thuật ngữ chưa thống nhất (9/36)** — Soutetsu tự xưng "em" trong 14 dòng và "anh" trong 6 dòng thoại (tổng 21/124 dòng thoại của mình, 16,9%), cộng "Mình" 1 dòng thoại và "Em" 2 dòng độc thoại. Người dịch file này chọn "em" làm dạng tự xưng mặc định khi Soutetsu nói với Mayami (cả 14 dòng "em" đều là nói với Mayami — hoặc báo cáo lại với Mayami/Fukami) — trái docs và trái quy ước của các file Paulette gần đây. Nếu trừ 9 dòng thuật ngữ và 23 dòng xưng hô, file chỉ còn 4 lỗi thực chất (1,0%) — ngang nhóm file sạch nhất.

## Chi tiết dòng sai

### Thuật ngữ

**1402 [Fukami]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「ううん、だって――\nわたし達、御一夜でこれからも暮らしていくでしょ？」
- TW: 「不行，因為——我們是要一直生活在御一夜的對不對？」
- Cũ: 「Không được, bởi vì—— chúng ta, từ nay về sau vẫn sẽ tiếp tục sống ở Ohimitera mà đúng không?」
- Sửa: 「Không được, bởi vì—— chúng ta, từ nay về sau vẫn sẽ tiếp tục sống ở Ohitoyo mà đúng không?」

**1407 [Minokasa]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「礼を言われることじゃなかとです。凪たちのため、\n御一夜の水ば守るのは、私の望みでもありますけん」
- TW: 「不需要道謝。我也想為了孩子們，保住御一夜的水咧」
- Cũ: 「Không cần phải cảm ơn đâu. Vì Nagi và bọn trẻ, bảo vệ nguồn nước của Ohimitera, cũng là mong muốn của tôi mà.」
- Sửa: 「Không cần phải cảm ơn đâu. Vì Nagi và bọn trẻ, bảo vệ nguồn nước của Ohitoyo, cũng là mong muốn của tôi mà.」

**1610 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致は御一夜の滅びに繋がると――\nわかってくれたのではなかったのか」
- TW: 「大家不是都已經明白了——\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶會毀掉御一夜嗎」
- Cũ: 「Việc thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; sẽ dẫn đến sự diệt vong của Ohimitera—— Chẳng phải mọi người đã hiểu ra rồi sao.」
- Sửa: 「Việc thu hút nhà máy Aircra sẽ dẫn đến sự diệt vong của Ohitoyo—— Chẳng phải mọi người đã hiểu ra rồi sao.」

**1666 [Fukami]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「だよね。御一夜で800円を越える時給なんて……\n深夜帯だって、1000円行くか行かないかなのに」
- TW: 「就是啊。在御一夜時薪超過８００日元的兼職……就算是打夜工，時薪都不一定超過１０００日元」
- Cũ: 「Đúng vậy. Ở Ohimitera mà lương theo giờ vượt quá 800 yên thì…… Dù là làm đêm, cũng chỉ tầm 1000 yên hoặc không tới thôi.」
- Sửa: 「Đúng vậy. Ở Ohitoyo mà lương theo giờ vượt quá 800 yên thì…… Dù là làm đêm, cũng chỉ tầm 1000 yên hoặc không tới thôi.」

**1677 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「れいなが託してもらったものを、フルに活かそう。\nそれがれいなにも僕らにも、きっと御一夜にも一番いい」
- TW: 「就讓我們好好運用技師們託付給玲奈的東西吧。這對於玲奈、我們，對於御一夜而言，一定都是最好的選擇」
- Cũ: 「Hãy tận dụng tối đa những gì Reina đã được gửi gắm. Đó chắc chắn là điều tốt nhất cho Reina, cho chúng ta, và cả cho Ohimitera nữa.」
- Sửa: 「Hãy tận dụng tối đa những gì Reina đã được gửi gắm. Đó chắc chắn là điều tốt nhất cho Reina, cho chúng ta, và cả cho Ohitoyo nữa.」

**1694 [Minokasa]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「そん隠れ蓑に――\nいいように御一夜の業者も使われてしまいましたかの」
- TW: 「恐怕御一夜的業內人士，也是被這一偽裝給利用了吧」
- Cũ: 「Cái vỏ bọc đó—— chắc là các nhà thầu ở Ohimitera cũng bị lợi dụng rồi nhỉ.」
- Sửa: 「Cái vỏ bọc đó—— chắc là các nhà thầu ở Ohitoyo cũng bị lợi dụng rồi nhỉ.」

**1796 [Soutetsu]** — 術仙炭鉱 = "mỏ than Jutsu-sen" (thiếu gạch nối: bản cũ "Jutsusen").

- JP: 「炭鉱、技術者さんたちの――\nかつて、術仙炭鉱で働いていた」
- TW: 「曾就職於術仙煤礦的技工名單」
- Cũ: 「Của các kỹ sư mỏ than—— những người từng làm việc ở mỏ than Jutsusen.」
- Sửa: 「Của các kỹ sư mỏ than—— những người từng làm việc ở mỏ than Jutsu-sen.」

**2151 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: だが――御一夜は長い不況の中にある。
- TW: 但是——御一夜的經濟蕭條持續已久。
- Cũ: Nhưng——Ohimitera đang chìm trong thời kỳ suy thoái kéo dài.
- Sửa: 「Nhưng——Ohitoyo đang chìm trong thời kỳ suy thoái kéo dài.」

**2462 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera". Đây là tên công ty: (株)御一夜ワークサービス = Công ty cổ phần Ohitoyo Work Service.

- JP: ふかみのか細い指が差す先、求人先の企業名は、\n（株）御一夜ワークサービス　となっている。
- TW: 深美纖細的手指指向一處，上面寫著發布招聘訊息的企業名——御一夜職業服務股份公司。
- Cũ: Nơi ngón tay thon thả của Fukami chỉ vào, tên doanh nghiệp tuyển dụng là, Công ty cổ phần Ohimitera Work Service.
- Sửa: 「Nơi ngón tay thon thả của Fukami chỉ vào, tên doanh nghiệp tuyển dụng là, Công ty cổ phần Ohitoyo Work Service.」

### Xưng hô

**1062 [lời dẫn]** — Độc thoại của Soutetsu tự xưng "Em" — trái quy ước độc thoại của file (tôi 62 dòng vs mình 9 dòng, tất cả đều đúng) và docs (locations §2.1: độc thoại "Tôi").

- JP: “秦さんだったら断らない”“きっと協力してくれる”\n――そんな希望に、甘え縋ろうとしただけだった。
- TW: “秦氏一定不會拒絕”“一定願意幫助我們”——我只是想從這樣一份寄託之中，尋得些許安慰。
- Cũ: “Nếu là anh Hata thì sẽ không từ chối đâu” “Chắc chắn anh ấy sẽ hợp tác” ——Em chỉ định dựa dẫm và bấu víu vào niềm hy vọng đó thôi.
- Sửa: “Nếu là anh Hata thì sẽ không từ chối đâu” “Chắc chắn anh ấy sẽ hợp tác” ——Tôi chỉ định dựa dẫm và bấu víu vào niềm hy vọng đó thôi.

**1103 [Soutetsu]** — Soutetsu tự xưng "em" khi nói với Mayami ("Xin lỗi chị") — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki; "em" cũng không phải dạng tự xưng của Soutetsu).

- JP: 「……すまん。いささか、動揺した。\nまさかここまで追い込まれるとは思ってなかった」
- TW: 「……抱歉，我有點動搖了。之前沒想過會被逼入這種絕境」
- Cũ: 「……Xin lỗi chị. Em hơi kích động. Không ngờ lại bị dồn đến mức này.」
- Sửa: 「……Xin lỗi chị. Tôi hơi kích động. Không ngờ lại bị dồn đến mức này.」

**1396 [Soutetsu]** — Soutetsu tự xưng "em" khi kể với Mayami/Fukami — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「いや――しかし――\n秦さんにも、他の幾人にも、僕は頭を下げ、て…………」
- TW: 「不——可是——不管是對秦氏，還是其他幾個人，我都是低頭去懇、求…………」
- Cũ: 「Không——nhưng mà—— Cả với anh Hata, và vài người khác nữa, em đã cúi đầu, nhờ vả…………」
- Sửa: 「Không——nhưng mà—— Cả với anh Hata, và vài người khác nữa, tôi đã cúi đầu, nhờ vả…………」

**1398 [Soutetsu]** — Soutetsu tự xưng "em" khi nói với Mayami — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「真闇姉一人の話ではない。蓑笠さんにも、赤井宮司にも\n――頼れる相手がいるのなら、心底頼るべきだった」
- TW: 「不光是真闇姐一個人。還有蓑笠先生、赤井宮司——既然找得到幫手，我就應該誠心誠意地求助」
- Cũ: 「Không chỉ một mình chị Mayami. Cả ông Minokasa, cả đền chủ Akai ——nếu có người để dựa dẫm, đáng lẽ em phải dựa dẫm từ tận đáy lòng.」
- Sửa: 「Không chỉ một mình chị Mayami. Cả ông Minokasa, cả đền chủ Akai——nếu có người để dựa dẫm, đáng lẽ tôi phải dựa dẫm từ tận đáy lòng.」

**1410 [Soutetsu]** — Soutetsu tự xưng "em" khi nói với Mayami — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「いや、教わった――\n一から十まで、丁寧に教えていただいた」
- TW: 「不，學到了——從頭到尾，秦氏都仔細地教會了我」
- Cũ: 「Không, em đã được dạy rồi—— Được chỉ dạy tận tình từ đầu đến cuối rồi.」
- Sửa: 「Không, tôi đã được dạy rồi—— Được chỉ dạy tận tình từ đầu đến cuối rồi.」

**1483 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Mayami/Fukami — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「その辺も含め、お話ししてきた。\n蓑笠さんも、すぐに動いてくださるそうだ」
- TW: 「包括玲奈的事在內，我已經去談過了。蓑笠先生也表示會立刻做好準備的」
- Cũ: 「Bao gồm cả chuyện đó, anh đã nói chuyện xong rồi. Ông Minokasa cũng bảo sẽ lập tức hành động.」
- Sửa: 「Bao gồm cả chuyện đó, tôi đã nói chuyện xong rồi. Ông Minokasa cũng bảo sẽ lập tức hành động.」

**1514 [Soutetsu]** — Soutetsu tự xưng "em" ×2 khi nói với Mayami ("chị Mayami") — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「教えてくれ、真闇姉。\n僕は、そうするために何をすればいい？」
- TW: 「告訴我，真闇姐。我要怎麼做才能成功？」
- Cũ: 「Chỉ cho em với, chị Mayami. Để làm được như vậy, em phải làm gì?」
- Sửa: 「Chỉ cho tôi với, chị Mayami. Để làm được như vậy, tôi phải làm gì?」

**1527 [Soutetsu]** — Soutetsu tự xưng "Mình" trong thoại trực tiếp — trái docs (locations §2.1: "Tôi"; tiền lệ Paulette 07 usagi 1690: "Mình" trong thoại trực tiếp là sai).

- JP: 「っと？　早すぎたか？」
- TW: 「哎呀？來得太早了嗎？」
- Cũ: 「Ủa? Mình đến sớm quá sao?」
- Sửa: 「Ủa? Tôi đến sớm quá sao?」

**1580 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói điện thoại với Minokasa — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「うん――うん……そうか、わかった」
- TW: 「嗯——嗯……是嗎，我知道了」
- Cũ: 「Ừ——ừm……vậy sao, anh hiểu rồi.」
- Sửa: 「Ừ——ừm……vậy sao, tôi hiểu rồi.」

**1619 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Paulette (1618 Reina chúc ngủ ngon Paulette và Soutetsu; Soutetsu đang chào tạm biệt ở nhà Paulette) — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「明日がなければ、泊まって行きたい。\nが――今は」
- TW: 「如果明天沒有事，我也很想留下過夜。可是，現在這個時期——」
- Cũ: 「Nếu không có ngày mai, anh rất muốn ở lại. Nhưng——bây giờ thì.」
- Sửa: 「Nếu không có ngày mai, tôi rất muốn ở lại. Nhưng——bây giờ thì.」

**1631 [Soutetsu]** — Soutetsu tự xưng "em" khi nói với Mayami — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「宝生元忠は……そこまでを準備し、仕掛けて来た。\nそれは――今の僕には及びもつかぬ力量だ」
- TW: 「寶生元忠……做了如此周詳的準備，向我們展開攻勢。他的能力——是現在的我所不可匹敵的」
- Cũ: 「Houshou Mototada……đã chuẩn bị đến mức đó, và ra tay. Đó là——năng lực mà em hiện tại không thể sánh bằng.」
- Sửa: 「Houshou Mototada……đã chuẩn bị đến mức đó, và ra tay. Đó là——năng lực mà tôi hiện tại không thể sánh bằng.」

**1640 [Soutetsu]** — Soutetsu tự xưng "em" ×2 khi nói với Mayami — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「申し訳ない。金の誘惑に負けたなど――\n未熟な僕の、逆恨みによる暴言に過ぎなかった」
- TW: 「對不起。所謂敗給了金錢的誘惑——只是幼稚的我遷怒於人的惡言」
- Cũ: 「Em xin lỗi. Cái gì mà thua trước cám dỗ của đồng tiền chứ—— Đó chỉ là những lời lẽ cay nghiệt do sự oán hận vô lý của một kẻ non nớt như em thôi.」
- Sửa: 「Tôi xin lỗi. Cái gì mà thua trước cám dỗ của đồng tiền chứ—— Đó chỉ là những lời lẽ cay nghiệt do sự oán hận vô lý của một kẻ non nớt như tôi thôi.」

**1641 [Soutetsu]** — Soutetsu tự xưng "em" ×2 khi nói với Mayami — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「済まない。僕が完全に間違えていた。\n口コミの誘いを断られ続け、きっと意固地になっていた」
- TW: 「對不起，是我完全錯了。我想我是因為勸說一直被拒絕，變得有點意氣用事了」
- Cũ: 「Em xin lỗi. Là em hoàn toàn sai. Bị từ chối liên tục qua những lời mời truyền miệng, chắc chắn em đã trở nên cố chấp rồi.」
- Sửa: 「Tôi xin lỗi. Là tôi hoàn toàn sai. Bị từ chối liên tục qua những lời mời truyền miệng, chắc chắn tôi đã trở nên cố chấp rồi.」

**1646 [Soutetsu]** — Soutetsu tự xưng "em" khi nói với Mayami — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「ああ、他の秦さんに用は無い」
- TW: 「對，我找別的秦氏也沒事啊」
- Cũ: 「Vâng, em đâu có việc gì với anh Hata nào khác đâu.」
- Sửa: 「Vâng, tôi đâu có việc gì với anh Hata nào khác đâu.」

**1686 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Paulette (1700 Paulette đáp lại "cảm ơn anh") — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「お互い様だ。僕も多くを、\nポーレットに任せているわけだしな」
- TW: 「彼此彼此。我也把很多事情交給了波萊特了嘛」
- Cũ: 「Có qua có lại thôi. Anh cũng, giao phó rất nhiều việc cho Paulette mà.」
- Sửa: 「Có qua có lại thôi. Tôi cũng, giao phó rất nhiều việc cho Paulette mà.」

**1702 [Soutetsu]** — Soutetsu tự xưng "em" khi nói với Mayami — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「僕は――まず、真闇姉に助力を願うべきだった」
- TW: 「我——應該最先請求真闇姐的幫助」
- Cũ: 「Em——đáng lẽ phải nhờ chị Mayami giúp đỡ đầu tiên.」
- Sửa: 「Tôi——đáng lẽ phải nhờ chị Mayami giúp đỡ đầu tiên.」

**1718 [Soutetsu]** — Soutetsu tự xưng "anh" ×2 khi nói với Paulette (1712 Paulette rủ vào trong, 1700 Paulette "cảm ơn anh") — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). "Em" gọi Paulette (ngôi hai) giữ nguyên — thuộc đề xuất "cô"/"em" đang chờ chốt.

- JP: 「引き止めてもらえて、嬉しかった。\nおかげで、明日もがんばれる」
- TW: 「我很高興你把我叫住。這樣一來，我明天又有動力了」
- Cũ: 「Anh rất vui vì em đã giữ anh lại. Nhờ vậy, ngày mai anh lại có thể cố gắng rồi.」
- Sửa: 「Tôi rất vui vì em đã giữ tôi lại. Nhờ vậy, ngày mai tôi lại có thể cố gắng rồi.」

**1729 [Soutetsu]** — Soutetsu tự xưng "em" khi nói với Mayami ("chị Mayami") — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「どうしたらいいかな、真闇姉。他はともかく、\n秦さんまでもが、金の力に負けてしまった」
- TW: 「我該怎麼辦，真闇姐。不說其他人，就連秦氏都敗給了金錢的力量」
- Cũ: 「Em phải làm sao đây, chị Mayami. Chưa nói đến những người khác, ngay cả anh Hata, cũng đã gục ngã trước sức mạnh của đồng tiền.」
- Sửa: 「Tôi phải làm sao đây, chị Mayami. Chưa nói đến những người khác, ngay cả anh Hata, cũng đã gục ngã trước sức mạnh của đồng tiền.」

**1774 [Soutetsu]** — Soutetsu tự xưng "em" khi nói với Mayami — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「僕の甘さが……苦境を深めてしまっていたのか」
- TW: 「是我的天真……加深了此刻的困境嗎」
- Cũ: 「Sự ngây thơ của em……đã làm hoàn cảnh thêm khó khăn sao.」
- Sửa: 「Sự ngây thơ của tôi……đã làm hoàn cảnh thêm khó khăn sao.」

**1801 [Soutetsu]** — Soutetsu tự xưng "em" khi nói với Mayami — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). "Mình" phản thân ("mình bị dồn ép") giữ nguyên.

- JP: 「無いものを欲しがるから……\n実際以上に、僕は追い詰められた気になったのか」
- TW: 「正因我得不到還要去強求……才會覺得情況比實際更糟糕」
- Cũ: 「Vì cứ ham muốn những thứ không có nên…… em mới cảm thấy mình bị dồn ép hơn cả thực tế sao.」
- Sửa: 「Vì cứ ham muốn những thứ không có nên…… tôi mới cảm thấy mình bị dồn ép hơn cả thực tế sao.」

**1819 [Soutetsu]** — Soutetsu tự xưng "em" ×3 khi nói với Mayami ("chị Mayami") — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「そうするために。真闇姉。\n僕に、僕らに――力を貸して欲しいんだ」
- TW: 「為了實現這個目標……真闇姐，我希望你能幫助我——借給我們你的力量」
- Cũ: 「Để làm được như vậy. Chị Mayami. Em muốn chị cho em, cho chúng em——mượn sức mạnh của chị.」
- Sửa: 「Để làm được như vậy. Chị Mayami. Tôi muốn chị cho tôi, cho chúng tôi——mượn sức mạnh của chị.」

**1943 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Paulette (1939 Paulette mời ở lại qua đêm) — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「それはいいな。\nそのときは、僕にも同乗させてくれ」
- TW: 「那可真不錯。到時候，讓我也當一回乘客吧」
- Cũ: 「Thế thì tốt quá. Lúc đó, cho anh đi cùng với nhé.」
- Sửa: 「Thế thì tốt quá. Lúc đó, cho tôi đi cùng với nhé.」

**2359 [lời dẫn]** — Độc thoại của Soutetsu tự xưng "Em" ×2 — trái quy ước độc thoại của file và docs (locations §2.1: độc thoại "Tôi"). "Mình" ở câu hai giữ nguyên theo mẫu "Tôi… mình…" (tiền lệ Paulette 10: "mình" sau "Tôi" trong cùng câu là cách phản thân, được giữ).

- JP: しているつもりだ。\nベストも、尽くしてきたつもりだ。
- TW: 我當然下定了決心。並且，也在全力以赴。
- Cũ: Em nghĩ là em đã chuẩn bị tâm lý rồi. Em cũng nghĩ là mình đã cố gắng hết sức.
- Sửa: 「Tôi nghĩ là tôi đã chuẩn bị tâm lý rồi. Tôi cũng nghĩ là mình đã cố gắng hết sức.」

### Lỗi nhỏ

**1903 [Soutetsu]** — Mất tiếng hít っ: JP 「証？　……っ！！」 dịch thành "Minh chứng? ……!!" — tiếng hít biến mất (TW giữ lại bằng "啊!!"). Tiền lệ Hachiroku 12 2103/2537 và Paulette 09 2274/2275/2277: JP 「っ！」→ "Ư!".

- JP: 「証？　\n……っ！！」
- TW: 「證據？……啊！！」
- Cũ: 「Minh chứng? ……!!」
- Sửa: 「Minh chứng? ……Ư!!」

**1976 [Soutetsu]** — Mất tiếng hít っ: JP 「っ！」 dịch thành "!" trơ trụi. Tiền lệ Hachiroku 12 2103/2537 và Paulette 09 2274/2275/2277: JP 「っ！」→ "Ư!".

- JP: 「っ！」
- TW: 「！」
- Cũ: 「!」
- Sửa: 「Ư!」

**1977 [Soutetsu]** — Mất tiếng hít っ: JP 「っ！！」 dịch thành "!!" trơ trụi. Tiền lệ Hachiroku 12 2103/2537 và Paulette 09 2274/2275/2277: JP 「っ！」→ "Ư!".

- JP: 「っ！！」
- TW: 「！！」
- Cũ: 「!!」
- Sửa: 「Ư!!」

**1978 [Soutetsu]** — Mất tiếng hít っ: JP 「っ！？」 dịch thành "!?" trơ trụi. Tiền lệ Hachiroku 12 2103/2537 và Paulette 09 2274/2275/2277: JP 「っ！」→ "Ư!".

- JP: 「っ！？」
- TW: 「！？」
- Cũ: 「!?」
- Sửa: 「Ư!?」

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
1062 = "“Nếu là anh Hata thì sẽ không từ chối đâu” “Chắc chắn anh ấy sẽ hợp tác” ——Tôi chỉ định dựa dẫm và bấu víu vào niềm hy vọng đó thôi."
1103 = "「……Xin lỗi chị. Tôi hơi kích động. Không ngờ lại bị dồn đến mức này.」"
1396 = "「Không——nhưng mà—— Cả với anh Hata, và vài người khác nữa, tôi đã cúi đầu, nhờ vả…………」"
1398 = "「Không chỉ một mình chị Mayami. Cả ông Minokasa, cả đền chủ Akai——nếu có người để dựa dẫm, đáng lẽ tôi phải dựa dẫm từ tận đáy lòng.」"
1402 = "「Không được, bởi vì—— chúng ta, từ nay về sau vẫn sẽ tiếp tục sống ở Ohitoyo mà đúng không?」"
1407 = "「Không cần phải cảm ơn đâu. Vì Nagi và bọn trẻ, bảo vệ nguồn nước của Ohitoyo, cũng là mong muốn của tôi mà.」"
1410 = "「Không, tôi đã được dạy rồi—— Được chỉ dạy tận tình từ đầu đến cuối rồi.」"
1483 = "「Bao gồm cả chuyện đó, tôi đã nói chuyện xong rồi. Ông Minokasa cũng bảo sẽ lập tức hành động.」"
1514 = "「Chỉ cho tôi với, chị Mayami. Để làm được như vậy, tôi phải làm gì?」"
1527 = "「Ủa? Tôi đến sớm quá sao?」"
1580 = "「Ừ——ừm……vậy sao, tôi hiểu rồi.」"
1610 = "「Việc thu hút nhà máy Aircra sẽ dẫn đến sự diệt vong của Ohitoyo—— Chẳng phải mọi người đã hiểu ra rồi sao.」"
1619 = "「Nếu không có ngày mai, tôi rất muốn ở lại. Nhưng——bây giờ thì.」"
1631 = "「Houshou Mototada……đã chuẩn bị đến mức đó, và ra tay. Đó là——năng lực mà tôi hiện tại không thể sánh bằng.」"
1640 = "「Tôi xin lỗi. Cái gì mà thua trước cám dỗ của đồng tiền chứ—— Đó chỉ là những lời lẽ cay nghiệt do sự oán hận vô lý của một kẻ non nớt như tôi thôi.」"
1641 = "「Tôi xin lỗi. Là tôi hoàn toàn sai. Bị từ chối liên tục qua những lời mời truyền miệng, chắc chắn tôi đã trở nên cố chấp rồi.」"
1646 = "「Vâng, tôi đâu có việc gì với anh Hata nào khác đâu.」"
1666 = "「Đúng vậy. Ở Ohitoyo mà lương theo giờ vượt quá 800 yên thì…… Dù là làm đêm, cũng chỉ tầm 1000 yên hoặc không tới thôi.」"
1677 = "「Hãy tận dụng tối đa những gì Reina đã được gửi gắm. Đó chắc chắn là điều tốt nhất cho Reina, cho chúng ta, và cả cho Ohitoyo nữa.」"
1686 = "「Có qua có lại thôi. Tôi cũng, giao phó rất nhiều việc cho Paulette mà.」"
1694 = "「Cái vỏ bọc đó—— chắc là các nhà thầu ở Ohitoyo cũng bị lợi dụng rồi nhỉ.」"
1702 = "「Tôi——đáng lẽ phải nhờ chị Mayami giúp đỡ đầu tiên.」"
1718 = "「Tôi rất vui vì em đã giữ tôi lại. Nhờ vậy, ngày mai tôi lại có thể cố gắng rồi.」"
1729 = "「Tôi phải làm sao đây, chị Mayami. Chưa nói đến những người khác, ngay cả anh Hata, cũng đã gục ngã trước sức mạnh của đồng tiền.」"
1774 = "「Sự ngây thơ của tôi……đã làm hoàn cảnh thêm khó khăn sao.」"
1796 = "「Của các kỹ sư mỏ than—— những người từng làm việc ở mỏ than Jutsu-sen.」"
1801 = "「Vì cứ ham muốn những thứ không có nên…… tôi mới cảm thấy mình bị dồn ép hơn cả thực tế sao.」"
1819 = "「Để làm được như vậy. Chị Mayami. Tôi muốn chị cho tôi, cho chúng tôi——mượn sức mạnh của chị.」"
1903 = "「Minh chứng? ……Ư!!」"
1943 = "「Thế thì tốt quá. Lúc đó, cho tôi đi cùng với nhé.」"
1976 = "「Ư!」"
1977 = "「Ư!!」"
1978 = "「Ư!?」"
2151 = "「Nhưng——Ohitoyo đang chìm trong thời kỳ suy thoái kéo dài.」"
2359 = "「Tôi nghĩ là tôi đã chuẩn bị tâm lý rồi. Tôi cũng nghĩ là mình đã cố gắng hết sức.」"
2462 = "「Nơi ngón tay thon thả của Fukami chỉ vào, tên doanh nghiệp tuyển dụng là, Công ty cổ phần Ohitoyo Work Service.」"
```

Khối trên đã kiểm chứng: parse bằng tomllib được **36/36 keys**, giá trị khớp đúng JSON. Không còn dạng cũ nào trong khối sửa (0 "Ohimitera"/"Ohito"/"Jussen"/"Jutsusen").

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- **Soutetsu gọi Paulette "cô" vs "em": "em" 1× (1459), "cô" 0×.** Dòng duy nhất rõ ràng: 1459 "Em cũng gặp đền chủ Akai rồi sao?" (nói với Paulette). Hai câu "cảm ơn em" (1531, 1559) không đếm vì người nghe không rõ (có thể là Reina hoặc Paulette). Tổng hợp P09–15: "cô" 43× vs "em" 7× (P09 7:1, P10 20:2, P11 9:0, P12 7:0, P13 0:2, P14 0:1, P15 0:1).
- **湯医: 0× trong file này** (không xuất hiện "Yui" hay "Yunoi"). Cán cân không đổi: "Yunoi" vẫn dẫn.
- **"KiHa 07": 9 gloss (64, 1071, 1451, 1591, 1745, 1804, 1875, 1947, 2267)** — file có nhiều gloss "KiHa" nhất từ trước đến nay; thêm bằng chứng mạnh cho đề xuất thống nhất "KiHa" (chính tả JR).
- **Xưởng rượu "Migita Ichi" (1727, 1732):** VN theo đúng JP 右田一酒蔵元 + TW 右田一釀酒廠. Nhưng docs locations §2.6 nói xưởng rượu là "Migita System" — cả hai dạng cùng tồn tại trong dự án ("Migita System" 11 lần, "Migita Ichi" 15 lần, theo kiểm tra ở Paulette 09). Cần Hieu đối chiếu docs với JP — không tính là sai ở đây.
- **マスコン vs マスターコントローラー:** file này dùng "bộ điều khiển trung tâm" cho マスコン (1073, 1981) nhưng "Master Controller" cho マスターコントローラー (1664). Kiểm tra toàn dự án: マスコン được dịch "điều khiển trung tâm"/"bộ điều khiển trung tâm" ở mọi chỗ (10+ lần), còn マスターコントローラー dạng đầy đủ chỉ xuất hiện đúng 1 lần trong toàn dự án (chính dòng 1664 này). Vì vậy "bộ điều khiển trung tâm" mới là quy ước dự án — **không** sửa 1073/1981. Đề xuất: thống nhất cả hai dạng về "điều khiển trung tâm" (sửa 1664) hoặc giữ "Master Controller" cho dạng đầy đủ — Hieu quyết.

## Đề xuất cập nhật context (chưa chốt)

1. **マスコン/マスターコントローラー** — thống nhất về "điều khiển trung tâm" (quy ước dự án 10+ lần) thay vì để 1664 dùng "Master Controller" một mình. Hieu quyết.
2. Các đề xuất đang chờ vẫn giữ nguyên: 湯医 "Yunoi" vs "Yui"; "cô" vs "em"; 整備体/運転ボディ; "KiHa" vs "Kiha"; 帝鉄; コン; 駿袋鉄道; Migita System vs Migita Ichi.

## Đã kiểm tra và KHÔNG tính là sai

- **1742 [Soutetsu]** — JP 大根 (củ cải) vs TW 指控 (buộc tội — TW đọc sai): bản Việt "Củ cải (Daikon)?" theo đúng JP. Xác nhận quy tắc JP-trên-TW.
- **2336 [lời dẫn]** — JP れいなの足 (chân Reina) vs TW 手指 (ngón tay — TW sai): bản Việt "nhìn xuống chân Reina" theo đúng JP. Xác nhận quy tắc JP-trên-TW.
- **2637 [lời dẫn]** — JP 大根/ごぼう (củ cải/ngưu bàng) vs TW hoàn toàn lạc đề: bản Việt "trông giống rễ ngưu bàng hơn là củ cải" theo đúng JP. Xác nhận quy tắc JP-trên-TW.
- **1073/1981 [Soutetsu/Paulette]** — マスコン dịch "bộ điều khiển trung tâm": là quy ước toàn dự án (10+ lần), không sửa — xem đề xuất ở trên.
- **1664 [Paulette]** — マスターコントローラー dịch "Master Controller": dạng đầy đủ duy nhất trong dự án; giữ nguyên chờ Hieu chốt đề xuất thống nhất — xem đề xuất ở trên.
- **1549 [Soutetsu, Paulette 14]** — đã ghi ở file Paulette 14 (không thuộc file này, nhắc lại để đối chiếu): "anh" trong câu tường thuật suy nghĩ của Paulette thì giữ nguyên.

## Kết bài

Paulette 15 (36/408, 8,8%) — file sạch về cấu trúc (0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng chưa dịch, 0 dòng chưa chắc chắn), nhưng là **file đầu tiên mà Soutetsu tự xưng "em" áp đảo "anh"** (14 vs 6 trong thoại, cộng "Mình" 1 dòng thoại và "Em" 2 dòng độc thoại): người dịch file này chọn "em" làm dạng tự xưng mặc định khi Soutetsu nói với Mayami — trái docs và trái quy ước của các file Paulette gần đây (P11, P12: "anh" 0 lần; P13: "anh" 2 lần). Thuật ngữ 9 dòng thì quen thuộc (8 Ohitoyo + 1 Jutsusen). Bốn lỗi mất tiếng hít っ (1903, 1976, 1977, 1978) thuộc mẫu hệ thống đã biết — riêng "!" trơ trụi xuất hiện 206 lần trong toàn dự án, là ứng cử viên số một cho đợt quét thống nhất sau này.

**Còn lại cho file này:** không còn gì — sau khi áp 36 bản sửa, file coi như xong, trừ các quyết định đang chờ Hieu chốt (đặc biệt "cô" vs "em" — file này cho thêm 1 "em", tổng hợp P09–15 là "cô" 43 vs "em" 7; và マスコン/マスターコントローラー — đề xuất thống nhất về "điều khiển trung tâm").

**Tổng cộng: 27 file đã audit, 1.774 dòng sai** (25 file / 1.706 + 32 + 36).
