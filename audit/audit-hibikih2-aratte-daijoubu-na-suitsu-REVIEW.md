# Audit — 日々姫h2_洗って大丈夫なスーツ.txt.toml

- File: `日々姫h2_洗って大丈夫なスーツ.txt.toml` — route 02_Hibiki, 290 dòng script (thoại: 日々姫 86, 双鉄H 60; độc thoại 144).
- Nội dung: Hibiki làm xong việc ở phòng thị trưởng rồi ngủ gật; Soutetsu bế em ấy (bế kiểu công chúa), cả hai thân mật trong phòng thị trưởng; xoay quanh bộ vest giặt được, chuyện tiết kiệm tiền giặt ủi, và mơ về ngôi nhà/gia đình chung của hai người. File H-scene (Hibiki route).
- **Kết quả: 16/290 dòng sai (5,5%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (290 dòng, key 37–1816, 0 khóa trùng, 0 ô VN trống); VN khớp TOML tuyệt đối 290/290 (0 lệch). `[selections]` rỗng. Không có thẻ `%l` nào trong JP lẫn VN — không có thẻ sai định dạng, không có thẻ VN tự thêm.
- TOML md5 `406a1ba5a7f06dc38f49413d0fbe2d47`; không có bản sao file này (không thuộc 11 nhóm trùng — đã kiểm tra md5 toàn bộ 227 file).
- Đại từ: không có dòng đại từ nào sai. Soutetsu "anh" với Hibiki đúng toàn file ở thoại (60 dòng 双鉄H); độc thoại (144 dòng) dùng "tôi" theo giọng kể — nhất quán toàn file, không phải lỗi. Hibiki gọi "anh hai"/"anh trai" đúng. 1552 義妹 → "em gái nuôi" đúng theo quyết 21/11 ~19:45 (nhà Migita là con nuôi).
- Thuật ngữ: không có thuật ngữ nào sai trong file (không xuất hiện 御一夜/帝鉄/整備体/運転体/市電/宮司; 市長 → "thị trưởng" đúng; スーツ → "vest" nhất quán).
- Gasp sweep: sweep có 4 mục cho file này — áp nguyên 3 (1085, 1086, 1283); mục 1071 là already-rendered (gasp đã diễn bằng Ưm, không cần sửa gasp — nhưng dòng này vẫn sai ở きゃっ→"Á" và びゅう bị mất, đã sửa riêng). Audit tự tìm thêm 1 gasp sweep bỏ sót (843 「っ――」→"Ư——"). Đã quét cơ học toàn bộ 176 dòng JP có っ: còn lại đều là っ giữa từ (ちゃった/って/っ…) hoặc âm đã diễn — không còn gasp nào mất.
- Hai nhóm VN trùng nhau trong file đều hợp lệ: 「Vậy à.」 (1198/1249 — JP đều 「そうか」); （Phụt! Phụt! Phụt! Phụt!） (1764/1766 — hai chuỗi SFX phun khác nhau nhưng cùng cách diễn, xem cờ cho vòng moan).

## §2. Danh sách sửa (16 dòng)

Phân loại: gasp 4 (843, 1085, 1086, 1283); moan 6 (1055, 1071, 1074, 1079, 1081, 1123); nguyên âm dài 3 (1077, 1078, 1138); dịch sai nghĩa 2 (1186, 1414); bịa thêm 1 (1107). Thoại 15/146 (10,3%), độc thoại 1/144 (0,7%). Theo nhân vật: 日々姫 12/86, 双鉄H 3/60, monologue 1/144.

### 843 — 双鉄H — gasp
- JP: 「っ――」
- TW: 「――」
- VN cũ: 「——」
- Sửa: 「Ư——」
- Lý do: JP 「っ――」 là gasp っ đầu dòng; VN cũ chỉ còn dấu gạch — âm mất hẳn. Thêm Ư theo quy tắc gasp (chỉ thêm khi っ mất hoàn toàn). Sweep bỏ sót dòng này (tiền lệ 995/1490/1562 cùng dạng).

### 1055 — 日々姫 — moan
- JP: 「やっ――やんっ！　おちんちん――にぃにの、ちんちん、\\nおまんこで――ぎゅって――抱きしめたいのにっ」
- TW: 「呀――呀！雞雞――阿哥的、雞雞，我本想用小穴――緊緊的――套住」
- VN cũ: 「A——Á! Cậu nhỏ——Cậu nhỏ của anh hai, em muốn dùng cô bé——ôm chặt lấy——cơ mà.」
- Sửa: 「A——Yan! Cậu nhỏ——Cậu nhỏ của anh hai, em muốn dùng cô bé——ôm chặt lấy——cơ mà.」
- Lý do: やんっ → "Á" làm mất ん. Các moan -ん khác trong file đều giữ n (ひゃんっ→"Hyan" 1062/1069, ふやんっ→"Phuyan" 1081, んきゅんっ→"Ưm kyun" 1139) → "Yan!".

### 1071 — 日々姫 — moan
- JP: 「きゃっ！？　射精っ――私、おちんちん、オナニーでっ\\n――びゅうって、射精――んっ――んううううう～っ！」
- TW: 「呀！？射了――我用雞雞、自慰――噗噗地射出來了――嗯――嗯啊～！」
- VN cũ: 「Á!? Xuất tinh rồi——Em, dùng cậu nhỏ, thủ dâm——mà, xuất tinh——Ưm——Ưm~~~!」
- Sửa: 「Kya!? Xuất tinh rồi——Em, dùng cậu nhỏ, thủ dâm——mà, phụt——xuất tinh——Ưm——Ưm~~~!」
- Lý do: きゃっ → "Á" vi phạm quy tắc ひゃ-family 21/11 (moan: ひゃ/ひゅ/ひあ/きゃ → romaji; "Á" chỉ đúng khi JP không có phụ âm mora) → "Kya!?". びゅうって (tiếng phun) bị mất — TW 噗噗地 có diễn → thêm "phụt" trước "xuất tinh" theo đúng thứ tự JP.

### 1074 — 双鉄H — moan
- JP: 「くはっ――あっ――」
- TW: 「呼――啊――」
- VN cũ: 「Kua——A——」
- Sửa: 「Kuha——A——」
- Lý do: くはっ → "Kua" làm mất は (kuha → kua) → "Kuha".

### 1077 — 日々姫 — nguyên âm dài
- JP: 「ふぅぅぅぅぅぅぅぅんっっ！」
- TW: 「呼嗯！」
- VN cũ: 「Fuuuuuuun!」
- Sửa: 「Fuuuuuuuuun!」
- Lý do: JP ふ + ぅ×8 = 9 nguyên âm u theo công thức (1 + số う/ぅ); VN cũ 7 u → 9 u.

### 1078 — 日々姫 — nguyên âm dài
- JP: 「はっ！　あっ！　あああああああんっ！！！」
- TW: 「呼！啊！啊啊啊！！！」
- VN cũ: 「Hơ! A! Aaaaaaaan!!!」
- Sửa: 「Hơ! A! Aaaaaaan!!!」
- Lý do: JP đoạn dài あ×7 (+ ん); VN cũ 8 a ở đoạn dài → 7 a.

### 1079 — 日々姫 — moan
- JP: 「ふあっ！　あんっ！　んっ――\\nにぃにっ――にぃにぃっ！」
- TW: 「呼！啊！嗯――阿哥――阿哥！」
- VN cũ: 「Phù! A! Ưm——Anh hai——Anh hai!」
- Sửa: 「Phùa! A! Ưm——Anh hai——Anh hai!」
- Lý do: ふあっ → "Phù!" làm mất あ; quy tắc fa/fu: ふあ → "phùa" → "Phùa!".

### 1081 — 日々姫 — moan
- JP: 「ふやんっ！！」
- TW: 「哎呀！！」
- VN cũ: 「Huyan!!」
- Sửa: 「Phuyan!!」
- Lý do: ふやんっ → "Huyan!!" — phụ âm đầu không theo quy tắc khóa ふやぁ→"phuya" → "Phuyan!!".

### 1085 — 日々姫 — gasp
- JP: 「えへへ、にぃに～っ」
- TW: 「哎嘿嘿，阿哥～」
- VN cũ: 「Ê hê hê, anh hai~」
- Sửa: 「Ê hê hê, anh hai~Ư」
- Lý do: Sweep lost-gasp-trailing — áp nguyên: JP gasp cuối sau ~, VN cũ bỏ gasp.

### 1086 — 日々姫 — gasp
- JP: 「えへへ～っ」
- TW: 「哎嘿嘿～」
- VN cũ: 「Ê hê hê~」
- Sửa: 「Ê hê hê~Ư」
- Lý do: Sweep lost-gasp-trailing — áp nguyên: JP gasp cuối sau ~, VN cũ bỏ gasp.

### 1107 — 日々姫 — bịa thêm
- JP: 「あ……すごい……私、ちゃんと……にぃにの、\\nあんなに、おっきいの――」
- TW: 「啊……好厲害……我把……阿哥的、那個大的――」
- VN cũ: 「A... Tuyệt quá... Em, đã thực sự... chứa được thứ to lớn, như thế, của anh hai——」
- Sửa: 「A... Tuyệt quá... Em, đã thực sự... thứ to lớn, như thế, của anh hai——」
- Lý do: JP cụt ở おっきいの――; TW cũng cụt. VN cũ bịa thêm động từ "chứa được" để hoàn thiện câu → bỏ, giữ cụt theo quy tắc không bịa phần hoàn thiện cho JP cụt.

### 1123 — 日々姫 — moan
- JP: 「んッ――ふあっ――あんっ！」
- TW: 「嗯――—呼――啊！」
- VN cũ: 「Ưm——Phù——A!」
- Sửa: 「Ưm——Phùa——A!」
- Lý do: ふあっ → "Phù" làm mất あ → "Phùa" (như 1079).

### 1138 — 日々姫 — nguyên âm dài
- JP: 「んきゅうううううううぅぅぅぅっ！！！」
- TW: 「嗯啊啊啊！！！」
- VN cũ: 「Ưm kyuuuuuuuu!!!」
- Sửa: 「Ưm kyuuuuuuuuuuuu!!!」
- Lý do: JP きゅ + う×7 + ぅ×4 = 12 u theo công thức (1 + số う/ぅ); VN cũ 8 u → 12 u.

### 1186 — 日々姫 — dịch sai nghĩa
- JP: 「なるから！　私っ――妊娠――する、からっ――\\nだから――にぃに――私の――おなかでっ――」
- TW: 「我願意！我――願意懷孕――所以――阿哥――射在我裡面――」
- VN cũ: 「Sẽ chảy mà! Em——sẽ mang thai——mà——Thế nên——Anh hai——Vào trong bụng——của em——」
- Sửa: 「Sẽ thành mà! Em——sẽ mang thai——mà——Thế nên——Anh hai——Vào trong bụng——của em——」
- Lý do: なるから = "sẽ thành (có thai)"; VN cũ "Sẽ chảy mà!" bịa "chảy" (なる ≠ 流れる), TW 我願意 cũng không ủng hộ "chảy" → "Sẽ thành mà!". Phần "Vào trong bụng của em——" giữ nguyên: TW 射在我裡面 ủng hộ động từ vào.

### 1283 — 双鉄H — gasp
- JP: 「っ！？」
- TW: 「！？」
- VN cũ: 「!?」
- Sửa: 「Ư!?」
- Lý do: Sweep lost-gasp-whole — áp nguyên: JP cả dòng chỉ là gasp っ!?; VN cũ chỉ còn dấu câu.

### 1414 — monologue — dịch sai nghĩa
- JP: 可愛い。嬉しい。愛おしい。\\n大事にしたくて、おもいっきりに甘やかしたくて。
- TW: 她真可愛，我好高興，真是惹人喜歡了。我好想憐愛她一番，好好寵愛她一番。
- VN cũ: Thật đáng yêu. Thật vui sướng. Thật đáng thương. Muốn trân trọng em ấy, muốn cưng chiều em ấy hết mực.
- Sửa: Thật đáng yêu. Thật vui sướng. Thật đáng quý. Muốn trân trọng em ấy, muốn cưng chiều em ấy hết mực.
- Lý do: 愛おしい = "đáng yêu quý, đáng trân trọng" (TW 惹人喜歡); VN cũ "đáng thương" (= đáng tội nghiệp) sai nghĩa → "đáng quý".

## §3. Giữ nguyên có lý do

- 846/1256 すぅ……すぅ → "Khò... khò." (tiếng thở khi ngủ) — giữ.
- 1031 「僕が、ではない。あの姿見が、だ」 → VN thêm "nhìn" — TW 不是看我 cũng thêm 看, JP+TW ủng hộ.
- 1064 かっ bị mất — TW cũng bỏ (呼――啊), JP+TW đồng thuận → giữ; cờ cho vòng moan.
- 1102 付け根 → "gốc đùi" theo TW 腿根.
- 1111/1125/1246 これ → "Thế này" — nhất quán toàn file, giữ.
- 1141/1151/1157 うん → "Vâng" — nhất quán toàn file, giữ.
- 1184 だ、大丈夫 → "Ch, chắc là..." — vấp "Ch" mở đầu "Chắc", giữ.
- 1205 "sinh ra... là để..." — TW 生來就是 ủng hộ.
- 1222 "ít nhất cũng phải trả được tiền giặt ủi" — TW 乾洗費還是出得起的吧 ủng hộ.
- 1042/1166 dấu "." ở mệnh đề hỏi — JP và TW đều không dùng "?" → giữ, đã cân nhắc, không tính sai.
- 1405 先走り → "chất dịch nhầy nhụa" — TW cũng diễn chung chung, giữ.
- 1480 手の筒 → "vòng tay đang siết chặt" — TW 雙手組成的洞穴, giữ.
- 1613 "vách âm đạo" cho 壁 — JP mơ hồ, giữ.
- 1763 ずりゅっ → "Phập" (trong khi 1809 cùng âm → "Sột soạt") — SFX ngẫu hứng theo Hieu, giữ; cờ vòng moan.
- 1764/1766/1771 dồn 4 biến thể びゅ thành một từ "Phụt" — giữ nghĩa phun; cờ vòng moan.
- 1787/1797/1798 độ dài diễn bằng phụ âm t ("Trượtttttt", "Siết chặtttt") — kiểu SFX, giữ; cờ vòng moan.
- 1028 "Nóng, quá"/"ngứa ngáy quá" — thêm "quá" làm từ nhấn trong rên, giữ (ranh giới, không tính sai).
- 1071 đuôi moan んううううう～っ → "Ưm~~~!" — giữ nguyên hình thức ~~~, cờ cho vòng moan.
- 1076 ふあ……ぁ…… → "Phù... a..." — diễn đủ cả hai mora ふ và あ, giữ (khác 1079/1123 ふあっ → "Phù" làm mất あ).

## §4. Cờ cho Hieu

- (1) 1071 đuôi moan んううううう～っ → "Ưm~~~!" — dấu ~~~ thay cho nguyên âm dài theo công thức; để vòng moan quyết hình thức cuối.
- (2) 1064 かっ bị mất (TW cũng bỏ) — vòng moan.
- (3) 1770 びゅくっ → "Giật" (TW toàn 噗噗 = phun) — "Giật" diễn co giật thay vì phun; vòng moan.
- (4) SFX phun 1764/1766/1771 dồn 4 biến thể びゅ thành một từ "Phụt"; 1764 và 1766 cùng VN （Phụt! Phụt! Phụt! Phụt!） — vòng moan.
- (5) fa/fu "Phùa" vs "Fua" chưa chốt → đợt thống nhất (file này dùng "Phùa" cho ふあっ theo quy tắc khóa hiện hành).
- (6) B19 vẫn park (không có thẻ %l nào trong file này).
- (7) Ghi chú dữ liệu: file làm việc /tmp của audit này bị ghi đè bởi một tiến trình khác giữa chừng (nội dung một file Hibiki khác) — đã kiểm chứng lại toàn bộ từ CSV3/TOML gốc; mọi số liệu trong review này lấy từ nguồn gốc, không từ /tmp.

- Lượt soát 2: 16/16 fix đã đọc lại toàn bộ giá trị sửa đối chiếu JP, 0 bỏ, 0 sửa.

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
843 = "「Ư——」"
1055 = "「A——Yan! Cậu nhỏ——Cậu nhỏ của anh hai, em muốn dùng cô bé——ôm chặt lấy——cơ mà.」"
1071 = "「Kya!? Xuất tinh rồi——Em, dùng cậu nhỏ, thủ dâm——mà, phụt——xuất tinh——Ưm——Ưm~~~!」"
1074 = "「Kuha——A——」"
1077 = "「Fuuuuuuuuun!」"
1078 = "「Hơ! A! Aaaaaaan!!!」"
1079 = "「Phùa! A! Ưm——Anh hai——Anh hai!」"
1081 = "「Phuyan!!」"
1085 = "「Ê hê hê, anh hai~Ư」"
1086 = "「Ê hê hê~Ư」"
1107 = "「A... Tuyệt quá... Em, đã thực sự... thứ to lớn, như thế, của anh hai——」"
1123 = "「Ưm——Phùa——A!」"
1138 = "「Ưm kyuuuuuuuuuuuu!!!」"
1186 = "「Sẽ thành mà! Em——sẽ mang thai——mà——Thế nên——Anh hai——Vào trong bụng——của em——」"
1283 = "「Ư!?」"
1414 = "Thật đáng yêu. Thật vui sướng. Thật đáng quý. Muốn trân trọng em ấy, muốn cưng chiều em ấy hết mực."
```

## Kết bài

File 日々姫h2_洗って大丈夫なスーツ.txt.toml: 290 dòng đã đọc đủ, 16 dòng sai (5,5%) — lỗi tập trung ở rên/moans H-scene (gasp 4: 843, 1085, 1086, 1283; moan mất âm 6: 1055, 1071, 1074, 1079, 1081, 1123; nguyên âm dài 3: 1077, 1078, 1138; dịch sai nghĩa 2: 1186, 1414; bịa thêm 1: 1107). Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Độc thoại "tôi" / thoại "anh" với Hibiki nhất quán, không lỗi đại từ. Cờ cho Hieu: đuôi moan 1071, かっ 1064, "Giật" 1770, SFX phun dồn, fa/fu "Phùa" vs "Fua" → đợt thống nhất; B19 vẫn park.
