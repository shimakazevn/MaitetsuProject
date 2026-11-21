# Moan-fix snippet — lr_真闇h1_僕のおねえちゃん.txt.toml (moan-lr-mayamih1-boku-no-oneechan)

- File: `lr_真闇h1_僕のおねえちゃん.txt.toml` — route 05_Mayami, 317 dòng script, audit trước đó 59 sai.
- TOML md5: `4baa00ccc02ca48bed882887b182d798`, không có bản trùng.
- CSV3: 1 bộ duy nhất, 317 dòng, 0 key trùng; VN khớp TOML 314/317 (3 dòng còn lại chỉ khác TOML-2 làm phẳng `\n` thành khoảng trắng).
- Đã đọc 317/317 dòng; xét 175 dòng rên/SFX/gasp (112 thoại rên + 63 SFX ngoặc đơn độc thoại).
- Đổi 7 dòng: 1167 はぁっ×3 "Hà"→"Haa" (audit bỏ sót, cùng lỗi 1659); 1433 ふぅっっっ "Fuuuu"→"Fuu" (fix audit "Foo" sai nguyên âm — THAY THẾ giá trị audit); 1457 んふふっ "ưm fufu"→"Nfufu" (một âm, một cách diễn; tiền lệ toàn file); 1464 ァァァ "Aaaa"→"Aaa" (3 a); 1598 thêm "ha" cho はっ (THAY THẾ giá trị audit — giữ đại từ + gasp của audit); 1816 thêm "ku" cho くっ―― cuối độc thoại (TW 嗚); 2029 ああ cuối độc thoại "a"→"aa".
- Kiểm chứng 17 fix rên/SFX của audit: 16 đúng (đếm cơ học lại 1466 12 a, 1467 8 a, 1492 19 u, 2145 11 t, 1531 6 u, 1484 3 a — đều đúng), chỉ 1433 sai nguyên âm. Không có dòng romaji mới cho họ ひゃ/ひあ/きゃ.
- Giữ ~168 dòng rên/SFX (họ ふぁ→"Fua", はぁ→"Haa", くあ→"Kua", んひゅ→"Nhyu", cười "Nfufu"/"Ufufu", んっ→"Ưm", SFX từ Việt theo quy ước file; っ nhấn mạnh cuối câu không thêm Ư).
- Sweep: 20 mục đã kiểm chứng — 16 audit đã áp đúng, 4 already-rendered (1428, 1503, 1698, 1803); không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào.
- Cờ cho đợt thống nhất: 2 (1433 — dùng "Fuu!!!!" thay "Foo!!!!" của audit; 1598 — dùng giá trị moan có "ha", thay giá trị audit).
- Lượt soát 2: tổng 7 / tái kiểm chứng 7 / bỏ 0 / sửa 0. JSON 7 mục, khóa string, jp/tw/old_vn khớp CSV3 7/7. Khối TOML parse bằng tomllib: 7 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-mayamih1-boku-no-oneechan-REVIEW.md`; danh sách sửa: `moan-lr-mayamih1-boku-no-oneechan-wrong.json`.

**Tổng cộng sau file này: 20 file / 475 dòng sai (moan)** (cơ sở 19 file / 468 dòng + 7 file này)
- FLAG (đợt thống nhất): 1433 — dùng giá trị moan 「Fuu!!!!」 thay fix audit 「Foo!!!!」 (JP ふぅ = fuu, codepoint U+3045; TW 呼嗚). 1598 — dùng giá trị moan có "ha——" thay giá trị audit (khôi phục hơi thở はっ, tiền lệ 1630).
