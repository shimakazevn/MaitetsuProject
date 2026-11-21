# Moan-fix REVIEW — れいなh3_おもらし自由化大作戦.txt.toml

Slug: `moan-reinah3-omorashi-jiyuuka-daisakusen` — route 04_Reina, H-scene (Reina đặc huấn "tự do hoá" tè dầm trong bồn tắm bao trọn gói; deep throat, tập nhịn/xả, ngâm bồn chung).

## §1. Xác minh file

- TOML: `sources/toml2/translation_toml/04_Reina/#U308c#U3044#U306ah3_#U304a#U3082#U3089#U3057#U81ea#U7531#U5316#U5927#U4f5c#U6226.txt.toml` (tên đĩa #U-escaped; basename không escape là `れいなh3_おもらし自由化大作戦.txt.toml`).
- TOML md5 `6c1b1c26745216faeebd6d942cc2e2f4` — **khớp audit** (ROUTE-AUDIT.md, file 99). UTF-8 BOM + CRLF, 279 khóa `[script]`. Không có bản trùng (audit đã xác nhận).
- CSV3: **1 set duy nhất** (`translation_toml\04_Reina\れいなh3_おもらし自由化大作戦.txt.toml`), 279 dòng, 0 trùng khóa. VN khớp TOML tuyệt đối 279/279 (sau chuẩn hoá `\n`/khoảng trắng — TOML-2 dẹp literal `\n` thành khoảng trắng, CSV3 là chuẩn).
- Audit đã gộp: 24 dòng sai (ROUTE-AUDIT.md: 99 file / 4.710 dòng) — gasp 4, fa/fu 17, SFX 3. TOML trên đĩa vẫn giữ VN gốc (fix audit chưa áp vào TOML — đúng mô hình amendment); bản moan này xây trên **giá trị fix của audit** ở 18 key trùng, và trên VN CSV3 ở 14 key mới.
- Sweep: 4 mục cho file, đã kiểm chứng trực tiếp — nhận 3 fix (1074, 1080, 1099 — audit đã sửa), 1 already-rendered (1199 — giữ). Audit quét bổ sung bắt thêm 1 gasp sweep bỏ sót (1050). **Quét gasp lại ở đợt moan này** (mọi dòng JP kết bằng っ trước `」`): không còn gasp nào sót — các っ còn lại đều đã diễn (はっ→"Ha", んっ→"ưm", ふっ→"phù", ごくっ→"goku", ちゅっ→"chụt", ひゅっ→"hyu", うっ→"ư", んうっ→"ưm" theo quy ước file) hoặc là っ nhấn mạnh gắn từ nội dung (991 舌がっ, 1029 のにっ, 1177 漏らすっ, 1187 大好きだっ, 1197 ないっ, 1132 ぺろっ→"liếm") — giữ nguyên theo quy tắc sweep.
- Không có dòng "Kh" nào trong file (0 dòng chứa token `Kh`/`kh` độc lập) — không có gì để đổi sang Ư. Không đụng dòng gasp Ư nào của audit/sweep (1099 chỉ sửa số lượng u, giữ nguyên Ư cuối dòng của audit).

## §2. Moan inventory

- Đã đọc **279/279 dòng** (toàn bộ file, JP + TW + VN).
- Ứng viên rên/SFX theo lọc máy: **193 dòng** (181 dòng JP chứa âm rên/thở/gasp/SFX + 12 dòng VN-only chứa token rên; trong 12 dòng VN-only, 11 là dương tính giả do `ực` trong từ thường "thực/rực/lực", chỉ 775 là ứng viên thật — đã flag, không sửa).
- **Sửa 32 dòng, giữ 161 dòng ứng viên.**
- Phân loại 32 dòng sửa (1014 thuộc 2 nhóm):
  - Romaji họ fa/fu (ふぁ→Fa, ふあ→Fua, ふや→Fuya, ふぇ→Fue, ぷあ→Pua): **17 dòng** — 1014, 1019, 1031, 1047, 1048, 1053, 1068, 1073, 1078, 1083, 1119, 1121, 1195, 1196, 1197, 1198, 1200.
  - Romaji họ ひあ (ひあ→Hia): **3 dòng** — 1014, 1016, 1055 (ひゃっ→"Hya" ở 1013/1195 đã đúng, giữ).
  - Romaji sai âm (VN cũ đọc sai hẳn âm JP): **3 dòng** — 1018 (ふゅあ→"Fyua", cũ "Hya"), 1040 (やぁん→"Yaan", cũ "Á~"), 1193 (ふゆ→"Fuyu", cũ "Hu…").
  - Romaji mất phụ âm mora (くっ→"Ku"): **2 dòng** — 1043, 1045 (cũ "ư"/"Ư!" mất hẳn k).
  - Đếm nguyên âm (công thức 1 + số う/ぅ/あ/ぁ/ー): **7 dòng** — 1025 (4u→3u), 1085 (7u→8u), 1092 (4u→5u), 1099 (7u→4u), 1102 (1u→2u), 1116 (1u→2u), 1192 (3a→2a).
  - Độ dài ん (んんっ = 2 mora): **1 dòng** — 1061 ("ưm"→"ưmm").
- Trùng audit: **18/32 key** (chỉ khác fix audit ở đúng token rên — xem §6). Mới: **14 key**.
- Hoàn lại đúng VN cũ (fix == old_vn — audit đã Việt hoá romaji gốc trước quy tắc romaji, đợt moan hoàn lại): **3 dòng** — 1048 ("Fuya"), 1119 ("Fuei!"), 1121 ("Pua!"). Tiền lệ: reinah4 5 dòng, lr-jiekei 12 dòng.

## §3. Các dòng sửa (32 dòng)

### 1014 [れいな] — romaji (ひあ + fa)
- JP: `「ひあっ――んっ――れいな――れいなもっ――んっ――\nしゅき――だいしゅきっ――そうてつ、さんっ――ふぁ」`
- TW: `「呀啊……玲奈……玲奈也是，愛你，最愛你了……雙鐵先生」`
- VN cũ: `「Hya——ưm——Reina——Reina cũng——ưm——\nthích——thích nhất——anh Soutetsu——ha」`
- Mới: `「Hia——ưm——Reina——Reina cũng——ưm——\nthích——thích nhất——anh Soutetsu——Fa」`
- Lý do: xây trên fix audit (audit chỉ sửa ふぁ→"phà", giữ "Hya" cho ひあっ). Quy tắc 3b: ひあ→"Hia" ("Hya" mất mora i — ひあ = hi+a, không phải hya). ふぁ→"Fa" (1 mora, romaji fallback).

### 1016 [れいな] — romaji (ひあ)
- JP: `「ひあっっ――んっ――あつい――おなかっ――\nれいなの――おなか――あつい――ですぅっ――」`
- TW: `「呀啊、啊嗯……裡面……好熱，玲奈的……裡面好熱呀……」`
- VN cũ: `「Hya——ưm——nóng——bụng——\nbụng của Reina——nóng——quá——」`
- Mới: `「Hia——ưm——nóng——bụng——\nbụng của Reina——nóng——quá——」`
- Lý do: ひあっっ→"Hia" (quy tắc 3b; っっ cuối là nhấn cắt, đã diễn ngầm). Phần còn lại là diễn nghĩa của audit, không thuộc phạm vi moan.

### 1018 [れいな] — romaji, sai âm
- JP: `「ふゅあああああああああああんっ！！！」`
- TW: `「呀啊啊啊啊啊啊！！！」`
- VN cũ: `「Hyaaaaaaaaaaaaaaa!!!」`
- Mới: `「Fyuaaaaaaaaaaan!!!」`
- Lý do: VN cũ đọc sai hẳn âm JP — ふゅあ = "Fyua" (fu + yu + a), không phải "Hya" (mất f, sai yu→ya). Đếm: JP có 11 chữ あ → 11 a + n (っ diễn ngầm, !!! giữ).

### 1019 [れいな] — romaji (fa/fu)
- JP: `「ふやああんっ！」`
- TW: `「呀啊啊啊！」`
- VN cũ: `「Hyaaaaan!」`
- Mới: `「Fuyaaaan!」`
- Lý do: xây trên fix audit "Phuyaaan!" → romaji "Fuyaaan!" (ふやああ = 3 a + n; tiền lệ lr-mikuro 1731 "Fuyaaaaaaan", reinah4 1983 "Fuyaaaan"). VN cũ "Hyaaaaan!" mất hẳn fu-ya.

### 1025 [れいな] — đếm nguyên âm
- JP: `「ふぉぅ～。ごくらくごくらく、ですよぉ」` — **xem cờ F10: codepoint là ふ + ぅ + ぅ (U+3045 ×2), KHÔNG phải ふぉぅ**
- TW: `「呼……真舒服真舒服」`
- VN cũ: `「Fuuuu~. Cực lạc cực lạc, quá đi mất ạ~」`
- Mới: `「Fuuu~. Cực lạc cực lạc, quá đi mất ạ~」`
- Lý do: JP ふぅぅ = fu + u + u = 3 nguyên âm u (công thức 1 + 2 ぅ). VN cũ 4 u — thừa 1. Đây là hơi thở dài thư giãn (không phải rên cao trào), giữ dạng romaji, chỉ sửa số lượng.

### 1031 [れいな] — romaji (fa/fu)
- JP: `「ふぁ」`
- TW: `「哇」`
- VN cũ: `「Fua」`
- Mới: `「Fa」`
- Lý do: xây trên fix audit "Phà" → romaji "Fa". ふぁ = 1 mora "Fa"; VN cũ "Fua" thừa 1 u (tiền lệ ふかみh3 2301/2345 ふぁ→"Fa").

### 1040 [れいな] — romaji, sai âm
- JP: `「やぁんっ」`
- TW: `「哎呀」`
- VN cũ: `「Á~」`
- Mới: `「Yaan~」`
- Lý do: やぁんっ = ya + a + n (2 a) — "Á~" mất hẳn phụ âm y (tiền lệ ふかみh3 2784 やぁん→"Yaan"). Giữ dấu ~ của VN cũ (diễn hơi kéo dài).

### 1043 [双鉄H] — romaji, mất phụ âm mora
- JP: `「んっ――くっ――れいなっ――れいなっ！」`
- TW: `「唔……玲奈，玲奈！」`
- VN cũ: `「Ưm——ư——Reina——Reina!」`
- Mới: `「Ưm——Ku——Reina——Reina!」`
- Lý do: くっ = tiếng gằn "Ku" — VN cũ "ư" mất hẳn phụ âm k (tiền lệ ふかみh3 2349 くっ→"Ku").

### 1045 [双鉄H] — romaji, mất phụ âm mora
- JP: `「くっ！」`
- TW: `「唔！」`
- VN cũ: `「Ư!」`
- Mới: `「Ku!」`
- Lý do: như 1043 — くっ→"Ku" (cùng tiền lệ ふかみh3 2349; cờ F2 của ハチロクh5 đã được ふかみh3 chốt bằng "Ku").

### 1047 [れいな] — romaji (fa/fu)
- JP: `「ひゅっ――ふあっ――」`
- TW: `「啊……啊啊……」`
- VN cũ: `「A……a a……」`
- Mới: `「Hyu——Fua——」`
- Lý do: xây trên fix audit "Hyu——phùa——" → "Hyu——Fua——". ひゅっ→"Hyu" của audit đã đúng (giữ); ふあっ→"Fua" (romaji fallback).

### 1048 [れいな] — romaji (fa/fu) — HOÀN LẠI ĐÚNG VN CŨ
- JP: `「ふやっ――あっ――れいな――きもちいっ――\nすりすり、され、て――きもち、いい――です、よぉっ」`
- TW: `「啊……玲奈……好舒服……蹭來蹭去的……好舒服哦」`
- VN cũ: `「Fuya——a——Reina——sướng——\nbị cọ cọ, thế này——sướng, lắm——ạ~」`
- Mới: `「Fuya——a——Reina——sướng——\nbị cọ cọ, thế này——sướng, lắm——ạ~」` (= VN cũ)
- Lý do: xây trên fix audit "Phuya——…" → hoàn lại romaji "Fuya" (ふやっ = Fuya; tiền lệ paulette-h3 982, lr-reinah1 1215). Audit chỉ đổi đúng token này nên giá trị moan trùng hẳn VN cũ — ghi nhận theo tiền lệ reinah4.

### 1053 [れいな] — romaji (fa/fu)
- JP: `「ふあっ――あっ――あんっ――んっ！\nふ、といっ――ですっ――いつも――いつも、よりぃ」`
- TW: `「啊啊、啊嗯、啊啊啊！好粗……比之前……還要粗……」`
- VN cũ: `「A a、a ưm、a a a! To……to hơn……\nbình thường……rồi」`
- Mới: `「Fua、a ưm、a a a! To……to hơn……\nbình thường……rồi」`
- Lý do: xây trên fix audit "Phùa、…" → "Fua、…". Chỉ đổi token ふあっ; phần còn lại (kể cả "a ưm" cho あんっ/んっ) là quyết của audit, không thuộc phạm vi moan.

### 1055 [れいな] — romaji (ひあ)
- JP: `「ひああああああああああんっ！」`
- TW: `「啊啊啊啊啊啊！」`
- VN cũ: `「Hyaaaaaaaaaaaaaaa!」`
- Mới: `「Hiaaaaaaaaaan!」`
- Lý do: ひあ = "Hia" (quy tắc 3b — "Hya" sai mora); đếm: JP có 10 chữ あ → 10 a + n (っ diễn ngầm). VN cũ 15 a + sai âm đầu.

### 1061 [れいな] — độ dài ん
- JP: `「んぶっ――むっ――んっ――んんっ――むっ――\nぐっ――ぐうっ――んっうっ――」`
- TW: `「啊嗯……嗚嗚……啾嚕……嗯……嗚嗚嗚……啊嗯……」`
- VN cũ: `「Nbu——mu——ưm——ưm——mu——\nGu——guu——ưm u——」`
- Mới: `「Nbu——mu——ưm——ưmm——mu——\nGu——guu——ưm u——」`
- Lý do: token thứ 4 là んんっ = 2 mora ん; VN cũ "ưm" (1 m) mất 1 mora → "ưmm" (tiền lệ lr-mikuro んんっ→"ưmm", 凪h2 んんんっ→"Ưmmm"). Các token khác đã đúng (んぶっ→"Nbu", んっ→"ưm", ぐうっ→"guu" 2u, んっうっ→"ưm u"). Xem cờ F5 (mâu thuẫn với "nn" của ふかみh3 F8 — chờ đợt thống nhất).

### 1068 [れいな] — romaji (fa/fu)
- JP: `「ふあっ――んっ――そうてつさん――んっ――\nは――しゅきっ――だいしゅき――そおてつさぁんっ」`
- TW: `「啊嗯……蛤啊……雙鐵先生……愛你，最愛你了……雙鐵先生」`
- VN cũ: `「Ha——ưm——anh Soutetsu——ưm——\nHa——thích——thích nhất——anh Soutetsu~」`
- Mới: `「Fua——ưm——anh Soutetsu——ưm——\nHa——thích——thích nhất——anh Soutetsu~」`
- Lý do: xây trên fix audit "Phùa——…" → "Fua——…". Chỉ đổi token ふあっ.

### 1073 [れいな] — romaji (fa/fu)
- JP: `「んきゅっ！　ふあっ――あっ――あっ！！」`
- TW: `「啊嗯！蛤啊、啊啊啊啊！！」`
- VN cũ: `「Ưm kyu! Ha——a——a!!」`
- Mới: `「Ưm kyu! Fua——a——a!!」`
- Lý do: xây trên fix audit "Ưm kyu! Phùa——…" → "Fua". んきゅっ→"Ưm kyu" của audit đã đúng, giữ.

### 1078 [れいな] — romaji (fa/fu)
- JP: `「やあっ！　これっ――れいなっ――\nはずかしっ――はずかし――ぃっ――で――ふあっ！」`
- TW: `「啊！這個……玲奈……好害羞……羞死了……啊嗯！」`
- VN cũ: `「A! Cái này——Reina——\nXấu hổ——xấu hổ——quá——đi——ha!」`
- Mới: `「A! Cái này——Reina——\nXấu hổ——xấu hổ——quá——đi——Fua!」`
- Lý do: xây trên fix audit "…——phùa!" → "…——Fua!". やあっ→"A!" là diễn nghĩa, không thuộc phạm vi moan.

### 1083 [れいな] — romaji (fa/fu)
- JP: `「ふにゃっ――んっ――ちゅ――ちゅうっ――\nちゅ――ちゅむっ――ふぁっ――ん～――ちゅるっ」`
- TW: `「啾……啾……嗯……啊嗯……啾嚕」`
- VN cũ: `「Funya——ưm——chu——chuu——\nChu——chumu——fua——n~——churu」`
- Mới: `「Funya——ưm——chu——chuu——\nChu——chumu——Fa——n~——churu」`
- Lý do: xây trên fix audit "…——phà——…" → "…——Fa——…". ふにゃっ→"Funya" và họ ちゅ→"chu/chuu/chumu/churu" của VN cũ đã đúng, giữ.

### 1085 [れいな] — đếm nguyên âm
- JP: `「ずっ――ずうううううううっ――ずじゅっ！\n――じゅるるるる～～――――ん～ッ――ごくっ」`
- TW: `「啾、啾嚕嚕嚕！啾嚕嚕嚕……嗯……咕嘟……」`
- VN cũ: `「Zu——zuuuuuuu——zuju!\n——Jururururu~~————n~——goku」`
- Mới: `「Zu——zuuuuuuuu——zuju!\n——Jururururu~~————n~——goku」`
- Lý do: ずうううううううっ = zu + 7 う → 8 u (công thức 1 + 7); VN cũ 7 u — thiếu 1. Các token khác đã đúng (ずじゅっ→"zuju", じゅるるるる→"Jururururu", ん～ッ→"n~", ごくっ→"goku").

### 1092 [れいな] — đếm nguyên âm
- JP: `「ンぶっ――むううっ――んっ――ふっ――んっ――\n（スヒっ）――（スヒっ）――んふふぅぅぅ～」`
- TW: `「嗚……嗯……啊嗯……啊……呼……呼……」`
- VN cũ: `「Nbu——muuu——ưm——phù——ưm——\n（Suhi）——（Suhi）——nfufuuu~」`
- Mới: `「Nbu——muuu——ưm——phù——ưm——\n（Suhi）——（Suhi）——nfufuuuu~」`
- Lý do: token cuối んふふぅぅぅ～ = ん + ふ(u) + ふ(u) + ぅ×3 = 5 u; VN cũ "nfufuuu" chỉ 4 u — thiếu 1. Các token khác đã đúng (むううっ→"muuu" 3u, んふっ→"nfu", （スヒっ）→"（Suhi）", ふっ→"phù").

### 1099 [れいな] — đếm nguyên âm (giữ Ư gasp của audit)
- JP: `「ンムッ――むっ――んううううっ～～～～っ！」`
- TW: `「嗯……嗚嗚！」`
- VN cũ: `「Nmu——mu——uuuuuuu~~~~!」`
- Mới: `「Nmu——mu——uuuu~~~~Ư!」`
- Lý do: xây trên fix audit (audit thêm Ư cuối dòng — gasp đã khóa, KHÔNG đụng). Chỉ sửa số lượng: んううううっ = ん + 4 う → 4 u (công thức 1 + 3); VN cũ/audit giữ 7 u — thừa 3. Parent đã flag sẵn ở audit ("1099: 7 u cho 4 う").

### 1102 [れいな] — đếm nguyên âm
- JP: `「んふー、このくらい固くなったら、\nきっと、だいじょうぶですよねぇ」`
- TW: `「嗯……變得這麼硬了，肯定沒問題吧」`
- VN cũ: `「Nfu~, cứng đến mức này rồi thì,\nchắc chắn, là không sao rồi nhỉ~」`
- Mới: `「Nfuu~, cứng đến mức này rồi thì,\nchắc chắn, là không sao rồi nhỉ~」`
- Lý do: んふー = n + fu + ー (trường âm = +1 mora) → 2 u (tiền lệ lr-nagih2: あ + 11 ー = 12 mora). VN cũ 1 u — thiếu 1.

### 1116 [れいな] — đếm nguyên âm
- JP: `「んっぐー」`
- TW: `「嘿嘿」`
- VN cũ: `「Ngu~」`
- Mới: `「Nguu~」`
- Lý do: んっぐー = n + gu + ー → 2 u (cùng tiền lệ ー như 1102). Đây là tiếng cười bịt miệng (TW 嘿嘿); giữ dạng romaji, chỉ sửa số lượng.

### 1119 [れいな] — romaji (fa/fu) — HOÀN LẠI ĐÚNG VN CŨ
- JP: `「ふぇいっ！」`
- TW: `「嘿！」`
- VN cũ: `「Fuei!」`
- Mới: `「Fuei!」` (= VN cũ)
- Lý do: xây trên fix audit "Phuêi!" → hoàn lại romaji "Fuei!" (ふぇいっ = fu-e-i; tiền lệ reinah4 1938 ふぇ→"Fue", lr-fukamih1 1252/1254 "Fue?", lr-mikuro 1708 "Fue!?"). Audit chỉ đổi đúng token này nên giá trị moan trùng hẳn VN cũ — ghi nhận theo tiền lệ reinah4. (Tiền lệ giữ "Phuê" ở ふかみh1 993 / 凪ふかみ01 1547 là trường hợp khác — xem ghi chú §4.)

### 1121 [れいな] — romaji (fa/fu) — HOÀN LẠI ĐÚNG VN CŨ
- JP: `「――ぷあっ！　あっ――どうですか？　そうてつさぁん。\nおもらし、しちゃいそうになりましたかぁ？」`
- TW: `「噗哈！啊……怎麼樣？雙鐵先生。感覺要失禁了嗎？」`
- VN cũ: `「——Pua! A——thế nào ạ? Anh Soutetsu~.\nAnh có cảm giác, sắp tè dầm ra chưa ạ~?」`
- Mới: `「——Pua! A——thế nào ạ? Anh Soutetsu~.\nAnh có cảm giác, sắp tè dầm ra chưa ạ~?」` (= VN cũ)
- Lý do: xây trên fix audit "——Phùa! …" → hoàn lại romaji "Pua!" (ぷあっ = Pua; tiền lệ ふかみh3 2351/2385 ぷあっ→"Pua"). Audit chỉ đổi đúng token này nên giá trị moan trùng hẳn VN cũ.

### 1192 [双鉄H] — đếm nguyên âm
- JP: `「わぁい！」`
- TW: `「耶！」`
- VN cũ: `「Waaai!」`
- Mới: `「Waai!」`
- Lý do: わぁい = wa + ぁ + i → 2 a (công thức 1 + 1 ぁ); VN cũ 3 a — thừa 1. Đây là tiếng reo (không phải rên cao trào) nhưng vẫn là diễn âm — áp công thức cơ học. Xem cờ F9.

### 1193 [れいな] — romaji, sai âm
- JP: `「おなかっ――ぐりって――ぐりって――んっ――\nふゆううううううううううううううううううん！！」`
- TW: `「肚子裡面……插進來了……嗚嗚……嗚嗚嗚嗚嗚嗚！！」`
- VN cũ: `「Bụng——bị đâm——bị đâm——ưm——\nHuuuuuuuuuuuuuuuuuuun!!」`
- Mới: `「Bụng——bị đâm——bị đâm——ưm——\nFuyuuuuuuuuuuuuuuuuuuun!!」`
- Lý do: VN cũ đọc sai hẳn âm đầu — ふゆ = "Fuyu" (fu + yu), không phải "Hu" (mất f và y). Đếm: ふ(1u) + ゆ(1u) + 18 う = 20 u + n; VN cũ 19 u — vừa sai âm vừa thiếu 1 u.

### 1195 [れいな] — romaji (fa/fu)
- JP: `「ふあっ――あちゅ――んっ！　ひゃっ――\nあっ――ああっっ――あっ――」`
- TW: `「蛤啊……啊……啊嗯……啊、啊啊……啊啊啊」`
- VN cũ: `「Ha——achu——ưm! Hya——\nA——aa——a——」`
- Mới: `「Fua——achu——ưm! Hya——\nA——aa——a——」`
- Lý do: xây trên fix audit "Phùa——…" → "Fua——…". ひゃっ→"Hya" của VN cũ đã đúng (giữ); あちゅ→"achu", ああっっ→"aa" đã đúng.

### 1196 [れいな] — romaji (fa/fu)
- JP: `「ふぁっ――あっ――んっ――んっ――んむっ――\nんくっ――ごくっ――ごくっ――――――ごくんっ」`
- TW: `「蛤啊……啊……嗯、嗯啊……咕嘟、咕嘟、咕嘟……」`
- VN cũ: `「Fua——a——ưm——ưm——nmu——\nNku——goku——goku——————gokun」`
- Mới: `「Fa——a——ưm——ưm——nmu——\nNku——goku——goku——————gokun」`
- Lý do: xây trên fix audit "Phà——…" → "Fa——…". ふぁっ = 1 mora "Fa"; VN cũ "Fua" thừa 1 u. Các token khác đã đúng (んむっ→"nmu", んくっ→"Nku", ごくっ→"goku", ごくんっ→"gokun").

### 1197 [れいな] — romaji (fa/fu)
- JP: `「ふぁっ――あっ――おもらし――\nしても――しても――はずかしく、ないっ」`
- TW: `「蛤啊……啊……就算失禁……也沒什麼……可害羞的」`
- VN cũ: `「Ha——a——tè dầm——\ncó làm thế——có làm thế——cũng không, xấu hổ」`
- Mới: `「Fa——a——tè dầm——\ncó làm thế——có làm thế——cũng không, xấu hổ」`
- Lý do: xây trên fix audit "Phùa——…" → "Fa——…" (JP là ふぁっ, 1 mora — khác 1198/1200 là ふあっ). Chỉ đổi token đầu.

### 1198 [れいな] — romaji (fa/fu)
- JP: `「ふあっ――あっ――そうてつ、さぁん」`
- TW: `「蛤啊……啊……雙鐵先生」`
- VN cũ: `「Ha——a——anh Soutetsu」`
- Mới: `「Fua——a——anh Soutetsu」`
- Lý do: xây trên fix audit "Phùa——…" → "Fua——…" (JP là ふあっ, 2 mora).

### 1200 [れいな] — romaji (fa/fu)
- JP: `「ふあっ――あっ――あっ――あっ――」`
- TW: `「蛤啊、啊、啊啊……」`
- VN cũ: `「Ha——a——a——a——」`
- Mới: `「Fua——a——a——a——」`
- Lý do: xây trên fix audit "Phùa——…" → "Fua——…" (JP là ふあっ, 2 mora).

## §4. Các dòng rên đã xét, giữ nguyên (ghi chú đáng kể)

- **Gasp Ư của audit/sweep — giữ toàn bộ, không xét lại:** 1050 (っ→"Ư"), 1074 (っ！→"Ư!"), 1080 (っ！！！？→"Ư!!!?"), 1099 (thêm Ư cuối — chỉ sửa số lượng u, §3). 1199 sweep "already-rendered" — VN "Ha——a——chụt——chiu——\nChụt——chụt——chụt——chuuu~" đã diễn đủ (ちゅうう～っ = 3u ✓).
- **Họ ん → "ưm" — quy ước file, audit đã chốt (giữ):** 1056 んむうっ→"ưm", 1090 んうっ→"ưm" (fix audit, parent-verified), 1130 んうっ→"ưm", 1046 ぅっ→"Ư", 1054 うっ→"ư" (fix audit). Audit review ghi rõ 1056/1090 "nén nhất quán trong file (tiền lệ h2 1045 んうっっ→'ưm')" — không sửa ở đợt moan.
- **ふっ → "phù" — giữ toàn bộ file:** 1067 (×2), 1071, 1092, 1101 — tiền lệ đã khóa ở ふかみh3 ("ふ/ふっ→'phù'"). Câu hỏi mở "Fu" hay "phù" (reinah4 F2) để đợt thống nhất quyết, không đổi ở đây.
- **Romaji đã đúng, giữ:** 1013 ひゃっ→"Hya", 1064 ひゅっ→"hyu" (+えうっ→"eu"), 1071 やっっ→"ya" (+ふっ→"Phù"), 1083 ふにゃっ→"Funya", 1095 んきゅううっ→"Ưm kyuu!" (2u ✓), 1065 んぐうっ→"nguu" (2u ✓), 1195 ひゃっ→"Hya", 1026 ふえ？→"Fue?", 1029 ひえっ→"Hie!?", 1081 うおっ→"Uo!?".
- **Họ ちゅ → "chụt" — quy ước file, giữ:** 1089 (ちゅううっ→"chụt", れるっ/れろっ→"chụt"), 1090 (fix audit), 1091 (ちゅううううっ→"chụtttttt" — xem cờ F6), 1101 (チュっ/ちゅろっ/れるっ/れろっ→"chụt"), 1199. 1089 あむ～～～～んっ→"ammmmm" (a + 5 m: む + 4 ~ — giữ theo quy ước m-hum của file).
- **Tiếng cười — giữ:** 1118/1128 えへへ→"e he he", 1102/1116 chỉ sửa số lượng (không đổi dạng).
- **SFX trong （ ） — giữ toàn bộ dạng động từ Việt** (tiền lệ ふかみh3 F4 — chưa áp công thức đếm ở đợt moan): 1743 （かぽーん）→"（Ào）", 1742 （ざばあっ！）→"（Ào!）", 1738, 1740, 1741, 1747, 1752/1753/1754, 1721, 1725, 1722–1735, 1744–1748, 1758 （ぺろっ）→"（Liếm）" — xem cờ F4.
- **っ nhấn mạnh / đã diễn — giữ:** 991 舌がっ, 1029 のにっ, 1177 漏らすっ, 1183/1179 れいなっ, 1187 大好きだっ, 1197 ないっ, 1132 ぺろっ→"liếm", 1094 っぐ→"gu" (xem cờ F7).
- **Filler / diễn nghĩa — không thuộc phạm vi moan, giữ:** 775 (xem cờ F1), 1020 む――→"Hừm——", 1105 うむ→"Ừm.", 1210 あの……えっと→"Ưm……ờm", 1130 あついっっ→"Nóng" (diễn nghĩa), 1016 ですぅっ→"quá" (diễn nghĩa), 1126/1107 ああ→"Ừ", 1138 おし、っこ (nói ngọng), 1113 しこ/しゅこ→"sục" (động từ).
- **Ghi chú về 1119:** tiền lệ giữ "Phuê" ở ふかみh1 993 (ふぇっ→"Phuê!?") và 凪ふかみ01 1547 ("Phuêê.") là các dòng đã được parent-verified KEEP — nhưng ở file này VN gốc đã là romaji "Fuei!" và đa số tiền lệ sau đó (reinah4, lr-fukamih1, lr-mikuro, paulette-lr-h1) đều chuyển ふぇ→"Fue" trong cảnh H, nên đợt này hoàn lại "Fuei!". Nếu đợt thống nhất chốt "Phuê" cho ふぇ thì 1119 quay lại "Phuêi!" cùng với các dòng đó.

## §5. Cờ (chưa quyết — không tự quyết, ghi lại cho parent / đợt thống nhất / audit)

- **F1 — 775 [双鉄H] (không sửa):** JP `「……う、む？」` / TW `「……嗯？」` / VN `「……Ư, m?」` — む diễn thành mỗi "m" (mất nguyên âm u). Đây là ngập ngừng trong thoại, không phải rên; không rõ "m" là cố ý diễn nói lắp hay mất âm. Để audit quyết.
- **F2 — 1115 [れいな] (không sửa — nói ngọng, miệng đầy):** JP `「んふふ～　ほれふぁら、えひふぁ、へひほーれふぅ」` / TW `「嘿嘿……啾嚕……啾嚕……」` / VN `「Nfufu~ ho re fua ra, e hi fua, he hi ho re fuu」` — lời nói ngọng (garbled speech, miệng đầy) — theo quy tắc 3b KHÔNG phải dòng rên, để audit. Audit đã flag sẵn: "1115 (lời ngọng phiên âm — chuẩn hoá ふぁ→'phà' hay giữ nguyên cả dòng)".
- **F3 — 1133 [れいな] (không sửa — chờ Hieu):** JP `「…ふえっ？」` / TW `「…」` / VN `「…hả?」` — audit đã flag "Chờ Hieu: 1133 (ふえっ？→'hả?' hay 'phuê?')". Không quyết ở đợt moan.
- **F4 — SFX trong （ ） chưa áp công thức đếm (đợt thống nhất):** 1738 （ぞろおお…18 お…っ）→"（Rộtttt…40 t…!!!）"; 1740 （ぷしゃああ…13 あ…っ）→"（Ào…15 o…!）"; 1741 （ちょおおおおおおお = 8 お）→"（Ào…15 o…）"; 1747 （ずぶううううううう = 7 う）→"（Phập…12 p…!!!!）"; 1752 （きゅううっ = 2 う）→"（Siết chặtttttt!）" (11 t); 1753 （きゅうううううっ = 5 う）→"（Siết chặtttttt!）" (7 t); 1754 （きゅううううううっ = 6 う）→"（Siết chặttttttt）" (8 t); 1721 （ずりゅううううううっ = 6 う）→"（Nhópppppppp!）" (14 p); 1725 （みちっ）→"（Phậpppppp!!!）" (6 p). Các dòng này dùng quy ước lặp phụ âm t/p thay cho nguyên âm — đợt moan giữ nguyên theo tiền lệ ふかみh3 F4.
- **F5 — 1061 �んんっ → "ưmm" (mâu thuẫn tiền lệ):** bản này dùng "ưmm" (tiền lệ lr-mikuro, 凪h2 "Ưmmm"); ふかみh3 F8 dùng "nn" cho んんっ (theo lr_ふかみh1/lr_れいな追加h) và tự flag là chưa chốt ("nn" hay "nnn"). Cần một quyết toàn dự án ở đợt thống nhất.
- **F6 — 1091 ちゅううううっ → "chụtttttt" và 1089 ちゅううっ → "chụt":** độ dài う (4u / 2u) được diễn bằng lặp chữ t / bỏ hẳn, không phải bằng nguyên âm. Giữ theo quy ước "chụt" của file; đợt thống nhất quyết có áp công thức đếm cho họ ちゅう… hay không.
- **F7 — 1094 っぐ → "gu" (giữ):** JP `「ん……ぉ……っぐ――んぐっ――はっ――うっ」` / VN `「Ưm……o……gu——ngu——ha——ư」` — っ đầu token (glottal catch trước ぐ) bị mất; không có dạng romaji chuẩn cho っ đầu token, và "Ưgu" sẽ diễn thừa. Giữ "gu"; đợt thống nhất có thể xét lại.
- **F8 — 1040 "Yaan~":** dấu ~ giữ từ VN cũ ("Á~"); vị trí ~ sau n (thay vì sau nguyên âm) là phán đoán của đợt này.
- **F9 — 1192 "Waai!":** tiếng reo (không phải rên cao trào) — áp công thức đếm cơ học (2 a). Nếu tiếng reo nằm ngoài phạm vi moan thì hoàn lại "Waaai!".
- **F10 — 1025 bẫy codepoint (bài học):** JP hiển thị "ふぉぅ" nhưng codepoint thực là ふ (U+3075) + ぅ (U+3045) + ぅ (U+3045) — tức ふぅぅ, KHÔNG phải ふぉぅ (ぉ là U+3049). Fix "Fuuu~" (3 u) dựa trên codepoint, không dựa trên hình chữ. Cùng bài học lr-mayamih1 (audit nhầm ぅ thành ぉ).
- **F11 — ふっ → "phù" hay "Fu" (câu hỏi mở toàn dự án):** file này giữ "phù" cho mọi ふっ (1067, 1071, 1092, 1101) theo tiền lệ đã khóa ở ふかみh3; reinah4 đã chuyển 5 dòng sang "Fu" và flag F2 chờ quyết. Đợt thống nhất quyết một dạng.

## §6. Lượt soát 2 + kiểm chứng cơ học

- **Lượt soát 2: tổng 32 / tái kiểm chứng 32 / bỏ 0 / sửa 0.** Đọc lại toàn bộ 32 giá trị fix đối chiếu từng JP (+TW) lần thứ hai — không phát hiện sai sót nào sau lượt đầu.
- JSON 32 mục, khóa string; jp/tw/old_vn khớp CSV3 tuyệt đối 32/32; 0 trùng khóa.
- Khối TOML parse bằng tomllib: 32 khóa, **0 sai lệch giá trị** so với JSON. Giá trị fix dùng literal `\n` (2 ký tự) theo quy ước dự án; trong khối TOML viết thành `\\n` (đã kiểm chứng parse ra đúng literal `\n`).
- Đếm nguyên âm kiểm chứng độc lập bằng máy: 1018 11a ✓, 1055 10a ✓, 1193 20u ✓, 1085 8u ✓, 1092 5u ✓, 1099 4u ✓, 1025 3u ✓ (codepoint-verified ふぅぅ), 1102 2u ✓, 1116 2u ✓, 1192 2a ✓, 1040 2a ✓, 1019 3a ✓.
- Diff fix moan vs fix audit (18 key trùng): **chỉ khác đúng token rên** — 0 thay đổi nghĩa/đại từ/thuật ngữ. 3 dòng hoàn lại đúng VN cũ (1048, 1119, 1121) — audit chỉ đổi đúng token fa/fu.
- 0 dòng "Kh" bị đổi (file không có dòng "Kh"). 0 dòng gasp Ư bị xét lại (1099 giữ Ư của audit).
- Cơ sở tổng: ROUTE-MOANS.md hiện tại **36 file / 846 dòng** (kiểm chứng lại lần cuối trước khi nộp: lúc bắt đầu là 35/843 — loop đã gộp lr_日々姫真闇h1 (+3) trong lúc làm file này; snippet đã rebase theo cơ sở mới 36/846 → tổng sau file này 37/878).

## §7. Khối TOML (parse-verified, 32 khóa, 0 sai lệch)

```toml
"1014" = "「Hia——ưm——Reina——Reina cũng——ưm——\\nthích——thích nhất——anh Soutetsu——Fa」"
"1016" = "「Hia——ưm——nóng——bụng——\\nbụng của Reina——nóng——quá——」"
"1018" = "「Fyuaaaaaaaaaaan!!!」"
"1019" = "「Fuyaaan!」"
"1025" = "「Fuuu~. Cực lạc cực lạc, quá đi mất ạ~」"
"1031" = "「Fa」"
"1040" = "「Yaan~」"
"1043" = "「Ưm——Ku——Reina——Reina!」"
"1045" = "「Ku!」"
"1047" = "「Hyu——Fua——」"
"1048" = "「Fuya——a——Reina——sướng——\\nbị cọ cọ, thế này——sướng, lắm——ạ~」"
"1053" = "「Fua、a ưm、a a a! To……to hơn……\\nbình thường……rồi」"
"1055" = "「Hiaaaaaaaaaan!」"
"1061" = "「Nbu——mu——ưm——ưmm——mu——\\nGu——guu——ưm u——」"
"1068" = "「Fua——ưm——anh Soutetsu——ưm——\\nHa——thích——thích nhất——anh Soutetsu~」"
"1073" = "「Ưm kyu! Fua——a——a!!」"
"1078" = "「A! Cái này——Reina——\\nXấu hổ——xấu hổ——quá——đi——Fua!」"
"1083" = "「Funya——ưm——chu——chuu——\\nChu——chumu——Fa——n~——churu」"
"1085" = "「Zu——zuuuuuuuu——zuju!\\n——Jururururu~~————n~——goku」"
"1092" = "「Nbu——muuu——ưm——phù——ưm——\\n（Suhi）——（Suhi）——nfufuuuu~」"
"1099" = "「Nmu——mu——uuuu~~~~Ư!」"
"1102" = "「Nfuu~, cứng đến mức này rồi thì,\\nchắc chắn, là không sao rồi nhỉ~」"
"1116" = "「Nguu~」"
"1119" = "「Fuei!」"
"1121" = "「——Pua! A——thế nào ạ? Anh Soutetsu~.\\nAnh có cảm giác, sắp tè dầm ra chưa ạ~?」"
"1192" = "「Waai!」"
"1193" = "「Bụng——bị đâm——bị đâm——ưm——\\nFuyuuuuuuuuuuuuuuuuuuun!!」"
"1195" = "「Fua——achu——ưm! Hya——\\nA——aa——a——」"
"1196" = "「Fa——a——ưm——ưm——nmu——\\nNku——goku——goku——————gokun」"
"1197" = "「Fa——a——tè dầm——\\ncó làm thế——có làm thế——cũng không, xấu hổ」"
"1198" = "「Fua——a——anh Soutetsu」"
"1200" = "「Fua——a——a——a——」"
```

## Kết bài

File れいなh3_おもらし自由化大作戦.txt.toml: đã đọc 279/279 dòng, xét 193 dòng ứng viên rên/SFX, **sửa 32 dòng** (17 romaji họ fa/fu + 3 romaji họ ひあ + 3 romaji sai âm + 2 romaji mất phụ âm mora + 7 đếm nguyên âm + 1 độ dài ん; 18 key trùng audit chỉ khác đúng token rên, 3 dòng hoàn lại đúng VN cũ), giữ 161 dòng. Lỗi tập trung ở họ fa/fu bị audit Việt hoá ("phà"/"phùa") trước quy tắc romaji, ひあ bị đọc thành "Hya", và rên dài đếm sai nguyên âm. Mọi gasp Ư và dòng "Kh" đều giữ nguyên (file không có "Kh"). Lượt soát 2: 32/32, 0 bỏ, 0 sửa; khối TOML parse đúng, 0 sai lệch. Cờ còn lại: F1 (775 "Ư, m?"), F2 (1115 nói ngọng), F3 (1133 chờ Hieu), F4 (SFX （ ） chưa đếm), F5 (んんっ "ưmm" vs "nn"), F6 (ちゅう… đếm), F7 (っぐ đầu token), F8 ("Yaan~"), F9 (1192 tiếng reo), F10 (bẫy codepoint ふぉ/ふぅ), F11 (ふっ "phù" vs "Fu") — tất cả chờ parent / đợt thống nhất / audit, không thuộc phạm vi moan.
