# Moan-fix REVIEW — lr_れいな追加h_夜の花嫁修業.txt.toml (moan-lr-reinah-tsuika-h-yoru-no-hanayome-shugyou)

File: `lrれいな追加h_夜の花嫁修業.txt.toml` — route 04_Reina, H-scene "đêm tân hôn / khóa học làm dâu" (Reina + Soutetsu).
Slug: `moan-lr-reinah-tsuika-h-yoru-no-hanayome-shugyou`.

## §1. Xác minh file

- TOML: `sources/toml2/translation_toml/04_Reina/lr#U308c#U3044#U306a#U8ffd#U52a0h_#U591c#U306e#U82b1#U5ac1#U4fee#U696d.txt.toml`
  - md5: `b6d6a52b2213d8bc98351a0f14d5ae91` (khớp md5 audit), UTF-8 BOM + CRLF, 365 khóa `[script]`.
  - Không có bản TOML trùng (so md5 toàn bộ `sources/toml2/`).
- CSV3: 1 bộ duy nhất, 365 dòng, 0 key trùng, 0 VN trống. VN TOML khớp CSV3 365/365 (sau chuẩn hoá `\n` literal ↔ khoảng trắng — TOML-2 làm phẳng `\n` literal thành khoảng trắng ở một số dòng; CSV3 là chuẩn cho fix list).
- Đã đọc 365/365 dòng (CSV3 + TOML). Audit trước đó: 33 sai (đã gộp).
- Sweep gasp: 10 mục cho file này (1233, 1321, 1331, 1332, 1335, 1337, 1475, 1572, 1923, 727) — cả 10 đều đã nằm trong audit JSON (kind sweep-gasp) và KHÔNG trùng key nào trong 47 fix moan này. Không dòng gasp Ư nào bị đụng; không dòng "Kh" nào bị đổi.
- Cơ sở tổng: **31 file / 688 dòng** (đọc lại từ `moans/ROUTE-MOANS.md`, khớp MEMORY).

## §2. Kiểm kê rên (moan inventory)

- 161/365 dòng chứa mẫu rên/thở/gasp/SFX (liệt kê bằng mẫu JP: họ fa/fu, ひゃ/ひゅ/ひあ/きゃ, あ/は/ん/く/ふ, cười, SFX trong （ ）).
- **Sửa 47 dòng, giữ 114 dòng.**
- Nhóm sửa: romaji 42 + mất âm (sound-loss) 5.
  - Họ fa/fu → romaji (32 dòng chứa token fa/fu): ふぁ→Fa, ふあ→Fua, ぷあ→Pua, ふや→Fuya, ふお→Fuo, ふきゅん→Fukyun, ふひゅん→Fuhyun; dạng tách "phù, a"/"phù——a" → "Fu, a"/"Fu——a".
  - Họ ひゃ/ひゅ/ひあ (11 dòng): ひゃう→Hyau, ひあ→Hia, ひゅあ→Hyua (gộp 1 token), んひゅ(ん)→Nhyu/Nhyun, んゆ(う)→Nyu/Nyuu.
  - Mất âm (5): 723 っふ→phù, 1116 ふくっ→Fuku, 1118 うあっ→Ua, 1123 く、→Ku, 1221 んくっ→Ư hự.
  - Đếm nguyên âm đã kiểm chứng bằng máy cho các token dài: 1075 (7 a), 1076 (4 a), 1077 (6 a), 1078 (9 a), 1080 (6 a), 1133 (18 a), 1170 (4 n), 1178 (2 u), 1049 (4 a), 1177 (2 a).
- Tiền lệ đã kiểm chứng chéo file (CSV3 toàn dự án): ふくっ→"Fuku" (lr_稀咲追加h 1090, lr_凪ふかみh1 1567); うあっ→"Ua" (日々姫h1 1042, lr_稀咲ポーレットh1 1592, lr_ふかみh1 1365/1390, lr_ふかみh2 1230); んゆ→"Nyu" (ハチロク01 2317/2320); ふきゅん→"Fukyun" (日々姫h5 1260, lr_ふかみh2 1095/1505, lr_凪ふかみh1 1487); くあっ→"Kua" (lr_ハチロクh1 1217, ハチロクh3 1037); ひゃう→"Hyau" (lr_ハチロクh3 1191/1195); ひあ→"Hia" (ハチロクh1 1227/1229); んひゅ→"Nhyu" (lr_ハチロクh1 1258, lr_ハチロクh3 1311). Cùng file Reina h1 đã gộp (48 fix): ふぁ→Fa, ふあ→Fua, ぷあ→Pua, ふや→Fuya, ふぇ→Fe, ひゃう→Hyau, ひゅあ→Hyua, んきゅ→Nkyu, dạng tách "phu, a"→"Fu, a" — file này theo đúng cùng quy ước.

## §3. Chi tiết từng dòng sửa (47 dòng)

### 3a. Họ fa/fu → romaji (32 dòng)

- **723 [双鉄]** — JP 「――くっ――っふ――んぁっ」 / TW 「——唔——呼——嗯啊」 / Cũ 「——Hự——ưm——a」 → **「——Hự——phù——aƯ」**. っふ: VN cũ "ưm" mất hẳn âm f (TW 呼 = thở ra); "phù" diễn đúng âm ふ. Giữ "aƯ" của audit (gasp っ của んぁっ).
- **724 [双鉄]** — JP 「――ぷあっ――あ……。あっ――ふ、あ」 / TW 「——噗哈——啊……呼、啊」 / Cũ 「——Phu a——a……. A——phù, a」 → **「——Pua——a……. A——Fu, a」**. ぷあっ→Pua; ふ、あ (nói lắp, tách) → "Fu, a" (tiền lệ lr-reinah1 1424).
- **736 [れいな]** — JP 「……んぅ……んっ――\\nふぁ……あっ――んっ――んんっ」 / TW 「……嗯……嗯——呼啊……啊……嗯——嗯嗯」 / Cũ 「……Ưm……ưm——\\nPhu a……a——ưm——ưm ưm」 → **「……Ưm……ưm——\\nFua……a——ưm——ưm ưm」**. ふぁ→Fua.
- **1051 [れいな]** — JP 「ひゃう――ふあっ――とけちゃう――とけちゃううっ、\\nれいな、あつくて――おまたも、おまたも、どろどろで」 / TW 「呀嗚——呼啊——融化了——要融化了玲奈全身好燙——股間，連股間都汪洋一片了」 / Cũ 「Hya u——phu a——tan chảy mất——tan chảy mất thôi,\\nReina, nóng quá——háng cũng, háng cũng, nhầy nhụa rồi」 → **「Hyau——Fua——tan chảy mất——tan chảy mất thôi,\\nReina, nóng quá——háng cũng, háng cũng, nhầy nhụa rồi」**. ひゃう→Hyau (tiền lệ lr-reinah1 1175); ふあっ→Fua.
- **1061 [れいな]** — JP 「ふぁ……あ……\\nキス。あまくて――すっごくきもちよかったですぅ」 / TW 「呼……哈……接吻——好甜蜜好舒服呀」 / Cũ 「Phu a……a……\\nNụ hôn. Ngọt ngào quá——thích lắm luôn nha~」 → **「Fua……a……\\nNụ hôn. Ngọt ngào quá——thích lắm luôn nha~」**. ふぁ→Fua.
- **1064 [双鉄]** — JP 「ふおっ！！？」 / TW 「呼哦？！！」 / Cũ 「Phu oá!!?」 → **「Fuo!!?」**. ふお→Fuo (một token; "Phu oá" tách 1 âm thành 2 tiết, cùng lỗi như fa/fu). Lần đầu xuất hiện trong dự án — chưa có tiền lệ chéo file, theo mẫu fa/fu.
- **1065 [れいな]** — JP 「ふやっ――やぁっ――もうちょっと――もうちょっと、\\nねっ――そうてつさぁんっ――もうちょっとぉ」 / TW 「呼啊——呀啊——再等一等——再等等，等一下——雙鐵先生——先等等我啊」 / Cũ 「Phu ya——ya——một chút nữa thôi——một chút nữa thôi,\\nnha~——anh Soutetsu ơi~——một chút nữa thôi nha~」 → **「Fuya——Yaa——một chút nữa thôi——một chút nữa thôi,\\nnha~——anh Soutetsu ơi~——một chút nữa thôi nha~」**. ふやっ→Fuya; やぁっ→Yaa (やぁ = 2 a; tiền lệ lr-reinah1 1208).
- **1067 [れいな]** — JP 「ふあっ――あっ――あっ――あっ！！！」 / TW 「呼啊——啊——啊——啊！！！」 / Cũ 「Phu a——a——a——a!!!」 → **「Fua——a——a——a!!!」**. ふあっ→Fua.
- **1068 [れいな]** — JP 「ふあっ――あっ――あっ――れいな、れいなぁっ」 / TW 「呼啊——啊——啊——玲奈、玲奈」 / Cũ 「Phu a——a——a——Reina, Reina」 → **「Fua——a——a——Reina, Reina」**. ふあっ→Fua.
- **1069 [双鉄]** — JP 「ふあっ――あっ――イクっ――イクっ！！！！」 / TW 「呼啊——啊——射了——要射了！！！！」 / Cũ 「Phu a——a——ra mất——anh ra mất!!!!」 → **「Fua——a——ra mất——anh ra mất!!!!」**. ふあっ→Fua (イクっ→"ra mất" giữ nguyên, diễn nghĩa).
- **1071 [れいな]** — JP 「ふあっ――んっ――れりゅっ――ちゅっ――ちゅむっ、\\nれろおっ――んちゅっ――ちゅるううっ――ちゅ、ちゅ」 / TW 「呼啊——嗯——咧溜——啾——啾啾，滋溜——嗯啾——啾嚕嚕——啾啾」 / Cũ 「Phu a——ưm——liếm——chụt——chụt,\\nliếm——ưm chụt——chụt——chụt, chụt」 → **「Fua——ưm——liếm——chụt——chụt,\\nliếm——ưm chụt——chụt——chụt, chụt」**. ふあっ→Fua.
- **1073 [れいな]** — JP 「ふぁ――おっぱい――んっ――ふ、ぬる、ぬるっ――\\nれいな、ちくびっ――ちくびっ――こん、なにっ――」 / TW 「呼啊——胸部——嗯——呼，滑溜溜的——玲奈的乳頭——乳頭——好舒爽——」 / Cũ 「Phu a——ngực——ưm——phù, trơn, trơn——\\nReina, nhũ hoa——nhũ hoa——nhiều, thế này——」 → **「Fua——ngực——ưm——Fu, trơn, trơn——\\nReina, nhũ hoa——nhũ hoa——nhiều, thế này——」**. ふぁ→Fua; ふ、(thở tách) → "Fu,".
- **1074 [れいな]** — JP 「ふぁ」 / TW 「呼啊」 / Cũ 「Phu a」 → **「Fua」**. ふぁ→Fua.
- **1075 [れいな]** — JP 「ふあああああああんっっっ」 / TW 「呼啊啊——」 / Cũ 「Phu a a a a a a an」 → **「FuaaaaaaanƯƯƯ」**. ふあ+6あ+ん = 7 a (đếm máy); xây trên giá trị audit (audit đã sửa số a đúng 7 và thêm ƯƯƯ cho っ×3) — chỉ đổi token fa→romaji.
- **1076 [れいな]** — JP 「ふぁぁぁあ――おっぱい、\\nれいな、おっぱいとろけちゃいますぅ」 / TW 「呼啊啊——胸部，玲奈的胸部快要融化了」 / Cũ 「Phu a a a a——ngực,\\nReina, ngực tan chảy mất thôi nha~」 → **「Fuaaaa——ngực,\\nReina, ngực tan chảy mất thôi nha~」**. ふぁぁぁあ = 4 a (đếm máy).
- **1077 [れいな]** — JP 「ふああああああんっっっっ」 / TW 「呼啊啊啊——」 / Cũ 「Phu a a a a a a an」 → **「FuaaaaaanƯƯƯƯ」**. ふあ+5あ+ん = 6 a (đếm máy; VN cũ thừa 1 a — audit đã sửa về 6 a và thêm ƯƯƯƯ cho っ×4); chỉ đổi token fa→romaji.
- **1078 [双鉄]** — JP 「ふあああああああああっっ！！！！」 / TW 「呼啊啊啊啊——！！！！」 / Cũ 「Phu a a a a a a a a a!!!!」 → **「Fuaaaaaaaaa!!!!」**. ふあ+8あ = 9 a (đếm máy).
- **1080 [れいな]** — JP 「ふやあああああっ！　しゅきっ――これっ――しゅきっ\\nそうてつ、さぁんっ――んっ――このまま、このままぁ」 / TW 「呼啊啊啊啊！好喜歡——這樣子頂——好喜歡啊雙鐵先生——嗯——就這樣、就這樣繼續」 / Cũ 「Phu ya a a a a a! Thích——cái này——thích quá\\nanh Soutetsu, ơi~——ưm——cứ thế này, cứ thế này nha~」 → **「Fuyaaaaaa! Thích——cái này——thích quá\\nanh Soutetsu, ơi~——ưm——cứ thế này, cứ thế này nha~」**. ふや+5あ = 6 a (đếm máy).
- **1081 [れいな]** — JP 「ふあっ！　あっ！　あっ！　あっ！\\nあっ！　あっ！　あっ！　ああっっっ！！！」 / TW 「呼啊！啊！啊！啊！啊！啊！啊！啊啊！！！」 / Cũ 「Phu a! A! A! A!\\nA! A! A! A a!!!」 → **「Fua! A! A! A!\\nA! A! A! A a!!!」**. ふあっ→Fua (ああっっっ giữ nguyên — audit đã quyết っ đã được diễn, xem §5).
- **1087 [れいな]** — JP 「ひあっ――はっ！　はっ！　ふあっ！　んっ！\\nくゅっ！　ふあっ！はっ！　は！　は！　はっ！　は！」 / TW 「咿呀——哈！哈！呼啊！嗯！唔！呼啊！哈！哈！哈！哈！哈！」 / Cũ 「Hi a——ha! Ha! Phu a! Ưm!\\nKyu! Phu a! Ha! Ha! Ha! Ha! Ha!」 → **「Hia——ha! Ha! Fua! Ưm!\\nKyu! Fua! Ha! Ha! Ha! Ha! Ha!」**. ひあっ→Hia (quy tắc 3b); ふあっ→Fua ×2.
- **1090 [れいな]** — JP 「ひゃうっ！　ふあっ！　しゅごっ！　しゅごいいっ！\\nそうてつさんのっ、ふといの、あついのっ――んうっ！」 / TW 「咿呀！呼啊！好厲害！好厲害啊！雙鐵先生粗粗的肉棒好熱啊——嗯嗚！」 / Cũ 「Hya u! Phu a! Sướng! Sướng quá!\\nCái to bự, nóng hổi của anh Soutetsu——ưm u!」 → **「Hyau! Fua! Sướng! Sướng quá!\\nCái to bự, nóng hổi của anh Soutetsu——ưm u!」**. ひゃうっ→Hyau; ふあっ→Fua.
- **1102 [れいな]** — JP 「はっ――みゅっ――ん――れりゅ――ん……（こくっ）\\nぷあっ――りゅっ――ちゅりゅうっ――ぷ――（ごく）」 / TW 「哈——啾——嗯——咧溜——嗯……（吞嚥）噗哈——滋溜——吸溜吸溜——噗——（吞嚥）」 / Cũ 「Háp——chụt——ưm——liếm——ưm……（Ực）\\nPhu a——liếm——chụt——phù——（Ực）」 → **「Háp——chụt——ưm——liếm——ưm……（Ực）\\nPua——liếm——chụt——phù——（Ực）」**. ぷあっ→Pua (ぷ――→"phù" giữ — token đơn).
- **1104 [れいな]** — JP 「はっ！　はっ――ふあっ――ひゃうっ！　そうてつ、さ、\\nれいなっ　れいなっ！　れいなっ！　もうっ！　もう！」 / TW 「哈！哈——呼啊——呀啊！雙鐵先生，玲奈、玲奈！玲奈！已經！忍不住了！」 / Cũ 「Ha! Ha——phu a——hya u! Anh Soutetsu,\\nReina, Reina! Reina! Ra mất! Ra mất!」 → **「Ha! Ha——Fua——Hyau! Anh Soutetsu,\\nReina, Reina! Reina! Ra mất! Ra mất!」**. ふあっ→Fua; ひゃうっ→Hyau.
- **1156 [れいな]** — JP 「ふきゅんっ！！！！！」 / TW 「嗚呼！！！！！」 / Cũ 「Phu kyun!!!!!」 → **「Fukyun!!!!!」**. ふきゅん→Fukyun (tiền lệ "Fukyun" ở 4 file khác).
- **1162 [双鉄]** — JP 「ん……ぷあ」 / TW 「嗯……噗哈」 / Cũ 「Ưm……phu a」 → **「Ưm……Pua」**. ぷあ→Pua.
- **1170 [れいな]** — JP 「ふひゅんんんんっ！！！！」 / TW 「嗯唔唔！！！！」 / Cũ 「Phu hyun n n n!!!!」 → **「Fuhyunnnn!!!!」**. ふひゅんんんん = Fu+hyu+4n (đếm máy); một cách diễn duy nhất, không trộn Việt+romaji. Lần đầu xuất hiện trong dự án.
- **1177 [れいな]** — JP 「んぷっ――ん――ん～～～～っ――――（ごくっっ）\\nぷああ。どろってしてて、お喉にはりつきますねぇ」 / TW 「嗯噗——嗯——嗯～～～～——（吞嚥）噗哈。好黏稠啊，都沾上喉嚨了」 / Cũ 「Ưm——ưm——ưm~~~~——（Ực）\\nPhu a a. Đặc sệt luôn, dính cả vào cổ họng nha~」 → **「Ưm——ưm——ưm~~~~——（Ực）\\nPuaa. Đặc sệt luôn, dính cả vào cổ họng nha~」**. ぷああ = 2 a → Puaa.
- **1188 [れいな]** — JP 「ぷあっ！　すごい。そうてつさんのせいえき、\\nしゃせい、こんないきおい、はじめてですねぇ」 / TW 「噗哈！雙鐵先生的精液好厲害。玲奈還是第一次見到勢頭如此兇猛的射精」 / Cũ 「Phu a! Tuyệt quá. Tinh dịch của anh Soutetsu,\\nphóng ra với lực mạnh thế này, đây là lần đầu tiên nha~」 → **「Pua! Tuyệt quá. Tinh dịch của anh Soutetsu,\\nphóng ra với lực mạnh thế này, đây là lần đầu tiên nha~」**. ぷあっ→Pua.
- **1202 [れいな]** — JP 「あちゅっ――ふあっ――れいなっ――あたって――\\nふ、あ――おまた――おなか――いっぱい、いっぱいぃ」 / TW 「好燙——呼啊——碰到——玲奈——最深處了——　呼、啊——股間——肚子裡——都是滿滿的」 / Cũ 「Nóng quá——phu a——Reina——bị bắn trúng——\\nphù, a——háng——bụng——đầy, đầy ắp rồi」 → **「Nóng quá——Fua——Reina——bị bắn trúng——\\nFu, a——háng——bụng——đầy, đầy ắp rồi」**. ふあっ→Fua; ふ、あ→"Fu, a" (あちゅっ→"Nóng quá" giữ — diễn nghĩa, không phải rên).
- **1211 [れいな]** — JP 「すじ、の、なか――ふっ、あっ――おにく、もっ――\\nあなもっ――にゅるにゅるっ――全部――気持ち、いい」 / TW 「小穴裡面——呼、啊——肉肉和洞洞——都呲溜溜的——兩個地方都很舒服」 / Cũ 「Bên trong, khe——phù, a——thịt, cũng——\\nlỗ cũng——trơn tuột——tất cả——sướng, lắm」 → **「Bên trong, khe——Fu, a——thịt, cũng——\\nlỗ cũng——trơn tuột——tất cả——sướng, lắm」**. ふっ、あっ (tách) → "Fu, a".
- **1283 [れいな]** — JP 「ほんと……ふ――あ――（ごくっ）――ん。\\nほんとに――すっごく――ぅ――そう、ですねぇ」 / TW 「真的……呼——啊——（吞嚥）——嗯。真的——說的——一點也沒錯啊」 / Cũ 「Đúng vậy……phù——a——（Ực）——ưm.\\nĐúng là——rất rất——ư——như vậy, nha~」 → **「Đúng vậy……Fu——a——（Ực）——ưm.\\nĐúng là——rất rất——ư——như vậy, nha~」**. ふ――あ―― (tách) → "Fu——a".
- **1294 [れいな]** — JP 「そ……です、よぉ――んっ――ふあっ――\\nれいな、れいなも――きもち、とっても、いいですしぃ」 / TW 「說的……沒錯——嗯——呼啊——玲奈，玲奈——也特別舒服」 / Cũ 「Đúng……vậy, nha~——ưm——phu a——\\nReina, Reina cũng——thấy sướng, lắm luôn nha~」 → **「Đúng……vậy, nha~——ưm——Fua——\\nReina, Reina cũng——thấy sướng, lắm luôn nha~」**. ふあっ→Fua.
- **1474 [れいな]** — JP 「ふあっ――あっ――おまた――すじっ――れいなの、\\nわれめっ――んっ――われめも――おまめ、もっ――」 / TW 呼啊——啊——小穴——還有——玲奈的、縫隙——嗯——還有縫隙——再加上豆豆也—— / Cũ 「Phu a——a——háng——khe——của Reina,\\nkhe hở——ưm——khe hở cũng——hột le, cũng——」 → **「Fua——a——háng——khe——của Reina,\\nkhe hở——ưm——khe hở cũng——hột le, cũng——」**. ふあっ→Fua.

### 3b. Họ ひゃ/ひゅ/ひあ/きゃ → romaji (quy tắc 3b)

- **1049 [れいな]** — JP 「ひゅああああっ――おっぱい、おっぱいも、しゅきぃ」 / TW 「呀啊啊啊啊——胸部、胸部那裡也好喜歡」 / Cũ 「Hyu a a a a——ngực, ngực cũng, thích」 → **「Hyuaaaa——ngực, ngực cũng, thích」**. ひゅあ+4あ = Hyu+4a, gộp 1 token (tiền lệ lr-reinah1 1171: ひゅあっ→"Hyua").
- **1092 [れいな]** — JP 「っひゅあっ！！？　ぢゅるって！　どちゅって！！\\nあついの！　あついのいっきに！　れいなのなかにっ」 / TW 「咿呀？！！滋滋的！啾啾的！！熱熱的！又大又熱的棒棒一下子進到了玲奈身體裡」 / Cũ 「Hyu a!!? Sục vào! Đâm phập vào!!\\nNóng quá! Nóng quá ập vào một lúc! Bên trong Reina」 → **「ƯHyua!!? Sục vào! Đâm phập vào!!\\nNóng quá! Nóng quá ập vào một lúc! Bên trong Reina」**. Xây trên giá trị audit (audit thêm Ư đầu cho っ) + gộp "Hyu a"→"Hyua".
- **1133 [れいな]** — JP 「ひゅあああああああああああああああああぁんっ！！」 / TW 「啊啊啊啊啊——！！」 / Cũ 「Hyu a a a a a a a a a a a a a a a an!!」 → **「Hyuaaaaaaaaaaaaaaaaaan!!」**. ひゅ+18a+ん (đếm máy; audit đã sửa số a đúng 18) — gộp thành 1 token romaji theo tiền lệ lr-reinah1 1171.
- **1164 [双鉄]** — JP 「んひゅんっ！！！」 / TW 「嗯咿！！！」 / Cũ 「Ưm hyun!!!」 → **「Nhyun!!!」**. んひゅん→Nhyun (quy tắc 3b).
- **1166 [れいな]** — JP 「んゆっ――ふ――それ、しゅきっ――んっ――おまたの、\\nすじ、を――すり、すり――されるの――きもち、いい」 / TW 「嗯唔——呼——好喜歡這樣——嗯——小穴——摩擦起來——特別舒爽」 / Cũ 「Ưm yu——phù——cái đó, thích lắm——ưm——khe,\\nkhe háng——cọ, cọ——như vậy——sướng, lắm」 → **「Nyu——phù——cái đó, thích lắm——ưm——khe,\\nkhe háng——cọ, cọ——như vậy——sướng, lắm」**. んゆっ→Nyu (tiền lệ ハチロク01 2317/2320: んゆー→"Nyu").
- **1168 [れいな]** — JP 「んひゅっ――ふ、ぁ――ぬる、ぬる――すきぃっ」 / TW 「嗯唔——呼、啊——滑滑的——我好喜歡」 / Cũ 「Ưm hyun——phù, a——trơn, trơn——thích quá」 → **「Nhyu——Fu, a——trơn, trơn——thích quá」**. んひゅっ→Nhyu (KHÔNG có ん sau ひゅ — VN cũ "hyun" thừa 1 n); ふ、ぁ→"Fu, a".
- **1172 [れいな]** — JP 「んひゅんっ！！」 / TW 「嗯唔！！」 / Cũ 「Ưm hyun!!」 → **「Nhyun!!」**. んひゅん→Nhyun.
- **1178 [れいな]** — JP 「んゆうっ！！！」 / TW 「嗯！！！」 / Cũ 「Ưm yuu!!!」 → **「Nyuu!!!」**. んゆうっ→Nyuu (2 u).

### 3c. くあ → Kua + mất âm (5 dòng)

- **1060 [双鉄]** — JP 「ふっ――あっ――あっ――くあっ」 / TW 「呼——啊——啊——唔啊」 / Cũ 「Phù——a——a——ư a」 → **「Phù——a——a——Kua」**. LẬT giá trị audit ("ư aƯ" → "Kua"): くあっ→Kua, っ cuối ngầm trong romaji (quy tắc 3b) — tiền lệ ポーレットh6 806 (audit "Ư a" → moan "Kua").
- **1119 [双鉄]** — JP 「くあっ！！！」 / TW 「唔啊！！！」 / Cũ 「Ku a!!!」 → **「Kua!!!」**. くあっ→Kua (một token).
- **1116 [双鉄]** — JP 「ふくっ！？」 / TW 「唔咕？！」 / Cũ 「Hự!?」 → **「Fuku!?」**. ふくっ→"Hự" mất hẳn âm ふ (TW 唔咕 giữ cả 2 âm tiết); tiền lệ "Fuku!"/"Fuku!!?" ở 2 file khác.
- **1118 [双鉄]** — JP 「うあっ！」 / TW 「唔啊！」 / Cũ 「Ư a!」 → **「Ua!」**. うあ→Ua (Ư diễn sai う thành gasp); tiền lệ "Ua!"/"Ua!!!!" ở 4+ file.
- **1123 [双鉄]** — JP 「あっ――く、はっ――しゃべられ、る、とっ」 / TW 「啊——唔、哈——你一說話……」 / Cũ 「A——ư, ha——em mà, nói, chuyện, thì」 → **「A——Ku, ha——em mà, nói, chuyện, thì」**. く、(nói lắp) → "Ku": VN cũ "ư" mất phụ âm k (mẫu lr-reinah1 1424).
- **1221 [双鉄]** — JP 「僕は、だなっ。そのっ、気持ち――いい、というか――\\nんくっ――あ。少し、びっくり、した、だけ、でっ――」 / TW 「我、呢。不是說什麼——很舒服，只是——唔——啊。有點、驚、慌、失、措、罷了——」 / Cũ 「Anh, là thế này. Việc đó, sướng——à không, phải nói là——\\nƯm——A. Anh chỉ hơi, giật mình, một chút, thôi——」 → **「Anh, là thế này. Việc đó, sướng——à không, phải nói là——\\nƯ hự——A. Anh chỉ hơi, giật mình, một chút, thôi——」**. んくっ→"Ưm" mất âm く; thống nhất trong file theo 1169/1173/1120 ("Ư hự").

## §4. Các dòng rên GIỮ nguyên (đáng chú ý)

- Hơi ngắn ふっ/ぷっ→"phù" giữ (1063, 1086, 1102 ぷ――, 1166 ふ――, 1262, 1270) — tiền lệ ポーレットh6.
- Cười うふふだ→audit "Ufufu~"/"Nfufu~" giữ (1056, 1059, 1185, 1186, 1251) — audit đã sửa, đúng quy tắc cười = tiếng cười.
- 10 dòng sweep-gasp (727, 1233, 1321, 1331, 1332, 1335, 1337, 1475, 1572, 1923) + các fix gasp của audit (1122, 1126, 1132, 1175, 1942) giữ nguyên, không đụng.
- Đếm nguyên âm của audit đã kiểm chứng đúng và giữ: 1063 (きゅう… = 8 u), 1157 (んう… = 6 u), 1189 (ひっきゅう… = 18 u), 1117 (あぁぁ = 3 a), 1135 (はぁああん = 4 a).
- くっ/んくっ→"Hự"/"Ư hự" giữ (723, 1038, 1114, 1120, 1169, 1173, 1259, 1868) — xem cờ F1.
- SFX độc thoại trong （ ） dạng nghĩa Việt giữ toàn bộ (44 dòng: 1053, 1830–1942…): "Phập", "Nhóp nhép", "Trơn tuột", "Sụp soạp", "chụt" cho họ ちゅ… — số lượng chữ lặp chưa chuẩn, xem cờ F4.
- ふわあっ→"Oa" giữ (1094, 1099, 1100) — thán từ ngạc nhiên, không phải rên.
- Nói ngọng/miệng đầy giữ, không phải dòng rên (1007, 1110, 1309, 1245).
- 1048 やぁあ→"Đừng" giữ nhưng cờ F5 (âm rên diễn thành từ).
- 1189 "Hi kyu" giữ nhưng cờ F6 (phụ âm đôi っ giữa từ bị bỏ).
- 1011 かっ→"Kh" — thuộc phạm vi audit (nói lắp, không phải rên), chỉ ghi nhận, không sửa.

## §5. Cờ cho đợt thống nhất / parent (không tự quyết)

- **F1 — くっ/くあっ: "Hự" vs "Ku"/"Kua" vs "Ư".** File này: くっ→"Hự" (1114, 1259, 1038), んくっ→"Ư hự" (1120, 1169, 1173, 1221), nhưng くあっ→"Kua" (1060, 1119, 1117). File khác: くあっ→"Hự!" (ハチロクh4 979, ハチロクh6 872/874) vs "Kua!!!" (lr_ハチロクh1 1217, ハチロクh3 1037). Chưa quyết chung.
- **F2 — ふきゅん: "Fukyun" (file này + 4 file) vs "Hukyun" (ハチロクh7 750).** Chính tả Fu vs Hu cho ふ.
- **F3 — ひあ: "Hia" (quy tắc 3b; ハチロクh1) vs "Hya" (共通13 2023) vs "Hí a"/"Hi a" (ハチロクh5/h6, file này cũ).**
- **F4 — SFX độc thoại （ ） chưa áp công thức đếm** (như h6 F6): số chữ lặp trong VN không khớp số nguyên âm JP — đã đếm máy: 1832 ぢゅろおおおっ (3 o) → "tuộtttttt" (6 t); 1833 じゅこんんんんんん (6 ん) → "sụcccccccccc" (11 c); 1854 じゅりゅううううっ (4 u) → "Sụcccccccc" (10 c); 1861 とろおおおおおおおおおっっっ (9 o) → 11 t; 1878 にゅるうううううっ (5 u) → 9 t; 1881 ぢゅぶりゅう… (14 u) → 20 p; 1893 にゅろお… (13 o) → 17 t; 1894 つー×19 → "dài"+20 i; 1900 ずろぉ×10 → 11 t; 1925 ぞりゅうううううぅぅぅぅぅぅ (10) → 11 t. Cần quyết quy ước đếm cho SFX nghĩa Việt.
- **F5 — 1048 やぁあ→"Đừng":** âm rên phản đối diễn thành từ "Đừng" (やぁ thứ hai cũng "đừng có"); giữ dạng từ hay romaji "Yaaa"? Audit đã chấp nhận dạng từ.
- **F6 — 1189 ひっきゅう… "Hi kyu":** phụ âm đôi っ giữa từ bị bỏ (romaji đầy đủ là "Hikkyu…"); audit chỉ sửa độ dài. Cần quyết cách diễn geminate giữa từ.
- **F7 — 1177 �ん～～～～っ → "ưm~~~~":** っ cuối không có trong sweep, audit không sửa; audit REVIEW đã quyết っ giữa dòng là "đã được diễn" (tiền lệ 仲国05 §4) — ghi nhận, không sửa.
- **F8 — Phán đoán mới, chưa có tiền lệ chéo file:** 1064 ふおっ→"Fuo" (duy nhất trong dự án), 1170 ふひゅんんんんっ→"Fuhyunnnn" (duy nhất trong dự án).
- **F9 — Audit đã cờ fa/fu toàn file cho đợt thống nhất** (audit REVIEW dòng 113, ~40 dòng "Phu a"): file moan này chuyển sang romaji theo quy tắc đã duyệt 21/11 ~01:56 + tiền lệ lr-reinah1 (48 fix cùng mẫu). Nếu Hieu muốn "phà"/"phùa" cho file này thì revert được từ JSON.
- **F10 — 1092/1060 xây trên / lật giá trị audit:** 1092 giữ Ư gasp của audit + gộp token; 1060 lật "ư aƯ"→"Kua" (tiền lệ h6 806 — っ ngầm trong romaji, không mất âm).

## §6. Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 47 fix đối chiếu JP (+TW) lần 2, sau khi đã sửa lỗi `\n` thật → `\n` literal ở lần build đầu (lỗi này chỉ nằm ở dạng lưu trữ, không đổi nội dung fix).
- Tổng: **47 / tái kiểm chứng: 47 / bỏ: 0 / sửa: 0**.
- Kiểm chứng máy: JSON 47 mục dạng chuẩn, khóa string; jp/tw/old_vn khớp CSV3 47/47 (lấy old_vn trực tiếp từ CSV3); mỗi fix chỉ khác old VN ở đúng token rên (47/47 fix ≠ old VN); khối TOML parse bằng tomllib: 47 khóa, 0 sai lệch giá trị; không fix nào chứa っ thô; không dòng "Kh" nào bị đổi; số `\n` literal trong fix = số trong old VN (không thêm/bớt dòng).
- Chồng lấn audit: 6 key — 723 (xây trên audit, giữ "aƯ"), 1060 (lật audit), 1075 + 1077 (xây trên audit: số a + Ư đã đúng), 1092 (xây trên audit: giữ Ư + gộp token), 1133 (xây trên audit: số a đã đúng + gộp token). 41 key còn lại là dòng mới audit không đụng.

## §7. Khối TOML đã kiểm chứng parse (47 khóa, 0 sai lệch giá trị)

```toml
[script]
"723" = "「——Hự——phù——aƯ」"
"724" = "「——Pua——a……. A——Fu, a」"
"736" = "「……Ưm……ưm——\\nFua……a——ưm——ưm ưm」"
"1049" = "「Hyuaaaa——ngực, ngực cũng, thích」"
"1051" = "「Hyau——Fua——tan chảy mất——tan chảy mất thôi,\\nReina, nóng quá——háng cũng, háng cũng, nhầy nhụa rồi」"
"1060" = "「Phù——a——a——Kua」"
"1061" = "「Fua……a……\\nNụ hôn. Ngọt ngào quá——thích lắm luôn nha~」"
"1064" = "「Fuo!!?」"
"1065" = "「Fuya——Yaa——một chút nữa thôi——một chút nữa thôi,\\nnha~——anh Soutetsu ơi~——một chút nữa thôi nha~」"
"1067" = "「Fua——a——a——a!!!」"
"1068" = "「Fua——a——a——Reina, Reina」"
"1069" = "「Fua——a——ra mất——anh ra mất!!!!」"
"1071" = "「Fua——ưm——liếm——chụt——chụt,\\nliếm——ưm chụt——chụt——chụt, chụt」"
"1073" = "「Fua——ngực——ưm——Fu, trơn, trơn——\\nReina, nhũ hoa——nhũ hoa——nhiều, thế này——」"
"1074" = "「Fua」"
"1075" = "「FuaaaaaaanƯƯƯ」"
"1076" = "「Fuaaaa——ngực,\\nReina, ngực tan chảy mất thôi nha~」"
"1077" = "「FuaaaaaanƯƯƯƯ」"
"1078" = "「Fuaaaaaaaaa!!!!」"
"1080" = "「Fuyaaaaaa! Thích——cái này——thích quá\\nanh Soutetsu, ơi~——ưm——cứ thế này, cứ thế này nha~」"
"1081" = "「Fua! A! A! A!\\nA! A! A! A a!!!」"
"1087" = "「Hia——ha! Ha! Fua! Ưm!\\nKyu! Fua! Ha! Ha! Ha! Ha! Ha!」"
"1090" = "「Hyau! Fua! Sướng! Sướng quá!\\nCái to bự, nóng hổi của anh Soutetsu——ưm u!」"
"1092" = "「ƯHyua!!? Sục vào! Đâm phập vào!!\\nNóng quá! Nóng quá ập vào một lúc! Bên trong Reina」"
"1102" = "「Háp——chụt——ưm——liếm——ưm……（Ực）\\nPua——liếm——chụt——phù——（Ực）」"
"1104" = "「Ha! Ha——Fua——Hyau! Anh Soutetsu,\\nReina, Reina! Reina! Ra mất! Ra mất!」"
"1116" = "「Fuku!?」"
"1118" = "「Ua!」"
"1119" = "「Kua!!!」"
"1123" = "「A——Ku, ha——em mà, nói, chuyện, thì」"
"1133" = "「Hyuaaaaaaaaaaaaaaaaaan!!」"
"1156" = "「Fukyun!!!!!」"
"1162" = "「Ưm……Pua」"
"1164" = "「Nhyun!!!」"
"1166" = "「Nyu——phù——cái đó, thích lắm——ưm——khe,\\nkhe háng——cọ, cọ——như vậy——sướng, lắm」"
"1168" = "「Nhyu——Fu, a——trơn, trơn——thích quá」"
"1170" = "「Fuhyunnnn!!!!」"
"1172" = "「Nhyun!!」"
"1177" = "「Ưm——ưm——ưm~~~~——（Ực）\\nPuaa. Đặc sệt luôn, dính cả vào cổ họng nha~」"
"1178" = "「Nyuu!!!」"
"1188" = "「Pua! Tuyệt quá. Tinh dịch của anh Soutetsu,\\nphóng ra với lực mạnh thế này, đây là lần đầu tiên nha~」"
"1202" = "「Nóng quá——Fua——Reina——bị bắn trúng——\\nFu, a——háng——bụng——đầy, đầy ắp rồi」"
"1211" = "「Bên trong, khe——Fu, a——thịt, cũng——\\nlỗ cũng——trơn tuột——tất cả——sướng, lắm」"
"1221" = "「Anh, là thế này. Việc đó, sướng——à không, phải nói là——\\nƯ hự——A. Anh chỉ hơi, giật mình, một chút, thôi——」"
"1283" = "「Đúng vậy……Fu——a——（Ực）——ưm.\\nĐúng là——rất rất——ư——như vậy, nha~」"
"1294" = "「Đúng……vậy, nha~——ưm——Fua——\\nReina, Reina cũng——thấy sướng, lắm luôn nha~」"
"1474" = "「Fua——a——háng——khe——của Reina,\\nkhe hở——ưm——khe hở cũng——hột le, cũng——」"
```

## Kết bài

File lr_れいな追加h_夜の花嫁修業: 365 dòng đã đọc hết, **47 dòng rên đổi (12,9%)** — romaji 42 (họ fa/fu 32 dòng + họ hya/hyu/hia 11 dòng + Kua 2 dòng, có chồng lấn) + mất âm 5. 6 key xây trên/lật giá trị audit (723, 1060, 1075, 1077, 1092, 1133); 41 key mới. 10 mục sweep đã kiểm chứng trực tiếp, 0 trùng key moan; không dòng gasp Ư nào bị đụng (trừ 1060 lật theo tiền lệ h6 806); không dòng "Kh" nào bị đổi; lượt soát 2: 47/47, 0 bỏ, 0 sửa. Cờ cho đợt thống nhất: F1 (くっ "Hự" vs "Ku"/"Kua"), F2 (Fukyun vs Hukyun), F3 (Hia vs Hya), F4 (SFX （ ） chưa áp công thức đếm), F5 (1048 やぁあ→"Đừng"), F6 (1189 geminate ひっきゅ), F7 (1177 っ sau ~~~~), F8 (Fuo/Fuhyunnnn lần đầu trong dự án), F9 (fa/fu audit đã cờ cho thống nhất), F10 (1060/1092 chồng audit).
