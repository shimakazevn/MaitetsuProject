# Moan-fix: ポーレットh8_気動車の国のアリス (Alice ở xứ sở toa xe tự hành) — 33 dòng rên sửa

## 1. Xác minh file

- File: `ポーレットh8_気動車の国のアリス.txt.toml` — route 03_Paulette, 649 dòng script, section `script` duy nhất.
- TOML: `sources/toml2/translation_toml/03_Paulette/#U30dd#U30fc#U30ec#U30c3#U30c8h8_#U6c17#U52d5#U8eca#U306e#U56fd#U306e#U30a2#U30ea#U30b9.txt.toml`, md5 `da94288489af95805aa9e8d2617d0a42` (khớp md5 audit đã ghi), không có bản trùng trong 227 file TOML.
- CSV3: 1 bộ duy nhất, 649 dòng, 0 key trùng; File `translation_toml\\03_Paulette\\ポーレットh8_気動車の国のアリス.txt.toml`. TOML vs CSV3: khớp toàn bộ (audit đã xác minh 0 khác biệt thực chất).
- Audit trước đó: 147 fix + 9 bổ sung Yunoi = 156 dòng sai (22,7%), lệch vị trí nặng với 6 chuỗi xoay vòng, 86 dòng. Các fix moan dưới đây được xét trên bản VN **sau audit** (fix audit + sửa moan gộp lại), còn `old_vn` trong JSON là VN hiện tại trong CSV3/TOML — theo đúng quy ước moan-fukamih1 key 1058.
- Cơ sở tổng moan trước file này (đã tự kiểm chứng lại trong `moans/ROUTE-MOANS.md`): **2 file / 38 dòng**.

## 2. Kiểm kê dòng rên

- Đã đọc 649/649 dòng (CSV3 + đối chiếu TOML). Tìm được **226 dòng ứng viên rên/thở/gasp/SFX** đã xét: 203 dòng theo mẫu chặt (âm rên/thở/gasp/SFX trong JP hoặc cách diễn rên trong VN) + 23 dòng gasp/SFX trong nhóm 42 dòng rà thêm ngoài mẫu (gasp っ trần, SFX trong ngoặc, えっ/おっと).
- Sửa **33 dòng**: 23 romaji + 9 cười (うふふ/うふ bị diễn thành rên) + 1 sai âm (2228). Giữ nguyên 193 dòng ứng viên.
- Nhóm lỗi chính:
  - **11 dòng thở La-tinh của audit**: 10 dòng sửa sang romaji (2132, 2134, 2137, 2139, 2142, 2187, 2241, 2286, 2365, 2304, 2413 — audit đã Việt hoá các dạng romaji cũ thành "Híu/Hiau/Kyaphù/Kíu/Hakíu/yôi-zo/iu/hiu"); 1 dòng giữ (2136 ひあっ → "Hia!?" đã là romaji đúng).
  - **Họ fa/fu (11 dòng)**: audit dùng quy ước file "phù a" cho ふあ/ふぁ/ぷぁ/ぷあ — tất cả 11 dòng đều chuyển sang romaji (Fua/Pua) vì "phù a" tách một âm duy nhất thành hai mảnh rời, đọc ngượng trong chuỗi rên.
  - **Cười bị diễn thành rên (9 dòng)**: うふふ/うふ → "Ư hự hự"/"Ư hự" — sai loại âm, vi phạm quy tắc Hieu 19/11 22:05 (cười là cười, không phải gasp).
  - **Sai âm (1 dòng)**: 2228 ぐ――ぅっ → "Ư——hự" (đảo ngược hai âm).
- Sweep gasp っ: 8 mục đã kiểm chứng trực tiếp trong `sweep-raw-gasp-wrong.json` — 7 bản sửa Ư (2147, 2148, 2183, 2252, 2253, 2254, 3150) audit đã nhận và **không đụng tới**; 1 already-rendered (2344) giữ nguyên. Không có dòng "Kh" nào bị đổi sang Ư.

## 3. Chi tiết dòng sửa (33 dòng)

### 3a. Romaji — thở La-tinh (11 dòng, audit đã Việt hoá)

**Key 2132 (ポーレット)**
- JP: `「ひゅあぁぁぁぁぁぁぁぁぁぁぁぁぁぁんっ！！！」`
- TW: `「呀啊啊啊啊啊！！！」`
- VN cũ: `「Hyuaaaaaaaaaaaaaaaan!!!」`
- Sửa: `「Hyuaaaaaaaaaaaaaaan!!!」`
- Lý do: JP ひゅあ + 14 ぁ = 15 âm a, rồi んっ. Bản cũ "Hyua…" thừa 1 a (16 a); audit sửa đúng số a (15) nhưng Việt hoá đầu âm thành "Híu". Khôi phục đầu romaji "Hyu" + 15 a + "n" theo công thức nguyên âm.

**Key 2134 (ポーレット)**
- JP: `「ひゃうんんっ！？　んっ――子宮、壁、これっ――\nは――ふあ――卵子、精液、びゅうびゅう、きて、る」`
- TW: `「呀嗯！？嗯——子宮的內壁上——這是——呼——呼啊——精液、打在卵子上了」`
- VN cũ: `「Hya un!? Ưm——tử cung, thành tử cung, cái này——\nhà——phù a——trứng, tinh dịch, đang, bắn vào」`
- Sửa: `「Hyaunn!? Ưm——tử cung, thành tử cung, cái này——\nhà——Fua——trứng, tinh dịch, đang, bắn vào」`
- Lý do: JP ひゃうんんっ là một âm duy nhất: ひゃう + んん + っ. Bản cũ tách thành "Hya un" (mất âm う, tách んん thành từ riêng). Romaji gộp "Hyaunn" (hyau + nn). Cùng dòng: ふあ → "Fua" thay "phù a".

**Key 2137 (ポーレット)**
- JP: `「ひゃうっ！？　あっ――ふっ――く、あっ――\nわたっ――わたし――イッた――イっ、ってっ！」`
- TW: `「呀！？啊——呼——啊——我——我——丟了——丟了！」`
- VN cũ: `「Hya!? A——phù——ư, a——\nem——em——lên đỉnh——lên đỉnh, rồi mà!」`
- Sửa: `「Hyau!? A——phù——ư, a——\nem——em——lên đỉnh——lên đỉnh, rồi mà!」`
- Lý do: JP ひゃうっ. Audit sửa "Hya" → "Hiau" (phiên âm Việt). Romaji đúng của ひゃう là "Hyau".

**Key 2139 (ポーレット)**
- JP: `「きゃふっ！？　はっ！　ああっ――早い、のっ――\nんっっ――ふあっ――もっと、これ、腰、ずれ、てっ」`
- TW: `「呀！？啊！啊——好快——嗯——呼啊——再來、這樣、腰會錯開」`
- VN cũ: `「Kya phu!? Hà! A a——nhanh, quá——\nưm——phù a——nữa đi, thế này, eo, lệch, mất」`
- Sửa: `「Kyafu!? Hà! A a——nhanh, quá——\nưm——Fua——nữa đi, thế này, eo, lệch, mất」`
- Lý do: JP きゃふっ → romaji "Kyafu" (audit "Kyaphù" là lai Việt–romaji). Cùng dòng ふあっ → "Fua" thay "phù a".

**Key 2142 (ポーレット)**
- JP: `「ひあ！？　あっ！　それ、らめっ！　イっちゃう、\nわた、しっ――すぐっ――ふ、きゅ――イっ、ちゃっ」`
- TW: `「呀！？啊！這樣不行！要丟了，我馬上要——呼——丟了」`
- VN cũ: `「Hia!? A! Thế này, không được! Lên đỉnh mất,\nem——ngay lập tức——phù, kyu——lên đỉnh, mất」`
- Sửa: `「Hia!? A! Thế này, không được! Lên đỉnh mất,\nem——ngay lập tức——phù, Kyu——lên đỉnh, mất」`
- Lý do: JP きゅ (trong ふ、きゅ). Audit "Kíu" là phiên âm Việt; romaji đúng là "Kyu". "phù" cho ふ giữ nguyên.

**Key 2185 (ポーレット)**
- JP: `「ふえっ！？」`
- TW: `「哎！？」`
- VN cũ: `——Nguy hiểm, quá.\nTôi lùi về phía giường để tạo khoảng cách, chật vật lắm mới kìm lại được.`
- Sửa: `「Fue!?」`
- Lý do: JP ふえっ là tiếng giật mình "fue". Audit "Phê!?" — trong tiếng Việt "phê" gợi nghĩa say thuốc, đọc lệch hẳn khỏi âm JP. Romaji "Fue!?" sạch và đúng âm.

**Key 2187 (ポーレット)**
- JP: `「えっ！？　やっ――いまのッ――んひゃうっ！？\nんんんんっ！？　なに、これっ――わたし、いまっ」`
- TW: `「哎！？呀——剛才——嗯！？嗯嗯嗯！？這是什麼——我剛才」`
- VN cũ: `「Hả!? Á——vừa rồi——ưm hyau!?\nƯm ưm ưm ưm!? Gì, thế này——em, vừa nãy」`
- Sửa: `「Hả!? Á——vừa rồi——ưm Hyau!?\nƯm ưm ưm ưm!? Gì, thế này——em, vừa nãy」`
- Lý do: JP んひゃうっ: ん giữ "ưm", ひゃう → romaji "Hyau" (audit "hiau" là phiên âm Việt).

**Key 2241 (ポーレット)**
- JP: `「はきゅっ！？　くっ――ふうううううっ」」`
- TW: `「啊呀！？啊——呼啊」`
- VN cũ: `「Hakyu!? Ư——phuuuuuu」`
- Sửa: `「Hakyu!? Hự——phuuuuuu」`
- Lý do: JP はきゅっ → romaji "Hakyu" (audit "Hakíu" là phiên âm Việt; bản cũ "Hakyu" đã đúng). Cùng dòng: くっ bản cũ diễn "Ư" — sai âm (く là tiếng gằn, không phải gasp); sửa thành "Hự" theo tiền lệ cùng file 2273/2275 (ん――くっ―― → "Ưm——hự——"). "phuuuuuu" (6 u = 1 + 5 う) giữ nguyên.

**Key 2286 (ポーレット)**
- JP: `「ん……あ――すごい……おちんちん、\nおっき、すぎて――これ――よいしょ――えいっ！」`
- TW: `「嗯……啊——好厲害……雞雞真大——這個——嘿咻！」`
- VN cũ: `「Ưm……a——Tuyệt quá……dương vật,\nto, quá——cái này——yoozo——ây da!」`
- Sửa: `「Ưm……a——Tuyệt quá……dương vật,\nto, quá——cái này——Yoisho——ây da!」`
- Lý do: JP よいしょ là tiếng rặn "heave-ho". Audit "yôi-zo" là lai Việt–romaji đọc rất ngượng; romaji "Yoisho" đúng âm JP (TW 嘿咻).

**Key 2365 (ポーレット)**
- JP: `「よいしょ――よいしょ――しこ――しこ――\nもにゅ、もにゅ――しこ――しこ――えいっ」`
- TW: `「嘿咻——嘿咻——套來——套去——揉來——揉去——套來——套去，嘿」`
- VN cũ: `「Yoozo——yoozo——sục——sục——\nnắn, nắn——sục——sục——ây da」`
- Sửa: `「Yoisho——Yoisho——sục——sục——\nnắn, nắn——sục——sục——ây da」`
- Lý do: JP よいしょ ×2. Audit "Yôi-zo" lai Việt–romaji, ngượng; romaji "Yoisho" ×2.

**Key 2304 (ポーレット)**
- JP: `「んゆっ！！？」`
- TW: `「嗯啊！！？」`
- VN cũ: `「Ưm yu!!?」`
- Sửa: `「Nyu!!?」`
- Lý do: JP んゆっ là một âm duy nhất: ん + ゆ. Bản cũ tách "Ưm yu", audit Việt hoá thành "Ưm iu". Romaji gộp "Nyu" theo tiền lệ nagih2 2395 (んきゅっ → "Nkyu").

**Key 2413 (ポーレット)**
- JP: `「きもち――いい――そこっ――だから、ねっ――\nんひゅっ！？　ふ――らめぇ――いま、今は、まだっ」`
- TW: `「好舒服——那裡——所以————嗯呀！？呼——不行——現在不行」`
- VN cũ: `「Sướng——quá——chỗ đó——nên là, nhé——\nưm hyu!? Phù——không được——bây, bây giờ, chưa được」`
- Sửa: `「Sướng——quá——chỗ đó——nên là, nhé——\nNhyu!? Phù——không được——bây, bây giờ, chưa được」`
- Lý do: JP んひゅっ là một âm duy nhất: ん + ひゅ. Bản cũ tách "ưm hyu", audit Việt hoá "ưm hiu". Romaji gộp "Nhyu" theo tiền lệ nagih2 (んひゅ → "Nhyu").

### 3b. Romaji — họ fa/fu (11 dòng)

**Key 2049 (ポーレット)**
- JP: `「やだっ！？　また、先、ひとり――でっ――ん、ふぁ、\nきもち、いいけどっ――いいけど――やぁ、なのっ！！」`
- TW: `「不要！我又要——一個人——嗯——雖然是、很舒服——但是我不要！！」`
- VN cũ: `「Không chịu đâu!? Lại, lên đỉnh, một mình——nữa——ưm, phù,\nsướng, lắm nhưng mà——nhưng mà——không chịu, đâu!!」`
- Sửa: `「Không chịu đâu!? Lại, lên đỉnh, một mình——nữa——ưm, Fua,\nsướng, lắm nhưng mà——nhưng mà——không chịu, đâu!!」`
- Lý do: JP ふぁ là hơi thở ngắn giữa hai tiếng rên. Bản cũ "phù" đọc như một từ Việt rời, ngượng trong chuỗi rên; romaji "Fua" giữ đúng âm JP (ふぁ = fua).

**Key 2163 (ポーレット)**
- JP: `「ふあっ――あっ――あっ――ああっ……\nふうっ――ふっ――ふっ――ふあああああ～」`
- TW: `「呼啊——啊——啊——啊……呼——啊——呼——呼啊～」`
- VN cũ: `「Phù a——a——a——a a……\nphù——phù——phù——phù a a a a a~」`
- Sửa: `「Fua——a——a——a a……\nphù——phù——phù——Fuaaaaa~」`
- Lý do: JP ふあっ và ふあああああ (5 âm a). Cả hai đều "phù a" trong bản cũ — tách một âm thành hai mảnh. Romaji "Fua" và "Fuaaaaa" (u + 5 a, theo công thức).

**Key 2165 (ポーレット)**
- JP: `「ふああ――うれしいっ――双鉄くんの――\nクリーム――精液っ」`
- TW: `「呼啊——我好開心——雙鐵君的——奶油——精液——」`
- VN cũ: `「Phù a——vui quá——kem——\ntinh dịch——của Anh Soutetsu」`
- Sửa: `「Fuaa——vui quá——kem——\ntinh dịch——của Anh Soutetsu」`
- Lý do: JP ふああ (ふ + 2 a). Bản cũ "Phù a" tách âm; romaji "Fuaa" (u + 2 a).

**Key 2167 (ポーレット)**
- JP: `「ふぁ……は――双鉄くん……（すんっ、すんっ）\nあ……双鉄、くん、で――わたし――いっぱい――」`
- TW: `「呼啊……啊——雙鐵君……（吸鼻子）啊……雙鐵君——弄得我全身都是」`
- VN cũ: `「Phù……hà——Anh Soutetsu……（sụt sịt, sụt sịt）\nA……bằng Anh Soutetsu——em——tràn ngập——」`
- Sửa: `「Fua……hà——Anh Soutetsu……（sụt sịt, sụt sịt）\nA……bằng Anh Soutetsu——em——tràn ngập——」`
- Lý do: JP ふぁ. Bản cũ "Phù" nghe như từ Việt; romaji "Fua" giữ đúng âm JP.

**Key 2207 (ポーレット)**
- JP: `「ふあっ――きた――あついのっ――精子っ――\nあかちゃんの、もとっ――双鉄、くんの、赤ちゃんの」`
- TW: `「啊——來了——熱熱的——精液——小寶寶的種子——雙鐵君的小寶寶」`
- VN cũ: `「Phù a——đến rồi——nóng quá——tinh trùng——\nmầm mống của, em bé——của Anh Soutetsu, của em bé」`
- Sửa: `「Fua——đến rồi——nóng quá——tinh trùng——\nmầm mống của, em bé——của Anh Soutetsu, của em bé」`
- Lý do: JP ふあっ. Bản cũ "Phù a" tách âm; romaji "Fua".

**Key 2212 (ポーレット)**
- JP: `「あ――は――んっ――ふううっ、ふぁ――は、あ。\nわたし――おまんこ――だき、ついて――ん、ふぁ」`
- TW: `「啊——呼——嗯——呼、啊——啊——我的——小穴——在抱著你——嗯、啊」`
- VN cũ: `「A——hà——ưm——phù, phù——hà, a.\nEm——âm đạo——đang ôm, chặt lấy——ưm, phù」`
- Sửa: `「A——hà——ưm——phù, Fua——hà, a.\nEm——âm đạo——đang ôm, chặt lấy——ưm, Fua」`
- Lý do: JP có hai tiếng ふぁ (giữa dòng và cuối dòng). Bản cũ diễn cả hai thành "phù" — mất âm a và nghe như hơi thở Việt. Romaji "Fua" cho cả hai; "phù" cho ふううっ giữ nguyên (quy ước file cho chuỗi ふう).

**Key 2214 (ポーレット)**
- JP: `「はぁっ――ふあ――あっ――んっ――ふあっ――\nだから、そういう、の――ん――ずるい、ですっ」`
- TW: `「啊——呼啊——啊——嗯——呼啊——所以——這樣——太狡猾了——」`
- VN cũ: `「Hà——phù a——a——ưm——phù a——\nthế nên, mấy trò, đó——ưm——ăn gian, lắm」`
- Sửa: `「Hà——Fua——a——ưm——Fua——\nthế nên, mấy trò, đó——ưm——ăn gian, lắm」`
- Lý do: JP có hai tiếng ふあ. Bản cũ "phù a" ×2 tách âm; romaji "Fua" ×2.

**Key 2279 (ポーレット)**
- JP: `「ん――んちゅ――ちゅぱ――ん、ぷぁ。\nえと……どう、しました？　双鉄くん」`
- TW: `「嗯——嗯啾——啾噗——嗯——噗。那個……怎麼了，雙鐵君」`
- VN cũ: `「Cho anh thêm miếng nữa đi——Lần này, hãy để anh ăn.」`
- Sửa: `「Ưm——ưm chụt——chụt——ưm, Pua. À ừm……sao, thế ạ? Anh Soutetsu.」`
- Lý do: JP ぷぁ. Audit "phù a" tách âm; romaji "Pua". (Fix này đã gồm bản sửa lệch vị trí của audit — xem ghi chú §5.)

**Key 2303 (ポーレット)**
- JP: `「んふうううううっ――ふあっ！？　あっ！　あっ、\nはげしっ――んっ――これっ――ふっ、あっ、あっ！」`
- TW: `「嗯啊——啊！？啊！啊！好激烈——嗯——這樣——呼、啊、啊！」`
- VN cũ: `「Ưm phuuuuuu——phù a!? A! A,\nmãnh liệt quá——ưm——thế này——phù, a, a!」`
- Sửa: `「Ưm phuuuuuu——Fua!? A! A,\nmãnh liệt quá——ưm——thế này——phù, a, a!」`
- Lý do: JP ふあっ → romaji "Fua" thay "phù a". "phuuuuuu" cho んふううううう (6 u = 1 + 5 う) giữ nguyên, đã đếm đúng.

**Key 2340 (ポーレット)**
- JP: `「ん？　……ぁ――ぷあっ――ね？　双鉄くん――ん。\nわたし、もっと――甘いの、ほしい――ちゅっ」`
- TW: `「嗯？……啊——呼——雙鐵君——嗯。我還想吃——更多甜甜的」`
- VN cũ: `Paulette chủ động tách môi tôi ra.`
- Sửa: `「Ưm? ……A——Pua——này? Anh Soutetsu——ưm.\nEm, muốn——nhiều đồ ngọt, hơn nữa——chụt」`
- Lý do: JP ぷあっ. Audit "phù" làm mất âm a (ぷあ = pua); romaji "Pua". (Fix này đã gồm bản sửa lệch vị trí của audit.)

**Key 2376 (双鉄)**
- JP: `「ぷあっ！？　（ずううううううううっっ！！）」`
- TW: `「噗啊！？（後退）」`
- VN cũ: `「Hể!?」`
- Sửa: `「Pua!? （Lùi lạiiiiiiiii!!）」`
- Lý do: JP ぷあっ → romaji "Pua" thay "Phù a" của audit. (Fix này đã gồm bản sửa lệch vị trí của audit.)

### 3c. Cười bị diễn thành rên (9 dòng)

**Key 2345 (ポーレット)**
- JP: `「うふふ……かえるさんのお店、大繁盛。\n『ぴちぱたぴちょん、ぴちぱちょん』」`
- TW: `「嘻嘻……青蛙先生的店生意紅火。“滴答滴答、滴答滴答”」`
- VN cũ: `「Ư hự hự……cửa hàng của bác ếch, buôn may bán đắt.\n『Lộp độp tí tách, lộp độp tí tách』」`
- Sửa: `「Ufufu……cửa hàng của bác ếch, buôn may bán đắt.\n『Lộp độp tí tách, lộp độp tí tách』」`
- Lý do: JP うふふ là tiếng cười khúc khích, không phải rên. Bản cũ "Ư hự hự" diễn thành tiếng rên — sai loại âm, vi phạm quy tắc Hieu 19/11 (cười là cười, không phải gasp). Sửa thành "Ufufu" theo tiền lệ Paulette trong chính file này (2356/2360/2370/2402 audit đã sửa đúng).

**Key 2349 (ポーレット)**
- JP: `「うふ、よかったぁ。『ああ』って真顔でいわれたら、\nどうしようかって思ってました」`
- TW: `「嘻嘻，太好啦。你要是一臉認真地同意了，我還不知道怎麼辦了」`
- VN cũ: `「Ư hự, may quá. Nếu anh mà tỉnh bơ đáp 『Ừ』,\nchắc em chẳng biết phải làm sao luôn.」`
- Sửa: `「Ufu, may quá. Nếu anh mà tỉnh bơ đáp 『Ừ』,\nchắc em chẳng biết phải làm sao luôn.」`
- Lý do: JP うふ là cười nhẹ. Bản cũ "Ư hự" diễn thành rên; sửa "Ufu".

**Key 2351 (ポーレット)**
- JP: `「うふふ――ね？　双鉄くんも、気持ち、いい？　\nちゃんと、びゅうびゅう、射精、できそう？」`
- TW: `「嘻嘻，對吧？你也舒服吧？感覺能射出來嗎？」`
- VN cũ: `「Ư hự hự——Thấy chưa? Anh Soutetsu cũng, sướng, đúng không?\nCó vẻ, sẽ bắn ra, xuất tinh, ngon lành nhỉ?」`
- Sửa: `「Ufufu——Thấy chưa? Anh Soutetsu cũng, sướng, đúng không?\nCó vẻ, sẽ bắn ra, xuất tinh, ngon lành nhỉ?」`
- Lý do: JP うふふ là cười. Bản cũ "Ư hự hự" diễn thành rên; sửa "Ufufu".

**Key 2353 (ポーレット)**
- JP: `「うふふ、うれしい。それじゃ、ゆーっくり。\nしこ――しこ――もみ――もみっ」`
- TW: `「嘻嘻，我好開心。那我就慢慢地，套來——套去——揉來——揉去」`
- VN cũ: `「Ư hự hự, em vui lắm. Vậy thì, từ từ thôi nhé.\nSục——sục——xoa——xoa」`
- Sửa: `「Ufufu, em vui lắm. Vậy thì, từ từ thôi nhé.\nSục——sục——xoa——xoa」`
- Lý do: JP うふふ là cười. Bản cũ "Ư hự hự" diễn thành rên; sửa "Ufufu".

**Key 2355 (ポーレット)**
- JP: `「うふふ、やっぱり、そうだったんですね」`
- TW: `「嘻嘻，果然是這樣」`
- VN cũ: `「Ư hự hự, quả nhiên, là vậy nhỉ.」`
- Sửa: `「Ufufu, quả nhiên, là vậy nhỉ.」`
- Lý do: JP うふふ là cười. Bản cũ "Ư hự hự" diễn thành rên; sửa "Ufufu".

**Key 2361 (ポーレット)**
- JP: `「うふふ、ほめすぎですよ。双鉄くん。\nでもうれしい。れいなに鍛えられたおかげかなぁ」`
- TW: `「嘻嘻，過獎啦，雙鐵君。不過我很開心，大概是跟玲奈練出來的吧」`
- VN cũ: `「Ư hự hự, anh khen quá lời rồi. Anh Soutetsu.\nNhưng em rất vui. Chắc là nhờ rèn luyện với Reina đấy.」`
- Sửa: `「Ufufu, anh khen quá lời rồi. Anh Soutetsu.\nNhưng em rất vui. Chắc là nhờ rèn luyện với Reina đấy.」`
- Lý do: JP うふふ là cười. Bản cũ "Ư hự hự" diễn thành rên; sửa "Ufufu".

**Key 2362 (ポーレット)**
- JP: `「うふふ、約束ですよ？\nわたし、ムース作っておきますね」`
- TW: `「嘻嘻，那就約好啦。我會做慕斯」`
- VN cũ: `「Ư hự hự, hứa rồi nhé?\nEm sẽ làm sẵn bánh mousse đợi anh.」`
- Sửa: `「Ufufu, hứa rồi nhé?\nEm sẽ làm sẵn bánh mousse đợi anh.」`
- Lý do: JP うふふ là cười. Bản cũ "Ư hự hự" diễn thành rên; sửa "Ufufu".

**Key 2364 (ポーレット)**
- JP: `「うふふ、双鉄くんのおちんちんさん。\nどうか、よろしくおねがいします」`
- TW: `「嘻嘻，雙鐵君的雞雞先生。請你多多指教啦」`
- VN cũ: `「Ư hự hự, dương vật của Anh Soutetsu.\nXin hãy giúp đỡ nhiều nhé.」`
- Sửa: `「Ufufu, dương vật của Anh Soutetsu.\nXin hãy giúp đỡ nhiều nhé.」`
- Lý do: JP うふふ là cười. Bản cũ "Ư hự hự" diễn thành rên; sửa "Ufufu".

**Key 2563 (ポーレット)**
- JP: `「ですね。うふふ、わたしも知りませんでした」`
- TW: `「是啊。嘻嘻，我之前也不知道來著」`
- VN cũ: `「Vâng. Ư hự hự, chính em cũng không biết điều đó.」`
- Sửa: `「Vâng. Ufufu, chính em cũng không biết điều đó.」`
- Lý do: JP うふふ là cười. Bản cũ "Ư hự hự" diễn thành rên; sửa "Ufufu".

### 3d. Sai âm (1 dòng)

**Key 2228 (双鉄)**
- JP: `「――ぐ――ぅっ――」`
- TW: `「啊——是——」`
- VN cũ: `「——Ư——hự——」`
- Sửa: `「——Guu——」`
- Lý do: JP ぐ――ぅっ: ぐ là tiếng gầm "gu", ぅ là nguyên âm dài, っ là ngắt. Bản cũ "Ư——hự" diễn sai cả hai âm (ぐ thành Ư, ぅっ thành hự — đảo ngược). Romaji "Guu" (gu + 1 ぅ = 2 u), dấu —— cuối giữ nhịp ngắt.

## 4. Dòng rên giữ nguyên (đáng chú ý)

- **Cười đã đúng (audit) — không đụng**: 2356 うふふっ → "Ufufu"; 2360 ふふっ → "Fufu"; 2370 んふふ、ははひはひはぁ → "Ừm fufu, haha hihi haa"; 2402 うふふ → "Ufufu". Đây là tiền lệ cho 9 dòng cười ở §3c.
- **Romaji đã đúng**: 2136 ひあっ → "Hia!?" (audit sửa "Hya" → "Hia" đúng âm); 2135 ひうっ → "Hiu!!?"; 2271/2272/2276 はうっ → "Hau"/"hau" (đã là dạng romaji, âm ngắn, giữ).
- **Gasp đã diễn đúng**: 2270 っ → "Hự"; 2273/2275 ん――くっ―― → "Ưm——hự——"; 2208 っ――ぐっ → "——Ư——hự!" (audit); 2277 ん――んんっ――んっ―― → "Ưm——ưm ưm——ưm——" (đủ 4 tiếng ん); 2307 んんんんっ → "Ưm ưm ưm ưm!" (audit thêm đủ 4); 2306 んんんっ → "Ưm ưm ưm" (đủ 3).
- **Chuỗi ふう → "phù" (quy ước file, không đụng)**: 2216, 2157, 2256, 2242 (ふぅ、ふううう～ → "phù, phù~"), 2210, 2785, 2224, 2267, 2413 (ふ―― → "Phù"). Audit giữ nhất quán dạng này trong toàn file; không áp công thức đếm nguyên âm cho chuỗi hơi thở ふう.
- **Chuỗi あ cách quãng (quy ước file)**: 2246/2247/2258 ああああ/あああ → "A a a a"/"A a a"; 2239, 2218, 2221, 2231 tương tự — giữ, không gộp thành "Aaaa" vì file dùng nhất quán dạng cách quãng.
- **SFX trong ngoặc (đã dịch thành động từ Việt, đúng)**: 3720/3722/3724/3730–3734/3736/3738/3741/3743/3748/3750–3752/3756/3761–3763/3767/3769–3772/3777 ("Sục/Thọc/Phập/Cộp/Siết chặt/…"). Riêng 3750/3738/3756 số chữ t kéo dài (6/8/10 t) không khớp hẳn số う trong JP (7/7/5) — đây là cách kéo dài cảm tính của bản dịch cũ cho SFX hành động, không phải lỗi âm rên; audit không sửa, giữ nguyên.
- **Cười Việt hoá tự nhiên**: 2368/2369/2372/2374 えへへ → "Ê hế hế" — giữ.
- **Lisp / nói ngọng**: 2496/2804 しゅき → "Thích quá" — giữ (không phải rên).
- **2308 んんんんんんんんんっっっ → "Ưm ưm ưm ưm ưm ưm ưm ưm ưm!!"**: đủ 9 tiếng ん; ba っ cuối là nhấn cắt, đã được "!!" diễn đạt — giữ.

## 5. Ghi chú cho đợt thống nhất (14 fix thay thế fix audit)

14 fix dưới đây **đã gộp bản sửa của audit** (lệch vị trí / Việt hoá La-tinh) — đợt thống nhất phải áp dụng **giá trị moan** này thay cho giá trị audit cho cùng key, không áp cả hai: 2132, 2137, 2139, 2142, 2185, 2187, 2241, 2279, 2286, 2304, 2340, 2365, 2376, 2413.

- 2132: giữ bản sửa số lượng của audit (16 → 15 âm a), chỉ đổi đầu âm "Híu" → "Hyu" (romaji).
- 2241: khôi phục "Hakyu" của bản cũ (audit đổi thành "Hakíu"); đồng thời sửa くっ "Ư" → "Hự" theo tiền lệ 2273/2275 cùng file.
- 2279, 2340, 2376, 2185: fix moan đã gồm bản sửa lệch vị trí của audit (VN cũ của 4 dòng này là bản dịch của dòng khác) — giá trị moan là giá trị cuối cùng cho dòng đó.
- Sau file này, **không còn dòng ふぁ/ふあ/ぷぁ/ぷあ nào diễn "phù a"/"phù" trong file** (đã kiểm chứng bằng quét toàn file: 13/13 dòng họ fa/fu nay đều là Fua/Pua).

## 6. Cờ (không quyết được ở đây)

**Key 2155 (双鉄)** — JP: `「はぁ――はぁ――はぁ――はぁっ」`, TW: `「呼——呼——呼——呼——」`, VN: `「Hà——hà——hà——hà」`. Tiếng はぁ thứ tư có っ cuối dòng nhưng không có dấu câu sau — âm ngắt có thể đã mất (không được diễn bằng Ư hay dấu nào). Sweep không liệt kê dòng này, audit (đã tìm ra 2 dòng sweep bỏ sót) cũng không sửa — hai vòng đều bỏ qua nên không rõ là cố ý hay sót. Đây là câu hỏi gasp-sweep, không phải diễn rên ngượng — **không sửa ở đây**, nhờ vòng audit / đợt thống nhất quyết: thêm Ư cuối dòng hay giữ nguyên.

**Key 2179 (双鉄)** — JP: `「おっと」`, TW: `「哎」`, VN: `「Ốp」`. `おっと` là tiếng giật mình/thốt lên ("oops/whoa"); "Ốp" đọc như tiếng đập, nghĩa lệch và nghe lạ — nhưng hướng sửa chưa rõ: "Ôi"/"Ối" (Việt hoá) hay "Otto" (romaji). Đây là câu hỏi nghĩa của thán từ, không phải rên — **không sửa ở đây**, nhờ vòng audit quyết.

## 7. Lượt soát 2 + khối TOML

- Lượt soát 2 (đọc lại toàn bộ 33 bản sửa đối chiếu JP + TW): **tổng 33 / tái kiểm chứng 33 / bỏ 0 / sửa 0**. Đã đếm lại từng độ dài nguyên âm bằng script: 2132 = 15 a (JP ひゅあ + 14 ぁ), 2163 = 5 a, 2165 = 2 a, 2241/2303 = 6 u (1 + 5 う), 2228 = 2 u (1 + 1 ぅ).
- JSON: `moan-paulette-h8-alice-rail-car-wrong.json` — 33 mục, khóa dạng string, jp/tw/old_vn khớp CSV3 tuyệt đối 33/33, không có fix nào trùng old_vn, mọi fix chỉ khác old_vn ở đúng phần rên cần sửa (đã kiểm tra diff từng dòng; 4 dòng 2185/2279/2340/2376 khác thêm phần lệch vị trí của audit — đã ghi rõ ở §5). Không fix nào chạm dòng gasp Ư của sweep; không dòng "Kh" nào bị đổi.
- Khối TOML dưới đây parse bằng tomllib: **33 khóa, 0 sai lệch giá trị** so với JSON. (Literal `\n` trong fix được viết `\\n` trong khối.)

```toml
[script]
"2049" = "「Không chịu đâu!? Lại, lên đỉnh, một mình——nữa——ưm, Fua,\\nsướng, lắm nhưng mà——nhưng mà——không chịu, đâu!!」"
"2132" = "「Hyuaaaaaaaaaaaaaaan!!!」"
"2134" = "「Hyaunn!? Ưm——tử cung, thành tử cung, cái này——\\nhà——Fua——trứng, tinh dịch, đang, bắn vào」"
"2137" = "「Hyau!? A——phù——ư, a——\\nem——em——lên đỉnh——lên đỉnh, rồi mà!」"
"2139" = "「Kyafu!? Hà! A a——nhanh, quá——\\nưm——Fua——nữa đi, thế này, eo, lệch, mất」"
"2142" = "「Hia!? A! Thế này, không được! Lên đỉnh mất,\\nem——ngay lập tức——phù, Kyu——lên đỉnh, mất」"
"2163" = "「Fua——a——a——a a……\\nphù——phù——phù——Fuaaaaa~」"
"2165" = "「Fuaa——vui quá——kem——\\ntinh dịch——của Anh Soutetsu」"
"2167" = "「Fua……hà——Anh Soutetsu……（sụt sịt, sụt sịt）\\nA……bằng Anh Soutetsu——em——tràn ngập——」"
"2185" = "「Fue!?」"
"2187" = "「Hả!? Á——vừa rồi——ưm Hyau!?\\nƯm ưm ưm ưm!? Gì, thế này——em, vừa nãy」"
"2207" = "「Fua——đến rồi——nóng quá——tinh trùng——\\nmầm mống của, em bé——của Anh Soutetsu, của em bé」"
"2212" = "「A——hà——ưm——phù, Fua——hà, a.\\nEm——âm đạo——đang ôm, chặt lấy——ưm, Fua」"
"2214" = "「Hà——Fua——a——ưm——Fua——\\nthế nên, mấy trò, đó——ưm——ăn gian, lắm」"
"2228" = "「——Guu——」"
"2241" = "「Hakyu!? Hự——phuuuuuu」"
"2279" = "「Ưm——ưm chụt——chụt——ưm, Pua. À ừm……sao, thế ạ? Anh Soutetsu.」"
"2286" = "「Ưm……a——Tuyệt quá……dương vật,\\nto, quá——cái này——Yoisho——ây da!」"
"2303" = "「Ưm phuuuuuu——Fua!? A! A,\\nmãnh liệt quá——ưm——thế này——phù, a, a!」"
"2304" = "「Nyu!!?」"
"2340" = "「Ưm? ……A——Pua——này? Anh Soutetsu——ưm.\\nEm, muốn——nhiều đồ ngọt, hơn nữa——chụt」"
"2345" = "「Ufufu……cửa hàng của bác ếch, buôn may bán đắt.\\n『Lộp độp tí tách, lộp độp tí tách』」"
"2349" = "「Ufu, may quá. Nếu anh mà tỉnh bơ đáp 『Ừ』,\\nchắc em chẳng biết phải làm sao luôn.」"
"2351" = "「Ufufu——Thấy chưa? Anh Soutetsu cũng, sướng, đúng không?\\nCó vẻ, sẽ bắn ra, xuất tinh, ngon lành nhỉ?」"
"2353" = "「Ufufu, em vui lắm. Vậy thì, từ từ thôi nhé.\\nSục——sục——xoa——xoa」"
"2355" = "「Ufufu, quả nhiên, là vậy nhỉ.」"
"2361" = "「Ufufu, anh khen quá lời rồi. Anh Soutetsu.\\nNhưng em rất vui. Chắc là nhờ rèn luyện với Reina đấy.」"
"2362" = "「Ufufu, hứa rồi nhé?\\nEm sẽ làm sẵn bánh mousse đợi anh.」"
"2364" = "「Ufufu, dương vật của Anh Soutetsu.\\nXin hãy giúp đỡ nhiều nhé.」"
"2365" = "「Yoisho——Yoisho——sục——sục——\\nnắn, nắn——sục——sục——ây da」"
"2376" = "「Pua!? （Lùi lạiiiiiiiii!!）」"
"2413" = "「Sướng——quá——chỗ đó——nên là, nhé——\\nNhyu!? Phù——không được——bây, bây giờ, chưa được」"
"2563" = "「Vâng. Ufufu, chính em cũng không biết điều đó.」"
```

**Tổng cộng sau file này: 3 file / 71 dòng sai (moan)** (cơ sở 2 file / 38 dòng + 33 file này)

## Kết bài

File ポーレットh8_気動車の国のアリス: đọc 649/649 dòng, xét 226 dòng rên/SFX, sửa 33 dòng (23 romaji + 9 cười + 1 sai âm), giữ 193 dòng, 8 dòng sweep không đụng, flag 2 dòng (2155, 2179). Lỗi rên tập trung ở ba kiểu hệ thống: audit đã Việt hoá các dạng romaji cũ thành "Híu/Hiau/Kyaphù/Kíu/Hakíu/yôi-zo/iu/hiu" (10/11 dòng thở La-tinh); quy ước file "phù a" cho họ fa/fu tách một âm thành hai mảnh (11 dòng); và 9 tiếng cười うふふ/うふ bị diễn thành tiếng rên "Ư hự hự". Sau file này tổng moan là 3 file / 71 dòng.
