# Moan-fix: Paulette h7_残業エッチもyシャツで — 47 dòng rên sửa (romaji + cười)

## 1. Xác minh file

- File: `ポーレットh7_残業エッチもyシャツで.txt.toml` — route 03_Paulette, 326 dòng script (độc thoại 174, Paulette 96, Soutetsu 56).
- TOML: `sources/toml2/translation_toml/03_Paulette/#U30dd#U30fc#U30ec#U30c3#U30c8h7_#U6b8b#U696d#U30a8#U30c3#U30c1#U3082y#U30b7#U30e3#U30c4#U3067.txt.toml`, md5 `6cd9aaebbdca88cdc9df37e560158f60` (khớp md5 audit đã ghi), không có bản trùng trong 227 file TOML.
- CSV3: 1 bộ duy nhất, 326 dòng, 0 key trùng; File `translation_toml\\03_Paulette\\ポーレットh7_残業エッチもyシャツで.txt.toml`. TOML vs CSV3: khớp toàn bộ 326/326 (chuẩn hoá `\n` → khoảng trắng), 0 khác biệt thực chất — khớp xác minh của audit.
- Audit trước đó: 24 fix (19/11), trong đó 10 key trùng với fix moan dưới đây — fix moan được xét trên bản VN **sau audit** (fix audit + sửa moan gộp lại), còn `old_vn` trong JSON là VN hiện tại trong CSV3/TOML (theo đúng quy ước moan-paulette-h8). 10 key trùng audit chỉ khác giá trị audit đúng token rên (xem §5).
- Sweep gasp っ: đã kiểm chứng trực tiếp trong `sweep-raw-gasp-wrong.json` — sweep có 10 mục trong file (6 bản sửa Ư: 1233, 1270, 1271, 1285, 1331, 1380 — audit đã nhận; 3 already-rendered: 879, 896, 899 — audit đồng ý; 1 needs-file-audit: 816 — audit tự giải quyết + 1 bỏ sót 912 — audit bắt được). Moan **không đụng** bất kỳ fix Ư nào của sweep/audit; 2 key moan (816, 912) đã gồm Ư của audit trong giá trị fix. Không có dòng "Kh" nào trong file (đã quét: 0 token "Kh"/"kh" độc lập) — không có gì bị đổi sang Ư.
- Quy ước giá trị fix: viết MỘT DÒNG (khoảng trắng thay cho `\n`), theo đúng quy ước audit của chính file này (file TOML gốc cũng lưu một dòng với khoảng trắng); `old_vn` trong JSON giữ nguyên literal `\n` của CSV3.

## 2. Tồn kho rên (moan inventory)

- Đọc toàn bộ 326/326 dòng; 208 dòng chứa dấu hiệu rên/thở/gasp/SFX đã xét kỹ (Paulette 88, Soutetsu 30, độc thoại 90 — gồm các khối SFX trong ngoặc và gasp cuối dòng). Sửa **47 dòng**, giữ 161 dòng.
- Phân loại 47 fix (một key có thể mang 2 token, tổng 66 token):
  - Họ fa/fu → romaji (18 token): 780 Pu, 809 Fuya, 818 Fua, 834 Fua×2, 847 Pu, 850 Fua, 851 Fa, 853 Fua, 854 Fua, 858 Fua, 882 Fa, 885 Fua, 901 Fu, 912 Fa, 920 Fuwa, 921 Fuaa, 930 Fupu.
  - Họ ひゃ/ひゅ/ひあ/きゃ → romaji (15 token): 808 Hia, 810 Hyu, 811 Hyau, 812 Hyau, 816 Hia, 818 Hia+Nyu, 820 Hia, 821 Kyafu+Kyau, 826 Hia, 830 Hyauu, 856 Yuh, 899 Kyafu, 920 Nhyun.
  - ん+phụ âm gộp romaji (13 token): 808 Nmu, 821 Nku, 834 Nkyun, 839 Nku, 867 Ngu, 872 Anmu, 903 Nryu, 905 Nmu+Amu, 918 Nkyun, 921 Nkyu, 930 Nmu, 965 Aaanmu (+ Nyu/Nhyun đã kể ở họ ひゃ).
  - や/ら/あう mất phụ âm (11 token): 786 Ya+Ra, 824 Au+Raa, 828 Ya+Yaaan, 843 Ya, 854 Yaa, 882 Ya, 889 Yan, 898 Au.
  - く → Ku (4 token): 838 Ku, 873 Ku, 882 Kku, 885 ku (+ 831 đã đúng).
  - ふぇ → Fue (1): 862. Cười → Ufufu (2): 936, 939. Âm dài khác (2): 808 Hamuu, 860 đếm 15u. Ngoài ra 2 key khôi phục romaji sau audit Việt hoá: 826, 860 (đã kể trong các họ trên).
- Lỗi rên tập trung ở ba kiểu hệ thống: audit đã Việt hoá các dạng romaji cũ thành "Kíu/Kyaphù/Hya/Ưm" (10 key trùng audit); quy ước file "phù/phù a" cho họ fa/fu tách một âm thành mảnh rời; và "Ưm" nuốt mất phụ âm sau ん (んく/んむ/んぐ/んりゅ/んゆ/んひゅ).

## 3. Chi tiết từng dòng sửa (47 dòng)

### Key 780 (ポーレット)
- JP: `「クビレのところも、ぷにぷにも……こう、して――\nんっ――ぷ、ぁ。ツバもまぶして、ゆっくり、ゆっくり」`
- TW: `「下面的溝，彈彈的地方……也這樣——嗯——噗。抹上唾液，慢慢地、慢慢地——」`
- VN cũ: `「Chỗ rãnh, cả chỗ mềm mềm nữa……làm, thế này——\nưm——phù, a. Thoa thêm nước bọt, từ từ, từ từ thôi」`
- Sửa: `「Chỗ rãnh, cả chỗ mềm mềm nữa……làm, thế này—— ưm——Pu, a. Thoa thêm nước bọt, từ từ, từ từ thôi」`
- Lý do: ぷ、ぁ là một âm duy nhất bị tách thành hai mảnh "phù, a" — gộp romaji "Pu, a" (tiền lệ ふ、あ→"Fu, a").

### Key 786 (ポーレット)
- JP: `「やっ、らっ！　らめっ――これっ――ちんちん――\nあつくて――とけりゅっ――とけちゃうっ！」`
- TW: `「不要！不行——這樣——雞雞——好燙——要化了——我要化了！」`
- VN cũ: `「A, á! Không được——thế này——dương vật——\nnóng quá——tan chảy——tan chảy mất!」`
- Sửa: `「Ya, Ra! Không được——thế này——dương vật—— nóng quá——tan chảy——tan chảy mất!」`
- Lý do: やっ→"A" và らっ→"á" đều mất phụ âm mora (y-, r-) — "Ya, Ra" (tiền lệ h3: "Á" cho やっ là lỗi mất phụ âm).

### Key 808 (ポーレット)
- JP: `「ひあっ――あ――あっ――ん――ンムッ――はむうっ」`
- TW: `「呀——啊——啊——嗯——嗯——唔」`
- VN cũ: `「Hya——a——a——ưm——ưm——hàm」`
- Sửa: `「Hia——a——a——ưm——Nmu——Hamuu」`
- Lý do: ひあっ→"Hya" sai âm (ひあ≠ひゃ) → "Hia" (quy tắc 3b); ンムッ→"ưm" mất m → "Nmu" (tiền lệ reinah3: んむっ→"nmu"); はむうっ→"hàm" mất âm u cuối → "Hamuu".

### Key 809 (ポーレット)
- JP: `「ふやっ――あっ――お、おっぱいっ」`
- TW: `「呀——啊——奶、奶子」`
- VN cũ: `「Phuya——a——ng-ngực」`
- Sửa: `「Fuya——a——ng-ngực」`
- Lý do: ふやっ→"Phuya" — romaji "Fuya" (tiền lệ nhiều file: ふや→Fuya).

### Key 810 (ポーレット)
- JP: `「ひゅぁぁあああああああああああああああんっ！！！」`
- TW: `「呀啊啊啊啊啊！！！」`
- VN cũ: `「Hyaaaaaaaaaaaaaaaaaaaan!!!」`
- Sửa: `「Hyuaaaaaaaaaaaaaaaaan!!!」`
- Lý do: ひゅぁぁあ… (ぁ×2 + あ×15 = 17 a) bị dịch thành "Hya" + 20 a: mất glide u của ひゅ và đếm sai — "Hyu" + 17 a + "n".

### Key 811 (ポーレット)
- JP: `「ひゃううううううううんっ！！！！」`
- TW: `「呀啊啊啊啊啊！！！！」`
- VN cũ: `「Hyaaaaaaaaaan!!!!」`
- Sửa: `「Hyauuuuuuuun!!!!」`
- Lý do: ひゃう×8ん bị dịch bằng a ("Hyaaaaaaaaaan") thay vì u — "Hyauuuuuuuun" (8 u + n).

### Key 812 (ポーレット)
- JP: `「ひゃううううううううっ！！！？」`
- TW: `「呀啊啊啊啊！！！？」`
- VN cũ: `「Hyaaaaaaaaaa!!!?」`
- Sửa: `「Hyauuuuuuuu!!!?」`
- Lý do: ひゃう×8っ bị dịch bằng a ("Hyaaaaaaaaaa") thay vì u — "Hyauuuuuuuu" (8 u).

### Key 816 (ポーレット)
- JP: `「ひあっ！　あっ――めくれっ――んっ――ひっぱ――っ\n――あっ――おま、んこっ――ひっ――しゅご――んっ」`
- TW: `「呀！啊——被掀翻了——嗯——被拉出來了——啊——小穴——呀——好刺激——嗯」`
- VN cũ: `「Hya! A——bị lộn, ngược——ưm——bị kéo, ra——\n——a——âm, đạo——hi——dữ, dội——ưm」`
- Sửa: `「Hia! A——bị lộn, ngược——ưm——bị kéo, ra——Ư ——a——âm, đạo——hi——dữ, dội——ưm」`
- Lý do: ひあっ→"Hya" sai âm → "Hia" (quy tắc 3b). Giữ nguyên Ư gasp của audit (っ cuối đoạn 1).

### Key 818 (ポーレット)
- JP: `「ひあっ！　あっ！　はっ！　あっ！　ふあっ！\nあっ――んゆっ――ひゃふっ！！」`
- TW: `「呀！啊！啊！啊！呼啊！啊——嗯——呀啊！！」`
- VN cũ: `「Hya! A! Hà! A! Phù!\nA——ưm——hya!!」`
- Sửa: `「Hia! A! Hà! A! Fua! A——Nyu——hyafu!!」`
- Lý do: ひあっ→"Hia"; ふあっ→"Fua"; んゆっ→"ưm" mất y → "Nyu" (tiền lệ h8/mayami). Giữ "hyafu" của audit cho ひゃふっ.

### Key 820 (ポーレット)
- JP: `「ひあっ！　あっ！　あ！　しゅごっ――これっ――ん！\nおまんこ、ずりずり、こす、られ――てっ――んふっ！」`
- TW: `「呀！啊！啊！這樣好厲害——嗯！小穴——被摩擦到了——嗯！」`
- VN cũ: `「Hya! A! A! Dữ quá——thế này——ưm!\nÂm đạo, bị trượt, bị cọ, xát——ưm!」`
- Sửa: `「Hia! A! A! Dữ quá——thế này——ưm! Âm đạo, bị trượt, bị cọ, xát——ưm!」`
- Lý do: ひあっ→"Hya" sai âm → "Hia" (quy tắc 3b).

### Key 821 (ポーレット)
- JP: `「きゃふっ！　んくっ――あっ――やっ――はッ――\nんっ――きもち――きゃう――あ――きもち、いいっ」`
- TW: `「呀！嗯——啊——呀——呼——嗯——好舒服——啊——好舒服」`
- VN cũ: `「Kya! Ưm——a——á——hà——\nưm——sướng——kya——a——sướng, quá」`
- Sửa: `「Kyafu! Nku——a——Ya——hà—— ưm——sướng——Kyau——a——sướng, quá」`
- Lý do: きゃふっ→"Kyafu" (thay "Kyaphù" của audit — lai Việt–romaji); んくっ→"Nku" (tiền lệ h2 cùng route); やっ→"Ya"; きゃう→"Kyau" (bản cũ "kya" mất u).

### Key 824 (ポーレット)
- JP: `「ひゃ、んっ！　そこ――あうっ――つぶつぶ、する、\nとこ、べろ、べろ――され、た――らあっ！」`
- TW: `「呀！那裡——啊——粗糙的地方——被舔到的話——啊！」`
- VN cũ: `「Hya, ưm! Chỗ đó——a——chỗ, sần sùi,\nbị, liếm, láp——mất, rồi——a!」`
- Sửa: `「Hya, ưm! Chỗ đó——Au——chỗ, sần sùi, bị, liếm, láp——mất, rồi——Raa!」`
- Lý do: あうっ→"a" mất u → "Au" (tiền lệ); らあっ→"a" mất r → "Raa" (ら+あ = 2 a).

### Key 826 (ポーレット)
- JP: `「ひあっ！？　きゅ――きゅふうううんっ！！！」`
- TW: `「呀！？呀——呀啊啊啊！！！」`
- VN cũ: `「Hya!? Kyu——kyufuuuun!!!」`
- Sửa: `「Hia!? Kyu——kyufuuuun!!!」`
- Lý do: ひあっ→"Hia"; khôi phục romaji "Kyu——kyufuuuun" — audit đã Việt hoá thành "Kíu——kíphúuuun" (tiền lệ h8: audit Việt hoá thở La-tinh → moan hoàn lại romaji); giữ "kyufuuuun" viết thường như VN cũ/audit (phần tiếp nối của cùng một hơi sau ——). Đếm u đúng: きゅふうううん = 5 u.

### Key 828 (ポーレット)
- JP: `「やっ！？　やああんっ！　なんで、なんで双鉄くんっ、\n抜いちゃうのぉっ！」`
- TW: `「呀！？呀！為什麼，為什麼雙鐵君，怎麼拔出去了！」`
- VN cũ: `「Á!? Á a a! Sao, sao Anh Soutetsu lại,\nrút ra thế!」`
- Sửa: `「Ya!? Yaaan! Sao, sao Anh Soutetsu lại, rút ra thế!」`
- Lý do: やっ→"Ya"; やああんっ→"Á a a" mất n (và や→"Á" sai) → "Yaaan" (3 a + n).

### Key 830 (ポーレット)
- JP: `「ひゃううっ！？　――あっ――だめ――らめぇっ――\nクリ、まで――クリ、まで――押され――一当たっ、て」`
- TW: `「呀！？啊——不行——不行——陰蒂——也被壓到了——按到了」`
- VN cũ: `「Hya!? ——A——không được——không được đâu——\nđến cả, âm vật——đến cả, âm vật——cũng bị đè——bị chạm, vào rồi」`
- Sửa: `「Hyauu!? ——A——không được——không được đâu—— đến cả, âm vật——đến cả, âm vật——cũng bị đè——bị chạm, vào rồi」`
- Lý do: ひゃううっ→"Hya" mất cả 2 u → "Hyauu".

### Key 834 (ポーレット)
- JP: `「んきゅんっ！？　んっ――ふあっ！？　らめっ、\nイクっ！　ふあっ！　あっ！　あっ！　あっ！！」`
- TW: `「呀！？嗯——呼啊！？不行，丟了！不行！呼啊！啊！啊！啊！！！」`
- VN cũ: `「Ưm kyun!? Ưm——phù!? Không được,\nlên đỉnh mất! Phù! A! A! A!!」`
- Sửa: `「Nkyun!? Ưm——Fua!? Không được, lên đỉnh mất! Fua! A! A! A!!」`
- Lý do: んきゅんっ→"Nkyun" (thay "Ưm" của audit — tiền lệ nagih2 2395, h8); ふあっ→"Fua" ×2.

### Key 838 (双鉄)
- JP: `「く――あっ――あっ――おっ――」`
- TW: `「呃——啊——啊——啊——」`
- VN cũ: `「Ư——a——a——ô——」`
- Sửa: `「Ku——a——a——ô——」`
- Lý do: く――→"Ư" mất hẳn k → "Ku——" (tiền lệ 831 cùng file: く→"Ku"; dấu —— mang độ dài, không cộng thêm u).

### Key 839 (双鉄)
- JP: `「んくっ！」`
- TW: `「呃！」`
- VN cũ: `「Ưm!」`
- Sửa: `「Nku!」`
- Lý do: んくっ→"Ưm" mất k → "Nku" (tiền lệ h2 cùng route, mayami, nagih2).

### Key 843 (ポーレット)
- JP: `「はっ――やっ――ンッ――嬉しっ――嬉しいッ――」`
- TW: `「呼——呀——嗯——我好開心——好開心——」`
- VN cũ: `「Hà——á——ưm——Vui quá——vui quá đi——」`
- Sửa: `「Hà——Ya——ưm——Vui quá——vui quá đi——」`
- Lý do: やっ→"á" mất y → "Ya".

### Key 847 (ポーレット)
- JP: `「ぷ――あっ――ごくっ――ごくっ、ごくんっ――ごく」`
- TW: `「呼——啊——咕嚕——咕嚕——咕嚕」`
- VN cũ: `「Phù——a——ực——ực, ực——ực」`
- Sửa: `「Pu——a——ực——ực, ực——ực」`
- Lý do: ぷ――あっ bị tách "Phù——a" → romaji "Pu——a".

### Key 850 (ポーレット)
- JP: `「は……ぁ……ふ……ふあ……あ……\nすご……か……った……」`
- TW: `「呼……啊……呼……呼啊……啊……真刺激……」`
- VN cũ: `「Hà……a……phù……phù a……a……\ntuyệt……quá……đi……」`
- Sửa: `「Hà……a……phù……Fua……a…… tuyệt……quá……đi……」`
- Lý do: ふあ→"phù a" tách âm → "Fua".

### Key 851 (ポーレット)
- JP: `「ふぁ……んっ――」`
- TW: `「呼……嗯——」`
- VN cũ: `「Phù……ưm——」`
- Sửa: `「Fa……ưm——」`
- Lý do: ふぁ→"Phù" sai âm (ふぁ = fa, không phải fu) → "Fa" (Hepburn chặt).

### Key 853 (ポーレット)
- JP: `「ふあっ――あっ――あっ――双鉄くん――双鉄くぅん」`
- TW: `「呼啊——啊——啊——雙鐵君——雙鐵君」`
- VN cũ: `「Phù——a——a——Anh Soutetsu——Anh Soutetsu」`
- Sửa: `「Fua——a——a——Anh Soutetsu——Anh Soutetsu」`
- Lý do: ふあっ→"Phù" → "Fua".

### Key 854 (ポーレット)
- JP: `「ふあっ――あっ――やぁっ――なのおっ！　ずりずり、\nだけ――でっ！　セックス、なしで、イクの、やぁぁ！」`
- TW: `「呼啊——啊——我不要！我不想！不做愛——光是被摸一摸、就高潮——不要！」`
- VN cũ: `「Phù——a——a——không chịu đâu! Chỉ cọ xát,\nthôi——mà! Không quan hệ, mà lên đỉnh, không chịu đâu!」`
- Sửa: `「Fua——a——Yaa——không chịu đâu! Chỉ cọ xát, thôi——mà! Không quan hệ, mà lên đỉnh, không chịu đâu!」`
- Lý do: ふあっ→"Fua"; やぁっ→"a" mất y → "Yaa" (や+ぁ = 2 a). Yaぁぁ cuối dòng chìm trong diễn nghĩa "không chịu đâu" — giữ nguyên, cờ F6.

### Key 856 (ポーレット)
- JP: `「ゅはぁぁぁぁぁぁあああああああんっ！！！」`
- TW: `「呼啊啊啊啊啊啊！！！」`
- VN cũ: `「Yuhaaaaaaaaaaaaaaaan!!!」`
- Sửa: `「Yuhaaaaaaaaaaaaaan!!!」`
- Lý do: ゅはぁ×6あ×7ん = 14 a sau "Yuh"; bản cũ viết 16 a → "Yuh" + 14 a + "n".

### Key 858 (ポーレット)
- JP: `「ふあっ！　あっ――ひっ――あっ――しきゅう――\nばちゅって――あついの――あたっ、って――はきゅ！」`
- TW: `「呼啊！啊——呀——啊——子宮——射到了——燙燙的——打到了——啊！」`
- VN cũ: `「Phù! A——hi——a——tử cung——\nbị bắn, trúng——nóng, quá——đập, vào——hakyu!」`
- Sửa: `「Fua! A——hi——a——tử cung—— bị bắn, trúng——nóng, quá——đập, vào——hakyu!」`
- Lý do: ふあっ→"Phù" → "Fua".

### Key 860 (ポーレット)
- JP: `「いっ――きゅううううううううううううぅぅんっ！！」`
- TW: `「咿——嗯啊啊啊啊啊！！」`
- VN cũ: `「I——kyuuuuuuuuuuuuuuuuuun!!」`
- Sửa: `「I——Kyuuuuuuuuuuuuuuun!!」`
- Lý do: きゅう×12ぅ×2ん = 15 u; bản cũ viết 18 u, audit Việt hoá "Kíuuuu…" → khôi phục romaji "Ky" + 15 u + "n".

### Key 862 (ポーレット)
- JP: `「ふえっ！？」`
- TW: `「哎！？」`
- VN cũ: `「Hể!?」`
- Sửa: `「Fue!?」`
- Lý do: ふえっ→"Hể" diễn nghĩa, sai âm → "Fue" (tiền lệ ふぇ→"Fue").

### Key 867 (ポーレット)
- JP: `「ァ――はっ――――んぐっ！」`
- TW: `「啊——呼——嗯！」`
- VN cũ: `「A——hà――――ưm!」`
- Sửa: `「A——hà――――Ngu!」`
- Lý do: んぐっ→"ưm" mất g → "Ngu" (tiền lệ reinah3: んぐうっ→"nguu").

### Key 872 (ポーレット)
- JP: `「あんむっ――んっ――ちゅっ――ちゅううっ――\nちゅずっ――れろっ――れるうっ――ちゅるっ！」`
- TW: `「啊——嗯——啾——啾嚕——啾嚕——啾嚕——啾噗——啾噗！」`
- VN cũ: `「A ưm——ưm——chụt——chụt——\nchụt——rộp——rộp——chụt!」`
- Sửa: `「Anmu——ưm——chụt——chụt—— chụt——rộp——rộp——chụt!」`
- Lý do: あんむっ→"A ưm" tách âm → "Anmu".

### Key 873 (双鉄)
- JP: `「く……あ――――あっ……は……はぁ……あ――」`
- TW: `「啊……啊——啊……呼……呼……啊——」`
- VN cũ: `「Ư……a――――a……hà……hà……a――」`
- Sửa: `「Ku……a――――a……hà……hà……a――」`
- Lý do: く……→"Ư" mất k → "Ku……" (tiền lệ 831 cùng file).

### Key 882 (ポーレット)
- JP: `「あっ！　あっ、あ、あっ！　っく――ふぁっ、ン！\nお、おしり――深い、のっ――んっ――やっ――あっ」`
- TW: `「啊！啊、啊、啊！嗯——嗯！屁、屁股裡——好深——嗯——呀——啊」`
- VN cũ: `「A! A, a, a! Ư——phù, ưm!\nM-mông——sâu, quá——ưm——a——a」`
- Sửa: `「A! A, a, a! Kku——Fa, ưm! M-mông——sâu, quá——ưm——Ya——a」`
- Lý do: っく――→"Ư" mất k → "Kku——" (Hepburn: っ nhân đôi k; phán đoán mới, cờ F10); ふぁっ→"Fa"; やっ→"Ya".

### Key 885 (ポーレット)
- JP: `「はっ！　あっ！　あっ！　あっ！　ひっ――ふあっ！\nそうてつ――く――ふっ――あ――そうてつ、くぅん」`
- TW: `「啊！啊！啊！啊！呀——呼啊！雙鐵——呼啊——雙鐵」`
- VN cũ: `「Hà! A! A! A! Hi——phù!\nAnh Soutetsu——ư——phù——a——Anh Soutetsu」`
- Sửa: `「Hà! A! A! A! Hi——Fua! Anh Soutetsu——ku——phù——a——Anh Soutetsu」`
- Lý do: ふあっ→"Fua"; く――→"ư" mất k → "ku——" (tiền lệ 831).

### Key 889 (ポーレット)
- JP: `「いうっ！？　あっ――おっぱい――乳首ッ――ひッ！\nぎゅって、されて――やんっ！　あっ――腰っ、ベロっ」`
- TW: `「啊！？啊——奶子——乳頭——呀！被按扁了！啊——腰那裡」`
- VN cũ: `「Iu!? A——ngực——nhũ hoa——hi!\nBị bóp chặt——á! A——eo, bị liếm」`
- Sửa: `「Iu!? A——ngực——nhũ hoa——hi! Bị bóp chặt——Yan! A——eo, bị liếm」`
- Lý do: やんっ→"á" mất y+n → "Yan".

### Key 898 (ポーレット)
- JP: `「ぁうっ！？」`
- TW: `「嗚！？」`
- VN cũ: `「Á!?」`
- Sửa: `「Au!?」`
- Lý do: ぁうっ→"Á" mất u → "Au" (tiền lệ).

### Key 899 (ポーレット)
- JP: `「んっ――きゃふっ――あっ！　かっ――き、きつ――っ\n――ンッ――はっ、あ――いきな、りっ――んうっ！」」`
- TW: `「嗯——呀——啊！啊——好粗——嗯——呼——啊——突然就——嗯！」」`
- VN cũ: `「Ưm——kya——a! C-chật, chật quá——\n——ưm——hà, a——đột ngột, quá——ưm!」`
- Sửa: `「Ưm——Kyafu——a! C-chật, chật quá—— ——ưm——hà, a——đột ngột, quá——ưm!」`
- Lý do: きゃふっ→"Kyafu" (thay "Kyaphù" của audit). Các gasp っ khác đã diễn đủ (sweep already-rendered, audit đồng ý).

### Key 901 (ポーレット)
- JP: `「ンンンっ――あっ――手、で――指、で――おっぱい、\nわたし、おっぱい――むにむに――いじられ、ふ、あ！」`
- TW: `「嗯——啊——我的奶——被手——被手指——按摩到了——啊！」`
- VN cũ: `「Ưm ưm ưm——a——bằng tay——bằng ngón tay——ngực,\ncủa em, ngực——mềm nhũn——bị sờ soạng, phù, a!」`
- Sửa: `「Ưm ưm ưm——a——bằng tay——bằng ngón tay——ngực, của em, ngực——mềm nhũn——bị sờ soạng, Fu, a!」`
- Lý do: ふ、あ→"phù, a" tách âm → "Fu, a".

### Key 903 (ポーレット)
- JP: `「んりゅ――れりゅっ――ぞりゅっ――ちゅるんっ！」`
- TW: `「嗯——啾嚕——啾嚕——啾噗！」`
- VN cũ: `「Ưm——rộp——rộp——chụt!」`
- Sửa: `「Nryu——rộp——rộp——chụt!」`
- Lý do: んりゅ――→"Ưm" mất hẳn りゅ → "Nryu" (phán đoán mới cùng họ ん+phụ âm gộp romaji; cờ F10).

### Key 905 (ポーレット)
- JP: `「んっ――んむっ――ちゅっ――ちゅうう――ジュル――\nあむっ――ちゅうっ――チュッ――ちゅるるう――じゅ」`
- TW: `「嗯——嗯——啾——啾嚕——啾嚕——嗯——啾——啾嚕——啾噗——啾噗」`
- VN cũ: `「Ưm——ưm——chụt——chụt——rột——\nưm——chụt——chụt——chụt——chụt」`
- Sửa: `「Ưm——Nmu——chụt——chụt——rột—— Amu——chụt——chụt——chụt——chụt」`
- Lý do: んむっ→"Nmu"; あむっ→"ưm" mất a → "Amu" (tiền lệ).

### Key 912 (ポーレット)
- JP: `「ん……っっ――ふぁ――あっ――ずぼ、ずぼ――んっ、\nされ、ると――ひ――あ――あつい、の――たまっ、て」`
- TW: `「嗯……嗯——呼——啊——被捅到的話——呀——熱——熱熱的——就攢起來了」`
- VN cũ: `「Ưm……ư——phù——a——thọc, thọc——ưm,\nbị, thế——hi——a——nóng, quá——tích tụ, lại」`
- Sửa: `「Ưm……ưư——Fa——a——thọc, thọc——ưm, bị, thế——hi——a——nóng, quá——tích tụ, lại」`
- Lý do: ふぁ――→"Fa" (giữ "ưư" của audit cho ん……っっ).

### Key 918 (ポーレット)
- JP: `「んきゅんっ！！！」`
- TW: `「嗯呀！！！」`
- VN cũ: `「Ưm kyun!!!」`
- Sửa: `「Nkyun!!!」`
- Lý do: んきゅんっ→"Nkyun" (thay "Ưm" của audit — tiền lệ nagih2, h8).

### Key 920 (ポーレット)
- JP: `「んひゅっんっ！！？　ふわっ！？　そ、双鉄くん\nこれっ！　あのっ！！」`
- TW: `「嗯呀！！？哇！？雙、雙鐵君，這樣！那個！！」`
- VN cũ: `「Ưm hyun!!? Oa!? A-Anh Soutetsu\ncái này! Cái đó!!」`
- Sửa: `「Nhyun!!? Fuwa!? A-Anh Soutetsu cái này! Cái đó!!」`
- Lý do: んひゅっんっ→"Nhyun" (quy tắc 3b: んひゅ→Nhyu/Nhyun); ふわっ→"Fuwa" (tiền lệ fukamih3).

### Key 921 (ポーレット)
- JP: `「んきゅっ！　ふああっ！！！」`
- TW: `「嗯啊！呼啊！！！」`
- VN cũ: `「Ưm kyu! Phù a!!!」`
- Sửa: `「Nkyu! Fuaa!!!」`
- Lý do: んきゅっ→"Nkyu"; ふああっ→"Fuaa" (ふあ+あ = 2 a).

### Key 930 (ポーレット)
- JP: `「んむっ！？　んっ――ふぷっ――ん、んっ――\nこくっ！　ごくっ――ごくっ――ごくんっ！」`
- TW: `「嗯！？嗯——呼——嗯——咕嚕！咕嚕——咕嚕——咕嚕！」`
- VN cũ: `「Ưm!? Ưm——phù——ưm, ưm——\nực! Ực——ực——ực!」`
- Sửa: `「Nmu!? Ưm——Fupu——ưm, ưm—— ực! Ực——ực——ực!」`
- Lý do: んむっ→"Nmu"; ふぷっ→"phù" mất ぷ → "Fupu" (phán đoán mới cùng họ mất phụ âm; cờ F10).

### Key 936 (ポーレット)
- JP: `「うふふっ……おつゆ、出てきたってことは――\nマッサージで……少しはおちんちん、楽になって――」`
- TW: `「嘻嘻……既然汁液出來了——說明我的按摩……讓雞雞放鬆一點了」`
- VN cũ: `「Ư hự hự……tiết nước ra rồi, nghĩa là——\nmassage……đã làm dương vật, thoải mái hơn chút——」`
- Sửa: `「Ufufu……tiết nước ra rồi, nghĩa là—— massage……đã làm dương vật, thoải mái hơn chút——」`
- Lý do: うふふっ là tiếng cười, không phải rên — "Ư hự hự" diễn thành tiếng rên → "Ufufu" (quy tắc Hieu 19/11; tiền lệ h8).

### Key 939 (ポーレット)
- JP: `「うふふっ、でしたね。双鉄くん」`
- TW: `「嘻嘻，是啊，雙鐵君」`
- VN cũ: `「Ư hự hự, đúng vậy nhỉ. Anh Soutetsu」`
- Sửa: `「Ufufu, đúng vậy nhỉ. Anh Soutetsu」`
- Lý do: Như 936: うふふっ → "Ufufu".

### Key 965 (ポーレット)
- JP: `「そこまで、ちゃあんとマッサージ。\nわたし、ですから――頑張りますね――あーーんむっ！」`
- TW: `「我會認真按摩。我會努力的，所以——！」`
- VN cũ: `「Sẽ massage, đàng hoàng cho đến lúc đó.\nVì là em, nên——em sẽ cố gắng——a——ưm!」`
- Sửa: `「Sẽ massage, đàng hoàng cho đến lúc đó. Vì là em, nên——em sẽ cố gắng——Aaanmu!」`
- Lý do: あーーんむっ→"a——ưm" tách âm → "Aaanmu" (あ+ー+ー = 3 a, + nmu).

## 4. Các dòng rên đã giữ (ghi chú đáng kể)

- **Gasp Ư đã đúng (không đụng)**: 6 fix Ư của sweep/audit (1233, 1270, 1271, 1285, 1331, 1380); 879 っ!→"A!" (sweep already-rendered, audit đồng ý); 924 っ!→"Ư!"; 912 "Ưm……ưư" (audit thêm đủ 2 っ); 816 "——Ư " (audit thêm gasp cuối đoạn 1).
- **Romaji đã đúng**: 824 "Hya", 831 く→"Ku" + くひっ→"kuhi", 807 くひっ→"Kuhi", 822 あひゅん→"Ahyun", 881 ひきゅっ→"Hikyu", 858 はきゅ→"hakyu", 897 はうっ→"Hau" (audit note: khớp dấu câu JP), 914 ぉお→"Ồ", 942 ぉぅっ→"Ồ", 917 む→"Ưm".
- **Thở dài/ngắn giữ nguyên**: 849 はぁ→"Hà……" (dấu …… mang độ dài); 873 はぁ→"hà……" (như 849); 815 ふううっ→"Phù——" (dấu —— mang độ dài); 572 すぅ→"Su……" (ngủ, dấu …… mang độ dài); 845 はっ→"Hà" (ngắn, đúng 1 a).
- **Cười đã đúng**: 941 えへへっ→"ê hế hế" (tiếng cười diễn thành tiếng cười, tự nhiên).
- **SFX trong ngoặc (đã dịch thành động từ Việt, đúng — tiền lệ h8)**: toàn bộ khối độc thoại — 1684/1701 "Thọc sâuuuuuuuu" (audit), 1651 "Chúuuuuuuuuuut!" (audit), 1648/1665 "Cộp!", 1659/1660/1662 "Phụt!", 1672 "Thọc——thọc——tuột——phụt!", 1692 "Liếm", 1695 "Siết! Siết chặt!!", 1702 "Co giật! Run rẩy!!", 1688 "Thọc——vào——sâu——hơn——", 1647 "Lắc——nhóp——nhóp nhép! Xoa nắn!", 1664 "Nhóp nhép!", 1666 "Thọc——rút——", 1676/1690 "Rột!". Riêng 1690 れろっ→"Liếm" (khác "rộp" ở thoại) là đúng quy ước theo ngữ cảnh: trong khối （ ） SFX dùng động từ, trong thoại dùng tiếng rên — như 1692 れるううううっ→"Liếm".
- **ふっ→"phù" giữ** (783, 814, 815, 845, 869, 877): hơi thở ngắn "fu", diễn Việt tự nhiên, không ngượng — cờ F7 (Fu vs phù chưa chốt toàn dự án).
- **Họ ちゅ/じゅ → "chụt" giữ** (894, 895, 905, 911, 872): quy ước file, đã cờ toàn dự án (h3 dùng "chụụt/chumu") — cờ F5.
- **んぷっ→"Ưm" giữ** (859, 928): theo fukamih3 (F3) + reinah-tsuika (giữ "Ưm" cho んぷっ trong chuỗi nuốt) — cờ F2.
- **んうっ→"ưm" giữ** (877, 927; 899 んうっ→"ưm"): thông lệ nhiều file — cờ F3.
- **んふっ→"ưm" giữ** (837, 820): chờ quyết "Nfu" — cờ F3 (fukamih3 F2).
- **Diễn nghĩa giữ nguyên**: 837 なっ→"Gì", 889 ベロっ→"bị liếm", 820 しゅごっ→"Dữ quá", 786/830 らめっ→"Không được", 875/797 しゅきっ/ふう→"thích quá"/"như thế nào" (từ, không phải rên), 787 ううん→"Không!", 854 やぁぁ cuối dòng chìm trong "không chịu đâu" (F6), 899 かっ――→"C-" (F4).
- **Không phải rên (nói lắp/ngập ngừng, giữ)**: 1024, 915, 573, 945, 1010, 933, 1023, 865, 866, 1021, 958, 1022, 993.

## 5. Ghi chú cho đợt thống nhất (10 fix thay thế fix audit + 10 cờ)

10 fix dưới đây **đã gộp bản sửa của audit** — đợt thống nhất phải áp dụng **giá trị moan** này thay cho giá trị audit cho cùng key, không áp cả hai: 816 (Hia + Ư của audit), 818 (Hia/Fua/Nyu + hyafu của audit), 821 (Kyafu/Nku/Ya/Kyau thay Kyaphù của audit), 826 (khôi phục romaji thay "Kíu——kíphúuuun" của audit), 834 (Nkyun/Fua thay "Ưm" của audit), 860 (khôi phục romaji thay "Kíuuuu…" của audit), 899 (Kyafu thay Kyaphù), 912 (Fa + ưư của audit), 918 (Nkyun thay "Ưm"), 921 (Nkyu/Fuaa thay "Ưm").

- **F1 — họ く**: "Ku/Kuu/Kku" (838, 873, 882, 885 + 831 cùng file) vs "Hự" (900 cùng file, h8 くっ→"Hự") vs "Ư". Cần quyết một dạng toàn dự án; giá trị moan dùng "Ku" (Hepburn + tiền lệ trong file).
- **F2 — ん+phụ âm tắc/mũi**: romaji gộp "Nku/Nmu/Ngu/Nryu" (839, 867, 872, 903, 905, 930, 965) vs "Ưm" (h6 giữ "ưm" cho んくっ; fukamih3 giữ んぷっ→"Ưm" + flag; reinah-tsuika giữ んぷっ→"Ưm"). File này: んぷっ (859, 928) GIỮ "Ưm", các cụm còn lại dùng romaji gộp theo h2/mayami/nagih2/reinah3. Cần quyết một dạng toàn dự án.
- **F3 — んうっ/んふっ → "ưm"**: giữ nguyên (877, 927, 899, 837, 820); "ưm ư"/"Nu"/"Nfu" còn treo (fukamih3 F2/F7).
- **F4 — 899 かっ――**: gasp かっ có được diễn đủ bằng "C-" trong "C-chật" không, hay cần "Ka"? Audit + sweep đều xếp already-rendered; giữ nguyên, hỏi đợt thống nhất.
- **F5 — họ ちゅ/じゅ dài**: file dùng "chụt" cho cả ちゅうっ/ちゅるうっ/じゅううううっ (894, 895, 905, 911, 872) vs h3 "chụụt/chumu" — đã cờ toàn dự án; giữ quy ước file.
- **F6 — 854 やぁぁ cuối dòng**: chìm trong diễn nghĩa "không chịu đâu" ("mà lên đỉnh, không chịu đâu!") — không thay token được (tiền lệ flag file khác: や/やぁ chìm trong diễn nghĩa); giữ nguyên.
- **F7 — ふっ→"phù" vs "Fu"**: giữ "phù" (783, 814, 815, 845, 869, 877) theo h8; chưa chốt toàn dự án.
- **F8 — SFX （ ） dài**: 1696 (じゅるるるるうううう…→"Rột rột rột"), 1649/1650 (じゅぶううっ→"Chụt") — audit không sửa; thuộc phạm vi SFX của audit, ghi để audit loop xem lại độ dài.
- **F9 — 912 ひ――あ――**: giữ "hi——a——" (audit giữ; dấu —— tách đúng như JP) — không phải ひあ gộp, không áp quy tắc 3b.
- **F10 — phán đoán mới lần đầu trong dự án ở file này**: 903 んりゅ→"Nryu", 930 ふぷっ→"Fupu", 882 っく→"Kku" — cần parent kiểm chứng.

## 6. Lượt soát 2 + khối TOML

- Lượt soát 2: đọc lại toàn bộ 47/47 giá trị fix đối chiếu JP (+TW) — **47 re-verified, 0 bị loại, 3 được sửa**: 838 "Kuu——"→"Ku——", 882 "Kkuu——"→"Kku——", 903 "Nryuu——"→"Nryu——" (lỗi đếm: dấu —— chỉ mang độ dài, không cộng thêm nguyên âm như mora う/あ thật — chỉ các mora う/あ/ぁ/ぅ mới được đếm).
- Đếm nguyên âm kiểm chứng độc lập (bằng script, sau lượt soát 2): 810 "Hyu"+17a, 811 "Hya"+8u, 812 "Hya"+8u, 826 "kyufuuuun" 5u, 828 "Yaaan" 3a, 830 "Hyauu" 2u, 856 "Yuh"+14a, 860 "Ky"+15u — tất cả khớp JP.
- JSON: `moan-paulette-h7-zangyou-ecchi-mo-y-shatsu-de-wrong.json` — 47 mục, khóa dạng string, jp/tw/old_vn khớp CSV3 tuyệt đối 47/47 (1 bộ duy nhất, 326 dòng), không fix nào trùng old_vn, mọi fix chỉ khác old_vn ở đúng token rên cần sửa (+ chuẩn hoá `\n`→khoảng trắng theo quy ước audit file này; 10 key trùng audit đã gồm giá trị audit — xem §5). Không fix nào chạm dòng gasp Ư của sweep/audit; không dòng "Kh" nào bị đổi (file không có). Không fix nào là đại từ/thuật ngữ/nghĩa/lệch vị trí.
- Khối TOML dưới đây: 47 khóa, đã parse kiểm chứng bằng tomllib, 0 sai lệch giá trị so với JSON.

```toml
[script]
"780" = "「Chỗ rãnh, cả chỗ mềm mềm nữa……làm, thế này—— ưm——Pu, a. Thoa thêm nước bọt, từ từ, từ từ thôi」"
"786" = "「Ya, Ra! Không được——thế này——dương vật—— nóng quá——tan chảy——tan chảy mất!」"
"808" = "「Hia——a——a——ưm——Nmu——Hamuu」"
"809" = "「Fuya——a——ng-ngực」"
"810" = "「Hyuaaaaaaaaaaaaaaaaan!!!」"
"811" = "「Hyauuuuuuuun!!!!」"
"812" = "「Hyauuuuuuuu!!!?」"
"816" = "「Hia! A——bị lộn, ngược——ưm——bị kéo, ra——Ư ——a——âm, đạo——hi——dữ, dội——ưm」"
"818" = "「Hia! A! Hà! A! Fua! A——Nyu——hyafu!!」"
"820" = "「Hia! A! A! Dữ quá——thế này——ưm! Âm đạo, bị trượt, bị cọ, xát——ưm!」"
"821" = "「Kyafu! Nku——a——Ya——hà—— ưm——sướng——Kyau——a——sướng, quá」"
"824" = "「Hya, ưm! Chỗ đó——Au——chỗ, sần sùi, bị, liếm, láp——mất, rồi——Raa!」"
"826" = "「Hia!? Kyu——kyufuuuun!!!」"
"828" = "「Ya!? Yaaan! Sao, sao Anh Soutetsu lại, rút ra thế!」"
"830" = "「Hyauu!? ——A——không được——không được đâu—— đến cả, âm vật——đến cả, âm vật——cũng bị đè——bị chạm, vào rồi」"
"834" = "「Nkyun!? Ưm——Fua!? Không được, lên đỉnh mất! Fua! A! A! A!!」"
"838" = "「Ku——a——a——ô——」"
"839" = "「Nku!」"
"843" = "「Hà——Ya——ưm——Vui quá——vui quá đi——」"
"847" = "「Pu——a——ực——ực, ực——ực」"
"850" = "「Hà……a……phù……Fua……a…… tuyệt……quá……đi……」"
"851" = "「Fa……ưm——」"
"853" = "「Fua——a——a——Anh Soutetsu——Anh Soutetsu」"
"854" = "「Fua——a——Yaa——không chịu đâu! Chỉ cọ xát, thôi——mà! Không quan hệ, mà lên đỉnh, không chịu đâu!」"
"856" = "「Yuhaaaaaaaaaaaaaan!!!」"
"858" = "「Fua! A——hi——a——tử cung—— bị bắn, trúng——nóng, quá——đập, vào——hakyu!」"
"860" = "「I——Kyuuuuuuuuuuuuuuun!!」"
"862" = "「Fue!?」"
"867" = "「A——hà――――Ngu!」"
"872" = "「Anmu——ưm——chụt——chụt—— chụt——rộp——rộp——chụt!」"
"873" = "「Ku……a――――a……hà……hà……a――」"
"882" = "「A! A, a, a! Kku——Fa, ưm! M-mông——sâu, quá——ưm——Ya——a」"
"885" = "「Hà! A! A! A! Hi——Fua! Anh Soutetsu——ku——phù——a——Anh Soutetsu」"
"889" = "「Iu!? A——ngực——nhũ hoa——hi! Bị bóp chặt——Yan! A——eo, bị liếm」"
"898" = "「Au!?」"
"899" = "「Ưm——Kyafu——a! C-chật, chật quá—— ——ưm——hà, a——đột ngột, quá——ưm!」"
"901" = "「Ưm ưm ưm——a——bằng tay——bằng ngón tay——ngực, của em, ngực——mềm nhũn——bị sờ soạng, Fu, a!」"
"903" = "「Nryu——rộp——rộp——chụt!」"
"905" = "「Ưm——Nmu——chụt——chụt——rột—— Amu——chụt——chụt——chụt——chụt」"
"912" = "「Ưm……ưư——Fa——a——thọc, thọc——ưm, bị, thế——hi——a——nóng, quá——tích tụ, lại」"
"918" = "「Nkyun!!!」"
"920" = "「Nhyun!!? Fuwa!? A-Anh Soutetsu cái này! Cái đó!!」"
"921" = "「Nkyu! Fuaa!!!」"
"930" = "「Nmu!? Ưm——Fupu——ưm, ưm—— ực! Ực——ực——ực!」"
"936" = "「Ufufu……tiết nước ra rồi, nghĩa là—— massage……đã làm dương vật, thoải mái hơn chút——」"
"939" = "「Ufufu, đúng vậy nhỉ. Anh Soutetsu」"
"965" = "「Sẽ massage, đàng hoàng cho đến lúc đó. Vì là em, nên——em sẽ cố gắng——Aaanmu!」"
```

## Kết bài

- File ポーレットh7_残業エッチもyシャツで: đọc 326/326 dòng, xét 208 dòng rên/SFX, sửa **47 dòng** (45 romaji + 2 cười), giữ 161 dòng, 10 cờ cho đợt thống nhất (§5).
- Lỗi rên tập trung ở ba kiểu hệ thống: audit Việt hoá romaji cũ (10 key), "phù/phù a" tách âm họ fa/fu (17 key có token fa/fu), và "Ưm" nuốt phụ âm sau ん (14 key có token ん-gộp).
- Sau file này tổng moan là 38 file / 925 dòng (cơ sở 37 file / 878 dòng + 47 file này — cơ sở đã kiểm chứng trực tiếp dòng tổng cuối của ROUTE-MOANS.md).
- Chi tiết đầy đủ: `moan-paulette-h7-zangyou-ecchi-mo-y-shatsu-de-REVIEW.md`; danh sách sửa: `moan-paulette-h7-zangyou-ecchi-mo-y-shatsu-de-wrong.json`.