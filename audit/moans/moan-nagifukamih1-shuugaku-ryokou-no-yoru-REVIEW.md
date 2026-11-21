# Moan-fix review: 凪ふかみh1_修学旅行の夜.txt.toml (moan-nagifukamih1-shuugaku-ryokou-no-yoru)

## 1. Kiểm chứng file

- File: `凪ふかみh1_修学旅行の夜.txt.toml` — route 07_Nagi_Fukami, đêm tu nghiệp của ba người (ăn ba ba, lần đầu làm tình ba người: Nagi trước, Fukami sau).
- TOML md5 `50c203c62f6e830c5e30413e09083b02` (khớp md5 audit), không có bản trùng trong 227 file.
- CSV3: 1 bộ duy nhất, 318 dòng, 0 key trùng; VN khớp TOML 318/318 sau chuẩn hóa `\n`/khoảng trắng.
- Đã đọc 318/318 dòng; xét 116 dòng rên/SFX (88 thoại + 28 SFX trong ngoặc).

## 2. Tổng quan các dòng đổi

- Đổi **26 dòng**: 24 romaji + 1 đếm nguyên âm (1314) + 1 sai âm (1232).
- Romaji họ fa/fu (9 dòng): 1166, 1218, 1227, 1237, 1246 (×2 token), 1247, 1336, 1440, 1474 — ふあ→Fua, ふぁ→Fa, ふや→Fuya.
- Romaji họ ひゃ/ひゅ/ひあ/きゃ (15 dòng): 1214 Hyafu, 1216 Hyua, 1219 Hya, 1221 Hyufu, 1222 Hyau, 1223 Hyan, 1224 Hia, 1226 Hyapu, 1304 Nhyu, 1306 Nhyun, 1347 Hya, 1365 Hia, 1486 Kya + Hyau, 1487 Hyaun + Hyua, 1490 Kyau.
- Quyết định họ ひゃ (ghi chú đánh giá 21/11, theo ủy quyền của Hieu): bản cũ dịch ひゃ/ひゅ/ひあ/きゃ thành "Á" làm mất hẳn phụ âm mora hy-/ky- — đây là lỗi mất âm đã được xác lập trong các file đã gộp (ポーレットh3 ROUTE-MOANS: "'Á' cho きゃっ/ひゃっ/やっ" là lỗi mất phụ âm mora; 凪h2 sửa ひあ "Hya"→"Hia" 5 dòng; んひゅ→"Nhyu/Nhyun" ở h7 836/837, 稀咲h3 2277, 凪h2 2512). "Á" chỉ đúng khi JP là あっ/あぁ (không có phụ âm mora). Quy tắc tự nhiên (Hieu 19/11) không cứu được "Á" ở đây vì âm hy-/ky- biến mất hoàn toàn, không phải chỉ nghe ngượng.

## 3. Từng dòng đổi (JP / TW / cũ / mới / lý do)

### 1. key 1166 [凪]
- JP: 「いっしょ――はっ――いくっ――ば、いっ――\nふあっ――あっ――にい、さん――ふかみ、ちゃっ――」
- TW: 「一起……啊……去……呼……啊……大哥哥……小深……」
- Cũ: 「Cùng nhau——hà——ra——nha, đi——\nphù——a——anh, hai——Fukami, ơi——」
- Mới: 「Cùng nhau——hà——ra——nha, đi——\nFua——a——anh, hai——Fukami, ơi——」
- Lý do: ふあっ họ fa: "phù" sai cách đọc (phù là ふぅ), "phùa" ngượng → romaji Fua

### 2. key 1214 [凪]
- JP: 「ひゃふっ――あっ――奥っ――奥、ばっ――\nにーさん――あた、って――」
- TW: 「呀……啊……裡面……裡面……大哥哥的……頂到了……」
- Cũ: 「Á phù——a——sâu quá——sâu, quá——\nanh hai——chạm, rồi——」
- Mới: 「Hyafu——a——sâu quá——sâu, quá——\nanh hai——chạm, rồi——」
- Lý do: ひゃふっ: "Á" làm mất phụ âm mora hy- (tiền lệ ポーレットh3: "Á" cho ひゃっ là lỗi mất âm); romaji Hyafu

### 3. key 1216 [ふかみ]
- JP: 「ひゅあっ――あっ！？」
- TW: 「呀……啊！？」
- Cũ: 「Á——a!?」
- Mới: 「Hyua——a!?」
- Lý do: ひゅあっ → Hyua (mora hy- không được mất)

### 4. key 1218 [ふかみ]
- JP: 「きゃあっ――んっ――やっ――熱っ――ふあっ――」
- TW: 「呀……嗯……哎呀……好熱……呼……」
- Cũ: 「Á——ưm——á——nóng quá——phù——」
- Mới: 「Á——ưm——á——nóng quá——Fua——」
- Lý do: ふあっ → Fua

### 5. key 1219 [ふかみ]
- JP: 「ひゃっ――んっ――あっ――おなか――んっ――\nおさ――れ、て――ふっ――だん、だんっ――」
- TW: 「呀……嗯……啊……裡面……嗯……被……推著……哼……越來越……」
- Cũ: 「Á——ưm——a——trong bụng——ưm——\nđang——bị, đẩy——phù——dần, dần——」
- Mới: 「Hya——ưm——a——trong bụng——ưm——\nđang——bị, đẩy——phù——dần, dần——」
- Lý do: ひゃっ → Hya

### 6. key 1221 [ふかみ]
- JP: 「ひゅふっ！」
- TW: 「呀！」
- Cũ: 「Á!」
- Mới: 「Hyufu!」
- Lý do: ひゅふっ → Hyufu (JP có !)

### 7. key 1222 [凪]
- JP: 「ひゃうっ！　あ――ふかみ――ちゃんっ――」
- TW: 「呀！啊……小……深……」
- Cũ: 「Á! A——Fukami——」
- Mới: 「Hyau! A——Fukami——」
- Lý do: ひゃうっ → Hyau (JP có !)

### 8. key 1223 [凪]
- JP: 「ひゃんっ！！」
- TW: 「呀！！」
- Cũ: 「Á!!」
- Mới: 「Hyan!!」
- Lý do: ひゃんっ → Hyan (JP có !!)

### 9. key 1224 [ふかみ]
- JP: 「ひあ"っ！！？」
- TW: 「呀！！？」
- Cũ: 「Á!!?」
- Mới: 「Hia!!?」
- Lý do: ひあっ → Hia (JP có !!?)

### 10. key 1226 [凪]
- JP: 「ひゃぷっ！？　わっ――んっ――にゃ、うっ――\nこ、これっ――んっ――熱か――ばいっ――臭か、ばい」
- TW: 「呀！？哇……嗯……喵……這、這個……嗯……好燙……味道好大」
- Cũ: 「Á!? Oa——ưm——nya, ư——\nc-cái này——ưm——nóng quá——nha——nặng mùi, nha」
- Mới: 「Hyapu!? Oa——ưm——nya, ư——\nc-cái này——ưm——nóng quá——nha——nặng mùi, nha」
- Lý do: ひゃぷっ → Hyapu (giữ cả ぷ mà bản cũ làm mất)

### 11. key 1227 [ふかみ]
- JP: 「やっ！？　おちん、ちん――しゅごっ――あっ――\nふっ――んんんっ――んっ！　ふあっ！　あっ！！」
- TW: 「呀！？雞巴……好舒服……啊……呼……嗯……嗯！呼！啊！！」
- Cũ: 「Á!? Chim——tuyệt quá——a——\nphù——ưm——ưm! Phù! A!!」
- Mới: 「Á!? Chim——tuyệt quá——a——\nphù——ưm——ưm! Fua! A!!」
- Lý do: ふあっ thứ hai trong dòng → Fua; ふっ đầu dòng giữ "phù" (hơi thở thường)

### 12. key 1232 [双鉄H]
- JP: 「くっ――あ」
- TW: 「呃……啊」
- Cũ: 「Ư——a」
- Mới: 「Hự——a」
- Lý do: くっ là tiếng nghẹn: 1229/1230 cùng cảnh đều "hự", dòng này "Ư" lệch nhịp trong file

### 13. key 1237 [凪]
- JP: 「ふぁっ――あっ――ちゅっ――んむっ――\nちゅるっ――れろっ――れるっ――れろおっ――」
- TW: 「呼……啊……啾……嗯唔……啾……啾……啾……啾……」
- Cũ: 「Phù——a——chụt——ưm——\nrột——liếm——liếm——liếm——」
- Mới: 「Fa——a——chụt——ưm——\nrột——liếm——liếm——liếm——」
- Lý do: ふぁっ ngắn → Fa (1 nguyên âm)

### 14. key 1246 [凪]
- JP: 「ふあっ――あっ――あっ――は、はあっ――\n――あっ――んっ――ふあっ――あっ――はぁ、はあっ」
- TW: 「哇……啊……啊……啊，啊…………啊……嗯……哇……啊……呼，呼」
- Cũ: 「Phù——a——a——hà, hà——\n——a——ưm——phù——a——hà, hà」
- Mới: 「Fua——a——a——hà, hà——\n——a——ưm——Fua——a——hà, hà」
- Lý do: ふあっ thứ nhất → Fua + ふあっ thứ hai → Fua

### 15. key 1247 [凪]
- JP: 「ふぁっ――あっ――あっ――おなか――んっ――\nおなか、にっ――にーさん――がっ――」
- TW: 「哇……啊……啊……肚子裡……嗯……大哥哥……在肚子裡……」
- Cũ: 「Phù——a——a——trong bụng——ưm——\ntrong, bụng——anh hai——đang——」
- Mới: 「Fa——a——a——trong bụng——ưm——\ntrong, bụng——anh hai——đang——」
- Lý do: ふぁっ → Fa

### 16. key 1304 [凪]
- JP: 「んひゅっ！」
- TW: 「嗯！」
- Cũ: 「Ưm!」
- Mới: 「Nhyu!」
- Lý do: んひゅっ → Nhyu (tiền lệ h7 837, 凪h2 2512)

### 17. key 1306 [凪]
- JP: 「んひゅんっ！！！」
- TW: 「嗯！！！」
- Cũ: 「Ưm!!!」
- Mới: 「Nhyun!!!」
- Lý do: んひゅんっ → Nhyun (tiền lệ h7 836, 稀咲h3 2277)

### 18. key 1314 [双鉄H]
- JP: 「ああっ！」
- TW: 「好啊！」
- Cũ: 「A!」
- Mới: 「Aa!」
- Lý do: ああっ có 2 âm a, bản cũ chỉ còn 1

### 19. key 1336 [凪]
- JP: 「ふかみちゃんも、ウチも――んっ――にーさんの、こと、\n信じとる……けんっ――あっ――ふあっ――んっ」
- TW: 「小深也是，咱也是……嗯……咱們都相信大哥哥……啊……哇……嗯」
- Cũ: 「Cả Fukami, cả em nữa——ưm——đều,\ntin tưởng... anh hai... nha——a——phù——ưm」
- Mới: 「Cả Fukami, cả em nữa——ưm——đều,\ntin tưởng... anh hai... nha——a——Fua——ưm」
- Lý do: ふあっ → Fua

### 20. key 1347 [凪]
- JP: 「違う――ばいっ！　ふ、ひゃっ――んっ――これ――\nさっきの――とっ――んっ――おんなじ、なの、に――」
- TW: 「感覺不一樣！呼，呀……嗯……這個……跟剛才的……嗯……明明是一樣的……」
- Cũ: 「Khác quá——nha! Phù, á——ưm——cái này——\nso với——lúc nãy——ưm——rõ ràng, giống nhau, mà——」
- Mới: 「Khác quá——nha! Phù, Hya——ưm——cái này——\nso với——lúc nãy——ưm——rõ ràng, giống nhau, mà——」
- Lý do: ひゃっ → Hya (ふ đầu dòng giữ "phù")

### 21. key 1365 [ふかみ]
- JP: 「知らないっ――こん――なのっ――ひあっ――わたし\n――わたしぃっ――とけ――る――とけ、ちゃうっ！」
- TW: 「我都不知道……竟然……呀……我……我……要溶化……要溶化了！」
- Cũ: 「Không biết đâu——cái——này——á——em\n——em——tan——chảy——tan chảy, mất thôi!」
- Mới: 「Không biết đâu——cái——này——Hia——em\n——em——tan——chảy——tan chảy, mất thôi!」
- Lý do: ひあっ → Hia

### 22. key 1440 [凪]
- JP: 「やっ――ふあっ――あっ――にーさん、の――\nにーさんの、おちん、ちん――ずりって――あた、って」
- TW: 「討厭……哇……啊……大哥哥的……大哥哥的雞巴……緊緊地……貼著」
- Cũ: 「Á——phù——a——của anh hai——\nchim của... anh hai——cọ vào——chạm, rồi」
- Mới: 「Á——Fua——a——của anh hai——\nchim của... anh hai——cọ vào——chạm, rồi」
- Lý do: ふあっ → Fua

### 23. key 1474 [凪]
- JP: 『「イっ――くぅぅぅぅぅぅぅぅうううううううんっ！」\n「ふやっ――あっ――んううううううううううっ～！！」』
- TW: 『「……去了！」\n「哇……啊……嗯！！」』
- Cũ: 『「R-raaaaaaa mấttttt!」\n「Á——a——ưmmmmmmmmmm~!!」』
- Mới: 『「R-raaaaaaa mấttttt!」\n「Fuya——a——ưmmmmmmmmmm~!!」』
- Lý do: ふやっ → Fuya (bản cũ gộp thành "Á" mất hẳn tiếng fu-ya)

### 24. key 1486 [凪]
- JP: 『「きゃっ！」\n「ひゃうっ！」』
- TW: 『「呀！」\n「呀！」』
- Cũ: 『「Á!」\n「Á!」』
- Mới: 『「Kya!」\n「Hyau!」』
- Lý do: きゃっ/ひゃうっ/ひゅあっ → romaji (mora ky-/hy- không được mất)

### 25. key 1487 [凪]
- JP: 『「ひゃうんっ！」\n「ひゅあっ！！」』
- TW: 『「呀！」\n「呀！！」』
- Cũ: 『「Á!」\n「Á!!」』
- Mới: 『「Hyaun!」\n「Hyua!!!」』
- Lý do: きゃっ/ひゃうっ/ひゅあっ → romaji (mora ky-/hy- không được mất)

### 26. key 1490 [ふかみ]
- JP: 『「んぶっ！？」\n「きゃうっ！？」』
- TW: 『「呃！？」\n「呀！？」』
- Cũ: 『「Ưm!?」\n「Á!?」』
- Mới: 『「Ưm!?」\n「Kyau!?」』
- Lý do: きゃうっ dòng 2 → Kyau

## 4. Các dòng giữ (đáng chú ý)

- Gasp Ư (16 dòng): っ――→"Ư", あっ→"a", んっ→"ưm" — đúng quy tắc gasp, không đụng. Sweep 5 mục của file (1235, 1236, 1285, 2022, 1736) đã kiểm chứng: 4 already-rendered đúng, 1736 っ đã diễn thành "ư" — không đụng.
- Hôn/liếm: ちゅっ→"chụt", れるっ/れろっ→"liếm", ぺろ→"liếm" — thống nhất cả file, giữ. 1317 れろおおおおおおおおっ→"Liếmmmmmmmm!" giữ (độ dài diễn bằng 8 chữ m, đúng tỉ lệ).
- Hơi thở ふっ/ふー: "phù" / "Phùuu" / "Phùuuuuu" — hơi thở thường, giữ. 1252 đã được audit sửa độ dài, không đụng lại.
- SFX trong ngoặc (28 dòng): （Phụt!）, （Siết chặt）, （Rột!）, （Trơn tuột...）, （Ngọ nguậy）, （Lảo đảo） — dạng động từ Việt đúng, giữ hết.
- Nói ngọng khi miệng bận (1291, 1303: ひっはひ/ひょはひょひょ...): diễn thành lời có nghĩa — thuộc phạm vi audit (audit đã duyệt), moan không đụng.
- 28 dòng nhiễu (tên Fukami, chữ すっぽん, lời thoại thường, độc thoại không có tiếng rên) — không phải dòng rên, giữ.

## 5. Chồng lấn với audit (không sửa trùng)

- Key 1280 (あんっ→"An"): audit của file đã sửa sẵn (1 trong 8 lỗi audit) — moan KHÔNG sửa trùng, chỉ ghi nhận.
- Key 1238 + 1252 (độ dài hơi thở ふー) và 2026/2027/2043 (SFX ướt "sột soạt"→"rột"/"nhóp nhép"/"Phập!"): audit đã sửa — moan không đụng lại.
- 7 key trùng audit chỉ khác đúng token rên: 1214, 1226, 1232, 1304, 1306, 1314, 1474 — áp MỘT giá trị mỗi key (giá trị moan thay thế ở đúng token rên).

## 6. Cờ cho đợt thống nhất

- Họ ひゃ/ひゅ/ひあ/きゃ → romaji là quy tắc đã chốt cho toàn dự án (xem §2); các file đã gộp trước đây dùng "Á" cho họ này cần rà lại trong đợt thống nhất.
- 1226 ひゃぷっ: bản cũ làm mất ぷ — đã giữ lại thành "Hyapu"; các file khác có ひゃぷ tương tự nên kiểm tra.
- 1291/1303 nói ngọng: nếu đợt thống nhất quyết diễn ngọng thì rà lại.

## 7. Lượt soát 2

- Tổng 26 / tái kiểm chứng 26 / bỏ 0 / sửa 0. Mỗi fix đã đọc lại vs JP + TW.
- Lưu ý: 15 dòng họ ひゃ ban đầu xếp "giữ" (theo quán tính "Á" của file), sau khi đối chiếu bằng chứng các file đã gộp (xem §2) đã chuyển sang "đổi" — đây là phần sửa trong lượt đánh giá theo ủy quyền của Hieu, không phải lượt soát 2.
- JSON 26 mục, khóa string, jp/tw/old_vn khớp CSV3 26/26. Khối TOML parse bằng tomllib: 26 khóa, 0 sai lệch giá trị.

## 8. Khối TOML

```toml
[script]
1166 = "「Cùng nhau——hà——ra——nha, đi——\\nFua——a——anh, hai——Fukami, ơi——」"
1214 = "「Hyafu——a——sâu quá——sâu, quá——\\nanh hai——chạm, rồi——」"
1216 = "「Hyua——a!?」"
1218 = "「Á——ưm——á——nóng quá——Fua——」"
1219 = "「Hya——ưm——a——trong bụng——ưm——\\nđang——bị, đẩy——phù——dần, dần——」"
1221 = "「Hyufu!」"
1222 = "「Hyau! A——Fukami——」"
1223 = "「Hyan!!」"
1224 = "「Hia!!?」"
1226 = "「Hyapu!? Oa——ưm——nya, ư——\\nc-cái này——ưm——nóng quá——nha——nặng mùi, nha」"
1227 = "「Á!? Chim——tuyệt quá——a——\\nphù——ưm——ưm! Fua! A!!」"
1232 = "「Hự——a」"
1237 = "「Fa——a——chụt——ưm——\\nrột——liếm——liếm——liếm——」"
1246 = "「Fua——a——a——hà, hà——\\n——a——ưm——Fua——a——hà, hà」"
1247 = "「Fa——a——a——trong bụng——ưm——\\ntrong, bụng——anh hai——đang——」"
1304 = "「Nhyu!」"
1306 = "「Nhyun!!!」"
1314 = "「Aa!」"
1336 = "「Cả Fukami, cả em nữa——ưm——đều,\\ntin tưởng... anh hai... nha——a——Fua——ưm」"
1347 = "「Khác quá——nha! Phù, Hya——ưm——cái này——\\nso với——lúc nãy——ưm——rõ ràng, giống nhau, mà——」"
1365 = "「Không biết đâu——cái——này——Hia——em\\n——em——tan——chảy——tan chảy, mất thôi!」"
1440 = "「Á——Fua——a——của anh hai——\\nchim của... anh hai——cọ vào——chạm, rồi」"
1474 = "『「R-raaaaaaa mấttttt!」\\n「Fuya——a——ưmmmmmmmmmm~!!」』"
1486 = "『「Kya!」\\n「Hyau!」』"
1487 = "『「Hyaun!」\\n「Hyua!!!」』"
1490 = "『「Ưm!?」\\n「Kyau!?」』"
```

Kết bài: file 凪ふかみh1_修学旅行の夜 — 26 dòng rên đã sửa (24 romaji + 1 đếm nguyên âm + 1 sai âm), 90 dòng rên/SFX giữ nguyên, sweep 5 mục không đụng, audit 8 lỗi không sửa trùng. Quy tắc họ ひゃ → romaji đã chốt cho toàn dự án.
