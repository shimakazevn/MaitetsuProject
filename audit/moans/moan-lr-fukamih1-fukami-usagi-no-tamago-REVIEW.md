# Moan-fix — lr_ふかみh1_ふかみうさぎのたまご.txt.toml (07_Nagi_Fukami)

## 1. Kiểm chứng file

- **File:** `lr_ふかみh1_ふかみうさぎのたまご.txt.toml` — route 07_Nagi_Fukami, cảnh Fukami làm thỏ Phục Sinh tặng Soutetsu "trứng" của mình.
- **Đường dẫn đĩa:** `sources/toml2/translation_toml/07_Nagi_Fukami/lr_#U3075#U304b#U307fh1_#U3075#U304b#U307f#U3046#U3055#U304e#U306e#U305f#U307e#U3054.txt.toml`
- **TOML md5:** `978b35d98d620183d1a58aa3aaa8eda0` — trùng khớp md5 audit. **Không có bản trùng lặp** (chỉ 1 bản trong `sources/toml2/`).
- **CSV3: 2 bộ** — bộ home `07_Nagi_Fukami` STALE (khớp TOML 3/289), bộ `11_Other` TỐT (khớp 288/289 tuyệt đối + 1 khác duy nhất là 1466, TOML làm phẳng literal `\n` đầu dòng thành khoảng trắng — khớp 289/289 về nội dung). **Đã dùng bộ 11_Other.**
- **Số dòng đã đọc: 289/289** (key 961–1973), đọc từng dòng đối chiếu JP + TW (CSV3 bộ TỐT) + VN (TOML).
- **Audit trước đó: 76 dòng sai** (xem `audit-lr-fukamih1-REVIEW.md`) — trong đó 17 gasp Ư, 21 fa/fu, 8 đếm nguyên âm, 1 mất tiếng thở はっ (1196).

## 2. Kho rên (moan inventory)

- **111 dòng theo mẫu quét** (64 thoại rên + 47 SFX trong ngoặc `（ ）` ở độc thoại), cộng các dòng rên lẻ đã đọc tay trong lúc đọc toàn bộ file (ぁ đơn, うあっ/くあっ/ひうっ/むっ, tiếng gắng sức んしょ/よいしょ, cười えへへ).
- **Đổi 33 dòng:** 21 romaji fa/fu + 9 đếm nguyên âm + 1 mất tiếng thở + 1 sai âm + 1 mất độ dài.
- **Giữ ~82 dòng rên/SFX** trong kho quét (xem §5) + các dòng rên lẻ đã đọc tay.
- **Không đụng 16/17 dòng gasp Ư của audit** (1257, 1259, 1260, 1261, 1262, 1288, 1339, 1374, 1435, 1438, 1613, 1651, 1681, 1682, 1780, 1835); dòng còn lại 1268 chỉ đổi phần ふぁっ → "Fa", giữ nguyên Ư gasp của audit. Không dòng "Kh" nào bị đổi (file này không có dòng "Kh" nào).
- **Không có dòng cười nào bị diễn thành rên** (chỉ có えへへ → "Ehehe", đã đúng).

## 3. Các dòng đã sửa (33 dòng)

Quy tắc áp dụng: romaji fallback (Hieu duyệt 21/11 ~01:56) — "phà"/"phù"/"phuê" cho họ fa/fu nghe ngượng trong tiếng Việt (gợi thổi/phù) nên chuyển sang romaji của âm JP; một dòng = một cách diễn (VN hoặc romaji, không trộn); độ dài nguyên âm theo công thức (số nguyên âm VN = 1 + số う/ぅ trong JP; với chuỗi ぁ thì đếm trực tiếp số ぁ). Các fix trùng key với audit thì **áp giá trị moan thay giá trị audit** (chỉ khác ở đúng phần rên), theo tiền lệ nagih2/h8/tomohari.

### A. Romaji họ fa/fu (21 dòng) — "phà"/"phù"/"phuê" → romaji

Quy ước romaji đã chốt theo tiền lệ nagih2/h8/tomohari: ふぁ → "Fa", ふあ → "Fua", ふぇ → "Fue", ぷあ → "Pua", ふぁぅ → "Fau"; ふ、あ tách nhịp bằng 、 → "Fu, a" (2 nhịp, theo cách đọc của audit và bản cũ — xem ghi chú §6).

- **1223 [ふかみ]** — JP: 「けど――んっ――それなら、なんで――ふ、ぁ――」. VN cũ: "——fu, a——". **Mới: "——Fu, a——"**. (Chỉ khác bản cũ ở chữ hoa — nhưng phải ghi dòng này để giá trị moan "Fu, a" thay giá trị audit "phù, a" ở đợt thống nhất.)
- **1233 [ふかみ]** — JP: 「ふぁっ――しゅごい！」. VN cũ: "Ha——tuyệt quá!". **Mới: "Fa——tuyệt quá!"**.
- **1252 [ふかみ]** — JP: 「ふぇ？――あ！」. VN cũ: "Hả? ——A!". **Mới: "Fue? ——A!"**.
- **1254 [ふかみ]** — JP: 「ふぇっ？　あ――あ！」. VN cũ: "Hả? A——a!". **Mới: "Fue? A——a!"**.
- **1267 [ふかみ]** — JP: 「ぁ――あっ――あんっ――ふあっ――あっ――あ――」. VN cũ: "A——a——an——ha——a——a——". **Mới: "A——a——an——Fua——a——a——"**.
- **1268 [ふかみ]** — JP: 「ぁ――ふぁっ――来た！　先っぽ――っ――亀頭――」. VN cũ: "A——ha——vào rồi! Phần đầu——quy đầu——". **Mới: "A——Fa——vào rồi! Phần đầu——Ư——quy đầu——"**. (Chỉ đổi ふぁっ → "Fa"; giữ nguyên Ư gasp của audit — KHÔNG xét lại gasp.)
- **1270 [ふかみ]** — JP: 「あっ――ふあっ――双鉄、おにいさんの、指――」. VN cũ: "A——ha——ngón tay". **Mới: "A——Fua——ngón tay"**.
- **1283 [ふかみ]** — JP: 「あっ！　んっ！　きゅっ！！　あっ！　あっ！ふあっ！」. VN cũ: "A! Ưm! Kyu!! A! A! Ha!". **Mới: "A! Ưm! Kyu!! A! A! Fua!"**.
- **1379 [ふかみ]** — JP: 「――ふ、あ」 (cuối dòng). VN cũ: "——fu, a.". **Mới: "——Fu, a."**. (Như 1223: chỉ khác bản cũ ở chữ hoa, nhưng cần chặn giá trị audit "phù, a".)
- **1457 [ふかみ]** — JP: 「ふぁっ――あっ――きもち、いい――」. VN cũ: "Ha——a——sướng, quá——". **Mới: "Fa——a——sướng, quá——"**.
- **1458 [ふかみ]** — JP: 「はっ――あっ――ふ、あっ――」. VN cũ: "Ha——a——fu, a——". **Mới: "Ha——a——Fu, a——"**. (Như 1223/1379.)
- **1460 [ふかみ]** — JP: 「は……ぁっ――ふぁぅ……んっ――」. VN cũ: "Ha…… a——hau…… ưm——". **Mới: "Ha…… a——Fau…… ưm——"**. (ふぁぅ = fa + ぅ → "Fau".)
- **1461 [ふかみ]** — JP: 「ふあっ……あ……う……」. VN cũ: "Ha…… a…… ư……". **Mới: "Fua…… a…… ư……"**.
- **1463 [ふかみ]** — JP: 「ふあっ――ンッ――うれしい――」. VN cũ: "Ha——ưm——vui quá——". **Mới: "Fua——ưm——vui quá——"**.
- **1464 [双鉄]** — JP: 「ふぁっ！　あっ！　あっ！　あっ！」. VN cũ: "Ha! A! A! A!". **Mới: "Fa! A! A! A!"**.
- **1465 [ふかみ]** — JP: 「ふああっ！」. VN cũ: "Haa!". **Mới: "Fuaa!"**. (ふああ = 2 a → "Fuaa".)
- **1467 [ふかみ]** — JP: 「ふぁ！　あっ！　すごい！」. VN cũ: "Ha! A! Tuyệt quá!". **Mới: "Fa! A! Tuyệt quá!"**.
- **1468 [ふかみ]** — JP: 「ふぁっ！　あっ！　そうてつ！」. VN cũ: "Ha! A! Soutetsu! Anh! A!". **Mới: "Fa! A! Soutetsu! Anh! A!"**.
- **1469 [ふかみ]** — JP: 「ふぁっ！　急にっ！」. VN cũ: "Ha! Đột nhiên!". **Mới: "Fa! Đột nhiên!"**.
- **1471 [ふかみ]** — JP: 「ふぁっ！　ここっ――」. VN cũ: "Ha! Chỗ này——". **Mới: "Fa! Chỗ này——"**.
- **1472 [ふかみ]** — JP: 「ふあっ！　そうてつ、おにいさんの、おちん、ちんっ」. VN cũ: "Ha! Dương, vật, của anh Soutetsu". **Mới: "Fua! Dương, vật, của anh Soutetsu"**.

Sau 21 dòng này, **không còn dòng fa/fu nào diễn "phà"/"phù"/"phuê" trong file**. ふう/ふっ (hơi thở "phù") không thuộc họ này — giữ nguyên (xem §5).

### B. Đếm nguyên âm (9 dòng) — 8 dòng áp nguyên giá trị audit + 1 dòng audit bỏ sót

- **1224 [ふかみ]** — JP: 「ひゅぁぁぁぁぁぁぁっぁぁぁぁぁぁぁっぁぁぁん！！」 (17 ぁ). VN cũ: "Hyuaaaaaaaaaan!!" (10 a). **Mới: "Hyuaaaaaaaaaaaaaaaaan!!"** (17 a — đã đếm lại bằng máy).
- **1279 [ふかみ]** — JP: 「きゃふうううううううっ！！」 (ふ + 7 う → 8 u). VN cũ: "Kyafuuu!!" (3 u). **Mới: "Kyafuuuuuuuu!!"** (8 u).
- **1310 [ふかみ]** — JP: 「んっ！　ゅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅんんっ！」 (ゅ + 15 ぅ → 16 u). VN cũ: "Ưm! Yuuuuuuuuuuuuuun!" (14 u). **Mới: "Ưm! Yuuuuuuuuuuuuuuuun!"** (16 u).
- **1655 [monologue]** — JP: 「きゅんきゅんぐいぐい締めてくる。」 (きゅん = 0 う → 1 u). VN cũ: "…siết chặt lấy tôi, kyuun kyuun." (2 u mỗi token). **Mới: "…siết chặt lấy tôi, kyun kyun."** (Audit bỏ sót — quét của audit chỉ kiểm tra chuỗi JP dài ≥3, còn đây là lỗi phía VN: JP ngắn mà VN kéo dài. Đối chiếu tiền lệ cùng file: 1968 きゅんっ → "Kyun" (1 u), 1782 きゅうん → "kyuun" (2 u).)
- **1920 [monologue]** — JP: （ぐぢゅぅぅぅぅぅぅぅぅぅぅぅぅっ！――ごりゅっ！） (ぐぢゅ + 12 ぅ → 14 u tổng). VN cũ: "(Guchuuuuuu! ——Cụp!)" (6 u). **Mới: "(Guchuuuuuuuuuuuuu! ——Cụp!)"** (14 u — giữ "Guch" của bản cũ, chỉ sửa số lượng).
- **1949 [monologue]** — JP: （きゅうううっ！！　きゅっ！） (きゅ + 3 う → 4 u). VN cũ: "(Kyuuu!! Kyu!)" (3 u). **Mới: "(Kyuuuu!! Kyu!)"** (4 u).
- **1966 [monologue]** — JP: （きゅううううううっっっ！！） (きゅ + 6 う → 7 u). VN cũ: "(Kyuuu!!)" (3 u). **Mới: "(Kyuuuuuuu!!)"** (7 u).
- **1967 [monologue]** — JP: （ぎちゅちゅっ！　きゅうっ！　きゅうんっ！！）. Token 2: きゅうっ → 2 u, VN cũ "Kyu" chỉ 1 u. **Mới: "(Gichuchu! Kyuu! Kyuun!!)"**. (Token 1 "Gichuchu" và token 3 "Kyuun" đã đúng.)
- **1968 [monologue]** — JP: （きゅんっ！） (0 う → 1 u). VN cũ: "(Kyuun!)" (2 u — thừa 1). **Mới: "(Kyun!)"**.

### C. Các lỗi rên khác (3 dòng)

- **1196 [双鉄] (mất tiếng thở)** — JP: 「だが――ぁっ――このまま、で、はっ――」. VN cũ: "Nhưng——a——cứ thế này, thì——" — tiếng thở はっ cuối dòng bị mất hẳn. **Mới: "Nhưng——a——cứ thế này, thì——ha——"**. (Áp nguyên giá trị audit; はっ → "ha" theo tiền lệ 1458/1462.)
- **1280 [ふかみ] (sai âm)** — JP: 「ひうっ！！！！！」. TW: 「啊嗚！！！！！」. VN cũ: "Hí!!!!!" — mất glide "u" (ひう = "hiu", TW 啊嗚 = hai nguyên âm). **Mới: "Hiu!!!!!"**. (Audit bỏ sót — không nằm trong danh sách giữ §5 của audit; ひう khác ひえ ở 1234, xem §5.)
- **1432 [双鉄] (mất độ dài)** — JP: 「ふ――かみ――緩めて、くれないとっ――ぁあっ！！」. VN cũ: "Fu——kami——nới lỏng ra, cho tôi——a!!" — ぁあ = 2 âm a nhưng VN chỉ có 1 "a". **Mới: "Fu——kami——nới lỏng ra, cho anh——aa!!"**. (Giữ đại từ "cho anh" của audit; chỉ thêm 1 "a". Audit bỏ sót vì quét đếm nguyên âm của audit chỉ kiểm tra chuỗi JP ≥3 âm. Tiền lệ cùng file: 1258 うあっ → "Ua!", 1226 くあっ → "Kua!!?" — rên 2 nguyên âm luôn giữ đủ 2 âm.)

## 4. Kiểm chứng sweep っ

Sweep `sweep-raw-gasp-wrong.json` có 13 mục cho file này (audit đã kiểm chứng ở §4 của audit review): 5 mục lost-gasp áp đúng (1288, 1613, 1651, 1780, 1835), 3 already-rendered giữ đúng (1287, 1304, 1400), 5 needs-file-audit (1384, 1445, 1629, 1817 đúng — không sửa; 1967 có lỗi đếm nguyên âm thật — đã sửa ở §3B). **16/17 dòng gasp Ư của audit đều KHÔNG đụng trong file moan này**; dòng còn lại 1268 chỉ đổi phần ふぁっ, giữ nguyên Ư của audit. Không dòng "Kh" nào bị đổi.

## 5. Các phán đoán giữ nguyên (không tính sai)

- **あっ/うあっ/くあっ → "A"/"Ua"/"Kua" (1225, 1226, 1258, 1295, 1296…): giữ.** Nguyên âm + っ cuối đã diễn bằng nguyên âm + dấu câu; tiền lệ 00common12.
- **ひゃうっ → "Hyau" (1285, 1294): giữ.** Đã là romaji đúng âm; tiền lệ h2 1097.
- **ひえっ → "Hí" (1234): giữ.** Đây là thốt từ ngạc nhiên (TW 「哇」), không phải rên — "Hí" là thốt từ tiếng Việt tự nhiên cho sự ngạc nhiên, khác với 1280 ひうっ là rên trong cụm rên (TW 「啊嗚」) nên phải giữ đủ âm "Hiu". Phân biệt này khác với tomohari 976 (ひえっ → "Hie!?") vì ở đó bản cũ là "Hi e!?" bị tách vỡ, còn ở đây "Hí" là một thốt từ hoàn chỉnh.
- **はうっ → "Hau" (1281), はぁっ → "Ha" (969, 1462), はっ → "Ha" (1458, 1466): giữ.** Theo quyết định giữ của audit (§5 audit review) — はぁっ → "Ha" là quy ước thở của file này; không sửa thành "Haa".
- **んっ/ンッ → "Ưm"/"ưm" (969, 971, 1185, 1301, 1304, 1305, 1312, 1313, 1345, 1347, 1363, 1384, 1387, 1397, 1400, 1409, 1428, 1474…): giữ.** Quy ước nhất quán của file cho tiếng rên đầu ん.
- **んひゅんっ → "Ưm hyun" (1277), くひゅんっ → "Kuhyun" (1286), んきゅううっ → "Ưm kyuuu" (1304, đủ 3 u), んきゅっ → "Ưm kyu" (1305): giữ.**
- **Tiếng gắng sức んしょ/よいしょ → "Ưm, dô"/"dô, ta" (1317, 1318, 1775): giữ.** Không phải rên.
- **Cười えへへ → "Ehehe" (1322, 1460): giữ.** Cười đúng, không phải rên.
- **SFX ướt giữ phong cách diễn Việt (không sửa theo công thức đếm nguyên âm):** 1910–1917, 1919, 1921–1933, 1939–1944, 1948, 1950–1952, 1954, 1956–1962, 1964, 1965, 1971, 1973 — "Sùng sục/Phụt/Cụp/Sột soạt/Nhóp nhép/chụt/Hự" là diễn đạt Việt tự nhiên cho SFX ướt, không ngượng; chỉ sửa các token nào VN đã chọn chiến lược kéo dài nguyên âm mà đếm sai (§3B). Đối chiếu 1782 きゅうん → "kyuun" (đủ 2 u — giữ).
- **Tên kéo dài "Fu——ka…… mi." / "Fu——kami——" (1430, 1432) và "Fuka——" (1435): giữ.** JP cố tình kéo dài tên; VN tách âm tiết theo đúng nhịp JP (chỉ sửa phần rên ぁあっ ở 1432).
- **っ nhấn mạnh dính từ (すごいっ, おまんこっ, わたしっ, だめっ, にっ――…): giữ.** Không phải gasp.
- **1308 ああ → "Ừ.": giữ.** Thốt từ đồng ý, không phải rên.
- **1499 （くん、くんっ――くんくんっ） → "(Khịt, khịt——khịt khịt)": giữ.** SFX khịt mũi, đúng.

## 6. Ghi chú cho đợt thống nhất

- 3 dòng tách nhịp ふ、ぁ/ふ、あ (1223, 1379, 1458) đang diễn "Fu, a" theo cách đọc 2 nhịp (audit + bản cũ đều đọc 2 nhịp). Nếu đợt thống nhất đọc 、 chỉ là ngắt nhịp trong 1 mora "fa" thì đổi sang "Fa, a" — nhưng cần quyết có căn cứ, vì cả 3 nguồn (JP 、, audit, bản cũ) đều ủng hộ 2 nhịp.
- 1460 ふぁぅ → "Fau" (fa + glide u) — đã quyết theo Hepburn; nếu đợt thống nhất muốn "Fua" thì đó là đọc khác âm (fu + a), không phải cùng âm.
- 9 dòng §3B (trừ 1655) + 1196 áp nguyên giá trị audit — ở đợt thống nhất chỉ áp MỘT giá trị moan cho mỗi key, không áp cả hai.
- 1268: giá trị moan giữ Ư gasp của audit — đợt thống nhất áp giá trị moan này (đã gồm Ư), không áp riêng fix audit.
- 1432: giá trị moan giữ đại từ "cho anh" của audit — đợt thống nhất áp giá trị moan này, không áp riêng fix audit.

## 7. Kiểm chứng kỹ thuật

- JSON `moan-lr-fukamih1-fukami-usagi-no-tamago-wrong.json`: 33 mục, dạng chuẩn list-of-dicts, key là chuỗi; jp/tw/old_vn khớp CSV3 bộ TỐT 33/33.
- Khối TOML `[script]` dưới đây parse OK bằng tomllib: 33 khóa, **0 sai lệch giá trị** so với JSON.
- Diff-sanity: mỗi fix chỉ khác old VN ở đúng chỗ sửa (trừ các dòng áp giá trị audit — 1196, 1224, 1279, 1310, 1920, 1949, 1966, 1967, 1968, 1268, 1432 — trong đó phần khác thêm là fix audit đã có: đại từ "anh", gasp Ư, hoặc tiếng thở "ha"; phần moan do file này quyết chỉ khác đúng token rên).
- **Lượt soát 2 (đọc lại toàn bộ 33 fix đối chiếu JP): 33/33 tái kiểm chứng, 0 bỏ, 0 sửa.** Không fix nào bị loại hay sửa lại trong lượt soát 2.

## 8. Khối TOML đã kiểm chứng (33 khóa)

```toml
[script]
"1196" = "「Nhưng——a——cứ thế này, thì——ha——」"
"1223" = "「Nhưng——ưm——nếu vậy, thì tại sao——Fu, a——\\nanh Soutetsu——a——lại cản, em, lại.」"
"1224" = "「Hyuaaaaaaaaaaaaaaaaan!!」"
"1233" = "「Fa——tuyệt quá! Thật nhiều——tinh dịch——ưm,\\nnóng hổi——phụt phụt, đánh, vào bụng.」"
"1252" = "「Fue? ——A! Chuyện đó, hoàn toàn không có gì phải xin lỗi đâu ạ.\\nBởi vì——đúng không? Anh Soutetsu.」"
"1254" = "「Fue? A——a! Lúc đó, không sao đâu. Em sẽ,\\nrút, dương vật, ra——rồi anh bắn tinh, tung tóe.」"
"1267" = "「A——a——an——Fua——a——a——」"
"1268" = "「A——Fa——vào rồi! Phần đầu——Ư——quy đầu——\\nhình như, còn——to hơn——lúc nãy, nữa.」"
"1270" = "「A——Fua——ngón tay, của anh Soutetsu——\\nthô ráp——thích quá——vừa to, vừa ấm.」"
"1279" = "「Kyafuuuuuuuu!!」"
"1280" = "「Hiu!!!!!」"
"1283" = "「A! Ưm! Kyu!! A! A! Fua!\\nA! Không được! Em! Thế này, không được đâu!!」"
"1310" = "「Ưm! Yuuuuuuuuuuuuuuuun!」"
"1379" = "「Em chỉ định một chút thôi, nên đã tháo cúc áo ở ngực ra……\\nƯm——không hiểu sao——lại không thể dừng lại được nữa——Fu, a.」"
"1432" = "「Fu——kami——nới lỏng ra, cho anh——aa!!」"
"1457" = "「Fa——a——sướng, quá——sướng quá đi\\n——ưm——a——nhưng mà——nhưng mà——ưm…… a.」"
"1458" = "「Ha——a——Fu, a——anh——Soutetsu——\\nưm——thế này——em——sốt ruột, lắm——a!」"
"1460" = "「Ha…… a——Fau…… ưm——ehehe——\\nanh Soutetsu——của em, anh Soutetsu của em.」"
"1461" = "「Fua…… a…… ư…… vậy, sao, ạ?」"
"1463" = "「Fua——ưm——vui quá——hạnh phúc quá——\\nấm áp quá——anh Soutetsu——em cảm nhận được, rất rõ.」"
"1464" = "「Fa! A! A! A!」"
"1465" = "「Fuaa! Đến rồi, đến rồi! Dương vật! Ưm——\\nĐóng dấu——ngoáy ngoáy——, vào tận cùng, bên trong——âm đạo.」"
"1467" = "「Fa! A! Tuyệt quá! Tử cung——âm đạo——\\ntinh trùng——thật nhiều, ực ực——em, đang nuốt.」"
"1468" = "「Fa! A! Soutetsu! Anh! A!\\nEm! Em! Âm đạo! Sắp, sắp!」"
"1469" = "「Fa! Đột nhiên! Đột nhiên, như vậy! Như vậy,\\nưm, hự! A! Mạnh quá! Mạnh quá đi!!」"
"1471" = "「Fa! Chỗ này——chỗ này, thích quá——ưm!!」"
"1472" = "「Fua! Dương, vật, của anh Soutetsu\\n——ưm! Âm đạo——âm đạo——đã lấp đầy, rồi.」"
"1655" = "Nói đúng hơn là, Fukami càng khít hơn.\\nKhao khát tinh dịch hơn nữa, em ấy siết chặt lấy tôi, kyun kyun."
"1920" = "(Guchuuuuuuuuuuuuu! ——Cụp!)"
"1949" = "(Kyuuuu!! Kyu!)"
"1966" = "(Kyuuuuuuu!!)"
"1967" = "(Gichuchu! Kyuu! Kyuun!!)"
"1968" = "(Kyun!)"
```

## Kết bài

File lr_ふかみh1_ふかみうさぎのたまご.txt.toml: 289 dòng đã đọc hết, **33 dòng rên đổi (21 romaji fa/fu + 9 đếm nguyên âm + 1 mất tiếng thở + 1 sai âm + 1 mất độ dài)**. Lỗi hệ thống lớn nhất: toàn bộ 21 dòng fa/fu của audit dùng "phà"/"phù"/"phuê" — đã chuyển hết sang romaji theo quy tắc fallback (không còn dòng fa/fu nào diễn "phà"/"phù" trong file). Ngoài ra bắt thêm 3 lỗi audit bỏ sót: 1280 ひうっ mất glide "u", 1432 ぁあっ mất 1 âm "a", 1655 きゅんきゅん thừa 1 "u" mỗi token. Không đụng 16/17 dòng gasp Ư của audit (1268 chỉ đổi phần fa, giữ Ư), không dòng "Kh" nào bị đổi, không có cười nào bị diễn thành rên. Bộ CSV tốt là 11_Other (bộ 07_Nagi_Fukami STALE). TOML không có bản trùng. Không có câu hỏi mới nào cần Hieu quyết từ file này.
