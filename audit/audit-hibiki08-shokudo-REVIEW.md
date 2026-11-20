# Audit — 日々姫08_とれいん食堂 (02_Hibiki) — 20/598 (3,3%)

File: `日々姫08_とれいん食堂.txt.toml` — route 02_Hibiki, 598 dòng script.
Disk: `sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59eb08_#U3068#U308c#U3044#U3093#U98df#U5802.txt.toml` (tên file #U-escaped, đúng như trên đĩa).
Nội dung: chuyến chạy đầu tiên của "とれいん食堂" (tàu nhà hàng) — thiết kế của Hibiki, Nagi + Fukami làm đội A ở bếp trên tàu, Saito và Mayami đi với tư cách hành khách, xoay xở lịch trình (trễ 15 phút, chạy bù 5 phút), bán vé, tham quan gara đầu máy hình ngành + bàn quay đầu máy ở Bungomori, và màn "tiết lộ bí mật tàu nhà hàng" cuối chuyến.
Nhân vật: monologue 250, 双鉄 87, 日々姫 81, ふかみ 54, 真闇 36, 凪 35, 斎藤 26, 栃木 16, 木本 5, 観光客 5, 山崎 2, 特産品売り 1.

Phương pháp: đọc toàn bộ 598 dòng theo từng hàng, đối chiếu JP + TW (CSV3), kiểm tra cơ học thêm (xem §3). Key order trong TOML == key order tăng dần; CSV3 order xáo trộn; cả hai đều KHÔNG phải story order — người nghe/đại từ xác định theo nội dung và dòng kề trong luồng truyện, không theo key.

## §1. Kết quả

Sai: **20/598 (3,3%)**.

Phân loại (20):
- **lost-gasp**: 7 (2181 trailing, 2196/2201/2213 whole, 2783 trailing-mid, 2785 trailing — 6 mục sweep, áp dụng cả 6; 2152 trailing-mid — sweep bỏ sót, audit tự tìm, xem §2.1).
- **SFX-laughter**: 2 (2142, 2143 — tiếng cười うふふ bị nhét Ư gasp).
- **terminology**: 3 (2342 — 帝鉄 → "Đường sắt Hoàng gia"; 2585 + 3038 — 冥国 → "Mỹ").
- **mistranslation**: 2 (2545 — số ít/số nhiều; 2718 — キュウロク đọc thành gara đầu máy).
- **pronoun**: 2 (2128 — Soutetsu gọi Fukami "cậu"; 3567 — "anh Tochigi/Kimoto" thay vì "bác").
- **added-tag**: 4 (2117, 2458, 3113, 3211 — VN thêm thẻ %l gloss mà JP không có; tiền lệ ムナカタ来訪 đã gỡ 31 thẻ tương tự).

Theo nhân vật: 日々姫 9/81 (11,1%), monologue 4/250 (1,6%), 双鉄 3/87 (3,4%), 真闇 2/36 (5,6%), 木本 1/16, 斎藤 1/26. Đối thoại 16/348 (4,6%), độc thoại 4/250 (1,6%).

Không misaligned / không rotation / không contamination chéo file / không orphan / 0 untranslated / 0 duplicate key. Không lỗi đại từ hệ thống: Soutetsu "anh" với Hibiki/Fukami/Nagi xuyên suốt và đúng (xem §3); độc thoại kể chuyện đồng nhất "tôi" (0 dòng monologue dùng "Anh").

Sweep っ-gasp: 6 mục cho file này trong `sweep-raw-gasp-wrong.json` — đã kiểm chứng từng mục với JP và áp dụng cả 6, 0 mục bị loại (xem §2.1). Audit quét thêm toàn bộ dòng JP có っ và tìm thêm 1 gasp sweep bỏ sót (2152).

Strong candidates 6 → đọc toàn bộ tìm ra 20 sai: heuristic chỉ đếm được một phần (nó không thấy lỗi SFX/nghĩa/đại từ/tag thêm).

## §2. Các lỗi và cách sửa

### §2.1. Gasp っ — 7 hàng (6 sweep + 1 tự tìm)

| Hàng | Nhân vật | JP | VN cũ | Fix |
|---|---|---|---|---|
| 2181 | 日々姫 | 「ううう～～っ」 | 「Uuu~~」 | 「Uuu~~Ư」 |
| 2196 | 日々姫 | 「っ！」 | 「!」 | 「Ư!」 |
| 2201 | 日々姫 | 「っ！！！」 | 「!!!」 | 「Ư!!!」 |
| 2213 | 日々姫 | 「っ！！？」 | 「!!?」 | 「Ư!!?」 |
| 2783 | 日々姫 | 「～～っ！　ご乗車、ありがとう、ございました！」 | 「~~! \nXin cảm ơn quý khách đã sử dụng dịch vụ ạ!」 | 「~~Ư! Xin cảm ơn quý khách đã sử dụng dịch vụ ạ!」 |
| 2785 | 日々姫 | 「～～～～～～～っ」 | 「~~~~~~~」 | 「~~~~~~~Ư」 |
| 2152 | 日々姫 | 「すう～――はぁ～っ――」 | 「Hít~——Hà~——」 | 「Hít~——Hà~Ư——」 |

Ghi chú 2152 (không có trong sweep): はぁ～っ là tiếng thở bị ngắt bởi っ giữa dòng (cùng lớp trailing-mid với sweep 2783: ～っ + nội dung tiếp theo) — VN "Hà~——" giữ dấu mà mất âm ngắt, thêm Ư sau dấu ~. Đây là phán đoán của audit (sweep không liệt kê); xem §6.

Ghi chú các っ còn lại (giữ nguyên, xem §3): あっ―― (2185) / あ――あっ (2186) → "A——" (tiếng cảm thán bị ngắt, đã diễn bằng "A" + gạch ngang); うんっ (1568, 2229) → "Vâng" / "Vâng!"; はいっ (2176, 2457) → "vâng ạ!"; てっ cuối (2193) là っ nhấn mạnh gắn với từ (quy tắc: không thêm Ư); ああっ (2195) → "A á!!" (đã diễn っ thành nhịp "á" thứ hai).

### §2.2. SFX-laughter — 2 hàng

- **2142** — 真闇: JP 「うふふっ、実はやってみたかったとよ。ひーちゃんが、そーちゃんが、いっつもしとること」; TW 「呵呵，其實咱一直很想嘗試一下小日小雙他們平時做的這些工作」; VN cũ: 「Ư fufu, thực ra chị đã luôn muốn thử làm rồi. Những việc mà Hi-chan và Sou-chan vẫn hay làm ấy.」; Sửa: 「Ufufu, thực ra chị đã luôn muốn thử làm rồi. Những việc mà Hi-chan và Sou-chan vẫn hay làm ấy.」 — うふふ là tiếng CƯỜI, không phải gasp; "Ư fufu" nhét gasp vào tiếng cười. Cùng JP うふふっ ở 2140 đã dịch đúng "Ufufu" ("Ufufu. Chị biết rõ lắm") — 2142/2143 lệch chuẩn.
- **2143** — 真闇: JP 「うふふ、楽しみ。きっぷ、お食事つきのコースでお願いします」; TW 「呵呵，真是期待。那我要訂附帶餐點的套票」; VN cũ: 「Ư fufu, mong chờ quá đi. Cho tôi vé có kèm theo bữa ăn nhé.」; Sửa: 「Ufufu, mong chờ quá đi. Cho tôi vé có kèm theo bữa ăn nhé.」 — JP うふふ không có cả っ, càng không có gasp.

### §2.3. Thuật ngữ — 3 hàng

- **2342** — 木本: JP 「[ていてつ,1]帝鉄マニアば、栃木んとこにはよー行きよるとですよ。こん男は、食堂車の話ばするのが好きですけんのう」; TW 「帝國鐵路迷們經常會去櫪木那裡坐坐。因為這傢伙很喜歡講餐車的事情」; VN cũ: 「Mấy tay cuồng Đường sắt Hoàng gia hay lui tới chỗ Tochigi lắm. Tên này thích nói chuyện về toa ăn mà lại」; Sửa: 「Mấy tay cuồng Teitetsu hay lui tới chỗ Tochigi lắm. Tên này thích nói chuyện về toa ăn mà lại」 — 帝鉄 = "Teitetsu" theo thuật ngữ đã chốt (không phải "Đường sắt Hoàng gia" — Hoàng gia là hoàng thất, sai nghĩa; cũng không phải "Đường sắt Đế quốc" dạng dài).
- **2585** — 双鉄: JP 「[めいこく,1]冥国式は、汎用性を持つ反面、日ノ本・[えい]詠式より車両理解の深さでは及ばないとも聞いている」; TW 「美國式的鐵路人偶雖然以通用性見長，但聽說對車輛的理解不如日本式、英國式那麼深」; VN cũ: 「Hàng của Mỹ tuy có tính đa dụng cao, nhưng nghe nói về độ hiểu biết toa xe thì không bằng hàng của Hinamoto hay Anh」; Sửa: 「Kiểu Minh Quốc tuy có tính đa dụng cao, nhưng nghe nói về độ hiểu biết toa xe thì không bằng hàng của Hinamoto hay Anh」 — 冥国 = "Minh Quốc" theo thuật ngữ đã chốt (chữ Hán đọc めいこく, không phải メリケン nói trong thoại — nên không dùng "Meriken"); "Hàng của Mỹ" là dịch theo TW, trái thuật ngữ đã chốt. "Hàng" → "Kiểu" cho khớp 式 (kiểu/loại). 日ノ本 giữ "Hinamoto" (phiên âm, chưa có thuật ngữ chốt — xem §6).
- **3038** — monologue: JP 「とれいん食堂レイルロオドは、改装前からの引き継ぎとなる冥国製――」; TW 「列車食堂沿用了原本的美國式鐵路人偶」; VN cũ: 「Railord của Toa ăn Train, được kế thừa từ trước khi cải tạo, là hàng do Mỹ sản xuất——」; Sửa: 「Railord của Toa ăn Train, được kế thừa từ trước khi cải tạo, là hàng do Minh Quốc sản xuất——」 — cùng lỗi 冥国 → "Mỹ" như 2585. "Toa ăn Train" giữ nguyên (chưa thống nhất tên gọi — xem §6).

### §2.4. Dịch sai nghĩa — 2 hàng

- **2545** — 日々姫: JP 「浮かれてもらうのも嬉しかけどね。苦労ば、たーくさんしたこだし」; TW 「看你們開開心心的我也很高興。畢竟她倆也吃了不少苦」; VN cũ: 「Mọi người vui vẻ thì em cũng mừng. Vì đứa bé này đã trải qua rất nhiều vất vả mà」; Sửa: 「Mọi người vui vẻ thì em cũng mừng. Vì hai đứa đã trải qua rất nhiều vất vả mà」 — こ ở đây chỉ Nagi và Fukami (hai đứa đã vất vả chuẩn bị); TW xác nhận 她倆 (cả hai). VN "đứa bé này" (số ít, một đứa) sai số lượng, lại mâu thuẫn với "Mọi người" ở ngay câu trước.
- **2718** — 斎藤: JP 「キュウロクやらいう機関庫は、ハチロクとくらべて、随分と大きゅうみえましたねぇ」; TW 「那個叫九六的機車，看起來比八六大了不少」; VN cũ: 「Cái gara đầu máy tên là Kyuroku gì đó, so với Hachiroku, trông có vẻ to hơn hẳn nhỉ.」; Sửa: 「Cái đầu máy tên là Kyuroku gì đó, so với Hachiroku, trông có vẻ to hơn hẳn nhỉ.」 — キュウロク (9600) và ハチロク (8620) đều là đầu máy hơi nước; so sánh "gara đầu máy" với một đầu máy là vô nghĩa. JP 機関庫 ở đây là cách dùng lỏng/từ gốc (TW chính thức đọc là 機車 = đầu máy). VN dịch sát chữ 機関庫 thành "gara đầu máy" là sai.

### §2.5. Đại từ — 2 hàng

- **2128** — 双鉄 (nói với Fukami): JP 「それでよい。頼む。が、絶対に走るなよ」; TW 「可以。那就拜託你了。不過絕對不要用跑的」; VN cũ: 「Được rồi. Nhờ cậu nhé. Nhưng tuyệt đối không được chạy đâu đấy.」; Sửa: 「Được rồi. Nhờ em nhé. Nhưng tuyệt đối không được chạy đâu đấy.」 — Đây là câu nối tiếp yêu cầu ở 2126 (Soutetsu nhờ Fukami kiểm tra lại luồng di chuyển: "Fukami, nhờ em xác nhận lại…"), người nghe là Fukami. Soutetsu gọi Fukami là "em" xuyên suốt file (2126, 2115 dùng "anh" tự xưng); "cậu" ở đây lệch chuẩn xưng hô.
- **3567** — monologue: JP 「雲仙の栃木さんと、豊後森の木本さんへの連絡を済ませ、頷き一つで、了解を得られたことを伝えてくれる。」; TW 「跟雲仙的老闆櫪木先生以及豐後森的木本先生聯繫過後，她朝我點了點頭，表示對方已了解情況」; VN cũ: 「Em ấy đã liên lạc xong với anh Tochigi ở Unsen và anh Kimoto ở Bungomori, và báo cho tôi biết là đã được sự đồng ý bằng một cái gật đầu.」; Sửa: 「Em ấy đã liên lạc xong với bác Tochigi ở Unsen và bác Kimoto ở Bungomori, và báo cho tôi biết là đã được sự đồng ý bằng một cái gật đầu.」 — Tochigi (bếp trưởng kỳ cựu, gọi Hibiki là 嬢ちゃん) và Kimoto (lão kỹ sư, 老技師 ở 3525) đều là người lớn tuổi; giọng kể của Soutetsu trong file này luôn dùng "bác" cho hai người (1525 "bác Tochigi… bác Kimoto", 3338/3389/3558/3608 "bác Tochigi", 3604 "bác Kimoto"). 3567 là dòng duy nhất dùng "anh" cho hai người này — lệch chuẩn xưng hô trong chính file.

### §2.6. Thẻ %l thêm vào — 4 hàng (gỡ thẻ, giữ chữ)

JP không có thẻ %l ở những chỗ này; VN tự thêm thẻ gloss (dạng bịa của Gemini — tiền lệ ムナカタ来訪 đã gỡ 31 thẻ gloss 機関士 tương tự). Cách sửa: gỡ markup `\x%l…;#00ffc040;…%l;#;`, giữ nguyên chữ gloss làm chữ thường (nghĩa của gloss vẫn đúng).

- **2117** — 双鉄: JP chỉ có thẻ ở 扇形機関庫; 転車台 là chữ thường (TW có thẻ, JP không — lấy JP làm chuẩn). VN cũ thêm thẻ `\x%l転車台;#00ffc040;bàn quay đầu máy%l;#;`; Sửa: 「…và trải nghiệm bàn quay đầu máy, 18:30 sẽ xuất phát.」 — khớp cách 2238 viết "Bàn quay đầu máy" dạng thường.
- **2458** — 日々姫: JP 「[ぎそう,1]艤装」 chỉ có ruby, không có thẻ %l. VN cũ thêm thẻ `\x%l艤装;#00ffc040;Trang thiết bị nội ngoại thất%l;#;`; Sửa: 「Vâng. Trang thiết bị nội ngoại thất cũng gần như hoàn tất rồi ạ. …」
- **3113** — monologue: JP 「杜氏」 chữ thường, không thẻ. VN cũ thêm thẻ `\x%l杜氏;#00ffc040;Trưởng hầm rượu%l;#;`; Sửa: 「…kể từ khi trở thành Trưởng hầm rượu.」
- **3211** — monologue: JP 「指差し確認。」 chữ thường, không thẻ. VN cũ thêm thẻ `\x%l指差し確認;#00ffc040;Chỉ tay hô xác nhận%l;#;`; Sửa: 「Chỉ tay hô xác nhận. Lặp lại hai lần——vậy là xong.」

## §3. Kiểm tra cơ học và các mục đã xác minh là ĐÚNG (giữ nguyên)

- CSV3: bộ duy nhất, 598 dòng, 0 key trùng, 0 VN trống; thư mục CSV `translation_toml\02_Hibiki`.
- TOML: md5 `8a6fb6d483dd862dd0d22df29ccd99d2`, BOM + CRLF, [selections] rỗng, không có bản sao trùng (kiểm tra toàn bộ `sources/toml2/` — chỉ 1 file mang tên này, 1 copy duy nhất).
- TOML ↔ CSV3: 598 khóa script khớp tuyệt đối, 0 khóa thừa/thiếu; 376 khác biệt giá trị đều chỉ do TOML-2 làm phẳng literal `\n` thành khoảng trắng (375 dòng + 2783 có dạng "khoảng trắng + `\n`" thành 1 khoảng trắng) — 0 khác biệt thực sự; comment # JP trong [script] 598/598 khớp CSV3 JP tuyệt đối.
- Trùng VN ở 2+ key: 4 nhóm, đều hợp lệ — 「Hửm?」 (2182/2247, cùng JP む？), 「Oa!」 (2153/2159/2160, cùng là tiếng "wa"), 「A——」 (2185/2252, cùng là "A" + gạch ngang), 「Nếu vậy thì――」 (2416/2746, cùng nghĩa "nếu vậy thì") — không phải lệch hàng.
- 1576 「…………」 giống hệt ở JP/TW/VN — dấu lửng hợp lệ.
- Không rò rỉ chữ Hán/Nhật (0 dòng VN chứa CJK quá 30%); không còn marker ruby [x,N] nào trong VN; không có tag %l nào bị mất (JP = VN về số lượng tag ở mọi dòng trừ 4 dòng gỡ thẻ ở §2.6).
- Đại từ đã kiểm chứng theo dòng kề: Soutetsu "anh" với Hibiki (2064, 2377, 2555, 2629), với Fukami (2115, 2126), với Nagi (2730 "xin lỗi em"), với Fukami+Nagi (2085, 2452); độc thoại Soutetsu đồng nhất "tôi" (quét toàn bộ monologue: 0 dòng dùng "Anh"); Fukami tự xưng "em" với người lớn, "tớ" với Nagi (bạn cùng tuổi, 2217); Nagi tự xưng "em" với người lớn (2367, 2429), "tớ" với Fukami (2747); Mayami tự xưng "chị" (2140); Nagi gọi Soutetsu "anh hai" (2750) — khớp quy tắc đã sửa 20/11.
- 1487/2721 "tụi em" là lời của Fukami (1487 là độc thoại trích lời Fukami trong 『』; 2721 Fukami nói trực tiếp: "列車が自分で、何をできるか教えてくれてるから") — "tụi em" = nhóm bếp (Fukami + Nagi), đúng.
- 2214 Nagi thêm "Nagi đại nhân" (JP 「って、そぎゃん言い方好かんばい！！」 không có 凪さま): GIỮ NGUYÊN — đây là lối nói quen thuộc của Nagi trong chính file này (2739 「したら凪さま！」, 2741 「凪さまお願いしてくるばい！」 đều dịch "Nagi đại nhân"/"Nagi-sama"), thêm vào không đổi nghĩa câu (vẫn là "cách nói đó tớ không thích"). Ghi vào §6 để parent quyết nếu muốn tính sai.
- 2193 "ăn cẩu lương no luôn rồi ạ" cho 「あははーごちそうさまです――てっ」: GIỮ NGUYÊN — ごちそうさま ở đây là câu đùa "no nê" khi xem cảnh tình cảm (TW: "我吃飽了"); "ăn cẩu lương" (ngắm cặp đôi tình tứ đến no) giữ đúng trò đùa, không bịa nghĩa. てっ cuối là っ nhấn mạnh gắn với từ, không thêm Ư.
- 2629 "Cứu anh một bàn thua trông thấy" cho 助けられた: GIỮ NGUYÊN — thành ngữ bóng đá địa phương hoá cho "cậu đã cứu anh" (người nghe là Hibiki, "anh… em" đúng); nghĩa "được cứu" còn nguyên.
- 2515 bỏ tên gọi 登呂流湯さん đầu câu (VN: "Vâng. Vì cấu hình thấp và đơn giản, nên đứa bé đó sẽ bền bỉ… bà ấy cũng nói vậy"): GIỮ NGUYÊN — "bà ấy" vẫn chỉ rõ Tororyu-yu (đã nhắc ở 2350 "Bà chủ nhà tắm Tororyu-yu nói à"), nghĩa đủ; TW cũng dùng "她還說" (bà ấy cũng nói).
- 2259 "anh Akai" (Hibiki nói): GIỮ NGUYÊN — Akai là kỹ sư trẻ quay lại làm việc, Hibiki gọi "anh" là hợp lý.
- 2585 日ノ本 → "Hinamoto": GIỮ NGUYÊN (chưa có thuật ngữ chốt cho 日ノ本 — xem §6).
- 2333 鯛湾 → "Đài Loan": GIỮ NGUYÊN — 鯛湾 là cách chơi chữ với 台湾 (Đài Loan), TW dùng 邰灣 xác nhận.
- 2195 「ああっ！！」 → "A á!!": GIỮ NGUYÊN — っ được diễn thành nhịp "á" thứ hai, hợp lệ.
- 3706 （ブーっ、ブーっ） → "（Rung, rung）" và 3707 （プシューーーーっ） → "（Phìiiiiiii）": GIỮ NGUYÊN — độ dài âm đã diễn (ブー = rung, プシュー = phì dài); っ ngắt cuối là nuance SFX, không tính sai.
- 2064 "Anh cảm thấy…" (双鉄, không phải monologue): đúng — Soutetsu nói với Hibiki về bộ đồng phục cô thiết kế, "anh" với Hibiki là chuẩn.

## §4. Lượt soát 2 (đọc lại toàn bộ fix)

20/20 tái kiểm chứng, 0 bỏ, 0 sửa. Từng fix đọc lại với JP của chính hàng đó: 2117 (gỡ thẻ 転車台, giữ gloss thường — khớp 2238), 2128 (cậu→em, nối tiếp 2126), 2142/2143 (cười → Ufufu, khớp 2140), 2152 (はぁ～っ → Hà~Ư, cùng lớp với sweep 2783), 2181/2196/2201/2213/2783/2785 (sweep, áp nguyên sau kiểm chứng), 2342 (帝鉄 → Teitetsu), 2458/3113/3211 (gỡ thẻ, giữ gloss), 2545 (đứa bé này → hai đứa, TW 她倆), 2585/3038 (冥国 → Minh Quốc), 2718 (gara đầu máy → đầu máy, TW 機車), 3567 (anh → bác ×2, khớp 1525/3604). Không fix nào bị loại hay sửa lại ở lượt 2.

## §5. Khối TOML (đã kiểm chứng parse)

```toml
"2117" = "「Theo dự kiến ban đầu, 18:00 sẽ đến ga Bungomori. Sau khi trải nghiệm đưa xe vào \\x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#; và trải nghiệm bàn quay đầu máy, 18:30 sẽ xuất phát.」"
"2128" = "「Được rồi. Nhờ em nhé. Nhưng tuyệt đối không được chạy đâu đấy.」"
"2142" = "「Ufufu, thực ra chị đã luôn muốn thử làm rồi. Những việc mà Hi-chan và Sou-chan vẫn hay làm ấy.」"
"2143" = "「Ufufu, mong chờ quá đi. Cho tôi vé có kèm theo bữa ăn nhé.」"
"2152" = "「Hít~——Hà~Ư——」"
"2181" = "「Uuu~~Ư」"
"2196" = "「Ư!」"
"2201" = "「Ư!!!」"
"2213" = "「Ư!!?」"
"2342" = "「Mấy tay cuồng Teitetsu hay lui tới chỗ Tochigi lắm. Tên này thích nói chuyện về toa ăn mà lại」"
"2458" = "「Vâng. Trang thiết bị nội ngoại thất cũng gần như hoàn tất rồi ạ. Tiếp theo là chạy thử nhiều lần để kiểm tra mặt vận hành, sau đó là các thiết bị」"
"2545" = "「Mọi người vui vẻ thì em cũng mừng. Vì hai đứa đã trải qua rất nhiều vất vả mà」"
"2585" = "「Kiểu Minh Quốc tuy có tính đa dụng cao, nhưng nghe nói về độ hiểu biết toa xe thì không bằng hàng của Hinamoto hay Anh」"
"2718" = "「Cái đầu máy tên là Kyuroku gì đó, so với Hachiroku, trông có vẻ to hơn hẳn nhỉ.」"
"2783" = "「~~Ư! Xin cảm ơn quý khách đã sử dụng dịch vụ ạ!」"
"2785" = "「~~~~~~~Ư」"
"3038" = "Railord của Toa ăn Train, được kế thừa từ trước khi cải tạo, là hàng do Minh Quốc sản xuất——"
"3113" = "Chị Mayami đã vô cùng vui sướng nhận lấy, thậm chí còn xin nghỉ phép lần đầu tiên kể từ khi trở thành Trưởng hầm rượu."
"3211" = "Chỉ tay hô xác nhận. Lặp lại hai lần——vậy là xong."
"3567" = "Em ấy đã liên lạc xong với bác Tochigi ở Unsen và bác Kimoto ở Bungomori, và báo cho tôi biết là đã được sự đồng ý bằng một cái gật đầu."
```

Kiểm chứng: khối parse được bằng tomllib, 20 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; tag %l được escape đúng `\\x%l…` nên parse ra đúng giá trị `\x%l…`). Tất cả fix đều 1 dòng, không có `\n` thủ công (game tự ngắt dòng). Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (xem log build).

## §6. Ghi chú cho Hieu (cần quyết / chờ thống nhất — không tính sai trong audit này)

- Thống nhất "Ohimitera"/"Ohito" → "Ohitoyo" (16 dòng dạng cũ: 1619, 2051, 2270, 2349, 2535, 2633, 2970, 3027, 3106, 3111, 3132, 3149, 3495, 3719 "Đường sắt Ohito", 3736, 3739 — theo tiền lệ các file trước, fix trong đợt thống nhất).
- Tên gọi "とれいん食堂": trong file này "Toa ăn Train" 8 dòng (1572, 2082, 2258, 2431, 3038, 3319, 3608, 3652) vs "Tàu nhà hàng" 13 dòng (2094, 2135, 2198, 2270, 2405, 2501, 2944, 3090, 3343, 3574, 3600, 3736, 3739) — toàn dự án cũng chia đôi (CSV3: 10 dòng "Toa ăn Train" vs 11 dòng "Tàu nhà hàng"), chưa có thuật ngữ chốt. Cần Hieu chốt một tên rồi thống nhất sau.
- 日ノ本 → "Hinamoto" (2585): giữ nguyên — chưa có thuật ngữ chốt (TW dùng 日本式); nếu chốt "Nhật Bản"/"Hinomoto" thì sửa trong đợt thống nhất.
- 2152 "Hà~Ư——" (はぁ～っ――): gasp do audit tự tìm, sweep không liệt kê — parent kiểm chứng lại giúp (cùng lớp trailing-mid với sweep 2783).
- 2214 "Nagi đại nhân" thêm vào (JP không có 凪さま): giữ nguyên vì là lối nói quen thuộc của Nagi trong file (2739/2741) — parent quyết nếu muốn tính sai/gỡ.
- 2193 "ăn cẩu lương" và 2629 "Cứu anh một bàn thua trông thấy": cách diễn sáng tạo, giữ nguyên — Hieu muốn diễn thẳng hơn thì báo.

## Kết bài

File 日々姫08_とれいん食堂: 598 dòng đã đọc hết, **20 dòng sai (3,3%)** — 7 gasp っ (6 sweep + 1 tự tìm), 2 tiếng cười bị nhét gasp, 3 thuật ngữ, 2 dịch sai nghĩa, 2 đại từ, 4 thẻ %l thêm vào. Không có chuỗi xoay, không lệch hàng, không lỗi đại từ hệ thống — file khá sạch, lỗi tập trung ở SFX và các chi tiết nhỏ. JSON 20 khóa chuỗi; khối TOML parse OK, 20 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 20/20; lượt soát 2: 20/20, 0 bỏ, 0 sửa.
