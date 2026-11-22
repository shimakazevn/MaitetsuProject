# Moan-fix: 真闇h1_長期熟成 — 真闇h1_長期熟成.txt.toml — 8 dòng

## 1. Kiểm chứng file

- File: `真闇h1_長期熟成.txt.toml` — route 05_Mayami, 298 dòng script (monologue 147, thoại 真闇 76, thoại 双鉄H 75). Cảnh H của Mayami ("ủ lâu năm"): Soutetsu say sóng nhiệt trong bồn tắm, Mayami cho gối đùi + quạt, trò chuyện về tuổi 25+ độc thân rồi quan hệ lần đầu (hôn, paizuri, oral, phá trinh, xuất tinh, hiệp hai), kết bằng chuyện con cái / gia đình mới.
- TOML: md5 `af87cd63e115c1890a4aa1a0a05fec4b`, UTF-8 BOM + CRLF (613 CRLF), 298 khóa script. Không có bản sao trùng.
- CSV3: 1 set duy nhất, 298 dòng, key 41–1841, 0 key trùng, 0 VN trống. VN khớp TOML 298/298 (chỉ khác dạng làm phẳng `\n`→khoảng trắng ở 156 dòng). `[selections]` rỗng. Không có thẻ `%l` nào trong file.
- Audit đã gộp trong ROUTE-AUDIT.md: 50/298 (16,8%) — đại từ 28, gasp 7, rên/nguyên âm 5, SFX 8, nghĩa 1, nhỏ 1.
- Sweep gasp kiểm chứng TRỰC TIẾP trong `sweep-raw-gasp-wrong.json`: 5 mục cho file — 1181, 1218, 1272, 1273 (audit đã áp nguyên) + 1092 already-rendered (không sửa). 0 mục trùng với 8 key sửa ở đây.
- Trùng audit: 0/8 key sửa ở đây trùng với fix audit — không xung đột giá trị (khác đợt lr_稀咲h1 có 7 dòng trùng).

## 2. Kho rên (moan inventory)

- Đọc toàn bộ 298 dòng (CSV3 + TOML).
- Dòng rên/thở/gasp/SFX đã xét: **113 dòng** — 78 dòng thoại (真闇 + 双鉄H) + 35 dòng SFX trong ngoặc （ ） (33 độc thoại + 2 thoại trong ngoặc đơn).
- **Đổi 8 dòng, giữ 105 dòng.**
- Phân loại 8 dòng đổi: họ や 2 (1010, 1011); tách âm đơn 2 (1050 あんっ, 1090 んあっっ); sai loại âm + mất nguyên âm dài 1 (1058); fa/fu dạng romaji 1 (1071); đếm độ dài 1 (1173); SFX romaji 1 (1792).

## 3. Các dòng sửa (per-row)

### 3.1 Key 1010 — 真闇

- JP: 「やっ――これっ――深っ――あっ――奥っ――んっ」
- TW: 「呀――這個――好深――啊――裡面――嗯」
- VN cũ: 「A――cái này――sâu quá――a――bên trong――ưm.」
- VN mới: 「Ya――cái này――sâu quá――a――bên trong――ưm.」
- Lý do: やっ là tiếng kêu giật mình/rên — "A" làm mất hẳn phụ âm y. Tiền lệ 日々姫h2: やんっ→"Yan!"; cờ F6 của audit file này ("やっ 'Ya' vs 'Á'") cũng chuyển cho vòng moan. や không có う/ぅ → 1 nguyên âm: "Ya". Các token còn lại giữ (これっ/深っ/奥っ là từ nội dung + っ, không phải gasp; あっ→"a", んっ→"ưm" đã đúng).

### 3.2 Key 1011 — 真闇

- JP: 「や……あっ――気持ち、いい――の――っ、\nゆっくり――どろって――たまる、みたい、でっ――」
- TW: 「呀……啊――好舒服――慢慢地――軟軟的――有種積攢的感覺――」
- VN cũ: 「A……a――Sướng, quá――\ntừ từ――như đang――tích tụ lại, vậy――」
- VN mới: 「Ya……a――Sướng, quá――\ntừ từ――như đang――tích tụ lại, vậy――」
- Lý do: như 1010 — や……→"Ya……". どろって vẫn giữ nguyên theo quyết định keep của audit (§ nhỏ: mất sắc thái "đặc quánh" nhưng câu vẫn đúng nghĩa) — ghi cờ F4 cho đợt thống nhất/Hieu, không tự thêm nghĩa ở đây.

### 3.3 Key 1050 — 真闇

- JP: 「あんっ！」
- TW: 「啊嗯！」
- VN cũ: 「A ưm!」
- VN mới: 「An!」
- Lý do: あんっ là MỘT âm duy nhất ("an"), bản cũ tách thành hai token "A ưm". Tiền lệ đã chốt ở 3 file: あんっ→"An" (paulette-lr-h1 1073/1074/1075 audit; lr-mayamih1 1471; nagifukamih1 1280 audit). っ cuối diễn bằng dấu "!". Một dòng = một cách diễn (quy tắc romaji fallback §3).

### 3.4 Key 1058 — 真闇

- JP: 「ちゅるるっ――ちゅっ――れりゅっ――んちゅうっ」
- TW: 「啾嚕――啾――舔――嗯啾」
- VN cũ: 「Chụt chụt――chụt――rột――ưm chụt.」
- VN mới: 「Chururu――chụt――rột――ưm chuu.」
- Lý do (2 token): (a) ちゅるるっ là tiếng liếm/lưỡi cuộn, không phải tiếng hôn "chụt" — tiền lệ trong chính file này: 1094 ちゅる→"Churu" (audit). → "Chururu" (ちゅ+る+る, đếm đúng). (b) んちゅうっ mất nguyên âm dài — đây đúng là điểm audit cờ cho vòng moan: ちゅう = chuu (công thức 1 + 1 う = 2 u; tiền lệ 1048 ちゅうっ→"chuu" trong file này). → "ưm chuu" (ん→"ưm" theo quy ước file). ちゅっ→"chụt" giữ (tiếng hôn, đúng); れりゅっ→"rột" giữ (quy ước file cho họ れ, như 1048).

### 3.5 Key 1071 — 真闇

- JP: 「ん……あっ――入って、くるっ――んんっ――\n双、ちゃんの――おちん、ちん――ふあっ」
- TW: 「嗯……啊――進來了――嗯嗯――小雙的――雞雞――嗚啊」
- VN cũ: 「Ưm……a――đang vào, này――ưm ưm――\nchim, của――Sou, chan――phua.」
- VN mới: 「Ưm……a――đang vào, này――ưm ưm――\nchim, của――Sou, chan――fua.」
- Lý do: "phua" không phải dạng romaji Hepburn (ふあ = fu + a = "fua") cũng không phải "phùa" theo quy tắc fa/fu đã khóa. Audit giữ "phua" với lý do "đúng dạng romaji" — lý do này sai: "ph" là cách viết phiên âm Việt, không phải Hepburn. Chuyển sang romaji "fua", viết thường giữa dòng theo tiền lệ 1038 trong file này ("ahi――hyu――ha" viết thường giữa dòng). Các token khác giữ (ん→"Ưm", あっ→"a", んんっ→"ưm ưm").

### 3.6 Key 1090 — 双鉄H

- JP: 「んあっっ！！？」
- TW: 「嗯啊！！？」
- VN cũ: 「Ưm a!!?」
- VN mới: 「Na!!?」
- Lý do: んあっ là MỘT âm ("na"), bản cũ tách thành hai token "Ưm a". Tiền lệ h7 843: んぁ→"Na" (đã ghi trong ROUTE-MOANS.md cờ F8: "phạm vi họ や + んあっ→'Na'"). っっ kép diễn bằng "!!?" (nhấn mạnh, không thêm nguyên âm — っ không phải nguyên âm dài). Một dòng = một cách diễn.

### 3.7 Key 1173 — 真闇

- JP: 「ほんなら。\nもおっと気持ちよぉなるために――ねぇ？」
- TW: 「既然這樣，為了大家都能更加舒服――這樣才對吧？」
- VN cũ: 「Vậy thì.\nĐể sướng hơn nữaaaa――nè?」
- VN mới: 「Vậy thì.\nĐể sướng hơn nữaa――nè?」
- Lý do: audit cờ đúng điểm này — "nữaaaa" kéo 4 a cho 1 nguyên âm dài. もおっと = も + お (2 mora, 1 nguyên âm dài thêm) → "nữa" + 1 a = "nữaa" (2 a). Độ dài của よぉ gộp chung vào "nữa" kéo dài (cả câu là một nhịp kéo dài, không tách riêng "sướng" — không có tiền lệ kéo phụ âm/vần cho よぉ ở đây).

### 3.8 Key 1792 — monologue (SFX)

- JP: （みちいいいいいいいいいっっ！！）
- TW: （吱嚕！！）
- VN cũ: （Phậpppppp!!）
- VN mới: （Michiiiiiiiiii!!）
- Lý do: みち là tiếng CĂNG/GIÃN (âm thanh âm đạo căng ra khi đút sâu — ngữ cảnh 1462 "ép sát hông trong một nhịp"), không phải tiếng đâm "Phập". TW 吱嚕 (tiếng rít/căng) ủng hộ. Chuyển sang romaji "Michi" + đúng số い: đếm bằng máy JP có 9 い sau みち (audit ghi "11 い" là SAI — kiểm chứng lại: みち + い×9); VN cũ 6 p (audit ghi "7 p" cũng SAI). "Michiiiiiiiiii" = "Michi" + 9 i (tổng 10 i sau "Mich"). Tiền lệ SFX romaji dài: hachiroku-h1 2179 じゅるるうるるる→"Jururuurururu". っっ→"!!" giữ.

## 4. Các dòng rên đã xét, giữ nguyên (ghi chú đáng kể)

- Đã đúng romaji: 1013 "Hya!!?" (ひゃっ), 1015 "Kya!?" (きゃっ), 1027 "Hia" (ひあっ), 1038 "ahi――hyu" (あひっ――ひゅっ), 1064 "Kya!?" (きゃっ, audit), 1086 "Nhyu!?" (んひゅっ, audit), 1112 "Pua" (ぷあっ), 1063 "Aphuun" (あふぅんっ — 2 u đúng công thức 1 + 1 ぅ).
- Audit đã sửa đúng, giữ: 1014 "Hya!?" (ひゃっ — CỜ Hieu "Hya vs Á" vẫn mở, xem §5 F1); 1021 "Phuya" (ふや); 1025 "Hii…ưm ưư" (ひ――/んううっ — 3 ư đúng công thức); 1048 "chuu" (ちゅうっ); 1069 "kuchu kuchu kuchu" (くちゅっ×3); 1089 "Nbu/Pue" (んぶっ/ぷえっ); 1091 "Ưm ưư" (んうぅっ — 3 ư); 1094 "Npu/Churu/Chumu"; 1793 "ku" (く); 1796 "Kuchuri" (くちゅりっ); 1815 "Nuchu" (ぬチッ).
- Giữ có lý do (quyết định, không phải bỏ sót):
  - 1080 んふっ→"ưm phư": quy ước file ふっ→"phư" ở 4 dòng (1034, 1040, 1059, 1091) — audit giữ; ふ đã diễn thành "phư" nên っ không "mất hoàn toàn" (cut-off diễn bằng dấu "." cuối câu). Audit cờ cho vòng moan — quyết: GIỮ.
  - 1089 ごくんっ→"ực": mất ん phân biệt với ごくっ — nhưng file dùng "ực" nhất quán cho mọi tiếng nuốt (1064, 1075, 1089); không có dạng "ựng" tự nhiên trong tiếng Việt. Ghi cờ F2 cho đợt thống nhất (tiền lệ reinah3 dùng romaji "gokun").
  - 1801/1803/1822 （びゅ…）→"Phụt!": 4 SFX xuất tinh khác nhau gộp thành "Phụt!" — đây là phong cách SFX Việt hoá của file; tiền lệ file chị em lr-mayamih1: "chỉ 2145 sửa vì 32 t vượt xa mọi tiền lệ", còn lại giữ; paulette-lr-h2 giữ "Phụt" cho びゅ/ぴゅ ở 19 dòng. Quyết: GIỮ, ghi cờ F3 (câu hỏi độ dài như fukamih2 F5 / paulette-h5 F4).
  - 1059/1214 くっ→"Ư" (audit): tiếng grunt đã diễn bằng Ư, không mất âm. Ranh giới grunt-vs-rên họ く vẫn mở (cờ F6 như lr_稀咲h1) — ghi cờ F6.
  - 1075 じゅるんっ→"rột": quy ước file cho tiếng liếm/nuốt ("rột" ở 1048, 1058); giữ.
  - 1031 うっ→"Ư", 1032 う――ぁッ→"Ư――a", 1249 はっ→"ha": っ đã diễn (Ư / gạch dài), giữ.
  - 1092 んんん～～～～～～～～っ→"Ưm ưm ưm~~~~~~~~!": sweep already-rendered, audit giữ; 8 dấu ~ khớp JP (đếm bằng máy).
  - 1073 そうひゃ→"Sou-chan": nói ngọng (garbled speech), KHÔNG phải dòng rên — để cho audit, không sửa ở đây.
  - 1241 よぉ ("sướng, nha?"): độ dài không diễn riêng — ghi cờ F5.
  - 1027 い、いくっ→"r-ra mất": nói lắp đã diễn, giữ.
  - 41/1811/1812/1813 （ぱた/パタパタ/ぽとっ）→"Phạch/Tách": SFX quạt đã đúng, giữ.
  - Các SFX độc thoại diễn bằng động từ Việt (1794 "Trượt", 1797, 1799 "Bịch", 1804/1806/1807, 1816/1817 "Thắt lại", 1824 "Ép chặt", 1826, 1831/1832/1833, 1838/1840/1841): quy ước file, audit giữ — giữ.

## 5. Cờ cho đợt thống nhất / Hieu

- **F1 — 1014 Hya vs Á → Hieu (vẫn mở từ audit):** ひゃっ khi hôn giật mình, audit sửa "Á!?"→"Hya!?"; quy tắc họ-ひゃ (§3b) ủng hộ "Hya", nhưng Hieu chưa chốt cho tiếng GIẬT MÌNH (không phải rên cao trào). Vòng moan KHÔNG đổi lại — chờ Hieu.
- **F2 — 1089 ごくんっ→"ực" (mất ん) → đợt thống nhất:** tiền lệ reinah3 dùng romaji "goku"/"gokun" cho họ ごく; file này dùng "ực" nhất quán. Quyết chung: giữ "ực" toàn dự án hay romaji "gokun" cho ごくんっ?
- **F3 — 1801/1803/1822/1823 độ dài SFX びゅ → đợt thống nhất:** có áp công thức đếm (mora→số t, như lr-mayamih1 2145: 11 mora→11 t) cho びゅうっ/びゅるるっ/びゅるるつ hay giữ "Phụt!" gộp? Cùng câu hỏi mở ở fukamih2 F5, paulette-h5 F4.
- **F4 — 1011 どろって bị mất → Hieu/đợt thống nhất:** audit giữ nguyên (câu đúng nghĩa, chỉ mất sắc thái "đặc quánh/rỉ ra"). Có thêm "rỉ ra" hay giữ?
- **F5 — 1241 よぉ không diễn độ dài → đợt thống nhất:** "sướng, nha?" — có cần kéo dài ("sướnggg"?) hay giữ? Không có tiền lệ.
- **F6 — ranh giới grunt-vs-rên họ く (1059, 1065, 1214: くっ→"Ư") → đợt thống nhất:** tiền lệ h6 §3c くっ→"Ku"; audit file này chọn "Ư". Giữ "Ư" hay đổi "Ku" toàn dự án?

## 6. Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 8 giá trị fix đối chiếu JP (+TW) lần 2, đếm lại độc lập số nguyên âm/i (1792: 9 い bằng máy; 1058: ちゅう = 2 u; 1063 đã đúng 2 u — không thuộc fix nhưng kiểm tra chéo).

- Tổng: **8** / tái kiểm chứng: **8** / bỏ: **0** / sửa: **0**.

## 7. Kiểm chứng cơ học

- JSON 8 mục, khóa STRING; jp/tw/old_vn khớp CSV3 tuyệt đối 8/8 (đọc trực tiếp từ CSV3 khi tạo JSON).
- Khối TOML 8 khóa, parse bằng tomllib OK, 0 sai lệch giá trị so với wrong.json.
- Mỗi fix chỉ khác VN cũ ở đúng token rên cần sửa (1010, 1011, 1050, 1058, 1071, 1090, 1173, 1792); 0 key trùng audit.
- Không dòng "Kh" nào trong file; không dòng Ư gasp nào bị chạm (sweep 1092 already-rendered giữ nguyên; gasp audit 1181/1218/1272/1273 không sửa lại).

## 8. Khối TOML (đã kiểm chứng parse)

```
"1010" = "「Ya――cái này――sâu quá――a――bên trong――ưm.」"
"1011" = "「Ya……a――Sướng, quá――\ntừ từ――như đang――tích tụ lại, vậy――」"
"1050" = "「An!」"
"1058" = "「Chururu――chụt――rột――ưm chuu.」"
"1071" = "「Ưm……a――đang vào, này――ưm ưm――\nchim, của――Sou, chan――fua.」"
"1090" = "「Na!!?」"
"1173" = "「Vậy thì.\nĐể sướng hơn nữaa――nè?」"
"1792" = "（Michiiiiiiiiii!!）"
```

Kết bài
