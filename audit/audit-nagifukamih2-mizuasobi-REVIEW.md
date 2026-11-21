# Audit — 凪ふかみh2_みずあそび.txt.toml (07_Nagi_Fukami)

File: `07_Nagi_Fukami/凪ふかみh2_みずあそび.txt.toml` — H-scene ba người (Soutetsu + Nagi + Fukami, chơi đùa ở bãi sông).
Phương pháp: đọc từng dòng đối chiếu JP + TW (CSV3), kiểm tra sweep gasp, kiểm tra đại từ theo dòng kề, lượt soát 2 đọc lại toàn bộ fix.

## 1. Tổng kết
- Đọc: **350/350 dòng** (key 1008–2184; monologue 170, ふかみ 66, 凪 65, 双鉄H 49).
- Sai: **42 dòng (12,0%)**.
- Phân loại: mất âm (rên romaji) 34; gasp 5 (đều từ sweep); sai nghĩa 1; thẻ %69 + sai nghĩa 1; thuật ngữ 1.
- 0 lệch dòng / 0 chuỗi xoay (rotation) / 0 nhiễm chéo file khác / 0 dòng mồ côi / 0 dòng chưa dịch / 0 key trùng.
- TOML md5: `dc5ff6dcb84a35650fb89a8465df9fe0`. Không có file TOML trùng cho scene này trong 07_Nagi_Fukami (chỉ một file みずあそび; các file lr_ là scene khác).
- [selections] rỗng; [characters]/[character_subs] khớp JP, không có lỗi.

## 2. Cơ sở tổng (đã kiểm chứng lại ROUTE-AUDIT.md)
Cơ sở dùng cho snippet là **194 file / 9.069 dòng sai** (không phải 193/9.052 như brief ban đầu — trong lúc audit, Hibiki 04 đã được gộp thêm 17 dòng lúc ~02:20; đã kiểm tra đuôi ROUTE-AUDIT.md trước khi viết snippet). Sau file này: **195 file / 9.111 dòng sai**.

## 3. Kiểm tra sweep gasp
Đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`: file này có **10 mục** — 5 mục sửa được (1015 lost-gasp-whole; 1294, 1865, 1946, 2019 lost-gasp-trailing) đều nhận nguyên văn sau khi đối chiếu JP; 5 mục already-rendered (1291, 1319, 1330, 1373, 1382 — tiếng gasp đã có dạng thể hiện Á/Ư/Ưm) giữ nguyên, không sửa.

## 4. Đại từ (đã kiểm chứng theo dòng kề)
- Soutetsu "anh" với Nagi + Fukami: 1026 ("Thế nên anh."), 1450 ("Quãng đời còn lại của anh.") — đúng quy tắc đã chốt.
- Fukami tự xưng "em" với Soutetsu: 1316, 1446, 1514 — đúng (cô gọi Soutetsu là "anh Soutetsu").
- Fukami→Nagi "cậu": 1457 ("Không phải lúc nãy cậu nói…") — đúng quy tắc cùng tuổi (tớ–cậu), không "em". Nagi→Fukami "bé Nagi"/"bé": 1256, 1312, 1419, 1430 — đúng, không "chị".
- Không có dòng Soutetsu nào tự xưng sai trong file này; không sửa đại từ nào.

## 5. Danh sách sửa (42 dòng)
### 1015 [凪] — gasp
- JP: 「っ！」
- TW: 「……」
- Cũ: 「!」
- Sửa: 「Ư!」
- Lý do: Gasp toàn dòng っ+! — VN cũ chỉ còn dấu "!", mất hẳn tiếng gasp → thêm Ư. Sweep lost-gasp-whole, nhận nguyên văn.

### 1258 [ふかみ] — sai nghĩa
- JP: 「そんなのっ！」
- TW: 「別管啦！」
- Cũ: 「Chuyện đó thì!」
- Sửa: 「Đừng để ý chuyện đó!」
- Lý do: そんなのっ là câu phản đối ngượng ngùng khi Soutetsu bảo Nagi nhìn kỹ miệng Fukami; TW 別管啦 (đừng để ý). VN cũ "Chuyện đó thì!" mơ hồ, không ra ý phản đối.

### 1266 [ふかみ] — mất âm
- JP: 「ひっ――」
- TW: 「呀……」
- Cũ: 「Á——」
- Sửa: 「Hi——」
- Lý do: ひっ là tiếng hít vào sắc — "Á" làm mất phụ âm h. Tiền lệ moan đã gộp: ひっ→Hi/Hí.

### 1267 [凪] — mất âm
- JP: 「ひゃふっ――ふあっ――あっ――ひゃ――あっ」
- TW: 「呀……哇……啊……呀……啊」
- Cũ: 「Á phù——phù——a——á——a」
- Sửa: 「Hyafu——Fua——a——Hya——a」
- Lý do: ひゃふっ→Hyafu, ふあっ→Fua (romaji fallback), ひゃ→Hya — "Á/phù" làm mất phụ âm hy- và âm tiết あ. Quy tắc ひゃ-family 21/11.

### 1269 [凪] — mất âm
- JP: 「ひ――あっ――のーみそ――あつ、くてっ―― / あつ、くて――ふっ――ひっ――ぐるぐる――って」
- TW: 「呀……啊……腦漿……發燙……好燙……呼……呀……在打轉」
- Cũ: 「Á——a——não——nóng, quá—— / nóng, quá——phù——á——quay cuồng——mất」
- Sửa: 「Hi——a——não——nóng, quá—— / nóng, quá——phù——hi——quay cuồng——mất」
- Lý do: ひ――→Hi; ひっ→hi — "Á" làm mất phụ âm h.

### 1271 [ふかみ] — mất âm
- JP: 「いっ――んっ――ふうっ――あっ――こ、これ―― / 入り口の――とこ――は、あっ――熱――く、てっ」
- TW: 「呀……嗯……呼……啊……這、這個……入口處……呼……好燙」
- Cũ: 「Á——ưm——phù——a——c-cái này—— / ở chỗ——cửa vào——thì, a——nóng——lắm」
- Sửa: 「Í——ưm——phù——a——c-cái này—— / ở chỗ——cửa vào——thì, a——nóng——lắm」
- Lý do: いっ→Í — "Á" làm mất vần i. Tiền lệ Paulette h3: いっ→Í.

### 1272 [凪] — mất âm
- JP: 「ひゃっ」
- TW: 「呀」
- Cũ: 「Á」
- Sửa: 「Hya」
- Lý do: ひゃっ→Hya (quy tắc ひゃ-family 21/11: "Á" làm mất phụ âm hy-).

### 1273 [ふかみ] — mất âm
- JP: 「ひゃふっ！」
- TW: 「呀！」
- Cũ: 「Á phù!」
- Sửa: 「Hyafu!」
- Lý do: ひゃふっ→Hyafu (tiền lệ 凪ふかみh1 1214).

### 1274 [ふかみ] — mất âm
- JP: 「ひゅっ！　きゅうううううううううううううんっ！」
- TW: 「呀！嗯！」
- Cũ: 「Á! Ưmmmmmmmmmmmmmm!」
- Sửa: 「Hyu! Kyuuuuuuuuuuuuuun!」
- Lý do: ひゅっ→Hyu; きゅう…んっ→Ky+14u+n theo công thức đếm vần (1 vần trong きゅ + 13う; 1ん).

### 1276 [ふかみ] — mất âm
- JP: 「ふきゅっ！　それ、しゅごっ――んっ――は、あっ、 / こきざみ、され、て――子宮――これっ――しゅき――」
- TW: 「呀！好棒……嗯……呼，被一點點地擠進來……子宮……我喜歡……」
- Cũ: 「Á! Cái đó, tuyệt quá——ưm——hà, a, / bị, nhấp nhấp——tử cung——cái này——thích quá——」
- Sửa: 「Fukyu! Cái đó, tuyệt quá——ưm——hà, a, / bị, nhấp nhấp——tử cung——cái này——thích quá——」
- Lý do: ふきゅっ→Fukyu (romaji; tiền lệ 3 file moan đã gộp: Hachiroku h6 824, h7 750, Fukami h3 2287). Xem Cờ cho Hieu.

### 1277 [凪] — mất âm
- JP: 「ひきゅううううううううんんっ！！！」
- TW: 「呀！！！」
- Cũ: 「Á ưmmmmmmmm!!」
- Sửa: 「Hikyuuuuuuuuunn!!!」
- Lý do: ひきゅう…んんっ→Hi+ky+9u+nn (công thức đếm vần: 1 vần trong きゅ + 8う; 2ん).

### 1278 [凪] — mất âm
- JP: 「ひゃぴっ！？」
- TW: 「呀！？」
- Cũ: 「Á!?」
- Sửa: 「Hyapi!?」
- Lý do: ひゃぴっ→Hyapi (tiền lệ 凪ふかみh1 1226: ひゃぷっ→Hyapu).

### 1279 [凪] — mất âm
- JP: 「いひゅっ！？　んっ――ひ――あっ――に――にーさ / ……んぎゅっ――まっ――まっ……ひぇっ――んうっ！」
- TW: 「呀！？哼……呀……啊……大……大哥哥……嗯……等……等……呀……嗯！」
- Cũ: 「Á!? Ưm——á——a——anh——anh hai / ...ưm——đợi——đợi... á——ưm!」
- Sửa: 「Ihyu!? Ưm——hi——a——anh——anh hai / ...Ngyu——đợi——đợi... Hye——ưm!」
- Lý do: いひゅっ→Ihyu; ひ→hi; んぎゅっ→Ngyu (tiền lệ Paulette h2 928); ひぇっ→Hye.

### 1280 [凪] — mất âm
- JP: 「ひゃっ！？　あっ――にーさんの、指……あっ、 / お尻の――なか、で――まわってる――ばいっ」
- TW: 「呀！？啊……大哥哥的手指……啊，在……屁眼裡面……打轉」
- Cũ: 「Á!? A——ngón tay, của anh hai... a, / đang——xoay tròn——bên trong... hậu môn——nha」
- Sửa: 「Hya!? A——ngón tay, của anh hai... a, / đang——xoay tròn——bên trong... hậu môn——nha」
- Lý do: ひゃっ→Hya.

### 1283 [ふかみ] — mất âm
- JP: 「ひっ！？　あっ――深い、のッ――ごつん、てっ―― / これっ――しゅごっ――あたまっ――チカ、チカっ」
- TW: 「呀！？啊……好深……在抖……這……好棒……腦袋發暈」
- Cũ: 「Á!? A——sâu, quá——cộc cộc—— / cái này——tuyệt quá——đầu óc——quay, cuồng」
- Sửa: 「Hí!? A——sâu, quá——cộc cộc—— / cái này——tuyệt quá——đầu óc——quay, cuồng」
- Lý do: ひっ→Hí (dạng đầu dòng có !?; tiền lệ Hachiroku h5 1020: ひっ→hí).

### 1284 [凪] — mất âm
- JP: 「ひえっ！？　にーさんっ！ / まだ、おちんちんばピュッピュして――ふあんっ！！」
- TW: 「呀！？大哥哥！雞巴又在冒水……哇！！」
- Cũ: 「Á!? Anh hai! / Chim vẫn đang xịt nước ra kìa——phù!!」
- Sửa: 「Hả!? Anh hai! / Chim vẫn đang xịt nước ra kìa——Fuan!!」
- Lý do: ひえっ→Hả (tiếng giật mình; tiền lệ Paulette h4 859 giữ "Hả!?" cho ひえっ); ふあんっ→Fuan (tiền lệ lr-Fukami h2 1268: ふああああああんっ→Fuaaaaaan).

### 1287 [ふかみ] — mất âm
- JP: 「ひっ、ぎゅっ！？　いきな、りっ」
- TW: 「呀，嗯！？怎麼突然」
- Cũ: 「Á, ư!? Đột, nhiên」
- Sửa: 「Hi, Gyu!? Đột, nhiên」
- Lý do: ひっ→Hi; ぎゅっ→Gyu (tiền lệ lr-Nagi h1 1221: ぎゅっ→Gyu).

### 1294 [ふかみ] — gasp
- JP: 「はぁ……はぁ……はぁっ――は――ああ～っ」
- TW: 「呼……呼……呼……呼……啊」
- Cũ: 「Hà... hà... hà——hà——a~」
- Sửa: 「Hà... hà... hà——hà——a~Ư」
- Lý do: っ cuối tuyệt đối sau ああ～ → thêm Ư. Sweep lost-gasp-trailing, nhận nguyên văn.

### 1295 [ふかみ] — mất âm
- JP: 「は……ぁっ……ふあっ――ん――それ――に…… / 重くて……ねばっこくって……くさ、く、て――」
- TW: 「呼……啊……呼……嗯……而且……好重……黏糊糊的……味道好大……」
- Cũ: 「Hà... a... phù——ưm——hơn nữa——... / nặng quá... nhầy nhụa quá... lại còn nặng, mùi, nữa——」
- Sửa: 「Hà... a... Fua——ưm——hơn nữa——... / nặng quá... nhầy nhụa quá... lại còn nặng, mùi, nữa——」
- Lý do: ふあっ→Fua — "phù" sai vần: ふあ là Fua/phùa, không phải "phù".

### 1297 [凪] — mất âm
- JP: 「んふっ――んんっ――えうううっ――べろおっ」
- TW: 「呼……嗯……嗚……啾」
- Cũ: 「Ưm phù——ưm——ư——liếm」
- Sửa: 「Ưm phù——ưm——Euuu——liếm」
- Lý do: えうううっ→Euuu — công thức đếm vần: え+3う = 4 vần; "ư" làm mất vần え và độ dài.

### 1299 [ふかみ] — mất âm
- JP: 「ひゃふぁ……んにゅ……にゃに、ひゃん―― / ん……にゅゅーっへ……ちゅ……ははほ？」
- TW: 「呼……嗯……小凪……跟我……一起玩吧」
- Cũ: 「Hà... ưm... Nagi, này—— / ưm... chụt... nhỉ?」
- Sửa: 「Hyafa... ưm... Nagi, này——Hyan—— / ưm... chụt... nhỉ?」
- Lý do: ひゃふぁ→Hyafa; ひゃん→Hyan — ひゃん bị bỏ hẳn trong VN cũ. (にゅゅーっへ là tiếng líu nhí không rõ nghĩa, giữ "ưm" — xem §6.)

### 1303 [凪] — mất âm
- JP: 「ふぎゅっ！」
- TW: 「呼！」
- Cũ: 「Phù!」
- Sửa: 「Fugyu!」
- Lý do: ふぎゅっ→Fugyu (ふ+ぎゅ; tương tự ぎゅっ→Gyu).

### 1310 [凪] — mất âm
- JP: 「ふあっ――出たばいっ！　にーさん――せーえきっ！ / びゅっびゅって！　すごく！　すっごく熱いかとばい！」
- TW: 「哇……射了！　大哥哥的……精液！呲呲的！　好多！　好燙！」
- Cũ: 「Oa——ra rồi nha! Anh hai——tinh dịch! / Bắn phụt phụt kìa! Nhiều quá! Nóng lắm luôn á nha!」
- Sửa: 「Fua——ra rồi nha! Anh hai——tinh dịch! / Bắn phụt phụt kìa! Nhiều quá! Nóng lắm luôn á nha!」
- Lý do: ふあっ→Fua — "Oa" là cách đọc của わ, không phải ふあ.

### 1314 [凪] — mất âm
- JP: 「ふあ……ふかみちゃん……すごか……すごかよ」
- TW: 「哇……小深……厲害，厲害啊」
- Cũ: 「Oa... Fukami... giỏi quá... giỏi quá nha」
- Sửa: 「Fua... Fukami... giỏi quá... giỏi quá nha」
- Lý do: ふあ→Fua (như trên).

### 1322 [凪] — mất âm
- JP: 「ふあっ？！　お尻いきなりばいっ！？」
- TW: 「哇？！怎麼突然對我屁股……」
- Cũ: 「Oa?! Sao tự nhiên lại nhắm vào hậu môn nha!?」
- Sửa: 「Fua?! Sao tự nhiên lại nhắm vào hậu môn nha!?」
- Lý do: ふあっ→Fua (như trên).

### 1328 [ふかみ] — mất âm
- JP: 「んっ――ふっ――んちゅっ――ちゅうっ――ふっ―― / ん、ふっ――ほーへふっ――ふぁ、んっ――」
- TW: 「哼……呼……啾……啾……呼……嗯，呼……是的……哈，哼……」
- Cũ: 「Ưm——phù——chụt——chu——phù—— / ưm, phù——phù——phù, ưm——」
- Sửa: 「Ưm——phù——chụt——chu——phù—— / ưm, phù——phù——Fa, ưm——」
- Lý do: ふぁ→Fa — "phù" sai vần (tiền lệ Reina h4 1983: ふぁ→Fa).

### 1335 [ふかみ] — mất âm
- JP: 「はっ――ひっ――あ、赤ちゃん――の――部屋っ―― / んっ――熱い、のっ――ぐり、って――んんうっ」
- TW: 「啊……呀……嬰、嬰兒……的……房間……哼……好燙……進來了……嗯嗯」
- Cũ: 「Hà——á——ph-phòng của em bé—— / ưm——nóng, quá——ngoáy, ngoáy——ưm ưm」
- Sửa: 「Hà——hi——ph-phòng của em bé—— / ưm——nóng, quá——ngoáy, ngoáy——ưm ưm」
- Lý do: ひっ→hi.

### 1344 [ふかみ] — mất âm
- JP: 「あんっ」
- TW: 「啊」
- Cũ: 「A」
- Sửa: 「An」
- Lý do: あんっ→An — "A" làm mất âm cuối n. Tiền lệ nhiều file moan đã gộp: あんっ→An.

### 1346 [ふかみ] — mất âm
- JP: 「えむっ――れるっ――るっ――れりゅうっ」
- TW: 「啊嗚……啾……啾……啾」
- Cũ: 「Ưm——liếm——liếm——liếm」
- Sửa: 「Emu——liếm——liếm——liếm」
- Lý do: えむっ→Emu — "Ưm" làm mất vần え; tương tự えうっ→Eu (tiền lệ lr-NagiFukami h1 1695).

### 1353 [ふかみ] — mất âm
- JP: 「あ！　ずるいっ、凪ちゃ――ふあっ！？」
- TW: 「啊！真奸詐，小凪……哇！？」
- Cũ: 「A! Ăn gian nha, bé Nagi——á!?」
- Sửa: 「A! Ăn gian nha, bé Nagi——Fua!?」
- Lý do: ふあっ→Fua.

### 1367 [凪] — mất âm
- JP: 「ん……ひ……なんか、にーさん――ふゅっ―― / へ、ヘンタイっぽい……ばいっ――」
- TW: 「嗯……呀……感覺，大哥哥……呼……好、好像個變態……」
- Cũ: 「Ưm... hì... sao tự dưng, anh hai——phù—— / gi-giống biến thái thế... nha——」
- Sửa: 「Ưm... hì... sao tự dưng, anh hai——Fyu—— / gi-giống biến thái thế... nha——」
- Lý do: ふゅっ→Fyu — tiền lệ Reina h3 1018: ふゅあ…→Fyua….

### 1372 [凪] — mất âm
- JP: 「ん……ふ……んっ――ふにゅっ……ふはふ…… / はへへふふぇ……ふっ――ほほはひは……ふぁい」
- TW: 「嗯……嗯……呼……呼……呼……呼……呼……呼」
- Cũ: 「Ưm... phù... ưm——mềm... phù... phù... / hà... hê hê... phù——... phù」
- Sửa: 「Ưm... phù... ưm——mềm... phù... phù... / hà... hê hê... phù——... Fai」
- Lý do: ふぁい→Fai — miệng đầy nên はい méo thành "fai"; tiền lệ Reina h4 1983: ふぁ→Fa.

### 1374 [ふかみ] — mất âm
- JP: 「えうっ――んっ――ちゅ……ちゅずっ――じゅるっ―― / んう……れろ――れるっ――ちゅうっ――ずじゅっ」
- TW: 「嗯……嗯……啾……啾……啾……嗯……啾……啾……啾……啾」
- Cũ: 「Ư——ưm——chụt... chụt——rột—— / ưm... liếm——liếm——chu——chụt」
- Sửa: 「Eu——ưm——chụt... chụt——rột—— / ưm... liếm——liếm——chu——chụt」
- Lý do: えうっ→Eu — tiền lệ lr-NagiFukami h1 1695: えうっ→Eu!.

### 1378 [凪] — mất âm
- JP: 「んひゅっ」
- TW: 「嗯」
- Cũ: 「Ưm」
- Sửa: 「Nhyu」
- Lý do: んひゅっ→Nhyu — quy tắc ひゃ-family; tiền lệ 凪ふかみh1 1304: んひゅっ→Nhyu!.

### 1405 [凪] — mất âm
- JP: 「にーさんのせーえき……ん……ぷぁ――苦か、けん…… / ふかみちゃんの、指……よけいに……ちゅっ――甘か」
- TW: 「大哥哥的精液……嗯……呼……好苦……小深的手指……特別……啾……甜」
- Cũ: 「Tinh dịch của anh hai... ưm... phù——đắng, quá... / ngón tay của Fukami... lại càng... chụt——ngọt ngào hơn」
- Sửa: 「Tinh dịch của anh hai... ưm... Pua——đắng, quá... / ngón tay của Fukami... lại càng... chụt——ngọt ngào hơn」
- Lý do: ぷぁ→Pua — tiền lệ Hachiroku h6 829/915: ぷぁ→Pua.

### 1428 [ふかみ] — mất âm
- JP: 「凪ちゃんの指――んっ――おいひい――ひょぉ……ん、 / ちゅっ――ちゅう――れろっ――れるうっ」
- TW: 「小凪的手指……嗯……真好吃……嗯，啾……啾……啾……啾」
- Cũ: 「Ngón tay của bé Nagi——ưm——ngon quá——ư... ưm, / chụt——chu——liếm——liếm」
- Sửa: 「Ngón tay của bé Nagi——ưm——ngon quá——Hyo... ưm, / chụt——chu——liếm——liếm」
- Lý do: ひょぉ→Hyo — họ ひゃ; tiền lệ Reina h2 1298: ひゅひょ→hyuhyo.

### 1528 [ふかみ] — thẻ %69 + sai nghĩa
- JP: %69;『「わかってるばーい。にーさん、いよいよお尻の穴ば試したかとよね？」 / 「わかってます。です。ここなら、おしっこ――しても汚れない場所。です、から」』
- TW: 『「咱們都明白。大哥哥，你想試試屁眼了吧？」 / 「我懂。在這就算漏尿也不髒。來吧」』
- Cũ: 『「Bọn em biết tòng tọc rồi nha. Anh hai, cuối cùng cũng muốn thử lỗ hậu môn rồi đúng không?」 / 「Bọn em biết. Mà. Ở đây thì, có đi tiểu——cũng không làm bẩn chỗ nào. Đâu, ạ.」』
- Sửa: %69;『「Bọn em biết tỏng rồi nha. Anh hai, cuối cùng cũng muốn thử lỗ hậu môn rồi đúng không?」 / 「Bọn em biết. Mà. Ở đây thì, có đi tiểu——cũng không làm bẩn chỗ nào. Đâu, ạ.」』
- Lý do: Khôi phục thẻ %69; đầu dòng — toàn dự án chỉ có 2 dòng %NN; (ポーレット01 1450 giữ %61; trong VN). "tòng tọc" không phải tiếng Việt → "biết tỏng" (わかってる = biết rõ).

### 1530 [ふかみ] — mất âm
- JP: 『「ふあっ」 / 「んっ」』
- TW: 『「哇」 / 「哼」』
- Cũ: 『「Phù」 / 「Ưm」』
- Sửa: 『「Fua」 / 「Ưm」』
- Lý do: ふあっ→Fua.

### 1852 [monologue] — thuật ngữ
- JP: 水棹を引き上げ、 / あとはすべてを流れに任せ――
- TW: 我拉起棹，準備讓船自由漂流……
- Cũ: Nhấc mái chèo lên, / phần còn lại phó mặc tất cả cho dòng nước——
- Sửa: Nhấc cây sào chống lên, / phần còn lại phó mặc tất cả cho dòng nước——
- Lý do: 水棹→"cây sào chống" — toàn dự án 7 dòng đều "sào chống/sào chống thuyền" (共通10, ポーレット08, 凪ふかみ01); "mái chèo" là 櫓/櫂, xem 凪ふかみ01 1676 đối chiếu ba loại.

### 1865 [monologue] — gasp
- JP: お互いに夢中なふたりの背後に回りこみ、 / 不意打ち愛撫でおしおきを――っ！？
- TW: 我繞到正沉浸在互舔的世界裡的她們背後，打算來個出其不意的愛撫……嗯！？
- Cũ: Tôi vòng ra phía sau hai cô gái đang say sưa với nhau, / định tung một đòn vuốt ve bất ngờ để trừng phạt——!?
- Sửa: Tôi vòng ra phía sau hai cô gái đang say sưa với nhau, / định tung một đòn vuốt ve bất ngờ để trừng phạt——Ư!?
- Lý do: っ cuối tuyệt đối sau —— → thêm Ư. Sweep lost-gasp-trailing, nhận nguyên văn.

### 1946 [monologue] — gasp
- JP: ふかみの、焦ったような声――っ！？
- TW: 深美的聲音似乎有些急不可耐……嗯！？
- Cũ: Giọng nói có vẻ luống cuống của Fukami——!?
- Sửa: Giọng nói có vẻ luống cuống của Fukami——Ư!?
- Lý do: Như trên. Sweep lost-gasp-trailing, nhận nguyên văn.

### 2019 [monologue] — gasp
- JP: 声と同時に、 / 凪は両手を川面に差し込み――っ！！？
- TW: 說著，凪就將雙手插入了河面……嗯！！？
- Cũ: Cùng lúc với tiếng reo hò, / Nagi thọc cả hai tay xuống mặt sông——!!?
- Sửa: Cùng lúc với tiếng reo hò, / Nagi thọc cả hai tay xuống mặt sông——Ư!!?
- Lý do: Như trên. Sweep lost-gasp-trailing, nhận nguyên văn.

## 6. Giữ nguyên có lý do (không sửa)
- 1027 ふかみっ――凪っ: っ gắn tên riêng (từ nội dung) không phải gasp → không thêm Ư (ranh giới gasp đã chốt).
- 1291, 1319, 1330, 1373, 1382: sweep already-rendered — gasp đã thể hiện (Ư/Á/Ưm) → giữ.
- 1323 いやぁんっ→"Ối!!": TW 哎呀 cũng là thán từ → giữ.
- 1324 ふえっ→"Hả!?": TW 哎 → giữ (tiếng giật mình, không phải rên).
- 1337 あちゅっ→"nóng quá": diễn ý "nóng" (あつ) → giữ.
- 1370 ふにゅっ→"mềm": diễn nghĩa (mềm/xẹp) → giữ; 1298 んうっ→"ưm" → giữ.
- 1381 んぐっ→"Ưm": tiền lệ 凪h2 2428 giữ "Ư" cho んぐっ → giữ.
- 1403 ふぇ→"he": TW 哎 → giữ.
- 1288/1290 ぬっ/うぐっ→"Hự": tiếng gằn của Soutetsu → giữ.
- 1293 あのっ→"cái đó——": っ ngắt câu đã thể hiện bằng dấu —— → giữ.
- 1030/1328 ほーへふっ→"phù": TW cũng diễn thành hơi thở → giữ.
- 1372 ほほはひは→"phù": TW cũng diễn thành hơi thở → giữ (chỉ sửa ふぁい cuối dòng).
- 1299 にゅゅーっへ: tiếng líu nhí miệng đầy, không có nghĩa rõ → giữ "ưm" (chỉ sửa 2 âm họ ひゃ).
- 1245 ともはり→"người lái đò"; 1432 大陰唇→"đại âm môi"; 1503 [もんじゅ,1] đã strip theo quy tắc [ruby] — đều giữ.
- 1667 "còn hơn cả ngàn lời nói": thành ngữ tiếng Việt cho 言葉以上 → giữ.
- 1832 ほっぺた→"gò má": JP thắng TW (TW ghi nhầm "bụng") → giữ.
- 2060 độc thoại "tôi": không phải tự vấn cảm xúc nội tâm → quy tắc chung "tôi" → giữ.
- 1858 押し込みっ: っ đã thể hiện bằng —— → giữ.
- 1271 ふうっ→"phù": giữ theo quy ước chung của file (ふっ→"phù" nhất quán); không phân biệt độ dài ふ/ふう ở đây.

## 7. Kiểm tra cấu trúc
- CSV3: 350 dòng, 1 set duy nhất, tập key trùng khớp TOML 350/350; JP trong comment TOML khớp CSV3 JP 350/350.
- VN TOML vs CSV3: 166 dòng khác nhau, TẤT CẢ đều do TOML-2 làm phẳng `\n` thành khoảng trắng (đã biết); CSV3 là chuẩn, fix lấy theo CSV3.
- [script] có 350 câu lệnh gán key, 350 key riêng biệt, không trùng. Không có VN trống, không có JP trống.
- JSON: 42 mục, key dạng chuỗi, list-of-dicts (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 42/42 (kiểm tra cơ học).
- Khối TOML: 42 khóa, parse bằng tomllib OK, 0 sai lệch giá trị so với JSON. Mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm tra diff cơ học 42/42).

## 8. Lượt soát 2 (bắt buộc)
- Đã đọc lại toàn bộ 42 fix đối chiếu từng JP: **42/42 tái kiểm chứng, 0 bỏ, 0 sửa**.
- Đếm vần đã kiểm tra lại: 1274 Ky+14u+n (1+13う), 1277 Hi+ky+9u+nn (1+8う, 2ん), 1297 Euuu (え+3う).

## 9. Cờ cho Hieu
- 1276 ふきゅっ→"Fukyu": cùng câu hỏi đang chờ Hieu từ file Niiroku 03 (dạng romaji "Fukyu" vs "Phù kiu"); file này đã dùng "Fukyu" theo tiền lệ 3 file moan đã gộp — nếu Hieu chọn "Phù kiu" thì đợt thống nhất sẽ sửa lại.
- 1299: dòng baby-talk líu nhí (にゅゅーっへ) không dịch sát được, đã giữ "ưm" — ghi nhận, không quyết thêm.
- B19 vẫn park (không có dòng nào trong file này cần check trong game).

## 10. Khối TOML (đã kiểm chứng parse)
```toml
"1015" = "「Ư!」"
"1258" = "「Đừng để ý chuyện đó!」"
"1266" = "「Hi——」"
"1267" = "「Hyafu——Fua——a——Hya——a」"
"1269" = "「Hi——a——não——nóng, quá——\\nnóng, quá——phù——hi——quay cuồng——mất」"
"1271" = "「Í——ưm——phù——a——c-cái này——\\nở chỗ——cửa vào——thì, a——nóng——lắm」"
"1272" = "「Hya」"
"1273" = "「Hyafu!」"
"1274" = "「Hyu! Kyuuuuuuuuuuuuuun!」"
"1276" = "「Fukyu! Cái đó, tuyệt quá——ưm——hà, a,\\nbị, nhấp nhấp——tử cung——cái này——thích quá——」"
"1277" = "「Hikyuuuuuuuuunn!!!」"
"1278" = "「Hyapi!?」"
"1279" = "「Ihyu!? Ưm——hi——a——anh——anh hai\\n...Ngyu——đợi——đợi... Hye——ưm!」"
"1280" = "「Hya!? A——ngón tay, của anh hai... a,\\nđang——xoay tròn——bên trong... hậu môn——nha」"
"1283" = "「Hí!? A——sâu, quá——cộc cộc——\\ncái này——tuyệt quá——đầu óc——quay, cuồng」"
"1284" = "「Hả!? Anh hai!\\nChim vẫn đang xịt nước ra kìa——Fuan!!」"
"1287" = "「Hi, Gyu!? Đột, nhiên」"
"1294" = "「Hà... hà... hà——hà——a~Ư」"
"1295" = "「Hà... a... Fua——ưm——hơn nữa——...\\nnặng quá... nhầy nhụa quá... lại còn nặng, mùi, nữa——」"
"1297" = "「Ưm phù——ưm——Euuu——liếm」"
"1299" = "「Hyafa... ưm... Nagi, này——Hyan——\\nưm... chụt... nhỉ?」"
"1303" = "「Fugyu!」"
"1310" = "「Fua——ra rồi nha! Anh hai——tinh dịch!\\nBắn phụt phụt kìa! Nhiều quá! Nóng lắm luôn á nha!」"
"1314" = "「Fua... Fukami... giỏi quá... giỏi quá nha」"
"1322" = "「Fua?! Sao tự nhiên lại nhắm vào hậu môn nha!?」"
"1328" = "「Ưm——phù——chụt——chu——phù——\\nưm, phù——phù——Fa, ưm——」"
"1335" = "「Hà——hi——ph-phòng của em bé——\\nưm——nóng, quá——ngoáy, ngoáy——ưm ưm」"
"1344" = "「An」"
"1346" = "「Emu——liếm——liếm——liếm」"
"1353" = "「A! Ăn gian nha, bé Nagi——Fua!?」"
"1367" = "「Ưm... hì... sao tự dưng, anh hai——Fyu——\\ngi-giống biến thái thế... nha——」"
"1372" = "「Ưm... phù... ưm——mềm... phù... phù...\\nhà... hê hê... phù——... Fai」"
"1374" = "「Eu——ưm——chụt... chụt——rột——\\nưm... liếm——liếm——chu——chụt」"
"1378" = "「Nhyu」"
"1405" = "「Tinh dịch của anh hai... ưm... Pua——đắng, quá...\\nngón tay của Fukami... lại càng... chụt——ngọt ngào hơn」"
"1428" = "「Ngón tay của bé Nagi——ưm——ngon quá——Hyo... ưm,\\nchụt——chu——liếm——liếm」"
"1528" = "%69;『「Bọn em biết tỏng rồi nha. Anh hai, cuối cùng cũng muốn thử lỗ hậu môn rồi đúng không?」\\n「Bọn em biết. Mà. Ở đây thì, có đi tiểu——cũng không làm bẩn chỗ nào. Đâu, ạ.」』"
"1530" = "『「Fua」\\n「Ưm」』"
"1852" = "Nhấc cây sào chống lên,\\nphần còn lại phó mặc tất cả cho dòng nước——"
"1865" = "Tôi vòng ra phía sau hai cô gái đang say sưa với nhau,\\nđịnh tung một đòn vuốt ve bất ngờ để trừng phạt——Ư!?"
"1946" = "Giọng nói có vẻ luống cuống của Fukami——Ư!?"
"2019" = "Cùng lúc với tiếng reo hò,\\nNagi thọc cả hai tay xuống mặt sông——Ư!!?"
```

## Kết bài
Đã audit xong 凪ふかみh2_みずあそび.txt.toml: 350 dòng đọc, 42 dòng sai (12,0%) — chủ yếu là rên họ ひゃ/ふあ bị dịch mất âm (34 dòng), cộng 5 gasp từ sweep, 1 sai nghĩa, 1 thẻ %69 bị rơi, 1 thuật ngữ 水棹. Không có lệch dòng, xoay dòng, nhiễm chéo hay dòng mồ côi. Đại từ Soutetsu/Fukami/Nagi trong file đều đúng quy tắc đã chốt, không cần sửa. Lượt soát 2: 42/42 tái kiểm chứng, 0 bỏ, 0 sửa. Khối TOML 42 khóa parse OK, 0 sai lệch. Cơ sở tổng đã rebase theo ROUTE-AUDIT.md hiện tại (194 file / 9.069 dòng sai); sau file này: 195 file / 9.111 dòng sai.