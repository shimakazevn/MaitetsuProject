# Moan-fix: ポーレットh1_ファーストセックス.txt.toml (moan-paulette-h1-fasuto-sekkusu)

- File: `ポーレットh1_ファーストセックス.txt.toml` — route 03_Paulette, 298 dòng script (monologue 190, ポーレット 74, 双鉄H 34). Cảnh H — lần đầu của Paulette và Soutetsu.
- TOML md5 `f70333e73074278312745a1870038ea3`, 1 bản duy nhất toàn dự án (không có file trùng md5). UTF-8 BOM + CRLF. `[info]` rỗng, `[selections]` rỗng, không thẻ %l, không [ruby]. Nhân vật: Paulette, Soutetsu H.
- CSV3: 1 bộ duy nhất (`translation_toml\\03_Paulette`), 298 dòng, 0 khóa trùng, 0 VN trống. TOML `[script]` 298 khóa khớp CSV3 298/298; giá trị VN khớp phẳng 142/298 (156 lệch còn lại toàn là chuẩn hoá `\n` literal ↔ khoảng trắng — TOML-2 làm phẳng `\n`; CSV3 là chuẩn cho fix).
- Audit trước đó: 51 sai (17,1%) — đã gộp vào ROUTE-AUDIT.md. File này KHÔNG có dòng "Kh" nào.

## 1. Kiểm chứng file

- Đã đọc 298/298 dòng (CSV3 + TOML-2).
- Sweep gasp: 6 mục cho file này (kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`, đã đối chiếu từng mục với quy tắc loại trừ của nó): 983 「っ！」→ audit 「Ư!」 ✓ (gasp cả dòng, VN chỉ còn dấu câu); 984 「～っ！」→ audit 「~Ư!」 ✓ (っ thô còn sót trong VN); 988 「っ！」→ audit 「Ư!」 ✓; 995 「っ！！！」→ audit 「Ư!!!」 ✓; 1007 「っ！」→ audit 「Ư!」 ✓; 1015 đuôi ん～っ → audit 「...ưm~Ư」 ✓ (gasp cuối sau ～). Cả 6 đều đã áp nguyên qua audit; KHÔNG dòng gasp Ư nào bị đụng trong đợt moan này; không dòng "Kh" nào bị đổi.
- Đếm nguyên âm của audit đã kiểm chứng lại độc lập bằng máy (đếm ký tự JP): không có dòng đếm nào của audit cần sửa (audit không sửa đếm rên trong file này).

## 2. Kiểm kê rên/SFX

- Đã xét 92 dòng rên/SFX: 56 thoại rên (ポーレット + 双鉄H) + 31 SFX trong ngoặc （ ） độc thoại + 3 trần thuật tiếng thở (1395, 1561, 1562) + 2 SFX trong thoại (926 くぱくぱ, 950 ぐちゅぐちゅ).
- Đổi 16 dòng: 13 romaji + 1 đếm nguyên âm (1006) + 2 sai âm (1042, 1758).
- Giữ 76 dòng rên/SFX (xem §4).
- Nhóm lỗi chính:
  - Họ fa/fu bị Việt hoá "phá"/"phà" — 3 dòng (976 ふああっ, 987 ふぁっ, 1065 ふぁっ): audit đã sửa thành "phà" theo quy tắc cũ; đợt moan đưa về romaji theo quy tắc fallback 21/11 + tiền lệ đã merge (h7 796/812 ふぁっ→"Fa"; ふかみh1 1048 ふあぁ→"Fuaa").
  - Họ ひゃ/きゃ diễn thành "Á" (mất phụ âm hy-/ky-) — 4 dòng (977, 981, 982, 989): theo quy tắc 3b quyết 21/11 ~11:55.
  - Âm rên mất phụ âm/glide hoặc sai âm — 6 dòng (978 いっ→"A" + thiếu 2 u; 979 mất hẳn ふう; 985 かっ→"Hà"; 996 あんっ mất ん; 1019 mất ぞおおおお; 1042 ああ→"Ừm").
  - Đếm nguyên âm — 1 dòng (1006: JP 13 âm a, VN cũ 12).
  - Rên bị diễn sai loại âm — 2 dòng (1106 んきゅっ mất きゅ; 1758 ぐううっ diễn thành tiếng đâm "Phập phập").
- 4/16 key trùng audit (976, 987, 1065, 1106) — fix moan thay thế fix audit ở đúng token rên; các phần khác của fix audit được giữ nguyên (xem §3, đã kiểm chứng diff bằng máy).

## 3. Chi tiết từng bản sửa (16 dòng)

Quy ước áp dụng: mỗi fix là MỘT giá trị duy nhất cho key đó. Với 4 key trùng audit, fix = giá trị audit + chỉ đổi token rên; với 12 key còn lại, fix = giá trị VN cũ + chỉ đổi token rên.

### 3a. Họ fa/fu → romaji (3 dòng)

**976** — ポーレット (trùng audit)
- JP: 「ひゃっ――あっ――子宮っ――子宮、に――キスっ――ふああっ！！！」
- TW: 「呀——啊——子宮——子宮——被親到了——哇啊！！！」
- VN cũ: 「Hya——á——tử cung——vào, tử cung——bị hôn——\nphá!!!」
- VN mới: 「Hya——á——tử cung——vào, tử cung——bị hôn——\nFuaa!!!」
- Lý do: ふああっ = fu-a-a → "Fuaa" (tiền lệ ふかみh1 1048 ふあぁ→"Fuaa"). "phá" sai theo quy tắc khóa (không bao giờ "phá"); "phà" của audit ngắn quá so với tiếng hét dài ふああっ. Chỉ đổi token này so với fix audit.

**987** — ポーレット (trùng audit)
- JP: 「ふぁっ」
- TW: 「呼」
- VN cũ: 「Phá.」
- VN mới: 「Fa.」
- Lý do: ふぁっ → "Fa" (Hepburn chặt; tiền lệ đã merge h7 796 ふぁっ→"Fa", audit "Phà" ngượng → romaji). Không thêm Ư (っ là ngắt của chính âm fa).

**1065** — ポーレット (trùng audit)
- JP: 「あつ、いっ――んっ――すごい……いっぱい……ふぁっ――しきゅ、うっ――んっ――おま、ん、こ」
- TW: 「好燙——嗯——好厲害……這麼多…………呼——在子宮裡——在小穴裡」
- VN cũ: 「Nóng, quá——ưm——tuyệt quá... nhiều... thật...\nphá——tử cung, ưm——âm đạo, ngập tràn rồi.」
- VN mới: 「Nóng, quá——ưm——tuyệt quá... nhiều... thật...\nFa——tử cung, ư——âm đạo.」
- Lý do: ふぁっ → "Fa" (như 987); うっ trần → "ư" (tiền lệ ふかみh1 1046 ふ……うっ → "phù……ư" — うっ trần diễn là "ư", "ưm" thừa m). Giữ んっ→"ưm" đầu dòng. Chỉ đổi 2 token rên so với fix audit (fix audit đã bỏ "ngập tràn rồi" — giữ nguyên phần đó).

### 3b. Họ ひゃ/きゃ → romaji, quy tắc 3b (4 dòng)

**977** — ポーレット
- JP: 「きゃっ」
- TW: 「呀」
- VN cũ: 「Á.」
- VN mới: 「Kya.」
- Lý do: きゃ → "Kya" (quy tắc 3b — "Á" mất phụ âm ky-).

**981** — ポーレット
- JP: 「きゃうっ！　ひゃっ――あっ――」
- TW: 「呀！呀——啊——」
- VN cũ: 「Á! Hya——a——」
- VN mới: 「Kyau! Hya——a——」
- Lý do: きゃうっ = kya-u + ngắt → "Kyau!" (quy tắc 3b). Giữ "Hya" và "a" đã đúng.

**982** — ポーレット
- JP: 「きゃっ！？」
- TW: 「呀！？」
- VN cũ: 「Á!?」
- VN mới: 「Kya!?」
- Lý do: きゃ → "Kya" (quy tắc 3b).

**989** — ポーレット
- JP: 「きゃふっ――ひゃっ――押され、てっ――んうっっ」
- TW: 「哇——呀——被頂到了——嗯」
- VN cũ: 「Á——hya——bị ấn, vào——ưm.」
- VN mới: 「Kyafu——hya——bị ấn, vào——ưm.」
- Lý do: きゃふっ = kya-fu + ngắt → "Kyafu" (tiền lệ h7 1442 きゃふ→"Kyafu"). Giữ "hya" thường giữa dòng và "ưm" cho んうっっ.

### 3c. Âm rên mất phụ âm/glide hoặc sai âm (6 dòng)

**978** — ポーレット
- JP: 「いっ――ひゅううううううううううううううっっ！！！」
- TW: 「呀啊啊啊啊啊！！！
- VN cũ: 「A——hyuuuuuuuuuuuuu!!!」
- VN mới: 「I——Hyuuuuuuuuuuuuuuu!!!」
- Lý do: いっ → "I" (い ≠ あ — VN cũ "A" sai âm); ひゅ + う×14 → "Hy" + 15 u (công thức 1+14; VN cũ chỉ có 13 u, thiếu 2). Đếm bằng máy: JP 14 う, fix 15 u ✓.

**979** — ポーレット
- JP: 「きゃふうううううううっっっ！！！」
- TW: 「呀啊啊啊！！！」
- VN cũ: 「Kyaaaaaaa!!!」
- VN mới: 「Kyafuuuuuuuu!!!」
- Lý do: きゃふう… = Kya + fu + う×7 → "Kyafuuuuuuuu" (8 u sau f, công thức 1+7). VN cũ mất hẳn âm ふう và kéo sai きゃ thành 7 a (きゃ chỉ có 1 a).

**985** — ポーレット
- JP: 「かっ――はっ――あっ――ふ、深い……ぃっ」
- TW: 「呼——啊——呼——好深啊……」
- VN cũ: 「Hà——hà——a——s, sâu quá... anh.」
- VN mới: 「Ka——hà——a——s, sâu quá... anh.」
- Lý do: かっ trong chuỗi thở gấp → "Ka" (tiền lệ đã merge 凪h2 2520 かっ――はっ！→"Ka——Hà!"; VN cũ "Hà" sai phụ âm k→h). Đây là hơi thở, không phải mảnh câu nói ngắt quãng (tiền lệ h3 1018 giữ "Hà" chỉ áp khi かっ là mảnh từ bị ngắt — ở đây không có từ nào bắt đầu bằng か). Giữ "hà"/"a" đã đúng. (ぃっ cuối dòng xem cờ F3.)

**996** — ポーレット
- JP: 「あんっ――」
- TW: 「啊——」
- VN cũ: 「A——」
- VN mới: 「An——」
- Lý do: あんっ = a-n + ngắt → "An" (tiền lệ lr-ふかみh1 1267 あんっ→"an"). VN cũ mất ん.

**1019** — ポーレット
- JP: 「んっ――ふっ――んっ――れろっ――れるっ――\nんっ――ちゅっ――ちゅるるっ――ちゅぞおおおおっ」
- TW: 「嗯——呼——嗯——啾嚕——啾嚕——嗯——啾——啾嚕嚕——啾嚕嚕」
- VN cũ: 「Ưm——phù——ưm——liếm——liếm——\nưm——chụt——chùn chụt——chuút.」
- VN mới: 「Ưm——phù——ưm——liếm——liếm——\nưm——chụt——chùn chụt——chuzooooo.」
- Lý do: ちゅぞおおおおっ = chu-zo + お×4 → "chuzooooo" (5 o). VN cũ "chuút" chỉ diễn ちゅ + ngắt, mất hẳn ぞおおおお. Chữ thường giữa dòng theo lệ romaji sau —— (như 978 "hyu").

**1042** — 双鉄H
- JP: 「ああ！」
- TW: 「嗯！」
- VN cũ: 「Ừm!」
- VN mới: 「Aa!」
- Lý do: ああ = "Aa" (2 a) — VN cũ "Ừm" là âm ん, sai hẳn âm (tiền lệ h1-chigiri 1263/1264 ああ→"Aa").

### 3d. Đếm nguyên âm (1 dòng)

**1006** — ポーレット
- JP: 「ぁぁあああああああああああっっっ！！！」
- TW: 「啊啊啊啊啊！！！」
- VN cũ: 「Aaaaaaaaaaaa!!!」
- VN mới: 「Aaaaaaaaaaaaa!!!」
- Lý do: JP có 13 âm a (ぁ×2 + あ×11), VN cũ chỉ có 12 — thêm 1 a. Đếm bằng máy ✓.

### 3e. Rên bị diễn sai loại âm (2 dòng)

**1106** — ポーレット (trùng audit)
- JP: 「だからッ――ん、動い、て……あ……\n双鉄、くん、を――わたし、の――なか――んきゅっ！」
- TW: 「所以——嗯——動起來吧——啊……雙鐵君——在我裡面——嗯！」
- VN cũ: 「Nên là——ưm, hãy di, chuyển... a...\nSoutetsu, này——bên trong, em——ưm, đi anh!」
- VN mới: 「Nên là——ưm, hãy di, chuyển... a...\nanh Soutetsu, này——bên trong, em——ưm kyu!」
- Lý do: んきゅっ = ん + きゅ + ngắt → "ưm kyu" (tiền lệ đã merge h1-chigiri: ん+X → "Ưm + X", vd 1282 んきゅうううう→"Ưm kyuuuuu"). Fix audit "ưm!" mất hẳn きゅ; "đi anh!" của VN cũ là bịa (không có trong JP). Chỉ đổi token cuối so với fix audit.

**1758** — monologue (SFX trong ngoặc)
- JP: 「（ごりっ！　ぐっ！　ぐううっ！　ぐみゅっ！）」
- TW: 「（用力挺動）」
- VN cũ: 「（Phập! Hự! Phập phập! Phập!）」
- VN mới: 「（Phập! Hự! Hựựự! Phập!）」
- Lý do: ぐううっ là tiếng rên/gầm dài (gu + う×2 → 3 ự, công thức 1+2) — VN cũ "Phập phập!" diễn thành tiếng đâm, sai loại âm. Trong cùng chuỗi, ぐっ đã được diễn là "Hự" nên ぐううっ phải cùng họ gầm: "Hựựự". Giữ ごりっ→"Phập", ぐみゅっ→"Phập".

## 4. Các dòng rên đã giữ (đáng chú ý)

- 980 ひゃうっ→"Hyau!" ✓ (romaji đã đúng); 993 ぅ→"Ư", あっ→"a" ✓; 997/998 chuỗi あっ → "a" ✓; 1004 ああ→"À" (công thức 1+0=1 ✓).
- 1002/1017/1026/1041: んっ→"ưm", ふっ→"phù", んふっ→"ưm phù" ✓; 1027 くっ→"hự", 994 っく→"Hự!" ✓; 1045 むっ→"Hử!?" (tiếng ậm ừ hỏi, TW 嗯 — giữ).
- 1010/1012/1016/1017 chuỗi liếm đã Việt hoá (chụt/chùn chụt/liếm/ực) ✓; 1015 giữ Ư gasp của audit.
- 1022/1186 くぅん sau tên "Soutetsu": GIỮ tên theo tiền lệ đã merge h3 (946/1069 くぅん là kéo dài của くん, không phải rên — giữ "anh Soutetsu", không thêm rên); audit đã sửa 2 dòng này thành "anh Soutetsu" (đại từ).
- 986 よぉ→"anh": tiểu từ cuối câu kéo dài, không phải rên — giữ (audit scope nếu có gì).
- 1171 ぺろっ→"liếm" ✓; 926 くぱくぱ→"mấp máy, co giật" ✓; 950 ぐちゅぐちゅ→"nhóp nhép" ✓.
- SFX （ ）: giữ 30/31 (chỉ đổi 1758) — 1756 きゅううううう→"Siết chặt!" (SFX nghĩa hành động), 1737 びゅうう→"phụttttt" (đã kéo dài), 1774 ずるうううううううう→"Rút ra——đâm vào" (SFX nghĩa), 1739 びゅくっ→"Giật nảy" (SFX nghĩa).
- 1081 う→"Ư", んっ→"ưm" ✓; 1099/1109/1144/1157/1167/1181/1183 んっ→"ưm", あっ→"á" ✓; 1020 ん――ぁっ→"Ưm——a." ✓.

## 5. Cờ (cho vòng audit / đợt thống nhất — KHÔNG sửa ở đây)

- **F1 — 1005** (audit loop): JP 「っ――」 độc lập, VN cũ 「A——」 — gasp diễn sai nguyên âm ("A" không có trong JP); cần Ư theo quy tắc gasp. Sweep + audit đều bỏ sót dòng này.
- **F2 — 1184** (audit loop): JP 「双鉄くんっ――っ――あっ――…」 — っ―― giữa bị mất hẳn trong VN (audit chỉ sửa đại từ); cần Ư.
- **F3 — 985** (audit loop): JP 「深い……ぃっ」 cuối — ぃっ bị mất (VN "...anh."); cần Ư (っ trên từ âm thanh).
- **F4 — 1022/1186** (đợt thống nhất): くぅん theo tiền lệ h3 là kéo dài của くん — giữ tên; nếu đợt thống nhất muốn diễn cả tiếng kéo dài thì đổi thành "anh Soutetsuuun".
- **F5 — 976/1065** (đợt thống nhất): phần nghĩa audit đã sửa ("tử cung——vào, tử cung——bị hôn" ở 976; bỏ "ngập tràn rồi" ở 1065) — moan chỉ đổi token rên; fix moan thay thế fix audit ở đúng token rên (đã kiểm chứng diff bằng máy).
- **F6 — 1057** (audit scope): をっ cuối dòng là tiểu từ + っ nhấn mạnh, không phải từ âm thanh → không phải gasp; audit không sửa — ghi lại, không sửa ở đây.
- **F7 — 1106** (ghi nhận): audit "ưm!" → moan "ưm kyu!" theo tiền lệ h1-chigiri (ん+X → "Ưm + X").

## 6. Lượt soát 2 + kiểm chứng máy

- Lượt soát 2: tổng 16 / tái kiểm chứng 16 / bỏ 0 / sửa 0 (đọc lại từng fix đối chiếu JP sau khi dựng xong; không fix nào phải sửa lại).
- JSON 16 mục dạng chuẩn (list of dicts, khóa string: key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 16/16. Mọi fix đều khác old_vn.
- Đếm nguyên âm kiểm chứng bằng máy: 978 = 15 u (JP ひゅ + 14 う) ✓; 979 = 8 u (ふ + 7 う) ✓; 1006 = 13 a (ぁ×2 + あ×11) ✓; 1019 = 5 o (ぞ + 4 お) ✓; 1758 = 3 ự (ぐ + 2 う) ✓.
- Khối TOML parse bằng tomllib: 16 khóa, 0 sai lệch giá trị so với JSON.
- 4 key trùng audit (976, 987, 1065, 1106): fix moan khác fix audit CHỈ ở token rên (đã kiểm chứng bằng diff cơ học).
- Không dòng gasp Ư nào bị đụng (983, 984, 988, 995, 1007, 1015 không có trong JSON); không dòng "Kh" nào bị đổi (file không có dòng "Kh").

## 7. Khối TOML (đã kiểm chứng parse)

```toml
[script]
976 = "「Hya——á——tử cung——vào, tử cung——bị hôn——\\nFuaa!!!」"
977 = "「Kya.」"
978 = "「I——Hyuuuuuuuuuuuuuuu!!!」"
979 = "「Kyafuuuuuuuu!!!」"
981 = "「Kyau! Hya——a——」"
982 = "「Kya!?」"
985 = "「Ka——hà——a——s, sâu quá... anh.」"
987 = "「Fa.」"
989 = "「Kyafu——hya——bị ấn, vào——ưm.」"
996 = "「An——」"
1006 = "「Aaaaaaaaaaaaa!!!」"
1019 = "「Ưm——phù——ưm——liếm——liếm——\\nưm——chụt——chùn chụt——chuzooooo.」"
1042 = "「Aa!」"
1065 = "「Nóng, quá——ưm——tuyệt quá... nhiều... thật...\\nFa——tử cung, ư——âm đạo.」"
1106 = "「Nên là——ưm, hãy di, chuyển... a...\\nanh Soutetsu, này——bên trong, em——ưm kyu!」"
1758 = "（Phập! Hự! Hựựự! Phập!）"
```

## Kết bài

File ポーレットh1_ファーストセックス.txt.toml: đã đọc 298/298 dòng, xét 92 dòng rên/SFX, **đổi 16 dòng (13 romaji + 1 đếm nguyên âm + 2 sai âm)** — 3 dòng fa/fu về romaji (976 Fuaa, 987 Fa, 1065 Fa), 4 dòng họ ひゃ/きゃ về romaji theo quy tắc 3b (977 Kya, 981 Kyau, 982 Kya, 989 Kyafu), 6 dòng mất phụ âm/glide hoặc sai âm (978, 979, 985, 996, 1019, 1042), 1 dòng đếm nguyên âm (1006: 13 a), 2 dòng sai loại âm (1106 ưm kyu, 1758 Hựựự). 4 key trùng audit chỉ khác fix audit ở đúng token rên. Không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào. Lượt soát 2: 16/16, 0 bỏ, 0 sửa. JSON + khối TOML đã kiểm chứng parse, 0 sai lệch. Cờ cho vòng audit: 3 gasp bị bỏ sót (1005, 1184, 985 ぃっ); cờ cho đợt thống nhất: くぅん sau tên (1022/1186), phần nghĩa audit ở 976/1065, 1057 をっ.
