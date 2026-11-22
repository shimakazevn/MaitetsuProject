# Snippet — Unification U13a: §1 OPEN T56–T66 (T56, T57, T58, T59, T60, T61, T63, T66)

- Đợt U13a: §1 OPEN T56–T66 theo quyết định của coordinator 22/11 ~11:25 (uỷ quyền Hieu), trên báo cáo điều tra E1: **171 dòng sửa, 33 file, 8 mục mới**.
- T56 仲国 → "Trung Quốc": **122 dòng** (72 "Trọng Quốc" + 46 "Zhongguo" tên nước + 2 "tiếng Zhongguo" → "tiếng Trung" + 1 "Nakakuni" + 1 "nước Chukoku" → "Trung Quốc"/"nước Trung Quốc"). Giữ: 76 dòng đã "Trung Quốc" (gồm 4 "tiếng Trung Quốc"), 5 "tiếng Trung", 仲国06 1796 ("trong nước").
- T57 詠国 → "Anh Quốc" (đứng riêng): **5 dòng** (1848 "Vịnh Quốc", 1529/1833/2533 "Eikoku (...)", 3529 "Anh quốc"). Giữ: 8 dòng dạng ghép "Anh" + 2 dòng đã "Anh Quốc" + ngoại lệ 真闇03 1687 (list 5 nước song song) + ハチロク09 2102 (cặp katakana với Minh Quốc).
- T58 次元流 → "Thị Hiện Lưu": **3 dòng** (凪ふかみ02 2280/2377/3109; TW 示現流 ×3, Jigen-ryū thật).
- T59 キルクイティウム → "Quirquitium": **1 dòng** (日々姫10 2458; 5/5 dòng 共通04 đã đúng).
- T60 頭取 → "Tổng giám đốc": **27 dòng** (16 "Chủ tịch" + 11 "Giám đốc"/"giám đốc ngân hàng"; giữ "ngân hàng"/"Ngân hàng Kumamoto"/"Ngân hàng Kumagin" theo dòng; 2 dòng 共通11 đã đúng). 3 dòng chỉ đổi dạng 頭取, giữ 支店長 "giám đốc chi nhánh" (ハチロク14 1731, ポーレット09 2131, 共通14 1551).
- T61 持株会社 → "công ty holding": **7 dòng** (ハチロク09 ×5, ハチロク15 1953, れいな03 1568; 3 dòng ハチロク12 đã đúng).
- T63 帝有鉄道 → "Đường sắt Đế quốc Hinomoto": **4 dòng** (日々姫01 1789, 日々姫02 60 — kèm tên luật "Đạo luật Đường sắt Đế quốc", 仲国03 2082/2248; 1134 đã đúng).
- T66 九国 → "chín tỉnh": **2 dòng** (グランドリライト07_真闇 2545/2546; 4 dòng còn lại đã đúng).
- T62/T64/T65 GIỮ NGUYÊN, 0 dòng (đã kiểm chứng: "Đảng Dân Do", "tiếng Minh Quốc", "Trừng trấp" 1828/2089 + "nước cam" 2054).
- Lượt soát 2: **171/171 tái kiểm chứng, 0 loại, 0 sửa giá trị fix.** Khối TOML 33 file / 171 key parse-verified. Nguồn `old_vn`: 150 CSV3 + 15 audit + 6 unification đã gộp + 0 moan.
- **LỆCH SỐ — coordinator lưu ý (ghi chi tiết ở REVIEW §0):** (1) T56 thực tế **122 dòng, không phải 124** như báo cáo E1 (E1 đếm trùng 2 dòng "tiếng Zhongguo" — chúng đã nằm trong "Zhongguo 48": 仲国02 27 = 26 + 2897, 仲国03 16 = 15 + 2845); tổng đợt này vì vậy là **171 dòng, không phải 173**. (2) **T66 (2 dòng) có trong quyết định coordinator nhưng không có trong bullet của task** — đã áp dụng và tách riêng theo item để loại được nếu muốn; nếu tính đúng 7 mục trong bullet thì đợt này là 7 mục / 169 dòng.
- **REBASE trên 2 batch gộp song song (§0d):** set2 (T3 帝鉄 → "Teitetsu", 240 dòng) và set3 (日ノ本 "Hinamoto" → "Hinomoto", 193 dòng) gộp trong lúc đợt này đang chạy; 5 dòng trùng (file,key) đã rebase `old_vn` lên giá trị sau set2/set3 (1529, 2175, 2082, 2083, 2251) — nhờ vậy cờ F-T63-1 (2082 nửa sau) và F-T57-1 (1529 "Hinamoto") coi như đã xong. Cờ còn mở duy nhất: **F-T56-1 — 仲国08 2823** (JP 日仲, không chứa 仲国; CUR còn "Trọng Quốc" — chờ quyết ở đợt vét U15).
- File: `unification/unification-t1-open-t56-t66-REVIEW.md` + `unification-t1-open-t56-t66-wrong.json` (171 mục, kind="terminology", item="T56"/"T57"/"T58"/"T59"/"T60"/"T61"/"T63"/"T66").

**Tổng cộng sau đợt này: 49 mục / 1.280 dòng sai (unification)** (cơ sở 41 mục / 1.115 dòng + đợt U13a 8 mục mới / 165 dòng mới — 6 dòng trùng đã gộp (U3/U4) không cộng lại; REBASE bởi coordinator: snippet gốc ghi cơ sở 21/662 đã cũ vì U9/U4/U3 gộp trong lúc agent chạy; T56 thực 122 dòng, tổng đợt 171 — xem LỆCH SỐ trong snippet).
