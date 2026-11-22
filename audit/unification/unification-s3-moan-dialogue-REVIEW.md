# Unification batch U12a — §3 moan/SFX, DIALOGUE tokens (M7, M8, M9, M10, M11, M15, M68, M70)

**Phạm vi:** 8 mục mới / **99 dòng** trong 43 file. Chỉ sửa token ĐỐI THOẠI trong H-scene. Không động vào （ ） SFX miêu tả (số lượng kéo dài, loại chữ) — đó là batch U12b/M14 chạy song song. Dòng nào vừa có token đối thoại phải sửa vừa có （ ） SFX thì chỉ sửa token đối thoại và cờ lại (§5, F8).

**Nguồn:** CSV3 good-set (87.833 dòng; đã loại 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`), `audit-*-wrong.json` (9.239 mục), `moans/moan-*-wrong.json` (1.516 mục), các đợt unification đã gộp (đối chiếu trùng lặp §5, F9), báo cáo điều tra F1 (`investigation-open-moan-questions-REPORT.md`, đọc toàn bộ kể cả §0 sửa list). Mọi dòng trong đợt này đều có trong CSV3 — không dòng nào phải lấy JP/old_vn từ TOML-2.

## 1. Phương pháp

- **Liệt kê:** script chỉ dùng để liệt kê/đếm (`u12a_enum.py` → `u12a_candidates.txt`, 805 dòng; `u12a_enum2.py` → `u12a_candidates2.txt`, 215 dòng) — đã đọc toàn bộ cả hai file ứng viên. Mọi giá trị fix đều do đọc JP (+TW + dòng kề) rồi viết tay; JP thắng TW.
- **old_vn:** giá trị hiện tại = fix moan nếu có trong bất kỳ `moan-*-wrong.json`, nếu không thì fix audit nếu có trong bất kỳ `audit-*-wrong.json`, nếu không thì fix unification nếu có trong bất kỳ `unification-*-wrong.json` ĐÃ GỘP, nếu không thì VN của CSV3 good-set.
- **Quy tắc chung:** một dòng = một cách diễn (VN hoặc romaji, không trộn) cho moan; công thức độ dài nguyên âm: tổng số mora Hepburn — khi mora gốc ĐÃ là nguyên âm thì KHÔNG đếm đôi (んう×6 = 6u, không phải 7u); tổng số chữ kéo dài = 1 + số う/ぅ/ー. Không sửa bulk bằng script.
- **Lắp ráp/kiểm chứng cơ học (`u12a_assemble.py`):** script chỉ ráp các cặp thay thế đã viết tay và kiểm chứng: (1) mọi `old_sub` xuất hiện đúng 1 lần trong `old_vn` lấy từ engine (99/99, 0 lỗi); (2) diff từng fix so với `old_vn` chỉ khác đúng chỗ token cần sửa (99/99 — xem §6); (3) đếm chữ bằng máy: M68 18/18 đúng số o, ハチロクh7 843 tổng 17u, lr追加_みくろ＆日々姫h 1731 tổng 7a; (4) đối chiếu 99/99 cặp (file, key) với các fix unification đã gộp — 0 trùng; (5) khối TOML parse-verified 43 file / 99 key, 0 lệch.
- **Không sửa trùng:** không dòng nào trong đợt này đã được sửa đúng trong audit/moan/unification đã gộp; hai trường hợp ĐẢO NGƯỢC fix moan (M9 1457, M10 992) được ghi rõ trong bảng và §3.

## 2. Quyết định áp dụng (coordinator quyết 22/11 ~11:30, theo ủy quyền của Hieu)

- **M7 くっ:** token đối thoại H-scene → "Ku". Giữ "Hự" trong 4 file quy ước (lr_ふかみh2, 日々姫h1, lrれいな追加h, ハチロクh2). 5 dòng "Hự" lẻ → "Ku" (凪ふかみh1 1232, lr_ふかみh1 1469, lr_凪h1 1190, ポーレットh6 851, 日々姫h4 1028). Giữ "kư" (lr_稀咲h1) và cụm động từ "Ngoáy"/"Thúc" (kể cả ハチロクh3 1815). Đối thoại non-H giữ "Ư". （ ） くっ → "Ư" — không động trong đợt này.
- **M8 や/やっ:** theo token KỀ SAU: theo sau là lời nói/từ chối (TW 不要) → "Á"; trong chuỗi token rên (kề là ふあっ/んっ/あっ… — âm, không phải từ) → "Ya"/"Yaa" (giữ độ dài, chữ thường giữa chuỗi). Bỏ "A" trần cho や. Giữ lr_稀咲h1 991 "Yaa!" và lr_日々姫ふかみh1 1334 "Ya!?". Sửa lr_凪h2 1203 token cuối "áa!" → "Áa!" (hoa đầu). Dòng đã diễn nghĩa ("Đừng"/"Không…") giữ nguyên.
- **M9 ふっ:** không đổi toàn dự án — chỉ thống nhất TRONG file: 真闇h3 "phù" (3) → "Phư" (quy ước Mayami h1 5×, h2 4× "Phư"); ハチロクh9 ("phù" 3 + "Fu" 3 — token trong chuỗi rên → "Fu", độc lập → giữ "phù"); lr_ニイロクh ("Fu" 3 + "phù" 1 → "Fu"); lr_真闇h1 ("Fu" 1 + "phù" 1 — đọc tay từng dòng). Giữ lr_日々姫ふかみh1 "Hư" (1350/1479).
- **M10 ふぇ/ふえ:** token trong chuỗi rên → "Fue"; thán từ ngạc nhiên độc lập (TW 哎/咦, theo sau là câu nói nhận ra/phủ nhận/hỏi) → "Hể?" (5 dòng: 凪h1 1090, ふかみh1 993, れいなh3 1026, れいなh4 1897, lr_稀咲h1 992 — 992 ĐẢO NGƯỢC fix moan "Fue!?"); kéo dài (ふぇぇ/ふえぇ) → giữ "Phuê…" (凪ふかみ01_流れ 1547, 共通13 2038, ハチロク02 2170); reina-h3 1133 giữ "Hả?" (không động).
- **M11 ふや:** H-scene → romaji "Fuya" (giữ độ dài: ふやぁ→"Fuyaa", ふやうっ→"Fuyau"); ふやん(っ) → "Fuyan" (日々姫h2 1081, ふかみh3 2366). Đối thoại non-H giữ "phuya" theo quy tắc fa/fu đã khóa. Đảo ngược các khóa audit (romaji fallback 21/11 + thực hành moan-pass làm căn cứ).
- **M15 ん+phụ âm:** H-scene → romaji Nkyu/Nku/Na/Nfu/Ne/Nhyu (giữ độ dài theo công thức Hepburn tổng): 日々姫h4 1075 んあっ "ưm a!"→"Na!"; 真闇h1 1080 んふっ "ưm phư"→"Nfu"; ハチロクh7 745 "ưn kyuuu"→"Nkyuuu", 843 "Ưn kyu…"→"Nkyu…", ハチロクh8 1561/821/759 "ưn ku"→"Nku"; lr真闇追加h 1097 "ưm ku"→"Nku"; lr_稀咲h1 1162 んうっ "…ưn ư!"→"Nu!". ん(っ) trần → "ưm": 真闇h3 2323/2328 "ưn"→"ưm". Giữ ポーレットh4 878 ぅんっ→"ưn" (ん sau nguyên âm ぅ). Không động dòng "nn"/"mm" đã đúng.
- **M68 れろ:** ngắn → "liếm" (hầu hết đã đúng — chỉ sửa chỗ token bị MẤT); dài (kéo ≥3 mora) → romaji "Rero" + số nguyên âm (1 + số お/ぉ): ハチロクh8 841, 日々姫h3 1857, れいなh2 1084, れいなh2 1114 + Nhóm 2 (~10 dòng đã diễn độ dài bằng kéo-m hoặc "dài": 凪h1 1772, 凪ふかみh1 1317, lr_凪ふかみh1 1633, lr_ニイロクh 2060, lr追加_みくろ＆日々姫h 1704/1854, lr_れいなh1 1372, 凪ふかみh2 1030, ハチロクh7 1840/1878 — CHUYỂN sang romaji cho thống nhất) + lr_日々姫ふかみh1 1461 chuẩn hóa "rê roooo"→"Reroooo" + 凪h2 2546 "Ngoáyyyyyy"→romaji (đếm o bằng máy). Dòng "rộp" (14) KHÔNG ĐỘNG — chờ T77.
- **M70 きゅ:** không đổi, trừ kiểm lại 真闇h2 1842 ("（Thắt lại――phập――kypu――kyuu）" — đọc tay JP+TW, quyết theo hệ của file: token ngắn → nghĩa, dài ≥3 → romaji; token nào không có nghĩa VN trong file thì giữ romaji và ghi chú).

**Ba chỗ số liệu của F1 được sửa trong đợt này:** (a) M8: "64 dòng A trần" của F1 bị nhiễm (phần lớn là あっ→"A") — đối chiếu theo token chỉ còn **17 dòng** や→"A" thật sự. (b) M9: lr_ニイロクh F1 ghi "Fu 2" nhưng thực tế "Fu" ×3 (1339, 1342, 1569) + "phù" ×1. (c) M7: 4 file quy ước giữ **11 dòng Hự**, không phải 12 — lrれいな追加h chỉ có 1 dòng Hự (723); 1221 là んくっ→"Ưm" (lớp M15), không phải Hự (xem §5, F7).

## 3. Bảng sửa theo mục
## 3.1. M7 — くっ đối thoại H-scene → "Ku" (23 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr_れいなh1_レディ・れいな | 1225 | 「くっ！！！」 | 「咕！！！」 | 「Ư!!!」 | 「Ku!!!」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| 凪h2_おとなの水着 | 2252 | 「最初は……凪、さま――んっ――くっ――\n好き、に――する――けんっ――」 | 「一開始……先要讓本小姐……嗯，唔……按自己的意願……隨便來」 | 「Ban đầu……Nagi, sama——Ưm——Ư——\nSẽ, làm——theo ý thích——á——」 | 「Ban đầu……Nagi, sama——Ưm——Ku——\nSẽ, làm——theo ý thích——á——」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| 凪h2_おとなの水着 | 2489 | 「くっ――ふっ――んひゅっ――んんん～っ！」 | 「唔……嗯……嗯……嗯！」 | 「Ư——Phù——Ưm hứ——Ưmmm~!!」 | 「Ku——Phù——Ưm hứ——Ưmmm~!!」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| 真闇h1_長期熟成 | 1059 | 「くっ――ふっ――」 | 「嗚――呼――」 | 「Ư――phư――」 | 「Ku――phư――」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| 真闇h1_長期熟成 | 1065 | 「んっ――くっ――」 | 「嗯――唔――」 | 「Ưm――Ư――」 | 「Ưm――Ku――」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| 真闇h1_長期熟成 | 1214 | 「真闇姉の、膣の……中……あっ――\nうねって―――ひだっ、これっ――くっ」 | 「真闇姐的小穴……裡……啊――很蜿蜒――這是什麼――唔」 | 「Bên trong……âm đạo, của chị Mayami……a――\nuốn lượn――nếp gấp này, là sao――Ư.」 | 「Bên trong……âm đạo, của chị Mayami……a――\nuốn lượn――nếp gấp này, là sao――Ku.」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| lr_ハチロクh2_新しい服。新しい旅 | 1464 | 「ぁっ――ぁっ――んっ――くっ」 | 「啊、啊、嗯、唔」 | 「A——a——ưm——ư」 | 「A——a——ưm——Ku」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| lr_ハチロクh2_新しい服。新しい旅 | 1486 | 「ん――くっ――ぁっ！」 | 「嗯……唔……啊！」 | 「Ưm——ư——aƯ!」 | 「Ưm——Ku——aƯ!」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| lr_ポーレットh1_家族旅行の最終日の夜 | 1026 | 「はっ――んっ――ふうっ、ふうっ――んっ！　あっ、\n腰っ、もっと――くっ、ふ――双鉄、くんっ――あっ！」 | 「哈——嗯——呼唔，呼唔——嗯！啊，腰、繼續、呼——雙鐵君——啊！」 | 「Ha——ưm——phù, phù——ưm! A,\nEo, tiếp tục đi——ư, phu——anh Soutetsu——a!」 | 「Ha——ưm——phù, phù——ưm! A,\nEo, tiếp tục đi——Ku, phu——anh Soutetsu——a!」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| lr_日々姫ふかみh1_凪ちゃんの代わり | 1265 | 「ダメ……だっ！　ぁ――くっ――もうっ、イクッ！」 | 「不行……了！　啊——嗚——要、射了！」 | 「Không…… được! A――ư――anh, ra mất!」 | 「Không…… được! A――Ku――anh, ra mất!」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| lr_日々姫ふかみh1_凪ちゃんの代わり | 1432 | 「ぁ――くっ！」 | 「啊——嗚！」 | 「A――ư!」 | 「A――Ku!」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| ハチロクh9_コノフクハキルコト | 2187 | 「ん、くっ――」 | 「嗯，嗯——」 | 「Ưm, ư——」 | 「Ưm, Ku——」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| ハチロクh9_コノフクハキルコト | 2289 | 「わたくし――の、おまたの――われ、めっ――んっ、\nふ――あっ――くっ――はぁ――おまん、まん、です」 | 「我——股間的——裂縫——嗯——呼——啊——嗯——啊——小妹妹」 | 「Là khe hở——giữa hai chân——của em——ưm,\nFu——a——ư——haa——là cô bé, ạ」 | 「Là khe hở——giữa hai chân——của em——ưm,\nFu——a——Ku——haa——là cô bé, ạ」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| ハチロクh9_コノフクハキルコト | 2378 | 「はひっ――んっ、くっ――ふ、あっ――\nはいっ！　そう、てつ――さまっ！！！」 | 「是——嗯——呼，啊——是！雙鐵少爺——！！！」 | 「Hahi——ưm, ư——Fu, a——\nVâng! Ngài Soutetsu!!!」 | 「Hahi——ưm, Ku——Fu, a——\nVâng! Ngài Soutetsu!!!」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| ポーレットh8_気動車の国のアリス | 2080 | 「イって――いい――くっ――僕も――すぐっ」 | 「你就——高潮吧——我也——很快要——」 | 「Cứ lên đỉnh——đi——ư——tôi cũng——sắp rồi」 | 「Cứ lên đỉnh——đi——Ku——tôi cũng——sắp rồi」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| 稀咲h1_性生活 | 988 | 「DVD――と、言ってた、が――んっ――くっ――\nそうした、ものを――見たり……っ――する、のか？」 | 「DVD――什麼的――嗯――嗚――你竟然會――看那種類型的……――DVD嗎？」 | 「Cô nói là, DVD——ưm——ư——\ncô cũng xem…… những thứ——như vậy, sao?」 | 「Cô nói là, DVD——ưm——Ku——\ncô cũng xem…… những thứ——như vậy, sao?」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| ポーレットh6_あなたとふたりの学園エッチ | 805 | 「やふっ――ふあっ！！？　んっ――そうてつ、くっ――\nあっ！　いまっ――うごいた、らっ――んきゅんっ！！」 | 「啊——呼啊！！？嗯——雙鐵——啊！現在——要是動起來——嗯啊！！」 | 「Yafu——Fua!!? Ưm——Anh Soutetsu, ư—— A! Bây giờ——mà cử động, thì——Nkyun!!」 | 「Yafu——Fua!!? Ưm——Anh Soutetsu, Ku—— A! Bây giờ——mà cử động, thì——Nkyun!!」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| lr_ポーレットh2_デコレーション＆ミルク | 1041 | 「はっ！　あっ！　ぁっ――あ――ぁあっ！！\nそう、てつ、くっ――あっ！　わた、しっ――だんだん」 | 「哈！啊！啊——啊——啊啊！！雙鐵、君——啊！我——快要」 | 「Ha! A! A——a——aa!!\nAnh, Soutetsu——a! Em——sắp」 | 「Ha! A! A——a——aa!!\nAnh, Soutetsu——Ku——a! Em——sắp」 | くっ đối thoại H-scene → "Ku" (quyết M7) CHÈN token: JP có くっ sau そう、てつ nhưng VN bỏ mất — khôi phục "Ku", không phải thay thế. |
| 凪ふかみh1_修学旅行の夜 | 1232 | 「くっ――あ」 | 「呃……啊」 | 「Hự——a」 | 「Ku——a」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| lr_ふかみh1_ふかみうさぎのたまご | 1469 | 「ふぁっ！　急にっ！　急にっ、そんなっ！　そんなっ、\nんっ、くっ！　あっ！　強いのっ！　強いのぉ！！」 | 「蛤啊！突然、突然這麼激烈！啊嗯！啊啊！好激烈……好激烈啊啊啊！！」 | 「Fa! Đột nhiên! Đột nhiên, như vậy! Như vậy,\nưm, hự! A! Mạnh quá! Mạnh quá đi!!」 | 「Fa! Đột nhiên! Đột nhiên, như vậy! Như vậy,\nưm, Ku! A! Mạnh quá! Mạnh quá đi!!」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| lr_凪h1_痛いの痛いの飛んでけばい | 1190 | 「あ……もう、ちょっと――んっ――くっ――ふあっ！\nも、ちょっとで――おまんこの、おく――おちん、ちん」 | 「啊……還差一點……嗯……唔……啊！還差一點……雞雞……就能進到……最深處了」 | 「A……Sắp, được rồi——ưm——hự——fua!\nMột, chút nữa thôi——là vào đến, tận cùng——bên trong, rồi」 | 「A……Sắp, được rồi——ưm——Ku——fua!\nMột, chút nữa thôi——là vào đến, tận cùng——bên trong, rồi」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| ポーレットh6_あなたとふたりの学園エッチ | 851 | 「ん……くっ――」 | 「嗯……啊——」 | 「Ưm……hự——」 | 「Ưm……Ku——」 | くっ đối thoại H-scene → "Ku" (quyết M7) |
| 日々姫h4_いもうとタオル | 1028 | 「んっ――くっ」 | 「嗯――唔」 | 「Ưm――hự」 | 「Ưm――Ku」 | くっ đối thoại H-scene → "Ku" (quyết M7) |

## 3.2. M8 — や/やっ: theo token KỀ SAU (17 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr_ふかみh2_セックスの意味 | 1275 | 「ふぁっ！　あっ！　来てるっ！　んっ！\nちょっと、ずつ――ふぁっ――や、ぁ――熱っ、くて」 | 「蛤啊！啊！進來了！嗯！一點點地……蛤啊……啊……好熱」 | 「Fa! A! Đang vào! Ưm!\nTừng chút, một——Fa——a, a——nóng, quá.」 | 「Fa! A! Đang vào! Ưm!\nTừng chút, một——Fa——Ya, a——nóng, quá.」 | や trong chuỗi rên (kề ふあっ) → "Ya" |
| lr_ポーレットh1_家族旅行の最終日の夜 | 1018 | 「ふえっ！？　やっ――双鉄くんっ――だめっ――\nお指っ――んっ――おまんのこ、中で――ひろげちゃっ」 | 「呼哎！？呀——雙鐵君——不可以——手指——嗯——在小穴裡——撐開」 | 「Fue!? A――Anh Soutetsu――không được――\nNgón tay――ưm――trong, âm đạo――đang mở rộng ra」 | 「Fue!? Á――Anh Soutetsu――không được――\nNgón tay――ưm――trong, âm đạo――đang mở rộng ra」 | Theo sau là lời nói (双鉄くん) → "Á" |
| lr_ポーレットh1_家族旅行の最終日の夜 | 1086 | 「んっ――やっ――はっ――んっ――ふっ」 | 「嗯——呀——哈——嗯——呼」 | 「Ưm――a――hà――ưm――phù」 | 「Ưm――Ya――hà――ưm――phù」 | Trong chuỗi rên (んっ—やっ—はっ—んっ—ふっ) → "Ya" |
| lr_ポーレットh1_家族旅行の最終日の夜 | 1100 | 「んっ！　――ふぁっっ――やぁんっ――指っ――んっ！\nいきなりっ――に、ほんっ――ひ――ぁっ――」 | 「嗯！——呼啊——呀嗯——手指——嗯！一上來就——兩根——呀——啊——」 | 「Ưm! ――Fa――A――Ngón tay――ưm! Đột nhiên――hai, ngón――hi――a――」 | 「Ưm! ――Fa――Yaan――Ngón tay――ưm! Đột nhiên――hai, ngón――hi――a――」 | や/やっ → xem ghi chú từng dòng やぁん — họ やん → romaji (tiền lệ 日々姫h2 1055 "Yan"); TW 呀嗯 là âm thuần. |
| lr_ポーレットh1_家族旅行の最終日の夜 | 1221 | 「やぁ、もうっ、破いちゃうとか――\n旅行中ですよ？　余分なんてもってきてないのに」 | 「討厭，真是的，居然把褲襪撕破了——我們現在可是在旅行中，我可沒有帶備用的」 | 「A, thiệt tình, xé rách thế này thì――\nĐang đi du lịch đấy nhé? Em đâu có mang theo đồ dự phòng đâu」 | 「Á, thiệt tình, xé rách thế này thì――\nĐang đi du lịch đấy nhé? Em đâu có mang theo đồ dự phòng đâu」 | Theo sau là lời nói (もうっ) → "Á" |
| lr_ポーレットh1_家族旅行の最終日の夜 | 959 | 「やっっ、えと、\nしてほしいっていうんじゃなくて、そのっ」 | 「不，呃，人家沒有想做啦，那個…」 | 「A, ừm,\nkhông phải là em muốn anh làm, mà là」 | 「Á, ừm,\nkhông phải là em muốn anh làm, mà là」 | Theo sau là lời nói/từ chối (TW 不) → "Á" |
| lr_ポーレットh1_家族旅行の最終日の夜 | 995 | 「やっ――してほし、してほしい、ですぅっ――んっ、\nそうてつ、くんに――わたしの大好きな、旦那さま、に」 | 「呀——想做，我想做啦——嗯，想被你——被我最愛的，丈夫疼愛」 | 「A――em muốn, em muốn anh làm, cho em――ưm,\nBởi anh Soutetsu――bởi người chồng, mà em yêu nhất」 | 「Á――em muốn, em muốn anh làm, cho em――ưm,\nBởi anh Soutetsu――bởi người chồng, mà em yêu nhất」 | Theo sau là lời nói (してほしい) → "Á" |
| lr_ポーレットh2_デコレーション＆ミルク | 1013 | 「やっ！　はっ！　はげしっ！　んっ！　こんなのっ！\nおっぱい、もっ！　あっ――おまんこ――もぉっ！！」 | 「呀！哈！好用力！嗯！這樣的！胸部也！啊——小穴——也！！」 | 「A! Ha! Mãnh liệt quá! Ưm! Thế này!\nCả ngực! A——cả âm đạo——nữa!!」 | 「Ya! Ha! Mãnh liệt quá! Ưm! Thế này!\nCả ngực! A——cả âm đạo——nữa!!」 | Đầu chuỗi rên (やっ! はっ! はげしっ! んっ!) → "Ya" |
| lr_稀咲ポーレットh1_悪い大人の契約 | 1523 | 「はっ！　あっ！？　やっ―うそっ―ふあっ―\nいっぱい、なのに―みちみち、してて、きつい、のに」 | 「哈！　啊！不要——騙人——呼啊——明明都、滿滿的了——滿滿的、緊緊的」 | 「Ha! A!? A——không thể nào——Fua—— Đầy ắp, rồi mà——căng cứng, chật chội, thế mà.」 | 「Ha! A!? Á——không thể nào——Fua—— Đầy ắp, rồi mà——căng cứng, chật chội, thế mà.」 | Theo sau là lời nói/từ chối (うそっ, TW 不要) → "Á" |
| ふかみh3_夏休みの最後の日の、前の日 | 2785 | 「や、ちょっと、ダメですよぉ！」 | 「討厭，不行，不可以的！」 | 「A, từ từ đã, không được đâu!」 | 「Á, từ từ đã, không được đâu!」 | Theo sau là lời nói (ちょっと、ダメ) → "Á" |
| れいなh3_おもらし自由化大作戦 | 1078 | 「やあっ！　これっ――れいなっ――\nはずかしっ――はずかし――ぃっ――で――ふあっ！」 | 「啊！這個……玲奈……好害羞……羞死了……啊嗯！」 | 「A! Cái này——Reina——\nXấu hổ——xấu hổ——quá——đi——Fua!」 | 「Áa! Cái này——Reina——\nXấu hổ——xấu hổ——quá——đi——Fua!」 | やあっ — giữ độ dài → "Áa" |
| グランドリライト03_日々姫 | 1998 | 「やあっ！？　今の撮られちゃったと！！？」 | 「呀！？你剛才把我拍下來了！！？」 | 「A!? Anh vừa chụp em đấy à!!?」 | 「Áa!? Anh vừa chụp em đấy à!!?」 | やあっ — giữ độ dài → "Áa" |
| ハチロクh1_契り | 1217 | 「やっ――あっ――うねうね――してっ――んっ――\nおなか――おまんまんっ――あっ、舐めて――ん、ふっ」 | 「呀——啊——舌頭——動來動去的——嗯——肚子裡——小妹妹——啊、舔得好——嗯、嗚」 | 「A――A――Uốn lượn――như vậy――Ưm――\nBụng――Bướm――A, liếm đi――Ưm, phù.」 | 「Ya――A――Uốn lượn――như vậy――Ưm――\nBụng――Bướm――A, liếm đi――Ưm, phù.」 | Đầu chuỗi rên (やっ—あっ—…) → "Ya" |
| ハチロクh1_契り | 1245 | 「あひっ――やっ――あうっっ……おまん、まん――\nはっ――あっ――とけ、ちゃうっ――んうっ」 | 「啊——呀——啊嗚……小妹妹——哈——啊——要融化了——嗯嗚」 | 「Ahi――A――Aư……Bướm, bướm――\nHa――A――Tan chảy, mất thôi――Ưm ư.」 | 「Ahi――Ya――Aư……Bướm, bướm――\nHa――A――Tan chảy, mất thôi――Ưm ư.」 | Giữa chuỗi rên (あひっ—やっ—あうっ) → "Ya" |
| ハチロクh8_桜色のひめごと | 706 | 「ひゃぎゅっ！？　ふっ――ふあっ！？　あっ――\nおっぱい――っ！　やっ、ちくびっ――くりゅ、ん、ふ」 | 「呀嗚！？呼——呼啊！？啊——乳房——！呀，乳頭——揉，嗯，呼」 | 「Hyagyu!? Phù——Fua!? A——\nnhũ hoa——Ư! A, núm vú——kích thích, ưm, phù」 | 「Hyagyu!? Phù——Fua!? A——\nnhũ hoa——Ư! Á, núm vú——kích thích, ưm, phù」 | Theo sau là lời nói (ちくびっ) → "Á" |
| 日々姫h5_白濁絵の具の射精会 | 1145 | 「やっ――らめえっ――さきっぽ――おちん、ぽっ――\nいったら、らめ、なの――さみしい――のぉおっ！」 | 「呀――不行――龜頭――雞雞――不要抽走――不然――好寂寞！」 | 「A――không được――phần đầu――chim, của anh――\nRút ra, không được, đâu――cô đơn, lắm――đó!」 | 「Á――không được――phần đầu――chim, của anh――\nRút ra, không được, đâu――cô đơn, lắm――đó!」 | Theo sau là lời từ chối (らめえっ) → "Á" |
| lr_凪h2_虎さんの交尾 | 1203 | 「ふあっ！　やぁっ！　やぁああっ！　にーさんの、\nおちんち、んっ――こわ――こわれるの――やあっ！」 | 「哇！不要！不要啊！大哥哥的雞雞……要把咱弄瘋了……不要啊！」 | 「Fua! Áa! Áaaa! Cậu nhỏ của anh,\nưm——hỏng——hỏng mất——áa!」 | 「Fua! Áa! Áaaa! Cậu nhỏ của anh,\nưm——hỏng——hỏng mất——Áa!」 | や/やっ → xem ghi chú từng dòng Chỉ sửa hoa đầu token cuối ("áa!" → "Áa!") cho khớp 2 token đầu của dòng. |

## 3.3. M9 — ふっ: thống nhất TRONG file (8 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| 真闇h3_補習授業の廃校舎 | 2212 | 「はっ――あ、あっ、あああ――んっ――そこ、\nば、され、たら――ふっ――あ――ぞわ、って」 | 「哈――啊、啊、啊啊啊――嗯――那裡，插那裡的話――呼――啊――好棒」 | 「Há――a, á, aaa――ưm――chỗ đó,\nbị, chạm, vào――phù――a――rùng mình, mất.」 | 「Há――a, á, aaa――ưm――chỗ đó,\nbị, chạm, vào――Phư――a――rùng mình, mất.」 | 真闇h3: "phù" → "Phư" (quy ước Mayami h1 5×/h2 4× "Phư") |
| 真闇h3_補習授業の廃校舎 | 2215 | 「はっ――ん――ふっ――あっ――おねえ、ちゃんっ、\nふぁうっ――ふあっ――そこ、ば――押されたらっ」 | 「哈――嗯――呼――啊――姐姐，哇――嗚啊――那裡――不能壓啊」 | 「Há――ưm――phù――á――chị, á,\nfau――fua――chỗ đó――bị ép vào thì.」 | 「Há――ưm――Phư――á――chị, á,\nfau――fua――chỗ đó――bị ép vào thì.」 | 真闇h3: "phù" → "Phư" (quy ước Mayami) |
| 真闇h3_補習授業の廃校舎 | 2256 | 「あっ――双ちゃん……んっ――それっ――\nおねえちゃん――好きっ――んっ――ふっ――あ」 | 「啊――小雙……嗯――那是――姐姐――喜歡――嗯――呼――啊」 | 「A――Sou-chan……ưm――cái đó――\nchị――thích lắm――ưm――phù――a.」 | 「A――Sou-chan……ưm――cái đó――\nchị――thích lắm――ưm――Phư――a.」 | 真闇h3: "phù" → "Phư" (quy ước Mayami) |
| ハチロクh9_コノフクハキルコト | 2033 | 「ふっ……んっ――――（ごくんっ）\nずっ――ちゅるっ――じゅううっ――（ごくっ）」 | 「呼……——（嗯）呲——啾嚕——吱嗚——（嗯）」 | 「Phù……ưm————（Ực）\nZu——churu——juuu——（Ực）」 | 「Fu……ưm————（Ực）\nZu——churu——juuu——（Ực）」 | ハチロクh9: token trong chuỗi rên → "Fu" Ca khó nhất file: ふっ đầu dòng + …… + んっ cùng dòng — xét là trong chuỗi rên (file đã dùng "Fu" 3 dòng). |
| ハチロクh9_コノフクハキルコト | 2138 | 「ちゅむっ！　じゅっ！　じゅぼっ――んっ、ふっ、\nれるっ――ぢゅっ！　ぢゅぼっ！　じゅるううっ！」 | 「啾姆！啾！呲啾——呼，咻嚕——呲啾！啾啵！啾嚕！」 | 「Chumu! Ju! Jubo——ưm, phù,\nreru——ju! Jubo! Juruuu!」 | 「Chumu! Ju! Jubo——ưm, Fu,\nreru——ju! Jubo! Juruuu!」 | ハチロクh9: token giữa chuỗi rên miệng → "Fu" |
| ハチロクh9_コノフクハキルコト | 2182 | 「んむっ！？　んっ――ちゅぼっ――じゅっ！\nぢゅぶっ！　ぢゅむっ！　ふっ――ちゅむ、じゅっ！」 | 「嗯姆！？嗯——啾啵——啾！啾噗！呲啾姆！呼——啾嗯，啾！」 | 「Ưm mu!? Ưm——chubo——ju!\nJubu! Jumu! Phù——chumu, ju!」 | 「Ưm mu!? Ưm——chubo——ju!\nJubu! Jumu! Fu——chumu, ju!」 | ハチロクh9: token giữa chuỗi rên miệng → "Fu" |
| lr_ニイロクh_誓い。約束 | 1571 | 「クリト、リス、もっ──ふっ！　あっ！　ちつ、こう、\nもっ──おしっこの、穴も──全部、全部がっ」 | 「陰蒂——呼！啊！陰道口——還有尿尿的小洞——全部、全部——」 | 「Âm, vật, cũng──phù! A! Cửa, âm đạo,\ncũng──cả lỗ, đi tiểu──tất cả, tất cả」 | 「Âm, vật, cũng──Fu! A! Cửa, âm đạo,\ncũng──cả lỗ, đi tiểu──tất cả, tất cả」 | lr_ニイロクh: "phù" → "Fu" (file còn lại 3× "Fu") |
| lr_真闇h1_僕のおねえちゃん | 1457 | 「う、ん……ふっ――ぁっ――んふふっ――双、ちゃん」 | 「唔，嗯……呼——啊——嗯呼呼——小、雙」 | 「Ư, m……phù——a——Nfufu——Sou, chan」 | 「Ư, m……Fu——a——Nfufu——Sou, chan」 | lr_真闇h1: "phù" → "Fu" (file còn lại romaji fu/Fu) ĐẢO NGƯỢC fix moan ("phù"): file còn lại đều romaji fu/Fu. |

## 3.4. M10 — ふぇ/ふえ thán từ ngạc nhiên → "Hể?" (5 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| 凪h1_ふたりっきりのデート | 1090 | 「ふえっ！？」 | 「哎！？」 | 「Phuê!?」 | 「Hể!?」 | Thán từ ngạc nhiên độc lập (TW 哎/咦) → "Hể?" (quyết M10) |
| ふかみh1_ともはり練習 | 993 | 「ふえっ！！？」 | 「哎！！？」 | 「Phuê!?」 | 「Hể!!?」 | Thán từ ngạc nhiên độc lập (TW 哎/咦) → "Hể?" (quyết M10) |
| れいなh3_おもらし自由化大作戦 | 1026 | 「ふえ？」 | 「咦？」 | 「Fue?」 | 「Hể?」 | Thán từ ngạc nhiên độc lập (TW 哎/咦) → "Hể?" (quyết M10) |
| れいなh4_ふたりっきりのハロウィン | 1897 | 「ふえ？　れいな、\nなにかかんちがいしちゃってるですかあ？」 | 「咦？玲奈弄錯了什麼事情嗎」 | 「Fue? Reina,\nđã hiểu lầm chuyện gì sao ạ~?」 | 「Hể? Reina,\nđã hiểu lầm chuyện gì sao ạ~?」 | Thán từ ngạc nhiên độc lập (TW 哎/咦) → "Hể?" (quyết M10) |
| lr_稀咲h1_おしおきとごほうび | 992 | 「ふえっ！？　あ！　あっ――ううん――\nなんでも……なんでもない……ただ――うぁっ――」 | 「哎？！啊、啊……沒什麼……什麼都沒有……只是……」 | 「Fue!? A! Á――không――\nkhông có gì……không có gì đâu……chỉ là――Ư á――」 | 「Hể!? A! Á――không――\nkhông có gì……không có gì đâu……chỉ là――Ư á――」 | Thán từ ngạc nhiên độc lập (TW 哎/咦) → "Hể?" (quyết M10) ĐẢO NGƯỢC fix moan ("Fue!?"): ngữ cảnh là câu phủ nhận (như 1091), không phải chuỗi rên. |

## 3.5. M11 — ふや H-scene → romaji "Fuya" (16 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1731 | 「ふやぁぁぁっぁぁぁんっ！　みくろ、好きっ！！\nこれ、しゅきっ！　ぐりゅって、されるのい、しゅきぃ」 | 「呼啊啊啊啊啊啊嗯！美玖路好喜歡這樣！這樣真棒！頂來頂去的，好喜歡」 | 「Phuyaaaaaaan! Mikuro, thích lắm!!\nCái này, thích lắm! Được cọ xát, thích lắmmm」 | 「Fuyaaaaaaan! Mikuro, thích lắm!!\nCái này, thích lắm! Được cọ xát, thích lắmmm」 | ふやぁぁぁっぁぁぁんっ → "Fuyaaaaaaan" (7 a, kiểm bằng máy) Số a kiểm bằng máy: JP や=1 + ぁ=6 → VN 7 a — chỉ thay tiền tố "Phuya" bằng "Fuya". |
| ふかみh3_夏休みの最後の日の、前の日 | 2366 | 「はうっ――んっ――ふっ――指、それっ――\nふやんっ！　くりって、され、るとぉっ」 | 「啊……嗯……呼……手指，呀！這樣摳弄……」 | 「A ư—— ưm—— phù—— ngón tay, cái đó——\nPhuyan! Bị, miết, hột le, thì」 | 「A ư—— ưm—— phù—— ngón tay, cái đó——\nFuyan! Bị, miết, hột le, thì」 | ふやんっ → "Fuyan" |
| れいなh1_おかあさんのレッスン | 1263 | 「ふや……ぁ……きもち……いい、ですぅ――んっ」 | 「呀啊……好舒服……啊嗯」 | 「Phuya……a……sướng……quá, ạ~――ưm.」 | 「Fuya……a……sướng……quá, ạ~――ưm.」 | ふや → "Fuya" |
| れいなh1_おかあさんのレッスン | 1525 | 「ぁっ……ふやっ――だめっ……ら、めぇっ」 | 「蛤啊……不行……不行啦」 | 「A……phuya――không được……kh-không được.」 | 「A……Fuya――không được……kh-không được.」 | ふやっ → "Fuya" |
| れいなh1_おかあさんのレッスン | 1531 | 「ふやっ――あっ――あっ――あっ――」 | 「蛤啊……啊、啊啊啊……」 | 「Phuya――a――a――a――」 | 「Fuya――a――a――a――」 | ふやっ → "Fuya" |
| ハチロクh4_ゼリー・シリンジ・コンドーム | 1121 | 「そ、双鉄さまぁっ――ふやっ――これっ――\nしゅごっ――くひいいいっんっ！」 | 「雙、雙鐵少爺——嗚呀——這下——好——好厲害嗯！」 | 「N, ngài Soutetsu——phuya——cái này——\ntuyệt quá——kư hi i i i ưm!」 | 「N, ngài Soutetsu——fuya——cái này——\ntuyệt quá——kư hi i i i ưm!」 | ふやっ → "fuya" (giữ chữ thường giữa chuỗi) Giữ chữ thường giữa chuỗi ("fuya") theo casing của dòng. |
| ハチロクh4_ゼリー・シリンジ・コンドーム | 988 | 「ふやっ！？」 | 「嗚呀！？」 | 「Phuya!?」 | 「Fuya!?」 | ふやっ → "Fuya" |
| ポーレットh2_制服変更？ | 929 | 「ひゃっ――あっ！\nんううっ――ふえっ――ふやぁっ」 | 「呀——啊！嗯——呼——呀」 | 「Hya——á!\nNuu——phuê——phuyaa.」 | 「Hya——á!\nNuu——phuê——Fuyaa.」 | ふやぁっ → "Fuyaa" (2 a) Chỉ sửa token ふや; ふえっ trong cùng dòng ("phuê") KHÔNG sửa — cờ cho M10 (xem §5). |
| ポーレットh2_制服変更？ | 957 | 「ふぇ……あ……ふやぁぁぁあ」 | 「呼……啊……啊呀」 | 「Phuê... a... phuyaaaaa.」 | 「Phuê... a... Fuyaaaaa.」 | ふやぁぁぁあ → "Fuyaaaaa" (5 a) Chỉ sửa token ふや; ふぇ trong cùng dòng ("Phuê") KHÔNG sửa — cờ cho M10 (xem §5). |
| 凪h1_ふたりっきりのデート | 1053 | 「ふやっ――あっ――これ――これ――んっ――\nおしり――あったかで――きもち――よかっ」 | 「呀……啊……這個……這個……嗯……屁股……熱熱的……好舒服」 | 「Phuya——A——Cái này——Cái này——Ưm——\nMông——Ấm quá——Sướng——quá」 | 「Fuya——A——Cái này——Cái này——Ưm——\nMông——Ấm quá——Sướng——quá」 | ふやっ → "Fuya" |
| 凪h1_ふたりっきりのデート | 1057 | 「ふやっ！」 | 「呀！」 | 「Phuya!」 | 「Fuya!」 | ふやっ → "Fuya" |
| 凪h1_ふたりっきりのデート | 1081 | 「ふやうっ！」 | 「哇！」 | 「Phuyau!」 | 「Fuyau!」 | ふやうっ → "Fuyau" |
| 日々姫h2_洗って大丈夫なスーツ | 1081 | 「ふやんっ！！」 | 「哎呀！！」 | 「Phuyan!!」 | 「Fuyan!!」 | ふやんっ → "Fuyan" |
| 日々姫h3_汚れてしまった制服で | 1042 | 「ふやっ！？　にぃに――舐めてっ――んっ――\nふあっ――あっ――ぺろ、ぺろ――おも――らしっ」 | 「呀！？阿哥――舔了――嗯――呼――啊――舔了――我的尿」 | 「Phuya!? Anh hai――đang liếm――ưm――\nFua――a――liếm, liếm――nước tiểu――của em」 | 「Fuya!? Anh hai――đang liếm――ưm――\nFua――a――liếm, liếm――nước tiểu――của em」 | ふやっ → "Fuya" |
| 日々姫h4_いもうとタオル | 964 | 「いうっ！？　――かっ――ふやっ――\nあぁぁぁぁぁああああああああんっ！！！」 | 「呀！？――唔――呀――啊啊啊啊啊！！！」 | 「Iu!? ――Ka――Phuya――\nAaaaaaaaaaaaaan!!!」 | 「Iu!? ――Ka――Fuya――\nAaaaaaaaaaaaaan!!!」 | ふやっ → "Fuya" |
| 真闇h1_長期熟成 | 1021 | 「ふや……んっ――きもち、い――」 | 「呼……嗯――好舒服――」 | 「Phuya……ưm――sướng, quá――」 | 「Fuya……ưm――sướng, quá――」 | ふや → "Fuya" |

## 3.6. M15 — ん+phụ âm H-scene → romaji (11 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| 日々姫h4_いもうとタオル | 1075 | 「深っ――コレッ――んあっ！　違うとこ――ぐりって！\nひぁっ――あっ――えぐれ――って――んきゅっっ！！」 | 「好深――這樣――嗯！頂的地方――不對！呀――啊――插到了――嗯哼！！」 | 「Sâu quá――Thế này――ưm a! Chỗ khác――bị ngoáy rồi!\nHia――a――Bị khoét sâu――vào trong――Nkyu!!」 | 「Sâu quá――Thế này――Na! Chỗ khác――bị ngoáy rồi!\nHia――a――Bị khoét sâu――vào trong――Nkyu!!」 | んあっ → "Na!" |
| 真闇h1_長期熟成 | 1080 | 「ん……双ちゃん――あっ――太っ――――んふっ」 | 「嗯……小雙――啊――好粗――嗯唔」 | 「Ưm……Sou-chan――a――to quá――――ưm phư.」 | 「Ưm……Sou-chan――a――to quá――――Nfu.」 | んふっ cuối dòng → "Nfu" |
| ハチロクh7_レトロモダンメイクラヴ | 745 | 「か……は……あっ――ぐっ――んっ――そ――ん、な、\nいき、なり――いき――なりッ――んきゅうう！！？」 | 「呃……啊——咕——嗯——那樣——的，突然——就——就——嗯啊——！！？」 | 「Ka……ha……a——Gu——ưm——như——vậy,\nđột, nhiên——đột——nhiên——ưn kyuuu!!?」 | 「Ka……ha……a——Gu——ưm——như——vậy,\nđột, nhiên——đột——nhiên——Nkyuuu!!?」 | んきゅうう (3u) → "Nkyuuu" |
| ハチロクh7_レトロモダンメイクラヴ | 843 | 「んっきゅぅぅぅぅぅぅぅぅぅうっぅううううう！！」 | 「嗯嗚——！！」 | 「Ưn kyuuuuuuuuuuuuuuuuu!!」 | 「Nkyuuuuuuuuuuuuuuuuu!!」 | んっきゅ… (tổng 17u) → "Nkyu" + 17u Số u kiểm bằng máy: JP tổng 17u, VN cũ 17u — chỉ thay tiền tố "Ưn " bằng "N", giữ nguyên độ dài. |
| ハチロクh8_桜色のひめごと | 1561 | （んくっ！　ごくっ！　ごくっ！！　ごくんっ！！） | （嗯嗯！嗯！嗯！！嗯！！） | （Ưn ku! Ực! Ực!! Ực!!） | （Nku! Ực! Ực!! Ực!!） | んくっ → "Nku" Dòng nằm trong （ ） — chỉ sửa token đối thoại んくっ, cờ ranh giới cho U12b. |
| ハチロクh8_桜色のひめごと | 821 | 「ん……ふあっ――あっ――んくっ――おまん、まん――\nんっ――ひ――くっ――ぞりって――する、とこっ――」 | 「嗯……呼啊——啊——嗯——小妹妹——嗯——咿——抽緊——被插的——部位——」 | 「Ưm……Fua——a——ưn ku——tiểu, huyệt——\nưm——hi——khục——bị chà xát——rồi——」 | 「Ưm……Fua——a——Nku——tiểu, huyệt——\nưm——hi——khục——bị chà xát——rồi——」 | んくっ → "Nku" |
| ハチロクh8_桜色のひめごと | 759 | 「あ――出てッ――んっ――熱、い――んくっ――ふ――\n双鉄、さまの――精子――あつい、のっ――ふ、ふぁ」 | 「啊——出來了——好熱——嗯——呼——雙鐵少爺的——精子——好熱——呼，嗚啊」 | 「A——ra rồi——ưm——nóng, quá——ưn ku——phù——\nTinh trùng——của Ngài Soutetsu——nóng, quá——phù, fa」 | 「A——ra rồi——ưm——nóng, quá——Nku——phù——\nTinh trùng——của Ngài Soutetsu——nóng, quá——phù, fa」 | んくっ → "Nku" |
| lr真闇追加h_赤ちゃん、欲しか | 1097 | 「ふあっ――んっっ――んくっ――く――はっ」 | 「呼啊——嗯——嗯——呼——啊」 | "「Fua——ưm——ưm ku——Ku——ha.」" | "「Fua——ưm——Nku——Ku——ha.」" | んくっ → "Nku" Giữ nguyên dấu ngoặc kép ASCII "..." vốn có trong giá trị moan; token く sau đó giữ "Ku". |
| lr_稀咲h1_おしおきとごほうび | 1162 | 「ボクも！　そうっ！　なのっ！　んっ――どくん、\nどくんて――双鉄の、ペニスの、先、から――んうっ！」 | 「我也是！啊嗯！蛤啊啊！你的龜頭……一直撞在裡面！」 | 「Em cũng! Vậy! Đó! Ưm――thình thịch,\nthình thịch――từ đầu, dương vật, của Soutetsu――ưn ư!」 | 「Em cũng! Vậy! Đó! Ưm――thình thịch,\nthình thịch――từ đầu, dương vật, của Soutetsu――Nu!」 | んうっ → "Nu!" |
| 真闇h3_補習授業の廃校舎 | 2323 | 「ん……や……ちくび――ンッ――くに、くに――\nそぎゃん、と――しつこく、され、たら――」 | 「嗯……呀……乳頭――嗯――擠、擠――別那麼――一直揉啊揉的――」 | 「Ưm……á……núm vú――ưn――bóp, bóp――\nbị trêu chọc――dai dẳng, như thế――」 | 「Ưm……á……núm vú――ưm――bóp, bóp――\nbị trêu chọc――dai dẳng, như thế――」 | ん(っ) trần → "ưm" |
| 真闇h3_補習授業の廃校舎 | 2328 | 「ん……はっ――ん……双ちゃん……て……\nやらし……んっ――ねっとり、して、てっ」 | 「嗯……哈――嗯……小雙……手……好下流……嗯――黏糊糊的」 | 「Ưm……há――ưm……tay của……Sou-chan……\ndâm đãng quá……ưn――dính, nhớp nháp, quá.」 | 「Ưm……há――ưm……tay của……Sou-chan……\ndâm đãng quá……ưm――dính, nhớp nháp, quá.」 | ん(っ) trần → "ưm" |

## 3.7. M68 — れろ dài → romaji "Rero" (18 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| ハチロクh8_桜色のひめごと | 841 | 「んむっ！　ん――むっ！！　じゅろろっ！　ちゅむ！　\n（すっ――ひっ）ちゅるっ！　れろおおおおおおっ！」 | 「嗯姆！嗯——姆！！呲啾——！啾嗯！（做——哈）啾嚕！咻嚕——！」 | 「Ưm mu! Ưm——mu!! Chóp chép! Chụt!\n（Su——hi）Chụt! Liếm láp!!」 | 「Ưm mu! Ưm——mu!! Chóp chép! Chụt!\n（Su——hi）Chụt! Rerooooooo!!」 | れろ×6お → "Rero" + 7 o |
| 日々姫h3_汚れてしまった制服で | 1857 | （れろおおおおおっっ） | （用力舔） | （Liếm láp） | （Reroooooo） | れろ×5お → "Rero" + 6 o |
| れいなh2_おもらし防止大作戦 | 1084 | 「じゅぼっ！　じゅちゅっ！　じゅっ！　じゅるるっ！\nくぽっ！　　じゅるっ！　ずるるっ！　れろおおおっ！」 | 「啾嚕嚕嚕……啾！啾！啾、啾、啾嚕、啾噗！」 | 「Chụt! Chụt! Chụt! Chụt!\nChụt! Chụt! Chụt! Chụt!」 | 「Chụt! Chụt! Chụt! Chụt!\nChụt! Chụt! Chụt! Reroooo!」 | れろ×3お → "Rero" + 4 o (chỉ token cuối) Chỉ sửa token CUỐI (れろおおおっ); 7 token "Chụt!" đầu là じゅぼっ/じゅちゅっ… giữ nguyên. |
| れいなh2_おもらし防止大作戦 | 1114 | 「ひゃいれふぅ――んッ――れろおおおおおおっ――\nんむっ――ぷあっ！　ぷはっ！　はぁっ……はぁっ」 | 「好的……嗯……啾嚕嚕嚕……嗯……噗哈！蛤啊、蛤啊……」 | 「Vâng ạ——ưm——chụt——\nƯm——Pua! Puha! Haa……Haa」 | 「Vâng ạ——ưm——Rerooooooo——\nƯm——Pua! Puha! Haa……Haa」 | れろ×6お → "Rero" + 7 o |
| 凪h1_ふたりっきりのデート | 1772 | （にゅうううっ！　べろっ！　れろおおおっ！） | （啾！啾！啾！） | （Trườn! Liếm! Liếmmmm!） | （Trườn! Liếm! Reroooo!） | れろ×3お → "Rero" + 4 o (Nhóm 2) |
| 凪ふかみh1_修学旅行の夜 | 1317 | 「わかったばい！　勝負どころで、スパートばいっ！\nれろおおおおおおおおっ！」 | 「好的！決勝時刻，衝刺了！啾！」 | 「Em hiểu rồi nha! Đến lúc quyết định rồi, tăng tốc thôi!\nLiếmmmmmmmm!」 | 「Em hiểu rồi nha! Đến lúc quyết định rồi, tăng tốc thôi!\nRerooooooooo!」 | れろ×8お → "Rero" + 9 o (Nhóm 2) |
| lr_凪ふかみh1_じぇいけい！ | 1633 | 「れろおおおおおおおおおおおおおおおおっ！！！！」\n「べちゅううううううううううううううううっ！！！！」 | 「啾！」\n「啾！」 | 「Liếmmmmmmmmmmmmmmmm!!!!」\n「Chụtttttttttttttttt!!!!」 | 「Rerooooooooooooooooo!!!!」\n「Chụtttttttttttttttt!!!!」 | れろ×16お → "Rero" + 17 o (Nhóm 2; chỉ dòng 1) Chỉ sửa dòng 1 (れろ); dòng 2 べちゅう… ("Chụtttt…") KHÔNG động — thuộc U12b. |
| lr_ニイロクh_誓い。約束 | 2060 | （れろおおおおおっ） | （舔拭） | （Liếmmmm） | （Reroooooo） | れろ×5お → "Rero" + 6 o (Nhóm 2) |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1704 | 「ふっ──んっ──ちゅうっ──れるっ──れろおおお」 | 「呼——嗯——啾——咧溜——滋溜溜溜」 | 「Phu──ưm──chụt──liếm──liếmmmmm」 | 「Phu──ưm──chụt──liếm──Reroooo」 | れろ×3お → "Rero" + 4 o (Nhóm 2) |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1854 | 「んむっ──ちゅっ──れりゅっ──れろおおおおおっ」 | 「嗯唔——啾——咧溜——滋溜溜」 | 「Ưm──chụt──liếm──liếmmmmm」 | 「Ưm──chụt──liếm──Reroooooo」 | れろ×5お → "Rero" + 6 o (Nhóm 2) |
| lr_れいなh1_レディ・れいな | 1372 | 「はいですぅ。そうてつさん汗かいちゃいましたかぁ？\nチュッ――れろおおおおおおおおおおおおおおおっ」 | 「是的。雙鐵先生出汗了嗎？啾——舔——」————————————」 | 「Vâng ạ~. Anh Soutetsu bị đổ mồ hôi rồi sao ạ~?\nChụt——liếm m m m m m m m m m m m m m m m」 | 「Vâng ạ~. Anh Soutetsu bị đổ mồ hôi rồi sao ạ~?\nChụt——Reroooooooooooooooo」 | れろ×15お → "Rero" + 16 o (Nhóm 2) |
| 凪ふかみh2_みずあそび | 1030 | 「……れ……るっ――ふっ――んっ――るろっ――\nろっ――れるうっ――れろっ――れろおおおお」 | 「……舔……呼……嗯……舔……舔……啾……啾……啾」 | 「...Liếm... liếm——phù——ưm——liếm——\nliếm——liếm——liếm——liếmmmmm」 | 「...Liếm... liếm——phù——ưm——liếm——\nliếm——liếm——liếm——Rerooooo」 | れろ×4お → "Rero" + 5 o (Nhóm 2; chỉ token dài cuối) Chỉ sửa token dài cuối; các token れろ/れる ngắn giữ "liếm". |
| ハチロクh7_レトロモダンメイクラヴ | 1840 | （れろおおおおっっ） | （咻嚕——） | （Liếm dài——） | （Rerooooo——） | れろ×4お → "Rero" + 5 o (Nhóm 2) Quyết coordinator Nhóm 2 thắng ghi chú M14 của F1 ("giữ Liếm dài") — thống nhất romaji. |
| ハチロクh7_レトロモダンメイクラヴ | 1878 | （れろっ――れるっ――れろおおおお――はぷっ！） | （嗯——咻嚕——咻嚕——哈噗！） | （Liếm——liếm——liếm dài——ngoạm!） | （Liếm——liếm——Rerooooo——ngoạm!） | れろ×4お → "Rero" + 5 o (Nhóm 2; chỉ token dài) Chỉ sửa token dài ("liếm dài"); hai token ngắn đầu giữ "Liếm/liếm". |
| lr_日々姫ふかみh1_凪ちゃんの代わり | 1461 | 「ちゅむ――れりゅっ――れろおおおっ――ずりゅっ――\nちゅむっ――ちゅっ――ずりゅうううっ――（こくっ）」 | 「啾唔——滋溜——滋溜溜——滋溜——啾唔——啾——滋溜溜——（嚥下）」 | 「Chùn chụt――rê ryu――rê roooo――zuryu――\nChùn chụt――chụt――zuryuuu――（Ực）」 | 「Chùn chụt――rê ryu――Reroooo――zuryu――\nChùn chụt――chụt――zuryuuu――（Ực）」 | "rê roooo" → "Reroooo" (chuẩn hóa, 4 o) |
| 凪h2_おとなの水着 | 2546 | 「べろっ――ぺろっ――れるっ――にゅちゅっ――\nちゅっ――ちゅむ――ぺろっ――れろおおおおっ」 | 「啾，啾，啾，啾，啾，啾，啾，啾」 | 「Liếm——Liếm——Ngoáy——Nhóp nhép——\nChụt——Chụt——Liếm——Ngoáyyyyyy」 | 「Liếm——Liếm——Ngoáy——Nhóp nhép——\nChụt——Chụt——Liếm——Rerooooo」 | れろ×4お → "Rero" + 5 o (thay "Ngoáyyyyyy") |
| lr_凪ふかみh1_じぇいけい！ | 1640 | 「ちゅううっ――ちゅぶっ――ぐちゅっ――ずちゅっ――\nちゅぐっ――グチュッ――じゅるる――れろおおおっ！」 | 「啾，啾，啾……啾，啾，啾……啾，啾！」 | 「Chụt——chụt——nhóp nhép——nhóp nhép——\nchụt——nhóp nhép——sột soạt——liếm!」 | 「Chụt——chụt——nhóp nhép——nhóp nhép——\nchụt——nhóp nhép——sột soạt——Reroooo!」 | れろ×3お → "Rero" + 4 o (SWEEP-ADDED) SWEEP-ADDED (không có trong list tay của F1): れろおおおっ bị mất độ dài, chỉ còn "liếm!" — cờ cho coordinator duyệt/xóa. |
| lr_稀咲h1_おしおきとごほうび | 1056 | 「ちゅうううううっ！　ずりゅっっっ！　ぢゅぼっ！\nれるっ――れろおおおおおっ！　ちゅうっ！　ぢゅっ！」 | 「啾嚕嚕嚕！啾噗、啾！啾嚕嚕嚕……啾！啾！」 | 「Chuuuuu! Juryu! Jubo!\nReru――rero o o o o o! Chuu! Ju!」 | 「Chuuuuu! Juryu! Jubo!\nReru――Reroooooo! Chuu! Ju!」 | れろ×5お → "Rero" + 6 o (SWEEP-ADDED, chuẩn hóa) SWEEP-ADDED: đã romaji nhưng viết rời "rero o o o o o" — chuẩn hóa spacing/case (cùng lớp với 1461). |

## 3.8. M70 — きゅ (真闇h2 1842) (1 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| 真闇h2_無濾過 | 1842 | （きゅっ――くぽっっ――きゅぷっ――きゅうっ） | （啾――啪――啾唔――壓） | （Thắt lại――phập――kypu――kyuu） | （Thắt lại――phập――kypu――Thắt lại） | Hệ romaji của file (quyết M70) Hệ romaji của file: token ngắn → nghĩa; きゅうっ (1う, TW 壓) → "Thắt lại" như 1846; きゅぷっ không có nghĩa VN trong file nên giữ "kypu". |

## 4. Đã kiểm chứng, giữ nguyên (không sửa)

**M7 — giữ:** "Kuh" (lr稀咲追加h 1079); "khục" (ハチロクh7 783, 846); "kư" (lr_稀咲h1 972/1190/1260); cụm động từ "Ngoáy"/"Thúc" (ポーレットh3 894, れいなh2 1047, lr_ハチロクh1 1423, 日々姫h5 1177/1321, ハチロクh3 1815, ポーレットh4 1008 いっ――くっ→"Ra——mất"); うくっ→"Ư ku"/"ư ku" (lr_稀咲ポーレットh1 1594, ふかみh2 1034 — đã có "ku"); token んくっ (lớp M15, không phải M7); くっ trong từ (まくって, 応えたくって, くっついて, くったり, くっきり, くっぽり, おくっ, ふかくっ, あつくっ — đều đã diễn nghĩa); mọi dòng （ごくっ）/（ ） không động. 4 file quy ước giữ "Hự" (11 dòng: lr_ふかみh2 4, 日々姫h1 4, ハチロクh2 2, lrれいな追加h 1).

**M8 — giữ:** lr_稀咲h1 991 "Yaa!", lr_日々姫ふかみh1 1334 "Ya!?" (đã quyết giữ); dòng đã diễn nghĩa: 凪h1 1105, lr_れいな追加h 1048, ハチロクh8 708 (音、やっ→"xấu hổ, quá"), 真闇h2 1046 (やっ→"khoan"), 日々姫h6 2405 (やぁ gộp vào "không chịu, đâu"). Ranh giới Ya-vs-Á mơ hồ — GIỮ nguyên quyết định của agent moan/audit (không phải dòng "A" trần): lr_日々姫真闇h1 1445 やあっ→"ya!" (trước là token rên あっ, sau là từ こぎゃんっ — hai quy tắc xung đột), ポーレットh5 862 "Yaa!?" (cấu trúc giống hệt 1334 đã giữ), ポーレットh5 927 "Ya!", 日々姫h3 1007 "Yaa", 日々姫h3 1070 "Ya", 真闇h1 1010 "Ya", 真闇h2 1084 "ya" (chữ thường giữa chuỗi).

**M9 — giữ:** lr_日々姫ふかみh1 "Hư" (1350/1479); lr_真闇h1 "fu" chữ thường (1440/1556 — đã romaji, chỉ khác case giữa chuỗi, không chuẩn hóa case trong đợt này). Nhánh "độc lập → giữ phù" của quyết M9 không có mẫu trong đợt này: cả 3 dòng ハチロクh9 đều trong chuỗi rên nên đều → "Fu"; file sau đợt này thống nhất "Fu" 6/6.

**M10 — giữ:** reina-h3 1133 "Hả?" (không động theo quyết); kéo dài 1547 "Phuêê.", 2038 "Phuêêêêê!?", 2170 "Phuêê……" (2170 thuộc ハチロク02_ハートブレイク・レイルロオド, không phải file 8620運転台通信 như F1 ghi); lr_稀咲h1 991 "Fue!?" (chuỗi rên).

**M11 — giữ:** đối thoại non-H "phuya" (quy tắc fa/fu đã khóa); 日々姫h6 2090 ふやしたら = động từ 増やす, đã diễn nghĩa.

**M15 — giữ:** ポーレットh4 878 ぅんっ→"ưn"; các dòng "nn"/"mm" đã đúng; れいなh3 1054 んくっ→"nku" (đã romaji, chữ thường giữa chuỗi — giữ).

**M68 — giữ:** romaji đã đúng (đếm o kiểm bằng máy): lr_日々姫真闇h1 1757 "reroooo" (4 o), ハチロクh2 1038 "Reroooo", ポーレットh3 966 "Reroooo", 日々姫h4 1052 "Reroooo", 真闇h3 2198 "reroooo"/"rerooooo" (4/5 o). Dòng "rộp" (14) không động — chờ T77.

**M70 — giữ:** toàn bộ file 真闇h2 ngoài 1842, theo hệ của file (ngắn → nghĩa, dài ≥3 → romaji; tiền lệ: 1846 きゅんっ→"Thắt lại" + きゅううううっ→"Kyuuuuu"; 1848 dài→romaji; đối thoại 1084 "Kyu!", 1088 "nkyun"; 986 きゅんきゅん đối thoại → nghĩa).

## 5. Cờ cho coordinator

**F1 — M7: F1 đếm thiếu "Hự" (cờ lớn nhất).** Quyết M7 ghi "5 dòng Hự lẻ", nhưng quét token-by-token còn **59 dòng đối thoại** khác có token くっ độc lập đang diễn "Hự"/"hự", ngoài 4 file quy ước và 5 dòng đã đổi. Quy tắc M7 như được viết ("token đối thoại H-scene → Ku", ngoại lệ = 4 file + "kư" + cụm động từ) sẽ đổi hết 59 dòng này, nhưng chỉ 5 dòng được nêu tên. KHÔNG tự đổi — chờ quyết follow-up của coordinator. Đếm bằng máy (dòng đối thoại trong H-file, JP có token くっ/くっっ độc lập, VN hiện tại chứa "Hự"/"hự", loại 4 file quy ước + 5 dòng đã đổi):

| File | Số dòng |
|---|---|
| 日々姫h5_白濁絵の具の射精会 | 10 |
| lr_凪h2_虎さんの交尾 | 5 |
| lr_凪ふかみh1_じぇいけい！ | 4 |
| lr_日々姫h2_デザートは食事の前に | 4 |
| lr稀咲追加h_お風呂は日ノ本式に限るね | 4 |
| ポーレットh4_クリーム＆クリーム | 4 |
| lr_ふかみh1_ふかみうさぎのたまご | 3 |
| ポーレットh8_気動車の国のアリス | 3 |
| 日々姫h6_オリエンテーリング借り物競走（ペア） | 3 |
| lr_ポーレットh2_デコレーション＆ミルク | 2 |
| lr_凪h1_痛いの痛いの飛んでけばい | 2 |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 2 |
| ポーレットh2_制服変更？ | 2 |
| 凪ふかみh1_修学旅行の夜 | 2 |
| 日々姫h3_汚れてしまった制服で | 2 |
| lr_ポーレットh1_家族旅行の最終日の夜 | 1 |
| れいなh1_おかあさんのレッスン | 1 |
| ハチロクh1_契り | 1 |
| ハチロクh3_磨き洗い | 1 |
| ポーレットh1_ファーストセックス | 1 |
| ポーレットh5_裸エプロンのレモンドレッシング和え | 1 |
| ポーレットh7_残業エッチもyシャツで | 1 |
| **Tổng** | **59** |

Lưu ý: đếm này là liệt kê cơ học theo token; coordinator nên xác nhận từng dòng theo token trước khi quyết (cùng lưu ý như số 280 bị nhiễm của F1).

**F2 — M15 sweep: ~154 dòng dạng tách ("Ưm kyu" 15, "Ưm ku" 16, "Ưm a" 13, "Ưm fu" 13, "Ưm phù" 9, "Ưn ku" 6, …) KHÔNG đổi.** Đây là quy ước nhất quán theo file (vd. ポーレットh2 "Ưm kyu", ハチロクh6 "Ưm kiu"/"ưm ku"), không nằm trong list 11 dòng đã nêu tên. Khoảng trống giữa quy tắc như được viết và list đã nêu tên — cần coordinator quyết. Các dòng đơn lẻ liên quan cũng cờ lại: ハチロクh3 1042 んくっ→"ưm", 凪h2 2501 んくっ→"Ư", 凪h2 2489 んひゅっ→"Ưm hứ", ふかみh3 2302 んくっ→"Ực", lr_れいな追加h 1221 んくっ→"Ưm", 真闇h3 2348 んふっ→"Ưm phư", れいなh3 1054 んくっ→"nku" (đã romaji, giữ).

**F3 — M7 ふかみh2 989:** くっ→"Kh" — giữ theo khóa "Kh" (glottal-stop っ), cờ lại vì mâu thuẫn với quy tắc M7 ("Ku"). Cần coordinator quyết (M7 vs khóa Kh).

**F4 — M68 sweep-added (2 dòng, không có trong list tay của F1):** lr_凪ふかみh1 1640 (れろおおおっ bị mất độ dài, chỉ còn "liếm!") và lr_稀咲h1 1056 ("rero o o o o o" — chuẩn hóa spacing/case, cùng lớp với 1461). Đã đổi trong đợt này; coordinator có thể gạch nếu không đồng ý.

**F5 — M10 cờ trong dòng M11:** ポーレットh2 929 (ふえっ→"phuê") và 957 (ふぇ→"Phuê") nằm trong chuỗi rên — theo M10 quy tắc 1 sẽ là "Fue", nhưng không có trong list M10 đã nêu tên; đợt này chỉ sửa token ふや. Cần quyết follow-up cho M10.

**F6 — M8 ranh giới Ya-vs-Á:** 6 dòng giữ nguyên đã liệt kê ở §4 (1445, 862, 927, 1007, 1070, 1010) + 真闇h2 1084 "ya" chữ thường. Hai quy tắc (theo sau là từ → Á; trong chuỗi rên → Ya) xung đột ở các dòng này; quyết giữ hiện tại được ghi lại để coordinator soi.

**F7 — Sửa số liệu F1:** 4 file quy ước M7 giữ **11 dòng Hự**, không phải 12 (lr_ふかみh2 4 + 日々姫h1 4 + ハチロクh2 2 + lrれいな追加h 1); lrれいな追加h 1221 không phải Hự. F1 ghi lr_ニイロクh "Fu 2" — thực tế "Fu" ×3 (1339, 1342, 1569). F1 ghi ハチロク02 2170 thuộc file 8620運転台通信 — thực tế thuộc ハチロク02_ハートブレイク・レイルロオド.

**F8 — Ranh giới với U12b:** ハチロクh8 1561 là dòng M15 đã nêu tên nhưng nằm TRONG （ ） — đợt này đã sửa token んくっ→"Nku" và cờ lại để U12b biết khi xử lý （ ） SFX của dòng này. Ngoài ra, các dòng M68 có （ ） trong fix (841, 1857, 1772, 2060, 1840, 1878) chỉ đổi token れろ dài, không động số lượng/kiểu chữ của các SFX （ ） khác trong cùng dòng.

**F9 — Trùng lặp:** đối chiếu 99/99 cặp (file, key) với mọi `unification-*-wrong.json` đã gộp — **0 trùng**. `old_vn` đã lấy theo thứ tự moan > audit > unification-đã-gộp > CSV3; không dòng nào bị sửa đè.

## 6. Lượt soát 2 (bắt buộc — đọc lại toàn bộ fix theo JP)

- **Tổng: 99 / tái kiểm chứng: 99 / loại: 0 / sửa: 0.** Đọc lại toàn bộ JSON đã ráp, từng fix đối chiếu JP (+TW) một lần nữa từ đầu; không phát hiện lỗi nào ở lượt soát 2.
- **Diff cơ học:** mỗi fix chỉ khác `old_vn` đúng ở span token cần sửa (99/99) — kiểm bằng difflib; hai trường hợp chèn/xóa span: M7 1041 chèn "Ku——" (token bị bỏ mất), M68 1056 xóa khoảng trắng "rero o o o o o" → "Reroooooo".
- **Đếm chữ bằng máy:** M68 18/18 đúng số o theo JP (1 + số お/ぉ); ハチロクh7 843 tổng 17u (JP 17u, VN cũ 17u); lr追加_みくろ＆日々姫h 1731 tổng 7a (JP や=1 + ぁ=6).
- **Khối TOML:** 43 file / 99 key parse-verified, 0 lệch (giá trị `\n` chữ trong fix được viết `\\n` trong khối; xem §7).

## 7. Khối TOML (parse-verified, theo file)
# lr_ふかみh1_ふかみうさぎのたまご.txt.toml
[script]
"1469" = "「Fa! Đột nhiên! Đột nhiên, như vậy! Như vậy,\\nưm, Ku! A! Mạnh quá! Mạnh quá đi!!」"

# lr_ふかみh2_セックスの意味.txt.toml
[script]
"1275" = "「Fa! A! Đang vào! Ưm!\\nTừng chút, một——Fa——Ya, a——nóng, quá.」"

# lr_れいなh1_レディ・れいな.txt.toml
[script]
"1225" = "「Ku!!!」"
"1372" = "「Vâng ạ~. Anh Soutetsu bị đổ mồ hôi rồi sao ạ~?\\nChụt——Reroooooooooooooooo」"

# lr_ニイロクh_誓い。約束.txt.toml
[script]
"1571" = "「Âm, vật, cũng──Fu! A! Cửa, âm đạo,\\ncũng──cả lỗ, đi tiểu──tất cả, tất cả」"
"2060" = "（Reroooooo）"

# lr_ハチロクh2_新しい服。新しい旅.txt.toml
[script]
"1464" = "「A——a——ưm——Ku」"
"1486" = "「Ưm——Ku——aƯ!」"

# lr_ポーレットh1_家族旅行の最終日の夜.txt.toml
[script]
"959" = "「Á, ừm,\\nkhông phải là em muốn anh làm, mà là」"
"995" = "「Á――em muốn, em muốn anh làm, cho em――ưm,\\nBởi anh Soutetsu――bởi người chồng, mà em yêu nhất」"
"1018" = "「Fue!? Á――Anh Soutetsu――không được――\\nNgón tay――ưm――trong, âm đạo――đang mở rộng ra」"
"1026" = "「Ha——ưm——phù, phù——ưm! A,\\nEo, tiếp tục đi——Ku, phu——anh Soutetsu——a!」"
"1086" = "「Ưm――Ya――hà――ưm――phù」"
"1100" = "「Ưm! ――Fa――Yaan――Ngón tay――ưm! Đột nhiên――hai, ngón――hi――a――」"
"1221" = "「Á, thiệt tình, xé rách thế này thì――\\nĐang đi du lịch đấy nhé? Em đâu có mang theo đồ dự phòng đâu」"

# lr_ポーレットh2_デコレーション＆ミルク.txt.toml
[script]
"1013" = "「Ya! Ha! Mãnh liệt quá! Ưm! Thế này!\\nCả ngực! A——cả âm đạo——nữa!!」"
"1041" = "「Ha! A! A——a——aa!!\\nAnh, Soutetsu——Ku——a! Em——sắp」"

# lr_凪h1_痛いの痛いの飛んでけばい.txt.toml
[script]
"1190" = "「A……Sắp, được rồi——ưm——Ku——fua!\\nMột, chút nữa thôi——là vào đến, tận cùng——bên trong, rồi」"

# lr_凪h2_虎さんの交尾.txt.toml
[script]
"1203" = "「Fua! Áa! Áaaa! Cậu nhỏ của anh,\\nưm——hỏng——hỏng mất——Áa!」"

# lr_凪ふかみh1_じぇいけい！.txt.toml
[script]
"1633" = "「Rerooooooooooooooooo!!!!」\\n「Chụtttttttttttttttt!!!!」"
"1640" = "「Chụt——chụt——nhóp nhép——nhóp nhép——\\nchụt——nhóp nhép——sột soạt——Reroooo!」"

# lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml
[script]
"1265" = "「Không…… được! A――Ku――anh, ra mất!」"
"1432" = "「A――Ku!」"
"1461" = "「Chùn chụt――rê ryu――Reroooo――zuryu――\\nChùn chụt――chụt――zuryuuu――（Ực）」"

# lr_真闇h1_僕のおねえちゃん.txt.toml
[script]
"1457" = "「Ư, m……Fu——a——Nfufu——Sou, chan」"

# lr_稀咲h1_おしおきとごほうび.txt.toml
[script]
"992" = "「Hể!? A! Á――không――\\nkhông có gì……không có gì đâu……chỉ là――Ư á――」"
"1056" = "「Chuuuuu! Juryu! Jubo!\\nReru――Reroooooo! Chuu! Ju!」"
"1162" = "「Em cũng! Vậy! Đó! Ưm――thình thịch,\\nthình thịch――từ đầu, dương vật, của Soutetsu――Nu!」"

# lr_稀咲ポーレットh1_悪い大人の契約.txt.toml
[script]
"1523" = "「Ha! A!? Á——không thể nào——Fua—— Đầy ắp, rồi mà——căng cứng, chật chội, thế mà.」"

# lr真闇追加h_赤ちゃん、欲しか.txt.toml
[script]
"1097" = "\"「Fua——ưm——Nku——Ku——ha.」\""

# lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml
[script]
"1704" = "「Phu──ưm──chụt──liếm──Reroooo」"
"1731" = "「Fuyaaaaaaan! Mikuro, thích lắm!!\\nCái này, thích lắm! Được cọ xát, thích lắmmm」"
"1854" = "「Ưm──chụt──liếm──Reroooooo」"

# ふかみh1_ともはり練習.txt.toml
[script]
"993" = "「Hể!!?」"

# ふかみh3_夏休みの最後の日の、前の日.txt.toml
[script]
"2366" = "「A ư—— ưm—— phù—— ngón tay, cái đó——\\nFuyan! Bị, miết, hột le, thì」"
"2785" = "「Á, từ từ đã, không được đâu!」"

# れいなh1_おかあさんのレッスン.txt.toml
[script]
"1263" = "「Fuya……a……sướng……quá, ạ~――ưm.」"
"1525" = "「A……Fuya――không được……kh-không được.」"
"1531" = "「Fuya――a――a――a――」"

# れいなh2_おもらし防止大作戦.txt.toml
[script]
"1084" = "「Chụt! Chụt! Chụt! Chụt!\\nChụt! Chụt! Chụt! Reroooo!」"
"1114" = "「Vâng ạ——ưm——Rerooooooo——\\nƯm——Pua! Puha! Haa……Haa」"

# れいなh3_おもらし自由化大作戦.txt.toml
[script]
"1026" = "「Hể?」"
"1078" = "「Áa! Cái này——Reina——\\nXấu hổ——xấu hổ——quá——đi——Fua!」"

# れいなh4_ふたりっきりのハロウィン.txt.toml
[script]
"1897" = "「Hể? Reina,\\nđã hiểu lầm chuyện gì sao ạ~?」"

# グランドリライト03_日々姫.txt.toml
[script]
"1998" = "「Áa!? Anh vừa chụp em đấy à!!?」"

# ハチロクh1_契り.txt.toml
[script]
"1217" = "「Ya――A――Uốn lượn――như vậy――Ưm――\\nBụng――Bướm――A, liếm đi――Ưm, phù.」"
"1245" = "「Ahi――Ya――Aư……Bướm, bướm――\\nHa――A――Tan chảy, mất thôi――Ưm ư.」"

# ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml
[script]
"988" = "「Fuya!?」"
"1121" = "「N, ngài Soutetsu——fuya——cái này——\\ntuyệt quá——kư hi i i i ưm!」"

# ハチロクh7_レトロモダンメイクラヴ.txt.toml
[script]
"745" = "「Ka……ha……a——Gu——ưm——như——vậy,\\nđột, nhiên——đột——nhiên——Nkyuuu!!?」"
"843" = "「Nkyuuuuuuuuuuuuuuuuu!!」"
"1840" = "（Rerooooo——）"
"1878" = "（Liếm——liếm——Rerooooo——ngoạm!）"

# ハチロクh8_桜色のひめごと.txt.toml
[script]
"706" = "「Hyagyu!? Phù——Fua!? A——\\nnhũ hoa——Ư! Á, núm vú——kích thích, ưm, phù」"
"759" = "「A——ra rồi——ưm——nóng, quá——Nku——phù——\\nTinh trùng——của Ngài Soutetsu——nóng, quá——phù, fa」"
"821" = "「Ưm……Fua——a——Nku——tiểu, huyệt——\\nưm——hi——khục——bị chà xát——rồi——」"
"841" = "「Ưm mu! Ưm——mu!! Chóp chép! Chụt!\\n（Su——hi）Chụt! Rerooooooo!!」"
"1561" = "（Nku! Ực! Ực!! Ực!!）"

# ハチロクh9_コノフクハキルコト.txt.toml
[script]
"2033" = "「Fu……ưm————（Ực）\\nZu——churu——juuu——（Ực）」"
"2138" = "「Chumu! Ju! Jubo——ưm, Fu,\\nreru——ju! Jubo! Juruuu!」"
"2182" = "「Ưm mu!? Ưm——chubo——ju!\\nJubu! Jumu! Fu——chumu, ju!」"
"2187" = "「Ưm, Ku——」"
"2289" = "「Là khe hở——giữa hai chân——của em——ưm,\\nFu——a——Ku——haa——là cô bé, ạ」"
"2378" = "「Hahi——ưm, Ku——Fu, a——\\nVâng! Ngài Soutetsu!!!」"

# ポーレットh2_制服変更？.txt.toml
[script]
"929" = "「Hya——á!\\nNuu——phuê——Fuyaa.」"
"957" = "「Phuê... a... Fuyaaaaa.」"

# ポーレットh6_あなたとふたりの学園エッチ.txt.toml
[script]
"805" = "「Yafu——Fua!!? Ưm——Anh Soutetsu, Ku—— A! Bây giờ——mà cử động, thì——Nkyun!!」"
"851" = "「Ưm……Ku——」"

# ポーレットh8_気動車の国のアリス.txt.toml
[script]
"2080" = "「Cứ lên đỉnh——đi——Ku——tôi cũng——sắp rồi」"

# 凪h1_ふたりっきりのデート.txt.toml
[script]
"1053" = "「Fuya——A——Cái này——Cái này——Ưm——\\nMông——Ấm quá——Sướng——quá」"
"1057" = "「Fuya!」"
"1081" = "「Fuyau!」"
"1090" = "「Hể!?」"
"1772" = "（Trườn! Liếm! Reroooo!）"

# 凪h2_おとなの水着.txt.toml
[script]
"2252" = "「Ban đầu……Nagi, sama——Ưm——Ku——\\nSẽ, làm——theo ý thích——á——」"
"2489" = "「Ku——Phù——Ưm hứ——Ưmmm~!!」"
"2546" = "「Liếm——Liếm——Ngoáy——Nhóp nhép——\\nChụt——Chụt——Liếm——Rerooooo」"

# 凪ふかみh1_修学旅行の夜.txt.toml
[script]
"1232" = "「Ku——a」"
"1317" = "「Em hiểu rồi nha! Đến lúc quyết định rồi, tăng tốc thôi!\\nRerooooooooo!」"

# 凪ふかみh2_みずあそび.txt.toml
[script]
"1030" = "「...Liếm... liếm——phù——ưm——liếm——\\nliếm——liếm——liếm——Rerooooo」"

# 日々姫h2_洗って大丈夫なスーツ.txt.toml
[script]
"1081" = "「Fuyan!!」"

# 日々姫h3_汚れてしまった制服で.txt.toml
[script]
"1042" = "「Fuya!? Anh hai――đang liếm――ưm――\\nFua――a――liếm, liếm――nước tiểu――của em」"
"1857" = "（Reroooooo）"

# 日々姫h4_いもうとタオル.txt.toml
[script]
"964" = "「Iu!? ――Ka――Fuya――\\nAaaaaaaaaaaaaan!!!」"
"1028" = "「Ưm――Ku」"
"1075" = "「Sâu quá――Thế này――Na! Chỗ khác――bị ngoáy rồi!\\nHia――a――Bị khoét sâu――vào trong――Nkyu!!」"

# 日々姫h5_白濁絵の具の射精会.txt.toml
[script]
"1145" = "「Á――không được――phần đầu――chim, của anh――\\nRút ra, không được, đâu――cô đơn, lắm――đó!」"

# 真闇h1_長期熟成.txt.toml
[script]
"1021" = "「Fuya……ưm――sướng, quá――」"
"1059" = "「Ku――phư――」"
"1065" = "「Ưm――Ku――」"
"1080" = "「Ưm……Sou-chan――a――to quá――――Nfu.」"
"1214" = "「Bên trong……âm đạo, của chị Mayami……a――\\nuốn lượn――nếp gấp này, là sao――Ku.」"

# 真闇h2_無濾過.txt.toml
[script]
"1842" = "（Thắt lại――phập――kypu――Thắt lại）"

# 真闇h3_補習授業の廃校舎.txt.toml
[script]
"2212" = "「Há――a, á, aaa――ưm――chỗ đó,\\nbị, chạm, vào――Phư――a――rùng mình, mất.」"
"2215" = "「Há――ưm――Phư――á――chị, á,\\nfau――fua――chỗ đó――bị ép vào thì.」"
"2256" = "「A――Sou-chan……ưm――cái đó――\\nchị――thích lắm――ưm――Phư――a.」"
"2323" = "「Ưm……á……núm vú――ưm――bóp, bóp――\\nbị trêu chọc――dai dẳng, như thế――」"
"2328" = "「Ưm……há――ưm……tay của……Sou-chan……\\ndâm đãng quá……ưm――dính, nhớp nháp, quá.」"

# 稀咲h1_性生活.txt.toml
[script]
"988" = "「Cô nói là, DVD——ưm——Ku——\\ncô cũng xem…… những thứ——như vậy, sao?」"

## **Ghi chú điều phối (coordinator, 22/11 ~12:10 — 1 dòng ghép):** 759 trùng U11a (M16) ở token khác nhau — đã GHÉP theo quy tắc composition: old_vn := fix U11a, fix := giá trị kết hợp (fix M16 đổi "phù, fua"→"phù, fa" + đổi M15 "ưn ku"→"Nku"). Kiểm chứng 2 chiều (bằng fix U11a + đổi M15, và bằng fix đợt này + đổi M16) — trùng nhau tuyệt đối. JSON + bảng §3 + khối TOML (REVIEW + `u12a_tomlblock.txt`) đã sửa đồng bộ.

Kết bài

Đợt U12a sửa **99 dòng (M7 23 + M8 17 + M9 8 + M10 5 + M11 16 + M15 11 + M68 18 + M70 1)** trong 43 file: token くっ đối thoại H-scene thống nhất thành "Ku" (trừ 4 file quy ước giữ "Hự"); や/やっ phân theo token kề sau ("Á" trước lời nói/từ chối, "Ya" trong chuỗi rên — và chỉ còn 17 dòng "A" trần thật sự, không phải 64 như F1 ghi); ふっ thống nhất trong từng file (Mayami → "Phư", ハチロクh9/lr_ニイロクh/lr_真闇h1 → "Fu"); ふぇ/ふえ ngạc nhiên độc lập → "Hể?"; ふや H-scene → romaji "Fuya"; ん+phụ âm H-scene → romaji N…; れろ dài → romaji "Rero" với số o đếm theo JP (kể cả 2 dòng sweep-added 1640/1056); 真闇h2 1842 quyết theo hệ romaji của file. Lượt soát 2: 99/99 tái kiểm chứng, 0 loại, 0 sửa. Khối TOML 43 file / 99 key parse-verified. Còn nợ coordinator: quyết follow-up cho 59 dòng Hự đối thoại còn lại (F1), sweep M15 ~154 dòng (F2), ふかみh2 989 "Kh" vs M7 (F3), 2 dòng M68 sweep-added (F4), cờ M10 trong dòng M11 (F5), và ranh giới Ya-vs-Á (F6).
