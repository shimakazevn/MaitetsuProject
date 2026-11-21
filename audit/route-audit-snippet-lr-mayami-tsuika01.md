## 05_Mayami lr真闇追加01 — 新婚旅行のリクエスト — 142/300 (47,3%)

- File thêm về tuần trăng mật (Soutetsu + Mayami bàn lịch trình trên Navi, chọn Reina làm hướng dẫn viên), kiểm tra ĐẦY ĐỦ 300 dòng. File bẩn thứ nhì dự án, gần một nửa sai — gần như toàn bộ là lệch hàng: 2 chuỗi xoay (A: 114 mắt xích, đầu là bản của 1036 → 1177 → … → 1736; B: 9 mắt xích, 1175 → 1283 → … → 1264), khép kín trong file, 0 dòng mồ côi.
- Phân loại: misaligned 125 (123 thu hồi + 1 dịch mới 1036 + 1 lặp hợp lệ 1175), terminology 8, pronoun 7, gasp 2. Hội thoại 109/229 (47,6%), độc thoại 33/71 (46,5%).
- 0 contamination (chỉ mục VN toàn dự án: 0/142) / 0 orphan / 1 untranslated (1264 — thu hồi bản đúng từ key 1744; dòng chưa dịch còn lại toàn dự án nằm ở lr真闇追加02) / 0 duplicate key / 0 uncertain.
- CSV↔TOML: 76 khớp tuyệt đối + 223 làm phẳng `\n`, 1 khác biệt thực chất (1264: TOML giữ văn TW làm placeholder, CSV trống). Thẻ `%l`: JP 0, VN 0.
- Sweep: 2 mục (1077, 1657), cả 2 áp nguyên văn sau khi kiểm chứng trực tiếp; quét 150 dòng JP có っ, không còn gasp sót (1080 うふふっ và 1097 わああっ là dòng lệch, bản đúng đã có tiếng cười/tiếng hét; 1474 là っ giữa từ ってことは, không phải gasp).
- Lượt soát 2: 142/142 đọc lại đối chiếu JP, 139 tái kiểm chứng, 0 bỏ, 3 sửa (1036, 1077, 1175 — cả 3 đều thiếu dấu 「 」 trong bản viết tay, đã bổ sung và chạy lại toàn bộ kiểm chứng máy). JSON 142 khóa chuỗi; khối TOML parse OK, 142 khóa, 0 sai lệch.
- Phán đoán ghi chú: 1086 んふふっ → "Ưm fufu" giữ nguyên (tiếng ưm mũi + cười, không phải rên; nhất quán với bản ở 1271); 1087 おっと → "Ây da" giữ nguyên (cảm thán hợp lệ, cùng họ với あら/ありゃ trong file); 1606 路子 = Michiko dịch đúng theo JP (TW lược, JP thắng); 1479 Soutetsu "anh nhờ em" với Reina là ĐÚNG (Reina thuộc nhóm "anh"); 1494 giữ gloss "xúc than" cho 投炭 (đa số trong file), chỉ bỏ "dồn toa" theo quyết định 1027 của Hieu. Lượt quét đại từ bắt thêm 1 lỗi lần đọc đầu bỏ sót (1281 "em"→"tôi"); quét lại toàn bộ bản thu hồi bắt thêm 3 lỗi "em"→"tôi" trong bản thu hồi (1071, 1249, 1283).
- Ohitoyo trong file: 13 dòng đã sửa (7 thuật ngữ thuần + 6 trong bản thu hồi) — còn 0. Yui→Yunoi: 2 dòng — còn 0. Migita System→Migita Ichi: 1 dòng — còn 0. "dồn toa": 1 dòng (1494) — còn 0.

**Tổng cộng sau file này: 61 file / 3.477 dòng sai** (cơ sở 60 file / 3.335 + 142 file này).
