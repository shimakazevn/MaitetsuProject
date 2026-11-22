# Audit: lr_稀咲h1_おしおきとごほうび.txt.toml — 60/297 (20,2%)

- File: `06_Kisaki/lr_稀咲h1_おしおきとごほうび.txt.toml` (route 06_Kisaki, 297 dòng script; monologue 113, 稀咲 103, 双鉄 81). Nội dung: Kisaki trừng phạt Soutetsu vì say rượu kể bí mật vợ chồng cho Paulette; phần lớn file là H-scene (Kisaki chủ động, Soutetsu bị trói tay).
- TOML md5 439e80f22d9abfcda5843f8d2f2844ca, không có bản trùng; CSV3 1 bộ 297 dòng, key khớp tuyệt đối, VN khớp TOML 297/297, 0 dòng VN trống. [selections] rỗng; 0 tag %l.
- Phân loại (60): gasp 20 (sweep 14 + mới 6), nguyên âm 16 (đếm bằng máy theo công thức 1 + số う/ぅ), đại từ 13 (Soutetsu→Kisaki "em"→"cô" 5 + trích lời Paulette 1 + Kisaki tự xưng "tôi"→"em" 7 theo ngữ cảnh 19:45), sai nghĩa 5 (1010 ああ→"Aa", 1133, 1166 いく→"ra", 1211 causative đảo ngược, 1390 にとにと→"cười tủm tỉm"), SFX 5 (1035 あぐっ, 1038 んぎっ, 1094 うふふっ→"Ufufu", 1690 くちゅっ→"Kuchu", 1720 ぃ×13 bị mất), chính tả 1 (1287 "tốt rồ"→"tốt rồi").
- Sweep gasp: 17 mục cho file này — áp nguyên văn 9; 5 mục khôi phục `\n` literal (1341/1425/1429/1551/1619, sweep dùng dạng làm phẳng); 1 mục already-rendered SAI đã sửa (1262 — っ! cuối dòng 1 bị mất); 2 mục already-rendered đúng (1065/1073); quét cơ học toàn bộ dòng JP có っ tìm thêm 6 gasp (710/971/972/974/1235/1262); 1081 false positive (っていうか).
- Đại từ: Soutetsu "tôi" với Kisaki xuyên suốt, 0 dòng "Anh" sai; Kisaki gọi Soutetsu "cậu"/tên trần, 0 dòng "anh Soutetsu"; キミ→"cậu" đúng cả 2 dòng. Kisaki tự xưng 18 dòng ボク/僕: 7 dòng "tôi"→"em" (rên/lên đỉnh/thú nhận mềm yếu), 11 dòng giữ "tôi" (ra lệnh/giải thích/quyết đoán).
- Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Thẻ %l: 0 lệch. Không còn っ thô trong VN sau fix (1020 là っ thô duy nhất).
- Lượt soát 2: 60/60 tái kiểm chứng, 0 bỏ, 1 sửa (1062 khôi phục `\n` literal). JSON 60 mục (key chuỗi); khối TOML 60 khóa parse OK, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 60/60; mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa.
- Chi tiết đầy đủ: `audit-lr-kisakih1-oshioki-gohobi-REVIEW.md`; danh sách sửa: `audit-lr-kisakih1-oshioki-gohobi-wrong.json` (60 mục).
- Cờ cho Hieu: (1) 1183 "Tôi"→"Em" là phán đoán biên, độ tin cậy thấp nhất — rà lại; (2) 1690 audit chọn "Kuchu" (theo 1688) thay "Chụt" — vòng moan xác nhận; (3) 1126 おちんぽっ và ペニス đều "Dương vật" — có cần từ thô riêng cho おちんぽ không? (4) fa/fu "Phùa" vs "Fua" chưa chốt → đợt thống nhất (file này dùng "Fua" nhất quán); (5) SFX độc thoại dài (1703–1709, 1720) → vòng moan; (6) B19 vẫn park.
- Ghi chú dữ liệu: JP trong CSV3 hỏng ký tự ở 1560 (���直 — TOML sạch 正直, VN dịch đúng, không tính sai); 1425 có 」 thừa đã bỏ trong fix.

**Tổng cộng sau file này: 213 file / 9.785 dòng sai** (cơ sở 212 file / 9.725 dòng sai + 60 file này)
