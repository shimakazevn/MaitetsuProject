# Audit — 稀咲h1_性生活.txt.toml (06_Kisaki)

- File: `06_Kisaki/稀咲h1_性生活.txt.toml` (TOML-2: `#U7a00#U54b2h1_#U6027#U751f#U6d3b.txt.toml`)
- Route: 06_Kisaki. Nội dung: 5 giờ sáng, Kisaki đánh thức Soutetsu đang ngủ gật trong phòng giám đốc chi nhánh sau buổi nhậu với ông Mototada (bố Kisaki); ông Mototada đã nói chuyện "đời sống vợ chồng hạnh phúc" với Soutetsu; Kisaki dạy Soutetsu về tình dục — cảnh H đầu tiên của hai người (oral, mất trinh, xuất tinh trong miệng rồi quan hệ), kết bằng nụ hôn và lời hẹn "cùng nhau học hỏi suốt đời".
- Đọc: **335/335 dòng** (keys 55–2096, section `script`), đọc từng dòng JP + TW + VN đối chiếu. CSV3 1 set duy nhất, key khớp tuyệt đối 335/335; VN khớp TOML ở 172/335 dòng, 163 dòng còn lại chỉ khác ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng — theo quy tắc, CSV3 là chuẩn cho fix list.
- **Sai: 38/335 (11,3%)**.
- Phân loại: đại từ 26 (Soutetsu "anh"→"tôi" / "em"→"cô" với Kisaki 15; Kisaki tự xưng "tôi"→"em" với Soutetsu 11), gasp 10 (cả 10 từ sweep, 1254 đã chỉnh số u), SFX 2 (1308 ぷえっ→"phuê", 1243 ぇあっ→"ea").
- **0 lệch dòng / 0 chuỗi xoay / 0 nhiễm chéo / 0 dòng mồ côi / 0 dòng chưa dịch / 0 khóa trùng.** Không có VN nào là lời thoại của file khác; không có VN lặp ở 2 key có JP khác nhau (các cặp trùng đều là SFX ngắn dùng chung: （Phụt!）×3, （Phụt）×3, （Phập――phập――phập――phập――）×3, 「Ừm」×2 — JP tương ứng cũng lặp/khớp nghĩa). Chỉ 1 dòng VN==TW: 1002 「…………」 (toàn dấu câu, không phải chưa dịch).
- TOML md5: `ac459e00d403158a8ecd05162a0194d0` — không có bản trùng (chỉ 1 file 稀咲h1_性生活 trong sources/toml2/; file lr_稀咲h1_おしおきとごほうび là file khác). `[selections]` rỗng ({}). `[characters]`: 1611 Soutetsu H, 1812 Kisaki. 1 tag `%l` duy nhất trong file (1325, gloss 真摯→"nghiêm túc" — JP có ruby [しんし,1]真摯 nên tag hợp lệ, giữ nguyên).
- Cơ sở tổng: **150 file / 6.658 dòng sai** (đã kiểm chứng trực tiếp với dòng tổng cuối của ROUTE-AUDIT.md — khớp với brief, không cần rebase).

## §1. Đại từ — lỗi hệ thống, nhưng CHỈ sửa phần đã khóa

### 1a. Soutetsu "anh"→"tôi" / "em"→"cô" với Kisaki (15 dòng — SỬA)

Soutetsu tự xưng "anh" 12 dòng và gọi Kisaki "em" 5 dòng (gộp 15 dòng), trong khi "tôi" đã đúng ở 8 dòng và "cô" đã đúng ở 3 dòng (1287, 1236, 988) — file KHÔNG nhất quán nội bộ. Theo quy tắc đã khóa (Soutetsu là "tôi" với Kisaki, gọi cô ấy "cô"; tiền lệ Grand 11 2173/2347, parent-verified), cả 15 đều sai. Người nghe đều là Kisaki (toàn bộ thoại 双鉄 trong file chỉ nói với Kisaki; chỉ có 2 nhân vật lên tiếng). Độc thoại Soutetsu dùng "tôi" đúng toàn file, không sửa.

### 1b. Kisaki tự xưng "tôi"→"em" với Soutetsu (11 dòng — SỬA)

Kisaki tự xưng "tôi" 11 dòng trong khi "em" đã đúng ở 19 dòng — file KHÔNG nhất quán nội bộ (không chia theo cảnh: cả "tôi" lẫn "em" đều xuất hiện cả ở đoạn trò chuyện đầu file lẫn trong cảnh H). Theo tiền lệ đã merge lr_稀咲h1 + h3 (Kisaki "em" với Soutetsu; Grand 11 parent đã loại 7 fix đổi "em"→"tôi" vì sai), 11 dòng "tôi" là sai. Lưu ý: câu hỏi đang chờ của file 02 ("Kisaki 'tôi' hay 'em'") áp dụng cho các file họp/công việc NHẤT QUÁN nội bộ theo "tôi" (16/16) — file này không thuộc trường hợp đó (nội bộ mâu thuẫn, cảnh H, đa số "em") nên sửa theo quy tắc đã khóa.

### 1c. Kisaki gọi Soutetsu "anh Soutetsu"/"anh" (41 dòng — GIỮ NGUYÊN, cờ chờ Hieu)

Kisaki gọi Soutetsu "anh Soutetsu" 34 dòng + "anh" đứng riêng 7 dòng + 1 dòng ngọng (1407 "anh Houtehu" — lời nói ngọng khi miệng đầy, không tính) — tổng 41 dòng, nội bộ file NHẤT QUÁN (0 lần "cậu"). Đây chính là câu hỏi đang chờ Hieu từ file 01/02 ("Kisaki 'tôi' hay 'em' / 'anh Soutetsu' hay 'cậu'"), đã cờ lại ở h3 (33 dòng giữ nguyên, parent chấp nhận khi gộp). Tiền lệ "cậu"/tên trần (Common 14, Grand 11 1664/2459/2617, hachiroku02 2311) đều từ ngữ cảnh họp/nhóm/công việc — trong khi file này là cảnh H thân mật, "anh" có thể đúng theo ngữ cảnh (giả thuyết file 02: thân mật → "em"/"anh", công việc → "tôi"/"cậu"). KHÔNG tự đổi hàng loạt 41 dòng khi Hieu chưa chốt — giữ nguyên toàn bộ, cờ ở đây + snippet. Các dòng 1416/1204/1373/1357/1462/1398/1376 chỉ sửa tự xưng "tôi"→"em", vẫn giữ "anh Soutetsu" (cặp "em/anh Soutetsu" giống hệt h3 đã merge).

## §2. Gasp っ — sweep kiểm chứng

Sweep có **13 mục** cho file này (đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`): 12 fix + 1 already-rendered (1012 「……っ」→"……Ư." đã diễn, giữ). 12 fix đều kiểm chứng đúng vs JP, nhưng có 2 điểm chỉnh:

- **1254: số u SỬA LẠI.** Sweep giữ 7 u của Gemini ("I hyuuuuuuuƯƯ"). Đếm lại độc lập: JP いっひゅうぅぅぅぅぅぅぅ = ひゅ(1 u) + う(1) + ぅ(7) = **9 u** theo công thức độ dài nguyên âm (tiền lệ moan lr稀咲追加h 1855: ひゅ1+う8=9u, đã đếm lại độc lập). Fix: "I hyuuuuuuuuuƯƯ!!!" (9 u, đã đếm bằng máy).
- **1316/1366: gộp với fix đại từ** (xem §1a) — sweep chỉ sửa phần っ, audit sửa thêm "anh"→"tôi".
- Các fix còn lại áp nguyên sweep: 1306 (3 dấu ~ khớp JP), 1310 (6 dấu ~ khớp), 1323 (5 dấu ~ khớp), 1486/1487/1488 (gasp cả dòng), 1492 (5 dấu ~ khớp), 1494 (10 dấu ~ khớp), 1650 (gasp cuối dòng độc thoại).

Quét máy bổ sung toàn bộ dòng JP chứa っ: **không còn gasp sót**. Các っ còn lại đều đã diễn hoặc thuộc quy ước toàn dự án: あっ→"A" (1270, 1264, 1261, 1293...), ああっ→"a" (1261), はうっ/はぅっ→"Hau" (1274 — quy ước dự án, tiền lệ h7/h8 + Common 12), んっ→"Ưm" (1282, 1311, 1285...), っ nhấn mạnh dính từ nội dung (1330 夫婦生活っ→".", 1269 長っ→"dài", 1299 かなっ→"nhỉ", 2077 子宮っ→"tử cung", 1442/1262 稀咲っ→"Kisaki"), SFX đã diễn (ちゅっ→"Chụt", ごくっ→"ực", ずぶっ/ずっ→"Phập", びゅっ→"Phụt", （しゅこっ）→"Tuốt" v.v.), っ――→―― (dashes diễn cut-off), ひあ/ひゃ family giữ ngẫu hứng (ひゃっ→"Hya"/"hya", ひあっ→"hya", ひゃんっ→"hyan" — Hieu 20/11, không thống nhất), fa/fu đã romaji (ふあっ→"fua", 1460/1466 — fallback romaji đã áp dụng, xem §3).

## §3. SFX / rên — romaji fallback đã áp dụng

- **1308** ぷえっ→"phuê!" (tiền lệ ふぇっ→"Phuê"; VN cũ "phù!" sai nguyên âm e→u).
- **1243** ぇあっ→"ea" (romaji fallback cho rên; "đừng để mất âm" — VN cũ "a" làm mất âm ぇ).
- Đã romaji sẵn, giữ nguyên: ふあっ→"fua" (1460, 1466 — tiền lệ moan ふかみh1 989 "Fua!"), ひゃっ→"hya" (1242, 1243, 1244, 1460), ひあっ→"hya" (1260, 1283), くはっ→"kuha" (1280, 1306), きゅ→"kyu" (1284, 1243).
- **1244 giữ nguyên, cờ nhỏ:** しゅごっ/すごっ→"tuyệt――tuyệt quá" — TW cũng diễn thành 好多 ("nhiều lắm"), JP しゅごっ mơ hồ (âm đẩy / biến thể すごい nói ngọng); VN theo TW, không sửa. Tiền lệ h3 2155 "Tuyệt quá!" cũng đang cờ cho Hieu.

## §4. Giữ nguyên (không tính sai)

- **1407** — lời nói ngọng khi miệng đầy (ひひひょ、ほーへふっ…): "anh Houtehu" là một phần của cách diễn ngọng, không phải xưng hô — giữ nguyên (tiền lệ h3 2238 "Anh Houhehu").
- **1275** 「っあっ！」→"A!" — っ đầu dòng mất nhưng âm あ đã diễn; quy ước dự án cho あっ→"A". Giữ (ranh giới).
- **1255** 「ぃあっ」→"Ư a" — っ diễn thành Ư, あ diễn thành "a"; ぇ/ぃ lướt mất nhưng cặp Ư+a giữ được hình 2 âm. Giữ (phương án romaji "Ia" để moan-fix loop xem xét nếu muốn).
- **ふっ→"fu"** (1309, 1283, 1223, 1244, 1466 — 5 dòng): nhất quán nội bộ file; ふ đã diễn, chỉ mất ngắt っ — cùng logic với はぅっ→"Hau" đã giữ. Giữ.
- **Chuỗi âm miệng** (1297, 1277, 1279: ちゅむっ→"chu mu", あむっ/あムッ→"a mu", はむっ→"ha mu", ちゅっ→"chụt"): っ cuối các âm miệng đã diễn bằng phụ âm cuối hoặc bỏ khi từ Việt đã kết thúc bằng nguyên âm — quy ước file, nhất quán. Giữ.
- **SFX dài bị rút gọn** (2042, 2045, 2043...): （ずぶうううううううううううっ――ごっ！！！）→"（Phập――bịch!!!）" — độ dài JP bị rút gọn nhưng file dùng "Phập"/"Phụt" nhất quán cho mọi SFX đẩy; không sửa (quy ước file).
- **Độc thoại "em ấy" vs "cô ấy"** (1692/1624/1759/1943 "em ấy" vs 1642 "cô ấy"): ngôi thứ ba trong độc thoại, không thuộc quy tắc xưng hô (quy tắc chỉ chi phối thoại trực tiếp) — giữ nguyên, ghi nhận mâu thuẫn nhỏ để đợt thống nhất xem xét.
- **1224** "hai người" (dọn dẹp): suy ra từ ngữ cảnh (Mototada + Soutetsu, xem 1390) — giữ.
- **1239** "tôi, chắc chắn." — JP きっと bỏ lửng, VN giữ nguyên dạng cụt — giữ (không bịa phần tiếp).
- **1461** だから bỏ lửng: JP だか、らっ cụt câu, VN "không, sao――đâu" giữ được nghĩa + độ cụt — giữ.
- **2077** （子宮――子宮っ）→"（Tử cung――tử cung）": っ nhấn mạnh dính từ nội dung, TW cũng không diễn — giữ.

## §5. Chi tiết từng dòng sai (38)


### 1189 [双鉄H] — pronoun

JP: 「何も、無理して飲まずとも」
TW: 「不用逼著自己吞下去的」
Cũ: 「Em không cần phải cố nuốt xuống đâu」
Mới: 「Cô không cần phải cố nuốt xuống đâu」
→ Soutetsu gọi Kisaki "em"→"cô" (quy tắc đã khóa; tiền lệ Grand 11 2173).

### 1204 [稀咲] — pronoun

JP: 「ボクが相手じゃ、ピンと来ないだなんて」
TW: 「你面對的可是我，怎麼能一點感覺都沒有」
Cũ: 「Đối phương là tôi mà, anh lại bảo không có cảm giác gì sao.」
Mới: 「Đối phương là em mà, anh lại bảo không có cảm giác gì sao.」
→ Kisaki tự xưng ボク với Soutetsu: "tôi"→"em"; "anh" (gọi Soutetsu) GIỮ NGUYÊN theo câu hỏi đang chờ Hieu.

### 1217 [稀咲] — pronoun

JP: 「それにしたって、随分とヘンな電話だと思っていたんだ。\n夜の夜中に、『普段より二時間は早く出勤しろ』なんて」
TW: 「其實我還覺得電話的內容奇怪呢。大半夜的電話叫我『比平時早兩小時來上班』」
Cũ: 「Dù vậy, tôi cũng thấy cuộc gọi đó khá kỳ lạ.\nNửa đêm nửa hôm lại bảo 『hãy đi làm sớm hơn bình thường hai tiếng』.」
Mới: 「Dù vậy, em cũng thấy cuộc gọi đó khá kỳ lạ.\nNửa đêm nửa hôm lại bảo 『hãy đi làm sớm hơn bình thường hai tiếng』.」
→ Kisaki tự xưng ボク với Soutetsu: "tôi"→"em" (tiền lệ lr_稀咲h1/h3; file này "em" 19 dòng vs "tôi" 11 dòng, không chia theo cảnh).

### 1243 [稀咲] — sfx

JP: 「きゅ――ん――ひゃっ――ぇあっ――あっ――」
TW: 「呀――嗯――呀――啊――啊――」
Cũ: 「Kyu――ưm――hya――a――a――」
Mới: 「Kyu――ưm――hya――ea――a――」
→ JP ぇあっ: ぇ+あ → "ea" (romaji fallback cho rên; "đừng để mất âm"); VN cũ "a" làm mất âm ぇ.

### 1254 [稀咲] — gasp

JP: 「いっひゅうぅぅぅぅぅぅぅっっ！！！」
TW: 「咿呀啊啊啊啊！！！」
Cũ: 「I hyuuuuuuuっっ!!!」
Mới: 「I hyuuuuuuuuuƯƯ!!!」
→ Sweep raw-tsu: っっ thô trong VN → ƯƯ. Đếm lại độc lập số u: JP いっひゅうぅぅぅぅぅぅぅ = ひゅ(1u) + う(1) + ぅ(7) = 9 u (công thức độ dài nguyên âm; tiền lệ moan lr稀咲追加h 1855: ひゅ1+う8=9u) — bản sweep giữ 7 u của Gemini là SAI, đã sửa thành 9 u.

### 1288 [双鉄H] — pronoun

JP: 「ああ――起こしてくれていたのか」
TW: 「嗯――是你叫醒我的吧」
Cũ: 「À——em đã đánh thức anh sao.」
Mới: 「À——cô đã đánh thức tôi sao.」
→ Soutetsu với Kisaki là "tôi" (JP 僕), gọi Kisaki "cô" — quy tắc đã khóa; VN cũ "em/anh" sai cả hai chiều (tiền lệ Grand 11 2173/2347).

### 1303 [稀咲] — pronoun

JP: 「うん。まぁ、ボクも同じだ。\nいずれ……遠からず……近いうちに、みたいな感じにね」
TW: 「嗯。其實我也一樣。感覺……很快就會了……應該不會離得太遠的」
Cũ: 「Ừm. Chà, tôi cũng vậy.\nMột ngày nào đó…… không xa…… kiểu như trong tương lai gần vậy.」
Mới: 「Ừm. Chà, em cũng vậy.\nMột ngày nào đó…… không xa…… kiểu như trong tương lai gần vậy.」
→ Kisaki tự xưng ボク với Soutetsu: "tôi"→"em" (tiền lệ lr_稀咲h1/h3).

### 1306 [稀咲] — gasp

JP: 「んきゅ――くはっ――んあっ――～～～っ！！！」
TW: 「嗯呀――嗚啊――嗯啊――～～～！！！」
Cũ: 「Ưm kyu――kuha――ưm a――~~~っ!!!」
Mới: 「Ưm kyu――kuha――ưm a――~~~Ư!!!」
→ Sweep raw-tsu: っ thô cuối dòng → Ư (JP ～～～っ; 3 dấu ~ khớp JP).

### 1308 [稀咲] — sfx

JP: 「んくっ――ごくっ――んっ――ごくっ、んっ――\nぷえっ！」
TW: 「嗯唔――咕嘟――嗯――咕嘟、嗯――噗哈！」
Cũ: 「Ưm――ực――ưm――ực, ưm――\nphù!」
Mới: 「Ưm――ực――ưm――ực, ưm――\nphuê!」
→ JP ぷえっ: ぷ+え+っ → "phuê" (tiền lệ ふぇっ→"Phuê"); VN cũ "phù!" sai nguyên âm (e→u).

### 1310 [稀咲] — gasp

JP: 「んぷっ！？　ぷっ――ん～～～～～～っ」
TW: 「嗯唔！？　噗――嗯～～～～～～」
Cũ: 「Ưm!? Phụt――ưm~~~~~~っ」
Mới: 「Ưm!? Phụt――ưm~~~~~~Ư」
→ Sweep raw-tsu: っ thô cuối dòng → Ư (JP ん～～～～～～っ; 6 dấu ~ khớp JP).

### 1316 [双鉄H] — pronoun

JP: 「ああ、僕もだ。\n――僕も……っっ――イくっ」
TW: 「嗯，我也想。――我也……――要射了」
Cũ: 「Ừm, anh cũng vậy.\n――Anh cũng……っっ――ra đây」
Mới: 「Ừm, tôi cũng vậy.\n――Tôi cũng……ƯƯ――ra đây」
→ Hai lỗi một dòng: (1) Soutetsu với Kisaki "anh"→"tôi" (2 lần, JP 僕もだ/僕も); (2) gasp っっ thô trong VN → ƯƯ (sweep raw-tsu, đã kiểm chứng vs JP).

### 1323 [稀咲] — gasp

JP: 「ん～～～～～っ――んっ――んうっ――ごくんっ！」
TW: 「嗯～～～～～――嗯――嗯唔――咕嚕！」
Cũ: 「Ưm~~~~~っ――ưm――ưm――ực!」
Mới: 「Ưm~~~~~Ư――ưm――ưm――ực!」
→ Sweep raw-tsu: っ thô sau ~~~~~ → Ư (JP ん～～～～～っ; 5 dấu ~ khớp JP).

### 1357 [稀咲] — pronoun

JP: 「性は――セックスは嫌悪をするべきものじゃない。\nボクが、双鉄にそれを教えてあげる」
TW: 「性事――做愛不是什麼應該厭惡的事。我會手把手教會你這一點的」
Cũ: 「Tình dục——tình dục không phải là thứ đáng bị ghê tởm.\nTôi sẽ dạy cho anh Soutetsu điều đó.」
Mới: 「Tình dục——tình dục không phải là thứ đáng bị ghê tởm.\nEm sẽ dạy cho anh Soutetsu điều đó.」
→ Kisaki tự xưng ボク với Soutetsu: "tôi"→"em"; "anh Soutetsu" GIỮ NGUYÊN theo câu hỏi đang chờ Hieu.

### 1361 [双鉄H] — pronoun

JP: 「僕が――稀咲に？」
TW: 「我――告訴你嗎？」
Cũ: 「Anh――dạy cho Kisaki sao?」
Mới: 「Tôi――dạy cho Kisaki sao?」
→ Soutetsu với Kisaki: "anh"→"tôi" (JP 僕が).

### 1364 [双鉄H] — pronoun

JP: 「僕もだ――僕のセックスも、稀咲からしか教われないし、\n教わりたくない」
TW: 「我也是――我的做愛只有稀咲能教會，我也不想別人來教」
Cũ: 「Anh cũng vậy――tình dục của anh, cũng chỉ có thể học từ Kisaki,\nvà anh cũng không muốn học từ ai khác」
Mới: 「Tôi cũng vậy――tình dục của tôi, cũng chỉ có thể học từ Kisaki,\nvà tôi cũng không muốn học từ ai khác」
→ Soutetsu với Kisaki: "anh"→"tôi" (3 lần, JP 僕).

### 1366 [双鉄H] — pronoun

JP: 「僕もだ――稀咲っ！　もう少し、でっ――っ！」
TW: 「我也是――稀咲！　再忍耐一小――！」
Cũ: 「Anh cũng vậy――Kisaki! Một chút, nữa thôi――っ!」
Mới: 「Tôi cũng vậy――Kisaki! Một chút, nữa thôi――Ư!」
→ Hai lỗi một dòng: (1) Soutetsu với Kisaki "anh"→"tôi" (JP 僕もだ); (2) gasp っ thô trong VN → Ư (sweep raw-tsu, đã kiểm chứng vs JP でっ――っ).

### 1369 [稀咲] — pronoun

JP: 「あんなに激しく感じたり、実際にするのかどうか――\nそこはフィクションなのかな？　とも思ってたけど……」
TW: 「我也會覺得，事實上真會那麼有感覺嗎――或許全是演出來的呢？　想是會這麼想……」
Cũ: 「Cảm thấy mãnh liệt như vậy, không biết thực tế có làm thế không——\nhay đó chỉ là hư cấu nhỉ? Tôi cũng từng nghĩ thế nhưng……」
Mới: 「Cảm thấy mãnh liệt như vậy, không biết thực tế có làm thế không——\nhay đó chỉ là hư cấu nhỉ? Em cũng từng nghĩ thế nhưng……」
→ Kisaki tự xưng ボク với Soutetsu: "tôi"→"em" (tiền lệ lr_稀咲h1/h3).

### 1373 [稀咲] — pronoun

JP: 「わかっているよ、双鉄」
TW: 「我懂的，雙鐵」
Cũ: 「Tôi hiểu mà, anh Soutetsu.」
Mới: 「Em hiểu mà, anh Soutetsu.」
→ Kisaki tự xưng ボク với Soutetsu: "tôi"→"em"; "anh Soutetsu" GIỮ NGUYÊN theo câu hỏi đang chờ Hieu.

### 1376 [稀咲] — pronoun

JP: 「ボクの気持ちとおんなじに、\nボクの体も、双鉄とくっつきあえて喜んでるんだ」
TW: 「我的心情很愉悅，身體也因為接觸到你而愉悅不已呢」
Cũ: 「Giống hệt như tâm trạng của tôi,\ncơ thể tôi cũng đang rất vui sướng vì được gắn kết với anh Soutetsu đấy.」
Mới: 「Giống hệt như tâm trạng của em,\ncơ thể em cũng đang rất vui sướng vì được gắn kết với anh Soutetsu đấy.」
→ Kisaki tự xưng ボク với Soutetsu (2 lần): "tôi"→"em"; "anh Soutetsu" GIỮ NGUYÊN theo câu hỏi đang chờ Hieu.

### 1379 [双鉄H] — pronoun

JP: 「もっと貪欲に学びたい。\n稀咲の、ヴァギナの傷が癒えたら、すぐにでも」
TW: 「我還想再多學點呢。只要稀咲小穴的傷好了，我願意立刻就做」
Cũ: 「Anh còn muốn học hỏi nhiều hơn nữa.\nChỉ cần vết thương ở âm đạo của Kisaki lành lại, anh sẵn sàng làm ngay lập tức」
Mới: 「Tôi còn muốn học hỏi nhiều hơn nữa.\nChỉ cần vết thương ở âm đạo của Kisaki lành lại, tôi sẵn sàng làm ngay lập tức」
→ Soutetsu với Kisaki: "anh"→"tôi" (2 lần, JP ngầm — người nói là Soutetsu).

### 1394 [双鉄H] — pronoun

JP: 「そうだな……好きだ。ペニスも、僕も、稀咲の――髪\n……も――手も……息も、匂いも……全てを、大好きだ」
TW: 「是啊……我喜歡。我的陰莖、我的心，喜歡稀咲的――頭髮……――手……呼吸、氣味……喜歡稀咲的一切」
Cũ: 「Đúng vậy…… anh thích lắm. Cả dương vật lẫn bản thân anh, đều thích――mái tóc\n……của Kisaki――cả đôi bàn tay…… hơi thở, và mùi hương…… anh yêu tất cả mọi thứ thuộc về em」
Mới: 「Đúng vậy…… tôi thích lắm. Cả dương vật lẫn bản thân tôi, đều thích――mái tóc\n……của Kisaki――cả đôi bàn tay…… hơi thở, và mùi hương…… tôi yêu tất cả mọi thứ thuộc về cô」
→ Soutetsu với Kisaki: "anh"→"tôi" (3 lần, JP 僕) và "em"→"cô" (JP không có đại từ — gọi Kisaki; tiền lệ Grand 11 2173).

### 1398 [稀咲] — pronoun

JP: 「そう……だね。ボクも、乳首が気持ちいい。\n双鉄の体に触れてる部分、全部、溶けそうに気持ちいい」
TW: 「是啊……是的，我的乳頭也很敏感。碰到雙鐵身體的每一處都舒服得要融化了」
Cũ: 「Đúng…… vậy. Tôi cũng, thấy sướng ở núm vú.\nNhững phần chạm vào cơ thể anh Soutetsu, tất cả, đều sướng đến mức như sắp tan chảy ra vậy.」
Mới: 「Đúng…… vậy. Em cũng, thấy sướng ở núm vú.\nNhững phần chạm vào cơ thể anh Soutetsu, tất cả, đều sướng đến mức như sắp tan chảy ra vậy.」
→ Kisaki tự xưng ボク với Soutetsu: "tôi"→"em"; "anh Soutetsu" GIỮ NGUYÊN theo câu hỏi đang chờ Hieu.

### 1400 [双鉄H] — pronoun

JP: 「そうか？　初めてのことなのだがな」
TW: 「是嗎？　明明是第一次啊」
Cũ: 「Vậy sao? Dù đây là lần đầu tiên anh làm chuyện này đấy」
Mới: 「Vậy sao? Dù đây là lần đầu tiên tôi làm chuyện này đấy」
→ Soutetsu với Kisaki: "anh"→"tôi" (JP ngầm — người nói là Soutetsu, lần đầu của cậu).

### 1416 [稀咲] — pronoun

JP: 「いや、慣れっこさ。\n双鉄は巻き込まれただけ。首謀者は父――頭取だ」
TW: 「沒事，我都習慣了。你只是被捲進來的，罪魁禍首是爸爸――行長」
Cũ: 「Không sao, tôi quen rồi.\nAnh Soutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——giám đốc ngân hàng cơ.」
Mới: 「Không sao, em quen rồi.\nAnh Soutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——giám đốc ngân hàng cơ.」
→ Kisaki tự xưng ボク với Soutetsu: "tôi"→"em" theo tiền lệ đã merge lr_稀咲h1 + h3 ("em" toàn file); "anh Soutetsu" GIỮ NGUYÊN theo câu hỏi đang chờ Hieu (h3 33 dòng, file 02 10 dòng).

### 1426 [双鉄H] — pronoun

JP: 「稀咲――これ以上、したら――もうっ！」
TW: 「稀咲――別再繼續了――我忍不住的！」
Cũ: 「Kisaki――nếu cứ tiếp tục thế này――anh ra mất!」
Mới: 「Kisaki――nếu cứ tiếp tục thế này――tôi ra mất!」
→ Soutetsu với Kisaki: "anh"→"tôi" (JP 僕, ngầm trong もう — "tôi sắp ra").

### 1432 [双鉄H] — pronoun

JP: 「稀咲……綺麗だ」
TW: 「稀咲……你好美」
Cũ: 「Kisaki…… em đẹp lắm」
Mới: 「Kisaki…… cô đẹp lắm」
→ Soutetsu gọi Kisaki "em"→"cô" (quy tắc đã khóa; tiền lệ Grand 11 2173).

### 1433 [双鉄H] — pronoun

JP: 「稀咲……パンツを脱いでくれるか？」
TW: 「稀咲……可以脫掉內褲嗎？」
Cũ: 「Kisaki…… em cởi quần lót ra được không?」
Mới: 「Kisaki…… cô cởi quần lót ra được không?」
→ Soutetsu gọi Kisaki "em"→"cô" (quy tắc đã khóa; tiền lệ Grand 11 2173).

### 1449 [双鉄H] — pronoun

JP: 「肌を重ねあうことがこれほど素敵なことだと……\n稀咲に教えてもらえることが、僕は本当に幸せだ」
TW: 「肌膚之親竟然如此美妙……有稀咲告訴我這一點，我真是太幸福了」
Cũ: 「Sự tiếp xúc da thịt lại tuyệt vời đến thế này……\nĐược Kisaki dạy cho điều đó, anh thực sự rất hạnh phúc」
Mới: 「Sự tiếp xúc da thịt lại tuyệt vời đến thế này……\nĐược Kisaki dạy cho điều đó, tôi thực sự rất hạnh phúc」
→ Soutetsu với Kisaki: "anh"→"tôi" (JP 僕は).

### 1450 [双鉄H] — pronoun

JP: 「そのおかげで、僕も――」
TW: 「託你的福，我也――」
Cũ: 「Nhờ vậy mà, anh cũng――」
Mới: 「Nhờ vậy mà, tôi cũng――」
→ Soutetsu với Kisaki: "anh"→"tôi" (JP 僕も).

### 1451 [双鉄H] — pronoun

JP: 「稀咲が起こしてくれたおかげかな。\nとても気持ちよく目覚めることが出来た」
TW: 「謝謝你叫醒我，醒來的感覺真的不錯」
Cũ: 「Chắc là nhờ Kisaki đánh thức anh chăng.\nAnh đã có thể thức dậy với một tâm trạng vô cùng sảng khoái.」
Mới: 「Chắc là nhờ Kisaki đánh thức tôi chăng.\nTôi đã có thể thức dậy với một tâm trạng vô cùng sảng khoái.」
→ Soutetsu với Kisaki là "tôi" (JP 僕, 2 lần) — quy tắc đã khóa; VN cũ "anh" cả hai lần.

### 1462 [稀咲] — pronoun

JP: 「そうなんだ。\nなら、もっと気持ち良くしてあげるよ」
TW: 「這就對了。我來幫你更加舒服吧」
Cũ: 「Ra là vậy.\nNếu thế, tôi sẽ làm cho anh sướng hơn nữa nhé.」
Mới: 「Ra là vậy.\nNếu thế, em sẽ làm cho anh sướng hơn nữa nhé.」
→ Kisaki tự xưng ボク với Soutetsu: "tôi"→"em"; "anh" GIỮ NGUYÊN theo câu hỏi đang chờ Hieu.

### 1464 [稀咲] — pronoun

JP: 「それも慣れっこ。\nで？　父はボクについて、どんな話をしたんだい？」
TW: 「這我也習慣了。然後呢？　我爸講了我什麼事啊？」
Cũ: 「Chuyện đó tôi cũng quen rồi.\nThế? Bố tôi đã nói gì về tôi vậy?」
Mới: 「Chuyện đó em cũng quen rồi.\nThế? Bố em đã nói gì về em vậy?」
→ Kisaki tự xưng ボク với Soutetsu: "tôi"→"em"; "Bố tôi/về tôi"→"Bố em/về em" theo cùng quy tắc (nói về bản thân với Soutetsu).

### 1486 [双鉄H] — gasp

JP: 「っ！」
TW: 「！」
Cũ: 「!」
Mới: 「Ư!」
→ Sweep lost-gasp-whole: JP 「っ！」 cả dòng chỉ là gasp, VN cũ chỉ còn "!" — thêm Ư.

### 1487 [稀咲] — gasp

JP: 「っ！！」
TW: 「！！」
Cũ: 「!!」
Mới: 「Ư!!」
→ Sweep lost-gasp-whole: JP 「っ！！」 cả dòng chỉ là gasp, VN cũ chỉ còn "!!" — thêm Ư.

### 1488 [双鉄H] — gasp

JP: 「っ！！！」
TW: 「！！！」
Cũ: 「っ!!!」
Mới: 「Ư!!!」
→ Sweep raw-tsu: JP 「っ！！！」 cả dòng chỉ là gasp, VN còn nguyên っ → Ư.

### 1492 [双鉄H] — gasp

JP: 「～～～～～っ！！！」
TW: 「～～～～～！！！」
Cũ: 「~~~~~っ!!!」
Mới: 「~~~~~Ư!!!」
→ Sweep raw-tsu: っ thô sau ~~~~~ → Ư (JP ～×5, VN ~×5 khớp).

### 1494 [稀咲] — gasp

JP: 「～～～～～～～～～～っ！！！」
TW: 「～～～～～～～～～～！！！」
Cũ: 「~~~~~~~~~~っ!!!」
Mới: 「~~~~~~~~~~Ư!!!」
→ Sweep raw-tsu: っ thô sau ~~~~~~~~~~ → Ư (JP ～×10, VN ~×10 khớp).

### 1650 [monologue] — gasp

JP: 嬉しげな笑み。\n強ばっていた稀咲の体が、少しやわら――っ！！？
TW: 她撐出了一個看似放鬆的微笑。稀咲原本僵硬的身體也柔軟了一――！！？
Cũ: Nụ cười rạng rỡ.\nCơ thể đang căng cứng của Kisaki, chợt mềm ra một chút――!!?
Mới: 「Nụ cười rạng rỡ.\nCơ thể đang căng cứng của Kisaki, chợt mềm ra một chút――Ư!!?」
→ Sweep lost-gasp-trailing: JP やわら――っ！！？ — gasp cuối dòng bị mất hẳn trong VN, thêm Ư sau ――.


## §6. Lượt soát 2

Đọc lại toàn bộ 38 bản sửa đối chiếu JP lần hai (in bảng key/JP/fix, kiểm tra tay từng dòng + đếm máy số u ở 1254 = 9, số ~ ở 1306/1310/1323/1492/1494 khớp JP): **38 tổng / 38 tái kiểm chứng / 0 loại bỏ / 0 sửa lại.**

## §7. Khối TOML (đã parse-kiểm chứng)

Khối `[script]` 38 khóa, parse bằng tomllib: 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\\n` trong khối là backslash-n dạng chữ, khớp CSV3).

```toml

"1189" = "「Cô không cần phải cố nuốt xuống đâu」"
"1204" = "「Đối phương là em mà, anh lại bảo không có cảm giác gì sao.」"
"1217" = "「Dù vậy, em cũng thấy cuộc gọi đó khá kỳ lạ.\\nNửa đêm nửa hôm lại bảo 『hãy đi làm sớm hơn bình thường hai tiếng』.」"
"1243" = "「Kyu――ưm――hya――ea――a――」"
"1254" = "「I hyuuuuuuuuuƯƯ!!!」"
"1288" = "「À——cô đã đánh thức tôi sao.」"
"1303" = "「Ừm. Chà, em cũng vậy.\\nMột ngày nào đó…… không xa…… kiểu như trong tương lai gần vậy.」"
"1306" = "「Ưm kyu――kuha――ưm a――~~~Ư!!!」"
"1308" = "「Ưm――ực――ưm――ực, ưm――\\nphuê!」"
"1310" = "「Ưm!? Phụt――ưm~~~~~~Ư」"
"1316" = "「Ừm, tôi cũng vậy.\\n――Tôi cũng……ƯƯ――ra đây」"
"1323" = "「Ưm~~~~~Ư――ưm――ưm――ực!」"
"1357" = "「Tình dục——tình dục không phải là thứ đáng bị ghê tởm.\\nEm sẽ dạy cho anh Soutetsu điều đó.」"
"1361" = "「Tôi――dạy cho Kisaki sao?」"
"1364" = "「Tôi cũng vậy――tình dục của tôi, cũng chỉ có thể học từ Kisaki,\\nvà tôi cũng không muốn học từ ai khác」"
"1366" = "「Tôi cũng vậy――Kisaki! Một chút, nữa thôi――Ư!」"
"1369" = "「Cảm thấy mãnh liệt như vậy, không biết thực tế có làm thế không——\\nhay đó chỉ là hư cấu nhỉ? Em cũng từng nghĩ thế nhưng……」"
"1373" = "「Em hiểu mà, anh Soutetsu.」"
"1376" = "「Giống hệt như tâm trạng của em,\\ncơ thể em cũng đang rất vui sướng vì được gắn kết với anh Soutetsu đấy.」"
"1379" = "「Tôi còn muốn học hỏi nhiều hơn nữa.\\nChỉ cần vết thương ở âm đạo của Kisaki lành lại, tôi sẵn sàng làm ngay lập tức」"
"1394" = "「Đúng vậy…… tôi thích lắm. Cả dương vật lẫn bản thân tôi, đều thích――mái tóc\\n……của Kisaki――cả đôi bàn tay…… hơi thở, và mùi hương…… tôi yêu tất cả mọi thứ thuộc về cô」"
"1398" = "「Đúng…… vậy. Em cũng, thấy sướng ở núm vú.\\nNhững phần chạm vào cơ thể anh Soutetsu, tất cả, đều sướng đến mức như sắp tan chảy ra vậy.」"
"1400" = "「Vậy sao? Dù đây là lần đầu tiên tôi làm chuyện này đấy」"
"1416" = "「Không sao, em quen rồi.\\nAnh Soutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——giám đốc ngân hàng cơ.」"
"1426" = "「Kisaki――nếu cứ tiếp tục thế này――tôi ra mất!」"
"1432" = "「Kisaki…… cô đẹp lắm」"
"1433" = "「Kisaki…… cô cởi quần lót ra được không?」"
"1449" = "「Sự tiếp xúc da thịt lại tuyệt vời đến thế này……\\nĐược Kisaki dạy cho điều đó, tôi thực sự rất hạnh phúc」"
"1450" = "「Nhờ vậy mà, tôi cũng――」"
"1451" = "「Chắc là nhờ Kisaki đánh thức tôi chăng.\\nTôi đã có thể thức dậy với một tâm trạng vô cùng sảng khoái.」"
"1462" = "「Ra là vậy.\\nNếu thế, em sẽ làm cho anh sướng hơn nữa nhé.」"
"1464" = "「Chuyện đó em cũng quen rồi.\\nThế? Bố em đã nói gì về em vậy?」"
"1486" = "「Ư!」"
"1487" = "「Ư!!」"
"1488" = "「Ư!!!」"
"1492" = "「~~~~~Ư!!!」"
"1494" = "「~~~~~~~~~~Ư!!!」"
"1650" = "「Nụ cười rạng rỡ.\\nCơ thể đang căng cứng của Kisaki, chợt mềm ra một chút――Ư!!?」"

```

File 稀咲h1_性生活 audit xong: đọc 335/335 dòng, sai **38/335 (11,3%)** — đại từ 26, gasp 10, SFX 2; 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 mồ côi, 0 chưa dịch, 0 trùng khóa. Lỗi tập trung ở cụm đại từ (Soutetsu "anh"/"em" với Kisaki và Kisaki tự xưng "tôi" — cả hai đều mâu thuẫn nội bộ file và trái quy tắc đã khóa), còn lại là gasp っ sweep đã liệt kê (1 dòng chỉnh số u) và 2 lỗi nguyên âm rên. Câu hỏi lớn duy nhất còn treo: Kisaki gọi Soutetsu "anh Soutetsu" 41 dòng — giữ nguyên chờ Hieu chốt (như h3/file 02), không tự đổi hàng loạt. Khối TOML 38 khóa parse đạt, lượt soát 2: 38/38/0/0.

Kết bài