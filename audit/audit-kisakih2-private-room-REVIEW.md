# Audit — 稀咲h2_プライベートルーム.txt.toml (route 06_Kisaki)

- File: `稀咲h2_プライベートルーム.txt.toml` — route 06_Kisaki, 1 bản duy nhất (không có file trùng).
- Đường dẫn: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/06_Kisaki/#U7a00#U54b2h2_#U30d7#U30e9#U30a4#U30d9#U30fc#U30c8#U30eb#U30fc#U30e0.txt.toml`
- Số dòng script: **323** (Kisaki 88, Soutetsu 66, độc thoại 169). Đọc toàn bộ 323/323 dòng đối chiếu JP + TW từ CSV3.
- Nội dung: cảnh H thứ hai của Kisaki — Kisaki tới phòng riêng của Soutetsu, dạy anh thủ dâm (nhớ tới cô, tự chạm vào mình), hai người làm tình lần hai; xen kẽ là Soutetsu ngạc nhiên vì phòng mình trống trơn (không sách/báo/tivi — "hình thái tối thượng" của người không có ham muốn vật chất) và Kisaki thừa nhận đã cố tình cho anh xem quần lót/vòng ngực.
- **Kết quả: 24/323 dòng sai (7,4%)** — file dịch khá tốt; lỗi tập trung ở thở gấp/moan (17, gồm 9 từ sweep) và 4 SFX trong khối hiệu ứng cuối file.
- CSV3: 1 set duy nhất, 0 khóa trùng, 0 dòng VN trống, 0 dòng VN == TW, 0 dòng VN == JP. TOML khớp CSV3 tuyệt đối modulo hiện tượng đã biết: 165 giá trị TOML đã flatten `\n` literal (164 thành khoảng trắng, 1 thành rỗng ở 1172 vì trước nó đã có khoảng trắng); CSV3 là bản authoritative, fix list lấy theo CSV3.
- TOML md5: `3faad778393314e55d05226b04768417`. Không có bản sao của file này trong 11 nhóm trùng. File có BOM + CRLF (663 dòng CRLF, 0 LF lẻ).
- `[selections]` rỗng. `[characters]`: 1544 'Soutetsu H', 1699 'Kisaki'. `[character_subs]`: 1865 'Soutetsu' — trỏ tới key không có trong `[script]` (script có 1864 rồi 1865 bị nhảy qua 1925); dư thừa vô hại, không tính lỗi (xem cờ).
- Sweep っ: kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` — file này có **9 mục** (1168, 1198, 1201, 1219 raw-tsu; 1389, 1390, 1391 lost-gasp-whole; 1804, 1832 lost-gasp-trailing). Cả 9 giá trị đã kiểm chứng đúng với JP và được nhận nguyên văn.

## Phân loại (24)

| Loại | Số dòng | Keys |
|---|---|---|
| Thở gấp — sweep (nhận nguyên văn) | 9 | 1168, 1198, 1201, 1219, 1389, 1390, 1391, 1804, 1832 |
| Rên/thở gấp — audit tự tìm | 8 | 1134, 1151, 1152, 1154, 1161, 1189, 1218, 1221 |
| Sai nghĩa (meaning) | 3 | 1259, 1616, 1853 |
| SFX | 4 | 1941, 1960, 1961, 1972 |

Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. Không có thẻ %l nào trong file (JP 0, VN 0) — không có lỗi tag.

## §1. Thở gấp — sweep, nhận nguyên văn (9)

### 1168 [稀咲] — raw-tsu ×2
- JP: `「ひゅあっ――っ――～～～～～～～っ！！！」`
- TW: `「咿啊――～～～～～～～！！！」`
- VN cũ: `「Hyu a――っ――~~~~~~~!!!」`
- Fix: `「Hyu a――Ư――~~~~~~~Ư!!!」` — 2 ký tự っ Nhật thô còn sót trong VN; giá trị sweep đã kiểm chứng đúng JP.

### 1198 [稀咲] — raw-tsu ×2
- JP: `「ぁっ――っ～～～～～～～っ！！！」`
- TW: `「啊～～～～～～～！！！」`
- VN cũ: `「A――っ~~~~~~~!!!」`
- Fix: `「A――Ư~~~~~~~Ư!!!」` — như 1168.

### 1201 [稀咲] — raw-tsu ×2
- JP: `「ふっ――っ――つ――ん～～～～～っ！！」`
- TW: `「嗚――嗯――嗯～～～～～！！」`
- VN cũ: `「Fu――っ――tsu――ưm~~~~~!!」`
- Fix: `「Fu――Ư――tsu――ưm~~~~~Ư!!」` — như 1168.

### 1219 [稀咲] — raw-tsu ×2
- JP: `「んきゅっ――っ――はっ――～～～～～っ！！！」`
- TW: `「嗯唔――哈――～～～～～！！！」`
- VN cũ: `「Ưm kyu――っ――ha――~~~~~っ!!!」`
- Fix: `「Ưm kyu――Ư――ha――~~~~~Ư!!!」` — như 1168. (んきゅ giữ "Ưm kyu" theo sweep — quy tắc romaji chỉ khóa ひゃ/ひゅ/ひあ/きゃ, không bao gồm きゅ.)

### 1389 [双鉄H] — lost-gasp-whole
- JP: `「っ！」`
- TW: `「！」`
- VN cũ: `「!」`
- Fix: `「Ư!」` — JP cả dòng chỉ là gasp っ + dấu câu; VN cũ chỉ còn dấu câu.

### 1390 [双鉄H] — lost-gasp-whole
- JP: `「っ！！！」`
- TW: `「！！！」`
- VN cũ: `「!!!」`
- Fix: `「Ư!!!」` — như 1389.

### 1391 [双鉄H] — lost-gasp-whole
- JP: `「っ！！？」`
- TW: `「！！？」`
- VN cũ: `「!!?」`
- Fix: `「Ư!!?」` — như 1389.

### 1804 [monologue] — lost-gasp-trailing
- JP: `僕のペニスに張り付き揉み込み絞ってきてる。\nならば、もう――このまま押し込み続けるだけで――っ！`
- TW: `緊緊包裹我的陰莖，揉搓並壓緊。那――我只要繼續往前推進――！`
- VN cũ: `Nó đang bám chặt, nhào nặn và vắt kiệt dương vật của tôi.\nNếu vậy thì, chỉ cần――cứ thế này tiếp tục đẩy sâu vào thôi――!`
- Fix: `Nó đang bám chặt, nhào nặn và vắt kiệt dương vật của tôi.\nNếu vậy thì, chỉ cần――cứ thế này tiếp tục đẩy sâu vào thôi――Ư!` — JP kết …だけで――っ!; VN cũ giữ dấu gạch nhưng bỏ gasp.

### 1832 [monologue] — lost-gasp-trailing
- JP: `じわりじわり――と進んでいけば――っ！？`
- TW: `要是一點點地――插進去呢――！？`
- VN cũ: `Từng chút, từng chút một――tiến sâu vào――!?`
- Fix: `Từng chút, từng chút một――tiến sâu vào――Ư!?` — như 1804.

## §2. Rên/thở gấp — audit tự tìm (8)

### 1134 [稀咲] — gasp cuối dòng bị mất: はっ
- JP: `「言、言わないでっ――欲しい、な――そういう――\nこと――はっ」`
- TW: `「別、別說了――別說了吧――那種――話――」`
- VN cũ: `「Đừng, đừng nói nữa――đừng nói――những chuyện――\nnhư thế――nữa」`
- Fix: `「Đừng, đừng nói nữa――đừng nói――những chuyện――\nnhư thế――nữa――haƯ」` — JP cuối dòng có はっ (hơi thở "ha" + っ); VN cũ bỏ mất hẳn âm này. Quy tắc gasp: っ gắn vào từ-âm (は) là gasp → diễn "ha" + Ư (tiền lệ はうっ → "HaƯ!?"). TW cũng bỏ mất — JP thắng.

### 1151 [稀咲] — gasp cuối dòng bị mất: んあっ
- JP: `「や……んっ……双、鉄……焦らしちゃ……\nや、だ――んあっ」`
- TW: `「呀……嗯……雙鐵……別逗弄我了……討厭――嗯啊」`
- VN cũ: `「Đừng…… ưm…… anh, Soutetsu…… cứ trêu chọc……\nthế này, ghét――lắm á」`
- Fix: `「Đừng…… ưm…… anh, Soutetsu…… cứ trêu chọc……\nthế này, ghét――lắm ưm áƯ」` — んあっ = ん (Ưm — tiền lệ trong file 1166/1203) + あ (á) + っ (Ư, tuyệt đối cuối dòng, không dấu câu sau). VN cũ "á" làm mất cả ん lẫn っ. TW 嗯啊 (ưm + á) xác nhận cả hai âm.

### 1152 [稀咲] — đếm nguyên âm: ひゃあ → Hyaa
- JP: `「ひゃあうっ！　――んうっ！！？」`
- TW: `「呀啊！　――嗯唔！！？」`
- VN cũ: `「Hya u! ――Ưm u!!?」`
- Fix: `「Hyaa u! ――Ưm u!!?」` — ひゃあうっ = ひゃ + あ + う + っ: ひゃあ có 2 mora-a → "Hyaa" (công thức nguyên âm; tiền lệ moan: ひゃあっ!? → "Hyaa!?"). VN cũ "Hya" chỉ có 1 chữ a.

### 1154 [稀咲] — họ ひゃ → romaji: ひゃう → Hyau
- JP: `「ひゃうっ！？　あっ――んっ――おしっ――\nおしりっ――んっ――ふっ――」`
- TW: `「呀！？　啊――嗯――屁――屁眼――嗯――呼――」`
- VN cũ: `「Hya!? A――ưm――mông――\nmông em――ưm――fu――」`
- Fix: `「Hyau!? A――ưm――mông――\nmông em――ưm――fu――」` — quy tắc họ ひゃ 21/11 (60 tiền lệ trong các file đã merge, gồm ひゃうっ!? → "Hyau!?"). VN cũ "Hya" làm mất mora う.

### 1161 [稀咲] — đếm nguyên âm + gasp cuối dòng: ふきゅうっ / しきゅ、うっ
- JP: `「ふきゅうっ――はっ――奥っ――しきゅ、うっ」`
- TW: `「呼哈――哈――往――裡面來」`
- VN cũ: `「Fu kyu――ha――sâu quá――tử cung, ư」`
- Fix: `「Fu kyuu――ha――sâu quá――tử cung, ưƯ」` — ふきゅうっ: きゅう = 2 mora-u → "kyuu" (công thức nguyên âm 1 + số う); VN cũ "kyu" thiếu 1 u. Cuối dòng しきゅ、うっ: う diễn "ư", っ tuyệt đối cuối dòng không dấu câu → thêm Ư (tiền lệ ぁ──ぅっ → "A──ưƯ.").

### 1189 [双鉄H] — gasp cuối dòng bị mất: ああっ
- JP: `「あっ……ああっ」`
- TW: `「啊……啊啊」`
- VN cũ: `「A…… a a」`
- Fix: `「A…… a aƯ」` — ああっ tuyệt đối cuối dòng, không dấu câu sau; VN cũ "a a" làm mất hẳn っ → thêm Ư (tiền lệ "A, a, a, aƯ").

### 1218 [稀咲] — んひゅ → Nhyu (quy tắc khóa)
- JP: `「んひゅっ――」`
- TW: `「嗯呀――」`
- VN cũ: `「Ưm hyu――」`
- Fix: `「Nhyu――」` — んひゅ → "Nhyu" theo quy tắc khóa 21/11 (んひゅ→Nhyu, んひゅん→Nhyun; 46 tiền lệ). VN cũ "Ưm hyu" trộn VN + romaji, trái quy tắc "một dòng = một cách diễn".

### 1221 [稀咲] — gasp cuối dòng bị mất: んふっ
- JP: `「んふっ」`
- TW: `「嗯唔」`
- VN cũ: `「Ưm fu」`
- Fix: `「Ưm fuƯ」` — んふっ tuyệt đối cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ → thêm Ư (tiền lệ くっふっ → "kufuƯ").

## §3. Sai nghĩa (3)

### 1259 [稀咲] — sai chủ ngữ/giọng: 出してあげる
- JP: `「ボクを思って興奮したら――\nペニスを、ズボンの外に出してあげるんだ」`
- TW: `「想著我而興奮的話――就解開你的褲子，把陰莖掏出來吧」`
- VN cũ: `「Nếu anh cảm thấy hưng phấn khi nghĩ về em――\nThì hãy lôi dương vật ra khỏi quần đi」`
- Fix: `「Nếu anh cảm thấy hưng phấn khi nghĩ về em――\nThì em sẽ lôi dương vật ra khỏi quần cho anh」` — 出してあげる = Kisaki (người nói) lấy ra GIÙM Soutetsu — chủ ngữ là Kisaki, benefactive あげる. VN cũ "Thì hãy lôi…" đổi thành mệnh lệnh cho Soutetsu tự làm — sai chủ ngữ/giọng. TW cũng dịch sai theo hướng này (就解開你的褲子…); JP thắng TW.

### 1616 [monologue] — きゅんきゅん là co thắt, không phải rên
- JP: `おまんこの感触をより詳細に確かめたくて\n腰を回せば、稀咲もきゅんきゅん答えてくれる。`
- TW: `我扭起腰，想將小穴的每一個角落都了解到透徹，稀咲也精神滿滿地回應了我。`
- VN cũ: `Muốn cảm nhận chi tiết hơn về âm hộ của em ấy,\ntôi xoay hông, Kisaki cũng rên rỉ đáp lại.`
- Fix: `Muốn cảm nhận chi tiết hơn về âm hộ của em ấy,\ntôi xoay hông, Kisaki cũng co thắt đáp lại.` — きゅんきゅん ở đây là âm hộ co thắt/đáp lại bằng cơ thể (đi với 腰を回せば), không phải rên thành tiếng. VN cũ "rên rỉ đáp lại" đổi phản ứng vật lý thành rên — sai nghĩa. TW cũng không nói rên.

### 1853 [monologue] — 愛しい bị thêm nghĩa "đáng thương"
- JP: `それが愛しくて可愛らしくて、\n膣の最奥、子宮のドアを叩く亀頭にも力がこもる。`
- TW: `這樣的她太可愛也太惹人疼愛，敲著小穴最深處子宮門的龜頭也多了幾分力氣。`
- VN cũ: `Trông em ấy thật đáng yêu và đáng thương,\nkhiến quy đầu đang gõ vào cánh cửa tử cung ở tận cùng âm đạo cũng thêm phần mạnh mẽ.`
- Fix: `Trông em ấy thật đáng yêu và dễ thương,\nkhiến quy đầu đang gõ vào cánh cửa tử cung ở tận cùng âm đạo cũng thêm phần mạnh mẽ.` — 愛しい = đáng yêu/thân thương, 可愛らしい = dễ thương — không có yếu tố "đáng thương" (thương hại). TW "太可愛也太惹人疼愛" cũng không có thương hại. VN cũ thêm "đáng thương" là bịa nghĩa.

## §4. SFX (4)

### 1941 [monologue] — くちゅっ là tiếng ướt, không phải lạch cạch
- JP: `（くちゅっ）`
- TW: `（咕啾）`
- VN cũ: `（Lạch cạch）`
- Fix: `（Chụt）` — くちゅっ là tiếng ướt nhóp nhép (TW 咕啾); "Lạch cạch" là tiếng lạch cạch của vật cứng — sai hẳn chất âm. Sửa theo họ ちゅっ trong file (1199, 1948 đều "Chụt").

### 1960 [monologue] — đếm nguyên âm: きゅううううう → 6 chữ u
- JP: `（きゅうううううんっ！）`
- TW: `（噗！）`
- VN cũ: `（Kyuuuuuuun!）`
- Fix: `（Kyuuuuun!）` — きゅ + う×5 = 6 mora-u → 6 chữ u (công thức nguyên âm); VN cũ có 7 chữ u. Tiền lệ moan: きゅうううっ → "Kyuuuu" (đếm đúng số u).

### 1961 [monologue] — ぐっ là tiếng gừ, không phải "Kéo"
- JP: `（ぐっ）`
- TW: `（噗）`
- VN cũ: `（Kéo）`
- Fix: `（Gừ）` — ぐっ là tiếng gằn/gừ ngắn; "Kéo" (kéo) không có cơ sở nào trong JP lẫn TW (TW 噗 = tiếng phụt). Sửa theo tiền lệ trong file: 1942 ぐううっ → "Gừ". (Cờ: "Thúc" là cách đọc khác có thể — xem §7.)

### 1972 [monologue] — ふみゅ là giẫm bằng chân, không phải nhào
- JP: `（ふみゅ――しこっ――こしゅっ――もみゅっ）`
- TW: `（揉――捋――捋――揉）`
- VN cũ: `（Nhào――tuốt――cọ――nắn）`
- Fix: `（Giẫm――tuốt――cọ――nắn）` — ふみゅ từ 踏む = giẫm/đạp bằng chân. VN cũ "Nhào" (nhào nặn bằng tay) sai động tác; file này tự dịch ふみゅっ → "Giẫm" (1976), ふみっ → "Đạp" (1989)/"Đạp nhẹ" (1990). TW 揉 (nhào) lẫn ふみゅ với もみゅっ cuối dòng — JP thắng TW.

## §5. Đại từ đã kiểm chứng — giữ nguyên, chờ đợt thống nhất (0 sửa)

Cụm đại từ vợ chồng Soutetsu↔Kisaki trong file này — KHÔNG sửa trong audit, cờ cho đợt thống nhất theo tiền lệ tsuika02/tsuika01 và quyết định 22/11 ~03:32 (quy tắc 19:45 VẪN ÁP DỤNG — "ngữ cảnh vợ chồng" không override; tiền lệ 稀咲h3 giữ bare 双鉄 ngay cả trong cảnh H):
- Kisaki gọi Soutetsu "anh Soutetsu": **29 dòng** (922, 1116, 1117, 1120, 1124, 1136, 1151, 1166, 1184, 1190, 1193, 1205, 1223, 1243, 1246, 1260, 1268, 1282, 1284, 1286, 1299, 1325, 1359, 1374, 1382, 1383, 1384, 1385, 1386 — gồm cả dạng "Anh, Soutetsu" có dấu phẩy và "anh Sou――tetsu" ngắt nhịp); JP luôn là bare 双鉄. Theo quy tắc khóa thì phải bỏ "anh" → bare "Soutetsu" (đã nằm trong sweep 19:45). Lưu ý: 1386 là nhắc tới ngôi thứ ba (JP 双鉄は), không phải xưng hô — vẫn liệt kê để đợt thống nhất quyết cả hai dạng.
- Kisaki xưng hô Soutetsu bằng "anh" độc lập (không kèm tên): **9 dòng** (924, 1160, 1176, 1215, 1244, 1259, 1279, 1317, 1349) — cùng hạng mục với Kisaki キミ "anh" → "cậu" trong quyết định 22/11 ~03:32 (file này không có キミ trong JP).
- Soutetsu tự xưng "Anh": **17 dòng** (915, 932, 933, 1207, 1226, 1230, 1233, 1236, 1265, 1271, 1273, 1275, 1278, 1302, 1313, 1321, 1334) → "Tôi" theo quyết định 22/11 ~03:32. (1295 KHÔNG tính: "Anh/chị muốn tham quan xưởng ạ?" là câu hỏi trích dẫn với người lạ, không phải tự xưng.) Đáng chú ý: độc thoại trong file này đã dùng "tôi" 100% (0 dòng "anh"), nên file đang tự mâu thuẫn giữa độc thoại ("tôi") và thoại ("Anh").
- Soutetsu gọi Kisaki "em": **3 dòng** (933, 1334, 1338); "cô": 0 dòng — 3 dòng này nhập vào hạng mục thống nhất MỚI (quyết định 22/11 ~03:32): Soutetsu→Kisaki "em" → "cô" (tsuika01 9 + tsuika02 6 + file này 3 = 18 dòng).
- Kisaki tự xưng: "em" 21 dòng, "tôi" 0 dòng — nhất quán với ngữ cảnh thân mật toàn file (cảnh H), đúng quy tắc ngữ cảnh (thân mật → "em"), không có gì phải sửa.

## §6. Giữ nguyên có lý do (không tính lỗi)

- **Bare っ → "Ưm"**: 905 「っ――」→"Ưm――", 1177 「っ――っ――っ――っ――」→"Ưm――ưm――ưm――ưm――", 1181 「っ」→"Ưm" — gasp đã được diễn (Ưm là dạng gasp tự nhiên); sweep không cờ các dòng này.
- **っ đã được diễn bằng dấu gạch/dấu câu**: 1153 きゃっ!?→"Kya!?", 1205 双っ――鉄っ――→"Sou――tetsu――", 1188 ふっ――→"fu――", 1220 んふっ――→"Ưm fu――", 1149 はっ――/あっ――→"ha――"/"a――" (tiền lệ khóa: あっ――→"A——").
- **っ nhấn mạnh cuối câu gắn vào từ nội dung/liên từ — không thêm Ư** (tiền lệ chukuni06: けれどっ, ダメばいっ…): 1230 からっ→"đây", 1246 けどっ→"đâu", 1260 からっ→"mất", 1365 それでっ→"vậy nên", 1344 稀咲っ→"Kisaki", 1158/1160 ふふっ→"Fufu" (tiếng cười, không phải gasp).
- **Cụt câu JP được VN giữ cụt hoặc hoàn thiện hiển nhiên theo ngữ pháp**: 932 (mảnh だが giữ nguyên dạng mảnh), 1119 とろとろに→"nhão nhoét rồi", 1190 それほど、ボクが――→"em đã――", 1260 狂っちゃ――からっ→"em sẽ phát điên――mất", 1321 その方が、オナニーよりも→"sẽ tốt hơn là thủ dâm" (so sánh よりも chỉ có thể hoàn thiện là "tốt hơn" — không phải bịa nội dung mới, khác tiền lệ Hibiki h5 1189).
- **1193 không phải lặp thừa**: 「双鉄が、ボクで、オナニー……ん……して、くれて、る」→"…thủ dâm…… vì em…… ưm…… vì em……" — "vì em" thứ nhất = ボクで, thứ hai = benefactive くれてる; cả hai đều có cơ sở JP.
- **1250 "chu pu" giữ nguyên**: ちゅぷっ → "chu pu" — tiền lệ moan đã merge giữ nguyên dạng này cho ちゅぷ(っ); không sửa.
- **1516 VN theo JP, bỏ TW**: TW đọc あの奥 thành 內褲 (quần lót) — sai; VN "Sâu bên trong đó" theo JP đúng.
- **1670 VN theo JP (đọc chữ)**: 会えない時間も、稀咲の体温と居られるように — VN "tôi vẫn có thể ở bên hơi ấm của Kisaki" theo đúng chủ ngữ JP (僕/精液 ở lại với hơi ấm của Kisaki); TW đọc ngược thành "cô ấy cảm nhận hơi ấm của tôi".
- **1984 くっ→"Cọ" giữ nguyên**: SFX một âm tiết mơ hồ; TW 擦 (cọ xát) đồng ý, ngữ cảnh xung quanh là các động tác cọ xát (1982–1983) — không đủ rõ để kết luận sai.
- **1479 "khoái cảm xuất tinh" giữ nguyên**: thêm nhẹ "khoái cảm" vào 至った射精 nhưng không bịa sự kiện mới — cùng loại với các hoàn thiện mảnh đã giữ ở trên.

## §7. Cờ cho Hieu / đợt thống nhất (KHÔNG tự quyết)

- **Cụm đại từ Soutetsu↔Kisaki (58 dòng)**: xem §5 — "anh Soutetsu" 29 + Kisaki "anh" độc lập 9 + Soutetsu "Anh" 17 + Soutetsu→Kisaki "em" 3 → đợt thống nhất (quyết định 22/11 ~03:32: quy tắc 19:45 vẫn áp dụng; "em"→"cô" là hạng mục mới, file này đóng góp 3 dòng).
- **1961 ぐっ → "Gừ" (đã quyết trong audit, nhưng ghi lại cách đọc khác)**: trong khối SFX, ぐっ đứng giữa các tiếng siết (1960 きゅうううううんっ, 1962 きゅむっ/しゅこっ, 1963 きゅううううっ) nên "Gừ" (tiếng gằn gắng sức) hợp hơn "Thúc" (thrust — tiền lệ 1991, nhưng ở đó ngữ cảnh là đâm/thúc). Nếu Hieu thấy ぐっ ở đây là tiếng thúc thì đổi thành "Thúc" trong đợt thống nhất.
- **[character_subs] 1865 'Soutetsu'** trỏ key không có trong `[script]` (như tiền lệ tsuika01: 1961) — dư thừa vô hại, không tính lỗi.
- **B19 / tag sweep vẫn park**: file này không có thẻ %l nào nên không có gì phải chờ B19.

## §8. Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 24 giá trị fix đối chiếu từng JP (lượt soát 2 đầy đủ, không chỉ parse-check):
- Tổng: **24** / Đã kiểm chứng lại: **24** / Loại bỏ: **0** / Sửa lại: **0**.
- Kiểm chứng cơ học (script `build-kisakih2-private-room.py`): JSON 24 mục; khối TOML parse được, 24 khóa, **0 sai lệch giá trị** so với JSON (so sánh chuỗi thô — tomllib parse `\\n` về `\n` literal); jp/tw/old_vn khớp CSV3 tuyệt đối 24/24; mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (diff từng dòng đã in ra kiểm tra).
- Đếm nguyên âm đã kiểm tra lại bằng script: 1152 (ひゃあ = 2 a), 1161 (きゅう = 2 u), 1960 (きゅううううう = 6 u).
- Cơ sở tổng đã tự kiểm chứng với ROUTE-AUDIT.md: **201 file / 9.210 dòng sai** — khớp với cơ sở được giao.

## Khối TOML (đã parse-kiểm chứng: 24 khóa, 0 sai lệch giá trị)

```toml
[script]
"1134" = "「Đừng, đừng nói nữa――đừng nói――những chuyện――\\nnhư thế――nữa――haƯ」"
"1151" = "「Đừng…… ưm…… anh, Soutetsu…… cứ trêu chọc……\\nthế này, ghét――lắm ưm áƯ」"
"1152" = "「Hyaa u! ――Ưm u!!?」"
"1154" = "「Hyau!? A――ưm――mông――\\nmông em――ưm――fu――」"
"1161" = "「Fu kyuu――ha――sâu quá――tử cung, ưƯ」"
"1168" = "「Hyu a――Ư――~~~~~~~Ư!!!」"
"1189" = "「A…… a aƯ」"
"1198" = "「A――Ư~~~~~~~Ư!!!」"
"1201" = "「Fu――Ư――tsu――ưm~~~~~Ư!!」"
"1218" = "「Nhyu――」"
"1219" = "「Ưm kyu――Ư――ha――~~~~~Ư!!!」"
"1221" = "「Ưm fuƯ」"
"1259" = "「Nếu anh cảm thấy hưng phấn khi nghĩ về em――\\nThì em sẽ lôi dương vật ra khỏi quần cho anh」"
"1389" = "「Ư!」"
"1390" = "「Ư!!!」"
"1391" = "「Ư!!?」"
"1616" = "Muốn cảm nhận chi tiết hơn về âm hộ của em ấy,\\ntôi xoay hông, Kisaki cũng co thắt đáp lại."
"1804" = "Nó đang bám chặt, nhào nặn và vắt kiệt dương vật của tôi.\\nNếu vậy thì, chỉ cần――cứ thế này tiếp tục đẩy sâu vào thôi――Ư!"
"1832" = "Từng chút, từng chút một――tiến sâu vào――Ư!?"
"1853" = "Trông em ấy thật đáng yêu và dễ thương,\\nkhiến quy đầu đang gõ vào cánh cửa tử cung ở tận cùng âm đạo cũng thêm phần mạnh mẽ."
"1941" = "（Chụt）"
"1960" = "（Kyuuuuun!）"
"1961" = "（Gừ）"
"1972" = "（Giẫm――tuốt――cọ――nắn）"
```

## Kết bài

File 稀咲h2_プライベートルーム: đọc 323/323 dòng, sai **24 dòng (7,4%)** — sweep 9 (raw-tsu 4, lost-gasp-whole 3, lost-gasp-trailing 2), rên/thở gấp tự tìm 8, sai nghĩa 3, SFX 4. Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Lỗi tập trung ở các gasp cuối dòng bị mất (1134, 1151, 1189, 1221), moan romaji/đếm nguyên âm (1152, 1154, 1161, 1218, 1960) và 4 SFX cuối file (1941, 1960, 1961, 1972). Cụm đại từ vợ chồng Soutetsu↔Kisaki (58 dòng) được giữ nguyên và cờ cho đợt thống nhất (xem §5/§7). Lượt soát 2: 24/24/0/0. Khối TOML 24 khóa parse đạt, 0 sai lệch.
