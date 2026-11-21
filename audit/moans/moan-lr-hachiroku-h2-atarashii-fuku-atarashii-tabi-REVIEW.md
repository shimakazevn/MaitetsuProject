# Moan-fix: lr_ハチロクh2_新しい服。新しい旅.txt.toml (01_Hachiroku)

- File: `lr_ハチロクh2_新しい服。新しい旅.txt.toml` — route 01_Hachiroku, 327 dòng script, audit trước đó 63 sai.
- TOML md5: `7b0a3c5d1db89046c9b50bee2ff0e6f5` (khớp md5 audit), không có bản trùng (md5 duy nhất trong 227 file TOML).
- CSV3: 1 bộ duy nhất (`translation_toml\01_Hachiroku`), 327 dòng, 0 key trùng. TOML vs CSV3 khác 173 key — toàn bộ là `\n` bị flatten thành khoảng trắng trong TOML-2 (đúng như audit đã ghi); CSV3 là chuẩn.
- Đã đọc 327/327 dòng; xét 133 dòng rên/SFX; đổi 20 dòng, giữ 113 dòng.

## §1. Kiểm kê rên (133 dòng xét, theo loại)

- Họ fa/fu (ふぁ/ふあ): 14 dòng trong chuỗi rên 1410–1443 — toàn bộ diễn "Haa/Haaaa" (la-tinh hoá, mất phụ âm f) → đổi sang romaji Fa/Fua (Hepburn chặt: ふぁ→Fa, ふあ→Fua; tiền lệ lr-h1, h7, 凪h2). Đây chính là 14 dòng audit §9.1 đã cờ cho đợt thống nhất.
- Họ ひあ/ひゃ/ひゅ: 5 dòng (1407, 1408, 1410, 1411, 1496) — 1407/1408/1411 audit đã sửa đúng "Hyau" (+Ư gasp), giữ; 1410 ひあっ→"Hia" (tiền lệ 凪h2: ひあ→"Hia"); 1496 đếm đúng, giữ.
- Gasp Ư (sweep + audit §2b): 32 dòng — 17 sweep + 12 audit mới + 3 already-rendered (1104, 1720, 2103) — KHÔNG đụng dòng nào (trừ 1410/1429/1433 đổi token fa/fu bên cạnh, giữ nguyên Ư của audit).
- Tiếng cười: 7 dòng (1423, 1424, 1447, 1508, 1511, 1547, 1606) — audit đã sửa đúng Nfufu/Ufufu/Fufu, giữ (chỉ 1424 đổi token fa ở dòng 1).
- Rên tách mảnh / sai âm: 1453, 1466, 1473 (gộp thành một cách diễn romaji), 1484 (くっ→"Ku"), 1567 (gasp tuyệt đối-cuối dòng audit sót).
- SFX dài trong ngoặc: 1715 (れるううううううっ→"Reruuuuuuu", 7 u).
- Chuỗi SFX miệng + SFX độc thoại: giữ theo quy ước file (xem §4).

## §2. Sửa romaji họ fa/fu (14 dòng)

Quy tắc romaji (Hieu 21/11 ~01:56): "Haa/Haaaa" mất hẳn phụ âm f của ふぁ/ふあ và nghe ngượng khi đọc dài — dùng romaji Hepburn chặt. Đếm nguyên âm theo công thức (1 + số う/ぅ; với ぁ/あ đếm trực tiếp số mora a).

- **1410** [ハチロク] JP: 「ひあっ！　んっ！　ふあっ！　ゆぅんっ！！！」 / TW: 「呀！嗯！呼啊！嗚嗚！！！」 / Cũ (audit): 「Hya! Ưm! Haa! YuunƯ!!!」 / Mới: 「Hia! Ưm! Fua! YuunƯ!!!」 — ひあっ→"Hia" (tiền lệ 凪h2); ふあっ→"Fua"; giữ Ư gasp + "Yuun" của audit (ゆぅん = 2 u, đúng).
- **1424** [ハチロク] JP: 「ふぁ――あ……あ……ん――。\nふっ――うふっ――うふふふふっ」 / TW: 「呼啊……啊……啊……嗯……呼……嘿嘿……哎嘿嘿」 / Cũ (audit): 「Haa——a……a……ưm——.\nHư——Ufu——Ufufufufu」 / Mới: 「Fa——a……a……ưm——.\nHư——Ufu——Ufufufufu」 — chỉ đổi ふぁ→"Fa"; dòng cười của audit giữ nguyên.
- **1425** [ハチロク] JP: 「ふぁ……ぁ――あ…………ふぁぁ……」 / TW: 「呼啊……啊、啊……呼啊……」 / Cũ: 「Haa……a——a…………haaa……」 / Mới: 「Fa……a——a…………Faa……」 — ふぁ→"Fa" (1 a, cũ "Haa" thừa 1 a); ふぁぁ→"Faa" (2 a, cũ "haaa" thừa 1 a).
- **1427** [ハチロク] JP: 「ふぁ――あっ！　はいっ――はいっ、双鉄さまっ――\nわたくしの――わたくしだけの――[マイ・マスター,4]愛しいお方」 / TW: 「呼啊、啊！好、好，雙鐵少爺……我的……只屬於我的……我至愛的主人」 / Cũ: 「Haa——a! Vâng——vâng, ngài Soutetsu——\nngười——người yêu dấu——của riêng em」 / Mới: 「Fa——a! Vâng——vâng, ngài Soutetsu——\nngười——người yêu dấu——của riêng em」 — chỉ đổi ふぁ→"Fa"; あっ giữa dòng giữ "a" theo ranh giới gasp.
- **1428** [ハチロク] JP: 「ふぁああああん！！！」 / TW: 「呼啊啊！！！」 / Cũ: 「Haaaaan!!!」 / Mới: 「Faaaaan!!!」 — ふぁ+ああああ = 5 a + ん; đếm cũ đã đúng 5 a, chỉ đổi phụ âm H→F. (Kiểm tra bằng máy bắt được bản nháp thừa 1 a — đã sửa trước lượt soát 2, xem §6.)
- **1429** [ハチロク] JP: 「ふあっ！　あっ！　あひっ！　あひゅっ！！！」 / TW: 「呼啊！啊！啊呼！啊唔！！！」 / Cũ (audit): 「Haa! A! Ahi! AhyuƯ!!!」 / Mới: 「Fua! A! Ahi! AhyuƯ!!!」 — chỉ đổi ふあっ→"Fua"; giữ Ư của audit.
- **1432** [ハチロク] JP: 「ふぁっ！　あっ！　あっ！　あうっ！　あっ！\nあついのっ！　たくさん、そうてつ、さまのっ！」 / TW: 「呼啊！啊！啊！啊嗚！啊！滾燙的液體！射出了好多，都是您的，精液！」 / Cũ: 「Haa! A! A! A ư! A!\nNóng quá! Thật nhiều, của ngài, Soutetsu!」 / Mới: 「Fa! A! A! Au! A!\nNóng quá! Thật nhiều, của ngài, Soutetsu!」 — ふぁっ→"Fa"; あうっ→"Au" (một âm duy nhất, cũ tách "A ư").
- **1433** [ハチロク] JP: 「ふぁ！　あっ！　あっ！　あっ！！！」 / TW: 「呼啊！啊！啊！啊！！！」 / Cũ (audit): 「Haa! A! A! AƯ!!!」 / Mới: 「Fa! A! A! AƯ!!!」 — chỉ đổi ふぁ→"Fa"; giữ Ư của audit.
- **1434** [ハチロク] JP: 「ふあっ！　あっ！　あっ！　あっ！　双鉄、さまっ！　\nわたくしのっ、いとしいっ――んっ、だんな、さまっ！」 / TW: 「呼啊！啊！啊！雙鐵，少爺！我摯愛的——嗯，夫君！」 / Cũ: 「Haa! A! A! A! Ngài, Soutetsu!\nNgười phu quân——ưm, yêu dấu, của em!」 / Mới: 「Fua! A! A! A! Ngài, Soutetsu!\nNgười phu quân——ưm, yêu dấu, của em!」 — chỉ đổi ふあっ→"Fua".
- **1436** [ハチロク] JP: 「ふあっ！　あっ！　ひもひひっ――そうへふ、はまっ！\nんっ！　わらくっ、わたくしっ、これ、しゅごっ――！」 / TW: 「呼啊！啊！好酥胡……雙鐵，少爺！嗯！我，我……這樣，好厲害！」 / Cũ (audit): 「Haa! A! Sướng quá——ngài Soutetsu!\nƯm! Em, em, cái này, sướng quá——!」 / Mới: 「Fua! A! Sướng quá——ngài Soutetsu!\nƯm! Em, em, cái này, sướng quá——!」 — chỉ đổi ふあっ→"Fua"; giữ nguyên fix nghĩa của audit (§4).
- **1438** [ハチロク] JP: 「ふあっ！　うれひっ――しゅき、らいしゅき、\nそうてつさまっ！　そうてつ、さまぁ！！」 / TW: 「呼啊！我好高興……雙鐵少爺，雙鐵少爺，我喜歡您，我愛您！！」 / Cũ: 「Haa! Vui quá——thích, cực kỳ thích,\nngài Soutetsu! Ngài Soutetsu!!」 / Mới: 「Fua! Vui quá——thích, cực kỳ thích,\nngài Soutetsu! Ngài Soutetsu!!」 — chỉ đổi ふあっ→"Fua".
- **1440** [ハチロク] JP: 「ふぁっ！　あらま、タブレット、ぜんぶ、おかひく――\nまっひろになるっ、んっ！　チカチカって、しへっ」 / TW: 「呼啊！腦袋、操作板，都變得，不正常了……全部一片空白，嗯！似乎要，火星四濺！」 / Cũ (audit): 「Haa! Chết mất, máy tính bảng, kỳ lạ hết rồi——\nTrắng xóa mất, ưm! Chớp nháy, liên tục」 / Mới: 「Fa! Chết mất, máy tính bảng, kỳ lạ hết rồi——\nTrắng xóa mất, ưm! Chớp nháy, liên tục」 — chỉ đổi ふぁっ→"Fa"; giữ fix thuật ngữ "máy tính bảng" của audit.
- **1442** [ハチロク] JP: 「ふぁああっ！　それっ、しゅきっ！\nきもちい――きもちいい――きもちいいっ！！」 / TW: 「呼啊！這樣動，正好！好舒服，好舒服，好舒服啊！」 / Cũ: 「Haaaa! Đúng rồi, thích lắm!\nSướng——sung sướng——sung sướng quá!!」 / Mới: 「Faaa! Đúng rồi, thích lắm!\nSướng——sung sướng——sung sướng quá!!」 — ふぁああ = 3 a (cũ "Haaaa" thừa 1 a) → "Faaa".
- **1443** [ハチロク] JP: 「ふぁぁああああっ！！？」 / TW: 「呼啊！！？」 / Cũ: 「Haaaaa!!?」 / Mới: 「Faaaaaa!!?」 — ふぁ+ぁ+ああああ = 6 a (cũ 5 a, thiếu 1) → "Faaaaaa".

## §3. Rên tách mảnh / sai âm / gasp / SFX dài (6 dòng)

- **1453** [双鉄] JP: 「うぁあああ！」 / TW: 「唔啊啊！」 / Cũ: 「Ư aaaa!」 / Mới: 「Uaaaa!」 — một âm duy nhất (u + 4 a), cũ tách thành "Ư" + "aaaa"; gộp thành romaji (tiền lệ ふかみh1: gộp mảnh rời của một âm rên).
- **1466** [ハチロク] JP: 「あむっ――じゅずっ！　れろおおっ――はむっ、はむっ、\nじゅぶっ！　じゅぼっ！　じゅびゅっ！　じゅぶっ！！」 / TW: 「啊、啾！溜、啊唔、唔、啾噗！啾啪！啾嚕！啾噗！」 / Cũ: 「A ưm——chụt! Liếm——a ưm, a ưm,\nchụt! Chụt! Chụt! Chụt!!」 / Mới: 「Amu——chụt! Rerooo——Hamu, Hamu,\nchụt! Chụt! Chụt! Chụt!!」 — あむっ→"Amu" (cũ "A ưm" tách + thêm m của ん); れろおおっ→"Rerooo" (3 o: ろ+おお; cũ "Liếm" mất hẳn âm — tiền lệ Paulette h3 966 れろおおおっ→"Reroooo"; れるっ ngắn mới giữ "liếm" theo audit 1716); はむっ→"Hamu" ×2 (cũ "a ưm" mất phụ âm h + tách); chuỗi chụt giữ theo quy ước SFX thoại của file.
- **1473** [ハチロク] JP: 「ぁうっ――だめ、です。動いては――双鉄さま」 / TW: 「啊嗚，不行，雙鐵少爺……您不可以亂動」 / Cũ: 「A ưm——không được, đâu. Ngài đừng cử động——ngài Soutetsu」 / Mới: 「Au——không được, đâu. Ngài đừng cử động——ngài Soutetsu」 — ぁうっ = a+u, một âm duy nhất → "Au"; っ giữa dòng có "——" sau diễn ngắt, không thêm Ư (theo ranh giới gasp của audit §2b; audit §9.3 cũng liệt kê dòng này vào nhóm chờ — quyết theo quy tắc, ghi cờ F3).
- **1484** [双鉄] JP: 「くっ！！！」 / TW: 「嗚！！！」 / Cũ: 「Ưm!!!」 / Mới: 「Ku!!!」 — く là phụ âm thật, không phải gasp っ trần; "Ưm" mất hẳn âm k (tiền lệ Paulette h3 906 くっ→"Ku", parent đã giữ + cờ rà lại ở đợt thống nhất). Audit §8 file này từng giữ "Ưm" — xem cờ F1.
- **1567** [ハチロク] JP: 「ふたりっ、一緒にっ、おんなじ、ようにっ――ぁっ\n一番っ、きもちっ、よくなるっ、ため、にっ――！」 / TW: 「我們會一起，以相同的，節奏……啊，為了獲得，至高的，快感……！」 / Cũ: 「Hai người, cùng nhau, giống, nhau——a\nĐể, trở nên, sung sướng, nhất——!」 / Mới: 「Hai người, cùng nhau, giống, nhau——aƯ\nĐể, trở nên, sung sướng, nhất——!」 — ぁっ ở cuối tuyệt đối dòng 1 trên từ âm thanh, っ mất hoàn toàn trong VN cũ; thêm Ư theo đúng mẫu audit §2b (1470 「ぁぁぁぁぁあああっ」→"AaaaaaƯ", 1463, 1527) — audit sót dòng này, sweep cũng không liệt kê.
- **1715** [ハチロク] JP: 「（れるううううううっ）――きゅぷっ！　ちゅぱっ――\nじゅぼっ！　じゅっ！　じゅぶっ！　ぶっ！　じゅち！」 / TW: 「（呲溜————）啾噗！啾啪、啾噗！啾！啾噗！噗！啾溜！」 / Cũ: 「（Liếm————）——Chụt! Chụt——\nChụt! Chụt! Chụt! Phụt! Chụt!」 / Mới: 「（Reruuuuuuu）——Chụt! Chụt——\nChụt! Chụt! Chụt! Phụt! Chụt!」 — chỉ đổi phần trong ngoặc: れる+6う = 7 u → "Reruuuuuuu" (tiền lệ Paulette h3 968 れるうううううっ→"Reruuuuuu" 6 u; audit §5 đã diễn âm dài trong ngoặc ở 1714/1716, còn 1715 audit sót); dòng thoại giữ "Chụt/Phụt" theo quy ước file.

## §4. Giữ nguyên có chủ đích (113 dòng)

- **Gasp Ư khóa — không đụng (29 dòng):** sweep 17 (1414, 1415, 1416, 1417, 1418, 1456, 1457, 1458, 1459, 1462, 1474, 1483, 1557, 1583, 1681, 2009, 2109) + audit §2b 12 (1105, 1407, 1408, 1411, 1463, 1470, 1472, 1486, 1527 — và 1410/1429/1433 chỉ đổi token fa/fu, giữ Ư). Đã kiểm chứng lại sweep trực tiếp: 20 mục (17 fix + 1104 already-rendered + 1720/2103 needs-file-audit đã được audit giải quyết, giữ).
- **Already-rendered (3):** 1104 「――っ」→"——Ưm", 1720 「～～～～～～～～っ」→"~~~~~~~~ưm", 2103 「――っ。」→"——ư." — gasp đã diễn bằng cách khác, giữ.
- **Cười (7):** 1423 "Nfufu", 1447/1508/1511/1547/1606 "Nfufu/Ufufu/Fufu" — audit §3 đã sửa đúng theo quy tắc Hieu + TW (嘻嘻/呵呵), giữ.
- **Đếm nguyên âm đã đúng (2):** 1495 んふううううううっ (7う) → "Ưm huuuuuuu" (8 = 1+7 ✓); 1496 んひゅうううううううっっっっ (7う) → "Ưm hyuuuuuuu" (8 ✓) — audit §8 đã kiểm chứng, giữ.
- **Chuỗi hơi thở mềm (24):** 1326, 1355, 1464, 1488, 1490, 1491, 1497, 1498, 1501, 1541, 1641, 1655, 1663, 1451, 1452, 1460, 1461, 1467, 1471, 1482, 1485, 1500, 1525, 1526 — んっ/くっ giữa chuỗi hơi thở diễn "ưm/ư" mềm; くっ ở đây là đuôi chuỗi, không phải tiếng độc lập như 1484. Audit §8 giữ.
- **Chuỗi SFX miệng thoại (8):** 1475, 1476, 1477, 1479, 1481, 1714, 1716, 1718 — diễn bằng từ SFX Việt "chụt/phụt/liếm" (1714/1716/1718 audit đã sửa phần ngoặc; dòng thoại giữ). 1477 じゅぶううううううっ→"Chụtttttt" giữ theo phong cách lặp phụ âm (tiền lệ lr_ふかみh1). Xem cờ F2 về ちゅむっ/ちゅるっ/ぺちゃっ diễn "chụt".
- **SFX độc thoại trong ngoặc — khối 2166–2210 (29 dòng):** giữ nguyên theo quy ước file audit §8 ("Phập/Phụt/Chụt", "Siết chặtttttt", "Xoa nắn/Vuốt ve/Bóp chặt" cho nhóm tay 2190–2196). Ghi chú: 2178 （とろおおおおおおおおおっ）→"（Phụt）" — TW 噗啾 ủng hộ âm phụt, audit giữ; 2202/2209 giữ phong cách lặp phụ âm. Xem cờ F4.
- **Hơi thở ふーっ (2):** 1905, 2056 → "Phù——" — audit §8 giữ.
- **Khác:** 1449 ふえっ→"Hả!?" (câu cảm thán ngạc nhiên, diễn nghĩa tự nhiên, không phải rên); 1320 + 1674–1680 すずっ→"Suzu" (っ trên tên riêng là nhấn mạnh); 1412 ぅ……ぁ→"Ư……a"; 1504 ああ→"Aa"; 1548 とっ→"với" (từ nối, không phải âm); 1652 あの→"ừm" (từ đệm).
- **Không dòng "Kh" nào bị đổi.** File không có dòng "Kh" cho っ (kiểm tra: 0 dòng VN chứa "Kh" liên quan gasp).
- **Quy tắc họ ひゃ (quyết 21/11 ~11:55, kiểm chứng lại khi viết review):** ひゃ/ひゅ/ひあ/きゃ trong dòng rên phải là romaji, "Á" là lỗi mất âm. File này KHÔNG còn dòng "Á" nào cho họ này: 1407/1408/1411 "Hyau" (audit), 1410 "Hia" (fix ở đây), 1429 あひゅっ→"Ahyu", 1496 んひゅう→"Ưm hyuuuuuuu". Các きゅ trong SFX không phải rên (1715 きゅぷっ→"Chụt", 2195 きゅむっ→"Bóp chặt", 2202 きゅううう→"Siết chặtttttt") giữ theo quy ước SFX của file — xem cờ F2/F4.

## §5. Cờ cho đợt thống nhất / vòng audit (không tự quyết)

- **F1 — 1484 くっ→"Ku" vs audit giữ "Ưm":** audit §8 liệt kê 1484 vào nhóm "んっ/くっ → Ưm/ư: giữ". Moan quyết theo tiền lệ Paulette h3 906 (く là phụ âm thật → "Ku", parent đã giữ + cờ rà lại). Cần chốt thống nhất toàn dự án: くっ độc lập → "Ku" hay giữ "Ưm".
- **F2 — Chuỗi SFX miệng 1475/1476/1479/1481 diễn "chụt/liếm":** 1475 ちゅむっ/ちゅるっ/ぺちゃっ đều → "chụt"; 1479 じゅにゅっ/じゅぬっ → "Chụt"; 1481 じゅむっ → "Ưm!"; 1715 きゅぷっ → "Chụt!" (dòng thoại). Tiền lệ h9/Paulette h3 sửa ちゅむっ→"chumu", ちゅるっ→"churu", nhưng file này có quy ước SFX thoại "chụt/liếm" mà audit giữ (1716/1718 dòng thoại). Cần quyết: giữ từ SFX Việt hay diễn âm romaji (chumu/churu/pecha/jumu/junyu/kyupu). Thêm: 1475 VN tự thêm ngoặc （ ） mà JP không có.
- **F3 — Ranh giới gasp っ―― (1582, 1589):** 1582 「……っ――」 → "……——" và 1589 「ん…………っ――」 → "Ưm…………——" — っ trước ―― cuối dòng, VN không có Ư. Sweep + audit đều bỏ qua; audit §9.3 chỉ liệt kê gasp giữa dòng. Cần vòng audit quyết: っ―― có tính là gasp bị mất không.
- **F4 — SFX độc thoại khối 2166–2210:** giữ theo audit §8, nhưng nhóm tay 2190–2196 diễn bằng động từ (Xoa nắn/Vuốt ve/Bóp chặt) và 2178/2202/2209 giữ phong cách lặp phụ âm — giống cờ h9 ("SFX độc thoại giữ onomatopoeia Việt, chưa áp công thức đếm nguyên âm"). Đợt thống nhất rà lại cùng cờ h9.
- **F5 — Quy ước Fa/Fua chặt vs h8:** file này dùng Hepburn chặt Fa (ふぁ) / Fua (ふあ) — khớp đa số tiền lệ (凪h2, lr-h2, lr_ふかみh1, lr-h1, h7). Khác với h8 đã merge (dùng "Fua" cho cả ふぁ, "Pua" cho cả ぷぁ) — xem cờ F4 của lr-h1. Cần quyết một dạng duy nhất toàn dự án ở đợt thống nhất.
- **F6 — 1473:** audit §9.3 liệt kê ぁうっ vào nhóm gasp chờ; moan quyết "Au——" (っ giữa dòng có "——" sau diễn ngắt, không thêm Ư) theo ranh giới gasp audit §2b. Ghi lại để đợt thống nhất rà.

## §6. Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 20 giá trị fix đối chiếu JP (+TW) lần 2, sau khi ráp JSON/TOML: **tổng 20 / kiểm chứng lại 20 / gỡ bỏ 0 / sửa lại 0**.

Trước lượt soát 2, kiểm tra đếm nguyên âm bằng máy đã bắt 1 lỗi: 1428 bản nháp "Faaaaaan" thừa 1 âm a (6 a, JP ふぁああああん = 5 a) — đã sửa thành "Faaaaan" (5 a) trước khi soát 2. Các đếm khác kiểm chứng bằng máy đều đúng: 1443 6 a, 1442 3 a, 1425 1 a/2 a, 1715 7 u, 1466 3 o, 1453 4 a.

## §7. Kiểm chứng kỹ thuật

- JSON: 20 mục, dạng chuẩn list-of-dicts, key chuỗi, đủ 7 trường (key/jp/tw/old_vn/fix/kind/character); jp/tw/old_vn khớp CSV3 20/20 (lấy trực tiếp từ CSV3).
- Diff-sanity: mọi fix chỉ khác giá trị cơ sở (fix audit nếu có, không thì VN cũ) ở đúng token rên — kiểm bằng difflib; không viết lại toàn dòng. 6 key trùng audit (1410, 1424, 1429, 1433, 1436, 1440) chỉ khác giá trị audit ở đúng token rên — áp MỘT giá trị moan mỗi key, không áp cả hai. 14 key còn lại xây từ VN cũ.
- Khối TOML: parse được (tomllib), 20 key, **0 sai lệch giá trị** so với JSON. Lưu ý định dạng: CSV3/TOML dùng `\n` literal (2 ký tự) làm dấu ngắt dòng trong giá trị — fix giữ nguyên quy ước này (không đổi thành newline thật); khối TOML viết `\\n` để parse về đúng literal `\n`.
- Sweep: 20 mục đã kiểm chứng trực tiếp — 17 fix Ư của audit giữ nguyên, 3 mục còn lại đã diễn rồi (1104, 1720, 2103).
- Không sửa ROUTE-MOANS.md, không gửi file cho Hieu.

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
1410 = "「Hia! Ưm! Fua! YuunƯ!!!」"
1424 = "「Fa——a……a……ưm——.\\nHư——Ufu——Ufufufufu」"
1425 = "「Fa……a——a…………Faa……」"
1427 = "「Fa——a! Vâng——vâng, ngài Soutetsu——\\nngười——người yêu dấu——của riêng em」"
1428 = "「Faaaaan!!!」"
1429 = "「Fua! A! Ahi! AhyuƯ!!!」"
1432 = "「Fa! A! A! Au! A!\\nNóng quá! Thật nhiều, của ngài, Soutetsu!」"
1433 = "「Fa! A! A! AƯ!!!」"
1434 = "「Fua! A! A! A! Ngài, Soutetsu!\\nNgười phu quân——ưm, yêu dấu, của em!」"
1436 = "「Fua! A! Sướng quá——ngài Soutetsu!\\nƯm! Em, em, cái này, sướng quá——!」"
1438 = "「Fua! Vui quá——thích, cực kỳ thích,\\nngài Soutetsu! Ngài Soutetsu!!」"
1440 = "「Fa! Chết mất, máy tính bảng, kỳ lạ hết rồi——\\nTrắng xóa mất, ưm! Chớp nháy, liên tục」"
1442 = "「Faaa! Đúng rồi, thích lắm!\\nSướng——sung sướng——sung sướng quá!!」"
1443 = "「Faaaaaa!!?」"
1453 = "「Uaaaa!」"
1466 = "「Amu——chụt! Rerooo——Hamu, Hamu,\\nchụt! Chụt! Chụt! Chụt!!」"
1473 = "「Au——không được, đâu. Ngài đừng cử động——ngài Soutetsu」"
1484 = "「Ku!!!」"
1567 = "「Hai người, cùng nhau, giống, nhau——aƯ\\nĐể, trở nên, sung sướng, nhất——!」"
1715 = "「（Reruuuuuuu）——Chụt! Chụt——\\nChụt! Chụt! Chụt! Phụt! Chụt!」"
```

## Kết bài

File lr_ハチロクh2_新しい服。新しい旅 — 327 dòng đọc hết, **20 dòng rên sửa**. Lỗi lớn nhất là họ fa/fu: 14 dòng trong chuỗi rên 1410–1443 đều diễn "Haa/Haaaa" mất phụ âm f — đã đưa về romaji Fa/Fua theo quy tắc Hieu phê duyệt (đúng 14 dòng audit §9.1 đã cờ cho đợt thống nhất). Thêm 3 rên tách mảnh gộp thành một cách diễn (1453, 1466, 1473), 1 sai âm (1484 くっ→"Ku"), 1 gasp tuyệt đối-cuối dòng audit sót (1567), 1 SFX dài trong ngoặc audit sót (1715). Giữ 113 dòng — gồm toàn bộ gasp Ư của sweep/audit, tiếng cười audit đã sửa, và khối SFX độc thoại 2166–2210 theo quy ước file. Còn chờ đợt thống nhất: F1 (くっ→"Ku" vs "Ưm"), F2 (chuỗi SFX miệng "chụt" vs romaji), F3 (gasp っ――), F4 (SFX độc thoại), F5 (Fa/Fua chặt vs h8), F6 (1473).
