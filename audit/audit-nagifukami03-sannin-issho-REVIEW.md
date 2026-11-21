# Audit — 07_Nagi_Fukami 凪ふかみ03_三人いっしょ.txt.toml

- File: `07_Nagi_Fukami/凪ふかみ03_三人いっしょ.txt.toml` ("ba người cùng nhau" — cảnh rèn dao ở lò rèn Minokasa + tỏ tình / tiếp tục chuyến dã ngoại)
- Đã đọc: **413/413 dòng** (toàn bộ `[script]`), đối chiếu từng dòng với JP + TW (CSV3).
- Kết quả: **17 dòng sai / 413 (4,1%)** — file sạch, không có lỗi hệ thống.
- Cơ sở tổng: 176 file / 8.005 dòng sai (đã kiểm chứng với ROUTE-AUDIT.md, dòng tổng mới nhất).

## Kiểm chứng nguồn

- CSV3: **1 bộ duy nhất** (413 dòng, key 1062–2562, không trùng key, 0 dòng VN trống). Không có bẫy dual-set.
- CSV3 ↔ TOML: 197 khớp tuyệt đối + 216 gộp `\n` thành khoảng trắng, **0 khác biệt thực chất**.
- JP comment trong TOML khớp CSV3 **413/413** (426 comment gồm cả `[characters]`/`[character_subs]`).
- TOML md5: `51f7f7a84eeaa7049b2f3d1eb2c30d00`, BOM + CRLF, `[selections]` rỗng. **Không có bản sao trùng** (quét md5 toàn bộ `sources/toml2/` — không file nào trùng).
- Thẻ `%l`: JP = VN = 4 thẻ (1561: 列車; 2521: 8620, 客車, 機関士), đều đúng dạng, không lệch, không thiếu `;`.
- Sweep gasp っ: file có **3 mục** trong `sweep-raw-gasp-wrong.json` (1460, 1848, 1849) — cả 3 đều đúng, đã nhận nguyên (xem dưới). 4 mục còn lại khi tìm "凪ふかみ03" thuộc file khác (凪ふかみ03_みかんの旅: 2229, 2273, 2274, 2295), không phải file này.
- Quét bổ sung bằng máy: mọi dòng JP chứa っ đã rà lại tay — các っ còn lại đều đã diễn (trong từ, hoặc thành "t"/"rốp"/"Keng"/"Phập"/"Chụt"/dấu câu) hoặc là っ nhấn mạnh gắn với từ nội dung (いいえっ 1854, ですからっ―― 1649, すごいっ 1552, あっ…… 1486) — không sót gasp nào ngoài 3 mục sweep.

## Phân loại lỗi (17)

- Xưng hô: 5 (1427, 1528, 1532, 1810, 2126)
- Sai nghĩa: 7 (2011 + 6 dòng "chân ga" 2135, 2333, 2445, 2504, 2530, 2537)
- Mất gasp っ: 3 (1460, 1848, 1849 — theo sweep)
- Lỗi nhỏ: 2 (1516, 1522 — "Ạ" đứng riêng câu)
- Lệch vị trí / xoay vòng: **0** — không có chuỗi lệch nào; đã kiểm tra cặp trùng giá trị: không có VN nào lặp ở 2 key.
- Nhiễm chéo file khác: **0**. Dòng mồ côi: **0**. Chưa dịch: **0**. Trùng key: **0**.
- Đại từ Fukami–Nagi: **0 lỗi** — Nagi→Fukami luôn "bé"/gọi tên (1494 "cậu" đúng), Fukami tự xưng "mình" (1455), Fukami→Nagi "cậu"/gọi tên; không có "chị"/"em" sai nào cho cặp này.
- Soutetsu "tôi" trong thoại: chỉ 4 dòng toàn file (1760 đúng — nói với Mayami; 1528/1532/1810 sai — đã sửa dưới). Soutetsu tự xưng "em": chỉ 1 dòng (1427 — đã sửa).

## Chi tiết từng lỗi

### 1. Xưng hô — 1427 (双鉄)

- JP: 「しかし――僕は右田の」
- TW: 「可是——我是右田家的」
- Cũ: 「Nhưng——em là người nhà Migita」
- Mới: 「Nhưng——tôi là người nhà Migita」
- Lý do: Soutetsu tự giới thiệu mình là người nhà Migita — người nghe là ông Minokasa (người lạ, bậc trưởng bối), bằng chứng: dòng tiếp theo 1429 dùng です + bản Việt có "ạ" ("Migitai——Là cơ sở nấu rượu Migitai ạ"); với Minokasa Soutetsu xưng "tôi" (xem thêm 1497 "cảm ơn ông"). Dù người nghe là Minokasa hay Mayami thì cũng là "tôi"; chỉ khi nói với Nagi/Fukami mới là "anh" — nội dung tự giới thiệu + lối nói trang trọng loại trừ hai em. "Nhà Migita" giữ nguyên (JP 右田の, không có 一).

### 2. Mất gasp — 1460 (ふかみ) [sweep: lost-gasp-trailing]

- JP: 「わぁあ！\n凪ちゃん、まだ開けちゃだ――めぇぇ～～っ！？」
- TW: 「哇！小凪，現在還不能開——門！？」
- Cũ: 「Oaaaa!\nNagi, vẫn chưa được mở cửa đâ——uuuu~~!?」
- Mới: 「Oaaaa!\nNagi, vẫn chưa được mở cửa đâ——uuuu~~Ư!?」
- Lý do: っ cuối sau ～～ bị mất hẳn — thêm Ư theo quy tắc gasp đã khóa. Nhận nguyên giá trị sweep (đã kiểm chứng với JP).

### 3. Lỗi nhỏ — 1516 (ふかみ)

- JP: 「ん……っと、これ――むつかしい。です」
- TW: 「嗯……喲，這個，好難啊。嗯」
- Cũ: 「Ưm... ừm, cái này——khó quá. Ạ」
- Mới: 「Ưm... ừm, cái này——khó quá ạ.」
- Lý do: です được diễn thành "Ạ" đứng riêng một câu — gộp vào cuối câu trước. Tiền lệ: file khác đã tính "Ạ." đứng riêng câu là lỗi nhỏ.

### 4. Lỗi nhỏ — 1522 (ふかみ)

- JP: 「うん。こんな感じ。です」
- TW: 「嗯。差不多這樣吧。嗯」
- Cũ: 「Vâng. Cảm giác như thế này. Ạ」
- Mới: 「Vâng, cảm giác như thế này ạ.」
- Lý do: như 1516 — "Ạ" đứng riêng câu, gộp lại.

### 5. Xưng hô — 1528 (双鉄)

- JP: 「うむ。イメージ通りに出来た。\n右田の台所には、広刃の包丁がないのだ」
- TW: 「嗯，做成我想的樣子了。右田家廚房裡，還缺一把闊刃的菜刀呢」
- Cũ: 「Ừm. Đúng như tôi tưởng tượng.\nNhà bếp của Migita không có con dao bản rộng nào cả」
- Mới: 「Ừm. Đúng như anh tưởng tượng.\nNhà bếp của Migita không có con dao bản rộng nào cả」
- Lý do: cùng khối thoại với các em ở lò rèn — dòng 1529 ngay sau nói về "chuyến đi dã ngoại của ba người cùng nhau", 1532 nói về Minokasa ở ngôi thứ ba ("bên kia"), Nagi đáp lại ở 1545; cùng cảnh Soutetsu dùng "anh" ở 1520 ("Anh có cảm giác...") và 1536 ("Vì anh... chịu đựng"). "Tôi" ở đây lạc giọng → "anh".

### 6. Xưng hô — 1532 (双鉄)

- JP: 「うむ？　するとむしろ、利害で繋がっているのかな。\n向こうが友達だというので、僕もそうだと思っていたが」
- TW: 「嗯？要這麼說的話，或許是利害一致吧。對方當我是朋友，我也就沒多想同樣當他是朋友了」
- Cũ: 「Ưm? Vậy ra là gắn kết với nhau vì lợi ích sao.\nBên kia bảo là bạn bè, nên tôi cũng nghĩ vậy thôi」
- Mới: 「Ưm? Vậy ra là gắn kết với nhau vì lợi ích sao.\nBên kia bảo là bạn bè, nên anh cũng nghĩ vậy thôi」
- Lý do: như 1528 — Soutetsu đang nói với Nagi/Fukami về Minokasa ("bên kia"); Nagi đáp thẳng ở 1545 ("Cơ duyên thế nào cũng chẳng quan trọng đâu..."). "Tôi" → "anh".

### 7. Xưng hô — 1810 (双鉄)

- JP: 「ならば僕には、\n帝大に、少なくとも一人は友達がいる」
- TW: 「這麼說的話，我在帝大至少也算有一個朋友了」
- Cũ: 「Nếu vậy thì,\nít nhất tôi cũng có một người bạn ở Đại học Đế quốc」
- Mới: 「Nếu vậy thì,\nít nhất anh cũng có một người bạn ở Đại học Đế quốc」
- Lý do: Soutetsu kết luận lại ý Fukami vừa nói ở 1803 ("nghe chuyện thì có vẻ không chỉ là lợi ích đâu"); dòng 1811 ngay sau nói với Nagi ("Em đạp mạnh quá rồi đấy"). Người nghe là Fukami/Nagi → "anh". "Đại học Đế quốc" giữ nguyên (帝大 = thuật ngữ đã chốt).

### 8. Mất gasp — 1848 (凪) [sweep: lost-gasp-whole]

- JP: 「っ！」
- TW: 「！」
- Cũ: 「!」
- Mới: 「Ư!」
- Lý do: cả dòng chỉ là tiếng hít っ + dấu cảm — bản Việt chỉ còn dấu câu. Nhận nguyên giá trị sweep.

### 9. Mất gasp — 1849 (双鉄) [sweep: lost-gasp-whole]

- JP: 「っ！！？」
- TW: 「！！？」
- Cũ: 「!!?」
- Mới: 「Ư!!?」
- Lý do: như 1848. Nhận nguyên giá trị sweep.

### 10. Sai nghĩa — 2011 (monologue)

- JP: ハンマーまでもが、少し動いて様子を見て――と、\n引っ込み思案になってるようだ。
- TW: 不要說鍛錘了，機器剛一動，感覺她就隨時打算收腳的樣子。
- Cũ: Ngay cả búa đập cũng hơi nhúc nhích thăm dò——\ncó vẻ như nó cũng đang e dè.
- Mới: Ngay cả búa đập cũng chỉ hơi nhúc nhích như đang thăm dò——\ncó vẻ em ấy cũng đang chần chừ, chỉ chực rụt chân lại.
- Lý do: chủ ngữ của 引っ込み思案 (chần chừ, ngập ngừng) là người đạp bàn đạp (Nagi), không phải cái búa — TW nói rõ "cô ấy có vẻ chỉ chực rụt chân lại". Bản cũ gán sự e dè cho "nó" (cái búa), sai chủ thể. "Em ấy" = Nagi (người đang đạp bàn đạp ở cảnh này; xem 2135).

### 11. Xưng hô — 2126 (monologue)

- JP: 凪なら元気一辺倒で、ふかみは常に慎重で。\nそのイメージとまるでことなる姿も見れた。
- TW: 凪無論何時都是精神抖擻，深美則總是慎重謹慎。今天所見與這樣的印象顯然完全不同。
- Cũ: Nagi thì lúc nào cũng tràn đầy năng lượng, còn Fukami thì luôn thận trọng.\nAnh cũng đã thấy được những dáng vẻ hoàn toàn khác với hình ảnh đó.
- Mới: Nagi thì lúc nào cũng tràn đầy năng lượng, còn Fukami thì luôn thận trọng.\nTôi cũng đã thấy được những dáng vẻ hoàn toàn khác với hình ảnh đó.
- Lý do: độc thoại không có người nghe — tự xưng chuẩn của Soutetsu trong lời dẫn là "tôi" (quét bằng máy: đây là dòng độc thoại duy nhất trong file dùng "Anh" làm chủ ngữ; 2549 "Mình..." là ngoại lệ độc thoại nội tâm trong ngoặc, giữ nguyên theo quy tắc).

### 12–17. Sai nghĩa — "chân ga" → "bàn đạp" (6 dòng, cùng một lỗi hệ thống)

ペダル ở đây là bàn đạp chân của búa máy rèn (belt hammer), không phải chân ga xe. TW đều viết 踏板 (bàn đạp). Cả 6 dòng chỉ đổi đúng cụm này, còn lại giữ nguyên:

- 2135 (monologue) — JP: 凪がペダルを踏み込めば、\n蓑笠さんのときより数倍速くハンマーが落ちる。 / TW: 凪踩在踏板上，鍛錘以蓑笠先生操作時數倍的速度落下。 / Cũ: "Nagi vừa đạp chân ga,\nbúa đã giáng xuống nhanh gấp mấy lần lúc ông Minokasa làm." / Mới: "Nagi vừa đạp bàn đạp,\nbúa đã giáng xuống nhanh gấp mấy lần lúc ông Minokasa làm."
- 2333 (monologue) — JP: ふかみの両肩がスっと下がって、\nペダルも、自然と踏み込まれていく。 / TW: 深美放鬆了緊繃的雙肩，踏板上的力道也自然了許多。 / Cũ: "Hai vai Fukami chùng xuống,\nchân ga cũng được đạp một cách tự nhiên." / Mới: "Hai vai Fukami chùng xuống,\nbàn đạp cũng được đạp một cách tự nhiên."
- 2445 (monologue) — JP: 蓑笠さんが機械の前に座りペダルを踏み込めば、\nガインガインと轟音をたて、ハンマーがピストン動作する。 / TW: 蓑笠先生坐在機器前，隨著他一下下踩下踏板，鍛錘上下活塞式地運動，鐺鐺的捶打聲響徹耳畔。 / Cũ: "Ông Minokasa ngồi trước máy, đạp chân ga,\nâm thanh rầm rầm vang lên, búa đập hoạt động như pít-tông." / Mới: "Ông Minokasa ngồi trước máy, đạp bàn đạp,\nâm thanh rầm rầm vang lên, búa đập hoạt động như pít-tông."
- 2504 (monologue) — JP: 踏み込み方もまるで違う。\n慎重……というか、緊張モードだ。 / TW: 踩踏板的動作也不一樣。與其說是慎重，不如說是太緊張吧。 / Cũ: "Cách đạp chân ga cũng hoàn toàn khác.\nThận trọng... hay nói đúng hơn là đang ở chế độ căng thẳng." / Mới: "Cách đạp bàn đạp cũng hoàn toàn khác.\nThận trọng... hay nói đúng hơn là đang ở chế độ căng thẳng."
- 2530 (monologue) — JP: 気持ちよさそげにハンマーを落とし、\n落としつづけて――ようやく、凪はペダルを離す。 / TW: 鍛錘以順暢的節奏不斷升起、落下——終於，凪從踏板上抬起了腳。 / Cũ: "Để búa đập xuống một cách thoải mái,\nđập liên tục——cuối cùng, Nagi cũng nhả chân ga." / Mới: "Để búa đập xuống một cách thoải mái,\nđập liên tục——cuối cùng, Nagi cũng nhả bàn đạp."
- 2537 (monologue) — JP: とにかくペダルは力を入れず、一定に―― / TW: 首先踏板上不要加太大力，保持穩定—— / Cũ: "Tóm lại là không dùng sức đạp chân ga, giữ nguyên một mức độ——" / Mới: "Tóm lại là không dùng sức đạp bàn đạp, giữ nguyên một mức độ——"

## Những dòng đã kiểm kỹ và GIỮ nguyên

- 1432 きゃっ → "Á!?" — tiếng giật mình ngoài H-scene, không áp quy tắc romaji ひゃ-family (quy tắc đó chỉ cho rên trong H-scene). Giữ.
- 1854 いいえっ / 違かとっ → "Không phải ạ" / "Sai rồi!" — っ nhấn mạnh gắn với từ nội dung, không thêm Ư theo quy tắc gasp đã khóa. Giữ.
- 1858 （ちゅっ！）×2 → "(Chụt!)" — っ đã diễn thành "t". Giữ.
- 1486 あっ…… → "A..." — dấu "..." đã diễn nét ngắt câu; tiền lệ ハチロク01 2319 (không thêm Ư khi âm ngắt đã được diễn). Giữ.
- 1510 ぷはあっ → "Phù," — tiếng thở ra đã diễn; tiền lệ file 09 (ふあっ→"Phù"). Giữ.
- 1823 しゅ、うがっ！？ → "Chuy... ư!?" — diễn lắp giọng (修学 bị ngắt + もごもご → "Ưm ưm~"). Giữ.
- 1633 養子 → "con nuôi" — đúng (養子, khác với 義; quyết định 義 21/11 ~19:45 xác nhận "nuôi" đúng cho nhà Migita). Giữ.
- 2549 độc thoại "(Mình... ngay từ đầu..." — ngoại lệ "mình" cho độc thoại nội tâm trong ngoặc. Giữ.
- 1760 "tôi" (nói với Mayami) và 1497 "cảm ơn ông" (nói với Minokasa) — đúng quy tắc đại từ. Giữ.
- 1089/1344/1529/1640/1647 v.v. dùng "dã ngoại" cho 修学旅行 — quy ước dự án, nhất quán toàn file. Giữ.
- 1561 gloss 列車 "tàu" và 2521 gloss 機関士 "lái tàu" — xem mục cờ cho Hieu dưới đây, không sửa trong audit này.

## Cờ cho Hieu (không quyết — chờ đợt thống nhất / quyết của Hieu)

1. **"Ohito" cho 御一夜 — 6 dòng** (1411, 1580, 1620, 1646, 2183, 2489): dạng cũ, chờ đợt thống nhất đổi thành "Ohitoyo" theo quyết định 19/11 + quyết định 21/11 ~17:30 ("Đường sắt Ohito" → "Đường sắt Ohitoyo", 236 dòng). Không sửa trong audit này.
2. **"Migitai" cho 右田一 — 3 dòng** (1071, 1429, 2525): dạng cũ của "Migita Ichi" (右田一 = Migita + Ichi); tiền lệ ふかみh2 1096 "Migitaichi" → "Migita Ichi" đã xếp vào đợt thống nhất. "Nhà Migita" cho 右田 (không có 一) ở 1427/1528/1633/1673 là đúng, giữ nguyên. Không sửa trong audit này.
3. **Gloss 列車 "tàu" — 1561**: quyết định 21/11 ~18:55 đổi gloss 列車 thành "đoàn tàu" (tiền lệ 真闇02 1113), các gloss 列車 còn lại quét trong đợt thống nhất. Không sửa trong audit này. (Gloss 機関士 "lái tàu" ở 2521 là dạng ngắn đã chốt, giữ nguyên.)
4. **Key 2058 không có trong file này**: quyết định 21/11 ~17:30 ghi "凪ふかみ03 2058" (代理車掌 → "trưởng tàu đại diện") — key 2058 thuộc file **凪ふかみ03_みかんの旅.txt.toml** (JP 「つまり、君は代理車掌か」, VN "trưởng tàu đại lý"), không thuộc file 三人いっしょ này (file này không có key 2058; đã kiểm tra CSV3 + TOML). Ghi chú để khỏi nhầm khi áp dụng quyết định đó.
5. **Không có dòng nào chưa chắc chắn** trong file này — không cần Hieu kiểm tra trong game.

## Lượt soát 2 (bắt buộc)

Đã đọc lại toàn bộ 17 giá trị sửa đối chiếu từng dòng với JP (+TW) sau khi viết xong danh sách lần 1.

- Tổng số sửa: **17**
- Đã kiểm chứng lại: **17**
- Bỏ đi: **0**
- Sửa lại giá trị trong lượt 2: **0**

Kiểm chứng cơ học (script): JSON 17 mục (key chuỗi, dạng list-of-dicts chuẩn); jp/tw/old_vn khớp CSV3 tuyệt đối **17/17**; khối TOML dưới đây parse được bằng tomllib, **17 khóa, 0 sai lệch giá trị** so với JSON; mỗi sửa chỉ khác bản cũ ở đúng chỗ cần sửa (kiểm tra diff từng dòng: đại từ đổi đúng 1 từ; gasp chỉ thêm Ư; "chân ga"→"bàn đạp" đúng 1 cụm; 1516/1522 chỉ gộp "Ạ"; 2011 viết lại đúng 1 câu có chủ ngữ sai).

## Khối TOML đã kiểm chứng parse

```toml
[script]
"1427" = "「Nhưng——tôi là người nhà Migita」"
"1460" = "「Oaaaa!\\nNagi, vẫn chưa được mở cửa đâ——uuuu~~Ư!?」"
"1516" = "「Ưm... ừm, cái này——khó quá ạ.」"
"1522" = "「Vâng, cảm giác như thế này ạ.」"
"1528" = "「Ừm. Đúng như anh tưởng tượng.\\nNhà bếp của Migita không có con dao bản rộng nào cả」"
"1532" = "「Ưm? Vậy ra là gắn kết với nhau vì lợi ích sao.\\nBên kia bảo là bạn bè, nên anh cũng nghĩ vậy thôi」"
"1810" = "「Nếu vậy thì,\\nít nhất anh cũng có một người bạn ở Đại học Đế quốc」"
"1848" = "「Ư!」"
"1849" = "「Ư!!?」"
"2011" = "Ngay cả búa đập cũng chỉ hơi nhúc nhích như đang thăm dò——\\ncó vẻ em ấy cũng đang chần chừ, chỉ chực rụt chân lại."
"2126" = "Nagi thì lúc nào cũng tràn đầy năng lượng, còn Fukami thì luôn thận trọng.\\nTôi cũng đã thấy được những dáng vẻ hoàn toàn khác với hình ảnh đó."
"2135" = "Nagi vừa đạp bàn đạp,\\nbúa đã giáng xuống nhanh gấp mấy lần lúc ông Minokasa làm."
"2333" = "Hai vai Fukami chùng xuống,\\nbàn đạp cũng được đạp một cách tự nhiên."
"2445" = "Ông Minokasa ngồi trước máy, đạp bàn đạp,\\nâm thanh rầm rầm vang lên, búa đập hoạt động như pít-tông."
"2504" = "Cách đạp bàn đạp cũng hoàn toàn khác.\\nThận trọng... hay nói đúng hơn là đang ở chế độ căng thẳng."
"2530" = "Để búa đập xuống một cách thoải mái,\\nđập liên tục——cuối cùng, Nagi cũng nhả bàn đạp."
"2537" = "Tóm lại là không dùng sức đạp bàn đạp, giữ nguyên một mức độ——"
```

## Kết bài

File 凪ふかみ03_三人いっしょ: 413 dòng đã đọc, **17 dòng sai (4,1%)** — xưng hô 5, sai nghĩa 7, mất gasp 3, lỗi nhỏ 2; 0 lệch vị trí, 0 nhiễm chéo, 0 dòng mồ côi, 0 chưa dịch, 0 trùng key. Không có lỗi hệ thống; lỗi tập trung ở 1 cụm "chân ga" (6 dòng) và 3 đại từ "tôi" lạc giọng trong cùng khối thoại ở lò rèn. 5 cờ cho Hieu (Ohito ×6, Migitai ×3, gloss 列車 ×1, key 2058 thuộc file みかんの旅, 0 dòng chưa chắc chắn) đều đã ghi ở trên, không sửa trong audit này. Lượt soát 2: 17/17 đã kiểm chứng lại, 0 bỏ, 0 sửa lại.
