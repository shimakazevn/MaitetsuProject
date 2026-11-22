# Moan-fix: 日々姫h4_いもうとタオル.txt.toml — 29 dòng rên/SFX

- File: `02_Hibiki/日々姫h4_いもうとタオル.txt.toml` (route 02_Hibiki, 296 dòng script; 1 bản, không trùng lặp)
- Nội dung: H-scene Hibiki — "khăn tắm em gái" (いもうとタオル): Hibiki dùng cơ thể/khăn tắm phục vụ Soutetsu trong nhà tắm sau ca trực.
- Phương pháp: đọc kỹ từng dòng đối chiếu JP + TW từ CSV3 (91.731 dòng), chỉ xét các dòng rên/thở/gasp/SFX; old_vn = giá trị audit-fix với 29 dòng audit đã sửa, CSV3 với các dòng còn lại. Đếm nguyên âm bằng máy cho mọi chuỗi rên dài. Kiểm tra sweep gasp trực tiếp.
- TOML md5 `5d1c304fe9a442ab317f5087d5e53464`, không có bản trùng; CSV3 1 bộ 296 dòng, key khớp tuyệt đối 296/296, 0 dòng VN trống. Audit file này: 29/296 sai (26 moan, 2 sai nghĩa, 1 SFX) — xem `audit-hibikih4-imouto-taoru-REVIEW.md`.

## Kiểm tra tổng moan (ROUTE-MOANS.md)
- Cơ sở lúc viết snippet: **60 file / 1.418 dòng** (đã rebase lần 2 — cơ sở lúc spawn là 58/1.399, 凪h1 (15 dòng) và 稀咲h2 (4 dòng) đã gộp trong khi agent chạy). File này +29 → **61 file / 1.447 dòng**.

## Kiểm kê rên (đã xét)
- Đọc 296/296 dòng (133 thoại + 163 độc thoại/narration). Dòng rên/thở/SFX đã xét: toàn bộ 133 dòng thoại (quét âm rên) + 35 dòng SFX độc thoại trong （ ）.
- Đổi **29 dòng**: 19 thoại + 10 SFX độc thoại. Phân loại: fa/fu → romaji 14 (972, 988, 990, 991, 995, 1001, 1002, 1006, 1014, 1029, 1032, 1034, 1040, 1041), romaji khác 3 (1035, 1052, 1075), chuỗi dài/đếm nguyên âm 2 (967, 1054), SFX dài/dồn 10 (1743, 1746, 1754, 1757, 1758, 1759, 1762, 1765, 1770, 1783).
- Tiền lệ áp dụng: 日々姫h3 (fa/fu→Fu/Fua/Pua, ふ……ぁっ→Fu……a, んううっ→Nuu, んふう…→Nfuuuu…), ハチロクh3 (ふあっ→Fua, うふふっ→Ufufu, んきゅっ→Nkyu, SFX dài→romaji giữ độ dài), lr_日々姫h2 (ふあっ→Fua, ふぁっ→Fa), lr稀咲追加h/凪h1 (đã gộp; xem cờ F1/F2/F6).

## Chi tiết từng dòng đổi
### 967 [日々姫] — chuỗi dài
- JP: 「きゃひっ！？　あっ――んうううううううっっ！！」
- TW: 「呀！？啊――嗯啊！！」
- VN cũ: 「Kyahi!? A――ưm ư ư ư ư ư ư ư!!」
- VN mới: 「Kyahi!? A――Nuuuuuuu!!」
- Lý do: んうううううううっっ = 8 mora (ん + 7う) → romaji "Nuuuuuuu" (N + 7u; quy tắc F6: mora gốc đã là nguyên âm thì không đếm gấp đôi). VN cũ 8 đơn vị "ưm ư…" vừa dài vừa ngượng, đọc như đếm; tiền lệ ハチロクh3 1064 (んうううううう→"Nuuuuuu"), 日々姫h3 1010 (んううっ→"Nuu").

### 972 [日々姫] — fa/fu
- JP: 「ひゃあっ！？　んっ――ふあっ――おちんちん――\nおして、るっ――おなかっ――までっ――ひうっ」
- TW: 「呀！？嗯――呼――雞雞――頂了進來――頂到了肚子裡面――呀」
- VN cũ: 「Hyaa!? Ưm――phùa――Chim của anh――\nĐang thúc, vào――tận trong bụng――em rồi――Hiu」
- VN mới: 「Hyaa!? Ưm――Fua――Chim của anh――\nĐang thúc, vào――tận trong bụng――em rồi――Hiu」
- Lý do: ふあっ → "Fua" theo romaji fallback (như 日々姫h3 1016/1053/1071/1077/1084, lr_日々姫h2 toàn bộ). ひうっ→"Hiu" giữ nguyên (audit đã sửa đúng).

### 988 [日々姫] — fa/fu
- JP: 「ふあっ――好きっ！　そこっ――しゅきっ！\nおちん、ちんにっ！　ずりって――される――んっ！！」
- TW: 「呼――那裡！我喜歡――那裡！喜歡――被雞雞擦到――嗯！！」
- VN cũ: 「Phùa――Thích quá! Chỗ đó――Thích lắm!\nBởi chim, của anh! Bị cọ xát――như thế――ưm!!」
- VN mới: 「Fua――Thích quá! Chỗ đó――Thích lắm!\nBởi chim, của anh! Bị cọ xát――như thế――ưm!!」
- Lý do: ふあっ → "Fua" (như 972).

### 990 [日々姫] — fa/fu + ふぇ
- JP: 「ふあっ……あっ……あっ――ふえっ――あっ――あ」
- TW: 「呼……啊……啊――呼――啊――啊」
- VN cũ: 「Phùa……a……a――Phuê――a――a」
- VN mới: 「Fua……a……a――Fue――a――a」
- Lý do: ふあっ → "Fua"; ふえっ → "Fue" (ふえ = fu+e). "Phuê" đổi sang romaji cho nhất quán họ fa/fu trong file (994/1006 đã romaji). Cờ F1: ふぇ "Fue" vs "Phuê" chưa chốt toàn dự án (ふかみh1 993, 凪ふかみ01 1547 giữ "Phuê" — xem cờ 凪h1 F1).

### 991 [日々姫] — ふぇ
- JP: 「ふぇ……ぁ……わた……私、おしっこ――おもらし――\n全部……全部して……イっちゃっ――きゅふっ！！？」
- TW: 「呼……啊……我……尿出來了――全部……尿出來了……要去了――呀！！？」
- VN cũ: 「Phuê……a……em……Em, đi tè――tè dầm――\nHết……hết sạch rồi……Lên đỉnh mất――kyufu!!?」
- VN mới: 「Fue……a……em……Em, đi tè――tè dầm――\nHết……hết sạch rồi……Lên đỉnh mất――kyufu!!?」
- Lý do: ふぇ → "Fue" (như 990; TW 呼 = hơi thở, không phải tiếng nấc). Cờ F1.

### 995 [日々姫] — fa/fu
- JP: 「ふあっ！　あっ！　にぃにっ！　してっ！\n全部！　わた、しにっ――私に――[だ,1]射精してっ！！」
- TW: 「呼！啊！阿哥！來吧！全射出來！在我裡面――射出來！！」
- VN cũ: 「Phùa! A! Anh hai! Làm đi anh!\nTất cả! Vào, trong em――Vào trong em――hãy xuất tinh đi!!」
- VN mới: 「Fua! A! Anh hai! Làm đi anh!\nTất cả! Vào, trong em――Vào trong em――hãy xuất tinh đi!!」
- Lý do: ふあっ → "Fua" (như 972).

### 1001 [日々姫] — fa/fu
- JP: 「えっ！？　にぃに――まって、お口、ゆすぐ――んっ、\nあっ――チュッ――ちゅむっ――んっ――ふあっ――」
- TW: 「哎！？阿哥――等等，我漱漱口――嗯、啊――啾――啾嚕――嗯――呼――」
- VN cũ: 「Hả!? Anh hai――đợi đã, để em súc miệng――ưm,\na――chụt――chùn chụt――ưm――phùa――」
- VN mới: 「Hả!? Anh hai――đợi đã, để em súc miệng――ưm,\na――chụt――chùn chụt――ưm――Fua――」
- Lý do: ふあっ cuối dòng → "Fua" (viết hoa giữa dòng theo tiền lệ 日々姫h3 1077).

### 1002 [日々姫] — fa/fu
- JP: 「はむっ――ふっ――ちゅっ――ちゅむっ」
- TW: 「唔――呼――啾――啾噗」
- VN cũ: 「Ngoạm――phù――chụt――chùn chụt」
- VN mới: 「Ngoạm――Fu――chụt――chùn chụt」
- Lý do: ふっ → "Fu" (tiền lệ 日々姫h3 1013/1055/1109/1142).

### 1006 [日々姫] — fa/fu
- JP: 「あっ――ふあっ――ふあああああああああんっ！！！」
- TW: 「啊――呼――呼啊――！！！」
- VN cũ: 「A――phùa――Fuaaaaaaaaan!!!」
- VN mới: 「A――Fua――Fuaaaaaaaaan!!!」
- Lý do: ふあっ ngắn → "Fua" cho nhất quán với rên dài cùng dòng đã romaji ("Fuaaaaaaaaan", 9 a — audit đã đếm máy). Đây chính là điểm cờ (1) của audit ("file dùng cả hai"); vòng moan chốt romaji cả hai.

### 1014 [日々姫] — fa/fu
- JP: 「あ……これ……ん……タオルな……私、も……\n気持ち……い……んっ――ふっ――」
- TW: 「啊……這樣……嗯……我這條……毛巾也……好舒服……嗯――呼――」
- VN cũ: 「A……Cái này……ưm……Khăn tắm là……em, cũng……\nSướng……quá……ưm――phù――」
- VN mới: 「A……Cái này……ưm……Khăn tắm là……em, cũng……\nSướng……quá……ưm――Fu――」
- Lý do: ふっ cuối dòng → "Fu" (như 1002).

### 1029 [日々姫] — fa/fu
- JP: 「んっ――んー……ん、ふっ――あむっ――れろっ――\nちゅくっ――ちゅむっ――じゅうっ――ちゅぶっ」
- TW: 「嗯――嗯――……嗯、呼――唔――啾噗――啾噗――啾噗――啾――啾噗」
- VN cũ: 「Ưm――ưm……ưm, phù――ngoạm――liếm――\nChụt――chùn chụt――chụt――chụt」
- VN mới: 「Ưm――ưm……ưm, Fu――ngoạm――liếm――\nChụt――chùn chụt――chụt――chụt」
- Lý do: ふっ → "Fu" (như 1002). れろっ→"liếm" giữ (tiền lệ 日々姫h3 1027).

### 1032 [日々姫] — fa/fu (ふぁ + ふ、ぁっ)
- JP: 「ん……ふぁ――乳首……いい――ふ、ぁっ」
- TW: 「嗯……呼――乳頭……好舒服――呼、啊」
- VN cũ: 「Ưm……phà――Núm vú……sướng quá――phà, a」
- VN mới: 「Ưm……Fa――Núm vú……sướng quá――Fu, a」
- Lý do: ふぁ (1 mora) → "Fa" (tiền lệ lr_日々姫h2 1173: ふぁっ→"Fa!"); ふ、ぁっ (ngắt nhịp) → "Fu, a" (tiền lệ 日々姫h3 1112: ふ……ぁっ→"Fu……a" — tách ふ thành "Fu", ぁ thành "a", đúng như JP ngắt).

### 1034 [日々姫] — fa/fu
- JP: 「ん……ふっ――あっ――んっ……ん……\nどぉお？　にぃにも……気持ち……いい？」
- TW: 「嗯……呼――啊――嗯……嗯……怎麼樣？阿哥也……舒服嗎……？」
- VN cũ: 「Ưm……phù――a――ưm……ưm……\nSao hả? Anh hai cũng……sướng……chứ?」
- VN mới: 「Ưm……Fu――a――ưm……ưm……\nSao hả? Anh hai cũng……sướng……chứ?」
- Lý do: ふっ → "Fu" (như 1002).

### 1035 [日々姫] — romaji (んぇっ mất phụ âm)
- JP: 「ん……むっ――んぇっ――」
- TW: 「嗯……唔――嗯――」
- VN cũ: 「Ưm……ưm――ưm――」
- VN mới: 「Ưm……ưm――Ne――」
- Lý do: cờ (4) của audit — んぇっ → "ưm" làm mất hẳn phụ âm ぇ sau ん. Romaji んぇ = "Ne" (ん→N, ぇ→e, Hepburn; っ hấp thụ vào ――). むっ→"ưm" giữ (む = tiếng hừ mũi, đúng âm). Cờ F8: dạng "Ne" chưa có tiền lệ.

### 1040 [日々姫] — fa/fu + んくっ
- JP: 「ん……ちゅうっ……ちゅっ――あむっっ――んっ――\nちゅき――にぃに……れるっ……ん……ふ……んくっ」
- TW: 「嗯……啾……啾――唔――嗯――我喜歡――阿哥……啾噗……嗯……呼……嗯」
- VN cũ: 「Ưm……chụt……chụt――ngoạm――ưm――\nYêu――anh hai……liếm……ưm……phù……ưm」
- VN mới: 「Ưm……chụt……chụt――ngoạm――ưm――\nYêu――anh hai……liếm……ưm……Fu……Nku」
- Lý do: cờ (4) của audit — んくっ → "ưm" làm mất hẳn phụ âm k sau ん; romaji んくっ = "Nku" (tiền lệ ハチロクh3 1218: んきゅっ→"Nkyu"). ふ…… → "Fu……". Cờ F8.

### 1041 [日々姫] — fa/fu (ぷぁ)
- JP: 「ん……ぷっ……ぷぁ――あ～」
- TW: 「嗯……噗……噗――啊～」
- VN cũ: 「Ưm……phụt……phà――A~」
- VN mới: 「Ưm……phụt……Pua――A~」
- Lý do: ぷぁ → "Pua" (ぷ=p, ぁ=a; tiền lệ 日々姫h3 1056/1111/1114: ぷあっ→"Pua"). ぷっ→"phụt" giữ (tiếng bật ngắn, đã đúng).

### 1052 [日々姫] — romaji (cười + liếm dài)
- JP: 「んふふっ――れろおおおっ」
- TW: 「嗯呼呼――啾噗」
- VN cũ: 「Ưm fufu――liếm láp」
- VN mới: 「Nfufu――Reroooo」
- Lý do: んふふっ → "Nfufu" (tiền lệ ハチロクh3 1009: うふふっ→"Ufufu"; 日々姫h3 1124: んふ…→"Nf…"). れろおおおっ (5 mora, 3お kéo dài) → "Reroooo" (れ=re, ろ=ro, お×3=ooo): đây là dòng âm thanh độc lập, "liếm láp" làm mất hẳn độ dài; các れろっ/ぺろっ NGẮN trong câu (1004/1022/1029) vẫn giữ "liếm" theo tiền lệ 日々姫h3 1027. Cờ F3 (viết hoa "Nfufu" — xem cờ lr_日々姫h2) + F6 (liếm dài → romaji hay giữ "liếm láp").

### 1054 [日々姫] — chuỗi dài + mất phụ âm k
- JP: 「くひゅううううううううんっ！！！」
- TW: 「嗯啊！！！」
- VN cũ: 「Ưm hyuuuuuuuuun!!!」
- VN mới: 「Kuhyuuuuuuuuun!!!」
- Lý do: くひゅううううううううんっ = 10 u (く1 + ひゅ1 + う×8) + ん. VN cũ "Ưm" cho く làm mất hẳn phụ âm k (く là tiếng "ku", không phải hừ mũi ん); romaji "Kuhyuuuuuuuuun" giữ đủ k + 10 u (đã đếm máy). Tiền lệ: ハチロクh3 1029 (くあぁっ→"Kuaa"), 凪h1 cờ F6 (くっ "Ku" trong thoại vs "Ư" trong SFX mô tả).

### 1075 [日々姫] — romaji (んきゅっっ)
- JP: 「深っ――コレッ――んあっ！　違うとこ――ぐりって！\nひぁっ――あっ――えぐれ――って――んきゅっっ！！」
- TW: 「好深――這樣――嗯！頂的地方――不對！呀――啊――插到了――嗯哼！！」
- VN cũ: 「Sâu quá――Thế này――ưm a! Chỗ khác――bị ngoáy rồi!\nHia――a――Bị khoét sâu――vào trong――ưm kyu!!」
- VN mới: 「Sâu quá――Thế này――ưm a! Chỗ khác――bị ngoáy rồi!\nHia――a――Bị khoét sâu――vào trong――Nkyu!!」
- Lý do: んきゅっっ → "Nkyu!!" (tiền lệ ハチロクh3 1218: んきゅっ→"Nkyu"; 日々姫h3 1016 giữ "Nkyuuu!" cho んきゅううっ). ひぁっ→"Hia" giữ nguyên (audit đã sửa đúng).

### 1743 [monologue] — SFX
- JP: （ぐりっ――ぐいっ――ずろおおおっ！　ずんっ！！）
- TW: （來回抽插）
- VN cũ: （Ngoáy——Thúc——Phập! Phập!!）
- VN mới: （Ngoáy——Thúc——Zuroooo! Phập!!）
- Lý do: ずろおおおっ (5 mora, 3お) → "Zuroooo" (ず=zu, ろ=ro, お×3=ooo) giữ độ dài; "Phập!" làm mất hẳn 3お. ぐりっ→"Ngoáy" và ぐいっ→"Thúc" giữ (động tác xoáy/đẩy, TW ủng hộ); ずんっ→"Phập!!" giữ (đâm ngắn, đúng từ).

### 1746 [monologue] — SFX
- JP: （ぷりゅんっ！）
- TW: （咕嚕！）
- VN cũ: （Bịch!）
- VN mới: （Puryun!）
- Lý do: ぷりゅんっ là tiếng nảy/lắc ướt, nhẹ (puryun); "Bịch!" là tiếng thịch nặng — sai hẳn họ âm. TW 咕嚕 (ục ục) cũng không phải tiếng thịch. Romaji "Puryun!" giữ đúng âm. Cờ F5: chưa có tiền lệ cho ぷりゅん.

### 1754 [monologue] — SFX dồn
- JP: （じゅぶっ！　じゅっっ！　じゅばっっ！　じゅぼっ！）
- TW: （啾噗！啾噗！噗啾！噗啾！）
- VN cũ: （Phập! Phập! Phập! Phập!）
- VN mới: （Jubu! Ju!! Juba!! Jubo!）
- Lý do: cờ (3) của audit — 4 SFX ướt KHÁC NHAU (じゅぶ/じゅ/じゅば/じゅぼ, っ đơn vs っ đôi) bị gộp thành 4×"Phập!" giống hệt. Romaji giữ đủ các điểm khác biệt: bu/ba/bo + っ đơn (!!) vs っ đôi (!!). Cờ F4: quy tắc chung cho dãy じゅ/ず dồn (xem 1759/1760).

### 1757 [monologue] — SFX dài
- JP: （ずぶうううううううううっ！！！）
- TW: （噗呲！！！）
- VN cũ: （Phập!!!）
- VN mới: （Zubuuuuuuuuuu!!!）
- Lý do: ずぶ + 9う = 11 mora → "Zubu" + 9u = 11 u (đã đếm máy); "Phập!!!" làm mất hẳn 9u. Tiền lệ ハチロクh3 1835 (ずぶうううううううううううっ→"Zubuuuuuuuuuuuu!!!").

### 1758 [monologue] — SFX dài
- JP: （ぷっ――ちょろっ――ちょっおおおおおおおおっ！！）
- TW: （噗哧――噗呲――！！）
- VN cũ: （Phụt——Tí tách——Phụt!!）
- VN mới: （Phụt——Tí tách——Chooooooooo!!）
- Lý do: ちょっおおおおおおおおっ = ちょ + 8お → "Cho" + 8o = 9 o (đã đếm máy); "Phụt!!" làm mất hẳn độ dài. ぷっ→"Phụt" giữ (bật ngắn); ちょろっ→"Tí tách" giữ (tiếng nhỏ giọt VN đúng âm).

### 1759 [monologue] — SFX dồn
- JP: （ずばっ！　じゅぶっ！　ずぶっ！　すぱんっ！！）
- TW: （噗啾！噗啾！啾噗！啾噗！！）
- VN cũ: （Bạch! Phập! Phập! Bạch!!）
- VN mới: （Phập! Phập! Phập! Bạch!!）
- Lý do: chỉ ずばっ sai — "Bạch!" là tiếng tát, còn ずばっ là tiếng đâm ướt (cùng họ với じゅぶっ/ずぶっ → "Phập!"). すぱんっ→"Bạch!!" giữ (すぱん đúng là tiếng tát/vỗ). Cờ F4.

### 1762 [monologue] — SFX dồn
- JP: （びゅううっ！　びゅるうっ！　びゅっ！　びゅう！！）
- TW: （噗噗！噗嚕！噗噗！噗噗！！）
- VN cũ: （Phụt! Phụt! Phụt! Phụt!!）
- VN mới: （Byuuu! Byuruu! Byu! Byuu!!）
- Lý do: 4 tiếng phun KHÁC NHAU gộp thành 4×"Phụt!": びゅううっ→"Byuuu" (3 u), びゅるうっ→"Byuruu" (3 u, giữ る), びゅっ→"Byu", びゅう→"Byuu" (2 u). Romaji giữ đủ độ dài + phụ âm る.

### 1765 [monologue] — SFX dài
- JP: （びゅううううううううううっっ！！！）
- TW: （噗嚕嚕！！！）
- VN cũ: （Phụt!!!）
- VN mới: （Byuuuuuuuuuuu!!!）
- Lý do: びゅ + 10う = 11 mora → "Byu" + 10u = 11 u (đã đếm máy); "Phụt!!!" làm mất hẳn 10u.

### 1770 [monologue] — SFX dồn
- JP: （びゅっ！　びゅううっ！　びゅるっ――びゅっ――）
- TW: （噗！噗噗！噗嚕――噗嚕――）
- VN cũ: （Phụt! Phụt! Phụt——Phụt——）
- VN mới: （Byu! Byuuu! Byuru――Byu――）
- Lý do: như 1762 — びゅっ→"Byu", びゅううっ→"Byuuu" (3 u), びゅるっ→"Byuru" (giữ る), びゅっ→"Byu". Dấu ―― giữ nguyên theo JP.

### 1783 [monologue] — SFX dài nhất file
- JP: （ずろおおぽおおおおおおおおおおっ！！）
- TW: （插入！！）
- VN cũ: （Phập!!）
- VN mới: （Zurooopooooooooooo!!）
- Lý do: ずろおおぽおおおおおおおおおおっ = 16 mora, 14 o (ろ1 + お×2 + ぽ1 + お×10) → "Zurooo" + "po" + 10 o = 14 o (đã đếm máy); "Phập!!" làm mất hẳn toàn bộ độ dài + âm ぽ giữa. Đây là SFX dài nhất file (audit cờ (3)).

## Các dòng rên đã giữ (đáng chú ý)
- 960 やっ→"Ya", 963/966/969 ひあっ→"Hia", 964 ふやっ→"Phuya" + rên dài 14 a (giữ "Phuya" theo tiền lệ 日々姫h3 1042; cờ F2), 971 ひゃっ→"Hya" + んううっ→"ưm ư ư" (3 mora, ngắn, đúng số lượng — khác 967 dài 8 mora), 962 んうっ→"ưm ư" (2 mora, ngắn, đúng), 1005 ぁあ→"Aa" (2 a), 1024 gasp っ→"Ư" (audit; dòng gasp KHÔNG xét lại), 1182/1183 gasp toàn dòng →"Ư" (sweep, KHÔNG xét lại).
- 974 やぁあん→"Yaaan" (3 a: やぁ=2 + あ=1, đúng), 1009 やっ→"ya" (viết thường giữa dòng — tiền lệ cùng file, audit đã dẫn), 987 ずぞおおおおおおっっっ→"Zuzooooooo" (7 o: ぞ1 + お×6, đã romaji đúng), 994 ふああああああっ→"Fuaaaaaa" (6 a, đã romaji đúng), 997 くぽっ→"Kupo", 1019 はうっ→"Hau", 976 くあっ→"Kua", 965 ひゃんっ→"Hyan", 1058 きゃ/きゃあっ→"Kya, kyaa".
- 993 っと→"Hự" — XÁC NHẬN phán đoán của audit (tiền lệ cùng file 1028 くっ→"hự"; っと là âm tắc /t/, "Phù" làm mất hẳn âm tắc). Cờ (2) của audit đã giải quyết.
- 1025 ううう～っ→"Ư ư ư~" (tiếng nức nở xin lỗi, 3 u đúng số lượng — không phải rên H), 1026 あぅぅ～→"Auu~" (3 mora đúng), 949 あああ→"Aaa".
- 1051 んひいいっ→"Ưm hiii" (3 i đúng; ん→"Ưm" đúng vì ん là hừ mũi), 1053 んふうううっ→"Ưm phuuuu" (4 u đúng, ngắn, tự nhiên — khác 1124 日々姫h3 dài 13 mora → "Nfuuuu…").
- 1038/1022/1004 ちゅ/ちゅむ/れる/ぺろ → "chụt/chùn chụt/liếm" giữ (cách diễn đã chốt toàn dự án cho họ ちゅ; れろっ ngắn trong câu giữ "liếm" theo 日々姫h3 1027).
- 984 んぺっ→"Phụt", んえっ→"Oẹ" giữ (tiếng khạc/ọe, TW 呸 ủng hộ — khác 1035 んぇっ→"Ne" là tiếng rên mũi trong chuỗi rên).
- 1045 っ giữa câu sau ―― đã bỏ, giữ nguyên (dấu ―― diễn ngắt câu; audit đã quyết).
- 1065 「ん～～――――ンム～っ」→"Ưm~~――――Ưm~" giữ (sweep already-rendered, đã kiểm chứng).
- SFX độc thoại giữ: 1755 （ざばあっ）→"Rào!", 1793 （ちゃぽんっ）→"Tùm", 1789 （とくんっ）→"Thịch——Thịch——", 1756/1796 （とろ…）→"Chảy xuống" (dòng chảy nhớt — diễn nghĩa, không ngượng), 1747 （ねとおおおっ）→"Nhớt nháp", 1788 （にゅるううううっ）→"Trượt dài!" ("dài" giữ độ dài), 1768/1787 dãy trượt (từ nghĩa giữ độ dài/khác biệt), 1773/1774/1781/1790 họ siết ("Kẹp chặt"/"Bóp nhẹ"/"Siết——Siết chặt" — audit đã xác nhận trùng VN hợp lệ theo TW), 1795/1778/1775/1785/1766/1779 SFX ngắn diễn nghĩa (TW ủng hộ), 1750 （てろおっ）→"Liếm láp" (liếm ngắn; khác 1052 れろおおおっ dài → romaji), 1760 4 SFX đều đúng từ ("Bạch! Bạch! Phập! Phập!" — すぱん/ぱん là tát, ずぶ/ずぱん là đâm), 1782 （ずんっっっっっ）→"Thúc mạnh!!!" + 1794 （ずっっっっっ――――ごりゅううううっつ）→"Thúc mạnh――――Nghiến chặt!!!" (cặp っ×5 nhất quán, audit vừa sửa 1794; !!! diễn nhấn stutter — cờ F7).

## Kiểm tra sweep gasp (trực tiếp trong sweep-raw-gasp-wrong.json)
- File này có 3 mục sweep: 1182 + 1183 (lost-gasp-whole) đã áp trong audit — KHÔNG xét lại (dòng Ư); 1065 (already-rendered) giữ nguyên. Audit tìm thêm 1 gasp sweep bỏ sót (1024) đã áp trong audit — KHÔNG xét lại. Không còn gasp nào bị sót.

## Cờ cho đợt thống nhất (unification)
- F1: ふぇ "Fue" vs "Phuê" (990/991 đổi sang "Fue"; ふかみh1 993 + 凪ふかみ01 1547 giữ "Phuê" — xem cờ 凪h1 F1). Cần chốt 1 dạng toàn dự án.
- F2: ふや "Phuya" vs "Fuya" (964 giữ "Phuya" theo 日々姫h3 1042; xem cờ 凪h1 F2).
- F3: "Nfufu" viết hoa (1052; xem cờ lr_日々姫h2 "nfufu" vs "Nfufu").
- F4: dãy SFX じゅ/ず dồn — romaji hay "Phập!" (1754 romaji cả 4; 1759 chỉ sửa ずばっ→"Phập!"; 1760 giữ nguyên 4×VN). Cần quy tắc chung cho SFX dồn.
- F5: ぷりゅんっ → "Puryun!" (1746; chưa có tiền lệ; "Bịch!" sai họ âm).
- F6: れろ dài → romaji hay "liếm láp" (1052 れろおおおっ→"Reroooo"; các れろっ/ぺろっ ngắn vẫn "liếm").
- F7: SFX っ×5 stutter → "Thúc mạnh" (1782/1794 giữ) hay romaji ("Zun…"/"Zuzuzuzuzu").
- F8: dạng romaji mới cho ん+phụ âm: んぇっ→"Ne" (1035), んくっ→"Nku" (1040) — tiền lệ ハチロクh3 1218 (んきゅっ→"Nkyu").
- F9: く đầu rên → "Ku" (1054 くひゅ→"Kuhyu…"; xem cờ 凪h1 F6: くっ "Ku" trong thoại vs "Ư" trong SFX mô tả).

## Lượt soát 2 (bắt buộc)
- Đã soát lại toàn bộ 29 fix lần 2 so với JP + đếm nguyên âm bằng máy: **29/29 tái kiểm chứng, 0 bỏ, 0 sửa**. JSON 29 mục (key chuỗi); jp/tw/old_vn khớp CSV3 tuyệt đối 29/29 (old_vn = audit-fix với 12 dòng audit đã sửa, CSV3 với 17 dòng còn lại); diff cơ học old→fix cho thấy mỗi fix chỉ khác VN cũ ở đúng token rên cần sửa (29/29). Đếm nguyên âm đã kiểm chứng bằng máy: 967 8 mora→"Nuuuuuuu" (N+7u), 1054 10u→"Kuhyuuuuuuuuun", 1757 11u→"Zubuuuuuuuuuu", 1758 9o→"Chooooooooo", 1765 11u→"Byuuuuuuuuuuu", 1783 14o→"Zurooopooooooooooo", 1743 4o→"Zuroooo", 1762 Byuuu/Byuruu/Byu/Byuu, 1770 Byu/Byuuu/Byuru/Byu, 1052 Reroooo (4 o).

## Khối TOML (đã parse-kiểm chứng — 29 khóa, 0 sai lệch giá trị so với JSON)

```toml
[script]
"967" = "「Kyahi!? A――Nuuuuuuu!!」"
"972" = "「Hyaa!? Ưm――Fua――Chim của anh――\\nĐang thúc, vào――tận trong bụng――em rồi――Hiu」"
"988" = "「Fua――Thích quá! Chỗ đó――Thích lắm!\\nBởi chim, của anh! Bị cọ xát――như thế――ưm!!」"
"990" = "「Fua……a……a――Fue――a――a」"
"991" = "「Fue……a……em……Em, đi tè――tè dầm――\\nHết……hết sạch rồi……Lên đỉnh mất――kyufu!!?」"
"995" = "「Fua! A! Anh hai! Làm đi anh!\\nTất cả! Vào, trong em――Vào trong em――hãy xuất tinh đi!!」"
"1001" = "「Hả!? Anh hai――đợi đã, để em súc miệng――ưm,\\na――chụt――chùn chụt――ưm――Fua――」"
"1002" = "「Ngoạm――Fu――chụt――chùn chụt」"
"1006" = "「A――Fua――Fuaaaaaaaaan!!!」"
"1014" = "「A……Cái này……ưm……Khăn tắm là……em, cũng……\\nSướng……quá……ưm――Fu――」"
"1029" = "「Ưm――ưm……ưm, Fu――ngoạm――liếm――\\nChụt――chùn chụt――chụt――chụt」"
"1032" = "「Ưm……Fa――Núm vú……sướng quá――Fu, a」"
"1034" = "「Ưm……Fu――a――ưm……ưm……\\nSao hả? Anh hai cũng……sướng……chứ?」"
"1035" = "「Ưm……ưm――Ne――」"
"1040" = "「Ưm……chụt……chụt――ngoạm――ưm――\\nYêu――anh hai……liếm……ưm……Fu……Nku」"
"1041" = "「Ưm……phụt……Pua――A~」"
"1052" = "「Nfufu――Reroooo」"
"1054" = "「Kuhyuuuuuuuuun!!!」"
"1075" = "「Sâu quá――Thế này――ưm a! Chỗ khác――bị ngoáy rồi!\\nHia――a――Bị khoét sâu――vào trong――Nkyu!!」"
"1743" = "（Ngoáy——Thúc——Zuroooo! Phập!!）"
"1746" = "（Puryun!）"
"1754" = "（Jubu! Ju!! Juba!! Jubo!）"
"1757" = "（Zubuuuuuuuuuu!!!）"
"1758" = "（Phụt——Tí tách——Chooooooooo!!）"
"1759" = "（Phập! Phập! Phập! Bạch!!）"
"1762" = "（Byuuu! Byuruu! Byu! Byuu!!）"
"1765" = "（Byuuuuuuuuuuu!!!）"
"1770" = "（Byu! Byuuu! Byuru――Byu――）"
"1783" = "（Zurooopooooooooooo!!）"```

## Kết bài
File 日々姫h4_いもうとタオル.txt.toml: 296 dòng đã đọc kỹ từng dòng đối chiếu JP + TW, 29 dòng rên/SFX đổi sang romaji hoặc sửa âm (19 thoại + 10 SFX độc thoại) — fa/fu→romaji 14, romaji khác 3, chuỗi dài 2, SFX dài/dồn 10. Không sửa đại từ/thuật ngữ/nghĩa. Sweep gasp kiểm tra trực tiếp 3/3 mục (2 Ư đã áp trong audit, 1 already-rendered) — không xét lại dòng Ư. 9 cờ cho đợt thống nhất (F1–F9: ふぇ Fue/Phuê, ふや Phuya/Fuya, Nfufu viết hoa, dãy じゅ/ず dồn, ぷりゅん, れろ dài, っ×5, ん+phụ âm mới, く→Ku). Đã soát lại toàn bộ 29 fix lần 2 (29/29/0/0).
