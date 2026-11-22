# Điều tra F1 — Các câu hỏi mở về rên/SFX (§3: M7, M8, M9, M10, M11, M14, M15, M19, M68, M70)

- **Nhiệm vụ:** chỉ điều tra + đề xuất quy tắc. KHÔNG sửa giá trị nào, KHÔNG viết fix JSON.
- **Ngày:** 22/11/2026. Người làm: subagent F1 (điều phối viên quyết định sau, batch khác áp dụng).
- **Nguồn:** CSV3 good set 87.833 dòng (tổng 91.731, đã bỏ 3.898 dòng stale theo `dual-csv-sets.md`); moan fix 1.516 dòng; audit fix 9.239 dòng.
  Quy ước giá trị hiện tại: **moan > audit > CSV3**.
- **Phương pháp:** mọi con số đếm bằng script (chỉ liệt kê/đếm); mọi giá trị đề xuất đọc tay theo JP (+TW).
  Engine chứng cứ (đã rebuild sau khi /tmp bị wipe): `~/workspace/maitetsu-pilot/unification/f1_engine.py`
  — đếm lại khớp: CSV3 91.731 / good-set 87.833; moan 1.516; audit 9.239.
- **Cảnh báo về con số đếm:** các bảng đếm "JP chứa âm X → VN hiện tại chứa Y" là đếm **theo dòng**, không phải theo token.
  Một dòng có nhiều âm rên nên "Ư" trong VN có thể là của một token khác trong cùng dòng (đặc biệt ở M7/M8/M15).
  Vì vậy con số dùng để định hướng, còn quy tắc dựa trên **các quyết định có chủ ý** (transition old→new của moan pass)
  và các tiền lệ đã xác minh tay từng dòng. Chỗ nào số bị nhiễu, báo cáo ghi rõ.

## §0. Các sai sót ghi nhận trong UNIFICATION-LIST.md (phải sửa trong danh sách, không lặng lẽ làm theo)

1. **M7 "凪h2 1195 'hự'" — sai file.** Đó là **lr_ふかみh2 1195** (JP 「子宮口、から――離し、たく、ないっ――くっ――…」,
   TW 「我不想離開子宮口了……唔……」, moan fix → "hự"). 凪h2 không có key 1195 (file chỉ 673 dòng).
2. **M7/M45 "れいなh1 1225" — sai file.** Đó là **lr_れいなh1 1225** (JP 「くっ！！！」, TW 「咕！！！」, hiện tại "Ư!!!" — moan agent đã flag F1, chưa từng đổi).
3. **M8 "lr_ふかみh2 (1181/1187/1203 'Á' từ chối vs 1325 'Yaa' rên)" — sai file.** Đó là **lr_凪h2**:
   1181/1187/1203 giữ "Á" (từ chối, moan chỉ sửa đếm), 1325 やぁ trong chuỗi hơi thở → "yaa" (chữ thường, giữa chuỗi).
   lr_ふかみh2 1181/1187/1203 không chứa や (đã xác minh bằng dump).
4. **M15 "ハチロクh9 2323/2328 'ưm' vs 'ưn'" — sai file.** Đó là **真闇h3 2323/2328** (んっ → "ưn" cả hai; CSV3 ハチロクh9 2323/2328 là dòng đại từ).
5. **M15 "凪ふかみh1 F5 (1061 'ưmm' vs 'nn')" — sai file.** 1061 んんっ → "ưmm" là **れいなh3 1061** (moan fix "ưm"→"ưmm");
   凪ふかみh1 không có key 1061 ở vai trò đó.
6. **M15 "日々姫h1 F2" và "れいなh1 F2" ghi sai:** 日々姫h1 F2 là fa/fu "Phù" (chờ thống nhất), không phải ん+phụ âm;
   bằng chứng ん ở 日々姫h1 là んふ→"Nfu" ×4 và んくう→"Nku…" (key 1003).
   Các key んきゅ→"Nkyu" 836/868 thuộc **ポーレットh6**, không phải ハチロクh6.
7. **M9 "ハチロクh6 F1" đáng ngờ:** ハチロクh6 F1 là くっ "Ku" vs "Hự"; cờ ふっ "phù" vs "Fu" là **ポーレットh6 F7**.
8. **M10 "凪ふかみ01 1547 ふぇぇっ" — sai file con.** Key 1547 có JP 「ふぇぇっ」 thuộc **凪ふかみ01_流れ.txt.toml**
   (TW 「嗚唉」, audit "Phuêê."); còn 凪ふかみ01_凪の成長、ふかみの成長 1547 là câu hỏi 「凪、わかりますか？」.
   (Có 2 file cùng tiền tố "凪ふかみ01".)
9. **M8 "tiền lệ moan-h8 2187 KHÔNG tồn tại" là SAI — nó CÓ tồn tại** (đã xác minh trực tiếp):
   ポーレットh8 key 2187 có trong CSV3 VÀ trong `moan-paulette-h8-alice-rail-car-wrong.json`
   (JP 「えっ！？ やっ――いまのッ――んひゃうっ！？…」, TW 「哎！？呀——」, old VN và moan fix đều giữ やっ → "Á——";
   moan fix chỉ đổi "hyau"→"Hyau"). Nó chỉ vắng trong audit wrong.json — lần xác minh trước chỉ kiểm audit JSON.
   Tiền lệ này DÙNG ĐƯỢC: やっ giật mình/thán từ → "Á".
10. **Sửa một kết luận trong REVIEW ふかみh3 F8:** ふかみh1 967 「ひゃああんんっ」 → "Hyaaann" là **ĐÚNG** (đếm bằng máy:
    JP ひゃ(1a)+あ+あ = 3 a, んん = 2 n; VN "Hyaaann" = 3 a + 2 n). Claim "3n" trong REVIEW là đếm sai.
    (Kiểm chứng thêm: 真闇h3 2278 「んくゅうぅぅぅぅぅぅぅぅぅぅんっ」 → "Nkyuuuuuuuuuuuun": 1u cơ sở + 11う = 12 u ✓, ん đầu = "N" + ん cuối = "n" ✓;
    真闇h3 2310 「ふああああああああんんんっっっっ」 → "Fuaaaaaaaannn": 8 a ✓, 3 n ✓.)
11. **M15 "lr_ハチロクh2 1842" không tồn tại trong file đó** (không phải dòng rên) — trích dẫn không xác minh được, bỏ qua.
12. **M15 "33 dòng んっ→'ưn'" là số bị nhiễu** (đếm chuỗi con, dính cả "Nhưng", "cũng"...). Đếm lại bằng từ độc lập:
    chỉ **8 dòng** có từ "ưn"/"Ưn" đứng riêng trong VN ở các dòng JP có んっ (so với 1.480 dòng "ưm" đứng riêng);
    trong 8 dòng đó 6 dòng là dạng tách "ưn ku"/"Ưn kyu" (xem §M15), chỉ **2 dòng** là ん(っ) trần → "ưn"
    (cả hai đều ở 真闇h3: 2323, 2328 — xem §M15).
13. **File audit-obasan-wrong.json (255 mục) không có fix nào** — chỉ có trường `vn` (là giá trị sai cũ), không có trường `fix`.
    Engine không map được file này (đúng — không có gì để map). Điều phối viên lưu ý: 255 dòng này có danh sách lỗi
    nhưng chưa có fix ghi lại ở đâu.
14. **ROUTE-MOANS.md mục lr_ニイロクh: cờ F1 ghi "ふえっ→'Fue' 991/992" — sai file (lỗi copy).**
    lr_ニイロクh KHÔNG có key 991/992 (key 945–2072 nhưng khuyết 991/992). Đó là cờ F1 của **lr_稀咲h1**
    (xem REVIEW `moan-lr-kisakih1-oshioki-to-gohoubi-REVIEW.md` dòng 79; các key 991/992 đã xác minh thuộc lr_稀咲h1).
    Lưu ý thêm: REVIEW lr_稀咲h1 dòng 15 ghi rõ lý do giữ "Fue!? Yaa!" ở 991 — xem §M8/§M10.

---

## M7. くっ → "Ku" vs "Hự" vs "Ư" vs "Ngoáy"

### Câu hỏi
Có ranh giới sạch thoại-vs-miêu tả không? Cái gì quyết định "Ngoáy"/"Thúc" vs "hự"?

### Tiền lệ đã xác minh (file/key/JP/TW/VN hiện tại)

**Thoại → "Ku" (moan pass đổi có chủ ý):**
- lr_ハチロクh2 1484 — JP 「くっ！！！」 / TW 「咕！！！」 / MOAN "Ku!!!"
- 凪h1 1067 — JP 「くっ――あっ」 / TW 「呃……啊」 / MOAN "Ku——A"
- ハチロクh4 989 — JP 「くっ――あっ――」 / MOAN "Ku——a——" (audit cũ "Hự" → moan đổi thành "Ku")
- ハチロクh4 1003 — JP 「くっ！？」 / MOAN "Ku!?"
- ハチロクh6 882/897/935/939 — JP 「くっ――」 / 「Ưm——Ku!」 / 「Ưm ku!!!!」 / "Ku!" (moan đổi từ "Hự"/"Ư")
- 真闇h2 1056/1085/1086 — JP 「くっ」 / MOAN "Ku"
- ハチロクh5 1020/1070 — JP 「くっ」 / MOAN "Ku"
- ポーレットh6 772 — JP 「くっ――ぁっ――」 / MOAN "Ku——a——"
- lr真闇追加h 1093/1127/1292/1805/1843 — JP 「くっ」 / MOAN "Ku"
- ふかみh3 2349 — JP (chuỗi rên, くっ giữa chuỗi) / MOAN "…ưm, Ku——"

**Thoại → "Hự" (giữ có chủ ý — quy ước từng file):**
- lr_ふかみh2 1195 — JP 「子宮口、から――離し、たく、ないっ――くっ――…」 / TW 「我不想離開子宮口了……唔……」 / MOAN "…hự——"
  (cùng file: 1066 「ん……くっ――」 → "Ưm…… hự——" [CSV3]; 1070 「くっ！！！！」 → "Hự!!!!" [CSV3]; 1273 → "Ưm——hự——" [MOAN])
- 日々姫h1 1041/1043/1044/1062 — 1041 JP 「はっ――あっ――くっ――」 / MOAN "Hơ——A——Hự——";
  1043 JP 「ぁっ――んっ――くっ――はっ――んんっ――」 / CSV3 "A——Ưm——Hự——Hơ——Ưm——";
  1044 JP 「かはっ――んっ――ん、くっ――」 / MOAN "Kaha——Ưm——Ưm, hự——"; 1062 JP 「ンッ――くっ」 / CSV3 "Ưm——hự."
- 凪ふかみh1 1232 — JP 「くっ――あ」 / MOAN "Hự——a" (đơn lẻ trong file)
- lr_ふかみh1 1469 — JP (chuỗi rên) / MOAN "…ưm, hự! A!…" (đơn lẻ trong file)
- lr_凪h1 1190 — JP (chuỗi rên) / MOAN "…ưm——hự——fua!…" (đơn lẻ trong file)
- lrれいな追加h 723/1221 — MOAN "Hự" (2 dòng, quy ước file)
- ハチロクh2 976/1041 — 976 MOAN "…Hự——đến đây——…"; 1041 "Hự——khít quá——" (2 dòng, moan giữ)
- ポーレットh6 851 — JP 「ん……くっ――」 / TW 「嗯……啊——」 / CSV3 "Ưm……hự——" (đơn lẻ; các dòng くっ khác trong file → "Ku", vd 772)
- 日々姫h4 1028 — JP 「んっ――くっ」 / CSV3 "Ưm――hự" (đơn lẻ; chưa rõ quy ước file)

**Thoại → "Ư" (chưa từng được quyết — giá trị CSV3/audit còn sót):**
- lr_れいなh1 1225 — JP 「くっ！！！」 / TW 「咕！！！」 / CSV3 "Ư!!!" (moan flag F1, chưa đổi)
- 真闇h1 1059/1065/1214 — JP 「くっ」 / "Ư" (audit giữ; F6 mở)
- Các dòng くっ trong file phi-H: "Ư" là dạng mặc định của CSV3 (tiếng gầm gừ trong thoại thường, không phải rên H).

**Miêu tả （ ） → "Ư" (âm mất hẳn nếu không có):**
- 凪h1 1766 （くっ） → "（Ư）"; 1770 （くっ――くちゅっ――…） → "（Ư——Nhóp nhép——…）";
  1780 （くっ――ぷっ） → "（Ư——Phụt）" — cả 3 đều CSV3, chưa từng bị moan pass đụng.
- lr_日々姫ふかみh1 2451 （ずっ――くっ） → "（Phập――Ư）" (CSV3).

**Miêu tả （ ） → "Ngoáy" (động từ):**
- ハチロクh3 1815 （くっ――くくっ――） → "（Ngoáy——ngoáy ngoáy——）" (CSV3, chưa từng đụng) —
  đối lập cùng file 1089 thoại くっ → "hự" (audit, moan giữ). Đây là dòng duy nhất miêu tả-くっ→"Ngoáy".

**Hòa vào cụm động từ (không render riêng âm くっ):**
- ポーレットh3 894 — JP (chuỗi rên) / MOAN "Yaa——bị ngoáy sâu——vào rồi——…" ("Ngoáy" là động từ của cả câu)
- れいなh2 1047 — MOAN "…bị ngoáy, ngoáy——Hyau!"
- lr_ハチロクh1 1423 / 日々姫h5 1321, 1177 — "Thúc (mạnh) vào…" (くっ hòa vào cụm "thúc")

**"kư" (quy ước file):** lr_稀咲h1 972/1190/1260 → "kư" (nhất quán trong file; đối lập lr_ニイロクh giữ "ku").

### Đếm toàn dự án
- Dòng JP chứa くっ: **1.243**.
- **Transition old→new của moan pass (chỉ tính các dòng moan fix có くっ trong JP — đây là bằng chứng quyết định):**

  | old → new | số dòng | ý nghĩa |
  |---|---|---|
  | Ư → Ư (giữ) | 50 | agent sửa token khác, để nguyên くっ→"Ư" — KHÔNG phải tán thành "Ư" |
  | Ư → Ku (đổi) | 33 | quyết định có chủ ý → "Ku" |
  | Hự → Ku (đổi) | 18 | quyết định có chủ ý → "Ku" (lật "Hự") |
  | Hự → Hự (giữ) | 8 | giữ quy ước file |
  | Ư → Hự (đổi) | 6 | quyết định có chủ ý → "Hự" (các file quy ước "Hự") |
  | Ku → Ku (giữ) | 5 | giữ "Ku" |
  | Ngoáy → Ngoáy (giữ) | 2 | giữ cụm động từ |
  | Ư → other / other → other | 7 / 20 | đổi sang Nku/… hoặc giữ dạng khác |

  **Khi moan agent thực sự quyết về くっ: → "Ku" 51 dòng vs → "Hự" 6 dòng.**
  Lý do ghi trong moan snippet lr真闇追加h (họ く): "h6 §3c: くっ/んくっ trong chuỗi rên → Ku/Ưm ku; 'Hự' mất phụ âm k".
- Đếm thô theo dòng (bị nhiễu vì 1 dòng nhiều âm — chỉ tham khảo):
  thoại H-file: "Ư" 280 / "Hự" 96 / "Ku" 46 / "Ngoáy" 6 / "Thúc" 3 / "kư" 2 / khác 132;
  miêu tả （ ） H-file: "Hự" 24 (phần lớn là hự của ぐっ/むっ cùng dòng, không phải của くっ) / "Ư" 17 / "Ngoáy" 8 / "Ku" 7 / khác 71.

### QUY TẮC ĐỀ XUẤT — M7 (độ tin cậy: cao cho thoại, trung bình-cao cho miêu tả)
1. **Thoại H-scene, くっ là token âm độc lập → "Ku".**
   (51 quyết định có chủ ý của moan pass vs 6; lý do h6 §3c: "Hự" làm mất phụ âm k.)
2. **Ngoại lệ "Hự" — chỉ các file có quy ước "Hự" nhất quán (≥2 dòng, moan đã giữ):**
   lr_ふかみh2 (4 dòng: 1066/1070/1195/1273), 日々姫h1 (4: 1041/1043/1044/1062),
   lrれいな追加h (2: 723/1221), ハチロクh2 (2: 976/1041). Giữ nguyên các file này.
3. **Các dòng "Hự" đơn lẻ (1 dòng trong file, trái với dạng chủ đạo của file) → đổi thành "Ku":**
   凪ふかみh1 1232, lr_ふかみh1 1469, lr_凪h1 1190, ポーレットh6 851, 日々姫h4 1028 (5 dòng).
   (Lý do: chúng là giá trị CSV3/audit đơn lẻ, không phải quy ước file.)
4. **Miêu tả （ ） くっ → "Ư"** (4 tiền lệ: 凪h1 1766/1770/1780, lr_日々姫ふかみh1 2451).
   Không có ranh giới thoại-vs-miêu tả "sạch" theo nghĩa một quy tắc cho cả hai — mà là **hai quy tắc theo vị trí**:
   thoại → "Ku" (giữ phụ âm), miêu tả → "Ư" (âm sẽ mất hẳn nếu không render).
5. **Giữ nguyên:** "kư" ở lr_稀咲h1 (quy ước file); các cụm động từ "Ngoáy"/"Thúc" nơi くっ đã hòa vào nghĩa của cả câu
   (ポーレットh3 894, れいなh2 1047, lr_ハチロクh1 1423, 日々姫h5 1177/1321); ハチロクh3 1815 "Ngoáy" (1 dòng duy nhất,
   phán đoán: giữ — chuỗi （くっ――くくっ――） là SFX cọ xát, "Ngoáy" diễn nghĩa hành động; đổi thành "Ư" sẽ mất nghĩa hành động).
6. **Thoại phi-H (Common/các route thường): くっ → giữ "Ư".** Đây là tiếng gầm gừ trong thoại thường, audit chưa từng flag,
   và bằng chứng moan pass chỉ áp cho H-scene. Không đụng.

**Số dòng ảnh hưởng (ước):** tối thiểu 50 dòng moan-giữ "Ư" + các dòng H-file くっ→"Ư" chưa từng được xem —
batch thống nhất phải căn token từng dòng (con số thô 280 dòng thoại H-file chứa "Ư" bị nhiễu, không dùng làm số fix).
Cộng 5 dòng "Hự" đơn lẻ → "Ku". Không đụng các file "Hự" (12 dòng) và phi-H.

---

## M8. や / やっ → "Ya" vs "Á" (và "A" / "Yan")

### Câu hỏi
Có ranh giới sạch từ chối-vs-rên không?

### Tiền lệ đã xác minh

**Từ chối độc lập → "Á":**
- lr_凪h2 1181 — JP 「ひうっ！？ やっ！ おしっこのとこ――んっ！ ふあっ！ そんなとこ――すったら――ばっちかばい」
  / TW 「呀！呀！是尿尿的地方……嗯！啊！吸這種地方……好髒」 / AUDIT "Hiu!? Á! Chỗ đi tiểu——ưm! …"
- lr_凪h2 1187 — JP 「ひゃうううっ！？ やっ！ やらっ！ 抜けちゃうっ！ おまんこから、いっちゃう！ おちんち――ふあっ！？」
  / TW 「呀？！呀！不要！要出去了！…」 / AUDIT "Hyauuu!? Á! Không chịu! Tuột ra mất! …"
- lr_凪h2 1203 — JP 「ふあっ！ やぁっ！ やぁああっ！ にーさんの、おちんち、んっ――こわ――こわれるの――やあっ！」
  / TW 「哇！不要！不要啊！大哥哥的雞雞……要把咱弄瘋了……不要啊！」 / MOAN "Fua! Áa! Áaaa! … áa!"
  (moan chỉ sửa đếm; token cuối "áa!" chữ thường — không nhất quán với 2 token đầu, xem quy tắc)
- 日々姫h2 1066 — JP 「やっ！ いまっ――乳首っ――んっ――…」 / TW 「呀！現在――…」 / CSV3 "Á! Bây giờ——…"
- 日々姫h2 1067 — JP 「やっ！ おちんちん――ンッ――すごく――…」 / TW 「呀！雞雞――嗯――…」 / CSV3 "Á! Cậu nhỏ——…"

**Giật mình/thán từ → "Á":**
- ポーレットh8 2187 — JP 「えっ！？ やっ――いまのッ――んひゃうっ！？…」 / TW 「哎！？呀——」 / MOAN "Á——…" (tiền lệ TỒN TẠI — xem §0.9)
- 日々姫h2 1220 — JP 「すがたみ？ ……えっ！？ やっ！？ 姿見っ！？」 / TW 「穿衣鏡？……哎！？呀！？穿衣鏡！？」 / CSV3 "…Hả!? Á!? …"
- 凪ふかみh1 1227 — JP (やっ！？ đầu dòng) / "Á!?" (giữ)

**Từ chối trong chuỗi rên → "Yaa" (XUNG ĐỘT với ranh giới từ chối→"Á"):**
- ポーレットh7 854 — JP 「ふあっ――あっ――やぁっ――なのおっ！ ずりずり、だけ――でっ！ セックス、なしで、イクの、やぁぁ！」
  / TW 「呼啊——啊——我不要！我不想！不做愛——光是被摸一摸、就高潮——不要！」
  / MOAN "Fua——a——Yaa——không chịu đâu! Chỉ cọ xát, thôi——mà! Không quan hệ, mà lên đỉnh, không chịu đâu!"
  (TW rõ ràng là từ chối, nhưng moan fix dùng "Yaa" + diễn nghĩa "không chịu đâu". Flag F6 của file ghi "やぁぁ 'chìm trong diễn nghĩa".)

**Chuỗi hơi thở/rên → "Ya"/"Yaa":**
- lr_凪h2 1325 — JP 「にぃ――さぁん――んっ――やぁ――ん――はっ――いじある――しな、いでっ――ンッ――もっと、してぇ」
  / TW 「大哥哥……嗯……呀……嗯……啊……不要欺負人……嗯……再來刺激點的」 / MOAN "…ưm——yaa——ưm——ha——…"
  (やぁ nối bằng ——, không có ！, giữa chuỗi hơi thở)
- lr_日々姫ふかみh1 1334 — JP 「やっ！？ 激しっ――ですっ――ふあっ！ あっ！」 / TW 「呀！？ 太激——烈了——…」 / MOAN "Ya!? Mãnh liệt――quá――fua! A!"
  (やっ！？ ở đây là thán từ "mãnh liệt quá", không phải từ chối — TW không có 不要)
- ポーレットh5 848/854/856/862/921/927 — や(っ/あ) → "Ya"/"Yaa" (chuỗi rên)
- lr真闇追加h 1067 やっ→"Ya", 1013 やあっ→"yaa" (chuỗi rên; tiền lệ h6 816)
- 真闇h1 1010/1011 やっ/や→"Ya"
- lr_稀咲h1 991 — JP 「ふえっ！？ やあっ！ んっ！ もう、ちょっと――ふあっ！ もうちょっと、だけ、がまん――ねっ！！」
  / TW 「哎？！呀啊！啊嗯，再等一下……蛤啊！再忍一下就好！！」 / MOAN "Fue!? Yaa! Ưm! …"
  (やあっ！ là token thứ 2 trong chuỗi rên — sau nó là んっ！ ふあっ！ (token rên), không phải câu từ.
  Lý do của chính agent trong REVIEW: "ふえっ nằm ĐẦU CHUỖI RÊN (tiếp nối やあっ――んっ――ふあっ),
  không phải thán từ ngạc nhiên độc lập"; "やあっ → 'Yaa' (や+あ = 2 a): 'Nha' làm mất phụ âm y. TW 呀啊 xác nhận âm 'yaa'."
  → GIỮ "Yaa!".)

**Diễn nghĩa (từ chối lồng trong câu) → giữ nghĩa:**
- 凪h1 1105 — JP 「…べろ、やっ――こんなに――ほじって――…」 / AUDIT "Không——Móc ngoáy——…"
- lr_れいな追加h 1048 — JP 「やぁあ――そんなの――…やぁ、ですよぉ」 / "Đừng——…đừng có so sánh…"

**"A" trần / "Yan" (không nhất quán):**
- 日々姫h2 1055 — JP 「やっ――やんっ！ おちんちん――にぃにの、ちんちん、おまんこで――ぎゅって――抱きしめたいのにっ」
  / TW 「呀――呀！…」 / AUDIT "A——Yan! …" (cùng một dòng: やっ→"A" nhưng やんっ→"Yan" — không nhất quán)
- 日々姫h2 1060 — JP 「や……ぁ……わたしっ――あ……私、の、おまん、こ――よだれ、垂らして――ひくひく、して――ます」
  / TW 「呀……啊……我――…」 / CSV3 "A... á... em——A... …" (chuỗi hơi thở kéo dài, ……-nối)
- 日々姫h2 1055 やんっ→"Yan" là tiền lệ duy nhất cho やん (project-wide: "Yan" chỉ 8 dòng).

### Đếm toàn dự án
- JP có token や: **2.063 dòng**. JP có やっ: **985** (Á 353 / Ya 110 / diễn nghĩa 43 / "A" trần 38 / "Yan" 1 / khác 440).
  JP có やぁ/やあ: **160** (Ya 64 / Á 38 / diễn nghĩa 25 / "A" 6 / khác 27).
- Riêng H-file: Ya/Yaa 100 / Á/á 99 / "A" trần 28 / diễn nghĩa 35 / khác 78 — gần như ngang nhau, chứng tỏ ranh giới
  là **ngữ cảnh**, không phải âm.
- "A" trần cho や-token: 64 dòng toàn dự án.

### QUY TẮC ĐỀ XUẤT — M8 (độ tin cậy: cao)
Ranh giới KHÔNG phải từ chối-vs-rên (h7 854 phá vỡ: từ chối rõ ràng nhưng → "Yaa").
Ranh giới là **token kề sau nó trong cùng dòng là gì**:
1. **や(っ/ぁ/あ) đứng trước câu từ / nội dung từ chối (TW 不要, hoặc sau nó là từ chứ không phải token rên) → "Á"**
   (giữ nguyên độ dài: やぁ→"Áa", やぁああ→"Áaaa").
   Áp dụng: lr_凪h2 1181/1187/1203, 日々姫h2 1066/1067/1220, ポーレットh8 2187, 凪ふかみh1 1227.
2. **や(っ/ぁ/あ) nằm trong chuỗi token rên (kề trước/sau là ふあっ/んっ/あっ… — âm, không phải từ) → "Ya"/"Yaa"**
   (giữ nguyên độ dài, chữ thường khi ở giữa chuỗi).
   Áp dụng: lr_凪h2 1325 ("yaa"), ポーレットh5 ×6, lr真闇追加h 1067/1013, 真闇h1 1010/1011,
   h7 854 ("Yaa" — giữ nguyên moan fix), lr_稀咲h1 991 ("Yaa!" — giữ nguyên; lý do của agent: đầu chuỗi rên,
   TW 呀啊 xác nhận âm "yaa").
   Ngoại lệ được chấp nhận: lr_日々姫ふかみh1 1334 "Ya!?" (moan agent quyết có chủ ý; TW chỉ là 呀 — âm thuần,
   không có 不要; line diễn ngạc nhiên về cường độ "mãnh liệt quá" chứ không phải từ chối).
3. **や đã được diễn nghĩa thành từ ("Đừng"/"Không…") trong câu → giữ nghĩa** (凪h1 1105, lr_れいな追加h 1048).
4. **Bỏ "A" trần cho や:** "A" chỉ đúng khi JP không có phụ âm mora (あ/あぁ). Tất cả や→"A" đổi theo quy tắc 1/2:
   - 日々姫h2 1055 "A——Yan!" → **"Ya——Yan!"** (cùng dòng đã có やんっ→"Yan"; "A" vs "Yan" là không nhất quán;
     やっ ở đây kề やんっ — token âm — nên theo quy tắc 2).
   - 日々姫h2 1060 "A... á..." → **"Ya... aa..."** (chuỗi hơi thở ……-nối).
5. **Dòng cần sửa theo quy tắc:** lr_凪h2 1203 token cuối "áa!" → **"Áa!"** (viết hoa thống nhất với 2 token đầu "Áa! Áaaa!").

**Số dòng ảnh hưởng (ước):** quy tắc 1/2 xác nhận phần lớn giá trị hiện tại (H-file Ya 100 / Á 99 đã đúng hướng);
sửa: 1203 viết hoa (1), các dòng "A" trần cho や (64 dòng toàn dự án, trong đó H-file 28) → "Ya"/"Á" theo token kề.
991 và 1334 GIỮ NGUYÊN ("Yaa!"/"Ya!?" — đã quyết có lý do).

---

## M9. ふっ → "Fu" vs "phù" vs "Hư" vs "Phư"

### Câu hỏi
Có mẫu theo nhân vật không?

### Tiền lệ đã xác minh

**→ "Fu" (moan pass đổi):**
- 日々姫h3 — 8 dòng: 1013 (JP 「ひゃっ――あっ――おっぱい――ンッ――にぃに――優、しいっ――ふっ――んっ」 / TW 「呀――啊――胸部――嗯――阿哥――好溫柔――呼――嗯」 / MOAN "…Fu――ưm"),
  1018/1021/1039/1055/1109/1112/1142 tương tự (F2: không hoàn về "Phù")
- れいなh4 — 5 dòng: 1936 (JP 「んっ――ふっ――あっ――さき、ぽっ――…」 / MOAN "Ưm——Fu——a——…"), 2005/2015/2088/2134 (F2 mở)
- lr_日々姫h1 — F2 ("Fu" trong file này vs "phù"/"Hư" các file khác; dạng tách "Fu, a" 1047/1160)
- lr稀咲追加h — 782 (JP 「――んっ――ふっ――あ。毎晩、みたいに――…」 / MOAN "——Ưm——Fu——A. …"), 1112 (JP 「あ……ふっ――ふあっ――…」 / MOAN "A……Fu――Fua――…")
- 日々姫h4 — 1029 (JP 「んっ――んー……ん、ふっ――あむっ――れろっ――…」 / MOAN "…ưm, Fu――ngoạm――liếm――…")
- lr_ハチロクh1 — 4 dòng "Fu" (1252/1149/1153…); ハチロクh2 — 2 dòng; lr_ニイロクh — 2 dòng; 日々姫h3 — 4 dòng (đếm theo file, thoại H-file)

**→ "phù" (giữ):**
- 日々姫h2 — 1096/1126/1133/1263 (F2 mở); 1126 JP 「んきゅっ――ふっ――あっ――…」 / MOAN "Nkyu——Phù——A——…"
  (cùng dòng có んきゅ→"Nkyu" nhưng ふっ vẫn "Phù" — file giữ "phù" ngay cả khi đã romaji hóa token kề)
- れいなh3 — 1067 (×2: JP 「んぐっ――ほっ……ふっ――あっ――…」 / CSV3 "…phù——a——…"), 1071 (JP 「んきゅっ！ ふっ――やっっ――…」 / AUDIT "Ưm kyu! Phù——ya——…"),
  1092 (JP 「ンぶっ――むううっ――んっ――ふっ――…」 / MOAN "…phù——ưm——…"), 1101 (JP 「ふっ……んっ――チュっ………」 / CSV3 "Phù……ưm——…") — F11 mở
- ハチロクh6 — 17 dòng "phù" (ngắn ふっ/ぷっ → "phù", giữ); ポーレットh6 — 9 dòng "phù" (F7 mở);
  ふかみh2 — 10 dòng; ふかみh3 — 9 dòng (tiền lệ khóa: "ふ/ふっ→'phù'"); 凪h1 — 7 dòng; 凪h2 — 8 dòng;
  日々姫h5 — 12 dòng; ポーレットh5 — 9 dòng; ハチロクh7/h8 — 6–7 dòng; れいなh2 — 8 dòng
- lr真闇追加h — 14 dòng "phù" (audit §4: "giữ ふっ độc lập → 'phù'"); lr追加_ひよこ… — 18 dòng "phù"

**→ "Hư"/"hư" (quy ước file):**
- lr_日々姫ふかみh1 — 1350 (JP 「ふっ――あっ――ぁっ――あっ！」 / TW 「呼——啊——啊——啊！」 / CSV3 "Hư――a――a――a!"),
  1479 (JP 「ん……ぁ――あっ――ふっ――あっ――ん――ちゅっ――…」 / CSV3 "…hư――a――ưm――…")
- lr_ハチロクh2/h3 — "hư" chữ thường giữa chuỗi (vd 1424/1447, 1318) — đếm theo file bị thiếu do classifier (xem ghi chú đếm)

**→ "Phư" (quy ước file Mayami):**
- 真闇h1 — 5 dòng "Phư" (1034/1040…); 真闇h2 — 4 dòng (1032: JP 「ふっ……あっ――はっ――んっ――…」 / TW 「呼……啊――哈――嗯――…」 / AUDIT "Phư……a――ha――ưm――…";
  1084); 真闇h3 — 4 "Phư" + 3 "phù" (TRỘN trong file — F2 mở)

### Đếm toàn dự án
- Dòng JP chứa ふっ: **917**. "phù" 230 / "Hư" 117 / "Fu" 47 / "Phu" (không dấu) 27 / "Phư" 15 / khác 481
  (481 "khác" phần lớn là dòng thoại thường — ふっ trong câu dài được diễn nghĩa, hoặc token ふっ không được render riêng).
- **Không có mẫu theo nhân vật:** Reina h3 → "phù" (4 dòng) nhưng Reina h4 → "Fu" (5 dòng) — cùng nhân vật, khác file.
  Hachiroku h6 → "phù" (17) nhưng lr_ハチロクh1 → "Fu" (4) và lr_ハチロクh2 → "hư". Hibiki h2/h5 → "phù", h3/h4 → "Fu".
  Mẫu duy nhất là **theo file** (agent của file đó chọn và giữ nhất quán trong file).

### QUY TẮC ĐỀ XUẤT — M9 (độ tin cậy: cao cho "giữ theo file", trung bình cho các fix lẻ)
1. **KHÔNG thống nhất ふっ toàn dự án. Giữ theo file** (mỗi file giữ dạng chủ đạo của nó: "Fu" / "phù" / "Hư" / "Phư").
   Lý do: ranh giới là file, không phải nhân vật hay ngữ cảnh; moan pass đã giữ "phù" ở ~25 file và đổi sang "Fu" ở ~8 file —
   lật ngược một phía sẽ đụng ~180–360 dòng đã quyết có chủ ý, không có lợi ích cho độc giả (cả "Fu" và "phù" đều đọc được,
   và quy tắc ngẫu hứng theo nhân vật/ngữ cảnh của Hieu 19/11 chấp nhận biến thiên theo file).
2. **Thống nhất NỘI BỘ file (batch kiểm tra từng file, lấy dạng đa số):**
   - **真闇h3: "phù" (3 dòng) → "Phư"** (quy ước Mayami: h1 5× "Phư", h2 4× "Phư"; h3 trộn 4 "Phư" + 3 "phù" là lỗi nhất quán nội bộ).
   - Các file trộn khác: ハチロクh9 ("phù" 3 + "Fu" 3 — hòa; batch quyết theo chuỗi rên: token trong chuỗi rên → "Fu",
     token độc lập → giữ "phù"), lr_ニイロクh ("Fu" 2 + "phù" 1 → "Fu"), lr_真闇h1 ("Fu" 1 + "phù" 1 — kiểm tra tay từng dòng).
   - lr_日々姫ふかみh1 "Hư" (2 dòng: 1350/1479) — giữ (quy ước file, dù chỉ 2 dòng; không có dạng cạnh tranh trong file).
3. **Không đụng:** các file đã nhất quán một dạng (danh sách đếm theo file ở trên).

**Số dòng ảnh hưởng:** ~3–6 dòng (chủ yếu 真闇h3 3 dòng + các file trộn lẻ). Không có batch lớn.

---

## M10. ふぇ / ふえ → "Fue" vs "Phuê" — và reina-h3 1133

### Câu hỏi
Thán từ ngạc nhiên vs token rên: tách ra được không? Điều tra reina-h3 1133 và tiền lệ 凪h1 1091.

### Tiền lệ đã xác minh — trung tâm vụ việc

**reina-h3 1133 (dòng cần quyết):**
- JP: 「はいですぅ！ いっぱい！ いっぱいいっぱい！ んっ――れいなに――ぴゅっぴゅっ、して――ふえっ？」
- TW: 「好的！來吧，來吧！把玲奈……射得滿滿的」 — **TW KHÔNG có tương đương của ふえっ？** (bỏ hẳn)
- VN hiện tại (CSV3, chưa từng được audit/moan đụng): 「Vâng ạ! Thật nhiều! Thật nhiều thật nhiều! Ưm——vào trong Reina——bắn ra đi——hả?」
- Bối cảnh: cuối một câu cầu xin dài; các token trước là んっ và SFX hành động ぴゅっぴゅっ — ふえっ？ KHÔNG nằm trong
  chuỗi rên (không có ふあっ/あっ/んっ rên kề sau), cũng KHÔNG đứng độc lập đầu dòng. Nó là một tiếng gasp hỏi ở cuối câu.

**凪h1 1091 (tiền lệ cha-quyết):**
- JP: 「ふぇ？ ――あっ！ あ、わかったばいっ」 / TW: 「哎？ ……啊！ 啊，好的」
- Moan REVERT audit "Phuê?" → **"Hể?"** (cha quyết 22/11 ~10:31, F30).
- Bối cảnh: thán từ ngạc nhiên độc lập, tiếp theo là câu nhận ra ("à, em hiểu rồi").

**Token rên trong chuỗi → "Fue" (nhất quán, ~10 dòng):**
- 日々姫h1 1022 — JP 「ふえっ！？ あっ――んっ――なか――ひあっ――めくれ――てっ――んっ！！」 / TW 「哎！？啊――嗯――裡面――呀――…」
  / MOAN "Fue!? A——Ưm——…" (giữa chuỗi rên; F4 của file ghi khác với tiền lệ thán từ độc lập)
- 日々姫h4 990 — JP 「ふあっ……あっ……あっ――ふえっ――あっ――あ」 / MOAN "Fua……a……a――Fue――a――a"
- 日々姫h4 991 — JP 「ふぇ……ぁ……わた……私、おしっこ――おもらし――全部……全部して……イっちゃっ――きゅふっ！！？」 / MOAN "Fue……a………"
- 凪h1 1046 — JP 「やっっ――ふぇっっ――へん――ヘン、ばいっ――…」 / MOAN "Ya——Fue——…"
- 凪h1 1086 — JP 「ふぇっ――あっ――お、まん、こ――んっ――…」 / MOAN "Fue——A——…"
- 凪h1 1087 — JP 「ふぇっ――あっ――びゅって――びゅう、って――…」 / MOAN "Fue——A——…"
- れいなh4 1976 — JP 「ぅあぁ――ぁっ――がく、がく――しちゃうっ――ふぇ――あ――きもち――きもち、いいっ――ふ、あ」 / MOAN "…Fue——a——sướng——…"
- lr_稀咲h1 991 — JP 「ふえっ！？ やあっ！ んっ！ もう、ちょっと――ふあっ！ もうちょっと、だけ、がまん――ねっ！！」 / MOAN "Fue!? Yaa! …"
  (xem §M8: agent ghi rõ ふえっ "nằm ĐẦU CHUỖI RÊN (tiếp nối やあっ――んっ――ふあっ), không phải thán từ ngạc nhiên độc lập";
  "'Hả' làm mất phụ âm f (ふ là f, không phải h)" — GIỮ "Fue!?")

**Thán từ ngạc nhiên độc lập → "Hể?" (theo tiền lệ 1091):**
- 凪h1 1090 — JP 「ふえっ！？」 (đứng một mình cả dòng) / TW 「哎！？」 / AUDIT "Phuê!?" (flag: chờ 1133)
- ふかみh1 993 — JP 「ふえっ！！？」 / TW 「哎！！？」 / AUDIT "Phuê!?" (lưu ý: VN CSV3 của dòng này là câu SAI LỆCH hoàn toàn — audit đã sửa thành "Phuê!?")
- れいなh3 1026 — JP 「ふえ？」 (đứng một mình) / TW 「咦？」 / CSV3 "Fue?" (chưa từng được flag)
- れいなh4 1897 — JP 「ふえ？ れいな、なにかかんちがいしちゃってるですかあ？」 / TW 「咦？玲奈弄錯了什麼事情嗎」 / CSV3 "Fue? …"
  (tiếp theo là câu hỏi "Reina đã hiểu lầm chuyện gì sao ạ?" — thán từ ngạc nhiên trong thoại, không phải rên)
- lr_稀咲h1 992 — JP 「ふえっ！？ あ！ あっ――ううん――なんでも……なんでもない……ただ――うぁっ――」
  / TW 「哎？！啊、啊……沒什麼……什麼都沒有……只是……」 / MOAN "Fue!? A! Á――không――…"
  (tiếp theo là câu phủ nhận "không có gì… không có gì đâu…" — giống cấu trúc 1091 (thán từ + câu lời nói),
  KHÔNG giống 991 (tiếp theo là token rên). Agent gộp 992 với 991 ("như 991"), nhưng ngữ cảnh khác hẳn.)

**Dạng kéo dài → giữ âm "Phuê…" (TW là tiếng thở dài, không phải ngạc nhiên):**
- 凪ふかみ01_流れ 1547 — JP 「ふぇぇっ」 / TW 「嗚唉」 / AUDIT "Phuêê." (đứng một mình; TW 嗚唉 = tiếng thở dài kéo dài)
- 共通13 2038 — JP 「ふぇぇぇええっ！？ だいじょうぶっ！ 大丈夫っ！ です」 / TW 「哎哎哎！？沒事！沒事的！嗯」 / AUDIT "Phuêêêêê!? …"
  (tiếng gasp hoảng hốt kéo dài 5 mora trước câu trấn an — "Hể" không kéo dài được tự nhiên)
- ハチロク02 2170 — JP 「ふえぇ……」 / TW 「嗚……」 / AUDIT "Phuêê……"

**Ngoài phạm vi:** lrれいな追加h 1245 「ほふぇふぇぇ、へふぉほぉ」 → "Ê hê hê, thế này nha~" (CSV3; âm cười/ngọng, không phải rên hay thán từ) — để nguyên.

### Đếm toàn dự án
- Dòng JP chứa ふぇ/ふえ: **94**. "Fue" 29 / "Phuê" 21 / "Hả" 15 / "Hể" 11 / "Hưa" 1 / khác 17.
  ("Hả" 15 dòng phần lớn là えっ/はっ… — không phải ふぇ; chỉ 1133 là ふえ→"Hả".)

### QUY TẮC ĐỀ XUẤT — M10 (độ tin cậy: cao cho chuỗi rên, trung bình-cao cho thán từ, trung bình cho 1133)
Tách được — bằng **token kề sau và TW**, không bằng dấu câu:
1. **Token rên (kề trước/sau là token rên: ふあっ/あっ/んっ/ひあっ…) → romaji "Fue".**
   Áp dụng: 1022, 990/991 (日々姫h4), 1046/1086/1087 (凪h1), 1976, lr_稀咲h1 991 (GIỮ "Fue!?").
2. **Thán từ ngạc nhiên độc lập — đứng một mình hoặc tiếp theo là câu lời nói (nhận ra/phủ nhận/hỏi), TW 哎/咦 — → thán từ Việt "Hể?"**
   (theo tiền lệ cha-quyết 1091). Áp dụng: **1090 → "Hể!?"**, **993 → "Hể!!?"**, **1026 → "Hể?"**,
   **1897 → "Hể?"**, **lr_稀咲h1 992 → "Hể!?"** (lật moan fix "Fue!?" — 992 tiếp theo là câu phủ nhận "không có gì…",
   giống cấu trúc 1091, không giống 991; ghi rõ đây là phán đoán lật một fix có chủ ý, độ tin cậy trung bình).
3. **Dạng kéo dài (ふぇぇ/ふえぇ, ≥2 mora kéo dài) → giữ âm "Phuê…" với độ dài khớp JP.**
   Áp dụng: 凪ふかみ01_流れ 1547 "Phuêê." (giữ), 共通13 2038 "Phuêêêêê!?" (giữ), ハチロク02 2170 "Phuêê……" (giữ).
4. **reina-h3 1133 → GIỮ "Hả?"** (phán đoán, độ tin cậy trung bình).
   Lý do: ふえっ？ ở đây là tiếng gasp hỏi ở cuối câu cầu xin — không phải token rên (quy tắc 1 không áp),
   không phải thán từ ngạc nhiên độc lập (quy tắc 2 không áp: không có câu nhận ra/hỏi tiếp theo, và TW bỏ hẳn token này
   nên không có bằng chứng TW 哎/咦). "Hả?" diễn đúng sắc thái hỏi ("hả?" = "huh?") hơn "Hể?" (ngạc nhiên) hay "Phuê?" (âm thuần).
   Đây là dòng duy nhất ふえ→"Hả" trong dự án; giữ nguyên giá trị CSV3 chưa từng bị đụng.

**Số dòng ảnh hưởng:** 6 dòng đổi sang "Hể?" (1090, 993, 1026, 1897, 992 + xem lại); 1133 giữ; 3 dòng kéo dài giữ.

---

## M11. ふや → "Phuya" vs "Fuya" vs "Phuyan"

### Câu hỏi
Ba dạng này phân biệt thế nào?

### Tiền lệ đã xác minh

**→ "Phuya" (audit giữ):**
- 凪h1 1053 — JP 「ふやっ――あっ――これ――これ――んっ――…」 / TW 「呀……啊……這個……這個……嗯……」 / AUDIT "Phuya——A——…"
- 凪h1 1057 — JP 「ふやっ！」 / TW 「呀！」 / AUDIT "Phuya!"
- 凪h1 1081 — JP 「ふやうっ！」 / TW 「哇！」 / AUDIT "Phuyau!"
- 日々姫h3 1042 — JP 「ふやっ！？ にぃに――舐めてっ――んっ――…」 / TW 「呀！？阿哥――舔了――嗯――…」 / MOAN "Phuya!? …" (moan giữ)
- 日々姫h4 964 — JP 「いうっ！？ ――かっ――ふやっ――あぁぁぁぁぁああああああああんっ！！！」 / AUDIT "…Phuya――…"
- 真闇h1 1021 — JP 「ふや……んっ――きもち、い――」 / TW 「呼……嗯――好舒服――」 / AUDIT "Phuya……ưm――…"
- lr_凪h1 1129 — JP 「ふやっ！」 / CSV3 "Phuya!" (giữ)

**→ "Fuya" (moan pass đổi):**
- 日々姫h1 1003 — JP 「ふやっ！？ あっ――んくううううううううっ！！！」 / TW 「呀！？啊――嗯啊――！！！」 / MOAN "Fuya!? A——Nkuuuuuuuuu!!!"
  (tiền lệ ghi trong file: ハチロクh5 1064/1065)
- lr_ふかみh2 — ふや→"Fuya" trong danh sách romaji 25 dòng của file
- lr_れいな追加h 1065/1080 — ふや→"Fuya"/"Fuyaaaaaa"

**→ "Phuyan" (chỉ khi có ん):**
- 日々姫h2 1081 — JP 「ふやんっ！！」 / TW 「哎呀！！」 / AUDIT "Phuyan!!" (CSV3 cũ là "Huyan!!" — audit sửa; ん làm thành "Phuyan")
- ふかみh3 2366 — ふやん→"Phuyan" (cùng dạng)

### Đếm toàn dự án
- Dòng JP chứa ふや: **53**. "Fuya" 35 / "Phuya" 14 / "Phuyan" 2 / khác 2.
  (Romaji đã là dạng đa số. Lưu ý: đếm theo dòng; "Fuya" 35 gồm cả các file lr_ハチロクh1 dùng "Fuya" nhất quán.)

### QUY TẮC ĐỀ XUẤT — M11 (độ tin cậy: trung bình-cao)
1. **H-scene ふや(っ/ぁ/う) → romaji "Fuya"** (giữ nguyên độ dài: ふやぁ→"Fuyaa", ふやうっ→"Fuyau").
   Lý do: romaji fallback đã duyệt 21/11 (VN nghe ngượng → romaji); moan pass đã áp romaji cho ふや ở 4+ file
   (日々姫h1, lr_ふかみh2, lr_れいな追加h, lr_ハチロクh1); đếm hiện tại romaji đã dẫn 35 vs 14;
   cùng họ với quyết định ひゃ-family 21/11 (âm khẩu cái hóa trong rên H → romaji).
   Quy tắc fa/fu đã chốt (ふやぁ → "phuya") vẫn giữ cho **thoại phi-H** — chỉ H-scene mới đổi sang romaji.
2. **ふやん(っ) → "Fuyan"** (giữ ん): 日々姫h2 1081 "Phuyan!!" → **"Fuyan!!"**; ふかみh3 2366 "Phuyan" → **"Fuyan"**.
3. **Các dòng đổi:** 凪h1 1053/1057/1081 ("Phuya"→"Fuya", "Phuyau"→"Fuyau"), 日々姫h3 1042, 日々姫h4 964,
   真闇h1 1021, lr_凪h1 1129 + các dòng "Phuya" còn lại (~14 dòng tổng).

**Số dòng ảnh hưởng:** ~16 dòng ("Phuya" 14 + "Phuyan" 2). Đây là thay đổi thống nhất có chủ ý —
lật các giá trị audit-lock ở 凪h1/日々姫h3/h4/真闇h1 — nên điều phối viên xác nhận lại trước khi áp
(vì audit đã "chốt" ふやぁ→"phuya"; lý do lật: moan pass + romaji fallback là quyết định sau, chuyên về rên H).

---

## M14. SFX miêu tả （ ） — công thức nguyên âm vs động từ Việt

### Câu hỏi
Giữ giá trị moan-pass theo từng file, hay thống nhất về một cách? (Và: cách đếm độ dài có đúng không?)

### Bằng chứng: hai hệ thống cùng tồn tại sau moan pass

**Hệ romaji (moan pass đổi SFX dài → romaji — đã kiểm chứng đếm bằng máy, đúng):**
- 真闇h2 — 1820/1823/1832/1834/1837/1846/1848/1872 (vd 1832 （くぱああっ） → "Kupaaa" — 3a đúng ngưỡng;
  1846 （きゅんっ――きゅううううっ） → "（Thắt lại――Kyuuuuu）" — chỉ token DÀI đổi, token ngắn giữ "Thắt lại")
- ハチロクh3 — 1828/1829/1832/1835/1836/1837 (vd 1836 （きゅううううううっ） → "Kyuuuuuuu!!!" — 7u đúng)
- 日々姫h4 — 1757/1765/1783/1758/1743/1762/1770/1754 (vd 1754 （じゅぶっ！ じゅっっ！ じゅばっっ！ じゅぼっ！） → "Jubu! Ju!! Juba!! Jubo!")
- lr稀咲追加h — 1819/1823/1857/1883 (SFX dài → romaji)
- 真闇h2 1822/1882 — （ぎちちちちちちっ！）/（キチチチチチチっ！） → 6× "Siết" (đếm số lần lặp đúng)

**Hệ động từ Việt + kéo dài phụ âm/nguyên âm (moan pass GIỮ — nhưng đếm SAI, đã kiểm chứng bằng máy):**
- 凪h1 1768 （ずぶうううううううううううううううっ！！！） 15う → "（Phập pppppppppppppppppppp!!!）" = 20 p — **lệch +5**
- 凪h1 1794 （ずっ――るぅぅぅぅううううううっ） 10う → "（Trượt——tuốtttttt）" = 7 t — **lệch −3**
- 凪h1 1797 （ずるうううううううううっ！！！） 9う → "（Trượt tuốtttttttttt!!!）" = 11 t — **lệch +2**
- 凪h1 1808 （きゅうううううううううんっ！！！） 9う → "（Siết chặttttttttttttt!!!）" = 14 t — **lệch +5**
- lr_ハチロクh3 1909 （じゅぶうううううううううううっ！！――ごっ！） 11う → "（Phậpppppppppppp!! …）" = 12 p — lệch +1
- lr_ハチロクh3 1966 （ぼぢゅうううううっ！！！！――…） 5う → "（Phậppppppp!!!! …）" = 7 p — lệch +2
- lr_ハチロクh3 1983 （ぢゅぶうううううううううううううっ！！！！） 13う → "（Phậpppppppppppp!!!!）" = 12 p — lệch −1
- lr_日々姫h2 1666 （びゅっ！ ぶりゅっ！ びゅぶっ！ ぶびゅうう！） token cuối 2う → "（…Phụtttt!）" = 4 t — lệch +2;
  1668 （どりゅうう！ ぶりゅうっ！ びゅぶっ！ ぶりゅ！） token đầu 2う → "（Phụttttt! …）" = 5 t — lệch +3
  (cùng 2–3u mà 4t vs 5t — chính flag F1 của file)
- lr_日々姫h2 1679 （ぎいっ） → "（Kétttt）" = 4 t — **sai LOẠI chữ kéo**: JP dài ở nguyên âm い (×2), không phải phụ âm t
- lr_日々姫h2 1681 （ちいいいいいいっ） い×7 → "（Xoètttttt）" = 6 t — **sai loại chữ kéo** (phải kéo nguyên âm è, không phải t)
- lr_日々姫h1 1773 きゅううっ (2う) → "Siết lạiiii!" = 4 i; 1795 きゅううううっ (4う) → "Siết chặt lạiiii!" = 4 i —
  **cùng 4 i cho 2う vs 4う**; 1797 (15う) → 14 i (lệch −1); 1810 (9う) → 10 a (đúng); 1818 (13う) → 10 a (lệch −3,
  giống hệt 1810 dù 9う vs 13う)
- lr_日々姫ふかみh1 2467 （ずりゅううううううううううっっっっ！！！！！！） 10う → "（Trơn tuột!!!!!!）" — **không kéo gì**;
  2468 （ずりゅうううううっっっっっっっっ！！！！） 5う → "（Trơn tuộtttttttt!!!!）" = 8 t — **đảo ngược: dòng NGẮN hơn lại được kéo, dòng DÀI hơn thì không**
- 日々姫h2 1787 （ずるうううううっっ！！！） 5う → "（Trượtttttt!!!）" = 6 t (lệch +1);
  1797 （きゅううううっ！） 4う → "（Siết chặtttt!）" = 4 t (đúng); 1798 （きゅんっ――きゅうううんっ） 3う → "（…Siết chặtttt）" = 4 t (lệch +1)

**Mất độ dài hoàn toàn (động từ ngắn, không kéo):**
- 稀咲h2 1932 （ずっ――ずるうううううううっ） 7う → "（Phập――phập）"; 1933 （ずぶううううっ！ ずばんっ！！！） 4う → "（Phập! Phập!!!）";
  1934 （ずぶううううううううううっ！！） 10う → "（Phập!!）"; 1935 （ずるうううううっっっ――） 5う → "（Phập――）";
  1936 （ずるうううううううっ！！！） 7う → "（Phập!!!）"; 1942 （ぐううっ！ ――――きゅんっ！） → "（Gừ! ――――Kyun!）";
  1944 spurt （どびゅっ！ びゅるっ！ どびゅるっ！ びゅうっ！） → "（Phụt! Phụt! Phụt! Phụt!）";
  1955 （びゅるるるるうぅぅっ！！！） → "（Phụt!!!）"; 1963 （きゅううううっ！） 4う → "（Siết chặt!）"
  (F1 của file: độ dài SFX mất trong các rendering VN)
- lr_日々姫h2 1659 （きゅんっ！ きゅううっ！ にゅるっ！ にゅむっ） 2う → "（Siết! Siết chặt! Trượt! Nhóp nhép）" — không kéo (F2)

### Đếm toàn dự án
- Dòng （ ） có JP kéo dài ≥3 mora: **460** toàn dự án, **403** trong H-file.
- Trong 403 dòng H-file: **122 dòng VN không có chuỗi chữ lặp nào** (mất độ dài hoàn toàn hoặc dùng từ "dài" thay cho kéo chữ).
- SFX dài きゅ trong （ ） ở H-file: động từ Việt 84 vs romaji 13 vs khác 10 (xem M70) — hệ động từ là đa số áp đảo,
  moan pass chỉ đổi sang romaji ở 4 file.

### QUY TẮC ĐỀ XUẤT — M14 (độ tin cậy: cao cho "giữ theo file + sửa đếm", cao cho công thức đếm)
1. **KHÔNG thống nhất một hệ cho （ ） SFX. Giữ hệ của từng file** (romaji ở 真闇h2/ハチロクh3/日々姫h4/lr稀咲追加h;
   động từ Việt ở các file còn lại). Lý do: moan pass đã quyết có chủ ý cả hai hệ; hệ động từ chiếm đa số (84 vs 13 ở きゅ dài);
   đổi hệ sẽ xáo ~100+ dòng đã quyết mà không thêm nghĩa cho độc giả. Quy tắc ngẫu hứng của Hieu chấp nhận biến thiên theo file.
2. **Thống nhất CÁCH ĐẾM trong cả hai hệ — công thức tổng-Hepburn (khóa theo quy tắc đếm nguyên âm đã chốt):**
   **tổng số chữ kéo (tính cả chữ gốc) = 1 + số う/ぅ/ー kéo dài trong JP.**
   - Romaji: tổng số nguyên âm = 1 + số う/ぅ (vd きゅううううううっ = 7 u → "Kyuuuuuuu" — đã đúng ở ハチロクh3 1836).
   - Động từ Việt: tổng số phụ âm/nguyên âm kéo = 1 + số う/ぅ (vd ずぶ+15う → "Phập" + 14 p = 15 p tổng; きゅううううっ (4う) → "chặtttt" = 4 t tổng
     — 日々姫h2 1797/1798 đã đúng dạng này; きゅううっ (2う) → "lạiii" = 3 i tổng).
   - っ cuối không cộng thêm chữ kéo (っ đã thể hiện bằng dấu ! hoặc chữ chặn như "t"/"p" trong từ gốc).
3. **Sửa đếm ở các dòng đã kiểm chứng sai** (áp công thức §2, từng token): 凪h1 1768/1794/1797/1808;
   lr_ハチロクh3 1909/1966/1983; lr_日々姫h2 1666/1668; lr_日々姫h1 1773/1795/1797/1810/1818;
   lr_日々姫ふかみh1 2467/2468; 日々姫h2 1787/1798. Batch phải đếm bằng máy từng token (không đếm tay).
4. **Sửa LOẠI chữ kéo:** lr_日々姫h2 1679 （ぎいっ） và 1681 （ちいいいいいいっ） — JP dài ở **nguyên âm** (い),
   phải kéo nguyên âm ("Kéé…"/"Xoèè…"), không phải kéo t. (Phán đoán: 1679 い×2 → tổng 2 è? — ぎい = gi + i: nguyên âm è ×2;
   1681 い×7 → è ×8 tổng. Batch xác nhận lại.)
5. **Các dòng mất độ dài hoàn toàn → thêm kéo (theo hệ của file) hoặc đổi sang romaji nếu file là hệ romaji:**
   稀咲h2 1932–1936/1942/1944/1955/1963 (9 dòng — fix set chính của M14), lr_日々姫ふかみh1 2467, lr_日々姫h2 1659.
   Ngoại lệ: spurt SFX giữ đồng nhất "Phụt!" theo M72 (稀咲h2 1944/1955 — giữ "Phụt!" nhưng THÊM kéo cho token dài:
   vd 1955 （びゅるるるるうだぅっ） → "（Phụtttt!!!）" thay vì "（Phụt!!!）" — phán đoán, batch xác nhận).

**Số dòng ảnh hưởng:** ~122 dòng H-file mất kéo (cần rà từng dòng — không phải dòng nào cũng sai: có dòng dùng từ "dài" thay cho kéo,
vd ハチロクh7 1840 "Liếm dài" — giữ); cộng ~20 dòng đếm sai đã liệt kê. Đây là batch lớn nhất của đợt thống nhất này —
cần đếm máy từng token, không làm tay.

---

## M15. ん + phụ âm → romaji vs "Ưm"

### Câu hỏi
ん+phụ âm render thế nào? Còn んっ, んん thì sao?

### Tiền lệ đã xác minh

**んきゅ → "Nkyu":**
- ポーレットh6 836 — JP 「んうっ――ぷあっ！ あっ――んきゅっ！ …」 / TW 「嗯——呼啊！啊——嗯！…」 / MOAN "Ưm ư——Pua! A——Nkyu! …"
- ポーレットh6 868 — JP 「んきゅっっ――うっ――…」 / MOAN "Nkyu——ư——…"
- ハチロクh3 1218 — JP 「そう、てつ――さまっ！？ んきゅっ――そこっ――…」 / TW 「雙鐵少爺——！？嗯嗚——…」 / MOAN "…Nkyu——chỗ đó——…"
- 日々姫h2 1126 — JP 「んきゅっ――ふっ――あっ――…」 / MOAN "Nkyu——Phù——A——…"
- 日々姫h2 1138 — JP 「んきゅうううううううぅぅぅぅっ！！！」 / MOAN "Nkyuuuuuuuuuuuu!!!"
- 日々姫h2 1139 — JP 「んきゅんっ！」 / MOAN "Nkyun!"
- 真闇h3 2278 — JP 「あっ！ んくゅうぅぅぅぅぅぅぅぅぅぅんっ！！！」 / MOAN "Á! Nkyuuuuuuuuuuuun!!!" (đếm đúng: 12 u, 2 n — xem §0.10)

**んく → "Nku":**
- 日々姫h4 1040 — JP 「ん……ちゅうっ……ちゅっ――あむっっ――んっ――ちゅき――にぃに……れるっ……ん……ふ……んくっ」 / MOAN "…Nku"
- ハチロクh3 963/1067 — んくっ → "Nku"/"Nku——" (supplement 22/11 ~11:00, lật "ưm"/"Ưm——")
- 日々姫h1 1003 — JP 「ふやっ！？ あっ――んくううううううううっ！！！」 / MOAN "Fuya!? A——Nkuuuuuuuuu!!!"
- lr真闇追加h 1097 — んくっ → "ưm ku" + く→"Ku" (dạng tách, xem dưới)

**んあ → "Na":**
- lr稀咲追加h 1162 — JP 「んあっ！？」 / TW 「嗯啊！？」 / MOAN "Na!?"
- 真闇h1 1090 — JP 「んあっっ！！？」 / TW 「嗯啊！！？」 / MOAN "Na!!?"
- lr真闇追加h 1103 — んあっ → "Na" (tiền lệ ハチロクh6 843 んぁ→"Na")
- XUNG ĐỘT: 日々姫h4 1075 — JP 「深っ――コレッ――んあっ！ 違うとこ――ぐりって！ ひぁっ――あっ――えぐれ――って――んきゅっっ！！」
  / MOAN "Sâu quá――Thế này――ưm a! … Nkyu!!" — cùng một dòng: んあっ → "ưm a!" nhưng んきゅっっ → "Nkyu!!"

**んふ → "Nfu" (vs "ưm phư"):**
- 日々姫h1 ×4 — んふ→"Nfu" (tiền lệ ハチロクh5 995, ハチロクh1 1219/1229, kisaki-h3 2207)
- XUNG ĐỘT: 真闇h1 1080 — JP 「ん……双ちゃん――あっ――太っ――――んふっ」 / TW 「嗯……小雙――啊――好粗――嗯唔」 / CSV3 "…ưm phư."
  (1 dòng duy nhất; file Mayami dùng "Phư" cho ふっ — xem quy tắc)

**んぇ → "Ne":** 日々姫h4 1035 — JP 「ん……むっ――んぇっ――」 / MOAN "Ưm……ưm――Ne――" (dạng mới duy nhất)

**Dạng tách "ưm/ưn + phụ âm" (file ハチロクh7/h8 — XUNG ĐỘT với romaji):**
- ハチロクh7 745 — JP 「…んっ――そ――ん、な、…んきゅうう！！？」 / MOAN "…ưm——…ưn kyuuu!!?" (んきゅうう → "ưn kyuuu")
- ハチロクh7 843 — JP 「んっきゅぅぅぅぅぅぅぅぅぅうっぅううううう！！」 / AUDIT "Ưn kyuuuuuuuuuuuuuuuuu!!"
- ハチロクh8 1561 — JP （んくっ！ ごくっ！ ごくっ！！ ごくんっ！！） / CSV3 "（Ưn ku! Ực! Ực!! Ực!!）"
- ハチロクh8 821/759 — んくっ → "ưn ku" (AUDIT)

**ん(っ) trần → "ưm":**
- 2.926 dòng JP có んっ; "ưm" đứng riêng 1.480 dòng vs "ưn" đứng riêng chỉ 8 dòng (trong đó 6 là dạng tách ở trên).
- Hai dòng trần → "ưn" duy nhất: 真闇h3 2323 (JP 「ん……や……ちくび――ンッ――くに、くに――…」 / AUDIT "…ưn――bóp, bóp――" — "ưn" render ンッ)
  và 真闇h3 2328 (JP 「ん……はっ――ん……双ちゃん……て……やらし……んっ――ねっとり、して、てっ」 / CSV3 "…ưn――dính, nhớp nháp, quá." — "ưn" render んっ).
  Cả hai đều là thoại thường (không phải rên H), cùng một file.

**んん → "nn"/"mm" (một chữ cái cho mỗi ん):**
- ふかみh3 2287 — JP 「ふきゅうううんんっ！！ …」 / MOAN "Fukyuuuunn!! …" (んん→"nn")
- ふかみh3 2289 — JP 「きゅふああああああああああああああんんっ！！！」 / MOAN "Kyufuaaaaaaaaaaaaaann!!!" (んん→"nn")
- れいなh3 1061 — JP 「んぶっ――むっ――んっ――んんっ――むっ――…」 / MOAN "…ưmm——…" (んん→"mm" trong từ "ưm")
- 真闇h3 2310 — JP 「ふああああああああんんんっっっっ」 / MOAN "Fuaaaaaaaannn" (んんん→"nnn" — đúng)
- ふかみh1 967 — JP 「ひゃああんんっ」 → "Hyaaann" (んん→"nn" — ĐÚNG; xem §0.10)
- Ngoại lệ giữ: ポーレットh4 878 — JP 「ひゃふっ――んっ――あっ――あひっ――ぅんっ！」 / CSV3 "…ưn!" (ぅんっ: ん đứng SAU nguyên âm ぅ → "ưn" = ư (ぅ) + n (ん) — đúng dạng nguyên âm+n, giữ)

### Đếm toàn dự án
- JP có ん+phụ âm: **573 dòng**. "Nkyu" 28 / "Nku" 13 / "Nfu" 8 / "Na" 5 / "Ne" 1 / "Nhyu" 1 / "Ưm" 215 (nhiễu — phần lớn là ん trần trong cùng dòng) / khác 247.
- JP có んっ: **2.926 dòng**. "ưm" 1.556 (đứng riêng 1.480) / "nn" 28 / "ưn" (đứng riêng) 8.

### QUY TẮC ĐỀ XUẤT — M15 (độ tin cậy: cao cho romaji ん+phụ âm, cao cho んっ→"ưm")
1. **ん + phụ âm trong rên H → romaji "N"+phụ âm: Nkyu / Nku / Na / Nfu / Ne / Nhyu** (giữ nguyên độ dài theo công thức tổng-Hepburn).
   Lý do: moan pass đã áp nhất quán ở nhiều file (28 Nkyu, 13 Nku…); một token = một rendering (quy tắc đã chốt);
   dạng tách "ưm ku" vi phạm tinh thần một-token-một-rendering và làm mất phụ âm đầu của ん.
2. **Sửa các xung đột:**
   - 日々姫h4 1075 んあっ "ưm a!" → **"Na!"** (cùng dòng đã có んきゅ→"Nkyu" — không nhất quán nội dòng).
   - 真闇h1 1080 んふっ "ưm phư" → **"Nfu"** (1 dòng duy nhất; quy ước "Phư" của file Mayami áp cho ふっ trần, không áp cho んふっ;
     tiền lệ Nfu có 4+ dòng ở 日々姫h1).
   - Dạng tách ハチロクh7/h8 → romaji: 745 "ưn kyuuu" → **"Nkyuuu"**, 843 "Ưn kyu…" → **"Nkyu…"**,
     1561/821/759 "ưn ku" → **"Nku"** (5 dòng).
   - lr真闇追加h 1097 んくっ "ưm ku" → **"Nku"** (theo quy tắc; token く sau đó vẫn "Ku" riêng — "Nku" đã chứa cả hai âm,
     không render く lần nữa).
   - lr_稀咲h1 1162 — JP 「…んうっ！」 / AUDIT "…ưn ư!" → **"Nu!"** (ん trước nguyên âm う → romaji "N"+nguyên âm, cùng quy tắc với んあ→"Na";
     giải quyết luôn cờ F5 của file này: "ん 'Ưn/ưn' trước nguyên âm" → romaji).
3. **ん(っ) trần → "ưm"** (1.480 vs 8). Sửa 2 dòng 真闇h3 2323/2328 "ưn" → **"ưm"**.
4. **んん(っ) → một chữ cái cho mỗi ん: "nn" trong từ romaji, "mm" trong từ "ưm"** (2287/2289 "nn", 1061 "mm", 2310 "nnn", 967 "nn" — đều đã đúng; không cần sửa).
   ポーレットh4 878 ぅんっ → "ưn" GIỮ (ん sau nguyên âm).
5. **Thoại phi-H:** ん(っ) trong thoại thường → "ưm" (đã là dạng chủ đạo); không đụng các dòng "ưm" phi-H.

**Số dòng ảnh hưởng:** ~11 dòng (1075, 1080, h7/h8 5 dòng, 1097, 真闇h3 2 dòng, lr_稀咲h1 1162).

---

## M19. じゅぶっ → "Chu mút" vs "Phập!"

### Câu hỏi
Hai dạng này phân biệt thế nào? (Lưu ý M72: không được phá tính đồng nhất của spurt-SFX ở 日々姫h2 F6.)

### Tiền lệ đã xác minh — 6 dòng ハチロクh3 (cùng một file, cả hai dạng)

| key | JP （ ） | TW （ ） | VN hiện tại | chuỗi |
|---|---|---|---|---|
| 1809 | （ぢゅぽっ！ じゅっ！ にゅくっ！ じゅぶっ！！） | （啾啵！啾！唔！啾！！） | CSV3 "（Chụt! Chụt! Ngoáy! Chu mút!!）" | toàn âm miệng (mút) |
| 1811 | （じゅぶっ！ じゅっ！ ぐりゅっ！ じゅぶっ！） | （啾噗！啾！唔溜！啾！） | CSV3 "（Phập! Chụt! Ngoáy! Phập!）" | có ぐりゅっ (xoáy/đâm) |
| 1794 | （ずっ！ じゅぶっ！ ずぼっ！ じゅぼっ！） | （呲！啾！啪！啾啵！） | MOAN "（Phập! Phập! Phập! Chu mút!）" | chuỗi đâm (ず/ずぼ); moan đổi token 2 "Sột sột"→"Phập!" nhưng GIỮ token 4 じゅぼっ→"Chu mút!" |
| 1807 | （ばちゅんっ！ じゅっ！ じゅぶっ！ じゅぱっ！） | （啪啾！啾！啾！啾啪！） | MOAN "（Phập! Chụt! Phập! Chụt!）" | mở đầu bằng ばちゅんっ (đâm); moan đổi じゅぶっ→"Phập!" |

**日々姫h4 (hệ romaji cho じゅ):**
- 1754 — JP （じゅぶっ！ じゅっっ！ じゅばっっ！ じゅぼっ！） / TW （啾噗！啾噗！噗啾！噗啾！） / MOAN "（Jubu! Ju!! Juba!! Jubo!）"
  (toàn âm miệng; file dùng romaji cho じゅ-SFX — tiền lệ romaji của file)
- 1759 — JP （ずばっ！ じゅぶっ！ ずぶっ！ すぱんっ！！） / TW （噗啾！噗啾！啾噗！啾噗！！） / MOAN "（Phập! Phập! Phập! Bạch!!）"
  (chuỗi đâm ずば/ずぶ/すぱん; moan đổi ずばっ "Bạch!"→"Phập!" và じゅぶっ→"Phập!")

**Ngày 1801 (M20, liên quan):** ハチロクh3 1801 ぶりゅん → "Phập!" GIỮ (vì "Phụt" sẽ đụng spurt-SFX trong file).

### Đếm toàn dự án
- Dòng JP chứa じゅぶっ: **154**. "Phập!" 58 / "Chụt" 24 / "Chu mút" 13 / khác 59.
- Phân loại chuỗi （ ） (phân loại máy, thô — TW không tách sạch được, xem dưới):

  | loại chuỗi | "Phập!" | "Chu mút" | "Chụt" | romaji "Jubu" | khác |
  |---|---|---|---|---|---|
  | có token đâm (ず/ずぼ/すぱ/ばちゅん/ぐりゅ) | 39 | 2 | 1 | 3 | 14 |
  | chỉ âm miệng (ぢゅぽ/にゅく/じゅぼ, không token đâm) | 1 | 2 | 1 | 1 | 1 |
  | chỉ じゅぶっ/じゅ (không token phân biệt) | 12 | 2 | 4 | 2 | 13 |
  | trộn đâm+miệng | 8 | 0 | 1 | 0 | 0 |

  → Tương quan chuỗi-vs-dạng **chỉ rõ trong ハチロクh3**, còn toàn dự án thì dạng chủ yếu là **quy ước file**:
  lr_ハチロクh2 → "Phập!" (chuỗi toàn "Phập! Phập! Phập! Phập!": 2187/2204/2207…),
  lr_れいなh1 → "Chu mút" (1870/1883…), 日々姫h4 → romaji "Jubu" (1754).
  TW không quyết được: 1794 token 2 (TW 啾) → "Phập!" nhưng 1809 token 4 (TW 啾) → "Chu mút" — cùng TW 啾, khác dạng.

### QUY TẮC ĐỀ XUẤT — M19 (độ tin cậy: trung bình-cao cho "giữ theo file", trung bình cho quy tắc chuỗi)
1. **Giữ theo file** (dạng chủ đạo của file đứng): lr_ハチロクh2 "Phập!", lr_れいなh1 "Chu mút", 日々姫h4 romaji "Jubu".
   Lý do: tương quan chuỗi không đứng vững toàn dự án (bảng trên); các file đã nhất quán nội bộ.
2. **Quy tắc chuỗi chỉ dùng làm tie-breaker trong file dùng CẢ HAI dạng (hiện chỉ có ハチロクh3 — và 6 dòng đó ĐÃ đúng quy tắc,
   không cần sửa):** chuỗi có token đâm (ず/ずぼ/すぱ/ばちゅん/ぐりゅ) → "Phập!"; chuỗi toàn âm miệng (ぢゅぽ/じゅ/にゅく/じゅぼ) → "Chu mút";
   file hệ romaji cho じゅ → "Jubu". 1794-token-4 là じゅぼっ (không phải じゅぶっ) → "Chu mút!" đúng vì bản thân token là âm miệng.
3. **Các dòng cần xem lại trong batch (chưa quyết — cần đọc JP+TW từng dòng):**
   lr_れいなh1 1896/1867 ("Chu mút" trong chuỗi phân loại "đâm" bằng máy),
   lr_ハチロクh3 1935 ("Phập!" trong chuỗi phân loại "miệng" bằng máy).
   Batch đọc tay 3 dòng này theo quy tắc chuỗi + dạng chủ đạo của file rồi quyết.
4. **M72 không bị ảnh hưởng:** spurt-SFX ("Phụt!") khác "Phập!" (đâm) — hai từ riêng biệt; 日々姫h2 F6 giữ spurt đồng nhất "Phụt!"
   (1764/1766/1771/1772) không liên quan đến じゅぶっ. Trong ハチロクh3, 1801 ぶりゅん → "Phập!" đã giữ để tránh đụng "Phụt" — giữ nguyên.

**Số dòng ảnh hưởng:** 0 dòng chắc chắn; 3 dòng xem lại (1896/1867/1935). "Xung đột" M19 thực chất đã tự giải khi tách theo file —
6 dòng ハチロクh3 đều nhất quán với quy tắc chuỗi.

---

## M68. れろ → romaji vs "liếm láp" (liên quan T77 "rộp"/"liếm")

### Câu hỏi
れろ ngắn vs dài phân biệt thế nào?

### Tiền lệ đã xác minh

**Dài → romaji (moan pass đổi):**
- 日々姫h4 1052 — JP 「んふふっ――れろおおおっ」 / TW 「嗯呼呼――啾噗」 / MOAN "Nfufu――Reroooo" (れろ+3お → 4 o tổng, đếm đúng)
- 真闇h3 2198 — JP 「ぺろっ――れろおおおっ――ぺろっ、ぺちゅっ。 チュルッ――ちゅっ――れろおおおおっ――れるっ」
  / TW 「呸嘍――呸嘍――呸囉、呸啾。啾嚕――啾――呸嘍――舔」
  / MOAN "Pero――reroooo――pero, pechu. Churu――chu――rerooooo――reru." (3お→4 o, 4お→5 o, đếm đúng; れるっ→"reru" theo hệ romaji của dòng)

**Ngắn → "liếm" (giữ):**
- 日々姫h4 1004 — JP 「はむっ――れろっ――ちゅっ、ちゅううっ――…」 / TW 「唔――啾噗――啾、啾――…」 / CSV3 "Ngoạm――liếm――chụt, chùn chụt――…"
- 日々姫h4 1029 — JP 「…あむっ――れろっ――ちゅくっ――…」 / MOAN "…ngoạm――liếm――Chụt――…"

**Dài → "liếm" + kéo chữ m (độ dài VẪN được diễn — không phải lỗi):**
- 凪h1 1772 — JP （にゅうううっ！ べろっ！ れろおおおっ！） / AUDIT "（Trườn! Liếm! Liếmmmm!）" (3お → 4 m tổng ✓)
- 凪ふかみh1 1317 — JP 「…れろおおおおおおおおっ！」 / CSV3 "…Liếmmmmmmmm!" (9お → 9 m tổng ✓)
- lr_凪ふかみh1 1633 — JP 「れろおおおおおおおおおおおおおおおおっ！！！！」 / CSV3 "Liếmmmmmmmmmmmmmmmm!!!!" (16お → 16 m ✓)
- lr_ニイロクh 2060 — JP （れろおおおおおっ） / CSV3 "（Liếmmmm）" (5お → 5 m ✓)
- lr追加_みくろ＆日々姫h 1704/1854 — れろおおお(お) → "liếmmmmm" (kéo m, lệch ±1)
- lr_れいなh1 1372 — れろ+16お → "liếm m×15" (kéo m)
- 凪ふかみh2 1030 — れろおおおお → "liếmmmmm" (4お → 5 m, lệch +1)

**Dài → "liếm (dài)" bằng từ (độ dài được diễn bằng từ, không kéo chữ):**
- ハチロクh7 1840 — JP （れろおおおおっっ） / CSV3 "（Liếm dài——）"
- ハチロクh7 1878 — JP （れろっ――れるっ――れろおおおお――はぷっ！） / AUDIT "（Liếm——liếm——liếm dài——ngoạm!）"

**Dài → MẤT độ dài / MẤT âm (lỗi thật):**
- ハチロクh8 841 — JP 「…れろおおおおおおっ！」 / CSV3 "…Liếm láp!!" (6お, không kéo)
- 日々姫h3 1857 — JP （れろおおおおおっっ） / CSV3 "（Liếm láp）" (5お, không kéo)
- れいなh2 1084 — JP 「…れろおおおっ！」 / CSV3 "…Chụt!" (token れろ BIẾN MẤT — cả dòng thành "Chụt! ×8")
- れいなh2 1114 — JP 「ひゃいれふぅ――んッ――れろおおおおおおっ――…」 / MOAN "…chụt——…" (token れろ bị moan fix bỏ hẳn)
- 凪h2 2546 — JP 「…れろおおおおっ」 / CSV3 "…Ngoáyyyyyy" (diễn nghĩa "ngoáy" + kéo y — phán đoán: giữ hay đổi, xem quy tắc)
- lr_日々姫ふかみh1 1461 — JP 「…れろおおおっ――…」 / CSV3 "…rê roooo――…" (dạng romaji viết cách "rê roooo" — đếm đúng 4 o; tính là hệ romaji)

**"rộp" (T77 — Hieu quyết, chưa chốt):** 14 dòng, vd lr_ポーレットh1 1065/1089/1203 → "rộp" cho れろ.
T77 vẫn mở (ハチロクh7 1878/1944 tạm "liếm"). M68 không quyết thay T77.

### Đếm toàn dự án
- Dòng JP chứa れろ: **220**. "liếm" 152 / romaji 29 / "rộp" 15 / khác 24.
- Dài (≥3 mora kéo dài): romaji 6 / "liếm" 6 / khác 11 (17 dòng đã liệt kê tay ở trên).
- Ngắn: "liếm" 111 / romaji 23 (nằm trong các dòng/hệ romaji — giữ theo file) / "rộp" 14 / khác 49.

### QUY TẮC ĐỀ XUẤT — M68 (độ tin cậy: cao cho ngắn, trung bình-cao cho dài)
1. **Ngắn れろ(っ) → "liếm"** (111 dòng; giữ nguyên; 23 dòng romaji ngắn nằm trong dòng/hệ romaji thì giữ theo file).
2. **Dài れろ (≥3 mora kéo dài) → romaji "Rero" + đếm nguyên âm** (1 + số お/ぉ: れろおおお→"Reroooo" 4 o).
   Lý do: moan pass đã đổi 1052/2198 sang romaji với đếm đúng; cùng họ với quyết định ひゃ-family (âm dài trong rên H → romaji);
   romaji là cách duy nhất diễn đúng cả âm lẫn độ dài mà không cần kéo chữ m.
3. **Phạm vi áp dụng (chia 2 nhóm — điều phối viên quyết nhóm 2):**
   - **Nhóm 1 — sửa ngay (lỗi thật, mất âm/độ dài):** ハチロクh8 841, 日々姫h3 1857, れいなh2 1084, れいなh2 1114 (4 dòng → romaji).
   - **Nhóm 2 — chỉ vì thống nhất (các dòng ĐÃ diễn đúng độ dài bằng kéo m hoặc từ "dài"):**
     凪h1 1772, 凪ふかみh1 1317, lr_凪ふかみh1 1633, lr_ニイロクh 2060, lr追加_みくろ＆日々姫h 1704/1854,
     lr_れいなh1 1372, 凪ふかみh2 1030, ハチロクh7 1840/1878 (~10 dòng).
     Đề xuất: **đổi sang romaji cho đồng nhất** (vì quy tắc đã chốt là romaji cho dài), nhưng ghi rõ đây là thay đổi thống nhất,
     không phải sửa lỗi — nếu điều phối viên muốn giảm xáo trộn thì giữ nhóm 2 nguyên.
   - 凪h2 2546 "Ngoáyyyyyy" — giữ hay đổi theo nhóm 2 (diễn nghĩa + kéo y, độ dài có).
   - lr_日々姫ふかみh1 1461 "rê roooo" — đã là romaji (chỉ khác cách viết có dấu/cách); chuẩn hóa thành "Reroooo" trong batch.
4. **"rộp" 14 dòng:** không đụng — chờ quyết T77 của Hieu.

**Số dòng ảnh hưởng:** 4 dòng chắc chắn + ~10 dòng thống nhất + 1 chuẩn hóa (1461).

---

## M70. Họ きゅ: ngắn → nghĩa vs dài → romaji (真闇h2 F6)

### Câu hỏi
Ngắn thì diễn nghĩa, dài thì romaji — ranh giới ở đâu, và có áp toàn dự án không?

### Tiền lệ đã xác minh

**Ngắn → nghĩa Việt:**
- 真闇h2 1846 — JP （きゅんっ――きゅううううっ） / TW （啾――壓） / MOAN "（Thắt lại――Kyuuuuu）"
  (token NGẮN きゅんっ → "Thắt lại"; token DÀI きゅううううっ → "Kyuuuuu" — cùng một dòng, hai cách xử lý)
- 真闇h2 1848 — JP （ふわっ――きゅうううううっ！） / TW （嗚哇――壓！） / MOAN "（Nhẹ bẫng――Kyuuuuuu!）" (dài → romaji)
- 真闇h2 986 — JP (thoại) きゅんきゅん (tim đập thình thịch, không phải SFX) → nghĩa Việt (giữ)
- 凪h1 1773 — JP （きゅんっ！ …） / CSV3 "（Siết! …）" — dạng khóa cho きゅん: "Thắt tim! Siết chặt!" (凪h1 1773, xem M14)

**Dài → romaji (moan pass đổi):**
- 真闇h2 1846/1848 (trên); ハチロクh3 1836 — JP （きゅううううううっ！！！） / TW （插入！！！） / MOAN "（Kyuuuuuuu!!!）" (7u đúng)
- 真闇h2 1820–1872 — loạt SFX dài → romaji (1832 くぱああ 3a → "Kupaaa" — ngưỡng 3; xem M14)

**Dài → nghĩa Việt (moan pass/audit GIỮ — đa số):**
- lr_日々姫h1 1797 — JP （きゅぅぅぅぅっぅぅぅぅぅぅぅぅぅぅぅんんっ！！） 15う / CSV3 "（Thắt chặt lạiiiiiiiiiiiiii!!）" (14 i — sai đếm, xem M14)
- 日々姫h2 1797 — JP （きゅううううっ！） 4う / CSV3 "（Siết chặtttt!）" (4 t — đếm đúng); 1798 — JP （きゅんっ――きゅうううんっ） / CSV3 "（Co thắt——Siết chặtttt）"
- 稀咲h2 1963 — JP （きゅううううっ！） 4う / CSV3 "（Siết chặt!）" (mất độ dài — xem M14)
- lr_日々姫h2 1659 — JP （きゅんっ！ きゅうううっ！ …） / CSV3 "（Siết! Siết chặt! …）" (mất độ dài — xem M14)

**Ngoại lệ/trộn trong một dòng (chưa từng được đụng):**
- 真闇h2 1842 — JP （きゅっ――くぽっっ――きゅぷっ――きゅうっ） / TW （啾――啪――啾唔――壓）
  / CSV3 "（Thắt lại――phập――kypu――kyuu）" — TRỘN trong một dòng: token 1 "Thắt lại" (nghĩa), token 3/4 romaji "kypu"/"kyuu"
  (きゅうっ chỉ có 1う — ngắn — nhưng lại romaji "kyuu"; không nhất quán với quy tắc ngắn→nghĩa)
- 真闇h2 1084 — JP (thoại) 「きゅっ！ ふっ――やっ――ぁっ――ぁあっ、んっ！」 / TW 「啾！ 呼――呀――啊――…」
  / CSV3 "Kyu! Phư――ya――a――aa, ưm!" — thoại きゅっ NGẮN nhưng romaji "Kyu!" (xung đột với ngắn→nghĩa nếu áp cho thoại)

### Đếm toàn dự án
- Dòng JP chứa きゅ: **636**. "Siết (chặt)" 160 / "Thắt (lại)" 45 / "Ky*" romaji 77 / khác 354.
- Ngắn: 485 dòng ("Siết" 89 / "Thắt" 25 / "Ky*" 55 / khác 316).
- Dài (≥3 mora kéo dài): 151 dòng ("Siết" 71 / "Thắt" 20 / "Ky*" 22 / khác 38).
- Riêng （ ） dài ở H-file: **nghĩa Việt 84 vs romaji 13 vs khác 10** — nghĩa Việt áp đảo.
  (Romaji 13 dòng tập trung ở 真闇h2, ハチロクh3, 日々姫h4 — các file hệ romaji.)

### QUY TẮC ĐỀ XUẤT — M70 (độ tin cậy: cao cho "không ép romaji toàn dự án", trung bình cho ngưỡng)
1. **KHÔNG ép dài→romaji toàn dự án.** Bằng chứng: （ ） dài ở H-file là nghĩa Việt 84 vs romaji 13 —
   moan pass chỉ đổi sang romaji ở 3–4 file hệ romaji, còn lại giữ nghĩa Việt có chủ ý.
   Ép romaji sẽ lật 84 dòng đã quyết.
2. **Quy tắc theo hệ của file (giống M14):**
   - File hệ romaji cho SFX (真闇h2, ハチロクh3, 日々姫h4, lr稀咲追加h): **ngắn (≤2 mora kéo dài) → nghĩa Việt** ("Siết"/"Thắt"/"Co thắt" theo file);
     **dài (≥3 mora kéo dài) → romaji** ("Kyu…" + đếm nguyên âm theo công thức tổng-Hepburn). Ngưỡng 3 lấy từ 真闇h2 1832 (くぱああ, 3a → romaji)
     và 1846/1848 (4–5u → romaji) vs 1846-token-1 (きゅんっ, 0 kéo dài → nghĩa).
   - File hệ động từ Việt: **giữ nghĩa Việt cả ngắn lẫn dài; sửa ĐẾM kéo theo M14** (vd 稀咲h2 1963 thêm kéo; lr_日々姫h1 1797 sửa 14 i → 16 i).
   - Thoại (không phải （ ）): きゅん/きゅんきゅん (tim/body) → nghĩa Việt (真闇h2 986); きゅっ thoại → xem từng dòng
     (真闇h2 1084 "Kyu!" là CSV3 chưa từng đụng — giữ nguyên, không ép về nghĩa; nó là tiếng gasp ngắn, romaji đọc được).
3. **Dòng cần xem lại:** 真闇h2 1842 "（Thắt lại――phập――kypu――kyuu）" — trộn trong một dòng của file hệ romaji.
   Theo quy tắc: token 1 きゅっ (ngắn) → "Thắt lại" ✓; token 3 きゅぷっ (ngắn) → romaji "kypu" ✗ (phải là nghĩa — nhưng きゅぷっ không có
   nghĩa Việt sẵn trong file: các token くぽっっ → "phập" là nghĩa; きゅぷっ → ?); token 4 きゅうっ (1う — ngắn) → "kyuu" ✗ (phải là nghĩa).
   Batch đọc tay cả dòng 1842 và quyết theo hệ file (khả năng: token 3/4 → nghĩa Việt "Thắt lại"/"phập"-tương đương, hoặc giữ romaji
   nếu file không có nghĩa Việt cho きゅぷっ/きゅうっ — chưa quyết, ghi là "xem lại").

**Số dòng ảnh hưởng:** 0 dòng chắc chắn (quy tắc xác nhận giá trị hiện tại ở cả hai hệ);
1 dòng xem lại (真闇h2 1842); các fix đếm thuộc M14 (vd 1963, 1797).

---

## Bảng tổng kết

| Mục | Quy tắc đề xuất | Độ tin cậy | Dòng ảnh hưởng (ước) |
|---|---|---|---|
| M7 くっ | Thoại H-scene → "Ku" (h6 §3c: "Hự" mất phụ âm k); giữ "Hự" ở 4 file quy ước (lr_ふかみh2, 日々姫h1, lrれいな追加h, ハチロクh2); 5 dòng "Hự" đơn lẻ → "Ku"; miêu tả （ ） → "Ư"; thoại phi-H giữ "Ư"; giữ "kư" (lr_稀咲h1) và cụm động từ "Ngoáy"/"Thúc" | Cao (thoại) / Trung bình-cao (miêu tả) | ≥50 dòng "Ư" (moan-giữ) + dòng H-file chưa xem + 5 dòng "Hự" đơn lẻ; không đụng 12 dòng "Hự" quy ước và phi-H |
| M8 や/やっ | Token kề sau là câu từ/từ chối → "Á"; token trong chuỗi rên (kề token âm) → "Ya/Yaa"; diễn nghĩa giữ nghĩa; bỏ "A" trần cho や | Cao | 64 dòng "A" trần + 1 viết hoa (1203); 991/1334 giữ nguyên |
| M9 ふっ | KHÔNG thống nhất toàn dự án — giữ theo file; chỉ thống nhất nội bộ file (真闇h3 "phù"→"Phư"; các file trộn theo đa số) | Cao (giữ theo file) / Trung bình (fix lẻ) | ~3–6 dòng |
| M10 ふぇ/ふえ | Chuỗi rên → "Fue"; thán từ ngạc nhiên độc lập (TW 哎/咦) → "Hể?"; dạng kéo dài → giữ "Phuê…"; reina-h3 1133 giữ "Hả?" | Cao (chuỗi) / Trung bình-cao (thán từ) / Trung bình (1133) | 6 dòng → "Hể?" (1090, 993, 1026, 1897, 992 + xem lại); 1133 giữ; 3 dòng dài giữ |
| M11 ふや | H-scene → romaji "Fuya" (ふやん→"Fuyan"); thoại phi-H giữ "phuya" theo quy tắc fa/fu đã chốt | Trung bình-cao | ~16 dòng (lật giá trị audit-lock — cần điều phối viên xác nhận lại) |
| M14 SFX （ ） | Giữ hệ từng file (romaji vs động từ Việt); thống nhất CÁCH ĐẾM: tổng chữ kéo = 1 + số う/ぅ/ー; sửa đếm sai + sửa loại chữ kéo (1679/1681); thêm kéo cho dòng mất độ dài | Cao (giữ hệ + công thức đếm) | ~122 dòng H-file mất kéo (rà từng dòng) + ~20 dòng đếm sai đã liệt kê — batch lớn nhất |
| M15 ん+phụ âm | ん+phụ âm rên H → romaji Nkyu/Nku/Na/Nfu/Ne/Nhyu; ん(っ) trần → "ưm"; んん → "nn"/"mm" (1 chữ/1 ん); sửa dạng tách "ưn ku" và 2 dòng 真闇h3 "ưn" | Cao | ~11 dòng (gồm lr_稀咲h1 1162 → "Nu!") |
| M19 じゅぶっ | Giữ theo file; quy tắc chuỗi (đâm→"Phập!", miệng→"Chu mút", hệ romaji→"Jubu") chỉ làm tie-breaker trong file dùng cả hai dạng; 6 dòng ハチロクh3 đã đúng, không sửa | Trung bình-cao (giữ theo file) / Trung bình (quy tắc chuỗi) | 0 dòng chắc chắn; 3 dòng xem lại (lr_れいなh1 1896/1867, lr_ハチロクh3 1935) |
| M68 れろ | Ngắn → "liếm"; dài (≥3) → romaji "Rero…" (nhóm 1: 4 dòng mất âm/độ dài sửa ngay; nhóm 2: ~10 dòng đã diễn đúng độ dài — chỉ đổi nếu muốn đồng nhất); "rộp" chờ T77 | Cao (ngắn) / Trung bình-cao (dài) | 4 + ~10 + 1 chuẩn hóa (1461) |
| M70 きゅ | KHÔNG ép dài→romaji toàn dự án; theo hệ file: file romaji thì ngắn→nghĩa, dài (≥3)→romaji; file động từ thì giữ nghĩa + sửa đếm (M14); thoại きゅん→nghĩa | Cao (không ép) / Trung bình (ngưỡng 3) | 0 dòng chắc chắn; 1 dòng xem lại (真闇h2 1842) |

## Phụ lục: ghi chú cho điều phối viên

1. **Các mục cần xác nhận lại trước khi áp (vì lật giá trị đã quyết có chủ ý):**
   - M11 (~16 dòng): lật audit-lock "Phuya" → "Fuya". Lý do lật: moan pass + romaji fallback là quyết định sau, chuyên về rên H.
   - M10 992 (lr_稀咲h1): lật moan fix "Fue!?" → "Hể!?". Lý do: ngữ cảnh dòng là câu phủ nhận (giống 1091), không phải chuỗi rên (khác 991).
   - M68 nhóm 2 (~10 dòng): chỉ vì thống nhất, không phải sửa lỗi.
2. **Các mục batch phải đếm/căn bằng máy, không làm tay:** M14 (đếm kéo từng token), M7 (căn token くっ từng dòng — con số 280 bị nhiễu),
   M15 (căn token ん+phụ âm).
3. **Sửa trong UNIFICATION-LIST.md:** 14 điểm §0 (sai file, sai key, tiền lệ 2187 tồn tại, cờ F1 lr_ニイロクh copy sai, số "33 dòng ưn" bị nhiễu…).
4. **File audit-obasan-wrong.json:** 255 mục không có fix — cần một đợt audit riêng hoặc xác nhận các dòng đó đã được fix ở đâu khác.
5. **Engine chứng cứ** (dùng cho đợt điều tra sau, đã lưu bền — không để /tmp nữa):
   `~/workspace/maitetsu-pilot/unification/f1_engine.py` — đếm lại khớp: CSV3 91.731 / good-set 87.833; moan 1.516; audit 9.239.
   (Lưu ý: `audit-lr-nagih2-wrong.json` lưu fix dạng chuỗi trần, không phải dict — engine đã xử lý; 1 mục unmatched còn lại:
   `audit-nagifukami07-bunki-sentakushi-wrong.json` key 86.)
6. Không có fix JSON nào được viết; không file audit/moan nào bị sửa; không gì được gửi cho Hieu.
