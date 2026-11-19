# Audit: Paulette h8_気動車の国のアリス (Alice ở xứ sở toa xe tự hành) — 147 dòng Việt sai (đã đối chiếu JP + TW)

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa từng dòng: 649 dòng (độc thoại 252, Paulette 232, Soutetsu 165), toàn bộ thuộc section `script`, đối chiếu JP + TW từ CSV3 và TOML-2.
- CSV vs TOML: 0 khác biệt thực chất (chỉ ở `\n`/khoảng trắng); tập key bằng nhau (649); `[selections]` rỗng; thẻ `%l`: 0 trong VN (không có thẻ hỏng); không có key trùng; không có dòng VN trống; VN==TW 0.
- md5: `da94288489af95805aa9e8d2617d0a42` — không trùng với bất kỳ file nào trong 227 file TOML (không có bản sao; bản sửa áp dụng cho 1 file duy nhất).
- Đọc toàn bộ 649 dòng phát hiện 147 dòng sai (22,7%). Rà soát chéo với sweep gasp っ và quét máy tính (pronoun sweep với `\n` chuẩn hoá trước, quét `\bchu\b` và các mảnh La-tinh còn sót, kiểm tra VN trùng và JP trùng) bắt thêm các dòng ngoài lần đọc đầu.
- Rà soát chéo với sweep gasp っ: sweep có 8 mục trong file này — 7 bản sửa (2147, 2148, 2183, 2252, 2253, 2254, 3150) và 1 "already-rendered" (2344: `ん～～（くちゅちゅっ）――んえ～～っ` → "Ưm~~ (chóp chép)——ưm~~" — audit đồng ý, không đưa vào danh sách sửa). Cả 7 bản sửa của sweep đều là dòng gasp thuần, KHÔNG trùng với bất kỳ bản sửa nào của audit — audit xác nhận cả 7, không có xung đột. Audit phát hiện thêm 2 dòng gasp mà sweep BỎ SÓT trong file này (2208: bỏ mất ぐっ sau っ; 2307: đếm thiếu 1 tiếng ん). Lưu ý: con số "18 mục sweep" từng ghi trong bản nháp là sai — 10 mục trong đó thuộc file Hachiroku h8 (`01_Hachiroku/ハチロクh8_桜色のひめごと.txt.toml`), một file khác.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ 147/147 bản sửa đối chiếu JP (đúng 147, 0 bị loại). Kiểm tra lần hai bắt được 1 lỗi thừa hưởng: 2110 (VN gốc lấy từ 2279 có "anh" là Soutetsu tự xưng — đã sửa thành "tôi"). Kiểm tra lần hai cũng xác nhận: không có bản sửa nào khác thừa hưởng lỗi xưng hô của dòng cho; không có khoảng trắng thừa trước `\n` (bản sửa một dòng, không dùng `\n`); không có dấu 。 thay cho dấu .; các âm thở ghép viết liền một từ ("Kyaphù", "Hakíu", "Hiau", "Híua…an"); không còn mảnh La-tinh nào sót (`\bchu\b` = 0; "pha" trong 2505/2817 là động từ Việt "pha trà", không phải mảnh La-tinh). 5 bản sửa thu hồi đã bỏ khoảng trắng thừa sau —— trong VN gốc (3404, 2224, 2203, 3114, 2290) — theo quy ước gạch —— không có khoảng trắng hai bên.
- Quy ước bản sửa: bản sửa viết MỘT DÒNG (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công — theo quyết định 19/11 của Hieu (game tự ngắt dòng, `\n` thủ công không quan trọng). File TOML gốc cũng lưu các giá trị này một dòng với khoảng trắng, nên khối TOML dưới đây dán vào khớp đúng dạng đó.

## Kết luận về cơ chế lỗi

- **File lệch vị trí nặng — mạng xoay vòng lớn nhất từ trước tới nay: 6 chuỗi, 86 dòng, chuỗi dài nhất 30 mắt xích** (h3 trước đó: 45 dòng, chuỗi dài nhất 15 mắt xích). Toàn bộ 86 dòng lệch đều thu hồi được bản dịch đúng ngay trong file — không có dòng nào phải dịch mới ngoài 6 đầu chuỗi (2784, 2277, 2270, 2776, 2571, 2185).
- **Không có tràn chương**: tất cả 86 dòng lệch đều giải quyết trong file. 5 bản Việt cũ là bản dịch mồ côi, không có JP nào trong toàn dự án khớp với chúng (VN cũ của 2110 "À ừm——ưm!?"; 2608 "Hả?"; 3249 "Ưm——ưm——ưm——"; 2376 "Hể!?"; 2817 "Vậy thì, pha như thế đi.") — mạng xoay vòng này là mạng hở, không phải vòng khép kín. VN cũ của 2227 ("Hự") không phải mồ côi ngoài file mà là bản trùng của 2146.
- **3114 đã được xác nhận lệch vị trí** — như P12 đã cảnh báo trong lần quét chỉ mục trước đó (VN cũ của 3114 "……Paulette." thực ra thuộc về 1510; bản dịch đúng của 3114 nằm ở 3156).
- Lỗi xưng hô hệ thống: Soutetsu tự xưng "anh" 36 dòng trong thoại (cùng lỗi hệ thống như h1–h7; độc thoại không có lần "Anh" nào sai). Quét máy tính tìm được 46 dòng Soutetsu/độc thoại chứa "Anh/anh" — 36 là lỗi thật, 10 còn lại là bản Việt lệch vị trí (2560, 2784, 3490, 3427, 3268, 1510, 3512, 1456, 3343, 2755) — KHÔNG tính là lỗi xưng hô.
- Thuật ngữ: Ohimitera 7 lần (6 dòng riêng + 2695 trong nhóm xưng hô) — tất cả sửa thành Ohitoyo theo quyết định 19/11.
- Tiếng thở La-tinh: 11 dòng (cùng họ lỗi như h1–h7); thở gấp っ bị bỏ mất: 3 dòng (2208, 2307, 2360) — trong đó 2208 và 2307 là 2 dòng sweep bỏ sót.
- Các bản Việt trùng trong file đều đã giải thích: 2146/2227 "Hự" (2227 sai — trùng của 2146); 2148/2253 "!!?" (cả hai đều là dòng gasp của sweep); 2147/2825 "!" (2147 là bản sửa sweep, 2825 đúng).

## Chi tiết dòng sai

### Lệch vị trí — chuỗi xoay vòng (86 dòng)

#### Chuỗi mega — 30 mắt xích (2784 → 2227)
**Key 2784 (双鉄)**
- JP: `「では、それで」`
- TW: `「那就奶茶」`
- VN cũ: `「Vâng. Ư hự hự, vui quá đi.\nĐược uống hồng trà mẹ tặng cùng với Anh Soutetsu thế này.」`
- Sửa: `「Vậy thì, cứ thế đi.」`
- Lý do: Lệch vị trí (đầu chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2402; JP dòng này chưa có bản dịch đúng trong file — dịch mới từ JP.
**Key 2402 (ポーレット)**
- JP: `「はぁい。うふふ、嬉しいなぁ。\nママにもらった紅茶を、双鉄くんと飲めるだなんて」`
- TW: `「好。嘻嘻，我好高興。竟然能把媽媽送的紅茶泡給你喝」`
- VN cũ: `「Anh cũng rất vui. Thật hạnh phúc.」`
- Sửa: `「Vâng. Ufufu, vui quá đi. Được uống hồng trà mẹ tặng cùng với Anh Soutetsu thế này.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2478; bản sửa là VN cũ của key 2784 — bản dịch đúng của JP dòng này.
**Key 2478 (双鉄)**
- JP: `「僕も嬉しい。しあわせだ」`
- TW: `「我也很開心，真是幸福啊」`
- VN cũ: `……Hương thơm nồng nàn bắt đầu lan tỏa khắp cửa hàng đường sắt.`
- Sửa: `「Tôi cũng rất vui. Thật hạnh phúc.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 1463; bản sửa là VN cũ của key 2402 — bản dịch đúng của JP dòng này. (đã sửa "Anh"→"Tôi" trong VN gốc vì đó là lỗi xưng hô của dòng cho)
**Key 1463 (monologue)**
- JP: `……豊かな香りがレールショップを満たし始める。`
- TW: `……鐵路商店裡開始被茶香填滿。`
- VN cũ: `Đặt ấm trà và đĩa lên khay,\nPaulette quay trở lại bàn.`
- Sửa: `……Hương thơm nồng nàn bắt đầu lan tỏa khắp cửa hàng đường sắt.`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 3490; bản sửa là VN cũ của key 2478 — bản dịch đúng của JP dòng này.
**Key 3490 (monologue)**
- JP: `ティーポットとお皿をトレーに乗せて、\nポーレットがテーブルへと戻ってくる。`
- TW: `波萊特把茶壺和盤子放在托盤上，端到了桌子這邊。`
- VN cũ: `「Anh đợi thêm một chút xíu nữa nhé.」`
- Sửa: `Đặt ấm trà và đĩa lên khay, Paulette quay trở lại bàn.`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2711; bản sửa là VN cũ của key 1463 — bản dịch đúng của JP dòng này.
**Key 2711 (ポーレット)**
- JP: `「もうちょっとだけ待ってくださいね」`
- TW: `「請再稍等一下」`
- VN cũ: `Cát trong đồng hồ cát mang màu hổ phách.\nTuôn rơi nhè nhẹ, chảy trôi giữa quá khứ và tương lai.`
- Sửa: `「Anh đợi thêm một chút xíu nữa nhé.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 3427; bản sửa là VN cũ của key 3490 — bản dịch đúng của JP dòng này.
**Key 3427 (monologue)**
- JP: `砂時計の砂は、琥珀色。\n過去と未来の間をさらさら、流れて落ちる。`
- TW: `沙漏裡的砂子呈現琥珀色。連接著過去與未來的細沙緩緩流下。`
- VN cũ: `「Xong rồi đây, xin mời anh thưởng thức.」`
- Sửa: `Cát trong đồng hồ cát mang màu hổ phách. Tuôn rơi nhè nhẹ, chảy trôi giữa quá khứ và tương lai.`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2407; bản sửa là VN cũ của key 2711 — bản dịch đúng của JP dòng này.
**Key 2407 (ポーレット)**
- JP: `「はぁい、どうぞ、召し上がれ」`
- TW: `「好了，請用吧」`
- VN cũ: `Vào chiếc cốc đã được hâm nóng sữa sẵn,\nngay khoảnh khắc hạt cát cuối cùng rơi xuống, hồng trà được thong thả rót vào.`
- Sửa: `「Xin mời anh thưởng thức.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 3520; bản sửa là VN cũ của key 3427 — bản dịch đúng của JP dòng này. (đã bỏ "Xong rồi đây, " trong VN gốc — cụm này không có trong JP)
**Key 3520 (monologue)**
- JP: `ミルクがすでに温められてるカップへと、\n砂が落ちきったその瞬間、紅茶がゆったり注がれる。`
- TW: `溫好的杯子裡已經倒上了牛奶，沙漏裡的沙子流完之後，她就把紅茶慢慢倒了進去。`
- VN cũ: `「……À——Đúng là ngon thật.」`
- Sửa: `Vào chiếc cốc đã được hâm nóng sữa sẵn, ngay khoảnh khắc hạt cát cuối cùng rơi xuống, hồng trà được thong thả rót vào.`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 1504; bản sửa là VN cũ của key 2407 — bản dịch đúng của JP dòng này.
**Key 1504 (双鉄)**
- JP: `「……ああ――確かに旨いな」`
- TW: `「……嗯——確實很好喝」`
- VN cũ: `「Bánh eclair mini. Hợp lắm đấy? Rất hợp luôn.」`
- Sửa: `「……À——Đúng là ngon thật.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2762; bản sửa là VN cũ của key 3520 — bản dịch đúng của JP dòng này.
**Key 2762 (ポーレット)**
- JP: `「ミニエクレア。あいますよ？　すごく」`
- TW: `「這跟泡芙非常搭」`
- VN cũ: `Paulette nhón lấy một chiếc bánh có họa tiết chùm nho sặc sỡ,\nrồi đưa về phía tôi.`
- Sửa: `「Bánh eclair mini. Hợp lắm đấy? Rất hợp luôn.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 3489; bản sửa là VN cũ của key 1504 — bản dịch đúng của JP dòng này.
**Key 3489 (monologue)**
- JP: `ポーレットがひとつ、鮮やかな葡萄の模様のものを\n摘んで僕へと差し出してくれる。`
- TW: `波萊特把一顆葡萄圖案的迷你泡芙遞到我面前。`
- VN cũ: `「Cái này, cứ thế ăn luôn được à?」`
- Sửa: `Paulette nhón lấy một chiếc bánh có họa tiết chùm nho sặc sỡ, rồi đưa về phía tôi.`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2753; bản sửa là VN cũ của key 2762 — bản dịch đúng của JP dòng này.
**Key 2753 (双鉄)**
- JP: `「これは、このまま食べられるのか？」`
- TW: `「這個可以直接吃嗎？」`
- VN cũ: `「Vâng.\nHọa tiết được in lên lớp sô-cô-la trắng đấy ạ.」`
- Sửa: `「Cái này, cứ thế ăn luôn được à?」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2298; bản sửa là VN cũ của key 3489 — bản dịch đúng của JP dòng này.
**Key 2298 (ポーレット)**
- JP: `「はい。\n絵柄は、ホワイトチョコへのプリントですから」`
- TW: `「嗯。圖案是用白巧克力畫上去的」`
- VN cũ: `「Nào, a~」`
- Sửa: `「Vâng. Họa tiết được in lên lớp sô-cô-la trắng đấy ạ.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2088; bản sửa là VN cũ của key 2753 — bản dịch đúng của JP dòng này.
**Key 2088 (ポーレット)**
- JP: `「はい、あ～ん」`
- TW: `「來，張嘴」`
- VN cũ: `Dù nói là mini, nhưng để ăn hết trong một miếng thì hơi to.\nTôi chỉ cắn một nửa vào miệng——`
- Sửa: `「Nào, a~」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 3653; bản sửa là VN cũ của key 2298 — bản dịch đúng của JP dòng này.
**Key 3653 (monologue)**
- JP: `ミニとはいえど、一口で食べきるにはやや大きい。\n半分だけを口の中へと納めれば――`
- TW: `雖然是迷你泡芙，一口還是吃不下去。我把它一半放進了嘴裡——`
- VN cũ: `「…………Hừm. Cái này——tuyệt thật đấy.」`
- Sửa: `Dù nói là mini, nhưng để ăn hết trong một miếng thì hơi to. Tôi chỉ cắn một nửa vào miệng——`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 1506; bản sửa là VN cũ của key 2088 — bản dịch đúng của JP dòng này.
**Key 1506 (双鉄)**
- JP: `「…………むぅ。これは――すごいな」`
- TW: `「……嗯。這個好」`
- VN cũ: `Có lẽ đây là, hương vị của người lớn chăng.`
- Sửa: `「…………Hừm. Cái này——tuyệt thật đấy.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 3638; bản sửa là VN cũ của key 3653 — bản dịch đúng của JP dòng này.
**Key 3638 (monologue)**
- JP: `大人の味、というのだろうか。`
- TW: `這可以說是成年人才能享用的美味吧。`
- VN cũ: `Mang chút cảm giác rượu vang nhè nhẹ của những trái nho chín mọng——\nHòa quyện cùng vị ngọt ngào êm dịu lan tỏa.`
- Sửa: `Có lẽ đây là, hương vị của người lớn chăng.`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 3404; bản sửa là VN cũ của key 1506 — bản dịch đúng của JP dòng này.
**Key 3404 (monologue)**
- JP: `熟した葡萄が持っている、ほんの少しのワイン感――\nその上に、芳醇な甘みが広がっていく。`
- TW: `有成熟葡萄特有的一點葡萄酒的感覺，同時還有芳醇的甘甜。`
- VN cũ: `「Am.」`
- Sửa: `Mang chút cảm giác rượu vang nhè nhẹ của những trái nho chín mọng——Hòa quyện cùng vị ngọt ngào êm dịu lan tỏa.`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2826; bản sửa là VN cũ của key 3638 — bản dịch đúng của JP dòng này. (đã bỏ khoảng trắng sau —— trong VN gốc, theo quy ước gạch —— không có khoảng trắng hai bên)
**Key 2826 (双鉄)**
- JP: `「あむっ」`
- TW: `「（咬）」`
- VN cũ: `Hăng hái cắn miếng thứ hai.\nTôi lỡ ngậm luôn cả đầu ngón tay của Paulette vào miệng.`
- Sửa: `「Am.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 3268; bản sửa là VN cũ của key 3404 — bản dịch đúng của JP dòng này.
**Key 3268 (monologue)**
- JP: `勢い込んでの二口目。\nポーレットの指先までを口にしてしまう。`
- TW: `我又接著吃了第二口。結果就不小心咬到了波萊特的指尖。`
- VN cũ: `「……Ưm——a. Anh Soutetsu.\nNhột——quá.」`
- Sửa: `Hăng hái cắn miếng thứ hai. Tôi lỡ ngậm luôn cả đầu ngón tay của Paulette vào miệng.`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 1502; bản sửa là VN cũ của key 2826 — bản dịch đúng của JP dòng này.
**Key 1502 (ポーレット)**
- JP: `「……ん――あ。双鉄、くん。\nくすぐったい――です」`
- TW: `「……嗯——啊。雙鐵君。這樣好癢」`
- VN cũ: `Thừa thế xông lên, tôi liếm láp, mút mát.\nThưởng thức trọn vẹn vị ngọt ngào, rồi chóp chép nhả ra.`
- Sửa: `「……Ưm——a. Anh Soutetsu. Nhột——quá.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 3282; bản sửa là VN cũ của key 3268 — bản dịch đúng của JP dòng này.
**Key 3282 (monologue)**
- JP: `調子にのって、舐め、ねぶる。\nたっぷり甘みを堪能してから、音をたて、離す。`
- TW: `我就得意忘形地開始舔了起來。我好好享用了一番甜美的手指，吸得咂砸作響，然後再鬆口。`
- VN cũ: `「Quả thực, là thượng hạng. Một hương vị phong phú tuyệt đỉnh.」`
- Sửa: `Thừa thế xông lên, tôi liếm láp, mút mát. Thưởng thức trọn vẹn vị ngọt ngào, rồi chóp chép nhả ra.`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2154; bản sửa là VN cũ của key 1502 — bản dịch đúng của JP dòng này.
**Key 2154 (双鉄)**
- JP: `「まさしく、上質。最高に豊かな味わいだ」`
- TW: `「味道真棒，口感非常豐富」`
- VN cũ: `「À, ừm……cái đó, không có chi, ạ.」`
- Sửa: `「Quả thực, là thượng hạng. Một hương vị phong phú tuyệt đỉnh.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2769; bản sửa là VN cũ của key 3282 — bản dịch đúng của JP dòng này.
**Key 2769 (ポーレット)**
- JP: `「え、ええと……その、おそまつさま、です」`
- TW: `「那、那個……不成敬意」`
- VN cũ: `「Không có chi cái gì, đây là một bữa tiệc ngon lành không gì sánh bằng đấy.」`
- Sửa: `「À, ừm……cái đó, không có chi, ạ.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2067; bản sửa là VN cũ của key 2154 — bản dịch đúng của JP dòng này.
**Key 2067 (双鉄)**
- JP: `「おそまつどころか、この上も無いごちそうだ」`
- TW: `「什麼不成敬意，就沒有比這更好吃的東西了」`
- VN cũ: `Yết hầu Paulette khẽ chuyển động cái ực.`
- Sửa: `「Không có chi cái gì, đây là một bữa tiệc ngon lành không gì sánh bằng đấy.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 3483; bản sửa là VN cũ của key 2769 — bản dịch đúng của JP dòng này.
**Key 3483 (monologue)**
- JP: `こくりと、ポーレットの喉が小さく動く。`
- TW: `波萊特咽了一口唾沫。`
- VN cũ: `「À ừm——nếu vậy.\nEm cũng, muốn ăn thử, ạ.」`
- Sửa: `Yết hầu Paulette khẽ chuyển động cái ực.`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2781; bản sửa là VN cũ của key 2067 — bản dịch đúng của JP dòng này.
**Key 2781 (ポーレット)**
- JP: `「ええと――なら。\nわたしも、食べてみたい、です」`
- TW: `「那個，既然如此，那我也想吃吃看」`
- VN cũ: `Đáp lễ ly rượu, à không, đáp lễ bánh eclair.\nTôi nhón lấy một chiếc có màu như bánh mì nướng, đưa cho cô ấy.`
- Sửa: `「À ừm——nếu vậy. Em cũng, muốn ăn thử, ạ.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 3277; bản sửa là VN cũ của key 3483 — bản dịch đúng của JP dòng này.
**Key 3277 (monologue)**
- JP: `ご返杯、ではなくご返エクレア。\n焼けたトーストの色をしたものを、つまみ、差し出す。`
- TW: `我回敬她一顆泡芙。我拿起一顆顏色跟烤好的吐司一樣的泡芙，遞到她面前。`
- VN cũ: `「A——em xin phép ạ.\nƯm——ngoạm——ngoạm——」`
- Sửa: `Đáp lễ ly rượu, à không, đáp lễ bánh eclair. Tôi nhón lấy một chiếc có màu như bánh mì nướng, đưa cho cô ấy.`
- Lý do: Lệch vị trí (chuỗi xoay vòng mega (30)): VN cũ là bản dịch của JP ở key 2227; bản sửa là VN cũ của key 2781 — bản dịch đúng của JP dòng này.
**Key 2227 (ポーレット)**
- JP: `「あ――いただきまぁす\nんっ――ぱくっ――ぱく――」`
- TW: `「啊——我開動了。嗯——嚼嚼——」`
- VN cũ: `「Hự」`
- Sửa: `「A——em xin phép ạ. Ưm——ngoạm——ngoạm——」`
- Lý do: Lệch vị trí (cuối chuỗi xoay vòng mega (30)): VN cũ là bản dịch mồ côi, không có JP nào trong dự án khớp với nó; bản sửa là VN cũ của key 3277 — bản dịch đúng của JP dòng này.

#### Chuỗi B+10 — 19 mắt xích (2277 → 2376)
**Key 2277 (ポーレット)**
- JP: `「ん――んんっ――んっ――」`
- TW: `「嗯——嗯——嗯——」`
- VN cũ: `Vị ngọt ngào ập đến trong khoang miệng.`
- Sửa: `「Ưm——ưm ưm——ưm——」`
- Lý do: Lệch vị trí (đầu chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 3552; JP dòng này chưa có bản dịch đúng trong file — dịch mới từ JP.
**Key 3552 (monologue)**
- JP: `口内に甘さが押し寄せてくる。`
- TW: `甜美的味道進入了我的口中。`
- VN cũ: `Bánh eclair, cùng với lưỡi và nước bọt của Paulette.\nThứ hỗn hợp sền sệt ấy, từ lưỡi chảy thẳng xuống háng.`
- Sửa: `Vị ngọt ngào ập đến trong khoang miệng.`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 3430; bản sửa là VN cũ của key 2277 — bản dịch đúng của JP dòng này.
**Key 3430 (monologue)**
- JP: `エクレアと、ポーレットの舌と唾液と。\nそれがどろどろ、舌から股間に流れ込む。`
- TW: `泡芙混合上了波萊特小舌和香津。這黏稠的感覺刺激著我的味蕾，也激起了我的欲望。`
- VN cũ: `「Ưm——hự——（ực）」`
- Sửa: `Bánh eclair, cùng với lưỡi và nước bọt của Paulette. Thứ hỗn hợp sền sệt ấy, từ lưỡi chảy thẳng xuống háng.`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 2275; bản sửa là VN cũ của key 3552 — bản dịch đúng của JP dòng này.
**Key 2275 (双鉄)**
- JP: `「ん――くっ――（ごくっ）」`
- TW: `「嗯——唔——（嚥下）」`
- VN cũ: `「Ưm……chụt——chụt——rộp——rộp,\nchụt——chụt——chụt——（ực）」`
- Sửa: `「Ưm——hự——（ực）」`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 2289; bản sửa là VN cũ của key 3430 — bản dịch đúng của JP dòng này.
**Key 2289 (ポーレット)**
- JP: `「ん……ちゅっ――ちゅるっ――れるっ――れろっ、\nちゅううっ――ちゅっ――ちゅずずずっ――（こく）」`
- TW: `「嗯……啾——啾嚕——啾嚕——啾噗——啾噗——啾噗——啾嚕——（嚥下）」`
- VN cũ: `Bánh eclair mini đã trôi xuống cổ họng.\nNhưng vị ngọt ngào lại càng tăng thêm.`
- Sửa: `「Ưm……chụt——chụt——rộp——rộp, chụt——chụt——chụt——（ực）」`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 3307; bản sửa là VN cũ của key 2275 — bản dịch đúng của JP dòng này.
**Key 3307 (monologue)**
- JP: `ミニエクレアは、喉へと落ちた。\nけれど、甘さは増していく。`
- TW: `我把迷你泡芙咽了下去，但是嘴裡的甜味反而更濃了。`
- VN cũ: `「A——ưm……chụt——phù——a——\nchụt——chụt——chụt——chụt——」`
- Sửa: `Bánh eclair mini đã trôi xuống cổ họng. Nhưng vị ngọt ngào lại càng tăng thêm.`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 2224; bản sửa là VN cũ của key 2289 — bản dịch đúng của JP dòng này.
**Key 2224 (ポーレット)**
- JP: `「あ――んっ……ちゅっ――ふ――あっ――\nちゅっ――ちゅむっ――ちゅうっ――ちゅっ――」`
- TW: `「啊——嗯……啾——呼——啊——啾——啾嚕——啾噗——啾——」`
- VN cũ: `Tiếng thở hổn hển. Bốc lên,\nlà hương thơm hòa quyện giữa mồ hôi, sô-cô-la và Paulette.`
- Sửa: `「A——ưm……chụt——phù——a——chụt——chụt——chụt——chụt——」`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 3512; bản sửa là VN cũ của key 3307 — bản dịch đúng của JP dòng này. (đã bỏ khoảng trắng sau —— trong VN gốc, theo quy ước gạch ——)
**Key 3512 (monologue)**
- JP: `漏れてくる息。立ち登ってくる、\n汗とチョコと、ポーレットとの混じった香り。`
- TW: `波萊特輕輕喘息著。升騰起來的汗香和巧克力的味道，加上波萊特的香味。`
- VN cũ: `「Hà……ưm……chụt——chụt——chụt——\nphù, a——thích quá——Anh Soutetsu, ơi——ưm, chụt」`
- Sửa: `Tiếng thở hổn hển. Bốc lên, là hương thơm hòa quyện giữa mồ hôi, sô-cô-la và Paulette.`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 2161; bản sửa là VN cũ của key 2224 — bản dịch đúng của JP dòng này.
**Key 2161 (ポーレット)**
- JP: `「は……ん……ちゅっ――ちゅうっ――チュ――\nふ、あ――しゅき――ほーへふ、ふん――ん、ちゅっ」`
- TW: `「呼……嗯……啾——啾——啾——呼啊——我喜歡你——雙鐵——嗯——啾」`
- VN cũ: `……Thưởng thức trọn vẹn vị ngọt ngào,\ntôi rụt lưỡi vào trong miệng.`
- Sửa: `「Hà……ưm……chụt——chụt——chụt——phù, a——thích quá——Anh Soutetsu, ơi——ưm, ưm, chụt」`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 1456; bản sửa là VN cũ của key 3512 — bản dịch đúng của JP dòng này. (đã thêm một "ưm" — JP có hai tiếng ふん――ん)
**Key 1456 (monologue)**
- JP: `……十分、甘さを堪能しつくし、\n舌を口内に引きこもらせる。`
- TW: `……在好好享受一番甜美的滋味之後，我把舌頭收了回來。`
- VN cũ: `「Ưm? ……A——phù——này? Anh Soutetsu——ưm.\nEm, muốn——nhiều đồ ngọt, hơn nữa——chụt」`
- Sửa: `……Thưởng thức trọn vẹn vị ngọt ngào, tôi rụt lưỡi vào trong miệng.`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 2340; bản sửa là VN cũ của key 2161 — bản dịch đúng của JP dòng này.
**Key 2340 (ポーレット)**
- JP: `「ん？　……ぁ――ぷあっ――ね？　双鉄くん――ん。\nわたし、もっと――甘いの、ほしい――ちゅっ」`
- TW: `「嗯？……啊——呼——雙鐵君——嗯。我還想吃——更多甜甜的」`
- VN cũ: `Paulette chủ động tách môi tôi ra.`
- Sửa: `「Ưm? ……A——phù——này? Anh Soutetsu——ưm. Em, muốn——nhiều đồ ngọt, hơn nữa——chụt」`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 3478; bản sửa là VN cũ của key 1456 — bản dịch đúng của JP dòng này.
**Key 3478 (monologue)**
- JP: `ポーレットから、僕の唇を割ってくる。`
- TW: `波萊特主動把舌頭伸進了我嘴裡。`
- VN cũ: `「Ưm……chụt——ưm——hàm——rộp, rộp,\nchụt, chụt——chụt——rộp, rộp」`
- Sửa: `Paulette chủ động tách môi tôi ra.`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 2292; bản sửa là VN cũ của key 2340 — bản dịch đúng của JP dòng này.
**Key 2292 (ポーレット)**
- JP: `「ん……ちゅっ――っ――はむっ――れるっ、るっ、\nちゅうっ、ちゅるっ――ちゅるるっ――れる、れろっ」`
- TW: `「嗯……啾——嗯——唔——啾嚕——啾嚕——啾噗——啾噗——啾噗——」`
- VN cũ: `Mỗi khi lưỡi Paulette ngọ nguậy,\ntôi có cảm giác như đến cả não mình cũng đang bị liếm láp.`
- Sửa: `「Ưm……chụt——ưm——hàm——rộp, rộp, chụt, chụt——chụt——rộp, rộp」`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 3485; bản sửa là VN cũ của key 3478 — bản dịch đúng của JP dòng này.
**Key 3485 (monologue)**
- JP: `ポーレットの舌が蠢くたびに、\n脳までなめられている気持ちになる。`
- TW: `波萊特在我嘴裡攪來攪去，簡直就是在直接舔我的快感神經。`
- VN cũ: `Đang bị ăn. Toàn bộ con người tôi.\nPaulette đang dùng đôi môi ấy để yêu thương, để nếm thử tôi.`
- Sửa: `Mỗi khi lưỡi Paulette ngọ nguậy, tôi có cảm giác như đến cả não mình cũng đang bị liếm láp.`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 3332; bản sửa là VN cũ của key 2292 — bản dịch đúng của JP dòng này.
**Key 3332 (monologue)**
- JP: `食べられている。僕の全部が。\nポーレットがその口唇で、愛し、味わってくれている。`
- TW: `我的一切都被她品嘗著。波萊特可愛唇舌的動作充滿了愛意。`
- VN cũ: `「Hàm——chụt——rộp——chụt——\nchụt——（ực）——rộp——rộp——chụt」`
- Sửa: `Đang bị ăn. Toàn bộ con người tôi. Paulette đang dùng đôi môi ấy để yêu thương, để nếm thử tôi.`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 2203; bản sửa là VN cũ của key 3485 — bản dịch đúng của JP dòng này.
**Key 2203 (ポーレット)**
- JP: `「はむっ――ちゅううっ――れるっ――じゅずっ――\nずっ――（ごくっ）――れるっ――れろお――ちゅむ」`
- TW: `「唔——啾嚕——啾嚕——啾噗——呼——（嚥下）——啾嚕——啾噗——啾噗——」`
- VN cũ: `Cảm giác dính chặt, càng thêm gia tăng.`
- Sửa: `「Hàm——chụt——rộp——chụt——chụt——（ực）——rộp——rộp——chụt」`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 3262; bản sửa là VN cũ của key 3332 — bản dịch đúng của JP dòng này. (đã bỏ khoảng trắng sau —— trong VN gốc, theo quy ước gạch ——)
**Key 3262 (monologue)**
- JP: `密着感が、更に増す。`
- TW: `我們抱得更緊了。`
- VN cũ: `Muốn cứ thế này mà ôm lấy em.\nMuốn làm tình với em một cách điên cuồng——!!?`
- Sửa: `Cảm giác dính chặt, càng thêm gia tăng.`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 3294; bản sửa là VN cũ của key 2203 — bản dịch đúng của JP dòng này.
**Key 3294 (monologue)**
- JP: `このまま抱いてしまいたい。\nめちゃくちゃに犯してしまいたっ――！！？`
- TW: `我想直接跟她這麼做愛。我想好好蹂躪她一番——`
- VN cũ: `「Phù!? （Lùi lạiiiiiiiii!!）」`
- Sửa: `Muốn cứ thế này mà ôm lấy em. Muốn làm tình với em một cách điên cuồng——!!?`
- Lý do: Lệch vị trí (chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch của JP ở key 2376; bản sửa là VN cũ của key 3262 — bản dịch đúng của JP dòng này.
**Key 2376 (双鉄)**
- JP: `「ぷあっ！？　（ずううううううううっっ！！）」`
- TW: `「噗啊！？（後退）」`
- VN cũ: `「Hể!?」`
- Sửa: `「Phù a!? （Lùi lạiiiiiiiii!!）」`
- Lý do: Lệch vị trí (cuối chuỗi xoay vòng B+10 (19)): VN cũ là bản dịch mồ côi, không có JP nào trong dự án khớp với nó; bản sửa là VN cũ của key 3294 — bản dịch đúng của JP dòng này. (đã sửa "Phù"→"Phù a" — JP ぷあっ, theo quy ước file)

#### Chuỗi C (Alice) — 9 mắt xích (2270 → 2110)
**Key 2270 (双鉄)**
- JP: `「っ」`
- TW: `「喔」`
- VN cũ: `Bị bao bọc.`
- Sửa: `「Hự」`
- Lý do: Lệch vị trí (đầu chuỗi xoay vòng C Alice (9)): VN cũ là bản dịch của JP ở key 3382; JP dòng này chưa có bản dịch đúng trong file — dịch mới từ JP.
**Key 3382 (monologue)**
- JP: `包まれる。`
- TW: `指尖被包住了。`
- VN cũ: `Đầu ngón tay của tôi trong nháy mắt,\nđã nằm gọn trong khoang miệng nóng hổi ướt át của Paulette.`
- Sửa: `Bị bao bọc.`
- Lý do: Lệch vị trí (chuỗi xoay vòng C Alice (9)): VN cũ là bản dịch của JP ở key 3339; bản sửa là VN cũ của key 2270 — bản dịch đúng của JP dòng này.
**Key 3339 (monologue)**
- JP: `僕の指先があっというまに、\nポーレットの熱く濡れた口内に。`
- TW: `我的指尖被波萊特又熱又濕的小嘴包住了。`
- VN cũ: `「Ưm……chụt——chụt——rộp——\nchụt——chụt——liếm——rộp」`
- Sửa: `Đầu ngón tay của tôi trong nháy mắt, đã nằm gọn trong khoang miệng nóng hổi ướt át của Paulette.`
- Lý do: Lệch vị trí (chuỗi xoay vòng C Alice (9)): VN cũ là bản dịch của JP ở key 2290; bản sửa là VN cũ của key 3382 — bản dịch đúng của JP dòng này.
**Key 2290 (ポーレット)**
- JP: `「ん……ちゅっ――ちゅるっ――れるっ――\nちゅむ――ちゅうっ――ぺろっっ――れろおおっ」`
- TW: `「嗯……啾——啾嚕——啾嚕——啾噗——啾噗——啾嚕——啾噗」`
- VN cũ: `Hoàn toàn là, những chuyển động khiêu gợi tôi.`
- Sửa: `「Ưm……chụt——chụt——rộp——chụt——chụt——liếm——rộp」`
- Lý do: Lệch vị trí (chuỗi xoay vòng C Alice (9)): VN cũ là bản dịch của JP ở key 3156; bản sửa là VN cũ của key 3339 — bản dịch đúng của JP dòng này. (đã bỏ khoảng trắng sau —— trong VN gốc, theo quy ước gạch ——)
**Key 3156 (monologue)**
- JP: `完全に、僕を誘う動きだ。`
- TW: `她的動作完全是在勾引我。`
- VN cũ: `Vừa mút mát, vừa dai dẳng, chầm chậm——\nliếm láp phần gốc khớp ngón tay đầu tiên của tôi.`
- Sửa: `Hoàn toàn là, những chuyển động khiêu gợi tôi.`
- Lý do: Lệch vị trí (chuỗi xoay vòng C Alice (9)): VN cũ là bản dịch của JP ở key 3114; bản sửa là VN cũ của key 2290 — bản dịch đúng của JP dòng này.
**Key 3114 (monologue)**
- JP: `吸い上げながら、しつこく、ゆるく――\n指の第一関節の付け根のところを、舐めあげてくる。`
- TW: `她一邊吸吮著，一邊在手指的第一關節處舔來舔去。`
- VN cũ: `「……Paulette.」`
- Sửa: `Vừa mút mát, vừa dai dẳng, chầm chậm——liếm láp phần gốc khớp ngón tay đầu tiên của tôi.`
- Lý do: Lệch vị trí (chuỗi xoay vòng C Alice (9)): VN cũ là bản dịch của JP ở key 1510; bản sửa là VN cũ của key 3156 — bản dịch đúng của JP dòng này. (đã bỏ khoảng trắng sau —— trong VN gốc, theo quy ước gạch ——)
**Key 1510 (双鉄)**
- JP: `「……ポーレット」`
- TW: `「……波萊特」`
- VN cũ: `「Ưm——ưm chụt——chụt——ưm, phù.\nÀ ừm……sao, thế ạ? Anh Soutetsu.」`
- Sửa: `「……Paulette.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng C Alice (9)): VN cũ là bản dịch của JP ở key 2279; bản sửa là VN cũ của key 3114 — bản dịch đúng của JP dòng này.
**Key 2279 (ポーレット)**
- JP: `「ん――んちゅ――ちゅぱ――ん、ぷぁ。\nえと……どう、しました？　双鉄くん」`
- TW: `「嗯——嗯啾——啾噗——嗯——噗。那個……怎麼了，雙鐵君」`
- VN cũ: `「Cho anh thêm miếng nữa đi——Lần này, hãy để anh ăn.」`
- Sửa: `「Ưm——ưm chụt——chụt——ưm, phù a. À ừm……sao, thế ạ? Anh Soutetsu.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng C Alice (9)): VN cũ là bản dịch của JP ở key 2110; bản sửa là VN cũ của key 1510 — bản dịch đúng của JP dòng này. (đã sửa "phù"→"phù a" — JP ぷぁ, theo quy ước file ふぁ→"phù a")
**Key 2110 (双鉄)**
- JP: `「おかわりを――今度は僕に、食べさせてくれ」`
- TW: `「再來一個——這次讓我再吃一個」`
- VN cũ: `「À ừm——ưm!?」`
- Sửa: `「Cho tôi thêm miếng nữa đi——Lần này, hãy để tôi ăn.」`
- Lý do: Lệch vị trí (cuối chuỗi xoay vòng C Alice (9)): VN cũ là bản dịch mồ côi, không có JP nào trong dự án khớp với nó; bản sửa là VN cũ của key 2279 — bản dịch đúng của JP dòng này. (đã sửa "anh"→"tôi" ×2 trong VN gốc — "anh" là Soutetsu tự xưng, JP 僕に)

#### Chuỗi D (cười/eclair) — 8 mắt xích (2776 → 3249)
**Key 2776 (ポーレット)**
- JP: `「えと――むぐっ！？」`
- TW: `「那個——唔！？」`
- VN cũ: `Tôi nhét chiếc bánh eclair mini vào đôi môi ướt át của Paulette.\nHá to miệng như một chú chim non, dùng ngón tay hối thúc.`
- Sửa: `「À ừm——múp!?」`
- Lý do: Lệch vị trí (đầu chuỗi xoay vòng D giggle/eclair (8)): VN cũ là bản dịch của JP ở key 3310; JP dòng này chưa có bản dịch đúng trong file — dịch mới từ JP.
**Key 3310 (monologue)**
- JP: `ポーレットの濡れた唇にミニエクレアをくわえさせ。\n雛鳥の如く自分の口を大きく開いて、指で促す。`
- TW: `我把迷你泡芙塞進了波萊特的小嘴裡，然後張開自己的嘴，用手指著，就像等待餵食的雛鳥一樣。`
- VN cũ: `「Ư hự hự, hự hự hự hự」`
- Sửa: `Tôi nhét chiếc bánh eclair mini vào đôi môi ướt át của Paulette. Há to miệng như một chú chim non, dùng ngón tay hối thúc.`
- Lý do: Lệch vị trí (chuỗi xoay vòng D giggle/eclair (8)): VN cũ là bản dịch của JP ở key 2370; bản sửa là VN cũ của key 2776 — bản dịch đúng của JP dòng này.
**Key 2370 (ポーレット)**
- JP: `「んふふ、ははひはひはぁ」`
- TW: `「嘿嘿，真沒辦法」`
- VN cũ: `Chỉ cắn đứt một nửa.`
- Sửa: `「Ừm fufu, haha hihi haa」`
- Lý do: Lệch vị trí (chuỗi xoay vòng D giggle/eclair (8)): VN cũ là bản dịch của JP ở key 3120; bản sửa là VN cũ của key 3310 — bản dịch đúng của JP dòng này.
**Key 3120 (monologue)**
- JP: `半分だけを噛みちぎり。`
- TW: `她咬下一半泡芙。`
- VN cũ: `Chóp chép, chóp chép, chầm chậm, chầm chậm,\nnhư đang trêu ngươi, nhai nghiền nát chiếc bánh eclair mini——`
- Sửa: `Chỉ cắn đứt một nửa.`
- Lý do: Lệch vị trí (chuỗi xoay vòng D giggle/eclair (8)): VN cũ là bản dịch của JP ở key 3529; bản sửa là VN cũ của key 2370 — bản dịch đúng của JP dòng này.
**Key 3529 (monologue)**
- JP: `ちゅく、ちゅくと、ゆっくりゆっくり、\n焦らすようにしてミニエクレアを噛みほぐし――`
- TW: `然後她慢慢地嚼著泡芙，故意讓我心急——`
- VN cũ: `「Ưm……」`
- Sửa: `Chóp chép, chóp chép, chầm chậm, chầm chậm, như đang trêu ngươi, nhai nghiền nát chiếc bánh eclair mini——`
- Lý do: Lệch vị trí (chuỗi xoay vòng D giggle/eclair (8)): VN cũ là bản dịch của JP ở key 2282; bản sửa là VN cũ của key 3120 — bản dịch đúng của JP dòng này.
**Key 2282 (ポーレット)**
- JP: `「ん……」`
- TW: `「嗯……」`
- VN cũ: `「Ưm——hự——」`
- Sửa: `「Ưm……」`
- Lý do: Lệch vị trí (chuỗi xoay vòng D giggle/eclair (8)): VN cũ là bản dịch của JP ở key 2273; bản sửa là VN cũ của key 3529 — bản dịch đúng của JP dòng này.
**Key 2273 (双鉄)**
- JP: `「ん――くっ――」`
- TW: `「嗯——唔——」`
- VN cũ: `Tôi ôm ghì lấy cô ấy.\nCảm giác như đang ôm một túi chườm nóng vậy. Thật ấm áp.`
- Sửa: `「Ưm——hự——」`
- Lý do: Lệch vị trí (chuỗi xoay vòng D giggle/eclair (8)): VN cũ là bản dịch của JP ở key 3249; bản sửa là VN cũ của key 2282 — bản dịch đúng của JP dòng này.
**Key 3249 (monologue)**
- JP: `抱き寄せる。\n湯たんぽを抱いているような気になる。あたたかだ。`
- TW: `我一下把她抱了過來。我感覺像是抱著暖水袋一樣，她身上暖暖的。`
- VN cũ: `「Ưm——ưm——ưm——」`
- Sửa: `Tôi ôm ghì lấy cô ấy. Cảm giác như đang ôm một túi chườm nóng vậy. Thật ấm áp.`
- Lý do: Lệch vị trí (cuối chuỗi xoay vòng D giggle/eclair (8)): VN cũ là bản dịch mồ côi, không có JP nào trong dự án khớp với nó; bản sửa là VN cũ của key 2273 — bản dịch đúng của JP dòng này.

#### Chuỗi E (bước chân/trà) — 7 mắt xích (2571 → 2817)
**Key 2571 (ポーレット)**
- JP: `「そうでした！　開けてみないと」`
- TW: `「是啊！快打開看看吧」`
- VN cũ: `Paulette hớn hở tháo lớp gói quà trang nhã.`
- Sửa: `「Đúng rồi! Phải mở ra xem mới được.」`
- Lý do: Lệch vị trí (đầu chuỗi xoay vòng E footsteps/tea (7)): VN cũ là bản dịch của JP ở key 3479; JP dòng này chưa có bản dịch đúng trong file — dịch mới từ JP.
**Key 3479 (monologue)**
- JP: `いそいそと、ポーレットが小洒落た包みを解いていく。`
- TW: `波萊特俐落地解開了漂亮的包裝布。`
- VN cũ: `「Oa, hồng trà Fauchon và bánh eclair mini này!\nVui quá, mẹ vẫn còn nhớ.」`
- Sửa: `Paulette hớn hở tháo lớp gói quà trang nhã.`
- Lý do: Lệch vị trí (chuỗi xoay vòng E footsteps/tea (7)): VN cũ là bản dịch của JP ở key 2177; bản sửa là VN cũ của key 2571 — bản dịch đúng của JP dòng này.
**Key 2177 (ポーレット)**
- JP: `「わぁあ、フォトンの紅茶とミニエクレア！\n嬉しい、ママ、覚えててくれたんだ」`
- TW: `「哇，是福頓的紅茶和迷你泡芙！我好高興，媽媽還記得呢」`
- VN cũ: `「Là món em thích sao?」`
- Sửa: `「Oa, hồng trà Fauchon và bánh eclair mini này! Vui quá, mẹ vẫn còn nhớ.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng E footsteps/tea (7)): VN cũ là bản dịch của JP ở key 2560; bản sửa là VN cũ của key 3479 — bản dịch đúng của JP dòng này.
**Key 2560 (双鉄)**
- JP: `「好物なのか？」`
- TW: `「是你愛吃的東西嗎？」`
- VN cũ: `「Thích từ hồi còn bé tí luôn ấy chứ!\nAnh đợi một lát nhé. Em đi pha ngay đây.」`
- Sửa: `「Là món em thích sao?」`
- Lý do: Lệch vị trí (chuỗi xoay vòng E footsteps/tea (7)): VN cũ là bản dịch của JP ở key 2505; bản sửa là VN cũ của key 2177 — bản dịch đúng của JP dòng này.
**Key 2505 (ポーレット)**
- JP: `「それはもう、ちっちゃいころから！\n待ってて下さい。すぐ淹れますね」`
- TW: `「我從小就愛吃！你等一下，我去泡茶」`
- VN cũ: `Lạch bạch lạch bạch, đến cả tiếng bước chân cũng rộn rã.`
- Sửa: `「Thích từ hồi còn bé tí luôn ấy chứ! Anh đợi một lát nhé. Em đi pha ngay đây.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng E footsteps/tea (7)): VN cũ là bản dịch của JP ở key 3170; bản sửa là VN cũ của key 2560 — bản dịch đúng của JP dòng này.
**Key 3170 (monologue)**
- JP: `パタパタと、足音までもが弾んでいる。`
- TW: `她的腳步聲跟說話聲一樣輕快。`
- VN cũ: `「Vì là trà Assam,\nnên em đề cử pha trà sữa nhé——」`
- Sửa: `Lạch bạch lạch bạch, đến cả tiếng bước chân cũng rộn rã.`
- Lý do: Lệch vị trí (chuỗi xoay vòng E footsteps/tea (7)): VN cũ là bản dịch của JP ở key 2817; bản sửa là VN cũ của key 2505 — bản dịch đúng của JP dòng này.
**Key 2817 (ポーレット)**
- JP: `「アッサムだから、\nミルクティーがおすすめですけどー」`
- TW: `「阿薩姆的話，我推薦奶茶——」`
- VN cũ: `「Vậy thì, pha như thế đi.」`
- Sửa: `「Vì là trà Assam, nên em đề cử pha trà sữa nhé——」`
- Lý do: Lệch vị trí (cuối chuỗi xoay vòng E footsteps/tea (7)): VN cũ là bản dịch mồ côi, không có JP nào trong dự án khớp với nó; bản sửa là VN cũ của key 3170 — bản dịch đúng của JP dòng này.

#### Chuỗi F (váy) — 13 mắt xích (2185 → 2608)
**Key 2185 (ポーレット)**
- JP: `「ふえっ！？」`
- TW: `「哎！？」`
- VN cũ: `——Nguy hiểm, quá.\nTôi lùi về phía giường để tạo khoảng cách, chật vật lắm mới kìm lại được.`
- Sửa: `「Phê!?」`
- Lý do: Lệch vị trí (đầu chuỗi xoay vòng F dress (13)): VN cũ là bản dịch của JP ở key 3183; JP dòng này chưa có bản dịch đúng trong file — dịch mới từ JP.
**Key 3183 (monologue)**
- JP: `――危う、かった。\nベッドに退避し距離を稼いで、なんとか防げた。`
- TW: `好危險。我退到了床那邊，才制止自己做出出格的舉動。`
- VN cũ: `「À, ừm……」`
- Sửa: `——Nguy hiểm, quá. Tôi lùi về phía giường để tạo khoảng cách, chật vật lắm mới kìm lại được.`
- Lý do: Lệch vị trí (chuỗi xoay vòng F dress (13)): VN cũ là bản dịch của JP ở key 2777; bản sửa là VN cũ của key 2185 — bản dịch đúng của JP dòng này.
**Key 2777 (ポーレット)**
- JP: `「え、と……」`
- TW: `「那個……」`
- VN cũ: `Đưa mắt nhìn xuống khuôn mặt có vẻ bối rối kia,\nPaulette đang tròn xoe mắt nhìn tôi.`
- Sửa: `「À, ừm……」`
- Lý do: Lệch vị trí (chuỗi xoay vòng F dress (13)): VN cũ là bản dịch của JP ở key 3343; bản sửa là VN cũ của key 3183 — bản dịch đúng của JP dòng này.
**Key 3343 (monologue)**
- JP: `困ったような顔に視線をおろしていけば、\nポーレットは、目を丸くして僕を見ている。`
- TW: `我看向一臉困惑的波萊特，只見她瞪大了眼睛盯著我的下半身。`
- VN cũ: `「Không——Anh nghĩ làm bẩn bằng nước bọt thì có lỗi lắm.」`
- Sửa: `Đưa mắt nhìn xuống khuôn mặt có vẻ bối rối kia, Paulette đang tròn xoe mắt nhìn tôi.`
- Lý do: Lệch vị trí (chuỗi xoay vòng F dress (13)): VN cũ là bản dịch của JP ở key 2150; bản sửa là VN cũ của key 2777 — bản dịch đúng của JP dòng này.
**Key 2150 (双鉄)**
- JP: `「いや――よだれで汚しては申し訳ないと思ってな」`
- TW: `「呃，我想要是把衣服弄髒就不好了」`
- VN cũ: `Nương theo ánh mắt của tôi,\nPaulette cũng cúi xuống nhìn cơ thể mình, nhìn bầu ngực mình.`
- Sửa: `「Không——Tôi nghĩ làm bẩn bằng nước bọt thì có lỗi lắm.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng F dress (13)): VN cũ là bản dịch của JP ở key 3606; bản sửa là VN cũ của key 3343 — bản dịch đúng của JP dòng này. (đã sửa "Anh"→"Tôi" trong VN gốc vì đó là lỗi xưng hô của dòng cho)
**Key 3606 (monologue)**
- JP: `僕の視線を追いかけて、\nポーレットも自分の体を、胸もとを見下ろす。`
- TW: `見我看向她，波萊特也低頭看著自己，看向自己的胸前。`
- VN cũ: `「Chiếc váy mẹ vợ cất công may cho mà.」`
- Sửa: `Nương theo ánh mắt của tôi, Paulette cũng cúi xuống nhìn cơ thể mình, nhìn bầu ngực mình.`
- Lý do: Lệch vị trí (chuỗi xoay vòng F dress (13)): VN cũ là bản dịch của JP ở key 2755; bản sửa là VN cũ của key 2150 — bản dịch đúng của JP dòng này.
**Key 2755 (双鉄)**
- JP: `「せっかく、お義母様が作って下さったドレスだ」`
- TW: `「這可是岳母大人給你做的寶貴衣服」`
- VN cũ: `「Ư hự hự. Cảm ơn anh.\nNhưng mà——nhé? Anh Soutetsu.」`
- Sửa: `「Chiếc váy mẹ vợ cất công may cho mà.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng F dress (13)): VN cũ là bản dịch của JP ở key 2356; bản sửa là VN cũ của key 3606 — bản dịch đúng của JP dòng này.
**Key 2356 (ポーレット)**
- JP: `「うふふっ。ありがとうございます。\nだけど――ですね？　双鉄くん」`
- TW: `「嘻嘻，謝謝你。不過呢，雙鐵君——」`
- VN cũ: `（Tuột——）`
- Sửa: `「Ufufu. Cảm ơn anh. Nhưng mà——nhé? Anh Soutetsu.」`
- Lý do: Lệch vị trí (chuỗi xoay vòng F dress (13)): VN cũ là bản dịch của JP ở key 3757; bản sửa là VN cũ của key 2755 — bản dịch đúng của JP dòng này.
**Key 3757 (monologue)**
- JP: `（しゅるっ――）`
- TW: `（脫下）`
- VN cũ: `Paulette cởi tạp dề ra, gấp lại.\nVà rồi, cứ thế——`
- Sửa: `（Tuột——）`
- Lý do: Lệch vị trí (chuỗi xoay vòng F dress (13)): VN cũ là bản dịch của JP ở key 3507; bản sửa là VN cũ của key 2356 — bản dịch đúng của JP dòng này.
**Key 3507 (monologue)**
- JP: `ポーレットがエプロンを外して、たたむ。\nそうして、そのまま――`
- TW: `波萊特脫下圍裙，疊了起來。然後她就直接——`
- VN cũ: `（Tách——tách——）`
- Sửa: `Paulette cởi tạp dề ra, gấp lại. Và rồi, cứ thế——`
- Lý do: Lệch vị trí (chuỗi xoay vòng F dress (13)): VN cũ là bản dịch của JP ở key 3760; bản sửa là VN cũ của key 3757 — bản dịch đúng của JP dòng này.
**Key 3760 (monologue)**
- JP: `（ぷち――ぷちっ――）`
- TW: `（解開鈕扣）`
- VN cũ: `「Paulette?」`
- Sửa: `（Tách——tách——）`
- Lý do: Lệch vị trí (chuỗi xoay vòng F dress (13)): VN cũ là bản dịch của JP ở key 2629; bản sửa là VN cũ của key 3507 — bản dịch đúng của JP dòng này.
**Key 2629 (双鉄)**
- JP: `「ポーレット？」`
- TW: `「波萊特？」`
- VN cũ: `「『Vì vậy』, làm bẩn cũng không sao.\nVì đây là bộ quần áo mẹ làm riêng cho em mà.」`
- Sửa: `「Paulette?」`
- Lý do: Lệch vị trí (chuỗi xoay vòng F dress (13)): VN cũ là bản dịch của JP ở key 2608; bản sửa là VN cũ của key 3760 — bản dịch đúng của JP dòng này.
**Key 2608 (ポーレット)**
- JP: `「『だから』、汚してもいいんです。\nママが、わたしのために作ってくれた服だから」`
- TW: `「正因為如此，弄髒也沒關係。正因為是媽媽給我做的衣服才沒關係」`
- VN cũ: `「Hả?」`
- Sửa: `「『Vì vậy』, làm bẩn cũng không sao. Vì đây là bộ quần áo mẹ làm riêng cho em mà.」`
- Lý do: Lệch vị trí (cuối chuỗi xoay vòng F dress (13)): VN cũ là bản dịch mồ côi, không có JP nào trong dự án khớp với nó; bản sửa là VN cũ của key 2629 — bản dịch đúng của JP dòng này.

### Xưng hô — Soutetsu tự xưng "anh" trong thoại (36 dòng)
**Key 1513 (双鉄)**
- JP: `「……本当にお疲れ様だ。素晴らしかった。\nこの上ないプロモーションになったと思う」`
- TW: `「……真的辛苦你了，簡直完美。我覺得沒有什麼宣傳能比這個更好」`
- VN cũ: `「……Em thực sự vất vả rồi. Tuyệt vời lắm.\nAnh nghĩ đây là một chiến dịch quảng bá không thể nào tốt hơn được nữa.」`
- Sửa: `「……Em thực sự vất vả rồi. Tuyệt vời lắm. Tôi nghĩ đây là một chiến dịch quảng bá không thể nào tốt hơn được nữa.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 1516 (双鉄)**
- JP: `「……予算や設備の都合もあろうが、僕としては、\n『世界各国の絵本と触れ合える』程度は必要かと思う」`
- TW: `「……肯定會有預算和設備上的限制，但我還是覺得有必要做到“能接觸到世界各國的繪本”」`
- VN cũ: `「……Dù sẽ có những hạn chế về ngân sách và cơ sở vật chất, nhưng theo anh,\nít nhất cũng cần phải đạt đến mức 『Có thể tiếp xúc với truyện tranh từ khắp nơi trên thế giới』.」`
- Sửa: `「……Dù sẽ có những hạn chế về ngân sách và cơ sở vật chất, nhưng theo tôi, ít nhất cũng cần phải đạt đến mức 『Có thể tiếp xúc với truyện tranh từ khắp nơi trên thế giới』.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2047 (双鉄)**
- JP: `「なんだかんだいっても僕は酒蔵の養子だからな。\n酒のことには、多少は詳しい」`
- TW: `「不管怎麼說我也是酒廠家的養子。關於酒這方面還是了解一點」`
- VN cũ: `「Nói gì thì nói, anh cũng là con nuôi của xưởng rượu mà.\nNên anh cũng biết đôi chút về rượu.」`
- Sửa: `「Nói gì thì nói, tôi cũng là con nuôi của xưởng rượu mà. Nên tôi cũng biết đôi chút về rượu.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2080 (双鉄)**
- JP: `「イって――いい――くっ――僕も――すぐっ」`
- TW: `「你就——高潮吧——我也——很快要——」`
- VN cũ: `「Cứ lên đỉnh——đi——ư——anh cũng——sắp rồi」`
- Sửa: `「Cứ lên đỉnh——đi——ư——tôi cũng——sắp rồi」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2089 (双鉄)**
- JP: `「さ、つづきだ。\nせっかくだ。最後まで読んでくれ」`
- TW: `「來，繼續吧。機會難得，就一直讀到最後吧」`
- VN cũ: `「Nào, tiếp tục thôi.\nCất công rồi, hãy đọc cho anh nghe đến cuối đi.」`
- Sửa: `「Nào, tiếp tục thôi. Cất công rồi, hãy đọc cho tôi nghe đến cuối đi.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2327 (双鉄)**
- JP: `「ああ。望むところだ。\n今日すぐにでも、まだ頑張れるぞ」`
- TW: `「嗯，我求之不得。今天我還能再努力一下」`
- VN cũ: `「Ừ. Anh cầu còn không được.\nNgay hôm nay, anh vẫn còn có thể cố gắng tiếp đấy.」`
- Sửa: `「Ừ. Tôi cầu còn không được. Ngay hôm nay, tôi vẫn còn có thể cố gắng tiếp đấy.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2329 (双鉄)**
- JP: `「ああ、さして強くない僕でも楽しめる、\n飲みくちのよい、軽いワインだ」`
- TW: `「嗯，我這種不會喝酒的人也能品嘗，是一種口味很輕的葡萄酒」`
- VN cũ: `「Ừ, một người tửu lượng kém như anh cũng có thể thưởng thức,\nlà loại rượu vang nhẹ, rất dễ uống.」`
- Sửa: `「Ừ, một người tửu lượng kém như tôi cũng có thể thưởng thức, là loại rượu vang nhẹ, rất dễ uống.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2338 (双鉄)**
- JP: `「ああ、喜んで見せてもらおう」`
- TW: `「嗯，那我就看看吧」`
- VN cũ: `「Ừ, anh rất sẵn lòng chiêm ngưỡng.」`
- Sửa: `「Ừ, tôi rất sẵn lòng chiêm ngưỡng.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2343 (双鉄)**
- JP: `「うむ？　抱くことが染めることとは感じるが――\n抱くだけではなく、染める、とは？」`
- TW: `「嗯？親熱不就有這個意思了嗎，不僅是親熱還要染色是什麼意思？」`
- VN cũ: `「Hửm? Anh cứ nghĩ ôm ấp chính là nhuộm màu rồi chứ——\nKhông chỉ ôm ấp, mà là nhuộm màu, nghĩa là sao?」`
- Sửa: `「Hửm? Tôi cứ nghĩ ôm ấp chính là nhuộm màu rồi chứ——Không chỉ ôm ấp, mà là nhuộm màu, nghĩa là sao?」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2421 (双鉄)**
- JP: `「ポーレットの足踏みワインなら、是非飲みたい」`
- TW: `「如果是你做的腳踩葡萄酒的話，那我真想嘗一嘗」`
- VN cũ: `「Nếu là rượu vang do Paulette giẫm chân làm ra, anh nhất định muốn uống thử.」`
- Sửa: `「Nếu là rượu vang do Paulette giẫm chân làm ra, tôi nhất định muốn uống thử.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2474 (双鉄)**
- JP: `「わからんな。もっとハッキリ言ってくれ。\nポーレットのどこを、僕の何で、染めてほしいのか」`
- TW: `「我不懂啊，你說清楚一點。你想讓我在你的哪裡染上顏色？」`
- VN cũ: `「Anh không hiểu. Nói rõ hơn cho anh nghe đi.\nEm muốn anh nhuộm phần nào của Paulette, bằng cái gì của anh?」`
- Sửa: `「Tôi không hiểu. Nói rõ hơn cho tôi nghe đi. Em muốn tôi nhuộm phần nào của Paulette, bằng cái gì của tôi?」`
- Lý do: Soutetsu tự xưng "anh" ×2 trong thoại (JP ポーレットのどこを、僕の何で) → "Tôi" ×2.
**Key 2489 (双鉄)**
- JP: `「婚約者同士の話が楽しく、弾みすぎただけのことだ。\nごめんなさいというのなら、僕も同罪になるぞ？」`
- TW: `「我們只是未婚夫妻之間開心地閒聊了一會。你要是道歉的話，我也有罪了」`
- VN cũ: `「Chỉ là câu chuyện giữa những người đã đính hôn quá vui vẻ, nên mới đi xa thôi.\nNếu em xin lỗi, thì anh cũng mang tội chung đấy nhé?」`
- Sửa: `「Chỉ là câu chuyện giữa những người đã đính hôn quá vui vẻ, nên mới đi xa thôi. Nếu em xin lỗi, thì tôi cũng mang tội chung đấy nhé?」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2504 (双鉄)**
- JP: `「楽しみだ」`
- TW: `「我很期待」`
- VN cũ: `「Anh rất mong chờ đấy.」`
- Sửa: `「Tôi rất mong chờ đấy.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2512 (双鉄)**
- JP: `「僕は、ポーレットをいっぱいに――\n夢中にさせたくて動いてる」`
- TW: `「我是為了讓你眼裡只有我在動」`
- VN cũ: `「Anh đang chuyển động, để khiến Paulette tràn ngập——\nsay đắm anh đấy.」`
- Sửa: `「Tôi đang chuyển động, để khiến Paulette tràn ngập——say đắm tôi đấy.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2517 (双鉄)**
- JP: `「補い合うために僕がいる。細部にとらわれず、\nポーレットにはポーレットの着想を伸ばしてほしい」`
- TW: `「我會幫忙完善。你不用在意細節，只管豐富你的想法就行了」`
- VN cũ: `「Có anh ở đây để bù đắp cho em mà. Đừng bận tâm đến những tiểu tiết,\nanh muốn Paulette cứ phát huy ý tưởng của Paulette đi.」`
- Sửa: `「Có tôi ở đây để bù đắp cho em mà. Đừng bận tâm đến những tiểu tiết, tôi muốn Paulette cứ phát huy ý tưởng của Paulette đi.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP 補い合うために僕がいる) → "Tôi".
**Key 2518 (双鉄)**
- JP: `「染め抜いて、上書きをして、マーキングする」`
- TW: `「我會把你染上顏色，覆蓋過去的痕跡，標上我的印記」`
- VN cũ: `「Anh sẽ nhuộm thắm, ghi đè lên, và đánh dấu.」`
- Sửa: `「Tôi sẽ nhuộm thắm, ghi đè lên, và đánh dấu.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2520 (双鉄)**
- JP: `「僕の、勃起は――おちんちんさんは――\nポーレットの、乳首を、ちゅうちゅう、したいっ」`
- TW: `「我的肉棒——我的雞雞先生——想親親你的乳頭」`
- VN cũ: `「Sự cương cứng của anh——dương vật của anh——\nmuốn, mút mút, nhũ hoa, của Paulette.」`
- Sửa: `「Sự cương cứng của tôi——dương vật của tôi——muốn, mút mút, nhũ hoa, của Paulette.」`
- Lý do: Soutetsu tự xưng "anh" ×2 trong thoại (JP 僕の、勃起は――おちんちんさんは) → "Tôi" ×2.
**Key 2524 (双鉄)**
- JP: `「僕も――ポーレットでいっぱいだ」`
- TW: `「我眼裡也只有你了」`
- VN cũ: `「Anh cũng——tràn ngập Paulette rồi.」`
- Sửa: `「Tôi cũng——tràn ngập Paulette rồi.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2529 (双鉄)**
- JP: `「ポーレットは僕のおんなだと、僕のものだと。\n全身すべて、骨にも、こころにも、染み込ませよう」`
- TW: `「我要宣示你是我的女人，是我的所有物。我要把你的全身，把你的骨肉，把你的心靈，全染上我的顏色」`
- VN cũ: `「Để khẳng định Paulette là người phụ nữ của anh, là của riêng anh.\nAnh sẽ để nó thấm sâu vào toàn bộ cơ thể, vào tận xương tủy, và cả trái tim em.」`
- Sửa: `「Để khẳng định Paulette là người phụ nữ của tôi, là của riêng tôi. Tôi sẽ để nó thấm sâu vào toàn bộ cơ thể, vào tận xương tủy, và cả trái tim em.」`
- Lý do: Soutetsu tự xưng "anh" ×2 trong thoại (JP ポーレットは僕のおんなだと、僕のものだと) → "Tôi" ×2.
**Key 2530 (双鉄)**
- JP: `「極上のイベント列車だったと思う。まさに適材適所。\n僕も、その一員を務めることができ、光栄だ」`
- TW: `「我覺得這個特別列車辦得真是太好了，真是物盡其用。我能作為一員參與其中，感覺很光榮」`
- VN cũ: `「Anh nghĩ đây là một chuyến tàu sự kiện cực kỳ xuất sắc. Đúng là dụng nhân như dụng mộc.\nAnh cũng rất vinh dự khi được đóng góp một phần vào đó.」`
- Sửa: `「Tôi nghĩ đây là một chuyến tàu sự kiện cực kỳ xuất sắc. Đúng là dụng nhân như dụng mộc. Tôi cũng rất vinh dự khi được đóng góp một phần vào đó.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2552 (双鉄)**
- JP: `「僕の、好きにか？」`
- TW: `「換我了嗎？」`
- VN cũ: `「Đến lượt anh, làm theo ý thích sao?」`
- Sửa: `「Đến lượt tôi, làm theo ý thích sao?」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2554 (双鉄)**
- JP: `「お話ももちろんだが、朗読がよかった。\n声の雨が、僕を、物語にひたしてくれた」`
- TW: `「故事當然有意思，不過你的朗讀也非常棒。聲音營造出的雨讓我完全沉浸在故事裡了」`
- VN cũ: `「Câu chuyện hay là đương nhiên rồi, nhưng cách em đọc cũng rất tuyệt.\nCơn mưa bằng giọng nói của em đã nhấn chìm anh vào câu chuyện.」`
- Sửa: `「Câu chuyện hay là đương nhiên rồi, nhưng cách em đọc cũng rất tuyệt. Cơn mưa bằng giọng nói của em đã nhấn chìm tôi vào câu chuyện.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2559 (双鉄)**
- JP: `「心得た」`
- TW: `「明白」`
- VN cũ: `「Anh hiểu rồi.」`
- Sửa: `「Tôi hiểu rồi.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2586 (双鉄)**
- JP: `「好みもあろうが、間違いなく質は高い。\n僕としては、特に赤がいい。馬サシとの相性は抜群だ」`
- TW: `「有我個人喜好的因素在裡面，不過客觀來講品質也很好。我特別喜歡紅酒，跟馬肉刺身非常搭」`
- VN cũ: `「Tuy còn tùy khẩu vị, nhưng chất lượng thì miễn chê.\nCá nhân anh đặc biệt thích rượu vang đỏ. Cực kỳ hợp với thịt ngựa sống luôn.」`
- Sửa: `「Tuy còn tùy khẩu vị, nhưng chất lượng thì miễn chê. Cá nhân tôi đặc biệt thích rượu vang đỏ. Cực kỳ hợp với thịt ngựa sống luôn.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2614 (双鉄)**
- JP: `「違ってはいない。メルヘン、という感じはする。\n大変に可愛らしいし、好きか嫌いかでいえば大好きだ」`
- TW: `「沒有不對勁，看起來非常有童話風。真的非常可愛，要說的話我很喜歡」`
- VN cũ: `「Không sai đâu. Mang lại cảm giác rất cổ tích.\nCực kỳ đáng yêu, nếu hỏi thích hay không thì anh rất thích.」`
- Sửa: `「Không sai đâu. Mang lại cảm giác rất cổ tích. Cực kỳ đáng yêu, nếu hỏi thích hay không thì tôi rất thích.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2661 (双鉄)**
- JP: `「もう鬼籍に入られているのか。\n残念だな、一度お会いしてみたかった」`
- TW: `「真遺憾，他已經去世了。我真想見見他」`
- VN cũ: `「Thầy ấy đã qua đời rồi sao.\nTiếc thật, anh rất muốn được gặp thầy một lần.」`
- Sửa: `「Thầy ấy đã qua đời rồi sao. Tiếc thật, tôi rất muốn được gặp thầy một lần.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2686 (双鉄)**
- JP: `「僕に？」`
- TW: `「被我？」`
- VN cũ: `「Bị anh?」`
- Sửa: `「Bị tôi?」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2693 (双鉄)**
- JP: `「するか？　おんぶ」`
- TW: `「要我背你嗎？」`
- VN cũ: `「Anh cõng em nhé?」`
- Sửa: `「Tôi cõng em nhé?」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2695 (双鉄)**
- JP: `「れいなにもナイショであるなら、\n御一夜鉄道最高機密のひとつだな――心得た」`
- TW: `「要是對玲奈都保密的話，這就是御一夜鐵道的最高機密之一了——我知道了」`
- VN cũ: `「Nếu phải giữ bí mật với cả Reina,\nthì đây là một trong những bí mật tối cao của Đường sắt Ohimitera rồi——Anh hiểu.」`
- Sửa: `「Nếu phải giữ bí mật với cả Reina, thì đây là một trong những bí mật tối cao của Đường sắt Ohitoyo rồi——Tôi hiểu.」`
- Lý do: Soutetsu tự xưng "Anh" trong thoại (JP 心得た) → "Tôi"; đồng thời sửa Ohimitera→Ohitoyo.
**Key 2751 (双鉄)**
- JP: `「ポーレットを染め抜くための精液だ。\n僕ではなく、ポーレットの意思で絞り出してほしい」`
- TW: `「這些精液是給你染色用的。那就不要按我的喜好，用你想要的方法把它榨出來吧」`
- VN cũ: `「Đây là tinh dịch dùng để nhuộm thắm Paulette.\nAnh muốn em tự vắt kiệt nó theo ý mình, chứ không phải ý anh.」`
- Sửa: `「Đây là tinh dịch dùng để nhuộm thắm Paulette. Tôi muốn em tự vắt kiệt nó theo ý mình, chứ không phải ý tôi.」`
- Lý do: Soutetsu tự xưng "Anh" trong thoại (JP 僕ではなく、ポーレットの意思で) → "Tôi".
**Key 2764 (双鉄)**
- JP: `「僕も一乗客になり、気動車の国のアリスに\nおもてなししてほしいと思ったほどだ。最高だった」`
- TW: `「連我都想變成乘客，讓內燃機車之國的愛麗絲招待我一下。真的是太棒了」`
- VN cũ: `「Đến mức anh cũng muốn trở thành một hành khách,\nđể được Alice ở xứ sở toa xe tự hành thiết đãi đấy. Tuyệt vời lắm.」`
- Sửa: `「Đến mức tôi cũng muốn trở thành một hành khách, để được Alice ở xứ sở toa xe tự hành thiết đãi đấy. Tuyệt vời lắm.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2783 (双鉄)**
- JP: `「それは困るな。\nなら、大人しく聞くとしよう。説明をあらためて頼む」`
- TW: `「那可就麻煩了。那我就聽你說吧，請你做一下說明」`
- VN cũ: `「Vậy thì rắc rối đấy.\nThế thì anh sẽ ngoan ngoãn lắng nghe. Nhờ em giải thích lại nhé.」`
- Sửa: `「Vậy thì rắc rối đấy. Thế thì tôi sẽ ngoan ngoãn lắng nghe. Nhờ em giải thích lại nhé.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2788 (双鉄)**
- JP: `「僕の好みも、正攻法でな」`
- TW: `「那就用我喜歡的正面攻擊」`
- VN cũ: `「Sở thích của anh, cũng là đánh trực diện mà.」`
- Sửa: `「Sở thích của tôi, cũng là đánh trực diện mà.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2794 (双鉄)**
- JP: `「ならば、是非。手に入れるので、一緒に飲もう」`
- TW: `「那就試試吧。我去買來，我們一起喝」`
- VN cũ: `「Vậy thì nhất định rồi. Anh sẽ mua về, chúng ta cùng uống nhé.」`
- Sửa: `「Vậy thì nhất định rồi. Tôi sẽ mua về, chúng ta cùng uống nhé.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2798 (双鉄)**
- JP: `「で、あれば、和風に寄せるのには反対だ。\n地元対策になるかもしれんが、観光アピールが弱まる」`
- TW: `「那我就反對偏向日式風格了。這對說服當地人可能有用，但是作為旅遊資源來說就太弱了」`
- VN cũ: `「Nếu vậy thì anh phản đối việc thiên về phong cách Nhật Bản.\nCó thể nó sẽ là đối sách tốt với địa phương, nhưng sức hút du lịch sẽ bị giảm sút.」`
- Sửa: `「Nếu vậy thì tôi phản đối việc thiên về phong cách Nhật Bản. Có thể nó sẽ là đối sách tốt với địa phương, nhưng sức hút du lịch sẽ bị giảm sút.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".
**Key 2800 (双鉄)**
- JP: `「ならば、機を見て僕にもご挨拶させてくれ」`
- TW: `「那有機會我也問候一下」`
- VN cũ: `「Nếu vậy, khi có dịp hãy cho anh gửi lời chào hỏi nhé.」`
- Sửa: `「Nếu vậy, khi có dịp hãy cho tôi gửi lời chào hỏi nhé.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP: chủ ngữ là Soutetsu, 僕) → "Tôi".

### Thuật ngữ — Ohimitera → Ohitoyo (6 dòng)
**Key 2125 (双鉄)**
- JP: `「『足踏みワイン体験』単体ではもったいない。\n御一夜にはクマ焼酎というブランドがあるのだから」`
- TW: `「只做“腳踩製酒體驗”就太浪費了。御一夜有隈燒酒這個品牌」`
- VN cũ: `「Chỉ tổ chức 『Trải nghiệm làm rượu vang bằng chân』 không thôi thì phí quá.\nOhimitera vốn có thương hiệu rượu Shochu Kuma mà.」`
- Sửa: `「Chỉ tổ chức 『Trải nghiệm làm rượu vang bằng chân』 không thôi thì phí quá. Ohitoyo vốn có thương hiệu rượu Shochu Kuma mà.」`
- Lý do: 御一夜 bị dịch "Ohimitera" — theo quyết định 19/11 phải là "Ohitoyo".
**Key 2300 (双鉄)**
- JP: `「うむ。御一夜駅-マイントレジャー駅間のみの\n利用者が多すぎるのは、確かにかなりもったいない」`
- TW: `「嗯。現在只有從御一夜站到煤探樂園站的乘客比較多，這樣實在是很浪費」`
- VN cũ: `「Ừm. Quả thực rất lãng phí khi lượng hành khách\nchỉ tập trung ở đoạn ga Ohimitera đến ga Mine Treasure.」`
- Sửa: `「Ừm. Quả thực rất lãng phí khi lượng hành khách chỉ tập trung ở đoạn ga Ohitoyo đến ga Mine Treasure.」`
- Lý do: 御一夜 bị dịch "Ohimitera" — theo quyết định 19/11 phải là "Ohitoyo".
**Key 2314 (双鉄)**
- JP: `「ああ、御一夜の酒蔵関係者や、\n湯医の絵本館の関係者を一同に集めてだ」`
- TW: `「嗯，可以讓御一夜的酒廠相關人員，還有湯醫的繪本館的人員都聚在一起」`
- VN cũ: `「Ừ, tập hợp những người liên quan đến xưởng rượu ở Ohimitera,\nvà những người liên quan đến thư viện truyện tranh Yunosaka lại với nhau.」`
- Sửa: `「Ừ, tập hợp những người liên quan đến xưởng rượu ở Ohitoyo, và những người liên quan đến thư viện truyện tranh Yunosaka lại với nhau.」`
- Lý do: 御一夜 bị dịch "Ohimitera" — theo quyết định 19/11 phải là "Ohitoyo".
**Key 2436 (双鉄)**
- JP: `「うむ。御一夜は酒造りの町だし――\n隈元には、ぶどう農園もワイナリーもある」`
- TW: `「對。御一夜本來就是產酒的地方——隈元有葡萄園，也有葡萄酒廠」`
- VN cũ: `「Ừm. Ohimitera vốn là thị trấn nấu rượu mà——\nỞ Kumamoto cũng có cả vườn nho lẫn xưởng rượu vang.」`
- Sửa: `「Ừm. Ohitoyo vốn là thị trấn nấu rượu mà——Ở Kumamoto cũng có cả vườn nho lẫn xưởng rượu vang.」`
- Lý do: 御一夜 bị dịch "Ohimitera" — theo quyết định 19/11 phải là "Ohitoyo".
**Key 2566 (ポーレット)**
- JP: `「ですよね。湯医ローカルな施設にしちゃったら、\n御一夜鉄道的には、ほとんど利益を生めませんよね」`
- TW: `「是啊。如果變成湯醫本地用的設施的話，御一夜鐵道方面就沒有收益了」`
- VN cũ: `「Đúng vậy nhỉ. Nếu chỉ biến nó thành cơ sở mang tính địa phương của Yunosaka,\nthì xét về mặt Đường sắt Ohimitera, hầu như sẽ chẳng sinh ra lợi nhuận gì.」`
- Sửa: `「Đúng vậy nhỉ. Nếu chỉ biến nó thành cơ sở mang tính địa phương của Yunosaka, thì xét về mặt Đường sắt Ohitoyo, hầu như sẽ chẳng sinh ra lợi nhuận gì.」`
- Lý do: 御一夜 bị dịch "Ohimitera" — theo quyết định 19/11 phải là "Ohitoyo".
**Key 2647 (ポーレット)**
- JP: `「現状、湯医方面における観光要素の弱さの克服が、\n御一夜鉄道の更なる改善へのカギになってますよね？」`
- TW: `「現在克服湯醫方面觀光要素太少的問題，就是改善御一夜鐵道的關鍵，我說的沒錯吧？」`
- VN cũ: `「Hiện tại, việc khắc phục sự yếu kém về yếu tố du lịch ở khu vực Yunosaka,\nchính là chìa khóa để cải thiện Đường sắt Ohimitera hơn nữa đúng không anh?」`
- Sửa: `「Hiện tại, việc khắc phục sự yếu kém về yếu tố du lịch ở khu vực Yunosaka, chính là chìa khóa để cải thiện Đường sắt Ohitoyo hơn nữa đúng không anh?」`
- Lý do: 御一夜 bị dịch "Ohimitera" — theo quyết định 19/11 phải là "Ohitoyo".

### Tiếng thở để nguyên dạng La-tinh (11 dòng)
**Key 2132 (ポーレット)**
- JP: `「ひゅあぁぁぁぁぁぁぁぁぁぁぁぁぁぁんっ！！！」`
- TW: `「呀啊啊啊啊啊！！！」`
- VN cũ: `「Hyuaaaaaaaaaaaaaaaan!!!」`
- Sửa: `「Híuaaaaaaaaaaaaaaan!!!」`
- Lý do: JP ひゅあぁぁぁぁぁぁぁぁぁぁぁぁぁぁんっ (15 あ/ぁ) bị phiên âm "Hyua…an" — Việt hoá: "Híu" + 15 chữ a + "n!!!" (đã đếm bằng script: đúng 15 a).
**Key 2136 (ポーレット)**
- JP: `「ひあっ！？」`
- TW: `「呀！？」`
- VN cũ: `「Hya!?」`
- Sửa: `「Hia!?」`
- Lý do: JP ひあっ bị dịch "Hya" — sai âm: ひあ là "Hia", không phải ひゃ "Hya" — sửa thành "Hia!?".
**Key 2137 (ポーレット)**
- JP: `「ひゃうっ！？　あっ――ふっ――く、あっ――\nわたっ――わたし――イッた――イっ、ってっ！」`
- TW: `「呀！？啊——呼——啊——我——我——丟了——丟了！」`
- VN cũ: `「Hya!? A——phù——ư, a——\nem——em——lên đỉnh——lên đỉnh, rồi mà!」`
- Sửa: `「Hiau!? A——phù——ư, a——em——em——lên đỉnh——lên đỉnh, rồi mà!」`
- Lý do: JP ひゃうっ bị dịch "Hya" (mất âm う) — Việt hoá "Hiau" (tiền lệ h1/h2: ひゃう→"Hiau").
**Key 2139 (ポーレット)**
- JP: `「きゃふっ！？　はっ！　ああっ――早い、のっ――\nんっっ――ふあっ――もっと、これ、腰、ずれ、てっ」`
- TW: `「呀！？啊！啊——好快——嗯——呼啊——再來、這樣、腰會錯開」`
- VN cũ: `「Kya phu!? Hà! A a——nhanh, quá——\nưm——phù a——nữa đi, thế này, eo, lệch, mất」`
- Sửa: `「Kyaphù!? Hà! A a——nhanh, quá——ưm——phù a——nữa đi, thế này, eo, lệch, mất」`
- Lý do: JP きゃふっ bị phiên âm "Kya phu" — Việt hoá viết liền một từ "Kyaphù" (tiền lệ h6 769: きゃふっ→"Kyaphù"); ふあっ→"phù a".
**Key 2142 (ポーレット)**
- JP: `「ひあ！？　あっ！　それ、らめっ！　イっちゃう、\nわた、しっ――すぐっ――ふ、きゅ――イっ、ちゃっ」`
- TW: `「呀！？啊！這樣不行！要丟了，我馬上要——呼——丟了」`
- VN cũ: `「Hia!? A! Thế này, không được! Lên đỉnh mất,\nem——ngay lập tức——phù, kyu——lên đỉnh, mất」`
- Sửa: `「Hia!? A! Thế này, không được! Lên đỉnh mất, em——ngay lập tức——phù, Kíu——lên đỉnh, mất」`
- Lý do: JP きゅ bị phiên âm "kyu" — Việt hoá "Kíu" (tiền lệ h6: きゅ→"Kíu"). (ひあ→"Hia" trong VN cũ đã đúng.)
**Key 2187 (ポーレット)**
- JP: `「えっ！？　やっ――いまのッ――んひゃうっ！？\nんんんんっ！？　なに、これっ――わたし、いまっ」`
- TW: `「哎！？呀——剛才——嗯！？嗯嗯嗯！？這是什麼——我剛才」`
- VN cũ: `「Hả!? Á——vừa rồi——ưm hyau!?\nƯm ưm ưm ưm!? Gì, thế này——em, vừa nãy」`
- Sửa: `「Hả!? Á——vừa rồi——ưm hiau!? Ưm ưm ưm ưm!? Gì, thế này——em, vừa nãy」`
- Lý do: JP んひゃうっ bị phiên âm "hyau" — Việt hoá "hiau" (ん→"ưm" đã đúng; ひゃう→"hiau").
**Key 2241 (ポーレット)**
- JP: `「はきゅっ！？　くっ――ふうううううっ」」`
- TW: `「啊呀！？啊——呼啊」`
- VN cũ: `「Hakyu!? Ư——phuuuuuu」`
- Sửa: `「Hakíu!? Ư——phuuuuuu」`
- Lý do: JP はきゅっ bị phiên âm "Hakyu" — Việt hoá "Hakíu" (は→"Ha", きゅ→"kíu").
**Key 2286 (ポーレット)**
- JP: `「ん……あ――すごい……おちんちん、\nおっき、すぎて――これ――よいしょ――えいっ！」`
- TW: `「嗯……啊——好厲害……雞雞真大——這個——嘿咻！」`
- VN cũ: `「Ưm……a——Tuyệt quá……dương vật,\nto, quá——cái này——yoozo——ây da!」`
- Sửa: `「Ưm……a——Tuyệt quá……dương vật, to, quá——cái này——yôi-zo——ây da!」`
- Lý do: JP よいしょ bị phiên âm "yoozo" (chữ thường, dạng La-tinh) — Việt hoá "yôi-zo" (theo cách file diễn よいしょ: "Yôi-zo" ở 2365).
**Key 2304 (ポーレット)**
- JP: `「んゆっ！！？」`
- TW: `「嗯啊！！？」`
- VN cũ: `「Ưm yu!!?」`
- Sửa: `「Ưm iu!!?」`
- Lý do: JP んゆっ bị phiên âm "yu" — Việt hoá "iu" (ん→"Ưm" đã đúng; ゆ→"iu").
**Key 2365 (ポーレット)**
- JP: `「よいしょ――よいしょ――しこ――しこ――\nもにゅ、もにゅ――しこ――しこ――えいっ」`
- TW: `「嘿咻——嘿咻——套來——套去——揉來——揉去——套來——套去，嘿」`
- VN cũ: `「Yoozo——yoozo——sục——sục——\nnắn, nắn——sục——sục——ây da」`
- Sửa: `「Yôi-zo——yôi-zo——sục——sục——nắn, nắn——sục——sục——ây da」`
- Lý do: JP よいしょ――よいしょ bị phiên âm "Yoozo——yoozo" — Việt hoá "Yôi-zo——yôi-zo".
**Key 2413 (ポーレット)**
- JP: `「きもち――いい――そこっ――だから、ねっ――\nんひゅっ！？　ふ――らめぇ――いま、今は、まだっ」`
- TW: `「好舒服——那裡——所以————嗯呀！？呼——不行——現在不行」`
- VN cũ: `「Sướng——quá——chỗ đó——nên là, nhé——\nưm hyu!? Phù——không được——bây, bây giờ, chưa được」`
- Sửa: `「Sướng——quá——chỗ đó——nên là, nhé——ưm hiu!? Phù——không được——bây, bây giờ, chưa được」`
- Lý do: JP んひゅっ bị phiên âm "hyu" — Việt hoá "hiu" (ん→"ưm" đã đúng; ひゅ→"hiu").

### Thở gấp っ bị bỏ mất (3 dòng)
**Key 2208 (双鉄)**
- JP: `「っ――ぐっ！」`
- TW: `「啊——呃！」`
- VN cũ: `「——Ư!」`
- Sửa: `「——Ư——hự!」`
- Lý do: JP っ――ぐっ！ bị bỏ mất ぐっ trong VN ("——Ư!") — sửa thành "——Ư——hự!" (っ→Ư, ぐっ→hự).
**Key 2307 (双鉄)**
- JP: `「んんんんっ！」`
- TW: `「嗯嗯嗯！」`
- VN cũ: `「Ưm ưm ưm!」`
- Sửa: `「Ưm ưm ưm ưm!」`
- Lý do: JP んんんんっ！ có 4 tiếng ん nhưng VN chỉ có 3 "Ưm" — sửa thành 4 "Ưm".
**Key 2360 (ポーレット)**
- JP: `「ふふっ、村娘風？　って感じですか？\nワインとか、足踏みしてつくっちゃったり」`
- TW: `「嘻嘻，這個可以叫鄉下的姑娘吧？比如用腳踩葡萄釀酒之類的」`
- VN cũ: `「Fufu, kiểu cô gái thôn quê? Cảm giác vậy đúng không anh?\nKiểu như, dùng chân giẫm để làm rượu vang ấy.」`
- Sửa: `「Fufu, kiểu cô gái thôn quê? Cảm giác vậy đúng không anh? Kiểu như, dùng chân giẫm để làm rượu vang ấy.」`
- Lý do: JP ふふっ (tiếng cười khúc khích) bị phiên âm "Fufu" — sửa theo quy ước file ふふっ→"Ư hự" (như 2345–2364: うふふ→"Ư hự hự").

### Sai nghĩa / lỗi đánh máy (5 dòng)
**Key 2158 (ポーレット)**
- JP: `「はっ――ああっ――きもち、いいいっ――んっ、\nあ――ぷくって、亀頭――なか、を――こす、って」`
- TW: `「呼——啊——好舒服——嗯——啊——碰到了——龜頭——蹭著裡面」`
- VN cũ: `「Hà——a a——sướng, quá đi——ưm,\na——phồng lên, quy đầu——đang cọ, xát——bên trong」`
- Sửa: `「Hà——a a——sướng, quá đi——ưm, a——phồng lên, quy đầu——bên trong——đang cọ, xát」`
- Lý do: Sai thứ tự từ: JP 亀頭――なか、を――こす (quy đầu — bên trong — cọ xát) nhưng VN cũ đảo thành "bên trong——quy đầu" — đổi lại đúng thứ tự JP.
**Key 2179 (双鉄)**
- JP: `「おっと」`
- TW: `「哎」`
- VN cũ: `「Ốp」`
- Sửa: `「Ối」`
- Lý do: JP おっと bị dịch "Ốp" — sai hoàn toàn; theo tiền lệ h7 861 (おっと "Ốp"→"Ối") sửa thành "Ối".
**Key 2416 (ポーレット)**
- JP: `「重くて、痛い――すごく、濃いっ――んっ――\nはぁっ――熱い、すごいの――わたし、どろどろっ」`
- TW: `「好重，好痛——好濃稠啊——嗯——呼——好燙——我已經變得黏糊糊了」`
- VN cũ: `「Nặng quá, đau quá——đặc, quá——ưm——\nhà——nóng quá, dữ dội quá——em, nhão nhoét hết rồi」`
- Sửa: `「Nặng quá, đau quá——đặc, quá——ưm——Hà——nóng quá, dữ dội quá——em, nhão nhoét hết rồi」`
- Lý do: Lỗi đánh máy: JP はぁっ (tiếng thở dài) bị dịch "nhà" — sửa thành "Hà".
**Key 2462 (双鉄)**
- JP: `「福岳から[しゃんはい,1]上杯に飛んで、パル＝イスか。\nポーレットの働きものは、ご両親譲りなのだな」`
- TW: `「從福岳飛到上烸，再到巴黎。你工作這麼賣力估計是父母的遺傳」`
- VN cũ: `「Bay từ Fukuoka đến Thượng Hải, rồi sang Paris sao.\nSự chăm chỉ của Paulette, chắc là được thừa hưởng từ ba mẹ nhỉ.」`
- Sửa: `「Bay từ Fukutake đến Thượng Hải, rồi sang Paris sao. Sự chăm chỉ của Paulette, chắc là được thừa hưởng từ ba mẹ nhỉ.」`
- Lý do: Sai tên địa danh: JP 福岳 bị dịch "Fukuoka" (福岡) — 福岳 là địa danh khác, đọc kun "Fukutake" (đề xuất, chờ Hieu xác nhận).
**Key 3214 (monologue)**
- JP: `幸福感が達成感が独占欲が全て混じって精子になって、\nポーレットの卵子を溺れさせてく。`
- TW: `幸福感、成就感、獨占欲都化作了精子，衝向了波萊特的卵子。`
- VN cũ: `Cảm giác hạnh phúc, cảm giác thành tựu, tính độc chiếm, tất cả hòa quyện thành tinh trùng,\nnhấn chìm buồng trứng của Paulette.`
- Sửa: `Cảm giác hạnh phúc, cảm giác thành tựu, tính độc chiếm, tất cả hòa quyện thành tinh trùng, nhấn chìm trứng của Paulette.`
- Lý do: Sai nghĩa: JP 卵子 (trứng/noãn) bị dịch "buồng trứng" (cơ quan) — sửa thành "trứng".

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
[script]
1456 = "……Thưởng thức trọn vẹn vị ngọt ngào, tôi rụt lưỡi vào trong miệng."
1463 = "……Hương thơm nồng nàn bắt đầu lan tỏa khắp cửa hàng đường sắt."
1502 = "「……Ưm——a. Anh Soutetsu. Nhột——quá.」"
1504 = "「……À——Đúng là ngon thật.」"
1506 = "「…………Hừm. Cái này——tuyệt thật đấy.」"
1510 = "「……Paulette.」"
1513 = "「……Em thực sự vất vả rồi. Tuyệt vời lắm. Tôi nghĩ đây là một chiến dịch quảng bá không thể nào tốt hơn được nữa.」"
1516 = "「……Dù sẽ có những hạn chế về ngân sách và cơ sở vật chất, nhưng theo tôi, ít nhất cũng cần phải đạt đến mức 『Có thể tiếp xúc với truyện tranh từ khắp nơi trên thế giới』.」"
2047 = "「Nói gì thì nói, tôi cũng là con nuôi của xưởng rượu mà. Nên tôi cũng biết đôi chút về rượu.」"
2067 = "「Không có chi cái gì, đây là một bữa tiệc ngon lành không gì sánh bằng đấy.」"
2080 = "「Cứ lên đỉnh——đi——ư——tôi cũng——sắp rồi」"
2088 = "「Nào, a~」"
2089 = "「Nào, tiếp tục thôi. Cất công rồi, hãy đọc cho tôi nghe đến cuối đi.」"
2110 = "「Cho tôi thêm miếng nữa đi——Lần này, hãy để tôi ăn.」"
2125 = "「Chỉ tổ chức 『Trải nghiệm làm rượu vang bằng chân』 không thôi thì phí quá. Ohitoyo vốn có thương hiệu rượu Shochu Kuma mà.」"
2132 = "「Híuaaaaaaaaaaaaaaan!!!」"
2136 = "「Hia!?」"
2137 = "「Hiau!? A——phù——ư, a——em——em——lên đỉnh——lên đỉnh, rồi mà!」"
2139 = "「Kyaphù!? Hà! A a——nhanh, quá——ưm——phù a——nữa đi, thế này, eo, lệch, mất」"
2142 = "「Hia!? A! Thế này, không được! Lên đỉnh mất, em——ngay lập tức——phù, Kíu——lên đỉnh, mất」"
2150 = "「Không——Tôi nghĩ làm bẩn bằng nước bọt thì có lỗi lắm.」"
2154 = "「Quả thực, là thượng hạng. Một hương vị phong phú tuyệt đỉnh.」"
2158 = "「Hà——a a——sướng, quá đi——ưm, a——phồng lên, quy đầu——bên trong——đang cọ, xát」"
2161 = "「Hà……ưm……chụt——chụt——chụt——phù, a——thích quá——Anh Soutetsu, ơi——ưm, ưm, chụt」"
2177 = "「Oa, hồng trà Fauchon và bánh eclair mini này! Vui quá, mẹ vẫn còn nhớ.」"
2179 = "「Ối」"
2185 = "「Phê!?」"
2187 = "「Hả!? Á——vừa rồi——ưm hiau!? Ưm ưm ưm ưm!? Gì, thế này——em, vừa nãy」"
2203 = "「Hàm——chụt——rộp——chụt——chụt——（ực）——rộp——rộp——chụt」"
2208 = "「——Ư——hự!」"
2224 = "「A——ưm……chụt——phù——a——chụt——chụt——chụt——chụt——」"
2227 = "「A——em xin phép ạ. Ưm——ngoạm——ngoạm——」"
2241 = "「Hakíu!? Ư——phuuuuuu」"
2270 = "「Hự」"
2273 = "「Ưm——hự——」"
2275 = "「Ưm——hự——（ực）」"
2277 = "「Ưm——ưm ưm——ưm——」"
2279 = "「Ưm——ưm chụt——chụt——ưm, phù a. À ừm……sao, thế ạ? Anh Soutetsu.」"
2282 = "「Ưm……」"
2286 = "「Ưm……a——Tuyệt quá……dương vật, to, quá——cái này——yôi-zo——ây da!」"
2289 = "「Ưm……chụt——chụt——rộp——rộp, chụt——chụt——chụt——（ực）」"
2290 = "「Ưm……chụt——chụt——rộp——chụt——chụt——liếm——rộp」"
2292 = "「Ưm……chụt——ưm——hàm——rộp, rộp, chụt, chụt——chụt——rộp, rộp」"
2298 = "「Vâng. Họa tiết được in lên lớp sô-cô-la trắng đấy ạ.」"
2300 = "「Ừm. Quả thực rất lãng phí khi lượng hành khách chỉ tập trung ở đoạn ga Ohitoyo đến ga Mine Treasure.」"
2304 = "「Ưm iu!!?」"
2307 = "「Ưm ưm ưm ưm!」"
2314 = "「Ừ, tập hợp những người liên quan đến xưởng rượu ở Ohitoyo, và những người liên quan đến thư viện truyện tranh Yunoi lại với nhau.」"
2327 = "「Ừ. Tôi cầu còn không được. Ngay hôm nay, tôi vẫn còn có thể cố gắng tiếp đấy.」"
2329 = "「Ừ, một người tửu lượng kém như tôi cũng có thể thưởng thức, là loại rượu vang nhẹ, rất dễ uống.」"
2338 = "「Ừ, tôi rất sẵn lòng chiêm ngưỡng.」"
2340 = "「Ưm? ……A——phù——này? Anh Soutetsu——ưm. Em, muốn——nhiều đồ ngọt, hơn nữa——chụt」"
2343 = "「Hửm? Tôi cứ nghĩ ôm ấp chính là nhuộm màu rồi chứ——Không chỉ ôm ấp, mà là nhuộm màu, nghĩa là sao?」"
2356 = "「Ufufu. Cảm ơn anh. Nhưng mà——nhé? Anh Soutetsu.」"
2360 = "「Fufu, kiểu cô gái thôn quê? Cảm giác vậy đúng không anh? Kiểu như, dùng chân giẫm để làm rượu vang ấy.」"
2365 = "「Yôi-zo——yôi-zo——sục——sục——nắn, nắn——sục——sục——ây da」"
2370 = "「Ừm fufu, haha hihi haa」"
2376 = "「Phù a!? （Lùi lạiiiiiiiii!!）」"
2402 = "「Vâng. Ufufu, vui quá đi. Được uống hồng trà mẹ tặng cùng với Anh Soutetsu thế này.」"
2407 = "「Xin mời anh thưởng thức.」"
2413 = "「Sướng——quá——chỗ đó——nên là, nhé——ưm hiu!? Phù——không được——bây, bây giờ, chưa được」"
2416 = "「Nặng quá, đau quá——đặc, quá——ưm——Hà——nóng quá, dữ dội quá——em, nhão nhoét hết rồi」"
2421 = "「Nếu là rượu vang do Paulette giẫm chân làm ra, tôi nhất định muốn uống thử.」"
2436 = "「Ừm. Ohitoyo vốn là thị trấn nấu rượu mà——Ở Kumamoto cũng có cả vườn nho lẫn xưởng rượu vang.」"
2462 = "「Bay từ Fukutake đến Thượng Hải, rồi sang Paris sao. Sự chăm chỉ của Paulette, chắc là được thừa hưởng từ ba mẹ nhỉ.」"
2474 = "「Tôi không hiểu. Nói rõ hơn cho tôi nghe đi. Em muốn tôi nhuộm phần nào của Paulette, bằng cái gì của tôi?」"
2478 = "「Tôi cũng rất vui. Thật hạnh phúc.」"
2489 = "「Chỉ là câu chuyện giữa những người đã đính hôn quá vui vẻ, nên mới đi xa thôi. Nếu em xin lỗi, thì tôi cũng mang tội chung đấy nhé?」"
2504 = "「Tôi rất mong chờ đấy.」"
2505 = "「Thích từ hồi còn bé tí luôn ấy chứ! Anh đợi một lát nhé. Em đi pha ngay đây.」"
2512 = "「Tôi đang chuyển động, để khiến Paulette tràn ngập——say đắm tôi đấy.」"
2517 = "「Có tôi ở đây để bù đắp cho em mà. Đừng bận tâm đến những tiểu tiết, tôi muốn Paulette cứ phát huy ý tưởng của Paulette đi.」"
2518 = "「Tôi sẽ nhuộm thắm, ghi đè lên, và đánh dấu.」"
2520 = "「Sự cương cứng của tôi——dương vật của tôi——muốn, mút mút, nhũ hoa, của Paulette.」"
2524 = "「Tôi cũng——tràn ngập Paulette rồi.」"
2529 = "「Để khẳng định Paulette là người phụ nữ của tôi, là của riêng tôi. Tôi sẽ để nó thấm sâu vào toàn bộ cơ thể, vào tận xương tủy, và cả trái tim em.」"
2530 = "「Tôi nghĩ đây là một chuyến tàu sự kiện cực kỳ xuất sắc. Đúng là dụng nhân như dụng mộc. Tôi cũng rất vinh dự khi được đóng góp một phần vào đó.」"
2552 = "「Đến lượt tôi, làm theo ý thích sao?」"
2554 = "「Câu chuyện hay là đương nhiên rồi, nhưng cách em đọc cũng rất tuyệt. Cơn mưa bằng giọng nói của em đã nhấn chìm tôi vào câu chuyện.」"
2559 = "「Tôi hiểu rồi.」"
2560 = "「Là món em thích sao?」"
2566 = "「Đúng vậy nhỉ. Nếu chỉ biến nó thành cơ sở mang tính địa phương của Yunoi, thì xét về mặt Đường sắt Ohitoyo, hầu như sẽ chẳng sinh ra lợi nhuận gì.」"
2571 = "「Đúng rồi! Phải mở ra xem mới được.」"
2586 = "「Tuy còn tùy khẩu vị, nhưng chất lượng thì miễn chê. Cá nhân tôi đặc biệt thích rượu vang đỏ. Cực kỳ hợp với thịt ngựa sống luôn.」"
2608 = "「『Vì vậy』, làm bẩn cũng không sao. Vì đây là bộ quần áo mẹ làm riêng cho em mà.」"
2614 = "「Không sai đâu. Mang lại cảm giác rất cổ tích. Cực kỳ đáng yêu, nếu hỏi thích hay không thì tôi rất thích.」"
2629 = "「Paulette?」"
2647 = "「Hiện tại, việc khắc phục sự yếu kém về yếu tố du lịch ở khu vực Yunoi, chính là chìa khóa để cải thiện Đường sắt Ohitoyo hơn nữa đúng không anh?」"
2661 = "「Thầy ấy đã qua đời rồi sao. Tiếc thật, tôi rất muốn được gặp thầy một lần.」"
2686 = "「Bị tôi?」"
2693 = "「Tôi cõng em nhé?」"
2695 = "「Nếu phải giữ bí mật với cả Reina, thì đây là một trong những bí mật tối cao của Đường sắt Ohitoyo rồi——Tôi hiểu.」"
2711 = "「Anh đợi thêm một chút xíu nữa nhé.」"
2751 = "「Đây là tinh dịch dùng để nhuộm thắm Paulette. Tôi muốn em tự vắt kiệt nó theo ý mình, chứ không phải ý tôi.」"
2753 = "「Cái này, cứ thế ăn luôn được à?」"
2755 = "「Chiếc váy mẹ vợ cất công may cho mà.」"
2762 = "「Bánh eclair mini. Hợp lắm đấy? Rất hợp luôn.」"
2764 = "「Đến mức tôi cũng muốn trở thành một hành khách, để được Alice ở xứ sở toa xe tự hành thiết đãi đấy. Tuyệt vời lắm.」"
2769 = "「À, ừm……cái đó, không có chi, ạ.」"
2776 = "「À ừm——múp!?」"
2777 = "「À, ừm……」"
2781 = "「À ừm——nếu vậy. Em cũng, muốn ăn thử, ạ.」"
2783 = "「Vậy thì rắc rối đấy. Thế thì tôi sẽ ngoan ngoãn lắng nghe. Nhờ em giải thích lại nhé.」"
2784 = "「Vậy thì, cứ thế đi.」"
2788 = "「Sở thích của tôi, cũng là đánh trực diện mà.」"
2794 = "「Vậy thì nhất định rồi. Tôi sẽ mua về, chúng ta cùng uống nhé.」"
2798 = "「Nếu vậy thì tôi phản đối việc thiên về phong cách Nhật Bản. Có thể nó sẽ là đối sách tốt với địa phương, nhưng sức hút du lịch sẽ bị giảm sút.」"
2800 = "「Nếu vậy, khi có dịp hãy cho tôi gửi lời chào hỏi nhé.」"
2817 = "「Vì là trà Assam, nên em đề cử pha trà sữa nhé——」"
2826 = "「Am.」"
3114 = "Vừa mút mát, vừa dai dẳng, chầm chậm——liếm láp phần gốc khớp ngón tay đầu tiên của tôi."
3120 = "Chỉ cắn đứt một nửa."
3156 = "Hoàn toàn là, những chuyển động khiêu gợi tôi."
3170 = "Lạch bạch lạch bạch, đến cả tiếng bước chân cũng rộn rã."
3183 = "——Nguy hiểm, quá. Tôi lùi về phía giường để tạo khoảng cách, chật vật lắm mới kìm lại được."
3214 = "Cảm giác hạnh phúc, cảm giác thành tựu, tính độc chiếm, tất cả hòa quyện thành tinh trùng, nhấn chìm trứng của Paulette."
3249 = "Tôi ôm ghì lấy cô ấy. Cảm giác như đang ôm một túi chườm nóng vậy. Thật ấm áp."
3262 = "Cảm giác dính chặt, càng thêm gia tăng."
3268 = "Hăng hái cắn miếng thứ hai. Tôi lỡ ngậm luôn cả đầu ngón tay của Paulette vào miệng."
3277 = "Đáp lễ ly rượu, à không, đáp lễ bánh eclair. Tôi nhón lấy một chiếc có màu như bánh mì nướng, đưa cho cô ấy."
3282 = "Thừa thế xông lên, tôi liếm láp, mút mát. Thưởng thức trọn vẹn vị ngọt ngào, rồi chóp chép nhả ra."
3294 = "Muốn cứ thế này mà ôm lấy em. Muốn làm tình với em một cách điên cuồng——!!?"
3307 = "Bánh eclair mini đã trôi xuống cổ họng. Nhưng vị ngọt ngào lại càng tăng thêm."
3310 = "Tôi nhét chiếc bánh eclair mini vào đôi môi ướt át của Paulette. Há to miệng như một chú chim non, dùng ngón tay hối thúc."
3332 = "Đang bị ăn. Toàn bộ con người tôi. Paulette đang dùng đôi môi ấy để yêu thương, để nếm thử tôi."
3339 = "Đầu ngón tay của tôi trong nháy mắt, đã nằm gọn trong khoang miệng nóng hổi ướt át của Paulette."
3343 = "Đưa mắt nhìn xuống khuôn mặt có vẻ bối rối kia, Paulette đang tròn xoe mắt nhìn tôi."
3382 = "Bị bao bọc."
3404 = "Mang chút cảm giác rượu vang nhè nhẹ của những trái nho chín mọng——Hòa quyện cùng vị ngọt ngào êm dịu lan tỏa."
3427 = "Cát trong đồng hồ cát mang màu hổ phách. Tuôn rơi nhè nhẹ, chảy trôi giữa quá khứ và tương lai."
3430 = "Bánh eclair, cùng với lưỡi và nước bọt của Paulette. Thứ hỗn hợp sền sệt ấy, từ lưỡi chảy thẳng xuống háng."
3478 = "Paulette chủ động tách môi tôi ra."
3479 = "Paulette hớn hở tháo lớp gói quà trang nhã."
3483 = "Yết hầu Paulette khẽ chuyển động cái ực."
3485 = "Mỗi khi lưỡi Paulette ngọ nguậy, tôi có cảm giác như đến cả não mình cũng đang bị liếm láp."
3489 = "Paulette nhón lấy một chiếc bánh có họa tiết chùm nho sặc sỡ, rồi đưa về phía tôi."
3490 = "Đặt ấm trà và đĩa lên khay, Paulette quay trở lại bàn."
3507 = "Paulette cởi tạp dề ra, gấp lại. Và rồi, cứ thế——"
3512 = "Tiếng thở hổn hển. Bốc lên, là hương thơm hòa quyện giữa mồ hôi, sô-cô-la và Paulette."
3520 = "Vào chiếc cốc đã được hâm nóng sữa sẵn, ngay khoảnh khắc hạt cát cuối cùng rơi xuống, hồng trà được thong thả rót vào."
3529 = "Chóp chép, chóp chép, chầm chậm, chầm chậm, như đang trêu ngươi, nhai nghiền nát chiếc bánh eclair mini——"
3552 = "Vị ngọt ngào ập đến trong khoang miệng."
3606 = "Nương theo ánh mắt của tôi, Paulette cũng cúi xuống nhìn cơ thể mình, nhìn bầu ngực mình."
3638 = "Có lẽ đây là, hương vị của người lớn chăng."
3653 = "Dù nói là mini, nhưng để ăn hết trong một miếng thì hơi to. Tôi chỉ cắn một nửa vào miệng——"
3757 = "（Tuột——）"
3760 = "（Tách——tách——）"
```

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- Soutetsu gọi Paulette "em" 12 lần trong thoại (2489, 2783, 2693, 2676, 2554, 2380, 2381, 2717, 2517, 2529, 2751, 2437) vs "cô" 0 lần — cộng dồn toàn dự án: "em" 96 vs "cô" 48 (sau h8; đính chính 19/11: sleeper 1627 đã quyết là hỏi Hikari, không tính "em"). Lưu ý: 2629 bị LOẠI khỏi đếm (VN cũ của nó là dòng của Paulette đang bị thay thế); 2753 là dương tính giả ("sô-cô-la"); 2273 là "cô ấy" ngôi thứ ba trong độc thoại, KHÔNG tính là cách gọi. Các lần "em ấy"/"cô ấy" trong độc thoại là ngôi thứ ba, KHÔNG tính.
- 湯医/湯医線: xuất hiện dạng thứ BA — "Yunosaka" 12/12 lần (2085, 2314, 2566, 2635, 2636, 2637, 2638, 2647, 2681, 2756, 2759, 2793); "Yui" 0 lần; "Yunoi" 0 lần. Hai dòng 2635/2638 mang furigana rõ ràng [ゆのい,1]湯医 / [ゆのいえほんかん,4]湯医絵本館 — ủng hộ "Yunoi". Lưu ý: docs có 湯ノ坂 (Yunosaka) — một từ khác — và context_trans.md dùng "tuyến Yui" cho 湯医線.
- 御一夜: 7 lần, tất cả đều là "Ohimitera" (2125, 2300, 2314, 2436, 2566, 2647, 2695) — đã sửa hết thành "Ohitoyo" theo quyết định 19/11; "Ohitoyo" 0 lần trong file.
- Không có 帝鉄/コン/KiHa/マスコン/宮司/整備体/運転ボディ/駿袋/Migita/オコジョ trong file. Paulette gọi Soutetsu "cậu": 0 lần. Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói: 0 lần. "Thẻ bảng": 0 lần. Railord: 1 lần (3663), đúng.
- Dòng chưa chắc chắn (2 dòng, KHÔNG đưa vào khối sửa — ghi cả hai phương án): 3087 (độc thoại Soutetsu, JP しかし――自己紹介をどうしよう。 — VN "mình nên tự giới thiệu thế nào đây": "Tôi" theo quy tắc vs giữ "mình" như suy nghĩ nội tâm; cùng câu hỏi mở như h3 1683 — ĐÃ QUYẾT 19/11: giữ "mình") và 3726 (suy nghĩ trong ngoặc, JP （お父上であり、お母上であり、れいなで――僕か） → VN "（Là ba, là mẹ, là Reina——và là mình sao.）": "mình" vs "Tôi").

## Đề xuất cập nhật context (chưa chốt)

- 福岳 → "Fukutake" (2462): 福岳 là địa danh hư cấu, xuất hiện đúng 1 lần trong toàn dự án, không có mục docs; VN cũ dịch nhầm thành "Fukuoka" (福岡). Đọc kun "Fukutake" là đề xuất — cần Hieu xác nhận trước khi coi là chuẩn.
- Quy ước "rộp" cho họ âm lăn lưỡi (file này): れる/るっ/れろ đều → "rộp", chỉ ぺろ → "liếm". Bằng chứng: 4 cặp đối chiếu đơn vị-đơn-vị khớp hoàn hảo (2275→2289 9/9, 3339→2290 8/8, 3478→2292 11/11, 3332→2203 9/9, cặp cuối lỏng ở じゅずっ/ずっ→"chụt"). Ghi nhận là quy ước riêng của file, chờ Hieu xác nhận trước khi áp dụng rộng.
- おっと → "Ối" (2179): theo tiền lệ h7 861 (おっと "Ốp" là sai hoàn toàn, đã sửa thành "Ối" trong h7) — cùng một lỗi lặp lại ở h8.
- 髑国 → "Đức" là ĐÚNG, không phải lỗi (2577): quy ước thế giới hư cấu của dự án — 冥国=Mỹ, 詠国=Anh, 髑国=Đức, 仲国=Trung Quốc, フランク=Pháp. Bằng chứng: 真闇03 1687 ghi "Dokkoku (Đức)"; 仲国06 1872, 凪ふかみ01 1587/1698/1812 đều dùng "Đức". TW 德國 cũng đúng ở đây.
- ぷぁ/ふぁ → "phù a": 2279 (ぷぁ) và 2376 (ぷあっ) đều sửa "phù"/"Phù" thành "phù a"/"Phù a" theo quy ước file ふぁ→"phù a".

## Đã kiểm tra và KHÔNG tính là sai

- 2131, 2135 ("Hiu" đã Việt hoá) — không phải dạng La-tinh sót.
- 2145 (Soutetsu gọi Paulette bằng tên trần) — đúng theo quy ước docs (chỉ Paulette gọi Soutetsu bằng tên trần mới sai).
- 2146 (JP っ trần → "Hự") — đã diễn đúng; đây là tiền lệ cho bản sửa mới ở 2270 (JP っ trần → "Hự").
- 2155, 2157, 2163 (っ giữa dòng trong chuỗi thở) — được hấp thụ theo quy tắc hiệu chuẩn (không thêm Ư cho っ giữa dòng).
- 2271/2272/2276 (はうっ→"Hau") — ĐÚNG theo tiền lệ h5 826 và h7 897; không gắn cờ はうっ→"Hau".
- 2296, 2303, 2306, 2308 (9 tiếng ん → 9 "Ưm") — đếm đúng.
- 2313, 2323 ("Paule——ờm", cách diễn ngập ngừng cuối câu) — giữ nguyên; TW bỏ っと.
- 2344 (sweep "already-rendered") — audit đồng ý, không đưa vào danh sách sửa.
- 2345–2364 (うふふ→"Ư hự hự") — quy ước riêng của file, giữ nguyên.
- 2470 (なぞなぞアリス → "Alice câu đố") — theo quy tắc furigana của docs.
- 2577 (髑国→"Đức") — đúng theo quy ước thế giới hư cấu (xem trên).
- 2505: VN thu hồi giữ "Anh đợi" — Paulette gọi Soutetsu là "Anh", ĐÚNG, không phải lỗi xưng hô.
- 3249: VN thu hồi có "cô ấy" ngôi thứ ba trong độc thoại — KHÔNG tính vào đếm "cô" vs "em".
- 1510: bản sửa "……Paulette." — tên gọi độc lập thì thầm, thuộc ngoại lệ rên (moan exception) như h1/h2.
- 2241: "phuuuuuu" giữ nguyên số lượng u của VN cũ (âm thở dài, độ dài là lựa chọn phong cách của bản dịch gốc); chỉ sửa "Hakyu"→"Hakíu".
- 2376: "Lùi lạiiiiiiiii!!" giữ nguyên số lượng i của VN gốc (VN thu hồi từ 3294); chỉ sửa "Phù"→"Phù a".

## Kết bài

- h8 sai 147/649 (22,7%) — tỉ lệ cao thứ hai trong các file Paulette đã kiểm (sau Hibiki 03 86,2% và obasan 56%), và là mạng xoay vòng lớn nhất từ trước tới nay: 6 chuỗi, 86 dòng, chuỗi dài nhất 30 mắt xích (mega-chain). Lỗi tập trung ở lệch vị trí (86) + xưng hô hệ thống (36) + tiếng thở La-tinh (11) + thuật ngữ Ohimitera (6) + sai nghĩa/lỗi đánh máy (5) + thở gấp っ (3).
- Khối TOML 147 key đã parse đúng bằng tomllib; số key khớp đúng với JSON (147); giá trị JSON khớp 0 sai lệch với khối TOML.
- Kiểm tra lần hai: 147/147 bản sửa đọc lại đối chiếu JP, 0 bị loại, 1 được sửa trong lần hai (2110 — lỗi xưng hô thừa hưởng từ dòng cho).
- 2 dòng chưa chắc chắn 3087 và 3726 — ĐÃ QUYẾT 19/11 (Hieu): giữ "mình" (độc thoại nội tâm tự vấn cảm xúc của Soutetsu — ngoại lệ như h3 1683). Cả hai đều đúng như bản cũ, không cần sửa; file còn 0 dòng chưa chắc chắn.
- Rà soát chéo sweep: 7 bản sửa sweep trong file đều được audit xác nhận (không xung đột); 1 mục "already-rendered" (2344) được đồng ý; audit bắt thêm 2 dòng gasp sweep bỏ sót (2208, 2307).
- Đề xuất mới cho Hieu: 福岳→"Fukutake" (chờ xác nhận); quy ước "rộp" cho họ れる/るっ/れろ; おっと→"Ối" (đã áp dụng ở 2179 theo tiền lệ h7).

---
**Bổ sung 19/11 (quyết định 湯医 — Hieu):** 12 dòng dùng "Yunosaka" cho 湯医 (2085, 2314, 2566, 2635, 2636, 2637, 2638, 2647, 2681, 2756, 2759, 2793) — JP cả 12 dòng đều là 湯医 (furigana ゆのい ở 2635/2638), không phải 湯ノ坂 — sửa thành "Yunoi". Trong đó 2314, 2566, 2647 đã có trong khối sửa gốc nên giá trị đã được cập nhật tại chỗ; 9 dòng mới trong khối dưới đây. File này giờ sai 156/649.

```toml
[script]
2085 = "「Là phòng trưng bày, nghĩa là có thể hiểu chuyến tàu cổ tích sẽ trở thành mô hình thu nhỏ của 『Thư viện Truyện tranh Yunoi』 đúng không?」"
2635 = "「Yunoi cũng có thương hiệu! 『Rượu vang Yunoi』」"
2636 = "「Sự liên kết giữa Yunoi và truyện tranh là gì?」"
2637 = "「Em cũng đã truyền đạt mối lo ngại đó cho phía Yunoi. Và đề xuất 『Thư viện Truyện tranh Yunoi』 đã được đưa ra vào hôm trước.」"
2638 = "「Chuyện về Thư viện Truyện tranh Yunoi, anh có thể nghĩ xa đến mức đó trong chớp mắt.」"
2681 = "「Làm được vậy thì lý tưởng quá. Bán ở cả thư viện truyện tranh nữa, lúc đó gọi là 『Rượu vang cổ tích Yunoi』 cũng hay.」"
2756 = "「Tác giả vẽ cuốn truyện tranh này, thầy 『Kinoko Daisuke』, nghe nói là người gốc Yunoi đấy ạ.」"
2759 = "「Ra vậy. Tuyệt vời thật. À——không chừng, ở Yunoi còn có cả bản gốc của truyện tranh nữa sao?」"
2793 = "「Vậy thì muốn hiện thực hóa nó quá nhỉ——cái đó……A! Làm sự kiện khai trương cho 『Thư viện Truyện tranh Yunoi』 luôn」"
```

---
## Đính chính 19/11 22:05 — tiếng cười không dập khuôn (quyết định của Hieu)

Hieu quyết: tiếng thở / tiếng rên / tiếng cười dịch NGẪU HỨNG theo tính cách từng nhân vật và ngữ cảnh, KHÔNG dập khuôn 1:1. Các bảng tra SFX chỉ là gợi ý mặc định. Theo đó, 4 dòng cười khúc khích trong file này đã sửa lại từ cách diễn "Ư hự" (tiếng rên/thở gấp) thành tiếng cười: 2356 "Ufufu. Cảm ơn anh. ...", 2360 "Fufu, kiểu cô gái thôn quê? ...", 2370 "Ừm fufu, haha hihi haa", 2402 "Vâng. Ufufu, vui quá đi. ...". Key 2360 được phân loại lại từ gasp thành tiếng cười (số gasp của file: 3 → 2; tổng vẫn 156). Tiền lệ "Ư hự" cho ふふっ/うふふ/んふふ bị bãi bỏ; xem sfx_and_emoticons.md §0.
