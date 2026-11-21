# Moan-fix REVIEW — れいなh1_おかあさんのレッスン.txt.toml (moan-reinah1-okaasan-no-lesson)

File: `れいなh1_おかあさんのレッスン.txt.toml` — route 04_Reina, H-scene "Bài học của mẹ" (Paulette làm mẫu dạy Reina; audit đã gộp 38/402).

## 1. File verification

- TOML: `sources/toml2/translation_toml/04_Reina/#U308c#U3044#U306ah1_#U304a#U304b#U3042#U3055#U3093#U306e#U30ec#U30c3#U30b9#U30f3.txt.toml`, md5 `09eaed303cc160ad7b01033ad81f8c51` (khớp md5 audit), không có bản trùng.
- CSV3: 1 set duy nhất (`translation_toml\04_Reina`), 402 dòng script, 0 key trùng. VN khớp TOML 402/402 sau chuẩn hoá `\n` (238 dòng chỉ khác ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng — CSV3 là chuẩn).
- Đã đọc 402/402 dòng. Không có `%l` tag trong file. `[selections]` rỗng.
- File có trong moan queue (vị trí 2), chưa có trong `ROUTE-MOANS.md` — không trùng lặp.

## 2. Moan inventory

- Dòng rên/SFX xét kỹ (mẫu chặt: ひあ/ひゃ/ひゅ/きゃ/んひゅ, fa/fu, くあ, うふふ, あっ/んっ/んんん, gasp っ, SFX trong （）, chuỗi kiss/suck ちゅ/じゅ/れろ, nói ngọng, よいしょ/はわ, モコォ/きゅん): **168 dòng**.
- Sửa: **17 dòng**. Giữ: **144 dòng**. Sweep: 7 mục đã kiểm chứng, không đụng (5 gasp Ư đã fix ở sweep: 1323, 1346, 1348, 1349, 1574; 2 already-rendered: 1373, 1375).
- Phân loại 17 dòng sửa: romaji 14 (1233, 1264, 1286, 1290, 1322, 1336, 1337, 1344, 1354, 1527, 1528, 1530, 1537, 1552), đếm nguyên âm 2 (1274, 1533), sai âm 1 (1420).
- Nhóm lỗi chính (một dòng có thể thuộc 2 nhóm):
  - (a) ふあ(っ)/ふわぁ bị tách mảnh hoặc mất âm ("Phù a" / "Phù" / "Ha" / "Phù oa") — 11 dòng (1233, 1264, 1286, 1290, 1336, 1344, 1354, 1528, 1530, 1537, 1552).
  - (b) ひあ/んひゅ diễn "Hya"/"Ưm" — mất/sai phụ âm mora (quy tắc 3b, quyết 21/11 ~11:55) — 4 dòng (1264, 1337, 1344, 1527).
  - (c) Sai/mất số lượng nguyên âm — 3 dòng (1274 ああっ→"A!", 1354 んんんっ→"ưm", 1533 ああっ→"A a").
  - (d) Sai hẳn âm — 2 dòng (1322 くあっ→"Hự!", 1420 いっ→"Á").
- Quan hệ với audit đã gộp (38 dòng): audit đã sửa 17 dòng fa/fu + 2 đếm nguyên âm + 2 tiếng cười + 5 gasp. Moan fix này **xét lại** các fix moan của audit theo quy tắc romaji (21/11 ~01:56) và quy tắc ひゃ-family 3b (21/11 ~11:55) — hai quyết định ra SAU khi audit gộp (20/11 ~17:20). 9 dòng sửa ở đây xây trên VN sau audit (giữ nguyên phần audit đúng, chỉ đổi phần rên): 1233, 1264, 1336, 1337, 1344, 1527, 1530, 1533, 1537. `old_vn` trong JSON vẫn là VN gốc CSV3 (theo quy tắc kiểm chứng của loop parent); giá trị `fix` là câu VN hoàn chỉnh cuối cùng (audit + moan).

## 3. Per-row fixes (17)

### 1233 [れいな] — ふあっ → "Fua" (audit "phù" làm mất âm "a")
- JP: 「せっくす……セックス――んっ――れいな――ちゃんと、\nそうてつ、さんと……んっ――あっ――ふあっ――あっ」
- TW: 「做愛……做愛……玲奈……和雙鐵先生……做到了……蛤啊……蛤啊……」
- Old VN (CSV3): 「Làm tình……làm tình——ưm——Reina——đã đàng hoàng,\nlàm với anh, Soutetsu……ưm——a——ha——a」
- Audit: 「……ưm——a——phù——a」 ("phù" cho ふあっ — mất hẳn âm "a")
- Fix: 「Làm tình……làm tình——ưm——Reina——đã đàng hoàng,\nlàm với anh, Soutetsu……ưm——a——Fua——a」
- Lý do: ふあっ = "fua" — một âm duy nhất; "phù" chỉ còn "fu", mất "a". Romaji "Fua" giữ đủ âm.

### 1264 [れいな] — ひあっ → "Hia"; ふあ…んっ tách mảnh → romaji một khối
- JP: 「ひあっ！？　あっ――あっ――あっ――\nふあああああああああああああんっ！！！」
- TW: 「呀啊？！啊啊啊啊……啊啊啊啊啊啊啊！！！」
- Old VN (CSV3): 「Hya!? A――a――a――\nPhù aaaaaaaaaaaaaa!!!」
- Audit: 「Hya!? A――a――a――\nPhù aaaaaaaaaaaaan!!!」 (chỉ sửa đếm: 13 a + n; vẫn tách "Phù a…n" và vẫn "Hya" cho ひあ)
- Fix: 「Hia!? A――a――a――\nFuaaaaaaaaaaaaan!!!」
- Lý do: (1) ひあ → "Hia" theo quy tắc 3b ("Hya" là âm của ひゃ, sai âm — tiền lệ 凪h2 sửa 5 dòng). (2) ふ + あ×13 + ん = "Fuaaaaaaaaaaaaan" (Fu + 13 a + n, đếm bằng script); bản cũ tách một âm thành "Phù" + "a…n" rời — tiền lệ ふかみh1 gộp mảnh rời thành một cách diễn romaji.

### 1274 [双鉄H] — ああっ → "Aa!" (mất một nguyên âm)
- JP: 「ああっ！」
- TW: 「呃啊！」
- Old VN: 「A!」
- Fix: 「Aa!」
- Lý do: ああっ = hai âm "a" + ngắt っ; "A!" chỉ còn một "a", mất nửa âm. Audit bỏ sót dòng này (audit chỉ sửa đếm 1264, 1374).

### 1286 [れいな] — ふわぁ → "Fuwaa" (tách mảnh "Phù oa")
- JP: 「ふわぁ……お風呂で見るときと、全然違う形ですぅ。\nほんとに、すっごく大きくなってるんですねぇ」
- TW: 「哇……跟洗澡的時候見到的形狀完全不一樣。真的變得好大呀」
- Old VN: 「Phù oa…… Hình dạng khác hẳn lúc thấy trong nhà tắm luôn ạ.\nThật sự là, đã lớn lên rất nhiều rồi nhỉ~」
- Fix: 「Fuwaa…… Hình dạng khác hẳn lúc thấy trong nhà tắm luôn ạ.\nThật sự là, đã lớn lên rất nhiều rồi nhỉ~」
- Lý do: ふわぁ = "fuwaa" — một âm duy nhất; "Phù oa" tách thành hai mảnh rời và sai âm ("Phù" là âm của ふぅ). Audit bỏ sót dòng này.

### 1290 [れいな] — ふあっ → "Fua" (tách mảnh "Phù a")
- JP: 「ふあっ――あつい――ですぅ――なんか――\nしろい、の」
- TW: 「哇啊……好熱……白白的……」
- Old VN: 「Phù a――nóng――quá ạ~――cái gì――\ntrắng trắng, ấy.」
- Fix: 「Fua――nóng――quá ạ~――cái gì――\ntrắng trắng, ấy.」
- Lý do: như 1233 — ふあっ là một âm "fua"; "Phù a" tách rời. Audit bỏ sót dòng này.

### 1322 [双鉄H] — くあっ → "Kua!" ("Hự!" làm mất hẳn âm "kua")
- JP: 「くあっ！」
- TW: 「唔！」
- Old VN: 「Hự!」
- Fix: 「Kua!」
- Lý do: くあっ = "kua" rõ ràng; "Hự!" chỉ là tiếng hự chung chung, mất hẳn âm "kua". Tiền lệ trong chính file này: 1272 くあっ → "Kua" (đã đúng). Ghi chú: audit đã cờ "Kua vs Hự (1272/1322)" chờ Hieu — quyết ở đây theo quy tắc romaji (Hieu duyệt 21/11 ~01:56) + tiền lệ 1272: âm JP rõ thì giữ âm, không thay bằng tiếng hự chung.

### 1336 [れいな] — ふあ×6 → "Fuaaaaaa" (tách mảnh "Phùaaaaaa")
- JP: 「ふああああああっ！！？」
- TW: 「啊啊啊啊啊！！？」
- Old VN: 「Haaaaaaaa!!?」
- Audit: 「Phùaaaaaa!!?」 (sửa "Ha…" → "Phù" + 6 a — đúng số lượng, nhưng vẫn tách "Phù" + "aaaaaa")
- Fix: 「Fuaaaaaa!!?」
- Lý do: ふ + あ×6 + っ = "Fuaaaaaa" (Fu + 6 a, đếm bằng script); một âm duy nhất, không tách mảnh.

### 1337 [れいな] — ひあっ → "Hia" (quy tắc 3b; audit "Hya" sai âm)
- JP: 「ひあっ――あっ！」
- TW: 「啊啊啊啊！」
- Old VN: 「Á——a!」
- Audit: 「Hya——a!」 (sửa "Á" → "Hya" — đúng hướng nhưng sai âm: "Hya" là ひゃ, JP là ひあ)
- Fix: 「Hia——a!」
- Lý do: quy tắc 3b (quyết 21/11 ~11:55, sau khi audit gộp): ひあ → "Hia". "Á" mất phụ âm h-, "Hya" thêm phụ âm y-; chỉ "Hia" giữ đủ âm. Đây cũng là một trong các mâu thuẫn ひあ/ひゃ audit đã cờ chờ Hieu — nay đã có quyết 3b.

### 1344 [れいな] — んひゅっ → "Nhyu!"; ふあぁっ → "Fuaa"
- JP: 「んひゅっ！　ふあぁっ――あっ――ひ、んっ――\nそこ――れいな――ふ、ぁ――ぞりって、される、とぉ」
- TW: 「啊嗯……蛤啊……啊……那裡……玲奈……蛤啊……被摩擦的話……」
- Old VN: 「Ưm! Ha——a——hi, ưm——\nChỗ đó——Reina——ha, a——bị cọ xát, thế này——」
- Audit: 「Ưm! Phùaa——a——hi, ưm——\nChỗ đó——Reina——phù, a——bị cọ xát, thế này——」 (giữ "Ưm!" cho んひゅ; "Phùaa" vẫn tách mảnh)
- Fix: 「Nhyu! Fuaa——a——hi, ưm——\nChỗ đó——Reina——phù, a——bị cọ xát, thế này——」
- Lý do: (1) んひゅ → "Nhyu" theo quy tắc 3b (tiền lệ h7 836/837, 稀咲h3 2277, 凪h2 2512: んひゅ→"Nhyu/Nhyun"); "Ưm!" mất hẳn âm "nhyu". (2) ふあぁっ = fu + a + a = "Fuaa" một khối; "Phùaa" tách mảnh. Giữ "phù, a" của audit cho ふ、ぁ (JP tự ngắt ふ、ぁ bằng dấu phẩy — hai mora rời, "phù, a" diễn đúng).

### 1354 [れいな] — ふあっ → "Fua"; んんんっ → "ưmmm" (mất độ dài)
- JP: 「あっっ！？　いまっ――いまの、とこ――ふあっ――\nざらっ、って――ざらって――んっ――んんんっ」
- TW: 「啊？！剛、剛才那個地方……麻麻的……啊嗯……啊啊……」
- Old VN: 「A!? Vừa nãy――chỗ, vừa nãy――phù a――\nnham nháp――nham nháp――ưm――ưm.」
- Fix: 「A!? Vừa nãy――chỗ, vừa nãy――Fua――\nnham nháp――nham nháp――ưm――ưmmm.」
- Lý do: (1) ふあっ → "Fua" (như 1290). (2) んんんっ = 3 mora "n" — "ưm" chỉ còn 1, mất độ dài; "ưmmm" (ư + 3 m) giữ đủ — tiền lệ 凪h2 んんんっ→"Ưmmm". Audit bỏ sót dòng này. Giữ "A!?" cho あっっ (dấu !? đã diễn っ kép nhấn mạnh).

### 1420 [れいな] — いっ → "Í!?" ("Á" sai nguyên âm)
- JP: 「い"っ！？」 (JP có ký tự `"` lạ sau い — lỗi phía JP, không phải lỗi VN; xem Flags)
- TW: 「好痛！？」
- Old VN: 「Á!?」
- Fix: 「Í!?」
- Lý do: いっ là tiếng gasp âm "i" ngắt; "Á" diễn âm "a" — sai nguyên âm, mất âm "i". Theo cùng logic mất âm của quy tắc 3b ("Á" chỉ đúng khi JP không có phụ âm mora — ở đây JP có nguyên âm "i" rõ ràng), sửa thành "Í!?". Audit bỏ sót dòng này.

### 1527 [れいな] — ひあッ → "Hia" (quy tắc 3b; audit "Hya" sai âm)
- JP: 「ひあッ――んっ――ひゃっ――あっ――\nそうてつ――さんっ――そおてつ――さぁん」
- TW: 「蛤啊……啊……啊……雙鐵先生……雙鐵先生……」
- Old VN: 「Á——ưm——hya——a——\nAnh——Soutetsu——anh——Soutetsu~」
- Audit: 「Hya——ưm——hya——a——\nAnh——Soutetsu——anh——Soutetsu~」
- Fix: 「Hia——ưm——hya——a——\nAnh——Soutetsu——anh——Soutetsu~」
- Lý do: như 1337 — ひあ → "Hia"; ひゃっ sau đó giữ "hya" (âm đã đúng, chữ thường giữa dòng là đúng quy cách câu). Chỉ đổi âm đầu.

### 1528 [れいな] — ふあっ → "Fua" (tách mảnh "Phù a")
- JP: 「ふあっ――あっ――\nんっ――くっ――」
- TW: 「蛤啊……啊……啊嗯……」
- Old VN: 「Phù a――a――\nƯm――hự――」
- Fix: 「Fua――a――\nƯm――hự――」
- Lý do: như 1290. Giữ くっ→"hự" (tiếng hự nghẹn — xem Kept notes).

### 1530 [れいな] — ふあっ → "Fua" (audit "Phù" làm mất âm "a")
- JP: 「ふあっ――あっ――あっ――あ……」
- TW: 「蛤啊……啊、啊、啊……」
- Old VN: 「Ha——a——a——a……」
- Audit: 「Phù——a——a——a……」
- Fix: 「Fua——a——a——a……」
- Lý do: như 1233 — "Phù" chỉ còn "fu", mất "a".

### 1533 [れいな] — ああっ → "Aa" (tách mảnh "A a"); giữ "Phùa"
- JP: 「ふあ――あっ！　あっ！　ああっ」
- TW: 「蛤啊……啊！啊！啊啊！」
- Old VN: 「Ha——a! A! A a」
- Audit: 「Phùa——a! A! A a」
- Fix: 「Phùa——a! A! Aa」
- Lý do: ああっ là MỘT âm hai "a" + ngắt; "A a" tách thành hai token rời. Gộp thành "Aa" (tiền lệ ふかみh1: gộp mảnh rời). Giữ "Phùa" của audit cho ふあ — dạng khóa ふあ→"phùa", không ngượng trong câu rên mạnh này.

### 1537 [れいな] — ふあっ → "Fua" (audit "phù" làm mất âm "a")
- JP: 「ぃっ――ふっ――ふあっ――ふうっ」
- TW: 「蛤啊……蛤啊……唔……」
- Old VN: 「Ư——phù——phù——phù」
- Audit: 「Ư——phù——phù——phùù」 (sửa ふうっ → "phùù" theo công thức 1+1う = 2 u — đúng; nhưng ふあっ vẫn "phù")
- Fix: 「Ư——phù——Fua——phùù」
- Lý do: như 1233/1530. Giữ ぃっ→"Ư" (gasp đã diễn), ふっ→"phù", ふうっ→"phùù" (audit đúng).

### 1552 [れいな] — ふあっ → "Fua" (tách mảnh "phù a")
- JP: 「そぉなん……です……ふあっ……あっ――んっ――\nきもちい、ぃ――ですぅ……ふっ……おっぱい、も……」
- TW: 「這樣啊……啊、啊嗯……好舒服……啊嗯……胸部也是……」
- Old VN: 「Vậy sao……ạ……phù a……a――ưm――\nsướng, quá――ạ~……phù……ngực, cũng……」
- Fix: 「Vậy sao……ạ……Fua……a――ưm――\nsướng, quá――ạ~……phù……ngực, cũng……」
- Lý do: như 1290. Giữ ふっ→"phù" cuối dòng.

## 4. Kept-moan notes (giữ — kèm lý do cho các dòng đáng chú ý)

- **Dạng khóa fa/fu của audit — giữ nguyên** (đã xét lại từng dòng theo quy tắc romaji; các dạng này không ngượng trong ngữ cảnh của chúng, nên giữ dạng khóa thay vì ép romaji): ふぁ→"Phà" (1284, 1350, 1529, 1532, 1535); ふあ→"Phùa" (1533); ふぇ→"phuê" (1266, 1278, 1355, 1526 — audit đổi từ romaji "Fue" sang "phuê" theo dạng khóa; tiếng gasp ngắn, "phuê" đọc tự nhiên); ふや→"phuya" (1263, 1525, 1531 — 1263 "Phuya……a" giữ nguyên vì JP tự ngắt ふや……ぁ bằng dấu …).
- **Romaji đã đúng — giữ**: ひゃわっ→"Hyawa" (1293, 1295), ひゃん→"Hyan" (1319), ひゃっ→"Hya" (1268, 1343, 1320), ひゃうっ→"Hyau" (1355), ぷきゃっ→"Pukya" (1320), ひひゃほ→"Hihyaho" (1370), くあっ→"Kua" (1272 — tiền lệ cho 1322), ふえっ→"Fue" không còn (audit đã đổi sang "phuê", xem trên).
- **Tiếng cười — audit đã sửa đúng, không đụng**: うふふ→"Ufufu" (1401, 2134 — audit đã sửa từ "Ư hự hự" sai quy tắc 22:05).
- **Đếm nguyên âm — audit đã sửa đúng, kiểm chứng lại**: 1374 きゅふう×12 → audit "Kyuuuuuuuuuuuuuu" = 14 u (1 kyu + 1 fu + 12 う — đếm lại bằng script, đúng). Không sửa thêm.
- **Gasp Ư — không đụng** (quy tắc khóa): 1323, 1346, 1348, 1349, 1574 (sweep đã fix); 1373, 1375 already-rendered (1373: 9 ぅ → 9 ư, đếm khớp).
- **"Kh" — không có dòng Kh nào trong file này** (không xung đột với quy tắc khóa 21/11).
- **SFX giữ nguyên**: chuỗi hôn/mút ちゅ/じゅ/れろ→"chụt/sụt/rộp" (1359, 1360, 1362, 1369, 1372, 1383…); SFX trong （）→ nghĩa Việt ("Bật ra", "Trơn tuột", "Phập", "Nhóp—nhép"…) (2320–2366); はむっ→"ngoạm" (1301, 1352, 1369…); ふっ→"phù" (1524, 1529, 1537, 1552); く→"hự" (1321 んっ――く — tiếng hự nghẹn ngắn, khác くあっ có âm "a" rõ); きゅんっ→"Thắt tim" (1345 — SFX diễn bằng nghĩa, tự nhiên); よいしょ→"Dô ta" (1221 — câu hô Việt tự nhiên); モコォ→ nghĩa "phồng to lên" (1571 — SFX diễn bằng nghĩa, giữ); nói ngọng/nói lắp romaji (1282, 1341, 1368, 1364, 1370, 1338 — giữ; xem Flags về 1282/1341); あ～～～ん→"a~~~n"/"A~~n" (1262, 1292 — giữ đủ âm); ちゅうううっ→"Chuuuu" (2351 — 4 u, đếm khớp JP ちゅ+う×3).

## 5. Flags (cho đợt thống nhất / audit — không tự quyết ở đây)

1. **1534 [ポーレット] — がっ―― → "ưm——" (không chắc, để lại)**: JP 「は……ぁっ――んっ――きて、るっ――\n来てるっ――双鉄、くん――がっ――」, TW 「蛤啊……嗯……進來了……雙鐵君……」, VN 「Ha……a——ưm——vào, rồi——\nVào rồi——anh Soutetsu——ưm——」. がっ là âm tiết bị ngắt (Paulette nói dở "Soutetsu-kun—ga—"), VN diễn thành tiếng hự chung "ưm" — mất âm tiết "ga". Đây là từ bị ngắt, không phải tiếng rên — thuộc phạm vi audit, không sửa trong moan fix. Đề nghị đợt thống nhất/audit xem xét "Ga" hay giữ "ưm".
2. **1420 — JP có ký tự `"` lạ**: JP 「い"っ！？」 — dấu `"` sau い có vẻ là lỗi gõ phía JP (không có trong TW). Không phải lỗi VN; ghi chú để kiểm tra nguồn JP nếu cần.
3. **1282 / 1341 — nói ngọng phiên âm**: audit đã cờ "2 dòng ngọng phiên âm" chờ Hieu (1282 はふぇふぇっ/はんは… → "Hafefe?/Hanha…", 1341 ぷっ――んっ――ほーへふはんほ… → "Pụt――ưm――hoohefuhanho…"). Cả hai đã là romaji, giữ nguyên ở đây; cờ của audit vẫn còn nguyên.
4. **1535 — phần nghĩa thuộc audit**: audit đã thêm "phà" cho ふぁっ (giữ); VN còn thêm "đau……quá" mà JP không có từ "đau" trực tiếp (JP: は……ぃ……っ……たっ……んくっ――ふぁっ……). Đó là quyết của audit đã gộp — không xét lại trong moan fix.
5. **Câu hỏi chờ của audit đã được giải quyết bởi quyết sau audit** (ghi để parent đối chiếu, không cần Hieu quyết lại): "Kua vs Hự (1272/1322)" → quyết "Kua" ở 1322 theo quy tắc romaji + tiền lệ 1272; mâu thuẫn ひあ/ひゃ ("Hya" vs "Hia" vs "Á") → quyết theo quy tắc 3b (21/11 ~11:55): 1264/1337/1527 → "Hia", 1344 んひゅ → "Nhyu".

## 6. Second-pass counts

- Lượt soát 2 (đọc lại toàn bộ 17 fix đối chiếu JP): tổng **17** / tái kiểm chứng **17** / bỏ **0** / sửa **0**.
- JSON 17 mục, khóa string, jp/tw/old_vn khớp CSV3 17/17. Khối TOML parse bằng tomllib: 17 khóa, 0 sai lệch giá trị so với wrong.json.
- 9 fix xây trên VN sau audit (1233, 1264, 1336, 1337, 1344, 1527, 1530, 1533, 1537): mỗi fix chỉ đổi phần rên, giữ nguyên phần còn lại của audit — kiểm chứng bằng diff cơ học (script `rep` chỉ thay đúng chuỗi đích, báo lỗi nếu chuỗi không duy nhất).

## 7. TOML block (parse-verified, 17 keys)

```toml
[script]
"1233" = "「Làm tình……làm tình——ưm——Reina——đã đàng hoàng,\\nlàm với anh, Soutetsu……ưm——a——Fua——a」"
"1264" = "「Hia!? A――a――a――\\nFuaaaaaaaaaaaaan!!!」"
"1274" = "「Aa!」"
"1286" = "「Fuwaa…… Hình dạng khác hẳn lúc thấy trong nhà tắm luôn ạ.\\nThật sự là, đã lớn lên rất nhiều rồi nhỉ~」"
"1290" = "「Fua――nóng――quá ạ~――cái gì――\\ntrắng trắng, ấy.」"
"1322" = "「Kua!」"
"1336" = "「Fuaaaaaa!!?」"
"1337" = "「Hia——a!」"
"1344" = "「Nhyu! Fuaa——a——hi, ưm——\\nChỗ đó——Reina——phù, a——bị cọ xát, thế này——」"
"1354" = "「A!? Vừa nãy――chỗ, vừa nãy――Fua――\\nnham nháp――nham nháp――ưm――ưmmm.」"
"1420" = "「Í!?」"
"1527" = "「Hia——ưm——hya——a——\\nAnh——Soutetsu——anh——Soutetsu~」"
"1528" = "「Fua――a――\\nƯm――hự――」"
"1530" = "「Fua——a——a——a……」"
"1533" = "「Phùa——a! A! Aa」"
"1537" = "「Ư——phù——Fua——phùù」"
"1552" = "「Vậy sao……ạ……Fua……a――ưm――\\nsướng, quá――ạ~……phù……ngực, cũng……」"
```

## Kết bài

File れいなh1_おかあさんのレッスン: đã đọc 402/402 dòng, xét 168 dòng rên/SFX, sửa **17 dòng** (14 romaji, 2 đếm nguyên âm, 1 sai âm), giữ 144 dòng, sweep 7 mục không đụng. Lỗi lớn nhất là họ ふあ(っ) bị tách mảnh hoặc mất âm ("Phù a"/"Phù"/"Ha" — 10 dòng) và họ ひあ/んひゅ bị diễn sai/mất âm theo quy tắc 3b (4 dòng) — tất cả đã sửa sang romaji một khối, đếm nguyên âm bằng script. 9 fix xây trên VN sau audit, chỉ đổi phần rên. Lượt soát 2: 17/17/0/0. Khối TOML 17 khóa parse-verified, 0 sai lệch. Cờ cho đợt thống nhất: 1534 がっ→"ưm" (chưa quyết), JP 1420 có `"` lạ, 1282/1341 (cờ audit còn nguyên), 1535 (phần nghĩa thuộc audit); hai câu hỏi chờ của audit ("Kua vs Hự", mâu thuẫn ひあ/ひゃ) đã được giải quyết bởi quy tắc romaji + 3b trong file này.
