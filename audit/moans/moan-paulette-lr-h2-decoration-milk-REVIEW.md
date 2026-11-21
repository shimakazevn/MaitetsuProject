# Moan-fix: lr_ポーレットh2_デコレーション＆ミルク (Decoration & Sữa) — 10 dòng rên sửa theo quy tắc romaji

## 1. Xác minh file

- File: `lr_ポーレットh2_デコレーション＆ミルク.txt.toml` — route 03_Paulette, 333 dòng script, section `script` duy nhất.
- TOML: `sources/toml2/translation_toml/03_Paulette/lr_#U30dd#U30fc#U30ec#U30c3#U30c8h2_#U30c7#U30b3#U30ec#U30fc#U30b7#U30e7#U30f3#Uff06#U30df#U30eb#U30af.txt.toml`, md5 `961d4a125957dfe488e38eed086c6200` (khớp md5 audit đã ghi), không có bản trùng trong 227 file TOML — bản sửa áp dụng cho 1 file duy nhất.
- CSV3: 1 bộ duy nhất, 333 dòng, 0 key trùng, 0 dòng VN trống; File `translation_toml\\03_Paulette\\lr_ポーレットh2_デコレーション＆ミルク.txt.toml`. TOML vs CSV3: khớp toàn bộ (audit đã xác minh 0 khác biệt thực chất).
- Audit trước đó: 69 dòng sai (đã merge vào ROUTE-AUDIT.md); trong đó 37 hơi thở/âm thanh thoại + 2 âm thanh độc thoại là các dòng rên — xem lại toàn bộ dưới đây theo quy tắc romaji. Các bản sửa moan dưới đây được xét trên bản VN **sau audit** (fix audit + sửa moan gộp lại), còn `old_vn` trong JSON là VN hiện tại trong CSV3/TOML — theo đúng quy ước moan-fukamih1 key 1058 / moan-paulette-h8. Khác biệt duy nhất giữa bản sửa moan và fix audit là: fix audit viết một dòng (khoảng trắng thay cho ngắt dòng), còn bản sửa moan giữ nguyên `\n` của VN cũ — để mỗi bản sửa chỉ khác VN cũ đúng ở phần rên nhắm tới.
- Cơ sở tổng moan trước file này (đã tự kiểm chứng lại trong `moans/ROUTE-MOANS.md`): **8 file / 205 dòng**.

## 2. Kiểm kê dòng rên

- Đã đọc **333/333 dòng** (CSV3 + đối chiếu TOML). Xét **281 dòng ứng viên rên/thở/gasp/SFX** theo mẫu (âm rên/thở/gasp/SFX trong JP hoặc cách diễn rên trong VN). **Sửa 10 dòng, giữ 271 dòng.**
- Phân loại:
  - Hơi thở fa/fu (ふぁ/ふあ/ふぁん + họ ふ): **18 dòng** — audit đã Việt hoá "pha"→"phà"/"phàn"/"phù"; đợt này xét lại theo romaji: **đổi 8** (1022, 1024, 1025, 1032, 1039, 1084, 1095, 1099), **giữ 9** (1043, 1053, 1072, 1074, 1079, 1127, 1167, 1315, 1735); 1009 đổi riêng sang "Kyufu" (xem §4b).
  - きゅふっ: **1 dòng** (1009) — đổi sang romaji "Kyufu" (tiền lệ 凪h2 2401: きゅふっ → "Kyufu"; h8 2142: "Kíu"→"Kyu").
  - Họ ひあ/ひゃ/ひゅ: **4 dòng** (1011, 1015, 1210, 1025) — **giữ cả 4** ("Hia"/"Hya" đã là romaji đúng; 1025 "Khíu" giữ — xem §5).
  - Cười ふふ/うふふ/えへへ/あはは: **9 dòng** (1018, 1043, 1059, 1060, 1075, 1087, 1194, 1227, 1321) — **giữ cả 9** ("Fufu"/"Ufufu"/"Ehehe"/"Ahaha" — tiếng cười, quyết Hieu 22:05).
  - Gasp っ → Ư: **13 mục sweep đã kiểm chứng trực tiếp** trong `sweep-raw-gasp-wrong.json` (1044, 1062, 1063, 1064, 1065, 1068, 1070, 1124, 1236, 1558, 1597 + 1009/1028) — **tất cả KHÓA, không đụng tới** (quy tắc Ư cho gasp mất). Không có dòng "Kh" nào bị đổi sang Ư.
  - Chuỗi SFX ちゅ/れる/ぺ (oral): **audit đã Việt hoá** thành "chụt"/"rộp"/"liếm nhẹ" v.v. — **giữ toàn bộ**, chỉ kiểm chứng lại số nguyên âm bằng máy: 1010 (18 u ✓), 1037 (9 ụ ✓), 1105 (5 ộ ✓), 1107 (2 ộ ✓), 1108 (3 ụ ✓), 1148 (3 ụ ✓), 1255 (19 ộ ✓), 1315 (2 ộ ✓), 1317 (2 ụ + 2 ậ ✓), 1319 (2 ụ + 3 ụ ✓), 1020 (2 ụ ✓), 1085 (3 ậ ✓), 1024 (3 à ✓). Không phát hiện lỗi đếm nào của audit trong nhóm này.
  - SFX độc thoại （…）: **giữ toàn bộ** cách diễn bằng động từ Việt ("Sục", "Lún", "Trượt", "nhóp nhép", "Phụt", "Co thắt dữ dội") theo quy ước file, audit đã ghi nhận.
  - Rên dài khác: **đổi 1** (1007: đếm lại độc lập — VN cũ thừa 1 âm a; audit đã giữ "Kyaaan" là "nằm trong khoảng chấp nhận được" nhưng đếm theo công thức thì thừa — xem §3), còn lại giữ (1036 "Hauu" 2 u ✓, 1131 "Ưm uu u" 3 u ✓, 1770 12 u ✓).

## 3. Tiêu chí đổi/giữ họ fa/fu (quyết theo từng dòng, theo quy tắc romaji 21/11 + tiền lệ lr_稀咲h1)

- **ĐỔI sang romaji** khi ふぁ/ふあ là tiếng rên/thở gấp trong cao trào (gắt, thở hổn hển, nằm trong chuỗi rên) — ở đó "phà" nghe gượng, như một từ Việt ("phà" = phà qua sông) bị ép vào tiếng rên. Tiền lệ: lr_稀咲h1 13 dòng, ふかみh1 989/1048/1049, 凪h2 8 dòng fa/fu.
- **GIỮ "phà"/"phù"** khi ふぁ/ふあ là hơi thở nhẹ cuối dòng / tiếng thở dài dịu trong ngữ cảnh trò chuyện, âu yếm — ở đó "phà" đọc như một tiếng thở dài tự nhiên.
- Phân biệt ふぁ → "Fa" và ふあ → "Fua" (Hepburn, theo đúng hình âm JP). ふぁんっ → "Fan".

## 4. Chi tiết dòng sửa (10 dòng)

### 4a. Romaji — họ fa/fu (8 dòng)

**Key 1022 (ポーレット)**
- JP: `「ふあっ――は――ァ――あっ――ゆっくり、も――\nすき――んっ――きもち、いいとこ――じっくり――ぁ」`
- TW: `「呼啊——哈——啊——啊——慢慢來——也好喜歡——嗯——舒服的，地方——仔細按摩——啊」`
- VN cũ: `「Pha——ha——a——a——chậm rãi, thế này——\nem cũng thích——ưm——chỗ, sướng ấy——cứ từ từ——a」` (audit: "Phà")
- Sửa: `「Fua——ha——a——a——chậm rãi, thế này——\nem cũng thích——ưm——chỗ, sướng ấy——cứ từ từ——a」`
- Lý do: ふあっ mở đầu chuỗi rên thở hổn hển trong cao trào — "Phà" gượng; "Fua" (ふあ).

**Key 1024 (ポーレット)**
- JP: `「ふあっ！　あっ！　あっ！　あっ！　ちょっ！　んあ！\nまっ――あっ――んぁっ！　ふぁああっっ！！！」`
- TW: `「呼啊！啊！啊！啊！等！嗯啊！一下——啊－嗯啊！呼啊啊啊！！！」`
- VN cũ: `「Pha! A! A! A! Khoan! Ưm a!\nKhoan đã——a——ưm a! Phaaaa!!!」` (audit: "Phà! … Phààà!!!")
- Sửa: `「Fua! A! A! A! Khoan! Ưm a!\nKhoan đã——a——ưm a! Faaa!!!」`
- Lý do: Hai tiếng ふあっ và ふぁああ đều trong chuỗi rên gắt — "Phà!"/"Phààà" gượng; "Fua!" (ふあ) và "Faaa" (ふぁああ = 3 âm a: ぁ+あ×2, đúng số audit đã đếm). Dấu っっ cuối dòng giữ nguyên "!!!" theo fix audit đã merge (cùng câu hỏi như 1093 — xem §6 Flags, không tự quyết ở đây).

**Key 1025 (ポーレット)**
- JP: `「くひゅっ！　んっ――ぁ――ふぁ――あっ――あ……\nぁっ――太い、とこ――ぞりって――すき――んっ――」`
- TW: `「咕呀！嗯——啊——呼啊——啊——啊……啊——粗的地方——刮到的感覺——好棒——嗯——」`
- VN cũ: `「Ku hyu! Ưm——a——pha——a——a……\nA——chỗ, to ấy——cọ vào——thích quá——ưm——」` (audit: "Khíu! … phà")
- Sửa: `「Khíu! Ưm——a——Fa——a——a……\nA——chỗ, to ấy——cọ vào——thích quá——ưm——」`
- Lý do: ふぁ kẹp giữa hai tiếng "a" trong chuỗi rên ngắn — "phà" gượng; "Fa" (ふぁ, không phải ふあ). "Khíu" cho くひゅっ giữ nguyên theo fix audit (tiếng gasp ngắn, tự nhiên, không ngượng).

**Key 1032 (ポーレット)**
- JP: `「はうううっ――ふあっ――あっ――\nおっぱい――ちくび――きもちいい――よぉ」`
- TW: `「哈唔唔唔——呼啊——啊——乳房——乳頭——好舒服——啊」`
- VN cũ: `「Hau uu——pha——a——\nngực——nhũ hoa——sướng quá——a」` (audit: "phà")
- Sửa: `「Hau uu——Fua——a——\nngực——nhũ hoa——sướng quá——a」`
- Lý do: ふあっ giữa chuỗi rên — "Fua". "Hau uu" giữ nguyên (はうううっ = 3 tiếng u ✓).

**Key 1039 (ポーレット)**
- JP: `「はっ！　ぁっ――ぁっ――ぁっ――わた、しっ――\nこれっ――ふぁ――もうっ、もうっ、もうっ、もうっ！」`
- TW: `「哈！啊——啊——啊——我——這樣——呼啊——已經，已經，已經，已經！」`
- VN cũ: `「Ha! A——a——a——em——\nthế này——pha——ra mất, ra mất, ra mất, ra mất!」` (audit: "phà")
- Sửa: `「Ha! A——a——a——em——\nthế này——Fa——ra mất, ra mất, ra mất, ra mất!」`
- Lý do: ふぁ trong chuỗi rên cao trào ("ra mất" ×4) — "phà" gượng; "Fa" (ふぁ — CHÚ Ý: đây là ふぁ, không phải ふあ, nên là "Fa" chứ không phải "Fua").

**Key 1084 (ポーレット)**
- JP: `「はっ――あうっ――ふぁんっ――んっ――くぅんっ――\nん。これ――ゆっくり――はっ――ゆっくぃ、らのにぃ」`
- TW: `「啊——啊唔——呼啊——嗯——咕嗯——嗯。這樣——慢慢擺動——哈——明明動作那麼慢」`
- VN cũ: `「Ha——au——pha——ưm——kuuun——\nƯm. Thế này——chậm rãi——ha——chậm rãi, thế mà」` (audit: "phàn")
- Sửa: `「Ha——au——Fan——ưm——kuuun——\nƯm. Thế này——chậm rãi——ha——chậm rãi, thế mà」`
- Lý do: ふぁんっ trong chuỗi thở gấp — "phàn" gượng (đọc như từ Việt "phàn nàn"); "Fan" (ふぁん). "kuuun" cho くぅんっ giữ nguyên theo quyết Hieu 22:19 (giữ "Kuuun").

**Key 1095 (ポーレット)**
- JP: `「ぁ！　んっ！　ふあっ！　あっ！　あっ！　ああっ！\nわたしっ！　でてるっ！　わたし！　おっぱいっ！！」`
- TW: `「啊！嗯！呼啊！啊！啊！啊啊！我！流出來了！我的！乳房！！」`
- VN cũ: `「A! Ưm! Pha! A! A! Aa!\nEm! Ra rồi! Ngực em! Ra sữa rồi!!」` (audit: "Phà!")
- Sửa: `「A! Ưm! Fua! A! A! Aa!\nEm! Ra rồi! Ngực em! Ra sữa rồi!!」`
- Lý do: ふあっ mở đầu chuỗi rên cao trào ("Ra rồi!") — "Phà!" gượng; "Fua!" (ふあ).

**Key 1099 (ポーレット)**
- JP: `「あっ！？　ぁ――ぁ――ぁっ――ふあっ――これっ――\nこれっ――えっ――やらっ――これっ――しゅきっ――」`
- TW: `「啊！？啊——啊——啊——呼啊——這個——這樣——哎——討厭——這樣——好棒——」`
- VN cũ: `「A!? A——a——a——pha——thế này——\nthế này——ế——ưm——thế này——thích quá——」` (audit: "phà")
- Sửa: `「A!? A——a——a——Fua——thế này——\nthế này——ế——ưm——thế này——thích quá——」`
- Lý do: ふあっ giữa chuỗi rên — "Fua".

### 4b. Romaji — きゅふっ (1 dòng)

**Key 1009 (ポーレット)**
- JP: `「きゅふっ！？　んっ！　ちょっ！\nおちつ――あっ――おちついて――そうてつく――っ！」`
- TW: `「呀呼！？嗯！等等！冷——啊——冷靜一點——雙鐵——！」`
- VN cũ: `「Kyu fu!? Ưm! Khoan đã!\nBình tĩnh——a——bình tĩnh lại đi——anh Soutetsu——!」` (audit: "Kíuphù!? … ——Ư!")
- Sửa: `「Kyufu!? Ưm! Khoan đã!\nBình tĩnh——a——bình tĩnh lại đi——anh Soutetsu——Ư!」`
- Lý do: きゅふっ là MỘT âm duy nhất — audit tách thành "Kíuphù" (hai mảnh Việt rời) nghe gượng; romaji "Kyufu" giữ đúng hình âm JP. Tiền lệ: 凪h2 2401 (きゅふっ → "Kyufu"), h8 2142 ("Kíu"→"Kyu"). "Ư!" cuối dòng là bản sửa gasp của audit (đã merge, KHÓA) — giữ nguyên trong bản sửa moan, KHÔNG phải Ư mới do đợt này thêm vào.

### 4c. Sửa đếm nguyên âm (1 dòng)

**Key 1007 (ポーレット)**
- JP: `「きゃぁん」`
- TW: `「呀——」`
- VN cũ: `「Kyaaan」`
- Sửa: `「Kyaan」`
- Lý do: Đếm lại độc lập theo công thức: JP きゃぁん có 2 âm a (きゃ + ぁ), VN cũ "Kyaaan" có 3 âm a — thừa 1. Audit đã giữ "Kyaaan" ("tiếng hét, nằm trong khoảng chấp nhận được") nhưng đếm theo công thức thì thừa, và bài học 凪h2 2500 là đếm lại độc lập, không tin số đã ghi. Sửa thành "Kyaan" (2 âm a).

## 5. Các dòng rên đã xét, giữ nguyên

- **fa/fu giữ "phà"/"phù" (hơi thở nhẹ, không phải rên cao trào):** 1074 ("A——phà——anh Soutetsu——anh Soutetsu" — gọi tên anh dịu dàng giữa tiếng thở, không phải chuỗi thở gấp); 1043 ("Ehehe. … ——a phù" — hơi thở nhẹ sau tiếng cười, dịu); 1053 ("Ồ phù!" — tiếng thở ngạc nhiên, tự nhiên); 1127 ("Ưm phù!!!" — quy ước file); 1167 ("Phù! A! Mạnh quá!" — hơi thở ngắn, tự nhiên); 1315 ("（Phù～～～Ư）" — hơi thở nhẹ trong ngoặc); 1072/1079 ("phu" — hơi thở bị cắt cụt bởi ——, audit đã chấp nhận); 1735 ("Bụp" — audit sửa "Bịch"→"Bụp", đã đúng âm mềm).
- **ひあ/ひゃ giữ:** 1011 "Hia" (ひあっ — đã là romaji đúng), 1015 "Hya!" (ひゃっ), 1210 "Hya!" (ひゃ), 1025 "Khíu" (くひゅっ — tiếng gasp ngắn, tự nhiên).
- **Cười (9 dòng):** 1018 "Fufu——fufufu! Ufufufufu!!!", 1043 "Ehehe", 1059 "Ufufu", 1060 "Ufufu", 1075 "ufufu", 1087 "Ahaha", 1194 "ehehe", 1227 "Ehehe", 1321 "Ufufu" — đều đã là tiếng cười, quyết Hieu 22:05 (cười là cười, không phải gasp).
- **Gasp Ư (13 mục sweep + 4 already-rendered):** giữ toàn bộ theo quy tắc khóa — 1044, 1064, 1070, 1236, 1558, 1597 (bản sửa Ư của sweep, audit xác nhận), 1062, 1063, 1065, 1068 (already-rendered "Ư"), 1009/1124 (audit bổ sung Ư cho gasp mất), 1028 (already-rendered, chỉ nói về gasp).
- **Rên dài/SFX dài giữ (đếm đã kiểm chứng bằng máy, §2):** 1010 "Kyuuuuuuuuuuuuuuuuuun" (18 u ✓), 1037 "Phập chụụụụụụụụụt" (9 ụ ✓), 1105 "rộộộộộp" (5 ộ ✓), 1107 "Rộột" (2 ộ ✓), 1108 "Chụụụt" (3 ụ ✓), 1148 "Chụụụt" (3 ụ ✓), 1255 "rộộộộộộộộộộộộộộộộộộộp" (19 ộ ✓), 1315 "rộộp" (2 ộ ✓), 1317 "Chụụt"/"Phậập" (2+2 ✓), 1319 "Chụụt"/"Chụụụt" (2+3 ✓), 1020 "chụụt" (2 ụ ✓), 1085 "Phậậập" (3 ậ ✓), 1024 "Phààà"→ nay "Faaa" (3 à ✓), 1036 "Hauu" (はぅぅ = 2 ぅ ✓), 1131 "Ưm uu u" (んうううっ = 3 u ✓), 1770 "Đâm sâu uuuuuuuuuuu" (12 u = 1+11 ✓, audit đã xác minh).
- **Chuỗi SFX oral + độc thoại:** giữ toàn bộ dạng Việt của audit ("chụt"/"rộp"/"liếm nhẹ"/"Ngoạm"/"Bụp"/"Hắt xì"/"Khụ"/"hự") và động từ Việt trong độc thoại — tự nhiên, không ngượng, đúng quy ước file.
- **Các dòng đã xét, giữ:** 1016 "Kya!?" (きゃっ), 1017 "Ư ha" (くはっ — theo TW 呃啊, audit chấp nhận), 1033 "Hau!!?" (はうっ), 1035 "Hau～～Ư" (gasp đã thêm Ư, khóa), 1052 "Hả? A——ưm", 1054 "Oa!" (ぉあっ), 1058 "Hứ" (むぅ — tiếng bĩu môi), 1061 "Ưa" (ぅぁっ), 1077 "A——a——a——ư——" (っ cuối đã diễn bằng "ư"), 1078 "A——a——a——aa!", 1089/1090 "Au" (あうっ), 1091 "Aa——", 1092 "A a!", 1094 "A!", 1097 "A!?", 1114 "Ưm——a——…", 1115 "(Liếm láp)" (ぺちょっっ), 1118 "Ưm……a!", 1120 "Ưm……" (ん……っと — TW cũng chỉ 嗯……), 1123 "Ừm.", 1125 "Ưm kyun!!!" (んきゅんっ, theo h7), 1129 "Ây da" (ん、しょっ — audit chấp nhận), 1130 "Ưm" (ううむ), 1137 "Ưm, ưm!", 1152 "V-Vâng!!?", 1183/1184 (chuỗi "ưm——ha——a"), 1197 "A u!!?", 1220 "lớp thịt mềm mại" (ぷりゅぷりゅ), 1235 "Gâu!" (わん！), 1245/1299 "Ưm a" (んあっ), 1266 "ưm" (ンッ), 1271 "Đừng! Đừng mà" (やぁん — theo TW), 1272 "Á!?", 1273 "Đừng, anh Soutetsu", 1300 "Anh Soutetsu?", 1320 "(Liếm nhẹ)" (ぺろっ), 1429/1449 (SFX trần thuật), 1491 "ngoan ngoãn" (ポフっと — audit chấp nhận), 1703 "(Khựng lại)", 1704/1707/1708/1757/1775 (SFX độc thoại đã Việt hoá thành cụm từ — audit giữ), 1710–1728 (びゅ/ぴゅ → "Phụt"), 1730 "(Phụt!!!)" (ぷりゅんんっっ — audit giữ), 1731–1784 (SFX độc thoại theo quy ước file), 1029 "Kuuun" (くぅん — quyết Hieu 22:19, giữ).

## 6. Flags (chưa quyết — ghi nhận, KHÔNG tự sửa)

1. **1093 「ぁあっっ！！」 → "A a!!":** JP kết thúc bằng HAI っ liên tiếp, VN chỉ diễn bằng "!!" — gasp có thể bị mất (tiền lệ phụ lục đa-っ lr_日々姫h2 971: mỗi っ → 1 Ư). Sweep không liệt kê dòng này, audit cũng không sửa. Đây là câu hỏi thuộc phạm vi gasp-sweep, không phải moan-fix — ghi lại để parent/audit quyết, không tự thêm Ư ở đây. Tương tự, 1024 "Faaa!!!" giữ "!!!" theo fix audit đã merge (cùng câu hỏi っっ).
2. **1017 くはっ → "Ư ha":** phụ âm "k" của く bị mất (diễn thành "Ư") — TW cũng diễn 呃 nên audit chấp nhận; nếu Hieu muốn giữ âm "Kuha" thì đổi ở đợt thống nhất.
3. **1077 「ぁ――ぁ――ァ――っ――」 → "A——a——a——ư——":** っ cuối diễn thành "ư" thường (không phải "Ư") — sweep không liệt kê; giữ nguyên, ghi chú.

## 7. Kiểm tra lần hai

- Đọc lại toàn bộ **10/10** bản sửa đối chiếu JP (+TW): **10 xác minh đúng, 0 bị loại, 0 sửa lại**. (Kiểm tra lần hai là lần đọc độc lập sau khi viết xong danh sách — các số đếm nguyên âm đã đếm lại bằng máy trước khi chốt: 1007 2 a, 1024 3 a, 1010 18 u, 1037 9 ụ, 1255 19 ộ.)
- Kiểm chứng bằng máy sau khi viết JSON: JSON có 10 mục, key là chuỗi; jp/tw/old_vn khớp CSV3 10/10; mỗi fix chỉ khác old_vn đúng ở (các) token rên đã nêu; khối TOML parse được bằng tomllib, 10 key, giá trị khớp JSON 10/10.
- Không có dòng "Kh" nào bị đổi sang Ư. Không có bản sửa nào chạm tới xưng hô/thuật ngữ/nghĩa (các fix audit khác trên cùng dòng — "Khíu" ở 1025, "Ư!" ở 1009 — được giữ nguyên vẹn trong bản sửa moan).
- File trùng lặp: không có (md5 duy nhất trong 227 file).

## 8. Khối TOML để dán vào file (đã kiểm chứng parse được)

Khối dưới đây đã kiểm chứng parse được bằng tomllib, đúng 10 key, giá trị khớp đúng JSON bản sửa. Dán vào section `[script]` của file `03_Paulette/lr_ポーレットh2_デコレーション＆ミルク.txt.toml` (ghi đè đúng 10 key này, giữ nguyên mọi key khác). Lưu ý: `\\n` trong khối là ký tự backslash-n thật (khớp VN cũ trong CSV3), KHÔNG phải ngắt dòng thật.

```toml
[script]
1007 = "「Kyaan」"
1009 = "「Kyufu!? Ưm! Khoan đã!\\nBình tĩnh——a——bình tĩnh lại đi——anh Soutetsu——Ư!」"
1022 = "「Fua——ha——a——a——chậm rãi, thế này——\\nem cũng thích——ưm——chỗ, sướng ấy——cứ từ từ——a」"
1024 = "「Fua! A! A! A! Khoan! Ưm a!\\nKhoan đã——a——ưm a! Faaa!!!」"
1025 = "「Khíu! Ưm——a——Fa——a——a……\\nA——chỗ, to ấy——cọ vào——thích quá——ưm——」"
1032 = "「Hau uu——Fua——a——\\nngực——nhũ hoa——sướng quá——a」"
1039 = "「Ha! A——a——a——em——\\nthế này——Fa——ra mất, ra mất, ra mất, ra mất!」"
1084 = "「Ha——au——Fan——ưm——kuuun——\\nƯm. Thế này——chậm rãi——ha——chậm rãi, thế mà」"
1095 = "「A! Ưm! Fua! A! A! Aa!\\nEm! Ra rồi! Ngực em! Ra sữa rồi!!」"
1099 = "「A!? A——a——a——Fua——thế này——\\nthế này——ế——ưm——thế này——thích quá——」"
```

## Kết bài

File lr_h2: đọc 333/333 dòng; xét 281 dòng ứng viên rên; **đổi 10 dòng** (9 romaji + 1 sửa đếm nguyên âm) — 8 họ fa/fu → Fa/Fua/Fan, 1 きゅふっ → "Kyufu", 1 きゃぁん thừa 1 âm a → "Kyaan"; giữ 271 dòng (trong đó 9 fa/fu thở nhẹ giữ "phà"/"phù", 9 cười giữ nguyên, 13 mục gasp Ư khóa, toàn bộ chuỗi SFX oral + độc thoại theo quy ước file). Kiểm tra lần hai: 10/10 xác minh đúng, 0 loại, 0 sửa lại. Đếm nguyên âm của audit trong nhóm SFX dài đã kiểm chứng lại bằng máy — tất cả đúng, không phát hiện lỗi đếm nào. Một flag gasp (1093, っっ cuối dòng) ghi lại cho parent quyết, không tự sửa.
