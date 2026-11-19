# Audit: Paulette 13_再評価 — 29 dòng Việt sai + 1 dòng chưa chắc chắn (đã đối chiếu JP + TW)

**Kết quả: 29/208 dòng sai (13,9%)** — 0 lệch vị trí, 0 chưa dịch, 0 cụt câu, **1 chưa chắc chắn (1357)**. File sạch về cấu trúc, lỗi tập trung ở thuật ngữ hệ thống (御一夜 13 dòng + 術仙 9 dòng) và thẻ %l thiếu dấu `;` (5 dòng). Cảnh: phiên họp hội đồng thành phố — Paulette biện luận bảo vệ kế hoạch Mine Treasure trước nghị sĩ Shinohara và các nghị viên, nghị án được thông qua; xen kẽ là cuộc điện thoại sáng sớm với Reina và Densha Hime.

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 208 dòng script** (thoại 97: Paulette 49, Soutetsu 17, lão nghị viên 16, chủ tọa 8, Reina 6, Fukami 1; lời dẫn 111) đối chiếu JP + TW từ CSV "Trang tính 3", target là TOML-2. TW chỉ là nhân chứng thứ hai; chỗ nào JP và TW mâu thuẫn thì theo JP (quy tắc Hieu đặt 19/11).
- Heuristic thoại↔lời dẫn báo **0 dòng** — bắt được 0/29. Toàn bộ lỗi đều là cùng-loại (thuật ngữ, thẻ, xưng hô, tiếng hít, SFX) nên heuristic không thấy được; thêm một bằng chứng nữa rằng heuristic chỉ là cận dưới.
- Không có key-shift sạch (shift 0: 208/208; các shift khác 0,961–0,990 — không có ý nghĩa vì key thưa và lỗi không phải lệch vị trí, không áp dụng).
- TOML và CSV giống hệt nhau về nội dung (133 dòng khác chỉ ở `\n`/khoảng trắng, 0 khác nội dung). Không có dòng CSV trống nào; VN==TW 1 dòng (1168 「……………………」 — giống hệt nhau ở cả ba thứ tiếng, không phải chưa dịch).
- `[selections]` rỗng (0 mục). Thẻ `%l`: 6 dòng có thẻ — **5 dòng thiếu dấu `;` đóng thẻ** (1397, 1366, 1596, 1637, 1641), chỉ 1674 đóng đúng. Xem đề xuất quét toàn dự án bên dưới.
- Phân loại lỗi: thuật ngữ 21 dòng (御一夜 13 — gồm 1353 mang cả hai lỗi; 術仙 9 — 1319/1320 thiếu gạch nối "Jutsusen", 7 dòng còn lại thiếu chữ "t" "Jussen"); thẻ %l thiếu `;` 5 dòng — trong đó 2 dòng kèm trong bản sửa thuật ngữ (1397, 1366) và 3 dòng riêng (1596, 1637, 1641); xưng hô 2 dòng (Soutetsu "anh" 1309/1479); mất tiếng hít っ 2 dòng (1483, 1484); sai nghĩa 1 dòng (SFX プッ 1952). Tổng 21 + 3 + 2 + 2 + 1 = 29 dòng sai. Theo người nói: Paulette 10, lời dẫn 10, lão nghị viên 4, chủ tọa 3, Soutetsu 2. **Chưa chắc chắn 1 dòng (1357, không đưa vào khối TOML).**
- Thoại sai 19/97 (19,6%), lời dẫn sai 10/111 (9,0%).
- Về xưng hô Soutetsu trong thoại: quét toàn bộ file bằng máy (đã chuẩn hoá `\n` thành khoảng trắng trước khi chạy regex `\b`, theo bài học Paulette 08) — "tôi/Tôi" 1 dòng (1471), "anh/Anh" tự xưng **2 lần** (1309, 1479 — cả hai đều sai), "em" ngôi hai 2 lần (1309, 1418 — đều gọi Paulette, giữ nguyên vì thuộc đề xuất đang chờ).
- Về "mình" trong độc thoại: 4 dòng chứa "mình" — **cả 4 đều đúng** (sở hữu cách "tình cảm của mình", phản thân "tự mình", mệnh đề phụ "như mình phải…", "rằng mình có thể…"). File này không có lỗi "mình" nào.
- Không có file trùng lặp: file này chỉ tồn tại ở 03_Paulette/ (đã kiểm tra md5 toàn bộ 227 file TOML-2; các cặp trùng khác đều là file Grand Rewrite — không liên quan file này).

## Kết luận về cơ chế lỗi

Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương, không có dòng mồ côi — đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (81.202 mục): 29/29 dòng sai chỉ xuất hiện đúng 1 lần trong toàn dự án, tại chính key của nó. 3 ngoại lệ đều là chuỗi ngắn chung chung, không phải câu của dòng khác:

- **1408 ("「Không sao đâu.」"), 1480 ("「Anh Soutetsu.」"), 1481 ("「Anh Soutetsu!」")**: mỗi chuỗi xuất hiện ở 2–3 file khác với JP tương đương (「大丈夫だ」/「平気」→ "Không sao đâu"; 「双鉄くん」→ "Anh Soutetsu") — đều là bản dịch đúng của JP riêng nó.

Cơ chế lỗi ở đây là **thuật ngữ hệ thống (21/29) + thẻ %l thiếu `;` (5/29)** — file này là file Paulette có tỉ lệ sai cao nhất kể từ Paulette 04 stove (22,1%), nhưng khác hẳn stove: không có một dòng lệch vị trí nào, lỗi chỉ là thuật ngữ chưa thống nhất theo các quyết định mới. Nếu trừ 21 dòng thuật ngữ, file chỉ còn 8 lỗi thực chất (3,8%) — ngang nhóm file sạch. Điểm đáng chú ý nhất: đây là **file đầu tiên trong route Paulette mà Soutetsu gọi Paulette là "em" nhiều hơn "cô"** (xem bằng chứng bên dưới) — phá vỡ chuỗi 4 file liên tiếp nghiêng về "cô".

## Chi tiết 29 dòng sai

### Thuật ngữ — 御一夜 (13 dòng)

**1156 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: ……最後の質問者は篠原議員。
御一夜市議会の生き字引とも言われる、長老議員だ。
- TW: ……最後提問的是篠原議員，他是被稱為御一夜市議會活字典的長老級議員。
- Cũ: ……Người đặt câu hỏi cuối cùng là nghị sĩ Shinohara.
Ông là một nghị sĩ lão làng, được mệnh danh là từ điển sống của Hội đồng thành phố Ohimitera.
- Sửa: ……Người đặt câu hỏi cuối cùng là nghị sĩ Shinohara. Ông là một nghị sĩ lão làng, được mệnh danh là từ điển sống của Hội đồng thành phố Ohitoyo.

**1352 [chủ tọa]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「御一夜市民の会、篠原くーん」
- TW: 「御一夜市民會，篠原議員」
- Cũ: 「Hội công dân Ohimitera, nghị sĩ Shinohara.」
- Sửa: 「Hội công dân Ohitoyo, nghị sĩ Shinohara.」

**1353 [lão nghị viên]** — 御一夜 = "Ohitoyo" + 術仙炭鉱 = "mỏ than Jutsu-sen" (dòng duy nhất mang cả hai lỗi thuật ngữ); bản cũ "Ohimitera" và "Mỏ than Jussen".

- JP: 「御一夜が術仙炭鉱にどれほど多くを注ぎ込んだか……
その誤った判断の、あれは、醜か残りカスたい」
- TW: 「御一夜曾經在術仙煤礦上幾乎投入了一切……那個廢煤礦，正是當初的錯誤判斷所留下的醜陋傷疤」
- Cũ: 「Ohimitera đã đổ bao nhiêu công sức và của cải vào Mỏ than Jussen……
Đó là, tàn dư xấu xí của một quyết định sai lầm.」
- Sửa: 「Ohitoyo đã đổ bao nhiêu công sức và của cải vào Mỏ than Jutsu-sen…… Đó là, tàn dư xấu xí của một quyết định sai lầm.」

**1365 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「御一夜がもとから持っているもの――
その再評価を、マイントレジャー計画は望むだけです」
- TW: 「我們煤探樂園計劃的初衷，就只是希望對御一夜原本擁有的資源重新進行評價」
- Cũ: 「Những gì Ohimitera vốn dĩ đã có――
Kế hoạch Mine Treasure chỉ mong muốn được đánh giá lại những thứ đó thôi ạ.」
- Sửa: 「Những gì Ohitoyo vốn dĩ đã có―― Kế hoạch Mine Treasure chỉ mong muốn được đánh giá lại những thứ đó thôi ạ.」

**1372 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「御一夜のかつての判断が、決して過ちではなかったと
――それが証明されることを、わたしは確信しています」
- TW: 「我相信一定能夠證明，御一夜曾經的判斷絕不是個錯誤」
- Cũ: 「Quyết định trong quá khứ của Ohimitera tuyệt đối không phải là một sai lầm
――Tôi tin chắc rằng điều đó sẽ được chứng minh ạ.」
- Sửa: 「Quyết định trong quá khứ của Ohitoyo tuyệt đối không phải là một sai lầm――Tôi tin chắc rằng điều đó sẽ được chứng minh ạ.」

**1374 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「父の愛した御一夜を、その歴史をわたしは信じています。
議員の皆さまに於かれましても、それは同様と信じます」
- TW: 「我相信父親所熱愛的御一夜，相信其一路走來的歷史。我相信各位議員也與我一樣」
- Cũ: 「Tôi tin vào Ohimitera mà cha tôi đã yêu thương, tin vào lịch sử của nó.
Tôi tin rằng các vị nghị sĩ ở đây cũng có cùng suy nghĩ đó ạ.」
- Sửa: 「Tôi tin vào Ohitoyo mà cha tôi đã yêu thương, tin vào lịch sử của nó. Tôi tin rằng các vị nghị sĩ ở đây cũng có cùng suy nghĩ đó ạ.」

**1376 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「その方々と、テーマパークの従業員となる若者たちとの
交流は、御一夜に新たな活気を呼ぶはずです」
- TW: 「我相信，通過那些人和主題公園所僱傭的年輕工作人員之間所進行的交流，一定能為御一夜的發展注入新的動力」
- Cũ: 「Sự giao lưu giữa những người đó và những người trẻ tuổi sẽ trở thành nhân viên của công viên chủ đề
chắc chắn sẽ mang lại sức sống mới cho Ohimitera ạ.」
- Sửa: 「Sự giao lưu giữa những người đó và những người trẻ tuổi sẽ trở thành nhân viên của công viên chủ đề chắc chắn sẽ mang lại sức sống mới cho Ohitoyo ạ.」

**1397 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera". Thẻ %l của ストーブ客車 thiếu dấu `;` đóng thẻ (JP có `%l;#;`) — sửa luôn trong cùng một dòng.

- JP: 「はい。\x%lストーブ客車;#00ffc040;ストーブ客車%l;#;、明日にも御一夜に届くそうです。
しかも、議案通過がならなくても、返却不要ってことで」
- TW: 「是的。\x%lストーブ客車;#00ffc040;暖爐客車%l;#;明天就可以送到御一夜。而且她還說就算議會沒有通過議案，也不用把車廂送回來」
- Cũ: 「Vâng. \x%lストーブ客車;#00ffc040;Toa xe sưởi ấm%l;#, nghe nói ngày mai sẽ đến Ohimitera.
Hơn nữa, cô ấy còn bảo dù nghị án không được thông qua, thì cũng không cần trả lại.」
- Sửa: 「Vâng. \x%lストーブ客車;#00ffc040;Toa xe sưởi ấm%l;#;, nghe nói ngày mai sẽ đến Ohitoyo. Hơn nữa, cô ấy còn bảo dù nghị án không được thông qua, thì cũng không cần trả lại.」

**1593 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 昨年度の御一夜市の宿泊観光客数は４０万人。
宿泊せず、観光施設を利用した客数がその他に３０万人だ。
- TW: 上一年在御一夜市住宿的觀光訪客約有４０萬人次。而不住宿僅是觀光的人次還有３０萬。
- Cũ: Số lượng khách du lịch lưu trú tại thành phố Ohimitera năm ngoái là 400 nghìn người.
Số lượng khách không lưu trú mà chỉ sử dụng các cơ sở du lịch là 300 nghìn người.
- Sửa: Số lượng khách du lịch lưu trú tại thành phố Ohitoyo năm ngoái là 400 nghìn người. Số lượng khách không lưu trú mà chỉ sử dụng các cơ sở du lịch là 300 nghìn người.

**1608 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: こうなった以上マイントレジャーに賛同し成功させるのが、
御一夜市にも隈銀にも、最善の選択となるのだから。
- TW: 事已至此，支持並推進煤探樂園計劃，也就成了御一夜市和隈元銀行最好的選擇。
- Cũ: Một khi đã thế này, việc tán thành và giúp Mine Treasure thành công,
chính là lựa chọn tốt nhất cho cả thành phố Ohimitera lẫn ngân hàng Kumagin.
- Sửa: Một khi đã thế này, việc tán thành và giúp Mine Treasure thành công, chính là lựa chọn tốt nhất cho cả thành phố Ohitoyo lẫn ngân hàng Kumagin.

**1683 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: ああ、これは……稀咲が警告してくれたとおり――
御一夜市そのものの持つ、傷跡なのだ。
- TW: 啊，原來這就是稀咲曾經警告過我們的——御一夜市的傷疤嗎。
- Cũ: A, đây là……đúng như lời Kisaki đã cảnh báo――
là vết sẹo của chính thành phố Ohimitera.
- Sửa: A, đây là……đúng như lời Kisaki đã cảnh báo―― là vết sẹo của chính thành phố Ohitoyo.

**1701 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: それを、僕らは掘り返す。
御一夜に淀んでいた力を呼び覚まし、観光客の力も借りて。
- TW: 就由我們來將這些東西開發出來。與遊客一同，發掘御一夜沉睡的活力。
- Cũ: Chúng tôi sẽ đào xới những thứ đó lên.
Đánh thức sức mạnh đang đọng lại ở Ohimitera, mượn cả sức mạnh của khách du lịch.
- Sửa: Chúng tôi sẽ đào xới những thứ đó lên. Đánh thức sức mạnh đang đọng lại ở Ohitoyo, mượn cả sức mạnh của khách du lịch.

**1724 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 御一夜の長い停滞のその一因は、
確実に、そうした断絶にもあるだろう。
- TW: 御一夜長期發展停滯也有著代溝這方面的原因吧。
- Cũ: Một trong những nguyên nhân khiến Ohimitera trì trệ trong một thời gian dài,
chắc chắn cũng là do sự đứt gãy đó.
- Sửa: Một trong những nguyên nhân khiến Ohitoyo trì trệ trong một thời gian dài, chắc chắn cũng là do sự đứt gãy đó.

### Thuật ngữ — 術仙炭鉱 (9 dòng)

**1319 [chủ tọa]** — 術仙炭鉱 = "mỏ than Jutsu-sen" (chuẩn có gạch nối, tiền lệ 廃炭鉱); bản cũ "Jutsusen" thiếu gạch nối.

- JP: 「賛成多数と認め、本案を可決いたします。続いて、
『旧術仙炭鉱の技術継承炭鉱としての助成申請案』」
- TW: 「多數人贊成，本議案通過。接著是“原術仙煤礦申請技術繼承煤礦補助金草案”」
- Cũ: 「Đa số tán thành, nghị án này được thông qua. Tiếp theo là,
『Nghị án xin trợ cấp cho mỏ than cũ Jutsusen với tư cách là mỏ than kế thừa kỹ thuật』.」
- Sửa: 「Đa số tán thành, nghị án này được thông qua. Tiếp theo là, 『Nghị án xin trợ cấp cho mỏ than cũ Jutsu-sen với tư cách là mỏ than kế thừa kỹ thuật』.」

**1320 [chủ tọa]** — 術仙炭鉱 = "mỏ than Jutsu-sen" (chuẩn có gạch nối); bản cũ "Jutsusen" thiếu gạch nối.

- JP: 「賛成多数と認め、本案を可決いたします。続いて、
『マイントレジャーによる術仙炭鉱地域再開発』案」
- TW: 「多數人贊成，本議案通過。接著是“通過煤探樂園進行術仙煤礦再開發草案”」
- Cũ: 「Đa số tán thành, nghị án này được thông qua. Tiếp theo là,
Nghị án 『Tái phát triển khu vực mỏ than Jutsusen thông qua Mine Treasure』.」
- Sửa: 「Đa số tán thành, nghị án này được thông qua. Tiếp theo là, Nghị án 『Tái phát triển khu vực mỏ than Jutsu-sen thông qua Mine Treasure』.」

**1366 [lão nghị viên]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" thiếu chữ "t". Thẻ %l của エアクラ thiếu dấu `;` đóng thẻ — sửa luôn trong cùng một dòng.

- JP: 「術仙炭鉱の再検証なしに\x%lエアクラ;#00ffc040;エアクラ%l;#;工場を誘致して――
目ぇ瞑ったまま、手ば引いてもらおうとしておったのか」
- TW: 「我們竟沒有重新審查術仙煤礦的可能性，就決定支持\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶——簡直就是閉著眼睛，讓人牽著走啊」
- Cũ: 「Mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;# mà không hề kiểm chứng lại Mỏ than Jussen――
Chẳng khác nào nhắm mắt đưa chân để người ta dắt đi sao.」
- Sửa: 「Mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; mà không hề kiểm chứng lại Mỏ than Jutsu-sen―― Chẳng khác nào nhắm mắt đưa chân để người ta dắt đi sao.」

**1422 [lão nghị viên]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" thiếu chữ "t".

- JP: 「石炭需要がのうなったと、そいば打ち切られたとき。
術仙炭鉱の命脈もまた、尽きたとです」
- TW: 「當不需要煤礦的時候，國家馬上就收回了援助。術仙煤礦的命運也止步於此」
- Cũ: 「Khi nhu cầu than đá không còn, nguồn trợ cấp đó bị cắt đứt.
Mệnh mạch của Mỏ than Jussen cũng theo đó mà cạn kiệt.」
- Sửa: 「Khi nhu cầu than đá không còn, nguồn trợ cấp đó bị cắt đứt. Mệnh mạch của Mỏ than Jutsu-sen cũng theo đó mà cạn kiệt.」

**1446 [Paulette]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" thiếu chữ "t".

- JP: 「術仙炭鉱にはまだ多くの石炭が眠り。
それだけにとどまらぬ、無数の価値が眠っているのです」
- TW: 「術仙煤礦現在煤礦儲量還很豐富。不僅如此，還有著很多可供開發的地方」
- Cũ: 「Mỏ than Jussen vẫn còn rất nhiều than đá đang ngủ yên.
Không chỉ dừng lại ở đó, còn vô số giá trị khác đang ngủ yên ở đó ạ.」
- Sửa: 「Mỏ than Jutsu-sen vẫn còn rất nhiều than đá đang ngủ yên. Không chỉ dừng lại ở đó, còn vô số giá trị khác đang ngủ yên ở đó ạ.」

**1447 [Paulette]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" thiếu chữ "t".

- JP: 「術仙炭鉱は、廃坑のぎりぎりまで設備投資と
技術練磨とを惜しまなかった」
- TW: 「術仙煤礦直到被廢棄的前一刻也在不惜成本進行設備投資和技術培訓」
- Cũ: 「Mỏ than Jussen, cho đến tận lúc sắp đóng cửa, vẫn không tiếc công đầu tư thiết bị
và mài giũa kỹ thuật.」
- Sửa: 「Mỏ than Jutsu-sen, cho đến tận lúc sắp đóng cửa, vẫn không tiếc công đầu tư thiết bị và mài giũa kỹ thuật.」

**1448 [Paulette]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" thiếu chữ "t".

- JP: 「術仙炭鉱の再評価は、第三者によって行われるべきです。
国により、観光客により、若者により」
- TW: 「術仙煤礦需要由第三者來重新評價。由國家、遊客、還有年輕人們」
- Cũ: 「Việc đánh giá lại Mỏ than Jussen nên được thực hiện bởi bên thứ ba.
Bởi quốc gia, bởi khách du lịch, bởi những người trẻ tuổi.」
- Sửa: 「Việc đánh giá lại Mỏ than Jutsu-sen nên được thực hiện bởi bên thứ ba. Bởi quốc gia, bởi khách du lịch, bởi những người trẻ tuổi.」

**1477 [lão nghị viên]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" thiếu chữ "t".

- JP: 「旧術仙炭鉱も、助成金を頼りに運営されていたことを、
知っておられますか」
- TW: 「那您知道舊術仙煤礦曾經也是依靠補助金運營的事吧」
- Cũ: 「Thị trưởng có biết rằng Mỏ than Jussen cũ
cũng từng được vận hành dựa vào tiền trợ cấp không?」
- Sửa: 「Thị trưởng có biết rằng Mỏ than Jutsu-sen cũ cũng từng được vận hành dựa vào tiền trợ cấp không?」

### Lỗi nhỏ — thẻ %l thiếu dấu `;` (3 dòng riêng)

**1596 [lời dẫn]** — Thẻ %l của エアクラ thiếu dấu `;` đóng thẻ (JP luôn có `%l;#;`). Nội dung câu đúng, chỉ sai cấu trúc thẻ.

- JP: \x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致賛成派と反対派と――
それだけでなく、無力感が生んでしまった、世代間の――
- TW: 不光是\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶支持派和反對派之間，年輕人和老年人之間也存在著代溝——
- Cũ: Phe ủng hộ và phe phản đối mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#――
Không chỉ vậy, còn là sự đứt gãy giữa các thế hệ do cảm giác bất lực sinh ra――
- Sửa: Phe ủng hộ và phe phản đối mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;―― Không chỉ vậy, còn là sự đứt gãy giữa các thế hệ do cảm giác bất lực sinh ra――

**1637 [lời dẫn]** — Thẻ %l của エアクラ thiếu dấu `;` đóng thẻ. Nội dung câu đúng, chỉ sai cấu trúc thẻ.

- JP: 元忠氏の存在は、\x%lエアクラ;#00ffc040;エアクラ%l;#;推進誘致派の議員たちへの、
おそらくは、強烈な締め付けとして働くだろう。
- TW: 光是寶生元忠在場，就能給支持\x%lエアクラ;#00ffc040;空凝機%l;#;落戶的議員們起到強烈的警示作用。
- Cũ: Sự hiện diện của ông Mototada,
có lẽ sẽ đóng vai trò như một sự răn đe mạnh mẽ đối với các nghị sĩ thuộc phe ủng hộ mời gọi \x%lエアクラ;#00ffc040;Aircra%l;#.
- Sửa: Sự hiện diện của ông Mototada, có lẽ sẽ đóng vai trò như một sự răn đe mạnh mẽ đối với các nghị sĩ thuộc phe ủng hộ mời gọi \x%lエアクラ;#00ffc040;Aircra%l;#;.

**1641 [lời dẫn]** — Thẻ %l của 乗務鞄 thiếu dấu `;` đóng thẻ. Nội dung câu đúng (gloss "cặp lái tàu" cho 乗務鞄 là chấp nhận được), chỉ sai cấu trúc thẻ.

- JP: ハチロク、日々姫、れいな、ふかみと凪はもちろん、
真闇姉に蓑笠老人――赤井宮司に、\x%l乗務鞄;#00ffc040;乗務鞄%l;#;の姿まである。
- TW: 八六、日日姬、玲奈、深美還有凪自不必說，甚至真闇姐和蓑笠爺爺、赤井宮司，還有他的\x%l乗務鞄;#00ffc040;乘務包%l;#;也在。
- Cũ: Hachiroku, Hibiki, Reina, Fukami và Nagi thì khỏi phải nói,
cả chị Mayami, ông lão Minokasa――Đại tư tế Akai, và cả chiếc \x%l乗務鞄;#00ffc040;cặp lái tàu%l;# cũng có mặt.
- Sửa: Hachiroku, Hibiki, Reina, Fukami và Nagi thì khỏi phải nói, cả chị Mayami, ông lão Minokasa――Đại tư tế Akai, và cả chiếc \x%l乗務鞄;#00ffc040;cặp lái tàu%l;#; cũng có mặt.

### Xưng hô (2 dòng)

**1309 [Soutetsu]** — Soutetsu tự xưng "Anh" khi nói với Paulette — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). Chỉ sửa đại từ tự xưng; "Em" gọi Paulette giữ nguyên (thuộc đề xuất "cô"/"em" đang chờ chốt).

- JP: 「うん。見ていた。
とても、見事だった」
- TW: 「嗯。我看著呢。你做得非常漂亮」
- Cũ: 「Ừ. Anh có xem mà.
Em làm rất xuất sắc.」
- Sửa: 「Ừ. Tôi có xem mà. Em làm rất xuất sắc.」

**1479 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Paulette — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「ならば、ご褒美をもらえるか？」
- TW: 「那，我有獎勵嗎？」
- Cũ: 「Vậy thì, anh có được nhận phần thưởng không?」
- Sửa: 「Vậy thì, tôi có được nhận phần thưởng không?」

### Lỗi nhỏ — mất tiếng hít っ (2 dòng)

**1483 [Paulette]** — JP 「っ！」 là tiếng hít độc lập; bản cũ 「!」 làm mất tiếng hít. Tiền lệ 再開発 2103/2537: sửa thành "Ư!".

- JP: 「っ！」
- TW: 「！」
- Cũ: 「!」
- Sửa: 「Ư!」

**1484 [Paulette]** — JP 「っ！？」 là tiếng hít độc lập; bản cũ 「!?」 làm mất tiếng hít. Tiền lệ 再開発 2103/2537: sửa thành "Ư!?".

- JP: 「っ！？」
- TW: 「！？」
- Cũ: 「!?」
- Sửa: 「Ư!?」

### Sai nghĩa (1 dòng)

**1952 [lời dẫn]** — プッ là tiếng bật nhẹ của môi (ngay sau tiếng hôn ちゅっ ở 1951), không phải tiếng bíp điện tử ("Tít" thuộc họ ピー/ピッ). TW 喀噠 ("cạch") cũng chỉ là phỏng đoán, không theo. Sửa thành "（Bụp）".

- JP: （プッ）
- TW: （喀噠）
- Cũ: （Tít）
- Sửa: （Bụp）

## Dòng chưa chắc chắn (1 dòng — KHÔNG đưa vào khối TOML)

**1357 [Paulette]** — Paulette tự xưng "em" giữa cảnh họp hội đồng. Các lần tự xưng khác của Paulette trong cảnh này đều là "tôi" (1258, 1260, 1267, 1285, 1327, 1331, 1335, 1356, 1363, 1364, 1365, 1372, 1374, 1376); "em" chỉ đúng nếu cô đang nói với Soutetsu ở cánh gà — 1884 xác nhận Soutetsu đứng ở 舞台袖 xem phiên họp, nhưng file không nói cô có quay sang anh hay không. Đã kiểm tra theo quy tắc cột Character: cột Character = ポーレット, 5 dòng xung quanh (1352–1364) toàn là câu trang trọng trong phiên họp, TW = 我 — đều không cho biết người nghe. Cần Hieu kiểm tra trong game: nếu cô nói với Soutetsu thì "Em" đúng, giữ nguyên; nếu nói với cả hội trường thì sửa thành "Tôi——tôi, làm được rồi!".

- JP: 「わたし――わたし、やりました！」
- TW: 「我——我做到了！」
- Cũ: 「Em——em, làm được rồi!」
- Sửa: (chưa có — chờ Hieu chốt)

## Bằng chứng cho các quyết định đang chờ Hieu chốt

- **Soutetsu gọi Paulette "cô" vs "em" (thoại trực tiếp): "em" 2 lần** (1309, 1418) **vs "cô" 0 lần** — **file đầu tiên trong route Paulette nghiêng về "em"**. Lưu ý: 1163 có "cô ấy" nhưng là ngôi ba (Soutetsu nói về Paulette với người khác), không tính vào cách gọi trực tiếp. Cộng dồn: Paulette 08 đề xuất "em", Paulette 09 "cô" 7 vs "em" 1, Paulette 10 "cô" 20 vs "em" 2, Paulette 11 "cô" 9 vs "em" 0, Paulette 12 "cô" 7 vs "em" 0, Paulette 13 "cô" 0 vs "em" 2 — **cộng dồn P09–13: "cô" 43 vs "em" 5**. File này phá vỡ chuỗi 4 file liên tiếp nghiêng về "cô" — bằng chứng mới cho đề xuất thống nhất "em" (Paulette 08 1534). **Không quyết, chỉ ghi số liệu.**
- **Paulette tự xưng theo người nghe (đúng quy cách, ghi nhận):** "tôi" trong cảnh hội đồng (9 dòng), "em" với Soutetsu (1424 — rõ ràng, nhắc đến 双鉄くん; 1357 chưa chắc chắn, xem trên), "chị" với Reina (1390, 1395), "cháu" với Densha Hime (1401).
- **湯医 / 帝鉄 / コン / タブレット: 0 lần xuất hiện trong file này** (cả JP lẫn VN) — không có bằng chứng mới cho các quyết định đang chờ.
- **御一夜: JP 13 lần, VN cũ "Ohimitera" 13 lần, "Ohito"/"Ohitoyo" 0 lần** — đã sửa hết thành "Ohitoyo" trong khối TOML; file không còn dạng cũ nào.
- **術仙: JP 9 lần, VN cũ "Jussen" 7 lần + "Jutsusen" 2 lần** — đã sửa hết thành "Jutsu-sen" trong khối TOML.

## Đề xuất cập nhật context

1. **Thẻ %l thiếu dấu `;` đóng thẻ — đề xuất quét toàn dự án.** Kiểm tra toàn dự án: thẻ %l trong JP luôn đóng bằng `%l;#;` (4756/4756), nhưng bản Việt thiếu `;` ở **151 chỗ** (5003 có, 151 thiếu). File này có 5 thẻ thiếu `;` (1397, 1366, 1596, 1637, 1641) và Paulette 12 có 1 thẻ (1121) — cả 6 đều đã sửa trong khối TOML của hai file. Nếu thẻ thiếu `;` làm parser TIPS đọc sai thì 151 dòng này đều cần sửa; nếu game vẫn hiển thị đúng thì đây chỉ là lỗi thẩm mỹ. Đề xuất: Hieu kiểm tra một dòng có thẻ thiếu `;` trong game (ví dụ Paulette 13 1596) rồi quyết định có quét toàn dự án hay không.
2. **Không có đề xuất mới nào khác.** Lưu ý: 1472 "Quảng trường Shirakabe" theo đúng furigana JP [しらかべ,1]白壁 (TW viết theo tên thật ngoài đời là 黒壁 "Kurokabe") — bản Việt theo JP là đúng, không tính sai, không cần đề xuất.

## Những dòng đã kiểm tra và KHÔNG tính sai

- **1168**: VN==TW ("「……………………」") — giống hệt nhau ở cả ba thứ tiếng, không phải chưa dịch.
- **1303/1307**: cùng VN "「Ư, m.」" — JP khác nhau (う、ん vs う、む) nhưng đều là tiếng ngập ngừng; bản Việt phiên âm giống nhau là cách làm nhất quán trong file, không tính sai.
- **1175**: "Cảm ơn cô, vì một phần biện luận tuyệt vời." — lão nghị viên gọi Paulette (thị trưởng) là "cô" là xưng hô lịch sự tự nhiên trong tiếng Việt; JP không có từ gọi nhưng thêm vào không đổi nghĩa.
- **1301**: えっ！？ → "Hả!?" — っ nằm trong từ えっ, đã dịch đúng bằng "Hả!?".
- **1295**: やったばいっ！！ → "Làm được rồi nè!!" — っ cuối câu là nhấn mạnh, đã dịch bằng "!!".
- **1306**: ちょっ！？ → "Khoan đã!?" — ちょっ là từ ちょっと rút gọn, đã dịch đúng.
- **1481**: 双鉄くんっ！ → "Anh Soutetsu!" — っ nhấn mạnh, đã dịch bằng "!".
- **1831**: "Nagi lấy hai tay bịt chặt miệng lại——っ!?" — tiếng hít っ được GIỮ nguyên trong bản cũ, đúng — chứng tỏ trong dự án đã có sẵn cả hai cách viết (giữ っ và "Ư"); các bản sửa tiếng hít trong audit này theo tiền lệ "Ư" (再開発 2103/2537, Paulette 09/11).
- **1795**: TW viết sai thành "展示預算表格" (trình bày bảng ngân sách) trong khi JP chỉ là "đưa bảng lật ra phía trước" — bản Việt theo đúng JP, không tính sai. Một ca JP-trên-TW điển hình.
- **1816**: TW thêm "親吻著對方的嘴唇" (hôn môi nhau) trong khi JP chỉ nói "trao nhau phần thưởng" — bản Việt theo đúng JP, không tính sai. Một ca JP-trên-TW điển hình.
- **1472**: "Quảng trường Shirakabe" theo furigana JP, không theo tên thật 黒壁 của TW — đúng theo quy tắc JP-trên-TW.
- **1742**: "chúng tôi thậm chí còn không nghĩ rằng mình có thể đánh giá lại nó" — "mình" nằm trong mệnh đề phụ ("rằng mình có thể…"), giữ nguyên theo tiền lệ Hachiroku 12.
- **1768/1753/1917**: "mình" trong "như mình phải…", "tình cảm của mình", "tự mình" — đều là mệnh đề phụ / sở hữu / phản thân, giữ nguyên.

## Khối TOML sửa (đã kiểm chứng: parse được, đúng 29/29 key)

```toml
1156 = "……Người đặt câu hỏi cuối cùng là nghị sĩ Shinohara. Ông là một nghị sĩ lão làng, được mệnh danh là từ điển sống của Hội đồng thành phố Ohitoyo."
1309 = "「Ừ. Tôi có xem mà. Em làm rất xuất sắc.」"
1319 = "「Đa số tán thành, nghị án này được thông qua. Tiếp theo là, 『Nghị án xin trợ cấp cho mỏ than cũ Jutsu-sen với tư cách là mỏ than kế thừa kỹ thuật』.」"
1320 = "「Đa số tán thành, nghị án này được thông qua. Tiếp theo là, Nghị án 『Tái phát triển khu vực mỏ than Jutsu-sen thông qua Mine Treasure』.」"
1352 = "「Hội công dân Ohitoyo, nghị sĩ Shinohara.」"
1353 = "「Ohitoyo đã đổ bao nhiêu công sức và của cải vào Mỏ than Jutsu-sen…… Đó là, tàn dư xấu xí của một quyết định sai lầm.」"
1365 = "「Những gì Ohitoyo vốn dĩ đã có―― Kế hoạch Mine Treasure chỉ mong muốn được đánh giá lại những thứ đó thôi ạ.」"
1366 = "「Mời gọi nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; mà không hề kiểm chứng lại Mỏ than Jutsu-sen―― Chẳng khác nào nhắm mắt đưa chân để người ta dắt đi sao.」"
1372 = "「Quyết định trong quá khứ của Ohitoyo tuyệt đối không phải là một sai lầm ――Tôi tin chắc rằng điều đó sẽ được chứng minh ạ.」"
1374 = "「Tôi tin vào Ohitoyo mà cha tôi đã yêu thương, tin vào lịch sử của nó. Tôi tin rằng các vị nghị sĩ ở đây cũng có cùng suy nghĩ đó ạ.」"
1376 = "「Sự giao lưu giữa những người đó và những người trẻ tuổi sẽ trở thành nhân viên của công viên chủ đề chắc chắn sẽ mang lại sức sống mới cho Ohitoyo ạ.」"
1397 = "「Vâng. \\x%lストーブ客車;#00ffc040;Toa xe sưởi ấm%l;#;, nghe nói ngày mai sẽ đến Ohitoyo. Hơn nữa, cô ấy còn bảo dù nghị án không được thông qua, thì cũng không cần trả lại.」"
1422 = "「Khi nhu cầu than đá không còn, nguồn trợ cấp đó bị cắt đứt. Mệnh mạch của Mỏ than Jutsu-sen cũng theo đó mà cạn kiệt.」"
1446 = "「Mỏ than Jutsu-sen vẫn còn rất nhiều than đá đang ngủ yên. Không chỉ dừng lại ở đó, còn vô số giá trị khác đang ngủ yên ở đó ạ.」"
1447 = "「Mỏ than Jutsu-sen, cho đến tận lúc sắp đóng cửa, vẫn không tiếc công đầu tư thiết bị và mài giũa kỹ thuật.」"
1448 = "「Việc đánh giá lại Mỏ than Jutsu-sen nên được thực hiện bởi bên thứ ba. Bởi quốc gia, bởi khách du lịch, bởi những người trẻ tuổi.」"
1477 = "「Thị trưởng có biết rằng Mỏ than Jutsu-sen cũ cũng từng được vận hành dựa vào tiền trợ cấp không?」"
1479 = "「Vậy thì, tôi có được nhận phần thưởng không?」"
1483 = "「Ư!」"
1484 = "「Ư!?」"
1593 = "Số lượng khách du lịch lưu trú tại thành phố Ohitoyo năm ngoái là 400 nghìn người. Số lượng khách không lưu trú mà chỉ sử dụng các cơ sở du lịch là 300 nghìn người."
1596 = "Phe ủng hộ và phe phản đối mời gọi nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;―― Không chỉ vậy, còn là sự đứt gãy giữa các thế hệ do cảm giác bất lực sinh ra――"
1608 = "Một khi đã thế này, việc tán thành và giúp Mine Treasure thành công, chính là lựa chọn tốt nhất cho cả thành phố Ohitoyo lẫn ngân hàng Kumagin."
1637 = "Sự hiện diện của ông Mototada, có lẽ sẽ đóng vai trò như một sự răn đe mạnh mẽ đối với các nghị sĩ thuộc phe ủng hộ mời gọi \\x%lエアクラ;#00ffc040;Aircra%l;#;."
1641 = "Hachiroku, Hibiki, Reina, Fukami và Nagi thì khỏi phải nói, cả chị Mayami, ông lão Minokasa――Đại tư tế Akai, và cả chiếc \\x%l乗務鞄;#00ffc040;cặp lái tàu%l;#; cũng có mặt."
1683 = "A, đây là……đúng như lời Kisaki đã cảnh báo―― là vết sẹo của chính thành phố Ohitoyo."
1701 = "Chúng tôi sẽ đào xới những thứ đó lên. Đánh thức sức mạnh đang đọng lại ở Ohitoyo, mượn cả sức mạnh của khách du lịch."
1724 = "Một trong những nguyên nhân khiến Ohitoyo trì trệ trong một thời gian dài, chắc chắn cũng là do sự đứt gãy đó."
1952 = "（Bụp）"
```

## Kết bài

Paulette 13 (29/208, 13,9%) — file Paulette có tỉ lệ sai cao nhất kể từ Paulette 04 stove (22,1%), nhưng bản chất hoàn toàn khác stove: không có một dòng lệch vị trí nào, 21/29 lỗi là thuật ngữ chưa thống nhất theo các quyết định mới (御一夜 13 + 術仙 9) và 5 dòng thẻ %l thiếu `;`. Trừ thuật ngữ ra, file chỉ còn 8 lỗi thực chất (3,8%) — ngang nhóm file sạch. Lỗi đáng chú ý nhất ngoài thuật ngữ là 1357 (chưa chắc chắn — cần Hieu kiểm tra trong game xem Paulette đang nói với Soutetsu hay với cả hội trường) và 1952 (プッ dịch thành "Tít" — tiếng bíp điện tử thay cho tiếng bật môi sau nụ hôn).

**Còn lại cho file này:** 1 dòng chưa chắc chắn (1357) — cần Hieu chốt người nghe rồi mới sửa. Hai việc chờ Hieu: (1) chốt 1357; (2) quyết định có quét toàn dự án cho 151 thẻ %l thiếu dấu `;` hay không (đề xuất 1 trên). Ngoài ra, file này là bằng chứng mới quan trọng cho quyết định "cô"/"em" — lần đầu tiên nghiêng về "em" (2 vs 0), phá vỡ chuỗi 4 file nghiêng về "cô".

**Bước tiếp theo:** Paulette 12 đã audit xong cùng đợt (7/194, 3,6% — xem `audit-paulette12-liberation-REVIEW.md`). Tổng cộng 25 file đã audit: 1.706 dòng sai.
