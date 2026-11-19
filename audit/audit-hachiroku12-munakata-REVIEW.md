# Audit: Hachiroku 12_ムナカタ来訪 — 12 dòng Việt sai (đã đối chiếu JP + TW)

File: `01_Hachiroku/ハチロク12_ムナカタ来訪.txt.toml` — 513 dòng script, **12 dòng Việt sai = 2,3%**, 2 nhóm chưa chắc chắn (3 key: 2811, 2528, 2976).
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. Đây là file thứ 8 audit toàn bộ, sau 廃炭鉱 31%, obasan 56%, Grand 01 45,6%, Hibiki 03 86,2%, Hachiroku 13 夜の嵐 44,9%, 実りの秋 0,4%, Nagi_Fukami 08a 4,3% — **file sạch thứ hai từ trước tới nay** (chỉ sau 実りの秋 0,4%), và là file đầu tiên của route Hachiroku được audit sau khi phát hiện tràn chương ở 夜の嵐.

## Phương pháp và số liệu kiểm chứng
- Đã đọc **hết 513/513 dòng script** (key 1097–3066, không liên tục), đối chiếu từng dòng với JP + TW theo nghĩa, người nói, thoại/lời dẫn, xưng hô độc thoại theo quy ước của chính file. Không ngoại suy tổng dự án từ file này.
- Phân loại 12 dòng sai: **lệch nội dung 3** (1567 mảnh câu chuyển chỗ từ 1718; 2824 phủ định ngược nghĩa; 2914 dịch nghĩa đen sai từ), **chưa dịch (còn nguyên tiếng Trung trong TOML) 0**, **dịch thiếu (cụt câu) 0**, **không chắc chắn 2 nhóm** (2811/2528: JP 小畑 vs TW 大畑; 2976: 冥国 — xem dưới). 9 dòng còn lại là lỗi nhỏ: **dấu câu/thẻ 8** (1687, 1697, 2169, 2182 thừa 「 mở đầu; 2899, 2538 mất dấu mở 『/「; 2025 thẻ `%l` hỏng; 2513 lời dẫn bọc trong ngoặc thoại 「」), **xưng hô 1** (2691 "ông Munakata" trái quy ước "chú Munakata"). Không có dòng nào mang tiếng Trung (VN==TW = 0 trong cả CSV lẫn TOML).
- Thoại sai 6/328 (1,8%); lời dẫn (monologue) sai 6/185 (3,2%). Theo người nói: monologue 6, Olivy 1, Hachiroku 2, Soutetsu 2, Munakata 1; Paulette 0/38, Reina 0/12, Kisaki 0/12.
- **Heuristic thoại/dẫn bắt được 1/513:** đúng 1 dòng lệch loại là 2513 (lời dẫn bọc ngoặc thoại) — và đó là lỗi thật, đã nằm trong 12 dòng sai. Heuristic không thấy 11 lỗi còn lại (cùng loại thoại→thoại sai, dẫn→dẫn sai, hoặc ở mức dấu câu/thẻ/xưng hô). Đây là minh chứng nữa rằng heuristic chỉ là giới hạn dưới.
- **Không có key-shift sạch:** dòng lệch duy nhất là 1567 (mảnh câu từ key 1718, lệch +151 — một lỗi dán nhầm đơn lẻ, không phải lệch đều hệ thống). Không có bằng chứng lệch đều; lỗi xác nhận bằng đọc ngữ nghĩa từng dòng.
- **TOML và CSV giống hệt nhau về nội dung:** 290/513 dòng khác nhau chỉ ở `\n`/khoảng trắng, 0 dòng khác nội dung thực. Không có dòng CSV trống nào trong file này.
- **Không xét lỗi định dạng `\n`:** theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng, `\n` thủ công không quan trọng. Chỉ báo lỗi nội dung. Các bản sửa trong khối TOML bên dưới viết liền một dòng (không chèn `\n` thủ công), trừ 4 dòng 1687/1697/2169/2182 giữ nguyên `\n` đã có sẵn trong bản gốc để không đổi cấu trúc câu.
- **[selections]:** file có tiêu đề section `[selections]` nhưng **rỗng (0 mục)** — không có lựa chọn nào để kiểm tra hay sửa.
- **Thẻ `%l`:** 31 dòng bản Việt gắn thẻ tra cứu `\x%l機関士;#00ffc040;lái tàu%l;#;` trước tên Munakata trong khi JP gốc không có 機関士 ở đó (1097, 1103, 1539, 2480, 2498, 2565, 2634, 2637, 2693, 2695, 2699, 2701, 2705, 2707, 2713, 2715, 2717, 2720, 2722, 2725, 2726, 2730, 2731, 2805, 2830, 2891, 2962, 2966, 2975, 2979, 2997) — bản dịch vẫn đúng nghĩa, chỉ thêm thẻ gloss cho nhất quán với những chỗ JP có 機関士 thật (1708, 1826, 1827). Hieu đã chốt 19/11: **gỡ cả 31 thẻ** (xem Bổ sung ở cuối file) — file này giờ sai 44/513 (13 bản sửa gốc + 31 thẻ gloss). 3 dòng nhắc 宗方さん nhưng không gắn thẻ (1678, 2703, 2921) cho thấy thẻ này được gắn không nhất quán. Không có thẻ `%l` nào bị mất hay lệch ngoài dòng 2025 (đã sửa trong khối).

## Kết luận về cơ chế lỗi
- File này **không bị xáo trộn cột Việt** như các file nặng trước đó: chỉ 1 dòng mang mảnh câu của key khác (1567 ← 1718, trong cùng file, và key 1718 vẫn đúng — không phải hoán đổi), không có dòng "mồ côi" (mọi câu Việt đều có JP/TW tương ứng), không có dòng trùng lặp sai (8 giá trị Việt trùng nhau trong file đều là những câu cảm thán ngắn mà JP cũng giống hệt/na ná nhau: 「A」1751/1695/1664, 「A——」2174/1682/1752, 「!」2185/1686/1666, 「Ừm」1722/1849, 「!!!」1689/1674, 「E he he~」1681/1750, 「Rõ rồi!」1980/1797, 「Ế ế ế!?」1679/1680 — đều đúng).
- **Không có bằng chứng tràn chương ngược:** không dòng Việt nào trong file trùng với các dòng sai của 夜の嵐 (kiểm tra toàn dự án: 0 câu Việt dài ≥12 ký tự trùng với file 夜の嵐); 13 dòng Việt trùng với file khác đều là câu ngắn thông dụng, mỗi dòng đều dịch đúng JP của chính nó. Chiều tràn đã biết là một chiều — từ Hachiroku 12 **sang** 夜の嵐 (32 dòng), không có chiều ngược lại.
- Lỗi còn lại là lỗi dịch thuật lẻ tẻ ở mức câu/chữ/dấu câu, không phải lỗi hệ thống. JP và TW khớp nhau ở mọi dòng sai (trừ 3 dòng chưa chắc chắn), nên mọi dòng sai đều sửa được chỉ bằng cách dịch lại/chuẩn hoá từ JP/TW, không cần thêm nguồn nào khác.
- 501 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Chi tiết 12 dòng sai

### A. Lệch nội dung (3 dòng)
- **1567** (Olivy): JP 「でも、コッカケーカク？　でやったことなら、ちゃんと記録、のこってるんじゃないの？」/ TW tương đương — "Nhưng mà, KẾ HOẠCH QUỐC GIA? Nếu là việc được thực hiện bởi cái đó, thì chẳng phải ghi chép vẫn còn được lưu lại đàng hoàng sao?" Bản Việt cũ nối thêm hai câu thuộc về key 1718 ("Để sau này còn phân tích nguyên nhân thất bại? Không thể áp dụng cho lần sau sao?") — key 1718 vẫn đúng nguyên vẹn, nên đây là mảnh câu bị dán thừa, không phải hoán đổi. Sửa: cắt hai câu thừa.
- **2824** (monologue): JP ハチロクと顔を見合わせたなら、オリヴィがふふん！と誇らしげな声を出す — "Khi [tôi] và Hachiroku nhìn nhau, Olivy hừm! một tiếng đầy tự hào." Bản Việt cũ thêm "Không cần" ("Không cần tôi và Hachiroku nhìn nhau…") khiến câu thành phủ định, ngược nghĩa JP. Sửa: bỏ "Không cần", giữ "hừm!" như bản cũ.
- **2914** (monologue): JP 線路を避けた、犬走りのあたりから掘り進んでいく — "Tránh phần đường ray, [chú ấy] đào tiếp từ khu vực 犬走り." 犬走り ở đây là dải đất hẹp ven đường ray (lối đi hẹp dọc tuyến), không phải "lối đi dành cho chó" — bản Việt cũ dịch nghĩa đen từng chữ 犬 (chó) + 走り (chạy). Sửa: "lối đi hẹp ven đường".

### B. Dấu câu / thẻ / xưng hô (9 dòng)
- **Thừa dấu 「 mở đầu (4 dòng):** 1687 (Hachiroku: 「「!」→「!」), 1697 (Soutetsu: 「「A!」→「A!」), 2169 (Soutetsu: 「「Chuyện đó thì——」→「Chuyện đó thì——」), 2182 (Munakata: 「「A」→「A」) — bản Việt bắt đầu bằng hai dấu 「 nhưng chỉ đóng một dấu 」.
- **Mất dấu mở (2 dòng):** 2899 (monologue: JP 『お前も大したものだったのだな』 — bản Việt mất dấu mở 『, dấu đóng 』 biến thành dấu nháy đơn lẻ `'`); 2538 (monologue: JP 『記録』とは… — cùng lỗi, mất 『 mở, đóng thành `'`).
- **Thẻ `%l` hỏng (1 dòng):** 2025 (Hachiroku) — thẻ ghi `\x%lTuyến núi%l;#;`, thiếu cả thuật ngữ JP lẫn mã màu; dạng đúng là `\x%l山線;#00ffc040;Tuyến núi%l;#;`. Nội dung còn lại của dòng đúng (Tuyến Hisatsu, Teitetsu, Ohimitera giữ nguyên theo quyết định đang chờ). Quyết định 19/11: 御一夜 = Ohitoyo — bản sửa 2025 đã đổi "Ohimitera - Hayato" thành "Ohitoyo - Hayato" trong đợt sửa 19/11.
- **Lời dẫn bọc ngoặc thoại (1 dòng):** 2513 (monologue) — JP là lời dẫn không ngoặc, bản Việt bọc trong 「」 khiến nó hiển thị như thoại. Đây là dòng duy nhất trong file bị như vậy (kiểm tra bằng máy: chỉ 1/185 dòng monologue bắt đầu bằng 「).
- **Xưng hô không nhất quán (1 dòng):** 2691 (monologue) — Soutetsu gọi Munakata là "ông Munakata", trong khi quy ước của file là "chú Munakata" (Olivy cũng gọi "chú" ở 2049). Sửa: "chú Munakata".

## Các cặp trùng lặp / lệch vị trí đã xác nhận (1 cặp, trong file)
- **1567 ← 1718:** hai câu cuối của bản Việt ở 1567 là bản dịch đúng của 1718 ("Để sau này còn phân tích nguyên nhân thất bại? Không thể áp dụng cho lần sau sao?"). Key 1718 vẫn đúng nguyên vẹn nên chỉ cần cắt phần thừa ở 1567, không cần sửa 1718. Không có cặp chuyển chỗ nào khác trong file.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- Soutetsu độc thoại xưng "Tôi" (40/185 dòng monologue có đại từ tôi; 0 dòng xưng "mình" ở vị trí chủ ngữ — 5 lần "mình" còn lại đều là thành ngữ: "hết sức mình" 2489, "một mình" 2583, "bản thân mình" 2633, "cổ mình" 2867, "giật mình" 2691 — đều đúng, không tính lỗi); Soutetsu thoại xưng "tôi"; Olivy gọi Soutetsu là "anh Soutetsu"; Hachiroku gọi Soutetsu là "ngài Soutetsu"; Munakata xưng "Tôi", gọi Soutetsu là "cậu Migita".
- 帝鉄 = "Teitetsu" dạng ngắn trong cả 6 lần xuất hiện (2252, 1848, 2875, 2710, 2025, 2015) — **chưa chốt** (docs: "Đường sắt Hoàng gia (Teitetsu)"); giữ nguyên như bản gốc, không đổi trong khối sửa.
- 御一夜: file dùng lẫn ba dạng — "Ohito" (~14 dòng: 2058, 1760, 1746, 1900, 2565, 2089, 2104, 2753, 2477, 2554, 2224, 1626, 1590, 2233), "Ohimitera" (12 dòng: 1705, 1900, 1847, 1525, 1886, 1658, 1955, 2089, 2176, 2025, 1650, 2027), "Ohitoyo" (2 dòng: 2191, 2049); hai dòng 1900 và 2089 chứa cả hai dạng trong cùng một câu ("Đường sắt Ohito" + "thành phố Ohimitera") — **chưa chốt**, ghi nhận để Hieu quyết một dạng thống nhất.
- 御一夜鉄道 = "Đường sắt Ohito" (2058, 1746, 1760, 1900, 2089, 2224, 2753, 2755, 2233) và "Công ty Đường sắt Ohitoyo" (2926); 御一夜市 = "thành phố Ohimitera" (1900, 1847). 術仙車両工場 = "nhà máy chế tạo toa xe Jutsu-sen" (1525 — có gạch nối, khớp chuẩn audit 廃炭鉱); 術仙炭鉱 = "mỏ than Jutsu-sen" (2092, 2191). ガンスコ giữ "Gansuko" (1869, 2644, 2713); エアクラ = "Aircra"; "Cowcatcher" giữ nguyên tiếng Anh (1604) — nhất quán với phong cách dự án, không tính lỗi. 隆起 = "phồng rộp" (2811, khớp nghĩa "mặt đất phình lên" như 実りの秋 dùng "phình lên").
- Còi tàu ポー không xuất hiện trong file này. Trailing "——っ" giữ nguyên theo sfx §3.

## Dòng không chắc chắn (2 nhóm, 3 key — cần Hieu xác nhận, KHÔNG nằm trong khối TOML)
- **2811 + 2528** (monologue): JP 小畑 / 小畑線 vs TW 大畑 / 大畑線 — hai nguồn mâu thuẫn nhau về tên địa danh; bản Việt theo TW thành "Okoba" (cả hai chỗ), mà "Okoba" không khớp cách đọc nào của 小畑 (Obata) hay 大畑 (Ohata). Bằng chứng nghiêng về JP: chương Hachiroku 11 có tên gốc là 御一夜鉄道小畑線 (tuyến Obata). Cần Hieu chốt: (a) lấy 小畑 hay 大畑, (b) cách viết: "Obata" / "Ohata" / giữ "Okoba".
- **2976** (monologue): JP 冥国製 (sản xuất tại Minh Quốc — xứ âm phủ) vs TW 美国製 (sản xuất tại Mỹ). Bản Việt để nguyên không dịch: "Meikoku". Lựa chọn: (a) "Mỹ" (theo TW), (b) "Minh Quốc" (dịch sát JP, song song với quyết định 19/11 của Hieu: 冥軍 = "Minh Quân", vì TW cũng dịch 冥軍 thành 美軍 theo cùng một kiểu). "Minh Quốc" là lựa chọn nhất quán, nhưng cần Hieu xác nhận trước khi áp dụng.

## Quyết định của Hieu 19/11 — ĐÃ CHỐT (ghi thêm sau audit)
- **小畑 / 大畑 → 小畑, phiên âm "Okoba":** chốt theo bản gốc trong game (tên chính thức là 小畑, tuyến 小畑線; Maitetsu đổi chữ nhẹ từ địa danh thật ở Kumamoto như 人吉 → 御一夜; ngoài đời ga mẫu là 大畑駅 nhưng tên trong game là 小畑). Kiểm tra toàn dự án: bản Việt đã dùng "Okoba" cho 小畑 ở 43 chỗ, gồm cả chương ハチロク04_小畑越え ("vượt đèo Okoba", "ga Okoba") — đó chính là quy ước phiên âm Romaji của team. **Kết luận: 2811 và 2528 KHÔNG cần sửa** — "Okoba" đã đúng theo quy ước của team; nhận định cũ trong audit ("Okoba không khớp cách đọc nào") là sai. Ngược lại, 4 chỗ dùng "Obata" (ハチロク15a 1842, 1455; ハチロク15b 1999; 日々姫01 2225) là thiểu số lệch quy ước — cần thống nhất về "Okoba" khi audit tới các file đó. Nếu trong script có dòng lạc chữ 大畑 giữa loạt 小畑, khả năng cao là lỗi gõ nhầm của tác giả — thống nhất về 小畑.
- **冥国 → "Minh Quốc":** chốt. 冥国 là tên hư cấu thay cho 米国 (Mỹ), tương tự cách đặt 冥軍 cho quân đội nước này; dùng "Minh Quốc" đảm bảo nhất quán với tiền lệ 冥軍 = "Minh Quân" trong hệ Hán-Việt toàn dự án. Lưu ý: ở vài chỗ (như mô tả nguồn gốc của Olivy) 冥国 có furigana メリケン (Meriken) — 9 chỗ trong JP, toàn ở Hachiroku 03/05/09/10/15a/15b, dạng "[メリケン,2]冥国式". Quy tắc áp dụng: khi メリケン là từ được nói ra (lời thoại, vd. 「メリケン？」) thì giữ "Meriken"; khi nó chỉ là furigana trên 冥国 thì bản dịch chính vẫn là "Minh Quốc". **Bản sửa cho 2976 ở khối bổ sung dưới đây** — chỉ đổi "Meikoku" → "Minh Quốc", giữ nguyên thẻ `%l`.
- **御一夜 → "Ohitoyo":** Hieu chốt gần như hoàn toàn ("gần như đã chốt xong hoàn toàn") dựa trên bằng chứng 8/8 trong file 再開発 kèm furigana おひとよ. Khối sửa của các file đã audit dùng "Ohimitera" (Grand 01, Hibiki 03, Paulette 04 stove) đã được sửa lại thành "Ohitoyo" trong đợt sửa 19/11 (Grand 01: 30 dòng, Hibiki 03: 7 dòng, Paulette 04 stove: 4 dòng, 夜の嵐: 2 dòng, haitan: 2 dòng); trong file này, dòng 2025 trong khối chính cũng đã đổi "Ohimitera - Hayato" thành "Ohitoyo - Hayato" trong đợt đó.

## Đề xuất cập nhật context (để Hieu quyết, KHÔNG tự đổi toàn dự án)
1. **Thẻ gloss 機関士 cho 宗方さん — gỡ hay giữ:** 31 dòng gắn thẻ `\x%l機関士;#00ffc040;lái tàu%l;#;` trước tên Munakata dù JP không có 機関士 (danh sách ở mục Phương pháp). Đây là gloss thêm cho rõ nghĩa, không sai nghĩa — nhưng gắn không nhất quán (3 dòng 1678, 2703, 2921 nhắc 宗方さん mà không gắn thẻ). Hieu chọn một trong hai: (a) giữ nguyên như một quy ước gloss của file, (b) gỡ 31 thẻ để giống hệt bản gốc.
2. **冥国 → "Minh Quốc":** theo đúng tiền lệ 冥軍 = "Minh Quân" (Hieu chốt 19/11), 冥国 nên là "Minh Quốc" thay vì "Mỹ" (TW) hay để nguyên "Meikoku". Chờ Hieu xác nhận ở dòng 2976 trước khi áp dụng.
3. **小畑 / 大畑:** xem dòng chưa chắc chắn 2811/2528 ở trên — quyết định này ảnh hưởng cả tên tuyến 小畑線 ở Hachiroku 11.
4. **御一夜 — Ohito / Ohimitera / Ohitoyo:** file này dùng lẫn cả ba dạng (xem mục Thuật ngữ). Quyết định 19/11: 御一夜 = Ohitoyo — bản sửa 2025 đã đổi sang "Ohitoyo - Hayato" (đợt sửa 19/11); các dòng đúng dùng lẫn ba dạng vẫn chờ đợt thống nhất sau.

## Giới hạn của audit này
- Đã đọc hết 513 dòng script của file này: 12 dòng sai đã xác nhận, 3 key chưa chắc chắn (2 nhóm), 498 dòng còn lại khớp JP/TW.
- Vẫn có thể sót vài dòng "trông hợp lý nhưng thực ra là bản dịch của dòng khác" — cách chắc chắn nhất vẫn là chơi qua chương và đối chiếu voice. Nếu Hieu gặp thêm dòng nào nghi ngờ trong file này thì gửi mình, mình kiểm tra nốt.
- File này (2,3% sai) sạch hơn hẳn 5 file nặng trước (31%–86,2%) và sạch thứ hai toàn dự án, chỉ sau 実りの秋 (0,4%). Tổng 8 file đã audit xong: 133 + 255 + 299 + 374 + 199 + 2 + 20 + 12 = **1.294 dòng sai**.

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)
Lưu ý khi chép: các bản sửa viết liền một dòng, không chèn `\n` thủ công — theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng. Ngoại lệ: 4 dòng 1687/1697/2169/2182 giữ nguyên `\n` đã có sẵn trong bản gốc. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng. Khối này đã kiểm tra bằng máy: trích khối từ chính file review, parse bằng tomllib — **12/12 key** khớp đúng tập dòng sai, không thừa không thiếu, giá trị sau khi parse khớp đúng bản sửa. Các dòng chưa chắc chắn (2811, 2528, 2976) KHÔNG nằm trong khối này.

```toml
1567 = "「Nhưng mà, KẾ HOẠCH QUỐC GIA? Nếu là việc được thực hiện bởi cái đó, thì chẳng phải ghi chép vẫn còn được lưu lại đàng hoàng sao?」"
1687 = "「!」\\n「Reina」"
1697 = "「A!」\\n「Chà!」"
2025 = "「Vâng, đúng vậy ạ. \\x%l山線;#00ffc040;Tuyến núi%l;#; này——nguyên là Tuyến Hisatsu của Teitetsu, đoạn Ohitoyo - Hayato, được cho là tuyến đường sắt quân sự」"
2169 = "「Chuyện đó thì——」\\n「Ngược lại đấy, Olivy」"
2182 = "「A」\\n「Tuyến đường quân sự?」"
2513 = "Giọng nói của Hachiroku khiến tôi thở phào nhẹ nhõm. Với giọng điệu này, chắc chắn em ấy đã nghĩ ra cách để giúp tôi."
2538 = "『Ghi chép』 không chỉ là thông tin vị trí sao."
2691 = "Bị đánh trúng điểm mù, chú Munakata giật mình khựng lại trong giây lát."
2824 = "Khi tôi và Hachiroku nhìn nhau, Olivy đã hừm! một tiếng đầy tự hào."
2899 = "『Nhóc cũng cừ lắm đấy chứ』 ——Dù không nói ra, nhưng lời đó vẫn truyền đạt được."
2914 = "Tránh phần đường ray, chú ấy bắt đầu đào từ khu vực lối đi hẹp ven đường."
```

## Khối TOML bổ sung — quyết định 19/11 (chỉ 1 key: 2976)
Áp dụng cùng khối chính. Khối này đã kiểm tra bằng máy: trích từ chính file review, parse bằng tomllib — **1/1 key**, giá trị sau khi parse khớp đúng bản sửa. 2811 và 2528 không có mặt ở đây vì đã đúng sẵn ("Okoba" là quy ước của team cho 小畑 — xem mục Quyết định).

```toml
2976 = "Nghe vậy, tôi mới nhận ra. Olivy được sản xuất tại Minh Quốc——là một \\x%lレイルロオド;#00ffc040;Railord%l;#; được chế tạo ở quốc gia chiến thắng trong cuộc \\x%l大戦;#00ffc040;Đại chiến%l;#; trước."
```

*Ghi chú 19/11 (sau khi Hieu kiểm tra chính tả): "Railord" 1 chữ l và "Olivy" đã đúng theo glossary của team (translation_guidelines.md:40 và context_trans.md mục 68 chốt レイルロオド = Railord; toàn dự án dùng Railord 907 lần, Raillord 0 lần; Olivy 1.434 lần, Olivi 0 lần — dòng TRANSLATION_GUIDE.md:48 ghi Olive/Olivia là ghi chú cũ, không khớp thực tế dùng). Dấu —— theo quy ước của team là dính cả hai bên (22.055 chỗ trong dự án, so với chỉ 2 chỗ có khoảng trắng hai bên), nên bản sửa viết "Minh Quốc——là" thay vì "Minh Quốc—— là".*

## Việc tiếp theo
1. Áp dụng khối TOML trên cho file Hachiroku 12_ムナカタ来訪 (nhớ quyết 2 nhóm dòng chưa chắc chắn và 4 đề xuất context ở trên trước, để khỏi sửa đi sửa lại), chơi thử chương rồi báo lại.
2. Audit file còn lại của Hachiroku 12 (再開発) — xem bản review riêng.
3. Xuất lại CSV mới từ TOML (sau khi áp fix) để CSV không còn cũ — với CSV3 thì chỉ còn 2 dòng lẻ chưa dịch (lr真闇追加01/02) là cần dịch mới; 144/146 dòng chưa dịch đã có bản dịch trong các khối audit (Grand 01: 100, Hibiki 03: 44).

## Kết bài
Hachiroku 12_ムナカタ来訪 là file thứ tám được audit toàn bộ, và là file sạch thứ hai toàn dự án (2,3% sai, chỉ sau 実りの秋 0,4%): không bị xáo trộn cột Việt, không có dòng chưa dịch, không có dòng mồ côi hay tràn từ chương khác — 12 lỗi còn lại chỉ là những sai sót lẻ tẻ ở mức câu/chữ/dấu câu (3 chỗ lệch nội dung, 8 chỗ dấu câu/thẻ, 1 chỗ xưng hô). Quan trọng hơn, file này trả lời câu hỏi đã đặt ra từ audit 夜の嵐: **cột Việt của Hachiroku 12 không bị nhiễm ngược** — chiều tràn chỉ đi một chiều, từ Hachiroku 12 sang 夜の嵐, và 32 câu Việt bị copy sang đó đều đang đứng đúng chỗ ở đây.

Việc còn lại của riêng file này chỉ là 2 nhóm dòng chưa chắc chắn (小畑/大畑, 冥国) và 4 quyết định context đang chờ chung cho cả dự án (thẻ gloss 機関士, 冥国, 小畑線, 御一夜); sau đó là áp dụng khối TOML 12 dòng và chơi thử chương để nghiệm thu. Còn về tổng thể dự án, tám file đã audit xong đã có 1.294 dòng sai — và việc hai file Hachiroku 12 đều sạch cho thấy sau khi xong các file nặng trong danh sách, vẫn nên tiếp tục audit các file còn lại thay vì cho rằng phần còn lại đều ổn.

---
**Bổ sung 19/11 (quyết định 12 — Hieu):** gỡ 31 thẻ gloss `\x%l機関士;#00ffc040;lái tàu%l;#;` / `Lái tàu` thêm vào trước tên Munakata (JP không có 機関士 ở 31 dòng này). Mỗi bản sửa = bản cũ trừ đúng thẻ gloss (và 1 khoảng trắng thừa do thẻ để lại) — đã kiểm chứng từng dòng bằng difflib (chỉ có thao tác xóa, không đổi chữ nào khác), JP không có 機関士, không còn thẻ, không dư khoảng trắng. Khối TOML 31 dòng dưới đây parse OK, khớp JSON.

```toml
[script]
1097 = "...Nhìn cách đối xử của Munakata, tôi cũng hiểu ra phần nào. Munakata quả thực sử dụng Olivy rất thành thạo."
1103 = "...Thực sự làm việc rất chăm chỉ. Cả Munakata và Olivy. Vừa thán phục, đồng thời tôi cũng hiểu ra."
1539 = "「Không, em cứ đứng đó là được rồi. Tóm lại, tôi muốn em quan sát và ghi chép lại quá trình làm việc của Munakata.」"
2480 = "Munakata bối rối ngồi phịch xuống ghế, chiếc ghế mà chú ấy vừa định nhổm dậy."
2498 = "Nhưng Olivy vờ như không có chuyện gì, với điệu bộ thường ngày, quay sang hỏi Munakata."
2565 = "Nhưng, Munakata đã đón nhận lời nói của Reina——văn hóa của Đường sắt Ohito, ít nhất là ngoài mặt, mà không hề bận tâm."
2634 = "Giọng nói của Olivy trong trẻo, quang đãng, không một chút vẩn đục. Có lẽ do sự lệch pha trong cuộc trò chuyện. Bàn tay của Munakata bất giác dừng lại."
2637 = "Tiếng hoan hô bật ra từ cổ họng Olivy. Cho đến khi ý định của Munakata được xác nhận, để không làm em ấy mừng hụt——"
2693 = "Phập, phập, phập. Munakata vừa đào một địa điểm khác, vừa nói."
2695 = "Munakata cũng cúi đầu——và thậm chí cả Olivy cũng làm theo."
2699 = "Ngay khi Munakata vừa nhận lấy, Olivy đã chúi mũi vào xem, nhưng không hề bị la mắng hay ngăn cản."
2701 = "Bàn tay Munakata chuyển động."
2705 = "Khẽ cúi chào. Khi Munakata quay người lại, Olivy cũng lập tức đi theo sau."
2707 = "Tiếng cười bật ra từ mũi Munakata."
2713 = "Giao máy ảnh và kẹp tài liệu cho Olivy, Munakata thản nhiên dùng Gansuko đào phần bị phồng rộp——"
2715 = "Tới đây, Munakata lại tỏ ra bối rối. Có vẻ như chú ấy không giỏi lấy ví dụ cho lắm."
2717 = "Munakata di chuyển sang địa điểm khác."
2720 = "Munakata vuốt mạnh cằm và lắc đầu."
2722 = "Munakata đứng dậy."
2725 = "Vừa nói, ánh mắt của Munakata chợt hướng về phía tôi."
2726 = "Munakata, quay về phía chúng tôi."
2730 = "Munakata mang vẻ mặt nhẹ nhõm, nhưng ngay lập tức, nét mặt lại trở nên nghiêm nghị."
2731 = "Câu trả lời của Munakata chỉ là một cái gật đầu. Truyền đạt rõ ràng rằng hoàn toàn không có chỗ cho sự thỏa hiệp hay giải pháp nào khác."
2805 = "Munakata có tinh thần ham học hỏi cao, khả năng nắm bắt tình hình nhạy bén—— Có thể cảm nhận được chú ấy là một người cực kỳ phù hợp với công việc thực tế, một người rất có năng lực."
2830 = "Nếu vậy thì có lẽ, về quản lý doanh nghiệp đường sắt hay những thứ tương tự—— Những bài giảng đó, Munakata cũng đã từng tham gia."
2891 = "Paulette lấy máy tính ra. Vừa nhìn vào tờ giấy vừa bấm máy, rồi nhẹ nhàng đẩy về phía Munakata."
2962 = "Bằng một cử chỉ coi đó là điều hiển nhiên, Olivy dang chụp ảnh lại quá trình làm việc của Munakata."
2966 = "Munakata đáp lại cũng rất rõ ràng."
2975 = "Gần như chắc chắn Munakata đã từng có kinh nghiệm xử lý những biện pháp như vậy. Cảm giác đó giúp tôi vơi bớt phần nào sự bất an."
2979 = "Olivy hạnh phúc khi được làm việc, khi được sử dụng. Nếu người đó là Munakata, thì có lẽ, hơn bất cứ điều gì——"
2997 = "Có lẽ vì có ấn tượng tốt với điều đó, khuôn mặt nghiêm nghị của Munakata, khẽ giãn ra."
```
