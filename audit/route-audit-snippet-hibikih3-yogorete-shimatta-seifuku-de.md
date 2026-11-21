# Audit snippet — 日々姫h3_汚れてしまった制服で.txt.toml (route 02_Hibiki)

- File: `日々姫h3_汚れてしまった制服で.txt.toml` — route 02_Hibiki, 322 dòng script, đọc toàn bộ 322/322 dòng đối chiếu JP + TW từ CSV3.
- **Sai 36 dòng (11,2%)** — rên 32, thở gấp 3 (2 từ sweep), SFX 1. Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa.
- Lỗi chính: các dòng rên H-scene — romaji họ ひゃ/や bị viết thành 'A'/'Hyaa' sai số nguyên âm hoặc mất phụ âm (y, h, f, ky, n): ひゃっ→'Hyaa' thừa a (1009/1013/1036), ひゃああんっ→'Hyaaaan' thừa 2 a (1033), ひゃっんっ→'Hyaa' mất ん (1034), ひあっ→'Hyaa' thay vì 'Hia' (1027/1041/1121), やっ/やあっ→'A' mất y (1007/1010/1023/1030/1041/1044/1046/1048/1070/1021), ふやっ→'Hyaa' sai hẳn phụ âm (1042), ふあ(っ)→'phù' thay vì 'phùa' (1016/1041/1042/1053/1071/1077/1084/1100/1121), んひゅっ/んきゅううっ/んひゃううううっ trộn 2 kiểu diễn 'ưm hyu' (1030/1076/1016/1121), 3 dòng rên dài bị viết gọn thành 'Ưm a' (1123/1125) hoặc thiếu 1 u (1124), きゅっ→'ưm' mất ky (1109), あんっ→'A' mất ん (1096); gasp 1262/1264 áp nguyên văn sweep ('Ư!'/'Ư!?'); SFX 1107 ううむ→'Ừm'.
- Sweep gasp: 3/3 mục đã kiểm tra trực tiếp — 2 nhận nguyên văn (1262, 1264), 1855 không sửa (dòng không lệch, VN diễn đúng cả hai tiếng khịt mũi).
- Đại từ: không sửa dòng nào — Soutetsu 'anh' với Hibiki đúng toàn file (Hibiki gọi 'anh hai'). Thuật ngữ: không có lỗi (Terre Verte đúng; không có 御一夜/帝鉄/湯医 trong file). Thẻ %l: 0 lệch. [character_subs] 1557/1712 trỏ key không có trong script (dư thừa vô hại, cùng mẫu Kisaki 1961).
- CỜ CHO HIEU: (1) 1073/1112 — あっ/ぁっ cuối dòng không dấu câu, VN chỉ còn 'a' trần (tiếng cụt っ có thể coi là mất; dạng 'aƯ' chưa từng xuất hiện — để vòng moan-fix phán lại); (2) 1050 ぬ――→'Ư' (mất n đầu, 'Nư' không tự nhiên); (3) 1082 う――っ――→'ư――' (っ không diễn riêng); (4) B19 vẫn park.
- Chi tiết đầy đủ: `audit-hibikih3-yogorete-shimatta-seifuku-de-REVIEW.md`; danh sách sửa: `audit-hibikih3-yogorete-shimatta-seifuku-de-wrong.json` (36 mục).

**Tổng cộng sau file này: 202 file / 9.246 dòng sai** (cơ sở 201 file / 9.210 dòng sai + 36 file này)
