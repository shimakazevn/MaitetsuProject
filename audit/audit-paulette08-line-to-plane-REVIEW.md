# Audit: Paulette 08_線から面へ — 27 dòng Việt sai (đã đối chiếu JP + TW)

**Kết quả: 27/387 dòng sai (7,0%)** — 0 lệch vị trí, 0 chưa dịch, 0 cụt câu, 0 chưa chắc chắn. File sạch về cấu trúc (không có dòng nào mang bản dịch của dòng khác), nhưng là file đa dạng lỗi nhất trong hai file Paulette 08: thuật ngữ 御一夜 (11 dòng), xưng hô Soutetsu trong cả thoại lẫn độc thoại (5 dòng), nghĩa (8 dòng), định dạng (1 dòng) và một thuật ngữ 端的. Đây là file Paulette 08 thứ hai (cảnh lập kế hoạch tour "từ đường thành mặt": tuyến xuôi dòng sông Kuma + đường sắt + Mine Treasure; Soutetsu, Paulette, Hachiroku, Nagi, Fukami, Mayami, du khách).

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 387 dòng script** (thoại 213, lời dẫn 174) đối chiếu JP + TW từ CSV "Trang tính 3", target là TOML-2. TW chỉ là nhân chứng thứ hai; chỗ nào JP và TW mâu thuẫn thì theo JP (quy tắc Hieu đặt 19/11).
- Heuristic thoại↔lời dẫn báo **1 dòng** (2433 — dấu 「 thừa) — bắt được 1/26. Toàn bộ lỗi còn lại đều là cùng-loại (xưng hô, thuật ngữ, nghĩa) nên heuristic không thấy được; thêm một bằng chứng nữa rằng heuristic chỉ là cận dưới.
- Không có key-shift sạch (shift −5..+5 đều ~1,000 — không có ý nghĩa vì key thưa và lỗi không phải lệch vị trí, không áp dụng).
- TOML và CSV giống hệt nhau về nội dung (234 dòng khác chỉ ở `\n`/khoảng trắng, 0 khác nội dung). Không có dòng CSV trống nào; VN==TW 0 dòng.
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Thẻ `%l`: 20 dòng có thẻ, không dòng nào lệch thẻ (1742, 1744, 2413 giữ nguyên thẻ, chỉ đổi gloss/nội dung).
- Phân loại lỗi: thuật ngữ 13 dòng (御一夜 11, Jussen 1, 端的 1), xưng hô 5 dòng (thoại 2, độc thoại 3), nghĩa 8 dòng, định dạng 1 dòng; chưa chắc chắn 0 dòng. Theo người nói: Soutetsu 7, Paulette 4, lời dẫn 9, Hachiroku 2, Reina 2, Fukami 2, du khách B 1; Nagi 0, Mayami 0, Hibiki 0.
- Về xưng hô Soutetsu trong thoại: quét toàn bộ file bằng máy — "anh" tự xưng 2 lần (1407, 1620 — đều sai, đều nói với du khách A, người lạ), "tôi" 14 lần, "em" ngôi hai 3 lần (1534 với Paulette, 1608 và 1769 với Nagi — đều đúng cách gọi, không phải tự xưng). Khác với file 未来へのレール (13 lần tự xưng thân mật so với 1 lần "tôi"), file này "tôi" chiếm đa số — chỉ 2 lần "anh" lọt qua.
- Về "mình" trong độc thoại: file có 7 dòng lời dẫn chứa "mình" — 4 dòng đúng (1991 sở hữu cách "của riêng mình", 2011 phản thân cho Hachiroku, 2056 phản thân cho Nagi, 2375 sở hữu cách "của riêng mình"), **3 dòng sai** (2473, 2545, 2549 — "mình" làm chủ ngữ cho Soutetsu, trong khi quy ước của file là "Tôi"). Ba dòng này dễ sót khi đọc vì "mình" đọc rất tự nhiên trong tiếng Việt — chỉ quét bằng máy mới bắt đủ.
- Không có file trùng lặp: file này chỉ tồn tại ở 03_Paulette/ (đã kiểm tra danh sách file toàn dự án trong CSV; không có bản sao ở thư mục khác).

## Kết luận về cơ chế lỗi

Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương, không có trùng lặp nội bộ sai — đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.381 mục): mỗi dòng sai trong file này chỉ xuất hiện đúng 1 lần trong toàn dự án, tại chính key của nó. Cơ chế lỗi ở đây là **lỗi từng dòng rải rác, không theo một mẫu hệ thống duy nhất** — khác với file 未来へのレール (hệ thống "anh") hay 支線 (hệ thống "anh" 17/17). Các lỗi chia thành bốn nhóm nhỏ:

1. **Thuật ngữ 御一夜 = "Ohimitera" trong toàn bộ file** (11/11 lần, 0 lần "Ohitoyo") — trái quyết định 19/11. Đây là nhóm lỗi lớn nhất, sửa cơ học.
2. **Xưng hô Soutetsu** (5 dòng): 2 lần "anh" trong thoại với người lạ (1407, 1620) và 3 lần "mình" làm chủ ngữ trong độc thoại (2473, 2545, 2549) — đều trái quy ước "Tôi" của file/docs.
3. **Nghĩa (7 dòng)** — đáng chú ý nhất là 2 dòng theo TW sai thay vì JP: 1633 (TW đọc 過去形 thành "đã chiến thắng") và 1414 (TW đọc thể bị động thành chủ động). Hai dòng này là minh chứng trực tiếp cho quy tắc JP-trên-TW mà Hieu đặt ra. 3 dòng thêm từ xưng hô "chị" không có trong JP (1398, 1662, 1735) — người dịch tự thêm cách gọi, cả ba đều sai người nhận.
4. **Định dạng + thuật ngữ lẻ** (2433 dấu 「 thừa, 2452 端的 dịch sai).

## Chi tiết 26 dòng sai

### A. Thuật ngữ theo quyết định mới — 御一夜 = "Ohitoyo" (11 dòng)

**1087 [観光客Ｂ]** — 御一夜 = "Ohitoyo" (quyết định 19/11; JP có furigana おひとよ trên 御一夜 — thêm một bằng chứng cho "Ohitoyo"). Bản cũ "Ohimitera".

- JP: 「……はぁぁ。\n[おひとよ,2]御一夜じゃ、こげーな虹さ、よう見れっぺか？」
- TW: 「……哈——在御一夜經常能看到這樣的彩虹嗎？」
- Cũ: 「...Hàà.\nỞ Ohimitera, thường thấy cầu vồng thế này lắm hả?」
- Sửa: 「...Hàà. Ở Ohitoyo, thường thấy cầu vồng thế này lắm hả?」

**1331 [れいな]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 「御一夜に戻るんじゃないんですかぁ？」
- TW: 「不是回御一夜嗎？」
- Cũ: 「Không phải quay lại Ohimitera sao ạ?」
- Sửa: 「Không phải quay lại Ohitoyo sao ạ?」

**1654 [ポーレット]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 「です。御一夜までの戻りは無人の回送車輌になるから、\n安全面のリスクも極限までさげられますし」
- TW: 「是的。因為返回御一夜的這段路是無人的空車，安全風險也能夠降到最低」
- Cũ: 「Vâng ạ. Chuyến về Ohimitera sẽ là chuyến xe trống không có khách,\nnên rủi ro về mặt an toàn cũng sẽ được giảm xuống mức tối đa.」
- Sửa: 「Vâng ạ. Chuyến về Ohitoyo sẽ là chuyến xe trống không có khách, nên rủi ro về mặt an toàn cũng sẽ được giảm xuống mức tối đa.」

**1670 [双鉄]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 「そのとおり、\nそこからは川下りで御一夜までを移動してもらう」
- TW: 「沒錯，讓遊客在那裡乘坐漂流船回到御一夜」
- Cũ: 「Đúng vậy,\ntừ đó sẽ cho họ đi thuyền xuôi dòng về Ohimitera.」
- Sửa: 「Đúng vậy, từ đó sẽ cho họ đi thuyền xuôi dòng về Ohitoyo.」

**1705 [ふかみ]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 「鉱山妖精は水を渡れないから、\n川下り船、御一夜までの脱出のお役にたつ。です」
- TW: 「礦山精靈不能過河。所以遊客們可以乘坐漂流船撤離至御一夜。嗯」
- Cũ: 「Tinh linh mỏ quặng không thể qua nước được,\nnên thuyền xuôi dòng sẽ có ích cho việc trốn thoát đến Ohimitera. Ạ.」
- Sửa: 「Tinh linh mỏ quặng không thể qua nước được, nên thuyền xuôi dòng sẽ có ích cho việc trốn thoát đến Ohitoyo. Ạ.」

**1707 [ポーレット]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 「御一夜に到着できたら、そこで一旦ツアーはおしまい。\nそのあとは、双鉄くんが言ったとおりにオプションで」
- TW: 「等遊客到達御一夜，觀光暫時告一段落。接下來就按照雙鐵君所說的，讓遊客自己選擇」
- Cũ: 「Khi đến được Ohimitera, chuyến tham quan sẽ tạm thời kết thúc ở đó.\nSau đó, sẽ là các lựa chọn như anh Soutetsu đã nói.」
- Sửa: 「Khi đến được Ohitoyo, chuyến tham quan sẽ tạm thời kết thúc ở đó. Sau đó, sẽ là các lựa chọn như anh Soutetsu đã nói.」

**1742 [双鉄]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera". "Yui" giữ nguyên — quyết định 湯医 chưa chốt. Thẻ `%l` giữ nguyên.

- JP: 「\x%l8620;#00ffc040;8620%l;#;を走らせて、御一夜――湯医を往復するのか？」
- TW: 「讓\x%l8620;#00ffc040;８６２０%l;#;在御一夜與湯醫之間往返嗎？」
- Cũ: 「Cho \x%l8620;#00ffc040;8620%l;#; chạy khứ hồi giữa Ohimitera――và Yui sao?」
- Sửa: 「Cho \\x%l8620;#00ffc040;8620%l;#; chạy khứ hồi giữa Ohitoyo――và Yui sao?」

**2155 [monologue]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 『マイントレジャーという仕事場』が、\n御一夜市民、誰にも受け入れられるのならば。
- TW: 如果“煤探樂園”這一職場，能夠接納所有御一夜市民的話——
- Cũ: Nếu 『Nơi làm việc mang tên Mine Treasure』,\nđược tất cả người dân Ohimitera chấp nhận.
- Sửa: Nếu 『Nơi làm việc mang tên Mine Treasure』, được tất cả người dân Ohitoyo chấp nhận.

**2413 [monologue]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera". Thẻ `%l` giữ nguyên.

- JP: \x%l8620;#00ffc040;8620%l;#;に満員の\x%l客車;#00ffc040;客車%l;#;を引かせるには観光復権が必要で、\n現状、クマ川下りは御一夜観光の看板だ。
- TW: 若想讓\x%l8620;#00ffc040;８６２０%l;#;拖運滿員的\x%l客車;#00ffc040;客運車廂%l;#;，就必須先復興旅遊業。而目前來看，隈河漂流是御一夜旅遊業的招牌。
- Cũ: Để \x%l8620;#00ffc040;8620%l;#; có thể kéo \x%l客車;#00ffc040;toa hành khách%l;#; chật kín người thì việc phục hồi du lịch là cần thiết,\nvà hiện tại, tuyến xuôi dòng sông Kuma chính là bộ mặt của du lịch Ohimitera.
- Sửa: Để \\x%l8620;#00ffc040;8620%l;#; có thể kéo \\x%l客車;#00ffc040;toa hành khách%l;#; chật kín người thì việc phục hồi du lịch là cần thiết, và hiện tại, tuyến xuôi dòng sông Kuma chính là bộ mặt của du lịch Ohitoyo.

**2423 [monologue]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 御一夜を笑顔で満たすことこそ、\nポーレットの笑顔を呼ぶことなのだと。
- TW: 若能讓御一夜充滿歡笑，波萊特也一定會展露笑顏。
- Cũ: Làm cho Ohimitera ngập tràn nụ cười,\nchính là mang lại nụ cười cho Paulette.
- Sửa: Làm cho Ohitoyo ngập tràn nụ cười, chính là mang lại nụ cười cho Paulette.

**2424 [monologue]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: この反応――これを御一夜全市からもしも引き出せたなら、\n観光振興は必ず、成せる。
- TW: 若能讓御一夜全市做出這樣的反應，旅遊業復興必能成功。
- Cũ: Phản ứng này――nếu có thể khơi gợi được điều này từ toàn thành phố Ohimitera,\nthì việc chấn hưng du lịch chắc chắn sẽ thành công.
- Sửa: Phản ứng này――nếu có thể khơi gợi được điều này từ toàn thành phố Ohitoyo, thì việc chấn hưng du lịch chắc chắn sẽ thành công.

### B. Thuật ngữ khác (2 dòng)

**1744 [双鉄]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" thiếu chữ "t" (lỗi đã thấy ở Grand 04 và Paulette 06). Thẻ `%l` giữ nguyên.

- JP: 「術仙炭鉱廃駅と鉱山鉄道とを復活させ、\nまずは、その区間を\x%lキハ07;#00ffc040;キハ07%l;#;に案内してもらう」
- TW: 「讓術仙煤礦廢車站與礦山鐵路復活，然後先讓\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;來跑這一路段」
- Cũ: 「Phục sinh nhà ga bỏ hoang mỏ than Jussen và tuyến đường sắt mỏ,\ntrước tiên, hãy để \x%lキハ07;#00ffc040;KiHa 07%l;#; dẫn đường trong khu vực đó.」
- Sửa: 「Phục sinh nhà ga bỏ hoang mỏ than Jutsu-sen và tuyến đường sắt mỏ, trước tiên, hãy để \\x%lキハ07;#00ffc040;KiHa 07%l;#; dẫn đường trong khu vực đó.」

**2452 [monologue]** — 端的に = "Ngắn gọn" (ghi chú thuật ngữ từ Paulette 06, tuyết 2158/2159); bản cũ "Nói thẳng ra" (thẳng thắn) sai nghĩa — TW 說白了 cũng là "nói thẳng", nhưng JP 端的に là "ngắn gọn, tóm lại".

- JP: 端的に言って、起きようという気にならん。
- TW: 說白了，就是不想起床。
- Cũ: Nói thẳng ra là, chẳng có chút hứng thú nào để thức dậy cả.
- Sửa: Nói ngắn gọn thì, chẳng có chút hứng thú nào để thức dậy cả.

### C. Xưng hô — Soutetsu (5 dòng)

**1407 [双鉄]** — Soutetsu tự xưng "anh" với du khách A (người lạ); docs: "Tôi" ("Anh" chỉ với Hibiki).

- JP: 「無理を言うな。僕は現実しか見ん男だぞ」
- TW: 「別強人所難了。我可是一個只關心現實的男人」
- Cũ: 「Đừng làm khó anh. Anh là kiểu đàn ông chỉ nhìn vào thực tế thôi.」
- Sửa: 「Đừng làm khó tôi. Tôi là kiểu đàn ông chỉ nhìn vào thực tế thôi.」

**1620 [双鉄]** — Soutetsu tự xưng "Anh" với du khách A; docs: "Tôi".

- JP: 「すまん。気合を入れなおしていた」
- TW: 「抱歉。我在給自己打氣呢」
- Cũ: 「Xin lỗi. Anh đang lấy lại tinh thần.」
- Sửa: 「Xin lỗi. Tôi đang lấy lại tinh thần.」

**2473 [monologue]** — Độc thoại Soutetsu dùng "mình" làm chủ ngữ; quy ước của file là "Tôi" (mọi dòng độc thoại khác đều dùng "tôi"). Dòng này dễ sót khi đọc vì "mình" đọc rất tự nhiên — chỉ quét bằng máy mới bắt đủ.

- JP: 絵本の中に紛れ込んでしまったかと思うほど――\nその光景は幻想的で、ごく単純に美しい。
- TW: 這一幅奇幻的畫面，單純而美麗。叫人不禁懷疑——是否闖入了童話的世界。
- Cũ: Cứ ngỡ như mình đã lạc vào trong một cuốn truyện tranh――\nKhung cảnh ấy thật huyền ảo, và đẹp đẽ một cách thuần túy.
- Sửa: Cứ ngỡ như tôi đã lạc vào trong một cuốn truyện tranh―― Khung cảnh ấy thật huyền ảo, và đẹp đẽ một cách thuần túy.

**2545 [monologue]** — Độc thoại Soutetsu dùng "mình" làm chủ ngữ ("những việc mình có thể làm"); quy ước của file là "Tôi". Thành ngữ "Dốc hết sức mình" giữ nguyên (đúng tiếng Việt, tiền lệ 未来へのレール 2968 "hết sức mình").

- JP: （僕にも、まだまだあるはずだ。\nポーレットのため、僕の力を尽くせることが）
- TW: （我也一定，還能為波萊特做些什麼）
- Cũ: （Chắc chắn vẫn còn những việc mình có thể làm.\nDốc hết sức mình vì Paulette.）
- Sửa: （Chắc chắn tôi vẫn còn những việc có thể làm. Dốc hết sức mình vì Paulette.）

**2549 [monologue]** — Độc thoại Soutetsu dùng "Mình" làm chủ ngữ; quy ước của file là "Tôi".

- JP: （体力には、いささかの自信があったのだが――）
- TW: （我原本對體力還有點自信的——）
- Cũ: （Mình vốn cũng khá tự tin vào thể lực của bản thân cơ mà――）
- Sửa: （Tôi vốn cũng khá tự tin vào thể lực của bản thân cơ mà――）

### D. Nghĩa (7 dòng)

**1095 [双鉄]** — Bản cũ thêm vế "Từ điểm nối thành đường" không có trong JP/TW. JP chỉ nói "từ đường thành mặt".

- JP: 「……線から面、だな」
- TW: 「……線連成了麵啊」
- Cũ: 「...Từ điểm nối thành đường, rồi mở rộng thành mặt nhỉ.」
- Sửa: 「……Từ đường thành mặt, nhỉ.」

**1398 [双鉄]** — Soutetsu hỏi Paulette (bạn đối thoại ở 1391–1392); gọi cô ấy là "chị" là sai — anh gọi Paulette là "em" (xem 1534) hoặc "cô". Dù người nghe có là Hachiroku thì "chị" cũng sai (anh gọi Hachiroku là "em"). Sửa thành "em" — đúng cho cả hai trường hợp có thể.

- JP: 「いくらか、とは」
- TW: 「具體是指？」
- Cũ: 「Vài chuyện, là gì vậy chị?」
- Sửa: 「Vài chuyện, là gì vậy em?」

**1414 [れいな]** — JP お任せされちゃいます là thể bị động: Reina ĐÃ được giao việc (tự xưng ngôi ba); bản cũ theo TW 「包在玲奈身上」 ("giao cho Reina đi") thành "xin nhận nhiệm vụ" — đảo chiều câu: biến người đã được giao thành người đang được nhờ nhận.

- JP: 「れいな、お任せされちゃいますよぉ」
- TW: 「包在玲奈身上吧」
- Cũ: 「Reina, xin nhận nhiệm vụ đó nha~」
- Sửa: 「Reina được giao việc đó rồi nha~」

**1598 [ふかみ]** — JP 絡みたい = "muốn tham gia/dính vào"; bản cũ "kết hợp" (combine) sai nghĩa. TW 「我也希望」 mơ hồ, không giúp — theo JP.

- JP: 「絡みたい！　です」
- TW: 「我也希望！嗯」
- Cũ: 「Em muốn kết hợp! Ạ.」
- Sửa: 「Em cũng muốn tham gia! Ạ.」

**1633 [ハチロク]** — JP 過去形 = "thì quá khứ" (thuật ngữ ngữ pháp); TW đọc sai thành "đã chiến thắng" (打贏了) và bản cũ theo TW. Theo quy tắc JP-trên-TW (Hieu 19/11), dịch từ JP: Hachiroku đang đùa rằng giá mà chuyện cần mong đợi đã là chuyện của quá khứ (đã xong) thì tốt rồi.

- JP: 「過去形ならばよろしゅうございました。\n双鉄様にお客様です」
- TW: 「既然打贏了就好。雙鐵少爺，有您的客人」
- Cũ: 「Thì quá khứ nghĩa là ngài đã chiến thắng rồi nhỉ.\nCó khách tìm ngài Soutetsu ạ.」
- Sửa: 「Nếu đã là chuyện của quá khứ thì tốt rồi ạ. Có khách tìm ngài Soutetsu ạ.」

**1662 [ハチロク]** — Hachiroku hỏi Soutetsu (cô vừa đáp lời ngài ở 1658: "Vâng thưa ngài Soutetsu"); thêm "Chị" là sai — Hachiroku không bao giờ gọi ai là "chị" (cô dùng 様, xưng hô trang trọng: わたくし, ございます), và Soutetsu là nam. Bỏ "Chị", giữ lối nói trang trọng.

- JP: 「わたくしに、何か？」
- TW: 「有什麼事嗎？」
- Cũ: 「Chị có chuyện gì với tôi sao?」
- Sửa: 「Có chuyện gì với tôi sao ạ?」

**1735 [ポーレット]** — Paulette đồng ý với ý tưởng tinh linh — ý này là của Hachiroku (1417: "Nếu là tinh linh thì..."); Paulette gọi Hachiroku là "Hachiroku-chan", không gọi "chị". Sửa theo cách xưng hô đã có của Paulette với Hachiroku.

- JP: 「言われてみればそうですね。\nなら、妖精ってことでどうでしょう？」
- TW: 「要這麼說的話，確實沒有錯呢。那麼，改成精靈怎麼樣？」
- Cũ: 「Nghe chị nói mới thấy đúng thật.\nVậy, đổi thành tinh linh thì sao ạ?」
- Sửa: 「Nghe Hachiroku-chan nói mới thấy đúng thật. Vậy, đổi thành tinh linh thì sao ạ?」

### E. Định dạng (1 dòng)

**2433 [monologue]** — Lời dẫn không có 「」 trong JP; bản cũ thêm dấu 「 mở mà không có dấu 」 đóng (lỗi ngược với obasan 2664, vốn thiếu dấu 「 mở). Bỏ dấu 「 thừa.

- JP: 奥の部屋からの反応はない。\nそれはおそらく、ふかみの安心のあらわれと――
- TW: 裡屋沒有動靜。看來深美沒有不放心——
- Cũ: 「Không có phản ứng gì từ căn phòng bên trong.\nĐó có lẽ là biểu hiện cho sự an tâm của Fukami――」
- Sửa: Không có phản ứng gì từ căn phòng bên trong. Đó có lẽ là biểu hiện cho sự an tâm của Fukami――

## Các cặp trùng lặp / lệch vị trí đã xác nhận

**0 cặp.** Không có dòng nào bị lệch vị trí, không có chuỗi xoay vòng, không có dòng nào mang bản dịch của dòng khác (kiểm chứng bằng chỉ mục Việt toàn dự án: mỗi dòng sai chỉ xuất hiện đúng 1 lần, tại chính key của nó). Không có giá trị Việt trùng lặp nội bộ trong file (0 cặp trùng).

## Dòng đã chốt sau audit (1 dòng — chốt ngày 19/11 từ cột Character + ngữ cảnh, không cần chơi game)

**1597 [ポーレット] — ĐÃ CHỐT: người giao việc là Soutetsu → "anh", bản cũ "chị" SAI.** JP: 「わたし――頑張ります。\n安心して、任せていただけるように」 (TW: 「我——我會繼續努力的。好讓您能放心交給我」). Cột Character trong CSV ghi rõ người nói là ポーレット (Paulette); đoạn hội thoại 1591–1608 chỉ có Soutetsu, Hachiroku, Paulette, Fukami, Nagi — Mayami (真闇) chưa nói câu nào, nói lần đầu ở 1610, nên không phải người giao việc. Soutetsu mới là người giao việc: 1569 anh chỉ đạo cả nhóm chuẩn bị tốt nhất, 1613 anh nói đã nhờ người hỗ trợ, 1636 anh chào Paulette "Hôm nay tôi không thể làm thư ký cho cô được" — tức Paulette chạy tour, Soutetsu là người hỗ trợ cô. Paulette gọi Soutetsu là "anh" ở mọi chỗ (1602 "anh Soutetsu"), không bao giờ gọi "chị". Bản sửa: `1597 = "「Em――sẽ cố gắng ạ. Để anh có thể yên tâm giao phó cho em.」"` — đã đưa vào khối TOML. Bài học: cột Character + 3–5 dòng xung quanh giải quyết được người nói/người được nhắc tới — không để "không chắc chắn" khi bằng chứng đã có trong file. (Lỗi này do audit cũ để sót, Hieu chỉ ra ngày 19/11.)

## Ghi chú quan sát (không tính lỗi, không đưa vào khối TOML)

- **1085 [ハチロク]:** 凪様 → "Nagi" (bỏ mất kính ngữ 様). **1677 [ハチロク]:** ふかみ様 → "Fukami" (bỏ mất 様). Nghĩa vẫn đúng, chỉ mất sắc thái trang trọng trong lời Hachiroku — ghi nhận, không tính lỗi (tiền lệ các file trước không tính mất kính ngữ là lỗi).
- **"KiHa" vs "Kiha":** file này dùng "KiHa 07" trong gloss thẻ `%l` ở 6 dòng (1363, 1490, 1628, 1744, 1810, 2177) và trong câu ở 2836 của file 未来へのレール; các file trước dùng "Kiha 07" (tiền lệ 廃炭鉱). "KiHa" thực ra là cách viết chính thức của JR (KiHa 07) — không tính lỗi, nhưng nên thống nhất một dạng cho toàn dự án (đề xuất: giữ "KiHa" vì đúng chính thức, và sửa các file cũ theo sau — cần Hieu chốt).
- **1534 [双鉄] — bằng chứng cho quyết định đang chờ:** Soutetsu nói "Rất vinh hạnh được em khen" — gọi Paulette là "em" trong bối cảnh làm việc/lập kế hoạch (cô khen kế hoạch của anh). Đây là bằng chứng cho phía "em" trong quyết định Soutetsu gọi Paulette "cô" (công việc) hay "em" (gia đình) — xem mục đề xuất. Không tính lỗi.
- **湯医:** 3 dòng "Yui" trong file (1363, 1628, 1742) KHÔNG tính sai — chờ Hieu chốt Yui hay Yunoi rồi thống nhất toàn dự án.
- **Soutetsu gọi Paulette "cô" (giữ nguyên):** 1623, 1715, 1739 — đúng bối cảnh công việc, không sửa; đối chiếu với 1534 ("em") ở trên.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)

- 御一夜 → "Ohitoyo" trong các bản sửa (quyết định 19/11; sau khi sửa file không còn "Ohimitera" nào).
- 術仙炭鉱 → "mỏ than Jutsu-sen" (sửa "Jussen").
- 端的 → "Ngắn gọn" (ghi chú thuật ngữ từ Paulette 06).
- 共感 → "cộng cảm" ở 1524 (liên kết Railord) — đúng, giữ nguyên.
- 湯医 → "Yui" giữ nguyên trong các dòng đúng (quyết định chưa chốt — xem trên).
- 冥軍, 冥国, 小畑, コン, 駿袋鉄道, 整備体/運転ボディ, 帝鉄 không xuất hiện trong file này.
- Soutetsu gọi Nagi bằng "em" (ngôi hai, đúng — 1608, 1769); gọi Paulette bằng "em" ở 1534 và "cô" ở 1623/1715/1739 (xem đề xuất).

## Đề xuất cập nhật context (chưa quyết định — cần Hieu chốt)

1. **Soutetsu gọi Paulette "cô" hay "em" — thêm bằng chứng cho phía "em" (key 1534):** Trong file này Soutetsu gọi Paulette là "em" ngay trong bối cảnh làm việc/lập kế hoạch tour ("Rất vinh hạnh được em khen"), trong khi ở 1623/1715/1739 (cũng bối cảnh công việc) anh gọi cô là "cô". Nếu chia theo bối cảnh (công việc "cô", gia đình "em") thì 1534 là ngoại lệ; nếu thống nhất "em" thì 1623/1715/1739 cần đổi. Đề xuất: **thống nhất "em" cho mọi bối cảnh** (Paulette là vợ của Soutetsu; "cô" tạo cảm giác xa cách không hợp với quan hệ vợ chồng, và file này đã dùng "em" ngay cả khi bàn công việc). Nếu Hieu chốt "em", các dòng "cô" ở 1623/1715/1739 (và ở các file khác) sẽ cần đổi theo trong đợt thống nhất sau.
2. **"KiHa" vs "Kiha" (key 1744 và 5 dòng thẻ khác):** đề xuất thống nhất "KiHa" (cách viết chính thức của JR) cho toàn dự án; nếu chốt, các file cũ dùng "Kiha" sẽ cần đổi theo.

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)

Lưu ý khi chép: các bản sửa viết liền một dòng, không chèn `\n` thủ công — theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng. Khối này đã kiểm tra bằng máy: trích khối từ chính file review, parse bằng tomllib — **27/27 key** khớp đúng tập dòng sai, không thừa không thiếu, giá trị sau khi parse khớp đúng bản sửa.

```toml
1087 = "「...Hàà. Ở Ohitoyo, thường thấy cầu vồng thế này lắm hả?」"
1095 = "「……Từ đường thành mặt, nhỉ.」"
1331 = "「Không phải quay lại Ohitoyo sao ạ?」"
1398 = "「Vài chuyện, là gì vậy em?」"
1407 = "「Đừng làm khó tôi. Tôi là kiểu đàn ông chỉ nhìn vào thực tế thôi.」"
1414 = "「Reina được giao việc đó rồi nha~」"
1597 = "「Em――sẽ cố gắng ạ. Để anh có thể yên tâm giao phó cho em.」"
1598 = "「Em cũng muốn tham gia! Ạ.」"
1620 = "「Xin lỗi. Tôi đang lấy lại tinh thần.」"
1633 = "「Nếu đã là chuyện của quá khứ thì tốt rồi ạ. Có khách tìm ngài Soutetsu ạ.」"
1654 = "「Vâng ạ. Chuyến về Ohitoyo sẽ là chuyến xe trống không có khách, nên rủi ro về mặt an toàn cũng sẽ được giảm xuống mức tối đa.」"
1662 = "「Có chuyện gì với tôi sao ạ?」"
1670 = "「Đúng vậy, từ đó sẽ cho họ đi thuyền xuôi dòng về Ohitoyo.」"
1705 = "「Tinh linh mỏ quặng không thể qua nước được, nên thuyền xuôi dòng sẽ có ích cho việc trốn thoát đến Ohitoyo. Ạ.」"
1707 = "「Khi đến được Ohitoyo, chuyến tham quan sẽ tạm thời kết thúc ở đó. Sau đó, sẽ là các lựa chọn như anh Soutetsu đã nói.」"
1735 = "「Nghe Hachiroku-chan nói mới thấy đúng thật. Vậy, đổi thành tinh linh thì sao ạ?」"
1742 = "「Cho \\x%l8620;#00ffc040;8620%l;#; chạy khứ hồi giữa Ohitoyo――và Yui sao?」"
1744 = "「Phục sinh nhà ga bỏ hoang mỏ than Jutsu-sen và tuyến đường sắt mỏ, trước tiên, hãy để \\x%lキハ07;#00ffc040;KiHa 07%l;#; dẫn đường trong khu vực đó.」"
2155 = "Nếu 『Nơi làm việc mang tên Mine Treasure』, được tất cả người dân Ohitoyo chấp nhận."
2413 = "Để \\x%l8620;#00ffc040;8620%l;#; có thể kéo \\x%l客車;#00ffc040;toa hành khách%l;#; chật kín người thì việc phục hồi du lịch là cần thiết, và hiện tại, tuyến xuôi dòng sông Kuma chính là bộ mặt của du lịch Ohitoyo."
2423 = "Làm cho Ohitoyo ngập tràn nụ cười, chính là mang lại nụ cười cho Paulette."
2424 = "Phản ứng này――nếu có thể khơi gợi được điều này từ toàn thành phố Ohitoyo, thì việc chấn hưng du lịch chắc chắn sẽ thành công."
2433 = "Không có phản ứng gì từ căn phòng bên trong. Đó có lẽ là biểu hiện cho sự an tâm của Fukami――"
2452 = "Nói ngắn gọn thì, chẳng có chút hứng thú nào để thức dậy cả."
2473 = "Cứ ngỡ như tôi đã lạc vào trong một cuốn truyện tranh―― Khung cảnh ấy thật huyền ảo, và đẹp đẽ một cách thuần túy."
2545 = "（Chắc chắn tôi vẫn còn những việc có thể làm. Dốc hết sức mình vì Paulette.）"
2549 = "（Tôi vốn cũng khá tự tin vào thể lực của bản thân cơ mà――）"
```

## Việc tiếp theo

- Dòng 1597 đã chốt ngày 19/11 (người giao việc là Soutetsu → "anh", xem mục trên) và đã đưa vào khối TOML.
- Sau khi áp 27 bản sửa, file coi như xong, trừ việc chờ Hieu chốt các quyết định đang chờ (đặc biệt 湯医 Yui vs Yunoi — file này có 3 dòng "Yui"; và đề xuất thống nhất "em" cho Paulette + "KiHa" — xem trên).
- File Paulette 08 thứ nhất (未来へのレール) đã được kiểm tra riêng — xem `audit-paulette08-future-rail-REVIEW.md`.

## Kết bài

File 線から面へ là file đa dạng lỗi nhất trong hai file Paulette 08: không có một mẫu hệ thống duy nhất mà là lỗi rải rác ở bốn nhóm (thuật ngữ, xưng hô thoại, xưng hô độc thoại, nghĩa) cộng một lỗi định dạng. Điểm đáng chú ý nhất là hai dòng theo TW sai thay vì JP (1633, 1414) — đúng loại lỗi mà quy tắc JP-trên-TW của Hieu sinh ra để chặn — và ba dòng "mình" làm chủ ngữ trong độc thoại (2473, 2545, 2549) mà chỉ quét bằng máy mới bắt đủ, vì "mình" đọc quá tự nhiên trong tiếng Việt. Ngược với file 未来へのレール (Soutetsu tự xưng "anh"/"em" 13 lần so với "tôi" 1 lần), file này "tôi" chiếm đa số trong thoại của Soutetsu — chỉ 2 lần "anh" lọt qua, đều khi nói với người lạ. Sau khi áp 27 bản sửa, file coi như xong. Hai file Paulette 08 cùng nhau nâng tổng số dòng sai đã kiểm chứng toàn dự án lên **1.599 dòng trên 20 file** (1.550 + 22 + 27) — và một lần nữa cho thấy hai file cùng một chương có thể khác nhau hoàn toàn về bản chất lỗi, nên không thể đoán loại lỗi từ file bên cạnh.
