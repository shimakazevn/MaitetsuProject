# Moan-fix review — ふかみh1_ともはり練習 (moan-fukamih1-tomohari-renshuu)

File H-scene Fukami — buổi hẹn riêng hai người luyện tập chèo thuyền (ともはり練習) trên thuyền xuôi dòng. Chỉ sửa TIẾNG RÊN / thở / gasp / SFX theo quy tắc romaji (Hieu duyệt 21/11 ~01:56). Không sửa đại từ, thuật ngữ, nghĩa, lệch dòng — những thứ đó thuộc audit / đợt thống nhất.

## §1. Kiểm chứng file

- File TOML: `07_Nagi_Fukami/ふかみh1_ともはり練習.txt.toml` — md5 `be7f335b835a741dab4d414880f9aacd`, không có bản trùng (md5 duy nhất trong 227 file TOML).
- CSV3 có **2 bộ** cho file này (544 dòng = 2 × 272): bộ home `translation_toml\07_Nagi_Fukami\` chỉ khớp TOML **1/272** VN — bộ CŨ, KHÔNG dùng. Bộ `translation_toml\11_Other\` khớp TOML **272/272** (sau khi tính TOML-2 flatten `\n` thành khoảng trắng) — dùng bộ này. Đây là file dual-set thứ 11.
- Đọc: **272/272 dòng script** (148 độc thoại, 75 thoại Fukami, 49 thoại Soutetsu), đối chiếu JP + TW từng dòng. Chú thích `# JP:` trong TOML khớp CSV3 (bộ 11_Other) 272/272.
- Audit của file đã merge: 98/272 sai (36,0%) — xem `audit-fukamih1-tomohari-renshuu-REVIEW.md`. Audit làm TRƯỚC quy tắc romaji nên các bản sửa rên của audit chưa theo quy tắc này; xem §5 và §6 về cách xử lý các dòng audit đã sửa.

## §2. Kiểm kê tiếng rên

- **107 dòng rên/SFX** đã xác định và xét từng dòng: 68 thoại rên (Fukami/Soutetsu) + 1 độc thoại có gasp (1403) + 38 dòng SFX (37 dòng `(…)` + 1499 `ぽた――り`).
- Phân loại theo âm:
  - Họ ひゃ/ひあ/ひゅ/ひえ (ひゃっ, ひあっ, ひゅあ, ひえっ, ひゅあん, ひゃああんん): 964, 965, 967, 968, 969, 971, 973, 974, 976, 977, 1055, 1058, 1061, 1077.
  - Họ fa/fu (ふぁ, ふあ, ふぇ, ふや, ぷあ): 987, 989, 992, 993, 1003, 1039, 1043, 1045, 1046, 1048, 1049.
  - Họ く/くぁ/くお (tiếng gằn Soutetsu): 979, 980, 982, 983, 1051.
  - Họ あ/は/ん (rên ngắn, đã đúng kiểu file): 998, 999, 1004, 1005, 1007, 1009, 1011, 1012, 1021, 1022, 1024, 1027, 1029, 1032, 1040, 1042, 1046, 1047, 1052, 1054, 1057.
  - Gasp っ (đã xử lý ở audit/sweep — xem §6): 979, 998, 1043, 1058, 1137, 1403.
  - Cười (giggles = TIẾNG CƯỜI, không phải rên): 1063 `うふふ` → "Ufufu" — đúng, giữ.
  - SFX mút/nuốt/đâm (`ちゅっ`, `じゅっ`, `ごくっ`, `ずっ`, `びゅっ`…): 984, 1035, 1036, 1037, 1641–1684 — đã đúng, giữ (xem §4).
  - Nói ngọng vì ngậm miệng (miệng đầy, phát âm méo): 1077 `ひもひひょふはっへふははひ` → "Hi mo hi hyo fu ha he fu ha ha hi" — đã là romaji, giữ.
- Kết quả: **13 dòng đổi** (12 romaji + 1 đếm nguyên âm), **94 dòng giữ**.

## §3. Các dòng sửa (13 dòng)

Quy tắc áp dụng: rên dài một hơi mà bản VN tách thành nhiều mảnh rời ("Hya ah ưm", "Hi ah", "Hyu a", "Phù ah") thì gộp lại thành MỘT cách diễn (romaji), độ dài nguyên âm theo công thức (số nguyên âm = 1 + số う/ぅ; với あ lặp thì đếm số あ trong JP). Một dòng = một cách diễn (VN hoặc romaji, không trộn).

### 967 — ふかみ — romaji
- JP: 「ひゃああんんっ」
- TW: 「呀嗯」
- Cũ: 「Hya ah ưm」
- Mới: 「Hyaaann」
- Lý do: một hơi rên liền duy nhất (ひゃ+ああ+んん) bị tách thành 3 mảnh trộn romaji + VN ("Hya" + "ah" + "ưm"), đọc rời rạc. Romaji một hơi: ひゃ=1 âm a + ああ=2 → 3 a; んん=2 n → "Hyaaann". Theo đúng mẫu quy tắc (ひゃぁ→"Hyaa").

### 973 — ふかみ — romaji
- JP: 「ひあっ！？　――あっ！　あつい――あついのっ――びゅうって――おなかっ――子宮っ――叩い――んっ！」
- TW: 「呀！？……啊！燙……好燙……呲呲地……感覺……在敲打……子宮……嗯！」
- Cũ: 「Hi ah!? ——Ah! Nóng quá——nóng quá——\nPhụt phụt——trong bụng——tử cung——bị gõ——ưm!」
- Mới: 「Hia!? ——Ah! Nóng quá——nóng quá——\nPhụt phụt——trong bụng——tử cung——bị gõ——ưm!」
- Lý do: ひあっ là một âm duy nhất, bản cũ tách thành "Hi ah" (2 mảnh). Gộp thành romaji "Hia". Phần còn lại giữ nguyên (あっ→"Ah", んっ→"ưm" đã đúng).

### 974 — ふかみ — romaji
- JP: 「ひゅあ！？――ンッ――むっ――んっ――ちゅううっ！　ちゅるっ――ぢゅむっ！　じゅぷっ！　ぢゅろっ！！」
- TW: 「呀！？……嗯……唔……嗯……啾！啾……啾！　噗！　啾！！」
- Cũ: 「Hyu a!?——Ưm——ưm——ưm——chụt ưm!\nChụt rột——rột! Nhóp nhép! Nhóp nhép!!」
- Mới: 「Hyua!?——Ưm——ưm——ưm——chụt ưm!\nChụt rột——rột! Nhóp nhép! Nhóp nhép!!」
- Lý do: ひゅあ là một âm duy nhất, bản cũ tách thành "Hyu a". Gộp thành romaji "Hyua". Phần còn lại giữ nguyên.

### 976 — ふかみ — romaji (2 chỗ trong 1 dòng)
- JP: 「ひえっ！？　えっ！？　ふわっ――あっ！　わた――わた――わたしっ――そんなっ！！」
- TW: 「呀！？哎！？哇……啊！我……我……我……怎麼會！！」
- Cũ: 「Hi e!? Ơ!? Phù ah——a!\nE——e——em——sao có thể!!」
- Mới: 「Hie!? Ơ!? Fuwa——a!\nE——e——em——sao có thể!!」
- Lý do: ひえっ→"Hie" (một âm, bản cũ tách "Hi e"); ふわっ→"Fuwa" (một âm, bản cũ tách "Phù ah" — ふわ bị tách thành "Phù"+"ah" nghe rất gượng). Giữ "——a!" cho あっ như bản cũ (không đổi thêm).

### 977 — ふかみ — romaji
- JP: 「ひゅあんっ！？　あっ――そこ――いま――そこっ――ぐりって――くりゅん、って！」
- TW: 「呀！？啊……那裡……現在……那裡……轉了……轉了！」
- Cũ: 「Hyu ah!? Ah——chỗ đó——vừa rồi——chỗ đó——\nCọ xát——cọ xát, rồi!」
- Mới: 「Hyuan!? Ah——chỗ đó——vừa rồi——chỗ đó——\nCọ xát——cọ xát, rồi!」
- Lý do: ひゅあんっ là một âm duy nhất, bản cũ tách thành "Hyu ah". Gộp thành romaji "Hyuan".

### 982 — 双鉄H — romaji
- JP: 「くおっ！」
- TW: 「呃啊！」
- Cũ: 「Kh oa!」
- Mới: 「Kuo!」
- Lý do: くおっ là MỘT tiếng gằn duy nhất ("kuo"), bản cũ tách thành "Kh"+"oa" (2 mảnh rời). Lưu ý: "Kh" ở đây diễn く (không phải っ), nên quy tắc "Kh giữ" cho っ không áp dụng. Romaji "Kuo!" diễn đúng một tiếng gằn.

### 983 — 双鉄H — romaji
- JP: 「くぁっ！」
- TW: 「呃！」
- Cũ: 「Kh ah!」
- Mới: 「Kwa!」
- Lý do: như 982 — くぁっ là một tiếng gằn duy nhất ("kwa"), bản cũ tách thành "Kh"+"ah". Romaji "Kwa!".

### 989 — ふかみ — romaji
- JP: 「ふあっ！」
- TW: 「哇！」
- Cũ: 「Phù ah!」
- Mới: 「Fua!」
- Lý do: ふあっ bị tách thành "Phù ah" (không phải dạng khóa "phùa", cũng không phải romaji) — nghe gượng. Họ fa/fu là đối tượng nêu đích danh trong quy tắc romaji. Dùng romaji "Fua!". Lưu ý: dòng này audit đã ghi chú đưa vào đợt thống nhất với dạng "phùa" (xem §6) — bản moan này thay thế ghi chú đó bằng romaji.

### 1027 — ふかみ — romaji (2 chỗ trong 1 dòng)
- JP: 「はぁんっ！　そこっ！　そこおおっ！　赤ちゃんの、部屋っ――子宮！　子宮でっ！！！」
- TW: 「啊！那裡！就在那裡！在嬰兒的房間……子宮！在子宮！！！」
- Cũ: 「Haa ah! Chỗ đó! Chỗ đó o o o!\nCăn phòng, của em bé——Tử cung! Ở tử cung!!!」
- Mới: 「Haan! Chỗ đó! Chỗ đóoo!\nCăn phòng, của em bé——Tử cung! Ở tử cung!!!」
- Lý do: はぁんっ là một hơi rên (は+ぁ+ん), bản cũ tách "Haa ah" → gộp romaji "Haan" (2 a + 1 n, theo công thức). そこおおっ: âm おお kéo dài của そこ, bản cũ tách thành 3 chữ "o o o" rời rạc → gộp vào chính từ: "Chỗ đóoo!" (đó + 2 o).

### 1048 — ふかみ — romaji (2 chỗ trong 1 dòng)
- JP: 「ん……あっ――ふあぁ……ぷあっ」
- TW: 「嗯……啊……哇……呼」
- Cũ: 「Ưm……ha——phù ah……phù ah」
- Mới: 「Ưm……ha——Fuaa……Pua」
- Lý do: ふあぁ→"Fuaa" đúng mẫu ví dụ của quy tắc (ふあぁ→"Fuaa"); ぷあっ→"Pua" (romaji, phân biệt ぷ/ふ). Bản cũ tách cả hai thành "phù ah". Giữ "Ưm……ha——" như cũ. Dòng này audit đã ghi chú đưa vào đợt thống nhất với dạng "phùa" — bản moan này thay thế ghi chú đó bằng romaji.

### 1049 — ふかみ — romaji
- JP: 「ん……あっ――なか……が――おされ――て――ふあっ――ひっ――めく、れる……みたい――でっ」
- TW: 「嗯……啊……裡面……被……推著……哇……呀……像是……在轉……」
- Cũ: 「Ưm……ah——bên trong……bị đẩy——vào——\nPhù ah——hi——như bị, lộn ngược……vậy——」
- Mới: 「Ưm……ah——bên trong……bị đẩy——vào——\nFua——hi——như bị, lộn ngược……vậy——」
- Lý do: ふあっ bị tách thành "Phù ah" → romaji "Fua". Giữ "hi" cho ひっ. Dòng này audit đã ghi chú đưa vào đợt thống nhất với dạng "phùa" — bản moan này thay thế ghi chú đó bằng romaji.

### 1057 — ふかみ — đếm nguyên âm
- JP: 「んきゅぅっ！！」
- TW: 「嗯！！」
- Cũ: 「Ưm kyuuu!!」
- Mới: 「Ưm kyuu!!」
- Lý do: công thức độ dài nguyên âm: số nguyên âm = 1 + số う/ぅ trong JP. きゅぅ có 1 ぅ → 2 u ("kyuu"), bản cũ viết 3 u ("kyuuu") — thừa 1 u. Chỉ sửa đúng 1 ký tự này.

### 1058 — ふかみ — romaji (dòng đã sửa ở audit, xem chú thích)
- JP: 「っ！！？――あひゅうううううんっ！！！」
- TW: 「嗯！！？……啊嗯！！！」
- Cũ: 「!!?——A hyu u u u u u ưm!!!」
- Mới: 「Ư!!?——Ahyuuuuuun!!!」
- Lý do: một hơi rên dài duy nhất (あ+ひゅ+う×5+ん) bị tách thành 7 mảnh rời ("A hyu u u u u u ưm") — ngượng rõ rệt. Romaji một hơi: あ→"A", ひゅ→"hyu" (1 u) + 5 う → tổng 6 u, んっ→"n" → "Ahyuuuuuun". Ư đầu dòng là fix gasp CỦA AUDIT (っ đầu dòng bị mất hẳn, TW có 嗯) — bản moan này GIỮ NGUYÊN Ư đó, chỉ đổi phần rên sang romaji. Khi áp dụng ở đợt thống nhất, dùng bản moan này thay bản audit cho key 1058 (không áp cả hai).

## §4. Các dòng rên đã giữ (không đổi)

- 964 `ひゃっ――あっ――…――んうっ` → "Hya——ah——…——ưm": các tiếng rên tách nhau bởi `――` và từ có nghĩa, mỗi tiếng một cách diễn — giữ.
- 965 `やっ` → "Ya"; `ですぅっ` → "đâu ạ": っ cuối gắn với từ có nghĩa (です) là nhấn mạnh, không phải gasp — giữ, không thêm Ư.
- 968 `ひゃんっ` → "Hyan!", `んっ` → "Ưm!!": hai tiếng rên riêng, mỗi tiếng một cách diễn — giữ.
- 971 `ひゃっ` → "Hya", `はっ` → "Ha": giữ. 979 `っ――` → "Kh——": xem §6 (xung đột với fix audit).
- 980 `く――あ……` → "Kh——a……": く và あ tách nhau bởi `――` trong JP nên hai mảnh là đúng — giữ (khác 982/983 là một tiếng gằn duy nhất bị tách).
- 984 gulp/SFX (`ごくっ`, `じゅるうるっ`…) → "Ực——ực——ưm bụp——ực——…": giữ.
- 998 `っ！` → "Ư!": gasp đúng quy tắc — giữ. 999 `あ――` → "A——": giữ.
- 1004 `あ……あっ――ああっ――あ――` → "A……ah——ahhh——a——": kiểu "ah" nhất quán cả file cho あっ, đọc tự nhiên — giữ (không đổi "ah"→"aa"; độ dài thể hiện bằng h, đây là lối viết cảm thán đã ổn định).
- 1005, 1007, 1009, 1011, 1012: "Ha……ah", "ưm", "chụt" — giữ.
- 1021 `あむっ` → "A ngoạm!": diễn VN hợp lý cho tiếng ngậm miệng — giữ. 1022 `あ！` → "A!": giữ.
- 1024 `はっ！あっ！…` → "Ha! Ah! Ah! Ah!": giữ. 1029, 1032: giữ.
- 1035, 1036, 1037 (SFX hôn/mút `ちゅっ/じゅっ/れろっ`): "Chụt/Liếm/Nhóp nhép" — giữ.
- 1040 `ん――` → "Ưm——": giữ. 1042 `んきゅっ` → "Ưm kyu", `イっ` → "lên", `んんん～～んっ` → "ưm ưm ưm~~ưm": giữ.
- 1046 `ふ……うっ` → "phù……ư", 1047 `ぷ、あ` → "phù, a": hai phần tách nhau bởi `……`/`、` trong JP nên hai mảnh là đúng — giữ.
- 1051 `んっ――れろっ――くっ――ご、くっ――` → "Ưm——liếm——kh——ự, c——": giữ (SFX nuốt, đã khớp nội dung).
- 1052 `ん……ちゅっ――ちゅうっ――ちゅっ` → "Ưm……chụt——chụt——chụt": giữ. 1054 `んっ！` → "Ưm!": giữ.
- 1055 `んひゅっ` → "Ưm hyu", 1061 `んぎゅっ` → "Ưm gyu": mẫu "Ưm + X" nhất quán cả file cho ん+X (ん và âm sau là 2 mora riêng) — giữ.
- 1063 `うふふ` → "Ufufu": cười, đúng quy tắc — giữ.
- 1077 nói ngọng (miệng đầy): đã là romaji từng âm tiết — giữ.
- 1130 `ん……っと` → "Ưm……", 1136 `んっ` → "ưm!": giữ.
- SFX `(…)` 1641–1684 (`びゅっ`, `ずっ`, `ぐりゅんっ`, `きゅううううっ`→"Co thắt!", `ざっぼーん`→audit fix "Tõm——!!!", `ぐらっ`→audit fix "Tròng trành!"): đã khớp, giữ. 1499 `ぽた――り` → audit fix "Tỏng——tỏng": giữ.

## §5. Cờ — dòng rên LỆCH DÒNG (không sửa ở đây, audit đã sửa nội dung)

Các dòng này VN cũ là dòng khác bị lệch vào; audit đã khôi phục đúng nội dung. Theo nhiệm vụ, moan-fix KHÔNG sửa dòng lệch — chỉ ghi chú để đợt thống nhất soát lại cách diễn rên TRONG BẢN SỬA CỦA AUDIT:

- **987** (audit fix: 「Phù——ah——của em——âm đạo——\nMiệng của——anh Soutetsu——bằng miệng——」): ふぁっ→"Phù" trong bản audit — đề nghị đợt thống nhất xét lại thành romaji "Fa" (một âm ふぁっ, "Phù" sai nguyên âm so với dạng khóa ふぁ→"phà", và cũng không phải romaji).
- **992** (audit fix: 「Phù, ah——lưỡi……ấm……quá……ưm.」): ふぁ→"Phù, ah" (tách mảnh, ngượng) — đề nghị đợt thống nhất xét lại thành "Fua, ah".
- **993** (audit fix: 「Phuê!?」): ふぇ→"Phuê" đúng dạng khóa — không cần xét lại.
- **995** (audit fix: 「Hả!? A! Anh Soutetsu, khoan hẵng qua đây——\nÁ!? Oa a a a a a a a!?」): わあああああっ→"Oa a a a a a a a" (8 âm a rời, trong khi JP chỉ có 6 âm a: わ+5 あ) — đề nghị đợt thống nhất xét lại thành romaji "Waaaaaa!?".
- **1003** (audit fix: 「Ah——phù——cháy, mất——…」): ふっ→"phù" (hơi thở ngắn, ổn) — không cần xét lại.
- **1039** (audit fix: 「Thích……thích……Anh Soutetsu, đối với em——\nĐã thích em rồi, sao……phù, ah.」): ふあ、ぁっ→"phù, ah" (tách mảnh) — đề nghị đợt thống nhất xét lại thành romaji "Fuaa.".
- **1045** (audit fix: 「Ưm——phù. Em ướt sũng hết cả rồi.…」): ん――ぷぁ→"Ưm——phù." — đề nghị đợt thống nhất xét lại ぷぁ thành romaji "Pua" ("Ưm——Pua.").
- Các dòng lệch còn lại đã sửa ở audit (969, 1001, 1014, 1015, 1018, 1019, 1026, 1034, 1651, 1654, 1655, 1675, 1678, 1681…): bản sửa của audit không còn vấn đề rên — không ghi chú thêm.

## §6. Gasp sweep + xung đột Kh (để đợt thống nhất quyết)

- Sweep `sweep-raw-gasp-wrong.json` có 3 mục cho file này — đã kiểm chứng từng mục trực tiếp:
  - **1461** (`女へと脱皮しかけてる――…`, kind already-rendered, fix rỗng): JP không có っ gasp nào — mục đúng là không sửa. Không làm gì.
  - **1403** (`ふかみがイヤイヤと頭を振っ――っ！`, kind needs-file-audit): sweep cho rằng VN lệch dòng — KIỂM CHỨNG SAI: bộ tốt 11_Other khớp TOML 272/272, VN dòng này đúng nội dung JP. Audit đã sửa gasp っ！ bị mất thành "——Ư!" — đúng. Không làm gì thêm.
  - **1426** (`そうしてそれは、とても静かな頷きになる。`, kind needs-file-audit): JP không có っ nào — mục sweep là false positive. Không làm gì.
- **XUNG ĐỘT Kh (cần đợt thống nhất quyết, không sửa ở đây):** audit sửa 2 dòng gasp TRƯỚC khi có quyết định khóa "Kh giữ" (21/11 ~01:55):
  - **979** `っ――`: VN cũ "Kh——" → audit fix "Ư——". Quyết định khóa sau đó: "Kh" cho っ (glottal-stop) GIỮ, không đổi thành Ư. Đề nghị đợt thống nhất HỦY fix audit của 979, giữ "Kh——".
  - **1043** `ん……っっ――んっ――ふっ――んっ`: VN cũ "Ưm……kh——ưm——phù——ưm" → audit fix "Ưm……ƯƯ——ưm——phù——ưm". Cùng xung đột: "kh" cũ diễn っっ đã đủ (âm đã được diễn, cấm diễn đôi). Đề nghị đợt thống nhất HỦY fix audit của 1043, giữ "kh".
  - Các dòng gasp khác audit đã sửa (1058 Ư đầu dòng, 1137 "Ư!!!", 1403 "——Ư!") đều đúng quy tắc gasp — giữ.
- **Ghi chú về audit §7:** audit ghi 7 dòng fa/fu đưa vào đợt thống nhất (987, 989, 992, 1039, 1045, 1048, 1049). Sau quy tắc romaji: 3 dòng (989, 1048, 1049) đã sửa Ở ĐÂY thành romaji — ghi chú thống nhất cho 3 dòng đó được thay thế. 4 dòng fa/fu còn lại (987, 992, 1039, 1045) vẫn chờ đợt thống nhất, kèm ghi chú xét lại romaji ở §5. Ngoài ra 995 (わあああああっ, không thuộc nhóm fa/fu) cũng có ghi chú xét lại romaji ở §5 — tổng cộng 5 ghi chú xét lại trong bản sửa audit.

## §7. Lượt soát 2 + khối TOML

- Lượt soát 2 (đọc lại toàn bộ 13 bản sửa đối chiếu JP + TW): **tổng 13 / tái kiểm chứng 13 / bỏ 0 / sửa 0**.
- JSON: `moan-fukamih1-tomohari-renshuu-wrong.json` — 13 mục, khóa dạng string, jp/tw/old_vn khớp CSV3 (bộ 11_Other) tuyệt đối 13/13, không có fix nào trùng old_vn, mọi fix chỉ khác old_vn ở đúng phần rên cần sửa (đã kiểm tra diff từng dòng). Không fix nào chạm dòng gasp Ư của sweep (1.146 dòng không được xem lại).
- Khối TOML dưới đây parse bằng tomllib: **13 khóa, 0 sai lệch giá trị** so với JSON. (Literal `\n` trong fix được viết `\\n` trong khối.)

```toml
[script]
"967" = "「Hyaaann」"
"973" = "「Hia!? ——Ah! Nóng quá——nóng quá——\\nPhụt phụt——trong bụng——tử cung——bị gõ——ưm!」"
"974" = "「Hyua!?——Ưm——ưm——ưm——chụt ưm!\\nChụt rột——rột! Nhóp nhép! Nhóp nhép!!」"
"976" = "「Hie!? Ơ!? Fuwa——a!\\nE——e——em——sao có thể!!」"
"977" = "「Hyuan!? Ah——chỗ đó——vừa rồi——chỗ đó——\\nCọ xát——cọ xát, rồi!」"
"982" = "「Kuo!」"
"983" = "「Kwa!」"
"989" = "「Fua!」"
"1027" = "「Haan! Chỗ đó! Chỗ đóoo!\\nCăn phòng, của em bé——Tử cung! Ở tử cung!!!」"
"1048" = "「Ưm……ha——Fuaa……Pua」"
"1049" = "「Ưm……ah——bên trong……bị đẩy——vào——\\nFua——hi——như bị, lộn ngược……vậy——」"
"1057" = "「Ưm kyuu!!」"
"1058" = "「Ư!!?——Ahyuuuuuun!!!」"
```

**Tổng cộng sau file này: 1 file / 13 dòng sai (moan)** (cơ sở 0 file / 0 dòng + 13 file này)

## Kết bài

File ふかみh1_ともはり練習: đọc 272/272 dòng, xét 107 dòng rên/SFX, đổi 13 dòng (12 romaji + 1 đếm nguyên âm), giữ 94 dòng. Lỗi rên tập trung ở một kiểu hệ thống của bản dịch cũ: tách một âm rên duy nhất thành nhiều mảnh rời ("Hya ah ưm", "Hi ah", "Phù ah") — đã gộp lại thành một cách diễn romaji theo đúng quy tắc. 3 dòng fa/fu (989, 1048, 1049) sửa thành romaji ở đây thay cho ghi chú "phùa" của audit. Còn chờ đợt thống nhất: 5 ghi chú xét lại romaji trong bản sửa audit (987, 992, 995, 1039, 1045) và 2 xung đột Kh (979, 1043 — đề nghị giữ "Kh"/"kh", hủy fix audit). Không có dòng nào cần hỏi Hieu. Sau file này tổng moan là 1 file / 13 dòng.
