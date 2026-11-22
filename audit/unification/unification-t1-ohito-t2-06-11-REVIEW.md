# Unification batch U2b — T1 (御一夜 → "Ohitoyo") + T2 (御一夜鉄道 → "Đường sắt Ohitoyo"), folders 06–11

## §0. Phạm vi

- Mục: **T1** (DECIDED 19/11, Hieu — 御一夜 → "Ohitoyo") và **T2** (DECIDED 21/11 ~17:30, Muse theo uỷ quyền — 御一夜鉄道 → "Đường sắt Ohitoyo"). T2 là tập con của T1: áp dạng dài "Đường sắt Ohitoyo" trước, rồi dạng trần "Ohito" → "Ohitoyo"; một dòng chứa cả hai dạng = một mục, item "T1+T2".
- Thư mục: **06_Kisaki / 07_Nagi_Fukami / 08_Niiroku / 09_Grand / 10_Chikuni / 11_Other**. Các dòng chứa "Ohimitera" KHÔNG thuộc batch này (batch U1).
- Kết quả: **72 dòng sửa** — T2: 29, T1: 40, T1+T2: 3; tổng 76 lần xuất hiện dạng cũ ("Đường sắt Ohito" ×34 + "Ohito" trần ×42). Phân bố theo thư mục: 06_Kisaki 38, 07_Nagi_Fukami 19, **09_Grand 15, 08_Niiroku 0, 10_Chikuni 0, 11_Other 0** (12 file).
- So với ước lượng trong UNIFICATION-LIST.md §0 (T1 còn 219, T2 còn 132 toàn dự án): U2a đã xử lý 136 dòng ở 00–05; batch này xử lý 72 dòng ở 06–11. Đếm lại toàn dự án theo giá trị hiện tại (moan > audit > CSV3, xem §1): còn **213 dòng** "Ohito" trần (00–05: 141, 06–11: 72); U2a 136 + U2b 72 = 208; **còn lại 5 dòng** — cả 5 đều là dòng chứa CẢ "Ohimitera" lẫn "Ohito" trần (ở 01/02/05, ngoài phạm vi batch này — xem cờ F-T1T2-1 ở §3). Chênh với ước lượng §0 (219) là 6 dòng: §0 đã ghi rõ các số "còn lại" là ước lượng, không phải số cuối cùng.

## §1. Phương pháp liệt kê (chỉ đếm, không sửa hàng loạt)

1. Đọc CSV3 good-set 87.833 dòng (đã bỏ 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`; trong phạm vi 06–11, các file dual-set là ふかみh1/h2/h3 + lr_ふかみh1/h2 (good set ở 11_Other) và グランドリライト08_ふかみ (good set ở 09_Grand) — bộ stale ở 07_Nagi_Fukami đã bị loại).
2. Tính giá trị hiện tại (current value) cho mọi dòng trong 06–11: giá trị fix moan nếu (file,key) có trong bất kỳ `moans/moan-*-wrong.json` nào (gồm cả supplement ハチロクh3), nếu không thì giá trị fix audit nếu có trong bất kỳ `audit-*-wrong.json` nào, nếu không thì VN CSV3. Đã nạp toàn bộ 217 file audit (9.191 mục) + 66 file moan (1.535 mục). Ghép fix-list với CSV3 bằng cặp (key, JP); file dict-shape duy nhất trong phạm vi (`audit-lr-nagih2-wrong.json`, không có JP) được ghép bằng (basename, key). Không ứng viên nào nằm trong nhóm (key, JP) trùng lặp gây mơ hồ: 0 ứng viên ambiguous; cả 17 dòng audit-src đều có đúng 1 provider là audit file của chính file đó.
3. Ứng viên = current value chứa `Ohito` KHÔNG theo sau bởi `yo` (regex `Ohito(?!yo)` — bắt buộc, vì "Ohitoyo" đã đúng tự nó đã chứa chuỗi "Ohito") và KHÔNG chứa "Ohimitera". Được **72 ứng viên**, 76 lần xuất hiện dạng cũ. Trong phạm vi 06–11 có thêm **42 dòng chứa "Ohimitera"** (đã loại theo quy tắc batch): 4 dòng ở 06_Kisaki (thuộc U1b) và 38 dòng ở 07–11 (thuộc U1c) — tất cả đã được xử lý ở batch U1, không dòng nào trong 42 dòng này chứa thêm "Ohito" trần (đã kiểm chứng bằng máy: 0 dòng chứa cả hai dạng trong 06–11).
4. Kiểm chứng chéo current value với TOML-2 (216 file, tên file #U-escaped đã giải mã): 72/72 dòng đều có mặt; 55 dòng khớp tuyệt đối (flat-compare, literal `\n` dẹp thành khoảng trắng); 17 dòng audit-src TOML khớp CSV3 VN chứ không khớp old_vn — GIẢI THÍCH ĐƯỢC: TOML-2 là trạng thái pre-fix, audit fix chỉ áp vào lúc rebuild (cùng hiện tượng U2a đã ghi: audit-src khác ở phần không liên quan tới Ohito); cả 17 dòng đều truy được về đúng audit file của file đó, 1 provider duy nhất. Không dòng nào bị tính sai current value vì fix-list ghép trượt.
5. Đọc từng dòng ứng viên: JP (+TW) của cả 72 dòng đã được đọc hết (xem §2). Dạng JP: 御一夜鉄道 32, 御一夜 trần 40; không có dạng kana (オヒトヨ/おひとよ) hay viết tắt 御鉄 trong batch này. TW đồng ý 72/72 (mọi TW đều viết 御一夜/御一夜鐵路). Không có dòng nào "Ohito" nằm trong gloss %l (đã kiểm tra bằng máy: 0 lần xuất hiện trong thẻ %l) — mọi lần xuất hiện đều là display text.
6. Fix = chỉ thay thế đúng chuỗi mục tiêu, giữ nguyên toàn bộ phần còn lại (kể cả "Yui" ở グランドリライト06_稀咲 2146 — thuộc mục T7, không đụng; kể cả "ông nội của Fukami" ở 2159 — thuộc mục T20, không đụng; kể cả "hợp đồng Maitetsu" ở 凪h2 1766 — thuộc mục T74 OPEN, không đụng; kể cả các phần audit đã sửa khác trong 17 dòng audit-src). Thứ tự: "Đường sắt Ohito" → "Đường sắt Ohitoyo" trước, rồi "Ohito" trần còn lại → "Ohitoyo".

## §2. Quyết định trong batch (theo uỷ quyền của Hieu — điều tra JP+TW rồi quyết, không park)

- **D1 — "Thành phố Đường sắt Ohito" = T1, không phải T2 (2 dòng: 凪ふかみ08c_新しい家族 2420/2341).** Bằng chứng: JP của cả hai dòng đều là 『鉄道の町・御一夜』 (dạng trần 御一夜, "thành phố đường sắt" là danh hiệu của thị trấn), không hề có 御一夜鉄道 (tên công ty); TW của cả hai dòng đều viết 鐵路之城御一夜. VN cũ "Thành phố Đường sắt Ohito" chỉ là cách dịch "thành phố đường sắt" + tên thị trấn — chữ "Đường sắt" ở đây thuộc về "thành phố", không thuộc về tên công ty. Chuỗi fix cho ra vẫn giống hệt nhau ("Thành phố Đường sắt Ohitoyo") dù xếp T1 hay T2; xếp T1 cho đúng bản chất JP term. Tiền lệ: U2a quyết 御鉄 → T2 theo cùng logic "xếp theo JP term, không theo chuỗi VN bề mặt".
- **Không có quyết định OPEN nào khác trong batch.** T1/T2 đều DECIDED; mọi ứng viên đều có JP kanji xác nhận trực tiếp; không có kana, không có viết tắt, không có TW mâu thuẫn JP.

## 06_Kisaki — `グランドリライト06_稀咲.txt.toml` (16 dòng)

### key 2054 — item T2 (JP: 御一夜鉄道)

- JP: 「あるのかもしれんが、僕は知らん。\n御一夜鉄道では、ボランティアによる手作業だ」
- TW: 「可能有吧，我也不知道。在御一夜鐵路都是靠志願者手工完成的」
- old_vn (audit): 「Có lẽ là có, nhưng tôi không biết.\nỞ Đường sắt Ohito, công việc này do các tình nguyện viên làm thủ công.」
- fix: 「Có lẽ là có, nhưng tôi không biết.\nỞ Đường sắt Ohitoyo, công việc này do các tình nguyện viên làm thủ công.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2485 — item T2 (JP: 御一夜鉄道)

- JP: 「幾度となく、って……御一夜鉄道の列車なんて、\n増便した今だって、そんなには走っていないだろう？」
- TW: 「無數次……御一夜鐵路的列車就算現在增加了班次，跑得也不是很頻繁吧？」
- old_vn (csv3): 「Vô số lần sao……Tàu của Đường sắt Ohito,\ncho dù bây giờ đã tăng chuyến, cũng đâu có chạy nhiều đến thế?」
- fix: 「Vô số lần sao……Tàu của Đường sắt Ohitoyo,\ncho dù bây giờ đã tăng chuyến, cũng đâu có chạy nhiều đến thế?」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1923 — item T2 (JP: 御一夜鉄道)

- JP: 「しかし……帝都の大会社から、御一夜鉄道にというのは、\n僕の立場でいうのも何だが」
- TW: 「但是……要從帝都的大公司轉到御一夜鐵路這種地方，以我的立場來說也有些……」
- old_vn (audit): 「Nhưng……chuyển từ một công ty lớn ở Teito sang Đường sắt Ohito,\ndù nói ra từ lập trường của tôi thì cũng hơi...」
- fix: 「Nhưng……chuyển từ một công ty lớn ở Teito sang Đường sắt Ohitoyo,\ndù nói ra từ lập trường của tôi thì cũng hơi...」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2014 — item T2 (JP: 御一夜鉄道)

- JP: 「さっきもいったが、今や交換用のレールは希少だ。\nゆえ御一夜鉄道では、余程のことが無いと交換できない」
- TW: 「剛才我也說了，現在可以替換的鐵軌很稀少。所以在御一夜鐵路，不是特殊情況就沒辦法換鐵軌」
- old_vn (audit): 「Như tôi đã nói, hiện nay đường ray thay thế rất hiếm.\nVì vậy ở Đường sắt Ohito, trừ khi có chuyện bất đắc dĩ, nếu không thì không thể thay được.」
- fix: 「Như tôi đã nói, hiện nay đường ray thay thế rất hiếm.\nVì vậy ở Đường sắt Ohitoyo, trừ khi có chuyện bất đắc dĩ, nếu không thì không thể thay được.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2497 — item T2 (JP: 御一夜鉄道)

- JP: 「今の御一夜鉄道は、列車密度が極めて薄い。ので、\n\x%l保線;#00ffc040;保線%l;#;を丁寧に行うことで、レールを延命できている」
- TW: 「現在御一夜鐵路的車次密度非常低。所以能通過細心\x%l保線;#00ffc040;巡線%l;#;來延長鐵軌的壽命」
- old_vn (csv3): 「Hiện tại, mật độ tàu của Đường sắt Ohito cực kỳ thưa thớt. Do đó,\nbằng cách \x%l保線;#00ffc040;bảo trì đường ray%l;#; cẩn thận, chúng ta có thể kéo dài tuổi thọ của đường ray.」
- fix: 「Hiện tại, mật độ tàu của Đường sắt Ohitoyo cực kỳ thưa thớt. Do đó,\nbằng cách \x%l保線;#00ffc040;bảo trì đường ray%l;#; cẩn thận, chúng ta có thể kéo dài tuổi thọ của đường ray.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2146 — item T1 (JP: 御一夜)

- JP: 「四人がかり！　それを――いちいちやるのかい？\n線路って、だって、御一夜－[ゆのい,1]湯医の間だけでも」
- TW: 「四人合力！就這麼一路敲過去？可是線路那麼長，就算只是御一夜到湯醫之間就夠遠了」
- old_vn (csv3): 「Cần tới bốn người cơ á! Phải làm thế――từng chỗ một sao?\nĐường ray dài lắm mà, chỉ tính riêng đoạn giữa Ohito và Yui thôi cũng đã...」
- fix: 「Cần tới bốn người cơ á! Phải làm thế――từng chỗ một sao?\nĐường ray dài lắm mà, chỉ tính riêng đoạn giữa Ohitoyo và Yui thôi cũng đã...」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2159 — item T2 (JP: 御一夜鉄道)

- JP: 「[せき]堰さん――ふかみの祖父たち、\x%l保線;#00ffc040;保線%l;#;ボランティアの\n方々や、僕ら、御一夜鉄道に関わる者が、だ」
- TW: 「堰先生——深美的祖父他們兄弟幾人，還有\x%l保線;#00ffc040;巡線%l;#;志願者們，以及我們御一夜鐵路的工作人員」
- old_vn (csv3): 「Ông Seki――ông nội của Fukami, các tình nguyện viên \x%l保線;#00ffc040;bảo trì đường ray%l;#;,\nvà cả chúng ta, những người liên quan đến Đường sắt Ohito.」
- fix: 「Ông Seki――ông nội của Fukami, các tình nguyện viên \x%l保線;#00ffc040;bảo trì đường ray%l;#;,\nvà cả chúng ta, những người liên quan đến Đường sắt Ohitoyo.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2690 — item T2 (JP: 御一夜鉄道)

- JP: 「経験者を、有償で雇用する他なくなる。\nそのごく当然のことが、今の御一夜鉄道では厳しい」
- TW: 「那就只能有償僱傭有工作經驗的人了。這本來是理所當然的事情，但對現在的御一夜鐵路來說還是很困難」
- old_vn (csv3): 「Không còn cách nào khác ngoài việc thuê người có kinh nghiệm và trả lương cho họ.\nMột điều tưởng chừng như hiển nhiên đó, lại rất khó khăn đối với Đường sắt Ohito hiện tại.」
- fix: 「Không còn cách nào khác ngoài việc thuê người có kinh nghiệm và trả lương cho họ.\nMột điều tưởng chừng như hiển nhiên đó, lại rất khó khăn đối với Đường sắt Ohitoyo hiện tại.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3129 — item T2 (JP: 御一夜鉄道)

- JP: 御一夜鉄道は、\x%l保線;#00ffc040;保線%l;#;ボランティアに支えられているが、\nこれが有償雇用であれば、経営は恐らく立ち行かない。
- TW: 御一夜鐵路雖然現在有\x%l保線;#00ffc040;巡線%l;#;志願者的支持，但要是改成有償僱傭的話，經營恐怕就難以為繼了。
- old_vn (csv3): Đường sắt Ohito hiện đang được hỗ trợ bởi các tình nguyện viên \x%l保線;#00ffc040;bảo trì đường ray%l;#;,\nnhưng nếu phải trả lương để thuê người, e rằng sẽ không trụ nổi.
- fix: Đường sắt Ohitoyo hiện đang được hỗ trợ bởi các tình nguyện viên \x%l保線;#00ffc040;bảo trì đường ray%l;#;,\nnhưng nếu phải trả lương để thuê người, e rằng sẽ không trụ nổi.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2599 — item T2 (JP: 御一夜鉄道)

- JP: 「それは、すでにあるのかもしれん。\n僕が知らず、御一夜鉄道にも無いだけで」
- TW: 「說不定已經有了吧。只是我不知道，御一夜鐵路也沒有而已」
- old_vn (audit): 「Có khi thứ đó đã tồn tại rồi cũng nên.\nChỉ là tôi không biết, và Đường sắt Ohito cũng không có thôi.」
- fix: 「Có khi thứ đó đã tồn tại rồi cũng nên.\nChỉ là tôi không biết, và Đường sắt Ohitoyo cũng không có thôi.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2720 — item T2 (JP: 御一夜鉄道)

- JP: 「では何故、御一夜鉄道には無いんだい？\n導入できれば、作業負担を劇的に減らせるだろうに」
- TW: 「那麼御一夜鐵路為什麼沒有呢？明明引進就能大幅減輕工作負擔」
- old_vn (csv3): 「Vậy tại sao Đường sắt Ohito lại không có?\nNếu áp dụng được, gánh nặng công việc sẽ giảm đi đáng kể mà.」
- fix: 「Vậy tại sao Đường sắt Ohitoyo lại không có?\nNếu áp dụng được, gánh nặng công việc sẽ giảm đi đáng kể mà.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2254 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道はただでさえ人手不足です。優秀な\x%l運転士;#00ffc040;運転士%l;#;と\n最新鋭の\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の参加を拒むなど、ありませんよ」
- TW: 「御一夜鐵路本來就很缺人手。像你們這麼優秀的\x%l運転士;#00ffc040;駕駛員%l;#;和\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，於我們而言自然是求之不得，又豈有拒絕的理由」
- old_vn (csv3): 「Đường sắt Ohito vốn đã thiếu nhân lực rồi. Chúng cháu không có lý do gì\nđể từ chối sự gia nhập của một \x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; xuất sắc và một \x%lレイルロオド;#00ffc040;Railord%l;#; tối tân đâu ạ.」
- fix: 「Đường sắt Ohitoyo vốn đã thiếu nhân lực rồi. Chúng cháu không có lý do gì\nđể từ chối sự gia nhập của một \x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; xuất sắc và một \x%lレイルロオド;#00ffc040;Railord%l;#; tối tân đâu ạ.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2154 — item T1 (JP: 御一夜)

- JP: 「上記ふたつにともなって発生する、市民一般の雇用。\nこれは明快にすぎる、"御一夜市民"へのメリットだ」
- TW: 「在這兩件事的實施中，也會僱傭普通市民。這就是對御一夜市民顯而易見的好處」
- old_vn (csv3): 「Đi kèm với hai điều trên là việc làm cho người dân.\nĐây là một lợi ích quá rõ ràng đối với "người dân Ohito".」
- fix: 「Đi kèm với hai điều trên là việc làm cho người dân.\nĐây là một lợi ích quá rõ ràng đối với "người dân Ohitoyo".」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2121 — item T1 (JP: 御一夜)

- JP: 「ああ。約束通りに支援しよう。『未来行き列車計画』を、\nエアクラ工場誘致に代わる、御一夜復興案として」
- TW: 「嗯，按照約定，我會幫助你們。讓“發往未來列車計劃”替代空凝機工廠的引進，成為新的御一夜復興計劃」
- old_vn (csv3): 「Ừ. Ta sẽ hỗ trợ như đã hứa. Đưa 『Kế hoạch Tàu Hướng Tới Tương Lai』,\ntrở thành phương án phục hưng Ohito thay thế cho việc mời gọi nhà máy Aircra.」
- fix: 「Ừ. Ta sẽ hỗ trợ như đã hứa. Đưa 『Kế hoạch Tàu Hướng Tới Tương Lai』,\ntrở thành phương án phục hưng Ohitoyo thay thế cho việc mời gọi nhà máy Aircra.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1326 — item T1 (JP: 御一夜)

- JP: ……オール御一夜体制が、ここに、ようやく成立した。
- TW: ……全御一夜體制在此刻終於成型了。
- old_vn (csv3): ……Thể chế Toàn Ohito, cuối cùng cũng đã được thành lập tại đây.
- fix: ……Thể chế Toàn Ohitoyo, cuối cùng cũng đã được thành lập tại đây.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 3124 — item T1 (JP: 御一夜)

- JP: 御一夜を、そして鉄道を、\nならばここから、きっと復興させていけよう。
- TW: 御一夜和鐵路，今後也一定會走向復興。
- old_vn (csv3): Vậy thì từ đây, chắc chắn chúng ta sẽ có thể phục hưng Ohito,\nvà cả ngành đường sắt nữa.
- fix: Vậy thì từ đây, chắc chắn chúng ta sẽ có thể phục hưng Ohitoyo,\nvà cả ngành đường sắt nữa.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

## 06_Kisaki — `稀咲01_金と人.txt.toml` (15 dòng)

### key 1800 — item T1 (JP: 御一夜)

- JP: 「見ているもの、見えているものが違うようだが、\n御一夜の発展を願う気持ちは同じだと感じたからな」
- TW: 「我覺得雖然我們的著眼點和看問題的角度各不相同，但希望御一夜發展壯大的心願是相通的」
- old_vn (csv3): 「Dù góc nhìn và những gì chúng ta thấy có vẻ khác nhau,\nnhưng anh cảm nhận được mong muốn phát triển Ohito của chúng ta là như nhau.」
- fix: 「Dù góc nhìn và những gì chúng ta thấy có vẻ khác nhau,\nnhưng anh cảm nhận được mong muốn phát triển Ohitoyo của chúng ta là như nhau.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1688 — item T1 (JP: 御一夜)

- JP: 「御一夜は焼酎の町であり、温泉の町だ。\n水の変化から受ける影響は、それだけ大きいものになる」
- TW: 「因為御一夜是燒酒之鄉，也是溫泉之鄉。水資源變化帶來的影響會比一般城市嚴重得多」
- old_vn (csv3): 「Ohito là thị trấn của shochu, và cũng là thị trấn của suối nước nóng.\nẢnh hưởng từ sự thay đổi của nguồn nước sẽ lớn đến mức đó đấy.」
- fix: 「Ohitoyo là thị trấn của shochu, và cũng là thị trấn của suối nước nóng.\nẢnh hưởng từ sự thay đổi của nguồn nước sẽ lớn đến mức đó đấy.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2351 — item T1 (JP: 御一夜)

- JP: 御一夜を大切にしていることなら、確かに感じた。
- TW: 我確實能感覺到，她也很珍惜御一夜。
- old_vn (csv3): Việc em ấy trân trọng Ohito, tôi thực sự đã cảm nhận được.
- fix: Việc em ấy trân trọng Ohitoyo, tôi thực sự đã cảm nhận được.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2198 — item T1 (JP: 御一夜)

- JP: だが、御一夜の何を大切と感じているか、\nそこに、恐らくは食い違いがある。
- TW: 但是，要說具體珍惜御一夜的什麼，這個問題的答案恐怕有所不同。
- old_vn (csv3): Nhưng, em ấy trân trọng điều gì ở Ohito,\ncó lẽ chúng tôi đang có sự khác biệt ở điểm đó.
- fix: Nhưng, em ấy trân trọng điều gì ở Ohitoyo,\ncó lẽ chúng tôi đang có sự khác biệt ở điểm đó.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1991 — item T1 (JP: 御一夜)

- JP: 「となると……御一夜はクマ焼酎というブランドを失う。\nその[いっしつ,1]逸失利益は――確かに無視できるものとも思えない」
- TW: 「這樣一來……御一夜就少了隈燒酒這樣一個品牌。我們確實不能眼睜睜看著這樣一塊利益消失掉」
- old_vn (audit): 「Nếu vậy……Ohito sẽ đánh mất thương hiệu shochu Kuma.\nKhoản lợi nhuận bị mất đó――đúng là không thể phớt lờ được.」
- fix: 「Nếu vậy……Ohitoyo sẽ đánh mất thương hiệu shochu Kuma.\nKhoản lợi nhuận bị mất đó――đúng là không thể phớt lờ được.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1704 — item T1 (JP: 御一夜)

- JP: 「メリットならある。御一夜市が衰退してしまうのなら、\nクマ焼酎もクマ川下りも鉄道も衰退していく」
- TW: 「好處當然有。如果御一夜繼續衰退下去，隈燒酒、隈河漂流和鐵路也會跟著走下坡路」
- old_vn (audit): 「Lợi ích thì có đấy. Nếu thành phố Ohito suy tàn,\nthì shochu Kuma, chèo thuyền trên sông Kuma hay đường sắt cũng sẽ lụi bại theo.」
- fix: 「Lợi ích thì có đấy. Nếu thành phố Ohitoyo suy tàn,\nthì shochu Kuma, chèo thuyền trên sông Kuma hay đường sắt cũng sẽ lụi bại theo.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2046 — item T1 (JP: 御一夜)

- JP: 「御一夜市の衰退を防ぐことと、工場誘致とは直結しない。\n僕らは他のやり方で御一夜を再興できると考えています」
- TW: 「阻止御一夜的衰退和工廠落戶並沒有直接聯繫。我們正在考慮其他重振御一夜的方法」
- old_vn (audit): 「Việc ngăn chặn sự suy tàn của thành phố Ohito không liên quan trực tiếp đến việc mời gọi nhà máy.\nChúng cháu tin rằng có những cách khác để phục hưng Ohito.」
- fix: 「Việc ngăn chặn sự suy tàn của thành phố Ohitoyo không liên quan trực tiếp đến việc mời gọi nhà máy.\nChúng cháu tin rằng có những cách khác để phục hưng Ohitoyo.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1785 — item T1 (JP: 御一夜)

- JP: 「御一夜市が二分されるのは好ましくありません。\nできるかぎり多くからの同意を得られるように――」
- TW: 「我不希望將御一夜一分為二。這時候應該儘可能得到多數人的同意——」
- old_vn (audit): 「Việc thành phố Ohito bị chia rẽ là điều không nên.\nChúng ta cần cố gắng đạt được sự đồng thuận từ càng nhiều người càng tốt――」
- fix: 「Việc thành phố Ohitoyo bị chia rẽ là điều không nên.\nChúng ta cần cố gắng đạt được sự đồng thuận từ càng nhiều người càng tốt――」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2291 — item T1 (JP: 御一夜)

- JP: そうして研磨される強さもあろうが、\n今の御一夜に求めるべきが、それであるとは思えない。
- TW: 如此磨礪而來的強大當然也有其價值，但我覺得，現在的御一夜需要的並不是它。
- old_vn (audit): Có thể sự mạnh mẽ được rèn giũa qua đó cũng tốt,\nnhưng tôi không nghĩ đó là điều Ohito cần lúc này.
- fix: Có thể sự mạnh mẽ được rèn giũa qua đó cũng tốt,\nnhưng tôi không nghĩ đó là điều Ohitoyo cần lúc này.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1775 — item T1 (JP: 御一夜)

- JP: 「あなたの目標とて、\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致自体ではない筈だ。\n誘致はあくまで、御一夜再生、経済振興の手段ですよね」
- TW: 「您的目的應該並不是\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶這件事本身。工廠落戶，只不過是讓御一夜重獲新生、振興經濟的手段吧」
- old_vn (audit): 「Mục tiêu của bác chắc chắn không phải là việc mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;.\nViệc mời gọi nhà máy chỉ là phương tiện để phục hưng Ohito và chấn hưng kinh tế thôi, đúng không ạ.」
- fix: 「Mục tiêu của bác chắc chắn không phải là việc mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;.\nViệc mời gọi nhà máy chỉ là phương tiện để phục hưng Ohitoyo và chấn hưng kinh tế thôi, đúng không ạ.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1620 — item T1 (JP: 御一夜)

- JP: 「ははぁ、つまりはこう言いたいわけか。\n『工場誘致より優れた御一夜再生計画がある』と」
- TW: 「哈哈，你是想說“你有比讓工廠落戶更優秀的御一夜振興方案”嗎」
- old_vn (audit): 「Haha, vậy là cháu muốn nói điều này sao.\n『Cháu có một kế hoạch phục hưng Ohito xuất sắc hơn việc mời gọi nhà máy』.」
- fix: 「Haha, vậy là cháu muốn nói điều này sao.\n『Cháu có một kế hoạch phục hưng Ohitoyo xuất sắc hơn việc mời gọi nhà máy』.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1749 — item T1 (JP: 御一夜)

- JP: 「さっきの例えを借りるなら、『旨くはないが安い酒』。\n御一夜市民の大多数は、工場誘致をそう捉えている」
- TW: 「就用剛才的例子來說吧，大多數御一夜市民都把工廠落戶方案當作是“不好喝但便宜的酒”」
- old_vn (audit): 「Mượn ví dụ lúc nãy của bác, thì đó là 『loại rượu không ngon nhưng rẻ』.\nĐại đa số người dân Ohito đều coi việc mời gọi nhà máy là như vậy.」
- fix: 「Mượn ví dụ lúc nãy của bác, thì đó là 『loại rượu không ngon nhưng rẻ』.\nĐại đa số người dân Ohitoyo đều coi việc mời gọi nhà máy là như vậy.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1549 — item T1 (JP: 御一夜)

- JP: 「しかしだ、御一夜は困窮している。\n安酒であれ、それがなければ渇ききるほどに」
- TW: 「但現在御一夜已經陷入窘境。哪怕是便宜酒，也比渴死要好」
- old_vn (audit): 「Nhưng mà, Ohito đang khốn khó.\nDù là rượu rẻ tiền, nếu không có nó thì sẽ chết khát mất.」
- fix: 「Nhưng mà, Ohitoyo đang khốn khó.\nDù là rượu rẻ tiền, nếu không có nó thì sẽ chết khát mất.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1551 — item T1 (JP: 御一夜)

- JP: 「それなら全てが、過去の遺物だ。\n御一夜の再生には繋がらんよ」
- TW: 「但這些東西都只是過去的遺產。和御一夜的復興並沒有聯繫」
- old_vn (audit): 「Nếu vậy thì tất cả đều là di vật của quá khứ.\nKhông thể dẫn đến sự phục hưng của Ohito được đâu.」
- fix: 「Nếu vậy thì tất cả đều là di vật của quá khứ.\nKhông thể dẫn đến sự phục hưng của Ohitoyo được đâu.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1705 — item T1 (JP: 御一夜)

- JP: 「ならば御一夜支店長。誘致は私の方で進める。\n君は外れて、別案の方に注力してくれたまえ」
- TW: 「好，御一夜支行行長，工廠落戶方案由我來推進。你就從這項方案中抽身，去全力推進別的方案」
- old_vn (audit): 「Vậy thì, Giám đốc chi nhánh Ohito. Việc mời gọi nhà máy cứ để ta lo.\nCon hãy rút lui khỏi chuyện đó, và tập trung vào phương án khác đi.」
- fix: 「Vậy thì, Giám đốc chi nhánh Ohitoyo. Việc mời gọi nhà máy cứ để ta lo.\nCon hãy rút lui khỏi chuyện đó, và tập trung vào phương án khác đi.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

## 06_Kisaki — `稀咲03_純白のレール.txt.toml` (7 dòng)

### key 1624 — item T2 (JP: 御一夜鉄道)

- JP: 「最初期は、御一夜鉄道さんからだけだ。が、ほどなく\n[ひさつ,1]肥颯みかん鉄道さんからもご応募いただいた」
- TW: 「一開始只有御一夜鐵路公司。但之後肥薩橙鐵路公司也馬上就參加了」
- old_vn (csv3): 「Giai đoạn đầu thì chỉ có từ Đường sắt Ohito thôi. Nhưng chẳng bao lâu sau,\nĐường sắt Hisatsu Mikan cũng đã đăng ký tham gia.」
- fix: 「Giai đoạn đầu thì chỉ có từ Đường sắt Ohitoyo thôi. Nhưng chẳng bao lâu sau,\nĐường sắt Hisatsu Mikan cũng đã đăng ký tham gia.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2565 — item T2 (JP: 御一夜鉄道)

- JP: ので、そこについては、御一夜鉄道株式会社に\n業務委託でお願いできればと相談をしていたのだが――
- TW: 所以我們找上了御一夜鐵路股份公司，希望能把業務委託給他們——
- old_vn (csv3): Do đó, về vấn đề này, chúng tôi đã thảo luận với Công ty Cổ phần Đường sắt Ohito\nđể nhờ họ nhận thầu công việc——
- fix: Do đó, về vấn đề này, chúng tôi đã thảo luận với Công ty Cổ phần Đường sắt Ohitoyo\nđể nhờ họ nhận thầu công việc——
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1957 — item T2 (JP: 御一夜鉄道)

- JP: 「そこでなのですけれども――御一夜鉄道の線路を全部、\nそのお金で買収していただくのはいかがですか？」
- TW: 「所以我在想——能不能把御一夜鐵路的所有線路都用那些資金買下來呢？」
- old_vn (csv3): 「Về chuyện đó thì——ngài nghĩ sao nếu dùng số tiền đó\nđể mua lại toàn bộ đường ray của Đường sắt Ohito ạ?」
- fix: 「Về chuyện đó thì——ngài nghĩ sao nếu dùng số tiền đó\nđể mua lại toàn bộ đường ray của Đường sắt Ohitoyo ạ?」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1906 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道の……御一夜-[ゆのい,1]湯医間をか？」
- TW: 「御一夜鐵路的……是說御一夜到湯醫嗎？」
- old_vn (audit): 「Của Đường sắt Ohito…… đoạn Ohitoyo - Yunoi sao?」
- fix: 「Của Đường sắt Ohitoyo…… đoạn Ohitoyo - Yunoi sao?」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước). Lần xuất hiện trần thứ hai trong dòng đã là "Ohitoyo" đúng sẵn (audit sửa trước) — chỉ đổi phần "Đường sắt Ohito".

### key 1963 — item T2 (JP: 御一夜鉄道)

- JP: 「ですので。『御一夜鉄道の所有する全線路』を、\n双鉄様の会社にご買収いただくのです」
- TW: 「所以，我希望雙鐵少爺的公司能收購御一夜鐵路的所有線路」
- old_vn (csv3): 「Chính vì thế. Công ty của ngài Soutetsu sẽ mua lại\n『toàn bộ đường ray thuộc sở hữu của Đường sắt Ohito』 ạ.」
- fix: 「Chính vì thế. Công ty của ngài Soutetsu sẽ mua lại\n『toàn bộ đường ray thuộc sở hữu của Đường sắt Ohitoyo』 ạ.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2894 — item T2 (JP: 御一夜鉄道)

- JP: そうなれば以降の御一夜鉄道は、\n\x%l保線;#00ffc040;保線%l;#;にかかる人員設備を、所有しなくて済むのだから――
- TW: 這樣，御一夜鐵路就不需要再負擔\x%l保線;#00ffc040;巡線%l;#;的人員和設備了。
- old_vn (csv3): Nếu vậy thì từ nay trở đi, Đường sắt Ohito\nsẽ không cần phải sở hữu nhân sự và thiết bị phục vụ cho việc \x%l保線;#00ffc040;bảo trì đường ray%l;#; nữa——
- fix: Nếu vậy thì từ nay trở đi, Đường sắt Ohitoyo\nsẽ không cần phải sở hữu nhân sự và thiết bị phục vụ cho việc \x%l保線;#00ffc040;bảo trì đường ray%l;#; nữa——
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1882 — item T2 (JP: 御一夜鉄道)

- JP: 「『第一期追加募集;\n（株）御一夜鉄道稼働中路線・御一夜-湯医間』ですか」
- TW: 「就叫“第一期追加集資：御一夜鐵路股份公司運營中的路線·御一夜至湯醫路段”嗎」
- old_vn (audit): 「『Đợt huy động bổ sung kỳ 1;\nTuyến đường đang hoạt động của Công ty CP Đường sắt Ohito・Đoạn Ohitoyo - Yunoi』 sao ạ.」
- fix: 「『Đợt huy động bổ sung kỳ 1;\nTuyến đường đang hoạt động của Công ty CP Đường sắt Ohitoyo・Đoạn Ohitoyo - Yunoi』 sao ạ.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước). Lần xuất hiện trần thứ hai trong dòng đã là "Ohitoyo" đúng sẵn (audit sửa trước) — chỉ đổi phần "Đường sắt Ohito".

## 07_Nagi_Fukami — `凪h2_おとなの水着.txt.toml` (2 dòng)

### key 1766 — item T2 (JP: 御一夜鉄道)

- JP: ……8620が完全復活し、僕も御一夜鉄道と、\n一般的なまいてつ契約を締結するようになった。
- TW: ……８６２０已經徹底恢復，我與御一夜鐵路也簽訂了正常的掌車人契約。
- old_vn (csv3): ……8620 đã hoàn toàn hồi sinh, và tôi cũng đã ký kết hợp đồng Maitetsu thông thường\nvới Đường sắt Ohito.
- fix: ……8620 đã hoàn toàn hồi sinh, và tôi cũng đã ký kết hợp đồng Maitetsu thông thường\nvới Đường sắt Ohitoyo.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3568 — item T2 (JP: 御一夜鉄道)

- JP: 御一夜鉄道オリジナル缶バッジ。ひとつ四百円。\n地味ではあるが、これも大切な収入源だ。
- TW: 御一夜鐵路原創徽章，一枚四百日元。儘管很老套，但這也是我們寶貴的收入來源。
- old_vn (csv3): Huy hiệu nguyên bản của Đường sắt Ohito. Một cái bốn trăm yên.\nTuy giản dị, nhưng đây cũng là một nguồn thu nhập quan trọng.
- fix: Huy hiệu nguyên bản của Đường sắt Ohitoyo. Một cái bốn trăm yên.\nTuy giản dị, nhưng đây cũng là một nguồn thu nhập quan trọng.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 07_Nagi_Fukami — `凪ふかみ03_三人いっしょ.txt.toml` (6 dòng)

### key 2183 — item T1 (JP: 御一夜)

- JP: せっつかれるまま、“御一夜スペシャル修学旅行！”と\n表紙書きされたしおりを開く。
- TW: 在凪的催促聲中，深美把手裡的手冊在桌上攤開，手冊寫著《御一夜特別修學旅行！》的封皮映入眼簾。
- old_vn (csv3): Bị hối thúc, tôi mở cuốn sổ tay có dòng chữ\n“Chuyến đi dã ngoại đặc biệt ở Ohito!” trên trang bìa.
- fix: Bị hối thúc, tôi mở cuốn sổ tay có dòng chữ\n“Chuyến đi dã ngoại đặc biệt ở Ohitoyo!” trên trang bìa.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1620 — item T1 (JP: 御一夜)

- JP: 「御一夜のことを改めて、双鉄さんとわたし達とで、\n勉強できる旅行にしたいなって」
- TW: 「我們希望雙鐵先生能和我們一起，來進行一次重新學習御一夜的旅行」
- old_vn (csv3): 「Tụi em muốn cùng anh Soutetsu có một chuyến đi\nđể tìm hiểu lại về Ohito ạ」
- fix: 「Tụi em muốn cùng anh Soutetsu có một chuyến đi\nđể tìm hiểu lại về Ohitoyo ạ」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1411 — item T1 (JP: 御一夜)

- JP: 「なるほど。御一夜を学ぶ、“修学”旅行か」
- TW: 「原來如此。學習御一夜的“修學”旅行啊」
- old_vn (csv3): 「Ra là vậy. Chuyến đi "dã ngoại" để tìm hiểu về Ohito sao」
- fix: 「Ra là vậy. Chuyến đi "dã ngoại" để tìm hiểu về Ohitoyo sao」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2489 — item T1 (JP: 御一夜)

- JP: 御一夜について学ぶのは、\n工場誘致を撤回させるためにも必ず役に立つ。
- TW: 認真學習御一夜，想必會對阻止工廠落戶的活動有所裨益吧。
- old_vn (csv3): Việc tìm hiểu về Ohito,\nchắc chắn sẽ có ích cho việc rút lại lời mời gọi xây dựng nhà máy.
- fix: Việc tìm hiểu về Ohitoyo,\nchắc chắn sẽ có ích cho việc rút lại lời mời gọi xây dựng nhà máy.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1580 — item T1 (JP: 御一夜)

- JP: 「御一夜一の腕利き鍛冶屋！\n蓑笠鍛冶店さんからばいっ！！」
- TW: 「就從御一夜技術首屈一指的鍛冶店——蓑笠鍛冶店開始唄！！」
- old_vn (csv3): 「Lò rèn cừ khôi nhất Ohito!\nBắt đầu từ lò rèn Minokasa!!」
- fix: 「Lò rèn cừ khôi nhất Ohitoyo!\nBắt đầu từ lò rèn Minokasa!!」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1646 — item T1 (JP: 御一夜)

- JP: 「だから一緒に学んでいきたい。御一夜のこと、\nこれからのこと、お互いのことを、出来るだけ」
- TW: 「所以我想和你們一起學習。學習御一夜，探索將來，了解彼此，越多越好」
- old_vn (csv3): 「Vì vậy anh muốn cùng nhau học hỏi. Về Ohito,\nvề tương lai, về lẫn nhau, nhiều nhất có thể」
- fix: 「Vì vậy anh muốn cùng nhau học hỏi. Về Ohitoyo,\nvề tương lai, về lẫn nhau, nhiều nhất có thể」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

## 07_Nagi_Fukami — `凪ふかみ05_凪の開眼！？.txt.toml` (1 dòng)

### key 2483 — item T2 (JP: 御一夜鉄道)

- JP: 「左様です。さすが凪さま。御一夜鉄道の次の機関士。\nお可愛く、お強いだけでなく、お賢くもあらせれますね」
- TW: 「沒錯。不愧是凪小姐，御一夜鐵道的下一位司機。既可愛，又厲害，而且還這麼聰敏機靈」
- old_vn (csv3): 「Đúng vậy. Không hổ danh là Nagi. Người lái tàu tiếp theo của Đường sắt Ohito.\nKhông chỉ dễ thương, mạnh mẽ mà còn vô cùng thông minh xuất chúng nữa.」
- fix: 「Đúng vậy. Không hổ danh là Nagi. Người lái tàu tiếp theo của Đường sắt Ohitoyo.\nKhông chỉ dễ thương, mạnh mẽ mà còn vô cùng thông minh xuất chúng nữa.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 07_Nagi_Fukami — `凪ふかみ08a_凪エピローグ_一番ほしい、一番.txt.toml` (3 dòng)

### key 1888 — item T2 (JP: 御一夜鉄道)

- JP: 「[うち,4]御一夜鉄道の早瀬は、長年大会を見てますからね。\nデータ分析を、非常にしっかりやってくれてます」
- TW: 「歷年的大賽，咱們御一夜鐵路的早瀨都親眼見過，她把數據資料整理分析得非常好」
- old_vn (csv3): 「Hayase của Đường sắt Ohito đã theo dõi giải đấu này nhiều năm rồi.\nCô ấy phân tích dữ liệu rất kỹ lưỡng.」
- fix: 「Hayase của Đường sắt Ohitoyo đã theo dõi giải đấu này nhiều năm rồi.\nCô ấy phân tích dữ liệu rất kỹ lưỡng.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2840 — item T2 (JP: 御一夜鉄道)

- JP: 御一夜鉄道の僕と凪との他のメンバーは、\n宗方さん率いる、みかん鉄道剣道部のおふたりだ。
- TW: 隊伍成員有來自御一夜鐵路的我和凪，還有橙鐵路劍道社的宗方先生，以及他帶來的兩個人。
- old_vn (csv3): Ngoài tôi và Nagi của Đường sắt Ohito,\ncác thành viên khác là hai người thuộc câu lạc bộ kiếm đạo Đường sắt Mikan do anh Munakata dẫn dắt.
- fix: Ngoài tôi và Nagi của Đường sắt Ohitoyo,\ncác thành viên khác là hai người thuộc câu lạc bộ kiếm đạo Đường sắt Mikan do anh Munakata dẫn dắt.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2695 — item T2 (JP: 御一夜鉄道)

- JP: 御一夜鉄道がみかん鉄道から譲渡を受けた、\nレイルロオドを失くしてしまった、Ⅸ号機関車。
- TW: 橙鐵路將失去了鐵路人偶的九號機車贈予給御一夜鐵路。
- old_vn (csv3): Đường sắt Ohito đã nhận chuyển nhượng từ Đường sắt Mikan,\nđầu máy số IX, chiếc đầu máy đã mất đi Railord của mình.
- fix: Đường sắt Ohitoyo đã nhận chuyển nhượng từ Đường sắt Mikan,\nđầu máy số IX, chiếc đầu máy đã mất đi Railord của mình.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 07_Nagi_Fukami — `凪ふかみ08c_新しい家族.txt.toml` (7 dòng)

### key 2585 — item T1 (JP: 御一夜)

- JP: 「バーベキュートレインとクマ川下りとの連携。\nそいを、御一夜全体の観光・産業への刺激にもつなげた」
- TW: 「ＢＢＱ列車和隈河漂流之間的合作，刺激了整個御一夜的觀光與生產」
- old_vn (csv3): 「Sự liên kết giữa chuyến tàu BBQ và xuôi dòng sông Kuma.\nViệc đó cũng đã tạo cú hích cho toàn bộ ngành du lịch và công nghiệp của Ohito.」
- fix: 「Sự liên kết giữa chuyến tàu BBQ và xuôi dòng sông Kuma.\nViệc đó cũng đã tạo cú hích cho toàn bộ ngành du lịch và công nghiệp của Ohitoyo.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2199 — item T1+T2 (JP: 御一夜鉄道 + 御一夜)

- JP: 「御一夜鉄道の収入だけでなく、御一夜市の税収も\n前年比で二十パーセント以上の増加をみせました」
- TW: 「御一夜鐵路的收入提升了，御一夜市的稅收也比前一年增加了２０％以上」
- old_vn (csv3): 「Không chỉ doanh thu của Đường sắt Ohito, mà thu nhập thuế của thành phố Ohito\ncũng cho thấy sự gia tăng hơn hai mươi phần trăm so với năm ngoái.」
- fix: 「Không chỉ doanh thu của Đường sắt Ohitoyo, mà thu nhập thuế của thành phố Ohitoyo\ncũng cho thấy sự gia tăng hơn hai mươi phần trăm so với năm ngoái.」
- Lý do: JP chứa cả 御一夜鉄道 và 御一夜; VN cũ dùng dạng cũ "Ohito" ở cả hai dạng → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2196 — item T1 (JP: 御一夜)

- JP: 「御一夜にもあるんですよ。そういうご相談、最近は」
- TW: 「御一夜也有。最近有人找我們諮詢這方面的問題」
- old_vn (csv3): 「Ở Ohito cũng có đấy ạ. Những lời nhờ tư vấn như vậy, dạo gần đây.」
- fix: 「Ở Ohitoyo cũng có đấy ạ. Những lời nhờ tư vấn như vậy, dạo gần đây.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2041 — item T1 (JP: 御一夜)

- JP: 「あー、なるほど！　じゃあ、『新しい生き方特区』とか\n『新しい家族の形特区』みたいなのを、御一夜に？」
- TW: 「啊，原來是這樣！那就是要在御一夜建立“新生活特區”或者“新家庭特區”？」
- old_vn (csv3): 「A, ra là vậy! Vậy thì, kiểu như 'Đặc khu Lối sống mới' hay\n'Đặc khu Hình thái Gia đình mới' ở Ohito sao?」
- fix: 「A, ra là vậy! Vậy thì, kiểu như 'Đặc khu Lối sống mới' hay\n'Đặc khu Hình thái Gia đình mới' ở Ohitoyo sao?」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2420 — item T1 (JP: 御一夜)

- JP: 「なるほど、これは――\n『鉄道の町・御一夜』構想にも深く関わる案件だね？」
- TW: 「看來，這跟“鐵路之城御一夜”構想也有很大的關係吧？」
- old_vn (csv3): 「Ra là vậy, chuyện này――\nCũng là một dự án liên quan mật thiết đến ý tưởng 'Thành phố Đường sắt Ohito' nhỉ?」
- fix: 「Ra là vậy, chuyện này――\nCũng là một dự án liên quan mật thiết đến ý tưởng 'Thành phố Đường sắt Ohitoyo' nhỉ?」
- Lý do: JP chứa 鉄道の町・御一夜 (dạng trần — xem §2 quyết định D1); VN cũ "Thành phố Đường sắt Ohito" → "Thành phố Đường sắt Ohitoyo" theo T1.

### key 2341 — item T1 (JP: 御一夜)

- JP: 「そうね、稀咲。鉄道の町・御一夜は、人と人が、\n人とレイルロオドとが、新しい形の家族になれる町」
- TW: 「是的，稀咲。鐵路之城御一夜，是一座人與人之間、人與鐵路人偶之間能夠組建新型家庭的城市」
- old_vn (csv3): 「Đúng vậy, Kisaki. Thành phố Đường sắt Ohito là nơi mà con người với con người,\ncon người với \x%lレイルロオド;#00ffc040;Railord%l;#;, có thể trở thành một gia đình kiểu mới.」
- fix: 「Đúng vậy, Kisaki. Thành phố Đường sắt Ohitoyo là nơi mà con người với con người,\ncon người với \x%lレイルロオド;#00ffc040;Railord%l;#;, có thể trở thành một gia đình kiểu mới.」
- Lý do: JP chứa 鉄道の町・御一夜 (dạng trần — xem §2 quyết định D1); VN cũ "Thành phố Đường sắt Ohito" → "Thành phố Đường sắt Ohitoyo" theo T1.

### key 2248 — item T1 (JP: 御一夜)

- JP: 「必ず、御一夜を――\n『新しい家族の形特区』に」
- TW: 「我們一定要讓御一夜成為“新家庭特區”」
- old_vn (csv3): 「Nhất định, sẽ biến Ohito――\nthành 'Đặc khu Hình thái Gia đình mới'.」
- fix: 「Nhất định, sẽ biến Ohitoyo――\nthành 'Đặc khu Hình thái Gia đình mới'.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

## 09_Grand — `グランドリライト01_オール御一夜、成立ならず.txt.toml` (1 dòng)

### key 1550 — item T2 (JP: 御一夜鉄道)

- JP: 「『御一夜鉄道未来行き列車を、必ずこの手で。\n僕らの重ねたこの手できっと！　走らせよう！』」
- TW: 「“讓我們靠我們的力量來讓御一夜鐵路發往未來列車飛馳起來！”」
- old_vn (csv3): 「'Chuyến tàu hướng tới tương lai của Đường sắt Ohito, nhất định bằng đôi tay này.\nBằng những đôi tay đang đan vào nhau này, chắc chắn! Sẽ lăn bánh!'」
- fix: 「'Chuyến tàu hướng tới tương lai của Đường sắt Ohitoyo, nhất định bằng đôi tay này.\nBằng những đôi tay đang đan vào nhau này, chắc chắn! Sẽ lăn bánh!'」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 09_Grand — `グランドリライト02_ナビ.txt.toml` (8 dòng)

### key 1684 — item T1 (JP: 御一夜)

- JP: 「御一夜で、[うち]家でやりたいことが山のようにある。\nできるだけ早く、無論、元気に帰ってくるさ」
- TW: 「我還有一大堆事情想在御一夜、在家裡做呢。所以我會儘量早點回來，當然會好好的啦」
- old_vn (csv3): 「Ở Ohito, ở nhà còn chất đống chuyện anh muốn làm.\nAnh sẽ cố gắng về sớm nhất có thể, tất nhiên là sẽ khỏe mạnh trở về rồi.」
- fix: 「Ở Ohitoyo, ở nhà còn chất đống chuyện anh muốn làm.\nAnh sẽ cố gắng về sớm nhất có thể, tất nhiên là sẽ khỏe mạnh trở về rồi.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2575 — item T1+T2 (JP: 御一夜鉄道 + 御一夜)

- JP: 御一夜に帰ってきて初めての休暇の申し出を\n右田家も、御一夜鉄道も、即座に快諾してくれた。
- TW: 這還是我回到御一夜之後第一次提出休假申請，右田家和御一夜鐵路都乾脆地應允了。
- old_vn (csv3): Lời đề nghị xin nghỉ phép đầu tiên kể từ khi trở về Ohito\nđã được nhà Migita và Đường sắt Ohito nhanh chóng chấp thuận.
- fix: Lời đề nghị xin nghỉ phép đầu tiên kể từ khi trở về Ohitoyo\nđã được nhà Migita và Đường sắt Ohitoyo nhanh chóng chấp thuận.
- Lý do: JP chứa cả 御一夜鉄道 và 御一夜; VN cũ dùng dạng cũ "Ohito" ở cả hai dạng → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2213 — item T1 (JP: 御一夜)

- JP: 御一夜を離れてからの六年半。\nその一時間を、僕は、どうしても使えなかった。
- TW: 在離開御一夜的六年半中，我無論如何都沒能鼓起勇氣花上這一小時回來。
- old_vn (csv3): Sáu năm rưỡi kể từ khi rời khỏi Ohito.\nTôi đã không thể nào dành ra được một giờ đồng hồ đó.
- fix: Sáu năm rưỡi kể từ khi rời khỏi Ohitoyo.\nTôi đã không thể nào dành ra được một giờ đồng hồ đó.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2319 — item T1+T2 (JP: 御一夜鉄道 + 御一夜)

- JP: 御一夜のこと。\n御一夜鉄道のこと。
- TW: 我想著有關御一夜的事。有關御一夜鐵路的事。
- old_vn (csv3): Về Ohito.\nVề Đường sắt Ohito.
- fix: Về Ohitoyo.\nVề Đường sắt Ohitoyo.
- Lý do: JP chứa cả 御一夜鉄道 và 御一夜; VN cũ dùng dạng cũ "Ohito" ở cả hai dạng → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1901 — item T2 (JP: 御一夜鉄道)

- JP: 「その成長を著しく促したのは、双鉄様の身の回りの、\n右田家や、御一夜鉄道に纏わる人々だと観測します」
- TW: 「Ｎａｖｉ觀測到，雙鐵少爺身邊的人，包括右田家和御一夜鐵路相關的人們，顯著地促進了您的成長」
- old_vn (csv3): 「Navi quan trắc thấy rằng, những người xung quanh ngài Soutetsu,\nnhững người liên quan đến nhà Migita và Đường sắt Ohito, đã thúc đẩy sự trưởng thành đó một cách đáng kể.」
- fix: 「Navi quan trắc thấy rằng, những người xung quanh ngài Soutetsu,\nnhững người liên quan đến nhà Migita và Đường sắt Ohitoyo, đã thúc đẩy sự trưởng thành đó một cách đáng kể.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1017 — item T1 (JP: 御一夜)

- JP: ――ナビが再び、まっすぐに飛ぶ。\n御一夜目指して、まっすぐに。
- TW: ——Ｎａｖｉ又開始直線飛行。徑直朝著御一夜飛去。
- old_vn (csv3): ――Navi lại tiếp tục bay thẳng.\nHướng thẳng về phía Ohito.
- fix: ――Navi lại tiếp tục bay thẳng.\nHướng thẳng về phía Ohitoyo.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2355 — item T1 (JP: 御一夜)

- JP: 元忠氏に出された課題の解決があり、\nオール御一夜体制を築けるような、そんな気もする。
- TW: 或許就能解決元忠先生提出的問題，建立起全御一夜體制。
- old_vn (csv3): Tôi có cảm giác rằng mình sẽ giải quyết được bài toán mà ông Mototada đặt ra,\nvà có thể xây dựng nên một thể chế toàn Ohito.
- fix: Tôi có cảm giác rằng mình sẽ giải quyết được bài toán mà ông Mototada đặt ra,\nvà có thể xây dựng nên một thể chế toàn Ohitoyo.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1713 — item T1 (JP: 御一夜)

- JP: 「日々姫、僕は――\n御一夜を、もっと知りたいと思うんだ」
- TW: 「日日姬，我——想要更加了解御一夜」
- old_vn (csv3): 「Hibiki này, anh――\nmuốn hiểu thêm về Ohito.」
- fix: 「Hibiki này, anh――\nmuốn hiểu thêm về Ohitoyo.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

## 09_Grand — `グランドリライト08_ふかみ.txt.toml` (5 dòng)

### key 2604 — item T2 (JP: 御一夜鉄道)

- JP: クマ川下りも極めて厳しかったようだが、\n御一夜鉄道も、大変に苦労させられた。
- TW: 在這期間，隈河漂流和御一夜鐵路的經營情況都極為嚴峻。
- old_vn (csv3): Có vẻ như dịch vụ xuôi dòng sông Kuma cũng gặp vô vàn khó khăn,\nvà Đường sắt Ohito cũng đã phải chật vật rất nhiều.
- fix: Có vẻ như dịch vụ xuôi dòng sông Kuma cũng gặp vô vàn khó khăn,\nvà Đường sắt Ohitoyo cũng đã phải chật vật rất nhiều.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2519 — item T1 (JP: 御一夜)

- JP: が、月一でふかみが御一夜に戻ってくると、\nそれが綺麗に解消するのだ。
- TW: 但是每個月深美回到御一夜的時候，一切問題就都迎刃而解了。
- old_vn (csv3): Thế nhưng, cứ mỗi tháng một lần khi Fukami trở về Ohito,\nnhững vấn đề đó lại được giải quyết một cách êm đẹp.
- fix: Thế nhưng, cứ mỗi tháng một lần khi Fukami trở về Ohitoyo,\nnhững vấn đề đó lại được giải quyết một cách êm đẹp.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 2623 — item T2 (JP: 御一夜鉄道)

- JP: 一年一人で頑張って、僕らに不足している多くを、\n御一夜鉄道へと持ち込んでくれた。
- TW: 她獨自努力了一年，帶著我們所欠缺的許多事物，回到了御一夜鐵路。
- old_vn (csv3): Một năm trời nỗ lực một mình, em ấy đã mang về cho Đường sắt Ohito\nrất nhiều điều mà chúng tôi còn thiếu sót.
- fix: Một năm trời nỗ lực một mình, em ấy đã mang về cho Đường sắt Ohitoyo\nrất nhiều điều mà chúng tôi còn thiếu sót.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2562 — item T1 (JP: 御一夜)

- JP: ホテルの業務を、精神を身につけ、御一夜に持ち帰る。\nその時点でもう、かなり厳しい任務であろうに――
- TW: 去學習酒店的工作，去鑽研酒店的精神，然後帶回御一夜。她應該早就明白這個任務有多艱辛……
- old_vn (csv3): Học hỏi nghiệp vụ và tinh thần của khách sạn, rồi mang về Ohito.\nChỉ riêng điều đó thôi đã là một nhiệm vụ khá khó khăn rồi――
- fix: Học hỏi nghiệp vụ và tinh thần của khách sạn, rồi mang về Ohitoyo.\nChỉ riêng điều đó thôi đã là một nhiệm vụ khá khó khăn rồi――
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

### key 1871 — item T1 (JP: 御一夜)

- JP: 「御一夜のこと。わたしのこと。きっと助けてくれるから。\nいまも絶対、愛してくれてるって思うから」
- TW: 「她一定會幫助御一夜、一定會幫助我的。她現在肯定依然愛著我」
- old_vn (csv3): 「Chuyện của Ohito. Chuyện của tôi. Nhất định người đó sẽ giúp đỡ.\nBởi vì tôi tin rằng, bây giờ người đó vẫn tuyệt đối yêu thương tôi.」
- fix: 「Chuyện của Ohitoyo. Chuyện của tôi. Nhất định người đó sẽ giúp đỡ.\nBởi vì tôi tin rằng, bây giờ người đó vẫn tuyệt đối yêu thương tôi.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1.

## 09_Grand — `グランドリライト11_ナインスターズ！.txt.toml` (1 dòng)

### key 2385 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道の制服ば、あんまり着慣れんけん。\nちょっと前から、着こなしとか考えとったし」
- TW: 「因為我穿不太慣御一夜鐵路的制服。所以已經提早開始穿著適應了」
- old_vn (csv3): 「Đồng phục của Đường sắt Ohito, em mặc chưa quen lắm.\nNên từ trước em đã phải nghĩ xem mặc thế nào cho đẹp rồi.」
- fix: 「Đồng phục của Đường sắt Ohitoyo, em mặc chưa quen lắm.\nNên từ trước em đã phải nghĩ xem mặc thế nào cho đẹp rồi.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## §3. Ghi chú giữ lại / cờ (đã xem xét nhưng KHÔNG đổi thêm gì ngoài Ohito)

- **0 dòng bị loại vì JP không chứa thuật ngữ.** Cả 72 ứng viên đều có JP xác nhận (kanji trực tiếp). Không có flag misalignment nào trong batch này.
- **稀咲03_純白のレール 1906/1882 (audit-src):** lần xuất hiện trần thứ hai trong mỗi dòng (đoạn "Ohitoyo - Yunoi", JP 御一夜-湯医間) đã là "Ohitoyo" đúng sẵn do audit sửa trước — batch này chỉ đổi phần "Đường sắt Ohito". old_vn = giá trị audit.
- **グランドリライト06_稀咲 2146:** "đoạn giữa Ohitoyo và Yui" — "Yui" GIỮ NGUYÊN (thuộc mục T7, batch khác).
- **グランドリライト06_稀咲 2159:** "ông nội của Fukami" / "Ông Seki" GIỮ NGUYÊN (Seki → "ông ngoại" thuộc mục T20, batch khác).
- **凪h2_おとなの水着 1766:** "hợp đồng Maitetsu" GIỮ NGUYÊN (thuộc mục T74 OPEN, chưa quyết).
- **17 dòng audit-src** (グランドリライト06_稀咲 2054/1923/2014/2599; 稀咲01_金と人 1991/1704/2046/1785/2291/1775/1620/1749/1549/1551/1705; 稀咲03_純白のレール 1906/1882): old_vn = giá trị fix audit (0 dòng moan-src trong batch — không dòng H-file nào ở 06–11 còn "Ohito"). Các phần audit đã sửa khác (đại từ, gloss, "Meriken", Teitetsu…) được giữ nguyên, chỉ đổi Ohito. Riêng 稀咲01 1991 là dòng misaligned: CSV3 VN là câu thoại khác hoàn toàn ("Chuyện mời gọi nhà máy…"), audit đã viết lại đúng theo JP (chứa "Ohito") — old_vn ở đây là giá trị audit, đúng quy ước.
- **08_Niiroku / 10_Chikuni / 11_Other: 0 ứng viên.** 08 và 11 không có dòng "Ohito" nào ngay ở mức CSV3; 10_Chikuni có 6 dòng ở mức CSV3 nhưng cả 6 đã được audit sửa thành "Ohitoyo" (giá trị hiện tại không còn dạng cũ).
- **F-T1T2-1 (cờ cho coordinator / batch leftovers — 5 dòng chứa CẢ "Ohimitera" lẫn "Ohito" trần, đều ở ngoài phạm vi 06–11, đã bị loại khỏi cả U2a lẫn U2b theo quy tắc batch):** ハチロク01_こんにちわ赤ちゃん 2467 ("Đường sắt Ohito……đoạn Ohimitera-Hayato"); ハチロク12_ムナカタ来訪 1900 ("thành phố Ohimitera, và Đường sắt Ohito"); ハチロク12_ムナカタ来訪 2089 ("Đường sắt Ohito……Tuyến sông Ohimitera - Yatsushiro"); 日々姫08_とれいん食堂 3719 ("Đoạn (Yui) - Ohimitera - Hayato là của Đường sắt Ohito"); 真闇h3_補習授業の廃校舎 2524 ("thành phố Ohimitera và Đường sắt Ohito" — U1b đã ghi chờ T2). Sau khi batch U1 sửa xong phần "Ohimitera" của 5 dòng này, phần "Ohito" trần vẫn còn — cần một lượt leftovers T1/T2 quét lại 5 dòng này (old_vn lúc đó = giá trị fix của U1).
- **Không đụng dòng gasp Ư hay dòng "Kh" nào.** Không dòng ứng viên nào là dòng gasp/moans.

## §4. Lượt soát 2 (second pass — đọc lại toàn bộ 72 fix với JP)

- **Tổng số fix:** 72. **Tái kiểm chứng:** 72/72. **Bỏ:** 0. **Sửa:** 0.
- **Kiểm chứng cơ học độc lập (đọc lại từ CSV3 + fix-list audit/moans, bằng code path riêng, không dùng lại code lúc liệt kê):** 72/72 mục có key dạng string, jp/tw khớp CSV3 tuyệt đối, old_vn = current value đúng quy ước (moan > audit > CSV3), fix khác old_vn ĐÚNG ở chuỗi mục tiêu duy nhất (kiểm tra bằng placeholder-diff: fix chỉ đổi "Đường sắt Ohito"→"Đường sắt Ohitoyo" và/hoặc "Ohito"→"Ohitoyo", 0 ký tự khác thay đổi), 0 lần xuất hiện "Ohito" trần còn sót trong fix, item T1/T2/T1+T2 khớp dạng JP 72/72, JP chứa thuật ngữ 72/72, 0 dòng lẫn "Ohimitera".
- **Kiểm chứng TOML:** 12 khối TOML (một khối mỗi file), 72 khóa, parse OK bằng tomllib, giá trị parse được khớp JSON 72/72. Trong khối, `\\n` = ký tự `\n` thật trong giá trị (quy ước TOML block của dự án); `\\x` = ký tự `\x` thật; dấu `"` trong giá trị được escape thành `\"` (2 dòng: グランドリライト06_稀咲 2154, 凪ふかみ03 1411).
- **Đọc lại bằng mắt:** toàn bộ 72 dòng JP/TW/old_vn đã đọc ở lượt 1 (§2 từng dòng); lượt 2 đọc lại fix value của từng dòng theo quy tắc dài-trước-trần-sau và đếm lại số lần "Ohitoyo" trong fix = số "Ohitoyo" cũ + số "Ohito" trần cũ (72/72 khớp).

## §5. Khối TOML (12 file, 72 khóa — áp vào file TOML khi rebuild; `\\n` trong khối = ký tự \n thật trong giá trị)

### 06_Kisaki/グランドリライト06_稀咲.txt.toml

```toml
2054 = "「Có lẽ là có, nhưng tôi không biết.\\nỞ Đường sắt Ohitoyo, công việc này do các tình nguyện viên làm thủ công.」"
2485 = "「Vô số lần sao……Tàu của Đường sắt Ohitoyo,\\ncho dù bây giờ đã tăng chuyến, cũng đâu có chạy nhiều đến thế?」"
1923 = "「Nhưng……chuyển từ một công ty lớn ở Teito sang Đường sắt Ohitoyo,\\ndù nói ra từ lập trường của tôi thì cũng hơi...」"
2014 = "「Như tôi đã nói, hiện nay đường ray thay thế rất hiếm.\\nVì vậy ở Đường sắt Ohitoyo, trừ khi có chuyện bất đắc dĩ, nếu không thì không thể thay được.」"
2497 = "「Hiện tại, mật độ tàu của Đường sắt Ohitoyo cực kỳ thưa thớt. Do đó,\\nbằng cách \\x%l保線;#00ffc040;bảo trì đường ray%l;#; cẩn thận, chúng ta có thể kéo dài tuổi thọ của đường ray.」"
2146 = "「Cần tới bốn người cơ á! Phải làm thế――từng chỗ một sao?\\nĐường ray dài lắm mà, chỉ tính riêng đoạn giữa Ohitoyo và Yui thôi cũng đã...」"
2159 = "「Ông Seki――ông nội của Fukami, các tình nguyện viên \\x%l保線;#00ffc040;bảo trì đường ray%l;#;,\\nvà cả chúng ta, những người liên quan đến Đường sắt Ohitoyo.」"
2690 = "「Không còn cách nào khác ngoài việc thuê người có kinh nghiệm và trả lương cho họ.\\nMột điều tưởng chừng như hiển nhiên đó, lại rất khó khăn đối với Đường sắt Ohitoyo hiện tại.」"
3129 = "Đường sắt Ohitoyo hiện đang được hỗ trợ bởi các tình nguyện viên \\x%l保線;#00ffc040;bảo trì đường ray%l;#;,\\nnhưng nếu phải trả lương để thuê người, e rằng sẽ không trụ nổi."
2599 = "「Có khi thứ đó đã tồn tại rồi cũng nên.\\nChỉ là tôi không biết, và Đường sắt Ohitoyo cũng không có thôi.」"
2720 = "「Vậy tại sao Đường sắt Ohitoyo lại không có?\\nNếu áp dụng được, gánh nặng công việc sẽ giảm đi đáng kể mà.」"
2254 = "「Đường sắt Ohitoyo vốn đã thiếu nhân lực rồi. Chúng cháu không có lý do gì\\nđể từ chối sự gia nhập của một \\x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; xuất sắc và một \\x%lレイルロオド;#00ffc040;Railord%l;#; tối tân đâu ạ.」"
2154 = "「Đi kèm với hai điều trên là việc làm cho người dân.\\nĐây là một lợi ích quá rõ ràng đối với \"người dân Ohitoyo\".」"
2121 = "「Ừ. Ta sẽ hỗ trợ như đã hứa. Đưa 『Kế hoạch Tàu Hướng Tới Tương Lai』,\\ntrở thành phương án phục hưng Ohitoyo thay thế cho việc mời gọi nhà máy Aircra.」"
1326 = "……Thể chế Toàn Ohitoyo, cuối cùng cũng đã được thành lập tại đây."
3124 = "Vậy thì từ đây, chắc chắn chúng ta sẽ có thể phục hưng Ohitoyo,\\nvà cả ngành đường sắt nữa."
```

### 06_Kisaki/稀咲01_金と人.txt.toml

```toml
1800 = "「Dù góc nhìn và những gì chúng ta thấy có vẻ khác nhau,\\nnhưng anh cảm nhận được mong muốn phát triển Ohitoyo của chúng ta là như nhau.」"
1688 = "「Ohitoyo là thị trấn của shochu, và cũng là thị trấn của suối nước nóng.\\nẢnh hưởng từ sự thay đổi của nguồn nước sẽ lớn đến mức đó đấy.」"
2351 = "Việc em ấy trân trọng Ohitoyo, tôi thực sự đã cảm nhận được."
2198 = "Nhưng, em ấy trân trọng điều gì ở Ohitoyo,\\ncó lẽ chúng tôi đang có sự khác biệt ở điểm đó."
1991 = "「Nếu vậy……Ohitoyo sẽ đánh mất thương hiệu shochu Kuma.\\nKhoản lợi nhuận bị mất đó――đúng là không thể phớt lờ được.」"
1704 = "「Lợi ích thì có đấy. Nếu thành phố Ohitoyo suy tàn,\\nthì shochu Kuma, chèo thuyền trên sông Kuma hay đường sắt cũng sẽ lụi bại theo.」"
2046 = "「Việc ngăn chặn sự suy tàn của thành phố Ohitoyo không liên quan trực tiếp đến việc mời gọi nhà máy.\\nChúng cháu tin rằng có những cách khác để phục hưng Ohitoyo.」"
1785 = "「Việc thành phố Ohitoyo bị chia rẽ là điều không nên.\\nChúng ta cần cố gắng đạt được sự đồng thuận từ càng nhiều người càng tốt――」"
2291 = "Có thể sự mạnh mẽ được rèn giũa qua đó cũng tốt,\\nnhưng tôi không nghĩ đó là điều Ohitoyo cần lúc này."
1775 = "「Mục tiêu của bác chắc chắn không phải là việc mời gọi nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;.\\nViệc mời gọi nhà máy chỉ là phương tiện để phục hưng Ohitoyo và chấn hưng kinh tế thôi, đúng không ạ.」"
1620 = "「Haha, vậy là cháu muốn nói điều này sao.\\n『Cháu có một kế hoạch phục hưng Ohitoyo xuất sắc hơn việc mời gọi nhà máy』.」"
1749 = "「Mượn ví dụ lúc nãy của bác, thì đó là 『loại rượu không ngon nhưng rẻ』.\\nĐại đa số người dân Ohitoyo đều coi việc mời gọi nhà máy là như vậy.」"
1549 = "「Nhưng mà, Ohitoyo đang khốn khó.\\nDù là rượu rẻ tiền, nếu không có nó thì sẽ chết khát mất.」"
1551 = "「Nếu vậy thì tất cả đều là di vật của quá khứ.\\nKhông thể dẫn đến sự phục hưng của Ohitoyo được đâu.」"
1705 = "「Vậy thì, Giám đốc chi nhánh Ohitoyo. Việc mời gọi nhà máy cứ để ta lo.\\nCon hãy rút lui khỏi chuyện đó, và tập trung vào phương án khác đi.」"
```

### 06_Kisaki/稀咲03_純白のレール.txt.toml

```toml
1624 = "「Giai đoạn đầu thì chỉ có từ Đường sắt Ohitoyo thôi. Nhưng chẳng bao lâu sau,\\nĐường sắt Hisatsu Mikan cũng đã đăng ký tham gia.」"
2565 = "Do đó, về vấn đề này, chúng tôi đã thảo luận với Công ty Cổ phần Đường sắt Ohitoyo\\nđể nhờ họ nhận thầu công việc——"
1957 = "「Về chuyện đó thì——ngài nghĩ sao nếu dùng số tiền đó\\nđể mua lại toàn bộ đường ray của Đường sắt Ohitoyo ạ?」"
1906 = "「Của Đường sắt Ohitoyo…… đoạn Ohitoyo - Yunoi sao?」"
1963 = "「Chính vì thế. Công ty của ngài Soutetsu sẽ mua lại\\n『toàn bộ đường ray thuộc sở hữu của Đường sắt Ohitoyo』 ạ.」"
2894 = "Nếu vậy thì từ nay trở đi, Đường sắt Ohitoyo\\nsẽ không cần phải sở hữu nhân sự và thiết bị phục vụ cho việc \\x%l保線;#00ffc040;bảo trì đường ray%l;#; nữa——"
1882 = "「『Đợt huy động bổ sung kỳ 1;\\nTuyến đường đang hoạt động của Công ty CP Đường sắt Ohitoyo・Đoạn Ohitoyo - Yunoi』 sao ạ.」"
```

### 07_Nagi_Fukami/凪h2_おとなの水着.txt.toml

```toml
1766 = "……8620 đã hoàn toàn hồi sinh, và tôi cũng đã ký kết hợp đồng Maitetsu thông thường\\nvới Đường sắt Ohitoyo."
3568 = "Huy hiệu nguyên bản của Đường sắt Ohitoyo. Một cái bốn trăm yên.\\nTuy giản dị, nhưng đây cũng là một nguồn thu nhập quan trọng."
```

### 07_Nagi_Fukami/凪ふかみ03_三人いっしょ.txt.toml

```toml
2183 = "Bị hối thúc, tôi mở cuốn sổ tay có dòng chữ\\n“Chuyến đi dã ngoại đặc biệt ở Ohitoyo!” trên trang bìa."
1620 = "「Tụi em muốn cùng anh Soutetsu có một chuyến đi\\nđể tìm hiểu lại về Ohitoyo ạ」"
1411 = "「Ra là vậy. Chuyến đi \"dã ngoại\" để tìm hiểu về Ohitoyo sao」"
2489 = "Việc tìm hiểu về Ohitoyo,\\nchắc chắn sẽ có ích cho việc rút lại lời mời gọi xây dựng nhà máy."
1580 = "「Lò rèn cừ khôi nhất Ohitoyo!\\nBắt đầu từ lò rèn Minokasa!!」"
1646 = "「Vì vậy anh muốn cùng nhau học hỏi. Về Ohitoyo,\\nvề tương lai, về lẫn nhau, nhiều nhất có thể」"
```

### 07_Nagi_Fukami/凪ふかみ05_凪の開眼！？.txt.toml

```toml
2483 = "「Đúng vậy. Không hổ danh là Nagi. Người lái tàu tiếp theo của Đường sắt Ohitoyo.\\nKhông chỉ dễ thương, mạnh mẽ mà còn vô cùng thông minh xuất chúng nữa.」"
```

### 07_Nagi_Fukami/凪ふかみ08a_凪エピローグ_一番ほしい、一番.txt.toml

```toml
1888 = "「Hayase của Đường sắt Ohitoyo đã theo dõi giải đấu này nhiều năm rồi.\\nCô ấy phân tích dữ liệu rất kỹ lưỡng.」"
2840 = "Ngoài tôi và Nagi của Đường sắt Ohitoyo,\\ncác thành viên khác là hai người thuộc câu lạc bộ kiếm đạo Đường sắt Mikan do anh Munakata dẫn dắt."
2695 = "Đường sắt Ohitoyo đã nhận chuyển nhượng từ Đường sắt Mikan,\\nđầu máy số IX, chiếc đầu máy đã mất đi Railord của mình."
```

### 07_Nagi_Fukami/凪ふかみ08c_新しい家族.txt.toml

```toml
2585 = "「Sự liên kết giữa chuyến tàu BBQ và xuôi dòng sông Kuma.\\nViệc đó cũng đã tạo cú hích cho toàn bộ ngành du lịch và công nghiệp của Ohitoyo.」"
2199 = "「Không chỉ doanh thu của Đường sắt Ohitoyo, mà thu nhập thuế của thành phố Ohitoyo\\ncũng cho thấy sự gia tăng hơn hai mươi phần trăm so với năm ngoái.」"
2196 = "「Ở Ohitoyo cũng có đấy ạ. Những lời nhờ tư vấn như vậy, dạo gần đây.」"
2041 = "「A, ra là vậy! Vậy thì, kiểu như 'Đặc khu Lối sống mới' hay\\n'Đặc khu Hình thái Gia đình mới' ở Ohitoyo sao?」"
2420 = "「Ra là vậy, chuyện này――\\nCũng là một dự án liên quan mật thiết đến ý tưởng 'Thành phố Đường sắt Ohitoyo' nhỉ?」"
2341 = "「Đúng vậy, Kisaki. Thành phố Đường sắt Ohitoyo là nơi mà con người với con người,\\ncon người với \\x%lレイルロオド;#00ffc040;Railord%l;#;, có thể trở thành một gia đình kiểu mới.」"
2248 = "「Nhất định, sẽ biến Ohitoyo――\\nthành 'Đặc khu Hình thái Gia đình mới'.」"
```

### 09_Grand/グランドリライト01_オール御一夜、成立ならず.txt.toml

```toml
1550 = "「'Chuyến tàu hướng tới tương lai của Đường sắt Ohitoyo, nhất định bằng đôi tay này.\\nBằng những đôi tay đang đan vào nhau này, chắc chắn! Sẽ lăn bánh!'」"
```

### 09_Grand/グランドリライト02_ナビ.txt.toml

```toml
1684 = "「Ở Ohitoyo, ở nhà còn chất đống chuyện anh muốn làm.\\nAnh sẽ cố gắng về sớm nhất có thể, tất nhiên là sẽ khỏe mạnh trở về rồi.」"
2575 = "Lời đề nghị xin nghỉ phép đầu tiên kể từ khi trở về Ohitoyo\\nđã được nhà Migita và Đường sắt Ohitoyo nhanh chóng chấp thuận."
2213 = "Sáu năm rưỡi kể từ khi rời khỏi Ohitoyo.\\nTôi đã không thể nào dành ra được một giờ đồng hồ đó."
2319 = "Về Ohitoyo.\\nVề Đường sắt Ohitoyo."
1901 = "「Navi quan trắc thấy rằng, những người xung quanh ngài Soutetsu,\\nnhững người liên quan đến nhà Migita và Đường sắt Ohitoyo, đã thúc đẩy sự trưởng thành đó một cách đáng kể.」"
1017 = "――Navi lại tiếp tục bay thẳng.\\nHướng thẳng về phía Ohitoyo."
2355 = "Tôi có cảm giác rằng mình sẽ giải quyết được bài toán mà ông Mototada đặt ra,\\nvà có thể xây dựng nên một thể chế toàn Ohitoyo."
1713 = "「Hibiki này, anh――\\nmuốn hiểu thêm về Ohitoyo.」"
```

### 09_Grand/グランドリライト08_ふかみ.txt.toml

```toml
2604 = "Có vẻ như dịch vụ xuôi dòng sông Kuma cũng gặp vô vàn khó khăn,\\nvà Đường sắt Ohitoyo cũng đã phải chật vật rất nhiều."
2519 = "Thế nhưng, cứ mỗi tháng một lần khi Fukami trở về Ohitoyo,\\nnhững vấn đề đó lại được giải quyết một cách êm đẹp."
2623 = "Một năm trời nỗ lực một mình, em ấy đã mang về cho Đường sắt Ohitoyo\\nrất nhiều điều mà chúng tôi còn thiếu sót."
2562 = "Học hỏi nghiệp vụ và tinh thần của khách sạn, rồi mang về Ohitoyo.\\nChỉ riêng điều đó thôi đã là một nhiệm vụ khá khó khăn rồi――"
1871 = "「Chuyện của Ohitoyo. Chuyện của tôi. Nhất định người đó sẽ giúp đỡ.\\nBởi vì tôi tin rằng, bây giờ người đó vẫn tuyệt đối yêu thương tôi.」"
```

### 09_Grand/グランドリライト11_ナインスターズ！.txt.toml

```toml
2385 = "「Đồng phục của Đường sắt Ohitoyo, em mặc chưa quen lắm.\\nNên từ trước em đã phải nghĩ xem mặc thế nào cho đẹp rồi.」"
```

Kết bài

Đợt U2b hoàn tất: 72 dòng T1/T2 ở 06–11 đã đọc JP (+TW) từng dòng, sửa đúng dạng đích "Ohitoyo", soát lại 72/72, khối TOML parse-verified 72/72. Toàn dự án còn lại 5 dòng "Ohito" trần — cả 5 đều là dòng hai-dạng (kèm "Ohimitera") ở 01/02/05, đã cờ F-T1T2-1 cho batch leftovers. Không dòng nào cần Hieu quyết thêm trong batch này.