# Audit: Paulette 06_おひとよマイントレジャー — 25 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/ポーレット06_おひとよマイントレジャー.txt.toml` — 367 dòng script, **25 dòng Việt sai = 6,8%**, 0 dòng chưa chắc chắn.
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. Đây là file thứ 15 audit toàn bộ, sau 廃炭鉱 31%, obasan 56%, Grand 01 45,6%, Hibiki 03 86,2%, Hachiroku 13 夜の嵐 44,9%, 実りの秋 0,4%, Nagi_Fukami 08a 4,3%, Hachiroku 12 ムナカタ来訪 2,3%, 再開発 4,4%, Paulette 04_ヒヤリング 1,8%, stove 22,1%, Paulette 05_whatsentertainment 2,8%, 鳴呼の町 5,0%, Grand Rewrite 04 3,9%.

## Phương pháp và số liệu kiểm chứng
- Đã đọc **hết 367/367 dòng script** (key 1435–2836), đối chiếu từng dòng với JP + TW theo nghĩa, người nói, thoại/lời dẫn, xưng hô độc thoại theo quy ước của chính file. Không ngoại suy tổng dự án từ file này.
- Phân loại 25 dòng sai: **thuật ngữ 16** (1464, 1765, 1851, 1964, 1974, 1980, 1983, 2026, 2148, 2155, 2182, 2186, 2210, 2415, 2704, 2753 — "Jussen" 6 dòng và "Ohimitera" 11 dòng, 1464 mang cả hai lỗi), **xưng hô 4** (1718, 1873, 1879, 2539), **sai nghĩa 4** (2089, 2369, 2533, 2836), **lỗi nhỏ 1** (1934). Lệch vị trí 0, chưa dịch 0, cụt câu 0, không chắc chắn 0.
- Thoại sai 18/212 (8,5%); lời dẫn (monologue) sai 7/155 (4,5%). Theo người nói: monologue 7, Soutetsu 6, Kisaki 4, Hibiki 4, Paulette 3, Fukami 1; Reina, Nagi, Hachiroku, Manami 0.
- Phân bố lỗi theo đoạn: key 1464–2026: 12 dòng; 2089–2415: 8 dòng; 2533–2836: 5 dòng — lỗi rải đều cả file, không tập trung một cảnh nào.
- **Heuristic thoại/dẫn báo 2 dòng** (2369, 2711) — 2369 là lỗi thật nhưng heuristic bắt vì lý do sai (thiếu dấu 「」 quanh từ "と", trong khi lỗi thật là dịch "to" thành "với" — xem mục C); 2711 là dương tính giả hoàn toàn (trích dẫn lồng trong lời dẫn, VN dùng "..." thay vì 「」 nhưng nội dung đúng). Heuristic bắt được **1/25 dòng sai (4,0%)** tính theo dòng, **0/25 theo đúng lý do** — thêm một minh chứng heuristic chỉ là giới hạn dưới.
- **Không có key-shift sạch:** test shift −2..+2 trên dấu thoại/dẫn, tốt nhất ở shift 0 (365/367 = 0,995; hai dòng lệch là 2369 và 2711 đã nói trên). Không có bằng chứng lệch đều; lỗi xác nhận bằng đọc ngữ nghĩa từng dòng + đối chiếu chỉ mục Việt toàn dự án.
- **TOML và CSV giống hệt nhau về nội dung:** kiểm tra toàn bộ 367 dòng, 0 dòng khác nội dung thực (229 dòng chỉ khác `\n`/khoảng trắng — theo quyết định của Hieu ngày 19/11, `\n` thủ công không quan trọng vì game tự xuống dòng). Không có dòng CSV trống nào trong file này. VN==TW: chỉ 1462 là 「…………」 (giống hệt nhau ở cả ba ngôn ngữ, không phải lỗi).
- **Không xét lỗi định dạng `\n`:** chỉ báo lỗi nội dung. Các bản sửa trong khối TOML bên dưới viết liền một dòng.
- **[selections]:** file có tiêu đề section `[selections]` nhưng **rỗng (0 mục)** — không có lựa chọn nào để kiểm tra hay sửa.
- **Thẻ `%l`:** không có dòng nào VN thêm/thiếu thẻ so với JP. Dấu gạch ―― trong bản sửa viết không khoảng trắng hai bên, theo quy ước dự án (22.055 dòng). Chú ý: dấu gạch trong file này là U+2015 (―), không phải U+2014 (—).
- **Không trùng file:** file này chỉ xuất hiện một lần trong zip, chỉ trong thư mục `03_Paulette/` — không có bản sao y hệt ở thư mục khác như Grand Rewrite 04.

## Kết luận về cơ chế lỗi
- **Không có lệch vị trí nào trong file này** — lần đầu tiên kể từ Nagi_Fukami 08a mà một file hoàn toàn không có dòng nào bị dán nhầm, và là file thứ hai liên tiếp (sau Grand 04) không có lệch vị trí. 0 dòng mồ côi, 0 cặp chuyển chỗ, 0 tràn chương, 0 trùng lặp nội bộ sai: mọi câu Việt sai đều đứng đúng key của nó, chỉ sai ở mức từ/câu.
- **16/25 lỗi là thuật ngữ theo quyết định đã chốt** (11 "Ohimitera" → "Ohitoyo" và 6 "Jussen" → "Jutsu-sen", 1464 mang cả hai). Nếu trừ 16 dòng thuật ngữ này, file chỉ còn 9 lỗi thực chất (2,5%) — nghĩa là phần lớn "tỷ lệ sai" của file này là do hai quy ước mới chưa được áp dụng ngược, không phải do dịch sai nội dung. 11 dòng "Ohimitera" gồm cả tên cơ sở "Ohimitera Mine Treasure" xuất hiện 4 lần (1851, 1980, 2148, 2186) — tên dự án của cả chương, nên việc đổi sang "Ohitoyo" ảnh hưởng trực tiếp tới tên gọi mà người chơi sẽ thấy trong game.
- **Lỗi đáng chú ý nhất là cặp chơi chữ "Treasure to Leisure" (2369, 2836):** cả hai dòng đều dịch từ nối tiếng Anh "to" thành từ Việt ("với", "và"), làm mất trò chơi chữ mà cả chương xoay quanh — tên dự án "Ohitoyo Mine Treasure" được đặt ra chính vì nó nối được với "Leisure" bằng "to" (xem 2160: Paulette nói thẳng "Cảm giác như chơi chữ với từ 'Leisure' vậy" — dòng này dịch đúng). TW ở cả hai chỗ đều giữ nguyên "ｔｏ　Ｌｅｉｓｕｒｅ", xác nhận "to" phải giữ nguyên.
- **Xưng hô Soutetsu:** 3/4 lỗi xưng hô là Soutetsu tự xưng "anh" (1873, 1879 trong thoại; 2539 trong độc thoại) trong khi file này anh dùng "tôi" ở 4 chỗ khác (1723, 1895, 2042, 2165) và gọi Paulette "cô" (2047) — không có cách phân biệt theo người nghe: "anh" xuất hiện cả khi nói với nhóm/Kisaki lẫn khi nói với Paulette, còn "tôi" cũng xuất hiện khi nói với Paulette (1984 ở file tuyết — xem audit file kia). Theo docs (locations §2.1) Soutetsu xưng "Tôi", chỉ dùng "Anh" khi nói với em gái Hibiki; 2000 trong file này ("anh đang nghĩ xem...") là nói với Hibiki nên đúng và không sửa.
- 342 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Chi tiết 25 dòng sai

### A. Thuật ngữ (16 dòng)
**A1. 術仙炭鉱 = "mỏ than Jutsu-sen", không phải "Jussen" (6 dòng — file viết thiếu chữ "t", cùng lỗi đã thấy ở Grand 04).**
- **1464** (Paulette): JP 「……術仙炭鉱にポジションを取った人が――御一夜には、たくさんいる」 — VN cũ "mỏ than Jussen" và "Ở Ohimitera" (cả hai lỗi trong một dòng). Sửa cả hai: "mỏ than Jutsu-sen――Ở Ohitoyo".
- **1765** (Hibiki): JP 「つまりこれ、術仙廃炭鉱一帯をまるごと、宝探しテーマパークにするってことですよね」 — "mỏ than bỏ hoang Jussen" → "mỏ than bỏ hoang Jutsu-sen".
- **1974** (Soutetsu): JP 「術仙廃炭鉱の再調査。れいなにも同行をしてもらいたい」 — "mỏ than bỏ hoang Jussen" → "mỏ than bỏ hoang Jutsu-sen".
- **2155** (Soutetsu): JP 「術仙廃炭鉱は、市の所有地なのだから」 — "mỏ than bỏ hoang Jussen" → "mỏ than bỏ hoang Jutsu-sen".
- **2704** (monologue): JP 「市内から術仙炭鉱には、送電線が伸びてきてなどいないのだから――」 — "mỏ than Jussen" → "mỏ than Jutsu-sen".
- **2753** (monologue): JP 「術仙炭鉱にかつてポジションを取っていて、そして今、エアクラ誘致賛成派の議員は確実にいる」 — "mỏ than Jussen" → "mỏ than Jutsu-sen" (giữ nguyên thẻ `%l` Aircra).

**A2. 御一夜 = "Ohitoyo" theo quyết định 19/11 của Hieu (11 dòng, gồm 4 lần tên cơ sở "Ohitoyo Mine Treasure").**
- **1851** (Hibiki): JP 「あ！　それいい！『おひとよマイントレジャー』」 — "『Ohimitera Mine Treasure』" → "『Ohitoyo Mine Treasure』".
- **1964** (Hibiki): JP 「私がエアクラ工場誘致に賛成してたのは、御一夜が元気になる方法が他に無いって思ってたから」 — "vực dậy Ohimitera" → "vực dậy Ohitoyo" (giữ nguyên thẻ `%l` Aircra).
- **1980** (Kisaki): JP 「『おひとよマイントレジャー』のことなら。面白い案だよね」 — "『Ohimitera Mine Treasure』" → "『Ohitoyo Mine Treasure』".
- **1983** (Kisaki): JP 「御一夜鉄道株式会社が事業主体となるのには、いくつかの問題がある」 — "Công ty Cổ phần Đường sắt Ohimitera" → "Công ty Cổ phần Đường sắt Ohitoyo". (Lưu ý: 株式会社 dịch "Công ty Cổ phần" là đúng — khác với 持株会社 ở Hachiroku 12 phải là "công ty holding" — chỉ sửa tên.)
- **2026** (Kisaki): JP 「御一夜鉄道のキャッシュじゃとても回らないよね」 — "Đường sắt Ohimitera" → "Đường sắt Ohitoyo".
- **2148** (Hibiki): JP 「この計画――おひとよマイントレジャーのこと。稀咲先輩にも、話してみてもいいですか？」 — "Ohimitera Mine Treasure" → "Ohitoyo Mine Treasure".
- **2182** (Paulette): JP 「なら――御一夜……マイントレジャー」 — "Ohimitera... Mine Treasure" → "Ohitoyo... Mine Treasure".
- **2186** (Soutetsu): JP 「ならば、施設名称はそれで行こう。『おひとよマイントレジャー』で」 — "『Ohimitera Mine Treasure』" → "『Ohitoyo Mine Treasure』".
- **2210** (Soutetsu): JP 「コールマイン。いいな――御一夜コールマイントレジャー……では、やや長いか」 — "Ohimitera Coal Mine Treasure" → "Ohitoyo Coal Mine Treasure".
- **2415** (monologue): JP 「マイントレジャー計画どころか、御一夜鉄道そのものが――」 — "Đường sắt Ohimitera" → "Đường sắt Ohitoyo".
- **1464** (Paulette): xem A1 — "Ở Ohimitera" → "Ở Ohitoyo".

### B. Xưng hô (4 dòng)
Quy ước docs (locations §2.1): Soutetsu xưng "Tôi" (chỉ dùng "Anh" khi nói với em gái Hibiki); Paulette xưng "Tôi"/"Em".
- **1718** (Paulette): JP 「ううん、違わないと思う。人間もレイルロオドも。揺れるのと揺れないの――強いのと弱いのがいるだけで」 — Paulette đang nói với Kisaki (cô gọi Kisaki "Cô Houshou" ở 1717 ngay trước đó) mà tự xưng "chị nghĩ" — trái docs và trái cách cô tự xưng "tôi" ở 8 chỗ khác trong file. Sửa thành "tôi nghĩ".
- **1873** (Soutetsu): JP 「うん、宝探し。小さなころ、僕が一番好きだった遊びだ」 — "Đó là trò chơi mà anh thích nhất hồi còn nhỏ" — Soutetsu nói với nhóm (Kisaki/Reina/Manami), không phải Hibiki. Sửa thành "mà tôi thích nhất hồi còn nhỏ".
- **1879** (Soutetsu): JP 「僕は、ふたごだったから。誕生日にも、クリスマスにも。プレゼントはいつでも、ふたつだった」 — "Vì anh là trẻ sinh đôi" — nói với Kisaki (cô đáp lại ở 1881), không phải Hibiki. Sửa thành "Vì tôi là trẻ sinh đôi".
- **2539** (monologue): JP 「それを形にしたいから、僕の"一番楽しい"を、そのままぶつける」 — độc thoại Soutetsu dùng "anh sẽ mang..." làm chủ ngữ — trái quy ước độc thoại "Tôi" của chính file (155 dòng độc thoại còn lại đều dùng "tôi"). Sửa thành "tôi sẽ mang...".

### C. Sai nghĩa (4 dòng)
- **2369** (monologue): JP 「だが、「と」の意味を持たせるためには、トレジャーの前に置くべき言葉が必要となる」 / TW 「但是，如果要讓"ｔｏ　Ｌｅｉｓｕｒｅ"這句話成立，就需要在前面加一個名詞」 — VN cũ dịch "to" thành "với": "để tạo ra ý nghĩa "với"" — sai: từ nối trong trò chơi chữ là "to" (Treasure **to** Leisure), không phải "với". Sửa thành "để tạo ra ý nghĩa "to"".
- **2836** (monologue): JP 「トレジャー、と、レジャー。単純極まるかけことばだが、意味的にも実にいい」 / TW 「Ｔｒｅａｓｕｒｅ、ｔｏ　Ｌｅｉｓｕｒｅ。雖然是一個很單純的雙關語，卻非常貼切」 — VN cũ "Treasure, **và** Leisure" — chữ "と" ở đây là từ "to" trong trò chơi chữ, không phải "và". Sửa thành "Treasure, to, Leisure."
- **2089** (Kisaki): JP 「期待をしても悪くなさそうだと教えてもらえた。キミに、だけじゃなくて――キミたちにだけどね」 / TW 「是你——不對，是你們讓我明白的」 — VN cũ "Không chỉ từ cô――mà là từ **các người** đấy" — "các người" mang sắc thái khinh miệt/xa cách trong tiếng Việt, trái hẳn giọng ấm áp biết ơn của Kisaki khi nói với Soutetsu và Paulette. Sửa thành "mà là từ mọi người đấy".
- **2533** (monologue): JP 「ならばまた鉄道債をと思いかけ、すぐさま自分の不明に気付く」 / TW 「我先是想到額外發行鐵路債券，但很快便發覺了自己的愚蠢」 — VN cũ "Tôi định **nói vậy thì** phát hành thêm trái phiếu đường sắt" — JP là 思いかけ ("chợt nghĩ tới"), không phải "nói"; câu Việt cũ gãy nghĩa ("định nói vậy thì phát hành..."). Sửa thành "Tôi vừa nghĩ đến việc phát hành thêm trái phiếu đường sắt, nhưng ngay lập tức nhận ra sự thiếu hiểu biết của mình."

### D. Lỗi nhỏ (1 dòng)
- **1934** (Fukami): JP 「宝探しの舞台だったら、あの暗いのもじめじめも、逆にいい、って思う。です」 — VN cũ "...ngược lại lại rất tuyệt, em nghĩ vậy. **ạ**" — chữ "ạ" rơi lẻ sau dấu chấm, thành một mảnh câu không gắn với câu nào (dấu lịch sự です của Fukami chưa được đưa vào câu). Sửa thành "...ngược lại lại rất tuyệt, em nghĩ vậy ạ."

## Các cặp trùng lặp / lệch vị trí đã xác nhận
- **0 cặp chuyển chỗ, 0 dòng mồ côi, 0 tràn chương.** Đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục): mọi câu Việt sai đều chỉ xuất hiện ở đúng key của chúng, không phải bản dịch đúng của key khác.
- **0 trùng lặp nội bộ sai:** file không có hai dòng nào trùng câu Việt mà JP khác nhau (1462 「…………」 trùng nhau ở cả ba ngôn ngữ nên không tính).
- **0 dòng Việt nào copy từ file khác:** các câu ngắn trùng với file khác (tiếng kêu, "Ừm.") đều đúng với JP của chính chúng.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- Soutetsu độc thoại xưng "Tôi" (155 dòng; chỉ 2539 xưng "anh"); Soutetsu thoại xưng "Tôi" trừ 1873, 1879 (sửa) và 2000 ("anh" — nói với Hibiki, đúng theo docs, không sửa); Soutetsu gọi Paulette "cô" (2047, ngữ cảnh công việc); Paulette xưng "Tôi" (8 dòng) trừ 1718; Paulette gọi Kisaki "Cô Houshou" (1717); Hibiki gọi Soutetsu "Anh trai" (qua lời Kisaki nhắc lại ở 1889).
- 御一夜 → **"Ohitoyo"** trong các bản sửa (quyết định 19/11 của Hieu); 御一夜鉄道 = "Đường sắt Ohitoyo" (1983, 2026, 2415); tên cơ sở おひとよマイントレジャー = "Ohitoyo Mine Treasure" (1851, 1980, 2148, 2186). Sau khi sửa, file này không còn "Ohimitera" nào.
- 術仙炭鉱 = **"mỏ than Jutsu-sen"** (có gạch nối, đủ chữ "t" — 6 dòng sửa; các dòng đúng sẵn có trong file cũng dùng "Jutsu-sen").
- エアクラ = **"Aircra"** (1903, 1964, 2753 — đúng sẵn có, không sửa); レイルロオド = **"Railord"** (1718, 1835 — đúng chính tả 1 chữ "l", không sửa); Olivy không xuất hiện trong file này.
- 帝鉄, 湯医, 冥国, 冥軍, 小畑, 大畑, コン không xuất hiện trong file này.
- Trò chơi chữ của chương: **Treasure "to" Leisure** — từ nối "to" giữ nguyên tiếng Anh trong bản sửa (2369, 2836); 2160 dịch đúng sẵn có ("chơi chữ với từ 'Leisure'").

## Đề xuất context mới
- **Soutetsu gọi Paulette "cô" hay "em"?** Trong file này Soutetsu gọi Paulette "cô" (2047, ngữ cảnh công việc — họp bàn kế hoạch với Kisaki), nhưng ở file 雪の宿 cùng chương 06 anh gọi cô "em" (1738, 1742, 2226, ngữ cảnh gia đình đi chơi). Hai cách đều nhất quán trong từng file, nên đây không tính là lỗi — nhưng cần Hieu chốt: phân biệt theo ngữ cảnh (công việc "cô" / gia đình "em") hay thống nhất một cách cho cả dự án. Nếu thống nhất "em", file này có 1 dòng cần đổi (2047); nếu phân biệt theo ngữ cảnh thì giữ nguyên cả hai.
- Không có đề xuất thuật ngữ mới nào khác từ file này.

## Khối TOML sửa (25 dòng — đã kiểm tra parse bằng tomllib, đúng 25/25 key, giá trị khớp JSON)
```toml
1464 = "「……Những người đã giữ vị thế đối với mỏ than Jutsu-sen――Ở Ohitoyo có rất nhiều」"
1718 = "「Không đâu, tôi nghĩ là không khác đâu. Cả con người và \\x%lレイルロオド;#00ffc040;Railord%l;#;. Chỉ là có người dao động và người không dao động――có người mạnh mẽ và người yếu đuối thôi」"
1765 = "「Tóm lại là, sẽ biến toàn bộ khu vực mỏ than bỏ hoang Jutsu-sen, thành một công viên chủ đề tìm kho báu đúng không」"
1851 = "「A! Thế được đó! 『Ohitoyo Mine Treasure』」"
1873 = "「Ừ, tìm kho báu. Đó là trò chơi mà tôi thích nhất hồi còn nhỏ.」"
1879 = "「Vì tôi là trẻ sinh đôi. Dù là sinh nhật hay Giáng sinh. Quà lúc nào cũng có hai món.」"
1934 = "「Nếu là bối cảnh tìm kho báu thì, sự tăm tối và ẩm ướt đó, ngược lại lại rất tuyệt, em nghĩ vậy ạ.」"
1964 = "「Việc em tán thành thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;, là vì em nghĩ không còn cách nào khác để vực dậy Ohitoyo」"
1974 = "「Điều tra lại mỏ than bỏ hoang Jutsu-sen. Tôi muốn Reina cũng đi cùng」"
1980 = "「Nếu là về 『Ohitoyo Mine Treasure』 thì rồi. Đó là một ý tưởng thú vị. Nếu coi nó như một câu chuyện」"
1983 = "「Đúng vậy, cô Paulette. Việc Công ty Cổ phần Đường sắt Ohitoyo trở thành chủ thể kinh doanh, có một vài vấn đề」"
2026 = "「Đúng thế. Nếu xảy ra một cuộc rút tiền ồ ạt, thì tiền mặt của Đường sắt Ohitoyo sẽ không thể nào xoay vòng nổi」"
2089 = "「Tôi đã biết được rằng có kỳ vọng một chút cũng không sao. Không chỉ từ cô――mà là từ mọi người đấy」"
2148 = "「Kế hoạch này――chuyện về Ohitoyo Mine Treasure ấy. Em thử nói chuyện với chị Kisaki có được không?」"
2155 = "「Ra vậy――đúng rồi nhỉ. Vì mỏ than bỏ hoang Jutsu-sen là đất thuộc sở hữu của thành phố mà」"
2182 = "「Nếu vậy――Ohitoyo... Mine Treasure」"
2186 = "「Nếu vậy, tên cơ sở cứ quyết định thế đi. Là 『Ohitoyo Mine Treasure』」"
2210 = "「Coal Mine. Hay đấy――Ohitoyo Coal Mine Treasure... thì hơi dài nhỉ」"
2369 = "Nhưng mà, để tạo ra ý nghĩa \"to\", thì cần phải có một từ đặt trước Treasure."
2415 = "Đừng nói là kế hoạch Mine Treasure, mà chính bản thân Đường sắt Ohitoyo cũng sẽ――"
2533 = "Tôi vừa nghĩ đến việc phát hành thêm trái phiếu đường sắt, nhưng ngay lập tức nhận ra sự thiếu hiểu biết của mình."
2539 = "Vì muốn biến điều đó thành hiện thực, tôi sẽ mang \"niềm vui lớn nhất\" của mình vào đó."
2704 = "Và từ thành phố đến mỏ than Jutsu-sen, không hề có đường dây điện nào kéo tới cả nên――"
2753 = "Những nghị viên từng giữ vị thế đối với mỏ than Jutsu-sen, và hiện tại thuộc phe ủng hộ thu hút \\x%lエアクラ;#00ffc040;Aircra%l;#;, chắc chắn là có."
2836 = "Treasure, to, Leisure. Một cách chơi chữ cực kỳ đơn giản, nhưng về mặt ý nghĩa cũng rất tuyệt."
```

## Kết bài
Paulette 06_おひとよマイントレジャー là file thứ mười lăm được audit toàn bộ (25/367 = 6,8% sai): một file sạch về cấu trúc — 0 dòng lệch vị trí, 0 dòng mồ côi, 0 tràn chương — nhưng mang nhiều lỗi thuật ngữ nhất theo tỷ lệ trong các file sạch (16/25 dòng là "Jussen" và "Ohimitera" theo quy ước cũ). Trừ 16 dòng thuật ngữ đó, file chỉ còn 9 lỗi thực chất (2,5%), tập trung ở xưng hô Soutetsu ("anh" thay vì "Tôi") và cặp chơi chữ "Treasure to Leisure" bị dịch mất từ nối "to". File này cũng là bằng chứng rõ nhất rằng hai file cùng một chương có thể khác nhau hoàn toàn về bản chất lỗi: file tuyết cùng chương 06 (xem audit kế tiếp) sạch hơn về thuật ngữ nhưng lại nặng về xưng hô.

Việc còn lại của riêng file này là áp dụng khối TOML 25 dòng và chơi thử chương để nghiệm thu. Tổng 15 file đã audit: 1.498 dòng sai. Còn một câu hỏi mở từ file này: Soutetsu gọi Paulette "cô" hay "em" — chờ Hieu chốt (xem mục Đề xuất context mới).
