# Audit: 真闇h1_長期熟成.txt.toml — 50/298 sai (16,8%)

- File: `真闇h1_長期熟成.txt.toml` — route 05_Mayami, 298 dòng script (monologue 147, thoại 真闇 76, thoại 双鉄H 75). Key 41–1552. TOML md5 `af87cd63e115c1890a4aa1a0a05fec4b`, không có bản trùng (chỉ 1 copy; các file `lr_真闇h1_*` là file khác). `[selections]` rỗng. Không có thẻ `%l` nào trong file (cả JP lẫn VN). Không có っ thô còn sót trong VN.
- Nội dung: cảnh H của Mayami ("ủ lâu năm") — Soutetsu bị say sóng nhiệt trong bồn tắm, Mayami cho gối đùi + quạt; trò chuyện về chuyện cô đã quá 25 tuổi còn độc thân và "ủ lâu năm" như rượu shochu; rồi quan hệ lần đầu: hôn, paizuri, oral, phá trinh, xuất tinh, hiệp hai, kết bằng chuyện con cái / gia đình mới.
- Phương pháp: đọc từng dòng JP + TW (CSV3) đối chiếu VN, kiểm tra đại từ theo người nghe, gasp theo quy tắc đã khóa, rên/SFX theo công thức nguyên âm + romaji fallback, quét máy bổ sung đại từ "em"/"anh"/"mình" toàn file.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất 298 dòng. TOML vs CSV3: 156 khác biệt — TẤT CẢ chỉ là TOML-2 làm phẳng `\n` thành khoảng trắng (hành vi đã biết, không phải lỗi); CSV3 là chuẩn cho danh sách sửa.
- Phân loại (50): đại từ 28, gasp 7, rên/nguyên âm 5, SFX 8, nghĩa 1, nhỏ 1.
- Đối thoại sai 27/151 (17,9%), độc thoại sai 23/147 (15,6%). Theo nhân vật: monologue 23, 双鉄H 13, 真闇 14.

## Đại từ — lỗi hệ thống "em"→"tôi" (28 dòng)

Mayami là người đối thoại DUY NHẤT của Soutetsu trong cả file (cô gọi cậu là 双ちゃん; cậu gọi cô là 真闇姉/"chị Mayami"). Theo quy tắc đã khóa, Soutetsu tự xưng "tôi" với Mayami — nhưng VN dùng "em" nhất quán ở cả thoại lẫn độc thoại (giống tiền lệ lr真闇追加02/03 và lr_真闇h1_僕のおねえちゃん, 22 dòng). Đã sửa toàn bộ 28 dòng, kiểm chứng từng dòng theo dòng kề. "em" của Mayami gọi Soutetsu (1131, 1171, 1142) GIỮ NGUYÊN — đó là cách cô xưng hô với cậu, đúng. "mình" trong độc thoại (1510 sở hữu, 1462 sở hữu, 1631/1675/1479/1420 "cửa mình") đều đúng theo tiền lệ, không sửa. Không có dòng nào Soutetsu tự xưng "anh".

## Gasp っ — sweep + tự tìm (7 dòng)

- Sweep: 5 mục cho file này — nhận nguyên 4 fix (1181, 1218, 1272, 1273), đã kiểm chứng đúng JP; 1 mục already-rendered (1092 んんん～～～っ! → "Ưm ưm ưm~~~~~~~~!") KHÔNG sửa — âm cắt đã được `~~~~` + `!` diễn đạt (tiền lệ ハチロク01 2319).
- Tự tìm: 1249 (はっ cuối dòng bị mất → "ha――", theo đúng tiền lệ trong chính file này: 1061 はっ――→"ha――"); 1065 + 1214 (くっ → "ư", mất gasp → "Ư", khớp 1059 くっ→"Ư" trong cùng file).
- Không sửa: 1812 （パタパタパタパタっ） — っ ở đây là tiếng quạt dừng đột ngột (âm vật thể, không phải hơi thở/gasp); TW cũng bỏ qua. 1112 あっ/これっ, 1225 るっ, 1241 中っ đều đúng quy tắc (gạch ngang / từ nội dung).

## Rên / SFX — quy tắc đã khóa

- Họ ひゃ/ひゅ/ひあ → romaji trong cảnh H: 1014 ひゃっ→"Hya" (xem cờ dưới), 1086 んひゅっ→"Nhyu" (một âm duy nhất, không tách "Ưm hyu").
- Công thức nguyên âm (VN = 1 + số う/ぅ): 1025 んううっ→"ưm ưư", 1091 んうぅっ→"Ưm ưư", 1048 ちゅうっ→"chuu".
- Họ fa/fu: 1021 ふや→"Phuya" (quy tắc đã khóa ふやぁ→"phuya"); 1071 ふあっ→"phua" giữ nguyên (đúng dạng romaji, chỉ khác chữ hoa với 1112 "Pua" — vị trí trong câu).
- SFX mất âm đầu / mất mora: 1069 くちゅっ→"kuchu" ×3, 1796 くちゅりっ→"Kuchuri", 1815 ぬチッ→"Nuchu", 1793 く→"ku", 1089 んぶっ→"Nbu" + ぷえっ→"Pue" (VN cũ "phuha" là nhầm với ぷはっ ở 1064 — đã kiểm chứng), 1094 (んぷ/ちゅ/ちゅる/ちゅむっ → "Npu/Chu/Churu/Chumu"), 1056 んふっ→"ưm fu" (bỏ "fu" thừa).

## Nghĩa (1 dòng)

- 1097: JP 「うん、双ちゃんのおちんちんを」 là câu cụt (を chờ tiếp nối ở 1135) — VN cũ thêm "thì sao." là bịa phần kết. Sửa về dạng cụt 「Ừm, chim của Sou-chan――」.

## Thuật ngữ / nhất quán trong file

- 長期熟成 = "ủ lâu năm" / "quá trình ủ lâu năm" nhất quán cả file (1223, 1121, 1264, 1267, 1078 "Cái bướm trinh nữ ủ lâu năm") — giữ nguyên, không sửa. Đây là phép ẩn dụ rượu shochu của Mayami, dịch đúng.
- おまんこ = "Cái bướm" nhất quán cả file (1186, 1066, 1078, 1151) — giữ nguyên trong audit (câu hỏi "chỗ đó" vs "lồn" của lr_真闇h1 vẫn chờ đợt thống nhất).
- のぼせる = "say sóng nhiệt" nhất quán cả file (1130, 1219, 1251) — giữ nguyên.
- 帝鉄/御一夜/運転体/整備体/タブレット: 0 dòng trong file này.
- ふっ → "phư" nhất quán cả file (1034, 1040, 1059, 1091) — giữ nguyên (xem cờ 1080).

## Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 50 giá trị sửa đối chiếu JP: **50/50 tái kiểm chứng, 0 bỏ, 0 sửa lại**. Kiểm chứng máy: JSON 50 mục dạng chuẩn (key chuỗi), khối TOML 50 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 50/50; diff-sanity: mỗi fix chỉ đổi đúng phần sửa mục tiêu.

## Cờ cho Hieu / vòng moan (không tự quyết)

1. **1014** (ひゃっ → "Hya"): đây là tiếng giật mình khi hôn, không phải rên lúc cao trào — áp dụng quy tắc họ-ひゃ cho cảnh H. Nếu Hieu muốn giữ "Á" cho tiếng giật mình thì hoàn lại 1 dòng này.
2. **Vòng moan**: 1058 (んちゅうっ→"ưm chụt" — mất nguyên âm dài, chưa sửa vì っ cuối dòng + quy ước "chụt" của file), 1080 (んふっ→"ưm phư" — mất っ cuối dòng; đối chiếu 1056 sửa "ưm fufu"→"ưm fu"), 1089 (ごくんっ→"ực" — mất ん phân biệt với ごくっ), 1792 (みちいいいいいいいいいっっ → "Phậpppppp!!" — 11 い JP vs 7 p VN, đếm theo mora?), 1801/1803/1822 (4 SFX xuất tinh khác nhau びゅぶっ/どびゅっ/びゅるるっ/んびゅるっ đều gộp thành "Phụt!" — phong cách SFX Việt hoá của file, có nên giữ hay tách romaji?), 1173 (気持ちよぉ → "sướng hơn nữaaaa" — kéo dài 4 a cho 1 nguyên âm dài).
3. **Nhỏ**: 1011 (どろって → "như đang" — mất sắc thái "đặc quánh" của どろ; giữ nguyên vì câu vẫn đúng nghĩa, chỉ mất sắc thái).
4. B19 vẫn park (không có tag %l hỏng trong file này).

## Đại từ (28 dòng)

### Key 821 — monologue

- JP: ……このリズムなら知っている。
これは、つまりは――
- TW: ……我知道這個節奏。這就是――
- Cũ: ……Nhịp điệu này thì em biết.
Nói cách khác, đây là――
- Sửa: ……Nhịp điệu này thì tôi biết.
Nói cách khác, đây là――

### Key 989 — 双鉄H

- JP: 「が、僕は性的なことにはぼんやりとしか知識が無いから、
どうしたものかと。――真闇姉に頼るにしても」
- TW: 「但是我對性只有最朦朧的了解，不知道該怎麼辦――只能看真闇姐的了」
- Cũ: 「Nhưng em chỉ có chút kiến thức mơ hồ về chuyện tình dục thôi,
nên không biết phải làm sao.――Dù có nhờ cậy chị Mayami đi nữa thì」
- Sửa: 「Nhưng tôi chỉ có chút kiến thức mơ hồ về chuyện tình dục thôi,
nên không biết phải làm sao.――Dù có nhờ cậy chị Mayami đi nữa thì」

### Key 1099 — 双鉄H

- JP: 「うむ。今夜は、昼間の続き――
ということになるのかと思って、それで……」
- TW: 「嗯，我在想今晚會不會繼續晨間的事――於是就……」
- Cũ: 「Ừm. Em cứ mải nghĩ xem đêm nay, liệu có phải là phần tiếp theo của lúc ban ngày――
hay không, thế nên……」
- Sửa: 「Ừm. Tôi cứ mải nghĩ xem đêm nay, liệu có phải là phần tiếp theo của lúc ban ngày――
hay không, thế nên……」

### Key 1101 — 双鉄H

- JP: 「うん。そう聞かせてもらっていたから、余計に悩んだ。
それで思考が、どうどうめぐりしてしまって――」
- TW: 「嗯，我知道，所以我才會更加煩惱。想啊想啊，最後自己繞了進去――」
- Cũ: 「Vâng. Vì đã nghe chị nói vậy nên em mới càng phiền não hơn.
Thế là dòng suy nghĩ cứ luẩn quẩn mãi――」
- Sửa: 「Vâng. Vì đã nghe chị nói vậy nên tôi mới càng phiền não hơn.
Thế là dòng suy nghĩ cứ luẩn quẩn mãi――」

### Key 1135 — 双鉄H

- JP: 「その――僕の、性器を」
- TW: 「就是――我的陰莖」
- Cũ: 「Đó là――dương vật của em.」
- Sửa: 「Đó là――dương vật của tôi.」

### Key 1161 — 双鉄H

- JP: 「僕は、
真闇姉がずっと、手付かずでいてくれたことが嬉しい」
- TW: 「我呢，很高興真闇姐一直靜靜地陪著我」
- Cũ: 「Em,
rất vui vì chị Mayami vẫn luôn giữ gìn bản thân trọn vẹn cho đến tận bây giờ.」
- Sửa: 「Tôi,
rất vui vì chị Mayami vẫn luôn giữ gìn bản thân trọn vẹn cho đến tận bây giờ.」

### Key 1165 — 双鉄H

- JP: 「それは、知ってる。
そうではなくて、何故僕は――」
- TW: 「我知道啊。我是奇怪為什麼我會――」
- Cũ: 「Chuyện đó thì em biết.
Nhưng ý em là, tại sao em lại――」
- Sửa: 「Chuyện đó thì tôi biết.
Nhưng ý tôi là, tại sao tôi lại――」

### Key 1168 — 双鉄H

- JP: 「だから僕は。真闇姉を味わってみたい」
- TW: 「所以我想嚐嚐真闇姐的味道」
- Cũ: 「Chính vì thế. Em muốn được thưởng thức chị Mayami.」
- Sửa: 「Chính vì thế. Tôi muốn được thưởng thức chị Mayami.」

### Key 1210 — 双鉄H

- JP: 「真闇姉……その――僕は、切ない」
- TW: 「真闇姐……我――挺難受的」
- Cũ: 「Chị Mayami……chuyện là――em, thấy rất khó chịu.」
- Sửa: 「Chị Mayami……chuyện là――tôi, thấy rất khó chịu.」

### Key 1251 — 双鉄H

- JP: 「そうか……僕は、考えすぎてノボせてしまったのか」
- TW: 「這樣啊……我想東西想太久，然後泡暈了嗎」
- Cũ: 「Ra vậy……Em suy nghĩ nhiều quá nên bị say sóng nhiệt sao.」
- Sửa: 「Ra vậy……Tôi suy nghĩ nhiều quá nên bị say sóng nhiệt sao.」

### Key 1416 — monologue

- JP: 思って、気づく。
ああそうだ。暑いではなく、はっきり熱い。
- TW: 原來如此。對啊，不是天氣熱，就是單純的發熱。
- Cũ: Nghĩ vậy, rồi em chợt nhận ra.
À đúng rồi. Không phải là nóng bức của thời tiết, mà rõ ràng là cơ thể đang phát sốt.
- Sửa: Nghĩ vậy, rồi tôi chợt nhận ra.
À đúng rồi. Không phải là nóng bức của thời tiết, mà rõ ràng là cơ thể đang phát sốt.

### Key 1469 — monologue

- JP: 安堵は、すぐさま欲に繋がる。
真闇姉の唇を、もっともっとと味わいたくなる。
- TW: 安心感勾引起心底裡的欲望，我開始更深一步地貪圖真闇姐嘴唇的味道。
- Cũ: Sự an tâm ngay lập tức chuyển hóa thành ham muốn.
Em muốn được thưởng thức đôi môi của chị Mayami nhiều hơn, nhiều hơn nữa.
- Sửa: Sự an tâm ngay lập tức chuyển hóa thành ham muốn.
Tôi muốn được thưởng thức đôi môi của chị Mayami nhiều hơn, nhiều hơn nữa.

### Key 1486 — monologue

- JP: 首の後ろが、搗きたての餅に張り付いているようで、
なのに顔から胸板にかけては、とても涼しい。
- TW: 後腦勺彷彿墊著一塊剛搗好的年糕。但是臉到胸膛卻又涼絲絲的。
- Cũ: Sau gáy em có cảm giác như đang dính chặt vào miếng bánh mochi vừa mới giã xong,
thế nhưng từ mặt xuống ngực lại rất mát mẻ.
- Sửa: Sau gáy tôi có cảm giác như đang dính chặt vào miếng bánh mochi vừa mới giã xong,
thế nhưng từ mặt xuống ngực lại rất mát mẻ.

### Key 1487 — monologue

- JP: 後ろ頭にこもった熱が、その下からただよう甘い匂いが、
あれほど悩んでいたことを、とても単純にしてくれる。
- TW: 後腦勺的熱量、頭下傳來的甜蜜氣息，解開了我腦海裡的一團亂麻。
- Cũ: Hơi nóng tích tụ sau gáy, cùng mùi hương ngọt ngào thoang thoảng từ bên dưới,
đã khiến những điều em từng phiền não trở nên vô cùng đơn giản.
- Sửa: Hơi nóng tích tụ sau gáy, cùng mùi hương ngọt ngào thoang thoảng từ bên dưới,
đã khiến những điều tôi từng phiền não trở nên vô cùng đơn giản.

### Key 1501 — monologue

- JP: 羊水のことはくわしく知らんが、
水の類がそうそう腐るものでないことは承知している。
- TW: 我不太了解羊水，但我知道水一類的東西並不容易變質。
- Cũ: Dù không rành về nước ối,
nhưng em biết các loại chất lỏng không dễ bị hỏng đến thế.
- Sửa: Dù không rành về nước ối,
nhưng tôi biết các loại chất lỏng không dễ bị hỏng đến thế.

### Key 1512 — monologue

- JP: 味わいたくて唇を舐めた舌先が、
開いた口に、そこから伸びて来た舌に甘く絡め取られる。
- TW: 我才舔了舔她的嘴唇嘗味道，她的舌頭就伸了過來，和我輕輕纏在了一起。
- Cũ: Đầu lưỡi em vừa liếm lên môi chị ấy để nếm thử,
đã bị chiếc lưỡi vươn ra từ khuôn miệng hé mở ấy quấn lấy đầy ngọt ngào.
- Sửa: Đầu lưỡi tôi vừa liếm lên môi chị ấy để nếm thử,
đã bị chiếc lưỡi vươn ra từ khuôn miệng hé mở ấy quấn lấy đầy ngọt ngào.

### Key 1517 — monologue

- JP: 見上げる視線のその先で、
真闇姉はひどく申し訳なさそうな顔になる。
- TW: 我抬頭一看，真闇姐的臉上滿是羞愧。
- Cũ: Theo hướng ánh mắt ngước lên của em,
chị Mayami mang một vẻ mặt vô cùng áy náy.
- Sửa: Theo hướng ánh mắt ngước lên của tôi,
chị Mayami mang một vẻ mặt vô cùng áy náy.

### Key 1519 — monologue

- JP: もっと近づきたくなって、体を密着させ、気づく。
僕の性器が、ガチガチに勃起してしまっている。
- TW: 我抱得更緊了一點，想跟她湊得更近一點，這時我才發現。我的陰莖已經硬邦邦地挺立起來了。
- Cũ: Em muốn đến gần hơn nữa, ép sát cơ thể vào nhau, rồi nhận ra.
Dương vật của em đã cương cứng lên từ lúc nào.
- Sửa: Tôi muốn đến gần hơn nữa, ép sát cơ thể vào nhau, rồi nhận ra.
Dương vật của tôi đã cương cứng lên từ lúc nào.

### Key 1529 — monologue

- JP: 真正面から顔を見つめれば、
真闇姉はそっと目を閉じる。
- TW: 我正面看起來真闇姐的臉，她便靜靜地閉上了眼睛。
- Cũ: Khi em nhìn thẳng vào gương mặt chị ấy,
chị Mayami nhẹ nhàng nhắm mắt lại.
- Sửa: Khi tôi nhìn thẳng vào gương mặt chị ấy,
chị Mayami nhẹ nhàng nhắm mắt lại.

### Key 1549 — monologue

- JP: 体を起こす。
- TW: 支起身體。
- Cũ: Em ngồi dậy.
- Sửa: Tôi ngồi dậy.

### Key 1561 — monologue

- JP: もじもじと体をよじるたび、
甘くてゆるい快感が、僕の下腹部に蓄積していく。
- TW: 每次忸怩起身體，甜蜜又舒緩的快感就會往我下腹部集聚。
- Cũ: Mỗi lần chị ấy ngượng ngùng vặn vẹo cơ thể,
một khoái cảm ngọt ngào, lâng lâng lại tích tụ nơi bụng dưới của em.
- Sửa: Mỗi lần chị ấy ngượng ngùng vặn vẹo cơ thể,
một khoái cảm ngọt ngào, lâng lâng lại tích tụ nơi bụng dưới của tôi.

### Key 1629 — monologue

- JP: 真闇姉がゆったりと、僕を仰いでくれてる。
その顔が、その胸が、僕の顔のすぐ真上にある。
- TW: 真闇姐在慢慢地給我搖團扇。她的臉蛋、胸膛都在我臉的正上方。
- Cũ: Chị Mayami đang thong thả quạt cho em.
Gương mặt ấy, vòng ngực ấy, đang ở ngay phía trên mặt em.
- Sửa: Chị Mayami đang thong thả quạt cho tôi.
Gương mặt ấy, vòng ngực ấy, đang ở ngay phía trên mặt tôi.

### Key 1642 — monologue

- JP: 僕の唇のすぐわきに、
真闇姉から零れた汗が落ちてくる。
- TW: 真闇姐的汗水滴落在我嘴唇的旁邊。
- Cũ: Ngay sát bên khóe môi em,
một giọt mồ hôi từ chị Mayami rơi xuống.
- Sửa: Ngay sát bên khóe môi tôi,
một giọt mồ hôi từ chị Mayami rơi xuống.

### Key 1651 — monologue

- JP: 真闇姉の舌が動くたび、
舌を、口内を舐められるたび、体がどんどん熱くなる。
- TW: 真闇姐的舌頭動的時候，舌頭、口腔每次被舔，我的身體都會越來越熱。
- Cũ: Mỗi khi lưỡi chị Mayami chuyển động,
mỗi khi lưỡi và khoang miệng bị liếm láp, cơ thể em lại càng nóng bừng lên.
- Sửa: Mỗi khi lưỡi chị Mayami chuyển động,
mỗi khi lưỡi và khoang miệng bị liếm láp, cơ thể tôi lại càng nóng bừng lên.

### Key 1660 — monologue

- JP: 真闇姉だって暑いのに、膝枕してずうっと僕だけ、
優しく仰ぎ続けてくれた。
- TW: 真闇姐肯定也很熱，但她一直為我提供膝枕，一直對我這麼溫柔。
- Cũ: Chị Mayami cũng đang rất nóng, vậy mà vẫn cho em gối đùi,
và dịu dàng quạt cho em suốt.
- Sửa: Chị Mayami cũng đang rất nóng, vậy mà vẫn cho tôi gối đùi,
và dịu dàng quạt cho tôi suốt.

### Key 1697 — monologue

- JP: 気持ちいいのだが、焦れてしまう。
もっと強くと望んでしまう。
- TW: 舒服歸舒服，卻平復不了心頭的焦急。總會有進一步更強烈的渴求。
- Cũ: Dù rất sướng, nhưng lại khiến em bồn chồn.
Em lại khao khát mãnh liệt hơn nữa.
- Sửa: Dù rất sướng, nhưng lại khiến tôi bồn chồn.
Tôi lại khao khát mãnh liệt hơn nữa.

### Key 1718 — monologue

- JP: その熱は体の奥に火を灯し、
のぼせによってボヤけてた感覚を明確にしてくれる。
- TW: 這股熱度點燃了我心裡的慾火，熱昏頭而朦朧的感覺變得明確了起來。
- Cũ: Hơi ấm ấy thắp lên ngọn lửa từ sâu thẳm bên trong cơ thể em,
làm rõ nét lại những cảm giác đang mờ mịt vì cơn say sóng nhiệt.
- Sửa: Hơi ấm ấy thắp lên ngọn lửa từ sâu thẳm bên trong cơ thể tôi,
làm rõ nét lại những cảm giác đang mờ mịt vì cơn say sóng nhiệt.

### Key 1728 — monologue

- JP: 心地よい風が柔らかく吹く。
ほてった体を冷ましてくれる。
- TW: 陣陣令人心曠神怡的微風吹來，讓我燥熱的身體感到些許涼爽。
- Cũ: Cơn gió dễ chịu nhè nhẹ thổi qua.
Làm dịu đi cơ thể đang nóng hừng hực của em.
- Sửa: Cơn gió dễ chịu nhè nhẹ thổi qua.
Làm dịu đi cơ thể đang nóng hừng hực của tôi.

## Gasp っ (7 dòng)

### Key 1065 — 真闇

- JP: 「んっ――くっ――」
- TW: 「嗯――唔――」
- Cũ: 「Ưm――ư――」
- Sửa: 「Ưm――Ư――」

### Key 1181 — 真闇

- JP: 「痛っ――～～～～～っ！！」
- TW: 「痛――～～～～～！！」
- Cũ: 「Đau――~~~~~!!」
- Sửa: 「Đau――~~~~~Ư!!」

### Key 1214 — 双鉄H

- JP: 「真闇姉の、膣の……中……あっ――
うねって―――ひだっ、これっ――くっ」
- TW: 「真闇姐的小穴……裡……啊――很蜿蜒――這是什麼――唔」
- Cũ: 「Bên trong……âm đạo, của chị Mayami……a――
uốn lượn――nếp gấp này, là sao――ư.」
- Sửa: 「Bên trong……âm đạo, của chị Mayami……a――
uốn lượn――nếp gấp này, là sao――Ư.」

### Key 1218 — 双鉄H

- JP: 「真闇姉、なにを――っ！？」
- TW: 「真闇姐，你做什麼――！？」
- Cũ: 「Chị Mayami, làm gì――!?」
- Sửa: 「Chị Mayami, làm gì――Ư!?」

### Key 1249 — 双鉄H

- JP: 「な――んだ――これ、はっ――」
- TW: 「這是――怎麼――回事――」
- Cũ: 「Cái――gì――thế này――」
- Sửa: 「Cái――gì――thế này――ha――」

### Key 1272 — 双鉄H

- JP: 「っ！」
- TW: 「！」
- Cũ: 「!」
- Sửa: 「Ư!」

### Key 1273 — 双鉄H

- JP: 「っ！！？」
- TW: 「！！？」
- Cũ: 「!!?」
- Sửa: 「Ư!!?」

## Rên/nguyên âm (5 dòng)

### Key 1014 — 真闇

- JP: 「ひゃっ！？　あ……んっ――」
- TW: 「呀！？　啊……嗯――」
- Cũ: 「Á!? A……ưm――」
- Sửa: 「Hya!? A……ưm――」

### Key 1025 — 真闇

- JP: 「ひ――んっ――双ちゃんの――亀頭――あっ――
こすれ、て――めくれっ――んううっ！」
- TW: 「咿――嗯――小雙的――龜頭――啊――磨蹭――翻――嗯嗚！」
- Cũ: 「Hii――ưm――Quy đầu――của Sou-chan――a――
đang cọ xát――lật lên――ưm ư!」
- Sửa: 「Hii――ưm――Quy đầu――của Sou-chan――a――
đang cọ xát――lật lên――ưm ưư!」

### Key 1048 — 真闇

- JP: 「はぷっ――ンッ――れるっ――ちゅうっ――れろんっ」
- TW: 「啊嗚――嗯――舔――啾――舔」
- Cũ: 「Hapu――ưm――rột――chu――rột.」
- Sửa: 「Hapu――ưm――rột――chuu――rột.」

### Key 1086 — 真闇

- JP: 「んひゅっ！？」
- TW: 「嗯呀！？」
- Cũ: 「Ưm hyu!?」
- Sửa: 「Nhyu!?」

### Key 1091 — 真闇

- JP: 「んうぅっ――これっ――あたってっ――
子宮っ――こつん、って――ふっ――あんっ！」
- TW: 「嗯嗚――這個――碰到了――子宮――頂到了――呼――啊嗯！」
- Cũ: 「Ưm ư――cái này――chạm vào rồi――
Tử cung――cộc một cái――phư――a ưm!」
- Sửa: 「Ưm ưư――cái này――chạm vào rồi――
Tử cung――cộc một cái――phư――a ưm!」

## SFX (8 dòng)

### Key 1021 — 真闇

- JP: 「ふや……んっ――きもち、い――」
- TW: 「呼……嗯――好舒服――」
- Cũ: 「Phu……ưm――sướng, quá――」
- Sửa: 「Phuya……ưm――sướng, quá――」

### Key 1056 — 真闇

- JP: 「ちゅっ――んっ……んちゅっ――れるっ――れろっ
――ん……んふっ……ふっ」
- TW: 「啾――嗯……嗯啾――舔――舔――嗯……嗯唔……呼」
- Cũ: 「Chụt――ưm……ưm chụt――liếm――liếm
――ưm……ưm fufu……fu」
- Sửa: 「Chụt――ưm……ưm chụt――liếm――liếm
――ưm……ưm fu……fu」

### Key 1069 — 真闇

- JP: 「んっ……よだれ……ね？――
ん～～っ――くちゅっ、くちゅっ、くちゅっ」
- TW: 「嗯……唾沫吧……？――嗯～～――咕啾、咕啾、咕啾」
- Cũ: 「Ưm……nước bọt……hả?――
Ưm~~――chu chu chu.」
- Sửa: 「Ưm……nước bọt……hả?――
Ưm~~――kuchu kuchu kuchu.」

### Key 1089 — 真闇

- JP: 「んぶっ！？　んっ――ごくっ――ぷえっ――あっ――
んっ――じゅるっ――ごくっ――ごくんっ――ごくっ」
- TW: 「嗯唔！？　嗯――咕嘟――噗哈――啊――嗯――啾嚕――咕嘟――咕嚕――咕嘟」
- Cũ: 「Ưm!? Ưm――ực――phuha――a――
ưm――rột――ực――ực――ực.」
- Sửa: 「Nbu!? Ưm――ực――Pue――a――
ưm――rột――ực――ực――ực.」

### Key 1094 — 真闇

- JP: 「んっ！　んぷ――ちゅ――んっ、ちゅる――ちゅむっ」
- TW: 「嗯！　嗯唔――啾――嗯、啾嚕――啾唔」
- Cũ: 「Ưm! Ưm――chụt――ưm, chụt――chụt.」
- Sửa: 「Ưm! Npu――Chu――ưm, Churu――Chumu.」

### Key 1793 — monologue

- JP: （みちっ――く、ちっ）
- TW: （呲――哧溜）
- Cũ: （Mút――chu, chụt）
- Sửa: （Mút――ku, chụt）

### Key 1796 — monologue

- JP: （くちゅりっ）
- TW: （咕啾）
- Cũ: （Chụt）
- Sửa: （Kuchuri）

### Key 1815 — monologue

- JP: （ぬチッ――ぬるんっ）
- TW: （啾――咻嚕）
- Cũ: （Chu――trượt）
- Sửa: （Nuchu――trượt）

## Nghĩa (1 dòng)

### Key 1097 — 真闇

- JP: 「うん、双ちゃんのおちんちんを」
- TW: 「嗯，小雙的雞雞」
- Cũ: 「Ừm, chim của Sou-chan thì sao.」
- Sửa: 「Ừm, chim của Sou-chan――」

## Nhỏ (1 dòng)

### Key 1064 — 真闇

- JP: 「ん――ごくっ――ごくっ――ん……あ……ぷはっ――
きゃっ！？」
- TW: 「嗯――咕嘟――咕嘟――嗯……啊……噗哈――呀！？」
- Cũ: 「Ưm――ực――ực――ưm……a……phuha――
kya!?」
- Sửa: 「Ưm――ực――ực――ưm……a……phuha――
Kya!?」

## Khối TOML đã kiểm chứng (50 khóa, parse đúng, 0 sai lệch)

```toml
[script]
"821" = "……Nhịp điệu này thì tôi biết.\\nNói cách khác, đây là――"
"989" = "「Nhưng tôi chỉ có chút kiến thức mơ hồ về chuyện tình dục thôi,\\nnên không biết phải làm sao.――Dù có nhờ cậy chị Mayami đi nữa thì」"
"1014" = "「Hya!? A……ưm――」"
"1021" = "「Phuya……ưm――sướng, quá――」"
"1025" = "「Hii――ưm――Quy đầu――của Sou-chan――a――\\nđang cọ xát――lật lên――ưm ưư!」"
"1048" = "「Hapu――ưm――rột――chuu――rột.」"
"1056" = "「Chụt――ưm……ưm chụt――liếm――liếm\\n――ưm……ưm fu……fu」"
"1064" = "「Ưm――ực――ực――ưm……a……phuha――\\nKya!?」"
"1065" = "「Ưm――Ư――」"
"1069" = "「Ưm……nước bọt……hả?――\\nƯm~~――kuchu kuchu kuchu.」"
"1086" = "「Nhyu!?」"
"1089" = "「Nbu!? Ưm――ực――Pue――a――\\nưm――rột――ực――ực――ực.」"
"1091" = "「Ưm ưư――cái này――chạm vào rồi――\\nTử cung――cộc một cái――phư――a ưm!」"
"1094" = "「Ưm! Npu――Chu――ưm, Churu――Chumu.」"
"1097" = "「Ừm, chim của Sou-chan――」"
"1099" = "「Ừm. Tôi cứ mải nghĩ xem đêm nay, liệu có phải là phần tiếp theo của lúc ban ngày――\\nhay không, thế nên……」"
"1101" = "「Vâng. Vì đã nghe chị nói vậy nên tôi mới càng phiền não hơn.\\nThế là dòng suy nghĩ cứ luẩn quẩn mãi――」"
"1135" = "「Đó là――dương vật của tôi.」"
"1161" = "「Tôi,\\nrất vui vì chị Mayami vẫn luôn giữ gìn bản thân trọn vẹn cho đến tận bây giờ.」"
"1165" = "「Chuyện đó thì tôi biết.\\nNhưng ý tôi là, tại sao tôi lại――」"
"1168" = "「Chính vì thế. Tôi muốn được thưởng thức chị Mayami.」"
"1181" = "「Đau――~~~~~Ư!!」"
"1210" = "「Chị Mayami……chuyện là――tôi, thấy rất khó chịu.」"
"1214" = "「Bên trong……âm đạo, của chị Mayami……a――\\nuốn lượn――nếp gấp này, là sao――Ư.」"
"1218" = "「Chị Mayami, làm gì――Ư!?」"
"1249" = "「Cái――gì――thế này――ha――」"
"1251" = "「Ra vậy……Tôi suy nghĩ nhiều quá nên bị say sóng nhiệt sao.」"
"1272" = "「Ư!」"
"1273" = "「Ư!!?」"
"1416" = "Nghĩ vậy, rồi tôi chợt nhận ra.\\nÀ đúng rồi. Không phải là nóng bức của thời tiết, mà rõ ràng là cơ thể đang phát sốt."
"1469" = "Sự an tâm ngay lập tức chuyển hóa thành ham muốn.\\nTôi muốn được thưởng thức đôi môi của chị Mayami nhiều hơn, nhiều hơn nữa."
"1486" = "Sau gáy tôi có cảm giác như đang dính chặt vào miếng bánh mochi vừa mới giã xong,\\nthế nhưng từ mặt xuống ngực lại rất mát mẻ."
"1487" = "Hơi nóng tích tụ sau gáy, cùng mùi hương ngọt ngào thoang thoảng từ bên dưới,\\nđã khiến những điều tôi từng phiền não trở nên vô cùng đơn giản."
"1501" = "Dù không rành về nước ối,\\nnhưng tôi biết các loại chất lỏng không dễ bị hỏng đến thế."
"1512" = "Đầu lưỡi tôi vừa liếm lên môi chị ấy để nếm thử,\\nđã bị chiếc lưỡi vươn ra từ khuôn miệng hé mở ấy quấn lấy đầy ngọt ngào."
"1517" = "Theo hướng ánh mắt ngước lên của tôi,\\nchị Mayami mang một vẻ mặt vô cùng áy náy."
"1519" = "Tôi muốn đến gần hơn nữa, ép sát cơ thể vào nhau, rồi nhận ra.\\nDương vật của tôi đã cương cứng lên từ lúc nào."
"1529" = "Khi tôi nhìn thẳng vào gương mặt chị ấy,\\nchị Mayami nhẹ nhàng nhắm mắt lại."
"1549" = "Tôi ngồi dậy."
"1561" = "Mỗi lần chị ấy ngượng ngùng vặn vẹo cơ thể,\\nmột khoái cảm ngọt ngào, lâng lâng lại tích tụ nơi bụng dưới của tôi."
"1629" = "Chị Mayami đang thong thả quạt cho tôi.\\nGương mặt ấy, vòng ngực ấy, đang ở ngay phía trên mặt tôi."
"1642" = "Ngay sát bên khóe môi tôi,\\nmột giọt mồ hôi từ chị Mayami rơi xuống."
"1651" = "Mỗi khi lưỡi chị Mayami chuyển động,\\nmỗi khi lưỡi và khoang miệng bị liếm láp, cơ thể tôi lại càng nóng bừng lên."
"1660" = "Chị Mayami cũng đang rất nóng, vậy mà vẫn cho tôi gối đùi,\\nvà dịu dàng quạt cho tôi suốt."
"1697" = "Dù rất sướng, nhưng lại khiến tôi bồn chồn.\\nTôi lại khao khát mãnh liệt hơn nữa."
"1718" = "Hơi ấm ấy thắp lên ngọn lửa từ sâu thẳm bên trong cơ thể tôi,\\nlàm rõ nét lại những cảm giác đang mờ mịt vì cơn say sóng nhiệt."
"1728" = "Cơn gió dễ chịu nhè nhẹ thổi qua.\\nLàm dịu đi cơ thể đang nóng hừng hực của tôi."
"1793" = "（Mút――ku, chụt）"
"1796" = "（Kuchuri）"
"1815" = "（Nuchu――trượt）"
```

## Kết bài

File 真闇h1_長期熟成: 298 dòng đã đọc hết, 50 dòng sai (16,8%) — lỗi lớn nhất là hệ thống đại từ "em"→"tôi" của Soutetsu với Mayami (28 dòng), còn lại là gasp/rên/SFX theo các quy tắc đã khóa; không có lệch hàng, không có dòng mồ côi, không có thuật ngữ chờ sửa trong file. Mọi fix đã qua lượt soát 2 đầy đủ và kiểm chứng máy (JSON/TOML/CSV3 khớp tuyệt đối). Các cờ SFX/rên còn lại chuyển cho vòng moan; 1 phán đoán (1014) chờ Hieu.
