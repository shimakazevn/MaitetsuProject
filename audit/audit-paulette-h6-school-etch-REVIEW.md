# Audit: Paulette h6_あなたとふたりの学園エッチ — 36 dòng Việt sai (đã đối chiếu JP + TW)

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa từng dòng: 304 dòng (độc thoại 162, Paulette 80, Soutetsu 62), đối chiếu JP + TW từ CSV3 và TOML-2.
- CSV vs TOML: 0 khác biệt thực chất (167 khác biệt thô chỉ ở `\n`/khoảng trắng); tập key bằng nhau (304); `[selections]` rỗng; thẻ `%l`: 0 hỏng; không có key trùng; không có dòng VN trống; VN==TW 0.
- md5: `1a184880b82bce1ce58a67cbb3a5f923` — không trùng với bất kỳ file nào trong 227 file TOML (không có bản sao; bản sửa áp dụng cho 1 file duy nhất).
- Đọc toàn bộ 304 dòng phát hiện 36 dòng sai. Rà soát chéo với sweep gasp っ và quét máy tính (pronoun sweep với `\n` chuẩn hoá trước, quét `\bchu\b`/`\bKua\b`/`\bNky\w*`/`\bHouhehu\b`, kiểm tra VN trùng và JP trùng) bắt thêm các dòng ngoài lần đọc đầu.
- Rà soát chéo với sweep gasp っ: sweep có 11 mục trong file này, trong đó 833 là "already-rendered" (không phải bản sửa). 10 bản sửa còn lại: 8 mục audit xác nhận cùng giá trị (774, 790, 814, 816, 817, 819, 1290, 1377); 1 mục audit SỬA LẠI giá trị sweep (1271: sweep chỉ có 1 Ư, JP có 2 っ nên sửa thành 2 Ư — xem chi tiết); 1 mục audit MỞ RỘNG giá trị sweep (784: sweep chỉ thêm Ư, audit sửa thêm わらひ→"ehm"). Audit phát hiện thêm 2 dòng gasp mà sweep BỎ SÓT trong file này (815: っ ở đầu dòng; 850: hai っ cuối dòng). Mục 833 đã được giải quyết: sweep ghi "already-rendered", fix rỗng — audit đồng ý (các tiếng nấc đã được diễn: "Ưm", "phù", "a", "ư", "ư a", "ưm"), KHÔNG đưa vào danh sách sửa.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ 36/36 bản sửa đối chiếu JP (đúng 36, 0 bị loại). Kiểm tra lần hai cũng xác nhận: không có bản sửa nào thừa hưởng lỗi xưng hô của dòng khác (không có dòng lệch vị trí), không có khoảng trắng thừa trước `\n`, không có dấu 。 thay cho dấu ., các âm thở ghép viết liền một từ ("Kyaphù", "Hyafu", "Hí-hề-phù-ha-ha-hí", "Hôu-hê-hu").
- Quy ước bản sửa: bản sửa viết MỘT DÒNG (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công — theo quyết định 19/11 của Hieu (game tự ngắt dòng, `\n` thủ công không quan trọng). Điểm này KHÁC với h1–h4 (vốn giữ `\n` trong bản sửa). File TOML gốc cũng lưu các giá trị này một dòng với khoảng trắng, nên khối TOML dưới đây dán vào khớp đúng dạng đó.

## Kết luận về cơ chế lỗi

- Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương: file sạch về cấu trúc. Chỉ số VN trùng trong file (2 nhóm) đều hợp lệ — `「Ư——」` ×2 (803: JP `「ぅっ――」`; 771: JP `「っ――」` — hai tiếng nấc gần giống nhau, cùng diễn "Ư" là chấp nhận được); `（Siết chặt!!!）` ×2 (1566: JP きゅううううううっっ; 1577: JP きゅううううううっ — cùng một kiểu siết, khác nhau chỉ ở số っ cuối, diễn giống nhau là chấp nhận được).
- Lỗi chủ đạo là xưng hô hệ thống: Soutetsu tự xưng "anh" 12/12 lần trong thoại (chỉ có 1 lần "tôi" đúng trước khi sửa: 1574) — cùng lỗi hệ thống như h1/h2/h3/h4/h5. Độc thoại không có lần "Anh" nào sai.
- Cụm lỗi ちゅ→"chu": 4 dòng (840, 847, 850, 856) — ちゅるっ/ちゅむっ/ちゅう đều bị dịch "chu" trong khi file dịch các âm này là "chụt" ở mọi chỗ khác (802, 842, 873). Đây là cụm không nhất quán nội bộ file, không phải biến thể có chủ ý.
- Thở gấp: 11 dòng — 8 sweep đã có (trong đó 1271 sai thiếu 1 Ư), 2 sweep bỏ sót (815, 850), 1 mở rộng sweep (784). Bài học: sweep B1/B2 yêu cầu đúng một っ nên các dòng nhiều っ hoặc っ ở đầu dòng dài dễ lọt; audit đọc ngữ nghĩa vẫn bắt được.
- Tiếng thở La-tinh: 6 dòng (きゃふ/ひゃふ/きゅ-squeal dài/くぁ×2/んきゅん) — cùng họ lỗi như h1/h2/h3/h4/h5; riêng きゃ độc lập (836: "Kya") là tiếng ré, KHÔNG tính là sai (xem dưới).
- Sai hướng SFX: 1 dòng (1586: ずっ→"Trượt" thay vì "Phập") — cùng lỗi hướng như h4 1609 (ぬぶ→"Phập"); quy tắc hướng cần đối chiếu JP từng âm.
- Lời nói ngọng: 2 dòng (784, 835) + 850 (gộp trong gasp) — theo tiền lệ h3 1154, diễn ngọng bằng chính tả Việt có gạch nối.

### Ghi chú về hai điểm sweep khác audit (1271, 784)

- 1271: JP `震えてっ――っ！？` có HAI っ (một sau 震えて, một sau ――). Sweep chỉ sửa っ cuối (`"——Ư!?"`). Theo quy tắc một Ư cho một っ (tiền lệ addendum sweep: h7 1270 `――っっ`→`"——ƯƯ"`, lr_ふかみh2 1063 `ん～～～っっっ`→`"ưm~~~ƯƯƯ"`), bản sửa audit là `"run rẩyƯ——Ư!?"` (Ư dính ngay sau "run rẩy" cho 震えてっ, Ư sau "——" cho ――っ).
- 784: sweep chỉ thêm Ư cuối (`"…cũng——Ư!!!!"`). Audit giữ Ư đó và sửa thêm わらひ→"ehm" (わらひ là nói ngọng của わたし, không phải "em" chuẩn).

## Chi tiết dòng sai

### Xưng hô (12 dòng)

**Key 738 (双鉄)**
- JP: `「はっきり言うんだ。ポーレット。学園時代の僕ならば、\n今よりさらに、その手のことには理解が薄いぞ？」`
- TW: `「你要說清楚，波萊特。如果是學生時代的我，這方面的知識可要少很多」`
- VN cũ: `「Nói rõ ra đi, Paulette. Nếu là anh thời học sinh,\nhiểu biết về mấy chuyện đó còn kém xa bây giờ đấy nhé?」`
- Sửa: `「Nói rõ ra đi, Paulette. Nếu là tôi thời học sinh, hiểu biết về mấy chuyện đó còn kém xa bây giờ đấy nhé?」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP 学園時代の僕ならば) → "Tôi".

**Key 740 (双鉄)**
- JP: `「どうしたい、とは、何についてだ？\nはっきりいってもらえねばわからん」`
- TW: `「你說的做是要做什麼啊？不說清楚我可不明白」`
- VN cũ: `「Muốn thế nào, là về chuyện gì cơ?\nEm không nói rõ thì anh không hiểu đâu.」`
- Sửa: `「Muốn thế nào, là về chuyện gì cơ? Em không nói rõ thì tôi không hiểu đâu.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP はっきりいってもらえねばわからん, chủ ngữ là Soutetsu) → "Tôi".

**Key 866 (双鉄)**
- JP: `「ああ。動こう。だが――」`
- TW: `「嗯。那我就動，但是——」`
- VN cũ: `「Ừ. Anh sẽ cử động. Nhưng mà——」`
- Sửa: `「Ừ. Tôi sẽ cử động. Nhưng mà——」`
- Lý do: Soutetsu tự xưng "Anh" trong thoại (JP 動こう) → "Tôi".

**Key 879 (双鉄)**
- JP: `「ああ。僕もだ。ポーレットのことが大好きだ」`
- TW: `「嗯，我也一樣，我也最喜歡你了」`
- VN cũ: `「Ừ. Anh cũng vậy. Anh rất yêu Paulette.」`
- Sửa: `「Ừ. Tôi cũng vậy. Tôi rất yêu Paulette.」`
- Lý do: Soutetsu tự xưng "Anh" ×2 trong thoại (JP 僕もだ) → "Tôi" ×2.

**Key 885 (双鉄)**
- JP: `「ポーレットがもし同級にいれば、そのことに。\n僕もあるいは、気づけていたのかもしれないな」`
- TW: `「如果我跟你同年級的話，我也許就能早些發現這一點了」`
- VN cũ: `「Nếu Paulette học cùng lớp, có lẽ.\nAnh đã nhận ra điều đó sớm hơn rồi.」`
- Sửa: `「Nếu Paulette học cùng lớp, có lẽ. Tôi đã nhận ra điều đó sớm hơn rồi.」`
- Lý do: Soutetsu tự xưng "Anh" trong thoại (JP 僕もあるいは、気づけていたのかもしれないな) → "Tôi".

**Key 899 (双鉄)**
- JP: `「僕も、もっと。ポーレットの熱を感じたい」`
- TW: `「我也想多感受感受你的溫度」`
- VN cũ: `「Anh cũng muốn, cảm nhận hơi nóng của Paulette nhiều hơn nữa.」`
- Sửa: `「Tôi cũng muốn, cảm nhận hơi nóng của Paulette nhiều hơn nữa.」`
- Lý do: Soutetsu tự xưng "Anh" trong thoại (JP 僕も、もっと) → "Tôi".

**Key 900 (双鉄)**
- JP: `「僕もだ――ポーレット」`
- TW: `「我也愛你——波萊特」`
- VN cũ: `「Anh cũng vậy——Paulette」`
- Sửa: `「Tôi cũng vậy——Paulette」`
- Lý do: Soutetsu tự xưng "Anh" trong thoại (JP 僕もだ) → "Tôi".

**Key 903 (双鉄)**
- JP: `「つまり、ポーレット。僕は君にも――\nポーレットにも、好きに動いて欲しいのだ」`
- TW: `「我的意思是，波萊特。我想讓你也——想怎麼動就怎麼動」`
- VN cũ: `「Nghĩa là, Paulette à. Anh cũng muốn em——\nMuốn Paulette cũng tự do cử động theo ý thích.」`
- Sửa: `「Nghĩa là, Paulette à. Tôi cũng muốn em—— Muốn Paulette cũng tự do cử động theo ý thích.」`
- Lý do: Soutetsu tự xưng "Anh" trong thoại (JP 僕は君にも) → "Tôi".

**Key 909 (双鉄)**
- JP: `「もっとだ。全部。僕の全部を――\nポーレットに、呑み込んで欲しい」`
- TW: `「我還想要，我想讓我的全部都被你吞進去」`
- VN cũ: `「Nữa đi. Tất cả. Toàn bộ con người anh——\nAnh muốn Paulette nuốt trọn lấy.」`
- Sửa: `「Nữa đi. Tất cả. Toàn bộ con người tôi—— Tôi muốn Paulette nuốt trọn lấy.」`
- Lý do: Soutetsu tự xưng "anh" ×2 trong thoại (JP 僕の全部を) → "Tôi" ×2.

**Key 924 (双鉄)**
- JP: `「いいのか？　どろどろに汚してしまうぞ？」`
- TW: `「沒關係嗎？這樣會弄髒的」`
- VN cũ: `「Có sao không? Anh sẽ làm bẩn nhầy nhụa hết đấy nhé?」`
- Sửa: `「Có sao không? Tôi sẽ làm bẩn nhầy nhụa hết đấy nhé?」`
- Lý do: Soutetsu tự xưng "Anh" trong thoại (JP どろどろに汚してしまうぞ) → "Tôi".

**Key 935 (双鉄)**
- JP: `「――これほどまでに魅力的な胸だったとは、\nさすがに思えんからな」`
- TW: `「真沒想到你的胸部這麼有魅力」`
- VN cũ: `「——Quả thực anh không thể ngờ,\nngực em lại quyến rũ đến nhường này đấy.」`
- Sửa: `「——Quả thực tôi không thể ngờ, ngực em lại quyến rũ đến nhường này đấy.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP さすがに思えんからな, chủ ngữ là Soutetsu) → "Tôi".

**Key 946 (双鉄)**
- JP: `「これでは、足りん。\n僕が、ポーレットのおっぱいを“使う”のならば」`
- TW: `「這樣還不夠。如果要說我“用”你的胸的話」`
- VN cũ: `「Thế này thì, chưa đủ.\nNếu anh muốn 'sử dụng' ngực của Paulette.」`
- Sửa: `「Thế này thì, chưa đủ. Nếu tôi muốn 'sử dụng' ngực của Paulette.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP 僕が、ポーレットのおっぱいを“使う”のならば) → "Tôi".

### Thở gấp っ bị bỏ mất (11 dòng)

**Key 774 (双鉄)**
- JP: `「っ！！？」`
- TW: `「呃！！？」`
- VN cũ: `「!!?」`
- Sửa: `「Ư!!?」`
- Lý do: JP 「っ！！？」 bị bỏ mất trong VN ("!!?") — sweep đã sửa, giá trị khớp (sweep-confirmed).

**Key 790 (ポーレット)**
- JP: `「フ、ァッ！――あっ！　おっぱい――そこ――\nさきっぽ――ちく、び――っ！」`
- TW: `「呼、啊！——啊！胸部——那裡——前端——乳頭！」`
- VN cũ: `「Phù, a!——A! Ngực——chỗ đó——\nĐầu vú——núm, vú——!」`
- Sửa: `「Phù, a!——A! Ngực——chỗ đó—— Đầu vú——núm, vú——Ư!」`
- Lý do: JP ちく、び――っ！ (trailing っ sau dấu gạch dài) bị bỏ mất trong VN ("——!") — sweep đã sửa, giá trị khớp (sweep-confirmed).

**Key 814 (双鉄)**
- JP: `「っ！」`
- TW: `「啊！」`
- VN cũ: `「っ!」`
- Sửa: `「Ư!」`
- Lý do: JP 「っ！」 bị bỏ mất trong VN (bản Việt còn nguyên っ) — sweep đã sửa, giá trị khớp (sweep-confirmed).

**Key 815 (ポーレット)**
- JP: `「っ！　ふあっ！　あっ――んうっ――ちゅっ！」`
- TW: `「啊！呼啊！啊——嗯——啾！」`
- VN cũ: `「! Phù! A——ưm——chụt!」`
- Sửa: `「Ư! Phù! A——ưm——chụt!」`
- Lý do: JP っ！ ở ĐẦU dòng bị bỏ mất trong VN ("! Phù!…") — sweep BỎ SÓT (leading gasp trong dòng dài); sửa theo quy tắc っ→Ư.

**Key 816 (双鉄)**
- JP: `「っ！　――っ！？」`
- TW: `「啊！嗯！？」`
- VN cũ: `「A! ——!?」`
- Sửa: `「A! ——Ư!?」`
- Lý do: JP 「っ！　――っ！？」: っ đầu → "A" (tiếng nấc sắc), ――っ → Ư — sweep đã sửa, giá trị khớp (sweep-confirmed).

**Key 817 (双鉄)**
- JP: `「っ！！」`
- TW: `「啊！！」`
- VN cũ: `「!!」`
- Sửa: `「Ư!!」`
- Lý do: JP 「っ！！」 bị bỏ mất trong VN ("!!") — sweep đã sửa, giá trị khớp (sweep-confirmed).

**Key 819 (双鉄)**
- JP: `「っ！？」`
- TW: `「啊！？」`
- VN cũ: `「!?」`
- Sửa: `「Ư!?」`
- Lý do: JP 「っ！？」 bị bỏ mất trong VN ("!?") — sweep đã sửa, giá trị khớp (sweep-confirmed).

**Key 850 (ポーレット)**
- JP: `「ん……ふぁ……っ――ほーへふ……ふん……んっ――\nちゅ――ちゅむっ――ねろおっ――れるうっ――っ――」`
- TW: `「嗯……呼……啊——呼……嗯……嗯——雙鐵——啾噗——啾嚕——啾噗——嗯——」`
- VN cũ: `「Ưm……phù……——Houhehu……hun……ưm——\nChụt——chu——liếmmmm——liếmmmm——」`
- Sửa: `「Ưm……phù……——Hôu-hê-hu……hừm……ưm—— Chụt——chụt——liếmmmmƯ——Ư——」`
- Lý do: JP có HAI っ cuối dòng bị bỏ mất (れるうっ và っ độc lập sau ――) — sweep BỎ SÓT; mỗi っ một Ư (tiền lệ addendum sweep: một Ư cho một っ). Đồng thời sửa ほーへふ→"Hôu-hê-hu", ふん→"hừm" (nói ngọng), ちゅむっ→"chụt".

**Key 1271 (monologue)**
- JP: `腰を思い切り進めれば、\nポーレットもそのタイミングで大きく震えてっ――っ！？`
- TW: `我用力一推，波萊特忽然渾身一抖！`
- VN cũ: `Dồn hết sức đẩy hông tới,\nđúng lúc đó Paulette cũng giật nảy mình run rẩy——!?`
- Sửa: `Dồn hết sức đẩy hông tới, đúng lúc đó Paulette cũng giật nảy mình run rẩyƯ——Ư!?`
- Lý do: JP 震えてっ――っ！？ có HAI っ — sweep chỉ sửa MỘT ("——Ư!?"); sửa lại theo JP: một Ư cho một っ (震えてっ→"run rẩyƯ", ――っ→"——Ư"; tiền lệ addendum sweep).

**Key 1290 (monologue)**
- JP: `だから子宮に甘くキスして、\n僕が僕だと伝えてあげ――っ！？`
- TW: `所以我就讓肉棒親上子宮，清清楚楚地告訴它我是誰——`
- VN cũ: `Nên tôi hôn ngọt ngào lên tử cung,\nđể nói cho nó biết tôi là ai——!?`
- Sửa: `Nên tôi hôn ngọt ngào lên tử cung, để nói cho nó biết tôi là ai——Ư!?`
- Lý do: JP 伝えてあげ――っ！？ (trailing っ) bị bỏ mất trong VN ("——!?") — sweep đã sửa, giá trị khớp (sweep-confirmed).

**Key 1377 (monologue)**
- JP: `そうして、かわいい口が開く。\n全部飲めたと、ほめてほめてといわんばかりに――っ！`
- TW: `然後她張開了可愛的小嘴示意，簡直就是在等我誇她全部喝下去了。`
- VN cũ: `Sau đó, cái miệng đáng yêu hé mở.\nNhư muốn khoe khoang rằng em đã nuốt hết rồi, hãy khen em đi——!`
- Sửa: `Sau đó, cái miệng đáng yêu hé mở. Như muốn khoe khoang rằng em đã nuốt hết rồi, hãy khen em đi——Ư!`
- Lý do: JP ――っ！ (trailing っ) bị bỏ mất trong VN ("——!") — sweep đã sửa, giá trị khớp (sweep-confirmed).

### Tiếng thở/tiếng rên để nguyên dạng La-tinh (6 dòng)

**Key 768 (ポーレット)**
- JP: `「きゅぅぅぅぅぅぅぅぅぅん！！！」`
- TW: `「呀啊啊啊！！！」`
- VN cũ: `「Kyuuuuuuuuuun!!!」`
- Sửa: `「Kíuuuuuuuuun!!!」`
- Lý do: JP きゅぅぅぅぅぅぅぅぅぅん (tiếng ré dài) bị phiên âm "Kyuuuuuuuuuun" — theo tiền lệ h2 ("fuaaaaaaaaaaan" là lỗi): Việt hoá, giữ âm đầu "Kí" + kéo dài u (10 nguyên âm như JP).

**Key 769 (ポーレット)**
- JP: `「きゃふっ！！！」`
- TW: `「呀！！！」`
- VN cũ: `「Kya!!!」`
- Sửa: `「Kyaphù!!!」`
- Lý do: JP きゃふっ bị phiên âm "Kya" — theo đề xuất h3/h4 (Việt hoá họ きゃふ/ふにゃ/んきゅ/ふひゃ, viết liền một từ): "Kyaphù".

**Key 770 (ポーレット)**
- JP: `「ひゃふっ！！？」`
- TW: `「呀！！？」`
- VN cũ: `「Hya!!?」`
- Sửa: `「Hyafu!!?」`
- Lý do: JP ひゃふっ bị phiên âm "Hya" (mất âm ふ) — theo đề xuất h3/h4: "Hyafu" (giữ ひゃ→"Hya" theo tiền lệ h1/h2, thêm "fu").

**Key 800 (双鉄)**
- JP: `「くぁ――あっ――」`
- TW: `「唔——啊——」`
- VN cũ: `「Kua——a——」`
- Sửa: `「Ư a——a——」`
- Lý do: JP くぁ bị phiên âm "Kua" — theo quyết định くぁ/くあ→"Ư a" (h6 806 và sfx doc くっ→"Hự"/"Ư").

**Key 818 (双鉄)**
- JP: `「くあっ！！！」`
- TW: `「啊！！！」`
- VN cũ: `「Kua!!!」`
- Sửa: `「Ư a!!!」`
- Lý do: JP くあっ bị phiên âm "Kua" — theo quyết định くぁ/くあ→"Ư a".

**Key 869 (ポーレット)**
- JP: `「んきゅんっ！」`
- TW: `「嗯啊！」`
- VN cũ: `「Nkyun!」`
- Sửa: `「Ưm!」`
- Lý do: JP んきゅんっ bị phiên âm "Nkyun!" — theo tiền lệ h4 (んきゅ→"Ưm") và h6 805 ("ưm").

### Lời nói ngọng (2 dòng)

**Key 784 (ポーレット)**
- JP: `「ふっ――んっ――ちゅっ――ちゅうっ――んっ――\nほーへふ、ふ――ん――わらひ――もっ――っ！！！！」`
- TW: `「呼——嗯——啾——啾——嗯——雙鐵——嗯——我也——！！！！」`
- VN cũ: `「Phù——ưm——chụt——chụt——ưm——\nAnh Sou, tetsu——ưm——em——cũng——!!!!」`
- Sửa: `「Phù——ưm——chụt——chụt——ưm—— Anh Sou, tetsu——ưm——ehm——cũng——Ư!!!!」`
- Lý do: JP わらひ (nói ngọng của "わたし") bị dịch "em" — phải giữ dạng ngọng "ehm" (theo tiền lệ h3 1154: わらし→"ehm"). Tiếng nấc cuối っ→Ư đã có trong sweep (sweep-confirmed cho phần gasp).

**Key 835 (ポーレット)**
- JP: `「んっ――ひっへふははひ――ぷっ――ほーへふ……\nふっ――んっ！　――ちゅうううううううううっ！！」`
- TW: `「嗯——呼啊呼啊——噗——哈……呼嗯！啾嚕！！」`
- VN cũ: `「Ưm——hihhefuhahahi——phụt——Houhehu……\nPhù——ưm! ——Chụtttttttttt!!」`
- Sửa: `「Ưm——Hí-hề-phù-ha-ha-hí——phụt——Hôu-hê-hu…… Phù——ưm! ——Chụtttttttttt!!」`
- Lý do: JP ひっへふははひ bị phiên âm "hihhefuhahahi" và ほーへふ bị phiên âm "Houhehu" — nói ngọng, Việt hoá từng âm tiết có gạch nối (tiền lệ h3 1154) và giữ nguyên dạng dài.

### Âm hiệu (SFX) (5 dòng)

**Key 840 (ポーレット)**
- JP: `「んっ――ちゅっ――じゅるっ――じゅううっ――\nあっ――んうっ――んっ――ちゅるっ――ちゅっ――」`
- TW: `「嗯——啾——啾嚕——啾噗——啊——嗯——嗯——啾嚕——啾噗」`
- VN cũ: `「Ưm——chụt——sụt——chụtttt——\nA——ưm——ưm——chu——chụt——」`
- Sửa: `「Ưm——chụt——sụt——chụtttt—— A——ưm——ưm——chụt——chụt——」`
- Lý do: JP ちゅるっ bị dịch "chu" — không nhất quán với chính file (842, 873: ちゅるっ→"chụt") và docs (ちゅっ→"Chụt").

**Key 847 (ポーレット)**
- JP: `「ん……ぷっ――ん――ちゅっ――ちゅるっ――\nれろっ――ぺろっ――ちゅっ――ちゅろろっ」`
- TW: `「嗯……呼——嗯——啾嚕——啾嚕——啾噗——啾嚕——啾噗——啾噗」`
- VN cũ: `「Ưm……phù——ưm——chụt——chu——\nliếm——liếm——chụt——chụtttt」`
- Sửa: `「Ưm……phù——ưm——chụt——chụt—— liếm——liếm——chụt——chụtttt」`
- Lý do: JP ちゅるっ bị dịch "chu" — không nhất quán với chính file (842, 873: ちゅるっ→"chụt") và docs.

**Key 856 (ポーレット)**
- JP: `「ん……ちゅっ……ちゅう……ちゅむっ……ふっ――\nんっ――ちゅるっ――ちゅっ――れろっ――れるっ――」`
- TW: `「嗯……啾……啾……啾嚕……呼——嗯——啾嚕——啾噗——啾嚕——啾嚕——」`
- VN cũ: `「Ưm……chụt……chu……chụt……phù——\nƯm——chu——chụt——liếm——liếm——」`
- Sửa: `「Ưm……chụt……chụt……chụt……phù—— Ưm——chụt——chụt——liếm——liếm——」`
- Lý do: JP ちゅう và ちゅるっ đều bị dịch "chu" — không nhất quán với chính file (802, 842: ちゅう→"chụt"; 842, 873: ちゅるっ→"chụt") và docs.

**Key 868 (ポーレット)**
- JP: `「んきゅっっ――うっ――い、いっ――おっぱいっ――\nもっ――こしゅんって、こす、れて――きもち、いいっ」`
- TW: `「嗯啊——啊——好——胸部——也被蹭到——好舒服——」`
- VN cũ: `「Ư a——ư——sướng, quá——ngực——\ncũng——bị cọ, xát——sướng, quá」`
- Sửa: `「Ưm——ư——sướng, quá——ngực—— cũng——bị cọ, xát——sướng, quá」`
- Lý do: JP んきゅっっ bị dịch "Ư a" — sai: んきゅ→"Ưm" (tiền lệ h4); "Ư a" là cách dịch của くあ, không phải んきゅ. (うっ→"ư" đã đúng.)

**Key 1586 (monologue)**
- JP: `（ずっ――）`
- TW: `（挺動）`
- VN cũ: `（Trượt——）`
- Sửa: `（Phập——）`
- Lý do: JP ずっ (âm đâm vào) bị dịch "Trượt——" (trượt ra) — SAI HƯỚNG: họ ず = đâm vào (quy tắc h4; TW 挺動 xác nhận). Phải là "Phập" (như 1572: ずっ→"Phập").

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
[script]
738 = "「Nói rõ ra đi, Paulette. Nếu là tôi thời học sinh, hiểu biết về mấy chuyện đó còn kém xa bây giờ đấy nhé?」"
740 = "「Muốn thế nào, là về chuyện gì cơ? Em không nói rõ thì tôi không hiểu đâu.」"
768 = "「Kíuuuuuuuuun!!!」"
769 = "「Kyaphù!!!」"
770 = "「Hyafu!!?」"
774 = "「Ư!!?」"
784 = "「Phù——ưm——chụt——chụt——ưm—— Anh Sou, tetsu——ưm——ehm——cũng——Ư!!!!」"
790 = "「Phù, a!——A! Ngực——chỗ đó—— Đầu vú——núm, vú——Ư!」"
800 = "「Ư a——a——」"
814 = "「Ư!」"
815 = "「Ư! Phù! A——ưm——chụt!」"
816 = "「A! ——Ư!?」"
817 = "「Ư!!」"
818 = "「Ư a!!!」"
819 = "「Ư!?」"
835 = "「Ưm——Hí-hề-phù-ha-ha-hí——phụt——Hôu-hê-hu…… Phù——ưm! ——Chụtttttttttt!!」"
840 = "「Ưm——chụt——sụt——chụtttt—— A——ưm——ưm——chụt——chụt——」"
847 = "「Ưm……phù——ưm——chụt——chụt—— liếm——liếm——chụt——chụtttt」"
850 = "「Ưm……phù……——Hôu-hê-hu……hừm……ưm—— Chụt——chụt——liếmmmmƯ——Ư——」"
856 = "「Ưm……chụt……chụt……chụt……phù—— Ưm——chụt——chụt——liếm——liếm——」"
866 = "「Ừ. Tôi sẽ cử động. Nhưng mà——」"
868 = "「Ưm——ư——sướng, quá——ngực—— cũng——bị cọ, xát——sướng, quá」"
869 = "「Ưm!」"
879 = "「Ừ. Tôi cũng vậy. Tôi rất yêu Paulette.」"
885 = "「Nếu Paulette học cùng lớp, có lẽ. Tôi đã nhận ra điều đó sớm hơn rồi.」"
899 = "「Tôi cũng muốn, cảm nhận hơi nóng của Paulette nhiều hơn nữa.」"
900 = "「Tôi cũng vậy——Paulette」"
903 = "「Nghĩa là, Paulette à. Tôi cũng muốn em—— Muốn Paulette cũng tự do cử động theo ý thích.」"
909 = "「Nữa đi. Tất cả. Toàn bộ con người tôi—— Tôi muốn Paulette nuốt trọn lấy.」"
924 = "「Có sao không? Tôi sẽ làm bẩn nhầy nhụa hết đấy nhé?」"
935 = "「——Quả thực tôi không thể ngờ, ngực em lại quyến rũ đến nhường này đấy.」"
946 = "「Thế này thì, chưa đủ. Nếu tôi muốn 'sử dụng' ngực của Paulette.」"
1271 = "Dồn hết sức đẩy hông tới, đúng lúc đó Paulette cũng giật nảy mình run rẩyƯ——Ư!?"
1290 = "Nên tôi hôn ngọt ngào lên tử cung, để nói cho nó biết tôi là ai——Ư!?"
1377 = "Sau đó, cái miệng đáng yêu hé mở. Như muốn khoe khoang rằng em đã nuốt hết rồi, hãy khen em đi——Ư!"
1586 = "（Phập——）"
```

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- Soutetsu gọi Paulette "em" 6 lần trong thoại (735, 740, 892, 903, 914, 935) vs "cô" 0 lần — cộng dồn toàn dự án: "em" 84 vs "cô" 43 (sau h6). ĐÍNH CHÍNH số liệu: bản tóm tắt trước đó ghi h6 là 8 lần, nhưng đếm lại chính xác bằng script (chuẩn hoá `\n` trước regex `\bem\b`, chỉ tính thoại CHAR=双鉄) là 6 lần. Các lần "em"/"em ấy" trong độc thoại (1107, 1170, 1187, 1189, 1192, 1266, 1292, 1377, 1395) là ngôi thứ ba trong lời dẫn ("cô ấy"/"em ấy"), KHÔNG tính là cách gọi. "Cô bé" là danh từ chỉ bộ phận, không phải cách xưng hô.
- "mình" trong độc thoại: 7 lần (1172, 1239, 1271, 1355, 1366, 1466, 1605) — tất cả đều đúng (1271 "giật nảy mình" và 1605 "Rùng mình" là cụm động từ; 1172/1239/1355 là sở hữu/phản thân "của chính mình"/"cơ thể mình"/"cho chính mình"; 1366 "hòa mình", 1466 "đẫm mình" là động từ phản thân).
- Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói: 0 lần (mọi lần đều có "anh" trước tên; các tên rên độc lập 952 "Anh Soutetsu" đã đúng dạng).
- 御一夜: không xuất hiện trong file (0 lần cả 4 dạng Ohimitera/Ohito/Ohitoyo/御一夜).
- 帝大 tại 1163 (JP 帝大, Đại học Đế quốc) → VN "Đại học Đế quốc" — ĐÚNG, đây là tên trường (Imperial University), KHÔNG phải 帝鉄 đang chờ quyết định.
- Không có 湯医/帝鉄/コン/宮司/マスコン/KiHa/整備体/運転ボディ/駿袋/Migita/オコジョ trong file.
- Paulette gọi Soutetsu "cậu": 0 lần. "Thẻ bảng": 0 lần.

## Đề xuất cập nhật context (chưa chốt)

- Quy tắc ちゅ-family (củng cố từ h5): ちゅっ/ちゅう/ちゅるっ/ちゅむっ/ちゅろっ đều → "chụt"; "chu" là dạng sót, không phải biến thể có chủ ý.
- Quy tắc hướng SFX (đã có từ h4, file này có thêm bằng chứng ngược): ず/ずぶ-family = đâm vào ("Phập"), ぬぶ-family = rút ra ("Rút") — 1586 là trường hợp ずっ bị dịch ngược thành "Trượt" (trượt ra).
- Quy tắc gasp nhiều っ: một Ư cho một っ, Ư dính ngay sau âm nó thuộc về (tiền lệ addendum sweep) — áp dụng cho 1271, 850 trong file này.

## Đã kiểm tra và KHÔNG tính là sai

- Các dòng ひゃ→"Hya" (762: ひゃんっ→"Hya"; 796: ひゃっ→"Hya") — giữ theo tiền lệ h1/h2 và dung thứ h4 (ひゃん→"Hya"/"Hyan").
- 836 (きゃ độc lập →"Kya"): きゃ ở đây là tiếng ré đứng một mình (sau dấu 、), không phải âm thở ghép きゃふ — giữ dạng phiên âm như ひゃ→"Hya". Khác với 769 (きゃふっ→"Kyaphù", âm ghép phải Việt hoá).
- 944 (ふぁんっ→"phù"): bỏ đuôi ん được chấp nhận theo tiền lệ h4.
- 775, 1109, 1353 (おまんこ→"âm đạo"): cách diễn theo ngữ cảnh, chính xác về giải phẫu trong ngữ cảnh siết/cọ xát — KHÔNG phải uyển ngữ "cô bé", và không sai nghĩa. (Khác với 1023 ở h5 dùng "cô bé" cho おまんこ — cả hai cách đều được chấp nhận trong file của chúng.)
- 1600 (ぐりっ→"Thọc mạnh"): TW 用力頂入 ủng hộ; JP ぐりっ mơ hồ giữa nghiền và đâm, theo TW là chấp nhận được.
- 833: sweep ghi "already-rendered", fix rỗng — audit đồng ý, không đưa vào danh sách sửa (xem trên).
- Các bản Việt trùng trong file chỉ là tiếng rên/SFX ngắn lặp lại hợp lệ (xem trên).
- 762 (ひゃんっ→"Hya——gì vậy——thế này——"): JP `ひゃんっ――なにっ――これっ――` — "Hya" giữ theo tiền lệ; phần còn lại dịch đúng.

## Kết bài

- h6 sai 36/304 (11,8%) — cao hơn h5 (9,8%) và h4 (8,7%), thấp hơn nhiều so với h3 (24,7%). File sạch về cấu trúc; lỗi tập trung ở xưng hô hệ thống (12) + thở gấp (11) + tiếng thở La-tinh (6) + SFX (5) + lời nói ngọng (2).
- Khối TOML 36 key đã parse đúng; áp dụng khối này sẽ sửa hết 36 dòng. Không có dòng chưa chắc chắn nào trong file này. Hai điểm khác sweep (1271, 784) đã ghi rõ lý do ở trên để đối chiếu khi gộp với sweep.
