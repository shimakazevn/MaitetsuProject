# Moan-fix review — ポーレットh3_誘惑アイスコーヒー.txt.toml (moan-paulette-h3-yuuwaku-ice-coffee)

## 1. Kiểm chứng file

- File: `ポーレットh3_誘惑アイスコーヒー.txt.toml` — route 03_Paulette, 279 dòng script.
- TOML md5 `884568f018ff870371ba906804c8651c` (UTF-8 BOM + CRLF, 577 dòng); không có bản trùng (md5 không nằm trong 11 nhóm trùng của dự án).
- CSV3: 1 bộ duy nhất, 279 dòng, 0 key trùng; VN TOML-2 khớp CSV3 279/279 sau chuẩn hóa `\n`/khoảng trắng (155 khác biệt thô chỉ ở `\n` bị TOML-2 dẹt thành khoảng trắng — đúng như audit đã ghi; 0 khác biệt thực chất).
- Audit: 69/279 sai (24,7%), 1 dòng chưa chắc chắn (1683); file lệch vị trí nặng nhất trong các file Paulette h (chuỗi xoay vòng nội bộ 45 dòng). Audit review: `audit-paulette-h3-temptation-iced-coffee-REVIEW.md`.
- Cơ sở tổng moan (tự kiểm chứng lại từ `moans/ROUTE-MOANS.md`): **8 file / 205 dòng**.

## 2. Kiểm kê rên/SFX

- Đã đọc 279/279 dòng (JP + TW + VN). Xét 139 dòng rên/SFX theo mẫu token rên (57 Paulette + 16 Soutetsu H + 66 độc thoại, gồm 26 dòng SFX độc thoại trong ngoặc).
- Đổi 37 dòng: 13 romaji + 7 đếm nguyên âm + 17 sai âm.
- Kiểu lỗi chính: (1) họ fa/fu bị Việt hoá "phù"/"Phù" (mất hẳn âm a của ふあ/ふぁ) trong chuỗi rên cao trào — về romaji theo quy tắc Hieu duyệt 21/11; (2) rên dài đếm nguyên âm sai — kéo dài bằng phụ âm t/m ("chụtttt", "liếmmmm", "Sụtttttttttt") thay vì nguyên âm, hoặc thiếu/thừa 1 âm; (3) sai âm: phụ âm đầu/cuối mora bị mất hẳn ("Á" cho きゃっ/ひゃっ/やっ, "Ư" cho くっ, "chu" cho ちゅむっ/ちゅばっ/ぢゅぶっ).
- Giữ 102 dòng rên/SFX (xem §4).
- Sweep: 7 mục đã kiểm chứng trực tiếp trong `sweep-raw-gasp-wrong.json` — 6 bản sửa gasp Ư của audit (907, 908, 934, 935, 954, 1639) đã áp đúng giá trị, KHÔNG đụng dòng nào; 1 already-rendered (994) đồng ý giữ. Không có dòng "Kh" nào trong file (mọi "kh" tìm được đều là chữ Việt thường: không/khăn/khi...), nên không có dòng "Kh" nào bị đổi.

## 3. Các dòng sửa

### 3a. Romaji (13 dòng)

#### 897 — ポーレット — romaji (fa/fu + ya)
- JP: `「や……あっ――おしり……ふあっ――\n自分で……さわった、こと……ない……けどっ――」`
- TW: `「呀……啊——屁股……呼啊——我自己……雖然……沒摸過——」`
- Cũ: `「Á……a——mông……phù——\nBản thân em……chưa từng……chạm vào……nhưng——」`
- Mới: `「Ya……a——mông……Fua——\nBản thân em……chưa từng……chạm vào……nhưng——」`
- Lý do: や…… → "Ya" (mất y, xem §3c); ふあっ → "Fua" (bản cũ "phù" chỉ diễn ふ, mất hẳn âm a; họ fa/fu về romaji theo quy tắc 21/11, tiền lệ h9/kisaki h3).

#### 915 — ポーレット — romaji (fa/fu + đếm âm)
- JP: `「ふぁっ――あっ――ハァッ――あっ――」`
- TW: `「呼啊——啊——呼——啊——」`
- Cũ: `「Phù——a——hà——a——」`
- Mới: `「Fua——a——hàà——a——」`
- Lý do: ふぁっ → "Fua" (như 897); ハァッ = 2 âm a → "hàà" (bản cũ "hà" thiếu 1 âm).

#### 917 — ポーレット — romaji (fa/fu)
- JP: `「ふあっ――あっ――いっぱい――いっぱいっ――\nんっ、双鉄、くんの――精液――子宮――にっ――」`
- TW: `「呼啊——啊——好多——好多——雙鐵君的――精液――進到了子宮裡——」`
- Cũ: `「Phù——a——nhiều quá——nhiều quá——\nƯm, của anh Soutetsu——tinh dịch——vào trong, tử cung——rồi——」`
- Mới: `「Fua——a——nhiều quá——nhiều quá——\nƯm, của anh Soutetsu——tinh dịch——vào trong, tử cung——rồi——」`
- Lý do: ふあっ → "Fua" (bản cũ "phù" mất âm a).

#### 919 — ポーレット — romaji (fa/fu; key trùng audit)
- JP: `「ふあっ――あっ――ふか、いっ――これっ――\nんっ――すごい――おな、か――ささる、みたい、でっ」`
- TW: `「呼啊——啊——好深啊——這樣——嗯——好厲害——好像——刺到肚子裡」`
- Cũ (CSV3): `（Phập! Phập! Phập! Nhóp nhép!）` (lệch vị trí)
- Mới: `「Fua——a——sâu, quá——thế này——\nƯm——sướng quá——cảm giác, như đâm, vào tận bụng, vậy」`
- Lý do: xây trên giá trị audit ("Phù——a——..."), chỉ đổi token rên ふあっ――あっ―― → "Fua——a——" (tiền lệ h9: "phù a" tách nhịp trong chuỗi rên cao trào cũng về romaji).

#### 937 — ポーレット — romaji (fa/fu; key trùng audit)
- JP: `「ぁっ――双鉄くん、のっ――いつも、よりっ――\nふあっ――ふと、くてっ――めくれ、てっ――あっ」`
- TW: `「啊——你的——比平常——呼啊——還要粗大——在裡面挖著——啊」`
- Cũ (CSV3): `Dù vậy, hông tôi vẫn không dừng lại.` (lệch vị trí)
- Mới: `「A——của anh Soutetsu——to hơn, bình thường——\nFua——to, quá——bị nong rộng, ra——a」`
- Lý do: xây trên giá trị audit, chỉ đổi ふあっ → "Fua" (bản audit "Phù——" mất âm a).

#### 940 — ポーレット — romaji (fa/fu)
- JP: `「あっ――んっ――ふあっ――そ、双鉄、くんっ――\nわたし――わたしっ――あのっ――」`
- TW: `「啊——嗯——呼啊——雙、雙鐵君——我——我——那個——」`
- Cũ: `「A——ưm——phù——a, anh Soutetsu——\nEm——em——chuyện đó——」`
- Mới: `「A——ưm——Fua——a, anh Soutetsu——\nEm——em——chuyện đó——」`
- Lý do: ふあっ → "Fua" (bản cũ "phù" mất âm a).

#### 948 — ポーレット — romaji (pua + đếm âm)
- JP: `「あ……んっ――んむっ――ごくっ――んんんっ――\nぷあっ――はぁっ！　はぁああっ！」`
- TW: `「啊……嗯——嗯——咕嚕——嗯——呼啊——呼啊！呼啊！」`
- Cũ: `「A……ưm——ưm——ực——ưm——\nPhù——hà! Hààà!」`
- Mới: `「A……ưm——ưm——ực——ưm——\nPua——hàà! Hàààà!」`
- Lý do: ぷあっ → "Pua" (bản cũ "Phù" diễn thành ふ, sai hẳn phụ âm p; tiền lệ kisaki h3 2207 ぷぁ → "Pua"); はぁっ = 2 âm a → "hàà" (bản cũ thiếu 1); はぁああっ = 4 âm a → "Hàààà" (bản cũ "Hààà" thiếu 1).

#### 950 — ポーレット — romaji (fa/fu)
- JP: `「あっ……きもちいい……きもちいい……よぉ……\nふあっ――双鉄、くんの――おちん、ちんっ――あっ」`
- TW: `「啊……好舒服……好舒服啊…………呼啊――雙鐵君的——雞雞——啊」`
- Cũ: `「A……sướng quá……sướng quá……anh ơi……\nPhù——của, anh Soutetsu——dương, vật——a」`
- Mới: `「A……sướng quá……sướng quá……anh ơi……\nFua——của, anh Soutetsu——dương, vật——a」`
- Lý do: ふあっ → "Fua" (bản cũ "phù" mất âm a). "anh ơi" cho よぉ…… giữ nguyên (xưng hô, không thuộc moan).

#### 966 — ポーレット — romaji (rên dài + chumu)
- JP: `「ちゅっ――ちゅむっ――ぺろっ――れろおおおっ」`
- TW: `「啾嚕——啾嚕——啾嚕——啾嚕嚕」`
- Cũ: `「Chụt——chu——liếm——liếmmmm」`
- Mới: `「Chụt——chumu——liếm——Reroooo」`
- Lý do: ちゅむっ → "chumu" (xem §3c); れろおおおっ = 4 âm o (1+3) → "Reroooo" (bản cũ "liếmmmm" kéo dài bằng phụ âm m, sai hình âm; tiền lệ h9 2122 れるううううっ → "reruuuuu").

#### 968 — ポーレット — romaji (rên dài)
- JP: `「れるうううううっ！」`
- TW: `「啾嚕嚕！」`
- Cũ: `「Liếmmmmm!」`
- Mới: `「Reruuuuuu!」`
- Lý do: れるうううううっ = 6 âm u (1+5) → "Reruuuuuu" (bản cũ kéo dài bằng m; tiền lệ h9 2122).

#### 974 — ポーレット — romaji (rên dài + đếm âm)
- JP: `「んっ――ちゅるっ――ちゅろ――ちゅっ――\nすうっ――　！　――ずろぉぉぉぉぉぉっ！！！」`
- TW: `「嗯——啾嚕——啾嚕——啾啾——吸溜！吸溜！！！」`
- Cũ: `「Ưm——chụt——chụt——chụt——\nSụt——!——Sụtttttt!!!」`
- Mới: `「Ưm——chụt——chụt——chụt——\nSuụt——!——Zurooooooo!!!」`
- Lý do: すうっ = 2 âm u → "Suụt" (bản cũ "Sụt" thiếu 1); ずろぉぉぉぉぉぉっ = 7 âm o (1+6) → "Zurooooooo" (bản cũ "Sụtttttt" sai cả nguyên âm u/o lẫn kéo dài bằng t).

#### 977 — ポーレット — romaji (pua)
- JP: `「ん……ねちゅっ――ん――く――ぷぁ。おいし。\nけど……ミルクがあれば、もっとおいしい気がします」`
- TW: `「嗯……啾——嗯——咕。真好喝。但是……要是有牛奶的話，一定就更好喝了」`
- Cũ: `「Ưm……nhóp nhép——ưm——ực——phù. Ngon quá.\nNhưng mà……em nghĩ nếu có thêm sữa thì sẽ ngon hơn nữa.」`
- Mới: `「Ưm……nhóp nhép——ưm——ực——Pua. Ngon quá.\nNhưng mà……em nghĩ nếu có thêm sữa thì sẽ ngon hơn nữa.」`
- Lý do: ぷぁ → "Pua" (bản cũ "phù" diễn thành ふ, sai phụ âm p; như 948).

#### 1070 — ポーレット — romaji (fa/fu)
- JP: `「双鉄、くん、も――んっ――もう――こんなにっ――\n固く、て――あつく、て――ふあっ――」`
- TW: `「雙鐵君——嗯——你已經——這麼硬——這麼燙了——呼啊——」`
- Cũ: `「Anh Soutetsu, cũng——ưm——đã——thế này rồi——\nCứng, quá——nóng, quá——phù——」`
- Mới: `「Anh Soutetsu, cũng——ưm——đã——thế này rồi——\nCứng, quá——nóng, quá——Fua——」`
- Lý do: ふあっ → "Fua" (bản cũ "phù" mất âm a).

### 3b. Đếm nguyên âm (7 dòng)

#### 899 — ポーレット — đếm nguyên âm (key trùng audit)
- JP: `「ひゃああああああんっ！！」`
- TW: `「呀啊！！」`
- Cũ (CSV3): `（Siếttttttt!）` (lệch vị trí)
- Mới: `「Hyaaaaaaan!!」`
- Lý do: xây trên giá trị audit "Hyaaaaaaa!!" — đếm lại độc lập: JP có 7 âm a (ひゃ + あ×6) và 1 âm ん cuối; giá trị audit đếm đúng 7 a nhưng bỏ mất ん → thêm "n" cuối. (Xem cờ 4.)

#### 920 — ポーレット — đếm nguyên âm
- JP: `「ふぃぁぁあああああああああっ！！！」`
- TW: `「呼啊啊啊！！！」`
- Cũ: `「Phiaaaaaa!!!」`
- Mới: `「Phiaaaaaaaaaaa!!!」`
- Lý do: JP có 11 âm a (ぁ×2 + あ×9) → "Phi" + 11 a (bản cũ chỉ 6 a).

#### 923 — ポーレット — đếm nguyên âm
- JP: `「ずりゅうううううううううううっっ！！！」`
- TW: `「咕嚕！！！」`
- Cũ: `「Sụtttttttttt!!!」`
- Mới: `「Sụụụụụụụụụụụụt!!!」`
- Lý do: JP có 12 âm u (りゅ + う×11) → "S" + 12 ụ + "t" cho っ (bản cũ kéo dài bằng 10 phụ âm t, sai hình âm; tiền lệ lr_h1 1711 じゅぶううううっ → "Phậậậậập" 5 nguyên âm + phụ âm cuối). [Parent sửa 21/11 ~11:15: agent đếm thiếu 1 — JP có 11 chữ う, không phải 10; công thức 1+11=12.]

#### 927 — ポーレット — đếm nguyên âm
- JP: `「いっ――あっああああああああああああんっ！！」`
- TW: `「咿——啊啊啊啊！！」`
- Cũ: `「Í——a á a a a a a a a a a a!!」`
- Mới: `「Í——a á a a a a a a a a a a an!!」`
- Lý do: JP có 13 âm a + 1 âm ん cuối; bản cũ có 12 âm a và bỏ mất ん → thêm 1 âm a và "n" cuối.

#### 931 — ポーレット — đếm nguyên âm
- JP: `「はむっ――ちゅっ――ちゅううっ――ちゅっ！\nちゅばっ！　ちゅろっ！　ちゅうっ！　れろっ！」`
- TW: `「唔——啾嚕——啾嚕——啾嚕！啾噗！啾嚕！啾嚕！啾嚕！」`
- Cũ: `「Ngoạm——chụt——chụtttt——chụt!\nChu! Chụt! Chụtttt! Liếm!」`
- Mới: `「Ngoạm——chụt——chụụụt——chụt!\nChuba! Chụt! Chụụt! Liếm!」`
- Lý do: ちゅううっ = 3 âm u → "chụụụt", ちゅうっ = 2 âm u → "chụụt" (bản cũ kéo dài bằng t); ちゅばっ → "Chuba" (xem §3c). Giữ "chụt" cho ちゅっ/ちゅろっ và "Liếm" cho れろっ theo quy ước của file.

#### 933 — ポーレット — đếm nguyên âm
- JP: `「あむっ――ん――ちゅぶっ――ちゅるっ――\nぺろっ――れるっ――れろろっ――ちゅううっ」`
- TW: `「唔——嗯——啾嚕——啾嚕——啾嚕——啾嚕——啾嚕——啾嚕」`
- Cũ: `「Ngoạm——ưm——chu——chụt——\nliếm——liếm——liếm——chụtttt」`
- Mới: `「Ngoạm——ưm——chubu——chụt——\nliếm——liếm——liếm——chụụụt」`
- Lý do: ちゅぶっ → "chubu" (mất ぶ, xem §3c); ちゅううっ = 3 âm u → "chụụụt" (bản cũ kéo dài bằng t). Giữ "liếm" cho ぺろっ/れるっ/れろろっ theo quy ước của file.

#### 942 — ポーレット — đếm nguyên âm
- JP: `「はむっ――んっ――ん～～っ――\nれるっ、れろっ――ちゅむつ――ちゅうっ」`
- TW: `「啊——嗯——嗯～～啾嚕、啾嚕——嗯——啾嚕」`
- Cũ: `「Ngoạm——ưm——ưm～～\nliếm, liếm——chu——chụt」`
- Mới: `「Ngoạm——ưm——ưm～～\nliếm, liếm——chumu——chụụt」`
- Lý do: ちゅむつ → "chumu" (xem §3c; つ cuối là ngắt âm, diễn như ちゅむっ); ちゅうっ = 2 âm u → "chụụt" (bản cũ "chụt" thiếu 1 âm).

### 3c. Sai âm (17 dòng)

Quy tắc chung cho nhóm này (theo Hieu 19/11 22:19 — giữ càng gần tiếng Nhật gốc càng tốt; và "không để mất âm"): một mora phụ âm bị mất hẳn trong bản Việt là sai âm, sửa bằng romaji giữ nguyên hình âm. Ngược lại, "chụt" cho ちゅっ/ちゅるっ/ちゅろっ/ずちゅっ/じゅっ/じゅるっ được giữ (quy tắc họ ちゅ của h5 + quy ước của file — ず/じ/ぢ chỉ là biến thể hữu thanh của cùng âm đầu, còn む/ば/ぼ/ぶ là mora coda riêng biệt).

#### 890 — ポーレット — sai âm (key trùng audit)
- JP: `「やっっ――あっ――ンッッ――わたしの、アナ、ル――\n双鉄、くんに――広げ……られ、て――んうっっ――」`
- TW: `「呀——啊——嗯——我的屁眼——被你撐開了——嗯——」`
- Cũ (CSV3): `Tôi kéo nhẹ phần thịt xung quanh,\nnong rộng lỗ hậu dễ thương ra một chút.` (lệch vị trí)
- Mới: `「Ya——a——ưm——lỗ, hậu, của em——\nBị anh Soutetsu——nong……rộng, ra——ưm——」`
- Lý do: xây trên giá trị audit, chỉ đổi やっっ → "Ya" (bản audit "Á" mất hẳn y).

#### 893 — ポーレット — sai âm
- JP: `「やっ――あ――っ――おしりっ――もみもみっ――\nされるッ――っと――んっ――」`
- TW: `「呀——啊——屁股——被這樣揉著的話——嗯——」`
- Cũ: `「Á——a——mông——bị xoa bóp——\nThế này——thì——ưm——」`
- Mới: `「Ya——a——mông——bị xoa bóp——\nThế này——thì——ưm——」`
- Lý do: やっ → "Ya" (bản cũ "Á" mất y).

#### 894 — ポーレット — sai âm
- JP: `「やあっ――えぐれ――ってっ――けどっ――っ――\nもっと――あっ――もっ――ふか、くっ――にっ――」`
- TW: `「呀——被挖到了——但是——再來——啊——再深一點——」`
- Cũ: `「Á——bị ngoáy sâu——vào rồi——nhưng mà——\nHơn nữa——a——hơn, nữa——sâu, hơn——nữa——」`
- Mới: `「Yaa——bị ngoáy sâu——vào rồi——nhưng mà——\nHơn nữa——a——hơn, nữa——sâu, hơn——nữa——」`
- Lý do: やあっ = 2 âm a → "Yaa" (bản cũ "Á" mất y và thiếu 1 âm a).

#### 898 — ポーレット — sai âm
- JP: `「きゃっ」`
- TW: `「呀」`
- Cũ: `「Á」`
- Mới: `「Kya」`
- Lý do: きゃっ → "Kya" (bản cũ "Á" mất hẳn ky; tiền lệ h4 audit: きゃふっ → "kya" bị ghi sai vì mất ふ — mất mora là lỗi).

#### 900 — ポーレット — sai âm (key trùng audit)
- JP: `「くひゅっ！」`
- TW: `「呀！」`
- Cũ (CSV3): `「Đúng vậy nhỉ——Anh cũng——, tuyệt nhất là——\nTuyệt nhất là——anh vẫn muốn làm thế——」` (lệch vị trí)
- Mới: `「Kuhyu!」`
- Lý do: xây trên giá trị audit "Á!" — くひゅっ = ku-hyu, bản audit mất cả cụm → "Kuhyu!".

#### 902 — ポーレット — sai âm
- JP: `「きゃあっ！！？」`
- TW: `「呀！！？」`
- Cũ: `「Á!!?」`
- Mới: `「Kyaa!!?」`
- Lý do: きゃあっ = 2 âm a → "Kyaa" (bản cũ "Á" mất ky và thiếu 1 âm a).

#### 903 — ポーレット — sai âm
- JP: `「きゃっ！？」`
- TW: `「呀！？」`
- Cũ: `「Á!?」`
- Mới: `「Kya!?」`
- Lý do: きゃっ → "Kya" (như 898).

#### 904 — ポーレット — sai âm (key trùng audit)
- JP: `「ひゃっ！？　あっ――お尻――んっ――アナ、ル――\nわ、わたし――自分で、したこと――なく、て――んっ」`
- TW: `「呀！？啊——屁股——嗯——屁眼——我自己——沒有摸過——嗯——」`
- Cũ (CSV3): `Ngón tay không đút vào.\nCũng chưa chạm trực tiếp vào hậu môn.` (lệch vị trí)
- Mới: `「Hya!? A——mông——ưm——lỗ, hậu——\nE, em——chưa từng, tự làm——bao giờ——ưm」`
- Lý do: xây trên giá trị audit, chỉ đổi ひゃっ → "Hya" (bản audit "Á!?" mất hy; file đã có tiền lệ romaji đúng "Hyan!!" ở 901).

#### 906 — 双鉄H — sai âm
- JP: `「くっ――あっ――」`
- TW: `「呃——啊——」`
- Cũ: `「Ư——a——」`
- Mới: `「Ku——a——」`
- Lý do: くっ → "Ku" (bản cũ "Ư" mất hẳn phụ âm k; く là phụ âm thật, không phải gasp っ trần — so sánh 928 ぃっ → "Í" và 929 うぉっ → "Uo" đều giữ nguyên âm).

#### 914 — ポーレット — sai âm
- JP: `「ふっ――んっ――ちゅっ――ずちゅっ――\nちゅむっ――むっ――ちゅばっ――ちゅむっ」`
- TW: `「呼——嗯——啾——啾嚕——啾嚕——嗯——啾噗——啾噗」`
- Cũ: `「Phù——ưm——chụt——chụt——\nchu——ưm——chu——chu」`
- Mới: `「Phù——ưm——chụt——chụt——\nchumu——ưm——chuba——chumu」`
- Lý do: ちゅむっ ×2 → "chumu", ちゅばっ → "chuba" (bản cũ "chu" mất hẳn mora coda む/ば; tiền lệ h9 2156/1358 ちゅむっ → "chumu"). Giữ "chụt" cho ちゅっ/ずちゅっ.

#### 938 — 双鉄H — sai âm
- JP: `「ぅあっ――あっ――」`
- TW: `「啊——啊——」`
- Cũ: `「A——a——」`
- Mới: `「Ua——a——」`
- Lý do: ぅあっ → "Ua" (bản cũ "A" mất hẳn âm ぅ dẫn; tiền lệ kisaki h3 2197 ひあっ "I a" → "Hia").

#### 946 — ポーレット — sai âm
- JP: `「あ……んっ――ちゅっ――ちゅむっ――\nちゅきっ――好きっ――ンッ――双鉄、くぅん」`
- TW: `「啊……嗯——啾——啾嚕——我喜歡——好喜歡你——雙鐵——」`
- Cũ: `「A……ưm——chụt——chu——\nThích——thích anh lắm——ưm——anh Soutetsu」`
- Mới: `「A……ưm——chụt——chumu——\nThích——thích anh lắm——ưm——anh Soutetsu」`
- Lý do: ちゅむっ → "chumu" (như 914). Phần tên cuối "anh Soutetsu" giữ nguyên (xem §4 — くぅん là kéo dài của くん).

#### 955 — 双鉄H — sai âm
- JP: `「うぁっ！？」`
- TW: `「啊！？」`
- Cũ: `「Á!?」`
- Mới: `「Wa!?」`
- Lý do: うぁっ → "Wa" (bản cũ "Á" mất hẳn âm w dẫn; như 938).

#### 967 — ポーレット — sai âm
- JP: `「ちゅる――んっ……\nガムシロップ――用意してくれたんですね、双鉄くん」`
- TW: `「啾嚕——嗯……雙鐵君，你已經準備好糖漿了呢」`
- Cũ: `「Chụt——ưm……\nAnh Soutetsu đã chuẩn bị sẵn——si-rô đường rồi nhỉ.」`
- Mới: `「Churu——ưm……\nAnh Soutetsu đã chuẩn bị sẵn——si-rô đường rồi nhỉ.」`
- Lý do: ちゅる―― KHÔNG có っ → "Churu" (bản cũ "Chụt" thêm ngắt âm っ giả và mất る; quy tắc h5 ちゅるっ → "chụt" chỉ áp khi có っ).

#### 969 — ポーレット — sai âm
- JP: `「じゅっ！　じゅぼっ！　じゅるっ！　ぢゅぶっ！！」`
- TW: `「啾嚕！啾噗！啾嚕！啾噗！！」`
- Cũ: `「Chụt! Chu! Chụt! Chu!!」`
- Mới: `「Chụt! Jubo! Chụt! Jubu!!」`
- Lý do: じゅぼっ → "Jubo", ぢゅぶっ → "Jubu" (bản cũ "Chu" mất hẳn mora coda ぼ/ぶ). Giữ "Chụt" cho じゅっ/じゅるっ.

#### 970 — ポーレット — sai âm
- JP: `「ちゅむっ！　れろっ！　ちゅっ！　ちゅうっ！\nずちゅ！　ずぢゅっ！　ぢゅぼっ！　じゅろっ！！」`
- TW: `「啾嚕！啾嚕！啾嚕！啾噗！啾噗！啾噗！啾噗！啾嚕！！」`
- Cũ: `「Chu! Liếm! Chụt! Chụtttt!\nChụt! Chụt! Chu! Chụtttt!!」`
- Mới: `「Chumu! Liếm! Chụt! Chụụt!\nChụt! Chụt! Jubo! Chụt!!」`
- Lý do: ちゅむっ → "Chumu"; ちゅうっ = 2 âm u → "Chụụt" (bản cũ kéo dài bằng t); ぢゅぼっ → "Jubo" (mất ぼ); じゅろっ → "Chụt" (bản cũ "Chụtttt" kéo dài bằng t cho một âm ngắn, không có nguyên âm dài trong JP). Giữ "Chụt" cho ずちゅ/ずぢゅっ, "Liếm" cho れろっ.

#### 982 — ポーレット — sai âm (key trùng audit; dịch mới của audit)
- JP: `「くひゅんっ！　ふやっ――」`
- TW: `「嗯啊！呼呀——」`
- Cũ (CSV3): `Thử dập hông vào sâu hơn,\ncơ thể Paulette lại run lên bần bật.` (lệch vị trí)
- Mới: `「Kuhyun! Fuya——」`
- Lý do: xây trên giá trị audit "Hí——phù——" (bản dịch mới của audit cho dòng lệch vị trí không tìm thấy bản dịch đúng trong file): くひゅんっ → "Kuhyun" (bản audit "Hí" mất く và ん), ふやっ → "Fuya" (bản audit "phù" mất や; romaji cho nhất quán với các ふあ → "Fua" trong file).

## 4. Các dòng rên giữ nguyên (đáng chú ý)

- Gasp Ư của audit/sweep (907, 908, 934, 935, 954, 1639) — KHÔNG đụng, theo quy tắc khóa. 994 đã sweep ghi already-rendered — giữ nguyên.
- 901 ひゃんっ → "Hyan!!" — romaji đúng, giữ (tiền lệ cho 904).
- 928 ぃっ → "Í!!", 929 うぉっ → "Uo!?", 912 はっ――アッ → "Hà——á!", 944 ああ―― → "A——", 953/951 あ → "A" — giữ nguyên âm đúng.
- 971 うむ―― → "Ừm——", 993 うむ？ → "Hửm?", 976 ん……あっ → "Ưm……a——", 926 こほん―― → "E hèm——" — giữ.
- 958 ちゅっ → "Chụt", 965 ちゅるっ――ちゅっ――ぺろっ―― → "Chụt——chụt——liếm——liếm——" — giữ theo quy tắc họ ちゅ (h5).
- 1011 ふっ――あっ―― → "Phù——a——" (giá trị audit) — giữ: ふっ đứng riêng diễn "Phù" là đúng, chỉ ふあ/ふぁ mới về romaji.
- 924 むぷっ → "Ưm" — giữ: âm m (môi khép) đã bao hàm tiếng bật môi ぷ; こくっ/んぐっ → "ực" giữ. (Xem cờ 7.)
- 946/1069 tên rên: くぅん sau "Soutetsu" là kéo dài của くん — giữ "anh Soutetsu" theo B4, không thêm rên.
- 1018 かっ――あっ → "a——á" — giữ: かっ là mảnh câu nói ngắt quãng, không phải âm rên.
- 994 ん～～っ――んっ――んぅ～～～っ → "Ưm～～ưm——ưm～～～" — giữ: mọi âm đều đã diễn (sweep ghi already-rendered).
- SFX độc thoại trong ngoặc （ ） — giữ nguyên onomatopoeia Việt, theo tiền lệ h9 (nhóm này nhất quán dùng onomatopoeia Việt, chưa áp công thức đếm nguyên âm): 37, 1640–1649, 1652, 1655–1656, 1658, 1661–1662, 1666–1669, 1671, 1673, 1675–1676, 1684, 1686. Các giá trị audit của 1641 "（Thịch!）", 1658 "（Sụttt!）", 1673 "（Kítttttt!）", 1676 "（Trơn tuộtttt）" cũng giữ nguyên (xem cờ 3).
- 1648 （む、ぅ……） → "（Ư, m……）" — giữ (cả hai âm đều có mặt).
- 1450 ちろり, 1482 むりゅむりゅ — diễn thành động từ/cụm nghĩa trong lời dẫn, audit đã chấp nhận — giữ (không phải âm rên trong thoại).

## 5. Cờ

1. **1013 (không phải moan — cờ cho audit/đợt thống nhất):** JP `うれしっ――嬉しいです。双鉄くんっ`, TW `我好高興`, VN cũ `「Sướng——Em vui lắm. Anh Soutetsu」`. うれしい = "vui mừng/hạnh phúc" (TW 高興 xác nhận); "Sướng" mang nghĩa khoái cảm thể xác — có thể là lỗi nghĩa audit bỏ sót. Không sửa ở đây (ngoài phạm vi moan).
2. **1683:** dòng chưa chắc chắn của audit (Soutetsu H, JP 僕 → VN "mình" cả hai vế) — không phải moan, không đụng.
3. **SFX độc thoại （ ） chưa áp công thức đếm nguyên âm** (như cờ 6 của h9): 1652 びゅううっ → "phụtttt", 1655/1656 びゅううっ → "phụtttt"/"Phụtttt!", 1658 ずりゅうううっ → "Sụttt!", 1671 きゅうううううっ → "siếttttt", 1673 ギチチチチチチっ → "Kítttttt!", 1676 ぬろおおおおっ → "Trơn tuộtttt" — đều kéo dài bằng phụ âm t. Đợt thống nhất quyết có áp công thức cho nhóm SFX độc thoại này không (h9 cũng để cờ tương tự).
4. **899:** giá trị audit "Hyaaaaaaa!!" đếm ĐÚNG 7 âm a (đã đếm lại độc lập theo từng ký tự); chỉ thiếu ん cuối → fix chỉ thêm "n" ("Hyaaaaaaan!!"). Ghi rõ để parent khỏi tưởng audit đếm sai.
5. **7 key trùng audit (890, 899, 900, 904, 919, 937, 982):** fix moan xây trên giá trị audit, chỉ khác đúng token rên (đã kiểm chứng bằng difflib §6); KHÔNG áp thêm fix audit cùng key — parent gộp fix moan thì dùng giá trị này thay cho giá trị audit.
6. **946/1069:** くぅん kéo dài của くん sau tên "Soutetsu" — giữ "anh Soutetsu". Nếu đợt thống nhất muốn diễn cả tiếng kéo dài thì đổi thành "anh Soutetsuuun".
7. **924 むぷっ → "Ưm":** giữ theo lý do §4; nếu đợt thống nhất muốn giữ cả ぷ thì đổi "Mupu".
8. **1072 み、→ "Q," và 1002 ご！→ "X...":** cách diễn tiếng lắp — không thuộc moan, audit đã chấp nhận; ghi nhận, không sửa.

## 6. Lượt soát 2

- **Tổng 37 / tái kiểm chứng 37 / bỏ 0 / sửa 0.**
- Lượt soát 2 đọc lại toàn bộ từng giá trị fix đối chiếu JP (+TW khi cần), đếm lại độc lập từng rên dài bằng ký tự (899: 7 a + ん; 920: 11 a; 923: 12 u [parent sửa: agent ghi 11 u — JP có 11 chữ う]; 927: 13 a + ん; 966: 4 o; 968: 6 u; 974: 7 o, すうっ 2 u; 948: はぁっ 2 a, はぁああっ 4 a; 915: ハァッ 2 a). Trong lượt soát đã đính chính ghi chú về 899 (giá trị audit đếm đúng, chỉ thiếu ん) — không đổi giá trị fix nào.
- Chuẩn hóa mã hoá trước lượt soát 2: giá trị fix dùng ký tự xuống dòng dạng backslash-n (2 ký tự, như JSON audit và CSV3), không dùng ký tự xuống dòng thật — phát hiện khi so sánh với giá trị audit (difflib báo lệch `\\n` giả).
- JSON 37 mục dạng chuẩn (khóa string; jp/tw/old_vn khớp CSV3 tuyệt đối 37/37); khối TOML parse bằng tomllib: 37 khóa, 0 sai lệch giá trị.
- Kiểm tra cơ học (difflib): 7 key trùng audit chỉ khác giá trị audit ở đúng token rên; 30 key còn lại chỉ khác VN cũ ở token rên nhắm tới.
- Không dòng gasp Ư nào bị đụng; không dòng "Kh" nào bị đổi (file không có dòng "Kh" nào).

## 7. Khối TOML (đã kiểm chứng parse)

Khối TOML dưới đây parse được bằng tomllib, **37 key, 0 sai lệch giá trị so với JSON**. Quy tắc ký tự xuống dòng: giá trị fix nào chứa ký tự xuống dòng dạng backslash-n (2 ký tự, như trong JSON và trong TOML gốc) thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON.

[script]
"890" = "「Ya——a——ưm——lỗ, hậu, của em——\\nBị anh Soutetsu——nong……rộng, ra——ưm——」"
"893" = "「Ya——a——mông——bị xoa bóp——\\nThế này——thì——ưm——」"
"894" = "「Yaa——bị ngoáy sâu——vào rồi——nhưng mà——\\nHơn nữa——a——hơn, nữa——sâu, hơn——nữa——」"
"897" = "「Ya……a——mông……Fua——\\nBản thân em……chưa từng……chạm vào……nhưng——」"
"898" = "「Kya」"
"899" = "「Hyaaaaaaan!!」"
"900" = "「Kuhyu!」"
"902" = "「Kyaa!!?」"
"903" = "「Kya!?」"
"904" = "「Hya!? A——mông——ưm——lỗ, hậu——\\nE, em——chưa từng, tự làm——bao giờ——ưm」"
"906" = "「Ku——a——」"
"914" = "「Phù——ưm——chụt——chụt——\\nchumu——ưm——chuba——chumu」"
"915" = "「Fua——a——hàà——a——」"
"917" = "「Fua——a——nhiều quá——nhiều quá——\\nƯm, của anh Soutetsu——tinh dịch——vào trong, tử cung——rồi——」"
"919" = "「Fua——a——sâu, quá——thế này——\\nƯm——sướng quá——cảm giác, như đâm, vào tận bụng, vậy」"
"920" = "「Phiaaaaaaaaaaa!!!」"
"923" = "「Sụụụụụụụụụụụụt!!!」"
"927" = "「Í——a á a a a a a a a a a a an!!」"
"931" = "「Ngoạm——chụt——chụụụt——chụt!\\nChuba! Chụt! Chụụt! Liếm!」"
"933" = "「Ngoạm——ưm——chubu——chụt——\\nliếm——liếm——liếm——chụụụt」"
"937" = "「A——của anh Soutetsu——to hơn, bình thường——\\nFua——to, quá——bị nong rộng, ra——a」"
"938" = "「Ua——a——」"
"940" = "「A——ưm——Fua——a, anh Soutetsu——\\nEm——em——chuyện đó——」"
"942" = "「Ngoạm——ưm——ưm～～\\nliếm, liếm——chumu——chụụt」"
"946" = "「A……ưm——chụt——chumu——\\nThích——thích anh lắm——ưm——anh Soutetsu」"
"948" = "「A……ưm——ưm——ực——ưm——\\nPua——hàà! Hàààà!」"
"950" = "「A……sướng quá……sướng quá……anh ơi……\\nFua——của, anh Soutetsu——dương, vật——a」"
"955" = "「Wa!?」"
"966" = "「Chụt——chumu——liếm——Reroooo」"
"967" = "「Churu——ưm……\\nAnh Soutetsu đã chuẩn bị sẵn——si-rô đường rồi nhỉ.」"
"968" = "「Reruuuuuu!」"
"969" = "「Chụt! Jubo! Chụt! Jubu!!」"
"970" = "「Chumu! Liếm! Chụt! Chụụt!\\nChụt! Chụt! Jubo! Chụt!!」"
"974" = "「Ưm——chụt——chụt——chụt——\\nSuụt——!——Zurooooooo!!!」"
"977" = "「Ưm……nhóp nhép——ưm——ực——Pua. Ngon quá.\\nNhưng mà……em nghĩ nếu có thêm sữa thì sẽ ngon hơn nữa.」"
"982" = "「Kuhyun! Fuya——」"
"1070" = "「Anh Soutetsu, cũng——ưm——đã——thế này rồi——\\nCứng, quá——nóng, quá——Fua——」"
## Kết bài

File ポーレットh3_誘惑アイスコーヒー đã sửa xong tiếng rên theo quy tắc romaji: đọc 279/279 dòng, xét 139 dòng rên/SFX, đổi 37 dòng (13 romaji + 7 đếm nguyên âm + 17 sai âm), giữ 102 dòng. Lỗi tập trung ở họ fa/fu bị Việt hoá mất âm a ("phù" cho ふあ/ふぁ), rên dài kéo bằng phụ âm t/m thay vì nguyên âm, và phụ âm mora bị mất hẳn ("Á" cho きゃっ/ひゃっ/やっ, "chu" cho ちゅむっ/ちゅばっ). Mọi gasp Ư của audit/sweep và SFX độc thoại trong ngoặc đều giữ nguyên; 7 key trùng audit chỉ khác đúng token rên. Lượt soát 2: 37/37 tái kiểm chứng, 0 bỏ, 0 sửa; JSON 37 mục khớp CSV3 tuyệt đối; khối TOML 37 khóa parse đúng, 0 sai lệch. Cờ còn lại: 1013 (lỗi nghĩa "Sướng" cho うれしい), nhóm SFX độc thoại chưa áp công thức đếm nguyên âm, và dòng chưa chắc chắn 1683 của audit — tất cả chờ đợt thống nhất/audit, không thuộc phạm vi moan.
