# Audit: lr_凪h1_痛いの痛いの飛んでけばい — 22 dòng Việt sai (đã đối chiếu JP + TW)

**Kết quả: 22/304 dòng sai (7,2%)** — lệch dòng 1, sweep 19, SFX 1, đại từ 1. 0 chưa dịch, 0 trùng key, 0 tràn file khác, 0 dòng mồ côi, 0 chuỗi xoay vòng. Cảnh: Nagi luyện kiếm làm gãy kiếm gỗ, mảnh kiếm văng trúng háng Soutetsu; Nagi chữa đau bằng "thổi bay cơn đau" (痛いの痛いの飛んでけ) rồi cảnh chuyển sang H; Soutetsu muốn ngực Nagi to lên / ra sữa.

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 304 dòng script** (độc thoại 134, Nagi 100, Soutetsu 70) đối chiếu JP + TW từ CSV3 "Trang tính 3", target là TOML-2. TW khớp đúng thứ tự với JP ở toàn file nên dùng được làm nhân chứng thứ hai cho mọi phán đoán.
- CSV3 chỉ có **1 bộ 304 dòng** cho file này (không có dual-set); key khớp TOML tuyệt đối 304/304. 160 dòng khác TOML chỉ ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng — CSV3 (literal `\n`) là chuẩn cho danh sách sửa. 0 dòng VN trống, 0 dòng VN == TW. `[selections]` rỗng ({}). TOML md5 3b4b468a7b4e2fc41327c15a75dd230c, BOM + CRLF; không có bản sao trùng nội dung trong toml2/ (chỉ 1 file có md5 này).
- Phân loại lỗi: lệch dòng 1, sweep 19, SFX 1, đại từ 1. Theo người nói: Nagi 10, Soutetsu 10, độc thoại 2.
- Kiểm tra chuỗi xoay vòng: dòng lệch duy nhất (1121) là lỗi giải mã lời nói ngọng (miệng đầy), không phải dòng bị đẩy — VN đúng của nó không nằm ở key nào khác trong file hay trong toàn dự án, nên dịch mới từ JP.
- Kiểm tra tràn file khác: đối chiếu từng VN dài (≥15 ký tự) với chỉ mục VN toàn dự án — 6 trùng đều là SFX chung chung ("Phụt!×4", "Phập!×4") hoặc câu ngắn thông dụng ("Tất nhiên rồi") vốn lặp lại hợp lệ; **0 dòng tràn file khác**.
- Kiểm tra sweep: 13 mục cho file này — 9 mục fix áp dụng nguyên (1178, 1208, 1211, 1212, 1215, 1515, 1209, 1193, 1124); 2 mục already-rendered (1135, 1155) thực ra vẫn sót っ cuối dòng sau dấu ――/～～ nên đã sửa; 2 mục needs-file-audit (1223, 1272) đã xử lý: VN khớp đúng JP, chỉ thiếu っ cuối dòng (1272 bỏ thêm "đó!" không có cơ sở JP). Ngoài ra audit tự tìm thêm 6 gasp sweep bỏ sót: 1126, 1173, 1183, 1210, 1213, 1231.
- Kiểm tra thẻ `%l`: 0 thẻ trong file (không có thuật ngữ cần gloss ở file này).
- Lượt soát 2: **22 tổng / 22 tái kiểm chứng / 0 loại bỏ / 0 sửa lại** (đọc lại toàn bộ 22 giá trị fix đối chiếu JP, xem ở cuối phần chi tiết).

## Kết luận về cơ chế lỗi

Lỗi chính là **gasp っ bị mất (19/22)**: file này gần như toàn cảnh H với hàng loạt dòng chỉ toàn tiếng rên/SFX, và bản dịch Gemini thường chỉ giữ dấu câu mà bỏ mất âm っ — cả dòng chỉ có っ + dấu câu (1208, 1211, 1212, 1215, 1193, 1209), っ cuối dòng sau ――/～～ (1124, 1135, 1155, 1223, 1272, 1515), っ đầu dòng (1210, 1213) và っ rời giữa câu sau dấu ―― (1126, 1173, 1183, 1231). Sweep đã bắt 9, còn sót 10 (6 bỏ sót hẳn + 2 phân loại already-rendered sai + 2 needs-file-audit). Quy tắc phân biệt đã áp dụng nhất quán: っ đứng riêng sau ――/～～/… hoặc đứng một mình đầu/cuối dòng = gasp (sửa thành Ư); っ gắn liền cuối từ (1131 んひゅぁぁ…っっ, 1224/1225 チェストー…っ, 1161 んひゅんんっ, 1192 はひゅっ, 1130 っ giữa từ, 1134 ――っと, 1280 よ～っんっ, 1358 声っ, 1648 ぎちっ・っと) = nhấn mạnh cắt ngang, giữ nguyên.

Ngoài ra 3 lỗi rải rác: 1121 Gemini bịa "ngốc nghếch" cho lời nói ngọng (giải mã đúng là "nếu uống tinh dịch của anh hai" — xem chi tiết); 1170 mất phụ âm k (かっ→"A"); 1567 độc thoại Soutetsu dùng "anh" thay vì "tôi" (dòng độc thoại duy nhất trong file dùng "anh", đã kiểm chứng cơ học).

## Chi tiết dòng sai

### Lệch dòng — lời nói ngọng bị dịch sai (1 dòng)

- **1121** [凪] — Nagi nói ngọng (miệng đầy) — VN cũ bịa "ngốc nghếch", mất hẳn mệnh đề chính. Giải mã theo quy tắc phụ âm→h khi nói ngọng: ひーはんほ = にーさんの, へーへひ = せいえき (tinh dịch), ほんはら = のんだら (nếu uống). Bằng chứng song song: key 1237 cùng cảnh, cùng các từ ngọng này, VN đã giải mã đúng ("tinh dịch của anh hai, uống hết") và TW cũng xác nhận 本小姐. TW ở 1121 ("原因在大哥哥") dịch thoáng, không theo — JP thắng. Phần cười ngọng cuối dòng giữ nguyên âm.
  JP: 「ひーはんほへーへひほんはら――んっ――ヂュルッ――\nれるっ――ん――あふぁはは、ひょふひゃっはふほへ～」
  TW: 「原因在大哥哥——啾嚕啾嚕——啾噗啾噗，噗哈——」
  Cũ: 「Vì anh hai ngốc nghếch――ưm――chụt――\nreru――ưm――afahaha, hyofuhyahhafuhouhe~」
  Mới: 「Nếu uống tinh dịch của anh hai――ưm――chụt――\nreru――ưm――afahaha, hyofuhyahhafuhouhe~」

### Sweep — gasp っ bị mất (19 dòng)

**Sweep áp nguyên (9 dòng):**

- **1178** [双鉄] — っ cuối dòng sau ―― (ぁっ――っ！): thêm Ư.
  JP: 「ぁっ――っ！」
  TW: 「啊……啊！」
  Cũ: 「Á――!」
  Mới: 「Á――Ư!」
- **1208** [双鉄] — Cả dòng chỉ có っ + !!: thêm Ư.
  JP: 「っ！！」
  TW: 「啊！！」
  Cũ: 「!!」
  Mới: 「Ư!!」
- **1209** [双鉄] — Cả dòng っ×4 + !!!!: thêm Ư×4 (bổ sung đa-っ 19/11).
  JP: 「っっっっ！！！！」
  TW: 「啊！！！」
  Cũ: 「!!!!」
  Mới: 「ƯƯƯƯ!!!!」
- **1211** [双鉄] — Cả dòng っ + !!!!: thêm Ư.
  JP: 「っ！！！！」
  TW: 「啊！！！！」
  Cũ: 「!!!!」
  Mới: 「Ư!!!!」
- **1212** [双鉄] — Cả dòng っ + !!!!!: thêm Ư.
  JP: 「っ！！！！！」
  TW: 「啊！！！！！」
  Cũ: 「!!!!!」
  Mới: 「Ư!!!!!」
- **1215** [双鉄] — Cả dòng っ + !?: thêm Ư.
  JP: 「っ！？」
  TW: 「啊？！」
  Cũ: 「!?」
  Mới: 「Ư!?」
- **1193** [双鉄] — Cả dòng っ×2 + !!!!: thêm Ư×2 (bổ sung đa-っ 19/11).
  JP: 「っっ！！！！」
  TW: 「啊啊！！！！」
  Cũ: 「!!!!」
  Mới: 「ƯƯ!!!!」
- **1124** [凪] — っ×5 cuối dòng sau ~~~~~~~~: thêm Ư×5 (bổ sung đa-っ 19/11).
  JP: 「ぃっ――ぁっ――～～～～～～～～っっっっっ！！」
  TW: 「呀……啊……啊！！」
  Cũ: 「I——a——~~~~~~~~!!」
  Mới: 「I——a——~~~~~~~~ƯƯƯƯƯ!!」
- **1515** [monologue] — っ cuối dòng sau ―― trong độc thoại: thêm Ư.
  JP: 脱力しきって甘えて来る声。\n僕も脱力しきっているが、応えたくって――っ！！！？
  TW: 凪的聲音是徹底脫力之後的撒嬌聲音。我也徹底脫力了，但我很想回應她……啊？！
  Cũ: Giọng nói nũng nịu cất lên khi em đã hoàn toàn kiệt sức.\nTôi cũng kiệt sức rồi, nhưng vẫn muốn đáp lại em——!!!?
  Mới: Giọng nói nũng nịu cất lên khi em đã hoàn toàn kiệt sức.\nTôi cũng kiệt sức rồi, nhưng vẫn muốn đáp lại em——Ư!!!?

**Sweep phân loại sai already-rendered (2 dòng — VN đã có Ư ở chỗ khác trong dòng nhưng vẫn sót っ cuối):**

- **1135** [双鉄] — Sweep ghi already-rendered vì dòng đã có Ư đầu dòng, nhưng っ cuối sau ―――― vẫn chưa diễn: thêm Ư cuối.
  JP: 「ぅっ――はっ――くううっ――――っ！」
  TW: 「呃……啊……唔……啊！」
  Cũ: 「Ư――hà――kuuu――――!」
  Mới: 「Ư――hà――kuuu――――Ư!」
- **1155** [凪] — Sweep ghi already-rendered, nhưng cả hai っ sau ~~~ (んんん～～っ và ずううう～～っ) đều chưa diễn: thêm Ư ở cả hai chỗ.
  JP: 「ふっ――んっ！　んんん～～っ！　んむっ！　じゅ！\nれるっ！　じゅぶっ！　じゅぼっ！　ずううう～～っ！」
  TW: 「唔……嗯！嗯……唔！啾！啾！啾！啾！滋！」
  Cũ: 「Phu――ưm! Ưm ưm~~~! Ưm mu! Ju!\nReru! Jubu! Jubo! Zuuuu~~~!」
  Mới: 「Phu――ưm! Ưm ưm~~~Ư! Ưm mu! Ju!\nReru! Jubu! Jubo! Zuuuu~~~Ư!」

**Sweep needs-file-audit đã xử lý (2 dòng):**

- **1223** [凪] — Sweep không đặt được gasp chắc chắn vì VN là âm dài; kiểm tra: VN khớp đúng âm JP (ずじゅ～…), chỉ thiếu っ cuối sau ~~~: thêm 1 Ư, giữ nguyên số lượng u.
  JP: 「ずじゅ～～～～～～～～～～～～～～～～～っ！！！」
  TW: 「啾～～～～～～～～～～～～～～～～～滋！！！」
  Cũ: 「Zujuuuuuuuuuuuuuuuuuuu!!!」
  Mới: 「ZujuuuuuuuuuuuuuuuuuuuƯ!!!」
- **1272** [双鉄] — Sweep không đặt được gasp; kiểm tra: VN khớp đúng JP (không lệch dòng), chỉ thiếu っ cuối sau ――. "đó!" cuối câu không có cơ sở JP (出せるようになる đã diễn bằng "có thể tiết ra") nên bỏ, thay bằng Ư.
  JP: 「お望み、どおりの――お乳を――母乳を――\n凪が――たくさん――出せる、ように、なる――っ！」
  TW: 「如你所願……我來幫你出奶……讓你能流出許多的母乳……啊！」
  Cũ: 「Như em, mong muốn——để Nagi——có thể, tiết ra——\nthật nhiều——sữa mẹ——đó!」
  Mới: 「Như em, mong muốn——để Nagi——có thể, tiết ra——\nthật nhiều——sữa mẹ——Ư!」

**Sweep bỏ sót, audit tự tìm (6 dòng):**

- **1126** [凪] — っ rời giữa câu sau ―― (あつくてっ――っ――びゅ): TW xác nhận có âm ở đó (啊). Thêm Ư sau "nóng, quá——".
  JP: 「やっ――はっ――すごっ――あつ、くてっ――っ――\nびゅ、びゅて――子宮――たたいて――おっぱい、も」
  TW: 「呀……啊……好棒……這麼燙……啊……咻咻的……打在……子宮上……還有胸部也被……」
  Cũ: 「A——ha——tuyệt quá——nóng, quá——\nbắn, bắn đi——đập vào——tử cung đi——cả ngực, nữa」
  Mới: 「A——ha——tuyệt quá——nóng, quá——Ư——\nbắn, bắn đi——đập vào——tử cung đi——cả ngực, nữa」
- **1173** [凪] — っ rời giữa câu sau ―― (どぎゃして――っ――どうして): thêm Ư.
  JP: 「ぁっ――ふあっ――どぎゃ、して――っ――どうして、\nにーさ――あ――凪、さまに――そうして、ほし、かと」
  TW: 「啊……啊……為什麼……為什麼……大哥哥……啊……會想讓本小姐……變成那樣？」
  Cũ: 「A——fua——sao, lại——tại sao,\nanh——a——lại muốn Nagi——trở nên, như vậy, chứ?」
  Mới: 「A——fua——sao, lại——Ư――tại sao,\nanh——a——lại muốn Nagi——trở nên, như vậy, chứ?」
- **1183** [双鉄] — Cả dòng chỉ có ぁ――っ――: TW diễn thành 2 âm (啊……嗯……), VN cũ chỉ còn 1 âm "A――". Thêm Ư.
  JP: 「ぁ――っ――」
  TW: 「啊……嗯……」
  Cũ: 「A――」
  Mới: 「A――Ư――」
- **1210** [凪] — っ đầu dòng sau ~~~ (～～～っ！！！): TW diễn thành 啊. Thêm Ư sau ~~~.
  JP: 「～～～っ！！！　んっ！　（すんっ）――ちゅむっ！\nれろおっ！　ずじゅっ！　じゅぶっ！　れりゅううっ！」
  TW: 「啊！！！嗯！（吸）……啾！啾！啾！啾！啾！」
  Cũ: 「~~~!!! Ưm! （Hít）――chụt!\nReroo! Zuju! Jubu! Reryuuu!」
  Mới: 「~~~Ư!!! Ưm! （Hít）――chụt!\nReroo! Zuju! Jubu! Reryuuu!」
- **1213** [凪] — っ đầu dòng cả cụm (っ！！！！…): sweep chỉ bắt dạng cả-dòng-nên sót dòng này vì sau đó còn nội dung khác. Thêm Ư đầu dòng.
  JP: 「っ！！！！　（はぷっ！！！！）――れるっ！\nじゅううううっ！　ずちゅっ！　じゅぶっ！！！！」
  TW: 「啊！！！！（含！！！！）啾!啾！啾！啾！！！！」
  Cũ: 「!!!! （Hapu!!!!）――reru!\nJuuuuuu! Zuchu! Jubu!!!!」
  Mới: 「Ư!!!! （Hapu!!!!）――reru!\nJuuuuuu! Zuchu! Jubu!!!!」
- **1231** [凪] — っ rời giữa câu sau ―― (けど――っ――ぁ！): thêm Ư.
  JP: 「ん……あっ――きもち、よか――けど――っ――ぁ！\nおっぱい――あんまり、大きく、なると、邪魔、やけん」
  TW: 「嗯……啊……好舒服……可是……啊！胸部太大……會很……礙事」
  Cũ: 「Ưm……á――sướng, quá――nhưng mà――a!\nVú――nếu to, quá, sẽ vướng víu, lắm」
  Mới: 「Ưm……á――sướng, quá――nhưng mà――Ư――a!\nVú――nếu to, quá, sẽ vướng víu, lắm」

### SFX — mất phụ âm (1 dòng)

- **1170** [凪] — かっ đầu dòng bị dịch thành "A", mất phụ âm k. Các SFX khác trong file đều giữ k (きゃ→Kya 1130, くひゅん→Khu hyun 1242, くあっ→Kua 1191, くふっ→Kufu 1156). Sửa "A"→"Ka".
  JP: 「かっ――はっっ――――あっ！　んっ！！！！」
  TW: 「啊……啊……啊！嗯！！！」
  Cũ: 「A——ha——a! Ưm!!!!」
  Mới: 「Ka——ha——a! Ưm!!!!」

### Đại từ (1 dòng)

- **1567** [monologue] — Độc thoại Soutetsu dùng "anh" — dòng độc thoại duy nhất trong 134 dòng độc thoại của file dùng "anh" (đã kiểm chứng cơ học); quy ước độc thoại là "tôi" (ngoại lệ "mình" chỉ cho độc thoại nội tâm cảm xúc, vd 1840). Người nghe trong cảnh là Nagi nhưng đây là lời dẫn nội tâm, không phải thoại. Sửa "anh"→"tôi".
  JP: 接近前に声をかけ、修行の手をとめてもらって近づけば、\n間違いなく、こんな事態を招かず済んだ。
  TW: 如果我在靠近前跟她搭話，讓她停下來再靠近，肯定不會發生這樣的事情。
  Cũ: Nếu anh lên tiếng trước khi đến gần, bảo em dừng tay lại rồi mới bước tới,\nthì chắc chắn đã không xảy ra chuyện này.
  Mới: Nếu tôi lên tiếng trước khi đến gần, bảo em dừng tay lại rồi mới bước tới,\nthì chắc chắn đã không xảy ra chuyện này.

## Các dòng đã kiểm tra kỹ và giữ nguyên (không sửa)

- **1130, 1131, 1224, 1225, 1161, 1192**: っ gắn liền cuối từ/cuối tiếng rên dài = nhấn mạnh cắt ngang, không phải gasp rời — giữ nguyên.
- **1134, 1280, 1358, 1648**: っ trong ――っと / よ～っんっ (tiếng ưm đã diễn) / 声っ / ぎちっ・っと — giữ nguyên.
- **1237**: lời nói ngọng giải mã đúng ("tinh dịch của anh hai, uống hết") — giữ nguyên; đây chính là bằng chứng song song để sửa 1121.
- **1337**: 「痛――――――つっっっ」 → "Đau――――――quá" — tiếng nhăn mặt vì đau つっっっ được diễn thành mức độ "quá"; giữ nguyên (ghi chú ở "Chờ Hieu").
- **1840**: độc thoại "mình" — ngoại lệ độc thoại nội tâm cảm xúc, giữ nguyên.
- **1256**: 抱かれている → "được Nagi ôm ấp" — theo sát JP (TW dịch mạnh hơn), giữ nguyên.
- **1366**: lời nói ngọng không giải mã chắc được — VN giữ nguyên âm, không bịa nghĩa — giữ nguyên, chờ Hieu (xem dưới).
- **1204, 1206, 1259, 1260, 1263, 1310, 1313**: にーさん dịch "Anh Soutetsu" thay vì "Anh hai" — không sai nghĩa, chỉ không nhất quán (xem "Chờ Hieu").

## Chờ Hieu (không tự quyết)

- **1366 [凪]**: lời nói ngọng 「はーふはん――ほん、へ――ちゅむっ――れるっ――ひほんは、ほほは――ほほへはひ――ぢゅう――ちゅむ」 — không giải mã chắc được (khác 1121/1237 là có song song xác thực trong file); VN hiện giữ nguyên âm ngọng, không bịa nghĩa. Hỏi Hieu có muốn giữ nguyên âm hay thử giải mã theo TW ("đều tại anh hai… khiến em học được bao nhiêu thứ")?
- **にーさん của Nagi**: 7 dòng dịch "Anh Soutetsu" (1204, 1206, 1259, 1260, 1263, 1310, 1313) so với ~20 dòng "Anh hai" — không sai nghĩa, chỉ không nhất quán; đề xuất đưa vào đợt thống nhất (chọn một dạng).
- **1337**: つっっっ (tiếng nhăn mặt vì đau) có nên diễn thành âm ("tsu tsu tsu") thay vì "quá" không? Hiện giữ "Đau――――――quá".

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
1121 = "「Nếu uống tinh dịch của anh hai――ưm――chụt――\\nreru――ưm――afahaha, hyofuhyahhafuhouhe~」"
1124 = "「I——a——~~~~~~~~ƯƯƯƯƯ!!」"
1126 = "「A——ha——tuyệt quá——nóng, quá——Ư——\\nbắn, bắn đi——đập vào——tử cung đi——cả ngực, nữa」"
1135 = "「Ư――hà――kuuu――――Ư!」"
1155 = "「Phu――ưm! Ưm ưm~~~Ư! Ưm mu! Ju!\\nReru! Jubu! Jubo! Zuuuu~~~Ư!」"
1170 = "「Ka——ha——a! Ưm!!!!」"
1173 = "「A——fua——sao, lại——Ư――tại sao,\\nanh——a——lại muốn Nagi——trở nên, như vậy, chứ?」"
1178 = "「Á――Ư!」"
1183 = "「A――Ư――」"
1193 = "「ƯƯ!!!!」"
1208 = "「Ư!!」"
1209 = "「ƯƯƯƯ!!!!」"
1210 = "「~~~Ư!!! Ưm! （Hít）――chụt!\\nReroo! Zuju! Jubu! Reryuuu!」"
1211 = "「Ư!!!!」"
1212 = "「Ư!!!!!」"
1213 = "「Ư!!!! （Hapu!!!!）――reru!\\nJuuuuuu! Zuchu! Jubu!!!!」"
1215 = "「Ư!?」"
1223 = "「ZujuuuuuuuuuuuuuuuuuuuƯ!!!」"
1231 = "「Ưm……á――sướng, quá――nhưng mà――Ư――a!\\nVú――nếu to, quá, sẽ vướng víu, lắm」"
1272 = "「Như em, mong muốn——để Nagi——có thể, tiết ra——\\nthật nhiều——sữa mẹ——Ư!」"
1515 = "Giọng nói nũng nịu cất lên khi em đã hoàn toàn kiệt sức.\\nTôi cũng kiệt sức rồi, nhưng vẫn muốn đáp lại em——Ư!!!?"
1567 = "Nếu tôi lên tiếng trước khi đến gần, bảo em dừng tay lại rồi mới bước tới,\\nthì chắc chắn đã không xảy ra chuyện này."
```

## Kết bài

File lr_凪h1_痛いの痛いの飛んでけばい đã đọc xong toàn bộ 304 dòng: **22 dòng sai (7,2%)**, gồm 19 gasp っ bị mất, 1 lệch dòng (lời nói ngọng 1121), 1 SFX mất phụ âm (1170), 1 đại từ độc thoại (1567). Lượt soát 2: 22/22/0/0. 0 chuỗi xoay vòng, 0 tràn file khác, 0 dòng mồ côi, 0 chưa dịch, 0 trùng key. Còn chờ Hieu: giải mã lời ngọng 1366, thống nhất "Anh hai" vs "Anh Soutetsu" (7 dòng), cách diễn つっっっ ở 1337.
