# Audit — lr_ふかみh1_ふかみうさぎのたまご.txt.toml (07_Nagi_Fukami)

## 1. Tổng quan

- **File:** `lr_ふかみh1_ふかみうさぎのたまご.txt.toml` — route 07_Nagi_Fukami, cảnh Fukami làm thỏ Phục Sinh (Easter bunny) tặng Soutetsu "trứng" của mình.
- **Đường dẫn:** `sources/toml2/translation_toml/07_Nagi_Fukami/lr_#U3075#U304b#U307fh1_#U3075#U304b#U307f#U3046#U3055#U304e#U306e#U305f#U307e#U3054.txt.toml`
- **Số dòng đã đọc:** 289/289 dòng script (key 961–1973), đọc từng dòng đối chiếu JP + TW (CSV3) + VN (TOML).
- **Số dòng sai: 76/289 (26,3%).**
- **Cơ sở tổng cộng: 83 file / 4.293 dòng sai** (kiểm chứng với ROUTE-AUDIT.md lúc viết snippet — cơ sở parent giao 82/4.273 đã cũ vì file ハチロク08 20 dòng được gộp song song lúc 11:15 trong khi audit file này; đã rebase theo ROUTE-AUDIT.md hiện tại) **→ sau file này: 84 file / 4.369 dòng sai.**

### Phân loại lỗi

| Nhóm | Số dòng | Keys |
|---|---|---|
| Đại từ — Soutetsu tự xưng "tôi" → "anh" với Fukami (39 lần xuất hiện) | 30 | 972, 975, 1187, 1200, 1201, 1220, 1257, 1307, 1325, 1328, 1333, 1356, 1365, 1374, 1376, 1377, 1381, 1391, 1393, 1398, 1406, 1408, 1411, 1420, 1432, 1433, 1445, 1452, 1455, 1486 |
| Gasp っ bị mất (đứng một mình / sau ―― / sau …… / cả dòng) | 17 | 1257, 1259, 1260, 1261, 1262, 1268, 1288, 1339, 1374, 1435, 1438, 1613, 1651, 1681, 1682, 1780, 1835 |
| SFX fa/fu — ふぁ/ふあ/ふぇ/ふや mất âm đầu "ph" (thành "Ha"/"Hả"/"fu") | 21 | 1223, 1233, 1252, 1254, 1267, 1268, 1270, 1283, 1379, 1457, 1458, 1460, 1461, 1463, 1464, 1465, 1467, 1468, 1469, 1471, 1472 |
| SFX đếm nguyên âm dài sai công thức (VN = 1 + số う/ぅ trong JP) | 8 | 1224, 1279, 1310, 1920, 1949, 1966, 1967, 1968 |
| SFX mất tiếng thở はっ cuối dòng | 1 | 1196 |
| Thuật ngữ — おまんこ "lồn" lẻ loi giữa 27 lần "âm đạo" | 2 | 1669, 1731 |

Ba dòng mang hai lỗi cùng lúc: 1257 (đại từ + gasp), 1374 (đại từ + gasp), 1268 (gasp + fa/fu). Tổng số dòng phân biệt: 76.

### Không có lỗi hệ thống

- **Lệch dòng / xoay vòng (rotation): 0.** VN tại mỗi key khớp đúng JP của key đó; không có cặp lệch nào.
- **Nhiễm chéo (contamination): 0.** Không dòng VN nào thuộc về file khác.
- **Dòng mồ côi (orphan): 0.** Mọi dòng VN đều có JP/TW tương ứng trong file.
- **Chưa dịch: 0.** Không ô VN trống; VN == TW chỉ tại 961 「……」 (dấu câu, không phải chưa dịch).
- **Trùng key: 0.** 289 key duy nhất; CSV3 bộ TỐT và TOML cùng 289 key, khớp 1–1.
- **Rò rỉ tiếng Nhật trong VN: 0.** Không ký tự kana/kanji nào còn trong VN.

## 2. Phương pháp và độ tin cậy của nguồn

- **Nguồn chính: CSV3 bộ 11_Other.** File này có **2 bộ CSV**: `07_Nagi_Fukami` (STALE) và `11_Other` (TỐT). Xác định bằng flat-match VN với TOML: bộ 11_Other khớp 119/289 tuyệt đối + 169/289 chỉ khác ở `\n` bị TOML làm phẳng thành khoảng trắng (= 288/289; 1 khác còn lại là 1466, TOML nuốt luôn `\n` đầu dòng) — tức khớp 289/289 về nội dung. Bộ 07_Nagi_Fukami chỉ khớp tuyệt đối 3/289. **Bộ 07 là STALE — đã audit bằng bộ 11_Other.** JP của bộ TỐT khớp 289/289 với comment `# JP:` trong TOML; JP hai bộ khác nhau ở 242 key (TW hai bộ giống hệt nhau, 0 khác).
- **TOML md5:** `978b35d98d620183d1a58aa3aaa8eda0`. **Không có file trùng lặp** — chỉ 1 bản duy nhất trong `sources/toml2/` (11 nhóm trùng toàn dự án, file này không thuộc nhóm nào).
- **Sweep っ:** kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` — file này CÓ 13 mục (xem §4). Quét bổ sung toàn bộ 289 dòng JP chứa っ: bắt thêm 12 gasp sweep bỏ sót (1257, 1259, 1260, 1261, 1262, 1339, 1374, 1435, 1438, 1681, 1682 + 1268). Không còn gasp っ trần nào khác bị mất.
- **Quét xưng hô bằng máy** (đã chuẩn hoá `\n` thành khoảng trắng trước khi chạy regex `\b` — lần quét đầu bỏ sót 5 dòng vì "tôi" đứng ngay sau `\n` literal trong CSV, khiến `\b` không khớp; đã quét lại sau khi chuẩn hoá): Soutetsu trong thoại tự xưng "tôi" 39 lần / 30 dòng, "anh" 0 lần — tức toàn bộ thoại Soutetsu trong file đều sai xưng hô. Độc thoại "tôi" giữ nguyên theo quy tắc chung (xem §5); "mình" trong độc thoại 0 dòng sai.
- **Quét ふぁ/ふあ/ふぇ/ふや toàn file bằng regex:** bắt đủ 21 dòng (không dựa vào cảm tính).
- **Quét đếm nguyên âm:** kiểm tra mọi chuỗi nguyên âm dài ≥3 trong JP đối chiếu VN.

## 3. Các lỗi đã sửa (76 dòng)

### A. Đại từ — Soutetsu "tôi" → "anh" với Fukami (30 dòng, 39 lần)

Toàn bộ file là cảnh Soutetsu ↔ Fukami (chỉ có 3 loại Character: ふかみ / 双鉄 / monologue; không có nhân vật thứ ba nào). Fukami gọi Soutetsu là 「双鉄おにいさん」 ("anh Soutetsu") xuyên suốt file — theo quy tắc đã sửa 20/11, Soutetsu tự xưng "anh" với Fukami. VN cũ dùng "tôi" ở **mọi** dòng thoại Soutetsu (30/30 dòng thoại có đại từ — 0 dòng đã đúng), khác với file ふかみh2 (từ key 1224 đã dùng đúng "anh"). Đây là lỗi hệ thống của file này, không phải lỗi rải rác.

Mỗi dòng dưới đây đã kiểm chứng người nghe là Fukami từ dòng kề (cảnh đối thoại trực tiếp, Fukami gọi "anh Soutetsu" ngay trước/sau). Chỉ thay đại từ, giữ nguyên mọi từ khác:

- **972** — 「……僕も、思いっきりに染め付けたいのはやまやまだ。」 → "Tôi cũng rất muốn nhuộm nó" → **"Anh cũng rất muốn nhuộm nó"**.
- **975** — 「僕もセックス――ふかみに夢中になってしまって」 → "thế mà tôi cũng mải mê" → **"thế mà anh cũng mải mê"**.
- **1187** — 「僕には、ふかみを責めようなどという気持ちは一切ない」 → "Tôi hoàn toàn không có ý định" → **"Anh hoàn toàn không có ý định"**.
- **1200** — 「僕がイクことを伝えたら」 → "nếu tôi báo sắp ra … để tôi bắn lên" → **"nếu anh báo sắp ra … để anh bắn lên"** (×2).
- **1201** — 「僕の一番強い匂いを」 → "mùi hương mạnh nhất của tôi" → **"của anh"**.
- **1220** — 「僕は、悪い子だったということかな」 → "Chẳng lẽ tôi là một đứa trẻ hư" → **"Chẳng lẽ anh là một đứa trẻ hư"**.
- **1257** — xem mục B (kèm gasp).
- **1307** — 「一番、濃い、僕の匂いは」 → "Mùi hương, đậm nhất, của tôi" → **"của anh"**.
- **1325** — 「僕には、今一つ状況がつかめていない」 → "tôi vẫn chưa nắm bắt được" → **"anh vẫn chưa nắm bắt được"**.
- **1328** — 「僕は嬉しいし大歓迎だ」 → "tôi cũng rất vui" → **"anh cũng rất vui"**.
- **1333** — 「ふかみに幾度も射精するのはむしろ望むところだし」 → "điều tôi mong muốn … tôi nghĩ" → **"điều anh mong muốn … anh nghĩ"** (×2).
- **1356** — 「今すぐにでもむしゃぶりつきたい」 → "tôi muốn ngấu nghiến nó" → **"anh muốn ngấu nghiến nó"**.
- **1365** — 「体にかけてほしいと」 → "muốn tôi bắn lên người" → **"muốn anh bắn lên người"**. (Tag `[そと,1]` trong JP là tag phía JP, VN đã chuẩn hoá — không phải lỗi.)
- **1374** — xem mục B (kèm gasp).
- **1376** — 「僕は、詳しくは知らんのだが」 → "Tôi không rành lắm" → **"Anh không rành lắm"**.
- **1377** — 「僕も好きだし、幸せだ」 → "Tôi cũng thích … tôi muốn" → **"Anh cũng thích … anh muốn"** (×2).
- **1381** — 「ふかみのたまごを――僕が、おいしくいただくことと」 → "tôi đang nghĩ … việc tôi, thưởng thức" → **"anh đang nghĩ … việc anh, thưởng thức"** (×2).
- **1391** — 「僕の方で制御する他に、手はなかろう」 → "tôi nghĩ không còn cách nào" → **"anh nghĩ không còn cách nào"**. ("tự mình kiểm soát" là phản thân, giữ nguyên.)
- **1393** — 「何かの書物で目にしたが」 → "tôi từng đọc được" → **"anh từng đọc được"**.
- **1398** — 「感じてほしい」 → "Tôi muốn em cảm nhận" → **"Anh muốn em cảm nhận"**.
- **1406** — 「うたた寝をしている僕にのしかかり」 → "đè lên người tôi lúc tôi đang ngủ gật … quần áo của tôi" → **"người anh … lúc anh đang ngủ gật … quần áo của anh"** (×3).
- **1408** — 「ふかみに一度確認しようと」 → "tôi muốn xác nhận lại" → **"anh muốn xác nhận lại"**.
- **1411** — 「ふかみに決めてほしい」 → "Tôi muốn Fukami quyết định" → **"Anh muốn Fukami quyết định"**.
- **1420** — 「僕も応えようとしたのだが」 → "tôi cũng đã định đáp ứng" → **"anh cũng đã định đáp ứng"**.
- **1432** — 「緩めて、くれないとっ」 → "nới lỏng ra, cho tôi" → **"cho anh"**. (Tên kéo dài "Fu——kami——" giữ nguyên — xem §5.)
- **1433** — 「ふかみ――僕も――限界、だっ」 → "tôi cũng——đến giới hạn" → **"anh cũng——đến giới hạn"**.
- **1445** — 「僕もふかみとキスしたかった」 → "Tôi cũng muốn hôn Fukami" → **"Anh cũng muốn hôn Fukami"**. (Sweep đánh dấu needs-file-audit; lỗi thật là đại từ.)
- **1452** — 「僕の部屋に入ったら、僕がうたたねをしていた？」 → "vào phòng tôi, thì thấy tôi đang ngủ gật?" → **"vào phòng anh, thì thấy anh đang ngủ gật?"** (×2).
- **1455** — 「僕が、射精、を」 → "nếu tôi … thời điểm … tôi, bắn tinh" → **"nếu anh … anh, bắn tinh"** (×2).
- **1486** — 「整理、したかった、だけ、だ」 → "tôi chỉ muốn, sắp xếp lại" → **"anh chỉ muốn, sắp xếp lại"**.

### B. Gasp っ bị mất (17 dòng)

Quy tắc: っ đứng một mình / sau ―― / sau …… / cả dòng → Ư. っ nhấn mạnh dính vào từ (わかっ, にっ, おまんこっ…) thì KHÔNG phải gasp — giữ nguyên.

- **1257 [双鉄]** — JP: 「っ――っ、くっ――ほぼ、間違いなく――」. VN cũ: "——, hự——gần như, chắc chắn—— tôi sẽ——…". Hai っ đầu dòng bị mất hẳn, chỉ còn dấu gạch. **Mới: "Ư――Ư, hự——gần như, chắc chắn—— anh sẽ——bắn tinh, vào bên trong mất thôi."** (kèm đại từ).
- **1259 [双鉄]** — JP: 「っ！　くっ！！」. VN cũ: "! Hự!!". **Mới: "Ư! Hự!!"**.
- **1260 [双鉄]** — JP: 「っ！！！！」. VN cũ: "!!!!". **Mới: "Ư!!!!"**. (Sweep bỏ sót.)
- **1261 [双鉄]** — JP: 「っ！！！！！！」. VN cũ: "!!!!!!". **Mới: "Ư!!!!!!"**. (Sweep bỏ sót.)
- **1262 [双鉄]** — JP: 「っ！？」. VN cũ: "!?". **Mới: "Ư!?"**. (Sweep bỏ sót.)
- **1268 [ふかみ]** — JP: 「ぁ――ふぁっ――来た！　先っぽ――っ――亀頭――」. VN cũ: "A——ha——vào rồi! Phần đầu——quy đầu——". Hai lỗi: ふぁっ → "ha" (mất âm ph) và っ sau ―― bị mất. **Mới: "A——phà——vào rồi! Phần đầu——Ư——quy đầu—— hình như, còn——to hơn——lúc nãy, nữa."** (Sweep bỏ sót cả hai.)
- **1288 [双鉄]** — JP: 「っ！」. VN cũ: "!". **Mới: "Ư!"**. (Sweep có, áp nguyên giá trị sweep.)
- **1339 [双鉄]** — JP: 「わかっ――っ！！！！？」. VN cũ: "Hiểu——!!!!?". っ thứ hai sau ―― là gasp (っ đầu là nhấn mạnh của わかっ). **Mới: "Hiểu——Ư!!!!?"**. (Sweep bỏ sót.)
- **1374 [双鉄]** — JP: 「どう、なるのだっ――っ！」. VN cũ: "thì——sẽ thế nào——!". **Mới: "thì——sẽ thế nào——Ư!"** (kèm đại từ ×2). (Sweep bỏ sót.)
- **1435 [双鉄]** — JP: 「ふかっ――っ！！！！！」. VN cũ: "Fuka——!!!!!". **Mới: "Fuka——Ư!!!!!"**. (Sweep bỏ sót.)
- **1438 [ふかみ]** — JP: 「もっと……っ――濃い、の、わたし――かぎたくなって」. VN cũ: "Em lại càng…… muốn——ngửi thấy mùi, đậm hơn, nữa." っ sau …… bị mất. **Mới: "Em lại càng……Ư——muốn——ngửi thấy mùi, đậm hơn, nữa."** (Sweep bỏ sót.)
- **1613 [monologue]** — JP: 「[だ,1]射精したて一番の精液は、もはや子宮に呑まれてしまった。\nが、今からでも、ふかみの体に注ぐためっ――っ！？！」. VN cũ: "…để rót lên cơ thể Fukami——!?". **Mới: "…để rót lên cơ thể Fukami——Ư!?"**. (Sweep có, áp nguyên giá trị sweep. Lưu ý: cột JP của sweep ở mục này bị sai — nó ghi JP của key 1681 ("腰へと添えていた指を…") thay vì JP của 1613; nhưng old_vn/fix của sweep khớp đúng VN của 1613, đã kiểm chứng lại với JP bộ TỐT — trailing gasp có thật. Ngược lại, chính vì JP bị lấy nhầm mà 1681 không có mục sweep nào dù cũng mất gasp — xem dưới.)
- **1651 [monologue]** — JP: 「僕はうたた寝を――っ！？」. VN cũ: "…mình đang ngủ gật mà——!?". **Mới: "…mình đang ngủ gật mà——Ư!?"**. (Sweep có, áp nguyên. "mình" trong độc thoại này giữ nguyên — xem §5.)
- **1681 [monologue]** — JP: 「ふかみの体全部を腕ごと僕へと引き寄せっ――っ！！」. VN cũ: "…Kéo toàn bộ cơ thể Fukami cùng với cánh tay về phía tôi——!!". **Mới: "…về phía tôi——Ư!!"**. (Sweep KHÔNG có mục này — JP của nó đã bị ghi nhầm sang mục 1613. Audit tự phát hiện.)
- **1682 [monologue]** — JP: 「ふかみが上昇するタイミングで――っ！！！？」. VN cũ: "…và đúng lúc Fukami nâng người lên——!!!?". **Mới: "…nâng người lên——Ư!!!?"**. (Sweep bỏ sót.)
- **1780 [monologue]** — JP: 「可愛らしいパンツをするする脱ぎ捨てていく――っ！？」. VN cũ: "…cởi bỏ chiếc quần lót dễ thương——!?". **Mới: "…cởi bỏ chiếc quần lót dễ thương——Ư!?"**. (Sweep có, áp nguyên.)
- **1835 [monologue]** — JP: 「復活祭の兎といえば――っ！」. VN cũ: "Nhắc đến thỏ Phục Sinh thì——!". **Mới: "Nhắc đến thỏ Phục Sinh thì——Ư!"**. (Sweep có, áp nguyên.)

### C. SFX fa/fu — mất âm đầu "ph" (21 dòng)

Gemini dịch các tiếng thở ふぁ/ふあ/ふぇ thành "Ha"/"Hả"/"fu" — mất phụ âm đầu (cùng mẫu lỗi đã ghi ở file hibiki07). Quy tắc đã chốt: ふぁ → "phà", ふあ → "phù", ふぇ → "phuê", ふやぁ → "phuya", không bao giờ romanisation.

- **1223 [ふかみ]** — JP: 「ふ、ぁ――」. VN cũ: "——fu, a——". **Mới: "——phù, a——"**. (ふ tách nhịp bằng 、, vẫn phải giữ âm ph.)
- **1233 [ふかみ]** — JP: 「ふぁっ――しゅごい！」. VN cũ: "Ha——tuyệt quá!". **Mới: "Phà——tuyệt quá!"**.
- **1252 [ふかみ]** — JP: 「ふぇ？――あ！」. VN cũ: "Hả? ——A!". **Mới: "Phuê? ——A!"**.
- **1254 [ふかみ]** — JP: 「ふぇっ？」. VN cũ: "Hả? A——a!". **Mới: "Phuê? A——a!"**.
- **1267 [ふかみ]** — JP: 「ぁ――あっ――あんっ――ふあっ――あっ――あ――」. VN cũ: "A——a——an——ha——a——a——". **Mới: "A——a——an——phù——a——a——"**.
- **1268 [ふかみ]** — xem mục B (kèm gasp).
- **1270 [ふかみ]** — JP: 「あっ――ふあっ――双鉄、おにいさんの、指――」. VN cũ: "A——ha——ngón tay, của anh Soutetsu——". **Mới: "A——phù——ngón tay, của anh Soutetsu——"**.
- **1283 [ふかみ]** — JP: 「あっ！　んっ！　きゅっ！！　あっ！　あっ！ふあっ！」. VN cũ: "A! Ưm! Kyu!! A! A! Ha!". **Mới: "A! Ưm! Kyu!! A! A! Phù!"**.
- **1379 [ふかみ]** — JP: 「――ふ、あ」. VN cũ: "——fu, a.". **Mới: "——phù, a."**.
- **1457 [ふかみ]** — JP: 「ふぁっ――あっ――きもち、いい――」. VN cũ: "Ha——a——sướng, quá——". **Mới: "Phà——a——sướng, quá——"**.
- **1458 [ふかみ]** — JP: 「はっ――あっ――ふ、あっ――」. VN cũ: "Ha——a——fu, a——anh——Soutetsu——". **Mới: "Ha——a——phù, a——anh——Soutetsu——"**. (はっ → "Ha" giữ nguyên — は đọc "ha" là đúng.)
- **1460 [ふかみ]** — JP: 「は……ぁっ――ふぁぅ……んっ――」. VN cũ: "Ha…… a——hau…… ưm——". **Mới: "Ha…… a——phàu…… ưm——"**. (ふぁぅ = ふぁ + ぅ → "phàu"; "hau" mất âm f.)
- **1461 [ふかみ]** — JP: 「ふあっ……あ……う……」. VN cũ: "Ha…… a…… ư……". **Mới: "Phù…… a…… ư……"**.
- **1463 [ふかみ]** — JP: 「ふあっ――ンッ――うれしい――」. VN cũ: "Ha——ưm——vui quá——". **Mới: "Phù——ưm——vui quá——"**.
- **1464 [双鉄]** — JP: 「ふぁっ！　あっ！　あっ！　あっ！」. VN cũ: "Ha! A! A! A!". **Mới: "Phà! A! A! A!"**.
- **1465 [ふかみ]** — JP: 「ふああっ！」. VN cũ: "Haa!". **Mới: "Phùaa!"**. (Theo tiền lệ h2: ふああああああんっ → "Phùaaaaaan" — ふ → "Phù", mỗi あ → một "a".)
- **1467 [ふかみ]** — JP: 「ふぁ！　あっ！　すごい！」. VN cũ: "Ha! A! Tuyệt quá!". **Mới: "Phà! A! Tuyệt quá!"**.
- **1468 [ふかみ]** — JP: 「ふぁっ！　あっ！　そうてつ！」. VN cũ: "Ha! A! Soutetsu! Anh! A!". **Mới: "Phà! A! Soutetsu! Anh! A!"**.
- **1469 [ふかみ]** — JP: 「ふぁっ！　急にっ！」. VN cũ: "Ha! Đột nhiên!". **Mới: "Phà! Đột nhiên!"**.
- **1471 [ふかみ]** — JP: 「ふぁっ！　ここっ――」. VN cũ: "Ha! Chỗ này——". **Mới: "Phà! Chỗ này——"**.
- **1472 [ふかみ]** — JP: 「ふあっ！　そうてつ、おにいさんの、おちん、ちんっ」. VN cũ: "Ha! Dương, vật, của anh Soutetsu". **Mới: "Phù! Dương, vật, của anh Soutetsu"**.

### D. SFX đếm nguyên âm dài (8 dòng)

Công thức đã chốt: số nguyên âm VN = 1 + số う/ぅ trong JP (áp cho token rên/SFX dùng cùng nguyên âm kéo dài; xem §5 về các token giữ phong cách khác).

- **1224 [ふかみ]** — JP: 「ひゅぁぁぁぁぁぁぁっぁぁぁぁぁぁぁっぁぁぁん！！」 (17 âm ぁ). VN cũ: "Hyuaaaaaaaaaan!!" (10 âm a — thiếu 7). **Mới: "Hyuaaaaaaaaaaaaaaaaan!!"** (17 âm a; tiền lệ 00common02 key 2016: ぴゃ + 7 a → VN 7 a).
- **1279 [ふかみ]** — JP: 「きゃふうううううううっ！！」 (ふ + 7 う → 8 nguyên âm u). VN cũ: "Kyafuuu!!" (3 u). **Mới: "Kyafuuuuuuuu!!"** (8 u).
- **1310 [ふかみ]** — JP: 「んっ！　ゅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅんんっ！」 (ゅ + 15 ぅ → 16 u). VN cũ: "Ưm! Yuuuuuuuuuuuuuun!" (14 u — thiếu 2). **Mới: "Ưm! Yuuuuuuuuuuuuuuuun!"** (16 u).
- **1920 [monologue]** — JP: （ぐぢゅぅぅぅぅぅぅぅぅぅぅぅぅっ！――ごりゅっ！） (ぐぢゅ + 12 ぅ → 14 u). VN cũ: "(Guchuuuuuu! ——Cụp!)" (6 u). **Mới: "(Guchuuuuuuuuuuuuu! ——Cụp!)"** (14 u).
- **1949 [monologue]** — JP: （きゅうううっ！！　きゅっ！） (きゅ + 3 う → 4 u). VN cũ: "(Kyuuu!! Kyu!)" (3 u). **Mới: "(Kyuuuu!! Kyu!)"** (4 u).
- **1966 [monologue]** — JP: （きゅううううううっっっ！！） (きゅ + 6 う → 7 u). VN cũ: "(Kyuuu!!)" (3 u). **Mới: "(Kyuuuuuuu!!)"** (7 u).
- **1967 [monologue]** — JP: （ぎちゅちゅっ！　きゅうっ！　きゅうんっ！！）. Token 2: きゅうっ → 2 u, VN cũ "Kyu" chỉ 1 u. **Mới: "(Gichuchu! Kyuu! Kyuun!!)"**. (Token 1 "Gichuchu" và token 3 "Kyuun" đã đúng số âm.)
- **1968 [monologue]** — JP: （きゅんっ！） (きゅ + ん → 1 u). VN cũ: "(Kyuun!)" (2 u — thừa 1). **Mới: "(Kyun!)"**. (Đối chiếu 1949 token 2 きゅっ → "Kyu!" đúng 1 u, và 1967 token 3 きゅうんっ → "Kyuun" đúng 2 u.)

### E. SFX mất tiếng thở + thuật ngữ (3 dòng)

- **1196 [双鉄] (sfx)** — JP: 「だが――ぁっ――このまま、で、はっ――」. VN cũ: "Nhưng——a——cứ thế này, thì——" — tiếng thở はっ cuối dòng bị mất hẳn. **Mới: "Nhưng——a——cứ thế này, thì——ha——"**. (はっ → "ha" theo tiền lệ: 1458 はっ → "Ha", 1462 はぁっ → "Ha".)
- **1669 [monologue] (terminology)** — JP: 「もうぐちょぐちょのおまんこに、勃起をぐりぐりめり込ませる。」. VN cũ: "…vào cái lồn đã ướt sũng." **Mới: "…vào cái âm đạo đã ướt sũng."** (おまんこ được dịch "âm đạo" 27 lần trong file; "lồn" chỉ xuất hiện 2 lần — chuẩn hoá cho nhất quán.)
- **1731 [monologue] (terminology)** — JP: 「蕩ける小さなおまんこで、僕の勃起を飲み込んでくる！」. VN cũ: "…và dùng cái lồn nhỏ bé đang tan chảy nuốt chửng sự cương cứng của tôi!" **Mới: "…và dùng cái âm đạo nhỏ bé đang tan chảy nuốt chửng sự cương cứng của tôi!"**. (Cùng lý do 1669.)

## 4. Kiểm chứng sweep っ

Sweep `sweep-raw-gasp-wrong.json` có 13 mục cho file này:

| Key | Loại sweep | Kết quả kiểm chứng |
|---|---|---|
| 1288 | lost-gasp-whole | Đúng — áp nguyên fix "Ư!" |
| 1613 | lost-gasp-trailing | Đúng về fix — áp nguyên "——Ư!?". **Nhưng cột JP của sweep ở mục này bị sai** (ghi JP của key 1681); đã kiểm chứng lại với JP bộ TỐT: trailing gasp có thật |
| 1651 | lost-gasp-trailing | Đúng — áp nguyên "——Ư!?" |
| 1780 | lost-gasp-trailing | Đúng — áp nguyên "——Ư!?" |
| 1835 | lost-gasp-trailing | Đúng — áp nguyên "——Ư!" |
| 1287 | already-rendered | Đúng — 「んうっ」 → "Ưm", không sửa |
| 1304 | already-rendered | Đúng — 「んきゅううっ」 → "Ưm kyuuu" (đủ 3 u), không sửa |
| 1400 | already-rendered | Đúng — すごいっ/んっ/ちゅっちゅっちゅ đều đã diễn, không sửa |
| 1384 | needs-file-audit | VN đúng hoàn toàn, không sửa |
| 1445 | needs-file-audit | Lỗi thật là đại từ (tôi → anh) — đã sửa ở §3A, không phải gasp |
| 1629 | needs-file-audit | VN đúng hoàn toàn (độc thoại "tôi" giữ theo quy tắc chung), không sửa |
| 1817 | needs-file-audit | VN đúng hoàn toàn, không sửa |
| 1967 | needs-file-audit | Có lỗi thật nhưng không phải gasp: đếm nguyên âm token 2 thiếu 1 (Kyu → Kyuu) — đã sửa ở §3D |

Sweep bắt đúng 5/17 gasp; 12 gasp còn lại do audit tự quét toàn bộ JP mà ra (1257, 1259, 1260, 1261, 1262, 1268, 1339, 1374, 1435, 1438, 1681, 1682). Đặc biệt 1681 mất gasp nhưng không có mục sweep vì JP của nó đã bị ghi nhầm vào mục 1613.

## 5. Các phán đoán giữ nguyên (không tính sai)

- **Độc thoại Soutetsu dùng "tôi": giữ.** Toàn bộ độc thoại (130 dòng monologue) dùng "tôi" theo quy tắc chung — quy tắc đại từ theo người nghe chỉ áp cho thoại 「」. Không dòng độc thoại nào dùng "anh" làm tự xưng (quét máy: 0).
- **1651 "mình đang ngủ gật": giữ.** Đây là độc thoại tự vấn lúc vừa tỉnh ngủ ("Đây là đâu? …A, không, mình đang ngủ gật mà——!?") — thuộc ngoại lệ "Soutetsu inner monologue = mình" (chỉ tự vấn cảm xúc). Bộ STALE viết "tôi đang ngủ gật" ở đây — bộ TỐT dùng "mình" là có chủ đích.
- **Tên kéo dài "Fu——ka…… mi." / "Fu——kami——" (1430, 1432) và "Fuka——" (1435): giữ.** JP cố tình kéo dài tên ふ――か……みっ / ふ――かみ――; VN tách âm tiết theo đúng nhịp JP. Không phải romanisation SFX.
- **ひゃ đầu tiếng rên giữ "Hyau" (1285, 1294): giữ.** Không có quy tắc đã chốt về ひゃ; tiền lệ h2: 1097 ひゃうっ → "Hyau" giữ, 1018/1019 ひゃうっ → "Ah"/"Á" giữ — SFX ngẫu hứng theo Hieu 19/11 22:05.
- **Kết thúc んっ → "n" (1277 んひゅんっ → "Ưm hyun", 1286 くひゅんっ → "Kuhyun", 1967 きゅうんっ → "Kyuun"): giữ.** Tiền lệ h2 key 1087: ふやんっ → "Phuyan" — っ sau ん không diễn thêm.
- **あっ/うあっ/くあっ → "A"/"Ua"/"Kua" (1225, 1226, 1258, 1295, 1296…): giữ.** Nguyên âm + っ cuối đã diễn bằng nguyên âm + dấu câu; tiền lệ 00common12: 2058 あっ → "A.", 2029 きゃっ!? → "Á, á!?".
- **はうっ → "Hau" (1281), はぁっ → "Ha" (1462), はっ → "Ha" (1458): giữ.** Tiền lệ 00common10: はぅ → "Hau" (2 nguyên âm).
- **っ nhấn mạnh dính từ (すごいっ, おまんこっ, わたしっ, だめっ, にっ――…): giữ.** Không phải gasp — VN diễn bằng chính từ đó.
- **1285 んううっ → "ưm": giữ.** Quy ước nhất quán của file cho tiếng rên đầu ん (1185/971/1301 んっ → "ưm"); không sửa thành "Ưưưm".
- **SFX ướt dài giữ phong cách lặp từ / lặp phụ âm (không sửa theo công thức đếm nguyên âm):** 1919 （じゅぶううううううううっ――ご、ちゅうううっっ） → "(Sùng sục sùng sục——cụp, sùng sục)"; 1939 （ずりゅううううううっっっっっっっ） → "(Sột soạttttt)"; 1940 （じゅぶううううううううううううっ） → "(Sùng sục sùng sục sùng sục!!!!!)"; 1941 （ずりゅうううっ――…） → "(Sột soạt——sùng sục——cụp)"; 1948 （ぎゅうううううううううううううううっっっっ） → "(Siếtttttt!!)"; 1954 （ずゆぶうううううううううううううっっっっ） → "(Phậpppppp!!)"; 1965 （ごちゅううううううっっ） → "(Phập——hự——sùng sục!)". Các dòng này diễn âm kéo dài bằng cách lặp từ/phụ âm chứ không kéo dài nguyên âm — độ dài âm thanh vẫn được giữ, chỉ khác chiến lược diễn. Tiền lệ giữ phong cách: 00common15 (đếm nguyên âm tiếng còi giữ), grand11 key 3970. Chỉ sửa các token nào VN đã chọn chiến lược kéo dài nguyên âm mà đếm sai (§3D).
- **1782 "Cô bé nhỏ nhắn" cho おまんこ: giữ.** Uyển ngữ tiếng Việt cho bộ phận sinh dục ("cô bé"), trong ngữ cảnh H-scene vẫn hiểu được; là lựa chọn diễn đạt có chủ đích, không sai nghĩa.
- **1417 "Vì vậy, nên mới có tư thế này, sao ạ?" (JP: だから、なんですか？この格好): giữ.** Lệch sắc thái nhẹ nhưng chấp nhận được.
- **1425 đảo trật tự mệnh đề (mùi tinh dịch đưa lên trước): giữ.** Nghĩa đầy đủ, không mất thông tin.
- **1441 せいり → "Sắp xếp": giữ.** せいり là rút gọn của 整理する; TW "理清、思緒" đồng thuận.
- **1406 "Migita System": không có trong file này.** Không có dòng nào chờ đợt thống nhất.
- **Chờ Hieu (không tự quyết):** không có câu hỏi thuật ngữ mới nào phát sinh từ file này. Các mục chờ sẵn (đợt thống nhất, B19) không liên quan file này.

## 6. Kiểm chứng kỹ thuật

- JSON `audit-lr-fukamih1-wrong.json`: 76 mục, dạng chuẩn list-of-dicts, key là chuỗi; jp/tw/old_vn khớp CSV3 bộ TỐT 76/76.
- Khối TOML `[script]` dưới đây parse OK bằng tomllib: 76 khóa, **0 sai lệch giá trị** so với JSON (so sánh chuỗi thô — tomllib parse `\\n` thành literal backslash-n đúng như CSV3).
- Diff-sanity: mỗi fix chỉ khác old VN ở đúng chỗ sửa (mỗi khối thay đổi ≤ 20 ký tự, tối đa 4 khối/dòng — các dòng 2 lỗi); không có viết lại lớn nào.
- **Lượt soát 2 (đọc lại toàn bộ 76 fix đối chiếu JP): 76/76 tái kiểm chứng, 0 bỏ, 0 sửa.** Không fix nào bị loại hay sửa lại trong lượt soát 2.

## 7. Khối TOML đã kiểm chứng (76 khóa)

```toml
[script]
"972" = "「……Anh cũng rất muốn nhuộm nó một cách thỏa thích.\\nNhưng đồng thời, chẳng phải Fukami còn một mong muốn khác sao.」"
"975" = "「……Xin lỗi. Vừa nãy còn nói những lời ra vẻ ta đây,\\nthế mà anh cũng mải mê làm tình——say đắm Fukami mất rồi.」"
"1187" = "「Không cần phải hoảng hốt. Cũng không cần phải chạy trốn.\\nAnh hoàn toàn không có ý định trách mắng Fukami đâu.」"
"1196" = "「Nhưng——a——cứ thế này, thì——ha——」"
"1200" = "「Lúc nãy, Fukami bảo——nếu anh báo sắp ra, em sẽ nhấc hông lên——\\nđể anh bắn lên toàn thân cơ mà.」"
"1201" = "「Em nói là muốn ngửi mùi hương mạnh nhất của anh——\\nmùi tinh dịch vừa mới bắn ra cơ mà.」"
"1220" = "「Hình như không thấy quả trứng nào thì phải……\\nChẳng lẽ anh là một đứa trẻ hư đến mức không được mang trứng đến sao.」"
"1223" = "「Nhưng——ưm——nếu vậy, thì tại sao——phù, a——\\nanh Soutetsu——a——lại cản, em, lại.」"
"1224" = "「Hyuaaaaaaaaaaaaaaaaan!!」"
"1233" = "「Phà——tuyệt quá! Thật nhiều——tinh dịch——ưm,\\nnóng hổi——phụt phụt, đánh, vào bụng.」"
"1252" = "「Phuê? ——A! Chuyện đó, hoàn toàn không có gì phải xin lỗi đâu ạ.\\nBởi vì——đúng không? Anh Soutetsu.」"
"1254" = "「Phuê? A——a! Lúc đó, không sao đâu. Em sẽ,\\nrút, dương vật, ra——rồi anh bắn tinh, tung tóe.」"
"1257" = "「Ư――Ư, hự——gần như, chắc chắn——\\nanh sẽ——bắn tinh, vào bên trong mất thôi.」"
"1259" = "「Ư! Hự!!」"
"1260" = "「Ư!!!!」"
"1261" = "「Ư!!!!!!」"
"1262" = "「Ư!?」"
"1267" = "「A——a——an——phù——a——a——」"
"1268" = "「A——phà——vào rồi! Phần đầu——Ư——quy đầu——\\nhình như, còn——to hơn——lúc nãy, nữa.」"
"1270" = "「A——phù——ngón tay, của anh Soutetsu——\\nthô ráp——thích quá——vừa to, vừa ấm.」"
"1279" = "「Kyafuuuuuuuu!!」"
"1283" = "「A! Ưm! Kyu!! A! A! Phù!\\nA! Không được! Em! Thế này, không được đâu!!」"
"1288" = "「Ư!」"
"1307" = "「Ưm——hự——a——.\\n……Mùi hương, đậm nhất, của anh——rốt cuộc, là mùi như thế nào.」"
"1310" = "「Ưm! Yuuuuuuuuuuuuuuuun!」"
"1325" = "「Trước khi trách mắng, thì\\nanh vẫn chưa nắm bắt được tình hình hiện tại.」"
"1328" = "「Trong chuyện này, dù Fukami có làm tới mức nào đi nữa,\\nanh cũng rất vui và cực kỳ hoan nghênh. Chuyện đó thì em không cần phải bận tâm đâu.」"
"1333" = "「Được bắn tinh nhiều lần vào Fukami mới là điều anh mong muốn.\\nVề mặt thể lực, anh nghĩ cũng hoàn toàn không có vấn đề gì.」"
"1339" = "「Hiểu——Ư!!!!?」"
"1356" = "「Rất đẹp, và đáng yêu. Nếu không phải đang ở tư thế này,\\nthì ngay bây giờ anh muốn ngấu nghiến nó.」"
"1365" = "「Bắn, bắn tinh ra ngoài——muốn anh bắn lên người——\\nhự, ha——hình như, em vừa mới nói vậy, mà nhỉ.」"
"1374" = "「Nếu anh——báo cho em biết——lúc anh sắp ra——\\nthì——sẽ thế nào——Ư!」"
"1376" = "「Anh không rành lắm——nó là thứ như thế nào vậy?\\nCái gọi là Thỏ Phục Sinh ấy.」"
"1377" = "「Anh cũng thích, và rất hạnh phúc. Vì vậy, anh muốn——\\nở gần Fukami hơn nữa. Muốn hòa quyện vào nhau.」"
"1379" = "「Em chỉ định một chút thôi, nên đã tháo cúc áo ở ngực ra……\\nƯm——không hiểu sao——lại không thể dừng lại được nữa——phù, a.」"
"1381" = "「Tóm lại, anh đang nghĩ xem cái nào thì tốt hơn——\\nGiữa việc anh, thưởng thức thật ngon lành——trứng của Fukami.」"
"1391" = "「Cái âm đạo tham lam này. Để không bị nuốt trọn toàn bộ tinh dịch,\\nanh nghĩ không còn cách nào khác ngoài việc tự mình kiểm soát.」"
"1393" = "「Chỗ thắt lại của quy đầu——phần đầu khấc, có hình dạng\\nđể vét tinh dịch đã bắn ra trước đó, anh từng đọc được ở cuốn sách nào đó thì phải.」"
"1398" = "「Hơn nữa, hơn nữa cơ. Anh muốn em cảm nhận nhiều hơn nữa.」"
"1406" = "「Nên em đã đè lên người anh lúc anh đang ngủ gật——\\nvà cởi quần áo của anh ra sao?」"
"1408" = "「Vì vậy, anh muốn xác nhận lại một lần xem Fukami chọn cái nào.」"
"1411" = "「Vì, vậy. Anh muốn Fukami quyết định.」"
"1420" = "「Đúng vậy nhỉ.\\nLúc đầu nghe em nói thế, anh cũng đã định đáp ứng rồi.」"
"1432" = "「Fu——kami——nới lỏng ra, cho anh——a!!」"
"1433" = "「Fukami——anh cũng——đến giới hạn, rồi!!!」"
"1435" = "「Fuka——Ư!!!!!」"
"1438" = "「Sau đó, mùi hương——mùi của anh Soutetsu, thoảng qua……\\nEm lại càng……Ư——muốn——ngửi thấy mùi, đậm hơn, nữa.」"
"1445" = "「Trùng hợp thật. Anh cũng muốn hôn Fukami.」"
"1452" = "「Nhưng khi vào phòng anh, thì thấy anh đang ngủ gật?」"
"1455" = "「Có rút ra được, không? Thật sự——nếu anh——\\nbáo cho Fukami——thời điểm——anh, bắn tinh.」"
"1457" = "「Phà——a——sướng, quá——sướng quá đi\\n——ưm——a——nhưng mà——nhưng mà——ưm…… a.」"
"1458" = "「Ha——a——phù, a——anh——Soutetsu——\\nưm——thế này——em——sốt ruột, lắm——a!」"
"1460" = "「Ha…… a——phàu…… ưm——ehehe——\\nanh Soutetsu——của em, anh Soutetsu của em.」"
"1461" = "「Phù…… a…… ư…… vậy, sao, ạ?」"
"1463" = "「Phù——ưm——vui quá——hạnh phúc quá——\\nấm áp quá——anh Soutetsu——em cảm nhận được, rất rõ.」"
"1464" = "「Phà! A! A! A!」"
"1465" = "「Phùaa! Đến rồi, đến rồi! Dương vật! Ưm——\\nĐóng dấu——ngoáy ngoáy——, vào tận cùng, bên trong——âm đạo.」"
"1467" = "「Phà! A! Tuyệt quá! Tử cung——âm đạo——\\ntinh trùng——thật nhiều, ực ực——em, đang nuốt.」"
"1468" = "「Phà! A! Soutetsu! Anh! A!\\nEm! Em! Âm đạo! Sắp, sắp!」"
"1469" = "「Phà! Đột nhiên! Đột nhiên, như vậy! Như vậy,\\nưm, hự! A! Mạnh quá! Mạnh quá đi!!」"
"1471" = "「Phà! Chỗ này——chỗ này, thích quá——ưm!!」"
"1472" = "「Phù! Dương, vật, của anh Soutetsu\\n——ưm! Âm đạo——âm đạo——đã lấp đầy, rồi.」"
"1486" = "「Không có gì——ưm…… a——chỉ là một thắc mắc rất đơn giản——\\nanh chỉ muốn, sắp xếp lại, một chút, thôi——」"
"1613" = "Dòng tinh dịch đầu tiên vừa bắn ra, đã bị tử cung nuốt chửng mất rồi.\\nNhưng, ngay từ bây giờ, để rót lên cơ thể Fukami——Ư!?"
"1651" = "Một giọng nói quen thuộc. Giọng của Fukami.\\nĐây là đâu? ……A, không, mình đang ngủ gật mà——Ư!?"
"1669" = "Đẩy hông từ dưới lên, và ấn mạnh sự cương cứng\\nvào cái âm đạo đã ướt sũng."
"1681" = "Những ngón tay đang đặt trên hông chuyển từ đỡ sang bấu chặt.\\nKéo toàn bộ cơ thể Fukami cùng với cánh tay về phía tôi——Ư!!"
"1682" = "Rút ra và bắn lên toàn thân. Để làm điều đó, tôi lệch nhịp thở,\\nvà đúng lúc Fukami nâng người lên——Ư!!!?"
"1731" = "Miệng thì bảo bắn lên người, nhưng Fukami lại nhanh chóng nhấc hông lên,\\nvà dùng cái âm đạo nhỏ bé đang tan chảy nuốt chửng sự cương cứng của tôi!"
"1780" = "Fukami hơi nhấc hông lên,\\nvà nhanh chóng cởi bỏ chiếc quần lót dễ thương——Ư!?"
"1835" = "Easter, là Lễ Phục Sinh nhỉ.\\nNhắc đến thỏ Phục Sinh thì——Ư!"
"1920" = "(Guchuuuuuuuuuuuuu! ——Cụp!)"
"1949" = "(Kyuuuu!! Kyu!)"
"1966" = "(Kyuuuuuuu!!)"
"1967" = "(Gichuchu! Kyuu! Kyuun!!)"
"1968" = "(Kyun!)"
```

## 8. Kiểm chứng cuối

- Khối TOML trên parse OK (tomllib), 76 khóa, 0 sai lệch giá trị so với JSON.
- JSON 76 mục, key chuỗi, jp/tw/old_vn khớp CSV3 bộ TỐT 76/76.
- Lượt soát 2: 76/76 tái kiểm chứng, 0 bỏ, 0 sửa.
- Tổng cộng sau file này: **84 file / 4.369 dòng sai** (cơ sở 83 file / 4.293 + 76 file này).

## Kết bài

File lr_ふかみh1_ふかみうさぎのたまご.txt.toml: 289 dòng đã đọc hết, **76 dòng sai (26,3%)** — cao hơn hẳn file chị em ふかみh2 (17,9%). Ba lỗi hệ thống: (1) Soutetsu tự xưng "tôi" trong **mọi** dòng thoại với Fukami (30 dòng, 39 lần — 0 dòng đã đúng); (2) tiếng thở fa/fu mất âm "ph" thành "Ha"/"Hả"/"fu" (21 dòng, tập trung ở cụm 1457–1472); (3) gasp っ bị mất (17 dòng, trong đó sweep chỉ bắt được 5, còn lại do quét toàn bộ JP mà ra — đáng chú ý sweep ghi nhầm JP của 1681 vào mục 1613, khiến 1681 không có mục sweep nào). Không có lệch dòng / xoay vòng / nhiễm chéo / mồ côi / chưa dịch / trùng key. Bộ CSV tốt là 11_Other (bộ 07_Nagi_Fukami STALE, chỉ khớp TOML 3/289). TOML không có bản trùng. Không có câu hỏi mới nào cần Hieu quyết từ file này.
