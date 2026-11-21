# Audit — 日々姫11_御一夜モザイク.txt.toml (02_Hibiki)

- File: `sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59eb11_#U5fa1#U4e00#U591c#U30e2#U30b6#U30a4#U30af.txt.toml`
- Route 02_Hibiki, 412 dòng script, 1 bản sao duy nhất (không có file trùng).
- TOML md5: `7c44326eff735310fe21b8079a57ddfe` (UTF-8 BOM + CRLF).
- CSV3: 1 set duy nhất, 412 dòng, khớp khóa 1–1 với TOML (0 khóa chỉ-có-CSV, 0 khóa chỉ-có-TOML), 0 VN trống, 0 VN==TW (không có dòng chưa dịch).
- Phương pháp: đọc từng dòng đối chiếu JP + TW (CSV3), kiểm tra sweep gasp trực tiếp, quét máy toàn bộ dòng JP chứa っ, rà đại từ Soutetsu/Hibiki toàn file.
- Kết quả: **412 dòng đã đọc, 6 dòng sai (1,5%)**.
- Phân loại: đại từ/xưng hô 3 (1921, 2215, 2480), gasp 2 (1907, 1952), SFX 1 (1874).
- 0 lệch hàng / 0 chuỗi xoay (rotation) / 0 nhiễm chéo file khác / 0 dòng mồ côi / 0 dòng chưa dịch / 0 khóa trùng.
- Lượt soát 2 (đọc lại toàn bộ 6 giá trị sửa đối chiếu JP): **6 tổng / 6 xác minh lại / 0 bỏ / 1 sửa** (1921: lúc soát 2 đã thu hẹp giá trị sửa — chỉ đổi "chị"→"em", giữ "người khác" vì TW 「讓別人來幫你」 đồng ý; không đổi thành "anh").

## §1. Các dòng sai (6)

### 1. Key 1874 — SFX — 日々姫
- JP: 「えっ！？　あっ――あうっ――えっ！？」
- TW: 「哎！？啊……唔……哎！？」
- Cũ: 「Hả!? A——Á——Hả!?」
- Mới: 「Hả!? A——Aư——Hả!?」
- Lý do: あうっ có 2 mora (a+u); công thức nguyên âm = 1 + số う/ぅ = 2 nguyên âm → "Aư" (tiền lệ あうっ→"Aư" trong ROUTE-AUDIT.md); "Á" làm mất mora う. Dấu —— sau đó diễn vết cắt của っ nên không thêm Ư.

### 2. Key 1907 — gasp — 日々姫
- JP: 「ん……はっ……はうっ」
- TW: 「嗯……嘿……」
- Cũ: 「Ưm……ha……hấu」
- Mới: 「Ưm……ha……hấuƯ」
- Lý do: はうっ ở cuối dòng tuyệt đối, không dấu câu sau — っ mất hoàn toàn. Quy tắc gasp đã khóa nêu đích danh はうっ là gasp phải thêm Ư (tiền lệ はうっ→"HauƯ", parent giữ 21/11). はっ giữa dòng → "ha" giữ theo quy ước toàn dự án (như あっ→"A").

### 3. Key 1921 — đại từ — 双鉄
- JP: 「うむ。たまには甘えてくれ」
- TW: 「嗯。有時也該讓別人來幫你」
- Cũ: 「Ừm. Thỉnh thoảng chị cũng nên dựa dẫm vào người khác đi.」
- Mới: 「Ừm. Thỉnh thoảng em cũng nên dựa dẫm vào người khác đi.」
- Lý do: người nghe là Hibiki, không phải Mayami. Thứ tự trong file: 1917 Soutetsu→Hibiki, 1918 Soutetsu→Hibiki ("Đừng bận tâm đến anh, em cứ tiếp tục đi"), [1921], 1923 Hibiki ("anh lật người lại"), 1925 Soutetsu→Hibiki ("Nhờ em vậy") — toàn bộ nhịp massage là Soutetsu↔Hibiki; Mayami không có dòng nào trong nhịp này (dòng gần nhất 1859, rồi 1981). Soutetsu với Hibiki → "em" theo quy tắc đã sửa. "Người khác" giữ nguyên (TW đồng ý).

### 4. Key 1952 — gasp (sweep) — 双鉄
- JP: 「ああ。\n――っ！！？」
- TW: 「好——！！？」
- Cũ: 「Ừ.\n——!!?」
- Mới: 「Ừ.\n——Ư!!?」
- Lý do: sweep `lost-gasp-trailing` — gasp cuối dòng sau dấu —— bị mất; nhận đúng giá trị sweep.

### 5. Key 2215 — đại từ — ポーレット
- JP: 「お待たせしましたー！　って、あれ？\n双鉄くんと凪ちゃんとふかみちゃんは？」
- TW: 「讓大家久等啦！哎？雙鐵君、小凪和小深呢？」
- Cũ: 「Để mọi người đợi lâu rồi! Ơ kìa?\nSou-chan, Nagi-chan và Fukami-chan đâu rồi?」
- Mới: 「Để mọi người đợi lâu rồi! Ơ kìa?\nAnh Soutetsu, Nagi-chan và Fukami-chan đâu rồi?」
- Lý do: khóa B4 — 双鉄くん của Paulette → "anh Soutetsu" (tiền lệ 4 fix đã parent kiểm chứng: 1730/2140/2220/2373). "Sou-chan" là dạng của Minokasa/Mayami, không phải của Paulette.

### 6. Key 2480 — đại từ — monologue
- JP: 「肉体的な疲労はともかく、\n精神・頭脳を僕らの誰より激しく使っている筈だ。」
- TW: 「先不說身體上的疲勞，她在精神和腦力方面的消耗比我們都大。」
- Cũ: `Bỏ qua sự mệt mỏi về thể xác,\nchắc chắn chị ấy đang phải vận dụng tinh thần và trí não căng thẳng hơn bất kỳ ai trong chúng tôi.`
- Mới: `Bỏ qua sự mệt mỏi về thể xác,\nchắc chắn em ấy đang phải vận dụng tinh thần và trí não căng thẳng hơn bất kỳ ai trong chúng tôi.`
- Lý do: độc thoại của Soutetsu, chủ ngữ là Hibiki (tiếp 2479 về khả năng lãnh đạo của Hibiki; TW dùng 她 = cô ấy, chỉ Hibiki). Soutetsu nhắc Hibiki ngôi thứ ba là "em ấy" (đối chiếu 2528 "em ấy cũng đang mong muốn"); "chị ấy" sai.

## §2. Sweep gasp kiểm chứng
- `sweep-raw-gasp-wrong.json` có 2 mục cho file này: 1952 `lost-gasp-trailing` — nhận (xem §1.4); 2321 `already-rendered` (「っ！」→"A!") — đúng, không sửa.
- Quét máy bổ sung toàn bộ dòng JP chứa っ: không còn gasp nào sweep bỏ sót. Các trường hợp giữ nguyên có lý do: 1466 「///////っ！！！」→"///////!!!" (dấu !!! diễn vết cắt); 1875 ひゃっ→"Hya"; 1887 んんっ→"ưm"; 1897 あっ→"A"; 1941 おうっ→"Oái!?"; 1964 よしっ→"Tốt!"; 1976 っんっ→"ưm"; 2156 よっ→"nhá"; 2321 đã nêu; SFX hành động 3036–3050 (どんっ/ぐいっ/ふみっ…) đã diễn thành động từ.
- Không còn っ thô trong VN.

## §3. Đại từ đã rà toàn file
- Soutetsu "anh/em" chỉ với Hibiki (1761, 1914, 1917, 1918, 1953, 1976, 2010, 2016, 2019, 2072, 2089, 2160, 2169, 2201, 2254, 2273, 2291); "cháu" chỉ với ông Minokasa (1477, 1753, 1759, 1772, 1778, 1948, 1962, 1994, 1998, 2029, 2035, 2070, 2081→"em ấy" về Hibiki, 2095, 2115, 2126, 2136, 2143, 2213, 2320); "tôi" chỉ ở 2050 (nói với đám đông, dạng trung lập) và trong độc thoại.
- Hibiki "em"/"anh trai" với Soutetsu đúng toàn file; "chị" chỉ ở 2125 ("chị Paulette", đúng) và 2307 (TW xác nhận 阿姐 = Mayami, đúng) — ngoài 2038 chờ Hieu (xem §5).
- Paulette tự xưng "em" đúng (1864, 2113, 2173); Mayami tự xưng "chị" đúng (1859, 1981); Hachiroku "Tôi" trang trọng đúng (2032); Minokasa "lão"/"Sou-chan" đúng.
- 3041 độc thoại nội tâm Soutetsu dùng "mình" là ĐÚNG (ngoại lệ "mình" cho tự vấn nội tâm đầy cảm xúc: "Mình……đang muốn kết hợp với Hibiki sao.").
- Câu JP cụt giữ nguyên dạng cụt: 2443, 2531, 2968 (JP thắng TW — TW thêm nội dung ở 2531 nhưng VN theo JP, đúng).

## §4. Thuật ngữ — chờ đợt thống nhất (không sửa trong audit)
- "Ohimitera" 12 dòng (JP 御一夜): 1480, 1989, 1996, 2095, 2136, 2143, 2260, 2464, 2483, 2531, 2804, 3032.
- "Denshahime" 2 dòng: 2018 (JP 電車姫様) và 1774 (JP 毛利の姫 — VN diễn giải thành "Denshahime của Mouri"; cùng một nhân vật, để đợt thống nhất đổi → "Công chúa Tàu điện").
- "Yên Hinamoto" 1 dòng: 2498 (JP 日ノ本) — đúng như hàng chờ đợt thống nhất của file này, KHÔNG sửa ở đây.
- "tuyến Yui" 1 dòng: 2095 (JP 湯医線) → đợt thống nhất "tuyến Yunoi".
- Gloss 帝鉄 "Đường sắt Hoàng gia" 1 dòng: 2141 — dạng đầy đủ đã chốt là "Đường sắt Đế quốc" (chỉ trong tooltip %l lần đầu), để đợt thống nhất.
- Các gloss đúng đã giữ: 列車 "đoàn tàu" (1823, 2115, 2136); エアクラ "Aircra" (2464); まいてつ "chủ tàu" (2853); 宮司 "Đền chủ Akai" (2263).

## §5. Chờ Hieu (giữ nguyên, không tự quyết)
- **2038** — Hibiki 「なら！　期待しちゃっていいと思うよ？」 → "Vậy thì! Chị cứ kỳ vọng đi!": người nghe chưa xác định. Lân cận trong file là cảnh Soutetsu/Minokasa/Hachiroku (2035, 2039 Soutetsu→Minokasa; 2042, 2045 Minokasa); "chị" có thể là Mayami hoặc Paulette, TW 「我覺得你可以期待一下」 không phân biệt được. Giữ nguyên "chị".
- Đợt thống nhất §4 (đặc biệt 2498 "Hinamoto" đã có trong hàng chờ).
- B19 vẫn park (không liên quan file này; không có thẻ %l lỗi trong file — đếm thẻ JP/VN khớp toàn file, 0 thẻ VN thiếu dấu `;`).

## §6. Khối TOML (đã kiểm chứng parse)
- JSON: `audit-hibiki11-ohitoyo-mosaic-wrong.json` — 6 mục, key dạng chuỗi, list-of-dicts.
- Khối TOML dưới đây parse được bằng tomllib: 6 khóa, 0 sai lệch giá trị so với JSON; jp/tw/old_vn khớp CSV3 tuyệt đối 6/6.

```toml
"1874" = "「Hả!? A——Aư——Hả!?」"
"1907" = "「Ưm……ha……hấuƯ」"
"1921" = "「Ừm. Thỉnh thoảng em cũng nên dựa dẫm vào người khác đi.」"
"1952" = "「Ừ.\\n——Ư!!?」"
"2215" = "「Để mọi người đợi lâu rồi! Ơ kìa?\\nAnh Soutetsu, Nagi-chan và Fukami-chan đâu rồi?」"
"2480" = "Bỏ qua sự mệt mỏi về thể xác,\\nchắc chắn em ấy đang phải vận dụng tinh thần và trí não căng thẳng hơn bất kỳ ai trong chúng tôi."
```

## Kết bài
File 日々姫11_御一夜モザイク: 412 dòng đã đọc, **6 dòng sai (1,5%)** — đại từ 3, gasp 2, SFX 1; không có lệch hàng, xoay, nhiễm chéo, mồ côi, chưa dịch hay khóa trùng. Lượt soát 2: 6/6 xác minh lại, 0 bỏ, 1 giá trị sửa đã chỉnh (1921). Cờ cho Hieu: 2038 "chị" chưa xác định người nghe; đợt thống nhất: "Ohimitera" ×12, "Denshahime" ×2, "Hinamoto" 2498, "tuyến Yui" 2095, gloss 帝鉄 "Đường sắt Hoàng gia" 2141.
