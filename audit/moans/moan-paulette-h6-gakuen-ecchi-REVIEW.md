# Moan-fix REVIEW — ポーレットh6_あなたとふたりの学園エッチ (moan-paulette-h6-gakuen-ecchi)

## §1. Xác minh file

- File: `ポーレットh6_あなたとふたりの学園エッチ.txt.toml` — route 03_Paulette, 304 dòng script.
- TOML md5: `1a184880b82bce1ce58a67cbb3a5f923` (khớp md5 audit), không có bản trùng trong 227 file TOML (đã kiểm lại bằng md5).
- CSV3: 1 bộ duy nhất (thư mục `03_Paulette`), 304 dòng, 0 key trùng. VN khớp TOML 304/304 sau chuẩn hoá `\n`→khoảng trắng (167 khác thô, toàn là TOML-2 làm phẳng `\n` — như audit đã ghi).
- Đã đọc 304/304 dòng (độc thoại 162, Paulette 80, Soutetsu 62). Audit trước đó: 36 sai (12 xưng hô + 11 thở gấp + 6 thở La-tinh + 5 SFX + 2 nói ngọng) — đợt moan này KHÔNG làm lại audit, chỉ sửa rên.
- Quy ước fix: một dòng (khoảng trắng thay `\n`), theo quy ước audit của chính file này (TOML gốc lưu một dòng).

## §2. Tồn kho rên (moan inventory)

- Dòng ứng viên rên/SFX đã xét: **193** (quét mẫu: っ gasp, họ fa/fu, ひゃ/ひあ/きゃ, くぁ/くあ, んきゅ, や, あんっ, かは, しょ, くっ/ぐっ, ぁあ, んう, nguyên âm dài, cười, SFX trong ngoặc — trong đó 44 dòng SFX độc thoại trong （ ）).
- Đổi: **35 dòng** — romaji 28 + đếm nguyên âm 5 + sai âm 2.
- Giữ: **158 dòng** (xem §5).
- Nhóm lỗi chính:
  - Họ fa/fu diễn "phù"/"phà" sai nguyên âm (12 dòng: 775, 777, 788, 807, 815, 833, 836, 838, 850, 853, 854, 859) → romaji Fa/Fua/Pa/Pua.
  - Mất phụ âm mora (7 dòng: 762 ひゃんっ mất n; 764/766 や mất y; 767 あんっ mất n; 796 きゃっ mất ky; 805 やふっ mất cả ya lẫn fu; 1348 かはっ mất ka) → romaji.
  - くぁ/くあ diễn "Ư a" mất k (806; 800/818 lật fix audit — xem F1) → "Kua".
  - んきゅ diễn "Ưm"/"ưm" mất kyu (805, 836, 868; 869 lật fix audit — xem F1/F2) → "Nkyu"/"Nkyun".
  - Đếm nguyên âm thiếu (6 dòng んうっ, 2 dòng はぁ, 1 dòng ふぅっ, 2 dòng ぁあっ, 2 dòng gộp mảnh ああ).
  - Sai âm (2 dòng: 916 しょっ→"hự"; 1600 ぐっ→"ưm").

## §3. Chi tiết từng dòng sửa (JP / TW / VN cũ / VN mới / lý do)

### §3.1 Romaji — họ ひゃ/ひあ/きゃ/や/あん (mất phụ âm hoặc mất ん)

**Key 762 (ポーレット)**
- JP: `「ひゃんっ――なにっ――これっ――」`
- TW: `「呀——這是——怎麼回事」`
- VN cũ: `「Hya——gì vậy——thế này——」`
- Sửa: `「Hyan——gì vậy——thế này——」`
- Lý do: ひゃんっ có ん — "Hya" làm mất ん. Tiền lệ h3 899 (thêm "n" cho ひゃ…んっ, parent đã kiểm chứng) và 凪ふかみh1 1223 "Hyan". Audit giữ "Hya" (xem §"Đã kiểm tra") — lật theo tiền lệ moan.

**Key 764 (ポーレット)**
- JP: `「やっ……熱い……です――双鉄、くんの―― おちん、ちんっ――」`
- TW: `「呀……好燙啊——雙鐵君——你的雞雞——」`
- VN cũ: `「Á……nóng……quá——của anh, Soutetsu—— Dương, vật——」`
- Sửa: `「Ya……nóng……quá——của anh, Soutetsu—— Dương, vật——」`
- Lý do: やっ có phụ âm y — "Á" làm mất hẳn. Tiền lệ h3 890/893/894/897 (や→"Ya"/"Yaa", đã merge). Quy tắc họ ひゃ 21/11: "Á" chỉ đúng khi JP không có phụ âm mora (あっ/あぁ).

**Key 766 (ポーレット)**
- JP: `「や……これっ――はっ――ぁあっ――こんなの―― しら、ないっ――んっ――きもち――よす、ぎっ――」`
- TW: `「呀……這樣——呼——啊——我以前——沒有過這種——實在——太刺激了——」`
- VN cũ: `「Á……thế này——hà——a——cảm giác này—— em không, biết——ưm——sướng——quá——」`
- Sửa: `「Ya……thế này——hà——Aa——cảm giác này—— em không, biết——ưm——sướng——quá——」`
- Lý do: や→"Ya" (như 764); ぁあっ = 2 mora a — "a" thiếu 1 âm → "Aa" (công thức đếm nguyên âm).

**Key 767 (ポーレット)**
- JP: `「あんっ」`
- TW: `「呀」`
- VN cũ: `「Á」`
- Sửa: `「An」`
- Lý do: あんっ có ん — "Á" làm mất ん. Tiền lệ lr-h1 giữ "An" cho あんっ.

**Key 796 (ポーレット)**
- JP: `「えっ！？　きゃっ！？　ひゃっ！！」`
- TW: `「哎！？哎！？呀！！」`
- VN cũ: `「Hả!? Á!? Hya!!」`
- Sửa: `「Hả!? Kya!? Hya!!」`
- Lý do: きゃっ → "Á" là lỗi mất phụ âm mora (quy tắc họ ひゃ 21/11). Tiền lệ h3 898/902/903 (きゃっ→"Kya"). ひゃっ→"Hya" giữ nguyên.

### §3.2 Romaji — họ fa/fu (ふぁ/ふあ/ぷぁ/ぷあ)

**Key 769 (ポーレット)**
- JP: `「きゃふっ！！！」`
- TW: `「呀！！！」`
- VN cũ: `「Kya!!!」`
- Sửa: `「Kyafu!!!」`
- Lý do: きゃふっ mất hẳn âm ふ trong VN cũ. Fix audit "Kyaphù" trộn 2 cách diễn (romaji "Kya" + Việt "phù") — một dòng = một cách diễn → romaji "Kyafu" (mẫu 770 "Hyafu").

**Key 770 (ポーレット)**
- JP: `「ひゃふっ！！？」`
- TW: `「呀！！？」`
- VN cũ: `「Hya!!?」`
- Sửa: `「Hyafu!!?」`
- Lý do: ひゃふっ mất âm ふ — thêm "fu". Giá trị này = giá trị audit (audit đã đúng).

**Key 775 (ポーレット)**
- JP: `「ふっ――ふぁっ――んっ――はぁっ――いいっ―― おまん、こっ――すごくっ――きゅうんっ――って！」`
- TW: `「呼——呼啊——嗯——呼——好——小穴——收縮得——好厲害——！」`
- VN cũ: `「Phù——phù——ưm——hà——sướng quá—— âm đạo——đang——siết chặt——lắm!」`
- Sửa: `「Phù——Fa——ưm——hàà——sướng quá—— âm đạo——đang——siết chặt——lắm!」`
- Lý do: ふぁっ → "phù" sai nguyên âm (a→u) → "Fa" (Hepburn chặt). はぁっ = 2 a — "hà" thiếu 1 → "hàà". ふっ→"Phù" giữ (hơi ngắn đúng âm u).

**Key 777 (ポーレット)**
- JP: `「はっ――あっ――ンッ――チュッ――ぷあっ――んん、 ふあっっ――あっ――あむっ！！！」`
- TW: `「呼——啊————啾噗——呼啊——嗯——呼啊——啊——嗯！！！」`
- VN cũ: `「Hà——a——ưm——chụt——phù——ưm, phù——a——ưm!!!」`
- Sửa: `「Hà——a——ưm——chụt——Pua——ưm, Fua——a——ưm!!!」`
- Lý do: ぷあっ→"Pua", ふあっっ→"Fua" (cả hai đều bị diễn "phù" mất âm a).

**Key 788 (ポーレット)**
- JP: `「はぁ……あっ――双鉄、くん……指…… エッチ――ですっ……ふぁ」`
- TW: `「呼……啊――雙鐵君……你的手指……好色啊……」`
- VN cũ: `「Hà……a——anh Soutetsu……ngón tay…… Dâm đãng——quá……phù」`
- Sửa: `「Hàà……a——anh Soutetsu……ngón tay…… Dâm đãng——quá……Fa」`
- Lý do: はぁ = 2 a → "Hàà"; ふぁ cuối dòng (hơi thở mềm) → "Fa" theo quy tắc fa (không dùng "phù" sai nguyên âm). Cờ: hơi thở mềm ふぁ có nên giữ "phù" không — xem F4.

**Key 807 (ポーレット)**
- JP: `「あっ――んっ――んっ――ふあっ――あっ！！！」`
- TW: `「啊——嗯——嗯——呼啊——啊！！！」`
- VN cũ: `「A——ưm——ưm——phù——a!!!」`
- Sửa: `「A——ưm——ưm——Fua——a!!!」`
- Lý do: ふあっ → "phù" mất âm a → "Fua".

**Key 815 (ポーレット)**
- JP: `「っ！　ふあっ！　あっ――んうっ――ちゅっ！」`
- TW: `「啊！呼啊！啊——嗯——啾！」`
- VN cũ: `「! Phù! A——ưm——chụt!」`
- Sửa: `「Ư! Fua! A——ưm ư——chụt!」`
- Lý do: Xây trên giá trị audit (audit chỉ thêm Ư đầu dòng). ふあっ→"Fua"; んうっ (2 mora) → "ưm ư" (xem §3.5).

**Key 833 (ポーレット)**
- JP: `「んっ――ふあっ――あっ――太っ―― っ――先、ぽっ――んあっ――んん～～っ！！！」`
- TW: `「嗯——呼——啊——好粗——嗯——前端——嗯——嗯～～！！！」`
- VN cũ: `「Ưm——phù——a——To quá—— ư——đầu, nấm——ư a——ưm～～!!!」`
- Sửa: `「Ưm——Fua——a——To quá—— ư——đầu, nấm——ư a——ưm～～!!!」`
- Lý do: Chỉ đổi token fa ふあっ→"Fua". Dòng này sweep ghi already-rendered — phần gasp đã diễn ("ư", "ư a", "ưm～～") KHÔNG đụng.

**Key 838 (ポーレット)**
- JP: `「ん――――むっ――――ごくんっ！　んっ――ごくっ ――ぁ――ふぁ――あっ……ぷぁぁ」`
- TW: `「嗯——唔——咕嚕！嗯——咕嚕——啊——呼——啊……呼啊」`
- VN cũ: `「Ưm――――ưm――――ực! Ưm——ực ——A——phù——a……phù」`
- Sửa: `「Ưm――――ưm――――ực! Ưm——ực ——A——Fa——a……Puaa」`
- Lý do: ふぁ→"Fa"; ぷぁぁ = 2 a → "Puaa" (VN cũ "phù" mất cả 2 âm a).

**Key 850 (ポーレット)**
- JP: `「ん……ふぁ……っ――ほーへふ……ふん……んっ―― ちゅ――ちゅむっ――ねろおっ――れるうっ――っ――」`
- TW: `「嗯……呼……啊——呼……嗯……嗯——雙鐵——啾噗——啾嚕——啾噗——嗯——」`
- VN cũ: `「Ưm……phù……——Houhehu……hun……ưm—— Chụt——chu——liếmmmm——liếmmmm——」`
- Sửa: `「Ưm……Fa……——Hôu-hê-hu……hừm……ưm—— Chụt——chụt——liếmmmmƯ——Ư——」`
- Lý do: Xây trên giá trị audit — chỉ đổi ふぁ→"Fa"; giữ nguyên toàn bộ fix audit (Hôu-hê-hu, hừm, chụt, ƯƯ cuối dòng).

**Key 853 (ポーレット)**
- JP: `「ん……ちゅっ――ちゅっ――んっ――しゅきっ―― ん――ぷあっ――あ。好き。です。あなたが。双鉄くん」`
- TW: `「嗯……啾——啾——嗯——我好喜歡——嗯――呼啊——啊，我好喜歡你，雙鐵君」`
- VN cũ: `「Ưm……chụt——chụt——ưm——thích, lắm—— Ưm——phù——a. Em thích. Thích anh. Anh Soutetsu.」`
- Sửa: `「Ưm……chụt——chụt——ưm——thích, lắm—— Ưm——Pua——a. Em thích. Thích anh. Anh Soutetsu.」`
- Lý do: ぷあっ → "phù" mất âm a → "Pua".

**Key 854 (ポーレット)**
- JP: `「んっ……ちゅっ――んむっ……ふあっ――ぷあっ！ あ！　あっ――あああっ！！」`
- TW: `「嗯……啾——嗯……呼啊——呼啊！啊！啊——啊啊啊！！」`
- VN cũ: `「Ưm……chụt——ưm……phù——phù! A! A——a a a!!」`
- Sửa: `「Ưm……chụt——ưm……Fua——Pua! A! A——Aaa!!」`
- Lý do: ふあっ→"Fua", ぷあっ→"Pua"; あああっ (3 a) bị tách thành "a a a" → gộp thành một cách diễn "Aaa" (tiền lệ ふかみh1: gộp mảnh rời của một âm rên duy nhất).

**Key 859 (ポーレット)**
- JP: `「ん……ぷっ――んくっ――――ぷあっ！　あっ……」`
- TW: `「嗯……噗——嗯——呼啊！啊……」`
- VN cũ: `「Ưm……phù——ưm――――phù! A……」`
- Sửa: `「Ưm……phù——ưm――――Pua! A……」`
- Lý do: ぷあっ → "Pua". んくっ→"ưm" giữ (xem §5).

**Key 944 (ポーレット)**
- JP: `「こ、れ……これ……ん――深っ――い――ふぁんっ！」`
- TW: `「這樣……這樣……嗯——好深——呼啊！」`
- VN cũ: `「Thế, này……thế này……ưm——Sâu——quá——phù!」`
- Sửa: `「Thế, này……thế này……ưm——Sâu——quá——Fan!」`
- Lý do: ふぁんっ = fa + n — "phù" mất cả âm a lẫn đuôi n → "Fan" (giữ đủ a và n; tiền lệ h3 899 thêm "n"). Audit ghi giữ "phù" ("bỏ đuôi ん được chấp nhận theo tiền lệ h4") — lật: tiền lệ đó chỉ cho bỏ ん, không cho đổi a→u.

### §3.3 Romaji — họ くぁ/くあ/くぅ/くっ/んきゅ

**Key 772 (双鉄)**
- JP: `「くっ――ぁっ――」`
- TW: `「呃——啊——」`
- VN cũ: `「Ư——a——」`
- Sửa: `「Ku——a——」`
- Lý do: くっ có phụ âm k thật — "Ư" làm mất hẳn. Tiền lệ h3 906 (くっ→"Ku", parent giữ khi merge, cờ đợt thống nhất). Cờ: doc sfx ghi くっ→"Hự"/"Ư" — xem F3.

**Key 801 (双鉄)**
- JP: `「くぅ――ぁっ」`
- TW: `「唔——啊」`
- VN cũ: `「Ư——a」`
- Sửa: `「Kuu——a」`
- Lý do: くぅ = ku + 1ぅ = 2 u — "Ư" mất k, "Kuu" giữ đủ phụ âm + độ dài.

**Key 805 (ポーレット)**
- JP: `「やふっ――ふあっ！！？　んっ――そうてつ、くっ―― あっ！　いまっ――うごいた、らっ――んきゅんっ！！」`
- TW: `「啊——呼啊！！？嗯——雙鐵——啊！現在——要是動起來——嗯啊！！」`
- VN cũ: `「Á——phù!!? Ưm——Anh Soutetsu, ư—— A! Bây giờ——mà cử động, thì——ưm!!」`
- Sửa: `「Yafu——Fua!!? Ưm——Anh Soutetsu, ư—— A! Bây giờ——mà cử động, thì——Nkyun!!」`
- Lý do: 3 token cùng dòng — やふっ → "Yafu" (ghép ya+fu, mẫu Kyafu/Hyafu; VN cũ "Á" mất cả ya lẫn fu); ふあっ→"Fua"; んきゅんっ→"Nkyun" (xem 868).

**Key 806 (双鉄)**
- JP: `「くあっ――あっ――あっ」`
- TW: `「啊——啊——啊」`
- VN cũ: `「Ư a——a——a」`
- Sửa: `「Kua——a——a」`
- Lý do: くあっ → "Ư a" mất phụ âm k. Tiền lệ h9 2101 (くああ→"Kuaa", parent giữ: "JP くああ có く, JP thắng TW") và lr_ふかみh1 giữ "Kua" cho くあっ. Đây chính là dòng 806 mà audit viện làm tiền lệ cho quyết định "くぁ/くあ→Ư a" — lật quyết định đó theo quy tắc romaji.

**Key 836 (ポーレット)**
- JP: `「んうっ――ぷあっ！　あっ――んきゅっ！ きゃ、ふうううううぅぅぅぅぅぅぅぅぅぅっ！！」`
- TW: `「嗯——呼啊！啊——嗯！呀啊啊啊啊！！」`
- VN cũ: `「Ưm——phù! A——ưm! Kya, phuuuuuuuuuuu!!」`
- Sửa: `「Ưm ư——Pua! A——Nkyu! Kya, Fuuuuuuuuuuuuuuuu!!」`
- Lý do: 4 token cùng dòng — んうっ→"Ưm ư" (2 mora); ぷあっ→"Pua"; んきゅっ→"Nkyu"; きゃ、ふうううううぅぅぅぅぅぅぅぅぅぅっ = ふ + 5う + 10ぅ = 16 u — VN cũ "phuuuuuuuuuuu" chỉ 11 u, thiếu 5 → romaji "F" + 16 u (đếm bằng máy).

**Key 868 (ポーレット)**
- JP: `「んきゅっっ――うっ――い、いっ――おっぱいっ―― もっ――こしゅんって、こす、れて――きもち、いいっ」`
- TW: `「嗯啊——啊——好——胸部——也被蹭到——好舒服——」`
- VN cũ: `「Ư a——ư——sướng, quá——ngực—— cũng——bị cọ, xát——sướng, quá」`
- Sửa: `「Nkyu——ư——sướng, quá——ngực—— cũng——bị cọ, xát——sướng, quá」`
- Lý do: Xây trên giá trị audit (chỉ đổi token đầu). んきゅ → "Nkyu": quy tắc 21/11 cho んひゅ→"Nhyu" suy rộng sang んきゅ (cùng cấu trúc mũi + mora khẩu cái); tiền lệ 凪h2 2395 "Nkyu" (đã merge). "Ưm" của audit làm mất cả mora きゅ. Xem F2.

### §3.4 Romaji — các âm lẻ khác

**Key 792 (双鉄)**
- JP: `「うぁっ――」`
- TW: `「哇——」`
- VN cũ: `「Oa——」`
- Sửa: `「Wa——」`
- Lý do: うぁっ = "wa" — "Oa" là cách đọc Việt cũ. Tiền lệ h3 955 (うぁっ→"Wa", đã merge). TW 哇 ủng hộ.

**Key 1348 (monologue)**
- JP: `かはっ、と荒い息を吐き、 ポーレットがいやいやと首を振る。`
- TW: `波萊特喘著粗氣，同時搖起頭來。`
- VN cũ: `Hà, thở ra một hơi gấp gáp, Paulette lắc đầu nguầy nguậy.`
- Sửa: `Kaha, thở ra một hơi gấp gáp, Paulette lắc đầu nguầy nguậy.`
- Lý do: かはっ có phụ âm ka — "Hà" làm mất ka. Cờ h3 1573 cùng mẫu (かはっ→"A!" mất "ka"). Romaji "Kaha" giữ đủ âm.

**Key 1561 (双鉄)**
- JP: `（ああ……）`
- TW: `（噢……）`
- VN cũ: `（A a……）`
- Sửa: `（Aa……）`
- Lý do: ああ (2 a) bị tách thành "A a" — gộp thành một cách diễn "Aa" (cùng tiền lệ gộp mảnh rời như 854).

### §3.5 Đếm nguyên âm

**Key 778 (ポーレット)**
- JP: `「ハッ――ぁっ――んっ――んううっ！」`
- TW: `「呼——啊——嗯——嗯！」`
- VN cũ: `「Hà——a——ưm——ưm ư!」`
- Sửa: `「Hà——a——ưm——ưm ư ư!」`
- Lý do: んううっ = 3 mora (ん+う+う) — "ưm ư" chỉ 2 âm, thiếu 1 → "ưm ư ư". Tiền lệ nội file 871 (んううっ→"Ưm ư ư", đã đúng).

**Key 789 (双鉄)**
- JP: `「ふっ……ぁあっ」」`
- TW: `「呼……啊」`
- VN cũ: `「Phù……a」」`
- Sửa: `「Phù……Aa」`
- Lý do: ぁあっ = 2 mora a — "a" thiếu 1 → "Aa". Đồng thời gỡ 1 dấu `」` thừa trong VN cũ (JP chỉ có 1 dấu đóng; lỗi đánh máy, TOML cũng có).

**Key 840 (ポーレット)**
- JP: `「んっ――ちゅっ――じゅるっ――じゅううっ―― あっ――んうっ――んっ――ちゅるっ――ちゅっ――」`
- TW: `「嗯——啾——啾嚕——啾噗——啊——嗯——嗯——啾嚕——啾噗」`
- VN cũ: `「Ưm——chụt——sụt——chụtttt—— A——ưm——ưm——chu——chụt——」`
- Sửa: `「Ưm——chụt——sụt——chụtttt—— A——ưm ư——ưm——chụt——chụt——」`
- Lý do: Xây trên giá trị audit (audit sửa "chu"→"chụt" ở cuối). んうっ (2 mora) → "ưm ư".

**Key 842 (ポーレット)**
- JP: `「んうっ――んっ――ちゅっ――ちゅうっ――ちゅむっ ――ちゅるっ――んっ――しゅ、き――らい、しゅきい」`
- TW: `「嗯——嗯——啾——啾——啾嚕————啾嚕——嗯——我喜歡——我好愛你」`
- VN cũ: `「Ưm——ưm——chụt——chụt——chụt ——chụt——ưm——thích, quá——yêu, quá đi」`
- Sửa: `「Ưm ư——ưm——chụt——chụt——chụt ——chụt——ưm——thích, quá——yêu, quá đi」`
- Lý do: んうっ đầu dòng (2 mora) → "Ưm ư". Token んっ thứ hai → "ưm" giữ nguyên.

**Key 870 (ポーレット)**
- JP: `「んうっ！！」`
- TW: `「嗯啊！！」`
- VN cũ: `「Ưm!!」`
- Sửa: `「Ưm ư!!」`
- Lý do: んうっ (2 mora) — "Ưm" thiếu 1 âm. TW 嗯啊 (2 âm) ủng hộ.

### §3.6 Sai âm

**Key 916 (ポーレット)**
- JP: `「はい……んっ――しょっ――んっ――ふっ――ふぅっ」`
- TW: `「是啊……嘿——咻——嗯——呼——呼」`
- VN cũ: `「Vâng……ưm——hự——ưm——phù——phù」`
- Sửa: `「Vâng……ưm——Sho——ưm——phù——Phùu」`
- Lý do: しょっ = "sho" — "hự" là cách diễn của くっ/ぐっ (grunt), sai hẳn phụ âm. Romaji "Sho". ふぅっ = 2 u — "phù" thiếu 1 → "Phùu" (tiền lệ lr-h2 1800: ふうっ→"Phùu!").

**Key 1600 (monologue)**
- JP: `（ぐりっ！　ゆさっ――ぐっ――ぐいいっ――むりゅっ）`
- TW: `（用力頂入）`
- VN cũ: `（Thọc mạnh! Lắc——ưm——mạnh——nhóp nhép）`
- Sửa: `（Thọc mạnh! Lắc——hự——mạnh——nhóp nhép）`
- Lý do: ぐっ → "ưm" làm mất hẳn âm g (ưm là cách diễn của ん). "Hự" là cách diễn grunt Việt theo doc (くっ→"Hự"), khớp 851 cùng file (くっ→"hự"). Dòng này vẫn giữ dạng nghĩa Việt của cả chuỗi, chỉ sửa đúng token grunt.

## §4. Hủy fix audit (giữ VN cũ) — KHÔNG đưa vào wrong.json, cờ cho đợt thống nhất

4 fix audit bị lật (fix moan = VN cũ, không thay đổi gì so với TOML hiện tại). Audit làm ngày 19/11, TRƯỚC quy tắc romaji (21/11) — audit đã Việt hoá các rên romaji vốn đã đúng:

- **768** (ポーレット): JP `きゅぅぅぅぅぅぅぅぅぅん` (10 u). VN cũ `「Kyuuuuuuuuuun!!!」` (đếm đúng 10 u). Audit sửa → `「Kíuuuuuuuuun!!!」` (Việt hoá). HỦY fix audit, giữ VN cũ "Kyuuuuuuuuun" — rên dài nhiều nguyên âm phải dùng romaji theo quy tắc 21/11 (tiền lệ h8 2132 "Hyu"+15a).
- **800** (双鉄): JP `くぁ――あっ――`. VN cũ `「Kua——a——」`. Audit sửa → `「Ư a——a——」`. HỦY fix audit, giữ "Kua" (xem 806).
- **818** (双鉄): JP `くあっ！！！`. VN cũ `「Kua!!!」`. Audit sửa → `「Ư a!!!」`. HỦY fix audit, giữ "Kua" (xem 806).
- **869** (ポーレット): JP `んきゅんっ！`. VN cũ `「Nkyun!」`. Audit sửa → `「Ưm!」` (kind "romanised" — audit coi romaji là lỗi). HỦY fix audit, giữ "Nkyun!" (xem 868).

## §5. Dòng rên giữ nguyên (ghi chú đáng kể)

- **Gasp Ư khóa (không đụng):** 771 `っ――`→"Ư——", 774, 814, 816, 817, 819 (sweep/audit), 1271 (2 Ư), 1290, 1377; phần gasp trong 784, 790, 850 (Ư của audit/sweep giữ nguyên trong fix value). Không có dòng "Kh" nào trong file — không đổi dòng "Kh" nào.
- **Already-rendered 833:** phần gasp đã diễn ("ư", "ư a", "ưm～～") giữ nguyên; chỉ đổi token fa (xem §3.2).
- **Hơi ngắn ふっ/ぷっ → "phù" giữ:** 775 (ふっ), 784, 845, 847, 848, 856, 859 (ぷっ), 916 (ふっ) — hơi thở ngắn đúng âm u.
- **Fa tách giữ dạng audit trong file:** 786 `ふっ――あっっ`→"phù——a", 790 `フ、ァッ`→"Phù, a!" — xem F4.
- **ひゃ→"Hya" giữ:** 796 ひゃっ; 762 chỉ đổi vì thêm n.
- **Họ ちゅ → "chụt" giữ (quy tắc audit của file):** 802, 808, 842, 873 (ちゅっ/ちゅう/ちゅるっ/ちゅむっ) — xem F5 (độ dài ちゅううっ chưa quyết).
- **ん + phụ âm tắc → "ưm" giữ:** 859 んくっ→"ưm" (mũi hấp thụ phụ âm tắc; tiền lệ h3 924 むぷっ→"Ưm"); 805 んっ→"ưm".
- **Nói ngọng giữ (không phải rên):** 784 わらひ→"ehm" (audit), 835 ひっへふははひ→"Hí-hề-phù-ha-ha-hí" + ほーへふ→"Hôu-hê-hu" (audit), 858 れへ……まふ……へ (nói ngọng, audit đã duyệt).
- **SFX độc thoại （ ） giữ dạng nghĩa Việt:** 1541–1617 (trừ 1586 audit "Phập" và 1600 đổi "hự") — xem F6.
- **Khác giữ:** 793 うぉっ→"Uây!" (thán từ Việt, xem F10); 952 くぅん trong tên gọi (âm kéo dài trong tên, không diễn); 760 あ～～～→"a～～～"; 773 ぅ、ぁっ→"Ư, a!"; 803 ぅっ→"Ư——"; 813 ぁっ→"A——"; 871 んううっ→"Ưm ư ư!" (tiền lệ đếm cho các dòng んうっ); 884 ぉっ→"Ồ"; 725/741/864/905 んっ→"ưm"; 1566/1577 きゅううううううっ→"Siết chặt" (nghĩa, audit đã duyệt); 1268 きゅうん→"siết chặt" (nghĩa, trong độc thoại).

## §6. Rà soát sweep gasp

- Sweep có 11 mục trong file này (đã kiểm chứng trực tiếp, khớp ghi nhận của audit):
  - 10 fix gasp Ư (774, 784, 790, 814, 816, 817, 819, 1271, 1290, 1377): không đụng dòng nào — các fix moan ở 784/790 chỉ giữ nguyên phần Ư của audit/sweep trong fix value (815/850 xây trên giá trị audit).
  - 1 already-rendered (833): không đụng phần gasp; chỉ đổi token fa ふあっ→"Fua".
- Audit phát hiện thêm 2 dòng gasp sweep bỏ sót (815, 850) — đã có trong fix audit; moan không sửa trùng.
- Không dòng "Kh" nào bị đổi.

## §7. Lượt soát 2 (second pass)

- Đọc lại toàn bộ 35/35 fix đối chiếu JP (+TW): **tổng 35 / tái kiểm chứng 35 / bỏ 0 / sửa 0**.
- Kiểm tra bằng máy: JSON 35 mục, khóa string; jp/tw/old_vn khớp CSV3 35/35; fix nào cũng khác VN cũ đúng ở token rên nhắm tới (không có no-op, không có `\n` trong fix).
- Đếm nguyên âm kiểm chứng độc lập bằng máy: 768 (10 u — VN cũ đã đúng, xem F1), 836 (ふ+5う+10ぅ = 16 u → "F"+16u), 778 (3 mora), 870/815/840/842 (んうっ 2 mora), 775/788 (はぁ 2 a), 854 (あああ 3 a), 1561 (ああ 2 a), 789/766 (ぁあ 2 a), 801 (くぅ 2 u), 916 (ふぅ 2 u), 838 (ぷぁぁ 2 a).
- Khối TOML parse bằng tomllib: 35 khóa, 0 sai lệch giá trị so với wrong.json.
- Các fix xây trên giá trị audit (chỉ đổi đúng token rên, giữ phần còn lại của audit): 770 (= audit), 815, 840, 850, 868. Các fix lật giá trị audit: 806, 944 (+ 4 hủy ở §4). Các fix mới so với audit: 762, 764, 766, 767, 772, 775, 777, 778, 788, 789, 792, 796, 801, 805, 807, 833, 836, 838, 842, 853, 854, 859, 870, 916, 1348, 1561, 1600 (27 dòng audit bỏ sót).

## §8. Cờ cho đợt thống nhất (không quyết)

- **F1 — HỦY 4 fix audit, giữ VN cũ (xem §4):** 768 ("Kíuuuuuuuuun" → giữ "Kyuuuuuuuuun"), 800/818 ("Ư a" → giữ "Kua"), 869 ("Ưm" → giữ "Nkyun!"). Áp giá trị moan, không áp fix audit cùng key.
- **F2 — んきゅ → "Nkyu"/"Nkyun" (805, 836, 868) vs audit "Ưm" (tiền lệ h4):** cần quyết một dạng toàn dự án (romaji Nkyu hay "Ưm"). Cùng câu hỏi cho んくっ (859 giữ "ưm").
- **F3 — くっ:** 772 đổi "Ư"→"Ku" (tiền lệ h3 906) vs 851 giữ "Hự" (doc sfx) vs doc "Ư" — cần một dạng thống nhất cho くっ độc lập.
- **F4 — fa tách (ふ、ぁ / ふ――あ):** file này giữ "phù, a"/"phù——a" (786, 790) theo tiền lệ audit trong file + h7 đã merge (11 dòng giữ) — NGƯỢC với h9 đã merge (đổi sang romaji "Fu, a"/"Fu——a", 7 dòng). Cần quyết một dạng duy nhất toàn dự án. Cùng câu hỏi: hơi thở mềm ふぁ cuối dòng (788 đổi "Fa") có nên giữ "phù" không.
- **F5 — họ ちゅう(っ):** file này giữ "chụt" (808, 830, 835, 840, 873; quy tắc audit) vs h3 đã merge "chụụụt"/"chụụt" (đếm nguyên âm: 835 ちゅう×9 → "Chụ"+9ụ+"t"?). Cần quyết: "chụt" hay đếm nguyên âm.
- **F6 — SFX độc thoại （ ） chưa áp công thức đếm nguyên âm** (cờ đứng như h9/h3): 1541 ずぬ――うううっ → "Phậppppppp" (3 u kéo bằng p); 1543 みゅにぃ×11 → "Múttttttttttt" (12 i kéo bằng t); 1552/1558/1560 びゅううっ → "Phụt"/"Phụtttt"; 1597 ぬとおおおおおっ (5 o) → "Nhễ nhạiiiiii" (6 i, sai cả âm lẫn đếm).
- **F7 — んうっ → "ưm ư" (778, 815, 836, 840, 842, 870):** TW diễn 1 âm 嗯 ở 815/840/842 nhưng 2 âm 嗯啊 ở 870; tiền lệ nội file 871 (3 âm cho 3 mora) + công thức ủng hộ 2 âm. Parent rà lại khi merge.
- **F8 — phán đoán moan mới, chưa có tiền lệ merge trực tiếp:** 916 しょっ→"Sho", 1348 かはっ→"Kaha" (chỉ có cờ h3 1573 cùng mẫu).
- **F9 — 789:** dấu `」` thừa trong VN cũ đã gỡ trong fix moan; ghi nhận để đợt thống nhất kiểm tra TOML.
- **F10 — 793 うぉっ→"Uây!" giữ:** thán từ Việt cho tiếng ngạc nhiên "wo" — ghi nhận, không đổi (nếu muốn thống nhất romaji "Wo!" thì quyết ở đợt thống nhất).

## §9. Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
[script]
762 = "「Hyan——gì vậy——thế này——」"
764 = "「Ya……nóng……quá——của anh, Soutetsu—— Dương, vật——」"
766 = "「Ya……thế này——hà——Aa——cảm giác này—— em không, biết——ưm——sướng——quá——」"
767 = "「An」"
769 = "「Kyafu!!!」"
770 = "「Hyafu!!?」"
772 = "「Ku——a——」"
775 = "「Phù——Fa——ưm——hàà——sướng quá—— âm đạo——đang——siết chặt——lắm!」"
777 = "「Hà——a——ưm——chụt——Pua——ưm, Fua——a——ưm!!!」"
778 = "「Hà——a——ưm——ưm ư ư!」"
788 = "「Hàà……a——anh Soutetsu……ngón tay…… Dâm đãng——quá……Fa」"
789 = "「Phù……Aa」"
792 = "「Wa——」"
796 = "「Hả!? Kya!? Hya!!」"
801 = "「Kuu——a」"
805 = "「Yafu——Fua!!? Ưm——Anh Soutetsu, ư—— A! Bây giờ——mà cử động, thì——Nkyun!!」"
806 = "「Kua——a——a」"
807 = "「A——ưm——ưm——Fua——a!!!」"
815 = "「Ư! Fua! A——ưm ư——chụt!」"
833 = "「Ưm——Fua——a——To quá—— ư——đầu, nấm——ư a——ưm～～!!!」"
836 = "「Ưm ư——Pua! A——Nkyu! Kya, Fuuuuuuuuuuuuuuuu!!」"
838 = "「Ưm――――ưm――――ực! Ưm——ực ——A——Fa——a……Puaa」"
840 = "「Ưm——chụt——sụt——chụtttt—— A——ưm ư——ưm——chụt——chụt——」"
842 = "「Ưm ư——ưm——chụt——chụt——chụt ——chụt——ưm——thích, quá——yêu, quá đi」"
850 = "「Ưm……Fa……——Hôu-hê-hu……hừm……ưm—— Chụt——chụt——liếmmmmƯ——Ư——」"
853 = "「Ưm……chụt——chụt——ưm——thích, lắm—— Ưm——Pua——a. Em thích. Thích anh. Anh Soutetsu.」"
854 = "「Ưm……chụt——ưm……Fua——Pua! A! A——Aaa!!」"
859 = "「Ưm……phù——ưm――――Pua! A……」"
868 = "「Nkyu——ư——sướng, quá——ngực—— cũng——bị cọ, xát——sướng, quá」"
870 = "「Ưm ư!!」"
916 = "「Vâng……ưm——Sho——ưm——phù——Phùu」"
944 = "「Thế, này……thế này……ưm——Sâu——quá——Fan!」"
1348 = "Kaha, thở ra một hơi gấp gáp, Paulette lắc đầu nguầy nguậy."
1561 = "（Aa……）"
1600 = "（Thọc mạnh! Lắc——hự——mạnh——nhóp nhép）"
```

## Kết bài

- h6 moan: đổi 35/304 dòng (11,5% file; 35/193 dòng rên ứng viên) — romaji 28, đếm nguyên âm 5, sai âm 2. Ngoài ra 4 fix audit bị đề nghị HỦY (giữ VN cũ — xem §4, không tính vào 35).
- Lỗi chủ đạo: họ fa/fu bị diễn "phù" mất âm a (12 dòng); mất phụ âm mora trong "Á"/"Ư" (や/きゃ/ひゃん/あんっ/くぁ/んきゅ/かは — 11 dòng); đếm nguyên âm thiếu (んうっ, はぁ, ふぅっ, ぁあっ, ああ tách mảnh).
- Khối TOML 35 key đã parse đúng (tomllib, 0 sai lệch); JSON 35 mục khóa string, jp/tw/old_vn khớp CSV3 35/35.
- Lượt soát 2: 35/35 tái kiểm chứng, 0 bỏ, 0 sửa. Sweep 11 mục đã kiểm chứng, không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào.
- 10 cờ cho đợt thống nhất (F1–F10), trong đó quan trọng nhất: F1 (hủy 4 fix audit), F2 (んきゅ Nkyu vs "Ưm"), F4 (fa tách "phù, a" vs "Fu, a"), F5 (ちゅう "chụt" vs đếm nguyên âm).
