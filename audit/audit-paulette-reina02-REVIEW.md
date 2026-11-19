# Audit: Paulette れいな02_れいなとポーレット (Reina và Paulette — tắm chung, họp bàn bán than) — 26 dòng Việt sai (đã đối chiếu JP + TW)

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa từng dòng: 419 dòng (độc thoại 158, れいな 82, 双鉄 61, ポーレット 55, ハチロク 18, 凪 11, 稀咲 8, ふかみ 8, 赤井宮司 6, ナビ 4, 日々姫 4, 蓑笠 2, 登呂流湯主人 2), toàn bộ thuộc section `script`, đối chiếu JP + TW từ CSV3 và TOML-2.
- CSV vs TOML: 0 khác biệt thực chất (chỉ ở `\n`/khoảng trắng); tập key bằng nhau (419); `[selections]` rỗng; thẻ `%l`: JP 69 thẻ, VN 72 thẻ — 3 thẻ VN thừa (1171, 2721, 2160 — đều đã sửa, xem dưới); 0 thẻ thiếu dấu `;` đóng; không có key trùng; không có dòng VN trống; VN==TW 1 (1229 `「…………」` — đúng như vậy).
- md5: `f14fdc142675b01dfd3e16602c0ec165` — trùng khớp với bản sao ở `04_Reina/れいな02_れいなとポーレット.txt.toml` (nhóm trùng lặp 03_Paulette ↔ 04_Reina; bản sửa áp dụng cho CẢ HAI bản sao).
- Đọc toàn bộ 419 dòng phát hiện 26 dòng sai (6,2%) — file sạch thứ hai trong các file Paulette đã kiểm (sau h7 7,4% thì file này còn thấp hơn). Thoại sai 17/261, lời dẫn sai 9/158. Theo người nói: 双鉄 10, độc thoại 9, れいな 2, 赤井宮司 2, ポーレット 1, 稀咲 1, ハチロク 1.
- Rà soát chéo với sweep gasp っ: sweep có 3 mục trong file này — 3 bản sửa (1948, 2199, 2388), audit xác nhận cả 3 cùng giá trị, không xung đột; 0 mục "already-rendered"; audit KHÔNG tìm thêm gasp nào sweep bỏ sót trong file này (đã kiểm tra toàn bộ các dòng っ cuối câu, っ đầu dòng và っ gắn từ — các trường hợp còn lại đều là っ nhấn mạnh/cắt âm, không phải gasp, xem § "Đã kiểm tra").
- Quét máy tính bổ sung: quét xưng hô Soutetsu (chuẩn hoá `\n` trước regex `\b`) — 5 dòng "anh" tự xưng, tất cả đều sai (2133, 1795, 1223, 1897, 1891); quét `\bchu\b` toàn cột VN: 0 lần trúng; quét ký tự Nhật còn sót trong VN (ngoài thẻ %l): 0; kiểm tra VN trùng: 4 nhóm (xem dưới); kiểm tra thẻ %l: JP 69 / VN 72 (xem trên).
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ 26/26 bản sửa đối chiếu JP (đúng 26, 0 bị loại). Kiểm tra lần hai xác nhận: không có bản sửa nào thừa hưởng lỗi xưng hô của dòng cho (không có dòng nào thu hồi VN từ dòng khác); không có khoảng trắng thừa trước `\n` (bản sửa một dòng, không dùng `\n`); không có dấu 。 thay cho dấu .; không còn mảnh La-tinh nào sót; không có っ thô trong bản sửa. **Bản sửa viết một dòng (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công** (như h5–h8).

## Kết luận về cơ chế lỗi

- **File sạch về cấu trúc: 0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương.** Không có dòng nào phải dịch mới, không có dòng nào thu hồi VN từ dòng khác. Lỗi rải rác, không theo họ hệ thống nào ngoài thuật ngữ (13) và xưng hô Soutetsu (5 + 1 lần gọi Paulette "cô").
- **Thuật ngữ: 13/26 dòng sai là thuật ngữ đã quyết nhưng chưa áp dụng** — Ohimitera 6 lần (2068, 2668, 2165, 1636, 1666, 1813), 帝鉄 3 lần (63, 2436, 1900 — đều dùng "Đường sắt Hoàng gia"), 冥国 3 lần (1777, 1169, 1158 — đều phiên âm "Meikoku"), タブレット 1 lần (2657 — "thẻ bảng"). File này là bằng chứng rõ nhất cho thấy các quyết định 19/11 chưa được áp dụng ngược vào các file đã dịch trước đó.
- **Thẻ %l tự thêm: 3 thẻ VN thừa so với JP** (1171, 2721 — gloss 改軌; 2160 — gloss 8620) — theo tiền lệ 機関士 (không thêm gloss khi JP không có), đã gỡ cả 3 thẻ, giữ nguyên chữ hiển thị. Sau khi sửa, VN còn đúng 69 thẻ = JP.
- VN trùng trong file (4 nhóm) đều hợp lệ: 1758/1753 (cùng `「うむ」` → "Ừm."), 1810/1975 (`「はいですぅ」`/`「はぁい」` → "Vâng ạ~" — hai câu đồng ý khác nhau, cùng bản dịch), 2062/2061 (cùng JP `「ね？ れいな」` → "Này? Reina." — câu lặp trong cảnh), 1676/1689 (cùng `「え？」` → "Hả?").
- 3 dòng độc thoại có dấu 「」 (2797, 2451, 2630 — lời dẫn trích câu nói) đều đúng, không phải lỗi loại dòng.

## Chi tiết dòng sai

### Thuật ngữ — 御一夜 → "Ohitoyo" (6 dòng)

**Key 2068 (双鉄)**
- JP: "「今日も、無事に御一夜に戻れそうだな」"
- TW: "「看來今天也能平安返回御一夜了」"
- VN cũ: "「Có vẻ hôm nay chúng ta cũng sẽ về đến Ohimitera an toàn nhỉ.」"
- Sửa: "「Có vẻ hôm nay chúng ta cũng sẽ về đến Ohitoyo an toàn nhỉ.」"
- Lý do: 御一夜 → "Ohitoyo" theo quyết định 19/11; VN cũ "Ohimitera".

**Key 2668 (monologue)**
- JP: "ほんの少し、笑いをふくんだような声。\\n御一夜まではあと少し、\\x%lエアクラ;#00ffc040;エアクラ%l;#;はとっくに作動可能だ。"
- TW: "玲奈的聲音中彷彿帶著些許笑意。很快就要到御一夜了，\\x%lエアクラ;#00ffc040;空凝機%l;#;早已恢復到可以運行的狀態。"
- VN cũ: "Một giọng nói dường như chứa đựng chút ý cười.\\nChỉ còn một chút nữa là đến Ohimitera, \\x%lエアクラ;#00ffc040;Aircra%l;#; đã có thể hoạt động từ lâu rồi."
- Sửa: "Một giọng nói dường như chứa đựng chút ý cười. Chỉ còn một chút nữa là đến Ohitoyo, \\x%lエアクラ;#00ffc040;Aircra%l;#; đã có thể hoạt động từ lâu rồi."
- Lý do: 御一夜 → "Ohitoyo" theo quyết định 19/11; VN cũ "Ohimitera".

**Key 2165 (れいな)**
- JP: "「入線良しですぅ。\\n御一夜駅。定刻通り。[ヒトナナマルマル,3]一七〇〇」"
- TW: "「進站正常。御一夜站。準點到站。１７００」"
- VN cũ: "「Vào ga an toàn rồi ạ.\\nGa Ohimitera. Đúng giờ. 17:00.」"
- Sửa: "「Vào ga an toàn rồi ạ. Ga Ohitoyo. Đúng giờ. 17:00.」"
- Lý do: 御一夜 → "Ohitoyo" theo quyết định 19/11; VN cũ "Ohimitera".

**Key 1636 (双鉄)**
- JP: "「御一夜駅一番入線。[ヒトナナマルマル,3]一七〇〇」"
- TW: "「停靠御一夜站１號月台。１７００」"
- VN cũ: "「Vào ga Ohimitera đường ray số 1. 17:00.」"
- Sửa: "「Vào ga Ohitoyo đường ray số 1. 17:00.」"
- Lý do: 御一夜 → "Ohitoyo" theo quyết định 19/11; VN cũ "Ohimitera".

**Key 1666 (双鉄)**
- JP: "「まさか御一夜-湯医間では気分転換になるまいしな。\\nかといって、他の路線となると――」"
- TW: "「只在御一夜與湯醫之間往返，也算不上散心。可要說其它路線的話——」"
- VN cũ: "「Chẳng lẽ lại đi lại giữa Ohimitera và Yui thì đâu gọi là giải khuây.\\nNhưng nếu đi tuyến khác thì——」"
- Sửa: "「Chẳng lẽ lại đi lại giữa Ohitoyo và Yunoi thì đâu gọi là giải khuây. Nhưng nếu đi tuyến khác thì——」"
- Lý do: Hai lỗi thuật ngữ trong một dòng: 御一夜 → "Ohitoyo" và 湯医 → "Yunoi" (furigana ゆのい), theo quyết định 19/11; VN cũ "Ohimitera và Yui".

**Key 1813 (赤井宮司)**
- JP: "「御一夜あたりだけを見れば信じられないだろうけどね。\\n首都圏となると、話はまるで違ったんだ」"
- TW: "「如果只看御一夜周邊，你或許會不敢相信。但若是放眼首都圈，則完全是另一番景象」"
- VN cũ: "「Nếu chỉ nhìn khu vực quanh Ohimitera thì chắc cháu không tin đâu nhỉ.\\nNhưng ở khu vực thủ đô thì câu chuyện hoàn toàn khác đấy.」"
- Sửa: "「Nếu chỉ nhìn khu vực quanh Ohitoyo thì chắc cháu không tin đâu nhỉ. Nhưng ở khu vực thủ đô thì câu chuyện hoàn toàn khác đấy.」"
- Lý do: 御一夜 → "Ohitoyo" theo quyết định 19/11; VN cũ "Ohimitera".

### Thuật ngữ — 帝鉄 (3 dòng)

**Key 63 (monologue)**
- JP: "帝都における\\x%l帝鉄;#00ffc040;帝鉄%l;#;勤務も、そこまで過酷なものだったのか\\n――思ってすぐさま、ああ、そうだったかと思いだす。"
- TW: "\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;明明位於帝都，工作殘酷竟然還如此殘酷——我一瞬間閃過這樣的念頭，然後很快想到了答案。"
- VN cũ: "Công việc ở \\x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; tại Đế đô cũng khắc nghiệt đến mức đó sao\\n——Vừa nghĩ đến đó, tôi lập tức nhớ ra, à, đúng là như vậy."
- Sửa: "Công việc ở \\x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#; tại Đế đô cũng khắc nghiệt đến mức đó sao ——Vừa nghĩ đến đó, tôi lập tức nhớ ra, à, đúng là như vậy."
- Lý do: 帝鉄 — lần đầu xuất hiện trong file (theo thứ tự script): dùng dạng đầy đủ "Đường sắt Đế quốc" trong thẻ %l; VN cũ "Đường sắt Hoàng gia" sai khái niệm (quyết định 19/11: 帝鉄 = Đường sắt Đế quốc, không phải Hoàng gia).

**Key 2436 (monologue)**
- JP: "ハチロクが、なんとも微妙な顔になる。\\n――\\x%l帝鉄;#00ffc040;帝鉄%l;#;末期の、あまりに巨額の累積赤字。"
- TW: "八六神情複雜。我想到的是\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;末期那巨額的累積赤字。"
- VN cũ: "Hachiroku làm một vẻ mặt rất khó tả.\\n——Đó là khoản lỗ lũy kế khổng lồ vào thời kỳ cuối của \\x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;."
- Sửa: "Hachiroku làm một vẻ mặt rất khó tả. ——Đó là khoản lỗ lũy kế khổng lồ vào thời kỳ cuối của \\x%l帝鉄;#00ffc040;Teitetsu%l;#;."
- Lý do: 帝鉄 → "Teitetsu" theo quyết định 19/11; VN cũ "Đường sắt Hoàng gia" trong thẻ %l.

**Key 1900 (赤井宮司)**
- JP: "「元\\x%l帝鉄;#00ffc040;帝鉄%l;#;の職員になら、人脈があります。\\n必要があれば、いつでも声をかけてください」"
- TW: "「我有前\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;職員的人脈。如果有需要，請隨時來找我」"
- VN cũ: "「Nếu là cựu nhân viên \\x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; thì tôi có quen biết.\\nKhi nào cần, xin cứ gọi tôi bất cứ lúc nào.」"
- Sửa: "「Nếu là cựu nhân viên \\x%l帝鉄;#00ffc040;Teitetsu%l;#; thì tôi có quen biết. Khi nào cần, xin cứ gọi tôi bất cứ lúc nào.」"
- Lý do: 帝鉄 → "Teitetsu" theo quyết định 19/11; VN cũ "Đường sắt Hoàng gia" trong thẻ %l.

### Thuật ngữ — 冥国 → "Minh Quốc" (3 dòng)

**Key 1777 (稀咲)**
- JP: "「政治的な動きがあったからね。\\n[めいこく,1]冥国にプッシュされると、否も応も無い」"
- TW: "「因為曾有過政治層面的操作。一旦受到美國的施壓，日本就別無選擇」"
- VN cũ: "「Vì có động thái chính trị nhúng tay vào mà.\\nMột khi đã bị Meikoku gây áp lực, thì chẳng có quyền nói không.」"
- Sửa: "「Vì có động thái chính trị nhúng tay vào mà. Một khi đã bị Minh Quốc gây áp lực, thì chẳng có quyền nói không.」"
- Lý do: 冥国 → "Minh Quốc" theo quyết định 19/11 (furigana めいこく, không phải メリケン nói); VN cũ phiên âm "Meikoku".

**Key 1169 (monologue)**
- JP: "冥国がくしゃみをすれば、日ノ本は三十九度の熱を出す。"
- TW: "“美國打一個噴嚏，日本就要發３９度的高燒”。"
- VN cũ: "Meikoku mà hắt hơi một cái, là Hinomoto sốt ba mươi chín độ."
- Sửa: "Minh Quốc mà hắt hơi một cái, là Hinomoto sốt ba mươi chín độ."
- Lý do: 冥国 → "Minh Quốc" theo quyết định 19/11; VN cũ phiên âm "Meikoku".

**Key 1158 (monologue)**
- JP: "――そういわれるほど、あの\\x%l大戦;#00ffc040;大戦%l;#;での戦勝国、\\n冥国が日ノ本へ与える影響は絶大だ。"
- TW: "——從這一句調侃中就能看得出，身為昔日那場大戰戰勝國的美國，對日本的影響是多麼巨大。"
- VN cũ: "——Người ta hay ví von như vậy, đủ thấy quốc gia thắng trận trong cuộc \\x%l大戦;#00ffc040;Đại chiến%l;#; năm xưa,\\nMeikoku, có tầm ảnh hưởng to lớn đến Hinomoto như thế nào."
- Sửa: "——Người ta hay ví von như vậy, đủ thấy quốc gia thắng trận trong cuộc \\x%l大戦;#00ffc040;Đại chiến%l;#; năm xưa, Minh Quốc, có tầm ảnh hưởng to lớn đến Hinomoto như thế nào."
- Lý do: 冥国 → "Minh Quốc" theo quyết định 19/11; VN cũ phiên âm "Meikoku".

### Thuật ngữ — タブレット → "máy tính bảng" (1 dòng)

**Key 2657 (monologue)**
- JP: "れいなは床に降り立って、\\n手早く\\x%lタブレット;#00ffc040;タブレット%l;#;を換装する。"
- TW: "玲奈從座位上跳下來，迅速地將\\x%lタブレット;#00ffc040;操作板%l;#;更換過去。"
- VN cũ: "Reina nhảy xuống sàn,\\nnhanh nhẹn tháo lắp \\x%lタブレット;#00ffc040;thẻ bảng%l;#;."
- Sửa: "Reina nhảy xuống sàn, nhanh nhẹn tháo lắp \\x%lタブレット;#00ffc040;máy tính bảng%l;#;."
- Lý do: タブレット → "máy tính bảng" theo quyết định 19/11; VN cũ "thẻ bảng" trong thẻ %l (không bao giờ dùng "Thẻ bảng").

### Xưng hô — Soutetsu tự xưng "anh" và gọi Paulette "cô" (6 dòng)

**Key 2133 (双鉄)**
- JP: "「\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;であるハチロクも、その遠縁である\\n僕の\\x%lエアクラ;#00ffc040;エアクラ%l;#;のナビも。普通に悩むし、心配もする」"
- TW: "「身為\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的八六，以及我那台稱得上是八六遠房親戚的\\x%lエアクラ;#00ffc040;空凝機%l;#;Ｎａｖｉ，都會煩惱、會擔心」"
- VN cũ: "「Hachiroku, một \\x%lレイルロオド;#00ffc040;Railord%l;#;, và cả Navi, trợ lý ảo \\x%lエアクラ;#00ffc040;Aircra%l;#; của anh,\\ncó thể coi là họ hàng xa của em, cũng biết trăn trở và lo lắng như người bình thường đấy.」"
- Sửa: "「Hachiroku, một \\x%lレイルロオド;#00ffc040;Railord%l;#;, và cả Navi, trợ lý ảo \\x%lエアクラ;#00ffc040;Aircra%l;#; của tôi, có thể coi là họ hàng xa của em, cũng biết trăn trở và lo lắng như người bình thường đấy.」"
- Lý do: Soutetsu tự xưng "anh" ("của anh") trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại. ("của em" trong dòng này gọi Reina, không phải Paulette — không tính vào đếm "cô"/"em".)

**Key 1795 (双鉄)**
- JP: "「ハチロクが基礎を叩き込んでくれたおかげだ。\\nというか――ポーレットはどうかしたのか？」"
- TW: "「多虧了八六你讓我牢牢掌握了基礎，對了，波萊特怎麼了嗎？」"
- VN cũ: "「Nhờ Hachiroku đã rèn giũa nền tảng cho anh đấy.\\nMà――Paulette sao thế?」"
- Sửa: "「Nhờ Hachiroku đã rèn giũa nền tảng cho tôi đấy. Mà――Paulette sao thế?」"
- Lý do: Soutetsu tự xưng "anh" ("cho anh") trong thoại — JP không có 僕 tường minh nhưng người nói là Soutetsu; quy tắc Soutetsu "Tôi".

**Key 1223 (双鉄)**
- JP: "「\\x%l客車;#00ffc040;客車%l;#;主体、\\x%l貨車;#00ffc040;貨車%l;#;一両くらいでやってもらえんだろうか？\\n観光客の看板になると同時に、宣伝にもなると思うので」"
- TW: "「\\x%l客車;#00ffc040;客運車廂%l;#;主體，外加一節\\x%l貨車;#00ffc040;貨運車廂%l;#;可以嗎？因為這麼做不僅能夠吸引遊客，還能起到宣傳作用」"
- VN cũ: "「Chủ yếu là \\x%l客車;#00ffc040;toa hành khách%l;#;, thêm khoảng một \\x%l貨車;#00ffc040;toa chở hàng%l;#; thì em làm được không?\\nVì anh nghĩ việc này vừa thu hút khách du lịch, vừa mang tính quảng bá nữa.」"
- Sửa: "「Chủ yếu là \\x%l客車;#00ffc040;toa hành khách%l;#;, thêm khoảng một \\x%l貨車;#00ffc040;toa chở hàng%l;#; thì em làm được không? Vì tôi nghĩ việc này vừa thu hút khách du lịch, vừa mang tính quảng bá nữa.」"
- Lý do: Soutetsu tự xưng "anh" ("Vì anh nghĩ") trong thoại — JP không có 僕 tường minh nhưng người nói là Soutetsu; quy tắc Soutetsu "Tôi". ("em" trong dòng này gọi Hachiroku, không phải Paulette.)

**Key 1897 (双鉄)**
- JP: "「と、思う。あるいは、混合\\x%l列車;#00ffc040;列車%l;#;の乗車オプションとして、\\n工場見学などの設定もできようし」"
- TW: "「我是這麼認為的。或者也可以在混合\\x%l列車;#00ffc040;列車%l;#;的觀光路線中，加入參觀工廠的選項」"
- VN cũ: "「Anh nghĩ vậy. Hoặc cũng có thể thiết lập thêm\\nlựa chọn tham quan nhà máy cho hành khách đi \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp.」"
- Sửa: "「Tôi nghĩ vậy. Hoặc cũng có thể thiết lập thêm lựa chọn tham quan nhà máy cho hành khách đi \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp.」"
- Lý do: Soutetsu tự xưng "Anh" trong thoại — người nói là Soutetsu; quy tắc Soutetsu "Tôi".

**Key 1891 (双鉄)**
- JP: "「ひとつだけ。教えて欲しいことがあるんだ」"
- TW: "「我想向你請教一件事」"
- VN cũ: "「Chỉ một chuyện thôi. Có điều này anh muốn hỏi em.」"
- Sửa: "「Chỉ một chuyện thôi. Có điều này tôi muốn hỏi em.」"
- Lý do: Soutetsu tự xưng "anh" ("anh muốn hỏi em") trong thoại — người nói là Soutetsu; quy tắc Soutetsu "Tôi". ("em" trong dòng này gọi Reina, không phải Paulette.)

**Key 2017 (双鉄)**
- JP: "「ポーレット。\\nこの線で、提案・交渉を頼めるだろうか？」"
- TW: "「波萊特。能麻煩你按照這個方向進行提案與交涉嗎？」"
- VN cũ: "「Paulette.\\nCô có thể dựa theo hướng này để đề xuất và đàm phán được không?」"
- Sửa: "「Paulette. Em có thể dựa theo hướng này để đề xuất và đàm phán được không?」"
- Lý do: Soutetsu gọi Paulette "Cô" — theo quyết định 19/11 phải là "em"; sửa "Cô có thể" → "Em có thể". (Đây là lần "cô" gọi Paulette duy nhất trong file.)

### Thở gấp っ — sweep xác nhận cùng giá trị (3 dòng)

**Key 2199 (双鉄)**
- JP: "「っ！」"
- TW: "「！」"
- VN cũ: "「!」"
- Sửa: "「Ư!」"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP 「っ！」 cả dòng bị bỏ mất trong VN.

**Key 1948 (れいな)**
- JP: "「はぁい、もちろん大好き――っ」"
- TW: "「是啊，當然是最喜歡——」"
- VN cũ: "「Vâng ạ~, tất nhiên là cực kỳ thích——」"
- Sửa: "「Vâng ạ~, tất nhiên là cực kỳ thích——Ư」"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP kết bằng ――っ bị bỏ mất trong VN.

**Key 2388 (monologue)**
- JP: "混合\\x%l列車;#00ffc040;列車%l;#;のことをれいなに聞かされた時、\\n全く同じ感想を――っ！"
- TW: "之前聽玲奈提起混合\\x%l列車;#00ffc040;列車%l;#;的時候，我也有過同樣的感想——啊！"
- VN cũ: "Khi nghe Reina kể về \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp,\\ntôi cũng có cảm nghĩ y hệt như vậy——!"
- Sửa: "Khi nghe Reina kể về \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp, tôi cũng có cảm nghĩ y hệt như vậy——Ư!"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP kết bằng ――っ！ bị bỏ mất trong VN.

### Thẻ %l do VN tự thêm — gỡ thẻ, giữ chữ hiển thị (3 dòng)

**Key 1171 (monologue)**
- JP: "カイキが必要になるケースもありそうですが、\\n赤井宮司がぼそりとつぶやく。"
- TW: "“雖然可能有些地方需要改軌”——赤井宮司如此喃喃自語道。"
- VN cũ: "\"Chắc cũng có trường hợp cần phải \\x%l改軌;#00ffc040;cải khổ đường ray%l;#; đấy\",\\nđền chủ Akai lẩm bẩm."
- Sửa: "\"Chắc cũng có trường hợp cần phải cải khổ đường ray đấy\", đền chủ Akai lẩm bẩm."
- Lý do: Thẻ %l gloss do VN tự thêm — JP không có thẻ ở đây (カイキ viết thường); theo tiền lệ 機関士 (không thêm gloss khi JP không có), gỡ thẻ, giữ nguyên chữ hiển thị "cải khổ đường ray".

**Key 2721 (monologue)**
- JP: "僕にはわからぬカイキに大きく頷いて、\\nハチロクも、きらきらとした瞳を僕へと向け直す。"
- TW: "聽到“改軌”這個我無法理解的詞，八六重重地點了點頭，用閃閃發亮的眼神看向我。"
- VN cũ: "Hachiroku gật đầu mạnh trước từ \"\\x%l改軌;#00ffc040;cải khổ đường ray%l;#;\" mà tôi không hiểu,\\nrồi cũng hướng đôi mắt lấp lánh về phía tôi."
- Sửa: "Hachiroku gật đầu mạnh trước từ \"cải khổ đường ray\" mà tôi không hiểu, rồi cũng hướng đôi mắt lấp lánh về phía tôi."
- Lý do: Thẻ %l gloss do VN tự thêm — JP không có thẻ ở đây (カイキ viết thường); theo tiền lệ 機関士, gỡ thẻ, giữ nguyên chữ hiển thị "cải khổ đường ray". (Dòng này Soutetsu nói rõ "từ mà tôi không hiểu" — gloss sẵn càng phá nhịp.)

**Key 2160 (ハチロク)**
- JP: "「となると、[ハチロク,3]8620も混合\\x%l列車;#00ffc040;列車%l;#;を？\\n大足ですので……あまり重いのは得意では無いのですが」"
- TW: "「這樣的話，８６２０也要牽引混合\\x%l列車;#00ffc040;列車%l;#;嗎？它的動輪很大……所以不便於牽引太重的車廂」"
- VN cũ: "「Vậy thì, \\x%l8620;#00ffc040;8620%l;#; cũng sẽ kéo \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp ạ?\\nBánh xe của em lớn…… nên em không giỏi kéo đồ quá nặng đâu ạ.」"
- Sửa: "「Vậy thì, 8620 cũng sẽ kéo \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp ạ? Bánh xe của em lớn…… nên em không giỏi kéo đồ quá nặng đâu ạ.」"
- Lý do: Thẻ %l do VN tự thêm cho 8620 — JP không có thẻ ở đây (8620 viết kèm ruby [ハチロク,3], không phải thẻ %l); theo tiền lệ 機関士, gỡ thẻ, giữ nguyên "8620". (Các dòng khác trong file JP có thẻ 8620 thì VN giữ đúng.)

### Sai nghĩa (1 dòng)

**Key 1733 (ポーレット)**
- JP: "「あ、そっか。トロッコとかの――\\x%l特殊軌道;#00ffc040;特殊軌道%l;#;の車輌なんだ。\\nゲージいくつ？　 [ろっぴゃくじゅう,4]610mmとか？」"
- TW: "「啊，這樣啊，原來是屬於礦車那一類的\\x%l特殊軌道;#00ffc040;特殊軌道%l;#;車輛。軌距是多少？６１０毫米嗎？」"
- VN cũ: "「A, ra vậy. Là phương tiện của \\x%l特殊軌道;#00ffc040;khổ đường sắt đặc biệt%l;#;——giống xe goòng nhỉ.\\nKhổ bao nhiêu? 610mm à?」"
- Sửa: "「A, ra vậy. Là phương tiện của \\x%l特殊軌道;#00ffc040;đường sắt đặc biệt%l;#;——giống xe goòng nhỉ. Khổ bao nhiêu? 610mm à?」"
- Lý do: 特殊軌道 (đường ray đặc biệt — phương tiện chạy đường đặc biệt như xe goòng) bị dịch thành "khổ đường sắt đặc biệt" — nhầm 軌道 (đường ray) với 軌間 (khổ đường ray; 1999 dùng "Khổ đường sắt" đúng cho 軌間).

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng ngoài các dòng đã quyết)

- Soutetsu gọi Paulette "em" 0 lần vs "cô" 1 lần (2017 — "Cô có thể dựa theo hướng này…", đã sửa thành "Em") — cộng dồn toàn dự án: **"em" 97 vs "cô" 49** (sau lr_kisaki 97/48 + file này 0/1). Lưu ý quan trọng: 5 dòng "cô" mà quét máy tính tìm được (2025, 1942, 1998, 1889, 1561) đều KHÔNG phải gọi Paulette — 2025 là "cô em gái" (chỉ Navi, ngôi thứ ba) + "của em" gọi Reina; 1942/1998/1889 là "cô ấy" ngôi thứ ba (chỉ Paulette, không phải cách gọi); 1561 gọi NAVI ("Cảm ơn cô" — Soutetsu gọi Navi là "cô", hợp lý vì Navi là trợ lý AI nữ, không phải trẻ con). Tương tự, 5 dòng "em" của Soutetsu trong file đều gọi Reina (2133, 2025, 1755, 1891) hoặc Hachiroku (1223) — KHÔNG tính vào đếm Paulette.
- 帝鉄: 3 lần trong file, thứ tự script là 63 → 2436 → 1900 — 63 là lần đầu nên dùng dạng đầy đủ "Đường sắt Đế quốc" trong thẻ %l, 2436/1900 dùng "Teitetsu".
- 冥国: 3 lần, tất cả đều phiên âm "Meikoku" (1777, 1169, 1158) — furigana đều là めいこく (cách đọc), không phải メリケン nói — theo quyết định phải là "Minh Quốc".
- KiHa: 2 lần (2529, 2460) đều đã đúng "KiHa 07". 宮司: 4 lần (2537, 2754, 1171, 2126) đều đã đúng "đền chủ". コン: 1 lần (2707) đã đúng "Trưởng ga Kon". Không có 湯医線 dạng "Yui"/"Yunosaka" ngoài 1666 ("Yui" — đã sửa thành "Yunoi"); không có マスコン/整備体/運転ボディ/駿袋/Migita/オコジョ/帝大/福岳 trong file. Paulette gọi Soutetsu "cậu": 0 lần. Tên trần "Soutetsu" trong câu nói: 0 lần. Soutetsu gọi Paulette "cậu": 0 lần.
- Paulette độc thoại xưng "tôi"/"mình" lẫn lộn (2552/2831 dùng "mình" trong câu "Giá như mình…", 2570/2794/2787 dùng "tôi") — đây là biến thể phong cách trong câu ước ("Giá như mình…"), không có quy tắc quyết cho độc thoại Paulette; giữ nguyên, ghi nhận là quan sát.

## Đề xuất cập nhật context (chưa chốt)

- Không có đề xuất mới từ file này.

## Đã kiểm tra và KHÔNG tính là sai

- 1238 "Vẫn chưa――được." (JP 「……まだだ――っと」) — thêm một từ "được" để hoàn chỉnh mảnh câu; nghĩa không đổi, nằm trong quyền tự do của dịch giả với mảnh câu lửng; giữ nguyên (ghi nhận là trường hợp biên).
- 1739 (JP "không nghĩ tới chuyện đi bác sĩ" → VN "chẳng ai muốn đến bác sĩ") — khái quát hoá theo TW ("一般也不會去找醫生"); giữ nguyên.
- 2152 冥ドル → "đô la Mỹ" — theo quy ước thế giới hư cấu (冥国=Mỹ) + TW １美元; giữ nguyên.
- 1700 あぁっ → "Aaa" — っ cuối gắn với nguyên âm là ngắt âm, không phải gasp (theo quy tắc sweep); giữ nguyên.
- 1673 ふぅっ → "Phù" — tiếng thở dài có ngắt âm, diễn đúng; giữ nguyên.
- 1226 良しっ！ / 1646 一本っ！？ — っ nhấn mạnh cuối từ, không phải gasp; giữ nguyên.
- 1691 んんっ → "khụ" — tiếng hắng giọng, diễn đúng; giữ nguyên.
- 1909/1695 っと → "Ồ"/"À" — diễn đúng tiếng ừ/à ngắt câu; giữ nguyên.
- 2432 チチチチ (tiếng kìm soát vé) — đã hấp thụ vào "thao tác thoăn thoắt" + "lách cách" ở câu trước; giữ nguyên.
- 2451/2797/2630 (độc thoại có dấu 「」) — trích dẫn lời nói trong lời dẫn, đúng; giữ nguyên.
- 1229 VN==TW `「…………」` — đúng như vậy.
- 2126 カイキ → "Kaiki" (phiên âm) — từ lạ mà Soutetsu đang hỏi nghĩa, giữ phiên âm là đúng (cùng lý do gỡ gloss ở 1171/2721: không cho sẵn nghĩa của từ mà nhân vật nói là không hiểu).
- 1948/2199/2388 ngoài 3 dòng sweep — không còn gasp nào bị bỏ mất (đã kiểm tra toàn bộ っ trong file).

## Kết bài

- れいな02 sai 26/419 (6,2%) — file sạch nhất trong các file Paulette đã kiểm tính tới nay; 0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương; lỗi tập trung ở thuật ngữ đã quyết nhưng chưa áp dụng ngược (13) + xưng hô Soutetsu (6) + thở gấp っ (3) + thẻ %l tự thêm (3) + sai nghĩa (1).
- Khối TOML 26 key đã parse đúng bằng tomllib; số key khớp đúng với JSON (26); giá trị JSON khớp 0 sai lệch với khối TOML; giá trị VN cũ trong JSON khớp 0 sai lệch với file TOML gốc (sau khi chuẩn hoá `\n` → khoảng trắng).
- Kiểm tra lần hai: 26/26 bản sửa đọc lại đối chiếu JP, 0 bị loại.
- Rà soát chéo sweep: 3 bản sửa sweep trong file đều được audit xác nhận cùng giá trị (không xung đột); 0 mục "already-rendered"; audit không tìm thêm gasp nào sweep bỏ sót.
- Bằng chứng mới: Soutetsu gọi Paulette "em" 0 lần vs "cô" 1 lần (2017, đã sửa) — cộng dồn "em" 97 vs "cô" 49. Ghi chú: 5 dòng "cô" quét máy tính tìm được đều không phải gọi Paulette (ngôi thứ ba hoặc gọi Navi).

```toml
[script]
63 = "Công việc ở \\x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#; tại Đế đô cũng khắc nghiệt đến mức đó sao ——Vừa nghĩ đến đó, tôi lập tức nhớ ra, à, đúng là như vậy."
1158 = "——Người ta hay ví von như vậy, đủ thấy quốc gia thắng trận trong cuộc \\x%l大戦;#00ffc040;Đại chiến%l;#; năm xưa, Minh Quốc, có tầm ảnh hưởng to lớn đến Hinomoto như thế nào."
1169 = "Minh Quốc mà hắt hơi một cái, là Hinomoto sốt ba mươi chín độ."
1171 = "\"Chắc cũng có trường hợp cần phải cải khổ đường ray đấy\", đền chủ Akai lẩm bẩm."
1223 = "「Chủ yếu là \\x%l客車;#00ffc040;toa hành khách%l;#;, thêm khoảng một \\x%l貨車;#00ffc040;toa chở hàng%l;#; thì em làm được không? Vì tôi nghĩ việc này vừa thu hút khách du lịch, vừa mang tính quảng bá nữa.」"
1636 = "「Vào ga Ohitoyo đường ray số 1. 17:00.」"
1666 = "「Chẳng lẽ lại đi lại giữa Ohitoyo và Yunoi thì đâu gọi là giải khuây. Nhưng nếu đi tuyến khác thì——」"
1733 = "「A, ra vậy. Là phương tiện của \\x%l特殊軌道;#00ffc040;đường sắt đặc biệt%l;#;——giống xe goòng nhỉ. Khổ bao nhiêu? 610mm à?」"
1777 = "「Vì có động thái chính trị nhúng tay vào mà. Một khi đã bị Minh Quốc gây áp lực, thì chẳng có quyền nói không.」"
1795 = "「Nhờ Hachiroku đã rèn giũa nền tảng cho tôi đấy. Mà――Paulette sao thế?」"
1813 = "「Nếu chỉ nhìn khu vực quanh Ohitoyo thì chắc cháu không tin đâu nhỉ. Nhưng ở khu vực thủ đô thì câu chuyện hoàn toàn khác đấy.」"
1891 = "「Chỉ một chuyện thôi. Có điều này tôi muốn hỏi em.」"
1897 = "「Tôi nghĩ vậy. Hoặc cũng có thể thiết lập thêm lựa chọn tham quan nhà máy cho hành khách đi \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp.」"
1900 = "「Nếu là cựu nhân viên \\x%l帝鉄;#00ffc040;Teitetsu%l;#; thì tôi có quen biết. Khi nào cần, xin cứ gọi tôi bất cứ lúc nào.」"
1948 = "「Vâng ạ~, tất nhiên là cực kỳ thích——Ư」"
2017 = "「Paulette. Em có thể dựa theo hướng này để đề xuất và đàm phán được không?」"
2068 = "「Có vẻ hôm nay chúng ta cũng sẽ về đến Ohitoyo an toàn nhỉ.」"
2133 = "「Hachiroku, một \\x%lレイルロオド;#00ffc040;Railord%l;#;, và cả Navi, trợ lý ảo \\x%lエアクラ;#00ffc040;Aircra%l;#; của tôi, có thể coi là họ hàng xa của em, cũng biết trăn trở và lo lắng như người bình thường đấy.」"
2160 = "「Vậy thì, 8620 cũng sẽ kéo \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp ạ? Bánh xe của em lớn…… nên em không giỏi kéo đồ quá nặng đâu ạ.」"
2165 = "「Vào ga an toàn rồi ạ. Ga Ohitoyo. Đúng giờ. 17:00.」"
2199 = "「Ư!」"
2388 = "Khi nghe Reina kể về \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp, tôi cũng có cảm nghĩ y hệt như vậy——Ư!"
2436 = "Hachiroku làm một vẻ mặt rất khó tả. ——Đó là khoản lỗ lũy kế khổng lồ vào thời kỳ cuối của \\x%l帝鉄;#00ffc040;Teitetsu%l;#;."
2657 = "Reina nhảy xuống sàn, nhanh nhẹn tháo lắp \\x%lタブレット;#00ffc040;máy tính bảng%l;#;."
2668 = "Một giọng nói dường như chứa đựng chút ý cười. Chỉ còn một chút nữa là đến Ohitoyo, \\x%lエアクラ;#00ffc040;Aircra%l;#; đã có thể hoạt động từ lâu rồi."
2721 = "Hachiroku gật đầu mạnh trước từ \"cải khổ đường ray\" mà tôi không hiểu, rồi cũng hướng đôi mắt lấp lánh về phía tôi."
```

