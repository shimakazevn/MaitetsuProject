# Moan-fix REVIEW — 真闇h2_無濾過.txt.toml

File: `05_Mayami/真闇h2_無濾過.txt.toml` — H-scene "rượu không lọc" (Soutetsu + Mayami nếm thử rượu shochu không lọc, quan hệ bằng mông). 316 dòng script, audit sai 17 (7 gasp, 1 đại từ, 1 nghĩa, 4 fa/fu, 3 nguyên âm, 1 romaji).
TOML md5: `6a7e62c050273bbf93e38135c93f7f15` (UTF-8 BOM + CRLF). CSV3: 1 bộ duy nhất, 316/316 khóa, 0 khóa trùng, 0 dòng chưa dịch. VN CSV3 ↔ TOML: 160 chênh lệch đều là `\n` bị TOML-2 làm phẳng thành khoảng trắng (đã biết) — CSV3 là chuẩn cho fix list. Sweep: 7/7 mục đã đối chiếu — tất cả nằm trong audit (gasp Ư), không có mục nào thuộc moan-fix này.

## §1. Kiểm kê tiếng rên

Đã đọc toàn bộ 316 dòng (JP + TW + VN). 249 dòng có dấu hiệu âm thanh (っ, kana nhỏ, nguyên âm dài, SFX trong （）) — đã xét từng dòng. Phân loại:

- Họ ひゃ/ひゅ/ひあ/きゃ đã romaji đúng: 16 dòng (1007, 1013, 1015, 1017, 1018, 1021, 1038, 1040, 1042, 1044, 1046, 1065, 1087, 1088, 1094, 1198).
- fa/fu: 4 dòng audit đã đổi "phua"→"phùa" (1040, 1058, 1088, 1117) — moan-fix này chuyển sang romaji; ふっ "Phư" (1032, 1084) + ふうっ "phuu" (1005) GIỮ (xem §3).
- Họ ちゅ: ~20 dòng, đã chuẩn (chụt/rột/chumu/chururu); 4 dòng sửa đếm nguyên âm / khôi phục っ (1029, 1075, 1078, 1450, 1844).
- SFX trong （） độc thoại: 1817–1893 (~50 dòng); 8 dòng SFX dài → romaji, 2 dòng sửa đếm lặp, 2 dòng sửa đếm t, còn lại giữ.
- Gasp Ư của audit — KHÔNG đụng (7 dòng): 827, 1158, 1208, 1209, 1210, 1211, 1213.
- Còn lại là っ phương ngữ Hakata / từ có nội dung (831, 973, 977, 980, 983, 986, 989, 990, 997, 999, 1036, 1051, 1053, 1060, 1064, 1067, 1069, 1071, 1079, 1082, 1090, 1110–1114, 1137–1140, 1150–1157, 1160–1191, 1194, 1202–1207, 1321–1892 độc thoại tường thuật, …) — không phải dòng rên, không sửa.

**Tổng fix: 28 dòng** — romaji 20, đếm nguyên âm 6, đếm lặp 2.

## §2. Chi tiết từng fix (JP / TW / VN cũ / VN mới / lý do)

### Romaji fa/fu (4) — tiền lệ lr_日々姫h2 (tất cả ふあっ→"Fua") + 日々姫h3 (fa/fu→Fu/Fua, ぷあ→Pua)

#### key 1040 — 真闇 — kind: romaji
- JP: 「いひゅっ！？　――んっ――そ、双ちゃん――そ、そこ、\nおしり――お尻の穴っ――あ――ふあっ！？」
- TW: 「咿呀！？　――嗯――小、小雙――那、那裡是屁股――屁眼――啊――嗚啊！？」
- VN cũ (sau audit): 「Ihyu!? ――Ưm――S-Sou-chan――chỗ, chỗ đó,\nmông――lỗ đít mà――a――phùa!?」
- VN mới: 「Ihyu!? ――Ưm――S-Sou-chan――chỗ, chỗ đó,\nmông――lỗ đít mà――a――Fua!?」
- Lý do: ふあっ trong dòng rên → romaji "Fua" (quy tắc 3 + tiền lệ lr_日々姫h2). "phùa" nghe ngượng ở đây. いひゅっ→"Ihyu" đã đúng, giữ.

#### key 1058 — 真闇 — kind: romaji
- JP: 「あ――来た――双ちゃんの、おちんちん――\nんっ――いっぱい――ふあっっ――嬉し――いひっ！？」
- TW: 「啊――來了――小雙的雞雞――嗯――好撐――嗚啊――好高興！？」
- VN cũ (sau audit): 「A――vào rồi――chim của, Sou-chan――\nưm――đầy quá――phùa――vui quá――ihi!?」
- VN mới: 「A――vào rồi――chim của, Sou-chan――\nưm――đầy quá――Fua――vui quá――ihi!?」
- Lý do: như 1040. ふあっっ (2 っ) — っ cuối ngầm trong romaji ngắn, vẫn "Fua".

#### key 1088 — 真闇 — kind: romaji
- JP: 「ふあっ――んひゅゅっ！！？　――やああっ、\n双ちゃんっ――そこ、違っ――んっ――んきゅんっ！」
- TW: 「嗚啊――嗯呀！！？　――呀啊啊、小雙――不是那裡――嗯――嗯呀嗯！」
- VN cũ (sau audit): 「Phùa――nhyuu!!? ――Yaaa,\nSou-chan――chỗ đó, không phải――ưm――nkyun!」
- VN mới: 「Fua――nhyuu!!? ――Yaaa,\nSou-chan――chỗ đó, không phải――ưm――nkyun!」
- Lý do: như 1040. んひゅゅっ→"nhyuu" (2 u) đã đúng.

#### key 1117 — 双鉄H — kind: romaji
- JP: 「ぷあっ――あっ――そんなに、されたら、\n僕、はっ――もうっ」
- TW: 「噗啊――啊――這樣子的話，我――已經要……」
- VN cũ (sau audit): 「Phùa――a――Bị làm thế này,\ntôi, thì――sắp.」
- VN mới: 「Pua――a――Bị làm thế này,\ntôi, thì――sắp.」
- Lý do: ぷあっ → "Pua" (tiền lệ 日々姫h3: ぷあ→Pua).

### くっ → Ku (4) — tiền lệ 凪h1 (くっ trong thoại → "Ku")

#### key 1056 — 双鉄H — kind: romaji
- JP: 「くっ！」
- TW: 「唔！」
- VN cũ: 「Ư!」
- VN mới: 「Ku!」
- Lý do: くっ là tiếng gằn "ku" (nếm rượu mạnh, nghẹn họng) — "Ư" làm mất phụ âm k- (sound-loss). "Ku!" đúng âm JP, tiền lệ 凪h1.

#### key 1085 — 双鉄H — kind: romaji
- JP: 「くっ――真闇――姉っ――」
- TW: 「嗚――真闇――姐――」
- VN cũ: 「Ư――chị――Mayami――」
- VN mới: 「Ku――chị――Mayami――」
- Lý do: như 1056 (gằn khi cố nói).

#### key 1086 — 双鉄H — kind: romaji
- JP: 「くっ――、真闇、姉っ」
- TW: 「嗚――真闇、姐」
- VN cũ: 「Ư――, chị, Mayami.」
- VN mới: 「Ku――, chị, Mayami.」
- Lý do: như 1056.

#### key 1092 — 双鉄H — kind: romaji
- JP: 「ん――くっ」
- TW: 「嗯――唔」
- VN cũ: 「Ưm――ư.」
- VN mới: 「Ưm――ku.」
- Lý do: như 1056 (ku thường, giữa dòng).

### Cười んふふ → Nfufu (3) — tiền lệ Mayami h3 key 2352 (んふふ "Ufufu"→"Nfufu")

#### key 1027 — 真闇 — kind: romaji
- JP: 「んふふ、双ちゃん。気持ちよかとね？」
- TW: 「呵呵，小双。気持ちよかとね？」
- VN cũ: 「Ufufu, Sou-chan. Sướng lắm hả?」
- VN mới: 「Nfufu, Sou-chan. Sướng lắm hả?」
- Lý do: んふふ là MỘT âm — "Ufufu" mất ん đầu. Tiếng cười, không phải rên.

#### key 1029 — 真闇 — kind: romaji
- JP: 「んふふ、双ちゃん。かわゆかねぇ。\nちゅっちゅっちゅって、赤ちゃんみたい」
- TW: 「呵呵，小雙，你真可愛。啾啾啾的，像嬰兒一樣」
- VN cũ: 「Ufufu, Sou-chan. Dễ thương quá đi.\nCứ chu chu chu thế này, hệt như em bé vậy.」
- VN mới: 「Nfufu, Sou-chan. Dễ thương quá đi.\nCứ chụt chụt chụt thế này, hệt như em bé vậy.」
- Lý do: (a) んふふ→"Nfufu" như 1027; (b) ちゅっちゅっちゅっ → "chụt chụt chụt" — "chu chu chu" làm mất っ cả 3 lần (cf. 1077/1083 ちゅっ→"chụt" trong cùng file).

#### key 1031 — 真闇 — kind: romaji
- JP: 「んふふ、双ちゃんと間接キッス」
- TW: 「呵呵，和小雙間接接吻」
- VN cũ: 「Ufufu, hôn gián tiếp với Sou-chan nè.」
- VN mới: 「Nfufu, hôn gián tiếp với Sou-chan nè.」
- Lý do: như 1027.

### あふ → Afu (1) — tiền lệ ハチロクh2 key 966 (あふっ "a phù"→"Afu")

#### key 1010 — 真闇 — kind: romaji
- JP: 「やんっ――んんっ――やあっ――おしり、ばっ――\nあつく――って――んっ――ヘン――これっ――あふっ」
- TW: 「呀嗯――嗯嗯――呀啊――屁股真的――好熱――啊――嗯――要――不對了――啊呼」
- VN cũ: 「Yan――ưm ưm――yaa――mông, thì――\nnóng――lắm――ưm――kỳ lạ――quá――aphu.」
- VN mới: 「Yan――ưm ưm――yaa――mông, thì――\nnóng――lắm――ưm――kỳ lạ――quá――Afu.」
- Lý do: あふっ là một âm duy nhất — "aphu" lai romaji (a) + Việt (phu), vi phạm một dòng = một cách diễn. "Afu" thuần romaji. Các âm khác đã đúng (Yan/yaa/ưm).

### Đếm nguyên âm ちゅう (3) — tiền lệ Mayami h3 key 2330 (ちゅう "chu"→"chuu", 2u)

#### key 1075 — 真闇 — kind: vowel-count
- JP: 「あは……双ちゃん。\nちゅうちゅうするたび、ビクン、ビクンて」
- TW: 「啊哈……小雙。啾啾的時候就在跳個不停呢」
- VN cũ: 「Aha……Sou-chan.\nMỗi lần em chu chu là nó lại giật nảy lên kìa.」
- VN mới: 「Aha……Sou-chan.\nMỗi lần em chuu chuu là nó lại giật nảy lên kìa.」
- Lý do: ちゅう = ちゅ(1u) + う(1u) = 2u; bản cũ "chu" 1u, thiếu 1u.

#### key 1078 — 双鉄H — kind: vowel-count
- JP: 「はぷっ――んっ――ちゅう――」
- TW: 「啊嗚――嗯――啾――」
- VN cũ: 「Hapu――ưm――chu――」
- VN mới: 「Hapu――ưm――chuu――」
- Lý do: như 1075. はぷっ→"Hapu", んっ→"ưm" đã đúng.

#### key 1450 — monologue — kind: vowel-count
- JP: 答えるかわりに、ひたすらに吸う。\nちゅくちゅく、ちゅうちゅう、一心に吸う。
- TW: 我一個勁地吮吸著，這也是我的回答。啾啾、啾啾，專心致志地吮吸。
- VN cũ: Thay cho câu trả lời, tôi chỉ mải miết mút mát.\nChụt chụt, chu chu, mút một cách say sưa.
- VN mới: Thay cho câu trả lời, tôi chỉ mải miết mút mát.\nChụt chụt, chuu chuu, mút một cách say sưa.
- Lý do: như 1075. ちゅくちゅく→"Chụt chụt" đã đúng.

### Đếm nguyên âm trong từ chụt (1) — tiền lệ ハチロクh3 key 1813 (ちゅろぉぉぉっ "Chụụụt" 3ụ → "Chụụụụt" 4ụ)

#### key 1844 — monologue — kind: vowel-count
- JP: （ちゅっうっ――じゅっ――じゅるっ）
- TW: （啾――啾――啾嚕）
- VN cũ: （Chụt――rột――rột）
- VN mới: （Chụụt――rột――rột）
- Lý do: ちゅっうっ = ちゅ(1u) + う(1u) = 2u; "Chụt" chỉ có 1 ụ, thiếu 1. "Chụụt" 2 ụ. じゅっ/じゅるっ→"rột" giữ.

### Kéo dài phụ âm t (2) — giữ kiểu t-stretch, sửa đếm theo công thức nguyên âm (tổng số nguyên âm phát âm = 1 + số う/ぅ; tiền lệ ハチロクh3 key 1063: audit đếm thiếu — 14う→15u, audit nói 13)

#### key 1142 — 真闇 — kind: vowel-count
- JP: 「おひりっ！　れっ――\nイっ――くうううううううぅぅぅぅぅぅんっ！！！」
- TW: 「屁眼！　要――要――高潮了嗯！！！」
- VN cũ (sau audit): 「Bằng mông! A――\nRa――mấttttttttttttt!!!」
- VN mới: 「Bằng mông! A――\nRa――mấtttttttttttttt!!!」
- Lý do: くうううううううぅぅぅぅぅぅ = く(1u) + う×7 + ぅ×6 = 14 nguyên âm u. Audit fix có 13 t (đếm thiếu âm u của く — đúng lỗi lớp h3 1063). Sửa 13t→14t. Kiểu t-stretch giữ nguyên; câu hỏi về kiểu này xem §4 F3.

#### key 1884 — monologue — kind: vowel-count
- JP: （ずろおおおおおおおおっっっ！）
- TW: （蹭！）
- VN cũ: （Trượttttt!）
- VN mới: （Trượttttttttt!）
- Lý do: ずろおおおおおおおお = ろ(1o) + お×8 = 9 nguyên âm o. Bản cũ 5 t. Sửa 5t→9t theo cùng công thức như 1142. Kiểu t-stretch giữ nguyên; xem §4 F3.

### SFX dài → romaji (8) — tiền lệ ハチロクh3 (§ SFX dài → romaji: ずぶう…→"Zubuuuuuuuuuuuuu" 13u, ずるう…→"Zuruuuuu" 6u, きゅう…→"Kyuuuuuuu" 7u)

#### key 1820 — monologue — kind: romaji
- JP: （ずぶうううううううっ！）
- TW: （吱噗！）
- VN cũ: （Phập!）
- VN mới: （Zubuuuuuuuu!）
- Lý do: ずぶ(2u) + う×7 = 9 nguyên âm u. "Phập!" mất toàn bộ độ dài. Romaji "Zubuuuuuuuu" (9 u).

#### key 1823 — monologue — kind: romaji
- JP: （ずるううううううううっ）
- TW: （吱溜）
- VN cũ: （Trượt tuột）
- VN mới: （Zuruuuuuuuuu）
- Lý do: ずる(2u) + う×8 = 10 nguyên âm u. "Trượt tuột" mất toàn bộ độ dài. Romaji "Zuruuuuuuuuu" (10 u). Không có ! trong JP nên fix không có !.

#### key 1832 — monologue — kind: romaji
- JP: （くぱああっ）
- TW: （咕叭）
- VN cũ: （Tách ra）
- VN mới: （Kupaaa）
- Lý do: くぱ(1a) + あ×2 = 3 nguyên âm a. "Tách ra" là cụm động từ, không diễn âm cũng không diễn độ dài; TW 咕叭 diễn bằng âm. Romaji "Kupaaa" (3 a). Dạng ngắn くぱっ→"Tách ra" vẫn giữ ở file khác (tiền lệ h3 1840).

#### key 1834 — monologue — kind: romaji
- JP: （むりゅううううううっ！）
- TW: （哧溜！）
- VN cũ: （Trượt!）
- VN mới: （Muryuuuuuuuu!）
- Lý do: むりゅ(2u) + う×6 = 8 nguyên âm u. "Trượt!" mất toàn bộ độ dài. Romaji "Muryuuuuuuuu" (8 u).

#### key 1837 — monologue — kind: romaji
- JP: （むにいいいっ）
- TW: （啪嗒）
- VN cũ: （Tách）
- VN mới: （Muniiii）
- Lý do: むに(1i) + い×3 = 4 nguyên âm i. "Tách" mất toàn bộ độ dài. Romaji "Muniiii" (4 i).

#### key 1846 — monologue — kind: romaji
- JP: （きゅんっ――きゅううううっ）
- TW: （啾――壓）
- VN cũ: （Thắt lại――siết chặt）
- VN mới: （Thắt lại――Kyuuuuu）
- Lý do: きゅうううう = きゅ(1u) + う×4 = 5 nguyên âm u. "siết chặt" mất toàn bộ độ dài. Romaji "Kyuuuuu" (5 u). きゅんっ→"Thắt lại" (ngắn) giữ.

#### key 1848 — monologue — kind: romaji
- JP: （ふわっ――きゅうううううっ！）
- TW: （嗚哇――壓！）
- VN cũ: （Nhẹ bẫng――siết chặt!）
- VN mới: （Nhẹ bẫng――Kyuuuuuu!）
- Lý do: きゅううううう = きゅ(1u) + う×5 = 6 nguyên âm u. Romaji "Kyuuuuuu" (6 u). ふわっ→"Nhẹ bẫng" (ngắn) giữ.

#### key 1872 — monologue — kind: romaji
- JP: （ずるっ――ぬとおおおおっ）
- TW: （擦――噗）
- VN cũ: （Trượt――tuột）
- VN mới: （Trượt――Nutooooo）
- Lý do: ぬとおおおお = と(1o) + お×4 = 5 nguyên âm o. "tuột" mất toàn bộ độ dài. Romaji "Nutooooo" (5 o). ずるっ→"Trượt" giữ.

### Đếm lặp SFX (2)

#### key 1822 — monologue — kind: count
- JP: （ぎちちちちちちっ！）
- TW: （吱溜！）
- VN cũ: （Siết siết siết siết siết!）
- VN mới: （Siết siết siết siết siết siết!）
- Lý do: ぎちちちちちち = ち×6; bản cũ 5 "Siết", thiếu 1.

#### key 1882 — monologue — kind: count
- JP: （キチチチチチチっ！）
- TW: （緊緊緊！）
- VN cũ: （Siết siết siết siết siết!）
- VN mới: （Siết siết siết siết siết siết!）
- Lý do: キチチチチチチ = チ×6; bản cũ 5 "Siết", thiếu 1.

## §3. Đã đọc và GIỮ NGUYÊN (không fix)

- **Gasp Ư của audit — KHÔNG đụng (7 dòng):** 827 「――っ！？」→"――Ư!?", 1158 「――っ！」→"――Ư!", 1208 「っ！」→"Ư!", 1209 「っ！！！」→"Ư!!!", 1210 「っ！！？」→"Ư!!?", 1211 「っ！？」→"Ư!?", 1213 「～～～～っ！！！」→"～～～～Ư!!!". (Sweep 7/7 mục đã đối chiếu — tất cả là các dòng này.)
- **Audit fix đếm nguyên âm đã đúng (4 dòng, kiểm chứng lại bằng chương trình):** 1017 ふひぃぃぃい→"fuhiiiii" (5 i), 1083 ちゅううっっ→"chuuu" (3 u), 1121 んひいいいいいいっっ→"nhiiiiiii" (7 i), 1198 んひゅううっ→"nhyuuu" (3 u). Audit fix 1018 やっ→"Ya!?" cũng đúng.
- **Họ ひゃ đã romaji đúng (16 dòng):** 1007 ヒャンっ→"Hyan", 1013 ひゃうっ→"Hyau", 1015 ひゃっ→"Hya", 1017 ひゃっっ→"Hya", 1018 んひゅっ→"Nhyu", 1021 ひゃうっ→"Hyau", 1038 いひゃっ→"Ihya", 1040 いひゅっ→"Ihyu", 1042 ひあっ→"Hia" + あひゅっ→"ahyu", 1044 ひあっ→"Hia", 1046 んひっ→"Nhi", 1065 ひあっ→"hia", 1087 くひゅっ→"Kuhyu" + んひゅっ→"nhyu", 1088 んひゅゅっ→"nhyuu", 1094 ひあっ→"hia", 1198 んひゅううっ→"nhyuuu".
- **Họ や đã romaji đúng:** 1005 やっ→"Ya", 1008 やああっ→"Yaaa" (3 a), 1010 やんっ→"Yan" + やあっ→"yaa", 1011 やあんっ→"Yaan", 1020 やっ→"Ya", 1084 やっ→"ya" + ぁっ→"a" + ぁあっ→"aa", 1088 やああっ→"Yaaa", 1198 やらっ→"Yara".
- **ふっ "Phư" GIỮ (1032, 1084) + ふうっ "phuu" GIỮ (1005):** tiền lệ Mayami h3 (giữ "phù"/"phư" cho hơi thở ngắn ふっ/ぷっ, câu hỏi mở F2). Xem §4 F1 — không tự ý đổi sang "Fu" khi hai file đã merge mâu thuẫn nhau (日々姫h3 F2 nói ngược lại).
- **んふっ "Ưm phư" GIỮ (1061, 1105):** tiền lệ Mayami h3 (giữ "Ưm phư" cho んふっ 2348 — hai cử động phát âm).
- **はぁっ "Haa" (1050), くはっ "Kuha" (1034), くふんっ "Kuhun" (1089):** giữ.
- **Họ ちゅ đã chuẩn:** 1077 はむっ→"Hamu" / ちゅっ→"chụt" / ちゅむっ→"chumu" / ちゅるるっ→"chururu"; 1083 ちゅっ→"Chụt" / れるっ→"rột" / ちゅるっ→"rột"; 1103 れるっ→"rột" / ちゅっ→"chụt" / れろっ→"rột"; 1819 ずっ→"Phập" / ずうっ→"phập" / こちゅんっ→"chụt"; 1827 ずばっ→"Phập" / すぱんっ→"Bạch" / ぐちゅっ→"Chụt" / じゅぶっ→"Chụt"; 1829 ずぼっつ→"Phập" / ぼちゅっ→"Chụt" / ずばっ→"Phập" / ずばんっ→"Phập"; 1845 ちゅるっ→"Rột" / ちゅっ→"chụt" / れるっ→"rột" / ちゅむうっ→"chumuu" (3 u, đúng).
- **ああ → "A a" GIỮ (1076, 1836):** tiền lệ ハチロクh3 (（ああ――）→"（A a——）", 2 a đúng).
- **む "Ư" (1055), ん……む？ "Ưm……hửm?" (1099), ん、むっ "Ưm, mu." (1108), んむっ "Ưm mu" (1106):** giữ — tiếng gằn ngắn, diễn Việt tự nhiên.
- **SFX ngắn diễn nghĩa Việt đã đúng:** 1817 （ぴたっ）→"（Dừng lại）", 1819, 1821 （ずぬるるるるるるっ）→"（Trượt tuột!!!）" (lặp âm tiết trượt, không phải kéo dài nguyên âm), 1824 （ずっ）→"（Phập!!!）", 1826 （ちぃ……ぃ――）→"（Kééét……）" (3 i đúng), 1828 （ずぱんっ）→"（Bạch!!!）", 1830 （ずぶっ――ずるっ――ぬぶぶぶぶっ）→"（Phập――trượt――phụt phụt phụt phụt）" (4 ぶ → 4 phụt), 1831 （つぷんっ）→"（Phập!）", 1833 （ごくっ）→"（Ực）", 1835 （つ――ぷっ）→"（Phập）", 1838 （パンッ！　スパッ！　パチュッ！　パンッ！）→"（Bạch! Bạch! Phập! Bạch!）", 1839 （くぽんっ）→"（Phập!）", 1849/1850 （ぐっ）→"（Phập）" (âm đâm, nhất quán trong file), 1852 （ぶびゅるるっ）→"（Phụt phụt!!）", 1856–1860 （びゅ…/ぴゅ…）→"（Phụt）" (SFX xuất tinh, nhất quán — tiền lệ h3), 1861 （ぱくっ）→"（Phập!）" (xem §4 F7), 1862 （ぬりゅっ）→"（Bôi）", 1863 （くりゅんっ）→"（Ấn）", 1867 （ぱくっ）→"（Ngoạm）" (tiền lệ h3 1806), 1868 （するっ）→"（Tuột）", 1869 （しゅこっ）→"（Sục!）", 1870 （くにっ、くにっ――もみゅっ――くりゅっ）→"（Nắn, nắn――xoa――ấn――）", 1871 （もみゅっ）→"（Xoa nắn）", 1873 （ずるっ――るっ――ずっ）→"（Trượt――tuột――phập）", 1874 （ずるぶっ！　ずぶっ！　ぶちゅんっ！　ずりゅっ！）→"（Trượt! Phập! Chụt! Trượt!）", 1875 （さすっ）→"（Vuốt nhẹ）", 1883 （ぴとっ）→"（Chạm nhẹ）".
- **Không đụng dòng "Kh" nào** (file này không có dòng "Kh" cho っ).
- **Độc thoại tường thuật có âm thanh nhưng diễn nghĩa (không phải dòng rên):** 1325 クリュクリュ→"uốn éo", 1433 ちゅうちゅう→"mút mát", 1438 ぷうんと→"phảng phất", 1450 đã sửa ở trên (dòng này trích dẫn SFX trực tiếp nên sửa), 1511 ぎゅっう→"siết chặt", 1540 ぐちょぐちょ→"nhóp nhép", 1607 締め付けっ→"siết chặt", 1621 ぺろり→"liếm nhẹ", 1677 こぷり→"trào ra ồ ạt", 1699 ひっかかって→"bám chặt", 1738 わななき→"run rẩy" — giữ (diễn nghĩa trong lời dẫn, không phải trích âm rên).

## §4. Cờ cho đợt thống nhất (không tự quyết — ghi lại để parent/Hieu xem)

- **F1 — ふっ "Phư"/"Phù" vs "Fu":** file này giữ "Phư" (1032, 1084) theo Mayami h3; 日々姫h3 F2 nói "ふっ→Fu not back to Phù". Hai file đã merge mâu thuẫn nhau — cần quyết một dạng toàn dự án.
- **F2 — くっ trong thoại:** file này dùng "Ku" (1056, 1085, 1086, 1092) theo 凪h1; ハチロクh3 giữ "hự" (1089) và cờ 1815 "Ngoáy" vs "hự"; 凪h1 cờ "Ku (thoại) vs Ư (SFX mô tả)". Cần quyết một dạng toàn dự án.
- **F3 — Kéo dài phụ âm t/c (t-stretch):** 1142 (14t) + 1884 (9t) giữ kiểu t-stretch, chỉ sửa đếm theo công thức nguyên âm. Bản thân kiểu này là câu hỏi mở (lr_日々姫h2 F1 "SFX-length t/c counting formula", 凪h1 cờ "descriptive-SFX consonant stretches") — đợt thống nhất quyết giữ t-stretch hay chuyển sang romaji.
- **F4 — んふふ "Nfufu" vs "Ufufu":** file này + Mayami h3 dùng "Nfufu"; một số file khác còn "Ufufu"; hoa/thường (Nfufu vs nfufu) đã cờ ở lr_日々姫h2 F3. Cần chuẩn hóa toàn dự án.
- **F5 — Ngưỡng SFX dài → romaji:** 1832 くぱああ (3 a) → "Kupaaa" trong khi dạng ngắn くぱっ→"Tách ra" giữ (tiền lệ h3 1840). Đợt thống nhất xác nhận ngưỡng (bao nhiêu nguyên âm kéo dài thì chuyển romaji).
- **F6 — Họ きゅ:** きゅっ/きゅんっ ngắn giữ diễn nghĩa ("Thắt lại" 1842/1846), きゅう… dài → romaji (1846 "Kyuuuuu", 1848 "Kyuuuuuu") — lai trong cùng họ âm; đợt thống nhất xác nhận ngưỡng.
- **F7 — 1861 ぱくっ→"Phập!" GIỮ:** ぱくっ ở đây là tiếng bật/tách sau xuất tinh (TW 噗), khác ngữ cảnh ハチロクh3 ぱくっ→"Ngoạm" (1806). Giữ theo ngữ cảnh; đợt thống nhất xác nhận.
- **F8 — 1005 ふうっ→"phuu" GIỮ:** cùng họ với F1 (ph- vs romaji Fu).

## §5. Khối TOML (28 khóa — áp vào file TOML khi rebuild; `\\n` trong khối = ký tự \n thật trong giá trị)

```toml
1010 = "「Yan――ưm ưm――yaa――mông, thì――\\nnóng――lắm――ưm――kỳ lạ――quá――Afu.」"
1027 = "「Nfufu, Sou-chan. Sướng lắm hả?」"
1029 = "「Nfufu, Sou-chan. Dễ thương quá đi.\\nCứ chụt chụt chụt thế này, hệt như em bé vậy.」"
1031 = "「Nfufu, hôn gián tiếp với Sou-chan nè.」"
1040 = "「Ihyu!? ――Ưm――S-Sou-chan――chỗ, chỗ đó,\\nmông――lỗ đít mà――a――Fua!?」"
1056 = "「Ku!」"
1058 = "「A――vào rồi――chim của, Sou-chan――\\nưm――đầy quá――Fua――vui quá――ihi!?」"
1075 = "「Aha……Sou-chan.\\nMỗi lần em chuu chuu là nó lại giật nảy lên kìa.」"
1078 = "「Hapu――ưm――chuu――」"
1085 = "「Ku――chị――Mayami――」"
1086 = "「Ku――, chị, Mayami.」"
1088 = "「Fua――nhyuu!!? ――Yaaa,\\nSou-chan――chỗ đó, không phải――ưm――nkyun!」"
1092 = "「Ưm――ku.」"
1117 = "「Pua――a――Bị làm thế này,\\ntôi, thì――sắp.」"
1142 = "「Bằng mông! A――\\nRa――mấtttttttttttttt!!!」"
1450 = "Thay cho câu trả lời, tôi chỉ mải miết mút mát.\\nChụt chụt, chuu chuu, mút một cách say sưa."
1820 = "（Zubuuuuuuuu!）"
1822 = "（Siết siết siết siết siết siết!）"
1823 = "（Zuruuuuuuuuu）"
1832 = "（Kupaaa）"
1834 = "（Muryuuuuuuu!）"
1837 = "（Muniiii）"
1844 = "（Chụụt――rột――rột）"
1846 = "（Thắt lại――Kyuuuuu）"
1848 = "（Nhẹ bẫng――Kyuuuuuu!）"
1872 = "（Trượt――Nutooooo）"
1882 = "（Siết siết siết siết siết siết!）"
1884 = "（Trượttttttttt!）"
```

## §6. Lượt soát 2 (second pass — đọc lại toàn bộ 28 fix với JP)

- **Tổng số fix:** 28. **Tái kiểm chứng:** 28/28. **Bỏ:** 0. **Sửa:** 0.
- **Kiểm chứng cơ học (đọc lại từ CSV3 + audit JSON, độc lập với lúc viết fix):** 28/28 mục có key dạng string, jp/tw/old_vn/character khớp CSV3 tuyệt đối, old_vn = VN sau audit (5 dòng: 1040, 1058, 1088, 1117, 1142) hoặc VN CSV3 (23 dòng), fix khác old_vn đúng ở token rên/SFX (kiểm bằng thay thế chuỗi đích danh từng token). Khối TOML 28 khóa parse OK, 0 sai lệch so với JSON. Không đụng dòng gasp Ư nào (827/1158/1208/1209/1210/1211/1213). Không đổi dòng "Kh" nào (file không có).
- **Đếm lại nguyên âm bằng chương trình (token trích trực tiếp từ JP thật trong CSV3, không gõ tay):** 1820 "Zubuuuuuuuu" 9u, 1823 "Zuruuuuuuuuu" 10u, 1834 "Muryuuuuuuuu" 8u, 1837 "Muniiii" 4i, 1846 "Kyuuuuu" 5u, 1848 "Kyuuuuuu" 6u, 1872 "Nutooooo" 5o, 1832 "Kupaaa" 3a, 1075/1078/1450 "chuu" 2u, 1844 "Chụụt" 2ụ, 1142 14t (く1 + 7う + 6ぅ), 1884 9t (ろ1 + 8お), 1822/1882 6 "Siết" (6 ち/チ) — tất cả khớp. Kiểm chứng lại audit fix: 1017 5i, 1083 3u, 1121 7i, 1198 3u — tất cả đúng, giữ nguyên.
- **Lưu ý phương pháp:** lần build đầu gõ sai số t cũ của 1142 (tưởng 14t, thực tế audit fix có 13t) nên thay thế chuỗi thất bại — đã sửa đặc tả (cũ 13t → mới 14t) và build lại; giá trị fix (14t) không đổi. Bài học như ハチロクh3: không kiểm chứng số lượng bằng chuỗi gõ tay.
- **Kiểm tra sweep trực tiếp:** 7/7 mục sweep của file này đã đối chiếu — tất cả nằm trong audit (gasp), không có mục nào thuộc moan-fix này.

Kết bài
