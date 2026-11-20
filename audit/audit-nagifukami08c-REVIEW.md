# Audit: Nagi_Fukami 08c — 凪ふかみ08c_新しい家族.txt.toml

**Tệp TOML:** `07_Nagi_Fukami/凪ふかみ08c_新しい家族.txt.toml` — md5 `57e635feca460be6e6b563f3201ab484`, 104.311 byte, BOM + CRLF (1.017 CRLF, 0 LF-only), `[selections]` rỗng, **không có bản sao trùng** (chỉ 1 tệp 08c trong 227 tệp TOML; 08b là file khác).

**Nội dung:** Soutetsu kiệt sức ngã gục, Nagi và Fukami chăm sóc; anh đề xuất ý tưởng "gia đình mới" (ba người thành một nhà); cuộc họp toàn thể với Paulette, Kisaki, Hachiroku, Reina, Mayami, hai ông Minokasa và Seki; đề xuất "Đặc khu Hình thái Gia đình mới", lập pháp hóa hợp đồng gia đình; kết ở 7 năm sau với "Gia đình được chứng nhận".

## 1. Tổng quan

**17/483 dòng sai (3,5%)** — thoại 14/339 (4,1%), độc thoại 3/144 (2,1%). Tỉ lệ thấp nhất nhóm Nagi_Fukami từ trước đến nay (08b 11,3%, h1 15,3%), file dịch khá sạch; lỗi tập trung ở đại từ xưng hô (8/17).

Phân loại (17): đại từ 8 (Soutetsu tự xưng "em"→"tôi" với Mayami 3: 2516, 2329, 2290; Soutetsu gọi Paulette "cậu"→"em" 2: 2290, 2131; Paulette gọi Soutetsu "cậu Soutetsu"→"anh Soutetsu" 4: 1838, 2514, 1870, 2332 — khóa B4), sai nghĩa 3 (倒れる→"ngã bệnh" 2: 1823, 2336; それぞれで→"từng người" 1: 2270), gasp 1 (2140, sweep lost-gasp-trailing áp nguyên), SFX 1 (2073 ふあっ "Oa"→"Phùa"), thẻ 3 (rò chữ JP trong ruby 2413; thẻ %l mang thuật ngữ TW 3071, 2996), lỗi đánh máy 1 (2956 dấu `'` thừa).

- Lệch dòng (misaligned): **0**. Chuỗi xoay (rotation chain): **0**. Tràn từ chương khác (contamination): **0** (kiểm tra bằng project VN index: VN dài >25 ký tự không trùng dòng nào ở file khác). Dòng mồ côi (orphan VN): **0**. Dòng chưa dịch: **0**. Trùng key: **0**. Dòng chưa chắc chắn (uncertain): **1** (2030 — xem §3.1).

## 2. Kiểm tra nguồn và cấu trúc

- CSV3 bộ duy nhất: 483 dòng, section `script` toàn bộ, 0 key trùng, 0 VN trống. CSV3↔TOML: 483/483 key khớp; VN khớp tuyệt đối 189 dòng + 294 dòng chỉ khác ở chỗ TOML-2 gộp `\n` thành khoảng trắng (đã kiểm chứng cơ học: sau khi thay `\n` bằng khoảng trắng thì 0 khác biệt thực chất).
- Comment `# JP:` trong khối `[script]`: 483/483 khớp đúng JP CSV3 (20 comment `# JP:` còn lại nằm ở `[characters]`/`[info]`, không phải dòng thoại).
- Thẻ %l: 14 thẻ trong file, tất cả đúng cấu trúc mở/đóng; 11 thẻ có thuật ngữ JP khớp đúng dòng JP; 3 thẻ sai xem §3.6 (3108 `[窯]` giữ nguyên — JP viết カマ, katakana của 窯, cùng một từ, không phải lỗi).
- Sweep っ: 2 mục cho file này — 2140 áp nguyên bản sửa (xem §3.4); 3052 "needs-file-audit" đã tự xử lý: VN "Fukami và Nagi gật đầu với nhau――hả!?" đã diễn gasp っ thành "hả" (cùng với !?), không mất âm, **không sửa** (xem §6.3).

## 3. Lỗi sai (chi tiết 17 dòng)

### 3.1 Đại từ (8 dòng)

**2516 — 双鉄 (Soutetsu trả lời Mayami) — "em"→"tôi"**

- JP: 「そこは、今はまだ精査していない。が――国会で成立する法案は、殆どが内閣による提出と聞く」
- TW: 「這方面我還沒仔細了解，但是……聽說在國會通過的法案幾乎都是由內閣提出的」
- Cũ: 「Chuyện đó, hiện tại em vẫn chưa xem xét kỹ lưỡng. Nhưng mà――Nghe nói các dự luật được thông qua tại Quốc hội, hầu hết đều do Nội các đệ trình.」
- Mới: 「Chuyện đó, hiện tại tôi vẫn chưa xem xét kỹ lưỡng. Nhưng mà――Nghe nói các dự luật được thông qua tại Quốc hội, hầu hết đều do Nội các đệ trình.」
- Lý do: Soutetsu tự xưng "tôi" với Mayami (quy tắc đã chốt; tiền lệ: file khác 14 dòng "em" với Mayami đều sai; lr真闇追加01 7 fix đại từ đều Mayami→"tôi"). Mayami vừa hỏi ở 2491, Soutetsu trả lời bà.

**2329 — 双鉄 (Soutetsu trả lời Mayami) — "em"→"tôi"**

- JP: 「それは、確かに。ので、社会的な機運を盛り上げ、必要性を認知して貰っての、議員立法でと考えている」
- TW: 「是的。因此，我希望推動社會理解，請議員參與立法」
- Cũ: 「Điều đó, quả thực là vậy. Vì thế, em đang nghĩ đến việc lập pháp do nghị sĩ đệ trình, sau khi dấy lên làn sóng xã hội và được công nhận về sự cần thiết.」
- Mới: 「Điều đó, quả thực là vậy. Vì thế, tôi đang nghĩ đến việc lập pháp do nghị sĩ đệ trình, sau khi dấy lên làn sóng xã hội và được công nhận về sự cần thiết.」
- Lý do: như 2516 — vẫn đang trả lời Mayami (bà hỏi tiếp ở 2216, Soutetsu đáp).

**2290 — 双鉄 (2 lỗi đại từ trong 1 dòng) — tự xưng "em"→"tôi" (nghe Mayami) + gọi Paulette "cậu"→"em"**

- JP: 「と、認識しているが――確認を頼んでもよいか？　ポーレット」
- TW: 「據我所知是這樣的……應該沒錯吧，波萊特？」
- Cũ: 「Em cũng hiểu là vậy nhưng――Có thể nhờ cậu xác nhận lại không? Paulette.」
- Mới: 「Tôi cũng hiểu là vậy nhưng――Có thể nhờ em xác nhận lại không? Paulette.」
- Lý do: nửa đầu trả lời Mayami (2491 bà hỏi "hiểu vậy là đúng chứ?") nên tự xưng "tôi"; nửa sau quay sang nhờ Paulette xác nhận — Soutetsu gọi Paulette là "em" (quy ước toàn dự án: "em" 119 vs "cô" 49, các file trước sửa hệ thống "cô"→"em"; "cậu" là dạng duy nhất trong toàn dự án ở đây, xem §6.4).

**2131 — 双鉄 (nói với Paulette) — "Cậu"→"Em"**

- JP: 「心得た。というか――それは、つまりは――特区を目指してくれるのか！」
- TW: 「好的。那麼……你的意思是，你願意認可建立特區的目標？」
- Cũ: 「Đã hiểu. Hay nói đúng hơn――vậy, tức là――Cậu sẽ hướng tới việc thành lập Đặc khu sao!」
- Mới: 「Đã hiểu. Hay nói đúng hơn――vậy, tức là――Em sẽ hướng tới việc thành lập Đặc khu sao!」
- Lý do: như 2290 — người nghe là Paulette (bà vừa nói ở 1870, Soutetsu đáp). Soutetsu gọi Paulette "em", không phải "cậu".

**1838 — ポーレット — "cậu Soutetsu"→"anh Soutetsu" (khóa B4)**

- JP: 「これを……双鉄くんと、ふかみちゃんと凪ちゃんで？」
- TW: 「你、小深和小凪準備這樣？」
- Cũ: 「Cái này……cậu Soutetsu, bé Fukami và Nagi cùng làm sao?」
- Mới: 「Cái này……anh Soutetsu, bé Fukami và Nagi cùng làm sao?」
- Lý do: khóa B4 — Paulette gọi 双鉄くん là "anh Soutetsu" (tiền lệ đã được parent kiểm chứng giữ lại ở 08b key 2436: "cậu Soutetsu"→"Anh Soutetsu"). Ngoại lệ duy nhất là câu tự sửa くん→さん (Common05 2721/2421/2275) — dòng này không có tự sửa.

**2514 — ポーレット — "nhóm cậu Soutetsu"→"nhóm anh Soutetsu" (khóa B4)**

- JP: 「確かにそれは、双鉄君たちのアイディアと努力が、一番目に見えて発揮されたケースだと思います」
- TW: 「這個確實是一個雙鐵君通過自己的設想和努力，拿出了足夠成果的例子」
- Cũ: 「Đó quả thực là trường hợp mà ý tưởng và sự nỗ lực của nhóm cậu Soutetsu, được phát huy một cách rõ rệt nhất đấy.」
- Mới: 「Đó quả thực là trường hợp mà ý tưởng và sự nỗ lực của nhóm anh Soutetsu, được phát huy một cách rõ rệt nhất đấy.」
- Lý do: như 1838 — 双鉄君たち của Paulette cũng theo khóa B4.

**1870 — ポーレット — "nhóm cậu Soutetsu"→"nhóm anh Soutetsu" (khóa B4)**

- JP: 「普段どおりに。明るく元気に、幸せに。双鉄くんたちは、モデルケースになってください」
- TW: 「保持現狀。開朗向上、健康幸福。你們以後就是模範案例」
- Cũ: 「Cứ như bình thường thôi. Vui vẻ, khỏe mạnh và hạnh phúc. Nhóm cậu Soutetsu, hãy trở thành trường hợp kiểu mẫu nhé.」
- Mới: 「Cứ như bình thường thôi. Vui vẻ, khỏe mạnh và hạnh phúc. Nhóm anh Soutetsu, hãy trở thành trường hợp kiểu mẫu nhé.」
- Lý do: như 1838.

**2332 — ポーレット — "nhóm cậu Soutetsu"→"nhóm anh Soutetsu" (khóa B4)**

- JP: 「はい。双鉄くんたちの姿をみて、みんなが、『彼らが家族になれないのはおかしい』って思う位に」
- TW: 「是的。要讓大家看著你們的模樣，覺得你們理所應當成為一家人」
- Cũ: 「Đúng vậy. Để khi nhìn vào hình ảnh của nhóm cậu Soutetsu, mọi người sẽ nghĩ rằng 'Bọn họ không thể trở thành gia đình thì thật kỳ lạ'.」
- Mới: 「Đúng vậy. Để khi nhìn vào hình ảnh của nhóm anh Soutetsu, mọi người sẽ nghĩ rằng 'Bọn họ không thể trở thành gia đình thì thật kỳ lạ'.」
- Lý do: như 1838.

**2030 — 双鉄 — LOẠI BỎ bởi parent (20/11 ~05:40) — giữ VN cũ "anh", ghi uncertain**

- JP: 「うむっ――まぁ、それは確かにだ。いかんな、僕が足を引っ張ってしまったか」
- TW: 「唔……嗯，沒錯。不行啊，我居然拖後腿了」
- VN cũ (GIỮ): 「Ưm――chà, điều đó thì đúng thật. Không được rồi, là anh đã ngáng chân mọi người sao.」
- Lý do loại: agent cho rằng dòng này trả lời Hachiroku ở 2554, nhưng 2554 thuộc cảnh khác (cuối buổi họp, cả nhóm ra về — 2550–2559), cách 524 key; dòng kề trực tiếp là Nagi 2029 gọi "にーさん" và hỏi về nước ("チームワークのお水") — Soutetsu đáp lại Nagi nên "anh" là đúng theo quy tắc đã chốt. Không đủ bằng chứng đổi sang "tôi"; theo brief, khi chưa chắc thì giữ VN cũ và ghi uncertain — chờ Hieu chốt nếu muốn đổi. Đã gỡ khỏi JSON + khối TOML; tổng còn 17.

### 3.2 Sai nghĩa (3 dòng)

**1823 — 凪 — 倒れさせちゃった: "ngã bệnh"→"ngã gục"**

- JP: 「ばってん、にーさんを倒れさせちゃったの、うちらの責任もおっきかとねって、話し合っとったばい」
- TW: 「但是經過討論，咱們覺得大哥哥會暈倒，也有很大一部分是咱們的責任」
- Cũ: 「Cơ mà, việc để anh Soutetsu ngã bệnh, bọn em đã bàn bạc và thấy mình cũng có trách nhiệm lớn lắm.」
- Mới: 「Cơ mà, việc để anh Soutetsu ngã gục, bọn em đã bàn bạc và thấy mình cũng có trách nhiệm lớn lắm.」
- Lý do: 倒れる ở đây là ngã gục/ngất (cả chương bàn về "cách ngã" 倒れ方: 2110 "như sụp đổ xuống", 2325 "cả hai cùng ngã nhào"); "ngã bệnh" (mắc bệnh) sai nghĩa. Toàn dự án 倒れる thường dịch "ngất"/"ngã gục"/"bị ngã" (15+10+7), "ngã bệnh" chỉ 3 lần (2 lần ở file này + 1 ở hachiroku h5 chưa audit).

**2336 — ふかみ — 倒れたばっかり: "ngã bệnh"→"ngã gục"**

- JP: 「ですです！　倒れたばっかりなんですから」
- TW: 「是的是的！你才剛醒過來不久呢」
- Cũ: 「Đúng rồi ạ! Anh vừa mới ngã bệnh xong mà.」
- Mới: 「Đúng rồi ạ! Anh vừa mới ngã gục xong mà.」
- Lý do: như 1823 — anh vừa ngã gục xong, không phải vừa ốm xong.

**2270 — ふかみ — それぞれで: "từng người"→"hai người một nhóm"**

- JP: 「あの……わたしたち、それぞれでと、三人でと――休みのたびに、出かけたり遊んでたりしてましたよね」
- TW: 「我說……我們每次休假的時候，都會分成兩人單獨出去玩，和三個人一起出去玩吧」
- Cũ: 「À ừm……chúng em, đi riêng từng người, hoặc đi chung ba người――Cứ mỗi dịp nghỉ là lại đi ra ngoài chơi nhỉ.」
- Mới: 「À ừm……chúng em, lúc thì đi chơi riêng hai người, lúc thì đi chung cả ba――Cứ mỗi dịp nghỉ là lại đi ra ngoài chơi nhỉ.」
- Lý do: それぞれで = đi theo từng cặp (hai người một nhóm), không phải đi lẻ từng người; TW 分成兩人 xác nhận. JP đối lập それぞれで (cặp đôi) với 三人で (cả ba).

### 3.3 Gasp (1 dòng)

**2140 — 凪 — áp nguyên bản sửa sweep (lost-gasp-trailing)**

- JP: 「にーさんとふかみちゃんが結婚したかったら――っ！」
- TW: 「如果大哥哥跟小深想結婚的話……啊！」
- Cũ: 「Nếu anh Soutetsu và bé Fukami muốn kết hôn thì――!」
- Mới: 「Nếu anh Soutetsu và bé Fukami muốn kết hôn thì――Ư!」
- Lý do: gasp cuối っ sau ―― bị mất; sweep đã liệt kê đúng, áp nguyên.

### 3.4 SFX (1 dòng)

**2073 — 凪＆深美 — ふあっ: "Oa"→"Phùa"**

- JP: 「にへへー！」\n「ふあっ」
- TW: 「嘿嘿嘿！」\n「哇」
- Cũ: 「Nihehe~!」\n「Oa」
- Mới: 「Nihehe~!」\n「Phùa」
- Lý do: ふあっ mất âm "ph" khi dịch thành "Oa"; tiền lệ lr_凪h2 (ふぁ/ふあ → "phà"/"phùa", 38 dòng) và 08b (2174/2176 ふぁっ → "Phà"). Các tiếng ふあ/はう/ひゃう/うお trong file đều giữ âm gốc bằng cách phiên âm (Hau, Hyau, Uoa, Ngigigi, kua~) — chỉ dòng này làm mất phụ âm đầu.

### 3.5 Thẻ (3 dòng)

**2413 — ポーレット — rò chữ Nhật trong thẻ ruby**

- JP: 「当たり前です！[わ　　た　　し　　た　　ち　　の　　な　　か,7]初恋の人のお願いじゃないですか」
- TW: 「當然了！[我們可是朋友啊,13]畢竟是初戀情人拜託自己的事情」
- Cũ: 「Tất nhiên rồi! Đó là lời thỉnh cầu của [わ　　た　　し　　た　　ち　　の　　な　　か,7]tình đầu mà.」
- Mới: 「Tất nhiên rồi! Đó là lời thỉnh cầu của [trong số chúng ta,7]tình đầu mà.」
- Lý do: VN giữ nguyên thẻ ruby tiếng Nhật chưa dịch — rò chữ ngoại (mẫu bịa của Gemini). Ruby わたしたちのなか = "trong số chúng ta" (người yêu đầu là một người trong nhóm); giữ nguyên số `,7` theo quy ước toàn dự án (vd. "[Occident Express,3]", "[Hachiroku,3]8620", "[bạn thanh mai trúc mã,3]").

**3071 — monologue — thẻ %l mang thuật ngữ TW**

- JP: 出発信号機は進行現示。逆転機を前進フルギアに。
- TW: 發車信號機顯示可以行進。我將迴轉機打到滿檔前進。
- Cũ: Đèn tín hiệu xuất phát hiển thị cho phép đi. Tôi kéo \x%l逆転機;#00ffc040;cần đảo chiều%l;#; sang \x%l満檔前進;#00ffc040;cài hết số tiến%l;#;.
- Mới: Đèn tín hiệu xuất phát hiển thị cho phép đi. Tôi kéo \x%l逆転機;#00ffc040;cần đảo chiều%l;#; sang \x%l前進フルギア;#00ffc040;cài hết số tiến%l;#;.
- Lý do: thuật ngữ JP trong thẻ là 満檔前進 — chữ Hán phồn thể của TW (滿檔前進), không có trong dòng JP (JP: 前進フルギア). Chỉ sửa thuật ngữ JP trong thẻ, giữ nguyên gloss "cài hết số tiến".

**2996 — monologue — thẻ %l mang thuật ngữ TW**

- JP: そうして手早く、単弁を運転位置へと持っていく。
- TW: 接著立刻將單剎拉到行駛位置。
- Cũ: Rồi nhanh tay, gạt \x%l単弁;#00ffc040;van hãm đơn%l;#; về \x%l行駛位置;#00ffc040;vị trí chạy tàu%l;#;.
- Mới: Rồi nhanh tay, gạt \x%l単弁;#00ffc040;van hãm đơn%l;#; về \x%l運転位置;#00ffc040;vị trí chạy tàu%l;#;.
- Lý do: như 3071 — 行駛位置 là tiếng Trung (TW), JP là 運転位置. Chỉ sửa thuật ngữ JP trong thẻ, giữ nguyên gloss "vị trí chạy tàu".

### 3.6 Lỗi đánh máy (1 dòng)

**2956 — monologue — dấu `'` thừa**

- JP: 『認定家族』。四年に一度、裁判所への申請と許諾を受ければ維持できる、法的に保護された新形体の家族。
- TW: 我們是"特許家庭"。這是一種新型家庭，只要每四年向家事法庭遞交一次申請並獲得批准，即可受法律保護。
- Cũ: Gia đình được chứng nhận'. Một hình thái gia đình mới được pháp luật bảo vệ, có thể duy trì bằng cách nộp đơn và nhận được sự cho phép của tòa án bốn năm một lần.
- Mới: Gia đình được chứng nhận. Một hình thái gia đình mới được pháp luật bảo vệ, có thể duy trì bằng cách nộp đơn và nhận được sự cho phép của tòa án bốn năm một lần.
- Lý do: dấu `'` sau "chứng nhận" là tàn dư của ngoặc 『』 (mở đầu bị mất, chỉ còn dấu đóng) — lỗi đánh máy.

## 4. Kiểm tra lệch dòng / chuỗi xoay / nhiễm chéo

- **Lệch dòng 0:** đã đọc toàn bộ 483 dòng đối chiếu JP + TW; không có dòng VN nào là lời thoại khác hẳn JP của nó. Hai dòng "ngã bệnh" (1823, 2336) là dịch sai nghĩa, không phải lệch dòng — VN vẫn bám sát JP của chính dòng đó.
- **Chuỗi xoay 0:** không có cặp dòng nào mà bản dịch đúng nằm ở key sai trong file.
- **Nhiễm chéo 0:** VN dài >25 ký tự không trùng với bất kỳ dòng nào ở file khác (3 ca nhiễm đã biết toàn dự án không xuất hiện ở đây).
- **Dòng mồ côi 0 / chưa dịch 0 / trùng key 0:** mọi VN đều có nguồn JP/TW tương ứng; không có VN trống.

## 5. Lượt soát 2

Đọc lại toàn bộ 18 bản sửa đối chiếu từng JP: **18 tổng / 18 tái kiểm chứng / 0 loại bỏ / 0 sửa lại**. Ghi chú: trong lúc kiểm chứng cơ học, phát hiện 12 bản sửa viết tay ban đầu thiếu cặp ngoặc 「」 mà VN cũ có (1823, 1838, 1870, 2030, 2131, 2270, 2290, 2329, 2332, 2336, 2514, 2516) — đã bổ sung lại trước khi chốt; đây là lỗi chép lại, không phải phán đoán dịch, nên không tính vào lượt soát 2. Sau khi sửa, diff-sanity 18/18 chỉ khác ở chỗ sửa có chủ đích (tỉ lệ tương đồng 0,75–1,00; thấp nhất 2413 do thay toàn bộ gloss ruby, 2270 do viết lại một mệnh đề). **Parent 20/11 ~05:40: loại 1 bản (2030, xem §3.1) khỏi JSON + khối TOML; còn 17 bản, diff-sanity 17/17. Lượt soát 2 chốt: 18 tổng / 17 tái kiểm chứng / 1 loại bỏ / 0 sửa lại.**

## 6. Ghi chú / phán đoán cần Hieu (không tự quyết)

- **6.1 Seki gọi "ông nội" hay "ông ngoại"? — CÂU HỎI TOÀN DỰ ÁN, không sửa ở file này.** Fukami gọi Seki là おじいちゃん, VN dịch "ông nội" ở 2402 ("Ông nội.") và 365 ("Ông nội kỳ quá."). Bằng chứng JP: Seki gọi Midori là 娘 (con gái) ở 2456 ("Midori――con bé đó là một người không có may mắn"), Midori là mẹ Fukami → Seki là ông ngoại (bên mẹ) theo họ hàng Việt, không phải ông nội. Nhưng toàn dự án đều dùng "ông nội" cho Seki (hachiroku08 2117, hibiki03 2368/2607, hibiki09 2010, nagifukami02 1338) và cho cả nhóm おじいちゃんたち (Seki + Minokasa). Đổi riêng 2 dòng ở file này sẽ gây mất nhất quán toàn dự án — cần Hieu chốt có đổi "ông nội"→"ông ngoại" cho Seki toàn dự án hay giữ nguyên quy ước hiện tại. (Minokasa thì chắc chắn "ông nội" đúng: Nagi mang họ Minokasa, ông nhắc đến "mấy đứa con trai ông" ở 2530.)
- **6.2 Nagi tự xưng "mình" (1984, 1995, 436) — giữ nguyên.** Nagi dùng "em" với Soutetsu, "cháu" với ông nội, "mình" khi nói chung với cả nhóm ("Mình gọi ông nội tới…", "Mình cũng hoàn toàn…", "Mình đang cùng bé Fukami…"). "Mình" là đại từ tự xưng trung tính hợp lệ; không có quy tắc dự án nào quy định đại từ tự xưng của Nagi. Không sửa.
- **6.3 Key 3052 (sweep needs-file-audit) — giữ nguyên, đã xử lý.** JP 「ふかみと凪はうなずきあって――っ！？」, VN "Fukami và Nagi gật đầu với nhau――hả!?" — gasp っ đã được diễn thành "hả" (kèm !?), không mất âm như 2140 (VN lúc đó chỉ có "――!"). Không cần thêm Ư.
- **6.4 Soutetsu gọi Paulette "cậu" — chỉ 2 lần trong toàn dự án, cả 2 đều ở file này (2290, 2131).** Quy ước đã chốt là "em" (119 lần "em" vs 49 lần "cô", các file trước sửa hệ thống "cô"→"em"); "cậu" là dạng lạc lõng duy nhất nên sửa về "em" theo quy ước. Key 2030 đã bị parent loại (xem §3.1): 2554 thuộc cảnh khác (2550–2559), dòng kề trực tiếp là Nagi 2029 — giữ VN cũ "anh", ghi uncertain, chờ Hieu chốt.
- **6.5 Grand01 còn sót 2 dòng Paulette "cậu Soutetsu" (2756, 2181) chưa sửa** — audit Grand01 làm trước khi đính chính B4 (19/11 22:24) nên bỏ sót; không thuộc file này, báo để parent ghi nhận cho đợt rà soát lại Grand01.
- **6.6 Ghi chú nhỏ (không tính sai):** 1403 "……Hai, đứa" — dấu phẩy mô phỏng dấu 、 trong JP (二人、とも), giữ nguyên. 2414 "Cháu nghĩ đó là!" — trật tự từ hơi vụng ("Vì cháu nghĩ đó là chuyện quan trọng mà" sẽ mượt hơn) nhưng nghĩa đúng, không sửa. 327 餅は餅屋 → "Trăm hay không bằng tay quen" — đổi tục ngữ tương đương, chấp nhận được. 修学旅行 → "chuyến đi dã ngoại" — dùng nhất quán cả file, giữ nguyên. Các tiếng phiên âm giữ âm gốc (Hau, Hyau, Uoa, Nihe, Ngigigi, kua~) giữ nguyên theo quy tắc SFX của Hieu. 3108 thẻ [窯] giữ nguyên (JP viết カマ = katakana của 窯). 241 "Cảm ơn cô" với Kisaki giữ nguyên theo tiền lệ đã chốt (file khác 1533 "Cảm ơn cô" = Kisaki đúng, khác 1559 = Mayami đã sửa thành "chị"). 375 Minokasa gọi 双鉄くん dịch trần "Soutetsu" trong lời trích của Nagi — đúng (không phải xưng hô trực tiếp); 384 "Cậu Soutetsu" của Minokasa giữ nguyên (ông già gọi thanh niên là "cậu", đúng như Seki ở 2389).

## 7. Mục chờ thống nhất (không tính vào 18 dòng sai)

- **"Ohito" (dạng cũ của 御一夜, đợi đợt thống nhất → "Ohitoyo"):** 7 dòng / 8 lần — 2585 (1 lần), 2199 (2 lần: "Đường sắt Ohito", "thành phố Ohito"), 2196, 2041, 2420, 2341, 2248.
- **"Yui" (dạng cũ của 湯医, đợi đợt thống nhất → "Yunoi"):** 2 dòng — 2541 ("Hẹn gặp lại ở Yui nhé!"), 2068 ("Ừ, hẹn gặp ở Yui.").
- Các dạng cũ khác: 0 (không có Ohimitera, "Đường sắt Hoàng gia", "Migita System", "Master Controller", "Obata" trong file).

## Kết bài

File 凪ふかみ08c — "Gia đình mới" — có **17/483 dòng sai (3,5%)**, thoại 14/339 (4,1%), độc thoại 3/144 (2,1%). Đây là file sạch nhất nhóm Nagi_Fukami đến nay: không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi hay chưa dịch. Lỗi tập trung ở đại từ xưng hô (8/17) — ba nhóm hệ thống: Soutetsu tự xưng "em" với Mayami (3 dòng), Soutetsu gọi Paulette "cậu" thay vì "em" (2 dòng), Paulette gọi Soutetsu "cậu Soutetsu" thay vì "anh Soutetsu" theo khóa B4 (4 dòng); còn lại là sai nghĩa lẻ (倒れる→"ngã gục" 2 dòng, それぞれで→"hai người một nhóm" 1 dòng), gasp sweep 1 dòng, SFX 1 dòng, thẻ 3 dòng (1 rò chữ Nhật trong ruby + 2 thẻ %l mang thuật ngữ tiếng Trung từ TW), lỗi đánh máy 1 dòng. Lượt soát 2: 18 tổng / 17 tái kiểm chứng / 1 loại bỏ (2030, parent) / 0 sửa lại. Ba việc để lại cho Hieu: (1) quyết "ông nội" hay "ông ngoại" cho Seki toàn dự án (§6.1); (2) đợt thống nhất "Ohito"→"Ohitoyo" (7 dòng) và "Yui"→"Yunoi" (2 dòng) trong file này; (3) key 2030 — giữ "anh" (người nghe là Nagi 2029) hay đổi "tôi" (nhóm có Hachiroku).

### Khối TOML (đã kiểm chứng parse)

```toml
[script]
"1823" = "「Cơ mà, việc để anh Soutetsu ngã gục,\\nbọn em đã bàn bạc và thấy mình cũng có trách nhiệm lớn lắm.」"
"1838" = "「Cái này……anh Soutetsu, bé Fukami và Nagi cùng làm sao?」"
"1870" = "「Cứ như bình thường thôi. Vui vẻ, khỏe mạnh và hạnh phúc.\\nNhóm anh Soutetsu, hãy trở thành trường hợp kiểu mẫu nhé.」"
"2073" = "「Nihehe~!」\\n「Phùa」"
"2131" = "「Đã hiểu. Hay nói đúng hơn――vậy, tức là――\\nEm sẽ hướng tới việc thành lập Đặc khu sao!」"
"2140" = "「Nếu anh Soutetsu và bé Fukami muốn kết hôn thì――Ư!」"
"2270" = "「À ừm……chúng em, lúc thì đi chơi riêng hai người, lúc thì đi chung cả ba――\\nCứ mỗi dịp nghỉ là lại đi ra ngoài chơi nhỉ.」"
"2290" = "「Tôi cũng hiểu là vậy nhưng――\\nCó thể nhờ em xác nhận lại không? Paulette.」"
"2329" = "「Điều đó, quả thực là vậy. Vì thế, tôi đang nghĩ đến việc lập pháp do nghị sĩ đệ trình,\\nsau khi dấy lên làn sóng xã hội và được công nhận về sự cần thiết.」"
"2332" = "「Đúng vậy. Để khi nhìn vào hình ảnh của nhóm anh Soutetsu, mọi người sẽ nghĩ rằng\\n'Bọn họ không thể trở thành gia đình thì thật kỳ lạ'.」"
"2336" = "「Đúng rồi ạ! Anh vừa mới ngã gục xong mà.」"
"2413" = "「Tất nhiên rồi!\\nĐó là lời thỉnh cầu của [trong số chúng ta,7]tình đầu mà.」"
"2514" = "「Đó quả thực là trường hợp mà ý tưởng và sự nỗ lực của nhóm anh Soutetsu,\\nđược phát huy một cách rõ rệt nhất đấy.」"
"2516" = "「Chuyện đó, hiện tại tôi vẫn chưa xem xét kỹ lưỡng. Nhưng mà――\\nNghe nói các dự luật được thông qua tại Quốc hội, hầu hết đều do Nội các đệ trình.」"
"2956" = "Gia đình được chứng nhận. Một hình thái gia đình mới được pháp luật bảo vệ,\\ncó thể duy trì bằng cách nộp đơn và nhận được sự cho phép của tòa án bốn năm một lần."
"2996" = "Rồi nhanh tay, gạt \\x%l単弁;#00ffc040;van hãm đơn%l;#; về \\x%l運転位置;#00ffc040;vị trí chạy tàu%l;#;."
"3071" = "Đèn tín hiệu xuất phát hiển thị cho phép đi.\\nTôi kéo \\x%l逆転機;#00ffc040;cần đảo chiều%l;#; sang \\x%l前進フルギア;#00ffc040;cài hết số tiến%l;#;."```
