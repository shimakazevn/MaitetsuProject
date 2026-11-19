# Audit: Paulette 09_ストーブ客車 — 28 dòng Việt sai (đã đối chiếu JP + TW)

> **Lưu ý về tên file (quan trọng):** yêu cầu audit ghi hai file `ポーレット09_再開発の夢.txt.toml` (465 dòng) và `ポーレット09_波止場の朝.txt.toml` (397 dòng) — **cả hai tên đều không tồn tại** trong dự án: không có trong CSV "Trang tính 3", không có trong cả hai zip TOML (translation_toml.zip và translation_toml-2.zip), không xuất hiện trong docs hay trong bất kỳ tên file nào của dự án. Không có file nào trong dự án có 465 dòng; 397 dòng là `日々姫08_開きかけのつぼみ` (route Hibiki). **File Paulette 09 duy nhất trong dự án là `ポーレット09_ストーブ客車.txt.toml` (405 dòng)** — audit này kiểm tra file đó thay thế, theo đúng thứ tự route Paulette đang làm dở.

**Kết quả: 28/405 dòng sai (6,9%)** — 0 lệch vị trí, 0 chưa dịch, 0 cụt câu, 0 chưa chắc chắn. File sạch về cấu trúc, lỗi tập trung ở thuật ngữ theo quyết định mới. Cảnh: phiên chất vấn hội đồng về dự án Mine Treasure của Paulette (Soutetsu, Paulette, Kisaki, các nghị viên; Paulette kiệt sức tới mức ngất xỉu cuối phiên).

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 405 dòng script** (thoại 236, lời dẫn 169) đối chiếu JP + TW từ CSV "Trang tính 3", target là TOML-2. TW chỉ là nhân chứng thứ hai; chỗ nào JP và TW mâu thuẫn thì theo JP (quy tắc Hieu đặt 19/11).
- Heuristic thoại↔lời dẫn báo **0 dòng** — bắt được 0/28. Toàn bộ lỗi đều là cùng-loại (thuật ngữ, xưng hô, nghĩa, lỗi nhỏ) nên heuristic không thấy được; thêm một bằng chứng nữa rằng heuristic chỉ là cận dưới.
- Không có key-shift sạch (shift 0: 405/405; các shift khác chỉ ~0,35–0,43 — không có ý nghĩa vì key thưa và lỗi không phải lệch vị trí, không áp dụng).
- TOML và CSV giống hệt nhau về nội dung (272 dòng khác chỉ ở `\n`/khoảng trắng, 0 khác nội dung). Không có dòng CSV trống nào; VN==TW 1 dòng (1390 「…………」 — giống hệt nhau ở cả ba thứ tiếng, không phải chưa dịch).
- `[selections]` rỗng (0 mục). Thẻ `%l`: 41 dòng có thẻ, không dòng nào lệch thẻ.
- Phân loại lỗi: thuật ngữ 17 dòng (御一夜 11, 術仙 "Jussen" 6 — 2048 mang cả hai, 電車姫 1), xưng hô 4 dòng, sai nghĩa 4 dòng, lỗi nhỏ 3 dòng (mất tiếng hít っ). Theo người nói: lời dẫn 7, Paulette 7, Soutetsu 7, trung kiên nghị viên 2, lão nghị viên 2, Kisaki 1, chủ tọa 1, nữ nghị viên 1.
- Thoại sai 21/236 (8,9%), lời dẫn sai 7/169 (4,1%).
- Về xưng hô Soutetsu trong thoại: quét toàn bộ file bằng máy — "anh" tự xưng 1 lần (1746 — sai), "tôi" 10 lần (9 dòng), "em" ngôi hai 1 lần (1746 — giữ nguyên, thuộc đề xuất đang chờ). Khác hẳn 支線 (17/17 "anh") và 未来へのレール (13 lần "anh"/"em" so với 1 lần "tôi") — file này "tôi" chiếm đa số, chỉ 1 lần "anh" lọt qua.
- Về "mình" trong độc thoại: 8 dòng chứa "mình"/"Mình" — 4 dòng đúng (2482 sở hữu cách cho Sekihara, 2651 "giật mình", 2726 sở hữu cách cho Paulette, 2767 "đắm mình"), **4 dòng sai** (2594, 2633, 2640, 2968). Quét máy bằng regex chữ thường đã sót 2968 ("Mình" viết hoa đầu câu) — chỉ đọc kỹ mới bắt được. "mình" trong thoại: tất cả đều đúng (sở hữu cách/phản thân/thành ngữ: 1672, 1791, 1826, 1878, 1925, 2043, 2050, 2257).
- Không có file trùng lặp: file này chỉ tồn tại ở 03_Paulette/ (đã kiểm tra danh sách file toàn dự án trong CSV; không có bản sao ở thư mục khác — khác Grand Rewrite 04).

## Kết luận về cơ chế lỗi

Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương, không có dòng mồ côi — đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.381 mục): 24/28 dòng sai chỉ xuất hiện đúng 1 lần trong toàn dự án, tại chính key của nó. 4 ngoại lệ đều là mẫu hệ thống, không phải tràn chương:

- **2633/2640**: trùng nhau trong chính file này — cùng một giá trị Việt cho hai câu JP khác thì (2633 triển vọng "sắp hiểu ra" vs 2640 quá khứ "đã hiểu ra"); 2633 sai thì, 2640 đúng nghĩa nhưng sai xưng hô.
- **2274/2275** ("「!」"/"「!?」"): xuất hiện ở hàng trăm dòng khắp dự án — cùng một lỗi nhỏ hệ thống (mất tiếng hít っ) lặp lại ở mọi file, không phải câu của dòng khác. Tiền lệ Hachiroku 12 再開発 2103/2537 đã sửa thành "Ư!".

Cơ chế lỗi ở đây là **lỗi từng dòng rải rác + thuật ngữ theo quyết định mới (17/28)** — giống các file Paulette 06–08 sạch về cấu trúc, khác hẳn Paulette 03 (lệch vị trí hàng loạt).

## Chi tiết 28 dòng sai

### A. Thuật ngữ theo quyết định mới — 御一夜 = "Ohitoyo" (11 dòng, gồm 2048 mang cả hai lỗi)

**1668 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11).

- JP: 「でも、日々姫ちゃんもあなたも。求めているのは、
御一夜の持続的発展のための最善策だとも認識してます」
- TW: 「不過，我覺得日日姬和你追求的都是能讓御一夜持續發展的最佳策略」
- Cũ: 「Nhưng mà, cả Hibiki và chị. Em hiểu rằng điều mà hai người đang tìm kiếm,
là phương sách tốt nhất cho sự phát triển bền vững của Ohimitera.」
- Sửa: 「Nhưng mà, cả Hibiki và chị. Em hiểu rằng điều mà hai người đang tìm kiếm, là phương sách tốt nhất cho sự phát triển bền vững của Ohitoyo.」

**1710 [trung kiên nghị viên]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「三セク形式を取ると言っていますが、結局のところ、
利益が出た場合は御一夜鉄道にも入りますよね？」
- TW: 「你們說要採取第三部門的形式，也就是說要是最後產生了利益的話，御一夜鐵路也會獲得一部分吧？」
- Cũ: 「Cô nói sẽ áp dụng mô hình Khu vực ba, nhưng rốt cuộc,
nếu có lợi nhuận thì Đường sắt Ohito cũng sẽ được chia phần đúng không?」
- Sửa: 「Cô nói sẽ áp dụng mô hình Khu vực ba, nhưng rốt cuộc, nếu có lợi nhuận thì Đường sắt Ohitoyo cũng sẽ được chia phần đúng không?」

**1731 [Kisaki]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「他の出資者は、市と、御一夜鉄道、右田一酒造元、
クマ川下りといったあたりになるのかな？」
- TW: 「其他出資者大概有市政府、御一夜鐵路、右田一釀酒廠還有隈河漂流吧？」
- Cũ: 「Các nhà đầu tư khác sẽ là thành phố, Đường sắt Ohito, xưởng nấu rượu Migita Ichi,
và công ty xuôi dòng sông Kuma nhỉ?」
- Sửa: 「Các nhà đầu tư khác sẽ là thành phố, Đường sắt Ohitoyo, xưởng nấu rượu Migita Ichi, và công ty xuôi dòng sông Kuma nhỉ?」

**1738 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11).

- JP: 「冬の風物詩――御一夜でいえば、
クマ川下りのコタツ船になるわけだな」
- TW: 「冬天特有的景致——用御一夜來舉例，就好像隈河漂流的船上裝了被爐一樣吧」
- Cũ: 「Nét đặc trưng của mùa đông――nếu ở Ohimitera,
thì sẽ là thuyền sưởi ấm xuôi dòng sông Kuma nhỉ.」
- Sửa: 「Nét đặc trưng của mùa đông――nếu ở Ohitoyo, thì sẽ là thuyền sưởi ấm xuôi dòng sông Kuma nhỉ.」

**1907 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11).

- JP: 「交通のため、少なくとも御一夜において鉄道は必要です。
その維持管理のため、現状、わたしの能力は不可欠です」
- TW: 「御一夜的交通需要鐵路，為了管理鐵路，目前我的能力是必不可少的」
- Cũ: 「Vì mục đích giao thông, ít nhất ở Ohimitera, đường sắt là cần thiết.
Để duy trì và quản lý nó, hiện tại năng lực của tôi là không thể thiếu.」
- Sửa: 「Vì mục đích giao thông, ít nhất ở Ohitoyo, đường sắt là cần thiết. Để duy trì và quản lý nó, hiện tại năng lực của tôi là không thể thiếu.」

**1924 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11).

- JP: 「御一夜市民を中心にした公募採用を検討しています」
- TW: 「我們正考慮以御一夜市民為中心，進行公開招聘」
- Cũ: 「Chúng tôi đang cân nhắc việc tuyển dụng công khai với trọng tâm là công dân Ohimitera.」
- Sửa: 「Chúng tôi đang cân nhắc việc tuyển dụng công khai với trọng tâm là công dân Ohitoyo.」

**1940 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11).

- JP: 「僕は市長秘書だ。御一夜市が受給可能かもしれない
補助金については、当然、秘書の職務として調査した」
- TW: 「我是市長秘書。對於御一夜有希望領到的補助金，我完成秘書工作時已經調查過了」
- Cũ: 「Tôi là thư ký thị trưởng. Về khoản trợ cấp mà thành phố Ohimitera
có thể nhận được, đương nhiên, tôi đã điều tra với tư cách là nhiệm vụ của thư ký.」
- Sửa: 「Tôi là thư ký thị trưởng. Về khoản trợ cấp mà thành phố Ohitoyo có thể nhận được, đương nhiên, tôi đã điều tra với tư cách là nhiệm vụ của thư ký.」

**1967 [chủ tọa]** — 御一夜 = "Ohitoyo" (quyết định 19/11).

- JP: 「御一夜の未来を考える会。
[にいつ,1]新津議員。質問をどうぞ」
- TW: 「接下來有請御一夜未來規劃會的新津議員提問」
- Cũ: 「Hội Suy nghĩ về Tương lai của Ohimitera.
Nghị viên Niitsu. Xin mời đặt câu hỏi.」
- Sửa: 「Hội Suy nghĩ về Tương lai của Ohitoyo. Nghị viên Niitsu. Xin mời đặt câu hỏi.」

**2048 [Soutetsu]** — Hai thuật ngữ trong một dòng: 術仙炭鉱 = "mỏ than Jutsu-sen" và 御一夜 = "Ohitoyo" (quyết định 19/11).

- JP: 「そう。そして旧術仙炭鉱の現所有者は御一夜市であり、
補助金制度はまだ生きている」
- TW: 「沒錯。而且現在舊術仙煤礦的所有者是御一夜市，補助金制度還存在著」
- Cũ: 「Đúng vậy. Hơn nữa, chủ sở hữu hiện tại của mỏ than Jussen cũ là thành phố Ohimitera,
và chế độ trợ cấp vẫn còn hiệu lực.」
- Sửa: 「Đúng vậy. Hơn nữa, chủ sở hữu hiện tại của mỏ than Jutsu-sen cũ là thành phố Ohitoyo, và chế độ trợ cấp vẫn còn hiệu lực.」

**2237 [trung kiên nghị viên]** — 御一夜 = "Ohitoyo" (quyết định 19/11).

- JP: 「なら、いますぐに辞職をすればいい。そんなハンパな
覚悟の市長に、御一夜の舵取りは任せられない」
- TW: 「那您何不現在就辭去市長之位。我們無法將御一夜的未來交給一個搖擺不定的市長」
- Cũ: 「Vậy thì cô hãy từ chức ngay bây giờ đi. Không thể giao phó việc lèo lái Ohimitera
cho một thị trưởng với sự quyết tâm nửa vời như vậy được.」
- Sửa: 「Vậy thì cô hãy từ chức ngay bây giờ đi. Không thể giao phó việc lèo lái Ohitoyo cho một thị trưởng với sự quyết tâm nửa vời như vậy được.」

**2468 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11).

- JP: 工場誘致自体が目的。
御一夜の発展を――ではなく。
- TW: 他的目的是讓工廠落戶，而不是御一夜的發展。
- Cũ: Mục tiêu là bản thân việc thu hút nhà máy.
Chứ không phải là――sự phát triển của Ohimitera.
- Sửa: Mục tiêu là bản thân việc thu hút nhà máy. Chứ không phải là――sự phát triển của Ohitoyo.

### B. Thuật ngữ — 術仙 "Jussen" → "Jutsu-sen" (6 dòng)

**1368 [lời dẫn]** — 術仙炭鉱 = "mỏ than Jutsu-sen" (quy ước dự án); bản cũ viết thiếu chữ "t" thành "Jussen".

- JP: ……質問時間を、まるで気にしていないようだ。
関原議員は淡々と、術仙炭鉱の歴史を語る。
- TW: ……關原議員彷彿毫不在意提問時間的限制，將術仙煤礦的歷史悠悠道來。
- Cũ: "...Dường như ông ta hoàn toàn không bận tâm đến thời gian đặt câu hỏi.
Nghị viên Sekihara cứ bình thản kể về lịch sử của mỏ than Jussen."
- Sửa: "...Dường như ông ta hoàn toàn không bận tâm đến thời gian đặt câu hỏi. Nghị viên Sekihara cứ bình thản kể về lịch sử của mỏ than Jutsu-sen."

**1892 [lão nghị viên]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ thiếu "t".

- JP: 「わしらね、市長。術仙炭鉱で昔働いていたとですよ」
- TW: 「市長啊，我們以前就在術仙煤礦工作」
- Cũ: 「Bọn tôi ấy mà, thưa thị trưởng. Ngày xưa từng làm việc ở mỏ than Jussen đấy.」
- Sửa: 「Bọn tôi ấy mà, thưa thị trưởng. Ngày xưa từng làm việc ở mỏ than Jutsu-sen đấy.」

**2081 [lão nghị viên]** — 術仙 = "Jutsu-sen"; bản cũ thiếu "t".

- JP: 「採炭ば、国の基幹産業の一つと言われておりましてな。
[じゅつせん,1]術仙は、その中でも十指に入る、優良炭鉱だったとです」
- TW: 「煤礦在當時是國家的基礎產業之一。術仙煤礦在整個國家的煤礦中也是屈指可數的富礦」
- Cũ: 「Khai thác than từng được coi là một trong những ngành công nghiệp mũi nhọn của đất nước.
Jussen là một mỏ than ưu tú, lọt top mười trong số đó đấy.」
- Sửa: 「Khai thác than từng được coi là một trong những ngành công nghiệp mũi nhọn của đất nước. Jutsu-sen là một mỏ than ưu tú, lọt top mười trong số đó đấy.」

**2156 [Paulette]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ thiếu "t".

- JP: 「術仙炭鉱の会計資料については、
わたしも確認させていただいております」
- TW: 「術仙煤礦的帳目資料我也有確認過」
- Cũ: 「Về các tài liệu kế toán của mỏ than Jussen,
tôi cũng đã xác nhận rồi ạ.」
- Sửa: 「Về các tài liệu kế toán của mỏ than Jutsu-sen, tôi cũng đã xác nhận rồi ạ.」

**2782 [lời dẫn]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ thiếu "t".

- JP: 僕らが想像していたよりも、
術仙炭鉱は、はるかに豊かな[やま,1]鉱山だったのだ。
- TW: 看來術仙煤礦曾經比我們想像的還要富有。
- Cũ: Hơn cả những gì chúng tôi từng tưởng tượng,
Mỏ than Jussen đã từng là một mỏ quặng trù phú đến nhường nào.
- Sửa: Hơn cả những gì chúng tôi từng tưởng tượng, Mỏ than Jutsu-sen đã từng là một mỏ quặng trù phú đến nhường nào.

**2048 [Soutetsu]** đã liệt kê ở mục A — dòng này mang cả hai lỗi (Jussen + Ohimitera) và đã sửa cả hai trong một bản sửa.

### C. Thuật ngữ — 電車姫 (1 dòng)

**2262 [Soutetsu]** — 電車姫 — cả file dùng "Densha Hime" 6 lần (1837, 1938, 2129, 2137, 2720, 2723), toàn dự án 20 vs 2; dòng này là ngoại lệ duy nhất trong file. (Dòng còn lại dùng "Công chúa Xe điện" là Grand 01 key 2710.)

- JP: 「電車姫――とは、確か、
廣島の毛利電鉄のオーナーのことだったか」
- TW: 「電車公主——我記得是廣島毛利電鐵的所有者吧」
- Cũ: 「Công chúa Xe điện――nhớ không nhầm thì,
là chủ sở hữu của Đường sắt điện Mouri ở Hiroshima nhỉ.」
- Sửa: 「Densha Hime――nhớ không nhầm thì, là chủ sở hữu của Đường sắt điện Mouri ở Hiroshima nhỉ.」

### D. Xưng hô (4 dòng)

**1746 [Soutetsu]** — Soutetsu tự xưng "anh" với Paulette — trái docs locations §2.1 ("Tôi"; "Anh" chỉ với Hibiki). Quét máy toàn file: Soutetsu xưng "tôi" 10 lần trong thoại, chỉ 1 lần "anh" (dòng này). Giữ "em" cho Paulette — thuộc đề xuất "cô" vs "em" đang chờ chốt, không đổi ở đây.

- JP: 「そのときには、僕と一緒に乗ってくれないか？
蒼森、津輕の――津っ鐵さんのストーブ\x%l列車;#00ffc040;列車%l;#;に」
- TW: 「到時候，能和我一起去嗎？一起去坐青森津輕——津鐵的暖爐\x%l列車;#00ffc040;列車%l;#;」
- Cũ: 「Đến lúc đó, em đi cùng anh nhé?
Lên chuyến \x%l列車;#00ffc040;tàu%l;#; sưởi ấm của Tsutetsu――ở Tsugaru, Aomori.」
- Sửa: 「Đến lúc đó, em đi cùng tôi nhé? Lên chuyến \x%l列車;#00ffc040;tàu%l;#; sưởi ấm của Tsutetsu――ở Tsugaru, Aomori.」

**2594 [lời dẫn]** — "mình" chỉ Soutetsu trong độc thoại — quy ước của file là "Tôi" (độc thoại dùng "Tôi" ở hàng chục dòng, chỉ 4 dòng dùng "mình" cho Soutetsu: 2594, 2633, 2640, 2968).

- JP: 下戸の僕さえ、飲みたくなるような情景が
脳裏に容易に浮き上がってくる。
- TW: 就連平時不喝酒的我，想到那一幅情景也不禁想要小酌兩杯。
- Cũ: Ngay cả một kẻ không biết uống rượu như tôi,
cũng dễ dàng mường tượng ra viễn cảnh khiến mình muốn nhâm nhi vài chén.
- Sửa: Ngay cả một kẻ không biết uống rượu như tôi, cũng dễ dàng mường tượng ra viễn cảnh khiến tôi muốn nhâm nhi vài chén.

**2640 [lời dẫn]** — "mình" làm chủ ngữ mệnh đề phụ cho Soutetsu trong độc thoại — quy ước "Tôi". (Nghĩa "đã hiểu ra" của dòng này là đúng, chỉ sai xưng hô.) Sửa: "Tôi có cảm giác như đã hiểu ra rồi."

- JP: わかった気がする。
- TW: 我好像懂了。
- Cũ: Tôi có cảm giác mình đã hiểu ra.
- Sửa: Tôi có cảm giác như đã hiểu ra rồi.

**2968 [lời dẫn]** — "Mình" đầu câu trong độc thoại ngoặc đơn — quy ước của file là "Tôi". (Khác tiền lệ whatsentertainment 2051, nơi "mình" được giữ vì đó là lời thoại trích dẫn trong thoại — đây là lời dẫn thuần.)

- JP: （ポーレットに心的不安があると……
その可能性に、僕は思い当たっていたのに――）
- TW: （我明明有猜想到，波萊特可能有著心靈創傷——）
- Cũ: "（Rằng Paulette đang có những bất an trong lòng...
Mình đã lờ mờ nhận ra khả năng đó rồi cơ mà――）"
- Sửa: "（Rằng Paulette đang có những bất an trong lòng... Tôi đã lờ mờ nhận ra khả năng đó rồi cơ mà――）"

### E. Sai nghĩa (4 dòng)

**1655 [Paulette]** — JP 「やっ――」 là câu cắt ngang (TW 不要 = "đừng"); bản cũ "Khôn――" vô nghĩa trong ngữ cảnh — Kisaki vừa nói còn quá sớm để nhận lời cảm ơn, Paulette ngắt lời.

- JP: 「やっ――」
- TW: 「不要——」
- Cũ: 「Khôn――」
- Sửa: 「Đừng――」

**1785 [Paulette]** — JP 「できますよ？　経験」 là khẳng định khả năng ("làm được mà"), TW 可以體驗到哦 — bản cũ "Được chứ anh?" đổi thành câu hỏi xin phép và thêm "anh" không có trong JP. Người nghe là lão nghị viên nên dùng "ạ".

- JP: 「できますよ？　経験」
- TW: 「可以體驗到哦」
- Cũ: 「Được chứ anh? Trải nghiệm ấy.」
- Sửa: 「Được chứ ạ. Trải nghiệm ấy.」

**2041 [nữ nghị viên]** — JP 民意は、それで問い直せるわね — 問い直す = "hỏi lại/thăm dò lại"; bản cũ "lấy lại được ý dân" (giành lại) sai nghĩa.

- JP: 「民意は、それで問い直せるわね」
- TW: 「正好通過那樣獲取最新的民意」
- Cũ: 「Như vậy thì có thể lấy lại được ý dân nhỉ.」
- Sửa: 「Như vậy thì có thể hỏi lại ý dân nhỉ.」

**2633 [lời dẫn]** — JP わかってしまうような気がする (sắp/có lẽ sẽ hiểu ra — triển vọng) vs 2640 わかった気がする (đã hiểu) — bản cũ trùng hệt giá trị của 2640 ("Tôi có cảm giác mình đã hiểu ra"), sai thì và trùng lặp. Sửa: "Tôi có cảm giác như sắp hiểu ra rồi."

- JP: わかってしまうような気がする。
- TW: 我似乎明白了。
- Cũ: Tôi có cảm giác mình đã hiểu ra.
- Sửa: Tôi có cảm giác như sắp hiểu ra rồi.

### F. Lỗi nhỏ — mất tiếng hít っ (3 dòng)

**2274 [Paulette]** — JP 「っ！」 (tiếng hít mạnh) — bản cũ chỉ còn "「!」", mất hẳn tiếng っ; tiền lệ Hachiroku 12 再開発 2103/2537 sửa thành "Ư!".

- JP: 「っ！」
- TW: 「！」
- Cũ: 「!」
- Sửa: 「Ư!」

**2275 [Soutetsu]** — JP 「っ！？」 — mất tiếng hít っ; sửa theo tiền lệ 再開発 2103/2537.

- JP: 「っ！？」
- TW: 「！？」
- Cũ: 「!?」
- Sửa: 「Ư!?」

**2277 [Soutetsu]** — JP 「～っ！」 — mất tiếng hít っ; sửa theo tiền lệ 再開発 2103/2537 (giữ dấu ~ như bản cũ).

- JP: 「～っ！」
- TW: 「～！」
- Cũ: 「~!」
- Sửa: 「~Ư!」

## Bằng chứng mới cho các quyết định đang chờ + quan sát không tính sai

- **Soutetsu gọi Paulette "cô" vs "em" — bằng chứng mới ĐẢO HƯỚNG so với Paulette 08:** trong file này Soutetsu gọi Paulette là "cô" 7 lần (1395, 1713, 1805, 1819, 1931, 2129, 2177) và "em" chỉ 1 lần (1746). Paulette 08 đề xuất thống nhất "em" dựa trên 1534 ("Rất vinh hạnh được em khen") đối lập 1623/1715/1739 ("cô"); file này "cô" áp đảo 7:1. Không thể chốt quy tắc xưng hô từ một file duy nhất — chờ Hieu quyết.
- **"KiHa 07":** 1 gloss ở 2609 — thêm bằng chứng cho đề xuất thống nhất "KiHa" (cách viết chính thức của JR; Paulette 08 đã có 6 gloss "KiHa").
- **湯医, 帝鉄, 冥国, 冥軍, 小畑, 大畑, 駿袋鉄道, 整備体/運転ボディ, 端的 không xuất hiện trong file.** コン xuất hiện 1 lần ở 2210 nhưng là コントロール, không phải cáo コン.
- **1731 "xưởng nấu rượu Migita Ichi"** (JP 右田一酒造元, TW 右田一釀酒廠 — JP/TW đồng thuận nên giữ nguyên, không tính sai): docs locations §2.6 ghi nhà máy rượu là "Migita System" — hai cách gọi cùng tồn tại toàn dự án ("Migita System" 11, "Migita Ichi" 15). Cần Hieu đối chiếu docs với JP.
- **Không tính sai (ghi để minh bạch):** 2446 thêm "nghe cô ấy kể mà" (TW cũng có 光是聽著 — diễn giải ngữ cảnh, không đổi nghĩa); 1972 "hai người đến đây" (Paulette + Soutetsu cùng đến gặp Kisaki — đúng ngữ cảnh, JP không ghi số người); 1709 "Khu vực ba sao?" (hạt "sao" hỏi, nhất quán với 2824 "Khu vực ba"); 1931 "thảo luận" thay cho 相談 (diễn giải nhẹ, không đổi nghĩa).
- **Hai trường hợp JP-thắng-TW (không phải lỗi — ghi nhận quy tắc hoạt động):** 1828 TW chèn "電車公主的電車" trong khi JP nói 廣島の話 — bản Việt theo đúng JP ("vụ ở Hiroshima"); 2540 TW viết 前任市長的左膀右臂 trong khi JP là 右腕 — bản Việt "cánh tay phải" theo đúng JP.

## Khối TOML sửa (28 dòng)

```toml
1368 = "\"...Dường như ông ta hoàn toàn không bận tâm đến thời gian đặt câu hỏi. Nghị viên Sekihara cứ bình thản kể về lịch sử của mỏ than Jutsu-sen.\""
1655 = "「Đừng――」"
1668 = "「Nhưng mà, cả Hibiki và chị. Em hiểu rằng điều mà hai người đang tìm kiếm, là phương sách tốt nhất cho sự phát triển bền vững của Ohitoyo.」"
1710 = "「Cô nói sẽ áp dụng mô hình Khu vực ba, nhưng rốt cuộc, nếu có lợi nhuận thì Đường sắt Ohitoyo cũng sẽ được chia phần đúng không?」"
1731 = "「Các nhà đầu tư khác sẽ là thành phố, Đường sắt Ohitoyo, xưởng nấu rượu Migita Ichi, và công ty xuôi dòng sông Kuma nhỉ?」"
1738 = "「Nét đặc trưng của mùa đông――nếu ở Ohitoyo, thì sẽ là thuyền sưởi ấm xuôi dòng sông Kuma nhỉ.」"
1746 = "「Đến lúc đó, em đi cùng tôi nhé? Lên chuyến \\x%l列車;#00ffc040;tàu%l;#; sưởi ấm của Tsutetsu――ở Tsugaru, Aomori.」"
1785 = "「Được chứ ạ. Trải nghiệm ấy.」"
1892 = "「Bọn tôi ấy mà, thưa thị trưởng. Ngày xưa từng làm việc ở mỏ than Jutsu-sen đấy.」"
1907 = "「Vì mục đích giao thông, ít nhất ở Ohitoyo, đường sắt là cần thiết. Để duy trì và quản lý nó, hiện tại năng lực của tôi là không thể thiếu.」"
1924 = "「Chúng tôi đang cân nhắc việc tuyển dụng công khai với trọng tâm là công dân Ohitoyo.」"
1940 = "「Tôi là thư ký thị trưởng. Về khoản trợ cấp mà thành phố Ohitoyo có thể nhận được, đương nhiên, tôi đã điều tra với tư cách là nhiệm vụ của thư ký.」"
1967 = "「Hội Suy nghĩ về Tương lai của Ohitoyo. Nghị viên Niitsu. Xin mời đặt câu hỏi.」"
2041 = "「Như vậy thì có thể hỏi lại ý dân nhỉ.」"
2048 = "「Đúng vậy. Hơn nữa, chủ sở hữu hiện tại của mỏ than Jutsu-sen cũ là thành phố Ohitoyo, và chế độ trợ cấp vẫn còn hiệu lực.」"
2081 = "「Khai thác than từng được coi là một trong những ngành công nghiệp mũi nhọn của đất nước. Jutsu-sen là một mỏ than ưu tú, lọt top mười trong số đó đấy.」"
2156 = "「Về các tài liệu kế toán của mỏ than Jutsu-sen, tôi cũng đã xác nhận rồi ạ.」"
2237 = "「Vậy thì cô hãy từ chức ngay bây giờ đi. Không thể giao phó việc lèo lái Ohitoyo cho một thị trưởng với sự quyết tâm nửa vời như vậy được.」"
2262 = "「Densha Hime――nhớ không nhầm thì, là chủ sở hữu của Đường sắt điện Mouri ở Hiroshima nhỉ.」"
2274 = "「Ư!」"
2275 = "「Ư!?」"
2277 = "「~Ư!」"
2468 = "Mục tiêu là bản thân việc thu hút nhà máy. Chứ không phải là――sự phát triển của Ohitoyo."
2594 = "Ngay cả một kẻ không biết uống rượu như tôi, cũng dễ dàng mường tượng ra viễn cảnh khiến tôi muốn nhâm nhi vài chén."
2633 = "Tôi có cảm giác như sắp hiểu ra rồi."
2640 = "Tôi có cảm giác như đã hiểu ra rồi."
2782 = "Hơn cả những gì chúng tôi từng tưởng tượng, Mỏ than Jutsu-sen đã từng là một mỏ quặng trù phú đến nhường nào."
2968 = "\"（Rằng Paulette đang có những bất an trong lòng... Tôi đã lờ mờ nhận ra khả năng đó rồi cơ mà――）\""
```

## Việc tiếp theo

- Sau khi áp 28 bản sửa, file coi như xong, trừ việc chờ Hieu chốt các quyết định đang chờ (đặc biệt "cô" vs "em" cho Paulette — file này cho bằng chứng mới 7:1 nghiêng về "cô"; và "KiHa" vs "Kiha"; và Migita System vs Migita Ichi).
- Lưu ý: 3 dòng mất tiếng hít っ (2274/2275/2277) là một mẫu hệ thống toàn dự án — cùng một lỗi xuất hiện ở hàng trăm dòng khác; nếu Hieu muốn, đợt thống nhất sau có thể quét toàn dự án cho mẫu này (JP 「っ！」→ "Ư!").
- File Paulette 09 thực tế chỉ có 1 file (ストーブ客車) — hai tên file 再開発の夢 / 波止場の朝 trong yêu cầu audit không tồn tại trong dự án; nếu Hieu có hai chương đó dưới tên khác thì gửi lại tên đúng.

## Kết bài

File ポーレット09_ストーブ客車 là file thứ 21 được audit toàn bộ (28/405 = 6,9% sai): sạch về cấu trúc (0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng chưa dịch, 0 dòng chưa chắc chắn) — lỗi tập trung ở thuật ngữ theo quyết định mới (17/28, trong đó 11 dòng Ohitoyo và 6 dòng "Jussen") cộng một ít xưng hô/nghĩa rải rác. Điểm đáng chú ý nhất là bằng chứng "cô" vs "em" đảo hướng so với Paulette 08: ở file này Soutetsu gọi Paulette là "cô" tới 7 lần, chỉ 1 lần "em" — cho thấy không thể chốt quy tắc xưng hô từ một file duy nhất. Sau khi áp 28 bản sửa, file coi như xong. 21 file đã audit xong đã có 1.628 dòng sai — và việc Paulette 09 (6,9%) sạch về cấu trúc trong khi Paulette 03 廃炭鉱 (31%) và obasan (56%) nặng lệch vị trí càng chứng minh không thể đoán độ sạch hay loại lỗi từ tên chương hay file bên cạnh; vẫn phải đọc hết từng dòng.
