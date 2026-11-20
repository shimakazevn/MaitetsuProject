# Audit — 稀咲h3_チャイナドレスでおもてなし.txt.toml (06_Kisaki)

- File: `06_Kisaki/稀咲h3_チャイナドレスでおもてなし.txt.toml` (TOML-2: `#U7a00#U54b2h3_#U30c1#U30e3#U30a4#U30ca#U30c9#U30ec#U30b9#U3067#U304a#U3082#U3066#U306a#U3057.txt.toml`)
- Route: 06_Kisaki. Nội dung: Kisaki tới xưởng rượu nhà Migita tham quan (thử rượu tươi chưa chưng cất, giải thích về men koji/citric), rồi hẹn hò ăn crepe, thử sườn xám Trọng Quốc may đo, cảnh H (sườn xám xuyên thấu, quan hệ trên sofa).
- Đọc: **662/662 dòng** (keys 2300–3234, section `script`), đọc từng dòng JP + TW + VN đối chiếu. CSV3 khớp TOML tuyệt đối (chỉ khác 371 dòng TOML-2 làm phẳng `\n` thành khoảng trắng — theo quy tắc, CSV3 là chuẩn cho fix list).
- **Sai: 75/662 (11,3%)**.
- Phân loại: đại từ 50, gasp 16 (11 từ sweep + 5 sweep bỏ sót), sai nghĩa 4, thuật ngữ 3, SFX 1, dấu câu 1.
- **0 lệch dòng / 0 chuỗi xoay / 0 nhiễm chéo / 0 dòng mồ côi / 0 dòng chưa dịch / 0 khóa trùng.** Không có dòng VN nào là lời thoại của file khác; không có VN lặp ở 2 key; không có ô VN trống.
- TOML md5: `3bccfb4626ff9b0e014a8655d1091f7e` — không có bản trùng (đã kiểm tra md5 toàn bộ sources/toml2/, không file nào khác cùng md5).
- Cơ sở tổng: **132 file / 6.013 dòng sai** (đã kiểm chứng trực tiếp với dòng tổng cuối của ROUTE-AUDIT.md — khớp với brief, không cần rebase).

## §1. Đại từ — Soutetsu "anh"→"tôi" với Kisaki (50 dòng, lỗi hệ thống)

Soutetsu tự xưng "anh" **50/50 lần** trong file này (thoại 49 + độc thoại 1, key 3006) — **không có lần nào dùng đúng "tôi"**. Theo quy tắc đã sửa (Soutetsu là "tôi" với Hachiroku/Mayami/Minokasa/**Kisaki**), cả 50 đều sai. Người nghe đều là Kisaki (toàn bộ thoại 双鉄 trong file đều nói với Kisaki; không có nhân vật thứ ba nào lên tiếng). Đã kiểm chứng bằng quét máy toàn file (chuẩn hóa `\n` trước khi quét — lưu ý: `\n` dạng chữ trong CSV3 làm regex `\banh\b` bỏ sót các "anh" đứng ngay sau xuống dòng, 2 dòng 2592/2428 suýt bị sót; đã quét lại và bắt đủ 50).

Kisaki tự xưng "em" với Soutetsu trong **toàn bộ** thoại của cô (0 lần "tôi" — đã quét máy) — đúng theo tiền lệ (Kisaki "em" với Soutetsu, "tôi" với Paulette), không sửa. Kisaki gọi Soutetsu "anh Soutetsu" 33 lần — giữ nguyên theo tiền lệ file 稀咲02 (10 lần "anh Soutetsu" được giữ, đã cờ cho Hieu); xem §5.

## §2. Thuật ngữ + sai nghĩa

- 御一夜→Ohitoyo: 4 dòng trong file (2648, 3099, 2740, 2302 — 2302 tính vào đại từ). Đây là toàn bộ "Ohimitera" trong file (đã quét máy).
- 2972: 反冥 dịch sai + エアクラ→"Aircra" (xem chi tiết từng dòng dưới).
- 2468/1550/3330: 3 lỗi nghĩa/diễn đạt (xem chi tiết từng dòng dưới).

## §3. Gasp っ — sweep kiểm chứng + 5 dòng sweep bỏ sót

Sweep có **13 mục** cho file này (đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`): 11 fix áp nguyên (1552, 2003, 2161, 2257, 2809, 2810, 2813, 2814, 2824, 2826, 3143), 2 already-rendered (3373, 3483 — không thêm Ư). Lưu ý 2003: bản sweep dùng khoảng trắng ở chỗ CSV3 có `\n` — đã chỉnh lại để Ư nằm cuối dòng 1 (đúng vị trí っ…… trong JP), giữ nguyên `\n` của CSV3.

Quét bổ sung toàn bộ dòng JP chứa っ: bắt thêm **5 gasp sweep bỏ sót** (2188, 2218, 2820, 2170, 2253) — đều là token gasp ～～+っ hoặc っ đầu dòng mà VN bỏ mất hẳn, cùng mẫu với các fix sweep đã xác nhận (2824/2826). Không còn gasp nào sót sau đợt quét này.

**Giữ nguyên theo quy ước toàn dự án (đã có tiền lệ gộp, parent-verified trong ROUTE-AUDIT.md):** あっ→"A"/"Á" (2234, 2242, 2241, 2197, 2225, 2195, 2252, 2675, 2755, 2160, 2165, 2223); ああっ→"a a" (2260, 2195 — tiền lệ hachiroku-h5/fukamih3, っ bỏ trước ！); はうっ→"Hau" (2239); はぁっ→"Ha"/"hà" (2223, 2206); んっ→"Ưm"/"ưm" (2261, 2252, 2283, 2077, 1538); ううっ→"Ư ư" (2256); んううっ→"ưm" (quy ước file, tiền lệ 1285); っ nhấn mạnh dính từ nội dung (鉄っ, それっ, ちからっ, ささえてっ, こしっ, 来たっ, そこっ, 好きっ, いくっ, ボクっ, もっとぉ→"nữa đi" (vần dài đã diễn), けどっ, むりっ, がまんっ — không thêm Ư); SFX đã diễn (ちゅっ→"Chụt", ごちゅっ/ずぶっ→"Phập", ごくっ→"Ực", ごくりっ→"Ực", （ぐいっ）→"Thúc" v.v.); っ――→―― (dashes diễn cut-off, tiền lệ あっ――→"A——": 1538, 2187, 3373 already-rendered, 2189/2203 ふぁっ――→"Fu…… a"); ひあ/ひゃ family giữ ngẫu hứng theo nhân vật + ngữ cảnh (Hieu 20/11 — không thống nhất): ひあっ→"I a", ひゃうっっ→"Hya!!?", ひゃんっ→"Hyan", ひゅっ→"Hưu", ひゅあっ→"Hyua", ひウっ→"I ư".

Lưu ý về 2240/2279/2116/2277/2278/2398 (moan dài + っ cuối: ふゅぁぁあああんんんっ→"Phuaaaaưm!", んんんっっ→"Ưm ưm", きゅううううううううううんんんっ→"rồiiiiii" v.v.): giữ nguyên — っ dính vào từ moan mà VN đã diễn thành từ (khác với token gasp ～～+っ độc lập của sweep); tiền lệ んううっ→"ưm" giữ (quy ước file, ROUTE-AUDIT.md).

## §4. Fa/fu — KHÔNG sửa trong audit này, để đợt thống nhất

Các dòng ふぁ/ふあ/ふうっ/ふっ trong file dùng lẫn lộn "phùa"/"phù"/"Phua"/"Fua"/"Fu…… a"/"phu, a" (mâu thuẫn phùa-vs-phù toàn dự án vẫn đang chờ Hieu; tiền lệ ハチロクh6 + 日々姫h1: fa/fu để đợt thống nhất, không sửa trong audit). Liệt kê để đợt thống nhất xử lý một lượt: 2207 (ぷぁ→"Pha"), 2189 (ふぁっ→"Fu…… a"), 2203 (ふぁ→"fu, a"), 2255 (ふあっ→"Fua!"), 2254 (ふあっ→"Phua!", ふ、あっ→"phu, á"), 2253 (ふあっ→"Phua"), 2188 (ふうっ→"Phù", ふぁっ→"phua"), 2201 (ふっ→"phù", ふうっ→"phù"), 2170 (ふぁっ→"phua", ふうっ→"phù"), 3808 (ふあっ→"phua"), 1538 (ふあっ→"Phua"), 2120 (ふあっ→"Phua"), 2152 (ふあっ→"phua", かふっ→"khaphu"), 2360 (ふあっ→"phua"), 2252 (ふあっ→"Phua"), 2225 (ふあっ→"phua"), 2195 (ふあっ→"phua"), 1988 (きゃふっ→"kya phu"). (ふっ ngắn →"fu"/"phu" và ふゅぁぁあああんんんっ→"Phuaaaaưm!" giữ nguyên — không nằm trong mâu thuẫn phùa/phù.)

## §5. Cờ chờ Hieu / để đợt thống nhất (không tự quyết)

1. **Kisaki gọi Soutetsu "anh Soutetsu" (33 dòng)** — brief ghi Kisaki gọi Soutetsu "cậu" hoặc tên trần (Common 14), nhưng toàn bộ file Kisaki (kể cả 稀咲02: 10 lần) đều dùng "anh Soutetsu" nhất quán. Giữ nguyên theo tiền lệ file 02; Hieu quyết xem có đổi sang "cậu Soutetsu"/tên trần toàn tuyến Kisaki hay không (đợt thống nhất).
2. **Fa/fu** — xem §4 (17+ dòng).
3. **2740: 旧帝鉄総裁 → "cựu Tổng giám đốc Đường sắt Hoàng gia"** — 帝鉄 dạng đầy đủ, để đợt thống nhất (tiền lệ 日々姫02: 6 dòng 帝鉄 "Đường sắt Hoàng gia" để đợt thống nhất). Chỉ sửa Ohimitera trong dòng này.
4. **2302: 帝大生 → "sinh viên Đại học Hoàng gia"** — 帝大 dạng đầy đủ ("Đại học Đế quốc" theo thuật ngữ đã quyết), để đợt thống nhất (trong danh sách thống nhất của brief: "帝大 variants → Đại học Đế quốc"). Chỉ sửa đại từ + Ohimitera trong dòng này.
5. **2648: 二干潟 → "Niigata"** — giữ nguyên: 二干潟 là tên địa danh giả trong game, đọc にいがた (chơi chữ 新潟/Niigata); dịch "Niigata" diễn được chơi chữ, dịch âm Hán-Việt ("Nhị Can Tả") sẽ mất nghĩa. Cờ để Hieu xác nhận nếu muốn đổi.
6. **2217: くあっ → "Kua!"** — giữ nguyên: "Kua" vs "Hự" là câu hỏi đang chờ Hieu toàn dự án (tiền lệ れいなh1).
7. **2238: "Anh Houhehu" + "hích anh"** — giữ nguyên: ほーへふっ/しゅき là lời ngọng khi đang hôn (miệng đầy), diễn ngẫu hứng theo quy tắc SFX 22:05; "hích anh" là "thích anh" nói ngọng. Không sửa.
8. **2155: しゅごっ → "Tuyệt quá!"** — giữ nguyên (しゅご = すごい nói ngọng = "tuyệt vời"; tiền lệ 日々姫h1 1059 "Sướng quá" cũng đang cờ cho Hieu chọn giữa giữ ngẫu hứng hay đổi).
9. **仲国 → "Trọng Quốc" (8 dòng)** — giữ nguyên: đã là cách diễn nhất quán toàn dự án (tiền lệ 仲国08).

## §6. Chi tiết từng dòng sai (75)

### 2146 [双鉄] — đại từ
JP: 「理解できれば、不思議でもなんでもない話なのだが。\n――もう少し細かく説明するか？」
TW: 「只要理解了，就沒什麼不可思議的。――要我再詳細解釋一下嗎？」
Cũ: 「Nếu hiểu được thì chẳng có gì kỳ lạ cả đâu.\n――Anh giải thích chi tiết hơn một chút nhé?」
Mới: 「Nếu hiểu được thì chẳng có gì kỳ lạ cả đâu.\n――Tôi giải thích chi tiết hơn một chút nhé?」
→ Soutetsu tự xưng "anh" với Kisaki — theo quy tắc đã sửa, Soutetsu là "tôi" với Kisaki (JP 僕).

### 2738 [双鉄] — đại từ
JP: 「おやすい御用だ。あらかじめ許可も受けている」
TW: 「這簡單，我先前已經獲得過對方的許可了」
Cũ: 「Chuyện nhỏ. Anh cũng đã xin phép trước rồi」
Mới: 「Chuyện nhỏ. Tôi cũng đã xin phép trước rồi」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2774 [双鉄] — đại từ
JP: 「ならば、ここで質問だ」
TW: 「那我有個問題要考考你」
Cũ: 「Vậy thì, anh có một câu hỏi cho em đây」
Mới: 「Vậy thì, tôi có một câu hỏi cho em đây」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2592 [双鉄] — đại từ
JP: 「米という同じ原料、同じ製法で何故そうなるか。\n少し、考えて見て欲しい」
TW: 「用的都是大米，做法也是一樣的，但為什麼味道卻截然不同。你稍微思想一下」
Cũ: 「Cùng một nguyên liệu là gạo, cùng một phương pháp sản xuất, nhưng tại sao lại thành ra như vậy.\nAnh muốn em thử suy nghĩ một chút xem」
Mới: 「Cùng một nguyên liệu là gạo, cùng một phương pháp sản xuất, nhưng tại sao lại thành ra như vậy.\nTôi muốn em thử suy nghĩ một chút xem」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2783 [双鉄] — đại từ
JP: 「では……そうだな。米焼酎と日本酒と、\nその代表的な産地を比べてみて欲しい」
TW: 「那麼……你可以對比下米燒酒和日本酒，它們代表性的產地」
Cũ: 「Vậy thì…… xem nào. Anh muốn em thử so sánh giữa shochu gạo và rượu sake,\ncùng với những vùng sản xuất tiêu biểu của chúng」
Mới: 「Vậy thì…… xem nào. Tôi muốn em thử so sánh giữa shochu gạo và rượu sake,\ncùng với những vùng sản xuất tiêu biểu của chúng」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2316 [双鉄] — đại từ
JP: 「ふむ、チーズクリームも旨いものだな。\n予想していたよりもクセが無い」
TW: 「奶油乳酪真是好吃啊。比想像中要爽口很多」
Cũ: 「Hừm, kem phô mai cũng ngon đấy chứ.\nKhông bị ngấy như anh tưởng」
Mới: 「Hừm, kem phô mai cũng ngon đấy chứ.\nKhông bị ngấy như tôi tưởng」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2476 [双鉄] — đại từ
JP: 「僕がか？\nなにか、おかしなことでもしたか？」
TW: 「我？我有什麼不對勁的嗎？」
Cũ: 「Anh sao?\nAnh đã làm chuyện gì kỳ lạ à?」
Mới: 「Tôi sao?\nTôi đã làm chuyện gì kỳ lạ à?」
→ Soutetsu "anh"→"tôi" với Kisaki (×2).

### 2401 [双鉄] — đại từ
JP: 「僕も稀咲に、稀咲のを食べさせてもらいたい。\n交代で、でどうだ？」
TW: 「我也希望稀咲餵我吃呢。換著來怎麼樣？」
Cũ: 「Anh cũng muốn được Kisaki đút cho ăn phần của em.\nChúng ta thay phiên nhau nhé, thấy sao?」
Mới: 「Tôi cũng muốn được Kisaki đút cho ăn phần của em.\nChúng ta thay phiên nhau nhé, thấy sao?」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2474 [双鉄] — đại từ
JP: 「気持ちは、とても――とても嬉しい」
TW: 「我，我真的――真的很高興」
Cũ: 「Tấm lòng của em, anh thực sự――thực sự rất vui」
Mới: 「Tấm lòng của em, tôi thực sự――thực sự rất vui」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2405 [双鉄] — đại từ
JP: 「僕も同じだ。結婚式の主役は、稀咲。\nゆえに、稀咲にとって最高の式を作りあげたい」
TW: 「我也是一樣的。婚禮的主角是你，所以我想給你一場最棒的婚禮」
Cũ: 「Anh cũng vậy thôi. Nhân vật chính của lễ cưới, là Kisaki.\nVì vậy, anh muốn tạo ra một hôn lễ tuyệt vời nhất dành cho Kisaki」
Mới: 「Tôi cũng vậy thôi. Nhân vật chính của lễ cưới, là Kisaki.\nVì vậy, tôi muốn tạo ra một hôn lễ tuyệt vời nhất dành cho Kisaki」
→ Soutetsu "anh"→"tôi" với Kisaki (×2).

### 2772 [双鉄] — đại từ
JP: 「なら、言い直そう。稀咲にとって――\nそして稀咲の夢にとって、最高の式を作りたいのだ」
TW: 「那我換個說法，我想為了你――為了你的夢，帶給你一場最棒的婚禮」
Cũ: 「Vậy thì, anh nói lại nhé. Đối với Kisaki――\nVà đối với ước mơ của Kisaki, anh muốn tạo ra một hôn lễ tuyệt vời nhất」
Mới: 「Vậy thì, tôi nói lại nhé. Đối với Kisaki――\nVà đối với ước mơ của Kisaki, tôi muốn tạo ra một hôn lễ tuyệt vời nhất」
→ Soutetsu "anh"→"tôi" với Kisaki (×2).

### 2289 [双鉄] — đại từ
JP: 「だな。僕もそう感じている」
TW: 「嗯，我也有這種感覺」
Cũ: 「Đúng vậy. Anh cũng cảm thấy thế」
Mới: 「Đúng vậy. Tôi cũng cảm thấy thế」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2434 [双鉄] — đại từ
JP: 「ふたりで同じ夢を抱けていることに、感謝している。\n元忠さんが、それをわかってくださっていることにも」
TW: 「我很高興能和你有著一樣的夢。也感謝元忠叔叔對我們的理解」
Cũ: 「Anh rất biết ơn vì hai chúng ta có thể cùng chung một ước mơ.\nVà cũng biết ơn vì bác Mototada đã thấu hiểu điều đó」
Mới: 「Tôi rất biết ơn vì hai chúng ta có thể cùng chung một ước mơ.\nVà cũng biết ơn vì bác Mototada đã thấu hiểu điều đó」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2661 [双鉄] — đại từ
JP: 「結婚式への出席希望者も膨れ上がったと聞いている。\n調整が、そう簡単につかぬだろうとも思うのだがな」
TW: 「聽說希望出席婚禮的人也多了很多。雖然調整起來不會容易」
Cũ: 「Anh nghe nói số lượng người muốn tham dự lễ cưới cũng tăng lên chóng mặt.\nAnh nghĩ việc sắp xếp chắc chắn sẽ không hề đơn giản đâu」
Mới: 「Tôi nghe nói số lượng người muốn tham dự lễ cưới cũng tăng lên chóng mặt.\nTôi nghĩ việc sắp xếp chắc chắn sẽ không hề đơn giản đâu」
→ Soutetsu "anh"→"tôi" với Kisaki (×2).

### 2658 [双鉄] — đại từ
JP: 「稀咲も僕も、考え事が趣味の様な一面もあるからな。\n『考えすぎるな』などとは、気休めでも言えんが」
TW: 「而且稀咲和我都有把思考作為樂趣的傾向。“別想太深了”這種安慰話就不用說了吧」
Cũ: 「Cả Kisaki và anh đều có sở thích là hay suy nghĩ mà.\nNên anh cũng chẳng thể nói những câu an ủi kiểu như 『Đừng suy nghĩ nhiều quá』 được」
Mới: 「Cả Kisaki và tôi đều có sở thích là hay suy nghĩ mà.\nNên tôi cũng chẳng thể nói những câu an ủi kiểu như 『Đừng suy nghĩ nhiều quá』 được」
→ Soutetsu "anh"→"tôi" với Kisaki (×2).

### 2443 [双鉄] — đại từ
JP: 「せめて現場で、僕も何かを手伝えればな」
TW: 「我想在現場提供一點幫助啦」
Cũ: 「Ít nhất thì ở hiện trường, anh cũng muốn giúp được gì đó」
Mới: 「Ít nhất thì ở hiện trường, tôi cũng muốn giúp được gì đó」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2419 [双鉄] — đại từ
JP: 「婚約者だと紹介してしまうことで、\n結婚式への招待の流れをつくるのか」
TW: 「我就介紹你是我的未婚夫，然後邀請她來婚禮做客吧」
Cũ: 「Bằng cách giới thiệu anh là vị hôn phu,\nem định tạo cớ để mời cô ấy đến dự lễ cưới luôn sao」
Mới: 「Bằng cách giới thiệu tôi là vị hôn phu,\nem định tạo cớ để mời cô ấy đến dự lễ cưới luôn sao」
→ Soutetsu tự xưng "anh"→"tôi" (giới thiệu mình là vị hôn phu).

### 2491 [双鉄] — đại từ
JP: 「その接待には、僕はどのような服でいけばいい？\n普通の背広でかまわないのか？」
TW: 「接待時我要穿什麼衣服？一般的西裝可以嗎？」
Cũ: 「Vậy đi tiếp khách thì anh nên mặc đồ gì?\nMặc vest bình thường có được không?」
Mới: 「Vậy đi tiếp khách thì tôi nên mặc đồ gì?\nMặc vest bình thường có được không?」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2302 [双鉄] — đại từ
JP: 「そのような立場にいなかったからな。\n御一夜に戻ってくる前は、酒問屋の社員兼帝大生だ」
TW: 「因為我以前沒有那個身份啊。我回到御一夜前，只是小酒鋪的店員和帝大學生」
Cũ: 「Anh đâu có ở vị thế để tham gia mấy chuyện đó.\nTrước khi trở về Ohimitera, anh chỉ là nhân viên của một cửa hàng bán buôn rượu kiêm sinh viên Đại học Hoàng gia thôi mà」
Mới: 「Tôi đâu có ở vị thế để tham gia mấy chuyện đó.\nTrước khi trở về Ohitoyo, tôi chỉ là nhân viên của một cửa hàng bán buôn rượu kiêm sinh viên Đại học Hoàng gia thôi mà」
→ Soutetsu "anh"→"tôi" (×2) với Kisaki; 御一夜→Ohitoyo theo thuật ngữ đã quyết. (帝大 "Đại học Hoàng gia" để đợt thống nhất — xem §5.)

### 2262 [双鉄] — đại từ
JP: 「ああ――見たい」
TW: 「嗯――我想看」
Cũ: 「Ừm――anh muốn xem」
Mới: 「Ừm――tôi muốn xem」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2445 [双鉄] — đại từ
JP: 「僕は、稀咲のチャイナドレス姿を見たい」
TW: 「我想看稀咲穿旗袍」
Cũ: 「Anh muốn ngắm nhìn dáng vẻ Kisaki trong bộ sườn xám」
Mới: 「Tôi muốn ngắm nhìn dáng vẻ Kisaki trong bộ sườn xám」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2291 [双鉄] — đại từ
JP: 「うむ。見せてくれ」
TW: 「嗯，讓我看看吧」
Cũ: 「Ừm. Cho anh xem đi」
Mới: 「Ừm. Cho tôi xem đi」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2429 [双鉄] — đại từ
JP: 「楽しみだ。早く見せてくれ」
TW: 「我很期待哦，快讓我看看」
Cũ: 「Anh mong lắm rồi đấy. Nhanh cho anh xem đi」
Mới: 「Tôi mong lắm rồi đấy. Nhanh cho tôi xem đi」
→ Soutetsu "anh"→"tôi" với Kisaki (×2).

### 1993 [双鉄] — đại từ
JP: 「いや、そのままだ。\n隠さずそのまま、全身をきちんと見せてくれ」
TW: 「不，就這樣。不要遮掩了，讓我看到你整個身體吧」
Cũ: 「Không, cứ giữ nguyên như vậy đi.\nĐừng che lại, hãy để anh ngắm nhìn toàn bộ cơ thể em」
Mới: 「Không, cứ giữ nguyên như vậy đi.\nĐừng che lại, hãy để tôi ngắm nhìn toàn bộ cơ thể em」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2510 [双鉄] — đại từ
JP: 「まぁな。言われるまでは、気づかなかった」
TW: 「是啊，你不說我還沒發現呢」
Cũ: 「Cũng đúng. Cho đến khi em nói, anh mới nhận ra đấy」
Mới: 「Cũng đúng. Cho đến khi em nói, tôi mới nhận ra đấy」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2387 [双鉄] — đại từ
JP: 「どうした。なにか僕がおかしなことでもいったか？」
TW: 「怎麼了，我說什麼奇怪的話了嗎？」
Cũ: 「Sao thế. Anh nói gì kỳ lạ à?」
Mới: 「Sao thế. Tôi nói gì kỳ lạ à?」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2440 [双鉄] — đại từ
JP: 「なにが、僕だ？」
TW: 「我怎麼了啊？」
Cũ: 「Anh thì, làm sao cơ?」
Mới: 「Tôi thì, làm sao cơ?」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2640 [双鉄] — đại từ
JP: 「稀咲。僕も幸せだ。\n即物的と思われてしまうかもしれないが――」
TW: 「稀咲，我也很幸福。你可能會覺得我講這話太功利――」
Cũ: 「Kisaki. Anh cũng hạnh phúc lắm.\nCó thể em sẽ nghĩ anh thực dụng, nhưng――」
Mới: 「Kisaki. Tôi cũng hạnh phúc lắm.\nCó thể em sẽ nghĩ tôi thực dụng, nhưng――」
→ Soutetsu "anh"→"tôi" với Kisaki (×2).

### 3006 [monologue] — đại từ
JP: それでもこれほど、心が動かされている。\n言葉にせずにはいられない。
TW: 但是我真的非常動心。怎麼都想把這個心思告訴她。
Cũ: Dù vậy, trái tim anh vẫn rung động đến nhường này.\nKhông thể không nói ra thành lời.
Mới: Dù vậy, trái tim tôi vẫn rung động đến nhường này.\nKhông thể không nói ra thành lời.
→ Độc thoại Soutetsu: "trái tim anh"→"trái tim tôi" (tự xưng "tôi" với Kisaki; tiền lệ độc thoại "Anh"→"Tôi" đã gộp trước đây).

### 2428 [双鉄] — đại từ
JP: 「稀咲がこれほどに美しいと、\n美しい女に愛される幸福を、改めて強く感じた」
TW: 「我很有感觸，稀咲會這麼美麗，有稀咲這麼美的女孩愛著自己是這麼幸福」
Cũ: 「Khi thấy Kisaki xinh đẹp đến thế này,\nanh lại một lần nữa cảm nhận sâu sắc niềm hạnh phúc khi được một người phụ nữ xinh đẹp yêu thương」
Mới: 「Khi thấy Kisaki xinh đẹp đến thế này,\ntôi lại một lần nữa cảm nhận sâu sắc niềm hạnh phúc khi được một người phụ nữ xinh đẹp yêu thương」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2463 [双鉄] — đại từ
JP: 「僕は稀咲が、稀咲であると知っている。\n稀咲の全てを愛しているし、尊敬している」
TW: 「我知道稀咲就是稀咲。我愛稀咲的一切，尊重稀咲的每一點」
Cũ: 「Anh biết Kisaki, chính là Kisaki.\nAnh yêu tất cả mọi thứ thuộc về Kisaki, và cũng rất tôn trọng em」
Mới: 「Tôi biết Kisaki, chính là Kisaki.\nTôi yêu tất cả mọi thứ thuộc về Kisaki, và cũng rất tôn trọng em」
→ Soutetsu "anh"→"tôi" với Kisaki (×2).

### 2397 [双鉄] — đại từ
JP: 「僕は稀咲を傷つけたくない、捻じ曲げたくない。\n稀咲が稀咲でなくなることを、何より強く恐れている」
TW: 「我不想傷害稀咲，不想扭曲你的想法。我最害怕的事情，就是你會不再是你自己」
Cũ: 「Anh không muốn làm tổn thương Kisaki, không muốn bóp méo con người em.\nAnh sợ hãi hơn bất cứ điều gì, việc Kisaki không còn là Kisaki nữa」
Mới: 「Tôi không muốn làm tổn thương Kisaki, không muốn bóp méo con người em.\nTôi sợ hãi hơn bất cứ điều gì, việc Kisaki không còn là Kisaki nữa」
→ Soutetsu "anh"→"tôi" với Kisaki (×2).

### 2453 [双鉄] — đại từ
JP: 「僕はこれほど、稀咲の体も求めてる。\nだが、体だけでは意味がないのだ」
TW: 「我是這麼渴求你的身體。但是渴求的絕不只是你的身體」
Cũ: 「Anh khao khát cơ thể của Kisaki đến nhường này.\nNhưng, nếu chỉ có cơ thể thôi thì chẳng có ý nghĩa gì cả」
Mới: 「Tôi khao khát cơ thể của Kisaki đến nhường này.\nNhưng, nếu chỉ có cơ thể thôi thì chẳng có ý nghĩa gì cả」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2418 [双鉄] — đại từ
JP: 「僕は、稀咲の全てが好きだ。どこかひとつを\n切り離したなら、それはもう、稀咲ではない」
TW: 「我喜歡你的一切，哪怕是少了一分一毫，也不是稀咲了」
Cũ: 「Anh, yêu mọi thứ thuộc về Kisaki. Nếu tách rời\nbất cứ phần nào ra, thì đó không còn là Kisaki nữa」
Mới: 「Tôi, yêu mọi thứ thuộc về Kisaki. Nếu tách rời\nbất cứ phần nào ra, thì đó không còn là Kisaki nữa」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2415 [双鉄] — đại từ
JP: 「それは、僕が不慣れだからだ。欲望のままに動いて、\n稀咲を傷つけはしないかと」
TW: 「我只是不太習慣，只怕自己性慾大發會傷害到你啊」
Cũ: 「Đó là, do anh chưa quen thôi. Anh sợ nếu cứ hành động theo dục vọng,\nthì sẽ làm tổn thương Kisaki mất」
Mới: 「Đó là, do tôi chưa quen thôi. Tôi sợ nếu cứ hành động theo dục vọng,\nthì sẽ làm tổn thương Kisaki mất」
→ Soutetsu "anh"→"tôi" với Kisaki (×2).

### 2612 [双鉄] — đại từ
JP: 「わかった」
TW: 「知道了」
Cũ: 「Anh hiểu rồi」
Mới: 「Tôi hiểu rồi」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2423 [双鉄] — đại từ
JP: 「十分、好きにしているが？」
TW: 「我已經很愛它們了啊？」
Cũ: 「Anh đã làm đủ thứ mình thích rồi mà?」
Mới: 「Tôi đã làm đủ thứ mình thích rồi mà?」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2411 [双鉄] — đại từ
JP: 「どこまでも――僕の望むままにか」
TW: 「我到底――能多麼隨心所欲呢」
Cũ: 「Dù thế nào đi nữa――cũng sẽ theo ý muốn của anh sao」
Mới: 「Dù thế nào đi nữa――cũng sẽ theo ý muốn của tôi sao」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2789 [双鉄] — đại từ
JP: 「おっぱい以外も、好きにするぞ」
TW: 「除了胸部，其他地方我也要為所欲為了」
Cũ: 「Ngoài vú ra, anh cũng sẽ làm theo ý mình đấy」
Mới: 「Ngoài vú ra, tôi cũng sẽ làm theo ý mình đấy」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2102 [双鉄] — đại từ
JP: 「もっと、近くで感じさせてくれ」
TW: 「再靠近一點，再讓我多點感覺」
Cũ: 「Hãy cho anh cảm nhận gần hơn nữa đi」
Mới: 「Hãy cho tôi cảm nhận gần hơn nữa đi」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 1987 [双鉄] — đại từ
JP: 「いかんか？　僕は言いたいのだがな」
TW: 「不行嗎？　可是我想說啊」
Cũ: 「Không được sao? Nhưng anh lại muốn nói đấy」
Mới: 「Không được sao? Nhưng tôi lại muốn nói đấy」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2775 [双鉄] — đại từ
JP: 「そして聞きたい。教えて欲しい。\nどうして紐をほどいてもなお、下着が落ちんのだ？」
TW: 「那我要問問你，請告訴我。為什麼解開帶子，內褲還是不掉下來呢？」
Cũ: 「Và anh muốn hỏi. Em hãy nói cho anh biết.\nTại sao cởi dây ra rồi mà quần lót vẫn không rớt xuống?」
Mới: 「Và tôi muốn hỏi. Em hãy nói cho tôi biết.\nTại sao cởi dây ra rồi mà quần lót vẫn không rớt xuống?」
→ Soutetsu "anh"→"tôi" với Kisaki (×2).

### 2728 [双鉄] — đại từ
JP: 「稀咲が言ってくれたように、僕のしたいセックスを、\n肉体の求めるままに、ひとまず、試してみたのだが」
TW: 「這就是你說的，我所渴求的性愛，只為了佔有肉體的性愛，我只是嘗試了一下」
Cũ: 「Như Kisaki đã nói, tình dục mà anh muốn,\nchỉ là khao khát thể xác, anh chỉ tạm thời thử xem sao thôi」
Mới: 「Như Kisaki đã nói, tình dục mà tôi muốn,\nchỉ là khao khát thể xác, tôi chỉ tạm thời thử xem sao thôi」
→ Soutetsu "anh"→"tôi" với Kisaki (×2).

### 2698 [双鉄] — đại từ
JP: 「体だけなら、素晴らしくいい。気持ちいい。\nだが、これ以上の快感を、僕はすでに知っている」
TW: 「身體非常滿足，非常快樂。但我早知道世上有更美妙的快感了」
Cũ: 「Nếu chỉ là thể xác thì tuyệt vời lắm. Rất sướng.\nNhưng mà, khoái cảm vượt lên trên thế này, anh đã biết rồi」
Mới: 「Nếu chỉ là thể xác thì tuyệt vời lắm. Rất sướng.\nNhưng mà, khoái cảm vượt lên trên thế này, tôi đã biết rồi」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2462 [双鉄] — đại từ
JP: 「僕が知っているのは、稀咲だけだ。稀咲との――\n肉体だけでなく、心も通わせるセックスだ」
TW: 「我知道的只有稀咲，只有和稀咲――肉體通肉體、心通心的性愛」
Cũ: 「Người anh biết, chỉ có Kisaki thôi. Với Kisaki――\nTình dục không chỉ là thể xác, mà còn là sự hòa quyện của tâm hồn」
Mới: 「Người tôi biết, chỉ có Kisaki thôi. Với Kisaki――\nTình dục không chỉ là thể xác, mà còn là sự hòa quyện của tâm hồn」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2251 [双鉄] — đại từ
JP: 「一方的に貪ることは、僕のしたいセックスじゃない。\n一番したくて気持ちいいのは、稀咲と作るセックスだ」
TW: 「單方面的貪婪，不是我想要的性愛。我最想做的、最快樂的，是和稀咲一起做的性愛」
Cũ: 「Đòi hỏi một chiều không phải là tình dục anh muốn.\nĐiều anh muốn nhất và sướng nhất, là tình dục cùng Kisaki tạo ra」
Mới: 「Đòi hỏi một chiều không phải là tình dục tôi muốn.\nĐiều tôi muốn nhất và sướng nhất, là tình dục cùng Kisaki tạo ra」
→ Soutetsu "anh"→"tôi" với Kisaki (×2).

### 2403 [双鉄] — đại từ
JP: 「僕もだ」
TW: 「我也是」
Cũ: 「Anh cũng vậy」
Mới: 「Tôi cũng vậy」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2402 [双鉄] — đại từ
JP: 「僕もだ――稀咲」
TW: 「我也是――稀咲」
Cũ: 「Anh cũng vậy――Kisaki」
Mới: 「Tôi cũng vậy――Kisaki」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2451 [双鉄] — đại từ
JP: 「それは嬉しい。\nしかし、やはり痛めてはもったいないな」
TW: 「我是很高興啦。但是我也不想弄壞這件衣服，多可惜啊」
Cũ: 「Anh rất vui.\nNhưng mà, làm hỏng thì vẫn uổng lắm」
Mới: 「Tôi rất vui.\nNhưng mà, làm hỏng thì vẫn uổng lắm」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2768 [双鉄] — đại từ
JP: 「ならば僕が、ソファに横たわるとしよう」
TW: 「那我就躺在沙發上好了」
Cũ: 「Nếu vậy anh sẽ nằm xuống sofa nhé」
Mới: 「Nếu vậy tôi sẽ nằm xuống sofa nhé」
→ Soutetsu "anh"→"tôi" với Kisaki.

### 2648 [稀咲] — thuật ngữ
JP: 「米焼酎の代表なら、もちろんクマ――御一夜だよね。\n日本酒は――[にいがた,2]二干潟のイメージが強いかな」
TW: 「米燒酒的代表就是球磨――御一夜吧。日本酒呢――我印象強烈的就是二干潟了」
Cũ: 「Đại diện cho shochu gạo thì tất nhiên là Kuma――Ohimitera rồi.\nCòn rượu sake thì――chắc là Niigata để lại ấn tượng mạnh nhất nhỉ」
Mới: 「Đại diện cho shochu gạo thì tất nhiên là Kuma――Ohitoyo rồi.\nCòn rượu sake thì――chắc là Niigata để lại ấn tượng mạnh nhất nhỉ」
→ 御一夜→"Ohitoyo" (thuật ngữ đã quyết; "Niigata" cho 二干潟 giữ nguyên — cách diễn đạt chơi chữ にいがた, xem §5).

### 3099 [monologue] — thuật ngữ
JP: 二度と取り返せない多くを、僕らはすでに、\nみんなから、御一夜から、授かっているのだから。
TW: 因為我們已經從所有人、從御一夜，收到了太多太多獨一無二的東西了。
Cũ: Bởi vì chúng tôi đã nhận được rất nhiều thứ không thể nào lấy lại được lần thứ hai,\ntừ mọi người, và từ Ohimitera.
Mới: Bởi vì chúng tôi đã nhận được rất nhiều thứ không thể nào lấy lại được lần thứ hai,\ntừ mọi người, và từ Ohitoyo.
→ 御一夜→"Ohitoyo" (thuật ngữ đã quyết).

### 2740 [双鉄] — thuật ngữ
JP: 「御一夜とも右田とも宝生とも縁もゆかりもなかった、\n旧帝鉄総裁を仲人にまで引っ張ってくださったのだ」
TW: 「連和御一夜、和右田、和寶生都沒有任何來往的舊帝鐵總裁，都肯當我們的媒人了」
Cũ: 「Bác ấy thậm chí còn mời được cựu Tổng giám đốc Đường sắt Hoàng gia,\nngười vốn không có chút liên hệ nào với Ohimitera, nhà Migita hay nhà Houshou, làm người mai mối cho chúng ta mà」
Mới: 「Bác ấy thậm chí còn mời được cựu Tổng giám đốc Đường sắt Hoàng gia,\nngười vốn không có chút liên hệ nào với Ohitoyo, nhà Migita hay nhà Houshou, làm người mai mối cho chúng ta mà」
→ 御一夜→"Ohitoyo" (thuật ngữ đã quyết). (旧帝鉄総裁 "cựu Tổng giám đốc Đường sắt Hoàng gia" để đợt thống nhất — xem §5.)

### 2972 [monologue] — sai nghĩa
JP: 反冥という政府方針もあってだろうか、\n仲国のエアクラ本格化は日ノ本よりもかなり遅れた。
TW: 一部分是出於反冥的行政要求，仲國的民航業比日本晚了很久才走上正軌。
Cũ: Có lẽ cũng một phần do chính sách phản đối Aerocraft của chính phủ,\nmà việc phổ biến Aerocraft ở Trọng Quốc diễn ra muộn hơn Hinomoto khá nhiều.
Mới: Có lẽ cũng một phần do chính sách chống Minh Quốc của chính phủ,\nmà việc phổ biến Aircra ở Trọng Quốc diễn ra muộn hơn Hinomoto khá nhiều.
→ 反冥 dịch sai thành "phản đối Aerocraft" — 反冥 là chính sách chống Minh Quốc (冥国), không liên quan tới エアクラ; TW 反冥 xác nhận. Đồng thời エアクラ→"Aircra" theo thuật ngữ đã quyết (không dùng "Aerocraft").

### 2468 [稀咲] — sai nghĩa
JP: 「『飲ませてくれる』んじゃないのかい？\n双鉄が、ボクに」
TW: 「我說了，要『給我喝』的啊，忘了嗎？要由你餵我喝」
Cũ: 「Chẳng phải anh bảo là 『cho em uống』 sao?\nAnh Soutetsu, cho em ấy」
Mới: 「Chẳng phải anh bảo là 『cho em uống』 sao?\nAnh Soutetsu, cho em」
→ Kisaki tự xưng "em ấy" — sai ngôi: JP 双鉄が、ボクに = "anh Soutetsu cho em (Kisaki)"; "em ấy" đọc thành người thứ ba ("cho cô ấy"). Sửa thành "cho em".

### 1550 [稀咲] — sai nghĩa
JP: 「『好きな男の子の家だから』。だよ？」
TW: 「“因為這裡是我喜歡的男孩子的家”喔？」
Cũ: 「『Vì đây là nhà của người con trai mà em thích』. Đó?」
Mới: 「『Vì đây là nhà của người con trai mà em thích』. Đấy nhé?」
→ だよ？ cuối câu dịch thành "Đó?" — "đó" là chỉ thị, không diễn được nghĩa xác nhận nhẹ của だよ？. Sửa "Đấy nhé?".

### 3330 [monologue] — sai nghĩa
JP: 酒の、香だ。
TW: 是酒的氣味。
Cũ: Là hương, rượu.
Mới: Là mùi hương của rượu.
→ 酒の、香だ。 dịch "Là hương, rượu." — đảo trật tự, tiếng Việt gãy. Sửa "Là mùi hương của rượu."

### 1552 [稀咲] — gasp っ
JP: 「……っ」
TW: 「……」
Cũ: 「……」
Mới: 「……Ư」
→ Sweep: 「……っ」 toàn dòng là gasp, VN mất hẳn → thêm Ư (áp nguyên sweep).

### 2003 [稀咲] — gasp っ
JP: 「乳首……双鉄、に……なでられ――て……っ……\nそれだけ、で――こんなに、あつく――かたく――」
TW: 「乳頭……在雙鐵……的撫摸下……就會――這麼熾熱――這麼堅挺――」
Cũ: 「Đầu vú…… được, anh Soutetsu…… vuốt ve――……\nChỉ cần vậy, thôi――đã nóng ran――và cứng lại, thế này――」
Mới: 「Đầu vú…… được, anh Soutetsu…… vuốt ve――……Ư\nChỉ cần vậy, thôi――đã nóng ran――và cứng lại, thế này――」
→ Sweep: っ…… cuối dòng 1 là gasp, VN mất hẳn → thêm Ư cuối dòng 1 (áp sweep, đã chỉnh lại giữ đúng \n của CSV3 — bản sweep dùng khoảng trắng).

### 2161 [稀咲] — gasp っ
JP: 「きゃ！　ふっ――～～～～～～～～っ！！！」
TW: 「呀！　呼――～～～～～～～～！！！」
Cũ: 「Kya! Phu――~~~~~~~~!!!」
Mới: 「Kya! Phu――~~~~~~~~Ư!!!」
→ Sweep: ～～～～～～～～っ！！！ — っ sau ~~~~ mất hẳn → thêm Ư (áp nguyên sweep).

### 2257 [稀咲] — gasp っ
JP: 「くふぅんんんん～～～～っ！！！」
TW: 「嗚嗯～～～～！！！」
Cũ: 「Khu phư ưm~~~~!!!」
Mới: 「Khu phư ưm~~~~Ư!!!」
→ Sweep: くふぅんんんん～～～～っ！！！ — っ sau ~~~~ mất hẳn → thêm Ư (áp nguyên sweep).

### 2809 [双鉄] — gasp っ
JP: 「っ！」
TW: 「！」
Cũ: 「!」
Mới: 「Ư!」
→ Sweep: 「っ！」 toàn dòng là gasp → "Ư!" (áp nguyên sweep).

### 2810 [双鉄] — gasp っ
JP: 「っ！！」
TW: 「！！」
Cũ: 「!!」
Mới: 「Ư!!」
→ Sweep: 「っ！！」 toàn dòng là gasp → "Ư!!" (áp nguyên sweep).

### 2813 [双鉄] — gasp っ
JP: 「っ！！？」
TW: 「！！？」
Cũ: 「!!?」
Mới: 「Ư!!?」
→ Sweep: 「っ！！？」 toàn dòng là gasp → "Ư!!?" (áp nguyên sweep).

### 2814 [双鉄] — gasp っ
JP: 「っ！？」
TW: 「！？」
Cũ: 「!?」
Mới: 「Ư!?」
→ Sweep: 「っ！？」 toàn dòng là gasp → "Ư!?" (áp nguyên sweep).

### 2824 [稀咲] — gasp っ
JP: 「～～～～～っ！」
TW: 「～～～～～！」
Cũ: 「~~~~~!」
Mới: 「~~~~~Ư!」
→ Sweep: 「～～～～～っ！」 — っ sau ~~~~ mất hẳn → thêm Ư (áp nguyên sweep).

### 2826 [稀咲] — gasp っ
JP: 「～～～～～～～～～っ！！！？」
TW: 「～～～～～～～～～！！！？」
Cũ: 「~~~~~~~~~!!!?」
Mới: 「~~~~~~~~~Ư!!!?」
→ Sweep: 「～～～～～～～～～っ！！！？」 — っ sau ~~~~~~~~ mất hẳn → thêm Ư (áp nguyên sweep).

### 3143 [monologue] — gasp っ
JP: 気づけば、稀咲が自分の体を隠そうと――っ！
TW: 她這是在遮掩自己的身體呢――！
Cũ: Bất chợt, Kisaki cố gắng che giấu cơ thể mình――!
Mới: Bất chợt, Kisaki cố gắng che giấu cơ thể mình――Ư!
→ Sweep: ――っ！ cuối dòng là gasp, VN mất hẳn → thêm Ư (áp nguyên sweep).

### 2188 [稀咲] — gasp っ
JP: 「ふうっ――はぁ――んっ――ふぁっ――んっ――\n～～っ！　はっ――ふぁっ――ん……んふ――」
TW: 「呼――哈――嗯――哇――嗯――～～！　哈――哇――嗯……嗯唔――」
Cũ: 「Phù――hà――ưm――phua――ưm――\n~~! Hà――phua――ưm……ưm phu――」
Mới: 「Phù――hà――ưm――phua――ưm――\n~~Ư! Hà――phua――ưm……ưm phu――」
→ Sweep bỏ sót: ～～っ！ giữa dòng là token gasp độc lập, VN "~~!" mất hẳn っ — cùng mẫu với sweep 2824/2826 (～～+っ+！ → thêm Ư).

### 2218 [稀咲] — gasp っ
JP: 「～～～っ！！　はっ――がまんっ、むりっ！\nがんばる、けどっ――もうっ！　おまんこ、だって！」
TW: 「唔～～～！！　哈――忍不住了！我想加油――但是忍不住了！　小穴也忍不住了！」
Cũ: 「~~~!! Hà――chịu đựng, không nổi!\nCố gắng, nhưng mà――không được! Cả âm đạo, cũng thế!」
Mới: 「~~~Ư!! Hà――chịu đựng, không nổi!\nCố gắng, nhưng mà――không được! Cả âm đạo, cũng thế!」
→ Sweep bỏ sót: ～～～っ！！ đầu dòng là token gasp độc lập, VN "~~~!!" mất hẳn っ — cùng mẫu sweep 2824/2826.

### 2820 [稀咲] — gasp っ
JP: 「～っ！？　こまる――なら――おち、ん、ちんっ、\nすこし――おまんこ――やすませ――ひゃっ！　ふっ」
TW: 「～！？　麻煩――的話――小雞雞慢點，稍微――讓小穴――休息一下――呀！　呼」
Cũ: 「~!? Gay go――thì――dương, vật,\ncho――âm đạo――nghỉ một chút――hya! Phu」
Mới: 「~Ư!? Gay go――thì――dương, vật,\ncho――âm đạo――nghỉ một chút――hya! Phu」
→ Sweep bỏ sót: ～っ！？ đầu dòng là token gasp độc lập, VN "~!?" mất hẳn っ — cùng mẫu sweep 2824/2826.

### 2170 [稀咲] — gasp っ
JP: 「っっっ～～っ――ふぁっ、あっ――おっぱい――ん、\nふっ――ふあっ――んっ――ふうっ――ふうっ」
TW: 「呃～～――哇、啊――胸部――嗯、呼――嗚啊――嗯――呼――呼」
Cũ: 「~~~――phua, á――vú――ưm,\nphù――phua――ưm――phù――phù」
Mới: 「Ư~~~――phua, á――vú――ưm,\nphù――phua――ưm――phù――phù」
→ Sweep bỏ sót: っっっ～～っ―― đầu dòng — cụm っっっ đầu dòng mất hẳn (quy tắc gasp đã khóa: っ đầu dòng → thêm Ư); っ sau ～～ đã được ―― diễn (tiền lệ ふぁっ――→"Phu a——"), không thêm Ư thứ hai.

### 2253 [稀咲] — gasp っ
JP: 「ふあっ――んっ――そう、てつ――すご、い――\nっ――びく、びく――してる――あつくて、おっきい」
TW: 「嗚啊――嗯――雙鐵――好厲害――小雞雞――跳個不停――好熱、好粗壯」
Cũ: 「Phua――ưm――anh, Soutetsu――tuyệt, quá――\n――giật, giật――liên hồi――nóng quá, to quá」
Mới: 「Phua――ưm――anh, Soutetsu――tuyệt, quá――\nƯ――giật, giật――liên hồi――nóng quá, to quá」
→ Sweep bỏ sót: っ―― đầu dòng 2 là gasp, VN "――giật" mất hẳn っ — quy tắc gasp đã khóa (っ đầu dòng → thêm Ư). (Khác 1538: ở đó っ―― được "Ưm" diễn vì theo sau là ううん.)

### 2158 [稀咲] — SFX
JP: 「きゃああっ！？」
TW: 「呀啊！？」
Cũ: 「Á!?」
Mới: 「Kyaaa!?」
→ きゃああっ！？ dịch "Á!?" — mất hẳn âm đầu きゃ của tiếng thét. File này luôn diễn âm đầu きゃ/ひゃ (きゃ！→"Kya!", ひゃうっっ→"Hya!!?", ひあっ→"I a"), nên sửa "Kyaaa!?" (3 âm a theo あああ).

### 3483 [monologue] — dấu câu
JP: 稀咲が、実にそわそわしている。\n足をもじもじ――っ！！？
TW: 稀咲扭動著身體，腳也扭扭捏捏的――！！？
Cũ: Kisaki đang thực sự rất bồn chồn.\nĐôi chân cứ xoắn xuýt vào nhau――!!?」
Mới: Kisaki đang thực sự rất bồn chồn.\nĐôi chân cứ xoắn xuýt vào nhau――!!?
→ Dấu 」 thừa cuối dòng VN (không có 「 mở đầu trong dòng) — gỡ. (Sweep xếp 3483 là already-rendered: っ đã được "!!?" diễn, không thêm Ư — chỉ gỡ dấu thừa.)
## §7. Lượt soát 2 (bắt buộc — đọc lại toàn bộ fix đối chiếu JP)

**75/75 tái kiểm chứng, 0 bỏ, 0 sửa.** Đọc lại từng fix trong file `work-kisakih3-secondpass.txt` đối chiếu trực tiếp JP (+TW): 50 đại từ đều là Soutetsu nói với Kisaki (JP 僕, không có ngoại lệ — toàn bộ thoại 双鉄 trong file đều hướng về Kisaki); 11 fix sweep áp nguyên đúng giá trị sweep (2003 đã chỉnh \n theo CSV3); 5 gasp sweep-bỏ-sót đúng mẫu sweep; 2158 đúng tiền lệ diễn âm đầu きゃ/ひゃ của file; 3483 chỉ gỡ dấu 」 thừa. Không phát hiện fix nào sai cần loại hay sửa lại trong lượt 2.

## §8. Kiểm chứng máy

- JSON: 75 mục dạng list-of-dicts chuẩn, key là chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 75/75; diff-sanity: 4 fix có tỉ lệ tương đồng < 0,80 đều là dòng ngắn (2612, 2403, 3330, 2158 — đổi 1 từ/cụm trong câu ngắn), đã kiểm từng dòng, không có viết lại lớn.
- Khối TOML: parse bằng tomllib OK, 75 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô — `\\n` trong khối parse lại thành backslash-n dạng chữ, khớp CSV3).
- Quét máy bổ sung: toàn bộ 662 dòng — 0 khóa trùng, 0 VN trống, 0 thẻ %l lệch (JP có thẻ thì VN có đủ, VN không tự thêm thẻ), chỉ 1 dấu 」 thừa (3483, đã sửa), "Ohimitera" còn 0 sau khi sửa (4 dòng), "Anh" của Soutetsu còn 0 sau khi sửa (50 dòng), Kisaki "tôi" 0 dòng (đúng "em" toàn file).

## Khối TOML (đã parse-kiểm chứng, 75 khóa)

```toml
"2146" = "「Nếu hiểu được thì chẳng có gì kỳ lạ cả đâu.\\n――Tôi giải thích chi tiết hơn một chút nhé?」"
"2738" = "「Chuyện nhỏ. Tôi cũng đã xin phép trước rồi」"
"2774" = "「Vậy thì, tôi có một câu hỏi cho em đây」"
"2592" = "「Cùng một nguyên liệu là gạo, cùng một phương pháp sản xuất, nhưng tại sao lại thành ra như vậy.\\nTôi muốn em thử suy nghĩ một chút xem」"
"2783" = "「Vậy thì…… xem nào. Tôi muốn em thử so sánh giữa shochu gạo và rượu sake,\\ncùng với những vùng sản xuất tiêu biểu của chúng」"
"2316" = "「Hừm, kem phô mai cũng ngon đấy chứ.\\nKhông bị ngấy như tôi tưởng」"
"2476" = "「Tôi sao?\\nTôi đã làm chuyện gì kỳ lạ à?」"
"2401" = "「Tôi cũng muốn được Kisaki đút cho ăn phần của em.\\nChúng ta thay phiên nhau nhé, thấy sao?」"
"2474" = "「Tấm lòng của em, tôi thực sự――thực sự rất vui」"
"2405" = "「Tôi cũng vậy thôi. Nhân vật chính của lễ cưới, là Kisaki.\\nVì vậy, tôi muốn tạo ra một hôn lễ tuyệt vời nhất dành cho Kisaki」"
"2772" = "「Vậy thì, tôi nói lại nhé. Đối với Kisaki――\\nVà đối với ước mơ của Kisaki, tôi muốn tạo ra một hôn lễ tuyệt vời nhất」"
"2289" = "「Đúng vậy. Tôi cũng cảm thấy thế」"
"2434" = "「Tôi rất biết ơn vì hai chúng ta có thể cùng chung một ước mơ.\\nVà cũng biết ơn vì bác Mototada đã thấu hiểu điều đó」"
"2661" = "「Tôi nghe nói số lượng người muốn tham dự lễ cưới cũng tăng lên chóng mặt.\\nTôi nghĩ việc sắp xếp chắc chắn sẽ không hề đơn giản đâu」"
"2658" = "「Cả Kisaki và tôi đều có sở thích là hay suy nghĩ mà.\\nNên tôi cũng chẳng thể nói những câu an ủi kiểu như 『Đừng suy nghĩ nhiều quá』 được」"
"2443" = "「Ít nhất thì ở hiện trường, tôi cũng muốn giúp được gì đó」"
"2419" = "「Bằng cách giới thiệu tôi là vị hôn phu,\\nem định tạo cớ để mời cô ấy đến dự lễ cưới luôn sao」"
"2491" = "「Vậy đi tiếp khách thì tôi nên mặc đồ gì?\\nMặc vest bình thường có được không?」"
"2302" = "「Tôi đâu có ở vị thế để tham gia mấy chuyện đó.\\nTrước khi trở về Ohitoyo, tôi chỉ là nhân viên của một cửa hàng bán buôn rượu kiêm sinh viên Đại học Hoàng gia thôi mà」"
"2262" = "「Ừm――tôi muốn xem」"
"2445" = "「Tôi muốn ngắm nhìn dáng vẻ Kisaki trong bộ sườn xám」"
"2291" = "「Ừm. Cho tôi xem đi」"
"2429" = "「Tôi mong lắm rồi đấy. Nhanh cho tôi xem đi」"
"1993" = "「Không, cứ giữ nguyên như vậy đi.\\nĐừng che lại, hãy để tôi ngắm nhìn toàn bộ cơ thể em」"
"2510" = "「Cũng đúng. Cho đến khi em nói, tôi mới nhận ra đấy」"
"2387" = "「Sao thế. Tôi nói gì kỳ lạ à?」"
"2440" = "「Tôi thì, làm sao cơ?」"
"2640" = "「Kisaki. Tôi cũng hạnh phúc lắm.\\nCó thể em sẽ nghĩ tôi thực dụng, nhưng――」"
"3006" = "Dù vậy, trái tim tôi vẫn rung động đến nhường này.\\nKhông thể không nói ra thành lời."
"2428" = "「Khi thấy Kisaki xinh đẹp đến thế này,\\ntôi lại một lần nữa cảm nhận sâu sắc niềm hạnh phúc khi được một người phụ nữ xinh đẹp yêu thương」"
"2463" = "「Tôi biết Kisaki, chính là Kisaki.\\nTôi yêu tất cả mọi thứ thuộc về Kisaki, và cũng rất tôn trọng em」"
"2397" = "「Tôi không muốn làm tổn thương Kisaki, không muốn bóp méo con người em.\\nTôi sợ hãi hơn bất cứ điều gì, việc Kisaki không còn là Kisaki nữa」"
"2453" = "「Tôi khao khát cơ thể của Kisaki đến nhường này.\\nNhưng, nếu chỉ có cơ thể thôi thì chẳng có ý nghĩa gì cả」"
"2418" = "「Tôi, yêu mọi thứ thuộc về Kisaki. Nếu tách rời\\nbất cứ phần nào ra, thì đó không còn là Kisaki nữa」"
"2415" = "「Đó là, do tôi chưa quen thôi. Tôi sợ nếu cứ hành động theo dục vọng,\\nthì sẽ làm tổn thương Kisaki mất」"
"2612" = "「Tôi hiểu rồi」"
"2423" = "「Tôi đã làm đủ thứ mình thích rồi mà?」"
"2411" = "「Dù thế nào đi nữa――cũng sẽ theo ý muốn của tôi sao」"
"2789" = "「Ngoài vú ra, tôi cũng sẽ làm theo ý mình đấy」"
"2102" = "「Hãy cho tôi cảm nhận gần hơn nữa đi」"
"1987" = "「Không được sao? Nhưng tôi lại muốn nói đấy」"
"2775" = "「Và tôi muốn hỏi. Em hãy nói cho tôi biết.\\nTại sao cởi dây ra rồi mà quần lót vẫn không rớt xuống?」"
"2728" = "「Như Kisaki đã nói, tình dục mà tôi muốn,\\nchỉ là khao khát thể xác, tôi chỉ tạm thời thử xem sao thôi」"
"2698" = "「Nếu chỉ là thể xác thì tuyệt vời lắm. Rất sướng.\\nNhưng mà, khoái cảm vượt lên trên thế này, tôi đã biết rồi」"
"2462" = "「Người tôi biết, chỉ có Kisaki thôi. Với Kisaki――\\nTình dục không chỉ là thể xác, mà còn là sự hòa quyện của tâm hồn」"
"2251" = "「Đòi hỏi một chiều không phải là tình dục tôi muốn.\\nĐiều tôi muốn nhất và sướng nhất, là tình dục cùng Kisaki tạo ra」"
"2403" = "「Tôi cũng vậy」"
"2402" = "「Tôi cũng vậy――Kisaki」"
"2451" = "「Tôi rất vui.\\nNhưng mà, làm hỏng thì vẫn uổng lắm」"
"2768" = "「Nếu vậy tôi sẽ nằm xuống sofa nhé」"
"2648" = "「Đại diện cho shochu gạo thì tất nhiên là Kuma――Ohitoyo rồi.\\nCòn rượu sake thì――chắc là Niigata để lại ấn tượng mạnh nhất nhỉ」"
"3099" = "Bởi vì chúng tôi đã nhận được rất nhiều thứ không thể nào lấy lại được lần thứ hai,\\ntừ mọi người, và từ Ohitoyo."
"2740" = "「Bác ấy thậm chí còn mời được cựu Tổng giám đốc Đường sắt Hoàng gia,\\nngười vốn không có chút liên hệ nào với Ohitoyo, nhà Migita hay nhà Houshou, làm người mai mối cho chúng ta mà」"
"2972" = "Có lẽ cũng một phần do chính sách chống Minh Quốc của chính phủ,\\nmà việc phổ biến Aircra ở Trọng Quốc diễn ra muộn hơn Hinomoto khá nhiều."
"2468" = "「Chẳng phải anh bảo là 『cho em uống』 sao?\\nAnh Soutetsu, cho em」"
"1550" = "「『Vì đây là nhà của người con trai mà em thích』. Đấy nhé?」"
"3330" = "Là mùi hương của rượu."
"1552" = "「……Ư」"
"2003" = "「Đầu vú…… được, anh Soutetsu…… vuốt ve――……Ư\\nChỉ cần vậy, thôi――đã nóng ran――và cứng lại, thế này――」"
"2161" = "「Kya! Phu――~~~~~~~~Ư!!!」"
"2257" = "「Khu phư ưm~~~~Ư!!!」"
"2809" = "「Ư!」"
"2810" = "「Ư!!」"
"2813" = "「Ư!!?」"
"2814" = "「Ư!?」"
"2824" = "「~~~~~Ư!」"
"2826" = "「~~~~~~~~~Ư!!!?」"
"3143" = "Bất chợt, Kisaki cố gắng che giấu cơ thể mình――Ư!"
"2188" = "「Phù――hà――ưm――phua――ưm――\\n~~Ư! Hà――phua――ưm……ưm phu――」"
"2218" = "「~~~Ư!! Hà――chịu đựng, không nổi!\\nCố gắng, nhưng mà――không được! Cả âm đạo, cũng thế!」"
"2820" = "「~Ư!? Gay go――thì――dương, vật,\\ncho――âm đạo――nghỉ một chút――hya! Phu」"
"2170" = "「Ư~~~――phua, á――vú――ưm,\\nphù――phua――ưm――phù――phù」"
"2253" = "「Phua――ưm――anh, Soutetsu――tuyệt, quá――\\nƯ――giật, giật――liên hồi――nóng quá, to quá」"
"2158" = "「Kyaaa!?」"
"3483" = "Kisaki đang thực sự rất bồn chồn.\\nĐôi chân cứ xoắn xuýt vào nhau――!!?"
```

## Kết bài

File 稀咲h3_チャイナドレスでおもてなし.txt.toml đã audit xong toàn bộ 662 dòng: **75 dòng sai (11,3%)** — đại từ 50 (Soutetsu "anh"→"tôi" với Kisaki — lỗi hệ thống, 50/50 lần sai), gasp 16 (11 từ sweep + 5 sweep bỏ sót), sai nghĩa 4, thuật ngữ 3, SFX 1, dấu câu 1. Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 75 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 75/75, 0 bỏ, 0 sửa. Chờ Hieu: Kisaki gọi "anh Soutetsu" (33 dòng), fa/fu (§4), 帝鉄/帝大 dạng đầy đủ (2740/2302), 二干潟→"Niigata" (2648), くあっ→"Kua!" (2217), "Anh Houhehu"/"hích anh" (2238), しゅごっ→"Tuyệt quá!" (2155).
