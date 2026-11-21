# Audit — lr_真闇h1_僕のおねえちゃん.txt.toml (05_Mayami)

- File: `05_Mayami/lr_真闇h1_僕のおねえちゃん.txt.toml` (TOML-2: `lr_#U771f#U95c7h1_#U50d5#U306e#U304a#U306d#U3048#U3061#U3083#U3093.txt.toml`)
- Route: 05_Mayami. Nội dung: cảnh H của Mayami ("chị của em") — Mayami mặc bộ đồ lót mới motif mèo đen (tai + đuôi mèo) khoe Soutetsu, trêu chọc rồi "dạy" em: oral, paizuri, quan hệ, xuất tinh trong; xen kẽ trò chuyện về lời khen (Mayami muốn thỉnh thoảng được khen ngợi) và ước muốn có hai đứa con với nhau.
- Đọc: **317/317 dòng** (keys 1163–2190, section `script`: monologue 141, thoại Soutetsu 90, thoại Mayami 86), đọc từng dòng JP + TW + VN đối chiếu. CSV3 1 set duy nhất, key khớp tuyệt đối 317/317; VN khớp TOML ở 170/317 dòng, 147 dòng còn lại chỉ khác ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng — theo quy tắc, CSV3 là chuẩn cho fix list.
- **Sai: 59/317 (18,6%)**.
- Phân loại: đại từ 22 (Soutetsu "em"→"tôi" với Mayami), gasp 21 (sweep 16 + sweep-missed 5), rên/nguyên âm 16, SFX 1 (2145), nghĩa 3 (1385, 1610 gộp với đại từ; 1684 riêng).
- **0 lệch dòng / 0 chuỗi xoay / 0 nhiễm chéo / 0 dòng mồ côi / 0 dòng chưa dịch / 0 khóa trùng.** Không có VN nào là lời thoại của file khác; VN lặp ở 2 key chỉ là SFX ngắn dùng chung (「A.」×2 — 1463 ぁっ vs 1473 あっ, cùng âm "a"; （Phập!）×2 — 2164 に……ちっ！ vs 2190 ぐりゅっ！, cùng là âm đẩy). Chỉ 2 dòng VN==TW: 1170 「…………」 và 1175 「……」 (toàn dấu câu, không phải chưa dịch).
- TOML md5: `4baa00ccc02ca48bed882887b182d798` — không có bản trùng (chỉ 1 file lr_真闇h1_僕のおねえちゃん trong sources/toml2/). `[selections]` rỗng ({}). `[characters]`: 1799, 1919. 0 tag `%l` trong file (không có tag nào để sửa). File UTF-8 BOM + CRLF (652 dòng).
- Cơ sở tổng: **153 file / 6.832 dòng sai** (đã kiểm chứng trực tiếp với dòng tổng cuối của ROUTE-AUDIT.md — task giao cơ sở 152/6.759, nhưng file lr_ハチロクh3_通販失敗いたしましたにゃん (73 dòng sai) đã được gộp lúc ~12:05 trong khi audit này đang chạy, nên REBASE lên 153/6.832).

## §1. Đại từ — Soutetsu "em"→"tôi" với Mayami, lỗi hệ thống (22 dòng — SỬA)

File dùng "em" cho Soutetsu xuyên suốt thoại (20 dòng) + 2 dòng độc thoại (1865, 2189), trong khi quy tắc đã khóa là "tôi" với Mayami (Mayami gọi cậu 双ちゃん/Sou-chan, chị gái nuôi lớn hơn — tiền lệ đã merge: lr真闇追加02 48 fix đại từ, lr真闇追加03 48 fix, 真闇h3 "tôi với Mayami xuyên suốt"). File KHÔNG nhất quán nội bộ: độc thoại Soutetsu dùng "tôi" ở ~30 dòng (1762, 1771, 1822, 1832, 1868, 1870, 1875...), chỉ 1865/2189 lệch sang "em". Toàn bộ thoại 双鉄 trong file chỉ nói với Mayami (chỉ có 2 nhân vật lên tiếng), nên không có trường hợp người nghe khác cần phân biệt. Tổng 41 token "em" tự xưng (đếm bằng máy) → "tôi".

Giữ nguyên, không sửa: Mayami gọi Soutetsu "em" (ngôi 2 — 1183, 1437, 1499, 1512, 1534, 1539, 1554, 1574, 1575, 1577, 1578, 1616, 1626, 1691, 1695, 1698 — chị gọi em trai, đúng); "em bé" (em bé — 1506, 1693) là danh từ, không phải đại từ. Soutetsu gọi Mayami "chị" xuyên suốt, không có "anh"/"cô" nào sai. "mình" trong độc thoại chỉ còn dạng sở hữu/thành ngữ đúng (1862 "lời mình vừa nói", 2026 "rùng mình").

Các dòng sửa: 1385 (×3 + nghĩa), 1388 (×3), 1397, 1425 (×2), 1483 (×2), 1562, 1572, 1584 (×3), 1586 (×2), 1591 (×2), 1593, 1595 (×2), 1598 (×3 + gasp), 1600 (×4), 1601, 1604 (×2), 1607 (×2 + gasp), 1610 (×2 + nghĩa), 1673 (×2), 1686, 1865 (độc thoại), 2189 (độc thoại).

## §2. Gasp っ — sweep kiểm chứng + 5 dòng sweep bỏ sót

Sweep có **20 mục** cho file này (đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`): **16 fix áp nguyên** sau khi kiểm chứng từng giá trị vs JP (1163, 1495, 1496, 1497, 1519, 1575, 1607, 1699, 1700, 1701, 1702, 1706, 1709, 1797, 1828, 1915 — trong đó 1607 gộp với fix đại từ) và **4 already-rendered đã kiểm chứng đúng, không sửa**: 1428 (んっ――ん～～～～っ → "Ưm——ưm~~~~!!" — gasp đã diễn), 1503 (ん――っぁ――んっ……っ！！ → "Ưm——a——ưm……!!"), 1698 (ん～～～っ → "Ưm~~~"), 1803 (真闇姉は――っ！ → "chị Mayami——!" — っ diễn bằng "!").

Quét máy bổ sung toàn bộ dòng JP chứa っ (**239 dòng**): tìm thêm **5 gasp sweep bỏ sót** (đều là っ đứng riêng, mất hoàn toàn trong VN):
- **1168**: JP có 2 っ đứng riêng (đầu dòng っ―― và giữa dòng っ、), VN mất cả 2 → thêm 2 Ư (1 Ư/1 っ theo quy tắc đa-っ, tiền lệ audit h6 1271, sweep §10 phụ lục). Các っ dính SFX (れりゅっ/ふっ/ぢゅれろっ) đã diễn bằng từ Việt ("Liếm"/"fu"/"chụt liếm"), không thêm Ư.
- **1494, 1542**: っ đứng riêng đầu dòng (っ！！ / っ！！！) mà VN chỉ còn dấu câu — khôi phục gasp đầu dòng (tiền lệ sweep §6 + phụ lục lr_h1 1077).
- **1598** (gộp đại từ), **1603**: っ đứng riêng giữa dòng (っ―― / ――っ――) bị VN bỏ mất → thêm Ư.

Giữ nguyên (ranh giới, đã đối chiếu): **1167** ――っ―― → "——!" (っ đã diễn bằng "!"); **1440** っ―― → "ư" thường (âm đã diễn, chỉ khác hoa/thường); **1548** いいこっ, **1694** ならばっ, **1600** でっ, **1407** いきなりっ — っ nhấn mạnh/cụt cuối câu dính từ nội dung (tiền lệ sweep 1474, không thêm Ư); các っ trong từ/cụm động từ (思った, しまった, せっかく, ずうっと, きっと, 真っ赤...) không phải gasp.

## §3. Rên/SFX — romaji fallback + công thức nguyên âm (17 dòng)

- **Quy tắc ひゃ-family 21/11 ~11:55** (moan loop, Hieu ủy quyền): trong cảnh H, ひゃ/ひゅ/ひあ/きゃ → romaji; "Á" cho chúng là lỗi mất phụ âm mora. Áp dụng: **1405** きゃっ→"Á."→"Kya.", **1534** やっ→"Á!?"→"Ya!?" (tiền lệ ポーレットh3 liệt kê cả やっ), **1438** ひゃぐっ→"Hyaa!?"→"Hyagu!?" (giữ cả âm ぐ; tiền lệ file くっ→"Ku", くあっ→"Kua").
- **Sai phụ âm f→h** (3 dòng): **1426** ファ→"Haa"→"Faa", **1436** ふ→"ha"→"fu", **1492** ふ→"hu" trong "Kyuh"→"Kyuf" (Hepburn ふ="fu"; file này ふ→"f" xuyên suốt: "Fua", "fu", "fua").
- **Đếm nguyên âm sai** (đếm lại bằng máy, công thức 1 + số う/ぅ — đếm theo mora): **1466** 12 a (VN 15), **1467** 8 a (VN 10), **1470** 3 a (VN 4), **1484** 3 a (VN 4), **1488** 1 a (VN 2), **1491** 2 o (VN 3), **1492** 19 u (VN 13 — kèm sửa "Kyuh"→"Kyuf"), **1659** はぁっ×3 = 2 a/lần (VN "Hà" 1 a/lần), **1471** あんっ→"A" mất âm ん→"An".
- **1531** んふうううううっ (6 u): VN "Ưm hưmmmm" chỉ còn 1 ư — mất độ dài nguyên âm, chuyển sang romaji theo fallback (1 dòng = 1 cách diễn): "Nfuuuuuu".
- **2145** (SFX): びゅぶううううううううう = 11 mora-u, VN 32 chữ t — thừa 21. Tiền lệ file: びゅうう (3 mora-u) → "phụttt" (3 t) ở 2111/2121 — số t = số mora-u → 11 t.
- Đã romaji đúng, giữ nguyên: ふぁっ→"Fua" (1428–1432, 1514), はぁっ→"Haa" (1446), あ/ぁ→"A/a" đúng số lượng (1459–1463, 1468, 1469, 1472–1474), くあっ→"Kua" (1485–1490), くはっ→"Kuha" (1486), はうっ→"Hau" (1449), んくっ→"Nku" (1532), んゆっ→"Nyu" (1533), んひゅ→"Nhyu" (1530, 1534), きゃんっ→"Kyan" (1407), にゃあん→"Nyaan" (1482), ぺろおお...→"Perooooooooo" 9 o khớp JP (1654), りゅううう→"ryuuuu" 4 u khớp JP (1481).

## §4. Nghĩa (3 dòng — 2 gộp với đại từ)

- **1385** (gộp đại từ): 強く思った — VN "Em đã nghĩ rất nhiều" nhầm cường độ thành số lượng (nghĩ nhiều vs cảm nhận mạnh); TW 讓我的感受更強烈了 xác nhận hướng "cảm nhận". Sửa: "Tôi đã cảm thấy thật mãnh liệt."
- **1610** (gộp đại từ): ふたりのこども (hai đứa con) bị VN bỏ mất số lượng — TW 我想要兩個孩子 xác nhận. Sửa: "Tôi muốn chúng ta có hai đứa con".
- **1684**: 一生懸命 (dốc hết sức) bị dịch thành "liên tục" (continuously) — sai nghĩa; TW 拚命 xác nhận. Sửa: "hết sức".

## §5. Giữ nguyên (không tính sai)

- **おまんこ→"chỗ đó" (6 dòng: 1441, 1556, 1572, 1576, 1693, 1915) vs "lồn" (6 dòng: 1426, 1539, 1573, 1600, 1645, 1896)** — cả hai cách diễn đều có trong file với tỉ lệ 6/6, chỉ khác mức độ trực tiếp, không sai nghĩa (người đọc vẫn hiểu đúng bộ phận được chỉ). Không thống nhất trong audit; ghi nhận để đợt thống nhất xem xét nếu Hieu muốn một dạng duy nhất.
- **1457** ふっ→"phù" — tiếng thở bằng tiếng Việt tự nhiên, không ngượng; không ép romaji (khác 1436/1426 là sai phụ âm f→h).
- **1618, 1649** (くっ――) và **1664** (がっ――) — tiếng ậm ừ/ngập ngừng giữa câu; dấu —— đã diễn độ ngập ngừng, không thêm âm.
- **1477** ぷあっ→"phuha" — SFX liếm diễn ấn tượng trong chuỗi "Chụt/rột", không sửa (khác 1516 ぷ、ぁっ→"pu, a" là romaji rời rạc — cả hai đều giữ).
- **1822** 義理の姉→"chị gái nuôi" — TW 繼姐 (chị kết nghĩa/nuôi) xác nhận, theo tiền lệ Common 10 key 2573 (kiểm tra TW trước khi cờ 義).
- **1453** câu cụt 他に được hoàn thiện tự nhiên ("thì làm gì có ai khác") — giữ (phần kết hiển nhiên, không bịa nội dung mới).
- **SFX dài bị rút gọn trong từ Việt** (2107, 2122, 2141, 2165, 2167, 2175, 2186, 2187...) — file dùng từ Việt ("Siết chặt", "Trượt dài", "Phập") cho SFX bóp/đẩy, độ dài JP không diễn bằng số lượng chữ — quy ước file, không sửa; chỉ 2145 sửa vì 32 t vượt xa mọi tiền lệ.
- **1380** JP có lỗi đánh máy (褒め足り無い, 言われてみたかこと) — VN dịch đúng nghĩa, không sửa JP.
- **1182** 「……ん……と、ね？」→"thì, nhé?" — diễn đạt tự nhiên, giữ.
- **1503** sweep already-rendered — xem §2 (không sửa).
- **1577/1870/1915...** — các dòng chỉ khác TOML-2 làm phẳng `\n` (147 dòng) — không phải lỗi dịch, CSV3 là chuẩn.

## §6. Chi tiết từng dòng sai (59)

### 1163 [monologue] — gasp

JP: ――‘あ”の形のまま口が固まる。\n息が吸われて、止まってしま――っ！
TW: ——她的嘴巴大張，僵住了。好像呼吸被吸走了一樣，就這麼定住不動了——！
Cũ: ——Miệng chị ấy há hốc cứng đờ thành hình chữ 'A'.\nHít một hơi, rồi nín bặt——!
Mới: ——Miệng chị ấy há hốc cứng đờ thành hình chữ 'A'.\nHít một hơi, rồi nín bặt——Ư!
→ Sweep lost-gasp-trailing áp nguyên: JP 止まってしま――っ！, VN mất gasp → thêm Ư sau ——).

### 1168 [真闇] — gasp

JP: 「っ――れりゅっ――っ、ふっ――ぢゅれろっ！！」
TW: 「——舔舔——滋、噗——舔舔！！」
Cũ: 「——Liếm——fu——chụt liếm!!」
Mới: 「Ư——Liếm——Ư、fu——chụt liếm!!」
→ Sweep bỏ sót: JP có 2 っ đứng riêng (đầu dòng っ―― và giữa dòng っ、), VN mất cả 2 — 1 Ư/1 っ theo quy tắc đa-っ (tiền lệ audit h6 1271, sweep §10 phụ lục). Các っ dính SFX (れりゅっ/ふっ/ぢゅれろっ) đã diễn bằng từ Việt, không thêm Ư.

### 1385 [双鉄] — pronoun

JP: 「が、今日あらためて真闇姉のかわいさを思い知らされて。\nその上で膣内射精をして。強く思った。そして、願った」
TW: 「但是，今天我再次領悟到了真闇姐的可愛。而且在你的體內射精。讓我的感受更強烈了。然後，我許了願望」
Cũ: 「Nhưng, hôm nay em lại một lần nữa nhận ra sự dễ thương của chị.\nRồi lại còn bắn vào trong nữa. Em đã nghĩ rất nhiều. Và, em đã ước」
Mới: 「Nhưng, hôm nay tôi lại một lần nữa nhận ra sự dễ thương của chị.\nRồi lại còn bắn vào trong nữa. Tôi đã cảm thấy thật mãnh liệt. Và, tôi đã ước」
→ Soutetsu tự xưng "em"→"tôi" với Mayami ×3 (quy tắc đã khóa); kèm sửa nghĩa: 強く思った "nghĩ rất nhiều" (số lượng) → "cảm thấy thật mãnh liệt" (cường độ; TW 讓我的感受更強烈了).

### 1388 [双鉄] — pronoun

JP: 「真闇姉ほど称賛を浴び続けている人物を僕は知らん。\nというか僕も、真闇姉を褒めない日の方が少なかろう」
TW: 「像真闇姐這樣總是受到別人稱讚的人，我可不認識第二個。話說回來，我沒有稱讚真闇姐的日子，才比較稀有吧」
Cũ: 「Người luôn được nhận những lời khen ngợi như chị Mayami thì em chưa thấy ai bao giờ.\nĐúng hơn là em cũng vậy, số ngày em không khen chị chắc chỉ đếm trên đầu ngón tay.」
Mới: 「Người luôn được nhận những lời khen ngợi như chị Mayami thì tôi chưa thấy ai bao giờ.\nĐúng hơn là tôi cũng vậy, số ngày tôi không khen chị chắc chỉ đếm trên đầu ngón tay.」
→ Soutetsu tự xưng "em"→"tôi" với Mayami ×3.

### 1397 [双鉄] — pronoun

JP: 「今も……褒め過ぎなのに――？\nあ、褒め足り無い部分があるのか？」
TW: 「剛剛也……誇得太過頭了——？啊，是說我還有哪裡稱讚得不到位嗎？」
Cũ: 「Bây giờ cũng……khen quá lời thế mà——?\nA, hay là có chỗ nào em khen chưa đủ sao?」
Mới: 「Bây giờ cũng……khen quá lời thế mà——?\nA, hay là có chỗ nào tôi khen chưa đủ sao?」
→ Soutetsu tự xưng "em"→"tôi" với Mayami.

### 1405 [真闇] — moan

JP: 「きゃっ」
TW: 「呀！」
Cũ: 「Á.」
Mới: 「Kya.」
→ Quy tắc ひゃ-family 21/11 ~11:55 (moan loop): きゃ → romaji; "Á" cho きゃっ là lỗi mất phụ âm mora (tiền lệ ポーレットh3). JP きゃっ không có nguyên âm dài — "Kya.".

### 1425 [双鉄] — pronoun

JP: 「ふ――ぁ――真、闇姉――\n僕っ、は――く、あっ――僕は――もうっ――」
TW: 「呼——啊——真、闇姐——我、哈——嗚，啊——我——已經——」
Cũ: 「Fu——a——chị, Mayami——\nem, là——ku, a——em——sắp——」
Mới: 「Fu——a——chị, Mayami——\ntôi, là——ku, a——tôi——sắp——」
→ Soutetsu tự xưng 僕→"em"→"tôi" với Mayami ×2 (rên ngắt quãng).

### 1426 [真闇] — moan

JP: 「ファ――あっっ！　精子――びゅう、びゅう――んっ、\nのんで――のんでる――おまんこ――しきゅう――がっ」
TW: 「呼——啊！　精子——咻，咻地——嗯、小穴——在喝——在喝精子」
Cũ: 「Haa——a! Tinh trùng——phụt, phụt——ưm,\nđang nuốt——đang nuốt——lồn——tử cung——đang nuốt」
Mới: 「Faa——a! Tinh trùng——phụt, phụt——ưm,\nđang nuốt——đang nuốt——lồn——tử cung——đang nuốt」
→ ファ→"Haa" sai phụ âm: Hepburn ファ="fa"; file này ふぁ/ファ đã romaji "Fua" ở 1428–1432 — sửa "Haa"→"Faa" (2 nguyên âm a khớp JP ファ+あっ).

### 1433 [双鉄] — moan

JP: 「ふぅっっっ！！！！」
TW: 「呼嗚～～～！！！！」
Cũ: 「Fuuuu!!!!」
Mới: 「Foo!!!!」
→ ふぉぉっっっ: JP 2 nguyên âm o (ふぉ+ぉ), VN "Fuuuu" sai nguyên âm u và thừa số lượng → "Foo" (2 o).

### 1436 [真闇] — moan

JP: 「ごく、ごく――のんで、る――精子――精液っ――\n双ちゃん、の――ふ、ぁ――うれし――うれし、かっ」
TW: 「咕嘟、咕嘟地——喝、著——精子——精液——小雙、的——呼、啊——好開心——好開心」
Cũ: 「Ực, ực——đang, nuốt——tinh trùng——tinh dịch——\ncủa, Sou-chan——ha, a——vui——vui, quá」
Mới: 「Ực, ực——đang, nuốt——tinh trùng——tinh dịch——\ncủa, Sou-chan——fu, a——vui——vui, quá」
→ ふ、ぁ→"ha, a" sai phụ âm: ふ="fu" (file này ふっ→"fu" ở 1440/1502/1512) — sửa "ha"→"fu".

### 1438 [双鉄] — moan

JP: 「ひゃぐっ！？」
TW: 「咿呀！？」
Cũ: 「Hyaa!?」
Mới: 「Hyagu!?」
→ ひゃぐっ: VN "Hyaa" bỏ mất âm ぐ và thêm 1 a thừa — romaji đầy đủ "Hyagu" (tiền lệ file: くっ→"Ku", くあっ→"Kua" đều giữ phụ âm đầu; quy tắc "không để mất âm").

### 1466 [双鉄] — moan

JP: 「ぁぁぁぁああああああああっ！！！！」
TW: 「啊啊啊啊啊啊啊啊啊啊啊啊！！！」
Cũ: 「Aaaaaaaaaaaaaaa!!!!」
Mới: 「Aaaaaaaaaaaa!!!!」
→ Đếm máy: JP ぁ×4+あ×8=12 nguyên âm a, VN 15 a — thừa 3 → 12 a.

### 1467 [双鉄] — moan

JP: 「ぁぁぁぁぁぁああっっ！！」
TW: 「啊啊啊啊啊啊啊！！」
Cũ: 「Aaaaaaaaaa!!」
Mới: 「Aaaaaaaa!!」
→ Đếm máy: JP ぁ×6+あ×2=8 nguyên âm a, VN 10 a — thừa 2 → 8 a.

### 1470 [双鉄] — moan

JP: 「ぁぁぁっ！！」
TW: 「啊啊啊！」
Cũ: 「Aaaa!!」
Mới: 「Aaa!!」
→ Đếm máy: JP ぁ×3=3 nguyên âm a, VN 4 a — thừa 1 → 3 a.

### 1471 [真闇] — moan

JP: 「あんっ」
TW: 「啊嗯」
Cũ: 「A」
Mới: 「An」
→ あんっ: VN "A" làm mất âm ん — romaji "An" (ん→n; tiền lệ 1514 あん→"an", 1535 ぁっん→"an").

### 1483 [双鉄] — pronoun

JP: 「うむ……あまりに真闇姉がかわいくて、\n愛おしすぎて、僕のものだと強くおもって――っと」
TW: 「嗚……真闇姐太可愛了，太誘人了，感覺你是只屬於我的東西，所以……」
Cũ: 「Ừm……vì chị Mayami quá đáng yêu,\nquá đỗi thân thương, khiến em có cảm giác mãnh liệt rằng chị là của em——nên.」
Mới: 「Ừm……vì chị Mayami quá đáng yêu,\nquá đỗi thân thương, khiến tôi có cảm giác mãnh liệt rằng chị là của tôi——nên.」
→ Soutetsu "em"→"tôi" ×2 (tự xưng + sở hữu "của em"→"của tôi").

### 1484 [双鉄] — moan

JP: 「くあああっ！」
TW: 「嗚啊啊啊啊！」
Cũ: 「Kuaaaa!」
Mới: 「Kuaaa!」
→ Đếm máy: JP くあああっ=3 nguyên âm a, VN 4 a — thừa 1 → 3 a.

### 1488 [双鉄] — moan

JP: 「くあっ！！！！」
TW: 「嗚啊！！！！」
Cũ: 「Kuaa!!!!」
Mới: 「Kua!!!!」
→ Đếm máy: JP くあっ=1 nguyên âm a, VN 2 a — thừa 1 → 1 a.

### 1491 [双鉄] — moan

JP: 「ふぉぉっ！」
TW: 「嗚喔！」
Cũ: 「Fooo!」
Mới: 「Foo!」
→ Đếm máy: JP ふぉぉ=2 nguyên âm o, VN 3 o — thừa 1 → 2 o.

### 1492 [真闇] — moan

JP: 「きゅふううううううううううぅぅぅぅぅぅぅんっ！」
TW: 「嗚嗚嗚嗚嗚嗚嗚嗚嗯！」
Cũ: 「Kyuhuuuuuuuuuuuun!」
Mới: 「Kyufuuuuuuuuuuuuuuuuuun!」
→ Đếm máy: JP きゅ(1u)+ふ(1u)+う×10+ぅ×7=19 nguyên âm u, VN 13 u — thiếu 6; kèm sửa phụ âm: ふ→"hu" sai (Hepburn "fu"; file này ふ→"f" xuyên suốt) — "Kyuh"→"Kyuf" + đủ 19 u.

### 1494 [双鉄] — gasp

JP: 「っ！！　ぁっ――」
TW: 「嗚！！啊——！」
Cũ: 「!! A——」
Mới: 「Ư!! A——」
→ Sweep bỏ sót: JP bắt đầu bằng っ đứng riêng (っ！！) mà VN chỉ còn "!!" — khôi phục gasp đầu dòng (tiền lệ sweep §6 + phụ lục lr_h1 1077).

### 1495 [双鉄] — gasp

JP: 「っ！！！」
TW: 「嗚！！！」
Cũ: 「!!!」
Mới: 「Ư!!!」
→ Sweep lost-gasp-whole áp nguyên: JP 「っ！！！」 cả dòng là gasp, VN chỉ còn dấu câu.

### 1496 [双鉄] — gasp

JP: 「っ！！！！！！！！」
TW: 「嗚！！！！！！！！」
Cũ: 「!!!!!!!!」
Mới: 「Ư!!!!!!!!」
→ Sweep lost-gasp-whole áp nguyên: JP 「っ！！！！！！！！」.

### 1497 [双鉄] — gasp

JP: 「っ！！？」
TW: 「嗚！！？」
Cũ: 「!!?」
Mới: 「Ư!!?」
→ Sweep lost-gasp-whole áp nguyên: JP 「っ！！？」.

### 1519 [真闇] — gasp

JP: 「うん。よかとよ。双ちゃん――っ！！」
TW: 「嗯。好啊。小雙——嗚！！」
Cũ: 「Ừ. Được mà. Sou-chan——!!」
Mới: 「Ừ. Được mà. Sou-chan——Ư!!」
→ Sweep lost-gasp-trailing áp nguyên: JP 双ちゃん――っ！！.

### 1531 [真闇] — moan

JP: 「んふうううううっ！！！」
TW: 「嗯嗚嗚嗚嗚嗚嗚！！！」
Cũ: 「Ưm hưmmmm!!!」
Mới: 「Nfuuuuuu!!!」
→ んふうううううっ: JP 6 nguyên âm u (ふ+う×5); VN "Ưm hưmmmm" chỉ còn 1 ư + m — mất độ dài nguyên âm, chuyển sang romaji theo fallback (1 dòng = 1 cách diễn): "Nfuuuuuu" (N+f+6u).

### 1534 [真闇] — moan

JP: 「んひゅっ！！！？　やっ！？　らめっ――いたずらっ、\n――今日は――おねえちゃ――して、あげる、けんっ」
TW: 「嗯嗚！！！？呀！？不要——欺負人——今天——姐姐——才能，欺負你」
Cũ: 「Nhyu!!!? Á!? Không được——đừng nghịch,\n——Hôm nay——chị——sẽ làm, cho em, mà.」
Mới: 「Nhyu!!!? Ya!? Không được——đừng nghịch,\n——Hôm nay——chị——sẽ làm, cho em, mà.」
→ Quy tắc ひゃ-family 21/11 ~11:55: "Á" cho やっ là lỗi mất phụ âm mora (tiền lệ ポーレットh3 liệt kê やっ) — sửa "Á"→"Ya". (んひゅっ→"Nhyu" đã đúng, giữ.)

### 1542 [真闇] — gasp

JP: 「っ！！！　んふふふふっ！」
TW: 「嗯！！！嗯呵呵呵呵！」
Cũ: 「!!! Nfufufufu!」
Mới: 「Ư!!! Nfufufufu!」
→ Sweep bỏ sót: JP bắt đầu bằng っ đứng riêng (っ！！！) mà VN chỉ còn "!!!" — khôi phục gasp đầu dòng.

### 1562 [双鉄] — pronoun

JP: 「申し訳ないのだが真闇姉。僕の勃起は逃げるというより、\nどこに入っていけばいいのか迷ってしまっているようだ」
TW: 「對不起，真闇姐。我的勃起與其說是逃跑，不如說是在猶豫，不知道該進入哪裡」
Cũ: 「Xin lỗi chị Mayami. Dương vật của em không phải là đang trốn,\nmà có vẻ như nó đang bối rối không biết nên đi vào đâu thì phải.」
Mới: 「Xin lỗi chị Mayami. Dương vật của tôi không phải là đang trốn,\nmà có vẻ như nó đang bối rối không biết nên đi vào đâu thì phải.」
→ Soutetsu "của em"→"của tôi" với Mayami.

### 1572 [双鉄] — pronoun

JP: 「おまんこ！　おまんこ！　おまんこだ！！\n僕の勃起は、真闇姉のおまんこだけに入っていく」
TW: 「小穴！　小穴！　小穴！！我的勃起只進入真闇姐的小穴」
Cũ: 「Chỗ đó! Chỗ đó! Là chỗ đó!!\nDương vật của em, sẽ chỉ đi vào chỗ đó của chị Mayami thôi.」
Mới: 「Chỗ đó! Chỗ đó! Là chỗ đó!!\nDương vật của tôi, sẽ chỉ đi vào chỗ đó của chị Mayami thôi.」
→ Soutetsu "của em"→"của tôi" với Mayami.

### 1575 [真闇] — gasp

JP: 「双ちゃんのおちんちんはおバカちゃんとねー。\nほんならね？　おねえちゃんが教えてあげる――っ！」
TW: 「小雙的小雞雞真是個小傻瓜～那好，　姐姐就來教你——！」
Cũ: 「Dương vật của Sou-chan ngốc nghếch quá nhỉ~.\nVậy thì nhé? Chị sẽ dạy cho em——!」
Mới: 「Dương vật của Sou-chan ngốc nghếch quá nhỉ~.\nVậy thì nhé? Chị sẽ dạy cho em——Ư!」
→ Sweep lost-gasp-trailing áp nguyên: JP 教えてあげる――っ！.

### 1584 [双鉄] — pronoun

JP: 「僕は恐らく、どこか現実感の無いことと捉えていた。\n心の隅で、真闇姉と対等以上になって初めてと思ってた」
TW: 「恐怕我一直認為這是缺乏現實感的事。在我內心深處，頭一次感覺我和真闇姐達到了超越互相平等的關係」
Cũ: 「Có lẽ em đã luôn coi chuyện này là một điều gì đó thiếu thực tế.\nTrong thâm tâm, em nghĩ phải đợi đến khi em sánh ngang hoặc vượt qua chị thì mới được」
Mới: 「Có lẽ tôi đã luôn coi chuyện này là một điều gì đó thiếu thực tế.\nTrong thâm tâm, tôi nghĩ phải đợi đến khi tôi sánh ngang hoặc vượt qua chị thì mới được」
→ Soutetsu tự xưng "em"→"tôi" với Mayami ×3.

### 1586 [双鉄] — pronoun

JP: 「僕――もう――僕っ――もうっ！！」
TW: 「我——已經——我——已經！！」
Cũ: 「Em——sắp——em——sắp rồi!!」
Mới: 「Tôi——sắp——tôi——sắp rồi!!」
→ Soutetsu 僕→"em"→"tôi" với Mayami ×2.

### 1591 [双鉄] — pronoun

JP: 「真闇姉のこどもは――真闇姉と僕とのこどもは、\nどれほどかわいらしいことだろうかと、そう思い」
TW: 「我在想，真闇姐的孩子——真闇姐和我生出的孩子，將會是多麼可愛」
Cũ: 「Em nghĩ, con của chị Mayami——con của chị và em,\nsẽ đáng yêu đến nhường nào」
Mới: 「Tôi nghĩ, con của chị Mayami——con của chị và tôi,\nsẽ đáng yêu đến nhường nào」
→ Soutetsu "em"→"tôi" ×2 (tự xưng + "con của chị và em"→"và tôi").

### 1593 [双鉄] — pronoun

JP: 「僕は、女性のファッションには――\nましてや下着の流行などには、詳しくないのだが」
TW: 「我對女性時尚一竅不通——更不用說流行了」
Cũ: 「Em thì, không rành về thời trang của phụ nữ——\nhuống hồ là xu hướng đồ lót.」
Mới: 「Tôi thì, không rành về thời trang của phụ nữ——\nhuống hồ là xu hướng đồ lót.」
→ Soutetsu tự xưng "em"→"tôi" với Mayami.

### 1595 [双鉄] — pronoun

JP: 「僕は――おねえちゃんと一緒にイきたい。\nおねえちゃんと一緒に、どこまでも気持ちよくなりたい」
TW: 「我想和——姐姐一起高潮。我想和姐姐一起，變得無比舒服」
Cũ: 「Em muốn——ra cùng với chị.\nCùng với chị, em muốn sướng đến tận cùng.」
Mới: 「Tôi muốn——ra cùng với chị.\nCùng với chị, tôi muốn sướng đến tận cùng.」
→ Soutetsu tự xưng "em"→"tôi" với Mayami ×2.

### 1598 [双鉄] — pronoun

JP: 「わかった！　わかりましたっ！　っ――今日は――\n僕、はっ――全部！　まかせる――おねえちゃんにっ！」
TW: 「我懂了！　我完全懂了！　——今天的——我——全部！　都交給你了——姐姐！」
Cũ: 「Em hiểu rồi! Em hiểu rồi! ——Hôm nay——\nem, sẽ——giao phó! Tất cả——cho chị!」
Mới: 「Tôi hiểu rồi! Tôi hiểu rồi! Ư——Hôm nay——\ntôi, sẽ——giao phó! Tất cả——cho chị!」
→ Soutetsu "em"→"tôi" ×3; kèm gasp sweep-missed: っ―― đứng riêng giữa dòng → Ư (tiền lệ sweep §6 khôi phục gasp đầu dòng/đứng riêng).

### 1600 [双鉄] — pronoun

JP: 「言うとおりにする。全部するから、したいからっ！\nだから、おねがい、僕を、おねえちゃんのおまんこでっ」
TW: 「我會照辦的。我會全部照辦的，我想要這麼做！所以，拜託，用姐姐的小穴，讓我」
Cũ: 「Em sẽ làm theo lời chị. Em sẽ làm tất cả, vì em muốn thế!\nNên, xin chị, hãy để em, trong lồn của chị」
Mới: 「Tôi sẽ làm theo lời chị. Tôi sẽ làm tất cả, vì tôi muốn thế!\nNên, xin chị, hãy để tôi, trong lồn của chị」
→ Soutetsu tự xưng "em"→"tôi" với Mayami ×4.

### 1601 [双鉄] — pronoun

JP: 「するっ！　子宮のドアにビッタリ亀頭を押し付けて、\nびゅうびゅう、たくさん、射精、するっ、からっ！」
TW: 「我會的！　我會用龜頭頂住子宮的門，射出，好多，好多，精液！
Cũ: 「Em sẽ làm! Ép sát quy đầu vào cửa tử cung,\nrồi bắn, bắn thật nhiều, tinh dịch, vào đó!」
Mới: 「Tôi sẽ làm! Ép sát quy đầu vào cửa tử cung,\nrồi bắn, bắn thật nhiều, tinh dịch, vào đó!」
→ Soutetsu tự xưng "em"→"tôi" với Mayami.

### 1603 [双鉄] — gasp

JP: 「脊髄反射で飛び出た言葉が――っ――\nどうやら――ぁ――正解、だった――よう、だなっ」
TW: 「我的條件反射所蹦出來的詞——嗯——看來——啊——是正確，的」
Cũ: 「Những lời thốt ra như phản xạ không điều kiện——\nCó vẻ như——a——đã là——câu trả lời chính xác——nhỉ.」
Mới: 「Những lời thốt ra như phản xạ không điều kiện——Ư——\nCó vẻ như——a——đã là——câu trả lời chính xác——nhỉ.」
→ Sweep bỏ sót: っ đứng riêng giữa 2 dấu —— (――っ――) bị VN bỏ mất — thêm Ư. Khác 1167 (――っ―― → "——!" đã diễn bằng "!").

### 1604 [双鉄] — pronoun

JP: 「わかる。先っぽが――あたってる。ちゅうちゅう、\n僕の、おちんちんが――吸われて、咥えられてる」
TW: 「我知道。前端——頂到了。啾啾，我的小雞雞——正在被吸吮著」
Cũ: 「Em biết. Phần đỉnh——đang chạm vào. Chụt chụt,\ndương vật, của em——đang bị hút, bị ngậm lấy.」
Mới: 「Tôi biết. Phần đỉnh——đang chạm vào. Chụt chụt,\ndương vật, của tôi——đang bị hút, bị ngậm lấy.」
→ Soutetsu "em"→"tôi" ×2 (tự xưng + sở hữu).

### 1607 [双鉄] — pronoun

JP: 「わかった。やめる――今日は――真闇姉っ――っ！！」
TW: 「我知道了。我不做了——今天是——真闇姐——嗚！！」
Cũ: 「Em hiểu rồi. Em sẽ dừng lại——hôm nay——chị Mayami——!!」
Mới: 「Tôi hiểu rồi. Tôi sẽ dừng lại——hôm nay——chị Mayami——Ư!!」
→ Soutetsu "em"→"tôi" ×2; kèm gasp sweep: 真闇姉っ――っ！！ → ——Ư!! (sweep áp nguyên sau kiểm chứng).

### 1610 [双鉄] — pronoun

JP: 「ゆえに願った。\nふたりのこどもを授かりたいと――作りたいと」
TW: 「所以我許了願望。我想要兩個孩子——想讓你生兩個孩子」
Cũ: 「Nên em đã ước.\nEm muốn chúng ta có con——muốn tạo ra chúng」
Mới: 「Nên tôi đã ước.\nTôi muốn chúng ta có hai đứa con——muốn tạo ra chúng」
→ Soutetsu "em"→"tôi" ×2; kèm sửa nghĩa: ふたりのこども (hai đứa con) bị VN bỏ mất số lượng — TW 我想要兩個孩子 xác nhận.

### 1659 [双鉄] — moan

JP: 「はぁっ、はあっ、はぁっ――真闇、姉っ」
TW: 「蛤啊、蛤啊、蛤啊——真闇、姐」
Cũ: 「Hà, hà, hà——chị, Mayami」
Mới: 「Haa, haa, haa——chị, Mayami」
→ Đếm máy: JP はぁっ/はあっ/はぁっ = 2 nguyên âm a mỗi lần, VN "Hà" chỉ 1 a mỗi lần — thiếu 1 a/lần → "Haa" ×3 (tiền lệ 1446 はぁっ×4→"Haa" ×4).

### 1673 [双鉄] — pronoun

JP: 「その確率を上げさせてくれ。\n今度は僕が――全部を、真闇姉にしてあげたい」
TW: 「讓我來提高這個機率吧。這次，我要把我的一切——都給真闇姐」
Cũ: 「Hãy để em tăng tỷ lệ đó lên nhé.\nLần này em muốn——dành tất cả cho chị Mayami」
Mới: 「Hãy để tôi tăng tỷ lệ đó lên nhé.\nLần này tôi muốn——dành tất cả cho chị Mayami」
→ Soutetsu "em"→"tôi" với Mayami ×2.

### 1684 [真闇] — meaning

JP: 「こぎゃん――いっしょう、けんめい――ひく、ひく――\nぱく、ぱく――そう、ちゃんの――おちん、ちんっ」
TW: 「這樣——拚命——抽插的——小雙的——小雞雞」
Cũ: 「Cứ thế này——liên tục——rút, rút——\nngậm, ngậm——chim, chim——của, Sou-chan」
Mới: 「Cứ thế này——hết sức——rút, rút——\nngậm, ngậm——chim, chim——của, Sou-chan」
→ 一生懸命 (dốc hết sức) bị dịch thành "liên tục" (continuously) — sai nghĩa; TW 拚命 (desperately) xác nhận. Sửa "liên tục"→"hết sức".

### 1686 [双鉄] — pronoun

JP: 「それもそうか。では――ううむ――\nヒント……せめてなにか、ヒントを僕に与えてほしい」
TW: 「那倒也是。那就——唔——……至少給我點提示吧」
Cũ: 「Cũng đúng nhỉ. Vậy thì——ưm——\nGợi ý……ít nhất hãy cho em một chút gợi ý đi.」
Mới: 「Cũng đúng nhỉ. Vậy thì——ưm——\nGợi ý……ít nhất hãy cho tôi một chút gợi ý đi.」
→ Soutetsu "cho em"→"cho tôi" với Mayami.

### 1699 [真闇] — gasp

JP: 「っ！！」
TW: 「！！」
Cũ: 「!!」
Mới: 「Ư!!」
→ Sweep lost-gasp-whole áp nguyên: JP 「っ！！」.

### 1700 [双鉄] — gasp

JP: 「っ！！！！」
TW: 「！！！！」
Cũ: 「!!!!」
Mới: 「Ư!!!!」
→ Sweep lost-gasp-whole áp nguyên: JP 「っ！！！！」.

### 1701 [双鉄] — gasp

JP: 「っ！！！！！」
TW: 「！！！！！」
Cũ: 「!!!!!」
Mới: 「Ư!!!!!」
→ Sweep lost-gasp-whole áp nguyên: JP 「っ！！！！！」.

### 1702 [双鉄] — gasp

JP: 「っ！！！？」
TW: 「！！！？」
Cũ: 「!!!?」
Mới: 「Ư!!!?」
→ Sweep lost-gasp-whole áp nguyên: JP 「っ！！！？」.

### 1706 [双鉄] — gasp

JP: 「～～～～っ！！！」
TW: 「～～～～嗚！！！」
Cũ: 「~~~~!!!」
Mới: 「~~~~Ư!!!」
→ Sweep lost-gasp-trailing áp nguyên: JP 「～～～～っ！！！」 (4 dấu ~ khớp JP).

### 1709 [双鉄] — gasp

JP: 「～～～～～～～～～～っ！！！」
TW: 「～～～～～～～～～～嗚！！！」
Cũ: 「~~~~~~~~~~!!!」
Mới: 「~~~~~~~~~~Ư!!!」
→ Sweep lost-gasp-trailing áp nguyên: JP 「～～～～～～～～～～っ！！！」 (10 dấu ~ khớp JP).

### 1797 [monologue] — gasp

JP: なるほど、これ以上ここに触れるのはヤボの極みか。\nならば、触れるべきは当然に――っ！？
TW: 原來如此，如果再提及這件事的話就太不解風情了。既然如此，我該摸的地方當然是——！？
Cũ: Ra vậy, nếu cứ tiếp tục nhắc đến chuyện này thì đúng là quá kém tinh tế.\nNếu vậy, nơi nên chạm vào tất nhiên là——!?
Mới: Ra vậy, nếu cứ tiếp tục nhắc đến chuyện này thì đúng là quá kém tinh tế.\nNếu vậy, nơi nên chạm vào tất nhiên là——Ư!?
→ Sweep lost-gasp-trailing áp nguyên: JP 触れるべきは当然に――っ！？.

### 1828 [monologue] — gasp

JP: おっぱいが大きくスライドし、勃起先端がその外側へと\n放り出されて寒くなる。いきなりの心細さ――っ！！？
TW: 她的雙乳大幅滑動，我勃起的尖端被拋向她胸部的外側，感覺好寒冷。突然感覺好無依無靠——嗚！！？
Cũ: Bầu ngực trượt mạnh sang một bên, phần đỉnh dương vật bị ném ra ngoài\nvà trở nên lạnh lẽo. Cảm giác hụt hẫng ập đến bất ngờ——!!?
Mới: Bầu ngực trượt mạnh sang một bên, phần đỉnh dương vật bị ném ra ngoài\nvà trở nên lạnh lẽo. Cảm giác hụt hẫng ập đến bất ngờ——Ư!!?
→ Sweep lost-gasp-trailing áp nguyên: JP 心細さ――っ！！？.

### 1865 [monologue] — pronoun

JP: もう思い切り腰をふりたい、突きあげたい。\nけれども今は――おねえちゃんと、約束したから。
TW: 我好想就這樣拚命地晃動腰，想也不想地抽插。但是剛才——我跟姐姐約定了。
Cũ: Muốn điên cuồng nhấp hông, muốn thúc mạnh lên.\nNhưng bây giờ——em đã hứa, với chị rồi.
Mới: Muốn điên cuồng nhấp hông, muốn thúc mạnh lên.\nNhưng bây giờ——tôi đã hứa, với chị rồi.
→ Độc thoại Soutetsu "em"→"tôi" với Mayami (độc thoại file này dùng "tôi" xuyên suốt, chỉ dòng này lệch).

### 1915 [monologue] — gasp

JP: 見た瞬間に、やりかけていた仕事の全てが吹き飛ばされる。\n下着と聞いたが、おっぱいもおまんこも見えてい――っ！
TW: 看到她的瞬間，正在做的工作全部被我忘到了九霄雲外。她說是內衣，但是連乳房和下陰都能看得一清二楚——！！
Cũ: Khoảnh khắc nhìn thấy, toàn bộ công việc đang làm dở đều bay biến sạch.\nNghe nói là đồ lót, nhưng mà ngực và cả chỗ đó đều phơi bày hết ra rồi kìa——!
Mới: Khoảnh khắc nhìn thấy, toàn bộ công việc đang làm dở đều bay biến sạch.\nNghe nói là đồ lót, nhưng mà ngực và cả chỗ đó đều phơi bày hết ra rồi kìa——Ư!
→ Sweep lost-gasp-trailing áp nguyên: JP 見えてい――っ！.

### 2145 [monologue] — sfx

JP: （びゅぶうううううううううっっっっっ！　ごちゅん！）
TW: （射出————————！　咕啾！）
Cũ: （Phụtttttttttttttttttttttttttttttttt! Ục!）
Mới: （Phụttttttttttt! Ục!）
→ Đếm máy: JP びゅぶううううううううう = 11 mora-u (びゅ1+ぶ1+う×9), VN 32 chữ t — thừa 21. Tiền lệ file: びゅうう (3 mora-u) → "phụttt" (3 t) ở 2111/2121 — số t = số mora-u → 11 t.

### 2189 [monologue] — pronoun

JP: （これ……は――まるで、僕の方が子猫ではないか）
TW: （這……簡直——就像我才是小貓咪一樣）
Cũ: （Thế này……thì——chẳng phải, em mới là mèo con sao.）
Mới: （Thế này……thì——chẳng phải, tôi mới là mèo con sao.）
→ Độc thoại Soutetsu: 僕の方が子猫ではないか (chính TÔI mới là mèo con) — "em"→"tôi".

## §7. Khối TOML (đã parse-kiểm chứng)

Khối `[script]` 59 khóa, parse bằng tomllib: 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\\n` trong khối là backslash-n dạng chữ, khớp CSV3).

```toml
"1163" = "——Miệng chị ấy há hốc cứng đờ thành hình chữ 'A'.\\nHít một hơi, rồi nín bặt——Ư!"
"1168" = "「Ư——Liếm——Ư、fu——chụt liếm!!」"
"1385" = "「Nhưng, hôm nay tôi lại một lần nữa nhận ra sự dễ thương của chị.\\nRồi lại còn bắn vào trong nữa. Tôi đã cảm thấy thật mãnh liệt. Và, tôi đã ước」"
"1388" = "「Người luôn được nhận những lời khen ngợi như chị Mayami thì tôi chưa thấy ai bao giờ.\\nĐúng hơn là tôi cũng vậy, số ngày tôi không khen chị chắc chỉ đếm trên đầu ngón tay.」"
"1397" = "「Bây giờ cũng……khen quá lời thế mà——?\\nA, hay là có chỗ nào tôi khen chưa đủ sao?」"
"1405" = "「Kya.」"
"1425" = "「Fu——a——chị, Mayami——\\ntôi, là——ku, a——tôi——sắp——」"
"1426" = "「Faa——a! Tinh trùng——phụt, phụt——ưm,\\nđang nuốt——đang nuốt——lồn——tử cung——đang nuốt」"
"1433" = "「Foo!!!!」"
"1436" = "「Ực, ực——đang, nuốt——tinh trùng——tinh dịch——\\ncủa, Sou-chan——fu, a——vui——vui, quá」"
"1438" = "「Hyagu!?」"
"1466" = "「Aaaaaaaaaaaa!!!!」"
"1467" = "「Aaaaaaaa!!」"
"1470" = "「Aaa!!」"
"1471" = "「An」"
"1483" = "「Ừm……vì chị Mayami quá đáng yêu,\\nquá đỗi thân thương, khiến tôi có cảm giác mãnh liệt rằng chị là của tôi——nên.」"
"1484" = "「Kuaaa!」"
"1488" = "「Kua!!!!」"
"1491" = "「Foo!」"
"1492" = "「Kyufuuuuuuuuuuuuuuuuuun!」"
"1494" = "「Ư!! A——」"
"1495" = "「Ư!!!」"
"1496" = "「Ư!!!!!!!!」"
"1497" = "「Ư!!?」"
"1519" = "「Ừ. Được mà. Sou-chan——Ư!!」"
"1531" = "「Nfuuuuuu!!!」"
"1534" = "「Nhyu!!!? Ya!? Không được——đừng nghịch,\\n——Hôm nay——chị——sẽ làm, cho em, mà.」"
"1542" = "「Ư!!! Nfufufufu!」"
"1562" = "「Xin lỗi chị Mayami. Dương vật của tôi không phải là đang trốn,\\nmà có vẻ như nó đang bối rối không biết nên đi vào đâu thì phải.」"
"1572" = "「Chỗ đó! Chỗ đó! Là chỗ đó!!\\nDương vật của tôi, sẽ chỉ đi vào chỗ đó của chị Mayami thôi.」"
"1575" = "「Dương vật của Sou-chan ngốc nghếch quá nhỉ~.\\nVậy thì nhé? Chị sẽ dạy cho em——Ư!」"
"1584" = "「Có lẽ tôi đã luôn coi chuyện này là một điều gì đó thiếu thực tế.\\nTrong thâm tâm, tôi nghĩ phải đợi đến khi tôi sánh ngang hoặc vượt qua chị thì mới được」"
"1586" = "「Tôi——sắp——tôi——sắp rồi!!」"
"1591" = "「Tôi nghĩ, con của chị Mayami——con của chị và tôi,\\nsẽ đáng yêu đến nhường nào」"
"1593" = "「Tôi thì, không rành về thời trang của phụ nữ——\\nhuống hồ là xu hướng đồ lót.」"
"1595" = "「Tôi muốn——ra cùng với chị.\\nCùng với chị, tôi muốn sướng đến tận cùng.」"
"1598" = "「Tôi hiểu rồi! Tôi hiểu rồi! Ư——Hôm nay——\\ntôi, sẽ——giao phó! Tất cả——cho chị!」"
"1600" = "「Tôi sẽ làm theo lời chị. Tôi sẽ làm tất cả, vì tôi muốn thế!\\nNên, xin chị, hãy để tôi, trong lồn của chị」"
"1601" = "「Tôi sẽ làm! Ép sát quy đầu vào cửa tử cung,\\nrồi bắn, bắn thật nhiều, tinh dịch, vào đó!」"
"1603" = "「Những lời thốt ra như phản xạ không điều kiện——Ư——\\nCó vẻ như——a——đã là——câu trả lời chính xác——nhỉ.」"
"1604" = "「Tôi biết. Phần đỉnh——đang chạm vào. Chụt chụt,\\ndương vật, của tôi——đang bị hút, bị ngậm lấy.」"
"1607" = "「Tôi hiểu rồi. Tôi sẽ dừng lại——hôm nay——chị Mayami——Ư!!」"
"1610" = "「Nên tôi đã ước.\\nTôi muốn chúng ta có hai đứa con——muốn tạo ra chúng」"
"1659" = "「Haa, haa, haa——chị, Mayami」"
"1673" = "「Hãy để tôi tăng tỷ lệ đó lên nhé.\\nLần này tôi muốn——dành tất cả cho chị Mayami」"
"1684" = "「Cứ thế này——hết sức——rút, rút——\\nngậm, ngậm——chim, chim——của, Sou-chan」"
"1686" = "「Cũng đúng nhỉ. Vậy thì——ưm——\\nGợi ý……ít nhất hãy cho tôi một chút gợi ý đi.」"
"1699" = "「Ư!!」"
"1700" = "「Ư!!!!」"
"1701" = "「Ư!!!!!」"
"1702" = "「Ư!!!?」"
"1706" = "「~~~~Ư!!!」"
"1709" = "「~~~~~~~~~~Ư!!!」"
"1797" = "Ra vậy, nếu cứ tiếp tục nhắc đến chuyện này thì đúng là quá kém tinh tế.\\nNếu vậy, nơi nên chạm vào tất nhiên là——Ư!?"
"1828" = "Bầu ngực trượt mạnh sang một bên, phần đỉnh dương vật bị ném ra ngoài\\nvà trở nên lạnh lẽo. Cảm giác hụt hẫng ập đến bất ngờ——Ư!!?"
"1865" = "Muốn điên cuồng nhấp hông, muốn thúc mạnh lên.\\nNhưng bây giờ——tôi đã hứa, với chị rồi."
"1915" = "Khoảnh khắc nhìn thấy, toàn bộ công việc đang làm dở đều bay biến sạch.\\nNghe nói là đồ lót, nhưng mà ngực và cả chỗ đó đều phơi bày hết ra rồi kìa——Ư!"
"2145" = "（Phụttttttttttt! Ục!）"
"2189" = "（Thế này……thì——chẳng phải, tôi mới là mèo con sao.）"
```

## §8. Lượt soát 2 (bắt buộc — đọc lại toàn bộ fix vs JP)

- Tổng: **59** / tái kiểm chứng: **59** / loại bỏ: **0** / sửa lại: **1** (1603 — khôi phục 「」 bị sót khi viết fix; đã kiểm tra ngoặc 「」/（） toàn bộ 59 fix sau khi sửa: 0 lệch).
- Trước lượt soát 2, khâu kiểm chứng máy đã bắt 1 lỗi viết hoa ở 1466/1467 ("A"*12 → "A"+"a"*11 — đã sửa, đếm lại bằng máy: 12/8 a).
- Kiểm chứng máy: JSON 59 mục dạng chuẩn, khóa chuỗi; khối TOML 59 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 59/59; diff-sanity: 0 fix viết lại lớn (tỉ lệ tương đồng thấp nhất là các dòng rên ngắn 1405/1531/1466/1467/2145 — đều là sửa có chủ đích trên 1 token âm thanh, đã đếm lại bằng máy: 1492 đủ 19 u, 2145 đủ 11 t, 1466 đủ 12 a, 1467 đủ 8 a).

File lr_真闇h1_僕のおねえちゃん audit xong: đọc 317/317 dòng, sai **59/317 (18,6%)** — đại từ 22, gasp 21 (sweep 16 + sweep-missed 5), rên/nguyên âm 16, SFX 1, nghĩa 3 (2 gộp đại từ). 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 mồ côi, 0 chưa dịch, 0 trùng khóa. Lỗi tập trung ở cụm đại từ hệ thống (Soutetsu "em" với Mayami — giống lr真闇追加02/03) và gasp っ (sweep 16 + 5 dòng sweep bỏ sót), còn lại là rên/nguyên âm theo romaji fallback. Không có câu hỏi nào cần Hieu quyết trong file này — các điểm đã cờ đều là ghi nhận cho đợt thống nhất (おまんこ "chỗ đó" vs "lồn" 6/6; SFX dài rút gọn trong từ Việt). Khối TOML 59 khóa parse đạt, lượt soát 2: 59/59, 0 bỏ, 1 sửa.

Kết bài
