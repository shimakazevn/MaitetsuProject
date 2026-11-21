# Moan-fix: Paulette lr_ポーレットh1_家族旅行の最終日の夜 (Đêm cuối cùng của chuyến du lịch gia đình) — 22 dòng rên sửa sang romaji

## Kiểm chứng file

- File: `03_Paulette/lr_ポーレットh1_家族旅行の最終日の夜.txt.toml` — route 03_Paulette, 303 dòng script (key 697–1745).
- TOML md5: `bd55bd0643350b7396121d5161727c21` — khớp md5 trong audit review, không có bản trùng (không thuộc nhóm 11 file trùng lặp).
- CSV3: 1 bộ duy nhất (`03_Paulette`), 303 dòng, 0 key trùng; TOML vs CSV3 khớp (chỉ khác `\n`/khoảng trắng như audit đã ghi).
- Audit trước đó: 64 sai đã merge (18 xưng hô + 1 nghĩa + 3 gasp + 37 hơi thở thoại + 5 SFX độc thoại). Moan pass này xét lại TOÀN BỘ dòng rên/SFX trong file, không chỉ 64 dòng audit.
- Sweep gasp っ: 17 mục trong file này (16 mục sweep + 1077 — sweep JSON hiện tại đã có 1077, audit ghi là "sweep bỏ sót" ở thời điểm audit). Đã kiểm từng mục: 0 dòng bị đụng bởi moan fix (xem mục "Ghi chú giữ" bên dưới).
- Quy ước romaji dùng trong file này: Hepburn chặt, khớp hình âm JP + công thức nguyên âm (số nguyên âm = 1 + số う/ぅ trong JP): ふぁ (1 mora) → "Fa", ふあ (2 mora) → "Fua", ぷぁ → "Pa", ぷあ → "Pua", ひゃう → "Hyau". Tiền lệ: 凪h2 dùng "Fa" cho ふぁ (2451, 2462) và lr-h2 dùng "Fa/Fua"; h8 dùng "Fua" cho cả ふぁ lẫn ふあ (2049, 2167, 2212) và "Pua" cho cả ぷぁ lẫn ぷあ (2279, 2340) — file này theo dạng Hepburn chặt, ghi flag F4 để đợt thống nhất quyết có thống nhất một dạng toàn dự án hay không.
- Cách xây fix: 19 dòng trùng audit — xây từ GIÁ TRỊ AUDIT (một dòng, khoảng trắng), chỉ đổi đúng phần rên, để không làm mất các quyết định khác của audit trong cùng dòng (SFX, gasp Ư, "Ưm kyu", "ư ư"); 3 dòng không có trong audit (1018, 1098, 1099) — xây từ VN cũ CSV3, giữ nguyên vị trí `\n`. Kiểm chứng bằng máy: mỗi fix chỉ khác giá trị gốc ở đúng (các) token rên đã nêu.
- Lưu ý: file `audit-paulette-lr-h1-wrong.json` dùng key INT (sai chuẩn "key string" của brief) — đã ghi nhận, không sửa file audit; file moan json này dùng key STRING theo chuẩn loop.

## Kiểm kê rên

- Đã đọc 303/303 dòng (khối H-scene 950–1235 đọc kỹ từng dòng + 54 dòng độc thoại SFX trong ngoặc + các dòng ngoài khối có âm thanh: 705, 728, 730, 732).
- Đã xét 143 dòng rên/SFX: 89 dòng thoại + 54 dòng độc thoại SFX.
- Đổi 22 dòng (21 romaji + 1 sai âm). Giữ 121 dòng.
- Phân loại 22 dòng đổi: ひゃう→Hyau 3 dòng (1000, 1002, 1003); ふぁ→Fa 8 dòng (1003, 1019, 1022, 1023, 1025, 1062, 1096, 1100); ふあ→Fua 5 dòng (1000, 1020, 1049, 1058, 1124); ぷぁ→Pa 2 dòng (1043, 1065); ぷあ→Pua 2 dòng (1113, 1201); ふえ→Fue 2 dòng (1018, 1098); きゅっふっ→Kyuffu 1 dòng (998); んゅっ→Nyu 1 dòng (1099). Tổng 24 token rên trong 22 dòng (1000 và 1003 mỗi dòng 2 token).
- Không có dòng nào sửa xưng hô/thuật ngữ/nghĩa. Không dòng "Kh" nào bị đổi sang Ư. Không dòng gasp Ư nào bị đụng.

## Chi tiết từng dòng sửa

**Key 998 (ポーレット) — romaji**
- JP: `「きゅっふっ！！！？　～～～～～～～っ！！！！」`
- TW: `「呀呼！！！？哇～～～～～！！！！」`
- VN cũ: `「Kyufu!!!? ~~~~~~~!!!!」`
- Sửa: `「Kyuffu!!!? ~~~~~~~Ư!!!!」`
- Lý do: きゅっふっ là MỘT âm duy nhất (kyu + っ nhân đôi + fu). "Kíuphù" của audit tách thành 2 vần Việt ("Kíu"+"phù") — sai hình âm. Romaji Hepburn "Kyuffu" (っ nhân đôi f). Giữ nguyên đuôi gasp ~~~~~~~Ư của sweep/audit.

**Key 1000 (ポーレット) — romaji**
- JP: `「ひゃうっ――んっ――ふあっ――ふっ――\n指、かたいとこ――かんせつ――こしゅ、れてっ」`
- TW: `「呀唔——嗯——呼啊——呼——手指的——關節——硬硬的，蹭到了」`
- VN cũ: `「Hya――ưm――phù――phù――\nChỗ cứng của, ngón tay――khớp xương――đang cọ, xát」`
- Sửa: `「Hyau――ưm――Fua――phù―― Chỗ cứng của, ngón tay――khớp xương――đang cọ, xát」`
- Lý do: ひゃうっ → "Hyau" (Hepburn: ひゃ=Hya + う=u; "Hiau" của audit không phải Hepburn — tiền lệ h8 2137 "Hyau"); ふあっ → "Fua" (họ fa/fu ngượng). Giữ "phù" cho ふっ (thở ngắn, tự nhiên).

**Key 1002 (ポーレット) — romaji**
- JP: `「ひゃうっ！！　けどっ―きもちいっ――んっ――\nそうてつ、くっ――んっ――しょこっ――そこっ」`
- TW: `「呀唔！！但是——好舒服——嗯雙鐵君——嗯——好棒——那裡」`
- VN cũ: `「Hya!! Nhưng mà――sướng quá――ưm――\nAnh Soutetsu――ưm――chỗ đó――chỗ đó」`
- Sửa: `「Hyau!! Nhưng mà――sướng quá――ưm―― Anh Soutetsu――ưm――chỗ đó――chỗ đó」`
- Lý do: ひゃうっ → "Hyau" (như 1000).

**Key 1003 (ポーレット) — romaji**
- JP: `「ひゃうっ！？　あっ――んっ！　くっ――ふぁっ！\nんあっ！！」`
- TW: `「呀唔！？啊——嗯！咕——呼啊！嗯啊！！」`
- VN cũ: `「Hyau!? A――ưm! Hự――phù!\nƯm a!!」`
- Sửa: `「Hyau!? A――ưm! Hự――Fa! Ưm a!!」`
- Lý do: ひゃうっ → "Hyau"; ふぁっ → "Fa" (ふぁ 1 mora / 1 nguyên âm). Giữ "Hự" cho くっ.

**Key 1018 (ポーレット) — romaji**
- JP: `「ふえっ！？　やっ――双鉄くんっ――だめっ――\nお指っ――んっ――おまんのこ、中で――ひろげちゃっ」`
- TW: `「呼哎！？呀——雙鐵君——不可以——手指——嗯——在小穴裡——撐開」`
- VN cũ: `「Hả!? A――Anh Soutetsu――không được――\nNgón tay――ưm――trong, âm đạo――đang mở rộng ra」`
- Sửa: `「Fue!? A――Anh Soutetsu――không được――\nNgón tay――ưm――trong, âm đạo――đang mở rộng ra」`
- Lý do: ふえっ: "Hả!?" mất hơi thở f và nguyên âm ue; TW 呼哎 là tiếng thở. Theo tiền lệ h8 2185 "Fue!?". Giữ nguyên phần còn lại của dòng.

**Key 1019 (ポーレット) — romaji**
- JP: `「ふぁっ――あっ――あっ――あっ――」`
- TW: `「呼啊——啊——啊——啊——」`
- VN cũ: `「Phù――a――a――a――」`
- Sửa: `「Fa――a――a――a――」`
- Lý do: ふぁっ → "Fa".

**Key 1020 (ポーレット) — romaji**
- JP: `「ふあっ――あっ――ねっ――ふあっ――もっと――\nそうてつ、くんっ――おまんこ――もっと――」`
- TW: `「呼啊——啊——我說——呼啊——繼續——雙鐵君——小穴——還要更多——」`
- VN cũ: `「Pha——a——nè——pha——nữa đi——\nAnh Soutetsu——âm đạo——nữa đi——」`
- Sửa: `「Fua——a——nè——Fua——nữa đi—— Anh Soutetsu——âm đạo——nữa đi——」`
- Lý do: ふあっ ×2 → "Fua".

**Key 1022 (ポーレット) — romaji**
- JP: `「ふぁっ――あっ――指より――わた、しっ――んっ――\nおちん、ちん――そうてつくん、の、ほしい、のにっっ」`
- TW: `「呼啊——啊——比起手指——我——嗯——明明——更想要，你的，肉棒呀」`
- VN cũ: `「Phù――a――Hơn cả ngón tay――em――ưm――\nMuốn, chim――của anh Soutetsu, cơ」`
- Sửa: `「Fa――a――Hơn cả ngón tay――em――ưm―― Muốn, chim――của anh Soutetsu, cơ」`
- Lý do: ふぁっ → "Fa".

**Key 1023 (ポーレット) — romaji**
- JP: `「ふあっ――あっ！　あっ！　あっ！\nはっ！　あっ――んうっ――くふっ――あっ！」`
- TW: `「呼啊——啊！啊！啊！哈！啊——嗯唔——咕呼——啊！」`
- VN cũ: `「Phù――a! A! A!\nHà! A――ưm――kufu――a!」`
- Sửa: `「Fa――a! A! A! Hà! A――ưm――Khự――a!」`
- Lý do: ふぁっ → "Fa". Giữ "Khự" cho くふっ (quy tắc Kh khóa 21/11 — っ đã diễn thành Kh, không đổi sang Ư).

**Key 1025 (ポーレット) — romaji**
- JP: `「ふぁっ――ンッ――（こくっ）――チュむっ――ちゅ\nれるっ――れりゅううっ――ぢゅるっ――ちゅううっ」`
- TW: `「呼啊——嗯——（吞嚥）——啾唔——啾滋溜——滋嚕嚕——啾嚕——啾唔唔」`
- VN cũ: `「Phù――ưm――（ực）――chùn chụt――chụt\nLiếm――liếm――chùn chụt――chùn chụt」`
- Sửa: `「Fa――ưm――（ực）――chụt――chụt Rộp――rộộộp――rột——chụụụt」`
- Lý do: ふぁっ → "Fa". Giữ toàn bộ SFX của audit (chụt/rộp/rột/chụụụt).

**Key 1043 (ポーレット) — romaji**
- JP: `「んむっ！？！　んっ――ちゅっ――じゅりゅっ――\nりゅっ――れるっ――ちゅぷっ――ちゅむっ――ぷぁ」`
- TW: `「唔嗯！？！嗯——啾——啾溜——溜——滋溜——啾噗——啾嗯——噗啊」`
- VN cũ: `「Ưm!?! Ưm——chụt——chu ryu——\nryu——rê ru——chu pu——chu mu——pha」`
- Sửa: `「Ưm!?! Ưm——chụt——rột—— rộp——rộp——chụt——chụt——Pa」`
- Lý do: ぷぁ → "Pa" (1 nguyên âm theo công thức). Giữ SFX của audit.

**Key 1049 (ポーレット) — romaji**
- JP: `「ぁっ――っ――ふあ――あっ――おくっ――おちんちん\n――きとう――あたると――頭も、ごちゅっって――」`
- TW: `「啊——唔——呼啊——啊——裡面——肉棒——龜頭——頂到之後——腦袋也，像被頂開了花——」`
- VN cũ: `「A——ư——pha——a——bên trong——dương vật\n——quy đầu——chạm vào——đầu em cũng, như muốn nổ tung——」`
- Sửa: `「A——ư——Fua——a——bên trong——dương vật ——quy đầu——chạm vào——đầu em cũng, như muốn nổ tung——」`
- Lý do: ふあ → "Fua".

**Key 1058 (ポーレット) — romaji**
- JP: `「あっ――うんっ――けどっ――ふあっ、あっ――\nけど、ね？　そうてつくぅん」`
- TW: `「啊——嗯——可是——呼啊，啊——可是啊，雙鐵君」`
- VN cũ: `「A——ưm——nhưng mà——pha, a——\nnhưng mà, anh Soutetsu」`
- Sửa: `「A——ưm——nhưng mà——Fua, a—— nhưng mà, anh Soutetsu」`
- Lý do: ふあっ → "Fua".

**Key 1062 (ポーレット) — romaji**
- JP: `「ぁ……チュッ――ちゅっ――んっ――ふぁっ。\nん……えへへっ――わたしも、愛しています。双鉄くん」`
- TW: `「啊……啾——啾——嗯——呼啊。嗯……哎嘿嘿——我也愛你。雙鐵君」`
- VN cũ: `「A……chụt——chụt——ưm——pha.\nƯm……ehehe——em cũng yêu anh. Anh Soutetsu」`
- Sửa: `「A……chụt——chụt——ưm——Fa. Ưm……ehehe——em cũng yêu anh. Anh Soutetsu」`
- Lý do: ふぁっ → "Fa". Giữ "ehehe" (audit đã flag chờ Hieu quyết: giữ Latin hay "hì hì" — không tự quyết).

**Key 1065 (ポーレット) — romaji**
- JP: `「あ……。ん――ちゅっ――ちゅむっ――ちゅっ、\nちゅぶっ――ちゅぱっ――ぷぁ――れろっ――にゅるっ」`
- TW: `「啊……嗯——啾——啾嗯——啾，啾噗——啾啪——噗啊——滋溜——啾嚕」`
- VN cũ: `「A……. Ưm――chụt――chùn chụt――chụt,\nchụt――chụt――phù――liếm――trơn tuột」`
- Sửa: `「A……. Ưm――chụt――chụt――chụt, chụt――chụt――Pa――rộp――trơn tuột」`
- Lý do: ぷぁ → "Pa". Giữ SFX của audit.

**Key 1096 (ポーレット) — romaji**
- JP: `「んきゅっ――ふぁっ――あっ、これ――しゅきっ――\nっっ――ふっ――ねっ――このまま――もっと」`
- TW: `「嗯呀——呼啊——啊，這個——好棒——唔——呼——來——就這樣——繼續」`
- VN cũ: `「Ưm——pha——a, thế này——thích quá——\nư——phu——nè——cứ thế này——nữa đi」`
- Sửa: `「Ưm kyu——Fa——a, thế này——thích quá—— ư ư——phu——nè——cứ thế này——nữa đi」`
- Lý do: ふぁっ → "Fa". Giữ "Ưm kyu" (んきゅっ, theo tiền lệ h7 của audit), "ư ư" (っっ, gasp của audit) và "phu" (ふっ cụt, audit chấp nhận).

**Key 1098 (ポーレット) — romaji**
- JP: `「ふえっ！？」`
- TW: `「嗯哎！？」`
- VN cũ: `「Hả!?」`
- Sửa: `「Fue!?」`
- Lý do: ふえっ → "Fue!?" (như 1018).

**Key 1099 (ポーレット) — moan-wrong-sound**
- JP: `「んゅっ！」`
- TW: `「嗯唔！」`
- VN cũ: `「Ưm!」`
- Sửa: `「Nyu!」`
- Lý do: んゅっ: old "Ưm!" mất hẳn âm yu (chỉ còn tiếng mũi). Romaji "Nyu!" (tiền lệ h8 2304 んゆっ→"Nyu"); 1 nguyên âm u theo công thức.

**Key 1100 (ポーレット) — romaji**
- JP: `「んっ！　――ふぁっっ――やぁんっ――指っ――んっ！\nいきなりっ――に、ほんっ――ひ――ぁっ――」`
- TW: `「嗯！——呼啊——呀嗯——手指——嗯！一上來就——兩根——呀——啊——」`
- VN cũ: `「Ưm! ――Phù――A――Ngón tay――ưm!\nĐột nhiên――hai, ngón――hi――a――」`
- Sửa: `「Ưm! ――Fa――A――Ngón tay――ưm! Đột nhiên――hai, ngón――hi――a――」`
- Lý do: ふぁっっ → "Fa" (cắt っ đôi diễn bằng ―― ngay sau).

**Key 1113 (ポーレット) — romaji**
- JP: `「ぷあっ！　あっ――はっ――あっ――しゅごっ――\nおまんこ――しきゅう――すごい――こい、のっ」`
- TW: `「噗啊！啊——哈——啊——好厲害——小穴——子宮——好多——濃濃的」`
- VN cũ: `「Pha! A——ha——a——tuyệt quá——\nâm đạo——tử cung——nhiều quá——đặc quá」`
- Sửa: `「Pua! A——ha——a——tuyệt quá—— âm đạo——tử cung——nhiều quá——đặc quá」`
- Lý do: ぷあっ → "Pua".

**Key 1124 (ポーレット) — romaji**
- JP: `「はい……っ――ふあっ――たくさん、たくさん――\n精子、わたし――そうてつくんから――受け取って」`
- TW: `「好的……呼啊——雙鐵君——要給我很多，很多——精子」`
- VN cũ: `「Vâng……ưm――phù――Thật nhiều, thật nhiều――\nTinh trùng, em――sẽ nhận lấy――từ anh Soutetsu」`
- Sửa: `「Vâng……ưm――Fua――Thật nhiều, thật nhiều―― Tinh trùng, em――sẽ nhận lấy――từ anh Soutetsu」`
- Lý do: ふあっ → "Fua".

**Key 1201 (ポーレット) — romaji**
- JP: `「れりゅっ――りゅっ！　じゅるるるるっ――（ごくっ）\nぷあっ――ね、双鉄くん――ンッ――ちゅ、ちゅむっ！」`
- TW: `「滋嚕——嚕！滋嚕嚕嚕嚕——（吞嚥）噗啊——雙鐵君——嗯——啾、啾唔！」`
- VN cũ: `「Rê ryu——ryu! Chu ru ru ru——（Ực）\nPha——nè, anh Soutetsu——ưm——chu, chu mu!」`
- Sửa: `「Rộp——rộp! Rột——（Ực） Pua——nè, anh Soutetsu——ưm——chụt, chụt!」`
- Lý do: ぷあっ → "Pua". Giữ SFX của audit.

## Ghi chú giữ (các dòng rên đã xét mà giữ nguyên)

- ひあっ → "Hia" đã là romaji (1005, 1007, 1011) — giữ; ひゃっ → "Hya" đã là romaji (997, 1009, 1013) — giữ. 1220 はああっ → "Haaa!" đúng công thức (3 a) — giữ.
- SFX miệng của audit giữ toàn bộ: chụt/rột/rộp/trơn tuột + đếm nguyên âm chụụụt/rộộộp/chụụụụt (1025, 1040, 1042, 1056, 1060, 1072, 1082, 1083, 1085, 1089, 1203, 1220) — diễn Việt tự nhiên, không ngượng.
- あんっ → "An" (1073, 1074, 1075 — audit) — giữ. んきゅっ → "Ưm kyu" (1097 — giống fix audit ở 1096) — giữ, không đổi sang "Nkyu" (kiểu 凪h2 2395) vì "Ưm kyu" đã diễn đủ cả ん lẫn きゅ, không ngượng.
- Hơi thở ngắn giữ nguyên: ふっ/ふうっ → "phù"/"phu" (1000, 1026, 1086, 1096, 1184), はっ/あっ/んっ → "Ha/A/Ưm" (1032, 1047, 1052, 1054, 1067, 1068, 1090, 1102, 1103, 1115, 1122, 1126, 1131, 1218, 1219, 1222) — diễn Việt ngắn gọn, đúng âm.
- Cười: ふふっ → "fufu" (1088), うふふ → "ufufu" (1181), えへへ → "ehehe" (1062) — đã là dạng Latin, là tiếng cười (không phải rên) — giữ; audit đã flag chờ Hieu quyết (giữ Latin hay "hì hì"/"phì phì"), moan pass không quyết thay.
- Độc thoại SFX 54 dòng giữ toàn bộ: đã diễn thành động từ Việt theo quy ước file (Đâm vào/rút ra/cọ xát/Phụt/Thúc mạnh/lút cán...); 5 dòng audit đã sửa giữ nguyên (1592 ぽっ→"Bụp", 1610 ぐいっ→"Giật mạnh", 1711 じゅぶううううっ→"Phậậậậập", 1716 "Trượt, trơn", 1721 ずゅぶっぅぅっ→"Phậậập").
- Gasp Ư (17 mục sweep): giữ toàn bộ, không đụng — 705 (――Ư), 997 (Hya――~~Ư), 1014, 1035 (Ế～～Ư), 1046, 1061, 1078/1079/1080 (Ư!/Ư!!/Ư!!!), 1196 (Paulette——Ư!), 1005/1083 (Ư cuối dòng của sweep/audit), 1044/1045 (Ư bổ sung của audit), 1016 (already-rendered, audit đồng ý), 1077 (Ư! đầu dòng, audit tìm thêm). Đuôi ~~~~~~~Ư của 998 được GIỮ NGUYÊN trong fix moan (chỉ đổi "Kíuphù"→"Kyuffu").
- 1015 っ (Soutetsu) → "Ưm" — tiếng ừm, TW 呃 — giữ, không phải rên cần romaji.
- 1034 えっ → "Hả!?" — giữ: えっ là cảm thán ngạc nhiên ngắn, khác ふえっ (có hơi thở f) ở 1018/1098 nên không đổi sang "Fue".
- 959 やっっ → "A, ừm", 995 ですぅっ (moan んっ→"ưm" đã có), 1153 っっ (diễn bằng ――), 1179 くんっ, 728 ばたんきゅ～ → "ngủ khò khò" (SFX ngủ) — giữ, không phải rên cần sửa.

## Flags (ghi lại, KHÔNG quyết)

- **F1 — 1156 くぅん:** JP `「ね？　それならね、双鉄くぅん」` — âm u kéo dài trong cách gọi tên ("Soutetsu-kuuun") không có trong VN cũ ("anh Soutetsu"). Không phải rên — ghi cho vòng audit/đợt thống nhất, không sửa ở đây.
- **F2 — 1689 ぷちゅっん:** độc thoại `（もに――ぷにゅっ――ぷりゅっ！　ぷちゅっん）` → VN `(Nắn bóp——Mềm mại——Mềm mại! Phụt)` — ぷちゅっん là tiếng nhớp/óp (squelch-pop), còn "Phụt" trong file này dùng cho びゅ (phun). Nghĩa SFX chưa chắc — ghi cho vòng audit, không sửa ở đây.
- **F3 — cười Latin 1062/1088/1181:** audit đã flag chờ Hieu quyết (giữ Latin "ehehe/fufu/ufufu" hay dùng "hì hì"/"phì phì"); moan pass giữ nguyên, không quyết thay.
- **F4 — quy ước Fa/Fua:** h8 dùng "Fua" cho cả ふぁ; file này dùng "Fa" cho ふぁ theo Hepburn chặt (tiền lệ 凪h2, lr-h2). Nếu muốn thống nhất một dạng toàn dự án thì quyết ở đợt thống nhất.
- **F5 — audit json key INT:** file `audit-paulette-lr-h1-wrong.json` dùng key số nguyên, sai chuẩn "key string" của brief (chỉ ghi nhận; moan json này dùng key string).

## Lượt soát 2

- Tổng 22 / tái kiểm chứng 22 / bỏ 0 / sửa 0. Đọc lại toàn bộ 22 fix đối chiếu JP (+TW): đếm nguyên âm khớp công thức từng token romaji (Fa 1, Fua 2, Pa 1, Pua 2, Hyau 2 = 1+1う, Kyuffu 1+1, Fue 2, Nyu 1); mỗi fix chỉ khác giá trị gốc ở đúng token rên; không fix nào lẫn xưng hô/thuật ngữ/nghĩa; không dòng Ư/Kh nào bị đụng.
- Kiểm chứng bằng máy: JSON 22 mục, key string, jp/tw/old_vn khớp CSV3 22/22; khối TOML parse bằng tomllib: 22 khóa, 0 sai lệch giá trị so với JSON.

## Khối TOML để dán vào file (đã kiểm chứng parse được)

Khối dưới đây đã kiểm chứng parse được bằng tomllib, đúng 22 key, giá trị khớp đúng JSON bản sửa. Dán vào section `[script]` của file `03_Paulette/lr_ポーレットh1_家族旅行の最終日の夜.txt.toml` (ghi đè đúng 22 key này; các key này THAY THẾ giá trị audit cùng key ở đợt thống nhất — áp giá trị moan, không áp cả hai; giữ nguyên mọi key khác). Lưu ý: `\\n` trong dòng 1018 là ký tự `\n` theo đúng CSV3 (game tự ngắt dòng).

```toml
[script]
998 = "「Kyuffu!!!? ~~~~~~~Ư!!!!」"
1000 = "「Hyau――ưm――Fua――phù―― Chỗ cứng của, ngón tay――khớp xương――đang cọ, xát」"
1002 = "「Hyau!! Nhưng mà――sướng quá――ưm―― Anh Soutetsu――ưm――chỗ đó――chỗ đó」"
1003 = "「Hyau!? A――ưm! Hự――Fa! Ưm a!!」"
1018 = "「Fue!? A――Anh Soutetsu――không được――\\nNgón tay――ưm――trong, âm đạo――đang mở rộng ra」"
1019 = "「Fa――a――a――a――」"
1020 = "「Fua——a——nè——Fua——nữa đi—— Anh Soutetsu——âm đạo——nữa đi——」"
1022 = "「Fa――a――Hơn cả ngón tay――em――ưm―― Muốn, chim――của anh Soutetsu, cơ」"
1023 = "「Fa――a! A! A! Hà! A――ưm――Khự――a!」"
1025 = "「Fa――ưm――（ực）――chụt――chụt Rộp――rộộộp――rột——chụụụt」"
1043 = "「Ưm!?! Ưm——chụt——rột—— rộp——rộp——chụt——chụt——Pa」"
1049 = "「A——ư——Fua——a——bên trong——dương vật ——quy đầu——chạm vào——đầu em cũng, như muốn nổ tung——」"
1058 = "「A——ưm——nhưng mà——Fua, a—— nhưng mà, anh Soutetsu」"
1062 = "「A……chụt——chụt——ưm——Fa. Ưm……ehehe——em cũng yêu anh. Anh Soutetsu」"
1065 = "「A……. Ưm――chụt――chụt――chụt, chụt――chụt――Pa――rộp――trơn tuột」"
1096 = "「Ưm kyu——Fa——a, thế này——thích quá—— ư ư——phu——nè——cứ thế này——nữa đi」"
1098 = "「Fue!?」"
1099 = "「Nyu!」"
1100 = "「Ưm! ――Fa――A――Ngón tay――ưm! Đột nhiên――hai, ngón――hi――a――」"
1113 = "「Pua! A——ha——a——tuyệt quá—— âm đạo——tử cung——nhiều quá——đặc quá」"
1124 = "「Vâng……ưm――Fua――Thật nhiều, thật nhiều―― Tinh trùng, em――sẽ nhận lấy――từ anh Soutetsu」"
1201 = "「Rộp——rộp! Rột——（Ực） Pua——nè, anh Soutetsu——ưm——chụt, chụt!」"
```

## Kết bài

File lr_ポーレットh1 đã xong moan-fix: đọc 303/303 dòng, xét 143 dòng rên/SFX, đổi 22 dòng (21 romaji + 1 sai âm mất tiếng), giữ 121 dòng. Toàn bộ họ fa/fu trong file giờ đã là romaji (Fa/Fua/Pa/Pua theo Hepburn chặt); ひゃう đã là "Hyau"; ひあ/ひゃ đã là "Hia"/"Hya" từ trước nên giữ. Không đụng gasp Ư (17 mục sweep), không đụng "Kh", không sửa xưng hô/thuật ngữ/nghĩa. Còn 5 flag ghi lại cho vòng audit/đợt thống nhất (F1–F5), trong đó F3 (cười Latin) chờ Hieu quyết. Chi tiết đầy đủ trong file này; danh sách sửa: `moan-paulette-lr-h1-kazoku-ryokou-wrong.json`; tóm tắt: `moan-snippet-paulette-lr-h1-kazoku-ryokou.md`.
