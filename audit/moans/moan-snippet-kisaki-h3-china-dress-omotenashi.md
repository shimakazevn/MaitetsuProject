# Moan-fix snippet — 稀咲h3_チャイナドレスでおもてなし.txt.toml (moan-kisaki-h3-china-dress-omotenashi)

- File: `稀咲h3_チャイナドレスでおもてなし.txt.toml` — route 06_Kisaki, 662 dòng script, TOML md5 `3bccfb4626ff9b0e014a8655d1091f7e`, không có bản trùng.
- CSV3: 1 bộ duy nhất (thư mục `06_Kisaki`), 662/662 dòng, 0 khóa trùng; VN TOML-2 khớp CSV3 sau chuẩn hóa `\n`.
- Đã đọc 662/662 dòng; xét 181 dòng rên/SFX (97 thoại Kisaki + 14 thoại Soutetsu + 70 độc thoại, gồm 58 dòng SFX trong ngoặc).
- Đổi 23 dòng: romaji 19 + độ dài nguyên âm 2 + âm sai 2.
- Romaji fa/fu → "Fua" (13): 1538, 2120, 2152, 2170, 2188, 2195, 2225, 2252, 2253, 2254, 2360, 3808 + 2207 (ぷぁ "Pha"→"Pua"); nhất quán với "Fua!" sẵn có ở 2255.
- Romaji họ hia/hya/hyu (4): 2197 ひあっ "I a"→"Hia" (+ たらぁっ "thì"→"thì a"), 2198 ひウっ "I ư"→"Hiu", 2206 ひゅっ "Hưu"→"Hyu", 2277 んひゅんっ "Ưm hưu"→"Nhyun".
- Romaji gộp mảnh rời của âm dài (2): 2155 んうううっ "ư ư ư"→"Nuuu", 2257 くふぅんんんん "Khu phư ưm"→"Kufuunnnn".
- Độ dài nguyên âm (2): 2162 ひゃうっっ "Hya"→"Hyau", 2269 れるうっ "rero"→"Reroo".
- Âm sai (2): 2228 う……む "Ư…… m"→"Ư…… ừm", 2238 ほーへふっ "Anh Houhehu"→"Anh Houhefu" (chỉ sửa ふ "hu"→"fu"; phần bỏ "Anh" parent đã lùi — là sửa đại từ, không thuộc moan; ghi cờ cho đợt thống nhất).
- Giữ 158 dòng rên/SFX, gồm 11 dòng gasp Ư của sweep đã khóa (audit áp nguyên; 4 dòng 2170/2188/2253/2257 giữ Ư của audit trong fix value — dùng fix moan, không áp thêm fix audit cùng key).
- Giữ theo tiền lệ audit đã khóa: "a a"/"á á" (ああっ), "Phuaaaaưm!" (2240), "rồiiiiii" (2116), "Ưm kyu" (2278), "Ưm ưm" (2279), "khưuuuuu" (2398); JP tự tách ("Fu…… a", "fu, a", "phu, á") giữ theo cấu trúc JP; "phù"/"fu" cho ふっ/ふうっ ngắn giữ.
- Sweep: 13 mục đã kiểm chứng — 11 fix Ư audit áp nguyên, 2 already-rendered (3373, 3483); không sửa lại dòng gasp Ư nào.
- Lượt soát 2: tổng 23 / tái kiểm chứng 23 / bỏ 0 / sửa 0 (bản nháp JSON đầu làm mất dấu 「 」, bắt được khi in kiểm tra lúc build, đã sửa trước lượt soát 2).
- Parent kiểm chứng 21/11 ~10:00: JSON 23, TOML 23 khóa 0 sai lệch, CSV3 23/23; 4 key trùng audit chỉ khác đúng token rên; Ư thêm vào đều là Ư của audit; SỬA 2155 "Nuuuu"→"Nuuu" và 2257 "Kufuuunnnn"→"Kufuunnnn" (đếm thừa 1 u); LÙI 2238 phần bỏ "Anh" (sửa đại từ, ghi cờ đợt thống nhất).
- Chi tiết đầy đủ: `moan-kisaki-h3-china-dress-omotenashi-REVIEW.md`; danh sách sửa: `moan-kisaki-h3-china-dress-omotenashi-wrong.json`.

**Tổng cộng sau file này: 8 file / 205 dòng sai (moan)** (cơ sở 7 file / 182 dòng + 23 file này)
- FLAG (đợt thống nhất): 4 fix value gộp cả Ư của audit (2170, 2188, 2253, 2257) — dùng fix moan, KHÔNG áp thêm fix audit cùng key. 2238: "Anh" giữ lại (parent lùi phần bỏ "Anh" — sửa đại từ, không thuộc moan); cờ: "Anh" là cách xưng Kisaki→Soutetsu hay từ bịa của Gemini (TW 呼 = tiếng thở)? 2197 thêm "a" cho たらぁっ (ぁ là mora nguyên âm, không phải chỉ っ).
