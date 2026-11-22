# Moan-fix: lr_日々姫h2_デザートは食事の前に.txt.toml — 5/288

- File: `02_Hibiki/lr_日々姫h2_デザートは食事の前に.txt.toml` (route 02_Hibiki, 288 dòng script; H-scene Hibiki — "món tráng miệng trước bữa ăn"). Audit đã gộp: 42/288 sai (13 gasp theo sweep, 26 moan đếm nguyên âm/phụ âm, 3 sai nghĩa).
- TOML md5 `278bb98599c53cd1d22db62a29101c26` (khớp audit), không có bản trùng; CSV3 1 bộ 288 dòng, 0 key trùng, VN khớp TOML 288/288 (dạng làm phẳng `\n`→khoảng trắng). File không có dòng "Kh".
- Sweep gasp kiểm tra trực tiếp 16/16 mục: 13 lost-gasp đã nằm trong audit (giữ nguyên), 973 đếm nguyên âm (đã kiểm chứng 3u — đúng), 1079 + 1663 already-rendered (giữ nguyên theo audit). Không đụng dòng gasp Ư nào.

## 1. Moan inventory — xét 149 dòng rên/SFX, đổi 5, giữ 144

- 112 dòng thoại rên/thở/SFX (Hibiki + Soutetsu, key 696–1215) + 4 dòng độc thoại gasp (675, 691, 1572, 1594 — đã fix Ư ở audit, giữ nguyên) + 33 dòng SFX trong ngoặc (1651–1693).
- Ngoài ra 10 dòng độc thoại có từ chỉ âm thanh đã đọc, giữ nguyên dạng diễn nghĩa (không phải dòng rên): 1302 あーん, 1317/1342 鼻息, 1379 はぁはぁ, 1404 ぱくぱく, 1417 嬌声, 1475 ガクガク, 1483 喘ぎ, 1513 ヒク, 1553 ぞわぞわ.
- Đổi 5 dòng — cùng một lỗi: ふあっ (2 mora f-u-a) bị render thiếu mora "u" thành "Fa"/"fa". Sửa thành "Fua"/"fua" theo tiền lệ moan-hachiroku-h4 (ふあっ→"Fua") và quy tắc romaji fallback Hieu duyệt 21/11 ~01:56 (họ fa/fu trong dòng rên → romaji vì "phà"/"phùa" nghe ngượng).

## 2. Chi tiết từng dòng sửa

### 1172 [日々姫] — moan (fa/fu thiếu mora u)

- JP: 「ふあっ――あっ――あっ――のんでる――のんでるっ、\nごくごくっ――ごく、ごくっ――あっ！！！」
- TW: 「蛤啊啊……射、射進來了……咕嘟咕嘟……咕嘟咕嘟的……啊！！！」
- Cũ: 「Fa——a——a——đang uống——đang uống,\nừng ực——ực, ực——a!!!」
- Mới: 「Fua——a——a——đang uống——đang uống,\nừng ực——ực, ực——a!!!」
- JP ふあっ = f-u-a (2 mora) — VN "Fa" chỉ có 1 âm, mất mora "u". Sửa "Fua"; các あっ→"a" đã đúng, giữ nguyên.

### 1173 [日々姫] — moan (fa/fu thiếu mora u, token thứ 2)

- JP: 「ふぁっ！　あっ――にぃにっ――んっ――ふあっ、\nあっ――べろっ――あったかい――しゅきぃっ」
- TW: 「蛤啊！啊……阿哥……嗯……蛤啊……啊……舌頭好暖……好舒服」
- Cũ: 「Fa! A——anh hai——ưm——fa,\nA——lưỡi——ấm quá——thích lắm.」
- Mới: 「Fa! A——anh hai——ưm——fua,\nA——lưỡi——ấm quá——thích lắm.」
- Token đầu ふぁっ (ァ nhỏ = 1 mora) → "Fa!" ĐÚNG, giữ nguyên. Token sau ふあっ (あ đầy = 2 mora) → "fa," thiếu "u" — sửa "fua,". Chỉ đổi đúng token này.

### 1174 [日々姫] — moan (fa/fu thiếu mora u)

- JP: 「ふあっ！　あっ――あっ！　あっ！！！！」
- TW: 「蛤啊！啊、啊！啊！！！！」
- Cũ: 「Fa! A——a! A!!!!」
- Mới: 「Fua! A——a! A!!!!」
- ふあっ → "Fua" (2 mora); các あっ→"A"/"a" đã đúng.

### 1175 [日々姫] — moan (fa/fu thiếu mora u)

- JP: 「ふあっ！　あっ！　おまん、こっ――しゅご、い、のっ、\nごちゅん、ごちゅんって――にぃにの、ちん、ちんっ」
- TW: 「蛤啊！啊！小穴……好舒服……阿哥的肉棒……跳來跳去的」
- Cũ: 「Fa! A! Chỗ, đó——tuyệt, quá,\ncứ đâm, bình bịch——của anh, hai.」
- Mới: 「Fua! A! Chỗ, đó——tuyệt, quá,\ncứ đâm, bình bịch——của anh, hai.」
- ふあっ → "Fua"; còn lại giữ nguyên.

### 1176 [日々姫] — moan (fa/fu thiếu mora u)

- JP: 「ふあっ！　あっ！　そこっ――そこっ！　ん……\nもっと、ゆっくり――いま――キツい、けんっ――あっ」
- TW: 「蛤啊！啊！那裡……那裡好舒服……嗯……再慢一點……現在身體……還繃得很緊」
- Cũ: 「Fa! A! Chỗ đó——chỗ đó! Ưm……\nChậm lại, một chút——bây giờ——chặt, quá——a.」
- Mới: 「Fua! A! Chỗ đó——chỗ đó! Ưm……\nChậm lại, một chút——bây giờ——chặt, quá——a.」
- ふあっ → "Fua"; ん→"Ưm", あっ→"a" đã đúng.

## 3. Kept-moan notes — các dòng rên đã xét, giữ nguyên (lý do 1 dòng)

- Họ ひゃ/ひゅ/ひあ → romaji đúng quy tắc 3b, giữ: 937 ひゅぁ→"Hyua" (14a/2n đã kiểm chứng), 941 ひゅあっ→"Hyua", 942 ひゃぐっ→"Hyagu", 943 ひあっ→"Hia", 946 ひゃっつ→"Hya", 1185 ひあっ→"hia".
- Họ fa/fu đã đúng romaji, giữ: 1106 ふぁ→"fa" (ァ nhỏ, 1 mora), 1038 ふぁむっ→"famu", 949 ぷぁ→"pua", 1051 ぷあっ→"pua", 1089 ぷあっ→"Pua!", 1033 ぷぁっ→"pua".
- Nói ngọng (miệng đầy) — KHÔNG phải dòng rên (quy tắc 3b), giữ: 1033 『ひゃばば、ばふぃっ』→"Hyababa, bafi"; 1057 ふぇひあふぁれ→"meshiagare" (audit đã giữ).
- 964 いやぁん→"Á" — JP không có phụ âm mora, "Á" đúng; 947 ふえっ→"Hể!!!" — thốt tự nhiên tiếng Việt, giữ.
- Soutetsu grunt họ く/グッ→"Hự" — quy ước nhất quán toàn file, giữ (là grunt, không phải rên): 696, 697, 948, 968, 969, 970, 1017 ぐっ, 1159 くっ, 1653/1669/1674/1677 ごちゅっ/ごっ/ぢゅっくん.
- Cờ audit (6) đã giải quyết — giữ: 939 ふっ→"fu", あっ→"a" (romaji trung thực); 984 はぁっ→"ha"; 994 中っ (っ ngắt câu, đã diễn bằng —— + "a!" của ぁっ sau đó, không thêm Ư); 1169/1170/1171 chuỗi はぁっ→"ha" (ngắt diễn bằng ——/!).
- 1079 ～～～～～っ→"~~~~~!!" và 1663 （ぐ～～～～～～っ）→"（Rột~~~~~~）" — sweep already-rendered, audit đã xác nhận giữ.
- Cười: 953/1035/1057 ふふっ→"Fufu"/"fufu", 980/1051/1088/1215 んふふ→"nfufu"/"Nfufu", 977/1081/1083/1085/1086 えへへ→"Ehehe" — giữ (cười, không phải rên).
- SFX trần diễn bằng động từ tiếng Việt — quy ước nhất quán toàn file, giữ: 992 はむっ→"Ngậm!", 1018 ぢゅぼっ→"Mút!", 1651 （はむっ！）→"（Ngậm!）".
- SFX ngoặc diễn nghĩa (1652–1693) giữ toàn bộ — xem cờ F1/F2. Riêng 1659 きゅううっ→"Siết chặt!" không kéo dài: phân biệt với きゅんっ→"Siết!" bằng chữ "chặt" (lựa chọn có chủ ý của dịch giả), giữ — xem cờ F2.
- Audit đếm nguyên âm/phụ âm đã kiểm chứng lại bằng máy, tất cả đúng: 937 14a/2n, 973 3u, 996 3u, 1001 10u/2n, 1004 3n, 1016 2u/3u/8u, 1017 2o, 1035 3o, 1036 4u, 1037 3u, 1042 3u/3u, 1043 12o, 1044 3u, 1045 7u/3u, 1046 3u, 1066 10u, 1070 19t, 1077 4m, 1081 5m, 1083 3m, 1088 6a, 1658 4ự, 1660 6i, 1677 13u, 1682 4o/2o, 1686 11i, 1687 10o, 1688 5i (chữ "i" thứ 6 trong đếm thô là của "Siết").

## 4. Flags — đợt thống nhất (không tự quyết)

- F1 — Công thức đếm cho SFX ngoặc dài (diễn nghĩa + kéo dài phụ âm cuối): chưa có quy tắc chốt. 1666 ぶびゅうう (3u)→"Phụtttt" (4t) vs 1668 どりゅうう (3u)→"Phụttttt" (5t) — cùng cấu trúc mora nhưng khác 1t; 1676 じゅぶううっ (3u)→"chụtttt" (4t); 1679 ぎいっ (2i)→"Kétttt" (4t); 1681 ちいいいいいいっ (8i)→"Xoètttttt" (6t); 1682/1683 し(i)こっ→"sụccc" (3c, nhất quán giữa 2 dòng). Tiền lệ moan-hachiroku-h4 F2 cùng câu hỏi. Giữ nguyên toàn bộ, chờ chốt công thức.
- F2 — 1659 きゅううっ (3u)→"Siết chặt!" không kéo dài, trong khi 1660/1686/1688 cùng họ きゅう… đều kéo dài ("lạiiiii"/"lạiiiiiiiiiii"/"lạiiiii") — cùng họ câu hỏi F1 (khi nào âm dài được render bằng độ dài?).
- F3 — Viết hoa "nfufu" (980, sau "……") vs "Nfufu" (1088, 1215, cũng sau "……") — không nhất quán; 1035 "fufu" giữa câu viết thường là đúng. Cosmetic, chờ thống nhất.
- F4 — Cờ audit (1) "Phùa" vs "Fua" chưa chốt: vòng moan áp romaji "Fua" theo quy tắc fallback Hieu duyệt 21/11 ~01:56 + tiền lệ h4; nếu Hieu muốn "Phùa" thì đợt thống nhất lật cả cụm fa/fu cùng lúc (1106, 1172–1176, 1038, 1051, 1089, 949, 1033).
- F5 — 1665 びゅっ――びゅ――りゅっ→"Phụt——phụ——t" (りゅっ render thành "t" cuối) — giữ như cách diễn hình âm trailing-off có chủ ý; cờ audit (5) đã nêu, vòng moan không đổi.

## 5. Lượt soát 2

- Đọc lại toàn bộ 5 giá trị fix đối chiếu JP từng dòng (mora ふあ/ふぁ, あっ, んっ, dấu câu): 5/5 tái kiểm chứng, 0 bỏ, 0 sửa.
- JSON 5 mục (key chuỗi); khối TOML 5 khóa parse OK, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 5/5; mỗi fix chỉ khác VN cũ ở đúng token "Fa"/"fa"→"Fua"/"fua"; old_vn khớp TOML 5/5 (dạng làm phẳng `\n`→khoảng trắng).

## 6. Khối TOML (đã parse-kiểm chứng: 5 khóa, 0 sai lệch)

```toml
[script]
"1172" = "「Fua——a——a——đang uống——đang uống,\\nừng ực——ực, ực——a!!!」"
"1173" = "「Fa! A——anh hai——ưm——fua,\\nA——lưỡi——ấm quá——thích lắm.」"
"1174" = "「Fua! A——a! A!!!!」"
"1175" = "「Fua! A! Chỗ, đó——tuyệt, quá,\\ncứ đâm, bình bịch——của anh, hai.」"
"1176" = "「Fua! A! Chỗ đó——chỗ đó! Ưm……\\nChậm lại, một chút——bây giờ——chặt, quá——a.」"
```

## Kết bài

File lr_日々姫h2_デザートは食事の前に.txt.toml: đọc 288/288 dòng, xét 149 dòng rên/SFX, đổi 5 dòng (1172–1176, cùng lỗi ふあっ→"Fa" thiếu mora "u", sửa "Fua"), giữ 144 dòng. Không đụng dòng gasp Ư nào, không dòng "Kh", không sửa đại từ/thuật ngữ/nghĩa. Lượt soát 2: 5/5 tái kiểm chứng, 0 bỏ, 0 sửa. TOML md5 `278bb98599c53cd1d22db62a29101c26`; CSV3 1 bộ 288 dòng; sweep 16/16 mục đã kiểm tra trực tiếp. Cờ đợt thống nhất: F1–F5 (công thức đếm t/c cho SFX ngoặc dài, 1659, viết hoa nfufu, "Phùa" vs "Fua", 1665 "phụ——t").
