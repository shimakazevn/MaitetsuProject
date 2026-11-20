# Audit lr_凪h2 — lr_凪h2_虎さんの交尾.txt.toml

**Ngày kiểm toán:** 20/11/2026
**Tệp TOML:** `07_Nagi_Fukami/lr_凪h2_虎さんの交尾.txt.toml` — md5 `4f26c5ed7e6e0d076848d8be1add75a7`, 60.808 byte, BOM, CRLF (604 CRLF, 0 LF-only), `[selections]` rỗng, **không có bản sao trùng** (kiểm tra md5 toàn bộ 227 tệp TOML).
**Nguồn CSV:** "Trang tính 3" — bộ hàng duy nhất `07_Nagi_Fukami` (không có bẫy dual-set ở file này), 293 hàng `[script]`.
**Kết quả: 46/293 dòng sai (15,7%), 0 dòng chưa chắc chắn, 0 dòng lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo file.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| SFX hơi thở fa/fu (quy tắc đã chốt) | 38 |
| Gasp っ bị mất | 7 |
| Sai nghĩa (meaning) | 1 |
| **Tổng** | **46** |

Key 1247 mang cả hai lỗi gasp + fa/fu (tính vào nhóm SFX trong bảng); tổng số dòng chạm vào gasp là 8. Nhóm SFX (38): ふぁ→"phà" 17 dòng (gồm 2 dòng kéo dài: 1273 ふぁぁうんっ→"Phàaun", 1278 ふぁぁぁぁぁぁぁんっ→"Phàaaaaaan" — giữ đủ 7 âm a và âm mũi ん), ふあっ→"phù" 19 dòng, ふあ (không っ)→"phùa" 3 dòng (1280, 1366, 1213) + 1 dòng bị cắt bởi ――→"phù" (1232), ふぇ→"phuê" 1 dòng, ふやっ→"phuya" 1 dòng, ふっ→"phù" 1 dòng (1199 mang cả 3: ふあっ + ふやっ + ふっ; 1273 mang ふぁぁうんっ + ふあっ; 1304 mang ふぁっ + ふあっ; 1280 mang ふぇ + ふあ). Nhóm gasp (7 tính riêng + 1247): 6 từ sweep áp nguyên đã kiểm chứng (1220, 1221, 1222, 1268, 1296 + 1247) và 2 gasp sweep bỏ sót bắt được khi quét bổ sung (1185, 1339). Sai nghĩa (1): 1124 (thiếu động từ "làm").

**Theo loại dòng:** thoại 46/170 sai (27,1%), độc thoại 0/123 sai (0%). **Theo nhân vật:** 凪 (Nagi) 45, 双鉄 (Soutetsu) 1, monologue 0.

File này sạch về cấu trúc — 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng, 0 dòng chưa chắc chắn. Lỗi tập trung ở một lỗi hệ thống duy nhất: toàn bộ 38 tiếng thở ふぁ/ふあ của Nagi đều để nguyên dạng La-tinh "Fua"/"fua" (trái quy tắc fa/fu đã chốt 19/11 và đã áp dụng ở các file h1/h2/lr-h1/lr-h2 và file h1 cùng route — 22 dòng). Toàn bộ 46 lỗi đều sửa được tại chỗ, không cần dịch lại.

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục. TOML md5 `4f26c5ed7e6e0d076848d8be1add75a7`, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng trong 227 tệp (file này chỉ có 1 copy).
- **CSV vs TOML:** VN khớp tuyệt đối 131 hàng; khớp sau khi gộp ký tự xuống dòng thành khoảng trắng 162 hàng; **0 khác biệt thực chất** — toàn bộ là hiện tượng gộp `\n` trong TOML-2. CSV3 là bản chuẩn cho fix list. JP comment trong TOML khớp CSV3 293/293.
- **Sweep っ (gasp):** kiểm tra trực tiếp sweep-raw-gasp-wrong.json — file này CÓ 6 mục, cả 6 áp nguyên đã kiểm chứng (1220, 1221, 1222, 1247, 1268, 1296). Quét bổ sung toàn bộ 223 dòng JP chứa っ: bắt thêm 2 gasp sweep bỏ sót (1185: っ trần giữa dòng "っ――"; 1339: "――っ、くっ――" hai tiếng nhưng VN chỉ diễn một). Không còn gasp っ trần nào khác bị mất.
- **Thẻ %l:** JP 0 thẻ, VN 0 thẻ — không có thẻ nào trong file này.
- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng: 0), không có VN mồ côi (orphan: 0), không có key trùng, không có hàng VN == TW.
- **Kiểm tra nhiễm chéo:** đối chiếu 46 giá trị VN cũ trong fix list + toàn bộ VN của file qua chỉ mục VN toàn dự án (91.731 dòng) — 31 lần trùng đều là câu ngắn thông dụng hoặc SFX lặp lại hợp lệ (「Ừm.」, 「Hả?」, (Chụt), (Phập!)…) dịch độc lập giống nhau; 0 lần trùng VN trong file với JP khác nhau. 2 cặp VN trùng trong file (1295/1332 「Ừm.」; 1296/1266 「!」) đều là cảm thán ngắn hợp lệ với JP khác nhau, không phải lệch dòng.
- **Đại từ:** Soutetsu tự xưng "anh" với Nagi trong toàn bộ thoại (0 lần "tôi" trong 62 dòng thoại 双鉄 — đúng quy tắc đã sửa 20/11: "anh" với Nagi/Fukami); độc thoại dùng "tôi" nhất quán; Nagi gọi Soutetsu "anh Soutetsu" (にーさん) nhất quán trong mọi dòng; Soutetsu gọi Nagi "em" nhất quán. Địa chỉ người nghe xác định từ nội dung dòng + mạch hội thoại, không dùng key kề nhau theo thứ tự số.
- **Thuật ngữ đã chốt:** không có từ nào trong danh sách quyết định xuất hiện sai trong file (0 "Ohimitera", 0 "Yui", 0 "Migita System", 0 "Teitetsu" sai dạng, 0 "cô" xưng hô sai).

## 3. Các lỗi đã sửa (46 dòng)

### 1124 — 凪 — meaning

**JP:** 「そぎゃん実況恥ずかしかとばい！！！⏎見るより、しゃべるより、もっと――もっとぉ」

**TW:** 「不要做這麼羞人的解說！！別看了，別說了，下手，下手嘛」

**VN cũ:** 「Tường thuật trực tiếp như vậy xấu hổ lắm!!!⏎Đừng nhìn nữa, đừng nói nữa, hãy——nữa đi」

**Fix:** 「Tường thuật trực tiếp như vậy xấu hổ lắm!!!⏎Đừng nhìn nữa, đừng nói nữa, làm đi——làm nữa đi」

JP 「見るより、しゃべるより、もっと――もっとぉ」 = "đừng nhìn, đừng nói nữa, làm nữa đi" (TW: 「別看了，別說了，下手，下手嘛"); VN cũ "hãy——nữa đi" thiếu động từ, câu dở dang.

### 1172 — 凪 — sfx

**JP:** 「ヒャう――あっ――にぃさん――にぃさぁん――⏎ふあっ！　もっと――ねっ――もっと――直接ぅ――ん」

**TW:** 「呀……啊……大哥哥……大哥哥……啊！再……那個……再直接一點……嗯」

**VN cũ:** 「Hyau——a——anh Soutetsu——anh Soutetsu——⏎Fua! Nữa đi——nhé——nữa đi——trực tiếp vào——ưm」

**Fix:** 「Hyau——a——anh Soutetsu——anh Soutetsu——⏎Phù! Nữa đi——nhé——nữa đi——trực tiếp vào——ưm」

Quy tắc fa/fu: ふあっ → "phù".

### 1174 — 凪 — sfx

**JP:** 「ひゃっ――ンッ――どうして、脇、と？　凪、さま⏎――ふぁっ――こぎゃんと――くすぐったか、と――」

**TW:** 「呀……嗯……為什麼是腋下？本小姐……啊……怕癢……」

**VN cũ:** 「Hya——ưm——sao lại, là nách, chứ? Nagi⏎——fua——chỗ đó——nhột lắm——」

**Fix:** 「Hya——ưm——sao lại, là nách, chứ? Nagi⏎——phà——chỗ đó——nhột lắm——」

Quy tắc fa/fu: ふぁっ → "phà".

### 1181 — 凪 — sfx

**JP:** 「ひうっ！？　やっ！　おしっこのとこ――んっ！⏎ふあっ！　そんなとこ――すったら――ばっちかばい」

**TW:** 「呀！呀！是尿尿的地方……嗯！啊！吸這種地方……好髒」

**VN cũ:** 「Hiu!? Á! Chỗ đi tiểu——ưm!⏎Fua! Chỗ đó——mà hút thì——bẩn lắm」

**Fix:** 「Hiu!? Á! Chỗ đi tiểu——ưm!⏎Phù! Chỗ đó——mà hút thì——bẩn lắm」

Quy tắc fa/fu: ふあっ → "phù".

### 1185 — 凪 — gasp

**JP:** 「ひゃぐっ！？　っ――ひゅぁぁぁぁぁぁぁあああん！」

**TW:** 「呀？！呀！」

**VN cũ:** 「Hyagu!? ——Hyuaaaaaa!」

**Fix:** 「Hyagu!? Ư——Hyuaaaaaa!」

Sweep BỎ SÓT: っ trần giữa dòng ("っ――") sau "！？" — tiếng hít bị mất, VN chỉ giữ dấu gạch. Bổ sung "Ư" (quy tắc "không để mất âm").

### 1187 — 凪 — sfx

**JP:** 「ひゃうううっ！？　やっ！　やらっ！　抜けちゃうっ！⏎おまんこから、いっちゃう！　おちんち――ふあっ！？」

**TW:** 「呀？！呀！不要！要出去了！要離開下面了！雞雞……啊！」

**VN cũ:** 「Hyauuu!? Á! Không chịu! Tuột ra mất!⏎Ra khỏi cô bé mất! Cậu nhỏ——fua!?」

**Fix:** 「Hyauuu!? Á! Không chịu! Tuột ra mất!⏎Ra khỏi cô bé mất! Cậu nhỏ——phù!?」

Quy tắc fa/fu: ふあっ → "phù".

### 1188 — 凪 — sfx

**JP:** 「ひゃうぅうっ！？　ふぁっ――あっ――」

**TW:** 「呀？！哇……啊……」

**VN cũ:** 「Hyauuu!? Fua——a——」

**Fix:** 「Hyauuu!? Phà——a——」

Quy tắc fa/fu: ふぁっ → "phà".

### 1190 — 凪 — sfx

**JP:** 「ひゃうっ！？　ふぁっ――あっ――きもち、よか、けど、⏎ん――いま見てほしいのは――もっと下――がお」

**TW:** 「呀？！哇……啊，好舒服，可是，唔……現在咱想讓你看更下面嗷」

**VN cũ:** 「Hyau!? Fua——a——sướng, lắm, nhưng mà,⏎ưm——bây giờ em muốn anh nhìn——xuống dưới cơ——gao」

**Fix:** 「Hyau!? Phà——a——sướng, lắm, nhưng mà,⏎ưm——bây giờ em muốn anh nhìn——xuống dưới cơ——gao」

Quy tắc fa/fu: ふぁっ → "phà".

### 1193 — 凪 — sfx

**JP:** 「んひっ！？　ふあっ――べろ――にーさんのべろが⏎おまんこ――おまんこっ――ぞりゅって、べちゅって」

**TW:** 「呀？！啊……口水……大哥哥的口水打在下面……」

**VN cũ:** 「Nhi!? Fua——lưỡi——lưỡi của anh⏎cô bé——cô bé——đang liếm, đang mút」

**Fix:** 「Nhi!? Phù——lưỡi——lưỡi của anh⏎cô bé——cô bé——đang liếm, đang mút」

Quy tắc fa/fu: ふあっ → "phù". ("べろ" = lưỡi, VN "lưỡi của anh" đúng theo JP; TW "口水" sai — JP thắng TW.)

### 1199 — 凪 — sfx

**JP:** 「ふあっ――あっ！　あ！　あ！　あっ――⏎んっ――ふやっ――きもち、よか――んっ――ふっ」

**TW:** 「哇……啊！啊！啊！啊……嗯……呀……好舒服……嗯……呼」

**VN cũ:** 「Fua——a! A! A! A——⏎Ưm——fuya——sướng, quá——ưm——fu」

**Fix:** 「Phù——a! A! A! A——⏎Ưm——phuya——sướng, quá——ưm——phù」

Quy tắc fa/fu: ふあっ → "phù"; ふやっ → "phuya"; ふっ cuối dòng → "phù" (tiền lệ lr-h2: ふっ "Phu" → "Phù").

### 1202 — 凪 — sfx

**JP:** 「ふあっ」

**TW:** 「哇」

**VN cũ:** 「Fua」

**Fix:** 「Phù」

Quy tắc fa/fu: ふあっ → "phù".

### 1203 — 凪 — sfx

**JP:** 「ふあっ！　やぁっ！　やぁああっ！　にーさんの、⏎おちんち、んっ――こわ――こわれるの――やあっ！」

**TW:** 「哇！不要！不要啊！大哥哥的雞雞……要把咱弄瘋了……不要啊！」

**VN cũ:** 「Fua! Á! Áaaa! Cậu nhỏ của anh,⏎ưm——hỏng——hỏng mất——á!」

**Fix:** 「Phù! Á! Áaaa! Cậu nhỏ của anh,⏎ưm——hỏng——hỏng mất——á!」

Quy tắc fa/fu: ふあっ → "phù".

### 1205 — 凪 — sfx

**JP:** 「ふぁっ！　はぁっ！　はぁ！　はぁっ！⏎はぁっ！　はあっ！　はあっ！　はあっ！」

**TW:** 「哇！啊！啊！啊！啊！啊！啊！啊！」

**VN cũ:** 「Fua! Ha! Ha! Ha!⏎Ha! Ha! Ha! Ha!」

**Fix:** 「Phà! Ha! Ha! Ha!⏎Ha! Ha! Ha! Ha!」

Quy tắc fa/fu: ふぁっ → "phà".

### 1207 — 凪 — sfx

**JP:** 「ふあっ！　あっ！　あ！　あっ！　こわ、れるっ――⏎うちのっ――うちの、おまんこ――こわれちゃう――ん」

**TW:** 「哇！啊！啊！啊！要瘋了……咱的……咱的下面……要瘋掉了……嗯」

**VN cũ:** 「Fua! A! A! A! Hỏng, mất——⏎của em——cô bé của em——sẽ hỏng mất——ưm」

**Fix:** 「Phù! A! A! A! Hỏng, mất——⏎của em——cô bé của em——sẽ hỏng mất——ưm」

Quy tắc fa/fu: ふあっ → "phù".

### 1210 — 凪 — sfx

**JP:** 「ふぁっ！？　ひゃうっ！　やぁらっ、はずかしかっ、⏎おしっこの、とこ――んっ！　つんつん、されるのぉ」

**TW:** 「哇？！呀！討厭，好害羞，尿尿的地方被頂著，好害羞」

**VN cũ:** 「Fua!? Hyau! Không chịu đâu, xấu hổ lắm,⏎chỗ đi tiểu——ưm! Cứ bị chọc chọc, vào đó」

**Fix:** 「Phà!? Hyau! Không chịu đâu, xấu hổ lắm,⏎chỗ đi tiểu——ưm! Cứ bị chọc chọc, vào đó」

Quy tắc fa/fu: ふぁっ → "phà".

### 1213 — 凪 — sfx

**JP:** 「ふあああああっ！？　待ってっ！　待ってっ、⏎にーさん！　いま、うち――うちのおまんこ――ふあ！」

**TW:** 「哇？！等一下！等一下，大哥哥！現在，咱……咱的下面……啊！」

**VN cũ:** 「Fuaaaaa!? Đợi đã! Đợi đã,⏎anh Soutetsu! Bây giờ, em——cô bé của em——fua!」

**Fix:** 「Phùaaaaa!? Đợi đã! Đợi đã,⏎anh Soutetsu! Bây giờ, em——cô bé của em——phùa!」

Quy tắc fa/fu: ふあああああっ (ふ+5 あ) → "Phùaaaaa" (giữ 6 nguyên âm); ふあ (không っ) → "phùa".

### 1220 — 凪 — gasp

**JP:** 「んひゅっ！　――～～～～～～～～～～～～っ！！！」

**TW:** 「唔！嗯！！！」

**VN cũ:** 「Nhyu! ——~~~~~~~~~~~~!!!」

**Fix:** 「Nhyu! ——~~~~~~~~~~~~Ư!!!」

Sweep lost-gasp-trailing, kiểm chứng đúng vs JP: 「んひゅっ！　――～～～～～～～～～～～～っ！！！」 — っ cuối sau dãy ~ bị mất.

### 1221 — 双鉄 — gasp

**JP:** 「っ！！」

**TW:** 「唔！！」

**VN cũ:** 「!!」

**Fix:** 「Ư!!」

Sweep lost-gasp-whole, kiểm chứng đúng vs JP: cả dòng chỉ là "っ！！" — VN chỉ còn dấu câu.

### 1222 — 双鉄 — gasp

**JP:** 「っ！！！」

**TW:** 「唔！！！」

**VN cũ:** 「!!!」

**Fix:** 「Ư!!!」

Sweep lost-gasp-whole, kiểm chứng đúng vs JP: cả dòng chỉ là "っ！！！" — VN chỉ còn dấu câu.

### 1229 — 凪 — sfx

**JP:** 「ふぁ――ひゃうっ――あっ……ん……んへへっ――⏎凪、さま――凪さま――んっ――うれしかと……ふぁっ」

**TW:** 「啊……呀……啊……嗯……嘿嘿，本小姐……本小姐……嗯……好開心……啊」

**VN cũ:** 「Fua——hyau——a……ưm……nhehe——⏎Nagi——Nagi——ưm——vui lắm……fua」

**Fix:** 「Phà——hyau——a……ưm……nhehe——⏎Nagi——Nagi——ưm——vui lắm……phà」

Quy tắc fa/fu: ふぁ → "phà" (×2). Tiếng cười "nhehe" (んへへっ) GIỮ — chờ quyết chung.

### 1232 — 双鉄 — sfx

**JP:** 「ふあ――ぁっ――」

**TW:** 「啊……啊……」

**VN cũ:** 「Fua——a——」

**Fix:** 「Phù——a——」

Quy tắc fa/fu: ふあ (bị cắt bởi ――, như っ) → "phù"; ぁっ → "a" giữ nguyên.

### 1235 — 凪 — sfx

**JP:** 「あっ――ふぁ――あっ――」

**TW:** 「啊……啊……啊……」

**VN cũ:** 「A——fua——a——」

**Fix:** 「A——phà——a——」

Quy tắc fa/fu: ふぁ → "phà".

### 1236 — 凪 — sfx

**JP:** 「ふぁ――ふぁ――アッっ――あっ――⏎にぃさん――ね――にぃさん――にぃさぁああん」

**TW:** 「啊……啊……啊……啊……大哥哥，大哥哥……大哥哥」

**VN cũ:** 「Fua——fua——A——a——⏎Anh Soutetsu——nè——anh Soutetsu——anh Soutetsuuuuu」

**Fix:** 「Phà——phà——A——a——⏎Anh Soutetsu——nè——anh Soutetsu——anh Soutetsuuuuu」

Quy tắc fa/fu: ふぁ → "phà" (×2).

### 1237 — 凪 — sfx

**JP:** 「ふぁ――あっ……んっ――あっ――にーさん――⏎にーさん――しゅき――すき――だいすきぃ」

**TW:** 「啊……啊……嗚……啊……大哥哥，大哥哥……愛你……愛你……愛死你了」

**VN cũ:** 「Fua——a……ưm——a——anh Soutetsu——⏎anh Soutetsu——yêu——yêu——yêu anh lắm」

**Fix:** 「Phà——a……ưm——a——anh Soutetsu——⏎anh Soutetsu——yêu——yêu——yêu anh lắm」

Quy tắc fa/fu: ふぁ → "phà".

### 1241 — 凪 — sfx

**JP:** 「ぁっ――っ――にーさん……エッチ、ばい……ふぁ……⏎凪さまの、ちっちゃか、おっぱい――そぎゃん、夢中に」

**TW:** 「啊……啊……大哥哥……好色情……啊……竟然對本小姐的……小小胸部……這麼沉醉」

**VN cũ:** 「A——a——anh Soutetsu……dâm đãng, quá……fua……⏎Say mê, ngực nhỏ, của Nagi——đến vậy sao」

**Fix:** 「A——a——anh Soutetsu……dâm đãng, quá……phà……⏎Say mê, ngực nhỏ, của Nagi——đến vậy sao」

Quy tắc fa/fu: ふぁ → "phà". (Hai tiếng "ぁっ――っ――" VN đã diễn đủ "A——a——", không sửa.)

### 1243 — 凪 — sfx

**JP:** 「ふぁっ――あっ――うれしかっ――あつか――[ぬく]温かぁ⏎――んっ――たくさん――精液――にいさん、のっ――」

**TW:** 「啊……啊……好開心，好暖……溫溫的……嗯……好多精液……都是大哥哥的」

**VN cũ:** 「Fua——a——vui quá——nóng quá——ấm quá⏎——ưm——nhiều quá——tinh dịch——của anh Soutetsu——」

**Fix:** 「Phà——a——vui quá——nóng quá——ấm quá⏎——ưm——nhiều quá——tinh dịch——của anh Soutetsu——」

Quy tắc fa/fu: ふぁっ → "phà". (Ruby [ぬく]温かぁ: VN "ấm quá" đã diễn đúng, không sửa.)

### 1247 — 凪 — sfx

**JP:** 「はっ――あっ――それっ――もっと――にーさん、⏎いまの――もっと――ふあっ！　もっとぉっ――っ！」

**TW:** 「啊……啊……這個，再來……大哥哥，剛才這個，再來……啊！再來！」

**VN cũ:** 「Ha——a——cái đó——nữa đi——anh Soutetsu,⏎lúc nãy ấy——nữa đi——fua! Nữa đi——!」

**Fix:** 「Ha——a——cái đó——nữa đi——anh Soutetsu,⏎lúc nãy ấy——nữa đi——phù! Nữa đi——Ư!」

Sweep lost-gasp-trailing (kết "もっとぉっ――っ！" → "Nữa đi——Ư!") + quy tắc fa/fu: ふあっ → "phù" ("fua" là La-tinh).

### 1248 — 凪 — sfx

**JP:** 「ふあっ――あ、おっぱい――んっ……凪さま、⏎キスであっつくなって、汗、かいてきたけん」

**TW:** 「啊……啊，胸部……嗯……本小姐吻得全身是汗了」

**VN cũ:** 「Fua——a, ngực——ưm……Nagi,⏎nóng rực lên vì nụ hôn, đổ cả mồ hôi rồi này」

**Fix:** 「Phù——a, ngực——ưm……Nagi,⏎nóng rực lên vì nụ hôn, đổ cả mồ hôi rồi này」

Quy tắc fa/fu: ふあっ → "phù" (tiền lệ h2 1008).

### 1250 — 凪 — sfx

**JP:** 「ふぁ――あっ――そこっ――しゅき――んっ――⏎にぃさぁん――もっと――もっと――もっと、してぇ」

**TW:** 「啊……啊，這裡，喜歡……嗯……大哥哥，用力，用力，再用力」

**VN cũ:** 「Fua——a——chỗ đó——thích lắm——ưm——⏎Anh Soutetsu——nữa đi——nữa đi——làm mạnh, hơn đi」

**Fix:** 「Phà——a——chỗ đó——thích lắm——ưm——⏎Anh Soutetsu——nữa đi——nữa đi——làm mạnh, hơn đi」

Quy tắc fa/fu: ふぁ → "phà".

### 1254 — 凪 — sfx

**JP:** 「ふぁ――そう、おちんちん、で――おまんこ、もっと⏎――じゅぶじゅぶって――して――んっ――は、あっ」

**TW:** 「啊……對，用雞雞……更猛烈一點……啊，啊」

**VN cũ:** 「Fua——đúng rồi, dùng cậu nhỏ——làm cô bé, mạnh hơn nữa⏎——phập phập——đi——ưm——ha, a」

**Fix:** 「Phà——đúng rồi, dùng cậu nhỏ——làm cô bé, mạnh hơn nữa⏎——phập phập——đi——ưm——ha, a」

Quy tắc fa/fu: ふぁ → "phà".

### 1258 — 凪 — sfx

**JP:** 「ふぁ……（ごくっ）――あ！　ふ、ふふふーん！！⏎にーさん、凪さまに興奮――発情しちゃったと？」

**TW:** 「啊……（咕咚）……啊！哼哼！！大哥哥看本小姐看得興奮，看得發情了吧？」

**VN cũ:** 「Fua……（Ực）——A! Fu, fufufu-n!!⏎Anh Soutetsu, hưng phấn với Nagi——đến phát tình rồi sao?」

**Fix:** 「Phà……（Ực）——A! Fu, fufufu-n!!⏎Anh Soutetsu, hưng phấn với Nagi——đến phát tình rồi sao?」

Quy tắc fa/fu: ふぁ → "phà". Phần cười "Fu, fufufu-n" (ふ、ふふふーん) GIỮ nguyên — tiếng cười La-tinh đang chờ quyết chung của Hieu.

### 1267 — 凪 — sfx

**JP:** 「ふあっ！　あっ！　あっ！　あっ！⏎あっ！　あっ！　あっ！　あっ！」

**TW:** 「啊！啊！啊！啊！啊！啊！啊！啊！」

**VN cũ:** 「Fua! A! A! A!⏎A! A! A! A!」

**Fix:** 「Phù! A! A! A!⏎A! A! A! A!」

Quy tắc fa/fu: ふあっ → "phù".

### 1268 — 凪 — gasp

**JP:** 「あっ！　あっ！　あっ! あっ！　あっ！　あっ！　⏎あっ！　あっ！　にーさん、うち――もうっ――っ！」

**TW:** 「啊！啊！啊！啊！啊！啊！啊！啊！大哥哥，咱快不行了！」

**VN cũ:** 「A! A! A! A! A! A!⏎A! A! Anh Soutetsu, em——không chịu nổi nữa——!」

**Fix:** 「A! A! A! A! A! A!⏎A! A! Anh Soutetsu, em——không chịu nổi nữa——Ư!」

Sweep lost-gasp-trailing, kiểm chứng đúng vs JP: kết "もうっ――っ！" — っ cuối sau gạch bị mất.

### 1269 — 凪 — sfx

**JP:** 「あっ！　あっ！　ふあっ！　あっ！　きもち、よかっ！⏎奥ばっ！　ノックっ――ノック、されるとっ――あっ！」

**TW:** 「啊！啊！啊！啊！舒服！裡面被敲打著……啊！」

**VN cũ:** 「A! A! Fua! A! Sướng, quá!⏎Bên trong! Cứ bị gõ——bị gõ cửa, thế này——a!」

**Fix:** 「A! A! Phù! A! Sướng, quá!⏎Bên trong! Cứ bị gõ——bị gõ cửa, thế này——a!」

Quy tắc fa/fu: ふあっ → "phù".

### 1271 — 凪 — sfx

**JP:** 「ふあっ！　あっ！　あっ！　あっ！　そこっ！⏎もっと！　赤ちゃんそだてるとこ、もっと――んうっ！」

**TW:** 「啊！啊！啊！啊！那裡！用力！養小孩的地方，用力！嗯！」

**VN cũ:** 「Fua! A! A! A! Chỗ đó!⏎Nữa đi! Chỗ nuôi em bé ấy, nữa đi——ưm!」

**Fix:** 「Phù! A! A! A! Chỗ đó!⏎Nữa đi! Chỗ nuôi em bé ấy, nữa đi——ưm!」

Quy tắc fa/fu: ふあっ → "phù".

### 1273 — 凪 — sfx

**JP:** 「ふぁぁうんっ！　ふあっ！　あっ！　にーさん！⏎にーさん！　にーさん！　にーさんっ！！！」

**TW:** 「啊！啊！啊！大哥哥！大哥哥！大哥哥！大哥哥！！！」

**VN cũ:** 「Fuaaun! Fua! A! Anh Soutetsu!⏎Anh Soutetsu! Anh Soutetsu! Anh Soutetsu!!!」

**Fix:** 「Phàaun! Phù! A! Anh Soutetsu!⏎Anh Soutetsu! Anh Soutetsu! Anh Soutetsu!!!」

Quy tắc fa/fu: ふぁぁうんっ → "Phàaun" (giữ đủ âm: phà + a + un); ふあっ → "phù".

### 1274 — 凪 — sfx

**JP:** 「ふあっ！　あっ！　そこ――ばいっ！　そこからっ――⏎んっ！　びゅうびゅう、たくさんたくさん、射精、して」

**TW:** 「啊！啊！就是那裡！在那裡……嗯！咻咻地射出來吧」

**VN cũ:** 「Fua! A! Chỗ đó——đấy! Từ chỗ đó——⏎Ưm! Bắn phụt phụt, thật nhiều thật nhiều, tinh dịch vào đi」

**Fix:** 「Phù! A! Chỗ đó——đấy! Từ chỗ đó——⏎Ưm! Bắn phụt phụt, thật nhiều thật nhiều, tinh dịch vào đi」

Quy tắc fa/fu: ふあっ → "phù".

### 1278 — 凪 — sfx

**JP:** 「ふぁぁぁぁぁぁぁんっ！！！！」

**TW:** 「啊！！！！」

**VN cũ:** 「Fuaaaaaaa!!!!」

**Fix:** 「Phàaaaaaan!!!!」

Quy tắc fa/fu: ふぁぁぁぁぁぁぁんっ (ふ+7 ぁ+ん) → "Phàaaaaaan" — giữ đủ 7 âm a VÀ âm mũi ん (VN cũ "Fuaaaaaaa" làm mất ん).

### 1280 — 凪 — sfx

**JP:** 「ふぇ――ふあ！！？」

**TW:** 「啊？啊！」

**VN cũ:** 「Hể——fua!!?」

**Fix:** 「Phuê——phùa!!?」

Quy tắc fa/fu đã chốt: ふぇ → "phuê" ("Hể" sai âm — ふぇ là tiếng thở, không phải "hể?"); ふあ (không っ) → "phùa".

### 1296 — 双鉄 — gasp

**JP:** 「っ！」

**TW:** 「嗯！」

**VN cũ:** 「!」

**Fix:** 「Ư!」

Sweep lost-gasp-whole, kiểm chứng đúng vs JP: cả dòng chỉ là "っ！" — VN chỉ còn "!".

### 1304 — 凪 — sfx

**JP:** 「んっ、ひゅっ！　ふぁっ――べろぉんって、されると、⏎され、ると――うち、ふあっ――おまんこ、あつ、くて」

**TW:** 「嗯，唔！啊……被你這樣舔著，咱……啊……咱的下面好熱」

**VN cũ:** 「Ưm, hyu! Fua——khi bị, liếm như vậy,⏎bị liếm, như vậy——em, fua——cô bé, nóng, quá」

**Fix:** 「Ưm, hyu! Phà——khi bị, liếm như vậy,⏎bị liếm, như vậy——em, phù——cô bé, nóng, quá」

Quy tắc fa/fu: ふぁっ → "phà"; ふあっ → "phù".

### 1339 — 双鉄 — gasp

**JP:** 「勃起ちんちんを膣口にいれる――っ、くっ――⏎これで――あっている、かな？」

**TW:** 「將勃起的雞雞塞進去……唔，這樣做，沒錯吧？」

**VN cũ:** 「Cho cậu nhỏ đang cương cứng vào cửa âm đạo——hự——⏎Thế này——đã đúng, chưa?」

**Fix:** 「Cho cậu nhỏ đang cương cứng vào cửa âm đạo——Ư, hự——⏎Thế này——đã đúng, chưa?」

Sweep BỎ SÓT: "――っ、くっ――" là hai tiếng (っ + くっ) nhưng VN chỉ diễn một ("hự"). Bổ sung "Ư" trước "hự".

### 1357 — 凪 — sfx

**JP:** 「そしたら――そしたら――ふあっ――あ――（ごくっ）⏎にーさんも、虎さんに――ケダモノになって、そうして」

**TW:** 「既然這樣……既然這樣，啊……啊……（咕咚）大哥哥也變成野獸吧，然後」

**VN cũ:** 「Vậy thì——vậy thì——fua——a——（Ực）⏎Anh Soutetsu cũng, hãy biến thành hổ——biến thành dã thú, rồi làm đi」

**Fix:** 「Vậy thì——vậy thì——phù——a——（Ực）⏎Anh Soutetsu cũng, hãy biến thành hổ——biến thành dã thú, rồi làm đi」

Quy tắc fa/fu: ふあっ → "phù".

### 1366 — 凪 — sfx

**JP:** 「凪さまのこと――うちの、こと――ふあ！　にーさんの、⏎あかちゃんの――おかあさんに――して欲しかとばい！」

**TW:** 「本小姐……咱……啊！想給大哥哥生孩子……想做媽媽！」

**VN cũ:** 「Hãy biến Nagi——biến em——fua! Thành mẹ——⏎của em bé——của anh đi!」

**Fix:** 「Hãy biến Nagi——biến em——phùa! Thành mẹ——⏎của em bé——của anh đi!」

Quy tắc fa/fu: ふあ (không っ) → "phùa" (tiền lệ h2 956).

### 1397 — 凪 — sfx

**JP:** 「やぁらぁ、にぃさぁん――ンッ――ふあっ――んうっ、⏎きもちよか、けど――もっと――もっと――他のとこぉ」

**TW:** 「討厭，大哥哥……唔……啊……嗯，好舒服……但是，再做點……別的事情吧」

**VN cũ:** 「Không chịu đâu, anh Soutetsu——ưm——fua——ưm,⏎sướng lắm, nhưng mà——nữa đi——nữa đi——chỗ khác cơ」

**Fix:** 「Không chịu đâu, anh Soutetsu——ưm——phù——ưm,⏎sướng lắm, nhưng mà——nữa đi——nữa đi——chỗ khác cơ」

Quy tắc fa/fu: ふあっ → "phù".

### 1420 — 凪 — sfx

**JP:** 「おちんちん――精子――ぜんぶっ！　にーさんの、⏎精子、精液――んくっ――ふあっ――全部――全部ぅ」

**TW:** 「雞雞……精液……都給咱！大哥哥的……精子，精液……嗚，啊……都給咱，都給咱」

**VN cũ:** 「Cậu nhỏ——tinh trùng——tất cả! Tinh trùng,⏎tinh dịch——nku——fua——của anh——tất cả——cho em tất cả đi」

**Fix:** 「Cậu nhỏ——tinh trùng——tất cả! Tinh trùng,⏎tinh dịch——nku——phù——của anh——tất cả——cho em tất cả đi」

Quy tắc fa/fu: ふあっ → "phù".

## 4. Đã kiểm tra và KHÔNG tính là sai

- **1297** 「イクッ！　けんっ！」 → "Ra mất! Rồi!" — けんっ là tiểu từ phương ngữ Hakata (けん = "vì/nên"), dùng như tiếng cảm thán cuối câu; "Rồi!" diễn ý "đã tới rồi" — giữ, ghi chú phán đoán.
- **1193** VN rên rời rạc ("lưỡi của anh / cô bé——cô bé——đang liếm, đang mút") — JP cũng rời rạc tương tự; "べろ" = lưỡi, VN theo JP (TW "口水" sai — JP thắng TW) — giữ.
- **1241** "ぁっ――っ――" → "A——a——" — hai tiếng っ đều có âm tương ứng trong VN — giữ.
- **Tiếng cười La-tinh GIỮ, chờ quyết chung của Hieu:** 1258 "Fu, fufufu-n" (ふ、ふふふーん), 1391 "fufu" (ふふっ), 1308/1313/1314 "Nhehe"/"Ehehe" — tiền lệ lr-h1: đề xuất chờ Hieu quyết (giữ La-tinh hay "phì phì"/"hì hì").
- **ぷあ/ぷぁ/んぷぁっ GIỮ "Pua"/"Npua":** 1225 (んぷぁっ→"Npua"), 1255/1285 (ぷあっ→"Pua"/"pua"), 1227 (ぷぁ→"Pua") — tiền lệ file h1 cùng route: "ぷぁ/ぷは/ぷあ 6 dòng giữ 'Pua/Puha' chờ quyết chung".
- **SFX La-tinh khác GIỮ (chưa có quy tắc chung):** "Hyau"/"Hya" (ひゃう/ひゃ), "Nhyu" (んひゅっ), "Nku"/"nku" (1218/1420 んくっ), "Aku" (1277 ぁくっ), "Kyaa" (1175 きゃあ), "Wa" (1209 わ), "Hie" (1214 ひえっ), "Hyan" (1182 ひゃんっ), "Hyawawa" (1176 ひゃわわっ), "Au" (1265 あうっ), "Nkyuu" (1289 んきゅううううううっ), "Hyuaaaaaa" (1185 ひゅぁぁぁぁぁぁぁあああん), "zujuuu" (1285 ずじゅうううっ), "hi-hamu"/"hyuki" (1290) — các file lr-h1/lr-h2 có quy ước riêng (ひゃう→"Hiau", きゅ→"Kíu", んくっ→"Ưm hự") nhưng chưa phải quy tắc đã chốt toàn dự án; file Nagi 08a cùng route cũng không chuẩn hoá SFX. Cần Hieu/parent quyết có áp dụng chuẩn hoá SFX rộng cho các file Nagi hay giữ dạng gần tiếng Nhật gốc (theo hướng dẫn 22:19).
- **1305** marker giọng nói `[とらなぎ,1]` trong JP — không phải text hiển thị; toàn dự án 4 lần xuất hiện đều bỏ qua trong VN (凪ふかみ08a 1720, 日々姫04 1869) — giữ cách xử lý.
- **1243** ruby `[ぬく]温かぁ` — VN "ấm quá" đã diễn đúng — giữ.
- **1325** "Anh——Soutetsu——" — chỉ là "anh Soutetsu" bị ngắt bởi gạch (にぃ――さぁん――) — giữ.
- **1266** 「！」 vs **1296** 「っ！": 1266 JP chỉ là "!" (không っ) nên VN "!" là đúng; 1296 JP có っ nên đã sửa thành "Ư!" — không nhầm lẫn.
- **1377** JP 「無論――かわいいアナルが見える」 — 無論 đọc むろん = "đương nhiên" (từ Nhật hợp lệ, không phải tiếng Trung); VN "Đương nhiên là" đúng. (TW có lỗi đánh máy "你你", không ảnh hưởng vì JP thắng TW.)
- **Ngoài phạm vi file này (ghi nhận cho parent):** khi tra marker `[..]` toàn dự án, phát hiện 日々姫03 key 2409 có VN "Vài ngày sau." rõ ràng lệch với JP (câu hỏi về Minokasa Nagi) — file đó sẽ được audit riêng theo queue, không sửa ở đây.

## Kết bài

File lr_凪h2 là H-scene Soutetsu + Nagi (Nagi mặc đồ lót tai-đuôi hổ đặt mua online nhưng không có vằn). Cấu trúc sạch hoàn toàn — không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng chưa dịch — và toàn bộ lỗi là lỗi hệ thống ở mức âm thanh: 38/38 tiếng thở ふぁ/ふあ của Nagi để nguyên dạng La-tinh, cộng 8 gasp っ bị mất (6 từ sweep + 2 bắt thêm) và 1 câu thiếu động từ. Sau khi áp dụng khối TOML 46 dòng dưới đây, file này coi như xong về mặt dịch thuật; phần còn lại chỉ là các quyết định SFX chung đang chờ (tiếng cười La-tinh, ぷあ "Pua", và chuẩn hoá SFX rộng cho các file Nagi).

Khối TOML dưới đây parse được bằng tomllib, **46 key, 0 sai lệch giá trị so với JSON**. Quy tắc ký tự xuống dòng: giá trị fix nào chứa ký tự xuống dòng dạng backslash-n (2 ký tự, như trong JSON và trong TOML gốc) thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON. (35 lần backslash-n trong 46 fix.)

- Lượt soát 2: 46/46 tái kiểm chứng, 0 bỏ, 0 sửa.

```toml
[script]
"1124" = "「Tường thuật trực tiếp như vậy xấu hổ lắm!!!\\nĐừng nhìn nữa, đừng nói nữa, làm đi——làm nữa đi」"
"1172" = "「Hyau——a——anh Soutetsu——anh Soutetsu——\\nPhù! Nữa đi——nhé——nữa đi——trực tiếp vào——ưm」"
"1174" = "「Hya——ưm——sao lại, là nách, chứ? Nagi\\n——phà——chỗ đó——nhột lắm——」"
"1181" = "「Hiu!? Á! Chỗ đi tiểu——ưm!\\nPhù! Chỗ đó——mà hút thì——bẩn lắm」"
"1185" = "「Hyagu!? Ư——Hyuaaaaaa!」"
"1187" = "「Hyauuu!? Á! Không chịu! Tuột ra mất!\\nRa khỏi cô bé mất! Cậu nhỏ——phù!?」"
"1188" = "「Hyauuu!? Phà——a——」"
"1190" = "「Hyau!? Phà——a——sướng, lắm, nhưng mà,\\nưm——bây giờ em muốn anh nhìn——xuống dưới cơ——gao」"
"1193" = "「Nhi!? Phù——lưỡi——lưỡi của anh\\ncô bé——cô bé——đang liếm, đang mút」"
"1199" = "「Phù——a! A! A! A——\\nƯm——phuya——sướng, quá——ưm——phù」"
"1202" = "「Phù」"
"1203" = "「Phù! Á! Áaaa! Cậu nhỏ của anh,\\nưm——hỏng——hỏng mất——á!」"
"1205" = "「Phà! Ha! Ha! Ha!\\nHa! Ha! Ha! Ha!」"
"1207" = "「Phù! A! A! A! Hỏng, mất——\\ncủa em——cô bé của em——sẽ hỏng mất——ưm」"
"1210" = "「Phà!? Hyau! Không chịu đâu, xấu hổ lắm,\\nchỗ đi tiểu——ưm! Cứ bị chọc chọc, vào đó」"
"1213" = "「Phùaaaaa!? Đợi đã! Đợi đã,\\nanh Soutetsu! Bây giờ, em——cô bé của em——phùa!」"
"1220" = "「Nhyu! ——~~~~~~~~~~~~Ư!!!」"
"1221" = "「Ư!!」"
"1222" = "「Ư!!!」"
"1229" = "「Phà——hyau——a……ưm……nhehe——\\nNagi——Nagi——ưm——vui lắm……phà」"
"1232" = "「Phù——a——」"
"1235" = "「A——phà——a——」"
"1236" = "「Phà——phà——A——a——\\nAnh Soutetsu——nè——anh Soutetsu——anh Soutetsuuuuu」"
"1237" = "「Phà——a……ưm——a——anh Soutetsu——\\nanh Soutetsu——yêu——yêu——yêu anh lắm」"
"1241" = "「A——a——anh Soutetsu……dâm đãng, quá……phà……\\nSay mê, ngực nhỏ, của Nagi——đến vậy sao」"
"1243" = "「Phà——a——vui quá——nóng quá——ấm quá\\n——ưm——nhiều quá——tinh dịch——của anh Soutetsu——」"
"1247" = "「Ha——a——cái đó——nữa đi——anh Soutetsu,\\nlúc nãy ấy——nữa đi——phù! Nữa đi——Ư!」"
"1248" = "「Phù——a, ngực——ưm……Nagi,\\nnóng rực lên vì nụ hôn, đổ cả mồ hôi rồi này」"
"1250" = "「Phà——a——chỗ đó——thích lắm——ưm——\\nAnh Soutetsu——nữa đi——nữa đi——làm mạnh, hơn đi」"
"1254" = "「Phà——đúng rồi, dùng cậu nhỏ——làm cô bé, mạnh hơn nữa\\n——phập phập——đi——ưm——ha, a」"
"1258" = "「Phà……（Ực）——A! Fu, fufufu-n!!\\nAnh Soutetsu, hưng phấn với Nagi——đến phát tình rồi sao?」"
"1267" = "「Phù! A! A! A!\\nA! A! A! A!」"
"1268" = "「A! A! A! A! A! A!\\nA! A! Anh Soutetsu, em——không chịu nổi nữa——Ư!」"
"1269" = "「A! A! Phù! A! Sướng, quá!\\nBên trong! Cứ bị gõ——bị gõ cửa, thế này——a!」"
"1271" = "「Phù! A! A! A! Chỗ đó!\\nNữa đi! Chỗ nuôi em bé ấy, nữa đi——ưm!」"
"1273" = "「Phàaun! Phù! A! Anh Soutetsu!\\nAnh Soutetsu! Anh Soutetsu! Anh Soutetsu!!!」"
"1274" = "「Phù! A! Chỗ đó——đấy! Từ chỗ đó——\\nƯm! Bắn phụt phụt, thật nhiều thật nhiều, tinh dịch vào đi」"
"1278" = "「Phàaaaaaan!!!!」"
"1280" = "「Phuê——phùa!!?」"
"1296" = "「Ư!」"
"1304" = "「Ưm, hyu! Phà——khi bị, liếm như vậy,\\nbị liếm, như vậy——em, phù——cô bé, nóng, quá」"
"1339" = "「Cho cậu nhỏ đang cương cứng vào cửa âm đạo——Ư, hự——\\nThế này——đã đúng, chưa?」"
"1357" = "「Vậy thì——vậy thì——phù——a——（Ực）\\nAnh Soutetsu cũng, hãy biến thành hổ——biến thành dã thú, rồi làm đi」"
"1366" = "「Hãy biến Nagi——biến em——phùa! Thành mẹ——\\ncủa em bé——của anh đi!」"
"1397" = "「Không chịu đâu, anh Soutetsu——ưm——phù——ưm,\\nsướng lắm, nhưng mà——nữa đi——nữa đi——chỗ khác cơ」"
"1420" = "「Cậu nhỏ——tinh trùng——tất cả! Tinh trùng,\\ntinh dịch——nku——phù——của anh——tất cả——cho em tất cả đi」"
```
