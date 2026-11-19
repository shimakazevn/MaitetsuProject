# Audit 00_Common file 11 — 共通11_経営資源.txt.toml

**Ngày kiểm toán:** 20/11/2026
**Tệp TOML:** `00_Common/共通11_経営資源.txt.toml` — md5 `2981d5f80fa4b088f19aa89c998ccca4`, BOM, CRLF, `[selections]` rỗng, **không có bản sao trùng** (kiểm tra md5 toàn bộ 227 tệp TOML).
**Nguồn CSV:** "Trang tính 3" — bộ hàng duy nhất `00_Common` (không có bẫy dual-set ở file này), 572 hàng `[script]`.
**Kết quả: 102/572 dòng sai (17,8%), 0 dòng chưa chắc chắn, 0 dòng lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo file.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| Thuật ngữ (terminology) | 59 |
| Đại từ xưng hô (pronoun) | 30 |
| Thẻ gloss %l (tag) | 2 |
| Tiếng thở/gasp (gasp) | 6 |
| Sai nghĩa (meaning) | 5 |
| **Tổng** | **102** |

**Theo loại dòng:** thoại 69/367 sai (18,8%), độc thoại 33/205 sai (16,1%).
**Theo nhân vật:** 双鉄 (Soutetsu) 42, monologue 33, ポーレット (Paulette) 14, 赤井宮司 (Akai) 8, ハチロク (Hachiroku) 4, 真闇 (Mayami) 1.

Nhóm thuật ngữ (59) chia nhỏ: 宮司→"đền chủ" 38 dòng / 39 lần xuất hiện (2293, 2302, 2401, 2503, 2522, 2530, 2578, 2620, 2672, 2782, 2783, 2814, 2886, 3002, 3253, 3307, 3313 [×2 trong một dòng], 3332, 3390, 3444, 3445, 3470, 3529, 3542, 3559, 3567, 3589, 3611, 3792, 3829, 3830, 3832, 3833, 3834, 3835, 3836, 3837, 3838 — trong đó 9 dòng viết hoa "Cung tư tế" đầu câu/xưng hô → "Đền chủ", 29 dòng viết thường → "đền chủ"; file này nặng về Akai nên 宮司 là lỗi nhiều nhất); 御一夜→Ohitoyo 12 dòng (1828, 2525, 2535, 2753, 2817, 2818, 2937, 2960, 3434, 3562, 3758, 3836); 帝鉄→Teitetsu 10 dòng (1777, 2522, 2529, 2546, 2620, 2693, 3321, 3487, 3834, 3836); 冥国→Minh Quốc 2 dòng (2628, 2901); 廣島電気鉄道→"Đường sắt điện Hiroshima" 1 dòng (2689); chú thích romaji "(kikanshi)/(untenshi)" gỡ 1 dòng (2580); 経営資源→"tài nguyên kinh doanh" 1 dòng (2546, chung dòng với Teitetsu). Nhóm đại từ (30): Soutetsu gọi Paulette "cô"→"em" 11 dòng (1845, 2239, 2250 [×2], 2253, 2299, 2380, 2423, 2445, 2997, 3003, 2308); Soutetsu tự xưng "tôi"→"anh" với Paulette 18 dòng (1797, 2238, 2250, 2380 [×2], 2466, 2479, 2572, 2583, 2596, 2599, 2645, 2711, 2987, 2995, 2998, 3003, 3023, 3031); Soutetsu tự xưng "em"→"tôi" với Mayami 4 dòng (2450, 2612, 2839, 2842 [×2]).

File này là file 00_Common "bẩn" nhất tính đến nay (17,8%, cao hơn file 05 với 12,4%) — không phải vì lệch dòng (0 dòng lệch) mà vì mật độ thuật ngữ chưa cập nhật theo các quyết định 19–20/11 rất cao: riêng 宮司 đã 38 dòng (Akai là nhân vật trung tâm của file: 41 dòng thoại + phần lớn độc thoại đều xoay quanh ông ấy), cộng với cụm đại từ Soutetsu↔Paulette 30 dòng. Toàn bộ 102 lỗi đều sửa được tại chỗ, không cần dịch lại.

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục. TOML md5 `2981d5f80fa4b088f19aa89c998ccca4`, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng trong 227 tệp.
- **CSV vs TOML:** VN khớp tuyệt đối 215 hàng; khớp sau khi gộp ký tự xuống dòng thành khoảng trắng 357 hàng; **0 khác biệt** — CSV3 là bản chuẩn cho fix list.
- **Sweep っ (gasp):** sweep CÓ liệt kê file này — 3 mục trong sweep-raw-gasp-wrong.json (1811, 3067, 3068). Cả 3 giá trị fix của sweep đã kiểm chứng đúng với JP và được áp nguyên. Quét っ hệ thống trên toàn bộ JP của file (không chỉ dựa vào sweep) không tìm thêm gasp っ trần nào bị mất; 3016 (あのっ！ → "Ưm!") là trường hợp audit tự phát hiện — tiếng ngập ngừng, không phải っ trần nên sweep không bắt. Các fix 2396/2419/3536 là theo công thức độ dài nguyên âm, không thuộc sweep.
- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng), không có VN mồ côi (orphan), không có key trùng. Chỉ 1 hàng VN == TW là key 1816 (JP/TW/VN đều là 「……」 — dấu lặng, hợp lệ, không phải chưa dịch). Các VN trùng nhau trong file chỉ là câu cảm thán ngắn lặp lại hợp lệ (「Ồ.」×4, 「Hừm.」×3, 「Vâng.」×3, 「A.」×2 — lưu ý fix 2419 phá nhóm 「Hừm.」 thành ×2 + 「Hừừm.」).
- **Kiểm tra nhiễm chéo:** đối chiếu 102 giá trị VN cũ trong fix list qua chỉ mục VN toàn dự án — 0 trùng khớp ngoài file. Toàn bộ 572 VN đều khớp đúng JP của chính dòng mình.
- **Thứ tự dòng:** key số trong file này KHÔNG phải thứ tự truyện — các cảnh xen kẽ nhau theo key (cảnh đền Akai, cảnh xưởng rượu, cảnh đi dạo đêm nằm lẫn lộn). Vì vậy địa chỉ người nghe được xác định từ nội dung dòng + mạch hội thoại (ai nói trước/sau về cùng chủ đề), KHÔNG dùng key kề nhau theo thứ tự số. Bằng chứng: 2572 (xem ghi chú trong mục đó).

## 3. Các lỗi đã sửa (102 dòng)

### 1777 — monologue — terminology

**JP:** ……ハチロクの経験した事故もまた、⏎あるいは帝鉄史に残るほど、苛烈なものであったのだろう。

**TW:** ……恐怕八六經歷的是能在帝國鐵路史上留名的慘烈事故吧。

**VN cũ:** ……Vụ tai nạn mà Hachiroku trải qua,⏎có lẽ thảm khốc đến mức lưu danh trong lịch sử Đường sắt Hoàng gia.

**Fix:** ……Vụ tai nạn mà Hachiroku trải qua,⏎có lẽ thảm khốc đến mức lưu danh trong lịch sử Teitetsu.

JP 帝鉄史. Quyết định 19/11: 帝鉄 = "Teitetsu" (bỏ "Đường sắt Hoàng gia").

### 1797 — 双鉄 — pronoun

**JP:** 「\x%l本屋;#00ffc040;[ほんおく,1]本屋%l;#;に[きゃっかしゃく,3]客貨車区。二つも専門用語を習った。⏎ハチロクを驚かすくらいの役には立とう」

**TW:** 「\x%l本屋;#00ffc040;主棟%l;#;還有客貨車區。我學到了這兩個專業術語。至少可以說出來嚇嚇八六呢」

**VN cũ:** 「\x%l本屋;#00ffc040;Tòa nhà chính%l;#; và khu toa khách toa hàng. Tôi đã học được hai thuật ngữ chuyên ngành.⏎Chắc cũng đủ để làm Hachiroku ngạc nhiên đấy.」

**Fix:** 「\x%l本屋;#00ffc040;Tòa nhà chính%l;#; và khu toa khách toa hàng. Anh đã học được hai thuật ngữ chuyên ngành.⏎Chắc cũng đủ để làm Hachiroku ngạc nhiên đấy.」

Soutetsu nói với Paulette (cảnh đi dạo đêm, chỉ có hai người; Paulette gọi Soutetsu là "anh Soutetsu" per khóa B4). Tự xưng đúng là "anh", không phải "tôi".

### 1811 — ハチロク — gasp

**JP:** 「…………っ」

**TW:** 「…………」

**VN cũ:** 「…………っ」

**Fix:** 「…………Ư」

Sweep っ-gasp: JP 「…………っ」. Áp nguyên giá trị sweep, đã kiểm chứng đúng với JP.

### 1828 — 双鉄 — terminology

**JP:** 「……なるほどな。⏎では、勤務地も御一夜ではなかった？」

**TW:** 「……原來如此。那麼，他的工作地點也不在御一夜？」

**VN cũ:** 「……Ra là vậy.⏎Vậy, nơi làm việc cũng không phải ở Ohimitera?」

**Fix:** 「……Ra là vậy.⏎Vậy, nơi làm việc cũng không phải ở Ohitoyo?」

JP 御一夜. Quyết định: 御一夜 = "Ohitoyo" (không phải Ohimitera/Ohito).

### 1845 — 双鉄 — pronoun

**JP:** 「……ポーレットは、⏎いつから鉄道を好きになったのだ？」

**TW:** 「……波萊特，你是從什麼時候開始喜歡鐵路的呢？」

**VN cũ:** 「……Paulette này,⏎cô bắt đầu thích đường sắt từ khi nào vậy?」

**Fix:** 「……Paulette này,⏎em bắt đầu thích đường sắt từ khi nào vậy?」

Soutetsu hỏi Paulette. Quyết định 19/11: Soutetsu gọi Paulette là "em" (thống nhất; "cô" 49 dòng còn lại chờ pass thống nhất).

### 2238 — 双鉄 — pronoun

**JP:** 「面白そうだな。手伝えることがあったら言ってくれ。⏎観光振興の、それも一助となるかもしれん」

**TW:** 「不是挺有趣的嗎。要是有什麼我能幫上忙的就儘管說。這或許也能為復興旅遊業提供一份助力」

**VN cũ:** 「Có vẻ thú vị đấy. Nếu có gì cần giúp thì cứ nói với tôi.⏎Có thể nó cũng sẽ góp phần vào việc chấn hưng du lịch đấy.」

**Fix:** 「Có vẻ thú vị đấy. Nếu có gì cần giúp thì cứ nói với anh.⏎Có thể nó cũng sẽ góp phần vào việc chấn hưng du lịch đấy.」

Soutetsu nói với Paulette (kế hoạch cho mèo trưởng ga của Paulette; Paulette đáp 2459 "lúc đó sẽ nhờ anh nhé"). Tự xưng "anh".

### 2239 — 双鉄 — pronoun

**JP:** 「構わん。というか、急ぎなら」

**TW:** 「不用在意。你既然有急事——」

**VN cũ:** 「Không sao. Nếu cô đang vội thì――」

**Fix:** 「Không sao. Nếu em đang vội thì――」

Soutetsu nói với Paulette (đáp lại 2435 Paulette vội đến gặp anh). "cô" → "em".

### 2250 — 双鉄 — pronoun

**JP:** 「いや、動けるのならば、今これ以上の話は無い。⏎腰を痛めでもしているのではないかと心配したのだが」

**TW:** 「不，你要是能自己站起來，我就沒什麼要說的了。我還以為你扭到腰了呢」

**VN cũ:** 「Không, nếu cô cử động được thì bây giờ không còn chuyện gì để nói nữa.⏎Tôi đã lo lắng không biết có phải cô bị đau lưng không.」

**Fix:** 「Không, nếu em cử động được thì bây giờ không còn chuyện gì để nói nữa.⏎Anh đã lo lắng không biết có phải em bị đau lưng không.」

Soutetsu nói với Paulette (hỏi về lưng cô ấy; Paulette đáp 2749). "cô" → "em" (2 chỗ), "tôi" → "anh".

### 2253 — 双鉄 — pronoun

**JP:** 「いや、今の話だけでも十分参考になった。⏎ありがとう」

**TW:** 「不，剛才的話十分有參考價值。謝謝你」

**VN cũ:** 「Không, chỉ những chuyện vừa rồi cũng đủ để tham khảo rồi.⏎Cảm ơn cô.」

**Fix:** 「Không, chỉ những chuyện vừa rồi cũng đủ để tham khảo rồi.⏎Cảm ơn em.」

Soutetsu cảm ơn Paulette (báo cáo buổi sáng ở cửa hàng đường sắt). "cô" → "em".

### 2293 — 双鉄 — terminology

**JP:** 「の、つもりらしかったがな。⏎赤井宮司は、切り崩されずになんとか追い返したらしい」

**TW:** 「似乎她是有這個打算。不過好像赤井先生總算沒有被她說動，把她趕了回去」

**VN cũ:** 「Có vẻ là định như vậy.⏎Nhưng cung tư tế Akai không bị lung lạc mà đã tìm cách đuổi về được.」

**Fix:** 「Có vẻ là định như vậy.⏎Nhưng đền chủ Akai không bị lung lạc mà đã tìm cách đuổi về được.」

JP 赤井宮司. Quyết định 19/11: 宮司 = "đền chủ" (thống nhất; "cung tư tế" là dịch cũ).

### 2299 — 双鉄 — pronoun

**JP:** 「この前聞いた、駅長犬のか？」

**TW:** 「你之前說過的，讓它當站長犬那件事？」

**VN cũ:** 「Vụ chó trưởng ga mà cô nói hôm trước à?」

**Fix:** 「Vụ chó trưởng ga mà em nói hôm trước à?」

Soutetsu hỏi Paulette (kế hoạch mèo trưởng ga do Paulette kể). "cô" → "em".

### 2302 — ポーレット — terminology

**JP:** 「双鉄くんも知ってたんですね。⏎けど、赤井宮司さんは工場勤務じゃなかったそうですよ」

**TW:** 「你也知道了啊。不過，赤井宮司當年似乎不是在工廠工作的」

**VN cũ:** 「Anh Soutetsu cũng biết nhỉ.⏎Nhưng nghe nói cung tư tế Akai không làm việc ở nhà máy đâu.」

**Fix:** 「Anh Soutetsu cũng biết nhỉ.⏎Nhưng nghe nói đền chủ Akai không làm việc ở nhà máy đâu.」

JP 赤井宮司さん. 宮司 = "đền chủ".

### 2308 — 双鉄 — pronoun

**JP:** 「宝生稀咲という娘を知っているか？」

**TW:** 「你認識寶生稀咲嗎？」

**VN cũ:** 「Cô có biết cô gái tên Houshou Kisaki không?」

**Fix:** 「Em có biết cô gái tên Houshou Kisaki không?」

Soutetsu hỏi Paulette (báo cáo buổi sáng; Paulette là người biết Kisaki). "cô" → "em".

### 2380 — 双鉄 — pronoun

**JP:** 「僕の経営資源を確認しても構わんか？」

**TW:** 「可以陪我去看看我的經營資源嗎？」

**VN cũ:** 「Cô có phiền cùng tôi đi xác nhận tài nguyên kinh doanh của tôi không?」

**Fix:** 「Em có phiền cùng anh đi xác nhận tài nguyên kinh doanh của anh không?」

Soutetsu mời Paulette cùng đi (cảnh đi dạo đêm, chỉ hai người). "cô" → "em", "tôi" → "anh" (2 chỗ).

### 2396 — 赤井宮司 — gasp

**JP:** 「ふぅ」

**TW:** 「呼」

**VN cũ:** 「Phù」

**Fix:** 「Phùù」

Akai thở dài: JP ふぅ. Công thức độ dài nguyên âm (VN = 1 + số う/ぅ trong JP): ふぅ có 1 う → "Phùù" (2 u). Bản cũ "Phù" thiếu 1 nguyên âm.

### 2401 — 赤井宮司 — terminology

**JP:** 「と。自己紹介もせずに昔話を失礼しました。⏎私はこの[やしろ]社の宮司、赤井[きよはる,1]清春です」

**TW:** 「哎呀。瞧我還沒自我介紹，就開始回憶往昔了。我是這所神社的宮司，名叫赤井清春」

**VN cũ:** 「Ái chà. Thật thất lễ khi chưa tự giới thiệu mà đã kể chuyện xưa.⏎Tôi là cung tư tế của đền này, Akai Kiyoharu.」

**Fix:** 「Ái chà. Thật thất lễ khi chưa tự giới thiệu mà đã kể chuyện xưa.⏎Tôi là đền chủ của đền này, Akai Kiyoharu.」

JP 宮司. 宮司 = "đền chủ". (Akai tự giới thiệu; "tôi" ở đây là Akai, giữ nguyên.)

### 2404 — 真闇 — tag

**JP:** 「あら、双ちゃんにハチロクちゃん。⏎[じょうぞうぐら,2]醸造蔵に来るとは、めずらしかとねぇ」

**TW:** 「哎呀，這不是小雙和八六嗎。你們竟然會來酒窖，這可真是少見咧」

**VN cũ:** 「Ây da, bé Sou và bé Hachiroku.⏎Đến \x%l醸造蔵;#00ffc040;nhà xưởng ủ rượu%l;#; thế này, hiếm thấy ghê nha.」

**Fix:** 「Ây da, bé Sou và bé Hachiroku.⏎Đến nhà xưởng ủ rượu thế này, hiếm thấy ghê nha.」

JP chỉ có ruby [じょうぞうぐら,2] trên 醸造蔵, KHÔNG có thẻ %l (đã kiểm chứng comment # JP trong TOML). Thẻ \x%l醸造蔵;#00ffc040;...%l;#; là do bản Việt tự thêm — gỡ, giữ chữ thường "nhà xưởng ủ rượu". Kiểu bịa của Gemini: thêm tag/gloss JP không có.

### 2419 — 双鉄 — gasp

**JP:** 「ふぅむ」

**TW:** 「唔」

**VN cũ:** 「Hừm.」

**Fix:** 「Hừừm.」

Soutetsu trầm ngâm: JP ふぅむ. Công thức độ dài nguyên âm: 1 う → "Hừừm" (2 ừ). Tiền lệ file 06 key 2074 (ふだむ→"Hừừm."), giữ dấu chấm như bản cũ.

### 2423 — 双鉄 — pronoun

**JP:** 「あ、ああ。そうだな。早く休んだ方がいい」

**TW:** 「啊、嗯。是啊。還是早點休息為好」

**VN cũ:** 「A, à. Đúng vậy nhỉ. Cô nên nghỉ ngơi sớm đi.」

**Fix:** 「A, à. Đúng vậy nhỉ. Em nên nghỉ ngơi sớm đi.」

Soutetsu nói với Paulette (cô ấy ho, khản giọng sau buổi họp hội đồng). "cô" → "em".

### 2445 — 双鉄 — pronoun

**JP:** 「これを飲むといい」

**TW:** 「喝吧」

**VN cũ:** 「Cô uống cái này đi.」

**Fix:** 「Em uống cái này đi.」

Soutetsu đưa đồ uống yuzu mật ong cho Paulette. "cô" → "em".

### 2450 — 双鉄 — pronoun

**JP:** 「うむ。そのとおりだ。お願いしたい」

**TW:** 「嗯。是的。請告訴我」

**VN cũ:** 「Ừm. Đúng là vậy. Em muốn nhờ chị.」

**Fix:** 「Ừm. Đúng là vậy. Tôi muốn nhờ chị.」

Soutetsu nói với Mayami (chị Mayami). Quyết định #18: Soutetsu với Mayami = "tôi" (không có ngoại lệ); "em" là thói quen cũ của dịch giả mang từ cảnh Paulette sang. (2450 không phải cảnh Paulette.)

### 2466 — 双鉄 — pronoun

**JP:** 「僕は携帯を持たんからな」

**TW:** 「因為我不帶手機的」

**VN cũ:** 「Tôi không mang điện thoại mà.」

**Fix:** 「Anh không mang điện thoại mà.」

Soutetsu nói với Paulette (cô ấy hỏi sao không nghe máy lúc 7 giờ). Tự xưng "anh".

### 2479 — 双鉄 — pronoun

**JP:** 「女性機関士か？　珍しかったとハチロクに聞いたが」

**TW:** 「女性司機？八六說過女性司機很少見呢」

**VN cũ:** 「Nữ lái tàu sao? Tôi nghe Hachiroku nói là hiếm lắm mà.」

**Fix:** 「Nữ lái tàu sao? Anh nghe Hachiroku nói là hiếm lắm mà.」

Soutetsu nói với Paulette (chuyện bà nội Katsuko từng làm lái tàu). Tự xưng "anh".

### 2503 — ハチロク — terminology

**JP:** 「かしこまりました、赤井宮司」

**TW:** 「好的，請讓我稱呼您為赤井宮司」

**VN cũ:** 「Tôi đã hiểu, cung tư tế Akai.」

**Fix:** 「Tôi đã hiểu, đền chủ Akai.」

JP 赤井宮司. Hachiroku xưng hô với Akai. 宮司 = "đền chủ".

### 2522 — ポーレット — terminology

**JP:** 「市の職員さんに、宮司さんの叔母さんがいるんですけど。⏎わざわざ帝鉄に勤めに出たのも、おなじ理由らしいです」

**TW:** 「宮司的叔母是市內的公務員。但他當年卻刻意選擇就職於帝國鐵路，似乎也是因為這個」

**VN cũ:** 「Trong số các nhân viên tòa thị chính, có dì của cung tư tế.⏎Nghe nói việc ngài ấy cất công đi làm ở Đường sắt Hoàng gia cũng vì lý do tương tự.」

**Fix:** 「Trong số các nhân viên tòa thị chính, có dì của đền chủ.⏎Nghe nói việc ngài ấy cất công đi làm ở Teitetsu cũng vì lý do tương tự.」

JP 宮司さん + 帝鉄. Hai fix trong một dòng: 宮司 = "đền chủ"; 帝鉄 = "Teitetsu".

### 2525 — 双鉄 — terminology

**JP:** 「8620修復自体を、御一夜全体の経営資源として共有する。⏎その活用で利益を産めると、皆に考えてもらえるように」

**TW:** 「將８６２０修復計劃本身作為御一夜整體的經營資源和大家共享。要讓大家認為利用這項資源能夠帶來利益」

**VN cũ:** 「Chia sẻ bản thân việc phục hồi 8620 như một tài nguyên kinh doanh của toàn bộ Ohimitera.⏎Để mọi người nghĩ rằng, có thể sinh ra lợi nhuận từ việc tận dụng nó.」

**Fix:** 「Chia sẻ bản thân việc phục hồi 8620 như một tài nguyên kinh doanh của toàn bộ Ohitoyo.⏎Để mọi người nghĩ rằng, có thể sinh ra lợi nhuận từ việc tận dụng nó.」

JP 御一夜. 御一夜 = "Ohitoyo".

### 2529 — 双鉄 — terminology

**JP:** 「粉蔵……蓑笠老人の話にも出てきたな。⏎帝鉄の工場があったというところで間違いないか？」

**TW:** 「小倉……蓑笠老人也提起過。那裡似乎曾經有帝國鐵路的工廠？」

**VN cũ:** 「Kokura……Cũng từng được nhắc đến trong câu chuyện của ông lão Minokasa.⏎Chắc chắn là nơi từng có nhà máy của Đường sắt Hoàng gia đúng không?」

**Fix:** 「Kokura……Cũng từng được nhắc đến trong câu chuyện của ông lão Minokasa.⏎Chắc chắn là nơi từng có nhà máy của Teitetsu đúng không?」

JP 帝鉄の工場. 帝鉄 = "Teitetsu".

### 2530 — 双鉄 — terminology

**JP:** 「粉蔵の機関区にも、[ハチロクニイマル,3]8620形は配備されていた。ゆえ、⏎8620形レイルロオドの姿を赤井宮司は見知っていた」

**TW:** 「小倉的機務段也曾配備了８６２０型。所以您才知道８６２０型的鐵路人偶是什麼樣子」

**VN cũ:** 「Khu đầu máy Kokura cũng được trang bị dòng 8620. Do đó,⏎cung tư tế Akai đã biết đến hình dáng của Railord dòng 8620.」

**Fix:** 「Khu đầu máy Kokura cũng được trang bị dòng 8620. Do đó,⏎đền chủ Akai đã biết đến hình dáng của Railord dòng 8620.」

JP 赤井宮司. 宮司 = "đền chủ". ("Railord" 1 chữ l đã đúng, giữ nguyên.)

### 2535 — 双鉄 — terminology

**JP:** 「名付けるなら、そう――⏎『蒸気焼酎・おひとよしのハチロク』でどうだろう」

**TW:** 「就取名叫——“蒸汽燒酒·御一夜八六”如何」

**VN cũ:** 「Nếu đặt tên, thì sao nhỉ――⏎『Shochu Hơi Nước・Hachiroku Ohimitera』 thì thế nào.」

**Fix:** 「Nếu đặt tên, thì sao nhỉ――⏎『Shochu Hơi Nước・Hachiroku Ohitoyo』 thì thế nào.」

JP 御一夜 trong tên rượu đề xuất. 御一夜 = "Ohitoyo".

### 2546 — 赤井宮司 — terminology

**JP:** 「最晩年の帝鉄は、経営資源の全てを電化に投資し、⏎しかしリターンを得ることが出来ず、滅んだのです」

**TW:** 「帝國鐵路最後孤注一擲將全部經營資源押在電動機車上，然而卻沒能逆轉局勢，最終倒閉了」

**VN cũ:** 「Đường sắt Hoàng gia những năm cuối đời đã đầu tư toàn bộ nguồn lực kinh doanh vào việc điện khí hóa,⏎nhưng không thu được lợi nhuận, và đã sụp đổ.」

**Fix:** 「Teitetsu những năm cuối đời đã đầu tư toàn bộ tài nguyên kinh doanh vào việc điện khí hóa,⏎nhưng không thu được lợi nhuận, và đã sụp đổ.」

JP 帝鉄 + 経営資源. Hai fix: 帝鉄 = "Teitetsu"; 経営資源 = "tài nguyên kinh doanh" (thuật ngữ chủ đề của file, đa số trong file 3 lần ở 2267/2881/3028; "nguồn lực kinh doanh" chỉ 1 lần này).

### 2572 — 双鉄 — pronoun

**JP:** 「うまくいくだろうな、それは。⏎僕の知る限り、日々姫は動物にたいそう好かれる」

**TW:** 「應該沒什麼問題吧。據我所知，日日姬很受動物歡迎」

**VN cũ:** 「Chắc sẽ suôn sẻ thôi.⏎Theo như tôi biết, Hibiki rất được động vật yêu quý.」

**Fix:** 「Chắc sẽ suôn sẻ thôi.⏎Theo như anh biết, Hibiki rất được động vật yêu quý.」

Soutetsu trấn an Paulette về kế hoạch cho mèo ăn làm quen (kế hoạch của Paulette với Reina; Paulette nói trước 2887 và tiếp sau 2805; Hachiroku chỉ hỏi xen 2247). Tự xưng "anh". Lưu ý: địa chỉ suy từ mạch truyện, không chắc tuyệt đối như các dòng đi dạo đêm — nhưng kế hoạch là của Paulette nên "anh" đứng vững.

### 2578 — ポーレット — terminology

**JP:** 「さすがにそこまでは……わたしも、⏎宮司さんご本人と踏み込んだお話はしませんし」

**TW:** 「我不是很清楚……畢竟我也沒怎麼和宮司聊過」

**VN cũ:** 「Đến mức đó thì……tôi cũng,⏎chưa nói chuyện sâu với bản thân cung tư tế.」

**Fix:** 「Đến mức đó thì……tôi cũng,⏎chưa nói chuyện sâu với bản thân đền chủ.」

JP 宮司さん. Paulette nói về Akai. 宮司 = "đền chủ".

### 2580 — 赤井宮司 — terminology

**JP:** 「機関士も経験しましたが、最後は運転士でした。⏎[こくら,1]粉蔵の試験区間で、\x%l電車;#00ffc040;電車%l;#;運転を」

**TW:** 「我也做過司機，不過最後還是做駕駛員了。負責在小倉的測試路段駕駛電動機車」

**VN cũ:** 「Tôi cũng từng trải qua vị trí lái tàu (kikanshi), nhưng cuối cùng thì tôi là người điều khiển tàu (untenshi).⏎Ở đoạn đường thử nghiệm Kokura, tôi đã điều khiển \x%l電車;#00ffc040;tàu điện%l;#;.」

**Fix:** 「Tôi cũng từng làm lái tàu, nhưng cuối cùng thì làm nhân viên cơ vụ.⏎Ở đoạn đường thử nghiệm Kokura, tôi đã điều khiển \x%l電車;#00ffc040;tàu điện%l;#;.」

Akai kể nghề nghiệp cũ. JP 機関士/運転士, bản Việt thêm chú thích romaji "(kikanshi)"/"(untenshi)" không có trong JP — gỡ. Dùng thuật ngữ đã quyết: 機関士 = "lái tàu", 運転士 = "nhân viên cơ vụ". Thẻ %l của 電車 là của JP, giữ nguyên.

### 2582 — ポーレット — meaning

**JP:** 「わたしだって[ヒノモト,2]日ノ本人ですよ？⏎育ちは、結構長い間フランクでしたけど」

**TW:** 「我也是日本人呀？雖然小時候在法國待了很長一段時間」

**VN cũ:** 「Tôi cũng là người Hinomoto mà?⏎Dù thời gian lớn lên ở Frank (Pháp) khá dài.」

**Fix:** 「Tôi cũng là người Hinomoto mà?⏎Dù thời gian lớn lên ở Frank khá dài.」

JP フランク (Frank) không có chú thích nào. "(Pháp)" là bản Việt tự thêm giải thích — gỡ. Kiểu bịa của Gemini: thêm chú thích trong ngoặc không có nguồn JP. (Cùng lỗi ở 2628 "(Mỹ)".)

### 2583 — 双鉄 — pronoun

**JP:** 「前にも少し見たことがあるが、見事なものだな」

**TW:** 「我以前也見過，這表做工真好啊」

**VN cũ:** 「Trước đây tôi cũng từng nhìn thấy một chút rồi, thật là một món đồ tuyệt đẹp.」

**Fix:** 「Trước đây anh cũng từng nhìn thấy một chút rồi, thật là một món đồ tuyệt đẹp.」

Soutetsu nói với Paulette (ngắm mặt dây chuyền đồng hồ bỏ túi của cô ấy). Tự xưng "anh".

### 2596 — 双鉄 — pronoun

**JP:** 「僕の、いったい何がさすがだ？」

**TW:** 「我做了什麼嗎？」

**VN cũ:** 「Tôi thì có gì mà không hổ danh?」

**Fix:** 「Anh thì có gì mà không hổ danh?」

Soutetsu đáp lại lời khen của Paulette 2355 ("Quả không hổ danh là anh Soutetsu"). Tự xưng "anh".

### 2599 — 双鉄 — pronoun

**JP:** 「さっき、電話をしたのだが」

**TW:** 「我剛才給你打電話了」

**VN cũ:** 「Vừa nãy, tôi có gọi điện thoại.」

**Fix:** 「Vừa nãy, anh có gọi điện thoại.」

Soutetsu nói với Paulette (cảnh gặp nhau buổi tối; Paulette hỏi 2298 về cuộc gọi 7 giờ). Tự xưng "anh".

### 2612 — 双鉄 — pronoun

**JP:** 「今、ポーレットたちと計画していることがある」

**TW:** 「我正在和波萊特他們計劃一件事」

**VN cũ:** 「Hiện tại, em đang lên kế hoạch cho một việc cùng với nhóm Paulette.」

**Fix:** 「Hiện tại, tôi đang lên kế hoạch cho một việc cùng với nhóm Paulette.」

Soutetsu nói với Mayami ("Hiện tại, em đang..." sai; Mayami là chị lớn, Soutetsu = "tôi" per quyết định #18).

### 2620 — 双鉄 — terminology

**JP:** 「旧帝鉄にお勤めだったと人に聞きましたが――⏎宮司は、機関士でいらっしゃったのですか？」

**TW:** 「我聽聞您曾就職於前帝國鐵路，您曾經是司機嗎？」

**VN cũ:** 「Tôi nghe người ta nói ngài từng làm việc ở Đường sắt Hoàng gia cũ――⏎Cung tư tế, ngài từng là lái tàu sao?」

**Fix:** 「Tôi nghe người ta nói ngài từng làm việc ở Teitetsu cũ――⏎Đền chủ, ngài từng là lái tàu sao?」

JP 旧帝鉄 + 宮司. Hai fix: 帝鉄 = "Teitetsu"; 宮司 = "đền chủ" (đầu dòng nên viết hoa "Đền chủ" — xưng hô trực tiếp với Akai).

### 2624 — ポーレット — meaning

**JP:** 「わたし、⏎あまり役に立つお話できなかった気もしますけど」

**TW:** 「我說的這些可能沒多大用處」

**VN cũ:** 「Tôi có cảm giác,⏎mình chưa kể được chuyện gì có ích cho lắm.」

**Fix:** 「Tôi có cảm giác,⏎tôi chưa kể được chuyện gì có ích cho lắm.」

Paulette tự xưng lẫn lộn trong một dòng: "Tôi... mình" (JP chỉ có わたし). Thống nhất về "tôi" (cách Paulette tự xưng trong cả file).

### 2628 — ポーレット — terminology

**JP:** 「国産じゃないんですよ。⏎[めいこく,1]冥国製です。[ウォールサム,7]WALLTHAM」

**TW:** 「我這塊表不是國貨，是美國廠商的。ＷＡＬＬＴＨＡＭ」

**VN cũ:** 「Không phải hàng nội địa đâu.⏎Là hàng sản xuất tại Meikoku (Mỹ) đấy. WALLTHAM.」

**Fix:** 「Không phải hàng nội địa đâu.⏎Là hàng sản xuất tại Minh Quốc đấy. WALLTHAM.」

JP [めいこく,1]冥国製. Quyết định: 冥国 = "Minh Quốc" (furigana めいこく không lấn át chữ chính 冥国); "(Mỹ)" là bản Việt tự thêm giải thích — gỡ.

### 2645 — 双鉄 — pronoun

**JP:** 「僕と？」

**TW:** 「找我？」

**VN cũ:** 「Gặp tôi?」

**Fix:** 「Gặp anh?」

Soutetsu hỏi lại Paulette 2435 ("xem có gặp được anh Soutetsu không"). Tự xưng "anh".

### 2672 — 赤井宮司 — terminology

**JP:** 「元・運転士ですよ。今は、ただの宮司です」

**TW:** 「是原駕駛員。現在只是一介宮司」

**VN cũ:** 「Là cựu lái tàu thôi. Bây giờ, tôi chỉ là một cung tư tế.」

**Fix:** 「Là cựu lái tàu thôi. Bây giờ, tôi chỉ là một đền chủ.」

JP 宮司. Akai tự giới thiệu. 宮司 = "đền chủ".

### 2689 — 赤井宮司 — terminology

**JP:** 「[ヒロデン,5]廣島電気鉄道のことですか。⏎なるほど――そう考えれば、我々も多少は報われますか」

**TW:** 「是指廣島電鐵嗎。原來如此——這麼想的話，我們的努力也並非徒勞」

**VN cũ:** 「Ý cô là Đường sắt Điện lực Hiroshima sao.⏎Ra là vậy――nếu nghĩ như thế, thì chúng tôi cũng được đền đáp phần nào nhỉ.」

**Fix:** 「Ý cô là Đường sắt điện Hiroshima sao.⏎Ra là vậy――nếu nghĩ như thế, thì chúng tôi cũng được đền đáp phần nào nhỉ.」

JP [ヒロデン,5]廣島電気鉄道 = Hiroshima Electric Railway. "Đường sắt Điện lực" sai nghĩa (電気鉄道 = đường sắt điện, không phải công ty điện lực).

### 2693 — 赤井宮司 — terminology

**JP:** 「ええ。[ホッカイドウ,2]北開道、[シコク,1]四國、[キュウシュウ,1]九洲――[ヒノモト,2]日ノ本全土で。⏎帝鉄は\x%l電車;#00ffc040;電車%l;#;こそを復活の切り札にと、必死でした」

**TW:** 「是的。北海道、四國、九州——乃至日本全土都有。帝國鐵路認為電動機車才是復活鐵路的關鍵」

**VN cũ:** 「Vâng. Hokkaido, Shikoku, Kyushu――Trên toàn cõi Hinomoto.⏎Đường sắt Hoàng gia đã tuyệt vọng coi \x%l電車;#00ffc040;tàu điện%l;#; chính là con bài tẩy để phục sinh.」

**Fix:** 「Vâng. Hokkaido, Shikoku, Kyushu――Trên toàn cõi Hinomoto.⏎Teitetsu đã tuyệt vọng coi \x%l電車;#00ffc040;tàu điện%l;#; chính là con bài tẩy để phục sinh.」

JP 帝鉄. 帝鉄 = "Teitetsu". (Thẻ %l của 電車 là của JP, giữ nguyên.)

### 2711 — 双鉄 — pronoun

**JP:** 「その字か。なるほど、理解できた」

**TW:** 「是這個意思啊。原來如此，我明白了」

**VN cũ:** 「Là chữ đó sao. Ra là vậy, tôi hiểu rồi.」

**Fix:** 「Là chữ đó sao. Ra là vậy, anh hiểu rồi.」

Soutetsu nói với Paulette (cô ấy giải thích chữ trên mặt dây chuyền). Tự xưng "anh".

### 2753 — ポーレット — terminology

**JP:** 「“御一夜温泉駅史”によると、この機関庫は、⏎[めいじ,1]明智四十一年、\x%l本屋;#00ffc040;[ほんおく,1]本屋%l;#;とともに作られたそうです」

**TW:** 「根據《御一夜溫泉站史》記載，這個機車庫是明治四十一年和\x%l本屋;#00ffc040;主棟%l;#;一起建起來的」

**VN cũ:** 「Theo “Lịch sử ga suối nước nóng Ohimitera”, xưởng đầu máy này,⏎được xây dựng cùng với \x%l本屋;#00ffc040;tòa nhà chính%l;#; vào năm Minh Trí thứ 41 đấy.」

**Fix:** 「Theo “Lịch sử ga suối nước nóng Ohitoyo”, xưởng đầu máy này,⏎được xây dựng cùng với \x%l本屋;#00ffc040;tòa nhà chính%l;#; vào năm Minh Trí thứ 41 đấy.」

JP “御一夜温泉駅史”. 御一夜 = "Ohitoyo". (Thẻ %l của 本屋 là của JP, giữ nguyên.)

### 2782 — ポーレット — terminology

**JP:** 「赤井宮司さんに自力でたどり着いたことですよ。⏎もう少しあとにご紹介しよう、って思ってたんですけど」

**TW:** 「沒想到你自己去找赤井宮司了。我原本還想過一段時間再介紹給你的」

**VN cũ:** 「Là việc anh tự mình tìm đến được chỗ cung tư tế Akai đấy.⏎Tôi vốn định để một thời gian nữa mới giới thiệu cơ.」

**Fix:** 「Là việc anh tự mình tìm đến được chỗ đền chủ Akai đấy.⏎Tôi vốn định để một thời gian nữa mới giới thiệu cơ.」

JP 赤井宮司さん. Paulette nói về Akai. 宮司 = "đền chủ".

### 2783 — ハチロク — terminology

**JP:** 「随分と現実的な方でしたね、赤井宮司は」

**TW:** 「沒想到您還是一位挺現實的人呢」

**VN cũ:** 「Ngài ấy là một người khá thực tế nhỉ, cung tư tế Akai ấy.」

**Fix:** 「Ngài ấy là một người khá thực tế nhỉ, đền chủ Akai ấy.」

JP 赤井宮司. Hachiroku nói về Akai. 宮司 = "đền chủ".

### 2814 — ポーレット — terminology

**JP:** 「お忙しいんですね、宮司さんも」

**TW:** 「畢竟神社的宮司很忙呢」

**VN cũ:** 「Cung tư tế cũng bận rộn nhỉ.」

**Fix:** 「Đền chủ cũng bận rộn nhỉ.」

JP 宮司さん. Paulette nói về Akai (đầu câu nên viết hoa "Đền chủ"). 宮司 = "đền chủ".

### 2817 — ポーレット — terminology

**JP:** 「もちろんです。銀行さん――⏎[くまもと,1]隈元銀行御一夜支店の支店長さんで、つまり……」

**TW:** 「當然了。她是銀行——隈元銀行御一夜支行的支行長，也就是說……」

**VN cũ:** 「Tất nhiên rồi. Ngân hàng――⏎Là giám đốc chi nhánh Ohimitera của Ngân hàng Kumamoto, nghĩa là...」

**Fix:** 「Tất nhiên rồi. Ngân hàng――⏎Là giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto, nghĩa là...」

JP 御一夜支店. 御一夜 = "Ohitoyo".

### 2818 — 双鉄 — terminology

**JP:** 「それはもちろん、8620の復活と走行をもってです。⏎そうするために必要な作業を、できるだけ御一夜でと」

**TW:** 「當然是修復並開動８６２０。而且最好所有工作都在御一夜完成」

**VN cũ:** 「Tất nhiên là bằng sự phục sinh và lăn bánh của 8620.⏎Để làm được điều đó, tôi muốn thực hiện các công việc cần thiết ở Ohimitera càng nhiều càng tốt.」

**Fix:** 「Tất nhiên là bằng sự phục sinh và lăn bánh của 8620.⏎Để làm được điều đó, tôi muốn thực hiện các công việc cần thiết ở Ohitoyo càng nhiều càng tốt.」

JP 御一夜で. Soutetsu nói với Akai. 御一夜 = "Ohitoyo".

### 2839 — 双鉄 — pronoun

**JP:** 「真闇姉、使われていない石炭ボイラが、⏎まだこの家にはあると聞いたと記憶しているが」

**TW:** 「真闇姐，我記得家裡還有不用的燒煤鍋爐啊」

**VN cũ:** 「Chị Mayami, em nhớ chị từng nói là trong nhà này⏎vẫn còn một cái lò hơi than không dùng đến.」

**Fix:** 「Chị Mayami, tôi nhớ chị từng nói là trong nhà này⏎vẫn còn một cái lò hơi than không dùng đến.」

Soutetsu hỏi Mayami. "em" sai với Mayami (quyết định #18: Soutetsu với Mayami = "tôi").

### 2842 — 双鉄 — pronoun

**JP:** 「その上で真闇姉、ひとつ、教えて欲しいことがある」

**TW:** 「真闇姐，還有一件事」

**VN cũ:** 「Dựa trên điều đó, chị Mayami, có một chuyện em muốn chị chỉ cho em.」

**Fix:** 「Dựa trên điều đó, chị Mayami, có một chuyện tôi muốn chị chỉ cho tôi.」

Soutetsu hỏi Mayami. "em" → "tôi" (2 chỗ, quyết định #18).

### 2886 — 双鉄 — terminology

**JP:** 「ともかく、その稀咲が訪ねていったそうなのだ。⏎僕らが訪問する前に、赤井宮司のところへと」

**TW:** 「總之，聽說那位稀咲去拜訪了赤井宮司。在我們去之前」

**VN cũ:** 「Dù sao thì, nghe nói Kisaki đó đã đến thăm.⏎Trước khi chúng tôi đến thăm chỗ cung tư tế Akai.」

**Fix:** 「Dù sao thì, nghe nói Kisaki đó đã đến thăm.⏎Trước khi chúng tôi đến thăm chỗ đền chủ Akai.」

JP 赤井宮司のところ. Soutetsu báo cáo với Paulette. 宮司 = "đền chủ".

### 2901 — ポーレット — terminology

**JP:** 「冥国の大統領が来た時、⏎移動に、お召し列車を使ってもらったそうなんです」

**TW:** 「聽說美國總統來訪時，坐過一輛御召列車」

**VN cũ:** 「Khi tổng thống Meikoku đến thăm,⏎nghe nói họ đã dùng tàu ngự dụng để ông ấy di chuyển.」

**Fix:** 「Khi tổng thống Minh Quốc đến thăm,⏎nghe nói họ đã dùng tàu ngự dụng để ông ấy di chuyển.」

JP 冥国. Paulette kể chuyện bà nội. 冥国 = "Minh Quốc" (chữ chính; furigana めいこく không lấn át).

### 2937 — 赤井宮司 — terminology

**JP:** 「御一夜に、⏎人と技術とを集める、というお考えでしょうか」

**TW:** 「讓技術和人才集中於御一夜，是嗎」

**VN cũ:** 「Ý cậu là,⏎tập trung con người và công nghệ ở Ohimitera sao.」

**Fix:** 「Ý cậu là,⏎tập trung con người và công nghệ ở Ohitoyo sao.」

JP 御一夜に. Akai hỏi Soutetsu. 御一夜 = "Ohitoyo".

### 2960 — ポーレット — terminology

**JP:** 「赤井阿蘇神社は、御一夜最大最古の神社で、⏎当然、[うじこ,1]氏子さんもすごく多くて、影響力があるんです」

**TW:** 「赤井阿蘇神社是御一夜最大、最古老的神社，自然信徒眾多，擁有很大的影響力」

**VN cũ:** 「Đền Akai Aso là ngôi đền lớn nhất và lâu đời nhất ở Ohimitera,⏎tất nhiên, số lượng giáo dân cũng rất đông, nên có sức ảnh hưởng lớn.」

**Fix:** 「Đền Akai Aso là ngôi đền lớn nhất và lâu đời nhất ở Ohitoyo,⏎tất nhiên, số lượng giáo dân cũng rất đông, nên có sức ảnh hưởng lớn.」

JP 御一夜最大最古. Paulette giới thiệu đền Akai Aso. 御一夜 = "Ohitoyo".

### 2987 — 双鉄 — pronoun

**JP:** 「そうだな、[ヒノモト,2]日ノ本人の僕にも少し難しい」

**TW:** 「這個讀音對我這個日本人來說也有點繞」

**VN cũ:** 「Đúng vậy, đối với một người Hinomoto như tôi cũng hơi khó.」

**Fix:** 「Đúng vậy, đối với một người Hinomoto như anh cũng hơi khó.」

Soutetsu nói với Paulette (cô ấy kể về gốc gác Frank/Hinomoto). Tự xưng "anh".

### 2995 — 双鉄 — pronoun

**JP:** 「そうか。ならば安心した」

**TW:** 「這樣啊。那我就放心了」

**VN cũ:** 「Vậy sao. Nếu thế thì tôi yên tâm rồi.」

**Fix:** 「Vậy sao. Nếu thế thì anh yên tâm rồi.」

Soutetsu nói với Paulette (cô ấy nói sẽ chuẩn bị cho mèo). Tự xưng "anh".

### 2997 — 双鉄 — pronoun

**JP:** 「ああ、喉が疲れているのか。⏎ちょっと待て」

**TW:** 「這樣啊，你嗓子一定累了吧。稍等」

**VN cũ:** 「À, cổ họng cô bị mệt sao.⏎Đợi một chút.」

**Fix:** 「À, cổ họng em bị mệt sao.⏎Đợi một chút.」

Soutetsu nói với Paulette (cô ấy ho). "cô" → "em".

### 2998 — 双鉄 — pronoun

**JP:** 「そうか、ならば、夜にでも電話で報告しよう」

**TW:** 「這樣啊，那我晚上再打電話報告」

**VN cũ:** 「Vậy sao, nếu thế, tối nay tôi sẽ gọi điện thoại báo cáo.」

**Fix:** 「Vậy sao, nếu thế, tối nay anh sẽ gọi điện thoại báo cáo.」

Soutetsu nói với Paulette (hẹn báo cáo buổi tối). Tự xưng "anh".

### 3002 — ポーレット — terminology

**JP:** 「それじゃあ、⏎赤井宮司さんにも会ってきたんですか」

**TW:** 「這麼說，你們昨天還去見了赤井宮司啊」

**VN cũ:** 「Vậy ra,⏎hai người cũng đã đi gặp cung tư tế Akai rồi sao.」

**Fix:** 「Vậy ra,⏎hai người cũng đã đi gặp đền chủ Akai rồi sao.」

JP 赤井宮司さん. Paulette hỏi Soutetsu+Hachiroku. 宮司 = "đền chủ".

### 3003 — 双鉄 — pronoun

**JP:** 「そのくらいはおごらせてくれ。⏎それが嫌なら、授業料ということで処理してくれ」

**TW:** 「這點小錢就讓我請了吧。或者你可以當是學費」

**VN cũ:** 「Chút đó cứ để tôi mời đi.⏎Nếu cô ngại, thì cứ coi như là học phí đi.」

**Fix:** 「Chút đó cứ để anh mời đi.⏎Nếu em ngại, thì cứ coi như là học phí đi.」

Soutetsu nói với Paulette (mời đồ uống; Paulette đòi trả "học phí" 2461). "tôi" → "anh", "cô" → "em".

### 3016 — ハチロク — meaning

**JP:** 「あのっ！」

**TW:** 「那個！」

**VN cũ:** 「Chỗ này ạ!」

**Fix:** 「Ưm!」

Hachiroku giơ tay: JP 「あのっ！" (tiếng ngập ngừng gọi). Bản cũ "Chỗ này ạ!" bịa ra "chỗ này" — JP không hề có địa điểm. Sửa theo âm: "Ưm!" (tiền lệ: tiếng ngập ngừng あの → "Ưm").

### 3023 — 双鉄 — pronoun

**JP:** 「では、僕はお先に失礼する」

**TW:** 「那我也先走一步」

**VN cũ:** 「Vậy, tôi xin phép đi trước.」

**Fix:** 「Vậy, anh xin phép đi trước.」

Soutetsu chào Paulette ra về (cảnh buổi sáng ở cửa hàng). Tự xưng "anh".

### 3031 — 双鉄 — pronoun

**JP:** 「話すなら、どうだ、このまま歩かんか？⏎丁度、僕も駅の方へと向かおうかと思っていた」

**TW:** 「那麼我們邊走邊聊如何？我正好也想去趟車站」

**VN cũ:** 「Nếu muốn nói chuyện, hay là chúng ta cứ vừa đi vừa nói nhé?⏎Đúng lúc tôi cũng đang định đi về phía nhà ga.」

**Fix:** 「Nếu muốn nói chuyện, hay là chúng ta cứ vừa đi vừa nói nhé?⏎Đúng lúc anh cũng đang định đi về phía nhà ga.」

Soutetsu rủ Paulette vừa đi vừa nói (mở đầu cảnh đi dạo đêm). Tự xưng "anh". ("chúng ta" là số nhiều, giữ nguyên.)

### 3067 — 双鉄 — gasp

**JP:** 「っ！！！！」

**TW:** 「！！！！」

**VN cũ:** 「!!!!」

**Fix:** 「Ư!!!!」

Sweep っ-gasp: JP 「っ！！！！". Áp nguyên giá trị sweep, đã kiểm chứng đúng với JP.

### 3068 — 双鉄 — gasp

**JP:** 「っ！？」

**TW:** 「！？」

**VN cũ:** 「!?」

**Fix:** 「Ư!?」

Sweep っ-gasp: JP 「っ！？". Áp nguyên giá trị sweep, đã kiểm chứng đúng với JP. (TOML đã làm phẳng \n của dòng này thành khoảng trắng — không phải lỗi dịch.)

### 3076 — ポーレット — tag

**JP:** 「[ハチロクニイマル,3]8620ですね、もちろんです！」

**TW:** 「８６２０是嗎，當然了！」

**VN cũ:** 「Là \x%l8620;#00ffc040;8620%l;#; nhỉ, tất nhiên rồi!」

**Fix:** 「Là 8620 nhỉ, tất nhiên rồi!」

JP chỉ có ruby [ハチロクニイマル,3] trên 8620, KHÔNG có thẻ %l (đã kiểm chứng comment # JP trong TOML). Thẻ \x%l8620;#00ffc040;8620%l;#; là do bản Việt tự thêm — gỡ, giữ "8620" thường.

### 3253 — monologue — terminology

**JP:** そうして赤井宮司はじっと、⏎僕を、ハチロクを順々に、見据える。

**TW:** 之後，他依次審視著我和八六。

**VN cũ:** Rồi cung tư tế Akai chăm chú,⏎nhìn thẳng vào tôi, rồi lần lượt nhìn sang Hachiroku.

**Fix:** Rồi đền chủ Akai chăm chú,⏎nhìn thẳng vào tôi, rồi lần lượt nhìn sang Hachiroku.

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ".

### 3273 — monologue — meaning

**JP:** けれども――少しさみしげな。

**TW:** 但是又顯得有些落寞。

**VN cũ:** Nhưng――có chút gì đó cô cô đơn.

**Fix:** Nhưng――có chút gì đó cô đơn.

JP 少しさみしげな (hơi buồn/cô đơn). Bản cũ "cô cô đơn" là lỗi đánh máy (lặp từ "cô").

### 3307 — monologue — terminology

**JP:** 当然のように宮司の言葉を受けるハチロク。⏎だが、僕は――疑問の方が先に立つ。

**TW:** 八六似乎理所當然地接受了宮司的話。但我心中卻冒出一個疑問。

**VN cũ:** Hachiroku đón nhận lời của cung tư tế như một lẽ đương nhiên.⏎Nhưng tôi thì――câu hỏi lại xuất hiện trước.

**Fix:** Hachiroku đón nhận lời của đền chủ như một lẽ đương nhiên.⏎Nhưng tôi thì――câu hỏi lại xuất hiện trước.

JP 宮司. Độc thoại. 宮司 = "đền chủ".

### 3313 — monologue — terminology

**JP:** 赤井宮司の言葉を遮るような、ハチロクの声。⏎しかし宮司は、それさえ穏やかに受け入れる。

**TW:** 八六打斷了赤井宮司的話。但宮司並不在意。

**VN cũ:** Giọng của Hachiroku như muốn ngắt lời cung tư tế Akai.⏎Nhưng cung tư tế, thậm chí còn điềm tĩnh đón nhận điều đó.

**Fix:** Giọng của Hachiroku như muốn ngắt lời đền chủ Akai.⏎Nhưng đền chủ, thậm chí còn điềm tĩnh đón nhận điều đó.

JP 赤井宮司 (dòng 1) + 宮司 (dòng 2). Độc thoại. 宮司 = "đền chủ" (2 chỗ trong một dòng).

### 3321 — monologue — terminology

**JP:** 帝鉄の末期を知れどハチロクは、事故で眠ったそのために、⏎最晩年の姿を恐らく、知らないのだと。

**TW:** 八六雖然經歷過帝國鐵路的末期，卻因遭遇事故陷入長眠，恐怕並不知道帝國鐵路最後的樣子。

**VN cũ:** Dù biết về sự kết thúc của Đường sắt Hoàng gia, nhưng Hachiroku, vì đã ngủ say sau vụ tai nạn,⏎có lẽ không biết về bộ dạng của nó trong những năm tháng cuối cùng.

**Fix:** Dù biết về sự kết thúc của Teitetsu, nhưng Hachiroku, vì đã ngủ say sau vụ tai nạn,⏎có lẽ không biết về bộ dạng của nó trong những năm tháng cuối cùng.

JP 帝鉄. Độc thoại. 帝鉄 = "Teitetsu".

### 3332 — monologue — terminology

**JP:** 赤井宮司がくれた助言の中にあった、⏎『銀行への相談』が、まず間違いなくそれだろう。

**TW:** 其中一個，無疑就是宮司所提及的“找銀行商量”的建議。

**VN cũ:** Trong số những lời khuyên mà cung tư tế Akai đưa ra,⏎『Thảo luận với ngân hàng』, chắc chắn là điều đó.

**Fix:** Trong số những lời khuyên mà đền chủ Akai đưa ra,⏎『Thảo luận với ngân hàng』, chắc chắn là điều đó.

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ".

### 3390 — monologue — terminology

**JP:** ポーレットが教えてくれたように、⏎赤井宮司は影響を与えたがらない人物らしい。

**TW:** 和波萊特說的一樣，赤井宮司是一位謹言慎行的人。

**VN cũ:** Giống như những gì Paulette đã nói cho tôi biết,⏎cung tư tế Akai có vẻ là người không thích gây ảnh hưởng.

**Fix:** Giống như những gì Paulette đã nói cho tôi biết,⏎đền chủ Akai có vẻ là người không thích gây ảnh hưởng.

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ".

### 3434 — monologue — terminology

**JP:** 御一夜全体を巻き込むため、利益共有をはかるため、⏎真闇姉のアドバイスどおり、『稼がせる』ことが必要だ。

**TW:** 如果要將整個御一夜拉進我們的計劃，大家共享利益的話，就得像真闇姐說的，要讓大家“有得賺”。

**VN cũ:** Để lôi kéo toàn bộ Ohimitera, để chia sẻ lợi nhuận,⏎đúng như lời khuyên của chị Mayami, cần phải 『cho người khác kiếm tiền』.

**Fix:** Để lôi kéo toàn bộ Ohitoyo, để chia sẻ lợi nhuận,⏎đúng như lời khuyên của chị Mayami, cần phải 『cho người khác kiếm tiền』.

JP 御一夜全体. Độc thoại. 御一夜 = "Ohitoyo".

### 3444 — monologue — terminology

**JP:** やがて深く息が吐かれて、⏎やむなしとでもいわんばかりに、宮司が重そうに口を開く。

**TW:** 宮司等了一會，看我似乎沒有理解他的意思，只得深深嘆了口氣，開口說。

**VN cũ:** Một lúc sau, cung tư tế thở dài thườn thượt,⏎như thể nói hết cách rồi, ngài ấy nặng nề mở lời.

**Fix:** Một lúc sau, đền chủ thở dài thườn thượt,⏎như thể nói hết cách rồi, ngài ấy nặng nề mở lời.

JP 宮司. Độc thoại. 宮司 = "đền chủ".

### 3445 — monologue — terminology

**JP:** 赤井宮司はごく穏やかに微笑んで、⏎ハチロクを見て、また僕を見る。

**TW:** 宮司露出安穩的笑容，看著八六，然後再看向我。

**VN cũ:** Cung tư tế Akai mỉm cười thật hiền từ,⏎nhìn Hachiroku, rồi lại nhìn tôi.

**Fix:** Đền chủ Akai mỉm cười thật hiền từ,⏎nhìn Hachiroku, rồi lại nhìn tôi.

JP 赤井宮司. Độc thoại (đầu câu nên viết hoa "Đền chủ"). 宮司 = "đền chủ".

### 3470 — monologue — terminology

**JP:** そしてもうひとつ、僕は経営資源を得た。⏎赤井宮司の助言が、どれほど的確か――

**TW:** 就這樣，我又得到了一份經營資源。赤井宮司的建議真是驚人地準確——

**VN cũ:** Và một điều nữa, tôi đã có được một tài nguyên kinh doanh.⏎Lời khuyên của cung tư tế Akai, xác đáng đến nhường nào――

**Fix:** Và một điều nữa, tôi đã có được một tài nguyên kinh doanh.⏎Lời khuyên của đền chủ Akai, xác đáng đến nhường nào――

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ".

### 3487 — monologue — terminology

**JP:** 旧帝鉄の残影を、⏎まぶたの裏に、まるで描いているかのように。

**TW:** 彷彿闔上眼就能看到前帝國鐵路的昔日殘影。

**VN cũ:** Như thể đang vẽ lại tàn ảnh của Đường sắt Hoàng gia cũ⏎bên trong mí mắt.

**Fix:** Như thể đang vẽ lại tàn ảnh của Teitetsu cũ⏎bên trong mí mắt.

JP 旧帝鉄. Độc thoại. 帝鉄 = "Teitetsu".

### 3529 — monologue — terminology

**JP:** 僕らが訪ねた赤井宮司は、論戦によほど疲れたらしく、⏎……率直にいってヘロヘロだった。

**TW:** 我們去拜訪赤井宮司的時候，他看起來滿臉疲憊……老實說，大概已經精疲力盡了。

**VN cũ:** Cung tư tế Akai mà chúng tôi đến thăm có vẻ rất mệt mỏi vì cuộc tranh luận,⏎……nói thẳng ra là bơ phờ.

**Fix:** Đền chủ Akai mà chúng tôi đến thăm có vẻ rất mệt mỏi vì cuộc tranh luận,⏎……nói thẳng ra là bơ phờ.

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ" — dòng này bị sót trong lần đọc theo chunk, bắt được nhờ quét regex toàn file (lượt soát 2).

### 3536 — monologue — gasp

**JP:** 感心のあまりこぼれた「ああ」を、⏎真闇姉は、同意のそれと受け取ってしまう。

**TW:** 我在感動之餘脫口而出的回答，被真闇姐當成了肯定之意。

**VN cũ:** Tiếng 「A」 buột miệng thốt ra vì quá khâm phục của tôi,⏎đã bị chị Mayami hiểu nhầm thành sự đồng tình.

**Fix:** Tiếng 「Aa」 buột miệng thốt ra vì quá khâm phục của tôi,⏎đã bị chị Mayami hiểu nhầm thành sự đồng tình.

Độc thoại nhắc lại âm thanh: JP 「ああ」 (2 nguyên âm あ). Công thức độ dài: "Aa" (2 chữ). Bản cũ "A" chỉ 1 chữ, mất một âm.

### 3542 — monologue — terminology

**JP:** 8620発見のこと、改修計画のこと。⏎蓑笠老人、凪とふかみ、赤井宮司から教わったこと。

**TW:** 我將發現８６２０、準備修復計劃、還有從蓑笠老人、凪、深美還有赤井宮司那裡得知的事情一五一十全盤托出。

**VN cũ:** Tôi đã kể lại chuyện phát hiện ra 8620, chuyện kế hoạch phục hồi.⏎Những gì được ông lão Minokasa, Nagi và Fukami, cung tư tế Akai chỉ dạy.

**Fix:** Tôi đã kể lại chuyện phát hiện ra 8620, chuyện kế hoạch phục hồi.⏎Những gì được ông lão Minokasa, Nagi và Fukami, đền chủ Akai chỉ dạy.

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ".

### 3559 — monologue — terminology

**JP:** 単刀直入に切り出せば、⏎ゆっくりと、赤井宮司が振り返る。

**TW:** 我直接切入正題，聽到我這麼說，赤井宮司緩緩回過頭去。

**VN cũ:** Mở lời trực tiếp,⏎cung tư tế Akai từ từ quay lại.

**Fix:** Mở lời trực tiếp,⏎đền chủ Akai từ từ quay lại.

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ".

### 3562 — monologue — terminology

**JP:** 麹番をしている女性には見覚えがある。⏎僕が御一夜を発ったころには、まだ掃除番だった人だ。

**TW:** 我記得這位看顧酒麴的女性。我離開御一夜的時候，她還只是負責打掃的員工。

**VN cũ:** Tôi có biết người phụ nữ đang làm công việc trông coi men kōji.⏎Khi tôi rời Ohimitera, cô ấy vẫn còn là người dọn dẹp.

**Fix:** Tôi có biết người phụ nữ đang làm công việc trông coi men kōji.⏎Khi tôi rời Ohitoyo, cô ấy vẫn còn là người dọn dẹp.

JP 御一夜を発った. Độc thoại. 御一夜 = "Ohitoyo".

### 3567 — monologue — terminology

**JP:** 歩きながら、赤井宮司との会話について報告する。⏎もちろん、真闇姉との会話の内容も。

**TW:** 我邊走邊告訴她，我和赤井宮司還有真闇姐商量的內容。

**VN cũ:** Vừa đi, tôi vừa báo cáo về cuộc nói chuyện với cung tư tế Akai.⏎Tất nhiên là cả nội dung cuộc nói chuyện với chị Mayami nữa.

**Fix:** Vừa đi, tôi vừa báo cáo về cuộc nói chuyện với đền chủ Akai.⏎Tất nhiên là cả nội dung cuộc nói chuyện với chị Mayami nữa.

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ".

### 3589 — monologue — terminology

**JP:** 遠く、粉蔵の機関区づとめだったという赤井宮司。⏎その人が、“あの事故”として承知している。

**TW:** 既然遠在小倉機務段的赤井宮司都知道“那場事故”。

**VN cũ:** Cung tư tế Akai, người từng làm việc ở khu đầu máy Kokura xa xôi.⏎Người đó, biết về nó như là “vụ tai nạn đó”.

**Fix:** Đền chủ Akai, người từng làm việc ở khu đầu máy Kokura xa xôi.⏎Người đó, biết về nó như là “vụ tai nạn đó”.

JP 赤井宮司. Độc thoại (đầu câu nên viết hoa "Đền chủ"). 宮司 = "đền chủ".

### 3611 — monologue — terminology

**JP:** 丁度いい。面会をいただくその前に、⏎赤井宮司の人となりにつき、聞いておければありがたい。

**TW:** 正好，藉這個機會，在和赤井宮司會面前，先向波萊特打聽一下他的為人吧。

**VN cũ:** Vừa hay. Trước khi có cuộc gặp,⏎nếu được nghe kể về tính cách của cung tư tế Akai thì thật tốt.

**Fix:** Vừa hay. Trước khi có cuộc gặp,⏎nếu được nghe kể về tính cách của đền chủ Akai thì thật tốt.

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ" — dòng này bị sót trong lần đọc theo chunk, bắt được nhờ quét hệ thống.

### 3645 — monologue — meaning

**JP:** ポーレットが珍しく、口惜しそうな表情をして無言で頷く。

**TW:** 波萊特少見地露出不甘心的表情，沉默著點點頭。

**VN cũ:** Paulette hiếm khi lộ vẻ mặt cam chịu và gật đầu trong im lặng.

**Fix:** Paulette hiếm khi lộ vẻ mặt không cam lòng và gật đầu trong im lặng.

JP 口惜しそうな (vẻ mặt không cam lòng/ấm ức); TW 不甘心. Bản cũ "cam chịu" là ngược nghĩa (cam chịu = chấp nhận, 口惜しい = không chấp nhận).

### 3758 — monologue — terminology

**JP:** 蓑笠老人が見せようとした、“今の御一夜観光の実態”。⏎――収益不足による人材流失と、空洞化が産む悪循環と。

**TW:** 蓑笠老人讓我親眼見證的“御一夜旅遊現狀”。——由於收入不足導致的人才流失，以及產業空洞化所造成的惡性循環。

**VN cũ:** “Thực trạng du lịch Ohimitera hiện nay” mà ông lão Minokasa muốn cho tôi thấy.⏎――Chảy máu chất xám do thiếu hụt lợi nhuận, và vòng luẩn quẩn do sự trống rỗng tạo ra.

**Fix:** “Thực trạng du lịch Ohitoyo hiện nay” mà ông lão Minokasa muốn cho tôi thấy.⏎――Chảy máu chất xám do thiếu hụt lợi nhuận, và vòng luẩn quẩn do sự trống rỗng tạo ra.

JP 御一夜観光. Độc thoại. 御一夜 = "Ohitoyo".

### 3792 — monologue — terminology

**JP:** たずねた途端、宮司の表情が柔らかみを増す。⏎「わかってらっしゃる」――顔が、言葉を発してる。

**TW:** 話音剛落，宮司的表情就變得更加柔和起來，也就是說我沒猜錯。

**VN cũ:** Ngay khi tôi vừa hỏi, nét mặt cung tư tế trở nên hiền hòa hơn.⏎『Cậu hiểu rõ đấy』――Khuôn mặt ngài ấy đang nói như vậy.

**Fix:** Ngay khi tôi vừa hỏi, nét mặt đền chủ trở nên hiền hòa hơn.⏎『Cậu hiểu rõ đấy』――Khuôn mặt ngài ấy đang nói như vậy.

JP 宮司. Độc thoại. 宮司 = "đền chủ".

### 3829 — monologue — terminology

**JP:** ハチロクの驚きを見て、⏎もったいぶるように、赤井宮司はひといきを置く。

**TW:** 赤井宮司停下來，欣賞了一下八六驚訝的表情，然後說道。

**VN cũ:** Nhìn thấy sự ngạc nhiên của Hachiroku,⏎như thể đang làm ra vẻ quan trọng, cung tư tế Akai dừng lại một nhịp.

**Fix:** Nhìn thấy sự ngạc nhiên của Hachiroku,⏎như thể đang làm ra vẻ quan trọng, đền chủ Akai dừng lại một nhịp.

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ" — dòng này bị sót trong lần đọc theo chunk, bắt được nhờ quét hệ thống.

### 3830 — monologue — terminology

**JP:** しみじみと、赤井宮司は目を閉じる。

**TW:** 赤井宮司感慨頗深地閉上眼睛。

**VN cũ:** Cung tư tế Akai nhắm mắt lại đầy thấm thía.

**Fix:** Đền chủ Akai nhắm mắt lại đầy thấm thía.

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ" — dòng này bị sót trong lần đọc theo chunk, bắt được nhờ quét regex toàn file (lượt soát 2).

### 3832 — monologue — terminology

**JP:** ならば安心というように、⏎赤井宮司は穏やかな目でハチロクを見る。

**TW:** 赤井宮司溫柔地望著歡喜雀躍的八六，似乎是在對她說“不用擔心”。

**VN cũ:** Như muốn nói vậy thì yên tâm rồi,⏎cung tư tế Akai nhìn Hachiroku bằng ánh mắt hiền từ.

**Fix:** Như muốn nói vậy thì yên tâm rồi,⏎đền chủ Akai nhìn Hachiroku bằng ánh mắt hiền từ.

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ".

### 3833 — monologue — terminology

**JP:** 赤井宮司の視線がリストの上へと落ちる。⏎ハチロクも緊張するのか、唇をきゅっと引き結んでいる。

**TW:** 赤井宮司瀏覽起清單。八六雙唇緊閉，她似乎也很緊張。

**VN cũ:** Ánh mắt của cung tư tế Akai lướt trên danh sách.⏎Hachiroku có lẽ cũng căng thẳng, mím chặt môi.

**Fix:** Ánh mắt của đền chủ Akai lướt trên danh sách.⏎Hachiroku có lẽ cũng căng thẳng, mím chặt môi.

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ".

### 3834 — monologue — terminology

**JP:** 元帝鉄のレイルロオドのハチロクに、⏎赤井宮司は、まるで１から教えるような話しぶりだ。

**TW:** 赤井宮司的語氣，聽起來彷彿是在從零開始教導八六這個前帝國鐵路的鐵路人偶一般。

**VN cũ:** Đối với Hachiroku, một Railord của Đường sắt Hoàng gia cũ,⏎cung tư tế Akai nói chuyện như thể đang dạy lại từ đầu.

**Fix:** Đối với Hachiroku, một Railord của Teitetsu cũ,⏎đền chủ Akai nói chuyện như thể đang dạy lại từ đầu.

JP 元帝鉄 + 赤井宮司. Hai fix: 帝鉄 = "Teitetsu"; 宮司 = "đền chủ".

### 3835 — monologue — terminology

**JP:** 赤井宮司は、疲れが抜けたご様子だ。

**TW:** 赤井宮司看來已經恢復了。

**VN cũ:** Cung tư tế Akai có vẻ đã hết mệt mỏi.

**Fix:** Đền chủ Akai có vẻ đã hết mệt mỏi.

JP 赤井宮司. Độc thoại (đầu câu nên viết hoa "Đền chủ"). 宮司 = "đền chủ".

### 3836 — monologue — terminology

**JP:** 帝鉄の末路を知る赤井宮司。⏎衰退に、まさに晒されている御一夜の人たち。

**TW:** 赤井宮司見證過帝國鐵路的末路。也了解為衰退所苦的御一夜的人們。

**VN cũ:** Cung tư tế Akai biết về kết cục của Đường sắt Hoàng gia.⏎Những người dân Ohimitera đang thực sự phơi mình trước sự suy thoái.

**Fix:** Đền chủ Akai biết về kết cục của Teitetsu.⏎Những người dân Ohitoyo đang thực sự phơi mình trước sự suy thoái.

JP 帝鉄 + 赤井宮司 + 御一夜. Ba fix trong một dòng: 帝鉄 = "Teitetsu"; 宮司 = "đền chủ"; 御一夜 = "Ohitoyo".

### 3837 — monologue — terminology

**JP:** 小さく頷き、⏎赤井宮司は今度はハチロクへと向きなおる。

**TW:** 赤井宮司輕輕點頭，看向八六。

**VN cũ:** Khẽ gật đầu,⏎cung tư tế Akai lần này quay sang Hachiroku.

**Fix:** Khẽ gật đầu,⏎đền chủ Akai lần này quay sang Hachiroku.

JP 赤井宮司. Độc thoại. 宮司 = "đền chủ".

### 3838 — monologue — terminology

**JP:** 赤井宮司は静かに頷き、僕の目を見る。

**TW:** 赤井宮司靜靜點頭，直視我的眼睛。

**VN cũ:** Cung tư tế Akai lặng lẽ gật đầu, nhìn vào mắt tôi.

**Fix:** Đền chủ Akai lặng lẽ gật đầu, nhìn vào mắt tôi.

JP 赤井宮司. Độc thoại (đầu câu nên viết hoa "Đền chủ"). 宮司 = "đền chủ".

## 4. Kiểm tra chéo

- **Chuỗi xoay (rotation):** 0 chuỗi. Không có dòng nào mà VN đúng nằm ở key khác trong file.
- **Nhiễm chéo file:** 0. Xem §2 (0 trùng khớp ngoài file trong 102 giá trị fix).
- **Thẻ %l:** 2 tag do bản Việt tự thêm đã gỡ (2404 醸造蔵, 3076 8620 — JP chỉ có ruby [..,n], đã kiểm chứng comment `# JP:` trong TOML; không có tag nào thiếu dấu `;` đóng trong file này). Các thẻ %l còn lại đều là của JP và được giữ nguyên (1797 本屋, 2693 電車, 2753 本屋, 2580 電車).
- **Gasp っ:** sweep CÓ liệt kê file này (3 mục 1811/3067/3068, áp nguyên). Audit tự quét toàn bộ っ trong JP: không còn gasp trần nào bị mất ngoài 3 mục sweep; các っ còn lại đều đã được diễn đúng (2406 えっ→"Hả!?", 2407 あっ→"A!", 2429 あっ/そうっ→nói lắp, 2425/2631 ho "khụ", 2393/2395/2461 cười "Ufufu") hoặc là っ nhấn mạnh cuối từ (2435 いえっ, 2501 はいっ, 3006 ごちそうさまっ, 3017 ですからっ — không thêm Ư, đúng quy tắc sweep).
- **まいてつ / 市電:** file này không có dòng nào dùng 2 thuật ngữ này (0 gloss まいてつ, 0 市電) — không áp dụng quyết định mới 20/11 ở đây.
- **"Anh Akai" (2406):** đã kiểm chứng KHÔNG phải lỗi — quét toàn dự án cho thấy "Anh Akai" là cách dịch đã thiết lập của 赤井さん (Hibiki ở 日々姫08 2259, Nagayama ở P14 1524, 技工Ｂ ở ニイロク03 4 lần). Paulette dùng "Anh Akai" khớp với quy ước chung của dự án (TW dịch 赤井さん là 赤井先生, nhưng bản Việt đã thống nhất "anh Akai").
- **2409 「ああ」→「A.」:** KHÔNG phải lỗi — quét toàn dự án: 「ああ」 đứng một mình được dịch 「A.」 16 lần (so với 「Ừ.」 54, 「À.」 48); "A." là cách dịch đã có trong dự án, giữ nguyên.
- **Soutetsu "tôi" giữ nguyên (đúng):** với Akai (2590, 2576, 2636, 2906, 2701, 2999, 2609, 2848) và với Hachiroku (2337) — quan hệ trang trọng, "tôi" đúng. Số nhiều "chúng tôi" với Paulette (2886, 2287) giữ nguyên; "Bọn em" (nhóm Soutetsu+Hachiroku) với Mayami (2592) giữ nguyên — quy tắc đại từ chỉ áp cho tự xưng số ít.

## 5. Kiểm tra lần 2 (second pass)

Đọc lại toàn bộ 102 fix so với JP của từng dòng: **tổng 102 / kiểm tra lại 102 / loại bỏ 0 / sửa 1**. Lần 2 bắt được 1 lỗi chép trong bản thảo fix: 3536 viết "sự đồng ý" trong khi VN cũ là "sự đồng tình" — đã sửa lại thành "đồng tình" (chỉ thay 「A」→「Aa」). Ngoài ra, trong lúc kiểm chứng, quét regex hệ thống toàn file theo từng thuật ngữ đã quyết đã bắt thêm **2 dòng mà lần đọc theo chunk bỏ sót** (3529, 3830 — đều là 宮司), nâng tổng từ 100 lên 102; riêng 宮司 lần đọc chunk đếm 35 dòng, quét hệ thống cho ra **38 dòng / 39 lần xuất hiện** (2620 đã có trong fix list qua nhóm 帝鉄; 3529 và 3830 hoàn toàn bị sót). Parse-check riêng là chưa đủ; con số trên là từ lần đọc lại bằng mắt + đối chiếu diff từng dòng.

## 6. Các dòng cố tình KHÔNG sửa (ghi chú phán đoán)

- **2406 "Anh Akai":** xem §4 — cách dịch đã thiết lập của 赤井さん toàn dự án. Không sửa.
- **2409 「ああ」→「A.」:** xem §4 — "A." đã có 16 lần trong dự án. Không sửa.
- **2408 「おお……」→「Ồ……」:** cách diễn cảm thán đã chuẩn. Không sửa.
- **2415 "chú chó con":** Soutetsu nói nhầm 子犬 (chó con) trong khi Paulette nói 子猫 (mèo con) — lỗi nhầm của chính nhân vật, là trò đùa trong truyện; Hachiroku sửa lại cho anh ta ở 2621. Không sửa.
- **3747 "Pyon!":** SFX giữ nguyên theo quy tắc ngẫu hứng 22:05 (tiếng nhảy của Hachiroku).
- **2909 "mài ra ăn được":** thành ngữ Việt đã thiết lập cho 理想で飯が食える. Không sửa.
- **2592 "Bọn em":** nhóm Soutetsu+Hachiroku nói với Mayami — số nhiều, không thuộc quy tắc tự xưng số ít. Không sửa.
- **2623 "các cậu":** Soutetsu gọi nhóm (Soutetsu+Hachiroku) — xưng hô nhóm, giữ nguyên.
- **3314 "Watashi" và 3884 "Reina":** bản thân các từ này đang được bàn luận trong hội thoại. Không sửa.
- **2681/2753 thẻ %l của 本屋:** JP có thẻ, bản Việt giữ đúng. Không sửa.
- **2886/2287 "chúng tôi" với Paulette; 2337 "Tôi" với Hachiroku; 2590/2576/2636/2906/2701/2999/2609/2848 "tôi" với Akai/Hachiroku:** đều đúng (số nhiều / quan hệ trang trọng). Không sửa.
- **1816 「……」:** JP/TW/VN giống hệt nhau — dấu lặng, hợp lệ. Không sửa.
- **2435/3017/2429/2501/3006 (っ nhấn mạnh cuối từ):** đã diễn đúng, không thêm Ư. Không sửa.
- **2572:** fix "tôi"→"anh" được giữ (xem ghi chú trong mục đó) — địa chỉ suy từ mạch truyện (kế hoạch cho mèo là của Paulette; cô ấy nói trước 2887 và tiếp sau 2805), không chắc tuyệt đối như các dòng đi dạo đêm nhưng đủ vững.

## Kết bài

File 11 là file 00_Common "bẩn" nhất tính đến nay (102/572 = 17,8%), nhưng bẩn vì thuật ngữ và đại từ — không phải vì cấu trúc: 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 dòng chưa chắc chắn. 59 lỗi thuật ngữ (宮司 38 dòng là nhiều nhất — file xoay quanh Akai) và 30 lỗi đại từ Soutetsu↔Paulette đều là hệ quả của các quyết định 19–20/11 chưa được áp dụng vào bản dịch cũ, cộng với thói quen xưng hô cũ của dịch giả. Toàn bộ 102 fix đều sửa tại chỗ. Sau file này, Ohitoyo còn lại trong 00_Common là 76 lần (14: 30, 15: 15, 10: 14, 12: 6, 13: 3, file 01 pilot: 8 chưa chốt — file 10 đang được audit song song, parent sẽ cộng dồn khi xong). Còn lại chưa kiểm toán trong 00_Common: 10, 12, 13, 14, 15, 末尾 (7 file trừ file 01 bản nháp; file 10 đang chạy).

Khối TOML dưới đây parse được bằng tomllib, **102 key, 0 sai lệch giá trị so với JSON**. Quy tắc ký tự xuống dòng: giá trị fix nào chứa ký tự xuống dòng dạng backslash-n (2 ký tự, như trong JSON và trong TOML gốc) thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON.

```toml
[script]
"1777" = "……Vụ tai nạn mà Hachiroku trải qua,\\ncó lẽ thảm khốc đến mức lưu danh trong lịch sử Teitetsu."
"1797" = "「\\x%l本屋;#00ffc040;Tòa nhà chính%l;#; và khu toa khách toa hàng. Anh đã học được hai thuật ngữ chuyên ngành.\\nChắc cũng đủ để làm Hachiroku ngạc nhiên đấy.」"
"1811" = "「…………Ư」"
"1828" = "「……Ra là vậy.\\nVậy, nơi làm việc cũng không phải ở Ohitoyo?」"
"1845" = "「……Paulette này,\\nem bắt đầu thích đường sắt từ khi nào vậy?」"
"2238" = "「Có vẻ thú vị đấy. Nếu có gì cần giúp thì cứ nói với anh.\\nCó thể nó cũng sẽ góp phần vào việc chấn hưng du lịch đấy.」"
"2239" = "「Không sao. Nếu em đang vội thì――」"
"2250" = "「Không, nếu em cử động được thì bây giờ không còn chuyện gì để nói nữa.\\nAnh đã lo lắng không biết có phải em bị đau lưng không.」"
"2253" = "「Không, chỉ những chuyện vừa rồi cũng đủ để tham khảo rồi.\\nCảm ơn em.」"
"2293" = "「Có vẻ là định như vậy.\\nNhưng đền chủ Akai không bị lung lạc mà đã tìm cách đuổi về được.」"
"2299" = "「Vụ chó trưởng ga mà em nói hôm trước à?」"
"2302" = "「Anh Soutetsu cũng biết nhỉ.\\nNhưng nghe nói đền chủ Akai không làm việc ở nhà máy đâu.」"
"2308" = "「Em có biết cô gái tên Houshou Kisaki không?」"
"2380" = "「Em có phiền cùng anh đi xác nhận tài nguyên kinh doanh của anh không?」"
"2396" = "「Phùù」"
"2401" = "「Ái chà. Thật thất lễ khi chưa tự giới thiệu mà đã kể chuyện xưa.\\nTôi là đền chủ của đền này, Akai Kiyoharu.」"
"2404" = "「Ây da, bé Sou và bé Hachiroku.\\nĐến nhà xưởng ủ rượu thế này, hiếm thấy ghê nha.」"
"2419" = "「Hừừm.」"
"2423" = "「A, à. Đúng vậy nhỉ. Em nên nghỉ ngơi sớm đi.」"
"2445" = "「Em uống cái này đi.」"
"2450" = "「Ừm. Đúng là vậy. Tôi muốn nhờ chị.」"
"2466" = "「Anh không mang điện thoại mà.」"
"2479" = "「Nữ lái tàu sao? Anh nghe Hachiroku nói là hiếm lắm mà.」"
"2503" = "「Tôi đã hiểu, đền chủ Akai.」"
"2522" = "「Trong số các nhân viên tòa thị chính, có dì của đền chủ.\\nNghe nói việc ngài ấy cất công đi làm ở Teitetsu cũng vì lý do tương tự.」"
"2525" = "「Chia sẻ bản thân việc phục hồi 8620 như một tài nguyên kinh doanh của toàn bộ Ohitoyo.\\nĐể mọi người nghĩ rằng, có thể sinh ra lợi nhuận từ việc tận dụng nó.」"
"2529" = "「Kokura……Cũng từng được nhắc đến trong câu chuyện của ông lão Minokasa.\\nChắc chắn là nơi từng có nhà máy của Teitetsu đúng không?」"
"2530" = "「Khu đầu máy Kokura cũng được trang bị dòng 8620. Do đó,\\nđền chủ Akai đã biết đến hình dáng của Railord dòng 8620.」"
"2535" = "「Nếu đặt tên, thì sao nhỉ――\\n『Shochu Hơi Nước・Hachiroku Ohitoyo』 thì thế nào.」"
"2546" = "「Teitetsu những năm cuối đời đã đầu tư toàn bộ tài nguyên kinh doanh vào việc điện khí hóa,\\nnhưng không thu được lợi nhuận, và đã sụp đổ.」"
"2572" = "「Chắc sẽ suôn sẻ thôi.\\nTheo như anh biết, Hibiki rất được động vật yêu quý.」"
"2578" = "「Đến mức đó thì……tôi cũng,\\nchưa nói chuyện sâu với bản thân đền chủ.」"
"2580" = "「Tôi cũng từng làm lái tàu, nhưng cuối cùng thì làm nhân viên cơ vụ.\\nỞ đoạn đường thử nghiệm Kokura, tôi đã điều khiển \\x%l電車;#00ffc040;tàu điện%l;#;.」"
"2582" = "「Tôi cũng là người Hinomoto mà?\\nDù thời gian lớn lên ở Frank khá dài.」"
"2583" = "「Trước đây anh cũng từng nhìn thấy một chút rồi, thật là một món đồ tuyệt đẹp.」"
"2596" = "「Anh thì có gì mà không hổ danh?」"
"2599" = "「Vừa nãy, anh có gọi điện thoại.」"
"2612" = "「Hiện tại, tôi đang lên kế hoạch cho một việc cùng với nhóm Paulette.」"
"2620" = "「Tôi nghe người ta nói ngài từng làm việc ở Teitetsu cũ――\\nĐền chủ, ngài từng là lái tàu sao?」"
"2624" = "「Tôi có cảm giác,\\ntôi chưa kể được chuyện gì có ích cho lắm.」"
"2628" = "「Không phải hàng nội địa đâu.\\nLà hàng sản xuất tại Minh Quốc đấy. WALLTHAM.」"
"2645" = "「Gặp anh?」"
"2672" = "「Là cựu lái tàu thôi. Bây giờ, tôi chỉ là một đền chủ.」"
"2689" = "「Ý cô là Đường sắt điện Hiroshima sao.\\nRa là vậy――nếu nghĩ như thế, thì chúng tôi cũng được đền đáp phần nào nhỉ.」"
"2693" = "「Vâng. Hokkaido, Shikoku, Kyushu――Trên toàn cõi Hinomoto.\\nTeitetsu đã tuyệt vọng coi \\x%l電車;#00ffc040;tàu điện%l;#; chính là con bài tẩy để phục sinh.」"
"2711" = "「Là chữ đó sao. Ra là vậy, anh hiểu rồi.」"
"2753" = "「Theo “Lịch sử ga suối nước nóng Ohitoyo”, xưởng đầu máy này,\\nđược xây dựng cùng với \\x%l本屋;#00ffc040;tòa nhà chính%l;#; vào năm Minh Trí thứ 41 đấy.」"
"2782" = "「Là việc anh tự mình tìm đến được chỗ đền chủ Akai đấy.\\nTôi vốn định để một thời gian nữa mới giới thiệu cơ.」"
"2783" = "「Ngài ấy là một người khá thực tế nhỉ, đền chủ Akai ấy.」"
"2814" = "「Đền chủ cũng bận rộn nhỉ.」"
"2817" = "「Tất nhiên rồi. Ngân hàng――\\nLà giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto, nghĩa là...」"
"2818" = "「Tất nhiên là bằng sự phục sinh và lăn bánh của 8620.\\nĐể làm được điều đó, tôi muốn thực hiện các công việc cần thiết ở Ohitoyo càng nhiều càng tốt.」"
"2839" = "「Chị Mayami, tôi nhớ chị từng nói là trong nhà này\\nvẫn còn một cái lò hơi than không dùng đến.」"
"2842" = "「Dựa trên điều đó, chị Mayami, có một chuyện tôi muốn chị chỉ cho tôi.」"
"2886" = "「Dù sao thì, nghe nói Kisaki đó đã đến thăm.\\nTrước khi chúng tôi đến thăm chỗ đền chủ Akai.」"
"2901" = "「Khi tổng thống Minh Quốc đến thăm,\\nnghe nói họ đã dùng tàu ngự dụng để ông ấy di chuyển.」"
"2937" = "「Ý cậu là,\\ntập trung con người và công nghệ ở Ohitoyo sao.」"
"2960" = "「Đền Akai Aso là ngôi đền lớn nhất và lâu đời nhất ở Ohitoyo,\\ntất nhiên, số lượng giáo dân cũng rất đông, nên có sức ảnh hưởng lớn.」"
"2987" = "「Đúng vậy, đối với một người Hinomoto như anh cũng hơi khó.」"
"2995" = "「Vậy sao. Nếu thế thì anh yên tâm rồi.」"
"2997" = "「À, cổ họng em bị mệt sao.\\nĐợi một chút.」"
"2998" = "「Vậy sao, nếu thế, tối nay anh sẽ gọi điện thoại báo cáo.」"
"3002" = "「Vậy ra,\\nhai người cũng đã đi gặp đền chủ Akai rồi sao.」"
"3003" = "「Chút đó cứ để anh mời đi.\\nNếu em ngại, thì cứ coi như là học phí đi.」"
"3016" = "「Ưm!」"
"3023" = "「Vậy, anh xin phép đi trước.」"
"3031" = "「Nếu muốn nói chuyện, hay là chúng ta cứ vừa đi vừa nói nhé?\\nĐúng lúc anh cũng đang định đi về phía nhà ga.」"
"3067" = "「Ư!!!!」"
"3068" = "「Ư!?」"
"3076" = "「Là 8620 nhỉ, tất nhiên rồi!」"
"3253" = "Rồi đền chủ Akai chăm chú,\\nnhìn thẳng vào tôi, rồi lần lượt nhìn sang Hachiroku."
"3273" = "Nhưng――có chút gì đó cô đơn."
"3307" = "Hachiroku đón nhận lời của đền chủ như một lẽ đương nhiên.\\nNhưng tôi thì――câu hỏi lại xuất hiện trước."
"3313" = "Giọng của Hachiroku như muốn ngắt lời đền chủ Akai.\\nNhưng đền chủ, thậm chí còn điềm tĩnh đón nhận điều đó."
"3321" = "Dù biết về sự kết thúc của Teitetsu, nhưng Hachiroku, vì đã ngủ say sau vụ tai nạn,\\ncó lẽ không biết về bộ dạng của nó trong những năm tháng cuối cùng."
"3332" = "Trong số những lời khuyên mà đền chủ Akai đưa ra,\\n『Thảo luận với ngân hàng』, chắc chắn là điều đó."
"3390" = "Giống như những gì Paulette đã nói cho tôi biết,\\nđền chủ Akai có vẻ là người không thích gây ảnh hưởng."
"3434" = "Để lôi kéo toàn bộ Ohitoyo, để chia sẻ lợi nhuận,\\nđúng như lời khuyên của chị Mayami, cần phải 『cho người khác kiếm tiền』."
"3444" = "Một lúc sau, đền chủ thở dài thườn thượt,\\nnhư thể nói hết cách rồi, ngài ấy nặng nề mở lời."
"3445" = "Đền chủ Akai mỉm cười thật hiền từ,\\nnhìn Hachiroku, rồi lại nhìn tôi."
"3470" = "Và một điều nữa, tôi đã có được một tài nguyên kinh doanh.\\nLời khuyên của đền chủ Akai, xác đáng đến nhường nào――"
"3487" = "Như thể đang vẽ lại tàn ảnh của Teitetsu cũ\\nbên trong mí mắt."
"3529" = "Đền chủ Akai mà chúng tôi đến thăm có vẻ rất mệt mỏi vì cuộc tranh luận,\\n……nói thẳng ra là bơ phờ."
"3536" = "Tiếng 「Aa」 buột miệng thốt ra vì quá khâm phục của tôi,\\nđã bị chị Mayami hiểu nhầm thành sự đồng tình."
"3542" = "Tôi đã kể lại chuyện phát hiện ra 8620, chuyện kế hoạch phục hồi.\\nNhững gì được ông lão Minokasa, Nagi và Fukami, đền chủ Akai chỉ dạy."
"3559" = "Mở lời trực tiếp,\\nđền chủ Akai từ từ quay lại."
"3562" = "Tôi có biết người phụ nữ đang làm công việc trông coi men kōji.\\nKhi tôi rời Ohitoyo, cô ấy vẫn còn là người dọn dẹp."
"3567" = "Vừa đi, tôi vừa báo cáo về cuộc nói chuyện với đền chủ Akai.\\nTất nhiên là cả nội dung cuộc nói chuyện với chị Mayami nữa."
"3589" = "Đền chủ Akai, người từng làm việc ở khu đầu máy Kokura xa xôi.\\nNgười đó, biết về nó như là “vụ tai nạn đó”."
"3611" = "Vừa hay. Trước khi có cuộc gặp,\\nnếu được nghe kể về tính cách của đền chủ Akai thì thật tốt."
"3645" = "Paulette hiếm khi lộ vẻ mặt không cam lòng và gật đầu trong im lặng."
"3758" = "“Thực trạng du lịch Ohitoyo hiện nay” mà ông lão Minokasa muốn cho tôi thấy.\\n――Chảy máu chất xám do thiếu hụt lợi nhuận, và vòng luẩn quẩn do sự trống rỗng tạo ra."
"3792" = "Ngay khi tôi vừa hỏi, nét mặt đền chủ trở nên hiền hòa hơn.\\n『Cậu hiểu rõ đấy』――Khuôn mặt ngài ấy đang nói như vậy."
"3829" = "Nhìn thấy sự ngạc nhiên của Hachiroku,\\nnhư thể đang làm ra vẻ quan trọng, đền chủ Akai dừng lại một nhịp."
"3830" = "Đền chủ Akai nhắm mắt lại đầy thấm thía."
"3832" = "Như muốn nói vậy thì yên tâm rồi,\\nđền chủ Akai nhìn Hachiroku bằng ánh mắt hiền từ."
"3833" = "Ánh mắt của đền chủ Akai lướt trên danh sách.\\nHachiroku có lẽ cũng căng thẳng, mím chặt môi."
"3834" = "Đối với Hachiroku, một Railord của Teitetsu cũ,\\nđền chủ Akai nói chuyện như thể đang dạy lại từ đầu."
"3835" = "Đền chủ Akai có vẻ đã hết mệt mỏi."
"3836" = "Đền chủ Akai biết về kết cục của Teitetsu.\\nNhững người dân Ohitoyo đang thực sự phơi mình trước sự suy thoái."
"3837" = "Khẽ gật đầu,\\nđền chủ Akai lần này quay sang Hachiroku."
"3838" = "Đền chủ Akai lặng lẽ gật đầu, nhìn vào mắt tôi."
```
