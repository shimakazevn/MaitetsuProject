# Audit — lr_れいなh1_レディ・れいな.txt.toml (04_Reina)

- File: `04_Reina/lr_れいなh1_レディ・れいな.txt.toml` (TOML-2: `lr_#U308c#U3044#U306ah1_#U30ec#U30c7#U30a3#U30fb#U308c#U3044#U306a.txt.toml`)
- Route: 04_Reina. Nội dung: cảnh H của Reina ("Lady Reina") — Reina mặc đồ lót motif chó con, đóng vai cún ("Gâu gâu", gọi Soutetsu là chủ nhân), handjob ("o-te-te sex") rồi oral; sau đó Soutetsu bế bổng em lên làm tình trước gương, Reina tè dầm (omorrashi) vào thau rửa mặt dưới bàn trang điểm trong lúc vẫn đang được bế, rồi tiếp tục hiệp hai ở tư thế cũ.
- Đọc: **311/311 dòng** (keys 897–1914, section `script`: monologue 134, thoại Reina 106, thoại Soutetsu 71), đọc từng dòng JP + TW + VN đối chiếu. CSV3 1 set duy nhất, key khớp tuyệt đối 311/311; VN khớp TOML ở 154/311 dòng, 157 dòng còn lại chỉ khác ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng — theo quy tắc, CSV3 là chuẩn cho fix list.
- **Sai: 60/311 (19,3%)**.
- Phân loại: đại từ 5 (Soutetsu "tôi"→"anh" với Reina), gasp 8 (sweep, áp nguyên cả 8), rên/thở romaji 39 (họ fa/fu 24 + họ ひゃ/ひゅ/きゃ/きゅ 11 mới + cười 4 mới, có chồng lấn giữa các nhóm trong cùng dòng), nguyên âm 5, âm khác 3 (1279 っっ→ƯƯ, 1285 ぉっ→Ô, 1305 んぉっ→Ôm).
- **0 lệch dòng / 0 chuỗi xoay / 0 nhiễm chéo / 0 dòng mồ côi / 0 dòng chưa dịch / 0 khóa trùng.** JP/TW/VN khớp nhau ở mọi dòng đã đọc; không có VN nào là lời thoại của file khác. VN lặp ở nhiều key chỉ là SFX ngắn dùng chung (「Ư!!!」×2 — 1258 っ！！！ vs 1431 っ！！！, cùng âm gasp; 「Hya!」×n, 「Chu mút!」×n — cùng âm SFX). Chỉ 2 dòng VN==TW về dấu câu: không có dòng nào VN trống.
- TOML md5: `229a246bcd0ae55d389ed9f3493620b3` — không có bản trùng (chỉ 1 file lr_れいなh1_レディ・れいな trong sources/toml2/; không thuộc 11 nhóm trùng). `[selections]` rỗng ({}). `[characters]`: 1507 Reina, 1576 Soutetsu. 0 tag `%l` trong file (không có tag nào để sửa). File UTF-8 BOM + CRLF (642 dòng).
- Cơ sở tổng: **154 file / 6.891 dòng sai** (đã kiểm chứng trực tiếp với dòng tổng cuối của ROUTE-AUDIT.md — khớp đúng cơ sở task giao, không cần rebase).

## §1. Đại từ — Soutetsu "tôi"→"anh" với Reina, lỗi hệ thống (5 dòng — SỬA)

File dùng "tôi" cho Soutetsu ở 5 dòng thoại (1153 ×2, 1234, 1339 ×2, 1353, 1423), trong khi quy tắc đã khóa là "anh" với Reina (Reina gọi cậu "anh Soutetsu" xuyên suốt file — 1400, 1426, 1427...; tiền lệ đã merge: Reina gọi "anh Soutetsu", Soutetsu là "anh" với Reina). File KHÔNG nhất quán nội bộ: Soutetsu đã đúng là "anh" ở 1386 ("cứ để anh, lo!") và 1389 ("Anh sắp…… xuất tinh"). Toàn bộ thoại 双鉄 trong file chỉ nói với Reina (chỉ có 2 nhân vật lên tiếng), nên không có trường hợp người nghe khác cần phân biệt. Độc thoại Soutetsu dùng "tôi" xuyên suốt — đúng (ngôi kể), không sửa.

Giữ nguyên, không sửa: Reina gọi Soutetsu "anh Soutetsu" (ngôi 2, đúng); Soutetsu gọi Reina "em" (1153, 1423, 1346, 1389 — đúng); "em bé" (1144 — danh từ, không phải đại từ).

Các dòng sửa: 1153 (×2), 1234, 1339 (×2, cả sở hữu "của tôi"→"của anh"), 1353, 1423.

## §2. Gasp っ — sweep kiểm chứng, áp nguyên cả 8 fix

Sweep có **15 mục** cho file này (đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`): **8 fix áp nguyên** sau khi kiểm chứng từng giá trị vs JP (904 lost-gasp-trailing; 1258, 1282, 1431, 1432, 1433, 1434 lost-gasp-whole; 1440 lost-gasp-trailing — trong đó 1431/1432/1433/1434 là 4 dòng gasp liên tiếp của Soutetsu) và **5 already-rendered đã kiểm chứng đúng, không sửa**: 1271 (chuỗi SFX mút đã diễn bằng "Chu mút/Chụt/Liếm"), 1280/1281/1283 (っ！！！→"Ư!!!" đã có Ư), 1761 (静止す――っ→"khựng lại——ư!!!" đã có ư).

**2 mục needs-file-audit đã kiểm chứng, KHÔNG sửa**: 1597 (あがっ――っ！！！？ → "dâng trào lên——ư!!!?" — gasp đã diễn bằng ư sau ——; VN là bản dịch đầy đủ, khớp JP, không lệch dòng như sweep lo ngại) và 1790 (染め尽くした――っ！？ → "nhuộm đẫm……——ư!?" — tương tự, gasp đã diễn).

Quét máy bổ sung toàn bộ dòng JP chứa っ (**~120 dòng**): không tìm thêm gasp nào sweep bỏ sót ngoài 1279 (xem §4 — っっ chỉ còn 1 Ư).

## §3. Rên/thở — romaji fallback + quy tắc ひゃ-family + tiếng cười (39 dòng)

- **Quy tắc ひゃ-family 21/11 ~11:55** (moan loop, Hieu ủy quyền): trong cảnh H, ひゃ/ひゅ/ひあ/きゃ → romaji; "Á" cho chúng là lỗi mất phụ âm mora. Áp dụng: **1170** きゃあん→"Á a!"→"Kyaan!" (mất cả ky- lẫn ん; tiền lệ Mayami h1 1407 きゃんっ→"Kyan", 1482 にゃあん→"Nyaan"), **1306/1307** んひゅっ→"Nhyu" (tiền lệ Mayami h1 1530/1534 んひゅ→"Nhyu"), **1171** ひゅあっ→"Hyua", **1173** きゃふうううううっ→"Kyafuuuuuu" (kya+fu+6 u), **1174** ひゃううううんっ→"Hyauuuun", **1175/1176** ひゃうっ→"Hyau", **1177** ぴゃゃうっ→"Pyayau", **1303** んきゅううううううううっっ→"Nkyuuuuuuuuu" (9 u), **1304** んきゅうううううう→"Nkyuuuuuuu" (7 u) + やぁんっ→"Yaan", **1308** んきゅんっ→"Nkyun". Tất cả các dòng này cũ đều TRỘN romaji + Việt trong cùng một âm ("Ưm hya", "Hya ư", "Ưm kyu ư ư…") — vi phạm "một dòng = một cách diễn".
- **Họ fa/fu → romaji** (romaji fallback Hieu duyệt 21/11 ~01:56; áp dụng cho file chưa audit): ふぁ (1 mora "fa") cũ dịch "Phu a" tách 1 mora thành 2 âm tiết (1185, 1214 "Oa!" còn mất luôn phụ âm f, 1202, 1207, 1208, 1210, 1212, 1183 ふぁんっ→"Fan"); ふあ (2 morae "fu-a") cũ "Phu a" chuyển romaji "Fua" (1173, 1175, 1180, 1204, 1211, 1217, 1218); ふぇ (1 mora "fe") cũ "phu e" tách mora (1179, 1236 "Hả!?" mất luôn âm "fe") → "Fe"; ふえ (2 morae) → "Fue" (1201); ふやっ → "Fuya" (1215); ぷあっ → "Pua" (1218); はうっ → "Hau" (1231, tiền lệ hachirokuh3 giữ "Hau"), はうぅ → "Hauu" (1232); ふ、あっ nói lắp → "Fu, a!" giữ dấu phẩy (1424). Đếm nguyên âm đã kiểm chứng bằng máy cho từng token romaji (vd. 1203 ふあああああっ = fu+5 a → "Fuaaaaa"; 1212 ふぁああっ → "Faaa").
- **Tiếng cười là tiếng CƯỜI, không phải gasp** (quy tắc Hieu 19/11 22:05; tiền lệ h8: Fufu/Ufufu): **1197** うふふぅ→"Ufufuu~", **1257** んふふ～っ→"Nfufu~", **1299** んふふ～～→"Nfufu~~", **1328** うふふだ→"Ufufuu~" — cũ đều là "Ư phu phu~" gắn Ư gasp vào tiếng cười. **1298** là dòng khó nhất file: んふふ～、ほれひゃあ、ひひはひゅひょ～ (nói ngọng vì ngậm trong miệng) cũ dịch "Ư phu phu~, hế hày, ho há hứa ho~" diễn sai nguyên âm (ひ→o/á) và mất phụ âm hy- → romaji toàn dòng "Nfufu~, Horehyaa, Hihihahyuhyo~" (TW: 嗯呼呼～類個，好大！ xác nhận là nói ngọng "cái này, to quá").
- Đã romaji đúng, giữ nguyên: きゃあああ♪→"Kya a a♪" (1169), きゅっ→"Kyu!" (1183), やっ→"Ya!" (1304), ひゃっ→"Hya!" (nhiều dòng), くあっ→"Kua!!" (1277), くっ→"Ư!!!" xem §5.

## §4. Nguyên âm + âm khác (8 dòng)

- **Đếm nguyên âm sai** (công thức 1 + số う/ぅ; đếm lại bằng máy): **1244** ああ――→"Aa——" (cũ "A——" thiếu 1 a), **1284** ああ――→"Aa——", **1288** ぁあ→"Aa." (cũ "A."), **1584** ああ―― (thốt "à" nhận ra, độc thoại) →"Aa——", **1226** わぁあ (3 a) →"Oa a a!" (cũ "Oa!" chỉ 1 a; "Oa" = /wa/ trong tiếng Việt, giữ nguyên âm đầu). **1202** gộp: はぁっ/はぁ (2 a) →"haa" ×3 (cũ "ha"; tiền lệ Mayami h1 1659: はぁっ = 2 a/lần). **1207** gộp: あん→"An" (tiền lệ Mayami h1 1471). **1199** gộp: わぁああっ (4 a) →"Oa a a a".
- **1279** っっ！！！ = 2 gasp riêng → "ƯƯ!!!" (TW 嗚嗚; cũ "Ư!!!" chỉ 1 Ư — quy tắc đa-っ 1 Ư/1 っ, tiền lệ Mayami h1 1168).
- **1285** ぉっ――ぁっ → "Ô——a": ぉ (nguyên âm o) cũ dịch "Ư" đổi o→ư — khác ぁっ→"A" giữ nguyên âm a. **1305** んぉっ → "Ôm!?": giữ nguyên âm o + mũi; cũ "Ưm" mất nguyên âm o.

## §5. Giữ nguyên (không tính sai)

- **おまんこ "lồn" (2 dòng: 1150, 1736) vs "chỗ đó" (2 dòng: 1400, 1427)** — cả hai cách diễn đều có trong file với tỉ lệ 2/2, chỉ khác mức độ trực tiếp, không sai nghĩa. Không thống nhất trong audit; ghi nhận để đợt thống nhất xem xét (cùng câu hỏi như Mayami h1: "chỗ đó" 6 vs "lồn" 6).
- **Tiếng sủa/rên kiểu chó "Ư ử"** (1379 くーんくーん, 1381 きゅううん, 1436 きゅぅぅぅん) — Reina đóng vai cún, "Ư ử" là tiếng rên ư ử chuẩn trong tiếng Việt cho chó rên; giữ nguyên cả 3 dòng (khác họ ひゃ moan ở §3 vì đây là tiếng rên kiểu chó, không phải rên H).
- **っ cuối rên ngắn đã diễn bằng chữ cái La-tinh** (905 っ――あ――あっ→"Ư——a——a", 1242 ぁ――あっ→"A——a", 1247 ぁ……あっ→"A…… a——", 1252 ぁぁぁぁっ→"A a a a", 1301 ぁああああああああっっっ→"A a a a a a a a a!!!!", 1243 ぁ――うっ→"A——ư", 1228 はっ――ぁっ→"Hộc——a", 1238 あっ――→"A——") — giữ theo thực hành đã được parent kiểm chứng ở hachirokuh3 (giữ La-tinh, chỉ sửa sai phụ âm); mâu thuẫn với brief 20/11 ("thêm Ư" cho ああっ/はうっ) đã được cờ cho Hieu ở file đó, không quyết lại ở đây.
- **1225** くっ！！！→"Ư!!!" và **1312** く→"ư" — tiếng gằn く* diễn bằng Ư/ư (nguyên âm u được giữ, chỉ mất phụ âm k đầu tiếng gằn); TW 咕/啊 cũng đọc nhẹ. Giữ theo quy ước file (khác 1285/1305 là mất nguyên âm o).
- **1240** ふか、いっ→"sâu, quá" — いっ là mảnh vỡ của いい (tốt) bị cắt ngang; "sâu, quá" đọc được như "sâu quá" trong tiếng Việt; giữ (phán đoán, đã ghi nhận).
- **1185** しゅごっ→"to quá!" — しゅごっ là nói ngọng của すごっ (tuyệt quá); TW cũng diễn theo hướng kích thước (脹大了); giữ.
- **1224** ぷはぁ→"phù" — tiếng thở dài sau khi uống, diễn bằng tiếng Việt tự nhiên "phù", không ngượng; không ép romaji (tiền lệ Mayami h1 1457 ふっ→"phù").
- **1300/1310** んくっ→"Ực", ごきゅっ→"ực" — tiếng nuốt ực bằng tiếng Việt, giữ. **1395** ふっ→"phu", **1303** ふっ→"Phu" — tiếng thở "phu" đúng 1 âm tiết/1 mora, giữ.
- **SFX dài (chuỗi "t"/"m"/"e")** — đã đếm máy toàn bộ: 1160 (+1), 1161 (0), 1162 (+2), 1163 (+1), 1318 (+3), 1319 (0), 1344 (0), 1345 (0), 1866 (−2), 1869 (+3), 1894 (0), 1895 (−1), 1906 (−3), 1913 (−3), 1372 m×15 = お×15 khớp tuyệt đối, 1860 e×19 (18+1), 1302 ~×9 = ー×9 khớp tuyệt đối. Độ lệch −4..+3, không có outlier cực đoan (tiền lệ Mayami h1: chỉ sửa 2145 vì 32 t so với 11 mora) — giữ nguyên toàn bộ theo quy ước file.
- **SFX trong ngoặc đơn diễn bằng nghĩa** (1884 （ぽふっ）→（Chạm）, 1856 （ぐぐぐっっ！）→（Cương cứng!）, 1888 （きゅうううっ）→（Siết chặt）, 1908/1913/1914 （きゅっ/ぐりゅっ）→（Thắt/Siết chặt/Ngoáy）, 1871 （ちょろっ）→（Róc rách）, 1886 （くいっ）→（Rút ra）, 1889 （さすっ）→（Xoa xoa）, 1902 （ぞくっ）→（Sởn gai ốc）, 1885 （ぐいっ！）→（Bế lên!）) — quy ước file nhất quán, giữ.
- **1597/1790** sweep needs-file-audit — xem §2 (đã kiểm chứng, không sửa). **1271/1280/1281/1283/1761** sweep already-rendered — xem §2 (đã kiểm chứng, không sửa).
- **1286/1314** ああ→"Ừ" — ああ là lời đồng tình ("ừ"), diễn bằng nghĩa, giữ (khác 1244/1284/1584 giữ âm "A" thì sửa số lượng).
- **1405/1148/1361/1224** えへへ→"e he he~"/"Hì hì" — tiếng cười diễn bằng tiếng Việt, là tiếng cười (không phải gasp), giữ.
- **Thuật ngữ đã chốt: 0 lần xuất hiện** trong file (không có 御一夜/帝鉄/宮司/Migita/日ノ本/Seki/乗務鞄/乗員/電車姫/まいてつ/市電/整備体/KiHa/エアクラ/冥国/小畑/回数券/帝大/砂撒き/杜氏/義父/義母/義理). 投炭 (1569) dịch "xúc than", không có gloss %l nên không vào diện thống nhất.
- Các dòng chỉ khác TOML-2 làm phẳng `\n` (157 dòng) — không phải lỗi dịch, CSV3 là chuẩn.

## §6. Chi tiết từng dòng sai (60)
### 904 [双鉄] — gasp

JP: 「――っ」
TW: 「——」
Cũ: 「——」
Mới: 「——Ư」
→ Sweep lost-gasp-trailing áp nguyên: JP ――っ, VN chỉ còn —— → thêm Ư.

### 1153 [双鉄] — pronoun

JP: 「もっと、もっと強くしてほしい。僕はれいなで、\nれいなのお口で、まずは一回、思い切り射精したい」
TW: 「再，再用力一點。我想在玲奈裡面，玲奈的嘴巴裡面，先盡情地射一次」
Cũ: 「Mạnh hơn, tôi muốn em làm mạnh hơn nữa. Tôi muốn với Reina,\ntrước tiên là xuất tinh một lần thật thỏa thích vào miệng Reina.」
Mới: 「Mạnh hơn, anh muốn em làm mạnh hơn nữa. Anh muốn với Reina,\ntrước tiên là xuất tinh một lần thật thỏa thích vào miệng Reina.」
→ Soutetsu "tôi"→"anh" với Reina ×2 (quy tắc đã khóa; Reina gọi "anh Soutetsu"; thoại chỉ nói với Reina).

### 1170 [れいな] — moan

JP: 「きゃあん」
TW: 「呀啊！」
Cũ: 「Á a!」
Mới: 「Kyaan!」
→ Quy tắc ひゃ-family 21/11: きゃあん→romaji "Kyaan"; "Á a!" mất phụ âm ky- và mất ん (tiền lệ Mayami h1 1407 きゃんっ→"Kyan", 1482 にゃあん→"Nyaan").

### 1171 [れいな] — moan

JP: 「ひゅあっ！？　あっ！　あっ、あっ、しゅごっ、んっ、\nれいなの、おまたっ、にっ――そうてつさん、がぁっ」
TW: 「呀啊！啊！啊，啊，好舒服，嗯，玲奈的，小穴裡——雙鐵先生，在裡面」
Cũ: 「Hyu a!? A! A, a, tuyệt quá, ưm,\ntrong, chỗ đó của Reina——anh Soutetsu, đang——」
Mới: 「Hyua!? A! A, a, tuyệt quá, ưm,\ntrong, chỗ đó của Reina——anh Soutetsu, đang——」
→ ひゅあっ→"Hyua" một từ romaji (cũ "Hyu a" tách rời).

### 1173 [れいな] — moan

JP: 「きゃふうううううっ！？　ひゃっ！　ふあっ！！！\nおく！　おなか！　れいな、ごちゅんて、ごちゅんして」
TW: 「呀嗚——————！？呀啊！呼啊！！！裡面！　肚子！　玲奈，咕滋，咕滋地」
Cũ: 「Kya phu ư ư ư ư ư!? Hya! Phu a!!!\nBên trong! Bụng! Reina, bị đâm cạch cạch, bị đâm cạch cạch rồi」
Mới: 「Kyafuuuuuu!? Hya! Fua!!!\nBên trong! Bụng! Reina, bị đâm cạch cạch, bị đâm cạch cạch rồi」
→ Một dòng = một cách diễn (romaji fallback): きゃふうううううっ→"Kyafuuuuuu" (kya+fu+6 u), ふあっ→"Fua"; cũ trộn "Kya phu ư ư…" + "Phu a".

### 1174 [れいな] — moan

JP: 「ひゃううううんっ！」
TW: 「呀嗚嗚嗚嗚！」
Cũ: 「Hya ư ư ư ưn!」
Mới: 「Hyauuuun!」
→ ひゃううううんっ→"Hyauuuun" (hya+4 u+n); cũ trộn "Hya ư ư ư ưn" (romaji + Việt).

### 1175 [れいな] — moan

JP: 「ひゃうっ！　ふあっ！　でも、でもっ――れいな、\nそんなのっ――はずかっ――あっ――はずか、しっ、あ」
TW: 「呀嗚！呼啊！但是、但是——玲奈，這樣——好害羞——啊——害羞、啊」
Cũ: 「Hya ư! Phu a! Nhưng, nhưng mà——Reina,\nnhư thế——xấu hổ——a——xấu hổ, lắm, a」
Mới: 「Hyau! Fua! Nhưng, nhưng mà——Reina,\nnhư thế——xấu hổ——a——xấu hổ, lắm, a」
→ ひゃうっ→"Hyau", ふあっ→"Fua"; cũ trộn "Hya ư" + "Phu a".

### 1176 [れいな] — moan

JP: 「ひゃうっ！　ずるって――おなか――おまたぁっ――\nれいな！　ずるって――しゅごい！　ながぃぃいっ」
TW: 「呀嗚！滋溜地——肚子裡面——小穴——玲奈！　滋溜地——好厲害！　好長——」
Cũ: 「Hya ư! Trơn tuột——bụng——chỗ đó——\nReina! Trơn tuột——tuyệt quá! Dài quá đi~」
Mới: 「Hyau! Trơn tuột——bụng——chỗ đó——\nReina! Trơn tuột——tuyệt quá! Dài quá đi~」
→ ひゃうっ→"Hyau"; cũ "Hya ư" trộn romaji + Việt.

### 1177 [れいな] — moan

JP: 「ぴゃゃうっ！？」
TW: 「呀嗚！？」
Cũ: 「Pya ư!?」
Mới: 「Pyayau!?」
→ ぴゃゃうっ→"Pyayau" (pya-ya-u); cũ "Pya ư" trộn.

### 1179 [れいな] — moan

JP: 「ひゃっ！　あっ！　あ！　あ――ふぇっ――あっ――\nれいな――れいな――そうてつ、さん――おも、らし」
TW: 「呀！啊！啊！啊——呼哎——啊——玲奈——玲奈——雙鐵先生——要尿出來了」
Cũ: 「Hya! A! A! A——phu e——a——\nReina——Reina——anh Soutetsu——tè, dầm mất」
Mới: 「Hya! A! A! A——Fe——a——\nReina——Reina——anh Soutetsu——tè, dầm mất」
→ ふぇっ (1 mora "fe") → "Fe"; cũ "phu e" tách 1 mora thành 2 âm tiết.

### 1180 [れいな] — moan

JP: 「ひゃっ！　あっ！　おなかっ！　おくっ、もっ！\nごんごん、され、てっ――れいなっ――ふあっ！」
TW: 「呀！啊！肚子！！裡面，也！！緊繃繃，的——玲奈——呼啊！」
Cũ: 「Hya! A! Bụng! Bên trong, cũng!\nBị đâm cạch cạch, rồi——Reina——phu a!」
Mới: 「Hya! A! Bụng! Bên trong, cũng!\nBị đâm cạch cạch, rồi——Reina——Fua!」
→ ふあっ→"Fua" (romaji fallback họ fa/fu); cũ "Phu a".

### 1183 [れいな] — moan

JP: 「ひゃっ！　んっ！　きゅっ！　ふぁんっ！　も、もうっ、\nれいなっ！　れいな、おまたがっ！　いっぱい、でっ！」
TW: 「呀！嗯！嗚！哈嗯！玲、玲奈、已經！　玲奈的、小穴！　滿滿的，了」
Cũ: 「Hya! Ưm! Kyu! Phu a n! K-Không, chịu nổi nữa,\nReina! Reina, chỗ đó! Lấp đầy, mất rồi!」
Mới: 「Hya! Ưm! Kyu! Fan! K-Không, chịu nổi nữa,\nReina! Reina, chỗ đó! Lấp đầy, mất rồi!」
→ ふぁんっ (fa+n) → "Fan"; cũ "Phu a n" tách ふぁ thành 2 âm tiết.

### 1185 [れいな] — moan

JP: 「ひゃっ！？　びくって、そうてつさんの――しゅごっ！\nふぁっ――いっつもよりも――あちゅい、おっきいっっ」
TW: 「呀！？雙鐵先生的，脹大了——嗚！！呼啊——比平時更——更熱、更大！」
Cũ: 「Hya!? Giật giật rồi, của anh Soutetsu——to quá!\nPhu a——so với mọi khi——nóng hơn, bự hơn nữa~」
Mới: 「Hya!? Giật giật rồi, của anh Soutetsu——to quá!\nFa——so với mọi khi——nóng hơn, bự hơn nữa~」
→ ふぁっ→"Fa"; cũ "Phu a" tách 1 mora thành 2 âm tiết.

### 1197 [れいな] — moan

JP: 「うふふぅ。たっぷりぬれましたぁ。\nそうしたらぁ、お手々をきゅうくつな筒にして～」
TW: 「呵呵。已經整個濕透了啊。那就讓我的手圈成一個圓形～」
Cũ: 「Ư phu phu~. Ướt đẫm rồi nha~.\nVậy thì~, làm đôi tay thành một cái ống chật chội nào~」
Mới: 「Ufufuu~. Ướt đẫm rồi nha~.\nVậy thì~, làm đôi tay thành một cái ống chật chội nào~」
→ Cười うふふぅ là tiếng CƯỜI, không phải gasp: → "Ufufuu~" (tiền lệ h8: Fufu/Ufufu); cũ "Ư phu phu~" gắn Ư gasp.

### 1199 [れいな] — moan

JP: 「ふぇ？　わ！　――わぁああっ」
TW: 「呼哎？哇！——哇啊啊」
Cũ: 「Phu e? Oa! ——Oa a a」
Mới: 「Fe? Oa! ——Oa a a a」
→ ふぇ？→"Fe?"; わぁああっ (4 nguyên âm a) → "Oa a a a" (cũ "Oa a a" thiếu 1 a; "Oa" = /wa/ trong tiếng Việt, giữ nguyên).

### 1201 [れいな] — moan

JP: 「ふえっ？　えっ！？　そうてつさん、そうてつさぁん」
TW: 「呼哎？哎！雙鐵先生，雙鐵先生～」
Cũ: 「Phu e? Ơ!? Anh Soutetsu, anh Soutetsu ơi~」
Mới: 「Fue? Ơ!? Anh Soutetsu, anh Soutetsu ơi~」
→ ふえっ (fu-e, 2 morae) → "Fue"; cũ "Phu e" (đúng số âm tiết nhưng chuyển romaji theo fallback họ fa/fu).

### 1202 [れいな] — moan

JP: 「ふぁっ――はっ――はっ――はっ――\nふぁぁっ――はぁっ――はぁ――はぁ――」
TW: 「呼啊——哈——哈——哈——呼啊——哈——哈——哈——」
Cũ: 「Phu a——ha——ha——ha——\nphu a a——ha——ha——ha——」
Mới: 「Fa——ha——ha——ha——\nFaa——haa——haa——haa——」
→ ふぁっ→"Fa", ふぁぁっ→"Faa" (2 a); はぁっ/はぁ (2 a) → "haa" (cũ "ha" thiếu 1 a; tiền lệ Mayami h1 1659: はぁっ = 2 a/lần).

### 1203 [れいな] — moan

JP: 「ふぁ――あっ――ふあああああっ――」
TW: 「呼啊——啊——呼啊啊啊————」
Cũ: 「Phu a——a——phu a a a a a——」
Mới: 「Fa——a——Fuaaaaa——」
→ ふぁ――→"Fa"; ふあああああっ (fu+5 a) → "Fuaaaaa" (cũ "phu a a a a a" — đúng số âm tiết nhưng romaji fallback).

### 1204 [れいな] — moan

JP: 「ふあっ――あっっ――あっ――あっ――\nれいな――ンッ――なかに、いっぱいっ――ふぁっ」
TW: 「呼啊——啊——啊——啊————玲奈——嗯——裡面，滿滿的——呼啊」
Cũ: 「Phu a——a——a——a——\nReina——ưm——bên trong, lấp đầy rồi——phu a」
Mới: 「Fua——a——a——a——\nReina——ưm——bên trong, lấp đầy rồi——Fua」
→ ふあっ→"Fua" ×2 (đầu + cuối dòng); cũ "Phu a".

### 1207 [れいな] — moan

JP: 「ふぁっ――あっ！　あん！　だからぁ、そうてつさぁん。\nもっと――もっと――ゆっくり――ゆっくりぃ」
TW: 「呼啊——啊！啊嗯！所以呢，雙鐵先生～再——再——慢點——慢慢來」
Cũ: 「Phu a——a! A! Cho nên là~, anh Soutetsu ơi~.\nNữa——nữa đi——chậm thôi——chậm thô~i」
Mới: 「Fa——a! An! Cho nên là~, anh Soutetsu ơi~.\nNữa——nữa đi——chậm thôi——chậm thô~i」
→ ふぁっ→"Fa"; あん (a+n) → "An" (cũ "A!" mất ん; tiền lệ Mayami h1 1471 あんっ→"An").

### 1208 [れいな] — moan

JP: 「ふぁっ――れいな――やぁっ――れいな――\nおもらし――れいな、してる――みえてる、おもらし」
TW: 「呼啊——玲奈——呀——玲奈————尿尿了——玲奈、尿尿了——看見了——尿尿」
Cũ: 「Phu a——Reina——a——Reina——\ntè dầm——Reina, đang tè dầm——thấy rồi, tè dầm」
Mới: 「Fa——Reina——Yaa——Reina——\ntè dầm——Reina, đang tè dầm——thấy rồi, tè dầm」
→ ふぁっ→"Fa"; やぁっ (ya-a) → "Yaa" (cũ "a" mất phụ âm y; tiền lệ 1304 やっ→"Ya!").

### 1210 [れいな] — moan

JP: 「ふぁ……あ……あっ――ふぁあ」
TW: 「呼啊……啊……啊——呼啊」
Cũ: 「Phu a…… a…… a——phu a」
Mới: 「Fa…… a…… a——Faa」
→ ふぁ→"Fa"; ふぁあ (fa+a) → "Faa".

### 1211 [れいな] — moan

JP: 「ふあっ」
TW: 「呼啊」
Cũ: 「Phu a」
Mới: 「Fua」
→ ふあっ (fu-a) → "Fua"; cũ "Phu a" tách 2 morae thành "Phu a" — chuyển romaji theo fallback.

### 1212 [れいな] — moan

JP: 「ふぁああっ！　んっ！　れいなっ！　ふぁっ！　あっ！\nおなかっ！　おなかぁっ！　ぐって！　ふぁ、あんっ！」
TW: 「呼啊啊！嗯！玲奈！呼啊！！啊！肚子！！　肚子裡面！！　被頂到了！　呼啊，啊嗯！」
Cũ: 「Phu a a a! Ưm! Reina! Phu a! A!\nBụng! Bụng! Bị đâm! Phu, a n!」
Mới: 「Faaa! Ưm! Reina! Fa! A!\nBụng! Bụng! Bị đâm! Fa, an!」
→ ふぁああっ (fa+2 a) → "Faaa"; ふぁっ→"Fa"; ふぁ、あんっ→"Fa, an!" (giữ dấu phẩy + ん).

### 1214 [れいな] — moan

JP: 「ふぁ！　えへっ――えへへぇ」
TW: 「呼啊！哎嘿——哎嘿嘿」
Cũ: 「Oa! Hì hì——hì hì hì~」
Mới: 「Fa! Hì hì——hì hì hì~」
→ ふぁ！→"Fa!"; cũ "Oa!" mất phụ âm f ("Oa" = /wa/).

### 1215 [れいな] — moan

JP: 「ふやっ！　あっ！　あっ！　あっ！　あっ！！！\nおくっ！　おくっ！　んっ、んううっ、きもち、いいっ」
TW: 「呼啊！啊！啊！啊！啊！！！裡面！　裡面！　嗯、嗯嗚、好舒、服！」
Cũ: 「Phu ya! A! A! A! A!!!\nBên trong! Bên trong! Ưm, ưm ư, sướng, quá đi」
Mới: 「Fuya! A! A! A! A!!!\nBên trong! Bên trong! Ưm, ưm ư, sướng, quá đi」
→ ふやっ (fu-ya) → "Fuya"; cũ "Phu ya" (đúng số âm tiết nhưng romaji fallback; thuật ngữ "phuya" cũng là 1 từ, không tách).

### 1217 [れいな] — moan

JP: 「ふあっ！　あっ！　あっ――ああっ！！！」
TW: 「呼啊！啊！啊，——啊！！」
Cũ: 「Phu a! A! A——a a!!!」
Mới: 「Fua! A! A——a a!!!」
→ ふあっ→"Fua"; cũ "Phu a".

### 1218 [れいな] — moan

JP: 「ぷあっ！！？　ふあっ――あっ――あっ――おなかっ\n――いき――ぜんぶ、でちゃうっ――ふあっ！　あっ！」
TW: 「呼啊！！？呼啊——啊——啊——肚子裡——要來了——全部，要出來了——呼啊！　啊！
Cũ: 「Phu a!!? Phu a——a——a——bụng——\nra——ra hết, mất thôi——phu a! A!」
Mới: 「Pua!? Fua——a——a——bụng——\nra——ra hết, mất thôi——Fua! A!」
→ ぷあっ (pu-a) → "Pua"; ふあっ→"Fua" ×2; cũ "Phu a".

### 1226 [れいな] — vowel

JP: 「わぁあ！　とっても元気ですねぇ」
TW: 「哇啊！真的好有精神哦」
Cũ: 「Oa! Cậu bé thật là sung sức quá đi~」
Mới: 「Oa a a! Cậu bé thật là sung sức quá đi~」
→ わぁあ (wa+2 a = 3 nguyên âm a) → "Oa a a"; cũ "Oa!" chỉ 1 a ("Oa" = /wa/).

### 1231 [れいな] — moan

JP: 「はうっ――かがみ――\nれいな、れいなのかがみには――」
TW: 「哈嗚——鏡子裡——玲奈，玲奈在鏡子裡——」
Cũ: 「Ha ư——gương——\nReina, trong gương của Reina thì——」
Mới: 「Hau——gương——\nReina, trong gương của Reina thì——」
→ はうっ→"Hau" một từ romaji (tiền lệ hachirokuh3 giữ "Hau"); cũ "Ha ư" trộn.

### 1232 [れいな] — moan

JP: 「はうぅ～～……。\nれいな……れいなぁ」
TW: 「哈嗚嗚～～……玲奈……玲奈啊」
Cũ: 「Ha ư ư~~……\nReina…… Reina á~」
Mới: 「Hauu~~……\nReina…… Reina á~」
→ はうぅ (ha+2 u) → "Hauu"; cũ "Ha ư ư" trộn.

### 1234 [双鉄] — pronoun

JP: 「ふむ――ならば、僕がご主人さまでよいのか？」
TW: 「唔——那麼，我就是主人了對嗎？」
Cũ: 「Hừm——Vậy thì, tôi làm chủ nhân có được không?」
Mới: 「Hừm——Vậy thì, anh làm chủ nhân có được không?」
→ Soutetsu "tôi"→"anh" với Reina (quy tắc đã khóa).

### 1236 [れいな] — moan

JP: 「ふぇっ！？　あの、そおてつさん……これじゃれいな、\nぎゅっーってするとこないですよぉ」
TW: 「唔哎！？那個，雙鐵先生……像這樣子，玲奈，沒辦法抱緊緊哦！」
Cũ: 「Hả!? Dạ, anh Soutetsu…… thế này thì Reina,\nkhông có chỗ nào để ôm chặt anh đâu ạ~」
Mới: 「Fe!? Dạ, anh Soutetsu…… thế này thì Reina,\nkhông có chỗ nào để ôm chặt anh đâu ạ~」
→ ふぇっ→"Fe!?"; cũ "Hả!?" mất hoàn toàn âm "fe" (chỉ còn nghĩa ngạc nhiên).

### 1244 [双鉄] — vowel

JP: 「ああ――気持ちいい……気持ちいい」
TW: 「啊——好舒服……好舒服」
Cũ: 「A——sướng quá…… sướng quá.」
Mới: 「Aa——sướng quá…… sướng quá.」
→ ああ―― (2 a) → "Aa——"; cũ "A——" thiếu 1 a.

### 1257 [れいな] — moan

JP: 「あ！　そうてつさん、先っぽからよだれ垂らしてますぅ。\nんふふ～っ、がまんしきれないんですねぇ」
TW: 「啊！雙鐵先生，你前面流口水了哦。嗯呵呵～看來已經受不了了」
Cũ: 「A! Anh Soutetsu, ở phần đỉnh đang chảy nước dãi kìa~.\nƯ phu phu~, anh không chịu nổi nữa rồi nhỉ~」
Mới: 「A! Anh Soutetsu, ở phần đỉnh đang chảy nước dãi kìa~.\nNfufu~, anh không chịu nổi nữa rồi nhỉ~」
→ Cười んふふ～っ là tiếng CƯỜI → "Nfufu~"; cũ "Ư phu phu~" gắn Ư gasp.

### 1258 [双鉄] — gasp

JP: 「っ！！！」
TW: 「啊！！！」
Cũ: 「!!!」
Mới: 「Ư!!!」
→ Sweep lost-gasp-whole áp nguyên: JP っ！！！, VN chỉ còn !!! → thêm Ư.

### 1279 [双鉄] — sound

JP: 「っっ！！！」
TW: 「嗚嗚！！！」
Cũ: 「Ư!!!」
Mới: 「ƯƯ!!!」
→ っっ！！！ = 2 gasp riêng → 2 Ư (TW 嗚嗚); cũ "Ư!!!" chỉ 1 Ư (quy tắc đa-っ: 1 Ư/1 っ; tiền lệ Mayami h1 1168).

### 1282 [双鉄] — gasp

JP: 「っ！！！！」
TW: 「嗚！！！！」
Cũ: 「!!!!」
Mới: 「Ư!!!!」
→ Sweep lost-gasp-whole áp nguyên: JP っ！！！！, VN chỉ còn !!!! → thêm Ư.

### 1284 [双鉄] — vowel

JP: 「ああ――」
TW: 「嗯——」
Cũ: 「A——」
Mới: 「Aa——」
→ ああ―― (2 a) → "Aa——"; cũ "A——" thiếu 1 a.

### 1285 [双鉄] — sound

JP: 「ぉっ――ぁっ」
TW: 「嗯——啊」
Cũ: 「Ư——a」
Mới: 「Ô——a」
→ ぉっ (nguyên âm o + っ) → "Ô"; cũ "Ư" đổi nguyên âm o→ư (khác ぁっ→"A" giữ nguyên âm a).

### 1288 [双鉄] — vowel

JP: 「ぁあ」
TW: 「嗯」
Cũ: 「A.」
Mới: 「Aa.」
→ ぁあ (2 a) → "Aa."; cũ "A." thiếu 1 a.

### 1298 [れいな] — moan

JP: 「んふふ～、ほれひゃあ、ひひはひゅひょ～」
TW: 「嗯呼呼～類個，好大！」
Cũ: 「Ư phu phu~, hế hày, ho há hứa ho~」
Mới: 「Nfufu~, Horehyaa, Hihihahyuhyo~」
→ Một dòng = một cách diễn (romaji): んふふ～→"Nfufu~" (cười), ほれひゃあ→"Horehyaa", ひひはひゅひょ～→"Hihihahyuhyo~"; cũ "Ư phu phu~, hế hày, ho há hứa ho~" diễn sai nguyên âm (ひ→o/á) và mất phụ âm hy-.

### 1299 [れいな] — moan

JP: 「んふふ～～」
TW: 「嗯呼呼～～」
Cũ: 「Ư phu phu~~」
Mới: 「Nfufu~~」
→ Cười んふふ～～ là tiếng CƯỜI → "Nfufu~~"; cũ "Ư phu phu~~" gắn Ư gasp.

### 1303 [れいな] — moan

JP: 「んきゅううううううううっっ！　ま、まって、\nまって、そうてつさぁん！　ふっ、れいな、はやくてっ」
TW: 「嗯嗚————————！等、等等，等等，雙鐵先生！　呼，玲奈，快要」
Cũ: 「Ưm kyu ư ư ư ư ư ư ư ư! K-Khoan đã,\nkhoan đã, anh Soutetsu ơi~! Phu, Reina, nhanh quá」
Mới: 「Nkyuuuuuuuuu! K-Khoan đã,\nkhoan đã, anh Soutetsu ơi~! Phu, Reina, nhanh quá」
→ んきゅううううううううっっ (n+kyu+8 u) → "Nkyuuuuuuuuu" (9 u); cũ trộn "Ưm kyu ư ư…".

### 1304 [れいな] — moan

JP: 「んきゅうううううう！　ひゃっ！　やっ！　やぁんっ、\nおまたっ！　おなかっ――れいなっ――おされてっ！！」
TW: 「嗯嗚嗚嗚嗚！咿呀！呀！不要，小穴！　玲奈的——肚子——被按著！！」
Cũ: 「Ưm kyu ư ư ư ư ư ư! Hya! Ya! Ya a,\nchỗ đó! Bụng——Reina——bị ấn vào!!」
Mới: 「Nkyuuuuuuu! Hya! Ya! Yaan,\nchỗ đó! Bụng——Reina——bị ấn vào!!」
→ んきゅうううううう (n+kyu+6 u) → "Nkyuuuuuuu" (7 u); やぁんっ→"Yaan" (giữ ん); cũ trộn "Ưm kyu ư ư…" + "Ya a" mất ん.

### 1305 [双鉄] — sound

JP: 「んぉっ！？」
TW: 「嗯嗚！」
Cũ: 「Ưm!?」
Mới: 「Ôm!?」
→ んぉっ (n+o+っ) → "Ôm" (giữ nguyên âm o + mũi); cũ "Ưm" mất nguyên âm o.

### 1306 [れいな] — moan

JP: 「んひゅっ！　はっ、あっ――そうてつ、さぁん――んっ。\nゆっくり、もっと、もっと――ゆっくりぃ――」
TW: 「嗯嗚！哈、啊——雙鐵、少爺——嗯。慢點，再，再——再慢點——」
Cũ: 「Ưm hya! Ha, a——anh Soutetsu, ơi~——ưm.\nChậm thôi, nữa, nữa đi——chậm thô~i——」
Mới: 「Nhyu! Ha, a——anh Soutetsu, ơi~——ưm.\nChậm thôi, nữa, nữa đi——chậm thô~i——」
→ んひゅっ→"Nhyu" (quy tắc ひゃ-family: んひゅ→Nhyu); cũ trộn "Ưm hya".

### 1307 [れいな] — moan

JP: 「んひゅっ！！！」
TW: 「嗯嗚！！」
Cũ: 「Ưm hyu!!!」
Mới: 「Nhyu!!!」
→ んひゅっ→"Nhyu"; cũ "Ưm hyu" trộn.

### 1308 [れいな] — moan

JP: 「んきゅんっ！！！」
TW: 「嗯嗚！！！」
Cũ: 「Ưm kyun!!!」
Mới: 「Nkyun!!!」
→ んきゅんっ (n+kyu+n) → "Nkyun"; cũ "Ưm kyun" trộn.

### 1328 [れいな] — moan

JP: 「はぁい。うふふぅ。\nれいな、おててせっくすもだいすきですよぉ」
TW: 「好的。嗚呼呼。玲奈，也很喜歡用小手手做愛」
Cũ: 「Vâng ạ~. Ư phu phu~.\nReina cũng thích làm tình bằng tay lắm đó nha~」
Mới: 「Vâng ạ~. Ufufuu~.\nReina cũng thích làm tình bằng tay lắm đó nha~」
→ Cười うふふぅ là tiếng CƯỜI → "Ufufuu~"; cũ "Ư phu phu~" gắn Ư gasp.

### 1339 [双鉄] — pronoun

JP: 「気持ちはいいが、ものたりなくある。もっと強く、\n僕はれいなに、僕の勃起を可愛がってもらいたい」
TW: 「感覺很舒服，但是還不夠。再用力點，我希望玲奈快點疼愛我的勃起」
Cũ: 「Cảm giác rất tuyệt, nhưng vẫn chưa đủ. Mạnh hơn nữa đi,\ntôi muốn Reina yêu chiều sự cương cứng của tôi.」
Mới: 「Cảm giác rất tuyệt, nhưng vẫn chưa đủ. Mạnh hơn nữa đi,\nanh muốn Reina yêu chiều sự cương cứng của anh.」
→ Soutetsu "tôi"→"anh" với Reina ×2 (cả tự xưng lẫn sở hữu "của tôi"→"của anh").

### 1353 [双鉄] — pronoun

JP: 「ここから先はセックスだ。セックスならば子犬ではなく、\nれいなと、僕は、したいと望む」
TW: 「接下來我們要做愛了。要做愛的話，那就不是我跟小狗，而是玲奈和我想要做。
Cũ: 「Từ đây trở đi là làm tình rồi. Nếu là làm tình thì không phải với cún con,\nmà là với Reina, tôi muốn làm tình cùng em.」
Mới: 「Từ đây trở đi là làm tình rồi. Nếu là làm tình thì không phải với cún con,\nmà là với Reina, anh muốn làm tình cùng em.」
→ Soutetsu "tôi"→"anh" với Reina (quy tắc đã khóa).

### 1423 [双鉄] — pronoun

JP: 「であらばれいな――\nまずは、おててセックスから願いたい」
TW: 「那麼，玲奈——首先，麻煩你用小手吧」
Cũ: 「Nếu vậy thì Reina——\nTrước tiên, tôi muốn nhờ em làm tình bằng tay.」
Mới: 「Nếu vậy thì Reina——\nTrước tiên, anh muốn nhờ em làm tình bằng tay.」
→ Soutetsu "tôi"→"anh" với Reina (quy tắc đã khóa).

### 1424 [れいな] — moan

JP: 「そぉてつ、さん、が――あっ――こんと、ろーる――\nふ、あっ！　れいな――れいなの――おもらし、をっ」
TW: 「雙鐵、先生、幫玲奈——啊——控、制——呼，啊！　玲奈——玲奈——尿尿」
Cũ: 「Anh Soutetsu, sẽ——a——kiểm, soát——\nphu, a! Reina——việc tè dầm——của Reina, sao」
Mới: 「Anh Soutetsu, sẽ——a——kiểm, soát——\nFu, a! Reina——việc tè dầm——của Reina, sao」
→ ふ、あっ (fu, a — nói lắp) → "Fu, a!" (giữ dấu phẩy); cũ "phu, a!" — chuyển romaji theo fallback họ fa/fu.

### 1431 [双鉄] — gasp

JP: 「っ！！！」
TW: 「！！！」
Cũ: 「!!!」
Mới: 「Ư!!!」
→ Sweep lost-gasp-whole áp nguyên: JP っ！！！, VN chỉ còn !!! → thêm Ư.

### 1432 [双鉄] — gasp

JP: 「っ！！！！」
TW: 「！！！！」
Cũ: 「!!!!」
Mới: 「Ư!!!!」
→ Sweep lost-gasp-whole áp nguyên: JP っ！！！！, VN chỉ còn !!!! → thêm Ư.

### 1433 [双鉄] — gasp

JP: 「っ！！！！！！」
TW: 「！！！！！！」
Cũ: 「!!!!!!」
Mới: 「Ư!!!!!!」
→ Sweep lost-gasp-whole áp nguyên: JP っ！！！！！！, VN chỉ còn !!!!!! → thêm Ư.

### 1434 [双鉄] — gasp

JP: 「っ！？」
TW: 「！？」
Cũ: 「!?」
Mới: 「Ư!?」
→ Sweep lost-gasp-whole áp nguyên: JP っ！？, VN chỉ còn !? → thêm Ư.

### 1440 [れいな] — gasp

JP: 「～～～～～～～～～～～～～～っ！！！！」
TW: 「～～～～～～～～～～～～～～嗚！！！！」
Cũ: 「~~~~~~~~~~~~~~!!!!」
Mới: 「~~~~~~~~~~~~~~Ư!!!!」
→ Sweep lost-gasp-trailing áp nguyên: JP ～×14+っ！！！！, VN giữ ~ nhưng mất gasp → thêm Ư sau ~.

### 1584 [monologue] — vowel

JP: ああ――そうだ。れいなはレディで。\nレディであると同時に深く……女であるのだ。
TW: 嗯——是啊。玲奈是個淑女。既是淑女，同時又深刻地……是個女人。
Cũ: A——đúng rồi. Reina là một quý cô.\nĐồng thời với việc là một quý cô, em ấy cũng sâu sắc là một…… người phụ nữ.
Mới: Aa——đúng rồi. Reina là một quý cô.\nĐồng thời với việc là một quý cô, em ấy cũng sâu sắc là một…… người phụ nữ.
→ ああ―― (2 a, thốt "à" nhận ra) → "Aa——"; cũ "A——" thiếu 1 a.

## Khối TOML đã kiểm chứng parse (60 khóa, 0 sai lệch giá trị)

```toml
[script]
"904" = "「——Ư」"
"1153" = "「Mạnh hơn, anh muốn em làm mạnh hơn nữa. Anh muốn với Reina,\\ntrước tiên là xuất tinh một lần thật thỏa thích vào miệng Reina.」"
"1170" = "「Kyaan!」"
"1171" = "「Hyua!? A! A, a, tuyệt quá, ưm,\\ntrong, chỗ đó của Reina——anh Soutetsu, đang——」"
"1173" = "「Kyafuuuuuu!? Hya! Fua!!!\\nBên trong! Bụng! Reina, bị đâm cạch cạch, bị đâm cạch cạch rồi」"
"1174" = "「Hyauuuun!」"
"1175" = "「Hyau! Fua! Nhưng, nhưng mà——Reina,\\nnhư thế——xấu hổ——a——xấu hổ, lắm, a」"
"1176" = "「Hyau! Trơn tuột——bụng——chỗ đó——\\nReina! Trơn tuột——tuyệt quá! Dài quá đi~」"
"1177" = "「Pyayau!?」"
"1179" = "「Hya! A! A! A——Fe——a——\\nReina——Reina——anh Soutetsu——tè, dầm mất」"
"1180" = "「Hya! A! Bụng! Bên trong, cũng!\\nBị đâm cạch cạch, rồi——Reina——Fua!」"
"1183" = "「Hya! Ưm! Kyu! Fan! K-Không, chịu nổi nữa,\\nReina! Reina, chỗ đó! Lấp đầy, mất rồi!」"
"1185" = "「Hya!? Giật giật rồi, của anh Soutetsu——to quá!\\nFa——so với mọi khi——nóng hơn, bự hơn nữa~」"
"1197" = "「Ufufuu~. Ướt đẫm rồi nha~.\\nVậy thì~, làm đôi tay thành một cái ống chật chội nào~」"
"1199" = "「Fe? Oa! ——Oa a a a」"
"1201" = "「Fue? Ơ!? Anh Soutetsu, anh Soutetsu ơi~」"
"1202" = "「Fa——ha——ha——ha——\\nFaa——haa——haa——haa——」"
"1203" = "「Fa——a——Fuaaaaa——」"
"1204" = "「Fua——a——a——a——\\nReina——ưm——bên trong, lấp đầy rồi——Fua」"
"1207" = "「Fa——a! An! Cho nên là~, anh Soutetsu ơi~.\\nNữa——nữa đi——chậm thôi——chậm thô~i」"
"1208" = "「Fa——Reina——Yaa——Reina——\\ntè dầm——Reina, đang tè dầm——thấy rồi, tè dầm」"
"1210" = "「Fa…… a…… a——Faa」"
"1211" = "「Fua」"
"1212" = "「Faaa! Ưm! Reina! Fa! A!\\nBụng! Bụng! Bị đâm! Fa, an!」"
"1214" = "「Fa! Hì hì——hì hì hì~」"
"1215" = "「Fuya! A! A! A! A!!!\\nBên trong! Bên trong! Ưm, ưm ư, sướng, quá đi」"
"1217" = "「Fua! A! A——a a!!!」"
"1218" = "「Pua!? Fua——a——a——bụng——\\nra——ra hết, mất thôi——Fua! A!」"
"1226" = "「Oa a a! Cậu bé thật là sung sức quá đi~」"
"1231" = "「Hau——gương——\\nReina, trong gương của Reina thì——」"
"1232" = "「Hauu~~……\\nReina…… Reina á~」"
"1234" = "「Hừm——Vậy thì, anh làm chủ nhân có được không?」"
"1236" = "「Fe!? Dạ, anh Soutetsu…… thế này thì Reina,\\nkhông có chỗ nào để ôm chặt anh đâu ạ~」"
"1244" = "「Aa——sướng quá…… sướng quá.」"
"1257" = "「A! Anh Soutetsu, ở phần đỉnh đang chảy nước dãi kìa~.\\nNfufu~, anh không chịu nổi nữa rồi nhỉ~」"
"1258" = "「Ư!!!」"
"1279" = "「ƯƯ!!!」"
"1282" = "「Ư!!!!」"
"1284" = "「Aa——」"
"1285" = "「Ô——a」"
"1288" = "「Aa.」"
"1298" = "「Nfufu~, Horehyaa, Hihihahyuhyo~」"
"1299" = "「Nfufu~~」"
"1303" = "「Nkyuuuuuuuuu! K-Khoan đã,\\nkhoan đã, anh Soutetsu ơi~! Phu, Reina, nhanh quá」"
"1304" = "「Nkyuuuuuuu! Hya! Ya! Yaan,\\nchỗ đó! Bụng——Reina——bị ấn vào!!」"
"1305" = "「Ôm!?」"
"1306" = "「Nhyu! Ha, a——anh Soutetsu, ơi~——ưm.\\nChậm thôi, nữa, nữa đi——chậm thô~i——」"
"1307" = "「Nhyu!!!」"
"1308" = "「Nkyun!!!」"
"1328" = "「Vâng ạ~. Ufufuu~.\\nReina cũng thích làm tình bằng tay lắm đó nha~」"
"1339" = "「Cảm giác rất tuyệt, nhưng vẫn chưa đủ. Mạnh hơn nữa đi,\\nanh muốn Reina yêu chiều sự cương cứng của anh.」"
"1353" = "「Từ đây trở đi là làm tình rồi. Nếu là làm tình thì không phải với cún con,\\nmà là với Reina, anh muốn làm tình cùng em.」"
"1423" = "「Nếu vậy thì Reina——\\nTrước tiên, anh muốn nhờ em làm tình bằng tay.」"
"1424" = "「Anh Soutetsu, sẽ——a——kiểm, soát——\\nFu, a! Reina——việc tè dầm——của Reina, sao」"
"1431" = "「Ư!!!」"
"1432" = "「Ư!!!!」"
"1433" = "「Ư!!!!!!」"
"1434" = "「Ư!?」"
"1440" = "「~~~~~~~~~~~~~~Ư!!!!」"
"1584" = "Aa——đúng rồi. Reina là một quý cô.\\nĐồng thời với việc là một quý cô, em ấy cũng sâu sắc là một…… người phụ nữ."
```

## Lượt soát 2

- Đã đọc lại toàn bộ 60 fix đối chiếu từng dòng JP (lượt soát 2): **60/60 re-verified, 0 bỏ, 0 sửa**. Đếm nguyên âm từng token romaji đã kiểm chứng bằng máy (Kyafuuuuuu 6 u, Hyauuuun 4 u, Nkyuuuuuuuuu 9 u, Nkyuuuuuuu 7 u, Fuaaaaa 5 a, Faaa 3 a, Kyaan/Yaan 2 a).
- JSON 60 mục, khối TOML [script] 60 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 60/60; mỗi fix chỉ khác old VN ở đúng chỗ sửa (diff-sanity: chỉ 4 dòng rên ngắn toàn dòng có tỉ lệ tương đồng <0,6 — 1170, 1174, 1298, 1299 — vì cả dòng chính là âm rên, đã kiểm chứng trong lượt soát 2).

## Chờ Hieu (chỉ ghi nhận, không cần quyết ngay)

- おまんこ "lồn" (1150, 1736) vs "chỗ đó" (1400, 1427) tỉ lệ 2/2 trong file — thống nhất 1 dạng toàn tuyến Reina hay giữ cả hai? (Cùng câu hỏi như Mayami h1: 6/6.)
- Mâu thuẫn quy tắc SFX ngắn + っ (brief 20/11 "thêm Ư" cho ああっ/はうっ vs thực hành hiện tại giữ La-tinh — file này giữ A/Hau/… theo hachirokuh3 + lr-h1/lr-h2 + ふかみh2 + moan-fix loop; đã được cờ ở hachirokuh3, không quyết lại ở đây).
- 1240 ふか、いっ → "sâu, quá" (phán đoán: いっ là mảnh vỡ của いい) và 1225 くっ → "Ư" (mất phụ âm k đầu tiếng gằn) — hai phán đoán ít chắc chắn hơn, nhờ moan-fix loop / parent xác nhận khi có dịp.

## Kết bài

File lr_れいなh1_レディ・れいな: 311 dòng đã đọc hết, **60 dòng sai (19,3%)** — lỗi tập trung ở rên/thở H-scene (39 dòng: họ fa/fu + họ ひゃ/きゅ trộn romaji–Việt + cười bị gắn Ư gasp), đại từ Soutetsu "tôi"→"anh" với Reina (5 dòng), gasp sweep (8 dòng), nguyên âm (5 dòng) và âm khác (3 dòng). Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Sweep đã kiểm chứng trực tiếp: 8 fix áp nguyên, 5 already-rendered đúng, 2 needs-file-audit đã kiểm chứng không sửa. Lượt soát 2: 60/60, 0 bỏ, 0 sửa.
