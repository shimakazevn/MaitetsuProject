# Unification U2c — §1 T1/T2 "Ohito" leftovers (folders 00–05): 5 dòng, 4 file

Đợt U2c: mục §1 T1 (DECIDED 19/11, Hieu) + T2 (DECIDED 21/11 ~17:30, Muse theo uỷ quyền) — các dòng còn sót dạng cũ "Ohito" / "Đường sắt Ohito" trong 6 folder 00/01/02/03/04/05 SAU khi các đợt U1a/U1b/U1c/U2a đã gộp. **5 dòng sửa, 4 file** (Hachiroku 3, Hibiki 1, Mayami 1; Common 0, Paulette 0, Reina 0). Cả 5 đều là T2 ("Đường sắt Ohito" → "Đường sắt Ohitoyo"); 0 dòng T1 trần, 0 dòng T1+T2.

## §0. Phạm vi

- 5 dòng đã biết từ trước (đã kiểm chứng từng dòng, không giả định): ハチロク01 2467, ハチロク12 1900/2089, 日々姫08 3719, 真闇h3 2524 — cả 5 đều có mặt trong đợt này, và không có dòng nào khác.
- Các dòng này chứa CẢ "Ohimitera" lẫn "Ohito": đợt U2a đã loại các dòng chứa "Ohimitera" (thuộc batch U1), còn các đợt U1 chỉ sửa phần "Ohimitera" → sau U1, mỗi dòng còn đúng 1 lần "Đường sắt Ohito" chưa sửa.

## §1. Phương pháp

1. **CSV3 good set (87.833 dòng):** đọc toàn bộ `sources/csv3/Matetsu Last Run - Trang tính 3.csv`, loại 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`. Đếm trong 6 folder 00–05: 64.840 dòng good-set.
2. **Map giá trị hiện tại** (xây bằng máy, đối chiếu chéo): moan wrong.json (66 file, 1.535 mục) + audit wrong.json (217 file: 9.147 mục dạng list ghép bằng (key, JP) + 52 mục dạng dict của `audit-00common14-wrong.json`, ghép bằng (file, key) = 共通14_負債) + các unification wrong.json ĐÃ GỘP (U1a/U1b/U1c/U2a/S6 = 479 khoá, 0 khoá trùng nhau). File `audit-obasan-wrong.json` (dạng cũ, không có fix) đã bị thay thế bởi `audit-paulette03-obasan-wrong.json` (256 mục, có fix) nên KHÔNG dùng — 4 dòng Ohito của file cũ (1150/1922/2339/2430) đều đã có fix mới trong map và không còn "Ohito".
3. **Thứ tự ưu tiên giá trị hiện tại — HIỆU CHỈNH so với thứ tự ghi trong task (moan > audit > unification):** giá trị hiện tại đúng phải là **unification (đã gộp) > moan > audit > CSV3**, vì theo QUY TẮC REBUILD trong `ROUTE-UNIFICATION.md` (22/11 ~11:20), rebuild áp dụng các fix list theo THỨ TỰ GỘP — batch sau ghi đè batch trước trên cùng (file, key) — và vì chính các batch U1/U2a đã lấy old_vn = giá trị audit/moan làm cơ sở. Bằng chứng trực tiếp: ハチロク12 2565 — U2a ghi old_vn = giá trị audit ("…văn hóa của Đường sắt Ohito…", đã bỏ gloss %l và dẹp `\n`) và fix = "…Đường sắt Ohitoyo…"; nếu dùng thứ tự moan > audit > unification thì dòng này (và ポーレット03 1750, cùng mẫu) sẽ bị tính là "còn Ohito" dù U2a đã sửa xong. Áp thứ tự task sẽ cho 14 ứng viên; áp thứ tự đúng (unification trước) chỉ còn đúng 5 dòng — chính là 5 dòng đã biết. 9 dòng chênh lệch đều đã sửa xong trong U2a (xem §4, đã kiểm chứng từng dòng bằng tra cứu trực tiếp, không qua map).
4. **Quét toàn bộ 6 folder:** regex `Ohito(?!yo)` trên giá trị hiện tại (không bắt "Ohitoyo" đã đúng). CSV3 VN có dạng "Ohito" trần trong 253 dòng ở 00–05; phân bổ giá trị hiện tại: 140 dòng qua unification, 113 dòng qua audit, 0 dòng qua moan, 0 dòng còn nguyên CSV3. Trong 253 dòng: 248 dòng đã đúng "Ohitoyo" ở giá trị hiện tại, chỉ 5 dòng còn sót (cả 5 đều qua unification U1a/U1b).
5. **Đọc từng dòng ứng viên:** JP (+TW) của cả 5 dòng đã đọc hết (xem §2). Dạng JP: 御一夜鉄道 5/5. TW đồng ý 5/5 (御一夜鐵路/御一夜鐵道). 0 dòng flag misalignment. 0 lần "Ohito" nằm trong gloss %l (kiểm tra bằng máy trên cả 5 dòng). Không đụng dòng gasp Ư hay dòng "Kh" nào (cả 5 đều là dòng thuật ngữ thường; fix chỉ thay đúng chuỗi mục tiêu).
6. **Fix = chỉ thay thế đúng chuỗi mục tiêu**, giữ nguyên toàn bộ phần còn lại (kể cả "(Yui)" ở 日々姫08 3719 — thuộc mục T7, không đụng; kể cả phần "Ohitoyo" đã sửa trong U1). Thứ tự: "Đường sắt Ohito" → "Đường sắt Ohitoyo" trước, rồi "Ohito" trần còn lại → "Ohitoyo" (không dòng nào còn dạng trần sau bước 1).
7. **Kiểm chứng chéo với TOML-2 (227 file, decode utf-8-sig + #U):** cả 5 dòng đều có mặt; TOML-2 lưu giá trị GỐC (còn "Ohimitera", `\n` dẹp thành khoảng trắng) nên so sánh sau khi quy đổi: flat(TOML) với Ohimitera→Ohitoyo == flat(old_vn) — 5/5 khớp sau khi gộp khoảng trắng (2 dòng ハチロク12 1900/2089 chỉ lệch 1 khoảng trắng kép do `\n` sau dấu phẩy bị dẹp — artifact đã biết, U2a cũng ghi nhận). Kiểm tra ngược: fix với "Đường sắt Ohitoyo"→"Đường sắt Ohito" == old_vn — 5/5.

## §2. Quyết định trong batch (theo uỷ quyền của Hieu — điều tra JP+TW rồi quyết, không park)

- **Không có quyết định OPEN nào trong batch.** T1/T2 đều DECIDED; cả 5 ứng viên đều có JP xác nhận trực tiếp (御一夜鉄道), không qua dạng viết tắt/kana.
- **Ranh giới T7:** 日々姫08 3719 có "(Yui)" — JP là （湯医）, tức tuyến Yunoi — thuộc mục T7 ("Yui"→"Yunoi"), KHÔNG sửa trong đợt này; chỉ sửa "Đường sắt Ohito".

## 01_Hachiroku — `ハチロク01_こんにちわ赤ちゃん.txt.toml` (1 dòng)

### key 2467 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道にとって初の廃線復線――御一夜-[はやと,1]早戸間の\\n扱いに関して、最終的に残った案は[ふたあん,1]二案でした」
- TW: 「御一夜鐵路恢復的第一條廢線——御一夜至隼人段的運營方案，在探討後最終留下了兩種選擇」
- old_vn (U1a (unification-t1-ohimitera-00-02) fix — giá trị hiện tại): 「Việc khôi phục tuyến đường sắt bị bãi bỏ đầu tiên của Đường sắt Ohito——Về cách xử lý đoạn Ohitoyo-Hayato,\\ncuối cùng có hai phương án được giữ lại.」
- fix: 「Việc khôi phục tuyến đường sắt bị bãi bỏ đầu tiên của Đường sắt Ohitoyo——Về cách xử lý đoạn Ohitoyo-Hayato,\\ncuối cùng có hai phương án được giữ lại.」
- Lý do: JP chứa 御一夜鉄道, TW đồng ý (御一夜鐵路); VN hiện tại còn dạng cũ "Đường sắt Ohito" → đổi thành "Đường sắt Ohitoyo" theo T2. Phần "Ohitoyo" còn lại trong dòng đã sửa đúng trong U1a, không đụng.

## 01_Hachiroku — `ハチロク12_ムナカタ来訪.txt.toml` (2 dòng)

### key 1900 — item T2 (JP: 御一夜鉄道)

- JP: 「確かに。ので御一夜市、御一夜鉄道とヴィジョンを\\n共有し、シナジーある展開をと考えている最中です」
- TW: 「您所言不虛，所以此次我行計劃與御一夜市以及御一夜鐵路共同展望前景，通力合作以起到相互促進的作用」
- old_vn (U1a (unification-t1-ohimitera-00-02) fix — giá trị hiện tại): 「Đúng là vậy. Vì thế chúng tôi đang trong quá trình chia sẻ tầm nhìn với thành phố Ohitoyo, \\nvà Đường sắt Ohito, để cùng nhau phát triển tạo ra sức mạnh tổng hợp.」
- fix: 「Đúng là vậy. Vì thế chúng tôi đang trong quá trình chia sẻ tầm nhìn với thành phố Ohitoyo, \\nvà Đường sắt Ohitoyo, để cùng nhau phát triển tạo ra sức mạnh tổng hợp.」
- Lý do: JP chứa 御一夜鉄道, TW đồng ý (御一夜鐵路); VN hiện tại còn dạng cũ "Đường sắt Ohito" → đổi thành "Đường sắt Ohitoyo" theo T2. Phần "Ohitoyo" còn lại trong dòng đã sửa đúng trong U1a, không đụng.

### key 2089 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道自身も、将来的な延伸を計画してます。\\n最優先は、御一夜－八ツ城の川線の復線。それから」
- TW: 「而我們御一夜鐵路也計劃於未來進一步延伸，首先是恢復御一夜至八代的河岸線路，然後再……」
- old_vn (U1a (unification-t1-ohimitera-00-02) fix — giá trị hiện tại): 「Bản thân Đường sắt Ohito cũng đang lên kế hoạch mở rộng trong tương lai. \\nƯu tiên hàng đầu là khôi phục Tuyến sông Ohitoyo - Yatsushiro. Sau đó」
- fix: 「Bản thân Đường sắt Ohitoyo cũng đang lên kế hoạch mở rộng trong tương lai. \\nƯu tiên hàng đầu là khôi phục Tuyến sông Ohitoyo - Yatsushiro. Sau đó」
- Lý do: JP chứa 御一夜鉄道, TW đồng ý (御一夜鐵路); VN hiện tại còn dạng cũ "Đường sắt Ohito" → đổi thành "Đường sắt Ohitoyo" theo T2. Phần "Ohitoyo" còn lại trong dòng đã sửa đúng trong U1a, không đụng.

## 02_Hibiki — `日々姫08_とれいん食堂.txt.toml` (1 dòng)

### key 3719 — item T2 (JP: 御一夜鉄道)

- JP: （湯医）-御一夜-早戸間が御一夜鉄道。\\n早戸-鹿兒島-千内-八ツ城-隈元までがみかん鉄道。
- TW: （湯醫）—御一夜—隼人段是御一夜鐵路。隼人—鹿兒島—川內—八代—隈元段是橙鐵路。
- old_vn (U1a (unification-t1-ohimitera-00-02) fix — giá trị hiện tại): Đoạn (Yui) - Ohitoyo - Hayato là của Đường sắt Ohito.\\nTừ Hayato - Kagoshima - Sendai - Yatsushiro - Kumamoto là của Đường sắt Mikan.
- fix: Đoạn (Yui) - Ohitoyo - Hayato là của Đường sắt Ohitoyo.\\nTừ Hayato - Kagoshima - Sendai - Yatsushiro - Kumamoto là của Đường sắt Mikan.
- Lý do: JP chứa 御一夜鉄道, TW đồng ý (御一夜鐵路); VN hiện tại còn dạng cũ "Đường sắt Ohito" → đổi thành "Đường sắt Ohitoyo" theo T2. Phần "Ohitoyo" còn lại trong dòng đã sửa đúng trong U1a, không đụng.

## 05_Mayami — `真闇h3_補習授業の廃校舎.txt.toml` (1 dòng)

### key 2524 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜市と御一夜鉄道とのさらなる発展に繋がる\\n可能性のあることだからな。無論、快諾した」
- TW: 「御一夜市和御一夜鐵道都可能因此有進一步的發展，所以我答應了」
- old_vn (U1b (unification-t1-ohimitera-03-06) fix — giá trị hiện tại): 「Bởi vì chuyện này có khả năng dẫn đến sự phát triển xa hơn nữa của thành phố Ohitoyo và Đường sắt Ohito mà.\\nTất nhiên là tôi đã vui vẻ nhận lời.」
- fix: 「Bởi vì chuyện này có khả năng dẫn đến sự phát triển xa hơn nữa của thành phố Ohitoyo và Đường sắt Ohitoyo mà.\\nTất nhiên là tôi đã vui vẻ nhận lời.」
- Lý do: JP chứa 御一夜鉄道, TW đồng ý (御一夜鐵路); VN hiện tại còn dạng cũ "Đường sắt Ohito" → đổi thành "Đường sắt Ohitoyo" theo T2. Phần "Ohitoyo" còn lại trong dòng đã sửa đúng trong U1b, không đụng.

## §3. Đã kiểm chứng, giữ nguyên, không dòng (không sửa)

- **9 dòng tưởng là ứng viên nhưng đã sửa xong trong U2a** (thấy được khi dùng sai thứ tự moan > audit > unification; đã kiểm chứng từng dòng bằng tra cứu trực tiếp file U2a): ハチロク04_小畑越え 1823/2112, ハチロク04_煙には煙を 1855/1920, ハチロク05_レイルロオドたち 2960, ハチロク15b_さよなら列車 1637, 日々姫16_夢を乗せて 2107, ポーレット03_大きなにもつのおばあさん 1750, ハチロク12_ムナカタ来訪 2565 — fix U2a của cả 9 dòng đều đã là "Ohitoyo"; old_vn của U2a chính là giá trị audit của chúng. Không đưa vào JSON đợt này (tránh trùng lặp và tránh old_vn sai — giá trị hiện tại của chúng đã là fix U2a, không phải giá trị audit).
- **248 dòng "Ohito" khác trong CSV3 (00–05) đã đúng ở giá trị hiện tại** (135 dòng qua fix unification, 113 dòng qua fix audit) — không đụng.
- **Folder 00_Common 0 dòng** (mọi dòng "Ohito" đã sửa hết trong audit); **03_Paulette 0 dòng** (1750 đã sửa trong U2a); **04_Reina 0 dòng**.
- **CSV3-gap: không có.** Cả 5 dòng đều có trong CSV3 (good set, không dual-set); không cần lấy JP/old_vn từ TOML-2, không dòng nào đặt tw="".
- **0 cờ misalignment, 0 dòng giữ lại vì không chắc chắn.** 2 mục audit có fix=null (凪ふかみ08a 2426, ポーレット13 1357 — các dòng chưa chắc chắn đã biết) được coi là "không có fix" khi xây map; cả hai đều ngoài phạm vi 00–05 và không chứa "Ohito".

## §4. Lượt soát 2

- Tổng số dòng sửa: **5**; tái kiểm chứng (đọc lại từng fix so với JP + kiểm tra ngược bằng máy): **5/5**; loại bỏ: **0**; sửa lại: **0**.
- Kiểm chứng chéo TOML-2: 5/5 (xem §1.7). Kiểm tra ngược fix→old_vn: 5/5. Không còn "Ohito" trần trong fix: 5/5 (regex `Ohito(?!yo)` = 0 lần; mỗi fix chứa đúng 2 lần "Ohitoyo" — 1 lần cũ từ U1 + 1 lần mới đợt này).
- Khối TOML: 4 file / 5 khoá, parse-verified (xem §5).

## §5. Khối TOML (parse-verified — trích fence rồi parse bằng tomllib, so với JSON: 5/5 khớp)

### `ハチロク01_こんにちわ赤ちゃん.txt.toml`

```toml
2467 = "「Việc khôi phục tuyến đường sắt bị bãi bỏ đầu tiên của Đường sắt Ohitoyo——Về cách xử lý đoạn Ohitoyo-Hayato,\\ncuối cùng có hai phương án được giữ lại.」"
```

### `ハチロク12_ムナカタ来訪.txt.toml`

```toml
1900 = "「Đúng là vậy. Vì thế chúng tôi đang trong quá trình chia sẻ tầm nhìn với thành phố Ohitoyo, \\nvà Đường sắt Ohitoyo, để cùng nhau phát triển tạo ra sức mạnh tổng hợp.」"
2089 = "「Bản thân Đường sắt Ohitoyo cũng đang lên kế hoạch mở rộng trong tương lai. \\nƯu tiên hàng đầu là khôi phục Tuyến sông Ohitoyo - Yatsushiro. Sau đó」"
```

### `日々姫08_とれいん食堂.txt.toml`

```toml
3719 = "Đoạn (Yui) - Ohitoyo - Hayato là của Đường sắt Ohitoyo.\\nTừ Hayato - Kagoshima - Sendai - Yatsushiro - Kumamoto là của Đường sắt Mikan."
```

### `真闇h3_補習授業の廃校舎.txt.toml`

```toml
2524 = "「Bởi vì chuyện này có khả năng dẫn đến sự phát triển xa hơn nữa của thành phố Ohitoyo và Đường sắt Ohitoyo mà.\\nTất nhiên là tôi đã vui vẻ nhận lời.」"
```

## Kết bài

Đợt U2c sửa nốt 5 dòng "Đường sắt Ohito" còn sót sau U1/U2a trong 4 file (Hachiroku 3, Hibiki 1, Mayami 1), tất cả đều là T2, JP 御一夜鉄道 xác nhận 5/5, lượt soát 2 đạt 5/5, khối TOML 4 file / 5 khoá parse-verified. Sau đợt này, trong 6 folder 00–05 không còn dòng nào có "Ohito" trần ở giá trị hiện tại (253 dòng CSV3 có "Ohito" đã đối chiếu hết: 248 đã đúng, 5 sửa trong đợt này). Lưu ý cho coordinator: thứ tự ưu tiên giá trị hiện tại đúng là unification (đã gộp) > moan > audit > CSV3 — thứ tự moan > audit > unification ghi trong task sẽ tạo 9 mục trùng lặp sai (đã sửa trong U2a); các batch sau nên dùng thứ tự đã hiệu chỉnh này.
