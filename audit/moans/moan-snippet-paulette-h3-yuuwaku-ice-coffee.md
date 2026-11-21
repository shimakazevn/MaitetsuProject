# Moan-fix snippet — ポーレットh3_誘惑アイスコーヒー.txt.toml (moan-paulette-h3-yuuwaku-ice-coffee)

- File: `ポーレットh3_誘惑アイスコーヒー.txt.toml` — route 03_Paulette, 279 dòng script, TOML md5 `884568f018ff870371ba906804c8651c` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 279 dòng, 0 key trùng; VN khớp TOML 279/279 sau chuẩn hóa `\n`/khoảng trắng (audit đã kiểm chứng; 37 key sửa kiểm tra lại 0 sai lệch).
- Đã đọc 279/279 dòng; xét 139 dòng rên/SFX (57 Paulette + 16 Soutetsu H + 66 độc thoại, gồm 26 SFX ngoặc).
- Đổi 37 dòng: 13 romaji + 7 đếm nguyên âm + 17 sai âm.
- Romaji fa/fu: 897/915/917/919/937/940/950/1070 ふあっ/ふぁっ→"Fua", 948 ぷあっ→"Pua", 977 ぷぁ→"Pua", 982 ふやっ→"Fuya"; 966 れろおおおっ→"Reroooo" (4 o), 968 れるうううううっ→"Reruuuuuu" (6 u), 974 ずろぉぉぉぉぉぉっ→"Zurooooooo" (7 o).
- Đếm nguyên âm: 899 ひゃ…んっ thêm "n" (7 a đã đúng), 920 ふぃぁ…→"Phi"+11 a, 923 ずりゅう…→"Sụ"+11 ụ+"t", 927 thêm 1 a + "n" (13 a), 931/933/942 ちゅううっ→"chụụụt" (3 u), ちゅうっ→"chụụt" (2 u); 948 はぁっ→"hàà" (2 a), はぁああっ→"Hàààà" (4 a); 915 ハァッ→"hàà"; 974 すうっ→"Suụt".
- Sai âm: 898/902/903 きゃっ→"Kya"/"Kyaa", 904 ひゃっ→"Hya", 890/893/894/897 や→"Ya"/"Yaa", 900 くひゅっ→"Kuhyu", 982 くひゅんっ→"Kuhyun", 906 くっ→"Ku", 938 ぅあっ→"Ua", 955 うぁっ→"Wa", 914/946/966/970 ちゅむっ→"chumu", 914/931 ちゅばっ→"Chuba", 933 ちゅぶっ→"chubu", 969 じゅぼっ→"Jubo", ぢゅぶっ→"Jubu", 970 ぢゅぼっ→"Jubo", じゅろっ "Chụtttt"→"Chụt", 967 ちゅる―― (không っ)→"Churu".
- Kiểu lỗi chính: họ fa/fu bị Việt hoá "phù" mất hẳn âm a; rên dài kéo bằng phụ âm t/m thay vì nguyên âm; phụ âm mora bị mất hẳn ("Á" cho きゃっ/ひゃっ/やっ, "chu" cho ちゅむっ/ちゅばっ).
- Giữ 102 dòng rên/SFX (romaji đúng "Hyan!!" 901, "Í!!"/"Uo!?", "Chụt" cho họ ちゅ, "liếm" cho れるっ/れろっ ngắn, "Phù" đứng riêng cho ふっ ngắn, SFX độc thoại onomatopoeia Việt, gasp Ư của audit/sweep không đụng).
- Sweep: 7 mục đã kiểm chứng — 6 bản sửa gasp Ư của audit (907, 908, 934, 935, 954, 1639) không đụng dòng nào; 1 already-rendered (994) giữ nguyên. File không có dòng "Kh" nào.
- Cờ cho đợt thống nhất: 1013 うれしっ→"Sướng" (lỗi nghĩa, TW 高興); SFX độc thoại （ ） chưa áp công thức đếm nguyên âm (1652/1655/1656/1658/1671/1673/1676 kéo bằng t); 1683 (dòng chưa chắc chắn của audit); 946/1069 くぅん kéo dài của くん sau tên "Soutetsu"; 924 むぷっ→"Ưm" giữ (âm m đã bao hàm ぷ).
- Lượt soát 2: tổng 37 / tái kiểm chứng 37 / bỏ 0 / sửa 0. JSON 37 mục, khóa string, jp/tw/old_vn khớp CSV3 37/37. Khối TOML parse bằng tomllib: 37 khóa, 0 sai lệch giá trị.
- 7 key trùng audit (890, 899, 900, 904, 919, 937, 982) chỉ khác giá trị audit ở đúng token rên; dùng fix moan thay cho giá trị audit khi gộp.
- Chi tiết đầy đủ: `moan-paulette-h3-yuuwaku-ice-coffee-REVIEW.md`; danh sách sửa: `moan-paulette-h3-yuuwaku-ice-coffee-wrong.json`.

**Tổng cộng sau file này: 10 file / 252 dòng sai (moan)** (cơ sở 9 file / 215 dòng + 37 file này) [parent REBASE 21/11 ~11:15 — snippet ghi cơ sở cũ 8/205 vì lr h2 đã gộp trước]
