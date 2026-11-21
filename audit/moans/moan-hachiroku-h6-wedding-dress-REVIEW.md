# Moan-fix: ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml (moan-hachiroku-h6-wedding-dress)

- File: `01_Hachiroku/ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml` — route 01_Hachiroku, 461 dòng script (monologue 266, ハチロク 118, 双鉄 77). Cảnh H — Soutetsu và Hachiroku (Suzu) trong trang phục váy cưới, đêm tân hôn.
- TOML md5 `9c51863393588f1bb888afa1bdbec48a` (khớp md5 audit), 1 bản duy nhất toàn dự án (không có file trùng md5). UTF-8 BOM + CRLF (941 dòng). `[info]` rỗng, `[selections]` rỗng, không thẻ %l, không [ruby].
- CSV3: 1 bộ duy nhất (`translation_toml\01_Hachiroku\ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml`), 461 dòng, 0 khóa trùng, 0 VN trống. TOML `[script]` 461 khóa khớp CSV3 461/461; giá trị VN khớp phẳng 459/461 (sau chuẩn hoá `\n` literal ↔ khoảng trắng — TOML-2 làm phẳng `\n`; 2 lệch còn lại 1758/1442 chỉ là escape `\"` của TOML, không phải lệch nội dung).
- Audit trước đó: 16 sai (3,5%) — đã gộp vào ROUTE-AUDIT.md. File này KHÔNG có dòng "Kh" nào. Không key nào trong 58 fix moan này trùng key audit (đã kiểm chứng: giao nhau = 0).

## 1. Kiểm chứng file

- Đã đọc 461/461 dòng (CSV3 + TOML-2).
- Sweep gasp: 14 mục cho file này (kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`): 11 fix Ư lost-gasp đã áp nguyên qua audit (519, 775, 873, 1008, 1080, 1081, 1082, 1083, 1085, 1557, 1771 — cả 11 đều nằm trong 16 fix audit) + 3 mục "already-rendered" (837, 938, 946). Không dòng gasp Ư nào bị đụng trong đợt moan này (946 chỉ sửa đếm nguyên âm ư, không đụng gasp — xem §3e); không dòng "Kh" nào bị đổi (file không có "Kh").
- Đếm nguyên âm của audit đã kiểm chứng lại độc lập bằng máy ở các chuỗi dài (819, 844, 929, 946 — xem §3e); 2 lỗi đếm của audit đã bỏ sót được sửa ở đây (819 thiếu 2u + 2n; 929 thiếu 3u + 1n).

## 2. Kiểm kê rên/SFX

- Đã xét 254 dòng rên/SFX: 131 thoại (ハチロク 88, 双鉄 43) + 123 độc thoại (chủ yếu SFX trong ngoặc （ ）).
- Đổi 58 dòng: 46 romaji + 12 đếm nguyên âm.
- Giữ 196 dòng rên/SFX (xem §4).
- Nhóm lỗi chính:
  - Họ fa/fu chưa tách bị Việt hoá "phù a"/"phù" — 14 dòng (829, 830, 831, 832, 852, 863, 881, 884, 915, 930, 941, 948, 950, 1020): audit đã cờ ~40 dòng "Phu a" chờ thống nhất; đợt moan đưa các token đơn về romaji theo quy tắc fallback 21/11. Dạng tách (ふ、ぁ / ふ……ぁ / ふっ――あっ — 2 token riêng trong JP) giữ nguyên "phù, a"/"phù……a"/"phù——a" theo tiền lệ h7 485/971.
  - Họ ひゃ/ひゅ/ひあ/きゃ/ひう mất phụ âm/glide — 13 dòng (812, 821, 842, 843, 845, 847, 849, 854, 924, 925, 926, 937, 940): "Á"/"Hí a"/"Ưm hứ"/"Ưm hiun" → Hya/Kya/Hia/Hiu/Hyua/Hyau/Nhyu/Nhyun/Kahyu theo quy tắc 3b.
  - Họ く/くあ/んくっ mất phụ âm k — 12 dòng (513, 514, 872, 874, 882, 887, 897, 904, 909, 935, 939, 1052): "Hự"/"Ưm"/"ư" → Ku/Kuu/Kua/Ưm ku theo tiền lệ paulette-h5 + h2 1020/1070 + lr-hiyoko 2349 (xem cờ F1).
  - や/あん/んぁ/ぃあ/ふきゅ/ちゅう/じゅう — 7 dòng (530, 816, 869, 871, 824, 838, 934).
  - Đếm nguyên âm — 12 dòng (819, 844, 929, 946, 839, 932, 856, 865, 866, 875, 1335, 1963).

## 3. Chi tiết từng bản sửa (58 dòng)

Quy ước áp dụng: mỗi fix là MỘT giá trị duy nhất cho key đó. Không key nào trùng audit, nên mọi fix đều build từ old VN (CSV3). Dạng tách fa (2 token riêng trong JP) giữ nguyên; chỉ token đơn mới về romaji.

### 3a. Họ fa/fu chưa tách → romaji (14 dòng)

**829** — ハチロク
- JP: 「ぷぁ……あ――ふぅ……ふっ――んっ――れるっ」
- TW: 「呼啊……啊——嗚……呼——咻嚕」
- VN cũ: 「Phù a……a——phù……phù——ưm——mút」
- VN mới: 「Pua……a——phù……phù——ưm——mút」
- Lý do: ぷぁ (một token) → "Pua" (romaji; "Phù a" tách mảnh, ngượng). Giữ "phù" cho ふぅ/ふっ.

**830** — ハチロク
- JP: 「ふあっ！」
- TW: 「呼啊！」
- VN cũ: 「Phù a!」
- VN mới: 「Fua!」
- Lý do: ふあっ → "Fua" (tiền lệ h7 692).

**831** — ハチロク
- JP: 「ふあっ！　あっ！　あっ！　あっ！！！」
- TW: 「呼啊！啊！啊！啊！！！」
- VN cũ: 「Phù a! A! A! A!!!」
- VN mới: 「Fua! A! A! A!!!」
- Lý do: ふあっ → "Fua".

**832** — ハチロク
- JP: 「ふあっ！！！」
- TW: 「呼啊！！！」
- VN cũ: 「Phù a!!!」
- VN mới: 「Fua!!!」
- Lý do: ふあっ → "Fua".

**852** — ハチロク
- JP: 「はっ――あっ――まだ――ふとっ――んっ――\nんっ――ふあっ――んくっ！！！」
- TW: 「哈——啊——還——嗚嗯——嗯——呼啊——嗯！！！」
- VN cũ: 「Hà——a——vẫn còn——to——ưm——\nưm——phù a——ưm hự!!!」
- VN mới: 「Hà——a——vẫn còn——to——ưm——\nưm——Fua——ưm ku!!!」
- Lý do: ふあっ → "Fua"; んくっ → "ưm ku" (く bị mất hẳn trong "ưm hự" — xem §3c). Giữ "to" cho ふとっ (tiền lệ paulette-h2 942 giữ "to").

**863** — ハチロク
- JP: 「あ……ぁっ……ふあっ……双鉄――さまっ」
- TW: 「啊……啊……呼啊……雙鐵少爺——」
- VN cũ: 「A……a……phù a……ngài Soutetsu——」
- VN mới: 「A……a……Fua……ngài Soutetsu——」
- Lý do: ふあっ → "Fua".

**881** — ハチロク
- JP: 「ふぁっ――あっ――あっ――あっ――あっ――\nはっ――はぁっ――はぁっ――はあっ――はあっ――」
- TW: 「嗚啊——啊——啊——啊——啊——哈——啊——啊——啊——啊——」
- VN cũ: 「Phù a——a——a——a——a——\nnhà——hà——hà——hà——hà——」
- VN mới: 「Fa——a——a——a——a——\nhà——hà——hà——hà——hà——」
- Lý do: ふぁっ → "Fa"; はっ đầu dòng 2 "nhà" → "hà" — lỗi đánh máy: はっ là hơi thở "ha", "nhà" là từ Việt "nhà cửa", không có căn cứ JP (cùng lỗi ở 948).

**884** — ハチロク
- JP: 「ん――ふっ――ふうっ――ふ――っ――れろっ――\nれるっ――ちゅくっ――ふぁ」
- TW: 「嗯——呼——呼——呼——嗯——咻嚕——啾嗯——嗚啊」
- VN cũ: 「Ưm——phù——phù——phù——ư——liếm——\nmút——chụt——phù a.」
- VN mới: 「Ưm——phù——phù——phù——ư——liếm——\nmút——chụt——Fa.」
- Lý do: ふぁ cuối dòng → "Fa". Giữ "phù" cho ふっ/ふうっ/ふ――っ.

**915** — ハチロク
- JP: 「ん……ごくっ――ぷぁ――ふぁ――あっ……\n双鉄、さま……そうてつさま……そうてつさまぁ」
- TW: 「嗯……嗯——噗啊——嗚啊——啊……雙鐵少爺……雙鐵少爺……雙鐵少爺」
- VN cũ: 「Ưm……ực——phù a——phù——a……\nNgài Soutetsu……Ngài Soutetsu……Ngài Soutetsu.」
- VN mới: 「Ưm……ực——Pua——Fa——a……\nNgài Soutetsu……Ngài Soutetsu……Ngài Soutetsu.」
- Lý do: ぷぁ → "Pua", ふぁ → "Fa" (bản cũ "phù a——phù" còn làm mất âm a của ふぁ). Giữ "ực" cho ごくっ.

**930** — ハチロク
- JP: 「んきゅっ！！？　あっ……ふぁ……あっ！」
- TW: 「嗯嗚！！？啊……嗚啊……啊！」
- VN cũ: 「Ưm kiuu!!? A……phù……a!」
- VN mới: 「Ưm kiu!!? A……Fa……a!」
- Lý do: ふぁ → "Fa"; んきゅっ "kiuu" → "kiu" (đếm, xem §3e).

**941** — ハチロク
- JP: 「んっ！　ふっ！　ふっ！　んっ！　ふっ！　ふあっ！\nんっ！　んくっ！　んっ！！！」
- TW: 「嗯！呼！呼！嗯！呼！呼啊！嗯！嗯嗯！嗯！！！」
- VN cũ: 「Ưm! Phù! Phù! Ưm! Phù! Phù a!\nƯm! Ưm hự! Ưm!!!」
- VN mới: 「Ưm! Phù! Phù! Ưm! Phù! Fua!\nƯm! Ưm ku! Ưm!!!」
- Lý do: ふあっ → "Fua"; んくっ → "Ưm ku" (xem §3c).

**948** — ハチロク
- JP: 「ぷあっ！　はっ――あっ――ん……ふあっ――\nはぁっ――はぁっ――はあっ――ふあああ～っ――！」
- TW: 「噗啊！哈——啊——……呼啊——啊——啊——啊——呼、啊嗯～——！」
- VN cũ: 「Phù a! Hà——a——ưm……phù a——\nnhà——hà——hà——phù a a a~——!」
- VN mới: 「Pua! Hà——a——ưm……Fua——\nhà——hà——hà——Fuaaa~——!」
- Lý do: ぷあっ → "Pua"; ふあっ → "Fua"; ふあああ～っ → "Fuaaa~" (ふ + あ×3 = 3 a); はぁっ "nhà" → "hà" (lỗi đánh máy như 881).

**950** — ハチロク
- JP: 「うれし……ふぁ――うれし――です――そうてつ、さま、\nわたくし――わたくし、だけ――の、だんな、さまぁっ」
- TW: 「好高興……嗚啊——高興——雙鐵少爺，我——我——一個人的夫君」
- VN cũ: 「Hạnh phúc……phù——hạnh phúc, quá——ngài Soutetsu,\nphu, quân——của riêng——một mình, em.」
- VN mới: 「Hạnh phúc……Fa——hạnh phúc, quá——ngài Soutetsu,\nphu, quân——của riêng——một mình, em.」
- Lý do: ふぁ → "Fa".

**1020** — ハチロク
- JP: 「おまんまん、で、す。双鉄……様。ふぁ――わたくしの、\nこんなに小さな――割れ目のような、おまんまん……が」
- TW: 「是小妹妹，雙鐵少爺……嗚啊——我的，這麼小——像裂口一樣的，小妹妹……」
- VN cũ: 「Là cô bé, ạ. Ngài Soutetsu…… Phù——cô bé của em,\nnhỏ xíu——như một khe hở thế này……đang.」
- VN mới: 「Là cô bé, ạ. Ngài Soutetsu…… Fa——cô bé của em,\nnhỏ xíu——như một khe hở thế này……đang.」
- Lý do: ふぁ → "Fa".

### 3b. Họ ひゃ/ひゅ/ひあ/きゃ → romaji (13 dòng)

**812** — ハチロク
- JP: 「ひゃっ――あっ――んっ――ぁっ――おまん、まん、\n子宮――おちん、ちん――に、なで、なでされ、て」
- TW: 「呀——啊——啊——小妹妹，子宮——被雞雞——撫摸來撫摸去」
- VN cũ: 「Á——a——ưm——a——cô, bé,\ntử cung——bị, dương, vật——vuốt, vuốt ve.」
- VN mới: 「Hya——a——ưm——a——cô, bé,\ntử cung——bị, dương, vật——vuốt, vuốt ve.」
- Lý do: ひゃっ → "Hya" ("Á" mất phụ âm hy, quy tắc 3b).

**821** — ハチロク
- JP: 「きゃっ！？」
- TW: 「呀！？」
- VN cũ: 「Á!?」
- VN mới: 「Kya!?」
- Lý do: きゃっ → "Kya" ("Á" mất phụ âm ky, quy tắc 3b; tiền lệ paulette-h2 944).

**842** — ハチロク
- JP: 「ひあっ――あっ――あっ――ああああっ！！！！」
- TW: 「咿啊——啊——啊——啊啊啊！！！！」
- VN cũ: 「Hí a——a——a——a a a a!!!!」
- VN mới: 「Hia——a——a——a a a a!!!!」
- Lý do: ひあっ → "Hia" ("Hí a" tách mảnh → romaji; tiền lệ lr-hiyoko ひあっ "Hi ah"→"Hia"). Giữ "a a a a" cho ああああっ (đủ 4 a, dạng tách đã có trong file).

**843** — ハチロク
- JP: 「ひあっ――あっ！　ふっ――んっ――くっ――んぁ！」
- TW: 「咿啊——啊！呼——嗯——嗯——啊！」
- VN cũ: 「Hí a——a! Phù——ưm——hự——ưm a!」
- VN mới: 「Hia——a! Phù——ưm——Ku——Na!」
- Lý do: ひあっ → "Hia"; くっ → "Ku" (xem §3c); んぁ → "Na" (một âm "na", bản cũ "ưm a" tách mảnh).

**845** — ハチロク
- JP: 「ひうっっ！！！」
- TW: 「咿！！！」
- VN cũ: 「Hí ư!!!」
- VN mới: 「Hiu!!!」
- Lý do: ひうっっ → "Hiu" ("Hí ư" tách mảnh; っ×2 diễn bằng !!!; tiền lệ ひう→"Hiu").

**847** — ハチロク
- JP: 「はっ――むちゅっ――んっ――ちゅう――ふ、ぁ――\nん、れるっ――ひゅぁっ――えろっ――ん、く――あ！」
- TW: 「哈——咕啾——啾——呼，啊——嗯，咻嚕——呀啊——啊嗚——啊！」
- VN cũ: 「Hà——chụm——ưm——chụt——phù, a——\nưm, mút——hí a——liếm——ưm, ư——a!」
- VN mới: 「Hà——chụm——ưm——chụt——phù, a——\nưm, mút——Hyua——liếm——ưm, Ku——a!」
- Lý do: ひゅぁっ → "Hyua" (tiền lệ ひゅあ→"Hyua"); ん、く → "ưm, Ku" (く→"ư" mất k). Giữ "phù, a" cho ふ、ぁ (2 token riêng).

**849** — ハチロク
- JP: 「はっ――ひっ――あっ――ほーへふっ――はま――\nんっ――しゅき――しゅきっ――ひゃうっ！」
- TW: 「哈——哈——啊——雙——鐵——嗯——喜歡——喜歡——呀嗚！」
- VN cũ: 「Hà——hí——a——S-Soutetsu——ngài——\nưm——thích——thích lắm——hi au!」
- VN mới: 「Hà——hí——a——S-Soutetsu——ngài——\nưm——thích——thích lắm——Hyau!」
- Lý do: ひゃうっ → "Hyau" ("hi au" tách mảnh; tiền lệ lr-nagih1 ひゃうっ→"Hyau"). Giữ "S-Soutetsu" cho ほーへふっ (nói ngọng) và "thích" cho しゅき (diễn nghĩa).

**854** — ハチロク
- JP: 「はっ……ひゃ、あ――んっ――いり、ぐち――の、\nとこっ……ゆ、っくり――じわ、って――ふ、は」
- TW: 「哈……呀，啊——入口——的部位……慢慢地——進來了——呼」
- VN cũ: 「Hà……hí, a——ưm——chỗ, cửa——\nvào……chầm, chậm——từ từ——phù, hà.」
- VN mới: 「Hà……Hya, a——ưm——chỗ, cửa——\nvào……chầm, chậm——từ từ——phù, hà.」
- Lý do: ひゃ、あ → "Hya, a" (giữ dấu phẩy tách theo JP — ひゃ và あ là 2 token riêng). Giữ "phù, hà" cho ふ、は.

**924** — ハチロク
- JP: 「んひゅっ――んっ――んゅっ――んん～――\nふっ――んふっ――ふっ――ふぅ～っ――」
- TW: 「嗯咻——嗯——嗯嗯～——呼——呼——呼——嗚～——」
- VN cũ: 「Ưm hứ——ưm——ưm——ưm ưm~——\nphù——ưm phù——phù——phù~——」
- VN mới: 「Nhyu——ưm——Nyu——ưm ưm~——\nphù——ưm phù——phù——phù~——」
- Lý do: んひゅっ → "Nhyu" (quy tắc 3b); んゅっ → "Nyu" ("ưm" mất hẳn âm yu; tiền lệ んゅっ→"Nyu", h8 2304 んゆっ→"Nyu"). Giữ "ưm ưm~" cho んん～ và "phù~" cho ふぅ～っ (~ đã diễn độ dài).

**925** — ハチロク
- JP: 「んひゅんっ！！」
- TW: 「嗯咻！！」
- VN cũ: 「Ưm hiun!!」
- VN mới: 「Nhyun!!」
- Lý do: んひゅんっ → "Nhyun" (quy tắc 3b: んひゅん→"Nhyun").

**926** — ハチロク
- JP: 「んひゅっ！！！」
- TW: 「嗯咻！！！」
- VN cũ: 「Ưm hứ!!!」
- VN mới: 「Nhyu!!!」
- Lý do: んひゅっ → "Nhyu".

**937** — ハチロク
- JP: 「んくっ！？　かひゅっ――あっ？　そう、てつ、さまっ\n――わた、くし――おく――もう、一番――お、くぅっ」
- TW: 「嗯嗯！？咻——啊？雙鐵少爺——我——裡面——最裡面的——地方」
- VN cũ: 「Ưm hự!? Hí——a? Ngài, Soutetsu\n——của, em——bên trong——đã đến, nơi——sâu, nhất rồi.」
- VN mới: 「Ưm ku!? Kahyu——a? Ngài, Soutetsu\n——của, em——bên trong——đã đến, nơi——sâu, nhất rồi.」
- Lý do: かひゅっ → "Kahyu" ("Hí" mất ka và glide y); んくっ → "Ưm ku" (xem §3c).

**940** — ハチロク
- JP: 「んっ！　ふっ――んひゅ！　んんっ！！！！」
- TW: 「嗯！呼——咻！嗯嗯！！！！」
- VN cũ: 「Ưm! Phù——ưm hứ! Ưm ưm!!!!」
- VN mới: 「Ưm! Phù——Nhyu! Ưm ưm!!!!」
- Lý do: んひゅ → "Nhyu".

### 3c. Họ く/くあ/んくっ → romaji (12 dòng)

Quy tắc áp dụng: くっ/んくっ trong chuỗi rên → "Ku"/"Ưm ku" (tiền lệ paulette-h5: くっ→"Ku" ở dòng rên; h2 1020/1070; lr-hiyoko 2349). Xem cờ F1 về ranh giới rên-vs-grunt.

**513** — 双鉄
- JP: 「っ――くうっ！」
- TW: 「——唔！」
- VN cũ: 「Ư——hự!」
- VN mới: 「Ư——Kuu!」
- Lý do: くうっ = 2 u → "Kuu" ("hự" mất k và mất độ dài; rên lên đỉnh của Soutetsu, giữ "Ư——" cho っ―― đầu dòng).

**514** — 双鉄
- JP: 「――――あっ――はっっ――――んっ――くっ」
- TW: 「——啊——不哈——嗯」
- VN cũ: 「————A——hà————ưm——hự」
- VN mới: 「————A——hà————ưm——Ku」
- Lý do: くっ cuối chuỗi rên → "Ku".

**872** — 双鉄
- JP: 「くあっ！」
- TW: 「啊！」
- VN cũ: 「Hự!」
- VN mới: 「Kua!」
- Lý do: くあっ → "Kua" ("Hự" mất k và nguyên âm a; tiền lệ くあっ→"Kua").

**874** — 双鉄
- JP: 「くあっ！！！！」
- TW: 「啊！！！！」
- VN cũ: 「Hự!!!!」
- VN mới: 「Kua!!!!」
- Lý do: くあっ → "Kua".

**882** — 双鉄
- JP: 「くっ――」
- TW: 「嗯——」
- VN cũ: 「Ưm——」
- VN mới: 「Ku——」
- Lý do: くっ → "Ku" ("Ưm" là âm của ん, sai hẳn; JP thắng TW). Rên/gằn đơn của Soutetsu — xem cờ F1.

**887** — ハチロク
- JP: 「んっ――ふっ――れるっ――るっ――んっ――\nちゅっ――んくっ――ふっ――ふううっ！」
- TW: 「嗯——呼——咻嚕——嚕——啾——嗯——呼——呼！」
- VN cũ: 「Ưm——phù——mút——mút——ưm——\nchụt——ưm——phù——phù ư ư!」
- VN mới: 「Ưm——phù——mút——mút——ưm——\nchụt——ưm ku——phù——phù ư ư!」
- Lý do: んくっ → "ưm ku" (bản cũ "ưm" làm mất hẳn く). Giữ "phù ư ư" cho ふううっ (đủ 3 u, xem §4).

**897** — 双鉄
- JP: 「ん――くっ！」
- TW: 「嗯——嗯！」
- VN cũ: 「Ưm——hự!」
- VN mới: 「Ưm——Ku!」
- Lý do: くっ → "Ku" (xem cờ F1).

**904** — ハチロク
- JP: 「ん……ふ……く……ぁ――双鉄……さま、の――\nおちん、ちん――硬くて、ぬれ、てる……ちんちん、が」
- TW: 「嗯……呼……啊——雙鐵少爺……——雞、雞——硬，又濕，的……小雞雞」
- VN cũ: 「Ưm……phù……ư……a——dương, vật……của——ngài Soutetsu……\ncứng quá, ướt, nhẹp……dương vật, của ngài.」
- VN mới: 「Ưm……phù……Ku……a——dương, vật……của——ngài Soutetsu……\ncứng quá, ướt, nhẹp……dương vật, của ngài.」
- Lý do: く → "Ku" ("ư" mất phụ âm k; tiền lệ h7 485 く……→"Ku……").

**909** — ハチロク
- JP: 「ん……あ――ふ……こん、なに――ゆっくり、だ、と。\nく、ふ――双鉄、さまの――おちん、ち――んきゅ！？」
- TW: 「嗯……啊——呼……這麼——慢慢地……呼——雙鐵少爺的——雞雞——嗯呀！？」
- VN cũ: 「Ưm……a——phù……chậm, chạp——thế này, thì.\nƯ, phù——dương, vật——của ngài Soutetsu——ưm kiuu!?」
- VN mới: 「Ưm……a——phù……chậm, chạp——thế này, thì.\nKu, phù——dương, vật——của ngài Soutetsu——ưm kiu!?」
- Lý do: く → "Ku"; んきゅ "kiuu" → "kiu" (đếm, xem §3e).

**935** — 双鉄
- JP: 「んくっ！！！！」
- TW: 「嗯嗯！！！！」
- VN cũ: 「Ưm hự!!!!」
- VN mới: 「Ưm ku!!!!」
- Lý do: んくっ → "Ưm ku" (rên lên đỉnh của Soutetsu).

**939** — 双鉄
- JP: 「くっ！」
- TW: 「嗯！」
- VN cũ: 「Ưm!」
- VN mới: 「Ku!」
- Lý do: くっ → "Ku" ("Ưm!" sai hẳn — Ưm là âm của ん).

**1052** — 双鉄
- JP: 「すずっ――く――ぁ」
- TW: 「鈴——啊」
- VN cũ: 「Suzu——ư——a」
- VN mới: 「Suzu——Ku——a」
- Lý do: く → "Ku" ("ư" mất k).

### 3d. や / あん / んぁ / ぃあ / ふきゅ / ちゅう / じゅう → romaji (7 dòng)

**530** — ハチロク
- JP: 「や……ぁ……双鉄……さぁ……ん……その、ような\n――こと――は――おっしゃられ――てはっ――んっ」
- TW: 「……啊……雙鐵少爺……嗯……那個，那種事——不要說——出來啊——嗯」
- VN cũ: 「A……a……ngài Soutetsu……ưm……những, lời\n——như thế——xin ngài đừng——nói ra——ưm.」
- VN mới: 「Ya……a……ngài Soutetsu……ưm……những, lời\n——như thế——xin ngài đừng——nói ra——ưm.」
- Lý do: や → "Ya" ("A" mất phụ âm y; tiền lệ lr-hiyoko や→"Ya").

**816** — ハチロク
- JP: 「や……そのようなお声……ふ、ぁ……わたくし……\nちく、び……んっ――恥ずかしい……です」
- TW: 「呀……這種聲音……呼，啊……我的……乳頭……嗯——好害羞……」
- VN cũ: 「Á……giọng nói đó của ngài……phù, a……em……\nnúm, vú……ưm——xấu hổ quá……ạ.」
- VN mới: 「Ya……giọng nói đó của ngài……phù, a……em……\nnúm, vú……ưm——xấu hổ quá……ạ.」
- Lý do: や → "Ya" ("Á" mất y). Giữ "phù, a" cho ふ、ぁ (2 token riêng).

**869** — ハチロク
- JP: 「ぃあああ～～ん！　か――ふッ―あっ――んっ！！」
- TW: 「啊啊啊～～嗯！啊——呼——啊——嗯！！」
- VN cũ: 「Á a a a~~! Hà——phù——a——ưm!!」
- VN mới: 「Iaaaan~~! Hà——phù——a——ưm!!」
- Lý do: ぃあああ～～ん = ぃ(i) + あ×3 + ん → "Iaaaan" (bản cũ "Á a a a" sai nguyên âm đầu — ぃ là i, không phải a — và tách mảnh; tiền lệ ぃあっ→"Ia"). Giữ "phù——a" cho ふッ―あっ (2 token riêng).

**871** — ハチロク
- JP: 「あんっ！！！」
- TW: 「啊嗯！！！」
- VN cũ: 「A ưm!!!」
- VN mới: 「An!!!」
- Lý do: あんっ là một âm duy nhất → "An" ("A ưm" tách mảnh; tiền lệ h2 974 giữ "an" cho あんっ).

**824** — ハチロク
- JP: 「ふっ――ふきゅっ――んっ！　ふっ――んっ――\nふうっ――ふっ――んっ――んんっ！！」
- TW: 「呼——呼嗯！呼——呼——呼——嗯——嗯！！」
- VN cũ: 「Phù——phù kiu——ưm! Phù——ưm——\nphù——phù——ưm——ưm ưm!!」
- VN mới: 「Phù——Fukyu——ưm! Phù——ưm——\nphù——phù——ưm——ưm ưm!!」
- Lý do: ふきゅっ → "Fukyu" ("phù kiu" tách một âm thành hai mảnh; tiền lệ h7 750 ふきゅん→"Fukyun").

**838** — ハチロク
- JP: 「れるっ――ちゅううっ――んっ――ふっ――んっ――\nふっ――っん！　ふうっ！　んっ　んんっ！！！」
- TW: 「咻嚕——啾嗚——嗯——呼——呼——嗯！呼！嗯嗯嗯！！！」
- VN cũ: 「Mút——chùn chụt——ưm——phù——ưm——\nphù——ưm! Phù! Ưm ưm ưm!!!」
- VN mới: 「Mút——Chuuu——ưm——phù——ưm——\nphù——ưm! Phù! Ưm ưm ưm!!!」
- Lý do: ちゅううっ = ちゅ + う×2 = 3 u → "Chuuu" ("chùn chụt" là cách diễn bịa — "chùn" không có căn cứ JP; âm hôn dài phải diễn đủ độ dài). Giữ "ưm" cho っん và "Ưm ưm ưm" cho んんっ.

**934** — ハチロク
- JP: 「んんんん～～～っ！！　んっ、ふっ――ん！　ふうっ、\nん、れるっ――れろっ――じゅうう――ずじゅじゅ～！」
- TW: 「嗯嗯嗯嗯～～～！！嗯，呼——！呼，嗯，咻嚕——嗯——吱吱嗯——呲啾呲啾～！」
- VN cũ: 「Ưm ưm ưm ưm~~~!! Ưm, phù——ưm! Phù,\nưm, mút——liếm——chùn chụt——rột rột~!」
- VN mới: 「Ưm ưm ưm ưm~~~!! Ưm, phù——ưm! Phù,\nưm, mút——liếm——Juuu——rột rột~!」
- Lý do: じゅうう = じゅ + う×2 = 3 u → "Juuu" (cùng lỗi "chùn chụt" như 838). Giữ "rột rột~" cho ずじゅじゅ～ (tiếng hút Việt, đúng).

### 3e. Đếm nguyên âm (12 dòng)

Quy tắc đếm (đã chốt): đếm theo từng mora — mỗi mora đóng góp đúng nguyên âm của nó (ふ=1u, きゅ=1u, mỗi う/ぅ=1u, ん=0, mỗi あ/ぁ=1a). Cách viết tắt "1 + số う/ぅ" chỉ đúng khi mora gốc có nguyên âm u; với mora gốc là ん thì không cộng 1 (tiền lệ paulette-h2 938: んうううっ = 3u → "Nuuu").

**819** — ハチロク
- JP: 「きゅふううううううううんんっ！！？」
- TW: 「呀嗚——！！？」
- VN cũ: 「Kiufuuuuuuu!!?」
- VN mới: 「Kiufuuuuuuuuunn!!?」
- Lý do: きゅふううううううううんんっ = きゅ(1u) + ふ(1u) + う×8 + ん×2 = 10 u + 2 n (đếm lại bằng máy); bản cũ 8 u / 0 n → 10 u / 2 n ("Kiu" + f + 9u + "nn").

**929** — ハチロク
- JP: 「きゅふうううううううんっ！！！！」
- TW: 「嗯嗚——！！！！」
- VN cũ: 「Kiufuuuuu!!!!」
- VN mới: 「Kiufuuuuuuuun!!!!」
- Lý do: きゅふうううううううんっ = 9 u + 1 n (đếm lại bằng máy); bản cũ 6 u / 0 n → 9 u / 1 n.

**844** — ハチロク
- JP: 「ひきゅううううううううううううんんんんんっ！！！」
- TW: 「咿嗚——嗯——！！！」
- VN cũ: 「Hí kiuuuuuuuuuuưm ưm ưm!!!」
- VN mới: 「Hí kiuuuuuuuuuuuuuưm ưm ưm ưm ưm!!!」
- Lý do: ひきゅううううううううううううんんんんんっ = きゅ(1u) + う×12 + ん×5 = 13 u + 5 ん (đếm lại bằng máy); bản cũ "kiu" 10 u + "ưm"×3 → 13 u + "ưm"×5 (giữ dạng "ưm" lặp của file, chỉ sửa số lượng).

**946** — ハチロク
- JP: 「んっ！！？　んっ！！！\nんうううううううううううううううううう～っ！！！！」
- TW: 「嗯！！？嗯！！！\n嗯嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚～！！！！」
- VN cũ: 「Ưm!!? Ưm!!!\nƯm ư ư ư ư ư ư ư ư ư ư ư ư ư ư ư ư ư~!!!!」
- VN mới: 「Ưm!!? Ưm!!!\nƯm ư ư ư ư ư ư ư ư ư ư ư ư ư ư ư ư ư ư~!!!!」
- Lý do: んうううううううううううううううううう～っ = ん(0) + う×18 = 18 u (đếm lại bằng máy); bản cũ 17 ư (1 Ưm + 16 ư) → 18 ư (1 Ưm + 17 ư). Lưu ý kiểm chứng: lần đếm đầu bằng script đã đếm thiếu 1 do không đếm 'Ư' trong "Ưm" (chỉ đếm 'ư' thường) — đã đếm lại trực tiếp ký tự và sửa đúng (tiền lệ 凪h2 key 2500: parent đã sửa lỗi đếm thiếu 1 tương tự).

**839** — ハチロク
- JP: 「ひ、ぐっ――あっ――そこっ――そこっ！　ぞりゅって、\nゆっくり――んっ――こす――られ――ひ――んきゅ！」
- TW: 「咿、咕——啊——那裡——那裡！呲溜呲溜的，慢慢地——摩擦——咿——嗯呀！」
- VN cũ: 「Hí, ưm——a——chỗ đó——chỗ đó! Bị cọ xát,\nchầm chậm——ưm——vào——đó——hí——ưm kiuu!」
- VN mới: 「Hí, ưm——a——chỗ đó——chỗ đó! Bị cọ xát,\nchầm chậm——ưm——vào——đó——hí——ưm kiu!」
- Lý do: んきゅ → 1 u ("kiu"; bản cũ "kiuu" thừa 1 u). Giữ nguyên "Hí, ưm" cho ひ、ぐっ — xem cờ F2 (chưa quyết "Hi, gu" vs "Hức, hức").

**932** — ハチロク
- JP: 「んきゅっ！？　ん！！？」
- TW: 「嗯嗚！？嗯！！？」
- VN cũ: 「Ưm kiuu!? Ưm!!?」
- VN mới: 「Ưm kiu!? Ưm!!?」
- Lý do: んきゅっ → 1 u ("kiu"; bản cũ "kiuu" thừa 1 u).

**856** — 双鉄
- JP: 「おお――」
- TW: 「哦——」
- VN cũ: 「Ồ——」
- VN mới: 「Ôô——」
- Lý do: おお = 2 mora o → 2 nguyên âm "Ôô" (bản cũ 1 o; tiền lệ 1432: ぁあ 2 a → "aa").

**865** — 双鉄
- JP: 「ああ……うむ」
- TW: 「啊……嗯」
- VN cũ: 「À……ừm.」
- VN mới: 「Aa……ừm.」
- Lý do: ああ = 2 a → "Aa" (hơi thở "ah" kéo dài, không phải thán từ đồng ý — khác với 868/870/916/1018 ああ→"Ừ" diễn nghĩa, giữ nguyên).

**866** — ハチロク
- JP: 「ああ……ニップレスのことでございますか」
- TW: 「啊……說的是透氣乳貼嗎」
- VN cũ: 「À……ngài đang nói đến miếng dán ngực sao ạ.」
- VN mới: 「Aa……ngài đang nói đến miếng dán ngực sao ạ.」
- Lý do: ああ = 2 a → "Aa" (hơi thở nhận ra, kéo dài bằng ……).

**875** — 双鉄
- JP: 「ああ、なるほどな」
- TW: 「啊，原來如此」
- VN cũ: 「À, ra là vậy.」
- VN mới: 「Aa, ra là vậy.」
- Lý do: ああ = 2 a → "Aa" (diễn âm, không diễn nghĩa — khác với 1018 ああ→"Ừ").

**1335** — monologue
- JP: 「極大にまで膨れ上がった僕の勃起に貫かれ――ああ。」
- TW: 「入口被我膨脹到極限的肉棒給捅開了——啊。」
- VN cũ: 「Bị cậu bé cương cứng đến cực đại của tôi đâm xuyên qua——a.」
- VN mới: 「Bị cậu bé cương cứng đến cực đại của tôi đâm xuyên qua——aa.」
- Lý do: ああ cuối câu độc thoại = 2 a → "aa".

**1963** — 双鉄
- JP: 「（ああ――そうなのか）」
- TW: 「（啊啊——原來如此）」
- VN cũ: 「（A——ra là vậy sao.）」
- VN mới: 「（Aa——ra là vậy sao.）」
- Lý do: ああ = 2 a → "Aa" (suy nghĩ trong ngoặc, hơi thở nhận ra).

## 4. Ghi chú các dòng rên giữ nguyên (196 dòng)

- Dạng tách fa — ふ、ぁ / ふ……ぁ / ふっ――あっ là 2 token riêng trong JP nên giữ "phù, a"/"phù……a"/"phù——a": 532 (ふ、ぁ), 906 (ふ……ぁ), 816 (ふ、ぁ — chỉ sửa や), 1045 (ん、ふ、あ), 1050 (ふ――ぁ, audit), 847 (ふ、ぁ — chỉ sửa ひゅぁ/く), 909 (く、ふ — chỉ sửa く/んきゅ), 1036 (ふっ――あ――), 913 (ふぅ……はぁ, không phải fa), 922 (は、ぁ). Tiền lệ h7 485/971 giữ dạng tách.
- SFX trong ngoặc （） ở độc thoại — giữ nguyên dạng động từ/từ láy Việt (Nắn/Bóp/Xoa/Phụt/Phập/Trượt/Lắc/Thít/Siết...) ~55 dòng (1925, 1929, 1930, 1931, 1935, 1936, 1940, 1941, 1944–1950, 1953, 1956, 1958–1962, 1964, 1966–1970, 1972, 1974–1984, 1986, 1988–1991, 1993–2002, 2005–2007, 2010, 2011, 2014–2029, 2031, 2036, 2038, 2040–2042, 2045, 2049). Kể cả （くっ）→（Ưm）/(hự) trong ngoặc (1959, 1979, 1980, 1981, 1982, 1931, 1960, 1936) — ranh giới F3, xem §5.
- Gasp Ư — không đụng: 509 (っ――→"Ư——"), 512 (――っ――→"——Ư——"), 515/516 (audit: "Ư——A"), 827 (っ→"Ư"), 1080–1083/873/519/775/1008/1557/1771/1085 (audit), 837/938/946 (sweep "already-rendered"; 946 chỉ sửa đếm ư).
- Cười: 823 うふふっ → "Ufufu." giữ (tiếng cười là tiếng cười).
- Giá trị audit giữ nguyên: 511 (いっ→"ư" trong câu nói ngọng khi đang mút — lựa chọn của audit, không đụng), 1050 (ふ――ぁ→"phù——a" dạng tách), 515/516 ("Ư——A").
- 814 ひ……あ…… → "Hí……a……" giữ (JP tách ひ và あ bằng …… — 2 hơi riêng, VN giữ đúng dạng tách).
- 842 "a a a a" cho ああああっ giữ (đủ 4 a, dạng tách đã có trong file — chỉ sửa ひあっ→"Hia").
- 859 やっ――と → "Cuối——cùng!" giữ (やっと = cuối cùng, từ có nghĩa, không phải rên); 850 いっ→"ra" giữ (いく rút gọn, diễn nghĩa); 857 ぬっ→"Hử!?" giữ (thán từ ngạc nhiên); 868/870/916/1018 ああ→"Ừ" giữ (đồng ý, diễn nghĩa, không phải hơi thở).
- 899/915 ごくっ/こくっ → "ực" giữ (tiếng nuốt, đúng); 899/922/891 んむっ → "ưm"/"Ưm" giữ (mẫu file: んむ→"ưm").
- 885/887 ふううっ → "phù ư ư" giữ (đủ 3 u, đúng công thức, dạng tách đã có trong file); 924 ふぅ～っ → "phù~" giữ (~ đã diễn độ dài); 938 んん～ → "Ưm ưm" giữ; 944 んっ → "Ưm" giữ.
- 928 んきゅんっ → "Ưm kiun" giữ (1 u + n, đúng); 820 きゅふっ → "Kiufu" giữ; 911/892 きゅっ → "kiu" giữ; 913 ふぅ → "phù" giữ.
- 931 ずぢゅるるるるるるるる～～っ → "chùn chụt chùn chụt~~" giữ (tiếng hút/slurp dài, dạng lặp đôi diễn độ dài — khác với ちゅうう/じゅうう ở 838/934 là âm hôn dài bị diễn sai thành "chùn chụt"); んぶっ → "Ưm bự" giữ ("bự" là âm "bu" nặng, không phải từ "to lớn").
- 852 ふとっ → "to" giữ (tiền lệ paulette-h2 942 giữ "to" cho ふとっ).
- SFX diễn nghĩa trong ngoặc: 1952 （ふわっ）→（Nhẹ nhàng）, 1951 （つ、くっ――）→（Chạm, vào——）, 2049 （ぺろっ）→（Bật tung）, 2014 （つんっ）→（Chọc）, 1923 （ちらっ）→（Liếc）, 1075 （すうっ）→(Hít sâu) — giữ (diễn nghĩa, không phải rên).

## 5. Cờ cho đợt thống nhất / parent

- **F1 — くっ "Ku" vs "Hự" (grunt):** đã áp "Ku"/"Ưm ku" cho くっ/んくっ trong chuỗi rên theo tiền lệ paulette-h5 + h2 1020/1070 + lr-hiyoko 2349; nhưng câu hỏi mở toàn dự án (h2 F2) vẫn còn — "Hự" là tiếng gằn Việt tự nhiên cho grunt của Soutetsu, đặc biệt các dòng gằn đơn 513 (くうっ), 882 (くっ――), 897 (ん――くっ！), 935 (んくっ!!!!). Chờ parent/đợt thống nhất quyết ranh giới rên-vs-grunt.
- **F2 — 839 ひ、ぐっ → "Hí, ưm" giữ nguyên:** ぐっ→"ưm" mất phụ âm g (cùng câu hỏi F5 của ROUTE-MOANS.md: ひっ、ぐっ → "Hi, gu" vs "Hức, hức"). Chỉ sửa đếm んきゅ trong dòng này; ぐっ chờ quyết.
- **F3 — SFX trong ngoặc （） ở độc thoại:** giữ dạng động từ Việt (xem §4). Ranh giới romaji-vs-động-từ cho SFX ngoặc vẫn là câu hỏi mở. Đặc biệt （くっ）→（Ưm）/(hự) trong ngoặc (1979, 1980, 1981, 1982, 1959) giữ theo mẫu này, dù くっ trong thoại đã về "Ku".
- **F4 — 2034 (くくっ） → （Kéo）:** không phải rên — くくっ là tiếng cười khẽ nén / tiếng sột soạt (TW 窸窣 = sột soạt), VN "Kéo" (kéo/drag) không khớp. Đây là lỗi nghĩa, thuộc audit — cờ lại, không sửa ở đợt moan này.
- **F5 — 1163 ひょっ:** ghi chú trong ROUTE-AUDIT.md ("1163 ひょっ→'hự' vs 'hây'") không thuộc file này — key 1163 không tồn tại trong CSV3/TOML của ハチロクh6 (file này không có dòng ひょ nào). Ghi chú đó thuộc file khác, parent kiểm chứng lại.
- **F6 — 931 ずぢゅるるるるるるるる～～っ "chùn chụt chùn chụt~~" giữ** (xem §4) — ranh giới với 838/934 đã sửa; nếu đợt thống nhất quyết "chùn" là sai thì sửa cả 3 dòng cùng lúc.

## 6. Lượt soát 2

- Tổng 58 / tái kiểm chứng 58 / bỏ 0 / sửa 0.
- Kiểm chứng cơ học: JSON 58 mục, khóa string; jp/tw/old_vn khớp CSV3 58/58; khối TOML parse bằng tomllib: 58 khóa, 0 sai lệch giá trị; không key nào trùng audit (giao nhau = 0); mỗi fix chỉ khác old VN ở đúng token rên đã nêu (đã diff từng dòng).
- Đếm nguyên âm chuỗi dài đã đếm lại độc lập bằng máy (819: 10u/2n; 929: 9u/1n; 844: 13u/5 ưm; 946: 18u); 24 token romaji đã kiểm chứng lại từng âm tiết với JP (Hya/Kya/Hia/Hiu/Hyua/Hyau/Nhyu/Nhyun/Kahyu/Kua/An/Iaaa/Ya/Fukyu/Chuuu/Juuu/Na).
- Lưu ý kiểm chứng: lần đếm đầu của script cho 946 đã đếm thiếu 1 do không đếm 'Ư' trong "Ưm" (chỉ đếm 'ư' thường) — đã phát hiện trong lượt soát 2, đếm lại trực tiếp ký tự và xác nhận fix đúng 18 ư (không cần sửa fix).

## Khối TOML

```toml
[script]
"513" = "「Ư——Kuu!」"
"514" = "「————A——hà————ưm——Ku」"
"530" = "「Ya……a……ngài Soutetsu……ưm……những, lời\n——như thế——xin ngài đừng——nói ra——ưm.」"
"812" = "「Hya——a——ưm——a——cô, bé,\ntử cung——bị, dương, vật——vuốt, vuốt ve.」"
"816" = "「Ya……giọng nói đó của ngài……phù, a……em……\nnúm, vú……ưm——xấu hổ quá……ạ.」"
"819" = "「Kiufuuuuuuuuunn!!?」"
"821" = "「Kya!?」"
"824" = "「Phù——Fukyu——ưm! Phù——ưm——\nphù——phù——ưm——ưm ưm!!」"
"829" = "「Pua……a——phù……phù——ưm——mút」"
"830" = "「Fua!」"
"831" = "「Fua! A! A! A!!!」"
"832" = "「Fua!!!」"
"838" = "「Mút——Chuuu——ưm——phù——ưm——\nphù——ưm! Phù! Ưm ưm ưm!!!」"
"839" = "「Hí, ưm——a——chỗ đó——chỗ đó! Bị cọ xát,\nchầm chậm——ưm——vào——đó——hí——ưm kiu!」"
"842" = "「Hia——a——a——a a a a!!!!」"
"843" = "「Hia——a! Phù——ưm——Ku——Na!」"
"844" = "「Hí kiuuuuuuuuuuuuuưm ưm ưm ưm ưm!!!」"
"845" = "「Hiu!!!」"
"847" = "「Hà——chụm——ưm——chụt——phù, a——\nưm, mút——Hyua——liếm——ưm, Ku——a!」"
"849" = "「Hà——hí——a——S-Soutetsu——ngài——\nưm——thích——thích lắm——Hyau!」"
"852" = "「Hà——a——vẫn còn——to——ưm——\nưm——Fua——ưm ku!!!」"
"854" = "「Hà……Hya, a——ưm——chỗ, cửa——\nvào……chầm, chậm——từ từ——phù, hà.」"
"856" = "「Ôô——」"
"863" = "「A……a……Fua……ngài Soutetsu——」"
"865" = "「Aa……ừm.」"
"866" = "「Aa……ngài đang nói đến miếng dán ngực sao ạ.」"
"869" = "「Iaaaan~~! Hà——phù——a——ưm!!」"
"871" = "「An!!!」"
"872" = "「Kua!」"
"874" = "「Kua!!!!」"
"875" = "「Aa, ra là vậy.」"
"881" = "「Fa——a——a——a——a——\nhà——hà——hà——hà——hà——」"
"882" = "「Ku——」"
"884" = "「Ưm——phù——phù——phù——ư——liếm——\nmút——chụt——Fa.」"
"887" = "「Ưm——phù——mút——mút——ưm——\nchụt——ưm ku——phù——phù ư ư!」"
"897" = "「Ưm——Ku!」"
"904" = "「Ưm……phù……Ku……a——dương, vật……của——ngài Soutetsu……\ncứng quá, ướt, nhẹp……dương vật, của ngài.」"
"909" = "「Ưm……a——phù……chậm, chạp——thế này, thì.\nKu, phù——dương, vật——của ngài Soutetsu——ưm kiu!?」"
"915" = "「Ưm……ực——Pua——Fa——a……\nNgài Soutetsu……Ngài Soutetsu……Ngài Soutetsu.」"
"924" = "「Nhyu——ưm——Nyu——ưm ưm~——\nphù——ưm phù——phù——phù~——」"
"925" = "「Nhyun!!」"
"926" = "「Nhyu!!!」"
"929" = "「Kiufuuuuuuuun!!!!」"
"930" = "「Ưm kiu!!? A……Fa……a!」"
"932" = "「Ưm kiu!? Ưm!!?」"
"934" = "「Ưm ưm ưm ưm~~~!! Ưm, phù——ưm! Phù,\nưm, mút——liếm——Juuu——rột rột~!」"
"935" = "「Ưm ku!!!!」"
"937" = "「Ưm ku!? Kahyu——a? Ngài, Soutetsu\n——của, em——bên trong——đã đến, nơi——sâu, nhất rồi.」"
"939" = "「Ku!」"
"940" = "「Ưm! Phù——Nhyu! Ưm ưm!!!!」"
"941" = "「Ưm! Phù! Phù! Ưm! Phù! Fua!\nƯm! Ưm ku! Ưm!!!」"
"946" = "「Ưm!!? Ưm!!!\nƯm ư ư ư ư ư ư ư ư ư ư ư ư ư ư ư ư ư~!!!!」"
"948" = "「Pua! Hà——a——ưm……Fua——\nhà——hà——hà——Fuaaa~——!」"
"950" = "「Hạnh phúc……Fa——hạnh phúc, quá——ngài Soutetsu,\nphu, quân——của riêng——một mình, em.」"
"1020" = "「Là cô bé, ạ. Ngài Soutetsu…… Fa——cô bé của em,\nnhỏ xíu——như một khe hở thế này……đang.」"
"1052" = "「Suzu——Ku——a」"
"1335" = "Bị cậu bé cương cứng đến cực đại của tôi đâm xuyên qua——aa."
"1963" = "（Aa——ra là vậy sao.）"
```

## Kết bài

File ハチロクh6_ウェディングドレスを脱ぎ捨てて (461 dòng) đã sửa moan xong: 58 dòng đổi (46 romaji + 12 đếm nguyên âm), 196 dòng rên/SFX giữ nguyên, 0 dòng gasp Ư bị đụng, 0 dòng "Kh" (file không có). 6 cờ để parent/đợt thống nhất (§5), trong đó F1 (Ku vs Hự) và F2 (ひ、ぐっ) là câu hỏi mở toàn dự án. Khối TOML 58 khóa đã parse-kiểm chứng, 0 sai lệch.
