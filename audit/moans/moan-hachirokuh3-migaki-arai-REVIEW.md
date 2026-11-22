# Moan-fix REVIEW — ハチロクh3_磨き洗い.txt.toml

File: `01_Hachiroku/ハチロクh3_磨き洗い.txt.toml` — H-scene "cọ rửa" (Soutetsu + Hachiroku tắm chung ở Tororyu-yu sau ca trực). 312 dòng script, audit sai 44 (27 gasp, 14 đại từ, 3 nghĩa).
Cơ sở tổng moan: **56 file / 1.351 dòng** (lr_日々姫h2 vừa merge 22/11 ~10:13, 5 dòng; GitHub 5ad2d1da). File này +24 dòng → **57 file / 1.375 dòng** sau khi merge.
Phạm vi: CHỈ rên/thở/gasp/SFX. Không đụng đại từ, thuật ngữ, nghĩa. Không đụng các dòng gasp Ư của audit/sweep. Không đụng dòng "Kh".

LƯU Ý VỀ NGUỒN DỮ LIỆU: hai file scratch cũ `.work-h3-cands.json` / `.work-h3-all.json` có giá trị JP BỊ LỆCH (vd. key 1021 hiển thị JP chứa ふぁっ, trong khi JP thật trong CSV3 không có ふぁっ). Toàn bộ fix dưới đây được xây dựng lại TRỰC TIẾP từ CSV3 (312 dòng, 1 bộ duy nhất, 0 key trùng) + audit JSON (44 fix), và kiểm chứng lại từng giá trị jp/tw/old_vn với CSV3. Hai file scratch lệch đó cần xóa, không dùng nữa.

## §1. Tóm tắt — 24 fix

| Nhóm | Số dòng | Keys |
|---|---|---|
| fa/fu → romaji | 5 | 964, 1012, 1015, 1084, 1127 |
| họ ひゃ/きゅ → romaji | 2 | 1006, 1218 |
| đếm nguyên âm (rên) | 6 | 1029, 1030, 1034, 1062, 1063, 1064 |
| SFX sai lớp nghĩa | 2 | 1794, 1807 |
| SFX dài → romaji | 6 | 1828, 1829, 1832, 1835, 1836, 1837 |
| đếm nguyên âm (SFX) | 1 | 1813 |
| cười → romaji | 2 | 1009, 1677 |
| **Tổng** | **24** | |

## §2. Chi tiết từng fix

### fa/fu → romaji (5)

#### key 964 — ハチロク — kind: fa/fu
- JP: 「いやなことなど――んっ――うれひっ――\nわたくしっ――嬉しい――ですっ――ふあっ！」
- TW: 「不討厭——嗯——好高興——我——好高興——呼啊！」
- VN cũ (sau audit): 「Không ghét đâu——ưm——vui——\nem——vui lắm——ạ——Phùa!」
- VN mới: 「Không ghét đâu——ưm——vui——\nem——vui lắm——ạ——Fua!」
- Lý do: ふあっ → romaji "Fua" theo quy ước vòng moan (h2/h5/h6/h7/h8/h9 + lr_日々姫h2 vừa merge 10:13 đều dùng Fua). "Phùa" nghe ngượng — đọc như từ "phà". F1 để đợt thống nhất chốt một dạng chung.

#### key 1012 — ハチロク — kind: fa/fu
- JP: 「ふあっ――あっ――知らない、とこっ――んっ――\nこすれて――これ――やっ――気持ち――いいっ」
- TW: 「呼啊——啊——不知道的部位——嗯——摩擦一下——這麼——哎——舒服——」
- VN cũ (sau audit): 「Phùa——a——nơi, chưa từng biết——ưm——\nđang bị cọ xát——cái này——Ya——sung——sướng quá」
- VN mới: 「Fua——a——nơi, chưa từng biết——ưm——\nđang bị cọ xát——cái này——Ya——sung——sướng quá」
- Lý do: ふあっ → "Fua" (như 964). Chỉ đổi token rên; phần còn lại giữ nguyên.

#### key 1015 — ハチロク — kind: fa/fu
- JP: 「はっ――あっ――ああっ――～～～んっ――ふあっ――\nあっ！？」
- TW: 「哈——啊——啊啊——～～～——呼啊——啊！？」
- VN cũ (sau audit): 「Ha——a——a a——～～～ưm——Phùa——\nA!?」
- VN mới: 「Ha——a——a a——～～～ưm——Fua——\nA!?」
- Lý do: ふあっ → "Fua" (như 964). Chỉ đổi token rên.

#### key 1084 — ハチロク — kind: fa/fu
- JP: 「ぷあっ――あっ――はっ――\nはい、双鉄、さまっ……ですが」
- TW: 「噗啊——啊——哈——是的，雙鐵少爺……不過」
- VN cũ (sau audit): 「Phùa——a——ha——\nVâng, ngài Soutetsu……nhưng mà」
- VN mới: 「Pua——a——ha——\nVâng, ngài Soutetsu……nhưng mà」
- Lý do: ぷあっ (2 mora) → "Pua" (như 964; ぷあ→Pua theo quy ước Hepburn chặt của vòng moan).

#### key 1127 — ハチロク — kind: fa/fu
- JP: 「は、はひっ――開発、したい、ですっ――んっ、\n双鉄、さまと――いっしょの――セックス――ふあっ」
- TW: 「是、是——我也想開發——嗯——和雙鐵少爺——一起的——性愛——呼啊」
- VN cũ (sau audit): 「Vâ, vâng——em muốn, khai phá——ưm,\nlàm tình——cùng với——ngài Soutetsu——Phùa」
- VN mới: 「Vâ, vâng——em muốn, khai phá——ưm,\nlàm tình——cùng với——ngài Soutetsu——Fua」
- Lý do: ふあっ cuối dòng → "Fua" (như 964).

### họ ひゃ/きゅ → romaji (2)

#### key 1006 — ハチロク — kind: hya
- JP: 「ひゃふっっ！？　きゅ、急に――双鉄、様っ！」
- TW: 「呀嗚！？這、這麼突然——雙鐵少爺！」
- VN cũ (sau audit): 「Hya fư!? Đ, đột nhiên——ngài Soutetsu!」
- VN mới: 「Hyafu!? Đ, đột nhiên——ngài Soutetsu!」
- Lý do: ひゃふっっ → "Hyafu" (tiền lệ file moan đã merge: ひゃふっ→"Hyafu"). "Hya fư" tách một chuỗi mora thành hai mảnh VN+romaji lẫn lộn — một dòng = một cách diễn.

#### key 1218 — ハチロク — kind: hya
- JP: 「そう、てつ――さまっ！？　んきゅっ――そこっ――\nおひりっ――おしりの――穴、ですぅっ――んっ」
- TW: 「雙鐵少爺——！？嗯嗚——那是——屁股——屁股的——洞，嗯——」
- VN cũ (sau audit): 「Ngài, Soutetsu——!? Ưm kya——chỗ đó——\nlà lỗ——lỗ——hậu môn, đấy ạ——ưm」
- VN mới: 「Ngài, Soutetsu——!? Nkyu——chỗ đó——\nlà lỗ——lỗ——hậu môn, đấy ạ——ưm」
- Lý do: んきゅっ → "Nkyu" — tiền lệ 3 file moan đã merge (んきゅっ→"Nkyu"). "Ưm kya" lẫn VN+romaji cho một âm duy nhất.

### đếm nguyên âm — rên (6)

#### key 1029 — 双鉄H — kind: vowel-count
- JP: 「くあぁっぁぁぁぁっ！」
- TW: 「啊啊啊！」
- VN cũ (sau audit): 「A a a a!」
- VN mới: 「Kuaa Aaaa!」
- Lý do: くあぁっ + あぁぁぁっ = 6 nguyên âm a (2+4). Bản cũ "A a a a!" chỉ có 4 a VÀ mất phụ âm k- của く. Romaji "Kuaa Aaaa!" khôi phục cả phụ âm lẫn số lượng.

#### key 1030 — ハチロク — kind: vowel-count
- JP: 「ずぞぉぉぉぉぉぉぉぉっ！！！」
- TW: 「啊啊！！！」
- VN cũ (sau audit): 「A a a a!!!」
- VN mới: 「Zuzooooooooo!!!」
- Lý do: ずぞぉぉぉぉぉぉぉぉっ = 9 nguyên âm o (ぞ 1 + ぉ×8). Bản cũ "A a a a!!!" sai cả phụ âm (mất z-), sai cả nguyên âm (a thay vì o), sai cả số lượng (4 thay vì 9). Romaji "Zuzooooooooo" — giữ u của ず theo tiền lệ "Zurooooooo".

#### key 1034 — ハチロク — kind: vowel-count
- JP: 「あーーーーーんっ――んっ――こくっ」
- TW: 「啊嗯———嗯——啊嗚」
- VN cũ (sau audit): 「A a a a ưm——ưm——ực」
- VN mới: 「A a a a a a ưm——ưm——ực」
- Lý do: あーーーーーんっ = あ + 5 ー = 6 nguyên âm a. Bản cũ "A a a a" chỉ có 4. Giữ phong cách VN cách khoảng của file, chỉ sửa số lượng thành 6.

#### key 1062 — ハチロク — kind: vowel-count
- JP: 「んひいいっ！！？」
- TW: 「嗯咿！！？」
- VN cũ (sau audit): 「Ưm hí ii!!?」
- VN mới: 「Nhiii!!?」
- Lý do: んひいいっ = ん + ひ + い + い = 3 nguyên âm i. Bản cũ "Ưm hí ii" tách một chuỗi mora thành hai mảnh ("hí ii") và lẫn VN+romaji. Romaji "Nhiii" (3 i) — tiền lệ んひゅ→"Nhyu".

#### key 1063 — ハチロク — kind: vowel-count
- JP: 「んふうううううううううううううう～～～っ！」
- TW: 「嗯嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚～～～！」
- VN cũ (sau audit): 「Ưm hưm～～～!」
- VN mới: 「Nfuuuuuuuuuuuuuuu～～～!」
- Lý do: んふうううううううううううううう = ふ (1u) + 14 う = 15 nguyên âm u (đếm bằng chương trình; ghi chú F2 của audit nói "13 う" là đếm thiếu 1). Bản cũ "Ưm hưm" chỉ có 2 âm tiết — mất âm nghiêm trọng. Romaji "Nfuuuuuuuuuuuuuuu" (15 u).

#### key 1064 — ハチロク — kind: vowel-count
- JP: 「んううううううっ！！！」
- TW: 「嗯嗚嗚嗚嗚嗚！！！」
- VN cũ (sau audit): 「Ưm ưm ưm!!!」
- VN mới: 「Nuuuuuu!!!」
- Lý do: んうううううう = ん + 6 う = 6 nguyên âm u theo tổng Hepburn (mora). Lưu ý về công thức: "1 + số う" đọc theo nghĩa đen sẽ cho 7, nhưng mora gốc Ở ĐÂY CHÍNH LÀ う nên công thức đó đếm trùng 1 — tổng đúng là 6. Xem §4 F6.

### SFX sai lớp nghĩa (2)

#### key 1794 — monologue — kind: sfx
- JP: （ずっ！　じゅぶっ！　ずぼっ！　じゅぼっ！）
- TW: （呲！啾！啪！啾啵！）
- VN cũ (sau audit): （Phập! Sột sột! Phập! Chu mút!）
- VN mới: （Phập! Phập! Phập! Chu mút!）
- Lý do: じゅぶっ là âm chèn ƯỚT (TW 啾), không phải âm cọ xát — "Sột sột" sai lớp nghĩa. Đổi thành "Phập!" (lớp chèn/đâm; tiền lệ trong chính file này: 1811 じゅぶっ→"Phập!").

#### key 1807 — monologue — kind: sfx
- JP: （ばちゅんっ！　じゅっ！　じゅぶっ！　じゅぱっ！）
- TW: （啪啾！啾！啾！啾啪！）
- VN cũ (sau audit): （Phập! Chụt! Sột sột! Chụt!）
- VN mới: （Phập! Chụt! Phập! Chụt!）
- Lý do: じゅぶっ → "Sột sột!" — cùng token, cùng lỗi sai lớp nghĩa như 1794 (audit chỉ gắn cờ 1794 nhưng 1807 mắc lỗi y hệt). Đổi thành "Phập!".

### SFX dài → romaji (6)

#### key 1828 — monologue — kind: romaji
- JP: （ずりゅううううううううううううっ！）
- TW: （噝溜——！）
- VN cũ (sau audit): （Trượt!!!）
- VN mới: （Zuryuuuuuuuuuuuuu!!!）
- Lý do: ずりゅうううううううううううう = ずりゅ (2u) + 12 う = 14 nguyên âm u. "Trượt!!!" mất toàn bộ độ dài. Romaji "Zuryuuuuuuuuuuuuuu" (14 u) — tiền lệ SFX trượt dài "Zuryuuuuuu".

#### key 1829 — monologue — kind: romaji
- JP: （すりゅううううっ）
- TW: （噝溜）
- VN cũ (sau audit): （Sột sột）
- VN mới: （Suryuuuuu）
- Lý do: すりゅうううう = すりゅ (2u) + 4 う = 6 nguyên âm u. "Sột sột" vừa mất độ dài vừa sai lớp (すりゅ là âm TRƯỢT — cf. 1833 すりゅっ→"Trượt!"). Romaji "Suryuuuuu" (6 u).

#### key 1832 — monologue — kind: romaji
- JP: （ずるううううっ）
- TW: （抽出）
- VN cũ (sau audit): （Rút ra）
- VN mới: （Zuruuuuu）
- Lý do: ずるうううう = ずる (2u) + 4 う = 6 nguyên âm u. "Rút ra" mất toàn bộ độ dài — audit F2 bỏ sót dòng này (cùng lớp với 1828/1829). Romaji "Zuruuuuu" (6 u).

#### key 1835 — monologue — kind: romaji
- JP: （ずぶうううううううううううっ！）
- TW: （插——！）
- VN cũ (sau audit): （Phập!!!）
- VN mới: （Zubuuuuuuuuuuuu!!!）
- Lý do: ずぶううううううううううう = ずぶ (2u) + 11 う = 13 nguyên âm u. "Phập!!!" mất toàn bộ độ dài. Romaji "Zubuuuuuuuuuuuuu" (13 u).

#### key 1836 — monologue — kind: romaji
- JP: （きゅううううううっ！！！）
- TW: （插入！！！）
- VN cũ (sau audit): （Siết chặt!!!）
- VN mới: （Kyuuuuuuu!!!）
- Lý do: きゅうううううう = きゅ (1u) + 6 う = 7 nguyên âm u. "Siết chặt!!!" mất toàn bộ độ dài. Romaji "Kyuuuuuuu" (7 u). Cf. cờ F2 của lr_日々姫h2 (1659 "Siết chặt!" không kéo dài) — xem §4 F7.

#### key 1837 — monologue — kind: romaji
- JP: （ずぼおおおおおおおおおっ！！）
- TW: （插入！！）
- VN cũ (sau audit): （Phập!!）
- VN mới: （Zuboooooooooo!!）
- Lý do: ずぼおおおおおおおおお = ずぼ (1o) + 9 お = 10 nguyên âm o. "Phập!!" mất toàn bộ độ dài. Romaji "Zuboooooooooo" (10 o).

### đếm nguyên âm — SFX (1)

#### key 1813 — monologue — kind: vowel-count
- JP: （ちゅろぉぉぉっ）
- TW: （啾嚕）
- VN cũ (sau audit): （Chụụụt）
- VN mới: （Chụụụụt）
- Lý do: ちゅろぉぉぉっ = ろ (1 o) + ぉ×3 = 4 nguyên âm o. Bản audit "Chụụụt" chỉ có 3 ụ — thiếu 1. Sửa thành "Chụụụụt" (4 ụ).

### cười → romaji (2)

#### key 1009 — ハチロク — kind: romaji
- JP: 「うふふっ」
- TW: 「呵呵」
- VN cũ (sau audit): 「Ư fufu」
- VN mới: 「Ufufu」
- Lý do: うふふっ là tiếng CƯỜI, không phải rên — "Ư fufu" gắn tiền tố gasp Ư vào tiếng cười là sai quy tắc khóa (cười diễn thành tiếng cười). Tiền lệ "Ufufu" trong các file moan đã merge.

#### key 1677 — monologue — kind: romaji
- JP: 僕の手の中、すずはほうっと幸せそうな息を吐き、\nやがて、うふふと小さく微笑む。
- TW: 鈴在我的懷抱中幸福地呼氣，不久，又輕輕地微笑起來。
- VN cũ (sau audit): Trong vòng tay tôi, Suzu khẽ thở hắt ra một hơi hạnh phúc,\nrồi mỉm cười "ư fufu" nhỏ nhẹ.
- VN mới: Trong vòng tay tôi, Suzu khẽ thở hắt ra một hơi hạnh phúc,\nrồi mỉm cười "ufufu" nhỏ nhẹ.
- Lý do: Tiếng cười được trích dẫn trong lời dẫn ("ư fufu") → "ufufu" cho nhất quán với 1009 "Ufufu". Chỉ đổi âm trích dẫn, còn lại giữ nguyên.

## §3. Đã đọc và GIỮ NGUYÊN (không fix)

Đã đọc toàn bộ 312 dòng (CSV3 + audit review + sweep 23 mục). Các nhóm giữ nguyên:

- **Gasp Ư của audit — KHÔNG đụng (6 dòng):** 783 「っ――」→"Ư——", 784 「っ――ぉっ――」→"Ư——o——", 785 「――っ――ぁっ！」→"——Ư——a!", 1221 「っ！」→"Ư!", 1222 「っ！！？」→"Ư!!?", 1226 「～～～～っ！」→"～～～～Ư!".
- **Họ ひゃ đã romaji đúng (4 dòng):** 1007 ひゃうんっ→"Hya ưm!", 1017 はひゅっ→"Ha Hyu!?", 1023 ひゅっ→"Hyu", 1149 ひぇ→"Hye".
- **Hơi thở / nuốt / nấc ngắn đã đúng:** 1010 「ふ……す……」→"Phù……su……", 1045 「ぅ、む……」→"Ư, ừm……", 1046/1048 ふっ→"phù", 1049 ひっ→"hi", 1065 んぶっ→"Ưm bư" / ぢゅっ→"chụt" / ぢゅるっ→"chu mút" / ちゅぷっ→"chụt", 1066 んううっ～っ→"Ưm ưm～" (2 u, đúng số lượng + ～ kéo dài), 1067 んくっ→"Ưm" (quy ước trong file, 3×), 1068/1069 ん！/んっ！？→"Ưm!"/"Ưm!?", 1037 くあっ→"Kua!", 1038 あっ×4→"A! A! A! A!", 1039 うあっ→"Ư a!", 1040 んっ――→"Ưm——", 1044 ごくっ/ごきゅっ→"ực", 1088 痛っ→"Đau!?", 1089 くっ→"hự", 1106 んふっ→"ưm hưm" (ngắn, chấp nhận được).
- **SFX ngắn đã đúng (giữ nguyên):** 1792/1793 ずりゅんっ→"Trượt!", 1800 にゅろんっ→"Trượt!", 1806 ぱくっ→"Ngoạm", 1808 ずぼっ→"Phập!" / じゅぼっ→"Chu mút!" / ぼちっ→"Chụt!", 1810 ちゅぷっ→"Chụt" / にゅるっ→"trượt" / にゅっ→"ngoáy" / こしゅっ→"sột sột", 1811 じゅぶっ→"Phập!" (tiền lệ cho 1794/1807), 1814 ちゅっ→"Chụt", 1816 くちんっ→"Phập", 1818/1820/1823/1824/1826 びゅ…→"Phụt" (xuất tinh, nhất quán), 1827 つぷっ→"Phập", 1833 しゅこ→"Vuốt" / しゅっ→"Vuốt" / しにゅっ→"Nắm" / すりゅっ→"Trượt", 1834 しゅこんっ→"Vuốt", 1838 しにゅっ→"Nắm lấy", 1839 さすっ→"Vuốt", 1840 くぱっ→"Tách ra", 1795 ごしゅっ→"Sột", 1805 （ああ――）→"（A a——）" (2 a, đúng), 1791 （ずっ――るっ――）→"（Trượt——vào——）" (ngắn, gạch ngang đã kéo dài đủ), 1787 くっ→"hự".
- **Không thuộc phạm vi moan:** 1139 「ふぁひ、ほーへふはは」 là lời nói ngọng (miệng đầy) — không phải dòng rên, giữ nguyên "Vâ ng, hô——hê phu ha ha"; 1474/1479/1685/1737 là lời dẫn có きゅっ/きゅう (động từ), không phải rên; 1148 là thoại thường, không có lỗi moan.
- **1224 「ぺろっ――れろっ――ちゅっ――れろろ～っ」→"Liếm——liếm——chụt——liếm láp～" — GIỮ:** chuỗi âm liếm được diễn bằng động từ tiếng Việt (liếm/chụt); "liếm láp～" đã có ～ kéo dài cho れろろ～っ. Sweep xếp kind "already-rendered", không fix; audit cũng không gắn cờ.
- **1801 ぶりゅん→"Phập!" — GIỮ (đã quyết, xem §4 F2).**
- **1815 くっ→"Ngoáy" — GIỮ (gắn cờ, xem §4 F5).**

## §4. Cờ cho đợt thống nhất

- **F1 — fa/fu một dạng chung (CHƯA CHỐT):** file này dùng romaji Fua/Pua, nhất quán với các file Hachiroku đã fix moan (h2/h5/h6/h7/h8/h9) và lr_日々姫h2 (vừa merge, 5/5 đều Fua). Các file audit dùng "Phùa"/"Phà". Đợt thống nhất chốt một dạng cho toàn dự án (cờ F4 của lr_日々姫h2 cũng là vấn đề này).
- **F2 — 1801 ぶりゅん→"Phập!" GIỮ:** ぶりゅん là âm nảy/lò xo của da thịt khi đâm vào; "Phập" là cách diễn âm đâm/va chạm đã chốt trong file này (ずっ/ずぼっ/じゅぶっ). "Phụt" tuy khớp TW 噗 nhưng trong file này "Phụt" đã là SFX xuất tinh (1818/1820/1823/1824/1826) — đổi sang "Phụt" sẽ gây nhầm lẫn. Đợt thống nhất có thể xem lại.
- **F3 — じゅぶっ không nhất quán:** 1809 "Chu mút!!" vs 1811/1794/1807 "Phập!" (cùng là âm chèn ướt). File này sửa 2 dòng "Sột sột" sai lớp thành "Phập!"; 1809 giữ "Chu mút" (cách diễn ướt/hút, TW 啾啵, không bị audit gắn cờ). Đợt thống nhất chọn một dạng.
- **F4 — 1810 にゅるっ→"trượt" viết thường** (các chỗ khác "Trượt") — lỗi chính tả nhỏ, không thuộc phạm vi moan.
- **F5 — 1815 くっ→"Ngoáy" vs 1089 くっ→"hự":** cùng âm くっ, hai cách diễn khác nhau (SFX độc thoại vs thoại). Giữ nguyên cả hai; đợt thống nhất xem xét.
- **F6 — Phương pháp đếm nguyên âm (1064):** tổng Hepburn/mora (6 u cho んうううううう) được dùng thay vì công thức "1 + số う/ぅ" đọc theo nghĩa đen (cho 7). Số "1" trong công thức là nguyên âm của mora gốc; khi mora gốc CHÍNH LÀ う thì công thức đọc đen sẽ đếm trùng. Các fix dài khác (1828: 14u, 1835: 13u, 1063: 15u) đều theo tổng Hepburn và đã đếm lại bằng chương trình.
- **F7 — Cf. cờ F2 của lr_日々姫h2:** key 1659 "Siết chặt!" không được kéo dài ở file đó. File này: 1836 きゅうううううう (7 u) → romaji "Kyuuuuuuu". Đợt thống nhất nên chốt cách xử lý SFX "Siết chặt" có chuỗi dài cho nhất quán.
- **F8 — Đếm lại F2 của audit:** ghi chú F2 của audit nói 1063 có "13 う" — đếm bằng chương trình là **14 う** (15 u tổng). Các số đếm trong F2 của audit nên được đếm lại bằng chương trình ở đợt thống nhất.

## §5. Khối TOML (24 khóa — áp vào file TOML khi rebuild; `\\n` trong khối = ký tự \n thật trong giá trị)

```toml
964 = "「Không ghét đâu——ưm——vui——\\nem——vui lắm——ạ——Fua!」"
1006 = "「Hyafu!? Đ, đột nhiên——ngài Soutetsu!」"
1009 = "「Ufufu」"
1012 = "「Fua——a——nơi, chưa từng biết——ưm——\\nđang bị cọ xát——cái này——Ya——sung——sướng quá」"
1015 = "「Ha——a——a a——～～～ưm——Fua——\\nA!?」"
1029 = "「Kuaa Aaaa!」"
1030 = "「Zuzooooooooo!!!」"
1034 = "「A a a a a a ưm——ưm——ực」"
1062 = "「Nhiii!!?」"
1063 = "「Nfuuuuuuuuuuuuuuu～～～!」"
1064 = "「Nuuuuuu!!!」"
1084 = "「Pua——a——ha——\\nVâng, ngài Soutetsu……nhưng mà」"
1127 = "「Vâ, vâng——em muốn, khai phá——ưm,\\nlàm tình——cùng với——ngài Soutetsu——Fua」"
1218 = "「Ngài, Soutetsu——!? Nkyu——chỗ đó——\\nlà lỗ——lỗ——hậu môn, đấy ạ——ưm」"
1677 = "Trong vòng tay tôi, Suzu khẽ thở hắt ra một hơi hạnh phúc,\\nrồi mỉm cười \"ufufu\" nhỏ nhẹ."
1794 = "（Phập! Phập! Phập! Chu mút!）"
1807 = "（Phập! Chụt! Phập! Chụt!）"
1813 = "（Chụụụụt）"
1828 = "（Zuryuuuuuuuuuuuuu!!!）"
1829 = "（Suryuuuuu）"
1832 = "（Zuruuuuu）"
1835 = "（Zubuuuuuuuuuuuu!!!）"
1836 = "（Kyuuuuuuu!!!）"
1837 = "（Zuboooooooooo!!）"
```

## §6. Lượt soát 2 (second pass — đọc lại toàn bộ 24 fix với JP)

- **Tổng số fix:** 24. **Tái kiểm chứng:** 24/24. **Bỏ:** 0. **Sửa:** 1.
- **Kiểm chứng cơ học (đọc lại từ CSV3 + audit JSON, độc lập với lúc viết fix):** 24/24 mục có key dạng string, jp/tw/old_vn/character khớp CSV3 tuyệt đối, old_vn = VN sau audit (hoặc VN CSV3 khi audit không sửa), fix khác old_vn đúng ở token rên/SFX. Khối TOML 24 khóa parse OK, 0 sai lệch so với JSON. Không đụng dòng gasp Ư nào (783/784/785/1221/1222/1226). Không đổi dòng "Kh" nào ("Kh" trong 964 chỉ là chữ cái đầu của từ "Không", không bị đụng).
- **Đếm lại nguyên âm bằng chương trình (bộ đếm Hepburn đầy đủ: yoon, dấu ー, kana nhỏ) với JP thật trong CSV3:** 11/13 token khớp ngay; 2 trường hợp "CHECK" được xem xét lại và xác nhận ĐÚNG (1034 là dòng nhiều token — token đầu あーーーーーん = 6 a, fix "A a a a a a" = 6 a; 1813 "Chụụụụt" có 4 ụ cho 4 nguyên âm o của ろぉぉぉ, chữ "Ch" mang âm chu của ちゅ).
- **1 lỗi thật được phát hiện và sửa trong lượt soát 2 — key 1832:** fix ban đầu "Zuruuuuuu" (7 u) sai 1 nguyên âm — JP thật là ずるうううう (ずる + **4** う = 6 u tổng), không phải 5 う như lúc đếm tay. Đã sửa thành "Zuruuuuu" (6 u) trong cả JSON, §2 và khối TOML; kiểm chứng lại toàn vẹn (JSON 24/24, TOML 24 khóa 0 sai lệch).
- **Kiểm tra sweep trực tiếp:** 23/23 mục sweep của file này đã đối chiếu — 20 nằm trong audit (gasp), 1 nằm trong fix moan này (1063), 2 kind "already-rendered" không fix (1066, 1224) — cả hai đều giữ đúng.
- **Lưu ý về phương pháp:** lượt đếm đầu tiên dùng bộ đếm thô + token gõ tay đã báo 7 "mismatch" giả (do không xử lý dấu ー, kana yoon, ụ tiếng Việt, và gõ thừa/thiếu chữ cái). Lượt đếm thứ hai dùng bộ đếm Hepburn đầy đủ + token trích trực tiếp từ CSV3/JSON mới là kết quả chính thức. Bài học: không bao giờ kiểm chứng số lượng bằng chuỗi gõ tay.

Kết bài
