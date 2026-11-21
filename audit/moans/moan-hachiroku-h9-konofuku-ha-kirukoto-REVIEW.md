# Moan-fix REVIEW — ハチロクh9_コノフクハキルコト.txt.toml (moan-hachiroku-h9-konofuku-ha-kirukoto)

File H-scene route 01_Hachiroku: Hachiroku mặc đồng phục "Tàu bia", cảnh H chính (khoảng key 1868–2650) + các dòng SFX độc thoại cuối file (3480–3504).

## 1. Xác minh tệp

- **TOML:** `sources/toml2/translation_toml/01_Hachiroku/#U30cf#U30c1#U30ed#U30afh9_#U30b3#U30ce#U30d5#U30af#U30cf#U30ad#U30eb#U30b3#U30c8.txt.toml` — md5 `bcbf02a0308ddac5d5aca3ac1cd717ce` (khớp md5 audit, tự tính lại), 119.546 byte, UTF-8 BOM + CRLF, `[selections]` rỗng, **không có bản sao trùng** (kiểm tra md5 toàn bộ 227 tệp TOML).
- **CSV3:** 1 bộ duy nhất (`translation_toml\01_Hachiroku`), 613 dòng script, 0 key trùng, 0 VN trống. CSV3 khớp TOML-2 613/613 (audit đã kiểm chứng; tự kiểm tra 26 key sửa: 0 sai lệch sau chuẩn hoá `\n`→khoảng trắng).
- **Audit của file đã merge:** 69/613 sai (11,3%) — xem `audit-hachiroku-h9-REVIEW.md`. 9/26 fix moan dưới đây chồng lên fix audit (chỉ khác audit ở đúng token rên; giá trị moan = giá trị audit + token rên đổi).
- **Cơ sở tổng moan (tự đọc `moans/ROUTE-MOANS.md`):** 6 file / 156 dòng (dòng tổng cuối file; dòng header "5 file / 125" là cũ, chưa cập nhật sau file thứ 6 — ghi nhận để parent sửa header khi merge).

## 2. Moan inventory — đã đọc 613/613 dòng, xét 100 dòng rên/SFX

- Theo nhân vật: ハチロク 69, 双鉄 20, monologue 11.
- Theo loại: 83 dòng có っ, 10 dòng họ fa/fu/hya (JP chứa ふぁ/ふあ/ふぇ/ふや/ひあ/ひゃ/ひゅ), 31 dòng nguyên âm dài, 6 dòng SFX trong （ ）, 4 dòng cười (2020/2023/2025/2585 — đều "Ufufu", giữ).
- **Đổi 26 dòng:** 13 romaji + 9 đếm nguyên âm + 4 sai âm. **Giữ 74 dòng.**
- Kiểu lỗi chính: (1) họ fa/fu bị Việt hoá thành "phù a"/"Phù a" trong chuỗi rên cao trào — về romaji theo quy tắc Hieu duyệt 21/11; (2) rên dài đếm nguyên âm sai — "Hà" cho はぁ (2 âm), "chụttttt" cho ちゅううう (4 âm u), "reruuuu" cho れるううううっ (5 âm u); (3) sai âm SFX: ちろっ→"Chụt", ちゅむっ→"chụt", きゅくぅぅぅぅ→"Ưm ưưưư".

## 3. Các dòng sửa (26)

### 3.1 Romaji họ fa/fu (13 dòng)

Tiền lệ: moan-lr-mikuro §17 — ふぁ/ふあ là rên/thở gấp trong cao trào, trong chuỗi rên, hoặc rên dài đứng riêng → romaji ("phà"/"phùa" nghe gượng); mikuro 1705: ふ……ぁ là một hơi duy nhất, JP tự tách bằng …… → "Fu……a", giữ nguyên hình tách. Áp dụng cho cả dạng tách ふ、あっ / ふっ、あっ / ふっ――あっ / ふ――あっ trong chuỗi rên (cùng một hơi "fu...a"). Hơi thở ふ/ふっ đứng riêng KHÔNG đi kèm あ thì giữ "phù"/"Phù" (2033/2036/2138/2182; mikuro 1800: ふうっ→"Phùu!").

#### 2082 — ハチロク — romaji

- JP: 「かっ――ふあ――だめっ――ですっ――ちか、らっ\nもう――はいら、ないっ――からだ――ガク、って」
- TW: 「啊——呼啊——不行——力氣已經——使不上了——身子——好僵」
- Cũ (CSV3): 「A——phù a——không được——đâu ạ——sức lực\nkhông còn——nữa rồiっ——cơ thể——cứng đờ, mất rồi」
- Mới: 「A——Fua——không được——đâu ạ——sức lực không còn——nữa rồiƯ——cơ thể——cứng đờ, mất rồi」
- Lý do: ふあ là một âm rên duy nhất; "phù a" tách thành hai từ Việt ("phù" = sưng/phù phép) nghe gượng → romaji "Fua". Phần còn lại = giá trị audit (Ư gasp cuối dòng của audit giữ nguyên).

#### 2089 — ハチロク — romaji

- JP: 「あ――はいっ、はいっ――さよう、ですね、\n双鉄、さまっ――んっ――ふっ――ふあっ――あ」
- TW: 「啊——是，是——這樣啊，雙鐵少爺——呼——呼啊——啊」
- Cũ: 「A——vâng, vâng——đúng vậy, nhỉ,\nNgài Soutetsuっ——ưm——phù——phù a——a」
- Mới: 「A——vâng, vâng——đúng vậy, nhỉ, Ngài SoutetsuƯ——ưm——Fu——Fua——a」
- Lý do: chuỗi hơi んっ――ふっ――ふあっ――あ trong cao trào; ふあっ → "Fua", ふっ trước nó cùng nhịp thở → "Fu" (một hệ romaji cho cả nhịp thở). Ư gasp của audit giữ nguyên.

#### 2037 — ハチロク — romaji

- JP: 「ふあっ！　あっ――ふううっ！　ふあっ！！」
- TW: 「呼啊！啊——呼！呼啊！！」
- Cũ: 「Phù a! A——phù ư ư! Phù a!!」
- Mới: 「Fua! A——Fuuu! Fua!!」
- Lý do: ふあっ ×2 → "Fua"; ふううっ = ふ+う+う = 3 u → "Fuuu" ("phù ư ư" tách một hơi thành ba mảnh, sai hình âm).

#### 2110 — ハチロク — romaji + đếm nguyên âm

- JP: 「はぁっ！　はぁっ！　はああっ！　ふあっ！？」
- TW: 「啊！啊！嗬啊！呼啊！？」
- Cũ: 「Hà! Hà! Hà a! Phù a!?」
- Mới: 「Haa! Haa! Haaa! Fua!?」
- Lý do: はぁっ = 2 a → "Haa" (bản cũ "Hà" thiếu 1 a; tiền lệ mikuro 1917: はぁ→2 a); はああっ = 3 a → "Haaa" (bản cũ "Hà a" tách + thiếu 1 a, gộp thành một token); ふあっ → "Fua".

#### 2180 — ハチロク — romaji + đếm nguyên âm

- JP: 「んっきゅっ！！？\nふああぁぁぁぁぁぁっぁぁぁぁっぁああああっ！！」
- TW: 「嗯嗚！！？呼、嗯啊啊——！！」
- Cũ: 「Ưm kyu!!?\nPhù a a a a a a a a a a a a a a a a a a a a!!」
- Mới: 「Ưm kyu!!?\nFuaaaaaaaaaaaaaaaaa!!」
- Lý do: rên dài một hơi bị tách thành 20 mảnh "a" rời — đúng kiểu romaji rule nhắm tới (tiền lệ ふかみh1 967 "Hya ah ưm"→"Hyaaann"). Đếm lại độc lập: JP có 17 âm a (あ×2 + ぁ×7 + ぁ×4 + あ×4) — bản cũ thừa 3 a → romaji "Fu" + 17 a. Giữ "Ưm kyu" đầu dòng và "!!" cuối (っ cuối là nhịp ngắt của rên dài, audit không thêm Ư, không đụng).

#### 2151 — ハチロク — romaji

- JP: 「ん――よい、しょっ。双鉄様の、おおきくて――\nふ……あ……お窓から出すだけ――でもっ」
- TW: 「嗯——好了。雙鐵少爺，您的好大——呼……啊……從小窗裡取出來就這麼——但是」
- Cũ: 「Ưm——xong, rồi. Của ngài Soutetsu, to quá——\nPhù……a……chỉ lấy ra từ cửa sổ thôi——mà cũngっ」
- Mới: 「Ưm——xong, rồi. Của ngài Soutetsu, to quá—— Fu……a……chỉ lấy ra từ cửa sổ thôi——mà cũngƯ」
- Lý do: ふ……あ là một hơi duy nhất, JP tự tách bằng …… (đúng tiền lệ mikuro 1705: "Phu……a"→"Fu……a"); "Phù" đọc như từ Việt → romaji, giữ nguyên hình tách. Ư cuối dòng của audit giữ nguyên.

#### 2289 — ハチロク — romaji + đếm nguyên âm

- JP: 「わたくし――の、おまたの――われ、めっ――んっ、\nふ――あっ――くっ――はぁ――おまん、まん、です」
- TW: 「我——股間的——裂縫——嗯——呼——啊——嗯——啊——小妹妹」
- Cũ: 「Là khe hở——giữa hai chân——của em——ưm,\nphù——a——ư——hà——là cô bé, ạ」
- Mới: 「Là khe hở——giữa hai chân——của em——ưm,\nFu——a——ư——haa——là cô bé, ạ」
- Lý do: ふ――あっ là một hơi "fu—a" trong chuỗi rên → "Fu——a"; はぁ = 2 a → "haa" (bản cũ "hà" thiếu 1 a). くっ→"ư" giữ nguyên (cách diễn nhất quán trong file: 2113/2149/2187).

#### 2109 — ハチロク — romaji + đếm nguyên âm

- JP: 「はぁ！　あ！　すきっ！　しゅき！　双鉄さまっ！\nそうてつ、さまっ――ふ、あっ――だんな、さまっ」
- TW: 「啊！啊！喜歡！捋來！雙鐵少爺！雙鐵少爺——呼，啊——夫君」
- Cũ: 「Hà! A! Thích quá! Thích quá! Ngài Soutetsu!\nNgài Soutetsuっ——phù, a——phu quânっ」
- Mới: 「Haa! A! Thích quá! Thích quá! Ngài Soutetsu!\nNgài SoutetsuƯ——Fu, a——phu quânƯ」
- Lý do: はぁ = 2 a → "Haa"; ふ、あっ trong chuỗi rên cao trào → "Fu, a" (giữ dấu phẩy = giữ nhịp 2 nhịp của JP; tiền lệ ふかみh1 1223/1379/1458 "Fu, a"). Ư của audit giữ nguyên.

#### 2378 — ハチロク — romaji

- JP: 「はひっ――んっ、くっ――ふ、あっ――\nはいっ！　そう、てつ――さまっ！！！」
- TW: 「是——嗯——呼，啊——是！雙鐵少爺——！！！」
- Cũ: 「Hahi——ưm, ư——phù, a——\nVâng! Ngài Soutetsu!!!」
- Mới: 「Hahi——ưm, ư——Fu, a——\nVâng! Ngài Soutetsu!!!」
- Lý do: ふ、あっ → "Fu, a" (như 2109). はひっ→"Hahi" (romaji cũ, giữ).

#### 1356 — ハチロク — romaji

- JP: 「は――あっ！　あ！　あ！　おまん、まんっ、\nふ、あっ――イク！　イク！　イク！　イクっ！」
- TW: 「——啊！啊！啊！小妹妹，呼，啊——高、高、高潮了！高潮了！」
- Cũ: 「Hà——a! A! A! Cô bé,\nphù, a——ra mất! Ra mất! Ra mất! Ra mất!」
- Mới: 「Hà——a! A! A! Cô bé,\nFu, a——ra mất! Ra mất! Ra mất! Ra mất!」
- Lý do: ふ、あっ trong cao trào → "Fu, a" (như 2109). は――あっ→"Hà——a" giữ nguyên (2 nhịp, đúng số âm).

#### 2613 — ハチロク — romaji

- JP: 「おちん――ちん――んっ。ふと、いっ――ふ、あっ、\nぼこっって、した――とこ――おまん、まん、にっ」
- TW: 「雞——雞——嗯。好粗——呼，啊，粗粗的——部位——進了小妹妹」
- Cũ: 「Dương vật——ưm. Thật to——phù, a,\nphần——nhô ra——đã vào trong——cô bé, rồiっ」
- Mới: 「Dương vật——ưm. Thật to——Fu, a,\nphần——nhô ra——đã vào trong——cô bé, rồiƯ」
- Lý do: ふ、あっ → "Fu, a" (như 2109). Ư cuối dòng của audit giữ nguyên.

#### 2319 — ハチロク — romaji

- JP: 「わた、くしの――おまん、まんっ――ふっ、あっ、\nこん、なに――よだれ、たくさん――たら、してっ」
- TW: 「我的——小妹妹——呼，啊，這麼多——涎水——淌了出來」
- Cũ: 「Cô bé——của em——phù, a,\nđang chảy——rất nhiều——nước dãi——thế nàyっ」
- Mới: 「Cô bé——của em——Fu, a,\nđang chảy——rất nhiều——nước dãi——thế nàyƯ」
- Lý do: ふっ、あっ trong chuỗi rên → "Fu, a" (như 2109). Ư cuối dòng của audit giữ nguyên.

#### 2144 — ハチロク — romaji

- JP: 「んっ――ふっ――あっ――んっ、く――んうっ、\n双鉄、さま――双鉄、さまの――おちん、ちんっ」
- TW: 「嗯——呼——啊——嗯——嗚，雙鐵少爺——雙鐵少爺的——雞雞」
- Cũ: 「Ưm——phù——a——ưm, ư——ưm ư,\nNgài Soutetsu——của ngài Soutetsu——dương vậtっ」
- Mới: 「Ưm——Fu——a——ưm, ư——ưm ư, Ngài Soutetsu——của ngài Soutetsu——dương vậtƯ」
- Lý do: ふっ――あっ trong chuỗi rên → "Fu——a". んうっ→"ưm ư" giữ nguyên. Ư cuối dòng của audit giữ nguyên.

### 3.2 Đếm nguyên âm (9 dòng)

Công thức: số nguyên âm VN = 1 + số う/ぅ trong JP (áp dụng tương tự cho chuỗi ぁ/あ: đếm tổng số mora nguyên âm). Kiểm chứng độc lập bằng token trong lượt soát 2.

#### 2055 — ハチロク — đếm nguyên âm

- JP: 「はっ、はあっ――はあっ――はあっ――\nおまん、まんの、奥っ――あと、もう、少し、で」
- TW: 「哈，哈——哈——哈——小妹妹的深處——再——一點點——」
- Cũ: 「Hà, hà——hà——hà——\nSâu bên trong, cô béっ——chỉ còn, một chút, nữa thôi」
- Mới: 「Hà, haa——haa——haa—— Sâu bên trong, cô béƯ——chỉ còn, một chút, nữa thôi」
- Lý do: はあっ = 2 a → "haa" ×3 (bản cũ "hà" thiếu 1 a mỗi hơi; tiền lệ mikuro 2200: はあっ→2a). はっ đầu dòng → "Hà" (1 a, đúng). Ư của audit giữ nguyên.

#### 2097 — ハチロク — đếm nguyên âm

- JP: 「はぁあっ――あっ――きもち、い――あっ、おいし、\nおいしいっ――ん――双鉄、さまの――おちん、ちん」
- TW: 「啊啊——啊——好，舒服——啊，好吃，好吃——雙鐵少爺的——雞，雞」
- Cũ: 「Hàa——a——sướng, quá——a, ngon,\nngon lắmっ——ưm——dương vật——của ngài Soutetsu」
- Mới: 「Haaa——a——sướng, quá——a, ngon, ngon lắmƯ——ưm——dương vật——của ngài Soutetsu」
- Lý do: はぁあっ = は+ぁ+あ = 3 a → "Haaa" (bản cũ "Hàa" thiếu 1 a). Ư của audit giữ nguyên.

#### 2120 — ハチロク — đếm nguyên âm

- JP: 「ちゅっ――れるっ――れろっ――ちゅううう――\nちゅるっ――（こくっ）――んっ――ちゅっ、ちゅむ」
- TW: 「啾——咻嚕——嗯——啾——啾嚕——（咕嚕）——啾，啾嗯」
- Cũ: 「Chụt——liếm——mút——chụttttt——\nchóp chép——（Ực）——ưm——chụt, chụt」
- Mới: 「Chụt——liếm——mút——chuuuu——\nchóp chép——（Ực）——ưm——chụt, chụt」
- Lý do: ちゅううう = ちゅ+う×3 = 4 u → "chuuuu". Bản cũ "chụttttt" kéo dài bằng phụ âm t thay vì nguyên âm, sai hình âm — và cùng token ちゅうっ được diễn "Chuu" ở 2128, ちゅううっ "chuuu" ở 2153, nên "chụttttt" là ngoại lệ không nhất quán trong chính file này.

#### 2078 — ハチロク — đếm nguyên âm

- JP: 「あっ――んっ……ちゅうっ」
- TW: 「啊——……啾嗚」
- Cũ: 「A——ưm……chụttttt」
- Mới: 「A——ưm……chuu」
- Lý do: ちゅうっ = 2 u → "chuu" (như 2128 ちゅうっ→"Chuu"). Bản cũ "chụttttt" kéo dài bằng t, sai hình âm.

#### 2122 — ハチロク — đếm nguyên âm

- JP: 「ちゅっ――じゅっ――じゅるっ――じゅううっ――\nんっ――れろおおっ――れるっ――れるううううっ」
- TW: 「啾——啾——啾嚕——吱吱嗚——嗯——嗯哦——咻嚕——咻嚕嗚嗚嗚」
- Cũ: 「Chu——ju——juru——juuu——\nƯm——rerooo——reru——reruuuu」
- Mới: 「Chu——ju——juru——juuu——\nƯm——rerooo——reru——reruuuuu」
- Lý do: れるううううっ = る(u)+う×4 = 5 u → "reruuuuu" (bản cũ 4 u, thiếu 1). Các token khác đúng: じゅううっ→"juuu" (3 u), れろおおっ→"rerooo" (3 o).

#### 2101 — 双鉄 — đếm nguyên âm

- JP: 「くああ！」
- TW: 「啊啊！」
- Cũ: 「Aaa!」
- Mới: 「Kuaa!」
- Lý do: くああ = 2 a → "Aa" (bản cũ 3 a, thừa 1). TW 啊啊 (2 a) xác nhận. Chỉ sửa số lượng, giữ cách diễn "Aa" (không khôi phục phụ âm k — TW cũng bỏ k).

#### 2053 — ハチロク — đếm nguyên âm (nói ngọng)

- JP: 「はっ――んっ――ちゅっ――ふっ、ほうへふ、はぁ\n――ちゅくっ、ん――らいふき――れふっ――ふぅっ」
- TW: 「哈——啾——呼，哈呼，啊——啾嗯，嗯——墜喜歡——嗚——嗚」
- Cũ: 「Ha——ưm——chụt——hu, ho he hu, haa\n——chu ku, ưm——dai suki——re hu——huu」
- Mới: 「Ha——ưm——chụt——hu, hoo he hu, haa\n——chu ku, ưm——dai suki——re hu——huu」
- Lý do: ほう = ほ+う = 2 o → "hoo" (bản cũ "ho" thiếu 1 o). Đây là lời nói ngọng khi miệng đang bận — chỉ sửa số âm, giữ nguyên cách diễn ngọng ("dai suki" cho らいふき, "re hu" cho れふっ). はぁ→"haa" (2 a) và ふだっ→"huu" (2 u) đã đúng.

#### 2134 — ハチロク — đếm nguyên âm (nói ngọng)

- JP: 「ぢゅる――（ごくっ）――んっ――\nふへひゅうほはひはふ、ほーへふはは」
- TW: 「啾嚕——（嗯）——唔嗯嗯啊嗯嗯、呼哈」
- Cũ: 「Juru——（Ực）——ưm——\nPhu he hyuu ho ha hi ha phu, ho he phu ha ha」
- Mới: 「Juru——（Ực）——ưm——\nPhu he hyuu ho ha hi ha phu, hoo he phu ha ha」
- Lý do: ほー = ほ+ー = 2 o → "hoo" (bản cũ "ho" thiếu 1 o). ひゅう→"hyuu" (2 u) đã đúng. Cùng loại lỗi nói ngọng như 2053.

#### 2054 — ハチロク — đếm nguyên âm

- JP: 「はっ、はっ――はああっ――は、あ――はぁっ」
- TW: 「哈，哈——啊啊——啊——啊」
- Cũ: 「Hà, hà——hà a——hà, a——hà」
- Mới: 「Hà, hà——haaa——hà, a——haa」
- Lý do: はああっ = 3 a → "haaa" (bản cũ "hà a" tách thành 2 token + thiếu 1 a — gộp thành một token theo chuẩn mikuro 2200); はぁっ = 2 a → "haa" (bản cũ "hà" thiếu 1 a). はっ→"Hà"/"hà" và は、あ→"hà, a" đã đúng số âm.

### 3.3 Sai âm (4 dòng)

#### 2136 — ハチロク — sai âm

- JP: 「ちろっ、ぺろっ、ぺろっ、ぺろっ、れるっ――\nんっ――ぺるっ、ぺろっ――ぺろ、ぺろ、ぺろ、ぺろ」
- TW: 「啾嚕，呸嚕，呸嚕，呸嚕，咻嚕——嗯——呸嚕，呸嚕——呸嚕、呸嚕」
- Cũ: 「Chụt, pero, pero, pero, rero——\nƯm——pero, pero——pero, pero, pero, pero」
- Mới: 「Chiro, pero, pero, pero, rero——\nƯm——pero, pero——pero, pero, pero, pero」
- Lý do: ちろっ là tiếng lưỡi lia ("chiro"), khác ちゅっ ("chụt", tiếng hôn/chụt). Bản cũ dùng "Chụt" cho cả hai, mất phân biệt âm — TW 啾嚕 cũng là âm liếm, không phải tiếng hôn. → romaji "Chiro".

#### 2156 — ハチロク — sai âm

- JP: 「ん……ちゅっ――ちゅむっ――ちゅっ――んっ――\nれるっ――れろっ――じゅるる――れるっ――ちゅぷ」
- TW: 「嗯……啾——啾姆——啾——咻嚕——嗯——啾嚕嚕——咻嚕——啾噗」
- Cũ: 「Ưm……chụt——chụt——chụt——ưm——\nliếm——liếm láp——chóp chép——liếm——chu pu」
- Mới: 「Ưm……chụt——chumu——chụt——ưm——\nliếm——liếm láp——chóp chép——liếm——chu pu」
- Lý do: ちゅむっ → "chumu" (tiền lệ 2140 ちゅむっ→"Chumu" trong chính file này); bản cũ viết "chụt" — nhầm với ちゅっ kề bên. Chỉ đổi đúng token này.

#### 1358 — ハチロク — sai âm ×2 + đếm nguyên âm

- JP: 「――ちゅっ――ちゅっ、ちゅっ――ちゅむ、ちゅっ、\nちゅっ、ちゅうっ――ちゅっ――ちゅむ――れるっ」
- TW: 「——啾——啾，啾——啾嗯，啾，啾，啾嗚——啾——啾嗯——咻嚕」
- Cũ: 「——Chụt——chụt, chụt——chụt, chụt,\nchụt, chụttttt——chụt——chụt——liếm lútttt」
- Mới: 「——Chụt——chụt, chụt——chumu, chụt,\nchụt, chuu——chụt——chumu——reru」
- Lý do: (1) ちゅむ ×2 → "chumu" (như 2156/2140; bản cũ "chụt" nhầm với ちゅっ — TW 啾嗯 xác nhận âm "chumu"); (2) ちゅうっ = 2 u → "chuu" (bản cũ "chụttttt" kéo dài bằng t); (3) れるっ → "reru" — bản cũ "liếm lútttt" là lai tạp khó hiểu ("liếm" = nghĩa liếm + "lútttt" không rõ âm nào của JP); file này diễn れるっ bằng "reru" ở 2043/2122/2140 nên dùng "reru" cho nhất quán.

#### 2178 — ハチロク — sai âm

- JP: 「きゅくぅぅぅぅ～～～っ！！」
- TW: 「嗯嗚嗚～～～！！」
- Cũ: 「Ưm ưưưư~~~!!」
- Mới: 「Kyukuuuuu~~~!!」
- Lý do: JP きゅくぅぅぅぅ là tiếng rên "kyukuuuu" có phụ âm k-y rõ ràng (6 u: きゅ+く+ぅ×4); bản cũ "Ưm ưưưư" diễn thành tiếng ưm thuần, mất hẳn hình âm kyu (và thiếu 1 u). TW diễn thành tiếng ưm (嗯嗚嗚) nhưng JP thắng TW. → romaji "Kyukuuuuu", giữ "~~~!!" (sweep ghi 2178 "already-rendered" — cách diễn っ bằng ~~~ không đụng).

## 4. Ghi chú giữ (các dòng rên đã đúng, không đổi)

- **Ư gasp (sweep + audit, 30 dòng):** KHÔNG đụng bất kỳ dòng nào. 9 key chồng audit (2055/2082/2089/2097/2109/2144/2151/2319/2613) chỉ đổi token rên, giữ nguyên Ư của audit.
- **"Kh" (1883):** 「Kh——ông——là do anh, ưm——」 — giữ nguyên "Kh" cho 僕がっ theo quyết định khóa 21/11 (không đổi sang Ư). Các "Khục"/"Khụ" ở 2591/2474 là tiếng ho/hắng giọng, không thuộc quy tắc này — giữ nguyên.
- **Romaji đã đúng:** 2041 ひゅゅあ→"Hyuua!!", 2045 ひあっ→"Hia!?", 2046 はひっ→"Hahi!?", きゅふっ→"Kyuhu!", 2112 きゃああっ→"Kyaaa" (3 a đúng), 2223 きゅうっ→"Kyuu" (2 u đúng), 2177 んひゅふぅぅぅっ→"Ưm hyu phuuuu" (5 u đúng), 2035 ふっ……あっ→"Hu……a" (đã romaji), 2154 ふっ→"hu".
- **Đếm nguyên âm đã đúng:** 2029 ぺろおっ→"peroo" (2 o), ぺちゅううっ→"pechuuu" (3 u); 2031 ぺろおおっ→"perooo" (3 o), ちゅずううっ→"chuzuuu" (4 u); 2043 るうううっ→"ruuu" (4 u), れるううっ→"reruuu" (3 u); 2127 ぢゅうううううっ→"Juuuuu" (6 u); 2128 ちゅうっ→"Chuu" (2 u); 2135 じゅるうううううっ→"Juruuuuu" (7 u), ぢゅぼおっ→"Juboo" (2 o); 2140 じゅるううっ→"Juruuu" (4 u); 2145 じゅりゅうう→"Juryuuu" (4 u); 2153 ちゅううっ→"chuuu" (3 u); 3480 きゅうううううっ→"kyuuuuuu" (6 u); 2329 んうううううううっ→"ưm ư ư ư ư ư ư" (7 ư + ưm, đếm lại độc lập đúng).
- **Hơi thở ふ/ふっ đứng riêng:** 2033/2036/2138/2182 "Phù"/"phù" — giữ (không đi kèm あ, không phải họ fa).
- **Cười:** 2020/2023/2025/2585 "Ufufu" — giữ (tiếng cười, không phải rên).
- **SFX độc thoại （ ）:** 3480/3483/3484/3492/3495/3502/3504 giữ nguyên dạng onomatopoeia Việt ("Phập", "Bạch", "Sục sâuuuuuu", "Chụt bọpppp!", "Co thắttttt!", "Phụttt!") — nhóm này nhất quán dùng onomatopoeia Việt, không có tiền lệ romaji trong file (khác với "chụt" trong thoại — xem cờ 6).
- **んっ→"Ưm"/"ưm", くっ→"ư"/"ưm":** nhất quán trong file (2113/2149/2187/2289) — giữ.
- **"chu pu" (2156, ちゅぷ) và "mu chu" (2035, むちゅっ):** tách 2 nhịp theo từng mora — giữ (nhất quán trong file, không ngượng).

## 5. Kiểm chứng sweep

- Sweep có 31 mục cho file này: 25 raw-tsu + 5 lost-gasp (2625 whole; 2815/3131/3250/3256 trailing) + 1 already-rendered (2178).
- Audit đã xử lý đủ 30 mục có fix: 23 raw-tsu áp nguyên + 2 raw-tsu sửa khác sweep (2428, 2588 — っ nhấn mạnh cuối câu, bỏ っ thay vì thêm Ư) + 5 lost-gasp. Kiểm chứng chéo: mọi mục sweep đều có trong danh sách fix của audit (25 raw-tsu + 5 lost-gasp = 30), không mục nào bị sót.
- Moan fix không thay đổi bất kỳ giá trị Ư nào của sweep/audit. Riêng 2178 (already-rendered): chỉ đổi phần rên きゅくぅぅぅぅ→"Kyukuuuuu", giữ nguyên cách diễn っ bằng "~~~".

## 6. Cờ (không quyết — để đợt thống nhất / parent kiểm tra)

1. **Mâu thuẫn audit ở 1883 (không phải moan):** `audit-hachiroku-h9-wrong.json` ghi fix 1883 là "là do anh", nhưng khối TOML trong `audit-hachiroku-h9-REVIEW.md` (§6) ghi "là do tôi", và `ROUTE-AUDIT.md` (§ h9) liệt 1883 trong nhóm "anh"→"tôi". Parent kiểm tra xem giá trị nào đã merge. Phần moan của 1883 ("Kh——ông", "ưm") giữ nguyên, không đổi ở đây.
2. **2020 "Ohimitera":** fix audit dùng dạng cũ "Đường sắt Ohimitera" — đợt thống nhất sẽ đổi thành "Ohitoyo" (đã trong hàng đợi thống nhất). Không đổi ở đây (Ufufu giữ nguyên).
3. **7 dòng tách nhịp fa (2109/2378/1356/2613/2319/2144/2289):** đã chuyển "phù, a"/"phù——a" → "Fu, a"/"Fu——a" theo tiền lệ mikuro 1705 + kisaki-h1 (fa trong chuỗi rên → romaji). Nếu Hieu muốn giữ "phù, a" cho dạng tách nhịp có dấu phẩy, 7 dòng này revert dễ dàng (mỗi dòng chỉ 1 token).
4. **1358 れるっ → "reru":** bản cũ "liếm lútttt" đã bỏ; nếu đợt thống nhất muốn dạng nghĩa "liếm" cho れるっ thì đổi "reru"→"liếm".
5. **2178 → "Kyukuuuuu":** TW diễn thành tiếng ưm (嗯嗚嗚); quyết theo JP (có phụ âm kyu rõ ràng) — JP thắng TW.
6. **SFX độc thoại (3480/3483/3484/3492/3495/3502/3504):** giữ onomatopoeia Việt + kéo dài bằng phụ âm ("Phụttt!", "bọpppp!", "Co thắttttt!"); KHÔNG áp công thức đếm nguyên âm cho nhóm này (vì không có tiền lệ romaji trong file). Nếu đợt thống nhất muốn áp công thức cho cả SFX, xét lại nhóm này.
7. **2053/2134:** chỉ sửa số âm trong lời nói ngọng ("hoo"); các mảnh ngọng còn lại giữ nguyên.

## 7. Lượt soát 2 (đọc lại toàn bộ fix đối chiếu từng JP)

Đọc lại toàn bộ 26 fix đối chiếu từng JP (+TW) lần thứ hai, kiểm tra lại từng token rên + đếm nguyên âm độc lập bằng token (2180: 17 a; 2178: 6 u; 2122: 5 u; 2120: 4 u; 2078: 2 u; 2097: 3 a; 2110: 2 a/2 a/3 a; 2055: 2 a ×3; 2054: 3 a + 2 a; 2037: 3 u; 2329 đã kiểm tra: 8 ư đúng — không đổi):

- **Tổng 26 / tái kiểm chứng 26 / bỏ 0 / sửa 0.**
- JSON 26 mục dạng chuẩn (khóa string; jp/tw/old_vn khớp CSV3 tuyệt đối 26/26); khối TOML parse bằng tomllib: 26 khóa, 0 sai lệch giá trị.
- Kiểm tra cơ học (difflib): 9 key chồng audit chỉ khác giá trị audit ở đúng token rên; 17 key còn lại chỉ khác VN cũ ở token rên nhắm tới (trừ 1358 đổi 4 token SFX trong cùng một dòng — đều là token rên/SFX).

## 8. Khối TOML (đã kiểm chứng parse)

Khối TOML dưới đây parse được bằng tomllib, **26 key, 0 sai lệch giá trị so với JSON**. Quy tắc ký tự xuống dòng: giá trị fix nào chứa ký tự xuống dòng dạng backslash-n (2 ký tự, như trong JSON và trong TOML gốc) thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON.

[script]
"1356" = "「Hà——a! A! A! Cô bé,\\nFu, a——ra mất! Ra mất! Ra mất! Ra mất!」"
"1358" = "「——Chụt——chụt, chụt——chumu, chụt,\\nchụt, chuu——chụt——chumu——reru」"
"2037" = "「Fua! A——Fuuu! Fua!!」"
"2053" = "「Ha——ưm——chụt——hu, hoo he hu, haa\\n——chu ku, ưm——dai suki——re hu——huu」"
"2054" = "「Hà, hà——haaa——hà, a——haa」"
"2055" = "「Hà, haa——haa——haa—— Sâu bên trong, cô béƯ——chỉ còn, một chút, nữa thôi」"
"2078" = "「A——ưm……chuu」"
"2082" = "「A——Fua——không được——đâu ạ——sức lực không còn——nữa rồiƯ——cơ thể——cứng đờ, mất rồi」"
"2089" = "「A——vâng, vâng——đúng vậy, nhỉ, Ngài SoutetsuƯ——ưm——Fu——Fua——a」"
"2097" = "「Haaa——a——sướng, quá——a, ngon, ngon lắmƯ——ưm——dương vật——của ngài Soutetsu」"
"2101" = "「Kuaa!」"
"2109" = "「Haa! A! Thích quá! Thích quá! Ngài Soutetsu! Ngài SoutetsuƯ——Fu, a——phu quânƯ」"
"2110" = "「Haa! Haa! Haaa! Fua!?」"
"2120" = "「Chụt——liếm——mút——chuuuu——\\nchóp chép——（Ực）——ưm——chụt, chụt」"
"2122" = "「Chu——ju——juru——juuu——\\nƯm——rerooo——reru——reruuuuu」"
"2134" = "「Juru——（Ực）——ưm——\\nPhu he hyuu ho ha hi ha phu, hoo he phu ha ha」"
"2136" = "「Chiro, pero, pero, pero, rero——\\nƯm——pero, pero——pero, pero, pero, pero」"
"2144" = "「Ưm——Fu——a——ưm, ư——ưm ư, Ngài Soutetsu——của ngài Soutetsu——dương vậtƯ」"
"2151" = "「Ưm——xong, rồi. Của ngài Soutetsu, to quá—— Fu……a……chỉ lấy ra từ cửa sổ thôi——mà cũngƯ」"
"2156" = "「Ưm……chụt——chumu——chụt——ưm——\\nliếm——liếm láp——chóp chép——liếm——chu pu」"
"2178" = "「Kyukuuuuu~~~!!」"
"2180" = "「Ưm kyu!!?\\nFuaaaaaaaaaaaaaaaaa!!」"
"2289" = "「Là khe hở——giữa hai chân——của em——ưm,\\nFu——a——ư——haa——là cô bé, ạ」"
"2319" = "「Cô bé——của em——Fu, a, đang chảy——rất nhiều——nước dãi——thế nàyƯ」"
"2378" = "「Hahi——ưm, ư——Fu, a——\\nVâng! Ngài Soutetsu!!!」"
"2613" = "「Dương vật——ưm. Thật to——Fu, a, phần——nhô ra——đã vào trong——cô bé, rồiƯ」"

## Ghi chú của parent (kiểm chứng khi gộp, 21/11 ~10:00)

- Kiểm chứng: JSON 26 mục dạng chuẩn, khóa string; khối TOML 26 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 26/26; TOML md5 bcbf02a0308ddac5d5aca3ac1cd717ce khớp audit; 9 key trùng audit chỉ khác giá trị audit ở đúng token rên; mọi Ư thêm vào đều là Ư của audit (9/9); không dòng "Kh" nào bị đổi; lượt soát 2: 26/26, 0 bỏ, 0 sửa.
- **SỬA 2101:** fix "Aa!" → "Kuaa!" (JP くああ có phụ âm く; TW 啊啊 bỏ k nhưng JP thắng TW theo quy tắc đã chốt; tiền lệ cùng file 2178 khôi phục phụ âm bị mất, và file mikuro diễn くあ thành "Kua"). Đã sửa wrong.json + "Mới:" §3 + khối TOML + snippet.
- **CỜ 1883 ĐÃ GIẢI QUYẾT (không còn mâu thuẫn):** agent đọc nhầm old_vn thành fix — audit wrong.json 1883 có old_vn "là do anh" và fix "là do tôi"; audit REVIEW khối TOML và ROUTE-AUDIT.md đều ghi "là do tôi". Giá trị đã merge là "là do tôi" (đại từ Soutetsu "tôi" với Hachiroku, đúng quy tắc). Không cần quyết thêm. Phần moan của 1883 không đổi.
- Đếm nguyên âm kiểm chứng độc lập: 2180 17 a, 2178 6 u, 2122 5 u, 2120 4 u, 2078 2 u, 2097 3 a, 2110 2/2/3 a, 2055 2 a ×3, 2054 3 a + 2 a, 2037 3 u — đều khớp.

## Kết bài

File ハチロクh9: đọc 613/613 dòng, xét 100 dòng rên/SFX, đổi 26 dòng (13 romaji + 9 đếm nguyên âm + 4 sai âm), giữ 74 dòng. Không đụng dòng Ư gasp nào, không đổi dòng "Kh" nào. 7 cờ ghi ở §6 (1 mâu thuẫn audit ở 1883 cần parent kiểm tra; còn lại để đợt thống nhất). Sau file này tổng moan là 7 file / 182 dòng (cơ sở 6 file / 156 dòng + 26 file này).
