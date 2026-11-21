# Moan-fix: lr_凪h1_痛いの痛いの飛んでけばい — 34 dòng rên đổi (romaji fallback)

**Kết quả: 34/304 dòng đổi** — romaji họ fa/fu 13, gộp một âm rên bị tách mảnh 4, mất/sai âm 5, đếm nguyên âm 12. Đã đọc hết 304/304 dòng (Nagi 100, Soutetsu 70, độc thoại 134). Cảnh: Nagi luyện kiếm làm gãy kiếm gỗ, mảnh văng trúng háng Soutetsu; Nagi "thổi bay cơn đau" rồi chuyển sang H (69, Soutetsu muốn ngực Nagi to lên / ra sữa).

## Xác minh file

- TOML: `lr_#U51eah1_#U75db#U3044#U306e#U75db#U3044#U306e#U98db#U3093#U3067#U3051#U3070#U3044.txt.toml`, md5 `3b4b468a7b4e2fc41327c15a75dd230c`, BOM + CRLF, 304 dòng script, không có bản trùng nội dung trong toml2/.
- CSV3: chỉ 1 bộ 304 dòng (thư mục home `07_Nagi_Fukami`); khớp TOML 304/304 sau chuẩn hoá `\n`→khoảng trắng (TOML-2 làm phẳng `\n`; CSV3 là chuẩn). 0 dòng VN trống, 0 dòng VN == TW.
- Audit trước đó (đã gộp): 22/304 dòng sai — 19 gasp Ư + 1 lệch dòng (1121) + 1 SFX (1170) + 1 đại từ (1567). Moan-fix này chỉ gộp với audit ở đúng 2 dòng (1213, 1223: giữ Ư của audit, chỉ đổi phần rên); không đụng dòng gasp Ư nào khác, không dòng "Kh" nào bị đổi.
- Sweep: 13 mục cho file này — 9 fix đã áp nguyên trong audit, 2 already-rendered đã sửa đúng (1135, 1155), 2 needs-file-audit đã xử lý (1223, 1272); audit tự tìm thêm 6 gasp (1126, 1173, 1183, 1210, 1213, 1231). Đã đối chiếu trực tiếp `sweep-raw-gasp-wrong.json` — không còn mục sweep nào chưa xử lý.
- Kiểm kê rên: 168 dòng chứa token rên/SFX (liệt kê theo token: ふぁ/ふあ/ふぇ/ふや/ひゃ/ひゅ/ひあ/きゃ/ぁ/んひゅ/じゅ/ちゅ/ぺろ/SFX trong （）…) — Nagi 83, Soutetsu 19, độc thoại 66 (trong đó 56 dòng SFX （）). Đổi 34, giữ 134.

## Quy tắc áp dụng

Romaji fallback (Hieu duyệt 21/11 ~01:56); ふぁ→Fa, ふあ→Fua, ふぇ→Fue, ふや→Fuya, ぷあ→Pua (tiền lệ moan-lr-nagih2 — bản cũ "Fua"/"fua"/"phua" dùng chung cho cả ふぁ lẫn ふあ là **sai âm**: ふぁ = fa, ふあ = fua; tiền lệ lr-mikuro-hibiki-h 1712). Một âm = một cách diễn (không tách một âm rên duy nhất thành nhiều mảnh — tiền lệ ふかみh1); chữ hoa/thường giữ theo vị trí trong câu (đầu câu/đầu dòng viết hoa, giữa câu viết thường — tiền lệ mikuro §5). Độ dài nguyên âm theo công thức (số nguyên âm = 1 + số う/ぅ; với ぁ/あ/ー/～ đếm trực tiếp số mora). Ư cho gasp mất hẳn KHÔNG xét lại; "Kh" cho っ KEEP.

## A. Romaji họ fa/fu (13 dòng)

- **1145 [凪]** — ふぁんっ = "fan" (fa + n); bản cũ "Phuan" vừa Việt hoá vừa lẫn âm.
  JP: 「ふぁんっ！！！」
  TW: 「哇！！！」
  Cũ: 「Phuan!!!」
  Mới: 「Fan!!!」
- **1185 [凪]** — ふぁっ → "fa" (giữa câu, thường).
  JP: 「あ……ん……ふぁっ――あっ――にーさん……\nもっと――もっと、強く――んっ――強く、して」
  TW: 「啊……嗯……啊……啊……大哥哥……用力……用力點……嗯……再用力點」
  Cũ: 「A……ưm……phua――á――anh hai……\nMạnh hơn――mạnh hơn, nữa――ưm――mạnh lên, đi」
  Mới: 「A……ưm……fa――á――anh hai……\nMạnh hơn――mạnh hơn, nữa――ưm――mạnh lên, đi」
- **1143 [凪]** — ふあっ → "Fua" (đầu dòng).
  JP: 「ふあっ――あっ！　よか、ばいっ――んっ――\nにーさんの、指――いつもと、感触――違くて――んっ」
  TW: 「哇……啊！舒服……嗯……大哥哥的手指……感覺和平時……不一樣……嗯……」
  Cũ: 「Phua――á! Tuyệt, quá――ưm――\nNgón tay, của anh hai――cảm giác――khác với, mọi khi――ưm」
  Mới: 「Fua――á! Tuyệt, quá――ưm――\nNgón tay, của anh hai――cảm giác――khác với, mọi khi――ưm」
- **1180 [凪]** — ふあっ → "Fua".
  JP: 「ふあっ――あっ！　あっ！　あっ！　さわり、方っ――\nにーさんの、手……さっきより、もっと――エッチ――」
  TW: 「啊……啊！啊！啊！你的手……你的摸法比剛才更色情了……」
  Cũ: 「Phua――á! Á! Á! Cách, sờ――\nTay, của anh hai……so với lúc nãy, còn――dâm đãng hơn――」
  Mới: 「Fua――á! Á! Á! Cách, sờ――\nTay, của anh hai……so với lúc nãy, còn――dâm đãng hơn――」
- **1201 [凪]** — ふぁっ → "Fa".
  JP: 「ふぁっ！　あっ！　乳首――乳首、やさしくっ――\n指で、されるのっ――きもち――よか、と――んっ！」
  TW: 「啊！啊！乳頭……乳頭，溫柔點……手指這樣摸著……咱好舒服……嗯！」
  Cũ: 「Phua! Á! Núm vú――núm vú, được vuốt ve nhẹ nhàng――\nbằng ngón tay――sướng――quá――ưm!」
  Mới: 「Fa! Á! Núm vú――núm vú, được vuốt ve nhẹ nhàng――\nbằng ngón tay――sướng――quá――ưm!」
- **1233 [凪]** — ふあっ → "fua" (cuối dòng, giữa câu).
  JP: 「ん……はっ――おっぱい――じわじわ――ンッ――\nまわり、から――もみもみ、される、の――ふあっ！」
  TW: 「嗯……啊……胸部，都是汗……嗯……被這樣從四周揉著……啊！」
  Cũ: 「Ưm……hà――vú――từ từ――ưm――\ntừ, xung quanh――bị, xoa nắn――phua!」
  Mới: 「Ưm……hà――vú――từ từ――ưm――\ntừ, xung quanh――bị, xoa nắn――fua!」
- **1199 [凪]** — ふあっ → "Fua".
  JP: 「ふあっ！　あ――にーさん、んんっ――元気、ばい、ね、\nぶつけた、とこ――もう、痛く――んっ――なか、と？」
  TW: 「啊！啊……大哥哥，唔……你真有精神，剛剛被打到的地方……已經……嗯……不痛了嗎？」
  Cũ: 「Phua! A――anh hai, ưm――khỏe, ghê, nhỉ,\nchỗ, bị va trúng――đã, hết đau――ưm――rồi, sao?」
  Mới: 「Fua! A――anh hai, ưm――khỏe, ghê, nhỉ,\nchỗ, bị va trúng――đã, hết đau――ưm――rồi, sao?」
- **1187 [凪]** — ふぁっ → "Fa".
  JP: 「ふぁっ――にーさん、ちょっと強引すぎば――けぷっ」
  TW: 「啊……大哥哥，你太強硬了……嗝」
  Cũ: 「Phua――anh hai, hơi bạo lực quá rồi――kệpp」
  Mới: 「Fa――anh hai, hơi bạo lực quá rồi――kệpp」
- **1195 [凪]** — ふえっ → "Fue" (tiền lệ nagih2 1280); bản cũ "Huê" sai phụ âm f→h. Giữ "Pua" cho ぷあっ.
  JP: 「ぷあっ！　ふえっ！？　にーさっ――！！！？」
  TW: 「啊！哎？！大哥哥……唔？！」
  Cũ: 「Pua! Huê!? Anh ha――!!!?」
  Mới: 「Pua! Fue!? Anh ha――!!!?」
- **1236 [凪]** — ふあっ → "fua" (giữa câu). Giữ "pua" cho ぷあっ.
  JP: 「ん――ぷあっ！　あ……にーさん、ん……そぎゃん、\nされ、たら――ふあっ――凪、さま――しゅう、ちゅう」
  TW: 「嗯……啊！啊……大哥哥，嗯……你這樣，啊……本小姐的……注意力」
  Cũ: 「Ưm――pua! A……anh hai, ưm……bị, làm,\nnhư vậy――phua――Nagi, sama――tập, trung」
  Mới: 「Ưm――pua! A……anh hai, ưm……bị, làm,\nnhư vậy――fua――Nagi, sama――tập, trung」
- **1158 [凪]** — ふあ―― → "Fua" (đầu câu sau "! ").
  JP: 「んくっ！　ふあ――あっ――んっ――（はむっ！）\nじゅるっ――ちゅぶっ！　じゅる！　じゅばっ！！」
  TW: 「唔！啊……啊……嗯……（含！）啾……啾！啾！啾！！」
  Cũ: 「Ưm ku! Phua――á――ưm――（Ngoạm!）\nJuru――chubu! Juru! Juba!!」
  Mới: 「Ưm ku! Fua――á――ưm――（Ngoạm!）\nJuru――chubu! Juru! Juba!!」
- **1162 [凪]** — ふぁっ → "fa" (giữa câu).
  JP: 「んくっ！？　ぷっ――ふぁっ――ンッ――じゅる！\nじゅぼっ！　じゅぶっ！　じゅばっ！　ちゅううっ」
  TW: 「唔？！噗……啊……嗯……啾！啾！啾！啾！啾」
  Cũ: 「Ưm ku!? Pu――phua――ưm――juru!\nJubo! Jubu! Juba! Chuuuu」
  Mới: 「Ưm ku!? Pu――fa――ưm――juru!\nJubo! Jubu! Juba! Chuuuu」
- **1129 [凪]** — ふやっ → "Fuya" (tiền lệ nagih2 giữ "fuya" cho ふやっ, hủy "phuya" của audit).
  JP: 「ふやっ！　あっ！　あっ！　んっ――（はぷっ！！）」
  TW: 「呀！啊！啊！嗯……（含！！）」
  Cũ: 「Phuya! Á! Á! Ưm――（Hapu!!）」
  Mới: 「Fuya! Á! Á! Ưm――（Hapu!!）」

## B. Một âm rên bị tách thành nhiều mảnh → gộp một cách diễn (4 dòng)

- **1157 [凪]** — んひゅんっ là MỘT âm; bản cũ tách "Ưm hyun". Quy tắc 3b: んひゅん→"Nhyun".
  JP: 「んひゅんっ！！！？」
  TW: 「唔嗯？！」
  Cũ: 「Ưm hyun!!!?」
  Mới: 「Nhyun!!!?」
- **1161 [凪]** — んひゅんんっ = "Nhyunn" (n + hyu + n + n).
  JP: 「んひゅんんっ！！！！」
  TW: 「唔！！！！」
  Cũ: 「Ưm hyun!!!!」
  Mới: 「Nhyunn!!!!」
- **1242 [凪]** — くひゅんっ là MỘT âm; bản cũ tách "Khu hyun".
  JP: 「くひゅんっ！！！」
  TW: 「嗯！！！」
  Cũ: 「Khu hyun!!!」
  Mới: 「Kuhyun!!!」
- **1234 [凪]** — ふぁはぁっ là MỘT âm (fa-haa); bản cũ tách "phu haa".
  JP: 「んっ――ふぁはぁっ」
  TW: 「嗯……啊啊」
  Cũ: 「Ưm――phu haa」
  Mới: 「Ưm――Fahaa」

## C. Mất/sai âm (5 dòng)

- **1190 [凪]** — ふあっ bị dịch thành "a!" — mất hẳn phụ âm f. Sửa thành romaji "fua!" (giữa câu, thường).
  JP: 「あ……もう、ちょっと――んっ――くっ――ふあっ！\nも、ちょっとで――おまんこの、おく――おちん、ちん」
  TW: 「啊……還差一點……嗯……唔……啊！還差一點……雞雞……就能進到……最深處了」
  Cũ: 「A……Sắp, được rồi——ưm——hự——a!\nMột, chút nữa thôi——là vào đến, tận cùng——bên trong, rồi」
  Mới: 「A……Sắp, được rồi——ưm——hự——fua!\nMột, chút nữa thôi——là vào đến, tận cùng——bên trong, rồi」
- **1216 [凪]** — ぺろっ → "rero" ×5: mất phụ âm p (ぺ = pe, không phải re). Cùng file ぺちょっ → "pecho" vẫn giữ p — "rero" là sai âm. Sửa cả 5 chỗ → "pero".
  JP: 「ぴちゃっ――ぺろっ――ぺろっ――ぺろっ――\nれりゅっ――ぺちょっ――ぺろっ――ぺろっ――」
  TW: 「啾……啾……啾……啾……啾……啾……啾……啾……」
  Cũ: 「Picha――rero――rero――rero――\nreryu――pecho――rero――rero――」
  Mới: 「Picha――pero――pero――pero――\nreryu――pecho――pero――pero――」
- **1219 [凪]** — ぢゅぼっ → "Chubo": ぢゅ = "ju" (hữu thanh), không phải "chu". File dùng "J-" cho じゅ nhất quán (Jubu/Juru/Ju) nên ぢゅ cũng "Ju".
  JP: 「ぐぽっ！　ぢゅぼっ！　ちゅぶっ！　ちゅううっ！\nくっ！　りゅっ！　ちゅううっ！　（はみっ！！）」
  TW: 「啾！啾！啾！啾！啾！啾！啾！（咬）」
  Cũ: 「Gupo! Chubo! Chubu! Chuuuu!\nKu! Ryu! Chuuuu! （Ngoạm!!）」
  Mới: 「Gupo! Jubo! Chubu! Chuuuu!\nKu! Ryu! Chuuuu! （Ngoạm!!）」
- **1214 [凪]** — わっ → "Oa": cùng dòng わわわわわわわっ đã dịch "wawawawawawa" (giữ w), còn わっ đầu dòng lại mất w thành "Oa" — không nhất quán, sai âm. Sửa → "Wa".
  JP: 「え？　わっ――わわわわわわわっ！？」
  TW: 「啊？哇……哇哇哇哇哇？！」
  Cũ: 「Hả? Oa――wawawawawawa!?」
  Mới: 「Hả? Wa――wawawawawawa!?」
- **1169 [双鉄]** — ぁあっ là MỘT âm (aa + ngắt); bản cũ tách "a á!". Gộp → "Aa!".
  JP: 「ぁ――ぁっ――ぁあっ！」
  TW: 「啊……啊……啊！」
  Cũ: 「A――á――a á!」
  Mới: 「A――á――Aa!」

## D. Đếm nguyên âm theo công thức (12 dòng)

Công thức: số nguyên âm VN = 1 + số う/ぅ trong JP; với ぁ/あ/ー/～ đếm trực tiếp số mora. Đếm lại bằng script theo từng token (không đếm tay chuỗi dài).

- **1163 [双鉄]** — はあっ = 2 âm a mỗi hơi (tiền lệ nagih2: 7 hơi はぁっ/はぁ/はあっ → "Haa" ×7; hachiroku-h9: 10 dòng tương tự). Bản cũ "ha" thiếu 1 a mỗi hơi ×4.
  JP: 「くあっ――はあっ――はあっ――はあっ――はあっ」
  TW: 「啊……呼……呼……呼……呼」
  Cũ: 「Kua——ha——ha——ha——ha」
  Mới: 「Kua——haa——haa——haa——haa」
- **1130 [凪]** — きゃふうう + ぅ×7: tổng 10 âm u (ふ 1 + う 2 + ぅ 7). Bản cũ tách "Kya phuu…u" 17 u — thừa 7 u, lại tách làm 2 mảnh. Gộp một token, đúng 10 u.
  JP: 「きゃふううっっっっっっっっっっぅぅぅぅぅぅぅ！！」
  TW: 「呀！！」
  Cũ: 「Kya phuuuuuuuuuuuuuuuuu!!」
  Mới: 「Kyafuuuuuuuuuu!!」
- **1131 [凪]** — んひゅ + ぁ×11: cần 11 a. Bản cũ "Nhyuaaaaaa" chỉ 6 a — thiếu 5.
  JP: 「んひゅぁぁぁぁぁぁぁぁぁぁぁっっ！！！」
  TW: 「呀！！！」
  Cũ: 「Nhyuaaaaaa!!!」
  Mới: 「Nhyuaaaaaaaaaaa!!!」
- **1223 [凪]** — ずじゅ + ～×17: tổng 19 u (ず 1 + じゅ 1 + ～ 17). Bản cũ 20 u — thừa 1. Giữ Ư cuối dòng của audit (っ cuối sau ~~~), chỉ bớt 1 u.
  JP: 「ずじゅ～～～～～～～～～～～～～～～～～っ！！！」
  TW: 「啾～～～～～～～～～～～～～～～～～滋！！！」
  Cũ: 「Zujuuuuuuuuuuuuuuuuuuu!!!」
  Mới: 「ZujuuuuuuuuuuuuuuuuuuƯ!!!」
- **1217 [凪]** — ずりゅうううううっ: tổng 7 u (ず 1 + りゅ 1 + う 5). Bản cũ "Zuryuuuuu" chỉ 6 u — thiếu 1. Các token khác đúng (Juru 2u, Jubo 1u, Zuryu 2u, Juruu 3u, Jubu 2u).
  JP: 「じゅるっ！　ずりゅうううううっ！　じゅぼ！\nずりゅっ！　じゅぼっ！　じゅるうっ！　じゅぶっ！！」
  TW: 「啾！啾！啾！啾！啾！啾！啾！」
  Cũ: 「Juru! Zuryuuuuu! Jubo!\nZuryu! Jubo! Juruu! Jubu!!」
  Mới: 「Juru! Zuryuuuuuu! Jubo!\nZuryu! Jubo! Juruu! Jubu!!」
- **1221 [凪]** — じゅるううううっ: tổng 6 u (じゅ 1 + る 1 + う 4). Bản cũ "Juruuuuuu" 7 u — thừa 1. Token じゅうううううっ → "Juuuuuu" (6 u) đã đúng, giữ.
  JP: 「じゅうううううっ！　ずぼっ――ごっ！！！！\nじゅるううううっっっ！　ずびょっ！――ぎゅっ！！」
  TW: 「啾！滋……咕！啾！滋！啾！」
  Cũ: 「Juuuuuu! Zubo――go!!!!\nJuruuuuuu! Zubyo!――Gyu!!」
  Mới: 「Juuuuuu! Zubo――go!!!!\nJuruuuuu! Zubyo!――Gyu!!」
- **1222 [凪]** — れりゅううううっ: sau y cần 5 u (りゅ 1 + う 4). Bản cũ "Reryuuuu" chỉ 4 u — thiếu 1. Các token khác đúng (Zuryuu 2u sau y, Chubu, Zuchu, Juba).
  JP: 「っちゅっ！　ずっ！　れりゅううううっ！　じゅぶっ！\nずりゅうっ！　ちゅぶっ！　ずちゅっ！　じゅばっ！」
  TW: 「啾！滋！啾！啾！啾！啾！滋！啾！」
  Cũ: 「Chụt! Thút! Reryuuuu! Jubu!\nZuryuu! Chubu! Zuchu! Juba!」
  Mới: 「Chụt! Thút! Reryuuuuu! Jubu!\nZuryuu! Chubu! Zuchu! Juba!」
- **1213 [凪]** — じゅううううっ: tổng 5 u (じゅ 1 + う 4). Bản cũ "Juuuuuu" 6 u — thừa 1. Áp luôn Ư đầu dòng của audit ("!!!!" → "Ư!!!!"), chỉ đổi phần rên.
  JP: 「っ！！！！　（はぷっ！！！！）――れるっ！\nじゅううううっ！　ずちゅっ！　じゅぶっ！！！！」
  TW: 「啊！！！！（含！！！！）啾!啾！啾！啾！！！！」
  Cũ: 「!!!! （Hapu!!!!）――reru!\nJuuuuuu! Zuchu! Jubu!!!!」
  Mới: 「Ư!!!! （Hapu!!!!）――reru!\nJuuuuu! Zuchu! Jubu!!!!」
- **1220 [凪]** — れるうううっ: tổng 4 u (る 1 + う 3). Bản cũ "Reruuuuu" 5 u — thừa 1.
  JP: 「じゅるっ！　れるうううっ！　れろっ！　ちゅぱっ！\nんっ！　じゅぶっ！　じゅぼっ！　じゅっ！　じゅぶ！」
  TW: 「啾！啾！啾！啾！嗯！啾！啾！啾！啾！」
  Cũ: 「Juru! Reruuuuu! Rero! Chupa!\nƯm! Jubu! Jubo! Ju! Jubu!」
  Mới: 「Juru! Reruuuu! Rero! Chupa!\nƯm! Jubu! Jubo! Ju! Jubu!」
- **1298 [凪]** — ふーっ = 2 mora → "Phùu" (2 u). Bản cũ "Phù" thiếu 1 u mỗi hơi ×2. Giữ "aa" cho ああっ (っ cuối = ngắt nhấn, theo tiền lệ audit 1131).
  JP: 「修行に夢中になってにーさんの気配ばとれなかった\nうちが未熟――ああっ――（ふーっ、ふーっ）」
  TW: 「是我沉浸於練刀，沒注意到大哥哥……啊（呼——呼——）」
  Cũ: 「Do em mải mê tu hành nên không nhận ra sự hiện diện của anh hai\nLà do em còn non kém――aa――（Phù, phù）」
  Mới: 「Do em mải mê tu hành nên không nhận ra sự hiện diện của anh hai\nLà do em còn non kém――aa――（Phùu, phùu）」
- **1379 [凪]** — ふーーーっ = 4 mora → "Phùuuu" (4 u). Bản cũ "Phùuu" thiếu 1 u mỗi hơi ×4. Giữ "Aa" cho ああ.
  JP: 「（ふーーーっ、ふーーーっ、ふーーーっ、ふーーーっ）\nああ、赤いの少しも引かんばい――にーさん、痛かと？」
  TW: 「（呼——呼——呼——呼——）噢，紅色變淺了。大哥哥，還痛嗎？」
  Cũ: 「（Phùuu, phùuu, phùuu, phùuu）\nAa, vết đỏ không mờ đi chút nào cả――anh hai, có đau không?」
  Mới: 「（Phùuuu, phùuuu, phùuuu, phùuuu）\nAa, vết đỏ không mờ đi chút nào cả――anh hai, có đau không?」
- **1137 [凪]** — ふー = 2 mora → "Phùu"; ふーっ → "Phùu" (ngắt っ không bớt nguyên âm — tiền lệ 1135 くううっ → "kuuu"). Giữ "ực" cho ごくっ.
  JP: 「（ふー、ふーっ――ごくっ）。\n……にーさん、痛いんじゃなかったと？」
  TW: 「呼——呼——咕咚……大哥哥，你痛不痛？」
  Cũ: 「（Phù, phù――ực）.\n……Anh hai, không phải anh đang đau sao?」
  Mới: 「（Phùu, phùu――ực）.\n……Anh hai, không phải anh đang đau sao?」

## Các dòng rên đã kiểm tra kỹ và giữ nguyên (không sửa)

- **ひゃ/ひゅ/ひあ/きゃ đã romaji đúng**: 1132 ひゃうっ→"Hyau", 1128 ひゃうっ→"Hyau", 1134 んひゅっ→"Nhyu", 1270 んひゅっ→"nhyu" (giữa câu, thường), 1192 はひゅっ→"Hahyu", 1131 đã sửa đếm (xem §D).
- **ふあっ đã romaji đúng, giữ**: 1203/1204 "Fua", 1167/1173 "fua", 1248/1134 "Fua", 1128 "fua". ぷあっ→"Pua"/"pua" đúng (1202, 1249, 1236).
- **Hơi thở thường ふっ → "Phu"/"phu", giữ** (không thuộc họ fa/fu — tiền lệ nagih2: ふっ→"phù" cho hơi thở thường): 1155, 1227.
- **Cười là cười, không diễn thành rên**: 1186 うふふっ/えへへっ/ふふふふふふっ→"Ufufu——ehehe! Fufufufufu!", 1252 えへへっ→"Ehehe!", 1251 にへへっ→"Nihehe!", 1342 うふふ～ん→"Ufufu~n", 1270 えへへっ→"Ehehe!".
- **Rên ngắn あ/は/ん đã đúng**: 1194 あっ→"Á!?", 1168 ぁっ/あっ→"Á/á", 1177 ぁ/ぁっ→"A/á", 1172 は/あっ→"Hà/á", 1175 は/あ→"Ha/a", 1229 ん/は/あ→"Ưm/hà/a", 1231 ん/あっ/ぁ→"Ưm/á/a", 1206 はっ/あっ→"Ha/A", 1154 うっわ→"Uwa", 1146 うおっ→"Uo!?", 1142 うあっ→"Ua", 1249 あうっ→"Au".
- **SFX hút/liếm đã đúng**: 1216 ぴちゃっ→"Picha", ぺちょっ→"pecho"; 1218–1222 các chuỗi じゅ/ちゅ (Jumu/Jubu/Jubo/Juba/Ju/Churu/Chubo), 1219 ちゅううっ→"Chuuuu" (3 u), ぐぽっ→"Gupo", くっ→"Ku", りゅっ→"Ryu"; 1241 ずりゅううううううううううっ→"Zuryuuuuuuuuuuu" (đếm lại bằng script: 12 u, đúng công thức) và じゅぼお…→"Jubooooooooooooooooooo" (19 o, đúng) — đã kiểm chứng, không sửa.
- **Gasp Ư của audit, giữ nguyên**: toàn bộ 19 dòng audit (1208/1209/1211/1212/1215/1193/1124/1178/1135/1155/1126/1173/1183/1210/1213/1231/1223/1272/1515) — chỉ 1213/1223 gộp thêm sửa rên, không đụng Ư.
- **Kiai (không phải rên)**: 1224/1225 チェストー…っ → "Chesuto…" — tiếng hô kiếm thuật ở đoạn mở đầu (không phải H-scene); đếm theo công thức thì thiếu 1 o (16 thay vì 17; 10 thay vì 11) nhưng để nguyên vì ngoài phạm vi rên — ghi cờ dưới đây.
- **Lời nói ngọng (không phải rên)**: 1121 (audit đã sửa nghĩa), 1366 (audit đã flag chờ Hieu) — không đụng.
- **Khác**: 1337 つっっっ→"Đau――――――quá" (audit giữ + flag chờ Hieu); 1298 ああっ→"aa" (っ = ngắt nhấn, theo tiền lệ audit 1131); 1187 けぷっ→"kệpp" (ợ hơi, giữ); 1319/1318 "Kh-ông" là nói lắp, không phải っ; 1165/1190/1305 くっ→"hự" (tiếng gằn trong thoại, nhất quán) vs 1219/1221 くっ→"Ku!" (trong chuỗi SFX) — giữ cả hai theo ngữ cảnh.

## Cờ cho đợt thống nhất / chờ Hieu (không tự quyết)

- **F1 — Kiai 1224/1225 thiếu 1 o theo công thức**: チェストー×16 → "Chesuto" + 16 o (cần 17); チェストー×10 → 10 o (cần 11). Đây là tiếng hô kiếm thuật, không phải rên — để nguyên ở đây, đợt thống nhất quyết có sửa đếm hay không.
- **F2 — 1337** (audit đã flag): つっっっ diễn thành "quá" thay vì âm — chờ Hieu.
- **F3 — 1366** (audit đã flag): lời ngọng chưa giải mã chắc — chờ Hieu.
- **F4 — "Phu"/"phu" cho ふっ** (1155, 1227) giữ nguyên không dấu: nếu đợt thống nhất muốn chuẩn hoá hơi thở thường thành "phù" thì sửa ở đó (tiền lệ nagih2 1199: ふっ→"phù").

## Lượt soát 2

**34 tổng / 34 tái kiểm chứng / 0 loại bỏ / 0 sửa lại** — đọc lại toàn bộ 34 giá trị fix đối chiếu JP (kiểm tra từng token rên, đếm nguyên âm bằng script theo từng token, xác minh chữ hoa/thường theo vị trí). Không có dòng nào bị loại hay sửa lại ở lượt 2.

## Kiểm chứng cơ học

- JSON 34 mục, khóa string; jp/tw/old_vn khớp CSV3 34/34 (1 bộ duy nhất, 304 dòng).
- Khối TOML parse bằng tomllib: 34 khóa, 0 sai lệch giá trị.
- Mỗi fix chỉ khác VN cũ ở đúng token rên nhắm tới (kiểm bằng diff từng cặp old/fix).
- Không dòng nào trùng key với audit ngoài 1213/1223 (đã đối chiếu audit-lr-nagih1-itai-wrong.json — fix moan = giá trị audit + đổi token rên).

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
1129 = "「Fuya! Á! Á! Ưm――（Hapu!!）」"
1130 = "「Kyafuuuuuuuuuu!!」"
1131 = "「Nhyuaaaaaaaaaaa!!!」"
1137 = "「（Phùu, phùu――ực）.\\n……Anh hai, không phải anh đang đau sao?」"
1143 = "「Fua――á! Tuyệt, quá――ưm――\\nNgón tay, của anh hai――cảm giác――khác với, mọi khi――ưm」"
1145 = "「Fan!!!」"
1157 = "「Nhyun!!!?」"
1158 = "「Ưm ku! Fua――á――ưm――（Ngoạm!）\\nJuru――chubu! Juru! Juba!!」"
1161 = "「Nhyunn!!!!」"
1162 = "「Ưm ku!? Pu――fa――ưm――juru!\\nJubo! Jubu! Juba! Chuuuu」"
1163 = "「Kua——haa——haa——haa——haa」"
1169 = "「A――á――Aa!」"
1180 = "「Fua――á! Á! Á! Cách, sờ――\\nTay, của anh hai……so với lúc nãy, còn――dâm đãng hơn――」"
1185 = "「A……ưm……fa――á――anh hai……\\nMạnh hơn――mạnh hơn, nữa――ưm――mạnh lên, đi」"
1187 = "「Fa――anh hai, hơi bạo lực quá rồi――kệpp」"
1190 = "「A……Sắp, được rồi——ưm——hự——fua!\\nMột, chút nữa thôi——là vào đến, tận cùng——bên trong, rồi」"
1195 = "「Pua! Fue!? Anh ha――!!!?」"
1199 = "「Fua! A――anh hai, ưm――khỏe, ghê, nhỉ,\\nchỗ, bị va trúng――đã, hết đau――ưm――rồi, sao?」"
1201 = "「Fa! Á! Núm vú――núm vú, được vuốt ve nhẹ nhàng――\\nbằng ngón tay――sướng――quá――ưm!」"
1213 = "「Ư!!!! （Hapu!!!!）――reru!\\nJuuuuu! Zuchu! Jubu!!!!」"
1214 = "「Hả? Wa――wawawawawawa!?」"
1216 = "「Picha――pero――pero――pero――\\nreryu――pecho――pero――pero――」"
1217 = "「Juru! Zuryuuuuuu! Jubo!\\nZuryu! Jubo! Juruu! Jubu!!」"
1219 = "「Gupo! Jubo! Chubu! Chuuuu!\\nKu! Ryu! Chuuuu! （Ngoạm!!）」"
1220 = "「Juru! Reruuuu! Rero! Chupa!\\nƯm! Jubu! Jubo! Ju! Jubu!」"
1221 = "「Juuuuuu! Zubo――go!!!!\\nJuruuuuu! Zubyo!――Gyu!!」"
1222 = "「Chụt! Thút! Reryuuuuu! Jubu!\\nZuryuu! Chubu! Zuchu! Juba!」"
1223 = "「ZujuuuuuuuuuuuuuuuuuuƯ!!!」"
1233 = "「Ưm……hà――vú――từ từ――ưm――\\ntừ, xung quanh――bị, xoa nắn――fua!」"
1234 = "「Ưm――Fahaa」"
1236 = "「Ưm――pua! A……anh hai, ưm……bị, làm,\\nnhư vậy――fua――Nagi, sama――tập, trung」"
1242 = "「Kuhyun!!!」"
1298 = "「Do em mải mê tu hành nên không nhận ra sự hiện diện của anh hai\\nLà do em còn non kém――aa――（Phùu, phùu）」"
1379 = "「（Phùuuu, phùuuu, phùuuu, phùuuu）\\nAa, vết đỏ không mờ đi chút nào cả――anh hai, có đau không?」"
```

## Kết bài

File lr_凪h1_痛いの痛いの飛んでけばい đã đọc xong toàn bộ 304 dòng: **34 dòng rên đổi** (17 romaji + 5 mất/sai âm + 12 đếm nguyên âm), gồm 13 dòng họ fa/fu chuyển sang romaji (ふぁ→Fa, ふあ→Fua, ふぇ→Fue, ふや→Fuya — bản cũ "phua"/"Phuan" vừa Việt hoá vừa lẫn âm ふぁ/ふあ), 4 dòng một âm rên bị tách mảnh được gộp lại (Nhyun/Nhyunn/Kuhyun/Fahaa), 5 dòng mất/sai âm (1190 mất f, 1216 mất p ×5, 1219 mất hữu thanh, 1214 mất w, 1169 tách âm), và 12 dòng đếm nguyên âm theo công thức. Lượt soát 2: 34/34/0/0. Không đụng dòng gasp Ư nào của audit ngoài việc gộp ở 1213/1223, không dòng "Kh" nào bị đổi, không sửa đại từ/thuật ngữ/nghĩa. Còn chờ Hieu/đợt thống nhất: F1 kiai 1224/1225, F2 1337, F3 1366, F4 "Phu" cho ふっ.
