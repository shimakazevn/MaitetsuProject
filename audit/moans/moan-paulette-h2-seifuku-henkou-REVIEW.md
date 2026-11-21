# Moan-fix REVIEW — ポーレットh2_制服変更？.txt.toml

## 1. Xác minh file

- File TOML: `sources/toml2/translation_toml/03_Paulette/#U30dd#U30fc#U30ec#U30c3#U30c8h2_#U5236#U670d#U5909#U66f4#Uff1f.txt.toml`
- TOML md5: `a46eac41e8c17082b9e6c101650f8cfc` (BOM + CRLF, 603 CRLF); sections `[info]`, `[characters]`, `[character_subs]`, `[script]`, `[selections]`.
- CSV3: 1 bộ duy nhất, 292 dòng, 292 key duy nhất, không key trùng. TOML khớp CSV3 theo flat-match (135 lệch chỉ do TOML gộp `\n` thành khoảng trắng — CSV3 là chuẩn cho fix list, theo AUDIT-BRIEF).
- Audit của file đã merge: 47 dòng sai (audit-paulette-h2-uniform-change). Trong đó 13 key trùng với đợt moan này (923, 932, 950, 952, 956, 957, 963, 985, 991, 1004, 1009, 1096, 1135); xem §6 về cách xử lý trùng.
- Đã đọc toàn bộ 292 dòng (JP + TW + VN cũ). Mẫu quét rên/SFX bắt 99 dòng: họ ひゃ/きゃ 20, họ fa/fu 8, đầu ん 3, SFX trong ngoặc （ ） 46, rên khác 22.

## 2. Tổng quan lỗi

Đổi **33 dòng** (11,3% của 292 dòng; 33/99 dòng rên/SFX):

- Romaji cho họ fa/fu + ひゃ/きゃ — 8 dòng (932, 942, 944, 956, 991, 992, 1003, 1008): "phá"/"phù" cho ふあ/ふぁ sai theo quy tắc khóa (không bao giờ "phá"; ふあ→"phùa" nhưng "phà"/"phùa" nghe ngượng trong rên H — tiền lệ đã merge h1 976/987/1065 đưa "phà" của audit về romaji "Fua"/"Fa"); "Á" cho きゃっ/きゃふっ mất phụ âm k.
- "Á"/từ cho やっ/やあ — 5 dòng (927, 935, 946, 980, 1025): "Á" cho やっ/やあ mất phụ âm y (tiền lệ h3 890 "Ya", 894 "Yaa"; parent merge Hibiki h6 2082 "a"→"Ya"); "Đừng"/"khôngggggg" thay âm rên bằng từ.
- Rên "Ưm + romaji" trộn trong MỘT âm — 7 dòng (938, 1019, 1021, 1022, 1023, 1025, 1026): んひゅ/んきゅ/んゆ/んふ bị tách thành "Ưm hyu"/"Ưm yu" — một âm = một cách diễn (tiền lệ mayami 1530/1532/1533: Nhyu/Nku/Nyu).
- Đếm nguyên âm sai — 9 dòng (923, 929, 932, 946, 957, 962, 963, 992, 1008 — tính cả 929; một số dòng vừa romaji vừa đếm): rên dài thiếu/thừa 1–3 nguyên âm (923 thừa 1 a, 962 thừa 1 a, 1021 thừa 3 u, 1022 thừa 2 u).
- Mất hẳn phụ âm mora — 4 dòng (928 んぎゅっ→"ưm", 931 �んくっ→"ưm", 937 あうっ→"á", 967 ふぇっ→"Á"): âm sau bị nuốt mất.
- Khác — 4 dòng (950 "Hya un" tách một âm làm đôi; 972 うう→"Ư" thiếu 1 u + うぇ→"a" sai âm; 1006 ちゅうっ→"chùn chụt" nhân đôi một tiếng hôn dài; 1660 くちいっ→"Đút vào" khác hẳn 1645 "Nhóp nhép" cùng JP).

## 3. Các dòng sửa

### 923 [ポーレット] — đếm a thừa 1
- JP: 「けどっ――けどぉっ――わたしっ――わらひぃっ――\nあっ――ふああああああああああんっっっっ！」
- TW: 「可是——可是——我已經——我已經——啊——呼啊啊啊！」
- VN cũ: 「Nhưng mà——nhưng mà——em——em——\ná——fuaaaaaaaaaaan!」
- VN mới: 「Nhưng mà——nhưng mà——em——em——\ná——fuaaaaaaaaaan!」
- Lý do: ふああああああああああん = 10 âm a (ふあ + あ×9); VN cũ 11 a, thừa 1. Giữ romaji — audit đổi sang "phuàààààààààn" (cũng thiếu 1 a, 9 à) bị đợt moan đè theo quy tắc fallback (rên dài → romaji; tiền lệ h1).

### 927 [ポーレット] — やっ thành từ "Đừng"
- JP: 「やっ――いまっ――ひっ――あっ――\nわら――ひっ――イっ――イって――るっ――んっ」
- TW: 「呀——剛才——呀——啊——我已經——丟了——嗯」
- VN cũ: 「Đừng——vừa nãy——hi——á——\nem——hi——đang——đang ra——rồi——ưm.」
- VN mới: 「Ya——vừa nãy——hi——á——\nem——hi——đang——đang ra——rồi——ưm.」
- Lý do: やっ là tiếng rên trong chuỗi lên đỉnh (イってる), không phải từ "đừng"; diễn thành "Ya" (giữ phụ âm y — tiền lệ h3 890). Các token còn lại giữ: ひっ→"hi", あっ→"á", んっ→"ưm".

### 928 [ポーレット] — mất ぎゅ
- JP: 「きあっ――あっ――ひおっ――んぎゅっ――」
- TW: 「呀——啊——咿——嗯——」
- VN cũ: 「Kia——á——hio——ưm——」
- VN mới: 「Kia——á——hio——Ngyu——」
- Lý do: んぎゅっ bị diễn thành "ưm" — mất hẳn phụ âm ぎゅ. Romaji "Ngyu" (cùng họ ん + phụ âm như Nku/Nyu/Nhyu đã merge).

### 929 [ポーレット] — thiếu 1 a + sót んううっ (lượt soát 2 bổ sung)
- JP: 「ひゃっ――あっ！\nんううっ――ふえっ――ふやぁっ」
- TW: 「呀——啊！嗯——呼——呀」
- VN cũ: 「Hya——á!\nƯm——phuê——phuya.」
- VN mới: 「Hya——á!\nNuu——phuê——phuyaa.」
- Lý do: んううっ = 2 âm u, VN cũ "Ưm" chỉ 1 nguyên âm → "Nuu"; ふやぁっ = 2 âm a, "phuya" chỉ 1 a → "phuyaa" (giữ dạng VN khóa "phuya"). ふえっ→"phuê" đã đúng, giữ.

### 931 [ポーレット] — mất く
- JP: 「ひゃっ――んくっ――子宮――ごりゅ――って――あ」
- TW: 「呀——嗯——子宮——被頂到了——啊」
- VN cũ: 「Hya——ưm——tử cung——bị đâm, phập——vào——a.」
- VN mới: 「Hya——Nku——tử cung——bị đâm, phập——vào——a.」
- Lý do: んくっ bị diễn thành "ưm" — mất hẳn phụ âm く. Romaji "Nku" (tiền lệ mayami 1532, nagifukami-h1 1562).

### 932 [ポーレット] — thiếu 1 a + "phá" sai khóa
- JP: 「ひゃあっ――んっ――おまん、こ――おそうじ――\nふあっ――ていねいに、おそうじ――らめ、なのぉっ」
- TW: 「呀——嗯——小穴——被清理了——呼啊——清理得——好仔細——不要啦」
- VN cũ: 「Hya——ưm——âm, đạo——đang được dọn dẹp——\nphá——dọn dẹp, cẩn thận quá——đừng, mà.」
- VN mới: 「Hyaa——ưm——âm, đạo——đang được dọn dẹp——\nFua——dọn dẹp, cẩn thận quá——đừng, mà.」
- Lý do: ひゃあっ = 2 âm a → "Hyaa" (VN cũ 1 a); ふあっ→"phá" sai theo quy tắc khóa (không bao giờ "phá") — đưa về romaji "Fua" theo tiền lệ h1 (audit sửa "phà" cũng bị đợt moan đè về romaji).

### 935 [ポーレット] — "Á" cho やっ mất phụ âm y
- JP: 「やっ――パンツごと――おしこむ――なんっ――！？」
- TW: 「呀——連內褲一起——按揉著——啊！？」
- VN cũ: 「Á——nhấn cả——quần lót vào——sao——!?」
- VN mới: 「Ya——nhấn cả——quần lót vào——sao——!?」
- Lý do: やっ = /ja/ — "Á" mất phụ âm y (tiền lệ h3 890 "Ya"; parent merge Hibiki h6 2082 "a"→"Ya").

### 937 [ポーレット] — mất う của あうっ
- JP: 「ひゃふうううっ！？　すわっ――吸われ――って――\nあうっ――ごくんって――んっ――ちゅう――って！」
- TW: 「呀唔！？被吸到了——啊嗚——還喝下去——被親到了！」
- VN cũ: 「Hyafuuuu!? Bị húúúút——vào——rồi——\ná——uống mất rồi——ưm——hôn——nữa!」
- VN mới: 「Hyafuuuu!? Bị húúúút——vào——rồi——\nAu——uống mất rồi——ưm——hôn——nữa!」
- Lý do: あうっ = 2 mora (a+u) — "á" chỉ diễn 1. Romaji "Au" (tiền lệ 964 あふ→"Afu"). ひゃふうううっ→"Hyafuuuu" đã đúng 4 u, giữ.

### 938 [ポーレット] — trộn "Ưm hyu" + thiếu u của んうううっ
- JP: 「ひゅあっ――はがれっ――る――\nんひゅっ――これっ――すごっ――んうううっ！」
- TW: 「呀啊——要剝掉了——嗯啊——這樣——好刺激——嗯！」
- VN cũ: 「Hyua——sắp bong——ra——\nưm hyu——cái này——tuyệt quá——ưm!」
- VN mới: 「Hyua——sắp bong——ra——\nNhyu——cái này——tuyệt quá——Nuuu!」
- Lý do: んひゅっ là MỘT âm — "ưm hyu" trộn VN + romaji, vi phạm một-dòng-một-cách-diễn → "Nhyu" (quy tắc 3b); んうううっ = 3 âm u, "ưm" chỉ 1 nguyên âm → "Nuuu".

### 942 [ポーレット] — きゃふっ thành "Hya"
- JP: 「きゃふっ！　あっ――ふとっ――太、いっ――」
- TW: 「呀！啊——好粗——好粗——」
- VN cũ: 「Hya! Á——to——to, quá——」
- VN mới: 「Kyafu! Á——to——to, quá——」
- Lý do: きゃふっ = kya + fu — "Hya" diễn thành ひゃ, sai hẳn phụ âm đầu (cùng lỗi với 1023 きゅ→"hyu"). Romaji "Kyafu".

### 944 [ポーレット] — "Á" cho きゃっ
- JP: 「きゃっ！？」
- TW: 「呀！？」
- VN cũ: 「Á!?」
- VN mới: 「Kya!?」
- Lý do: きゃ→"Kya" theo quy tắc 3b (21/11 ~11:55) — "Á" mất phụ âm ky (tiền lệ h3 898 "Kya", 902 "Kyaa").

### 946 [ポーレット] — やあっ thiếu 1 a (2 chỗ)
- JP: 「やあっ！？　らめっ――んっ――ちゅうちゅう、しな、\nがら――んっ――おしゃ、べり――しちゃ、やあっ――」
- TW: 「呀！？不行——嗯——不要一邊吸著——一邊說話」
- VN cũ: 「Á!? Đừng——ưm——đừng có vừa mút mát,\nvừa——ưm——nói, chuyện——chứ, á——」
- VN mới: 「Yaa!? Đừng——ưm——đừng có vừa mút mát,\nvừa——ưm——nói, chuyện——chứ, Yaa——」
- Lý do: やあっ = 2 âm a, "Á"/"á" chỉ 1 a và mất phụ âm y → "Yaa" cả hai chỗ (tiền lệ h3 894 "Yaa").

### 950 [ポーレット] — một âm tách làm đôi
- JP: 「ひゃうんっ！？　き、きたないっ――だって、\nおしっこ――んっ――そうてつ、くんっ――っ！」
- TW: 「呀！？很、很髒的——因為——有尿——嗯——雙鐵——嗯！」
- VN cũ: 「Hya un!? B, bẩn lắm——bởi vì,\ncó nước tiểu——ưm——Soutetsu, này——!」
- VN mới: 「Hyaun!? B, bẩn lắm——bởi vì,\ncó nước tiểu——ưm——anh Soutetsu, này——Ư!」
- Lý do: ひゃうんっ là MỘT âm — "Hya un" tách thành hai. SỬA (parent lúc merge): giá trị fix xây trên giá trị fix của audit (không phải VN cũ) — giữ "anh Soutetsu" (xưng hô, audit) + "Ư!" cuối dòng (gasp っ, sweep/audit) của audit, chỉ đổi token rên "Hya un"→"Hyaun". Áp MỘT giá trị mỗi key ở đợt thống nhất, nên giá trị moan phải chứa cả 2 lớp sửa.

### 956 [ポーレット] — ふぇ mất ぇ + ふあ thành "phúa"
- JP: 「ふ……ふぇ……ふあ」
- TW: 「呼……呼……呼啊」
- VN cũ: 「Phù... phu... phúa.」
- VN mới: 「Phù... phuê... Fua.」
- Lý do: ふぇ→"phu" mất hẳn âm ぇ → "phuê" theo dạng khóa + tiền lệ cùng file 929 "phuê" (audit chọn "phê" ở đây là không nhất quán với chính 929); ふあ→"phúa" sai thanh (khóa là "phùa") và nghe ngượng → romaji "Fua" theo tiền lệ h1.

### 957 [ポーレット] — ふぇ mất ぇ + ふやぁぁぁあ thiếu 1 a
- JP: 「ふぇ……あ……ふやぁぁぁあ」
- TW: 「呼……啊……啊呀」
- VN cũ: 「Phu... a... fuyahaaa.」
- VN mới: 「Phuê... a... phuyaaaaa.」
- Lý do: ふぇ→"phuê" (như 956); ふやぁぁぁあ = 5 âm a (や + ぁ×3 + あ) — "fuyahaaa" chỉ 4 a. Giữ dạng VN khóa "phuya" + đủ 5 a → "phuyaaaaa" (audit đổi sang "phuyaaa" chỉ 3 a, thiếu 2).

### 961 [双鉄H] — ぷあっ thành "Phù"
- JP: 「ぷあっ」
- TW: 「呼啊」
- VN cũ: 「Phù.」
- VN mới: 「Pua.」
- Lý do: ぷあっ = /pua/ — "Phù" diễn thành ふ, sai hẳn phụ âm p (tiền lệ kisaki h3 2207 ぷぁ→"Pua", nagifukami-h1 1525 "Pua!").

### 962 [ポーレット] — đếm a thừa 1
- JP: 「ふぁぁぁぁっぁぁぁぁんっ！」
- TW: 「呼啊啊啊！」
- VN cũ: 「Fuaaaaaaaaan!」
- VN mới: 「Fuaaaaaaaan!」
- Lý do: ふぁぁぁぁっぁぁぁぁん = 8 âm a (ふぁ + あ×4 + あ×3); VN cũ 9 a, thừa 1. Giữ romaji, chỉ sửa số lượng.

### 963 [ポーレット] — giữ romaji + sửa đếm 11u→10u (parent bổ sung lúc merge)
- JP: 「あふうううううううううんっ！！！」
- TW: 「呼啊啊啊！！！」
- VN cũ: 「Afuuuuuuuuuuun!!!」
- VN mới: 「Afuuuuuuuuuun!!!」
- Lý do (parent): JP あふうううううううううん = ふ 1u + う×9 = **10u** (đếm lại bằng máy từng ký tự); VN cũ romaji 11u — thừa 1u, KHÔNG đúng số lượng như agent ghi ở §5. Audit đổi thành "À phùuuuuuuuuun!!!" (đủ 10u nhưng Việt hoá, lý do "không phải tiếng Việt" ra đời TRƯỚC quy tắc romaji fallback) — không áp fix audit; giữ romaji, chỉ sửa đếm về 10u. TW 呼 xác nhận đây là tiếng thở, không phải từ.

### 967 [ポーレット] — ふぇっ thành "Á"
- JP: 「ふぇっ」
- TW: 「哎」
- VN cũ: 「Á.」
- VN mới: 「Phuê.」
- Lý do: ふぇっ = /fe/ — "Á" là âm あっ, sai hẳn âm. "Phuê" theo dạng khóa (cùng file 929 ふえっ→"phuê").

### 972 [ポーレット] — うう thiếu 1 u + うぇ thành "a"
- JP: 「うう……うぇ……きもちわるいよぉ\n……べたべたするよぉ」
- TW: 「唔……哎……感覺好不舒服……黏黏的」
- VN cũ: 「Ư... a... khó chịu quá à\n...nhớp nháp quá.」
- VN mới: 「Ưư... Uê... khó chịu quá à\n...nhớp nháp quá.」
- Lý do: うう = 2 âm u → "Ưư" (VN cũ 1 u); うぇ = /we/ (tiếng rên khó chịu) — "a" mất hẳn âm we → "Uê" (tiếng Việt tự nhiên cho vẻ khó chịu).

### 980 [ポーレット] — やあああっ thành từ "khôngggggg"
- JP: 「あっ――あっ――やあああっ」
- TW: 「啊——啊——呀啊」
- VN cũ: 「Á——á——khôngggggg.」
- VN mới: 「Á——á——Yaaaa.」
- Lý do: やあああっ = 4 âm a, là tiếng rên — "khôngggggg" thay âm rên bằng từ "không" (やあ không phải từ phủ định; từ phủ định là やだ/いやだ). Romaji "Yaaaa" theo tiền lệ cùng file 940 (9 a → 9 a).

### 991 [ポーレット] — ふぁ thành "phá"
- JP: 「あ……ひあ……あっ――ふぁ――あっ――あっ――あ」
- TW: 「啊……呀……啊——呼——啊——啊——啊」
- VN cũ: 「A... hia... á——phá——á——á——a.」
- VN mới: 「A... hia... á——Fa——á——á——a.」
- Lý do: ふぁ→"phá" sai theo quy tắc khóa (không bao giờ "phá") — đưa về romaji "Fa" theo tiền lệ h1 987 ふぁっ→"Fa" (audit sửa "phà" cũng bị đợt moan đè). ひあ→"hia" đã đúng quy tắc 3b, giữ.

### 992 [ポーレット] — ふあっ thành "phù" + はあっ thiếu 1 a
- JP: 「あ……ふあっ――あっ――――はっ――はあっ――」
- TW: 「啊……呼啊——啊——呼——呼啊」
- VN cũ: 「A... phù——á――――hà——hà——」
- VN mới: 「A... Fua——á――――hà——Hàà——」
- Lý do: ふあっ = /fua/ — "phù" mất hẳn âm a → romaji "Fua" (tiền lệ h1; audit gọi 1008 "phù" cho ふあっ là "đúng" nhưng đợt moan đè theo quy tắc fallback); はあっ = 2 âm a → "Hàà" (VN cũ 1 a — tiền lệ h3 948 はぁっ→"hàà").

### 1003 [双鉄H] — くあっ thành "Khà"
- JP: 「くあっ！」
- TW: 「啊！」
- VN cũ: 「Khà!」
- VN mới: 「Kua!」
- Lý do: くあっ = /kua/ — "Khà" mất âm u (khác với くっ→"hự" ở 909/978, ở đó không có nguyên âm). Romaji "Kua" (tiền lệ h9 2101 sửa "Aa"→"Kuaa" vì JP thắng TW; kisaki h3 2217, mikuro 1793 "Kua").

### 1006 [ポーレット] — ちゅうっ nhân đôi
- JP: 「れるっ――んっ――ちゅっ――ちゅうっ」
- TW: 「啾嚕——嗯——啾啾——啾嚕」
- VN cũ: 「Liếm——ưm——chụt——chùn chụt.」
- VN mới: 「Liếm——ưm——chụt——chuút.」
- Lý do: ちゅうっ là MỘT tiếng hôn dài (ちゅ + う + っ) — "chùn chụt" nhân thành hai tiếng. "chuút" theo đúng cách diễn cùng file ở 959 (ちゅうっ→"chuút").

### 1008 [ポーレット] — ふあっ thành "phù" + ああんっ mất ん
- JP: 「ん……ふあっ――あっ――ああんっ」
- TW: 「嗯……呼啊――啊――嗯」
- VN cũ: 「Ưm... phù——á——a.」
- VN mới: 「Ưm... Fua——á——Aan.」
- Lý do: ふあっ→"Fua" (như 992); ああんっ = 2 âm a + ん — "a" chỉ 1 a và mất hẳn ん → "Aan".

### 1019 [ポーレット] — trộn "Ưm hyu" + "ưm fuuuuu"
- JP: 「んひゅっ！　あっ――んふううううっ――」
- TW: 「嗯呼！啊——嗯唔——」
- VN cũ: 「Ưm hyu! Á——ưm fuuuuu——」
- VN mới: 「Nhyu! Á——Nfuuuuu——」
- Lý do: んひゅっ là MỘT âm → "Nhyu" (quy tắc 3b; tiền lệ mayami 1530); んふううううっ = 5 âm u (ふ + う×4) — "ưm fuuuuu" trộn VN + romaji cho một âm → "Nfuuuuu" (5 u).

### 1021 [ポーレット] — trộn + thừa 3 u
- JP: 「んひゅううううううううううっ！！！」
- TW: 「嗯啊啊啊啊！！！」
- VN cũ: 「Ưm hyuuuuuuuuuuuuuu!!!」
- VN mới: 「Nhyuuuuuuuuuuu!!!」
- Lý do: んひゅううううううううううっ = 11 âm u (ひゅ + う×10) — VN cũ 14 u, thừa 3, lại trộn "Ưm" → "Nhyu" + 10 u = 11 u.

### 1022 [ポーレット] — trộn + thừa 2 u
- JP: 「んひゅうううんっ！！」
- TW: 「嗯啊啊！！」
- VN cũ: 「Ưm hyuuuuuun!!」
- VN mới: 「Nhyuuuun!!」
- Lý do: んひゅうううんっ = 4 âm u (ひゅ + う×3) — VN cũ 6 u, thừa 2, lại trộn "Ưm" → "Nhyuuuun" (4 u).

### 1023 [ポーレット] — sai phụ âm ky→hy + trộn
- JP: 「んきゅうううううんっ！」
- TW: 「嗯啊！」
- VN cũ: 「Ưm hyuuuuuun!」
- VN mới: 「Nkyuuuuuun!」
- Lý do: んきゅうううううんっ = 6 âm u (きゅ + う×5) — VN cũ dùng "hyu" cho きゅ (sai phụ âm, như 942 きゃふ→"Hya"), lại trộn "Ưm" → "Nkyuuuuuun" (6 u).

### 1025 [ポーレット] — trộn "Ưm yu" + "Á" cho やっ
- JP: 「んゆっ！　やっ――くり――トリス……んっ――\nくり、くり――しちゃ…………らめっ」
- TW: 「嗯！呀——陰蒂——嗯……不要……揉來揉去……」
- VN cũ: 「Ưm yu! Á——âm——vật... ưm——\nđừng có... mân, mê... mà.」
- VN mới: 「Nyu! Ya——âm——vật... ưm——\nđừng có... mân, mê... mà.」
- Lý do: んゆっ là MỘT âm → "Nyu" (tiền lệ mayami 1533); やっ→"Ya" (giữ phụ âm y, như 927/935).

### 1026 [ポーレット] — trộn "Ưm hyu"
- JP: 「んひゅっ！？」
- TW: 「嗯！？」
- VN cũ: 「Ưm hyu!?」
- VN mới: 「Nhyu!?」
- Lý do: んひゅっ là MỘT âm → "Nhyu" (quy tắc 3b).

### 1660 [monologue] — cùng JP, khác cách diễn với 1645
- JP: 「（くちいっ）」
- TW: 「（插入）」
- VN cũ: 「（Đút vào）」
- VN mới: 「（Nhóp nhép）」
- Lý do: くちいっ là tiếng chụt ướt khi đút vào — cùng JP này ở 1645 đã diễn là "（Nhóp nhép）" (tiếng); 1660 diễn thành từ "Đút vào" (hành động) là không nhất quán trong file → thống nhất theo 1645.

## 4. Các dòng rên đã giữ (đáng chú ý)

- 940 やぁあああああああっ→"Yaaaaaaaaa" (9 a ✓); 941 ひゃうっ→"Hyau!" ✓; 943 ひあんっ→"Hian!!" ✓; 948 ひゃっ→"Hya!?" ✓.
- 951/1018 ああ――→"À——" — GIỮ theo tiền lệ Paulette h1 1004 + h3 944 (ああ thở dài: công thức 1+0=1); khác với はあっ/やあっ trong rên (992/946 đã sửa đủ số a).
- 955 ひゃっ→"hya", 964 ひゅあっ→"hyua" — chữ thường giữa dòng, chỉ là chính tả, giữ.
- 959 ちゅむ→"chùn chụt" — GIỮ: ちゅむ 2 mora → 2 nhịp là hợp lý (khác 1006 ちゅうっ 1 âm dài đã sửa thành "chuút"); ちゅうっ→"chuút" ✓.
- 966 ふわ→"Phì." — hơi thở nhẹ, giữ (không phải cười ふふっ).
- 969 えへへっ→"Ehehe." ✓; 974 む→"Ưm", ぷっ→"phụt" ✓; 975 うっ→"Ư." ✓; 977 ひ→"hi", あ→"a" ✓; 978 くっ→"hự" ✓.
- 979 っ→"Ư", ふっ→"phù" ✓ (sweep — không đụng lại).
- 983/1020 んうっ→"ưm"/"Ưm" (1 u ✓); 1009 あっ→"a" (tiền lệ h1 993/997/998); 986 あっ……→"A..." (dấu ... diễn cắt ngang; sweep không ghi).
- 1007 ん――→"Ưm——" ✓; 1027 うむ？→"Hửm?" ✓; 1028 うふふ→"Ufufu" ✓ (cười, không phải rên); 1044 ンッ→"ưm" ✓; 1096 ふ→"phù", あっ→"á" ✓; 1128 んっ→"ưm" ✓.
- 880/1059 っ gắn từ nội dung (だめぇっ, るっ, だからっ) — nhấn mạnh, không phải gasp; sweep không ghi — giữ.
- SFX trong ngoặc giữ: 1627 "Múúúúúúúúút" (9 ú ✓); 1631 "phụtttt"/1643 "phậpppppp" (kéo dài bằng phụ âm cuối — phong cách SFX của file); 1679 "Siết chặtttttt"/1680 "Thúc mạạnnnnh" (diễn bằng từ + kéo dài); 1682 ぐっ→"Hự", ぐううううっ→"Hựựựựự" ✓; 1640 ちゅむっ→"Chụt!?" ✓; 1695 きゅむむっ→"Siết chặt!" ✓.
- 1671/1688/1694 ぐっ diễn bằng động từ ("Nhấc lên"/"Ấn") — GIỮ theo ngữ cảnh (tiếng gắng sức lúc nâng/ấn, khác 1682 là tiếng gầm lúc thúc); spontaneity theo ngữ cảnh.

## 5. Cờ (flag — không tự quyết, chờ parent/đợt thống nhất)

1. **963 — ĐÃ SỬA (parent lúc merge, không còn là cờ):** JP có 10u (ふ 1u + う×9, đếm máy từng ký tự) — VN cũ romaji 11u thừa 1u, agent đếm nhầm 11u nên tưởng "đã đúng". Fix moan = romaji 10u "Afuuuuuuuuuun!!!", KHÔNG áp fix audit "À phùuuuuuuuuun!!!" (đủ 10u nhưng Việt hoá theo lý do tiền-romaji-rule). Đã thêm vào wrong.json (key 963, kind count).
2. **Các dòng gasp Ư của sweep/audit (952, 985, 1004, 1135, 950-cuối) — KHÔNG đụng lại** theo quy tắc (không xem lại 1.146 dòng sweep). ĐÃ GIẢI QUYẾT (parent): cả 5 dòng đều đã có fix trong audit wrong.json (952 "Ư!", 985 "Á——Ư!", 1004 "ƯƯ!!?", 1135 "~~~~~~~~Ư!!!", 950-cuối nằm trong fix audit của 950) — sẽ áp ở đợt thống nhất. TOML-2 giữ VN cũ là ĐÚNG mô hình amendment (fix chưa áp vào TOML bao giờ, kể cả fix audit); không có gì thiếu. Riêng 950: fix moan đã xây trên giá trị audit (giữ "anh Soutetsu" + "Ư!" cuối) — xem §3 950.
3. **960 — nói ngọng (miệng đầy):** 「やふほふほひは――ほうひを、へふらふほ」 → "Anh đang dọn dẹp——giúp em mà." — không phải dòng rên theo quy tắc 3b, để audit (audit đã sửa, key 960 trong 47 dòng).
4. **1001 くぅん sau tên** — giữ tên theo tiền lệ h1 (1022/1186: くぅん là kéo dài của くん, không phải rên).
5. **1639 れろっ/れるっ→"liếm"** — diễn bằng động từ, giữ (cặp nhất quán trong dòng).

## 6. Lượt soát 2

Đọc lại toàn bộ 33 giá trị fix đối chiếu JP (+TW khi cần), đếm lại độc lập từng rên dài bằng ký tự (923: 10 a; 962: 8 a; 963: 10 u; 957: 5 a; 932: 2 a; 946: 2 a ×2; 980: 4 a; 992: 2 a; 1008: 2 a + ん; 1019: 5 u; 1021: 11 u; 1022: 4 u; 1023: 6 u; 938: 3 u; 929: 2 u + 2 a). **33/33 tái kiểm chứng, 0 bỏ, 1 sửa** (32 của agent + 1 parent bổ sung 963: JP đếm máy 9う+ふ=10u, VN cũ 11u, fix romaji 10u; TW 呼 xác nhận tiếng thở) — lượt soát phát hiện 929 bị sót んうううっ→"Nuu" ở lượt 1 và đã bổ sung (giá trị fix của 929 được sửa, số dòng không đổi). Kiểm chứng chéo: JSON 33 mục dạng chuẩn (khóa string; jp/tw/old_vn khớp CSV3 tuyệt đối 33/33); khối TOML parse bằng tomllib: 33 khóa, 0 sai lệch giá trị; mỗi fix chỉ khác old_vn đúng token mục tiêu (kiểm chứng bằng thay thế chuỗi chính xác từng token) — TRỪ 950, giá trị fix xây trên giá trị audit (giữ "anh Soutetsu" + "Ư!" cuối của audit, chỉ đổi token rên); không dòng gasp Ư nào bị đụng (1003 "Khà"→"Kua": "Kh" đó là cách diễn sai của くあ, không phải Kh khóa cho っ); không dòng "Kh" khóa nào bị đổi.

## 7. Khối TOML (đã kiểm chứng parse)

Khối TOML dưới đây parse được bằng tomllib, **33 key, 0 sai lệch giá trị so với JSON**. Quy tắc ký tự xuống dòng: giá trị fix nào chứa ký tự xuống dòng dạng backslash-n (2 ký tự, như trong JSON và trong TOML gốc) thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON.

```toml
[script]
"923" = "「Nhưng mà——nhưng mà——em——em——\\ná——fuaaaaaaaaaan!」"
"927" = "「Ya——vừa nãy——hi——á——\\nem——hi——đang——đang ra——rồi——ưm.」"
"928" = "「Kia——á——hio——Ngyu——」"
"929" = "「Hya——á!\\nNuu——phuê——phuyaa.」"
"931" = "「Hya——Nku——tử cung——bị đâm, phập——vào——a.」"
"932" = "「Hyaa——ưm——âm, đạo——đang được dọn dẹp——\\nFua——dọn dẹp, cẩn thận quá——đừng, mà.」"
"935" = "「Ya——nhấn cả——quần lót vào——sao——!?」"
"937" = "「Hyafuuuu!? Bị húúúút——vào——rồi——\\nAu——uống mất rồi——ưm——hôn——nữa!」"
"938" = "「Hyua——sắp bong——ra——\\nNhyu——cái này——tuyệt quá——Nuuu!」"
"942" = "「Kyafu! Á——to——to, quá——」"
"944" = "「Kya!?」"
"946" = "「Yaa!? Đừng——ưm——đừng có vừa mút mát,\\nvừa——ưm——nói, chuyện——chứ, Yaa——」"
"950" = "「Hyaun!? B, bẩn lắm——bởi vì,\\ncó nước tiểu——ưm——anh Soutetsu, này——Ư!」"
"956" = "「Phù... phuê... Fua.」"
"957" = "「Phuê... a... phuyaaaaa.」"
"961" = "「Pua.」"
"962" = "「Fuaaaaaaaan!」"
"963" = "「Afuuuuuuuuuun!!!」"
"967" = "「Phuê.」"
"972" = "「Ưư... Uê... khó chịu quá à\\n...nhớp nháp quá.」"
"980" = "「Á——á——Yaaaa.」"
"991" = "「A... hia... á——Fa——á——á——a.」"
"992" = "「A... Fua——á――――hà——Hàà——」"
"1003" = "「Kua!」"
"1006" = "「Liếm——ưm——chụt——chuút.」"
"1008" = "「Ưm... Fua——á——Aan.」"
"1019" = "「Nhyu! Á——Nfuuuuu——」"
"1021" = "「Nhyuuuuuuuuuuu!!!」"
"1022" = "「Nhyuuuun!!」"
"1023" = "「Nkyuuuuuun!」"
"1025" = "「Nyu! Ya——âm——vật... ưm——\\nđừng có... mân, mê... mà.」"
"1026" = "「Nhyu!?」"
"1660" = "（Nhóp nhép）"
```

## Kết bài

File ポーレットh2_制服変更？ đã sửa xong tiếng rên theo quy tắc romaji: đọc 292/292 dòng, xét 99 dòng rên/SFX, đổi 33 dòng (8 romaji họ fa/fu + ひゃ/きゃ, 5 "Á"/từ cho やっ/やあ, 7 trộn "Ưm + romaji", 9 đếm nguyên âm, 4 mất phụ âm mora, 4 khác gồm 950/972/1006/1660 — một số dòng thuộc 2 nhóm). Lỗi tập trung ở rên ん + phụ âm bị tách thành "Ưm hyu"/"Ưm yu", họ fa/fu bị Việt hoá mất âm a ("phù" cho ふあ, "phá" cho ふぁ), và "Á" cho やっ/きゃっ làm mất phụ âm y/k. Mọi gasp Ư của audit/sweep và SFX độc thoại trong ngoặc đều giữ nguyên, trừ 1660 thống nhất theo 1645. Parent bổ sung lúc merge: 963 (giữ romaji, sửa đếm 11u→10u — agent đếm nhầm JP thành 11u) và 950 (giá trị fix xây trên giá trị audit, giữ "anh Soutetsu" + "Ư!" cuối). Cờ còn lại: 5 dòng gasp Ư đã có fix trong audit (áp ở đợt thống nhất; TOML-2 giữ VN cũ là đúng mô hình amendment), và 960 nói ngọng để audit.
