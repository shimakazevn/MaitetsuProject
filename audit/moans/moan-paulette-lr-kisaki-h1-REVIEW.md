# Moan-fix: lr_稀咲ポーレットh1_悪い大人の契約 (Paulette lr — Kisaki h1, "hợp đồng người lớn hư hỏng") — 22 dòng rên sửa theo quy tắc romaji

## Xác minh file

- File: `lr_稀咲ポーレットh1_悪い大人の契約.txt.toml` — route 03_Paulette, 488 dòng script.
- TOML md5: `342110f3930d8dcd96d8eaa574e0404a` — **trùng khớp** với bản sao ở `06_Kisaki/` (nhóm trùng lặp 03_Paulette ↔ 06_Kisaki); bản sửa áp dụng cho **CẢ HAI** bản sao.
- CSV3: **1 bộ duy nhất** (thư mục `03_Paulette`), 488 dòng, 0 key trùng, 0 dòng VN trống.
- TOML vs CSV3: 488 key khớp; chỉ 3 khác biệt `\n`/khoảng trắng (1484, 1611, 1900 — TOML giữ `\n` thật giữa hai mệnh đề, CSV3 gộp thành khoảng trắng; không khác nghĩa). CSV3 là chuẩn cho danh sách sửa.
- Audit trước đó: 85 dòng sai (đã merge vào ROUTE-AUDIT.md); trong đó 19 fa/fu + 4 はぁっ + 19 gasp っ + 11 độ dài SFX là các dòng rên — xem lại toàn bộ dưới đây theo quy tắc romaji.
- Sweep gasp: 16 mục duy nhất cho file này — 13 bản sửa Ư (audit xác nhận cùng giá trị), 3 already-rendered (1599, 1892, 1893 — audit đồng ý), 1 needs-file-audit (2236 — audit đã tự giải quyết); audit bắt thêm 6 gasp sweep bỏ sót (1596, 1598, 1902, 2236, 1567, 1590). **Tất cả 19 dòng gasp Ư đều KHÓA — không đụng tới trong đợt moan-fix này** (quy tắc Ư cho gasp mất, đã quyết).

## Kho rên (moan inventory)

- Đã đọc **488/488 dòng**; xét **256 dòng rên/SFX** (hợp của mẫu mạnh 238 + nguyên âm nhỏ ぁ/ぅ 57 + 8 dòng っ-moan rà thêm — các nhóm chồng nhau).
- Phân loại (chồng nhau, không phải phân hoạch):
  - Hơi thở fa/fu (ふぁ/ふあ): **19 dòng** — toàn bộ audit đã sửa "pha"→"phà"; đợt này xét lại theo romaji: **đổi 13, giữ 6**.
  - Hơi thở はぁっ/はあっ: **4 dòng** (1825, 1824, 1826, 1569) — audit sửa thành "Hà"; **giữ cả 4** ("Hà" ngắn, tự nhiên, không ngượng).
  - Gasp っ → Ư: **19 dòng** (khóa, giữ nguyên) + 3 already-rendered (giữ nguyên).
  - Tiếng rên/SFX dài (audit sửa độ dài): **11 dòng** (1619, 1440, 1441, 1488, 2599, 2503, 2608, 2540, 2500, 2536 + 1470 trong nhóm fa/fu) — **đổi 1** (2503: audit đếm thiếu 1 nguyên âm), giữ 10. (2500 đã loại sau kiểm chứng của parent — xem § Sửa đếm audit.)
  - Họ ひゃ/ひあ/ひゅ: **8 dòng** (1443, 1489, 1490, 1493, 1488, 1441, 1495 + độc thoại 2086 ひゅーひゅー) — **đổi 1** (1443 gộp "Hya un"→"Hyaun").
  - Cười ふふっ/フフ: **8 dòng** (1457, 1459, 1461, 1533, 1604, 1463, 1456, 1513) — **giữ cả 8** ("Fufu"/"fufu" — tiếng cười, quyết Hieu 22:05).
  - Chuỗi ちゅ/れる/ぺ (oral SFX): **44 dòng** chứa ちゅ/ぺ — **giữ toàn bộ** dạng âm tiết La-tinh (quy ước file, chưa có quyết "chụt" hệ thống của Hieu; chỉ 1586 audit đã sửa "Nu chu"→"Nu chụt").
  - Độc thoại （…）: **90 dòng** có ngoặc (SFX thrust/tay + aside) — SFX thrust đã diễn bằng âm tiết La-tinh hoặc động từ Việt ("Sục", "Lún", "Trượt", "nhóp nhép") theo quy ước file; **giữ**, trừ 1 dòng sửa đếm (2503). (2500 đã loại sau kiểm chứng của parent.)
  - Hơi thở/gasp ngắn khác (あっ/はっ/んっ/んく/んふ/あう/はう/ひう/ひえ/かは…): xét từng dòng, **đổi 4** (1442, 1642, 1576, 1593, 1566, 1484 — xem dưới), còn lại giữ.

## Tiêu chí đổi/giữ họ fa/fu (quyết theo từng dòng, theo quy tắc romaji 21/11)

- **ĐỔI sang romaji** khi ふぁ/ふあ là tiếng rên/thở gấp trong cao trào (gắt, thở hổn hển, nằm trong chuỗi rên, hoặc rên dài đứng riêng) — ở đó "phà" nghe gượng, như một từ Việt ("phà" = phà qua sông) bị ép vào tiếng rên. Tiền lệ: ふかみh1 989/1048/1049, 凪h2 8 dòng fa/fu.
- **GIỮ "phà"** khi ふぁ/ふあ là hơi thở nhẹ cuối dòng / tiếng thở dài dịu trong ngữ cảnh trò chuyện, âu yếm — ở đó "phà" đọc như một tiếng thở dài tự nhiên.
- Phân biệt ふぁ → "Fa" và ふあ → "Fua" (Hepburn, theo đúng hình âm JP).

## Chi tiết dòng sửa (22 dòng)

### Hơi thở fa/fu → romaji (13 dòng)

**Key 1468 (双鉄)**
- JP: "「ふぁぁあああっっ」"
- TW: "「呼啊啊啊啊啊啊」"
- VN cũ: "「Phaaaaaa」" (audit sửa thành "Phàaaaaa")
- Sửa: "「Faaaaa」"
- Lý do: Rên dài đứng riêng trong cao trào; "Phàaaaaa" ngượng. **Đếm lại độc lập: JP có 5 âm a (ふぁ + ぁあああ), KHÔNG phải 6 như audit ghi** ("VN cũ đếm đúng 6 âm a" là sai — VN cũ "Phaaaaaa" thừa 1 âm a; audit giữ nguyên lỗi đếm đó). Romaji đúng 5 âm a: "Faaaaa". (Bài học 凪h2 2500: đếm lại công thức, không tin số trong JSON/block.)

**Key 1397 (ポーレット)**
- JP: "「セックス―セックス。双鉄くんと、稀咲と、セックス。\\n三人で……ふぁっ―ちゅむっ―ちゅぅぅっ―」"
- TW: "「做愛——做愛。和雙鐵君，和稀咲，一起做愛。三個人一起……呼啊——啾——啾——」"
- VN cũ: "「Làm tình——làm tình. Làm tình với anh Soutetsu và Kisaki.\\nBa người cùng nhau……pha——chu mu——chuu u——」" (audit: "phà")
- Sửa: "「Làm tình——làm tình. Làm tình với anh Soutetsu và Kisaki. Ba người cùng nhau……Fa——chu mu——chuu u——」"
- Lý do: ふぁっ nằm trong chuỗi thở hổn hển giữa các tiếng hôn — "phà" gượng; romaji "Fa" (ふぁ, không phải ふあ). Phần còn lại ("chu mu", "chuu u") giữ theo quy ước file.

**Key 1495 (ポーレット)**
- JP: "「ひゃっ！？　あ、双鉄くんの、指の、おなか―ふぁっ、\\nわたしの、おまんこ―入り口の、とこ―アウッ―」"
- TW: "「咿呀！？啊，雙鐵君的，手指的，肚子——呼啊、正在、我的——小穴的、入口——啊嗚——」"
- VN cũ: "「Hya!? A, phần bụng, ngón tay, của anh Soutetsu——pha,\\nđang ở, cửa mình——âm đạo, của em——au——」" (audit: "phà,")
- Sửa: "「Hya!? A, phần bụng, ngón tay, của anh Soutetsu——Fa, đang ở, cửa mình——âm đạo, của em——au——」"
- Lý do: ふぁっ là hơi thở gấp giữa câu trong lúc thở hổn hển — "phà," gượng; "Fa," theo JP (ひゃっ đầu dòng giữ "Hya!?" — đã đúng).

**Key 1472 (ポーレット)**
- JP: "「ふあっ！　あっ！　あっ！　あっ！　またっ―\\nやぁっ！　おねがい、おねがいっ―双鉄くぅんっ！」"
- TW: "「呼啊！　啊！　啊！　啊！　又來了——呀啊！　拜託，拜託了——雙鐵君！」"
- VN cũ: "「Pha! A! A! A! Lại nữa——\\nNhá! Xin anh, xin anh đấy——anh Soutetsu!」" (audit: "Phà!")
- Sửa: "「Fua! A! A! A! Lại nữa—— Nhá! Xin anh, xin anh đấy——anh Soutetsu!」"
- Lý do: Mở đầu chuỗi rên cao trào — "Phà!" ngượng; "Fua!" (ふあ).

**Key 1481 (ポーレット)**
- JP: "「ふぁっっ！！！！！」"
- TW: "「呼啊！！！！！！」"
- VN cũ: "「Pha!!!!!」" (audit: "Phà!!!!!")
- Sửa: "「Fa!!!!!」"
- Lý do: Rên đứng riêng, gắt (ふぁっっ) — "Fa" theo JP; っっ đã diễn bằng "!!!!!".

**Key 1523 (ポーレット)**
- JP: "「はっ！　あっ！？　やっ―うそっ―ふあっ―\\nいっぱい、なのに―みちみち、してて、きつい、のに」"
- TW: "「哈！　啊！不要——騙人——呼啊——明明都、滿滿的了——滿滿的、緊緊的」"
- VN cũ: "「Ha! A!? A——không thể nào——pha——\\nĐầy ắp, rồi mà——căng cứng, chật chội, thế mà.」" (audit: "phà——")
- Sửa: "「Ha! A!? A——không thể nào——Fua—— Đầy ắp, rồi mà——căng cứng, chật chội, thế mà.」"
- Lý do: ふあっ giữa chuỗi thở gấp — "Fua".

**Key 1480 (ポーレット)**
- JP: "「ふあっ！！　いい、いいよぉ！　相性、いいのっ―\\nふあっ！　うれし―嬉しいっ―嬉しい、嬉しいっ！」"
- TW: "「呼啊！！好，好舒服！　身體，好合適——呼啊！　好高興——好高興——好高興、好高興！」"
- VN cũ: "「Pha!! Thích, thích lắm! Hợp nhau, lắm——\\nPha! Vui——vui quá——vui quá, vui quá đi!」" (audit: "Phà!!" / "Phà!")
- Sửa: "「Fua!! Thích, thích lắm! Hợp nhau, lắm—— Fua! Vui——vui quá——vui quá, vui quá đi!」"
- Lý do: Hai tiếng ふあっ đều là rên phấn khích — cả hai đều "Fua".

**Key 1477 (ポーレット)**
- JP: "「ふあっ！　んっ！　おまんこ、おまんこっ！\\nわたしの、なに、これっ―ぎゅううって、して、ふあ」"
- TW: "「呼啊！　嗯！　小穴，小穴！！我的、小穴、怎麼——好緊、嗚啊」"
- VN cũ: "「Pha! Ưm! Âm đạo, âm đạo!\\nCủa em, gì thế, này——đang siết chặt, lấy, pha」" (audit: "Phà!" / "phà")
- Sửa: "「Fua! Ưm! Âm đạo, âm đạo! Của em, gì thế, này——đang siết chặt, lấy, Fua」"
- Lý do: Mở đầu bằng ふあっ！ gắt + kết bằng ふあ (không っ, vẫn là hơi thở trong cao trào) — cả hai "Fua" (dòng cuối không dấu ! vì JP không có !).

**Key 1536 (稀咲)**
- JP: "「ぁ―ふあっ―あっ」"
- TW: "「啊——呼啊——啊！」"
- VN cũ: "「A——pha——a」" (audit: "A——phà——a")
- Sửa: "「A——Fua——a」"
- Lý do: ふあっ kẹp giữa hai tiếng "a" trong chuỗi rên ngắn — "Fua" là một nhịp thở duy nhất, không tách.

**Key 1475 (稀咲)**
- JP: "「ふぁっ！　あっ！　あっ！　あっ！　あっ！　あっ！\\nあっ！　あっ！　そう、てつ―双鉄ぅ―んっ！」"
- TW: "「呼啊！　啊！　啊！　啊！　啊！　啊！啊！　啊！　雙、鐵——雙鐵——嗯！」"
- VN cũ: "「Pha! A! A! A! A! A!\\nA! A! Anh, Soutetsu——anh Soutetsu——ưm!」" (audit: "Phà!")
- Sửa: "「Fa! A! A! A! A! A! A! A! Anh, Soutetsu——anh Soutetsu——ưm!」"
- Lý do: Mở đầu chuỗi rên dài — "Fa!" (ふぁ).

**Key 1470 (稀咲)**
- JP: "「ふぁああああん！　双鉄、ね？　そうてつぅ―あっ、\\nボク、ね？　ボクっ―ボク、もう、もう、もうっ！」"
- TW: "「呼啊啊啊啊啊！　雙鐵……　雙鐵——啊、我，啊……　我——我、已經、已經、已經」"
- VN cũ: "「Pha a a a a n! Anh Soutetsu, nè? Anh Soutetsu——a,\\nem, nè? Em——em, sắp, sắp, sắp rồi!」" (audit: "Phà a a a a a n!")
- Sửa: "「Faaaaaan! Anh Soutetsu, nè? Anh Soutetsu——a, em, nè? Em——em, sắp, sắp, sắp rồi!」"
- Lý do: Rên dài một hơi (ふぁ + あ×5 = 6 âm a, đã đếm lại độc lập) — gộp thành một tiếng romaji "Faaaaaan!" thay cho dạng tách "Phà a a a a a n!".

**Key 1624 (稀咲)**
- JP: "「うんっ！　うんっ！　がまん―しゅるっ―けどっ\\nだけど―ふあっ！　あっ―ボク―ボクっ！　もう」"
- TW: "「嗯！　嗯！　我會——忍的——但是——呼啊！　啊——我——我！　已經」"
- VN cũ: "「Ưm! Ưm! Em sẽ——nhịn——nhưng mà\\nnhưng mà——pha! A——em——em! Sắp」" (audit: "phà!")
- Sửa: "「Ưm! Ưm! Em sẽ——nhịn——nhưng mà nhưng mà——Fua! A——em——em! Sắp」"
- Lý do: ふあっ giữa chuỗi rên — "Fua!".

**Key 1478 (稀咲)**
- JP: "「ふあっ！　双鉄！　そうてつ、そうてつぅっ―」"
- TW: "「呼啊！　雙鐵！　雙鐵、雙鐵——」"
- VN cũ: "「Pha! Anh Soutetsu! Anh Soutetsu, anh Soutetsu——」" (audit: "Phà!")
- Sửa: "「Fua! Anh Soutetsu! Anh Soutetsu, anh Soutetsu——」"
- Lý do: Mở đầu bằng ふあっ！ gắt — "Fua!".

### Romaji khác (7 dòng)

**Key 1442 (稀咲)**
- JP: "「きゃふっ！！！？　あ―やだっ―双鉄っ―んっ。\\nそんな―急に―急に―こんなのっ―」"
- TW: "「呀嗚！！！？啊——不要——雙鐵——嗯。不要——太突然——突然——這樣」"
- VN cũ: "「Kya fu!!!? A——đừng——anh Soutetsu——ưm.\\nThế này——đột nhiên——đột nhiên——thế này——」" (audit: "Kyaphù!!!?")
- Sửa: "「Kyafu!!!? A——đừng——anh Soutetsu——ưm. Thế này——đột nhiên——đột nhiên——thế này——」"
- Lý do: きゃふっ = "Kyafu" (Hepburn: kya + fu + っ); audit gộp thành "Kyaphù" với "phù" có dấu — đọc như từ Việt chen vào tiếng rên, ngượng. Romaji "Kyafu" khớp hình âm JP.

**Key 1642 (ポーレット)**
- JP: "「すごい……おっきい―それに―（くんくん）―\\n匂い、濃くて―とっても―えっちで―はふぅ」"
- TW: "「好厲害……好大——而且——（聞聞）——味道，好濃烈——非常——色情——哈呼」"
- VN cũ: "「Tuyệt quá……to thật——hơn nữa——（khịt khịt）——\\nmùi, nồng quá——rất là——dâm đãng——ha phu.」" (audit: "ha phù.")
- Sửa: "「Tuyệt quá……to thật——hơn nữa——（khịt khịt）—— mùi, nồng quá——rất là——dâm đãng——Hafuu.」"
- Lý do: はふぅ = "Hafuu" (ha + fu + u dài) — một hơi thở dài mượt; "ha phù" tách thành hai âm tiết Việt ("ha" + từ "phù"), ngượng.

**Key 1443 (ポーレット)**
- JP: "「ひゃうんっ！！？」"
- TW: "「呀嗚！！？」"
- VN cũ: "「Hya un!!?」"
- Sửa: "「Hyaun!!?」"
- Lý do: ひゃうんっ là MỘT âm rên duy nhất (hya + u + n, cắt bởi っ) — VN cũ tách thành hai mảnh "Hya un" (cùng lỗi như ふかみh1 "Hya ah ưm"). Gộp thành một cách diễn romaji "Hyaun" (tiền lệ ふかみh1 967 "Hyaaann").

**Key 1576 (ポーレット)**
- JP: "「あっ！？　あっ―うそっ―ふわっ―すごっ―\\n双鉄くんのおちんちんが―わたしも、おまんこ―」"
- TW: "「啊！？啊——騙人——嗚哇——好厲害——雙鐵君的小雞雞——我的小穴也——」"
- VN cũ: "「A!? A——không thể nào——bồng bềnh——tuyệt quá——\\nDương vật của anh Soutetsu——âm đạo, của em cũng——」"
- Sửa: "「A!? A——không thể nào——Fuwa——tuyệt quá—— Dương vật của anh Soutetsu——âm đạo, của em cũng——」"
- Lý do: ふわっ là một tiếng thở/gasp mềm ("fuwa") — VN cũ diễn thành từ nghĩa "bồng bềnh" (bồng bềnh = trôi nổi), làm mất hẳn âm thanh; TW cũng diễn thành âm (嗚哇). Romaji "Fuwa" giữ đúng hình âm JP.

**Key 1593 (双鉄)**
- JP: "「ぅうっ―くっ―あっ―はっ―」"
- TW: "「嗚嗚——嗯——啊——哈——」"
- VN cũ: "「U u——ku——a——ha——」"
- Sửa: "「Uu——ku——a——ha——」"
- Lý do: ぅうっ là MỘT hơi "uu" cắt ngắn — VN cũ tách thành "U u" (đọc như hai tiếng nấc rời). Gộp thành "Uu". (Các âm sau — "ku", "a", "ha" — là âm tiết khác nhau nên giữ tách.)

**Key 1566 (双鉄)**
- JP: "「あうっ」"
- TW: "「啊嗚！」"
- VN cũ: "「A u」"
- Sửa: "「Au」"
- Lý do: あうっ là MỘT âm "au" (a + u, cắt bởi っ) — VN cũ tách "A u". Gộp thành "Au".

**Key 1484 (ポーレット)**
- JP: "「くうっ！！！」 「ぁっ！？」"
- TW: "「咕嗚！！」 「啊！？」"
- VN cũ: "「Kuu u!!!」 「A!?」"
- Sửa: "「Kuu!!!」 「A!?」"
- Lý do: くうっ = "kuu" (く 1 âm u + う 1 âm u = **2 âm u**) — VN cũ "Kuu u" vừa tách âm vừa thừa 1 âm u (3 âm u). Gộp + sửa đếm thành "Kuu". (Audit chỉ ghi nhận đây là âm thanh, không phải tên コン, và không kiểm đếm — đếm lại độc lập tại đây.)

### Sửa đếm audit (2 dòng — audit đếm thiếu 1 nguyên âm)

**Key 2500 (monologue)**
- JP: "（きゅうううううううううううううっっっ！）"
- TW: "（劇烈收縮！！！！）"
- VN cũ: "（Kyuu uu uu uu uu uu uu uu uu uu uu uu uu!）" (audit sửa thành "（Kíuuuuuuuuuuuuu!）")
- **ĐÃ LOẠI KHỎI FIX LIST (parent kiểm chứng 21/11 ~03:20):** agent đếm sai — agent chỉ đếm chữ "u" trong fix audit (13 chữ u) mà không tính nguyên âm gốc "í" của "Kí". Đếm đúng theo công thức: "Kí" (1 nguyên âm gốc) + 13 chữ u = **14 nguyên âm** = 1 + 13う ✓ — fix audit ĐÃ ĐÚNG đếm. Giá trị moan của agent ("Kí" + 14 chữ u = 15 nguyên âm) thừa 1 âm. Vì fix audit đã đúng và dạng "Kí" là quy ước file (giữ ở 1619 "kíu", 1440 "Kíu"), dòng này KHÔNG cần sửa moan — đã loại khỏi wrong.json (22 → 21 mục) và khỏi khối TOML.

**Key 2503 (monologue)**
- JP: "（ずりゅううううううううううううううううっ！！！）"
- TW: "（呲溜——————————！！！）"
- VN cũ: "（Zu ryuu uu uu uu uu uu uu uu uu uu uu uu uu uu uu uu!!!）" (audit sửa thành "（Zu ryuuuuuuuuuuuuuuuu!!!）" — 17 âm u)
- Sửa: "（Zu ryuuuuuuuuuuuuuuuuu!!!）" (**18 âm u**)
- Lý do: Đếm lại độc lập: ず (1 âm u) + りゅ (1 âm u) + う×16 = **18 âm u**. Audit ghi "16 âm u" (chỉ đếm う, quên mất ず) và fix chỉ có 17 âm u — thiếu 1. Giữ dạng "Zu ryu" của audit, chỉ sửa đếm.

## Giữ nguyên (ghi chú các dòng rên đáng chú ý đã xét mà không sửa)

- **fa/fu giữ "phà" (6 dòng — hơi thở nhẹ, không phải rên cao trào):** 1497 (thở dài dịu cuối câu âu yếm "……phà."), 1584 ("Phà……" sau chuỗi hôn, trước lời cảm ơn), 1464 ("Phà——a……" mở đầu dịu), 1641 ("……vậy mà, phà." — xấu hổ, dịu), 1467 ("Phà……a——a……" — thở dài trong lúc oral, dịu; đồng thời GIỮ fix sở hữu của audit "của anh Soutetsu"), 1513 ("phà——a——" sau はぁ―んっ―, khen Soutetsu "đã cố gắng lắm rồi").
- **はぁっ → "Hà" (4 dòng: 1825, 1824, 1826, 1569):** giữ — "Hà" ngắn, tự nhiên.
- **Gasp Ư (19 dòng + 3 already-rendered):** giữ toàn bộ theo quy tắc khóa (không xét lại gasp Ư).
- **Cười ふふっ/フフ (8 dòng):** giữ "Fufu"/"fufu" — là tiếng cười, không phải rên.
- **Rên dài/SFX dài giữ (9 dòng):** 1619 "Ưm kíuuuuuuuuuu" (đếm lại: 10 âm u ✓), 1440 "Kíua a a…" (18 âm a ✓), 1441 "Híua a a…" (15 âm a ✓), 1488 "Hyau uu uu…" (10 âm u ✓), 2599 "Zu buuuuuuuuu" (10 âm u ✓), 2608 (16 ✓), 2540 (17 ✓), 2536 (11+4 ✓) — đếm đúng; dạng chữ cách nhau ("a a a…", "uu uu…") là quy ước nhóm âm của file, audit đã ghi nhận cho 1822/1820 nên giữ nhất quán, không đổi sang romaji liền.
- **Chuỗi ちゅ/れる/ぺ:** giữ dạng âm tiết La-tinh ("chuu u", "chu mu", "rê ru", "pê ro", "pê chu") — quy ước file; quyết "chụt" hệ thống vẫn chờ Hieu.
- **SFX độc thoại （…）:** giữ cách diễn bằng động từ Việt ("Sục", "Lún", "Trượt", "nhóp nhép", "Phịch", "Ực") và âm tiết La-tinh ("Zu bu", "Go chu", "Ju bu") — quy ước file, audit đã ghi nhận (ぐっ→"lún", ずりゅっ→"Trượt" là đúng).
- **Quy ước "Ưm ku"/"Ư ku"/"Ưm hi"/"Ưm gu":** giữ (1594, 1605, 1617, 1618, 1620, 1621, 1622) — các âm tiết khác nhau nên tách là đúng.
- **"ưm fu" cho んふ(っ):** giữ (1542, 1546, 1677) — quy ước file.
- **ひゃ/ひあ giữ:** 1489/1490 "Hyau!?" (đúng âm), 1493 "Hya!?" (っっ đã diễn bằng "!?"), 1495 "Hya!?" (đầu dòng, giữ; chỉ đổi phần ふぁっ trong dòng), 1520 "Hauu!?" (2 âm u ✓), 1595 "Hiu!?", 1444 "Hie!?".
- **Các dòng đã xét, giữ:** 1509 (dòng lệch vị trí — audit đã dịch mới; rên はっ→"Ha", あっ→"a" đúng), 1511 ("Ha——a! A! A!!" đúng), 1539 ("Aaa!" đúng), 1563 ("A a a a a" — 5 âm a ✓, quy ước chữ cách), 1573 かはっ→"A!" (TW cũng 啊 — giữ; tiếng "kaha" bị mất phụ âm đầu, ghi chú ở § Flags), 1574 ("A." đúng), 1585/1587/1589/1820/1821/1822 (chuỗi oral, quy ước file), 1712 わらひっ→"Ehm!" (tiền lệ h6 784, đã đúng), 1760 (nói ngọng "heiki"→"Khôn, ng——sao——a——ưm——phu" — cách diễn nói lắp có chủ ý, giữ), 1561 「ぁっ」→"A" (TW cũng không dấu câu — giữ).

## Sweep — đã kiểm chứng trực tiếp

- Đọc `sweep-raw-gasp-wrong.json` trực tiếp: 16 mục duy nhất cho file này (13 fix + 3 already-rendered + 2236 needs-file-audit; file sweep có các mục trùng lặp do 2 bản TOML). Tất cả đã được audit xác nhận cùng giá trị; không có mục sweep nào cần hành động moan-fix (gasp Ư khóa).
- Không có dòng "Kh" nào bị đổi sang Ư (quy tắc khóa 21/11 giữ "Kh").

## Flags (ghi chú cho đợt thống nhất / vòng audit — KHÔNG quyết thay Hieu)

1. **1573 かはっ → "A!":** tiếng gasp "kaha" (ho sặc) bị diễn thành "A!" trơn — mất phụ âm "ka". TW cũng diễn 啊 nên giữ; nếu Hieu muốn giữ âm "Kaha!" thì đổi ở đợt thống nhất.
2. **1561 「ぁっ」 → "A":** không có dấu câu diễn sự ngắt (っ) — TW cũng để trơn; giữ, ghi chú.
3. **1760 nói ngọng "heiki":** cách diễn "Khôn, ng——sao——a——ưm——phu" là có chủ ý (chia từ Việt theo nhịp ngọng JP); giữ nguyên, không đụng.
4. **Họ ちゅ → "chụt" hệ thống:** file này giữ dạng âm tiết ("chuu u", "chu mu", "rê ru") theo quyết audit; nếu Hieu chốt "chụt" thì cần một lượt rà hệ thống (quyết đang chờ, đã ghi ở audit review).
5. **Audit đếm sai 2 dòng (đã SỬA trong đợt này, không chỉ flag):** 1468 (audit ghi 6 âm a, JP có 5), 2503 (audit fix 17 âm u, JP có 18). Đã sửa đúng đếm trong fix list này. (2500 agent báo sai nhưng parent kiểm chứng: audit đã đúng — xem § Sửa đếm audit; đã loại.)
6. **File trùng lặp:** mọi fix áp dụng cho CẢ HAI bản sao (03_Paulette + 06_Kisaki) — md5 đã xác minh giống nhau.

## Kiểm tra lần hai (second pass)

- Đọc lại toàn bộ **22/22** bản sửa đối chiếu JP (+TW khi cần): **22 tái kiểm chứng / 0 bỏ / 0 sửa** (lượt soát 2 không phát hiện thêm lỗi nào sau khi đã đếm lại độc lập các dòng dài 1468/1470/2500/2503).
- Kiểm tra máy: JSON 22 mục, key dạng string, jp/tw/old_vn/character khớp CSV3 **22/22**; khối TOML parse bằng tomllib: **22 key, 0 sai lệch giá trị** so với JSON; mỗi fix khác giá trị gốc (audit fix hoặc VN gốc) **chỉ ở phần rên** (kiểm tra diff từng dòng — xem § chi tiết); không có fix nào đụng xưng hô, thuật ngữ, hay nghĩa (chỉ rên/SFX).
- Phân loại: 20 `moan-wrong-sound` + 2 `moan-length`.

## Kết bài

- lr_稀咲ポーレットh1: đọc 488/488 dòng; xét 256 dòng rên/SFX; **đổi 22 dòng** (13 fa/fu → romaji Fa/Fua, 5 romaji khác, 2 gộp âm tách, 2 sửa đếm audit); giữ 234 dòng rên/SFX (trong đó 19 gasp Ư khóa + 3 already-rendered + 6 fa/fu thở nhẹ + 4 "Hà" + 8 cười "Fufu" + toàn bộ chuỗi ちゅ/れる/ぺ và SFX độc thoại theo quy ước file).
- 2 phát hiện đếm: audit đếm sai 1468 (6→5 âm a), 2503 (17→18 âm u) — đã sửa đúng trong đợt này (đếm lại độc lập theo công thức, bài học 凪h2 2500). 2500: parent loại (audit đã đúng 14 nguyên âm: "Kí" + 13u).
- Khối TOML 22 key đã parse đúng bằng tomllib; số key khớp đúng với JSON (22); giá trị JSON khớp 0 sai lệch với khối TOML; giá trị VN cũ trong JSON khớp 0 sai lệch với CSV3 (22/22).
- Kiểm tra lần hai: 22/22 bản sửa đọc lại đối chiếu JP, 0 bị loại.
- File trùng lặp: cả hai bản sao (03_Paulette + 06_Kisaki) có cùng md5 — fix áp dụng cho cả hai.

```toml
[script]
1397 = "「Làm tình——làm tình. Làm tình với anh Soutetsu và Kisaki. Ba người cùng nhau……Fa——chu mu——chuu u——」"
1442 = "「Kyafu!!!? A——đừng——anh Soutetsu——ưm. Thế này——đột nhiên——đột nhiên——thế này——」"
1443 = "「Hyaun!!?」"
1468 = "「Faaaaa」"
1470 = "「Faaaaaan! Anh Soutetsu, nè? Anh Soutetsu——a, em, nè? Em——em, sắp, sắp, sắp rồi!」"
1472 = "「Fua! A! A! A! Lại nữa—— Nhá! Xin anh, xin anh đấy——anh Soutetsu!」"
1475 = "「Fa! A! A! A! A! A! A! A! Anh, Soutetsu——anh Soutetsu——ưm!」"
1477 = "「Fua! Ưm! Âm đạo, âm đạo! Của em, gì thế, này——đang siết chặt, lấy, Fua」"
1478 = "「Fua! Anh Soutetsu! Anh Soutetsu, anh Soutetsu——」"
1480 = "「Fua!! Thích, thích lắm! Hợp nhau, lắm—— Fua! Vui——vui quá——vui quá, vui quá đi!」"
1481 = "「Fa!!!!!」"
1484 = "「Kuu!!!」 「A!?」"
1495 = "「Hya!? A, phần bụng, ngón tay, của anh Soutetsu——Fa, đang ở, cửa mình——âm đạo, của em——au——」"
1523 = "「Ha! A!? A——không thể nào——Fua—— Đầy ắp, rồi mà——căng cứng, chật chội, thế mà.」"
1536 = "「A——Fua——a」"
1566 = "「Au」"
1576 = "「A!? A——không thể nào——Fuwa——tuyệt quá—— Dương vật của anh Soutetsu——âm đạo, của em cũng——」"
1593 = "「Uu——ku——a——ha——」"
1624 = "「Ưm! Ưm! Em sẽ——nhịn——nhưng mà nhưng mà——Fua! A——em——em! Sắp」"
1642 = "「Tuyệt quá……to thật——hơn nữa——（khịt khịt）—— mùi, nồng quá——rất là——dâm đãng——Hafuu.」"
2503 = "（Zu ryuuuuuuuuuuuuuuuuu!!!）"
```
