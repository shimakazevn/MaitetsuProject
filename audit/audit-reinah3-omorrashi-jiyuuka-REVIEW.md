# Audit — れいなh3_おもらし自由化大作戦.txt.toml

- File: `れいなh3_おもらし自由化大作戦.txt.toml` — route 04_Reina, 279 dòng script (84 thoại Reina, 60 thoại Soutetsu, 135 độc thoại).
- Nội dung: tiếp nối h2 — Reina đặc huấn "tự do hoá" việc tè dầm: làm tình trong bồn tắm bao trọn gói mượn của chủ Tororyu-yu, Soutetsu dạy Reina rằng xuất tinh của anh và tè dầm của cô bé là một; Reina học deep throat, tập nhịn/xả, rồi cả hai nhận ra dù tìm ra đáp án vẫn sẽ tiếp tục khao khát nhau; kết bằng cảnh ngâm bồn chung và thỏ khăn tắm.
- **Kết quả: 24/279 dòng sai (8,6%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (279 dòng, 0 khóa trùng, 0 ô VN trống); VN khớp TOML tuyệt đối 279/279 (0 lệch thực chất — 159 dòng chỉ khác ở chỗ TOML-2 làm phẳng dấu \n thành khoảng trắng, đã biết, không phải lỗi). `[selections]` rỗng. Không có thẻ `%l` nào trong JP lẫn VN — không có thẻ sai định dạng, không có thẻ VN tự thêm.
- TOML md5 `6c1b1c26745216faeebd6d942cc2e2f4`; không có bản sao file này (không thuộc 11 nhóm trùng — đã kiểm tra md5 toàn bộ 227 file).
- Soutetsu "anh" với Reina đúng toàn file; "tôi" chỉ xuất hiện ở 1718 (suy nghĩ trong ngoặc đơn, đúng quy tắc độc thoại) và "mình" ở 1751 (ngoại lệ độc thoại nội tâm đã chốt). Độc thoại 57 dòng dùng "tôi", 0 dòng dùng "anh". Reina gọi "anh Soutetsu" 13 dòng; Soutetsu gọi Reina "em" đúng (vd. 994, 1184). Không có sửa đại từ nào trong file này.
- Thuật ngữ: không có Ohitoyo/Teitetsu/Migita/Yunoi/KiHa trong file nên không có gì chờ đợt thống nhất; Tororyu-yu (1112) giữ nguyên tên riêng. Không có dòng nào dùng "cô" cho Reina hay "chị" cho Fukami/Nagi.

## §2. Danh sách sửa (24 dòng)

Phân loại: gasp 4 (1050, 1074, 1080, 1099 — 3 từ sweep + 1 sweep bỏ sót), fa/fu 17 (1014, 1019, 1031, 1047, 1048, 1053, 1068, 1073, 1078, 1083, 1119, 1121, 1195, 1196, 1197, 1198, 1200 — ふあ/ふぁ/ぷあ→"phùa"/"phà", ふぇ→"phuê", ふやぁ→"phuya"), SFX 3 (1054 んくっ→"nku", 1071 chuỗi rên mất âm, 1090 んうっ→"ưm").

### 1014 — Reina — fa/fu
- JP: 「ひあっ――んっ――れいな――れいなもっ――んっ――\nしゅき――だいしゅきっ――そうてつ、さんっ――ふぁ」
- TW: 「呀啊……玲奈……玲奈也是，愛你，最愛你了……雙鐵先生」
- VN cũ: 「Hya——ưm——Reina——Reina cũng——ưm——\nthích——thích nhất——anh Soutetsu——ha」
- Sửa: 「Hya——ưm——Reina——Reina cũng——ưm——\nthích——thích nhất——anh Soutetsu——phà」
- Lý do: JP ふぁ cuối dòng: ふぁ→"phà" theo quy tắc fa/fu đã chốt (tiền lệ h2: ふぁ→"phà"). VN cũ "ha" làm mất phụ âm f.

### 1019 — Reina — fa/fu
- JP: 「ふやああんっ！」
- TW: 「呀啊啊啊！」
- VN cũ: 「Hyaaaaan!」
- Sửa: 「Phuyaaan!」
- Lý do: JP ふやああんっ: ふやぁ→"phuya" theo quy tắc đã chốt (tiền lệ reina-h4 1983: ふやあああんっ→"Phuyaaaan!"); 3 âm a (や+ああ) → "Phuyaaan". VN cũ "Hyaaaaan" là romanisation, mất âm ph.

### 1031 — Reina — fa/fu
- JP: 「ふぁ」
- TW: 「哇」
- VN cũ: 「Fua」
- Sửa: 「Phà」
- Lý do: JP ふぁ: ふぁ→"phà" theo quy tắc fa/fu đã chốt. VN cũ "Fua" là romanisation (quy tắc: không romanisation với nhóm fa/fu).

### 1047 — Reina — fa/fu
- JP: 「ひゅっ――ふあっ――」
- TW: 「啊……啊啊……」
- VN cũ: 「A……a a……」
- Sửa: 「Hyu——phùa——」
- Lý do: JP ひゅっ――ふあっ――: ひゅっ→"Hyu" (romanisation đã giữ toàn dự án, tiền lệ h2 1089), ふあっ→"phùa" theo quy tắc fa/fu. VN cũ "A……a a……" làm mất cả hai âm.

### 1048 — Reina — fa/fu
- JP: 「ふやっ――あっ――れいな――きもちいっ――\nすりすり、され、て――きもち、いい――です、よぉっ」
- TW: 「啊……玲奈……好舒服……蹭來蹭去的……好舒服哦」
- VN cũ: 「Fuya——a——Reina——sướng——\nbị cọ cọ, thế này——sướng, lắm——ạ~」
- Sửa: 「Phuya——a——Reina——sướng——\nbị cọ cọ, thế này——sướng, lắm——ạ~」
- Lý do: JP ふやっ: ふやっ→"Phuya" theo quy tắc đã chốt (tiền lệ h5 1064, reina-h4 2455). VN cũ "Fuya" là romanisation.

### 1050 — Soutetsu — gasp
- JP: 「っ」
- TW: 「啊」
- VN cũ: 「!」
- Sửa: 「Ư」
- Lý do: JP 「っ」 cả dòng là gasp, VN chỉ còn "!": gasp bị mất, sweep bỏ sót (sweep chỉ có 4 mục cho file này, không có 1050). Fix 「Ư」 theo tiền lệ sweep: bare っ → 「Ư」 (lr_ハチロクh2 1414, ニイロク04 1265).

### 1053 — Reina — fa/fu
- JP: 「ふあっ――あっ――あんっ――んっ！\nふ、といっ――ですっ――いつも――いつも、よりぃ」
- TW: 「啊啊、啊嗯、啊啊啊！好粗……比之前……還要粗……」
- VN cũ: 「A a、a ưm、a a a! To……to hơn……\nbình thường……rồi」
- Sửa: 「Phùa、a ưm、a a a! To……to hơn……\nbình thường……rồi」
- Lý do: JP ふあっ: ふあっ→"phùa" theo quy tắc fa/fu. VN cũ "A a" làm mất phụ âm f (ánh xạ: ふあっ→"A a", あっ――あんっ→"a ưm", んっ→"a a a" — chỉ sửa phần ふあっ).

### 1054 — Soutetsu — SFX
- JP: 「ぁっ――あっ――んくっ――うっ」
- TW: 「啊啊啊……」
- VN cũ: 「A——a——ưm——ư」
- Sửa: 「A——a——nku——ư」
- Lý do: JP んくっ: trong cùng file, 1196 dịch んくっ→"Nku"; VN cũ "ưm" làm mất phụ âm k. Fix "nku" (viết thường theo quy ước nối tiếp trong file).

### 1068 — Reina — fa/fu
- JP: 「ふあっ――んっ――そうてつさん――んっ――\nは――しゅきっ――だいしゅき――そおてつさぁんっ」
- TW: 「啊嗯……蛤啊……雙鐵先生……愛你，最愛你了……雙鐵先生」
- VN cũ: 「Ha——ưm——anh Soutetsu——ưm——\nHa——thích——thích nhất——anh Soutetsu~」
- Sửa: 「Phùa——ưm——anh Soutetsu——ưm——\nHa——thích——thích nhất——anh Soutetsu~」
- Lý do: JP ふあっ (đầu dòng): ふあっ→"phùa" theo quy tắc fa/fu. VN cũ "Ha" làm mất f. Chỉ sửa "Ha" đầu; "Ha" thứ hai là は――, giữ nguyên.

### 1071 — Reina — SFX
- JP: 「んきゅっ！　ふっ――やっっ――そこっ――\nれいな――そこで――ぐりゅって、されるの――んっ！」
- TW: 「啊嗯！啊……那裡……玲奈……那裡……被插到了……啊嗯！」
- VN cũ: 「A ưm! A……chỗ đó……Reina……chỗ đó……\nbị đâm vào……a ưm!」
- Sửa: 「Ưm kyu! Phù——ya——chỗ đó……Reina……chỗ đó……\nbị đâm vào……a ưm!」
- Lý do: JP んきゅっ！ ふっ――やっっ――そこっ――: んきゅっ→"Ưm kyu" (như 1073 trong cùng file), ふっ→"Phù" (như 1067/1101), やっっ→"ya". VN cũ "A ưm! A……" làm mất âm kyu và nuốt mất やっっ.

### 1073 — Reina — fa/fu
- JP: 「んきゅっ！　ふあっ――あっ――あっ！！」
- TW: 「啊嗯！蛤啊、啊啊啊啊！！」
- VN cũ: 「Ưm kyu! Ha——a——a!!」
- Sửa: 「Ưm kyu! Phùa——a——a!!」
- Lý do: JP ふあっ→"phùa" theo quy tắc fa/fu. VN cũ "Ha" làm mất f. (んきゅっ→"Ưm kyu" giữ nguyên.)

### 1074 — Soutetsu — gasp
- JP: 「っ！」
- TW: 「啊！」
- VN cũ: 「!」
- Sửa: 「Ư!」
- Lý do: Sweep lost-gasp-whole: áp nguyên fix sweep 「Ư!」, đã kiểm chứng với JP 「っ！」/TW 「啊！」.

### 1078 — Reina — fa/fu
- JP: 「やあっ！　これっ――れいなっ――\nはずかしっ――はずかし――ぃっ――で――ふあっ！」
- TW: 「啊！這個……玲奈……好害羞……羞死了……啊嗯！」
- VN cũ: 「A! Cái này——Reina——\nXấu hổ——xấu hổ——quá——đi——ha!」
- Sửa: 「A! Cái này——Reina——\nXấu hổ——xấu hổ——quá——đi——phùa!」
- Lý do: JP ふあっ！ cuối dòng → "phùa!" theo quy tắc fa/fu. VN cũ "ha!" làm mất f.

### 1080 — Soutetsu — gasp
- JP: 「っ！！！？」
- TW: 「啊！！！？」
- VN cũ: 「!!!?」
- Sửa: 「Ư!!!?」
- Lý do: Sweep lost-gasp-whole: áp nguyên fix sweep 「Ư!!!?」, đã kiểm chứng với JP 「っ！！！？」.

### 1083 — Reina — fa/fu
- JP: 「ふにゃっ――んっ――ちゅ――ちゅうっ――\nちゅ――ちゅむっ――ふぁっ――ん～――ちゅるっ」
- TW: 「啾……啾……嗯……啊嗯……啾嚕」
- VN cũ: 「Funya——ưm——chu——chuu——\nChu——chumu——fua——n~——churu」
- Sửa: 「Funya——ưm——chu——chuu——\nChu——chumu——phà——n~——churu」
- Lý do: JP ふぁっ→"phà" theo quy tắc fa/fu. VN cũ "fua" là romanisation. (ふにゃっ→"Funya" giữ nguyên — romanisation rên, không thuộc nhóm fa/fu.)

### 1090 — Reina — SFX
- JP: 「んっ……ンッ――んむっ――んうっ――\nれるっ――れろっ――ちゅぷっ――ちゅぼっ」
- TW: 「啾嚕、啾啾……啾嚕嚕嚕啾、啾嚕、啾嚕嚕……啾嚕嚕」
- VN cũ: 「Ưm……Ưm——ưm——ư——\nChụt——chụt——chụt——chụt」
- Sửa: 「Ưm……Ưm——ưm——ưm——\nChụt——chụt——chụt——chụt」
- Lý do: JP んうっ: tiền lệ h5 759 — んうっ→"ưm ư" (VN cũ "ưm" mất âm う); ở đây VN cũ chỉ còn "ư" (mất cả ん lẫn う). Fix tối thiểu "ưm" theo dạng nén đã chấp nhận ở h2 1045 (んうっっ→"ưm").

### 1099 — Reina — gasp
- JP: 「ンムッ――むっ――んううううっ～～～～っ！」
- TW: 「嗯……嗚嗚！」
- VN cũ: 「Nmu——mu——uuuuuuu~~~~!」
- Sửa: 「Nmu——mu——uuuuuuu~~~~Ư!」
- Lý do: Sweep lost-gasp-trailing: áp nguyên fix sweep (thêm Ư cuối dòng), đã kiểm chứng với JP. (Số lượng u trong tiếng rên: xem §4.)

### 1119 — Reina — fa/fu
- JP: 「ふぇいっ！」
- TW: 「嘿！」
- VN cũ: 「Fuei!」
- Sửa: 「Phuêi!」
- Lý do: JP ふぇいっ: ふぇ→"phuê" theo quy tắc đã chốt (tiền lệ h2 1183: ふぇっ→"Phuê"); giữ âm い → "Phuêi!". VN cũ "Fuei!" là romanisation.

### 1121 — Reina — fa/fu
- JP: 「――ぷあっ！　あっ――どうですか？　そうてつさぁん。\nおもらし、しちゃいそうになりましたかぁ？」
- TW: 「噗哈！啊……怎麼樣？雙鐵先生。感覺要失禁了嗎？」
- VN cũ: 「——Pua! A——thế nào ạ? Anh Soutetsu~.\nAnh có cảm giác, sắp tè dầm ra chưa ạ~?」
- Sửa: 「——Phùa! A——thế nào ạ? Anh Soutetsu~.\nAnh có cảm giác, sắp tè dầm ra chưa ạ~?」
- Lý do: JP ぷあっ: ぷあっ→"phùa" theo quy tắc đã chốt (tiền lệ h2 1114: ぷあっ→"phùa"). VN cũ "Pua!" là romanisation.

### 1195 — Reina — fa/fu
- JP: 「ふあっ――あちゅ――んっ！　ひゃっ――\nあっ――ああっっ――あっ――」
- TW: 「蛤啊……啊……啊嗯……啊、啊啊……啊啊啊」
- VN cũ: 「Ha——achu——ưm! Hya——\nA——aa——a——」
- Sửa: 「Phùa——achu——ưm! Hya——\nA——aa——a——」
- Lý do: JP ふあっ→"phùa" theo quy tắc fa/fu. VN cũ "Ha" làm mất f.

### 1196 — Reina — fa/fu
- JP: 「ふぁっ――あっ――んっ――んっ――んむっ――\nんくっ――ごくっ――ごくっ――――――ごくんっ」
- TW: 「蛤啊……啊……嗯、嗯啊……咕嘟、咕嘟、咕嘟……」
- VN cũ: 「Fua——a——ưm——ưm——nmu——\nNku——goku——goku——————gokun」
- Sửa: 「Phà——a——ưm——ưm——nmu——\nNku——goku——goku——————gokun」
- Lý do: JP ふぁっ→"phà" theo quy tắc fa/fu. VN cũ "Fua" là romanisation.

### 1197 — Reina — fa/fu
- JP: 「ふぁっ――あっ――おもらし――\nしても――しても――はずかしく、ないっ」
- TW: 「蛤啊……啊……就算失禁……也沒什麼……可害羞的」
- VN cũ: 「Ha——a——tè dầm——\ncó làm thế——có làm thế——cũng không, xấu hổ」
- Sửa: 「Phùa——a——tè dầm——\ncó làm thế——có làm thế——cũng không, xấu hổ」
- Lý do: JP ふあっ→"phùa" theo quy tắc fa/fu. VN cũ "Ha" làm mất f.

### 1198 — Reina — fa/fu
- JP: 「ふあっ――あっ――そうてつ、さぁん」
- TW: 「蛤啊……啊……雙鐵先生」
- VN cũ: 「Ha——a——anh Soutetsu」
- Sửa: 「Phùa——a——anh Soutetsu」
- Lý do: JP ふあっ→"phùa" theo quy tắc fa/fu. VN cũ "Ha" làm mất f.

### 1200 — Reina — fa/fu
- JP: 「ふあっ――あっ――あっ――あっ――」
- TW: 「蛤啊、啊、啊啊……」
- VN cũ: 「Ha——a——a——a——」
- Sửa: 「Phùa——a——a——a——」
- Lý do: JP ふあっ→"phùa" theo quy tắc fa/fu. VN cũ "Ha" làm mất f.

## §3. Sweep っ-gasp kiểm chứng

- Sweep có đúng 4 mục cho file này: 1074, 1080, 1099 (fix) và 1199 (already-rendered). Nhận cả 3 fix, đã kiểm chứng từng giá trị với JP (xem §2); 1199 giữ nguyên không sửa (VN đã diễn đủ âm: はっ→"Ha", ちゅ→"chụt", ちゅうう～っ→"chuuu~").
- Quét máy bổ sung toàn file: phát hiện 1 gasp sweep bỏ sót — 1050 「っ」→"!" (bare っ, không dấu câu; tiền lệ sweep: bare っ → 「Ư」). 1079 「！！！」 JP không có âm, VN "!!!" đúng (TW thêm 啊, không theo).
- Các っ còn lại đều đã được diễn (はっ→"Ha", んっ→"ưm", ふっ→"phù", ごくっ→"goku", ちゅっ→"chụt"…) hoặc là っ nhấn mạnh cuối câu gắn vào từ (991 舌がっ, 1029 のにっ, 1177 漏らすっ, 1179/1183 れいなっ, 1187 大好きだっ — không thêm Ư theo quy tắc sweep) hoặc っ sau ん không diễn thêm (1019 ふやああんっ, 1193 …ううん, 1056 んむうっ — tiền lệ lr-fukamih1 1277: っ sau ん không diễn thêm). Không còn gasp nào sót.

## §4. Các dòng đã kiểm tra kỹ nhưng giữ nguyên (không tính sai)

- Key 775: 「……う、む？」→ "……Ư, m?" — giữ: diễn âm hai nhịp ngập ngừng theo JP (う、む tách dấu phẩy); khác "Ừm" ở 1105/1413 nhưng đó là うむ liền mạch.
- Key 1013/1016/1018/1055: ひゃ/ひあ/ふゅあ→"Hya" — giữ: romanisation tiếng rên đã dùng nhất quán toàn dự án (tiền lệ h2 §4: ひゃあああんっ→"Hyaaaaaan"); điều khoản "không romanisation" trong brief chỉ áp dụng cho nhóm fa/fu (ふぁ/ふあ/ふぇ/ふやぁ). ふゅあ không thuộc nhóm fa/fu đã chốt.
- Key 1040: やぁんっ→"Á~" — giữ (tiền lệ h2 996 giữ "Á" cho ひゃ).
- Key 1042/1064/1095: うぁっ→"Ua", ひゅっ→"hyu", んきゅううっ→"Ưm kyuu" — giữ (romanisation rên nhất quán).
- Key 1043/1045: くっ→"ư"/"Ư!" — giữ: SFX doc cho くっ→"Hự"/"Ư".
- Key 1056/1090: んむうっ/んむっ→"ưm" — giữ: nén nhất quán trong file (tiền lệ h2 1045 んうっっ→"ưm").
- Key 1089/1090/1091: れるっ/れろっ/るっ→"chụt" — giữ: làm phẳng SFX miệng thành "chụt" nhất quán trong file (tiền lệ h2 không sửa dạng này).
- Key 1099: số lượng u trong tiếng rên dài — VN cũ 7 u cho JP んううううっ (4 う; quy tắc độ dài: 1 + 4 = 5). GIỮ NGUYÊN giá trị sweep (7 u): số lượng nguyên âm ở tiếng rên dài trong file này vốn lỏng (1018/1055 cùng VN "Hyaaaaaaaaaaaaaaa" cho JP 11/10 âm a khác nhau); chỉ sửa gasp cuối theo sweep. Ghi vào §6 để Hieu quyết có chuẩn hoá nghiêm số lượng nguyên âm hay không.
- Key 1115: lời nói ngọng do miệng đầy (ほれふぁら、えひふぁ、へひほーれふぅ) — giữ nguyên cả dòng phiên âm; xem §6.
- Key 1133: ふえっ？→"hả?" — giữ: diễn nghĩa câu hỏi ngạc nhiên bằng từ Việt tự nhiên thay vì âm "phuê?"; xem §6.
- Key 1193: ふゆううう…→"Huuuu…n" — giữ: romanisation rên (ふゆ không thuộc nhóm fa/fu); số u = 19 khớp đúng quy tắc độ dài (1 + 18 う).
- Key 1210: "anh bảo là" — giữ: theo TW ("你不是說"), JP dở dang ở chữ "動"; VN hoàn thiện theo TW, không bịa thêm ngoài TW.
- Key 1171: すさまじい→"đáng sợ" — giữ: trong khoảng nghĩa của すさまじい (kinh khủng/choáng ngợp); TW "很厲害" cũng chỉ "lợi hại".
- Key 1740/1741: ぷしゃあああっ/ちょろっつ→"Ào" — giữ: diễn âm nước; 1741 làm phẳng tiếng róc rách thành "Ào" nhưng cùng nhóm âm nước, không sai nghĩa.
- Key 1751: 僕→"mình" — giữ: ngoại lệ độc thoại nội tâm (inner emotional self-questioning) đã chốt; 1718 僕→"tôi" trong ngoặc đơn cũng đúng quy tắc độc thoại chung.
- Key 1079: JP 「！！！」 không có âm — VN "!!!" đúng. Key 991: JP dở dang (舌がっ) — VN dở dang theo, đúng.
- 27 cặp VN trùng trong file với JP khác nhau (kiểm tra qua chỉ mục VN toàn dự án): toàn là câu ngắn/SFX chung ("!", "Ừm.", "Sao vậy?", "(Phụt!)", "(Ào)") — lặp hợp lệ, không phải nhiễm chéo. Trong file: "!" ×2 (1050/1074 — sau sửa thành "Ư"/"Ư!" đã phân biệt), "(Phụt!)" ×2 (1744 ずるっ！/1745 ずっ！ — cùng một âm SFX).

## §5. Khối TOML (đã parse-kiểm chứng: 24 khóa, 0 sai lệch)

```toml
[script]
"1014" = "「Hya——ưm——Reina——Reina cũng——ưm——\\nthích——thích nhất——anh Soutetsu——phà」"
"1019" = "「Phuyaaan!」"
"1031" = "「Phà」"
"1047" = "「Hyu——phùa——」"
"1048" = "「Phuya——a——Reina——sướng——\\nbị cọ cọ, thế này——sướng, lắm——ạ~」"
"1050" = "「Ư」"
"1053" = "「Phùa、a ưm、a a a! To……to hơn……\\nbình thường……rồi」"
"1054" = "「A——a——nku——ư」"
"1068" = "「Phùa——ưm——anh Soutetsu——ưm——\\nHa——thích——thích nhất——anh Soutetsu~」"
"1071" = "「Ưm kyu! Phù——ya——chỗ đó……Reina……chỗ đó……\\nbị đâm vào……a ưm!」"
"1073" = "「Ưm kyu! Phùa——a——a!!」"
"1074" = "「Ư!」"
"1078" = "「A! Cái này——Reina——\\nXấu hổ——xấu hổ——quá——đi——phùa!」"
"1080" = "「Ư!!!?」"
"1083" = "「Funya——ưm——chu——chuu——\\nChu——chumu——phà——n~——churu」"
"1090" = "「Ưm……Ưm——ưm——ưm——\\nChụt——chụt——chụt——chụt」"
"1099" = "「Nmu——mu——uuuuuuu~~~~Ư!」"
"1119" = "「Phuêi!」"
"1121" = "「——Phùa! A——thế nào ạ? Anh Soutetsu~.\\nAnh có cảm giác, sắp tè dầm ra chưa ạ~?」"
"1195" = "「Phùa——achu——ưm! Hya——\\nA——aa——a——」"
"1196" = "「Phà——a——ưm——ưm——nmu——\\nNku——goku——goku——————gokun」"
"1197" = "「Phùa——a——tè dầm——\\ncó làm thế——có làm thế——cũng không, xấu hổ」"
"1198" = "「Phùa——a——anh Soutetsu」"
"1200" = "「Phùa——a——a——a——」"
```

## §6. Lượt soát 2 + Chờ Hieu

- Lượt soát 2: 24/24 fix đọc lại đối chiếu JP — 24 giữ nguyên, 0 bỏ, 0 sửa. (Lượt soát có xét lại 1099: giữ giá trị sweep, chỉ ghi chú số lượng u ở §4.)
- Chờ Hieu (không tự quyết):
  1. Key 1115 — lời nói ngọng do miệng đầy: toàn dòng phiên âm La-tinh ("ho re fua ra, e hi fua, he hi ho re fuu"), trong đó 2 chỗ ふぁ→"fua". Có chuẩn hoá 2 chỗ đó theo quy tắc fa/fu (→"phà") hay giữ nguyên cả dòng phiên âm vì đây là lời nói ngọng cố ý? Hieu quyết.
  2. Key 1133 — ふえっ？→"hả?": giữ cách diễn nghĩa câu hỏi hiện tại, hay sửa thành "phuê?" theo đúng quy tắc fa/fu?
  3. Số lượng nguyên âm ở tiếng rên dài: có chuẩn hoá nghiêm theo quy tắc (VN = 1 + số う/ぅ) hay không? Hiện file này lỏng: 1099 có 7 u cho 4 う; 1018/1055 cùng "Hya" + 15 a cho JP 11/10 âm a.
  4. Mâu thuẫn fa/fu toàn dự án (đã ghi trong MEMORY): ふあ→"phùa" (áp dụng ở file này theo phán quyết của parent ở h2) vs "phù" (lr_ふかみh2) — chờ đợt thống nhất, không tự đổi.

## Kết bài

File れいなh3_おもらし自由化大作戦 đã audit xong toàn bộ 279 dòng: 24 dòng sai (8,6%) — 4 gasp (3 từ sweep + 1 sweep bỏ sót 1050), 17 fa/fu (ふあ/ふぁ/ぷあ→"phùa"/"phà", ふぇ→"phuê", ふやぁ→"phuya"), 3 SFX (1054, 1071, 1090). Không lệch dòng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 24 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 24/24, 0 bỏ, 0 sửa. Chờ Hieu: 1115 (lời ngọng phiên âm), 1133 (ふえっ？→"hả?"), số lượng nguyên âm tiếng rên dài, và mâu thuẫn fa/fu toàn dự án.
