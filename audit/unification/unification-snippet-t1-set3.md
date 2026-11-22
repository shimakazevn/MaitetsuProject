# Snippet — Unification batch U4: §1 set-3 terminology (T6, T7, T15, T16, T41, T45, T47, T54, T55, T11, T12, T19, T20)

- Đợt U4: 11 mục thuật ngữ §1 set-3 (tất cả DECIDED — áp trực tiếp): **193 dòng sửa, 56 file**.
  - T6 日ノ本 "Hinamoto" → "Hinomoto": **34 dòng**.
  - T7 湯医 / 湯医線 "Yui" → "Yunoi": **107 dòng** (111 lần xuất hiện; 4 dòng ×2: 日々姫08 3132, グランドリライト04 2205, ポーレット08 2363, グランドリライト11 3916). Gồm 9 dòng JP kana ユノイ線 và 8 dòng "Học viện Yui" (湯医学園) → "Học viện Yunoi".
  - T15 小畑 "Obata"/"Kobata" → "Okoba": **6 dòng** (5 + 1 dòng hai mục ハチロク15a 1842).
  - T16 駿袋鉄道 "Suntetsu" → "Suntai": **1 dòng** (ポーレット02_解放b寝台 1966, ruby すんたい; TW 駿遠 sai theo JP).
  - T41 "Kiha" → "KiHa" (chính tả chính thức của JR): **18 dòng** (17 + 1 dòng hai mục ハチロク08 2840); 7/18 nằm trong gloss %l.
  - T45 冥国 "Meikoku" → "Minh Quốc": **6 dòng**.
  - T47 マスコン / マスターコントローラー → "điều khiển trung tâm": **5 dòng**.
  - T11 運転体 → "thân vận hành": **11 dòng**. T12 整備体 → "thân bảo trì": **3 dòng** (kiểm kê toàn bộ 86 dòng JP 運転体/整備体/ボディ).
  - T19 乗員 "phi hành đoàn" → "nhân viên tàu": **1 dòng** (日々姫03 2834).
  - T20 Seki "ông nội" → "ông ngoại": **3 dòng** (共通12 2182, ハチロク05 1178, グランドリライト06 2159; CHỈ dòng Seki, kiểm kê toàn bộ 25 dòng "ông nội").
  - T54 回数券 → "vé lượt" / 定期券 → "vé định kỳ": **0 dòng** — đã sửa hết trong audit (3 dòng sleeper P02 + 7 dòng 定期券, kể cả P02 1832 JP kana かいすうけん).
  - T55 仲国06 1412 → "Nhân giống": **0 dòng** — đã sửa trong unification đã gộp (U10/s6, F8).
- Cả 193 dòng đều đọc JP (+TW); 182/193 JP chứa trực tiếp thuật ngữ kanji, 9 dòng T7 JP kana ユノイ (cùng thuật ngữ), 2 trường hợp giải thích riêng (D3: ハチロク01 2828 JP dùng レイナナ, referent vẫn KiHa 07; D4: ハチロク06 2139 JP chỉ còn ruby しゅかんせいぎょき, TW 主控 xác nhận). Lượt soát 2: **193/193 tái kiểm chứng, 0 loại bỏ, 0 sửa lại**. Khối TOML 56 file / 193 khóa parse-verified (chạy lại sau rebase 3719).
- Quyết định trong batch (theo uỷ quyền): D1 — T47 bỏ "bộ" trong "bộ điều khiển trung tâm" (4 dòng: P15 1073/1981, ハチロク06 2139/2763; dạng khóa là trần, tiền lệ ハチロク06 2145); D2 — T11/T12 thống nhất cả biến thể chưa liệt kê ("thân điều khiển" ×5, "cơ thể lái tàu", "thân hình lái tàu", "cơ thể bảo dưỡng", "thân chính bảo dưỡng" — tiền lệ audit れいな01 2218 / ニイロク04 2061).
- Giữ lại: T7 địa danh 由衣 ×2 (ハチロク09 2118 — ngoại lệ đã ghi; ハチロク04 1925 — cùng địa danh, áp cùng ngoại lệ); T6 JP 日ノ本 dạng khác ×7 ("Nippon Sharyo" ×5, "Yamato Nadeshiko" ×2 — T73 OPEN); T11/T12 dương tính giả ×2 (仲国06 2327 "kíp lái" = tổ lái, 日々姫09 1942 整備体験); T19 12 dòng "phi hành đoàn" còn lại thuộc T18 (túi); T20 mục con OPEN (ハチロク09 2027 "bác Seki", 日々姫03 2368/2607, ハチロク07 2588 "các ông của Nagi", 凪ふかみ01 1884, ふかみh1 2368/2607, Grand 08 2010, 日々姫04 2668).
- Rebase chồng lấn (cảnh báo coordinator 22/11 ~11:35): 日々姫08 3719 nằm cả ở U2c (đã gộp) và batch này — old_vn đã sửa về giá trị U2c, fix = giá trị gộp "(Yunoi) … Đường sắt Ohitoyo". Hai dòng chồng U2b (Grand06 2146/2159) đã khớp giá trị gộp từ đầu. Thứ tự giá trị hiện tại đã sửa theo coordinator: **unification-đã-gộp > moan > audit > CSV3** (brief gốc viết ngược; chỉ 3719 trong batch này bị ảnh hưởng).
- Chồng lấn với file worker ĐANG CHẠY (chưa gộp — coordinator xử lý thứ tự gộp): set2 — Grand06 3472, P03 1723, ハチロク13 2555, ハチロク12 2508; T56–T66 — ハチロク10 1529.
- File: `unification/unification-t1-set3-REVIEW.md` + `unification-t1-set3-wrong.json` (193 mục, kind="terminology", item="T6"/"T7"/"T15"/"T16"/"T41"/"T45"/"T47"/"T11"/"T12"/"T19"/"T20"/"T7+T15"/"T7+T41").

**Tổng cộng sau đợt này: 32 mục / 855 dòng sai (unification)** (cơ sở 21 mục / 662 dòng + đợt U4 11 mục mới / 193 dòng — T6, T7, T15, T16, T41, T45, T47, T11, T12, T19, T20 đều là mục mới chưa tính trong chain; T54/T55 thêm 0 dòng; đối chiếu ROUTE-UNIFICATION.md trực tiếp lúc cuối đợt, sau khi U2b gộp 22/11 ~11:40)
