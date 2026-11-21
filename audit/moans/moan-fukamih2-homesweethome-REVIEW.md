# Moan-fix REVIEW — ふかみh2_homesweethome.txt.toml (07_Nagi_Fukami)

## §1. Xác minh tệp

- **Tệp TOML:** `07_Nagi_Fukami/#U3075#U304b#U307fh2_homesweethome.txt.toml` — md5 `5dee3edcf2470621aa4f3b78c9c0a43b` (khớp md5 audit), BOM + CRLF, `[selections]` rỗng, **không có bản sao trùng** (chỉ 1 copy trong 227 tệp TOML).
- **CSV3:** 2 bộ (301 dòng mỗi bộ) — bộ tốt là thư mục `11_Other` (flat-match VN↔TOML **301/301**; bộ `07_Nagi_Fukami` chỉ khớp 12/301, là bộ stale). Chỉ xét bộ tốt. TOML vs CSV3 khớp 301/301.
- **Đọc:** 301/301 dòng script. Audit file này: 22 dòng sai (gasp Ư 9 + 1 raw っ, đếm nguyên âm 2, đại từ/ý nghĩa 10) — xem §5 về các fix audit KHÔNG đụng tới.
- **Cơ sở tổng:** ROUTE-MOANS.md hiện tại **39 file / 962 dòng sai (moan)** (đã đọc trực tiếp dòng tổng cuối, 21/11 ~20:15) — snippet rebase theo cơ sở này.

## §2. Kiểm kê moan

- **Tổng dòng rên/SFX đã xét: 112** (67 thoại + 45 độc thoại/SFX trong （ ）).
  - Thoại: 745, 747, 748, 749, 968, 970, 971, 972, 973, 975, 977, 981, 982, 983, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1007, 1008, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1020, 1021, 1022, 1024, 1025, 1026, 1027, 1028, 1029, 1031, 1032, 1033, 1034, 1036, 1042, 1043, 1044, 1045, 1067, 1117, 1144, 1163, 1165, 1172.
  - Độc thoại/SFX （ ）: 1361, 1442, 1520, 1555, 1566, 1591, 1721–1726, 1730, 1731, 1733–1747, 1749–1755, 1758, 1761, 1766–1769, 1770, 1772, 1776.
- **Sửa: 19 dòng** — romaji 13 (973, 975, 981, 982, 983, 988, 990, 993, 999, 1025, 1032, 1034, 1043), âm sai/mất phụ âm 4 (1003, 1004, 1013, 1022), đếm nguyên âm 2 (1011, 1555).
- **Giữ: 93 dòng.**
- **Sweep:** kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` — file này có **17 mục** (1442, 1735, 736, 1033, 988, 1043, 1312, 1382, 1440, 1465, 1482, 1512, 1553, 1601, 1605, 1723, 1566). Audit đã giải quyết hết: 1442/1735/1566 sửa trong audit, 736/1312/1382/1440/1465/1482/1512/1553/1601/1605/1723 là false positive, 1033 already-rendered, 988 already-rendered (chỉ xét gasp っ — xem §3 key 988: âm ひひゅっ vẫn sai, sửa ở đây), 1043 fa/fu (sửa ở đây). Quét gasp lại toàn file: không còn gasp nào sót ngoài các fix audit.

## §3. Từng dòng sửa (19)

### 973 — ふあっ → romaji (quy tắc 3)
- JP: 「ひゃっ！？　やっ――双鉄さんっ！？\nパンツ、わたしの、パンツ――食い……込ん――ふあっ」
- TW: 「呀！討厭……雙鐵先生！內褲，我的內褲……你按進來了……啊」
- Cũ: 「Hya!? Ya——anh Soutetsu!?\nQuần lót, quần lót của em——lún……vào——phù ah」
- Mới: 「Hya!? Ya——anh Soutetsu!?\nQuần lót, quần lót của em——lún……vào——fua」
- Lý do: ふあっ (1 âm a) bị tách thành "phù ah" (2 mảnh, không phải dạng khóa "phùa", cũng không phải romaji) — nghe gượng. Romaji "fua" (viết thường giữa dòng theo lối file này). "Hya"/"Ya" đã đúng, giữ. Tiền lệ fukamih1 ふあっ→"Fua!" (cùng dạng cũ "Phù ah", cùng ghi chú audit đưa vào đợt thống nhất dạng "phùa" — bản moan này thay thế ghi chú đó bằng romaji, xem cờ F1).

### 975 — ひあっ → romaji (quy tắc 3b)
- JP: 「ひあっ――あっ――んっ――ん――ふうっ――」
- TW: 「呀，啊，嗯，嗯，呼」
- Cũ: 「Hi ah——ah——ưm——ưm——phù ư——」
- Mới: 「Hia——ah——ưm——ưm——phù ư——」
- Lý do: ひあっ là một âm duy nhất, bản cũ tách thành "Hi ah" (2 mảnh) — "Á"/tách mảnh cho họ ひあ là mất phụ âm mora (quy tắc 3b). Romaji "Hia". Phần còn lại giữ: あっ→"ah", んっ/ん→"ưm", ふうっ→"phù ư" (đã đúng theo quy tắc gasp). Tiền lệ fukamih1 ひあっ→"Hia" (cùng dạng cũ "Hi ah").

### 981 — ふあっ → romaji
- JP: 「ふあっ！」 — TW: 「哇！」
- Cũ: 「Phù ah!」 — Mới: 「Fua!」
- Lý do: như 973 ("Phù ah" tách mảnh, ngượng). Tiền lệ fukamih1 ふあっ→"Fua!" y hệt.

### 982 — ぷあっ → romaji
- JP: 「ぷあっ！！？」 — TW: 「哇？！」
- Cũ: 「Phù ah!!?」 — Mới: 「Pua!!?」
- Lý do: như 973, phân biệt ぷ/ふ (Pua, không phải Fua). Tiền lệ lr-fukamih2 ぷあっ→"Pua".

### 983 — ぱあっ + やぁっ → romaji + đếm nguyên âm
- JP: 「ぱあっ！？　ま、またグイって――んっ！　あ――\nパンツでっ……感じちゃう、とかっ――あっ――やぁっ」
- TW: 「哇？！又、又按……嗯！啊……被內褲……弄出感覺了……啊……不要……」
- Cũ: 「Pa ah!? L, lại ấn mạnh nữa——ưm! A——\nBằng quần lót……mà cũng cảm thấy sướng, sao——ah——ya」
- Mới: 「Paa!? L, lại ấn mạnh nữa——ưm! A——\nBằng quần lót……mà cũng cảm thấy sướng, sao——ah——yaa」
- Lý do: ぱあっ = ぱ+あ = 2 âm a → "Paa" (một hơi duy nhất, không tách "Pa ah"); やぁっ = や+ぁ = 2 âm a → "yaa" (bản cũ "ya" thiếu 1 a). Phần còn lại giữ (んっ→"ưm", あ→"A", あっ→"ah").

### 988 — ひひゅっ bị dịch sai thành "ưm"
- JP: 「ぃ――っ――～～～っ！？　んっ――ふっ――\nふぉっ――ふ――んっ！　んっ――ふっ――ひひゅっ」
- TW: 「唔……唔，唔？！嗯，呼，呼，呼，嗯！嗯，呼，唔」
- Cũ: 「Ư——ư——~~~ư!? Ưm——phù——\nphù——phù——ưm! Ưm——phù——ưm」
- Mới: 「Ư——ư——~~~ư!? Ưm——phù——\nphù——phù——ưm! Ưm——phù——hihyu」
- Lý do: dòng 2 JP có 6 token (ふぉっ, ふ, んっ, んっ, ふっ, ひひゅっ), VN cũ cũng 6 token — token cuối "ưm" ứng với ひひゅっ, tức âm hi+hyu bị dịch thành "ưm" (mất hẳn phụ âm). Romaji "hihyu" (viết thường giữa dòng). Sweep ghi "already-rendered" cho dòng này nhưng chỉ xét gasp っ, không xét token ひひゅっ. Phần đầu giữ (ぃ→"Ư" là gasp, đã ổn định trong chuỗi rên lỏng của file).

### 990 — く→"Ư" là âm sai
- JP: 「く――あっ！」 — TW: 「唔……啊！」
- Cũ: 「Ư——a!」 — Mới: 「Ku——a!」
- Lý do: く là âm "ku" kéo dài (――), không phải gasp — dịch thành "Ư" là sai âm hẳn. "Ku——" (giữ dấu gạch kéo dài). あっ→"a!" giữ (dấu ! diễn độ cắt của っ; tiền lệ fukamih1 giữ "ah"/"a" cho あっ).

### 993 — んきゅんっ mất ん cuối
- JP: 「んきゅんっ！」 — TW: 「唔！」
- Cũ: 「Ưm kyu!」 — Mới: 「Ưm kyun!」
- Lý do: きゅん = kyun (có n cuối) — bản cũ "kyu" bỏ mất ん. Theo mẫu file này ん+X = "Ưm + romaji" (994 "Ưm gu", 1000 "ưm gyu").

### 999 — んきゅっ mất きゅ, んふっ mất ふ
- JP: 「んきゅっ――ん――グッ――んふっ――んっっ！　む」
- TW: 「唔，唔，唔，呼，嗯！唔」
- Cũ: 「Ưm——ưm——hự——ưm——ưm! Ưm」
- Mới: 「Ưm kyu——ưm——hự——ưm fu——ưm! Ưm」
- Lý do: 6 token JP ↔ 6 token VN: んきゅっ→"Ưm" (mất きゅ), んふっ→"ưm" (mất ふ). Theo mẫu file: んむっ→"Ưm mu" (987), んぷっ→"ưm pu" (1000), んぎゅっ→"ưm gyu" (1000) — mora thứ hai luôn được giữ. Sửa thành "Ưm kyu" và "ưm fu". グッ→"hự", ん→"ưm", んっっ→"ưm!", む→"Ưm" giữ.

### 1003 — んむっ mất む
- JP: 「ふっ――んっ――んうっ――んむっ――ムッ～っ！」
- TW: 「唔，嗯，嗯，唔，唔！」
- Cũ: 「Phù——ưm——ưm——ưm——ưm~m!」
- Mới: 「Phù——ưm——ưm——ưm mu——ưm~m!」
- Lý do: token thứ 4 んむっ→"ưm" (mất む); tiền lệ cùng file 987 んむっ→"Ưm mu". んうっ→"ưm" (token 3) giữ — xem cờ F4 (mâu thuẫn với 1033 "ưm ư").

### 1004 — ぐ→"mu" là âm sai
- JP: 「むぐっ！！！？」 — TW: 「唔？！」
- Cũ: 「Ư mu!!!?」 — Mới: 「Ưm gu!!!?」
- Lý do: むぐっ = mu+gu — bản cũ gán "mu" cho ぐ (sai phụ âm). Theo mẫu file: む→"Ưm" (991), ぐ→"gu" (994, 1000).

### 1011 — đếm nguyên âm chuỗi "a" leo thang
- JP: 「あ……あー……あ～っ――あ～～っ！」 — TW: 「啊……哦……噢……噢！」
- Cũ: 「A…… a…… a~—— a~~!」
- Mới: 「A…… aa…… aa~—— aaa~~!」
- Lý do: đếm theo mora: あ=1, あー=2, あ～っ=2, あ～～っ=3 → tổng 8 âm a; bản cũ 1+1+1+2=5. Đây là chuỗi rên leo thang (không phải thở dài/nhận ra như 749/1045 — xem §4), nên áp công thức đếm đầy đủ. Dấu ~~ giữ nguyên kiểu cũ.

### 1013 — はっ mất h
- JP: 「ぁっ――はっ――んっ――んっ――んっ！！」 — TW: 「啊……啊，嗯，嗯，嗯！！」
- Cũ: 「A——a——ưm——ưm——ưm!!」
- Mới: 「A——ha——ưm——ưm——ưm!!」
- Lý do: はっ = ha+っ — bản cũ "a" mất phụ âm h (mất mora, như tiền lệ họ ひゃ). Tiền lệ cùng file: 1020 はっ→"ha", 1021 はうっ→"Ha ư". "ha" viết thường giữa dòng.

### 1022 — はうっ mất h
- JP: 「はうっ！！！！」 — TW: 「啊嗚！！！！」
- Cũ: 「A ư!!!!」 — Mới: 「Ha ư!!!!」
- Lý do: như 1013; mâu thuẫn trong cùng file: 1021 はうっ→"Ha ư" (giữ h), 1022→"A ư" (mất h). Sửa theo 1021.

### 1025 — ふぁ×3 → romaji
- JP: 「ふぁっ――んっ――ぢゅっ――ぢゅちゅるっ――ぐ――\nあっ――ほーへふ、ふぁ――ほーへふ、ふぁんっ！！」
- TW: 「啊，嗯，啾，啾，唔，啊，唔唔唔，唔唔唔！！」
- Cũ: 「Phù a——ưm——chụt——chụt rột——gu——\nAh——ho he fu, phù a——ho he fu, phù an!!」
- Mới: 「Fa——ưm——chụt——chụt rột——gu——\nAh——ho he fu, fa——ho he fu, fan!!」
- Lý do: ふぁっ→"Fa" (1 a, っ ngầm), ふぁ→"fa", ふぁんっ→"fan" — dạng cũ "Phù a"/"phù a"/"phù an" tách mảnh, ngượng (quy tắc 3/5). "ho he fu" cho ほーへふ giữ (nói ngọng miệng đầy, không phải token rên — quy tắc 3b). あっ→"Ah", ぢゅっ→"chụt", ぐ→"gu" giữ.

### 1032 — ぷはっ mất は
- JP: 「ん……ん、ちゅ――ちゅるっ――んっ――――――\nごくんっ……ん～～～――ぷはっ」
- TW: 「嗯……嗯，啾，啾，嗯……咕咚……嗯……噗哈」
- Cũ: 「Ưm……ưm, chụt——chụt——ưm——————\nỰc……ưm~~~——phù」
- Mới: 「Ưm……ưm, chụt——chụt——ưm——————\nỰc……ưm~~~——puha」
- Lý do: ぷはっ = pu+ha+っ — bản cũ "phù" chỉ giữ ぷ, mất hẳn は. TW 噗哈 xác nhận pu+ha. Romaji "puha" (một hơi duy nhất; dạng "Phù ha" tách 2 mảnh như "phù ah" ở 973).

### 1034 — ふぁひ/ふぁん → romaji
- JP: 「ん……ふ、あっ――んっ――ふぁひ……んうっ――んっ、\nほーへふ……ふぁん……うくっ――んっ！」
- TW: 「嗯……好……嗯……好……嗯，嗯，唔唔……嗯……嗯！」
- Cũ: 「Ưm……phù, ah——ưm——phù a hi……ưm ư——ưm,\nHo he fu……phù an……ư ku——ưm!」
- Mới: 「Ưm……phù, ah——ưm——fahi……ưm ư——ưm,\nHo he fu……fan……ư ku——ưm!」
- Lý do: ふぁひ = fa+hi → "fahi"; ふぁん = fan → "fan" — dạng cũ tách mảnh, ngượng. "phù, ah" cho ふ、あっ giữ (2 token riêng, không phải 1 token tách mảnh). うくっ→"ư ku", んうっ→"ưm ư" giữ.

### 1043 — ぷあっ mất あ
- JP: 「ぷあっ」 — TW: 「噗啊」
- Cũ: 「Phù」 — Mới: 「Pua」
- Lý do: ぷあっ = pua+っ — bản cũ "Phù" chỉ giữ ぷ, mất hẳn あ. Romaji "Pua" (phân biệt ぷ/ふ). Audit §4 đã ghi đây là fa/fu dạng cũ chờ thống nhất — bản moan này thay thế bằng romaji (xem cờ F1).

### 1555 — あーん thiếu 1 a + mất ん (độc thoại)
- JP: 「あーんと、ふかみは口を開け、\nその内側を、僕にたっぷり見せつける。」
- TW: 「深美張開嘴，將嘴的內側全部亮給我看。」
- Cũ: 「A~, Fukami há miệng ra,\nphô bày trọn vẹn bên trong cho tôi thấy.」
- Mới: 「Aan~, Fukami há miệng ra,\nphô bày trọn vẹn bên trong cho tôi thấy.」
- Lý do: あーん = あ+ー+ん = 2 âm a + n — bản cũ "A~" chỉ 1 a, mất ん. Tiền lệ fukamih1 ひゃああんんっ→"Hyaaann" (đếm đủ a + n).

## §4. Các dòng rên đã giữ (ghi chú)

- **Romaji đã đúng:** 970 ひゃうっ→"Hya ư", 971 ひゃんっ→"Hyan", 972 やんっ→"Yan!", 973 ひゃっ→"Hya", 977 ひゃっ→"Hya", 993 きゅん (đã sửa n) — họ ひゃ/ひゅ/ひあ không còn "Á" nào sai (chỉ 1067 あっ→"Á" là đúng, vì JP không có phụ âm mora — xem cờ F2).
- **ふっ→"phù" toàn file** (987, 988, 994, 1000, 1003, 1005, 1029, 1036…): giữ theo tiền lệ reinah2 (ふっ→"phù" cả file).
- **ん/む→"ưm"/"Ưm"** (986, 991, 992, 1000, 1012, 1031, 1033, 1117…): giữ. Chuỗi rên lỏng 987/994/1000/1003/1033/1036 giữ nguyên (audit §5) — chỉ sửa các mora bị mất hẳn (999, 1003).
- **"Kh" khóa — KHÔNG đụng (5 dòng):** 989 くっ――あっ→"Kh——ah", 997 むぅ、っ→"ưm, kh", 1017 っ→"Kh", 1731 っぐっ→"kh", 1739 っぐっ→"Kh" (quyết 21/11: "Kh" giữ, không đổi thành Ư).
- **Gasp Ư của audit/sweep — KHÔNG đụng:** các fix audit đã đúng (995, 996, 1007, 1024, 1172, 1442, 1520, 1566, 1591, 1735, 1776) và các gasp Ư đã có sẵn trong TOML (998, 1001, 1042).
- **Đếm nguyên âm đã đúng (kiểm chứng cơ học):** 1028 ぢゅう×12 → "Chụt" + 13 u (1 của ぢゅ + 12), 994 ふううっ→"phù u u" (3 u), 1005 ふうううっ→"phù ư ư ư" (4 u), 1745 ずるううううっ→"Trượt sâu u u u u" (4 u), 1766 きゅううう→"Kyu u u u" (3 u), きゅんん→"Kyun n", 1769 きゅううっ→"kyu u u" (2 u).
- **SFX trong （ ） giữ dạng động từ/từ tượng thanh Việt** (1721 "Trượt", 1722 "Cắn", 1730 "Phập——trượt sâu u u u u", 1738, 1749, 1752 "Kéo", 1755 "Dừng lại", 1770 "Tuột!"): theo tiền lệ reinah2 giữ SFX （ ） dạng Việt; xem cờ F5 về nguyên âm dài.
- **Cười:** file không có ふふっ/うふふ/んふふ; 1361 にへへ→"hì hì" (độc thoại, cười mãn nguyện) giữ.
- **ああ thở dài/nhận ra — GIỮ, không sửa thành "Aa":** 749 「――ああ」→"——Ah" và 1045 「ああ――」→"A——" đều là tiếng thở dài/đáp lời của Soutetsu (không phải rên) — theo tiền lệ lr-hibikifukami-h1 1931 (ああ thở dài giữ "A"/"À"; dạng "Aa" chỉ áp cho ああ trong ngữ cảnh rên). Ngược lại 1011 là chuỗi rên nên sửa đếm (xem §3).
- **"phù, ah" cho ふ、あっ (1034) giữ** — 2 token riêng, không phải 1 token tách mảnh (khác fukamih1 992 ふぁ→"Phù, ah" đã flag).
- **998:** "Ư~~~~~~~~ư" (8 ~ so với JP 7 ~) — lệch dấu ~, không phải nguyên âm; giữ (không đáng sửa).
- **968:** ひっ→"Hi", ぃっ→"i", ふぉっ/ふうっ→"Phù ư" — giữ (mỗi âm đều có diễn đạt; "Phù ư" là dạng chuẩn của file cho ふうっ; ふぉ→"Phù" đã được audit chấp nhận ở 1044).
- **977 んぐっ→"Ưm gu" giữ** — xem cờ F3.
- **1744:** "Phập p p p p p p p p" giữ (audit giữ; số lượng p không kiểm chứng theo công thức nguyên âm).

## §5. Fix audit KHÔNG đụng tới (0 trùng key)

Moan JSON này có **0 key trùng** với `audit-fukamih2-homesweethome-wrong.json` (22 key). Các fix audit giữ nguyên giá trị audit: gasp Ư (995, 996, 1007, 1024, 1172, 1442, 1520, 1566, 1591, 1735), đếm nguyên âm (1044 "Phù u u u u u u u n" — 7 u, 1767 "Kyu u u u u u u n" — 6 u), SFX sai từ (1562), mất âm は (1776 "ha"), đại từ/ý nghĩa (1116, 1455, 1461, 1564, 1579, 1641, 1660, 1759). Không sửa fix audit nào; không đụng thẻ %l đã bỏ (1050, 1073, 1096×2 — chờ đợt quét thẻ, B19).

## §6. Cờ cho đợt thống nhất

- **F1 — fa/fu 6 dòng sửa thành romaji ở đây (973, 981, 982, 1025, 1034, 1043):** quyết 21/11 ~01:55 đã ghi 6 dòng này vào đợt thống nhất dạng "phà"/"phùa" — bản moan này THAY THẾ ghi chú đó bằng romaji theo quy tắc fallback Hieu duyệt 21/11 ~01:56 (dạng cũ "phù ah"/"Phù a" tách mảnh, ngượng). Cần cập nhật mục đợt thống nhất cho file này (bỏ 6 dòng khỏi danh sách "→ phà/phùa"). Tiền lệ: fukamih1 đã thay thế 3 dòng fa/fu tương tự.
- **F2 — あっ diễn không nhất quán trong file:** "A" (1026), "Ah" (1025/1031), "Á" (1067 — đúng cho あ trần), "a" (990/1013) — đều giữ ở đây; có nên thống nhất thành một dạng không?
- **F3 — んぐっ "Ưm gu" (977) vs paulette-h7 "Ngu":** mẫu file này là "Ưm + romaji" (993/994/999/1000/1033) — mâu thuẫn liên file, chờ thống nhất (cùng câu hỏi reinah2 F3 んくっ "Nku" hay "Ưm").
- **F4 — んうっ hai dạng trong cùng file:** 1003 "ưm" vs 1033 "ưm ư" — một trong hai cần thống nhất.
- **F5 — SFX （ ） chưa áp công thức đếm:** 1740 ずぶうううううううッ→"Phập——————" (chỉ gạch dài, không chữ u), 1768 きゅう×10→"Siết chặt" (động từ, mất hẳn âm — trong khi 1766/1767/1769 cùng cụm đều diễn âm kyu), 1726 びゅうっ→"Phụt" (mất u dài), 1741 じゅうぶっ→"Phập" (mất u dài + bu). Cùng câu hỏi reinah2 F4.
- **F6 — 970 って→"mất":** "sẽ có, cảm giác……mất" — って cuối dòng dịch thành "mất" nghe như bịa thêm ý; không phải lỗi moan nên không sửa ở đây — cần kiểm tra ý nghĩa (audit không flag).
- **F7 — 1026 あっ→"A!?" giữ** (gasp diễn bằng !?); 998 lệch 1 dấu ~ — giữ, không đáng sửa.
- **F8 — 1744 "Phập p p p p p p p p" (9 p) so với JP ん×3 + っ×7:** số lượng p chưa đối chiếu công thức — giữ theo audit.

## §7. Lượt soát 2 (bắt buộc)

- **Tổng: 19 / tái kiểm chứng: 19 / bỏ: 0 / sửa: 0.**
- Đọc lại toàn bộ 19 giá trị fix so với JP từng dòng: đếm nguyên âm kiểm chứng độc lập — 983 ぱあっ 2a + やぁっ 2a, 1011 1+2+2+3=8a, 1028 13u, 1555 あーん 2a+n, 1766/1769 đã đúng; token ひひゅっ (988), きゅ (999), ふ (999), む (1003), h (1013/1022), は (1032), あ (1043) đều đã khôi phục; không dòng "Kh" nào bị đổi; không dòng gasp Ư nào bị sửa lại.
- JSON 19 mục, khóa string, jp/tw/old_vn khớp CSV3 (bộ tốt 11_Other) 19/19. Khối TOML parse bằng tomllib: 19 khóa, 0 sai lệch giá trị.

## §8. Khối TOML (đã parse-verified)

```toml
[script]
"973" = "「Hya!? Ya——anh Soutetsu!?\\nQuần lót, quần lót của em——lún……vào——fua」"
"975" = "「Hia——ah——ưm——ưm——phù ư——」"
"981" = "「Fua!」"
"982" = "「Pua!!?」"
"983" = "「Paa!? L, lại ấn mạnh nữa——ưm! A——\\nBằng quần lót……mà cũng cảm thấy sướng, sao——ah——yaa」"
"988" = "「Ư——ư——~~~ư!? Ưm——phù——\\nphù——phù——ưm! Ưm——phù——hihyu」"
"990" = "「Ku——a!」"
"993" = "「Ưm kyun!」"
"999" = "「Ưm kyu——ưm——hự——ưm fu——ưm! Ưm」"
"1003" = "「Phù——ưm——ưm——ưm mu——ưm~m!」"
"1004" = "「Ưm gu!!!?」"
"1011" = "「A…… aa…… aa~—— aaa~~!」"
"1013" = "「A——ha——ưm——ưm——ưm!!」"
"1022" = "「Ha ư!!!!」"
"1025" = "「Fa——ưm——chụt——chụt rột——gu——\\nAh——ho he fu, fa——ho he fu, fan!!」"
"1032" = "「Ưm……ưm, chụt——chụt——ưm——————\\nỰc……ưm~~~——puha」"
"1034" = "「Ưm……phù, ah——ưm——fahi……ưm ư——ưm,\\nHo he fu……fan……ư ku——ưm!」"
"1043" = "「Pua」"
"1555" = "Aan~, Fukami há miệng ra,\\nphô bày trọn vẹn bên trong cho tôi thấy."
```

Kết bài
