# Audit — ハチロク02_8620運転台通信.txt.toml (01_Hachiroku)

## Tổng quan

- File: `ハチロク02_8620運転台通信.txt.toml` — route 01_Hachiroku, **336 dòng script** (độc thoại 132, Soutetsu 63, Hachiroku 46, Điện xa Công chúa 31, Fukami 22, Nagi 21, Hibiki 14, Paulette 4, Reina 2, chim sẻ 1).
- Nội dung: buổi họp trực tuyến với Điện xa Công chúa Mouri Aki — bà đặt mua dài hạn bản tin "8620運転台通信" (miễn phí trọn đời), hứa tặng một toa hành khách phù hợp với 8620 trong 2 tuần, mời cả nhóm đến Hiroshima; xen kẽ là các đoạn giải thích kỹ thuật về buồng đốt/ống lò hơi/thân lò/buồng khói, bữa ăn do Nagi–Fukami mang đến, và vụ nhầm lẫn 'chop' (cú chặt) với 'chip' (tiền tip) của bà cụ người nước ngoài.
- Phương pháp: đọc từng dòng đối chiếu JP + TW từ CSV3 (Trang tính 3), kiểm chứng chéo sweep っ, kiểm tra cơ học trùng khóa/trùng VN/thẻ %l/dòng chưa dịch.
- **Kết quả: 336 dòng đọc, 17 dòng sai (5,1%).**
- Phân loại (17): thuật ngữ 5 (71, 1741, 1917, 2535, 2766), gasp っ 5 (1465, 1837, 2261, 2272, 2282), đại từ 2 (1951, 2230), dịch sai 2 (1906, 2222), bỏ sót 1 (1940), lỗi chính tả 1 (1945), SFX 1 (2415).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất (không có set trùng/stale). VN khớp TOML sau chuẩn hoá `\n` (210 dòng chênh lệch chỉ là `\n` bị TOML-2 dẹp thành khoảng trắng — đã biết, CSV3 là chuẩn). `[selections]` rỗng. Không có bản sao của file này (md5 `9ffb338bd09ef4a09ec44ee58a3ab01a`, không trùng md5 với file nào khác).
- Đại từ đã kiểm chứng toàn file: Soutetsu 'anh' đúng với Hibiki/Nagi/Fukami (1867, 1882, 1931, 1936, 2057, 2059, 2217, 2672); 'tôi' đúng với Điện xa Công chúa (1889, 1998, 2073, 2171, 2181, 2251) và với Hachiroku trong các dòng độc thoại; Hachiroku tự xưng 'em' nhất quán; Paulette→Soutetsu chỉ sai 1 dòng (1951). Nagi→Fukami 'bé' đúng (1954); Fukami tự xưng 'mình' không xuất hiện sai trong file này.

## Kiểm chứng sweep っ

- Sweep có **4 mục** cho file này trong `sweep-raw-gasp-wrong.json` (1837, 2261, 2272, 2282) — cả 4 đều kiểm chứng đúng với JP, đã nhận nguyên văn vào danh sách sửa.
- Sweep **sót 1 mục**: key 1465 「っ――」 (gasp nguyên dòng kèm dấu gạch) không có trong sweep — đã tự bắt và sửa thành 「Ư——」.
- Các っ còn lại trong file đã rà bằng máy (JP chứa っ mà VN không có Ư): toàn bộ là っ trong từ/ngữ điệu địa phương đã được diễn tả (ばいっ→'á', ひゃわっ→'Hyawa', うおっ→'Ua', ちゅんくっ→'Chun!', ぼりんっ/バリっ→'Rộp!/Rắc!'), hoặc っ cuối nhấn mạnh đã có dấu câu diễn tả — không còn gasp nào bị mất.
- Thẻ %l: số lượng `%l;` JP = VN ở mọi dòng; không có thẻ thiếu dấu `;` hay thẻ lệch trong file này (các cảnh báo 'bare %l' khi quét máy là do tag mở có dạng `\x%l<từ>;` — đó là dạng chuẩn, không phải lỗi).

## Chi tiết từng dòng sai (17)

### key 71 — monologue — terminology

- JP: \x%l市電;#00ffc040;市電%l;#;なら、線路は町の間を縫って走っているはず。\n\x%l8620;#00ffc040;8620%l;#;の吐き出す煙は、町を真っ黒にしてしまおう。
- TW: \x%l市電;#00ffc040;市電%l;#;的路線鋪設在街道之間。\x%l8620;#00ffc040;８６２０%l;#;排出的煙將會燻黑附近街道的設施。
- VN cũ: Nếu là \x%l市電;#00ffc040;nguồn điện chính%l;#;, thì đường ray chắc chắn sẽ chạy len lỏi giữa các khu phố.\nKhói do \x%l8620;#00ffc040;8620%l;#; nhả ra sẽ nhuộm đen cả thành phố mất.
- VN mới: Nếu là \x%l市電;#00ffc040;tàu điện thành phố%l;#;, thì đường ray chắc chắn sẽ chạy len lỏi giữa các khu phố.\nKhói do \x%l8620;#00ffc040;8620%l;#; nhả ra sẽ nhuộm đen cả thị trấn mất.
- Lý do: Gloss %l của 市電 sai hẳn: 'nguồn điện chính' (nguồn điện chính = main power supply) trong khi 市電 = tàu điện thành phố — thuật ngữ đã chốt. 町 (thị trấn Ohitoyo) dịch thành 'thành phố' là sai nghĩa: trong chính file này key 2773 dịch 町 là 'thị trấn'. Hai dòng 71/1917 đã nằm trong danh sách chờ đợt thống nhất — sửa luôn tại đây để gạch khỏi danh sách đó.

### key 1465 — 双鉄 — gasp

- JP: 「っ――」
- TW: 「——」
- VN cũ: 「——」
- VN mới: 「Ư——」
- Lý do: JP là gasp nguyên dòng っ――, VN bỏ mất っ chỉ còn dấu gạch. Theo quy tắc gasp: っ đầu dòng/đứng một mình kèm dấu câu là tiếng rên → thêm Ư. TW cũng bỏ (——) nhưng JP thắng TW. Sweep KHÔNG liệt kê dòng này — sweep sót 1 mục trong file.

### key 1741 — ハチロク — terminology

- JP: 「もっとも、[めいこく,1]冥国は戦後、素晴らしい国となりました。\nあの国の大統領は、立派な方でございます」
- TW: 「不過，美國在戰後確實國力昌盛。美國的總統，也是一位治國有方的人」
- VN cũ: 「Tuy nhiên, nước Mỹ sau chiến tranh đã trở thành một quốc gia tuyệt vời.\nTổng thống của đất nước đó là một người xuất chúng ạ.」
- VN mới: 「Tuy nhiên, Minh Quốc sau chiến tranh đã trở thành một quốc gia tuyệt vời.\nTổng thống của đất nước đó là một người xuất chúng ạ.」
- Lý do: 冥国 dịch 'nước Mỹ' trái thuật ngữ đã chốt: 冥国 = 'Minh Quốc'. TW nói 美國 nhưng JP thắng TW; [めいこく,1] là furigana đọc, không phải tên nước thật.

### key 1837 — 双鉄 — gasp

- JP: 「っ！」
- TW: 「呃！」
- VN cũ: 「!」
- VN mới: 「Ư!」
- Lý do: Sweep lost-gasp-whole, đã kiểm chứng đúng JP 「っ！」/TW 呃！ → nhận nguyên văn fix của sweep.

### key 1906 — 双鉄 — mistranslation

- JP: 「ほう。西洋にもそうした――\n体育会系ノリというヤツはあるのだな」
- TW: 「噢。在西方也有這種——體育系風格的禮尚往來方式啊」
- VN cũ: 「Hô. Ở phương Tây cũng có kiểu——\nđộng chân động tay của mấy người theo chủ nghĩa thể thao à.」
- VN mới: 「Hô. Ở phương Tây cũng có kiểu——\nđáp lễ kiểu dân thể thao à.」
- Lý do: 体育会系ノリ = phong cách đáp lễ kiểu dân câu lạc bộ thể thao; TW nói rõ 體育系風格的禮尚往來方式 (cách đáp lễ qua lại). VN cũ 'động chân động tay của mấy người theo chủ nghĩa thể thao' vừa sai nghĩa ノリ (không khí/phong cách, không phải 'động chân động tay') vừa bịa thêm 'chủ nghĩa' không có trong JP.

### key 1917 — ハチロク — terminology

- JP: 「[ばいえん,1]煤煙――煙突から出る猛然たる煙によって、です。\n廣島電気鉄道は、\x%l市電;#00ffc040;[しでん,1]市電%l;#;とお伺いいたしましたので」
- TW: 「因為煙囪中會排出大量的黑煙——也就是煤煙。據我所知廣島電氣鐵路為\x%l市電;#00ffc040;市電%l;#;」
- VN cũ: 「Là do muội than——khói mù mịt thải ra từ ống khói ạ.\nVì em được biết Đường sắt Điện Hiroshima là \x%l市電;#00ffc040;nguồn điện chính%l;#; ạ.」
- VN mới: 「Là do muội than——khói mù mịt thải ra từ ống khói ạ.\nVì em được biết Đường sắt Điện Hiroshima là \x%l市電;#00ffc040;tàu điện thành phố%l;#; ạ.」
- Lý do: Giống key 71: gloss %l 市電 'nguồn điện chính' sai → 'tàu điện thành phố' (thuật ngữ đã chốt).

### key 1940 — ハチロク — omission

- JP: 「それを繰り返していけば、[うちの子,3]8620のことを、\nみなさまにも広く、より深く知っていただけるのですね」
- TW: 「如此反覆下去，大家就會對[我們家這孩子,3]８６２０理解更多，訊息也會傳播得更廣」
- VN cũ: 「Nếu cứ lặp đi lặp lại như vậy, mọi người sẽ biết đến 8620,\nmột cách rộng rãi và sâu sắc hơn nhỉ.」
- VN mới: 「Nếu cứ lặp đi lặp lại như vậy, mọi người sẽ biết đến 8620 nhà mình,\nmột cách rộng rãi và sâu sắc hơn nhỉ.」
- Lý do: JP có tag [うちの子,3] (8620 như 'đứa con trong nhà'), TW giữ lại 我們家這孩子; VN cũ bỏ mất sắc thái này → thêm 'nhà mình'.

### key 1945 — ハチロク — typo

- JP: 「もっともっとです、双鉄様。いずれ、あの高窓に、\n[すみぞ,1]墨染めの雀が鈴なりになりますとも」
- TW: 「它原本就這麼黑，雙鐵少爺。也許不用多久，那邊的天窗上就會有成群結隊的墨染一般黑的麻雀了」
- VN cũ: 「Sẽ còn đen hơn nữa cơ ạ, ngài Soutetsu. Rồi sẽ đến lúc, trên những ô cửa sổ cao kia,\nđàn chim sẻ đen như nhuộm mực sẽ đậu trĩu trĩt cho xem.」
- VN mới: 「Sẽ còn đen hơn nữa cơ ạ, ngài Soutetsu. Rồi sẽ đến lúc, trên những ô cửa sổ cao kia,\nđàn chim sẻ đen như nhuộm mực sẽ đậu trĩu trịt cho xem.」
- Lý do: Lỗi chính tả: 'trĩu trĩt' → 'trĩu trịt' (鈴なり = đậu thành chùm trĩu trịt).

### key 1951 — ポーレット — pronoun

- JP: 「それはそうと双鉄くん。\n姫様がお呼びです」
- TW: 「對了，雙鐵君。公主殿下傳你過去」
- VN cũ: 「Nhắc mới nhớ, cậu Soutetsu.\nCông chúa đang gọi cậu đấy.」
- VN mới: 「Nhắc mới nhớ, anh Soutetsu.\nCông chúa đang gọi anh đấy.」
- Lý do: Paulette gọi Soutetsu là 双鉄くん → theo khóa B4 phải là 'anh Soutetsu', không phải 'cậu Soutetsu'. Cả hai chỗ 'cậu' trong dòng đều sửa thành 'anh'.

### key 2222 — 双鉄 — mistranslation

- JP: 「確かに……これはうまいな。\nパンはもちもち、カツはさくさく――っと」
- TW: 「這麵包……確實挺好吃的。外面的麵包皮鬆軟可口，裡面的炸肉排口感酥脆——啊」
- VN cũ: 「Công nhận……ngon thật.\nBánh mì thì dai mềm, thịt cốt lết thì giòn rụm——ái chà.」
- VN mới: 「Công nhận……ngon thật.\nBánh mì thì dai mềm, thịt cốt lết thì giòn rụm——.」
- Lý do: JP kết bằng さくさく――っと (âm giòn kết thúc đột ngột; dấu gạch —— đã diễn tả cú ngắt). VN cũ thêm 'ái chà' — thán từ ngạc nhiên không có căn cứ trong JP → bỏ, chỉ giữ dấu gạch.

### key 2230 — 双鉄 — pronoun

- JP: 「飾りではない。あのハンドルは回して開けるためにある。\n僕も最初に目にしたときは、驚いた」
- TW: 「那可不是裝飾啊。只要扭動那個把手就真的可以打開。其實我第一次看到那東西的時候也嚇了一跳」
- VN cũ: 「Không phải đồ trang trí đâu. Tay cầm đó dùng để vặn mở đấy.\nLần đầu tiên nhìn thấy, tôi cũng ngạc nhiên lắm.」
- VN mới: 「Không phải đồ trang trí đâu. Tay cầm đó dùng để vặn mở đấy.\nLần đầu tiên nhìn thấy, anh cũng ngạc nhiên lắm.」
- Lý do: Soutetsu trả lời trực tiếp thắc mắc của Fukami ở key 2009 ('tưởng tay cầm tròn là đồ trang trí'), nên tự xưng phải là 'anh' (quy tắc đã sửa: Soutetsu 'anh' với Fukami), không phải 'tôi'.

### key 2261 — ハチロク — gasp

- JP: 「っ！！」
- TW: 「！！」
- VN cũ: 「!!」
- VN mới: 「Ư!!」
- Lý do: Sweep lost-gasp-whole, đã kiểm chứng đúng JP 「っ！！」 → nhận nguyên văn fix của sweep.

### key 2272 — 凪 — gasp

- JP: 『「え～～っ！」\n「え～～っ！」』
- TW: 『「是嗎！」\n「是嗎！」』
- VN cũ: 『「Hả~~!」\n「Hả~~!」』
- VN mới: 『「Hả~~Ư!」\n「Hả~~Ư!」』
- Lý do: Sweep lost-gasp-trailing, đã kiểm chứng đúng JP え～～っ！ ×2 → nhận, thêm Ư sau dấu ~ ở cả hai dòng.

### key 2282 — ハチロク — gasp

- JP: 『「っ！！？」\n「あっ」』
- TW: 『「！！？」\n「啊」』
- VN cũ: 『「!!?」\n「A.」』
- VN mới: 『「Ư!!?」\n「A.」』
- Lý do: Sweep lost-gasp-whole, đã kiểm chứng đúng JP 「っ！！？」 → nhận cho dòng 1; dòng 2 「あっ」 → 'A.' đã diễn tả đủ (dấu chấm diễn tả cú ngắt âm), giữ nguyên.

### key 2415 — monologue — SFX

- JP: なぜなのか、凪はけらけら笑っている。\nふかみは両手で口を押さえて、目を輝かせ僕らを見てる。
- TW: 不知怎的，凪發出了爽朗的笑聲。而深美則是用兩隻手將嘴遮住，朝我們投來饒有興致的目光。
- VN cũ: Chẳng hiểu sao, Nagi lại cười khúc khích.\nCòn Fukami thì lấy hai tay che miệng, mắt sáng rực nhìn chúng tôi.
- VN mới: Chẳng hiểu sao, Nagi lại cười ha hả.\nCòn Fukami thì lấy hai tay che miệng, mắt sáng rực nhìn chúng tôi.
- Lý do: けらけら = cười lớn, sảng khoái (TW: 爽朗的笑聲), không phải cười khúc khích (cười nhỏ). → 'cười ha hả'.

### key 2535 — monologue — terminology

- JP: 分割された画面の中から、僕と同様真っ黒な顔の日々姫と、\n整備ボディに換装し、真っ白なハチロクの叱咤を浴びる。
- TW: 在分屏畫面中傳來了和我一樣臉上黑糊糊的日日姬的，還有換上了整備體被我嚇得滿臉蒼白的八六的訓斥聲。
- VN cũ: Từ trong màn hình được chia nhỏ, tôi bị Hibiki với khuôn mặt đen thui giống mình,\nvà Hachiroku vừa thay thân chính trắng trẻo mắng mỏ.
- VN mới: Từ trong màn hình được chia nhỏ, tôi bị Hibiki với khuôn mặt đen thui giống mình,\nvà Hachiroku vừa thay thân bảo trì trắng trẻo mắng mỏ.
- Lý do: 整備ボディ = thân bảo trì (thân máy bảo trì, đối với 運転ボディ = thân vận hành). VN cũ 'thân chính' sai hoàn toàn nghĩa — 'thân chính' không tồn tại trong hệ thống thân máy của Railord.

### key 2766 — monologue — terminology

- JP: 冥国なり詠国なりの、しかも老婆が、\n賞賛の意で、よもやチョップをくれるなど――
- TW: 美國或者是英國出身的遊客，況且還是老婆婆，居然以贈送小肥肉為表達讚賞的方式――
- VN cũ: Một bà cụ người Mỹ hay người Anh,\nlại đi tặng "cú chặt" để tỏ ý khen ngợi sao——
- VN mới: Một bà cụ người Minh Quốc hay người Anh,\nlại đi tặng "cú chặt" để tỏ ý khen ngợi sao——
- Lý do: 冥国 → 'Minh Quốc' theo thuật ngữ đã chốt (như key 1741). 'người Anh' cho 詠国 giữ nguyên: chưa có thuật ngữ chốt cho 詠国 và TW cũng nói 英國.

## Các dòng đã xem xét nhưng GIỮ NGUYÊN (quyết định có ghi chú)

- 1732 (ハチロク): 鬼畜冥詠 → 'quỷ súc Mỹ Anh' — giữ. Đây là cách chơi chữ với 鬼畜米英 (Mỹ–Anh), TW cũng dịch 鬼畜美英; không phải lỗi.
- 1902 (電車姫): gloss 機関士 'người lái tàu' — giữ. Nghĩa tương đương dạng rút gọn đã chốt 'lái tàu' (機関士 = 'thợ lái đầu máy', dạng ngắn 'lái tàu').
- 2015 (電車姫): そしての？ → 'Và rồi sao?' — giữ. Đây là câu gợi mở trong lập luận của Công chúa, TW 況且 cũng mang nghĩa nối tiếp.
- 2075/2228/2766 (凪/日々姫/độc thoại): vụ 'chop' vs 'chip' (tiền tip) được giải quyết ngay trong thoại (key 2228 Hibiki tự đính chính) — VN 'cú chặt' ở 2075/2766 là đúng theo JP チョップ, không phải lỗi.
- 2254 (双鉄): 詠国 → 'nước Anh' — giữ. Chưa có thuật ngữ chốt cho 詠国; TW nói 英國; khác với 冥国 đã chốt 'Minh Quốc'.

## Các dòng chưa chắc chắn — chờ Hieu (KHÔNG tính vào 17, không tự quyết)

- **1849 (ハチロク)**: JP 「ひゃわっ！？ え？ あ――はい、なんでございましょう、双鉄様」 — VN 「Hyawa!? Hả? A——vâng, có chuyện gì vậy ạ, ngài Soutetsu.」 — ひゃわっ → 'Hyawa': xung đột ひあ/ひゃ toàn dự án ('Hya' vs 'Hia' vs 'Á') đang chờ Hieu chốt.
- **1952 (双鉄)**: JP 「そうだな、そういう感じがいいと僕も考えた。興味を引きそうなエピソードを、説明につなげていく」 — VN 「Đúng vậy, anh cũng nghĩ làm theo hướng đó sẽ rất hay. Kết nối những câu chuyện thú vị vào phần giải thích.」 — 'anh' chưa rõ địa chỉ: nếu Soutetsu đang đáp lại đề xuất làm báo của Hachiroku (key 1940/1945) thì phải là 'tôi'; nếu nói với nhóm Nagi/Fukami thì 'anh' đúng. Dòng kề 1951 (Paulette) / 1953 (Nagi) không phân định được — giữ nguyên.
- **1960 (凪)**: JP 「じいちゃんの仕事みたいばい！」 — VN 「Giống hệt công việc của ông nội em á!」 — 'ông nội' theo quy ước toàn dự án; câu hỏi 'ông nội' hay 'ông ngoại' (dòng 08c: Midori là mẹ Fukami) đang chờ Hieu chốt — ghi chú, không đổi.
- **2049 (ふかみ)**: JP 「こんにちわ。あ、これ、おふたりにお福分け。です」 — VN 「Chào em. A, cái này, là quà lộc cho hai người. ạ.」 — 'Chào em': người được chào không rõ trong dòng (Reina thì 'em' đúng; Hibiki thì phải 'chị'; Nagi thì 'cậu') — giữ nguyên.

## Lượt soát 2 (bắt buộc)

- Tổng số fix: 17 / đã soát lại: 17 / bỏ: 0 / sửa: 7.
- 7 fix được sửa trong lượt soát 2: các key 1741, 1906, 1940, 1945, 1951, 2222, 2230 — kiểm tra diff cơ học phát hiện bản nháp đầu đã làm mất dấu 「」 bao thoại (VN cũ trong CSV3 có 「」); đã khôi phục đủ 「」 và chạy lại kiểm tra diff: mọi fix giờ chỉ khác VN cũ đúng ở chỗ cần sửa.
- Kiểm tra cơ học sau lượt soát 2: JSON 17 mục, khóa là chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 17/17; khối TOML 17 khóa, parse được bằng tomllib, 0 sai lệch giá trị so với JSON; không fix nào chứa ký tự xuống dòng thật (mọi `\n` đều là backslash-n literal như CSV3).

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
"71" = "Nếu là \\x%l市電;#00ffc040;tàu điện thành phố%l;#;, thì đường ray chắc chắn sẽ chạy len lỏi giữa các khu phố.\\nKhói do \\x%l8620;#00ffc040;8620%l;#; nhả ra sẽ nhuộm đen cả thị trấn mất."
"1465" = "「Ư——」"
"1741" = "「Tuy nhiên, Minh Quốc sau chiến tranh đã trở thành một quốc gia tuyệt vời.\\nTổng thống của đất nước đó là một người xuất chúng ạ.」"
"1837" = "「Ư!」"
"1906" = "「Hô. Ở phương Tây cũng có kiểu——\\nđáp lễ kiểu dân thể thao à.」"
"1917" = "「Là do muội than——khói mù mịt thải ra từ ống khói ạ.\\nVì em được biết Đường sắt Điện Hiroshima là \\x%l市電;#00ffc040;tàu điện thành phố%l;#; ạ.」"
"1940" = "「Nếu cứ lặp đi lặp lại như vậy, mọi người sẽ biết đến 8620 nhà mình,\\nmột cách rộng rãi và sâu sắc hơn nhỉ.」"
"1945" = "「Sẽ còn đen hơn nữa cơ ạ, ngài Soutetsu. Rồi sẽ đến lúc, trên những ô cửa sổ cao kia,\\nđàn chim sẻ đen như nhuộm mực sẽ đậu trĩu trịt cho xem.」"
"1951" = "「Nhắc mới nhớ, anh Soutetsu.\\nCông chúa đang gọi anh đấy.」"
"2222" = "「Công nhận……ngon thật.\\nBánh mì thì dai mềm, thịt cốt lết thì giòn rụm——.」"
"2230" = "「Không phải đồ trang trí đâu. Tay cầm đó dùng để vặn mở đấy.\\nLần đầu tiên nhìn thấy, anh cũng ngạc nhiên lắm.」"
"2261" = "「Ư!!」"
"2272" = "『「Hả~~Ư!」\\n「Hả~~Ư!」』"
"2282" = "『「Ư!!?」\\n「A.」』"
"2415" = "Chẳng hiểu sao, Nagi lại cười ha hả.\\nCòn Fukami thì lấy hai tay che miệng, mắt sáng rực nhìn chúng tôi."
"2535" = "Từ trong màn hình được chia nhỏ, tôi bị Hibiki với khuôn mặt đen thui giống mình,\\nvà Hachiroku vừa thay thân bảo trì trắng trẻo mắng mỏ."
"2766" = "Một bà cụ người Minh Quốc hay người Anh,\\nlại đi tặng \"cú chặt\" để tỏ ý khen ngợi sao——"
```

## Kết bài

File ハチロク02_8620運転台通信.txt.toml: 336 dòng đọc, 17 dòng sai (5,1%) — lỗi tập trung ở thuật ngữ đã chốt nhưng bản dịch cũ chưa theo (市電, 冥国, 整備ボディ) và gasp っ bị mất (5 dòng, trong đó 4 từ sweep + 1 sweep sót). Không có lệch dòng, xoay chuỗi, nhiễm chéo hay dòng mồ côi. 4 dòng chờ Hieu (1849, 1952, 1960, 2049) đã liệt kê ở trên, không tính vào tổng sai. Khối TOML 17 khóa đã parse-kiểm chứng, sẵn sàng để gộp.

Kết bài