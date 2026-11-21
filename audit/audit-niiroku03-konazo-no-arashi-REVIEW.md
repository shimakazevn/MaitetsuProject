# Audit: ニイロク03_粉蔵の嵐.txt.toml — 36/357 (10,1%)

- File: `08_Niiroku/ニイロク03_粉蔵の嵐.txt.toml` (route 08_Niiroku, 357 dòng script; monologue 125, ニイロク 83, 赤井 79, 先輩 23, 後東 18, 技工Ａ 13, 技工Ｂ 13, シロ 3). Nội dung: "cơn bão Kokura" — tin giải thể Teitetsu, Akai được nhờ đứng ra dẫn đầu phong trào, thu thập chữ ký (vượt 100), bốn vị Đoạn trưởng có thể "quay xe", Niiroku tỏ tình với Kiyoharu, cộng cảm/panic tràn vào, Kuha 26 là biểu tượng phục sinh của Teitetsu, Shiro đau khổ kéo phế xa về Moji; kết bằng cảnh Niiroku trốn trong tủ, hoảng loạn, "Thích Kiyoharu".
- TOML md5 `397367dc63b89391749b8876cd26ae90`, không có bản trùng (chỉ xuất hiện 1 lần trong 227 file); CSV3 1 bộ 357 dòng, key khớp tuyệt đối, 0 dòng VN trống, 0 dòng VN==TW, 0 dòng VN==JP. TOML vs CSV3: 239 khác biệt đều là kiểu làm phẳng `\n`→khoảng trắng đã biết của TOML-2, 0 khác biệt nội dung. [selections] rỗng; [characters] đủ 7 nhân vật.
- Đọc đủ 357/357 dòng đối chiếu JP + TW. Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. 2 cặp VN trùng lặp đều là dấu câu cảm thán ngắn: 「!!?」 1435/1463 (JP 「！！？」 — đúng) vs 1426 (JP 「っ！！？」 — đã sửa thành 「Ư!!?」); 「!!!」 1452 (JP 「！！！」 — đúng) vs 1812 (JP 「っ！！！」 — đã sửa thành 「Ư!!!」). Sau sửa không còn VN trùng nào khác JP.
- Sweep kiểm chứng: 5 mục cho file này trong `sweep-raw-gasp-wrong.json` (1036, 1426, 1451, 1812, 2083) — nhận cả 5; giá trị sweep khớp tuyệt đối sau khi chuẩn hóa kiểu làm phẳng `\n`→khoảng trắng của TOML (sweep lấy từ TOML; fix giữ `\n` gốc của CSV3 theo brief).
- Phân loại (36): thuật ngữ 22 (帝鉄 18: 1057, 1074, 1081, 1084, 1086, 1508, 1510, 1520, 1601, 1622, 1634, 1768, 2112, 2226, 2228, 2244, 2261, 2325; 帝労 2: 1444, 2072; 冥国 2: 1409, 1412 — 1081 mang cả 帝鉄 lẫn 冥国), xưng hô 7 (1846, 1985, 2019, 2138, 2328, 2331, 2333), gasp 5 (1036, 1426, 1451, 1812, 2083 — cả 5 từ sweep), SFX 1 (1429), thẻ %l 1 (1568).

## §1. Thuật ngữ (22)

### 帝鉄 → "Teitetsu" (18 dòng; quyết định Hieu 19/11 — "Đường sắt Hoàng gia" dịch sai khái niệm: 帝鉄 = 帝国鉄道 = Đường sắt Đế quốc, không phải 皇室/Hoàng gia)
- 1057 (技工Ａ): JP 「『帝鉄解体。全路線を廃線・道路化』！」→ VN cũ "'Giải thể Đường sắt Hoàng gia. Bãi bỏ toàn bộ tuyến đường - Chuyển đổi thành đường bộ'!" → Sửa "'Giải thể Teitetsu. Bãi bỏ toàn bộ tuyến đường - Chuyển đổi thành đường bộ'!"
- 1074 (赤井): JP 民営・分社化は帝鉄にも有利 → "có lợi cho cả Đường sắt Hoàng gia" → "có lợi cho cả Teitetsu."
- 1081 (赤井): JP しかし帝鉄はそう出来なかった / 冥国 → "Đường sắt Hoàng gia đã không thể" + "Meikoku" → "Teitetsu đã không thể" + "Minh Quốc" (xem thêm §1b).
- 1084 (赤井): JP 帝鉄が主導となれば → "Nếu Đường sắt Hoàng gia đứng ra chủ đạo" → "Nếu Teitetsu đứng ra chủ đạo".
- 1086 (赤井): JP 帝鉄の昨年の単年度赤字額は8300億円強 → "Mức thâm hụt trong một năm vừa qua của Đường sắt Hoàng gia" → "của Teitetsu". (Số liệu giữ nguyên: 830 tỷ yên, 37 nghìn tỷ yên — đúng.)
- 1508 (先輩): JP 帝鉄ば一度潰して → "giải thể Đường sắt Hoàng gia một lần" → "giải thể Teitetsu một lần".
- 1510 (後東): JP 帝鉄解体が避けられない → "việc giải thể Đường sắt Hoàng gia là không thể tránh khỏi" → "việc giải thể Teitetsu là không thể tránh khỏi".
- 1520 (赤井): JP 帝鉄――いえ、鉄道復活の種火 → "Đường sắt Hoàng gia――không, mồi lửa" → "Teitetsu――không, mồi lửa".
- 1601 (赤井): JP 帝鉄は発展的に、民営化し分社化すべき → "Đường sắt Hoàng gia nên phát triển" → "Teitetsu nên phát triển".
- 1622 (赤井): JP ニイロクは帝鉄再生の象徴 → "biểu tượng cho sự tái sinh của Đường sắt Hoàng gia" → "của Teitetsu".
- 1634 (技工Ａ): JP 帝鉄解体を撤回させて → "rút lại quyết định giải thể Đường sắt Hoàng gia" → "giải thể Teitetsu".
- 1768 (技工Ｂ): JP 帝鉄の希望 → "niềm hy vọng của Đường sắt Hoàng gia" → "của Teitetsu".
- 2112 (monologue): JP 帝鉄貨物を分離して → "Vận tải hàng hóa Đường sắt Hoàng gia bị tách riêng" → "Vận tải hàng hóa Teitetsu bị tách riêng".
- 2226 (monologue): JP 帝鉄の解体決定 → "quyết định giải thể Đường sắt Hoàng gia" → "giải thể Teitetsu".
- 2228 (monologue): JP 帝鉄復活の希望の象徴 → "biểu tượng hy vọng cho sự phục sinh của Đường sắt Hoàng gia" → "của Teitetsu".
- 2244 (monologue): JP 帝鉄解体のニュース → "tin tức giải thể Đường sắt Hoàng gia" → "giải thể Teitetsu".
- 2261 (monologue): JP 帝鉄解体？ → "Giải thể Đường sắt Hoàng gia?" → "Giải thể Teitetsu?"
- 2325 (monologue): JP 帝鉄がなくなっちゃうかもしれない → "Đường sắt Hoàng gia có thể sẽ biến mất" → "Teitetsu có thể sẽ biến mất".
- Sau sửa, file không còn dòng "Đường sắt Hoàng gia" nào. (Tiền lệ sửa trong audit: ハチロク07 "Hoàng gia→Teitetsu 4", ハチロク10 "帝鉄→Teitetsu 10".)

### 帝労 → "Công đoàn Teitetsu" (2 dòng)
- 1444 (先輩): JP ワシは[ていろう,1]帝労の幹部 → VN cũ "tôi là cán bộ của Công đoàn Đường sắt Hoàng gia" → Sửa "tôi là cán bộ của Công đoàn Teitetsu." (帝労 = 帝国鉄道労働組合 — công đoàn của Teitetsu; áp dụng cùng quyết định 19/11.)
- 2072 (monologue): JP 帝労。帝鉄最大の労働組合 → VN cũ "Công đoàn Đường sắt Hoàng gia. Tổ chức công đoàn lớn nhất của Đường sắt Hoàng gia." → Sửa "Công đoàn Teitetsu. Tổ chức công đoàn lớn nhất của Teitetsu."

### 冥国 → "Minh Quốc" (3 dòng — 1081 đã tính ở trên, thêm 1409, 1412)
- 1409 (赤井): JP 冥国の命令での、施策 → VN cũ "theo mệnh lệnh của Meikoku" → Sửa "theo mệnh lệnh của Minh Quốc." (JP không có furigana メリケン — quy tắc đã chốt: 冥国 = "Minh Quốc", chỉ giữ "Meriken" khi メリケン được nói ra; TW 美國 là cách đọc của TW, JP thắng.)
- 1412 (赤井): JP 冥国絡みの国策 → VN cũ "quốc sách có liên quan đến Meikoku" → Sửa "có liên quan đến Minh Quốc". (Tiền lệ: 冥国 "Meikoku"→"Minh Quốc" ở 2 file đã merge.)

## §2. Xưng hô (7)

### 1846 — 技工Ｂ — "Akai, cậu" → "Anh Akai, anh"
- JP: 「電車区長ば逃げまわっとるみたいで――赤井さん、あんた、なんか知りませんかね」
- TW: 「電車段長不知跑哪去了——赤井，你知道些什麼嗎」
- VN cũ: 「Đoạn trưởng xe điện có vẻ đang lẩn trốn――\nAkai, cậu, có biết gì không?」
- Sửa: 「Đoạn trưởng xe điện có vẻ đang lẩn trốn――\nAnh Akai, anh có biết gì không?」
- Lý do: JP có 赤井さん; dạng đã thiết lập của 技工Ｂ với Akai trong file này là "anh Akai" ×3 (1566, 1768, 1817) — 1846 là dòng duy nhất dùng "cậu". (Tiền lệ toàn dự án: "Anh Akai" là cách dịch đã thiết lập của 赤井さん.)

### 1985 — monologue — "ông ấy" → "anh ấy" (người được nhắc là Kiyoharu)
- JP: あんなに親切にしてくれたのにって――\n少し不安で、怖くなる。
- TW: 但他以前明明對我那麼親切——這讓我感到有些不安和恐懼。
- VN cũ: Rõ ràng ông ấy đã đối xử tốt với mình như vậy mà――\nCảm thấy có chút bất an, và sợ hãi.
- Sửa: Rõ ràng anh ấy đã đối xử tốt với mình như vậy mà――\nCảm thấy có chút bất an, và sợ hãi.
- Lý do: mạch 1980–1984 là Kiyoharu xoa đầu Niiroku ("Anh ấy xoa đầu mình" ở 1982), tiếp nối 2130/2188–2190/2193 (Kiyoharu ôm cô ấy; TW 2193 xác nhận 清春用力地抱住了我). "Ông ấy" ở 1985 là cùng một người — Kiyoharu, trong khi "ông ấy" ở 1048/2244 đều chỉ Đoạn trưởng (đúng, giữ nguyên).

### Độc thoại Niiroku "tôi" → "mình" (5 dòng — chuẩn nội bộ file)
- Độc thoại của Niiroku trong file dùng "mình" 38 dòng vs "Tôi"/"tôi" 5 dòng — sửa 5 dòng lệch theo đa số nội bộ (tiền lệ Nagi 08a: 13 dòng Fukami "tôi"→"mình" theo 43/49).
- 2019: JP 今のが――きっと、パニックっていうやつ。\nシロおねえちゃんが焦ってた意味を、わからされた。→ "Tôi đã hiểu được lý do tại sao chị Shiro lại vội vàng đến thế." → "Mình đã hiểu được lý do tại sao chị Shiro lại vội vàng đến thế."
- 2138: JP 清春にして欲しいこと、たくさんあるし、\nそれが欲か、愛情かなんて、よくわからない。→ "Có rất nhiều điều tôi muốn Kiyoharu làm cho mình,\nđó là dục vọng hay tình yêu, tôi cũng không rõ nữa." → "Có rất nhiều điều mình muốn Kiyoharu làm cho mình,\nđó là dục vọng hay tình yêu, mình cũng không rõ nữa."
- 2328: JP （解体なんてされたくない！　いやだ！　逃げたい）→ "（Tôi không muốn bị tháo dỡ đâu! Không muốn! Tôi muốn trốn chạy）" → "（Mình không muốn bị tháo dỡ đâu! Không muốn! Mình muốn trốn chạy）"
- 2331: JP （助けて。助けて。助けて――助けてっ！！！）→ "（Cứu tôi với. Cứu tôi với. Cứu tôi với――Cứu tôi với!!!）" → "（Cứu mình với. Cứu mình với. Cứu mình với――Cứu mình với!!!）" (っ cuối gắn với động từ 助けて — từ nội dung, không phải gasp, nên không thêm Ư theo quy tắc.)
- 2333: JP （どうしてこんな――一生懸命頑張ってるのに）→ "（Tại sao lại thành ra thế này――tôi đã cố gắng hết sức rồi mà）" → "（Tại sao lại thành ra thế này――mình đã cố gắng hết sức rồi mà）"

## §3. Gasp っ (5 — cả 5 từ sweep, nhận nguyên văn)

### 1036 — monologue — gasp cuối dòng sau ――
- JP: ……つながらない。\nチャンネル、もっと広げ――っ！！！？
- TW: ……連不上她。擴大一下頻道的接收範圍……啊！！！？
- VN cũ: ......Không kết nối được.\nMở rộng kênh tần số hơn nữa――!!!?
- Sửa: ......Không kết nối được.\nMở rộng kênh tần số hơn nữa――Ư!!!?

### 1426 — 赤井 — gasp cả dòng
- JP: 「っ！！？」 / TW: 「呃！！？」 / VN cũ: 「!!?」 / Sửa: 「Ư!!?」

### 1451 — 赤井 — gasp cả dòng
- JP: 「っ！」 / TW: 「唔！」 / VN cũ: 「!」 / Sửa: 「Ư!」

### 1812 — 後東 — gasp cả dòng
- JP: 「っ！！！」 / TW: 「這！！！」 / VN cũ: 「!!!」 / Sửa: 「Ư!!!」

### 2083 — monologue — gasp cuối dòng sau ――
- JP: 渦まいて、凄く、たくさん――一斉に――\n怒ってる、泣いて、戸惑って――っ！！？
- TW: 從共鳴裡傳來了好多聲音，充滿了憤怒、悲傷和困惑，一起湧入我的腦海。
- VN cũ: Cuộn xoáy, rất nhiều, vô số――cùng một lúc――\nTức giận, khóc lóc, hoang mang――!!?
- Sửa: Cuộn xoáy, rất nhiều, vô số――cùng một lúc――\nTức giận, khóc lóc, hoang mang――Ư!!?

## §4. SFX (1)

### 1429 — ニイロク — ふきゅっ "Fu kyu" → "Fukyu"
- JP: 「ふきゅっ！！？」 / TW: 「呼啊！！？」
- VN cũ: 「Fu kyu!!?」 / Sửa: 「Fukyu!!?」
- Lý do: dạng romaji đã thiết lập toàn dự án cho ふきゅっ là "Fukyu" một từ (lr_日々姫h1 1069, lr_日々姫真闇h1 1468/1469, ふかみh3 2449, 日々姫h6 2266); "Fu kyu" tách khoảng trắng làm vỡ một mora きゅ thành hai âm tiết. Một dòng = một cách diễn (romaji).

## §5. Thẻ %l (1)

### 1568 — ニイロク — gỡ thẻ gloss VN tự thêm cho ビュッフェ
- JP: 「ゆったりとしたシート。ビュッフェ。カーテン。\n軽食を取りながら、仕事をしながらの移動を提供」 (JP không có thẻ, không có ruby cho ビュッフェ)
- TW: 「我們有可以坐下來慢慢享受風景、處理工作的座位和\x%lビュッフェ;#00ffc040;飲食櫃臺%l;#;。能讓客人在旅程中簡單用餐並進行工作」
- VN cũ: 「Ghế ngồi rộng rãi thoải mái. \x%lビュッフェ;#00ffc040;Quầy ăn nhẹ%l;#;. Rèm che.\nCung cấp một chuyến đi vừa có thể thưởng thức bữa ăn nhẹ, vừa có thể làm việc.」
- Sửa: 「Ghế ngồi rộng rãi thoải mái. Quầy ăn nhẹ. Rèm che.\nCung cấp một chuyến đi vừa có thể thưởng thức bữa ăn nhẹ, vừa có thể làm việc.」
- Lý do: Gemini tự thêm thẻ gloss mà JP không có (mẫu bịa đã ghi trong skill); gloss "Quầy ăn nhẹ" đúng nghĩa (TW 飲食櫃臺) nên giữ làm text thường, chỉ gỡ thẻ. Sau sửa: thẻ %l trong VN 18 = JP 18 (9 thẻ).

## §6. Đã kiểm chứng đúng — giữ nguyên

- Niiroku gọi Soutetsu "anh" (1368 "Anh cũng biết ngại sao?", 1574 "rất thích anh", 1582 "tôi luôn quan sát anh mà") — đúng; tiền lệ ハチロク07: Soutetsu "anh" với Niiroku (2829), quan hệ đối ứng. 1046 "Ý anh là" (Niiroku hỏi Akai) đúng.
- 1425 ひっ！！？ → "Hí!!?" — giữ. Tiền lệ cùng route: ニイロク04 1710 giữ "Hí!?" (file đã merge); "Hí" cũng xuất hiện ở ハチロクh3 1014, ハチロクh6 850, ハチロクh7 765. (Các file khác dùng "Hi" — SFX ngẫu hứng theo ngữ cảnh, không thống nhất ép.)
- 1456 「あ――ああ！」→ "A――aa!" — giữ; mẫu "A――aa!" lặp lại toàn dự án (39 dòng), chỉ là cách viết thường chữ "aa", không sai nghĩa.
- 1469 あっ！→ "A!", 1448 わっ！？→ "Oa!?" — giữ; っ đã diễn bằng dấu "!" (sweep không liệt kê; theo quy tắc chỉ thêm Ư khi âm っ hoàn toàn mất).
- 1334 やっ！！！→ "Không!!!" — giữ; tiếng kêu từ chối, TW 不要 đồng thuận.
- 1657 「きよは」→ "Kiyoha" — giữ; tên gọi cụt, không bịa phần hoàn thiện.
- 1980 なでなで、乱暴にくしゃくしゃって。→ "Xoa xoa, rồi vò đầu mình một cách thô bạo." — giữ; TW dịch sai thành ho khan (強行咳嗽), VN theo đúng JP.
- 1746 「時間、大丈夫なら、このまま聞きたい。」→ "Nếu có thời gian, tôi muốn nghe trong tư thế này." — giữ; VN theo JP "このまま", TW tự thêm 抱著我.
- 1491 「はい、今」→ "Vâng, tôi ra ngay." — giữ; TW "我這就來開門" ủng hộ.
- 2092 清春に産みだしてもらった → "do Kiyoharu sinh ra" — giữ; "sinh ra" phản ánh 産みだす (đưa vào đời), không sai.
- 1404/1570 帝央 → "Teiou" — giữ (dạng đã có trong dự án); 1811/2041/2080 廃車回送 → "hồi tống phế xa" nhất quán ×3; 1048/2244 区長/電車区長 → "Đoạn trưởng"/"Đoạn trưởng xe điện" nhất quán.
- 1734 共感 → "cộng cảm" — đúng (năng lực Railord, không phải "đồng cảm" giữa người với người).
- 2040 どどど, 2058 ギュンギュン, 2106 ぽわっ — giữ cách diễn hiện tại (đã truyền được nghĩa; SFX ngẫu hứng).
- 1086 số liệu 830 tỷ yên / 37 nghìn tỷ yên — đúng (8300億, 37兆).
- 2322 （すっ――）→ "（Soạt――）", 2323 （バタバタバタ）→ "（Lạch cạch lạch cạch lạch cạch）" — giữ.

## §7. Chưa chắc chắn / cờ cho Hieu

1. **1802 (後東) — người nghe mơ hồ, KHÔNG sửa.** JP 「いや、そんなこと俺らに聞かれても――」 không nêu rõ người hỏi. VN cũ "Không, anh hỏi chúng tôi chuyện đó thì――" dùng "anh". Nhưng 後東 gọi Akai là "cậu" ở 1788 ("Akai, cậu......"), và người hỏi cũng có thể là 先輩. Không đủ căn cứ để đổi "anh"→"cậu" nên giữ nguyên VN, chờ Hieu quyết (hoặc để nguyên).
2. **2331 "Cứu mình với"** — sửa theo chuẩn độc thoại "mình" của file; nhưng "Cứu tôi với!" là câu kêu cứu quen thuộc hơn trong tiếng Việt. Nếu Hieu muốn giữ câu kêu cứu tự nhiên thì bỏ fix này.
3. **1429 "Fukyu"** — dạng romaji theo đa số dự án; nếu Hieu muốn dạng Việt ("Phù kiu") thì đổi lại.
4. B19 vẫn park (không liên quan file này — file không có thẻ %l thiếu `;`).

## §8. Khối TOML (đã parse-kiểm chứng: 36 khóa, 0 sai lệch giá trị so với JSON)

```toml
[script]
1036 = "......Không kết nối được.\\nMở rộng kênh tần số hơn nữa――Ư!!!?"
1057 = "「'Giải thể Teitetsu. Bãi bỏ toàn bộ tuyến đường - Chuyển đổi thành đường bộ'!\\n'Hướng tới sự ra đời của công ty Xe buýt Aircra'」"
1074 = "「......Thông thường thì,\\ntư nhân hóa và chia tách công ty là một đề xuất có lợi cho cả Teitetsu.」"
1081 = "「......Nhưng Teitetsu đã không thể làm như vậy.\\nCó lẽ, chính phủ hoặc là Minh Quốc, đã không cho phép họ làm điều đó.」"
1084 = "「......Nếu Teitetsu đứng ra chủ đạo, thì chuyện này rất dễ dàng.\\nVì sự tồn tại của đường sắt, tôi cứ nghĩ đương nhiên họ sẽ làm như vậy.」"
1086 = "「......Mức thâm hụt trong một năm vừa qua của Teitetsu là hơn 830 tỷ yên.\\nKhoản nợ lũy kế thực tế đã lên tới 37 nghìn tỷ yên.」"
1409 = "「Nhưng, chuyện lần này lại khác. Công ty Aircra――\\nKhông, đúng hơn là, chính sách này được đưa ra theo mệnh lệnh của Minh Quốc.」"
1412 = "「Nhưng, nếu bị đánh giá là không có dư địa đàm phán thì sẽ bị đè bẹp.\\nVới quốc sách có liên quan đến Minh Quốc, những kẻ ở tầm cỡ như chúng ta không thể chống cự được đâu.」"
1426 = "「Ư!!?」"
1429 = "「Fukyu!!?」"
1444 = "「Nếu làm được thì tôi đã làm rồi. Nhưng, tôi là cán bộ của Công đoàn Teitetsu.\\nVới phía ban quản lý thì như nước với lửa vậy.」"
1451 = "「Ư!」"
1508 = "「Tức là giải thể Teitetsu một lần, rồi chia nhỏ nó ra.\\nSau khi làm vậy, sẽ thành lập các công ty mới.」"
1510 = "「Đúng vậy! Nếu việc giải thể Teitetsu là không thể tránh khỏi\\nthì chỉ còn cách làm thôi!!」"
1520 = "「Dù trong trường hợp xấu nhất, chỉ cần cô còn ở lại,\\nTeitetsu――không, mồi lửa cho sự phục sinh của đường sắt, sẽ tiếp tục tồn tại.」"
1568 = "「Ghế ngồi rộng rãi thoải mái. Quầy ăn nhẹ. Rèm che.\\nCung cấp một chuyến đi vừa có thể thưởng thức bữa ăn nhẹ, vừa có thể làm việc.」"
1601 = "「Vì vậy, chúng tôi đã bàn bạc với nhau.\\nTeitetsu nên phát triển theo hướng tư nhân hóa và chia tách thành các công ty con.」"
1622 = "「Đúng vậy, Niiroku là biểu tượng cho sự tái sinh của Teitetsu――\\nTrong tình huống này, cô rất có thể sẽ trở thành mục tiêu công kích đầu tiên.」"
1634 = "「Tốt nhất thì, tất nhiên là bắt họ rút lại quyết định giải thể Teitetsu rồi.」"
1768 = "「Nếu là anh Akai thì chắc chắn làm được! Anh là niềm hy vọng của Teitetsu,\\nlà lái tàu thử nghiệm được giao phó dòng \\x%lクハ26;#00ffc040;Kuha 26%l;#; mà!!」"
1812 = "「Ư!!!」"
1846 = "「Đoạn trưởng xe điện có vẻ đang lẩn trốn――\\nAnh Akai, anh có biết gì không?」"
1985 = "Rõ ràng anh ấy đã đối xử tốt với mình như vậy mà――\\nCảm thấy có chút bất an, và sợ hãi."
2019 = "Cảm giác vừa rồi――chắc chắn là thứ gọi là hoảng loạn.\\nMình đã hiểu được lý do tại sao chị Shiro lại vội vàng đến thế."
2072 = "Công đoàn Teitetsu. Tổ chức công đoàn lớn nhất của Teitetsu. Luôn đối lập với phía ban quản lý,\\nchị Shiro đã dạy mình như vậy."
2083 = "Cuộn xoáy, rất nhiều, vô số――cùng một lúc――\\nTức giận, khóc lóc, hoang mang――Ư!!?"
2112 = "Mình biết. Vì chị Shiro từng than vãn rồi.\\nThị phần hàng hóa bị xe tải cướp mất, Vận tải hàng hóa Teitetsu bị tách riêng."
2138 = "Có rất nhiều điều mình muốn Kiyoharu làm cho mình,\\nđó là dục vọng hay tình yêu, mình cũng không rõ nữa."
2226 = "'Quyết định'――nếu quyết định giải thể Teitetsu là thật.\\nThì người có thể làm được chuyện đó――"
2228 = "Và bởi vì mình, là Railord điều khiển tổng hợp \\x%lクハ26;#00ffc040;Kuha 26%l;#;.\\nChính là biểu tượng hy vọng cho sự phục sinh của Teitetsu."
2244 = "Đoạn trưởng xe điện. Kể từ khi có tin tức giải thể Teitetsu,\\nông ấy thực sự không gặp bất cứ ai, kể cả Kiyoharu."
2261 = "Giải thể Teitetsu?\\nBãi bỏ toàn bộ tuyến đường?"
2325 = "（Ừm. Tuyệt đối không phải lúc để đối đầu nhau.\\nBởi vì đây là thời khắc sinh tử, Teitetsu có thể sẽ biến mất）"
2328 = "（Mình không muốn bị tháo dỡ đâu! Không muốn! Mình muốn trốn chạy）"
2331 = "（Cứu mình với. Cứu mình với. Cứu mình với――Cứu mình với!!!）"
2333 = "（Tại sao lại thành ra thế này――mình đã cố gắng hết sức rồi mà）"
```

## §9. Lượt soát 2

- Tổng số fix: 36 / soát lại: 36 / bỏ: 0 / sửa: 0. Mỗi fix đã đọc lại toàn bộ giá trị đối chiếu JP (kèm TW) ở lượt 2: 1036/1426/1451/1812/2083 (khớp sweep nguyên văn, TW 啊/呃/唔/這 đồng thuận); 18 帝鉄 + 2 帝労 (quyết định Hieu 19/11, docs translation_guidelines.md:73); 1409/1412/1081 冥国 (ruby めいこく ở 1081, không phải メリケン); 1846 (赤井さん trong JP + "anh Akai" ×3); 1985 (mạch xoa đầu 1980–1984 + TW 2193); 2019/2138/2328/2331/2333 (chuẩn "mình" 38/43 dòng độc thoại); 1568 (JP không thẻ — TW 飲食櫃臺 ủng hộ gloss); 1429 (dạng "Fukyu" đa số dự án 4+ lần).

## Kết bài

File ニイロク03_粉蔵の嵐 đã audit xong toàn bộ 357 dòng: 36 dòng sai (10,1%) — thuật ngữ 22, xưng hô 7, gasp 5, SFX 1, thẻ %l 1. Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 36 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 36/36, 0 bỏ, 0 sửa. Cờ cho Hieu: 1802 người nghe mơ hồ (giữ "anh"); 2331 "Cứu mình với" vs "Cứu tôi với"; 1429 dạng "Fukyu".
