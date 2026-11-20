# Audit — ハチロク01_こんにちわ赤ちゃん.txt.toml (01_Hachiroku)

## Tổng quan

- File: `ハチロク01_こんにちわ赤ちゃん.txt.toml` — route 01_Hachiroku, **530 dòng script** (độc thoại 183, Hachiroku 113, Soutetsu 112, Urakami 27, Kisaki 25, Mototada 22, Mayu 21, Hibiki 15, Mayami 12).
- Nội dung: Soutetsu và Hachiroku đón Urakami cùng bé Mayu mới sinh; Hachiroku lần đầu bế em bé, tập vỗ ợ hơi, cho bú, dỗ ngủ, và nhận ra mình khao khát có con nhưng sợ thân phận Railord không thể sinh con; xen kẽ cuộc họp với Mototada và Kisaki về Dự án SL Đại Kyushu — tuyến Yunoi–Hayato, 8620 quá tải, các hãng lớn nhảy vào khai thác đầu máy hơi nước. Kết: Soutetsu và Hachiroku ước được đón một đứa trẻ, một thành viên mới trong gia đình.
- Phương pháp: đọc từng dòng đối chiếu JP + TW từ CSV3 (Trang tính 3), kiểm chứng chéo sweep っ, kiểm tra cơ học trùng khóa/trùng VN/thẻ %l/dòng chưa dịch/VN==TW/rò ký tự ngoại ngữ.
- **Kết quả: 530 dòng đọc, 15 dòng sai (2,8%).**
- Phân loại (15): gasp 6 (sweep: 1620, 1621, 2262, 2263, 2280, 2637), dịch sai 4 (2392, 2426, 2549, 2762), thuật ngữ 2 (Toukai đọc sai: 2216, 2815), đại từ/xưng hô 2 (2393, 2790), rò ký tự ngoại ngữ 1 (2164).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất (không có set trùng/stale). VN khớp TOML sau chuẩn hoá `\n` (322 dòng chênh lệch chỉ là `\n` bị TOML-2 dẹp thành khoảng trắng — đã biết, CSV3 là chuẩn). `[selections]` rỗng. Không có bản sao của file này (md5 `f7fccdad72cb0c04171cd9b121cb614a`, xuất hiện đúng 1 lần trong 227 file sources/toml2 — 216 md5 duy nhất, 11 nhóm trùng đã biết đều là file khác).
- Đại từ đã kiểm chứng toàn file: Soutetsu 'tôi' với Hachiroku ở mọi dòng đối thoại (đã rà bằng máy: 0 dòng Soutetsu tự xưng 'anh'); Hachiroku tự xưng 'em' nhất quán (chỉ có 'chúng tôi' dạng nhóm ở 2491, 2790); Kisaki 'tôi' với mọi người, gọi Soutetsu 'cậu' (2138) giữ nguyên; Mayami gọi Soutetsu 'Sou-chan'; Hibiki gọi Soutetsu 'anh hai'; Urakami gọi Hachiroku 'chị Hachiroku' (2574) giữ nguyên.

## Kiểm chứng sweep っ

- Sweep có **6 mục** cho file này trong `sweep-raw-gasp-wrong.json`: 1620, 1621 (lost-gasp-trailing), 2262, 2263 (lost-gasp-whole), 2280, 2637 (lost-gasp-trailing). Cả 6 đều kiểm chứng đúng với JP/TW trong CSV3; 5 mục nhận nguyên văn fix của sweep, riêng 2637 nhận nội dung nhưng viết theo dạng ngắt dòng của CSV3 (sweep dùng dạng TOML đã dẹp `\n` thành khoảng trắng — CSV3 là chuẩn).
- Các っ còn lại trong file đã rà bằng máy (JP chứa っ): toàn bộ là っ trong từ (～ている, ちょっと…), っ cuối nhấn mạnh gắn với từ nội dung (さまっ 2269/2381/2383, 戻りませんとっ 2229, ご馳走さまーっ 2521, 時間っ 1588, 声っ 2772, わたくしっ 2383/2617, ですけれどっ 2541/2617, なんとかわいっ 2718 — không thêm Ư theo quy tắc), hoặc âm đã diễn thành 'A'/'Hả'/'Fufu'/'Hừ'/'kyaha'/'Nfu' (2283, 2285, 2286, 2307, 2225, 2349, 2271, 2244, 2276, 2265, 2266). Không còn gasp nào bị mất — ngoại trừ 2319, xem mục chờ Hieu.
- Thẻ %l: 28 mở / 28 đóng, không có thẻ lệch hay thiếu `;` trong file này; số lượng `%l` JP = VN ở mọi dòng có thẻ.
- Trùng VN: 3 cặp VN trùng nhau đều là câu ngắn lặp lại hợp lệ cho cùng JP (「Ôi!」 2242/2246 cho 「まぁ！」; 「Nkyua!」 2313/2314 cho 「んきゅあ！」; 「Nfu~.」 2316/2321 cho 「んふー」) — không phải lệch dòng.

## Chi tiết từng dòng sai (15)

### key 1620 — 双鉄 — gasp

- JP: 「――っ！」
- TW: 「——咦！」
- VN cũ: 「——!」
- VN mới: 「——Ư!」
- Lý do: Sweep lost-gasp-trailing: JP 「――っ！」 — っ cuối sau dấu gạch, VN chỉ giữ dấu gạch + '!' mà mất tiếng gasp; TW 咦 cũng là tiếng thốt. Nhận fix của sweep: thêm Ư sau dấu gạch.

### key 1621 — ハチロク — gasp

- JP: 「――――――っ！！！」
- TW: 「——唔！！！」
- VN cũ: 「——————!!!」
- VN mới: 「——————Ư!!!」
- Lý do: Sweep lost-gasp-trailing: JP 「――――――っ！！！」 (6 dấu gạch + っ), VN chỉ giữ dấu gạch + '!!!'. Nhận fix của sweep: thêm Ư sau dấu gạch.

### key 2164 — ハチロク — meaning

- JP: 「セレモニイ――各種の式典などで、\nお客様の前に出ることなどはございました」
- TW: 「典禮——或者說各種儀式上，我是有在客人面前露過面的」
- VN cũ: 「Lễ nghi——trong các buổi lễ kỷ niệm,\nem vẫn xuất hiện trước mặt hành客.」
- VN mới: 「Lễ nghi——trong các buổi lễ kỷ niệm,\nem vẫn xuất hiện trước mặt khách hàng.」
- Lý do: VN cũ lẫn ký tự Hán 客 chưa dịch trong 'hành客' — lỗi rò rỉ ký tự ngoại ngữ (cùng họ lỗi rò tiếng Hàn file 12 key 3241). お客様 = khách hàng trong ngữ cảnh đường sắt; chỉ sửa từ đó, giữ nguyên phần còn lại.

### key 2216 — ハチロク — terminology

- JP: 「[なごてつ,2]名護鉄は申すまでもない名門私鉄。[とうかい,1]東峡鉄道は、旧帝鉄\n東峡道本線の、[みしま,1]箕島-[おおさか,1]逢坂間を買い受けた会社ですね」
- TW: 「名古屋鐵路作為私營鐵路界的名門自不必多言。東海鐵路則是購入了前帝國鐵路東海道本線三島至大阪段的公司」
- VN cũ: 「Nagotetsu là tuyến đường sắt tư nhân danh tiếng thì khỏi phải bàn rồi. Đường sắt Toukyou, là công ty đã mua lại tuyến chính Toukyou-dou của Teitetsu cũ, đoạn Mishima-Ousaka nhỉ.」
- VN mới: 「Nagotetsu là tuyến đường sắt tư nhân danh tiếng thì khỏi phải bàn rồi. Đường sắt Toukai, là công ty đã mua lại tuyến chính Toukai-dou của Teitetsu cũ, đoạn Mishima-Ousaka nhỉ.」
- Lý do: Furigana JP [とうかい,1] và TW 東海 đều là Toukai; VN cũ 'Toukyou' là đọc sai (Đông Hải ≠ Đông Kinh). Sửa cả hai chỗ: 'Đường sắt Toukai' và 'tuyến chính Toukai-dou'; 箕島-逢坂 giữ 'Mishima-Ousaka' theo furigana.

### key 2262 — ハチロク — gasp

- JP: 「っ！！」
- TW: 「唔！！」
- VN cũ: 「!!」
- VN mới: 「Ư!!」
- Lý do: Sweep lost-gasp-whole: JP chỉ có っ + '!!', VN chỉ còn dấu câu. Nhận fix của sweep: 'Ư!!'.

### key 2263 — ハチロク — gasp

- JP: 「っ！！！」
- TW: 「唔！！！」
- VN cũ: 「!!!」
- VN mới: 「Ư!!!」
- Lý do: Sweep lost-gasp-whole: JP chỉ có っ + '!!!', VN chỉ còn dấu câu. Nhận fix của sweep: 'Ư!!!'.

### key 2280 — まゆ — gasp

- JP: 「あにゅ～～っ」
- TW: 「啊妞～～」
- VN cũ: 「Anyu~~.」
- VN mới: 「Anyu~~Ư.」
- Lý do: Sweep lost-gasp-trailing: JP あにゅ～～っ — っ cuối sau ～～, VN 'Anyu~~.' làm mất tiếng; nhận fix của sweep 'Anyu~~Ư.'. Độ dài nguyên âm giữ nguyên (～～).

### key 2392 — ハチロク — meaning

- JP: 「は、はい。それでは――\nどうぞ、よろしくおねがいいたします」
- TW: 「好、好的。那恭敬不如從命——就請讓我抱一下下吧」
- VN cũ: 「V, vâng. Vậy thì——\nXin nhờ cô ạ.」
- VN mới: 「V, vâng. Vậy thì——\nXin cô cho em bế bé một chút ạ.」
- Lý do: TW chứng: '就請讓我抱一下下吧' = 'xin cho em bế bé một chút' — Hachiroku đang đón bé từ tay Urakami. VN cũ 'Xin nhờ cô ạ' mơ hồ, mất hẳn đối tượng (bé) và hướng nhờ (xin được bế). Sửa theo TW.

### key 2393 — 浦上 — pronoun

- JP: 「お久しぶりです。支店長――いえ、稀咲さん。\nそれに、右田さんにハチロクさんも」
- TW: 「好久不見，支行長——不，稀咲小姐。右田先生，八六小姐，你們好」
- VN cũ: 「Lâu rồi không gặp. Giám đốc chi nhánh——à không, anh Kisaki.\nCùng với anh Migita và cô Hachiroku nữa.」
- VN mới: 「Lâu rồi không gặp. Giám đốc chi nhánh——à không, cô Kisaki.\nCùng với anh Migita và cô Hachiroku nữa.」
- Lý do: 稀咲さん là nữ (TW 稀咲小姐); Urakami gọi Kisaki là 'anh Kisaki' sai giới tính/xưng hô. Tiền lệ dự án: Kisaki là 'cô' (Soutetsu gọi 'cô' — xem AUDIT-BRIEF). Sửa 'anh Kisaki' → 'cô Kisaki'; 'anh Migita' (Soutetsu, nam) và 'cô Hachiroku' giữ nguyên.

### key 2426 — 真闇 — meaning

- JP: 「すずちゃんには……あのこにはどうにもできん、\nさだめから、かな」
- TW: 「就是鈴妹妹……她無論如何都無法改變的——命運吧」
- VN cũ: 「Khỏi số phận……mà con bé không thể nào thay đổi được,\nchắc vậy.」
- VN mới: 「Là số phận……mà con bé chẳng thể nào thay đổi được,\nchắc vậy.」
- Lý do: VN cũ 'Khỏi số phận……' không thành câu tiếng Việt ('khỏi' không nối được nghĩa). JP さだめ = số phận; あのこにはどうにもできん = con bé chẳng thể làm gì được. Sửa 'Khỏi' → 'Là', giữ nguyên phần còn lại.

### key 2549 — 双鉄 — meaning

- JP: 「だから、落ち着け。僕もわからんが、笑顔でいるのだ。\n恐らく、悪い意味での『んあーん』ではなかろう」
- TW: 「所以說冷靜一點啊。具體我也不太清楚，但看她面帶笑容，應該這聲“嗯啊——嗯”應該不是什麼不好的意思吧」
- VN cũ: 「Thế nên tôi mới bảo em bình tĩnh. Tôi cũng không biết, nhưng cứ giữ nụ cười đi.\nCó lẽ tiếng 『Nga——n』 đó không mang ý nghĩa xấu đâu.」
- VN mới: 「Thế nên tôi mới bảo em bình tĩnh. Tôi cũng không biết nữa, nhưng bé đang cười kìa.\nCó lẽ tiếng 『Nga——n』 đó không mang ý nghĩa xấu đâu.」
- Lý do: Chủ ngữ của 笑顔でいるのだ là Mayu (TW: '但看她面帶笑容' — bé đang cười), không phải mệnh lệnh cho Hachiroku; VN cũ 'cứ giữ nụ cười đi' đổi chủ ngữ sai. Sửa câu đó thành 'nhưng bé đang cười kìa'.

### key 2637 — 双鉄 — gasp

- JP: 「どうにもできん？\n――いったい何のことを――――っ！！！」
- TW: 「無論如何都無法改變？——到底是什麼————啊！！！」
- VN cũ: 「Không thể thay đổi được?\n——Rốt cuộc là chuyện gì chứ————!!!」
- VN mới: 「Không thể thay đổi được?\n——Rốt cuộc là chuyện gì chứ————Ư!!!」
- Lý do: Sweep lost-gasp-trailing: JP ――――っ!!! cuối dòng, VN giữ dấu gạch + '!!!' mà mất っ; TW '啊!!!' cũng là tiếng thốt. Nhận fix của sweep: thêm Ư sau 4 dấu gạch.

### key 2762 — ハチロク — meaning

- JP: 「良かったのは、双鉄さまもですよ？、\n双鉄さまもまゆちゃんと、相性抜群でございますから」
- TW: 「這一點上雙鐵少爺您也一樣哦？您和小茉祐一定也很合得來的」
- VN cũ: 「Người tốt là, cả ngài Soutetsu nữa cơ?\nBởi vì ngài Soutetsu và bé Mayu, cũng rất hợp nhau mà.」
- VN mới: 「Điều tốt là, cả ngài Soutetsu nữa cơ?\nBởi vì ngài Soutetsu và bé Mayu, cũng rất hợp nhau mà.」
- Lý do: 良かったのは = 'điều tốt là', không phải 'người tốt là' — VN cũ biến tính từ 良かった thành danh từ chỉ người. TW '這一點上雙鐵少爺您也一樣哦？' xác nhận nghĩa 'điều tốt này cũng đúng với ngài'. Chỉ sửa cụm đầu.

### key 2790 — ハチロク — pronoun

- JP: 「それでは、失礼いたします。稀咲様、浦上様」
- TW: 「那我們先告辭了，稀咲小姐，浦上閣下」
- VN cũ: 「Vậy, chúng tôi xin phép. Kisaki, cô Urakami.」
- VN mới: 「Vậy, chúng tôi xin phép. Cô Kisaki, cô Urakami.」
- Lý do: Hachiroku xưng hô cực kỳ lễ phép; JP 稀咲様 (có 様) mà VN để tên trần 'Kisaki' là thiếu kính ngữ, lệch hẳn với 'cô Urakami' ngay sau đó. Sửa 'Kisaki' → 'cô Kisaki'.

### key 2815 — 双鉄 — terminology

- JP: 「そうした各地でのヒットが、[なごてつ,2]名護鉄や[とうかい,1]東峡鉄道――\n大廃線を生き残った大手鉄道事業者にも波及しました」
- TW: 「隨著這股熱潮的蔓延，連名古屋鐵路和東海鐵路——這些經歷過大廢線生存至今的大型鐵路公司都無法再置身事外」
- VN cũ: 「Những cú hit ở các nơi đó, đã lan rộng đến Nagotetsu và Đường sắt Toukyou——\nNhững doanh nghiệp đường sắt lớn đã sống sót qua đợt Đại bãi bỏ tuyến.」
- VN mới: 「Những cú hit ở các nơi đó, đã lan rộng đến Nagotetsu và Đường sắt Toukai——\nNhững doanh nghiệp đường sắt lớn đã sống sót qua đợt Đại bãi bỏ tuyến.」
- Lý do: Như 2216: furigana [とうかい,1] + TW 東海 = Toukai; VN cũ 'Toukyou' đọc sai. Sửa 'Đường sắt Toukai'.

## Lượt soát 2 (bắt buộc)

- Tổng 15 / soát lại 15 / bỏ 0 / sửa 0. Đã đọc lại toàn bộ 15 fix đối chiếu JP + TW; cả 15 đều giữ nguyên, không bỏ dòng nào, không sửa giá trị nào.
- Ghi chú lượt 2: 2392 sửa theo TW (JP よろしくおねがいいたします mơ hồ, TW mới rõ nghĩa 'xin cho em bế bé'); 2549 sửa theo TW (chủ ngữ đang cười là Mayu, TW '但看她面帶笑容'); 2426 sửa 'Khỏi' → 'Là' vì VN cũ không thành câu tiếng Việt; 2216/2815 đối chiếu furigana [とうかい,1] + TW 東海, chắc chắn là Toukai.

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
"1620" = "「——Ư!」"
"1621" = "「——————Ư!!!」"
"2164" = "「Lễ nghi——trong các buổi lễ kỷ niệm,\\nem vẫn xuất hiện trước mặt khách hàng.」"
"2216" = "「Nagotetsu là tuyến đường sắt tư nhân danh tiếng thì khỏi phải bàn rồi. Đường sắt Toukai, là công ty đã mua lại tuyến chính Toukai-dou của Teitetsu cũ, đoạn Mishima-Ousaka nhỉ.」"
"2262" = "「Ư!!」"
"2263" = "「Ư!!!」"
"2280" = "「Anyu~~Ư.」"
"2392" = "「V, vâng. Vậy thì——\\nXin cô cho em bế bé một chút ạ.」"
"2393" = "「Lâu rồi không gặp. Giám đốc chi nhánh——à không, cô Kisaki.\\nCùng với anh Migita và cô Hachiroku nữa.」"
"2426" = "「Là số phận……mà con bé chẳng thể nào thay đổi được,\\nchắc vậy.」"
"2549" = "「Thế nên tôi mới bảo em bình tĩnh. Tôi cũng không biết nữa, nhưng bé đang cười kìa.\\nCó lẽ tiếng 『Nga——n』 đó không mang ý nghĩa xấu đâu.」"
"2637" = "「Không thể thay đổi được?\\n——Rốt cuộc là chuyện gì chứ————Ư!!!」"
"2762" = "「Điều tốt là, cả ngài Soutetsu nữa cơ?\\nBởi vì ngài Soutetsu và bé Mayu, cũng rất hợp nhau mà.」"
"2790" = "「Vậy, chúng tôi xin phép. Cô Kisaki, cô Urakami.」"
"2815" = "「Những cú hit ở các nơi đó, đã lan rộng đến Nagotetsu và Đường sắt Toukai——\\nNhững doanh nghiệp đường sắt lớn đã sống sót qua đợt Đại bãi bỏ tuyến.」"
```

- Khối 15 khóa, parse bằng tomllib, 0 sai lệch giá trị so với JSON; jp/tw/old_vn khớp CSV3 tuyệt đối 15/15.

## Chờ Hieu / quan sát (không tính sai)

- Unification pass (đã chốt, KHÔNG tính vào 15 dòng này): 御一夜 dạng cũ 16 dòng — 'Ohimitera' 9 dòng (1662, 2130, 2467, 2647, 2662, 2710, 2725, 2792, 2801) và 'Đường sắt Ohito' 8 dòng (1670, 2096, 2135, 2161, 2412, 2467, 2468, 2494; 2467 mang cả hai dạng) → 'Ohitoyo' / 'Đường sắt Ohitoyo'; まいてつ 1 dòng (2816 'các Maitetsu' → 'các chủ tàu').
- 2319 (まゆ) 「んあーんっ」 → 'Nga——n.': っ cuối gắn với âm thanh em bé (sound-word) — theo quyết định 20/11 (っ gắn với từ âm thanh là gasp → thêm Ư, vd ああっ/はうっ) thì có thể cần 'Nga——nƯ.'; nhưng trong chính file này ああっ (2286) và んふっ (2307) đều được giữ không Ư ('A!?', 'Nfu'), và sweep cũng không liệt kê 2319. Giữ nguyên, chờ Hieu quyết có thêm Ư cho 2319 hay giữ quy ước hiện tại của file.
- 1619 (ハチロク) 「――ふっ――ふ、ふっ――くふふっ」 → '——Phù——ph, phù——kufufu.': 'kufufu' là phiên âm tiếng cười; giữ nguyên theo quy tắc ưu tiên gần tiếng Nhật gốc (Hieu 22:19), không tính sai.
- 2222 (まゆ) 「ふにゃあ」 → 'Oe.': tiếng bập bẹ của em bé diễn thành tiếng khóc 'oe' của trẻ VN — giữ nguyên (ngẫu hứng theo nhân vật/ngữ cảnh), không tính sai. Cùng họ: 2304 「ふぇ、ぇ……」 → 'Oe, e……' giữ nguyên.
- 2697: 'kính ống thủy sáng' (thay kính 水面計ガラス) — từ 'sáng' thừa nhưng không đổi nghĩa; giữ nguyên.
- 2622: Kisaki gọi người nghe 'em' — xác định người nghe là Hachiroku (cô đang lúng túng ở 2617–2618, Kisaki giục nói thẳng ý kiến); 'em' đúng, giữ nguyên.
- 3046 độc thoại: 'Lạnh lùng như băng——từ đó chợt lóe lên trong đầu tôi.' — câu hơi rối nhưng đủ nghĩa; giữ nguyên.

## Kết bài

File ハチロク01_こんにちわ赤ちゃん.txt.toml: 530 dòng đọc, 15 dòng sai (2,8%) — lỗi nhẹ, tập trung ở gasp っ bị mất (6 dòng, toàn bộ từ sweep) và vài lỗi dịch lẻ (Toukai đọc sai 2 dòng, xưng hô Kisaki 2 dòng, rò ký tự Hán 1 dòng, dịch sai 4 dòng). Không có lệch dòng, xoay chuỗi, nhiễm chéo hay dòng mồ côi. 16 dòng Ohimitera/Ohito + 1 dòng Maitetsu đã ghi vào danh sách unification pass, không tính vào tổng sai. 1 dòng chờ Hieu (2319). Khối TOML 15 khóa đã parse-kiểm chứng, sẵn sàng để gộp.

Kết bài
