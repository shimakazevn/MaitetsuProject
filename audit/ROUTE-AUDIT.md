# Audit mật độ lỗi theo route — Maitetsu (translation_toml-2.zip)

Ngày audit: 2026-11-19. Nguồn: `/tmp/maitetsu2/translation_toml/` (227 file, giải nén từ
`~/workspace/user/files/translation_toml-2.zip`; bản Việt giống hệt 100% zip cũ).
Phương pháp: chỉ đếm trong section `[script]`, bỏ dòng comment `# JP:`, bỏ dòng trống.
Tổng dòng script (không trống): **93.153** — lệch 6 dòng so với con số 93.159 trong
REVIEW pilot, do cách đếm khác nhau, không đáng kể.

## Mật độ lỗi theo route (dấu phẩy kiểu máy dịch + "mình")

Pattern quét: `, (cơ|mà|chẳng|nữa|thôi|đâu|rồi|nhỉ)` và từ đứng riêng `mình`.
"Mình" đếm mọi nhân vật, không chỉ Soutetsu — đây là tín hiệu mật độ, không phải
kết luận từng dòng. Pattern dấu phẩy cũng có thể bắt trúng vài dấu phẩy đúng —
danh sách quét để sửa tay, không tự động thay.

| Route | File | Dòng | Dấu phẩy MT | "mình" | Tổng | /1000 dòng |
|---|---|---|---|---|---|---|
| 11_Other | 1 | 442 | 31 | 25 | 56 | **126,7** |
| 07_Nagi_Fukami | 28 | 11.446 | 428 | 587 | 1.015 | **88,7** |
| 08_Niiroku | 5 | 1.806 | 46 | 100 | 146 | **80,8** |
| 02_Hibiki | 37 | 15.291 | 454 | 632 | 1.086 | **71,0** |
| 05_Mayami | 12 | 4.706 | 141 | 180 | 321 | 68,2 |
| 04_Reina | 13 | 4.915 | 147 | 177 | 324 | 65,9 |
| 06_Kisaki | 13 | 5.248 | 156 | 179 | 335 | 63,8 |
| 03_Paulette | 37 | 14.334 | 391 | 507 | 898 | 62,6 |
| 00_Common | 16 | 6.278 | 169 | 223 | 392 | 62,4 |
| 09_Grand | 11 | 5.692 | 112 | 234 | 346 | 60,8 |
| 01_Hachiroku | 46 | 19.893 | 566 | 609 | 1.175 | 59,1 |
| 10_Chikuni | 8 | 3.329 | 90 | 94 | 184 | 55,3 |
| **Tổng** | **227** | **93.153** | **2.731** | **3.547** | **6.278** | **67,4** |

## Kết luận cho câu hỏi 5 trong REVIEW (route nào làm trước)

- **Tệ nhất trong các route lớn: 07_Nagi_Fukami** — mật độ cao nhất (88,7/1000),
  28 file / 11.446 dòng, 1.015 điểm cần soát. Ngoài ra "xuống sông" (từ thêm
  không có trong gốc, pilot phát hiện ở Common) tập trung ở đây: **10/16 lần
  toàn dự án** nằm trong Nagi_Fukami.
- **Đứng thứ hai: 02_Hibiki** — 71,0/1000, số điểm tuyệt đối lớn thứ hai (1.086),
  37 file / 15.291 dòng.
- **11_Other** mật độ cao nhất (126,7) nhưng chỉ 1 file / 442 dòng — nên soát
  kèm trong một đợt nhỏ, không đáng làm cả route riêng.
- **01_Hachiroku** có số điểm tuyệt đối lớn nhất (1.175) nhưng mật độ thấp nhất
  trong nhóm route lớn (59,1/1000) — làm sau Hibiki/Nagi_Fukami.
- **00_Common chưa xong:** pilot mới sửa file 01/16. Còn 15 file với 392 điểm
  quét (169 dấu phẩy MT + 223 "mình") — nếu Hieu muốn chốt tone trước thì
  làm nốt Common rồi mới sang route khác.

## Kiểm chứng lại câu hỏi 2 trong REVIEW (gloss của 帝鉄)

Đếm riêng trong thẻ gloss `%l...%l` và ngoài thẻ (lời thoại thường):

| Dạng | Trong gloss `%l` | Ngoài gloss (lời thoại) |
|---|---|---|
| 帝鉄 (giữ nguyên JP) | 60 | 0 |
| Đường sắt Hoàng gia | 53 | 160 |
| Teitetsu | 9 | 56 |

- Trong gloss: 60 / 53 / 9 — khớp gần đúng với REVIEW (57 / 50 / 7, cộng 2 chỗ
  "Đường sắt Hoàng gia (Teitetsu)" đếm trùng cả hai cột). Chênh lệch nhỏ do
  REVIEW có thể đã loại từ ghép như 帝鉄貨物.
- **Phát hiện mới:** ngoài gloss, "Đường sắt Hoàng gia" xuất hiện **160 lần**
  và "Teitetsu" **56 lần** trong lời thoại thường. Quyết định ở câu hỏi 2
  ảnh hưởng ~330 chỗ, không chỉ ~116 chỗ trong gloss — cần chuẩn hoá cả hai nơi.
- **Aircra:** 504 lần toàn dự án, dùng nhất quán — không cần động vào.
- "cậu bảo": chỉ 2 lần toàn dự án. "Hôm nay": 228 lần (gồm cả dùng đúng) —
  chỉ soát khi đối chiếu từng câu với gốc, không quét hàng loạt được.

## Hibiki 03_湯富院 (19/11/2026) — 374/434 sai (86,2%), nặng nhất từ trước tới nay
- Lệch nội dung 330, chưa dịch 44 (TOML VN==TW 44/44 — placeholder tiếng Trung, không có bản dịch để mất; 17 lấy lại bằng chuyển chỗ, 27 dịch mới), cụt câu 0, không chắc chắn 0.
- 120 cặp chuyển chỗ đã xác nhận (lần đọc đầu chỉ thấy 71 — rà soát lần 2 tìm thêm 49 cặp xa); không key-shift sạch (shift -5..+5: 0,59–0,62).
- Mikuro sai 34/34 (100%), Soutetsu 107/123, Hibiki 78/87, lời dẫn 133/148, Thị trưởng Yufuin 22/42 (ít sai nhất).
- 2158: JP 冥軍 vs TW 美軍 — Hieu đã chốt 19/11: 冥軍 = "Minh Quân" (quân Minh/netherworld), bản sửa trong audit dùng "Minh Quân" theo JP, không dùng "quân đội Mỹ" theo TW.
- Tổng 4 file đã audit: 1.061 dòng sai (133+255+299+374). File audit: audit-hibiki03-REVIEW.md (khối TOML parse 374/374), audit-hibiki03-wrong.json.
- Quyết định 19/11: 御一夜 = Ohitoyo — 7 bản sửa trong khối đã đổi từ "Ohimitera" sang "Ohitoyo" (đợt sửa 19/11).

## Hachiroku 13_夜の嵐 (19/11/2026) — 201/443 sai (45,4%), ngang Grand 01
- Lệch nội dung 199, chưa dịch 0, cụt câu 0, không chắc chắn 0. Thoại sai 110/246, lời dẫn sai 89/197. Hibiki 0/26 (duy nhất không sai dòng nào); Paulette 18/26, Mayami 11/12, Soutetsu 51/112, monologue 90/198.
- Không key-shift sạch (shift -5..+5: 0,753–0,777, tốt nhất ở 0). Heuristic chỉ báo 99/443 (22,3%).
- Cơ chế lỗi có thêm lớp mới: 168 cặp trùng lặp trong cùng file (167 dòng sai mang câu Việt của key khác; 2760 trùng với 2 key đúng); 32 dòng sai còn lại mang câu Việt từ chương trước — cả 32 câu đều có mặt trong `ハチロク12_再開発.txt.toml` (kiểm tra mẫu: 91 = bản dịch đúng của Hachiroku 12 key 3207) — lỗi tràn qua lại giữa các chương. 0/199 bản sửa lấy lại được từ trong file — bản dịch đúng gốc đã mất, phải dịch mới.
- TOML và CSV giống hệt nhau về nội dung (270 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào.
- Thuật ngữ: 術仙炭鉱 = "mỏ than Jutsusen" (theo file; audit 廃炭鉱 dùng "Jutsu-sen" — khác dấu gạch nối); 御一夜駅 = "ga Ohitoyo" (theo dòng đúng sẵn có), riêng thành phố ở 2873/2885 dùng "Ohimitera" theo docs — Quyết định 19/11: 御一夜 = Ohitoyo, 2 bản sửa đã đổi sang "Ohitoyo" (đợt sửa 19/11); 湯医 = "Yunoi" trong bản sửa (theo đề xuất Grand 01), trái với "Yui" ở 実りの秋 2102; コン = "Kuu" (theo file, dù phiên âm thường là "Kon").
- Tổng 5 file đã audit: 1.260 dòng sai (133+255+299+374+199). File audit: audit-hachiroku13-yoru-no-arashi-REVIEW.md (khối TOML parse 199/199), audit-hachiroku13-yoru-no-arashi-wrong.json.
- Hệ quả: nên audit Hachiroku 12 sau, vì cột Việt của nó có thể cũng bị xáo trộn ngược lại.

## Hachiroku 13_実りの秋 (19/11/2026) — 2/474 sai (0,4%), sạch nhất từ trước tới nay
- Lệch nội dung (sai nghĩa) 2, chưa dịch 0, cụt câu 0, không chắc chắn 0. Thoại sai 1/274, lời dẫn sai 1/200. Cả hai cùng một lỗi: 隆起 (mặt đất phình lên) dịch thành "sụt lún" (ngược nghĩa) — key 1721 (Soutetsu) và 2492 (monologue); các dòng khác trong file đều dịch đúng "phình lên" (1343, 1754, 1826, 1936, 2115, 3022).
- Không key-shift (shift 0 khớp 0,998); heuristic báo 1/474. Không trùng lặp sai, không lệch vị trí, không câu Việt từ chương khác. TOML và CSV giống hệt nhau về nội dung (280 dòng khác chỉ ở `\n`/khoảng trắng).
- Thuật ngữ trong file (ghi nhận, chưa phải quyết định): 御一夜鉄道 = "Đường sắt Ohito", 御一夜駅 = "ga suối nước nóng Ohitoyo", 湯医 = "Yui" (2102) — trái với "Yunoi" ở 夜の嵐; 帝鉄 = "Teitetsu" dạng ngắn (1751, 1980). Furigana ở 2102: 御一夜 = おひとよ ("Ohitoyo") — bằng chứng mới cho quyết định 御一夜 đang chờ Hieu.
- Hai file cùng chương 13 trái ngược nhau hoàn toàn (44,9% vs 0,4%) — không thể đoán chất lượng file chưa audit từ file bên cạnh.
- Tổng 6 file đã audit: 1.262 dòng sai (133+255+299+374+199+2). File audit: audit-hachiroku13-minori-no-aki-REVIEW.md (khối TOML parse 2/2), audit-hachiroku13-minori-no-aki-wrong.json.

## Nagi_Fukami 08a_凪エピローグ (19/11/2026) — 20/462 sai (4,3%), 1 dòng chưa chắc chắn; sạch thứ hai từ trước tới nay
- Lệch nội dung 0, chưa dịch 0, cụt câu 0, không chắc chắn 1 (2426, JP bỏ lửng — TW hoàn thiện thành "cũng chẳng sao", VN cũ hoàn thiện mơ hồ thành "vẫn mong như vậy"; cần Hieu chọn). 20 dòng sai gồm: sai nghĩa 5 (1191, 1754, 1811, 1962, 1991), câu gãy 1 (1222), xưng hô độc thoại không nhất quán 14 (13 dòng Fukami xưng "tôi" → chuẩn hoá "mình" theo 43/49 dòng đúng trong file; 1 dòng Soutetsu 2879 xưng "mình" → "tôi").
- Thoại sai 5/259 (1,9%), lời dẫn sai 15/203 (7,4%). Theo người nói: monologue 15, Fukami 2, Soutetsu 2, Nagi 1; Munakata, Hachiroku, Hibiki, Paulette, Reina, Mayami, Kisaki, Nakamura, Trọng tài, Loa phát thanh: 0.
- **File đầu tiên không có một dòng lệch vị trí nào:** không trùng lặp sai (5 cặp Việt trùng nhau đều là câu cảm thán ngắn có JP giống hệt/na ná), không dòng mồ côi, không tràn chương (cả 20 câu Việt sai chỉ xuất hiện ở đúng key của chúng trong toàn dự án; kiểm tra tên nhân vật 0 nghi ngờ). **Heuristic thoại/dẫn bắt được 0/462 (0%)** — mọi lỗi đều cùng loại hoặc ở mức đại từ, heuristic mù hoàn toàn với file này; bằng chứng rõ nhất heuristic chỉ là giới hạn dưới.
- Không có key-shift sạch (shift test không kết luận được do key thưa + thoại/dẫn theo cụm dài; không có bằng chứng lệch đều). TOML và CSV giống hệt nhau về nội dung (268 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào. 冥軍 / 帝鉄 / 湯医 / コン / エアクラ / 砂撒 không xuất hiện.
- `[selections]` có tiêu đề nhưng rỗng (0 mục) — không có gì để kiểm tra. Quan sát thêm (không tính lỗi): 5 dòng mang thẻ `%l` cho 機関士 (1207, 1542, 1750, 1804, 2568) mà JP gốc không có thẻ — bản dịch vẫn đúng.
- Thuật ngữ: 御一夜鉄道 = "Đường sắt Ohito" trong 3 dòng đúng sẵn có (1888, 2695, 2840) — Quyết định 19/11: 御一夜 = Ohitoyo (3 dòng đúng vẫn dùng "Ohito", chờ đợt thống nhất sau). Fukami độc thoại xưng "mình" (43/49 dòng đúng) — chờ Hieu chốt trước khi áp dụng ngược.
- Tổng 7 file đã audit: 1.282 dòng sai (133+255+299+374+199+2+20). File audit: audit-nagifukami08a-REVIEW.md (khối TOML parse 20/20, dòng 2426 không nằm trong khối), audit-nagifukami08a-wrong.json (21 mục: 20 sai + 1 chưa chắc chắn).
- Hệ quả: độ xáo trộn không đồng đều giữa các file — không thể đoán độ sạch của file chưa audit từ tên chương hay heuristic; vẫn phải đọc hết từng dòng. Tiếp theo: Hachiroku 12 (nghi tràn chương từ audit 夜の嵐).

## Hachiroku 12_ムナカタ来訪 (19/11/2026) — 44/513 sai (8,6%), 2 nhóm chưa chắc chắn; gồm 31 thẻ gloss 機関士 gỡ theo quyết định 19/11
- Lệch nội dung 3 (1567 mảnh câu chuyển chỗ từ 1718 trong cùng file; 2824 phủ định ngược nghĩa; 2914 犬走り dịch nghĩa đen thành "lối đi dành cho chó"), chưa dịch 0, cụt câu 0, không chắc chắn 2 nhóm (2811/2528: JP 小畑 vs TW 大畑, VN "Okoba" theo TW; 2976: 冥国 — VN để nguyên "Meikoku", lựa chọn "Mỹ" theo TW vs "Minh Quốc" theo tiền lệ 冥軍 = "Minh Quân"). 9 lỗi nhỏ còn lại: dấu câu/thẻ 8 (1687, 1697, 2169, 2182 thừa 「 mở; 2899, 2538 mất dấu mở 『; 2025 thẻ `%l` hỏng; 2513 lời dẫn bọc ngoặc thoại), xưng hô 1 (2691 "ông Munakata" trái quy ước "chú Munakata").
- Thoại sai 6/328, lời dẫn sai 6/185. Theo người nói: monologue 6, Olivy 1, Hachiroku 2, Soutetsu 2, Munakata 1; Paulette, Reina, Kisaki 0.
- **Không tràn ngược:** 0 câu Việt dài trùng với 夜の嵐; 13 dòng trùng file khác đều là câu ngắn thông dụng, đều đúng. Chiều tràn chỉ đi một chiều, từ Hachiroku 12 sang 夜の嵐.
- Không key-shift sạch (lệch duy nhất 1567←1718 là +151, một lỗi dán nhầm đơn lẻ). Heuristic chỉ bắt được 1/513 (2513, lỗi thật). TOML và CSV giống hệt nhau về nội dung (290 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào.
- Quan sát hệ thống (không tính lỗi): 31 dòng gắn thẻ gloss `\x%l機関士;#00ffc040;lái tàu%l;#;` trước tên Munakata dù JP không có 機関士 (1097, 1103, 1539, 2480, 2498, 2565, 2634, 2637, 2693, 2695, 2699, 2701, 2705, 2707, 2713, 2715, 2717, 2720, 2722, 2725, 2726, 2730, 2731, 2805, 2830, 2891, 2962, 2966, 2975, 2979, 2997) — Hieu quyết gỡ hay giữ.
- Thuật ngữ: 帝鉄 = "Teitetsu" dạng ngắn cả 6 lần (2252, 1848, 2875, 2710, 2025, 2015); 御一夜 dùng lẫn ba dạng Ohito ~14 / Ohimitera 12 / Ohitoyo 2 (2191, 2049); 御一夜市 = "thành phố Ohimitera" (1900, 1847); Quyết định 19/11: 御一夜 = Ohitoyo — bản sửa 2025 đã đổi "Ohimitera - Hayato" → "Ohitoyo - Hayato" (đợt sửa 19/11), các dòng đúng dùng lẫn 3 dạng vẫn chờ đợt thống nhất sau; 術仙車両工場 = "nhà máy chế tạo toa xe Jutsu-sen" (1525, có gạch nối). Soutetsu độc thoại xưng "Tôi" (40 dòng; 0 dòng xưng "mình" ở vị trí chủ ngữ).
- Tổng 8 file đã audit: 1.294 dòng sai (133+255+299+374+199+2+20+12). File audit: audit-hachiroku12-munakata-REVIEW.md (khối TOML parse 12/12; 3 key chưa chắc chắn không nằm trong khối), audit-hachiroku12-munakata-wrong.json (15 mục: 12 sai + 3 chưa chắc chắn).

## Hachiroku 12_再開発 (19/11/2026) — 19/427 sai (4,4%), 0 dòng chưa chắc chắn; nguồn gốc của lỗi tràn chương ở 夜の嵐
- Lệch nội dung 8 (3195, 3021: 整備体 → "thân chính"; 3285: 運転ボディ → "thân chính" — hai loại thân máy bị gộp một tên; 3054: 大詔 → "Đại Chiếu" thay vì "Taisho"; 2225: 専用乗車券 → "Vé chuyên cơ"; 2258, 2381, 1699: 持株会社 → "công ty cổ phần" thay vì "công ty holding"), chưa dịch 0, cụt câu 0, không chắc chắn 0. 11 lỗi nhỏ còn lại: nhất quán thuật ngữ 7 (2016, 2280, 2098, 3070, 2500, 2515, 2508: "Jutsusen" → "Jutsu-sen"), dấu câu 3 (2103, 2537: mất tiếng hít っ; 1660: mất ngoặc ngoài 「」), xưng hô độc thoại 1 (3290: "mình" → "Tôi").
- Thoại sai 13/249, lời dẫn sai 6/178. Theo người nói: monologue 6, Soutetsu 5, Hachiroku 4, Kisaki 2, Paulette 2; Hibiki, Nagi, Reina, Fukami 0.
- **File này là NGUỒN của 32 dòng tràn sang 夜の嵐, không phải nạn nhân:** 32 cặp đã xác nhận (3207↔夜の嵐 91, 2281↔1182, và 30 cặp còn lại — xem review); cả 32 câu đều dịch đúng JP tại key gốc ở đây. Không tràn ngược vào file này. Trong file: 0 cặp chuyển chỗ.
- Không key-shift (0 dòng lệch vị trí). Heuristic chỉ bắt được 1/427 (1660, lỗi thật); báo 1 VN==TW giả (1662 là 「…………」). TOML và CSV giống hệt nhau về nội dung (237 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào.
- Thuật ngữ: 御一夜 → "Ohitoyo" nhất quán 8/8 dòng (2926, 2488, 2346, 2345, 1672, 2471, 2316, 2508) — bằng chứng mạnh nhất cho "Ohitoyo" (furigana おひとよ); 湯医 → "Yui" cả 3 chỗ (2508, 2464, 2853) — trái với "Yunoi" ở Grand 01/夜の嵐, vẫn chờ Hieu; 術仙炭鉱 chuẩn hoá "Jutsu-sen"; 整備体 = "thân bảo trì", 運転ボディ = "thân vận hành"; コン không xuất hiện (1650 là コンマ "phẩy 8", dịch đúng). Soutetsu độc thoại xưng "Tôi" (75 dòng; chỉ 3290 xưng "mình" ở vị trí chủ ngữ).
- Cả chương 12 đều sạch (2,3% + 4,4%) — trái hẳn chương 13 (44,9% vs 0,4%): không thể đoán độ sạch từ tên chương hay file bên cạnh.
- Tổng 9 file đã audit: 1.313 dòng sai (133+255+299+374+199+2+20+12+19). File audit: audit-hachiroku12-sai-kaihatsu-REVIEW.md (khối TOML parse 19/19), audit-hachiroku12-sai-kaihatsu-wrong.json.
## Paulette 04_ヒヤリング (19/11/2026) — 7/395 sai (1,8%), 1 dòng chưa chắc chắn; sạch thứ hai từ trước tới nay
- Sai nghĩa 4 (1360 lệch thứ tự từ theo TW — JP "Thích" trước, VN "Không" trước; 1607 汚名返上 → "rửa sạch cái danh tiếng đó" thay vì "lấy lại danh dự"; 2567 dấu phẩy kiểu MT làm câu gãy; 1132 — đã chốt 19/11: độc thoại Soutetsu, chủ ngữ là tình trạng chung, "Vẫn chưa được." thay vì "Tôi không hề."), xưng hô độc thoại 4 (2580, 2584, 2586, 2590: Soutetsu "mình" → "Tôi" trong suy nghĩ ngoặc, trái quy ước file + docs), chưa dịch 0, cụt câu 0, không chắc chắn 0.
- Thoại sai 2/207, lời dẫn sai 5/188. Theo người nói: monologue 5, Paulette 2; Soutetsu thoại, Hibiki, Fukami, Miyamoto, Hachiroku, Nagi, Mayami, Reina 0.
- **File này là NGUỒN của lỗi tràn sang stove, không phải nạn nhân:** 90 dòng Việt đúng ở đây bị copy sang file stove (xem dưới); không tràn ngược vào file này. Trong file: 0 cặp chuyển chỗ, 0 dòng mồ côi (2 cặp trùng 「Ồ.」 1463/1464, 「Ừm.」 1467/1494 đều là cảm thán ngắn đúng).
- Không key-shift sạch (shift test −5..+5 tốt nhất ở shift 0, 394/395 = 0,997). Heuristic chỉ báo 1 dòng 2125 là dương tính giả (lời dẫn có trích dẫn lồng), bắt được 0/7 lỗi thật. TOML và CSV giống hệt nhau về nội dung (0 dòng khác nội dung thực). Không có dòng CSV trống nào; VN==TW chỉ 1160 là 「……」.
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Không có lệch thẻ `%l` nào. Thuật ngữ: 御一夜 "Ohimitera" 5 / "Ohito" 1 ở các dòng đúng — Quyết định 19/11: 御一夜 = Ohitoyo (các dòng đúng vẫn dùng "Ohimitera"/"Ohito", chờ đợt thống nhất sau); 湯医 → "Yui" (2023, 2532) — trái "Yunoi" ở Grand 01/Hibiki 03, vẫn chờ Hieu; 帝鉄 không xuất hiện; エアクラ = "Aircra".
- Tổng 10 file đã audit: 1.321 dòng sai (133+255+299+374+199+2+20+12+19+8). File audit: audit-paulette04-hearing-REVIEW.md (khối TOML parse 8/8), audit-paulette04-hearing-wrong.json (8 mục).

## Paulette 04_鳴呼いきストーブ列車 (19/11/2026) — 101/457 sai (22,1%), 0 dòng chưa chắc chắn; file nặng thứ sáu từ trước tới nay
- Lệch vị trí 99 (90 copy từ file hearing kề bên + 1 dòng nguồn không xác định 2252 "Anh Soutetsu." — câu ngắn thông dụng ở 12 file + 7 mảnh vỡ mồ côi 1816, 1887, 1922, 2014, 2020, 2518, 2536 + 1 trùng lặp nội bộ 2140←2104), lỗi gloss 2 (2076, 2642: タブレット → "Thẻ bảng" thay vì "máy tính bảng"), chưa dịch 0, cụt câu 0, không chắc chắn 0. 0/101 bản sửa khôi phục được trong file (không có cặp chuyển chỗ nội bộ) — mọi dòng sai đều dịch mới từ JP/TW.
- Lời dẫn sai 35/144, thoại sai 66/313. Theo người nói: monologue 35, Soutetsu 24, Hikari 21, Paulette 16, Reina 3, bà cụ 2; Tourist Association, Passenger C/D, Conductor, Station staff 0. Lỗi rải đều cả file (25 + 22 + 18 + 26 + 10 theo từng đoạn key).
- **Tràn chương thứ hai trong dự án, cùng mô hình Hachiroku 12 → 夜の嵐 nhưng lớn hơn gần gấp ba:** 90 dòng Việt đúng của hearing bị copy sang đây, một chiều (hearing sạch 1,8%, không nhiễm ngược). Hai file cùng một chương 04 mà một file sạch một file nặng — không thể đoán độ sạch từ tên chương hay file bên cạnh.
- Không key-shift sạch (shift test −5..+5 tốt nhất ở shift 0, 409/457 = 0,895). Heuristic báo 48 dòng, bắt tối đa 48/101, sót ít nhất 53 dòng cùng loại/gloss/mảnh vỡ. TOML và CSV giống hệt nhau về nội dung (0 dòng khác nội dung thực). Không có dòng CSV trống nào; VN==TW 0.
- Quan sát hệ thống (không tính lỗi): 6 dòng đúng gắn thẻ gloss `%l` mà JP không có (1780, 1811, 2050, 2076, 2698, 2816 — 2028 đã sai nên không tính) — Hieu quyết gỡ hay giữ (riêng 2076 giữ thẻ, chỉ sửa gloss). Không có dòng nào VN làm mất thẻ `%l` của JP.
- Thuật ngữ: 御一夜 → "Ohitoyo" trong các bản sửa (Quyết định 19/11, đợt sửa 19/11 đổi 4 dòng từ "Ohimitera"; file dùng lẫn "Ohito" 2604 / "Ohimitera" 2809 ở dòng đúng, chờ đợt thống nhất sau); 湯煙鉄道 = "Đường sắt Yukemuri"; 術仙炭鉱 = "mỏ than Jutsu-sen"; 運転台 = "buồng lái"; 駿袋鉄道 → "Đường sắt Suntai" theo ruby JP すんたい (TW viết 駿遠 — cần Hieu xác nhận nếu muốn theo TW).
- Tổng 11 file đã audit: 1.421 dòng sai (133+255+299+374+199+2+20+12+19+7+101). File audit: audit-paulette04-stove-train-REVIEW.md (khối TOML parse 101/101), audit-paulette04-stove-train-wrong.json (101 mục).
- Tiếp theo: Paulette 05, Grand Rewrite 04, hoặc các file còn lại theo thứ tự nặng trước (danh sách heuristic).

## Paulette 05_whatsentertainment (19/11/2026) — 10/362 sai (2,8%), 0 dòng chưa chắc chắn; file sạch thứ tư từ trước tới nay
- Xưng hô 4 (1390, 1418, 2034, 2286: Soutetsu "mình" → "Tôi" — cùng mẫu lỗi ở pilot và hearing), sai nghĩa 2 (1296, 1952: "Anh Miyamoto" — TW 宮本女士 xác nhận là nữ, sửa thành "Cô Miyamoto"; 1952 thêm lỗi "——bất thường" cho 非常), lỗi nhỏ 2 (1346, 1534: dấu "Ạ." đứng riêng câu, Fukami), thuật ngữ 2 (1490, 1903: "Ohimitera" → "Ohitoyo" theo quyết định 19/11). Lệch vị trí 0, chưa dịch 0, cụt câu 0, không chắc chắn 0.
- Thoại sai 6/202, lời dẫn sai 4/160. Theo người nói: monologue 4, Paulette 2, Fukami 2, Soutetsu 2; Hachiroku, Reina, Nagi 0.
- Không có lệch vị trí: 0 dòng mồ côi, 0 cặp chuyển chỗ, 0 tràn chương. 2 cặp Việt trùng nhau đều đúng: 「Hửm?」 1313/1336 và (Keng! Keng! Keng! Keng!) 2279/2282 (cùng tiếng búa đập).
- Không key-shift sạch (shift test −5..+5 tốt nhất ở shift 0, 362/362 = 1,000). Heuristic báo 0 dòng, bắt được 0/10 lỗi thật — toàn bộ lỗi cùng loại hoặc ở mức từ/câu. TOML và CSV giống hệt nhau về nội dung (210 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW 0.
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Không có lệch thẻ `%l` nào. Thuật ngữ: 御一夜 → "Ohitoyo" trong các bản sửa (1490, 1903) — quyết định 19/11; đây là 2 dòng duy nhất có 御一夜 trong file, sau khi sửa file không còn "Ohimitera" nào; エアクラ = "Aircra" (1974, đúng sẵn có); 湯医, 帝鉄, 冥国, 冥軍, 小畑, 大畑 không xuất hiện.
- Tổng 12 file đã audit: 1.431 dòng sai (133+255+299+374+199+2+20+12+19+7+101+10). File audit: audit-paulette05-whatsentertainment-REVIEW.md (khối TOML parse 10/10), audit-paulette05-whatsentertainment-wrong.json (10 mục).

## Paulette 05_鳴呼の町 (19/11/2026) — 23/458 sai (5,0%), 1 dòng chưa chắc chắn; lệch vị trí theo chuỗi xoay vòng nội bộ (mới)
- Lệch vị trí 11 (3 chuỗi xoay vòng nội bộ: chuỗi hố tuyết 1264←2518, 2518←2375, 2375←2187, 2187 dịch mới; chuỗi tai nạn thứ cấp 2558←2568, 2568←1264; chuỗi lời nói 1969←2699, 2699←2697, 2697←2784, 2784←1245, 1245 dịch mới), sai nghĩa 5 (1700 thêm "Mẹ ơi" sai người nghe — Hikari đang nói với papa; 1726 かまくま → "Gấu tuyết" thay vì "Lều tuyết" theo TW 雪洞; 2010, 2136, 2177 水切りかご → "rổ vớt nước" thay vì "rổ ráo nước" theo TW 瀝水籃), thuật ngữ 5 (1625, 2112, 2140, 2512, 2640: "Ohimitera" → "Ohitoyo" theo quyết định 19/11), xưng hô 2 (1660, 2593: Soutetsu "mình" → "Tôi"). Chưa dịch 0, cụt câu 0, không chắc chắn 1 (1992, JP いただくのー！ — VN "Xin được chỉ giáo~!" đi theo TW 教我們吧 nhưng いただく không có nghĩa "dạy"; cần Hieu chơi tới đoạn đó).
- Thoại sai 12/303, lời dẫn sai 11/155. Theo người nói: monologue 11, Soutetsu 6, Paulette 3, Hikari 3; Reina, bà cụ, nhân viên cửa hàng 0. Lỗi tập trung ở cảnh trượt chân xuống hố tuyết (key 1245–2784).
- **Cơ chế mới: xoay vòng nội bộ, không tràn chương.** Toàn bộ 11 dòng lệch đều là bản dịch đúng của một key khác trong cùng file; 9/11 bản sửa khôi phục được từ trong file, chỉ 2 dòng dịch mới (1245, 2187). 2 trùng lặp nội bộ: "A!!" 1854/1969 và "Đợi đã! Đừng động đậy…" 2091/2558 (chỉ key đầu đúng). 0 tràn chương — 26 dòng Việt trùng file khác đều là câu ngắn thông dụng đúng với JP của chính chúng.
- Không key-shift sạch (shift test −5..+5 tốt nhất ở shift 0, 453/458 = 0,989). Heuristic báo 5 dòng (1264, 2187, 2518, 2558, 2699 — đều là lỗi thật), bắt được 5/23. TOML và CSV giống hệt nhau về nội dung (217 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW 0.
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Không có lệch thẻ `%l` nào. Thuật ngữ: 御一夜 → "Ohitoyo" trong các bản sửa (5 dòng, quyết định 19/11); 水切りかご = "rổ ráo nước" (ghi nhận để thống nhất về sau); かまくら = "lều tuyết", かまくま = "gấu tuyết" chỉ khi Hikari nói sai (1633); 湯医, 帝鉄, 冥国, 冥軍, 小畑, 大畑 không xuất hiện; コン ở 2540 là コンビニ, không phải cáo.
- Tổng 13 file đã audit: 1.454 dòng sai (133+255+299+374+199+2+20+12+19+7+101+10+23). File audit: audit-paulette05-narukonotown-REVIEW.md (khối TOML parse 23/23; dòng 1992 không nằm trong khối), audit-paulette05-narukonotown-wrong.json (24 mục: 23 sai + 1 chưa chắc chắn).
- Tiếp theo: Grand Rewrite 04_ポーレット (489 dòng), hoặc các file còn lại theo thứ tự nặng trước.

## Grand Rewrite 04_ポーレット (19/11/2026) — 19/489 sai (3,9%), 0 dòng chưa chắc chắn; file sạch, không lệch vị trí
- Thuật ngữ 14 (御一夜 → "Ohitoyo" 10 dòng: 1705, 1919, 1959, 1962, 2055, 2268, 2292, 2662, 3063, 3103 — 8 "Ohimitera" + 2 "Ohito"; 術仙 → "Jutsu-sen" 4 dòng: 1690, 2174, 2220, 2923 — file viết thiếu "t" thành "Jussen"), sai nghĩa 3 (1862 Paulette "Nhờ em nhé" sai người xưng hô → "Nhờ anh nhé"; 1864 よかった → "Thích quá" thay vì "Tốt quá"; 2135 thêm tác nhân "Navi" không có trong JP — bản sửa dịch sát JP theo quy tắc tin JP, bỏ cả "Navi" lẫn phần TW thêm vào), xưng hô 2 (2733, 2770: Soutetsu độc thoại "mình" → "Tôi"). Lệch vị trí 0, chưa dịch 0, cụt câu 0, không chắc chắn 0.
- Thoại sai 13/294, lời dẫn sai 6/195. Theo người nói: Paulette 8, monologue 6, Soutetsu 5; Michiko, Reina, Navi 0. Lỗi rải đều cả file (2 + 5 + 4 + 4 + 4 theo từng đoạn key).
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + 5 trùng lặp nội bộ đều đúng + chỉ mục Việt toàn dự án (81.213 mục, chỉ khớp 10 câu ngắn thông dụng đúng với JP của chính chúng). Heuristic báo 0 dòng, bắt được 0/19.
- Không key-shift sạch (shift test −5..+5 tốt nhất ở shift 0). TOML và CSV giống hệt nhau về nội dung (308 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW 0.
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Không có lệch thẻ `%l` nào. Thuật ngữ: 御一夜 → "Ohitoyo" trong các bản sửa (quyết định 19/11; sau khi sửa file không còn "Ohimitera"/"Ohito" nào); 術仙炭鉱 = "mỏ than Jutsu-sen"; 湯医 → "Yui" ở cả 12 chỗ — quyết định Yui/Yunoi vẫn chờ Hieu nên giữ nguyên; 閉塞 = "đóng đường" đúng theo glossary team (translation_guidelines.md:51), không tính lỗi; 共感 2112/2114 dịch "đồng cảm" là đúng (đồng cảm giữa người với người, không phải năng lực Railord "cộng cảm"); 帝鉄, 冥国, 冥軍, 小畑, 大畑 không xuất hiện; コン ở 1906 là コンセプト, không phải cáo.
- Lưu ý: cùng tên file còn có bản sao y hệt trong `09_Grand/` (cùng md5 469b3da460c27dbca329c397cc553e2a) — khi áp fix cần áp cho cả hai thư mục.
- Tổng 14 file đã audit: 1.473 dòng sai (133+255+299+374+199+2+20+12+19+7+101+10+23+19). File audit: audit-grand04-paulette-REVIEW.md (khối TOML parse 19/19), audit-grand04-paulette-wrong.json (19 mục).
- Tiếp theo: các file còn lại theo thứ tự nặng trước (danh sách heuristic).

## Paulette 06_おひとよマイントレジャー (19/11/2026) — 25/367 sai (6,8%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, nặng về thuật ngữ
- Thuật ngữ 16 (御一夜 → "Ohitoyo" 11 dòng: 1464, 1851, 1964, 1980, 1983, 2026, 2148, 2182, 2186, 2210, 2415 — gồm 4 lần tên cơ sở "Ohitoyo Mine Treasure"; 術仙 → "Jutsu-sen" 6 dòng: 1464, 1765, 1974, 2155, 2704, 2753 — file viết thiếu "t" thành "Jussen"; 1464 mang cả hai lỗi), xưng hô 4 (1718: Paulette "chị nghĩ" → "tôi nghĩ" khi nói với Kisaki; 1873, 1879: Soutetsu "anh" → "tôi" khi nói với nhóm/Kisaki, không phải Hibiki; 2539: Soutetsu độc thoại "anh" → "tôi"), sai nghĩa 4 (2369, 2836: chơi chữ "Treasure **to** Leisure" bị dịch thành "với"/"và" — TW giữ nguyên "ｔｏ　Ｌｅｉｓｕｒｅ"; 2089: Kisaki "các người" → "mọi người", trái giọng biết ơn; 2533: 思いかけ "chợt nghĩ tới" bị dịch thành "định nói vậy thì" làm câu gãy nghĩa), lỗi nhỏ 1 (1934: Fukami ". ạ" rơi lẻ sau dấu chấm). Lệch vị trí 0, chưa dịch 0, cụt câu 0, không chắc chắn 0. Trừ 16 dòng thuật ngữ, file chỉ còn 9 lỗi thực chất (2,5%).
- Thoại sai 18/212, lời dẫn sai 7/155. Theo người nói: monologue 7, Soutetsu 6, Kisaki 4, Hibiki 4, Paulette 3, Fukami 1; Reina, Nagi, Hachiroku, Manami 0. Lỗi rải đều cả file (12 + 8 + 5 theo từng đoạn key).
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 trùng lặp nội bộ sai:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục). Heuristic báo 2 dòng (2369, 2711): 2369 là lỗi thật nhưng vì lý do khác (dấu ngoặc, không phải chơi chữ); 2711 là dương tính giả (trích dẫn lồng dùng "..."). Heuristic bắt được 1/25 theo dòng, 0/25 theo đúng lý do.
- Không key-shift sạch (shift test −2..+2 tốt nhất ở shift 0, 365/367 = 0,995). TOML và CSV giống hệt nhau về nội dung (229 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW chỉ 1462 là 「…………」.
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Không có lệch thẻ `%l` nào. Thuật ngữ: 御一夜 → "Ohitoyo" trong các bản sửa (quyết định 19/11; sau khi sửa file không còn "Ohimitera" nào); 術仙炭鉱 = "mỏ than Jutsu-sen"; エアクラ = "Aircra" (1903, 1964, 2753); レイルロオド = "Railord" (1718, 1835); 帝鉄, 湯医, 冥国, 冥軍, 小畑, 大畑, コン không xuất hiện. Không có bản sao file này ở thư mục khác.
- Câu hỏi mở: Soutetsu gọi Paulette "cô" (2047, ngữ cảnh công việc) trong khi ở file tuyết cùng chương 06 gọi "em" — cần Hieu chốt phân biệt theo ngữ cảnh hay thống nhất một cách.
- Tổng 15 file đã audit: 1.498 dòng sai (133+255+299+374+199+2+20+12+19+7+101+10+23+19+25). File audit: audit-paulette06-ohitoyo-treasure-REVIEW.md (khối TOML parse 25/25), audit-paulette06-ohitoyo-treasure-wrong.json (25 mục).

## Paulette 06_雪の宿 (19/11/2026) — 14/432 sai (3,2%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, nặng về xưng hô
- Xưng hô 8 (Soutetsu tự xưng "anh" với Paulette 5 dòng: 1854, 1954, 2048, 2070, 2132 — file dùng cả "tôi" (8 chỗ) lẫn "anh" (5 chỗ) với cùng người nghe nên "anh" là không nhất quán; 1331: Hikari gọi ba mình là "cậu" → "ba" (Soutetsu thuật lại tâm trạng con gái); 1879: Paulette gọi con gái mình là "bạn ấy" → "con bé" (kèm "Thấy chưa?" → "Nè?"); 1997: Paulette tự xưng "chị" → "em" khi nói về Reina với Soutetsu), sai nghĩa 3 (1736: Paulette "anh cũng muốn" → "em muốn" — gán mong muốn sang Soutetsu; 2158, 2159: 端的 → "Thẳng thắn" thay vì "Ngắn gọn" — chính câu giải nghĩa trong dòng và TW 簡而言之 đều chỉ nghĩa đúng), lỗi nhỏ 3 (1835: mất tiếng hít っ → "Á!!!"; 1846: 「ああ――」 hai あ dịch thành "A――" một A → "Aa――"; 2672: độc thoại Soutetsu "để ba dạy cho con nhé" → "tôi sẽ dạy cho con bé"). Lệch vị trí 0, chưa dịch 0, cụt câu 0, không chắc chắn 0.
- Thoại sai 13/273, lời dẫn sai 1/159. Theo người nói: Soutetsu 8, Paulette 3, Hikari 2, monologue 1; Reina, nhân viên phục vụ 0. Lỗi rải đều cả file (8 + 5 + 1 theo từng đoạn key).
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục). 2 cặp trùng lặp nội bộ: "A――" 1827/1846 (chỉ 1827 đúng); "（Tõm）" 2854/2859 (JP ちゃぷっ/ちゃぽん gần như giống nhau, "Tõm" hợp lý cho cả hai — không tính lỗi). Heuristic báo 0 dòng, bắt được 0/14.
- Không key-shift sạch (shift 0 khớp hoàn hảo 432/432). TOML và CSV giống hệt nhau về nội dung (250 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW 0.
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Thẻ `%l`: 1 dòng VN thêm thẻ (2045, thêm gloss Aircra — chữ hiển thị đúng, chỉ ghi nhận quan sát theo tiền lệ Nagi 08a/stove). Thuật ngữ: 共感 = "cộng cảm" khi là năng lực Railord (1887, 2035, 2427 — khác với "đồng cảm" giữa người với người ở Grand 04); 端的 = "Ngắn gọn" (thuật ngữ mới ghi nhận); レイルロオド = "Railord" (2049, 2196); エアクラ = "Aircra" (2045); 日ノ本 = "Hinomoto"; 鳴呼 = "Naruko"; 御一夜, 術仙, 帝鉄, 湯医, 冥国, 冥軍, 小畑, 大畑, コン không xuất hiện. Không có bản sao file này ở thư mục khác.
- Hai file cùng chương 06 trái ngược nhau về bản chất lỗi: treasure nặng về thuật ngữ (16/25), tuyết nặng về xưng hô (8/14) — không thể đoán loại lỗi từ file bên cạnh.
- Tổng 16 file đã audit: 1.512 dòng sai (133+255+299+374+199+2+20+12+19+7+101+10+23+19+25+14). File audit: audit-paulette06-snow-inn-REVIEW.md (khối TOML parse 14/14), audit-paulette06-snow-inn-wrong.json (14 mục).

## Paulette 07_うさぎ (19/11/2026) — 13/463 sai (2,8%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi rải rác ở xưng hô/sai nghĩa
- Xưng hô 6 (Soutetsu tự xưng "anh" 4 dòng thoại: 1548, 1884, 1887, 2096 + "Mình" 1690; độc thoại "mình" 2536 — file dùng "Tôi" 57/64 chỗ trong lời dẫn và chỉ 1 lần "tôi" trong thoại ở 1876), sai nghĩa 4 (1604, 1605: Hikari 4 tuổi tự xưng "chị" → "Hikari"; 1841: bịa thêm "đang gọi con kìa" — JP chỉ là câu bỏ lửng; 2611: "lòng họ" → "lòng mẹ" theo TW), thuật ngữ 2 (2115, 2380: Ohimitera → Ohitoyo), lỗi nhỏ 1 (2776: thừa 「」 quanh SFX (Cộc)).
- Thoại sai 9/292, lời dẫn sai 4/171. Theo người nói: Soutetsu 6, lời dẫn 4, Hikari 2, bà mẹ trẻ 1; Paulette, Reina, em bé 0. Lỗi rải đều cả file (5 + 4 + 4 theo từng đoạn key).
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 trùng lặp nội bộ sai:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục). Heuristic báo 2 dòng (2590 dương tính giả — lời dẫn trích lời nói; 2776 lỗi thật nhưng là lỗi nhỏ): bắt được 1/13 theo dòng, 0/13 theo đúng lý do.
- Không key-shift sạch (shift 0 khớp 461/463 = 0,996; shift +3/+4 đạt 1,000 chỉ vì key thưa). TOML và CSV giống hệt nhau về nội dung (218 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW 0.
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Thẻ `%l`: 4 dòng có thẻ, không dòng nào lệch. Thuật ngữ: 御一夜 → "Ohitoyo" (file đã có sẵn 1 "Ohitoyo" đúng ở 1907); 術仙炭鉱 = "mỏ than Jutsu-sen"; 帝鉄, 湯医, 冥国, 冥軍, 小畑, 大畑, コン không xuất hiện. Không có bản sao file này ở thư mục khác.
- Tổng 17 file đã audit: 1.525 dòng sai (133+255+299+374+199+2+20+12+19+7+101+10+23+19+25+14+13). File audit: audit-paulette07-usagi-REVIEW.md (khối TOML parse 13/13), audit-paulette07-usagi-wrong.json (13 mục).

## Paulette 07_支線 (19/11/2026) — 25/358 sai (7,0%), 0 dòng chưa chắc chắn; file sạch về cấu trúc nhưng nặng về xưng hô hệ thống
- Xưng hô 17 (Soutetsu tự xưng "anh" 17/17 lần trong thoại, 0 lần "tôi" — cách dịch hệ thống trái docs locations §2.1; 1963 "bọn anh" → "bọn tôi"; "mình" trong mệnh đề phụ giữ nguyên theo tiền lệ Hachiroku 12), thuật ngữ 8 (Ohimitera → Ohitoyo 8 dòng: 1249, 1696, 1781, 1856, 1942, 1952, 2311, 2366 — 1952 mang cả hai lỗi; 1664: 整備体 "thân chính" → "thân bảo trì", đề xuất chưa chốt).
- Thoại sai 23/207, lời dẫn sai 2/151. Theo người nói: Soutetsu 18, Reina 2, Minokasa 2, Paulette 1, lời dẫn 2; Nagi 0. Lỗi tập trung nửa đầu file (19/25 dòng ở key < 2015).
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục). Heuristic báo 0 dòng, bắt được 0/25 — toàn bộ lỗi đều cùng-loại nên heuristic không thấy.
- Không key-shift sạch (shift −5..+5 đều ~1,000 vì key thưa). TOML và CSV giống hệt nhau về nội dung (220 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW 1 (1265 「……」 — chỉ dấu câu, đúng).
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Thẻ `%l`: 45 dòng có thẻ, không dòng nào lệch. Thuật ngữ: 御一夜 → "Ohitoyo" (file đã có sẵn 1 "Ohitoyo" đúng ở 2307); 帝鉄, 湯医, 冥国, 冥軍, 小畑, 大畑, コン, 駿袋鉄道 không xuất hiện. Không có bản sao file này ở thư mục khác.
- Đề xuất cập nhật context chờ Hieu chốt: 整備体 = "thân bảo trì" / 運転ボディ = "thân vận hành" (tiền lệ Hachiroku 12); nếu chốt, 2512 ("cơ thể lái tàu" — dịch đúng, hiện không tính lỗi) cần đổi theo để thống nhất.
- Tổng 18 file đã audit: 1.550 dòng sai (133+255+299+374+199+2+20+12+19+7+101+10+23+19+25+14+13+25). File audit: audit-paulette07-shisen-REVIEW.md (khối TOML parse 25/25), audit-paulette07-shisen-wrong.json (25 mục).
- Tiếp theo: các file còn lại theo thứ tự nặng trước (danh sách heuristic).

## Paulette 08_未来へのレール (19/11/2026) — 22/466 sai (4,7%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, nặng về xưng hô hệ thống + thuật ngữ
- Xưng hô 10 (Soutetsu tự xưng "anh" 8 dòng thoại: 1490, 1946, 1979, 2058, 2068, 2188, 2199, 2210; "em" tự xưng 2 dòng: 2027, 2264; quét bằng máy: "anh" tự xưng 11 lần — 8 sai + 3 đúng khi nói với Hibiki 1901, 2346, 2347 — "em" tự xưng 2 lần đều sai, "tôi" chỉ 1 lần 2024), thuật ngữ 8 (Ohimitera 7 dòng + Ohito 1 dòng 2041 → Ohitoyo), sai nghĩa 4 (2220 thêm động từ "Tiếp nhận"; 2277 Nagi tự xưng 凪さま bị dịch thành hô ngữ "Nagi đại nhân!"; 2917 thêm từ "khen ngợi"; 3119 ナッパ服 → "trang phục làm việc" thay vì "đồ da nappa").
- Thoại sai 18/308, lời dẫn sai 4/158. Theo người nói: Soutetsu 13, Kisaki 3, Hibiki 1, Nagi 1, lời dẫn 4; Hachiroku 0, Paulette 0, Mayami 0, Hikari 0.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 trùng lặp nội bộ sai:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.381 mục). Heuristic báo 0 dòng, bắt được 0/22.
- Không key-shift sạch (shift −5..+5 đều ~1,000 vì key thưa). TOML và CSV giống hệt nhau về nội dung (244 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW 0.
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Thẻ `%l`: 1 dòng có thẻ (2090 — bản Việt thêm thẻ cho 2D3/4-8-6, nội dung đúng, chỉ ghi nhận quan sát). Thuật ngữ: 御一夜 → "Ohitoyo" (sau khi sửa file không còn "Ohimitera"/"Ohito" nào); ナッパ服 = "đồ da nappa"; 湯医 "Yui" 9 dòng (1888, 1910, 2301, 2306, 2363, 2447, 2672, 3042, 3043) giữ nguyên — quyết định chưa chốt; JP 2306 có furigana ゆのい trên 湯医 (thêm bằng chứng cho đề xuất "Yunoi"); 帝鉄 2 dòng (2384, 2777) dùng đúng dạng docs "Đường sắt Hoàng gia". 冥軍, 冥国, 小畑, コン, 駿袋鉄道, 整備体/運転ボディ không xuất hiện. Không có bản sao file này ở thư mục khác.
- "mình" trong độc thoại: 4 dòng (2831, 2841, 2968, 3041) đều đúng (sở hữu cách/thành ngữ) — không tính sai dòng nào.
- Tổng 19 file đã audit: 1.572 dòng sai (133+255+299+374+199+2+20+12+19+7+101+10+23+19+25+14+13+25+22). File audit: audit-paulette08-future-rail-REVIEW.md (khối TOML parse 22/22), audit-paulette08-future-rail-wrong.json (22 mục).

## Paulette 08_線から面へ (19/11/2026) — 26/387 sai (6,7%), 1 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi đa dạng nhất trong hai file Paulette 08
- Thuật ngữ 13 (御一夜 11 dòng: 1087, 1331, 1654, 1670, 1705, 1707, 1742, 2155, 2413, 2423, 2424 → Ohitoyo; 1744: 術仙炭鉱 "Jussen" thiếu "t" → "Jutsu-sen"; 2452: 端的 → "Ngắn gọn" thay vì "Nói thẳng ra"), xưng hô 5 (Soutetsu tự xưng "anh" trong thoại 2 dòng với du khách A: 1407, 1620; độc thoại "mình" làm chủ ngữ 3 dòng: 2473, 2545, 2549 — chỉ quét bằng máy mới bắt đủ), sai nghĩa 8 (1095 thêm vế "Từ điểm nối thành đường"; 1398, 1662, 1735 thêm "chị" sai người nhận; 1414 đảo chiều thể bị động của Reina; 1598 絡みたい → "kết hợp"; 1633 theo TW sai 過去形 → "đã chiến thắng" thay vì JP "thì quá khứ"; 1597 — đã chốt 19/11: người giao việc là Soutetsu → "anh", bản cũ "chị" sai), định dạng 1 (2433 thừa dấu 「 mở). Chưa chắc chắn 0 dòng.
- Thoại sai 18/213, lời dẫn sai 8/174. Theo người nói: Soutetsu 8, Paulette 5, lời dẫn 8, Hachiroku 2, Reina 2, Fukami 1, du khách B 1; Nagi 0, Mayami 0, Hibiki 0.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 trùng lặp nội bộ sai:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.381 mục). Heuristic báo 1 dòng (2433 — dấu 「 thừa): bắt được 1/26.
- Không key-shift sạch (shift −5..+5 đều ~1,000 vì key thưa). TOML và CSV giống hệt nhau về nội dung (234 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW 0.
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Thẻ `%l`: 20 dòng có thẻ, không dòng nào lệch. Thuật ngữ: 御一夜 → "Ohitoyo" (sau khi sửa file không còn "Ohimitera" nào); 共感 = "cộng cảm" ở 1524 (đúng, giữ nguyên); 湯医 "Yui" 3 dòng (1363, 1628, 1742) giữ nguyên — quyết định chưa chốt. 冥軍, 冥国, 小畑, コン, 駿袋鉄道, 整備体/運転ボディ, 帝鉄 không xuất hiện. Không có bản sao file này ở thư mục khác.
- "mình" trong độc thoại: 7 dòng — 4 đúng (1991, 2011, 2056, 2375: sở hữu cách/phản thân), 3 sai (2473, 2545, 2549: làm chủ ngữ cho Soutetsu).
- Đề xuất cập nhật context chờ Hieu chốt: (1) Soutetsu gọi Paulette thống nhất "em" cho mọi bối cảnh — bằng chứng mới 1534 ("Rất vinh hạnh được em khen", bối cảnh làm việc) đối lập 1623/1715/1739 ("cô", cũng bối cảnh công việc); (2) thống nhất "KiHa" (cách viết chính thức của JR) thay vì "Kiha" — file này dùng "KiHa 07" ở 6 gloss thẻ (1363, 1490, 1628, 1744, 1810, 2177).
- Tổng 20 file đã audit: 1.600 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27). File audit: audit-paulette08-line-to-plane-REVIEW.md (khối TOML parse 27/27), audit-paulette08-line-to-plane-wrong.json (27 mục).
- Tiếp theo: các file còn lại theo thứ tự nặng trước (danh sách heuristic).

## Paulette 09_ストーブ客車 (19/11/2026) — 28/405 sai (6,9%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở thuật ngữ theo quyết định mới
- **Lưu ý về tên file:** yêu cầu audit ghi hai file `ポーレット09_再開発の夢` (465 dòng) và `ポーレット09_波止場の朝` (397 dòng) — cả hai tên đều KHÔNG tồn tại trong dự án (không có trong CSV "Trang tính 3", cả hai zip TOML, docs hay bất kỳ tên file nào; không có file nào 465 dòng; 397 dòng là `日々姫08_開きかけのつぼみ` route Hibiki). File Paulette 09 duy nhất là `ポーレット09_ストーブ客車.txt.toml` (405 dòng) — đã audit file đó thay thế.
- Thuật ngữ 17 (御一夜 11 dòng: 1668, 1710, 1731, 1738, 1907, 1924, 1940, 1967, 2048, 2237, 2468 → Ohitoyo; 術仙 "Jussen" 6 dòng: 1368, 1892, 2048, 2081, 2156, 2782 → "Jutsu-sen" — 2048 mang cả hai; 電車姫 2262: "Công chúa Xe điện" → "Densha Hime", ngoại lệ duy nhất trong file khi cả file dùng "Densha Hime" 6 lần, toàn dự án 20 vs 2), xưng hô 4 (1746: Soutetsu "anh" → "tôi" với Paulette — chỉ 1 lần "anh" trong file, "tôi" 10 lần; độc thoại "mình" 3 dòng: 2594, 2640, 2968), sai nghĩa 4 (1655: JP 「やっ――」 bị dịch "Khôn――"; 1785: できますよ？ bị đổi thành câu hỏi xin phép + thêm "anh"; 2041: 問い直せる "hỏi lại ý dân" bị dịch "lấy lại được ý dân"; 2633: trùng giá trị với 2640, sai thì — triển vọng "sắp hiểu ra" vs quá khứ "đã hiểu ra"), lỗi nhỏ 3 (2274, 2275, 2277: mất tiếng hít っ — sửa "Ư!"/"Ư!?"/"~Ư!" theo tiền lệ 再開発 2103/2537).
- Thoại sai 21/236, lời dẫn sai 7/169. Theo người nói: lời dẫn 7, Paulette 7, Soutetsu 7, trung kiên nghị viên 2, lão nghị viên 2, Kisaki 1, chủ tọa 1, nữ nghị viên 1.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.381 mục); 24/28 dòng sai chỉ xuất hiện 1 lần. Ngoại lệ: 2633/2640 trùng nhau trong file; 2274/2275 là mẫu lỗi hệ thống toàn dự án (hàng trăm dòng "「!」" mất っ). Heuristic báo 0 dòng: bắt được 0/28.
- Không key-shift sạch (shift 0: 405/405). TOML và CSV giống hệt nhau về nội dung (272 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW 1 dòng (1390 「…………」 — giống hệt cả ba thứ tiếng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: 41 dòng có thẻ, không dòng nào lệch. Không có bản sao file này ở thư mục khác.
- "mình" trong độc thoại: 8 dòng — 4 đúng (2482, 2651, 2726, 2767), 4 sai (2594, 2633, 2640, 2968); quét máy sót 2968 ("Mình" viết hoa) — chỉ đọc kỹ mới bắt được.
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "cô" 7 lần (1395, 1713, 1805, 1819, 1931, 2129, 2177) vs "em" 1 lần (1746) — ĐẢO HƯỚNG so với đề xuất "thống nhất em" từ Paulette 08; "KiHa 07" thêm 1 gloss ở 2609. 湯医, 帝鉄, 冥国, 冥軍, 小畑, 駿袋鉄道, 整備体/運転ボディ, 端的 không xuất hiện. Không tính sai: 1731 "xưởng nấu rượu Migita Ichi" (JP 右田一酒造元, TW đồng thuận; docs §2.6 ghi "Migita System" — hai cách gọi cùng tồn tại 11 vs 15 toàn dự án, cần Hieu đối chiếu).
- Tổng 21 file đã audit: 1.626 dòng sai (133+255+299+374+199+2+20+12+19+7+101+10+23+19+25+14+13+25+22+26+28). File audit: audit-paulette09-stove-car-REVIEW.md (khối TOML parse 28/28), audit-paulette09-stove-car-wrong.json (28 mục).

## Paulette 10_見えない傷 (19/11/2026) — 20/388 sai (5,2%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi rải rác từng dòng ở cảnh gia đình
- Thuật ngữ 3 (御一夜 3 dòng: 1042, 1573 "Ohimitera", 2133 "Ohito" → Ohitoyo), sai nghĩa 3 (白湯 2 dòng 1611, 2019: "nước lọc" → "nước ấm" theo chuẩn của chính file ở 1504; 1846: TW chèn chủ ngữ 媽媽她 nên bản cũ dịch sai thành "Mẹ... khóc mất rồi" — đúng là Paulette nhỏ khóc gọi mẹ, sửa "Mình... khóc mất rồi―― Mẹ――"), xưng hô 7 (Soutetsu "anh" 2 dòng thoại 1382, 1445; độc thoại "mình" làm chủ ngữ 4 dòng 1963, 2283, 2360, 2385; thì thầm "anh" 1 dòng 2148), lỗi nhỏ 7 (mất tiếng hít っ: 984, 1000, 1633, 1634, 1635, 1636, 1639 — trong đó 1000/1633 là tiếng hít mở đầu câu, không độc lập nhưng vẫn mất thật).
- Thoại sai 12/200, lời dẫn sai 8/188. Theo người nói: lời dẫn 8, Soutetsu 6, Paulette 3, Kozo 2, Maia 1; Reina 0.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục); 15/20 dòng sai chỉ xuất hiện 1 lần. Ngoại lệ: 984, 1634, 1635 (chuỗi dấu câu/gasp ngắn chung chung), 1636/1639 trùng nhau trong file (cùng tiếng hít nghẹn ở hai cảnh lái tàu). Heuristic báo 0 dòng: bắt được 0/20.
- Không key-shift sạch (shift 0: 388/388; các shift khác ~1,000 vì key thưa). TOML và CSV giống hệt nhau về nội dung (220 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW 0.
- `[selections]` rỗng (0 mục). Thẻ `%l`: 24 dòng có thẻ ở cả JP và VN, không dòng nào lệch. Không có bản sao file này ở thư mục khác.
- "mình" trong độc thoại: 27 dòng — 23 đúng (sở hữu cách/phản thân/thành ngữ, mẫu "Tôi… mình…", lời thoại nội tâm trích dẫn 2039, POV trẻ con của Paulette nhỏ 12 dòng), 4 sai (1963, 2283, 2360, 2385). Soutetsu thoại: "tôi/Tôi" 19 dòng vs "anh/Anh" 2 dòng (cả hai sai).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "cô" 20 lần (991, 998, 1239, 1262, 1278, 1314, 1353, 1362, 1378, 1451, 1465, 1469, 1471, 1487, 1510, 1511, 1522, 1561, 1565, 1575) vs "em" 2 lần (1369, 1373) — nghiêng mạnh về "cô"; 湯医 "Yunoi" 7 lần (1524, 1556, 1916, 2044, 2053, 2287, 2297), 0 lần "Yui" (1524 có furigana ゆのい); "KiHa 07" 4 gloss thẻ (65, 1487, 1563, 1565); 機関士/運転士 "nhân viên cơ vụ" 3 dòng (959, 1241, 1998) — không tính sai. Quy ước file: 62 dòng độc thoại bắt đầu bằng dấu ngoặc kép "..." (POV trẻ con + một số suy nghĩ ngoặc đơn) — không tính sai, bản sửa giữ nguyên. 2032: JP tự mang thẻ %l kép lỗi, VN giữ nguyên — không tính sai.
- Tổng 22 file đã audit: 1.648 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20). File audit: audit-paulette10-unseen-wound-REVIEW.md (khối TOML parse 20/20), audit-paulette10-unseen-wound-wrong.json (20 mục).

## Paulette 11_記憶と記録 (19/11/2026) — 22/402 sai (5,5%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở thuật ngữ タブレット + tiếng hít っ
- Thuật ngữ 12 (タブレット 9 dòng: 998, 1349, 1528, 1551, 1660, 1724, 1754, 2006, 2085 — "Thẻ bảng"/"thẻ bảng" → "máy tính bảng" theo tiền lệ stove 2076/2642; 御一夜 3 dòng: 1463, 1550 "Ohimitera", 1538 "Ohito" → Ohitoyo), sai nghĩa 1 (1001: chủ ngữ là cái thẻ bảng theo chủ đề từ 998, TW đọc ngôi thứ nhất nên bản cũ biến Soutetsu thành chủ ngữ "cháu" — theo quy tắc JP-trên-TW), xưng hô 2 (độc thoại "mình" trong suy nghĩ ngoặc đơn: 2600, 2601 — 2601 kèm lỗi dùng từ "thà" → "mà"), lỗi nhỏ 7 (mất tiếng hít っ: 1008, 1771, 1772, 1774, 1775, 1776, 1777 — cụm 1771–1777 liên tiếp trong một cảnh Paulette hoảng sợ).
- Thoại sai 18/200, lời dẫn sai 4/202. Theo người nói: Soutetsu 10, Paulette 5, lời dẫn 4, Chủ nhà tắm Tororyu-yu 1, Niiroku 1, Đại tư tế Akai 1; Reina 0.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục); 17/22 dòng sai chỉ xuất hiện 1 lần. Ngoại lệ: 1771, 1772, 1774, 1775, 1776 (chuỗi gasp ngắn chung chung). Heuristic báo 0 dòng: bắt được 0/22.
- Không key-shift sạch (shift 0: 402/402; các shift khác 0,97–0,99 vì key thưa). TOML và CSV giống hệt nhau về nội dung (284 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW 1 dòng (1019 「…………」 — giống hệt cả ba thứ tiếng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: 47 dòng có thẻ ở cả JP và VN, không dòng nào lệch. Không có bản sao file này ở thư mục khác.
- "mình" trong độc thoại: 11 dòng — 9 đúng (sở hữu cách/phản thân/thành ngữ, mẫu "Tôi… mình…"), 2 sai (2600, 2601). Soutetsu thoại: "tôi/Tôi" 8 dòng, "anh/Anh" tự xưng 0 lần, "cháu/Cháu" 18 dòng (với bậc trên — đúng, trừ 1001), "em" ngôi hai 2 lần (cả hai với Reina).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "cô" 9 lần (1280, 1312, 1381, 1399, 1485, 1488, 1567, 1568, 1722) vs "em" 0 lần — bằng chứng thứ ba liên tiếp nghiêng về "cô"; 湯医 "Yunoi" 1 lần (1618); 運転士 "nhân viên cơ vụ" 2 dòng (2412, 2511) — không tính sai; 整備ボディ 1304 "cơ thể bảo dưỡng" — không tính sai, bằng chứng cho đề xuất "thân bảo trì". Đề xuất cập nhật context: (1) glossary trong game context_trans.md:541 ghi "Thẻ bảng (tablet)" mâu thuẫn với "máy tính bảng" — nên sửa glossary; (2) ruby [tên,N] trên số hiệu: toàn dự án bỏ 306 lần vs giữ 14 lần nên 1781 bỏ "[ニイロク,1]26" là chuẩn chung, không tính sai.
- Tổng 23 file đã audit: 1.670 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22). File audit: audit-paulette11-memory-record-REVIEW.md (khối TOML parse 22/22), audit-paulette11-memory-record-wrong.json (22 mục).

## Paulette 12_解放 (19/11/2026) — 7/194 sai (3,6%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi rải rác từng dòng ở cảnh điện thoại với mẹ
- Thuật ngữ 1 (1121: 御一夜 "Ohimitera" → Ohitoyo + thẻ %l của エアクラ thiếu dấu `;` đóng), lỗi nhỏ 3 (mất tiếng hít っ: 822, 1161, 1162 — sửa "Ư"/"Ư!"/"Ư!?" theo tiền lệ 再開発 2103/2537), sai nghĩa 2 (1448: ぽわっと "Phừng phực" → "Ấm dần lên." — sai hẳn hình ảnh hơi ấm dịu dàng; 1510: theo TW thêm "đã dừng lại" trong khi JP chỉ là mảnh câu bỏ lửng — bỏ theo quy tắc JP-trên-TW), xưng hô 1 (độc thoại "mình" 1525 → "Tôi").
- Thoại sai 4/102, lời dẫn sai 3/92. Theo người nói: Soutetsu 3, Paulette 1, lời dẫn 3.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (81.202 mục); 7/7 dòng sai chỉ xuất hiện 1 lần. Ngoại lệ: 1011/1012 trùng "「Hả?」" (JP cả hai đều 「え？」 — hợp lệ); các chuỗi ngắn chung chung khác đều là bản dịch đúng của JP riêng nó. Heuristic báo 0 dòng: bắt được 0/7.
- Không key-shift sạch (shift 0: 194/194). TOML và CSV giống hệt nhau về nội dung (131 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW 0.
- `[selections]` rỗng (0 mục). Thẻ `%l`: 1 dòng có thẻ (1121), thiếu dấu `;` đóng — đã sửa trong khối TOML. Không có bản sao file này ở thư mục khác.
- "mình" trong độc thoại: 7 dòng — 6 đúng (sở hữu/phản thân/mệnh đề phụ/thành ngữ "một mình mẹ"), 1 sai (1525). Soutetsu thoại: "tôi/Tôi" 15 dòng, "anh/Anh" tự xưng 0 lần — sạch như Paulette 11 về mặt này.
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "cô" 7 lần (973, 1021, 1058, 1090, 1110, 1112, 1113) vs "em" 0 lần — cộng dồn P09–12: "cô" 43 vs "em" 3. 湯医, 帝鉄, コン, タブレット: 0 lần xuất hiện. Đề xuất cập nhật context: (1) quét toàn dự án cho 151 thẻ %l thiếu dấu `;` đóng (JP 4756/4756 có ";") — cần Hieu kiểm tra trong game trước.
- Tổng 24 file đã audit: 1.677 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7). File audit: audit-paulette12-liberation-REVIEW.md (khối TOML parse 7/7), audit-paulette12-liberation-wrong.json (7 mục).

## Paulette 13_再評価 (19/11/2026) — 29/208 sai (13,9%), 1 dòng chưa chắc chắn (1357); file sạch về cấu trúc, lỗi tập trung ở thuật ngữ hệ thống + thẻ %l
- Thuật ngữ 21 (御一夜 13 dòng: 1156, 1352, 1353, 1365, 1372, 1374, 1376, 1397, 1593, 1608, 1683, 1701, 1724 → Ohitoyo; 術仙 9 dòng: 1319, 1320 "Jutsusen" thiếu gạch nối, 1353, 1366, 1422, 1446, 1447, 1448, 1477 "Jussen" thiếu chữ "t" → "Jutsu-sen" — 1353 mang cả hai), lỗi nhỏ 5 (thẻ %l thiếu dấu `;` đóng: 1397, 1366 kèm trong bản sửa thuật ngữ; 1596, 1637, 1641 riêng), xưng hô 2 (Soutetsu "anh" → "tôi" với Paulette: 1309, 1479 — 1309 giữ "Em" gọi Paulette theo đề xuất đang chờ), lỗi nhỏ 2 (mất tiếng hít っ: 1483, 1484), sai nghĩa 1 (1952: プッ "Tít" → "Bụp" — tiếng bật môi sau nụ hôn, không phải tiếng bíp). Chưa chắc chắn 1 (1357: Paulette tự xưng "em" giữa cảnh họp hội đồng — chỉ đúng nếu nói với Soutetsu ở cánh gà; đã kiểm tra cột Character + 5 dòng xung quanh, không xác định được người nghe — chờ Hieu kiểm tra trong game, KHÔNG đưa vào khối TOML).
- Thoại sai 19/97, lời dẫn sai 10/111. Theo người nói: Paulette 10, lời dẫn 10, lão nghị viên 4, chủ tọa 3, Soutetsu 2.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (81.202 mục); 29/29 dòng sai chỉ xuất hiện 1 lần. Ngoại lệ: 1408, 1480, 1481 (chuỗi ngắn chung chung, bản dịch đúng của JP riêng nó). Heuristic báo 0 dòng: bắt được 0/29.
- Không key-shift sạch (shift 0: 208/208). TOML và CSV giống hệt nhau về nội dung (133 dòng khác chỉ ở `\n`/khoảng trắng). Không có dòng CSV trống nào; VN==TW 1 dòng (1168 「……………………」 — giống hệt cả ba thứ tiếng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: 6 dòng có thẻ, 5 thiếu dấu `;` đóng (1397, 1366, 1596, 1637, 1641) — chỉ 1674 đóng đúng. Không có bản sao file này ở thư mục khác.
- "mình" trong độc thoại: 4 dòng — cả 4 đều đúng (sở hữu/phản thân/mệnh đề phụ). Soutetsu thoại: "tôi/Tôi" 1 dòng, "anh/Anh" tự xưng 2 lần (cả hai sai).
- Bằng chứng mới cho quyết định đang chờ: **Soutetsu gọi Paulette "em" 2 lần (1309, 1418) vs "cô" 0 lần (trực tiếp) — file đầu tiên trong route Paulette nghiêng về "em"**, phá vỡ chuỗi 4 file liên tiếp nghiêng về "cô"; cộng dồn P09–13: "cô" 43 vs "em" 5. (1163 có "cô ấy" nhưng là ngôi ba, không tính.) Paulette tự xưng theo người nghe: "tôi" ở hội đồng, "em" với Soutetsu, "chị" với Reina, "cháu" với Densha Hime. 湯医, 帝鉄, コン, タブレット: 0 lần xuất hiện. 1472 "Quảng trường Shirakabe" theo furigana JP (không theo tên thật 黒壁 của TW) — đúng, không tính sai. Đề xuất cập nhật context: (1) quét toàn dự án cho 151 thẻ %l thiếu dấu `;` đóng (như Paulette 12).
- Phát hiện ngoài lề qua chỉ mục Việt: ポーレットh8 3114 và 日々姫04 2480 có VN không khớp JP của chính nó (có vẻ lệch vị trí) — để lại cho audit các file đó sau.
- Tổng 25 file đã audit: 1.706 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29). File audit: audit-paulette13-reevaluation-REVIEW.md (khối TOML parse 29/29), audit-paulette13-reevaluation-wrong.json (30 mục: 29 sai + 1 chưa chắc chắn).
- Tiếp theo: các file Paulette 14 trở đi chưa audit; thứ tự ưu tiên theo danh sách heuristic.

## Paulette 14_ふたたび走り出すために (19/11/2026) — 32/376 sai (8,5%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở xưng hô hệ thống + thuật ngữ
- Thuật ngữ 12 (御一夜 10 dòng: 1422, 1508, 1560, 1584, 1723, 1733, 1814, 1878, 2123, 2135 → Ohitoyo; 術仙 1 dòng: 2462 "Jutsusen" thiếu gạch nối → "Jutsu-sen"; 廃駅 1 dòng: 1683 "Ga phế liệu" → "Ga bỏ hoang" — cách dịch 廃駅 duy nhất kiểu này trong toàn dự án, các chỗ khác đều "ga bỏ hoang"), xưng hô 18 dòng (Soutetsu tự xưng "anh" 17 dòng trong thoại: 1386, 1424, 1514, 1519, 1544, 1571, 1617, 1622, 1628, 1644, 1647, 1653, 1655, 1657, 1727, 1733, 1739 + "Anh" 1 dòng trong độc thoại 2273 — 1733 mang cả hai lỗi nên tổng lượt lỗi là 33 trên 32 dòng), lỗi nhỏ 2 (mất tiếng hít っ: 1889, 1890 → "Ư!!?"), sai nghĩa 1 (2400: ぽわっと "cười rạng rỡ" → "khẽ cười, ấm áp và dịu dàng" — tiền lệ Paulette 12 1448).
- Thoại sai 27/212, lời dẫn sai 5/164. Theo người nói: Soutetsu 21, lời dẫn 5, Hibiki 3, Hachiroku 2, đền chủ Akai 1.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục); 29/32 dòng sai chỉ xuất hiện 1 lần. Ngoại lệ: 1657 "Anh á?" cũng có ở 日々姫01 2307 (JP 「僕がか？」 — cùng một lỗi xưng hô ở file khác, không phải tràn chương); 1889/1890 "!!?" xuất hiện 85 lần (mẫu lỗi hệ thống mất tiếng hít っ). Heuristic báo 0 dòng: bắt được 0/32. Không có dòng CSV trống nào; VN==TW 0.
- Không key-shift sạch (shift 0: 376/376). TOML và CSV giống hệt nhau về nội dung (229 dòng khác chỉ ở `\n`/khoảng trắng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: 32 dòng có thẻ trong VN (JP có 30) — **0 thẻ thiếu dấu `;` đóng** (khác Paulette 13: 5 thẻ thiếu `;`); 1410 có thẻ gloss cho ruby [にい,1]/[いもうと,1] có sẵn trong JP.
- "mình" trong độc thoại: 8 dòng chứa "mình"/"Anh" — 7 dòng "mình" đều đúng (sở hữu/phản thân/thành ngữ/suy nghĩ trích dẫn), 1 dòng sai (2273 "Anh"). Soutetsu thoại: "tôi/Tôi" 8 dòng, "anh/Anh" tự xưng 18 dòng (17 sai + 1549 là tiếng của Paulette trong câu tường thuật "cô ấy nghĩ anh…" — giữ nguyên).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 1 lần (1549) vs "cô" 0 lần — cộng dồn P09–14: "cô" 43 vs "em" 6; 湯医 "Yui" 1 lần (83 "ga Yui"), "Yunoi" 0 lần; "KiHa 07" 3 gloss (1400, 1818, 2049); 運転ボディ → "thân hình lái tàu" (2286), 整備ボディ → "thân chính bảo dưỡng" (2530) — bằng chứng mới cho đề xuất cặp "thân vận hành"/"thân bảo trì". Đã kiểm tra và không tính sai: 1410 (mảnh câu dở dang theo đúng JP), 1495 (美味しそう "nghe ngon" — trong cảnh nghe mô tả bento nên tự nhiên), 1549 (xem trên), 1404 (っ sau số đếm chỉ là nhấn mạnh), 1677 ("trăm sự nhờ ông" thêm vào nhưng không đổi nghĩa).
- Tổng 26 file đã audit: 1.738 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32). File audit: audit-paulette14-run-again-REVIEW.md (khối TOML parse 32/32), audit-paulette14-run-again-wrong.json (32 mục).

## Paulette 15_求人難 (19/11/2026) — 36/408 sai (8,8%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở xưng hô hệ thống (Soutetsu "em" áp đảo "anh")
- Thuật ngữ 9 (御一夜 8 dòng: 1402, 1407, 1610, 1666, 1677, 1694, 2151, 2462 → Ohitoyo — 2462 là tên công ty Ohitoyo Work Service; 術仙 1 dòng: 1796 "Jutsusen" thiếu gạch nối → "Jutsu-sen"), xưng hô 23 dòng (Soutetsu tự xưng "em" 14 dòng trong thoại: 1103, 1396, 1398, 1410, 1514, 1631, 1640, 1641, 1646, 1702, 1729, 1774, 1801, 1819 + "anh" 6 dòng: 1483, 1580, 1619, 1686, 1718, 1943 + "Mình" 1 dòng trong thoại 1527 + "Em" 2 dòng trong độc thoại 1062, 2359 — 2359 giữ "mình" ở câu hai theo mẫu "Tôi… mình…"), lỗi nhỏ 4 (mất tiếng hít っ: 1903 "……!!" → "……Ư!!", 1976 "!" → "Ư!", 1977 "!!" → "Ư!!", 1978 "!?" → "Ư!?").
- Thoại sai 32/250, lời dẫn sai 4/158. Theo người nói: Soutetsu 27, lời dẫn 4, Fukami 2, Minokasa 2, Paulette 1.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục); 33/36 dòng sai chỉ xuất hiện 1 lần. Ngoại lệ: 1976 "!" 206 lần, 1977 "!!" 54 lần, 1978 "!?" 68 lần (mẫu lỗi hệ thống mất tiếng hít っ). Heuristic báo 0 dòng: bắt được 0/36. Không có dòng CSV trống nào; VN==TW 0.
- Không key-shift sạch (shift 0: 408/408). TOML và CSV giống hệt nhau về nội dung (265 dòng khác chỉ ở `\n`/khoảng trắng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: 27 dòng có thẻ trong VN (JP có 24) — **0 thẻ thiếu dấu `;` đóng**; 1786, 1849, 1958 có thẻ gloss cho ruby có sẵn trong JP ([かんそう,1], [いっとき,1], [ハチロク,3]).
- "mình" trong độc thoại: 6 dòng chứa "mình" — tất cả đều đúng (sở hữu/phản thân). Soutetsu thoại: "tôi/Tôi" 9 dòng, "anh/Anh" tự xưng 6 dòng (tất cả sai), "em/Em" tự xưng 14 dòng (tất cả sai) — file đầu tiên "em" áp đảo "anh"; cả 14 dòng "em" đều là nói với Mayami.
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 1 lần (1459) vs "cô" 0 lần — cộng dồn P09–15: "cô" 43 vs "em" 7; 湯医 0 lần; "KiHa 07" 9 gloss (nhiều nhất từ trước đến nay); "Migita Ichi" 2 lần (1727, 1732 — theo đúng JP 右田一酒蔵元, trái docs "Migita System" — chờ Hieu đối chiếu); マスコン "bộ điều khiển trung tâm" (1073, 1981) vs マスターコントローラー "Master Controller" (1664) — kiểm tra toàn dự án: "điều khiển trung tâm" là quy ước 10+ lần, "Master Controller" chỉ 1 lần → đề xuất thống nhất về "điều khiển trung tâm". Đã kiểm tra và không tính sai (JP-trên-TW): 1742 (大根 "Củ cải" — TW đọc sai thành 指控), 2336 (れいなの足 "chân Reina" — TW sai thành ngón tay), 2637 (大根/ごぼう — TW lạc đề).
- Tổng 27 file đã audit: 1.774 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36). File audit: audit-paulette15-hiring-difficulty-REVIEW.md (khối TOML parse 36/36), audit-paulette15-hiring-difficulty-wrong.json (36 mục).

## Paulette 16_明日へのレール (19/11/2026) — 55/542 sai (10,1%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở xưng hô hệ thống (Soutetsu "anh" 23/90 dòng thoại) + thuật ngữ
- Thuật ngữ 17 (御一夜 16 dòng: 1313, 1699, 1912, 1968, 2032, 2038, 2043, 2075, 2105, 2152, 2194, 2196, 2217, 2321, 2338, 2933 → Ohitoyo; 術仙 1 dòng: 2252 "Jutsusen" thiếu gạch nối → "Jutsu-sen"), xưng hô 27 dòng (Soutetsu tự xưng "anh/Anh" 23 dòng trong thoại: 1703, 1711, 1738, 1743, 1745, 1947, 1967, 2087, 2102, 2117, 2121, 2141, 2144, 2162, 2186, 2211, 2247, 2253, 2344, 2408, 2412, 2425, 2430 + 4 dòng trong độc thoại: 1303, 2816, 3015, 3391), sai nghĩa 7 (Paulette gọi Soutetsu là "cậu" 4 dòng: 1739, 2269, 2351, 2429 — theo docs §2.4 "Anh Soutetsu" + tỉ lệ toàn dự án 470:13; 1707 "kịch kim" — từ không có trong tiếng Việt, chỉ xuất hiện đúng 1 lần toàn dự án; 1838 tự bịa kết luận "Thì chắc chắn rồi" vào câu dở dang của JP; 2326 "Phu nhân Minokasa" theo TW sai — JP 蓑笠さん là ông Minokasa, bằng chứng 3308), lỗi nhỏ 4 (mất tiếng hít っ: 2448, 2449, 2450 + 3330 còn sót kana っ "——っ!").
- Thoại sai 48/324, lời dẫn sai 7/218. Theo người nói: Soutetsu 29, Paulette 12, lời dẫn 7, nhân viên B 2, Bộ trưởng Giáo dục 2, Bộ trưởng Kinh tế 2, Fukami 1.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục); 52/55 dòng sai chỉ xuất hiện 1 lần. Ngoại lệ: 2448 "!" 206 lần, 2449 "!!?" 85 lần, 2450 "!?" 68 lần (mẫu lỗi hệ thống mất tiếng hít っ). Heuristic báo 0 dòng: bắt được 0/55 (1307 là dương tính giả: JP mở đầu bằng “ cong, VN mở đầu bằng " thẳng). Không có dòng CSV trống nào; VN==TW 0.
- Không key-shift sạch (shift 0: 541/542). TOML và CSV giống hệt nhau về nội dung (327 dòng khác chỉ ở `\n`/khoảng trắng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: 28 dòng có thẻ trong VN (JP có 28) — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 11 dòng — tất cả đều đúng (sở hữu/phản thân/thành ngữ/mẫu "Tôi… mình…"). Soutetsu thoại: "tôi/Tôi" 7 dòng (đúng), "anh/Anh" tự xưng 23 dòng (tất cả sai), "em/Em" tự xưng 0 dòng, "cháu" 2 dòng (đúng, với người lớn tuổi). "mình" trong thoại Soutetsu 4 dòng (1682, 2087, 2141, 2162) — tất cả đúng, giữ nguyên.
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 7 lần (1751, 1967, 2117, 2121, 2247, 2412, 2425) vs "cô" 0 lần — cộng dồn P09–16: "cô" 43 vs "em" 14. **Mẫu mới: ranh giới rạch ròi theo chương** — P09–12 nghiêng "cô" (43:3), P13–16 nghiêng "em" (0:11). 湯医 "Yui" 1 lần (2032), "Yunoi" 0 lần. "KiHa 07": 3 gloss đều là "Kiha" (1971, 2835, 3251). **Đề xuất mới: 宮司** — file này dùng "ông Guuji" 4× (1708, 2292, 2933, 3304); toàn dự án "đền chủ" 46× vs "Cung tư tế" 11× vs "Guuji" 9× → đề xuất thống nhất về "đền chủ". 帝鉄 1× đúng dạng docs. Đã kiểm tra và không tính sai: 3236 "anh ta" (ngôi ba), 1307 (dương tính giả), 2246 (VN theo JP, TW tự thêm 双鉄先生), 2321 (địa danh theo furigana JP), 3377 （コンコン） tiếng gõ cửa.
- Tổng 28 file đã audit: 1.829 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55). File audit: audit-paulette16-tomorrow-rail-REVIEW.md (khối TOML parse 55/55), audit-paulette16-tomorrow-rail-wrong.json (55 mục).
- Route Paulette chính (chương 03–16 + Grand 04) đã audit xong toàn bộ. Còn lại trong 03_Paulette: chương 02 (2 file), h1–h8 (8 file), lr_h1/lr_h2/lr_稀咲h1/れいな02 (4 file). (Chương 01 đã audit xong 19/11 — xem 2 mục dưới.)

## Paulette 01_ポーレット退任 (19/11/2026) — 35/419 sai (8,4%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở xưng hô hệ thống (Soutetsu "anh" 19/21 lần tự xưng) + thuật ngữ
- Thuật ngữ 12 (御一夜 12 dòng: 1813, 1977, 1789, 2012, 1543, 1727, 2342, 1796, 1567, 2008, 2004, 1865 → Ohitoyo — 1789 mang cả hai dạng "Ohimitera" + "Đường sắt Ohito"; file có 0 lần "Ohitoyo" đúng), xưng hô 19 dòng (Soutetsu tự xưng "anh" trong thoại: 1932, 2019, 1511, 1207, 1841, 1942, 1558, 1582, 1194, 1820, 1940, 1741, 1827, 2020, 2009, 1858, 1998, 1941, 1830), lỗi nhỏ 4 (mất tiếng hít っ: 1648 → "Ư!"; độc thoại bọc trong 「」: 2557, 2555; "bà Takasaki" → "chị Takasaki": 2247).
- Thoại sai 31/269, lời dẫn sai 4/150. Theo người nói: Soutetsu 19, Paulette 7, Kisaki 3, lời dẫn 4, nhân viên B 1, Reina 1.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục); 34/35 dòng sai chỉ xuất hiện 1 lần. Ngoại lệ: 1648 "「!」" xuất hiện 206 lần (mẫu lỗi hệ thống mất tiếng hít っ). Heuristic báo 2 dòng: bắt được 2/35 (2557, 2555). Không có dòng CSV trống nào; VN==TW 0.
- Không key-shift sạch (shift 0: 417/419). TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 1 thẻ gloss thêm vào ở 2443 — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 10 dòng — tất cả đều đúng (sở hữu/phản thân/thành ngữ/mẫu "Tôi… mình…"). Soutetsu thoại: "tôi/Tôi" 2 dòng (1923, 1999 — đúng), "anh/Anh" tự xưng 19 dòng (tất cả sai).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 6 lần (1820, 1922, 1531, 1765, 2007, 1541) vs "cô" 2 lần (1539, 2005) — cộng dồn P09–16 + file này: "cô" 43 vs "em" 20; **chương 01 nghiêng "em" — giả thuyết "ranh giới rạch ròi theo chương" bị phá vỡ**. 宮司 1 lần (2236 "thầy tế Akai" — biến thể thứ 4); "KiHa 07S" 1 gloss (2548). Đã kiểm tra và không tính sai: Paulette gọi Kisaki "chị" (1624, 1795, 2012 — quy ước toàn dự án, cũng có ở 共通11 và Grand 04 2029); 1893 "vợ anh Takasaki" (anh = Takasaki); cặp trùng "「A——」" 1641/1697 đều đúng.
- Tổng 29 file đã audit: 1.864 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35). File audit: audit-paulette01-retirement-REVIEW.md (khối TOML parse 35/35), audit-paulette01-retirement-wrong.json (35 mục).

## Paulette 01_御一夜探し (19/11/2026) — 44/369 sai (11,9%), 0 dòng chưa chắc chắn; 1 cặp lệch vị trí + lỗi hệ thống xưng hô ("anh" 15/15) và thuật ngữ ("Ohito" 25/25)
- Thuật ngữ 24 (御一夜 24 dòng: 1696, 1786, 1716, 1683, 1859, 1846, 1527, 1588, 1914, 1789, 1693, 1927, 2307, 2471, 1524, 1776, 2556, 1820, 1889, 1691, 1936, 1945, 1686, 2551 → Ohitoyo — 1846 mang 2 lần "Ohito"; file có 0 lần "Ohitoyo" đúng), xưng hô 15 dòng (Soutetsu tự xưng "anh": 1699, 1463, 1704, 1817, 1633, 1649, 1538, 1563, 1668, 1914, 1927, 1926, 1196, 1625, 1592 — 1914, 1927 mang cả hai lỗi), sai nghĩa 5 (1756 廃客車 "phế liệu" → "bỏ hoang"; 1888 bỏ tên キジウマ; 1151 cắt cụt + 2196 thừa câu — cặp lệch vị trí; 1683 Nagi tự xưng 凪様 → "Bổn tiểu thư"), lỗi nhỏ 3 (mất tiếng hít っ: 1947, 2480, 1950).
- Thoại sai 37/217, lời dẫn sai 7/152. Theo người nói: Soutetsu 22, Paulette 10, lời dẫn 7, Nagi 2, Hachiroku 1, Mayami 1, Hibiki 1.
- **Lệch vị trí 1 cặp (1151↔2196), 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** câu 2 của 1151 nằm thừa ở đầu 2196; cả hai đều là lời dẫn nên heuristic không phát hiện. Đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục); 43/44 dòng sai chỉ xuất hiện 1 lần. Ngoại lệ: 1947 "「!」" xuất hiện 206 lần (mẫu lỗi hệ thống mất tiếng hít っ). Heuristic báo 0 dòng: bắt được 0/44. Không có dòng CSV trống nào; VN==TW 0.
- Không key-shift sạch (shift 0: 369/369). TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 84 thẻ, VN có 84 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 10 dòng — tất cả đều đúng (thành ngữ "một mình"/"giật mình", sở hữu, mẫu "Tôi… mình…"). Soutetsu thoại: "tôi/Tôi" 0 lần, "anh/Anh" tự xưng 15 dòng (tất cả sai) — file đầu tiên có tỉ lệ "anh" 100%.
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 10 lần (1845, 1503, 1649, 1928, 1916, 1812, 1651, 1661, 1927, 1926) vs "cô" 0 lần — cộng dồn P01 + P09–16: "cô" 43 vs "em" 30; **chương 01 nghiêng "em" 16:2, phá vỡ giả thuyết ranh giới chương**. コン dùng "Kon" 10 lần (JP 11 lần; lần thứ hai ở 1594 dịch thành "em" — đúng). 帝鉄 1 dòng (1912) đúng dạng docs. Đã kiểm tra và không tính sai (JP-trên-TW): 1490 "Kusatsu" (furigana くさつ), 2560 "Okinawa" (furigana おきなわ); 1450 "%61;" có sẵn trong JP; 1825 Soutetsu gọi "Nagi đại nhân" (đúng); "bà" cho bà Nagayama trong độc thoại vs "cô" trong thoại (quy ước trong file).
- Tổng 30 file đã audit: 1.908 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44). File audit: audit-paulette01-ohitoyo-search-REVIEW.md (khối TOML parse 44/44), audit-paulette01-ohitoyo-search-wrong.json (44 mục).
- Chương 01 tuyến Paulette đã audit xong (35 + 44 = 79 dòng sai trên 788 dòng, 10,0%). Còn lại trong 03_Paulette: chương 02 (2 file), h1–h8 (8 file), lr_h1/lr_h2/lr_稀咲h1/れいな02 (4 file).

## Paulette 02_古地図 (19/11/2026) — 41/385 sai (10,6%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở thuật ngữ hệ thống + xưng hô (Soutetsu "anh" 9/10 lần tự xưng)
- Thuật ngữ 25 (御一夜 11 dòng: 1582, 1688, 1751, 1753, 1826, 1900, 1924, 1935, 2100, 2560, 2675 "Ohito" → Ohitoyo; 術仙 11 dòng: 1683, 1719, 1725, 1856, 1858, 2052, 2136, 2394, 2670, 2747, 2414 "Jussen" thiếu chữ "t" → "Jutsu-sen"; 術仙道 2 dòng: 2048, 2414 "Jussendo" → "Jutsusendo" — 2414 mang cả hai lỗi; ポイント 1896 "công tắc" → "ghi" (TW 轉轍器); 大詔 2104 "Đại Chiếu" → "Taisho" theo tiền lệ 再開発 3054), xưng hô 9 dòng (Soutetsu tự xưng "anh" trong thoại: 1572, 1574, 1581, 1598, 1640, 1763, 1840, 1842, 2037 — 4 dòng trong số đó chỉ phát hiện được bằng quét máy), sai nghĩa 4 (1617 đảo ngược chủ thể — Akai giúp Soutetsu nhận ra; 1782 gọi sai người được nhờ "cô" — người được nhờ là Soutetsu "cậu", ghi chú phương án Hibiki "cháu"; 2105 gọi thầy Akai là "chị" → "thầy"; 2553 キンメダイ "cá tráp đỏ" → "cá mắt vàng", TW 金眼鯛 xác nhận), lỗi nhỏ 3 (mất tiếng hít っ: 1638, 2172, 2173).
- Thoại sai 34/241, lời dẫn sai 7/144. Theo người nói: Soutetsu 23, Paulette 4, Akai 4, lời dẫn 7, Hibiki 1, Mayami 1, Fukami 1.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục); bản Việt trùng duy nhất trong file là "「Vâng。」" 1895/1728 (JP đều 「はい」, đều đúng). Heuristic báo 0 dòng: bắt được 0/41 (không có lỗi lệch vị trí để bắt). Heuristic dấu phẩy MT báo 15 dòng: 0 dòng sai. Không có dòng CSV trống nào; VN==TW 0.
- Không key-shift sạch (shift 0: 385/385; các shift khác cũng 1,000 — kiểm tra không cho thông tin thêm). TOML và CSV giống hệt nhau về nội dung (240 dòng khác chỉ ở `\n`/khoảng trắng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 12 thẻ, VN có 12 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 6 dòng — tất cả đều đúng (sở hữu/phản thân/thành ngữ/mệnh đề lồng "Tôi… mình…"). Soutetsu thoại: "tôi/Tôi" 1 dòng (1617, đúng — chỉ sai từ "cháu" làm chủ thể), "anh/Anh" tự xưng 9 dòng (tất cả sai), "cháu" 4 dòng (đúng, với thầy Akai), "em" gọi người khác 6 dòng (1706, 1732, 1840, 1871, 1961, 2056 — 2056 người được gọi không rõ nên không tính vào tally).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 4 lần (1706, 1732, 1840, 1961) vs "cô" 0 lần — cộng dồn P01 + P09–16 + file này: "cô" 43 vs "em" 34. 湯医 "Yui" 1 lần (2104), "Yunoi" 0 lần. 帝鉄 dạng trần "Teitetsu" 1 lần (2104). 宮司 dùng "thầy"/"thầy tế". "KiHa" 4 gloss, "Kiha" 0. Đã kiểm tra và không tính sai: 1816 "(gỗ)" thừa nhưng vô hại; 1710 オウム (VN "vẹt" theo JP, TW đọc nhầm thành 千); 1829 福丘 "Fukuoka" theo furigana ふくおか; ký tự lạ trong JP của CSV3 tại 2105, 2394 (TOML-2 sạch — lỗi hiển thị CSV).
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (41/41 đúng, 0 bị loại). Tổng 31 file đã audit: 1.949 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41). File audit: audit-paulette02-old-map-REVIEW.md (khối TOML parse 41/41), audit-paulette02-old-map-wrong.json (41 mục).

## Paulette 02_解放b寝台 (19/11/2026) — 49/421 sai (11,6%), 0 dòng chưa chắc chắn; TRÀN CHƯƠNG HAI CHIỀU đầu tiên của dự án (obasan ↔ sleeper, 19 dòng)
- Lệch vị trí 19 (1624, 1712, 1760, 1797, 1807, 1892, 2053, 2432, 2450, 2459, 2519, 2531, 2570, 2584, 2646, 2662, 2681, 2684, 2688 — tất cả đều mang bản Việt của obasan; 17/19 khôi phục được từ key obasan tương ứng: 1680, 2637, 2017, 2277, 1704, 2265, 1583, 1628, 1961, 1682, 1830, 2517, 2478, 2503, 2563, 1809, 2466 — cả 17 key nguồn đều đã nằm trong danh sách 255 dòng sai của audit obasan, nên sửa hai file sẽ khớp nhau; 1712 sửa 1 từ trong bản khôi phục ("phần thưởng" → "bữa ăn", người dịch lẫn ごちそうさまでした với ご褒美 1624); chỉ 1892 và 2684 phải dịch mới), xưng hô 16 dòng (Soutetsu tự xưng "anh" trong thoại: 1222, 1240, 1248, 1604, 1623, 1833, 1887, 1920, 1961, 2036, 2037, 2082, 2095 — 13/13 lần tự xưng, 0 lần "tôi"; 1614 gọi Hikari "em" → "con"; độc thoại "mình" chủ ngữ độc lập: 2339, 2590), thuật ngữ 5 (回数券 "vé tháng" → "vé lượt": 1819, 1832, 2560 — TW 多次票 xác nhận; "Ohito" → Ohitoyo: 1931, 1946), sai nghĩa 3 (1636 tự bịa thêm "chọn" vào câu dở dang của JP; 2389 誘導 "dụ dỗ" → "dẫn dắt"; 2446 sai thì/quá khứ giả định), lỗi nhỏ 5 (mất tiếng hít っ 1779; はぅう "Hả." → "Hau." 1781; lỗi đánh máy "đối đối phó" 2081; thừa 」 2402; SFX ゴーーーーーっ "Xình xịch" → "Ù ù ù ù" 2690).
- Thoại sai 29/273, lời dẫn sai 19/148. Theo người nói: Soutetsu 19, lời dẫn 19, Paulette 7, Hikari 3.
- **Tràn chương HAI CHIỀU obasan ↔ sleeper (19 dòng), 0 chuỗi xoay vòng trong file, 0 dòng mồ côi:** trường hợp tràn chương thứ ba của dự án, và là trường hợp đầu tiên hai chiều — 17 dòng obasan mang bản dịch đúng của các dòng sleeper này (đã xác minh bằng đọc JP/TW tại obasan, không chỉ tra chỉ mục). Đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục). Heuristic bắt được 10/19 dòng lệch (1624, 1797, 2432, 2450, 2459, 2519, 2531, 2646, 2662, 2681); 9 dòng còn lại có dấu thoại/lời dẫn trùng JP. Không có dòng CSV trống nào; VN==TW 0.
- Không key-shift sạch (shift 0: 411/421). TOML và CSV giống hệt nhau về nội dung (166 dòng khác chỉ ở `\n`/khoảng trắng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 14 thẻ (7 dòng thêm gloss mà JP không có — cùng quy ước file stove, cả 7 gloss đều dịch đúng: 検札鋏 → "kìm soát vé", 蒸気機関車 → "đầu máy hơi nước", 喚呼 → "hô xác nhận") — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 6 dòng — 4 dòng đúng (sở hữu/phản thân/thành ngữ), 2 dòng sai là chủ ngữ độc lập (2339, 2590). Soutetsu thoại: "tôi/Tôi" 0 lần, "anh/Anh" tự xưng 13 dòng (tất cả sai), "em" 15 lần (13 lần gọi Paulette, 1 lần gọi Hikari 1614 — sai, 1 lần gọi Reina 2002 — đúng).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 13 lần (1248, 1623, 1627*, 1669, 1809, 1820, 1833, 1887, 1907, 1939, 2036, 2052, 2080 — *1627 người được gọi chưa rõ Paulette hay Hikari) vs "cô" 0 lần — cộng dồn toàn dự án: "cô" 43 vs "em" 47, **"em" lần đầu vượt "cô"**. 駿袋鉄道 "Đường sắt Suntetsu" 1 lần (1966 — khác đề xuất "Suntai"). とき鉄 "Tokitetsu" (1928), 津っ鐵 "Tsuttetsu" (1829, theo ruby つってつ). "KiHa" 1 gloss, "Kiha" 0. 湯医 0 lần; 帝鉄 JP 1× (1925 "Đế Thiết"). Đã kiểm tra và không tính sai: 1627 người được gọi chưa rõ (ghi chú để Hieu quyết); 2038 定期券 "vé định kỳ"; 2080 印籠 "hộp ấn"; 2381 câu trích trực tiếp bịa thêm nhưng giữ đúng nghĩa; ký tự lạ trong JP của CSV3 tại 2339 (TOML-2 sạch).
- **Đề xuất mới: thêm 回数券 → "vé lượt" vào glossary (context_trans.md)** — phân biệt với 定期券 = "vé định kỳ".
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (48/48 đúng, 0 bị loại). Tổng 32 file đã audit: 1.997 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41+48). File audit: audit-paulette02-sleeper-car-REVIEW.md (khối TOML parse 48/48), audit-paulette02-sleeper-car-wrong.json (48 mục).
- Chương 02 tuyến Paulette đã audit xong (41 + 48 = 89 dòng sai trên 806 dòng, 11,0%). Còn lại trong 03_Paulette: h1–h8 (8 file), lr_h1/lr_h2/lr_稀咲h1/れいな02 (4 file).

## Paulette h1_ファーストセックス (19/11/2026) — 51/298 sai (17,1%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở xưng hô hệ thống + tên trần lần đầu bùng phát
- Xưng hô 28 dòng (Soutetsu tự xưng "anh" trong thoại: 1103, 1098, 1149, 1120, 1134, 1066, 1133, 1084, 1089, 1095, 1138, 1102 — 12/12 lần tự xưng, 0 lần "Tôi"; suy nghĩ dùng "Mình" làm chủ ngữ độc lập: 1727; Paulette gọi Soutetsu bằng tên trần trong câu nói → "anh Soutetsu": 1036, 1044, 1047, 1052, 1053, 1081, 1111, 1123, 1139, 1145, 1169, 1176, 1178, 1182, 926 — 15 dòng; 12 dòng tên rên giữ nguyên theo ngoại lệ: 1002, 1022, 1057, 1106, 1109, 1157, 1167, 1181, 1183, 1184, 1185, 1186), thuật ngữ 1 (1483 "Ohimitera" → Ohitoyo), sai nghĩa 3 (1106 tự bịa "đi anh!"; 1157 "em ấy" sai ngôi → "em"; 1065 tự bịa "ngập tràn rồi" + "phá" → "phà"), lỗi nhỏ 9 (mất tiếng hít っ: 1007, 988, 983, 1008, 995; chữ っ còn sót trong bản Việt: 984; tiếng thở ふぁ thành động từ "phá": 987, 976; mất gasp cuối sau dấu ~: 1015 — do đợt quét gasp っ phát hiện khi rà soát chéo).
- Thoại sai 40/143, lời dẫn sai 1/155. Theo người nói: Soutetsu 19, Paulette 21, lời dẫn 1.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục); không có bản Việt nào trên 20 ký tự trùng với file khác. Các bản Việt trùng trong file: "「!」" 1007/988/983 (JP đều 「っ！」, cả 3 đều sai cùng lỗi mất tiếng hít); "「A——」" 1005/996 (JP 「っ――」/「あんっ――」, đều đúng). Heuristic (dấu thoại ↔ lời dẫn): shift 0 đạt 298/298 = 1,000; các shift khác 0,980–0,990 — không có key-shift sạch. Không có dòng CSV trống nào; VN==TW 0.
- TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất; 156 khác biệt thô chỉ ở `\n`/khoảng trắng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 0 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 5 dòng — tất cả đều đúng (sở hữu/phản thân/thành ngữ). Soutetsu thoại: "tôi/Tôi" 0 lần, "anh/Anh" tự xưng 12 dòng (tất cả sai). "mình" ở CHAR 双鉄H 4 dòng: 1103 (phản thân, đúng), 1742 (sở hữu phản thân, đúng), 1727 (chủ ngữ độc lập, sai), 1732 (sở hữu phản thân, đúng).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 4 lần (1038, 1103, 1134, 1089) vs "cô" 0 lần — cộng dồn toàn dự án: "em" 51 vs "cô" 43. 御一夜 "Ohimitera" 1 lần (1483, đã sửa), "Ohito" 0, "Ohitoyo" 0. Không có 湯医/帝鉄/コン trong file.
- **Quy tắc mới (đề xuất, cần Hieu duyệt): tên trần vs tên rên** — Paulette gọi Soutetsu bằng tên trần trong câu nói hoàn chỉnh là sai → "anh Soutetsu"; tên rên độc lập/kèm tiếng rên trong lúc thân mật giữ nguyên. P16 còn 3 dòng tên trần chưa được tính sai (2008, 2015, 2016) — đưa vào đợt thống nhất sau. **Đề xuất thứ hai: tiếng thở fa/fu** (ふぁ/ふあ/ふぇ → "phà"/"phù"/"phê"/"phùa", không phải động từ "phá", không để nguyên dạng La-tinh) — bằng chứng h1 3 dòng + h2 6 dòng.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (40/40 đúng, 0 bị loại; bổ sung 1 dòng từ rà soát chéo với đợt quét gasp っ — 1015, kiểm tra lại 1/1 đúng — tổng 41/41, 0 bị loại). Rà soát chéo với sweep: sweep xác nhận 5/6 bản sửa gasp っ của audit (1007, 983, 984, 988, 995 — cùng giá trị sửa); dòng 1008 (「っっ！！？」 → "ƯƯ!!?") không có trong danh sách sweep, bản sửa của audit giữ nguyên. Tổng 33 file đã audit: 2.048 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41+48+51). File audit: audit-paulette-h1-first-sex-REVIEW.md (khối TOML parse 51/51), audit-paulette-h1-first-sex-wrong.json (51 mục).

## Paulette h2_制服変更？ (19/11/2026) — 47/292 sai (16,1%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở xưng hô hệ thống + SFX tiếng thở không nhất quán
- Xưng hô 28 dòng (Soutetsu tự xưng "anh" trong thoại: 1073, 1040, 1017, 1060, 1127, 1111, 891, 1655, 894, 1072, 1082, 960, 1059, 1051, 1055 — 15/15 lần tự xưng, 0 lần "Tôi"; độc thoại dùng "anh": 1253, 1427; Paulette gọi Soutetsu bằng tên trần trong câu nói → "anh Soutetsu": 925, 900, 1120, 1130, 1061, 1114, 1014, 1129, 948, 1031, 1046 — 11 dòng; 8 dòng tên rên giữ nguyên theo ngoại lệ: 1000, 1009, 1096, 1128, 1001, 950, 983, 995), thuật ngữ 1 (889 "Ohimitera" → Ohitoyo), lỗi nhỏ 11 (mất tiếng hít っ cả dòng: 1004, 952; mất gasp cuối sau gạch/dấu ~: 1135, 950, 985 — cả 3 do đợt quét gasp っ phát hiện khi rà soát chéo; tiếng thở ふぁ/ふぇ/ふや dịch sai: 956 "phu/phúa", 957 "Phu/fuyahaaa", 923 "fuaaaaaaaaaaan", 963 "Afuuuuuuuuuuun", 932 "phá", 991 "phá").
- Thoại sai 38/140, lời dẫn sai 2/152. Theo người nói: Soutetsu 18, Paulette 20, lời dẫn 2.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục). 7 bản Việt trên 20 ký tự trùng với file khác — tất cả đều là cụm ngắn/SFX/gasp dùng chung ("Có vẻ, là vậy nhỉ." 1087; "Sao vậy? Paulette." 1048; "（Rào rào rào rào rào）" 1672/1642; "（Phụt! Phụt! Phụt! Phụt!）" 1636/1634; "Ưm hyuuuuuuuuuuuuuu!!!" 1021) — không phải tràn chương. Heuristic (dấu thoại ↔ lời dẫn): shift 0 đạt 292/292 = 1,000; các shift khác 0,986–0,993 — không có key-shift sạch. Không có dòng CSV trống nào; VN==TW 0.
- TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất; 135 khác biệt thô chỉ ở `\n`/khoảng trắng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 0 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 9 dòng — tất cả đều đúng (sở hữu/phản thân/thành ngữ "tự mình"). Soutetsu thoại: "tôi/Tôi" 0 lần, "anh/Anh" tự xưng 15 dòng (tất cả sai). "mình" ở CHAR 双鉄H 1 dòng: 1127 (mệnh đề lồng, phản thân, đúng).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 6 lần (1119, 903, 1655, 894, 1082, 960) vs "cô" 0 lần — cộng dồn toàn dự án: "em" 57 vs "cô" 43 ("Em ấy" tại 1040 là Hibiki, không tính). 御一夜 "Ohimitera" 1 lần (889, đã sửa), "Ohito" 0, "Ohitoyo" 0. Không có 湯医/帝鉄/コン trong file. **1135 — đảo quyết định:** lúc đầu không tính sai (cho rằng ~~~ đã là tiếng rên), nhưng rà soát chéo với đợt quét gasp っ cho thấy JP kết bằng ～っ và TW có 啊 — mất gasp cuối theo quy tắc B2 — đã chuyển sang danh sách sai.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (37/37 đúng, 0 bị loại; bổ sung 3 dòng từ rà soát chéo với đợt quét gasp っ — 1135, 950, 985, kiểm tra lại 3/3 đúng — tổng 40/40, 0 bị loại). Rà soát chéo với sweep: sweep xác nhận 2/2 bản sửa gasp っ của audit (1004, 952 — cùng giá trị sửa). Tổng 34 file đã audit: 2.095 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41+48+51+47). File audit: audit-paulette-h2-uniform-change-REVIEW.md (khối TOML parse 47/47), audit-paulette-h2-uniform-change-wrong.json (47 mục).
- Hai file h1+h2 cộng lại sai 81/590 dòng (13,7%). Còn lại trong 03_Paulette: h3–h8 (6 file), lr_h1/lr_h2/lr_稀咲h1/れいな02 (4 file).

## Paulette h3_誘惑アイスコーヒー (19/11/2026) — 69/279 sai (24,7%), 1 dòng chưa chắc chắn (1683); file lệch vị trí nặng nhất trong các file Paulette h, chuỗi xoay vòng nội bộ 45 dòng
- Lệch vị trí 45 dòng (38 phục hồi trong file theo 6 chuỗi + 1 nhánh + 1 dòng riêng lẻ: chuỗi A 15 mắt đầu 1676, chuỗi B 10 mắt đầu 1641 nhánh 1642←919, chuỗi C 4 mắt đầu 1673, chuỗi D 2 mắt đầu 1682, chuỗi E 2 mắt đầu 982, chuỗi F 2 mắt đầu 1461 nhánh 899←1650←872; 7 dịch mới: 982, 1461, 1641, 1658, 1673, 1676, 1682), xưng hô 18 (Soutetsu tự xưng "anh" 15/15 lần, 0 lần "Tôi"; tên trần 986, 1016, 1071), thở gấp 6 (907, 908, 934, 935, 954, 1639 — 4 do sweep bắt được).
- Thoại sai 41/122, lời dẫn sai 28/157. Theo người nói: độc thoại 28, Soutetsu H 26, Paulette 15.
- **Chuỗi xoay vòng nội bộ thứ tư của dự án (45 dòng, 38 phục hồi trong file); 7 bản Việt mồ côi không có JP trong file (VN tại 703, 899, 1052, 1062, 1488, 1642, 1658) — nguồn ngoài file chưa tra.** Heuristic (dấu thoại ↔ lời dẫn): shift 0 đạt 246/279; 12 dòng lệch cùng loại chỉ tra chỉ mục Việt mới tìm ra. Không có bằng chứng tràn chương từ file khác. Không có dòng CSV trống nào; VN==TW 0.
- TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất; 155 khác biệt thô chỉ ở `\n`/khoảng trắng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 0 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 5 lần — 1 lần (1359) nằm trong bản Việt lệch vị trí (đã sửa), 4 lần còn lại đều đúng (sở hữu/phản thân). Soutetsu thoại: "tôi/Tôi" 1 lần, "anh/Anh" tự xưng 15 dòng (tất cả sai). **Dòng chưa chắc chắn mới: 1683** (Soutetsu H, JP 僕 → VN "mình" ở cả hai vế; ứng viên: sửa "tôi" theo quy tắc Soutetsu "Tôi" vs giữ "mình" vì là giọng nghĩ thầm).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 8 lần (705, 980, 999, 1006, 1034, 1045, 1050, 1067) vs "cô" 0 lần — cộng dồn toàn dự án: "em" 65 vs "cô" 43. 御一夜 "Ohimitera" 2 lần trong các dòng đúng (1255, 1347), "Ohito" 0, "Ohitoyo" 0. Không có 湯医/帝鉄/コン trong file. **Tinh chỉnh quy tắc tên trần vs tên rên:** 986 và 1071 không phải tên rên (câu nói hoàn chỉnh / câu hỏi mở đầu bằng cách gọi tên) — ngoại lệ "tên rên giữ nguyên" chỉ áp dụng cho tên rên trong lúc thân mật.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (69/69 đúng, 0 bị loại; trong kiểm tra lần hai đã sửa lại bản Việt phục hồi tại 1026 mang lỗi xưng hô gốc, 10 khoảng trắng thừa trước `\n`, 15 dấu 。 thay cho .). Rà soát chéo với sweep: sweep xác nhận 6/6 bản sửa gasp っ của audit (cùng giá trị sửa). Tổng 35 file đã audit: 2.164 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41+48+51+47+69). File audit: audit-paulette-h3-temptation-iced-coffee-REVIEW.md (khối TOML parse 69/69), audit-paulette-h3-temptation-iced-coffee-wrong.json (69 mục).

## Paulette h4_クリーム＆クリーム (19/11/2026) — 23/265 sai (8,7%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở tiếng thở La-tinh + xưng hô hệ thống
- Tiếng thở La-tinh 10 (859, 881, 882, 884, 901, 903, 911, 914, 952, 970 — họ âm きゃふ/ふにゃ/んきゅ/ふひゃ + lời ngọng), xưng hô 8 (Soutetsu tự xưng "anh" 8/8 lần, 0 lần "Tôi": 702, 853, 906, 973, 984, 998, 1021, 1207 — 4 do pronoun sweep bắt được), thở gấp 3 (941, 1030, 1632 — 1 do sweep bắt được), sai nghĩa 2 (1466 オコジョ "chồn hương"→"chồn trắng"; 1609 ぬぶ "Phập"→"Rút" — sai hướng).
- Thoại sai 20/110, lời dẫn sai 3/155. Theo người nói: Soutetsu H 8, Paulette 11, Soutetsu 1, độc thoại 3.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương.** Heuristic (dấu thoại ↔ lời dẫn): shift 0 đạt 265/265 = 1,000. Không có dòng CSV trống nào; VN==TW 0.
- TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất; 146 khác biệt thô chỉ ở `\n`/khoảng trắng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 0 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 4 lần — tất cả đều đúng (thành ngữ/sở hữu/phản thân: 1328, 1294, 1303, 1259). Soutetsu thoại: "tôi/Tôi" 1 lần, "anh/Anh" tự xưng 8 dòng (tất cả sai).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 5 lần (853, 863, 906, 984, 1021) vs "cô" 0 lần — cộng dồn toàn dự án: "em" 70 vs "cô" 43 (sửa số liệu: bản tóm tắt trước ghi h4 là 6 lần, đếm lại là 5 — 1207 là lời Paulette thuật lại, không phải Soutetsu gọi). 御一夜 0 lần. Không có 湯医/帝鉄/コン trong file. **Đề xuất mới: mở rộng quy tắc fa/fu** sang họ âm きゃふ/ふにゃ/んきゅ/ふひゃ; **quy tắc hướng SFX:** ぬぶ = rút ra, ずぶ = đâm vào.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (23/23 đúng, 0 bị loại; trong kiểm tra lần hai đã sửa lại 8 khoảng trắng thừa trước `\n`, 2 dấu 。 thay cho ., 3 âm ghép viết tách đã gộp lại). Rà soát chéo với sweep: sweep xác nhận 3/3 bản sửa gasp っ của audit (cùng giá trị sửa). Tổng 36 file đã audit: 2.187 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41+48+51+47+69+23). File audit: audit-paulette-h4-cream-and-cream-REVIEW.md (khối TOML parse 23/23), audit-paulette-h4-cream-and-cream-wrong.json (23 mục).
- Bốn file h1–h4 cộng lại sai 173/1.134 dòng (15,3%). Còn lại trong 03_Paulette: h5–h8 (4 file), lr_h1/lr_h2/lr_稀咲h1/れいな02 (4 file).

## Quét gasp っ toàn dự án (19/11/2026) — 1.146 dòng sửa / 210 file (sau §10: 1.147; §11 20/11 loại 1474 — っ nhấn mạnh, không phải gasp) (A: 318 dòng VN còn っ thô; B1: 381 dòng mất gasp cả dòng; B2: 416 dòng mất gasp cuối dòng + 11 dòng mất gasp giữa dòng; phụ lục §9 do parent rà soát: +16 dòng đa-っ — 3 gasp cả dòng + 13 gasp cuối dòng — mẫu B1/B2 chỉ bắt đúng 1 っ; đã kiểm tra lại từng dòng, 16/16 khớp); lần kiểm tra thứ hai đọc lại 1.126/1.126, loại 13 dòng (10 SFX đã dịch + 3 JP/TW mâu thuẫn), viết lại 8 dòng, bổ sung 11 dòng audit còn sót gasp (đã sửa lại trong 5 file audit: Grand 01 1519/2306/2338, Hibiki 03 1933/2433, Paulette 01 search 1947, 夜の嵐 2068/2334, obasan 1583/1590/2326 — khối đã parse lại, tổng số dòng sai các file không đổi); không sửa: 32 audit đã sửa, 136 VN đã diễn gasp bằng cách khác, 82 cần audit file, 4 chưa chắc chắn (+2 SFX đa-っ đã diễn: lr_日々姫h2 973, Paulette h7 896). Katakana sót: KHÔNG có từ katakana nào chưa dịch — 151 tag `%l` thiếu dấu `;` (+9 tag đóng sai dạng khác = 160 tag hỏng / 13 file, tập trung 真闇02 64, Paulette 11 54, Paulette 10 24). File: sweep-raw-gasp-REVIEW.md (210 khối TOML + 12 khối phụ lục, parse đúng), sweep-raw-gasp-wrong.json (1.399 mục).

## Paulette h5_裸エプロンのレモンドレッシング和え (19/11/2026) — 30/305 sai (9,8%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở xưng hô hệ thống + SFX
- Xưng hô 11 (Soutetsu tự xưng "anh" 10/10 lần trong thoại — 635, 839, 950, 961, 965, 976, 979, 984, 986, 1045 — chỉ có 2 lần "tôi" đúng trước khi sửa: 1718, 1634; "Anh" 1 lần trong độc thoại: 1401), SFX 8 (826 はうっ→"Hau!"; 942 ちゅむっ→"chụt"; 1023 びゅうびゅう bị bỏ mất; 1691 とんっ→"Cốc nhẹ!"; 1694 にゅぶうっ→"rútttt" — sai hướng; 1713 ぐいっ→"Giật mạnh!"; 1717 ぐいっ→"Thóp bụng!" — bịa theo TW; 1723 ちゅっ→"Chu"), thở gấp 5 (904, 905, 935, 953, 1228 — cả 5 sweep xác nhận cùng giá trị), tiếng thở La-tinh 5 (892 きゅう dài→"Siếttttttttt"; 932 くあっ→"Ư a!"; 947/949 んきゅ→"Ưm"; 980 ひゅいっ→"Huyi!"), sai nghĩa 1 (1290 我が身→"lý trí", phải là "thể xác").
- Thoại sai 22/136, lời dẫn sai 8/169. Theo người nói: Soutetsu 14, Paulette 8, độc thoại 8.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương.** VN trùng trong file (2 nhóm: `「!!!」` ×2, `「っ!」` ×3) đều hợp lệ — 1053 (JP `「！！！」` không có っ) đúng, 935 sai. Không có dòng CSV trống nào; VN==TW 1 (631, `「…………」` — đúng).
- TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất; 197 khác biệt thô chỉ ở `\n`/khoảng trắng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 0 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 6 lần — tất cả đều đúng (1365 "cửa mình"; còn lại sở hữu/phản thân). Soutetsu thoại: "tôi/Tôi" 2 lần, "anh/Anh" tự xưng 10 dòng (tất cả sai).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 8 lần (635, 836, 838, 839, 965, 972, 986, 1026) vs "cô" 0 lần — cộng dồn toàn dự án: "em" 78 vs "cô" 43 (1718 "em ấy" là ngôi thứ ba trong độc thoại, không tính). 御一夜 0 lần. Không có 湯医/帝鉄/コン trong file. **Quy tắc ちゅ-family:** ちゅっ/ちゅう/ちゅるっ/ちゅむっ/ちゅろっ đều → "chụt"; "chu" là dạng sót.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (30/30 đúng, 0 bị loại; bổ sung 1 dòng từ rà soát chéo — 942, kiểm tra lại 1/1 đúng — tổng 30/30). Rà soát chéo với sweep: sweep xác nhận 5/5 bản sửa gasp っ của audit (cùng giá trị sửa). **Bản sửa viết một dòng (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công** — theo quyết định 19/11 của Hieu; khác với h1–h4 vốn giữ `\n`. Tổng 37 file đã audit: 2.217 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41+48+51+47+69+23+30). File audit: audit-paulette-h5-apron-lemon-dressing-REVIEW.md (khối TOML parse 30/30), audit-paulette-h5-apron-lemon-dressing-wrong.json (30 mục).

## Paulette h6_あなたとふたりの学園エッチ (19/11/2026) — 36/304 sai (11,8%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở xưng hô hệ thống + thở gấp
- Xưng hô 12 (Soutetsu tự xưng "anh" 12/12 lần trong thoại — 738, 740, 866, 879, 885, 899, 900, 903, 909, 924, 935, 946 — chỉ có 1 lần "tôi" đúng trước khi sửa: 1574; độc thoại 0 lần sai), thở gấp 11 (774, 790, 814, 815, 816, 817, 819, 850, 1271, 1290, 1377 — 8 sweep xác nhận cùng giá trị; 1271 audit sửa lại giá trị sweep: 1 Ư → 2 Ư vì JP có 2 っ; 784 audit mở rộng giá trị sweep: thêm わらひ→"ehm"; 815 và 850 là sweep bỏ sót), tiếng thở La-tinh 6 (768 きゅ-squeal dài→"Kíuuuuuuuuun"; 769 きゃふっ→"Kyaphù"; 770 ひゃふっ→"Hyafu"; 800/818 くぁ/くあ→"Ư a"; 869 んきゅんっ→"Ưm!"), SFX 5 (840, 847, 856: ちゅるっ/ちゅむっ/ちゅう→"chu", phải là "chụt"; 868 んきゅっっ→"Ư a", phải là "Ưm"; 1586 ずっ→"Trượt" — sai hướng, phải là "Phập"), lời ngọng 2 (784 わらひ→"ehm"; 835 ひっへふははひ→"Hí-hề-phù-ha-ha-hí", ほーへふ→"Hôu-hê-hu").
- Thoại sai 32/142, lời dẫn sai 4/162. Theo người nói: Soutetsu 19, Paulette 13, độc thoại 4.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương.** VN trùng trong file (2 nhóm: `「Ư——」` ×2 — 803 JP `「ぅっ――」`, 771 JP `「っ――」`, cùng diễn "Ư" là chấp nhận được; `（Siết chặt!!!）` ×2 — 1566/1577, cùng kiểu siết) đều hợp lệ. Không có dòng CSV trống nào; VN==TW 0.
- TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất; 167 khác biệt thô chỉ ở `\n`/khoảng trắng).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 0 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 7 lần — tất cả đều đúng (1271 "giật nảy mình", 1605 "Rùng mình" là cụm động từ; còn lại sở hữu/phản thân). Soutetsu thoại: "tôi/Tôi" 1 lần, "anh/Anh" tự xưng 12 dòng (tất cả sai).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 6 lần (735, 740, 892, 903, 914, 935) vs "cô" 0 lần — cộng dồn toàn dự án: "em" 84 vs "cô" 43 (**đính chính:** bản tóm tắt trước ghi h6 là 8 lần, đếm lại chính xác bằng script là 6 — các lần "em"/"em ấy" trong độc thoại là ngôi thứ ba, không tính). 御一夜 0 lần. 帝大 1163 → "Đại học Đế quốc" (đúng — tên trường, không phải 帝鉄). Không có 湯医/帝鉄/コン trong file. **Quy tắc gasp nhiều っ:** một Ư cho một っ, Ư dính ngay sau âm nó thuộc về (1271, 850).
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (36/36 đúng, 0 bị loại). Rà soát chéo với sweep: sweep có 11 mục trong file (833 là "already-rendered", không phải bản sửa — audit đồng ý, không đưa vào danh sách); 8/10 bản sửa gasp của audit được sweep xác nhận cùng giá trị; 1 sửa lại giá trị sweep (1271), 1 mở rộng giá trị sweep (784); audit tìm thêm 2 gasp sweep bỏ sót (815, 850). **Bản sửa viết một dòng (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công** (như h5). Tổng 38 file đã audit: 2.253 dòng sai (133+255+299+374+199+2+20+12+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41+48+51+47+69+23+30+36). File audit: audit-paulette-h6-school-etch-REVIEW.md (khối TOML parse 36/36), audit-paulette-h6-school-etch-wrong.json (36 mục).
- Sáu file h1–h6 cộng lại sai 239/1.743 dòng (13,7%). Còn lại trong 03_Paulette: h7–h8 (2 file), lr_h1/lr_h2/lr_稀咲h1/れいな02 (4 file).

## Paulette h7_残業エッチもyシャツで (19/11/2026) — 24/326 sai (7,4%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở thở gấp/SFX
- Xưng hô 3 (Soutetsu tự xưng "anh" 2/6 lần trong thoại — 959, 969; chỉ có 4 lần "tôi" đúng trước khi sửa; Paulette tự xưng "tôi" 1 lần — 977, phá vỡ quy ước "em" 15 lần trong file), thở gấp 8 (816, 912, 1233, 1270, 1271, 1285, 1331, 1380 — 6 sweep xác nhận cùng giá trị, 1270 là phụ lục đa-っ; 816 sweep ghi needs-file-audit, audit tự giải quyết; 912 sweep bỏ sót), tiếng thở 6 (818 ひゃふっ→"hya", 821/899 きゃふっ→"kya" — mất ふ; 834/918 んきゅんっ→"Ưm kyun", 921 んきゅっ→"Ưm kyu"), SFX 6 (826/860 tiếng ré dài きゅ bị để phiên âm La-tinh; 894 ずりゅりゅ→"chụt" thay vì "rột"; 895 れるっ→"Liếm" thay vì "rộp"; 1651/1684 âm dài bị dịch gọn, mất độ dài), khác 1 (861 おっと→"Ốp").
- Thoại sai 17/152, lời dẫn sai 7/174. Theo người nói: Soutetsu 4, Paulette 13, độc thoại 7.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương.** VN trùng trong file (6 nhóm) đều hợp lệ — `「Ưm」` ×2 (859 JP `「んぷっ」`, 917 JP `「む」`), `「Ưm!」` ×2 (922, 839), `（Phụt! Phụt! Phụt! Phụt!）` ×3 (1659/1660/1662), `「Đúng vậy」` ×2 (976/979), `（Cộp!）` ×2 (1648/1665), `（Phập! Phập! Chụt! Chụt!）` ×2 (1649/1650). Chỉ số VN toàn dự án: 41 dòng trùng file khác đều là câu ngắn/SFX chung — không tràn chương; 1684 trùng h6 1591 nhưng JP khác (h6 là ずんっ ngắn, đúng ở đó); 861 trùng h8 2179 (cùng JP おっと — lỗi tương tự chờ audit h8). Không có dòng CSV trống nào; VN==TW 1 (562 `「…………」` — đúng).
- TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 0 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 3 lần — tất cả đều đúng (1334, 1266, 1400). Soutetsu thoại: "tôi/Tôi" 4 lần, "anh/Anh" tự xưng 2 dòng (tất cả sai).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 1 lần (907) vs "cô" 5 lần (560, 953×2, 954, 1015) — cộng dồn toàn dự án: "em" 85 vs "cô" 48 — **lần đầu tiên một file h nghiêng về "cô" kể từ Paulette 02**. 御一夜 0 lần. Không có 湯医/帝鉄/コン trong file. **Đề xuất mới: quy tắc độ dài âm SFX** (âm dài JP phải kéo dài tương ứng trong VN; tiền lệ 1700/1701). Ghi chú: 897 はうっ→"Hau" KHÔNG sửa (JP không có "!", toàn dự án "Hau" 9× vs "Hau!" 4×).
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (24/24 đúng, 0 bị loại). Rà soát chéo với sweep: sweep có 10 mục trong file (6 bản sửa — audit xác nhận cùng giá trị 6/6; 3 already-rendered — audit đồng ý 879/896, 899 sửa thêm lỗi きゃふ; 1 needs-file-audit — audit tự giải quyết 816); audit tìm thêm 1 gasp sweep bỏ sót (912). **Bản sửa viết một dòng (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công** (như h5/h6). Tổng 39 file đã audit: 2.312 dòng sai (133+255+299+374+201+2+20+44+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41+49+51+47+69+23+30+36+24) — đính chính 19/11: tổng cũ 2.260 thiếu 1 (khối bổ sung 2976 của ムナカタ来訪 chưa cộng) + 1 (sleeper 1627 → "con", quyết định B1) + 2 (夜の嵐 1929/2551 Kuu→Kon, quyết định B8) + 31 (thẻ gloss 機関士 ở ムナカタ来訪, quyết định 12).. File audit: audit-paulette-h7-overtime-etch-REVIEW.md (khối TOML parse 24/24), audit-paulette-h7-overtime-etch-wrong.json (24 mục).
- Bảy file h1–h7 cộng lại sai 263/2.069 dòng (12,7%). Còn lại trong 03_Paulette: h8 (1 file), lr_h1/lr_h2/lr_稀咲h1/れいな02 (4 file).

## Paulette h8_気動車の国のアリス (19/11/2026) — 147/649 sai (22,7%), 2 dòng chưa chắc chắn; file lệch vị trí nặng — mạng xoay vòng lớn nhất từ trước tới nay
- Lệch vị trí 86 (6 chuỗi xoay vòng: mega 30 mắt xích 2784→2227; B+10 19 mắt xích 2277→2376; C Alice 9 mắt xích 2270→2110; D 8 mắt xích 2776→3249; E 7 mắt xích 2571→2817; F váy 13 mắt xích 2185→2608 — tất cả đều thu hồi được bản dịch đúng trong file; 6 đầu chuỗi dịch mới: 2784, 2277, 2270, 2776, 2571, 2185; 5 VN cũ là bản dịch mồ côi không có JP nào trong dự án: 2110, 2608, 3249, 2376, 2817; VN cũ của 2227 "Hự" là bản trùng của 2146). 3114 xác nhận lệch vị trí (như P12 đã cảnh báo). Xưng hô 36 (Soutetsu tự xưng "anh" 36 dòng trong thoại — 1513, 1516, 2047, 2080, 2089, 2327, 2329, 2338, 2343, 2421, 2474, 2489, 2504, 2512, 2517, 2518, 2520, 2524, 2529, 2530, 2552, 2554, 2559, 2586, 2614, 2661, 2686, 2693, 2695, 2751, 2764, 2783, 2788, 2794, 2798, 2800 — 4 dòng trong số đó chỉ bắt được bằng quét máy tính: 2794, 2693, 2089, 2764; độc thoại 0 lần sai), tiếng thở La-tinh 11 (2132 ひゅあ→"Híua…an" 15 a; 2136 ひあ→"Hya" sai âm, phải là "Hia"; 2137 ひゃう→"Hiau"; 2139 きゃふ→"Kyaphù"; 2142 きゅ→"Kíu"; 2187 んひゃう→"hiau"; 2241 はきゅ→"Hakíu"; 2286/2365 よいしょ→"yôi-zo"/"Yôi-zo"; 2304 んゆ→"iu"; 2413 んひゅ→"hiu"), thuật ngữ 6 (Ohimitera→Ohitoyo: 2125, 2300, 2314, 2436, 2566, 2647 — cộng 2695 trong nhóm xưng hô, tổng 7 lần), sai nghĩa/lỗi đánh máy 5 (2158 đảo thứ tự 亀頭/なか; 2179 おっと→"Ốp", phải là "Ối" theo tiền lệ h7 861; 2416 はぁっ→"nhà", phải là "Hà"; 2462 福岳→"Fukuoka", phải là "Fukutake"; 3214 卵子→"buồng trứng", phải là "trứng"), thở gấp 3 (2208 bỏ mất ぐっ; 2307 đếm thiếu 1 tiếng ん, 3→4 "Ưm"; 2360 ふふっ→"Fufu", phải là "Ư hự").
- Thoại sai 108/397, lời dẫn sai 39/252. Theo người nói: Soutetsu 62, Paulette 46, độc thoại 39. Lệch vị trí theo người nói: Soutetsu 18, Paulette 30, độc thoại 38.
- **0 tràn chương.** Tất cả 86 dòng lệch đều giải quyết trong file. VN trùng trong file (3 nhóm) đều đã giải thích: 2146/2227 "Hự" (2227 sai); 2148/2253 "!!?" (cả hai là dòng gasp của sweep); 2147/2825 "!" (2147 là bản sửa sweep, 2825 đúng). Không có dòng CSV trống nào; VN==TW 0.
- TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 0 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 0 lần sai (chỉ có 2 dòng chưa chắc chắn 3087/3726 — xem dưới). Soutetsu thoại: "anh/Anh" tự xưng 36 dòng (tất cả sai).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 12 lần (2489, 2783, 2693, 2676, 2554, 2380, 2381, 2717, 2517, 2529, 2751, 2437) vs "cô" 0 lần — cộng dồn toàn dự án: "em" 97 vs "cô" 48 (2629 bị loại — VN cũ của nó là dòng Paulette đang bị thay thế; 2753 là "sô-cô-la" dương tính giả; 2273 là "cô ấy" ngôi thứ ba). 湯医: dạng thứ ba "Yunosaka" 12/12 lần (2085, 2314, 2566, 2635, 2636, 2637, 2638, 2647, 2681, 2756, 2759, 2793); "Yui" 0; "Yunoi" 0 — 2635/2638 mang furigana [ゆのい] ủng hộ "Yunoi". 御一夜 7 lần, tất cả "Ohimitera" — đã sửa thành "Ohitoyo". Không có 帝鉄/コン/KiHa/マスコン/宮司/整備体/運転ボディ/駿袋/Migita/オコジョ trong file. Paulette gọi Soutetsu "cậu": 0 lần; tên trần "Soutetsu" trong câu nói: 0 lần. **Đề xuất mới: 福岳→"Fukutake" (chờ xác nhận); quy ước "rộp" cho họ れる/るっ/れろ (chỉ ぺろ→"liếm"); おっと→"Ối" (theo tiền lệ h7 861).** Ghi chú: 髑国→"Đức" là ĐÚNG (quy ước thế giới hư cấu: 冥国=Mỹ, 詠国=Anh, 髑国=Đức, 仲国=Trung Quốc).
- 2 dòng chưa chắc chắn 3087 và 3726 — ĐÃ QUYẾT 19/11 (Hieu): giữ "mình" (độc thoại nội tâm tự vấn cảm xúc của Soutetsu — ngoại lệ như h3 1683); 0 dòng chưa chắc chắn còn lại trong file.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (147/147 đúng, 0 bị loại, 1 được sửa trong lần hai: 2110 — "anh"→"tôi", lỗi xưng hô thừa hưởng từ dòng cho). Rà soát chéo với sweep: sweep có 8 mục trong file (7 bản sửa — audit xác nhận cùng giá trị 7/7, không xung đột; 1 already-rendered 2344 — audit đồng ý); audit tìm thêm 2 gasp sweep bỏ sót (2208, 2307). Lưu ý: con số "18 mục sweep" trong bản nháp là sai — 10 mục thuộc file Hachiroku h8, một file khác. **Bản sửa viết một dòng (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công** (như h5/h6/h7). Tổng 40 file đã audit: 2.468 dòng sai (133+255+299+374+201+2+20+44+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41+49+51+47+69+23+30+36+24+156) — đính chính 19/11: h8 147 → 156 (12 dòng "Yunosaka" → "Yunoi", quyết định 湯医; 3 trong số đó đã có trong khối sửa nên chỉ cộng thêm 9 mục mới).. File audit: audit-paulette-h8-alice-rail-car-REVIEW.md (khối TOML parse 147/147), audit-paulette-h8-alice-rail-car-wrong.json (147 mục).
- Tám file h1–h8 cộng lại sai 436/2.718 dòng (16,0%). Còn lại trong 03_Paulette: lr_h1/lr_h2/lr_稀咲h1/れいな02 (4 file).

## Paulette lr_稀咲ポーレットh1_悪い大人の契約 (19/11/2026) — 85/488 sai (17,4%), 0 dòng chưa chắc chắn; file h sạch về cấu trúc, lỗi tập trung ở xưng hô + hơi thở fa/fu + thở gấp + độ dài SFX
- Xưng hô 21 (Soutetsu tự xưng "anh" 21 dòng trong thoại — 33 lần xuất hiện; "tôi" 0 lần trước khi sửa; độc thoại 0 lần sai), hơi thở 36 (ふぁ/ふあ 19 dòng "pha"/"Pha" không dấu — tất cả đều sai; はぁっ 4 dòng "Ha" thay vì "Hà"; SFX/thở dài 13 dòng — 6 dòng đếm thừa đúng gấp đôi 2599/2503/2608/2540/2500/2536 + 5 dòng đếm lệch âm a/u 1440/1441/1488/1619/1470 + 1586 ぬちゅっ "Nu chu"→"Nu chụt" + 1442 きゃふっ "Kya fu"→"Kyaphù" + 1642 はふぅ "ha phu"→"ha phù"), thở gấp 19 (13 sweep xác nhận cùng giá trị; 6 sweep bỏ sót 1596/1598/1902/2236/1567/1590 — 1598 có hai っ mà cả sweep lẫn phụ lục đa-っ §9 đều bỏ sót; 2236 sweep ghi needs-file-audit, audit tự giải quyết), sai nghĩa/lỗi đánh máy 8 (2232 ký tự Nhật sót "khóえ mắt"; 1386 dấu phẩy thừa; 1502 bịa thêm "có sao không"; 1644/1467/997 dấu phẩy sở hữu/xưng hô "của anh, Soutetsu"; 1712 わらひっ→"Ehm!"; 1580 Paulette gọi Kisaki "cậu"→"em"; 1802 ", cô" thừa), lệch vị trí 1 (1509 — VN cũ là bản sao y hệt VN của 1511, dịch mới từ JP).
- Thoại sai 72/280, lời dẫn sai 13/208. Theo người nói: 双鉄 30, ポーレット 29, 稀咲 13, độc thoại 13.
- **0 chuỗi xoay vòng, 0 tràn chương.** Chỉ 1 dòng lệch vị trí (1509). VN trùng trong file (2 nhóm) đều hợp lệ: 1509/1511 (1511 đúng); 2528/2495 （Phịch） cùng là tiếng ngã. Không có dòng CSV trống nào; VN==TW 3 (985, 1902, 964 — đều đúng).
- TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 0 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 15 lần — tất cả đều đúng. Soutetsu thoại: "tôi/Tôi" 0 lần, "anh/Anh" tự xưng 21 dòng (tất cả sai).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 1 lần (1700) vs "cô" 0 lần — cộng dồn toàn dự án: "em" 97 vs "cô" 48 (các lần "em" khác của Soutetsu trong file đều gọi Kisaki, không tính). Kisaki xưng hô theo đối tượng (em với Soutetsu, tôi với Paulette — không phải lỗi); Kisaki gọi Paulette "cô" 10 lần nhất quán, không sửa. ふふっ 6 dòng giữ "Fufu" (cười khúc khích) — MÂU THUẪN với tiền lệ h8 2360 ("Ư hự" trong cảnh H), cần Hieu chốt. Không có 帝鉄/湯医/コン (1484 くうっ là âm thanh, không phải tên)/KiHa/マスコン/宮司/整備体/運転ボディ/駿袋/Migita/オコジョ trong file. Paulette gọi Soutetsu "cậu": 0 lần; tên trần "Soutetsu" trong câu nói: 0 lần; tên rên đứng riêng: 0 lần.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (85/85 đúng, 0 bị loại). Rà soát chéo với sweep: sweep có 16 mục trong file (13 bản sửa — audit xác nhận cùng giá trị 13/13; 3 already-rendered — audit đồng ý); audit tìm thêm 6 gasp sweep bỏ sót. **Bản sửa viết một dòng (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công** (như h5–h8). File audit: audit-paulette-lr-kisaki-h1-REVIEW.md (khối TOML parse 85/85), audit-paulette-lr-kisaki-h1-wrong.json (85 mục).

## Paulette れいな02_れいなとポーレット (19/11/2026) — 26/419 sai (6,2%), 0 dòng chưa chắc chắn; file sạch nhất từ trước tới nay, 0 lệch vị trí/rotation/tràn chương
- Thuật ngữ 13 (Ohimitera→Ohitoyo 6 lần: 2068, 2668, 2165, 1636, 1666, 1813 — 1666 kèm "Yui"→"Yunoi"; 帝鉄 3 lần: 63 là lần đầu, dùng dạng đầy đủ "Đường sắt Đế quốc" trong thẻ %l, 2436/1900 "Teitetsu"; 冥国 3 lần phiên âm "Meikoku"→"Minh Quốc": 1777, 1169, 1158; タブレット 1 lần "thẻ bảng"→"máy tính bảng": 2657), xưng hô 6 (Soutetsu tự xưng "anh" 5 dòng: 2133, 1795, 1223, 1897, 1891; gọi Paulette "cô" 1 dòng: 2017→"Em"), thở gấp 3 (1948, 2199, 2388 — sweep xác nhận cùng giá trị 3/3; 0 sweep bỏ sót), thẻ %l tự thêm 3 (1171, 2721 gloss 改軌; 2160 gloss 8620 — gỡ thẻ theo tiền lệ 機関士; sau khi sửa VN còn 69 thẻ = JP), sai nghĩa 1 (1733 軌道 "khổ đường sắt đặc biệt"→"đường sắt đặc biệt").
- Thoại sai 17/261, lời dẫn sai 9/158. Theo người nói: 双鉄 10, độc thoại 9, れいな 2, 赤井宮司 2, ポーレット 1, 稀咲 1, ハチロク 1.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương.** VN trùng trong file (4 nhóm) đều hợp lệ: 1758/1753 「うむ」; 1810/1975 「はいですぅ」/「はぁい」; 2062/2061 「ね？れいな」; 1676/1689 「え？」. Không có dòng CSV trống nào; VN==TW 1 (1229 — đúng).
- TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 69 thẻ, VN có 72 thẻ (3 thẻ VN thừa — đã sửa) — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 17 lần — tất cả đều đúng. Soutetsu thoại: "tôi/Tôi" 7 lần (đúng), "anh/Anh" tự xưng 5 dòng (tất cả sai).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 0 lần vs "cô" 1 lần (2017, đã sửa) — cộng dồn toàn dự án: "em" 97 vs "cô" 49. 5 dòng "cô" quét máy tính tìm được đều không phải gọi Paulette (ngôi thứ ba "cô ấy"/"cô em gái" hoặc gọi Navi). KiHa 2 lần đã đúng; "đền chủ" 4 lần đã đúng; "Kon" 2707 đã đúng. Paulette độc thoại xưng "tôi"/"mình" lẫn lộn (câu ước "Giá như mình…") — biến thể phong cách, giữ nguyên.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (26/26 đúng, 0 bị loại). Rà soát chéo với sweep: sweep có 3 mục trong file (3 bản sửa — audit xác nhận cùng giá trị 3/3; 0 already-rendered); audit không tìm thêm gasp nào sweep bỏ sót. **Bản sửa viết một dòng (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công** (như h5–h8). Tổng 42 file đã audit: 2.579 dòng sai (133+255+299+374+201+2+20+44+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41+49+51+47+69+23+30+36+24+156+85+26). File audit: audit-paulette-reina02-REVIEW.md (khối TOML parse 26/26), audit-paulette-reina02-wrong.json (26 mục).

## Paulette lr_h1_家族旅行の最終日の夜 (19/11/2026) — 64/303 sai (21,1%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở hơi thở/âm thanh La-tinh + xưng hô
- Xưng hô 18 (Soutetsu tự xưng "anh" 18 dòng trong thoại; "tôi" 0 lần trước khi sửa; độc thoại 0 lần sai), nghĩa sai 1 (732 "họ sẽ…"→"chúng mình sẽ…" — Paulette nói về mình và Soutetsu), thở gấp 3 (1044, 1045 — mỗi dòng mất 1 tiếng っ, sweep ghi already-rendered nhưng audit không đồng ý; 1077 sweep BỎ SÓT — gasp đầu dòng `っ！――ポーレット`), hơi thở/âm thanh thoại 37 (họ lỗi lớn nhất: ちゅ/ぢゅ/じゅ/ず/れる/りゅ/れろ/にゅ còn La-tinh "chu"/"ju"/"rê ru"/"rê ryu"; 998 sweep "Kyufu"→audit "Kíuphù"; 1005 sweep "Hya"→audit "Hia"; 1083 sweep giữ La-tinh→audit Việt hoá toàn bộ; 1073–1075 あんっ→"An" giữ phụ âm mũi ん), âm thanh độc thoại 5 (1592 ぽっ→"Bụp"; 1610 ぐいっ→"Giật mạnh"; 1711 じゅぶううううっ→"Phậậậậập" 5 nguyên âm; 1716 "Trượt, dài"→"Trượt, trơn" bỏ "dài" bịa thêm; 1721 ずゅぶっぅぅっ→"Phậậập" 3 nguyên âm).
- Thoại sai 59/163, lời dẫn sai 5/140. Theo người nói: ポーレット 40, 双鉄 19, độc thoại 5.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương.** VN trùng trong file đều hợp lý (JP khác nhau): 「A」1068/1073, 「Ừ」1094/1175, 「Ưm!」1099/1102. Không có dòng CSV trống nào; VN==TW 1 (705 — đã sửa trong sweep gasp).
- TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 0 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: tất cả đều đúng (phản thân/sở hữu). Soutetsu thoại: "tôi/Tôi" 0 lần, "anh/Anh" tự xưng 18 dòng (tất cả sai). 979 không tính là lỗi xưng hô ("anh" là lời Paulette thuật lại).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 9 lần vs "cô" 0 lần — cộng dồn toàn dự án: "em" 106 vs "cô" 49 (96 sau h8; lr_稀咲h1 +1 "em" → 97; れいな02 +1 "cô" → 49; file này +9 "em"). Tên rên trần B4: 0 lần. Cười khúc khích La-tinh 3 dòng (1062 ehehe, 1088 fufu, 1181 ufufu) — đề xuất mới, cần Hieu chốt (h8 "Ư hự" là quy ước riêng file, không áp dụng). **Quy tắc độ dài âm kéo dài đã chốt: số nguyên âm VN = 1 (âm gốc) + số ký tự う/ぅ trong token JP** (bằng chứng h7 1651: う×10 → 11 chữ u; mọi token lr đều khớp). VN cũ trộn U+2015 (―, 366 lần) và U+2014 (—, 496 lần); bản sửa dùng U+2014 thống nhất.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (64/64 đúng, 0 bị loại). Kiểm tra lần hai sửa 5 bản sửa (1711: 6→5 nguyên âm; 1721: 4→3; 1042/1083/1089: ちゅうっ→"chụụt"). Rà soát chéo với sweep: sweep có 16 mục trong file (13 bản sửa — audit xác nhận giống hệt 10, thay thế 3 bằng bản đọc kỹ hơn: 998/1005/1083; 3 already-rendered — audit đồng ý 1016, không đồng ý 1044/1045); audit tìm thêm 1 gasp sweep bỏ sót (1077). **Bản sửa viết một dòng (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công** (như h5–h8). Tổng 43 file đã audit: 2.643 dòng sai (133+255+299+374+201+2+20+44+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41+49+51+47+69+23+30+36+24+156+85+26+64). File audit: audit-paulette-lr-h1-REVIEW.md (khối TOML parse 64/64), audit-paulette-lr-h1-wrong.json (64 mục).

## Paulette lr_h2_デコレーション＆ミルク (19/11/2026) — 69/333 sai (20,7%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở hơi thở/âm thanh La-tinh + xưng hô + thuật ngữ
- Xưng hô 23 (Soutetsu tự xưng "anh" 23 dòng trong thoại; "tôi" 0 lần trước khi sửa; độc thoại 0 lần sai), thuật ngữ 6 (Decoration/decoration 5 lần: 995, 1120, 1287, 1323, 1621 → "trang trí"; Ohimitera 1 lần: 1280 → "Ohitoyo"), hơi thở/âm thanh thoại 37 (1028 cả dòng còn nguyên La-tinh; ぺろ→"liếm nhẹ" theo quy ước riêng của file; 1133 こほっ "kho hộc" không phải từ Việt → "Khụ"; 1134 あちゅっ hắt hơi → "Hắt xì"; 1009/1124 mỗi dòng mất 1 tiếng gasp っ, sweep ghi already-rendered nhưng audit không đồng ý), âm thanh độc thoại 2 (1726 cả 4 âm còn La-tinh; 1735 ぽふっ "Bịch"→"Bụp" — tiếng mềm, không phải tiếng động mạnh).
- Thoại sai 65/204, lời dẫn sai 3/129. Theo người nói: ポーレット 36, 双鉄 29, độc thoại 3.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương.** Không có dòng CSV trống nào; VN==TW 0.
- TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 0 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: tất cả đều đúng. Soutetsu thoại: "tôi/Tôi" 0 lần, "anh/Anh" tự xưng 23 dòng (tất cả sai).
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 13 lần vs "cô" 0 lần — cộng dồn toàn dự án: "em" 119 vs "cô" 49. Tên rên trần B4: **1 lần — key 1079** (lần gọi đầu そうてつ、くん → "anh Soutetsu", lần sau rên trần "Soutetsu" — CHỈ GHI NHẬN, KHÔNG SỬA). Cười khúc khích La-tinh 8 dòng (1018, 1043, 1059, 1060, 1075, 1087, 1194, 1227, 1321) — đề xuất mới, cần Hieu chốt. くぅん chưa có dạng Việt thống nhất ("Kuuun" là dạng đang dùng; 1029, 1084) — câu hỏi mở mới. **1770 là bằng chứng mạnh nhất cho quy tắc độ dài âm: VN cũ "Đâm sâu uuuuuuuuuuu" (12 chữ u) ĐÃ ĐÚNG (JP う×11 → 1+11 = 12) nên bị loại khỏi danh sách sửa trong lần kiểm tra thứ hai** — tổng giảm từ 69 xuống 68. VN cũ dùng U+2014 (—, 656 lần) là chính, chỉ 30 lần U+2015.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (68/68 đúng; 1 dòng bị loại trong lần kiểm tra thứ hai: 1770 — VN cũ đã đúng). Kiểm tra lần hai sửa 5 bản sửa (1107: 3→2 nguyên âm, cả 2 vị trí; 1020/1105/1317/1319: ちゅうっ→"chụụt"/"Chụụt"). Rà soát chéo với sweep: sweep có 6 bản sửa trong file (1044, 1064, 1070, 1236, 1558, 1597 — audit xác nhận cùng giá trị 6/6, không trùng bản sửa audit); 4 already-rendered (1062, 1063, 1065, 1068 — audit đồng ý); audit không đồng ý already-rendered ở 1009/1124. **Bản sửa viết một dòng (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công** (như h5–h8). Tổng 44 file đã audit: 2.712 dòng sai (133+255+299+374+201+2+20+44+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41+49+51+47+69+23+30+36+24+156+85+26+64+69). File audit: audit-paulette-lr-h2-REVIEW.md (khối TOML parse 69/69), audit-paulette-lr-h2-wrong.json (69 mục).
- 03_Paulette đã audit xong toàn bộ (chương 01–16, Grand 04, h1–h8, lr_h1/lr_h2/lr_稀咲h1/れいな02).

- Đính chính 19/11 22:05 (quyết định của Hieu): tiếng thở/rên/cười dịch NGẪU HỨNG theo tính cách nhân vật + ngữ cảnh, KHÔNG dập khuôn 1:1 — các bảng SFX chỉ là gợi ý mặc định. 4 dòng h8 (2356/2360/2370/2402) sửa "Ư hự" → tiếng cười ("Ufufu"/"Fufu"); 2360 phân loại lại từ gasp → cười (tổng h8 vẫn 156). Mâu thuẫn ふふっ ở lr_kisaki đã giải quyết: giữ "Fufu". Docs đã cập nhật: sfx_and_emoticons.md §0 + §1.5, translation_guidelines.md §0.


**Đính chính B4 19/11 22:24 (Hieu ủy quyền Muse chốt):** ngoại lệ tên rên bãi bỏ — h1 41→51 (+10), h2 40→47 (+7), lr_h2 68→69 (+1); tổng dự án 2.694→2.712. B2 cũng đã chốt cùng lúc: old-map 1782 khóa "cậu".

## 00_Common file 03_ハチロクとナビ (19/11/2026) — 15/315 sai (4,8%), 0 dòng chưa chắc chắn; file sạch thứ ba toàn dự án, lỗi lẻ tẻ theo quyết định mới + xưng hô + rên っ
- Thuật ngữ 5 (帝鉄→Teitetsu 911/912; 御一夜→Ohitoyo 1200/1435/1506 — file còn 0 dòng Ohimitera), xưng hô 3 (Navi→Soutetsu "cô"→"anh" 1147 — "cô" cho Soutetsu chỉ xuất hiện đúng dòng này trong 148 dòng Navi nói toàn dự án; Soutetsu "mình" tân ngữ→"tôi" 1430/2025 theo tiền lệ pilot 1652), rên っ 4 (1273/1274/1323 theo sweep + 1309 sweep-missed: っ!? đứng một mình sau ――), SFX 1 (2106 mất tiếng cười ふふ → "khẽ bật cười"), nhỏ 1 (1358 "cú giáng trời giáng!"→"cú trời giáng!"), nghĩa 1 (1318 'còn nợ' theo TW — Hieu chốt 19/11 23:37).
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi, 0 dòng chưa dịch.** VN trùng lặp trong file: 0; JP trùng lặp: 0. 20 dòng Việt trùng với file khác đều là câu ngắn stock (うむ/ああ/なるほど…).
- TOML và CSV (bộ đúng) giống hệt nhau về nội dung (0 khác biệt thực chất; 211 dòng `\n` bị làm phẳng trong TOML). `# JP:` đủ 315/315 key script.
- **⚠️ CSV có HAI bộ dòng cho file này** (mẫu như lr_ふかみh2): bộ `01_Hachiroku\` khớp TOML 315/315 (khớp y hệt 104 + `\n`-phẳng 211), bộ `00_Common\` mồ côi (chỉ 24 khớp, 287 lệch VN, 48 lệch JP — bản cũ). Số dòng thực của file là **315, không phải 630**. Phải loại bộ mồ côi trước khi rebuild, nếu không 287 dòng đúng sẽ bị ghi đè bằng bản cũ. TOML chỉ có một bản duy nhất (md5 `5bb90d70f91d54136f8ec4b7b1290c5d`, không trùng lặp).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP = VN ở mọi dòng — **0 thẻ thiếu dấu `;` đóng**. Gloss 機関士 "người lái tàu" / 運転士 "nhân viên cơ vụ" (1638, 2108) giữ theo quy ước thiểu số đã chốt.
- "mình" trong độc thoại Soutetsu: 19 lần, chỉ 2 sai (1430, 2025 — tân ngữ); còn lại đều đúng (sở hữu/phản thân/mệnh đề phụ/thành ngữ, theo tiền lệ hearing 2151/2247/2248). Soutetsu thoại: "tôi" nhất quán, "anh" tự xưng 0 lần. "cô" cho Navi (1680, 2030, 2050) giữ theo cách dùng đã chốt (17× Soutetsu→Navi "cô" toàn dự án). "chị ấy" 1427/1577 = chị Mayami (xác nhận ở 1562 真闇姉).
- 0 dòng chưa chắc chắn: 1318 đã chốt theo Hieu (19/11 23:37) — hướng 'còn nợ' theo TW, đã thêm vào fix list (15 key).
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (14/14 đúng, 0 bị loại, 10 được sửa trong lần hai: bổ sung dấu 「」 bị thiếu ở 911/912/1147/1200/1309/1323/1358/1430/1435/1506); 1318 thêm sau theo quyết định của Hieu (23:37), parent kiểm chứng JP/TW. Rà soát chéo với sweep: sweep có 5 mục trong file (3 bản sửa nhận nguyên văn — 1273/1274/1323; 2 needs-file-audit 1547/2036 đã kiểm tra, không cần sửa) + 1 sweep-missed do audit tìm ra (1309).
- Fix list (15/15 key verified to parse, 0 lệch giá trị) saved at ~/workspace/maitetsu-pilot/audit-00common03-REVIEW.md and audit-00common03-wrong.json — NOT sent to Hieu (no-files rule).

**Tổng sau file này: 45 file / 2.727 dòng sai** (44 file / 2.712 trước file này + 15). Ghi chú cho người merge: một audit song song khác đang chạy cùng lúc — nếu file đó merge trước, cộng 15 vào tổng của nó thay vì con số này.

## 00_Common 02_共通02_日々姫と真闇と人形と (19/11/2026) — 33/467 sai (7,1%), 0 dòng chưa chắc chắn; file sạch về cấu trúc, lỗi tập trung ở xưng hô Soutetsu + thuật ngữ
- Xưng hô 13 (Soutetsu tự xưng "em" 8 dòng: 1872, 2064, 2167 nửa đầu, 2209 ×2, 2324, 2418, 2433, 2563 — đều sai người nghe; "tôi"→"anh" với Hibiki 2 dòng: 2162, 2163; "anh"→"tôi" với Mayami/Hachiroku 1 dòng: 1976; Hachiroku gọi Soutetsu "cô"→"ngài" 1 dòng: 2443; độc thoại "mình"→"tôi" 1 dòng: 2848 — tường thuật khách quan, không thuộc ngoại lệ tự vấn), thuật ngữ 7 (Ohimitera→Ohitoyo 5 dòng: 2135, 2201, 2413, 2495, 3009 — toàn bộ 5 chỗ trong file; gloss 帝鉄 "Đường sắt Hoàng gia"→"Teitetsu" 1 dòng: 2182; "Jussendo"→"Jutsu-sendo" 1 dòng: 2323), lỗi nhỏ 4 (2076 dấu phẩy thừa; 3184 khoảng trắng cuối; 3243 "!" thừa; 3247 thừa 1 "!"), sai nghĩa 3 (1880 転ぶぞ→"sắp ngã đấy?"; 2035 bịa phần kết cho câu cụt; 2695 "Hai chữ"→"Bốn chữ"), SFX 3 (2016 thiếu 1 nguyên âm; 2017 thừa 1; 2018 mất âm う), gasp 2 (1560, 2009 — っ sau tên riêng có thẻ %l, sweep bỏ sót), thẻ %l 1 (2693 — VN tự thêm gloss 杜氏, gỡ thẻ).
- Thoại sai 26/296, lời dẫn sai 7/171. Theo người nói: 双鉄 13, 日々姫 9, độc thoại 7, ハチロク 3, 真闇 1.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 nhiễm chéo, 0 VN trùng lặp.** Không có dòng CSV trống nào; VN==TW 0.
- **Nguồn dữ liệu — bẫy hai bộ CSV như lr_ふかみh2/共通03:** CSV3 liệt kê file này hai lần (467 dòng mỗi bộ). Bộ `00_Common` STALE (VN khớp TOML chỉ 31/467, JP lệch 214 dòng) — bỏ. Audit dùng bộ `02_Hibiki` (JP khớp comment TOML 467/467, VN khớp 466/467). TOML-2 chỉ có một file (md5 170e26e6b14a6decfb7f42fbd1ffe95d), không có bản sao trùng lặp. Số dòng thực là 467, không phải 934.
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 19 thẻ, VN có 20 thẻ (1 thẻ VN thừa — đã sửa) — **0 thẻ thiếu dấu `;` đóng**.
- "mình" trong độc thoại: 16 lần — 1 sai (2848, tường thuật khách quan), còn lại đúng (3008 tự vấn theo ngoại lệ; các "mình" phản thân/sở hữu đều đúng). Soutetsu thoại: "tôi" đúng chỗ, "anh" đúng với Hibiki, "em" không bao giờ đúng.
- Bằng chứng mới cho quyết định đang chờ: không có. B4 (tên trần "Soutetsu"): 2 lần xuất hiện — 1884 (giải thích từ nguyên tên, đúng), 1942 (tự giới thiệu, đúng) — Paulette không xuất hiện trong file.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (33/33 đúng, 0 bị loại; lần hai sửa 7 bản sửa: 2693, 2695, 2848, 3009, 3184, 3243, 3247 — bỏ dấu 「」 thêm thừa ở dòng độc thoại). Rà soát chéo với sweep: sweep có 5 mục trong file (2 bản sửa — audit xác nhận cùng giá trị 2/2: 2194, 2570; 3 needs-file-audit — audit kiểm chứng đúng, không sửa: 1942, 2592, 2894); audit tìm thêm 2 gasp sweep bỏ sót (1560, 2009). **Bản sửa viết một dòng (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công** (như h5–h8; ngoại lệ duy nhất: 2009 giữ `\n` trong khối TOML vì giá trị TOML gốc chứa `\n` dạng text — xem review). Tổng 46 file đã audit: 2.760 dòng sai (133+255+299+374+201+2+20+44+19+8+101+10+23+19+25+14+13+25+22+27+28+20+22+7+29+32+36+55+35+44+41+49+51+47+69+23+30+36+24+156+85+26+64+69+15+33). File audit: audit-00common02-REVIEW.md (khối TOML parse 33/33), audit-00common02-wrong.json (33 mục).
- 00_Common: còn 14 file chưa audit (01 đã làm pilot 35/155 — bản nháp, chưa chốt).

# ROUTE-AUDIT entry — 00_Common file 04 (共通04_キハ07。ポーレットとれいな)

- **File:** `00_Common/共通04_キハ07。ポーレットとれいな.txt.toml` — md5 `024224f6c52fa78e6dbec6b5f66ba881`, không có bản sao trùng.
- **Nguồn:** CSV3 bộ `03_Paulette` (385 dòng, khớp TOML 384/385; bộ `00_Common` là bộ cũ, chỉ khớp 15/385 — không dùng). Số dòng thật 385, không phải 770.
- **Kết quả: 19/385 dòng sai (4,9%)** — file sạch thứ tư của dự án (sau 実りの秋 0,4%, ヒヤリング 2,0%, 共通03 4,4%).
- **Phân loại:** thuật ngữ 6 (1791 gloss 枕木 'tàu vẹt', 2254 tag bịa 運転体 + 整備体 'thân chính', 2262 帝鉄, 2388 整備ボディ 'thân chính', 2558 tag bịa 整備体 + 'thân chính', 2658 Ohimitera), xưng hô 4 (2138, 2177, 2404, 2624 — Soutetsu gọi Hachiroku/Reina là 'cô' thay vì 'em'), sai nghĩa 4 (2154 câu cụt theo TW, 2393 JP thắng TW, 2534 lời hô 喚呼, 2591 lặp lại cách đọc 'Toumen?'), rên っ 2 (2676, 2677 — sweep lost-gasp-whole), nhỏ 3 (2098 thiếu 1 lần lặp, 2329 thiếu dấu phẩy, 2966 tự thêm ngoặc).
- **Cấu trúc:** 0 lệch dòng, 0 chuỗi xoay, 0 tràn chương, 0 dòng mồ côi, 0 chưa dịch, 0 trùng key, 0 dòng uncertain.
- **Second pass:** 19 tổng / 19 kiểm tra lại / 0 loại bỏ / 0 sửa.
- **Khối TOML:** 19 key, parse-verified, 0 lệch giá trị so với JSON.
- **Ghi chú:** キルクイティウム thống nhất "Quirquitium" 5/5 trong file; "Circuithium" ở 日々姫10 key 2458 là vấn đề thống nhất liên file (docs chưa quyết). CSV==TOML 0 lệch thật (2677 chỉ là lỗi chuẩn hoá `\n` của script so sánh). 'cô' cho Navi (2449) giữ theo quy ước; "Mình" ở 3348 giữ theo ngoại lệ độc thoại nội tâm; 2214 giữ "Soutetsu" trần giữa câu (JP bare ソウテツ đang lắp bắp đọc tên, không phải cách gọi).
- **Tổng mới: 47 files / 2.779 dòng sai** (từ base 46 files / 2.760 + 19). Lưu ý: một audit song song (00_Common file 05) đang chạy — khi merge, cộng thêm số của file 05 vào tổng này.

## 00_Common file 05_ようやく石炭 (19/11/2026) — 52/421 sai (12,4%), 0 dòng chưa chắc chắn; file Common thứ ba được audit, lỗi tập trung thuật ngữ chuyên ngành + xưng hô, 0 lệch dòng
- Thuật ngữ 32 (御一夜→Ohitoyo 11: 77, 3082, 2484, 2183, 2495, 2641, 2266, 2426, 2254, 2645, 3104 — file còn 0 dòng Ohimitera; 帝鉄→Teitetsu 8: 2685, 1809, 2418, 2392, 2680, 2408, 1843, 2524; まいてつ→chủ tàu 6: 2443, 2719, 2474, 2467, 2730, 2495 — thống nhất nội bộ file theo quyết định “chủ tàu”, “người sành toa xe” 7 dòng đã sửa; 気動車→toa xe tự hành 5: 1812, 2188, 2509, 2151, 2591 — “động cơ” là sai, tiền lệ ディーゼル気動車→“toa xe diesel tự hành”; 市電→tàu điện thành phố 2: 2404, 2378 — “nguồn điện chính” sai nghĩa; Hieu chốt 20/11, docs mục 119 đã sửa; 整備体→thân bảo trì 1: 2227), xưng hô 9 (Soutetsu→Paulette “cô”→“em” 5: 2573, 2139, 2395, 2442, 2185; Soutetsu→Hachiroku “cô”→“em” 2: 2440, 2727 — tiền lệ file 03 “em” 65 dòng + 夜の嵐 1528; Soutetsu độc thoại “Mình”→“Tôi” 1: 3560 — chủ ngữ mệnh đề chính; Paulette tự sửa くん→さん 1: 2551 “Cậu Soutetsu……à không, anh Soutetsu” theo mẫu 2721/2421/2275 trong file), rên っ 3 (2763, 2287 theo sweep nguyên văn + 2284 sweep-missed あぐっ→“Agu.”), SFX 1 (1840 うふふふふ bị diễn thành “ư hừ hừ hừ” → “Ufufufufu” theo quy tắc 22:05), nghĩa 2 (2559 khôi phục→khắc phục sự chậm trễ; 2699 đô con→uống khỏe), nhỏ 2 (2417 hửm→không phải; 3089 ngắt câu Railord/Reina), tag 3 (gỡ tag %l VN tự thêm: 2587, 2662, 2991 — theo tiền lệ reina02).
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi, 0 dòng chưa dịch.** VN trùng lặp trong file: 0; JP trùng lặp: 0. Kiểm tra bằng project VN index: VN dài >25 ký tự chỉ trùng 1 dòng với ハチロク10_炙り出し 2405 — JP hai bên gần như giống hệt nhau (心底、驚いたような顔 vs 心底、びっくりしたような顔) nên là hai bản dịch độc lập, không phải tràn chương.
- TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất; 265 dòng `\n` bị làm phẳng trong TOML). `# JP:` đủ 421/421 key script. CSV chỉ có MỘT bộ dòng cho file này (`00_Common\`, 421 dòng) — không có bẫy hai bộ. TOML chỉ có một bản duy nhất (md5 `de5a6dfdd9e725f1e7df12251d6d2b2f`, không trùng lặp).
- `[selections]` rỗng (0 mục). Thẻ `%l`: JP = VN ở mọi dòng — **0 thẻ thiếu dấu `;` đóng**. Gloss 機関士/運転士 “người lái tàu” (2505, 2432, 2727, 2319) giữ theo quy ước đã chốt. Tag phức tạp ở 2524 (%l; lồng ruby [ハチロクニイマル,3]) giữ nguyên cấu trúc JP, chỉ đổi gloss.
- “mình” trong độc thoại Soutetsu: 15 lần, chỉ 1 sai (3560 — chủ ngữ mệnh đề chính); còn lại đều đúng (sở hữu/phản thân/mệnh đề phụ/thành ngữ, theo tiền lệ hearing). Soutetsu thoại: “tôi” nhất quán. “cô” cho Paulette từ Hachiroku (2732, 2733, 2610) và “Thị trưởng Paulette” cho ポーレット様 (2572) giữ theo docs §2.2 — Paulette là thị trưởng (3316, 2436). B4: 0 dòng Paulette gọi tên trần “Soutetsu” (tất cả đều “anh/ngài/cậu Soutetsu”).
- 0 dòng chưa chắc chắn. Hai điểm để lại cho đợt thống nhất: (1) gloss まいてつ toàn dự án chia 4 cách (chủ tàu 23 / Maitetsu 11 / người sành toa xe 9 / người đam mê đường sắt 3) — Hieu chốt “chủ tàu” 20/11 theo đề xuất của Muse (tiền lệ TW 掌車人); (2) gloss 市電 “nguồn điện chính” (docs mục 119) mâu thuẫn JP — audit sửa 2 dòng về “tàu điện thành phố” (Hieu chốt 20/11, docs đã sửa).
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (52/52 đúng, 0 bị loại, 1 được sửa trong lần hai: 3089 khôi phục tag %l của レイルロオド bị rớt trong bản thảo); kiểm tra chẵn lẻ 「」 (0 lệch) và số lượng tag %l (0 lệch, trừ 3 dòng cố tình gỡ tag VN tự thêm). Rà soát chéo với sweep: sweep có 3 mục trong file (2 bản sửa nhận nguyên văn — 2763/2287; 1 already-rendered 2311) + 1 sweep-missed do audit tìm ra (2284).
- Fix list (52/52 key verified to parse, 0 lệch giá trị) saved at ~/workspace/maitetsu-pilot/audit-00common05-REVIEW.md and audit-00common05-wrong.json — NOT sent to Hieu (no-files rule).

**Tổng sau file này: 48 file / 2.831 dòng sai** (47 file / 2.779 trước file này + 52). Ghi chú: file 04 đã merge trước (47 file / 2.779); tổng sau file này 48 file / 2.831.

## 00_Common file 07 — 共通07_鍵.txt.toml (19/11/2026)

**34/331 dòng sai (10,3%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo.**
- Đại từ 19 (Soutetsu gọi Paulette "cô"→"em" 12; Soutetsu tự xưng "em" 2 — 1777, 1801; B4 "Soutetsu-kun"→"anh Soutetsu" 5), thuật ngữ 7 (KiHa 1; Ohitoyo 5 lần/4 dòng; "khối lượng chỉnh bị vận hành"→"khối lượng vận hành" 1; Teitetsu 1), minor 5, tag 1 (2525 — VN tự thêm thẻ gloss, gỡ + sửa gloss thành "thân bảo trì"), meaning 1 (1423 すごい → "Khủng thật"), gasp 1 (2144, sweep lost-gasp-whole, khớp sweep).
- Thoại 30/210 sai, độc thoại 4/121 sai. Theo nhân vật: 双鉄 17, ポーレット 11, れいな 1, ハチロク 1, độc thoại 4.
- Nguồn sạch: CSV bộ duy nhất 00_Common; VN khớp tuyệt đối 140, khớp sau khi gộp dòng 330/331 (1 khác biệt chỉ là khoảng trắng thừa cuối dòng). TOML md5 ee6e26eef127ff6d76a5ddb65e2242f9, không có bản sao trùng.
- Không sai có chủ đích: 1910 (san→kun là điểm nhấn của câu), 2342 (độc thoại nhận ra đổi từ "anh" sang "kun" — phân biệt san/kun là nội dung), 1893 ("anh Soutetsu" vs "anh hai"), 1898/2070/2103 ("Sou-chan" của Mayami), 1979 (quirk của JP), 2025, 2119, 2121, 2279, 2425, 2534.
- Dị thường dữ liệu (không phải lỗi VN): thẻ %l phía JP ở 2547 bị tách bởi ký tự xuống dòng (mở 1, đóng 0 theo dòng); phía VN đóng đúng, gloss "trưởng hầm rượu" đúng.
- Lượt soát 2: 34 tổng / 34 kiểm tra lại / 0 loại bỏ / 5 sửa lại (1423, 1445 rơi 「」; 1431 chuỗi thay thế không khớp do thẻ %l chen giữa; 1684, 2133 "anh" đầu câu phải viết hoa "Anh").
- Ohitoyo 00_Common: đã sửa 5 lần ở file này; còn lại 109 lần (file 14: 30, 09: 15, 15: 15, 10: 14, 11: 12, 01 pilot: 8 chưa chốt, 12: 6, 06: 4, 13: 3, 08: 2 — file 04 đã sửa xong 1 dòng ở audit trước).
- Còn lại chưa kiểm toán trong 00_Common: 06, 08, 09, 10, 11, 12, 13, 14, 15, 末尾 (10 file).
- Deliverables: `audit-00common07-REVIEW.md`, `audit-00common07-wrong.json` (34 mục, key dạng chuỗi). Khối TOML trong review đã kiểm chứng parse: 34 key, 0 sai lệch giá trị.

**Tổng cộng sau file này: 49 file / 2.865 dòng sai** (cơ sở 48 file / 2.831 + 34 file này). Lưu ý: một audit song song khác đang chạy cùng lúc — tổng này chưa gồm file đó; cộng dồn khi file kia xong.

## 00_Common file 06_8620を探せ (20/11/2026) — 47/444 sai (10,6%), 0 dòng chưa chắc chắn; file Common thứ tư được audit, lỗi tập trung xưng hô Soutetsu (25) + nghĩa (12), 0 lệch dòng
- Xưng hô 25 (Soutetsu tự xưng “tôi”→“anh” với Hibiki 11: 1882, 1940, 1942, 1946, 2080, 2099, 2240, 2244, 2248, 2269, 2270; Soutetsu tự xưng “anh”→“tôi” với Hachiroku 5: 1879, 2206, 2207, 2220, 2334 — 1879 kèm “cô ấy”→“nó” cho chiếc 8620; Soutetsu gọi “cô”→“em” 4: 1587, 2034, 2286, 2410; Hibiki→Hachiroku “cô/cháu”→“chị/em” 3: 2092, 2460, 2461; Hachiroku tự xưng “cháu”→“em” 1: 2231; Hachiroku gọi Soutetsu “cô”→“Ngài” 1: 2150 — quy ước đã chốt: “anh” chỉ với Hibiki, với Hachiroku/Mayami là “tôi”; tiền lệ file 02 2162/2163 + file 05 2440/2727), thuật ngữ 6 (御一夜→Ohitoyo 4: 2347, 2395, 3102, 3103; 運転士 gloss→“nhân viên cơ vụ” 2: 2129, 2714), nghĩa 12 (1891 義理の家族→thông gia; 1898 thiếu 1 lần “Không được”; 1900 そんなんっ→“Không đời nào!”; 1950 viển vông→mơ hồ; 1957 đảo hướng câu hỏi “Mình”→“Em”; 2297 + 2513 nói lắp tên 8620 bị chuẩn hoá — giữ lại theo tiền lệ 1904; 2385 bịa “mệt”; 2740 + 2932 義→“nuôi” bịa thêm; 2857 それ/これ→“Chuyện nào”; 3092 あがり症→“sợ đám đông”), rên っ 2 (2510, 2511 sweep-missed), SFX 2 (2074 ふぅむ→“Hừừm” theo công thức nguyên âm; 2760 ふふ→“fufu” không phải “ufufu”).
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi, 0 dòng chưa dịch.** VN dài >25 ký tự chỉ trùng 3 dòng ở file khác, JP hai bên giống hệt nhau (câu lặp lại, không phải tràn). Tag %l: JP = VN mọi dòng, 0 thẻ thiếu `;`. VN trùng lặp: 4 cặp câu ngắn lặp hợp lệ (JP giống hệt); 2074/2075 JP khác nhau (ふぅむ vs ふむ) đã sửa 2074.
- Nguồn: bẫy hai bộ CSV — dùng bộ `01_Hachiroku` (JP khớp TOML 444/444, VN khớp 444/444 sau khi gỡ `\n`); bộ `00_Common` STALE (VN khớp 20/444) đã bỏ. TOML một bản duy nhất, md5 `1d4c8254efe7fe5c556f1a67bed5e439`, `[selections]` rỗng, BOM + CRLF. Paulette 0 dòng thoại nên B4 không áp dụng. Sweep: 0 fixed trong file; 3 key needs-file-audit (2016, 3153, 3173) đều không cần sửa (JP không có っ).
- Giữ nguyên (đã kiểm tra, không sai): Hachiroku→Hibiki “cô” (1954, 2225, 2393 — lối nói trang trọng, “chị Hibiki” là dạng tên+gọi); gloss 投炭 “xúc than” (1596, 2951 — đa số 31/48 toàn dự án); “mình” ở mệnh đề phụ/sở hữu/phản thân (1940, 2004, 2334, 2402); Hibiki “cháu” với bà chủ (1982, 2308); “chúng cháu” khiêm nhường (2001, 2198, 2458). 0 dòng chưa chắc chắn (2461: JP là câu bỏ lửng, giữ cách đọc của người dịch cũ, chỉ sửa xưng hô).
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (47/47 đúng, 0 bị loại, 0 sửa lại) + kiểm tra cơ học (mỗi bản sửa chỉ đổi đúng đoạn cần sửa, 47/47 khớp); khối TOML 47 key parse-verified bằng tomllib, 0 lệch giá trị. Fix list saved at ~/workspace/maitetsu-pilot/audit-00common06-REVIEW.md and audit-00common06-wrong.json — NOT sent to Hieu (no-files rule).

**Tổng sau file này: 50 file / 2.912 dòng sai** (49 file / 2.865 trước file này + 47). Ghi chú: file 07 đã merge trước (49 file / 2.865); tổng sau file này 50 file / 2.912. Ohitoyo còn lại 105 lần (109 − 4 ở file này).

## 00_Common file 09 — 共通09_さきだつもの.txt.toml (20/11/2026)

**36/497 dòng sai (7,2%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo.**
- Thuật ngữ 18 (Ohimitera→Ohitoyo 15 dòng: 2199, 2221, 2452, 2497, 2569, 2710, 2741, 2770, 2782, 3001, 3005, 3027, 3138, 3150, 3303 — file 00_Common "bẩn" nhất về Ohimitera; 帝鉄→Teitetsu 3: 2482, 2644, 2724; 湯医→Yunoi 1: 3027 chung dòng với Ohitoyo), đại từ 9 (Soutetsu gọi Paulette "cô"→"em" 4: 2601, 2737, 2355, 2363; Soutetsu tự xưng "anh" sai đối tượng 2: 2123 với Nagi, 2397 với Minokasa; B4 "Soutetsu-kun"→"anh Soutetsu" 2: 2461, 2632; Soutetsu gọi ông lão Minokasa là "cô" 1: 2161), tag 4 (VN tự thêm thẻ gloss, gỡ: 2182, 2580, 2740, 3519), gasp 3 (2326 あぐっ→"Agu!" theo tiền lệ file 05 2284; 2796 bare っ!→"Ư!" theo tiền lệ sweep file 01 1247; 2802 っ đầu dòng→"Ư!!?" theo tiền lệ lr_h1 1077), meaning 2 (102 堅いところ dịch ngược nghĩa "nơi an toàn nhất"→"chỗ khó khăn nhất"; 2216 誘致反対 "Hủy bỏ thu hút"→"Phản đối thu hút nhà máy!").
- Thoại 27/286 sai, độc thoại 9/211 sai. Theo nhân vật: 双鉄 13, monologue 9, 路子 4, 蓑笠 3, 日々姫 2, ハチロク 2, ポーレット 2, 凪 1.
- Nguồn sạch: CSV bộ duy nhất 00_Common; VN khớp tuyệt đối 227, khớp sau khi gộp dòng 269/497 (1 khác biệt duy nhất là key 3378 — TOML làm phẳng ký tự \n thành khoảng trắng, hiện tượng đã biết, không phải lỗi dịch). TOML md5 c2bc3fe444488de0f3599b65c6d6334f, BOM + CRLF, [selections] rỗng, không có bản sao trùng.
- Sweep っ — ĐÍNH CHÍNH CỦA PARENT: sweep CÓ liệt kê file này (9 mục trong sweep-raw-gasp-wrong.json: 109, 2581, 2634, 2681, 2796, 3270, 3284, 3655, 2359); 8 giá trị fix đã kiểm chứng đúng, 2796 trùng với fix của audit; 2359 already-rendered đúng. 2 gasp mất do audit phát hiện mà sweep bỏ sót: 2326, 2802.
- Không sai có chủ đích: 3238 (độc thoại "Anh tò mò lắm" là nội dung thông điệp nhẩm gửi tới Michiko, khác tiền lệ file 06 2220 là tường thuật về bản thân), 3681 ("mình" trong độc thoại nội tâm tự vấn cảm xúc, theo ngoại lệ h3 1683), các "anh" với Michiko 2353/2356/2487/2492/2494/2503/2664 (anh trai với em gái), "cô" đúng 2309/2421/2501 (ngôi thứ ba / danh xưng), Paulette "anh Soutetsu" đúng 2583/2756/2792.
- Dị thường dữ liệu (không phải lỗi VN): JP 2482 có tag dị dạng (đóng `%l;`, thừa `\x%l8620;#;`) — TW giữ nguyên, VN đã chuẩn hóa thành 3 tag thường; chỉ sửa gloss Teitetsu. JP 2802 trùng Grand 01 3088 nhưng đó là dòng đã lệch sẵn trong Grand 01, không phải nhiễm vào file này.
- Lượt soát 2: 36 tổng / 36 kiểm tra lại / 0 loại bỏ / 1 sửa lại (2461 "anh Soutetsu" đầu câu phải viết hoa "Anh"). Parent loại thêm 1 fix sai (2525) sau lần 2.
- Ohitoyo 00_Common: đã sửa 15 lần ở file này (khớp đúng con số 15 đã đếm trước đó); còn lại sau file này: 90 lần (14: 30, 15: 15, 10: 14, 11: 12, 12: 6, 13: 3, 08: 2 chưa merge, 01 pilot: 8 chưa chốt).
- Còn lại chưa kiểm toán trong 00_Common: 10, 11, 12, 13, 14, 15, 末尾 (7 file; file 01 pilot vẫn là bản nháp).
- Deliverables: `audit-00common09-REVIEW.md`, `audit-00common09-wrong.json` (36 mục, key dạng chuỗi). Khối TOML trong review đã kiểm chứng parse: 36 key, 0 sai lệch giá trị.

**Tổng cộng sau file này: 51 file / 2.948 dòng sai** (cơ sở 50 file / 2.912 + 36 file này — parent loại 2 fix sai 2525, 2123 và bổ sung 1 fix sót 2719 sau audit; tổng không đổi).

## 00_Common file 08_傷跡 (20/11/2026) — 38/360 sai (10,6%), 0 dòng chưa chắc chắn; lỗi tập trung đại từ Soutetsu xưng "anh" với Hachiroku, 0 lệch dòng
- Đại từ 18 (Soutetsu tự xưng "anh"→"tôi" 13: 1688, 1725, 1782, 1858, 1876, 1897, 1901, 1921, 1923, 1937, 1958, 1999, 2076 — "anh" với Hibiki/Michiko/Paulette/Reina, "tôi" với Hachiroku/Mayami/Nagi/Minokasa; Soutetsu gọi Paulette "cô"→"em" 1: 1974; gọi Reina "cô"→"em" 1: 1855; độc thoại Soutetsu tự xưng "em"→"tôi" 2: 71, 76; B4 "Soutetsu-kun"→"anh Soutetsu" 1: 2084 — romaji "S-Soutetsu-kun!?" → "A-Anh Soutetsu!?"), thuật ngữ 16 (整備体→"thân bảo trì" 6: 76, 77, 1747, 1810, 1982, 2453; 運転体→"thân vận hành" 5: 1456, 1486, 2517, 2529, 2692 — "kíp lái" sai, đó là thân thể không phải kíp người; タブレット→"máy tính bảng" 4: 1480, 1929, 1991, 2836; Ohimitera→Ohitoyo 2: 1881, 2547), tag 3 (gỡ thẻ %l VN tự thêm — JP chỉ có [ボディ] dạng ruby: 1486, 1747, 1810), gasp 4 (1996/2098/2099 theo sweep nguyên văn + 1490 sweep-missed 「っ――」→「Ư――」).
- Thoại 27/180 sai, độc thoại 11/180 sai. Theo nhân vật: 双鉄 18, ハチロク 5, れいな 3, ポーレット 1, độc thoại 11.
- Nguồn sạch: CSV bộ duy nhất 00_Common; VN khớp tuyệt đối 162, khớp sau khi gộp dòng 360/360. TOML một bản duy nhất, md5 `6d338fc2caafd1b4abd75c58e1aa4dcd`, `[selections]` rỗng, BOM + CRLF. 0 thẻ %l malformed.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi, 0 dòng chưa dịch.** Chỉ mục VN toàn dự án: 2 ứng viên trùng VN ở file khác đều là câu lặp hợp lệ với JP gần như giống hệt (2036 様/さま; 2340 固く握手/固く、握手).
- Giữ nguyên (đã kiểm tra, không sai): 2023 "Anh đi lấy nước và than nhé?" — người nghe mơ hồ (Hibiki được giao việc lấy than/nước ở 2010, lại xung phong ở 2080) nên "anh" có thể đúng — trường hợp biên, ghi lại cho Hieu; 1912 Hachiroku "Chị mới là người phải xin lỗi" — người nghe là Reina, "chị" đúng (tiền lệ 1966); "mình" phản thân/tân ngữ ở 1901/2519/2572 giữ nguyên; độc thoại Hibiki tự xưng "em" giữ nguyên; 1808/1865/1695 giữ nguyên.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ (38/38 đúng, 0 bị loại, 0 sửa lại — parent loại thêm 2 fix sai 1980/2071 sau lần 2) + kiểm tra cơ học (JSON jp/tw/old_vn khớp CSV tuyệt đối; khối TOML 38 key parse-verified bằng tomllib, 0 lệch giá trị). Fix list saved at ~/workspace/maitetsu-pilot/audit-00common08-REVIEW.md and audit-00common08-wrong.json — NOT sent to Hieu (no-files rule).
- Ohitoyo 00_Common còn lại 88 lần (14: 30, 15: 15, 10: 14, 11: 12, 12: 6, 13: 3, 01 pilot: 8 chưa chốt — file 08 đã sửa xong 2 dòng, file 09 đã sửa xong 15 dòng).
- Điểm để lại cho đợt thống nhất: (1) gloss 乗務鞄 — toàn dự án "túi phi hành đoàn" 11 vs "cặp lái tàu" 3, TW 乘務包; "phi hành đoàn" là thuật ngữ hàng không, sai lĩnh vực, nhưng là đa số nên giữ nguyên trong file này chờ Hieu chốt; (2) trường hợp biên 2023.

**Tổng sau file này: 52 file / 2.986 dòng sai** (cơ sở 51 file / 2.948 + 38 file này — parent loại 2 fix sai 1980/2071 sau audit).

## 00_Common file 10 — 共通10_クマ川くだりで見る景色.txt.toml (20/11/2026)

**40/430 dòng sai (9,3%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng.**
- Thuật ngữ 23 (Ohimitera→Ohitoyo 13 mục + 2995 trong mục gasp = 14 dòng: 3356, 3254, 2708, 3296, 2486, 2276, 2778, 2801, 2813, 3404, 2352, 3129, 2510, 2995 — đúng con số 14 đã đếm trước đó; 帝鉄→Teitetsu 3: 2508, 2767, 3092; 湯医→Yunoi 4: 2396, 2605, 2276, 2778; 帝大→"Đại học Đế quốc" 1: 2264 — cùng mẫu dịch sai như 帝鉄; 運転体→"thân vận hành" 2: 3005, 3359; タブレット→"máy tính bảng" 1: 3376; 術仙→"Jutsu-sen" 1: 2771; 宮司→"đền chủ" 1: 3092 chung dòng với Teitetsu), đại từ 11 (Soutetsu "tôi"→"anh" với Fukami 1: 2779 — Fukami gọi Soutetsu là 「双鉄おにいさん」 (2706), 12 dòng "anh" khác với Fukami; Soutetsu "anh"→"tôi" với Hachiroku 3: 2475, 2479, 2656; Fukami "Chị nói"→"Anh nói" 1: 2221, đối tượng là Soutetsu; Nagi "bé Fukami"→"chị Fukami" 4: 2218, 2228, 2604, 2430 + Soutetsu trích lời Nagi 1: 2642; độc thoại "Anh"→"Tôi" 1: 3217), gasp 3 (2209, 2815, 2995 — cả 3 từ sweep, đã kiểm chứng đúng), meaning 2 (3268 VN bịa thêm "nghe những điều người ta" — JP không có 聞, không có "người ta"; 2477 どう……だろうな dịch ngược sắc thái không chắc chắn), SFX 1 (2369 はぅ→"Hau", tiếng bối rối không phải đồng ý "Vâng").
- Thoại 29/270 sai, độc thoại 12/160 sai. Theo nhân vật: monologue 12, 双鉄 11, ふかみ 6, ハチロク 6, 凪 4, 稀咲 2.
- Nguồn sạch: CSV bộ duy nhất 00_Common; VN khớp tuyệt đối 177, khớp sau khi gộp dòng 253/430, 0 khác biệt. TOML md5 a36943d7a08e0c9705401e3b771db961, 86.402 byte, BOM + CRLF, [selections] rỗng, không có bản sao trùng.
- Sweep っ: kiểm tra trực tiếp sweep-raw-gasp-wrong.json — file này CÓ 3 mục (2209, 2815, 2995), cả 3 giá trị đúng, đã nhận (2995 kèm sửa Ohitoyo cùng dòng). Không có gasp nào sweep bỏ sót trong file này.
- Nhiễm chéo: tra chỉ mục VN toàn dự án — 16 lần trùng đều là câu ngắn thông dụng dịch độc lập giống nhau; 2 lần lặp hợp lệ có JP giống hệt (2578, 3294). Không nhiễm chéo.
- Phán đoán 2616 — ĐÃ QUYẾT BỞI PARENT (20/11): Hachiroku giữ "Chị nghĩ" với Fukami (Fukami gọi cô ấy là "Chị Hachiroku" ở 2706, logic đối ứng như khóa B4). Tiền đề "em 2× với Fukami" sai một nửa: 2483 nói với Soutetsu nên "em" đúng; 2597 giữ nguyên "em" (người nghe chưa rõ).
- Không sai có chủ đích: 3005 乗務鞄 "túi phi hành đoàn" GIỮ NGUYÊN chờ quyết định thống nhất của Hieu (đa số 11 vs "cặp lái tàu" 3); 2573 "bố nuôi/mẹ nuôi" ĐÚNG (JP 義父/義母, TW 養父/養母, ngữ cảnh con nuôi — khác mẫu bịa file 06); 2388 hai câu hô giống nhau đúng (cùng JP ヨイサノサノ); 2682 "cô ta" giữ (bà lão hư cấu); 2307 "Pyawa" giữ (ひゃ→"Hya" đã chốt); 2493/2707 tự giới thiệu trang trọng giữ; 2633 "Chúng tôi" số nhiều giữ; 2502/2554 っ nhấn mạnh bỏ đúng; 3325/3326 hai dòng khác nhau (túi Hachiroku vs túi áo Soutetsu); 1873 VN==TW chỉ là dấu ba chấm.
- Dị thường dữ liệu (không phải lỗi VN): JP 2508 có tag dị dạng (mở 5 / đóng 4, cùng mẫu file 09 key 2482: đóng `%l;` thiếu `;` + thừa `\x%l8620;#;`); VN đã chuẩn hóa, chỉ sửa gloss Teitetsu.
- Lượt soát 2: 40 tổng / 40 kiểm tra lại / 0 loại bỏ / 3 sửa lại (2276, 2778 — bản thảo quên Yui→Yunoi trong cùng dòng; 3268 — bỏ "lại" thừa). Parent loại thêm 1 fix sai (2616) sau lần 2. Kiểm tra cơ học: ngoặc cân bằng 40/40, tag %l không đổi ở mọi dòng.
- Ohitoyo 00_Common: đã sửa 14 lần ở file này; còn lại sau file này: 74 lần (14: 30, 15: 15, 11: 12, 12: 6, 13: 3, 01 pilot: 8 chưa chốt).
- Còn lại chưa kiểm toán trong 00_Common: 11, 12, 13, 14, 15, 末尾 (6 file; file 01 vẫn là bản nháp pilot).
- Deliverables: `audit-00common10-REVIEW.md`, `audit-00common10-wrong.json` (40 mục, key dạng chuỗi). Khối TOML trong review đã kiểm chứng parse: 40 key, 0 sai lệch giá trị.

**Tổng cộng sau file này: 53 file / 3.026 dòng sai** (cơ sở 52 file / 2.986 + 40 file này — parent loại 1 fix sai 2616 sau audit).

## 00_Common file 11 — 共通11_経営資源.txt.toml (20/11/2026)

**102/572 dòng sai (17,8%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo.**
- Thuật ngữ 59 (宮司→"đền chủ" 38 dòng / 39 lần: 2293, 2302, 2401, 2503, 2522, 2530, 2578, 2620, 2672, 2782, 2783, 2814, 2886, 3002, 3253, 3307, 3313 [×2], 3332, 3390, 3444, 3445, 3470, 3529, 3542, 3559, 3567, 3589, 3611, 3792, 3829, 3830, 3832, 3833, 3834, 3835, 3836, 3837, 3838 — file nặng về Akai nên đây là lỗi nhiều nhất; Ohitoyo 12: 1828, 2525, 2535, 2753, 2817, 2818, 2937, 2960, 3434, 3562, 3758, 3836; 帝鉄→Teitetsu 10: 1777, 2522, 2529, 2546, 2620, 2693, 3321, 3487, 3834, 3836; 冥国→Minh Quốc 2: 2628, 2901; 廣島電気鉄道→"Đường sắt điện Hiroshima" 1: 2689; gỡ chú thích romaji "(kikanshi)/(untenshi)" 1: 2580; 経営資源→"tài nguyên kinh doanh" 1: 2546 chung dòng với Teitetsu), đại từ 30 (Soutetsu gọi Paulette "cô"→"em" 11 dòng: 1845, 2239, 2250 [×2], 2253, 2299, 2380, 2423, 2445, 2997, 3003, 2308; Soutetsu tự xưng "tôi"→"anh" với Paulette 18 dòng: 1797, 2238, 2250, 2380 [×2], 2466, 2479, 2572, 2583, 2596, 2599, 2645, 2711, 2987, 2995, 2998, 3003, 3023, 3031; Soutetsu "em"→"tôi" với Mayami 4 dòng: 2450, 2612, 2839, 2842 [×2]), tag 2 (VN tự thêm thẻ gloss, gỡ: 2404 醸造蔵, 3076 8620 — JP chỉ có ruby, đã kiểm chứng comment # JP trong TOML), gasp 6 (sweep 1811, 3067, 3068 áp nguyên; 2396 ふぅ→"Phùù", 2419 ふぅむ→"Hừừm." theo công thức nguyên âm, tiền lệ file 06 2074; 3536 「ああ」→"Aa"), meaning 5 (2582 gỡ "(Pháp)" tự thêm; 2624 Paulette "Tôi... mình" thống nhất về "tôi"; 3016 あのっ！ "Chỗ này ạ!" bịa → "Ưm!"; 3273 lỗi đánh máy "cô cô đơn"; 3645 口惜しい "cam chịu" ngược nghĩa → "không cam lòng", TW 不甘心).
- Thoại 69/367 sai (18,8%), độc thoại 33/205 sai (16,1%). Theo nhân vật: 双鉄 42, monologue 33, ポーレット 14, 赤井宮司 8, ハチロク 4, 真闇 1.
- Nguồn sạch: CSV bộ duy nhất 00_Common; VN khớp tuyệt đối 215, khớp sau khi gộp dòng 357/572, 0 khác biệt. TOML md5 2981d5f80fa4b088f19aa89c998ccca4, BOM + CRLF, [selections] rỗng, không có bản sao trùng. 0 hàng chưa dịch, 0 key trùng; 1 hàng VN == TW là 1816 (「……」 giống hệt JP/TW, hợp lệ). VN trùng trong file chỉ là câu ngắn lặp lại hợp lệ (「Ồ.」×4, 「Hừm.」×3, 「Vâng.」×3, 「A.」×2).
- Sweep っ: sweep CÓ liệt kê file này (3 mục 1811/3067/3068, cả 3 đã kiểm chứng đúng, áp nguyên); quét っ hệ thống toàn bộ JP không tìm thêm gasp trần nào bị mất; 3016 là audit tự phát hiện (tiếng ngập ngừng, không phải っ trần).
- Không sai có chủ đích: 2406 "Anh Akai" (quét toàn dự án: "Anh Akai" là cách dịch đã thiết lập của 赤井さん — Hibiki 日々姫08 2259, Nagayama P14 1524, 技工Ｂ ニイロク03 ×4); 2409 「ああ」→"A." (đã có 16 lần trong dự án); 2415 "chú chó con" (lỗi nhầm của chính Soutetsu, là trò đùa; Hachiroku sửa ở 2621); 3747 "Pyon!" (SFX, quy tắc ngẫu hứng); 2909 "mài ra ăn được" (thành ngữ); 2592 "Bọn em" (số nhiều); 2623 "các cậu" (xưng hô nhóm); 3314 "Watashi", 3884 "Reina" (từ đang được bàn luận); 2886/2287 "chúng tôi" với Paulette (số nhiều); 2337 "Tôi" với Hachiroku và 2590/2576/2636/2906/2701/2999/2609/2848 "tôi" với Akai/Hachiroku (quan hệ trang trọng, đúng). 2572 "anh" với Paulette: địa chỉ suy từ mạch truyện (kế hoạch cho mèo là của Paulette; cô ấy nói trước 2887 và tiếp sau 2805) — đủ vững nhưng ghi chú rõ trong review.
- Thứ tự dòng: key số trong file này KHÔNG phải thứ tự truyện (các cảnh xen kẽ nhau) — địa chỉ người nghe xác định từ nội dung + mạch hội thoại, không dùng key kề theo thứ tự số.
- Lượt soát 2: 102 tổng / 102 kiểm tra lại / 0 loại bỏ / 1 sửa lại (3536 chép nhầm "đồng tình" thành "đồng ý", đã sửa lại — chỉ thay 「A」→「Aa」). Quét regex hệ thống trong lúc kiểm chứng bắt thêm 2 dòng lần đọc chunk bỏ sót (3529, 3830 — đều 宮司); 宮司 thực tế là 38 dòng / 39 lần, không phải 35 dòng như lần đọc đầu đếm.
- Ohitoyo 00_Common: đã sửa 12 lần ở file này; còn lại sau file này: 62 lần (14: 30, 15: 15, 12: 6, 13: 3, 01 pilot: 8 chưa chốt — file 10 đã sửa xong 14 lần).
- Còn lại chưa kiểm toán trong 00_Common: 12, 13, 14, 15, 末尾 (5 file; file 12 đang audit song song; file 01 pilot vẫn là bản nháp).
- Deliverables: `audit-00common11-REVIEW.md`, `audit-00common11-wrong.json` (102 mục, key dạng chuỗi). Khối TOML trong review đã kiểm chứng parse: 102 key, 0 sai lệch giá trị.

**Tổng cộng sau file này: 54 file / 3.128 dòng sai** (cơ sở 53 file / 3.026 + 102 file này — parent sửa 20/11 01:18: cơ sở gốc 52/2.986 chưa gồm file 10, thiếu 40 dòng).

## 00_Common file 12 — 共通12_のぞみ.txt.toml (20/11/2026)

**35/520 dòng sai (6,7%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng.**
- Thuật ngữ 15 (Ohimitera→Ohitoyo 6: 2169, 2211, 2458, 2569, 2184, 3447 — đúng con số ~6 đã đếm trước đó; 宮司→"đền chủ" 6: 3436, 2069, 3433 "Cung tư tế", 3445, 3435, 3038 "Thầy Akai" — biến thể "Thầy" chưa từng thống kê; 湯医→Yunoi 1: 3391 — dòng "Yui" thứ ba trong dự án; 撮り鉄→"người chụp ảnh tàu" 1: 2415; 車両鉄→"người mê toa xe" 1: 2492, kèm khôi phục tag %l), đại từ 13 (Soutetsu "anh"→"tôi" với Hachiroku 4: 2132, 2193, 2251, 2626 dòng 2; Soutetsu "tôi"→"anh" với Fukami 1: 2424 + với Reina 1: 2117 — người nghe là Reina, tiền lệ file 08 keys 1980/2071; Soutetsu gọi Hachiroku "cô"→"em" 7: 1970, 2320, 1973, 2266, 2269, 2300, 2538 — 2300 kèm gỡ tag %l VN tự thêm trên 8620), gasp 2 (2632, 2633 — cả 2 từ sweep, đã kiểm chứng đúng), meaning 3 (2385 bỏ mất だご — "đói bụng" không có trong JP; 2403 bịa thêm "chuyên dụng"; 3241 từ Hàn "확" lọt vào VN), typo 1 (2102 "dang"→"đang"), SFX 1 (2113 おっと "Hây dô."→"Ôi chà." — lỗi dán nhầm: "Hây dô." là cách dịch của よっと, xem 日々姫08 2251; cùng JP おっと ở 2118 trong file này đã dịch đúng "Ôi chà.").
- Thoại 27/303 sai, độc thoại 8/217 sai. Theo nhân vật: 双鉄 19, monologue 8, 日々姫 3, 赤井宮司 2, ポーレット 1, 凪 1, 早瀬流 1.
- Nguồn sạch: CSV bộ duy nhất 00_Common; VN khớp tuyệt đối 194, khớp sau khi gộp dòng 326/520, 0 khác biệt. TOML md5 7cef20cf0cab502f5680336f10ea8d85, 111.255 byte, BOM + CRLF, [selections] rỗng, không có bản sao trùng.
- Sweep っ: kiểm tra trực tiếp sweep-raw-gasp-wrong.json — file này CÓ 2 mục (2632, 2633), cả 2 giá trị đúng, đã nhận. Quét bổ sung toàn bộ 189 dòng JP chứa っ (24 ứng viên): còn lại đều là っ nhấn mạnh hoặc âm đã render. Không có gasp nào sweep bỏ sót trong file này.
- Nhiễm chéo: tra chỉ mục VN toàn dự án — 155 lần trùng đều là câu ngắn thông dụng dịch độc lập giống nhau; 0 lần trùng VN trong file với JP khác nhau; JP trùng trong file đều hợp lệ (2110/2083/2084 うむ→"Ừm."; 2363/2228 はい, 2359/2349 ああ khác ngữ cảnh; 2118/2113 cùng JP おっと — chính là lỗi 2113). Không nhiễm chéo.
- Phán đoán giữ nguyên (người nghe chưa rõ): 2244, 2524 (phát biểu trước nhóm), 2404 (người nghe không xác định được — Fukami/Michiko → "anh", Akai/Hachiroku → "tôi").
- Không sai có chủ đích: 2143 "cô ấy" chỉ tuyến Yunoi (TW dùng 她); 2604 "cô ấy" chỉ Paulette ngôi thứ ba trang trọng với Akai; 2104 "cô ta" chỉ Kisaki (giọng khó chịu); 2968/2597 tag %l trên 8620 bị bỏ nhưng gloss bằng chính thuật ngữ nên không mất thông tin; 3129 dị thường tag JP (VN giữ nguyên y JP, cùng mẫu file 09 key 2482); 3126 義理 "trên danh nghĩa" giữ; 2023 "đau đầu" giữ; 2061/2597 Fukami "mình" với bạn học giữ; 1966/2489/2612 Hachiroku "tao/mày" giữ; 2525 "Cảm ơn mọi người." giữ; 2278 "mình" là phản thân 自分, không phải tự xưng; 2590 まいてつ "chủ tàu" đã đúng; 1926/2578/3158 đã đúng.
- Lượt soát 2: 35 tổng / 35 kiểm tra lại / 0 loại bỏ / 0 sửa lại. (Trước lượt soát 2, kiểm tra cơ học bắt được 31 giá trị fix bị cắt ngắn do bản in làm việc giới hạn độ dài — đã viết lại đầy đủ; quét bổ sung tìm thêm 1 fix 2117 với Reina.) Kiểm tra cơ học: ngoặc cân bằng 35/35, tag %l không đổi trừ 2492/2300.
- Ohitoyo 00_Common: đã sửa 6 lần ở file này; còn lại sau file này: 56 lần (14: 30, 15: 15, 13: 3, 01 pilot: 8 chưa chốt — file 11 đã sửa xong 12 lần).
- Còn lại chưa kiểm toán trong 00_Common: 13 (đang chạy song song), 14, 15, 末尾 (4 file; file 01 vẫn là bản nháp pilot).
- Deliverables: `audit-00common12-REVIEW.md`, `audit-00common12-wrong.json` (35 mục, key dạng chuỗi). Khối TOML trong review đã kiểm chứng parse: 35 key, 0 sai lệch giá trị.

**Tổng cộng sau file này: 55 file / 3.163 dòng sai** (cơ sở 54 file / 3.128 + 35 file này).

## 00_Common file 13 — 共通13_勾配図.txt.toml (20/11/2026)

**45/462 dòng sai (9,7%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng.**
- Thuật ngữ 12 (Ohimitera→Ohitoyo 3: 2076, 2267, 3237 — toàn bộ "Ohimitera" trong file; 湯医/湯医線→Yunoi 3: 2119, 2436, 2481 — toàn bộ "Yui" trong file; レール種別→"loại ray" 2: 1550, 2538; 運転体→"thân vận hành" 2: 1878, 2948 — 2948 kèm khôi phục thẻ %l bị rớt, chính là lệch đếm %l 69 vs 68 của file; 宮司→"đền chủ" 2: 2707, 2941 — biến thể "thầy Akai", như file 12 key 3038), đại từ 20 (Soutetsu gọi Hachiroku "cô"→"em" 11: 1537, 1568, 1892 [×2], 1925, 2126, 2215, 2271, 2335, 2380, 2498, 2514 [×2]; Soutetsu gọi Fukami "cô"→"em" 2: 1904, 1906 [×2] — 1903 gọi thẳng tên Fukami; Soutetsu tự xưng "anh"→"tôi" với Hachiroku 2: 2218, 2333; Nagi gọi Fukami "chị/em" 3: 2151, 2153, 2156 — quy tắc file 10; Hachiroku gọi Soutetsu "cô"→"ngài" 1: 2329 — cô ấy chấm điểm cho Soutetsu; Hachiroku gọi Hibiki "cô ấy"→"em ấy" 1: 2512), gasp 7 (toàn bộ từ sweep, áp nguyên đã kiểm chứng: 1874, 1927, 2028, 2533, 2534, 2535, 2810), SFX 5 (2023 ひあっ→"Hia", tiền lệ lr_h1 1005; 2033 ふぁ→"phà"; 2038 ふぇ→"Phuêêêêê!?"; 2052 ふうむ→"Hừừm." theo công thức độ dài nguyên âm; 2432 ふぇ→"phuê"), meaning 1 (2349 のぼせてアテられた "say sóng"→"choáng váng", TW 泡暈).
- Thoại 40/276 sai (14,5%), độc thoại 5/186 sai (2,7%). Theo nhân vật: 双鉄 25, ハチロク 6, 凪 5, monologue 5, ふかみ 4.
- Nguồn sạch: CSV bộ duy nhất 00_Common; VN khớp tuyệt đối 188, khớp sau khi gộp dòng 271/462, 3 khác biệt (2038, 2271, 2965) đều là hiện tượng gộp `\n` trong TOML, không phải lỗi dịch. TOML md5 db85026889f356064969c0e2745af096, 96.458 byte, BOM + CRLF, [selections] rỗng, không có bản sao trùng. 0 hàng chưa dịch, 0 key trùng; 1 hàng VN == TW là 1557 (「…………」 giống hệt JP/TW, hợp lệ).
- Sweep っ: kiểm tra trực tiếp sweep-raw-gasp-wrong.json — file này CÓ 8 mục (7 fix + 1 already-rendered 2057), cả 7 giá trị đúng, đã nhận. Quét bổ sung toàn bộ 180 dòng JP chứa っ: còn lại đều là っ nhấn mạnh hoặc âm đã render. Không có gasp nào sweep bỏ sót trong file này.
- Thẻ %l: JP 69 thẻ, VN 68 thẻ — lệch đúng 1 thẻ ở 2948 (bản Việt làm rớt cả thẻ), fix đã khôi phục. Không có thẻ đóng sai định dạng.
- Nhiễm chéo: tra chỉ mục VN toàn dự án — 1 lần trùng bề ngoài (2959 với 日々姫05 3069) nhưng JP hai dòng gần như giống hệt nhau (わかる。僕も同じであるから / わかる。僕もおんなじだから), là dòng lặp hợp lệ. Không nhiễm chéo.
- Phán đoán giữ nguyên: 1898 "anh sẽ đứng ra" — người nghe là các cô gái (TW 你們 số nhiều + nội dung xin phép người giám hộ), không phải Hachiroku; fix "anh"→"tôi" ở đợt đọc đầu đã bị loại bỏ sau khi kiểm tra lại. Các dòng không sửa khác: 1519 Tororyu-yu (tên riêng), 1571 "Đẹp quá" (JP thắng TW), 1907 "bám vào anh đi" (người nghe Fukami/Nagi đều gọi "anh"), 2057 already-rendered, 2503 "Bà chủ" (TW 她說), 3307 "mày ơi" (tự nhủ).
- Lượt soát 2: 45 tổng / 45 kiểm tra lại / 0 loại bỏ / 0 sửa lại.
- Ohitoyo 00_Common: đã sửa 3 lần ở file này; còn lại sau file này: 53 lần (14: 30, 15: 15, 01 pilot: 8 chưa chốt — file 12 đã sửa xong 6 lần, file 11 đã sửa xong 12 lần).
- Còn lại chưa kiểm toán trong 00_Common: 14, 15, 末尾 (3 file; file 01 vẫn là bản nháp pilot).
- Deliverables: `audit-00common13-REVIEW.md`, `audit-00common13-wrong.json` (45 mục, key dạng chuỗi). Khối TOML trong review đã kiểm chứng parse: 45 key, 0 sai lệch giá trị.

**Tổng cộng sau file này: 56 file / 3.208 dòng sai** (cơ sở 55 file / 3.163 + 45 file này).

## 00_Common file 14 — 共通14_負債.txt.toml (20/11/2026)

**52/411 dòng sai (12,7%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng.**
- Thuật ngữ 32 (Ohimitera→Ohitoyo 30: 1082, 1128, 1137, 1411, 1461, 1467, 1487, 1499, 1520, 1529, 1551, 1569, 1637, 1657, 1662, 1671, 1686, 1731, 1735, 1766, 1797, 1805, 1831, 1834, 1896, 1928, 2404, 2488, 2642, 2674 — đúng con số ~30 đã đếm trước đó; Yui→Yunoi 4: 1435, 1571, 1671, 1805 — 1671 và 1805 trùng với Ohimitera, cùng dòng; 帝鉄→Teitetsu 1: 1717), đại từ 15 (Soutetsu tự xưng "em"→"tôi"/"anh" 5: 1471, 1554, 1555, 1832 → "tôi", 1874 → "anh" với Hibiki; Soutetsu "Anh"→"Tôi" 2: 1407 với Kisaki, 1418 với ngân hàng; Soutetsu "tôi"→"anh" với Paulette 2: 1527, 1599; Paulette "mình"→"em" 1: 1529, kèm Ohimitera; Soutetsu gọi Paulette "cô"→"em" 1: 1858; Soutetsu "Cảm ơn cô"→"Cảm ơn chị" 1: 1559 với Mayami — phán đoán từ ngữ cảnh, xem review §7; độc thoại "Em"→"Tôi" 2: 2152, 2402), gasp 3 (1443, 1549, 1550 — cả 3 từ sweep, đã kiểm chứng đúng), tag 1 (1548 — VN tự thêm tag %l cho 8620; 1571 cũng gỡ tag nhưng tính vào thuật ngữ), nhỏ 1 (2686 — dấu ・ Nhật → " và ").
- Thoại 44/236 sai, độc thoại 8/175 sai. Theo nhân vật: 双鉄 26, monologue 8, ポーレット 8, 日々姫 5, 浦上 3, 稀咲 1, 元忠 1.
- Nguồn sạch: CSV bộ duy nhất 00_Common; VN khớp tuyệt đối 136, khớp sau khi gộp dòng 274/411, chỉ 1 khác biệt ở 1955 (TOML-2 làm phẳng \n thành khoảng trắng — hiện tượng đã biết; CSV3 tin cậy; VN ở 1955 đúng, không sửa). TOML md5 1c10d754dc7442a5347c67bbdec03f99, 93.437 byte, BOM + CRLF, [selections] rỗng, không có bản sao trùng.
- Sweep っ: kiểm tra trực tiếp sweep-raw-gasp-wrong.json — file này CÓ 3 mục (1443, 1549, 1550), cả 3 giá trị đúng, đã nhận (1443 đã khôi phục dạng \n của CSV3 vì giá trị sweep bị làm phẳng). Quét bổ sung toàn bộ 143 dòng JP chứa っ: còn lại đều là っ trong từ, っ nhấn mạnh cuối câu, hoặc âm đã render. Không có gasp nào sweep bỏ sót trong file này.
- Nhiễm chéo: tra chỉ mục VN toàn dự án — chỉ 3 cặp VN trùng, JP tương ứng cũng giống nhau (1116/1117 「…………」, 1535/1561 「うん」, 1501/1748 「なるほど」) — dịch độc lập giống nhau. Không nhiễm chéo.
- Phán đoán giữ nguyên: 2206/2317 義理の弟/義理の兄 → "em trai nuôi"/"anh trai nuôi" (TW nói 義弟/義兄 — em/anh kết nghĩa, khớp bối cảnh nhận nuôi; khác file 06 vì ở đó TW nói 血緣關係); 1407 "em ấy" (đại từ ngôi thứ ba, người được chỉ chưa xác định); 1465/1469 "tôi" (người nghe là ngân hàng, không phải Hibiki); 1533 "Cảm ơn cô" = Kisaki (khác 1559 = Mayami); 1838 "anh" (người nghe có khả năng là Reina); 1990 "Cảm ơn anh" = Urakami; 2482 "em ấy" = Paulette (luồng 2479→2482); 1935 "Đi rồi lại lùi" (diễn đúng thao tác quay đầu trên đường tam giác).
- Lượt soát 2: 52 tổng / 52 kiểm tra lại / 0 loại bỏ / 0 sửa lại. (Trước lượt soát 2, quét cơ học bắt lại 7 dòng Ohimitera bị bỏ sót khi đọc mắt: 1467, 1487, 1520, 1662, 1671, 1731, 1797.) Kiểm tra cơ học: mỗi fix chỉ khác VN cũ đúng ở chỗ sửa có chủ đích (52/52).
- Ohitoyo 00_Common: đã sửa 30 lần ở file này (30/30 — đúng con số đã đếm); còn lại sau file này: 23 lần (15: 15, 01 pilot: 8 chưa chốt — file 13 đã sửa hết 3 lần của nó trong audit song song).
- Còn lại chưa kiểm toán trong 00_Common: 15, 末尾 (2 file; file 01 vẫn là bản nháp pilot, file 13 đã xong song song).
- Deliverables: `audit-00common14-REVIEW.md`, `audit-00common14-wrong.json` (52 mục, key dạng chuỗi). Khối TOML trong review đã kiểm chứng parse: 52 key, 0 sai lệch giá trị.

**Tổng cộng sau file này: 57 file / 3.260 dòng sai** (cơ sở 56 file / 3.208 + 52 file này).

## 00_Common file 末尾 — 共通末尾_ルート分岐.txt.toml (20/11/2026)

**0/3 dòng sai (0%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng.**

- File rẽ nhánh route cuối Common: **chỉ 3 dòng, tất cả ở `[selections]`**, không có dòng `[script]` nào. TOML md5 `23c4c00fa9c23dcdf341575bf7864238`, BOM + CRLF, không trùng lặp.
- Cả 3 dòng lựa chọn đều dịch đúng (TW 「Xの意見を参考にする」 → "Tham khảo ý kiến của X": Hachiroku 103, Paulette 107, Hibiki 126). Không có thuật ngữ đã chốt, không đại từ, không tag %l, không っ, không bịa thêm.
- Sweep: 0 mục cho file này (đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`). Nhiễm chéo: mỗi chuỗi VN chỉ xuất hiện đúng 1 lần trong toàn dự án, ở chính file này. CSV↔TOML khớp 3/3.
- Lượt soát 2: 0 tổng / 0 kiểm tra lại / 0 loại bỏ / 0 sửa lại.
- Ghi chú không tính lỗi: `[info] 122 = "回り始める動輪"` là tiêu đề của file 15 (metadata nhân bản, file 14/15 có `[info]` rỗng) — không ảnh hưởng game. Việc 3 lựa chọn hiện tiếng Trung trong game là vấn đề build đã được Hieu park từ 19/11, không phải lỗi dịch.
- Deliverables: `audit-00common-matsubi-REVIEW.md`, `audit-00common-matsubi-wrong.json` (0 mục). Khối TOML trong review đã kiểm chứng parse: 0 key, 0 sai lệch giá trị.
- Ohitoyo 00_Common: không đổi, còn lại **23** (15: 15, 01 pilot: 8 chưa chốt).
- Còn lại chưa kiểm toán trong 00_Common: 15 (đang chạy song song), 01 pilot (bản nháp 35/155, cần audit đầy đủ).

**Tổng cộng sau file này: 58 file / 3.260 dòng sai** (cơ sở 57 file / 3.260 + 0 file này).

## 00_Common file 15 — 共通15_回り始める動輪.txt.toml (20/11/2026)

**27/492 dòng sai (5,5%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng.**
- Thuật ngữ 18 (Ohimitera→Ohitoyo 14 dòng / 15 lần: 1544, 1795, 2064 [×2], 2173, 2307, 2308, 2312, 2339, 2673, 2895, 2903, 2942, 3307, 3358 — toàn bộ "Ohimitera" trong file; 運転体→"thân vận hành" 3: 1516, 2619, 2938; 整備体→"thân bảo trì" 1: 3140; タブレット→"máy tính bảng" 1: 2619 — cùng dòng với 運転体; 帝鉄→"Teitetsu" 1: 3108; 湯医線→"tuyến Yunoi" 1: 2903 — dòng "Yui" thứ 8 toàn dự án; key 2308 tính vào đại từ nhưng đồng thời sửa 1 Ohimitera, tổng dòng chạm thuật ngữ là 19), đại từ 5 (Hibiki "chị"→"em" 2: 1843 [×2], 2132 [×3]; Soutetsu "cô"→"em" 1: 1943; Soutetsu "anh"→"tôi" với Hachiroku 2: 2063, 2308), meaning 2 (1541 bịa "Dù" + mất 確かだ; 1951 "rất biết ơn" bịa thêm), gasp 1 (1906 từ sweep, đã kiểm chứng), SFX 1 (2378 ぐぎぎぎ nghiến răng → "Ken két").
- Thoại 17/251 sai (6,8%), độc thoại 10/241 sai (4,1%). Theo nhân vật: 双鉄 6, 日々姫 4, ハチロク 4, monologue 10, 蓑笠 1, ポーレット 1, 凪 1.
- Nguồn sạch: CSV bộ duy nhất 00_Common; VN khớp tuyệt đối 194, khớp sau khi gộp dòng 294/492, 4 khác biệt đều là hiện tượng gộp `\n` trong TOML, không phải lỗi dịch. TOML md5 3e8962a81d4d874c12d33ca89c7a201c, 106.839 byte, BOM + CRLF, [selections] rỗng, không có bản sao trùng. 0 hàng chưa dịch, 0 key trùng; 1 hàng VN == TW là 1517 (「…………」 giống hệt JP/TW, hợp lệ).
- Sweep っ: kiểm tra trực tiếp sweep-raw-gasp-wrong.json — file này CÓ 2 mục: 1906 áp nguyên đã kiểm chứng; **1474 BÁC — audit thắng sweep** (JP ブロワーっ！！ là っ nhấn mạnh cuối câu gắn thuật ngữ hô to, VN đã diễn bằng "!!"; mẫu giống hệt 1835/1973/2000/2113 chưa từng diễn thành Ư). Quét bổ sung toàn bộ 174 dòng JP chứa っ: không có gasp nào sweep bỏ sót.
- Thẻ %l: JP 284 = VN 284, khớp tuyệt đối; không có thẻ đóng sai định dạng trong VN. JP có 4 thẻ đóng sai phía nguồn (1501, 2594, 2858, 2927) nhưng VN đã chuẩn hoá — không phải lỗi VN.
- Nhiễm chéo: tra chỉ mục VN toàn dự án — 155 lần trùng đều là câu ngắn thông dụng dịch độc lập giống nhau; 0 lần trùng VN trong file với JP khác nhau. Không nhiễm chéo.
- Phán đoán giữ nguyên / **CÂU HỎI QUY TẮC CẦN QUYẾT: Nagi gọi Soutetsu にーさん ("anh hai") 326 lần toàn dự án (vs "anh Soutetsu" 64 lần) — theo nguyên tắc xưng hô tương hỗ, Soutetsu là "anh" với Nagi, MÂU THUẪN với nhánh "tôi với Nagi" của quy tắc đã sửa 20/11. 1461/2078 giữ "anh", KHÔNG sửa thành "tôi" — parent quyết xem có sửa quy tắc không.** Các dòng giữ khác: 1914/1938 "tôi" trong suy ngẫm nhóm (1938 không nhất quán với 1936 "anh" với Fukami — ghi chú phán đoán); 1775/2157 Hachiroku→Hibiki "chị Hibiki" (đa số 8 vs "cô" 1); 2158 Minokasa→Soutetsu bare "Soutetsu!" (đa số 6 vs "Cậu Soutetsu" 2); 1775/2171 "Thị trưởng Paulette" (100+ lần); 2054 Michiko tự xưng "em" (đa số 23 vs "chị" 15 — chờ unification); 2366 凪様→"Nagi" (vocative); 3119 "của anh" trong tường thuật (góc nhìn Hibiki, 2332); しゅ/しゅん → "xình, xịch" (31, 2774, 2792 — phong cách nhất quán).
- Lượt soát 2: 27 tổng / 27 kiểm tra lại / 0 loại bỏ / 0 sửa lại. Kiểm tra cơ học: mỗi fix khác VN cũ CHỈ ở chỗ sửa có chủ đích (difflib, 27/27).
- Ohitoyo 00_Common: đã sửa 15 lần ở file này (15/15 — đúng con số đã đếm); còn lại sau file này: **8 lần** (01 pilot: 8 chưa chốt — toàn bộ "Ohimitera" còn lại trong 00_Common).
- Còn lại chưa kiểm toán trong 00_Common: chỉ còn file 01 pilot (bản nháp 35/155, cần audit đầy đủ).
- Deliverables: `audit-00common15-REVIEW.md`, `audit-00common15-wrong.json` (27 mục, key dạng chuỗi). Khối TOML trong review đã kiểm chứng parse: 27 key, 0 sai lệch giá trị.

**Tổng cộng sau file này: 59 file / 3.287 dòng sai** (cơ sở 58 file / 3.260 + 27 file này).

## 00_Common 01 — 共通01_右田双鉄の帰還 — 48/155 (31,0%)

- File mở đầu game, kiểm tra ĐẦY ĐỦ thay thế bản pilot 19/11 (35/155, nháp). Pilot: 30 fix giữ nguyên, 4 sửa lại/mở rộng (1173, 1335, 1430, 1628), 1 bỏ (992 — CSV3 đã đúng, pilot sửa lỗi làm phẳng của TOML-2). 13 fix mới: 4 gasp sweep (1247, 1317, 1375, 1382; 1430 gộp), 7 Ohitoyo, 2 Migita + 1 fix do parent bổ sung theo quyết định của Hieu (1027 — bỏ "dồn toa").
- Phân loại: terminology 10 (Ohitoyo 8, Migita 2), meaning 22, pronoun 4, minor 7, gasp 4. Hội thoại 33/111 (29,7%), độc thoại 14/44 (31,8%).
- 0 misaligned / 0 rotation / 0 contamination (chỉ mục VN toàn dự án: 0/48) / 0 orphan / 0 untranslated / 0 duplicate key / 0 uncertain.
- CSV↔TOML: 58 khớp tuyệt đối + 97 làm phẳng `\n`, 0 khác biệt thực chất; JP comment 171 dòng, 0 lệch. Thẻ `%l`: JP = VN mọi dòng.
- Sweep: 5 mục, 4 áp nguyên + 1430 gộp; quét 59 dòng JP có っ, không còn gasp sót (1238 おっと đã dịch đúng).
- Lượt soát 2: 47/47 tái kiểm chứng, 0 bỏ, 0 sửa + 1 fix parent bổ sung (1027) kiểm chứng 1/1. JSON 48 khóa chuỗi; khối TOML parse OK, 48 khóa, 0 sai lệch.
- Phán đoán ghi chú: 1173 bỏ "Hôm nay", giữ câu 2 theo TW; 1335 gloss "Đường sắt Đế quốc" (tooltip lần đầu, quyết định #6); 1027 "phun cát dồn toa" ĐÃ CHỐT (Hieu 20/11 02:03: bỏ "dồn toa" → "Kiến nghị phun cát."); quy tắc Nagi mới (Soutetsu "anh" với Nagi) không ảnh hưởng file này — Nagi không xuất hiện.
- Ohitoyo trong 00_Common sau file này: còn 0 — 00_Common đã hết Ohimitera (134/134 đã sửa).

**Tổng cộng sau file này: 60 file / 3.335 dòng sai** (cơ sở 59 file / 3.287 + 48 file này — parent bổ sung 1027 theo quyết định của Hieu 20/11 02:03).

## 05_Mayami lr真闇追加01 — 新婚旅行のリクエスト — 142/300 (47,3%)

- File thêm về tuần trăng mật (Soutetsu + Mayami bàn lịch trình trên Navi, chọn Reina làm hướng dẫn viên), kiểm tra ĐẦY ĐỦ 300 dòng. File bẩn thứ ba dự án (sau Hibiki 03 86,2% và obasan 56%), gần một nửa sai — gần như toàn bộ là lệch hàng: 2 chuỗi xoay (A: 114 mắt xích, đầu là bản của 1036 → 1177 → … → 1736; B: 9 mắt xích, 1175 → 1283 → … → 1264), khép kín trong file, 0 dòng mồ côi.
- Phân loại: misaligned 125 (123 thu hồi + 1 dịch mới 1036 + 1 lặp hợp lệ 1175), terminology 8, pronoun 7, gasp 2. Hội thoại 109/229 (47,6%), độc thoại 33/71 (46,5%).
- 0 contamination (chỉ mục VN toàn dự án: 0/142) / 0 orphan / 1 untranslated (1264 — thu hồi bản đúng từ key 1744; dòng chưa dịch còn lại toàn dự án nằm ở lr真闇追加02) / 0 duplicate key / 0 uncertain.
- CSV↔TOML: 76 khớp tuyệt đối + 223 làm phẳng `\\n`, 1 khác biệt thực chất (1264: TOML giữ văn TW làm placeholder, CSV trống). Thẻ `%l`: JP 0, VN 0.
- Sweep: 2 mục (1077, 1657), cả 2 áp nguyên văn sau khi kiểm chứng trực tiếp; quét 150 dòng JP có っ, không còn gasp sót (1080 うふふっ và 1097 わああっ là dòng lệch, bản đúng đã có tiếng cười/tiếng hét; 1474 là っ giữa từ ってことは, không phải gasp).
- Lượt soát 2: 142/142 đọc lại đối chiếu JP, 139 tái kiểm chứng, 0 bỏ, 3 sửa (1036, 1077, 1175 — cả 3 đều thiếu dấu 「 」 trong bản viết tay, đã bổ sung và chạy lại toàn bộ kiểm chứng máy). JSON 142 khóa chuỗi; khối TOML parse OK, 142 khóa, 0 sai lệch.
- Phán đoán ghi chú: 1086 んふふっ → "Ưm fufu" giữ nguyên (tiếng ưm mũi + cười, không phải rên; nhất quán với bản ở 1271); 1087 おっと → "Ây da" giữ nguyên (cảm thán hợp lệ, cùng họ với あら/ありゃ trong file); 1606 路子 = Michiko dịch đúng theo JP (TW lược, JP thắng); 1479 Soutetsu "anh nhờ em" với Reina là ĐÚNG (Reina thuộc nhóm "anh"); 1494 giữ gloss "xúc than" cho 投炭 (đa số trong file), chỉ bỏ "dồn toa" theo quyết định 1027 của Hieu. Lượt quét đại từ bắt thêm 1 lỗi lần đọc đầu bỏ sót (1281 "em"→"tôi"); quét lại toàn bộ bản thu hồi bắt thêm 3 lỗi "em"→"tôi" trong bản thu hồi (1071, 1249, 1283).
- Ohitoyo trong file: 13 dòng đã sửa (7 thuật ngữ thuần + 6 trong bản thu hồi) — còn 0. Yui→Yunoi: 2 dòng — còn 0. Migita System→Migita Ichi: 1 dòng — còn 0. "dồn toa": 1 dòng (1494) — còn 0.
- Parent kiểm chứng 20/11 ~04:20: JSON 142 khóa chuỗi, khối TOML 142 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 142/142; 122/122 claim thu hồi đối chiếu nguồn — 106 nguyên văn, 16 chỉ khác ở sửa có chủ đích (Ohimitera→Ohitoyo, "em"→"tôi", "System"→"Ichi", thêm " nó" 1446), 0 sai lệch lớn; 1264 thu hồi từ 1744 đã kiểm chứng; 7 fix đại từ kiểm chứng theo thứ tự TOML (đối tượng đều là Mayami → "tôi" đúng); 3 sửa lượt 2 (1036/1077/1175) đều đã có 「 」 trong khối cuối. Sửa nhỏ của parent khi gộp: "file bẩn thứ nhì" → "thứ ba" (47,3% < obasan 56%).

**Tổng cộng sau file này: 61 file / 3.477 dòng sai** (cơ sở 60 file / 3.335 + 142 file này).

## lr_凪ふかみh1 — lr_凪ふかみh1_じぇいけい！.txt.toml — 62/404 (15,3%)

- H-scene Soutetsu + Nagi + Fukami (file "JK": Soutetsu mặc đồng phục nữ sinh). Hai lỗi hệ thống: 凪さま 9/9 chưa sửa thành "Bổn tiểu thư" (tiền lệ P08 2277, P01 1683; TW 本小姐 9/9); ふぁ/ふあ romanised 22 dòng (20 sửa riêng + 2 gộp trong fix meaning). 3 dòng romaji nguyên vẹn (1375, 1545, 1550) dịch theo TW. 腰を振る → "đẩy hông" 2 dòng (994, 2182).
- Phân loại: terminology 16 (凪さま 9, 現役 8 — 1519 mang cả hai), meaning 10, pronoun 1 (1455), sfx 20, gasp 15. Hội thoại 55/275 (20,0%), độc thoại 7/129 (5,4%).
- 0 misaligned / 0 rotation / 0 contamination (chỉ mục VN toàn dự án: 10 lần trùng đều là câu ngắn thông dụng hoặc SFX lặp lại hợp lệ) / 0 orphan / 0 untranslated / 0 duplicate key / 0 uncertain.
- CSV bộ duy nhất 404 dòng; CSV↔TOML flat-match 404/404. TOML md5 ef960cfc3776057ff0cbcad101eb4875, BOM + CRLF, [selections] rỗng, không bản sao trùng. Thẻ %l: JP = VN mọi dòng.
- Sweep: 17 mục — 13 fixed áp nguyên (gồm 2121, 2217 chunk-4 bỏ sót), 1 override (1563, sweep ghi already-rendered), 1 sweep-missed bắt được (1624), 2 already-rendered giữ (1395, 1495), 1 needs-file-audit không sửa (1838). Quét hệ thống 288 dòng JP có っ: không còn gasp sót.
- Lượt soát 2: 62/62 tái kiểm chứng, 0 bỏ, 0 sửa. JSON 62 khóa chuỗi; khối TOML parse OK, 62 khóa, 0 sai lệch.
- Phán đoán ghi chú: 1378/1842 "anh" GIỮ (thoại có 「」, không phải độc thoại — quy luật 「」 tuyệt đối: 129/129 dòng monologue không 「」, 275/275 dòng thoại có 「」); ぷぁ/ぷは/ぷあ 6 dòng giữ "Pua/Puha" chờ quyết chung; 1708/1825 borderline thoại/suy ngẫm; 1746 Fukami "tớ" vs "chị" chờ unification pass.
- Parent kiểm chứng 20/11 ~04:20: JSON 62 khóa, khối TOML 62 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 62/62; 凪さま 9/9 JP + TW 本小姐 9/9 → "Bổn tiểu thư" 9/9; Fua/fua 21 dòng cũ → Phà/phà 21; 1455 "anh" đúng (đối tượng Nagi/Fukami đều nhóm "anh").

**Tổng cộng sau file này: 62 file / 3.539 dòng sai** (cơ sở 61 file / 3.477 + 62 file này).

## lr_凪h2 — lr_凪h2_虎さんの交尾.txt.toml — 46/293 (15,7%)

- H-scene Soutetsu + Nagi (Nagi mặc đồ lót tai-đuôi hổ đặt mua online nhưng không có vằn, đòi trả hàng trước khi làm tình). Lỗi hệ thống duy nhất: ふぁ/ふあ romanised 38 dòng (quy tắc fa/fu đã chốt 19/11; 1247 gộp gasp). Không có lỗi đại từ hay thuật ngữ nào.
- Phân loại: sfx 38 (ふぁ→"phà" 17, ふあっ→"phù" 19, ふあ không っ→"phùa" 3 + 1 dòng cắt bởi ――→"phù" 1232, ふぇ→"phuê" 1, ふやっ→"phuya" 1, ふっ→"phù" 1 — 1199 mang cả 3, 1273/1304/1280 mang 2), gasp 7 tính riêng (1247 mang cả gasp + fa/fu, tính vào sfx; tổng 8 dòng chạm gasp), meaning 1 (1124 thiếu động từ "làm"). Thoại 46/170 (27,1%), độc thoại 0/123. Theo nhân vật: 凪 45, 双鉄 1.
- 0 misaligned / 0 rotation / 0 contamination (chỉ mục VN toàn dự án: 31 lần trùng đều là câu ngắn thông dụng hoặc SFX lặp lại hợp lệ; 2 cặp trùng trong file 1295/1332, 1296/1266 đều là cảm thán ngắn hợp lệ) / 0 orphan / 0 untranslated / 0 duplicate key / 0 uncertain.
- CSV bộ duy nhất 293 dòng; CSV↔TOML: 131 khớp tuyệt đối + 162 gộp \\n thành khoảng trắng, 0 khác biệt thực chất; JP comment 293/293 khớp CSV3. TOML md5 4f26c5ed7e6e0d076848d8be1add75a7, BOM + CRLF, [selections] rỗng, không bản sao trùng. Thẻ %l: JP = VN = 0.
- Sweep: 6 mục — 6 áp nguyên đã kiểm chứng (1220, 1221, 1222, 1247, 1268, 1296); 2 gasp sweep bỏ sót bắt được khi quét bổ sung 223 dòng JP có っ (1185: っ trần giữa dòng "っ――"; 1339: "――っ、くっ――" hai tiếng nhưng VN chỉ diễn một). Không còn gasp sót.
- Lượt soát 2: 46/46 tái kiểm chứng, 0 bỏ, 0 sửa. JSON 46 khóa chuỗi; khối TOML parse OK, 46 khóa, 0 sai lệch.
- Phán đoán ghi chú: 1297 けんっ→"Rồi!" giữ (tiểu từ phương ngữ Hakata); 1193/1241 giữ (JP rời rạc tương tự / hai tiếng đều có âm); tiếng cười La-tinh giữ chờ quyết chung (1258 "fufufu-n", 1391 "fufu", 1308/1313/1314 "Nhehe"/"Ehehe"); ぷあ/ぷぁ giữ "Pua"/"Npua" (1225, 1227, 1255, 1285 — tiền lệ file h1 cùng route); SFX La-tinh khác giữ chờ quyết chung (Hyau/Hya/Nhyu/Nku/Aku/Kyaa/Wa/Hie/Hyan/Hyawawa/Au/Nkyuu/Hyuaaaaaa/zujuuu/hi-hamu/hyuki — quy ước lr-h1/lr-h2 chưa phải quy tắc đã chốt); 1305 marker giọng nói [とらなぎ,1] bỏ qua đúng lệ (4 lần toàn dự án đều bỏ); 1243 ruby [ぬく] đã diễn "ấm quá"; 1325 "Anh——Soutetsu——" chỉ là ngắt bởi gạch; 1266 "!" đúng (JP không っ) vs 1296 đã sửa "Ư!"; 1377 無論 = むろん "đương nhiên" (từ Nhật hợp lệ).
- Ngoài phạm vi file này: 日々姫03 key 2409 có VN "Vài ngày sau." rõ ràng lệch với JP — để queue audit riêng.
- Parent kiểm chứng 20/11 ~04:30: JSON 46 mục (dạng fix-only `{key: fix}`, khác dạng chuẩn có jp/tw/old_vn — old_vn đã đối chiếu từ review thay vì JSON), khối TOML 46 khóa, 0 sai lệch giá trị; old_vn trong review khớp CSV3 tuyệt đối 46/46; 38 dòng cũ chứa "fua" khớp 38 fix sfx; lượt soát 2 ghi trong review (46/46, 0 bỏ, 0 sửa). Flag Hibiki 03 key 2409 đã kiểm chứng: đúng là VN lệch ("Vài ngày sau." vs JP dài về 機関助士) NHƯNG đã nằm trong fix list audit Hibiki 03 (374 mục) — không cần audit riêng.

**Tổng cộng sau file này: 63 file / 3.585 dòng sai** (cơ sở 62 file / 3.539 + 46 file này).

## 07_Nagi_Fukami 凪ふかみ08b — ふかみエピローグ_赤を切る勇気 — 69/609 (11,3%)

- Fukami epilogue (Fukami làm trưởng tàu, phóng viên phỏng vấn về "cắt cờ đỏ"). Kiểm tra ĐẦY ĐỦ 609 dòng (372 thoại, 237 độc thoại). Hoàn thiện từ bản nháp bị ngắt: agent đầu tiên chốt 100 bản sửa rồi bị timeout cron; agent hoàn thiện kiểm chứng cơ học 100/100 + đọc lại lần 2 từng bản đối chiếu JP + TW, **loại 31 bản** (xem dưới), còn 69.
- Phân loại (69): terminology 29 (Ohitoyo 16, Teitetsu 2, Yunoi 2, Teiou 1, hoán đổi gloss 機関士/運転士 9 — 2698 mang cả Ohitoyo), pronoun 1 (2436 Paulette → Soutetsu "anh Soutetsu", khóa B4), gasp 2 (2250, 2405, sweep áp nguyên), meaning 1 (2754 Fukami tự sửa おにー→さん, TW xác nhận), sfx 2 (2174/2176 ふぁっ → "Phà"), tag 34 (gỡ thẻ gloss %l do Gemini tự thêm; 7 dòng khác gỡ thẻ kèm sửa thuật ngữ nên tổng 41 dòng chạm thẻ). Thoại 48/372 (12,9%), độc thoại 21/237 (8,9%).
- 0 misaligned / 0 rotation / 0 contamination / 0 orphan / 0 untranslated / 0 duplicate key / 0 uncertain.
- CSV bộ duy nhất 609 dòng; CSV↔TOML: 243 khớp tuyệt đối + 366 gộp `\\n` thành khoảng trắng, 0 khác biệt thực chất; JP comment 609/609 khớp CSV3. TOML md5 393abd804e7ab4835e9d94b92ba53a75, BOM + CRLF, [selections] rỗng, không bản sao trùng. Thẻ %l: chỉ 2411 còn 1 thẻ (đúng thẻ 入換 của JP).
- Sweep: 3 mục — 2250, 2405 áp nguyên đã kiểm chứng trực tiếp; 2232 already-rendered (VN "Á!!!" đã diễn gasp — không sửa).
- Lượt soát 2: 100 tổng / 69 tái kiểm chứng / 31 loại bỏ / 0 sửa lại. JSON 69 khóa chuỗi (đã viết lại từ dạng fix-only của agent đầu tiên, đủ jp/tw/old_vn/fix/kind/character); khối TOML parse OK, 69 khóa, 0 sai lệch.
- **31 bản sửa bị loại (§3 review): tiền đề "Fukami là chị lớn của Nagi" SAI.** Bằng chứng JP: ふかみh2 key 1118 — Fukami nói Hibiki trạc tuổi "em và Nagi" (わたしと凪ちゃんと同じくらいの年, TW 年紀差不多) → hai người bằng tuổi; key 2254 trong file này Nagi nói ba người là "bạn bè" (友達); TW gọi Fukami là 小深 ("bé Fukami") trong lời Nagi; toàn dự án Nagi gọi Fukami "bé" 58 lần vs "chị" 0 lần; Fukami tự xưng trong file này "Mình" 8 lần vs "Chị" 0 lần (2451 giữ "Mình"). Loại: Nagi → Fukami "bé"→"chị" 24 dòng, Fukami tự xưng "mình"→"chị" 5 dòng, Fukami → Nagi "cậu"→"em" 2 dòng (2473, 2655). Giữ nguyên VN cũ, ghi đầy đủ để đợt thống nhất quyết sau — đừng áp ngược "chị"/"em" nếu không có bằng chứng tuổi tác mới.
- Phán đoán ghi chú: 2285/2320/2411/2522 giữ gloss "dồn toa" cho 入換 (quy ước chung, quyết định 1027 của Hieu chỉ bỏ "dồn toa" trong câu 砂撒き); 2156 "Teiou" đúng (JP 帝央 [ていおう], không phải "Teito"); 2754 không thuộc mẫu tự sửa さん→くん ở file 07 (đây là おにー→さん, TW 雙鐵哥……雙鐵先生 xác nhận).
- Parent kiểm chứng 20/11 ~05:00: JSON 69 mục dạng chuẩn, khối TOML 69 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 69/69; bằng chứng loại 31 bản đã kiểm chứng trực tiếp (ふかみh2 1118 JP đúng "cùng tuổi", 08b 2254 đúng "bạn bè"; đếm lại của parent: Nagi gọi "bé Fukami" 56 lần vs "chị Fukami" 0 lần toàn dự án — khớp hướng kết luận; 2473/2655 không còn trong JSON); fix đại từ giữ lại duy nhất 2436 đúng khóa B4 (JP 双鉄くん → "Anh Soutetsu"); 4 dòng giữ "dồn toa" đều có JP 入換, chỉ gỡ thẻ/sửa Teitetsu — không mâu thuẫn quyết định 1027 (chỉ áp cho câu 砂撒き).

**Tổng cộng sau file này: 64 file / 3.654 dòng sai** (cơ sở 63 file / 3.585 + 69 file này).

## 02_Hibiki 日々姫16 — 夢を乗せて — 16/400 (4,0%)

- Cảnh nghị viện + chạy tàu buổi sáng: Hibiki trả lời chất vấn về đồng hồ búp bê ga Ohitoyo, rồi cả nhóm chạy chuyến SL Ohitoyo; Soutetsu cầu hôn Hibiki trên buồng lái. Kiểm tra ĐẦY ĐỦ 400 dòng (215 thoại, 185 độc thoại).
- Phân loại (16): terminology 9 (まいてつ gloss "người đam mê đường sắt" → "chủ tàu" 3 — 2710, 2391, 2107, cả 3 dòng duy nhất toàn dự án dùng gloss này; 湯医 → "Yunoi" 2 — 2106, 1950; 整備ボディ → "thân bảo trì" 3 — 2609, 2408, 2340, 2340 kèm タブレット "thẻ bảng" → "máy tính bảng"; 運転ボディ → "thân vận hành" 1 — 2545), pronoun 6 (Soutetsu "anh"/"em" → "tôi" với Hachiroku 3 — 1709, 2084, 2087; với Kisaki 1 — 1893; với Mayami 1 — 2010 "Bên em" → "Bên tôi"; Paulette gọi Soutetsu thiếu "anh" 1 — 1719, khóa B4), gasp 1 (2683 raw-tsu, sweep áp nguyên sau kiểm chứng).
- 0 misaligned / 0 rotation / 0 contamination / 0 orphan / 0 untranslated / 0 duplicate key / 0 uncertain.
- CSV bộ duy nhất 400 dòng; CSV↔TOML: 361 khớp tuyệt đối + 39 gộp `\n` thành khoảng trắng, 0 khác biệt thực chất; JP comment khớp CSV3. TOML md5 c647cda50a94fe07d0b75fbcf3712a94, BOM + CRLF, [selections] rỗng, không bản sao trùng. Thẻ %l: tag parity OK 16/16, không thẻ hỏng trong file.
- Sweep: 2 mục — 2683 áp nguyên đã kiểm chứng; 1703 already-rendered (VN "Ưm~~" đã diễn gasp — không sửa).
- Lượt soát 2: 16 tổng / 16 tái kiểm chứng / 0 loại bỏ / 0 sửa lại. JSON 16 khóa chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 16/16; khối TOML parse OK, 16 khóa, 0 sai lệch.
- Phán đoán ghi chú: "Đường sắt Ohito" GIỮ (2107, 1994) — 215 lần toàn dự án vs "Đường sắt Ohitoyo" 5 lần, chờ Hieu/unification quyết có đổi tên công ty đường sắt không; "Ohimitera" 16 dòng GIỮ chờ thống nhất; "bọn anh" của Soutetsu GIỮ (1840, 1837, 1391) theo quy tắc dạng nhóm; Hachiroku bỏ 様 với Hibiki/Nagi (1735, 2111, 2109, 2119) — không nhất quán, cần quy ước; Nagi gọi Fukami tên trần ở 1788 (dự án "bé" 56×) — ghi chú thống nhất, tuyệt đối không đổi sang "chị"; 1868 義理の兄妹 → "anh em nuôi" GIỮ theo TW 義兄妹 (tiền lệ file 14); "dồn toa" cho 入換/入替 GIỮ theo quy ước 1027; gloss 機関助士 "phụ lái tàu" GIỮ (54× nhất quán); "Denshahime" GIỮ; 1685 っ cuối câu nhấn mạnh bỏ đúng, không thêm Ư.

- Parent kiểm chứng 20/11 ~05:22: JSON 16 mục dạng chuẩn, khối TOML 16 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 16/16; diff-sanity 16/16 chỉ khác ở chỗ sửa có chủ đích (tỉ lệ 0,82–0,99, không viết lại lớn); 6 fix đại từ kiểm chứng theo dòng kề: 1709 Hachiroku (1811 「何かあったのですか？」), 1893 Kisaki (1662 báo đơn mới), 2010 Mayami (1591 giao hàng), 2084/2087 Hachiroku (2089 「お二人」), 1719 đúng khóa B4 (Paulette 双鉄くん → "anh Soutetsu"); 2683 sweep áp nguyên đã kiểm chứng trực tiếp; lượt soát 2 ghi trong review (16/16, 0 bỏ, 0 sửa).
**Tổng cộng sau file này: 65 file / 3.670 dòng sai** (cơ sở 64 file / 3.654 + 16 file này).

## 07_Nagi_Fukami 凪ふかみ08c — 新しい家族 — 17/483 (3,5%)

- "Gia đình mới": Soutetsu kiệt sức ngã gục, Nagi + Fukami chăm sóc; anh đề xuất ba người thành một gia đình; họp toàn thể (Paulette, Kisaki, Hachiroku, Reina, Mayami, hai ông Minokasa + Seki) bàn "Đặc khu Hình thái Gia đình mới" và lập pháp hóa hợp đồng gia đình; kết 7 năm sau với "Gia đình được chứng nhận". Kiểm tra ĐẦY ĐỦ 483 dòng (339 thoại, 144 độc thoại).
- Phân loại (17): pronoun 8 (Soutetsu tự xưng "em"→"tôi" với Mayami 3: 2516, 2329, 2290; Soutetsu gọi Paulette "cậu"→"em" 2: 2290, 2131; Paulette "cậu Soutetsu"→"anh Soutetsu" 4: 1838, 2514, 1870, 2332 — khóa B4), meaning 3 (倒れる "ngã bệnh"→"ngã gục" 2: 1823, 2336; それぞれで "từng người"→"hai người một nhóm" 1: 2270), gasp 1 (2140 sweep áp nguyên), sfx 1 (2073 ふあっ "Oa"→"Phùa"), tag 3 (rò chữ JP trong ruby 2413; thẻ %l mang thuật ngữ TW 3071, 2996), typo 1 (2956 dấu `'` thừa). Thoại 14/339 (4,1%), độc thoại 3/144 (2,1%).
- 0 misaligned / 0 rotation / 0 contamination / 0 orphan / 0 untranslated / 0 duplicate key / 1 uncertain (2030 — giữ "anh", chờ Hieu).
- CSV bộ duy nhất 483 dòng; CSV↔TOML: 189 khớp tuyệt đối + 294 gộp `\n` thành khoảng trắng, 0 khác biệt thực chất; JP comment 483/483 khớp CSV3. TOML md5 57e635feca460be6e6b563f3201ab484, BOM + CRLF, [selections] rỗng, không bản sao trùng. Thẻ %l: 14 thẻ, 11 đúng; 3108 [窯] giữ nguyên (JP viết カマ = katakana của 窯).
- Sweep: 2 mục — 2140 áp nguyên đã kiểm chứng trực tiếp; 3052 needs-file-audit đã xử lý (VN "――hả!?" đã diễn gasp, không sửa).
- Lượt soát 2: 18 tổng / 17 tái kiểm chứng / 1 loại bỏ (2030, parent) / 0 sửa lại. JSON 17 khóa chuỗi; khối TOML parse OK, 17 khóa, 0 sai lệch. (Kiểm chứng cơ học phát hiện 12 bản sửa viết tay thiếu cặp ngoặc 「」 của VN cũ — đã bổ sung trước khi chốt; lỗi chép lại, không tính vào lượt soát 2.)
- Phán đoán ghi chú: Seki gọi "ông nội" hay "ông ngoại" — CÂU HỎI TOÀN DỰ ÁN, không sửa ở file này (Seki gọi Midori là 娘 ở 2456, Midori là mẹ Fukami → ông ngoại theo họ hàng Việt; nhưng toàn dự án đều dùng "ông nội" cho Seki — cần Hieu chốt). Nagi tự xưng "mình" (1984, 1995, 436) giữ nguyên. Grand01 còn sót 2 dòng Paulette "cậu Soutetsu" (2756, 2181) chưa sửa (audit trước đính chính B4) — báo để parent ghi nhận. Key 2030 LOẠI BỎ bởi parent: giữ "anh" (người nghe là Nagi 2029, 2554 thuộc cảnh khác), chờ Hieu chốt.
- Chờ thống nhất (không tính sai): "Ohito"→"Ohitoyo" 7 dòng / 8 lần (2585, 2199 ×2, 2196, 2041, 2420, 2341, 2248); "Yui"→"Yunoi" 2 dòng (2541, 2068).

- Parent kiểm chứng 20/11 ~05:40: JSON 17 mục (sau khi loại 2030) dạng chuẩn, khối TOML 17 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 17/17; diff-sanity 17/17 chỉ khác ở chỗ sửa có chủ đích (tỉ lệ 0,75–1,00); 8 fix đại từ kiểm chứng theo dòng kề: 2516/2329 Mayami (2491, 2216), 2290 hai đối tượng (nửa đầu Mayami qua 2491, nửa sau Paulette đích danh), 2131 "em" đúng cho cả Nagi lẫn Paulette, 4× B4 Paulette 双鉄くん→"anh Soutetsu"; 2270 TW xác nhận "hai người một nhóm", 2413 ruby JP dịch sang VN, 2140 sweep áp nguyên; lượt soát 2: 18 tổng / 17 tái kiểm chứng / 1 loại bỏ (2030) / 0 sửa lại. **2030 LOẠI BỎ: agent cho là trả lời Hachiroku ở 2554 nhưng 2554 thuộc cảnh khác (2550–2559), dòng kề là Nagi 2029 gọi "にーさん" — giữ VN cũ "anh", ghi uncertain, chờ Hieu.**
**Tổng cộng sau file này: 66 file / 3.687 dòng sai** (cơ sở 65 file / 3.670 + 17 file này).

## 04_Reina lrれいな追加01 — はじめての冬 — 15/322 (4,7%)

- "Mùa đông đầu tiên": Soutetsu và Reina ngồi sưởi sàn ăn quýt, xem album ảnh cũ của bác Denjirou và cô Kayoko (thời mỏ than Katakami, lớp bổ túc ban đêm 夜学), bàn khóa tu dưỡng tân nương và nhờ chị Mayami làm giáo viên; Mayami ghé qua sau một ngày làm ở xưởng rượu. Kiểm tra ĐẦY ĐỦ 322 dòng (233 thoại, 89 độc thoại).
- Phân loại (15): sfx-laughter 7 (977, 1111, 1168, 1170, 1174, 1177, 1178 — うふふ/うっふふ "Ư phu phu"→"Ufufu"), pronoun 4 (975, 1285 Soutetsu "tôi"→"anh" với Reina; 1155, 1312 "em"→"anh" với Reina), fa/fu 2 (1097 ふあぁーあ "Phu a~ a"→"Phùa~ a"; 1101 ふぁ "Phu a"→"Phà"), fabrication 1 (1051 "những di sản quý giá" bịa thêm), terminology 1 (1594 "Đường sắt Ohito"→"Đường sắt Ohitoyo"). Thoại 14/233 (6,0%), độc thoại 1/89 (1,1%).
- 0 misaligned / 0 rotation / 0 contamination / 0 orphan / 0 untranslated / 0 duplicate key / 0 uncertain.
- CSV bộ duy nhất 322 dòng; CSV↔TOML: 124 khớp tuyệt đối + 198 gộp `\n` thành khoảng trắng, 0 khác biệt thực chất; JP comment 322/322 khớp CSV3. TOML md5 91bbc47d045eb6f41187c89c5fd5255d, BOM + CRLF (666 CRLF, 0 LF-only), [selections] rỗng, không bản sao trùng. Thẻ %l: số lượng khớp JP mọi dòng, 0 thẻ thiếu `;`. Không có っ thô trong VN.
- Sweep: 0 mục cho file này — đã kiểm tra trực tiếp trong sweep-raw-gasp-wrong.json (1 kết quả khớp tên khi tìm mờ thuộc file Mayami lr真闇追加01 key 1657, không phải file này).
- Lượt soát 2: 15 tổng / 15 tái kiểm chứng / 0 loại bỏ / 0 sửa lại. JSON 15 khóa chuỗi; khối TOML parse OK, 15 khóa, 0 sai lệch. Diff-sanity 15/15 (tương đồng 0,71–0,99; thấp nhất 1101 vì cả dòng chỉ có một tiếng). Quét bổ sung: toàn bộ "tôi"/"em" trong thoại Soutetsu và toàn bộ "Ư phu phu"/"Phu a" (9 chỗ) đã rà lại, không còn sót.
- Phán đoán ghi chú (không tự quyết, chỉ ghi lại): 1008 hoàn thiện câu cụt JP bằng "thì sao?" — giữ nguyên; 1103 ふわわわ giữ "Oa oa oa" (TW 哇哇 đồng ý); 1541 "đáng yêu lắm" hoàn thiện chỗ lửng さぞや — giữ nguyên; 1130 んふー giữ "Ưm phu~!" — không mất âm; 649/1747 "cha nuôi/mẹ nuôi" đúng (TW 養父/養母).
- Chờ thống nhất (không tính sai): không có — không còn dạng cũ nào khác trong file ("Ohito" duy nhất ở 1594 đã sửa thẳng trong audit này theo tiền lệ 08b).

**Tổng cộng sau file này: 67 file / 3.702 dòng sai** (cơ sở 66 file / 3.687 + 15 file này)

- Parent kiểm chứng 20/11 ~06:07: JSON 15 mục dạng chuẩn, khối TOML 15 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 15/15; diff-sanity 15/15 chỉ khác ở chỗ sửa có chủ đích (tỉ lệ 0,71–0,99); 1051 bịa "di sản quý giá" xác nhận (JP không có), 1594 御一夜鉄道→"Ohitoyo" đúng, 977/1097 tiếng cười/yawn đúng quy tắc; lượt soát 2 ghi trong review (15/15, 0 bỏ, 0 sửa). **1312 SỬA LẠI bởi parent: agent cho "Tôi" với Mayami nhưng người nghe là Reina (1318 "僕かられいなにお願いさせてくれ"; Mayami chưa vào cảnh, lần đầu lên tiếng ở 1387) — đúng là "Anh có một việc nhất định phải nhờ chị Mayami."** Bài học: đại từ theo NGƯỜI NGHE, không theo người được nhắc tới.

## 11_Other lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」 — 22/441 (5,0%)

- File: `11_Other/lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml` (441 dòng script; monologue 239, Hiyoko 116, Điện xa Cơ 86). TOML md5 bdb02933933db615a0380eb3839cd6de, không có bản trùng; CSV3 1 bộ 441 dòng, key khớp tuyệt đối.
- Lỗi chính: **chuỗi xoay vòng 10 mắt xích** — VN (và TW) bị đẩy sang key khác theo vòng: 1375→2093→1499→1468 (trùng lặp), 2092→1375, 1782→2092, 1563→1782, 1860→1563, 2332→1860, 1874→2332, 2301→1874; VN đúng của 2301 không có trong file/dự án nên dịch mới ("Yêu đương! Tôi làm được đàng hoàng mà!!").
- Còn lại: sweep っ 6 dòng (1301, 1554, 1591, 1925, 2099 áp nguyên; 2166 needs-file-audit: mất gasp + tự bịa "tốt nhất là"), SFX 5 dòng (1386, 1418, 1774: くちいっ/ぐちゅううっ → "Nhóp nhép"; 2331: ぷあっ "phụt" → "phù ah"; 2426: sweep bỏ sót gasp toàn dòng + "きゅぅ…" viết thành "Cứu…" → "Kyuuuuuuuuuuuuu"), nghĩa 1 dòng (1302: "ゆえ" vì → "vì thế" đảo nhân quả).
- 0 chưa dịch, 0 trùng key, 0 tràn file khác, 0 lỗi đại từ Soutetsu (không xuất hiện), 0 thuật ngữ đã chốt sai. Cột TW lệch thứ tự toàn file — audit theo JP.
- Lượt soát 2: 22 tổng / 22 tái kiểm chứng / 0 loại bỏ / 0 sửa lại.
- Chờ Hieu (không tính sai): Olivy độc thoại "tôi" (12) hay "mình" (18); "phù ah" hay "phà"/"phùa"; 詠字新聞 → "báo Eiji" (4×); SFX dạng động từ trong file.
- Chi tiết đầy đủ: `audit-lr-olivy-hiyoko-REVIEW.md`; danh sách sửa: `audit-lr-olivy-hiyoko-wrong.json` (22 mục, khối TOML 22 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối).

**Tổng cộng sau file này: 68 file / 3.724 dòng sai** (cơ sở 67 file / 3.702 + 22 file này)

- Parent kiểm chứng 20/11 ~06:17: JSON 22 mục dạng chuẩn, khối TOML 22 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 22/22; chuỗi xoay 9/9 mắt kiểm chứng cơ học (fix(B) == VN cũ ở A), 1499 cũ trùng VN đúng ở 1468, 2301 dịch mới không tồn tại ở đâu trong file; 2099 khớp sweep nguyên văn, 2166 needs-file-audit xử lý đúng (bỏ "tốt nhất là" bịa, thêm Ư), 2426 sweep bỏ sót xác nhận (gasp đầu dòng mất + "きゅぅ…" viết sai thành "Cứu…" → "Kyuuuuuuuuuuuuu", đếm âm đúng); 1302 "ゆえ"→"vì" đúng, 1386 "Nhóp nhép" theo quy ước file 1867; lượt soát 2 ghi trong review (22/22, 0 bỏ, 0 sửa). Không sửa nào bị loại hay sửa lại.

## 02_Hibiki 日々姫07_たったひとりの宣戦布告 — 20/400 (5,0%)

- File: `日々姫07_たったひとりの宣戦布告.txt.toml` (route 02_Hibiki, 400 dòng script, 1 bản).
- Kết quả: **20/400 dòng sai (5,0%)** — sweep 4, sfx 8, đại từ 5, nghĩa 3. 0 lệch dòng, 0 chuỗi xoay, 0 tràn file khác, 0 dòng chưa dịch, 0 trùng key.
- Sweep: 4 mục áp nguyên đã kiểm chứng (1949, 2166, 2168, 2169) + 2 gasp sweep bỏ sót (1333, 1728). SFX fa/fu: 1720 (ふぇっ→"Phuê?"), 1727 (ふあっ→"Phù!?"), 1742 (ふえっ→"Phuê!?"), 1759 (ふぁっ→"Phà."), 1785 (thiếu 1 âm a), 2430 (はうぅ→"Hauu!"). Đại từ: 1870 ("chị"→"em" với Kisaki), 1883/1981 ("tớ"→"em"), 1797/1849 (tự sửa 真闇さん→真闇姉 bị viết trùng, sửa theo tiền lệ Paulette file 07). Nghĩa: 2128 (ね？→"Nghe em nói này"), 2596 (số nhiều→số ít), 2718 (にぃに→兄さん: "anh hai——anh trai").
- Lượt soát 2: 20 tổng / 20 tái kiểm chứng / 0 loại bỏ / 0 sửa lại. Khối TOML 20 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối.
- Chờ Hieu: quy tắc chung cho ぴゃ/あわわ; thuật ngữ 評議会 ("buổi bình chọn" hay "Hội đồng bình xét"); gloss 帝鉄 "Đường sắt Hoàng gia" (1629) trong đợt thống nhất.
- Chi tiết đầy đủ: `audit-hibiki07-sensenfukoku-REVIEW.md`; danh sách sửa: `audit-hibiki07-sensenfukoku-wrong.json` (20 mục, khối TOML 20 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối).

**Tổng cộng sau file này: 69 file / 3.744 dòng sai** (cơ sở 68 file / 3,724 + 20 file này)

- Parent kiểm chứng 20/11 ~06:52: JSON 20 mục dạng chuẩn, khối TOML 20 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 20/20; diff-sanity: 5 dòng tỉ lệ thấp đều là SFX 1 âm hoặc câu ngắn (1720/1727/1728/1759 fa/fu theo quy tắc đã chốt, 2128 theo TW); 5 fix đại từ kiểm chứng theo dòng kề: 1870 Kisaki (1869), 1883/1981 Soutetsu (1885/1982), 1797/1849 tự sửa 真闇さん→真闇姉 đúng JP; lượt soát 2 ghi trong review (20/20, 0 bỏ, 0 sửa). Không sửa nào bị loại hay sửa lại.

## 09_Grand グランドリライト11_ナインスターズ！ — 19/603 (3,1%)

- Đọc toàn bộ 603 dòng script đối chiếu JP + TW (CSV3). TOML md5 `235c146a22a4d2b84e7006c9470f5aac`; 1 copy (không có bản sao thứ hai trong `sources/toml2/`).
- **0 lệch hàng, 0 chuỗi xoay vòng, 0 tràn file khác, 0 dòng mồ côi, 0 chưa dịch, 0 trùng key.** 603 key duy nhất; chỉ VN==TW ở 1652 (toàn dấu `「…………」`).
- **Đại từ 8:** Kisaki 5 — Soutetsu "anh"→"tôi" với Kisaki (2347), Soutetsu gọi Kisaki "em"→"cô" (2173), Kisaki gọi Soutetsu "anh Soutetsu"→tên trần/"cậu" (1664, 2459, 2617 đã sửa lại); Soutetsu "anh"→"tôi" với Hachiroku (2574) và khi nói với cả nhóm (2428 みんな, 2104 全員 — tiền lệ Paulette 14:1544). **Parent đã loại 7 fix tự xưng Kisaki "em"→"tôi" (2142, 2508, 2514, 2531, 2599, 2681, 2846) — sai theo tiền lệ đã merge lr_稀咲h1: Kisaki xưng hô theo người nghe ("em" với Soutetsu, "tôi" với Paulette).**
- **Nghĩa 1:** 2619 đảo chiều đồng bộ — JP: KiHa 07 phải liên động theo thao tác của xe đi trước (8620); VN cũ nói ngược lại.
- **Thuật ngữ 3:** 3300 運転体 "thân chính"→"thân vận hành" và 3554 タブレット "thẻ bảng"→"máy tính bảng" (theo quyết định Common 15); 3242 ISC "International Spirits Challenge"→"Competition" (game tự viết ở 真闇01 key 1558).
- **Sweep っ 4:** 2315/2317/2318/2355 gasp toàn dòng → "Ư!"/"Ư!!"/"Ư!!!"/"Ư!!?" (áp nguyên từ sweep, đã kiểm chứng từng dấu).
- **Thêm/bịa 2:** 2462 VN thêm "Ngài Soutetsu. " không có trong JP/TW — bỏ; 2416 VN thêm tag %l quanh 改札鋏 mà JP chỉ có ruby — giữ chữ, bỏ tag.
- **SFX 1:** 3972 （ぽっ！） "Bíp!"→"Bộp!" (TW 啵 = pop, không phải beep).
- Lượt soát 2: agent **26 tổng / 26 tái kiểm chứng / 0 loại bỏ / 0 sửa lại**; parent loại 7 + sửa 1 (2617) → **19 fix**.
- Giữ nguyên (không tính sai): 2477 "Anh có một ý tưởng" (trả lời câu hỏi trực tiếp của Paulette ở 2799, dù nhóm có mặt — không chắc quy tắc nhóm); 2804 "anh" (Soutetsu một mình, addressee mơ hồ); 2767 "bọn anh" (addressee Paulette số ít). Ứng viên đợt thống nhất: Ohimitera 12 dòng, Ohito 1, tuyến Yui 4, Yui tên địa danh 1, Đường sắt Hoàng gia 1, Kobata 1, 九国 "chín tỉnh" vs "chín vùng", 運転体 toàn dự án.
- Chi tiết đầy đủ: `audit-grand11-nine-stars-REVIEW.md`; danh sách sửa: `audit-grand11-nine-stars-wrong.json` (19 mục, khối TOML 19 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 19/19).

**Tổng cộng sau file này: 70 file / 3.763 dòng sai** (cơ sở 69 file / 3,744 + 19 file này)

- Parent kiểm chứng 20/11 ~06:52: JSON 19 mục (sau khi loại 7) dạng chuẩn, khối TOML 19 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 19/19; 2619 đảo chiều đồng bộ xác nhận (JP/TW đồng ý, VN cũ ngược); 2173 xác nhận người nghe là Kisaki (chủ đề lời mời của bạn 仲国 + 2174 người vắng mặt là Hachiroku theo 2194); 2574 xác nhận người nghe Hachiroku (trả lời báo cáo 2155 "楽しかった"); 2347/2104/2428 theo quy tắc "tôi" với Kisaki/nhóm; 1664/2459/2617 tên trần/"cậu" theo JP 双鉄 trần + tiền lệ Common 14. **7 fix LOẠI BỎ: 2142/2508/2514/2531/2599/2681/2846 — agent đổi tự xưng Kisaki "em"→"tôi" theo quy tắc "luôn Tôi" là SAI; tiền lệ đã merge lr_稀咲h1 (review dòng 637) + ROUTE-AUDIT: Kisaki xưng hô THEO NGƯỜI NGHE ("em" với Soutetsu, "tôi" với Paulette), JP đều là ボク. 2617 SỬA LẠI: giữ tên trần "Soutetsu", tự xưng về "em" (người nghe gồm Soutetsu + Paulette).**

## 05_Mayami lr真闇追加03_ブルートレインの夜 — 56/337 (16,6%)

- File: `lr真闇追加03_ブルートレインの夜.txt.toml` — route 05_Mayami, 337 dòng script (monologue 108, hội thoại 229).
- Sai: **56/337 (16,6%)** — pronoun 48 (đối thoại với Mayami 24 + với Reina 1 + độc thoại 23), mistranslation 4, gasp 3, fa/fu 1.
- Không lệch hàng, không chuỗi xoay, 0 orphan / 0 untranslated / 0 duplicate key. Sweep: 2 mục (1120, 1121) đã áp; thêm gasp 905 sweep bỏ sót. Strong candidates 10 → 1 sai (731).
- Second pass: 56/56 đã đọc lại, 0 loại bỏ, 29 sửa lại (khôi phục dấu ngoặc 「 」 bị rơi khi chép fix).
- Chi tiết đầy đủ: `audit-lr-mayami-tsuika03-REVIEW.md`; danh sách sửa: `audit-lr-mayami-tsuika03-wrong.json` (56 mục, khối TOML 56 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 56/56).
- 

**Tổng cộng sau file này: 71 file / 3.819 dòng sai** (cơ sở 70 file / 3.763 + 56 file này)

- Ghi chú cho Hieu: "Ohimitera" còn 3 dòng (1044, 1381, 1768) chờ đợt thống nhất thuật ngữ (1044 còn sai "thành phố" cho 御一夜市); xác nhận người nghe của 3 dòng 1204/1379/1422 (suy luận từ dòng kề, đã ghi lý do trong review); 1283 là fix ngược chiều duy nhất (Soutetsu với Reina → "anh").

- Parent kiểm chứng 20/11 ~07:50: JSON 56 mục dạng chuẩn, khối TOML 56 khóa, 0 sai lệch giá trị (sau khi parent chuẩn hóa mã hóa 48 giá trị fix trong JSON: newline thực → literal \n theo quy ước CSV3/TOML — nội dung fix không đổi; bản JSON gốc lưu ở audit-lr-mayami-tsuika03-wrong.json.orig-2026-11-20); jp/tw/old_vn khớp CSV3 tuyệt đối 56/56; diff-sanity: 0 fix viết lại lớn; đại từ kiểm chứng theo dòng kề: 1283 người nghe Reina → "anh" (đúng, fix ngược chiều duy nhất), 1204 đáp lời mời của Mayami ở 1146 → "tôi", 1379 đáp 1378 của Mayami, Reina ngôi thứ ba → "tôi", 1422 kể với Mayami, Reina ngôi thứ ba → "tôi"; 1288 đảo phủ định xác nhận (JP 塞がんどけば = đừng bịt kín), 689 te-form, 731 bỏ "lòng Reina" bịa, 1893 bỏ "dồn toa" theo quyết định 1027 của Hieu; lượt soát 2 ghi trong review (56/56, 0 bỏ, 0 sửa). Không sửa nào bị loại hay sửa lại.

## 01_Hachiroku ハチロク15a_痛みとの決別 — 78/361 (21,6%)

- File: `01_Hachiroku/ハチロク15a_痛みとの決別.txt.toml` (361 dòng script; monologue 128, Hachiroku 63, Soutetsu 51, Olivy 51, Hiyoko 17, Munakata 13, Paulette 9, Hibiki 7, Kisaki 5, Nagi 4, Mayami 4, Reina 3, Fukami 3, Akai 2, Niiroku 1). TOML md5 ead734bc28455314028f91501e8ba027, không có bản trùng; CSV3 1 bộ 361 dòng, key khớp tuyệt đối.
- Lỗi chính: **chuỗi xoay vòng 55 mắt xích** — VN bị đẩy xuống một dòng theo thứ tự CSV (2775→2660), 54 mắt tìm lại được VN đúng trong file, 1 mắt 2660 dịch mới; thêm mảnh chuỗi 1938 (giữ bản dịch khác của JP 1804) cũng dịch mới. TW khớp đúng thứ tự với JP nên làm nhân chứng thứ hai được.
- Còn lại: đại từ 14 (Soutetsu→Hachiroku "anh"→"tôi" 5, xưng hô nhóm "anh"→"tôi" 4, độc thoại Soutetsu 2510, Paulette→Soutetsu B4 2, Hachiroku↔Olivy 2 — Olivy lớn tuổi hơn Hachiroku, bằng chứng ハチロク06 3455 + ハチロク03 2582 + ハチロク05 2880), sweep っ 6 (3 mục khôi phục lại `\n` từ CSV3 vì bản sweep làm phẳng thành khoảng trắng), thuật ngữ Meriken 1, SFX っっ 1.
- 0 chưa dịch, 0 trùng key, 0 tràn file khác, 0 dòng mồ côi. Lượt soát 2: 78/78/0/0.
- Chờ Hieu (không tính sai): Soutetsu→Olivy "anh" (giữ nguyên); Hachiroku→Hiyoko tự xưng "em" (giữ nguyên); ứng viên thống nhất 9 dòng (Ohito 3, Obata 2, Migita System 1, Thầy cúng 1, Yui 1, Tablet 1).
- Chi tiết đầy đủ: `audit-hachiroku15a-REVIEW.md`; danh sách sửa: `audit-hachiroku15a-wrong.json` (78 mục, khối TOML 78 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 78/78).

**Tổng cộng sau file này: 72 file / 3.897 dòng sai** (cơ sở 71 file / 3.819 + 78 file này)

- Parent kiểm chứng 20/11 ~07:50: JSON 78 mục dạng chuẩn, khối TOML 78 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 78/78; chuỗi xoay 55 mắt kiểm chứng cơ học: 50 mắt fix == VN cũ ở key nguồn, 4 mắt sửa đại từ đồng thời đã kiểm tra từng cặp (1986←2028 "Anh"→"Tôi" ×2, 1766←2746, 2113←2466, 2190←2518 "em"→"chị"), 2660 + 1938 dịch mới đã đối chiếu JP/TW (2660: 想い→"tâm niệm" hợp TW 思念; 1938: 共感→"cộng cảm" đúng quy tắc, giữ tag %l); đại từ kiểm chứng theo dòng kề: 2012/2210/1787/2026 Soutetsu→Hachiroku "tôi", 1782/1831/2011/2212 nhóm → "tôi", 2510 độc thoại "tôi", 2231 Paulette B4, 1947/2560 Hachiroku→Olivy "em" (Olivy lớn tuổi hơn, bằng chứng h06 3455/h03 2582/h05 2880); lượt soát 2 ghi trong review (78/78, 0 bỏ, 0 sửa). Không sửa nào bị loại hay sửa lại.

## 02_Hibiki 日々姫06_みくろ、来訪 — 14/482 (2,9%)

File: `日々姫06_みくろ、来訪.txt.toml` — route 02_Hibiki, 482 dòng script (monologue 153, hội thoại 329).
Sai: **14/482 (2,9%)** — pronoun 6 (1849, 1860, 2013, 2212, 2224, 2471), mistranslation 3 (1973, 2436, 2971), gasp 3 (1986, 2015, 2035), sfx 1 (2062), terminology 1 (2146).
Không lệch hàng, không chuỗi xoay, 0 orphan / 0 untranslated / 0 duplicate key. Sweep: 3 mục (1986, 2015, 2035) đã áp nguyên. Strong candidates 9 → đọc toàn bộ tìm ra 14 sai.
Second pass: 14/14 đã đọc lại, 0 loại bỏ, 0 sửa lại.
Chi tiết đầy đủ: `audit-hibiki06-mikuro-REVIEW.md`; danh sách sửa: `audit-hibiki06-mikuro-wrong.json` (14 mục, khối TOML 14 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 14/14).
**Tổng cộng sau file này: 73 file / 3.911 dòng sai** (cơ sở 72 file / 3.897 + 14 file này)
Ghi chú cho Hieu: thống nhất "Ohimitera" (7 dòng, 9 chỗ dùng) + 帝鉄 (3128) + gloss 扇形機関庫 "hình ngành" (3059); xác nhận người nghe của 1877 ("tìm tôi" hay "tìm anh"); xác nhận giới tính nhân viên 職員Ａ (bản dịch đang dùng "cậu"); quyết có chuẩn hoá 文庫森 (2489) thành Bungo-Mori không.

- Parent kiểm chứng 20/11 ~08:35: JSON 14 mục dạng chuẩn, khối TOML 14 khóa (review + snippet), 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 14/14; diff-sanity: 0 fix viết lại lớn; đại từ kiểm chứng theo dòng kề: 1849/2013 Mikuro → "tôi", 1860 Hibiki → "anh", 2212 Hibiki → "em", 2224 Soutetsu tự đánh giá → "anh" (người nghe Hibiki, cf. 2218/2228/2229), 2471 Mikuro → "cô"; 2146 ナッパ服 → "đồ bảo hộ" theo đa số dự án (4/5 dòng hiện dùng "đồ bảo hộ"; "đồ da nappa" ở Paulette 08 chờ thống nhất); 1877 uncertain giữ nguyên, không tính sai; lượt soát 2 ghi trong review §3 (14/14, 0 bỏ, 0 sửa). Không sửa nào bị loại hay sửa lại. Khối TOML trong snippet đã lược khi gộp (ROUTE-AUDIT.md không chứa khối TOML; khối đầy đủ ở REVIEW.md).

## 07_Nagi_Fukami lr_凪h1_痛いの痛いの飛んでけばい — 22/304 (7,2%)

- "Cơn đau bay đi mất": Nagi luyện kiếm làm gãy kiếm gỗ, mảnh kiếm văng trúng háng Soutetsu; Nagi chữa đau bằng "thổi bay cơn đau" rồi cảnh chuyển sang H; Soutetsu muốn ngực Nagi to lên / ra sữa. Kiểm tra ĐẦY ĐỦ 304 dòng (134 độc thoại, 100 Nagi, 70 Soutetsu).
- Phân loại (22): sweep 19 (gasp っ bị mất), misaligned 1 (1121 lời nói ngọng bị dịch sai), sfx 1 (1170 かっ→"A" mất phụ âm k), pronoun 1 (1567 độc thoại "anh"→"tôi"). Nagi 10, Soutetsu 10, độc thoại 2.
- 0 misaligned-rotation / 0 contamination / 0 orphan / 0 untranslated / 0 duplicate key / 1 uncertain (1366 — lời ngọng không giải mã chắc, giữ nguyên âm, chờ Hieu).
- CSV bộ duy nhất 304 dòng; CSV↔TOML: 144 khớp tuyệt đối + 160 gộp `\n` thành khoảng trắng, 0 khác biệt thực chất; JP comment 304/304 khớp CSV3. TOML md5 3b4b468a7b4e2fc41327c15a75dd230c, BOM + CRLF, [selections] rỗng, không bản sao trùng.
- Sweep: 13 mục — 9 áp nguyên (1178, 1208, 1211, 1212, 1215, 1515, 1209, 1193, 1124); 2 already-rendered (1135, 1155) thực ra vẫn sót っ cuối dòng nên đã sửa; 2 needs-file-audit (1223, 1272) đã xử lý (VN khớp JP, chỉ thiếu っ cuối; 1272 bỏ thêm "đó!" không cơ sở JP). Audit tự tìm thêm 6 gasp sweep bỏ sót: 1126, 1173, 1183, 1210, 1213, 1231. Quy tắc: っ đứng riêng sau ――/～～/… hoặc một mình đầu/cuối dòng = gasp (Ư); っ gắn cuối từ = nhấn mạnh, giữ nguyên (1130, 1131, 1224, 1225, 1161, 1192, 1134, 1280, 1358, 1648).
- Lệch 1121: lời ngọng ひーはんほへーへひほんはら = にーさんの精液飲んだら ("nếu uống tinh dịch của anh hai") — bằng chứng song song key 1237 cùng cảnh giải mã đúng; TW dịch thoáng, JP thắng. VN cũ bịa "ngốc nghếch".
- Lượt soát 2: 22 tổng / 22 tái kiểm chứng / 0 loại bỏ / 0 sửa lại. JSON 22 khóa chuỗi; khối TOML parse OK, 22 khóa, 0 sai lệch giá trị.
- Phán đoán ghi chú: 1237 giải mã ngọng đúng, giữ nguyên (bằng chứng cho 1121); 1337 つっっっ diễn thành "quá", giữ nguyên; 1840 độc thoại "mình" (ngoại lệ nội tâm), giữ nguyên; 1256 抱かれている theo sát JP, giữ nguyên.
- Chờ Hieu (không tính sai): giải mã lời ngọng 1366 (giữ nguyên âm hay theo TW?); thống nhất にーさん "Anh hai" vs "Anh Soutetsu" (7 dòng: 1204, 1206, 1259, 1260, 1263, 1310, 1313); cách diễn つっっっ ở 1337.

**Tổng cộng sau file này: 74 file / 3.933 dòng sai** (cơ sở 73 file / 3.911 + 22 file này)

- Parent kiểm chứng 20/11 ~08:35: JSON 22 mục dạng chuẩn, khối TOML 22 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 22/22; diff-sanity: 0 fix viết lại lớn; 1121 giải mã lời ngọng kiểm chứng qua 1237 (cùng mẫu, VN cũ đã giải đúng "tinh dịch của anh hai"); 1567 độc thoại "anh"→"tôi" (duy nhất trong 134 dòng độc thoại, cf. 1595 "Tôi"); 1170 "A"→"Ka" khôi phục phụ âm k; 19 gasp sweep kiểm chứng từng dấu vs JP; 1366 uncertain giữ nguyên, không tính sai; lượt soát 2 ghi trong review (22/22, 0 bỏ, 0 sửa). Không sửa nào bị loại hay sửa lại. **Totals line đã rebase: snippet gốc ghi cơ sở 72/3.897 → 73/3.919; sau khi gộp Hibiki 06 trước, cơ sở đúng là 73/3.911 → tổng mới 74/3.933.**

## 09_Grand グランドリライト02_ナビ — 2/435 (0,5%)

File: `グランドリライト02_ナビ.txt.toml` — route 09_Grand, 435 dòng script (monologue 200, 双鉄 145, ナビ 44, 路子 21, 日々姫 15, ハチロク 7, 真闇 3).
Sai: **2/435 (0,5%)** — pronoun 2 (1867, 1493).
- 1867 (双鉄→Michiko): "tôi"→"anh" — cảnh mơ với Michiko, mọi câu khác của Soutetsu với Michiko trong cùng cảnh đều dùng "anh" (1729, 1095, 1661, 1651, 1687); quy tắc đã sửa: "anh" với Michiko.
- 1493 (双鉄→nhóm Hachiroku + Hibiki): "anh"→"tôi" (cả 3 chỗ: "anh muốn" + 2× "gia đình anh") — người nghe là cả hai người (VN cũ ghi "hai người"; Hachiroku đáp 1752, Hibiki nói ngay trước 1859); tiền lệ Paulette 14 key 1544 (địa chỉ nhóm → "tôi").
Không lệch hàng, không chuỗi xoay, 0 orphan / 0 untranslated / 0 duplicate key. Sweep: 0 mục cho file này; mọi っ nhấn mạnh cuối từ đều đã diễn (1527, 1553, 1732, 1591, 2617, 2576, 2614, 1782). %l tag sạch, 0 tag thiếu `;`.
CSV bộ duy nhất 435 dòng, 0 key trùng, 0 VN trống; TOML ↔ CSV3 khớp tuyệt đối 435/435 (khóa + VN + JP comment); TOML md5 58d5973b73c2dab6a2ef6bf31feb6b30, BOM + CRLF, [selections] rỗng, không bản sao trùng.
Second pass: 2/2 đã đọc lại, 0 loại bỏ, 0 sửa lại.
Chi tiết đầy đủ: `audit-grand02-navi-REVIEW.md`; danh sách sửa: `audit-grand02-navi-wrong.json` (2 mục, khối TOML 2 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 2/2).
**Tổng cộng sau file này: 75 file / 3.935 dòng sai** (cơ sở 74 file / 3.933 + 2 file này)
Ghi chú cho Hieu: thống nhất "Ohito"→"Ohitoyo" (10 chỗ, 8 key: 1684, 2575, 2213, 2319, 1901, 1017, 2355, 1713); chuẩn hoá tự xưng Hachiroku với Soutetsu ("Tôi" ở 1785/1589 — ngữ cảnh trang trọng わたくし — vs "em" ở 1195).
- Parent kiểm chứng 20/11 ~09:20: JSON 2 mục dạng chuẩn, khối TOML 2 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 2/2; diff-sanity: 0 fix viết lại lớn; đại từ kiểm chứng theo dòng kề: 1867 Soutetsu→Michiko "anh" (cùng cảnh mơ, các dòng kề 1729/1095/1661/1651/1687 đều "anh"), 1493 nhóm Hachiroku+Hibiki "tôi" (VN cũ ghi "hai người"; Michiko nói 1492; 1494 tiếp tục "tôi"; tiền lệ Paulette 14 key 1544); lượt soát 2 ghi trong review §4 (2/2, 0 bỏ, 0 sửa). Không sửa nào bị loại hay sửa lại.

## れいなh4 — れいなh4_ふたりっきりのハロウィン.txt.toml — 59/584 (10,1%)

- H-scene Halloween Soutetsu + Reina (Reina hiểu lầm "とまる" = dừng hoạt động thay vì "泊まる" = nghỉ lại qua đêm; tìm chủ nhân thú bông Cô bé quàng khăn đỏ bị đánh rơi). Lỗi hệ thống duy nhất: tiếng thở fa/fu La-tinh 34 dòng (quy tắc fa/fu đã chốt 19/11) + 3 tiếng cười うふふぅ bị diễn thành tiếng rên.
- Phân loại: sfx 34 (ふあっ→"phù" 17 token/16 dòng, ふぁ→"phà" 4, ふあ không っ→"phùa" 4, ふぇ→"phuê" 4, ふやっ/ふやぁ→"phuya" 3, ふっ→"phù" 5, ふ lẻ cuối dòng→"phù" 2, trong đó 7 token kéo dài — 1894 "phàa", 1983 "Phuyaaaan", 1986 "Phàaan", 2454 "Phùaa", 2456 "Phàa", 2458 "Phùaaaaaa"+"Phùaa"), gasp 6 (5 từ sweep áp nguyên 1963/1990/2022/2972/3095 + 1 sweep bỏ sót 1962), giggle→rên 3 (2099/2104/2111), meaning 8 (1958, 2040, 2263, 2276, 2313, 2545, 3056, 3156), terminology 5 (2118/2350 姉妹機→"máy chị em"; 2535/2797/3118 御一夜→Ohitoyo), pronoun 2 (độc thoại Soutetsu "anh"→"tôi" 3028/3188), minor 1 (2925 "mềm nắn bóp"→"phúng phính"). Thoại 50/396 (12,6%), độc thoại 9/188 (4,8%). Theo nhân vật: れいな 43, 双鉄 7, monologue 9.
- 0 misaligned / 0 rotation / 0 contamination (4 cặp VN trùng trong file đều là JP giống nhau hoặc SFX ngắn hợp lệ: 2506/2296, 2022/1962, 3251/3282, 3254/3268) / 0 orphan / 0 untranslated / 0 duplicate key / 1 uncertain (2288 — chủ ngữ といっていた không xác định được, giữ nguyên chờ Hieu kiểm tra trong game).
- CSV bộ duy nhất 584 dòng; CSV↔TOML: 225 khớp tuyệt đối + 359 gộp \n thành khoảng trắng, 0 khác biệt thực chất; comment # JP: trong [script] 584/584. TOML md5 43ddc25620d65d8d021ab6e6572b5caa, BOM + CRLF, [selections] rỗng, không bản sao trùng. Thẻ %l: JP = VN = 0; ruby [tên,1] 3 dòng (2150/2241/2338) bỏ marker theo lệ toàn dự án.
- Sweep: 5 mục — 5 áp nguyên đã kiểm chứng (1963, 1990, 2022, 2972, 3095); 1 gasp sweep bỏ sót bắt được khi quét bổ sung toàn bộ dòng JP có っ (1962: っ――！ cả dòng). Không còn gasp sót (2901 ためっ! là っ nhấn mạnh, đúng là không thêm Ư).
- Lượt soát 2: 59/59 tái kiểm chứng, 0 bỏ, 0 sửa. JSON 59 khóa chuỗi; khối TOML parse OK, 59 khóa, 0 sai lệch.
- Phán đoán ghi chú: 2241 湯医="Yui" giữ nguyên (quyết định Yui/Yunoi vẫn chờ Hieu) — nhưng JP mang furigana [ゆのい,1], bằng chứng mới cho đề xuất "Yunoi"; 2000 "Fuyu" (ふゆっ) giữ nguyên (quy tắc fa/fu không bao ふゆ); 2015 "Kyufu" giữ nguyên (cả từ SFX, tiền lệ h6); 2408 "Dribble dribble——cut in——shoot!" giữ nguyên (JP katakana tiếng Anh); 3083 "Pyokon"/3269 "choro" giữ nguyên (onomatopoeia ngoài họ fa/fu); 2525/2541 "Cái từ đó" giữ nguyên (chỉ từ xưng hô おまえ) khác 1958 đã sửa "Cái kiểu đó á?"; 2403/2997 VN theo JP, không theo TW (TW tự thêm nội dung); 3012 "nụ cười rạng rỡ" giữ nguyên (động từ "tan chảy thành" đã diễn とろとろ); 2899 giữ nguyên (chủ ngữ kháng nghị không rõ trong JP).

**Tổng cộng sau file này: 76 file / 3.994 dòng sai** (cơ sở 75 file / 3.935 + 59 file này)
- Parent kiểm chứng 20/11 ~09:20: JSON 59 mục dạng chuẩn, khối TOML 59 khóa (nằm trong section [script]), 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 59/59; diff-sanity: chỉ 1 fix viết lại lớn (1890 ふぇっ "E"→"Phuê" theo quy tắc fa/fu đã chốt); đại từ kiểm chứng theo dòng kề: 3028/3188 độc thoại Soutetsu "anh"→"tôi" (monologue, cf. 1494 "Tôi khi còn nhỏ"); meaning kiểm chứng: 3156 đảo nghĩa đã sửa đúng (赤ちゃんというか), 2040 すまん→"xin lỗi", 1958 そんなの→"Cái kiểu đó á?" (TW 哪種？); 2288 uncertain giữ nguyên, không tính sai; lượt soát 2 ghi trong review §5 (59/59, 0 bỏ, 0 sửa). Không sửa nào bị loại hay sửa lại. **Totals line đã rebase: snippet gốc ghi cơ sở 74/3.933 → 75/3.992; sau khi gộp Grand02 trước, cơ sở đúng là 75/3.935 → tổng mới 76/3.994.**


## 日々姫04 — 日々姫04_カフェキッチン.txt.toml — 42/406 (10,3%)

**File:** 日々姫04_カフェキッチン.txt.toml — 406 dòng, **42 dòng sai (10,3%)**.

Nhiễm chéo tư liệu Mikuro/D51: 15 dòng (1720, 1726, 1956, 2011, 2093, 2101, 2191, 2240, 2305, 2603, 2668, 2670, 2746, 2763, 2781). Lệch rời rạc: 9 dòng (1894, 2106, 2303, 2461, 2464, 2469, 2480 — key 2480 đã xác nhận lệch như flag trước đó, 2505, 2665). Bịa thêm câu cụt: 1938. SFX cười thành tiếng rên: 6 dòng (1828, 1831, 1833, 1836, 1837, 2273). Mất tiếng thở っ: 2 dòng (1306, 1909, theo sweep). Đại từ Soutetsu: 2 dòng (1708, 1721). Thuật ngữ カフェ: 5 dòng. Màu 柿色: 2 dòng.

Lượt soát 2: 42/42 tái kiểm chứng, 0 bỏ, 1 sửa (2273 khôi phục câu đầu bị rơi). JSON 42 khóa chuỗi; khối TOML parse OK, 42 khóa, 0 sai lệch. 0 dòng chưa dịch, 0 key trùng, không có rotation chain trong file.

Chờ Hieu: 1938 (TW hoàn thiện câu cụt: tự tay pha trà chanh cho chị hai — có lấy không?) và 柿色 (TW: nâu đỏ — giữ 'vàng cam' hay đổi?).

**Tổng cộng sau file này: 77 file / 4.036 dòng sai** (cơ sở 76 file / 3.994 + 42 file này)
- Parent kiểm chứng 20/11 ~09:55: JSON 42 mục dạng chuẩn, khối TOML 42 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 42/42; diff-sanity: 24 lệch hàng đều là dịch mới từ JP (0 fix viết lại lớn ngoài 24 lệch); nhiễm chéo Mikuro/D51 kiểm chứng: VN cũ 1956 khớp JP 日々姫03 2937 (D51 1031 ở Yu); 2480 xác nhận lệch như flag trước đó; đại từ kiểm chứng theo dòng kề: 1708 Paulette→"anh" (1707 Paulette nói), 1721 Hibiki→"anh" (1720 にぃに); 1938 giữ câu cụt theo JP, chờ Hieu (TW hoàn thiện: tự tay pha trà chanh cho chị hai); 柿色 "vàng cam" chờ Hieu (TW: nâu đỏ); lượt soát 2 ghi trong review §5 (42/42, 0 bỏ, 1 sửa 2273 khôi phục câu đầu). Không sửa nào bị loại hay sửa lại.


## lr真闇追加02_御一夜新婚旅行 — 81/355 (22,8%)

File: `lr真闇追加02_御一夜新婚旅行.txt.toml` — route 05_Mayami, 355 dòng script (真闇 108, monologue 87, 双鉄 79, れいな 61, 日々姫 20).
Sai: **81/355 (22,8%)** — misaligned 24 + untranslated 1 + pronoun 48 + terminology 5 + meaning 2 + gasp 1.
- Chuỗi xoay VN hệ thống: 25 hàng đầu theo thứ tự file của CSV3 (vị trí 0–24) bị lệch VN xuống 1 hàng — VN ở hàng i là bản dịch đúng của JP ở hàng i−1. 1370 (đầu chuỗi) VN trống (TOML giữ câu tiếng Trung); bản dịch đúng của 1346 「うむ」 bị mất hẳn (dịch mới "Ừm"). 24 hàng lệch được sửa bằng cách đưa VN về đúng hàng của nó (chỉ chỉnh thêm: 1120 "em"→"tôi", 1183 "em"→"chị", 1428 "Ohito"→"Ohitoyo", 1503 "thân chính"→"thân bảo trì", 1632 "Hii-chan"→"Hi-chan").
- Đại từ Soutetsu sai hệ thống 48: độc thoại 30 dòng dùng "em" thay "tôi" (chỉ 1888 dùng đúng "tôi"); đối thoại 18 (với Mayami → "tôi" 16, với Reina → "anh" 2: 747, 1545; 1130/1610 "em" ngôi 2 → "chị").
- Thuật ngữ 5: 右田一→"Migitakazu" (1252, 1562, 1829); 一升瓶→"chai rượu Issho" (1749, 1952 → "chai rượu 1,8 lít"); 1829 kèm 和もう "thú vị"→"êm đềm".
- Nghĩa sai 2: 1414 バトンタッチ→"trao cờ" (→"đến lượt em đấy"); 1681 してみたか→"Em muốn đi!!" (→"Thử rồi à!!", bịa — không phải lệch hàng).
- Gasp 1: 1835 (sweep, thiếu Ư → "——Ư!!").
- 1291 義父さん→"bố nuôi" ĐÚNG, giữ nguyên (Soutetsu là con nuôi nhà Migita — 共通10 2573, TW 養父); chỉ sửa đại từ.
Không orphan / 0 untranslated ngoài 1370 / 0 duplicate key / 0 contamination chéo file. %l tag sạch. Mọi っ khác đã diễn đúng. "Yui" (1545) giữ nguyên chờ Hieu; "Bikoku" (1331/1485/1664) giữ nguyên theo furigana (TW: Myanmar — chờ Hieu chốt).
CSV bộ duy nhất 355 dòng, 0 key trùng; TOML ↔ CSV3 khớp tuyệt đối 354/355 (chỉ khác 1370); TOML md5 7ca65c08188951eea0f7655cacce4999, BOM + CRLF, [selections] rỗng, không bản sao trùng.
Second pass: 81/81 tái kiểm chứng, 0 bỏ, 0 sửa. JSON 81 khóa chuỗi; khối TOML parse OK, 81 khóa, 0 sai lệch.
Chi tiết đầy đủ: `audit-lr-mayami-tsuika02-REVIEW.md`; danh sách sửa: `audit-lr-mayami-tsuika02-wrong.json` (81 mục, khối TOML 81 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 81/81).
Ghi chú cho Hieu: thống nhất "Ohito"/"Ohimitera"→"Ohitoyo" (1268, 1350, 1368, 1884 — không tính sai, theo tiền lệ Hibiki 06/Grand02), 宮司→"đền chủ" (1456, 1500 — không tính sai); "Migitakazu" còn 6 hàng ở Grand07_真闇 + 真闇01; phán đoán ít chắc: 1545 "anh" (Reina) vs "tôi" (nhóm), 1612 "Bọn anh" giữ nguyên.
**Tổng cộng sau file này: 78 file / 4.117 dòng sai** (cơ sở 77 file / 4.036 + 81 file này)
- Parent kiểm chứng 20/11 ~09:55: JSON 81 mục dạng chuẩn, khối TOML 81 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 81/81; chuỗi xoay kiểm chứng cơ học: 23/23 fix trả đúng VN lệch (19 khớp tuyệt đối, 4 chỉnh nhỏ 1120/1183/1428/1503/1632), 1346 dịch mới "Ừm" cho JP うむ, chuỗi dừng đúng ở vị trí 24 (1888 khớp JP); 1370 dịch mới từ JP+TW (dòng chưa dịch duy nhất trong file); đại từ kiểm chứng theo dòng kề: 47/48 chỉ đổi đại từ (731 kèm chuẩn hoá ngoặc kép + bỏ "rồi" thừa, hợp JP); 747 Reina→"anh" (746 Reina hỏi trực tiếp), 1545 "anh" theo mạch hỏi–đáp 1542 (flag ít chắc — 1548–1549 nói với nhóm, chờ Hieu kiểm tra trong game), 1130/1610 "em" ngôi 2→"chị" (Mayami); 1291 "bố nuôi" giữ nguyên theo tiền lệ 共通10 2573; 6 hàng dạng cũ KHÔNG tính sai (1268/1350/1368/1884 Ohito, 1456/1500 宮司 — theo tiền lệ Grand02/Hibiki06, fix trong review §6, chờ đợt thống nhất); lượt soát 2 ghi trong review §4 (81/81, 0 bỏ, 0 sửa). Không sửa nào bị loại hay sửa lại. **Totals line đã rebase: snippet gốc ghi cơ sở 76/3.994 → 77/4.075; sau khi gộp Hibiki04 trước, cơ sở đúng là 77/4.036 → tổng mới 78/4.117.**


## 真闇h3_補習授業の廃校舎 — 15/710 (2,1%)

File: `真闇h3_補習授業の廃校舎.txt.toml` — route 05_Mayami, 710 dòng script (monologue 301, 真闇 223, 双鉄 186).
Sai: **15/710 (2,1%)** — raw-tsu 2 + lost-gasp-whole 3 + lost-gasp-trailing 3 + SFX 3 + mistranslation 1 + word-order 1 + nuance 1 + fabrication 1.
- Gasp っ 8 (toàn bộ từ sweep, áp dụng cả 8, 0 loại): 1554, 2694 raw-tsu; 2889, 2890, 2891 cả dòng chỉ là っ; 3114, 3264, 3965 trailing sau ――. 2694 chỉ sửa っ giữa dòng; っ cuối "ぜんぶうっ！" là emphatic, giữ nguyên.
- SFX 3: 2194 + 2665 tiếng cười うふふ bị nhét Ư gasp → "Ufufu" (khớp 2195/2352); 2323 onomatopoeia くに、くに đọc sai thành "cứ, cứ" → "bóp, bóp".
- Nghĩa sai 4: 2444 ぶつける → "va chạm" (→"trút hết"); 2308 đảo thứ tự + mất ひとの (khôi phục trình tự Sou-chan → đàn ông → con người); 2274 いっぱい "đầy" → "sắp đầy" (→"đầy ắp"); 2778 thêm "à." hỏi không có căn cứ.
Không misaligned / rotation / contamination / orphan / untranslated / duplicate-keys. Không lỗi đại từ hệ thống: Soutetsu "tôi" với Mayami xuyên suốt, "em" chỉ khi làm học sinh trong roleplay; 2451 双鉄さん → "anh Soutetsu" là chuyển đổi có chủ ý, giữ nguyên.
CSV bộ duy nhất 710 dòng, 0 key trùng, 0 VN trống; TOML ↔ CSV3 khớp tuyệt đối 710 khóa (428 khác chỉ do TOML-2 làm phẳng `\n` thành khoảng trắng); TOML md5 679f382102d8ec0738d3e2eb97494730, BOM + CRLF, [selections] rỗng, không bản sao trùng; 0 tag %l trong file.
Second pass: 15/15 tái kiểm chứng, 0 bỏ, 0 sửa. JSON 15 khóa chuỗi; khối TOML parse OK, 15 khóa, 0 sai lệch.
Chi tiết đầy đủ: `audit-mayami-h3-REVIEW.md`; danh sách sửa: `audit-mayami-h3-wrong.json` (15 mục, khối TOML 15 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 15/15).
Ghi chú cho Hieu: thống nhất "Ohito"/"Ohimitera"→"Ohitoyo" (1543, 2524, 2608 — không tính sai), 帝大→"Đại học Đế quốc" (3299), 頭取→"Chủ tịch/Tổng giám đốc ngân hàng" (2469 — toàn dự án chưa thống nhất); phán đoán ít chắc: 2328 "quá" cuối (emphatic っ hay "――Ư"), 3967 "（Phập――）" (gasp đầu mất), 2878 thứ tự từ lộn xộn nhưng nghĩa đủ.
**Tổng cộng sau file này: 79 file / 4.132 dòng sai** (cơ sở 78 file / 4.117 + 15 file này)
- Parent kiểm chứng 20/11 ~10:15: JSON 15 mục dạng chuẩn, khối TOML 15 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 15/15; diff-sanity: 0 fix viết lại lớn; SFX kiểm chứng: 2194/2665 うふふ → "Ufufu" (tiếng cười, không gasp), 2323 くに、くに → "bóp, bóp"; 2694 っ giữa dòng → Ư, っ cuối "ぜんぶうっ！" nhấn mạnh giữ nguyên; không lỗi đại từ hệ thống (Soutetsu "tôi" với Mayami); lượt soát 2 ghi trong review §4 (15/15, 0 bỏ, 0 sửa). Không sửa nào bị loại hay sửa lại. Chờ Hieu: 2328 "quá" cuối, 3967 "(Phập――)", thống nhất Ohito (1543/2524/2608), 帝大 (3299), 頭取 (2469).


## ハチロクh9 — ハチロクh9_コノフクハキルコト.txt.toml — 69/613 (11,3%)

- H-scene + thử nghiệm Tàu bia: Soutetsu + Hachiroku, bí mật "コノフクハキルコト" (mặc vào) vs "コノフクハキノコト" (vứt bỏ) do sợi chỉ vụn làm lệch chữ ル→ノ; tìm chủ nhân bộ đồ, thử đồ, và cảnh riêng tư sau giờ làm. Lỗi hệ thống duy nhất: Soutetsu tự xưng "anh" với Hachiroku (28 dòng — quy tắc đã sửa 20/11: "tôi") + gasp っ trần/mất (30 dòng).
- Phân loại: pronoun 28 (Soutetsu "anh"→"tôi" với Hachiroku: 1399, 1413, 1883, 1933, 1940, 1958, 1975, 2074, 2205, 2294, 2306, 2323, 2324, 2325, 2328, 2342, 2345, 2348, 2357, 2389, 2435, 2447, 2467, 2494, 2572, 2574, 2576, 3174), raw-tsu 25 (23 áp nguyên từ sweep + 2 bác fix sweep 2428/2588 — っ nhấn mạnh cuối câu, bỏ っ thay vì thêm Ư), terminology 7 (御一夜→Ohitoyo: 1380/2020/2264/2269/2418/2578; 帝鉄→Teitetsu: 2258), mistranslation 4 (1362/2455 chuỗi 誇る "khen ngợi" không phải "tự hào về"; 1889 câu bỏ lửng bị hoàn thiện ngược; 2927 chủ ngữ — TW xác nhận Hachiroku tự lau), lost-gasp 5 (2625 whole; 2815/3131/3250/3256 trailing). Thoại 63/372 (16,9%), độc thoại 6/241 (2,5%). Theo nhân vật: 双鉄 32, ハチロク 31, monologue 6.
- 0 misaligned / 0 rotation / 0 contamination (chỉ 1 VN trùng JP khác: 「Ưm」 cho cả 「むぅ」 2470 lẫn 「む」 2169 — tiếng ậm ừ ngắn hợp lệ) / 0 orphan / 0 untranslated / 0 duplicate key / 1 uncertain (2053 — lời ngọng らいふき→"dai suki" giữ nguyên dạng La-tinh, chờ Hieu chốt).
- CSV bộ duy nhất 613 dòng; CSV↔TOML: 613 key khớp, 0 khác biệt giá trị; comment # JP: trong [script] 613/613. TOML md5 bcbf02a0308ddac5d5aca3ac1cd717ce, BOM + CRLF, [selections] rỗng, không bản sao trùng. Thẻ %l: JP = VN = 0; ruby [tên,1] 11 dòng bỏ marker theo lệ toàn dự án.
- Sweep: 31 mục — 28 áp nguyên đã kiểm chứng (23 raw-tsu + 1 whole + 4 trailing); 2 bác fix sweep (2428, 2588 — っ nhấn mạnh, tiền lệ mục 1474); 1 already-rendered giữ nguyên (2178). Quét bổ sung toàn bộ dòng JP có っ: không còn gasp sót.
- Lượt soát 2: 69/69 tái kiểm chứng, 0 bỏ, 2 sửa (2927, 3174 — bỏ dấu 「」 thừa trong bản fix nháp). JSON 69 khóa chuỗi; khối TOML parse OK, 69 khóa, 0 sai lệch.
- Phán đoán ghi chú: 2053 giữ nguyên (xem uncertain); 1410 "những năm đầu thời Chính Hòa" giữ nguyên; 1870 "cùng nhau ra nhé" giữ nguyên; 3274 被相続人="người thừa kế hợp pháp" giữ nguyên theo TW.

**Tổng cộng sau file này: 80 file / 4.201 dòng sai** (cơ sở 79 file / 4.132 + 69 file này)
- Parent kiểm chứng 20/11 ~10:15: JSON 69 mục dạng chuẩn, khối TOML 69 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 69/69; diff-sanity: 0 fix viết lại lớn; đại từ kiểm chứng theo dòng kề: 28 fix Soutetsu "anh"→"tôi" với Hachiroku (5 đầu câu "Anh"→"Tôi"; 3174 độc thoại trong cảnh với Hachiroku, đúng quy tắc "tôi"); 2 fix sweep bị bác kiểm chứng: 2428 「ところだっ」 và 2588 「いくぞっ」 là っ nhấn mạnh cuối câu (tiền lệ 1474) — bỏ っ thô, không thêm Ư; 2053 uncertain giữ nguyên, không tính sai; lượt soát 2 ghi trong review §5 (69/69, 0 bỏ, 2 sửa 2927/3174 bỏ 「」 thừa). Không sửa nào bị loại hay sửa lại. **Totals line đã rebase: snippet gốc ghi cơ sở 78/4.117 → 79/4.186; sau khi gộp Mayami-h3 trước, cơ sở đúng là 79/4.132 → tổng mới 80/4.201.**


## 日々姫08 — 日々姫08_とれいん食堂.txt.toml — 20/598 (3,3%)

- Chuyến chạy đầu tiên của tàu nhà hàng: thiết kế của Hibiki, Nagi + Fukami làm đội A ở bếp trên tàu, Saito và Mayami đi với tư cách hành khách, xoay xở lịch trình (trễ 15 phút, chạy bù 5 phút), bán vé, tham quan gara đầu máy hình ngành + bàn quay đầu máy ở Bungomori. Không lỗi hệ thống: lỗi rải rác ở SFX và chi tiết nhỏ.
- Phân loại: lost-gasp 7 (2181 trailing, 2196/2201/2213 whole, 2783 trailing-mid, 2785 trailing — 6 áp nguyên từ sweep + 2152 trailing-mid do audit tự tìm, sweep bỏ sót), SFX-laughter 2 (2142, 2143 — tiếng cười うふふ bị nhét Ư gasp), terminology 3 (2342 帝鉄→"Đường sắt Hoàng gia"; 2585/3038 冥国→"Mỹ"), mistranslation 2 (2545 "đứa bé này"→"hai đứa", TW 她倆; 2718 キュウロク "gara đầu máy"→"đầu máy", TW 機車), pronoun 2 (2128 Soutetsu gọi Fukami "cậu"→"em", nối tiếp 2126; 3567 "anh Tochigi/Kimoto"→"bác", khớp 1525/3604), added-tag 4 (2117 転車台, 2458 艤装, 3113 杜氏, 3211 指差し確認 — gỡ thẻ %l VN tự thêm, giữ gloss làm chữ thường; tiền lệ ムナカタ来訪 gỡ 31 thẻ). Đối thoại 16/348 (4,6%), độc thoại 4/250 (1,6%). Theo nhân vật: 日々姫 9, monologue 4, 双鉄 3, 真闇 2, 木本 1, 斎藤 1.
- 0 misaligned / 0 rotation / 0 contamination / 0 orphan / 0 untranslated / 0 duplicate key / 0 uncertain. Trùng VN 4 nhóm đều là cảm thán ngắn hợp lệ (Hửm?/Oa!/A——/Nếu vậy thì――); 1576 「…………」 giống hệt JP/TW/VN.
- CSV bộ duy nhất 598 dòng, 0 key trùng, 0 VN trống; CSV↔TOML: 598 key khớp, 0 khác biệt giá trị thực (376 khác chỉ do TOML-2 làm phẳng literal `\n` thành khoảng trắng); comment # JP trong [script] 598/598 khớp CSV3. TOML md5 8a6fb6d483dd862dd0d22df29ccd99d2, BOM + CRLF, [selections] rỗng, không bản sao trùng. Thẻ %l: JP = VN ở mọi dòng trừ 4 dòng gỡ thẻ; 0 marker ruby còn trong VN.
- Sweep: 6 mục — áp nguyên cả 6 đã kiểm chứng (3 whole + 2 trailing + 1 trailing-mid); 0 mục bị bác. Quét bổ sung toàn bộ dòng JP có っ: tìm thêm 1 gasp sót (2152 はぁ～っ―― → "Hà~Ư——"); các っ còn lại đều là っ trong từ/phương ngữ, cảm thán ngắt đã diễn (あっ→"A——", うんっ→"Vâng"), っ nhấn mạnh cuối từ (てっ 2193) hoặc SFX đã diễn (2195 "A á!!", 3706/3707).
- Lượt soát 2: 20/20 tái kiểm chứng, 0 bỏ, 0 sửa. JSON 20 khóa chuỗi; khối TOML parse OK, 20 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 20/20.
- Phán đoán ghi chú: 2214 "Nagi đại nhân" thêm vào giữ nguyên (lối nói quen thuộc của Nagi trong file, 2739/2741); 2193 "ăn cẩu lương" và 2629 "Cứu anh một bàn thua trông thấy" là cách diễn sáng tạo, giữ nguyên; 2515 bỏ tên gọi 登呂流湯さん đầu câu giữ nguyên ("bà ấy" vẫn rõ); 2585 日ノ本 giữ "Hinamoto" (chưa có thuật ngữ chốt).

**Tổng cộng sau file này: 81 file / 4.221 dòng sai** (cơ sở 80 file / 4.201 + 20 file này — cơ sở đã kiểm chứng lại với ROUTE-AUDIT.md trước khi viết, khớp với số parent giao).
- Parent kiểm chứng 20/11 ~10:45: JSON 20 mục dạng chuẩn, khối TOML 20 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 20/20; diff-sanity: 0 fix viết lại lớn; đại từ kiểm chứng theo dòng kề: 2128 Soutetsu gọi Fukami "cậu"→"em" (2126 đã dùng "em" với Fukami, đúng quy tắc "anh"); 3567 "anh Tochigi/Kimoto"→"bác" (khớp quy ước file 1525/3604); gasp 2152 do audit tự tìm: JP 「すう～――はぁ～っ――」 có っ ở nhịp thở ra, TW 呼——, thêm "Ư" đúng (sweep bỏ sót, không phải emphatic); lượt soát 2 ghi trong review (20/20, 0 bỏ, 0 sửa). Không sửa nào bị loại hay sửa lại. Chờ Hieu: thống nhất "Toa ăn Train" (8 dòng) vs "Tàu nhà hàng" (13 dòng) + 16 dòng "Ohimitera"/"Ohito"→"Ohitoyo" (không tính sai).


## lr_ふかみh2 — lr_ふかみh2_セックスの意味.txt.toml — 52/291 (17,9%)

- H-scene Soutetsu + Fukami (nếm rượu amazake rồi làm tình để tạo em bé; "ý nghĩa thực sự của sex" — file kết route Nagi/Fukami). Ba lỗi hệ thống: (1) Soutetsu tự xưng "tôi" trong toàn bộ thoại đầu file với Fukami 13 dòng; (2) tiếng thở ふぁ/ふあ của Fukami đều thành "Ha"/"Ah" mất âm f 24 dòng (quy tắc fa/fu đã chốt 19/11); (3) gasp っ trần/cuối dòng rên bị mất 15 dòng chạm gasp, sweep bỏ sót 9. Không có lỗi nghĩa hay thuật ngữ nào (1 dòng "Migita System" 1406 chờ đợt thống nhất, không tính sai).
- Phân loại: pronoun 13 (Soutetsu "tôi"→"anh" với Fukami: 989, 990, 1147, 1168, 1175, 1205, 1207, 1214, 1215, 1241, 1243, 1250, 1290), sfx 24 (ふぁ→"phà" 8, ふあっ→"phù" 11, ふあ không っ→"phùa" 0, ふぇ→"phuê" 0, ふやっ→"phuya" 1, ふっ→"phù" 3 — 1063 mang cả 3, 1030 mang 2, 1275 mang 2; 1016 mang cả fa/fu), gasp 14 tính riêng (1063 mang cả gasp + fa/fu, tính vào sfx; tổng 15 dòng chạm gasp), sfx-count 1 (1124 thừa 3 âm o). Thoại 49/162 (30,2%), độc thoại 3/129 (2,3%). Theo nhân vật: ふかみ 31, 双鉄 18, monologue 3.
- 0 misaligned / 0 rotation / 0 contamination (đối chiếu VN file qua chỉ mục VN toàn dự án: 0 lần trùng VN trong file với JP khác nhau; 1 cặp VN trùng 1068/1105 đều là JP giống hệt 「っ！！」 — lặp hợp lệ) / 0 orphan / 0 untranslated / 0 duplicate key / 0 uncertain.
- CSV dual-set (BẪY): CSV3 có 2 bộ hàng cho file này (mỗi bộ 291 hàng, key 757–1775). Bộ `07_Nagi_Fukami` STALE (khớp phẳng TOML 5/291); bộ `11_Other` là bộ tốt (khớp phẳng 291/291) — chỉ audit bộ tốt. CSV↔TOML: 128 khớp tuyệt đối + 163 gộp \n thành khoảng trắng, 0 khác biệt thực chất; JP comment 291/291 khớp CSV3. TOML md5 896562ad2c4430d5219eef5d177b99c5, BOM + CRLF, [selections] rỗng, không bản sao trùng. Thẻ %l: JP = VN = 0.
- Sweep: 21 mục — 3 áp nguyên đã kiểm chứng (1105, 1558; 1063 phần gasp áp nguyên, token ふっ sửa thêm "fu"→"phù" theo fa/fu); needs-file-audit 12 đã giải quyết hết (sửa 5: 1099, 1107, 1179, 1260, 1241; giữ 7: 1027, 1120, 1423, 1479, 1717, 1733, 1760); uncertain 2 (1078 giữ, 1588 sửa); already-rendered 4 đã kiểm chứng (1029, 1035, 1070, 1763); 9 gasp sweep bỏ sót bắt được khi quét bổ sung toàn bộ dòng JP có っ (1068, 1069, 1072, 1085, 1086, 1125, 1126, 1127, 1598). Không còn gasp sót. っ nhấn mạnh cuối câu trong thoại giữ nguyên (tiền lệ 1474, 2428, 2588).
- Lượt soát 2: 52/52 tái kiểm chứng, 0 bỏ, 3 sửa (1269, 1270, 1273 — "Phà" → "Phù" cho token ふあっ; phân biệt ふぁ (ぁ nhỏ) → "phà" / ふあ (あ đầy) + っ → "phù"). JSON 52 khóa chuỗi; khối TOML parse OK, 52 khóa, 0 sai lệch.
- Phán đoán ghi chú: 1406 "Migita System" chờ đợt thống nhất (không tính sai); 987 "Khôn đao" giữ (ngọng "không đau", TW đồng thuận); âm ひゃ đầu tiếng rên giữ "Ah"/"Á" (1018, 1019, 1094, 1101 dòng 2 — không có quy tắc đã chốt về ひゃ); はぁっ → "Ha" giữ (tiền lệ lr_凪h2); っ nhấn mạnh trong thoại giữ (xem §4 review); đếm âm giữ nguyên ở 1085/1125 (lệch 1 / tách âm tiết không rõ) và dấu ~ ở 1099/1127 (không có quy tắc đếm ~); 1463 "Tôi muốn Fukami" giữ (khớp TW); 1295 "blowjob" giữ (loanword); 1014/1207/1568 giữ (vụng về nhưng đúng nghĩa / khớp JP).

**Tổng cộng sau file này: 82 file / 4.273 dòng sai** (cơ sở 81 file / 4.221 + 52 file này)
- Parent kiểm chứng 20/11 ~10:55: JSON 52 mục dạng chuẩn, khối TOML [script] 52 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 52/52 với bộ TỐT 11_Other (bộ STALE 07_Nagi_Fukami lệch 97 điểm — agent dùng đúng bộ, bẫy dual-set đã tránh); diff-sanity: 5 fix viết lại lớn đều là dòng SFX ngắn, đã kiểm từng dòng (1039 ふあっ→"Phù", 1072 っ cả dòng→"Ư――", 1086 rên dài + っ cuối→Ư, 1087 ふやんっ→"Phuyan", 1277 ふあっ→"Phù"); đại từ kiểm chứng theo dòng kề: 13 fix Soutetsu "tôi"→"anh" với Fukami (989/1147/1290 — cảnh thân mật, Fukami gọi "o-nii"; từ key 1224 đã dùng đúng "anh"); lượt soát 2 ghi trong review (52/52, 0 bỏ, 3 sửa 1269/1270/1273 "Phà"→"Phù"). Không sửa nào bị loại hay sửa lại. **Totals line đã rebase: snippet gốc ghi cơ sở 80/4.201 → 81/4.253; sau khi gộp Hibiki08 trước, cơ sở đúng là 81/4.221 → tổng mới 82/4.273.** Chờ Hieu: 1406 "Migita System" (đợt thống nhất, không tính sai); ひゃ đầu tiếng rên giữ "Ah"/"Á" (1018/1019/1094/1101 — chưa có quy tắc chốt).


## ハチロク08 — ハチロク08_教導.txt.toml — 20/562 (3,6%)

- Lớp học bảo trì đường ray của Olivy: đố vui về cầu, tà vẹt, phụt bùn, nước ngầm; ba trưởng lão Seki/Nagare/Osamu, Nagi, Fukami, Niiroku, Akai tham dự.
- Phân loại: terminology 8 (帝鉄 5, 可変パッド 1, Railord 2), name 5 (流→"Ryu" 5 — file duy nhất trong dự án gọi sai, toàn dự án đều "Nagare"), pronoun 3 (1898 Hachiroku "em"→"tôi"; 2187 Fukami "em"→"mình" với Nagi; 3256 "anh Osamu"→"ông Osamu"), mistranslation 2 (1351 一番→"thứ nhất"; 1385 必要。ない dịch ngược nghĩa), sfx 1 (2855 くすっ→"(Phụt)"), gasp 1 (3202, áp nguyên sweep). Đối thoại 14/410, độc thoại 6/152. Theo nhân vật: オリヴィ 6, monologue 6, ニイロク 2, ハチロク 2, ふかみ 2, 凪 1, 赤井 1.
- 0 misaligned / 0 rotation / 0 contamination / 0 orphan / 0 untranslated / 0 duplicate key / 0 uncertain.
- CSV bộ duy nhất 562 dòng, 0 key trùng, 0 VN trống; CSV↔TOML: 562 key khớp, 0 khác biệt giá trị thực (223 khớp tuyệt đối + 339 gộp \n thành khoảng trắng); comment # JP 562/562 khớp CSV3. TOML md5 98b197a95b59203975febf766cc038a8, BOM + CRLF, [selections] rỗng, không bản sao trùng. Thẻ %l: JP = VN mọi dòng; 0 marker ruby còn trong VN.
- Sweep: 2 mục — 3202 áp nguyên đã kiểm chứng; 2085 already-rendered giữ nguyên. Quét bổ sung toàn bộ 251 dòng JP có っ: không gasp nào sót; っ cuối tiếng reo và っ nhấn mạnh cuối câu giữ nguyên (tiền lệ 1474/2428/2588).
- Lượt soát 2: 20/20 tái kiểm chứng, 0 bỏ, 1 sửa (1385 dấu kết câu "." gõ nhầm thành "。" trong bản nháp, đã sửa).
- Phán đoán ghi chú: 1992 Soutetsu "tôi" giữ (phía cúi đầu là các trưởng lão, dòng kề TOML 1988/1993); 2625 "em" = Olivy giữ; Fukami/Olivy/Hachiroku tự xưng em/tớ/cháu lẫn lộn giữ nguyên trừ 2187/1898; 日ノ本 "Hinomoto" giữ.
- Chờ Hieu (đợt thống nhất, không tính sai): "Yui"→"Yunoi" 12 dòng (1351, 1379, 1966, 2302, 2382, 2635, 2794, 2828, 2840, 2850, 2868, 3335); "Ohito"→"Ohitoyo" 10 dòng (1384, 2031, 2091, 2327, 2328, 2651, 2826, 2828, 2868, 3358); 日ノ本 "Hinomoto" (file này) vs "Hinamoto" (Hibiki08 đã giữ) — cần chốt một cách viết chung.
- JSON 20 khóa chuỗi; khối TOML parse OK, 20 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 20/20.

**Tổng cộng sau file này: 83 file / 4.293 dòng sai** (cơ sở 82 file / 4.273 + 20 file này)
- Parent kiểm chứng 20/11 ~11:15: JSON 20 mục dạng chuẩn, khối TOML 20 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 20/20; diff-sanity: 1 dòng SFX ngắn viết lại toàn bộ (2855 くすっ→"Hì hì", đúng JP/TW); đại từ kiểm chứng theo dòng kề: 1898 Hachiroku "em"→"tôi" (tự mâu thuẫn "em… bà lão", nói với Soutetsu 1900; "em" với Soutetsu ở 2487/2844/2847 giữ nguyên), 2187 Fukami "mình" với Nagi (đúng quy tắc đã sửa), 3256 "ông Osamu" (khớp 3168/3171 trong file); tên 流→"Nagare" kiểm chứng độc lập: 共通12 2135 tự giới thiệu "ta là Nagare", "ông Ryu" chỉ xuất hiện trong file này (5 dòng), "Nagare" có ở 4 file khác; lượt soát 2 ghi trong review (20/20, 0 bỏ, 1 sửa 1385). Không sửa nào bị loại hay sửa lại. **Totals line không cần rebase: snippet ghi cơ sở 82/4.273, khớp ROUTE-AUDIT.md hiện tại.** Chờ Hieu: 12 dòng "Yui"→"Yunoi", 10 dòng "Ohito"→"Ohitoyo" (đợt thống nhất, không tính sai); 日ノ本 "Hinomoto" (file này) vs "Hinamoto" (Hibiki08 đã giữ) — cần chốt một cách viết chung.


## lr_ふかみh1 — lr_ふかみh1_ふかみうさぎのたまご.txt.toml — 76/289 (26,3%)

- H-scene Soutetsu + Fukami (Fukami làm thỏ Phục Sinh tặng Soutetsu "trứng âm đạo" của mình; hai người tranh nhau chọn bắn trong hay bắn ngoài để ngửi mùi tinh dịch). Ba lỗi hệ thống: (1) Soutetsu tự xưng "tôi" trong TOÀN BỘ thoại với Fukami — 30 dòng, 39 lần, 0 dòng đã đúng (khác ふかみh2 chỉ sai 13 dòng đầu file); (2) tiếng thở ふぁ/ふあ/ふぇ của Fukami thành "Ha"/"Hả"/"fu" mất âm f 21 dòng (quy tắc fa/fu đã chốt 19/11); (3) gasp っ bị mất 17 dòng, sweep chỉ bắt được 5, 12 do quét toàn bộ JP mà ra — đáng chú ý sweep ghi nhầm JP của 1681 vào mục 1613, khiến 1681 không có mục sweep nào. Không có lỗi nghĩa hay thuật ngữ nào ngoài 2 dòng "lồn" lẻ loi (1669, 1731).
- Phân loại: pronoun 30 (Soutetsu "tôi"→"anh" với Fukami — toàn bộ 30 dòng thoại có đại từ), gasp 17 (1257, 1259, 1260, 1261, 1262, 1268, 1288, 1339, 1374, 1435, 1438, 1613, 1651, 1681, 1682, 1780, 1835 — 1257/1374 mang cả pronoun, 1268 mang cả fa/fu), sfx 30 (fa/fu 21: ふぁ→"phà" 8, ふあっ→"phù" 6, ふぇ→"phuê" 2, ふ、あ→"phù, a" 3, ふぁぅ→"phàu" 1, ふああっ→"Phùaa" 1; đếm nguyên âm 8: 1224 thiếu 7 âm a, 1279 thiếu 5 âm u, 1310 thiếu 2 âm u, 1920 thiếu 8 âm u, 1949 thiếu 1 âm u, 1966 thiếu 4 âm u, 1967 thiếu 1 âm u, 1968 thừa 1 âm u; mất tiếng thở はっ 1: 1196), terminology 2 (1669, 1731 "lồn"→"âm đạo"). Thoại 双鉄 39/66 (59,1%), thoại ふかみ 24/93 (25,8%), độc thoại 13/130 (10,0%). Theo nhân vật: 双鉄 39, ふかみ 24, monologue 13.
- 0 misaligned / 0 rotation / 0 contamination / 0 orphan / 0 untranslated / 0 duplicate key / 0 uncertain. VN == TW chỉ 961 「……」 (dấu câu).
- CSV dual-set (BẪY): CSV3 có 2 bộ hàng cho file này (mỗi bộ 289 hàng, key 961–1973). Bộ `07_Nagi_Fukami` STALE (khớp tuyệt đối TOML 3/289); bộ `11_Other` là bộ tốt (119 khớp tuyệt đối + 169 chỉ khác `\n` bị TOML làm phẳng + 1 khác là 1466 TOML nuốt `\n` đầu dòng = khớp nội dung 289/289) — chỉ audit bộ tốt. JP bộ tốt khớp comment `# JP:` trong TOML 289/289; JP hai bộ khác nhau 242 key, TW hai bộ giống hệt. TOML md5 978b35d98d620183d1a58aa3aaa8eda0, BOM + CRLF, [selections] rỗng, không bản sao trùng. Thẻ %l: JP = VN = 0.
- Sweep: 13 mục — 5 áp nguyên đã kiểm chứng (1288, 1613, 1651, 1780, 1835); already-rendered 3 đã kiểm chứng (1287, 1304, 1400); needs-file-audit 5 đã giải quyết hết (giữ 3: 1384, 1629, 1817; sửa 2: 1445 đại từ, 1967 đếm âm); 12 gasp sweep bỏ sót bắt được khi quét bổ sung toàn bộ dòng JP có っ (1257, 1259, 1260, 1261, 1262, 1268, 1339, 1374, 1435, 1438, 1681, 1682). Không còn gasp sót. Lưu ý: cột JP của sweep ở mục 1613 bị sai (ghi JP của 1681) — fix vẫn đúng vì old_vn/fix khớp VN của 1613, đã kiểm chứng lại với JP bộ TỐT.
- Lượt soát 2: 76/76 tái kiểm chứng, 0 bỏ, 0 sửa. JSON 76 khóa chuỗi; khối TOML parse OK, 76 khóa, 0 sai lệch.
- Phán đoán ghi chú: độc thoại Soutetsu "tôi" giữ (quy tắc chung); 1651 "mình đang ngủ gật" giữ (ngoại lệ độc thoại tự vấn); tên kéo dài "Fu——ka…… mi." (1430/1432) giữ; ひゃ đầu tiếng rên giữ "Hyau" (1285, 1294); kết thúc んっ → "n" giữ (1277, 1286, 1967); あっ/うあっ → "A"/"Ua" giữ; はうっ → "Hau", はぁっ → "Ha" giữ; っ nhấn mạnh dính từ giữ; 1285 んううっ → "ưm" giữ (quy ước file); SFX ướt dài giữ phong cách lặp từ/lặp phụ âm, không sửa theo công thức đếm âm (1919, 1939, 1940, 1941, 1948, 1954, 1965 — tiền lệ tiếng còi 00common15/grand11); 1782 "Cô bé nhỏ nhắn" cho おまんこ giữ (uyển ngữ); 1417/1425/1441 giữ (lệch sắc thái nhẹ / đảo trật tự / せいり = sắp xếp). Không có câu hỏi mới nào cần Hieu quyết.

**Tổng cộng sau file này: 84 file / 4.369 dòng sai** (cơ sở 83 file / 4.293 + 76 file này)
- Parent kiểm chứng 20/11 ~11:20: JSON 76 mục dạng chuẩn, khối TOML 76 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 76/76 với bộ TỐT 11_Other (bộ STALE 07_Nagi_Fukami lệch 75/76 — agent dùng đúng bộ, bẫy dual-set đã tránh; khớp phẳng bộ tốt 288/289, dòng lệch duy nhất 1466 TOML nuốt \n đầu dòng); diff-sanity: 0 fix viết lại lớn; đại từ kiểm chứng theo dòng kề trên 3 mẫu (972/1377/1486 — toàn file chỉ có Soutetsu↔Fukami, 66 thoại 双鉄 + 93 thoại ふかみ + 130 độc thoại, đúng quy tắc "anh" với Fukami); lỗi sweep xác nhận độc lập: mục 1613 ghi JP của 1681 (TW/old_vn vẫn đúng của 1613), mục 1681 của sweep thuộc file khác — fix 1613 vẫn đúng vì đã kiểm với JP bộ tốt; lượt soát 2 ghi trong review (76/76, 0 bỏ, 0 sửa). Không sửa nào bị loại hay sửa lại. **Totals line không cần rebase: snippet ghi cơ sở 83/4.293, khớp ROUTE-AUDIT.md hiện tại (agent đã tự rebase sau khi ハチロク08 gộp song song).** Không có câu hỏi mới nào cần Hieu quyết từ file này.


## 日々姫03 — 日々姫03_客車手配.txt.toml — 41/504 (8,1%)

- Tìm mua toa hành khách cho 8620: trái phiếu đường sắt thời Teitetsu, Đường sắt Suntai nhượng toa cải tạo, vận chuyển từ Shizuoka về Ohitoyo; xen kẽ cảnh pha trà sadou/doesu. Lỗi hệ thống: thuật ngữ tên cũ chưa theo quy tắc đã chốt (Ohitoyo/Teitetsu/Suntai/Yunoi).
- Xoay vòng 3 dòng 2447/3220/3662 (đã kiểm chứng toàn dự án: mỗi VN đang nằm sai key, dời nguyên văn về đúng key; không dòng nào cần dịch mới, không còn dòng mồ côi).
- Phân loại: terminology 27 (Ohitoyo 14 dòng/16 lần, Teitetsu 5, Suntai 6 dòng/7 lần, Yunoi 2, 機関士 3), pronoun 5 (2384, 2458, 2482, 2637 — Paulette→Soutetsu "anh" theo khóa B4; 2675 parent-added Paulette "Chị"→"Em" với Soutetsu), rotation 3 (2447, 3220, 3662), gasp 3 (2322, 2427, 2894 — áp nguyên sweep), mistranslation 2 (2487 輸送→"vận chuyển"; 2543 bịa câu hỏi "em hiểu chưa?"), sfx 1 (2389 ふぁぁ→"Phàaa"). Thoại 32/273, độc thoại 9/231. Theo nhân vật: ポーレット 11, monologue 9, 双鉄 7, 日々姫 5, ハチロク 5, れいな 2, ふかみ 1, 凪 1.
- 3 misaligned (vòng xoay 2447/3220/3662 — xem §1 review) / 0 rotation khác / 0 contamination (cặp VN trùng duy nhất 2417/2438 cùng JP 「ああ」) / 0 orphan / 0 untranslated / 0 duplicate key / 2 uncertain (2530, 2603 — Soutetsu "tôi" đáp người gọi ngoài cảnh, chưa xác định được người nghe).
- CSV bộ duy nhất 504 dòng, 0 key trùng, 0 VN trống; CSV↔TOML: 176 khớp tuyệt đối + 325 gộp \n thành khoảng trắng + 3 dòng làm phẳng \n đầu dòng, 0 khác biệt thực chất; comment # JP 504/504 khớp CSV3. TOML md5 a066fd1ca4854418d892c78d87384a78, BOM + CRLF, [selections] rỗng, không bản sao trùng. Thẻ %l: JP = VN mọi dòng trừ 3 dòng chuyển ruby JP thành thẻ %l (2354, 2679, 2828 — chữ hiển thị đúng, không tính sai); 0 marker ruby còn trong VN.
- Sweep: 4 mục — 3 áp nguyên đã kiểm chứng (2322, 2427, 2894); already-rendered 1 giữ nguyên (2328). Quét bổ sung toàn bộ 192 dòng JP có っ: không gasp nào sót; các っ còn lại là nhấn mạnh/phương ngữ/đã diễn.
- Lượt soát 2: 40/40 tái kiểm chứng, 0 bỏ, 1 sửa (2543 thiếu dấu 「」 trong bản nháp, đã sửa). Parent kiểm chứng 20/11 ~11:50: 1 fix sửa lại (2482 "của chị"→"của em"), 1 fix thêm (2675). JSON 41 khóa chuỗi; khối TOML parse OK, 41 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 41/41.
- Phán đoán ghi chú: 2530/2603 giữ (không xác định được người nghe); 2249 駿川 giữ "Surukawa" (JP thắng TW); 2834 乗員 "phi hành đoàn" giữ (quy ước dự án); 3764 義兄 "anh trai nuôi" giữ (TW 義兄, tiền lệ file 14); độc thoại nội tâm Soutetsu "mình" giữ; Paulette "mình" 2266/2608/2873 giữ.
- Chờ Hieu (không tính sai): "ông nội" 2368/2607 (câu hỏi ông nội vs ông ngoại toàn dự án); 日ノ本 "Hinomoto" 2561 vs "Hinamoto" (Hibiki08) — cần chốt một cách viết; Paulette "mình" vs "em" có thống nhất không; xác nhận người nghe ở 2530/2603.

**Tổng cộng sau file này: 85 file / 4.410 dòng sai** (cơ sở 84 file / 4.369 + 41 file này — parent thêm 2675, sửa 2482; cơ sở đã kiểm chứng lại với ROUTE-AUDIT.md, khớp).
- Parent kiểm chứng 20/11 ~11:50: JSON 41 mục dạng chuẩn (40 của agent + 2675 parent thêm, tiền lệ file 09 key 2719); khối TOML 41 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 41/41; vòng xoay 2447/3220/3662 kiểm chứng độc lập với JP (mỗi fix khớp đúng JP của key đích, chu trình khép kín); đại từ kiểm chứng theo dòng kề: 2384/2637 Paulette→Soutetsu 'anh' (khóa B4), 2458 'anh' qua điện thoại (cùng cuộc gọi 2455 đã dùng 'anh', người gọi là Paulette), 2482 người nghe Soutetsu đã xác nhận (đáp 'うん' 2479; Hibiki 2484/2486 đáp Soutetsu '兄さん') — parent sửa thêm 'của chị'→'của em' để câu nhất quán, 2675 parent thêm cùng lỗi (Paulette đáp câu hỏi Soutetsu 2671→2673→2675); sweep 3 áp nguyên + 1 already-rendered giữ; lượt soát 2 ghi trong review (40/40, 0 bỏ, 1 sửa 2543) + parent sửa 2482/thêm 2675. **Totals line: 85/4.410 (cơ sở 84/4.369 khớp ROUTE-AUDIT.md).** Chờ Hieu: 'ông nội' 2368/2607; 日ノ本 'Hinomoto' vs 'Hinamoto'; Paulette 'mình' vs 'em' (2266/2608/2873); người nghe 2530/2603.


## 日々姫07 — 日々姫07_姉の想い。妹の想い.txt.toml — 15/430 (3,5%)

- File: `日々姫07_姉の想い。妹の想い.txt.toml` — route 02_Hibiki, 430 dòng script. Nội dung: Hibiki trình bày thiết kế bếp + thực đơn toa ăn; Mayami từ chối lên tàu; Soutetsu dỗ dành Hibiki; cả hai đến Bungomori gặp Kimoto, nghe về đầu máy 29611, nảy ra ý "toa ăn đưa đồ tươi vào" → tên mới 『とれいん食堂』.
- Lệch vị trí 0, chưa dịch 0, cụt câu 0, không chắc chắn 2 (2632 — chủ ngữ độc thoại "Tôi đã thảo luận với cô Yamazaki..." bỏ lửng, Soutetsu hay Hibiki; 1941 — Paulette "Em cũng tán thành", người nghe chưa rõ: Hibiki → "chị", Kisaki → "tôi", Soutetsu → "em").
- Phân loại (15): lost-gasp 6 (1832, 1833, 1834, 1850, 1900 — 5 mục sweep, áp nguyên đã kiểm chứng; 1431 — sweep bỏ sót, audit tự tìm: JP 3 âm っ, VN cũ chỉ 2 Ư); thuật ngữ 1 (1366: 帝鉄 "Đường sắt Hoàng gia" → "Teitetsu cũ", tiền lệ 日々姫08 2342); xưng hô 2 (1859: Fukami tự xưng "chị" → "em" (người nghe Soutetsu/Hibiki — parent sửa: agent ghi nhầm "mình" với Nagi, dẫn chứng 2111 sai; tiền lệ ふかみh2 "em" với Soutetsu + 1831/1841 "em" với Hibiki trong file); 1721: Paulette tự xưng "em" → "chị" với Hibiki (parent: bỏ dẫn chứng sai "đáp ngay 1874", xem review §2.3); sai nghĩa 2 (2900: 運び込む "đưa vào thực tế" → "vận chuyển nó vào"; 2982: 高菜めし "cơm trộn mù tạt" → "cơm trộn cải mù tạt muối", TW 大芥飯糰); lỗi nhỏ 3 (1798, 2169: dấu "Ạ" đứng riêng câu, Fukami — tiền lệ file 08 1934; 2992: còi báo trưa U×18 → U×8, khớp JP ウ×8 + ー×3); tag 1 (1428: gỡ thẻ %l VN tự thêm trên 扇形機関庫, JP chỉ có ruby — tiền lệ 日々姫08 gỡ 4 thẻ, 08b gỡ 34 thẻ).
- `[selections]` rỗng (0 mục). Không có lệch thẻ `%l` nào (6 dòng có thẻ, 5 khớp JP tuyệt đối; 1428 đã sửa). Thuật ngữ: 8 dòng 御一夜 dạng cũ (2247 "Ohimitera", 1962 + 2840 "Đường sắt Ohito" ×3, 2166, 2604, 2605, 2512, 2402) chờ đợt thống nhất, không tính sai (theo tiền lệ 日々姫08: 16 dòng không tính sai, parent đã kiểm chứng 20/11); 湯医, 帝鉄 (trừ 1366 đã sửa), 冥国, 冥軍, 小畑, 大畑, コン không xuất hiện; "gara đầu máy hình ngành" (扇形機関庫, 5 dòng) giữ nguyên — 23× toàn dự án, chờ Hieu chốt "hình ngành" hay "hình quạt" (xem §6 review). Không có bản sao file này ở thư mục khác.
- Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "cô" 1× (2058 "cảm ơn cô", ngữ cảnh công việc) vs "em" 0× — cộng dồn P09–15: "cô" 43× vs "em" 7×. "Toa ăn Train" (1358, 2572) giữ nguyên — đã ghi chú ở 日々姫08 §6.

**Tổng cộng sau file này: 86 file / 4.425 dòng sai** (cơ sở 85 file / 4.410 + 15 file này — rebase bởi parent sau khi 日々姫03 gộp trước, 41 dòng)
- Parent kiểm chứng 20/11 ~11:50: JSON 15 mục dạng chuẩn, khối TOML 15 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 15/15; sweep 5 mục áp nguyên đã kiểm chứng + 1431 audit tự tìm (JP 3× っ, VN cũ 2× Ư — đúng); đại từ: 1859 parent sửa 'mình'→'em' (lý do 'trả lời Nagi, dòng kề 2111' của agent SAI — 2111 cách ~250 key, thuộc cảnh khác; dòng kề là Soutetsu 1857/Hibiki 1856; tiền lệ ふかみh2 'em' với Soutetsu + 1831/1841/1798 'em' với Hibiki trong file; 'mình' chỉ với Nagi), 1721 fix 'chị' giữ nhưng dẫn chứng 'Hibiki đáp ngay 1874' SAI (1874 thuộc cảnh Kisaki bàn chi phí, nhiều khả năng cảm ơn Kisaki) — lý do đúng: khen thiết kế của Hibiki trước mặt cả nhóm, Paulette 'chị' với các em/cảnh nhóm; lượt soát 2 ghi trong review (15/15, 0 bỏ, 0 sửa) + parent sửa 1859. **Totals line REBASE: snippet ghi cơ sở 84/4.369, parent rebase thành 86/4.425 (cơ sở 85/4.410 sau khi 日々姫03 gộp trước).** Chờ Hieu: 'gara đầu máy hình ngành' vs 'hình quạt' (扇形, 23× toàn dự án); Soutetsu gọi Paulette 'cô' 43× vs 'em' 7× (P09–15); không chắc chắn 2632/1941; 8 dòng Ohitoyo dạng cũ chờ đợt thống nhất.


## 日々姫09 — 日々姫09_静かなる開戦.txt.toml — 15/401 (3,7%)

- File: `日々姫09_静かなる開戦.txt.toml` — route 02_Hibiki, 401 dòng script. Nội dung: họp báo từ chức của Paulette; Hibiki quyết định ứng cử thị trưởng; kế hoạch "chắp vá" toa xe phế liệu (8620 + KiHa 07S) trình trước các chủ trái phiếu; họp báo đối đầu của Kisaki trên TV; Hibiki sốt cao, cảnh Soutetsu bôi thuốc hạ sốt.
- Lệch vị trí 0, chưa dịch 0, cụt câu 0, không chắc chắn 0. 4/6 cờ strong-candidate là cũ (tính từ CSV cũ) — trong CSV3 các dòng 2139/2567/2601/2737 đều đã đúng, không có chuỗi xoay vòng.
- Phân loại (15): sfx/gasp 11 (1459, 1558, 1579, 1604, 1918, 1919, 1920 — 7 mục sweep áp nguyên đã kiểm chứng; 1240, 1560, 1565, 1607 — sweep bỏ sót, audit tự tìm); xưng hô 1 (1715: Soutetsu "em" → "anh" với Hibiki); bịa thêm 2 (1205: "Xin,"; 1904: Hibiki gọi "anh Soutetsu"); sai nghĩa 1 (2679: 素直 "ngoan ngoãn" → "thẳng thắn").
- `[selections]` rỗng (0 mục). Không có lệch thẻ `%l` nào (0 thẻ sai định dạng; 1899 thứ tự thẻ đảo do đảo câu, gloss khớp term). Thuật ngữ: 17 dòng 御一夜 dạng cũ "Ohimitera" + 5 dòng "thầy cúng Akai" (宮司) + 1690 "xưởng rượu Migita" thiếu "Ichi" chờ đợt thống nhất, không tính sai. Không có bản sao file này ở thư mục khác.
- Chi tiết đầy đủ: `audit-hibiki09-shizuka-kaisen-REVIEW.md`; danh sách sửa: `audit-hibiki09-shizuka-kaisen-wrong.json` (15 mục, khối TOML 15 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối).

**Tổng cộng sau file này: 87 file / 4.440 dòng sai** (cơ sở 86 file / 4.425 + 15 file này)
- Parent kiểm chứng 20/11 ~12:15: JSON 15 mục dạng chuẩn, khối TOML 15 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 15/15; đại từ 1715 kiểm chứng theo dòng kề (Soutetsu đáp Hibiki 1711–1718, 'anh' đúng quy tắc); 1607 kiểm chứng: JP むっ/あうっ + TW '塗在胸——唔，後背！' — fix thêm 'Mừ――áu' theo quy tắc SFX ngẫu hứng, giữ 'Ngực――à không, lưng!'; 1904 'anh Soutetsu' bịa thêm (JP にぃに/兄さん) đã gỡ; 2679 素直/TW 率直 → 'thẳng thắn' đúng; lượt soát 2 ghi trong review (15/15, 0 bỏ, 4 sửa). **Totals line: 87/4.440 (cơ sở 86/4.425 khớp ROUTE-AUDIT.md).** Chờ Hieu: 'Ohimitera' 17 dòng + 'thầy cúng Akai' 5 dòng + 1690 'xưởng rượu Migita' thiếu 'Ichi' chờ đợt thống nhất.


## ハチロク11 — ハチロク11_御一夜鉄道小畑線.txt.toml — 29/460 (6,3%)

- File: `ハチロク11_御一夜鉄道小畑線.txt.toml` — route 01_Hachiroku, 460 dòng script. Nội dung: chạy thử nghiệm tuyến Okoba (vượt đèo Yatake, vòng lặp Okoba); bàn về Tablet / Railord là chủng loài / sinh sản–nhân bản / niêm phong–Lõi Lord; Olivy từ chối đóng băng bảo quản.
- Lỗi hệ thống: chuỗi xoay vòng 16 dòng (thoại ↔ độc thoại xen kẽ): 15 dòng dời nguyên văn VN về đúng key (kiểm toàn dự án: mỗi VN lệch chỉ có ở 1 key trong file này), 2229 dịch mới (bản dịch đúng không có trong dự án), bản dịch của 2779 bị nhân đôi ở 2065 (2779 giữ nguyên, đã đúng).
- Phân loại: rotation 16 (1289, 1748, 1871, 1915, 1920, 2059, 2065, 2109, 2131, 2214, 2229, 2237, 2580, 2668, 2748, 2777), gasp 5 (1736, 1739, 1781, 2202, 2858 — 4 mục sweep + 2202 audit tự tìm), terminology 3 (1851, 2023, 2575: 冥国 “Meikoku”→“Minh Quốc”), sfx 2 (1744 ふぁ “Oa”→“Phà”, 1772 ふあ “Oa”→“Phùa”), mistranslation 2 (2191, 2193: thêm “vì” thừa), punctuation 1 (2600: dấu ' lẻ ở “Hinomoto'”). Thoại 22/286, độc thoại 7/174. Theo nhân vật: ポーレット 8, monologue 7, 双鉄 5, ハチロク 3, ニイロク 2, れいな 2, オリヴィ 1, 赤井 1.
- 0 misaligned ngoài chuỗi xoay / 0 rotation khác / 0 contamination liên file / 0 orphan / 0 untranslated / 0 duplicate key.
- CSV bộ duy nhất 460 dòng, 0 key trùng, 0 VN trống; CSV↔TOML: 205 khớp tuyệt đối + 255 gộp `\n` thành khoảng trắng, 0 khác biệt thực chất; comment # JP 460/460 khớp CSV3. TOML md5 31de0f3ff4f370e1a8520ae6cb2b841a, BOM + CRLF, [selections] rỗng, không bản sao trùng. Thẻ %l: JP = VN mọi dòng sau khi sửa chuỗi xoay (3 dòng chuyển ruby JP thành thẻ %l, chữ hiển thị đúng, không tính sai: 1652, 2055, 1827, 2262); 0 thẻ thiếu `;`.
- Sweep: 4 mục — 4 áp nguyên đã kiểm chứng (1736, 1739, 1781, 2858); audit tự tìm thêm 2202. Quét bổ sung toàn bộ 170 dòng JP có っ: các っ còn lại là nhấn mạnh/đã diễn, không gasp sót.
- Lượt soát 2: 29/29 tái kiểm chứng, 0 bỏ, 2 sửa (1851, 2023: bản nháp đầu làm rơi cặp 「」, đã sửa lại). JSON 29 khóa chuỗi; khối TOML parse OK, 29 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 29/29.
- Chờ Hieu (không tính sai): “Ohimitera” 3 dòng (1201, 2011, 2664) + “Đường sắt Ohito” 2 dòng (2121, 2446) chờ đợt thống nhất; 日ノ本 “Hinomoto” vs “Hinamoto” 4 dòng (1987, 2078, 2600, 2718).

**Tổng cộng sau file này: 88 file / 4.469 dòng sai** (cơ sở 87 file / 4.440 + 29 file này — rebase bởi parent sau khi 日々姫09 gộp trước, 15 dòng)
- Parent kiểm chứng 20/11 ~12:15: JSON 29 mục dạng chuẩn, khối TOML 29 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 29/29; chuỗi xoay 16 dòng kiểm chứng cơ học: 15 fix dời nguyên văn từ key khác trong file, 2229 dịch mới (JP 「でしたら、ね？　双鉄さま」, Hachiroku gọi 'ngài Soutetsu' — đúng); 2779 không trong JSON, VN trùng 2065 nguyên văn (đã đúng, giữ nguyên); gasp/sfx/terminology kiểm chứng theo JP (1744 ふぁ→'Phà', 1772 ふあ→'Phùa', 1851/2023/2575 冥国→'Minh Quốc'); lượt soát 2 ghi trong review (29/29, 0 bỏ, 2 sửa). **Totals line REBASE: snippet ghi cơ sở 86/4.425, parent rebase thành 88/4.469 (cơ sở 87/4.440 sau khi 日々姫09 gộp trước).** Chờ Hieu: 'Ohimitera'/'Đường sắt Ohito' 5 dòng chờ đợt thống nhất; 日ノ本 'Hinomoto' vs 'Hinamoto' 4 dòng.


## 日々姫09_run_with_our_dreams — 日々姫09_run_with_our_dreams.txt.toml — 10/378 (2,6%)

- File: `日々姫09_run_with_our_dreams.txt.toml` — route 02_Hibiki, 378 dòng script. Nội dung: lễ cưới Soutetsu–Hibiki trên GAMADUS (lễ 人前式): lời thề, trao nhẫn, nghi thức San-san-kudo, bài phát biểu với họ hàng/đối tác; Mikuro gặp lại Hachiroku; rời đi hưởng tuần trăng mật.
- Lệch vị trí 0, chưa dịch 0, cụt câu 0, không chắc chắn 0. 3/5 cờ strong-candidate là cũ (tính từ CSV cũ) — giá trị VN trong candidates file thuộc về key khác trong cùng file (1633←1752, 1845←1770, 2036←1781); trong CSV3/TOML cả 3 dòng đều đã đúng; 1854 chỉ khác ngắt dòng; 2125 khớp và đã đúng. Không có chuỗi xoay vòng.
- Phân loại (10): sfx tiếng cười 3 (1695, 1736, 1738 — うふふ/うふふぅ bị dịch "Ư fufu", bỏ gasp); gasp 2 (1778, 2478 — sweep, áp nguyên đã kiểm chứng); sai nghĩa 2 (2070: thì giả định → "Chuyến chèo thuyền… Không biết mọi chuyện đã ra sao nữa rồi"; 2366: "giơ ngón tay cái lên" → "giơ ngón tay lên"); xưng hô độc thoại 2 (2390, 2735: "anh" → "tôi"); thuật ngữ 1 (2483: "Gamadas" → "GAMADUS").
- `[selections]` rỗng (0 mục). Không có lệch thẻ `%l` nào (0 thẻ sai định dạng; 0 thẻ thiếu `;`). Thuật ngữ dạng cũ chờ đợt thống nhất, không tính sai: "Ohimitera" 3 dòng (1906, 2400, 2708), "Đường sắt Hoàng gia" 4 dòng (1687, 1906, 2046, 2095), "Yui" 2 dòng (1640, 2708), "cha xứ Akai" 3 dòng (2636, 2699, 2751), "Xưởng rượu Migita" thiếu "Ichi" 1 dòng (1840). Không có bản sao file này ở thư mục khác.
- Chi tiết đầy đủ: `audit-hibiki09-run-with-our-dreams-REVIEW.md`; danh sách sửa: `audit-hibiki09-run-with-our-dreams-wrong.json` (10 mục, khối TOML 10 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối).

**Tổng cộng sau file này: 89 file / 4.479 dòng sai** (cơ sở 88 file / 4.469 + 10 file này)
- Parent kiểm chứng 20/11 ~12:45: JSON 10 mục dạng chuẩn, khối TOML 10 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 10/10; đại từ 2390/2735 kiểm chứng theo dòng kề (độc thoại Soutetsu, cả file đồng nhất 'tôi' 146/148, 'anh' không có người nghe — lạc giọng, sửa 'tôi' đúng); 2070 kiểm chứng: JP どうなってたか là giả định quá khứ, TW xác nhận; **parent sửa 2070 khi gộp: khôi phục cặp 「」 bị agent làm rơi (nội dung dịch giữ nguyên, tổng không đổi)**; lượt soát 2 ghi trong review (10/10, 0 bỏ, 0 sửa). **Totals line: 89/4.479 (cơ sở 88/4.469 khớp ROUTE-AUDIT.md).** Chờ Hieu: 'Ohimitera' 3 + 'Đường sắt Hoàng gia' 4 + 'Yui' 2 + 'cha xứ Akai' 3 + 'Xưởng rượu Migita' thiếu 'Ichi' 1 chờ đợt thống nhất; 2010 'ông nội' gắn với câu hỏi ông nội/ông ngoại đang chờ chốt từ 08c.


## ハチロク04 — ハチロク04_煙には煙を.txt.toml — 10/389 (2,6%)

- File: `ハチロク04_煙には煙を.txt.toml` — route 01_Hachiroku, 389 dòng script. Nội dung: thử nghiệm khói lò sưởi trong toa hành khách; ý "lấy khói trị khói" — chuyến tàu BBQ thịt nướng; ảnh kỷ niệm chuyến số 1; Paulette báo đặt vé quá tải, bàn tăng chuyến + đào tạo Hibiki/Nagi, tin đồn đầu máy 6200 "Nelson".
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 389/389. `[selections]` rỗng. Không có thẻ `%l` sai định dạng (0/389). Không có bản sao file này.
- Phân loại (10): xưng hô 6 (1848, 2415: Hibiki "bọn anh"/"anh chị" → "bọn em"; 2058, 2425, 2392, 1920: Soutetsu "anh" → "tôi" với Hachiroku), sai nghĩa 2 (1855: phòng "rộng" → "chật hẹp" theo TW 狹窄; 2383: 6200 "xuất xưởng" → "xuất hiện trở lại"), cụt câu 1 (2062: bỏ mảnh vỡ "Cả,"), gasp 1 (2455: 「Ư!」 — sweep lost-gasp-whole, đã kiểm chứng; sweep còn 3088 đã diễn, không sửa).
- Thuật ngữ: "Ohito" 6 dòng (2073, 1855, 2393, 2105, 2464, 1920) + "Yui" 2 dòng (2947, 2464) chờ đợt thống nhất, không tính sai. Nagi → Fukami "cậu" (1894, 2076, 2078) giữ — biến thể 25× toàn dự án, chỉ cấm "chị". Paulette "tôi" (2189, 2192) giữ, chờ quyết. Ruby [ハチロク,3]/[ネルソン,3] bị bỏ (1544, 1531, 2459, 1533) — ghi chú chờ quyết.
- Chi tiết đầy đủ: `audit-hachiroku04-kemuri-REVIEW.md`; danh sách sửa: `audit-hachiroku04-kemuri-wrong.json` (10 mục, khối TOML 10 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 10/10; lượt soát 2: 10/10, 0 bỏ, 9 sửa — khôi phục 「」).

**Tổng cộng sau file này: 90 file / 4.489 dòng sai** (cơ sở 89 file / 4.479 + 10 file này — rebase bởi parent sau khi 日々姫09_run_with_our_dreams gộp trước, 10 dòng)
- Parent kiểm chứng 20/11 ~12:45: JSON 10 mục dạng chuẩn, khối TOML 10 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 10/10; đại từ kiểm chứng từng dòng kề: 2058 (monologue 2673, Hachiroku hướng mắt về Soutetsu), 2425 (gọi thẳng tên Hachiroku), 2392 ('trong lúc đó' = Hachiroku bàn ca trực với Paulette 2328/2136), 1920 (trả lời Hachiroku 2442, Hachiroku đáp 2195) — 'tôi' với Hachiroku đúng quy tắc; 1855 'chật hẹp' theo TW 狹窄 (JP この広さ mang nghĩa mỉa mai trong ngữ cảnh phàn nàn, TW giải nghĩa); 2383 出る→'xuất hiện trở lại' (TW 再出山); 2415 Hibiki 'bọn em' đúng (người nói là Hibiki); lượt soát 2 ghi trong review (10/10, 0 bỏ, 9 sửa — agent tự khôi phục 「」 làm rơi ở bản nháp). **Totals line REBASE: snippet ghi cơ sở 88/4.469, parent rebase thành 90/4.489 (cơ sở 89/4.479 sau khi 日々姫09_run_with_our_dreams gộp trước).** Chờ Hieu: 'Ohito' 6 dòng + 'Yui' 2 dòng chờ đợt thống nhất; 'ông nội' cho 爺ちゃん (2420, 2203) gắn với câu hỏi ông nội/ông ngoại; ruby [ハチロク,3]/[ネルソン,3] bị bỏ (1544, 1531, 2459, 1533) chờ quyết thống nhất.



## lrれいな追加03 — lrれいな追加03_れいなとのレール.txt.toml — 7/304 (2,3%)

- File: `lrれいな追加03_れいなとのレール.txt.toml` — route 04_Reina, 304 dòng script. Nội dung: Soutetsu và Reina hẹn hò tham quan Ohitoyo — luyện xúc than dồn toa (投炭), đi thuyền sông Kuma, làm dao, tham quan xưởng rượu Migita; bàn về gia đình và ước mơ nối đường sắt tới Katakami, Moji, Hiroshima.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 304/304 (187 chênh lệch chỉ là TOML-2 làm phẳng literal `\n` thành khoảng trắng, 0 khác biệt thực chất). `[selections]` rỗng. Không có thẻ `%l` nào trong file. Không có bản sao file này.
- Phân loại (7): sai nghĩa 3 (1122: "Anh thích chanh á?" → "Anh ăn chanh sao?" — TW "ăn nước chanh" + ngữ cảnh 1240/1246; 1534: とも "Cùng với" → "Hay là"; 1732: đảo nghĩa "không phản đối mạnh mẽ" → "không mạnh mẽ đòi hỏi" — TW "沒有強烈要求", 主張≠反対), bịa thêm 2 (1633: bỏ "vẻ đầy tự hào"; 1674: bỏ "ngực" — JP/TW không có), SFX 1 (659: ふぁ "Phá~" → "Phà~" theo quy tắc), gasp 1 (1079: 「Ư——」 — sweep raw-tsu, đã kiểm chứng; sweep chỉ có 1 mục cho file).
- Thuật ngữ: "Ohimitera" 4 dòng (675, 981, 1182, 1578) + "Đường sắt Ohito" 1 dòng (1319) chờ đợt thống nhất, không tính sai. Xưng hô Soutetsu sạch: 0 dòng "tôi" với Reina, monologue "mình" 2 dòng (1197, 1306) đúng ngoại lệ. TW sai ở 1007/1009 (100杯→1000) và 1240 — VN theo JP đúng.
- Chi tiết đầy đủ: `audit-lr-reina-tsuika03-REVIEW.md`; danh sách sửa: `audit-lr-reina-tsuika03-wrong.json` (7 mục, khối TOML 7 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 7/7; lượt soát 2: 7/7, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 91 file / 4.496 dòng sai** (cơ sở 90 file / 4.489 + 7 file này)
- Parent kiểm chứng 20/11 ~13:08: JSON 7 mục dạng chuẩn list-of-dicts, khóa chuỗi; khối TOML 7 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 7/7; diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (1732 là viết lại câu do đảo nghĩa, đã đối chiếu JP 主張 + TW); 1122 kiểm chứng theo TW + ngữ cảnh 1240/1246; lượt soát 2 ghi trong review (7/7, 0 bỏ, 0 sửa). **Totals line: 91/4.496 (cơ sở 90/4.489 khớp ROUTE-AUDIT.md, không cần rebase).** Chờ Hieu: 'Ohimitera' 4 + 'Đường sắt Ohito' 1 chờ đợt thống nhất; 1258 'mã-ãi' (ずうっと) có thể thống nhất thành 'mãi mãi'; 1357 JP gốc có ký tự '?' không đọc được, VN hoàn thiện theo TW.


## ふかみh3 — ふかみh3_夏休みの最後の日の、前の日.txt.toml — 28/649 (4,3%)

- File: `ふかみh3_夏休みの最後の日の、前の日.txt.toml` — route 07_Nagi_Fukami, 649 dòng script. Nội dung: buổi hẹn hò Soutetsu–Fukami dọc tuyến đường sắt ngày trước ngày cuối kỳ nghỉ hè: bài học đá ba-lát/nhổ cỏ/bảo trì đường ray, nhà ga bỏ hoang với bức vẽ ô chung tình (Kenji & Manami), mưa rào và trú mưa, gốc cây kỷ niệm của Nagi, cảnh H, chủ đề "tô điểm thêm kỷ niệm".
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 có 2 set × 649 — chỉ audit set tốt (11_Other); set home-folder (07_Nagi_Fukami) là STALE, JP bị xoay (642/649 VN lệch TOML).
- Phân loại (28): fa/fu 20 (2278, 2287, 2301, 2302, 2338, 2345, 2346, 2351, 2352, 2358, 2359, 2362, 2371, 2385, 2388, 2394, 2402, 2430, 2577, 2767 — "phù" cho mọi ふぁ/ふあ/ぷあ, trái quy tắc đã chốt 19/11, sửa thành "phà"/"phùa"); gasp 4 (1664, 2728 từ sweep; 1677, 2449 sweep bỏ sót — gasp cả dòng, TW xác nhận); sai nghĩa 3 (2130 "Hôm nay phải làm sao?" → "Hôm nay là sao?"; 3300 健気だ "Đáng yêu" → "Can đảm"; 3887 bỏ "chân em" thêm vào không có căn cứ JP/TW); bịa nghĩa 1 (2292: JP không có 雨, TW "居然這麼大" — "mưa to" là Gemini bịa từ bối cảnh, sửa thành "to"; KHÔNG phải lệch dòng).
- `[selections]` rỗng. Không có thẻ `%l` sai định dạng (25 mở / 25 đóng). Không có bản sao file này.
- Chi tiết đầy đủ: `audit-fukami-h3-REVIEW.md`; danh sách sửa: `audit-fukami-h3-wrong.json` (28 mục, khối TOML 28 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 28/28; lượt soát 2: 28/28, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 92 file / 4.524 dòng sai** (cơ sở 91 file / 4.496 + 28 file này — rebase bởi parent sau khi lrれいな追加03 gộp trước, 7 dòng)
- Parent kiểm chứng 20/11 ~13:16: JSON 28 mục dạng chuẩn, khóa chuỗi; khối TOML 28 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 (set tốt 11_Other) tuyệt đối 28/28; dual-set kiểm chứng độc lập: set 11_Other khớp TOML 649/649, set home-folder chỉ 7/649, JP khác nhau ở 546/649 key — agent audit đúng set; sweep kiểm chứng: 14 mục cho file, 1664/2728 có trong sweep, 1677/2449 vắng mặt — agent bắt đúng 2 gasp sweep bỏ sót; diff-sanity: 2292 chỉ bỏ "mưa "; 3300 đổi 1 từ "Đáng yêu"→"Can đảm"; 3887 chỉ bỏ " chân em"; các fix fa/fu chỉ đổi 1 ký tự đúng chỗ (2301/2359/2402/2767 kiểm tra từng dòng); lượt soát 2 ghi trong review (28/28, 0 bỏ, 0 sửa). **Totals line REBASE: snippet ghi cơ sở 90/4.489, parent rebase thành 92/4.524 (cơ sở 91/4.496 sau khi lrれいな追加03 gộp trước).** Chờ Hieu: 'Đường sắt Ohitera' 4 dòng (2442, 2506, 2638, 2867) + 日ノ本 'Hinomoto' 1 dòng (3178) chờ đợt thống nhất; 3300 'Can đảm quá' cho 健気だ và 3887 bỏ 'chân em' là 2 điểm cần Hieu xem lại cách diễn.


## 日々姫05 — 日々姫05_御一夜ステーションカフェ.txt.toml — 13/577 (2,3%)

- File: `日々姫05_御一夜ステーションカフェ.txt.toml` — route 02_Hibiki, 577 dòng script. Nội dung: ngày chạy thử quán cà phê ga Ohitoyo (Gamadas Café đổi tên) — Soutetsu và Hibiki phục vụ khách trong toa ăn (Hachiroku, Reina, Paulette, Kisaki, Fukami, Nagi, phu nhân Nagayama, các gia đình có trẻ con); thực đơn SL curry / dầu diesel / than đá; cuộc thi đặt biệt danh cho quán; chủ đề "mảnh ghép hạnh phúc" và bướm lột xác; sự bảo bọc quá mức của Mayami; chuyện cái chăn đắp cho hai người ngủ quên; kết bằng lời thề của Soutetsu sẽ làm ngọn gió nâng cánh Hibiki.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối sau chuẩn hóa `\\n` (326 lệch chỉ là TOML-2 làm phẳng literal `\\n` thành khoảng trắng, 0 khác biệt thực chất). `[selections]` rỗng. Thẻ `%l` đúng (3 thẻ: 2854 ×2, 3041 ×1). Không có bản sao file này.
- Phân loại (13): xưng hô 4 (1518 Soutetsu→Hibiki "tôi"→"anh"; 2212 Soutetsu→Hachiroku "anh"→"tôi"; 2407 Soutetsu→Mayami "em"→"tôi" ×2; 2577 độc thoại "Anh"→"Tôi"), gasp 4 (2040, 2069, 2967, 3330 — cả 4 từ sweep, đã kiểm chứng), SFX 4 (1509 ふぅ "Phù."→"Phùù." theo công thức nguyên âm; 2081 ああっ "A."→"Aa."; 2364 ああっ "A,"→"Aa,"; 1909 khôi phục tiếng cười ゲゲゲ "[Gegege,2]Tệ tệ tệ của [Ge]tệ đấy"), sai nghĩa 1 (3179 くすぐったそうに "buồn buồn buồn buồn"→"nhột").
- Chi tiết đầy đủ: `audit-hibiki05-station-cafe-REVIEW.md`; danh sách sửa: `audit-hibiki05-station-cafe-wrong.json` (13 mục, khối TOML 13 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 13/13; lượt soát 2: 13/13, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 93 file / 4.537 dòng sai** (cơ sở 92 file / 4.524 + 13 file này)
- Chờ Hieu: "Ohimitera" 3 dòng (2560, 3223, 3285) chờ đợt thống nhất; 1909 khôi phục thẻ [Gegege,2]/[Ge] cần Hieu xác nhận cách diễn; 1928 "chú" (người nghe không xác định chắc chắn) và 2038 gasp っ trước あ chưa diễn là 2 điểm cần Hieu xem lại.
- Parent kiểm chứng 20/11 ~13:45: JSON 13 mục dạng chuẩn, khóa chuỗi; khối TOML 13 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 13/13; đại từ kiểm chứng theo dòng kề (1518 Soutetsu→Hibiki 'anh'; 2212 đáp Hachiroku 2210 'tôi'; 2407 cảm ơn Mayami 'tôi'; 2577 độc thoại 'tôi'); gasp 4/4 từ sweep đã kiểm chứng; 1909 khôi phục thẻ [Gegege,2]/[Ge] theo JP ゲゲゲ là âm thanh; lượt soát 2 ghi trong review (13/13, 0 bỏ, 0 sửa). **Totals line: 93/4.537 (cơ sở 92/4.524 khớp ROUTE-AUDIT.md, không cần rebase).** Chờ Hieu: 'Ohimitera' 3 dòng chờ đợt thống nhất; 1909 cần xác nhận cách diễn; 1928 'chú' (người nghe chưa chắc) và 2038 gasp っ trước あ chưa diễn là 2 điểm cần xem lại.


## ハチロク14_冬 — ハチロク14_冬.txt.toml — 39/660 (5,9%)

- File: `ハチロク14_冬.txt.toml` — route 01_Hachiroku, 660 dòng script. Nội dung: đêm trực tuyết — Olivy sốt cao vẫn cố trực, giấu nhiệt độ bằng thạch một miếng; nước giếng lẫn cát ở nhiều nhà, nghi núi lửa Shin'endake hoạt động, lập ca trực 24h (3 ca × 8 tiếng); Hachiroku–Soutetsu bàn về "truyền đạt lại" và việc được nhớ đến.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 660/660 (5 chênh lệch chỉ là ký tự `\n` literal, 0 khác biệt thực chất). `[selections]` rỗng. Không có thẻ `%l` sai định dạng. Không có bản sao file này (md5 `b1d3343faed4a0f9fb1b27caa54db204`).
- Phân loại (39): gasp 12 (2385, 2386, 2515, 2551, 2552, 3154, 3623, 3861, 4104 từ sweep + 1760, 2590, 2690 sweep bỏ sót/sai phân loại), xưng hô/đại từ 12 (2573, 3143, 3190, 3202, 3256, 3257 Paulette→Soutetsu trái B4 lock "anh Soutetsu" + 2420, 2711, 2833, 2949, 3219 Soutetsu + 2684 Olivy tự xưng "chị"), thuật ngữ/gloss %l 13 (機関士→"nhân viên cơ vụ" 9 dòng, タブレット→"thẻ bảng" 3 dòng, 氏子→"giáo dân" 1, 運転体→"kíp lái" 1 — 3983 gộp 2 gloss trong 1 dòng), sai nghĩa/bịa 1 (3777: 義姉/義妹 → "chị/em gái nuôi", TW không có 養, sửa thành "chị chồng/em chồng"), SFX 1 (2549: うぅ → "Ưư" theo mẫu 2592).
- Sweep kiểm chứng: 9 mục cho file, nhận cả 9; bắt thêm 1760 (っ――ぁ), 2590 (っ / っっっ — sweep bỏ sót), 2690 (sweep ghi "already-rendered" là sai — cùng mẫu trailing ――っ như 3861/4104).
- Thuật ngữ: "Ohito" 8 dòng (1780, 2587, 2774, 2918 ×2, 3680, 3747, 3843, 4147) + "Yui" (湯医) 1 dòng (3680) chờ đợt thống nhất, không tính sai. Soutetsu sạch thêm: "anh" với Hibiki (3074), "anh hai" với Nagi (2649), "anh Soutetsu" với Reina (2976, 2993, 3254/3255) đều đúng.
- Chi tiết đầy đủ: `audit-hachiroku14-fuyu-REVIEW.md`; danh sách sửa: `audit-hachiroku14-fuyu-wrong.json` (39 mục, khối TOML 39 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 39/39; lượt soát 2: 39/39, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 94 file / 4.576 dòng sai** (cơ sở 93 file / 4.537 + 39 file này — rebase bởi parent sau khi 日々姫05 gộp trước, 13 dòng)

- Chờ Hieu: 2590 "Ưưư" (JP 3 っ vs TW 2 嗚); 3202 người nghe có phải Soutetsu ("anh") không; 3190 cách gọi Paulette→Olivy ("Nhờ cậu nhé" giữ nguyên); 3777 "chị chồng/em chồng" (Mayami/Hibiki) có hợp không; 2690 sweep sai phân loại.
- Parent kiểm chứng 20/11 ~13:45: JSON 39 mục dạng chuẩn, khóa chuỗi; khối TOML 39 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 39/39; diff-sanity: các fix gloss chỉ đổi đúng từ gloss ('nhân viên cơ vụ'→'thợ lái đầu máy', 'thẻ bảng'→'máy tính bảng'); đại từ kiểm chứng theo dòng kề (3202 người nghe Soutetsu — ủy quyền + lịch báo cáo 3 tiếng, nối tiếp 3143 trao toàn quyền và 3190 chuyển máy cho Soutetsu; 3219 'Nhờ cô nhé' ở 3220 → Hachiroku; 2711 đáp Olivy 2710; 2684 Olivy tự xưng 'tôi' như 2687); 3777 kiểm chứng: người nói Hachiroku (わたくし), 4073 Soutetsu gọi Hachiroku là 'vợ mình' nên 義姉/義妹 = chị/em gái của Soutetsu (Mayami/Hibiki, cf. 3139/3570 '真闇姉' ghép với Hibiki) → 'chị chồng/em chồng' có cơ sở, nhưng vẫn chờ Hieu chốt; lượt soát 2 ghi trong review (39/39, 0 bỏ, 0 sửa). **Totals line REBASE: snippet ghi cơ sở 92/4.524, parent rebase thành 94/4.576 (cơ sở 93/4.537 sau khi 日々姫05 gộp trước).** Chờ Hieu: 2590 'Ưưư' (JP 3 っ vs TW 2 嗚); 3202 người nghe; 3190 cách gọi Paulette→Olivy; 3777 'chị chồng/em chồng'; 2690 sweep sai phân loại.


## 凪ふかみ05 — 凪ふかみ05_凪の開眼！？.txt.toml — 18/478 (3,8%)

- File: `凪ふかみ05_凪の開眼！？.txt.toml` — route 07_Nagi_Fukami, 478 dòng script (343 thoại, 135 độc thoại). Nội dung: ngày "mở mắt" của Nagi — giúp bà lão xe lăn qua đường ray (Fukami tìm được tấm thẻ lấp lánh trong khe ghế bằng kinh nghiệm thuyền xuôi dòng); thi xúc than với Soutetsu; Hachiroku dạy chỉnh trang/cư xử; Kisaki dạy TPO, kính ngữ và đổi "bai"→"desu"; kết bằng chuyến tu học cùng "anh hai".
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 478/478. `[selections]` rỗng. Không có bản sao file này (md5 `0596fd7ef8f679f40a5822decef70eec`).
- Phân loại (18): xưng hô/đại từ 2 (2578 Fukami→bà lão "Em"→"Cháu", khớp 2489/2665 "cháu/chúng cháu"; 2648 Suzuki→ông lão Minokasa "em"→"ông" — TW 蓑笠小姐 là lỗi nữ hóa như file 09 key 2326), thuật ngữ 4 (2228, 2960 運転体→"thân vận hành" theo tiền lệ Hachiroku14 3983; 3167, 3276 "Kiha 07S"→"KiHa 07S"), thẻ %l VN tự thêm 7 (2214, 2215, 2391, 2479, 2522, 2475, 2989 — gỡ theo tiền lệ file 09/11; thẻ lấy từ JP từ TW, JP không có thẻ; 2522/2475 đồng thời sửa gloss 機関士→"thợ lái đầu máy"), gasp 1 (2058 từ sweep "Phù~~Ư"), SFX 4 (1970 ふぅ "Phù."→"Phùù." theo công thức; 2039 ひゃっ "Á."→"Hya." khớp 2095; 2068 はうっ "hauu"→"hau"; 3264 しゅっ×4 "Xình xịch"→"Xoẹt" — tiếng xẻng, không phải tiếng tàu).
- Sweep kiểm chứng: 3 mục cho file — nhận 2058; 2142 (「っ！」→"A!") và 2160 (「っ！！？」→"Ế!!?") đã diễn gasp, giữ nguyên. Sweep bỏ sót 1970, 2068, 3264.
- Nagi/Fukami: không có dòng nào dùng sai "chị"/"em" cho cặp này; Soutetsu "anh" với Nagi/Fukami đúng toàn file.
- Chi tiết đầy đủ: `audit-nagifukami05-kaigan-REVIEW.md`; danh sách sửa: `audit-nagifukami05-kaigan-wrong.json` (18 mục, khối TOML 18 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 18/18; lượt soát 2: 18/18, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 95 file / 4.594 dòng sai** (cơ sở 94 file / 4.576 dòng sai + 18 file này)

- Chờ Hieu: "Ohito"/"Ohimitera" 4 dòng (2483, 3222, 2367, 2266) + "Yui" 2 dòng (1979, 2972) chờ đợt thống nhất; 3161 じーちゃん→"ông nội" (câu hỏi "ông nội hay ông ngoại" đang chờ chốt); 2679 Nagi gọi Hachiroku "cô" vs 1981 "chị Hachiroku" có cần thống nhất không; 3268/3269 SFX giữ nguyên theo phán đoán.
- Parent kiểm chứng 20/11 ~14:15: JSON 18 mục dạng chuẩn, khóa chuỗi; khối TOML 18 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 18/18; đại từ kiểm chứng theo dòng kề (2578 Fukami→bà lão 'cháu' khớp 2489/2665; 2648 Suzuki→ông Minokasa, TW 蓑笠小姐 nữ hóa như file 09 key 2326); 3264 SFX viết lại cả dòng (しゅっ×4 là tiếng xẻng, không phải tiếng tàu); lượt soát 2 ghi trong review (18/18, 0 bỏ, 0 sửa). **Totals line: 95/4.594 (cơ sở 94/4.576 khớp ROUTE-AUDIT.md, không cần rebase).** Chờ Hieu: 'Ohito'/'Ohimitera' 4 dòng + 'Yui' 2 dòng chờ đợt thống nhất; 3161 'ông nội hay ông ngoại' đang chờ chốt; 2679 Nagi gọi Hachiroku 'cô' vs 1981 'chị Hachiroku'.


## ハチロク05_レイルロオドたち — ハチロク05_レイルロオドたち.txt.toml — 42/570 (7,4%)

- File: `ハチロク05_レイルロオドたち.txt.toml` — route 01_Hachiroku, 570 dòng script. Nội dung: Olivy đến Ohitoyo, Soutetsu truyền lại lời Munakata (chạy thử tuyến chính, môi trường tốt); Hachiroku khen ngợi công tác kiểm tra bảo dưỡng của "cô giáo Olivy"; chọn lái tàu cho chuyến chạy thử (Hibiki vs Nagi, cuối cùng rút thăm); Fukami lén học làm trưởng tàu; tranh luận "đường tắt vs đường vòng" (Olivy mắng Soutetsu ngạo mạn); báo cáo chạy thử với Paulette và Reina (Olivy 100 điểm, Hibiki chật vật với buồng lái tay phải, gia cố biển báo); Olivy nghe lén chuyện tuổi thọ (kiểm tra toàn diện hàng năm), suy sụp vì mình là Railord kiểu Meriken không có Master; kế hoạch của Soutetsu (lương, mua lại Đầu máy số 9, nghiên cứu kéo dài tuổi thọ); Olivy quá nhiệt, được đưa đi Tororyu-yu.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 570/570. `[selections]` rỗng. Không có thẻ `%l` sai định dạng. Không có bản sao file này (md5 `14a9b1b96740ced97469f984b138465f`).
- Phân loại (42): gasp 8 (2267, 2382, 2439, 2443, 2459, 3023, 3326, 3611 — tất cả từ sweep), xưng hô/đại từ 24 (Soutetsu→Hachiroku "anh"→"tôi" 3: 2476, 2667, 2233; Soutetsu→Paulette "tôi"→"anh" 9: 3024, 2475, 2689, 3062, 2944, 2449, 2960, 2710, 2836; Soutetsu→Olivy "tôi"→"anh" 6: 2685, 2819, 2879, 2663, 2679, 2688; Paulette→Soutetsu "cậu"→"anh" trái B4 lock 4: 2929, 3078, 2709, 2715; Hachiroku "xin lỗi anh" 1: 2431; 2949 "Giúp tôi"→"Giúp anh" ở vế cảm ơn Paulette, vế sau "đi theo tôi" với Hachiroku giữ nguyên), sai nghĩa 3 (2713: "ít liên quan nhất"→"vài người"; 2564: đảo chủ ngữ rút thăm; 3026: "giá trị lợi dụng"→"không còn cần đến nữa"), thuật ngữ 7 (冥国式 4: 2866 "kiểu Minh Quốc", 2605 furigana メリケン→"kiểu Meriken", 3501, 3740; 冥語 1: 3512 "tiếng Minh Quốc"; 可変パッド 2: 1728, 3057 "tấm đệm lót có thể điều chỉnh" — trong file 2322 đã dịch đúng).
- Sweep kiểm chứng: 8 mục cho file, nhận cả 8; quét máy bổ sung: không còn gasp nào sweep bỏ sót, không còn ký tự Nhật nào sót trong VN ngoài 4 dòng っ thô đã sửa.
- Thuật ngữ: "Ohito" 17 dòng (2473, 2455, 2834, 2922, 3555, 3461, 3706, 3790, 2640, 2361, 2765, 2941, 3743, 3003, 2960, 2316, 2638) + "Tuyến Yui" 7 dòng (2796, 2839, 2260, 2270, 2484, 2776, 2912) + "đèo Kobata" 1 dòng (3010) chờ đợt thống nhất, không tính sai. Soutetsu sạch thêm: "anh"/"em" với Olivy (2755, 2786, 2294, 2914, 2891, 2676, 3008, 2542), "anh" với Paulette (3055, 2296) đều đúng; "bọn anh"/"Chúng anh" (2842, 2775, 3075) giữ nguyên theo quy tắc nhóm.
- Chi tiết đầy đủ: `audit-hachiroku05-railord-tachi-REVIEW.md`; danh sách sửa: `audit-hachiroku05-railord-tachi-wrong.json` (42 mục, khối TOML 42 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 42/42; lượt soát 2: 42/42, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 96 file / 4.636 dòng sai** (cơ sở 95 file / 4.594 dòng sai + 42 file này — rebase bởi parent sau khi 凪ふかみ05 gộp trước, 18 dòng)
- Chờ Hieu: 2262 người nghe lẫn Hachiroku + Paulette nên giữ nguyên "anh"; 2539/2757/2663 Soutetsu gọi Olivy là "cô" (JP おまえ, giọng gay gắt) — giữ nguyên hay thống nhất "em"; 2879 câu JP dở dang, VN hoàn thiện theo TW; 2557 Hachiroku gọi Olivy "cậu" (JP あなた trung tính) giữ nguyên; 3512 冥語 → "tiếng Minh Quốc" (TW ghi 英語).
- Parent kiểm chứng 20/11 ~14:15: JSON 42 mục dạng chuẩn, khóa chuỗi; khối TOML 42 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 42/42; đại từ kiểm chứng theo dòng kề/nội dung (2476 đáp Hachiroku 3085 '双鉄さま？いかがされました？'; 2949 vế cảm ơn Paulette 3072 → 'Giúp anh', vế gọi Hachiroku giữ 'tôi'; 2929 B4 lock 'anh Soutetsu'; 2431 Hachiroku 'xin lỗi ạ'); 3512 'tiếng Minh Quốc' vs TW 英語 đã ghi chờ Hieu; lượt soát 2 ghi trong review (42/42, 0 bỏ, 0 sửa). **Totals line REBASE: snippet ghi cơ sở 94/4.576, parent rebase thành 96/4.636 (cơ sở 95/4.594 sau khi 凪ふかみ05 gộp trước).** Chờ Hieu: 2262 người nghe lẫn Hachiroku+Paulette; 2539/2757/2663 Soutetsu gọi Olivy 'cô' (JP おまえ) giữ hay thống nhất 'em'; 2879 JP dở dang hoàn thiện theo TW; 2557 Hachiroku gọi Olivy 'cậu'; 3512 'tiếng Minh Quốc' vs TW 英語.

## れいなh2 — れいなh2_おもらし防止大作戦.txt.toml — 23/284 (8,1%)

- File: `れいなh2_おもらし防止大作戦.txt.toml` — route 04_Reina, 284 dòng script (87 thoại Reina, 49 thoại Soutetsu, 148 độc thoại). Nội dung: Reina xin đặc huấn chống tè dầm — nhịn tè khi sướng, đặc huấn miệng để nuốt ực không nhả ra, làm tình đàng hoàng như người lớn; mặc đồng phục theo gợi ý của Paulette, ôm thú bông KiHa 07 làm bùa hộ mệnh; Soutetsu đặc huấn suốt đêm, kết bằng việc khắc sâu "bốn chữ" おもらし vào lòng.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 284/284. `[selections]` rỗng. Không có thẻ `%l` nào trong file. Không có bản sao file này (md5 `141739546028af97fdbac1c3ffe9ab6e`).
- Phân loại (23): gasp 4 (1031, 1070, 1071, 1215 — cả 4 từ sweep), fa/fu 14 (1001, 1027, 1036, 1052, 1061, 1065, 1081, 1114, 1174, 1180, 1182, 1183, 1184, 1185 — ふあ/ぷあ→"phùa", ふぁ→"phà", ふぇ→"phuê", tiền lệ ふかみh3), SFX cười 2 (1104 ふふ～っ, 1108 うふふぉ bị diễn thành "Ư hu hu~" như khóc/rên → "Fufu~"/"Ufufu~" theo quy tắc Hieu 19/11), bịa thêm 2 (1118 "ưm" thêm vào cho よ、ぉ; 1628 "tôi mở nó ra" theo TW, JP không có), sai nghĩa 1 (1465 その四文字→"bốn chữ ấy").
- Sweep kiểm chứng: 4 mục cho file, nhận cả 4; quét máy bổ sung không còn gasp nào sweep bỏ sót.
- Soutetsu "anh" với Reina đúng toàn file (0 dòng "tôi" sai đối tượng); "chị Paulette" (1145/1146) khớp 34 dòng route 04_Reina. Không có thuật ngữ chờ đợt thống nhất trong file.
- Chi tiết đầy đủ: `audit-reina-h2-omorashi-boushi-REVIEW.md`; danh sách sửa: `audit-reina-h2-omorashi-boushi-wrong.json` (23 mục, khối TOML 23 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 23/23; lượt soát 2: 23/23, 0 bỏ, 1 sửa).

**Tổng cộng sau file này: 97 file / 4.659 dòng sai** (cơ sở 96 file / 4.636 dòng sai + 23 file này)

- Chờ Hieu: không có mục nào chờ Hieu trong file này.
- Parent kiểm chứng 20/11 ~14:45: JSON 23 mục dạng chuẩn, khóa chuỗi; khối TOML 23 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 23/23; không có sửa đại từ; 1628 gỡ “tôi mở nó ra” theo JP (TW bịa thêm); 1118 gỡ “ưm” bịa, “đấy” diễn よ; 1104/1108 tiếng cười theo quy tắc Hieu 19/11; lượt soát 2 ghi trong review (23/23, 0 bỏ, 1 sửa). **Totals line: 97/4.659 (cơ sở 96/4.636 khớp ROUTE-AUDIT.md, không cần rebase).** Chờ Hieu: không có mục nào.

## ハチロクh5_おだいどこしごと — ハチロクh5_おだいどこしごと.txt.toml — 27/291 (9,3%)

- File: `ハチロクh5_おだいどこしごと.txt.toml` — route 01_Hachiroku, 291 dòng script. Nội dung: sau đợt cúm cả nhà, Hachiroku học nấu ăn từ Mayami và nấu cho Soutetsu; hai người làm tình trong bếp (tạp dề khỏa thân, "công việc bếp núc" của người vợ), Hachiroku tè dầm khi lên đỉnh, Soutetsu uống "nước tiểu" (thực chất là nước cất từ hơi nước), rồi làm tình lần hai và thề hẹn "mãi mãi về sau".
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 143/291 + 148 gộp `\n` thành khoảng trắng, 0 khác biệt thực chất. `[selections]` rỗng. Không có thẻ `%l` nào (JP = VN = TOML = 0). Không có bản sao file này (md5 `4f711f40ec474cb1d9de27daee7eda85`).
- Phân loại (27): gasp 7 (992, 1031, 1085, 1401, 1416, 998, 1075), fa/fu 6 (1006, 1008, 1010, 1011, 1033, 1089), SFX khác 14 — trong đó 4 dòng mang cả fa/fu + gasp (1064, 1065, 1073, 1222) và 3 dòng mang cả gasp + đếm nguyên âm (996, 1067, 1077). Theo nhân vật: ハチロク 22, 双鉄H 3, monologue 2.
- Sweep kiểm chứng: 6 mục cho file, áp nguyên cả 6 (1064/1065 gộp thêm sửa fa); sweep bỏ sót 1085 (~~~~ + っっ → ƯƯ, tiền lệ ハチロクh6); quét bổ sung toàn bộ 172 dòng JP chứa っ bắt thêm 9 gasp cuối dòng rên (996, 998, 1067, 1073, 1075, 1077, 1222, 1015, 1070). っ nhấn mạnh gắn với từ (さまっ, すずっ, ですっ…) giữ nguyên theo tiền lệ h9/fukamih2.
- Đại từ/đại từ xưng hô: Soutetsu "tôi" với Hachiroku nhất quán toàn file, Hachiroku "em" / "ngài Soutetsu" nhất quán — 0 lỗi. Thuật ngữ: "nhà Migita" đúng; không có Ohitoyo/Teitetsu/Yui/Okoba trong file.
- Chi tiết đầy đủ: `audit-hachiroku-h5-odaidoko-REVIEW.md`; danh sách sửa: `audit-hachiroku-h5-odaidoko-wrong.json` (27 mục, khối TOML 27 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 27/27; lượt soát 2: 27/27, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 98 file / 4.686 dòng sai** (cơ sở 97 file / 4.659 dòng sai + 27 file này — rebase bởi parent sau khi れいなh2 gộp trước, 23 dòng)

- Chờ Hieu: mâu thuẫn fa/fu toàn dự án — ふあっ → "phùa" (MEMORY + ふかみh3, parent-verified) vs "phù" (lr_ふかみh2, parent-verified); quy tắc ひゃ đầu tiếng rên dài chưa chốt (996 giữ "Á", 999/1000 sửa → "Hya" theo 凪ふかみ05); phán đoán SFX 1008 (あひっ→"Ahi"), 1015 (はひっ→"Hahí"), 1227 (かふっ→"Kaphù", tiền lệ paulette-h7 chưa parent-verify); 998 れふっ giữ nguyên.
- Parent kiểm chứng 20/11 ~15:00: JSON 27 mục dạng chuẩn, khóa chuỗi; khối TOML 27 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 27/27; không có sửa đại từ; 759 'ưm ư' theo tiền lệ ハチロクh9 2144; 996 giữ 'Á' cho ひゃ rên dài (chưa có quy tắc chốt, như lr_ふかみh2); 1070 'phù a' giữ (đủ âm, khác cách ngắt âm tiết với 'phùa' — ghi đợt thống nhất). **PHÁN QUYẾT fa/fu của parent: ふあ → 'phùa' giữ nguyên** (quy tắc đã chốt 19/11; 'phù' làm mất âm あ, trái 'không để mất âm') — 9 dòng fa/fu của file này giữ nguyên; lr_ふかみh2 'phù' 11 dòng theo review (987, 1030, 1039, 1094, 1101, 1104, 1191, 1262, 1269, 1270, 1273, 1277 + dạng dài 1268) chuyển sang đợt thống nhất. **Totals line REBASE: snippet ghi cơ sở 96/4.636 → 97/4.663; tổng đúng 98/4.686 (cơ sở 97/4.659 sau khi れいなh2 gộp trước).** Chờ Hieu: ひゃ đầu tiếng rên dài chưa có quy tắc chốt; SFX phán đoán 1008/1015/1227.

## れいなh3 — れいなh3_おもらし自由化大作戦.txt.toml — 24/279 (8,6%)

- File: `れいなh3_おもらし自由化大作戦.txt.toml` — route 04_Reina, 279 dòng script (84 thoại Reina, 60 thoại Soutetsu, 135 độc thoại). Nội dung: Reina đặc huấn "tự do hoá" việc tè dầm trong bồn tắm bao trọn gói mượn của chủ Tororyu-yu — Soutetsu dạy Reina rằng xuất tinh của anh và tè dầm của cô bé là một; Reina học deep throat, tập nhịn/xả; kết bằng cảnh ngâm bồn chung và thỏ khăn tắm.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 279/279. `[selections]` rỗng. Không có thẻ `%l` nào trong file. Không có bản sao file này (md5 `6c1b1c26745216faeebd6d942cc2e2f4`).
- Phân loại (24): gasp 4 (1050, 1074, 1080, 1099 — 3 từ sweep + 1 sweep bỏ sót 1050), fa/fu 17 (1014, 1019, 1031, 1047, 1048, 1053, 1068, 1073, 1078, 1083, 1119, 1121, 1195, 1196, 1197, 1198, 1200 — ふあ/ふぁ/ぷあ→"phùa"/"phà", ふぇ→"phuê", ふやぁ→"phuya"), SFX 3 (1054 んくっ→"nku", 1071 chuỗi rên mất âm, 1090 んうっ→"ưm").
- Sweep kiểm chứng: 4 mục cho file, nhận 3 fix + 1 already-rendered (1199); quét máy bổ sung bắt thêm 1 gasp sweep bỏ sót (1050).
- Soutetsu "anh" với Reina đúng toàn file (0 dòng "tôi" sai đối tượng — "tôi" chỉ ở 1718 suy nghĩ trong ngoặc đơn, "mình" ở 1751 theo ngoại lệ độc thoại nội tâm). Không có thuật ngữ chờ đợt thống nhất trong file.
- Chi tiết đầy đủ: `audit-reinah3-omorrashi-jiyuuka-REVIEW.md`; danh sách sửa: `audit-reinah3-omorrashi-jiyuuka-wrong.json` (24 mục, khối TOML 24 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 24/24; lượt soát 2: 24/24, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 99 file / 4.710 dòng sai** (cơ sở 98 file / 4.686 dòng sai + 24 file này)

- Chờ Hieu: 1115 (lời ngọng phiên âm — chuẩn hoá ふぁ→"phà" hay giữ nguyên cả dòng); 1133 (ふえっ？→"hả?" hay "phuê?"); số lượng nguyên âm tiếng rên dài (1099: 7 u cho 4 う); mâu thuẫn fa/fu toàn dự án ("phùa" vs "phù").

- Parent kiểm chứng 20/11 ~15:45: JSON 24 mục dạng chuẩn, khóa chuỗi; khối TOML 24 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 24/24; không có sửa đại từ; 1047 ひゅっ――ふあっ → 'Hyu——phùa' đúng JP; 1050 gasp sweep bỏ sót (JP っ trần → 'Ư', tiền lệ sweep); 1031 'Fua' → 'Phà' theo quy tắc ふぁ→'phà'; lượt soát 2 ghi trong review (24/24, 0 bỏ, 0 sửa). **Totals line: 99/4.710 (cơ sở 98/4.686 khớp ROUTE-AUDIT.md, không cần rebase).** Chờ Hieu: 1115 lời ngọng phiên âm (chuẩn hoá ふぁ→'phà' hay giữ nguyên cả dòng); 1133 ふえっ？ 'hả?' hay 'phuê?'; số lượng nguyên âm tiếng rên dài (1099: 7 u cho 4 う).

## 凪h2_おとなの水着 — 凪h2_おとなの水着.txt.toml — 89/673 (13,2%)

- File: `凪h2_おとなの水着.txt.toml` — route 07_Nagi_Fukami, 673 dòng script. Nội dung: Nagi và Soutetsu mua đồ bơi qua mạng (chọn đồ bơi "người lớn" chững chạc thay cho đồ bơi quy định của trường, bàn về thương hiệu Channel/Vucci, đồ bơi cũ), rồi Nagi thử đồ bơi trước mặt Soutetsu; cảnh làm tình dài (Nagi mặc đồ bơi, oral, Soutetsu xuất tinh), xen kẽ trò chuyện về bà nội, kiếm thuật, đốt ngải cứu, và kỷ niệm với Fukami; cuối file hai người làm huy hiệu biểu trưng đầu tàu (御一夜鉄道).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 673/673, 0 khác biệt thực chất. `[selections]` rỗng. Không có thẻ `%l` nào (JP = VN = TOML = 0). Không có bản sao file này (md5 `a581ef85d1d7aed81fc5303b23f050ea`).
- Phân loại (89): đại từ 50, gasp 7, fa/fu 5, SFX 15, đếm nguyên âm 9, nghĩa 3. Theo nhân vật: 双鉄 56 (đại từ 50 + gasp 3 + đếm nguyên âm 3), 凪 25 (SFX 15 + fa/fu 5 + đếm nguyên âm 4 + nghĩa 1), monologue 8 (gasp 4 + nghĩa 2 + đếm nguyên âm 2).
- Sweep kiểm chứng: 8 mục cho file — 7 mục lost-gasp-trailing áp nguyên cả 7 (2487, 2536, 2544, 3354, 3433, 3610, 3719); mục 2489 ghi "already-rendered" nhưng kiểm tra lại vẫn sai 2 âm (んひゅっ → "Ưm hứ", んんん～っ → "Ưmmm~") nên sửa luôn. Quét bổ sung toàn bộ các dòng JP kết bằng っ: không bắt thêm gasp nào — các っ còn lại đều là っ nhấn mạnh gắn với từ (だっ/ぞっ/にっ/ちんっ/とっ/ねっ/さまっ), っ theo sau bởi ――/、/……, hoặc onomatopoeia đã dịch thành từ Việt (ぺろっ → "Liếm", はむっ → "Ngoạm", カチっ → "click") — giữ nguyên theo tiền lệ.
- Đại từ: lỗi hệ thống — Soutetsu xưng "tôi" với Nagi trong 50/164 dòng thoại (61 lần), ngược với tiền lệ 凪ふかみ05 ("Soutetsu anh với Nagi/Fukami đúng toàn file"); Soutetsu tự xưng "anh" đúng: 0 dòng. Đã quét lại case-insensitive toàn file (bắt thêm 2 dòng chỉ có "Tôi" viết hoa đầu câu: 2712, 2717). Nagi gọi Soutetsu "anh hai" nhất quán; Fukami chỉ được nhắc tên ("bé Fukami" — đúng quy tắc cùng tuổi). Monologue "tôi" giữ nguyên. "Chúng tôi"/"bọn tôi": 0 dòng.
- Thuật ngữ: 帝都 → "Đế đô", 市電 → "tàu điện thành phố", 帝鉄 → "Teitetsu", 湯医 → "Yunoi" đúng; ちゅ-family thống nhất "Chụt". Đếm nguyên âm: 5 dòng "Oa" sai nguyên âm o→a (2603, 2607, 2612, 2613, 2751); 2410 đếm lại bằng script (17 u → 15 u). Nghĩa: 2749 "Phải mở ra" ngược nghĩa với あけんと ("không mở được"); 3346 bỏ mất 無い; 3717 bịa thêm "dồn toa".
- Chi tiết đầy đủ: `audit-nagih2-otonano-mizugi-REVIEW.md`; danh sách sửa: `audit-nagih2-otonano-mizugi-wrong.json` (89 mục, khối TOML 89 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 89/89; lượt soát 2: 89/89, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 100 file / 4.799 dòng sai** (cơ sở 99 file / 4.710 dòng sai + 89 file này — rebase bởi parent sau khi れいなh3 gộp trước, 24 dòng)

- Chờ Hieu: phán đoán 2520 あぐっ → "Agù" (tiền lệ mâu thuẫn: 3 file dùng "A"/"Á" vs 1 file "Agu" — cần parent chốt); 2529 あー → "Aa" (日々姫06 dùng "Aaa!" cho あー！); đợt thống nhất: "Đường sắt Ohito" (1766, 3568), "Đại học Hoàng gia" (1759), "hợp đồng Maitetsu" (1766), "Phù a" giữ nguyên (2452, 2445, 2589, 2428, 2526), "ông nội/bà nội" (2668 — chờ chốt "ông nội" hay "ông ngoại").

- Parent kiểm chứng 20/11 ~15:45: JSON 89 mục dạng chuẩn, khóa chuỗi; khối TOML 89 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 89/89; đại từ kiểm chứng qua dòng kề (mẫu 11/50 dòng đều đối thoại với Nagi — 'anh hai', 'em'; 61 lần 'tôi' trong 50 dòng 双鉄, sửa chỉ đổi tôi→anh, giữ nguyên viết hoa đầu câu); 2749/3346/3717 nghĩa kiểm tra đúng JP/TW; lượt soát 2 ghi trong review (89/89, 0 bỏ, 0 sửa). **PHÁN QUYẾT 2520 あぐっ: giữ 'Agù'** — §5 của agent ghi ngược tiền lệ: tiền lệ đã audit là 'Agu' (Common 05 key 2284 + Common 09 key 2326, đều đã gộp); 'A' chỉ là VN cũ trước audit. **Totals line REBASE: snippet ghi cơ sở 98/4.686 → 99/4.775; tổng đúng 100/4.799 (cơ sở 99/4.710 sau khi れいなh3 gộp trước).** Chờ Hieu: 2529 あー → 'Aa' (日々姫06 dùng 'Aaa!' cho あー！); đợt thống nhất 'Đường sắt Ohito' (1766, 3568), 'Đại học Hoàng gia' (1759), 'hợp đồng Maitetsu' (1766), 'Phù a' giữ nguyên (5 dòng), 'ông nội/bà nội' 2668.

## 日々姫10_稀咲の未来図、日々姫の未来図 — 日々姫10 (02_Hibiki) — 16/489 (3,3%)

- File: `日々姫10_稀咲の未来図、日々姫の未来図.txt.toml` — route 02_Hibiki, 489 dòng script. Nội dung: phỏng vấn Kisaki của phóng viên Ichikawa; trình diễn sa bàn N-gauge (KiHa 07 + 8620); Hibiki vật lộn vẽ "bản đồ tương lai", bị Kisaki sao chép kế hoạch phục hồi toa xe; Hibiki quỳ rạp xin lỗi cả nhóm.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất; TOML-2 dẹp `\n` thành khoảng trắng ở 317 dòng (chỉ khác định dạng, CSV3 làm chuẩn).
- Phân loại (16): gasp 2 (2940, 3390 — cả 2 từ sweep, đều nhận); đại từ 3 (2691 Soutetsu "tôi"→"anh" với Paulette; 2847 Fukami "chị"→"mình" với Nagi; 2925 Hachiroku "Anh"→"Ngài" với Soutetsu); sai nghĩa 4 (2647 "Chắc…… vậy thôi" → "Ừ…… đúng vậy."; 2888 「いいか」 "lại đây nào" → "được chứ?"; 3620 破顔一笑 "phá lên cười" → "nhoẻn miệng cười"; 3666 様付け "kính ngữ \"cô\"" → "thôi gọi Kisaki bằng kính ngữ"); phong cách 3 (2581, 2602, 2920 — です đứng một mình thành "Ạ."); bịa nghĩa 1 (2437 「いやいや、どうもどうも」 → "Chắc chắn rồi"); bỏ sót 1 (2720 集合運転装置 "thiết bị lái tích hợp"); thẻ %l 1 (2781 — ngắt dòng nằm trong thẻ, dời ra sau `#;`); phiên âm 1 (2943 えぬ "En-nu" → "N").
- `[selections]` rỗng. Không có bản sao file này (md5 `45ecfdf18d22d323e120874ecafc3a6c` duy nhất).
- Chi tiết đầy đủ: `audit-hibiki10-miraizu-REVIEW.md`; danh sách sửa: `audit-hibiki10-miraizu-wrong.json` (16 mục, khối TOML 16 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 16/16; lượt soát 2: 16/16, 0 bỏ, 0 sửa).
- Chờ Hieu: 2464 (JP 1 dòng 「うんっ！」 vs TW/VN 2 dòng 「Vâng!」 — nhân đôi hay lặp thật trong game?); 2595 + 2715 (Hibiki tự xưng "chị" trong cảnh đông người — "em" nếu nói với Soutetsu); thuật ngữ dạng cũ chờ thống nhất: "Ohimitera" 24 dòng, "Đường sắt Hoàng gia" 1 (2495), "tuyến Yui" 1 (2613), "Circuithium" 1 (2458).

**Tổng cộng sau file này: 101 file / 4.815 dòng sai** (cơ sở 100 file / 4.799 dòng sai + 16 file này)
- Parent kiểm chứng 20/11 ~16:00: JSON 16 mục dạng chuẩn, khóa chuỗi; khối TOML 16 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 16/16; đại từ kiểm chứng qua dòng kề: 2691 Soutetsu nói thẳng với Paulette ("ポーレット、すまんが") → "anh" đúng; 2847 Fukami nói với Nagi ("凪ちゃんは…") → "mình" đúng; 2925 Hachiroku, dòng kề 2922 "双鉄様？" → "Ngài" đúng; 2437 bịa nghĩa kiểm tra đúng JP/TW; 2888 「いいか」 theo JP (JP thắng TW "過來一下"); 3620 破顔一笑 → "nhoẻn miệng cười" đúng; lượt soát 2 ghi trong review (16/16, 0 bỏ, 0 sửa). **Totals line: 101/4.815 (cơ sở 100/4.799 khớp ROUTE-AUDIT.md, không cần rebase).** Chờ Hieu: 2464 nhân đôi "Vâng!" (JP 1 dòng vs TW/VN 2 dòng); 2595 + 2715 Hibiki "chị" trong cảnh đông người; đợt thống nhất "Ohimitera" 24 dòng, "Đường sắt Hoàng gia" (2495), "tuyến Yui" (2613), "Circuithium" (2458).

## 01_Hachiroku ハチロク06_のぞみ — 31/501 (6,2%)

- File: `01_Hachiroku/ハチロク06_のぞみ.txt.toml` (501 dòng script; monologue 149, Soutetsu 95, Hachiroku 89, Olivy 82, bà chủ 35, Hibiki 32, Mayami 17, Reina 1, Paulette 1). TOML md5 f8bbef02ab93efa20463ffb54186c7f9, không có bản trùng; CSV3 1 bộ 501 dòng, key khớp tuyệt đối.
- Lỗi chính: đại từ 14 (Hachiroku↔Olivy 7 — Olivy lớn tuổi hơn Hachiroku, bằng chứng chính file này key 3455 + tiền lệ ハチロク15a 1947/2560; Soutetsu độc thoại "chị Hibiki"→"em Hibiki" 4 — Hibiki là em gái ruột của Soutetsu; bà chủ nhà tắm Tororyu-yu "ông chủ"→"bà chủ" 2; Soutetsu xưng hô nhóm "anh"→"tôi" 1 ở 2830, tiền lệ Paulette 14:1544), thuật ngữ 13 (Aerocraft→Aircra 9, Master Controller→điều khiển trung tâm 1, Đường sắt Hoàng gia→Teitetsu 1, Điện xá Công chúa→Công chúa Tàu điện 2), sai nghĩa 2 (1664 câu cảm thán bị dịch thành câu hỏi; 2279 nghĩa ngược về chăn hè), sweep っ 1 (2402, đã kiểm chứng), format 1 (2370 rác annotation [8620'86]).
- 0 chưa dịch, 0 trùng key, 0 tràn file khác, 0 dòng mồ côi, 0 chuỗi xoay vòng. Lượt soát 2: 31/31/0/0.
- Chờ Hieu (không tính sai): 1660 博太→"Hakuta" hay "Hakata" (TW đọc 博多); tên gọi Densha-hime chưa thống nhất toàn dự án (5+ dạng); ruby [X,n] chưa thống nhất; Olivy xưng "cậu" với Soutetsu/Hachiroku (giữ nguyên); Soutetsu tự xưng với Olivy "tôi" hay "anh" (file này dùng "tôi" nhất quán, quy tắc chưa bao phủ).
- Chi tiết đầy đủ: `audit-hachiroku06-nozomi-REVIEW.md`; danh sách sửa: `audit-hachiroku06-nozomi-wrong.json` (31 mục, khối TOML 31 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 31/31).

**Tổng cộng sau file này: 102 file / 4.846 dòng sai** (cơ sở 101 file / 4.815 dòng sai + 31 file này — rebase bởi parent sau khi 日々姫10 gộp trước, 16 dòng)
- Parent kiểm chứng 20/11 ~16:00: JSON 31 mục dạng chuẩn, khóa chuỗi; khối TOML 31 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 31/31; đại từ kiểm chứng qua dòng kề: cụm Olivy 7 dòng đúng — bằng chứng 3455 「オリヴィは…ハチロクよりも古いのだ」 + 2457 Hachiroku gọi Olivy 先輩; 2378 TW "謝謝你奧莉薇" xác nhận cảm ơn Olivy; bà chủ nhà tắm là nữ — VN đã dùng "bà chủ" (1550/2607/3453) + chủ tự xưng ウチ (2271); Soutetsu độc thoại "chị Hibiki"→"em Hibiki" 4 dòng đúng (Hibiki là em gái ruột; 3329 JP 真闇姉); 2830 xưng hô nhóm → "tôi" theo tiền lệ Paulette 14:1544; 1664/2279 nghĩa kiểm tra đúng JP/TW; lượt soát 2 ghi trong review (31/31, 0 bỏ, 0 sửa). **Totals line REBASE: snippet ghi cơ sở 100/4.799 → 101/4.815; tổng đúng 102/4.846 (cơ sở 101/4.815 sau khi 日々姫10 gộp trước).** Chờ Hieu: 1660 博太 "Hakuta" hay "Hakata"; tên Densha-hime chưa thống nhất (5+ dạng); ruby [X,n]; Olivy xưng "cậu"; Soutetsu xưng với Olivy "tôi" hay "anh".

## 10_Chikuni 仲国05_真夜中の餐車 — 14/467 (3,0%)

- File: `10_Chikuni/仲国05_真夜中の餐車.txt.toml` (467 dòng script; monologue 234, Hachiroku 81, Suika 56, Soutetsu 54, Hibiki 18, Zhihuan 17, Jiang 7). TOML md5 fe04f16828477df45bf95ab529d47673, không có bản trùng; CSV3 1 bộ 467 dòng, key khớp tuyệt đối.
- Lỗi chính: gasp っ 13 (10 theo sweep đã kiểm chứng + 3 sweep bỏ sót: 1946 っ đầu dòng, 1562 「っ――」, 2378 kèm ふえっ→"Phuê" theo quy tắc fa/fu), thuật ngữ 1 (1605 整備体 "thân chính"→"thân bảo trì").
- 0 chưa dịch, 0 trùng key, 0 tràn file khác, 0 dòng mồ côi, 0 chuỗi xoay vòng. Lượt soát 2: 14/14/0/0.
- Chờ Hieu (không tính sai): 1956/2254 っ cuối tuyệt đối không dấu câu (thêm Ư hay giữ nguyên); ruby [X,n] chưa thống nhất; 1926 "từ dưới đếm lên" hơi khó hiểu; 3303/3280 cùng "(Phịch)" cho とっ vs どさっ.
- Chi tiết đầy đủ: `audit-chukuni05-REVIEW.md`; danh sách sửa: `audit-chukuni05-wrong.json` (14 mục, khối TOML 14 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 14/14).

```toml
[script]
1562 = "「Ư――」"
1605 = "「……Đúng vậy. Ngay cả với [cơ thể này] thân bảo trì cũng có thể nhận ra,\\nchắc chắn độ dốc không hề nhỏ.」"
1946 = "「Ư!!!? Có chuyện gì vậy, Hachiroku.」"
1947 = "「Ư!!?」"
1972 = "「Ư!!!」"
1982 = "「Ư!!」"
1983 = "「Ư!!?」\\n「Đúng vậy. Khớp nối toa xe cũng đang bị kéo căng――trước hết là cái đó.」"
2071 = "「Sao vậy? ――Ư!\\nKhông lẽ đi lại mệt mỏi quá nên phát sốt rồi.」"
2365 = "「Thầy Soutetsu sao? Suika――\\nkhông hề nghe thấy tiếng bước chân nào như vậy――Ư!!?」"
2375 = "「Ư!!!!!」"
2376 = "「Ư!!!?」"
2378 = "「Ư!!!?」「Phuê!?」\\n「Có chuyện gì vậy!?」"
2874 = "Dù không hề ra lệnh, nhưng khí xả tự động lọt ra từ miệng tôi,\\ntạo thành một tiếng động lớn không ngờ――Ư!"
3158 = "Suika khẽ gật đầu.\\nVì vậy, tôi mở cộng cảm――Ư!!!!!!!!!"
```

**Tổng cộng sau file này: 103 file / 4.860 dòng sai** (cơ sở 102 file / 4.846 dòng sai + 14 file này)
- Parent kiểm chứng 20/11 ~16:15: JSON 14 mục dạng chuẩn, khóa chuỗi; khối TOML 14 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 14/14; diff-sanity: chỉ chèn Ư / 1 thuật ngữ (1605 整備体→"thân bảo trì") / 1 fa-fu (2378 ふえっ→"Phuê"); lượt soát 2 ghi trong review (14/14, 0 bỏ, 0 sửa). **Totals line: 103/4.860 (cơ sở 102/4.846 khớp ROUTE-AUDIT.md, không cần rebase).** Chờ Hieu: 1956/2254 っ cuối tuyệt đối không dấu câu (thêm Ư hay giữ nguyên); ruby [X,n] chưa thống nhất; 1926 "từ dưới đếm lên" hơi khó hiểu; 3303/3280 cùng "(Phịch)" cho とっ vs どさっ.

## 01_Hachiroku ハチロクh6_ウェディングドレスを脱ぎ捨てて — 16/461 (3,5%)

- File: `01_Hachiroku/ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml` (461 dòng script; monologue 266, ハチロク 118, 双鉄 77). TOML md5 9c51863393588f1bb888afa1bdbec48a, không có bản trùng; CSV3 1 bộ 461 dòng, key khớp tuyệt đối (245 "lệch" chỉ là TOML làm phẳng `\n` thành khoảng trắng).
- Lỗi chính: gasp っ 13 (11 theo sweep đã kiểm chứng lại từng dòng — 519, 775, 873, 1008, 1080–1083, 1085, 1557, 1771; 2 đầu dòng sweep bỏ sót — 515, 516, cùng file 509/513 đều giữ Ư), từ bịa thêm 2 (1050 "mất", 1760 "liếm lấy"), đọc sai tên vỡ 1 (511: そう→"ngài", さ→"của" — đúng ra Sou–tetsu–ngài, TW xác nhận).
- 0 lệch/luân chuyển, 0 dòng mồ côi, 0 chưa dịch, 0 trùng key, 0 lỗi %l; đại từ Soutetsu "tôi" với Hachiroku đúng suốt; thuật ngữ đã quyết (Railord, cộng cảm, miếng dán ngực, phu quân) đúng. Lượt soát 2: 16/16/0/0.
- Chờ Hieu (không tính sai): fa/fu biến thể "phù a"/"phù" 14 dòng (829, 830, 831, 832, 852, 863, 881, 884, 915, 930, 941, 948, 950, 1020) — để unification pass theo tiền lệ lr_ふかみh2; key 491 JP cụt (TW "hết sức rồi" vs VN mơ hồ, giữ nguyên); key 1813 JP "旧悪" lạ (gần như chắc là lỗi gõ của 凶悪, VN theo TW đúng); key 1027 theo JP ("Thứ đó——?") thay vì TW; key 1522 "giọt mồ hôi" chấp nhận theo ngữ cảnh 1381.
- Chi tiết đầy đủ: `audit-hachiroku-h6-wedding-REVIEW.md`; danh sách sửa: `audit-hachiroku-h6-wedding-wrong.json` (16 mục, khối TOML 16 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 16/16).

```toml
[script]
"511" = "「Hà——chụm——ư——chụt——Sou——\\nmút——tetsu——chụt——ngài——ưm!!?」"
"515" = "「Ư——A——a! A! A! A!!」"
"516" = "「Ư——A!」"
"519" = "「——ƯƯ!!」"
"775" = "「Nhưng mà, bây giờ chỉ có hai chúng ta thôi mà?\\nĐâu cần thiết phải giấu núm vú ngay cả với tôi chứ——Ư!」"
"873" = "「Ư!!」"
"1008" = "「Vì——vậy, nhiều hơn nữa——những thứ……bên trong, ngài Soutetsu\\n——vào sâu hơn nữa——tất cả——em muốn, có——Ư!?」"
"1050" = "「Làm, như thế……thì——a——em,\\nưm……phù——a——vú……vú!」"
"1080" = "「Ư!」"
"1081" = "「Ư!!」"
"1082" = "「Ư!!!!!」"
"1083" = "「Ư!!?」"
"1085" = "「~~~~ƯƯ!!!!!!!!!」"
"1557" = "Chà xát núm vú bằng phần hông của cậu bé đang cương cứng,\\ntrượt mạnh qua khe hẹp giữa chiếc váy và bầu ngực——Ư!?"
"1760" = "Suzu——đã dùng lưỡi.\\nCố gắng vươn chiếc lưỡi ngắn ngủi về phía cậu bé đang cương cứng."
"1771" = "Sâu trong cổ họng Suzu khẽ giật,\\ntoàn bộ nước bọt và hơi thở trong miệng tôi bị hút mạnh đi——Ư!?"
```

**Tổng cộng sau file này: 104 file / 4.876 dòng sai** (cơ sở 103 file / 4.860 dòng sai + 16 file này — rebase bởi parent sau khi 仲国05 gộp trước, 14 dòng)
- Parent kiểm chứng 20/11 ~16:15: JSON 16 mục dạng chuẩn, khóa chuỗi; khối TOML 16 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 16/16; diff-sanity: chèn Ư / 2 từ bịa đã bỏ (1050 "mất", 1760 "liếm lấy") / 1 tên vỡ đọc sai (511 Sou–tetsu–ngài, TW xác nhận); lượt soát 2 ghi trong review (16/16, 0 bỏ, 0 sửa). **Totals line: 104/4.876 (rebase bởi parent sau khi 仲国05 gộp trước, 14 dòng).** Chờ Hieu: fa/fu biến thể "phù a"/"phù" 14 dòng — để unification pass theo tiền lệ lr_ふかみh2; key 491 JP cụt; key 1813 JP "旧悪" lạ; key 1027 theo JP thay vì TW; key 1522 "giọt mồ hôi" theo ngữ cảnh 1381.

## 01_Hachiroku ハチロク06_それぞれの傷跡 — 24/407 (5,9%)

- File: `ハチロク06_それぞれの傷跡.txt.toml` — route 01_Hachiroku, 407 dòng script (74 thoại Hachiroku, 62 thoại Soutetsu, 39 thoại Paulette, 33 thoại Hibiki, 16 thoại Reina, 183 độc thoại). Nội dung: Hachiroku phát hiện khung gầm 8620 bị biến dạng; Soutetsu thừa nhận sợ tai nạn đường sắt, định ngừng vận hành 8620 để bảo vệ Hachiroku; hiểu lầm giữa hai người rồi được Hibiki hoà giải; kế hoạch tàu BBQ + đổi biểu đồ chạy tàu; thời hạn 2 năm từ cha của Mayami.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 407/407 (262 dòng chỉ khác ở chỗ TOML-2 làm phẳng dấu \n thành khoảng trắng). `[selections]` rỗng. Không có bản sao file này (md5 `c27fb7616a7462dcc5232456dbb9e977`).
- Phân loại (24): gasp 9 (1613, 1638, 1648, 1974, 1979, 2025, 2026, 2031, 2629 — 5 từ sweep + 2 sweep bỏ sót + 2 đính chính sweep), đại từ 8 (1770 "ngài ấy"→"ngài"; 1991 Soutetsu→Paulette "cô"→"em"; 2356, 2420, 2455, 2474, 2768, 2797 độc thoại Hachiroku "em"→"tôi"), tag 3 (1556, 1710, 1784 — VN tự thêm thẻ gloss cho 8620, JP chỉ có ruby), nghĩa 3 (1654 gỡ "Do" bịa ở câu cụt; 2350 口惜しい "hối hận"→"không cam lòng"; 2800 "run lên bần bật"→"run rẩy nhè nhẹ"), SFX 1 (2598 ぐっ bị bỏ mất).
- Sweep kiểm chứng: 7 mục cho file — nhận nguyên 5 fix (1974, 2025, 2026, 2031, 2629; 2629 chuẩn lại dấu \n theo CSV3); đính chính 1638 already-rendered ("A!!" diễn âm あ, không phải っ) và 1979 needs-file-audit (VN "Chuyện đó!" bịa từ cho một tiếng gasp); quét bổ sung bắt thêm 2 gasp sweep bỏ sót (1613, 1648 bare っ→"Ưm").
- Soutetsu "tôi" với Hachiroku đúng toàn file (0 dòng "anh" sai); độc thoại Hachiroku "tôi" ở ~30 dòng, chỉ 6 dòng lạc sang "em". Thuật ngữ chờ đợt thống nhất: "Ohimitera" 4 dòng (1710, 1819, 2706, 2710), "tuyến Yui" 2 dòng (1801, 2710).
- Chi tiết đầy đủ: `audit-hachiroku06-sorezore-kizuato-REVIEW.md`; danh sách sửa: `audit-hachiroku06-sorezore-kizuato-wrong.json` (24 mục, khối TOML 24 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 24/24; lượt soát 2: 24/24, 0 bỏ, 0 sửa).

```toml
[script]
"1556" = "「8620 đã mang lại niềm vui cho rất nhiều người đúng không?\\n\"Bản tin buồng lái 8620\" cũng đang được rất nhiều người đọc nữa.」"
"1613" = "「Ư」"
"1638" = "「Ư!!」"
"1648" = "「Ư」"
"1654" = "「Anh Soutetsu……」"
"1710" = "「Những người dân Ohimitera, những vị khách đến tham quan――\\nCó nhiều người yêu mến 8620 hơn em nghĩ đấy.」"
"1770" = "「Nếu vậy…… giá như ngài nói cho em biết ngay từ đầu.」"
"1784" = "「Đúng không? Vì là anh hai mà.\\nAnh ấy tuyệt đối sẽ không bao giờ bỏ rơi 8620 đâu.」"
"1974" = "「Hỏi han gì chứ――sợ tai nạn là chuyện đương nhiên mà――Ư!」"
"1979" = "「Ư!」"
"1991" = "「Nếu vậy thì, nhờ em tiến hành theo cách đó được không?」"
"2025" = "「Ư!!?」"
"2026" = "「Ư!?」"
"2031" = "『「――Ư!」\\n「A」』"
"2350" = "Thật vui. Thật nhẹ nhõm.\\nNhưng mà, tôi cũng cảm thấy hơi――một chút xíu thôi, hơi không cam lòng."
"2356" = "Nếu cứ tiếp tục gượng ép chạy thêm hai năm nữa, sự biến dạng sẽ không thể phục hồi,\\nvà chắc chắn sẽ phá hủy \\x%l8620;#00ffc040;8620%l;#;――phân thân của tôi mất."
"2420" = "Còn tôi――tôi thì――\\nNhưng mà, tôi chỉ là một \\x%lレイルロオド;#00ffc040;Railord%l;#; thôi mà――"
"2455" = "Nên tôi cũng muốn đáp lại, tôi đã cố gắng hết sức.\\nThế mà \\x%l8620;#00ffc040;8620%l;#; của tôi――lại trở thành gánh nặng cho ngài Soutetsu……"
"2474" = "Nếu vậy thì, tôi……\\nViệc tôi nên làm, chỉ có một thôi."
"2598" = "Không thèm lau đi vết bẩn trên đầu gối,\\nHachiroku bất chợt tiến sát lại gần tôi."
"2629" = "Nếu bám chặt vào đường ray bằng một lực mạnh, và trục bánh xe bị vặn xoắn mạnh,\\nthì đương nhiên sẽ tạo ra sức mạnh lớn, nhưng tải trọng cũng sẽ lớn theo tương ứng――Ư!"
"2768" = "Chuyện như vậy――\\nChuyện như vậy…… tôi tuyệt đối sẽ không làm."
"2797" = "Ngài Soutetsu dù biết rõ tôi bị lỗi,\\nnhưng vẫn trở thành \\x%l機関士;#00ffc040;Lái tàu%l;#; của tôi, và đã cố gắng vì tôi đến nhường nào."
"2800" = "Bàn tay ngài Soutetsu đang nắm chặt lại.\\nNắm chặt đến mức run rẩy nhè nhẹ."
```

**Tổng cộng sau file này: 105 file / 4.900 dòng sai** (cơ sở 104 file / 4.876 dòng sai + 24 file này)
- Parent kiểm chứng 20/11 ~17:00: JSON 24 mục dạng chuẩn, khóa chuỗi; khối TOML 24 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 24/24; diff-sanity: tỉ lệ thấp nhất 1979 (0,38 — VN bịa "Chuyện đó!" cho tiếng gasp trần → "Ư!"), 1638 (0,80 — "A!!"→"Ư!!", đính chính sweep), 1654 (0,86 — gỡ "Do" bịa); đại từ kiểm chứng theo thứ tự TOML (1991 Soutetsu→Paulette "em" — Paulette kề dòng + độc thoại xác nhận; 1770 "ngài" — JP dùng kính ngữ ngôi 2; cụm độc thoại Hachiroku 6 dòng "em"→"tôi", character=monologue); lượt soát 2 ghi trong review (24/24, 0 bỏ, 0 sửa). **Totals line: 105/4.900 (cơ sở 104/4.876 khớp ROUTE-AUDIT.md, không cần rebase).** Chờ Hieu: 1654 (câu cụt 「双鉄くんに……」 của Paulette — phần tiếp theo không rõ); đợt thống nhất "Ohimitera"→"Ohitoyo" và "tuyến Yui"→"tuyến Yunoi"; 1850 ("trực tiếp nghe" theo ngữ cảnh 1966 hay "trực tiếp hỏi" theo TW).

## 07_Nagi_Fukami 凪ふかみ06_凪の欲しいもの — 36/445 (8,1%)

- File: `07_Nagi_Fukami/凪ふかみ06_凪の欲しいもの.txt.toml` (445 dòng script; monologue 153, 双鉄 149, 凪 106, 真闇 37). TOML md5 11f7a6a2ef37148c3336561fce88dc9f, không có bản trùng; CSV3 1 bộ 445 dòng, key khớp tuyệt đối (1 "lệch" duy nhất là TOML làm phẳng khoảng trắng đôi ở 1844).
- Lỗi chính: đại từ Soutetsu 14 (13 tự xưng sai — 11 với Mayami → "tôi" gồm 10 "em"→"tôi" và 2030 "anh"→"tôi", 2 với Nagi → "anh" 1601/1626 — cộng 1 Nagi gọi Soutetsu "nó"→"anh" 2131); SFX 13 (5 gasp っ theo sweep đã kiểm chứng lại từng dòng — 1231, 1755, 1820, 1821, 1988; 8 đếm nguyên âm sweep bỏ sót — 1757, 1816, 1817, 1835, 1836, 1839, 2079, 2180); thuật ngữ 7 (Ohitoyo 5, Yunoi 2, thân bảo trì 1 — 2021 gộp 2 thuật ngữ); sai nghĩa/bịa 2 (2336 "Nhưng mà." bịa thêm, 2649 "chị em sinh đôi" sai giới tính).
- 0 lệch/luân chuyển, 0 dòng mồ côi, 0 chưa dịch, 0 trùng key, 0 lỗi %l (file không có thẻ %l); Nagi→Fukami "cậu ấy" đúng; 義父→"cha nuôi" hợp lệ (TW 養父, key 2505); Soutetsu "anh" với Nagi đúng suốt. Lượt soát 2: 36/36/0/0.
- Chờ Hieu (không tính sai): 2024/2169/2222 người nghe mơ hồ (Mayami vs Nagi) — giữ nguyên; 2819 "(Ấn)" cho ぐっ (gợi ý "(Gừ)"); 1759 "hauu" giữ nguyên; ruby [x,n] 15 chỗ chưa thống nhất; 2222 "Phù!" cho ぷあっ — để unification pass.
- Chi tiết đầy đủ: `audit-nagifukami06-hoshiimono-REVIEW.md`; danh sách sửa: `audit-nagifukami06-hoshiimono-wrong.json` (36 mục, khối TOML 36 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 36/36).

```toml
[script]
"1231" = "「——————ƯƯƯ!!!」"
"1259" = "「……Nếu để chuông reo thì cô ấy sẽ thức dậy mất.\\nDù là cảm biến của thân bảo trì, chắc chắn vẫn nhạy bén hơn con người.」"
"1601" = "「Không——à, đợi anh một chút.」"
"1626" = "「Tận hưởng niềm vui khi đi chơi cũng là trân trọng bản thân mà.\\nAnh đang rất tận hưởng chuyến tu học cùng Nagi và Fukami đấy.」"
"1755" = "「Ê ê ê~Ư!?」"
"1757" = "「Ủa? Không có tác dụng mấy với anh hai hả?\\nGyuuuuuu!!!」"
"1796" = "「Ái chà, có vẻ tôi đã hơi thong thả quá đà rồi.」"
"1816" = "「Hau///」"
"1817" = "「Hau.」"
"1820" = "「Ư!!」"
"1821" = "「Ư!!!!!」"
"1835" = "CHEEEEEEEEESUTOOOOOOOO!!!"
"1836" = "CHEEEEEESUTOOOOOƯƯƯ!!!"
"1839" = "「Ưm…… ưư.」"
"1853" = "「Ừm. Tôi xin phép!」"
"1859" = "「Ừm. Nằm trong khuôn khổ chuyến tu học.\\nHôm nay, tôi và Nagi sẽ đi chơi cùng nhau.」"
"1878" = "「Oa oa oa! Ngắm nhìn thị trấn Ohitoyo từ trên máy bay hả!?\\nNghe cũng vui lắm nha!!」"
"1890" = "「Lên KiHa 07, đi đến Yunoi hả anh?」"
"1897" = "「Cảm ơn chị vì bữa ăn. Rất ngon và ấm bụng.\\nVậy tôi đi đây, tôi sẽ cẩn thận.」"
"1959" = "「Chắc là vậy rồi. Dù tôi không tự nhận thức được.\\nNhưng dưới góc nhìn của chị Mayami thì sao? Tôi, có thay đổi không?」"
"1988" = "「Xin lỗi, anh tới sát giờ qu——Ư\\nKhụ! Khụ khụ!」"
"2016" = "「Đúng vậy. Giờ này,\\nở Ohitoyo chỉ có cửa hàng tiện lợi là có bán đồ ăn thức uống thôi.」"
"2018" = "「Đúng vậy. Nếu không phải chạy thay chuyến tàu đầu tiên bằng 8620,\\nthì tôi cũng chẳng dậy vào giờ này đâu.」"
"2021" = "「Đúng vậy. Chuyến 1D khởi hành lúc 05:39 sẽ đến Yunoi lúc 06:22.\\nChuyến khứ hồi 2D khởi hành lúc 06:29 sẽ đến ga suối nước nóng Ohitoyo lúc 07:16.」"
"2030" = "「Điều tôi nghĩ đến đầu tiên là những nơi như quán cà phê.\\nVừa ngắm Nagi dễ thương, vừa thong thả tận hưởng thời gian, có vẻ sẽ hạnh phúc lắm.」"
"2074" = "「Bây giờ, khác rồi.\\nTôi đang rất trân trọng bản thân mình.」"
"2076" = "「Có giờ giới nghiêm mà. Nên cũng không đến nỗi quá muộn——\\nnhưng cũng không ít lần tôi phải hớt hải đưa con bé về nhà sát nút 21:00.」"
"2079" = "「Ui da da da da da da da da!?」"
"2131" = "「Anh bảo sao!?」"
"2170" = "「Vậy thì ngại quá. Nếu mất công thì để tôi làm cho.」"
"2180" = "「Vậy em ấn nha! Gyuuuu!」"
"2182" = "「Vậy thì, chúng ta cùng làm được không.\\nTôi cũng có thể giúp được chút ít, sẵn tiện muốn xua đi cơn buồn ngủ nữa.」"
"2336" = "Từ lúc nào, những chuyến tu học thường nhật này,\\nđã hoàn toàn trở thành một phần của tôi, khiến tôi quên béng mất."
"2598" = "Không cần nghe hết câu tôi cũng gật đầu đồng ý.\\nGiờ này, ở Ohitoyo chỉ có cửa hàng tiện lợi là mở cửa thôi."
"2649" = "Là anh em sinh đôi, ngang hàng với nhau.\\nChính vì vậy, dù chỉ là một khác biệt nhỏ cũng khiến tôi phải hơn thua."
"2735" = "Ít nhất là về góc nhìn thực tế đối với du lịch Ohitoyo,\\nhiện tại có lẽ đến cả mẹ của Fukami cũng không thể sánh bằng con bé."
```

**Tổng cộng sau file này: 106 file / 4.936 dòng sai** (cơ sở 105 file / 4.900 dòng sai + 36 file này)
- Parent kiểm chứng 20/11 ~17:00: JSON 36 mục dạng chuẩn, khóa chuỗi; khối TOML 36 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 36/36; diff-sanity: tỉ lệ thấp nhất 1897 (0,82 — đổi đại từ + sửa câu 2 theo JP "tôi sẽ cẩn thận"), 2131 (0,83 — Nagi "nó"→"anh"), 1836 (0,84 — đếm nguyên âm 6E+5O+3Ư theo JP); đại từ kiểm chứng theo thứ tự TOML (1601/1626 Soutetsu→Nagi "anh" — Nagi kề dòng; 1796/2030/2170 Soutetsu→Mayami "tôi" — Mayami kề dòng, 2030 nói về Nagi ngôi 3; 2131 Nagi→Soutetsu "anh"); lượt soát 2 ghi trong review (36/36, 0 bỏ, 0 sửa). **Totals line: 106/4.936 (rebase bởi parent sau khi ハチロク06 gộp trước, 24 dòng).** Chờ Hieu: 2024/2169/2222 người nghe mơ hồ (Mayami vs Nagi); 2819 "(Ấn)" cho ぐっ; ruby [x,n] 15 chỗ; 2222 "Phù!" cho ぷあっ — để unification pass.


## れいな01 — れいな01_炭鉱探索.txt.toml — 35/403 (8,7%)

- File: `れいな01_炭鉱探索.txt.toml` — route 04_Reina, 403 dòng script (145 độc thoại, 120 thoại Soutetsu, 94 thoại Reina, 44 thoại Paulette). Nội dung: khảo sát mỏ than bỏ hoang 術仙 — Reina giảng về mỏ than (quặng pirit, axit sunfuric, celluloid, đường sắt mỏ, tàu hỗn hợp, xe goòng chở người); cảnh "chơi trò gia đình" ở ký túc xá; kết bằng việc Paulette và Reina được giải phóng khỏi chuyến chạy định kỳ.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 403/403 (266 chênh lệch đều là TOML làm phẳng `\n` thành khoảng trắng, 0 chênh lệch nội dung). `[selections]` rỗng. Không có bản sao file này (md5 `945c238f9039b7edc88998a761c5cdb8`).
- Phân loại (35): đại từ 20 (1559, 1582, 1599, 1601, 1606, 1610, 1611, 1614, 1615, 1691, 1742, 1745, 1747, 1763, 1769, 1775, 1833, 1862, 2006, 2019 — Soutetsu "tôi"→"anh" với Reina/Paulette, "cô"→"em" cho Paulette, Paulette "chị"→"em" với Soutetsu; 1742 kèm 術仙 "Jussen"→"Jutsu-sen"), SFX 7 (1538 えへへぇ "E hèm"→"Ehehe~"; 1624, 1626, 1629, 1630, 1633, 1634 うふふぅ "Ư hự hự"→"Ufufu"), gasp 1 (2035 từ sweep), sai nghĩa 4 (1580 mỏ=núi; 1643 KiHa 07 bị gọi "người"; 1663 お麩 "váng đậu"→"phù"; 2348 đảo chiều sai khiến 思い出させる), thuật ngữ 3 (1644 整備体→"thân bảo trì"; 2218 運転ボディ→"thân vận hành"; 2349 Ohimitera→Ohitoyo + Yui→Yunoi).
- Sweep kiểm chứng: 1 mục cho file (2035), áp nguyên văn; quét máy toàn bộ っ: không còn gasp nào sót.
- Soutetsu "anh" với Reina/Paulette đã nhất quán sau sửa (17 dòng "tôi" sai + 2 "cô" + 1 Paulette "chị"); độc thoại "tôi" giữ nguyên theo quy tắc chung. Paulette "tôi" ở 4 dòng công việc trang trọng (1717, 1748, 1920, 1987) giữ nguyên theo tiền lệ "tôi ở hội đồng".
- Chi tiết đầy đủ: `audit-reina01-tankou-REVIEW.md`; danh sách sửa: `audit-reina01-tankou-wrong.json` (35 mục, khối TOML 35 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 35/35; lượt soát 2: 35/35, 0 bỏ, 0 sửa; diff-sanity bắt 3 lỗi ngoặc 「」 tự thêm vào 2218/2348/2349, đã sửa trước soát 2).


```toml
"1538" = "「Oaaa, Reina vui lắm ạ. Ehehe~, anh Soutetsu,\\nnhớ cả những chuyện như vậy luôn đó hả~」"
"1559" = "「À――chuyện đó, trước đây anh cũng từng nghe nói. Nhưng mà,\\nchính vì thế nên tất cả các loại dây điện đều được cách điện nghiêm ngặt rồi mà nhỉ?」"
"1580" = "「À, ra vậy! \\nMỏ trên núi là mỏ trên núi――nghĩa là, nó chính là một ngọn núi.」"
"1582" = "「À, quả nhiên là anh làm phiền em rồi.」"
"1599" = "「Ừm. Lái thử KiHa 07 rồi anh mới hiểu rõ.\\nLý do Paulette nói 8620 phù hợp với du lịch.」"
"1601" = "「Ừ. Chắc là vì anh đã rất ngạc nhiên.\\nMột \\x%lレイルロオド;#00ffc040;Railord%l;#; nhỏ bé thế này, mà lại đi chở hàng hóa sao――」"
"1606" = "「Ừm. Trăm sự nhờ em.」"
"1610" = "「Ừ, cứ giao cho anh.」"
"1611" = "「À, anh cũng từng nghe nói. Vì thua kém về chất lượng và cạnh tranh giá cả,\\nnên các mỏ than trong nước đều bị đẩy đến bờ vực đóng cửa.」"
"1614" = "「Ừ, em sẽ cố gắng.\\nVà――anh Soutetsu.」"
"1615" = "「Ừm, anh sẽ mong đợi lắm đấy.」"
"1624" = "「Ufufu, mình đi làm vất vả rồi ạ~」"
"1626" = "「Ufufu, anh thích là Reina vui rồi ạ~」"
"1629" = "「Ufufu, kỳ lạ anh nhỉ~」"
"1630" = "「Ufufu, đúng vậy đó ạ~」"
"1633" = "「Ufufu,\\nThấy mình ăn ngon miệng thế này em vui lắm đó nha~」"
"1634" = "「Ufufu~, anh Soutetsu, rõ ràng là anh Soutetsu mà,\\nlại nói chuyện hơi kỳ lạ rồi đó ạ~?」"
"1643" = "「Cả Reina và KiHa 07 đều khỏe mạnh mà lị~」"
"1644" = "「Vì ở thân bảo trì——\\nhầu như chẳng bao giờ Reina được bế cả ạ.」"
"1663" = "「Vâng ạ, hôm nay có thịt hầm khoai tây,\\nvà súp miso nấu với hành và phù đó nha~」"
"1691" = "「À, anh có chuyện muốn hỏi.\\nMỏ than này, liệu trữ lượng than có còn không?」"
"1742" = "「Để tìm kiếm những ý tưởng cộng thêm đó,\\nanh muốn tiến hành thêm các cuộc khảo sát quanh mỏ than bỏ hoang Jutsu-sen――」"
"1745" = "「Anh hiểu mà, chính vì thế,\\nnên anh mới nhờ em dạy lái \\x%lキハ07;#00ffc040;KiHa 07%l;#; mà.」"
"1747" = "「Lái tàu và khảo sát, anh sẽ thực hiện không để xảy ra sự cố nào.\\nHơn thế nữa――chắc chắn, anh sẽ tìm ra được manh mối gì đó.」"
"1763" = "「Xin lỗi nhé, Paulette.\\nEm đang mải suy nghĩ gì à?」"
"1769" = "「Nhờ có sự dư dả thời gian, anh có thể tập trung quan sát hơn. Về tính tiện lợi,\\nđộng cơ diesel vượt xa động cơ hơi nước.」"
"1775" = "「Nếu khả năng không phải là không, thì cứ thử xem xét cũng chẳng mất gì.\\nAnh được dạy như vậy, và anh chỉ luôn làm theo như thế thôi.」"
"1833" = "「Vậy sao——cái đó là một loại nhựa dẻo mà...\\nanh cứ tưởng người ta làm từ dầu mỏ hay gì đó chứ.」"
"1862" = "「Đúng vậy. Ở quy mô lớn hơn nhiều——\\nNếu không thì, anh có cảm giác sẽ không thể nào tái hoạt động được.」"
"2006" = "「Vậy thì tốt quá rồi. Nhưng mà xin lỗi em nhé.\\nAnh đi nhanh quá phải không.」"
"2019" = "「Vậy thì, có khả năng khai thác than trở lại không?\\nÝ anh là, về mặt quyền lợi và giấy phép các thứ.」"
"2035" = "「Ư!」"
"2218" = "Đúng là, Hachiroku mà tôi vẫn thường hay bế\\nlà ở thân vận hành――tức là cơ thể cỡ búp bê."
"2348" = "Đạp lên đám cỏ dại mùa hè, tôi gợi cho đường ray cũ đã hoàn toàn bị vùi lấp nhớ lại vai trò của nó."
"2349" = "Tuyến đường sắt của chúng tôi bị cô lập chỉ giữa Ohitoyo và Yunoi,\\ncứ như thể là biểu tượng cho kênh phân phối của chúng tôi vậy."
```

**Tổng cộng sau file này: 107 file / 4.971 dòng sai** (cơ sở 106 file / 4.936 dòng sai + 35 file này)

- Chờ Hieu: 2415 (ô JP chứa tiếng Việt "Bước đi xạo xạc." + TW sao nhầm của 1917 — dữ liệu gốc hỏng ở cả CSV3 lẫn TOML, JP thật không rõ, không sửa được); 2348 + 1804 (TW sao nhầm của dòng khác, đã lấy JP làm chuẩn — chỉ ghi nhận, không cần quyết).
- Parent kiểm chứng 20/11 ~17:15: JSON 35 mục dạng chuẩn, khóa chuỗi; khối TOML 35 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 35/35; diff-sanity: tỉ lệ thấp nhất 1629/1630 (0,75 — cười うふふぅ "Ư hự hự"→"Ufufu", chỉ đổi phần SFX), 1644 (0,83 — thuật ngữ 整備体), 2218 (0,85 — thuật ngữ 運転ボディ); đại từ kiểm chứng theo review §2 (1742 Soutetsu→Paulette "anh" — Paulette nhận việc ở 1748; 1769/1775 Soutetsu→Reina "anh"; 2019 Soutetsu→Paulette "anh"); lượt soát 2 ghi trong review (35/35, 0 bỏ, 0 sửa). **Totals line: 107/4.971 (cơ sở 106/4.936, khớp ROUTE-AUDIT.md — không cần rebase).** Chờ Hieu: 2415 (ô JP chứa tiếng Việt, dữ liệu gốc hỏng ở cả CSV3 lẫn TOML — không sửa được); 2348 + 1804 (TW sao nhầm, đã lấy JP làm chuẩn).


## れいなh1 — れいなh1_おかあさんのレッスン.txt.toml — 38/402 (9,5%)

- File: `れいなh1_おかあさんのレッスン.txt.toml` — route 04_Reina, 402 dòng script (93 thoại Reina, 55 thoại Soutetsu, 51 thoại Paulette, 203 độc thoại). Nội dung: H-scene "Bài học của mẹ" — Paulette đóng vai mẹ dạy Reina làm tình với Soutetsu (Reina học oral và giao hợp lần đầu, Paulette làm mẫu rồi tự tham gia để khép lại mối tình đầu không thành và trở thành mẹ của Reina); Soutetsu nhận ra "tiếng nói của cơ thể"; kết bằng cảnh cả ba trở thành một gia đình.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 402/402 (238 dòng chỉ khác ở chỗ TOML-2 làm phẳng \n). `[selections]` rỗng. Không có thẻ `%l` nào trong file. Không có bản sao file này (md5 `09eaed303cc160ad7b01033ad81f8c51`).
- Phân loại (38): xưng hô 11 (Soutetsu "tôi"→"anh" 7: 1210, 1248, 1390, 1405, 1451, 1455, 1481; Paulette "tôi"→"chị" 1: 1416, "chị"→"em" 2: 1448, 1453; độc thoại "Chị Paulette"→"Paulette" 1: 2066), gasp 5 (1323, 1346, 1348, 1349, 1574 — cả 5 từ sweep), tiếng cười 2 (1401, 2134 — うふふ→"Ufufu"), fa/fu 17 (1233, 1266, 1278, 1284, 1336, 1337, 1344, 1350, 1355, 1526, 1527, 1529, 1530, 1532, 1533, 1535, 1537), đếm nguyên âm 2 (1264, 1374), sai nghĩa 1 (2065 rò chữ "備"→"chuẩn bị").
- Sweep kiểm chứng: 7 mục cho file, nhận 5 fix + 2 already-rendered đúng (1373, 1375); sweep bỏ sót 0 gasp (quét máy toàn bộ JP).
- Chi tiết đầy đủ: `audit-reinah1-okaasan-REVIEW.md`; danh sách sửa: `audit-reinah1-okaasan-wrong.json` (38 mục, khối TOML 38 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 38/38; lượt soát 2: 38/38, 0 bỏ, 1 sửa 1264).


```toml
[script]
"1210" = "「Không, chính anh cũng muốn nhờ em.」"
"1233" = "「Làm tình……làm tình——ưm——Reina——đã đàng hoàng,\\nlàm với anh, Soutetsu……ưm——a——phù——a」"
"1248" = "「Là cái này sao? Sự bồn chồn mà anh đang cảm thấy,\\nReina cũng bị nó ám ảnh sao?」"
"1264" = "「Hya!? A――a――a――\\nPhù aaaaaaaaaaaaan!!!」"
"1266" = "「Hya!? A――c-cái gì――thế này――\\nphuê――Reina――Reina――sao ấy――」"
"1278" = "「Phuê!?」"
"1284" = "「Phà……a……tuyệt quá……tuyệt quá……ạ~」"
"1323" = "「Ư!!」"
"1336" = "「Phùaaaaaa!!?」"
"1337" = "「Hya——a!」"
"1344" = "「Ưm! Phùaa——a——hi, ưm——\\nChỗ đó——Reina——phù, a——bị cọ xát, thế này——」"
"1346" = "「Ư!」"
"1348" = "「Ư!!?」"
"1349" = "「Ư!?」"
"1350" = "「A……phà――a.」"
"1355" = "「Hyau!? Phuê.」"
"1374" = "「Kyuuuuuuuuuuuuuu!!!!」"
"1390" = "「À, có. Một từ mà anh rất thích.」"
"1401" = "「Ufufu, lần này, đến lượt hoàn thành việc chuẩn bị cho Reina nhỉ.」"
"1405" = "「Anh đã không lắng nghe tiếng nói của cơ thể mình một cách đàng hoàng sao.」"
"1416" = "「Chị hiểu rồi. Vậy thì――\\nReina, qua đây nào?」"
"1448" = "「Làm mẫu. Em, muốn cho Reina xem.\\nChỉ một lần, chỉ một lần duy nhất thôi, làm mẫu cho em ấy.」"
"1451" = "「Anh cũng vậy. Anh rất tôn trọng Paulette,\\nvà tin tưởng em.」"
"1453" = "「Em thì…… cũng được thôi――nhưng mà……\\nNếu anh Soutetsu――không thấy phiền.」"
"1455" = "「Anh cởi rồi――nhưng mà.」"
"1481" = "「Nếu vậy Paulette. Xin hãy chỉ cho anh với.\\nLàm thế nào để nghe được tiếng nói của cơ thể.」"
"1526" = "「Phuê――không được――dừng――lại――ưm――\\nReina……sẽ làm bẩn……căn phòng mất――ư――」"
"1527" = "「Hya——ưm——hya——a——\\nAnh——Soutetsu——anh——Soutetsu~」"
"1529" = "「Phà……a――đang……nuốt……ưm――phù.」"
"1530" = "「Phù——a——a——a……」"
"1532" = "「Phà……a——a!?」"
"1533" = "「Phùa——a! A! A a」"
"1535" = "「Ha……đau……quá……ưm——phà……\\nReina……đang làm tình……với anh Soutetsu……rồi」"
"1537" = "「Ư——phù——phù——phùù」"
"1574" = "「~~~~Ư!」"
"2065" = "Để được chỉ dạy điều đó, cần phải có sự chuẩn bị."
"2066" = "Paulette còn dạy cả những chuyện như thế này sao."
"2134" = "Chứng kiến cảnh đó,\\nReina nở một nụ cười hạnh phúc \"Ufufu\"."
```

**Tổng cộng sau file này: 108 file / 5.009 dòng sai** (cơ sở 107 file / 4.971 dòng sai + 38 file này)
- Chờ Hieu: 4 dòng Paulette "tôi" mơ hồ người nghe (1352, 1421, 1423, 1447 — không đưa vào TOML); 2 dòng ngọng phiên âm (1282, 1341); mâu thuẫn ひあ/ひゃ ("Hya" vs "Hia" vs "Á"); "Kua" vs "Hự" (1272/1322); じゅるむっ (1341); みち dài (2324); số lượng t kéo dài; "Hinomoto" vs "Hinamoto" (1408); mâu thuẫn fa/fu toàn dự án.
- Parent kiểm chứng 20/11 ~17:20: JSON 38 mục dạng chuẩn, khóa chuỗi; khối TOML 38 khóa (bảng [script]), 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 38/38; diff-sanity: tỉ lệ thấp nhất 1278 (0,67 — token SFX ngắn ふぇっ "Fue"→"Phuê"), 1337 (0,75 — ひあっ "Á"→"Hya", theo tiền lệ h3, mâu thuẫn ひあ/ひゃ đã cờ cho Hieu), 1336 (0,79 — ふああああああっ→"Phùaaaaaa"); đại từ kiểm chứng theo review §2 + dòng kề (1210/1451/1455 Soutetsu→Reina/Paulette "anh"; 1416 Paulette→Reina "chị"; 1448/1453 Paulette→Soutetsu "em"; 2066 độc thoại "Chị Paulette"→"Paulette"); lượt soát 2 ghi trong review (38/38, 0 bỏ, 1 sửa 1264). **Totals line: 108/5.009 — REBASE bởi parent: base của agent 106/4.936 đã cũ (viết trước khi れいな01 gộp xong); cơ sở đúng 107/4.971 + 38.** Chờ Hieu: 4 dòng Paulette "tôi" mơ hồ người nghe (1352/1421/1423/1447, không đưa vào TOML); mâu thuẫn ひあ/ひゃ; "Kua" vs "Hự"; mâu thuẫn fa/fu "phùa" vs "phù" toàn dự án.

## lrれいな追加02 — lrれいな追加02_花嫁修業の先生たち.txt.toml — 16/384 (4,2%)

- File: `lrれいな追加02_花嫁修業の先生たち.txt.toml` — route 04_Reina, 384 dòng script (110 độc thoại, 92 thoại Reina, 56 thoại Soutetsu, 45 Kisaki, 43 Hibiki, 38 Mayami). Nội dung: buổi học "làm cô dâu" — Mayami dạy nấu ăn, Kisaki dạy trà đạo, Hibiki dạy cắm hoa; Soutetsu + Reina là học viên.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 384/384 (238 chênh lệch chỉ là `\n`→khoảng trắng đã biết). `[selections]` rỗng. Không có thẻ `%l` nào trong file. Không có bản sao file này (md5 `d620b749cf8ff3d0db532c2b68a22295`).
- Phân loại (16): đại từ 5 (1187, 1357, 1405, 1456, 1692), SFX tiếng cười 6 (1263, 1265, 1266, 1376, 1511, 2017 — うふふ→"Ư hư hư" sai quy tắc 22:05, sửa thành "Ufufu"/"ufufu"), gasp 3 từ sweep (1339, 1363, 1885 — nhận nguyên văn), fa/fu 1 (1274 ふああっ→"Phùa a."), SFX/discourse 1 (1655 っと→"Rồi").
- Sweep kiểm chứng: 3 mục cho file, nhận cả 3; quét máy bổ sung không bắt thêm gasp.
- Chi tiết đầy đủ: `audit-lr-reina-tsuika02-REVIEW.md`; danh sách sửa: `audit-lr-reina-tsuika02-wrong.json` (16 mục, khối TOML 16 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 16/16; lượt soát 2: 16/16, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 109 file / 5.025 dòng sai** (cơ sở 108 file / 5.009 dòng sai + 16 file này)

- Chờ Hieu: 1505 + 1637 (đại từ Soutetsu mơ hồ người nghe, giữ nguyên); Kisaki ボク với Soutetsu "tôi" hay "em" (tiền lệ h1 có phải chỉ đúng trong bối cảnh riêng?); mâu thuẫn fa/fu toàn dự án.

```toml
[script]
"1187" = "「Không, cô đừng khiêm tốn như vậy.」"
"1263" = "「Ufufu~」"
"1265" = "「Ufufu~.\\nThấy chị vui, Reina cũng vui lắ-ắm luôn nha~」"
"1266" = "「Ufufu, vậy thì còn gì bằng nữa.」"
"1274" = "「Phùa a.」"
"1339" = "「Ừm. ——Ư!」"
"1357" = "「À, ừm. Tất nhiên rồi.\\nCó vẻ thú vị đấy. Tôi cũng rất hứng thú.」"
"1363" = "「Hửm?——Ư!!!!!!」"
"1376" = "「Ufufu~, đúng vậy nha~. Cả cô Kisaki và chị Hibiki,\\nđều đã dạy cho Reina và anh Soutetsu rất nhiều điều nha~」"
"1405" = "「Nếu chị Mayami cũng không phiền. Hai người đã nói chuyện gì vậy,\\ncó thể cho tôi nghe cùng được không.」"
"1456" = "「Tôi không hề biết……Thay vì tăng lượng muối, chị lại làm cho vị đậm đà hơn,\\nthấm hơn……Chị đã tốn bao nhiêu công sức để làm điều đó——」"
"1511" = "「Thế này đúng không ạ~. ——Ufufu~,\\ntrông giống bàn tay mèo thật đó nha~」"
"1655" = "「Hoàn toàn chính xác! ——Rồi」"
"1692" = "「Thông qua nghệ thuật cắm hoa để thiết kế chính cuộc sống của mình——\\nAnh có cảm giác mình đã học được tầm quan trọng của việc lựa chọn và sắp xếp.」"
"1885" = "Làm theo chỉ thị dời chiếc bàn trà hình tam giác và sofa đi,\\nKisaki liền nhanh nhẹn trong khoảng thời gian đó——Ư!"
"2017" = "Khoảnh khắc chị Mayami thì thầm điều gì đó,\\nReina bật cười khúc khích ufufu."
```
- Parent kiểm chứng 20/11 ~17:40: JSON 16 mục dạng chuẩn, khóa chuỗi; khối TOML 16 khóa (snippet + review), 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 16/16; diff-sanity thấp nhất 1263 (0,33 — SFX ngắn うふふぅ), còn lại ≥0,82; đại từ kiểm chứng theo dòng kề (1187 Kisaki 1183, 1357 Kisaki 1351/1355, 1405 Mayami, 1456 Mayami, 1692 Hibiki ikebana); lượt soát 2 ghi trong review (16/16, 0 bỏ, 0 sửa).

## 稀咲01 — 稀咲01_金と人.txt.toml — 178/379 (47,0%)

- File: `稀咲01_金と人.txt.toml` — route 06_Kisaki, 379 dòng script (93 thoại Kisaki, 84 thoại Soutetsu, 30 thoại Hibiki, 29 thoại Mototada, 1 thoại Uragami, 142 độc thoại). Nội dung: Mototada đến chi nhánh của Kisaki; tranh luận tiền bạc/niềm tin, mời gọi nhà máy Aircra vs phục hưng Ohito, nghiệp vụ đối chiếu sổ sách (cửu khứ pháp, vụ lệch 820/280 yên), ăn pizza; kết bằng lời hứa cạnh tranh công bằng.
- Chuỗi xoay lớn: 173 dòng lệch vị trí (165 fix lấy lại bản dịch đúng trong file + 8 dịch mới), đại từ 3 (1612, 1757, 1805 — Kisaki "chị"→"em" với Soutetsu), gasp 2 (1618, 2063 — 「っ！」→"Ư!"). Mồ côi 0, nhiễm chéo 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 379/379. `[selections]` rỗng. Không có bản sao file này (md5 `9701d0e61e823e0ed70f50888d83dc7a`).
- Phân loại (178): lệch dòng 173 (chuỗi xoay, dài nhất 21 mắt xích), đại từ 3, gasp 2 (cả 2 từ sweep: 1618 already-rendered + 2063 needs-file-audit — thực chất đều là lệch dòng, đã xử lý).
- Soutetsu "tôi" với Kisaki đúng toàn file; Kisaki "em" với Soutetsu (3 dòng "chị" đã sửa). Thuật ngữ: エアクラ="Aircra" đúng; 日ノ本 "Hinomoto" đang chờ Hieu chốt.
- Chi tiết đầy đủ: `audit-kisaki01-kane-to-hito-REVIEW.md`; danh sách sửa: `audit-kisaki01-kane-to-hito-wrong.json` (178 mục, khối TOML 178 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 178/178; lượt soát 2: 178/178, 0 bỏ, 0 sửa — lượt 2 bắt thêm 1 dòng đọc sót 2057).

**Tổng cộng sau file này: 110 file / 5.203 dòng sai** (cơ sở 109 file / 5.025 dòng sai + 178 file này)

- Chờ Hieu: 1637 "Hừm." vs "Hừ." (ふん); 1983 "Đó là――" vs "Chuyện đó――"; 1702 Kisaki "tôi" vs "cháu" với Mototada; 2190 "phũ phàng" (bản dịch hơi phóng); 日ノ本 "Hinomoto" vs "Hinamoto".
- Parent kiểm chứng 20/11 ~17:40: JSON 178 mục dạng chuẩn, khóa chuỗi; khối TOML 178 khóa (review; snippet không có khối TOML), 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 178/178; 165 fix lệch dòng khớp nguyên văn VN của khóa nguồn trong CSV3, 0 trùng nguồn, mọi nguồn đều là dòng sai; 8 dịch mới + 3 đại từ + 2 gasp soát nghĩa trực tiếp vs JP (mẫu 8/8 lệch dòng khớp nghĩa JP); đại từ Kisaki "chị"→"em" với Soutetsu kiểm chứng theo dòng kề (1612 sau Soutetsu 1611, 1757 sau Soutetsu 1753, 1805 trước Soutetsu 1810); lượt soát 2 ghi trong review (178/178, 0 bỏ, 0 sửa — bắt thêm 2057). **Totals line: 110/5.203 — REBASE bởi parent: base của agent 108/5.009 đã cũ (viết trước khi lrれいな追加02 gộp xong); cơ sở đúng 109/5.025 + 178.**

## 仲国01 — 仲国01_副丘→北琴.txt.toml — 22/349 (6,3%)

- File: `仲国01_副丘→北琴.txt.toml` — route 10_Chikuni, 349 dòng script (độc thoại 128, thoại Soutetsu 85, Hachiroku 76, Hibiki 52, CA 6, loa phát thanh 2). Nội dung: chuyến bay 248 của Hãng hàng không Quốc tế Trung Quốc từ Fukuoka (Phụ Khâu) đến Bắc Cầm: Soutetsu, Hibiki và Hachiroku lần đầu ra nước ngoài — điền thẻ nhập cảnh, đăng ký dấu vân tay, bữa ăn trên máy bay (Hachiroku được phục vụ than antraxit), bàn về vai trò của mỗi người trong chuyến khảo sát "Nine Stars phiên bản Trung Quốc".
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 349/349 (sau chuẩn hoá \n). `[selections]` rỗng. Không có bản sao file này (md5 `ecae81ef3a0b3b46296df859a3c01807`).
- Phân loại (22): đại từ 6 (1356, 1744, 1943, 1999, 2162, 2173 — Soutetsu "anh"→"tôi" với Hachiroku; 1356 là số nhiều "các em"), thuật ngữ 7 (2013 Ohimitera→Ohitoyo; 1706, 2113 タブレット gloss "thẻ bảng"→"máy tính bảng"; 1790, 2035, 2091 定期券 "vé tháng"→"vé định kỳ"; 2085 整備体 gloss "thân chính"→"thân bảo trì"), dịch sai 5 (1329, 1403, 1834, 1888, 2137), gasp 2 (1776, 1803 — はうっ→"HaƯ"), SFX 1 (2207 — tiếng nhai than ばりっ/ぼりっ/ごりっ/がりっ), dấu câu 1 (2407 — bỏ 「」 thừa ở độc thoại).
- Sweep kiểm chứng: 0 mục cho file này trong `sweep-raw-gasp-wrong.json` (sweep có mục cho các file Chikuni khác 仲国02/04/05/07); cả 2 fix gasp đều là sweep bỏ sót. Không còn っ thô trong VN.
- Soutetsu "anh" đúng với Hibiki và khi nói với cả nhóm (1400, 1704, 1838, 1846, 2110); 6 dòng "anh" sai vì địa chỉ chỉ có Hachiroku — đã sửa thành "tôi" (địa chỉ kiểm chứng theo dòng kề: 1744 sau Hachiroku 1743; 1943/1999/2162/2173 JP gọi đích danh Hachiroku/お前).
- Chi tiết đầy đủ: `audit-chukuni01-fukyuu-kita-koto-REVIEW.md`; danh sách sửa: `audit-chukuni01-fukyuu-kita-koto-wrong.json` (22 mục, khối TOML 22 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 22/22; lượt soát 2: 22/22, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 111 file / 5.225 dòng sai** (cơ sở 110 file / 5.203 dòng sai + 22 file này)

- Chờ Hieu: 日ノ本 "Hinomoto" vs "Hinamoto" (toàn file dùng "Hinomoto"); 2011 運転体 "thân lái" vs dạng chủ đạo "kíp lái" (chưa có thuật ngữ đã chốt); Hachiroku→Hibiki "chị" (1377) vs "cô" (file 06); 橙汁 "Trừng trấp" (1828, 2089) vs "nước cam".

## lrれいな追加h — lrれいな追加h_夜の花嫁修業.txt.toml — 33/365 (9,0%)

- File: `lrれいな追加h_夜の花嫁修業.txt.toml` — route 04_Reina, 365 dòng script (165 độc thoại, 111 thoại Reina, 89 thoại Soutetsu). Nội dung: Reina trình diễn "khóa học làm dâu bí mật" do Paulette hướng dẫn (gel bôi trơn, kích thích lỗ hậu, tư thế cún, "thêm một ngón nữa", mười lần), xen kẽ độc thoại Soutetsu về cảm giác mới lạ và sự đồng thuận "trò nào cũng thử, không hợp thì dừng".
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 365/365 (chênh lệch chỉ là `\n`→khoảng trắng đã biết). `[selections]` rỗng. Không có thẻ `%l` nào trong file. Không có bản sao file này (md5 `b6d6a52b2213d8bc98351a0f14d5ae91`).
- Phân loại (33): gasp っ 19 (10 từ sweep — 727, 1233, 1321, 1331, 1332, 1335, 1337, 1475, 1572, 1923 — nhận nguyên văn; 9 sweep bỏ sót — 723, 1060, 1075, 1092, 1122, 1126, 1132, 1175, 1942 — っ cuối tuyệt đối/đầu dòng theo tiền lệ 仲国05 1956/2254 + 1946), tiếng cười diễn thành tiếng rên 5 (1056, 1059, 1185, 1186, 1251 — うふふ/んふふ→"Ư hư hư" sai quy tắc 22:05, sửa thành "Ufufu"/"Nfufu"), sai nghĩa 3 (1007 bịa "tắm rửa sạch sẽ"; 1135 "nhanh hơn, nữa đi" sai nghĩa TW "không làm sớm hơn" + cười thành rên; 1163 ひょっ→"hihi" sai — tiếng nhún người, không phải cười), độ dài nguyên âm SFX 6 (1063, 1077, 1117, 1133, 1157, 1189 — theo quy tắc đã chốt: số nguyên âm VN = 1 + số う/ぅ trong token JP).
- Đại từ đúng toàn file: Soutetsu "anh" 12/12 dòng có đại từ, 0 lần "tôi" trong thoại; Reina gọi "anh Soutetsu" nhất quán.
- Chi tiết đầy đủ: `audit-lr-reinah-yoru-no-hanayome-shugyou-REVIEW.md`; danh sách sửa: `audit-lr-reinah-yoru-no-hanayome-shugyou-wrong.json` (33 mục, khối TOML 33 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 33/33; lượt soát 2: 33/33, 0 bỏ, 1 sửa — 1135 khôi phục 2 dấu gạch ngang bị mất).

**Tổng cộng sau file này: 112 file / 5.258 dòng sai** (cơ sở 111 file / 5.225 dòng sai + 33 file này)

- REBASE: base được giao lúc spawn là 110 file / 5.203 dòng sai đã cũ — trong lúc audit, file 仲国01 đã gộp xong (+22) nên ROUTE-AUDIT.md hiện kết ở 111/5.225; snippet dùng cơ sở này (đã kiểm chứng trực tiếp với ROUTE-AUDIT.md).
- Chờ Hieu: thống nhất fa/fu (~40 dòng "Phu a" cho ふぁ/ふあ/ぷあ trong file — chờ đợt thống nhất, cùng ハチロクh6 + lr_ふかみh2); mâu thuẫn ひあ/ひゃ toàn dự án ("Hya" vs "Hia" vs "Á"); ranh giới quy tắc gasp giữa dòng (chỉ thêm Ư cho っ cuối tuyệt đối/đầu dòng — nếu muốn "không để mất âm" tuyệt đối thì còn ~50 dòng nữa trong file này); 1163 ひょっ→"hự" vs "hây".

```toml
[script]
"723" = "「——Hự——ưm——aƯ」"
"727" = "「——Ư!!!!!」"
"1007" = "「Anh Soutetsu không có bẩn đâu nha~\\nTrên người anh thì có chỗ nào bẩn đâu nha~」"
"1056" = "「Ufufu~, tiếp theo là~——ưm……\\nChụt——chụt——chụt——liếm」"
"1059" = "「Ufufu~. Sau đó thì, để không bị bẩn nha~」"
"1060" = "「Phù——a——a——ư aƯ」"
"1063" = "「Phù, kyu u u u u u u u!!」"
"1075" = "「Phu a a a a a a anƯƯƯ」"
"1077" = "「Phu a a a a a anƯƯƯƯ」"
"1092" = "「ƯHyu a!!? Sục vào! Đâm phập vào!!\\nNóng quá! Nóng quá ập vào một lúc! Bên trong Reina」"
"1117" = "「Kua……a——a——a a a……」"
"1122" = "「A a a a aƯ」"
"1126" = "「A——a——aƯ」"
"1132" = "「A a aƯ」"
"1133" = "「Hyu a a a a a a a a a a a a a a a a a an!!」"
"1135" = "「Hà a a an! A——chuyện sướng——thế này, sao——không làm sớm hơn————NfufuuƯƯ」"
"1157" = "「Ưm u u u u u u——anh Soutetsu, anh Soutetsu,\\nnữa đi——nữa đi~——nè, anh Soutetsu ơi~」"
"1163" = "「Ưm, hự.」"
"1175" = "「Ư aƯ」"
"1185" = "「Ufufu~. Ừm thì nha~, cô ấy bảo là hai người cùng nhau\\ntận hưởng những trò chơi kỳ quái, thì tình cảm vợ chồng sẽ càng thêm gắn kết nha~」"
"1186" = "「Nfufu~」"
"1189" = "「Hi kyu u u u u u u u u u u u u u u u u u n!!」"
"1233" = "「Khóa học, làm dâu, của——Ư——thành quả——hơn cả mong đợi,\\ntuyệt vời, quá——. Ưm!」"
"1251" = "「Chị Paulette bảo là \\\"Cả con trai và con gái đều có thể sướng ở đây\\\".\\nUfufu~, anh Soutetsu cũng giống vậy nhỉ.」"
"1321" = "「Nếu vậy thì——nhiều hơn nữa——Ư!」"
"1331" = "「Ư!!!」"
"1332" = "「Ư!!!! ——A hự!」"
"1335" = "「~~~~~ƯƯƯ」"
"1337" = "「~~~~~~~~Ư!!!」"
"1475" = "Ư!"
"1572" = "Tôi không hề nhận ra. Reina đang dùng tay bao lấy quy đầu,\\nvà hứng lấy toàn bộ tinh dịch——Ư!?"
"1923" = "（Là do lỗ hậu đang bị kích thích sao……Ư——\\nMột kích thích đơn thuần lên dương vật thôi mà lại mạnh gấp mấy lần bình thường——）"
"1942" = "（Phụt——phụt——phụt——phù——phùƯ）"
```

## 凪ふかみ01 — 凪ふかみ01_凪の成長、ふかみの成長.txt.toml — 33/347 (9,5%)

- File: `凪ふかみ01_凪の成長、ふかみの成長.txt.toml` — route 07_Nagi_Fukami, 347 dòng script (78 thoại Nagi, 64 thoại Soutetsu, 49 thoại Fukami, 20 thoại Hachiroku, 8 thoại Paulette, 4 thoại Reina, 124 độc thoại Nagi). Nội dung: Nagi xin dự Đại hội Rèn luyện kiếm đạo — Hachiroku kiểm tra kỹ thuật xúc than của Nagi trên 8620; Fukami đợi ở ga với lời nhắn của sư phụ Nagi; cả nhóm bàn về triết lý đầu máy của Minh Quốc (tuổi thọ 10 năm, sản xuất hàng loạt) đối lập với Hinomoto/Đức (30–100 năm); Soutetsu chạy đi xin chữ ký hiệu trưởng và ông Minokasa để kịp nộp đơn; cuối file sư phụ cho phép Nagi dự giải.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 347/347 (208 dòng chỉ khác ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng). `[selections]` rỗng. Thẻ `%l` JP vs VN bằng nhau ở mọi dòng, 0 lệch. Không có bản sao file này (md5 `e6e70075e3d125fe3c9b1191aebf5104`).
- Phân loại (33): terminology 22 (冥国→"Minh Quốc" 13 dòng: 1511, 1587, 1593, 1664, 1698, 1708, 1777, 1792, 1796, 1914, 1950, 1955, 1965; 凪さま→"Bổn tiểu thư" 8 dòng: 1485, 1571, 1685, 1708, 1839, 1886, 2347, 2452; 御一夜→"Ohitoyo" 1: 1968; "Kiha 07S"→"KiHa 07S" 2: 1673, 1688), pronoun 6 (độc thoại Nagi "em"→"mình": 2155, 2216, 2227, 2288, 2389, 2431), gasp 2 (1620, 2452 — cả 2 từ sweep), mistranslation 2 (1630 "Tin diu?"→"Tin vui?", 1979 "Dòng lọi"→"Vòng loại"), sfx 1 (1589 ふぁっ "Oa."→"Phà.").
- Sweep kiểm chứng: 2 mục cho file (1620, 2452), áp nguyên cả 2 sau khi kiểm chứng JP; tự quét toàn bộ っ không phát hiện gasp nào sweep bỏ sót.
- Soutetsu "anh" với Nagi/Fukami/Paulette/Reina đúng toàn file; "tôi" chỉ 2 dòng, cả 2 đều nói với Hachiroku (1776, 1964 — đúng). Nagi gọi Fukami "cậu" (7 lần), không có "chị" cho Fukami. 湯医→"Yunoi" 3/3, 帝鉄→"Teitetsu" 1/1, エアクラ→"Aircra" 2/2 đúng sẵn.
- Chi tiết đầy đủ: `audit-nagifukami01-REVIEW.md`; danh sách sửa: `audit-nagifukami01-wrong.json` (33 mục, khối TOML 33 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 33/33; lượt soát 2: 33/33, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 113 file / 5.291 dòng sai** (cơ sở 112 file / 5.258 dòng sai + 33 file này)

- Chờ Hieu: 日ノ本 "Hinomoto" vs "Hinamoto" (9 dòng: 1209, 1585, 1587, 1664, 1698, 1795, 1816, 1955, 1965); 1884 じーちゃん→"Ông nội" (câu hỏi ông nội vs ông ngoại toàn dự án); 1955 Soutetsu "Anh cảm giác..." — người nghe mơ hồ (Hachiroku hay cả nhóm); 1517 Nagi tự xưng "em" với Fukami (1 lần, có thống nhất về "tớ"/"mình" không). Ghi chú: một review cũ từng ghi "冥国=Mỹ" nhưng quyết định 19/11 là "Minh Quốc" và file này đã có sẵn 1 dòng "Minh Quốc" đúng (2394) — đã sửa theo brief.

```toml
[script]
"1485" = "「Không cần đổi đâu á! Bổn tiểu thư một mình làm được á!!」"
"1511" = "「『10 năm sau có thể tạo ra những thứ tốt hơn bằng công nghệ và vật liệu mới』.\\nVì vậy, người Minh Quốc không thích sử dụng một món đồ quá lâu ạ.」"
"1571" = "「Chỉ là sư phụ không cho phép thôi!\\nVới Bổn tiểu thư thì vô địch toàn quốc cũng không phải là giấc mơ đâu nha!」"
"1587" = "「Em nhớ là, đầu máy hơi nước đã có ở Anh, Minh Quốc và Đức\\ntừ rất lâu trước cả Hinomoto rồi phải không?」"
"1589" = "「Phà.」"
"1593" = "「Fufufu, đúng thật.\\nPhong cách của Minh Quốc có vẻ rất hợp với Nagi nhỉ.」"
"1620" = "「Ư!!!」"
"1630" = "「Tin vui?」"
"1664" = "「A! Đúng rồi, thông số kỹ thuật là do phía Hinomoto đặt hàng mà.\\nNếu vậy, chúng ta có thể sử dụng sức mạnh công nghiệp của Minh Quốc theo ý tưởng của Hinomoto.」"
"1673" = "「Ở trên \\x%lキハ07s;#00ffc040;KiHa 07S%l;#;.\\nCô ấy nói là đi lên núi tu luyện hay gì đó.」"
"1685" = "「Tuyệt đỉnh của anh hai!\\nBổn tiểu thư sẽ——hỗ trợ——cho á! Nhé!!」"
"1688" = "「Tuyệt quá! \\nVậy cậu đến đây bằng chuyến \\x%lキハ07s;#00ffc040;KiHa 07S%l;#; đầu tiên vào buổi sáng hả?」"
"1698" = "「Ở Minh Quốc, cách suy nghĩ về đồ vật hoàn toàn khác biệt ạ.\\nỞ Hinomoto hay Đức, người ta thường tính đến việc sử dụng trong 30 năm tới,」"
"1708" = "「Ngầu quá đi! Công nghệ cao nha!!\\nBổn tiểu thư thích cách suy nghĩ của nước Minh Quốc rồi đó!!」"
"1777" = "「Cách suy nghĩ đó khá hợp lý đấy.\\nNước Minh Quốc mà tôi nghe kể, có vẻ đúng là một quốc gia như vậy.」"
"1792" = "「Vậy là, ở Minh Quốc,\\ncó khi không còn lại đầu máy hơi nước nào nữa sao??」"
"1796" = "「Suy luận tuyệt vời lắm, Nagi.\\nCách suy nghĩ kiểu Minh Quốc, có vẻ thực sự rất hợp với em nhỉ.」"
"1839" = "「Bổn tiểu thư——\\nBổn tiểu thư, sắp được làm lái tàu rồi sao!!?」"
"1886" = "「Bây giờ Bổn tiểu thư xúc than dồn toa!\\nCòn giỏi hơn cả anh hai nữa á!!」"
"1914" = "「Còn ở Minh Quốc, họ cho rằng tuổi thọ 10 năm là đủ rồi ạ.」"
"1950" = "「Tình hình bên đó thì……thế nào nhỉ.\\nMinh Quốc cũng là nơi khởi nguồn của Aircra mà——Hachiroku?」"
"1955" = "「Anh cảm giác những toa xe được chế tạo theo kiểu Minh Quốc sẽ không bán được ra nước ngoài.\\nNhưng thực tế, ở Hinomoto cũng có rất nhiều \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; nhập khẩu từ Minh Quốc đúng không?」"
"1965" = "「Vậy thì, ở Minh Quốc chắc chắn phải có nhiều đầu máy hơi nước\\nhơn Hinomoto rất nhiều đúng không?」"
"1968" = "「Nhờ có 8620……và đoàn tàu BBQ.\\nOhitoyo đã thực sự lấy lại được sức sống rồi.」"
"1979" = "「Vòng loại……là sao——Vòng loại gì cơ???」"
"2155" = "2 phút 60 xẻng. Với nhịp độ thường ngày ngay sau khi xuất phát,\\nmình đang xúc than dồn toa rất chuẩn xác nhưng——"
"2216" = "Mình cũng phối hợp bỏ xẻng xuống, mở thiết bị thổi gió để thông gió.\\nNước ừng ực! Cho lò hơi nãy giờ đang cố gắng uống nước á."
"2227" = "Mình biết mà, thế nên lại càng hừng hực khí thế hơn.\\nMình nhất định sẽ thi đậu."
"2288" = "Thình thịch, ngực mình đập rộn ràng.\\nĐược anh tin tưởng mình vui lắm á! Cảm thấy tràn đầy năng lượng luôn!!"
"2347" = "Bổn tiểu thư, à không, mình——tớ, cũng vậy!"
"2389" = "Thế là, mình cũng thư giãn theo á.\\nThư giãn rồi thì mồ hôi, lại túa ra như tắm á."
"2431" = "Tranh thủ lúc này mình cũng tiếp nước!\\nUống ừng ực nước trong bình á."
"2452" = "Vui quá đi!\\nCảm giác Bổn tiểu thư tự nhiên thông minh hẳn ra——Ư!!!"
```

## ハチロク02 — ハチロク02_8620運転台通信.txt.toml — 17/336 (5,1%)

- File: `ハチロク02_8620運転台通信.txt.toml` — route 01_Hachiroku, 336 dòng script (độc thoại 132, Soutetsu 63, Hachiroku 46, Điện xa Công chúa 31, Fukami 22, Nagi 21, Hibiki 14, Paulette 4, Reina 2, chim sẻ 1). Nội dung: họp trực tuyến với Điện xa Công chúa Mouri Aki — đặt mua dài hạn bản tin '8620運転台通信' (miễn phí trọn đời), hứa tặng một toa hành khách trong 2 tuần, mời cả nhóm đến Hiroshima; xen kẽ giải thích kỹ thuật buồng đốt/ống lò hơi/thân lò/buồng khói, bữa ăn Nagi–Fukami mang đến, và vụ nhầm 'chop' với 'chip' (tiền tip).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 336/336 (sau chuẩn hoá `\n`). `[selections]` rỗng. Không có bản sao file này (md5 `9ffb338bd09ef4a09ec44ee58a3ab01a`).
- Phân loại (17): thuật ngữ 5 (71, 1917 市電 gloss 'nguồn điện chính'→'tàu điện thành phố' + 町 'thành phố'→'thị trấn'; 1741, 2766 冥国 'nước Mỹ'→'Minh Quốc'; 2535 整備ボディ 'thân chính'→'thân bảo trì'), gasp っ 5 (1465 sweep sót — 「っ――」→'Ư——'; 1837, 2261, 2272, 2282 từ sweep, nhận nguyên văn), đại từ 2 (1951 Paulette 双鉄くん 'cậu Soutetsu'→'anh Soutetsu' theo khóa B4; 2230 Soutetsu 'tôi'→'anh' — trả lời Fukami key 2009), dịch sai 2 (1906 体育会系ノリ 'động chân động tay… chủ nghĩa thể thao'→'đáp lễ kiểu dân thể thao'; 2222 bỏ 'ái chà' bịa thêm sau さくさく――っと), bỏ sót 1 (1940 [うちの子,3] → thêm 'nhà mình'), lỗi chính tả 1 (1945 'trĩu trĩt'→'trĩu trịt'), SFX 1 (2415 けらけら 'cười khúc khích'→'cười ha hả').
- Sweep kiểm chứng: 4 mục cho file này (1837, 2261, 2272, 2282) đều đúng, đã nhận; sweep sót 1 mục (1465). Không còn っ thô trong VN; thẻ %l cân bằng JP = VN ở mọi dòng.
- Đại từ đúng toàn file: Soutetsu 'anh' với Hibiki/Nagi/Fukami, 'tôi' với Điện xa Công chúa; Hachiroku tự xưng 'em' nhất quán; Nagi→Fukami 'bé' đúng (1954).
- Chi tiết đầy đủ: `audit-hachiroku02-REVIEW.md`; danh sách sửa: `audit-hachiroku02-wrong.json` (17 mục, khối TOML 17 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 17/17; lượt soát 2: 17/17, 0 bỏ, 7 sửa — khôi phục dấu 「」 bị mất ở 1741, 1906, 1940, 1945, 1951, 2222, 2230).

**Tổng cộng sau file này: 114 file / 5.308 dòng sai** (cơ sở 113 file / 5.291 dòng sai + 17 file này)
- REBASE: cơ sở giao lúc spawn là 112 file / 5.258 dòng sai đã cũ — trong lúc audit, file 凪ふかみ01 đã gộp xong (+33) nên ROUTE-AUDIT.md hiện kết ở 113/5.291; snippet dùng cơ sở này (đã kiểm chứng trực tiếp với ROUTE-AUDIT.md).

- Chờ Hieu: 1849 ひゃわっ 'Hyawa' (xung đột ひあ/ひゃ toàn dự án); 1952 Soutetsu 'anh' vs 'tôi' (địa chỉ mơ hồ: Hachiroku hay nhóm Nagi/Fukami); 1960 Nagi 'ông nội' (câu hỏi ông nội/ông ngoại đang chờ chốt); 2049 Fukami 'Chào em' (người được chào không rõ). Lưu ý: 2 dòng 市電 71/1917 đã sửa tại đây nên gạch khỏi danh sách chờ đợt thống nhất.

```toml
[script]
"71" = "Nếu là \\x%l市電;#00ffc040;tàu điện thành phố%l;#;, thì đường ray chắc chắn sẽ chạy len lỏi giữa các khu phố.\\nKhói do \\x%l8620;#00ffc040;8620%l;#; nhả ra sẽ nhuộm đen cả thị trấn mất."
"1465" = "「Ư——」"
"1741" = "「Tuy nhiên, Minh Quốc sau chiến tranh đã trở thành một quốc gia tuyệt vời.\\nTổng thống của đất nước đó là một người xuất chúng ạ.」"
"1837" = "「Ư!」"
"1906" = "「Hô. Ở phương Tây cũng có kiểu——\\nđáp lễ kiểu dân thể thao à.」"
"1917" = "「Là do muội than——khói mù mịt thải ra từ ống khói ạ.\\nVì em được biết Đường sắt Điện Hiroshima là \\x%l市電;#00ffc040;tàu điện thành phố%l;#; ạ.」"
"1940" = "「Nếu cứ lặp đi lặp lại như vậy, mọi người sẽ biết đến 8620 nhà mình,\\nmột cách rộng rãi và sâu sắc hơn nhỉ.」"
"1945" = "「Sẽ còn đen hơn nữa cơ ạ, ngài Soutetsu. Rồi sẽ đến lúc, trên những ô cửa sổ cao kia,\\nđàn chim sẻ đen như nhuộm mực sẽ đậu trĩu trịt cho xem.」"
"1951" = "「Nhắc mới nhớ, anh Soutetsu.\\nCông chúa đang gọi anh đấy.」"
"2222" = "「Công nhận……ngon thật.\\nBánh mì thì dai mềm, thịt cốt lết thì giòn rụm——.」"
"2230" = "「Không phải đồ trang trí đâu. Tay cầm đó dùng để vặn mở đấy.\\nLần đầu tiên nhìn thấy, anh cũng ngạc nhiên lắm.」"
"2261" = "「Ư!!」"
"2272" = "『「Hả~~Ư!」\\n「Hả~~Ư!」』"
"2282" = "『「Ư!!?」\\n「A.」』"
"2415" = "Chẳng hiểu sao, Nagi lại cười ha hả.\\nCòn Fukami thì lấy hai tay che miệng, mắt sáng rực nhìn chúng tôi."
"2535" = "Từ trong màn hình được chia nhỏ, tôi bị Hibiki với khuôn mặt đen thui giống mình,\\nvà Hachiroku vừa thay thân bảo trì trắng trẻo mắng mỏ."
"2766" = "Một bà cụ người Minh Quốc hay người Anh,\\nlại đi tặng \"cú chặt\" để tỏ ý khen ngợi sao——"
```

## ハチロク10 — ハチロク10_旺宮鉄道歴史館.txt.toml — 65/572 (11,4%)

- File: `ハチロク10_旺宮鉄道歴史館.txt.toml` — route 01_Hachiroku, 572 dòng script (độc thoại 196, Soutetsu 124, ひよこ 117, Hachiroku 99, Olivy 36). Nội dung: thăm Bảo tàng Lịch sử Đường sắt Oukyou, gặp tiến sĩ Fushicho (Hiyoko) — giải thích タブレット, cộng cảm toàn phần, lịch sử Stephenson/Trevithick, Đại bãi bỏ, sự kiện Ueyama; Olivy được kiểm tra có ý thức.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 572/572 (sau chuẩn hoá `\n`). `[selections]` rỗng. Không có bản sao file này (md5 `4326168a59b6c3b615098e40471f3923`).
- Phân loại (65): thuật ngữ 36 (タブレット 19, Ohitoyo 5, Teitetsu 3, 電車姫 4, 冥国 2, 運転体 2, 整備体 3, 宮司 1, 機関士 1 — 2146/3209/3510 mang nhiều lỗi trong một dòng), đại từ 9 (Soutetsu 'anh'→'tôi' 7: 2007, 2010, 2187, 2460, 2462, 2547, 2842; Hachiroku 2: 2289, 2340), gasp っ 9 (8 từ sweep + 2488 sweep phân loại sai), SFX 6 (tiếng cười thành tiếng rên 5: 2208, 2283, 2284, 2292, 2759; くすっ 1: 2943), dịch sai 3 (2019, 2181, 3475), thẻ %l 1 (2816), lỗi đánh máy 1 (3581 'xo xa'→'vượt xa').
- Sweep kiểm chứng: 9 mục cho file này (8 fix đều đúng, nhận nguyên văn; 2488 already-rendered bị phân loại sai — cùng mẫu っ cuối sau dấu gạch như 3447/3663 trong file, đã sửa thành ——Ư!). Không còn っ thô trong VN; thẻ %l cân bằng JP = VN ở mọi dòng sau khi sửa 2816.
- Đại từ đúng toàn file: Soutetsu 'tôi' với Hachiroku và tiến sĩ Fushicho, 'anh' với Olivy (2275, 2302 — tiền lệ ハチロク05); Hachiroku tự xưng 'em' nhất quán; Olivy gọi Soutetsu 'cậu' giữ nguyên.
- Chi tiết đầy đủ: `audit-hachiroku10-REVIEW.md`; danh sách sửa: `audit-hachiroku10-wrong.json` (65 mục, khối TOML 65 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 65/65; lượt soát 2: 65/65, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 115 file / 5.373 dòng sai** (cơ sở 114 file / 5.308 dòng sai + 65 file này)
- REBASE: cơ sở giao lúc spawn là 114 file / 5.308 dòng sai — đã kiểm chứng trực tiếp với ROUTE-AUDIT.md (dòng tổng cuối), khớp, không cần rebase.

- Chờ Hieu: 日ノ本 'Hinomoto' (1507, 2375, 2730, 3431, 3480) vs 'Hinamoto' (1529, 1994, 2488); Soutetsu gọi Olivy 'cậu' (2304) vs 'em' (2302); Hachiroku tự xưng 'Tôi' (2321, 2451, 2890) vs 'em'; tiến sĩ Fushicho gọi Soutetsu 'Anh Migita' (2092, 2197, 2198) vs 'ngài Migita'.

```toml
[script]
"1479" = "「Khả năng tự sao chép của \\x%lタブレット;#00ffc040;máy tính bảng%l;#;——của linh hồn. Hoặc là chức năng sinh sản.\\nChẳng phải là để giải trừ phong ấn được đặt trên đó sao.」"
"1488" = "「Các loại kiểm tra theo luật định của \\x%lレイルロオド;#00ffc040;Railord%l;#;,\\ntất cả đều được tiến hành trong trạng thái tháo \\x%lタブレット;#00ffc040;máy tính bảng%l;#;, tức là trạng thái không khởi động.」"
"2007" = "「Không đâu, em khiêm tốn như vậy làm tôi buồn đấy. Có Hachiroku,\\nvà có tôi——hai chúng ta đã cùng nhau, đi đến tận bước đường này mà.」"
"2010" = "「Không, tôi thấy câu nói đó của em cũng có vấn đề đấy.」"
"2019" = "「Dù muốn hay không, nhìn thấy một lần là không thể nào quên được luôn đó~!\\nMong được giúp đỡ nha, Doctor Phoenix!」"
"2062" = "「Ư!!?」\\n「!!」"
"2113" = "「Trên toàn thế giới, \\x%lタブレット;#00ffc040;máy tính bảng%l;#; của tất cả các \\x%lレイルロオド;#00ffc040;Railord%l;#;,\\nđều được xuất xưởng từ một nhà máy duy nhất.」"
"2146" = "「Tháo \\x%lタブレット;#00ffc040;máy tính bảng%l;#; ra khỏi cả \\x%l運転体;#00ffc040;thân vận hành%l;#; lẫn \\x%l整備体;#00ffc040;thân bảo trì%l;#;, rồi đem đi cất giữ.\\nTrạng thái đó, đã……kéo dài được hơn bốn năm rồi thì phải.」"
"2152" = "「Ra là vậy, có lẽ cũng có khía cạnh đó đấy.\\nĐiều đó cuối cùng, đã nuôi dưỡng nên văn hóa công ty của Đường sắt Ohitoyo.」"
"2181" = "「Không thể thực hiện được. ——Nếu đã như vậy, thì các Navi Aircra thông thường,\\nkhông sở hữu thứ gì đó……giống như linh hồn sao ạ?」"
"2184" = "「Chỉ cần suy ngược lại là được. Rằng 『\\x%lタブレット;#00ffc040;Máy tính bảng%l;#; mang một bản chất\\nsẽ bị loại bỏ nếu được biết đến quá rộng rãi』 đúng không?」"
"2187" = "「Dù vậy, tôi vẫn còn vô cùng thiếu kinh nghiệm.\\nThực tế thì, tôi cũng đâu biết gì về Cow Catcher.」"
"2190" = "「Vậy mà, nếu như họ đã loại bỏ \\x%lタブレット;#00ffc040;máy tính bảng%l;#;.\\nThì mục đích của Đại bãi bỏ chính là——tiêu diệt \\x%lタブレット;#00ffc040;máy tính bảng%l;#;.」"
"2205" = "「——Ư」"
"2206" = "「Ư!!?」"
"2208" = "「Nfufufufu.」"
"2222" = "「Uây~, hiếm thấy thật đấy!\\nCòn hiếm hơn cả \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Meriken nhiều đó nha~!」"
"2233" = "「À, tên bây giờ là Aki nhỉ. Mouri Aki.\\nNfufu. Mà, người đời thường gọi là Công chúa Tàu điện đấy.」"
"2238" = "「Dù có chế tạo một cơ thể mới hay làm bất cứ điều gì đi chăng nữa,\\n\\x%lタブレット;#00ffc040;máy tính bảng%l;#; cũng chắc chắn sẽ già yếu đi, và cuối cùng, sẽ phải đối mặt với cái chết không thể tránh khỏi.」"
"2241" = "「Ư!!?」\\n「!!!」"
"2259" = "「Ư!!!」"
"2283" = "「Nfufu.」"
"2284" = "「Nfufufu.」"
"2289" = "「Ufufu, được cô khen ngợi em thấy rất vinh hạnh.\\nNhưng mà, tất cả đều là nhờ vào năng lực và sự nỗ lực của ngài Soutetsu đấy.」"
"2292" = "「Nfufu, vậy cũng được thôi, cô Hachiroku.\\nNếu vậy, tôi cũng sẽ thay đổi nội dung yêu cầu nhé.」"
"2315" = "「Thời kỳ hoàng kim của Teitetsu. \\x%lレイルロオド;#00ffc040;Railord%l;#; chỉ là linh kiện bảo đảm an toàn tiêu hao.\\nLà luận văn vào cái thời mà chẳng có ai nghĩ đến việc kéo dài tuổi thọ cho các cô cả.」"
"2328" = "「Ể!? Soutetsu, cậu không phải là fan cuồng đường sắt sao!?\\nThế mà cậu lại là chủ tàu, rồi còn làm \\x%l機関士;#00ffc040;Lái tàu%l;#; nữa á!?」"
"2340" = "「Chị Olivy……\\nđã tồi tệ đến mức đó rồi sao ạ?」"
"2416" = "「Tốt lắm. Vậy thì, tôi có thể tiến hành phân tích và sao chép\\n\\x%lタブレット;#00ffc040;máy tính bảng%l;#; của cô Hachiroku được chứ?」"
"2451" = "「Tôi là \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của 8620 thuộc Đường sắt Ohitoyo,\\nHachiroku. Xin được chiếu cố ạ.」"
"2460" = "「Tôi tin vào phán đoán của em.\\nTôi muốn chính em hãy suy nghĩ xem điều gì là tốt nhất cho em và Olivy.」"
"2462" = "「Tôi nghĩ, chắc chắn là có khả năng đó.\\nGiữa tôi và Hachiroku——không, Suzu——giữa tôi và em.」"
"2465" = "「Hình hài con người, tôi nghĩ là để trong trường hợp khẩn cấp có thể\\nđóng vai trò thay thế cho \\x%l機関士;#00ffc040;Lái tàu%l;#; và \\x%l機関助士;#00ffc040;phụ lái tàu%l;#;.」"
"2488" = "「\\x%lレイルロオド;#00ffc040;Railord%l;#; là một sự tồn tại ưu việt. Thực tế là ở Hinamoto hiện tại,\\ncác \\x%lレイルロオド;#00ffc040;Railord%l;#; đã nghỉ hưu đang hoạt động sôi nổi ở khắp mọi nơi——Ư!」"
"2493" = "「Nói cách khác, \\x%lタブレット;#00ffc040;máy tính bảng%l;#; chỉ có ở một nơi duy nhất——\\nkhông, nếu nói một cách chính xác hơn, thì có lẽ là」"
"2507" = "「Nếu vậy, hoàn toàn không cần thiết phải\\nloại bỏ \\x%lタブレット;#00ffc040;máy tính bảng%l;#; khỏi Navi Aircra. Vậy mà」"
"2532" = "「Là \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; của Minh Quốc sao.」"
"2547" = "「Quả nhiên là vậy sao. Cảm ơn cô đã cho tôi biết.」"
"2551" = "「Như tôi đã nói lúc nãy, Navi Aircra và \\x%lタブレット;#00ffc040;máy tính bảng%l;#;,\\nvốn dĩ nên là những thứ cùng tồn tại với nhau.」"
"2564" = "「Là thứ trú ngụ bên trong \\x%lタブレット;#00ffc040;máy tính bảng%l;#; sao ạ?」"
"2606" = "「Thế nhưng, thực tế là \\x%lタブレット;#00ffc040;máy tính bảng%l;#; đã bị loại bỏ.\\nThậm chí, nguồn cung cấp duy nhất của nó cũng đã bị đóng lại.」"
"2632" = "「Tại vì, ngày xưa ấy? Những nơi như Teitetsu là doanh nghiệp nhà nước,\\nnên có vẻ cũng có những người tìm đến đường sắt vì muốn sự ổn định.」"
"2636" = "「Đương nhiên, công ty \\x%lレイルロオド;#00ffc040;Railord%l;#; Tablet cũng bị đóng cửa và giải thể.\\nBởi vì công nghệ chế tạo \\x%lタブレット;#00ffc040;máy tính bảng%l;#; đã hoàn toàn bị thất truyền.」"
"2644" = "「Tororyu-yu——Cựu kỹ quan Toro!\\nÀ, nhắc mới nhớ, bà ấy đang sống ở Ohitoyo nhỉ.」"
"2731" = "「Một cơ chế không hề có từ thế hệ thứ nhất trở đi.\\nNói cách khác, là Navi Aircra có chứa \\x%lタブレット;#00ffc040;máy tính bảng%l;#; bên trong.」"
"2759" = "「Fufun?」"
"2816" = "「Là bộ gạt vật cản nhô nhọn ra phía trước, đặc trưng của \\x%l蒸機;#00ffc040;Đầu máy hơi nước%l;#; kiểu cũ của Minh Quốc.\\nĐó chính là Cow Catcher ạ.」"
"2839" = "「Ư!!!?」"
"2842" = "「Tôi đã chứng kiến. Công việc của Hibiki. Thiết kế là,\\nbiến những cách bố trí tưởng chừng như không thể thành có thể thông qua việc sắp xếp lại.」"
"2866" = "「Trước khi tháo \\x%lタブレット;#00ffc040;máy tính bảng%l;#; ra, cô ấy vẫn đang hoạt động sao?」"
"2894" = "「Nếu vậy, mức độ mở hoàn toàn là——đúng như nghĩa đen,\\ntất cả những gì bên trong \\x%lタブレット;#00ffc040;máy tính bảng%l;#;——\\x%l共感;#00ffc040;cộng cảm%l;#; toàn bộ lĩnh vực, sao?」"
"2916" = "「Ngài Soutetsu là vì Ohitoyo. Và, một phần nào đó,\\nlà vì em——nên mới trở thành \\x%l機関士;#00ffc040;Lái tàu%l;#; hơi nước ạ.」"
"2943" = "「Do——Doc, tor……Phoe, nix. Hì hì.」"
"3209" = "Ngay cả khi vận hành \\x%l運転体;#00ffc040;thân vận hành%l;#;, việc bắt buộc phải đặt \\x%l整備体;#00ffc040;thân bảo trì%l;#; bên trong buồng lái,\\nchính là minh chứng rõ ràng nhất cho điều đó."
"3241" = "Nhưng, nếu việc giải trừ phong ấn là chìa khóa.\\nThì việc sao chép, hay sáng tạo ra \\x%lタブレット;#00ffc040;máy tính bảng%l;#; vốn được cho là bất khả thi hiện nay——"
"3266" = "Những ngón tay của Hachiroku đưa lên trước ngực——\\nnhư đang bấu chặt lấy \\x%lタブレット;#00ffc040;máy tính bảng%l;#; của mình."
"3447" = "Tổng tài đầu tiên của Teitetsu được phát hiện đã tử vong do bị tàu cán vào một đêm mưa giữa khuya.\\nĐó là một vụ án mạng, hay chỉ là một tai nạn, sự thật đó cho đến nay vẫn——Ư!"
"3463" = "Những thông tin về tôi và Hachiroku, cho đến cả những chi tiết khá nhỏ nhặt,\\ncó lẽ đã được Công chúa Tàu điện truyền đạt lại rồi."
"3475" = "Một tầng hầm mờ tối và lạnh lẽo.\\nNhà chứa xe……không, gọi là nhà kho thì đúng hơn."
"3510" = "Tôi nhớ đến \\x%lレイルロオド;#00ffc040;Railord%l;#; của đền chủ Akai——Niiroku.\\nNghe nói cô ấy đã đánh mất \\x%l整備体;#00ffc040;thân bảo trì%l;#; của mình——"
"3581" = "Nhưng đường sắt đã phát triển\\nvượt xa so với những gì Trevithick tưởng tượng."
"3633" = "Tên thật. Chắc hẳn là cái tên mà Công chúa Tàu điện đã cho chúng tôi biết,\\ncái tên 『Hiyoko』."
"3663" = "Sững sờ——kinh ngạc——không, còn trống rỗng hơn cả những từ ngữ đó——\\nA, đúng rồi. Một biểu cảm như người mất hồn——Ư!!?"
"3705" = "Chuỗi ký tự đó, chính là cách đối xử với \\x%lレイルロオド;#00ffc040;Railord%l;#; theo kiểu Teitetsu,\\ntrong một thời gian gần đây, tôi cũng đã phần nào hiểu được."
"3759" = "（A. Nếu vậy thì cái tên 『Momiji』 lúc nãy——\\ncũng giống như một biệt danh của Công chúa Tàu điện sao?）"
```

## lr_ハチロクh2 — lr_ハチロクh2_新しい服。新しい旅.txt.toml — 63/327 (19,3%)

- File: `lr_ハチロクh2_新しい服。新しい旅.txt.toml` — route 01_Hachiroku, 327 dòng script (107 thoại Hachiroku, 89 thoại Soutetsu, 131 độc thoại). Nội dung: cảnh h Hachiroku — bộ quần áo mới đưa hai người vào "chuyến đi mới" ngay trong phòng quen thuộc; cô mặc đồ mới, ân ái nhiều lượt, kết bằng cảnh Soutetsu nằm nghỉ còn Hachiroku chuẩn bị bữa cơm.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất. 173 lệch TOML/CSV3 đều chỉ là `\n` bị flatten thành khoảng trắng trong TOML-2. `[selections]` rỗng. Không có thẻ `%l` nào trong file. Không có bản sao file này (md5 `7b0a3c5d1db89046c9b50bee2ff0e6f5`).
- Phân loại (63): xưng hô 22 (Soutetsu tự xưng "anh" 22/24 dòng thoại với Hachiroku — 1361, 1402 quét máy bắt thêm; chỉ 2 dòng "tôi" đúng sẵn 1364, 1579; 2 dòng gộp gasp 1557, 1681), thở gấp 29 chỗ (17 từ sweep + 12 mới: 1105, 1407, 1408, 1410, 1411, 1429, 1433, 1463, 1470, 1472, 1486, 1527 — っ cuối tuyệt đối trên từ âm thanh theo quyết định 仲国05), tiếng cười 7 (1423, 1424, 1447, 1508, 1511, 1547, 1606 — cười diễn thành rên, sửa về Nfufu/Ufufu/Fufu), sai nghĩa 3 (1436 はまっ=さま không phải "sâu", わらくっ="Em" không phải "Của em"; 1593 chủ ngữ quần áo; 1836 お仕置きして欲しい ngược hướng + gỡ ngoặc tự thêm), SFX 3 (1714 ぐぽ→"(Gupoooooooo)"; 1716 ぬと/れる/じゅるるるる→"(Nụtọooo——liếm——Chùn chụt)"; 1718 じゅぶううっ→"Chụụụt!"), thuật ngữ 1 (1440 タブレット→"máy tính bảng").
- Sweep kiểm chứng: 20 mục cho file, nhận 17 fix + 1 already-rendered (1104) + 2 needs-audit giải quyết xong không sửa (1720 "~~~~~~~~ưm", 2103 "ư" mềm — đều không lệch dòng).
- Chi tiết đầy đủ: `audit-lr-hachirokuh2-REVIEW.md`; danh sách sửa: `audit-lr-hachirokuh2-wrong.json` (63 mục, khối TOML 63 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 63/63; lượt soát 2: 63/63, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 116 file / 5.436 dòng sai** (cơ sở 115 file / 5.373 dòng sai + 63 file này)

- Chờ Hieu: đợt thống nhất fa/fu (14 dòng: 1410, 1424, 1425, 1427, 1428, 1429, 1432, 1433, 1434, 1436, 1438, 1440, 1442, 1443 — ふぁ/ふあ→"Haa"); mâu thuẫn ひあ/ひゃ (1410 "Hya" giữ); ranh giới gasp giữa dòng (~11 dòng / ~25 token っ giữa dòng, chủ yếu trong chuỗi rên 1410–1443); mâu thuẫn tiền lệ Hibiki 03 key 2360 (ふふっ→"Ư hự" ngược quy tắc cười); "Tablet" còn 16 dòng toàn dự án; 1121 Hachiroku gọi Soutetsu "anh" cho あなた (giữ — xem §8 review).
- Parent đính chính 20/11 ~19:25: cờ "Hibiki 03 key 2360 ふふっ→Ư hự" là ghi nhầm — không có key 2360 trong fix list Hibiki 03 (dòng ふふ duy nhất, key 2752, đã là tiếng cười đúng); 2360 là key của ポーレットh8, 4 dòng "Ư hự" đó đã sửa thành tiếng cười từ 19/11 22:05 — KHÔNG cần Hieu quyết.

```toml
[script]
1105 = "「——AƯ」"
1120 = "「——Làm tôi cháy bỏng, làm tôi khao khát. Rằng tôi muốn em, muốn ôm lấy em.\\nĐã khiến tôi nóng bỏng và hưng phấn đến nhường này.」"
1358 = "「Cho dù có hỏng đi chăng nữa——tôi nhất định, sẽ sửa lại cho em」"
1361 = "「Là em đấy, Suzu. Cơ thể em khi tôi ngước nhìn từ đây.\\nSức nóng của em, và cả mùi cơ thể lẽ ra không tồn tại——」"
1402 = "「Cô bé của em, vẫn giống hệt như lần đầu tiên tôi nhìn thấy.\\nVẫn cho tôi thấy vẻ thanh khiết tột cùng không đổi thay」"
1407 = "「HyauƯ!!!!」"
1408 = "「HyauuuƯ!!!?」"
1410 = "「Hya! Ưm! Haa! YuunƯ!!!」"
1411 = "「HyauƯ!!!!」"
1414 = "「Ư」"
1415 = "「Ư!!!」"
1416 = "「Ư!!!!」"
1417 = "「Ư!?」"
1418 = "「Ư——a——Suzu, Suzu!」"
1423 = "「Nfufu」"
1424 = "「Haa——a……a……ưm——.\\nHư——Ufu——Ufufufufu」"
1429 = "「Haa! A! Ahi! AhyuƯ!!!」"
1433 = "「Haa! A! A! AƯ!!!」"
1436 = "「Haa! A! Sướng quá——ngài Soutetsu!\\nƯm! Em, em, cái này, sướng quá——!」"
1440 = "「Haa! Chết mất, máy tính bảng, kỳ lạ hết rồi——\\nTrắng xóa mất, ưm! Chớp nháy, liên tục」"
1447 = "「Trời ạ, ngài Soutetsu thật là. Nhưng mà——đúng vậy nhỉ. Fufu」"
1456 = "「Ư!!!!」"
1457 = "「Ư!!!!!!」"
1458 = "「Ư!!!!!!!!」"
1459 = "「Ư!!!?」"
1462 = "「A——a——Ư——」"
1463 = "「A, a, a, aƯ」"
1470 = "「AaaaaaƯ」"
1472 = "「HauƯ.」"
1474 = "「A~~~~Ư」"
1483 = "「Ư——!!!!」"
1486 = "「Ưm——ư——aƯ!」"
1507 = "「Aa, tôi biết rồi. Tôi cũng cùng em」"
1508 = "「Nfufu. Em uống ngoan chứ」"
1511 = "「Ufufu, đương nhiên rồi ạ? Vì là của hai người mà.\\nVì là chuyến đi của ngài Soutetsu và em mà」"
1513 = "「Linh hồn của em, thứ mà tôi yêu thương nhất,\\nđây là một vỏ bọc vô cùng xinh đẹp, hoàn toàn hài hòa với nội tâm đó.」"
1516 = "「Trong mắt tôi thì là vậy.\\nNgay cả những bóng đen vô cùng nhỏ bé được vẽ ra.」"
1527 = "「AaƯ!」"
1539 = "「Ừ, tôi đang cương cứng.」"
1547 = "「Đúng không ạ, Ufufu」"
1557 = "「Tôi cũng vậy, Suzu. Thế nên——Ư!!!?」"
1560 = "「Tôi cũng vậy. Tôi rất yêu em」"
1566 = "「Vì chúng ta là vợ chồng, là bạn đời, là đối tác.\\nCùng với em, như một người phụ nữ, tôi muốn cả hai cùng nhau thay đổi」"
1574 = "「Bộ phận sinh dục của em. Cô bé của em ấy.\\nĐã đón nhận tôi hết lần này đến lần khác và hoàn toàn mang hình dáng của tôi」"
1578 = "「Mong muốn của tôi là——mong muốn không bao giờ thay đổi là——cùng với em——」"
1583 = "「Em! Không——a ư——giới hạn, giới hạn rồi!\\nƯ——nhưng mà——cùng, cùng nhau, nhé, cùng nhau」"
1593 = "「Lần tới ngài muốn em mặc bộ quần áo nào, và muốn có chuyến đi mới như thế nào.\\nNhỉ? Ngài Soutetsu. Ngài đang nghĩ gì vậy?」"
1595 = "「Nếu vậy, Suzu. Hãy hiểu mong muốn của tôi」"
1599 = "「Dù bên trong đã thay đổi thành của một người phụ nữ——trưởng thành hoàn toàn,\\nthành bộ phận sinh dục nữ dành riêng cho tôi」"
1606 = "「Vâng. Ufufu. Thế nên em, bộ quần áo này.\\nEm thích nó hơn ngày hôm qua rồi」"
1619 = "「Nhỉ. Đương nhiên rồi.\\nVì là chuyến đi mà tôi và em, cùng nhau trải qua mà」"
1623 = "「Nhưng mà, ngay cả vẻ bề ngoài, tôi vẫn luôn,\\nbị tan chảy và mê hoặc đấy.」"
1624 = "「Tất nhiên tôi biết rất rõ, cơ thể của em——\\nCòn làm tôi tan chảy hơn cả vẻ bề ngoài của nó.」"
1648 = "「Tôi đã có một trải nghiệm mới, một chuyến đi trong căn phòng này.\\nNếu em cũng vậy thì——」"
1669 = "「Ngay bây giờ ở đây——tắm trên người tôi là được.」"
1671 = "「Giống như tôi thôi」"
1681 = "「Su, zu. Không được đâu.\\n——Cứ thế này thì, tôi——Ư!?」"
1714 = "「（Gupoooooooo）——ưm……ưm!」"
1716 = "「（Nụtọooo——liếm——Chùn chụt）\\nChụt! Phụt! Chụt! Phụt!」"
1718 = "「Vì thế……ưm.\\nChụụụt! Chụt! Chụt! Chụt!」"
1836 = "Mặc dù tôi cũng rất muốn cứ thế này mà được em ấy trừng phạt——\\nnhưng tôi không muốn ân ái với Suzu trong khi em ấy vẫn còn hiểu lầm."
2009 = "Một hành động vô cùng dâm đãng, nhưng lại được tô điểm bằng nụ cười ngây thơ——Ư!!"
2109 = "Chuyển động của Suzu trở nên đơn điệu. Chỉ để thúc giục tôi xuất tinh——\\nsự thẳng thừng, đơn giản, bạo lực, mang tính động vật và máy móc này——Ư!?"
```

## ハチロク01 — ハチロク01_こんにちわ赤ちゃん.txt.toml — 15/530 (2,8%)

- File: `ハチロク01_こんにちわ赤ちゃん.txt.toml` — route 01_Hachiroku, 530 dòng script (độc thoại 183, Hachiroku 113, Soutetsu 112, Urakami 27, Kisaki 25, Mototada 22, Mayu 21, Hibiki 15, Mayami 12). Nội dung: Soutetsu và Hachiroku đón Urakami cùng bé Mayu mới sinh — Hachiroku lần đầu bế em bé, tập vỗ ợ hơi, cho bú, dỗ ngủ; xen kẽ cuộc họp với Mototada và Kisaki về Dự án SL Đại Kyushu (tuyến Yunoi–Hayato, 8620 quá tải); kết: Soutetsu nhận ra Hachiroku khao khát có con nhưng sợ thân phận Railord không thể sinh con.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 530/530 (sau chuẩn hoá `\n`). `[selections]` rỗng. Không có bản sao file này (md5 `f7fccdad72cb0c04171cd9b121cb614a`).
- Phân loại (15): gasp 6 (sweep: 1620, 1621, 2262, 2263, 2280, 2637), dịch sai 4 (2392, 2426, 2549, 2762), thuật ngữ 2 (Toukai đọc sai: 2216, 2815), đại từ/xưng hô 2 (2393 'anh Kisaki'→'cô Kisaki', 2790 tên trần 'Kisaki'→'cô Kisaki'), rò ký tự 1 (2164 'hành客'→'khách hàng').
- Sweep kiểm chứng: 6 mục cho file này, cả 6 đều đúng, nhận hết (2637 theo dạng ngắt dòng CSV3). Không còn っ thô trong VN; thẻ %l cân bằng JP = VN ở mọi dòng.
- Đại từ đúng toàn file: Soutetsu 'tôi' với Hachiroku ở mọi dòng đối thoại (0 dòng 'anh'); Hachiroku tự xưng 'em' nhất quán; Kisaki gọi Soutetsu 'cậu' giữ nguyên.
- Chi tiết đầy đủ: `audit-hachiroku01-konnichiwa-akachan-REVIEW.md`; danh sách sửa: `audit-hachiroku01-konnichiwa-akachan-wrong.json` (15 mục, khối TOML 15 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 15/15; lượt soát 2: 15/15, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 117 file / 5.451 dòng sai** (cơ sở 116 file / 5.436 dòng sai + 15 file này)
- REBASE: cơ sở giao lúc spawn là 116 file / 5.436 dòng sai — đã kiểm chứng trực tiếp với ROUTE-AUDIT.md (dòng tổng cuối), khớp, không cần rebase.

- Chờ Hieu: Ohimitera/Ohito 16 dòng + Maitetsu 1 dòng (2816) → unification pass; 2319 んあーんっ 'Nga——n.' có thêm Ư hay không (xem REVIEW).

```toml
[script]
"1620" = "「——Ư!」"
"1621" = "「——————Ư!!!」"
"2164" = "「Lễ nghi——trong các buổi lễ kỷ niệm,\\nem vẫn xuất hiện trước mặt khách hàng.」"
"2216" = "「Nagotetsu là tuyến đường sắt tư nhân danh tiếng thì khỏi phải bàn rồi. Đường sắt Toukai, là công ty đã mua lại tuyến chính Toukai-dou của Teitetsu cũ, đoạn Mishima-Ousaka nhỉ.」"
"2262" = "「Ư!!」"
"2263" = "「Ư!!!」"
"2280" = "「Anyu~~Ư.」"
"2392" = "「V, vâng. Vậy thì——\\nXin cô cho em bế bé một chút ạ.」"
"2393" = "「Lâu rồi không gặp. Giám đốc chi nhánh——à không, cô Kisaki.\\nCùng với anh Migita và cô Hachiroku nữa.」"
"2426" = "「Là số phận……mà con bé chẳng thể nào thay đổi được,\\nchắc vậy.」"
"2549" = "「Thế nên tôi mới bảo em bình tĩnh. Tôi cũng không biết nữa, nhưng bé đang cười kìa.\\nCó lẽ tiếng 『Nga——n』 đó không mang ý nghĩa xấu đâu.」"
"2637" = "「Không thể thay đổi được?\\n——Rốt cuộc là chuyện gì chứ————Ư!!!」"
"2762" = "「Điều tốt là, cả ngài Soutetsu nữa cơ?\\nBởi vì ngài Soutetsu và bé Mayu, cũng rất hợp nhau mà.」"
"2790" = "「Vậy, chúng tôi xin phép. Cô Kisaki, cô Urakami.」"
"2815" = "「Những cú hit ở các nơi đó, đã lan rộng đến Nagotetsu và Đường sắt Toukai——\\nNhững doanh nghiệp đường sắt lớn đã sống sót qua đợt Đại bãi bỏ tuyến.」"
```

## ふかみh1_ともはり練習 — ふかみh1_ともはり練習.txt.toml — 98/272 (36,0%)

- File: `ふかみh1_ともはり練習.txt.toml` — route 07_Nagi_Fukami, 272 dòng script (148 độc thoại, 75 thoại Fukami, 49 thoại Soutetsu). Nội dung: cảnh h Fukami — buổi hẹn riêng hai người luyện tập chèo thuyền (ともはり練習) trên thuyền xuôi dòng: Fukami lau người cho Soutetsu, hai người ân ái trên thuyền, xen kẽ đối thoại về số lần hẹn hò riêng (Fukami 2 lần, Nagi 1 lần).
- Lệch vị trí 88, chuỗi xoay 6, nhiễm chéo 0, mồ côi 2 xác nhận (+4 chưa rõ), chưa dịch 0, trùng khóa 0. CSV3 2 set — bộ home (07_Nagi_Fukami) là bộ cũ (khớp TOML 1/272 VN, JP khác 188 dòng), bộ 11_Other mới là chuẩn (khớp TOML 272/272). 151 lệch TOML/CSV3 đều chỉ là `\n` bị flatten thành khoảng trắng trong TOML-2. `[selections]` rỗng. Không có thẻ `%l` nào trong file. Không có bản sao file này (md5 `be7f335b835a741dab4d414880f9aacd`).
- Phân loại (98): lệch dòng 88 (82 khôi phục trong file + 6 viết mới) · thở gấp 5 (979, 1043, 1058, 1137, 1403) · SFX 2 (781, 969) · dịch sai 2 (1011 gán nhầm bụng cho Soutetsu, 1474 力んだ声→"quyết tâm") · nhãn 1 (766 độc thoại bị bọc 「」).
- Sweep kiểm chứng: 3 mục cho file, nhận 1 fix (1403) + 2 false positive (1426, 1461 — JP không có っ, VN đã đúng); sweep bỏ sót 4 dòng gasp (979, 1043, 1058, 1137).
- Chi tiết đầy đủ: `audit-fukamih1-tomohari-renshuu-REVIEW.md`; danh sách sửa: `audit-fukamih1-tomohari-renshuu-wrong.json` (98 mục, khối TOML 98 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 98/98; lượt soát 2: 98/98, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 118 file / 5.549 dòng sai** (cơ sở 117 file / 5.451 dòng sai + 98 file này)
- REBASE (parent): snippet ghi cơ sở 116 file / 5.436 — đã rebase về 117 file / 5.451 sau khi gộp ハチロク01 (tổng mới 118 file / 5.549).

- Chờ Hieu: đợt thống nhất fa/fu 7 dòng (987, 989, 992, 1039, 1045, 1048, 1049 — ふあ/ふぁ/ぷあ→"phà"/"phùa"); 4 VN mồ côi có thể là bản dịch lỏng (1031, 1034, 1081, 1675); 2 VN mồ côi xác nhận không có nguồn (781, 1065); 990 dùng "Uoa!?" (bản dịch có sẵn trong file cho うぉっ); 1553 chuẩn hóa ngoặc JP （...」 → （...）.

```toml
[script]
"762" = "……Fukami đang ra sức lau người cho tôi.\\nĐược em ấy lau cho thì đúng là biết ơn thật đấy, nhưng mà——"
"766" = "……Chắc chắn là ướt rồi.\\nAnh đã cảm nhận được dâm thủy rỉ ra từ nãy đến giờ rồi."
"772" = "「……“Dù không bình đẳng nhưng vẫn công bằng”——sao.」"
"781" = "「……Ư……ưm…………ưm…………」"
"942" = "「Nhưng mà……không ngờ lại làm chuyện này trên thuyền xuôi dòng.」"
"952" = "「Nhờ em lau người cho nhiệt tình quá nên anh——\\nĐã hoàn toàn nóng lên mất rồi.」"
"969" = "「Hya fu!」"
"979" = "「Ư——」"
"981" = "「Không sao……ưm.」"
"987" = "「Phù——ah——của em——âm đạo——\\nMiệng của——anh Soutetsu——bằng miệng——」"
"990" = "「Uoa!?」"
"992" = "「Phù, ah——lưỡi……ấm……quá……ưm.」"
"993" = "「Phuê!?」"
"995" = "「Hả!? A! Anh Soutetsu, khoan hẵng qua đây——\\nÁ!? Oa a a a a a a a!?」"
"1001" = "「A……ya……thấm, vào rồi——ưm——em, âm đạo——nước bọt của anh Soutetsu……, thấm, vào——nóng, quá.」"
"1003" = "「Ah——phù——cháy, mất——tan chảy, mất——\\nCủa, em——âm đạo——ưm——tan chảy, mất thôi.」"
"1011" = "「A……ưm——ha——to, quá ạ——\\nCủa anh Soutetsu——ưm——đang đâm vào bụng em——」"
"1014" = "「A……v, vâng. ——Đúng, vậy nhỉ.\\nEm……cũng, ướt nhẹp……thế này, rồi.」"
"1015" = "「A……của, em……của, em……âm, đạo……\\nKhuôn mặt của……anh Soutetsu……gần……gần thế này.」"
"1018" = "「A……chỗ này vẫn chưa lau được chút nào cả.\\nEm xin lỗi——ưm……ây da, ây, da.」"
"1019" = "「A——」"
"1026" = "「A! Vâng! Vâng! Trăm sự nhờ anh ạ!!」"
"1031" = "「Hả!? Ơ!? T, tại sao——vậy, ạ?」"
"1034" = "「A, giỏi quá. Anh Soutetsu.\\nNếu làm như vừa nãy, anh có thể vượt qua dòng thác mà không bị tròng trành đấy.」"
"1039" = "「Thích……thích……Anh Soutetsu, đối với em——\\nĐã thích em rồi, sao……phù, ah.」"
"1043" = "「Ưm……ƯƯ——ưm——phù——ưm」"
"1045" = "「Ưm——phù. Em ướt sũng hết cả rồi.\\nThế này mà không cởi ra……thì Fukami sẽ bị cảm lạnh mất.」"
"1053" = "「Ư……ưm.」"
"1058" = "「Ư!!?——A hyu u u u u u ưm!!!」"
"1059" = "「Ưm nu!?」"
"1064" = "「Ây da, ây da——chà, chà——chà, chà.」"
"1065" = "「Ối!」"
"1068" = "「Nếu vậy thì.」"
"1074" = "「Em xin lỗi. Em đang đun nước tắm rồi nhưng……\\nChắc là vẫn còn phải mất thêm một lúc nữa.」"
"1081" = "「Chắc chắn là sẽ “thích nhiều hơn”, “thích hơn nữa”……\\nNhưng một người đã thích Fukami như anh, thì làm sao có chuyện “bắt đầu thích” được nữa.」"
"1083" = "「Đúng hơn là, Fukami đang ướt sũng rồi kìa.\\nNếu em không phiền——anh rất sẵn lòng giúp em lau người đấy?」"
"1085" = "「Vì thế……phần dưới……ừm, phần dưới——nếu, nếu——\\nNếu được……ừm! Nhờ anh, Soutetsu——làm, giúp em……」"
"1087" = "「Vì vậy, hẹn hò riêng hai người, em sẽ được hai lần,\\ncòn bé Nagi một lần. Thế này là vừa đủ công bằng rồi nhỉ.」"
"1088" = "「Vì vậy, em muốn anh xem lần đầu tiên.\\nHình ảnh em đang chèo thuyền trên sân nhà của mình——」"
"1093" = "「Chà, chà——lau, lau——ưm……sao rồi ạ?\\nAnh Soutetsu đã khô bớt chút nào chưa?」"
"1100" = "「Đúng vậy. Dù chênh lệch chưa đến mười phút,\\nnhưng người đầu tiên làm tình với anh Soutetsu là……bé Nagi.」"
"1106" = "「Chính là điều anh đang mong đợi đấy.」"
"1107" = "「Không sao đâu——chắc là không lo bị cảm lạnh đâu.」"
"1116" = "「Fukami!?」"
"1117" = "「Tại sao á, vì anh đã thích Fukami mất rồi.」"
"1118" = "「Vì có tận hai cơ hội mà,\\nnên em nghĩ, lần đầu tiên sẽ ở sân nhà của mình——」"
"1121" = "「Nếu để anh Soutetsu bị cảm lạnh thì em thấy có lỗi lắm.\\nEm sẽ lau cho anh bao nhiêu cũng được.」"
"1123" = "「“Bắt đầu thích” sao? Chuyện đó là không thể nào.」"
"1129" = "「Vậy sao.」"
"1133" = "「A, ừm——em——phần trên, em sẽ tự——tự cởi,\\nừm——em sẽ cởi, nên——」"
"1135" = "「Một em, đã được anh Soutetsu……khen là đ, đẹp.\\nEm muốn……anh Soutetsu……sẽ, sẽ thích, em, hơn nữa.」"
"1137" = "「Ư!!!」"
"1253" = "Nhưng ngay sau đó,\\nvị mật ngòn ngọt, mang theo chút hơi ấm bắt đầu hòa quyện vào."
"1263" = "Chỉ muốn bù đắp một chút cho việc đã khiến em ấy phải chờ đợi."
"1300" = "Không hẳn là tươi mát, mà đúng hơn là hương vị của nước lan tỏa trong miệng."
"1305" = "Vì tôi mãi không thể xác định được đó có phải là cám dỗ hay không,\\nnên có vẻ như tôi đã vô tình khiến Fukami phải nóng lòng chờ đợi."
"1307" = "Tại sao số lần lại không bằng nhau, cho đến khi được hai người giải thích,\\ntôi vẫn cảm thấy thật kỳ lạ, nhưng mà……"
"1309" = "Nơi tận cùng đường nét của vùng bụng hoàn toàn phẳng lì, một cặp ngực nhỏ hình bát úp, căng tròn,\\nđang lộ ra với núm vú màu hồng."
"1312" = "Vào thời kỳ hưng thịnh, dịch vụ đi thuyền xuôi dòng vào mùa đông rất đắt khách,\\nhọ thường cung cấp nước tắm sau giờ làm việc cho những người lái đò bị lạnh cóng."
"1319" = "Theo từng nhịp lau, nó cứ tiến lại gần rồi lại lùi ra xa,\\ntừng giọt, từng giọt nước nhỏ xuống mặt tôi."
"1326" = "Anh muốn làm em tan chảy. Liếm láp, mút mát nhiều hơn, nhiều hơn nữa.\\nNhưng để làm được điều đó, thì lớp vải mỏng này——"
"1358" = "Nhìn lại một lần nữa vào âm đạo đã hoàn toàn phơi bày,\\ntôi chăm chú quan sát——"
"1378" = "Cơ thể ngày càng nóng lên,\\nnhững phần da thịt chạm vào nhau ướt đẫm mồ hôi của cả hai."
"1379" = "Ngay sát chóp mũi của Fukami,\\ndương vật đang cương cứng của tôi đã nhô cao lên lớp quần."
"1382" = "Ngay từ đầu đã tung hết sức, tôi hôn lên đường rãnh dọc đang in hằn qua lớp quần lót,\\nrồi cứ thế thè lưỡi liếm láp thật mạnh."
"1385" = "Với Fukami, và Nagi.\\nMột buổi hẹn hò trọn vẹn một ngày chỉ có hai người với từng người."
"1387" = "Cảm giác vượt qua được thử thách khiến tôi vô tình thốt lên những lời nhẹ nhõm."
"1403" = "Có lẽ vì khoái cảm quá mãnh liệt,\\nFukami lắc đầu nguầy nguậy——Ư!"
"1431" = "Nếu đó là quyết định của Fukami và Nagi,\\nthì tôi cũng không nên xen mồm vào làm gì."
"1440" = "Mùi hương trở nên nồng đậm hơn."
"1442" = "Phía bên kia âm đạo của Fukami."
"1451" = "Em ấy đang nói ra sự thật với giọng điệu đều đều."
"1453" = "Giọng nói vui vẻ, hào hứng."
"1455" = "Mong muốn của Fukami là,\\nđược cùng tôi luyện tập chèo thuyền, chỉ có hai người với nhau."
"1465" = "Fukami nhận ra điều đó, nhưng không hề ngoảnh mặt đi.\\nNếu vậy thì, quả nhiên——đây chắc chắn là một sự cám dỗ rồi."
"1473" = "Sức ép bí ẩn trong giọng nói của Fukami cũng hoàn toàn biến mất,\\nthay vào đó, em ấy bắt đầu trở nên vui vẻ, hào hứng."
"1474" = "Giọng nói căng thẳng.\\nHơi thở gấp gáp, mạnh mẽ đến mức làm rung chuyển cả dương vật."
"1476" = "Từng giọt nước nhỏ xuống từ háng em như kéo thành sợi.\\nEo của Fukami lại bắt đầu đung đưa, cọ quậy."
"1484" = "Vì thế, Fukami đang lau người cho tôi.\\nTrong khi vẫn đang mặc nguyên bộ quần áo, đồ lót ướt sũng, mỏng tang."
"1496" = "Vượt qua dòng thác này, một lúc sau,\\nchỉ cần để thuyền trôi lững lờ theo dòng nước là được."
"1499" = "Tỏng——tỏng."
"1500" = "Để tránh làm văng những giọt nước thừa thãi, em ấy bảo tôi nằm xuống,\\nrồi ngồi lên trên, ra sức lắc lư eo, lau người cho tôi."
"1520" = "Ngay trước mắt tôi, là phần háng quần lót của Fukami đang banh rộng.\\nNó ướt sũng, ngậm đầy nước và dính chặt vào da."
"1533" = "Ba người……hay nói đúng hơn là, theo thỏa thuận thực tế giữa Fukami và Nagi,\\nsố lần hẹn hò được chốt lại là Fukami hai lần, Nagi một lần."
"1535" = "Màng nhĩ tôi rung lên dễ chịu bởi giọng nói đầy vui sướng,\\ntôi từ từ lột lớp vải đang dính chặt ra, cởi sạch phần dưới của Fukami."
"1546" = "Chiếc thuyền rung lắc dữ dội dù không phải ở chỗ nước chảy xiết.\\nPhản ứng đó khiến tôi nhận ra lời nói của mình thiếu sót trầm trọng."
"1553" = "（Liếm! Liếm——chụt——ngoạm!）"
"1561" = "Nói rồi, Fukami đứng thẳng lưng ở mũi thuyền.\\nDù đang vươn thẳng người, đôi gò má em vẫn dần ửng đỏ."
"1580" = "Dù độ dày có lẽ chưa đến vài milimet,\\nnhưng chiếc quần lót ướt sũng dính chặt này thực sự quá vướng víu."
"1581" = "Vì thế, bồn tắm ở đây cực kỳ lớn,\\nnên việc đun nước cũng mất khá nhiều thời gian——nghe nói là vậy."
"1588" = "Chỉ là vậy thôi, nhưng không hiểu sao\\ntôi lại cảm nhận được một sức ép khó tả."
"1651" = "（Rột——chụt! Nhóp nhép! Ực!）"
"1654" = "（Chụt——rột——liếm——liếm liếm liếm）"
"1655" = "（Nhóp nhép!!）"
"1659" = "（Ồ……）"
"1675" = "（Tõm——!!!）"
"1678" = "（Tròng trành!）"
"1681" = "（Liếm! Liếm! Liếm! Nhóp nhép!）"
```

## 凪ふかみ02 — 凪ふかみ02_凪の大会初挑戦！.txt.toml — 32/517 (6,2%)

- File: `凪ふかみ02_凪の大会初挑戦！.txt.toml` — route 07_Nagi_Fukami, 517 dòng script (115 thoại Nagi, 102 thoại Fukami, 83 thoại Soutetsu, 5 thoại Nakamura, 3 thoại trọng tài, 209 độc thoại Fukami). Nội dung: Nagi dự giải kiếm đạo lần đầu — Soutetsu huấn luyện, Fukami kể chuyện/hỗ trợ hậu cần; xung đột Thể Xá Lưu vs luật kiếm đạo (cấm thể thuật, cấm đâm, cấm chém chéo; chỉ được Trung Đoạn/Chính Nhãn); tập luyện trong bụi tre, sát khí.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 517/517 (287 dòng chỉ khác ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng). `[selections]` rỗng. Thẻ `%l` JP vs VN bằng nhau ở mọi dòng, 0 lệch. Không có bản sao file này (md5 `25803e1c333ba074a159e5e9f7d60aa1`).
- Phân loại (32): pronoun 21 (độc thoại Fukami "tôi"→"mình" 18 dòng: 2674, 2686, 2857, 2880, 2941, 2942, 2997, 3001, 3011, 3024, 3026, 3083, 3151, 3201, 3205, 3212, 3220, 3230; Soutetsu "tôi"→"anh" 3 dòng: 1508, 2243, 2248), gasp 5 (1470, 1471, 2082, 2688, 2771 — cả 5 từ sweep), terminology 3 (1962, 2482 "Taisha"→"Thể Xá Lưu"; 2429 "Seigan"/"Daijodan"→"Chính Nhãn"/"Đại Thượng Đoạn"), sfx 2 (2042 ぴきゃうっ "Ái da"→"Á!!", 2852 けらけら "cười khúc khích"→"cười ha hả"), consistency 1 (1511 "kami"→"kami-chan", khớp 1473).
- Sweep kiểm chứng: 5 mục cho file (1470, 1471, 2082, 2688, 2771), áp nguyên cả 5 sau khi kiểm chứng JP (lưu ý: fix của sweep cho 2771 dùng khoảng trắng thay cho `\n` của CSV3 — bản sửa đã giữ nguyên `\n` theo CSV3); tự quét toàn bộ っ không phát hiện gasp nào sweep bỏ sót.
- Soutetsu "anh" với Nagi/Fukami đúng toàn file trừ 3 dòng "tôi" đã sửa. Nagi gọi Fukami "cậu" (4 lần), không có "chị". Fukami tự xưng "tớ"/"mình" trong thoại giữ nguyên biến thể (tiền lệ 01/08b). 日ノ本→"Hinomoto" 1/1 đúng (2287); 残心→"tàn tâm" khớp tiền lệ 08a; 忠等部 là lỗi chính tả trong JP gốc (2134, 2331), VN dịch đúng, không sửa.
- Chi tiết đầy đủ: `audit-nagifukami02-REVIEW.md`; danh sách sửa: `audit-nagifukami02-wrong.json` (32 mục, khối TOML 32 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 32/32; lượt soát 2: 32/32, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 119 file / 5.581 dòng sai** (cơ sở 118 file / 5.549 dòng sai + 32 file này)

- Chờ Hieu: 次元流 → "Thứ Nguyên Lưu" hay "Thị Hiện Lưu"? (2280, 2377, 3109 — cả 3 dòng 次元流 trong toàn dự án đều ở file này; JP viết 次元流 đọc じげん, TW dùng 示現流); Nagi tự xưng trong thoại có thống nhất "tớ"/"mình"/"em" không (1862 "em" với Fukami; các dòng "tớ" 2026/2034/2123/2193/2205/2360/2363); 1491 đuôi って bỏ lửng ("——sao." hay "——thì…"); 2079 câu nói ngọng của Nagi (có giữ VN cũ "trả đũa lại nè, há miệng ra nào" không).
- Đính chính: ghi chú "Seki key 2299 dùng 'ông ngoại'" trong brief bị gán nhầm file — dòng Seki thật sự nằm ở file **凪ふかみ02_命の重さ.txt.toml key 2299**, không phải file này (file này không có dòng nào nhắc tới Seki; key 2299 ở đây là thoại Soutetsu không liên quan tới ông). Việc sửa "ông ngoại" thuộc về file 命の重さ khi tới lượt audit nó.

```toml
[script]
"1470" = "「——Ư」"
"1471" = "「——Ư」"
"1508" = "「……Gì đây, chỉ có mình anh bị cho ra rìa sao.」"
"1511" = "「……kami-chan? Fukami-chan ơiii!!」"
"1962" = "「Hiện tại thì cũng tạm ổn, nhưng ở hiệp thứ hai vừa nãy,\\nthói quen của phái Thể Xá Lưu đã bộc lộ. Em đã vác kiếm lên vai phải khi vung đấy.」"
"2042" = "「Á!!」\\n「Anh Soutetsu!」"
"2082" = "「Ư!!」"
"2243" = "「Anh không phiền đâu.\\n——Navi cũng nói là rất sẵn lòng đấy.」"
"2248" = "「Ừm. Từ giờ anh sẽ luyện tập với Nagi, nhưng mà——」"
"2429" = "「Kết hợp với bước chân, từ thế Chính Nhãn vung kiếm lên Đại Thượng Đoạn.\\nRồi không dừng lại mà đánh thẳng vào mặt thì kiếm của Nagi mới phát huy được.」"
"2482" = "「Căn bản và cũng là tuyệt kỹ của phái Thể Xá Lưu là chém chéo từ tư thế mở nửa người sang phải.\\nNhưng vì đó là đòn cấm, nên đường kiếm của Nagi bị hạn chế.」"
"2674" = "Nhưng bây giờ thì mình đã hiểu."
"2686" = "Thế rồi, nỗi sợ hãi tan biến đi mất.\\nBây giờ, chuyện gì vừa xảy ra……dù sợ, nhưng mình vẫn muốn biết."
"2688" = "Một mạch vung kiếm lên cao, rồi cứ thế lao vào đối thủ——Ư!?"
"2771" = "Bán khai, chắc có nghĩa là mở một nửa.\\nCơ thể của Nagi, đúng như cái tên, xoay nửa người lại——Ư!"
"2852" = "Nagi làm vẻ mặt giật mình,\\nrồi cười ha hả."
"2857" = "Góc nghiêng ấy, khiến mình thoáng chốc mê mẩn.\\nThật tĩnh lặng, thật xinh đẹp——ngay cả những giọt mồ hôi cũng lấp lánh như ngọc vậy."
"2880" = "Nếu chưa nhìn thấy Nagi-chan của ngày hôm nay,\\nchắc chắn mình đã thắc mắc \"Biện pháp an toàn á?\"."
"2941" = "Nagi-chan vốn rất khó chịu với điều đó, nhưng trọng tài đã tách họ ra——\\nNên mình đinh ninh rằng thế này là nắm chắc phần thắng rồi."
"2942" = "Không có tiếng đáp lại. Làm sao mà trả lời được cơ chứ.\\nNhưng mình biết, Nagi-chan vẫn nghe thấy rất rõ."
"2997" = "Mình ngồi thụp xuống!\\nSợ hãi vì nghĩ có thứ gì đó sắp tới, cơ thể mình cứng đờ không cử động nổi!"
"3001" = "Mình cũng vậy.\\nMình đã thở phào nhẹ nhõm."
"3011" = "Mình và Nagi-chan chợt chạm mắt nhau.\\nCùng gật đầu."
"3024" = "Qua giọng nói của anh Soutetsu, mình cũng cảm nhận được.\\nQuả nhiên, đây chính là cơ hội!!"
"3026" = "Việc mà mình có thể giúp.\\nHộp cứu thương, chanh ngâm mật ong, và nước uống thể thao."
"3083" = "Dù là việc nhỏ nhặt đến đâu,\\nmình tin chắc chắn cũng có việc mình có thể giúp được."
"3151" = "Bị nói là bắt bài...\\nlàm mình có cảm giác rất không lành."
"3201" = "Xoạt, âm thanh như dẫm lên lá khô.\\nPhù, tiếng thở hắt ra. Những âm thanh quen thuộc với đôi tai mình."
"3205" = "Chừng đó thì, mình cũng biết.\\nLà nói về tay, về cổ tay——Nhưng mà!"
"3212" = "Rất đáng sợ, chỉ cần chậm một giây thôi là sẽ bị đánh trúng,\\nnếu là mình, tuyệt đối không thể làm được."
"3220" = "Dù không hiểu các thuật ngữ chuyên môn,\\nnhưng mình cũng thấy rõ Nagi-chan đánh rất đẹp mắt!"
"3230" = "Quả không hổ danh là anh Soutetsu.\\nHình như mình cũng hiểu ra rồi."
```

## ハチロク07 — ハチロク07_延命.txt.toml — 64/499 (12,8%)

- File: `ハチロク07_延命.txt.toml` — route 01_Hachiroku, 499 dòng script (157 độc thoại, 92 thoại Olivy, 61 thoại Soutetsu, 53 thoại Paulette, 47 thoại Hachiroku, 41 thoại Điện xá Công chúa, 23 thoại Niiroku, 5 thoại Reina, 4 thoại Kisaki, 4 thoại Nagi, 3 thoại Hibiki, 3 thoại Fukami, 3 thoại Mayami, 3 thoại Akai). Nội dung: cuộc họp buổi tối về tương lai của Olivy — kiểm tra toàn diện hàng năm, kéo dài tuổi thọ Railord, lương và vai trò mới sau khi nghỉ lái tàu; Niiroku (Railord của Kuha 26, lái tàu Kiyoharu) xuất hiện, nghi ngờ về "cô gái quấn băng gạc" (Railord không có cộng cảm); Densha-hime tài trợ nghiên cứu kéo dài tuổi thọ và gợi ý "bí quyết sống khỏe cho Railord"; Olivy đồng ý chia sẻ kỹ thuật bảo trì đường ray và lái tàu; kết bằng cảnh đo thân nhiệt và tiếng bíp của nhiệt kế.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 499/499 (2 dòng 2299, 2386 chỉ khác ở chỗ TOML-2 làm phẳng \n thành khoảng trắng, đã biết). `[selections]` rỗng. Không có thẻ `%l` sai định dạng, không có thẻ VN tự thêm. Không có bản sao file này (md5 `4cd3b14b4f5365d86e1f0459692a8449`).
- Phân loại (64): thuật ngữ 53 (Điện xá Công chúa→Công chúa Tàu điện 26; Ohito/Ohigawa→Ohitoyo 12; Hoàng gia→Teitetsu 4 — 2490 mang 2 lỗi; Thẻ bảng→máy tính bảng 4; Mỹ→Minh Quốc 2; Nagi đại nhân→Bổn tiểu thư 1; thân chính/Kíp lái→thân bảo trì/thân vận hành 2; Lõi Lord→Lõi Railord 3), đại từ 7 (Soutetsu "tôi"→"anh" với Olivy 2418, Hibiki 2508, Niiroku 2829; Hachiroku "tôi"→"em" 2345, 2565, 2905; Fukami "em"→"cậu" với Nagi 2453), thân tộc 1 (Seki "ông nội"→"ông ngoại" 2679), gasp sweep 3 (2548, 2828, 3528), SFX 1 (3584 つぽっ "Bóp"→"Póc").
- Sweep kiểm chứng: 4 mục cho file, nhận 3 fix (2548, 2828, 3528) + 1 already-rendered (2292 "A!"); quét máy bổ sung: không còn gasp nào sweep bỏ sót (あっ→"A", あっ！？→"A!?", はうっ→"Hau", うんっ→"Vâng" đều là quy ước toàn dự án, đã kiểm chứng bằng CSV3).
- Soutetsu "anh" với Paulette/Hibiki/Olivy/Niiroku đúng sau khi sửa 3 dòng; "tôi" chỉ còn ở chỗ đúng (với Điện xá Công chúa 2513/2817, tự giới thiệu 2538, dạng nhóm). Hachiroku "em" nhất quán sau khi sửa 3 dòng. 53 dòng thuật ngữ sửa trực tiếp trong audit (theo tiền lệ ハチロク10 đã gộp) — KHÔNG thêm lại các key này vào hàng đợi thống nhất (liệt kê ở REVIEW §6).
- Chi tiết đầy đủ: `audit-hachiroku07-enmei-REVIEW.md`; danh sách sửa: `audit-hachiroku07-enmei-wrong.json` (64 mục, khối TOML 64 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 64/64; lượt soát 2: 64/64, 0 bỏ, 2 sửa — 3121 khôi phục thẻ %l, 3528 khôi phục \n).

**Tổng cộng sau file này: 120 file / 5.645 dòng sai** (cơ sở 119 file / 5.581 dòng sai + 64 file này)

- Chờ Hieu: 2679 (Seki "ông ngoại" — dòng Seki thứ 5, parent kiểm chứng lại nhóm "おじいちゃんたち" có phải Seki không); 2916–2918 (giọng ngọng của Hachiroku — giữ bản rõ nghĩa hay diễn ngọng); 2339 (xác nhận người nghe của Fukami là Olivy, không phải Nagi).
- REBASE (parent): snippet ghi cơ sở 118 file / 5.549 — đã rebase về 119 file / 5.581 sau khi gộp 凪ふかみ02 (tổng mới 120 file / 5.645).

```toml
[script]
1588 = "――6 năm qua. Những thiết kế mà Hibiki tạo ra,\\nđã thực sự kéo gần khoảng cách giữa chúng tôi và Công chúa Tàu điện một cách đáng kể."
1605 = "……Tôi nhìn vào tờ ghi chú lời khuyên của Công chúa Tàu điện."
1640 = "「——Tôi, đã mất thân bảo trì rồi.\\nthân vận hành. Chỉ còn lại cơ thể này thôi.」"
1662 = "「Chỉ là tên gọi tạm thôi. Một thứ không có tên chính thức――\\nLà 'thứ khiến \\x%lタブレット;#00ffc040;máy tính bảng%l;#; trở thành \\x%lタブレット;#00ffc040;máy tính bảng%l;#;'」"
2173 = "「Railord――Lõi?」"
2203 = "「Bộ phận Cơ khí \\x%lレイルロオド;#00ffc040;Railord%l;#; Teitetsu cũ ở Omiya――\\nNay là Viện nghiên cứu \\x%lレイルロオド;#00ffc040;Railord%l;#; Omiya, ta đang đầu tư vốn vào đó」"
2209 = "「Xin chào. Olivy là \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc,\\nbạn là kiểu Hinomoto nhỉ? \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của xe nào vậy?」"
2343 = "「A!? Xin cảm ơn ngài――hơn thế nữa, tôi xin lỗi.\\nChuyện nội bộ của chúng tôi đã làm mất thời gian quý báu của Công chúa Tàu điện――」"
2345 = "「A!? Cái đó――không phải, em, ừm thì」"
2382 = "「Ufufu, không có chi. Vậy thì,\\nvới tư cách là giám đốc Đường sắt Ohitoyo――tôi hỏi lại lần nữa nhé?」"
2390 = "「Hừm, vị đền chủ đó,\\ntừng là \\x%l運転士;#00ffc040;lái tàu%l;#; của Teitetsu sao~」"
2393 = "「Lần tới Olivy! Hãy đến chơi chuyến đi thuyền trên sông Kuma nha!\\nĐể chào mừng, Bổn tiểu thư đây sẽ đích thân chèo thuyền cho cậu!!」"
2399 = "「Việc kiểm tra toàn diện hàng năm được khuyến nghị cho quá trình vận hành của Olivy.\\nVới tài sản hiện tại của Đường sắt Ohitoyo thì không thể đáp ứng được.」"
2418 = "「Olivy cũng có kiến thức về kỹ thuật bảo trì đường ray mới nhất.\\nAnh cũng mong em có thể truyền đạt điều đó cho Đường sắt Ohitoyo.」"
2444 = "「Thứ khiến \\x%lタブレット;#00ffc040;máy tính bảng%l;#;――trở thành \\x%lタブレット;#00ffc040;máy tính bảng%l;#;」"
2451 = "「Khi nhận được yêu cầu từ Công chúa Tàu điện, giả sử cô Paulette,\\nkhông hỏi han gì Olivy mà cứ thế đáp ứng」"
2453 = "「Này, Nagi! Sao cậu lại nói chuyện đó lúc này chứ......」"
2487 = "「Dựa trên lời khuyên của Công chúa Tàu điện trong cuộc họp buổi sáng,\\nPaulette đã quyết định phải tổ chức thêm một cuộc họp nữa」"
2490 = "「Đường sắt Ohitoyo không giống như các công ty đường sắt khác,\\nkhông có sự kế thừa kinh nghiệm từ thời Teitetsu.」"
2508 = "「Anh cũng vậy」"
2529 = "「Tôi là. Niiroku. Từng là \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của\\ntàu điện tốc hành nguyên mẫu Kuha 26 thuộc Teitetsu cũ.」"
2532 = "「Kết quả kiểm tra lần trước của Olivy ở Omiya,\\ntôi muốn để Công chúa Tàu điện xác nhận」"
2533 = "「Tôi là Hachiroku. \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của\\n\\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; 8620 thuộc Đường sắt Ohitoyo.」"
2548 = "「Ư!!?」\\n「Trời ạ!」"
2561 = "「Vậy nên. ――Hồ sơ kiểm tra của Olivy,\\nđể Công chúa Tàu điện xem qua, có được không?」"
2565 = "「Xin lỗi ạ. Dù là lo lắng thì cũng phải biết cách truyền đạt nhỉ.\\nEm cứ lặp đi lặp lại cùng một sai lầm mãi thôi」"
2608 = "「Đúng vậy, Olivy. Hôm nay, sau khi bàn bạc với Công chúa Tàu điện,\\ntôi nghĩ tốt nhất là nên truyền đạt lại suy nghĩ của mình」"
2614 = "「Vậy…… sao ạ?\\nNếu Công chúa Tàu điện đã nói thế, thì tôi không ý kiến gì nữa」"
2679 = "「Ông ngoại và mọi người đi tham gia chuyến du lịch giải khuây của hiệp hội thuyền du lịch rồi.\\nNhưng mà, gọi điện lúc nào cũng được, ạ......」"
2695 = "「Đúng vậy. Lời khuyên của ngài ấy cũng rất chất lượng. Cả chúng tôi và Đường sắt Ohitoyo,\\nđều nhận được sự giúp đỡ rất nhiều từ ngài ấy.」"
2739 = "「Nếu thấy lãng phí, ta đã ngắt lời rồi. Việc được tận mắt chứng kiến\\nsự gắn kết bền chặt của tổ chức Đường sắt Ohitoyo, cũng là một điều tốt」"
2745 = "「Kiểm tra toàn diện hàng năm, với tiềm lực vốn của Đường sắt Ohitoyo\\nthì không thể nào thực hiện được――ngươi biết chứ?」"
2759 = "「Nếu vậy thì…… xem nào, tôi sẽ thưa với Công chúa Tàu điện,\\n'Xin ngài thứ lỗi cho lúc này'」"
2770 = "「Đúng là vậy nhưng――đi hỏi \\x%lレイルロオド;#00ffc040;Railord%l;#; mấy chuyện đó,\\nĐường sắt Ohitoyo đúng là……」"
2814 = "「Điều đó chứng tỏ,\\nhọ rất coi trọng Đường sắt Ohitoyo đấy」"
2817 = "「Vâng――tôi chỉ ghép lại từ những lời của Công chúa Tàu điện thôi ạ.\\nXin ngài cứ tùy ý sử dụng」"
2824 = "「Tài liệu lần này,\\ntôi nghĩ nên để Công chúa Tàu điện xem qua」"
2828 = "「Ư!!?」"
2829 = "「Không, anh thì——」"
2839 = "「Ý ngài là dù có cố gắng tái tạo…… hay chế tạo mới \\x%lタブレット;#00ffc040;máy tính bảng%l;#;,\\ncũng không thể thực hiện được――đúng không ạ?」"
2844 = "「Đương nhiên cũng có những vấn đề đó. Nhưng về mặt kỹ thuật thuần túy,\\ncũng bó tay. Hoàn toàn không thể tái tạo lại Lõi Railord được」"
2850 = "「Lõi Railord――là gì vậy ạ? Cái đó ấy」"
2905 = "「Không đâu. Trong quá trình tiếp xúc với Olivy, em mới nhận ra.\\n“Đường sắt” mà em biết, chỉ là một phần rất nhỏ bé mà thôi.」"
3121 = "Chắc là trong vô thức. Hachiroku chạm vào chiếc \\x%lタブレット;#00ffc040;máy tính bảng%l;#; trên cổ.\\n\\x%lタブレット;#00ffc040;Máy tính bảng%l;#;…… quả thực là một thứ vô cùng khó định nghĩa."
3135 = "Không, gần như chắc chắn rồi.\\nLà một \\x%lレイルロオド;#00ffc040;Railord%l;#; trong \\x%l運転体;#00ffc040;thân vận hành%l;#;."
3161 = "Có lẽ là vì giọng điệu quá đỗi thân mật với Công chúa Tàu điện."
3174 = "Chỉ bằng một câu nói vừa rồi, chỉ bằng nụ cười rạng rỡ ấy,\\ncũng đủ để truyền đạt rõ ràng đến Công chúa Tàu điện."
3294 = "Ngay khi tiếng đóng cửa vang lên,\\nánh mắt của Công chúa Tàu điện vụt――nheo lại sắc lẹm như lưỡi dao."
3310 = "Chuyển từ Đường sắt Mikan sang Đường sắt Ohitoyo――\\nQuyết định của chính mình, vào ngày hôm đó."
3410 = "Một cú ném thẳng vào giữa trọng tâm.\\nThì ra đây là phong cách Minh Quốc sao, tôi bất giác có suy nghĩ lệch lạc như vậy."
3412 = "Có lẽ cô bé đã sớm hiểu được,\\nai mới là người giữ két sắt của Đường sắt Ohitoyo."
3451 = "Đặt những câu hỏi khá sâu sát, trực tiếp với Công chúa Tàu điện――\\nĐến mức độ được phép làm như vậy."
3525 = "Chiếc quạt xòe ra cái phạch,\\nche đi khóe miệng của Công chúa Tàu điện."
3528 = "Dù đã nghe nói là \"chắc chắn sẽ hứng thú\",\\nnhưng tôi không ngờ lại đến mức này——Ư!!"
3531 = "Công chúa Tàu điện đã nghe kế hoạch vận hành Olivy từ Paulette,\\nvà dựa trên đó, ngài đã khuyên nên công bố sớm."
3532 = "Cạch, Công chúa Tàu điện khép quạt lại thật mạnh trong tích tắc,\\ntạo ra một âm thanh khô khốc."
3533 = "Lạch cạch, lạch cạch, chiếc quạt của Công chúa Tàu điện nhịp nhàng gõ nhẹ."
3534 = "Nhận lấy tập tài liệu từ bàn tay vươn ra ngoài khung hình,\\nCông chúa Tàu điện lật giở với tốc độ đáng kinh ngạc."
3535 = "Công chúa Tàu điện, bật cười vô cùng thích thú.\\nNhưng ngay sau đó, khóe miệng ngài đã bị chiếc quạt che khuất."
3536 = "Chỉ một khoảnh khắc――Công chúa Tàu điện nín thở."
3537 = "Xua đi nét u buồn thoáng hiện trong đôi mắt,\\nánh nhìn của Công chúa Tàu điện chuyển sang trái."
3538 = "Một cái quạt có vẻ đầy mãn nguyện.\\nĐôi mắt của Công chúa Tàu điện khẽ――nheo lại."
3540 = "Chiếc quạt nhỏ khẽ phe phẩy, mái tóc của Công chúa Tàu điện cũng đung đưa theo."
3584 = "（Póc）"
```

## ハチロク09 — ハチロク09_もくもくオリヴィ.txt.toml — 34/477 (7,1%)

- File: `ハチロク09_もくもくオリヴィ.txt.toml` — route 01_Hachiroku, 477 dòng script (độc thoại 169, Soutetsu 99, Hachiroku 86, Olivy 39, Fukami 19, bé Yuu 15, Niiroku 13, Nagi 13, Akai 10, Hibiki 9, mẹ của bé 5). Nội dung: chuyến tàu BBQ đầu tiên của Đầu máy số 9 mang tên Olivy — lễ tại ga suối nước nóng Ohitoyo, Soutetsu và Hachiroku đi tàu với tư cách vợ chồng (riêng tư), nướng thịt bò Aka-ou, bé Yuu (Misato Yuu) — đứa trẻ hay vẫy tay ở trạm chắn, Fukami đọc thông báo lần đầu, tới ga Yunoi, cảnh nhà tắm Tororyu-yu, chuyện về Hiyoko "Phượng Hoàng Lửa" ở Bảo tàng Đường sắt Omiya, kết bằng cảnh đêm hai người nắm tay nhau ngủ.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối về khóa (276 dòng chỉ khác ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng, đã biết). `[selections]` rỗng. Không có thẻ `%l` sai định dạng, không có thẻ VN tự thêm. Không có bản sao file này (md5 `a7aaca57dba45044b12d131baa097422`).
- Phân loại (34): thuật ngữ 20 (Ohimitera→Ohitoyo 7; Yui→Yunoi 5 + 2698 mang cả hai; Đường sắt Hoàng gia→Teitetsu 4; Densha Hime→Công chúa Tàu điện 2; Minh Quốc (Nước Mỹ)→Meriken 1 — 1606 furigana メリケン; thân máy bảo dưỡng→thân bảo trì 1), dịch sai nghĩa 8 ("cô bé"→"đứa bé" cho bé Yuu 5 — 1925, 1628, 1670, 2631, 2556; 2870 "Rất muốn làm theo"→"Rất muốn lên tiếng nhắc nhở"; 1053 "cho tôi xem"→"cho chúng tôi xem" theo TW 我們; 1951 "từ lâu rồi" bịa thêm), gasp sweep 3 (1648, 1675, 1678), lỗi chính tả 2 (1946 "chúng chúng ta"; 1599 "Q-Quả"→"Qu-Quả"), gloss thừa 1 (1508 bỏ "(Người phụ nữ Nhật Bản truyền thống)").
- Sweep kiểm chứng: 3 mục cho file, nhận cả 3 (1648, 1675, 1678); 1678 đã xử lý — VN dòng 2 KHÔNG lệch dòng, chỉ dòng 1 mất gasp (và thiếu dấu `」` đóng, fix bổ sung cả hai); quét máy bổ sung: không còn gasp nào sweep bỏ sót (1668/1649/1638 chỉ có dấu câu, JP không có っ; các っ khác đã được diễn đạt sẵn).
- Soutetsu "anh" với Hachiroku giữ nguyên 12 dòng (1702, 1688, 1859, 2028, 1802, 1073, 1724, 1883, 1578, 1734, 1861, 1545 + 1891, 2116) — register vợ chồng có chủ ý trong chuyến đi riêng tư (Hachiroku gọi "phu quân", Soutetsu gọi "suzu"); trước cảnh này Soutetsu vẫn "tôi" (1951). Key 2118 由衣 (địa danh Yui) giữ "Yui", KHÔNG đổi thành Yunoi. 20 dòng thuật ngữ sửa trực tiếp trong audit (theo tiền lệ ハチロク07/ハチロク10) — KHÔNG thêm lại các key này vào hàng đợi thống nhất.
- Chi tiết đầy đủ: `audit-hachiroku09-mokumoku-olivy-REVIEW.md`; danh sách sửa: `audit-hachiroku09-mokumoku-olivy-wrong.json` (34 mục, khối TOML 34 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 34/34; lượt soát 2: 34/34, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 121 file / 5.679 dòng sai** (cơ sở 120 file / 5.645 dòng sai + 34 file này)

- Chờ Hieu: phạm vi "anh" của Soutetsu với Hachiroku ở cảnh tắm (1073, 1724, 1883, 1578, 1734) và cảnh đêm (1861, 1545, 1891, 2116) — giữ toàn bộ "anh" ở nửa sau hay chỉ trong cảnh hẹn hò trên tàu; 2027 "bác Seki" — quyết định Seki = "ông ngoại" có áp dụng cho cách xưng hô của Soutetsu không; 1508/1879 日ノ本撫子 "Yamato Nadeshiko" có đổi thành "Hinomoto Nadeshiko" không; 1848 詠国 "Vịnh Quốc" có chuẩn hoá thành "Anh Quốc" không (TW: 英國).

```toml
"1006" = "——Và rồi, con tàu đã đến ga Yunoi."
"1031" = "……Mình đã mất đi thân bảo trì rồi. Giờ nói ra thì đã muộn màng——\\nKhông. Chuyện đó. Thực sự, đã quá muộn rồi."
"1037" = "……Việc tiến vào ga Suối nước nóng Ohitoyo, buổi lễ,\\nvà cả việc tiếp đón hành khách, đều được thực hiện vô cùng bài bản."
"1053" = "……Cảnh sắc mà ngày hôm đó, cha đã muốn cho chúng tôi xem.\\nTuyệt vời đến mức đó sao."
"1481" = "「Phượng Hoàng Lửa……chứng kiến giây phút cuối cùng của Teitetsu——」"
"1482" = "「Phượng Hoàng Lửa (Fushichou)! Tớ biết! Nổi tiếng lắm đó nha!\\n\\x%lレイルロオド;#00ffc040;Railord%l;#; đã chứng kiến giây phút cuối cùng của Teitetsu!」"
"1508" = "「Niiroku cũng là Yamato Nadeshiko nhỉ~!\\nThích thật đấy, tóc đen! Ghen tị quá đi!!」"
"1521" = "「Hôm nay, em sẽ là Suzu sao ạ? Rõ ràng là đang ở trên tàu của Đường sắt Ohitoyo,\\nhơn nữa, lại còn có cả cô Fukami ở đây nữa.」"
"1572" = "「Chân thành cảm ơn quý khách đã đồng hành cùng chúng tôi trên chặng đường dài.\\nTàu sắp đến ga Yunoi, ga cuối Yunoi ạ.」"
"1599" = "「Qu-Quả đúng là vậy nhỉ!\\nNếu còn mười phút nữa, thì, ừm, chúng ta phải chuẩn bị xuống tàu thôi.」"
"1606" = "「Và để bày tỏ sự tôn kính với quê hương của Đầu máy số 9 ạ.\\nThế này sẽ mang lại cảm giác Meriken hơn, quý khách có thấy vậy không ạ?」"
"1628" = "「Oa. Đứa bé đó, là bé Yuu——lúc nãy.」"
"1645" = "「Ưm.\\n……Thời Teitetsu, sao ạ?」"
"1648" = "「Ư!」"
"1670" = "「A! Nhắc mới nhớ, đứa bé đó cũng đã nói nhỉ.\\n『Nghi ngút khói vẫn chưa đủ』.」"
"1675" = "「Ư!?」\\n「Á!?」"
"1678" = "「Ư!?」\\nCái, cái gì, đã đến rồi sao!? Mới chớp mắt một cái thôi mà.」"
"1724" = "「Ừm. Chuyện về 『Kẻ kỳ quặc』,\\nmà Công chúa Tàu điện đã nhắc đến, anh đã nghe được rồi.」"
"1771" = "「Olivy-chan đã hoàn hảo rồi ạ. Về Tuyến Yunoi,\\nkhông còn gì tôi có thể dạy cho cô bé nữa đâu.」"
"1819" = "「Dù là trên tàu của Đường sắt Ohitoyo, nhưng hôm nay hoàn toàn là không gian riêng tư.\\nVé cũng đã mua đàng hoàng rồi.」"
"1925" = "「Ra là vậy——Cháu là đứa bé thường hay vẫy tay\\nở chỗ cửa hàng gần trạm chắn tàu đúng không?」"
"1946" = "「Không sao đâu ạ. Ngài Soutetsu.\\nVì ngày mai, chúng ta cũng sẽ luôn ở bên nhau mà.」"
"1951" = "「Không đâu, dù không có chuyện này thì chúng tôi cũng định đón khoảnh khắc này ở \\x%l客車;#00ffc040;toa hành khách%l;#; mà.\\nVì việc huấn luyện của tôi và Hachiroku, đã kết thúc rồi.」"
"2028" = "「Cái đó——ở Đế Đô thì sao?\\nThời Teitetsu, em đã từng nhìn thấy những cảnh sắc tuyệt vời nào qua cửa sổ?」"
"2029" = "「Kính thưa quý khách, cảm ơn quý khách hôm nay đã lên chuyến tàu BBQ của Đường sắt Ohitoyo,\\n『Olivy Nghi Ngút Khói』 ạ.」"
"2030" = "「Kính thưa quý khách, cảm ơn quý khách đã đồng hành cùng chuyến đi.\\nKhoảng mười phút nữa, tàu sẽ đến ga cuối, ga Yunoi ạ.」"
"2100" = "「Gì ấy nhỉ~, cái mà, Công chúa Tàu điện đã nói ấy.」"
"2116" = "「Tất nhiên rồi. Những \\x%lレイルロオド;#00ffc040;Railord%l;#; xuất sắc như em hay Olivy,\\nĐường sắt Ohitoyo chắc chắn cũng không muốn đánh mất đâu.」"
"2556" = "Đôi mắt của đứa bé sáng long lanh."
"2631" = "Nếu như mong đợi sự 『nghi ngút khói』 bay qua cửa sổ,\\nthì điểm đó, chắc chắn sẽ không thể khiến đứa bé hài lòng được."
"2698" = "Tuy lúc xuất phát có hơi đáng lo, nhưng đoạn Ohitoyo - Yunoi là một tuyến đường bằng phẳng.\\nHơn nữa, giữa chừng không hề dừng đỗ, Đầu máy số 9 cũng không chạy với tốc độ cao."
"2831" = "Vui mừng là vậy, nhưng mặt khác, tôi cũng cảm thấy có chút cô đơn.\\nDù không có chúng tôi, Tuyến Yunoi vẫn sẽ tiếp tục hoạt động."
"2835" = "Dù vô cùng thoải mái, nhưng với tư cách là nhân viên của Đường sắt Ohitoyo,\\ntôi vẫn hơi bận tâm việc các ghế không được lấp đầy."
"2870" = "（Chú ý. Cô ấy rất muốn lên tiếng nhắc nhở.\\nNhưng mà——đang chờ đợi——để họ tự nhận ra——a!）"
```

## ハチロク03 — ハチロク03_冥国式レイルロオド.txt.toml — 58/490 (11,8%)

- File: `ハチロク03_冥国式レイルロオド.txt.toml` — route 01_Hachiroku, 490 dòng script (178 độc thoại, 99 thoại Soutetsu, 85 thoại Olivy, 66 thoại Hachiroku, 25 thoại Paulette, 23 thoại Hibiki, 7 thoại Nagi, 6 thoại Reina, 1 thoại Fukami). Nội dung: ngày đầu tiên của Olivy ở Ohitoyo — chào hỏi buổi sáng, thống nhất cách gọi tên, Hachiroku xin lỗi vì đã đối xử với Olivy như trẻ con, ăn sáng (đập than), đến công ty (Olivy xin lỗi Paulette, nhận nhiệm vụ đi theo chuyến tàu + chạy thử Ⅸ号), giải thích "kiểu Meriken" (Minh Quốc) vs "kiểu Hinomoto", phanh khẩn cấp vì hươu, Hachiroku tắt đèn pha theo cộng cảm "Off the light" của Olivy, kết bằng cảm xúc tuyệt vọng đen tối của Olivy qua cộng cảm.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 490/490 (272 dòng chỉ khác ở chỗ TOML-2 làm phẳng \n thành khoảng trắng, đã biết). `[selections]` rỗng. Không có thẻ `%l` sai định dạng (1 dòng VN tự thêm thẻ: 2127 機関庫, gloss đúng, chỉ ghi nhận). Không có bản sao file này (md5 `4e718f528c5de0e6aca78a3e53094ec7`).
- Phân loại (58): thuật ngữ 32 (Minh Quốc/Meriken 19 — furigana メリケン→"Meriken" 4: 2694, 2697, 2475, 2083; còn lại→"Minh Quốc" 15; Ohito→Ohitoyo 7; Yui→Yunoi 2 dòng riêng; Teitetsu 1; 凪さま→"Bổn tiểu thư" 3), đại từ 10 (Soutetsu "tôi"/"cô"→"anh"/"em" với Olivy 9: 1988, 2023, 2042, 2044, 2112, 2300, 2345, 2383 + 2315 kiêm; Hibiki "chị"→"em" với Olivy 1: 2370), đại từ + thuật ngữ 2 (2315, 1993 — đều kiêm Yui), gasp sweep 9, sai nghĩa 2 (2426: "hãy kiểm tra buồng lái" bịa thêm — sửa "cứ ở trong buồng lái" theo TW; 2646: 庫内整理 "nhà kho"→"trong kho đầu máy"), lỗi nhỏ 1 (2479: "đại lội tắm" lỗi đánh máy + "gấp trăm lần"→"gấp hàng trăm lần"), SFX 2 (3428, 3429: パンっ "(Đập tay!)"→"(Bốp!)").
- Sweep kiểm chứng: 9 mục cho file, nhận cả 9 (1528, 2124, 2125, 2165, 2167, 2168, 2629, 2684, 3078); quét máy bổ sung: không còn gasp nào sweep bỏ sót (các っ còn lại đều đã diễn đúng hoặc là っ nhấn mạnh cuối câu/phó từ).
- Soutetsu "anh" với Olivy đúng sau khi sửa 9 dòng (+ 2315); "tôi" chỉ còn ở chỗ đúng (với Hachiroku 2039/2216/2386/2368, độc thoại, dạng nhóm). Hachiroku "em"/"chị" với Olivy đúng sau khi sửa 1993. Hibiki "em" với Olivy đúng sau khi sửa 2370. Olivy tự xưng "tôi" (6 dòng) và gọi Soutetsu "cậu" (2680) giữ nguyên theo tiền lệ ハチロク14/06.
- Yui→Yunoi đã sửa 5 dòng trong audit này (1551, 2449, 2315, 3272, 1993) theo thuật ngữ đã chốt — KHÔNG thêm lại vào hàng đợi thống nhất. Ohito→Ohitoyo đã sửa 7 dòng, Minh Quốc/Meriken 19 dòng, Teitetsu 3359, thân vận hành/thân bảo trì 1984, Bổn tiểu thư 3 dòng — KHÔNG thêm lại vào hàng đợi thống nhất (liệt kê ở REVIEW §6).
- Chi tiết đầy đủ: `audit-hachiroku03-meikoku-REVIEW.md`; danh sách sửa: `audit-hachiroku03-meikoku-wrong.json` (58 mục, khối TOML 58 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 58/58; lượt soát 2: 58/58, 0 bỏ, 0 sửa giá trị).

**Tổng cộng sau file này: 122 file / 5.737 dòng sai** (cơ sở 121 file / 5.679 dòng sai + 58 file này)

- Chờ Hieu: 日ノ本 "Hinamoto" còn 10 dòng (2510, 2412, 2585, 1580, 1532, 2084, 3115, 2503, 2454, 2399) — đợt thống nhất (brief ghi ×9, đếm thực tế là 10); 2149 fa/fu ngáp ("Haa~"/"Hafaa~" — áp quy tắc ふぁ→"phà" hay giữ nguyên?); 2680 Olivy gọi Soutetsu "cậu" (vs "anh" ở 2589/2663 — có thống nhất thành "anh" không?); 運転体 "thân vận hành" (1984) chờ đợt thống nhất chốt một dạng toàn dự án ("thân vận hành" vs "thân lái" vs "kíp lái").

```toml
[script]
1528 = "\"Olivy đã bị đối xử như thế nào ở Đường sắt Mikan\"\\n——Ư!"
1551 = "「Có vẻ như bên trong buồng lái cũng không có vấn đề gì.\\nVậy thì chúng ta hãy nhanh chóng tăng tốc chạy bù giờ đến Yunoi thôi ạ.」"
1580 = "「……\\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc khác biệt rất lớn so với \\x%lレイルロオド;#00ffc040;Railord%l;#;\\nkiểu Hinamoto, kiểu Anh hay kiểu Đức, họ thường xuyên thay ca làm nhiệm vụ ạ.」"
1984 = "「Không có \\x%l運転体;#00ffc040;thân vận hành%l;#; hay \\x%l整備体;#00ffc040;thân bảo trì%l;#;, chỉ có một cơ thể duy nhất khiến tôi rất ngạc nhiên.\\nĐó là do đầu máy hơi nước Minh Quốc——không phải」"
1988 = "「Không chỉ thao tác kiểm tra máy móc nhanh nhẹn, mà chỉ thị \\x%l投炭;#00ffc040;thêm than%l;#; cũng rất chính xác,\\nnên anh cứ tưởng em có nhiều kinh nghiệm làm nhiệm vụ trên dòng 8620——đầu máy hơi nước của Teitetsu chứ.」"
1993 = "「Không cần đâu ạ. Chỉ cần chị có lòng là được rồi.\\nDù sao thì đây cũng là chuyến đi đầu tiên của Olivy trên tuyến Yunoi mà.」"
2023 = "「Hôm nay em đã giúp đỡ rất nhiều.\\nCũng không hẳn là quà cảm ơn, nhưng nếu em thích thì dùng thử xem?」"
2042 = "「Olivy, em từng làm nhiệm vụ trên dòng 8620 rồi sao?」"
2044 = "「Em không sao——…………chứ?」"
2076 = "「Được sản xuất vào năm Minh Trị 45. Do hãng Aldwin Locomotive Works\\ncủa Minh Quốc chế tạo.」"
2083 = "「Lúc nãy cũng có nhắc đến, cái gọi là kiểu Meriken đó——」"
2112 = "「Nhưng mà, lúc nãy,\\nanh nghe thấy giọng em có vẻ rất đau đớn——」"
2124 = "「Ư!!?」"
2125 = "「Ư!?」"
2165 = "「Ư!!」"
2167 = "「Ư!!!!」"
2168 = "「Ư!?」"
2198 = "「Au~, Bổn tiểu thư đây xui xẻo quá đi mất á!」"
2238 = "「À. Để anh giới thiệu lại bản thân nhé.\\nChào mừng đến Ohitoyo, Olivy. Anh là Migita Soutetsu.」"
2283 = "「Olivy mới là người cần giúp đỡ! Mong mọi người giúp đỡ nha!\\nOlivy sẽ cố gắng để trở nên yêu thích Ohitoyo thật nhiều!」"
2300 = "「Em cứ nghỉ ngơi cho khỏe đi.\\nNếu có gì cần hỏi, ngày mai anh sẽ xác nhận lại sau.」"
2315 = "「Nếu mọi chuyện suôn sẻ đến đó, trước tiên em sẽ bắt cặp với anh,\\nlái thử đầu máy số 9 trên tuyến Yunoi. Nếu không có vấn đề gì thì」"
2341 = "「Là kiểu Minh Quốc ạ.\\nTrong trường hợp này, ý cô ấy là \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc đó ạ.」"
2345 = "「Là vậy đó. Anh cũng sẽ đi theo với tư cách là \\x%l機関士;#00ffc040;lái tàu%l;#; hướng dẫn.\\nCuối cùng em sẽ bắt cặp với ai thì còn phải dựa vào đánh giá tổng hợp nữa.」"
2370 = "「Em cũng rất hoan nghênh cách gọi đó!\\nMột lần nữa mong được giúp đỡ nhé, Olivy!」"
2373 = "「Với tư cách là Giám đốc của Công ty Cổ phần Đường sắt Ohitoyo.\\nTôi xin chấp nhận lời xin lỗi của cô Olivy.」"
2383 = "「Anh cũng không rành những người khác nên không dám khẳng định——\\nNhưng có lẽ, ở đâu cũng vậy thôi.」"
2388 = "「Em cũng nghe nói rằng ở Hokkaido thời kỳ đầu khai phá, do đất đai rộng lớn và mật độ vận chuyển thấp nên họ đã áp dụng kiểu Minh Quốc làm hình mẫu ạ.」"
2389 = "「Ở Minh Quốc, như vậy chắc là đủ rồi.\\nLãnh thổ rộng lớn, mật độ vận chuyển chắc chắn cũng khá thưa thớt.」"
2399 = "「Nên đầu máy hơi nước và \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc,\\nđã không thể trở thành hình mẫu cho kiểu Hinamoto sao.」"
2426 = "「Có sao hay không thì vẫn chưa biết được đâu ạ.\\nNgài Soutetsu cứ ở trong buồng lái ạ. Hibiki, hãy đưa em đi xem thử.」"
2433 = "「Em bị ngã rồi va đập vào đâu à?」"
2437 = "「Vâng. Quốc gia đã lấy kiểu Anh làm hình mẫu, các tuyến đường sắt tư nhân lớn\\ncũng chủ yếu dùng kiểu Đức và Anh. Kiểu Minh Quốc vốn dĩ đã là thiểu số rồi.」"
2449 = "「Không, trong chuyến chạy làm quen Tuyến Yunoi, Hachiroku cũng sẽ đi cùng.\\nỞ Đường sắt Mikan, không có chuyện \\x%lレイルロオド;#00ffc040;Railord%l;#; tiền nhiệm đi cùng sao?」"
2456 = "「Bổn tiểu thư đây có hơi bực mình một tẹo,\\nnhưng mà đã xin lỗi rồi thì tha cho á! Cho trôi tuột đi hết luôn á!」"
2458 = "「Thì Bổn tiểu thư đây! Sẽ bắt cặp với Bổn tiểu thư để làm nhiệm vụ á!」"
2468 = "「Chào mừng đến với Ohitoyo. Và, chào mừng đến với Đường sắt Ohitoyo!\\nTừ nay về sau, mong cô giúp đỡ nhiều hơn!」"
2473 = "「Không có đâu nha! Đầu máy hơi nước đang hoạt động của Đường sắt Mikan, đầu máy số 9…… thì\\nđã ở Ohitoyo rồi, nên giờ chỉ còn \\x%lC56;#00ffc040;C56%l;#; 99 và chiếc mới đến thôi.」"
2475 = "「Không có không có nha. Olivy chỉ luôn đi với đầu máy số 9 thôi.\\nUổng phí ghê ha? Dù gì cũng cất công mang danh kiểu Meriken mà.」"
2479 = "「Vâng. Là nhà tắm lớn với suối nước nóng thiên nhiên chính hiệu đó ạ.\\nTuyệt vời hơn gấp hàng trăm lần so với nước đun sôi ở các cơ sở nhà ga tiêu chuẩn đấy ạ.」"
2540 = "「Những cô bé kiểu Minh Quốc không được tối ưu hóa theo kiểu như vậy.\\nĐổi lại, họ có thể bắt cặp với bất kỳ ai và lên bất kỳ toa xe nào ngay lập tức.」"
2541 = "「Đầu máy hơi nước Minh Quốc.」"
2585 = "「Đúng vậy. Đó là đặc điểm lớn nhất của \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc.\\nVốn dĩ, tư tưởng thiết kế của họ đã khác với kiểu Hinamoto, kiểu Anh hay kiểu Đức rồi.」"
2623 = "「Đó chính là điểm mạnh của đầu máy hơi nước Minh Quốc đấy.」"
2629 = "「Ư!」\\n「Không phải đâu ạ!」"
2636 = "「Nói cách khác, những \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc như Olivy,\\ncó thể bắt cặp với bất kỳ Master——à không, bất kỳ \\x%l機関士;#00ffc040;lái tàu%l;#; nào sao?」"
2646 = "「Vậy, Olivy nên bắt đầu từ công việc gì đây?\\n\\x%l罐磨;#00ffc040;Cọ rửa lò hơi%l;#;? Dọn dẹp trong kho đầu máy?」"
2684 = "「Ngài Soutetsu!」「Phanh khẩn cấpppp!!!!」\\n「Ư!!!」"
2694 = "「Meriken?」"
2697 = "「OK đã rõ! Bắt cặp với ai cũng được hết á!\\nVì Olivy là kiểu Meriken mà!」"
3078 = "Chắc hẳn Olivy cũng đang tập trung cao độ.\\nÁnh mắt cô ấy như xuyên thấu lưng tôi, nhưng nếu cứ giữ vững phong độ này thì——Ư!"
3115 = "Ở kiểu Hinamoto, hầu hết đều buộc phải bỏ đi.\\nNhưng nếu là kiểu Minh Quốc, thì không cần lo lắng về việc tái sử dụng."
3272 = "Để được như vậy, trước tiên phải đến Yunoi đã.\\nSau đó quay trở lại Ohitoyo!"
3317 = "Nhỡ may tôi làm hỏng việc, khiến cô ấy nghĩ \"Đường sắt Ohitoyo chỉ đến thế này thôi sao\"\\nthì e rằng cũng chẳng tốt đẹp gì cho Olivy."
3351 = "Nhắc mới nhớ, lúc nãy cũng có nhắc đến kiểu Minh Quốc gì đó."
3359 = "\\x%lレイルロオド;#00ffc040;Railord%l;#; chiếc đầu tiên, của mẫu 8620 thuộc Teitetsu đầy vinh quang,\\nchiếc \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; sản xuất hàng loạt trong nước đầu tiên."
3428 = "（Bốp!!）"
3429 = "（Bốp!）"
```

## ハチロク09 — ハチロク09_採決.txt.toml — 39/471 (8,3%)

- File: `ハチロク09_採決.txt.toml` — route 01_Hachiroku, 471 dòng script (độc thoại 207, Soutetsu 110, Hachiroku 40, Hibiki 22, Paulette 22, Kisaki 18, Reina 17, chủ tọa 11, nữ nghị sĩ 8, nghị sĩ trung kiên 7, Urakami 3, Kon 2, chim sẻ 2, Nagi 1, Fukami 1). Nội dung: ngày bỏ phiếu quyết định ở hội đồng thành phố Ohitoyo — Paulette giải trình dự toán ngân sách bổ sung và tuyên bố từ chức, Soutetsu làm nhân chứng về tàu BBQ 8620, Kisaki chất vấn về tính tái hiện của việc thay khung gầm, Hachiroku phát biểu về các tuyến đường sắt Kyushu, dự toán thông qua, tiệc mừng, kết bằng cảnh đêm ở nhà xe đầu máy với Reina, Kon và bầy chim sẻ.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối về khóa (297 dòng chỉ khác ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng, đã biết). `[selections]` rỗng. Không có thẻ `%l` sai định dạng. Không có bản sao file này (md5 `df8fdf27838f6b6d01625020164b4e28`).
- Phân loại (39): thuật ngữ 29 (Ohimitera→Ohitoyo 24 dòng / 25 lần; 湯医線→Tuyến Yunoi 1 — 1818 mang cả hai; 運転鞄/鞄→"túi công tác" 4; gloss 帝鉄 "Đường sắt Hoàng gia"→"Đường sắt Đế quốc" 1), gasp sweep 4 (2452, 2453, 2454, 2649), SFX 3 (3334, 1473 vỗ tay "Lộp bộp"→"Bốp"; 1530 すぅ "Su"→"Suu"), đại từ 1 (2064 Hachiroku gọi Fukami "cô"→"em"), dịch sai nghĩa 1 (2097 Kisaki bịa "đùa à"), thẻ %l 1 (2288 gỡ thẻ VN tự thêm trên 静態保存).
- Sweep kiểm chứng: 4 mục cho file, nhận cả 4 (2452, 2453, 2454, 2649); quét máy bổ sung: không còn gasp nào sweep bỏ sót (1945/1946 ケンっ → "Keng!"; 1989 ひゃっ → "hya"; 1990 ちゅんくっ → "Chiếp chiếp!"; các っ khác đã được diễn đạt sẵn).
- Soutetsu "anh" với Hachiroku GIỮ NGUYÊN 5 dòng (1870, 2002, 2189, 2190, 2230) — cùng câu hỏi phạm vi như cờ もくもくオリヴィ, chờ Hieu (2190 đã sửa thuật ngữ, giữ "anh"). "bọn anh" 2240 giữ theo quy tắc dạng nhóm; Kisaki "Tôi" 2115 giữ (phát biểu trước nhóm). 29 dòng thuật ngữ sửa trực tiếp trong audit (theo tiền lệ ハチロク03/ハチロク07/ハチロク09_もくもくオリヴィ) — KHÔNG thêm lại các key này vào hàng đợi thống nhất.
- Chi tiết đầy đủ: `audit-hachiroku09-saiketsu-REVIEW.md`; danh sách sửa: `audit-hachiroku09-saiketsu-wrong.json` (39 mục, khối TOML 39 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 39/39; lượt soát 2: 39/39, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 123 file / 5.776 dòng sai** (cơ sở 122 file / 5.737 dòng sai + 39 file này)

- Chờ Hieu: phạm vi "anh" của Soutetsu với Hachiroku (1870, 2002, 2189, 2190, 2230) — giữ toàn bộ "anh" trong cảnh riêng tư hay sửa thành "tôi"; "Anh Migita" với Soutetsu (1937, 1825, 2449) hay "ngài Migita"; 2411 民由連 "Đảng Dân Do" hay "Đảng Dân Hữu" (TW: 民友連); 持株会社 "công ty cổ phần" toàn dự án (10 dòng / 4 file) có đổi thành "công ty holding" trong đợt thống nhất không.

```toml
"1473" = "Bốp, bốp. Tiếng vỗ tay đầu tiên, là từ Kisaki.\\nChẳng mấy chốc, nó đã vang lên từ khắp hội trường, từ tất cả những đôi bàn tay."
"1530" = "「……Suu……suu.」"
"1818" = "「Những tuyến đường sắt còn sót lại ở Kyushu,\\nkhông chỉ có Tuyến Yunoi của Đường sắt Ohitoyo đâu ạ.」"
"1855" = "「Tuy nhiên, lại có vấn đề về nhân sự. Nhìn vào giới chính trị,\\nOhitoyo có rất nhiều nhân tài xuất chúng, nhưng mà——」"
"1868" = "「Nằm ở khu vực lân cận——đúng rồi, ví dụ như Đường sắt Mikan,\\nnếu chúng ta khôi phục lại tuyến đường giữa Ohitoyo và Yatsushiro, thì có thể kết nối được với họ.」"
"1912" = "「Ra là vậy……phân bổ phương tiện đến các nơi——và rồi, tập trung những trang thiết bị, nhân lực\\nchuyên môn hóa cho việc bảo trì, sửa chữa SL về Ohitoyo.」"
"2017" = "「Vì vậy, vì sự phát triển tốt đẹp hơn của cả chính trị và kinh tế Ohitoyo,\\ntôi đã quyết định rằng việc từ chức thị trưởng sẽ là lựa chọn tốt hơn.」"
"2064" = "「Th, thế nào——em hỏi vậy thì……」"
"2066" = "「Ngay phía Nam……Hóa ra nó lại nằm gần Ohitoyo đến thế này sao.」"
"2097" = "「Khôi phục tuyến đường, cậu Soutetsu.\\nNói thì nghe dễ dàng thế thôi.」"
"2105" = "「Với tư cách là Quê hương của hơi nước Ohitoyo, chúng ta sẽ liên kết tất cả các nguồn tài nguyên lại với nhau.\\nĐó là điều mà chỉ Ohitoyo, chỉ đường sắt mới có thể làm được.」"
"2107" = "「Em chỉ đang giúp đỡ những việc mà em nghĩ là tốt nhất cho Ohitoyo thôi.」"
"2112" = "「Tôi là Houshou Kisaki, Giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto.」"
"2128" = "「Nhân dịp này, chúng ta sẽ tiếp tục phần hỏi đáp liên quan.\\nHội Tương lai Ohitoyo. Nghị sĩ Niitsu.」"
"2164" = "「Đúng vậy nhỉ. Trong cuộc họp hội đồng hôm nay, tương lai của đứa bé đó, 8620——\\nKhông, là tương lai của chính Ohitoyo sẽ được định đoạt.」"
"2190" = "「Ví dụ như……đúng rồi, giả sử anh muốn nhờ chị Mayami,\\nquản lý toàn bộ mảng rượu shochu Kuma trong thành phố Ohitoyo.」"
"2220" = "「Do đó, chúng ta sẽ hồi sinh các tuyến đường sắt lấy Ohitoyo làm trung tâm,\\nvà tạo ra một mô hình tập trung vận hành SL tại đó.」"
"2282" = "「\\x%l台枠;#00ffc040;Khung gầm%l;#; được thay thế, cũng vẫn chỉ là những bộ phận cũ kỹ.\\nPhía Đường sắt Ohitoyo phụ trách kiểm tra bảo dưỡng, đã bỏ sót những hư hỏng của \\x%l台枠;#00ffc040;khung gầm%l;#;.」"
"2284" = "「Và trung tâm của sự kết nối đó……chính là Ohitoyo.」"
"2288" = "「Nếu tính cả những chiếc đang được lưu tĩnh,\\nthì chỉ tính riêng trong Kyushu, tôi nghĩ số lượng còn gấp vài lần như thế.」"
"2296" = "「Thành phố của SL……của hơi nước——\\nKhông, đúng rồi——Quê hương của hơi nước, Ohitoyo.」"
"2323" = "「Biến Ohitoyo thành ga xuất phát cho du lịch SL. Từ \\x%l8620;#00ffc040;8620%l;#; đổi chuyến,\\nđể có thể đi du lịch khắp Kyushu bằng SL. Chúng ta sẽ tạo ra một tương lai như vậy.」"
"2452" = "「Ư!」"
"2453" = "「Ư!!?」"
"2454" = "「Ư!?」"
"2649" = "Các kỹ thuật viên ở Kokura cũng vậy, và cả những kỹ sư\\ncủa bộ phận hơi nước thuộc Công ty Xe lửa Hinomoto, nơi được cho là đã bị đóng cửa nữa——Ư!"
"2672" = "Một giọng nói, phát ra từ chiếc túi công tác."
"2792" = "Có lẽ do rượu vang, hai má cô ấy khá ửng đỏ,\\ntrên tay đang cầm một tấm bản đồ tuyến đường, có vẻ như là từ thời \\x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#;."
"2804" = "Vì tôi tin rằng, điều đó sẽ tạo ra một tương lai tốt đẹp hơn cho Ohitoyo……\\nVà vì tôi mong muốn, Hachiroku sẽ sống ở đó."
"2899" = "Từ trong chiếc túi công tác, phát ra một giọng nói nghẹn lại."
"2900" = "Từ trong chiếc túi công tác, truyền ra một giọng nói trầm thấp——\\nNhưng lại chứa đựng sự vui sướng và tự hào của Hachiroku."
"2923" = "Dù có thêm tiền trợ cấp vào tình hình tài chính hiện tại của Đường sắt Ohitoyo,\\nthì nói thật, việc đáp ứng được chi phí đó……là cực kỳ khó khăn."
"2952" = "Khi tôi mở túi công tác và ôm cô ấy lên,\\nHachiroku vẫn giữ nguyên tư thế đó, lớn tiếng nói."
"3021" = "Cuộc họp hội đồng thành phố Ohitoyo, thẩm định ngân sách bổ sung của ủy ban ngân sách.\\nBởi vì cuộc bỏ phiếu sẽ được diễn ra."
"3062" = "Để không nhìn nhận sai lầm về tương lai của Ohitoyo, nhằm thúc đẩy các cuộc tranh luận sôi nổi hơn,\\nviệc ông ấy chấp nhận mức độ sai lệch đó, cũng không có gì lạ."
"3063" = "Để xây dựng một tương lai tốt đẹp hơn cho Ohitoyo——\\nMột hành động vô tư, chỉ nhắm vào một mục đích duy nhất đó."
"3070" = "Rượu shochu, suối nước nóng, \\x%l蒸気機関車;#00ffc040;Đầu máy hơi nước%l;#;——Ohitoyo, ngay tại thời điểm này,\\ncũng đã là một thành phố xứng đáng được gọi là \"Quê hương của hơi nước\" rồi."
"3196" = "Mà là một cuộc thi, để tìm ra giải pháp tối ưu nhất\\nnhằm xây dựng một Ohitoyo tốt đẹp hơn."
"3334" = "（Bốp bốp bốp bốp）"
```

## 凪ふかみ04 — 凪ふかみ04_ふかみの決意.txt.toml — 94/474 (19,8%)

- File: `凪ふかみ04_ふかみの決意.txt.toml` — route 07_Nagi_Fukami, 474 dòng script (độc thoại 151, Fukami 149, Soutetsu 44, Nagi 43, Hibiki 29, Reina 28, Paulette 21, ông già 4, nhân viên công ty 2, trẻ em 2, ông chú 1). Nội dung: ngày đầu tiên Fukami làm nhân viên nhà ga ở Ohitoyo — buổi sáng làm nhiệm vụ cùng Soutetsu và Nagi, học việc, dọn nhà vệ sinh và bàn chuyện “nhìn nhà vệ sinh là biết nhà ga”, chiếc ghế đá bên bờ biển Yatsushiro, hồi tưởng chuyến đi đường sắt Mikan, Fukami xin được trở thành “người đồng đội thực sự của đường sắt Ohitoyo — trưởng tàu!”, kết bằng độc thoại về việc muốn bước vào chữ “chúng ta” của Soutetsu và Nagi.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối về khóa (0 lệch). `[selections]` rỗng. Không có thẻ `%l` sai định dạng. Không có bản sao file này (md5 `cb4cdb1d355ee5b597970e389848a97d`).
- Phân loại (94): đại từ 79 (độc thoại Fukami tôi/em→mình 67; đối thoại 12 — Fukami tự xưng “chị” sai 4: 2137, 2143, 2165, 2240; Fukami “em” với Nagi 2: 2158, 2178; nhóm “bọn chị”/“bọn em” sai 3: 2262, 2438, 2478; Fukami “em” với Reina 2: 2442, 2514; nhất quán trong dòng 1: 2622), thuật ngữ 13 (Ohito→Ohitoyo 7 dòng / 8 lần; 定期券 “vé tháng”→“vé định kỳ” 3; 凪さま→“Bổn tiểu thư” 1; まいてつ→“giới chủ tàu” 1; gloss “Kiha”→“KiHa” 1 + 3131 gộp trong dòng đại từ), dịch sai nghĩa 2 (2596 bịa “ảnh hưởng”; 3296 mất chuyển chủ ngữ).
- Sweep kiểm chứng: 0 mục cho file này; quét máy bổ sung 6 đoạn JP kết bằng っ đều đã diễn đạt sẵn (2130, 2131, 2148, 2167, 2322, 2644) — 0 gasp sweep bỏ sót. Không có dòng cười nào bị dịch thành tiếng rên; 1 dòng fa/fu (2177) để đợt thống nhất, không tính vào 94.
- 13 dòng thuật ngữ sửa trực tiếp trong audit (theo tiền lệ ハチロク03/ハチロク07/ハチロク09_採決) — KHÔNG thêm lại các key này vào hàng đợi thống nhất.
- Chi tiết đầy đủ: `audit-nagifukami04-fukami-no-ketsui-REVIEW.md`; danh sách sửa: `audit-nagifukami04-fukami-no-ketsui-wrong.json` (94 mục, khối TOML 94 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 94/94; lượt soát 2: 94/94, 0 bỏ, 1 sửa — 3190 “Tôi cũng” đầu câu sau `\n` bị sót lượt đầu, đã sửa thành “Mình cũng”).

**Tổng cộng sau file này: 124 file / 5.870 dòng sai** (cơ sở 123 file / 5.776 dòng sai + 94 file này)

- Chờ Hieu: chuyện ghế đá — Fukami tự xưng “em” ở 2294, 2296, 2407 (đúng nếu Soutetsu có mặt, sai thành “tớ”/“mình” nếu chỉ nói với Nagi); 2309 “Nhờ em nhé” (đúng chỉ khi người nghe là Reina); 2393 “Chị xin phép” (đúng chỉ khi ăn cùng Reina); 2174 Nagi “Em đợi anh nhaaaa!” (đúng chỉ khi đợi Soutetsu); 3294 ぷぁん “Tuýt!” hay “Bụp!” (TW: 砰); 2177 ふぁ……→“Oa...” thêm vào hàng đợi thống nhất (fa/fu).

```toml
"1522" = "...Cờ xanh và cờ đỏ,\\nrốt cuộc mình chẳng phải phất lần nào."
"1526" = "...Chị Paulette, vừa thanh toán,\\nvừa nhận vé của khách khác, vừa kiểm tra vé định kỳ nữa."
"2086" = "「Để chắc chắn thì, tuyến Yunoi của đường sắt Ohitoyo,\\nhiện tại chỉ có hai ga là Ohitoyo và Yunoi thôi ạ——」"
"2111" = "「Đạo đường. Đạo đường kiếm đạo ở thị trấn Ohitoyo」"
"2137" = "「Ờm... vì đó——cũng là công việc nhà mình.\\nChèo thuyền trên sông Kuma cũng khá giống vậy, nên là」"
"2143" = "「Ưm... ờm.\\nHay là em nên quay lại sau nhỉ?」"
"2158" = "「Hiee!? E, tớ, thì——\\ntớ có gì——mà giỏi——ạ!?」"
"2165" = "「Hả? Em có làm gì đâu——」"
"2178" = "「Ha... hau...\\nK, không có... tớ——」"
"2221" = "「A! Ý hay đấy! Ừ. Nhờ Fukami\\nkiểm tra lại sức hấp dẫn dọc tuyến đường sắt Ohitoyo một lần nữa」"
"2240" = "「A, ừ. ——Vâng.\\nCháu nhớ——cháu nhớ chứ, ạ」"
"2262" = "「Ừ. Vừa thấy biển——à, đúng rồi.\\nTừ lúc đó trở đi, bé Olivy đã bắt chuyện với bọn tớ mà」"
"2283" = "「Ufufu, chị Fukami, giỏi quá đi.\\nNày chị Paulette, nếu đường sắt Ohitoyo có chuyến tàu du lịch tiếp theo」"
"2416" = "「Vì thế, xin hãy cho em——trở thành một người đồng đội thực sự của đường sắt Ohitoyo.\\n——Trở thành trưởng tàu! Đi ạ!!!」"
"2433" = "「Đúng không? Vì vậy, không phải chỉ dựa vào sức của một người.\\nMà đường sắt Ohitoyo——phải cải thiện vấn đề này với tư cách là một tổ chức」"
"2438" = "「Đúng rồi ạ. Bọn mình đi Aircra đến Sendai,\\nrồi từ Sendai lại cứ ngồi tàu suốt——」"
"2442" = "「Đúng vậy ạ. Thế nên chị dọn dẹp nhà vệ sinh là đúng rồi」"
"2460" = "「Đúng vậy! Nếu thế thì chắc chắn bổn tiểu thư này!\\nSẽ cho Fukami thấy những cảnh sắc đẹp hơn nữa!」"
"2478" = "「Ví dụ như lúc chèo thuyền xuôi dòng, bọn mình sẽ hát.\\nCứ nói mãi thì khách sẽ không muốn nghe nữa」"
"2499" = "「Vé một chiều từ Yunoi là 690 yên ạ.\\nQuý khách vui lòng gia hạn vé định kỳ ở Cửa hàng đường sắt nhé」"
"2514" = "「Ờm, chị vẫn chưa biết gì nhiều về nhà ga——\\nNên chị muốn xem xét nhà vệ sinh thật kỹ càng」"
"2569" = "「Bà đi qua bên kia, đến Cửa hàng đường sắt,\\nrồi hỏi mua 『Vé Ohitoyo Một Đêm』 nhé」"
"2572" = "「Cảm ơn quý kh——a!\\nQuý khách ơi? Vé định kỳ của quý khách hết hạn rồi ạ」"
"2596" = "「Chuyện đó... vâng, ạ.\\nEm nghĩ là, đúng là có đấy ạ」"
"2622" = "「Nếu vậy thì, em.\\nNghĩ là em có thể giúp ích được một chút」"
"2664" = "「Việc cải tạo toa hành khách BBQ đang rất nổi tiếng trong giới chủ tàu đấy.\\nThế nên họ mới ngỏ ý nhờ chúng ta thiết kế giúp」"
"2881" = "Nhưng... mình muốn nói, muốn truyền đạt——\\nVì đó là điều mình luôn ao ước."
"2882" = "Nhưng mà, mình cũng có cùng cảm giác.\\n15 phút, chỉ như một cái chớp mắt——ơ, a!"
"2885" = "Nhưng, cơ hội thế này sẽ không có lần thứ hai.\\nNếu bây giờ không nói, chắc chắn cả đời này mình sẽ không thể nói ra!"
"2887" = "Nhưng. Vì thế.\\nVì nhìn thấy những thứ khác nhau, nên cũng có chữ \"chúng ta\" mà mình có thể bước vào."
"2888" = "Việc luôn giữ gìn sạch sẽ quan trọng đến mức nào,\\nbản thân mình cũng tự cảm nhận được."
"2891" = "Nếu mình là một nhân viên nhà ga dễ bắt chuyện,\\nmình muốn mình có thể trả lời thỏa đáng mọi câu hỏi."
"2961" = "Nhưng——nhưng mà! Nghĩ về chuyến đi đường sắt Mikan,\\ntừ lúc đó đến giờ, mình đã suy nghĩ rất kỹ rồi... cơ mà."
"2968" = "A——vừa nãy, tim mình hơi nhói lên một chút.\\nVì trong chữ \"chúng ta\" đó, không có mình ở đây."
"2972" = "Vì chèo thuyền trên sông Kuma là khởi đầu cho mọi thứ của mình mà."
"2974" = "Khi học về sông ngòi, về hệ sinh thái,\\nmình cũng được dạy về hệ thống."
"2979" = "Vui quá, thực sự rất vui.\\nMọi người đều quan tâm đến mình."
"2985" = "Nhẹ nhõm quá.\\nMình bắt đầu thấy tự tin hơn chút."
"2988" = "Có vẻ như chị Paulette và chị Hibiki đã biết chuyện rồi,\\nnhưng mình vẫn kể lại không sót chữ nào những gì mình đã thấy."
"2994" = "Chỉ thế thôi là mình cũng lờ mờ hiểu ra.\\nVì... là anh Soutetsu và Nagi mà."
"2997" = "Sở thích của mình,\\ntrà chanh không đường, em ấy cũng nhớ nữa."
"2999" = "Nếu trở thành trưởng tàu,\\nmình có thể cùng hai người họ chạy về phía bên kia đường ray."
"3003" = "Nếu không có chèo thuyền trên sông Kuma,\\nmình đã không gặp được Nagi và anh Soutetsu."
"3016" = "Đúng rồi, mình đến đây là để nói chuyện đó——\\nKhông, là để nhờ vả."
"3017" = "Với anh Soutetsu, với Nagi, với mẹ và mọi người,\\nnhư vậy là vô cùng, vô cùng thất lễ, mình hiểu điều đó."
"3019" = "Nagi lao đến ôm chầm lấy mình.\\nNhư một chú cún con đang vẫy đuôi vậy!"
"3021" = "Nagi lại ôm chặt lấy mình một lần nữa——\\nRồi sau đó, nét mặt em ấy trở nên nghiêm túc."
"3023" = "Nagi vung tay ra,\\nnên mình cũng đập tay lại gần như phản xạ có điều kiện."
"3029" = "Làm mình giật cả mình.\\nĐột nhiên bị gọi từ phía sau——ơ, a."
"3067" = "Oa, oa. Làm sao đây.\\nĐến lúc quan trọng, quả nhiên chân mình lại chùn bước."
"3070" = "Bởi vì, mình...\\nchỉ là được dẫn đi cùng thôi——mà, nhỉ?"
"3074" = "Mình nuốt ực câu 『Cỡ như mình thì』 đang chực trào ra.\\nNếu nói thế, sẽ thật có lỗi với những người quan trọng của mình——"
"3080" = "Vì là Nagi nên chắc chắn không phải đang trêu chọc mình.\\nNhưng——"
"3082" = "Mình hiểu rồi. Điều mình đã làm——không,\\nlàm như mọi khi, kết quả là công việc đã hoàn thành."
"3084" = "Sợ hãi, và xấu hổ.\\nĐến giờ này rồi còn... một giọng nói vang lên trong mình."
"3086" = "Thế rồi, mình muốn nói chuyện lắm,\\nnhưng đầu óc cứ lâng lâng, mơ màng..."
"3088" = "Mình đang đau đầu không biết mở lời thế nào——\\nNhưng, nếu có chị Hibiki đi cùng. Thì!"
"3090" = "Tim mình bắt đầu đập thình thịch——\\nDù vậy, anh ấy vẫn nhìn mình chăm chú."
"3092" = "An tâm gì chứ, mình hoàn toàn không thấy vậy mà.\\nTim mình đang đập thình thịch thế này cơ mà."
"3097" = "Nhưng, chính vì thế, mình đã cố gắng tìm kiếm."
"3101" = "Thấy rồi, chị Paulette.\\n\\x%lキハ07s;#00ffc040;KiHa 07S%l;#;, có vẻ vừa mới quay lại."
"3104" = "Còn nữa, cái này.\\nHướng dẫn cho khách cũng là sự giúp đỡ mà mình có thể làm."
"3106" = "Mình vuốt ve đầu khen ngoan ngoãn,\\nthì em ấy lại rừ rừ, giờ thì giống hệt mèo con luôn!"
"3120" = "Hay nói đúng hơn, có lẽ chị Hibiki,\\nđã cố tình làm vậy để giúp mình."
"3126" = "Dù chỉ mới một ngày, nhưng mình cảm thấy mình đã trở thành\\n\"đồng đội\" hơn ngày hôm qua rất nhiều!"
"3128" = "Hiểu ra rồi, mình lại thấy kỳ lạ.\\nNếu vậy, việc đưa mình về cũng——"
"3131" = "Thực ra, mình muốn đợi \\x%lキハ07s;#00ffc040;KiHa 07S%l;#; quay lại,\\nđể giúp soát vé luôn cơ, nhưng mà——"
"3143" = "Không, dù vậy cũng không sao,\\nmình sẽ làm nũng với anh Soutetsu trong khoảng thời gian đó."
"3153" = "Lý do đó, chị Paulette đã\\ndạy cho mình rất cẩn thận, để mình có thể hiểu và bắt tay vào làm."
"3161" = "Dù có phải là sự thật hay không cũng không quan trọng——Anh Soutetsu,\\nnghĩ về mình như vậy khiến mình vô cùng hạnh phúc!!"
"3165" = "Lúc đó, anh Soutetsu——\\nchắc chắn sẽ nhìn sâu vào mắt mình, rồi ôm lấy vai mình——"
"3166" = "Tiếng Kumamoto.\\nCứ như Nagi đang nói chuyện với mình vậy, mình thấy bình tĩnh hơn chút."
"3177" = "Giọng nói êm ái của Reina.\\nChỉ vậy thôi cũng đủ làm mình nhẹ nhõm."
"3188" = "Giỏi thật đấy, thực sự luôn.\\nVì là chuyện thường ngày nên mình hoàn toàn không để ý..."
"3190" = "Quả nhiên mình thấy ghen tị.\\nMình cũng——muốn trở thành đồng đội, một người đồng đội thực sự."
"3191" = "Vui quá, cảm giác này. Dù không thể cùng nhau lái tàu,\\nnhưng tự mình, đã bước vào \"chúng ta\" rồi!"
"3196" = "Được cảm ơn, mình ngẩn tò te."
"3200" = "Chết rồi, cái này thì mình không biết."
"3208" = "Tiếng nước róc rách.\\nÂm thanh mà mình thích nhất."
"3214" = "A, không. Ngực mình chợt hẫng đi, nhói đau.\\nAnh Soutetsu đang khen mình, vậy mà——"
"3222" = "Chính mình đã nói ra, một điều hiển nhiên——\\nTrong chữ \"chúng ta\" của anh Soutetsu, không có mình."
"3227" = "Bị bắt chờ thế này thì... a... không được, không được nghĩ vậy. Nhưng——\\nMình lại bắt đầu nghĩ 『Quả nhiên mình chẳng là gì cả』."
"3239" = "Cứ muốn uống trà thế này mãi thôi,\\nthành thật mà nói mình cũng có cảm giác đó——nhưng..."
"3255" = "Vì bản thân mình nữa,\\nmình nghĩ chắc chắn sau này nó sẽ có ích."
"3257" = "Sao thế nhỉ?\\nChị Paulette... cứ nhìn chằm chằm... vào mặt mình."
"3258" = "Nghe anh ấy nói mình mới nhớ ra một chút. Đúng rồi, mình——\\nvừa đi vừa được anh ấy dạy cho rất nhiều thứ..."
"3262" = "Vẫn chưa kịp đi tắm,\\nmùi hương của sự cố gắng vì mình và Nagi."
"3269" = "Dù nghĩ đó chỉ là sự tình cờ,\\nnhưng nếu thực sự là vậy, mình cũng muốn tận dụng ưu điểm đó."
"3270" = "Mình biết chứ——\\nKhông, vì biết nên mới phải cố gắng!"
"3272" = "Nói rồi, anh Soutetsu nhìn mình.\\nTừ đỉnh đầu đến mũi giày."
"3276" = "Mình bị phát hiện là đã thức dậy rồi.\\nBị phát hiện rồi——nhưng anh ấy bảo cứ thế này cũng được."
"3277" = "Anh Soutetsu gật gù.\\nRồi nhìn chằm chằm——vào mắt mình."
"3280" = "Anh Soutetsu bật cười khúc khích. Ở trên lưng.\\nNên mình lại ôm chặt lấy anh ấy hơn."
"3296" = "8620 ra khỏi xưởng thì mình sẽ vào xưởng,\\nvà tiến hành bảo dưỡng trước khi xuất phát."
```

## 仲国02 — 仲国02_北琴の鉄道.txt.toml — 14/448 (3,1%)

- File: `仲国02_北琴の鉄道.txt.toml` — route 10_Chikuni, 448 dòng script (Soutetsu 104, độc thoại 136, Hibiki 58, Jiang 48, Suika 46, Hachiroku 45, Zhihuan 11). Nội dung: đoàn Soutetsu–Hibiki–Hachiroku đến ga Bắc Cầm ở Zhongguo để khảo sát — gặp thư ký Jiang Yehuang, Railord Suika (Dongfu 4 2000) và lái tàu Liu Zhihuan; vướng kiểm tra an ninh gắt gao ở ga, Hibiki suýt bị thu sổ phác thảo vì vẽ đầu máy; giải thích hệ thống vé, tàu nhanh K – đặc khoái T – trực đạt đặc khoái Z, toa giường mềm/cứng, Lục Bỉ Xa; kết bằng việc quyết định lịch trình (lên tàu sáng ngày mốt, tham quan Bảo tàng Lịch sử Đường sắt Zhongguo).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, khóa khớp TOML tuyệt đối 448/448. `[selections]` rỗng. Không có thẻ `%l` sai định dạng. Không có bản sao file này (md5 `84d160b68d227bb3fd574c8a1fbb83f7`).
- Phân loại (14): thuật ngữ 8 (1685, 2262, 2388, 2984, 2985, 2996, 3164, 3264 — 御一夜→Ohitoyo: 5× "Ohito" + 3× "Ohimitera", sửa trong audit theo tiền lệ ハチロク03/07/09 — KHÔNG thêm lại vào hàng đợi thống nhất), đại từ 2 (2026 Soutetsu "cậu"→"cô" với Jiang; 2182 Soutetsu "cậu"→"em" với Hibiki), dịch sai nghĩa 3 (2255 特急→"đặc cấp"; 2497, 3192 独り言→"nói mớ"), gasp 1 (2231 っ đầu dòng, sweep bỏ sót).
- Sweep kiểm chứng: 4 mục cho file, nhận 0 fix (3 already-rendered: 2171, 2186, 2232; 1 needs-file-audit 3294 đã xử lý, không sửa); quét máy bổ sung bắt thêm 1 gasp sweep bỏ sót (2231). Không còn っ thô trong VN. 2204 はうっ→"Hau..." và 2225 あっ→"A." giữ theo quy ước toàn dự án.
- Chi tiết đầy đủ: `audit-chukuni02-kita-koto-no-tetsudo-REVIEW.md`; danh sách sửa: `audit-chukuni02-kita-koto-no-tetsudo-wrong.json` (14 mục, khối TOML 14 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 14/14; lượt soát 2: 14/14, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 125 file / 5.884 dòng sai** (cơ sở 124 file / 5.870 dòng sai + 14 file này)

- Chờ Hieu: 2182 — người nghe là Hibiki ("em", đã sửa theo cách gọi cuối câu) hay Hachiroku (thì phải là "cô")? "Cậu" sai trong cả hai cách đọc; 2356 "Trăm sự nhờ cậu." — người nghe Jiang ("cô") hay Zhihuan ("cậu")? Không sửa, cần xác nhận.

- Ghi chú của parent (kiểm chứng khi gộp): 2182 đã xác minh là "em" — JP gọi thẳng "日々姫" ở cuối câu, TW xác nhận; không cần Hieu quyết. 2356 giữ nguyên cờ chờ Hieu.

```toml
"1685" = "「……Chúng ta cũng phải hướng tới điều đó thôi. Cả Đường sắt Ohitoyo của chúng ta nữa.\\nPhải đồng hành cùng cuộc sống của mọi người một cách sâu sắc hơn, rộng lớn hơn.」"
"2026" = "「Xin lỗi, cảm ơn cô nhiều.」"
"2182" = "「Haha. Đúng là làm em bối rối thật rồi. Xin lỗi nhé.\\nVậy thì chúng ta đừng khách sáo nữa. Được chứ? Hibiki.」"
"2231" = "「Ư!! \\x%lｚｈｉｈｕａｎ;#00ffc040;Zhihuan%l;#;!!!」"
"2255" = "「Ồ. Đúng là điều thú vị chỉ có ở những nước cùng chung vùng văn hóa chữ Hán nhỉ.\\nNếu vậy thì——tàu tốc hành đặc biệt cũng giữ nguyên là tốc hành đặc biệt sao?」"
"2262" = "「Nếu nói theo lịch sử Đường sắt Ohitoyo thì……\\nĐó là hai năm trước khi Nine Stars có chuyến chạy đầu tiên nhỉ.」"
"2388" = "「R, rất vui được gặp cô. Tôi là Migita Hibiki. Nhà thiết kế toa xe thuộc Đường sắt Ohitoyo,\\nđồng thời cũng là lái tàu và phụ lái tàu.」"
"2497" = "「Vâng! Những chuyển động trong tâm trí như vậy đã vô tình bộc lộ ra ngoài,\\ncái này, người ta thường gọi là nói một mình nhỉ.」"
"2984" = "Trên tấm bảng mô phỏng 8620 có viết dòng chữ\\n『Hoan nghênh! Phái đoàn Đường sắt Ohitoyo』."
"2985" = "Ngay cả trong lễ hội mùa thu \"Okunchi\" náo nhiệt nhất của đền Akai ở Ohitoyo,\\nchắc cũng khó mà thấy được cảnh tượng đông đúc đến mức này."
"2996" = "Nếu có thể lập ra được bản thảo cho kế hoạch Nine Stars phiên bản Zhongguo,\\nthì kinh nghiệm đó nhất định cũng sẽ…… mang lại lợi ích cho Đường sắt Ohitoyo……?"
"3164" = "Vì môi trường đặc thù của Đường sắt Ohitoyo,\\nnên chúng tôi thường hay vô tình quên mất điểm đó, nhưng……"
"3192" = "Bản thân người nói một mình chắc cũng khó mà tự nhận thức được\\nbối cảnh khiến họ thốt ra những lời đó."
"3264" = "Cảnh tượng này không thể thấy trên các chuyến tàu du lịch chỉ định chỗ ngồi hoàn toàn như Nine Stars,\\nvà cũng chưa từng thấy trên toàn bộ các chuyến tàu thông thường của Đường sắt Ohitoyo."
```

## 稀咲02 — 稀咲02_新事業案.txt.toml — 29/448 (6,5%)

- File: `稀咲02_新事業案.txt.toml` — route 06_Kisaki, 448 dòng script (độc thoại 170, Kisaki 128, Soutetsu 116, Hibiki 20, Hachiroku 14). Nội dung: Kisaki trình bày phương án "quỹ My Rail" (chứng khoán hóa đường ray) để cứu tuyến Ohitoyo trước sức ép nhà máy Aircra; xen kẽ cảnh tập lái/tắm trên đầu máy 8620 (Kisaki phụ lái tập sự, Soutetsu hướng dẫn, Hibiki nhân viên cơ vụ tập sự); kết bằng chạy thử 8620.
- Phân loại (29): thuật ngữ 10 (御一夜→Ohitoyo 9: 1371, 1721, 1750, 1772, 2038, 2192, 2331, 2559, 2676; 右田一→Migita Ichi 1: 2151), thở gấp 7 (1870, 2289, 2394, 2395, 2810, 2821, 2830 — cả 7 từ sweep, đã kiểm chứng), sai nghĩa 7 (1370, 2223: 謳歌 "ca ngợi"→"tận hưởng"; 1674: 地獄の窯 "lò bát quái"→"lò địa ngục"; 1942: bỏ chủ ngữ bịa "hành khách"; 2376: 兄さん "anh Soutetsu"→"anh trai"; 2915: 合格点 "điểm tuyệt đối"→"điểm đạt"; 2992: "sinh ra từ nụ cười"→"cô thiếu nữ… nghĩ ra"), thẻ %l 2 (2008, 2365: "[8620'86]" hỏng → tag `\x%l8620;#00ffc040;8620%l;#;` theo mẫu 1758), đại từ 1 (2260: Hachiroku "Chị Kisaki"→"Cô Kisaki", khớp 2262 + toàn dự án 10:2), SFX 1 (2523: ちゃぷん "róc rách"→"'chụp' một tiếng"), thêm nghĩa 1 (2874: bỏ ghi chú "(Bảo hỏa - Hoka / Ngoài ra - Hoka)" không có trong JP).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất; TOML khớp CSV3 tuyệt đối modulo flatten `\n`→khoảng trắng đã biết (235 dòng); md5 `ead507acd1b6cb5a2ef94bf4ea990d92`, không có bản sao. `[selections]` rỗng. Trái với file 01 cùng route (47,0%, chuỗi xoay 173 dòng), file này không có chuỗi xoay — lỗi tập trung ở thuật ngữ cũ Ohimitera/Ohito.
- Đại từ đúng toàn file: Soutetsu "tôi" với Kisaki (0 dòng "anh" tự xưng; 3 lần "anh" đều là "anh Urakami" ngôi thứ ba); Soutetsu gọi Kisaki "cô", Hibiki "em ấy", Hachiroku "em", Mayami "chị Mayami"; Hibiki "em"/"anh hai"; Hachiroku "em"/"ngài Soutetsu". 日ノ本 đã là "Hinomoto" đúng 4/4; まいてつ→"chủ tàu", エアクラ→"Aircra" đúng toàn file.
- Sweep: 7 mục áp nguyên đã kiểm chứng, 0 mục bị bác, 0 gasp sweep bỏ sót. Lượt soát 2: 29/29/0/0. JSON 29 mục dạng chuẩn, khóa chuỗi; khối TOML 29 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 29/29.
- Chờ Hieu: Kisaki tự xưng "tôi" hay "em" với Soutetsu — câu hỏi ĐANG CHỜ từ file 01, file này bổ sung thêm 16 dòng "tôi" + 10 dòng "anh Soutetsu" (nội bộ file nhất quán, không sửa); toàn dự án Kisaki "tôi" 284 vs "em" 247, cảnh H dùng "em" áp đảo, cảnh họp/công việc dùng "tôi" — khả năng theo ngữ cảnh nhưng chờ Hieu chốt. 2874: ghi chú chơi chữ đã bỏ, Hieu có thể yêu cầu khôi phục. 2151 "Migita Ichi" có thể trùng với 15 dòng trong hàng đợi thống nhất — đợt thống nhất đối chiếu lại.

**Tổng cộng sau file này: 126 file / 5.913 dòng sai** (cơ sở 125 file / 5.884 dòng sai + 29 file này)

- Ghi chú của parent (kiểm chứng khi gộp): 2260 "Cô Kisaki" đã xác minh — Hachiroku gọi Kisaki 様, dòng 2262 cùng file đã là "Cô Kisaki"; 2376 "anh trai" đúng (JP 兄さん, TW 哥哥); 2915 "điểm đạt" đúng (合格点 = điểm đạt, không phải tuyệt đối); 2992 sửa lỗi đổi chủ ngữ đúng (TW: 少女所想到的); 2874 bỏ ghi chú chơi chữ không có trong JP — đã cờ cho Hieu nếu muốn khôi phục.

```toml
"1370" = "「Công ty \\x%lエアクラ;#00ffc040;Aircra%l;#; cũng có những khó khăn riêng của công ty \\x%lエアクラ;#00ffc040;Aircra%l;#; nhỉ.\\nTôi cứ tưởng họ đang tận hưởng mùa xuân của thế gian này cơ.」"
"1371" = "「Lý do lớn nhất khiến công ty \\x%lエアクラ;#00ffc040;Aircra%l;#; chọn Ohitoyo làm địa điểm ứng cử,\\nlà vì nơi đây dễ dàng trở thành cứ điểm sản xuất và bán hàng cho khu vực trung tâm Kyushu.」"
"1674" = "「B, bình thường thì tôi không sợ đâu.\\nNhưng mà giật mình chứ sao!? Ngọn lửa cứ như lò địa ngục thế này.」"
"1721" = "「Cùng tồn tại và cùng phát triển? Giữa thành phố Ohitoyo và\\ncông ty \\x%lエアクラ;#00ffc040;Aircra%l;#; sao?」"
"1750" = "「Tuy nhiên, nếu chỉ có hợp tác thì cũng không thể tránh khỏi sự suy thoái chậm chạp.\\nGiống hệt như tình trạng mà Ohitoyo đang mắc phải vậy.」"
"1772" = "「Nếu giả sử có thể khôi phục lại tuyến đường đó, thì cả công ty \\x%lエアクラ;#00ffc040;Aircra%l;#; và Đường sắt Ohitoyo\\nđều có thể tạo ra lợi nhuận…… nên tôi đã nghĩ nếu làm được thì tốt biết mấy.」"
"1870" = "「Hiee!? Auwa!?——A——kyuuu～～～Ư」"
"1942" = "「À, đúng vậy. Bị \\x%l炭水車;#00ffc040;toa tiếp than nước%l;#; và lò hơi che khuất,\\nnên hoàn toàn không thể nhìn thấy tình hình trong \\x%l運転台;#00ffc040;buồng lái%l;#; hay cảnh vật phía trước.」"
"2008" = "「Giống như anh Soutetsu sở hữu \\x%l8620;#00ffc040;8620%l;#, cho chạy tàu, và nhận được phần lợi nhuận được chia. Ý tôi là làm điều tương tự với đường ray, nhưng với số lượng người tham gia lớn hơn.」"
"2038" = "「Cả Đường sắt Ohitoyo nữa sao? Ơ, à…… ra là vậy. Đương nhiên rồi,\\nnếu là vận chuyển thì sẽ có \\x%l列車;#00ffc040;đoàn tàu%l;#; chở hàng chạy qua mà——」"
"2151" = "「Đúng vậy. Xưởng rượu Migita Ichi cũng thế,\\nvà Kumagin cũng không ngoại lệ.」"
"2192" = "「Công việc của anh ấy không phải là 『thu hút nhà máy đến Ohitoyo』,\\nmà là 『chọn địa điểm tối ưu nhất để đặt nhà máy』.」"
"2223" = "「Bây giờ vẫn còn phí bản quyền của động cơ Aero-Craftech,\\nnên mùa xuân của thế gian này vẫn là mùa xuân thôi…… nhưng làm gì có dư dả để mà tận hưởng chứ.」"
"2260" = "「Cô Kisaki sẽ làm \\x%l機関助士;#00ffc040;phụ lái tàu%l;#; tập sự. Ngài Soutetsu sẽ hướng dẫn.\\nNếu vậy, Hibiki sẽ làm \\x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; tập sự——」"
"2289" = "「C, căng thẳng――――～～～Ư」"
"2331" = "「Cách đó…… ý cô là, khôi phục lại tuyến đường giữa Ohitoyo và Sendai sao?」"
"2365" = "「Là nhờ được ngồi trên \\x%l8620;#00ffc040;8620%l;#; đấy. Hơn nữa, cũng nhờ được nghe anh kể chi tiết về chuyện khôi phục tuyến đường.」"
"2376" = "「Anh hai——anh trai?」"
"2394" = "「Ư!」"
"2395" = "「Ư!?」"
"2523" = "Tiếng nước kêu 'chụp' một tiếng."
"2559" = "Giữa nơi đó và Ohitoyo trước đây,\\ntừng được kết nối bằng tuyến đường sắt \\x%l帝鉄;#00ffc040;Teitetsu%l;#; chạy vòng quanh Kagoshima."
"2676" = "Nếu có thể thiết lập một địa điểm ứng cử viên có lợi thế hơn Ohitoyo,\\nthì vừa có thể tránh được việc thu hút nhà máy, vừa mang lại điểm cộng cho anh Urakami."
"2810" = "Dáng vẻ thiếu tự tin trong \\x%l運転台;#00ffc040;buồng lái%l;#; khi nãy, giờ đây lại xinh đẹp đến nhường này sao――――――Ư!!"
"2821" = "Ngay chính diện. Ánh mắt của Kisaki nhìn xuống dưới. Và ánh mắt đó, ngay lập tức lại hướng lên trên——Ư!!?"
"2830" = "Tiếng nước đó không hề dừng lại, mà vòng sang bên hông, rồi tiến sát ngay bên cạnh tôi——Ư!!"
"2874" = "Bản thân mình vừa vô tình thốt ra\\nmột câu chơi chữ nhạt nhẽo."
"2915" = "Gương mặt Kisaki lộ vẻ hài lòng.\\nCó vẻ như sự hiểu biết của tôi đã nhận được điểm đạt."
"2992" = "Phương án dẫn đến sự hồi sinh của mạng lưới đường sắt——sinh mệnh của ngành đường sắt, đã được cô thiếu nữ đang mỉm cười ngay trước mắt tôi nghĩ ra."
```

## 日々姫02 — 日々姫02_文庫森.txt.toml — 14/412 (3,4%)

- File: `日々姫02_文庫森.txt.toml` — route 02_Hibiki, 412 dòng script (độc thoại 166, Soutetsu 105, Hibiki 100, Kimoto 41). Nội dung: Soutetsu và Hibiki thăm gara đầu máy hình quạt ở Bungomori, gặp lão kỹ sư Kimoto; trò vẽ đoán trên lưng (10 điểm); Kimoto kể lịch sử Đường sắt Kyudai (hai tuyến tư nhân hợp nhất, quốc hữu hóa dưới 帝鉄, suy tàn vì cơ giới hóa và Aircra), gara hình quạt là biểu tượng của Bungomori; kết bằng Hibiki tìm thấy "hạt giống" cho bản thiết kế.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, khóa khớp TOML tuyệt đối 412/412. `[selections]` rỗng. Không có thẻ `%l` sai định dạng. Không có bản sao file này (md5 `29f4cac3a73d38f175346da6ffa3482c`).
- Phân loại (14): thuật ngữ 7 (扇形機関庫 gloss "hình ngành"→"hình quạt" 5: 1617, 1706, 1831, 1832, 1833; 御一夜→Ohitoyo 2: 1770, 1792 — 1792 hai lần trong một dòng), gasp 4 (1522, 1713, 2051, 2065 — cả 4 từ sweep, đã kiểm chứng; 1522 kèm sửa "dang"→"đang"), dịch sai nghĩa 2 (1725 深く "sâu sắc"→"mải mê đến thế"; 2559 のぼせる "say nắng"→"choáng vì nóng" — cảnh tắm), lỗi đánh máy 1 (2512 "dang"→"đang").
- Sweep kiểm chứng: 5 mục cho file, nhận 4 fix (1522, 1713, 2051, 2065), 1 already-rendered (1664) đúng không sửa; 0 gasp sweep bỏ sót. Lượt soát 2: 14/14/0/0. JSON 14 mục dạng chuẩn, khóa chuỗi; khối TOML 14 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 14/14.
- Đại từ đúng toàn file: Soutetsu "anh" với Hibiki, "tôi" độc thoại, "cháu" với Kimoto; Kimoto gọi Hibiki "cô" nhất quán. 日ノ本 đã là "Hinomoto" đúng; エアクラ→"Aircra" đúng.
- Chờ Hieu: 1629 ひえ→"Hí!?" (nghe như cười khúc khích, đề xuất "Hử!?"); 1883 Soutetsu "tôi" trong liệt kê nhóm ("Hibiki, tôi, và mọi người" — giữ theo nguyên tắc nhóm). Đợt thống nhất: 帝鉄 "Đường sắt Hoàng gia" 6 dòng (1242, 1570 gloss, 1655, 1869, 1954, 2544) + 帝有鉄道 key 60 — không tính sai, không sửa trong audit này.

**Tổng cộng sau file này: 127 file / 5.927 dòng sai** (cơ sở 126 file / 5.913 dòng sai + 14 file này)

```toml
"1522" = "「Nhưng, khi một khung cảnh tuyệt vời đến thế này,\\nđang phản chiếu trong đôi mắt của Hibiki——Ư!」"
"1617" = "「Sau khi hợp nhất thì nó phát triển rực rỡ lắm.\\n\\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#; này cũng là thứ được xây dựng vào thời điểm đó.」"
"1706" = "「Hửm? A, không——ra vậy, Hibiki\\nđang nhìn biểu cảm của \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; nhỉ——」"
"1713" = "「Ê he~Ư! Ê he he~Ư!\\nAnh vẽ \"âm vang\" (Hibiki) cho em đó hả!!」"
"1725" = "「Vì em biết anh hai sẽ bảo vệ em.\\nNên em mới có thể mải mê đến thế——á, a a a.」"
"1770" = "「Ohitoyo cũng vậy sao?」"
"1792" = "「Tất cả chúng ta, đều được kết nối với nhau.\\nVậy thì đây là——Ohitoyo——và, Đường sắt Ohitoyo.」"
"1831" = "「\\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#;……Tuyệt quá! Dễ thương quá đi.」"
"1832" = "「\\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#;, sao——」"
"1833" = "「\\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#; là biểu tượng vô cùng lớn lao\\nlần đầu tiên xuất hiện ở Bungomori——không thể để mất được.」"
"2051" = "「Anh hai, từ lúc nào mà anh lại——Ư!!\\nXin lỗi! Em xin lỗi!!?」"
"2065" = "「Toa ăn——\\nToa ăn á! Rào cản cao quá đi mất~~Ư!!」"
"2512" = "Lác đác vài người có vẻ là người dân địa phương,\\nđang đứng thành vòng tròn quanh chúng tôi để theo dõi."
"2559" = "Làn da tôi ôm lấy đang nóng bừng.\\nCó lẽ con bé sắp choáng vì nóng đến nơi rồi."
```
- Ghi chú của parent (kiểm chứng khi gộp): JSON 14 mục, khối TOML 14 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 14/14; lượt soát 2: 14/14/0/0; cơ sở 126/5.913 đã đối chiếu ROUTE-AUDIT.md, không cần rebase. 1725/2559 đã đối chiếu JP+TW — sửa nghĩa đúng. 0 sửa đại từ. Cờ chờ Hieu: 1629, 1883.

## 仲国08 — 仲国08_謝謝再見！.txt.toml — 17/445 (3,8%)

- File: `仲国08_謝謝再見！.txt.toml` — route 10_Chikuni, 445 dòng script (độc thoại 155, 双鉄 94, 日々姫 47, ハチロク 44, 姜 36, 西瓜 35, 志寰 34). Nội dung: buổi chia tay ở Trọng Quốc — chốt bản thảo đề xuất (Bắc Đẩu/Nam Đẩu, rally 108 vì sao, vé Thủy Hử), chụp ảnh kỷ niệm có chữ ký, rồi ra sân bay về Hinomoto.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, khóa khớp TOML tuyệt đối 445/445. `[selections]` rỗng. Không có thẻ `%l` sai định dạng. Không có bản sao file này (md5 `e83119a945bc7c408c805218548c2f23`).
- Phân loại (17): thuật ngữ 11 (1484, 1694, 1862, 1902, 2042, 2330, 2432, 2587, 2654, 2713, 2804 — 御一夜→Ohitoyo: 10× "Ohimitera" + 1× "Ohito", sửa trong audit theo tiền lệ 仲国02/稀咲02 — KHÔNG thêm lại vào hàng đợi thống nhất; 1902 đồng thời khôi phục thẻ %l), thẻ %l 4 (1081, 1083, 1782, 1891 — VN bỏ mất thẻ %l của JP cho クハ26/電車; toàn dự án thẻ này giữ 61 dòng, chỉ 5 dòng bỏ — cả 5 đều ở file này), đại từ 1 (1806 Hibiki "chị Jiang"→"cô Jiang" — khớp 1480 trong file và 6 dòng khác toàn route), gasp 1 (1635 っ đầu dòng → "Ư!", sweep bỏ sót).
- Sweep kiểm chứng: 0 mục cho file này trong `sweep-raw-gasp-wrong.json` (kiểm tra trực tiếp); quét máy bổ sung toàn bộ 134 dòng JP chứa っ bắt thêm 1 gasp (1635). Không còn っ thô trong VN. はうっ→"Hau" (1598, 1703), あっ→"A" giữ theo quy ước toàn dự án.
- Chi tiết đầy đủ: `audit-chukuni08-xiexie-zaijian-REVIEW.md`; danh sách sửa: `audit-chukuni08-xiexie-zaijian-wrong.json` (17 mục, khối TOML 17 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 17/17; lượt soát 2: 17/17, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 128 file / 5.944 dòng sai** (cơ sở 127 file / 5.927 dòng sai + 17 file này)

- Chờ Hieu: 2054 橙汁 "nước cam" vs "Trừng trấp" (đã chờ từ 仲国01, không quyết); 2104 — người nghe của "Cảm ơn cô." (Zhihuan) suy luận là Hachiroku (ba lời cảm ơn 2102/2103/2104 ứng với ba người ký ảnh), cần xác nhận.

```toml
"1081" = "「Đường ray mà \\x%lクハ26;#00ffc040;Kuha 26%l;#; chạy là khổ hẹp, khổ đường sắt 1067mm.\\nTốc độ tối đa trong vận hành thương mại dừng lại ở mức 100km/h.」"
"1083" = "「\\x%lクハ26;#00ffc040;Kuha 26%l;#; là \\x%l電車;#00ffc040;tàu điện%l;#; thử nghiệm tốc hành. Đoàn tàu đó đã được\\nphục chế hoàn toàn cho kế hoạch Nine Stars——điều này không sai chứ?」"
"1484" = "「Chỉ Đường sắt Ohitoyo thôi thì không đủ. Sẽ cần phải tập hợp\\nnhiều trí tuệ và công nghệ hơn nữa từ hai nước Hinomoto và Trọng Quốc.」"
"1635" = "「Ư! ——Vậy thưa thầy Soutetsu, thầy còn phương án nào khác không?」"
"1694" = "「Cảm ơn. Zhihuan và Suika cũng vậy,\\nlúc nào cũng có thể đến Ohitoyo chơi nhé. Chúng tôi sẽ chào đón hết mình.」"
"1782" = "「Chúng tôi có \\x%lクハ26;#00ffc040;Kuha 26%l;#; tốc hành \\x%l電車;#00ffc040;tàu điện%l;#;. Còn đường sắt quốc gia Trọng Quốc có Dongfeng 4D\\nvà sự tích lũy phong phú trong việc vận hành tàu trên khổ tiêu chuẩn 1435mm.」"
"1806" = "「Cho nên, anh hai nè.\\nTrước khi gửi cho cô Jiang, anh kiểm tra lại lần cuối giúp em được không?」"
"1862" = "「Đúng vậy. Tôi thì không rành lắm, nhưng Paulette\\n——Hinai, Giám đốc Đường sắt Ohitoyo, có kiến thức rất phong phú.」"
"1891" = "「Ừ. Zhihuan. Vận hành thương mại với tốc độ trên 200km/h cũng là có thể.\\nNếu kết hợp công nghệ và bí quyết của \\x%lクハ26;#00ffc040;Kuha 26%l;#; và Dongfeng 4D.」"
"1902" = "「Việc tạo ra thời gian tham quan…… trên tính toán thì——là có thể.\\nCó thể——bởi vì, Đường sắt Ohitoyo có đoàn tàu \\x%lクハ26;#00ffc040;Kuha 26%l;#;-000.」"
"2042" = "「Đó là bản thảo đề xuất của chúng tôi, Đường sắt Ohitoyo,\\nnhằm phục hưng đường sắt quốc gia Trọng Quốc ở thời điểm hiện tại.」"
"2330" = "Cuộc họp qua mạng có người đến muộn, có người rời đi giữa chừng, nhưng kết quả là gần như toàn bộ những người liên quan đến Đường sắt Ohitoyo đều đã tham gia."
"2432" = "Trên tấm bảng mô phỏng dòng 8620,\\nlà dòng chữ \"Chào mừng! Đoàn Đường sắt Ohitoyo\"."
"2587" = "Chỉ là để đền đáp công ơn của nhà Migita. Để bảo vệ nguồn nước của Ohitoyo.\\nĐể tìm lại món đồ bị mất của một Railord tình cờ kết duyên."
"2654" = "Cuộc sống ở Ohitoyo, và những chuyến đi. Đường sắt đã cho tôi thấy——\\nhiện tại, quá khứ, và cả tương lai của chính bản thân tôi."
"2713" = "Đó tuyệt đối không phải là một trải nghiệm đặc biệt nào cả,\\ntôi đã học được điều đó từ Hibiki, Paulette——và tất cả mọi người ở Ohitoyo."
"2804" = "Mặc dù đã được Paulette và nhóm Ohitoyo kiểm tra kỹ lưỡng và xác nhận,\\nnhưng quả thực tôi vẫn cảm thấy nhẹ nhõm."
```
- Ghi chú của parent (kiểm chứng khi gộp): JSON 17 mục, khối TOML 17 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 17/17; lượt soát 2: 17/17/0/0; cơ sở của agent (126/5.913) đã LỖI THỜI vì 日々姫02_文庫森 gộp trước — đã REBASE sang cơ sở 127/5.927 → 128/5.944. Khối TOML lấy từ review (snippet thiếu, đã bỏ dòng [script]). 1635 gasp đầu dòng + 1902 khôi phục thẻ %l đã đối chiếu JP — đúng. 1806 "cô Jiang" đã xác minh theo 1480 cùng file. Cờ chờ Hieu: 2054, 2104.


## ハチロク08 — ハチロク08_台枠問題.txt.toml — 21/408 (5,1%)

- File: `ハチロク08_台枠問題.txt.toml` — route 01_Hachiroku, 408 dòng script (độc thoại 162, 双鉄 87, ハチロク 63, ポーレット 32, 凪 18, 日々姫 18, ふかみ 14, 蓑笠 5, れいな 5, 赤井宮司 2, 真闇 2). Nội dung: vấn đề khung gầm (台枠) của 8620 bị biến dạng — bàn phương án đổi khung gầm với 58623 (cỗ máy số 1 của Nippon Sharyo, đang lưu tĩnh tại trụ sở chính Nagoya), giữ hai tấm biển hiệu 8620 + đoàn tàu BBQ, video quảng bá cán mốc 12 vạn lượt xem, xen cảnh ăn trưa đổi món (かえっこ) và màn mô hình khung gầm bằng điều khiển + pin của ông Minokasa.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, khóa khớp TOML tuyệt đối 408/408. `[selections]` rỗng. Không có thẻ `%l` sai định dạng. Không có bản sao file này (md5 `7f63a5a165771defdda21cce22cbf042`).
- Phân loại (21): thuật ngữ 12 (御一夜→Ohitoyo 7: 1974, 2026, 2163, 2316, 2422, 3151, 3166; まいてつ→chủ tàu 2: 1988, 2055; KiHa 2: 2211, 3166; 帝鉄→Teitetsu 1: 2268; 湯医線→Yunoi 1: 3087 — 3166 mang hai thuật ngữ trong một dòng; các dạng cũ sửa trong audit theo tiền lệ 仲国02/稀咲02/仲国08 — KHÔNG thêm lại vào hàng đợi thống nhất), ý nghĩa 4 (1587 khôi phục vị ngữ bị mất của câu khẩu hiệu 機影見えざるは無し; 2186 sửa câu đổi món bị mất nghĩa trao đổi; 2333 Reina “chị ấy”→“em” — nói về chính mình; 2507 bỏ “nóng” bịa thêm ở 圧延鋼板), đại từ 1 (2169 Soutetsu “tôi”→“anh” — người nghe là Paulette, khớp 2168 cùng cảnh), rò ngoại ngữ 1 (2167 chữ Hàn 차 trong “차 thiện” → “phương án tốt thứ hai”), gasp 2 (2501, 2502 — áp nguyên sweep), SFX 1 (2052 “Ư... m”→“Ưm...”).
- Sweep kiểm chứng: 2 mục cho file này trong `sweep-raw-gasp-wrong.json` (2501, 2502), cả hai đối chiếu JP đúng và đã áp nguyên. Quét máy bổ sung toàn bộ 150 dòng JP chứa っ: không còn gasp nào sweep bỏ sót; ああっ→“a a” ở 2020/2028 giữ theo tiền lệ hachiroku-h5/fukamih3 (っ bỏ trước ！). Không còn っ thô trong VN.
- Chi tiết đầy đủ: `audit-hachiroku08-wakumondai-REVIEW.md`; danh sách sửa: `audit-hachiroku08-wakumondai-wrong.json` (21 mục, khối TOML 21 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 21/21; lượt soát 2: 21/21, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 129 file / 5.965 dòng sai** (cơ sở 128/5.944 + 21 file này)

- Chờ Hieu: 1896 + 2398 (đại từ Soutetsu khi nói với nhóm hỗn hợp — “anh” vs “tôi”, giữ nguyên); 2023 (trích dẫn ngắt giữa chừng 「日ノ本の鉄路に8620の――」 — VN hoàn thiện câu trích theo câu đầy đủ ở 1587, giữ hay cắt về đúng chỗ ngắt — đã nằm trong danh sách chờ đợt thống nhất của brief).

```toml
"1587" = "「『——đâu đâu cũng thấy bóng dáng của 8620』. Đó chính là,\\nniềm tự hào lớn nhất của chị em chúng em ạ.」"
"1974" = "「Ra là thế,\\ncất công lặn lội đến tận Ohitoyo để đi \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ——」"
"1988" = "「Được thế thì tốt quá.\\nTôi e là…… không hiểu được những tinh tế trong tâm hồn của một \\x%lまいてつ;#00ffc040;chủ tàu%l;#; đâu.」"
"2026" = "「Ưm, từ đây thì…… công viên di tích thành Ohitoyo chăng?」"
"2052" = "「Ưm... Đúng vậy nhỉ. Ạ.」"
"2055" = "「Ừ. \"Chỉ cần \\x%l台枠;#00ffc040;khung gầm%l;#; thôi cũng muốn cho nó chạy lại một lần nữa\"\\n——Nếu tìm được \\x%lまいてつ;#00ffc040;chủ tàu%l;#; có suy nghĩ như vậy.」"
"2163" = "「Ông thấy sao ạ?\\nKhả năng tiến hành sửa chữa 8620 tại Ohitoyo là——」"
"2167" = "「Nói là phương án tốt thứ hai thì đúng hơn—— Khi thực sự không còn cách nào khác……\\nTôi nghĩ, hay là chúng ta —— \\x%l静態保存;#00ffc040;lưu tĩnh%l;#; 8620?」"
"2169" = "「Điều đó—— anh cũng hoàn toàn đồng tình.」"
"2186" = "「Em cho anh một nửa nhé? Rồi anh hai cũng cho em một nửa phần của anh.」"
"2211" = "「May mắn là sự xáo trộn do việc thay đổi đầu máy xe lửa hầu như không xảy ra.\\nKhảo sát về việc dùng \\x%lキハ07;#00ffc040;KiHa 07%l;#; kéo tàu cũng cho thấy mức độ hài lòng rất cao.」"
"2268" = "「Khung gầm dạng tấm nghe nói từ thời đó đã rất khó ổn định chất lượng rồi……\\nVào cuối thời kỳ \\x%l帝鉄;#00ffc040;Teitetsu%l;#;, hầu hết đã được thay thế bằng khung gầm dạng thanh đấy.」"
"2316" = "「Thị trưởng Paulette…… đã nói là sẽ xin\\ntiền trợ cấp của thành phố cho Đường sắt Ohitoyo nhưng mà.」"
"2333" = "「Reina cũng bất ngờ lắm đó nha!\\nMới trước đây thôi, em toàn hay quên.」"
"2422" = "「Từ chức thị trưởng——\\nđể tập trung vào vị trí giám đốc Đường sắt Ohitoyo sao ạ?」"
"2501" = "「Ư!」"
"2502" = "「Ư!?」"
"2507" = "「\\x%l台枠;#00ffc040;Khung gầm%l;#; của 8620 là khung gầm dạng tấm—— với chiều dọc là thép tấm cán dày 25mm——\\nTức là cấu trúc lấy chiều cao để tạo độ cứng cáp ạ.」"
"3087" = "Nếu chỉ kinh doanh trong phạm vi tuyến Yunoi,\\ngánh nặng lên \\x%l8620;#00ffc040;8620%l;#; sẽ được giữ ở mức tối thiểu."
"3151" = "Toàn bộ chi phí liên quan, tất nhiên sẽ do chúng tôi——\\nhay nói đúng hơn là Công ty Cổ phần Đường sắt Ohitoyo gánh vác."
"3166" = "\\x%lキハ07;#00ffc040;KiHa 07%l;#; chắc chắn cũng là một toa xe đáng yêu và đầy sức hút,\\nnhưng \\x%l8620;#00ffc040;8620%l;#; mới chính là bảng hiệu vàng cho sự phục hưng du lịch của Ohitoyo——"
```
- Ghi chú của parent (kiểm chứng khi gộp): JSON 21 mục, khối TOML 21 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 21/21; lượt soát 2: 21/21/0/0; cơ sở 128/5.944 đã đối chiếu ROUTE-AUDIT.md, không cần rebase. 2169 "anh" đã xác minh người nghe Paulette (2168 cùng cảnh); 2333 Reina nói về chính mình — "em" đúng; 1587/2186/2507/2167 đã đối chiếu JP+TW — đúng. Cờ chờ Hieu: 1896, 2398, 2023 (2023 đã trong hàng đợi thống nhất).


## 日々姫02 — 日々姫02_日々姫の日々.txt.toml — 24/410 (5,9%)

- File: `日々姫02_日々姫の日々.txt.toml` — route 02_Hibiki, 410 dòng script (độc thoại 186, Soutetsu 89, Hibiki 79, Kisaki 22, Saitou 17). Nội dung: buổi sáng ở nhà xưởng ủ rượu — Soutetsu đánh bóng bồn chứa, gặp Hibiki phác thảo nhà xưởng lần đầu; bà Saitou nhận xét Hachiroku hợp quản lý nhiệt độ nhưng "không phải người trở thành thợ nấu rượu"; chiều đến văn phòng Kisaki — dự án "biển hiệu thành phố cũng phải đẹp", bản đồ minh họa, ký hiệu tượng hình của Hibiki; kết bằng Hibiki nhờ Soutetsu dạy làm phụ lái tàu, bắt đầu từ 100kg xúc than.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 410/410 ngoại trừ 242 dòng TOML-2 dẹp `\n` thành khoảng trắng. `[selections]` rỗng. Không có bản sao file này (md5 `bc2003a84a0c9b38fee9be64a31ee67b`).
- Phân loại (24): thuật ngữ 14 (2741, 2111, 2524, 3116, 2316, 2105, 2329, 3122, 2165, 2684, 2364, 2663, 2320, 2346 — Ohimitera→Ohitoyo), bịa thêm 2 (1906 義兄→"anh trai nuôi", 2325 義妹→"em gái nuôi" — bỏ "nuôi", TW chỉ nói 哥哥/妹妹), dịch sai nghĩa 1 (2976 醸造→"chưng cất", sửa "sau khi ủ men"), đại từ 1 (2062 Soutetsu "tôi"→"anh" với Hibiki), gasp 4 (1992, 2002, 2374, 2376 — cả 4 từ sweep), dấu câu 3 (2663, 2905, 3080 — dấu 」 thừa ở dòng độc thoại không có ngoặc kép; 2663 gộp với thuật ngữ).
- Sweep kiểm chứng: 4 mục cho file, nhận cả 4 fix (đã chuẩn hóa `\\n` dẹp thành khoảng trắng khi đối chiếu); quét máy bổ sung không bắt thêm gasp nào (1636, 2130 giữ nguyên theo quy tắc gasp đã khóa).
- Soutetsu "anh" với Hibiki đúng toàn file (1 dòng "tôi" sai đối tượng 2062 đã sửa; "tôi" chỉ ở 3 dòng cảnh Kisaki — đúng; "cháu" với bà Saitou — đúng). "Migita System" ×2 (2671, 2516) thuộc đợt thống nhất, không sửa trong audit.
- Chi tiết đầy đủ: `audit-hibiki02-hibi-no-hibi-REVIEW.md`; danh sách sửa: `audit-hibiki02-hibi-no-hibi-wrong.json` (24 mục, khối TOML 24 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 24/24; lượt soát 2: 24/24, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 130 file / 5.989 dòng sai** (cơ sở 129/5.965 + 24 file này)

- Chờ Hieu: 1906/2325 (義兄/義妹 — "anh rể/em dâu" hay giữ "anh trai/em gái"? Soutetsu được nhận nuôi per 2108 引き取られた, nên 義 có thể cố ý); 2349/2713 (gloss 機関助士 "phụ lái tàu" vs TW 司爐 "người đốt lò"); 2512 (投炭 gloss "xúc than" — đã trong hàng đợi thống nhất).

```toml
"2741" = "Nếu vẽ như một biểu tượng của Ohitoyo thì quá hợp lý rồi.\\nNhưng——ừm, khuôn mặt gật đầu của Hibiki lại có phần cứng nhắc."
"2111" = "「Anh chỉ muốn hiểu thêm về Ohitoyo thôi. Đúng như Hibiki đã nói,\\ncó những khung cảnh chỉ khi làm người quét dọn mới nhìn thấy được.」"
"2524" = "Nếu vậy, chắc chắn ở chỗ của Houshou Kisaki,\\ntôi sẽ gặp được điều gì đó giúp hiểu thêm về Ohitoyo."
"3116" = "（Phủi đi vết mờ đục, gột rửa vết bẩn,\\nvà dùng đôi mắt trong trẻo để tìm hiểu lại Ohitoyo từ con số không.）"
"2316" = "「Bản đồ minh họa thành phố Ohitoyo sao.」"
"2105" = "「Tôi đã nghĩ ra 『Dự án biển hiệu thành phố Ohitoyo cũng phải đẹp』.\\nĐưa biểu tượng tượng hình lên cả bản đồ lẫn biển hiệu.」"
"2329" = "「Quả đúng là——thành phố Ohitoyo, biển hiệu cũng phải đẹp, nhỉ.」"
"3122" = "（Hơn nữa... Kisaki thực sự đang nghĩ đến sự phát triển của Ohitoyo.）"
"2165" = "「Ừm. Là vậy đấy. Hơn nữa, anh cũng học hỏi được nhiều điều.\\nRa là vậy, chuyện này sẽ giúp ích cho việc \"hiểu thêm về Ohitoyo\" đây.」"
"2684" = "Ohitoyo là một thành phố cổ, ít bị tàn phá bởi chiến tranh.\\nTất nhiên cũng có những nơi được xây dựng lại."
"2364" = "「Anh hai, để phục hưng Ohitoyo,\\nsự hồi sinh của Hachiroku là không thể thiếu.」"
"2663" = "Nếu lãng phí những nỗ lực đó,\\nthì việc phục hưng Ohitoyo sẽ càng xa vời hơn."
"2320" = "「Nếu vậy, chỉ hiểu biết sâu sắc về Ohitoyo thôi là chưa đủ.\\nĐể \\x%l8620;#00ffc040;8620%l;#; hồi sinh, chúng ta phải nỗ lực nhiều hơn nữa.」"
"2346" = "「Vậy thì bắt đầu thôi. Mục tiêu là ga Suối nước nóng Ohitoyo.」"
"1906" = "「Vậy thì——với tư cách là anh trai, tôi rất biết ơn.」"
"2325" = "「Tất nhiên rồi. Là cô em gái quan trọng của tôi mà,\\nvới lại đường về của tôi cũng là đường đó.」"
"2976" = "Rượu shochu sau khi ủ men nếu được ủ kỹ trong thùng gỗ,\\nsẽ có thêm hương vị và màu sắc giống như rượu whisky."
"2062" = "「Có vẻ là vậy. Nghe nói đã gặp nhau vài lần, nhưng anh hoàn toàn không nhớ gì cả.」"
"1992" = "「A... a~~Ư」"
"2002" = "「Cơ mà! Việc có vẽ đẹp được hay không,\\nlại là một chuyện hoàn toàn khác đấy nhé~Ư」"
"2374" = "「Ư!」"
"2376" = "「~~Ư!」"
"3080" = "Lẽ nào... mình...\\nđã nói điều gì kinh khủng lắm sao?"
"2905" = "Để giải quyết triệt để tất cả,\\nhiều người vẫn đang làm việc không ngừng nghỉ."
```
- Ghi chú của parent (kiểm chứng khi gộp): JSON 24 mục, khối TOML 24 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 24/24; lượt soát 2: 24/24/0/0; cơ sở của agent (128/5.944) đã LỖI THỜI vì ハチロク08 gộp trước — đã REBASE sang cơ sở 129/5.965 → 130/5.989. 2062 "anh" đã xác minh người nghe Hibiki (2061 cùng cảnh); 1906/2325 bỏ "nuôi" đã đối chiếu JP+TW — sửa đúng, nhưng cờ chờ Hieu vì Soutetsu được nhận nuôi (2108); 2976 đã đối chiếu JP+TW — đúng. Cờ chờ Hieu: 1906/2325, 2349/2713, 2512.


## ハチロク10 — ハチロク10_炙り出し.txt.toml — 12/380 (3,2%)

- File: `ハチロク10_炙り出し.txt.toml` — route 01_Hachiroku, 380 dòng.
- **Sai: 12 dòng (3,2%)** — đại từ 6 (1789, 2069, 2018, 1895, 1733, 1966: Soutetsu "anh"→"tôi" với Hachiroku), gasp 4 (2105, 2110, 2513 từ sweep + 1395 sweep bỏ sót: JP 「っ」 cả dòng), thuật ngữ 1 (2434 Ohimitera→Ohitoyo), dịch sai 1 (2411 乗員 "phi hành đoàn"→"nhân viên tàu").
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- Lượt soát 2: 12/12/0/0. JSON 12 mục, khối TOML 12 khóa, 0 sai lệch giá trị.
- Cờ chờ Hieu: 1825 ("tôi" với Paulette hay nhóm?), 2694 (gloss 機関士 "người lái tàu" — toàn dự án chia 3 dạng, "thợ lái đầu máy" 0×), Hinamoto ×4 (1930, 1793, 1868, 2801 — đợt thống nhất), 日々姫03 2834 cũng "phi hành đoàn", 2872 "lưu tĩnh" giữ nguyên (dạng chủ đạo 17×).

**Tổng cộng sau file này: 131 file / 6.001 dòng sai** (cơ sở 130/5.989 + 12 file này)

```toml
[script]
"1789" = "「Ừm. Cố tình nhấn mạnh là bằng chính bánh xe của nó——thì tôi hiểu rồi.\\nLoại Ất là đặt toàn bộ lên \\x%l貨車;#00ffc040;toa chở hàng%l;#; hay gì đó để vận chuyển đúng không?」"
"2069" = "「Vậy thì, hãy để tôi chụp em.\\nEm có thể mượn một cái đèn khò đến đây được không?」"
"2018" = "「Tôi không biết nữa. Cảm giác như đó là một giấc mơ đẹp.\\nVì đó là giấc mơ về Michiko——về em gái tôi.」"
"1895" = "「Michiko và tôi là anh em sinh đôi.\\nVì vậy, đó chắc chắn là tôi trong hình hài của Michiko.」"
"1733" = "「Chỉ là một chút ký ức dội lại thôi.\\nVì thế nên, tôi mới thấy bất an……hơi bất ổn một chút.」"
"1966" = "「Không sao, tôi ổn mà.\\nTôi không muốn làm phiền em chỉ vì một giấc mơ.」"
"2434" = "Khắc sâu hình ảnh \"Quê hương của hơi nước Ohitoyo\" vào tâm trí mọi người,\\ntừ đó, hiện thực hóa khái niệm Đại Kyushu SL."
"2411" = "Để ngăn chặn việc toàn bộ hành khách và nhân viên tàu bị diệt vong——\\nĐể hạn chế thương vong, cô ấy đã cố tình gây ra tai nạn đó."
"2105" = "「Ư!」"
"2110" = "『「Ư!?」\\n「Á——em xin lỗi——ơ, a, anh hai.」』"
"2513" = "Để có thể khắc sâu hình ảnh Hachiroku,\\nvào tận trong tim mình——Ư!?"
"1395" = "「Ư……」"
```
- Ghi chú của parent (kiểm chứng khi gộp): JSON 12 mục, khối TOML 12 khóa ([script]), 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 12/12; lượt soát 2: 12/12/0/0; cơ sở 130/5.989 đã đối chiếu ROUTE-AUDIT.md, không cần rebase. 6 đại từ "anh"→"tôi" đã xác minh người nghe Hachiroku từ mạch ác mộng/lo lắng (1861 Hachiroku hỏi ác mộng, 1872 Hachiroku thấy mặt tái, 1924 Hachiroku xin chia sẻ lo lắng) và "お前" + Hachiroku kề bên (1966, 2069); 1789 trả lời phần giải thích của Hachiroku; 1395 sweep bỏ sót đã đối chiếu JP (「っ」 cả dòng). Cờ chờ Hieu: 1825, 2694, Hinamoto ×4, 日々姫03 2834, 2872.


## 日々姫h1 — 日々姫h1_マッサージの続き.txt.toml — 12/329 (3,6%)

- File: `日々姫h1_マッサージの続き.txt.toml` — route 02_Hibiki, 329 dòng script (độc thoại 183, 日々姫 81, 双鉄H 65). Nội dung: cảnh H tiếp nối buổi mát xa — đêm sau tiệc mừng chiến thắng, Hibiki sang phòng Soutetsu mát xa cho anh (mát xa đứng, rồi bằng miệng), cả hai thừa nhận muốn làm tình, Soutetsu đề nghị làm tình "đàng hoàng" thay vì thuận đà, Hibiki đồng ý và xin anh lấy đi lần đầu của mình, quan hệ lần đầu, kết bằng những nụ hôn và cả hai chìm vào giấc ngủ.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 329/329. `[selections]` rỗng. Không có bản sao file này (md5 `c8169ed72a3a329d6f677624531c75cf`).
- Phân loại (12): gasp 10 (792, 1011, 1051, 1056, 1222, 1230, 1231, 1232, 1237, 1670 — 6 mục sweep nhận nguyên + 4 sweep bỏ sót: 792 「っ――」→「——Ư」, 1051 「っ！」→「Ư!」, 1056 và 1222 đoạn っ―― đứng một mình bị mất), dịch sai nghĩa 2 (970 子宮に "Tử cung, đang" → "Vào trong tử cung"; 1046 してもらって "Mút mát——Cho." → "Cho em.").
- Sweep kiểm chứng: 6 mục cho file, nhận cả 6 fix; quét máy toàn bộ dòng có っ bắt thêm 4 gasp sweep bỏ sót (792, 1051, 1056, 1222); các っ còn lại giữ nguyên theo quy tắc gasp đã khóa (っ trước gạch ngang thì gạch đã diễn tiếng ngắt — vd. 1042; SFX đã diễn — vd. ぺろっ→"Liếm."; 1049 「っ」→"A.").
- Soutetsu "anh" với Hibiki đúng toàn file (quét máy 65 dòng 双鉄H: 0 dòng "tôi"; độc thoại dùng "tôi" xuyên suốt). Không có thuật ngữ đã quyết nào sai, không thẻ `%l`, không ký tự JP thô trong VN.
- Chi tiết đầy đủ: `audit-hibikih1-massage-no-tsuzuki-REVIEW.md`; danh sách sửa: `audit-hibikih1-massage-no-tsuzuki-wrong.json` (12 mục, khối TOML 12 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 12/12; lượt soát 2: 12/12, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 132 file / 6.013 dòng sai** (cơ sở 131/6.001 + 12 file này)

- Chờ Hieu: fa/fu "Phù" → unification (1013, 1017, 1018, 1059 — ふあっ/ふぁ, dạng đã quyết là "phùa"/"phà"); 1383 monologue lẫn "Anh"/"tôi" cho Soutetsu (chuẩn hóa về "tôi" hay giữ?); 1059 しゅごっ→"Sướng quá" (JP+TW "amazing" — giữ ngẫu hứng hay đổi "Tuyệt quá"?); 1025 ふぇ？→"Hả?" (không theo bảng "phuê"); 1015 lời ngọng khi thè lưỡi (ろふろふ→"Lêu lêu" — giữ ngẫu hứng).

```toml
"792" = "「——Ư」"
"970" = "「Đến rồi! Đến rồi——A——Ưm——Nóng quá——Tinh dịch——Bụng——Vào trong tử cung——」"
"1011" = "「Ơ, xin lỗi——Ư!?」"
"1046" = "「A——Ngực! Ưm——Em——Bị anh hai——Ưm, ngực——Mút mát——Cho em.」"
"1051" = "「Ư! A——」"
"1056" = "「Ngoạm——Ư——Liếm——Liếm——Mút.」"
"1222" = "「Anh——hai——em——Ư——Hơ——A——Không sao——đâu——」"
"1230" = "「Ư!」"
"1231" = "「Ư!!!」"
"1232" = "「Ư!!?」"
"1237" = "「~~~~~~Ư!!」"
"1670" = "Đôi mắt Hibiki cong lên thành hình vòng cung đầy vẻ vui sướng——Ư!?"
```
- Ghi chú của parent (kiểm chứng khi gộp): JSON 12 mục, khối TOML 12 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 12/12; lượt soát 2: 12/12/0/0; cơ sở của agent (130/5.989) đã LỖI THỜI vì ハチロク10 gộp trước — đã REBASE sang cơ sở 131/6.001 → 132/6.013. Soutetsu "anh" với Hibiki đúng toàn file, không có đại từ nào sai; 4 gasp sweep bỏ sót (792, 1051, 1056, 1222) đều là っ mất hẳn tiếng, đúng quy tắc gasp đã khóa. Cờ chờ Hieu: fa/fu "Phù" 1013/1017/1018/1059, 1383, 1059, 1025, 1015.


## 凪ふかみh1_修学旅行の夜.txt.toml (07_Nagi_Fukami) — 8/318 (2,5%)

- File: `凪ふかみh1_修学旅行の夜.txt.toml` — đêm tu nghiệp của ba người (ăn ba ba, lần đầu làm tình ba người: Nagi trước, Fukami sau).
- **8 dòng sai / 318 dòng (2,5%)** — không lệch dòng, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa.
- Phân loại: đại từ 1 (1332 Fukami "tớ"→"mình" với Nagi), gasp 1 (1280 あんっ→"An", sweep bỏ sót), SFX 5 (1238 + 1252 độ dài hơi thở ふー; 2026 + 2027 + 2043 "sột soạt" sai loại tiếng ướt → "rột"/"nhóp nhép"/"Phập!"), lỗi gõ 1 (939 dấu ' thừa).
- Sweep: 5 mục đã kiểm tra — 4 already-rendered đúng (1235, 1236, 1285, 2022); 1736 needs-file-audit đã xử lý: っ đã diễn thành "ư", không sửa.
- Cờ cho Hieu: (1) nói ngọng 1291/1303 — giữ lời rõ hay trả về âm ngọng (cùng loại ハチロク07 2916–2918); (2) fa/fu "phù" 8 key (1166, 1218, 1227, 1237, 1246, 1247, 1336, 1440) → đợt thống nhất; (3) 1224 lỗi dấu `"` phía JP, không phải lỗi VN.
- Lượt soát 2: 8/8/0/0. JSON 8 mục, khối TOML 8 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 8/8.

```toml
"939" = "Chỗ, đáng xấu hổ, nhất――\\nNhư thể cô ấy đang tự mình thể hiện câu nói đó vậy."
"1238" = "「Hơi thở á? Hơi thở làm cho của anh hai giật giật được luôn á?\\n（Phùuuuuuuuuuuuuu!）」"
"1252" = "「Oa. Thật này——Anh Soutetsu, có cảm giác chỉ với hơi thở thôi sao.\\n（Phùuuu）（Phùuuu）（Phùuuuuuu）」"
"1280" = "「An」"
"1332" = "「Bé Nagi, nhé? Không sao đâu——vì mình cũng, ở cùng cậu mà.」"
"2026" = "（Trơn tuột——nhóp nhép——rột——rột!）"
"2027" = "（Nhóp nhép! Nhóp nhép! Chụt chụt! Trơn tuột!）"
"2043" = "（Phập——rột! Phập! Phập!）"
```

**Tổng cộng sau file này: 133 file / 6.021 dòng sai** (cơ sở 132/6.013 + 8 file này)
- Ghi chú của parent (kiểm chứng khi gộp): JSON 8 mục, khối TOML 8 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 8/8; lượt soát 2: 8/8/0/0; cơ sở 132/6.013 đã kiểm chứng → 133/6.021. Đại từ 1332 đã kiểm chứng: Fukami nói với Nagi (JP gọi 凪ちゃん), "mình" đúng chuẩn. Cờ chờ Hieu: nói ngọng 1291/1303, fa/fu "phù" 8 key → đợt thống nhất, lỗi dấu `"` phía JP ở 1224.


## 稀咲h3 — 稀咲h3_チャイナドレスでおもてなし.txt.toml — 75/662 (11,3%)

- File: `稀咲h3_チャイナドレスでおもてなし.txt.toml` — route 06_Kisaki, 662 dòng script (173 thoại Soutetsu, 214 thoại Kisaki, 275 độc thoại). Nội dung: Kisaki tham quan xưởng rượu nhà Migita (thử rượu tươi chưa chưng cất, Soutetsu giải thích men koji/axit citric), hẹn hò ăn crepe, thử sườn xám Trọng Quốc may đo, cảnh H (sườn xám xuyên thấu, quan hệ trên sofa).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 662/662 (chỉ khác 371 dòng TOML-2 làm phẳng `\n` thành khoảng trắng — CSV3 là chuẩn). `[selections]` rỗng ({}). Không có thẻ `%l` nào trong file. Không có bản sao file này (md5 `3bccfb4626ff9b0e014a8655d1091f7e`).
- Phân loại (75): đại từ 50 (Soutetsu "anh"→"tôi" với Kisaki — 50/50 lần sai, lỗi hệ thống; xem danh sách dưới), gasp 16 (11 từ sweep: 1552, 2003, 2161, 2257, 2809, 2810, 2813, 2814, 2824, 2826, 3143 + 5 sweep bỏ sót: 2170, 2188, 2218, 2253, 2820), sai nghĩa 4 (2468, 1550, 2972, 3330), thuật ngữ 3 (2648, 2740, 3099 — Ohimitera→Ohitoyo; 2302 tính vào đại từ), SFX 1 (2158 きゃああっ→"Kyaaa!?"), dấu câu 1 (3483 gỡ 」 thừa).
- Đại từ 50 dòng: 1987, 1993, 2102, 2146, 2251, 2262, 2289, 2291, 2302, 2316, 2387, 2397, 2401, 2402, 2403, 2405, 2411, 2415, 2418, 2419, 2423, 2428, 2429, 2434, 2440, 2443, 2445, 2451, 2453, 2462, 2463, 2474, 2476, 2491, 2510, 2592, 2612, 2640, 2658, 2661, 2698, 2728, 2738, 2768, 2772, 2774, 2775, 2783, 2789, 3006.
- Sweep kiểm chứng: 13 mục cho file, nhận 11 fix (2003 đã chỉnh lại giữ đúng `\n` của CSV3) + 2 already-rendered (3373, 3483); quét máy bổ sung toàn bộ dòng JP chứa っ bắt thêm 5 gasp sweep bỏ sót (2170, 2188, 2218, 2253, 2820). Không còn gasp sót. あっ/はうっ/ああっ/んっ giữ theo quy ước toàn dự án (tiền lệ gộp trong ROUTE-AUDIT.md); fa/fu để đợt thống nhất (17+ dòng, xem review §4).
- Kisaki tự xưng "em" với Soutetsu đúng toàn file (0 lần "tôi"); Kisaki gọi "anh Soutetsu" 33 lần giữ nguyên theo tiền lệ file 稀咲02. Không có thuật ngữ nào khác chờ đợt thống nhất ngoài 帝鉄/帝大 dạng đầy đủ (2740, 2302).
- Chi tiết đầy đủ: `audit-kisakih3-china-dress-omotenashi-REVIEW.md`; danh sách sửa: `audit-kisakih3-china-dress-omotenashi-wrong.json` (75 mục, khối TOML 75 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 75/75; lượt soát 2: 75/75, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 134 file / 6.096 dòng sai** (cơ sở 133/6.021 + 75 file này)

- Chờ Hieu: Kisaki gọi "anh Soutetsu" (33 dòng — đổi sang "cậu Soutetsu"/tên trần toàn tuyến Kisaki hay giữ?); fa/fu "phùa" vs "phù" (17+ dòng, §4 review); 2740 帝鉄 "Đường sắt Hoàng gia" + 2302 帝大 "Đại học Hoàng gia" (đợt thống nhất); 2648 二干潟→"Niigata" (giữ hay đổi?); 2217 くあっ→"Kua!" ("Kua" vs "Hự"); 2238 "Anh Houhehu"/"hích anh" (lời ngọng khi hôn — giữ ngẫu hứng); 2155 しゅごっ→"Tuyệt quá!" (giữ hay đổi "Sướng quá"?).

```toml
"2146" = "「Nếu hiểu được thì chẳng có gì kỳ lạ cả đâu.\\n――Tôi giải thích chi tiết hơn một chút nhé?」"
"2738" = "「Chuyện nhỏ. Tôi cũng đã xin phép trước rồi」"
"2774" = "「Vậy thì, tôi có một câu hỏi cho em đây」"
"2592" = "「Cùng một nguyên liệu là gạo, cùng một phương pháp sản xuất, nhưng tại sao lại thành ra như vậy.\\nTôi muốn em thử suy nghĩ một chút xem」"
"2783" = "「Vậy thì…… xem nào. Tôi muốn em thử so sánh giữa shochu gạo và rượu sake,\\ncùng với những vùng sản xuất tiêu biểu của chúng」"
"2316" = "「Hừm, kem phô mai cũng ngon đấy chứ.\\nKhông bị ngấy như tôi tưởng」"
"2476" = "「Tôi sao?\\nTôi đã làm chuyện gì kỳ lạ à?」"
"2401" = "「Tôi cũng muốn được Kisaki đút cho ăn phần của em.\\nChúng ta thay phiên nhau nhé, thấy sao?」"
"2474" = "「Tấm lòng của em, tôi thực sự――thực sự rất vui」"
"2405" = "「Tôi cũng vậy thôi. Nhân vật chính của lễ cưới, là Kisaki.\\nVì vậy, tôi muốn tạo ra một hôn lễ tuyệt vời nhất dành cho Kisaki」"
"2772" = "「Vậy thì, tôi nói lại nhé. Đối với Kisaki――\\nVà đối với ước mơ của Kisaki, tôi muốn tạo ra một hôn lễ tuyệt vời nhất」"
"2289" = "「Đúng vậy. Tôi cũng cảm thấy thế」"
"2434" = "「Tôi rất biết ơn vì hai chúng ta có thể cùng chung một ước mơ.\\nVà cũng biết ơn vì bác Mototada đã thấu hiểu điều đó」"
"2661" = "「Tôi nghe nói số lượng người muốn tham dự lễ cưới cũng tăng lên chóng mặt.\\nTôi nghĩ việc sắp xếp chắc chắn sẽ không hề đơn giản đâu」"
"2658" = "「Cả Kisaki và tôi đều có sở thích là hay suy nghĩ mà.\\nNên tôi cũng chẳng thể nói những câu an ủi kiểu như 『Đừng suy nghĩ nhiều quá』 được」"
"2443" = "「Ít nhất thì ở hiện trường, tôi cũng muốn giúp được gì đó」"
"2419" = "「Bằng cách giới thiệu tôi là vị hôn phu,\\nem định tạo cớ để mời cô ấy đến dự lễ cưới luôn sao」"
"2491" = "「Vậy đi tiếp khách thì tôi nên mặc đồ gì?\\nMặc vest bình thường có được không?」"
"2302" = "「Tôi đâu có ở vị thế để tham gia mấy chuyện đó.\\nTrước khi trở về Ohitoyo, tôi chỉ là nhân viên của một cửa hàng bán buôn rượu kiêm sinh viên Đại học Hoàng gia thôi mà」"
"2262" = "「Ừm――tôi muốn xem」"
"2445" = "「Tôi muốn ngắm nhìn dáng vẻ Kisaki trong bộ sườn xám」"
"2291" = "「Ừm. Cho tôi xem đi」"
"2429" = "「Tôi mong lắm rồi đấy. Nhanh cho tôi xem đi」"
"1993" = "「Không, cứ giữ nguyên như vậy đi.\\nĐừng che lại, hãy để tôi ngắm nhìn toàn bộ cơ thể em」"
"2510" = "「Cũng đúng. Cho đến khi em nói, tôi mới nhận ra đấy」"
"2387" = "「Sao thế. Tôi nói gì kỳ lạ à?」"
"2440" = "「Tôi thì, làm sao cơ?」"
"2640" = "「Kisaki. Tôi cũng hạnh phúc lắm.\\nCó thể em sẽ nghĩ tôi thực dụng, nhưng――」"
"3006" = "Dù vậy, trái tim tôi vẫn rung động đến nhường này.\\nKhông thể không nói ra thành lời."
"2428" = "「Khi thấy Kisaki xinh đẹp đến thế này,\\ntôi lại một lần nữa cảm nhận sâu sắc niềm hạnh phúc khi được một người phụ nữ xinh đẹp yêu thương」"
"2463" = "「Tôi biết Kisaki, chính là Kisaki.\\nTôi yêu tất cả mọi thứ thuộc về Kisaki, và cũng rất tôn trọng em」"
"2397" = "「Tôi không muốn làm tổn thương Kisaki, không muốn bóp méo con người em.\\nTôi sợ hãi hơn bất cứ điều gì, việc Kisaki không còn là Kisaki nữa」"
"2453" = "「Tôi khao khát cơ thể của Kisaki đến nhường này.\\nNhưng, nếu chỉ có cơ thể thôi thì chẳng có ý nghĩa gì cả」"
"2418" = "「Tôi, yêu mọi thứ thuộc về Kisaki. Nếu tách rời\\nbất cứ phần nào ra, thì đó không còn là Kisaki nữa」"
"2415" = "「Đó là, do tôi chưa quen thôi. Tôi sợ nếu cứ hành động theo dục vọng,\\nthì sẽ làm tổn thương Kisaki mất」"
"2612" = "「Tôi hiểu rồi」"
"2423" = "「Tôi đã làm đủ thứ mình thích rồi mà?」"
"2411" = "「Dù thế nào đi nữa――cũng sẽ theo ý muốn của tôi sao」"
"2789" = "「Ngoài vú ra, tôi cũng sẽ làm theo ý mình đấy」"
"2102" = "「Hãy cho tôi cảm nhận gần hơn nữa đi」"
"1987" = "「Không được sao? Nhưng tôi lại muốn nói đấy」"
"2775" = "「Và tôi muốn hỏi. Em hãy nói cho tôi biết.\\nTại sao cởi dây ra rồi mà quần lót vẫn không rớt xuống?」"
"2728" = "「Như Kisaki đã nói, tình dục mà tôi muốn,\\nchỉ là khao khát thể xác, tôi chỉ tạm thời thử xem sao thôi」"
"2698" = "「Nếu chỉ là thể xác thì tuyệt vời lắm. Rất sướng.\\nNhưng mà, khoái cảm vượt lên trên thế này, tôi đã biết rồi」"
"2462" = "「Người tôi biết, chỉ có Kisaki thôi. Với Kisaki――\\nTình dục không chỉ là thể xác, mà còn là sự hòa quyện của tâm hồn」"
"2251" = "「Đòi hỏi một chiều không phải là tình dục tôi muốn.\\nĐiều tôi muốn nhất và sướng nhất, là tình dục cùng Kisaki tạo ra」"
"2403" = "「Tôi cũng vậy」"
"2402" = "「Tôi cũng vậy――Kisaki」"
"2451" = "「Tôi rất vui.\\nNhưng mà, làm hỏng thì vẫn uổng lắm」"
"2768" = "「Nếu vậy tôi sẽ nằm xuống sofa nhé」"
"2648" = "「Đại diện cho shochu gạo thì tất nhiên là Kuma――Ohitoyo rồi.\\nCòn rượu sake thì――chắc là Niigata để lại ấn tượng mạnh nhất nhỉ」"
"3099" = "Bởi vì chúng tôi đã nhận được rất nhiều thứ không thể nào lấy lại được lần thứ hai,\\ntừ mọi người, và từ Ohitoyo."
"2740" = "「Bác ấy thậm chí còn mời được cựu Tổng giám đốc Đường sắt Hoàng gia,\\nngười vốn không có chút liên hệ nào với Ohitoyo, nhà Migita hay nhà Houshou, làm người mai mối cho chúng ta mà」"
"2972" = "Có lẽ cũng một phần do chính sách chống Minh Quốc của chính phủ,\\nmà việc phổ biến Aircra ở Trọng Quốc diễn ra muộn hơn Hinomoto khá nhiều."
"2468" = "「Chẳng phải anh bảo là 『cho em uống』 sao?\\nAnh Soutetsu, cho em」"
"1550" = "「『Vì đây là nhà của người con trai mà em thích』. Đấy nhé?」"
"3330" = "Là mùi hương của rượu."
"1552" = "「……Ư」"
"2003" = "「Đầu vú…… được, anh Soutetsu…… vuốt ve――……Ư\\nChỉ cần vậy, thôi――đã nóng ran――và cứng lại, thế này――」"
"2161" = "「Kya! Phu――~~~~~~~~Ư!!!」"
"2257" = "「Khu phư ưm~~~~Ư!!!」"
"2809" = "「Ư!」"
"2810" = "「Ư!!」"
"2813" = "「Ư!!?」"
"2814" = "「Ư!?」"
"2824" = "「~~~~~Ư!」"
"2826" = "「~~~~~~~~~Ư!!!?」"
"3143" = "Bất chợt, Kisaki cố gắng che giấu cơ thể mình――Ư!"
"2188" = "「Phù――hà――ưm――phua――ưm――\\n~~Ư! Hà――phua――ưm……ưm phu――」"
"2218" = "「~~~Ư!! Hà――chịu đựng, không nổi!\\nCố gắng, nhưng mà――không được! Cả âm đạo, cũng thế!」"
"2820" = "「~Ư!? Gay go――thì――dương, vật,\\ncho――âm đạo――nghỉ một chút――hya! Phu」"
"2170" = "「Ư~~~――phua, á――vú――ưm,\\nphù――phua――ưm――phù――phù」"
"2253" = "「Phua――ưm――anh, Soutetsu――tuyệt, quá――\\nƯ――giật, giật――liên hồi――nóng quá, to quá」"
"2158" = "「Kyaaa!?」"
"3483" = "Kisaki đang thực sự rất bồn chồn.\\nĐôi chân cứ xoắn xuýt vào nhau――!!?"
```
- Ghi chú của parent (kiểm chứng khi gộp): JSON 75 mục, khối TOML 75 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 75/75; lượt soát 2: 75/75/0/0; cơ sở của agent (132/6.013) đã LỖI THỜI vì 凪ふかみh1 gộp trước — đã REBASE sang cơ sở 133/6.021 → 134/6.096. Đại từ đã kiểm chứng: file chỉ có 3 loại nhân vật (monologue/稀咲/双鉄) nên cả 49 dòng thoại Soutetsu + độc thoại 3006 (TW "告訴她" = Kisaki) đều nói với Kisaki → "tôi" đúng. Cờ chờ Hieu: Kisaki gọi "anh Soutetsu" 33×, fa/fu 17+ dòng, 帝鉄/帝大 dạng đầy đủ (2740/2302), 2648 二干潟→"Niigata", 2217 "Kua", 2238 lời ngọng, 2155 "Tuyệt quá!". Ghi chú của agent về quy ước あっ/はうっ: chỉ là các dòng GIỮ nguyên, không có fix nào — không cần quyết.
