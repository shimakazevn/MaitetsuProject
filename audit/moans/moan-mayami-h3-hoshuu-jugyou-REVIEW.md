# Moan-fix REVIEW — 真闇h3_補習授業の廃校舎 (mayami-h3-hoshuu-jugyou)

## 1. Xác minh file

- File: `真闇h3_補習授業の廃校舎.txt.toml` — `sources/toml2/translation_toml/05_Mayami/#U771f#U95c7h3_#U88dc#U7fd2#U6388#U696d#U306e#U5ec3#U6821#U820e.txt.toml`.
- TOML md5: `679f382102d8ec0738d3e2eb97494730`. UTF-8 BOM + CRLF (1437 CRLF). 710 dòng script, key 37–4054, không key trùng, không bản trùng.
- CSV3: 1 bộ duy nhất (`translation_toml\05_Mayami\真闇h3_補習授業の廃校舎.txt.toml`), 710 dòng, 0 key trùng. VN khớp TOML 282/710 trực tiếp; 428 lệch còn lại đều do TOML-2 flatten `\n` thành khoảng trắng (đã kiểm chứng 428/428) — CSV3 là bản chính xác, dùng làm chuẩn.
- Audit đã gộp trước đó: 15 dòng sai (audit-mayami-h3, xem §3.5). Chỉ sửa moan, không re-audit.
- Sweep gasp: 8 mục cho file này (1554, 2694, 2889, 2890, 2891, 3114, 3264, 3965) — cả 8 đều đã được audit áp dụng đúng, đã kiểm chứng từng mục với JP. Không có dòng "Kh" nào trong file (quét `Kh` chỉ ra các từ tiếng Việt "không/khó/khác" — không có rendering "Kh" cho っ).

## 2. Kho rên (moan inventory)

- Đã đọc 710/710 dòng. Quét ứng cử viên: 233 dòng (mẫu rên/SFX trên JP + VN) + 44 dòng quét bổ sung (nguyên âm dài, nói ngọng) = 277 dòng xét kỹ.
- Xác định 145 dòng rên/SFX: 42 dòng đổi + 103 dòng giữ.
- 42 dòng đổi, theo loại: romaji 23, đếm nguyên âm 14, sai âm (mất phụ âm mora) 4, gasp 1.
- Kiểu lỗi chính: (a) tách một âm rên duy nhất thành nhiều mảnh rời ("Fua a a a…", "rero o o o", "Ưn ư ư…", "A a a") — gộp thành một cách diễn romaji; (b) diễn lai romaji + tiếng Việt trong một âm ("Hiaư", "Haư", "faư", "Nhyư ư ư…") — thuần romaji; (c) sai/mất đếm nguyên âm (はぁっ "Há" 1a, ちゅうううううっ "Chuuuu" 4u, 双ちゃぁん "Sou-chaaan" 3a); (d) mất phụ âm mora đầu âm (か―― "A", ぬ―― "Ư", ちゅるっ "chụt", んふふ "Ufufu").

## 3. Các dòng sửa (42 dòng)

### 3.1 Romaji — gộp mảnh rời / thuần romaji (23 dòng)

**2182 — 真闇 — ひあうっ → "Hiaư!?" thành "Hiau!?"**
- JP: 「ひあうっ！！？」
- TW: 「呀啊！！？」
- Cũ: 「Hiaư!?」
- Mới: 「Hiau!?」
- Lý do: "Hiaư" lai romaji + ư Việt; ひあう = "Hiau" thuần romaji (quy tắc một âm = một cách diễn).

**2184 — 真闇 — ひゃあああん mất ん**
- JP: 「ひゃあああん――とけ、ちゃうっ――からだ――\nおねえ、ちゃんっ――おにく――どろって、しちゃう」
- TW: 「呀嗯――身體――彷彿要融化了――姐姐――的肉――要融化了」
- Cũ: 「Hyaaa――tan, chảy mất――cơ thể――\nchị, á――thịt――sắp nhão ra, mất rồi.」
- Mới: 「Hyaaaan――tan, chảy mất――cơ thể――\nchị, á――thịt――sắp nhão ra, mất rồi.」
- Lý do: ひゃあああん = 4 nguyên âm a (ひゃ 1 + あ×3) + ん 1; bản cũ "Hyaaa" 3a và mất hẳn ん cuối. Chỉ đổi token rên đầu dòng; "chị, á" cho おねえ、ちゃんっ giữ nguyên (っ đã diễn thành "á").

**2198 — 真闇 — れろおおお/れろおおおお tách mảnh**
- JP: 「ぺろっ――れろおおおっ――ぺろっ、ぺちゅっ。\nチュルッ――ちゅっ――れろおおおおっ――れるっ」
- TW: 「呸嘍――呸嘍――呸囉、呸啾。啾嚕――啾――呸嘍――舔」
- Cũ: 「Pero――rero o o o――pero, pechu.\nChuru――chu――rero o o o o――reru.」
- Mới: 「Pero――reroooo――pero, pechu.\nChuru――chu――rerooooo――reru.」
- Lý do: れろおおお = 4 o (ろ 1 + お×3), れろおおおお = 5 o; bản cũ tách thành mảnh rời "rero o o o" (đúng đếm, sai dạng — tiền lệ ふかみh1). "Pero/pechu/Churu/chu" giữ nguyên.

**2199 — 双鉄 — ひははひはふ thiếu một âm "ha"**
- JP: 「ひははひはふ」
- TW: 「呼，呼，呼」
- Cũ: 「Hihahihafu.」
- Mới: 「Hihahahihafu.」
- Lý do: JP 6 mora hi-ha-ha-hi-ha-fu; bản cũ chỉ có 5 âm tiết (thiếu "ha" thứ hai). Đây là tiếng cười (không phải nói ngọng miệng đầy như 2898 — xem §5).

**2208 — 双鉄 — ぅあ "Ưa" thành "Ua"**
- JP: 「ぅあ」
- TW: 「哇」
- Cũ: 「Ưa.」
- Mới: 「Ua.」
- Lý do: ぅあ = "Ua" romaji; "Ưa" là cách diễn Việt (tiền lệ: ぅあっ→"Ua" ở file khác; "ư a" tách mảnh → "Ua").

**2212 — 真闇 — あああ "a a a" thành "aaa"**
- JP: 「はっ――あ、あっ、あああ――んっ――そこ、\nば、され、たら――ふっ――あ――ぞわ、って」
- TW: 「哈――啊、啊、啊啊啊――嗯――那裡，插那裡的話――呼――啊――好棒」
- Cũ: 「Há――a, á, a a a――ưm――chỗ đó,\nbị, chạm, vào――phù――a――rùng mình, mất.」
- Mới: 「Há――a, á, aaa――ưm――chỗ đó,\nbị, chạm, vào――phù――a――rùng mình, mất.」
- Lý do: あああ (không dấu phẩy trong JP) bị tách thành 3 mảnh rời; gộp thành "aaa". "a, á" cho あ、あっ giữ nguyên (JP có dấu 、 nên giữ dấu phẩy).

**2215 — 真闇 — ふぁうっ "faư" thành "fau"**
- JP: 「はっ――ん――ふっ――あっ――おねえ、ちゃんっ、\nふぁうっ――ふあっ――そこ、ば――押されたらっ」
- TW: 「哈――嗯――呼――啊――姐姐，哇――嗚啊――那裡――不能壓啊」
- Cũ: 「Há――ưm――phù――á――chị, á,\nfaư――fua――chỗ đó――bị ép vào thì.」
- Mới: 「Há――ưm――phù――á――chị, á,\nfau――fua――chỗ đó――bị ép vào thì.」
- Lý do: ふぁう = "fau" thuần romaji; "faư" lai romaji + ư Việt. "fua" cho ふあっ giữ nguyên (file này dùng romaji "Fua/fua" cho họ ふぁ/ふあ — tiền lệ giữ ở nhiều file).

**2227 — 真闇 — はうっ "Haư" thành "Hau"; んんっ "ưm ưm" thành "ưmm"**
- JP: 「はうっ！？　あつっ――んっ――んんっ――あっ」
- TW: 「哈！？　好熱――嗯――嗯嗯――啊」
- Cũ: 「Haư!? Nóng――ưm――ưm ưm――á.」
- Mới: 「Hau!? Nóng――ưm――ưmm――á.」
- Lý do: はう = "Hau" thuần romaji ("Haư" lai); んんっ = 2 mora ん → "ưmm" (tiền lệ 凪h2 1604; "ưm ưm" tách một âm mũi duy nhất thành 2 mảnh).

**2270 — 真闇 — ああ "A a" thành "Aa"**
- JP: 「ああ……」
- TW: 「啊啊……」
- Cũ: 「A a……」
- Mới: 「Aa……」
- Lý do: tách mảnh; gộp thành "Aa" (2a).

**2271 — 双鉄 — あああ "A a a" thành "Aaa"**
- JP: 「あああ」
- TW: 「啊啊」
- Cũ: 「A a a.」
- Mới: 「Aaa.」
- Lý do: tách mảnh; gộp thành "Aaa" (3a).

**2272 — 双鉄 — ああああああああ tách mảnh**
- JP: 「ああああああああっっっ！！！」
- TW: 「啊啊啊啊啊啊！！！」
- Cũ: 「A a a a a a a á!!!」
- Mới: 「Aaaaaaaa!!!」
- Lý do: 8a, đếm đúng (7 a thường + 1 á) nhưng tách mảnh; gộp thành "Aaaaaaaa" (8a). っ×3 cuối đã diễn ngầm (quy tắc 3b).

**2273 — 双鉄 — ぁぁぁあああ tách mảnh**
- JP: 「ぁぁぁあああっ！！？」
- TW: 「啊啊啊啊啊啊！！？」
- Cũ: 「A a a a a á!!?」
- Mới: 「Aaaaaa!!?」
- Lý do: 6a, đếm đúng nhưng tách mảnh; gộp thành "Aaaaaa" (6a).

**2274 — 真闇 — あああっ "A a a!" thành "Aaa!" (thay thế giá trị audit)**
- JP: 「あああっ！　そこっ――ゆっくり、いけん、のっ！\nいま、いまっ、おまんこ――いっぱい、やけんっ！」
- TW: 「啊啊啊！　那裡――慢慢地，嗯！快、快，射滿我的――小穴！」
- Cũ (CSV3): 「A a a! Chỗ đó――chậm lại, không được, đâu!\nBây giờ, bây giờ, âm hộ――sắp đầy, mất rồi!」
- Mới (trên giá trị audit — giữ "đầy ắp"): 「Aaa! Chỗ đó――chậm lại, không được, đâu!\nBây giờ, bây giờ, âm hộ――đầy ắp, mất rồi!」
- Lý do: chỉ thay đúng 1 token rên trong giá trị audit; phần nghĩa "đầy ắp" của audit giữ nguyên.

**2277 — 真闇 — はうっ "Haư" thành "Hau"**
- JP: 「はうっ」
- TW: 「啊嗚」
- Cũ: 「Haư.」
- Mới: 「Hau.」
- Lý do: はう = "Hau" thuần romaji ("Haư" lai).

**2278 — 真闇 — んくゅうぅぅぅぅぅぅぅぅぅぅんっ gộp mảnh + đếm**
- JP: 「あっ！　んくゅうぅぅぅぅぅぅぅぅぅぅんっ！！！」
- TW: 「啊！　嗯、咕溜、嗯！！！」
- Cũ: 「Á! Ưn kư ư ư ư ư ư ư ư ư ư ưn!!!」
- Mới: 「Á! Nkyuuuuuuuuuuuun!!!」
- Lý do: ん + くゅ(1u) + う(1u) + ぅ×10 + ん = 12u + 2n; bản cũ lai (Ưn/kư/ư) + tách mảnh + thừa 1 ư (13 ư so với 12u JP). Gộp thành romaji thuần "Nkyuuuuuuuuuuuun" (12u, 2n).

**2305 — 双鉄 — く――ううっ "Kư――ư ư!" thành "Ku――uu!"**
- JP: 「く――ううっ！」
- TW: 「嗚――嗚嗚！」
- Cũ: 「Kư――ư ư!」
- Mới: 「Ku――uu!」
- Lý do: く(1u) + うう(2u) = 3u; "Kư――ư ư" lai + tách mảnh. "Ku――uu!" đủ 3u, một cách diễn.

**2307 — 双鉄 — うぁ "Ưa" thành "Ua"; あああ "a a a" thành "aaa"**
- JP: 「うぁ――あっ――あああ――あっ――」
- TW: 「嗚啊――啊――啊啊啊――啊――」
- Cũ: 「Ưa――á――a a a――á――」
- Mới: 「Ua――á――aaa――á――」
- Lý do: うぁ = "Ua" thuần romaji; あああ tách mảnh → "aaa" (3a).

**2308 — 真闇 — うあ "Ưa" thành "Ua" (thay thế giá trị audit)**
- JP: 「うあ……どろっ、どろ――んっ――（すんっ、すん）\nふぁ……双ちゃんの……おとこの……ひとの……匂い」
- TW: 「嗚啊……黏黏糊糊的――嗯――（嗅、嗅）哇……小雙……男孩子……的氣味」
- Cũ (CSV3): 「Ưa……nhớt, nhớp nháp――ưm――（khịt, khịt）\nFua……mùi của……đàn ông……của……Sou-chan.」
- Mới (trên giá trị audit — giữ thứ tự từ audit sửa): 「Ua……nhớt, nhớp nháp――ưm――（khịt, khịt）\nFua……mùi của Sou-chan……mùi đàn ông……mùi của một con người.」
- Lý do: chỉ thay đúng 1 token rên trong giá trị audit; "Fua" cho ふぁ…… giữ nguyên.

**2310 — 真闇 — ふああああああああんんんっっっっ gộp mảnh + đếm**
- JP: 「ふああああああああんんんっっっっ」
- TW: 「嗚啊啊啊啊啊啊嗯嗯嗯」
- Cũ: 「Fua a a a a a a a a ưm ưm ưm」
- Mới: 「Fuaaaaaaaannn」
- Lý do: ふあ(1a) + あ×7 = 8a, ん×3; bản cũ 9a (thừa 1a) + tách mảnh + "ưm ưm ưm" lai. Gộp thành romaji thuần "Fuaaaaaaaannn" (8a, 3n).

**2311 — 真闇 — ああああああ "a a a a a á" thành "aaaaaa"; んうううっ "Ưn ư ư ư" thành "Nuuu"**
- JP: 「ふあっ！　あっ――ああああああっ！　んうううっ」
- TW: 「嗚啊！　啊――啊啊啊啊啊啊！　嗯嗚」
- Cũ: 「Fua! Á――a a a a a á! Ưn ư ư ư」
- Mới: 「Fua! Á――aaaaaa! Nuuu」
- Lý do: ああああああ = 6a, tách mảnh → "aaaaaa"; んうううっ = ん + う×3 → "Nuuu" thuần romaji ("Ưn ư ư ư" lai + tách mảnh). "Fua!"/"Á" giữ nguyên.

**2312 — 真闇 — あああっ "A a a" thành "Aaa"; んんっ "Ưm" thành "Ưmm"**
- JP: 「ふあっ！　あっ！　あっ！　あっ！　\nあっ！　あっ！　んんっ！　あああっ！！」
- TW: 「嗚啊！　啊！　啊！　啊！啊！　啊！　嗯嗯！　啊啊啊！！」
- Cũ: 「Fua! Á! Á! Á!\nÁ! Á! Ưm! A a a!!」
- Mới: 「Fua! Á! Á! Á!\nÁ! Á! Ưmm! Aaa!!」
- Lý do: あああっ = 3a tách mảnh → "Aaa"; んんっ = 2 mora ん → "Ưmm" (bản cũ "Ưm" mất 1 ん; tiền lệ 凪h2 1604).

**2334 — 真闇 — んんっ "ưm ưm" thành "ưmm"**
- JP: 「ん……ちゅっ――んんっ――ぷあっ――\nおいしくは、なかけど――ん――ちゅるっ（ごくっ）」
- TW: 「嗯……啾――嗯嗯――噗啊――雖然不太好喝啦――嗯――啾（咕嘟）」
- Cũ: 「Ưm……chu――ưm ưm――pua――\nDù không, ngon lắm――ưm――churu（ực）」
- Mới: 「Ưm……chu――ưmm――pua――\nDù không, ngon lắm――ưm――churu（ực）」
- Lý do: んんっ = 2 mora ん → "ưmm"; "ưm ưm" tách một âm mũi duy nhất thành 2 mảnh.

**2346 — 真闇 — んひゅううううううううううっっ gộp mảnh**
- JP: 「んひゅううううううううううっっ！！！！」
- TW: 「嗯呀！！！！」
- Cũ: 「Nhyư ư ư ư ư ư ư ư ư ư ư!!!!」
- Mới: 「Nhyuuuuuuuuuuu!!!!」
- Lý do: ひゅ(1u) + う×10 = 11u; bản cũ đúng đếm (11 ư) nhưng lai (Nhy + ư) + tách mảnh. Gộp thành romaji thuần "Nhyuuuuuuuuuuu" (11u).

**2355 — 真闇 — んうううううううぅぅぅぅっ gộp mảnh**
- JP: 「んうううううううぅぅぅぅっ！！！」
- TW: 「嗯嗚！！！」
- Cũ: 「Ưn ư ư ư ư ư ư ư ư ư ư!!!」
- Mới: 「Nuuuuuuuuuuu!!!」
- Lý do: う×7 + ぅ×4 = 11u; bản cũ đúng đếm (11 ư) nhưng lai + tách mảnh. Gộp thành romaji thuần "Nuuuuuuuuuuu" (11u).

### 3.2 Đếm nguyên âm (14 dòng)

**2211 — 真闇 — そうちゃあぁんっ "Sou-chaaaan" (4a) thành "Sou-chaaan" (3a)**
- JP: 「は――あっ――双ちゃん――そうちゃあぁんっ」
- TW: 「哈――啊――小雙――小雙」
- Cũ: 「Há――á――Sou-chan――Sou-chaaaan.」
- Mới: 「Há――á――Sou-chan――Sou-chaaan.」
- Lý do: ちゃ(1a) + あ + ぁ = 3a; bản cũ 4a (thừa 1a). は―― "Há" (1a) giữ nguyên.

**2218 — 真闇 — はぁっ "Há" (1a) thành "Haa" (2a)**
- JP: 「はぁっ――きて、来てる――双ちゃんの――\nあつい、の――おちん、ちん――ふ、あっ――」
- TW: 「哈――快來、來了――小雙――熱乎的――雞雞――呼、啊――」
- Cũ: 「Há――vào, vào rồi――của Sou-chan――\nnóng, quá――dương, vật――fua, á――」
- Mới: 「Haa――vào, vào rồi――của Sou-chan――\nnóng, quá――dương, vật――fua, á――」
- Lý do: はぁっ = は(1a) + ぁ(1a) = 2a; bản cũ "Há" mất 1a (tiền lệ: はぁっ "Hà"→"Haa" ở file khác). "fua, á" cho ふ、あっ giữ nguyên (JP có dấu 、).

**2225 — 真闇 — はぁっ/はあっ "Há! Há! Há!" thành "Haa! Haa! Haa!"**
- JP: 「はぁっ！　はあっ！　はあっ！　ひあっ！！？」
- TW: 「哈！　蛤啊！　蛤啊！　咿啊！！？」
- Cũ: 「Há! Há! Há! Hia!?」
- Mới: 「Haa! Haa! Haa! Hia!?」
- Lý do: はぁっ và はあっ đều = 2a; bản cũ 1a mỗi âm (mất 3a tổng). ひあっ "Hia" giữ nguyên (romaji đúng).

**2268 — 双鉄 — ああ―― "A――" thành "Aa――"**
- JP: 「ああ――」
- TW: 「啊啊――」
- Cũ: 「A――」
- Mới: 「Aa――」
- Lý do: ああ = 2a; bản cũ 1a (dấu ―― trong JP đã có sẵn, không thay cho nguyên âm thứ hai).

**2269 — 双鉄 — ああ―― "A――" thành "Aa――"**
- JP: 「ああ――うむ」
- TW: 「啊啊――嗯」
- Cũ: 「A――ừm.」
- Mới: 「Aa――ừm.」
- Lý do: như 2268; うむ "ừm" giữ nguyên (tiếng ừm Việt cho grunt suy nghĩ).

**2288 — 真闇 — ちゅうううううっ "chuuuuu" (5u) thành "chuuuuuu" (6u)**
- JP: 「ちゅうっ――ちゅっ――はむっ、あむっ――んっ\nちゅろおっ、ちゅろ、ころっ――ちゅうううううっ」
- TW: 「啾――啾――啊嗚、啊嗚――嗯啾囉、啾囉、咕溜――啾」
- Cũ: 「Chuu――chu――hamu, amu――ưm\nchuroo, churo, koro――chuuuuu.」
- Mới: 「Chuu――chu――hamu, amu――ưm\nchuroo, churo, koro――chuuuuuu.」
- Lý do: ちゅ(1u) + う×5 = 6u; bản cũ 5u (thiếu 1u). "churoo" cho ちゅろおっ (2 o) giữ nguyên.

**2295 — 真闇 — ちゅうううううっ "Chuuuu" (4u) thành "Chuuuuuu" (6u)**
- JP: 「じゅぼっ！　じゅぶっ！　じゅっ！　じゅぶぶっ！\nじゅぼっ！　ちゅううううっ！　じゅ！　じゅばっ！」
- TW: 「啾啵！　啾噗！　啾！　啾噗！啾啵！　啾！　啾！　啾叭！」
- Cũ: 「Jubo! Jubu! Ju! Jububu!\nJubo! Chuuuu! Ju! Juba!」
- Mới: 「Jubo! Jubu! Ju! Jububu!\nJubo! Chuuuuuu! Ju! Juba!」
- Lý do: ちゅ(1u) + う×5 = 6u; bản cũ 4u (thiếu 2u).

**2300 — 双鉄 — ああ "A." thành "Aa."**
- JP: 「ああ」
- TW: 「喔」
- Cũ: 「A.」
- Mới: 「Aa.」
- Lý do: ああ độc lập (tiếng thở dài sau cảnh oral) = 2a; bản cũ 1a. Các ああ trong thoại thường (2301/2304/2314/2360/2388/2405/2412/2705/2710/2836) là từ đệm diễn ngôn, giữ nguyên dạng "A/À" (xem §4).

**2306 — 真闇 — 双ちゃぁん "Sou-chaaan" (3a) thành "Sou-chaan" (2a)**
- JP: 「ふあっ――あっ――あっ――\n双ちゃん……双ちゃぁん」
- TW: 「嗚啊――啊――啊――小雙……小雙」
- Cũ: 「Fua――á――á――\nSou-chan……Sou-chaaan.」
- Mới: 「Fua――á――á――\nSou-chan……Sou-chaan.」
- Lý do: ちゃ(1a) + ぁ(1a) = 2a; bản cũ 3a (thừa 1a). "Fua"/"á" giữ nguyên.

**2330 — 真闇 — ちゅう…… "chu……" thành "chuu……"**
- JP: 「ん……は、ぁ……いけん、よ？　双ちゃん。ね？\nあっ！？　ちゅっ――ちゅむっ――ちゅう……れるっ」
- TW: 「嗯……哈、啊……不行喔？　小雙。好嗎？啊！？　啾――啾唔――啾……舔」
- Cũ: 「Ưm……ha, a……không được, đâu? Sou-chan. Nè?\nA!? Chụt――chumu――chu……rột.」
- Mới: 「Ưm……ha, a……không được, đâu? Sou-chan. Nè?\nA!? Chụt――chumu――chuu……rột.」
- Lý do: ちゅう = ちゅ(1u) + う(1u) = 2u; bản cũ "chu" 1u (thiếu 1u). "ha, a" cho は、ぁ giữ nguyên (JP có dấu 、).

**2472 — 真闇 — 双ちゃんんっ "Sou-chan!" thành "Sou-chann!"**
- JP: 「来てっ！　双ちゃんんっ！　おね、ちゃんっ、\nもう―イク――イっちゃう――けんっ――ふあっ！！」
- TW: 「射吧！　小雙！　姐姐，要高潮――高潮了――嗯――嗚啊！！」
- Cũ: 「Đến đi! Sou-chan! Chị, chị,\nsắp―ra――ra mất――rồi――fua!!」
- Mới: 「Đến đi! Sou-chann! Chị, chị,\nsắp―ra――ra mất――rồi――fua!!」
- Lý do: 双ちゃん + ん (mũi kéo dài) + っ (cắt); bản cũ mất hẳn ん. "Sou-chann!" giữ 2n; "!" diễn っ. "fua!!" giữ nguyên.

**2686 — 双鉄 — (xem §3.3; đếm kèm: ぬ―― "Ư" thành "Nuu")**

**2776 — 真闇 — はぁぁ "Haa" (2a) thành "Haaa" (3a)**
- JP: 「はぁぁ――すきっ――好き、双ちゃんっ――\nおねえちゃん、おねえちゃん――最初から――ふあっ！」
- TW: 「蛤啊――喜歡――喜歡你，小雙――姐姐、姐姐――一開始就喜歡你――嗚啊！」
- Cũ: 「Haa――thích――thích lắm, Sou-chan――\nchị, chị――ngay từ đầu đã――fua!」
- Mới: 「Haaa――thích――thích lắm, Sou-chan――\nchị, chị――ngay từ đầu đã――fua!」
- Lý do: はぁぁ = は(1a) + ぁ×2 = 3a; bản cũ 2a (thiếu 1a).

**4019 — monologue — ぐうううっ "Gư ư ư!" thành "Guuuu!"**
- JP: （ぐうううっ！　ごちゅうううううううううっん！！）
- TW: （咕！　咕啾！！）
- Cũ: （Gư ư ư! Phập!!）
- Mới: （Guuuu! Phập!!）
- Lý do: ぐ(1u) + う×3 = 4u; bản cũ 3 ư tách mảnh. Chỉ đổi SFX đầu (diễn âm); SFX sau "Phập!!" giữ nguyên (dạng nghĩa Việt cho ごちゅうううううううううっん — quy ước SFX ngoặc, xem §4).

### 3.3 Sai âm — mất phụ âm mora (4 dòng)

**2249 — 真闇 — か―― "A――" thành "Ka――"**
- JP: 「か――はっ――あっ――ふあっ！　おくっ、ん、\nおくっ――きてる――子宮、に――子宮にぃっ！！」
- TW: 「啊――哈――啊――嗚啊！　深處、深處――來了――子宮――子宮！！」
- Cũ: 「A――há――á――fua! Sâu quá, ưm,\nsâu quá――đến rồi――tử cung, vào――tử cung rồi!!」
- Mới: 「Ka――há――á――fua! Sâu quá, ưm,\nsâu quá――đến rồi――tử cung, vào――tử cung rồi!!」
- Lý do: か―― là tiếng nấc cụt đầu âm "ka"; bản cũ "A" mất hẳn phụ âm k (tiền lệ: mất âm いっ/ぎっ → "I――Gi!" ở file khác). "há/á/fua" giữ nguyên.

**2352 — 真闇 — んふふ "Ufufu" thành "Nfufu"**
- JP: 「んふふ――おかえし。（ちゅっ！）」
- TW: 「嗯唔――回你一個。（啾！）」
- Cũ: 「Ufufu――trả lại nè. (Chụt!)」
- Mới: 「Nfufu――trả lại nè. (Chụt!)」
- Lý do: んふふ = "Nfufu" (một âm, một cách diễn; tiền lệ んふふっ "ưm fufu"→"Nfufu" ở file khác). "Ufufu" mất ん đầu. Cười là tiếng cười, không phải rên (quy tắc Hieu 19/11).

**2363 — 真闇 — ちゅるっ "chụt" thành "churu"**
- JP: 「んっ！？　ふっ――あむっ――れろっ――ちゅるっ、\nちゅっ――れるっ――じゅむっ――ちゅ、ちゅううっ」
- TW: 「嗯！？　呼――啊嗚――舔――啾、啾――舔――啾――啾、啾」
- Cũ: 「Ưm!? Phư――amu――rột――chụt,\nchụt――rột――jumu――chu, chuuu.」
- Mới: 「Ưm!? Phư――amu――rột――churu,\nchụt――rột――jumu――chu, chuuu.」
- Lý do: ちゅるっ = "churu" (2 mora); bản cũ "chụt" (SFX hôn "chụt" của ちゅっ) làm mất mora る và trùng hẳn với ちゅっ ngay sau đó. Quy ước file: ちゅるっ → "churu" (2276/2290/2336). "rột" cho れろっ/れるっ giữ nguyên (onomatopoeia Việt cho tiếng liếm, quy ước SFX).

**2686 — 双鉄 — ぬ―― "Ư" thành "Nuu"**
- JP: 「ぬ――むっ――このっ！」
- TW: 「溜――嗯――媽的！」
- Cũ: 「Ư――ưm――cái này!」
- Mới: 「Nuu――ưm――cái này!」
- Lý do: ぬ―― là tiếng rặn/gắng sức "nuu" (không phải gasp っ); bản cũ "Ư" mất hẳn phụ âm n và nhầm thành gasp. "Nuu" (2u: ぬ 1u + ―― kéo dài). むっ "ưm" giữ nguyên (quy ước file cho む).

### 3.4 Gasp — gasp đầu dòng sweep bỏ sót (1 dòng)

**3967 — monologue — （っ――プッ――） thêm Ư đầu**
- JP: （っ――プッ――）
- TW: （――噗――）
- Cũ: （Phập――）
- Mới: （Ư――Phập――）
- Lý do: っ đầu dòng trong ngoặc bị mất hẳn trong VN (sweep 8 mục cho file này không bao phủ trường hợp này — gasp mới, cùng mẫu "gasp bỏ sót" ở file khác). Theo ranh giới gasp: thêm Ư khi âm っ hoàn toàn mất và ở đầu dòng. "Phập" cho プッ giữ nguyên (dạng nghĩa Việt cho SFX ngoặc).

### 3.5 Trùng audit (2 dòng — chỉ thay token rên, xem §3.1)

- 2274: fix = giá trị audit, chỉ thay "A a a!" → "Aaa!" (giữ "đầy ắp").
- 2308: fix = giá trị audit, chỉ thay "Ưa……" → "Ua……" (giữ thứ tự từ audit sửa).
- Các fix audit khác có yếu tố moan đều đã đúng, không đụng: 1554 「……Ư」, 2194 「Ufufu.」, 2665 「Ufufu, nồng nhiệt…」, 2694 「Nóng quá――Ư――…fua, á――」, 2889/2890/2891 「Ư!/Ư!!/Ư!!?」, 3114/3264/3965 「――Ư!?」.

## 4. Các dòng rên giữ nguyên (103 dòng — ghi chú những dòng đáng chú ý)

- Họ ひゃ/ひゅ/ひあ/きゃ đã romaji sẵn, đúng quy tắc 21/11: 2185 "Hyan!?", 2204 "Hia!?", 2216 "hia", 2225 "Hia!?", 2249 "fua!", 2306 "Fua", 2312 "Fua!", 2352 "(Chụt!)" sau khi sửa "Nfufu".
- Họ ふぁ/ふあ đã romaji "Fua/fua" (không chuyển sang "phà/phùa" — file này dùng romaji nhất quán, tiền lệ giữ "Fua" ở nhiều file; "phà/phùa" chỉ áp trong đợt thống nhất nếu Hieu quyết): 2204, 2215, 2218, 2249, 2306, 2308, 2310, 2311, 2312, 2472, 2694 (audit), 2776.
- あっ → "Á"/"A" (cả hai dạng đều chấp nhận cho あっ không phụ âm mora; không thống nhất trong file này): 2224 "Há! Á! Á!", 2251/2256/2257/2258 "A――/á", 2285 "A!", 2306/2312 "Á!".
- はっ → "Há/há" (1a, đúng đếm): 2209 "há――há――há――haa" (はぁっ cuối đã đúng "haa" 2a), 2224, 2249, 2477.
- ふっ/ぷっ → "phù"/"phư" (hơi thở ngắn; hai thanh điệu cùng tồn tại trong file — câu hỏi mở toàn dự án, xem §5 F2): 2212/2215/2256 "phù", 2324/2348/2363/2364 "phư/Phư".
- んっ → "Ưm/ưm" (quy ước file): 2212, 2216, 2256, 2316, 2324, 2326, 2332, 2334, 2364; んっ → "ưn" (2 dòng 2323, 2328 — giữ, xem §5 F1); ん…… → "Ưm……" (2321, 2337, 2338).
- ん+X lai "ƯmX/ƯnX" không dấu cách (quy ước file, tiền lệ "Ưm + X" ở ふかみh1): 2350 "Ưmpu", 2353 "Ưnmu", 2354 "Ưmbu"; "Ưm phư" cho んふっ (2348) giữ (hai cử động phát âm, tiền lệ "Ưm fu" có dấu cách ở file khác).
- Cười là tiếng cười: 2143 "ahaha!", 2195 "Ufufu", 2352 "Nfufu" (sau sửa), 2194/2665 "Ufufu" (audit).
- SFX chuỗi miệng romaji nhất quán: 2276 "Hamu――chu――churu――koro――churu――rero, koro――koryu", 2288 "Chuu――chu――hamu, amu――ưm", 2290 "Chu――re, ru――chuu――chu, chumu", 2292 "Chu――reru――rero――churu, ru", 2299 "Juuu! Jubo! Jururu~~nyubo!", 2316 "Ưm――chu――chumu――chuu――ưm", 2332 "Ưm……chu――ưm chu――chu――chuu", 2336 "Ưm……chu――zuro――churu, ruu, ru", 2350 "Ưmpu――ưm――rero――rero, zu――ju", 2353 "Ưnmu――rero――picha, pecha――zuchu", 2357 "Ưm! Chuzu! Jubo! Bochu!!", 2363 "jumu――chu, chuuu", 2424 "Picho, pecho――chuu――perororo!".
- SFX trong ngoặc （ ） dạng nghĩa Việt (quy ước file, tiền lệ giữ ở nhiều file): 4008 "Bạch! Phập! Phịch! Sục!", 4010/4011/4024/4025/4027, 4012 "Phập――sục――phịch――hự!", 4014/4015/4016 "Phập/Trượt", 4017/4018 "Sần sật", 4022 "Chạm nhẹ", 4028 "(Chụt)", 4029 "(Cạch)", 4030 "Xoẹt――xoẹt roạt――", 4042/4043 "Siết chặt", 4047–4054 "Nắn bóp/Xoa nắn/Vuốt nhẹ/Cọ cọ/Giật! Trượt!".
- SFX romaji trong ngoặc đúng đếm: 4021 "Byubu! Byugun! Byubu! Byuru!", 4034 "Byuru! Byu! Byubu! Byuku!", 4035 "Byuru! Byuuu! Byu――byuru", 4036 "Byuruu! Byu! Byururu! Byubu!", 4038 "Byu! Bubyu! Byuru! Byuuu!", 4041 "Byuu! Byu! Bubyu! Byururu!".
- Tách âm theo dấu 、 của JP thì giữ (không phải lỗi tách mảnh): 2212 "a, á" (あ、あっ), 2215 "chị, á," (おねえ、ちゃんっ), 2218 "fua, á" (ふ、あっ), 2309 "Kua, a" (くあ、あ), 2316 "chu, mu" (ちゅ、むっ), 2330 "ha, a" (は、ぁ), 2336 "churu, ruu, ru" (ちゅる、るう、るっ), 2477 "chị, á" (おねえ、ちゃんっ), 2493 "fua, á" (ふ、あっ).
- っ nhấn mạnh cuối từ nội dung (không thêm Ư — quy tắc ranh giới gasp): 2108 そのっ―― "cái đó――", 2184 とけ、ちゃうっ "tan, chảy mất", 2258 あついのっ/たくさんっ "nóng quá/nhiều quá", 2490 双ちゃんっ―― "Sou-chan――", 2866 たらっ/けんっ "thế này!/mất thôi.", 2878 きて、るっ "đang tiến vào…rồi".
- Grunt suy nghĩ / từ đệm diễn ngôn (không phải rên, giữ nguyên): 2243 むぅ "Hừm.", 2313 ううむ―― "Ưm――", 2314/2342/2344 うむ "Ừm", 2356 ふむふむ "Hừm hừm.", 2359/2374/2376 うん/ん "Ưm/Ừm", 2419 ふむ "Hửm?", 2627 ふむふむ "Hừm hừm.", 2301/2304/2318/2360/2388/2405/2412/2674/2705/2710/2836 ああ "A/À/Ừ".
- 37 (くにっ）→ "(Bóp nhẹ）": SFX bóp dạng nghĩa, giữ.
- 2896 （ごくっ、ごく）→ "（Ực, ực）", 2897 （ごくっ）→ "(Ực)": SFX nuốt, giữ.

## 5. Cờ (flags — cho đợt thống nhất / audit, không quyết ở đây)

- F1 — んっ hai dạng "ưm" (2212/2216/2256/2316…) vs "ưn" (2323 ンッ, 2328 めっ): cùng âm ん, khác phụ âm cuối m/n. File này dùng cả hai; tiền lệ toàn dự án là "ưm". Chờ quyết thống nhất có đổi "ưn" → "ưm" không.
- F2 — ふっ hai thanh "phù" (2212/2215/2256) vs "phư" (2324/2348/2363/2364): câu hỏi mở toàn dự án (đã có ở file khác: "fu" vs "phù").
- F3 — SFX trong ngoặc （ ） chưa áp công thức đếm: 4014 ずりゅうううううううう (9u) → "Phập", 4016 つうううっ → "Trượt", 4042/4043 きゅうううううんんっ/きゅううううううううっ → "Siết chặt" — đều diễn nghĩa, độ dài JP mất. Cùng mẫu cờ F4 ở file khác; chờ quyết ranh giới diễn nghĩa vs đếm cho SFX ngoặc.
- F4 — んんっ "ưmm" (2227/2312/2334) vs "nn" romaji: tiền lệ file này theo 凪h2 ("ưmm"); có mâu thuẫn với ふかみh1 967 "Hyaaann" (3n) và cờ F8 file khác. Chờ quyết thống nhất.
- F5 — 2898 「へーんふ、ほふひひはひへ、ひょはよよ？」→ "Hén fư, hô fư hi hi ha hi hê, hyô ha yo yo?": nói ngọng miệng đầy (sau 2896–2897 nuốt), KHÔNG phải dòng rên theo quy tắc 3b — để lại cho audit, không sửa ở đây.
- F6 — 2107 「はぁい、めしあがれ」→ "Được rồi, ăn đi.": はぁい đầu câu bị bỏ hẳn (từ đệm "đây, ăn đi"). Không phải rên; ghi chú cho audit xem có bổ sung "Đây," không.
- F7 — 2199 (đã sửa "Hihahahihafu"): tiếng cười ngọng của Soutetsu; đã sửa theo dạng cười, nhưng nếu parent xem đây là nói ngọng (không phải rên) thì rút lại — khác 2898 ở chỗ không có ngữ cảnh miệng đầy.
- F8 — 2300 ああ "Aa." (đã sửa) vs 2301/2304 ああ diễn ngôn giữ "A,": ranh giới tiếng thở độc lập (sửa theo công thức) vs từ đệm diễn ngôn (giữ). Ghi lại để thống nhất.

## 6. Lượt soát 2 (second pass — đọc lại toàn bộ 42 fix với JP)

- Tổng: 42 / tái kiểm chứng 42 / bỏ 0 / sửa 0.
- Đã đọc lại từng fix với đúng JP của hàng đó, kiểm đếm lại nguyên âm bằng script (đếm mora あ/ぁ/う/ぅ/ん trong JP so với nguyên âm trong fix): 2182 Hiau, 2184 Hyaaaan (4a+1n), 2198 reroooo (4o)/rerooooo (5o), 2199 Hihahahihafu (6 âm tiết), 2211 Sou-chaaan (3a), 2218 Haa (2a), 2225 Haa×3 (2a), 2227 Hau + ưmm (2m), 2249 Ka, 2268/2269 Aa (2a), 2270 Aa (2a), 2271 Aaa (3a), 2272 Aaaaaaaa (8a), 2273 Aaaaaa (6a), 2274 Aaa (3a), 2278 Nkyuuuuuuuuuuuun (12u+2n), 2288 chuuuuuu (6u), 2295 Chuuuuuu (6u), 2300 Aa (2a), 2305 Ku――uu (3u), 2306 Sou-chaan (2a), 2307 Ua + aaa (3a), 2310 Fuaaaaaaaannn (8a+3n), 2311 aaaaaa (6a) + Nuuu (3u), 2312 Aaa (3a) + Ưmm (2m), 2330 chuu (2u), 2334 ưmm (2m), 2346 Nhyuuuuuuuuuuu (11u), 2352 Nfufu, 2355 Nuuuuuuuuuuu (11u), 2363 churu, 2472 Sou-chann (2n), 2686 Nuu (2u), 2776 Haaa (3a), 3967 Ư――Phập, 4019 Guuuu (4u) — tất cả đều khớp đếm JP.
- JSON 42 mục, khóa string, jp/tw/old_vn khớp CSV3 42/42 (1 bộ duy nhất, 710 dòng, 0 key trùng). Khối TOML parse bằng tomllib: 42 khóa, 0 sai lệch giá trị.
- Không dòng "Kh" nào bị đổi (file không có rendering "Kh"); không dòng gasp Ư nào của audit/sweep bị đụng (1554/2194/2665/2694/2889/2890/2891/3114/3264/3965 giữ nguyên giá trị audit).

## 7. Khối TOML (parse-verified, 42 khóa)

```toml
[script]
"2182" = "「Hiau!?」"
"2184" = "「Hyaaaan――tan, chảy mất――cơ thể――\\nchị, á――thịt――sắp nhão ra, mất rồi.」"
"2198" = "「Pero――reroooo――pero, pechu.\\nChuru――chu――rerooooo――reru.」"
"2199" = "「Hihahahihafu.」"
"2208" = "「Ua.」"
"2211" = "「Há――á――Sou-chan――Sou-chaaan.」"
"2212" = "「Há――a, á, aaa――ưm――chỗ đó,\\nbị, chạm, vào――phù――a――rùng mình, mất.」"
"2215" = "「Há――ưm――phù――á――chị, á,\\nfau――fua――chỗ đó――bị ép vào thì.」"
"2218" = "「Haa――vào, vào rồi――của Sou-chan――\\nnóng, quá――dương, vật――fua, á――」"
"2225" = "「Haa! Haa! Haa! Hia!?」"
"2227" = "「Hau!? Nóng――ưm――ưmm――á.」"
"2249" = "「Ka――há――á――fua! Sâu quá, ưm,\\nsâu quá――đến rồi――tử cung, vào――tử cung rồi!!」"
"2268" = "「Aa――」"
"2269" = "「Aa――ừm.」"
"2270" = "「Aa……」"
"2271" = "「Aaa.」"
"2272" = "「Aaaaaaaa!!!」"
"2273" = "「Aaaaaa!!?」"
"2274" = "「Aaa! Chỗ đó――chậm lại, không được, đâu!\\nBây giờ, bây giờ, âm hộ――đầy ắp, mất rồi!」"
"2277" = "「Hau.」"
"2278" = "「Á! Nkyuuuuuuuuuuuun!!!」"
"2288" = "「Chuu――chu――hamu, amu――ưm\\nchuroo, churo, koro――chuuuuuu.」"
"2295" = "「Jubo! Jubu! Ju! Jububu!\\nJubo! Chuuuuuu! Ju! Juba!」"
"2300" = "「Aa.」"
"2305" = "「Ku――uu!」"
"2306" = "「Fua――á――á――\\nSou-chan……Sou-chaan.」"
"2307" = "「Ua――á――aaa――á――」"
"2308" = "「Ua……nhớt, nhớp nháp――ưm――（khịt, khịt）\\nFua……mùi của Sou-chan……mùi đàn ông……mùi của một con người.」"
"2310" = "「Fuaaaaaaaannn」"
"2311" = "「Fua! Á――aaaaaa! Nuuu」"
"2312" = "「Fua! Á! Á! Á!\\nÁ! Á! Ưmm! Aaa!!」"
"2330" = "「Ưm……ha, a……không được, đâu? Sou-chan. Nè?\\nA!? Chụt――chumu――chuu……rột.」"
"2334" = "「Ưm……chu――ưmm――pua――\\nDù không, ngon lắm――ưm――churu（ực）」"
"2346" = "「Nhyuuuuuuuuuuu!!!!」"
"2352" = "「Nfufu――trả lại nè. (Chụt!)」"
"2355" = "「Nuuuuuuuuuuu!!!」"
"2363" = "「Ưm!? Phư――amu――rột――churu,\\nchụt――rột――jumu――chu, chuuu.」"
"2472" = "「Đến đi! Sou-chann! Chị, chị,\\nsắp―ra――ra mất――rồi――fua!!」"
"2686" = "「Nuu――ưm――cái này!」"
"2776" = "「Haaa――thích――thích lắm, Sou-chan――\\nchị, chị――ngay từ đầu đã――fua!」"
"3967" = "（Ư――Phập――）"
"4019" = "（Guuuu! Phập!!）"
```

## Kết bài

File 真闇h3_補習授業の廃校舎: đã đọc 710/710 dòng, xác định 145 dòng rên/SFX, đổi 42 dòng (23 romaji + 14 đếm nguyên âm + 4 sai âm + 1 gasp), giữ 103 dòng. Lỗi lớn nhất là kiểu tách mảnh rời và diễn lai romaji–tiếng Việt; đã gộp về một cách diễn romaji thuần với đếm nguyên âm kiểm chứng bằng script. Hai dòng trùng audit (2274, 2308) chỉ thay đúng token rên, giữ nguyên phần còn lại của giá trị audit. 8 mục sweep đã kiểm chứng (đều đúng, audit đã áp dụng); thêm 1 gasp sweep bỏ sót (3967). 8 cờ ghi lại cho đợt thống nhất/audit, không quyết ở đây.
