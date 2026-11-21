# Moan-fix — lr_真闇h1_僕のおねえちゃん.txt.toml (05_Mayami)

- File: `05_Mayami/lr_真闇h1_僕のおねえちゃん.txt.toml` (TOML-2: `lr_#U771f#U95c7h1_#U50d5#U306e#U304a#U306d#U3048#U3061#U3083#U3093.txt.toml`)
- Route: 05_Mayami. Cảnh H của Mayami — Mayami mặc đồ lót mới motif mèo đen khoe Soutetsu, trêu chọc rồi "dạy" em: oral, paizuri, quan hệ, xuất tinh trong.
- Đọc: **317/317 dòng** (keys 1163–2190), đọc từng dòng JP + TW + VN đối chiếu. CSV3 1 bộ duy nhất, key khớp tuyệt đối 317/317; VN khớp TOML ở 314/317 dòng, 3 dòng còn lại chỉ khác ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng (1464, 1598, 2029) — theo quy tắc, CSV3 là chuẩn cho fix list.
- TOML md5: `4baa00ccc02ca48bed882887b182d798` — không có bản trùng (chỉ 1 file lr_真闇h1_僕のおねえちゃん trong sources/toml2/). 0 tag `%l` trong file. File UTF-8 BOM + CRLF.
- Audit trước đó: 59 sai/317 (18,6%) — đại từ 22, gasp 21, rên/nguyên âm 16, SFX 1, nghĩa 3. Audit đã áp quy tắc romaji fallback + họ ひゃ-family (audit gần đây), nên đợt moan này là kiểm chứng nhẹ các giá trị rên của audit + tìm dòng audit bỏ sót.
- Cơ sở tổng (moan): **19 file / 468 dòng** (đọc trực tiếp từ dòng tổng của moans/ROUTE-MOANS.md lúc viết snippet).

## §1. Kiểm kê rên/SFX

- Xét **175 dòng rên/SFX/gasp** (112 dòng thoại chứa âm rên/thở/gasp/SFX + 63 dòng SFX trong ngoặc đơn độc thoại), trong đó:
  - 21 dòng gasp thuần (audit §2: 16 sweep + 5 sweep bỏ sót) — KHÔNG xét lại (Ư đã khóa).
  - 17 dòng rên/SFX audit đã sửa (16 moan + 1 SFX 2145) — kiểm chứng lại từng giá trị (xem §3).
  - Còn lại là các dòng rên/SFX giữ nguyên — kiểm chứng lại trong lúc đọc.
- **Đổi 7 dòng**: 3 đếm nguyên âm (1167, 1464, 2029), 2 romaji (1433, 1457), 2 thiếu âm rên (1598, 1816). Không có dòng romaji mới cho họ ひゃ/ひあ/きゃ (audit đã romaji đúng hết).

## §2. Chi tiết từng dòng sửa (7)

### 1167 [双鉄] — đếm nguyên âm

JP: 「――っ――はぁっ！　はぁっ！　はぁっ！！」
TW: 「——嗯——哈！　哈！　蛤啊！」
Cũ: 「——! Hà! Hà! Hà!!」
Mới: 「——! Haa! Haa! Haa!!」
→ はぁっ = 2 a/lần (は + ぁ kéo dài), VN cũ chỉ 1 a/lần. Cùng lỗi như 1659 mà audit đã sửa ("Haa, haa, haa") — audit bỏ sót dòng này. Phần đầu ――っ―― giữ nguyên "——!" theo quyết định audit §2 (っ đã diễn bằng "!").

### 1433 [双鉄] — romaji, sai nguyên âm trong fix audit (THAY THẾ giá trị audit)

JP: 「ふぅっっっ！！！！」
TW: 「呼嗚～～～！！！！」
Cũ: 「Fuuuu!!!!」
Mới: 「Fuu!!!!」
→ JP là ふぅ (ふ + ぅ nhỏ = "fuu", 2 u — đã xác minh bằng codepoint U+3045, không phải ぉ). VN cũ "Fuuuu" (4 u) sai số lượng; fix audit "Foo!!!!" sai NGUYÊN ÂM (o thay vì u). TW 呼嗚 xác nhận "uu". Giá trị moan này THAY THẾ fix audit 1433 ở đợt thống nhất (xem §5).

### 1457 [真闇] — romaji, một âm rên bị tách thành hai cách diễn

JP: 「う、ん……ふっ――ぁっ――んふふっ――双、ちゃん」
TW: 「唔，嗯……呼——啊——嗯呼呼——小、雙」
Cũ: 「Ư, m……phù——a——ưm fufu——Sou, chan」
Mới: 「Ư, m……phù——a——Nfufu——Sou, chan」
→ んふふっ là MỘT tiếng cười, VN cũ tách thành "ưm" + "fufu" (trộn Việt + romaji cho một âm duy nhất). Toàn file んふふっ đều diễn "Nfufu" (1423, 1517, 1527, 1542) — thống nhất theo đó. Phần ふっ→"phù" giữ nguyên theo quyết định audit §5 (tiếng thở Việt tự nhiên, không ngượng).

### 1464 [双鉄] — đếm nguyên âm

JP: 「ァァァっ――亀頭にっ――鈴口に――
さきっぽに舌を――入れようと――などっっ！！！」
TW: 「啊啊啊——我的龜頭——我的鈴口——舌頭——快進來了——！！！」
Cũ: 「Aaaa——vào quy đầu——vào lỗ sáo——
định đưa lưỡi——vào phần đỉnh——sao!!!」
Mới: 「Aaa——vào quy đầu——vào lỗ sáo——
định đưa lưỡi——vào phần đỉnh——sao!!!」
→ ァァァ = 3 a (đã đếm cơ học U+30A1 ×3), VN cũ "Aaaa" thừa 1 a. Audit không cờ dòng này.

### 1598 [双鉄] — thiếu âm rên (THAY THẾ giá trị audit — thêm "ha")

JP: 「わかった！　わかりましたっ！　っ――今日は――
僕、はっ――全部！　まかせる――おねえちゃんにっ！」
TW: 「我懂了！　我完全懂了！　——今天的——我——全部！　都交給你了——姐姐！」
Cũ: 「Em hiểu rồi! Em hiểu rồi! ——Hôm nay——
em, sẽ——giao phó! Tất cả——cho chị!」
Mới: 「Tôi hiểu rồi! Tôi hiểu rồi! Ư——Hôm nay——
tôi, ha——sẽ——giao phó! Tất cả——cho chị!」
→ Giá trị mới = giá trị fix audit + thêm "ha——" cho はっ (hơi thở ngắt câu giữa "僕、" và "全部！"). Audit bỏ mất âm này. Tiền lệ trong file: 1630 「真闇、姉、はっ――」→"Chị, Mayami, ha——" (audit giữ). Phần đại từ (em→tôi) và gasp (っ――→Ư——) là của audit, giữ nguyên trong giá trị này. Ở đợt thống nhất phải dùng giá trị moan này, KHÔNG dùng giá trị audit (xem §5).

### 1816 [monologue] — thiếu âm rên

JP: このタイミング舌がくっ――！！！！！！！
TW: 在這種時候的舌頭，嗚——！！！！！！！！！
Cũ: Lưỡi lại liếm vào lúc này——!!!!!!!
Mới: Lưỡi lại liếm vào lúc này——ku!!!!!!!
→ くっ―― là tiếng "kuh" bật ra cuối câu (ngạc nhiên/bực mình), VN cũ bỏ mất hẳn âm, chỉ còn dấu câu. Tiền lệ trong file: くっ đứng riêng đều diễn "Ku" (1434 くっ――ああっ→"Ku——aa", 1504 んっ――くっ――→"Ưm——ku——", 1479/1481 "ku"). TW có 嗚 tương ứng với âm này. Khác 1618/1649 (くっ―― giữa câu, ngập ngừng — audit giữ, dấu —— đã diễn độ ngập ngừng): ở đây くっ là cảm thán cuối dòng, không thể bỏ. Giữ nguyên 7 dấu ! theo JP (đã đếm cơ học ！×7).

### 2029 [monologue] — đếm nguyên âm

JP: 部屋に入ってきたその瞬間から勃起していた乳首を押せば、
真闇姉は発情しきったメス猫のような声を――ああ。
TW: 進入房間的那一瞬間，我按下她勃起的乳頭，真闇姐就發出像發情的母貓一樣的聲音——啊。
Cũ: Khi tôi ấn vào núm vú đã cương cứng từ khoảnh khắc bước vào phòng,
chị Mayami phát ra tiếng kêu như một con mèo cái đang động dục——a.
Mới: Khi tôi ấn vào núm vú đã cương cứng từ khoảnh khắc bước vào phòng,
chị Mayami phát ra tiếng kêu như một con mèo cái đang động dục——aa.
→ ああ cuối câu = 2 a (tiếng "ah" ngân dài khi độc thoại buông lơi), VN cũ chỉ 1 a. Phân biệt với 1832 (ああ, と理解がおいついてくる — thán từ nhận ra "à, hiểu rồi", diễn "a" là tự nhiên, giữ nguyên — xem §4).

## §3. Kiểm chứng 17 fix rên/SFX của audit — tất cả ĐÚNG, giữ nguyên

Đã đếm lại cơ học từng dòng (số nguyên âm trong fix so với JP):

- 1405 きゃっ→"Kya." ✓ (họ ひゃ → romaji).
- 1426 ファ――→"Faa" (2 a) ✓; あっっ→"a" ✓.
- 1436 ふ、ぁ→"fu, a" ✓ (sửa f→h).
- 1438 ひゃぐっ→"Hyagu!?" ✓ (giữ cả âm ぐ).
- 1466 12 a → "Aaaaaaaaaaaa" (12 a, đã đếm: ぁ×4 + あ×8) ✓.
- 1467 8 a → "Aaaaaaaa" (ぁ×6 + あ×2) ✓.
- 1470 3 a → "Aaa" ✓.
- 1471 あんっ→"An" ✓ (giữ ん).
- 1484 くあああっ→"Kuaaa" (3 a) ✓.
- 1488 くあっ→"Kua" (1 a) ✓.
- 1491 ふぉぉっ→"Foo" (2 o — JP ふぉぉ đã xác minh codepoint U+3049 ×2) ✓.
- 1492 きゅふううううううううううぅぅぅぅぅぅぅんっ→19 u → "Kyufuuuuuuuuuuuuuuuuuun" (19 u) ✓ + sửa "Kyuh"→"Kyuf" ✓.
- 1531 んふうううううっ (6 u) → "Nfuuuuuu" ✓.
- 1534 やっ→"Ya!?" ✓ (tiền lệ ポーレットh3 liệt kê cả やっ); んひゅっ→"Nhyu" ✓.
- 1659 はぁっ×3 → "Haa, haa, haa" (2 a/lần) ✓.
- 2145 (SFX) びゅぶううううううううう = 11 mora-u → 11 t "Phụttttttttttt" ✓.
- Ngoại lệ duy nhất: **1433** — fix audit "Foo" sai nguyên âm (xem §2, đã sửa thành "Fuu").

## §4. Giữ nguyên (không tính sai)

- **Họ ふぁ/ふあ đã romaji đúng**: ふぁっ→"Fua" (1428–1432, 1514 "fua" giữa dòng), はぁっ→"Haa" (1446 ×4, 1516, 1556), あ/ぁ đúng số lượng (1458–1463, 1468 6 a, 1469 5 a, 1472–1474), くあっ→"Kua" (1485, 1487, 1489, 1490), くはっ→"Kuha" (1486), はうっ→"Hau" (1449), んくっ→"Nku" (1532), んゆっ→"Nyu" (1533), んひゅ→"Nhyu" (1530, 1534), きゃんっ→"Kyan" (1407), にゃあん→"Nyaan" (1482), ぺろおお...→"Perooooooooo" 9 o khớp JP (1654), りゅううう→"ryuuuu" 4 u khớp JP (1481), ふぁんっ→"Fan" (1187), にゃぁ→"nyaa" (1173, mèo kêu).
- **Cười**: んふふっ→"Nfufu" (1423, 1517, 1527, 1542), うふふっ→"Ufufu" (1625) — tiếng cười, không phải rên.
- **んっ/うん/む → "Ưm/Ừm"**: 1182, 1407, 1441, 1454, 1455, 1499, 1502, 1504, 1510, 1512, 1514, 1516, 1537, 1539, 1540, 1541, 1556, 1642, 1664, 1689, 1693 — đều tự nhiên, giữ nguyên.
- **Tách âm theo JP**: ふ――ぁ→"Fu——a" (1425), ふっ――あっ→"fu——a" (1499, 1556), ふ、ぁ→"fu, a" (1436), う、ん→"Ư, m" (1457, 1506), は――く→"là——ku" (1425) — JP tách thì VN tách theo, không gộp.
- **SFX trong ngoặc đơn diễn bằng từ Việt** (quy ước file, audit §5 giữ): 2107–2190 (Siết chặt, Trượt dài, Phụt, Chụt, Nhào nặn, Ép chặt...) — chỉ 2145 sửa vì 32 t vượt xa mọi tiền lệ. Các dòng 1612, 1613, 1677, 2108, 2122, 2136, 2165–2167, 2170 tương tự.
- **Gasp đã diễn**: 1440 っ――→"ư" thường (giữ theo audit §2); 1167 đầu dòng ――っ――→"——!" (giữ theo audit §2); 1428/1503/1698 sweep already-rendered (xem §6).
- **っ nhấn mạnh/cụt cuối câu dính từ nội dung — không thêm Ư**: 1548 いいこっ, 1694 ならばっ, 1600 でっ, 1407 いきなりっ, 1640 真闇姉っ, 1645 精液っ, 1649/1618 くっ――/がっ―― giữa câu (dấu —— đã diễn độ ngập ngừng) — theo tiền lệ sweep 1474 + audit §2/§5.
- **1832** ああ→"a" (thán từ nhận ra, không phải âm rên kéo dài) — giữ, phân biệt với 2029 (âm "ah" ngân cuối độc thoại).
- **1543** んん→"Hửm", **1544** ん……しょ→"Hây……dô" (tiếng rặn tự nhiên) — giữ.
- **1561** びゅうびゅう→"Bắn thật nhiều" — diễn nghĩa mô tả trong thoại, không phải SFX ngoặc đơn; giữ theo quy ước audit §5 (không thống nhất trong đợt moan).
- **1457** ふっ→"phù" — tiếng thở Việt tự nhiên (chỉ đổi phần んふふっ sang "Nfufu", xem §2).

## §5. Cờ cho đợt thống nhất (2 cờ — cả 2 đều THAY THẾ giá trị audit)

### Cờ 1 — 1433: dùng giá trị moan "Fuu!!!!", KHÔNG dùng fix audit "Foo!!!!"

- JP ふぉっっっ (codepoints 0x3075 ふ + 0x3045 ぅ + っ×3) = "Fuu", không phải "Foo". Fix audit nhầm ぅ (u nhỏ) thành ぉ (o nhỏ). TW 呼嗚 xác nhận "uu". VN cũ "Fuuuu" (4 u) cũng sai số lượng. Giá trị đúng duy nhất: 「Fuu!!!!」.

### Cờ 2 — 1598: dùng giá trị moan (thêm "ha"), KHÔNG dùng giá trị audit

- Giá trị audit: 「Tôi hiểu rồi! Tôi hiểu rồi! Ư——Hôm nay——
tôi, sẽ——giao phó! Tất cả——cho chị!」 — bỏ mất はっ.
- Giá trị moan: 「Tôi hiểu rồi! Tôi hiểu rồi! Ư——Hôm nay——
tôi, ha——sẽ——giao phó! Tất cả——cho chị!」 — khôi phục はっ→"ha" (tiền lệ 1630). Phần đại từ + gasp của audit giữ nguyên trong giá trị moan.

## §6. Kiểm chứng sweep gasp

- Sweep có **20 mục** cho file này (đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`):
  - **16 mục audit đã áp nguyên, kiểm chứng đúng, không đụng lại**: 1163, 1495, 1496, 1497, 1519, 1575, 1607, 1699, 1700, 1701, 1702, 1706, 1709, 1797, 1828, 1915 (trong đó 1607 gộp với fix đại từ).
  - **4 mục already-rendered, kiểm chứng đúng, không sửa**: 1428 (んっ――ん～～～～っ → "Ưm——ưm~~~~!!"), 1503 (ん――っぁ――んっ……っ！！ → "Ưm——a——ưm……!!"), 1698 (ん～～～っ → "Ưm~~~"), 1803 (真闇姉は――っ！ → "chị Mayami——!" — っ diễn bằng "!").
- 5 dòng gasp sweep bỏ sót (1168, 1494, 1542, 1598, 1603) audit đã tìm và sửa — đều là Ư, không xét lại.
- Không có dòng "Kh" nào trong file bị đổi sang Ư. Không có dòng gasp Ư nào bị xem lại.

## §7. Lượt soát 2 (second pass)

- Đọc lại toàn bộ 7 giá trị fix so với JP + TW sau lượt đầu, kèm đếm cơ học lại: 1167 (はぁ×3 = 2 a/lần), 1433 (codepoint ふ+ぅ, TW 呼嗚), 1464 (ァ U+30A1 ×3), 1492/1466/1467/2145/1531/1484 (đếm lại các fix audit — đều đúng), 1816 (！×7 khớp VN), 2029 (ああ = 2 a).
- Tổng: 7 / tái kiểm chứng: 7 / bỏ: 0 / sửa: 0.

## §8. Khối TOML (parse-verified bằng tomllib: 7 khóa, 0 sai lệch giá trị so với wrong.json)

```toml
[script]
"1167" = "「——! Haa! Haa! Haa!!」"
"1433" = "「Fuu!!!!」"
"1457" = "「Ư, m……phù——a——Nfufu——Sou, chan」"
"1464" = "「Aaa——vào quy đầu——vào lỗ sáo——\\nđịnh đưa lưỡi——vào phần đỉnh——sao!!!」"
"1598" = "「Tôi hiểu rồi! Tôi hiểu rồi! Ư——Hôm nay——\\ntôi, ha——sẽ——giao phó! Tất cả——cho chị!」"
"1816" = "Lưỡi lại liếm vào lúc này——ku!!!!!!!"
"2029" = "Khi tôi ấn vào núm vú đã cương cứng từ khoảnh khắc bước vào phòng,\\nchị Mayami phát ra tiếng kêu như một con mèo cái đang động dục——aa."
```

Lưu ý: trong khối TOML trên, `\\n` là ký tự xuống dòng đã escape (giá trị thực trong JSON/TOML là `\n` literal như CSV3).

## Kết bài

File lr_真闇h1_僕のおねえちゃん: đã đọc 317/317 dòng, xét 175 dòng rên/SFX/gasp, đổi 7 dòng (1167 thiếu 1 a/lần ×3, 1433 fix audit sai nguyên âm "Foo"→"Fuu", 1457 "ưm fufu" trộn hai cách diễn→"Nfufu", 1464 thừa 1 a, 1598 fix audit bỏ mất hơi thở はっ→thêm "ha", 1816 bỏ mất tiếng "ku", 2029 thiếu 1 a) — audit file này đã áp romaji rất kỹ nên chỉ còn lỗi đếm/thiếu âm lẻ tẻ, không có dòng romaji mới cho họ ひゃ/きゃ. 2 cờ cho đợt thống nhất (1433 + 1598 đều thay thế giá trị audit). Không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào.
