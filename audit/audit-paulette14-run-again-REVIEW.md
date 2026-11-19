# Audit: Paulette 14_ふたたび走り出すために — 32 dòng Việt sai (đã đối chiếu JP + TW)

**Kết quả: 32/376 dòng sai (8.5%)** — 0 lệch vị trí, 0 chưa dịch, 0 cụt câu, 0 chưa chắc chắn. Cảnh: chuẩn bị cơm hộp bento Kijiuma, tập lái cho Niiroku/Reina, Kisaki cảnh báo về Mototada, chuẩn bị đón bộ trưởng thị sát.

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 376 dòng script** (thoại 212: Soutetsu 72, Hibiki 32, Hachiroku 24, Paulette 17, Nagayama 15, Reina 14, Kisaki 10, Akai 9, Tororyu 8, Niiroku 6, Nagi 5; lời dẫn 164) đối chiếu JP + TW từ CSV "Trang tính 3", target là TOML-2. TW chỉ là nhân chứng thứ hai; chỗ nào JP và TW mâu thuẫn thì theo JP (quy tắc Hieu đặt 19/11).
- Heuristic thoại↔lời dẫn báo **0 dòng** — bắt được 0/32. Toàn bộ lỗi đều là cùng-loại (thuật ngữ, xưng hô, tiếng hít, nghĩa) nên heuristic không thấy được; thêm một bằng chứng nữa rằng heuristic chỉ là cận dưới.
- Không có key-shift sạch (shift 0: 376/376; các shift khác 128/128–166/166 — không có ý nghĩa vì key thưa và lỗi không phải lệch vị trí, không áp dụng).
- TOML và CSV giống hệt nhau về nội dung (229 dòng khác chỉ ở `\n`/khoảng trắng, 0 khác nội dung). Không có dòng CSV trống nào; VN==TW 0 dòng. `[selections]` rỗng (0 mục). Thẻ `%l`: 32 dòng có thẻ trong VN (JP có 30) — **0 thẻ thiếu dấu `;` đóng** (khác với Paulette 13: 5 thẻ thiếu `;`); 1 dòng VN có thẻ JP không có (1410 — thẻ gloss cho ruby [にい,1]/[いもうと,1] có sẵn trong JP, không phải bịa thêm).
- Phân loại lỗi: thuật ngữ 12 dòng (御一夜 10 — gồm 1733 mang cả hai lỗi; 術仙 1 "Jutsusen" thiếu gạch nối; 廃駅 1 "ga phế liệu"); xưng hô 18 dòng (Soutetsu tự xưng "anh" 17 dòng trong thoại + "Anh" 1 dòng trong độc thoại 2273); mất tiếng hít っ 2 dòng (1889, 1890); sai nghĩa 1 dòng (ぽわっと 2400). Tổng 12 + 18 + 2 + 1 = 33 lượt lỗi trên 32 dòng (1733 mang cả hai lỗi; trong JSON, 1733 xếp loại 'terminology' nên số mục theo loại là thuật ngữ 12, xưng hô 17, lỗi nhỏ 2, sai nghĩa 1 = 32 mục). Theo người nói: Soutetsu 21, lời dẫn 5, Hibiki 3, Hachiroku 2, đền chủ Akai 1. **Chưa chắc chắn 0 dòng.**
- Thoại sai 27/212 (12,7%), lời dẫn sai 5/164 (3,0%).
- Về xưng hô Soutetsu trong thoại: quét toàn bộ file bằng máy (đã chuẩn hoá `\n` thành khoảng trắng trước khi chạy regex `\b`, theo bài học Paulette 08) — "tôi/Tôi" 8 dòng, "anh/Anh" tự xưng **18 dòng** (17 dòng sai + 1549 là tiếng hít của Paulette trong câu tường thuật "cô ấy nghĩ anh…" — giữ nguyên, xem mục đã kiểm tra), "em" ngôi hai 13 lần (đều gọi người khác, đúng). "Mình" trong thoại trực tiếp: 0 dòng (1527 là ở Paulette 15, không phải file này).
- Về "mình" trong độc thoại: 8 dòng chứa "mình"/"Anh" — **7 dòng "mình" đều đúng** (sở hữu cách "của mình" 2084/2163, phản thân "tự mình" 2348, thành ngữ "một mình" 2205, suy nghĩ trích dẫn 2420, "cho mình tôi" 2424, "trong mình" 2079) và **1 dòng sai** (2273 "Anh" tự xưng — đã đưa vào danh sách). File này không có lỗi "mình" nào.
- Không có file trùng lặp: file này chỉ tồn tại ở 03_Paulette/ (đã kiểm tra tên trong cả 227 file TOML-2; các cặp trùng khác đều là file Grand Rewrite — không liên quan file này).

## Kết luận về cơ chế lỗi

Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương, không có dòng mồ côi — đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục): 29/32 dòng sai chỉ xuất hiện đúng 1 lần trong toàn dự án, tại chính key của nó. 3 ngoại lệ đều là chuỗi ngắn chung chung, không phải câu của dòng khác:

- **1657 ("「Anh á?」")**: cũng xuất hiện ở 日々姫01 2307 (JP 「僕がか？」) — đó là cùng một lỗi xưng hô "anh" ở file khác, không phải tràn chương. Ghi nhận để audit 日々姫01 sau này.
- **1889/1890 ("「!!?」")**: xuất hiện ở 85 chỗ trong toàn dự án — đều là cùng một lỗi hệ thống mất tiếng hít っ, không phải câu của dòng khác.

Cơ chế lỗi ở đây là **xưng hô hệ thống (18/32) + thuật ngữ chưa thống nhất (12/32)** — Soutetsu tự xưng "anh" trong 17/72 dòng thoại của mình (23,6%), gần như là một lựa chọn dịch nhất quán của người dịch file này (giống Paulette 07 支線: 17/17 "anh"), trái docs và trái quy ước của chính các file Paulette gần đây (Paulette 11: "anh" 0 lần; Paulette 12: "anh" 0 lần). Nếu trừ 12 dòng thuật ngữ và 18 dòng xưng hô, file chỉ còn 3 lỗi thực chất (0,8%) — ngang nhóm file sạch nhất.

## Chi tiết dòng sai

### Thuật ngữ

**1422 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「しかし議会は、マイントレジャーの方が御一夜の未来を\n託すのによりふさわしい計画だと――既に判断している」
- TW: 「但是市議會已經做出了決定——認為煤探樂園計劃才是更適合御一夜未來的計劃」
- Cũ: 「Nhưng hội đồng thành phố đã phán quyết rằng——kế hoạch Mine Treasure phù hợp để gửi gắm tương lai của Ohimitera hơn.」
- Sửa: 「Nhưng hội đồng thành phố đã phán quyết rằng——kế hoạch Mine Treasure phù hợp để gửi gắm tương lai của Ohitoyo hơn.」

**1508 [Hibiki]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「あ！　それいいかも！！\n鮎も、御一夜の超名物だし」
- TW: 「啊！　這個不錯！！香魚也是御一夜的一大特色」
- Cũ: 「A! Ý đó có vẻ hay đấy!! Cá hương cũng là siêu đặc sản của Ohimitera mà.」
- Sửa: 「A! Ý đó có vẻ hay đấy!! Cá hương cũng là siêu đặc sản của Ohitoyo mà.」

**1560 [Hibiki]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「すごい、ぜんぶ御一夜の特産！」
- TW: 「好厲害，這些都是御一夜的特產！」
- Cũ: 「Tuyệt quá, toàn là đặc sản của Ohimitera không à!」
- Sửa: 「Tuyệt quá, toàn là đặc sản của Ohitoyo không à!」

**1584 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「宝生稀咲――隈元銀行御一夜支店長です」
- TW: 「寶生稀咲——隈元銀行御一夜支行長」
- Cũ: 「Houshou Kisaki——Giám đốc chi nhánh Ohimitera của ngân hàng Kumamoto.」
- Sửa: 「Houshou Kisaki——Giám đốc chi nhánh Ohitoyo của ngân hàng Kumamoto.」

**1683 [Hibiki]** — 廃駅 = "ga bỏ hoang" — toàn dự án dùng "ga bỏ hoang" (20+ chỗ, vd. "Ga bỏ hoang Kawamura", "Ga bỏ hoang Ichibu"); "ga phế liệu" là cách dịch duy nhất kiểu này trong toàn dự án.

- JP: 「新[つるは,1]弦羽廃駅、通過、良し！」
- TW: 「新鶴羽廢車站，通過，正常！」
- Cũ: 「Ga phế liệu Tsuruha mới, đi qua, tốt!」
- Sửa: 「Ga bỏ hoang Tsuruha mới, đi qua, tốt!」

**1723 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「はい。そうなります。\nその方々が、御一夜への視察を予定しておられると」
- TW: 「是的。聽說他們計劃來御一夜視察」
- Cũ: 「Vâng. Đúng là vậy. Những vị đó, dự định sẽ đến thị sát Ohimitera.」
- Sửa: 「Vâng. Đúng là vậy. Những vị đó, dự định sẽ đến thị sát Ohitoyo.」

**1733 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11) + Soutetsu tự xưng "anh" — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). Dòng duy nhất mang cả hai lỗi.

- JP: 「うむ。観光振興の、重要な一助となろうかと考え、\n『御一夜市らしい駅弁』の開発をお願いしているのだ」
- TW: 「沒錯。我認為這是旅遊復興計劃重要的一環，因此拜託永山女士開發出一款具有御一夜特色的鐵路便當」
- Cũ: 「Ừm. Anh nghĩ nó sẽ là một trợ thủ đắc lực cho việc chấn hưng du lịch, nên đang nhờ cô ấy phát triển một loại 『Cơm hộp bento nhà ga mang đậm chất Ohimitera』.」
- Sửa: 「Ừm. Tôi nghĩ nó sẽ là một trợ thủ đắc lực cho việc chấn hưng du lịch, nên đang nhờ cô ấy phát triển một loại 『Cơm hộp bento nhà ga mang đậm chất Ohitoyo』.」

**1814 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「予定は、予定だ。来月十日にお二方揃って、\n御一夜への視察を“予定”しておられるそうだ」
- TW: 「計劃就是計劃。他們“計劃”在下個月１０號一起來御一夜視察」
- Cũ: 「Dự định là, dự định đó. Nghe nói hai vị đó cùng nhau “dự định” sẽ đến thị sát Ohimitera vào mùng 10 tháng sau.」
- Sửa: 「Dự định là, dự định đó. Nghe nói hai vị đó cùng nhau “dự định” sẽ đến thị sát Ohitoyo vào mùng 10 tháng sau.」

**1878 [Hachiroku]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「マイントレジャー計画を。御一夜が、わたくしたちが、\n目指す未来を。双鉄様がまっすぐにお示し下さったから」
- TW: 「雙鐵少爺想出了煤探樂園計劃，為御一夜還有我們指明了前進的方向」
- Cũ: 「Kế hoạch Mine Treasure. Tương lai mà Ohimitera, mà chúng ta đang hướng tới. Ngài Soutetsu đã vạch ra con đường thẳng tắp đó.」
- Sửa: 「Kế hoạch Mine Treasure. Tương lai mà Ohitoyo, mà chúng ta đang hướng tới. Ngài Soutetsu đã vạch ra con đường thẳng tắp đó.」

**2123 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 変わった所では鮎寿司なども、\n御一夜では普通に食べられている。
- TW: 其中某些人家甚至還會把香魚做成壽司。
- Cũ: Thậm chí những món độc lạ như sushi cá hương, cũng được ăn rất bình thường ở Ohimitera.
- Sửa: 「Thậm chí những món độc lạ như sushi cá hương, cũng được ăn rất bình thường ở Ohitoyo.」

**2135 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 最初は、御一夜の町と環境とを守るため。\nその上に、ハチロクを再び走らせることが加わって――
- TW: 原本是為了守護御一夜的環境與城鎮。後來，我又希望八六能再次奔跑於鐵軌之上——
- Cũ: Ban đầu, là để bảo vệ thị trấn Ohimitera và môi trường. Thêm vào đó là việc muốn để Hachiroku được chạy một lần nữa——
- Sửa: 「Ban đầu, là để bảo vệ thị trấn Ohitoyo và môi trường. Thêm vào đó là việc muốn để Hachiroku được chạy một lần nữa——」

**2462 [lời dẫn]** — 術仙炭鉱 = "mỏ than Jutsu-sen" (thiếu gạch nối: bản cũ "Jutsusen").

- JP: 術仙炭鉱の技術継承炭鉱の認可。\n赤井阿蘇神社の文化財指定。
- TW: 術仙煤礦的技術繼承煤礦認定，以及赤井阿蘇神社的文化財產指定。
- Cũ: Công nhận mỏ than Jutsusen là mỏ than kế thừa kỹ thuật. Chỉ định đền Akai Aso là tài sản văn hóa.
- Sửa: 「Công nhận mỏ than Jutsu-sen là mỏ than kế thừa kỹ thuật. Chỉ định đền Akai Aso là tài sản văn hóa.」

### Xưng hô

**1386 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Niiroku (Reina được nhắc ở ngôi ba: "Giống hệt như Reina bây giờ") — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). "Em" gọi Niiroku giữ nguyên.

- JP: 「変わらず接する。\n今のれいなと、おんなじに」
- TW: 「不管玲奈變成什麼樣，我都會像現在這樣同玲奈相處的」
- Cũ: 「Anh vẫn sẽ đối xử với em như vậy. Giống hệt như Reina bây giờ.」
- Sửa: 「Tôi vẫn sẽ đối xử với em như vậy. Giống hệt như Reina bây giờ.」

**1424 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Paulette/nhóm — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「しかし、今のポーレットとならば大丈夫だと考えた。\n今の僕らなら、支えあい、よりよい判断を下せると」
- TW: 「但是我認為，現在的我們已經能夠坦然面對這件事。我們可以互相扶持，做出最好的判斷」
- Cũ: 「Nhưng anh nghĩ, nếu là Paulette hiện tại thì sẽ không sao cả. Nếu là chúng ta bây giờ, có thể hỗ trợ lẫn nhau và đưa ra phán đoán tốt hơn.」
- Sửa: 「Nhưng tôi nghĩ, nếu là Paulette hiện tại thì sẽ không sao cả. Nếu là chúng ta bây giờ, có thể hỗ trợ lẫn nhau và đưa ra phán đoán tốt hơn.」

**1514 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Hachiroku (1512–1513 Hachiroku nói, 1517 Hachiroku đáp lại) — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「う、うむ。\n言われずとも行ってくる」
- TW: 「嗯、嗯。你不說我也會走的」
- Cũ: 「Ừ, ừm. Em không nói thì anh cũng đi mà.」
- Sửa: 「Ừ, ừm. Em không nói thì tôi cũng đi mà.」

**1519 [Soutetsu]** — Soutetsu tự xưng "anh" trong cuộc họp nhóm (người nói trước/sau là Hachiroku, Kisaki — không phải Hibiki) — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「うん。僕としては大賛成だ。無論、\nポーレットたちの意見も聞かねばなるまいが」
- TW: 「嗯。我是很喜歡這個設計。當然還要問一下波萊特她們的意見」
- Cũ: 「Ừ. Về phần anh thì cực kỳ tán thành. Tất nhiên, cũng phải hỏi ý kiến của nhóm Paulette nữa.」
- Sửa: 「Ừ. Về phần tôi thì cực kỳ tán thành. Tất nhiên, cũng phải hỏi ý kiến của nhóm Paulette nữa.」

**1544 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với nhóm (1546 Nagi đáp lại) — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「大部分は、ポーレットに任せておけるからな。\n僕は、その隙間を埋めればいいだけだ」
- TW: 「大部分都是波萊特在處理。我只需要為她鋪平道路就好」
- Cũ: 「Vì phần lớn công việc, anh đều có thể giao cho Paulette mà. Anh chỉ cần lấp đầy những khoảng trống đó thôi.」
- Sửa: 「Vì phần lớn công việc, tôi đều có thể giao cho Paulette mà. Tôi chỉ cần lấp đầy những khoảng trống đó thôi.」

**1571 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Paulette — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「以前のポーレットにであれば、\nもう少し、慎重に伝えていたかもしれん」
- TW: 「如果你還是以前的那個波萊特，我或許會更加慎重地轉達吧」
- Cũ: 「Nếu là Paulette trước đây, có lẽ anh đã truyền đạt một cách thận trọng hơn một chút.」
- Sửa: 「Nếu là Paulette trước đây, có lẽ tôi đã truyền đạt một cách thận trọng hơn một chút.」

**1617 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Niiroku/nhóm (1613 Niiroku nói, 1614 Soutetsu) — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「僕は、責任を果たせたのか」
- TW: 「我……已經完成任務了嗎」
- Cũ: 「Anh, đã hoàn thành trách nhiệm rồi sao.」
- Sửa: 「Tôi, đã hoàn thành trách nhiệm rồi sao.」

**1622 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với ông chủ Tororyu-yu (1619 ông chủ nói) — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「僕の力もなにも――」
- TW: 「我什麼也沒——」
- Cũ: 「Sức mạnh của anh thì có gì——」
- Sửa: 「Sức mạnh của tôi thì có gì——」

**1628 [Soutetsu]** — Soutetsu tự xưng "anh" ×2 khi nói với nhóm — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「その都度必死で、目の前のことに向き合っていただけだ。\nあるいは僕が一番、先を見通せてなかったのかもしれん」
- TW: 「我只是一次次拚命努力去面對眼前的難關而已。說不定，我才是最沒有遠見的人」
- Cũ: 「Mỗi lần như vậy, anh chỉ liều mạng đối mặt với những thứ trước mắt thôi. Có lẽ anh mới là người không nhìn thấu được tương lai nhất cũng nên.」
- Sửa: 「Mỗi lần như vậy, tôi chỉ liều mạng đối mặt với những thứ trước mắt thôi. Có lẽ tôi mới là người không nhìn thấu được tương lai nhất cũng nên.」

**1644 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Hachiroku (1642 Hachiroku nói, 1646 Hachiroku đáp) — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「僕は……レールか」
- TW: 「我是……鐵軌」
- Cũ: 「Anh là……đường ray sao.」
- Sửa: 「Tôi là……đường ray sao.」

**1647 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Hachiroku + Nagi ("君たち") — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). "Các em" giữ nguyên.

- JP: 「ベストを尽くす。\n君たちが再び、心置きなく走り出せるようにも」
- TW: 「我會盡全力的。這樣也能讓你們心無掛礙地再次出發」
- Cũ: 「Anh sẽ cố gắng hết sức. Để các em có thể một lần nữa, chạy đi mà không chút vướng bận.」
- Sửa: 「Tôi sẽ cố gắng hết sức. Để các em có thể một lần nữa, chạy đi mà không chút vướng bận.」

**1653 [Soutetsu]** — Soutetsu tự xưng "anh" ×2 khi nói với nhóm — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「蓑笠さんのところにもご相談だ。\n職人まわりを、できる限りまとめていただきたいのでな」
- TW: 「我要去找蓑笠先生談談，得請他儘快跟工匠們談妥」
- Cũ: 「Anh đi bàn bạc với ông Minokasa. Anh muốn nhờ ông ấy tập hợp các thợ thủ công lại càng sớm càng tốt.」
- Sửa: 「Tôi đi bàn bạc với ông Minokasa. Tôi muốn nhờ ông ấy tập hợp các thợ thủ công lại càng sớm càng tốt.」

**1655 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với nhóm — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「これは――いけそうな気がするな」
- TW: 「我覺得——這個可以啊」
- Cũ: 「Cái này——anh có linh cảm là sẽ thành công đấy.」
- Sửa: 「Cái này——tôi có linh cảm là sẽ thành công đấy.」

**1657 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với nhóm — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). Cùng một VN "Anh á?" cũng xuất hiện ở 日々姫01 2307 (JP 「僕がか？」) — đó là cùng một lỗi xưng hô ở file khác, không phải tràn chương.

- JP: 「僕？」
- TW: 「我？」
- Cũ: 「Anh á?」
- Sửa: 「Tôi á?」

**1727 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với nhóm — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「さて――それなのだが。僕は“キジ馬”を、\nひとつのキーにできないだろうかと考えている」
- TW: 「是這樣的。我在考慮能不能以“雉子馬”作為便當的主題」
- Cũ: 「À thì——về chuyện đó. Anh đang nghĩ, liệu chúng ta có thể lấy “Kijiuma” làm một từ khóa chính được không.」
- Sửa: 「À thì——về chuyện đó. Tôi đang nghĩ, liệu chúng ta có thể lấy “Kijiuma” làm một từ khóa chính được không.」

**1739 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Paulette — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「れいなを支えるポーレットを、僕は支えようと思う。\nきっとそれが、一番良い結果につながるはずだ」
- TW: 「波萊特支持著玲奈，而我會支持著波萊特。這一定是最好的解決方法」
- Cũ: 「Anh định sẽ hỗ trợ Paulette, người đang hỗ trợ Reina. Chắc chắn điều đó, sẽ dẫn đến kết quả tốt nhất.」
- Sửa: 「Tôi định sẽ hỗ trợ Paulette, người đang hỗ trợ Reina. Chắc chắn điều đó, sẽ dẫn đến kết quả tốt nhất.」

**2273 [lời dẫn]** — Độc thoại của Soutetsu tự xưng "Anh" — trái quy ước độc thoại của file (tôi 61 dòng vs mình 8 dòng, tất cả đều đúng) và docs (locations §2.1: độc thoại "Tôi").

- JP: 僕はただ、自分自身の目的を果たそうとしただけだった。
- TW: 我只是想達成我的目的而已。
- Cũ: Anh chỉ đơn thuần là cố gắng hoàn thành mục đích của bản thân thôi.
- Sửa: 「Tôi chỉ đơn thuần là cố gắng hoàn thành mục đích của bản thân thôi.」

### Sai nghĩa

**2400 [lời dẫn]** — ぽわっと là ánh sáng ấm áp, mờ dịu (tiền lệ Paulette 12 1448: "Ấm dần lên", KHÔNG phải "Phừng phực"); "cười rạng rỡ" (rực rỡ, sáng chói) đi ngược hướng với ぽわっと. やわらかに = dịu dàng thì bản cũ đã đúng.

- JP: ぽわっと、やわらかにれいなが笑う。
- TW: 玲奈高興地笑了起來。
- Cũ: Reina cười rạng rỡ, dịu dàng.
- Sửa: 「Reina khẽ cười, ấm áp và dịu dàng.」

### Lỗi nhỏ

**1889 [Soutetsu]** — Mất tiếng hít っ: JP 「っ！！？」 dịch thành "!!?" trơ trụi (TW cũng nuốt mất: "！！！"). Tiền lệ Hachiroku 12 2103/2537 và Paulette 09 2274/2275/2277: JP 「っ！」→ "Ư!".

- JP: 「っ！！？」
- TW: 「！！！」
- Cũ: 「!!?」
- Sửa: 「Ư!!?」

**1890 [Hachiroku]** — Mất tiếng hít っ: JP 「っ！！？」 dịch thành "!!?" trơ trụi. Tiền lệ Hachiroku 12 2103/2537 và Paulette 09 2274/2275/2277: JP 「っ！」→ "Ư!".

- JP: 「っ！！？」
- TW: 「！！？」
- Cũ: 「!!?」
- Sửa: 「Ư!!?」

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
1386 = "「Tôi vẫn sẽ đối xử với em như vậy. Giống hệt như Reina bây giờ.」"
1422 = "「Nhưng hội đồng thành phố đã phán quyết rằng——kế hoạch Mine Treasure phù hợp để gửi gắm tương lai của Ohitoyo hơn.」"
1424 = "「Nhưng tôi nghĩ, nếu là Paulette hiện tại thì sẽ không sao cả. Nếu là chúng ta bây giờ, có thể hỗ trợ lẫn nhau và đưa ra phán đoán tốt hơn.」"
1508 = "「A! Ý đó có vẻ hay đấy!! Cá hương cũng là siêu đặc sản của Ohitoyo mà.」"
1514 = "「Ừ, ừm. Em không nói thì tôi cũng đi mà.」"
1519 = "「Ừ. Về phần tôi thì cực kỳ tán thành. Tất nhiên, cũng phải hỏi ý kiến của nhóm Paulette nữa.」"
1544 = "「Vì phần lớn công việc, tôi đều có thể giao cho Paulette mà. Tôi chỉ cần lấp đầy những khoảng trống đó thôi.」"
1560 = "「Tuyệt quá, toàn là đặc sản của Ohitoyo không à!」"
1571 = "「Nếu là Paulette trước đây, có lẽ tôi đã truyền đạt một cách thận trọng hơn một chút.」"
1584 = "「Houshou Kisaki——Giám đốc chi nhánh Ohitoyo của ngân hàng Kumamoto.」"
1617 = "「Tôi, đã hoàn thành trách nhiệm rồi sao.」"
1622 = "「Sức mạnh của tôi thì có gì——」"
1628 = "「Mỗi lần như vậy, tôi chỉ liều mạng đối mặt với những thứ trước mắt thôi. Có lẽ tôi mới là người không nhìn thấu được tương lai nhất cũng nên.」"
1644 = "「Tôi là……đường ray sao.」"
1647 = "「Tôi sẽ cố gắng hết sức. Để các em có thể một lần nữa, chạy đi mà không chút vướng bận.」"
1653 = "「Tôi đi bàn bạc với ông Minokasa. Tôi muốn nhờ ông ấy tập hợp các thợ thủ công lại càng sớm càng tốt.」"
1655 = "「Cái này——tôi có linh cảm là sẽ thành công đấy.」"
1657 = "「Tôi á?」"
1683 = "「Ga bỏ hoang Tsuruha mới, đi qua, tốt!」"
1723 = "「Vâng. Đúng là vậy. Những vị đó, dự định sẽ đến thị sát Ohitoyo.」"
1727 = "「À thì——về chuyện đó. Tôi đang nghĩ, liệu chúng ta có thể lấy “Kijiuma” làm một từ khóa chính được không.」"
1733 = "「Ừm. Tôi nghĩ nó sẽ là một trợ thủ đắc lực cho việc chấn hưng du lịch, nên đang nhờ cô ấy phát triển một loại 『Cơm hộp bento nhà ga mang đậm chất Ohitoyo』.」"
1739 = "「Tôi định sẽ hỗ trợ Paulette, người đang hỗ trợ Reina. Chắc chắn điều đó, sẽ dẫn đến kết quả tốt nhất.」"
1814 = "「Dự định là, dự định đó. Nghe nói hai vị đó cùng nhau “dự định” sẽ đến thị sát Ohitoyo vào mùng 10 tháng sau.」"
1878 = "「Kế hoạch Mine Treasure. Tương lai mà Ohitoyo, mà chúng ta đang hướng tới. Ngài Soutetsu đã vạch ra con đường thẳng tắp đó.」"
1889 = "「Ư!!?」"
1890 = "「Ư!!?」"
2123 = "「Thậm chí những món độc lạ như sushi cá hương, cũng được ăn rất bình thường ở Ohitoyo.」"
2135 = "「Ban đầu, là để bảo vệ thị trấn Ohitoyo và môi trường. Thêm vào đó là việc muốn để Hachiroku được chạy một lần nữa——」"
2273 = "「Tôi chỉ đơn thuần là cố gắng hoàn thành mục đích của bản thân thôi.」"
2400 = "「Reina khẽ cười, ấm áp và dịu dàng.」"
2462 = "「Công nhận mỏ than Jutsu-sen là mỏ than kế thừa kỹ thuật. Chỉ định đền Akai Aso là tài sản văn hóa.」"
```

Khối trên đã kiểm chứng: parse bằng tomllib được **32/32 keys**, giá trị khớp đúng JSON. Không còn dạng cũ nào trong khối sửa (0 "Ohimitera"/"Ohito"/"Jussen"/"Jutsusen").

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- **Soutetsu gọi Paulette "cô" vs "em": "em" 1× (1549), "cô" 0×.** Dòng duy nhất: 1549 "Để truyền đạt cho em, Paulette——vào lúc nào, và như thế nào." Các "cô" khác trong file đều gọi người khác (1409 Kisaki, 1562 Nagayama, 1673 Kisaki). Tổng hợp P09–14: "cô" 43× vs "em" 6× (P09 7:1, P10 20:2, P11 9:0, P12 7:0, P13 0:2, P14 0:1). Chuỗi nghiêng về "cô" vẫn áp đảo, nhưng P13–P14 cho thêm 3 "em" liên tiếp.
- **湯医: "Yui" 1× (83 "ga Yui"), "Yunoi" 0×.** File này không có thêm bằng chứng furigana ゆのい. Tổng hợp: "Yunoi" vẫn dẫn nhờ Grand 01 + 夜の嵐 + Paulette 10 (7×, 1524 có furigana ゆのい) + Paulette 11 (1×); "Yui" xuất hiện ở 廃炭鉱, 実りの秋 (2102) và file này.
- **"KiHa 07": 3 gloss (1400, 1818, 2049)** — thêm bằng chứng cho đề xuất thống nhất "KiHa" (chính tả JR).
- **運転ボディ → "thân hình lái tàu" (2286); 整備ボディ → "thân chính bảo dưỡng" (2530).** Cả hai đều là bằng chứng mới cho đề xuất cặp "thân vận hành" / "thân bảo trì" đang chờ chốt: 2286 dùng "thân hình lái tàu" (dịch sát nghĩa từng chữ), 2530 dùng "thân chính bảo dưỡng" (khác với "thân chính" trơ trụi từng bị coi là lỗi gộp hai thân ở Hachiroku 12 — ở đây có thêm "bảo dưỡng" nên đã phân biệt được, không tính là sai).
- **新鶴羽 vs 新弦羽:** 1683 viết "Tsuruha mới" cho 新弦羽; một dòng khác trong dự án viết "Ga bỏ hoang Tân Tsuruha" cho 新鶴羽. Hai ga có kanji khác nhau (弦羽 vs 鶴羽) nhưng cùng đọc つるは — có thể là cùng một ga viết khác nhau, hoặc hai ga khác nhau. Đề xuất thống nhất "mới" vs "Tân" trong đợt rà soát sau (không tính thêm lỗi).

## Đề xuất cập nhật context (chưa chốt)

Không có đề xuất mới. Các đề xuất đang chờ vẫn giữ nguyên: 湯医 "Yunoi" vs "Yui"; "cô" vs "em"; 整備体/運転ボディ; "KiHa" vs "Kiha"; 帝鉄; コン; 駿袋鉄道.

## Đã kiểm tra và KHÔNG tính là sai

- **1410 [Hibiki]** — câu bị ngắt quãng kiểu "Của cô em gái dễ thương, dành cho ông anh trai đó" — JP cũng là một mảnh câu dở dang (「かわいい、義兄さんの義妹の」 kết thúc bằng の), bản Việt giữ đúng dạng mảnh câu đó; hai thẻ %l gloss cho ruby [にい,1]/[いもうと,1] có sẵn trong JP. Giữ nguyên.
- **1495 [Hibiki]** — 美味しそう dịch "Nghe ngon quá đi!": JP 美味しそう (trông ngon) vs TW 聽起來 (nghe ngon) — bản Việt theo TW. Nhưng trong cảnh này mọi người đang nghe mô tả ý tưởng bento chứ không nhìn thấy món ăn, nên "nghe ngon" là tự nhiên trong tiếng Việt; đây là khác biệt quy ước ngôn ngữ, không phải sai nghĩa. Giữ nguyên.
- **1549 [Soutetsu]** — "cô ấy nghĩ anh có thể chọn…" — "anh" nằm trong câu tường thuật suy nghĩ của Paulette ("cô ấy nghĩ…"), tức là cách Paulette gọi Soutetsu, không phải Soutetsu tự xưng. Giữ nguyên.
- **1404 [Nagi]** — đếm số "Hai mươi sáu!——…" bỏ っ sau mỗi số: っ ở đây chỉ là nhấn mạnh, không phải tiếng hít độc lập 「っ！」 — không thuộc mẫu lỗi mất tiếng hít. Giữ nguyên.
- **1677 [đền chủ Akai]** — "trăm sự nhờ ông" thêm vào so với JP 「どうか」: là cách nói nhờ vả tự nhiên trong tiếng Việt, không đổi nghĩa. Giữ nguyên.

## Kết bài

Paulette 14 (32/376, 8,5%) — file sạch về cấu trúc (0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng chưa dịch, 0 dòng chưa chắc chắn), nhưng là **file Paulette có tỉ lệ xưng hô sai cao nhất kể từ Paulette 07 支線**: Soutetsu tự xưng "anh" trong 17/72 dòng thoại của mình, cộng 1 dòng độc thoại "Anh" — gần như là lựa chọn nhất quán của người dịch file này, trái docs và trái quy ước của các file Paulette gần đây (P11, P12: "anh" 0 lần). Thuật ngữ 12 dòng thì quen thuộc (10 Ohitoyo + 1 Jutsusen + 1 "ga phế liệu" — dòng 1683 là cách dịch 廃駅 duy nhất kiểu này trong toàn dự án). Ba lỗi còn lại đều là mẫu hệ thống đã biết: mất tiếng hít っ (1889, 1890) và ぽわっと dịch quá sáng (2400).

**Còn lại cho file này:** không còn gì — sau khi áp 32 bản sửa, file coi như xong, trừ các quyết định đang chờ Hieu chốt (đặc biệt "cô" vs "em" — file này cho thêm 1 "em", tổng hợp P09–14 là "cô" 43 vs "em" 6; và 湯医 — file này chỉ có 1 "Yui", không làm thay đổi cán cân nghiêng về "Yunoi").

**Tổng cộng: 27 file đã audit, 1.774 dòng sai** (25 file / 1.706 + 32 + 36).
