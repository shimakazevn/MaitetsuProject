# Moan-fix snippet — 日々姫h5_白濁絵の具の射精会.txt.toml (moan-hibikih5-hakudaku-enogu)

- File: `日々姫h5_白濁絵の具の射精会.txt.toml` — route 02_Hibiki, 343 dòng script, audit trước đó 39 sai.
- Đã đọc 343/343 dòng; xét 153 dòng rên/SFX (thoại 105 + monologue 48, gồm 44 dòng SFX （）).
- Đổi 3 dòng (nguyên âm 1, moan 2), giữ 150 dòng rên/SFX.
- Nguyên âm 1: 1153 ひゅっ！あああああああああんっ "Hyu! Aaaaaaaaaaaan" (12 a) → "Hyu! Aaaaaaaaan" (9 a) — áp lại fix audit đã bị parent loại, với giá trị ĐÚNG 9 a (JP 9 a + 1 n, đếm bằng máy).
- Moan 2: 1215 はっ "A!" → "Hà!" (mất phụ âm h — ngoại lệ duy nhất của quy ước はっ→"Hà" trong file); 1255 ふ、ぅ "phù" → "phù, u" (âm ぅ bị mất hẳn; tiền lệ 1190 ふ、ぁ→"phù, a"; TW hai tiếng 呼).
- Đồng ý toàn bộ 37 fix moan/gasp/nguyên âm còn hiệu lực của audit; phán lại và đồng ý cả hai phán đoán của audit: 1264 "Nukyu" (ん-う-きゅ đủ 3 mora) và 1154 "Po" (ぽッ là âm tiết おちんぽ bị cắt; "ưm" cũ là âm mũi không có trong JP).
- Đếm nguyên âm kiểm tra lại bằng máy cho mọi chuỗi moan dài: 1151 8a/2n, 1156 10a, 1157 1a/1u/1n, 1152 1a/1u/2n, 1212 12u/6n, 1213 9u, 1228 18o, 1261 3u, 1265 6u, 1269 3u, 1226 5u — tất cả khớp.
- Không dòng gasp Ư nào bị xem lại; không dòng "Kh" nào bị đổi; không có dòng ふぇ/ふや hay dòng cười nào trong file.
- Cờ: F1 1189 không phải dòng moan — MEMORY 22/11 ~02:47 đã quyết bỏ "đã bao phủ", áp ở đợt thống nhất; F2 1215 "Hà!" là fix mới — parent xem lại ở lúc gộp nếu thấy "A!" là diễn có chủ ý.
- Lượt soát 2: 3/3 tái kiểm chứng, 0 bỏ, 0 sửa (kiểm tra cơ học bắt 1 lỗi mã hoá `\n` trong bản nháp JSON — đã dựng lại từ CSV3, khớp tuyệt đối).
- Chi tiết đầy đủ: `moan-hibikih5-hakudaku-enogu-REVIEW.md`; danh sách sửa: `moan-hibikih5-hakudaku-enogu-wrong.json`.
- **Tổng cộng sau file này: 48 file / 1242 dòng sai (moan)** (cơ sở 47 file / 1239 dòng + 3 file này — cơ sở đã kiểm chứng trực tiếp dòng tổng của ROUTE-MOANS.md)
