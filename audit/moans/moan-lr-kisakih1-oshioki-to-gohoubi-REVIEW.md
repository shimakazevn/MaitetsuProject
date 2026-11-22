# Moan-fix: lr_稀咲h1_おしおきとごほうび.txt.toml — 6/297 (moan)

- File: `06_Kisaki/lr_稀咲h1_おしおきとごほうび.txt.toml` (route 06_Kisaki, 297 dòng script; Kisaki trừng phạt Soutetsu vì say rượu kể bí mật vợ chồng cho Paulette; phần lớn file là H-scene, Kisaki chủ động, Soutetsu bị trói tay).
- TOML md5 `439e80f22d9abfcda5843f8d2f2844ca` khớp audit; không có bản trùng; CSV3 1 bộ duy nhất 297 dòng, 0 key trùng; BOM + CRLF; 0 tag %l. Audit đã sửa 60 dòng (gasp 20, nguyên âm 16, đại từ 13, sai nghĩa 5, SFX 5, chính tả 1) — vòng moan xây trên giá trị audit, chỉ sửa rên.
- Đọc 297/297 dòng; xét kỹ 163 dòng ứng viên rên/SFX (quét máy toàn file + đọc tay từng dòng): rên thoại あ/は/ふ/ん/ちゅ/ぢゅ/ず, SFX độc thoại （ ）45 dòng (1685–1729), cười 8 dòng, gasp Ư của audit 20 dòng, hơi thở ふっ 5 dòng, họ fa/fu 9 dòng, họ hya 1 dòng. **Đổi 6 dòng, giữ 157 dòng.**
- Sweep gasp kiểm tra trực tiếp 17/17 mục (`sweep-raw-gasp-wrong.json`): 14 fix + 3 already-rendered — tất cả đã được audit áp dụng (1262 already-rendered SAI đã sửa trong audit); không đụng dòng gasp Ư nào; file không có dòng "Kh" nào; 0 っ thô trong VN sau fix.

## 1. Romaji (2)

### 991 — 稀咲
- JP: 「ふえっ！？　やあっ！　んっ！　もう、ちょっと――\nふあっ！　もうちょっと、だけ、がまん――ねっ！！」
- TW: 「哎？！呀啊！啊嗯，再等一下……蛤啊！再忍一下就好！！」
- VN cũ: 「Hả!? Nha! Ưm! Thêm, chút nữa thôi――\nFua! Thêm một chút, nữa thôi, ráng nhịn――nhé!!」
- VN mới: 「Fue!? Yaa! Ưm! Thêm, chút nữa thôi――\nFua! Thêm một chút, nữa thôi, ráng nhịn――nhé!!」
- Lý do: ふえっ nằm ĐẦU CHUỖI RÊN (tiếp nối やあっ――んっ――ふあっ), không phải thán từ ngạc nhiên độc lập — romaji "Fue" (tiền lệ 日々姫h1 1022, cờ F4 của file đó vẫn chờ parent quyết — xem cờ F1). "Hả" làm mất phụ âm f (ふ là f, không phải h). やあっ → "Yaa" (や+あ = 2 a; tiền lệ 日々姫h1 やっ→"Ya" 5 dòng đã gộp): "Nha" làm mất phụ âm y. TW 呀啊 xác nhận âm "yaa".

### 992 — 稀咲
- JP: 「ふえっ！？　あ！　あっ――ううん――\nなんでも……なんでもない……ただ――うぁっ――」
- TW: 「哎？！啊、啊……沒什麼……什麼都沒有……只是……」
- VN cũ: 「Hả!? A! Á――không――\nkhông có gì……không có gì đâu……chỉ là――ưa――」
- VN mới: 「Fue!? A! Á――không――\nkhông có gì……không có gì đâu……chỉ là――Ư á――」
- Lý do: như 991 — ふえっ đầu chuỗi rên → "Fue" (xem cờ F1). うぁっ → "Ư á" theo mẫu nội file: 1021 ぅあっ → "Ư á", 1034 ぅぁっ → "Ư á" (cùng âm u+a hai mora); "ưa" gộp hai mora thành một âm tiết Việt, phá nhất quán nội file.

## 2. Đếm nguyên âm (4)

### 1023 — 稀咲
- JP: 「あーーーん……（はぷっ）――ちゅっ――ちゅううっ、\nちゅるっ――ずっ――――――（こくっ）――ぷぁっ」
- TW: 「啊嗯……啊嗚……啾、啾嚕……啾嚕……嗚……咕嘟……噗」
- VN cũ: 「Aaaaan……(hapu)――chu――chuuu,\nchuru――zu――――――(koku)――pua.」
- VN mới: 「Aaaan……(hapu)――chu――chuuu,\nchuru――zu――――――(koku)――pua.」
- Lý do: あーーーん = あ + ー×3 = 4 a (cộng ん); VN cũ 5 a, thừa 1 a. Phần còn lại đúng (hapu/chu/chuuu/churu/zu/koku/pua đã kiểm bằng máy).

### 1173 — 稀咲
- JP: 「嬉しい――ね。双鉄……そうてつぅ」
- TW: 「我好開心，雙鐵……雙鐵」
- VN cũ: 「Vui quá――nhỉ. Soutetsu……Soutetsuuu.」
- VN mới: 「Vui quá――nhỉ. Soutetsu……Soutetsuu.」
- Lý do: そうてつぅ = 3 âm u (う trong そう + u trong つ + ぅ); "Soutetsuuu" có 4 u, thừa 1. Tiền lệ: file khác đã sửa そうてつぅっ → "Soutetsuu" (3 u).

### 1263 — 稀咲
- JP: 「ふあっ！　はっ！　あ！　んっ！　うっ！　ねっ？\nねっ！？　でしょ？　双鉄っ！　んっ　そうてつぅ」
- TW: 「蛤啊啊！蛤啊、啊嗯、啊嗚……你懂吧？雙鐵……你懂吧……雙鐵」
- VN cũ: 「Fua! Há! A! Ưm! Ư! Nhỉ?\nNhỉ!? Đúng không? Soutetsu! Ưm, Soutetsuuu.」
- VN mới: 「Fua! Há! A! Ưm! Ư! Nhỉ?\nNhỉ!? Đúng không? Soutetsu! Ưm, Soutetsuu.」
- Lý do: như 1173 — そうてつぅ = 3 u; "Soutetsuuu" thừa 1 u.

### 1708 — monologue
- JP: （ずゆりゅりゅりゅりゅぶびゅぶうぅぅぅぅぅぅ～！）
- TW: （啾嚕嚕嚕嚕嚕！）
- VN cũ (giá trị audit): （Zuyuryuryuryuryububyubuuuuuuu~!）
- VN mới: （Zuyuryuryuryuryububyubuuuuuuuu~!）
- Lý do: JP = 16 u (ずゆりゅ×4 = 6 u; ぶびゅぶ = 3 u; うぅ×6 = 7 u). Audit ghi đúng "16 u" nhưng chuỗi fix chỉ có 15 u (CSV gốc 14 u → audit sửa lên 15, vẫn thiếu 1) — đây là sửa lỗi chép của audit, không phải đổi hướng. Thêm 1 u vào đuôi (7 u → 8 u).

## 3. Giữ nguyên có chủ đích (rên/SFX đã đúng)

- **Gasp Ư (20 dòng audit, đã khóa):** 710/971/972/974/1000/1001/1003/1020/1029/1030/1039/1062/1235/1262/1291/1341/1425/1429/1551/1619 — không đụng dòng nào. Sweep 17 mục đã kiểm trực tiếp, khớp audit.
- **Họ fa/fu (9 dòng):** ふあっ/ふぁ → "Fua" nhất quán cả file (991/1008/1025/1073/1075/1259/1262/1263/1037); 0 dòng "phà"/"phùa" còn lại.
- **Họ hya (1 dòng duy nhất):** 997 きゃっっ → "Kya" ✓; không còn "Á" cho họ ひゃ/ひゅ/ひあ/きゃ trong file (1281/1282 là nói ngọng, xem dưới).
- **"Á" giữ đúng:** 999 ぁっ×4, 1014 あっ×3, 1017 ぁっ/あっ/はっ, 1025 あっ/ああっ, 1261 はっ/あっ×3, 1262/1263/1073/1259 あっ — JP không có phụ âm mora, "Á" đúng.
- **Đếm nguyên âm đã kiểm bằng máy, đúng:** 1011 12 a, 1013 6 a, 1018 6 a, 1025 はああっ 3 a / はぁっ 2 a (theo parent CHỐT 2 a ở lr_ニイロクh F3) / ああっ 2 a, 998/1037 はぁっ/はあっ 2 a, 1043–1064 họ ちゅ/ぢゅ/ず (Juu 2 u, Reryuuuu 4 u, Kyufuuuu 5 u…), 1703–1707/1709 (16 u / 10 o / 13 u / 17 o / 19 u / 11 u), 1720 ぃ×13 → 13 i, 1729 きゅう… = 14 u + "Tokun!" (đã kiểm cả katakana トクン), 1686–1694 toàn bộ token ちゅ/ぢゅ/びゅ (Juba/Jubo/Jubu/Bachu/Sunyu/kuchu/Byu/Byuu/Byuuu…).
- **Cười (8 dòng, đúng quy tắc Hieu 19/11 — cười, không phải rên):** 945/995/1087/1089 ふふっ → "Fufu"; 986/1093/1160 うふふっ → "Ufufu"/"ufufu"; 1095 んふふっ → "Nfufu".
- **Hơi thở ふっ → "phù" giữ (5 dòng):** 710, 978 (ふ～っ×4 → "Phù~"), 986, 1053, 1069 — tiền lệ đa số (reinah2, nhiều file: ふっ ngắn là hơi thở, "phù" đúng âm, không ngượng); chỉ ふあ/ふぁ mới bắt buộc romaji. Xem cờ F4.
- **ん → "Ưm"/"Ưn" giữ:** 1025 んあっ → "Ưn á", 1026 んううっ → "Ưn ư ư", 1162/1259 んうっ → "ưn ư" — quy ước nội file nhất quán (ん trước nguyên âm diễn "Ưn/ưn"); 1027/1065/1076/1077/1185/1296 んっ → "Ưm". Xem cờ F5.
- **SFX （ ） diễn bằng động từ Việt giữ (theo audit + TW đồng ý):** 1685 くっ → "Vạch", 1695 どさっ → "Bịch", 1710 つーっ → "Chọc――", 1712–1719/1727/1728 ぎゅう…/ぎう… → "Véo mạnh" (+ đếm !), 1721 ツネっ → "Véo", 1723 むぎゅっ → "Bóp chặt", 1724 ふるっ → "Lắc lư", 1726 さすっ → "Vuốt ve"; 1720 ぎゅりっ――ぃ×13 → "Véo――iiiiiiiiiiiii" (động từ + kéo dài romaji — xem cờ F3). 1306 （すーっ、はーっ） → "(Hít, thở)" giữ (hơi thở diễn bằng lời Việt tự nhiên).
- **Nói ngọng giữ (không phải dòng rên, quy tắc 3b):** 1281 「ほへははひょふへ、ほうひひ」 → "Hô hê ha ha hyô fư hê, hô hi hi"; 1282 「ほひほひ、はははふぇ」 → "Hô hi hô hi, ha ha ha fê" (kể cả ふぇ → "fê" trong dòng ngọng này).
- **Khác giữ:** 1094 ごろーーーーーーん → "nàoooooo" (diễn nghĩa tự nhiên, audit giữ); 1006/1112/1113 痛っ → "Đau" (từ chỉ đau, không phải rên); 1035 あぐっ → "Agu", 1038 んぎっ → "Ưngi" (audit, đúng); 1021 ぅあっ / 1034 ぅぁっ → "Ư á" (mẫu cho fix 992); 1260 は――ぁ――ぁっ――くっ――あっ → "Há――a――á――kư――á" (くっ → "kư", xem cờ F2).

## 4. Quét cơ học toàn file (bổ sung)

- Quét mọi dòng JP có っ chưa nằm trong audit/sweep: chỉ còn っ trong từ (っていうか, やらかした, ほっとして, スっと…), っ đã diễn (んっ→"Ưm", ちゅっ→"Chu", 痛っ→"Đau", あがっ→"A gá", かはっ→"Kaha"…), っ nhấn mạnh trên tên/từ nội dung (稀咲っ, いいっ, すごくてっ, もうっ――, 今もっ――, 叩いてっ — diễn bằng nghĩa/――, không phải gasp), và SFX động từ (mục trên). 4 dòng kiểm tay riêng: 1584 「――っ痛っ」 → "――á đau" (っ đã diễn "á"); 1457 ほしくってっ, (っ cuối câu trên từ nội dung, TW cũng lược); 1408 今もっ―― (nhấn mạnh, không phải gasp); 1624 叩いてっ！！ (động từ đã diễn). Không còn gasp bị mất nào.
- Quét toàn file bằng máy: ふえ chỉ 991/992; やあ chỉ 991; そうてつぅ chỉ 1173/1263; họ fa 9 dòng đều "Fua"; họ hya 1 dòng "Kya"; token romaji thuần không còn lệch đếm nào ngoài 6 dòng đã sửa (chỉ còn tên riêng "Kisaki" — không phải âm).

## 5. Không sửa (ngoài phạm vi moan)

- Đại từ/terminology/nghĩa của audit (955/1014/1033/1075/1109/1119/1160/1162/1164/1166/1183/1211/1233/1245/1287/1390/1133…) không đụng. Cờ audit giữ nguyên (1183 biên, 1690 Kuchu vs Chụt, 1126 おちんぽ, B19 park).

## 6. Cờ cho parent / đợt thống nhất

- **F1 — ふえっ → "Fue" (991/992):** phán đoán theo tiền lệ 日々姫h1 1022 (cờ F4 của file đó vẫn chờ parent quyết). Nếu parent giữ "Hả" cho thán từ ngạc nhiên thì hoàn 2 dòng này; 1282 ふぇ "fê" trong dòng nói ngọng thì giữ nguyên trong mọi trường hợp.
- **F2 — くっ → "kư" (972/974/1190/1260) vs "ku":** file này dùng "kư" nhất quán; lr_ニイロクh F4 parent giữ "ku" theo ハチロクh6 — chờ quyết chung toàn dự án, không đổi lẻ file này.
- **F3 — SFX （ぎゅ…） dài:** 1720 "Véo――iiiiiiiiiiiii" trộn động từ Việt + kéo dài romaji trong 1 dòng; 1710/1712–1719/1727/1728 "Véo (mạnh)" không đếm nguyên âm, đối lập 1703–1709 romaji thuần có đếm — chờ quyết chung về họ SFX này (cùng họ với lr_日々姫h1 F1).
- **F4 — ふっ → "phù" (710/978/986/1053/1069) vs "Fu":** giữ "phù" theo đa số tiền lệ; ngoại lệ paulette-h3/h9 dùng "Fu" khi cùng nhịp thở với ふあっ — chờ quyết chung (lr_日々姫h1 F2).
- **F5 — ん → "Ưn/ưn" trước nguyên âm (1025/1026/1162/1259):** quy ước nội file nhất quán; nếu chuẩn hoá thành "Ưm" thì đổi cả 4 dòng cùng lúc.
- **F6 — 1708:** audit ghi đúng "16 u" nhưng chuỗi fix chỉ có 15 u — đã sửa theo đúng số audit công bố; parent kiểm lại khi gộp.

## Lượt soát 2

- Đọc lại toàn bộ 6 giá trị sửa đối chiếu JP (+TW) sau khi viết xong: **tổng 6 / tái kiểm chứng 6 / loại bỏ 0 / sửa lại 0**. Kiểm chứng cơ học: JSON 6 mục (key chuỗi); khối TOML parse được (tomllib), 6 khóa, 0 sai lệch giá trị so với JSON; jp/tw/old_vn khớp CSV3 tuyệt đối 6/6 (lấy trực tiếp từ CSV3; 1708 old_vn = giá trị audit); diff-sanity: mọi fix chỉ khác VN cũ ở đúng token rên cần sửa (991: 2 token; 992: 2 token; 1023: 1 nguyên âm; 1173/1263: 1 nguyên âm; 1708: 1 nguyên âm); 0 fix còn っ thô; mọi fix giữ nguyên dấu 「」/（） của dòng gốc; ngắt dòng là `\\n` literal theo chuẩn CSV3.
- Cơ sở tổng: ROUTE-MOANS.md lúc viết snippet là **51 file / 1285 dòng sai (moan)** (đã tự kiểm chứng lại từ file, không dùng cơ sở lúc spawn).

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
"991" = "「Fue!? Yaa! Ưm! Thêm, chút nữa thôi――\\nFua! Thêm một chút, nữa thôi, ráng nhịn――nhé!!」"
"992" = "「Fue!? A! Á――không――\\nkhông có gì……không có gì đâu……chỉ là――Ư á――」"
"1023" = "「Aaaan……(hapu)――chu――chuuu,\\nchuru――zu――――――(koku)――pua.」"
"1173" = "「Vui quá――nhỉ. Soutetsu……Soutetsuu.」"
"1263" = "「Fua! Há! A! Ưm! Ư! Nhỉ?\\nNhỉ!? Đúng không? Soutetsu! Ưm, Soutetsuu.」"
"1708" = "（Zuyuryuryuryuryububyubuuuuuuuu~!）"
```

## Kết bài

File lr_稀咲h1_おしおきとごほうび.txt.toml: 297 dòng đã đọc, 163 dòng ứng viên rên/SFX đã xét kỹ, **đổi 6 dòng (moan)** — romaji 2 (991/992: ふえっ→"Fue", やあっ→"Yaa", うぁっ→"Ư á"), đếm nguyên âm 4 (1023: 5 a→4 a; 1173/1263: "Soutetsuuu"→"Soutetsuu" 3 u; 1708: 15 u→16 u, sửa lỗi chép của audit). File vốn đã sạch về rên nhờ audit dùng romaji nhất quán ("Fua", "Kya", đếm nguyên âm đúng ở hầu hết các dòng); không còn "Á" cho họ hya, không còn "phà"/"phùa", không đụng gasp Ư hay dòng "Kh" (file không có dòng "Kh"). Sweep gasp kiểm tra trực tiếp 17/17 mục, khớp audit. Khối TOML 6 khóa đã kiểm chứng parse, 0 sai lệch. Lượt soát thứ hai: 6/6 tái kiểm chứng, 0 loại bỏ, 0 sửa. 6 cờ cho parent/đợt thống nhất (F1 ふえっ→"Fue", F2 くっ "kư" vs "ku", F3 SFX ぎゅ… dài, F4 ふっ "phù" vs "Fu", F5 ん "Ưn/ưn", F6 1708).
