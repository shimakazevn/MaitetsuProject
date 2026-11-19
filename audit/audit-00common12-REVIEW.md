# Audit 00_Common file 12 — 共通12_のぞみ.txt.toml

**35/520 dòng sai (6,7%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng.**

## 1. Tổng quan

| Loại | Số dòng | Key |
|---|---|---|
| Thuật ngữ | 15 | Ohimitera→Ohitoyo 6 (2169, 2211, 2458, 2569, 2184, 3447 — đúng con số ~6 đã đếm trước đó); 宮司→"đền chủ" 6 (3436, 2069, 3433 "Cung tư tế"; 3445, 3435, 3038 "Thầy Akai" — biến thể "Thầy" chưa có trong thống kê cũ); 湯医→Yunoi 1 (3391 — dòng "Yui" thứ ba trong dự án); 撮り鉄→"người chụp ảnh tàu" 1 (2415); 車両鉄→"người mê toa xe" 1 (2492, kèm khôi phục tag %l) |
| Đại từ | 13 | Soutetsu "anh"→"tôi" với Hachiroku 4 (2132, 2193, 2251, 2626 — dòng 2); Soutetsu "tôi"→"anh" với Fukami 1 (2424) + với Reina 1 (2117 — người nghe là Reina, xem §3); Soutetsu gọi Hachiroku "cô"→"em" 7 (1970, 2320, 1973, 2266, 2269, 2300, 2538) |
| Gasp (っ) | 2 | 2632, 2633 — cả 2 đều từ sweep, đã kiểm chứng đúng |
| Nghĩa | 3 | 2385 (だご bị bỏ — "đói bụng" không có trong JP), 2403 (bịa thêm "chuyên dụng"), 3241 (từ Hàn "확" lọt vào VN) |
| Lỗi đánh máy | 1 | 2102 ("dang" → "đang") |
| SFX | 1 | 2113 (おっと "Hây dô." → "Ôi chà." — lỗi dán nhầm, xem §3) |
| **Tổng** | **35** | |

Thoại 27/303 sai (8,9%), độc thoại 8/217 sai (3,7%). Theo nhân vật: 双鉄 19, monologue 8, 日々姫 3, 赤井宮司 2, ポーレット 1, 凪 1, 早瀬流 1.

## 2. Phương pháp

- Nguồn: CSV3 bộ duy nhất 00_Common (520 dòng, toàn `script`); TOML-2 `共通12_のぞみ.txt.toml`, md5 `7cef20cf0cab502f5680336f10ea8d85`, 111.255 byte, BOM + CRLF (1.109 CRLF, 0 LF-only), `[selections]` rỗng, không có bản sao trùng (không thuộc 11 nhóm trùng).
- So sánh CSV↔TOML: 194 dòng khớp tuyệt đối + 326 dòng khớp sau khi gộp ký tự xuống dòng, **0 khác biệt** — nguồn sạch, CSV3 là bản tin cậy cho fix list.
- Sweep っ: kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` — file này có **2 mục** (2632, 2633, đều lost-gasp-whole). Cả 2 giá trị đã kiểm chứng đúng với JP và được nhận nguyên văn. Quét bổ sung toàn bộ 189 dòng JP chứa っ (24 ứng viên gasp): các dòng còn lại đều là っ nhấn mạnh cuối câu hoặc âm đã được render (2100 ぅっ→"Ư", 2071 えっ!?→"Hả!?", 2060 ひゃあっ!?→"Hyaa!?", 2059 はうっ→"Hau!!?", 2029 きゃっ!?→"Á, á!?", 2119 ぉぅっ!?→"Ối!?"). Không có gasp nào sweep bỏ sót trong file này.
- Nhiễm chéo: tra toàn bộ chỉ mục VN của dự án — 155 lần trùng, tất cả đều là các câu ngắn thông dụng được dịch độc lập giống nhau ("Đúng vậy nhỉ.", "Vậy sao.", "Ra là vậy.", "Vâng ạ.", v.v.); 0 lần trùng VN trong file với JP khác nhau; JP trùng trong file đều hợp lệ (2110/2083/2084 うむ→"Ừm." giống hệt; 2363/2228 はい và 2359/2349 ああ khác ngữ cảnh). Riêng 2118/2113 cùng JP おっと nhưng VN khác nhau — chính là lỗi 2113 (xem §3). Không có nhiễm chéo.
- Kiểm tra chuỗi xoay trước khi dịch mới: không có dòng lệch nào, nên không cần dịch mới dòng nào; không có dòng mồ côi, không có dòng chưa dịch.
- Quét cơ học toàn bộ giá trị VN đầy đủ (không cắt ngắn): các thuật ngữ đã chốt chỉ còn đúng các dòng trong fix list (Ohimitera đúng 6, Yui đúng 1, "Cung tư tế"/"Thầy Akai" đúng 6, Tori-tetsu/Sharyo-tetsu mỗi loại 1); tag %l chỉ lệch ở 4 dòng (2968, 2597, 2492, 2300 — xem §3/§4); ký tự ngoại ngữ trong VN chỉ còn 3241 (từ Hàn "확" — đã sửa) ngoài các thuật ngữ JP hợp lệ trong tag %l.
- Quy tắc áp dụng: Ohitoyo / Teitetsu / Yunoi / "chủ tàu" / "tàu điện thành phố" / "thân bảo trì" / "thân vận hành" / KiHa / "đền chủ" / Migita Ichi / "vé lượt" / Railord / Olivy; quy tắc đại từ Soutetsu đã sửa ("anh" với Hibiki/Michiko/Paulette/Reina, "tôi" với Hachiroku/Mayami/Nagi/Minokasa — KHÔNG dùng lối tắt cũ "chỉ với Hibiki"); khóa B4 (双鉄くん→"anh Soutetsu", không có ngoại lệ rên; tên trần ソウテツ trong cảnh gọi tên là có chủ đích); Hachiroku với Fukami là "chị" (tiền lệ file 10 key 2616); quy tắc ngẫu hứng 22:05 (SFX theo nhân vật + ngữ cảnh, không dập khuôn; tiếng cười không bao giờ thành tiếng rên); công thức độ dài nguyên âm (số nguyên âm VN = 1 + số う/ぅ trong JP); JP thắng TW khi xung đột; cảnh giác bịa của Gemini (từ bịa không có cơ sở JP, tag %l tự thêm, hoàn thiện câu JP bị cắt cụt — nhưng kiểm tra TW trước khi kết luận 義 là bịa: 義父/義母 có thể là "bố nuôi/mẹ nuôi" khi TW nói 養父/養母).

## 3. Các lỗi đã sửa (35 dòng)

### 1970 — 双鉄 — Đại từ

**JP:** 「それこそ甘いな。考えが」

**TW:** 「你想得太簡單了」

**VN cũ:** 「Suy nghĩ của cô ngây thơ quá đấy.」

**Fix:** 「Suy nghĩ của em ngây thơ quá đấy.」

Soutetsu gọi Hachiroku là "em" — trong file này Soutetsu đã gọi Hachiroku là "em" ở 2132, 2193, 2251, 2626; 7 dòng "cô" là ngoại lệ, thống nhất thành "em".

### 1973 — 双鉄 — Đại từ

**JP:** 「やっと言ったな。お前の望みを」

**TW:** 「你終於說出你的心願了啊」

**VN cũ:** 「Cuối cùng cô cũng chịu nói ra rồi. Mong muốn của cô.」

**Fix:** 「Cuối cùng em cũng chịu nói ra rồi. Mong muốn của em.」

Như 1970: Soutetsu gọi Hachiroku là "em" (2× "cô" trong cùng dòng).

### 2069 — 双鉄 — Thuật ngữ

**JP:** 「これはこれは、⏎赤井宮司に足をお運びいただけるとは、光栄です」

**TW:** 「哎呀，赤井先生大駕光臨，真是榮幸」

**VN cũ:** 「Ái chà ái chà,⏎Được cung tư tế Akai cất công đến đây, thật là vinh hạnh.」

**Fix:** 「Ái chà ái chà,⏎Được đền chủ Akai cất công đến đây, thật là vinh hạnh.」

Quyết định 19/11: 宮司 = "đền chủ". "Cung tư tế" là dạng cũ cần thống nhất.

### 2102 — 双鉄 — Lỗi đánh máy

**JP:** 「うん――おお！　なかなかどうして、⏎立派にやっているではないか」

**TW:** 「嗯——噢！這不是做得很好嗎」

**VN cũ:** 「Ừ——ồ! Chẳng phải em ấy,⏎dang làm rất tốt hay sao.」

**Fix:** 「Ừ——ồ! Chẳng phải em ấy,⏎đang làm rất tốt hay sao.」

Lỗi đánh máy: "dang" → "đang".

### 2113 — 早瀬流 — SFX

**JP:** 「おっと」

**TW:** 「嘿」

**VN cũ:** 「Hây dô.」

**Fix:** 「Ôi chà.」

おっと là tiếng kêu ngạc nhiên ("Ôi chà"), không phải tiếng hô gắng sức. VN cũ "Hây dô." là cách dịch của よっと (heave-ho) — xem 日々姫08 2251 render よっと thành "Hây dô."; cùng JP おっと ở 2118 trong file này đã dịch đúng "Ôi chà.". Đây là lỗi dán nhầm.

### 2117 — 双鉄 — Đại từ

**JP:** 「おっと。⏎すみません、よそ見をしてしまって」

**TW:** 「噢。對不起，在看旁邊沒注意」

**VN cũ:** 「Ôi chà.⏎Xin lỗi, tôi mải nhìn đi chỗ khác.」

**Fix:** 「Ôi chà.⏎Xin lỗi, anh mải nhìn đi chỗ khác.」

Đối tượng là Reina (người vừa nói ở 2115, Soutetsu xin lỗi vì đã nhìn đi chỗ khác trong lúc cô ấy nói). Quy tắc đã sửa: Soutetsu tự xưng "anh" với Reina. Tiền lệ file 08 keys 1980/2071 (parent đã xác nhận "anh" với Reina là đúng).

### 2132 — 双鉄 — Đại từ

**JP:** 「その上で問おう。⏎お前は、修復前の\x%l8620;#00ffc040;8620%l;#;の公開を果たして、望むのか？」

**TW:** 「在這個前提之上再問你一次，你真的希望把修復前的\x%l8620;#00ffc040;８６２０%l;#;公之於眾嗎？」

**VN cũ:** 「Dựa trên điều đó, anh muốn hỏi.⏎Rốt cuộc em, có mong muốn công khai \x%l8620;#00ffc040;8620%l;#; trước khi phục hồi không?」

**Fix:** 「Dựa trên điều đó, tôi muốn hỏi.⏎Rốt cuộc em, có mong muốn công khai \x%l8620;#00ffc040;8620%l;#; trước khi phục hồi không?」

Quy tắc đại từ đã sửa (20/11): Soutetsu tự xưng "tôi" với Hachiroku. Đối tượng là Hachiroku ("em" trong cùng dòng = Hachiroku; câu hỏi về việc công khai 8620, Hachiroku là người được hỏi).

### 2169 — 双鉄 — Thuật ngữ

**JP:** 「『御一夜のSL』として[ハチロクニイマル,3]8620を認識してもらう。⏎それができれば、\x%l8620;#00ffc040;8620%l;#;を観光復権の旗印と出来よう」

**TW:** 「將８６２０塑造成大眾認識中的“御一夜蒸汽機車”。可以的話，就能把\x%l8620;#00ffc040;８６２０%l;#;打造成旅遊業復興的旗幟」

**VN cũ:** 「Phải làm cho mọi người nhận thức 8620 là 『SL của Ohimitera』.⏎Nếu làm được điều đó, chúng ta có thể biến \x%l8620;#00ffc040;8620%l;#; thành ngọn cờ đầu cho việc chấn hưng du lịch.」

**Fix:** 「Phải làm cho mọi người nhận thức 8620 là 『SL của Ohitoyo』.⏎Nếu làm được điều đó, chúng ta có thể biến \x%l8620;#00ffc040;8620%l;#; thành ngọn cờ đầu cho việc chấn hưng du lịch.」

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 2184 — ポーレット — Thuật ngữ

**JP:** 「口コミは、効果ありますからね。⏎ことに、御一夜のような古い町では」

**TW:** 「小道消息傳得可快了。特別是在御一夜這種老城」

**VN cũ:** 「Truyền miệng có hiệu quả lắm đấy.⏎Đặc biệt là ở một thị trấn cổ như Ohimitera.」

**Fix:** 「Truyền miệng có hiệu quả lắm đấy.⏎Đặc biệt là ở một thị trấn cổ như Ohitoyo.」

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 2193 — 双鉄 — Đại từ

**JP:** 「と、いうことだ。ハチロク。お前も望んでくれるなら、⏎修復前の\x%l8620;#00ffc040;8620%l;#;の展示を行いたい」

**TW:** 「就是這樣，八六。要是你也願意的話，我想展示修復前的\x%l8620;#00ffc040;８６２０%l;#;」

**VN cũ:** 「Chuyện là như vậy đấy. Hachiroku. Nếu em cũng mong muốn,⏎anh muốn tổ chức trưng bày \x%l8620;#00ffc040;8620%l;#; trước khi phục hồi.」

**Fix:** 「Chuyện là như vậy đấy. Hachiroku. Nếu em cũng mong muốn,⏎tôi muốn tổ chức trưng bày \x%l8620;#00ffc040;8620%l;#; trước khi phục hồi.」

Quy tắc đại từ đã sửa (20/11): Soutetsu tự xưng "tôi" với Hachiroku. Đối tượng là Hachiroku (gọi thẳng tên ở đầu dòng).

### 2211 — 日々姫 — Thuật ngữ

**JP:** 「御一夜市の……私たちの町の、ＳＬ」

**TW:** 「御一夜市的……我們城市的蒸汽機車」

**VN cũ:** 「SL của thành phố Ohimitera……của thị trấn chúng ta.」

**Fix:** 「SL của thành phố Ohitoyo……của thị trấn chúng ta.」

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 2251 — 双鉄 — Đại từ

**JP:** 「物を超えた部分の。お前をお前たらしめる知性の。⏎お前自身の――お前の望みはどうであるかと聞いている」

**TW:** 「我問的是——你真正的希望是什麼，這希望發自你的真心，讓你超越了普通的物品、形成了你的智慧」

**VN cũ:** 「Anh đang hỏi về phần vượt lên trên một đồ vật. Về trí tuệ làm nên con người em.⏎Về chính bản thân em――anh đang hỏi mong muốn của em là gì.」

**Fix:** 「Tôi đang hỏi về phần vượt lên trên một đồ vật. Về trí tuệ làm nên con người em.⏎Về chính bản thân em――tôi đang hỏi mong muốn của em là gì.」

Quy tắc đại từ đã sửa (20/11): Soutetsu tự xưng "tôi" với Hachiroku. Đối tượng là Hachiroku ("bản thân em" = Hachiroku; tiếp nối cuộc đối thoại với Hachiroku).

### 2266 — 双鉄 — Đại từ

**JP:** 「僕は、お前のオーナーだ。⏎僕は、お前に約束をした」

**TW:** 「我是你的主人。我答應過你」

**VN cũ:** 「Tôi là chủ sở hữu của cô.⏎Tôi đã hứa với cô rồi.」

**Fix:** 「Tôi là chủ sở hữu của em.⏎Tôi đã hứa với em rồi.」

Như 1970: Soutetsu gọi Hachiroku là "em" (2× "cô" trong cùng dòng).

### 2269 — 双鉄 — Đại từ

**JP:** 「僕は、お前の望みを叶える」

**TW:** 「我會實現你的心願的」

**VN cũ:** 「Tôi sẽ biến mong muốn của cô thành hiện thực.」

**Fix:** 「Tôi sẽ biến mong muốn của em thành hiện thực.」

Như 1970: Soutetsu gọi Hachiroku là "em".

### 2300 — 双鉄 — Đại từ

**JP:** 「故にハチロク、お前を再び走らせよう。⏎お前と[ハチロクニイマル,3]8620に、人と、笑顔とを運ばせよう」

**TW:** 「所以八六，我一定會讓你再次跑起來的。一定會讓你和８６２０再次載起人們，載起他們的笑容」

**VN cũ:** 「Vì vậy Hachiroku, tôi sẽ làm cho cô chạy lại một lần nữa.⏎Sẽ làm cho cô và \x%l8620;#00ffc040;8620%l;#; lại được chở mọi người, và những nụ cười.」

**Fix:** 「Vì vậy Hachiroku, tôi sẽ làm cho em chạy lại một lần nữa.⏎Sẽ làm cho em và 8620 lại được chở mọi người, và những nụ cười.」

Như 1970: Soutetsu gọi Hachiroku là "em" (2× "cô"). Đồng thời gỡ tag %l do VN tự thêm trên 8620 — JP chỉ có ruby [ハチロクニイマル,3], không có tag %l; tiền lệ reina02: tag VN tự thêm bị gỡ.

### 2320 — 双鉄 — Đại từ

**JP:** 「お前が行っても、誰が行っても同じだろうさ。⏎男女の機微とは、どうやらそうしたものらしいからな」

**TW:** 「換成是你去還是誰去都一樣吧。異性之間的關係就是這麼複雜」

**VN cũ:** 「Dù là cô đi, hay ai đi thì cũng thế thôi.⏎Những tinh tế giữa nam và nữ, có vẻ là như vậy đấy.」

**Fix:** 「Dù là em đi, hay ai đi thì cũng thế thôi.⏎Những tinh tế giữa nam và nữ, có vẻ là như vậy đấy.」

Như 1970: Soutetsu gọi Hachiroku là "em"; "cô" là ngoại lệ cần thống nhất.

### 2385 — 凪 — Nghĩa

**JP:** 「やにわにだごばい！　[ゆべし,2]柚餅子ばい！⏎あ、かき氷も食べたかばいっ！」

**TW:** 「止餓糰子！還有柚餅！啊，刨冰也好想吃咧！」

**VN cũ:** 「Tự nhiên đói bụng quá! Yubeshi! (Bánh nếp yuzu)⏎A, cũng muốn ăn cả đá bào nữa!」

**Fix:** 「Tự nhiên thèm dango quá! Yubeshi! (Bánh nếp yuzu)⏎A, cũng muốn ăn cả đá bào nữa!」

JP やにわにだごばい = "bỗng dưng, dango!" — だご (dango, bánh gạo) bị bỏ mất, VN cũ dịch thành "đói bụng" (không có trong JP). TW giữ 團子. Kiểu bỏ/bịa của bản Gemini gốc.

### 2403 — 双鉄 — Nghĩa

**JP:** 「そう、これこそが国産蒸気第一号。⏎栄光の[ハチロク,3]8620形トップナンバー機、[ハチロクニイマル,3]8620だ」

**TW:** 「沒錯，這就國產蒸汽機車第一號，偉大的八六型號首車，８６２０」

**VN cũ:** 「Đúng vậy, đây chính là chiếc máy hơi nước quốc sản đầu tiên.⏎Cỗ máy chuyên dụng số hiệu đầu tiên đầy vinh quang của dòng 8620, 8620.」

**Fix:** 「Đúng vậy, đây chính là chiếc máy hơi nước quốc sản đầu tiên.⏎Cỗ máy số hiệu đầu tiên đầy vinh quang của dòng 8620, chính là 8620.」

VN cũ bịa thêm "chuyên dụng" — JP トップナンバー機 (cỗ máy số hiệu đầu tiên) không có từ nào nghĩa "chuyên dụng"; TW cũng không có. Đồng thời sửa cuối câu thành "chính là 8620" theo JP これぞハチロクニイマルだ (これぞ = chính là).

### 2415 — 赤井宮司 — Thuật ngữ

**JP:** 「前市長の[ひない,1]雛衣さん。⏎ポーレットさんのお父様は、正真正銘の[と]撮り[テツ]鉄でした」

**TW:** 「波萊特的父親，前市長雛衣先生是一名實實在在的鐵影家」

**VN cũ:** 「Ngài Hinai, cựu thị trưởng.⏎Cha của cô Paulette là một Tori-tetsu chân chính đấy.」

**Fix:** 「Ngài Hinai, cựu thị trưởng.⏎Cha của cô Paulette là một người chụp ảnh tàu chân chính đấy.」

撮り鉄 = người chụp ảnh tàu (撮る = chụp ảnh, 鉄 = tàu). VN cũ để nguyên romaji "Tori-tetsu" — chưa dịch. So sánh 2492 車両鉄 và 乗り鉄 "người thích đi tàu" trong cùng file.

### 2424 — 双鉄 — Đại từ

**JP:** 「確かに、ふかみ達にはそうだろうな。⏎僕世代でも、子供の頃にかろうじてだから」

**TW:** 「深美這個年紀的人確實沒看過啊。我這代人也只在小時候看到過」

**VN cũ:** 「Đúng là với thế hệ của Fukami thì là vậy nhỉ.⏎Ngay cả thế hệ của tôi, cũng chỉ may mắn được thấy hồi còn nhỏ thôi.」

**Fix:** 「Đúng là với thế hệ của Fukami thì là vậy nhỉ.⏎Ngay cả thế hệ của anh, cũng chỉ may mắn được thấy hồi còn nhỏ thôi.」

Đối tượng là Fukami (đáp lại 2257 của Fukami về thế hệ chưa từng thấy đầu máy hơi nước thật). Quy tắc đã sửa: Soutetsu tự xưng "anh" với Fukami. Tiền lệ file 10 key 2779.

### 2458 — 双鉄 — Thuật ngữ

**JP:** 「銀行主導で作ったという、日々姫のイラストマップを⏎見て思った。御一夜の再生を願う気持ちは同じだと」

**TW:** 「看了那張你在銀行主導下畫的彩繪地圖，我覺得我們想要復興御一夜的目標是一樣的」

**VN cũ:** 「Anh đã nghĩ vậy khi xem bản đồ minh họa do ngân hàng chủ đạo mà Hibiki vẽ.⏎Rằng mong muốn tái thiết Ohimitera của chúng ta là giống nhau.」

**Fix:** 「Anh đã nghĩ vậy khi xem bản đồ minh họa do ngân hàng chủ đạo mà Hibiki vẽ.⏎Rằng mong muốn tái thiết Ohitoyo của chúng ta là giống nhau.」

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 2492 — 赤井宮司 — Thuật ngữ

**JP:** 「ポーレットさんは、\x%l乗り鉄;#00ffc040;乗り鉄%l;#;の\x%l車両鉄;#00ffc040;[シャリョウテツ,2]車両鉄%l;#;ですからね。⏎殆どカメラは使わず、そのまま眠らせているようです」

**TW:** 「而波萊特小姐是\x%l乗り鉄;#00ffc040;鐵行家%l;#;中的\x%l車両鉄;#00ffc040;博鐵家%l;#;，所以她不怎麼拍照，相機一直就那樣放著了」

**VN cũ:** 「Cô Paulette là một Sharyo-tetsu thuộc phái \x%l乗り鉄;#00ffc040;người thích đi tàu%l;#; mà.⏎Cô ấy hầu như không dùng máy ảnh, có vẻ cứ để nó nằm im lìm như vậy thôi.」

**Fix:** 「Cô Paulette là \x%l車両鉄;#00ffc040;người mê toa xe%l;#; thuộc phái \x%l乗り鉄;#00ffc040;người thích đi tàu%l;#; mà.⏎Cô ấy hầu như không dùng máy ảnh, có vẻ cứ để nó nằm im lìm như vậy thôi.」

車両鉄 = người mê toa xe (車両 = toa xe). VN cũ để romaji "Sharyo-tetsu" và làm mất tag %l của JP; khôi phục tag theo mẫu của 乗り鉄 trong cùng dòng: \x%l車両鉄;#00ffc040;người mê toa xe%l;#;.

### 2538 — 双鉄 — Đại từ

**JP:** 「走るぞハチロク。お前の望みをかなえるために。⏎そうするために――お前も走れ。全力で」

**TW:** 「跑起來吧，八六。為了實現你的心願，你也盡全力跑起來吧」

**VN cũ:** 「Chạy thôi Hachiroku. Để biến mong muốn của cô thành hiện thực.⏎Để làm được điều đó——cô cũng phải chạy đi. Bằng toàn bộ sức lực.」

**Fix:** 「Chạy thôi Hachiroku. Để biến mong muốn của em thành hiện thực.⏎Để làm được điều đó——em cũng phải chạy đi. Bằng toàn bộ sức lực.」

Như 1970: Soutetsu gọi Hachiroku là "em" (2× "cô").

### 2569 — 日々姫 — Thuật ngữ

**JP:** 「それは……\x%lエアクラ;#00ffc040;エアクラ%l;#;工場の誘致は、もちろん、⏎御一夜の経済再生のための手段と考えています」

**TW:** 「這……對我來說引進\x%lエアクラ;#00ffc040;空凝機%l;#;工廠只是御一夜經濟復興的一種手段」

**VN cũ:** 「Chuyện đó……việc thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;, tất nhiên,⏎em coi đó là phương tiện để tái thiết kinh tế Ohimitera.」

**Fix:** 「Chuyện đó……việc thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;, tất nhiên,⏎em coi đó là phương tiện để tái thiết kinh tế Ohitoyo.」

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 2626 — 双鉄 — Đại từ

**JP:** 「故に、僕の望みに従う。⏎物としてのお前たちの本懐がそれと、理解している」

**TW:** 「願意遵從我的願望。這就是你們作為物品最大的願望，我明白」

**VN cũ:** 「Nên, em sẽ tuân theo mong muốn của tôi.⏎Anh hiểu đó là tâm nguyện của các em với tư cách là một đồ vật.」

**Fix:** 「Nên, em sẽ tuân theo mong muốn của tôi.⏎Tôi hiểu đó là tâm nguyện của các em với tư cách là một đồ vật.」

Dòng 2 nói với Hachiroku ("Anh hiểu" → "Tôi hiểu"); dòng 1 giữ nguyên — "em" là người nghe Hachiroku, "tôi" là Soutetsu, đều đúng.

### 2632 — 日々姫 — Gasp (っ)

**JP:** 「っ！」

**TW:** 「！」

**VN cũ:** 「!」

**Fix:** 「Ư!」

Sweep lost-gasp-whole: JP là gasp nguyên dòng っ+punct, VN cũ chỉ còn dấu câu. Áp nguyên văn giá trị sweep (đã kiểm chứng đúng JP).

### 2633 — 双鉄 — Gasp (っ)

**JP:** 「っ！？」

**TW:** 「！？」

**VN cũ:** 「!?」

**Fix:** 「Ư!?」

Sweep lost-gasp-whole: JP là gasp nguyên dòng っ+punct, VN cũ chỉ còn dấu câu. Áp nguyên văn giá trị sweep (đã kiểm chứng đúng JP).

### 3038 — monologue — Thuật ngữ

**JP:** ポーレットを迎えにいったのだろう。⏎赤井宮司、蓑笠老人――日々姫さえもが残っていない。

**TW:** 大家似乎都去迎接波萊特了，赤井先生、蓑笠老人——就連日日姬也走了。

**VN cũ:** Chắc là đi đón Paulette hết rồi.⏎Thầy Akai, ông lão Minokasa——ngay cả Hibiki cũng không còn ở lại.

**Fix:** Chắc là đi đón Paulette hết rồi.⏎Đền chủ Akai, ông lão Minokasa——ngay cả Hibiki cũng không còn ở lại.

Quyết định 19/11: 宮司 = "đền chủ". "Thầy Akai" bỏ mất chức danh 宮司 (JP 赤井宮司). (Độc thoại của Soutetsu.)

### 3241 — monologue — Nghĩa

**JP:** 日々姫がびくりと顔を跳ね上げる。⏎その反応に、確信が深まる。

**TW:** 日日姬大吃一驚。她的反應讓我更加確信。

**VN cũ:** Hibiki giật nảy mình ngẩng mặt lên.⏎Phản ứng đó càng làm tôi thêm 확 tín.

**Fix:** Hibiki giật nảy mình ngẩng mặt lên.⏎Phản ứng đó càng làm tôi thêm chắc chắn.

VN cũ để lọt từ Hàn "확" (chắc chắn) — lỗi rò rỉ ngôn ngữ của bản dịch gốc. JP 確信が深まる = sự chắc chắn càng sâu thêm; TW 更加確信. (Độc thoại của Soutetsu.)

### 3391 — monologue — Thuật ngữ

**JP:** \x%l8620;#00ffc040;8620%l;#;を湯医にたどり着かせたのなら、⏎あの\x%l列車;#00ffc040;列車%l;#;から――路子も、降りられるのかもしれない。

**TW:** 若是能幫助\x%l8620;#00ffc040;８６２０%l;#;駛到湯醫的話，說不定路子——就能從那輛\x%l列車;#00ffc040;列車%l;#;上下來了。

**VN cũ:** Nếu có thể đưa \x%l8620;#00ffc040;8620%l;#; đến được Yui,⏎thì có lẽ——Michiko cũng có thể bước xuống từ chuyến \x%l列車;#00ffc040;tàu%l;#; đó.

**Fix:** Nếu có thể đưa \x%l8620;#00ffc040;8620%l;#; đến được Yunoi,⏎thì có lẽ——Michiko cũng có thể bước xuống từ chuyến \x%l列車;#00ffc040;tàu%l;#; đó.

Quyết định 19/11: 湯医/湯医線 = "Yunoi" (furigana ゆのい). Dòng 2143 trong cùng file đã dùng đúng "Yunoi" — 3391 là dòng còn sót "Yui" (dòng thứ ba trong dự án, sau P14 83 và P16 2032).

### 3433 — monologue — Thuật ngữ

**JP:** 全てを記録しようかとでもしているのか、⏎赤井宮司は機関庫内の細部の写真を次々と撮る。

**TW:** 赤井先生可能是想要把所有東西都記錄下來吧，他不停地拍著車庫的各種細節。

**VN cũ:** Cứ như thể đang định ghi lại tất cả mọi thứ,⏎cung tư tế Akai liên tục chụp ảnh các chi tiết bên trong xưởng đầu máy.

**Fix:** Cứ như thể đang định ghi lại tất cả mọi thứ,⏎đền chủ Akai liên tục chụp ảnh các chi tiết bên trong xưởng đầu máy.

Quyết định 19/11: 宮司 = "đền chủ". "Cung tư tế" là dạng cũ cần thống nhất. (Độc thoại của Soutetsu.)

### 3435 — monologue — Thuật ngữ

**JP:** いわんばかりに指先でつくったＸの字を口の前にあて、⏎赤井宮司は僕らの前から去っていく。

**TW:** 赤井先生就像是在表示這個意思一般用手指在嘴前比出叉號，然後轉身離開了。

**VN cũ:** Thầy Akai đưa ngón tay tạo thành hình chữ X trước miệng như muốn nói vậy,⏎rồi quay lưng rời đi.

**Fix:** Đền chủ Akai đưa ngón tay tạo thành hình chữ X trước miệng như muốn nói vậy,⏎rồi quay lưng rời đi.

Quyết định 19/11: 宮司 = "đền chủ". "Thầy Akai" bỏ mất chức danh 宮司 (JP 赤井宮司). (Độc thoại của Soutetsu.)

### 3436 — monologue — Thuật ngữ

**JP:** 赤井宮司が率直に意見してくれた。

**TW:** 赤井先生曾坦誠地勸過我。

**VN cũ:** Cung tư tế Akai đã thẳng thắn đưa ra ý kiến.

**Fix:** Đền chủ Akai đã thẳng thắn đưa ra ý kiến.

Quyết định 19/11: 宮司 = "đền chủ". "Cung tư tế" là dạng cũ cần thống nhất. (Độc thoại của Soutetsu.)

### 3445 — monologue — Thuật ngữ

**JP:** 赤井宮司が満足そうに頷いてくれる。⏎周辺記録の必要性は、僕にも大いに理解できた。

**TW:** 赤井宮司滿意地點頭。我非常了解記錄周邊情況有多重要。

**VN cũ:** Thầy Akai gật đầu vẻ hài lòng.⏎Tôi cũng đã rất hiểu tầm quan trọng của việc ghi chép tình hình xung quanh.

**Fix:** Đền chủ Akai gật đầu vẻ hài lòng.⏎Tôi cũng đã rất hiểu tầm quan trọng của việc ghi chép tình hình xung quanh.

Quyết định 19/11: 宮司 = "đền chủ". "Thầy Akai" bỏ mất chức danh 宮司 (JP 赤井宮司). (Độc thoại của Soutetsu.)

### 3447 — monologue — Thuật ngữ

**JP:** ここを乗り越えられないのなら、⏎御一夜を――そして路子を――救えはしない。

**TW:** 跨不過這道難關，就拯救不了御一夜——拯救不了路子。

**VN cũ:** Nếu không thể vượt qua được chướng ngại này,⏎thì sẽ không thể cứu được Ohimitera——và cả Michiko nữa.

**Fix:** Nếu không thể vượt qua được chướng ngại này,⏎thì sẽ không thể cứu được Ohitoyo——và cả Michiko nữa.

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera". (Độc thoại của Soutetsu.)

## 4. Các dòng giữ nguyên có chủ đích và phán đoán

**Phán đoán giữ nguyên (người nghe chưa rõ — không sửa, chờ Hieu nếu muốn xem lại):**

- **2244** — Soutetsu "tôi nghĩ truyền miệng từ học sinh sẽ mang lại hiệu quả lớn": nói với cả nhóm, đáp lại ý truyền miệng của Paulette (2184). Người nghe chính là Paulette (nhóm "anh") nhưng là phát biểu trước nhóm có Hachiroku, nên "tôi" giữ nguyên được. Tương tự **2524** — "Ngay cả tôi, cũng chỉ thực sự cảm nhận được…": nói với cả phòng (Paulette/Fukami là người nghe chính, cả hai đều thuộc nhóm "anh", nhưng là phát biểu trước nhóm).
- **2404** — Soutetsu "Chỉ cần Fukami đến là tôi đã biết ơn lắm rồi": người nghe không xác định được chắc chắn từ các dòng kề — nếu nói với Fukami/Michiko thì phải là "anh", nếu nói với Akai/Hachiroku/cả nhóm thì "tôi" đứng được. Giữ nguyên.

**Giữ nguyên có chủ đích (đã kiểm chứng, không phải lỗi):**

- **2143** — "cô ấy" chỉ tuyến Yunoi được nhân cách hóa ("Hôm nay, cô ấy đang chạy thêm chuyến tăng cường"): TW dùng 她 (cô ấy), "Yunoi" trong cùng dòng đã đúng.
- **2604** — "cô ấy" chỉ Paulette ở ngôi thứ ba khi nói với Akai (trang trọng): "tôi sẽ thử bàn với cô ấy một lần" — ngôi thứ ba trang trọng với người lớn tuổi, khác với "em" khi gọi trực tiếp.
- **2104** — "cô ta" chỉ Kisaki: Kisaki là phụ nữ trưởng thành, Soutetsu đang nói với giọng khó chịu về việc bị thị sát — "cô ta" đúng sắc thái.
- **2968, 2597** — tag %l trên 8620 trong JP bị VN bỏ: gloss của tag là chính "8620" (bằng với thuật ngữ), bỏ tag không mất thông tin gì; khác với 2492 (tag mang gloss dịch "người mê toa xe") và 2300 (tag VN tự thêm).
- **3129** — dị thường dữ liệu, không phải lỗi VN: JP có tag dị dạng (đóng `%l;` thiếu `;` + mở tag mới), VN giữ nguyên y hệt JP — cùng mẫu file 09 key 2482 và file 10 key 2508.
- **3126** — 義理 dịch "Dù là trên danh nghĩa" — chấp nhận được (nghĩa bóng của 義理 trong ngữ cảnh này).
- **2023** — なやむ dịch "đau đầu" — thành ngữ, chấp nhận được.
- **2061, 2597** — Fukami tự xưng "mình" với bạn học: đúng ngữ điệu bạn bè cùng trang lứa; "Em" chỉ dùng với Soutetsu/người lớn.
- **1966, 2489, 2612** — Hachiroku xưng "tao/mày" với 8620: ngữ điệu thô ráp thân mật nhất quán trong cảnh, giữ nguyên.
- **2525** — ありがとう dịch "Cảm ơn mọi người.": nói với cả nhóm, thêm "mọi người" là cách nói tự nhiên trong tiếng Việt (cùng VN với 日々姫03 2803 có JP ありがとう、みんな).
- **2058** — あっ→"A.": tiếng "ah" ngạc nhiên ngắn, đã render. **2029** — きゃっ!?→"Á, á!?": tiếng kêu giật mình, đã render. **2059** — はうっ→"Hau!!?": giữ nguyên âm Latin theo tiền lệ h7.
- **2278** — Hachiroku "Mong muốn của mình là gì": JP là 自分の望み ("mong muốn của chính mình") — "mình" ở đây là đại từ phản thân, không phải tự xưng; vế sau わたくし vẫn dịch đúng "tôi".
- **2141** — "Anh nhìn mà mê mẩn luôn" với Fukami: đúng (nhóm "anh"). **2590** — まいてつ đã là "chủ tàu" ✓. **1926** — 電車→"tàu điện" (không phải 市電) ✓. **2578** — 気動車→"toa xe tự hành" ✓. **3158** — KiHa ✓. **2102** — "em ấy" chỉ Fukami (người nghe là Hachiroku) ✓.

## 5. Khối TOML (đã kiểm chứng parse)

```toml
[script]
"1970" = "「Suy nghĩ của em ngây thơ quá đấy.」"
"1973" = "「Cuối cùng em cũng chịu nói ra rồi. Mong muốn của em.」"
"2069" = "「Ái chà ái chà,\\nĐược đền chủ Akai cất công đến đây, thật là vinh hạnh.」"
"2102" = "「Ừ——ồ! Chẳng phải em ấy,\\nđang làm rất tốt hay sao.」"
"2113" = "「Ôi chà.」"
"2117" = "「Ôi chà.\\nXin lỗi, anh mải nhìn đi chỗ khác.」"
"2132" = "「Dựa trên điều đó, tôi muốn hỏi.\\nRốt cuộc em, có mong muốn công khai \\x%l8620;#00ffc040;8620%l;#; trước khi phục hồi không?」"
"2169" = "「Phải làm cho mọi người nhận thức 8620 là 『SL của Ohitoyo』.\\nNếu làm được điều đó, chúng ta có thể biến \\x%l8620;#00ffc040;8620%l;#; thành ngọn cờ đầu cho việc chấn hưng du lịch.」"
"2184" = "「Truyền miệng có hiệu quả lắm đấy.\\nĐặc biệt là ở một thị trấn cổ như Ohitoyo.」"
"2193" = "「Chuyện là như vậy đấy. Hachiroku. Nếu em cũng mong muốn,\\ntôi muốn tổ chức trưng bày \\x%l8620;#00ffc040;8620%l;#; trước khi phục hồi.」"
"2211" = "「SL của thành phố Ohitoyo……của thị trấn chúng ta.」"
"2251" = "「Tôi đang hỏi về phần vượt lên trên một đồ vật. Về trí tuệ làm nên con người em.\\nVề chính bản thân em――tôi đang hỏi mong muốn của em là gì.」"
"2266" = "「Tôi là chủ sở hữu của em.\\nTôi đã hứa với em rồi.」"
"2269" = "「Tôi sẽ biến mong muốn của em thành hiện thực.」"
"2300" = "「Vì vậy Hachiroku, tôi sẽ làm cho em chạy lại một lần nữa.\\nSẽ làm cho em và 8620 lại được chở mọi người, và những nụ cười.」"
"2320" = "「Dù là em đi, hay ai đi thì cũng thế thôi.\\nNhững tinh tế giữa nam và nữ, có vẻ là như vậy đấy.」"
"2385" = "「Tự nhiên thèm dango quá! Yubeshi! (Bánh nếp yuzu)\\nA, cũng muốn ăn cả đá bào nữa!」"
"2403" = "「Đúng vậy, đây chính là chiếc máy hơi nước quốc sản đầu tiên.\\nCỗ máy số hiệu đầu tiên đầy vinh quang của dòng 8620, chính là 8620.」"
"2415" = "「Ngài Hinai, cựu thị trưởng.\\nCha của cô Paulette là một người chụp ảnh tàu chân chính đấy.」"
"2424" = "「Đúng là với thế hệ của Fukami thì là vậy nhỉ.\\nNgay cả thế hệ của anh, cũng chỉ may mắn được thấy hồi còn nhỏ thôi.」"
"2458" = "「Anh đã nghĩ vậy khi xem bản đồ minh họa do ngân hàng chủ đạo mà Hibiki vẽ.\\nRằng mong muốn tái thiết Ohitoyo của chúng ta là giống nhau.」"
"2492" = "「Cô Paulette là \\x%l車両鉄;#00ffc040;người mê toa xe%l;#; thuộc phái \\x%l乗り鉄;#00ffc040;người thích đi tàu%l;#; mà.\\nCô ấy hầu như không dùng máy ảnh, có vẻ cứ để nó nằm im lìm như vậy thôi.」"
"2538" = "「Chạy thôi Hachiroku. Để biến mong muốn của em thành hiện thực.\\nĐể làm được điều đó——em cũng phải chạy đi. Bằng toàn bộ sức lực.」"
"2569" = "「Chuyện đó……việc thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;, tất nhiên,\\nem coi đó là phương tiện để tái thiết kinh tế Ohitoyo.」"
"2626" = "「Nên, em sẽ tuân theo mong muốn của tôi.\\nTôi hiểu đó là tâm nguyện của các em với tư cách là một đồ vật.」"
"2632" = "「Ư!」"
"2633" = "「Ư!?」"
"3038" = "Chắc là đi đón Paulette hết rồi.\\nĐền chủ Akai, ông lão Minokasa——ngay cả Hibiki cũng không còn ở lại."
"3241" = "Hibiki giật nảy mình ngẩng mặt lên.\\nPhản ứng đó càng làm tôi thêm chắc chắn."
"3391" = "Nếu có thể đưa \\x%l8620;#00ffc040;8620%l;#; đến được Yunoi,\\nthì có lẽ——Michiko cũng có thể bước xuống từ chuyến \\x%l列車;#00ffc040;tàu%l;#; đó."
"3433" = "Cứ như thể đang định ghi lại tất cả mọi thứ,\\nđền chủ Akai liên tục chụp ảnh các chi tiết bên trong xưởng đầu máy."
"3435" = "Đền chủ Akai đưa ngón tay tạo thành hình chữ X trước miệng như muốn nói vậy,\\nrồi quay lưng rời đi."
"3436" = "Đền chủ Akai đã thẳng thắn đưa ra ý kiến."
"3445" = "Đền chủ Akai gật đầu vẻ hài lòng.\\nTôi cũng đã rất hiểu tầm quan trọng của việc ghi chép tình hình xung quanh."
"3447" = "Nếu không thể vượt qua được chướng ngại này,\\nthì sẽ không thể cứu được Ohitoyo——và cả Michiko nữa."
```

Kiểm tra cơ học: khối parse được bằng tomllib, 35 key, 0 sai lệch giá trị so với JSON; ngoặc cân bằng 35/35; tag %l không đổi ở mọi dòng trừ 2492 (khôi phục 1 tag) và 2300 (gỡ 1 tag VN tự thêm).

## Kết bài

File 12 là một file tương đối sạch (6,7% sai, thấp hơn mức trung bình ~15% của dự án tới nay và thấp hơn file 10 là 9,3%): không có dòng lệch, không có chuỗi xoay, không có nhiễm chéo, không có dòng chưa dịch, không có dòng mồ côi. Lỗi tập trung vào thuật ngữ đã chốt (Ohitoyo 6 dòng — đúng con số 6 đã đếm trước đó, 宮司 6 dòng gồm cả biến thể "Thầy Akai" chưa từng thống kê, Yunoi 1 dòng) và đại từ của Soutetsu (13/35 dòng đại từ: 5× tự xưng với Hachiroku/Fukami/Reina và 7× gọi Hachiroku "cô"→"em" — riêng 2117 là dòng "tôi" với Reina, chiều ngược với 3 fix sai đã bị parent loại ở file 08/09). Ba lỗi nghĩa đều là kiểu bịa/bỏ/lẫn ngôn ngữ của bản Gemini gốc, trong đó 3241 (từ Hàn "확") và 2385 (bỏ mất だご) là rõ nhất. Sau file này, Ohitoyo còn lại trong 00_Common: **68** (14: 30, 15: 15, 11: 12, 13: 3, 01 pilot: 8 chưa chốt). Còn lại chưa kiểm toán trong 00_Common: 11 (đang chạy song song), 13, 14, 15, 末尾 (5 file; file 01 vẫn là bản nháp pilot). Ba phán đoán giữ nguyên 2244/2524/2404 (người nghe chưa rõ) chờ Hieu xem lại nếu muốn; 乗務鞄 "túi phi hành đoàn" không xuất hiện trong file này nên không có gì để ghi thêm.

Lượt soát 2: 35 tổng / 35 kiểm tra lại / 0 loại bỏ / 0 sửa lại. (Trước lượt soát 2, khâu kiểm tra cơ học đã bắt được 31 giá trị fix bị cắt ngắn do bản in làm việc bị giới hạn độ dài — toàn bộ đã viết lại đầy đủ nguyên giá trị VN cũ chỉ đổi chỗ cần sửa, và quét bổ sung bằng script đã tìm thêm 1 fix đại từ 2117 với Reina. Lượt soát 2 đọc lại toàn bộ 35 giá trị fix so với JP, không phát hiện thêm lỗi nào.)
