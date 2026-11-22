# Unification batch U5 — §1 misc terminology (T8/T9/T25–T28/T50–T53) + §4 gloss sweeps G1/G2

## §0. Phạm vi

- Mục DECIDED theo `UNIFICATION-LIST.md` §1 + §4, batch U5 (`queue.json`): **T8, T9, T25, T26, T27, T28, T50, T51, T52, T53, G1, G2**.
- Kết quả: **8 mục có dòng sửa / 336 dòng sửa** — T8: 18, T25: 2 (1 dòng chung với T26), T26: 2 (1 dòng chung với T25), T27: 90 (85 gloss + 5 plain), T51: 2, T52: 20, G1: 121, G2: 83 (82 + 1 dòng chung với T27). 4 mục đã kiểm chứng, 0 dòng sửa: **T9, T28, T50, T53** (xem §4).
- Phân bố nguồn old_vn (quy ước rebuild đã sửa 22/11 ~11:35: unification-đã-gộp > moan > audit > CSV3): CSV3 207, audit 116, unification-đã-gộp 12, moan 1. 12 dòng unif-src (old_vn = fix của batch đã gộp, fix đợt này chỉ đổi phần của mình): れいな03 1455 (G1), グランド06 1923 (T52, fix U2b), ハチロク02 2376 (G2), ハチロク04 2393 (G1), ハチロク04 2464 (G1), 日々姫05 2701 (T52), ハチロク15a 2031 (G2, fix U9 — gộp 22/11 ~11:45, sau khi map đợt này dựng lần đầu; đã nạp lại map và sửa old_vn/fix thành giá trị kết hợp). Thêm 5 dòng GHÉP bởi coordinator 22/11 (U5-7): ハチロク11 2251 (T27, fix U3), ハチロク13 2326/2328 (T27, fix U4), ハチロク13 2336 (T27, fix U4), ポーレット03 2814 (G2, fix U4). Riêng 2464 nguồn gốc CSV3 lúc liệt kê (bản đếm cũ ghi nhầm là unif-src — nay đã gộp đúng, old_vn = fix U4).
- Không đụng dòng gasp Ư hay dòng "Kh" nào (kiểm tra bằng máy: 0 dòng fix chạm token Ư/Kh — mọi fix chỉ đổi đúng chuỗi thuật ngữ/gloss của mục mình).

## §1. Phương pháp liệt kê (chỉ đếm, không sửa hàng loạt)

1. Đọc CSV3 good-set 87.833 dòng (đã bỏ 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`).
2. Tính giá trị hiện tại (current value) cho mọi dòng: fix unification **đã gộp** (9 file: U1a/U1b/U1c, U2a, **U2b, U2c, U9 — gộp trong lúc batch chạy, đã nạp lại vào map trước khi assemble**, U6, U10) > fix moan (1.516 mục) > fix audit (9.238 mục — 2 mục fix:null đã bỏ: 凪ふかみ08a 2426, ポーレット13 1357) > VN CSV3. Map `_u5_map.json`: 87.833 good-set, audit 9.238 mapped (0 unmatched), moan 1.516 mapped (0 unmatched), unif-đã-gộp 678 mục. **Lưu ý:** file U3 (set2), U4 (set3), U13a (t56-t66), U7a/U7b, U11a, U12a, U12b đang RUNNING — KHÔNG nằm trong map; trùng lặp với chúng được kiểm tra riêng ở §4. U9 đã gộp 22/11 ~11:45 và đã nằm trong map.
3. Ứng viên mỗi mục = current value còn chứa dạng cũ VÀ JP chứa thuật ngữ gốc (đọc từng dòng JP + TW). Số ứng viên: T8 79, T9 4, T25 8, T26 56, T27/T28 118 (JP có タブレット), T50 21, T51 396, T52 73, T53 230, G1 194 (tag %l列車), G2 230 (tag %l機関士).
4. Kiểm chứng chéo current value với TOML-2: các dòng hand-fix (48 dòng) đều có mặt; old_vn của 6 dòng unif-src khớp fix của batch đã gộp (vd. Grand06 1923 = fix U2b: "Đường sắt Ohitoyo" + "Teito").
5. Fix = chỉ thay thế đúng chuỗi mục tiêu, giữ nguyên toàn bộ phần còn lại (kể cả các phần audit đã sửa khác, kể cả đại từ, kể cả các gloss %l khác trong cùng dòng — trừ dòng gộp 2090/2411 xem §3).

## §2. Quyết định trong batch (theo uỷ quyền của Hieu — điều tra JP+TW rồi quyết, không park)

### T8 — まいてつ → "chủ tàu" (18 dòng)

Dạng chung (common noun) của まいてつ = "chủ tàu" (tips entry "Chủ sở hữu tàu" là tips-only). 18 dòng sửa: 6 ở 共通05 (đa số gloss %lまいてつ "Maitetsu" → "chủ tàu"), 6 ở ハチロク01 (5 gloss + 1 plain "các Maitetsu ở khắp nơi"), 1 ở ポーレット02 (2078), 2 ở ポーレット04 (plain "maitetsu" thường), 3 ở グランド08 (JP 大物まいてつ / まいてつ trần, VN cũ dịch lệch "ông trùm đường sắt"/"giới đường sắt" → "chủ tàu (lớn)"). Viết hoa "Chủ tàu" khi ở đầu câu (ハチロク01 2475 — tag mở đầu câu, JP まいてつが文頭).

### T25 — 従輪 → "Bánh xe chịu tải" (2 dòng, 1 dòng chung T26) · T26 — 動輪 → "Bánh xe chủ động" (2 dòng, 1 dòng chung T25)

- **ポーレット08 2090 (item T25+T26):** JP "動輪4つに先輪2つに、従輪3つ" — VN cũ thiếu "xe" ở 2 chỗ: "4 bánh chủ động, 2 bánh dẫn hướng trước, 3 bánh chịu tải sau" → "4 bánh xe chủ động, 2 bánh dẫn hướng trước, 3 bánh xe chịu tải sau". Giữ nguyên "sau"/"trước" (thông tin vị trí) và viết thường giữa câu.
- **仲国03 1540 (T25, gloss %l従輪):** "Bánh chịu tải không động lực" → "Bánh xe chịu tải không động lực" — chỉ thêm "xe"; KHÔNG bỏ "không động lực" (dạng tips "Bánh xe chịu tải không động lực" là tips-only, nhưng gloss này đã có "không động lực" từ trước và nó đúng nghĩa: 従輪 là bánh không truyền động).
- **ポーレット03 2412 (T26):** JP "動輪がレールをたたく音" — VN cũ (audit-src, thực ra là dòng lệch khác trong CSV3) "Chỉ còn tiếng bánh xe gõ lên đường ray…" → "Chỉ còn tiếng bánh xe chủ động gõ lên đường ray…".

### T27 — タブレット (Railord core) → gloss "Thẻ bảng (Tablet)" (90 dòng: 85 gloss + 5 plain)

**Phát hiện lớn nhất của batch:** audit đã đổi có hệ thống gloss core タブレット từ CSV3 "thẻ bảng"/"Tablet" sang "máy tính bảng" (theo quy tắc cũ trong AUDIT-BRIEF.md:12 — 操作板/タブレット → "máy tính bảng"), ở rất nhiều file (Common 08, ハチロク07, ハチロク10_旺宮鉄道歴史館, グランド10, ハチロク14, ハチロク16, 共通10/15, ポーレット11, 仲国01…). Quyết định 22/11 ~04:03 (Hieu) nói core KHÔNG BAO GIỜ là "máy tính bảng". Dạng đích (tips entry §168 + LOGIC-DICH-VA-SUA.md:83,368–370): gloss %lタブレット → **"Thẻ bảng (Tablet)"** (luôn viết hoa, dạng tựa đề của tips entry); dialogue plain core = "thẻ bảng" hoặc "Tablet" (LOGIC).

**Census gloss %lタブレット (giá trị hiện tại):** 75 dòng / 80 tag — "máy tính bảng" 63, "Tablet" 9, "thẻ bảng" 6, "Máy tính bảng" 2; dạng "Thẻ bảng (Tablet)" xuất hiện **0 lần**. Cả 75 dòng đều sửa. Cộng 10 dòng ニイロク04 (%l操作板 — xem dưới) = **85 dòng gloss**.

**CỜ G8 (căng thẳng cần parent/Hieu chốt):** G8 ghi "Common 08 ×4 KEEP 'thẻ bảng'" — viết theo trạng thái CSV3. Giá trị hiện tại của 4 dòng đó (1480/1929/1991/2836) là audit "máy tính bảng". Đợt này khôi phục chúng về dạng TIPS đã chốt "Thẻ bảng (Tablet)" — thỏa ý G8 (không phải "máy tính bảng"). Nếu Hieu muốn 4 dòng đó là "thẻ bảng" trần (không "(Tablet)"), parent lật lại 4 dòng này sau.

**ニイロク04_終端 (10 dòng: 1918/2011/2054/2061/2151/2152/2153/2411/2624/2673):** JP chỉ có タブレット (không có 操作板), VN dùng tag %l操作板 với gloss "máy tính bảng"/"Máy tính bảng". Fix CHỈ gloss → "Thẻ bảng (Tablet)", GIỮ nguyên term 操作板 trong tag (brief cấm sửa term JP trong tag). **Cờ cho U15/G12:** term tag 操作板 ≠ JP タブレット ở 10 dòng này (1918 có 2 tag).

**Plain-text core (5 dòng):** 4 dòng KHÔI PHỤC về CSV3 (trạng thái trước khi audit đổi sai): lr_ハチロクh2 1440 "máy tính bảng" → "Tablet" (moan-src); ハチロクh1 1382 "Máy tính bảng, tháo ra…" → "Thẻ bảng, tháo ra…" (đầu câu, viết hoa); ハチロクh1 2013 "tháo cả máy tính bảng ra" → "tháo cả thẻ bảng ra"; ポーレット04 2642 "Đọc được máy tính bảng, Express" → "Đọc được Thẻ bảng, Express". 1 dòng device: ハチロク12 1594 "hãy dùng Tablet này" → "hãy dùng máy tính bảng này" (TW 平板電腦 là quyết định — TW dùng 操作板 cho core ở mọi chỗ khác, 平板 ở đây là ngoại lệ có ý nghĩa; cảnh khảo sát thực địa, "このタブレット" = thiết bị cầm tay).

**Phát hiện P04 2076/2642 (audit review sai):** audit review P04 cho rằng タブレット ở đây = "máy tính bảng mà Hikari đang đọc" (đọc từ tablet của Hibiki) — SAI. CSV3 key 2604 monologue: "ひかりが読めていたものは、旧帝鉄の――つまり、御一夜鉄道でも同じく使われている表記部分で" (thứ Hikari đọc được là ký hiệu/chữ viết cũ của Teitetsu trên tàu). Cô ấy đọc chữ viết TRÊN TÀU (ストーブ客車, タブレット, エクスプレス, ブレスレット); タブレット = core term. JP 2076 là hiragana たぶれっと. Nên 2076 → gloss "Thẻ bảng (Tablet)", 2642 → plain "Thẻ bảng" (khôi phục CSV3). Ghi thêm: audit review P04 dòng 16 ghi VN đã thêm %l tag ở 7 dòng JP không có (1780/1811/2028/2050/2076/2698/2816) — thuộc G12, không đụng đợt này; 2076 giữ nguyên tag, chỉ sửa gloss.

**ハチロク10_旺宮鉄道歴史館 2636:** chỉ sửa gloss; plain "Railord Tablet" (tên công ty) giữ "Tablet".

### T51 — 隈元 → "Kumamoto" (2 dòng)

106 dòng JP-隈元; 104 đã đúng "Kumamoto". 2 ngoại lệ đều là JP 隈元銀行 (tên đầy đủ của ngân hàng) bị rút thành "Kumagin": 稀咲02 2649 "giám đốc chi nhánh của Kumagin" → "giám đốc chi nhánh Ngân hàng Kumamoto"; 稀咲03 2713 "của Kumagin chi nhánh Ohitoyo" → "của Ngân hàng Kumamoto chi nhánh Ohitoyo". "Kumagin" ĐÚNG cho JP 隈銀 (くまぎん, biệt danh ngân hàng) — giữ 20 dòng còn lại.

### T52 — 帝都 → "Đế đô" (20 dòng)

73 dòng JP-帝都: 53 "Đế đô" (đúng), 10 "Đế Đô" (viết hoa giữa câu → "Đế đô"), 6 "Teito" (đều ở グランド06_稀咲: 1841/1923/2113/2208/2519/2702 → "Đế đô"), 4 "thủ đô" (dạng chung → "Đế đô": ハチロク12 2091 "khu vực thủ đô" → "khu vực Đế đô"; 日々姫04 2134, 日々姫05 2470 "trên thủ đô" → "ở Đế đô"; 日々姫05 2701 "hay thủ đô" → "hay Đế đô"). Ranh giới sửa từng phần: 真闇h3 3299 chỉ sửa "Đế Đô"→"Đế đô", ĐỂ NGUYÊN "Đại học Hoàng gia" (T5, chưa giao batch nào — cờ §4); グランド06 1923 chỉ sửa "Teito"→"Đế đô" (phần "Đường sắt Ohito" đã do U2b sửa — old_vn đợt này đã là fix U2b).

### T9 / T28 / T50 / T53 — 0 dòng sửa (đã kiểm chứng)

- **T9 市電 → "tàu điện thành phố":** chỉ 4 dòng JP-市電 toàn dự án (共通05 2404/2378, ハチロク02 1917/71); cả 4 đã được audit sửa đúng.
- **T28 iPad = "máy tính bảng":** 20 dòng đã đúng, plain text, không %l tag — giữ nguyên (danh sách ở §4).
- **T50 流 → "Nagare":** 21 ứng viên đều đã đúng "Nagare" hoặc SFX "Ryu" (りゅ/りゅっ — tiếng liếm: lr_稀咲ポーレットh1 2507, lr_凪h1 1219, lr_ふかみh2 1744 — giữ). 5 dòng "ông Ryu" ở ハチロク08_教導 (3380/3167/3168/3171/2210) đã được audit sửa thành "Nagare" (list ghi nhầm là 日々姫03 — sai file, xem §4).
- **T53 運転台 → "buồng lái":** 135 dòng JP-運転台; 134 đã đúng; 1 dòng tưởng là ngoại lệ — 仲国07 1726 — thực ra ĐÃ chứa "buồng lái" (với khoảng trắng full-width "buồng　lái" trong đoạn gắn tag %f, khớp định dạng nguồn) — giữ. 217 dòng có "buồng lái" mà JP không có 運転台 (term JP khác) — ngoài phạm vi, giữ.

### G1 — 列車 %l gloss → "đoàn tàu" (121 dòng / 192 dòng có tag)

Census gloss %l列車 (giá trị hiện tại, 192 dòng / 197 tag): "tàu" 85, "đoàn tàu" 67, "chuyến tàu" 26, "Tàu" 8, "Đoàn tàu" 7, "Chuyến tàu" 4. Sửa 121 dòng, giữ nguyên viết hoa: "tàu"→"đoàn tàu", "Tàu"→"Đoàn tàu", "chuyến tàu"→"đoàn tàu", "Chuyến tàu"→"Đoàn tàu". Tất cả 121 dòng đã kiểm JP chứa 列車. Dòng 2 tag: ポーレット09 2232 (2× "tàu" → sửa cả 2), 共通12 3473 (2× "tàu" → sửa cả 2); đã đúng cả 2 tag: ポーレット03 2526, れいな02 1934, 凪ふかみ01 1609. 真闇02_精髄 2319 giữ theo list (đã là "đoàn tàu"). 2 dòng có "%l列車" nhưng là term khác — 列車防護 (凪ふかみ07 2306, 凪ふかみ08b 2397, gloss "phòng vệ tàu" đúng cho 列車防護) — ngoài phạm vi, giữ (giải quyết chênh 192 vs 194 lúc liệt kê).

### G2 — 機関士 %l gloss → "lái tàu" (83 dòng / 230 dòng có tag)

Census gloss %l機関士 (giá trị hiện tại, 230 dòng / 235 tag): "lái tàu" 99, "Lái tàu" 50 (đúng), "người lái tàu" 42, "thợ lái đầu máy" 16, "nhân viên cơ vụ" 13, "Người lái tàu" 11, "Thợ lái đầu máy" 2, "nữ lái tàu" 1, "Master" 1. Sửa 83 dòng, giữ nguyên viết hoa: "người lái tàu"→"lái tàu", "Người lái tàu"→"Lái tàu", "thợ lái đầu máy"→"lái tàu", "Thợ lái đầu máy"→"Lái tàu", "nữ lái tàu"→"lái tàu" (日々姫06 3394 — JP 女性機関士, list ghi rõ), "nhân viên cơ vụ"→"lái tàu" (13 lần xuất hiện: P10 959/1241, Common12 2574/2911, Common15 2029/2136/2938/3161, 稀咲02 1378/2017/2260/2569/2634 — đều là 機関士 trần, kể cả 2938 "chiếc cặp nhân viên cơ vụ" = 機関士鞄, túi của lái tàu). Tất cả các dòng đã kiểm JP chứa 機関士. Dòng 2 tag: ハチロク03 2679 ("Người lái tàu"+"người lái tàu" → "Lái tàu"+"lái tàu"), 2709 (2× "người lái tàu" → 2× "lái tàu"); đã đúng cả 2 tag: ハチロク06 2830, ハチロク12 2864, 凪ふかみ08a 2568.

**GIỮ — 共通04_キハ07。ポーレットとれいな 2651 gloss "Master":** JP có ruby [マスター,2]機関士; gloss diễn ruby (cô ấy muốn anh làm Master của mình, không chỉ là lái tàu) — có chủ ý, không đổi. Đây là dòng duy nhất trong 230 dòng có tag %l機関士 bị loại khỏi fix (83 sửa + 146 đã đúng "lái tàu"/"Lái tàu" + 1 giữ này).

**Ranh giới — gloss 運転士:** 3 dòng có CẢ %l機関士 (sửa) và %l運転士 gloss "nhân viên cơ vụ" (ĐỂ NGUYÊN — term khác, không thuộc mục này): 共通03 1638, 共通03 2108, 共通06 2129. Gloss 機関助士 ("phụ lái tàu", vd. 稀咲02 2260) cũng không đụng.

## §3. Bảng sửa (336 dòng)

### T8 — まいてつ → "chủ tàu" (18 dòng)

| File | Key | JP | TW | old_vn | fix | Đổi |
|---|---|---|---|---|---|---|
| グランドリライト08_ふかみ.txt.toml | 2123 | 「一号列車走行開始というゴールに向けて、事業者も\nまいてつも、息をとめての全力疾走を続けている」 | 「為了讓一號列車開始運營，相關公司與掌車人都屏著呼吸，向著目標全力奔跑」 | 「Hướng tới mục tiêu khởi hành chuyến tàu số 1, cả các doanh nghiệp\nvà giới đường sắt đều đang nín thở chạy nước rút.」 | 「Hướng tới mục tiêu khởi hành chuyến tàu số 1, cả các doanh nghiệp\nvà các chủ tàu đều đang nín thở chạy nước rút.」 | «giới» → «các»; «đường» → «chủ»; «sắt» → «tàu» |
| グランドリライト08_ふかみ.txt.toml | 2572 | 一つの事業者が、一人のまいてつが挫けてしまえば、\nその時点で、ナインスターズは地に落ち砕けかねない。 | 只要有那麼一個相關公司、一個掌車人放棄，九星計劃就有可能因此夭折。 | Chỉ cần một doanh nghiệp, một ông trùm đường sắt bỏ cuộc,\nthì ngay lúc đó, Nine Stars có thể sẽ tan tành mây khói. | Chỉ cần một doanh nghiệp, một chủ tàu bỏ cuộc,\nthì ngay lúc đó, Nine Stars có thể sẽ tan tành mây khói. | «ông» → «chủ»; «trùm đường sắt» → «tàu» |
| グランドリライト08_ふかみ.txt.toml | 2595 | 九洲周遊リレートレイン・ナインスターズ一号列車。\n参加を希望し、大物まいてつも九洲入りを予定している。 | 因為環遊九州聯運列車九星一號列車，一些知名掌車人也希望進駐九州，參與運營。 | Chuyến tàu tiếp sức vòng quanh Kyushu - Nine Stars số 1.\nCác ông trùm đường sắt cũng bày tỏ nguyện vọng tham gia và dự định tiến vào Kyushu. | Chuyến tàu tiếp sức vòng quanh Kyushu - Nine Stars số 1.\nCác chủ tàu lớn cũng bày tỏ nguyện vọng tham gia và dự định tiến vào Kyushu. | «ông» → «chủ»; «trùm» → «tàu»; «đường sắt» → «lớn» |
| ハチロク01_こんにちわ赤ちゃん.txt.toml | 2816 | 「ほぼ正解だ。それだけでなく、各地のまいてつ達が、\n各社の構想の中に続々組み入れられている」 | 「雖不中亦不遠矣。不僅如此，各地的掌車人們，也一一投身於各大公司的藍圖之中」 | 「Gần như là chính xác. Không chỉ vậy, các Maitetsu ở khắp nơi,\ncũng đang lần lượt được đưa vào dự án của các công ty.」 | 「Gần như là chính xác. Không chỉ vậy, các chủ tàu ở khắp nơi,\ncũng đang lần lượt được đưa vào dự án của các công ty.」 | «Maitetsu» → «chủ tàu» |
| ハチロク01_双鉄の目・ハチロクの目.txt.toml | 1361 | ……\x%lまいてつ;#00ffc040;まいてつ%l;#;たちは、自分に必要な車輌を手放さない。\nそして\x%l客車;#00ffc040;客車%l;#;は、動力車よりも欲しがるものが限られている。 | ……\x%lまいてつ;#00ffc040;掌車人%l;#;們自然不會輕易放棄自己需要的車輛。而\x%l客車;#00ffc040;客運車廂%l;#;更因其比動力車更高的稀缺性而異常搶手。 | ……Các \x%lまいてつ;#00ffc040;Maitetsu%l;#; sẽ không từ bỏ phương tiện cần thiết cho mình.\nVà \x%l客車;#00ffc040;toa hành khách%l;#; thì, đối tượng mong muốn sở hữu nó còn hạn chế hơn cả toa xe động lực. | ……Các \x%lまいてつ;#00ffc040;chủ tàu%l;#; sẽ không từ bỏ phương tiện cần thiết cho mình.\nVà \x%l客車;#00ffc040;toa hành khách%l;#; thì, đối tượng mong muốn sở hữu nó còn hạn chế hơn cả toa xe động lực. | «\x%lまいてつ;#00ffc040;Maitetsu%l;#;» → «\x%lまいてつ;#00ffc040;chủ tàu%l;#;» |
| ハチロク01_双鉄の目・ハチロクの目.txt.toml | 1394 | 「――引退した\x%lまいてつ;#00ffc040;まいてつ%l;#;が放出することもありますけど、\nそういうのは、たいてい動力車もセットですから……」 | 「——因\x%lまいてつ;#00ffc040;掌車人%l;#;引退而轉手的情況倒也不是沒有，但這種情況基本都是和動力車打包的……」 | 「——Mặc dù cũng có trường hợp các \x%lまいてつ;#00ffc040;Maitetsu%l;#; đã nghỉ hưu nhượng lại,\nnhưng những trường hợp đó, thường là đi kèm cả toa xe động lực theo bộ……」 | 「——Mặc dù cũng có trường hợp các \x%lまいてつ;#00ffc040;chủ tàu%l;#; đã nghỉ hưu nhượng lại,\nnhưng những trường hợp đó, thường là đi kèm cả toa xe động lực theo bộ……」 | «\x%lまいてつ;#00ffc040;Maitetsu%l;#;» → «\x%lまいてつ;#00ffc040;chủ tàu%l;#;» |
| ハチロク01_双鉄の目・ハチロクの目.txt.toml | 2041 | 「ポーレットの\x%lまいてつ;#00ffc040;まいてつ%l;#;仲間たちは見てくれていよう。\nならば、当初の目的のためにはマッチしていようが――」 | 「波萊特的\x%lまいてつ;#00ffc040;掌車人%l;#;朋友們都有在看吧。這倒也沒有違背開設網站的初衷，不過——」 | 「Chắc những người bạn \x%lまいてつ;#00ffc040;Maitetsu%l;#; của Paulette vẫn xem đấy.\nNếu vậy thì, nó vẫn phù hợp với mục đích ban đầu, nhưng——」 | 「Chắc những người bạn \x%lまいてつ;#00ffc040;chủ tàu%l;#; của Paulette vẫn xem đấy.\nNếu vậy thì, nó vẫn phù hợp với mục đích ban đầu, nhưng——」 | «\x%lまいてつ;#00ffc040;Maitetsu%l;#;» → «\x%lまいてつ;#00ffc040;chủ tàu%l;#;» |
| ハチロク01_双鉄の目・ハチロクの目.txt.toml | 2224 | 「\x%lまいてつ;#00ffc040;まいてつ%l;#;さんの引退を待つ以外で、\n\x%l客車;#00ffc040;客車%l;#;を手に入れる方法って全然無いんですか？」 | 「除了等待\x%lまいてつ;#00ffc040;掌車人%l;#;引退以外，就完全沒有得到\x%l客車;#00ffc040;客運車廂%l;#;的方法了嗎？」 | 「Ngoài việc chờ các \x%lまいてつ;#00ffc040;Maitetsu%l;#; nghỉ hưu ra,\nthì hoàn toàn không còn cách nào khác để có được \x%l客車;#00ffc040;toa hành khách%l;#; sao ạ?」 | 「Ngoài việc chờ các \x%lまいてつ;#00ffc040;chủ tàu%l;#; nghỉ hưu ra,\nthì hoàn toàn không còn cách nào khác để có được \x%l客車;#00ffc040;toa hành khách%l;#; sao ạ?」 | «\x%lまいてつ;#00ffc040;Maitetsu%l;#;» → «\x%lまいてつ;#00ffc040;chủ tàu%l;#;» |
| ハチロク01_双鉄の目・ハチロクの目.txt.toml | 2475 | \x%lまいてつ;#00ffc040;まいてつ%l;#;が、どれほど実用に即していようと\n究極的には趣味の色合いが濃い世界なら…… | 在\x%lまいてつ;#00ffc040;掌車人%l;#;的世界，不論如何向實用妥協，骨子裡還是對興趣的嚮往，如此想來…… | \x%lまいてつ;#00ffc040;Maitetsu%l;#;, dù có thực dụng đến mức nào đi chăng nữa\nnhưng xét cho cùng, nếu đó là một thế giới mang đậm màu sắc sở thích thì…… | \x%lまいてつ;#00ffc040;Chủ tàu%l;#;, dù có thực dụng đến mức nào đi chăng nữa\nnhưng xét cho cùng, nếu đó là một thế giới mang đậm màu sắc sở thích thì…… | «\x%lまいてつ;#00ffc040;Maitetsu%l;#;,» → «\x%lまいてつ;#00ffc040;Chủ tàu%l;#;,» |
| ポーレット02_解放b寝台.txt.toml | 2078 | 「つまり、とき鉄の線路を、みち鉄の車両――か、\nみち鉄所属のまいてつさんの車両が走っているのか」 | 「這條線路屬於常鐵，但列車是陸鐵的。也就是說，陸鐵旗下的掌車人負責開動這裡的列車」 | 「Tức là, tàu của Michitetsu—— hay nói đúng hơn là tàu của Maitetsu thuộc sở hữu của Michitetsu, đang chạy trên tuyến đường sắt của Tokitetsu à.」 | 「Tức là, tàu của Michitetsu—— hay nói đúng hơn là tàu của chủ tàu thuộc sở hữu của Michitetsu, đang chạy trên tuyến đường sắt của Tokitetsu à.」 | «Maitetsu» → «chủ tàu» |
| ポーレット04_鳴呼いきストーブ列車.txt.toml | 2020 | 「こっちのまいてつ仲間に、窓口並んでもらいましたから。\n狙い打ちってぇやつですよ」 | 「我是請這邊的掌車人同行幫我排隊買到的。這裡的票我是志在必得」 | 「Tôi đã nhờ bạn bè maitetsu ở đây xếp hàng ở quầy vé giúp mà. Đúng kiểu đánh trúng mục tiêu đấy.」 | 「Tôi đã nhờ bạn bè chủ tàu ở đây xếp hàng ở quầy vé giúp mà. Đúng kiểu đánh trúng mục tiêu đấy.」 | «maitetsu» → «chủ tàu» |
| ポーレット04_鳴呼いきストーブ列車.txt.toml | 2542 | ここは僕に、父親として、まいてつとしての、\n花を持たせてくれるのだろう。 | 她一定是想為我這個父親，我這個掌車人撐腰吧。 | Chắc là cô ấy đang muốn dành vinh dự cho tôi, với tư cách là một người cha, một maitetsu. | Chắc là cô ấy đang muốn dành vinh dự cho tôi, với tư cách là một người cha, một chủ tàu. | «maitetsu.» → «chủ tàu.» |
| 共通05_ようやく石炭.txt.toml | 1826 | 「いったい、『\x%lまいてつ;#00ffc040;まいてつ%l;#;』とは何であろうな？」 | 「“\x%lまいてつ;#00ffc040;掌車人%l;#;”究竟是什麼呢？」 | 「Rốt cuộc, 『\x%lまいてつ;#00ffc040;Maitetsu%l;#;』 là gì vậy?」 | 「Rốt cuộc, 『\x%lまいてつ;#00ffc040;chủ tàu%l;#;』 là gì vậy?」 | «『\x%lまいてつ;#00ffc040;Maitetsu%l;#;』» → «『\x%lまいてつ;#00ffc040;chủ tàu%l;#;』» |
| 共通05_ようやく石炭.txt.toml | 2132 | 「いや。今のところ、僕は単なる素人だ。\nその、『\x%lまいてつ;#00ffc040;まいてつ%l;#;』がなにかわからぬ程度のな」 | 「不。現在我還僅僅是個外行而已。甚至都不知道“\x%lまいてつ;#00ffc040;掌車人%l;#;”是什麼」 | 「Không. Hiện tại, tôi chỉ là một tay mơ thôi.\nĐến mức còn chẳng biết 『\x%lまいてつ;#00ffc040;Maitetsu%l;#;』 là gì nữa cơ.」 | 「Không. Hiện tại, tôi chỉ là một tay mơ thôi.\nĐến mức còn chẳng biết 『\x%lまいてつ;#00ffc040;chủ tàu%l;#;』 là gì nữa cơ.」 | «『\x%lまいてつ;#00ffc040;Maitetsu%l;#;』» → «『\x%lまいてつ;#00ffc040;chủ tàu%l;#;』» |
| 共通05_ようやく石炭.txt.toml | 2155 | 「つまり“\x%lまいてつ;#00ffc040;まいてつ%l;#;”とは、個人で\x%l列車;#00ffc040;列車%l;#;を所有し走らせる\n――そうした鉄道マニ……ファンのことですね？」 | 「也就是說所謂“\x%lまいてつ;#00ffc040;掌車人%l;#;”，指的就是以個人身份擁有\x%l列車;#00ffc040;列車%l;#;並使其運作的鐵路迷……鐵路愛好者嗎？」 | 「Nói tóm lại “\x%lまいてつ;#00ffc040;Maitetsu%l;#;” là những người sở hữu cá nhân và vận hành \x%l列車;#00ffc040;đoàn tàu%l;#;\n——Tức là những fan……những người hâm mộ đường sắt đó phải không?」 | 「Nói tóm lại “\x%lまいてつ;#00ffc040;chủ tàu%l;#;” là những người sở hữu cá nhân và vận hành \x%l列車;#00ffc040;đoàn tàu%l;#;\n——Tức là những fan……những người hâm mộ đường sắt đó phải không?」 | «“\x%lまいてつ;#00ffc040;Maitetsu%l;#;”» → «“\x%lまいてつ;#00ffc040;chủ tàu%l;#;”» |
| 共通05_ようやく石炭.txt.toml | 2472 | 「\x%lまいてつ;#00ffc040;まいてつ%l;#;の人かな。\x%lレイルロオド;#00ffc040;レイルロオド%l;#;と一緒だし」 | 「是\x%lまいてつ;#00ffc040;掌車人%l;#;吧。還帶著\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;」 | 「Chắc là người của hội \x%lまいてつ;#00ffc040;Maitetsu%l;#; nhỉ. Đi cùng với \x%lレイルロオド;#00ffc040;Railord%l;#; mà.」 | 「Chắc là người của hội \x%lまいてつ;#00ffc040;chủ tàu%l;#; nhỉ. Đi cùng với \x%lレイルロオド;#00ffc040;Railord%l;#; mà.」 | «\x%lまいてつ;#00ffc040;Maitetsu%l;#;» → «\x%lまいてつ;#00ffc040;chủ tàu%l;#;» |
| 共通05_ようやく石炭.txt.toml | 2501 | 「そうなんです。毛利のお姫様の『廣島毛利電気鉄道』が、\n\x%lまいてつ;#00ffc040;まいてつ%l;#;という互助システムの出発点です」 | 「是的。毛利公主殿下的“廣島毛利電力鐵路”，就是\x%lまいてつ;#00ffc040;掌車人%l;#;這一互助制度的原點」 | 「Đúng vậy. 『Đường sắt điện Hiroshima Mouri』 của công chúa nhà Mouri,\nchính là điểm xuất phát của hệ thống tương trợ mang tên \x%lまいてつ;#00ffc040;Maitetsu%l;#;.」 | 「Đúng vậy. 『Đường sắt điện Hiroshima Mouri』 của công chúa nhà Mouri,\nchính là điểm xuất phát của hệ thống tương trợ mang tên \x%lまいてつ;#00ffc040;chủ tàu%l;#;.」 | «\x%lまいてつ;#00ffc040;Maitetsu%l;#;.」» → «\x%lまいてつ;#00ffc040;chủ tàu%l;#;.」» |
| 共通05_ようやく石炭.txt.toml | 3296 | テツとは、鉄道マニアのこと。そして、\n“My鉄道”を持つテツが即ち――“\x%lまいてつ;#00ffc040;まいてつ%l;#;”なのか、と。 | 所謂的鐵路人，都是些痴迷鐵路之人。而“擁有專屬列車的人”，也就是“\x%lまいてつ;#00ffc040;掌車人%l;#;”。 | Tetsu nghĩa là người cuồng đường sắt. Và,\nnhững Tetsu sở hữu “My đường sắt” chính là——“\x%lまいてつ;#00ffc040;Maitetsu%l;#;” sao. | Tetsu nghĩa là người cuồng đường sắt. Và,\nnhững Tetsu sở hữu “My đường sắt” chính là——“\x%lまいてつ;#00ffc040;chủ tàu%l;#;” sao. | «là——“\x%lまいてつ;#00ffc040;Maitetsu%l;#;”» → «là——“\x%lまいてつ;#00ffc040;chủ tàu%l;#;”» |

### T25/T26 — 従輪 → "Bánh xe chịu tải" / 動輪 → "Bánh xe chủ động" (3 dòng)

| File | Key | JP | TW | old_vn | fix | Đổi |
|---|---|---|---|---|---|---|
| 仲国03_北琴鉄道歴史館.txt.toml | 1540 | 「\x%l先輪;#00ffc040;先輪%l;#;が1軸2つで。動輪がD――4軸8つで。\n\x%l従輪;#00ffc040;従輪%l;#;も、1軸2つ」 | 「\x%l先輪;#00ffc040;導輪%l;#;１軸２個，動輪是Ｄ——也就是４軸８個。\x%l従輪;#00ffc040;從輪%l;#;也是１軸２個」 | 「\x%l先輪;#00ffc040;Bánh dẫn hướng trước%l;#; là 1 trục 2 bánh. Bánh xe chủ động là D——4 trục 8 bánh.\n\x%l従輪;#00ffc040;Bánh chịu tải không động lực%l;#; cũng là 1 trục 2 bánh.」 | 「\x%l先輪;#00ffc040;Bánh dẫn hướng trước%l;#; là 1 trục 2 bánh. Bánh xe chủ động là D——4 trục 8 bánh.\n\x%l従輪;#00ffc040;Bánh xe chịu tải không động lực%l;#; cũng là 1 trục 2 bánh.」 | +«xe » |
| ポーレット08_未来へのレール.txt.toml | 2090 | 「動輪4つに[せんりん,1]先輪2つに、[じゅうりん,1]従輪3つ。\n[にーでーさん,2]2d3、[よんはちろく,4]4-8-6の車軸配置。か」 | 「四個動輪、兩個導輪、三個從輪。軸式為\x%l2D3;#00ffc040;２Ｄ３%l;#;、\x%l4-8-6;#00ffc040;４－８－６%l;#;嗎」 | 「4 bánh chủ động, 2 bánh dẫn hướng trước, 3 bánh chịu tải sau.\nSơ đồ trục \x%l2D3;#00ffc040;2D3%l;#;, \x%l4-8-6;#00ffc040;4-8-6%l;#;. À」 | 「4 bánh xe chủ động, 2 bánh dẫn hướng trước, 3 bánh xe chịu tải sau.\nSơ đồ trục \x%l2D3;#00ffc040;2D3%l;#;, \x%l4-8-6;#00ffc040;4-8-6%l;#;. À」 | +« xe»; +«xe » |
| ポーレット03_大きなにもつのおばあさん.txt.toml | 2412 | つかの間、沈黙。\n動輪がレールをたたく音だけが、車内に規則正しく響く。 | 我們就這麼沉默地坐了一會。只剩動輪碾過鐵軌的聲音在車廂裡有規律地迴響。 | Chốc lát im lặng.\nChỉ còn tiếng bánh xe gõ lên đường ray vang đều đều trong toa. | Chốc lát im lặng.\nChỉ còn tiếng bánh xe chủ động gõ lên đường ray vang đều đều trong toa. | +« chủ động» |

### T27 — plain text (4 khôi phục CSV3 + 1 device) (5 dòng)

| File | Key | JP | TW | old_vn | fix | Đổi |
|---|---|---|---|---|---|---|
| lr_ハチロクh2_新しい服。新しい旅.txt.toml | 1440 | 「ふぁっ！　あらま、タブレット、ぜんぶ、おかひく――\nまっひろになるっ、んっ！　チカチカって、しへっ」 | 「呼啊！腦袋、操作板，都變得，不正常了……全部一片空白，嗯！似乎要，火星四濺！」 | 「Fa! Chết mất, máy tính bảng, kỳ lạ hết rồi——\nTrắng xóa mất, ưm! Chớp nháy, liên tục」 | 「Fa! Chết mất, Tablet, kỳ lạ hết rồi——\nTrắng xóa mất, ưm! Chớp nháy, liên tục」 | «máy tính bảng,» → «Tablet,» |
| ハチロク12_ムナカタ来訪.txt.toml | 1594 | 「ハチロク、このタブレットを使い、ナビとも連携し、\nこの周辺の地下水流や、火山活動の情報収集をしてくれ」 | 「八六，你馬上用這平板與Ｎａｖｉ聯繫，合作調查這一帶的地下徑流，以及火山活動的訊息」 | 「Hachiroku, hãy dùng Tablet này, kết hợp với Navi, \nthu thập thông tin về mạch nước ngầm và hoạt động núi lửa xung quanh đây nhé.」 | 「Hachiroku, hãy dùng máy tính bảng này, kết hợp với Navi, \nthu thập thông tin về mạch nước ngầm và hoạt động núi lửa xung quanh đây nhé.」 | «Tablet» → «máy tính bảng» |
| ハチロクh1_契り.txt.toml | 1382 | 「タブレット、外してしまって大丈夫なのか？」 | 「操作板也可以卸下來的嗎？」 | 「Máy tính bảng, tháo ra như vậy có sao không?」 | 「Thẻ bảng, tháo ra như vậy có sao không?」 | «「Máy tính» → «「Thẻ» |
| ハチロクh1_契り.txt.toml | 2013 | どころか、タブレットまでを外してしまう。 | 甚至操作板她要卸了下來。 | Thậm chí, em ấy còn tháo cả máy tính bảng ra. | Thậm chí, em ấy còn tháo cả thẻ bảng ra. | «máy tính» → «thẻ» |
| ポーレット04_鳴呼いきストーブ列車.txt.toml | 2642 | タブレット、エクスプレスは読めるのに、\n『ブレスレット』は読めない。 | 明明會讀\x%lタブレット;#00ffc040;操作板%l;#;，特快列車，卻不會讀手鍊。 | Đọc được máy tính bảng, Express, nhưng lại không đọc được 『Bracelet』 (Vòng tay). | Đọc được Thẻ bảng, Express, nhưng lại không đọc được 『Bracelet』 (Vòng tay). | «máy tính» → «Thẻ» |

### T27 — gloss %lタブレット / %l操作板 → "Thẻ bảng (Tablet)" (84 dòng; +1 dòng gộp G2+T27 ở bảng G2 = 85 dòng gloss) (84 dòng)

| File | Key | JP | TW | old_vn | fix | Đổi |
|---|---|---|---|---|---|---|
| れいな02_れいなとポーレット.txt.toml | 2657 | れいなは床に降り立って、\n手早く\x%lタブレット;#00ffc040;タブレット%l;#;を換装する。 | 玲奈從座位上跳下來，迅速地將\x%lタブレット;#00ffc040;操作板%l;#;更換過去。 | Reina nhảy xuống sàn, nhanh nhẹn tháo lắp \x%lタブレット;#00ffc040;máy tính bảng%l;#;. | Reina nhảy xuống sàn, nhanh nhẹn tháo lắp \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;. | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;.» → «(Tablet)%l;#;.» |
| グランドリライト10_ハチロク.txt.toml | 1119 | ……トゥーレシビック博士こそは、真なる天才だったのだ。\n\x%lタブレット;#00ffc040;タブレット%l;#;とは、安全装置に他ならぬがゆえ。 | ……特里維西克博士才是真正的天才啊。因為\x%lタブレット;#00ffc040;操作板%l;#;正是最關鍵的保險裝置啊。 | ……Tiến sĩ Trevithick quả thực là một thiên tài thực sự.\nBởi vì \x%lタブレット;#00ffc040;máy tính bảng%l;#;, không gì khác chính là một thiết bị an toàn. | ……Tiến sĩ Trevithick quả thực là một thiên tài thực sự.\nBởi vì \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;, không gì khác chính là một thiết bị an toàn. | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;,» → «(Tablet)%l;#;,» |
| グランドリライト10_ハチロク.txt.toml | 1898 | 「\x%lタブレット;#00ffc040;タブレット%l;#;新造と\x%lレイルロオド;#00ffc040;レイルロオド%l;#;新造とを、事業化する。\n鉄道分野にとどまらぬ、人類の新しいパートナーとして」 | 「把\x%lタブレット;#00ffc040;操作板%l;#;和\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的生產事業進行產業化。不要局限於鐵路領域，而是作為人類的新伙伴」 | 「Thương mại hóa việc chế tạo \x%lタブレット;#00ffc040;máy tính bảng%l;#; mới và \x%lレイルロオド;#00ffc040;Railord%l;#; mới.\nKhông chỉ dừng lại ở lĩnh vực đường sắt, mà như những đối tác mới của nhân loại」 | 「Thương mại hóa việc chế tạo \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; mới và \x%lレイルロオド;#00ffc040;Railord%l;#; mới.\nKhông chỉ dừng lại ở lĩnh vực đường sắt, mà như những đối tác mới của nhân loại」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| グランドリライト10_ハチロク.txt.toml | 1907 | 「その方向で広報告知をし、資金を集め、\n\x%lレイルロオド;#00ffc040;レイルロオド%l;#;研究を、\x%lタブレット;#00ffc040;タブレット%l;#;再開発を進める」 | 「按照這個方向去廣而告之，去籌集資金，繼續推進\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的研究，以及重新開發\x%lタブレット;#00ffc040;操作板%l;#;」 | 「Thông báo rộng rãi theo hướng đó, kêu gọi vốn,\nđẩy mạnh nghiên cứu \x%lレイルロオド;#00ffc040;Railord%l;#; và tái phát triển \x%lタブレット;#00ffc040;máy tính bảng%l;#;」 | 「Thông báo rộng rãi theo hướng đó, kêu gọi vốn,\nđẩy mạnh nghiên cứu \x%lレイルロオド;#00ffc040;Railord%l;#; và tái phát triển \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;」» → «(Tablet)%l;#;」» |
| グランドリライト10_ハチロク.txt.toml | 1941 | 「ですな。エアクラナビも最古の世代は、\x%lタブレット;#00ffc040;タブレット%l;#;内包。\nそれこそ、純粋な\x%lレイルロオド;#00ffc040;レイルロオド%l;#;後継とも申せますし」 | 「是啊。最早一代空凝機導航系統也內建了\x%lタブレット;#00ffc040;操作板%l;#;。所以它們完全可以算作\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的接班人啊」 | 「Đúng vậy. Aircra Navi thế hệ cổ nhất cũng bao hàm \x%lタブレット;#00ffc040;máy tính bảng%l;#;.\nChính điều đó, cũng có thể gọi là hậu duệ \x%lレイルロオド;#00ffc040;Railord%l;#; thuần túy」 | 「Đúng vậy. Aircra Navi thế hệ cổ nhất cũng bao hàm \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;.\nChính điều đó, cũng có thể gọi là hậu duệ \x%lレイルロオド;#00ffc040;Railord%l;#; thuần túy」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;.\nChính» → «(Tablet)%l;#;.\nChính» |
| グランドリライト10_ハチロク.txt.toml | 1982 | 「即効性が認められる可能性がある\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の延命法。\nならびに、今ある\x%lタブレット;#00ffc040;タブレット%l;#;の複製についてを」 | 「有可能立刻奏效的延長\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;壽命的方法，以及現存關於\x%lタブレット;#00ffc040;操作板%l;#;複製的研究成果」 | 「Phương pháp kéo dài tuổi thọ của \x%lレイルロオド;#00ffc040;Railord%l;#; có khả năng mang lại hiệu quả tức thì.\nVà cả việc sao chép \x%lタブレット;#00ffc040;máy tính bảng%l;#; hiện có nữa」 | 「Phương pháp kéo dài tuổi thọ của \x%lレイルロオド;#00ffc040;Railord%l;#; có khả năng mang lại hiệu quả tức thì.\nVà cả việc sao chép \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; hiện có nữa」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| グランドリライト10_ハチロク.txt.toml | 2938 | それを廃して、\x%lタブレット;#00ffc040;タブレット%l;#;形人工知能に置き換え戻せば、\n社会が被る悪影響も、最小限ですむだろう。 | 那麼將其廢棄，重新用回\x%lタブレット;#00ffc040;操作板%l;#;型人工智慧的話，就能把對社會的負面影響控制在最低限度。 | Nếu loại bỏ nó và thay thế lại bằng trí tuệ nhân tạo dạng \x%lタブレット;#00ffc040;máy tính bảng%l;#;,\nthì những ảnh hưởng xấu mà xã hội phải gánh chịu cũng sẽ ở mức tối thiểu. | Nếu loại bỏ nó và thay thế lại bằng trí tuệ nhân tạo dạng \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;,\nthì những ảnh hưởng xấu mà xã hội phải gánh chịu cũng sẽ ở mức tối thiểu. | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;,\nthì» → «(Tablet)%l;#;,\nthì» |
| グランドリライト11_ナインスターズ！.txt.toml | 3554 | そして\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の物を模した\x%lタブレット;#00ffc040;タブレット%l;#;――\nリレートレインの象徴は、僕から赤井\x%l運転士;#00ffc040;運転士%l;#;へと。 | 我將模仿\x%lレイルロオド;#00ffc040;鐵路人偶%l;\x%lタブレット;#;#00ffc040;操作板%l;#;的圓盤——也就是接力列車的象徵交給了赤井\x%l運転士;#00ffc040;駕駛員%l;#;。 | Và \x%lタブレット;#00ffc040;máy tính bảng%l;#; mô phỏng đồ của \x%lレイルロオド;#00ffc040;Railord%l;#;——\nbiểu tượng của chuyến tàu chuyển tiếp, được tôi trao lại cho \x%l運転士;#00ffc040;lái tàu%l;#; Akai. | Và \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; mô phỏng đồ của \x%lレイルロオド;#00ffc040;Railord%l;#;——\nbiểu tượng của chuyến tàu chuyển tiếp, được tôi trao lại cho \x%l運転士;#00ffc040;lái tàu%l;#; Akai. | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ニイロク04_終端.txt.toml | 1918 | 「ですので、あとはタブレットです。\nタブレットさえどうにかできれば」 | 「所以，接下來就是操作板了。只要能搞定操作板，接下來就好說了」 | 「Vì vậy, còn lại là \x%l操作板;#00ffc040;máy tính bảng%l;#;.\nChỉ cần giải quyết được \x%l操作板;#00ffc040;máy tính bảng%l;#; thì.」 | 「Vì vậy, còn lại là \x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#;.\nChỉ cần giải quyết được \x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#; thì.」 | «\x%l操作板;#00ffc040;máy» → «\x%l操作板;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;.\nChỉ» → «(Tablet)%l;#;.\nChỉ»; «\x%l操作板;#00ffc040;máy» → «\x%l操作板;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ニイロク04_終端.txt.toml | 2011 | 「そこまでするなら――後東さんは、\nどうしてタブレットも助けないの？」 | 「為什麼後東先生做到這種地步，也保不住操作板呢？」 | 「Nếu đã làm đến mức đó——thì anh Goto,\ntại sao lại không cứu cả \x%l操作板;#00ffc040;máy tính bảng%l;#;?」 | 「Nếu đã làm đến mức đó——thì anh Goto,\ntại sao lại không cứu cả \x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#;?」 | «\x%l操作板;#00ffc040;máy» → «\x%l操作板;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;?」» → «(Tablet)%l;#;?」» |
| ニイロク04_終端.txt.toml | 2054 | 「結果として、ブランクの運転体が[のこ]遺りました。\nタブレットも、整備体も車輌も無い運転体が」 | 「結果就是，他保住了一台空白的駕駛體。它既沒有操作板，也沒有整備體、更別提車輛」 | 「Kết quả là, một \x%l運転体;#00ffc040;thân vận hành%l;#; trống rỗng đã bị bỏ lại.\nMột \x%l運転体;#00ffc040;thân vận hành%l;#; không có \x%l操作板;#00ffc040;máy tính bảng%l;#;, không có \x%l整備体;#00ffc040;thân bảo trì%l;#; cũng không có toa xe.」 | 「Kết quả là, một \x%l運転体;#00ffc040;thân vận hành%l;#; trống rỗng đã bị bỏ lại.\nMột \x%l運転体;#00ffc040;thân vận hành%l;#; không có \x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#;, không có \x%l整備体;#00ffc040;thân bảo trì%l;#; cũng không có toa xe.」 | «\x%l操作板;#00ffc040;máy» → «\x%l操作板;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;,» → «(Tablet)%l;#;,» |
| ニイロク04_終端.txt.toml | 2061 | 「運転体とタブレット。最低限それだけ守れば」 | 「至少，我一定要保住你的駕駛體和操作板」 | 「\x%l運転体;#00ffc040;Thân vận hành%l;#; và \x%l操作板;#00ffc040;máy tính bảng%l;#;. Chỉ cần bảo vệ được tối thiểu những thứ đó.」 | 「\x%l運転体;#00ffc040;Thân vận hành%l;#; và \x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#;. Chỉ cần bảo vệ được tối thiểu những thứ đó.」 | «\x%l操作板;#00ffc040;máy» → «\x%l操作板;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;.» → «(Tablet)%l;#;.» |
| ニイロク04_終端.txt.toml | 2151 | 「なら、\n動作確認したあとのタブレットは、そのまま？」 | 「那麼，測試完之後的操作板，就放在那不動了？」 | 「Nếu vậy,\n\x%l操作板;#00ffc040;máy tính bảng%l;#; sau khi xác nhận hoạt động xong, sẽ để nguyên như thế à?」 | 「Nếu vậy,\n\x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#; sau khi xác nhận hoạt động xong, sẽ để nguyên như thế à?」 | «vậy,\n\x%l操作板;#00ffc040;máy» → «vậy,\n\x%l操作板;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ニイロク04_終端.txt.toml | 2152 | 「レイルロオド自らがタブレットを外部に投げ捨てる。\n機関助士、ないし密乗した者が同様の行為をする」 | 「鐵路人偶可能會自己把操作板丟到車外面。司爐，以及偷偷搭上車的人也有可能會這麼做」 | 「Railord tự mình ném \x%l操作板;#00ffc040;máy tính bảng%l;#; ra bên ngoài.\n\x%l機関助士;#00ffc040;Phụ lái tàu%l;#;, hoặc kẻ đi lậu vé cũng có thể làm hành động tương tự.」 | 「Railord tự mình ném \x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#; ra bên ngoài.\n\x%l機関助士;#00ffc040;Phụ lái tàu%l;#;, hoặc kẻ đi lậu vé cũng có thể làm hành động tương tự.」 | «\x%l操作板;#00ffc040;máy» → «\x%l操作板;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ニイロク04_終端.txt.toml | 2153 | 「レイルロオドは、\nタブレット換装によっての動作確認がなされます」 | 「鐵路人偶是更換操作板來測試運作是否正常的」 | 「Railord thì,\nsẽ được xác nhận hoạt động thông qua việc hoán đổi \x%l操作板;#00ffc040;máy tính bảng%l;#;.」 | 「Railord thì,\nsẽ được xác nhận hoạt động thông qua việc hoán đổi \x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#;.」 | «\x%l操作板;#00ffc040;máy» → «\x%l操作板;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;.」» → «(Tablet)%l;#;.」» |
| ニイロク04_終端.txt.toml | 2624 | シロのタブレットを、ブランクのダミー運転体に、\nそして、ニイロクの整備体へと。 | 把四六的操作板放到空白的駕駛體上，然後，配以二六的整備體。 | \x%l操作板;#00ffc040;Máy tính bảng%l;#; của Shiro, vào \x%l運転体;#00ffc040;thân vận hành%l;#; mô hình trống rỗng,\nvà sau đó, là vào \x%l整備体;#00ffc040;thân bảo trì%l;#; của Niiroku. | \x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#; của Shiro, vào \x%l運転体;#00ffc040;thân vận hành%l;#; mô hình trống rỗng,\nvà sau đó, là vào \x%l整備体;#00ffc040;thân bảo trì%l;#; của Niiroku. | «\x%l操作板;#00ffc040;Máy» → «\x%l操作板;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ニイロク04_終端.txt.toml | 2673 | どう考えても、高負荷すぎです。\nタブレットが瞬時に破損したとて、おかしくない程。 | 無論怎麼想，這對四六那邊的負荷都太重了。哪怕操作板瞬間損壞也不奇怪。 | Dù nghĩ thế nào, thì cũng quá sức chịu đựng.\nĐến mức dù \x%l操作板;#00ffc040;máy tính bảng%l;#; có bị phá hủy ngay tức khắc, thì cũng không có gì lạ. | Dù nghĩ thế nào, thì cũng quá sức chịu đựng.\nĐến mức dù \x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#; có bị phá hủy ngay tức khắc, thì cũng không có gì lạ. | «\x%l操作板;#00ffc040;máy» → «\x%l操作板;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク07_延命.txt.toml | 1662 | 「仮称じゃ。正式名称の存在しない――\n『\x%lタブレット;#00ffc040;タブレット%l;#;を\x%lタブレット;#00ffc040;タブレット%l;#;たらしめる何か』のこと」 | 「“實現\x%lタブレット;#00ffc040;操作板%l;#;功能之物”——並無正式名稱，暫稱如此而已」 | 「Chỉ là tên gọi tạm thôi. Một thứ không có tên chính thức――\nLà 'thứ khiến \x%lタブレット;#00ffc040;máy tính bảng%l;#; trở thành \x%lタブレット;#00ffc040;máy tính bảng%l;#;'」 | 「Chỉ là tên gọi tạm thôi. Một thứ không có tên chính thức――\nLà 'thứ khiến \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; trở thành \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;'」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;»; «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;'」» → «(Tablet)%l;#;'」» |
| ハチロク07_延命.txt.toml | 2444 | 「\x%lタブレット;#00ffc040;タブレット%l;#;を――\x%lタブレット;#00ffc040;タブレット%l;#;たらしめる」 | 「實現\x%lタブレット;#00ffc040;操作板%l;#;功能——的東西」 | 「Thứ khiến \x%lタブレット;#00ffc040;máy tính bảng%l;#;――trở thành \x%lタブレット;#00ffc040;máy tính bảng%l;#;」 | 「Thứ khiến \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;――trở thành \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;――trở» → «(Tablet)%l;#;――trở»; «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;」» → «(Tablet)%l;#;」» |
| ハチロク07_延命.txt.toml | 2839 | 「\x%lタブレット;#00ffc040;タブレット%l;#;を再現……あるいは新造しようとしても、\n果たせない――というほどの意味でしょうか？」 | 「那也就是說，復現操作板……或者說製造新的\x%lタブレット;#00ffc040;操作板%l;#;已經不可能了，對嗎？」 | 「Ý ngài là dù có cố gắng tái tạo…… hay chế tạo mới \x%lタブレット;#00ffc040;máy tính bảng%l;#;,\ncũng không thể thực hiện được――đúng không ạ?」 | 「Ý ngài là dù có cố gắng tái tạo…… hay chế tạo mới \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;,\ncũng không thể thực hiện được――đúng không ạ?」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;,\ncũng» → «(Tablet)%l;#;,\ncũng» |
| ハチロク07_延命.txt.toml | 3121 | 無意識にだろう。ハチロクが首元の\x%lタブレット;#00ffc040;タブレット%l;#;に触れる。\n\x%lタブレット;#00ffc040;タブレット%l;#;……確かに、極めて定義の難しいものだ。 | 不知是有意還是無意，八六碰了碰頸間的\x%lタブレット;#00ffc040;操作板%l;#;。\x%lタブレット;#00ffc040;操作板%l;#;……還確實是個很難簡單定義的東西。 | Chắc là trong vô thức. Hachiroku chạm vào chiếc \x%lタブレット;#00ffc040;máy tính bảng%l;#; trên cổ.\n\x%lタブレット;#00ffc040;Máy tính bảng%l;#;…… quả thực là một thứ vô cùng khó định nghĩa. | Chắc là trong vô thức. Hachiroku chạm vào chiếc \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; trên cổ.\n\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;…… quả thực là một thứ vô cùng khó định nghĩa. | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;»; «cổ.\n\x%lタブレット;#00ffc040;Máy» → «cổ.\n\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;……» → «(Tablet)%l;#;……» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 1479 | 「\x%lタブレット;#00ffc040;タブレット%l;#;の――魂の自己複製。ないしは繁殖の機能。\nそこに為された封印を、開封するためなのではないかと」 | 「\x%lタブレット;#00ffc040;操作板%l;#;具備——複製靈魂，或者是繁衍後代的能力。而封印也或許正是為此而設的」 | 「Khả năng tự sao chép của \x%lタブレット;#00ffc040;máy tính bảng%l;#;——của linh hồn. Hoặc là chức năng sinh sản.\nChẳng phải là để giải trừ phong ấn được đặt trên đó sao.」 | 「Khả năng tự sao chép của \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;——của linh hồn. Hoặc là chức năng sinh sản.\nChẳng phải là để giải trừ phong ấn được đặt trên đó sao.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;——của» → «(Tablet)%l;#;——của» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 1488 | 「\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の各種法定検査は、\n全て\x%lタブレット;#00ffc040;タブレット%l;#;を外され、非・起動状態で行われますな」 | 「\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的各項法定檢查，均要取下\x%lタブレット;#00ffc040;操作板%l;#;，於關機狀態實行」 | 「Các loại kiểm tra theo luật định của \x%lレイルロオド;#00ffc040;Railord%l;#;,\ntất cả đều được tiến hành trong trạng thái tháo \x%lタブレット;#00ffc040;máy tính bảng%l;#;, tức là trạng thái không khởi động.」 | 「Các loại kiểm tra theo luật định của \x%lレイルロオド;#00ffc040;Railord%l;#;,\ntất cả đều được tiến hành trong trạng thái tháo \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;, tức là trạng thái không khởi động.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;,» → «(Tablet)%l;#;,» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2113 | 「世界中、全ての\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の\x%lタブレット;#00ffc040;タブレット%l;#;は、\nただ一箇所の工場から出荷されていました」 | 「全世界，一切\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的\x%lタブレット;#00ffc040;操作板%l;#;，均產自同一座工廠」 | 「Trên toàn thế giới, \x%lタブレット;#00ffc040;máy tính bảng%l;#; của tất cả các \x%lレイルロオド;#00ffc040;Railord%l;#;,\nđều được xuất xưởng từ một nhà máy duy nhất.」 | 「Trên toàn thế giới, \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; của tất cả các \x%lレイルロオド;#00ffc040;Railord%l;#;,\nđều được xuất xưởng từ một nhà máy duy nhất.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2146 | 「\x%l運転体;#00ffc040;運転体%l;#;からも\x%l整備体;#00ffc040;整備体%l;#;からも\x%lタブレット;#00ffc040;タブレット%l;#;を外し、安置。\nその状態が、もう……かれこれ四年以上になりますかな」 | 「卸下\x%lタブレット;#00ffc040;操作板%l;#;，並與\x%l運転体;#00ffc040;駕駛體%l;#;和\x%l整備体;#00ffc040;整備體%l;#;一同進行了封存處置，掐指算來……迄今已四年有餘」 | 「Tháo \x%lタブレット;#00ffc040;máy tính bảng%l;#; ra khỏi cả \x%l運転体;#00ffc040;thân vận hành%l;#; lẫn \x%l整備体;#00ffc040;thân bảo trì%l;#;, rồi đem đi cất giữ.\nTrạng thái đó, đã……kéo dài được hơn bốn năm rồi thì phải.」 | 「Tháo \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; ra khỏi cả \x%l運転体;#00ffc040;thân vận hành%l;#; lẫn \x%l整備体;#00ffc040;thân bảo trì%l;#;, rồi đem đi cất giữ.\nTrạng thái đó, đã……kéo dài được hơn bốn năm rồi thì phải.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2184 | 「逆算すればいい。『\x%lタブレット;#00ffc040;タブレット%l;#;は、知られすぎると、\n排除される性質をもつ』ということになるだろう？」 | 「只需從結果反推便是。換言之，就是寧肯中止使用\x%lタブレット;#00ffc040;操作板%l;#;，也不可令其廣為人知」 | 「Chỉ cần suy ngược lại là được. Rằng 『\x%lタブレット;#00ffc040;Máy tính bảng%l;#; mang một bản chất\nsẽ bị loại bỏ nếu được biết đến quá rộng rãi』 đúng không?」 | 「Chỉ cần suy ngược lại là được. Rằng 『\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; mang một bản chất\nsẽ bị loại bỏ nếu được biết đến quá rộng rãi』 đúng không?」 | «『\x%lタブレット;#00ffc040;Máy» → «『\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2190 | 「にもかかわらず、\x%lタブレット;#00ffc040;タブレット%l;#;を除去したのならば。\n大廃線の目的は――\x%lタブレット;#00ffc040;タブレット%l;#;を滅ぼすことに」 | 「可現實卻是大多數空凝機導航均沒有安裝\x%lタブレット;#00ffc040;操作板%l;#;。由此可以推斷，大廢線的真正目的在於——銷毀所有\x%lタブレット;#00ffc040;操作板%l;#;」 | 「Vậy mà, nếu như họ đã loại bỏ \x%lタブレット;#00ffc040;máy tính bảng%l;#;.\nThì mục đích của Đại bãi bỏ chính là——tiêu diệt \x%lタブレット;#00ffc040;máy tính bảng%l;#;.」 | 「Vậy mà, nếu như họ đã loại bỏ \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;.\nThì mục đích của Đại bãi bỏ chính là——tiêu diệt \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;.\nThì» → «(Tablet)%l;#;.\nThì»; «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;.」» → «(Tablet)%l;#;.」» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2238 | 「ボディ新造をしようがなにをしようが、\n\x%lタブレット;#00ffc040;タブレット%l;#;は必ず老衰し、やがて、不可避の死を迎える」 | 「哪怕更換身體，亦或是採取其他延壽手段，終究無法避免\x%lタブレット;#00ffc040;操作板%l;#;的衰老乃至死亡」 | 「Dù có chế tạo một cơ thể mới hay làm bất cứ điều gì đi chăng nữa,\n\x%lタブレット;#00ffc040;máy tính bảng%l;#; cũng chắc chắn sẽ già yếu đi, và cuối cùng, sẽ phải đối mặt với cái chết không thể tránh khỏi.」 | 「Dù có chế tạo một cơ thể mới hay làm bất cứ điều gì đi chăng nữa,\n\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; cũng chắc chắn sẽ già yếu đi, và cuối cùng, sẽ phải đối mặt với cái chết không thể tránh khỏi.」 | «nữa,\n\x%lタブレット;#00ffc040;máy» → «nữa,\n\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2416 | 「結構。では、ハチロク氏の\x%lタブレット;#00ffc040;タブレット%l;#;は\n解析・複製させてもらってかまわないかな？」 | 「很好。那麼我需要解析並複製八六女士的\x%lタブレット;#00ffc040;操作板%l;#;，你們對此沒有異議吧？」 | 「Tốt lắm. Vậy thì, tôi có thể tiến hành phân tích và sao chép\n\x%lタブレット;#00ffc040;máy tính bảng%l;#; của cô Hachiroku được chứ?」 | 「Tốt lắm. Vậy thì, tôi có thể tiến hành phân tích và sao chép\n\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; của cô Hachiroku được chứ?」 | «chép\n\x%lタブレット;#00ffc040;máy» → «chép\n\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2493 | 「言い換えるなら、\x%lタブレット;#00ffc040;タブレット%l;#;はただ一箇所――\nいや、より厳密にいうのであれば、恐らくは」 | 「換句話講，就只有一個地方——不，嚴格來講，恐怕是——」 | 「Nói cách khác, \x%lタブレット;#00ffc040;máy tính bảng%l;#; chỉ có ở một nơi duy nhất——\nkhông, nếu nói một cách chính xác hơn, thì có lẽ là」 | 「Nói cách khác, \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; chỉ có ở một nơi duy nhất——\nkhông, nếu nói một cách chính xác hơn, thì có lẽ là」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2507 | 「ならば、\x%lタブレット;#00ffc040;タブレット%l;#;をエアクラナビから\n除去する必要は全くなかった。にもかかわらず」 | 「既然如此，那就更加沒有理由——或者應該說沒有任何理由不為空凝機導航安裝\x%lタブレット;#00ffc040;操作板%l;#;，可現實卻是——」 | 「Nếu vậy, hoàn toàn không cần thiết phải\nloại bỏ \x%lタブレット;#00ffc040;máy tính bảng%l;#; khỏi Navi Aircra. Vậy mà」 | 「Nếu vậy, hoàn toàn không cần thiết phải\nloại bỏ \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; khỏi Navi Aircra. Vậy mà」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2551 | 「さっきもいったが、エアクラナビと\x%lタブレット;#00ffc040;タブレット%l;#;は、\n本来は共存してしかるべきものと考える」 | 「正如剛才所言，我認為按理來說，空凝機導航和\x%lタブレット;#00ffc040;操作板%l;#;原本屬於互惠互利，共同發展的關係」 | 「Như tôi đã nói lúc nãy, Navi Aircra và \x%lタブレット;#00ffc040;máy tính bảng%l;#;,\nvốn dĩ nên là những thứ cùng tồn tại với nhau.」 | 「Như tôi đã nói lúc nãy, Navi Aircra và \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;,\nvốn dĩ nên là những thứ cùng tồn tại với nhau.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;,\nvốn» → «(Tablet)%l;#;,\nvốn» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2564 | 「\x%lタブレット;#00ffc040;タブレット%l;#;に、宿るものなのでしょうか？」 | 「正是源自這\x%lタブレット;#00ffc040;操作板%l;#;是嗎？」 | 「Là thứ trú ngụ bên trong \x%lタブレット;#00ffc040;máy tính bảng%l;#; sao ạ?」 | 「Là thứ trú ngụ bên trong \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; sao ạ?」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2606 | 「けれど、実際には\x%lタブレット;#00ffc040;タブレット%l;#;は排除された。\nどころか、その唯一の供給源も、閉ざされてしまった」 | 「然而結果卻是\x%lタブレット;#00ffc040;操作板%l;#;沒有被採用，甚至連其唯一的供應渠道也被切斷」 | 「Thế nhưng, thực tế là \x%lタブレット;#00ffc040;máy tính bảng%l;#; đã bị loại bỏ.\nThậm chí, nguồn cung cấp duy nhất của nó cũng đã bị đóng lại.」 | 「Thế nhưng, thực tế là \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; đã bị loại bỏ.\nThậm chí, nguồn cung cấp duy nhất của nó cũng đã bị đóng lại.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2636 | 「当然、\x%lレイルロオド;#00ffc040;レイルロオド%l;#;・タブレット社も廃業・解体だ。\n\x%lタブレット;#00ffc040;タブレット%l;#;の製造技術が、完全に途絶したのだからね」 | 「當然生產\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;操作板的公司也只有破產解散。畢竟製造\x%lタブレット;#00ffc040;操作板%l;#;的技術等於已經徹底失傳」 | 「Đương nhiên, công ty \x%lレイルロオド;#00ffc040;Railord%l;#; Tablet cũng bị đóng cửa và giải thể.\nBởi vì công nghệ chế tạo \x%lタブレット;#00ffc040;máy tính bảng%l;#; đã hoàn toàn bị thất truyền.」 | 「Đương nhiên, công ty \x%lレイルロオド;#00ffc040;Railord%l;#; Tablet cũng bị đóng cửa và giải thể.\nBởi vì công nghệ chế tạo \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; đã hoàn toàn bị thất truyền.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2731 | 「第一世代以降には無い機構。\nすなわち、\x%lタブレット;#00ffc040;タブレット%l;#;を内包するエアクラ・ナビ、と」 | 「要說從第一代以後的不同之處，便在於後來的空凝機不再內建\x%lタブレット;#00ffc040;操作板%l;#;」 | 「Một cơ chế không hề có từ thế hệ thứ nhất trở đi.\nNói cách khác, là Navi Aircra có chứa \x%lタブレット;#00ffc040;máy tính bảng%l;#; bên trong.」 | 「Một cơ chế không hề có từ thế hệ thứ nhất trở đi.\nNói cách khác, là Navi Aircra có chứa \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; bên trong.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2866 | 「\x%lタブレット;#00ffc040;タブレット%l;#;を外す前には、稼働していた？」 | 「那她在取下\x%lタブレット;#00ffc040;操作板%l;#;之前依然處於啟動狀態？」 | 「Trước khi tháo \x%lタブレット;#00ffc040;máy tính bảng%l;#; ra, cô ấy vẫn đang hoạt động sao?」 | 「Trước khi tháo \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; ra, cô ấy vẫn đang hoạt động sao?」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 2894 | 「ならば、タブレットレベルとは――文字通り、\n\x%lタブレット;#00ffc040;タブレット%l;#;の中身全て――全領域の\x%l共感;#00ffc040;共感%l;#;、か？」 | 「那麼核心級\x%l共感;#00ffc040;共鳴%l;#;的意思也很明顯，是對包括人偶核——也就是\x%lタブレット;#00ffc040;操作板%l;#;的全部領域實行\x%l共感;#00ffc040;共鳴%l;#;，對嗎？」 | 「Nếu vậy, mức độ mở hoàn toàn là——đúng như nghĩa đen,\ntất cả những gì bên trong \x%lタブレット;#00ffc040;máy tính bảng%l;#;——\x%l共感;#00ffc040;cộng cảm%l;#; toàn bộ lĩnh vực, sao?」 | 「Nếu vậy, mức độ mở hoàn toàn là——đúng như nghĩa đen,\ntất cả những gì bên trong \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;——\x%l共感;#00ffc040;cộng cảm%l;#; toàn bộ lĩnh vực, sao?」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;——\x%l共感;#00ffc040;cộng» → «(Tablet)%l;#;——\x%l共感;#00ffc040;cộng» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 3241 | が、シーリング開放がキーであるなら。\n今は不可能という\x%lタブレット;#00ffc040;タブレット%l;#;の複製なり、創造なりが―― | 但是通過解除封印這一機能，迄今為止對於\x%lタブレット;#00ffc040;操作板%l;#;一直未能實現的複製，乃至於創造，或許就能成為現實—— | Nhưng, nếu việc giải trừ phong ấn là chìa khóa.\nThì việc sao chép, hay sáng tạo ra \x%lタブレット;#00ffc040;máy tính bảng%l;#; vốn được cho là bất khả thi hiện nay—— | Nhưng, nếu việc giải trừ phong ấn là chìa khóa.\nThì việc sao chép, hay sáng tạo ra \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; vốn được cho là bất khả thi hiện nay—— | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク10_旺宮鉄道歴史館.txt.toml | 3266 | ハチロクの指が自分の胸を――\n\x%lタブレット;#00ffc040;タブレット%l;#;の上を、つかむようにして押さえる。 | 八六就若有所思地抓住自己胸口上的\x%lタブレット;#00ffc040;操作板%l;#;，並緊緊按住。 | Những ngón tay của Hachiroku đưa lên trước ngực——\nnhư đang bấu chặt lấy \x%lタブレット;#00ffc040;máy tính bảng%l;#; của mình. | Những ngón tay của Hachiroku đưa lên trước ngực——\nnhư đang bấu chặt lấy \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; của mình. | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク11_御一夜鉄道小畑線.txt.toml | 109 | \x%lタブレット;#00ffc040;タブレット%l;#;――魂は必ず、\n時間とともに不可逆の消耗を重ねていく。 | \x%lタブレット;#00ffc040;操作板%l;#;——其中的靈魂，必然會隨時間流逝而產生、積累不可逆的損耗。 | \x%lタブレット;#00ffc040;Tablet%l;#;——Linh hồn chắc chắn sẽ, \nchịu sự hao mòn không thể đảo ngược theo thời gian. | \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;——Linh hồn chắc chắn sẽ, \nchịu sự hao mòn không thể đảo ngược theo thời gian. | «\x%lタブレット;#00ffc040;Tablet%l;#;——Linh» → «\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;——Linh» |
| ハチロク11_御一夜鉄道小畑線.txt.toml | 1213 | 「\x%lタブレット;#00ffc040;タブレット%l;#;自体は全世界で共通なのだ。\nゆえ、仮に『\x%lレイルロオド;#00ffc040;レイルロオド%l;#;種族説』が真であるなら――」 | 「\x%lタブレット;#00ffc040;操作板%l;#;自身是全世界共通的，所以如果“\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;物種說”真的成立的話——」 | 「Bản thân \x%lタブレット;#00ffc040;Tablet%l;#; là thứ dùng chung trên toàn thế giới. \nVì vậy, giả sử 'thuyết chủng loài \x%lレイルロオド;#00ffc040;Railord%l;#;' là đúng thì——」 | 「Bản thân \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; là thứ dùng chung trên toàn thế giới. \nVì vậy, giả sử 'thuyết chủng loài \x%lレイルロオド;#00ffc040;Railord%l;#;' là đúng thì——」 | «\x%lタブレット;#00ffc040;Tablet%l;#;» → «\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;» |
| ハチロク11_御一夜鉄道小畑線.txt.toml | 1702 | 「だってトーケツホゾンして、オリヴィの\x%lタブレット;#00ffc040;タブレット%l;#;から、オリヴィのコピーみたいの？　つくれたとして」 | 「即便封存了，以後能夠通過奧莉薇的\x%lタブレット;#00ffc040;操作板%l;#;，重新製作一個什麼像是奧莉薇的複製品一樣的東西」 | 「Bởi vì dù có đóng băng bảo quản, rồi từ \x%lタブレット;#00ffc040;Tablet%l;#; của Olivy, tạo ra một bản sao của Olivy đi chăng nữa.」 | 「Bởi vì dù có đóng băng bảo quản, rồi từ \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; của Olivy, tạo ra một bản sao của Olivy đi chăng nữa.」 | «\x%lタブレット;#00ffc040;Tablet%l;#;» → «\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;» |
| ハチロク11_御一夜鉄道小畑線.txt.toml | 1763 | 「あー……うん。ですよね！　\nならキーは、\x%lタブレット;#00ffc040;タブレット%l;#;自体に埋め込まれてるのかも！」 | 「啊……嗯。有道理！所以這關鍵應該還是在\x%lタブレット;#00ffc040;操作板%l;#;自身之中！」 | 「A... ừm. Đúng vậy! \nNếu thế thì chìa khóa có thể đã được nhúng sẵn trong chính \x%lタブレット;#00ffc040;Tablet%l;#; rồi!」 | 「A... ừm. Đúng vậy! \nNếu thế thì chìa khóa có thể đã được nhúng sẵn trong chính \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; rồi!」 | «\x%lタブレット;#00ffc040;Tablet%l;#;» → «\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;» |
| ハチロク11_御一夜鉄道小畑線.txt.toml | 1883 | 「そういうふうに\x%lタブレット;#00ffc040;タブレット%l;#;が役にたっても。そのあと。\nオリヴィ、なにしたらいいのか――わかんなくなりそう」 | 「如果說是以\x%lタブレット;#00ffc040;操作板%l;#;這種方式做出了貢獻的話，那奧莉薇就不知道之後還能做什麼了」 | 「Cho dù \x%lタブレット;#00ffc040;Tablet%l;#; có giúp ích được theo cách đó. Thì sau đó. \nOlivy, có lẽ sẽ không biết——mình nên làm gì nữa.」 | 「Cho dù \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; có giúp ích được theo cách đó. Thì sau đó. \nOlivy, có lẽ sẽ không biết——mình nên làm gì nữa.」 | «\x%lタブレット;#00ffc040;Tablet%l;#;» → «\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;» |
| ハチロク11_御一夜鉄道小畑線.txt.toml | 1915 | 「\x%lレイルロオド;#00ffc040;レイルロオド%l;#;が、種族として作られたかもしれないこと。\n\x%lタブレット;#00ffc040;タブレット%l;#;は繁殖……増殖？　できるかもしれないこと」 | 「就是說\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;可能是作為一個全新的物種被創造出來的。\x%lタブレット;#00ffc040;操作板%l;#;或許可以繁殖……或者說增殖？」 | 「Chuyện \x%lレイルロオド;#00ffc040;Railord%l;#; có thể được tạo ra như một chủng loài. \nChuyện \x%lタブレット;#00ffc040;Tablet%l;#; có thể sinh sản... nhân bản? được ấy.」 | 「Chuyện \x%lレイルロオド;#00ffc040;Railord%l;#; có thể được tạo ra như một chủng loài. \nChuyện \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; có thể sinh sản... nhân bản? được ấy.」 | «\x%lタブレット;#00ffc040;Tablet%l;#;» → «\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;» |
| ハチロク11_御一夜鉄道小畑線.txt.toml | 2251 | 「電車姫様がおっしゃっていた――\n『\x%lタブレット;#00ffc040;タブレット%l;#;からの、ロオドコアの再精錬』」 | 「電車公主殿下所說的——“由\x%lタブレット;#00ffc040;操作板%l;#;二次提取人偶核”」 | 「Ngài Công chúa Tàu điện đã nói—— \n'Việc tinh luyện lại Lõi Lord từ \x%lタブレット;#00ffc040;Tablet%l;#;'」 | 「Ngài Công chúa Tàu điện đã nói—— \n'Việc tinh luyện lại Lõi Lord từ \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;'」 | «\x%lタブレット;#00ffc040;Tablet%l;#;'」» → «\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;'」» |
| ハチロク11_御一夜鉄道小畑線.txt.toml | 2513 | 僕達が走れなくなってしまったとても、\n次の世代に、\x%lタブレット;#00ffc040;タブレット%l;#;を受け渡すことができる。 | 即便將來有一天我們無法繼續馳騁，那也可以將\x%lタブレット;#00ffc040;操作板%l;#;傳承給下一代。 | Cho dù chúng ta không thể chạy được nữa, \nchúng ta vẫn có thể trao lại \x%lタブレット;#00ffc040;Tablet%l;#; cho thế hệ tiếp theo. | Cho dù chúng ta không thể chạy được nữa, \nchúng ta vẫn có thể trao lại \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; cho thế hệ tiếp theo. | «\x%lタブレット;#00ffc040;Tablet%l;#;» → «\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;» |
| ハチロク12_再開発.txt.toml | 2973 | キャブへとハチロクを入れてやる。\nと、すぐにごとりと\x%lタブレット;#00ffc040;タブレット%l;#;を換える音。 | 我把八六抱上了駕駛室。緊接著就聽到了換裝\x%lタブレット;#00ffc040;操作板%l;#;的聲音。 | Tôi bế Hachiroku đặt vào buồng lái.\nNgay sau đó, có tiếng lạch cạch đổi \x%lタブレット;#00ffc040;thẻ bảng%l;#;. | Tôi bế Hachiroku đặt vào buồng lái.\nNgay sau đó, có tiếng lạch cạch đổi \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;. | «\x%lタブレット;#00ffc040;thẻ» → «\x%lタブレット;#00ffc040;Thẻ»; «bảng%l;#;.» → «bảng (Tablet)%l;#;.» |
| ハチロク12_再開発.txt.toml | 3195 | 床に降り立ち、ハチロクは、\n\x%l整備体;#00ffc040;整備体%l;#;へと\x%lタブレット;#00ffc040;タブレット%l;#;を換える。 | 說著，八六從位子上下來，把\x%lタブレット;#00ffc040;操作板%l;#;換裝到了\x%l整備体;#00ffc040;整備體%l;#;上。 | Bước xuống sàn, Hachiroku chuyển \x%lタブレット;#00ffc040;thẻ bảng%l;#; sang \x%l整備体;#00ffc040;thân bảo trì%l;#;. | Bước xuống sàn, Hachiroku chuyển \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; sang \x%l整備体;#00ffc040;thân bảo trì%l;#;. | «\x%lタブレット;#00ffc040;thẻ» → «\x%lタブレット;#00ffc040;Thẻ»; «bảng%l;#;» → «bảng (Tablet)%l;#;» |
| ハチロク13_夜の嵐.txt.toml | 1538 | 「ハチロク、下りるぞ。\n\x%lタブレット;#00ffc040;タブレット%l;#;を換えてくれ」 | 「八六，我們下車了。你把\x%lタブレット;#00ffc040;操作板%l;#;換一下」 | 「Hachiroku, xuống đi. Đổi \x%lタブレット;#00ffc040;thẻ bảng%l;#; cho tôi.」 | 「Hachiroku, xuống đi. Đổi \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; cho tôi.」 | «\x%lタブレット;#00ffc040;thẻ» → «\x%lタブレット;#00ffc040;Thẻ»; «bảng%l;#;» → «bảng (Tablet)%l;#;» |
| ハチロク13_夜の嵐.txt.toml | 2326 | それを見届けハチロクは、\x%lタブレット;#00ffc040;タブレット%l;#;を換え、\n\x%l運転体;#00ffc040;運転体%l;#;に戻って声を引き締める。 | 八六見狀，又將\x%lタブレット;#00ffc040;操作板%l;#;換到了\x%l運転体;#00ffc040;駕駛體%l;#;上，嚴肅地說。 | Thấy vậy, Hachiroku đổi \x%lタブレット;#00ffc040;thẻ bảng%l;#;,\ntrở lại \x%l運転体;#00ffc040;thân vận hành%l;#; và cất giọng nghiêm túc. | Thấy vậy, Hachiroku đổi \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;,\ntrở lại \x%l運転体;#00ffc040;thân vận hành%l;#; và cất giọng nghiêm túc. | «\x%lタブレット;#00ffc040;thẻ» → «\x%lタブレット;#00ffc040;Thẻ»; «bảng%l;#;,\ntrở» → «bảng (Tablet)%l;#;,\ntrở» |
| ハチロク13_夜の嵐.txt.toml | 2328 | それを見届けハチロクは、\n\x%lタブレット;#00ffc040;タブレット%l;#;を外し\x%l運転体;#00ffc040;運転体%l;#;へと。 | 八六見狀，自己取出了\x%lタブレット;#00ffc040;操作板%l;#;換到\x%l運転体;#00ffc040;駕駛體%l;#;上。 | Thấy vậy, Hachiroku\ntháo \x%lタブレット;#00ffc040;thẻ bảng%l;#; ra và chuyển sang \x%l運転体;#00ffc040;thân vận hành%l;#;. | Thấy vậy, Hachiroku\ntháo \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; ra và chuyển sang \x%l運転体;#00ffc040;thân vận hành%l;#;. | «\x%lタブレット;#00ffc040;thẻ» → «\x%lタブレット;#00ffc040;Thẻ»; «bảng%l;#;» → «bảng (Tablet)%l;#;» |
| ハチロク13_夜の嵐.txt.toml | 2336 | ハチロクはすぐ\x%l整備体;#00ffc040;整備体%l;#;へとまた\x%lタブレット;#00ffc040;タブレット%l;#;を入れ替える。\nだったら僕は、またワンスコを握るしか無い。 | 八六馬上又將\x%lタブレット;#00ffc040;操作板%l;#;換到\x%l整備体;#00ffc040;整備體%l;#;身上。看來我又得拿起公斤鍬了。 | Hachiroku lập tức chuyển \x%lタブレット;#00ffc040;thẻ bảng%l;#; về lại \x%l整備体;#00ffc040;thân bảo trì%l;#;.\nVậy thì tôi chỉ còn cách cầm xẻng lên lại thôi. | Hachiroku lập tức chuyển \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; về lại \x%l整備体;#00ffc040;thân bảo trì%l;#;.\nVậy thì tôi chỉ còn cách cầm xẻng lên lại thôi. | «\x%lタブレット;#00ffc040;thẻ» → «\x%lタブレット;#00ffc040;Thẻ»; «bảng%l;#;» → «bảng (Tablet)%l;#;» |
| ハチロク14_冬.txt.toml | 2474 | 「いっても同じ。\nこれ、\x%lタブレット;#00ffc040;タブレット%l;#;がもうボロボロなせいだから」 | 「去哪都一樣，奧莉薇這是因為\x%lタブレット;#00ffc040;操作板%l;#;已經不堪重負了」 | 「Đến đó cũng vậy thôi.\nCái này, là do \x%lタブレット;#00ffc040;máy tính bảng%l;#; đã tơi tả rồi.」 | 「Đến đó cũng vậy thôi.\nCái này, là do \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; đã tơi tả rồi.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク14_冬.txt.toml | 2997 | 「諦めるには早すぎる。例えば明日、\x%lタブレット;#00ffc040;タブレット%l;#;に関する\n新しい知見が発見されるかもしれない」 | 「現在還沒到放棄的時候，說不定明天就會有關於\x%lタブレット;#00ffc040;操作板%l;#;的新發現」 | 「Bỏ cuộc bây giờ là quá sớm. Ví dụ như ngày mai, có thể\nsẽ phát hiện ra kiến thức mới liên quan đến \x%lタブレット;#00ffc040;máy tính bảng%l;#; thì sao.」 | 「Bỏ cuộc bây giờ là quá sớm. Ví dụ như ngày mai, có thể\nsẽ phát hiện ra kiến thức mới liên quan đến \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; thì sao.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク14_冬.txt.toml | 3757 | \x%lタブレット;#00ffc040;タブレット%l;#;の損傷ならば、直せない。\n登呂流湯さんにも、不死鳥博士にも、他の誰にも。 | 如果是\x%lタブレット;#00ffc040;操作板%l;#;的問題，那我們便無計可施，即使換成登呂流浴場老闆和不死鳥博士，或是什麼其他人，都同樣無能為力。 | Nếu là \x%lタブレット;#00ffc040;máy tính bảng%l;#; bị hỏng, thì không thể sửa được.\nCả ông Tororyu-yu, Tiến sĩ Fushicho, hay bất kỳ ai khác cũng vậy. | Nếu là \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; bị hỏng, thì không thể sửa được.\nCả ông Tororyu-yu, Tiến sĩ Fushicho, hay bất kỳ ai khác cũng vậy. | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク15a_痛みとの決別.txt.toml | 2748 | 言語を越えて、\x%lタブレット;#00ffc040;タブレット%l;#;の奥に直接、\n『止まれ』『安全を確保せよ』と、響いてきます。 | 這是超越了語言的命令，直接通過我的\x%lタブレット;#00ffc040;操作板%l;#;命令我“停下來”“確保安全”。 | Vượt qua cả ngôn từ, vang vọng trực tiếp vào sâu bên trong \x%lタブレット;#00ffc040;Tablet%l;#;,\n『Dừng lại』 『Hãy đảm bảo an toàn』. | Vượt qua cả ngôn từ, vang vọng trực tiếp vào sâu bên trong \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;,\n『Dừng lại』 『Hãy đảm bảo an toàn』. | «\x%lタブレット;#00ffc040;Tablet%l;#;,\n『Dừng» → «\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;,\n『Dừng» |
| ハチロク16_春.txt.toml | 1611 | 「『百年以上を走り抜けた\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の\x%lタブレット;#00ffc040;タブレット%l;#;から、\n全く新しいロオドコアが精製された』であったかの？」 | 「似是“從馳騁百年以上的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的\x%lタブレット;#00ffc040;操作板%l;#;中，提取製造出了全新的人偶核”云云？」 | 「Hình như là 『Từ \x%lタブレット;#00ffc040;máy tính bảng%l;#; của một \x%lレイルロオド;#00ffc040;Railord%l;#; đã hoạt động hơn một trăm năm,\nmột Lõi Railord hoàn toàn mới đã được tinh chế ra』 thì phải?」 | 「Hình như là 『Từ \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; của một \x%lレイルロオド;#00ffc040;Railord%l;#; đã hoạt động hơn một trăm năm,\nmột Lõi Railord hoàn toàn mới đã được tinh chế ra』 thì phải?」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク16_春.txt.toml | 1995 | 「無論、手元で育てたくはありました。なにせ貴重な、\n一枚の\x%lタブレット;#00ffc040;タブレット%l;#;からの、ふたつのロオドコアの精製例」 | 「當然，我很想親自撫養她。不管怎麼說，從一塊\x%lタブレット;#00ffc040;操作板%l;#;中提取製造出兩個人偶核，這實在太罕見了」 | 「Tất nhiên là tôi muốn tự tay nuôi dưỡng con bé rồi. Dù sao đây cũng là một trường hợp vô cùng quý giá,\ntinh chế ra hai Lõi Railord từ một \x%lタブレット;#00ffc040;máy tính bảng%l;#; duy nhất cơ mà.」 | 「Tất nhiên là tôi muốn tự tay nuôi dưỡng con bé rồi. Dù sao đây cũng là một trường hợp vô cùng quý giá,\ntinh chế ra hai Lõi Railord từ một \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; duy nhất cơ mà.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク16_春.txt.toml | 2298 | いうなれば、\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の“魂”というべき何物か。\nそれが、オリヴィの\x%lタブレット;#00ffc040;タブレット%l;#;から精製されて―― | 也就是說，它可以稱作\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的“靈魂”。而用奧莉薇的\x%lタブレット;#00ffc040;操作板%l;#;製造而成的話—— | Nói cách khác, nó giống như là “linh hồn” của \x%lレイルロオド;#00ffc040;Railord%l;#; vậy.\nThứ đó, đã được tinh chế từ \x%lタブレット;#00ffc040;máy tính bảng%l;#; của Olivy―― | Nói cách khác, nó giống như là “linh hồn” của \x%lレイルロオド;#00ffc040;Railord%l;#; vậy.\nThứ đó, đã được tinh chế từ \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; của Olivy―― | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ハチロク16_春.txt.toml | 2307 | ロオドコア。\x%lタブレット;#00ffc040;タブレット%l;#;を\x%lタブレット;#00ffc040;タブレット%l;#;たらしめ\n\x%lレイルロオド;#00ffc040;レイルロオド%l;#;を\x%lレイルロオド;#00ffc040;レイルロオド%l;#;たらしめている…… | 人偶核。有了它，\x%lタブレット;#00ffc040;操作板%l;#;才成其為\x%lタブレット;#00ffc040;操作板%l;#;，\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;才成其為\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;…… | Lõi Railord. Thứ làm cho \x%lタブレット;#00ffc040;máy tính bảng%l;#; trở thành \x%lタブレット;#00ffc040;máy tính bảng%l;#;\nlàm cho \x%lレイルロオド;#00ffc040;Railord%l;#; trở thành \x%lレイルロオド;#00ffc040;Railord%l;#;…… | Lõi Railord. Thứ làm cho \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; trở thành \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;\nlàm cho \x%lレイルロオド;#00ffc040;Railord%l;#; trở thành \x%lレイルロオド;#00ffc040;Railord%l;#;…… | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;»; «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;\nlàm» → «(Tablet)%l;#;\nlàm» |
| ハチロク16_春.txt.toml | 2509 | \x%lタブレット;#00ffc040;タブレット%l;#;からの精製は、機能停止後と同義であろうが、\nそうであっても、僕らは、僕らで、未来を繋げる。 | 想要由鐵路人偶的\x%lタブレット;#00ffc040;操作板%l;#;提取製造出新的人偶核，就必須等鐵路人偶停止活動，但即便如此，我們也能讓未來延續下去。 | Việc tinh chế từ \x%lタブレット;#00ffc040;máy tính bảng%l;#; có lẽ đồng nghĩa với việc chức năng đã ngừng hoạt động,\nnhưng dù vậy, chúng tôi vẫn có thể tự mình kết nối với tương lai. | Việc tinh chế từ \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; có lẽ đồng nghĩa với việc chức năng đã ngừng hoạt động,\nnhưng dù vậy, chúng tôi vẫn có thể tự mình kết nối với tương lai. | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| ポーレット04_鳴呼いきストーブ列車.txt.toml | 2076 | 「よめるのー！　たぶれっと！！」 | 「會！\x%lタブレット;#00ffc040;操作板%l;#;！！」 | 「Con đọc được nè~! \x%lタブレット;#00ffc040;máy tính bảng%l;#;!!」 | 「Con đọc được nè~! \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;!!」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;!!」» → «(Tablet)%l;#;!!」» |
| ポーレット11_記憶と記録.txt.toml | 998 | 「\x%lタブレット;#00ffc040;タブレット%l;#;は……記録と同時に、記憶もしてしまう？\nが、脳に近似しているのなら、恐らくプロセッサも――」 | 「\x%lタブレット;#00ffc040;操作板%l;#;在記錄的同時……還會完成記憶？可是，既然處理器與大腦很相似，那恐怕它也——」 | 「\x%lタブレット;#00ffc040;máy tính bảng%l;#……không chỉ ghi chép mà còn ghi nhớ luôn sao? Nhưng nếu nó gần giống với não bộ, thì có lẽ bộ vi xử lý cũng——」 | 「\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#……không chỉ ghi chép mà còn ghi nhớ luôn sao? Nhưng nếu nó gần giống với não bộ, thì có lẽ bộ vi xử lý cũng——」 | «「\x%lタブレット;#00ffc040;máy» → «「\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#……không» → «(Tablet)%l;#……không» |
| ポーレット11_記憶と記録.txt.toml | 1349 | 「\x%lタブレット;#00ffc040;タブレット%l;#;ば交換すれば、\nどん\x%lレイルロオド;#00ffc040;レイルロオド%l;#;も同一の機能ばできるようになる――」 | 「只要更換\x%lタブレット;#00ffc040;操作板%l;#;，任何\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;都能夠擁有相同的功能——」 | 「Chỉ cần thay đổi \x%lタブレット;#00ffc040;máy tính bảng%l;#, thì bất kỳ \x%lレイルロオド;#00ffc040;Railord%l;# nào cũng có thể thực hiện được chức năng tương tự——」 | 「Chỉ cần thay đổi \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#, thì bất kỳ \x%lレイルロオド;#00ffc040;Railord%l;# nào cũng có thể thực hiện được chức năng tương tự——」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#,» → «(Tablet)%l;#,» |
| ポーレット11_記憶と記録.txt.toml | 1528 | 「そういう意味。そうして再び走れるのなら、\n自分の\x%lタブレット;#00ffc040;タブレット%l;#;を[イニシャライズ,2]初期化しても構わない」 | 「是的。如果能夠再一次奔跑，就算將我的\x%lタブレット;#00ffc040;操作板%l;#;初始化也沒關係」 | 「Ý tôi là vậy đấy. Nếu làm vậy mà có thể chạy lại được, thì có [khởi tạo,2]khởi tạo lại \x%lタブレット;#00ffc040;máy tính bảng%l;# của tôi cũng không sao.」 | 「Ý tôi là vậy đấy. Nếu làm vậy mà có thể chạy lại được, thì có [khởi tạo,2]khởi tạo lại \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# của tôi cũng không sao.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#» → «(Tablet)%l;#» |
| ポーレット11_記憶と記録.txt.toml | 1551 | 「例えば、ハチロクの\x%lタブレット;#00ffc040;タブレット%l;#;を\nれいなのボディに換装すると、そのボディは――」 | 「比方說，若將八六的\x%lタブレット;#00ffc040;操作板%l;#;裝入玲奈的機體，那麼那個機體——」 | 「Ví dụ, nếu lắp \x%lタブレット;#00ffc040;máy tính bảng%l;# của Hachiroku vào cơ thể của Reina, thì cơ thể đó sẽ——」 | 「Ví dụ, nếu lắp \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# của Hachiroku vào cơ thể của Reina, thì cơ thể đó sẽ——」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#» → «(Tablet)%l;#» |
| ポーレット11_記憶と記録.txt.toml | 1660 | 「ひょっとして……それが、\x%lタブレット;#00ffc040;タブレット%l;#;ですか？」 | 「莫非……存儲介質就是\x%lタブレット;#00ffc040;操作板%l;#;嗎？」 | 「Không lẽ……đó chính là, \x%lタブレット;#00ffc040;máy tính bảng%l;# sao ạ?」 | 「Không lẽ……đó chính là, \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# sao ạ?」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#» → «(Tablet)%l;#» |
| ポーレット11_記憶と記録.txt.toml | 1724 | 「そうか……冷静に考えれば、れいなくんの\x%lタブレット;#00ffc040;タブレット%l;#;を\nニイロクに実装するのと大差ない」 | 「這樣啊……冷靜下來一想，這基本上等於將玲奈的\x%lタブレット;#00ffc040;操作板%l;#;安裝到二六體內」 | 「Vậy sao……Nghĩ kỹ lại thì, việc này chẳng khác gì cài đặt \x%lタブレット;#00ffc040;máy tính bảng%l;# của cô bé Reina cho Niiroku cả.」 | 「Vậy sao……Nghĩ kỹ lại thì, việc này chẳng khác gì cài đặt \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# của cô bé Reina cho Niiroku cả.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#» → «(Tablet)%l;#» |
| ポーレット11_記憶と記録.txt.toml | 1754 | 「なら、\n他者の\x%lタブレット;#00ffc040;タブレット%l;#;をそこに実装してしまえば――」 | 「那麼，如果為其安裝了他人的\x%lタブレット;#00ffc040;操作板%l;#;——」 | 「Nếu vậy, nếu cài đặt \x%lタブレット;#00ffc040;máy tính bảng%l;# của người khác vào đó thì——」 | 「Nếu vậy, nếu cài đặt \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# của người khác vào đó thì——」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#» → «(Tablet)%l;#» |
| ポーレット11_記憶と記録.txt.toml | 2006 | しかし、\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の\x%lタブレット;#00ffc040;タブレット%l;#;の場合は、\nどうなのだろう？ | 但如果換成\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的\x%lタブレット;#00ffc040;操作板%l;#;，又會怎麼樣呢？ | Tuy nhiên, trong trường hợp \x%lタブレット;#00ffc040;máy tính bảng%l;# của \x%lレイルロオド;#00ffc040;Railord%l;#, thì sẽ thế nào? | Tuy nhiên, trong trường hợp \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# của \x%lレイルロオド;#00ffc040;Railord%l;#, thì sẽ thế nào? | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#» → «(Tablet)%l;#» |
| ポーレット11_記憶と記録.txt.toml | 2085 | 別のボディにその\x%lタブレット;#00ffc040;タブレット%l;#;を換装すれば、\nハチロクは、即座に新しい生を得ることが出来る。 | 只要將\x%lタブレット;#00ffc040;操作板%l;#;更換到其它機體中，八六便能夠重獲新生。 | Nếu lắp \x%lタブレット;#00ffc040;máy tính bảng%l;# đó vào một cơ thể khác, Hachiroku sẽ ngay lập tức có được một cuộc sống mới. | Nếu lắp \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# đó vào một cơ thể khác, Hachiroku sẽ ngay lập tức có được một cuộc sống mới. | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#» → «(Tablet)%l;#» |
| 仲国01_副丘→北琴.txt.toml | 1706 | 「で、ございましょうね。レイルロオドの個体認証なら、\nこれはタブレットが絶対確実でございますから」 | 「似乎確實如此呢。其實要識別鐵路人偶的身份的話，檢查一下操作板就萬無一失了」 | 「Có lẽ là vậy ạ. Nếu là xác thực cá nhân của Railord,\nthì \x%lタブレット;#00ffc040;máy tính bảng%l;#; này mới là thứ chắc chắn tuyệt đối ạ.」 | 「Có lẽ là vậy ạ. Nếu là xác thực cá nhân của Railord,\nthì \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; này mới là thứ chắc chắn tuyệt đối ạ.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| 仲国01_副丘→北琴.txt.toml | 2113 | 「パスポオト。身の安全とタブレットの次に大事で、\n肌身離さず携行するもの」 | 「護照，保證了自身和操作板的安全以後，最重要的就是它了。我一定會片刻不離隨身攜帶」 | 「Hộ chiếu. Là thứ quan trọng thứ ba sau sự an toàn của bản thân và \x%lタブレット;#00ffc040;máy tính bảng%l;#;,\nphải luôn mang theo bên người không được rời nửa bước.」 | 「Hộ chiếu. Là thứ quan trọng thứ ba sau sự an toàn của bản thân và \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;,\nphải luôn mang theo bên người không được rời nửa bước.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;,\nphải» → «(Tablet)%l;#;,\nphải» |
| 共通08_傷跡.txt.toml | 1480 | 「\x%lタブレット;#00ffc040;タブレット%l;#;は……お前の、魂なのか？」 | 「\x%lタブレット;#00ffc040;操作板%l;#;……那是你的靈魂嗎？」 | 「\x%lタブレット;#00ffc040;máy tính bảng%l;#;……là linh hồn của em sao?」 | 「\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;……là linh hồn của em sao?」 | «「\x%lタブレット;#00ffc040;máy» → «「\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;……là» → «(Tablet)%l;#;……là» |
| 共通08_傷跡.txt.toml | 1929 | 「\x%lタブレット;#00ffc040;タブレット%l;#;を交換します。\n驚かないでくださいましね？」 | 「我要交換\x%lタブレット;#00ffc040;操作板%l;#;了。您可不要吃驚哦？」 | 「Em sẽ đổi \x%lタブレット;#00ffc040;máy tính bảng%l;#;.\nNgài đừng ngạc nhiên nhé?」 | 「Em sẽ đổi \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;.\nNgài đừng ngạc nhiên nhé?」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;.\nNgài» → «(Tablet)%l;#;.\nNgài» |
| 共通08_傷跡.txt.toml | 1991 | 「人間の体に例えるのなら、\n\x%lタブレット;#00ffc040;タブレット%l;#;は、脳に近いかとわたくしは」 | 「用人類的身體來比喻的話，我覺得\x%lタブレット;#00ffc040;操作板%l;#;應該更接近於大腦吧」 | 「Nếu so sánh với cơ thể con người,\nthì em nghĩ \x%lタブレット;#00ffc040;máy tính bảng%l;#; giống với bộ não hơn ạ.」 | 「Nếu so sánh với cơ thể con người,\nthì em nghĩ \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; giống với bộ não hơn ạ.」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| 共通08_傷跡.txt.toml | 2836 | （あれが\x%lタブレット;#00ffc040;タブレット%l;#;とやらか？\n交換、とハチロクは言っていたが……） | （那就是\x%lタブレット;#00ffc040;操作板%l;#;嗎？八六說要交換這個……） | （Đó là cái gọi là \x%lタブレット;#00ffc040;máy tính bảng%l;#; sao?\nHachiroku có nói là đổi, nhưng mà……） | （Đó là cái gọi là \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; sao?\nHachiroku có nói là đổi, nhưng mà……） | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| 共通10_クマ川くだりで見る景色.txt.toml | 3376 | \x%lタブレット;#00ffc040;タブレット%l;#;を換装すればジュニアサイズも大きくなるが\nさてその場合、救命胴衣はどう扱われる――おや。 | 若將\x%lタブレット;#00ffc040;操作板%l;#;更換到駕駛體的話，就連兒童救生衣都會顯得太大。那樣的話，不知該穿什麼尺碼的救生衣——哦？ | Nếu đổi \x%lタブレット;#00ffc040;máy tính bảng%l;#; thì size trẻ em cũng sẽ thành to thôi,\nnhưng trong trường hợp đó thì xử lý áo phao thế nào đây――ủa. | Nếu đổi \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; thì size trẻ em cũng sẽ thành to thôi,\nnhưng trong trường hợp đó thì xử lý áo phao thế nào đây――ủa. | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| 共通15_回り始める動輪.txt.toml | 2619 | かちり、\x%lタブレット;#00ffc040;タブレット%l;#;が交換される。\nぱちり、\x%l運転体;#00ffc040;運転体%l;#;のハチロクの目が開く。 | 交換完\x%lタブレット;#00ffc040;操作板%l;#;，八六的\x%l運転体;#00ffc040;駕駛體%l;#;睜開了眼。 | Cạch, \x%lタブレット;#00ffc040;máy tính bảng%l;#; được hoán đổi.\nChớp chớp, đôi mắt của Hachiroku \x%l運転体;#00ffc040;thân vận hành%l;#; mở ra. | Cạch, \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; được hoán đổi.\nChớp chớp, đôi mắt của Hachiroku \x%l運転体;#00ffc040;thân vận hành%l;#; mở ra. | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| 日々姫04_同乗.txt.toml | 2432 | \x%lタブレット;#00ffc040;タブレット%l;#;を換え、小さな運転ボディとなれば、\nハチロクはますます、頼もしくなる。 | 八六交換\x%lタブレット;#00ffc040;操作板%l;#;，換上小小的駕駛體，看起來越來越可靠。 | Khi thay \x%lタブレット;#00ffc040;máy tính bảng%l;#; và trở thành thân vận hành nhỏ bé,\nHachiroku lại càng trở nên đáng tin cậy hơn. | Khi thay \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; và trở thành thân vận hành nhỏ bé,\nHachiroku lại càng trở nên đáng tin cậy hơn. | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| 日々姫14_投開票.txt.toml | 1597 | 「\x%l運転体;#00ffc040;運転体%l;#;へ、\x%lタブレット;#00ffc040;タブレット%l;#;交換はしないのか？」 | 「你不把\x%lタブレット;#00ffc040;操作板%l;#;替換到\x%l運転体;#00ffc040;駕駛體%l;#;上嗎？」 | 「Không đổi \x%lタブレット;#00ffc040;máy tính bảng%l;#; sang \x%l運転体;#00ffc040;thân vận hành%l;#; sao?」 | 「Không đổi \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; sang \x%l運転体;#00ffc040;thân vận hành%l;#; sao?」 | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |
| 日々姫16_夢を乗せて.txt.toml | 2340 | \x%lタブレット;#00ffc040;タブレット%l;#;を手早くはめ替えて、\nハチロクは整備ボディに代わる。 | 八六迅速地替換了\x%lタブレット;#00ffc040;操作板%l;#;，切換到整備體。 | Nhanh chóng thay \x%lタブレット;#00ffc040;máy tính bảng%l;#;, Hachiroku chuyển sang thân bảo trì. | Nhanh chóng thay \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;, Hachiroku chuyển sang thân bảo trì. | «\x%lタブレット;#00ffc040;máy» → «\x%lタブレット;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;,» → «(Tablet)%l;#;,» |

### T51 — 隈元銀行 → "Ngân hàng Kumamoto" (2 dòng)

| File | Key | JP | TW | old_vn | fix | Đổi |
|---|---|---|---|---|---|---|
| 稀咲02_新事業案.txt.toml | 2649 | 隈元銀行の支店長で、日々姫の先輩で恩人で。\nけど、それ以前に――宝生稀咲は、少女なのだと。 | 她是隈元銀行的支行行長，是日日姬的學姐和恩人。但更根本地說——寶生稀咲是一位少女。 | Là giám đốc chi nhánh của Kumagin, là tiền bối và ân nhân của Hibiki.\nNhưng trước những điều đó——Houshou Kisaki, là một thiếu nữ. | Là giám đốc chi nhánh Ngân hàng Kumamoto, là tiền bối và ân nhân của Hibiki.\nNhưng trước những điều đó——Houshou Kisaki, là một thiếu nữ. | «của» → «Ngân»; «Kumagin,» → «hàng Kumamoto,» |
| 稀咲03_純白のレール.txt.toml | 2713 | なにせ稀咲は隈元銀行御一夜支店の、\n誰もが認める優れたリーダーなのだから。 | 畢竟稀咲本人可是人人都認可的隈元銀行御一夜支行的優秀領導。 | Dù sao thì Kisaki cũng là một nhà lãnh đạo xuất sắc được mọi người công nhận của Kumagin chi nhánh Ohitoyo mà. | Dù sao thì Kisaki cũng là một nhà lãnh đạo xuất sắc được mọi người công nhận của Ngân hàng Kumamoto chi nhánh Ohitoyo mà. | «Kumagin» → «Ngân hàng Kumamoto» |

### T52 — 帝都 → "Đế đô" (20 dòng)

| File | Key | JP | TW | old_vn | fix | Đổi |
|---|---|---|---|---|---|---|
| グランドリライト06_稀咲.txt.toml | 1841 | 「さすがにいきなり帝都は無理さ。比較して\n遥かに条件のいい九洲で、ようやくどうかな案だから」 | 「一上來就在帝都實施肯定行不通。而相較之下條件遠遠好得多的九州，終於提出了一個不錯的方案」 | 「Đột ngột nhảy vào Teito thì chắc chắn là không thể rồi. Ngay cả ở Kyushu với điều kiện tốt hơn hẳn,\nphương án này cũng chỉ mới ở mức có thể xem xét thôi.」 | 「Đột ngột nhảy vào Đế đô thì chắc chắn là không thể rồi. Ngay cả ở Kyushu với điều kiện tốt hơn hẳn,\nphương án này cũng chỉ mới ở mức có thể xem xét thôi.」 | «Teito» → «Đế đô» |
| グランドリライト06_稀咲.txt.toml | 1923 | 「しかし……帝都の大会社から、御一夜鉄道にというのは、\n僕の立場でいうのも何だが」 | 「但是……要從帝都的大公司轉到御一夜鐵路這種地方，以我的立場來說也有些……」 | 「Nhưng……chuyển từ một công ty lớn ở Teito sang Đường sắt Ohitoyo,\ndù nói ra từ lập trường của tôi thì cũng hơi...」 | 「Nhưng……chuyển từ một công ty lớn ở Đế đô sang Đường sắt Ohitoyo,\ndù nói ra từ lập trường của tôi thì cũng hơi...」 | «Teito» → «Đế đô» |
| グランドリライト06_稀咲.txt.toml | 2113 | 「うん。後東氏が帝都で類似事業を成功させたいなら、\nこの着地点が、一番安全確実だから」 | 「嗯。如果後東先生想在帝都辦成類似的企劃，這樣收尾是最安全可靠的」 | 「Vâng. Nếu ông Goto muốn thực hiện thành công một dự án tương tự ở Teito,\nthì điểm dừng này là an toàn và chắc chắn nhất.」 | 「Vâng. Nếu ông Goto muốn thực hiện thành công một dự án tương tự ở Đế đô,\nthì điểm dừng này là an toàn và chắc chắn nhất.」 | «Teito,\nthì» → «Đế đô,\nthì» |
| グランドリライト06_稀咲.txt.toml | 2208 | 「[ねづう,1]禰通氏。[つづみ]鼓氏。\n――後東氏以上がごろごろいるのが、帝都だからね」 | 「帝都還有祢通先生、鼓先生。那裡比後東先生勢力更大的人物數不勝數」 | 「Ông Nezu. Ông Tsutsumi.\n――Bởi vì ở Teito nhan nhản những kẻ máu mặt hơn cả ông Goto mà.」 | 「Ông Nezu. Ông Tsutsumi.\n――Bởi vì ở Đế đô nhan nhản những kẻ máu mặt hơn cả ông Goto mà.」 | «Teito» → «Đế đô» |
| グランドリライト06_稀咲.txt.toml | 2519 | 「――帝都でいきなりでは、失敗するか」 | 「直接在帝都辦就會失敗嗎？」 | 「――Đột ngột triển khai ở Teito thì sẽ thất bại sao?」 | 「――Đột ngột triển khai ở Đế đô thì sẽ thất bại sao?」 | «Teito» → «Đế đô» |
| グランドリライト06_稀咲.txt.toml | 2702 | 「ありえないかと。帝都ではこの事業案が成立する余地が、\n限りなく小さくなりますから」 | 「那怎麼可能。要在帝都實施這個企劃案，成功率微乎其微」 | 「Chuyện đó là không thể nào. Khả năng dự án này thành công ở Teito\nlà vô cùng nhỏ bé.」 | 「Chuyện đó là không thể nào. Khả năng dự án này thành công ở Đế đô\nlà vô cùng nhỏ bé.」 | «Teito\nlà» → «Đế đô\nlà» |
| ハチロク03_冥国式レイルロオド.txt.toml | 2290 | 「帝都育ちだ。……そんな経験もないだろうに。\nあるいは、どこかで訓練を受けたことがあるのか」 | 「她出身帝都，按說不太會有這樣的經驗才對。還是說在哪裡受過這樣的訓練呢」 | 「Cô ấy lớn lên ở Đế Đô mà.……Chắc hẳn chưa từng có kinh nghiệm như vậy.\nHay là cô ấy đã được huấn luyện ở đâu đó rồi nhỉ.」 | 「Cô ấy lớn lên ở Đế đô mà.……Chắc hẳn chưa từng có kinh nghiệm như vậy.\nHay là cô ấy đã được huấn luyện ở đâu đó rồi nhỉ.」 | «Đô» → «đô» |
| ハチロク04_小畑越え.txt.toml | 3226 | ロングシートも、帝都を思い出して嫌いではない。\nが、御一夜から小畑を越えて早戸へと―― | 雖然對於豎排座位，抑或由此勾起的在帝都時的回憶，我都並不牴觸，但是從御一夜出發越過大畑前往隼人—— | Ghế dài dọc theo xe gợi nhớ đến Đế Đô nên tôi cũng không ghét.\nNhưng đi từ Ohitoyo qua đèo Okoba đến Hayato—— | Ghế dài dọc theo xe gợi nhớ đến Đế đô nên tôi cũng không ghét.\nNhưng đi từ Ohitoyo qua đèo Okoba đến Hayato—— | «Đô» → «đô» |
| ハチロク09_もくもくオリヴィ.txt.toml | 2028 | 「そのっ――帝都ではどうだった？\n帝鉄時代は、どんな見事な車窓を見ていた？」 | 「說起來——帝都是怎麼樣的呢？你在帝國鐵路時代從車窗外看到的又是怎樣美妙的景色呢？」 | 「Cái đó——ở Đế Đô thì sao?\nThời Teitetsu, em đã từng nhìn thấy những cảnh sắc tuyệt vời nào qua cửa sổ?」 | 「Cái đó——ở Đế đô thì sao?\nThời Teitetsu, em đã từng nhìn thấy những cảnh sắc tuyệt vời nào qua cửa sổ?」 | «Đô» → «đô» |
| ハチロク12_ムナカタ来訪.txt.toml | 2091 | 「今はみかん鉄道様の[せんだい,1]千内－[やつしろ,2]八ツ城を含む旧鹿兒島本線と、\n旧[ひさつ,1]肥颯線との関係は、帝都まわりで申しましたら」 | 「而現在橙鐵路包含川內至八代路段的前鹿兒島本線與前肥薩線的關係，單從帝都周邊的路段而言」 | 「Mối quan hệ giữa Tuyến chính Kagoshima cũ (hiện tại bao gồm đoạn Sendai - Yatsushiro của Đường sắt Mikan) \nvà Tuyến Hisatsu cũ, nếu so sánh với khu vực thủ đô thì」 | 「Mối quan hệ giữa Tuyến chính Kagoshima cũ (hiện tại bao gồm đoạn Sendai - Yatsushiro của Đường sắt Mikan) \nvà Tuyến Hisatsu cũ, nếu so sánh với khu vực Đế đô thì」 | «thủ» → «Đế» |
| 仲国06_聖都とパンダとハチロクと.txt.toml | 1435 | 「大変に残念ですが、明々後日、帰国予定日の\n翌日には、ポーレット様に帝都での会合のご予定が」 | 「但著實遺憾，大後天，也就是按計劃回國後的一天，波萊特大人已有了在帝都的會見安排」 | 「Rất tiếc, nhưng ngày kia, tức là một ngày sau ngày dự định về nước,\nThị trưởng Paulette đã có lịch họp ở Đế Đô rồi ạ.」 | 「Rất tiếc, nhưng ngày kia, tức là một ngày sau ngày dự định về nước,\nThị trưởng Paulette đã có lịch họp ở Đế đô rồi ạ.」 | «Đô» → «đô» |
| 共通03_ハチロクとナビ.txt.toml | 1320 | 「そういう話だ。\n僕は、それを食い止めたいと帝都から戻ってきた」 | 「就是這個問題。我從帝都回來也就是因為不想事態發展成那樣」 | 「Là chuyện đó đấy.\nTôi từ Đế Đô trở về là để ngăn chặn điều đó.」 | 「Là chuyện đó đấy.\nTôi từ Đế đô trở về là để ngăn chặn điều đó.」 | «Đô» → «đô» |
| 共通03_ハチロクとナビ.txt.toml | 1516 | 「なのになぜ、帝都の僕にまで届くほど――\n\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致活動が活発になってしまったのだ？」 | 「然而為什麼，引進\x%lエアクラ;#00ffc040;空凝機%l;#;工廠的事情會鬧到連身在帝都的我都知道了呢？」 | 「Nhưng tại sao, nó lại lan đến tận chỗ tôi ở Đế Đô——\nChiến dịch thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; lại trở nên rầm rộ đến vậy?」 | 「Nhưng tại sao, nó lại lan đến tận chỗ tôi ở Đế đô——\nChiến dịch thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; lại trở nên rầm rộ đến vậy?」 | «Đô——\nChiến» → «đô——\nChiến» |
| 共通09_さきだつもの.txt.toml | 2669 | 「右田の長男さんいうたら、\n帝都にいかれたいう話でしょう」 | 「要說到右田家的長男，我聽說不是去帝都上學了嗎」 | 「Nghe nói con cả nhà Migita,\nđã lên Đế Đô rồi cơ mà.」 | 「Nghe nói con cả nhà Migita,\nđã lên Đế đô rồi cơ mà.」 | «Đô» → «đô» |
| 凪ふかみ06_凪の欲しいもの.txt.toml | 1800 | 「ああ、帝都の[はりい,1]鍼医にならったことがあるのだ。\n疲れを見るには、ここ――」 | 「哦，這是我從帝都的針灸醫生那學來的。要看疲勞程度就按這裡」 | 「À, anh từng học được từ một thầy châm cứu ở Đế Đô.\nĐể xem mức độ mệt mỏi thì ấn vào đây——」 | 「À, anh từng học được từ một thầy châm cứu ở Đế đô.\nĐể xem mức độ mệt mỏi thì ấn vào đây——」 | «Đô.\nĐể» → «đô.\nĐể» |
| 凪ふかみ06_凪の欲しいもの.txt.toml | 2142 | 「予想より遥かになめらかだ。\nまるで、帝都生まれの帝都育ちの者の言葉と聞こえるぞ」 | 「超乎想像的流暢啊。簡直就是土生土長帝都人的口音」 | 「Trôi chảy hơn anh tưởng nhiều đấy.\nNghe cứ như lời của một người sinh ra và lớn lên ở Đế Đô vậy.」 | 「Trôi chảy hơn anh tưởng nhiều đấy.\nNghe cứ như lời của một người sinh ra và lớn lên ở Đế đô vậy.」 | «Đô» → «đô» |
| 日々姫04_カフェキッチン.txt.toml | 2134 | 「はい。帝都の製菓学校で勉強してホテルの厨房で働いて。\nそれから[ほうしょう,1]宝生先輩にひっぱられて、ここに」 | 「是的。我曾經在帝都的糕點學校就讀，畢業後在賓館的廚房工作，然後被寶生前輩挖角來到了這裡」 | 「Vâng. Tôi đã học ở trường làm bánh kẹo trên thủ đô, rồi làm việc trong bếp của khách sạn.\nSau đó bị tiền bối Houshou kéo đến đây.」 | 「Vâng. Tôi đã học ở trường làm bánh kẹo ở Đế đô, rồi làm việc trong bếp của khách sạn.\nSau đó bị tiền bối Houshou kéo đến đây.」 | «trên» → «ở»; «thủ» → «Đế» |
| 日々姫05_市議会見学.txt.toml | 2470 | が、僕とて料理が嫌いではない。\n帝都で一人暮らしのころは、あれこれと工夫もしたものだ。 | 但我卻不討厭做飯。在帝都一個人生活的時候，我也下了不少功夫。 | Nhưng tôi cũng không ghét việc nấu ăn.\nHồi còn sống một mình trên thủ đô, tôi cũng từng mày mò đủ món. | Nhưng tôi cũng không ghét việc nấu ăn.\nHồi còn sống một mình ở Đế đô, tôi cũng từng mày mò đủ món. | «trên» → «ở»; «thủ» → «Đế» |
| 日々姫05_市議会見学.txt.toml | 2701 | 標準語とか、帝都とか。それはやっぱり憧れだけど、\n御一夜には御一夜の面白さがある。 | 普通話也好，帝都也好，這些確實很讓人嚮往，不過御一夜也有御一夜的樂趣。 | Tiếng phổ thông, hay thủ đô. Những thứ đó quả thực rất đáng ngưỡng mộ,\nnhưng Ohitoyo cũng có những điều thú vị riêng của Ohitoyo. | Tiếng phổ thông, hay Đế đô. Những thứ đó quả thực rất đáng ngưỡng mộ,\nnhưng Ohitoyo cũng có những điều thú vị riêng của Ohitoyo. | «thủ» → «Đế» |
| 真闇h3_補習授業の廃校舎.txt.toml | 3299 | 学園時代も、帝都に引っ越し帝大に進学してのちも、\n指示されたことをただこなしていただけだった。 | 學生時代啊，搬去帝都上帝大啊，我都是聽命行事而已。 | Dù là thời còn đi học, hay sau khi chuyển đến Đế Đô học Đại học Hoàng gia,\ntôi cũng chỉ biết làm theo những gì được bảo. | Dù là thời còn đi học, hay sau khi chuyển đến Đế đô học Đại học Hoàng gia,\ntôi cũng chỉ biết làm theo những gì được bảo. | «Đô» → «đô» |

### G1 — 列車 gloss → "đoàn tàu" (121 dòng)

| File | Key | JP | TW | old_vn | fix | Đổi |
|---|---|---|---|---|---|---|
| れいな01_炭鉱探索.txt.toml | 1784 | 「そおですねぇ。鉱山で\x%l列車;#00ffc040;列車%l;#;っていったら貨物ですから。\n人だけを運ぶのは、特別に人車って呼ぶんです」 | 「是呀。因為礦山的\x%l列車;#00ffc040;列車%l;#;都是用來運貨的，所以才將專門運人的車輛區分開來，稱作“人車”」 | 「Dạ đúng rồi~. Ở mỏ thì \x%l列車;#00ffc040;tàu%l;#; là để chở hàng hóa mà.\nNên loại chỉ dùng để chở người thì được gọi đặc biệt là xe goòng chở người ạ.」 | 「Dạ đúng rồi~. Ở mỏ thì \x%l列車;#00ffc040;đoàn tàu%l;#; là để chở hàng hóa mà.\nNên loại chỉ dùng để chở người thì được gọi đặc biệt là xe goòng chở người ạ.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| れいな01_炭鉱探索.txt.toml | 1788 | 「そおですねぇ、体験採掘で掘った石炭を\x%l貨車;#00ffc040;貨車%l;#;につむなら、\nそれも立派な、混合\x%l列車;#00ffc040;列車%l;#;になるってれいな、思いますぅ」 | 「是呀。玲奈覺得，如果要將採煤體驗中採到的煤炭裝進\x%l貨車;#00ffc040;貨運車廂%l;#;，那麼就完全稱得上是混合\x%l列車;#00ffc040;列車%l;#;了」 | 「Dạ đúng rồi~, nếu chất than đào được từ trải nghiệm khai thác lên \x%l貨車;#00ffc040;toa chở hàng%l;#;,\nthì nó cũng trở thành một \x%l列車;#00ffc040;tàu%l;#; hỗn hợp đàng hoàng đó ạ, Reina nghĩ vậy~」 | 「Dạ đúng rồi~, nếu chất than đào được từ trải nghiệm khai thác lên \x%l貨車;#00ffc040;toa chở hàng%l;#;,\nthì nó cũng trở thành một \x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp đàng hoàng đó ạ, Reina nghĩ vậy~」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| れいな01_炭鉱探索.txt.toml | 1794 | 「ですねぇ。[かたがみ,1]硬上ではふつーのことでした。\n[ていてつ,1]帝鉄さんだと、混合\x%l列車;#00ffc040;列車%l;#;とかいったみたいですねぇ」 | 「是呀。這在片上礦山是很常見的。聽說帝國鐵路將其稱為混合\x%l列車;#00ffc040;列車%l;#;」 | 「Dạ đúng rồi~. Ở mỏ Katakami thì đó là chuyện bình thường ạ.\nBên Teitetsu thì hình như gọi là \x%l列車;#00ffc040;tàu%l;#; hỗn hợp hay sao ấy ạ~」 | 「Dạ đúng rồi~. Ở mỏ Katakami thì đó là chuyện bình thường ạ.\nBên Teitetsu thì hình như gọi là \x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp hay sao ấy ạ~」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| れいな01_炭鉱探索.txt.toml | 1849 | 「機械、人員、設備維持――\x%l列車;#00ffc040;列車%l;#;収入など焼け石に水だな。\nこれは、もし助成金が打ち切りになりでもしたら」 | 「機器、人員、設備維護——\x%l列車;#00ffc040;列車%l;#;的收入根本是杯水車薪啊。如果哪一天，國家停止下撥補助金——」 | 「Máy móc, nhân sự, bảo trì thiết bị――doanh thu từ \x%l列車;#00ffc040;tàu%l;#; chỉ như muối bỏ bể thôi.\nThế này, lỡ như trợ cấp bị cắt thì sao.」 | 「Máy móc, nhân sự, bảo trì thiết bị――doanh thu từ \x%l列車;#00ffc040;đoàn tàu%l;#; chỉ như muối bỏ bể thôi.\nThế này, lỡ như trợ cấp bị cắt thì sao.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| れいな01_炭鉱探索.txt.toml | 1877 | 「混合\x%l列車;#00ffc040;列車%l;#;か、面白そうだな。というか、ああ、いや……\nマイントレジャーでやるのも、いわば」 | 「混合\x%l列車;#00ffc040;列車%l;#;嗎，聽起來很有趣。話說回來……啊，我們的煤探樂園，其實也是——」 | 「\x%l列車;#00ffc040;Tàu%l;#; hỗn hợp à, nghe thú vị đấy. Mà khoan, à, không...\nViệc chúng ta làm ở Mine Treasure, nói cách khác thì...」 | 「\x%l列車;#00ffc040;Đoàn tàu%l;#; hỗn hợp à, nghe thú vị đấy. Mà khoan, à, không...\nViệc chúng ta làm ở Mine Treasure, nói cách khác thì...」 | «「\x%l列車;#00ffc040;Tàu%l;#;» → «「\x%l列車;#00ffc040;Đoàn tàu%l;#;» |
| れいな01_炭鉱探索.txt.toml | 2016 | 「となると、混合\x%l列車;#00ffc040;列車%l;#;という名称を使うべきかもしれんな。\n物珍しく、観光気分が高まりそうだ」 | 「那麼，我們或許應該用上混合\x%l列車;#00ffc040;列車%l;#;這一名稱。有種稀奇的感覺，應該能烘托觀光的氛圍」 | 「Nếu vậy, có lẽ chúng ta nên sử dụng cái tên \x%l列車;#00ffc040;tàu%l;#; hỗn hợp.\nNghe có vẻ mới lạ, chắc chắn sẽ làm tăng thêm không khí du lịch đấy.」 | 「Nếu vậy, có lẽ chúng ta nên sử dụng cái tên \x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp.\nNghe có vẻ mới lạ, chắc chắn sẽ làm tăng thêm không khí du lịch đấy.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| れいな02_れいなとポーレット.txt.toml | 1182 | ……ああ。そうか。ひょっとして世代的に、\n凪あたりはもう、貨物\x%l列車;#00ffc040;列車%l;#;を知らんのかもしれん。 | ……啊，原來如此。或許像凪這個年紀的孩子已經不知道什麼是貨運\x%l列車;#00ffc040;列車%l;#;了。 | ……À. Ra vậy. Có lẽ do khoảng cách thế hệ,\nnhững đứa trẻ như Nagi đã không còn biết đến \x%l列車;#00ffc040;tàu%l;#; chở hàng nữa rồi. | ……À. Ra vậy. Có lẽ do khoảng cách thế hệ,\nnhững đứa trẻ như Nagi đã không còn biết đến \x%l列車;#00ffc040;đoàn tàu%l;#; chở hàng nữa rồi. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| れいな02_れいなとポーレット.txt.toml | 1856 | 「帝都で最も栄えた環状線。[やまのて,2]山之手線においては、\n二分に一本、休むことなく\x%l列車;#00ffc040;列車%l;#;は走っておりました」 | 「帝都最繁榮的環狀線——山手線，每兩分鐘就有一班\x%l列車;#00ffc040;列車%l;#;發車，正可謂川流不息」 | 「Tuyến đường vòng sầm uất nhất Đế đô. Ở tuyến Yamanote,\ncứ hai phút lại có một chuyến \x%l列車;#00ffc040;tàu%l;#; chạy không ngừng nghỉ ạ.」 | 「Tuyến đường vòng sầm uất nhất Đế đô. Ở tuyến Yamanote,\ncứ hai phút lại có một chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; chạy không ngừng nghỉ ạ.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| れいな02_れいなとポーレット.txt.toml | 1955 | 「ええ。その上で、\n旅客線路を貨物\x%l列車;#00ffc040;列車%l;#;が走ることも、よくありました」 | 「是的。並且，貨運\x%l列車;#00ffc040;列車%l;#;也經常會在客運線路上行駛」 | 「Đúng vậy. Ngoài ra,\n\x%l列車;#00ffc040;tàu%l;#; chở hàng chạy trên tuyến chở khách cũng là chuyện thường xuyên xảy ra.」 | 「Đúng vậy. Ngoài ra,\n\x%l列車;#00ffc040;đoàn tàu%l;#; chở hàng chạy trên tuyến chở khách cũng là chuyện thường xuyên xảy ra.」 | «ra,\n\x%l列車;#00ffc040;tàu%l;#;» → «ra,\n\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| れいな02_れいなとポーレット.txt.toml | 2127 | 「貨物\x%l列車;#00ffc040;列車%l;#;と一緒ばい！？\nそん\x%l客車;#00ffc040;客車%l;#;、なんかとっても面白そうばい！！」 | 「跟貨運\x%l列車;#00ffc040;列車%l;#;一起！？這樣的\x%l客車;#00ffc040;客運車廂%l;#;聽起來好好玩咧！！」 | 「Đi cùng với \x%l列車;#00ffc040;tàu%l;#; chở hàng luôn nè!?\n\x%l客車;#00ffc040;Toa hành khách%l;#; như thế, nghe có vẻ thú vị quá nè!!」 | 「Đi cùng với \x%l列車;#00ffc040;đoàn tàu%l;#; chở hàng luôn nè!?\n\x%l客車;#00ffc040;Toa hành khách%l;#; như thế, nghe có vẻ thú vị quá nè!!」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| れいな03_しゅっぱつしんこう.txt.toml | 1455 | 「はい。今までのように、全ての\x%l列車;#00ffc040;列車%l;#;が御一夜に帰着して\n一日を終えるとは限らなくなりますから」 | 「嗯，因為到時候就不一定能像之前那樣所有的\x%l列車;#00ffc040;列車%l;#;都在一天結束前回到御一夜了」 | 「Vâng ạ. Vì sẽ không còn chuyện tất cả các \x%l列車;#00ffc040;tàu%l;#; đều trở về Ohitoyo\nđể kết thúc một ngày như trước đây nữa.」 | 「Vâng ạ. Vì sẽ không còn chuyện tất cả các \x%l列車;#00ffc040;đoàn tàu%l;#; đều trở về Ohitoyo\nđể kết thúc một ngày như trước đây nữa.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| れいな03_しゅっぱつしんこう.txt.toml | 2376 | ならば八ツ城行きの混合\x%l列車;#00ffc040;列車%l;#;も、\n日々姫が持っていくこととなる。 | 那開往八代的混合\x%l列車;#00ffc040;列車%l;#;也要由日日姬去駕駛了。 | Nếu vậy thì \x%l列車;#00ffc040;tàu%l;#; hỗn hợp đi Yatsushiro,\ncũng sẽ do Hibiki phụ trách. | Nếu vậy thì \x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp đi Yatsushiro,\ncũng sẽ do Hibiki phụ trách. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ニイロク04_終端.txt.toml | 1593 | 「いいえ。けれど、列車を止めることは許されません。\n解体処分をされる[もじ,1]門次まで――、一直線です」 | 「不會。但是，誰都不可以停下列車。列車要直接開到進行拆解處理的門司」 | 「Không. Tuy nhiên, không được phép dừng \x%l列車;#00ffc040;tàu%l;#; lại.\nCho đến tận Moji, nơi sẽ tiến hành tháo dỡ——, là đi thẳng một mạch.」 | 「Không. Tuy nhiên, không được phép dừng \x%l列車;#00ffc040;đoàn tàu%l;#; lại.\nCho đến tận Moji, nơi sẽ tiến hành tháo dỡ——, là đi thẳng một mạch.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク01_双鉄の目・ハチロクの目.txt.toml | 1780 | 「あー、\x%l列車;#00ffc040;列車%l;#;ってこの構図だとここまで絵になるとね。\n勉強になる」 | 「哦～\x%l列車;#00ffc040;列車%l;#;這樣構圖竟然可以這麼和諧。真是學到了」 | 「A, \x%l列車;#00ffc040;tàu%l;#; mà chụp góc này thì lên hình đẹp đến mức này luôn á.\nHọc hỏi được nhiều rồi đây.」 | 「A, \x%l列車;#00ffc040;đoàn tàu%l;#; mà chụp góc này thì lên hình đẹp đến mức này luôn á.\nHọc hỏi được nhiều rồi đây.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク02_8620運転台通信.txt.toml | 2034 | 「なれば、一度きりのイベント\x%l列車;#00ffc040;列車%l;#;として遊びに参れ――\nという意味であるとしておこうぞ」 | 「既然如此——讓其作為一次性活動的特別\x%l列車;#00ffc040;列車%l;#;前來便可」 | 「Vậy thì, hãy đến chơi như một chuyến \x%l列車;#00ffc040;tàu%l;#; sự kiện chỉ có một lần duy nhất——\nHãy coi ý ta là như vậy đi.」 | 「Vậy thì, hãy đến chơi như một chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; sự kiện chỉ có một lần duy nhất——\nHãy coi ý ta là như vậy đi.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク02_8620運転台通信.txt.toml | 2645 | 言葉が、固着していた記憶を揺する。\n……幼い頃に、路子と一緒に\x%l列車;#00ffc040;列車%l;#;に乗った、あのワクワク。 | 我自言自語中的一字一句動搖著我心中凝固的記憶。……我想起了小時候，和路子一起乘坐\x%l列車;#00ffc040;列車%l;#;時那顆躍動的心。 | Những lời nói làm lay động ký ức vốn đã in sâu trong tôi.\n……Sự háo hức khi cùng Michiko đi \x%l列車;#00ffc040;tàu%l;#; hồi còn nhỏ. | Những lời nói làm lay động ký ức vốn đã in sâu trong tôi.\n……Sự háo hức khi cùng Michiko đi \x%l列車;#00ffc040;đoàn tàu%l;#; hồi còn nhỏ. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク03_客車試験.txt.toml | 1369 | 「\x%l客車;#00ffc040;客車%l;#;。\n……\x%l列車;#00ffc040;列車%l;#;か」 | 「\x%l客車;#00ffc040;客運車廂%l;#;……\x%l列車;#00ffc040;列車%l;#;啊」 | 「\x%l客車;#00ffc040;Toa hành khách%l;#;.\n……\x%l列車;#00ffc040;Tàu%l;#; à.」 | 「\x%l客車;#00ffc040;Toa hành khách%l;#;.\n……\x%l列車;#00ffc040;Đoàn tàu%l;#; à.」 | «khách%l;#;.\n……\x%l列車;#00ffc040;Tàu%l;#;» → «khách%l;#;.\n……\x%l列車;#00ffc040;Đoàn tàu%l;#;» |
| ハチロク03_客車試験.txt.toml | 1882 | 「うん、涼しい。貸し切り\x%l列車;#00ffc040;列車%l;#;の特権ね」 | 「嗯，涼快。這是包下整列\x%l列車;#00ffc040;列車%l;#;的特權吧」 | 「Ừm, mát thật. Đặc quyền của việc bao trọn \x%l列車;#00ffc040;tàu%l;#; nhỉ.」 | 「Ừm, mát thật. Đặc quyền của việc bao trọn \x%l列車;#00ffc040;đoàn tàu%l;#; nhỉ.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク03_客車試験.txt.toml | 2682 | しまったカメラを、また取り出さずにいられなくなる。\n\x%l列車;#00ffc040;列車%l;#;――とは、良く言ったものだとつくづく感じる。 | 我不由自主地從口袋裡又把相機拿了出來。\x%l列車;#00ffc040;列車%l;#;這個稱呼，還真是讓人覺得頗有道理。 | Tôi không kìm được mà lấy lại chiếc máy ảnh vừa cất đi.\n\x%l列車;#00ffc040;Tàu%l;#;——tôi thực sự cảm thấy cái tên này thật chí lý. | Tôi không kìm được mà lấy lại chiếc máy ảnh vừa cất đi.\n\x%l列車;#00ffc040;Đoàn tàu%l;#;——tôi thực sự cảm thấy cái tên này thật chí lý. | «đi.\n\x%l列車;#00ffc040;Tàu%l;#;——tôi» → «đi.\n\x%l列車;#00ffc040;Đoàn tàu%l;#;——tôi» |
| ハチロク03_客車試験.txt.toml | 2732 | 列になって、繋がってこそ、はじめて“\x%l列車;#00ffc040;列車%l;#;”。 | 排成一列，首尾相連，方才成為“\x%l列車;#00ffc040;列車%l;#;”。 | Phải xếp thành hàng, kết nối với nhau, thì mới thành "\x%l列車;#00ffc040;Tàu%l;#;". | Phải xếp thành hàng, kết nối với nhau, thì mới thành "\x%l列車;#00ffc040;Đoàn tàu%l;#;". | «"\x%l列車;#00ffc040;Tàu%l;#;".» → «"\x%l列車;#00ffc040;Đoàn tàu%l;#;".» |
| ハチロク04_煙には煙を.txt.toml | 1914 | 「どうせ夜は、川下りありません、し。\n夜、あんまり\x%l列車;#00ffc040;列車%l;#;に乗ることないから――面白い。です」 | 「反正晚上沒人去漂流。因為我很少晚上坐\x%l列車;#00ffc040;列車%l;#;——所以我感覺很有趣。嗯」 | 「Dù sao buổi tối cũng không có thuyền xuôi dòng.\nBan đêm, em ít khi đi \x%l列車;#00ffc040;tàu%l;#; nên――cũng thú vị lắm ạ.」 | 「Dù sao buổi tối cũng không có thuyền xuôi dòng.\nBan đêm, em ít khi đi \x%l列車;#00ffc040;đoàn tàu%l;#; nên――cũng thú vị lắm ạ.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク04_煙には煙を.txt.toml | 1922 | 「あらかじめ、焼肉をする\x%l列車;#00ffc040;列車%l;#;とわかっているのなら、\n乗客はケムさを、ある程度覚悟してくれると思うからだ」 | 「只要事先明白是用來烤肉的\x%l列車;#00ffc040;列車%l;#;，乘客也會做好在一定程度上“會熏人”的心理準備了」 | 「Bởi vì nếu đã biết trước đây là \x%l列車;#00ffc040;chuyến tàu%l;#; để nướng thịt,\nanh nghĩ hành khách sẽ phần nào chuẩn bị tinh thần cho việc bị ám khói.」 | 「Bởi vì nếu đã biết trước đây là \x%l列車;#00ffc040;đoàn tàu%l;#; để nướng thịt,\nanh nghĩ hành khách sẽ phần nào chuẩn bị tinh thần cho việc bị ám khói.」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ハチロク04_煙には煙を.txt.toml | 2062 | 「焼肉\x%l列車;#00ffc040;列車%l;#;……っていうことにするなら、エプロン――\n服が汚れないようつけて貰っておかしくない。です、し」 | 「如果變成烤肉\x%l列車;#00ffc040;列車%l;#;……讓乘客們穿上圍裙——防止弄髒衣服，也不會顯得奇怪」 | 「Nếu gọi là \x%l列車;#00ffc040;Chuyến tàu%l;#; Thịt nướng……thì việc phát tạp dề――\nđể quần áo không bị bẩn cũng không có gì lạ đâu ạ.」 | 「Nếu gọi là \x%l列車;#00ffc040;Đoàn tàu%l;#; Thịt nướng……thì việc phát tạp dề――\nđể quần áo không bị bẩn cũng không có gì lạ đâu ạ.」 | «\x%l列車;#00ffc040;Chuyến» → «\x%l列車;#00ffc040;Đoàn» |
| ハチロク04_煙には煙を.txt.toml | 2182 | 「だよねぇ、焼肉\x%l列車;#00ffc040;列車%l;#;――じゃないや。\nええと、バーベキュートレインになったんだよね」 | 「是啊，烤肉\x%l列車;#00ffc040;列車%l;#;——不對。呃，現在叫ＢＢＱ列車了啊」 | 「Cũng đúng ha, \x%l列車;#00ffc040;chuyến tàu%l;#; thịt nướng――à không.\nỪm, đổi tên thành chuyến tàu BBQ rồi nhỉ.」 | 「Cũng đúng ha, \x%l列車;#00ffc040;đoàn tàu%l;#; thịt nướng――à không.\nỪm, đổi tên thành chuyến tàu BBQ rồi nhỉ.」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ハチロク04_煙には煙を.txt.toml | 2236 | 「試験\x%l列車;#00ffc040;列車%l;#;の一番\x%l列車;#00ffc040;列車%l;#;！\nふかみちゃんと一緒に、絶対、乗せてもらうばい！！」 | 「測試\x%l列車;#00ffc040;列車%l;#;的首班\x%l列車;#00ffc040;列車%l;#;！咱一定要和小深一起坐！！」 | 「\x%l列車;#00ffc040;Chuyến tàu%l;#; thử nghiệm đầu tiên!\nTớ nhất định sẽ ngồi cùng Fukami nha!!」 | 「\x%l列車;#00ffc040;Đoàn tàu%l;#; thử nghiệm đầu tiên!\nTớ nhất định sẽ ngồi cùng Fukami nha!!」 | «「\x%l列車;#00ffc040;Chuyến» → «「\x%l列車;#00ffc040;Đoàn» |
| ハチロク04_煙には煙を.txt.toml | 2389 | 「栄えある一番\x%l列車;#00ffc040;列車%l;#;だ。多少のトラブルには目をつぶり、\nとにかく走りきらせたい気持ちも、正直持ってる。が」 | 「這是光榮的首班\x%l列車;#00ffc040;列車%l;#;。雖然老實說，我也想忽略一些輕微的故障，總之先讓它跑起來。但是」 | 「Đây là \x%l列車;#00ffc040;chuyến tàu%l;#; số 1 đầy vinh quang. Thú thực là anh cũng có suy nghĩ\nmuốn nhắm mắt làm ngơ trước vài rắc rối nhỏ để cố chạy cho xong. Nhưng,」 | 「Đây là \x%l列車;#00ffc040;đoàn tàu%l;#; số 1 đầy vinh quang. Thú thực là anh cũng có suy nghĩ\nmuốn nhắm mắt làm ngơ trước vài rắc rối nhỏ để cố chạy cho xong. Nhưng,」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ハチロク04_煙には煙を.txt.toml | 2393 | 「絶対、評判になるよね、この\x%l列車;#00ffc040;列車%l;#;。\nそれで、御一夜――またにぎやかな町になるよね」 | 「這輛\x%l列車;#00ffc040;列車%l;#;絕對會大受好評的。而御一夜——也會變回以前一樣熱鬧的鎮子」 | 「Chắc chắn \x%l列車;#00ffc040;chuyến tàu%l;#; này sẽ nổi tiếng lắm đây.\nRồi Ohitoyo――sẽ lại trở thành một thị trấn nhộn nhịp nhỉ.」 | 「Chắc chắn \x%l列車;#00ffc040;đoàn tàu%l;#; này sẽ nổi tiếng lắm đây.\nRồi Ohitoyo――sẽ lại trở thành một thị trấn nhộn nhịp nhỉ.」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ハチロク04_煙には煙を.txt.toml | 2395 | 「言われたら、一番\x%l列車;#00ffc040;列車%l;#;にもポーレットねえちゃんたち\n乗っとらんねぇ」 | 「這麼說來。波萊特姐姐她們也沒坐首班\x%l列車;#00ffc040;列車%l;#;啊」 | 「Nhắc mới nhớ, chuyến \x%l列車;#00ffc040;tàu%l;#; đầu tiên chị Paulette và mọi người\ncũng không đi nha.」 | 「Nhắc mới nhớ, chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; đầu tiên chị Paulette và mọi người\ncũng không đi nha.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク04_煙には煙を.txt.toml | 2430 | 「さて、まさしく日々姫の言葉通りの、\n記念すべき一号\x%l列車;#00ffc040;列車%l;#;です」 | 「那麼，正如日日姬所說，這是值得紀念的首班\x%l列車;#00ffc040;列車%l;#;」 | 「Nào, đúng như lời Hibiki đã nói,\nđây là \x%l列車;#00ffc040;chuyến tàu%l;#; số 1 vô cùng đáng nhớ ạ.」 | 「Nào, đúng như lời Hibiki đã nói,\nđây là \x%l列車;#00ffc040;đoàn tàu%l;#; số 1 vô cùng đáng nhớ ạ.」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ハチロク04_煙には煙を.txt.toml | 2464 | 「バーベキュー\x%l列車;#00ffc040;列車%l;#;の折り返し、[ゆのい,1]湯医の発船場から\n御一夜まで、川下り使う人も右肩上がりじゃないですか」 | 「ＢＢＱ\x%l列車;#00ffc040;列車%l;#;折返的時候，選擇利用漂流從湯醫的發船場去御一夜的人不也越來越多了嗎」 | 「Lúc \x%l列車;#00ffc040;chuyến tàu%l;#; BBQ quay về, số người sử dụng thuyền xuôi dòng từ bến tàu Yunoi\nđến Ohitoyo cũng đang tăng lên đều đặn mà.」 | 「Lúc \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ quay về, số người sử dụng thuyền xuôi dòng từ bến tàu Yunoi\nđến Ohitoyo cũng đang tăng lên đều đặn mà.」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ハチロク04_煙には煙を.txt.toml | 2769 | 僕らが送った一号\x%l列車;#00ffc040;列車%l;#;の様子の写真を、\n安芸様はネットで紹介してくださった。 | 安芸殿下在網路上介紹了我們投遞過去的首班\x%l列車;#00ffc040;列車%l;#;的外表的照片。 | Ngài Aki đã giới thiệu bức ảnh chụp \x%l列車;#00ffc040;chuyến tàu%l;#; số 1\nmà chúng tôi gửi trên mạng. | Ngài Aki đã giới thiệu bức ảnh chụp \x%l列車;#00ffc040;đoàn tàu%l;#; số 1\nmà chúng tôi gửi trên mạng. | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ハチロク06_それぞれの傷跡.txt.toml | 1501 | 「ローカルの観光\x%l列車;#00ffc040;列車%l;#;ではある形式ですし……\n課題をいくつか解消できれば、いける気がします」 | 「作為當地的觀光\x%l列車;#00ffc040;列車%l;#;這樣的形式倒不是沒有先例，解決掉幾個難點的話，應該是可行的」 | 「Đây cũng là một hình thức \x%l列車;#00ffc040;tàu%l;#; du lịch địa phương……\nNếu giải quyết được một số vấn đề, tôi nghĩ là sẽ ổn thôi.」 | 「Đây cũng là một hình thức \x%l列車;#00ffc040;đoàn tàu%l;#; du lịch địa phương……\nNếu giải quyết được một số vấn đề, tôi nghĩ là sẽ ổn thôi.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク06_それぞれの傷跡.txt.toml | 1572 | 「なるほど、かなり残酷なこととなるか。\n食べ盛りの学園生が主体の\x%l列車;#00ffc040;列車%l;#;だものな」 | 「原來如此，確實很難忍受呢。畢竟那邊\x%l列車;#00ffc040;列車%l;#;的乘客多是正值成長期、胃口旺盛的學生」 | 「Ra vậy, như thế thì khá là tàn nhẫn nhỉ.\nVì hành khách chủ yếu của chuyến \x%l列車;#00ffc040;tàu%l;#; này là những học sinh đang tuổi ăn tuổi lớn mà.」 | 「Ra vậy, như thế thì khá là tàn nhẫn nhỉ.\nVì hành khách chủ yếu của chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; này là những học sinh đang tuổi ăn tuổi lớn mà.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク06_それぞれの傷跡.txt.toml | 1737 | 「ええと――臭い対策。必要になると思います。\n\x%lキハ07;#00ffc040;キハ07%l;#;側――[にちよう,1]日用\x%l列車;#00ffc040;列車%l;#;側に焼肉の臭いが流れこむと……」 | 「我想想，還有就是必須要有處理氣味的方法吧。如果烤肉的味道飄到\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;，也就是通勤\x%l列車;#00ffc040;列車%l;#;那邊的話……」 | 「Để xem nào――biện pháp xử lý mùi hương. Tôi nghĩ là cần thiết đấy.\nNếu mùi thịt nướng bay sang phía \x%lキハ07;#00ffc040;KiHa 07%l;#;――phía \x%l列車;#00ffc040;tàu%l;#; chạy thường ngày thì……」 | 「Để xem nào――biện pháp xử lý mùi hương. Tôi nghĩ là cần thiết đấy.\nNếu mùi thịt nướng bay sang phía \x%lキハ07;#00ffc040;KiHa 07%l;#;――phía \x%l列車;#00ffc040;đoàn tàu%l;#; chạy thường ngày thì……」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク06_それぞれの傷跡.txt.toml | 2023 | 「まず、時間ですよね。\n朝は、観光\x%l列車;#00ffc040;列車%l;#;としてはかなり早い時刻になります」 | 「首先就是時間了吧。早上的話，對於觀光\x%l列車;#00ffc040;列車%l;#;而言可以說是相當早了」 | 「Đầu tiên là thời gian.\nBuổi sáng thì hơi quá sớm đối với một chuyến \x%l列車;#00ffc040;tàu%l;#; du lịch.」 | 「Đầu tiên là thời gian.\nBuổi sáng thì hơi quá sớm đối với một chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; du lịch.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク07_ハチロクの目覚め.txt.toml | 2079 | 車輌故障に伴っての、機関車変更。\nバーベキュー\x%l列車;#00ffc040;列車%l;#;の主体はあくまで\x%l客車;#00ffc040;客車%l;#;―― | 因為先前的車輛故障，我們變更了編組。 | Đổi đầu máy do sự cố phương tiện.\nChủ thể của \x%l列車;#00ffc040;tàu%l;#; BBQ suy cho cùng vẫn là \x%l客車;#00ffc040;toa hành khách%l;#;―― | Đổi đầu máy do sự cố phương tiện.\nChủ thể của \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ suy cho cùng vẫn là \x%l客車;#00ffc040;toa hành khách%l;#;―― | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク09_採決.txt.toml | 1894 | 「公共性が。他者の緩やかな連帯が、好感され評価される。\nバーベキュー\x%l列車;#00ffc040;列車%l;#;の大ヒットは、そんな嗜好の現れです」 | 「公共性和為他人提供舒適的共處空間，能博得旅客的好感及好評。ＢＢＱ\x%l列車;#00ffc040;列車%l;#;的爆紅正是這一嗜好的體現」 | 「Tính công cộng. Sự liên kết nhẹ nhàng với những người khác, được yêu thích và đánh giá cao.\nSự thành công vang dội của \x%l列車;#00ffc040;chuyến tàu%l;#; BBQ, chính là biểu hiện của sở thích đó.」 | 「Tính công cộng. Sự liên kết nhẹ nhàng với những người khác, được yêu thích và đánh giá cao.\nSự thành công vang dội của \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ, chính là biểu hiện của sở thích đó.」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ハチロク09_採決.txt.toml | 1937 | 「右田さんはバーベキュー\x%l列車;#00ffc040;列車%l;#;――[ハチロクニイマル,3]8620号の、\n主任\x%l機関士;#00ffc040;機関士%l;#;兼運行責任者でいらっしゃるとのことですが」 | 「右田先生是ＢＢＱ\x%l列車;#00ffc040;列車%l;#;——８６２０號的主任\x%l機関士;#00ffc040;司機%l;#;兼運營負責人，是嗎？」 | 「Anh Migita là \x%l機関士;#00ffc040;Lái tàu%l;#; trưởng kiêm người chịu trách nhiệm vận hành của \x%l列車;#00ffc040;chuyến tàu%l;#; BBQ——\nĐầu máy 8620 đúng không ạ?」 | 「Anh Migita là \x%l機関士;#00ffc040;Lái tàu%l;#; trưởng kiêm người chịu trách nhiệm vận hành của \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ——\nĐầu máy 8620 đúng không ạ?」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ハチロク09_採決.txt.toml | 2100 | 「バーベキュー\x%l列車;#00ffc040;列車%l;#;の運行について、\nクレームが発生している件はご存知ですね？」 | 「想必您知道有部分人對ＢＢＱ\x%l列車;#00ffc040;列車%l;#;的運營表示不滿吧？」 | 「Về việc vận hành \x%l列車;#00ffc040;chuyến tàu%l;#; BBQ,\nchắc cô cũng biết là đang có những lời phàn nàn phát sinh đúng không?」 | 「Về việc vận hành \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ,\nchắc cô cũng biết là đang có những lời phàn nàn phát sinh đúng không?」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ハチロク09_採決.txt.toml | 2174 | 「はい。[ハチロクニイマル,3]8620によるバーベキュー\x%l列車;#00ffc040;列車%l;#;の、\n全ての運行を担当させていただいております」 | 「是的。有關８６２０以及ＢＢＱ\x%l列車;#00ffc040;列車%l;#;運營的一切事務都由我負責」 | 「Vâng. Tôi chịu trách nhiệm toàn bộ việc vận hành,\ncủa \x%l列車;#00ffc040;chuyến tàu%l;#; BBQ do Đầu máy 8620 đảm nhận.」 | 「Vâng. Tôi chịu trách nhiệm toàn bộ việc vận hành,\ncủa \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ do Đầu máy 8620 đảm nhận.」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ハチロク09_採決.txt.toml | 3064 | そのためには、\x%l8620;#00ffc040;8620%l;#;の復活と、\nバーベキュー\x%l列車;#00ffc040;列車%l;#;のより一層の活性化が必須となる。 | 為此需要讓\x%l8620;#00ffc040;８６２０%l;#;復活，以及讓ＢＢＱ\x%l列車;#00ffc040;列車%l;#;更進一步最佳化利用。 | Để làm được điều đó, sự hồi sinh của \x%l8620;#00ffc040;8620%l;#;, và\nviệc kích hoạt mạnh mẽ hơn nữa \x%l列車;#00ffc040;chuyến tàu%l;#; BBQ là điều bắt buộc. | Để làm được điều đó, sự hồi sinh của \x%l8620;#00ffc040;8620%l;#;, và\nviệc kích hoạt mạnh mẽ hơn nữa \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ là điều bắt buộc. | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ハチロク10_炙り出し.txt.toml | 1940 | 「はい。今日もバーベキュー\x%l列車;#00ffc040;列車%l;#;、\n九割がたは席埋まってますし、張り切ってくれてます」 | 「是的。今天ＢＢＱ\x%l列車;#00ffc040;列車%l;#;也幾乎擠滿了客人，她可是鼓足了幹勁」 | 「Vâng. Hôm nay \x%l列車;#00ffc040;tàu%l;#; BBQ cũng\nkín chỗ đến chín phần rồi, nên em ấy đang rất hăng hái ạ.」 | 「Vâng. Hôm nay \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ cũng\nkín chỗ đến chín phần rồi, nên em ấy đang rất hăng hái ạ.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク11_幽霊.txt.toml | 2184 | 「バーベキュー\x%l列車;#00ffc040;列車%l;#;の\x%l機関士;#00ffc040;機関士%l;#;さんか」 | 「ＢＢＱ\x%l列車;#00ffc040;列車%l;#;的\x%l機関士;#00ffc040;司機%l;#;啊」 | 「Là anh \x%l機関士;#00ffc040;lái tàu%l;#; của \x%l列車;#00ffc040;chuyến tàu%l;#; BBQ sao.」 | 「Là anh \x%l機関士;#00ffc040;lái tàu%l;#; của \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ sao.」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ハチロク12_再開発.txt.toml | 2977 | 内側に曲げた左手を線路に見立て、\n親指を立てた右の拳を\x%l列車;#00ffc040;列車%l;#;に見立て、滑らせる。 | 我把左手向內彎，比出線路的樣子，右手握拳立起拇指，比出\x%l列車;#00ffc040;列車%l;#;的樣子在上面滑行。 | Tôi lấy bàn tay trái cong vào trong làm đường ray,\nnắm đấm phải dựng ngón cái lên làm \x%l列車;#00ffc040;tàu%l;#; rồi trượt đi. | Tôi lấy bàn tay trái cong vào trong làm đường ray,\nnắm đấm phải dựng ngón cái lên làm \x%l列車;#00ffc040;đoàn tàu%l;#; rồi trượt đi. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク12_再開発.txt.toml | 3088 | バーベキュー\x%l列車;#00ffc040;列車%l;#;で、高めてくれたであろう期待を、\n現状、僕達は裏切ってしまっているに等しいのだから。 | 當初對ＢＢＱ\x%l列車;#00ffc040;列車%l;#;投以那麼高的期待，而如今這副光景，說是我們辜負了那份期待也不為過。 | Bởi vì hiện tại, chúng tôi gần như đã phản bội lại\nnhững kỳ vọng được thổi bùng lên từ chuyến \x%l列車;#00ffc040;tàu%l;#; BBQ. | Bởi vì hiện tại, chúng tôi gần như đã phản bội lại\nnhững kỳ vọng được thổi bùng lên từ chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ハチロク15_家族.txt.toml | 2717 | 入線してる。\nこの\x%l列車;#00ffc040;列車%l;#;はもう、終着駅についている。 | 進站了。這班\x%l列車;#00ffc040;列車%l;#;已經抵達了終點站。 | Đang tiến vào sân ga.\n\x%l列車;#00ffc040;Chuyến tàu%l;#; này, đã đến nhà ga cuối cùng. | Đang tiến vào sân ga.\n\x%l列車;#00ffc040;Đoàn tàu%l;#; này, đã đến nhà ga cuối cùng. | «ga.\n\x%l列車;#00ffc040;Chuyến» → «ga.\n\x%l列車;#00ffc040;Đoàn» |
| ポーレット01_御一夜探し.txt.toml | 1748 | 「\x%l列車;#00ffc040;列車%l;#;に乗って、駅弁やその土地の名産を食べることを\n主とするタイプの鉄道ファンね」 | 「是指以乘坐\x%l列車;#00ffc040;列車%l;#;品嘗鐵路便當及當地美食為主要目的的鐵路愛好者」 | 「Là kiểu người hâm mộ đường sắt lấy việc đi \x%l列車;#00ffc040;tàu%l;#;\nđể thưởng thức cơm hộp nhà ga và đặc sản địa phương làm mục đích chính ấy.」 | 「Là kiểu người hâm mộ đường sắt lấy việc đi \x%l列車;#00ffc040;đoàn tàu%l;#;\nđể thưởng thức cơm hộp nhà ga và đặc sản địa phương làm mục đích chính ấy.」 | «\x%l列車;#00ffc040;tàu%l;#;\nđể» → «\x%l列車;#00ffc040;đoàn tàu%l;#;\nđể» |
| ポーレット09_ストーブ客車.txt.toml | 1746 | 「そのときには、僕と一緒に乗ってくれないか？\n蒼森、津輕の――津っ鐵さんのストーブ\x%l列車;#00ffc040;列車%l;#;に」 | 「到時候，能和我一起去嗎？一起去坐青森津輕——津鐵的暖爐\x%l列車;#00ffc040;列車%l;#;」 | 「Đến lúc đó, em đi cùng tôi nhé? Lên chuyến \x%l列車;#00ffc040;tàu%l;#; sưởi ấm của Tsutetsu――ở Tsugaru, Aomori.」 | 「Đến lúc đó, em đi cùng tôi nhé? Lên chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; sưởi ấm của Tsutetsu――ở Tsugaru, Aomori.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ポーレット09_ストーブ客車.txt.toml | 2219 | 「\x%l単線;#00ffc040;単線%l;#;で。ストーブ\x%l列車;#00ffc040;列車%l;#;はとっても静かで。\nガイドのおばさんの津輕弁、初めて聞くのに懐かしくて」 | 「還是\x%l単線;#00ffc040;單線%l;#;。暖爐\x%l列車;#00ffc040;列車%l;#;非常安靜。導遊大媽操著津輕口音，明明是第一次聽卻非常親切」 | 「Đường \x%l単線;#00ffc040;đơn%l;#; ạ. Chuyến \x%l列車;#00ffc040;tàu%l;#; sưởi ấm rất đỗi tĩnh lặng.\nGiọng Tsugaru của cô hướng dẫn viên, lần đầu tiên nghe nhưng lại thấy thật hoài niệm.」 | 「Đường \x%l単線;#00ffc040;đơn%l;#; ạ. Chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; sưởi ấm rất đỗi tĩnh lặng.\nGiọng Tsugaru của cô hướng dẫn viên, lần đầu tiên nghe nhưng lại thấy thật hoài niệm.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ポーレット09_ストーブ客車.txt.toml | 2229 | 「あの！　さっきの話っ――\nえと、ストーブ\x%l列車;#00ffc040;列車%l;#;を経験してみたいって」 | 「那個！　剛才說過的，就是那個——你說想體驗暖爐\x%l列車;#00ffc040;列車%l;#;那件事」 | 「Dạ! Chuyện lúc nãy――\nỪm, chuyện anh nói muốn trải nghiệm \x%l列車;#00ffc040;tàu%l;#; sưởi ấm ấy.」 | 「Dạ! Chuyện lúc nãy――\nỪm, chuyện anh nói muốn trải nghiệm \x%l列車;#00ffc040;đoàn tàu%l;#; sưởi ấm ấy.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ポーレット09_ストーブ客車.txt.toml | 2232 | 「ええと、津っ鐵さんもストーブ\x%l列車;#00ffc040;列車%l;#;もまだ現役です。\n観光\x%l列車;#00ffc040;列車%l;#;として、一番くらいに名高いですから」 | 「那個，津鐵和暖爐\x%l列車;#00ffc040;列車%l;#;如今都還在運營。因為這列觀光\x%l列車;#00ffc040;列車%l;#;非常有名」 | 「À ừm, Tsutetsu và chuyến \x%l列車;#00ffc040;tàu%l;#; sưởi ấm vẫn đang hoạt động đấy ạ.\nLà một chuyến \x%l列車;#00ffc040;tàu%l;#; du lịch, nó nổi tiếng nhất nhì luôn đó.」 | 「À ừm, Tsutetsu và chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; sưởi ấm vẫn đang hoạt động đấy ạ.\nLà một chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; du lịch, nó nổi tiếng nhất nhì luôn đó.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;»; «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ポーレット09_ストーブ客車.txt.toml | 2634 | 日ノ本一の観光\x%l列車;#00ffc040;列車%l;#;――\nあやかっていては、それを越えるには至れまい。 | 我們要打造日本第一的觀光\x%l列車;#00ffc040;列車%l;#;——如果只是去效仿，就無法超越。 | Chuyến \x%l列車;#00ffc040;tàu%l;#; du lịch số một Hinomoto――\nNếu chỉ biết bắt chước, thì sẽ chẳng bao giờ vượt qua được nó. | Chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; du lịch số một Hinomoto――\nNếu chỉ biết bắt chước, thì sẽ chẳng bao giờ vượt qua được nó. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ポーレット10_見えない傷.txt.toml | 1461 | 「だから、臨時\x%l列車;#00ffc040;列車%l;#;を仕立てて、\nお客様無しの練習走行とわたしの移送とを兼ねる」 | 「所以才安排了臨時\x%l列車;#00ffc040;列車%l;#;，既能夠在沒有乘客的情況下練習駕駛，又能夠載我一程」 | 「Vì vậy, chúng ta mới thiết lập một \x%l列車;#00ffc040;chuyến tàu%l;# lâm thời,\nvừa kết hợp chạy tập luyện không có hành khách, vừa để đưa tôi đi luôn.」 | 「Vì vậy, chúng ta mới thiết lập một \x%l列車;#00ffc040;đoàn tàu%l;# lâm thời,\nvừa kết hợp chạy tập luyện không có hành khách, vừa để đưa tôi đi luôn.」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| ポーレット16_明日へのレール.txt.toml | 1782 | 「あと五分程、\x%l列車;#00ffc040;列車%l;#;はマイントレジャー入口駅につきます。\nそこからは、トロッコに乗っていただきます」 | 「再過大約５分鐘，\x%l列車;#00ffc040;列車%l;#;就會到達煤探樂園入口站。之後要請各位乘坐礦車」 | 「Khoảng 5 phút nữa, \x%l列車;#00ffc040;tàu%l;#; sẽ đến ga Cổng vào Mine Treasure.\nTừ đó, xin mời quý vị chuyển sang đi xe goòng.」 | 「Khoảng 5 phút nữa, \x%l列車;#00ffc040;đoàn tàu%l;#; sẽ đến ga Cổng vào Mine Treasure.\nTừ đó, xin mời quý vị chuyển sang đi xe goòng.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ポーレット16_明日へのレール.txt.toml | 1973 | 「なかなか楽しい物ですよ。\nこの\x%l列車;#00ffc040;列車%l;#;ほど、乗り心地よくはありませんがね」 | 「坐起來可是很有意思的。雖然不如這輛\x%l列車;#00ffc040;列車%l;#;坐著舒服」 | 「Cũng khá thú vị đấy.\nTuy không được thoải mái như chuyến \x%l列車;#00ffc040;tàu%l;#; này đâu.」 | 「Cũng khá thú vị đấy.\nTuy không được thoải mái như chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; này đâu.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| ポーレット16_明日へのレール.txt.toml | 2250 | 「ええ。マイントレジャーでの観光\x%l列車;#00ffc040;列車%l;#;の駅弁の、\nその、試食品ということですので、ご遠慮なく」 | 「當然。這是煤探樂園觀光\x%l列車;#00ffc040;列車%l;#;便當的試吃品，請大家不要客氣」 | 「Vâng. Đây là hàng dùng thử của cơm hộp bento nhà ga\ncho \x%l列車;#00ffc040;chuyến tàu%l;#; du lịch ở Mine Treasure, nên mọi người cứ tự nhiên nhé.」 | 「Vâng. Đây là hàng dùng thử của cơm hộp bento nhà ga\ncho \x%l列車;#00ffc040;đoàn tàu%l;#; du lịch ở Mine Treasure, nên mọi người cứ tự nhiên nhé.」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| 共通02_日々姫と真闇と人形と.txt.toml | 2339 | 「そして、日々姫様はレールと\x%l列車;#00ffc040;列車%l;#;とのたてる響き。\n汰斗様は、お孫様達に素敵なお名前をつけられましたね」 | 「然後，日日姬大人是鐵軌與\x%l列車;#00ffc040;列車%l;#;之間發出的聲音。汰斗老爺給各位愛孫取了很棒的名字呢」 | 「Và, ngài Hibiki là âm vang (Hibiki) được tạo ra giữa đường ray và \x%l列車;#00ffc040;tàu%l;#;.\nNgài Taito đã đặt cho các cháu của mình những cái tên thật tuyệt vời.」 | 「Và, ngài Hibiki là âm vang (Hibiki) được tạo ra giữa đường ray và \x%l列車;#00ffc040;đoàn tàu%l;#;.\nNgài Taito đã đặt cho các cháu của mình những cái tên thật tuyệt vời.」 | «\x%l列車;#00ffc040;tàu%l;#;.\nNgài» → «\x%l列車;#00ffc040;đoàn tàu%l;#;.\nNgài» |
| 共通04_キハ07。ポーレットとれいな.txt.toml | 1811 | 「ならば、\x%l待避線;#00ffc040;待避線%l;#;が死ぬに至るまで使われない理由は、\n“\x%l列車;#00ffc040;列車%l;#;の行き違いが全く発生しないから”、となるか」 | 「\x%l待避線;#00ffc040;待避線%l;#;長期閒置直至荒廢，是因為根本沒有\x%l列車;#00ffc040;列車%l;#;需要交換位置嗎」 | 「Vậy thì, lý do \x%l待避線;#00ffc040;đường tránh tàu%l;#; không được sử dụng đến mức bị bỏ hoang,\nlà do "hoàn toàn không có chuyện các \x%l列車;#00ffc040;chuyến tàu%l;#; cần tránh nhau", phải không?」 | 「Vậy thì, lý do \x%l待避線;#00ffc040;đường tránh tàu%l;#; không được sử dụng đến mức bị bỏ hoang,\nlà do "hoàn toàn không có chuyện các \x%l列車;#00ffc040;đoàn tàu%l;#; cần tránh nhau", phải không?」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| 共通04_キハ07。ポーレットとれいな.txt.toml | 1814 | 「\x%l列車;#00ffc040;列車%l;#;が踏む――車輪で削る面であるから、\x%l踏面;#00ffc040;踏面%l;#;か。\nゆえに、そこだけは錆びつかない」 | 「\x%l踏面;#00ffc040;踏面%l;#;就是——\x%l列車;#00ffc040;列車%l;#;車輪踏在軌道上、產生削磨的麵。所以只有那裡沒有鏽跡」 | 「Là mặt bị \x%l列車;#00ffc040;tàu%l;#; giẫm lên——bị bánh xe bào mòn, nên gọi là \x%l踏面;#00ffc040;mặt lăn bánh xe%l;#; sao.\nVì vậy, chỉ có chỗ đó là không bị gỉ sét.」 | 「Là mặt bị \x%l列車;#00ffc040;đoàn tàu%l;#; giẫm lên——bị bánh xe bào mòn, nên gọi là \x%l踏面;#00ffc040;mặt lăn bánh xe%l;#; sao.\nVì vậy, chỉ có chỗ đó là không bị gỉ sét.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通04_キハ07。ポーレットとれいな.txt.toml | 2086 | 「\x%l列車;#00ffc040;列車%l;#;や\x%lレイルロオド;#00ffc040;レイルロオド%l;#;と同じく――\n駅さえ……死んでしまうものなのですね」 | 「不只是\x%l列車;#00ffc040;列車%l;#;和\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;——就連車站也……無法使用了」 | 「Giống như \x%l列車;#00ffc040;tàu%l;#; hay \x%lレイルロオド;#00ffc040;Railord%l;#;——\nNgay cả nhà ga……cũng sẽ chết đi nhỉ.」 | 「Giống như \x%l列車;#00ffc040;đoàn tàu%l;#; hay \x%lレイルロオド;#00ffc040;Railord%l;#;——\nNgay cả nhà ga……cũng sẽ chết đi nhỉ.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通04_キハ07。ポーレットとれいな.txt.toml | 2260 | 「この路線の\x%l列車;#00ffc040;列車%l;#;の\x%lレイルロオド;#00ffc040;レイルロオド%l;#;が、\n規則に忠実な子であるからです、双鉄様」 | 「因為負責這條線路上\x%l列車;#00ffc040;列車%l;#;的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;非常守規則，雙鐵少爺」 | 「Bởi vì \x%lレイルロオド;#00ffc040;Railord%l;#; của \x%l列車;#00ffc040;chuyến tàu%l;#; trên tuyến đường này\nlà một đứa trẻ rất trung thành với luật lệ, ngài Soutetsu.」 | 「Bởi vì \x%lレイルロオド;#00ffc040;Railord%l;#; của \x%l列車;#00ffc040;đoàn tàu%l;#; trên tuyến đường này\nlà một đứa trẻ rất trung thành với luật lệ, ngài Soutetsu.」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| 共通04_キハ07。ポーレットとれいな.txt.toml | 2292 | 「もしも廃線されていれば、\n当然、\x%l列車;#00ffc040;列車%l;#;は走らず、ゆえにレールも削られはせず」 | 「如果線路已經被廢棄，就不會有\x%l列車;#00ffc040;列車%l;#;在上面行駛，鐵軌也就不會被削磨」 | 「Nếu đã bị bỏ hoang,\nthì đương nhiên, \x%l列車;#00ffc040;tàu%l;#; sẽ không chạy, và đường ray cũng sẽ không bị bào mòn.」 | 「Nếu đã bị bỏ hoang,\nthì đương nhiên, \x%l列車;#00ffc040;đoàn tàu%l;#; sẽ không chạy, và đường ray cũng sẽ không bị bào mòn.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通04_キハ07。ポーレットとれいな.txt.toml | 2366 | 「でしたらどこかに、まだ生きている駅もありましょう。\nそこにはきっと、生きている\x%l列車;#00ffc040;列車%l;#;と鉄道員も」 | 「所以一定有仍在使用的車站。也一定有仍在使用的\x%l列車;#00ffc040;列車%l;#;和鐵路工人」 | 「Nếu vậy thì ở đâu đó, hẳn vẫn còn nhà ga đang sống.\nỞ đó chắc chắn cũng có \x%l列車;#00ffc040;tàu%l;#; và nhân viên đường sắt đang sống.」 | 「Nếu vậy thì ở đâu đó, hẳn vẫn còn nhà ga đang sống.\nỞ đó chắc chắn cũng có \x%l列車;#00ffc040;đoàn tàu%l;#; và nhân viên đường sắt đang sống.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通04_キハ07。ポーレットとれいな.txt.toml | 2967 | ああ、これは――\nそうだ。これが\x%l列車;#00ffc040;列車%l;#;の音だ。 | 啊，沒錯——這就是\x%l列車;#00ffc040;列車%l;#;發出的聲音。 | A, đây là——\nĐúng rồi. Đây là âm thanh của \x%l列車;#00ffc040;chuyến tàu%l;#;. | A, đây là——\nĐúng rồi. Đây là âm thanh của \x%l列車;#00ffc040;đoàn tàu%l;#;. | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| 共通04_キハ07。ポーレットとれいな.txt.toml | 3037 | その役割は、自らが砕けることにより、\n\x%l列車;#00ffc040;列車%l;#;が与える衝撃を、線路に代わって受けることだと。 | 它的職責是藉由自身的粉碎，替鐵軌吸收\x%l列車;#00ffc040;列車%l;#;帶來的衝擊。 | Vai trò của nó là tự vỡ vụn ra,\nđể chịu thay đường ray những lực tác động từ \x%l列車;#00ffc040;tàu%l;#;. | Vai trò của nó là tự vỡ vụn ra,\nđể chịu thay đường ray những lực tác động từ \x%l列車;#00ffc040;đoàn tàu%l;#;. | «\x%l列車;#00ffc040;tàu%l;#;.» → «\x%l列車;#00ffc040;đoàn tàu%l;#;.» |
| 共通04_キハ07。ポーレットとれいな.txt.toml | 3061 | 退避線とは、\x%l単線;#00ffc040;単線%l;#;上で\x%l列車;#00ffc040;列車%l;#;を行き違いさせるため、\n迂回をさせる目的で、駅などに設けられる線路だと。 | 待避線，即為了讓\x%l列車;#00ffc040;列車%l;#;在\x%l単線;#00ffc040;單線%l;#;上交換位置，設立在車站的供繞行的線路。 | Đường tránh tàu là đường ray được thiết lập tại các nhà ga với mục đích cho tàu đi vòng,\nđể các \x%l列車;#00ffc040;chuyến tàu%l;#; có thể tránh nhau trên \x%l単線;#00ffc040;đường đơn%l;#;. | Đường tránh tàu là đường ray được thiết lập tại các nhà ga với mục đích cho tàu đi vòng,\nđể các \x%l列車;#00ffc040;đoàn tàu%l;#; có thể tránh nhau trên \x%l単線;#00ffc040;đường đơn%l;#;. | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| 共通04_キハ07。ポーレットとれいな.txt.toml | 3171 | しかし、\x%l列車;#00ffc040;列車%l;#;本数の激減につれ、\nルールは徐々に、守られなくなっていったのだと。 | 然而，隨著\x%l列車;#00ffc040;列車%l;#;數量的急劇減少，遵守規則的人漸漸變少了。 | Tuy nhiên, cùng với sự sụt giảm nghiêm trọng của số lượng \x%l列車;#00ffc040;chuyến tàu%l;#;,\ncác quy tắc cũng dần dần không còn được tuân thủ nữa. | Tuy nhiên, cùng với sự sụt giảm nghiêm trọng của số lượng \x%l列車;#00ffc040;đoàn tàu%l;#;,\ncác quy tắc cũng dần dần không còn được tuân thủ nữa. | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| 共通04_キハ07。ポーレットとれいな.txt.toml | 3188 | “\x%l列車;#00ffc040;列車%l;#;の音”と感じた瞬間、\nそれを思い出した瞬間に―― | 當我意識到這是“\x%l列車;#00ffc040;列車%l;#;的聲音”，回想起那些感覺的一瞬間—— | Khoảnh khắc tôi cảm nhận được "âm thanh của \x%l列車;#00ffc040;chuyến tàu%l;#;",\nkhoảnh khắc tôi nhớ lại điều đó—— | Khoảnh khắc tôi cảm nhận được "âm thanh của \x%l列車;#00ffc040;đoàn tàu%l;#;",\nkhoảnh khắc tôi nhớ lại điều đó—— | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| 共通04_キハ07。ポーレットとれいな.txt.toml | 3307 | ならば、ここで待っていれば、\n\x%l列車;#00ffc040;列車%l;#;がいずれ来てくれるということなのだろう。 | 那就是說只要等在這裡，早晚會有\x%l列車;#00ffc040;列車%l;#;過來。 | Nếu vậy, chỉ cần đợi ở đây,\nkiểu gì cũng sẽ có \x%l列車;#00ffc040;chuyến tàu%l;#; đến đón chúng tôi. | Nếu vậy, chỉ cần đợi ở đây,\nkiểu gì cũng sẽ có \x%l列車;#00ffc040;đoàn tàu%l;#; đến đón chúng tôi. | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| 共通05_ようやく石炭.txt.toml | 2969 | ああ、しかし、一両\x%l編成;#00ffc040;編成%l;#;、という言葉もあるか？\nなら一両でも、一\x%l編成;#00ffc040;編成%l;#;で、\x%l列車;#00ffc040;列車%l;#;で――恐らくあるのだろう。 | 不過，好像也有單節\x%l編成;#00ffc040;編組%l;#;這個詞吧？那麼，由單節\x%l編成;#00ffc040;編組%l;#;組成的\x%l列車;#00ffc040;列車%l;#;應該也是存在的吧。 | A, nhưng mà, có từ gọi là \x%l編成;#00ffc040;đoàn tàu%l;#; một toa không nhỉ?\nNếu vậy thì dù chỉ có một toa, nó vẫn là một \x%l編成;#00ffc040;đoàn tàu%l;#;, một \x%l列車;#00ffc040;chuyến tàu%l;#;——có lẽ là có. | A, nhưng mà, có từ gọi là \x%l編成;#00ffc040;đoàn tàu%l;#; một toa không nhỉ?\nNếu vậy thì dù chỉ có một toa, nó vẫn là một \x%l編成;#00ffc040;đoàn tàu%l;#;, một \x%l列車;#00ffc040;đoàn tàu%l;#;——có lẽ là có. | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| 共通06_8620を探せ.txt.toml | 1573 | ……ああ、この音か。\n\x%l列車;#00ffc040;列車%l;#;の音か。 | ……啊，這聲音是，是\x%l列車;#00ffc040;列車%l;#;的聲音嗎。 | ……A, âm thanh này.\nLà tiếng \x%l列車;#00ffc040;tàu%l;#; chạy sao. | ……A, âm thanh này.\nLà tiếng \x%l列車;#00ffc040;đoàn tàu%l;#; chạy sao. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通06_8620を探せ.txt.toml | 1957 | 「まだこの\x%l列車;#00ffc040;列車%l;#;に乗っているのか」 | 「你還在這輛\x%l列車;#00ffc040;列車%l;#;上啊」 | 「Em vẫn đang ở trên chuyến \x%l列車;#00ffc040;tàu%l;#; này sao.」 | 「Em vẫn đang ở trên chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; này sao.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通06_8620を探せ.txt.toml | 2119 | 「間違いなくポーレットの目も、そうした“赤”を、\n日々姫の目にはボロな\x%l列車;#00ffc040;列車%l;#;に見ているのだ」 | 「在波萊特眼中一定也有這樣的“紅色”，而在日日姬眼裡它只是破舊的\x%l列車;#00ffc040;列車%l;#;」 | 「Chắc chắn đôi mắt của Paulette cũng đang nhìn thấy "màu đỏ" như vậy,\nở đoàn \x%l列車;#00ffc040;tàu%l;#; mà trong mắt Hibiki chỉ là đống sắt vụn.」 | 「Chắc chắn đôi mắt của Paulette cũng đang nhìn thấy "màu đỏ" như vậy,\nở đoàn \x%l列車;#00ffc040;đoàn tàu%l;#; mà trong mắt Hibiki chỉ là đống sắt vụn.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通06_8620を探せ.txt.toml | 2137 | 「どこからどう見てもガラクタのボロ\x%l列車;#00ffc040;列車%l;#;でも、\n“素晴らしい歴史的価値”って、市議会とかで」 | 「她在市議會上，宣稱怎麼看都是破爛的舊\x%l列車;#00ffc040;列車%l;#;擁有“偉大的歷史價值”」 | 「Dù nhìn từ góc độ nào thì cũng chỉ là một đoàn \x%l列車;#00ffc040;tàu%l;#; rách nát như đống sắt vụn,\nnhưng ở hội đồng thành phố lại bảo là "có giá trị lịch sử tuyệt vời"」 | 「Dù nhìn từ góc độ nào thì cũng chỉ là một đoàn \x%l列車;#00ffc040;đoàn tàu%l;#; rách nát như đống sắt vụn,\nnhưng ở hội đồng thành phố lại bảo là "có giá trị lịch sử tuyệt vời"」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通06_8620を探せ.txt.toml | 2216 | 「わたくしたち\x%lレイルロオド;#00ffc040;レイルロオド%l;#;とその\x%l列車;#00ffc040;列車%l;#;とは、\nいわば、血を分けたきょうだいです」 | 「我們\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;和所屬\x%l列車;#00ffc040;列車%l;#;之間的關係，可以說是血脈相連的同胞」 | 「\x%lレイルロオド;#00ffc040;Railord%l;#; chúng em và đoàn \x%l列車;#00ffc040;tàu%l;#; của mình,\ncó thể nói là anh em ruột thịt cùng chung dòng máu ạ.」 | 「\x%lレイルロオド;#00ffc040;Railord%l;#; chúng em và đoàn \x%l列車;#00ffc040;đoàn tàu%l;#; của mình,\ncó thể nói là anh em ruột thịt cùng chung dòng máu ạ.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通06_8620を探せ.txt.toml | 2451 | 「この\x%l列車;#00ffc040;列車%l;#;は……どこへ向かっているのかな」 | 「這輛\x%l列車;#00ffc040;列車%l;#;……開向什麼地方呢」 | 「Chuyến \x%l列車;#00ffc040;tàu%l;#; này…… đang đi về đâu vậy nhỉ.」 | 「Chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; này…… đang đi về đâu vậy nhỉ.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通06_8620を探せ.txt.toml | 2694 | この\x%l列車;#00ffc040;列車%l;#;にのり、最後になってしまった旅を――\n路子と父さんと母さんと、そうして僕は、したのだから。 | 乘上這輛\x%l列車;#00ffc040;列車%l;#;，路子、父親、母親以及我踏上了我們最後一次旅途。 | Bởi vì chuyến hành trình cuối cùng trên chuyến \x%l列車;#00ffc040;tàu%l;#; này——\ntôi đã đi cùng Michiko, bố và mẹ mà. | Bởi vì chuyến hành trình cuối cùng trên chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; này——\ntôi đã đi cùng Michiko, bố và mẹ mà. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通06_8620を探せ.txt.toml | 3112 | 父さんと母さんは乗ってない。\n路子はひとり、ずっと\x%l列車;#00ffc040;列車%l;#;に乗り続けている。 | 父親和母親沒在車上。路子一直一個人坐著\x%l列車;#00ffc040;列車%l;#;。 | Bố và mẹ không có trên tàu.\nMichiko vẫn luôn đi trên chuyến \x%l列車;#00ffc040;tàu%l;#; này một mình. | Bố và mẹ không có trên tàu.\nMichiko vẫn luôn đi trên chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; này một mình. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通09_さきだつもの.txt.toml | 105 | \x%l列車;#00ffc040;列車%l;#;――これ、加速してっ！？ | \x%l列車;#00ffc040;列車%l;#;在加速！？ | \x%l列車;#00ffc040;Tàu%l;#;——đang tăng tốc sao!? | \x%l列車;#00ffc040;Đoàn tàu%l;#;——đang tăng tốc sao!? | «\x%l列車;#00ffc040;Tàu%l;#;——đang» → «\x%l列車;#00ffc040;Đoàn tàu%l;#;——đang» |
| 共通09_さきだつもの.txt.toml | 106 | \x%l列車;#00ffc040;列車%l;#;が横に大きくゆれて、路子が僕に貼りついてくる。\n母さんも、父さんにギュっとしがみついてる。 | \x%l列車;#00ffc040;列車%l;#;突然傾斜了一下，路子嚇得緊緊抱住我。媽媽也趕緊抱住爸爸。 | \x%l列車;#00ffc040;Tàu%l;#; lắc mạnh sang một bên, Michiko bám chặt lấy tôi.\nMẹ cũng ôm chầm lấy bố. | \x%l列車;#00ffc040;Đoàn tàu%l;#; lắc mạnh sang một bên, Michiko bám chặt lấy tôi.\nMẹ cũng ôm chầm lấy bố. | «\x%l列車;#00ffc040;Tàu%l;#;» → «\x%l列車;#00ffc040;Đoàn tàu%l;#;» |
| 共通09_さきだつもの.txt.toml | 2488 | 「駅長ネコって、むかしはたくさんいたそうなんです。\n観光\x%l列車;#00ffc040;列車%l;#;の拠点駅とかに」 | 「我聽說也有貓擔任車站站長的呢。就在觀光\x%l列車;#00ffc040;列車%l;#;的總站裡」 | 「Nghe nói ngày xưa có rất nhiều mèo trạm trưởng đấy.\nỞ các ga trung tâm của \x%l列車;#00ffc040;tàu%l;#; du lịch chẳng hạn.」 | 「Nghe nói ngày xưa có rất nhiều mèo trạm trưởng đấy.\nỞ các ga trung tâm của \x%l列車;#00ffc040;đoàn tàu%l;#; du lịch chẳng hạn.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通09_さきだつもの.txt.toml | 2530 | 「この\x%l列車;#00ffc040;列車%l;#;、\x%l蒸気機関車;#00ffc040;蒸気機関車%l;#;が引っ張ってるでしょ？\nだから、前の方に行ってみたら」 | 「是\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;在牽引這輛\x%l列車;#00ffc040;列車%l;#;對吧？所以，我們去前面看看」 | 「\x%l列車;#00ffc040;Chuyến tàu%l;#; này, do \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; kéo đúng không?\nNên nếu lên phía trước xem thử.」 | 「\x%l列車;#00ffc040;Đoàn tàu%l;#; này, do \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; kéo đúng không?\nNên nếu lên phía trước xem thử.」 | «「\x%l列車;#00ffc040;Chuyến» → «「\x%l列車;#00ffc040;Đoàn» |
| 共通09_さきだつもの.txt.toml | 2540 | 「ああ。しばらくいくと、この\x%l列車;#00ffc040;列車%l;#;は\n冨士川[きょうりょう,1]橋梁という鉄橋を抜ける」 | 「是啊，再過一會，這輛\x%l列車;#00ffc040;列車%l;#;就會穿過一座叫富士川的鐵橋」 | 「Ừ. Đi thêm một lát nữa, \x%l列車;#00ffc040;chuyến tàu%l;#; này\nsẽ đi qua một cây cầu sắt tên là cầu Fujikawa.」 | 「Ừ. Đi thêm một lát nữa, \x%l列車;#00ffc040;đoàn tàu%l;#; này\nsẽ đi qua một cây cầu sắt tên là cầu Fujikawa.」 | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| 共通09_さきだつもの.txt.toml | 2726 | 「\x%l客車;#00ffc040;客車%l;#;のこととか、固定費とかを考えないでソレですから。\n観光\x%l列車;#00ffc040;列車%l;#;ですから指定席券でやれるとしても……」 | 「這還沒有把\x%l客車;#00ffc040;客運車廂%l;#;還有固定成本納入計算。就算我們是觀光\x%l列車;#00ffc040;列車%l;#;可以賣稍貴一些的指定座位票也……」 | 「Đó là còn chưa tính đến chuyện \x%l客車;#00ffc040;toa hành khách%l;#; hay chi phí cố định đấy ạ.\nDù là \x%l列車;#00ffc040;tàu%l;#; du lịch nên có thể bán vé ghế chỉ định đi chăng nữa thì……」 | 「Đó là còn chưa tính đến chuyện \x%l客車;#00ffc040;toa hành khách%l;#; hay chi phí cố định đấy ạ.\nDù là \x%l列車;#00ffc040;đoàn tàu%l;#; du lịch nên có thể bán vé ghế chỉ định đi chăng nữa thì……」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通09_さきだつもの.txt.toml | 2998 | あまりのことに対応できず、\nそのまま\x%l列車;#00ffc040;列車%l;#;の揺れに弾かれっ―― | 來不及應對這一突發情況，我的身體就這樣被搖晃的\x%l列車;#00ffc040;列車%l;#;彈飛—— | Quá bất ngờ nên tôi không kịp phản ứng,\ncứ thế bị chấn động của \x%l列車;#00ffc040;tàu%l;#; hất văng đi—— | Quá bất ngờ nên tôi không kịp phản ứng,\ncứ thế bị chấn động của \x%l列車;#00ffc040;đoàn tàu%l;#; hất văng đi—— | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通09_さきだつもの.txt.toml | 3551 | ガタガタゆれてさらに加速する\x%l列車;#00ffc040;列車%l;#;に怖じず、\nしっかりと僕の手を取って、路子は笑顔で立ち上がる。 | 路子這次沒有害怕一邊搖晃一邊繼續加速的\x%l列車;#00ffc040;列車%l;#;，而是緊緊握住我的手，笑著站了起來。 | Không hề sợ hãi trước \x%l列車;#00ffc040;chuyến tàu%l;#; đang rung lắc dữ dội và tiếp tục tăng tốc,\nMichiko nắm chặt tay tôi, mỉm cười đứng dậy. | Không hề sợ hãi trước \x%l列車;#00ffc040;đoàn tàu%l;#; đang rung lắc dữ dội và tiếp tục tăng tốc,\nMichiko nắm chặt tay tôi, mỉm cười đứng dậy. | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| 共通12_のぞみ.txt.toml | 2340 | 「\x%l列車;#00ffc040;列車%l;#;ばい。市長さんのが戻ってきたと」 | 「是\x%l列車;#00ffc040;列車%l;#;。市長回來咧」 | 「Là \x%l列車;#00ffc040;tàu%l;#; đấy. Xe của ngài thị trưởng đã quay về rồi.」 | 「Là \x%l列車;#00ffc040;đoàn tàu%l;#; đấy. Xe của ngài thị trưởng đã quay về rồi.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通12_のぞみ.txt.toml | 2393 | 「新線開通のときや、逆に\x%l列車;#00ffc040;列車%l;#;が廃止されるときなどには、\nホームがマニ――鉄道ファンで、埋め尽くされたのです」 | 「比如在開通新線的時候，或者就算是\x%l列車;#00ffc040;列車%l;#;被廢止的時候，站台上會擠滿了鐵路迷——鐵路愛好者」 | 「Vào lúc khai trương tuyến mới, hay ngược lại là khi \x%l列車;#00ffc040;tàu%l;#; bị ngừng hoạt động,\nsân ga sẽ chật kín những người đam——những người hâm mộ đường sắt ạ.」 | 「Vào lúc khai trương tuyến mới, hay ngược lại là khi \x%l列車;#00ffc040;đoàn tàu%l;#; bị ngừng hoạt động,\nsân ga sẽ chật kín những người đam——những người hâm mộ đường sắt ạ.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通12_のぞみ.txt.toml | 3391 | \x%l8620;#00ffc040;8620%l;#;を湯医にたどり着かせたのなら、\nあの\x%l列車;#00ffc040;列車%l;#;から――路子も、降りられるのかもしれない。 | 若是能幫助\x%l8620;#00ffc040;８６２０%l;#;駛到湯醫的話，說不定路子——就能從那輛\x%l列車;#00ffc040;列車%l;#;上下來了。 | Nếu có thể đưa \x%l8620;#00ffc040;8620%l;#; đến được Yunoi,\nthì có lẽ——Michiko cũng có thể bước xuống từ chuyến \x%l列車;#00ffc040;tàu%l;#; đó. | Nếu có thể đưa \x%l8620;#00ffc040;8620%l;#; đến được Yunoi,\nthì có lẽ——Michiko cũng có thể bước xuống từ chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; đó. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通12_のぞみ.txt.toml | 3473 | それも習った。\x%l列車;#00ffc040;列車%l;#;には、極めて大きな慣性が働く。\n\x%l列車;#00ffc040;列車%l;#;重量、速度、線路状況等にもよるが―― | 這我也學過了。雖然也受\x%l列車;#00ffc040;列車%l;#;的重量、速度和線路狀況等因素的影響，總的來說\x%l列車;#00ffc040;列車%l;#;的慣性極大—— | Tôi cũng đã học điều đó. Một lực quán tính cực lớn sẽ tác động lên \x%l列車;#00ffc040;tàu%l;#;.\nDù còn tùy thuộc vào trọng lượng \x%l列車;#00ffc040;tàu%l;#;, tốc độ, tình trạng đường ray, v.v.—— | Tôi cũng đã học điều đó. Một lực quán tính cực lớn sẽ tác động lên \x%l列車;#00ffc040;đoàn tàu%l;#;.\nDù còn tùy thuộc vào trọng lượng \x%l列車;#00ffc040;đoàn tàu%l;#;, tốc độ, tình trạng đường ray, v.v.—— | «\x%l列車;#00ffc040;tàu%l;#;.\nDù» → «\x%l列車;#00ffc040;đoàn tàu%l;#;.\nDù»; «\x%l列車;#00ffc040;tàu%l;#;,» → «\x%l列車;#00ffc040;đoàn tàu%l;#;,» |
| 共通13_勾配図.txt.toml | 1542 | 「\x%l共感;#00ffc040;共感%l;#;が通らぬなら、れいなが居眠りしているのだ！\nならば\x%l列車;#00ffc040;列車%l;#;は、他の方法で止める他ないっ！！」 | 「\x%l共感;#00ffc040;共鳴%l;#;不行的話，就說明玲奈在打瞌睡！既然這樣，只能用其他方法攔下\x%l列車;#00ffc040;列車%l;#;！！」 | 「Nếu \x%l共感;#00ffc040;cộng cảm%l;#; không kết nối được, thì tức là Reina đang ngủ gật!\nNếu vậy thì không còn cách nào khác ngoài việc dùng cách khác để dừng \x%l列車;#00ffc040;tàu%l;#; lại!!」 | 「Nếu \x%l共感;#00ffc040;cộng cảm%l;#; không kết nối được, thì tức là Reina đang ngủ gật!\nNếu vậy thì không còn cách nào khác ngoài việc dùng cách khác để dừng \x%l列車;#00ffc040;đoàn tàu%l;#; lại!!」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通13_勾配図.txt.toml | 1938 | 「ハチロク！　\x%l列車;#00ffc040;列車%l;#;を止める方法を！」 | 「八六！有什麼方法能讓\x%l列車;#00ffc040;列車%l;#;停下來！」 | 「Hachiroku! Cách để dừng \x%l列車;#00ffc040;tàu%l;#; lại!」 | 「Hachiroku! Cách để dừng \x%l列車;#00ffc040;đoàn tàu%l;#; lại!」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 共通13_勾配図.txt.toml | 2419 | 「シャツを脱いで、\x%l列車;#00ffc040;列車%l;#;に大きく振って合図を！」 | 「脫掉襯衫大力揮舞，給\x%l列車;#00ffc040;列車%l;#;打信號！」 | 「Hãy cởi áo sơ mi ra, vẫy thật mạnh để ra hiệu cho \x%l列車;#00ffc040;tàu%l;#;!」 | 「Hãy cởi áo sơ mi ra, vẫy thật mạnh để ra hiệu cho \x%l列車;#00ffc040;đoàn tàu%l;#;!」 | «\x%l列車;#00ffc040;tàu%l;#;!」» → «\x%l列車;#00ffc040;đoàn tàu%l;#;!」» |
| 共通14_負債.txt.toml | 1759 | 「矢印方向に進んだ\x%l列車;#00ffc040;列車%l;#;は、\nまず、[サンカク]△の底辺を進み切ります」 | 「朝箭頭方向前進的\x%l列車;#00ffc040;列車%l;#;，首先沿著三角形的底邊開到底」 | 「\x%l列車;#00ffc040;Tàu%l;#; di chuyển theo hướng mũi tên,\ntrước tiên sẽ đi hết cạnh đáy của hình tam giác △.」 | 「\x%l列車;#00ffc040;Đoàn tàu%l;#; di chuyển theo hướng mũi tên,\ntrước tiên sẽ đi hết cạnh đáy của hình tam giác △.」 | «「\x%l列車;#00ffc040;Tàu%l;#;» → «「\x%l列車;#00ffc040;Đoàn tàu%l;#;» |
| 共通15_回り始める動輪.txt.toml | 2126 | 「そうです、双鉄くん。\n\x%l列車;#00ffc040;列車%l;#;先頭の\x%lトレインマーク;#00ffc040;トレインマーク%l;#;は、\x%lヘッドマーク;#00ffc040;ヘッドマーク%l;#;です」 | 「是的，雙鐵君。\x%l列車;#00ffc040;列車%l;#;前面的\x%lトレインマーク;#00ffc040;車標%l;#;就叫做\x%lヘッドマーク;#00ffc040;頭標%l;#;」 | 「Đúng vậy, anh Soutetsu.\n\x%lトレインマーク;#00ffc040;Biểu trưng tàu%l;#; gắn ở đầu \x%l列車;#00ffc040;tàu%l;#; được gọi là \x%lヘッドマーク;#00ffc040;biểu trưng đầu tàu%l;#;.」 | 「Đúng vậy, anh Soutetsu.\n\x%lトレインマーク;#00ffc040;Biểu trưng tàu%l;#; gắn ở đầu \x%l列車;#00ffc040;đoàn tàu%l;#; được gọi là \x%lヘッドマーク;#00ffc040;biểu trưng đầu tàu%l;#;.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 凪ふかみ02_命の重さ.txt.toml | 1948 | バーベキュー\x%l列車;#00ffc040;列車%l;#;の乗務においてはもちろんのこと、\n訓練時にさえ、これほどの悪天候は経験してない。 | 在進行ＢＢＱ\x%l列車;#00ffc040;列車%l;#;的乘務工作的時候自不用說，就連訓練的時候也沒有經歷過如此惡劣的天氣。 | Trong lúc làm nhiệm vụ trên \x%l列車;#00ffc040;chuyến tàu%l;#; BBQ thì không nói làm gì,\nnhưng ngay cả trong lúc huấn luyện, tôi cũng chưa từng trải qua thời tiết khắc nghiệt đến thế này. | Trong lúc làm nhiệm vụ trên \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ thì không nói làm gì,\nnhưng ngay cả trong lúc huấn luyện, tôi cũng chưa từng trải qua thời tiết khắc nghiệt đến thế này. | «\x%l列車;#00ffc040;chuyến» → «\x%l列車;#00ffc040;đoàn» |
| 凪ふかみ03_三人いっしょ.txt.toml | 1561 | 「はい！　\n双鉄さんも、夜のバーベキュー\x%l列車;#00ffc040;列車%l;#;頑張ってください！」 | 「好的！雙鐵先生，晚上的ＢＢＱ\x%l列車;#00ffc040;列車%l;#;也要加油哦！」 | 「Vâng!\nAnh Soutetsu cũng cố gắng với chuyến \x%l列車;#00ffc040;tàu%l;#; BBQ tối nay nhé!」 | 「Vâng!\nAnh Soutetsu cũng cố gắng với chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ tối nay nhé!」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 凪ふかみ08c_新しい家族.txt.toml | 2735 | 家族という名の新しい列車に乗って。\nさらに輝く――未来へと。 | 乘著一輛名為家庭的新列車，向著更加閃耀的未來前進。 | Lên chuyến \x%l列車;#00ffc040;tàu%l;#; mới mang tên gia đình.\nHướng tới――một tương lai rực rỡ hơn. | Lên chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; mới mang tên gia đình.\nHướng tới――một tương lai rực rỡ hơn. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 日々姫03_客車手配.txt.toml | 2862 | 「なら決まりとね！　湯医から御一夜の最初の\x%l列車;#00ffc040;列車%l;#;、\n予約一番はウチとふかみちゃんとばい！」 | 「那就這麼決定啦！咱和小深第一個預約從湯醫開到御一夜的第一輛\x%l列車;#00ffc040;列車%l;#;！」 | 「Vậy là quyết định rồi nhé! Chuyến \x%l列車;#00ffc040;tàu%l;#; đầu tiên từ Yunoi về Ohitoyo,\nngười đặt chỗ số 1 là em và Fukami nha!」 | 「Vậy là quyết định rồi nhé! Chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; đầu tiên từ Yunoi về Ohitoyo,\nngười đặt chỗ số 1 là em và Fukami nha!」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 日々姫06_日々姫の決断.txt.toml | 2398 | 「\x%l列車;#00ffc040;列車%l;#;内広告や駅広告、路線広告などをフルパッケージで、\n隈元銀行として契約を結びたい――というお話です」 | 「他們想讓我們把\x%l列車;#00ffc040;列車%l;#;的內部廣告、車站廣告和線路廣告等等一起全包給隈元銀行」 | 「Đó là lời đề nghị muốn ký hợp đồng trọn gói cho quảng cáo trong \x%l列車;#00ffc040;tàu%l;#;,\nquảng cáo tại ga, quảng cáo trên tuyến đường... với tư cách là Ngân hàng Kumamoto.」 | 「Đó là lời đề nghị muốn ký hợp đồng trọn gói cho quảng cáo trong \x%l列車;#00ffc040;đoàn tàu%l;#;,\nquảng cáo tại ga, quảng cáo trên tuyến đường... với tư cách là Ngân hàng Kumamoto.」 | «\x%l列車;#00ffc040;tàu%l;#;,\nquảng» → «\x%l列車;#00ffc040;đoàn tàu%l;#;,\nquảng» |
| 日々姫08_開きかけのつぼみ.txt.toml | 3052 | \x%l客車;#00ffc040;客車%l;#;無しでは、\x%l8620;#00ffc040;8620%l;#;の観光\x%l列車;#00ffc040;列車%l;#;化は果たせない。\nそして現状、煙害直撃の隙間\x%l客車;#00ffc040;客車%l;#;しか僕らは持たない。 | 缺了\x%l客車;#00ffc040;客運車廂%l;#;就沒辦法把\x%l8620;#00ffc040;８６２０%l;#;打造成觀光\x%l列車;#00ffc040;列車%l;#;。而現在我們手裡只有一輛有縫隙會進煙的\x%l客車;#00ffc040;客運車廂%l;#;。 | Không có \x%l客車;#00ffc040;toa hành khách%l;#;, thì không thể biến \x%l8620;#00ffc040;8620%l;#; thành \x%l列車;#00ffc040;tàu%l;#; du lịch được.\nVà hiện tại, chúng tôi chỉ có duy nhất một \x%l客車;#00ffc040;toa hành khách%l;#; có khe hở khiến khói bay thẳng vào. | Không có \x%l客車;#00ffc040;toa hành khách%l;#;, thì không thể biến \x%l8620;#00ffc040;8620%l;#; thành \x%l列車;#00ffc040;đoàn tàu%l;#; du lịch được.\nVà hiện tại, chúng tôi chỉ có duy nhất một \x%l客車;#00ffc040;toa hành khách%l;#; có khe hở khiến khói bay thẳng vào. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇01_再蒸留.txt.toml | 1414 | 「ああ！　それが、“地元ごと”――それぞれの地元で、\nそれぞれの焼酎を飲める、焼酎\x%l列車;#00ffc040;列車%l;#;を走らせる」 | 「啊！是這樣的“各自在當地辦”——在各自的產地，開行可以喝當地燒酒的\x%l列車;#00ffc040;列車%l;#;啊」 | 「A! Vậy ra, “từng địa phương” là——chạy những chuyến \x%l列車;#00ffc040;tàu%l;#; shochu \nđể thưởng thức rượu shochu đặc trưng của từng địa phương.」 | 「A! Vậy ra, “từng địa phương” là——chạy những chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; shochu \nđể thưởng thức rượu shochu đặc trưng của từng địa phương.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇01_再蒸留.txt.toml | 1416 | 「あ！　なら、\nプレミア焼酎ば[の]飲みっ[くら]比できる\x%l列車;#00ffc040;列車%l;#;にすると？」 | 「啊！那就弄一輛可以品各種高級燒酒的\x%l列車;#00ffc040;列車%l;#;？」 | 「A! Vậy thì, \nsẽ làm thành một chuyến \x%l列車;#00ffc040;tàu%l;#; có thể uống thử các loại shochu hiếm sao?」 | 「A! Vậy thì, \nsẽ làm thành một chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; có thể uống thử các loại shochu hiếm sao?」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇01_再蒸留.txt.toml | 1452 | 「うん、そうだな、将来的には。もしも線路がつながれば、\n焼酎\x%l列車;#00ffc040;列車%l;#;でぐるり九洲――とさえ出来るかもしれん」 | 「嗯，是啊，將來如果線路連接到一起，說不定還能乘燒酒\x%l列車;#00ffc040;列車%l;#;環遊九州呢」 | 「Ừ, đúng vậy, trong tương lai. Nếu các tuyến đường sắt được kết nối, \nthậm chí chúng ta có thể đi một vòng Kyushu bằng \x%l列車;#00ffc040;tàu%l;#; shochu cũng nên.」 | 「Ừ, đúng vậy, trong tương lai. Nếu các tuyến đường sắt được kết nối, \nthậm chí chúng ta có thể đi một vòng Kyushu bằng \x%l列車;#00ffc040;đoàn tàu%l;#; shochu cũng nên.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇01_再蒸留.txt.toml | 1460 | 「と、いうのはどうだろう。\n\x%l列車;#00ffc040;列車%l;#;で酒を飲ませるというのがマズくなければ――」 | 「嗯，這樣怎麼樣呢。只要在\x%l列車;#00ffc040;列車%l;#;上喝酒不會有什麼麻煩的話——」 | 「Mọi người thấy thế nào. \nNếu việc cho uống rượu trên \x%l列車;#00ffc040;tàu%l;#; không có gì bất ổn thì——」 | 「Mọi người thấy thế nào. \nNếu việc cho uống rượu trên \x%l列車;#00ffc040;đoàn tàu%l;#; không có gì bất ổn thì——」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇01_再蒸留.txt.toml | 1504 | 「ね、双ちゃん。\nそん\x%l列車;#00ffc040;列車%l;#;ば、どんだけ走らせっと？」 | 「小雙，那種\x%l列車;#00ffc040;列車%l;#;你估摸一天開幾趟啊？」 | 「Này, Sou-chan. \nChuyến \x%l列車;#00ffc040;tàu%l;#; đó, em định cho chạy bao nhiêu chuyến?」 | 「Này, Sou-chan. \nChuyến \x%l列車;#00ffc040;đoàn tàu%l;#; đó, em định cho chạy bao nhiêu chuyến?」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇01_再蒸留.txt.toml | 1575 | 「良いですね――焼酎\x%l列車;#00ffc040;列車%l;#;を各地に点在させて。\nそして、将来的には。いずれ、きっと」 | 「挺好的呢——讓燒酒\x%l列車;#00ffc040;列車%l;#;散布在各個地方。而且將來肯定能——」 | 「Hay quá——Phân bố các chuyến \x%l列車;#00ffc040;tàu%l;#; shochu rải rác khắp nơi. \nVà rồi, trong tương lai. Một ngày nào đó, chắc chắn.」 | 「Hay quá——Phân bố các chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; shochu rải rác khắp nơi. \nVà rồi, trong tương lai. Một ngày nào đó, chắc chắn.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇01_再蒸留.txt.toml | 1590 | 「そうか――そのような\x%l列車;#00ffc040;列車%l;#;にしてしまえば、\nみなが飲みたがるのは、プレミア焼酎に偏るよな」 | 「是啊——要是弄出那種\x%l列車;#00ffc040;列車%l;#;的話，大家肯定會偏向想喝高級燒酒啊」 | 「Ra vậy——Nếu làm một chuyến \x%l列車;#00ffc040;tàu%l;#; như thế, \nthì ai cũng sẽ đổ xô đi uống các loại shochu hiếm nhỉ.」 | 「Ra vậy——Nếu làm một chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; như thế, \nthì ai cũng sẽ đổ xô đi uống các loại shochu hiếm nhỉ.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇01_再蒸留.txt.toml | 1716 | 「[ビール,1]麦酒\x%l列車;#00ffc040;列車%l;#;というものを走らせる私鉄は、\n鉄道全盛期には、決して珍しくはありませんでしたし」 | 「讓啤酒\x%l列車;#00ffc040;列車%l;#;上路行駛的私營鐵路在鐵路全盛期也絕不少見」 | 「Vào thời kỳ hoàng kim của đường sắt, những tuyến đường sắt tư nhân vận hành các chuyến \x%l列車;#00ffc040;tàu%l;#; bia \nhoàn toàn không phải là chuyện hiếm đâu ạ.」 | 「Vào thời kỳ hoàng kim của đường sắt, những tuyến đường sắt tư nhân vận hành các chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; bia \nhoàn toàn không phải là chuyện hiếm đâu ạ.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇01_再蒸留.txt.toml | 1779 | 「ならば、焼酎を飲める\x%l列車;#00ffc040;列車%l;#;を仕立ててはどうだろう」 | 「那我們弄一輛可以喝燒酒的\x%l列車;#00ffc040;列車%l;#;怎麼樣」 | 「Nếu vậy, chúng ta thiết kế một chuyến \x%l列車;#00ffc040;tàu%l;#; có thể uống rượu shochu thì sao?」 | 「Nếu vậy, chúng ta thiết kế một chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; có thể uống rượu shochu thì sao?」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇01_再蒸留.txt.toml | 1785 | 「では、飲み比べ\x%l列車;#00ffc040;列車%l;#;は実現不可能となりますか」 | 「那麼，品酒\x%l列車;#00ffc040;列車%l;#;就無法實現了嗎」 | 「Vậy là chuyến \x%l列車;#00ffc040;tàu%l;#; uống thử so sánh không thể thực hiện được sao ạ?」 | 「Vậy là chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; uống thử so sánh không thể thực hiện được sao ạ?」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇02_精髄.txt.toml | 1113 | 「\x%l列車;#00ffc040;列車%l;#;の自動\x%lブレーキ;#00ffc040;ブレーキ%l;#;は、空気圧がかかり続けることで\n解除されてる。圧力を抜けば、\x%lブレーキ;#00ffc040;ブレーキ%l;#;がかかる構造だ」 | 「\x%l列車;#00ffc040;列車%l;#;的自動\x%lブレーキ;#00ffc040;剎車%l;#;可以透過持續對空氣加壓來將其解除。在這個構造下如果將壓力降低\x%lブレーキ;#00ffc040;剎車%l;#;就會起作用」 | 「\x%lブレーキ;#00ffc040;Phanh%l;#; tự động của \x%l列車;#00ffc040;tàu%l;#; được nhả ra bằng cách liên tục duy trì áp suất không khí. \nCấu tạo của nó là khi xả áp suất thì \x%lブレーキ;#00ffc040;phanh%l;#; sẽ hoạt động.」 | 「\x%lブレーキ;#00ffc040;Phanh%l;#; tự động của \x%l列車;#00ffc040;đoàn tàu%l;#; được nhả ra bằng cách liên tục duy trì áp suất không khí. \nCấu tạo của nó là khi xả áp suất thì \x%lブレーキ;#00ffc040;phanh%l;#; sẽ hoạt động.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇02_精髄.txt.toml | 1528 | 「焼酎\x%l列車;#00ffc040;列車%l;#;の案が更に深まるかもしれないし、\n僕としては、是非とも乗ってもらいたい」 | 「其實我是很希望你能來列車上坐坐的，說不定這樣一來還可以最佳化燒酒\x%l列車;#00ffc040;列車%l;#;方案」 | 「Biết đâu ý tưởng về chuyến \x%l列車;#00ffc040;tàu%l;#; shochu sẽ càng sâu sắc hơn, \nvề phần tôi, tôi rất muốn chị thử lên ngồi.」 | 「Biết đâu ý tưởng về chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; shochu sẽ càng sâu sắc hơn, \nvề phần tôi, tôi rất muốn chị thử lên ngồi.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇02_精髄.txt.toml | 1780 | 「と、いうことだが。真闇姉から何か希望はあるか？\n焼酎\x%l列車;#00ffc040;列車%l;#;としても運用できるよう」 | 「於是，真闇姐你有什麼可以運用到燒酒\x%l列車;#00ffc040;列車%l;#;上的想法嗎？」 | 「Chuyện là vậy đó. Chị Mayami có nguyện vọng gì không? \nĐể có thể vận hành như một chuyến \x%l列車;#00ffc040;tàu%l;#; shochu.」 | 「Chuyện là vậy đó. Chị Mayami có nguyện vọng gì không? \nĐể có thể vận hành như một chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; shochu.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇02_精髄.txt.toml | 2535 | 焼酎\x%l列車;#00ffc040;列車%l;#;のアイディアも、無論大事なことではあるが。\nそれ以前。 | 燒酒\x%l列車;#00ffc040;列車%l;#;方案毫無疑問很重要，但是在此之上…… | Tất nhiên, ý tưởng về chuyến \x%l列車;#00ffc040;tàu%l;#; shochu cũng rất quan trọng. \nNhưng trước đó. | Tất nhiên, ý tưởng về chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; shochu cũng rất quan trọng. \nNhưng trước đó. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇03_ひとしずく.txt.toml | 1708 | 「すごかよねぇ。ほんまこつ、\n九洲ぐるり、焼酎\x%l列車;#00ffc040;列車%l;#;でめぐれる日も近かとかもねぇ」 | 「太棒了。這樣一來，或許燒酒\x%l列車;#00ffc040;列車%l;#;環繞全九州的那一天或許真的不遠了」 | 「Đỉnh thật đấy. Cứ đà này,\nngày mà \x%l列車;#00ffc040;tàu%l;#; shochu chạy một vòng quanh Kyushu chắc cũng không còn xa nữa đâu nhỉ.」 | 「Đỉnh thật đấy. Cứ đà này,\nngày mà \x%l列車;#00ffc040;đoàn tàu%l;#; shochu chạy một vòng quanh Kyushu chắc cũng không còn xa nữa đâu nhỉ.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇03_ひとしずく.txt.toml | 1735 | 「そう、七県めの参加だ。\nこれで九洲全県に、焼酎\x%l列車;#00ffc040;列車%l;#;が走ることになる」 | 「對，總共有七個縣參加。這樣一來，燒酒\x%l列車;#00ffc040;列車%l;#;就能在九州所有的縣行駛了」 | 「Đúng vậy, tỉnh thứ bảy tham gia rồi.\nThế này thì \x%l列車;#00ffc040;tàu%l;#; shochu sẽ chạy khắp toàn bộ các tỉnh ở Kyushu luôn.」 | 「Đúng vậy, tỉnh thứ bảy tham gia rồi.\nThế này thì \x%l列車;#00ffc040;đoàn tàu%l;#; shochu sẽ chạy khắp toàn bộ các tỉnh ở Kyushu luôn.」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 真闇03_ひとしずく.txt.toml | 1768 | 「焼酎\x%l列車;#00ffc040;列車%l;#;、また参加者が増えてくれたと？」 | 「想參與燒酒\x%l列車;#00ffc040;列車%l;#;的人又增多了？」 | 「\x%l列車;#00ffc040;Tàu%l;#; shochu, lại có thêm người tham gia sao?」 | 「\x%l列車;#00ffc040;Đoàn tàu%l;#; shochu, lại có thêm người tham gia sao?」 | «「\x%l列車;#00ffc040;Tàu%l;#;» → «「\x%l列車;#00ffc040;Đoàn tàu%l;#;» |
| 稀咲03_純白のレール.txt.toml | 1918 | 「おめでとうございます、ふたりとも。\n新婚旅行、\x%l列車;#00ffc040;列車%l;#;の旅がおすすめですよ？」 | 「恭喜你們。蜜月旅行就選\x%l列車;#00ffc040;列車%l;#;之旅怎麼樣？」 | 「Xin chúc mừng hai người.\nTuần trăng mật, tôi đề xuất một chuyến đi bằng \x%l列車;#00ffc040;tàu%l;#; nhé?」 | 「Xin chúc mừng hai người.\nTuần trăng mật, tôi đề xuất một chuyến đi bằng \x%l列車;#00ffc040;đoàn tàu%l;#; nhé?」 | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 稀咲03_純白のレール.txt.toml | 2513 | 復線が成り、\x%lエアクラ;#00ffc040;エアクラ%l;#;工場の千内移転が決定し。\n御一夜-鹿兒島間の観光\x%l列車;#00ffc040;列車%l;#;が走りだす。 | 我們成功恢復了廢線，讓\x%lエアクラ;#00ffc040;空凝機%l;#;工廠決定改在川內落戶。從御一夜到鹿兒島的觀光\x%l列車;#00ffc040;列車%l;#;也即將啟動。 | Khôi phục tuyến đường thành công, nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; quyết định chuyển đến Sendai.\nChuyến \x%l列車;#00ffc040;tàu%l;#; du lịch đoạn Ohitoyo - Kagoshima bắt đầu lăn bánh. | Khôi phục tuyến đường thành công, nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; quyết định chuyển đến Sendai.\nChuyến \x%l列車;#00ffc040;đoàn tàu%l;#; du lịch đoạn Ohitoyo - Kagoshima bắt đầu lăn bánh. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |
| 稀咲03_純白のレール.txt.toml | 2923 | 観光\x%l列車;#00ffc040;列車%l;#;第一号のニュースはそのまま、\n今日開始するＭＲＦ二期募集の宣伝にもなる。 | 首班觀光\x%l列車;#00ffc040;列車%l;#;的新聞也能成為今天開始的第二期集資的宣傳。 | Tin tức về chuyến \x%l列車;#00ffc040;tàu%l;#; du lịch đầu tiên sẽ trở thành\nlời quảng cáo cho đợt huy động MRF kỳ 2 bắt đầu từ hôm nay. | Tin tức về chuyến \x%l列車;#00ffc040;đoàn tàu%l;#; du lịch đầu tiên sẽ trở thành\nlời quảng cáo cho đợt huy động MRF kỳ 2 bắt đầu từ hôm nay. | «\x%l列車;#00ffc040;tàu%l;#;» → «\x%l列車;#00ffc040;đoàn tàu%l;#;» |

### G2 — 機関士 gloss → "lái tàu" (kể cả dòng gộp G2+T27) (83 dòng)

| File | Key | JP | TW | old_vn | fix | Đổi |
|---|---|---|---|---|---|---|
| れいな03_しゅっぱつしんこう.txt.toml | 2387 | 日々姫が急速に成長している今もなお、\nハチロクは僕を、最良の\x%l機関士;#00ffc040;機関士%l;#;と認めてくれてる。 | 雖然現在日日姬已經迅速地成長起來了，但八六仍然認為我是最好的\x%l機関士;#00ffc040;司機%l;#;。 | Ngay cả bây giờ, khi Hibiki đang trưởng thành nhanh chóng,\nHachiroku vẫn công nhận tôi là người \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; xuất sắc nhất. | Ngay cả bây giờ, khi Hibiki đang trưởng thành nhanh chóng,\nHachiroku vẫn công nhận tôi là người \x%l機関士;#00ffc040;lái tàu%l;#; xuất sắc nhất. | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;» → «tàu%l;#;» |
| グランドリライト01_オール御一夜、成立ならず.txt.toml | 2548 | 「イヤなどと、そのようなことは決して！\nけれど、\x%lレイルロオド;#00ffc040;レイルロオド%l;#;が、\x%l機関士;#00ffc040;機関士%l;#;に約束を強いるなど」 | 「我並不是嫌棄您！只是，我身為一介\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，實在無法強迫\x%l機関士;#00ffc040;司機%l;#;做出約定」 | 「Không phiền chút nào, tuyệt đối không ạ!\nThế nhưng, một \x%lレイルロオド;#00ffc040;Railord%l;#; sao có thể ép buộc \x%l機関士;#00ffc040;người lái tàu%l;#; hứa hẹn được...」 | 「Không phiền chút nào, tuyệt đối không ạ!\nThế nhưng, một \x%lレイルロオド;#00ffc040;Railord%l;#; sao có thể ép buộc \x%l機関士;#00ffc040;lái tàu%l;#; hứa hẹn được...」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| グランドリライト01_オール御一夜、成立ならず.txt.toml | 2585 | 「わたくしが双鉄様のお側に仕えるのは当然のこと。\n\x%l機関士;#00ffc040;機関士%l;#;と、\x%lレイルロオド;#00ffc040;レイルロオド%l;#;との間柄なのですから」 | 「我侍奉在雙鐵少爺身邊是理所當然的。畢竟我們可是\x%l機関士;#00ffc040;司機%l;#;和\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的關係」 | 「Việc tôi hầu hạ bên cạnh ngài Soutetsu là điều đương nhiên. Vì đó là mối quan hệ giữa \x%l機関士;#00ffc040;người lái tàu%l;#; và \x%lレイルロオド;#00ffc040;Railord%l;#; mà.」 | 「Việc tôi hầu hạ bên cạnh ngài Soutetsu là điều đương nhiên. Vì đó là mối quan hệ giữa \x%l機関士;#00ffc040;lái tàu%l;#; và \x%lレイルロオド;#00ffc040;Railord%l;#; mà.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| グランドリライト04_ポーレット.txt.toml | 1935 | 「うふふ、記念すべき第一号は、\nやっぱり\x%l機関士;#00ffc040;機関士%l;#;さんに、です！」 | 「嘿嘿，值得紀念的第一號徽章還是應該送給\x%l機関士;#00ffc040;司機%l;#;！」 | 「Ufufu, chiếc huy hiệu số một đáng nhớ này,\ntất nhiên phải dành tặng cho \x%l機関士;#00ffc040;người lái tàu%l;#; rồi!」 | 「Ufufu, chiếc huy hiệu số một đáng nhớ này,\ntất nhiên phải dành tặng cho \x%l機関士;#00ffc040;lái tàu%l;#; rồi!」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| グランドリライト06_稀咲.txt.toml | 2508 | 「当然のことです。双鉄様はわたくしの\x%l機関士;#00ffc040;機関士%l;#;。\nマスターになられたのですから」 | 「當然了。因為雙鐵少爺您成了我的\x%l機関士;#00ffc040;司機%l;#;，成了我的主人啊」 | 「Đó là điều hiển nhiên ạ. Ngài Soutetsu là \x%l機関士;#00ffc040;người lái tàu%l;#; của em.\nVì ngài đã trở thành Master của em mà.」 | 「Đó là điều hiển nhiên ạ. Ngài Soutetsu là \x%l機関士;#00ffc040;lái tàu%l;#; của em.\nVì ngài đã trở thành Master của em mà.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| グランドリライト10_ハチロク.txt.toml | 1582 | 「この日報にも驚きました。これほど簡潔に、\nかつ詳細に変調を観察できる\x%l機関士;#00ffc040;機関士%l;#;は珍しい」 | 「但這份日報也同樣令人吃驚。很少有\x%l機関士;#00ffc040;司機%l;#;能對異常狀況觀察得如此簡潔卻又詳盡」 | 「Tôi cũng rất ngạc nhiên trước bản báo cáo hàng ngày này. Một \x%l機関士;#00ffc040;người lái tàu%l;#; có thể quan sát sự thay đổi một cách ngắn gọn và chi tiết đến mức này quả là hiếm có」 | 「Tôi cũng rất ngạc nhiên trước bản báo cáo hàng ngày này. Một \x%l機関士;#00ffc040;lái tàu%l;#; có thể quan sát sự thay đổi một cách ngắn gọn và chi tiết đến mức này quả là hiếm có」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| グランドリライト10_ハチロク.txt.toml | 1776 | 「宗方\x%l機関士;#00ffc040;機関士%l;#;も、また、尊敬し、\n見習うべき方の一人であると思っています」 | 「宗方\x%l機関士;#00ffc040;司機%l;#;也是個值得我們尊敬和學習的人啊」 | 「Tôi cũng nghĩ \x%l機関士;#00ffc040;người lái tàu%l;#; Munakata là một trong những người đáng để tôn trọng và học hỏi」 | 「Tôi cũng nghĩ \x%l機関士;#00ffc040;lái tàu%l;#; Munakata là một trong những người đáng để tôn trọng và học hỏi」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| グランドリライト10_ハチロク.txt.toml | 1777 | 「宗方\x%l機関士;#00ffc040;機関士%l;#;は、オリヴィを物として扱います。\n一線を引き、踏み込まさせず――けれど、とても大切に」 | 「宗方\x%l機関士;#00ffc040;司機%l;#;把奧莉薇當成了一件物品。他絕不會做出任何越界之事——但依然非常關心她」 | 「\x%l機関士;#00ffc040;Người lái tàu%l;#; Munakata đối xử với Olivy như một món đồ.\nVạch ra ranh giới, không cho phép bước qua——nhưng lại vô cùng trân trọng」 | 「\x%l機関士;#00ffc040;Lái tàu%l;#; Munakata đối xử với Olivy như một món đồ.\nVạch ra ranh giới, không cho phép bước qua——nhưng lại vô cùng trân trọng」 | «「\x%l機関士;#00ffc040;Người lái» → «「\x%l機関士;#00ffc040;Lái» |
| グランドリライト10_ハチロク.txt.toml | 1993 | 「まさしく、そのとおりだと感じます。\n今日だけを見ても、宗方\x%l機関士;#00ffc040;機関士%l;#;は、そう徹底している」 | 「正如您所說。只看今天宗方\x%l機関士;#00ffc040;司機%l;#;的決定，就知道他依然在貫徹自己的作風」 | 「Tôi cảm thấy, quả đúng là như vậy.\nChỉ nhìn vào ngày hôm nay thôi, \x%l機関士;#00ffc040;người lái tàu%l;#; Munakata cũng đã triệt để như vậy」 | 「Tôi cảm thấy, quả đúng là như vậy.\nChỉ nhìn vào ngày hôm nay thôi, \x%l機関士;#00ffc040;lái tàu%l;#; Munakata cũng đã triệt để như vậy」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| グランドリライト11_ナインスターズ！.txt.toml | 2646 | 「汗を、僕が？　\x%l蒸気機関車;#00ffc040;蒸気機関車%l;#;の\x%l機関士;#00ffc040;機関士%l;#;が？\nたかだか駅までを走ったくらいで？」 | 「流汗？我可是\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;的\x%l機関士;#00ffc040;司機%l;#;，跑兩步路到車站而已，哪會流汗呢」 | 「Đổ mồ hôi, tôi á? \x%l機関士;#00ffc040;Người lái tàu%l;#; của \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; cơ mà?\nChỉ chạy đến ga thôi mà đổ mồ hôi sao?」 | 「Đổ mồ hôi, tôi á? \x%l機関士;#00ffc040;Lái tàu%l;#; của \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; cơ mà?\nChỉ chạy đến ga thôi mà đổ mồ hôi sao?」 | «\x%l機関士;#00ffc040;Người lái» → «\x%l機関士;#00ffc040;Lái» |
| ハチロク01_双鉄の目・ハチロクの目.txt.toml | 1808 | 「うん。一晩じっくりと考えてみたのだが、\n僕は、\x%l機関士;#00ffc040;機関士%l;#;に専念したいと思う」 | 「嗯。經過一夜的深思熟慮，我決定要專心做\x%l機関士;#00ffc040;司機%l;#;」 | 「Ừm. Sau một đêm suy nghĩ kỹ càng,\ntôi muốn chuyên tâm làm \x%l機関士;#00ffc040;người lái tàu%l;#;.」 | 「Ừm. Sau một đêm suy nghĩ kỹ càng,\ntôi muốn chuyên tâm làm \x%l機関士;#00ffc040;lái tàu%l;#;.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク01_双鉄の目・ハチロクの目.txt.toml | 2020 | 「そうだな。日常使う鉄道の\x%l機関士;#00ffc040;機関士%l;#;などは、\n人というより、装置であり、あるいは背景だろうから」 | 「沒錯。人們每天經鐵路出行，\x%l機関士;#00ffc040;司機%l;#;只會被當作是某種裝置，或者說是背景，而非一個特定的人」 | 「Đúng vậy. \x%l機関士;#00ffc040;Người lái tàu%l;#; của tuyến đường sắt được sử dụng hàng ngày,\nthay vì là một con người, thì giống như một cỗ máy, hay một bối cảnh hơn.」 | 「Đúng vậy. \x%l機関士;#00ffc040;Lái tàu%l;#; của tuyến đường sắt được sử dụng hàng ngày,\nthay vì là một con người, thì giống như một cỗ máy, hay một bối cảnh hơn.」 | «\x%l機関士;#00ffc040;Người lái» → «\x%l機関士;#00ffc040;Lái» |
| ハチロク02_8620運転台通信.txt.toml | 1902 | 「うぷぷ。なんだなんだ、真っ黒だのう。\nそちが\x%l機関士;#00ffc040;機関士%l;#;――[みぎたそうてつ,3]右田双鉄だな」 | 「噗噗。這樣一身黑，是怎麼弄出來的啊。你就是\x%l機関士;#00ffc040;司機%l;#;——右田雙鐵嗎」 | 「Upupu. Gì đây gì đây, đen thui thùi lùi luôn.\nNgươi chính là \x%l機関士;#00ffc040;người lái tàu%l;#;——Migita Soutetsu nhỉ.」 | 「Upupu. Gì đây gì đây, đen thui thùi lùi luôn.\nNgươi chính là \x%l機関士;#00ffc040;lái tàu%l;#;——Migita Soutetsu nhỉ.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク02_ハートブレイク・レイルロオド.txt.toml | 75 | \x%l機関士;#00ffc040;機関士%l;#;は、そのまままっすぐ\nポーレットの方へと向かっていく。 | \x%l機関士;#00ffc040;司機%l;#;便筆直地朝波萊特那邊走了過去。 | \x%l機関士;#00ffc040;Người lái tàu%l;#; cứ thế đi thẳng\nvề phía Paulette. | \x%l機関士;#00ffc040;Lái tàu%l;#; cứ thế đi thẳng\nvề phía Paulette. | «\x%l機関士;#00ffc040;Người lái» → «\x%l機関士;#00ffc040;Lái» |
| ハチロク02_ハートブレイク・レイルロオド.txt.toml | 2085 | 「今日も一日ご安全に、右田\x%l機関士;#00ffc040;機関士%l;#;」 | 「右田\x%l機関士;#00ffc040;司機%l;#;，希望您今天也能一如既往地安全行駛」 | 「Hôm nay cũng chúc ngài một ngày bình an, \x%l機関士;#00ffc040;người lái tàu%l;#; Migita.」 | 「Hôm nay cũng chúc ngài một ngày bình an, \x%l機関士;#00ffc040;lái tàu%l;#; Migita.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク02_ハートブレイク・レイルロオド.txt.toml | 2166 | 「え？　――あっ、はい。わかりました。双鉄く――\n右田\x%l機関士;#00ffc040;機関士%l;#;。そっち、おねがいできますか？」 | 「啊？啊，好的，沒問題。雙鐵——右田\x%l機関士;#00ffc040;司機%l;#;，這裡可以交給你處理嗎？」 | 「Dạ? ——A, vâng. Cháu hiểu rồi. Anh Soutetsu——\n\x%l機関士;#00ffc040;Người lái tàu%l;#; Migita. Bên đó, nhờ anh được không?」 | 「Dạ? ——A, vâng. Cháu hiểu rồi. Anh Soutetsu——\n\x%l機関士;#00ffc040;Lái tàu%l;#; Migita. Bên đó, nhờ anh được không?」 | «Soutetsu——\n\x%l機関士;#00ffc040;Người lái» → «Soutetsu——\n\x%l機関士;#00ffc040;Lái» |
| ハチロク02_ハートブレイク・レイルロオド.txt.toml | 2376 | 「御一夜鉄道運輸部長、\x%l保線部長;#00ffc040;保線部長%l;#;。\n兼、8620号のまいてつ蒸気\x%l機関士;#00ffc040;機関士%l;#;、右田双鉄だ」 | 「我是御一夜鐵路運輸部長及\x%l保線部長;#00ffc040;巡線部長%l;#;，兼８６２０號掌車人\x%l機関士;#00ffc040;司機%l;#;，右田雙鐵」 | 「Trưởng phòng Vận tải Đường sắt Ohitoyo, \x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;.\nKiêm chủ tàu 8620, \x%l機関士;#00ffc040;người lái tàu%l;#; hơi nước, Migita Soutetsu.」 | 「Trưởng phòng Vận tải Đường sắt Ohitoyo, \x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;.\nKiêm chủ tàu 8620, \x%l機関士;#00ffc040;lái tàu%l;#; hơi nước, Migita Soutetsu.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク02_ハートブレイク・レイルロオド.txt.toml | 3077 | 宗方\x%l機関士;#00ffc040;機関士%l;#;はレールショップへとポーレットに連れられ、\n振り向きもせずに消えていく。 | 宗方\x%l機関士;#00ffc040;司機%l;#;頭也不回一下，就隨波萊特前後走進了鐵路商店。 | \x%l機関士;#00ffc040;Người lái tàu%l;#; Munakata được Paulette dẫn vào Rail Shop,\nvà khuất dạng mà không thèm ngoảnh lại nhìn. | \x%l機関士;#00ffc040;Lái tàu%l;#; Munakata được Paulette dẫn vào Rail Shop,\nvà khuất dạng mà không thèm ngoảnh lại nhìn. | «\x%l機関士;#00ffc040;Người lái» → «\x%l機関士;#00ffc040;Lái» |
| ハチロク02_ハートブレイク・レイルロオド.txt.toml | 3147 | 恐らくは、宗方\x%l機関士;#00ffc040;機関士%l;#;の姿を探して―― | 應該是在尋找宗方\x%l機関士;#00ffc040;司機%l;#;吧—— | Có lẽ, em ấy đang tìm kiếm hình bóng của \x%l機関士;#00ffc040;người lái tàu%l;#; Munakata—— | Có lẽ, em ấy đang tìm kiếm hình bóng của \x%l機関士;#00ffc040;lái tàu%l;#; Munakata—— | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク02_ハートブレイク・レイルロオド.txt.toml | 3449 | （逆に言えば\x%l補機;#00ffc040;補機%l;#;ありとはいえ、それで矢岳を越えて来る\n宗方\x%l機関士;#00ffc040;機関士%l;#;とオリヴィとは――凄まじい腕なのだろうが） | （但反過來看，雖說掛了\x%l補機;#00ffc040;補機%l;#;，但他們卻能不帶司爐翻越矢岳到我們這裡，應該說宗方\x%l機関士;#00ffc040;司機%l;#;和奧莉薇技術過人嗎） | （Nói cách khác, dù có \x%l補機;#00ffc040;đầu máy phụ%l;#; đi chăng nữa, nhưng có thể vượt qua Yatake với tình trạng đó,\nthì \x%l機関士;#00ffc040;người lái tàu%l;#; Munakata và Olivy——chắc hẳn phải có tay nghề rất đáng nể.） | （Nói cách khác, dù có \x%l補機;#00ffc040;đầu máy phụ%l;#; đi chăng nữa, nhưng có thể vượt qua Yatake với tình trạng đó,\nthì \x%l機関士;#00ffc040;lái tàu%l;#; Munakata và Olivy——chắc hẳn phải có tay nghề rất đáng nể.） | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク03_冥国式レイルロオド.txt.toml | 2107 | 「右田では日々姫と混同するゆえ、\n公的な場では、双鉄\x%l機関士;#00ffc040;機関士%l;#;で頼む」 | 「叫右田的話就有可能和日日姬弄混了，所以在正式場合就叫我雙鐵\x%l機関士;#00ffc040;司機%l;#;吧」 | 「Gọi Migita thì sẽ nhầm với Hibiki mất,\nnên ở những nơi công cộng, cứ gọi anh là \x%l機関士;#00ffc040;người lái tàu%l;#; Soutetsu nhé.」 | 「Gọi Migita thì sẽ nhầm với Hibiki mất,\nnên ở những nơi công cộng, cứ gọi anh là \x%l機関士;#00ffc040;lái tàu%l;#; Soutetsu nhé.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク03_冥国式レイルロオド.txt.toml | 2420 | 「リョーカイ！　ヒビキ\x%l機関士;#00ffc040;機関士%l;#;！！」 | 「明白！日日姬\x%l機関士;#00ffc040;司機%l;#;！！」 | 「Đã rõ! \x%l機関士;#00ffc040;Người lái tàu%l;#; Hibiki!!」 | 「Đã rõ! \x%l機関士;#00ffc040;Lái tàu%l;#; Hibiki!!」 | «\x%l機関士;#00ffc040;Người lái» → «\x%l機関士;#00ffc040;Lái» |
| ハチロク03_冥国式レイルロオド.txt.toml | 2663 | 「じゃ、ソーテツサマのことなんて呼べばいい？\nミギタ\x%l機関士;#00ffc040;機関士%l;#;？　ソーテツサン？」 | 「那我該怎麼稱呼雙鐵少爺才好呢？右田\x%l機関士;#00ffc040;司機%l;#;？雙鐵先生？」 | 「Vậy, em nên gọi ngài Soutetsu là gì đây?\n\x%l機関士;#00ffc040;Người lái tàu%l;#; Migita? Anh Soutetsu?」 | 「Vậy, em nên gọi ngài Soutetsu là gì đây?\n\x%l機関士;#00ffc040;Lái tàu%l;#; Migita? Anh Soutetsu?」 | «đây?\n\x%l機関士;#00ffc040;Người lái» → «đây?\n\x%l機関士;#00ffc040;Lái» |
| ハチロク03_冥国式レイルロオド.txt.toml | 2679 | 「ソーテツ\x%l機関士;#00ffc040;機関士%l;#;。じゃ、ヒビキはヒビキ\x%l機関士;#00ffc040;機関士%l;#;？」 | 「雙鐵\x%l機関士;#00ffc040;司機%l;#;，好的。那日日姬就是日日姬\x%l機関士;#00ffc040;司機%l;#;囉？」 | 「\x%l機関士;#00ffc040;Người lái tàu%l;#; Soutetsu. Vậy, Hibiki là \x%l機関士;#00ffc040;người lái tàu%l;#; Hibiki hả?」 | 「\x%l機関士;#00ffc040;Lái tàu%l;#; Soutetsu. Vậy, Hibiki là \x%l機関士;#00ffc040;lái tàu%l;#; Hibiki hả?」 | «「\x%l機関士;#00ffc040;Người lái» → «「\x%l機関士;#00ffc040;Lái»; «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク03_冥国式レイルロオド.txt.toml | 2709 | 「オッケー！　じゃ、ソーテツとヒビキでっ！\n乗務のときはソーテツ\x%l機関士;#00ffc040;機関士%l;#;とヒビキ\x%l機関士;#00ffc040;機関士%l;#;っ！」 | 「ＯＫ！那就叫雙鐵和日日姬啦！執行乘務任務時候就是雙鐵\x%l機関士;#00ffc040;司機%l;#;和日日姬\x%l機関士;#00ffc040;司機%l;#;！」 | 「OK! Vậy, gọi là Soutetsu và Hibiki nha!\nKhi làm nhiệm vụ thì là \x%l機関士;#00ffc040;người lái tàu%l;#; Soutetsu và \x%l機関士;#00ffc040;người lái tàu%l;#; Hibiki!」 | 「OK! Vậy, gọi là Soutetsu và Hibiki nha!\nKhi làm nhiệm vụ thì là \x%l機関士;#00ffc040;lái tàu%l;#; Soutetsu và \x%l機関士;#00ffc040;lái tàu%l;#; Hibiki!」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái»; «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク03_冥国式レイルロオド.txt.toml | 3108 | 凪もⅨ号の\x%l機関士;#00ffc040;機関士%l;#;になりたがっているが、\nこの相性が乗務に活きれば、日々姫が優勢かもしれん。 | 姑且凪也是九號的候選\x%l機関士;#00ffc040;司機%l;#;之一，不過若是這合拍也能體現在乘務工作上的話，日日姬恐怕就頗有優勢了。 | Nagi cũng muốn trở thành \x%l機関士;#00ffc040;người lái tàu%l;#; của Đầu máy số 9,\nnhưng nếu sự ăn ý này được phát huy trong công việc, thì Hibiki có thể sẽ chiếm ưu thế hơn. | Nagi cũng muốn trở thành \x%l機関士;#00ffc040;lái tàu%l;#; của Đầu máy số 9,\nnhưng nếu sự ăn ý này được phát huy trong công việc, thì Hibiki có thể sẽ chiếm ưu thế hơn. | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク07_ハチロクの目覚め.txt.toml | 2085 | ハチロクを助けると決めたとき。\n\x%l機関士;#00ffc040;機関士%l;#;になると、自らの意思で選んだ、あのとき。 | 在我決定要幫助八六的時候，在我自己選擇了要成為\x%l機関士;#00ffc040;司機%l;#;的時候。 | Khi quyết định cứu Hachiroku.\nKhi tự mình lựa chọn trở thành \x%l機関士;#00ffc040;thợ lái đầu máy%l;#;, vào lúc đó. | Khi quyết định cứu Hachiroku.\nKhi tự mình lựa chọn trở thành \x%l機関士;#00ffc040;lái tàu%l;#;, vào lúc đó. | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;,» → «tàu%l;#;,» |
| ハチロク07_ハチロクの目覚め.txt.toml | 2316 | だから、\n\x%l機関士;#00ffc040;機関士%l;#;として直接苦情に対応したいし、お詫びしたい。 | 所以，我作為\x%l機関士;#00ffc040;司機%l;#;理應親自前往賠禮道歉。 | Vì vậy,\ntôi muốn trực tiếp giải quyết khiếu nại và xin lỗi với tư cách là \x%l機関士;#00ffc040;thợ lái đầu máy%l;#;. | Vì vậy,\ntôi muốn trực tiếp giải quyết khiếu nại và xin lỗi với tư cách là \x%l機関士;#00ffc040;lái tàu%l;#;. | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;.» → «tàu%l;#;.» |
| ハチロク10_炙り出し.txt.toml | 2694 | \x%l機関士;#00ffc040;機関士%l;#;の僕をたて、控えてくれていたのだろうか。\n水を向けられハチロクは、流れるように話し始める。 | 看來八六剛才尊重作為\x%l機関士;#00ffc040;司機%l;#;的我沒有插嘴。如今話題拋向了八六，她就順著話題發展說了下去。 | Có lẽ em ấy đã nhường lời để tôn trọng \x%l機関士;#00ffc040;người lái tàu%l;#; là tôi chăng.\nĐược tôi gợi ý, Hachiroku bắt đầu trình bày một cách trôi chảy. | Có lẽ em ấy đã nhường lời để tôn trọng \x%l機関士;#00ffc040;lái tàu%l;#; là tôi chăng.\nĐược tôi gợi ý, Hachiroku bắt đầu trình bày một cách trôi chảy. | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク11_幽霊.txt.toml | 2701 | もちろん、多少は離れても、\n\x%l機関士;#00ffc040;機関士%l;#;と\x%lレイルロオド;#00ffc040;レイルロオド%l;#;です。 | 當然，即便如此，\x%l機関士;#00ffc040;司機%l;#;與\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的關係也並不會改變。 | Tất nhiên, dù có xa cách đôi chút,\nnhưng chúng em vẫn là \x%l機関士;#00ffc040;người lái tàu%l;#; và \x%lレイルロオド;#00ffc040;Railord%l;#;. | Tất nhiên, dù có xa cách đôi chút,\nnhưng chúng em vẫn là \x%l機関士;#00ffc040;lái tàu%l;#; và \x%lレイルロオド;#00ffc040;Railord%l;#;. | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク11_御一夜鉄道小畑線.txt.toml | 2197 | 「不要でしつこい助言。清春。電車\x%l運転士;#00ffc040;運転士%l;#;になるまえ。\n\x%l機関士;#00ffc040;機関士%l;#;。[こうばい,1]勾配路線――[ひたひこやま,4]肥田飛虎山線だって経験済み」 | 「這樣的建議，並無必要。清春在轉做電車\x%l運転士;#00ffc040;駕駛員%l;#;前，作為\x%l機関士;#00ffc040;司機%l;#;，就有爬坡線路——日田彥山線——的駕駛經驗了」 | 「Lời khuyên dư thừa và dai dẳng. Kiyoharu. Trước khi trở thành \x%l運転士;#00ffc040;người lái tàu%l;#; điện. \nĐã từng là \x%l機関士;#00ffc040;người lái tàu%l;#; hơi nước. Tuyến đường dốc——Tuyến Hitahikoyama cũng đã từng có kinh nghiệm rồi.」 | 「Lời khuyên dư thừa và dai dẳng. Kiyoharu. Trước khi trở thành \x%l運転士;#00ffc040;người lái tàu%l;#; điện. \nĐã từng là \x%l機関士;#00ffc040;lái tàu%l;#; hơi nước. Tuyến đường dốc——Tuyến Hitahikoyama cũng đã từng có kinh nghiệm rồi.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク14_冬.txt.toml | 2342 | 「実際にお見舞いしたのはニイロクだけだったけど。\n赤井\x%l機関士;#00ffc040;機関士%l;#;、買い物に付き合わされたって」 | 「不過就二六上去看了看奧莉薇，赤井\x%l機関士;#00ffc040;司機%l;#;是陪她買東西一起來的」 | 「Nhưng người thực sự đến thăm chỉ có Niiroku thôi.\n\x%l機関士;#00ffc040;Thợ lái đầu máy%l;#; Akai bảo là bị kéo đi mua sắm cùng.」 | 「Nhưng người thực sự đến thăm chỉ có Niiroku thôi.\n\x%l機関士;#00ffc040;Lái tàu%l;#; Akai bảo là bị kéo đi mua sắm cùng.」 | «thôi.\n\x%l機関士;#00ffc040;Thợ» → «thôi.\n\x%l機関士;#00ffc040;Lái»; «lái đầu máy%l;#;» → «tàu%l;#;» |
| ハチロク14_冬.txt.toml | 2371 | 「ニイロク、すぐおりてきて、『お邪魔した』って。\nあんまり早くて、赤井\x%l機関士;#00ffc040;機関士%l;#;も驚いた顔しとった」 | 「二六隨時就下來準備回去，那這速度快得，把赤井\x%l機関士;#00ffc040;司機%l;#;都給嚇一跳」 | 「Niiroku xuống ngay lập tức, rồi bảo 『Xin lỗi vì đã làm phiền』.\nNhanh quá mức khiến \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai cũng phải tròn mắt ngạc nhiên.」 | 「Niiroku xuống ngay lập tức, rồi bảo 『Xin lỗi vì đã làm phiền』.\nNhanh quá mức khiến \x%l機関士;#00ffc040;lái tàu%l;#; Akai cũng phải tròn mắt ngạc nhiên.」 | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;» → «tàu%l;#;» |
| ハチロク14_冬.txt.toml | 2497 | 「短かかったと！　赤井\x%l機関士;#00ffc040;機関士%l;#;を放ってもおけんけん\nわたし、ここでお茶お出ししとったんだけど」 | 「可不是唄！我又不能晾著赤井\x%l機関士;#00ffc040;司機%l;#;，這不還給人泡了茶吶」 | 「Ngắn lắm luôn! Em không thể bỏ mặc \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai được\nnên đã pha trà mời ở đây, nhưng mà.」 | 「Ngắn lắm luôn! Em không thể bỏ mặc \x%l機関士;#00ffc040;lái tàu%l;#; Akai được\nnên đã pha trà mời ở đây, nhưng mà.」 | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;» → «tàu%l;#;» |
| ハチロク14_冬.txt.toml | 2851 | 「赤井\x%l機関士;#00ffc040;機関士%l;#;には、お二方と凪と情報を出し合って、\n常時監視候補者のリスト作成をお願いしたく思います」 | 「我希望赤井\x%l機関士;#00ffc040;司機%l;#;能和凪還有流和治兩位先生交換意見，完成參與全天監視的成員候補名單」 | 「Tôi muốn nhờ \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai cùng hai ông ấy và Nagi trao đổi thông tin,\nđể lập danh sách các ứng viên giám sát thường trực.」 | 「Tôi muốn nhờ \x%l機関士;#00ffc040;lái tàu%l;#; Akai cùng hai ông ấy và Nagi trao đổi thông tin,\nđể lập danh sách các ứng viên giám sát thường trực.」 | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;» → «tàu%l;#;» |
| ハチロク14_冬.txt.toml | 2920 | 「だよ？　昨日、赤井\x%l機関士;#00ffc040;機関士%l;#;といっしょに」 | 「是呀，昨天跟赤井\x%l機関士;#00ffc040;司機%l;#;一起來的」 | 「Đúng vậy? Hôm qua, cùng với \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai đó.」 | 「Đúng vậy? Hôm qua, cùng với \x%l機関士;#00ffc040;lái tàu%l;#; Akai đó.」 | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;» → «tàu%l;#;» |
| ハチロク14_冬.txt.toml | 3155 | 「赤井\x%l機関士;#00ffc040;機関士%l;#;もか」 | 「連赤井\x%l機関士;#00ffc040;司機%l;#;都來了嗎」 | 「Cả \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai nữa sao.」 | 「Cả \x%l機関士;#00ffc040;lái tàu%l;#; Akai nữa sao.」 | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;» → «tàu%l;#;» |
| ハチロク14_冬.txt.toml | 3854 | 手短に要点だけを確認し、\n電話を切って、赤井\x%l機関士;#00ffc040;機関士%l;#;へと向き直る。 | 我就簡單問了一下他們對主要情況的了解程度，而後掛上電話再次向赤井\x%l機関士;#00ffc040;司機%l;#;開口。 | Tôi xác nhận ngắn gọn những điểm chính,\nrồi cúp máy, quay sang \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai. | Tôi xác nhận ngắn gọn những điểm chính,\nrồi cúp máy, quay sang \x%l機関士;#00ffc040;lái tàu%l;#; Akai. | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;» → «tàu%l;#;» |
| ハチロク14_冬.txt.toml | 3983 | 確かに、\x%l運転体;#00ffc040;運転体%l;#;では買い物にも不自由しよう。\n赤井\x%l機関士;#00ffc040;機関士%l;#;も、いつもながらとはいえご苦労なことだ。 | 的確，二六隻有\x%l運転体;#00ffc040;駕駛體%l;#;，購物時也多有不便。雖然估計赤井\x%l機関士;#00ffc040;司機%l;#;也是習以為常，但仔細一想著實也是不容易。 | Đúng là, với \x%l運転体;#00ffc040;thân vận hành%l;#; thì việc mua sắm cũng bất tiện.\n\x%l機関士;#00ffc040;Thợ lái đầu máy%l;#; Akai, dù là chuyện thường ngày nhưng cũng vất vả thật. | Đúng là, với \x%l運転体;#00ffc040;thân vận hành%l;#; thì việc mua sắm cũng bất tiện.\n\x%l機関士;#00ffc040;Lái tàu%l;#; Akai, dù là chuyện thường ngày nhưng cũng vất vả thật. | «tiện.\n\x%l機関士;#00ffc040;Thợ» → «tiện.\n\x%l機関士;#00ffc040;Lái»; «lái đầu máy%l;#;» → «tàu%l;#;» |
| ハチロク14_冬.txt.toml | 4065 | ポーレット様に、れいなに、ニイロクに、赤井\x%l機関士;#00ffc040;機関士%l;#;に。\n縁ある全ての存在に、今の言葉を、ただ、届けたい。 | 還有波萊特小姐、玲奈、二六、赤井\x%l機関士;#00ffc040;司機%l;#;，以及其他所有與御一夜密不可分的人們，都聽到她方才這句飽含喜悅的話語。 | Cho cô Paulette, cho Reina, cho Niiroku, cho \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai.\nEm chỉ muốn truyền đạt lại những lời vừa rồi, cho tất cả những người có duyên gặp gỡ. | Cho cô Paulette, cho Reina, cho Niiroku, cho \x%l機関士;#00ffc040;lái tàu%l;#; Akai.\nEm chỉ muốn truyền đạt lại những lời vừa rồi, cho tất cả những người có duyên gặp gỡ. | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;» → «tàu%l;#;» |
| ハチロク14_橋.txt.toml | 2368 | 事故の、そのあと。\x%l機関士;#00ffc040;機関士%l;#;からも仲間からも。\n同じ時間を過ごした存在、全てから―― | 在事故之後，不管是\x%l機関士;#00ffc040;司機%l;#;還是同伴，曾與她共度時光的所有人都將她拋棄—— | Sau vụ tai nạn đó. Từ \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; cho đến những người đồng đội.\nTừ tất cả những người đã cùng chung sống trong khoảng thời gian đó—— | Sau vụ tai nạn đó. Từ \x%l機関士;#00ffc040;lái tàu%l;#; cho đến những người đồng đội.\nTừ tất cả những người đã cùng chung sống trong khoảng thời gian đó—— | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;» → «tàu%l;#;» |
| ハチロク14_橋.txt.toml | 2374 | 助士が不在で、僕が投げ込みに回る以上、\n\x%l機関士;#00ffc040;機関士%l;#;として\x%l8620;#00ffc040;8620%l;#;を運転するのは、ハチロクだ。 | 在沒有司爐，必須由我來加煤的情況下，是八六在作為\x%l機関士;#00ffc040;司機%l;#;駕駛\x%l8620;#00ffc040;８６２０%l;#;。 | Vì không có phụ lái tàu, tôi phải quay sang xúc than,\nnên người lái \x%l8620;#00ffc040;8620%l;#; với tư cách là \x%l機関士;#00ffc040;thợ lái đầu máy%l;#;, chính là Hachiroku. | Vì không có phụ lái tàu, tôi phải quay sang xúc than,\nnên người lái \x%l8620;#00ffc040;8620%l;#; với tư cách là \x%l機関士;#00ffc040;lái tàu%l;#;, chính là Hachiroku. | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;,» → «tàu%l;#;,» |
| ハチロク14_橋.txt.toml | 2678 | \x%l機関士;#00ffc040;機関士%l;#;の僕と、\x%l運転体;#00ffc040;運転体%l;#;のハチロクとで組んでるときの――\n背中を完全に預けあえている安心感が、今は無い。 | 現在我感覺不到由我擔當\x%l機関士;#00ffc040;司機%l;#;與使用\x%l運転体;#00ffc040;駕駛體%l;#;的八六搭檔時那種能將身後完全託付給對方的安全感。 | Cảm giác an tâm khi tôi làm \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; kết hợp với \x%l運転体;#00ffc040;thân vận hành%l;#; của Hachiroku——\ncảm giác có thể hoàn toàn giao phó tấm lưng cho nhau, bây giờ không còn nữa. | Cảm giác an tâm khi tôi làm \x%l機関士;#00ffc040;lái tàu%l;#; kết hợp với \x%l運転体;#00ffc040;thân vận hành%l;#; của Hachiroku——\ncảm giác có thể hoàn toàn giao phó tấm lưng cho nhau, bây giờ không còn nữa. | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;» → «tàu%l;#;» |
| ハチロク14_橋.txt.toml | 2927 | （ハチロクが――\x%l機関士;#00ffc040;機関士%l;#;役など） | （居然要由八六來擔任\x%l機関士;#00ffc040;司機%l;#;） | （Để Hachiroku——đóng vai trò \x%l機関士;#00ffc040;thợ lái đầu máy%l;#;） | （Để Hachiroku——đóng vai trò \x%l機関士;#00ffc040;lái tàu%l;#;） | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;）» → «tàu%l;#;）» |
| ハチロク15a_痛みとの決別.txt.toml | 2031 | 「礼を言う。\n今の俺は、お前にとって、\x%l機関士;#00ffc040;機関士%l;#;でもなんでもないのに」 | 「我要謝謝你。明明我都不是你的\x%l機関士;#00ffc040;司機%l;#;了」 | 「Cảm ơn cô.\nDù tao bây giờ, đối với cô, chẳng còn là \x%l機関士;#00ffc040;người lái tàu%l;#; hay gì nữa」 | 「Cảm ơn cô.\nDù tao bây giờ, đối với cô, chẳng còn là \x%l機関士;#00ffc040;lái tàu%l;#; hay gì nữa」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク15b_さよなら列車.txt.toml | 1577 | 「\x%l機関士;#00ffc040;機関士%l;#;さんたちにお差し入れ」 | 「咱是來慰勞\x%l機関士;#00ffc040;司機%l;#;們的」 | 「Chị mang đồ tiếp tế cho các \x%l機関士;#00ffc040;người lái tàu%l;#; đây」 | 「Chị mang đồ tiếp tế cho các \x%l機関士;#00ffc040;lái tàu%l;#; đây」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク15b_さよなら列車.txt.toml | 1721 | 「日々姫、\x%l機関士;#00ffc040;機関士%l;#;に！　僕が助士をやる」 | 「日日姬，你去當\x%l機関士;#00ffc040;司機%l;#;，我來當司爐」 | 「Hibiki, làm \x%l機関士;#00ffc040;người lái tàu%l;#;! Anh sẽ làm phụ lái」 | 「Hibiki, làm \x%l機関士;#00ffc040;lái tàu%l;#;! Anh sẽ làm phụ lái」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ハチロク15b_さよなら列車.txt.toml | 2333 | （ふかみも、凪も――ニイロクも赤井\x%l機関士;#00ffc040;機関士%l;#;も、\nポーレットもれいなも――みんな、同じだ） | （深美、凪、二六、赤井\x%l機関士;#00ffc040;司機%l;#;、波萊特、玲奈——大家的心意都是一樣的） | （Cả Fukami, Nagi——Niiroku và \x%l機関士;#00ffc040;người lái tàu%l;#; Akai,\ncả Paulette và Reina nữa——tất cả mọi người, đều có chung một tâm trạng） | （Cả Fukami, Nagi——Niiroku và \x%l機関士;#00ffc040;lái tàu%l;#; Akai,\ncả Paulette và Reina nữa——tất cả mọi người, đều có chung một tâm trạng） | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| ポーレット03_廃炭鉱.txt.toml | 2814 | 慣れぬ\x%lキハ07;#00ffc040;キハ07%l;#;の\x%l運転台;#00ffc040;運転台%l;#;で、\n\x%l機関助士;#00ffc040;機関助士%l;#;でも\x%l機関士;#00ffc040;機関士%l;#;でもない、\x%l運転士;#00ffc040;運転士%l;#;役。 | 站在還不熟悉的\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;的\x%l運転台;#00ffc040;駕駛台%l;#;上，此刻的日日姬既不是\x%l機関助士;#00ffc040;司爐%l;#;也不是\x%l機関士;#00ffc040;司機%l;#;，而是\x%l運転士;#00ffc040;駕駛員%l;#;。 | Trong \x%l運転台;#00ffc040;buồng lái%l;#; của \x%lキハ07;#00ffc040;KiHa 07%l;#; mà em còn chưa quen, Hibiki lúc này không phải \x%l機関助士;#00ffc040;phụ lái%l;#; cũng không phải \x%l機関士;#00ffc040;Người lái tàu%l;#;, mà đang đóng vai trò \x%l運転士;#00ffc040;người lái%l;#;. | Trong \x%l運転台;#00ffc040;buồng lái%l;#; của \x%lキハ07;#00ffc040;KiHa 07%l;#; mà em còn chưa quen, Hibiki lúc này không phải \x%l機関助士;#00ffc040;phụ lái%l;#; cũng không phải \x%l機関士;#00ffc040;Lái tàu%l;#;, mà đang đóng vai trò \x%l運転士;#00ffc040;người lái%l;#;. | «\x%l機関士;#00ffc040;Người lái» → «\x%l機関士;#00ffc040;Lái» |
| ポーレット10_見えない傷.txt.toml | 959 | “僕ほど経験の乏しい者が、\x%l機関士;#00ffc040;機関士%l;#;などとおこがましい”\n真っ先に頭に浮かぶ答えは、呑み込むしか無い。 | “像我這樣缺乏經驗的人，要以\x%l機関士;#00ffc040;司機%l;#;自居也未免太狂妄自大了”——我不得不將這句到了嘴邊的話咽回去。 | “Một kẻ thiếu kinh nghiệm như tôi mà tự nhận là \x%l機関士;#00ffc040;nhân viên cơ vụ%l;# thì thật quá tự cao”\nTôi đành phải nuốt ngược câu trả lời nảy ra đầu tiên trong đầu mình xuống. | “Một kẻ thiếu kinh nghiệm như tôi mà tự nhận là \x%l機関士;#00ffc040;lái tàu%l;# thì thật quá tự cao”\nTôi đành phải nuốt ngược câu trả lời nảy ra đầu tiên trong đầu mình xuống. | «\x%l機関士;#00ffc040;nhân» → «\x%l機関士;#00ffc040;lái»; «viên cơ vụ%l;#» → «tàu%l;#» |
| ポーレット10_見えない傷.txt.toml | 1241 | 「さすが、\x%l機関士;#00ffc040;機関士%l;#;さんは違いますね。\n冷静で、ポイントつかむのが上手いです」 | 「不愧是\x%l機関士;#00ffc040;司機%l;#;，就是與平常人不一樣呀。頭腦冷靜，悟性也高」 | 「Quả nhiên, \x%l機関士;#00ffc040;nhân viên cơ vụ%l;# có khác nhỉ.\nAnh rất bình tĩnh và nắm bắt trọng tâm rất tốt.」 | 「Quả nhiên, \x%l機関士;#00ffc040;lái tàu%l;# có khác nhỉ.\nAnh rất bình tĩnh và nắm bắt trọng tâm rất tốt.」 | «\x%l機関士;#00ffc040;nhân» → «\x%l機関士;#00ffc040;lái»; «viên cơ vụ%l;#» → «tàu%l;#» |
| 共通03_ハチロクとナビ.txt.toml | 1638 | 「それももちろん。駆動車両および\x%l列車;#00ffc040;列車%l;#;の制御は、\n\x%lレイルロオド;#00ffc040;レイルロオド%l;#;と、\x%l機関士;#00ffc040;機関士%l;#;・\x%l運転士;#00ffc040;運転士%l;#;との共同で行います」 | 「那當然。牽引車以及\x%l列車;#00ffc040;列車%l;#;的控制，是由\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;與\x%l機関士;#00ffc040;司機%l;#;、\x%l運転士;#00ffc040;駕駛員%l;#;共同完成的」 | 「Đó là điều hiển nhiên ạ. Việc điều khiển phương tiện động lực và \x%l列車;#00ffc040;đoàn tàu%l;#;,\nsẽ do \x%lレイルロオド;#00ffc040;Railord%l;#; cùng với \x%l機関士;#00ffc040;người lái tàu%l;#; hoặc \x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; phối hợp thực hiện.」 | 「Đó là điều hiển nhiên ạ. Việc điều khiển phương tiện động lực và \x%l列車;#00ffc040;đoàn tàu%l;#;,\nsẽ do \x%lレイルロオド;#00ffc040;Railord%l;#; cùng với \x%l機関士;#00ffc040;lái tàu%l;#; hoặc \x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; phối hợp thực hiện.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 共通03_ハチロクとナビ.txt.toml | 2108 | 機関車を運転する人間が\x%l機関士;#00ffc040;機関士%l;#;。\nそれ以外の駆動車両を運転するのが\x%l運転士;#00ffc040;運転士%l;#;と教えてもらう。 | 駕駛機車的人就叫\x%l機関士;#00ffc040;司機%l;#;。駕駛其他車輛的則被稱作\x%l運転士;#00ffc040;駕駛員%l;#;。 | Người lái đầu máy xe lửa thì gọi là \x%l機関士;#00ffc040;người lái tàu%l;#;.\nCòn người điều khiển các phương tiện động lực khác thì gọi là \x%l運転士;#00ffc040;nhân viên cơ vụ%l;#;, tôi được dạy như vậy. | Người lái đầu máy xe lửa thì gọi là \x%l機関士;#00ffc040;lái tàu%l;#;.\nCòn người điều khiển các phương tiện động lực khác thì gọi là \x%l運転士;#00ffc040;nhân viên cơ vụ%l;#;, tôi được dạy như vậy. | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 共通05_ようやく石炭.txt.toml | 2252 | 「これをすれば\x%l機関士;#00ffc040;機関士%l;#;になれるというなら。\n無論、やるさ」 | 「只要做好這個就可以成為\x%l機関士;#00ffc040;司機%l;#;的話，沒問題，我做」 | 「Nếu làm thế này mà có thể trở thành \x%l機関士;#00ffc040;người lái tàu%l;#;.\nThì tất nhiên, tôi sẽ làm.」 | 「Nếu làm thế này mà có thể trở thành \x%l機関士;#00ffc040;lái tàu%l;#;.\nThì tất nhiên, tôi sẽ làm.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 共通05_ようやく石炭.txt.toml | 2432 | 「わたくしは、双鉄様にわたくしの\x%l機関士;#00ffc040;機関士%l;#;に――\nマスターになっていただきたく望んでいます」 | 「我希望，雙鐵少爺可以成為與我搭檔的，我的\x%l機関士;#00ffc040;司機%l;#;」 | 「Tôi rất mong ngài Soutetsu sẽ trở thành \x%l機関士;#00ffc040;người lái tàu%l;#;——\nTrở thành Master của tôi.」 | 「Tôi rất mong ngài Soutetsu sẽ trở thành \x%l機関士;#00ffc040;lái tàu%l;#;——\nTrở thành Master của tôi.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 共通05_ようやく石炭.txt.toml | 2505 | 「はい。なぜならわたくしにはマスター。\n\x%l機関士;#00ffc040;機関士%l;#;がまだ、いないからです」 | 「是的。要問為何的話，因為我還沒有可以搭檔的\x%l機関士;#00ffc040;司機%l;#;」 | 「Vâng. Bởi vì tôi vẫn chưa có Master.\nTôi vẫn chưa có \x%l機関士;#00ffc040;người lái tàu%l;#;.」 | 「Vâng. Bởi vì tôi vẫn chưa có Master.\nTôi vẫn chưa có \x%l機関士;#00ffc040;lái tàu%l;#;.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 共通05_ようやく石炭.txt.toml | 2727 | 「ならば、ハチロク。\n僕はお前の\x%l機関士;#00ffc040;機関士%l;#;と」 | 「那麼，八六。就由我來當你的\x%l機関士;#00ffc040;司機%l;#;」 | 「Nếu vậy, Hachiroku. Tôi sẽ trở thành \x%l機関士;#00ffc040;người lái tàu%l;#; của em.」 | 「Nếu vậy, Hachiroku. Tôi sẽ trở thành \x%l機関士;#00ffc040;lái tàu%l;#; của em.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 共通05_ようやく石炭.txt.toml | 3140 | 鉄道全盛だったころにも、\n\x%lレイルロオド;#00ffc040;レイルロオド%l;#;が\x%l機関士;#00ffc040;機関士%l;#;候補に指導をしていたのだろうか？ | 在鐵路全盛的時期，也曾是由\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;對\x%l機関士;#00ffc040;司機%l;#;候補進行指導的嗎？ | Vào thời kỳ hoàng kim của đường sắt,\ncác \x%lレイルロオド;#00ffc040;Railord%l;#; cũng từng hướng dẫn cho các ứng viên \x%l機関士;#00ffc040;người lái tàu%l;#; sao? | Vào thời kỳ hoàng kim của đường sắt,\ncác \x%lレイルロオド;#00ffc040;Railord%l;#; cũng từng hướng dẫn cho các ứng viên \x%l機関士;#00ffc040;lái tàu%l;#; sao? | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 共通06_8620を探せ.txt.toml | 73 | それならば\x%l機関士;#00ffc040;機関士%l;#;も\x%lレイルロオド;#00ffc040;レイルロオド%l;#;も、\n相当な数がいそうなものだが…… | \x%l機関士;#00ffc040;司機%l;#;和\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的數量應該相當多啊…… | Nếu vậy thì số lượng \x%l機関士;#00ffc040;người lái tàu%l;#; và \x%lレイルロオド;#00ffc040;Railord%l;#;,\nchắc hẳn cũng phải rất đông đảo mới đúng…… | Nếu vậy thì số lượng \x%l機関士;#00ffc040;lái tàu%l;#; và \x%lレイルロオド;#00ffc040;Railord%l;#;,\nchắc hẳn cũng phải rất đông đảo mới đúng…… | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 共通06_8620を探せ.txt.toml | 2027 | 「が、\x%l機関士;#00ffc040;機関士%l;#;云々も実は、\n\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致反対運動に繋げられるかもしれんのだ」 | 「可是\x%l機関士;#00ffc040;司機%l;#;這些事也許會有利於反對引進\x%lエアクラ;#00ffc040;空凝機%l;#;工廠運動」 | 「Nhưng mà, chuyện \x%l機関士;#00ffc040;người lái tàu%l;#; này nọ thực ra,\ncũng có thể liên quan đến phong trào phản đối thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; đấy.」 | 「Nhưng mà, chuyện \x%l機関士;#00ffc040;lái tàu%l;#; này nọ thực ra,\ncũng có thể liên quan đến phong trào phản đối thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; đấy.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 共通06_8620を探せ.txt.toml | 2112 | 「[ていおう,1]帝央\x%l機関区;#00ffc040;機関区%l;#;では、長いこと清美機関士お一人だけでした。\nもっとも、戦中には女性\x%l機関士;#00ffc040;機関士%l;#;の方が多くなりましたが」 | 「在帝都中央\x%l機関区;#00ffc040;機務段%l;#;，很長一段時間裡女性司機只有清美司機一人。不過在戰爭中女性\x%l機関士;#00ffc040;司機%l;#;倒是變得更多了」 | 「Ở \x%l機関区;#00ffc040;kho đầu máy%l;#; Teiou, trong một thời gian dài chỉ có một mình cô Kiyomi là người lái tàu thôi ạ.\nTuy nhiên, trong thời chiến thì số lượng nữ \x%l機関士;#00ffc040;người lái tàu%l;#; đã tăng lên rất nhiều.」 | 「Ở \x%l機関区;#00ffc040;kho đầu máy%l;#; Teiou, trong một thời gian dài chỉ có một mình cô Kiyomi là người lái tàu thôi ạ.\nTuy nhiên, trong thời chiến thì số lượng nữ \x%l機関士;#00ffc040;lái tàu%l;#; đã tăng lên rất nhiều.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 共通06_8620を探せ.txt.toml | 2129 | 「女性……\x%l機関士;#00ffc040;機関士%l;#;さんって、機関車の\x%l運転士;#00ffc040;運転士%l;#;さんよね。\n昔はそげな人おったと？」 | 「女性……\x%l機関士;#00ffc040;司機%l;#;是指機車的\x%l運転士;#00ffc040;駕駛員%l;#;吧。以前有這種人嗎？」 | 「Phụ nữ…… \x%l機関士;#00ffc040;Người lái tàu%l;#; là \x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; đầu máy xe lửa nhỉ.\nNgày xưa cũng có người như vậy sao?」 | 「Phụ nữ…… \x%l機関士;#00ffc040;Lái tàu%l;#; là \x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; đầu máy xe lửa nhỉ.\nNgày xưa cũng có người như vậy sao?」 | «\x%l機関士;#00ffc040;Người lái» → «\x%l機関士;#00ffc040;Lái» |
| 共通06_8620を探せ.txt.toml | 2257 | 「戦時徴用の\x%l機関士;#00ffc040;機関士%l;#;さん達は清美機関士をおっかながって。\nですからずっと、お風呂はわたくし達ふたりじめでした」 | 「戰時徵用的\x%l機関士;#00ffc040;司機%l;#;們都害怕清美司機。所以一直都是我們倆獨占整個澡堂」 | 「Các \x%l機関士;#00ffc040;người lái tàu%l;#; bị trưng dụng thời chiến rất sợ cô Kiyomi.\nThế nên bồn tắm lúc nào cũng chỉ có hai chúng em độc chiếm thôi ạ.」 | 「Các \x%l機関士;#00ffc040;lái tàu%l;#; bị trưng dụng thời chiến rất sợ cô Kiyomi.\nThế nên bồn tắm lúc nào cũng chỉ có hai chúng em độc chiếm thôi ạ.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 共通06_8620を探せ.txt.toml | 2422 | 「にぃにぃを\x%l機関士;#00ffc040;機関士%l;#;に！？　そんなん！\n家におってくれる時間が減って――じゃなくて！」 | 「讓阿哥當\x%l機関士;#00ffc040;司機%l;#;！？不要！那樣待在家裡的時間會減少的——不對！」 | 「Bắt anh hai làm \x%l機関士;#00ffc040;người lái tàu%l;#; á!? Sao có thể!\nThời gian anh ở nhà sẽ ít đi mất——à không phải!」 | 「Bắt anh hai làm \x%l機関士;#00ffc040;lái tàu%l;#; á!? Sao có thể!\nThời gian anh ở nhà sẽ ít đi mất——à không phải!」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 共通12_のぞみ.txt.toml | 2574 | 「それはいけない。\x%l機関士;#00ffc040;機関士%l;#;になるのでしたら、\nカメラに慣れておいたほうがいい」 | 「這可不行啊。要是你準備當\x%l機関士;#00ffc040;司機%l;#;，還是早點習慣拍照吧」 | 「Thế này không được rồi. Nếu cậu định trở thành \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#;,\nthì nên làm quen với máy ảnh từ sớm đi.」 | 「Thế này không được rồi. Nếu cậu định trở thành \x%l機関士;#00ffc040;lái tàu%l;#;,\nthì nên làm quen với máy ảnh từ sớm đi.」 | «\x%l機関士;#00ffc040;nhân» → «\x%l機関士;#00ffc040;lái»; «viên cơ vụ%l;#;,\nthì» → «tàu%l;#;,\nthì» |
| 共通12_のぞみ.txt.toml | 2911 | それが何故かを即時に理解出来る程度には、\nハチロクによる\x%l機関士;#00ffc040;機関士%l;#;教育も身についてきている。 | 八六對我的\x%l機関士;#00ffc040;司機%l;#;教育已見成效，我立刻就理解了他的意思。 | Ở mức độ có thể hiểu ngay lập tức lý do tại sao,\nsự giáo dục \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; của Hachiroku cũng đã ngấm vào người tôi. | Ở mức độ có thể hiểu ngay lập tức lý do tại sao,\nsự giáo dục \x%l機関士;#00ffc040;lái tàu%l;#; của Hachiroku cũng đã ngấm vào người tôi. | «\x%l機関士;#00ffc040;nhân» → «\x%l機関士;#00ffc040;lái»; «viên cơ vụ%l;#;» → «tàu%l;#;» |
| 共通15_回り始める動輪.txt.toml | 2029 | 「餅は餅屋、汽車は汽車屋です、双鉄様。\n双鉄様の\x%l機関士;#00ffc040;機関士%l;#;としての適正は、明快に示されています」 | 「常言道，術業有專攻，雙鐵少爺。您作為\x%l機関士;#00ffc040;司機%l;#;的天賦，大家都看在眼裡」 | 「Bánh giầy có thợ làm bánh giầy, tàu hỏa có thợ làm tàu hỏa, ngài Soutetsu.\nNăng lực của ngài Soutetsu với tư cách là một \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; đã được thể hiện rất rõ ràng.」 | 「Bánh giầy có thợ làm bánh giầy, tàu hỏa có thợ làm tàu hỏa, ngài Soutetsu.\nNăng lực của ngài Soutetsu với tư cách là một \x%l機関士;#00ffc040;lái tàu%l;#; đã được thể hiện rất rõ ràng.」 | «\x%l機関士;#00ffc040;nhân» → «\x%l機関士;#00ffc040;lái»; «viên cơ vụ%l;#;» → «tàu%l;#;» |
| 共通15_回り始める動輪.txt.toml | 2136 | 「ファンサービスも、\x%l機関士;#00ffc040;機関士%l;#;の大事なお仕事ですよ？\n双鉄様」 | 「服務觀眾，也是\x%l機関士;#00ffc040;司機%l;#;重要的工作哦，雙鐵少爺」 | 「Phục vụ người hâm mộ cũng là một công việc quan trọng của \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; đấy ạ?\nNgài Soutetsu.」 | 「Phục vụ người hâm mộ cũng là một công việc quan trọng của \x%l機関士;#00ffc040;lái tàu%l;#; đấy ạ?\nNgài Soutetsu.」 | «\x%l機関士;#00ffc040;nhân» → «\x%l機関士;#00ffc040;lái»; «viên cơ vụ%l;#;» → «tàu%l;#;» |
| 共通15_回り始める動輪.txt.toml | 2938 | \x%l機関士;#00ffc040;機関士%l;#;鞄を大きく開き、\n中から\x%l運転体;#00ffc040;運転体%l;#;のハチロクを取り出す。 | 我打開\x%l機関士;#00ffc040;司機%l;#;專用包，從中取出八六的\x%l運転体;#00ffc040;駕駛體%l;#;。 | Tôi mở rộng chiếc cặp \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#;,\nlấy Hachiroku \x%l運転体;#00ffc040;thân vận hành%l;#; từ bên trong ra. | Tôi mở rộng chiếc cặp \x%l機関士;#00ffc040;lái tàu%l;#;,\nlấy Hachiroku \x%l運転体;#00ffc040;thân vận hành%l;#; từ bên trong ra. | «\x%l機関士;#00ffc040;nhân» → «\x%l機関士;#00ffc040;lái»; «viên cơ vụ%l;#;,\nlấy» → «tàu%l;#;,\nlấy» |
| 共通15_回り始める動輪.txt.toml | 3161 | 今の僕は、駆け出しも駆け出し、\nほとんど素人の\x%l機関士;#00ffc040;機関士%l;#;だ。 | 現在的我，還是個徹頭徹尾的新手\x%l機関士;#00ffc040;司機%l;#;。 | Tôi bây giờ, chỉ mới là một người mới bắt đầu,\nmột \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; gần như nghiệp dư. | Tôi bây giờ, chỉ mới là một người mới bắt đầu,\nmột \x%l機関士;#00ffc040;lái tàu%l;#; gần như nghiệp dư. | «\x%l機関士;#00ffc040;nhân» → «\x%l機関士;#00ffc040;lái»; «viên cơ vụ%l;#;» → «tàu%l;#;» |
| 日々姫02_日々姫の日々.txt.toml | 2713 | 僕とて、どう甘く見ても\x%l機関士;#00ffc040;機関士%l;#;の見習いの卵レベルだ。\n指導などとはおこがましい。 | 我充其量只是個正在學習的實習\x%l機関士;#00ffc040;司機%l;#;，指導別人太自不量力了。 | Bản thân tôi, dù nhìn thế nào cũng chỉ là một \x%l機関士;#00ffc040;người lái tàu%l;#; tập sự.\nChỉ bảo người khác thì quá tự cao rồi. | Bản thân tôi, dù nhìn thế nào cũng chỉ là một \x%l機関士;#00ffc040;lái tàu%l;#; tập sự.\nChỉ bảo người khác thì quá tự cao rồi. | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 日々姫03_客車手配.txt.toml | 3604 | \x%l機関士;#00ffc040;機関士%l;#;として認められた今、\n僕はハチロクのオーナーであり、マスターだ。 | 現在我既然被正式承認為\x%l機関士;#00ffc040;司機%l;#;，那我就是八六的主人兼司機了。 | Bây giờ, khi đã được công nhận là một \x%l機関士;#00ffc040;thợ lái đầu máy%l;#;,\ntôi là chủ sở hữu và cũng là Master của Hachiroku. | Bây giờ, khi đã được công nhận là một \x%l機関士;#00ffc040;lái tàu%l;#;,\ntôi là chủ sở hữu và cũng là Master của Hachiroku. | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;,\ntôi» → «tàu%l;#;,\ntôi» |
| 日々姫06_日々姫の決断.txt.toml | 3259 | 意外と感じ、感じた瞬間、思い出す。\nそういえばハチロクの前\x%l機関士;#00ffc040;機関士%l;#;は、女性とのことだった。 | 在我感到意外的同時又忽然想起八六之前的\x%l機関士;#00ffc040;司機%l;#;是女性的事。 | Cảm thấy bất ngờ, và ngay khoảnh khắc đó, tôi chợt nhớ ra.\nNhắc mới nhớ, \x%l機関士;#00ffc040;người lái tàu%l;#; trước đây của Hachiroku là phụ nữ. | Cảm thấy bất ngờ, và ngay khoảnh khắc đó, tôi chợt nhớ ra.\nNhắc mới nhớ, \x%l機関士;#00ffc040;lái tàu%l;#; trước đây của Hachiroku là phụ nữ. | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 日々姫06_日々姫の決断.txt.toml | 3394 | あるいは件の女性\x%l機関士;#00ffc040;機関士%l;#;が、\nそうした噂に、辟易させられていたのかもしれん。 | 或許那個女\x%l機関士;#00ffc040;司機%l;#;曾經就被這種傳聞攪得束手無策。 | Hoặc cũng có thể \x%l機関士;#00ffc040;nữ lái tàu%l;#; đó,\nđã từng bị những tin đồn như vậy làm cho khốn đốn cũng nên. | Hoặc cũng có thể \x%l機関士;#00ffc040;lái tàu%l;#; đó,\nđã từng bị những tin đồn như vậy làm cho khốn đốn cũng nên. | «\x%l機関士;#00ffc040;nữ lái» → «\x%l機関士;#00ffc040;lái» |
| 日々姫08_開きかけのつぼみ.txt.toml | 2155 | 「端的に聞くが――\n\x%l8620;#00ffc040;8620%l;#;の\x%l機関士;#00ffc040;機関士%l;#;を僕と交代でやってはもらえないだろうか」 | 「我就直接問了——你能不能和我輪著當\x%l8620;#00ffc040;８６２０%l;#;的\x%l機関士;#00ffc040;司機%l;#;」 | 「Nói thẳng ra thì――\nEm có thể luân phiên làm \x%l機関士;#00ffc040;người lái tàu%l;#; \x%l8620;#00ffc040;8620%l;#; với anh được không?」 | 「Nói thẳng ra thì――\nEm có thể luân phiên làm \x%l機関士;#00ffc040;lái tàu%l;#; \x%l8620;#00ffc040;8620%l;#; với anh được không?」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 日々姫08_開きかけのつぼみ.txt.toml | 2299 | 「確かに、トップナンバー機であるわたくしの場合、\nマスターのみを\x%l機関士;#00ffc040;機関士%l;#;にしての乗務が、あるべき姿です」 | 「的確，作為首車，不應該讓主人以外的人來當\x%l機関士;#00ffc040;司機%l;#;」 | 「Đúng là với tư cách là đầu máy số 1 như em,\nviệc chỉ có Master làm \x%l機関士;#00ffc040;người lái tàu%l;#; mới là hình mẫu chuẩn mực ạ.」 | 「Đúng là với tư cách là đầu máy số 1 như em,\nviệc chỉ có Master làm \x%l機関士;#00ffc040;lái tàu%l;#; mới là hình mẫu chuẩn mực ạ.」 | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 日々姫08_開きかけのつぼみ.txt.toml | 2838 | 故、ポーレット\x%l機関士;#00ffc040;機関士%l;#;-僕が\x%l機関助士;#00ffc040;機関助士%l;#;という体制の方が、\nその逆よりもよほど楽に、よりよい結果を出せる筈だ。 | 所以就由波萊特當\x%l機関士;#00ffc040;司機%l;#;，我當\x%l機関助士;#00ffc040;司爐%l;#;，這樣可能反而會更加輕鬆，效果也會更好。 | Do đó, với thể chế Paulette làm \x%l機関士;#00ffc040;người lái tàu%l;#; - tôi làm \x%l機関助士;#00ffc040;phụ lái tàu%l;#;,\nchắc chắn sẽ dễ dàng và mang lại kết quả tốt hơn so với chiều ngược lại. | Do đó, với thể chế Paulette làm \x%l機関士;#00ffc040;lái tàu%l;#; - tôi làm \x%l機関助士;#00ffc040;phụ lái tàu%l;#;,\nchắc chắn sẽ dễ dàng và mang lại kết quả tốt hơn so với chiều ngược lại. | «\x%l機関士;#00ffc040;người lái» → «\x%l機関士;#00ffc040;lái» |
| 稀咲02_新事業案.txt.toml | 1378 | 「\x%l機関士;#00ffc040;機関士%l;#;側も異常なしです。\nポーレット様から出発合図が出れば――あっ」 | 「\x%l機関士;#00ffc040;司機%l;#;那邊也沒有異常。只要波萊特小姐發出出發信號——啊」 | 「Phía \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; cũng không có gì bất thường ạ.\nChỉ cần Thị trưởng Paulette phát tín hiệu xuất phát là——a.」 | 「Phía \x%l機関士;#00ffc040;lái tàu%l;#; cũng không có gì bất thường ạ.\nChỉ cần Thị trưởng Paulette phát tín hiệu xuất phát là——a.」 | «\x%l機関士;#00ffc040;nhân» → «\x%l機関士;#00ffc040;lái»; «viên cơ vụ%l;#;» → «tàu%l;#;» |
| 稀咲02_新事業案.txt.toml | 2017 | 「わ、私が\x%l機関士;#00ffc040;機関士%l;#;代理だなんて――」 | 「居、居然讓我當代理\x%l機関士;#00ffc040;司機%l;#;——」 | 「V, việc để em làm đại lý \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#;——」 | 「V, việc để em làm đại lý \x%l機関士;#00ffc040;lái tàu%l;#;——」 | «\x%l機関士;#00ffc040;nhân» → «\x%l機関士;#00ffc040;lái»; «viên cơ vụ%l;#;——」» → «tàu%l;#;——」» |
| 稀咲02_新事業案.txt.toml | 2260 | 「稀咲様が\x%l機関助士;#00ffc040;機関助士%l;#;見習い。双鉄様がその指導。\nとなれば、日々姫が\x%l機関士;#00ffc040;機関士%l;#;見習いで――」 | 「稀咲小姐擔任見習\x%l機関助士;#00ffc040;司爐%l;#;。雙鐵少爺進行指導。這樣一來，就只能讓日日姬擔任見習\x%l機関士;#00ffc040;司機%l;#;——」 | 「Cô Kisaki sẽ làm \x%l機関助士;#00ffc040;phụ lái tàu%l;#; tập sự. Ngài Soutetsu sẽ hướng dẫn.\nNếu vậy, Hibiki sẽ làm \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; tập sự——」 | 「Cô Kisaki sẽ làm \x%l機関助士;#00ffc040;phụ lái tàu%l;#; tập sự. Ngài Soutetsu sẽ hướng dẫn.\nNếu vậy, Hibiki sẽ làm \x%l機関士;#00ffc040;lái tàu%l;#; tập sự——」 | «\x%l機関士;#00ffc040;nhân» → «\x%l機関士;#00ffc040;lái»; «viên cơ vụ%l;#;» → «tàu%l;#;» |
| 稀咲02_新事業案.txt.toml | 2569 | が、数日程度の訓練で出来る\x%l機関士;#00ffc040;機関士%l;#;の仕事など、\n正真正銘、なにひとつない。 | 但是，僅僅經過幾天的訓練，是勝任不了任何\x%l機関士;#00ffc040;司機%l;#;的工作的。 | Tuy nhiên, công việc của \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; mà chỉ cần huấn luyện vài ngày là làm được thì,\nthực sự là chẳng có công việc nào cả. | Tuy nhiên, công việc của \x%l機関士;#00ffc040;lái tàu%l;#; mà chỉ cần huấn luyện vài ngày là làm được thì,\nthực sự là chẳng có công việc nào cả. | «\x%l機関士;#00ffc040;nhân» → «\x%l機関士;#00ffc040;lái»; «viên cơ vụ%l;#;» → «tàu%l;#;» |
| 稀咲02_新事業案.txt.toml | 2634 | \x%l機関士;#00ffc040;機関士%l;#;側で、日々姫が盛大にずっこける。\nそうされ、気付き。 | 在\x%l機関士;#00ffc040;司機%l;#;那邊，日日姬誇張地做了個無奈的動作。 | Ở phía ghế \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#;, Hibiki trượt chân ngã cái oạch.\nNhờ vậy tôi mới nhận ra. | Ở phía ghế \x%l機関士;#00ffc040;lái tàu%l;#;, Hibiki trượt chân ngã cái oạch.\nNhờ vậy tôi mới nhận ra. | «\x%l機関士;#00ffc040;nhân» → «\x%l機関士;#00ffc040;lái»; «viên cơ vụ%l;#;,» → «tàu%l;#;,» |
| ニイロク04_終端.txt.toml | 2411 | これほどの機関士とレイルロオドです。\n機転によって、シロのタブレットも回収されれば―― | 他們是那麼優秀的司機和鐵路人偶。如果隨機應變，能拿回四六的操作板—— | Là một \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; và Railord tuyệt vời đến thế cơ mà.\nNếu tùy cơ ứng biến, và thu hồi được cả \x%l操作板;#00ffc040;máy tính bảng%l;#; của Shiro thì—— | Là một \x%l機関士;#00ffc040;lái tàu%l;#; và Railord tuyệt vời đến thế cơ mà.\nNếu tùy cơ ứng biến, và thu hồi được cả \x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#; của Shiro thì—— | «\x%l機関士;#00ffc040;thợ» → «\x%l機関士;#00ffc040;lái»; «lái đầu máy%l;#;» → «tàu%l;#;»; «\x%l操作板;#00ffc040;máy» → «\x%l操作板;#00ffc040;Thẻ»; «tính» → «bảng»; «bảng%l;#;» → «(Tablet)%l;#;» |

## §4. Giữ nguyên / cờ

### Giữ nguyên (đã đọc JP, không sửa)

- **T8:** 日々姫03 2056 + 2678 ("Đài Maitetsu radio" / "Đài phát thanh Maitetsu Đường sắt Ohitoyo" — tên chương trình まいてつラジオ, dùng proper-name); 凪h2 1766 "hợp đồng Maitetsu" — SKIP, T74 OPEN; mọi dòng đã là "chủ tàu" (kể cả các dòng audit đã sửa ở 共通05, ハチロク02 3184/2376…); mọi dòng マニア/鉄道マニア mà JP không có まいてつ (vd. ハチロク04 3199, ハチロク16 2284, グランド03 2086/2077, れいな02 2546, ポーレット04 2515/1400, 日々姫03 3610, 仲国01 1385).
- **T9:** 4 dòng JP-市電 đã đúng (共通05 2404/2378, ハチロク02 1917/71).
- **T25:** 6/8 ứng viên có JP không chứa 従輪 ("chịu tải" là nghĩa chung, không phải term) — giữ.
- **T26:** 54/56 ứng viên đã là "bánh xe chủ động"/"Bánh xe chủ động" — giữ.
- **T27/T28:** plain "thẻ bảng" core không tag — lr追加_ひよこ 1421 (giữ); ruby "[タブレット・レベル,2]" — ハチロク15a 1436 (term khác, không có dạng đã chốt — giữ); "タブレットレベル" diễn giải "mức độ mở hoàn toàn" — ハチロク10 1539/2750/2831/2903/3530/3555 (giữ); **T28 iPad "máy tính bảng" — giữ 20 dòng:** ハチロク01 2160/2753/2428, ハチロク08 2991/2945, グランド03 2940/2953/2381/1450, 日々姫h6 3405, 真闇03 2723, グランド08 2250/2494, 仲国01 2504/2076/2489/2138, 仲国07 1540, 仲国08 2593/1652. CG グランド03_タブレット1.png là tên file ảnh, không phải dòng CSV3 — chỉ làm ngữ cảnh.
- **T50:** SFX "Ryu" (りゅ/りゅっ) giữ 3 dòng; "Kuma" (クマ焼酎 / クマ川) là term khác — giữ (xem T51 cho Kumagin/Kumamoto).
- **T51:** "Kumagin" đúng cho JP 隈銀 — giữ 20 dòng; "Kuma" (shochu Kuma / sông Kuma) — giữ.
- **T52:** 53 dòng đã là "Đế đô" — giữ.
- **T53:** 134 dòng đã là "buồng lái" + 仲国07 1726 (full-width space) — giữ.
- **G1:** 71 dòng đã đúng ("đoàn tàu" 64 + "Đoàn tàu" 7); 真闇02 2319 giữ theo list; 2 dòng 列車防護 giữ (xem §2).
- **G2:** 146 dòng đã đúng ("lái tàu"/"Lái tàu"); 共通04 2651 "Master" giữ (xem §2); gloss 運転士 "nhân viên cơ vụ" giữ ở 3 dòng (1638/2108/2129); gloss 機関助士 giữ.

### Cờ (cần parent / batch khác xử lý)

- **CỜ U5-1 (G8 — Common 08 ×4):** 4 dòng Common 08 (1480/1929/1991/2836) đợt này về "Thẻ bảng (Tablet)". Nếu Hieu muốn "thẻ bảng" trần, lật lại 4 dòng này (xem §2 T27).
- **CỜ U5-2 (tag %l thiếu dấu `;` đóng — có từ CSV3, thuộc tag sweep đã park S1–S5/B19):** 12 dòng trong đợt này có tag đóng dị dạng `%l;#` (thiếu `;` cuối) — gloss đã sửa, phần đóng tag GIỮ NGUYÊN như cũ, không thêm `;` (ngoài phạm vi mục; sweep sẽ quyết sau khi có check in-game B19). Các dòng: ポーレット11_記憶と記録 998/1349/1528/1551/1660/1724/1754/2006/2085 (tag %lタブレット), ポーレット10_見えない傷 959/1241 (tag %l機関士), ポーレット10_見えない傷 1461 (tag %l列車). Bằng chứng có từ trước: CSV3 VN của P11 998 đã là `…Thẻ bảng%l;#……` (thiếu `;`), audit chỉ đổi gloss, không tạo ra lỗi này.
- **CỜ U5-3 (ニイロク04 — term tag 操作板 ≠ JP タブレット):** 10 dòng (1918/2011/2054/2061/2151/2152/2153/2411/2624/2673) — gloss đã sửa, term tag giữ 操作板. Chuyển cho U15/G12: đổi term tag sang タブレット hay giữ 操作板 (cần check in-game xem tag nào game hiển thị).
- **CỜ U5-4 (P04 — audit review sai + tag thừa):** audit review P04 đọc sai 2076/2642 (xem §2); ngoài ra audit đã thêm %l tag ở 7 dòng JP không có tag (1780/1811/2028/2050/2076/2698/2816) — thuộc G12, không đụng đợt này.
- **CỜ U5-5 (T5 chưa giao):** 真闇h3 3299 — "Đại học Hoàng gia" (JP 帝大) để nguyên; T5 (帝大 → ?) chưa thuộc batch nào.
- **CỜ U5-6 (list sai):** (a) G8 ghi "gloss タブレット 'thẻ bảng'→'máy tính bảng' ×5 trong ハチロク10_炙り出し" — KHÔNG TỒN TẠI: TOML-2 ハチロク10_炙り出し có 0 タブレット và 0 操作板; các file audit-hachiroku10-aburidashi cũng không nhắc Tablet. (b) T50 list ghi 5 dòng "ông Ryu" ở 日々姫03 — thực ra ở ハチロク08_教導 (3380/3167/3168/3171/2210), đã đúng "Nagare". (c) T51 list dẫn "仲国02 2434" — key 2434 không tồn tại trong 仲国02_北琴の鉄道 ở CSV3.
- **CỜ U5-7 (trùng batch đang RUNNING — 6 dòng, cần gộp giá trị kết hợp, xem mẫu U2c/U4 3719):** **ĐÃ GHÉP bởi coordinator 22/11: JSON + REVIEW §3 + khối TOML đã sửa đồng bộ (old_vn = fix batch đã gộp, fix = giá trị kết hợp); 4/6 giá trị kết hợp khớp tuyệt đối với cờ này, 2/6 (2326, 2814) khớp trừ dấu `;` đóng tag mà cờ ghi thiếu (artifact của cờ — JSON/TOML là chuẩn).** cả 6 dòng đều có old_vn giống nhau ở 2 batch (cùng current value) và fix của batch kia GIỮ NGUYÊN chuỗi của đợt này — nhưng rebuild áp fix-list theo thứ tự gộp, batch gộp sau sẽ ghi đè và làm mất đổi của batch gộp trước nếu không gộp giá trị. Giá trị kết hợp (old_vn + cả 2 đổi) cho từng dòng (dòng thứ 7 — ハチロク15a 2031 trùng U9 — đã chuyển sang U5-8 vì U9 đã gộp 22/11 ~11:45 và fix đợt này đã là giá trị kết hợp):
  - ハチロク11_御一夜鉄道小畑線 2251 (U5 T27 + U3 T10): `「Ngài Công chúa Tàu điện đã nói—— \n'Việc tinh luyện lại Lõi Lord từ \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;'」`
  - ハチロク04_煙には煙を 2464 (U5 G1 + U4 T7): `「Lúc \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ quay về, số người sử dụng thuyền xuôi dòng từ bến tàu Yunoi\nđến Ohitoyo cũng đang tăng lên đều đặn mà.」`
  - ハチロク13_夜の嵐 2326 (U5 T27 + U4 T11): `Thấy vậy, Hachiroku đổi \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#,\ntrở lại \x%l運転体;#00ffc040;thân vận hành%l;#; và cất giọng nghiêm túc.`
  - ハチロク13_夜の嵐 2328 (U5 T27 + U4 T11): `Thấy vậy, Hachiroku\ntháo \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; ra và chuyển sang \x%l運転体;#00ffc040;thân vận hành%l;#;.`
  - ハチロク13_夜の嵐 2336 (U5 T27 + U4 T12): `Hachiroku lập tức chuyển \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; về lại \x%l整備体;#00ffc040;thân bảo trì%l;#;.\nVậy thì tôi chỉ còn cách cầm xẻng lên lại thôi.`
  - ポーレット03_廃炭鉱 2814 (U5 G2 + U4 T41): `Trong \x%l運転台;#00ffc040;buồng lái%l;#; của \x%lキハ07;#00ffc040;KiHa 07%l;#; mà em còn chưa quen, Hibiki lúc này không phải \x%l機関助士;#00ffc040;phụ lái%l;#; cũng không phải \x%l機関士;#00ffc040;Lái tàu%l;#;, mà đang đóng vai trò \x%l運転士;#00ffc040;người lái%l;#. `
  - ~~ハチロク15a_痛みとの決別 2031 (U5 G2 + U9 P15) — ĐÃ XỬ LÝ, xem U5-8 (U9 đã gộp; fix đợt này = giá trị kết hợp `Dù tao… + gloss lái tàu`).~~
- **CỜ U5-8 (trùng batch ĐÃ GỘP — đã xử lý đúng):** (a) グランド06_稀咲 1923 trùng U2b (đã gộp 22/11 ~11:40): old_vn đợt này = fix U2b ("Đường sắt Ohitoyo" + "Teito"), fix đợt này chỉ đổi "Teito"→"Đế đô" trên đó. (b) ハチロク15a_痛みとの決別 2031 trùng U9 (đã gộp 22/11 ~11:45): old_vn đợt này = fix U9 ("Dù tao…" + gloss "người lái tàu"), fix đợt này = giá trị kết hợp "Dù tao… + gloss lái tàu" — rebuild theo thứ tự gộp sẽ ra đúng, không hồi quy đổi của U9. Không còn dòng nào khác trùng batch đã gộp (kiểm tra bằng máy với 9 file unif-đã-gộp: 7 dòng unif-src đều là old_vn hợp lệ).

## §5. Lượt soát 2 (second pass — đọc lại toàn bộ 336 fix với JP)

- **Tổng số fix:** 336. **Tái kiểm chứng (đọc lại từng fix với JP/TW):** 336/336. **Bỏ:** 0. **Sửa:** 0.
- **Kiểm chứng cơ học độc lập (code path riêng, không dùng lại code lúc liệt kê):** 336/336 mục có key dạng string, file basename đầy đủ `.txt.toml`, jp/tw khớp CSV3 tuyệt đối (good-set), old_vn = current value đúng quy ước rebuild (unification-đã-gộp > moan > audit > CSV3), fix khác old_vn; JP chứa thuật ngữ gốc 336/336 (T27: タブレット hoặc たぶれっと 2076; T8: まいてつ); 0 dòng chạm token gasp Ư hay token "Kh" đứng riêng. **Kiểm theo phạm vi tag (tag-scoped, thay cho placeholder-diff toàn chuỗi — bản toàn chuỗi báo sai vì chuỗi cũ xuất hiện ở chỗ KHÔNG được sửa, vd. "tàu" trong "bến tàu", "người lái tàu" trong gloss 運転士 giữ nguyên, "chủ tàu" là chuỗi con của "các chủ tàu"):** mọi tag %l giữ nguyên term + mã màu; mọi gloss đổi đều nằm trong tập triple đã chốt (term, gloss cũ, gloss mới) — 0 lỗi; mask toàn bộ tag rồi diff phần text trần: 36 dòng có diff, tất cả đều khớp đúng đổi đã chốt bằng tay (T52 Teito/Đế Đô/thủ đô→Đế đô + "Đ"→"đ" giữa câu 10 dòng + "trên"→"ở" 2 dòng; T8 Maitetsu/maitetsu/giới đường sắt/ông trùm đường sắt→chủ tàu/các chủ tàu/chủ tàu (lớn) 7 dòng; T27-plain 5 dòng; T26 "chủ động" 1 dòng; T25+T26 "xe" 1 dòng; T51 Kumagin→Kumamoto + "Ngân hàng" 2 dòng); 0 lần xuất hiện dạng cũ còn sót trong fix ở đúng vị trí đã sửa (G1: 0 gloss cũ; G2: 0 gloss cũ; T27: 0 gloss khác "Thẻ bảng (Tablet)").
- **Lỗi bắt được Ở BƯỚC KIỂM CHỨNG TRƯỚC KHI SOÁT 2 (đã sửa, không tính vào lượt soát):** 6 dòng T27-gloss có 2 tag trong một dòng ban đầu chỉ được sửa tag đầu (code dùng re.search + replace lần 1): ニイロク04 1918, ハチロク07 1662/2444/3121, ハチロク10 2190, ハチロク16 2307. Đã sửa code sang thay TẤT CẢ các tag sai trong dòng và kiểm lại: 6/6 dòng nay cả 2 tag đều là "Thẻ bảng (Tablet)". Số dòng không đổi (85 dòng gloss), chỉ giá trị fix của 6 dòng này thay đổi.
- **Kiểm chứng TOML:** 82 khối TOML (một khối mỗi file), 336 khóa, parse OK bằng tomllib, giá trị parse được khớp JSON 336/336. Trong khối, `\\n` = ký tự `\n` thật trong giá trị (quy ước TOML block của dự án); `\\x` = ký tự `\x` thật; dấu `"` trong giá trị được escape thành `\"` (kiểm bằng máy: 0 khối lỗi parse).
- **Đọc lại bằng mắt:** toàn bộ 336 dòng JP/TW/old_vn/fix đã đọc ở lượt 1 (§2 từng mục + bảng §3); lượt 2 đọc lại từng fix value trong bảng §3 theo đúng chuỗi đã chốt của từng mục (T8 "chủ tàu", T25/T26 "bánh xe …", T27 "Thẻ bảng (Tablet)", T51 "Ngân hàng Kumamoto", T52 "Đế đô", G1 "đoàn tàu", G2 "lái tàu") và đếm lại: 336/336 khớp, 0 dòng cần bỏ, 0 dòng cần sửa lại.

**Ghi chú điều phối (coordinator, 22/11 ~12:00 — 6 dòng ghép U5-7):** 6 dòng trên trùng batch đã gộp (U3 T10, U4 T7/T11/T12/T41) ở token khác nhau — đã GHÉP theo quy tắc composition (U4-3719): old_vn := fix batch đã gộp, fix := fix đã gộp + thay đổi của đợt này. Mỗi giá trị ghép được kiểm chứng bằng 2 cách độc lập: (1) thay thế token đơn trên fix đã gộp (token xuất hiện đúng 1 lần); (2) đối chiếu với giá trị kết hợp worker ghi trong cờ U5-7 — 4/6 khớp tuyệt đối, 2/6 (2326, 2814) khớp trừ dấu `;` đóng tag bị cờ ghi thiếu. Lượt soát 2 của worker (336/336) đọc fix CŨ của 6 dòng này; 6 giá trị ghép đã được coordinator kiểm lại từng giá trị với JP (token của đợt này + token của batch đã gộp đều đã qua soát 2 ở batch gốc). Nguồn old_vn sau gộp: CSV3 207, audit 116, unification-đã-gộp 12, moan 1.

## §6. Khối TOML (82 file, 336 khóa — áp vào file TOML khi rebuild; `\\n` trong khối = ký tự \n thật trong giá trị; `\\x` = ký tự \x thật; `\"` = `"` thật)

### 00_Common/共通05_ようやく石炭.txt.toml

```toml
1826 = "「Rốt cuộc, 『\\x%lまいてつ;#00ffc040;chủ tàu%l;#;』 là gì vậy?」"
2132 = "「Không. Hiện tại, tôi chỉ là một tay mơ thôi.\\nĐến mức còn chẳng biết 『\\x%lまいてつ;#00ffc040;chủ tàu%l;#;』 là gì nữa cơ.」"
2155 = "「Nói tóm lại “\\x%lまいてつ;#00ffc040;chủ tàu%l;#;” là những người sở hữu cá nhân và vận hành \\x%l列車;#00ffc040;đoàn tàu%l;#;\\n——Tức là những fan……những người hâm mộ đường sắt đó phải không?」"
2252 = "「Nếu làm thế này mà có thể trở thành \\x%l機関士;#00ffc040;lái tàu%l;#;.\\nThì tất nhiên, tôi sẽ làm.」"
2432 = "「Tôi rất mong ngài Soutetsu sẽ trở thành \\x%l機関士;#00ffc040;lái tàu%l;#;——\\nTrở thành Master của tôi.」"
2472 = "「Chắc là người của hội \\x%lまいてつ;#00ffc040;chủ tàu%l;#; nhỉ. Đi cùng với \\x%lレイルロオド;#00ffc040;Railord%l;#; mà.」"
2501 = "「Đúng vậy. 『Đường sắt điện Hiroshima Mouri』 của công chúa nhà Mouri,\\nchính là điểm xuất phát của hệ thống tương trợ mang tên \\x%lまいてつ;#00ffc040;chủ tàu%l;#;.」"
2505 = "「Vâng. Bởi vì tôi vẫn chưa có Master.\\nTôi vẫn chưa có \\x%l機関士;#00ffc040;lái tàu%l;#;.」"
2727 = "「Nếu vậy, Hachiroku. Tôi sẽ trở thành \\x%l機関士;#00ffc040;lái tàu%l;#; của em.」"
2969 = "A, nhưng mà, có từ gọi là \\x%l編成;#00ffc040;đoàn tàu%l;#; một toa không nhỉ?\\nNếu vậy thì dù chỉ có một toa, nó vẫn là một \\x%l編成;#00ffc040;đoàn tàu%l;#;, một \\x%l列車;#00ffc040;đoàn tàu%l;#;——có lẽ là có."
3140 = "Vào thời kỳ hoàng kim của đường sắt,\\ncác \\x%lレイルロオド;#00ffc040;Railord%l;#; cũng từng hướng dẫn cho các ứng viên \\x%l機関士;#00ffc040;lái tàu%l;#; sao?"
3296 = "Tetsu nghĩa là người cuồng đường sắt. Và,\\nnhững Tetsu sở hữu “My đường sắt” chính là——“\\x%lまいてつ;#00ffc040;chủ tàu%l;#;” sao."
```

### 00_Common/共通08_傷跡.txt.toml

```toml
1480 = "「\\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;……là linh hồn của em sao?」"
1929 = "「Em sẽ đổi \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;.\\nNgài đừng ngạc nhiên nhé?」"
1991 = "「Nếu so sánh với cơ thể con người,\\nthì em nghĩ \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; giống với bộ não hơn ạ.」"
2836 = "（Đó là cái gọi là \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; sao?\\nHachiroku có nói là đổi, nhưng mà……）"
```

### 00_Common/共通09_さきだつもの.txt.toml

```toml
105 = "\\x%l列車;#00ffc040;Đoàn tàu%l;#;——đang tăng tốc sao!?"
106 = "\\x%l列車;#00ffc040;Đoàn tàu%l;#; lắc mạnh sang một bên, Michiko bám chặt lấy tôi.\\nMẹ cũng ôm chầm lấy bố."
2488 = "「Nghe nói ngày xưa có rất nhiều mèo trạm trưởng đấy.\\nỞ các ga trung tâm của \\x%l列車;#00ffc040;đoàn tàu%l;#; du lịch chẳng hạn.」"
2530 = "「\\x%l列車;#00ffc040;Đoàn tàu%l;#; này, do \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; kéo đúng không?\\nNên nếu lên phía trước xem thử.」"
2540 = "「Ừ. Đi thêm một lát nữa, \\x%l列車;#00ffc040;đoàn tàu%l;#; này\\nsẽ đi qua một cây cầu sắt tên là cầu Fujikawa.」"
2669 = "「Nghe nói con cả nhà Migita,\\nđã lên Đế đô rồi cơ mà.」"
2726 = "「Đó là còn chưa tính đến chuyện \\x%l客車;#00ffc040;toa hành khách%l;#; hay chi phí cố định đấy ạ.\\nDù là \\x%l列車;#00ffc040;đoàn tàu%l;#; du lịch nên có thể bán vé ghế chỉ định đi chăng nữa thì……」"
2998 = "Quá bất ngờ nên tôi không kịp phản ứng,\\ncứ thế bị chấn động của \\x%l列車;#00ffc040;đoàn tàu%l;#; hất văng đi——"
3551 = "Không hề sợ hãi trước \\x%l列車;#00ffc040;đoàn tàu%l;#; đang rung lắc dữ dội và tiếp tục tăng tốc,\\nMichiko nắm chặt tay tôi, mỉm cười đứng dậy."
```

### 00_Common/共通10_クマ川くだりで見る景色.txt.toml

```toml
3376 = "Nếu đổi \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; thì size trẻ em cũng sẽ thành to thôi,\\nnhưng trong trường hợp đó thì xử lý áo phao thế nào đây――ủa."
```

### 00_Common/共通12_のぞみ.txt.toml

```toml
2340 = "「Là \\x%l列車;#00ffc040;đoàn tàu%l;#; đấy. Xe của ngài thị trưởng đã quay về rồi.」"
2393 = "「Vào lúc khai trương tuyến mới, hay ngược lại là khi \\x%l列車;#00ffc040;đoàn tàu%l;#; bị ngừng hoạt động,\\nsân ga sẽ chật kín những người đam——những người hâm mộ đường sắt ạ.」"
2574 = "「Thế này không được rồi. Nếu cậu định trở thành \\x%l機関士;#00ffc040;lái tàu%l;#;,\\nthì nên làm quen với máy ảnh từ sớm đi.」"
2911 = "Ở mức độ có thể hiểu ngay lập tức lý do tại sao,\\nsự giáo dục \\x%l機関士;#00ffc040;lái tàu%l;#; của Hachiroku cũng đã ngấm vào người tôi."
3391 = "Nếu có thể đưa \\x%l8620;#00ffc040;8620%l;#; đến được Yunoi,\\nthì có lẽ——Michiko cũng có thể bước xuống từ chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; đó."
3473 = "Tôi cũng đã học điều đó. Một lực quán tính cực lớn sẽ tác động lên \\x%l列車;#00ffc040;đoàn tàu%l;#;.\\nDù còn tùy thuộc vào trọng lượng \\x%l列車;#00ffc040;đoàn tàu%l;#;, tốc độ, tình trạng đường ray, v.v.——"
```

### 00_Common/共通13_勾配図.txt.toml

```toml
1542 = "「Nếu \\x%l共感;#00ffc040;cộng cảm%l;#; không kết nối được, thì tức là Reina đang ngủ gật!\\nNếu vậy thì không còn cách nào khác ngoài việc dùng cách khác để dừng \\x%l列車;#00ffc040;đoàn tàu%l;#; lại!!」"
1938 = "「Hachiroku! Cách để dừng \\x%l列車;#00ffc040;đoàn tàu%l;#; lại!」"
2419 = "「Hãy cởi áo sơ mi ra, vẫy thật mạnh để ra hiệu cho \\x%l列車;#00ffc040;đoàn tàu%l;#;!」"
```

### 00_Common/共通14_負債.txt.toml

```toml
1759 = "「\\x%l列車;#00ffc040;Đoàn tàu%l;#; di chuyển theo hướng mũi tên,\\ntrước tiên sẽ đi hết cạnh đáy của hình tam giác △.」"
```

### 00_Common/共通15_回り始める動輪.txt.toml

```toml
2029 = "「Bánh giầy có thợ làm bánh giầy, tàu hỏa có thợ làm tàu hỏa, ngài Soutetsu.\\nNăng lực của ngài Soutetsu với tư cách là một \\x%l機関士;#00ffc040;lái tàu%l;#; đã được thể hiện rất rõ ràng.」"
2126 = "「Đúng vậy, anh Soutetsu.\\n\\x%lトレインマーク;#00ffc040;Biểu trưng tàu%l;#; gắn ở đầu \\x%l列車;#00ffc040;đoàn tàu%l;#; được gọi là \\x%lヘッドマーク;#00ffc040;biểu trưng đầu tàu%l;#;.」"
2136 = "「Phục vụ người hâm mộ cũng là một công việc quan trọng của \\x%l機関士;#00ffc040;lái tàu%l;#; đấy ạ?\\nNgài Soutetsu.」"
2619 = "Cạch, \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; được hoán đổi.\\nChớp chớp, đôi mắt của Hachiroku \\x%l運転体;#00ffc040;thân vận hành%l;#; mở ra."
2938 = "Tôi mở rộng chiếc cặp \\x%l機関士;#00ffc040;lái tàu%l;#;,\\nlấy Hachiroku \\x%l運転体;#00ffc040;thân vận hành%l;#; từ bên trong ra."
3161 = "Tôi bây giờ, chỉ mới là một người mới bắt đầu,\\nmột \\x%l機関士;#00ffc040;lái tàu%l;#; gần như nghiệp dư."
```

### 01_Hachiroku/lr_ハチロクh2_新しい服。新しい旅.txt.toml

```toml
1440 = "「Fa! Chết mất, Tablet, kỳ lạ hết rồi——\\nTrắng xóa mất, ưm! Chớp nháy, liên tục」"
```

### 01_Hachiroku/グランドリライト10_ハチロク.txt.toml

```toml
1119 = "……Tiến sĩ Trevithick quả thực là một thiên tài thực sự.\\nBởi vì \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;, không gì khác chính là một thiết bị an toàn."
1582 = "「Tôi cũng rất ngạc nhiên trước bản báo cáo hàng ngày này. Một \\x%l機関士;#00ffc040;lái tàu%l;#; có thể quan sát sự thay đổi một cách ngắn gọn và chi tiết đến mức này quả là hiếm có」"
1776 = "「Tôi cũng nghĩ \\x%l機関士;#00ffc040;lái tàu%l;#; Munakata là một trong những người đáng để tôn trọng và học hỏi」"
1777 = "「\\x%l機関士;#00ffc040;Lái tàu%l;#; Munakata đối xử với Olivy như một món đồ.\\nVạch ra ranh giới, không cho phép bước qua——nhưng lại vô cùng trân trọng」"
1898 = "「Thương mại hóa việc chế tạo \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; mới và \\x%lレイルロオド;#00ffc040;Railord%l;#; mới.\\nKhông chỉ dừng lại ở lĩnh vực đường sắt, mà như những đối tác mới của nhân loại」"
1907 = "「Thông báo rộng rãi theo hướng đó, kêu gọi vốn,\\nđẩy mạnh nghiên cứu \\x%lレイルロオド;#00ffc040;Railord%l;#; và tái phát triển \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;」"
1941 = "「Đúng vậy. Aircra Navi thế hệ cổ nhất cũng bao hàm \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;.\\nChính điều đó, cũng có thể gọi là hậu duệ \\x%lレイルロオド;#00ffc040;Railord%l;#; thuần túy」"
1982 = "「Phương pháp kéo dài tuổi thọ của \\x%lレイルロオド;#00ffc040;Railord%l;#; có khả năng mang lại hiệu quả tức thì.\\nVà cả việc sao chép \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; hiện có nữa」"
1993 = "「Tôi cảm thấy, quả đúng là như vậy.\\nChỉ nhìn vào ngày hôm nay thôi, \\x%l機関士;#00ffc040;lái tàu%l;#; Munakata cũng đã triệt để như vậy」"
2938 = "Nếu loại bỏ nó và thay thế lại bằng trí tuệ nhân tạo dạng \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;,\\nthì những ảnh hưởng xấu mà xã hội phải gánh chịu cũng sẽ ở mức tối thiểu."
```

### 01_Hachiroku/ハチロク01_こんにちわ赤ちゃん.txt.toml

```toml
2816 = "「Gần như là chính xác. Không chỉ vậy, các chủ tàu ở khắp nơi,\\ncũng đang lần lượt được đưa vào dự án của các công ty.」"
```

### 01_Hachiroku/ハチロク01_双鉄の目・ハチロクの目.txt.toml

```toml
1361 = "……Các \\x%lまいてつ;#00ffc040;chủ tàu%l;#; sẽ không từ bỏ phương tiện cần thiết cho mình.\\nVà \\x%l客車;#00ffc040;toa hành khách%l;#; thì, đối tượng mong muốn sở hữu nó còn hạn chế hơn cả toa xe động lực."
1394 = "「——Mặc dù cũng có trường hợp các \\x%lまいてつ;#00ffc040;chủ tàu%l;#; đã nghỉ hưu nhượng lại,\\nnhưng những trường hợp đó, thường là đi kèm cả toa xe động lực theo bộ……」"
1780 = "「A, \\x%l列車;#00ffc040;đoàn tàu%l;#; mà chụp góc này thì lên hình đẹp đến mức này luôn á.\\nHọc hỏi được nhiều rồi đây.」"
1808 = "「Ừm. Sau một đêm suy nghĩ kỹ càng,\\ntôi muốn chuyên tâm làm \\x%l機関士;#00ffc040;lái tàu%l;#;.」"
2020 = "「Đúng vậy. \\x%l機関士;#00ffc040;Lái tàu%l;#; của tuyến đường sắt được sử dụng hàng ngày,\\nthay vì là một con người, thì giống như một cỗ máy, hay một bối cảnh hơn.」"
2041 = "「Chắc những người bạn \\x%lまいてつ;#00ffc040;chủ tàu%l;#; của Paulette vẫn xem đấy.\\nNếu vậy thì, nó vẫn phù hợp với mục đích ban đầu, nhưng——」"
2224 = "「Ngoài việc chờ các \\x%lまいてつ;#00ffc040;chủ tàu%l;#; nghỉ hưu ra,\\nthì hoàn toàn không còn cách nào khác để có được \\x%l客車;#00ffc040;toa hành khách%l;#; sao ạ?」"
2475 = "\\x%lまいてつ;#00ffc040;Chủ tàu%l;#;, dù có thực dụng đến mức nào đi chăng nữa\\nnhưng xét cho cùng, nếu đó là một thế giới mang đậm màu sắc sở thích thì……"
```

### 01_Hachiroku/ハチロク02_8620運転台通信.txt.toml

```toml
1902 = "「Upupu. Gì đây gì đây, đen thui thùi lùi luôn.\\nNgươi chính là \\x%l機関士;#00ffc040;lái tàu%l;#;——Migita Soutetsu nhỉ.」"
2034 = "「Vậy thì, hãy đến chơi như một chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; sự kiện chỉ có một lần duy nhất——\\nHãy coi ý ta là như vậy đi.」"
2645 = "Những lời nói làm lay động ký ức vốn đã in sâu trong tôi.\\n……Sự háo hức khi cùng Michiko đi \\x%l列車;#00ffc040;đoàn tàu%l;#; hồi còn nhỏ."
```

### 01_Hachiroku/ハチロク02_ハートブレイク・レイルロオド.txt.toml

```toml
75 = "\\x%l機関士;#00ffc040;Lái tàu%l;#; cứ thế đi thẳng\\nvề phía Paulette."
2085 = "「Hôm nay cũng chúc ngài một ngày bình an, \\x%l機関士;#00ffc040;lái tàu%l;#; Migita.」"
2166 = "「Dạ? ——A, vâng. Cháu hiểu rồi. Anh Soutetsu——\\n\\x%l機関士;#00ffc040;Lái tàu%l;#; Migita. Bên đó, nhờ anh được không?」"
2376 = "「Trưởng phòng Vận tải Đường sắt Ohitoyo, \\x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;.\\nKiêm chủ tàu 8620, \\x%l機関士;#00ffc040;lái tàu%l;#; hơi nước, Migita Soutetsu.」"
3077 = "\\x%l機関士;#00ffc040;Lái tàu%l;#; Munakata được Paulette dẫn vào Rail Shop,\\nvà khuất dạng mà không thèm ngoảnh lại nhìn."
3147 = "Có lẽ, em ấy đang tìm kiếm hình bóng của \\x%l機関士;#00ffc040;lái tàu%l;#; Munakata——"
3449 = "（Nói cách khác, dù có \\x%l補機;#00ffc040;đầu máy phụ%l;#; đi chăng nữa, nhưng có thể vượt qua Yatake với tình trạng đó,\\nthì \\x%l機関士;#00ffc040;lái tàu%l;#; Munakata và Olivy——chắc hẳn phải có tay nghề rất đáng nể.）"
```

### 01_Hachiroku/ハチロク03_冥国式レイルロオド.txt.toml

```toml
2107 = "「Gọi Migita thì sẽ nhầm với Hibiki mất,\\nnên ở những nơi công cộng, cứ gọi anh là \\x%l機関士;#00ffc040;lái tàu%l;#; Soutetsu nhé.」"
2290 = "「Cô ấy lớn lên ở Đế đô mà.……Chắc hẳn chưa từng có kinh nghiệm như vậy.\\nHay là cô ấy đã được huấn luyện ở đâu đó rồi nhỉ.」"
2420 = "「Đã rõ! \\x%l機関士;#00ffc040;Lái tàu%l;#; Hibiki!!」"
2663 = "「Vậy, em nên gọi ngài Soutetsu là gì đây?\\n\\x%l機関士;#00ffc040;Lái tàu%l;#; Migita? Anh Soutetsu?」"
2679 = "「\\x%l機関士;#00ffc040;Lái tàu%l;#; Soutetsu. Vậy, Hibiki là \\x%l機関士;#00ffc040;lái tàu%l;#; Hibiki hả?」"
2709 = "「OK! Vậy, gọi là Soutetsu và Hibiki nha!\\nKhi làm nhiệm vụ thì là \\x%l機関士;#00ffc040;lái tàu%l;#; Soutetsu và \\x%l機関士;#00ffc040;lái tàu%l;#; Hibiki!」"
3108 = "Nagi cũng muốn trở thành \\x%l機関士;#00ffc040;lái tàu%l;#; của Đầu máy số 9,\\nnhưng nếu sự ăn ý này được phát huy trong công việc, thì Hibiki có thể sẽ chiếm ưu thế hơn."
```

### 01_Hachiroku/ハチロク03_客車試験.txt.toml

```toml
1369 = "「\\x%l客車;#00ffc040;Toa hành khách%l;#;.\\n……\\x%l列車;#00ffc040;Đoàn tàu%l;#; à.」"
1882 = "「Ừm, mát thật. Đặc quyền của việc bao trọn \\x%l列車;#00ffc040;đoàn tàu%l;#; nhỉ.」"
2682 = "Tôi không kìm được mà lấy lại chiếc máy ảnh vừa cất đi.\\n\\x%l列車;#00ffc040;Đoàn tàu%l;#;——tôi thực sự cảm thấy cái tên này thật chí lý."
2732 = "Phải xếp thành hàng, kết nối với nhau, thì mới thành \"\\x%l列車;#00ffc040;Đoàn tàu%l;#;\"."
```

### 01_Hachiroku/ハチロク04_小畑越え.txt.toml

```toml
3226 = "Ghế dài dọc theo xe gợi nhớ đến Đế đô nên tôi cũng không ghét.\\nNhưng đi từ Ohitoyo qua đèo Okoba đến Hayato——"
```

### 01_Hachiroku/ハチロク04_煙には煙を.txt.toml

```toml
1914 = "「Dù sao buổi tối cũng không có thuyền xuôi dòng.\\nBan đêm, em ít khi đi \\x%l列車;#00ffc040;đoàn tàu%l;#; nên――cũng thú vị lắm ạ.」"
1922 = "「Bởi vì nếu đã biết trước đây là \\x%l列車;#00ffc040;đoàn tàu%l;#; để nướng thịt,\\nanh nghĩ hành khách sẽ phần nào chuẩn bị tinh thần cho việc bị ám khói.」"
2062 = "「Nếu gọi là \\x%l列車;#00ffc040;Đoàn tàu%l;#; Thịt nướng……thì việc phát tạp dề――\\nđể quần áo không bị bẩn cũng không có gì lạ đâu ạ.」"
2182 = "「Cũng đúng ha, \\x%l列車;#00ffc040;đoàn tàu%l;#; thịt nướng――à không.\\nỪm, đổi tên thành chuyến tàu BBQ rồi nhỉ.」"
2236 = "「\\x%l列車;#00ffc040;Đoàn tàu%l;#; thử nghiệm đầu tiên!\\nTớ nhất định sẽ ngồi cùng Fukami nha!!」"
2389 = "「Đây là \\x%l列車;#00ffc040;đoàn tàu%l;#; số 1 đầy vinh quang. Thú thực là anh cũng có suy nghĩ\\nmuốn nhắm mắt làm ngơ trước vài rắc rối nhỏ để cố chạy cho xong. Nhưng,」"
2393 = "「Chắc chắn \\x%l列車;#00ffc040;đoàn tàu%l;#; này sẽ nổi tiếng lắm đây.\\nRồi Ohitoyo――sẽ lại trở thành một thị trấn nhộn nhịp nhỉ.」"
2395 = "「Nhắc mới nhớ, chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; đầu tiên chị Paulette và mọi người\\ncũng không đi nha.」"
2430 = "「Nào, đúng như lời Hibiki đã nói,\\nđây là \\x%l列車;#00ffc040;đoàn tàu%l;#; số 1 vô cùng đáng nhớ ạ.」"
2464 = "「Lúc \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ quay về, số người sử dụng thuyền xuôi dòng từ bến tàu Yunoi\\nđến Ohitoyo cũng đang tăng lên đều đặn mà.」"
2769 = "Ngài Aki đã giới thiệu bức ảnh chụp \\x%l列車;#00ffc040;đoàn tàu%l;#; số 1\\nmà chúng tôi gửi trên mạng."
```

### 01_Hachiroku/ハチロク06_それぞれの傷跡.txt.toml

```toml
1501 = "「Đây cũng là một hình thức \\x%l列車;#00ffc040;đoàn tàu%l;#; du lịch địa phương……\\nNếu giải quyết được một số vấn đề, tôi nghĩ là sẽ ổn thôi.」"
1572 = "「Ra vậy, như thế thì khá là tàn nhẫn nhỉ.\\nVì hành khách chủ yếu của chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; này là những học sinh đang tuổi ăn tuổi lớn mà.」"
1737 = "「Để xem nào――biện pháp xử lý mùi hương. Tôi nghĩ là cần thiết đấy.\\nNếu mùi thịt nướng bay sang phía \\x%lキハ07;#00ffc040;KiHa 07%l;#;――phía \\x%l列車;#00ffc040;đoàn tàu%l;#; chạy thường ngày thì……」"
2023 = "「Đầu tiên là thời gian.\\nBuổi sáng thì hơi quá sớm đối với một chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; du lịch.」"
```

### 01_Hachiroku/ハチロク07_ハチロクの目覚め.txt.toml

```toml
2079 = "Đổi đầu máy do sự cố phương tiện.\\nChủ thể của \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ suy cho cùng vẫn là \\x%l客車;#00ffc040;toa hành khách%l;#;――"
2085 = "Khi quyết định cứu Hachiroku.\\nKhi tự mình lựa chọn trở thành \\x%l機関士;#00ffc040;lái tàu%l;#;, vào lúc đó."
2316 = "Vì vậy,\\ntôi muốn trực tiếp giải quyết khiếu nại và xin lỗi với tư cách là \\x%l機関士;#00ffc040;lái tàu%l;#;."
```

### 01_Hachiroku/ハチロク07_延命.txt.toml

```toml
1662 = "「Chỉ là tên gọi tạm thôi. Một thứ không có tên chính thức――\\nLà 'thứ khiến \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; trở thành \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;'」"
2444 = "「Thứ khiến \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;――trở thành \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;」"
2839 = "「Ý ngài là dù có cố gắng tái tạo…… hay chế tạo mới \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;,\\ncũng không thể thực hiện được――đúng không ạ?」"
3121 = "Chắc là trong vô thức. Hachiroku chạm vào chiếc \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; trên cổ.\\n\\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;…… quả thực là một thứ vô cùng khó định nghĩa."
```

### 01_Hachiroku/ハチロク09_もくもくオリヴィ.txt.toml

```toml
2028 = "「Cái đó——ở Đế đô thì sao?\\nThời Teitetsu, em đã từng nhìn thấy những cảnh sắc tuyệt vời nào qua cửa sổ?」"
```

### 01_Hachiroku/ハチロク09_採決.txt.toml

```toml
1894 = "「Tính công cộng. Sự liên kết nhẹ nhàng với những người khác, được yêu thích và đánh giá cao.\\nSự thành công vang dội của \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ, chính là biểu hiện của sở thích đó.」"
1937 = "「Anh Migita là \\x%l機関士;#00ffc040;Lái tàu%l;#; trưởng kiêm người chịu trách nhiệm vận hành của \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ——\\nĐầu máy 8620 đúng không ạ?」"
2100 = "「Về việc vận hành \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ,\\nchắc cô cũng biết là đang có những lời phàn nàn phát sinh đúng không?」"
2174 = "「Vâng. Tôi chịu trách nhiệm toàn bộ việc vận hành,\\ncủa \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ do Đầu máy 8620 đảm nhận.」"
3064 = "Để làm được điều đó, sự hồi sinh của \\x%l8620;#00ffc040;8620%l;#;, và\\nviệc kích hoạt mạnh mẽ hơn nữa \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ là điều bắt buộc."
```

### 01_Hachiroku/ハチロク10_旺宮鉄道歴史館.txt.toml

```toml
1479 = "「Khả năng tự sao chép của \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;——của linh hồn. Hoặc là chức năng sinh sản.\\nChẳng phải là để giải trừ phong ấn được đặt trên đó sao.」"
1488 = "「Các loại kiểm tra theo luật định của \\x%lレイルロオド;#00ffc040;Railord%l;#;,\\ntất cả đều được tiến hành trong trạng thái tháo \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;, tức là trạng thái không khởi động.」"
2113 = "「Trên toàn thế giới, \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; của tất cả các \\x%lレイルロオド;#00ffc040;Railord%l;#;,\\nđều được xuất xưởng từ một nhà máy duy nhất.」"
2146 = "「Tháo \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; ra khỏi cả \\x%l運転体;#00ffc040;thân vận hành%l;#; lẫn \\x%l整備体;#00ffc040;thân bảo trì%l;#;, rồi đem đi cất giữ.\\nTrạng thái đó, đã……kéo dài được hơn bốn năm rồi thì phải.」"
2184 = "「Chỉ cần suy ngược lại là được. Rằng 『\\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; mang một bản chất\\nsẽ bị loại bỏ nếu được biết đến quá rộng rãi』 đúng không?」"
2190 = "「Vậy mà, nếu như họ đã loại bỏ \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;.\\nThì mục đích của Đại bãi bỏ chính là——tiêu diệt \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;.」"
2238 = "「Dù có chế tạo một cơ thể mới hay làm bất cứ điều gì đi chăng nữa,\\n\\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; cũng chắc chắn sẽ già yếu đi, và cuối cùng, sẽ phải đối mặt với cái chết không thể tránh khỏi.」"
2416 = "「Tốt lắm. Vậy thì, tôi có thể tiến hành phân tích và sao chép\\n\\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; của cô Hachiroku được chứ?」"
2493 = "「Nói cách khác, \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; chỉ có ở một nơi duy nhất——\\nkhông, nếu nói một cách chính xác hơn, thì có lẽ là」"
2507 = "「Nếu vậy, hoàn toàn không cần thiết phải\\nloại bỏ \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; khỏi Navi Aircra. Vậy mà」"
2551 = "「Như tôi đã nói lúc nãy, Navi Aircra và \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;,\\nvốn dĩ nên là những thứ cùng tồn tại với nhau.」"
2564 = "「Là thứ trú ngụ bên trong \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; sao ạ?」"
2606 = "「Thế nhưng, thực tế là \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; đã bị loại bỏ.\\nThậm chí, nguồn cung cấp duy nhất của nó cũng đã bị đóng lại.」"
2636 = "「Đương nhiên, công ty \\x%lレイルロオド;#00ffc040;Railord%l;#; Tablet cũng bị đóng cửa và giải thể.\\nBởi vì công nghệ chế tạo \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; đã hoàn toàn bị thất truyền.」"
2731 = "「Một cơ chế không hề có từ thế hệ thứ nhất trở đi.\\nNói cách khác, là Navi Aircra có chứa \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; bên trong.」"
2866 = "「Trước khi tháo \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; ra, cô ấy vẫn đang hoạt động sao?」"
2894 = "「Nếu vậy, mức độ mở hoàn toàn là——đúng như nghĩa đen,\\ntất cả những gì bên trong \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;——\\x%l共感;#00ffc040;cộng cảm%l;#; toàn bộ lĩnh vực, sao?」"
3241 = "Nhưng, nếu việc giải trừ phong ấn là chìa khóa.\\nThì việc sao chép, hay sáng tạo ra \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; vốn được cho là bất khả thi hiện nay——"
3266 = "Những ngón tay của Hachiroku đưa lên trước ngực——\\nnhư đang bấu chặt lấy \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; của mình."
```

### 01_Hachiroku/ハチロク10_炙り出し.txt.toml

```toml
1940 = "「Vâng. Hôm nay \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ cũng\\nkín chỗ đến chín phần rồi, nên em ấy đang rất hăng hái ạ.」"
2694 = "Có lẽ em ấy đã nhường lời để tôn trọng \\x%l機関士;#00ffc040;lái tàu%l;#; là tôi chăng.\\nĐược tôi gợi ý, Hachiroku bắt đầu trình bày một cách trôi chảy."
```

### 01_Hachiroku/ハチロク11_幽霊.txt.toml

```toml
2184 = "「Là anh \\x%l機関士;#00ffc040;lái tàu%l;#; của \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ sao.」"
2701 = "Tất nhiên, dù có xa cách đôi chút,\\nnhưng chúng em vẫn là \\x%l機関士;#00ffc040;lái tàu%l;#; và \\x%lレイルロオド;#00ffc040;Railord%l;#;."
```

### 01_Hachiroku/ハチロク11_御一夜鉄道小畑線.txt.toml

```toml
109 = "\\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;——Linh hồn chắc chắn sẽ, \\nchịu sự hao mòn không thể đảo ngược theo thời gian."
1213 = "「Bản thân \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; là thứ dùng chung trên toàn thế giới. \\nVì vậy, giả sử 'thuyết chủng loài \\x%lレイルロオド;#00ffc040;Railord%l;#;' là đúng thì——」"
1702 = "「Bởi vì dù có đóng băng bảo quản, rồi từ \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; của Olivy, tạo ra một bản sao của Olivy đi chăng nữa.」"
1763 = "「A... ừm. Đúng vậy! \\nNếu thế thì chìa khóa có thể đã được nhúng sẵn trong chính \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; rồi!」"
1883 = "「Cho dù \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; có giúp ích được theo cách đó. Thì sau đó. \\nOlivy, có lẽ sẽ không biết——mình nên làm gì nữa.」"
1915 = "「Chuyện \\x%lレイルロオド;#00ffc040;Railord%l;#; có thể được tạo ra như một chủng loài. \\nChuyện \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; có thể sinh sản... nhân bản? được ấy.」"
2197 = "「Lời khuyên dư thừa và dai dẳng. Kiyoharu. Trước khi trở thành \\x%l運転士;#00ffc040;người lái tàu%l;#; điện. \\nĐã từng là \\x%l機関士;#00ffc040;lái tàu%l;#; hơi nước. Tuyến đường dốc——Tuyến Hitahikoyama cũng đã từng có kinh nghiệm rồi.」"
2251 = "「Ngài Công chúa Tàu điện đã nói—— \\n'Việc tinh luyện lại Lõi Lord từ \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;'」"
2513 = "Cho dù chúng ta không thể chạy được nữa, \\nchúng ta vẫn có thể trao lại \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; cho thế hệ tiếp theo."
```

### 01_Hachiroku/ハチロク12_ムナカタ来訪.txt.toml

```toml
1594 = "「Hachiroku, hãy dùng máy tính bảng này, kết hợp với Navi, \\nthu thập thông tin về mạch nước ngầm và hoạt động núi lửa xung quanh đây nhé.」"
2091 = "「Mối quan hệ giữa Tuyến chính Kagoshima cũ (hiện tại bao gồm đoạn Sendai - Yatsushiro của Đường sắt Mikan) \\nvà Tuyến Hisatsu cũ, nếu so sánh với khu vực Đế đô thì」"
```

### 01_Hachiroku/ハチロク12_再開発.txt.toml

```toml
2973 = "Tôi bế Hachiroku đặt vào buồng lái.\\nNgay sau đó, có tiếng lạch cạch đổi \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;."
2977 = "Tôi lấy bàn tay trái cong vào trong làm đường ray,\\nnắm đấm phải dựng ngón cái lên làm \\x%l列車;#00ffc040;đoàn tàu%l;#; rồi trượt đi."
3088 = "Bởi vì hiện tại, chúng tôi gần như đã phản bội lại\\nnhững kỳ vọng được thổi bùng lên từ chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ."
3195 = "Bước xuống sàn, Hachiroku chuyển \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; sang \\x%l整備体;#00ffc040;thân bảo trì%l;#;."
```

### 01_Hachiroku/ハチロク13_夜の嵐.txt.toml

```toml
1538 = "「Hachiroku, xuống đi. Đổi \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; cho tôi.」"
2326 = "Thấy vậy, Hachiroku đổi \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;,\\ntrở lại \\x%l運転体;#00ffc040;thân vận hành%l;#; và cất giọng nghiêm túc."
2328 = "Thấy vậy, Hachiroku\\ntháo \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; ra và chuyển sang \\x%l運転体;#00ffc040;thân vận hành%l;#;."
2336 = "Hachiroku lập tức chuyển \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; về lại \\x%l整備体;#00ffc040;thân bảo trì%l;#;.\\nVậy thì tôi chỉ còn cách cầm xẻng lên lại thôi."
```

### 01_Hachiroku/ハチロク14_冬.txt.toml

```toml
2342 = "「Nhưng người thực sự đến thăm chỉ có Niiroku thôi.\\n\\x%l機関士;#00ffc040;Lái tàu%l;#; Akai bảo là bị kéo đi mua sắm cùng.」"
2371 = "「Niiroku xuống ngay lập tức, rồi bảo 『Xin lỗi vì đã làm phiền』.\\nNhanh quá mức khiến \\x%l機関士;#00ffc040;lái tàu%l;#; Akai cũng phải tròn mắt ngạc nhiên.」"
2474 = "「Đến đó cũng vậy thôi.\\nCái này, là do \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; đã tơi tả rồi.」"
2497 = "「Ngắn lắm luôn! Em không thể bỏ mặc \\x%l機関士;#00ffc040;lái tàu%l;#; Akai được\\nnên đã pha trà mời ở đây, nhưng mà.」"
2851 = "「Tôi muốn nhờ \\x%l機関士;#00ffc040;lái tàu%l;#; Akai cùng hai ông ấy và Nagi trao đổi thông tin,\\nđể lập danh sách các ứng viên giám sát thường trực.」"
2920 = "「Đúng vậy? Hôm qua, cùng với \\x%l機関士;#00ffc040;lái tàu%l;#; Akai đó.」"
2997 = "「Bỏ cuộc bây giờ là quá sớm. Ví dụ như ngày mai, có thể\\nsẽ phát hiện ra kiến thức mới liên quan đến \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; thì sao.」"
3155 = "「Cả \\x%l機関士;#00ffc040;lái tàu%l;#; Akai nữa sao.」"
3757 = "Nếu là \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; bị hỏng, thì không thể sửa được.\\nCả ông Tororyu-yu, Tiến sĩ Fushicho, hay bất kỳ ai khác cũng vậy."
3854 = "Tôi xác nhận ngắn gọn những điểm chính,\\nrồi cúp máy, quay sang \\x%l機関士;#00ffc040;lái tàu%l;#; Akai."
3983 = "Đúng là, với \\x%l運転体;#00ffc040;thân vận hành%l;#; thì việc mua sắm cũng bất tiện.\\n\\x%l機関士;#00ffc040;Lái tàu%l;#; Akai, dù là chuyện thường ngày nhưng cũng vất vả thật."
4065 = "Cho cô Paulette, cho Reina, cho Niiroku, cho \\x%l機関士;#00ffc040;lái tàu%l;#; Akai.\\nEm chỉ muốn truyền đạt lại những lời vừa rồi, cho tất cả những người có duyên gặp gỡ."
```

### 01_Hachiroku/ハチロク14_橋.txt.toml

```toml
2368 = "Sau vụ tai nạn đó. Từ \\x%l機関士;#00ffc040;lái tàu%l;#; cho đến những người đồng đội.\\nTừ tất cả những người đã cùng chung sống trong khoảng thời gian đó——"
2374 = "Vì không có phụ lái tàu, tôi phải quay sang xúc than,\\nnên người lái \\x%l8620;#00ffc040;8620%l;#; với tư cách là \\x%l機関士;#00ffc040;lái tàu%l;#;, chính là Hachiroku."
2678 = "Cảm giác an tâm khi tôi làm \\x%l機関士;#00ffc040;lái tàu%l;#; kết hợp với \\x%l運転体;#00ffc040;thân vận hành%l;#; của Hachiroku——\\ncảm giác có thể hoàn toàn giao phó tấm lưng cho nhau, bây giờ không còn nữa."
2927 = "（Để Hachiroku——đóng vai trò \\x%l機関士;#00ffc040;lái tàu%l;#;）"
```

### 01_Hachiroku/ハチロク15_家族.txt.toml

```toml
2717 = "Đang tiến vào sân ga.\\n\\x%l列車;#00ffc040;Đoàn tàu%l;#; này, đã đến nhà ga cuối cùng."
```

### 01_Hachiroku/ハチロク15a_痛みとの決別.txt.toml

```toml
2031 = "「Cảm ơn cô.\\nDù tao bây giờ, đối với cô, chẳng còn là \\x%l機関士;#00ffc040;lái tàu%l;#; hay gì nữa」"
2748 = "Vượt qua cả ngôn từ, vang vọng trực tiếp vào sâu bên trong \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;,\\n『Dừng lại』 『Hãy đảm bảo an toàn』."
```

### 01_Hachiroku/ハチロク15b_さよなら列車.txt.toml

```toml
1577 = "「Chị mang đồ tiếp tế cho các \\x%l機関士;#00ffc040;lái tàu%l;#; đây」"
1721 = "「Hibiki, làm \\x%l機関士;#00ffc040;lái tàu%l;#;! Anh sẽ làm phụ lái」"
2333 = "（Cả Fukami, Nagi——Niiroku và \\x%l機関士;#00ffc040;lái tàu%l;#; Akai,\\ncả Paulette và Reina nữa——tất cả mọi người, đều có chung một tâm trạng）"
```

### 01_Hachiroku/ハチロク16_春.txt.toml

```toml
1611 = "「Hình như là 『Từ \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; của một \\x%lレイルロオド;#00ffc040;Railord%l;#; đã hoạt động hơn một trăm năm,\\nmột Lõi Railord hoàn toàn mới đã được tinh chế ra』 thì phải?」"
1995 = "「Tất nhiên là tôi muốn tự tay nuôi dưỡng con bé rồi. Dù sao đây cũng là một trường hợp vô cùng quý giá,\\ntinh chế ra hai Lõi Railord từ một \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; duy nhất cơ mà.」"
2298 = "Nói cách khác, nó giống như là “linh hồn” của \\x%lレイルロオド;#00ffc040;Railord%l;#; vậy.\\nThứ đó, đã được tinh chế từ \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; của Olivy――"
2307 = "Lõi Railord. Thứ làm cho \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; trở thành \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;\\nlàm cho \\x%lレイルロオド;#00ffc040;Railord%l;#; trở thành \\x%lレイルロオド;#00ffc040;Railord%l;#;……"
2509 = "Việc tinh chế từ \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; có lẽ đồng nghĩa với việc chức năng đã ngừng hoạt động,\\nnhưng dù vậy, chúng tôi vẫn có thể tự mình kết nối với tương lai."
```

### 01_Hachiroku/ハチロクh1_契り.txt.toml

```toml
1382 = "「Thẻ bảng, tháo ra như vậy có sao không?」"
2013 = "Thậm chí, em ấy còn tháo cả thẻ bảng ra."
```

### 01_Hachiroku/仲国06_聖都とパンダとハチロクと.txt.toml

```toml
1435 = "「Rất tiếc, nhưng ngày kia, tức là một ngày sau ngày dự định về nước,\\nThị trưởng Paulette đã có lịch họp ở Đế đô rồi ạ.」"
```

### 01_Hachiroku/共通03_ハチロクとナビ.txt.toml

```toml
1320 = "「Là chuyện đó đấy.\\nTôi từ Đế đô trở về là để ngăn chặn điều đó.」"
1516 = "「Nhưng tại sao, nó lại lan đến tận chỗ tôi ở Đế đô——\\nChiến dịch thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; lại trở nên rầm rộ đến vậy?」"
1638 = "「Đó là điều hiển nhiên ạ. Việc điều khiển phương tiện động lực và \\x%l列車;#00ffc040;đoàn tàu%l;#;,\\nsẽ do \\x%lレイルロオド;#00ffc040;Railord%l;#; cùng với \\x%l機関士;#00ffc040;lái tàu%l;#; hoặc \\x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; phối hợp thực hiện.」"
2108 = "Người lái đầu máy xe lửa thì gọi là \\x%l機関士;#00ffc040;lái tàu%l;#;.\\nCòn người điều khiển các phương tiện động lực khác thì gọi là \\x%l運転士;#00ffc040;nhân viên cơ vụ%l;#;, tôi được dạy như vậy."
```

### 01_Hachiroku/共通06_8620を探せ.txt.toml

```toml
73 = "Nếu vậy thì số lượng \\x%l機関士;#00ffc040;lái tàu%l;#; và \\x%lレイルロオド;#00ffc040;Railord%l;#;,\\nchắc hẳn cũng phải rất đông đảo mới đúng……"
1573 = "……A, âm thanh này.\\nLà tiếng \\x%l列車;#00ffc040;đoàn tàu%l;#; chạy sao."
1957 = "「Em vẫn đang ở trên chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; này sao.」"
2027 = "「Nhưng mà, chuyện \\x%l機関士;#00ffc040;lái tàu%l;#; này nọ thực ra,\\ncũng có thể liên quan đến phong trào phản đối thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; đấy.」"
2112 = "「Ở \\x%l機関区;#00ffc040;kho đầu máy%l;#; Teiou, trong một thời gian dài chỉ có một mình cô Kiyomi là người lái tàu thôi ạ.\\nTuy nhiên, trong thời chiến thì số lượng nữ \\x%l機関士;#00ffc040;lái tàu%l;#; đã tăng lên rất nhiều.」"
2119 = "「Chắc chắn đôi mắt của Paulette cũng đang nhìn thấy \"màu đỏ\" như vậy,\\nở đoàn \\x%l列車;#00ffc040;đoàn tàu%l;#; mà trong mắt Hibiki chỉ là đống sắt vụn.」"
2129 = "「Phụ nữ…… \\x%l機関士;#00ffc040;Lái tàu%l;#; là \\x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; đầu máy xe lửa nhỉ.\\nNgày xưa cũng có người như vậy sao?」"
2137 = "「Dù nhìn từ góc độ nào thì cũng chỉ là một đoàn \\x%l列車;#00ffc040;đoàn tàu%l;#; rách nát như đống sắt vụn,\\nnhưng ở hội đồng thành phố lại bảo là \"có giá trị lịch sử tuyệt vời\"」"
2216 = "「\\x%lレイルロオド;#00ffc040;Railord%l;#; chúng em và đoàn \\x%l列車;#00ffc040;đoàn tàu%l;#; của mình,\\ncó thể nói là anh em ruột thịt cùng chung dòng máu ạ.」"
2257 = "「Các \\x%l機関士;#00ffc040;lái tàu%l;#; bị trưng dụng thời chiến rất sợ cô Kiyomi.\\nThế nên bồn tắm lúc nào cũng chỉ có hai chúng em độc chiếm thôi ạ.」"
2422 = "「Bắt anh hai làm \\x%l機関士;#00ffc040;lái tàu%l;#; á!? Sao có thể!\\nThời gian anh ở nhà sẽ ít đi mất——à không phải!」"
2451 = "「Chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; này…… đang đi về đâu vậy nhỉ.」"
2694 = "Bởi vì chuyến hành trình cuối cùng trên chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; này——\\ntôi đã đi cùng Michiko, bố và mẹ mà."
3112 = "Bố và mẹ không có trên tàu.\\nMichiko vẫn luôn đi trên chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; này một mình."
```

### 02_Hibiki/共通02_日々姫と真闇と人形と.txt.toml

```toml
2339 = "「Và, ngài Hibiki là âm vang (Hibiki) được tạo ra giữa đường ray và \\x%l列車;#00ffc040;đoàn tàu%l;#;.\\nNgài Taito đã đặt cho các cháu của mình những cái tên thật tuyệt vời.」"
```

### 02_Hibiki/日々姫02_日々姫の日々.txt.toml

```toml
2713 = "Bản thân tôi, dù nhìn thế nào cũng chỉ là một \\x%l機関士;#00ffc040;lái tàu%l;#; tập sự.\\nChỉ bảo người khác thì quá tự cao rồi."
```

### 02_Hibiki/日々姫03_客車手配.txt.toml

```toml
2862 = "「Vậy là quyết định rồi nhé! Chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; đầu tiên từ Yunoi về Ohitoyo,\\nngười đặt chỗ số 1 là em và Fukami nha!」"
3604 = "Bây giờ, khi đã được công nhận là một \\x%l機関士;#00ffc040;lái tàu%l;#;,\\ntôi là chủ sở hữu và cũng là Master của Hachiroku."
```

### 02_Hibiki/日々姫04_カフェキッチン.txt.toml

```toml
2134 = "「Vâng. Tôi đã học ở trường làm bánh kẹo ở Đế đô, rồi làm việc trong bếp của khách sạn.\\nSau đó bị tiền bối Houshou kéo đến đây.」"
```

### 02_Hibiki/日々姫04_同乗.txt.toml

```toml
2432 = "Khi thay \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; và trở thành thân vận hành nhỏ bé,\\nHachiroku lại càng trở nên đáng tin cậy hơn."
```

### 02_Hibiki/日々姫05_市議会見学.txt.toml

```toml
2470 = "Nhưng tôi cũng không ghét việc nấu ăn.\\nHồi còn sống một mình ở Đế đô, tôi cũng từng mày mò đủ món."
2701 = "Tiếng phổ thông, hay Đế đô. Những thứ đó quả thực rất đáng ngưỡng mộ,\\nnhưng Ohitoyo cũng có những điều thú vị riêng của Ohitoyo."
```

### 02_Hibiki/日々姫06_日々姫の決断.txt.toml

```toml
2398 = "「Đó là lời đề nghị muốn ký hợp đồng trọn gói cho quảng cáo trong \\x%l列車;#00ffc040;đoàn tàu%l;#;,\\nquảng cáo tại ga, quảng cáo trên tuyến đường... với tư cách là Ngân hàng Kumamoto.」"
3259 = "Cảm thấy bất ngờ, và ngay khoảnh khắc đó, tôi chợt nhớ ra.\\nNhắc mới nhớ, \\x%l機関士;#00ffc040;lái tàu%l;#; trước đây của Hachiroku là phụ nữ."
3394 = "Hoặc cũng có thể \\x%l機関士;#00ffc040;lái tàu%l;#; đó,\\nđã từng bị những tin đồn như vậy làm cho khốn đốn cũng nên."
```

### 02_Hibiki/日々姫08_開きかけのつぼみ.txt.toml

```toml
2155 = "「Nói thẳng ra thì――\\nEm có thể luân phiên làm \\x%l機関士;#00ffc040;lái tàu%l;#; \\x%l8620;#00ffc040;8620%l;#; với anh được không?」"
2299 = "「Đúng là với tư cách là đầu máy số 1 như em,\\nviệc chỉ có Master làm \\x%l機関士;#00ffc040;lái tàu%l;#; mới là hình mẫu chuẩn mực ạ.」"
2838 = "Do đó, với thể chế Paulette làm \\x%l機関士;#00ffc040;lái tàu%l;#; - tôi làm \\x%l機関助士;#00ffc040;phụ lái tàu%l;#;,\\nchắc chắn sẽ dễ dàng và mang lại kết quả tốt hơn so với chiều ngược lại."
3052 = "Không có \\x%l客車;#00ffc040;toa hành khách%l;#;, thì không thể biến \\x%l8620;#00ffc040;8620%l;#; thành \\x%l列車;#00ffc040;đoàn tàu%l;#; du lịch được.\\nVà hiện tại, chúng tôi chỉ có duy nhất một \\x%l客車;#00ffc040;toa hành khách%l;#; có khe hở khiến khói bay thẳng vào."
```

### 02_Hibiki/日々姫14_投開票.txt.toml

```toml
1597 = "「Không đổi \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; sang \\x%l運転体;#00ffc040;thân vận hành%l;#; sao?」"
```

### 02_Hibiki/日々姫16_夢を乗せて.txt.toml

```toml
2340 = "Nhanh chóng thay \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;, Hachiroku chuyển sang thân bảo trì."
```

### 03_Paulette/れいな02_れいなとポーレット.txt.toml

```toml
1182 = "……À. Ra vậy. Có lẽ do khoảng cách thế hệ,\\nnhững đứa trẻ như Nagi đã không còn biết đến \\x%l列車;#00ffc040;đoàn tàu%l;#; chở hàng nữa rồi."
1856 = "「Tuyến đường vòng sầm uất nhất Đế đô. Ở tuyến Yamanote,\\ncứ hai phút lại có một chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; chạy không ngừng nghỉ ạ.」"
1955 = "「Đúng vậy. Ngoài ra,\\n\\x%l列車;#00ffc040;đoàn tàu%l;#; chở hàng chạy trên tuyến chở khách cũng là chuyện thường xuyên xảy ra.」"
2127 = "「Đi cùng với \\x%l列車;#00ffc040;đoàn tàu%l;#; chở hàng luôn nè!?\\n\\x%l客車;#00ffc040;Toa hành khách%l;#; như thế, nghe có vẻ thú vị quá nè!!」"
2657 = "Reina nhảy xuống sàn, nhanh nhẹn tháo lắp \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;."
```

### 03_Paulette/グランドリライト04_ポーレット.txt.toml

```toml
1935 = "「Ufufu, chiếc huy hiệu số một đáng nhớ này,\\ntất nhiên phải dành tặng cho \\x%l機関士;#00ffc040;lái tàu%l;#; rồi!」"
```

### 03_Paulette/ポーレット01_御一夜探し.txt.toml

```toml
1748 = "「Là kiểu người hâm mộ đường sắt lấy việc đi \\x%l列車;#00ffc040;đoàn tàu%l;#;\\nđể thưởng thức cơm hộp nhà ga và đặc sản địa phương làm mục đích chính ấy.」"
```

### 03_Paulette/ポーレット02_解放b寝台.txt.toml

```toml
2078 = "「Tức là, tàu của Michitetsu—— hay nói đúng hơn là tàu của chủ tàu thuộc sở hữu của Michitetsu, đang chạy trên tuyến đường sắt của Tokitetsu à.」"
```

### 03_Paulette/ポーレット03_大きなにもつのおばあさん.txt.toml

```toml
2412 = "Chốc lát im lặng.\\nChỉ còn tiếng bánh xe chủ động gõ lên đường ray vang đều đều trong toa."
```

### 03_Paulette/ポーレット03_廃炭鉱.txt.toml

```toml
2814 = "Trong \\x%l運転台;#00ffc040;buồng lái%l;#; của \\x%lキハ07;#00ffc040;KiHa 07%l;#; mà em còn chưa quen, Hibiki lúc này không phải \\x%l機関助士;#00ffc040;phụ lái%l;#; cũng không phải \\x%l機関士;#00ffc040;Lái tàu%l;#;, mà đang đóng vai trò \\x%l運転士;#00ffc040;người lái%l;#;."
```

### 03_Paulette/ポーレット04_鳴呼いきストーブ列車.txt.toml

```toml
2020 = "「Tôi đã nhờ bạn bè chủ tàu ở đây xếp hàng ở quầy vé giúp mà. Đúng kiểu đánh trúng mục tiêu đấy.」"
2076 = "「Con đọc được nè~! \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;!!」"
2542 = "Chắc là cô ấy đang muốn dành vinh dự cho tôi, với tư cách là một người cha, một chủ tàu."
2642 = "Đọc được Thẻ bảng, Express, nhưng lại không đọc được 『Bracelet』 (Vòng tay)."
```

### 03_Paulette/ポーレット08_未来へのレール.txt.toml

```toml
2090 = "「4 bánh xe chủ động, 2 bánh dẫn hướng trước, 3 bánh xe chịu tải sau.\\nSơ đồ trục \\x%l2D3;#00ffc040;2D3%l;#;, \\x%l4-8-6;#00ffc040;4-8-6%l;#;. À」"
```

### 03_Paulette/ポーレット09_ストーブ客車.txt.toml

```toml
1746 = "「Đến lúc đó, em đi cùng tôi nhé? Lên chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; sưởi ấm của Tsutetsu――ở Tsugaru, Aomori.」"
2219 = "「Đường \\x%l単線;#00ffc040;đơn%l;#; ạ. Chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; sưởi ấm rất đỗi tĩnh lặng.\\nGiọng Tsugaru của cô hướng dẫn viên, lần đầu tiên nghe nhưng lại thấy thật hoài niệm.」"
2229 = "「Dạ! Chuyện lúc nãy――\\nỪm, chuyện anh nói muốn trải nghiệm \\x%l列車;#00ffc040;đoàn tàu%l;#; sưởi ấm ấy.」"
2232 = "「À ừm, Tsutetsu và chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; sưởi ấm vẫn đang hoạt động đấy ạ.\\nLà một chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; du lịch, nó nổi tiếng nhất nhì luôn đó.」"
2634 = "Chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; du lịch số một Hinomoto――\\nNếu chỉ biết bắt chước, thì sẽ chẳng bao giờ vượt qua được nó."
```

### 03_Paulette/ポーレット10_見えない傷.txt.toml

```toml
959 = "“Một kẻ thiếu kinh nghiệm như tôi mà tự nhận là \\x%l機関士;#00ffc040;lái tàu%l;# thì thật quá tự cao”\\nTôi đành phải nuốt ngược câu trả lời nảy ra đầu tiên trong đầu mình xuống."
1241 = "「Quả nhiên, \\x%l機関士;#00ffc040;lái tàu%l;# có khác nhỉ.\\nAnh rất bình tĩnh và nắm bắt trọng tâm rất tốt.」"
1461 = "「Vì vậy, chúng ta mới thiết lập một \\x%l列車;#00ffc040;đoàn tàu%l;# lâm thời,\\nvừa kết hợp chạy tập luyện không có hành khách, vừa để đưa tôi đi luôn.」"
```

### 03_Paulette/ポーレット11_記憶と記録.txt.toml

```toml
998 = "「\\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#……không chỉ ghi chép mà còn ghi nhớ luôn sao? Nhưng nếu nó gần giống với não bộ, thì có lẽ bộ vi xử lý cũng——」"
1349 = "「Chỉ cần thay đổi \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#, thì bất kỳ \\x%lレイルロオド;#00ffc040;Railord%l;# nào cũng có thể thực hiện được chức năng tương tự——」"
1528 = "「Ý tôi là vậy đấy. Nếu làm vậy mà có thể chạy lại được, thì có [khởi tạo,2]khởi tạo lại \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# của tôi cũng không sao.」"
1551 = "「Ví dụ, nếu lắp \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# của Hachiroku vào cơ thể của Reina, thì cơ thể đó sẽ——」"
1660 = "「Không lẽ……đó chính là, \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# sao ạ?」"
1724 = "「Vậy sao……Nghĩ kỹ lại thì, việc này chẳng khác gì cài đặt \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# của cô bé Reina cho Niiroku cả.」"
1754 = "「Nếu vậy, nếu cài đặt \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# của người khác vào đó thì——」"
2006 = "Tuy nhiên, trong trường hợp \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# của \\x%lレイルロオド;#00ffc040;Railord%l;#, thì sẽ thế nào?"
2085 = "Nếu lắp \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# đó vào một cơ thể khác, Hachiroku sẽ ngay lập tức có được một cuộc sống mới."
```

### 03_Paulette/ポーレット16_明日へのレール.txt.toml

```toml
1782 = "「Khoảng 5 phút nữa, \\x%l列車;#00ffc040;đoàn tàu%l;#; sẽ đến ga Cổng vào Mine Treasure.\\nTừ đó, xin mời quý vị chuyển sang đi xe goòng.」"
1973 = "「Cũng khá thú vị đấy.\\nTuy không được thoải mái như chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; này đâu.」"
2250 = "「Vâng. Đây là hàng dùng thử của cơm hộp bento nhà ga\\ncho \\x%l列車;#00ffc040;đoàn tàu%l;#; du lịch ở Mine Treasure, nên mọi người cứ tự nhiên nhé.」"
```

### 03_Paulette/共通04_キハ07。ポーレットとれいな.txt.toml

```toml
1811 = "「Vậy thì, lý do \\x%l待避線;#00ffc040;đường tránh tàu%l;#; không được sử dụng đến mức bị bỏ hoang,\\nlà do \"hoàn toàn không có chuyện các \\x%l列車;#00ffc040;đoàn tàu%l;#; cần tránh nhau\", phải không?」"
1814 = "「Là mặt bị \\x%l列車;#00ffc040;đoàn tàu%l;#; giẫm lên——bị bánh xe bào mòn, nên gọi là \\x%l踏面;#00ffc040;mặt lăn bánh xe%l;#; sao.\\nVì vậy, chỉ có chỗ đó là không bị gỉ sét.」"
2086 = "「Giống như \\x%l列車;#00ffc040;đoàn tàu%l;#; hay \\x%lレイルロオド;#00ffc040;Railord%l;#;——\\nNgay cả nhà ga……cũng sẽ chết đi nhỉ.」"
2260 = "「Bởi vì \\x%lレイルロオド;#00ffc040;Railord%l;#; của \\x%l列車;#00ffc040;đoàn tàu%l;#; trên tuyến đường này\\nlà một đứa trẻ rất trung thành với luật lệ, ngài Soutetsu.」"
2292 = "「Nếu đã bị bỏ hoang,\\nthì đương nhiên, \\x%l列車;#00ffc040;đoàn tàu%l;#; sẽ không chạy, và đường ray cũng sẽ không bị bào mòn.」"
2366 = "「Nếu vậy thì ở đâu đó, hẳn vẫn còn nhà ga đang sống.\\nỞ đó chắc chắn cũng có \\x%l列車;#00ffc040;đoàn tàu%l;#; và nhân viên đường sắt đang sống.」"
2967 = "A, đây là——\\nĐúng rồi. Đây là âm thanh của \\x%l列車;#00ffc040;đoàn tàu%l;#;."
3037 = "Vai trò của nó là tự vỡ vụn ra,\\nđể chịu thay đường ray những lực tác động từ \\x%l列車;#00ffc040;đoàn tàu%l;#;."
3061 = "Đường tránh tàu là đường ray được thiết lập tại các nhà ga với mục đích cho tàu đi vòng,\\nđể các \\x%l列車;#00ffc040;đoàn tàu%l;#; có thể tránh nhau trên \\x%l単線;#00ffc040;đường đơn%l;#;."
3171 = "Tuy nhiên, cùng với sự sụt giảm nghiêm trọng của số lượng \\x%l列車;#00ffc040;đoàn tàu%l;#;,\\ncác quy tắc cũng dần dần không còn được tuân thủ nữa."
3188 = "Khoảnh khắc tôi cảm nhận được \"âm thanh của \\x%l列車;#00ffc040;đoàn tàu%l;#;\",\\nkhoảnh khắc tôi nhớ lại điều đó——"
3307 = "Nếu vậy, chỉ cần đợi ở đây,\\nkiểu gì cũng sẽ có \\x%l列車;#00ffc040;đoàn tàu%l;#; đến đón chúng tôi."
```

### 04_Reina/れいな01_炭鉱探索.txt.toml

```toml
1784 = "「Dạ đúng rồi~. Ở mỏ thì \\x%l列車;#00ffc040;đoàn tàu%l;#; là để chở hàng hóa mà.\\nNên loại chỉ dùng để chở người thì được gọi đặc biệt là xe goòng chở người ạ.」"
1788 = "「Dạ đúng rồi~, nếu chất than đào được từ trải nghiệm khai thác lên \\x%l貨車;#00ffc040;toa chở hàng%l;#;,\\nthì nó cũng trở thành một \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp đàng hoàng đó ạ, Reina nghĩ vậy~」"
1794 = "「Dạ đúng rồi~. Ở mỏ Katakami thì đó là chuyện bình thường ạ.\\nBên Teitetsu thì hình như gọi là \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp hay sao ấy ạ~」"
1849 = "「Máy móc, nhân sự, bảo trì thiết bị――doanh thu từ \\x%l列車;#00ffc040;đoàn tàu%l;#; chỉ như muối bỏ bể thôi.\\nThế này, lỡ như trợ cấp bị cắt thì sao.」"
1877 = "「\\x%l列車;#00ffc040;Đoàn tàu%l;#; hỗn hợp à, nghe thú vị đấy. Mà khoan, à, không...\\nViệc chúng ta làm ở Mine Treasure, nói cách khác thì...」"
2016 = "「Nếu vậy, có lẽ chúng ta nên sử dụng cái tên \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp.\\nNghe có vẻ mới lạ, chắc chắn sẽ làm tăng thêm không khí du lịch đấy.」"
```

### 04_Reina/れいな03_しゅっぱつしんこう.txt.toml

```toml
1455 = "「Vâng ạ. Vì sẽ không còn chuyện tất cả các \\x%l列車;#00ffc040;đoàn tàu%l;#; đều trở về Ohitoyo\\nđể kết thúc một ngày như trước đây nữa.」"
2376 = "Nếu vậy thì \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp đi Yatsushiro,\\ncũng sẽ do Hibiki phụ trách."
2387 = "Ngay cả bây giờ, khi Hibiki đang trưởng thành nhanh chóng,\\nHachiroku vẫn công nhận tôi là người \\x%l機関士;#00ffc040;lái tàu%l;#; xuất sắc nhất."
```

### 05_Mayami/真闇01_再蒸留.txt.toml

```toml
1414 = "「A! Vậy ra, “từng địa phương” là——chạy những chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; shochu \\nđể thưởng thức rượu shochu đặc trưng của từng địa phương.」"
1416 = "「A! Vậy thì, \\nsẽ làm thành một chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; có thể uống thử các loại shochu hiếm sao?」"
1452 = "「Ừ, đúng vậy, trong tương lai. Nếu các tuyến đường sắt được kết nối, \\nthậm chí chúng ta có thể đi một vòng Kyushu bằng \\x%l列車;#00ffc040;đoàn tàu%l;#; shochu cũng nên.」"
1460 = "「Mọi người thấy thế nào. \\nNếu việc cho uống rượu trên \\x%l列車;#00ffc040;đoàn tàu%l;#; không có gì bất ổn thì——」"
1504 = "「Này, Sou-chan. \\nChuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; đó, em định cho chạy bao nhiêu chuyến?」"
1575 = "「Hay quá——Phân bố các chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; shochu rải rác khắp nơi. \\nVà rồi, trong tương lai. Một ngày nào đó, chắc chắn.」"
1590 = "「Ra vậy——Nếu làm một chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; như thế, \\nthì ai cũng sẽ đổ xô đi uống các loại shochu hiếm nhỉ.」"
1716 = "「Vào thời kỳ hoàng kim của đường sắt, những tuyến đường sắt tư nhân vận hành các chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; bia \\nhoàn toàn không phải là chuyện hiếm đâu ạ.」"
1779 = "「Nếu vậy, chúng ta thiết kế một chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; có thể uống rượu shochu thì sao?」"
1785 = "「Vậy là chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; uống thử so sánh không thể thực hiện được sao ạ?」"
```

### 05_Mayami/真闇02_精髄.txt.toml

```toml
1113 = "「\\x%lブレーキ;#00ffc040;Phanh%l;#; tự động của \\x%l列車;#00ffc040;đoàn tàu%l;#; được nhả ra bằng cách liên tục duy trì áp suất không khí. \\nCấu tạo của nó là khi xả áp suất thì \\x%lブレーキ;#00ffc040;phanh%l;#; sẽ hoạt động.」"
1528 = "「Biết đâu ý tưởng về chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; shochu sẽ càng sâu sắc hơn, \\nvề phần tôi, tôi rất muốn chị thử lên ngồi.」"
1780 = "「Chuyện là vậy đó. Chị Mayami có nguyện vọng gì không? \\nĐể có thể vận hành như một chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; shochu.」"
2535 = "Tất nhiên, ý tưởng về chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; shochu cũng rất quan trọng. \\nNhưng trước đó."
```

### 05_Mayami/真闇03_ひとしずく.txt.toml

```toml
1708 = "「Đỉnh thật đấy. Cứ đà này,\\nngày mà \\x%l列車;#00ffc040;đoàn tàu%l;#; shochu chạy một vòng quanh Kyushu chắc cũng không còn xa nữa đâu nhỉ.」"
1735 = "「Đúng vậy, tỉnh thứ bảy tham gia rồi.\\nThế này thì \\x%l列車;#00ffc040;đoàn tàu%l;#; shochu sẽ chạy khắp toàn bộ các tỉnh ở Kyushu luôn.」"
1768 = "「\\x%l列車;#00ffc040;Đoàn tàu%l;#; shochu, lại có thêm người tham gia sao?」"
```

### 05_Mayami/真闇h3_補習授業の廃校舎.txt.toml

```toml
3299 = "Dù là thời còn đi học, hay sau khi chuyển đến Đế đô học Đại học Hoàng gia,\\ntôi cũng chỉ biết làm theo những gì được bảo."
```

### 06_Kisaki/グランドリライト06_稀咲.txt.toml

```toml
1841 = "「Đột ngột nhảy vào Đế đô thì chắc chắn là không thể rồi. Ngay cả ở Kyushu với điều kiện tốt hơn hẳn,\\nphương án này cũng chỉ mới ở mức có thể xem xét thôi.」"
1923 = "「Nhưng……chuyển từ một công ty lớn ở Đế đô sang Đường sắt Ohitoyo,\\ndù nói ra từ lập trường của tôi thì cũng hơi...」"
2113 = "「Vâng. Nếu ông Goto muốn thực hiện thành công một dự án tương tự ở Đế đô,\\nthì điểm dừng này là an toàn và chắc chắn nhất.」"
2208 = "「Ông Nezu. Ông Tsutsumi.\\n――Bởi vì ở Đế đô nhan nhản những kẻ máu mặt hơn cả ông Goto mà.」"
2508 = "「Đó là điều hiển nhiên ạ. Ngài Soutetsu là \\x%l機関士;#00ffc040;lái tàu%l;#; của em.\\nVì ngài đã trở thành Master của em mà.」"
2519 = "「――Đột ngột triển khai ở Đế đô thì sẽ thất bại sao?」"
2702 = "「Chuyện đó là không thể nào. Khả năng dự án này thành công ở Đế đô\\nlà vô cùng nhỏ bé.」"
```

### 06_Kisaki/稀咲02_新事業案.txt.toml

```toml
1378 = "「Phía \\x%l機関士;#00ffc040;lái tàu%l;#; cũng không có gì bất thường ạ.\\nChỉ cần Thị trưởng Paulette phát tín hiệu xuất phát là——a.」"
2017 = "「V, việc để em làm đại lý \\x%l機関士;#00ffc040;lái tàu%l;#;——」"
2260 = "「Cô Kisaki sẽ làm \\x%l機関助士;#00ffc040;phụ lái tàu%l;#; tập sự. Ngài Soutetsu sẽ hướng dẫn.\\nNếu vậy, Hibiki sẽ làm \\x%l機関士;#00ffc040;lái tàu%l;#; tập sự——」"
2569 = "Tuy nhiên, công việc của \\x%l機関士;#00ffc040;lái tàu%l;#; mà chỉ cần huấn luyện vài ngày là làm được thì,\\nthực sự là chẳng có công việc nào cả."
2634 = "Ở phía ghế \\x%l機関士;#00ffc040;lái tàu%l;#;, Hibiki trượt chân ngã cái oạch.\\nNhờ vậy tôi mới nhận ra."
2649 = "Là giám đốc chi nhánh Ngân hàng Kumamoto, là tiền bối và ân nhân của Hibiki.\\nNhưng trước những điều đó——Houshou Kisaki, là một thiếu nữ."
```

### 06_Kisaki/稀咲03_純白のレール.txt.toml

```toml
1918 = "「Xin chúc mừng hai người.\\nTuần trăng mật, tôi đề xuất một chuyến đi bằng \\x%l列車;#00ffc040;đoàn tàu%l;#; nhé?」"
2513 = "Khôi phục tuyến đường thành công, nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; quyết định chuyển đến Sendai.\\nChuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; du lịch đoạn Ohitoyo - Kagoshima bắt đầu lăn bánh."
2713 = "Dù sao thì Kisaki cũng là một nhà lãnh đạo xuất sắc được mọi người công nhận của Ngân hàng Kumamoto chi nhánh Ohitoyo mà."
2923 = "Tin tức về chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; du lịch đầu tiên sẽ trở thành\\nlời quảng cáo cho đợt huy động MRF kỳ 2 bắt đầu từ hôm nay."
```

### 07_Nagi_Fukami/凪ふかみ02_命の重さ.txt.toml

```toml
1948 = "Trong lúc làm nhiệm vụ trên \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ thì không nói làm gì,\\nnhưng ngay cả trong lúc huấn luyện, tôi cũng chưa từng trải qua thời tiết khắc nghiệt đến thế này."
```

### 07_Nagi_Fukami/凪ふかみ03_三人いっしょ.txt.toml

```toml
1561 = "「Vâng!\\nAnh Soutetsu cũng cố gắng với chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ tối nay nhé!」"
```

### 07_Nagi_Fukami/凪ふかみ06_凪の欲しいもの.txt.toml

```toml
1800 = "「À, anh từng học được từ một thầy châm cứu ở Đế đô.\\nĐể xem mức độ mệt mỏi thì ấn vào đây——」"
2142 = "「Trôi chảy hơn anh tưởng nhiều đấy.\\nNghe cứ như lời của một người sinh ra và lớn lên ở Đế đô vậy.」"
```

### 07_Nagi_Fukami/凪ふかみ08c_新しい家族.txt.toml

```toml
2735 = "Lên chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; mới mang tên gia đình.\\nHướng tới――một tương lai rực rỡ hơn."
```

### 08_Niiroku/ニイロク04_終端.txt.toml

```toml
1593 = "「Không. Tuy nhiên, không được phép dừng \\x%l列車;#00ffc040;đoàn tàu%l;#; lại.\\nCho đến tận Moji, nơi sẽ tiến hành tháo dỡ——, là đi thẳng một mạch.」"
1918 = "「Vì vậy, còn lại là \\x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#;.\\nChỉ cần giải quyết được \\x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#; thì.」"
2011 = "「Nếu đã làm đến mức đó——thì anh Goto,\\ntại sao lại không cứu cả \\x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#;?」"
2054 = "「Kết quả là, một \\x%l運転体;#00ffc040;thân vận hành%l;#; trống rỗng đã bị bỏ lại.\\nMột \\x%l運転体;#00ffc040;thân vận hành%l;#; không có \\x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#;, không có \\x%l整備体;#00ffc040;thân bảo trì%l;#; cũng không có toa xe.」"
2061 = "「\\x%l運転体;#00ffc040;Thân vận hành%l;#; và \\x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#;. Chỉ cần bảo vệ được tối thiểu những thứ đó.」"
2151 = "「Nếu vậy,\\n\\x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#; sau khi xác nhận hoạt động xong, sẽ để nguyên như thế à?」"
2152 = "「Railord tự mình ném \\x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#; ra bên ngoài.\\n\\x%l機関助士;#00ffc040;Phụ lái tàu%l;#;, hoặc kẻ đi lậu vé cũng có thể làm hành động tương tự.」"
2153 = "「Railord thì,\\nsẽ được xác nhận hoạt động thông qua việc hoán đổi \\x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#;.」"
2411 = "Là một \\x%l機関士;#00ffc040;lái tàu%l;#; và Railord tuyệt vời đến thế cơ mà.\\nNếu tùy cơ ứng biến, và thu hồi được cả \\x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#; của Shiro thì——"
2624 = "\\x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#; của Shiro, vào \\x%l運転体;#00ffc040;thân vận hành%l;#; mô hình trống rỗng,\\nvà sau đó, là vào \\x%l整備体;#00ffc040;thân bảo trì%l;#; của Niiroku."
2673 = "Dù nghĩ thế nào, thì cũng quá sức chịu đựng.\\nĐến mức dù \\x%l操作板;#00ffc040;Thẻ bảng (Tablet)%l;#; có bị phá hủy ngay tức khắc, thì cũng không có gì lạ."
```

### 09_Grand/グランドリライト01_オール御一夜、成立ならず.txt.toml

```toml
2548 = "「Không phiền chút nào, tuyệt đối không ạ!\\nThế nhưng, một \\x%lレイルロオド;#00ffc040;Railord%l;#; sao có thể ép buộc \\x%l機関士;#00ffc040;lái tàu%l;#; hứa hẹn được...」"
2585 = "「Việc tôi hầu hạ bên cạnh ngài Soutetsu là điều đương nhiên. Vì đó là mối quan hệ giữa \\x%l機関士;#00ffc040;lái tàu%l;#; và \\x%lレイルロオド;#00ffc040;Railord%l;#; mà.」"
```

### 09_Grand/グランドリライト08_ふかみ.txt.toml

```toml
2123 = "「Hướng tới mục tiêu khởi hành chuyến tàu số 1, cả các doanh nghiệp\\nvà các chủ tàu đều đang nín thở chạy nước rút.」"
2572 = "Chỉ cần một doanh nghiệp, một chủ tàu bỏ cuộc,\\nthì ngay lúc đó, Nine Stars có thể sẽ tan tành mây khói."
2595 = "Chuyến tàu tiếp sức vòng quanh Kyushu - Nine Stars số 1.\\nCác chủ tàu lớn cũng bày tỏ nguyện vọng tham gia và dự định tiến vào Kyushu."
```

### 09_Grand/グランドリライト11_ナインスターズ！.txt.toml

```toml
2646 = "「Đổ mồ hôi, tôi á? \\x%l機関士;#00ffc040;Lái tàu%l;#; của \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; cơ mà?\\nChỉ chạy đến ga thôi mà đổ mồ hôi sao?」"
3554 = "Và \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; mô phỏng đồ của \\x%lレイルロオド;#00ffc040;Railord%l;#;——\\nbiểu tượng của chuyến tàu chuyển tiếp, được tôi trao lại cho \\x%l運転士;#00ffc040;lái tàu%l;#; Akai."
```

### 10_Chikuni/仲国01_副丘→北琴.txt.toml

```toml
1706 = "「Có lẽ là vậy ạ. Nếu là xác thực cá nhân của Railord,\\nthì \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#; này mới là thứ chắc chắn tuyệt đối ạ.」"
2113 = "「Hộ chiếu. Là thứ quan trọng thứ ba sau sự an toàn của bản thân và \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;#;,\\nphải luôn mang theo bên người không được rời nửa bước.」"
```

### 10_Chikuni/仲国03_北琴鉄道歴史館.txt.toml

```toml
1540 = "「\\x%l先輪;#00ffc040;Bánh dẫn hướng trước%l;#; là 1 trục 2 bánh. Bánh xe chủ động là D——4 trục 8 bánh.\\n\\x%l従輪;#00ffc040;Bánh xe chịu tải không động lực%l;#; cũng là 1 trục 2 bánh.」"
```

Kết bài

Đợt U5 xong: 8 mục / 336 dòng (T8 18, T25+T26 3 dòng riêng biệt, T27 90, T51 2, T52 20, G1 121, G2 83). 4 mục kiểm chứng 0 dòng (T9, T28, T50, T53). Cờ cần parent chốt: U5-1 (G8 Common 08 — "Thẻ bảng (Tablet)" hay "thẻ bảng" trần), U5-7 (6 dòng trùng batch đang chạy — ĐÃ GHÉP bởi coordinator 22/11, xem ghi chú §5). File: `unification/unification-t1-misc-gloss-wrong.json` (336 mục) + `unification/unification-t1-misc-gloss-REVIEW.md` + `unification/unification-snippet-t1-misc-gloss.md`.