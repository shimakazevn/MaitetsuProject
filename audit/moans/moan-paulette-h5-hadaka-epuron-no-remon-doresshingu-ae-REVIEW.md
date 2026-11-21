# Moan-fix REVIEW — ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml

- File: `ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml` — route 03_Paulette, 305 dòng script.
- TOML md5: `ba0e02364d99fd8aa8f08daea04428b2` (khớp md5 audit), không có bản trùng trong 227 file TOML (đã kiểm lại bằng md5 toàn bộ; cùng basename cũng không có ở thư mục khác).
- CSV3: 1 bộ duy nhất (thư mục `03_Paulette`), 305 dòng, 0 key trùng. VN khớp TOML 305/305 sau chuẩn hoá `\n`→khoảng trắng (197 khác thô, toàn là TOML-2 làm phẳng `\n` — như audit đã ghi). 1 khác biệt duy nhất ngoài `\n`: key 1231 — TOML escape `\"` trong khi CSV3 để `"` trần (khác biệt escape, không phải nội dung; không phải dòng rên, xem cờ F8).
- Audit trước đó: 30 lỗi (audit-paulette-h5-apron-lemon-dressing), trong đó 18 dòng có fix liên quan rên/SFX/gasp — xem §4 (2 fix audit bị HỦY, 4 fix audit bị lật/kế thừa có chỉnh, còn lại giữ nguyên).
- Quy ước fix: một dòng (khoảng trắng thay `\n`), theo quy ước audit của chính file này (TOML gốc lưu một dòng; audit 18/18 fix đa dòng đều làm phẳng).
- Sweep っ: 5 mục cho file này trong sweep-raw-gasp-wrong.json — 904/905/953 (raw-tsu), 935 (lost-gasp-whole), 1228 (lost-gasp-trailing). Cả 5 đã được audit sửa đúng thành Ư (`「Ư!」`, `「Ư!!!」`, `——Ư!`); moan pass KHÔNG đụng vào dòng gasp Ư nào. File không có token "Kh" độc lập nào — không dòng "Kh" nào bị đổi.

## §1. Kiểm kê rên (moan inventory)

- Đã đọc 305/305 dòng (CSV3 + TOML).
- 202 dòng rên/SFX ứng viên theo mẫu quét (JP chứa âm rên/thở/gasp/SFX — bao gồm cả ngắt câu っ trong thoại thường); trong đó 33 dòng SFX độc thoại （ ）.
- Sửa 36, giữ 166.
- Phân loại 36 dòng sửa: romaji 27, đếm nguyên âm 6, romaji + đếm nguyên âm 3.
- Lỗi chủ đạo: (1) họ fa/fu bị diễn "phù"/"Phù" mất hẳn âm a của ふあ/ふぁ/ぷあ (15 dòng, 17 token); (2) mất phụ âm mora trong "Á"/"Ư" (や/やぁ/きゃ/くっ/んきゅ/きゅ/あんっ/ひゅい — 16 dòng); (3) đếm nguyên âm thiếu — rên dài nhiều mora bị gộp thành 1 âm (んううっ, んうぅっ, んーむっ, んんっ, ふぅんっ, ふあ dài 891; cộng ふうっ trong 855/856 và んんっ trong 870).

## §2. Danh sách sửa (36 dòng)

### 846 — んんっ → "ưm ưm" [vowel-count]
- JP: `「け……ど――それ、でも――ボウ、ル――\nボウ、ルっ――きっと――汚しちゃ――んんっ！」`
- TW: `「可以……這樣——碗就一定——會弄髒了——嗯——！」`
- Cũ: `「Nhưng……mà——dù, vậy——cái, thau——\nCái, thau——chắc chắn——sẽ bị bẩn——ưm!」`
- Mới: `「Nhưng……mà——dù, vậy——cái, thau—— Cái, thau——chắc chắn——sẽ bị bẩn——ưm ưm!」`
- Lý do: んんっ = 2 mora ん — "ưm" chỉ diễn 1 nhịp, mất 1 âm (tiền lệ moan 凪h2 đã sửa mất độ dài んんんっ → 3 nhịp; "đừng để mất âm").

### 848 — やっ→"Ya", ふあっ→"Fua" [romaji]
- JP: `「やっ――ふっ――ふあっ――あっ！　おまん、こっ――\nとけるっ――ぺろぺろ、され、て――とろけ、ちゃうっ」`
- TW: `「呀——呼——呼啊——啊！小穴——要化了——被舔到——要化了」`
- Cũ: `「Á——phù——phù——a! Cô bé——\nTan chảy——bị, liếm láp——sắp tan chảy, mất rồi」`
- Mới: `「Ya——phù——Fua——a! Cô bé—— Tan chảy——bị, liếm láp——sắp tan chảy, mất rồi」`
- Lý do: やっ→"Á" mất phụ âm y (tiền lệ h3: "'Á' cho きゃっ/ひゃっ/やっ" là lỗi mất âm); ふあっ→"phù" mất âm a.

### 849 — んううっ → "ưm ư ư" [vowel-count]
- JP: `「ひゃっ――あっ――焦らし、ちゃ――\nやぁ――ですっ――んううっ――あっ！」`
- TW: `「呀——啊——不要——挑逗啦——嗯——啊！」`
- Cũ: `「Hya——a——đừng trêu chọc, em——\nNữa——mà——ưm——a!」`
- Mới: `「Hya——a——đừng trêu chọc, em—— Nữa——mà——ưm ư ư——a!」`
- Lý do: んううっ = ん+う+う = 3 nhịp — "ưm" chỉ diễn 1 (tiền lệ h6 778 んううっ→"ưm ư ư"). やぁ→"Nữa" là diễn nghĩa (やぁです = "thôi đi mà") — giữ.

### 854 — くっ→"Ku", やっ→"Ya", ふあっ→"Fua" [romaji]
- JP: `「ひゃきゅ！　くっ――んっ――やっ――優し、ふあっ！\n――きもち、い――キス、キスっ――双鉄、くん、の！」`
- TW: `「呀！唔——嗯——雙鐵君的吻——好溫柔——呼啊！好舒服！」`
- Cũ: `「Hyakyu! Ư——ưm——á——thật dịu dàng, phù!\n——Sướng, quá——hôn, nụ hôn——của anh, Soutetsu!」`
- Mới: `「Hyakyu! Ku——ưm——Ya——thật dịu dàng, Fua! ——Sướng, quá——hôn, nụ hôn——của anh, Soutetsu!」`
- Lý do: くっ→"Ư" mất hẳn phụ âm k (tiền lệ h6 772 くっ→"Ku"); やっ→"á" mất y; ふあっ→"phù" mất a. ひゃきゅ→"Hyakyu" đã đúng — giữ.

### 855 — ふうっ→"Phùù", ふあっ→"Fua" [romaji+vowel-count]
- JP: `「ひゃっ！　あっ――んっ――ふうっ――ふあっ！」`
- TW: `「呀！啊——嗯——呼——呼啊！」`
- Cũ: `「Hya! A——ưm——phù——phù!」`
- Mới: `「Hya! A——ưm——Phùù——Fua!」`
- Lý do: ふうっ = ふ+う+っ = 2 u — "phù" thiếu 1 (tiền lệ lr-h2 1800 ふうっ→"Phùu"); ふあっ→"phù" mất a.

### 856 — や→"Ya", きゅっ→"Kyu", ふうっ→"Phùù" [romaji+vowel-count]
- JP: `「や！　あっ――やわらかっ――んっ――んあっ！\nぬめっ、って――あったか――ふっ、きゅっ――ふうっ」`
- TW: `「呀！啊――軟軟的——嗯——嗯！滑滑的——熱熱的——呼——呼啊」`
- Cũ: `「Á! A——mềm quá——ưm——ưm a!\nTrơn tuột——ấm quá——phù, siết——phù」`
- Mới: `「Ya! A——mềm quá——ưm——ưm a! Trơn tuột——ấm quá——phù, Kyu——Phùù」`
- Lý do: や→"Á" mất y; きゅっ là tiếng rít "kyu" — "siết" (siết chặt) là bịa nghĩa cho một âm thanh (JP thắng TW; TW cũng chỉ diễn là 呼 "hơi thở"); ふうっ thiếu 1 u.

### 860 — きゃっ→"Kya" [romaji]
- JP: `「きゃっ！？」`
- TW: `「呀！？」`
- Cũ: `「Á!?」`
- Mới: `「Kya!?」`
- Lý do: quy tắc 3b (21/11): きゃ→romaji "Kya"; "Á" mất phụ âm ky.

### 862 — やあっ→"Yaa", ああっ→"Aa" [romaji]
- JP: `「やあっ！？　『おお』と、かっ――あっ――あっ――あ、\nああっ！」`
- TW: `「呀！？不要感嘆——啊——啊——啊！」`
- Cũ: `「Á!? Đừng có 'ồ'——a——a——a, a á!」`
- Mới: `「Yaa!? Đừng có 'ồ'——a——a——a, a Aa!」`
- Lý do: やあっ = や+あ = 2 a — "Á" mất y và mất 1 a; ああっ = 2 a — "á" chỉ diễn 1 (tiền lệ h6 789 ぁあっ→"Aa").

### 864 — ふあ→"Fa" [romaji]
- JP: `「ひゃっ！？　抜けっ――んっ！　あつ、っ！　ふあ！」`
- TW: `「呀！？拔出去了——嗯！好燙！啊！」`
- Cũ: `「Hya!? Tuột ra——ưm! Nóng, quá! Phù!」`
- Mới: `「Hya!? Tuột ra——ưm! Nóng, quá! Fa!」`
- Lý do: ふあ→"Phù" mất âm a.

### 870 — くっ→"Ku", んんっ→"ưm ưm" [romaji+vowel-count]
- JP: `「ふ、くっ――あっ――はっ――んんっ！\nわ……わ、たし――もれ、そっ――その――おしっ、こ」`
- TW: `「呼——啊——呼——嗯！我…我要——尿出來了」`
- Cũ: `「Phù, ư——a——hà——ưm!\nE……e, em——sắp, són——đó——t, tè」`
- Mới: `「Phù, Ku——a——hà——ưm ưm! E……e, em——sắp, són——đó——t, tè」`
- Lý do: くっ→"ư" mất hẳn k; んんっ = 2 mora ん — "ưm" chỉ diễn 1 nhịp.

### 873 — ふあっ→"Fua" [romaji]
- JP: `「はっ――ぁっ――はい、双鉄、くん――んっ！\n来て――くだ、さ――いっ――ふあっ！！」`
- TW: `「呼——啊——好的，雙鐵君——嗯！來吧——呼啊！！」`
- Cũ: `「Hà——a——vâng, anh Soutetsu——ưm!\nHãy đến——đây, đi——ạ——phù!!」`
- Mới: `「Hà——a——vâng, anh Soutetsu——ưm! Hãy đến——đây, đi——ạ——Fua!!」`
- Lý do: ふあっ→"phù" mất âm a.

### 880 — やっ→"Ya" [romaji]
- JP: `「は……やっ……恥ずか……しぃ……よぉ……は、あ――\nおし、っこ――おしっこ――早く……とまってぇ」`
- TW: `「呼……呀……好羞恥——呼——啊——尿——快停下——」`
- Cũ: `「Hà……á……xấu hổ……quá……anh ơi……hà, a——\nT, tè——đi tè——mau……dừng lại đi」`
- Mới: `「Hà……Ya……xấu hổ……quá……anh ơi……hà, a—— T, tè——đi tè——mau……dừng lại đi」`
- Lý do: やっ→"á" mất phụ âm y.

### 883 — ふあっ→"Fua", くっ→"Ku" [romaji]
- JP: `「は……ぁっ――ンッ――ふあっ――あっ――\nこれ……好きっ――んっ――くっ――ぁ――はぁ」`
- TW: `「呼……啊——嗯——呼啊——啊——我喜歡……這樣——嗯——唔——啊——呼啊」`
- Cũ: `「Hà……a——ưm——phù——a——\nThế này……thích lắm——ưm——ư——a——hà」`
- Mới: `「Hà……a——ưm——Fua——a—— Thế này……thích lắm——ưm——Ku——a——hà」`
- Lý do: ふあっ→"phù" mất a; くっ→"ư" mất k.

### 884 — ふぁ→"Fa" [romaji]
- JP: `「は……ぁ……んっ――ふぅ……ふぅ……ふぁ」`
- TW: `「呼……啊……嗯——呼……呼……呼啊」`
- Cũ: `「Hà……a……ưm——phù……phù……phù」`
- Mới: `「Hà……a……ưm——phù……phù……Fa」`
- Lý do: ふぁ cuối dòng → "phù" mất âm a (TW 呼啊 xác nhận có âm a).

### 886 — ふあっ→"Fua" ×2, くっ→"Ku", あんっ→"An" [romaji]
- JP: `「ふあっ――あっ――双鉄、くんっ――んっ――\nあっっ――くっ――ふあっ――あっ――あんっ」`
- TW: `「呼啊——啊——雙鐵君——嗯——啊——呃——呼啊——啊——嗯」`
- Cũ: `「Phù——a——anh Soutetsu——ưm——\nA——ư——phù——a——a」`
- Mới: `「Fua——a——anh Soutetsu——ưm—— A——Ku——Fua——a——An」`
- Lý do: cả 2 lần ふあっ đều → "phù" mất a (âm "a" sau đó là của あっ kế tiếp, không phải của ふあっ); くっ→"ư" mất k; あんっ = a+ん — "a" mất ん (tiền lệ h6 767 あんっ→"An").

### 888 — ぷあっ→"Pua" [romaji]
- JP: `「ぷあっ――あっ……ポーレット」`
- TW: `「呼啊——啊……波萊特」`
- Cũ: `「Phù——a……Paulette」`
- Mới: `「Pua——a……Paulette」`
- Lý do: ぷあっ→"phù" mất a (âm "a" sau đó là của あっ kế tiếp). Soutetsu nói — romaji "Pua" theo tiền lệ h6 777 ぷあっ→"Pua".

### 890 — ふぁ→"Fa" [romaji]
- JP: `「ふぁ……コート……され、てる――ンッ――\nわたし、双鉄、くん――ホワイト、ソース――でっ――」`
- TW: `「呼啊……我被淋上醬料了——嗯——雙鐵君——你的白汁——把我澆了一遍」`
- Cũ: `「Phù……bị……phủ lên, rồi——ưm——\nEm, bị anh Soutetsu——phủ bằng nước xốt, trắng——rồi——」`
- Mới: `「Fa……bị……phủ lên, rồi——ưm—— Em, bị anh Soutetsu——phủ bằng nước xốt, trắng——rồi——」`
- Lý do: ふぁ→"Phù" mất âm a (TW 呼啊).

### 891 — đếm nguyên âm: 22 a → 17 a [vowel-count]
- JP: `「ふぁぁぁぁぁぁぁぁぁっぁぁぁぁぁぁぁぁっ！！！」`
- TW: `「呼啊啊啊啊啊啊！！！」`
- Cũ: `「Phuaaaaaaaaaaaaaaaaaaaaaa!!!」`
- Mới: `「Phuaaaaaaaaa—Aaaaaaaa!!!」`
- Lý do: đếm máy: JP có 17 âm a — đoạn 1 (trước っ đầu) 9 a, đoạn 2 (giữa 2 dấu っ) 8 a; VN cũ có 22 a (thừa 5). Dấu っ giữa rên dài diễn bằng "——" (quy ước ngắt câu của file), っ cuối diễn bằng "!!!". Mới: "Phu"+9 a, "—", "A"+7 a (= 8 a) — tổng 17 a.

### 892 — lật fix audit "Siết" → khôi phục romaji "Kyuuuuuuuuu" [romaji]
- JP: `「ふっ――きゅううううううううっっ！！！」`
- TW: `「呼啊啊啊啊！！！」`
- Cũ (CSV3): `「Phù——kyuuuuuuuuu!!!」`
- Mới: `「Phù——Kyuuuuuuuuu!!!」`
- Lý do: VN cũ đã là romaji đúng (9 u = 1+8 theo công thức); audit đổi thành "Siếttttttttt" — bịa nghĩa "siết chặt" cho một âm thanh thuần túy (きゅううう là tiếng rít dài, TW cũng chỉ diễn là 呼啊). Khôi phục romaji, viết hoa K theo quy ước romaji của file (tiền lệ h6 768 "Kyuuuuuuuuun" giữ nguyên). Chỉ khác VN cũ ở chữ hoa K.

### 893 — ぷあっ→"Pua" [romaji]
- JP: `「ぷあっ！」`
- TW: `「呼啊！」`
- Cũ: `「Phù!」`
- Mới: `「Pua!」`
- Lý do: ぷあっ→"Phù" mất âm a (Soutetsu thở ra; tiền lệ h6 777 ぷあっ→"Pua").

### 895 — ふあっ→"Fa" [romaji]
- JP: `「ふあっ！　あっ！　あっ！　あっ！　双鉄、くんっ！\nあっ――子宮！　もっと！　叩いて、もっぉ！」`
- TW: `「呼啊！啊！啊！啊！雙鐵君！啊——子宮！再多來！頂一頂！」`
- Cũ: `「Phù! A! A! A! Anh Soutetsu!\nA——tử cung! Nữa đi! Đâm vào, nữa đi!」`
- Mới: `「Fa! A! A! A! Anh Soutetsu! A——tử cung! Nữa đi! Đâm vào, nữa đi!」`
- Lý do: ふあっ→"Phù" mất âm a.

### 906 — ふあっ→"Fua" ×2 [romaji]
- JP: `「かっ――ふあっ――おな、か――おまん、こっ――\nんっ――これ――すご――えぐれ――てっ――ふあっ！」`
- TW: `「啊——呼啊——肚子——小穴裡——嗯——這樣——好厲害——被挖到了——呼啊！」`
- Cũ: `「A——phù——bụng——cô bé——\nƯm——thế này——tuyệt quá——bị ngoáy sâu——vào——phù!」`
- Mới: `「A——Fua——bụng——cô bé—— Ưm——thế này——tuyệt quá——bị ngoáy sâu——vào——Fua!」`
- Lý do: cả 2 lần ふあっ đều → "phù" mất a.

### 913 — やっ→"Ya" [romaji]
- JP: `「やっ――あっ――足っ――んっ――ふっ――は、あっ、\nこれっ――だめっ――腰――浮い、て――んうっ！」`
- TW: `「啊——腿——嗯——呼——呼啊——這樣——不行——腰——抬起來了！」`
- Cũ: `「Á——a——chân——ưm——phù——hà, a,\nThế này——không được——hông——nổi lên, rồi——ưm!」`
- Mới: `「Ya——a——chân——ưm——phù——hà, a, Thế này——không được——hông——nổi lên, rồi——ưm!」`
- Lý do: やっ→"Á" mất phụ âm y.

### 915 — ふぅんっ→"Phùù ưm" [vowel-count]
- JP: `「あ……ま、た――ンッ――そんな……あっ――優、しく\n――は、んっ――てい、ねい――にっ――ふぅんっ！」`
- TW: `「啊……又來——嗯——動作好輕——啊——好用心——呼啊！」`
- Cũ: `「A……lại, nữa——ưm——như thế……a——thật, dịu dàng\n——hà, ưm——cẩn, thận——quá——phù ưm!」`
- Mới: `「A……lại, nữa——ưm——như thế……a——thật, dịu dàng ——hà, ưm——cẩn, thận——quá——Phùù ưm!」`
- Lý do: ふぅんっ = ふ+う+ん+っ — ふぅ là 2 u theo công thức (1+1), VN cũ "phù" chỉ có 1 u; ん diễn "ưm" giữ nguyên (tách 2 mảnh theo kiểu diễn của file cho ふぅん).

### 920 — ふぁ→"Fa" [romaji]
- JP: `「あ……ふぁ……あっ……しちゃ……った……おし、っこ。\nわたし……双鉄、くんの――目の、前――――でっ」`
- TW: `「啊……呼……啊……我竟然……在雙鐵君面前……尿出來了——」`
- Cũ: `「A……phù……a……em tè……mất……rồi.\nEm……ngay trước, mặt——anh Soutetsu――――」`
- Mới: `「A……Fa……a……em tè……mất……rồi. Em……ngay trước, mặt——anh Soutetsu――――」`
- Lý do: ふぁ→"phù" mất âm a (TW 呼).

### 921 — やぁ→"Yaa" [romaji]
- JP: `「あ……あっ――あっ……やぁ……やだ……やぁだぁっ」`
- TW: `「啊……啊——啊……呀……討厭……討厭啦」`
- Cũ: `「A……a——a……á……không chịu……không chịu đâu」`
- Mới: `「A……a——a……Yaa……không chịu……không chịu đâu」`
- Lý do: やぁ (gasp độc lập) = や+あ = 2 a — "á" mất y và mất 1 a. やだ/やぁだぁっ diễn nghĩa "không chịu" — giữ (đó là từ, không phải rên thuần).

### 924 — えろぉっ→"Eroo" [romaji]
- JP: `「あ……むっ――んっ――れるっ――えろぉっ――ン\n――ちゅっ――ちゅるっ――はむっ――れるうっ」`
- TW: `「啊……嗯——嗯――啾嚕——啾噗——嗯――啾噗——啾噗――啾嚕——啾噗」`
- Cũ: `「A……ngoạm——ưm——liếm——liếmmmm——ưm\n——Chụt——chụt——ngoạm——liếmmmm」`
- Mới: `「A……ngoạm——ưm——liếm——Eroo——ưm ——Chụt——chụt——ngoạm——liếmmmm」`
- Lý do: えろぉっ = え+ろ+お (2 o) — âm "ero" bị diễn thành "liếmmmm" (trùng với れるっ/れるうっ), mất hẳn âm thanh gốc. Romaji "Eroo" theo quy tắc "đừng để mất âm". ちゅるっ→"chụt" giữ theo cờ F4 (họ ちゅ chờ quyết chung).

### 927 — や→"Ya" [romaji]
- JP: `「あっ、や！　止まら、なっ――ふっ――あ、見ないで！見ないでください、双鉄く、んっ――あっ――んうっ！」`
- TW: `「啊、呀！停不下來——啊——不要看！不要看啦，雙鐵——啊——嗯！」`
- Cũ: `「A, á! Không dừng, được——phù——a, đừng nhìn! Đừng nhìn em mà, anh Soutetsu——a——ưm!」`
- Mới: `「A, Ya! Không dừng, được——phù——a, đừng nhìn! Đừng nhìn em mà, anh Soutetsu——a——ưm!」`
- Lý do: や→"á" mất phụ âm y.

### 938 — んーむっ→"Ưm ưm" [vowel-count]
- JP: `「んーむっ――ちゅ――はむ――ちゅるっ――ちろ、\nちるる――れろっ――れるうっ――」`
- TW: `「嗯——唔——啾嚕——啾嚕——啾噗——啾噗——啾嚕——啾嚕——啾噗——」`
- Cũ: `「Ưm——chụt——ngoạm——chụt——liếm,\nliếm——liếm——liếmmmm——」`
- Mới: `「Ưm ưm——chụt——ngoạm——chụt——liếm, liếm——liếm——liếmmmm——」`
- Lý do: んーむっ = ん (kéo dài) + む = 2 nhịp — "Ưm" chỉ diễn 1, mất mora む.

### 940 — くっ→"Ku", ふあっ→"Fua" [romaji]
- JP: `「ん……くっ――ふあっ――あっ！　ちがっ――\nそこっ！　んっ――やぁ――なの――焦れっ――たい」`
- TW: `「嗯……呼——呼啊——啊！不對——那裡！嗯——討厭——我好心急」`
- Cũ: `「Ưm……ư——phù——a! Không phải——\nChỗ đó! Ưm——ghét——quá——sốt ruột——quá」`
- Mới: `「Ưm……Ku——Fua——a! Không phải—— Chỗ đó! Ưm——ghét——quá——sốt ruột——quá」`
- Lý do: くっ→"ư" mất k; ふあっ→"phù" mất a (âm "a" sau đó là của あっ kế tiếp).

### 942 — ちゅむっ→"chumu" [romaji]
- JP: `「んっ……ちゅっ――ちゅむっ――ちゅうう――ちゅっ\n――ぷ、あっ――ん――れろっ――れるっ――れろおっ」`
- TW: `「嗯……啾——啾嚕——啾啾——啾嚕——呼、啊——嗯——啾嚕——啾嚕——啾噗」`
- Cũ (CSV3): `「Ưm……chụt——chu——chụtttt——chụt\n——Phù, a——ưm——liếm——liếm——liếmmmm」`
- Mới: `「Ưm……chụt——chumu——chụtttt——chụt ——Phù, a——ưm——liếm——liếm——liếmmmm」`
- Lý do: ちゅむっ→"chu" mất hẳn mora む (tiền lệ h3: ちゅむっ→"chumu" romaji; h3 cũng liệt kê "chu cho ちゅむっ/ちゅばっ/ぢゅぶっ" là lỗi mất âm). Giá trị này xây trên VN cũ CSV3 (chỉ đổi đúng token rên), thay thế cả fix audit "chụt" cho cùng token (audit cũng mất む). ちゅうう→"chụtttt" giữ theo cờ F4.

### 949 — くぅんっ→"Kuun" (giữ "Nkyu" của CSV3) [romaji]
- JP: `「んきゅっ！　あっ――双鉄――くぅんっ！　んっ、\nもっと――ふか、くてっ――へい、きっ――わたしっ」`
- TW: `「嗯！啊——雙鐵！嗯——再深一點——我也——沒關係」`
- Cũ (CSV3): `「Nkyu! A——anh Soutetsu! Ưm,\nSâu——hơn nữa——em không, sao——đâu」`
- Mới: `「Nkyu! A——anh Soutetsu! Kuun, Sâu——hơn nữa——em không, sao——đâu」`
- Lý do: くぅんっ = く+う+ん = 2 u — "Ưm" mất hẳn âm ku (tiền lệ h6 805 んきゅんっ→"Nkyun", くぅ→"Kuu"). Đồng thời KHÔI PHỤC "Nkyu" cho んきゅっ: VN cũ đã đúng, audit đổi thành "Ưm!" là lùi (mất ky) — xem §4.

### 958 — ふあっ→"Fua" [romaji]
- JP: `「あ……熱っ、いっ――んっ――ふあっ――あっ――\nおだい、どこっ――エプロ、ん――わた、し――もっ」`
- TW: `「好……好燙啊——嗯——呼啊——啊——廚房——圍裙——還有我——」`
- Cũ: `「A……nóng, quá——ưm——phù——a——\nNhà, bếp——tạp dề, ề——cả, em——nữa」`
- Mới: `「A……nóng, quá——ưm——Fua——a—— Nhà, bếp——tạp dề, ề——cả, em——nữa」`
- Lý do: ふあっ→"phù" mất a (âm "a" sau đó là của あっ kế tiếp).

### 980 — ひゅいっ→"Hyui" (sửa chính tả romaji) [romaji]
- JP: `「わか、るつ――ぷくっ、て！　双鉄、くん――の――\nおちん――ひゅいっ！　あっ――おちん、ちんぅ」`
- TW: `「我感覺得到——漲大了！雙鐵君——你的雞雞——啊！啊——雞雞漲大了」`
- Cũ (CSV3): `「Em cảm, nhận được——đang phồng, lên! Của anh——Soutetsu——\nDương vật——hyui! A——dương, vật」`
- Mới: `「Em cảm, nhận được——đang phồng, lên! Của anh——Soutetsu—— Dương vật——Hyui! A——dương, vật」`
- Lý do: ひゅい = hyu-i — Hepburn đúng là "Hyui"; VN cũ "hyui" đã đúng chính tả (chỉ viết thường), audit đổi thành "Huyi" là sai chính tả (đảo u/y). Khôi phục đúng chính tả + viết hoa H theo quy ước romaji. Chỉ khác VN cũ ở chữ hoa.

### 1015 — んうぅっ→"ưm ư ư" [vowel-count]
- JP: `「舌っ――んっ！　ふ、あっ――入って――ぬるって！\nわたしの、おまんこ――[なか,1]膣内、[すす]啜られて、んうぅっ！！」`
- TW: `「舌頭——嗯！呼、啊——進來了——滑進來了！我的小穴裡面——被舔到了，嗯！！」`
- Cũ: `「Lưỡi——ưm! Phù, a——vào rồi——trơn tuột!\nCô bé, của em——bên trong âm đạo, bị húp trọn, ưm!!」`
- Mới: `「Lưỡi——ưm! Phù, a——vào rồi——trơn tuột! Cô bé, của em——bên trong âm đạo, bị húp trọn, ưm ư ư!!」`
- Lý do: んうぅっ = ん+う+ぅ = 3 nhịp — "ưm" chỉ diễn 1 (tiền lệ h6 778 んううっ→"ưm ư ư").

### 1733 — くっ→"Ku" [romaji]
- JP: `（ぐッ――ぐりゅっ――くっ――んっ――）`
- TW: `（鑽來鑽去）`
- Cũ: `（Hự——ngoáy——ư——ưm——）`
- Mới: `（Hự——ngoáy——Ku——ưm——）`
- Lý do: くっ→"ư" mất hẳn phụ âm k (SFX độc thoại; ぐッ→"Hự" giữ nguyên theo quy ước grunt của file).

## §3. Giữ nguyên — các rên đã đúng (ghi chú đáng kể)

- fa tách "phù, a"/"phù——a" giữ (852 ふあっ――そ、, 886 không thuộc nhóm này — xem §2; 888 không thuộc nhóm này; 899 ふ、ぅっ, 1015/1050/942 ふ、あっ): JP có dấu phẩy tách ふ và あっ thành 2 mảnh riêng — "phù" + "a" diễn đủ cả 2 mora. Khác với ふあっ liền một cụm (đã sửa hết sang romaji). So sánh cờ F4 h6 (fa tách "phù, a" vs h9 "Fu, a") — file này nhất quán dùng "phù, a".
- ひゃ/ひゅ/きゃ romaji đã đúng, giữ: 849 ひゃっ→"Hya", 852 ひゃうんっ→"Hyaun!", 855 ひゃっ→"Hya!", 859 ひゃっ→"Hya!", 933 ひゃうっ→"Hyau!", 850 あひゅんっ→"Ahyun!!!", 854 ひゃきゅ→"Hyakyu!".
- はうっ romaji đã đúng, giữ: 826 (audit "Hau!" — giữ), 897 はうっ→"Hau!", 974 はうっ→"hau!".
- んきゅ romaji đã đúng, giữ: 947 "Nkyun!!!!" (CSV3; audit đổi sai — xem §4), 949 "Nkyu!" (CSV3; giữ trong fix §2).
- くあ romaji đã đúng, giữ: 932 "Kua!" (CSV3; audit đổi sai — xem §4).
- Gasp Ư đã khóa, giữ: 904/905/953/935/1228 (audit), 826? không — 826 là はうっ; các Ư trong 910 (っ→Ư), 847, 849, 875... giữ nguyên, không đụng.
- ふっ/ぷっ→"phù" giữ (toàn file nhất quán): 870 ふ、→"Phù", 927 ふっ→"phù", 968 ふっ→"phù".
- んっ→"ưm" giữ (toàn file nhất quán): 833, 925, 936, 943, 966, 1015 んっ, 913 んっ, 925...
- ちゅ→"chụt" giữ (quy ước file): 924/938/942 ちゅっ, 1723 ちゅっ.
- SFX độc thoại （ ） diễn bằng động từ Việt giữ (quy ước file, audit đã duyệt): 1690 （ぱくっ!）→"Ngoạm!", 1691 （とんっ!）→audit "Cốc nhẹ!", 1694, 1696, 1699, 1700, 1701, 1702, 1704, 1706, 1712, 1713, 1715, 1716, 1717, 1720, 1721, 1722, 1725, 1726, 1728, 1729, 1735, 1739.
- 1735 （ずぶうううううううううううっ!!!）→"（Phậppppppppppppp!!!）" giữ: đã đếm máy — VN có 14 chữ p = đúng 14 mora JP (ず・ぶ・う×11・っ), không sai đếm.
- 823/868 ひ――/ひっ→"hí" giữ (xem cờ F3): ひ đơn không thuộc họ ひゃ/ひゅ/ひあ/きゃ của quy tắc 3b; file nhất quán dùng "hí" cho cả 2 dòng.
- 1003 くっ→"hự!" giữ: Soutetsu rặn (grunt), không phải rên của Paulette; "hự" là cách diễn grunt đã khóa trong file (1713 ぐっ→"Hự"); xem cờ F2.
- 878 ちゅっ→"hôn" giữ: 1399 độc thoại ngay sau đó nói rõ "子宮に、亀頭がキスしてる" (quy đầu đang hôn tử cung) — "hôn" là diễn nghĩa có chủ ý, không phải mất âm; xem cờ F6.
- 903 ふぇ？→"Hả?" giữ: thốt ngạc nhiên, "Hả?" là tương đương Việt tự nhiên; không phải rên.
- 992 やあんっ→"Không chịu đâu" giữ: やあん là từ phủ định ("không chịu"), diễn nghĩa — không phải rên thuần.
- 1017 こしゅっ→"cọ xát", 876 ぐりゅ→"Ngoáy", 1713/1717 ぐいっ→audit "Giật mạnh!" giữ: SFX hành động diễn bằng động từ (quy ước file).
- 1023 びゅうびゅう→audit "phụt phụt" giữ: audit đã bổ sung đúng âm spurt mà CSV3 bỏ sót.
- 826 はうっ→audit "Hau!" giữ: romaji đúng.

## §4. Fix audit bị HỦY / bị lật (đợt thống nhất áp dụng)

- HỦY 2 fix audit (giữ VN cũ, KHÔNG đưa vào JSON — audit làm 19/11, TRƯỚC quy tắc romaji 21/11):
  - 932 くあっ！: audit "Ư a!" → giữ CSV3 "Kua!" (tiền lệ h6 806 くあっ→"Kua"; "Ư a" mất phụ âm k).
  - 947 んきゅんっ！！！！: audit "Ưm!!!!" → giữ CSV3 "Nkyun!!!!" (tiền lệ h6 805 んきゅんっ→"Nkyun"; "Ưm" mất hẳn kyun).
- LẬT / kế thừa có chỉnh 4 fix audit (đã đưa vào JSON §2, fix moan thắng giá trị audit):
  - 892: audit "Siếttttttttt!!!" → moan "Kyuuuuuuuuu!!!" (khôi phục romaji; xem §2).
  - 949: audit "Ưm! … Ưm," → moan "Nkyu! … Kuun," (giữ "Nkyu" của CSV3 + sửa くぅんっ; xem §2).
  - 942: audit "chụt" (cho ちゅむっ) → moan "chumu" (xem §2).
  - 980: audit "Huyi!" → moan "Hyui!" (sửa chính tả romaji; xem §2).
- Giữ nguyên các fix audit còn lại (826 "Hau!", 904/905/935/953/1228 gasp Ư, 1023 "phụt phụt", 1691/1694/1713/1717/1723 SFX).

## §5. Cờ cho đợt thống nhất / cho Hieu (không quyết ở đây)

- F1 — HỦY 2 fix audit (§4): 932 "Kua!", 947 "Nkyun!!!!" — khi gộp audit + moan, KHÔNG áp giá trị audit cho 2 key này.
- F2 — くっ "Ku" (rên Paulette: 854/870/883/886/940/1733) vs "Hự" (grunt: 1003, 1713 ぐっ) vs doc "Ư" — cùng câu hỏi h6 F3, chưa có quyết chung. File này: rên → "Ku", grunt/rặn → "Hự".
- F3 — ひ/ひっ đơn "hí" giữ (823, 868): ひ đơn không nằm trong họ ひゃ/ひゅ/ひあ/きゃ của quy tắc 3b. Nếu đợt thống nhất mở rộng romaji sang ひ đơn thì đổi thành "Hi".
- F4 — họ ちゅ dài: 942 ちゅうう→"chụtttt" (audit, giữ), 924/938 ちゅるっ→"chụt", 1723 ちゅるう→"Chụt" (audit, giữ), れるうっ→"liếmmmm", 1722 ずちゅううっ→"Mútttttttt", 1702/1704 びゅうっ→"Phụtttt" — kéo dài bằng phụ âm t/m thay vì nguyên âm. Tiền lệ h3 liệt kê đây là lỗi chính và đã sửa bằng nguyên âm; h6 F5 hoãn quyết cho họ ちゅ. Chờ quyết chung.
- F5 — 868 ぐっ→"mất": `「はっ――ひっ――いっ、ぐっ――」` → "Hà——hí——ra, mất——ưm" — ぐっ (grunt lúc lên đỉnh) diễn thành từ "mất" không rõ nghĩa; audit giữ nguyên. Cần xem lại nghĩa (có thể là "Hự" như 1003/1713).
- F6 — 878 ちゅっ→"hôn" giữ (lý do ở §3); nếu đợt thống nhất quyết ちゅっ luôn là "chụt" thì đổi.
- F7 — 3 dòng nói lắp KHÔNG phải rên, audit không sửa, ghi lại để audit loop xem: 909 いっ――いっ→"K——kh——không" (いっ diễn thành "K—kh" khó hiểu), 959 きっ→"T," (き diễn thành "T"), 1047 そ……→"A..." (そ diễn thành "A").
- F8 — 1048 双鉄くぅん: tên gọi kéo dài ("Anh Soutetsu……Anh Soutetsu") — độ dài くぅん bị mất, không phải rên nên không sửa ở đây. 1231: TOML escape `\"` vs CSV3 `"` trần (chỉ khác escape, không khác nội dung).
- F9 — 891: っ giữa rên dài diễn bằng "——" ("Phuaaaaaaaaa—Aaaaaaaa!!!") — cách diễn mới cho っ kẹp giữa rên dài, chờ xác nhận chung. 1735: p-count 14 đã kiểm chứng đúng (14 mora), giữ.
- F10 — 915 ふぅんっ→"Phùù ưm": một hơi rên duy nhất tách thành 2 mảnh ("Phùù" + "ưm") theo kiểu diễn của file; tiền lệ khác (lr_ふかみh1 くふぅんんんん→"Kufuunnnn") gộp thành romaji một hơi — nếu thống nhất gộp thì đổi thành "Phùùưm".

## §6. Lượt soát 2 + kiểm chứng cơ học

- Lượt soát 2: đọc lại toàn bộ 36 giá trị fix đối chiếu từng JP (+TW khi cần), đếm lại độc lập từng rên dài bằng ký tự (891: 9 a + 8 a = 17; 892: 9 u; 886: あんっ→"An"; 849/1015: 3 nhịp; 938: 2 nhịp; 846/870: 2 nhịp; 915: 2 u; 1735: 14 p = 14 mora — đã kiểm chứng lại, giữ nguyên).
- Kết quả lượt soát 2: tổng 36 / tái kiểm chứng 36 / bỏ 0 / sửa 1 (942: phát hiện fix tay ban đầu làm mất 1 token "liếm" — đã khôi phục đủ 11 token, chỉ đổi "chu"→"chumu").
- JSON 36 mục, khóa string, jp/tw/old_vn khớp CSV3 36/36 (kiểm chứng máy: old_vn == giá trị CSV3 từng dòng; jp/tw cũng khớp).
- Kiểm chứng diff: mỗi fix chỉ khác VN cũ ở đúng token rên đã nêu (+ làm phẳng `\n`→khoảng trắng theo quy ước file); không fix nào đụng dòng không phải rên.
- Khối TOML parse bằng tomllib: 36 khóa, 0 sai lệch giá trị so với wrong.json (xem §7).

## §7. Kiểm chứng khối TOML (đã chạy tomllib)

- Khối TOML ở §8 parse được bằng tomllib: 36 khóa, 0 sai lệch giá trị so với `moan-paulette-h5-hadaka-epuron-no-remon-doresshingu-ae-wrong.json`.
- TOML gốc: BOM + CRLF, md5 `ba0e02364d99fd8aa8f08daea04428b2`, 305 key script, 0 key trùng, không có bản trùng.

## §8. Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
[script]
846 = "「Nhưng……mà——dù, vậy——cái, thau—— Cái, thau——chắc chắn——sẽ bị bẩn——ưm ưm!」"
848 = "「Ya——phù——Fua——a! Cô bé—— Tan chảy——bị, liếm láp——sắp tan chảy, mất rồi」"
849 = "「Hya——a——đừng trêu chọc, em—— Nữa——mà——ưm ư ư——a!」"
854 = "「Hyakyu! Ku——ưm——Ya——thật dịu dàng, Fua! ——Sướng, quá——hôn, nụ hôn——của anh, Soutetsu!」"
855 = "「Hya! A——ưm——Phùù——Fua!」"
856 = "「Ya! A——mềm quá——ưm——ưm a! Trơn tuột——ấm quá——phù, Kyu——Phùù」"
860 = "「Kya!?」"
862 = "「Yaa!? Đừng có 'ồ'——a——a——a, a Aa!」"
864 = "「Hya!? Tuột ra——ưm! Nóng, quá! Fa!」"
870 = "「Phù, Ku——a——hà——ưm ưm! E……e, em——sắp, són——đó——t, tè」"
873 = "「Hà——a——vâng, anh Soutetsu——ưm! Hãy đến——đây, đi——ạ——Fua!!」"
880 = "「Hà……Ya……xấu hổ……quá……anh ơi……hà, a—— T, tè——đi tè——mau……dừng lại đi」"
883 = "「Hà……a——ưm——Fua——a—— Thế này……thích lắm——ưm——Ku——a——hà」"
884 = "「Hà……a……ưm——phù……phù……Fa」"
886 = "「Fua——a——anh Soutetsu——ưm—— A——Ku——Fua——a——An」"
888 = "「Pua——a……Paulette」"
890 = "「Fa……bị……phủ lên, rồi——ưm—— Em, bị anh Soutetsu——phủ bằng nước xốt, trắng——rồi——」"
891 = "「Phuaaaaaaaaa—Aaaaaaaa!!!」"
892 = "「Phù——Kyuuuuuuuuu!!!」"
893 = "「Pua!」"
895 = "「Fa! A! A! A! Anh Soutetsu! A——tử cung! Nữa đi! Đâm vào, nữa đi!」"
906 = "「A——Fua——bụng——cô bé—— Ưm——thế này——tuyệt quá——bị ngoáy sâu——vào——Fua!」"
913 = "「Ya——a——chân——ưm——phù——hà, a, Thế này——không được——hông——nổi lên, rồi——ưm!」"
915 = "「A……lại, nữa——ưm——như thế……a——thật, dịu dàng ——hà, ưm——cẩn, thận——quá——Phùù ưm!」"
920 = "「A……Fa……a……em tè……mất……rồi. Em……ngay trước, mặt——anh Soutetsu――――」"
921 = "「A……a——a……Yaa……không chịu……không chịu đâu」"
924 = "「A……ngoạm——ưm——liếm——Eroo——ưm ——Chụt——chụt——ngoạm——liếmmmm」"
927 = "「A, Ya! Không dừng, được——phù——a, đừng nhìn! Đừng nhìn em mà, anh Soutetsu——a——ưm!」"
938 = "「Ưm ưm——chụt——ngoạm——chụt——liếm, liếm——liếm——liếmmmm——」"
940 = "「Ưm……Ku——Fua——a! Không phải—— Chỗ đó! Ưm——ghét——quá——sốt ruột——quá」"
942 = "「Ưm……chụt——chumu——chụtttt——chụt ——Phù, a——ưm——liếm——liếm——liếmmmm」"
949 = "「Nkyu! A——anh Soutetsu! Kuun, Sâu——hơn nữa——em không, sao——đâu」"
958 = "「A……nóng, quá——ưm——Fua——a—— Nhà, bếp——tạp dề, ề——cả, em——nữa」"
980 = "「Em cảm, nhận được——đang phồng, lên! Của anh——Soutetsu—— Dương vật——Hyui! A——dương, vật」"
1015 = "「Lưỡi——ưm! Phù, a——vào rồi——trơn tuột! Cô bé, của em——bên trong âm đạo, bị húp trọn, ưm ư ư!!」"
1733 = "（Hự——ngoáy——Ku——ưm——）"
```

## Kết bài

- h5 moan: đổi 36/305 dòng (11,8% file; 36/202 dòng rên ứng viên) — romaji 27, đếm nguyên âm 6, romaji + đếm nguyên âm 3. Ngoài ra 2 fix audit bị đề nghị HỦY (932 "Kua!", 947 "Nkyun!!!!" — giữ VN cũ, xem §4).
- Lỗi chủ đạo: họ fa/fu bị diễn "phù" mất âm a (15 dòng, 17 token); mất phụ âm mora trong "Á"/"Ư" (や/きゃ/くっ/んきゅ/きゅ/あんっ/ひゅい — 16 dòng); đếm nguyên âm thiếu (んううっ, んうぅっ, んーむっ, んんっ, ふぅんっ, ふぁ dài 891; cộng ふうっ trong 855/856 và んんっ trong 870).
- Khối TOML 36 key đã parse đúng (tomllib, 0 sai lệch); JSON 36 mục khóa string, jp/tw/old_vn khớp CSV3 36/36.
- Lượt soát 2: 36/36 tái kiểm chứng, 0 bỏ, 1 sửa (942 khôi phục token "liếm" bị sót). Sweep 5 mục đã kiểm chứng, không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào.
- 10 cờ cho đợt thống nhất (F1–F10), trong đó quan trọng nhất: F1 (hủy 2 fix audit), F2 (くっ "Ku" vs "Hự"), F4 (họ ちゅ dài kéo bằng t/m), F5 (868 ぐっ→"mất").
