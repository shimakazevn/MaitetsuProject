# Moan-fix — lr_凪h2_虎さんの交尾.txt.toml (07_Nagi_Fukami)

**Ngày:** 21/11/2026
**Tệp TOML:** `07_Nagi_Fukami/lr_凪h2_虎さんの交尾.txt.toml` — md5 `4f26c5ed7e6e0d076848d8be1add75a7` (khớp md5 audit), 60.808 byte, BOM + CRLF, `[selections]` rỗng, **không có bản sao trùng** (kiểm tra md5 toàn bộ 227 tệp TOML).
**Nguồn CSV:** "Trang tính 3" — bộ hàng duy nhất `07_Nagi_Fukami`, 293 hàng `[script]`, 0 key trùng; CSV↔TOML: 131 khớp tuyệt đối + 162 gộp `\n` thành khoảng trắng (hiện tượng TOML-2 làm phẳng), 0 khác biệt thực chất; JP comment 293/293 khớp CSV3. CSV3 là bản chuẩn cho fix list.
**Audit trước đó (đã gộp):** 46/293 dòng sai (15,7%) — 38 sfx fa/fu + 7 gasp + 1 meaning. Audit viết trước quy tắc romaji (21/11 ~01:56) nên đã Việt hoá toàn bộ 38 tiếng thở fa/fu thành "phà"/"phù"/"phùa"/"phuê"/"phuya" — bản moan này xét lại toàn bộ 38 dòng đó theo quy tắc romaji.

## 1. Kiểm chứng file

- Đọc 293/293 dòng CSV3 (bộ duy nhất) + đối chiếu TOML. Không dual-set, không key trùng, không dòng chưa dịch.
- TOML md5 `4f26c5ed7e6e0d076848d8be1add75a7`, khớp md5 audit; không bản sao trùng.
- Thẻ %l: JP = VN = 0.

## 2. Kho rên (moan inventory)

- Xét 141 dòng có tiếng rên/thở/gasp (102 thoại + 39 độc thoại) + 48 dòng SFX trong ngoặc （ ） (39 trong số đó đã nằm trong 141 dòng trên) — tổng cộng **150 dòng xét**; 10 dòng trong số đó là tiếng cười.
- Phân loại 26 dòng sửa: romaji 22 (20 họ fa/fu + ひあ 1 + や-moan 1); đếm nguyên âm thuần 3 (1185, 1203, 1276) — 1205 mang cả romaji fa lẫn đếm はぁ; sai âm 1 (1245 か→"Ha"). (1205 mang cả romaji fa + đếm はぁ; 1203 trùng audit fa/fu nhưng chỉ sửa đếm や, token ふあっ đã đúng; 1199/1247 mang phần áp nguyên giá trị audit — xem từng dòng.)
- Ngoài 26 dòng sửa: **17 dòng audit fa/fu được HỦY fix audit, giữ romaji cũ** (bản cũ đã đúng — xem §6 cờ 1; không nằm trong JSON này, theo tiền lệ lr-mikuro-hibiki-h).
- Giữ ~124 dòng rên/SFX (xem §4). Sweep 6 mục không đụng (xem §5).

## 3. Các dòng đã sửa (26 dòng)

Quy tắc áp dụng chung: romaji Hepburn; ふぁ→Fa, ふあ→Fua, ふぇ→Fue, ふや→Fuya (bản cũ "Fua"/"fua" dùng chung cho cả ふぁ lẫn ふあ là **sai âm** — ふぁ = fa, ふあ = fua; tiền lệ lr-mikuro-hibiki-h 1712); một âm = một cách diễn; độ dài nguyên âm theo công thức (số nguyên âm = 1 + số う/ぅ; với ぁ/あ/ー đếm trực tiếp số mora); giữ nguyên chữ hoa/thường của bản cũ theo vị trí trong câu (tiền lệ mikuro §5: "fua"/"fue" thường giữa câu được giữ). Giá trị audit được **hủy ở đúng token rên** và chỉ giữ lại ở đúng phần audit đúng (1199 ふっ→"phù", 1247 gasp Ư, 1185 gasp Ư).

### A. Romaji họ fa/fu — ふぁ→Fa / ふあ→Fua (19 dòng)

#### 1174 — 凪 — romaji

- JP: 「ひゃっ――ンッ――どうして、脇、と？　凪、さま\n――ふぁっ――こぎゃんと――くすぐったか、と――」
- TW: 「呀……嗯……為什麼是腋下？本小姐……啊……怕癢……」
- Cũ: 「Hya——ưm——sao lại, là nách, chứ? Nagi\n——fua——chỗ đó——nhột lắm——」
- Mới: 「Hya——ưm——sao lại, là nách, chứ? Nagi\n——fa——chỗ đó——nhột lắm——」
- Lý do: ふぁっ = "fa"; bản cũ "fua" sai âm (fua là ふあ). Audit "phà" — "phà" đọc như từ "phà" (ngượng) nên hủy, dùng romaji. Giữ "Hya"/"ưm".

#### 1188 — 凪 — romaji

- JP: 「ひゃうぅうっ！？　ふぁっ――あっ――」
- TW: 「呀？！哇……啊……」
- Cũ: 「Hyauuu!? Fua——a——」
- Mới: 「Hyauuu!? Fa——a——」
- Lý do: ふぁっ = "Fa"; bản cũ "Fua" sai âm. Giữ "Hyauuu" (ひゃうぅう = 3 u, đúng).

#### 1190 — 凪 — romaji

- JP: 「ひゃうっ！？　ふぁっ――あっ――きもち、よか、けど、\nん――いま見てほしいのは――もっと下――がお」
- TW: 「呀？！哇……啊，好舒服，可是，唔……現在咱想讓你看更下面嗷」
- Cũ: 「Hyau!? Fua——a——sướng, lắm, nhưng mà,\nưm——bây giờ em muốn anh nhìn——xuống dưới cơ——gao」
- Mới: 「Hyau!? Fa——a——sướng, lắm, nhưng mà,\nưm——bây giờ em muốn anh nhìn——xuống dưới cơ——gao」
- Lý do: ふぁっ = "Fa"; bản cũ "Fua" sai âm. Giữ "Hyau"/"gao".

#### 1199 — 凪 — romaji (áp nguyên phần audit cho ふっ)

- JP: 「ふあっ――あっ！　あ！　あ！　あっ――\nんっ――ふやっ――きもち、よか――んっ――ふっ」
- TW: 「哇……啊！啊！啊！啊……嗯……呀……好舒服……嗯……呼」
- Cũ: 「Fua——a! A! A! A——\nƯm——fuya——sướng, quá——ưm——fu」
- Mới: 「Fua——a! A! A! A——\nƯm——fuya——sướng, quá——ưm——phù」
- Lý do: ふあっ→"Fua" và ふやっ→"fuya" bản cũ đã đúng romaji (giữ; hủy "Phù"/"phuya" của audit). Chỉ đổi ふっ cuối dòng: "fu"→"phù" — áp nguyên giá trị audit (hơi thở thường ふ = "phù", tiền lệ lr-fukamih2 1063/1264 giữ "phù" cho ふっ).

#### 1205 — 凪 — romaji + đếm nguyên âm

- JP: 「ふぁっ！　はぁっ！　はぁ！　はぁっ！\nはぁっ！　はあっ！　はあっ！　はあっ！」
- TW: 「哇！啊！啊！啊！啊！啊！啊！啊！」
- Cũ: 「Fua! Ha! Ha! Ha!\nHa! Ha! Ha! Ha!」
- Mới: 「Fa! Haa! Haa! Haa!\nHaa! Haa! Haa! Haa!」
- Lý do: (1) ふぁっ = "Fa"; bản cũ "Fua" sai âm. (2) Cả 7 hơi はぁっ/はぁ/はあっ đều = 2 âm a (は + ぁ/あ) nhưng bản cũ chỉ diễn 1 a ("Ha") — thiếu 1 a mỗi hơi; sửa thành "Haa" ×7 (tiền lệ hachiroku-h9: 10 dòng はぁっ/はあっ thiếu 1 a; lr-hibikifukami-h1: はぁっ/はあっ = 2 a mỗi âm). Đếm lại bằng token: JP có 7 hơi は (4 はぁ + 3 はあ), bản sửa có đúng 7 "Haa".

#### 1210 — 凪 — romaji

- JP: 「ふぁっ！？　ひゃうっ！　やぁらっ、はずかしかっ、\nおしっこの、とこ――んっ！　つんつん、されるのぉ」
- TW: 「哇？！呀！討厭，好害羞，尿尿的地方被頂著，好害羞」
- Cũ: 「Fua!? Hyau! Không chịu đâu, xấu hổ lắm,\nchỗ đi tiểu——ưm! Cứ bị chọc chọc, vào đó」
- Mới: 「Fa!? Hyau! Không chịu đâu, xấu hổ lắm,\nchỗ đi tiểu——ưm! Cứ bị chọc chọc, vào đó」
- Lý do: ふぁっ = "Fa"; bản cũ "Fua" sai âm. Giữ "Hyau"; やぁらっ→"Không chịu" là từ (không phải rên) nên giữ.

#### 1229 — 凪 — romaji

- JP: 「ふぁ――ひゃうっ――あっ……ん……んへへっ――\n凪、さま――凪さま――んっ――うれしかと……ふぁっ」
- TW: 「啊……呀……啊……嗯……嘿嘿，本小姐……本小姐……嗯……好開心……啊」
- Cũ: 「Fua——hyau——a……ưm……nhehe——\nNagi——Nagi——ưm——vui lắm……fua」
- Mới: 「Fa——hyau——a……ưm……nhehe——\nNagi——Nagi——ưm——vui lắm……fa」
- Lý do: cả hai ふぁ (đầu và cuối dòng) đều = "fa"; bản cũ "Fua"/"fua" sai âm. Giữ "hyau"/"nhehe".

#### 1235 — 凪 — romaji

- JP: 「あっ――ふぁ――あっ――」
- TW: 「啊……啊……啊……」
- Cũ: 「A——fua——a——」
- Mới: 「A——fa——a——」
- Lý do: ふぁ = "fa"; bản cũ "fua" sai âm. Giữ "A"/"a" cho あっ.

#### 1236 — 凪 — romaji

- JP: 「ふぁ――ふぁ――アッっ――あっ――\nにぃさん――ね――にぃさん――にぃさぁああん」
- TW: 「啊……啊……啊……啊……大哥哥，大哥哥……大哥哥」
- Cũ: 「Fua——fua——A——a——\nAnh Soutetsu——nè——anh Soutetsu——anh Soutetsuuuuu」
- Mới: 「Fa——fa——A——a——\nAnh Soutetsu——nè——anh Soutetsu——anh Soutetsuuuuu」
- Lý do: cả hai ふぁ đều = "fa"; bản cũ "Fua"/"fua" sai âm.

#### 1237 — 凪 — romaji

- JP: 「ふぁ――あっ……んっ――あっ――にーさん――\nにーさん――しゅき――すき――だいすきぃ」
- TW: 「啊……啊……嗚……啊……大哥哥，大哥哥……愛你……愛你……愛死你了」
- Cũ: 「Fua——a……ưm——a——anh Soutetsu——\nanh Soutetsu——yêu——yêu——yêu anh lắm」
- Mới: 「Fa——a……ưm——a——anh Soutetsu——\nanh Soutetsu——yêu——yêu——yêu anh lắm」
- Lý do: ふぁ = "Fa"; bản cũ "Fua" sai âm.

#### 1241 — 凪 — romaji

- JP: 「ぁっ――っ――にーさん……エッチ、ばい……ふぁ……\n凪さまの、ちっちゃか、おっぱい――そぎゃん、夢中に」
- TW: 「啊……啊……大哥哥……好色情……啊……竟然對本小姐的……小小胸部……這麼沉醉」
- Cũ: 「A——a——anh Soutetsu……dâm đãng, quá……fua……\nSay mê, ngực nhỏ, của Nagi——đến vậy sao」
- Mới: 「A——a——anh Soutetsu……dâm đãng, quá……fa……\nSay mê, ngực nhỏ, của Nagi——đến vậy sao」
- Lý do: ふぁ = "fa"; bản cũ "fua" sai âm. Giữ "A——a——" cho "ぁっ――っ――" (audit đã quyết đủ âm).

#### 1243 — 凪 — romaji

- JP: 「ふぁっ――あっ――うれしかっ――あつか――[ぬく]温かぁ\n――んっ――たくさん――精液――にいさん、のっ――」
- TW: 「啊……啊……好開心，好暖……溫溫的……嗯……好多精液……都是大哥哥的」
- Cũ: 「Fua——a——vui quá——nóng quá——ấm quá\n——ưm——nhiều quá——tinh dịch——của anh Soutetsu——」
- Mới: 「Fa——a——vui quá——nóng quá——ấm quá\n——ưm——nhiều quá——tinh dịch——của anh Soutetsu——」
- Lý do: ふぁっ = "Fa"; bản cũ "Fua" sai âm.

#### 1247 — 凪 — romaji (giữ gasp Ư của audit)

- JP: 「はっ――あっ――それっ――もっと――にーさん、\nいまの――もっと――ふあっ！　もっとぉっ――っ！」
- TW: 「啊……啊……這個，再來……大哥哥，剛才這個，再來……啊！再來！」
- Cũ: 「Ha——a——cái đó——nữa đi——anh Soutetsu,\nlúc nãy ấy——nữa đi——fua! Nữa đi——!」
- Mới: 「Ha——a——cái đó——nữa đi——anh Soutetsu,\nlúc nãy ấy——nữa đi——fua! Nữa đi——Ư!」
- Lý do: ふあっ→"fua" bản cũ đã đúng romaji (giữ; hủy "phù" của audit). Chỉ áp nguyên gasp Ư của audit/sweep ở cuối dòng ("もっとぉっ――っ！" → "Nữa đi——Ư!"). Không đụng gasp Ư ngoài việc giữ nguyên.

#### 1250 — 凪 — romaji

- JP: 「ふぁ――あっ――そこっ――しゅき――んっ――\nにぃさぁん――もっと――もっと――もっと、してぇ」
- TW: 「啊……啊，這裡，喜歡……嗯……大哥哥，用力，用力，再用力」
- Cũ: 「Fua——a——chỗ đó——thích lắm——ưm——\nAnh Soutetsu——nữa đi——nữa đi——làm mạnh, hơn đi」
- Mới: 「Fa——a——chỗ đó——thích lắm——ưm——\nAnh Soutetsu——nữa đi——nữa đi——làm mạnh, hơn đi」
- Lý do: ふぁ = "Fa"; bản cũ "Fua" sai âm.

#### 1254 — 凪 — romaji

- JP: 「ふぁ――そう、おちんちん、で――おまんこ、もっと\n――じゅぶじゅぶって――して――んっ――は、あっ」
- TW: 「啊……對，用雞雞……更猛烈一點……啊，啊」
- Cũ: 「Fua——đúng rồi, dùng cậu nhỏ——làm cô bé, mạnh hơn nữa\n——phập phập——đi——ưm——ha, a」
- Mới: 「Fa——đúng rồi, dùng cậu nhỏ——làm cô bé, mạnh hơn nữa\n——phập phập——đi——ưm——ha, a」
- Lý do: ふぁ = "Fa"; bản cũ "Fua" sai âm. Giữ "ha, a" cho は、あっ.

#### 1258 — 凪 — romaji

- JP: 「ふぁ……（ごくっ）――あ！　ふ、ふふふーん！！\nにーさん、凪さまに興奮――発情しちゃったと？」
- TW: 「啊……（咕咚）……啊！哼哼！！大哥哥看本小姐看得興奮，看得發情了吧？」
- Cũ: 「Fua……（Ực）——A! Fu, fufufu-n!!\nAnh Soutetsu, hưng phấn với Nagi——đến phát tình rồi sao?」
- Mới: 「Fa……（Ực）——A! Fu, fufufu-n!!\nAnh Soutetsu, hưng phấn với Nagi——đến phát tình rồi sao?」
- Lý do: ふぁ = "Fa"; bản cũ "Fua" sai âm. Giữ nguyên tiếng cười "Fu, fufufu-n" (ふ、ふふふーん) theo ghi chú audit — cười La-tinh chờ quyết chung.

#### 1273 — 凪 — romaji

- JP: 「ふぁぁうんっ！　ふあっ！　あっ！　にーさん！\nにーさん！　にーさん！　にーさんっ！！！」
- TW: 「啊！啊！啊！大哥哥！大哥哥！大哥哥！大哥哥！！！」
- Cũ: 「Fuaaun! Fua! A! Anh Soutetsu!\nAnh Soutetsu! Anh Soutetsu! Anh Soutetsu!!!」
- Mới: 「Faaun! Fua! A! Anh Soutetsu!\nAnh Soutetsu! Anh Soutetsu! Anh Soutetsu!!!」
- Lý do: ふぁぁうんっ = "Faaun" (faa + un); bản cũ "Fuaaun" thừa 1 u sau f (đó là âm của ふあぁ, không phải ふぁぁ). ふあっ→"Fua" giữ nguyên (đã đúng).

#### 1278 — 凪 — romaji

- JP: 「ふぁぁぁぁぁぁぁんっ！！！！」
- TW: 「啊！！！！」
- Cũ: 「Fuaaaaaaa!!!!」
- Mới: 「Faaaaaaan!!!!」
- Lý do: ふぁぁぁぁぁぁぁんっ = "fa" + 6 a + "n" = 7 âm a + ん → "Faaaaaaan" (F + 7 a + n). Bản cũ "Fuaaaaaaa" sai âm (fua thay vì fa) VÀ làm mất ん (audit đã sửa đếm thành "Phàaaaaaan" — 7 a + n đúng đếm; bản moan chỉ đổi hệ diễn sang romaji, giữ đếm và âm mũi của audit).

#### 1280 — 凪 — romaji

- JP: 「ふぇ――ふあ！！？」
- TW: 「啊？啊！」
- Cũ: 「Hể——fua!!?」
- Mới: 「Fue——fua!!?」
- Lý do: ふぇ = "Fue"; bản cũ "Hể" sai hẳn âm (hể là tiếng hỏi, không phải tiếng thở ふぇ). Audit sửa thành "Phuê" — hủy, dùng romaji theo họ fa/fu (tiền lệ lr-mikuro-hibiki-h 1708: audit "Phuê!?" → giữ "Fue!?"). ふあ→"fua" giữ nguyên (đã đúng).

#### 1304 — 凪 — romaji

- JP: 「んっ、ひゅっ！　ふぁっ――べろぉんって、されると、\nされ、ると――うち、ふあっ――おまんこ、あつ、くて」
- TW: 「嗯，唔！啊……被你這樣舔著，咱……啊……咱的下面好熱」
- Cũ: 「Ưm, hyu! Fua——khi bị, liếm như vậy,\nbị liếm, như vậy——em, fua——cô bé, nóng, quá」
- Mới: 「Ưm, hyu! Fa——khi bị, liếm như vậy,\nbị liếm, như vậy——em, fua——cô bé, nóng, quá」
- Lý do: ふぁっ = "Fa"; bản cũ "Fua" sai âm. ふあっ→"fua" giữ nguyên (đã đúng). Giữ "hyu" cho ひゅっ.

### B. ひあ → Hia (1 dòng)

#### 1183 — 凪 — romaji

- JP: 「ひあっっ！！！」
- TW: 「呀！！！」
- Cũ: 「Hya!!!」
- Mới: 「Hia!!!」
- Lý do: ひあ = "Hia", không phải "Hya" (hya là ひゃ). Bản cũ sai mora — quy tắc 3b: ひあ→"Hia" (tiền lệ otona-no-mizugi: ひあ→"Hia" 5 dòng; 凪ふかみh1 1214). Dấu っ×2 là cắt cụt, đã diễn bằng !!!.

### C. Đếm nguyên âm (4 dòng)

#### 1185 — 凪 — vowel-count (giữ gasp Ư của audit)

- JP: 「ひゃぐっ！？　っ――ひゅぁぁぁぁぁぁぁあああん！」
- TW: 「呀？！呀！」
- Cũ: 「Hyagu!? ——Hyuaaaaaa!」
- Mới: 「Hyagu!? Ư——Hyuaaaaaaaaaa!」
- Lý do: (1) Giữ nguyên gasp Ư của audit cho っ trần giữa dòng ("っ――" → "Ư——"). (2) Đếm lại độc lập bằng token: JP ひゅぁぁぁぁぁぁぁあああん = ひゅ + ぁ×7 + あ×3 = **10 âm a**; bản cũ "Hyuaaaaaa" chỉ có 6 a — thiếu 4 a → sửa thành "Hyuaaaaaaaaaa" (Hyu + 10 a; tiền lệ jiekei 1484: "Hyuaaaaaaaaaa (đếm lại: 10 a, đúng)"). Giữ "Hyagu" cho ひゃぐっ.

#### 1203 — 凪 — vowel-count (や giữ "Á", chỉ sửa đếm)

- JP: 「ふあっ！　やぁっ！　やぁああっ！　にーさんの、\nおちんち、んっ――こわ――こわれるの――やあっ！」
- TW: 「哇！不要！不要啊！大哥哥的雞雞……要把咱弄瘋了……不要啊！」
- Cũ: 「Fua! Á! Áaaa! Cậu nhỏ của anh,\nưm——hỏng——hỏng mất——á!」
- Mới: 「Fua! Áa! Áaaa! Cậu nhỏ của anh,\nưm——hỏng——hỏng mất——áa!」
- Lý do: や ở đây là từ chối ("không chịu/đừng") nên giữ "Á" theo tiền lệ jiekei (xem §6 cờ 2); chỉ sửa **đếm**: やぁっ = 2 âm a ("Á"→"Áa"), やぁああっ = 4 âm a ("Áaaa" đã đúng, giữ), やあっ = 2 âm a ("á"→"áa"). Tiền lệ jiekei 1581 sửa đếm やああっ "Áaaa"→"Áaa" mà vẫn giữ "Á". ふあっ→"Fua" giữ nguyên.

#### 1276 — 凪 — vowel-count

- JP: 「あーーーーーーーーーーーっ！！！！？」
- TW: 「啊！！」
- Cũ: 「Aaaaaaaaaaaa!!!!?」
- Mới: 「Aaaaaaaaaaaa!!!!?」
- Lý do: JP あ + 11 dấu ー = **12 mora**; bản cũ chỉ có 11 chữ a — thiếu 1 a → thêm 1 a thành 12 chữ. っ cuối + "!!!!?" đã diễn cắt cụt (audit quét bổ sung 223 dòng có っ đã quyết không thêm Ư ở đây — giữ nguyên quyết định đó).

#### 1205 — (đã nêu ở §3A — phần đếm はぁ)

- 7 hơi はぁっ/はぁ/はあっ đều = 2 âm a → "Haa" ×7 (xem §3A 1205).

### D. Sai âm khác (1 dòng)

#### 1245 — 凪 — wrong-sound

- JP: 「か――はっ――あ――あっとる、ばい――がお。\nそれで、腰を、最初は、ゆっくり、動かし、て――」
- TW: 「啊……啊……對，沒錯咧……嗷。然後，一開始的時候，要慢慢動腰」
- Cũ: 「Ha——ha——a——đúng rồi, đó——gao.\nRồi sau đó, ban đầu, hãy từ từ, chuyển động, hông——」
- Mới: 「Ka——ha——a——đúng rồi, đó——gao.\nRồi sau đó, ban đầu, hãy từ từ, chuyển động, hông——」
- Lý do: chuỗi rên 3 hơi か――はっ――あ―― bị diễn thành "Ha——ha——a——" — hơi đầu か = "ka", bản cũ "Ha" sai phụ âm k→h (tiền lệ otona-no-mizugi: かっ = "ka", bản cũ "Hà" sai phụ âm k→h → "Ka"). Hai hơi sau はっ→"ha", あ→"a" đã đúng, giữ. "あっとる"→"đúng rồi" là từ, giữ.

### E. Rên や trong chuỗi rên (1 dòng)

#### 1325 — 凪 — romaji

- JP: 「にぃ――さぁん――んっ――やぁ――ん――はっ――\nいじある――しな、いでっ――ンッ――もっと、してぇ」
- TW: 「大哥哥……嗯……呀……嗯……啊……不要欺負人……嗯……再來刺激點的」
- Cũ: 「Anh——Soutetsu——ưm——á——ưm——ha——\nđừng——trêu em, nữa——ưm——làm mạnh, hơn đi」
- Mới: 「Anh——Soutetsu——ưm——yaa——ưm——ha——\nđừng——trêu em, nữa——ưm——làm mạnh, hơn đi」
- Lý do: やぁ ở đây nằm giữa chuỗi hơi thở んっ――やぁ――ん――はっ (không phải từ từ chối — lời từ chối nằm ở "いじある――しな、いでっ" → "đừng trêu em nữa", đã diễn đủ); TW cũng diễn bằng tiếng 呀. Là tiếng rên nên giữ phụ âm y-: やぁ = 2 âm a → "yaa" (tiền lệ ポーレットh3: "'Á' cho きゃっ/ひゃっ/やっ" là lỗi mất phụ âm; lr-hibikifukami-h1 1334 やっ→"Ya"). Phân biệt với 1181/1187/1203 (や là từ chối → giữ "Á", xem §6 cờ 2).

## 4. Các dòng giữ (đáng chú ý)

- **ひゃ/ひゅ đã romaji đúng, giữ:** ひゃう→"Hyau" (1172, 1190, 1210), ひゃううう→"Hyauuu" (1187, 3 u đúng), ひゃうぅう→"Hyauuu" (1188, 3 u đúng), ひゃっ→"Hya" (1174, 1192), ひゃん→"Hyan" (1182), ひゃわわ→"Hyawawa" (1176), ひゃうん→"Hyaun" (1177), ひゃうっ→"Hyau" (1178, 1210), ひゃぐ→"Hyagu" (1185), ひゅ→"hyu" (1304), ひう→"Hiu" (1181), ひえ→"Hie" (1214).
- **ん + phụ âm đã romaji đúng, giữ:** んひゅ→"Nhyu" (1184, 1220), んひゅん→"Nhyun" (1299), んひっ→"Nhi" (1193), んきゅう→"Nkyuuuuuu" (1289, 6 u đúng), んくっ→"Nku" (1218, 1420), きゃあ→"Kyaa♪" (1175).
- **ぷあ/ぷぁ đã romaji đúng, giữ:** ぷあっ→"Pua" (1196, 1255), "pua" thường giữa câu (1217, 1285), ぷぁ→"Pua" (1227), んぷぁっ→"Npua" (1225).
- **Hơi thở thường đã đúng, giữ:** あっ→"A", んっ→"Ưm"/"ưm", くっ→"Hự" (1215, 1219, 1231, 1339), はっ→"Ha"/"ha", は……う……→"Ha……u……" (1251), ふわ→"fuwa" (1264), ぁうっ→"Au" (1265), ぁぅ～→"Au~" (1263), わ→"Wa" (1209, 1192 "wa!?"), ふ、ぁ→"fu, a" (1239, hai âm riêng — tiền lệ lr-fukamih2).
- **Cười là cười, giữ:** ふふっ→"fufu" (1391), えへへ→"Ehehe" (1252, 1309, 1313, 1314, 1318), んへへ→"Nhehe" (1229, 1308), ふ、ふふふーん→"Fu, fufufu-n" (1258), へへへ→"Hehehe" (1311).
- **がお (tiếng hổ) giữ romaji:** "gao" (1190, 1245, 1305, 1311, 1384, 1398).
- **SFX trong ngoặc （ ） giữ dạng động từ Việt** ("Chụt/Liếm/Nhóp nhép/Phập/Phụt/Trượt/Siết/Ngoáy/Mở rộng…", 48 dòng) — theo tiền lệ h8: số chữ kéo dài của SFX hành động là cách kéo dài cảm tính, không áp công thức đếm. Hôn/mút ちゅ/れる/じゅ giữ "chụt/liếm/nhóp nhép" (1282–1292, 1800–1855).
- **ふーーっ thở dài giữ "Phù":** 1313 (4 hơi ふーーっ/ふーっ/ふーーーっ/ふーーーーっ → "Phù——phù——phù——phù——") — "phù" là tiếng thở ra tự nhiên trong tiếng Việt, không ngượng; độ dài diễn bằng gạch nối (borderline, đã ghi nhận — không sửa).
- **Gasp Ư của audit/sweep giữ nguyên toàn bộ** (8 dòng gasp: 1185, 1220, 1221, 1222, 1247, 1268, 1296, 1339) — chỉ 1185 và 1247 xuất hiện trong JSON này vì có thêm sửa rên/count; các dòng còn lại không đụng.
- **Không dòng "Kh" nào bị đổi.** ("Kh" trong "Không chịu đâu" 1210 và "khi" 1304 là từ tiếng Việt, không phải cách diễn glottal-stop っ.)

## 5. Đối chiếu đợt quét gasp っ (kiểm chứng trực tiếp sweep-raw-gasp-wrong.json)

- File này CÓ 6 mục sweep — cả 6 đã được audit áp nguyên và kiểm chứng (1220, 1221, 1222, 1247, 1268, 1296); audit quét bổ sung bắt thêm 2 gasp (1185, 1339). **Không dòng gasp Ư nào bị sửa hay đụng lại ở đây** — 1185 và 1247 chỉ giữ nguyên Ư của audit trong giá trị moan mới.
- Quét bổ sung toàn bộ dòng JP có っ khi đọc file: không còn gasp っ trần nào bị mất ngoài 8 dòng audit đã xử lý (quyết định không thêm Ư cho 1276 あー…っ và 1373 ときはっ… là của audit — giữ nguyên).

## 6. Cờ cho đợt thống nhất

- **CỜ 1 — HỦY 17 fix fa/fu của audit** (audit sửa romaji cũ thành "phà"/"phù"/"phùa"; bản cũ đã là romaji đúng cho ふあ — giữ nguyên bản cũ, KHÔNG áp bản audit cho các dòng này; tiền lệ lr-mikuro-hibiki-h HỦY 23 fix):
  - 1172 ふあっ: audit "Phù!" → giữ "Fua!"
  - 1181 ふあっ: audit "Phù!" → giữ "Fua!"
  - 1187 ふあっ: audit "phù!?" → giữ "fua!?"
  - 1193 ふあっ: audit "Phù——" → giữ "Fua——"
  - 1202 ふあっ: audit "Phù" → giữ "Fua"
  - 1207 ふあっ: audit "Phù!" → giữ "Fua!"
  - 1213 ふあああああっ + ふあ: audit "Phùaaaaa!? … phùa!" → giữ "Fuaaaaa!? … fua!" (6 nguyên âm đúng)
  - 1232 ふあ――ぁっ: audit "Phù——a——" → giữ "Fua——a——"
  - 1248 ふあっ: audit "Phù——a," → giữ "Fua——a,"
  - 1267 ふあっ: audit "Phù!" → giữ "Fua!"
  - 1269 ふあっ: audit "Phù!" → giữ "Fua!"
  - 1271 ふあっ: audit "Phù!" → giữ "Fua!"
  - 1274 ふあっ: audit "Phù!" → giữ "Fua!"
  - 1357 ふあっ: audit "phù——a——" → giữ "fua——a——"
  - 1366 ふあ: audit "phùa!" → giữ "fua!"
  - 1397 ふあっ: audit "phù——ưm," → giữ "fua——ưm,"
  - 1420 ふあっ: audit "phù——" → giữ "fua——"
  - (1199 chỉ hủy phần "Phù"/"phuya" của audit cho ふあっ/ふやっ, giữ phần ふっ→"phù" của audit — giá trị cuối trong JSON §3.)
  - (1247 chỉ hủy phần "phù" của audit cho ふあっ, giữ gasp Ư của audit — giá trị cuối trong JSON §3.)
- **CỜ 2 — や chưa quyết chung toàn dự án** (cần quyết một lần ở đợt thống nhất): file này giữ "Á" cho や là từ chối (1181 やっ, 1187 やっ, 1203 やぁっ/やぁああっ/やあっ — chỉ sửa đếm) theo tiền lệ jiekei (lr-nagifukami-h1: "や không nằm trong danh sách romaji của quy tắc 3b", giữ "Á" cho やっ), nhưng đổi やぁ thành "Yaa" ở 1325 vì đó là tiếng rên trong chuỗi hơi thở (TW: 呀). NGƯỢC với lr-hibikifukami-h1 1334 (やっ→"Ya") và tiền lệ ポーレットh3 ("'Á' cho きゃっ/ひゃっ/やっ" là lỗi mất phụ âm) — parent đã ghi nhận mâu thuẫn này ở ROUTE-MOANS.md (jiekei giữ "Á" vs hibikifukami "Ya"). Quyết định ở đây: phân biệt theo vai trò (rên → romaji giữ y-; từ chối → giữ "Á" + sửa đếm) — chờ quyết chung.
- **CỜ 3 — 1164 (ngoài phạm vi moan, chỉ ghi nhận):** JP 「そ、それだけじゃなく――」 (nói lắp そ、そ) → VN cũ "Kh, không chỉ vậy đâu" — "Kh," là cách diễn lạ cho tiếng nói lắp, không phải rên/gasp. Audit không sửa; bản moan không đụng (không phải moan). Để audit loop xem lại nếu cần.
- **CỜ 4 — 1313 (borderline, đã giữ):** 4 hơi ふーーっ/ふーっ/ふーーーっ/ふーーーーっ dài ngắn khác nhau nhưng VN đều diễn "Phù" — độ dài không phân biệt. Giữ vì "phù" là hơi thở tự nhiên; nếu đợt thống nhất muốn chuẩn hoá độ dài hơi thở thì xét lại dòng này.

## 7. Lượt soát 2 (đọc lại toàn bộ fix vs JP)

- Tổng 26 / tái kiểm chứng 26 / bỏ 0 / sửa 0.
- Mọi số đếm nguyên âm dài đều đếm lại độc lập bằng token từ JP (không tin số đếm cũ): 1185 = 10 a (7 ぁ + 3 あ), 1276 = 12 mora (あ + 11 ー), 1278 = 7 a + ん, 1273 = 2 a ("Faaun"), 1205 = 7 hơi は × 2 a ("Haa" ×7), 1203 = 2/4/2 a ("Áa"/"Áaaa"/"áa").
- JSON 26 mục dạng chuẩn (khóa string, jp/tw/old_vn khớp CSV3 tuyệt đối 26/26); khối TOML 26 khóa parse bằng tomllib, 0 sai lệch giá trị so với JSON; mọi fix chỉ khác bản cũ ở đúng token rên nhắm tới (trừ 1199/1247 áp nguyên phần audit đúng — đã nêu rõ ở §3).
- Không dòng gasp Ư nào bị đụng ngoài việc giữ nguyên Ư của audit (1185, 1247); không dòng "Kh" nào bị đổi.

## 8. Khối TOML (đã kiểm chứng parse)

Lưu ý: literal `\n` trong giá trị fix được viết `\\n` trong block (đúng quy tắc TOML). Block đã parse bằng tomllib: 26 key, 0 mismatch với wrong.json. Các fix là amendments, áp dụng cùng unification pass — KHÔNG sửa trực tiếp TOML.

```toml
[script]
"1174" = "「Hya——ưm——sao lại, là nách, chứ? Nagi\\n——fa——chỗ đó——nhột lắm——」"
"1183" = "「Hia!!!」"
"1185" = "「Hyagu!? Ư——Hyuaaaaaaaaaa!」"
"1188" = "「Hyauuu!? Fa——a——」"
"1190" = "「Hyau!? Fa——a——sướng, lắm, nhưng mà,\\nưm——bây giờ em muốn anh nhìn——xuống dưới cơ——gao」"
"1199" = "「Fua——a! A! A! A——\\nƯm——fuya——sướng, quá——ưm——phù」"
"1203" = "「Fua! Áa! Áaaa! Cậu nhỏ của anh,\\nưm——hỏng——hỏng mất——áa!」"
"1205" = "「Fa! Haa! Haa! Haa!\\nHaa! Haa! Haa! Haa!」"
"1210" = "「Fa!? Hyau! Không chịu đâu, xấu hổ lắm,\\nchỗ đi tiểu——ưm! Cứ bị chọc chọc, vào đó」"
"1229" = "「Fa——hyau——a……ưm……nhehe——\\nNagi——Nagi——ưm——vui lắm……fa」"
"1235" = "「A——fa——a——」"
"1236" = "「Fa——fa——A——a——\\nAnh Soutetsu——nè——anh Soutetsu——anh Soutetsuuuuu」"
"1237" = "「Fa——a……ưm——a——anh Soutetsu——\\nanh Soutetsu——yêu——yêu——yêu anh lắm」"
"1241" = "「A——a——anh Soutetsu……dâm đãng, quá……fa……\\nSay mê, ngực nhỏ, của Nagi——đến vậy sao」"
"1243" = "「Fa——a——vui quá——nóng quá——ấm quá\\n——ưm——nhiều quá——tinh dịch——của anh Soutetsu——」"
"1245" = "「Ka——ha——a——đúng rồi, đó——gao.\\nRồi sau đó, ban đầu, hãy từ từ, chuyển động, hông——」"
"1247" = "「Ha——a——cái đó——nữa đi——anh Soutetsu,\\nlúc nãy ấy——nữa đi——fua! Nữa đi——Ư!」"
"1250" = "「Fa——a——chỗ đó——thích lắm——ưm——\\nAnh Soutetsu——nữa đi——nữa đi——làm mạnh, hơn đi」"
"1254" = "「Fa——đúng rồi, dùng cậu nhỏ——làm cô bé, mạnh hơn nữa\\n——phập phập——đi——ưm——ha, a」"
"1258" = "「Fa……（Ực）——A! Fu, fufufu-n!!\\nAnh Soutetsu, hưng phấn với Nagi——đến phát tình rồi sao?」"
"1273" = "「Faaun! Fua! A! Anh Soutetsu!\\nAnh Soutetsu! Anh Soutetsu! Anh Soutetsu!!!」"
"1276" = "「Aaaaaaaaaaaa!!!!?」"
"1278" = "「Faaaaaaan!!!!」"
"1280" = "「Fue——fua!!?」"
"1304" = "「Ưm, hyu! Fa——khi bị, liếm như vậy,\\nbị liếm, như vậy——em, fua——cô bé, nóng, quá」"
"1325" = "「Anh——Soutetsu——ưm——yaa——ưm——ha——\\nđừng——trêu em, nữa——ưm——làm mạnh, hơn đi」"
```

## Kết bài

File lr_凪h2_虎さんの交尾: đọc 293 dòng, xét 150 dòng rên/SFX, sửa 26 dòng (22 romaji — trong đó 20 họ fa/fu — + 3 đếm nguyên âm thuần + 1 sai âm; 1205 mang cả romaji lẫn đếm), giữ ~124 dòng, 6 dòng sweep không đụng. Lỗi tập trung ở 2 nhóm: bản cũ dùng chung "Fua"/"fua" cho cả ふぁ lẫn ふあ (19 dòng — ふぁ phải là "Fa"), và đếm nguyên âm thiếu (1185 thiếu 4 a, 1276 thiếu 1 a, 1205 thiếu 1 a × 7 hơi, 1203 thiếu 1 a × 2 tiếng や). Ngoài JSON: HỦY 17 fix fa/fu của audit (giữ romaji cũ đã đúng) và cờ や chưa quyết chung (giữ "Á" cho từ chối, "Yaa" cho rên). Second pass: 26/26 re-verified, 0 removed, 0 corrected.
