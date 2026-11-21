# Moan snippet — ポーレットh2_制服変更？.txt.toml

- File: ポーレットh2_制服変更？.txt.toml (03_Paulette, 292 dòng, audit 47 sai đã merge).
- Đọc toàn bộ 292/292 dòng; 99 dòng rên/SFX theo mẫu quét.
- Đổi 33 dòng rên: 8 romaji họ fa/fu + ひゃ/きゃ (932, 942, 944, 956, 991, 992, 1003, 1008); 5 "Á"/từ cho やっ/やあ (927, 935, 946, 980, 1025); 7 trộn "Ưm + romaji" trong một âm (938, 1019, 1021, 1022, 1023, 1025, 1026); 9 đếm nguyên âm (923, 929, 932, 946, 957, 962, 963, 992, 1008); 4 mất phụ âm mora (928, 931, 937, 967); 4 khác (950, 972, 1006, 1660).
- Lỗi nặng nhất: rên ん + phụ âm bị tách "Ưm hyu"/"Ưm yu" (7 dòng, kể cả 1023 sai phụ âm ky→hy); họ fa/fu bị Việt hoá mất âm ("phù" cho ふあ, "phá" cho ふぁ); "Á" cho やっ/きゃっ mất phụ âm y/k.
- Gasp Ư của sweep/audit (952, 985, 1004, 1135, 950-cuối) không đụng; không dòng "Kh" khóa nào bị đổi (1003 "Khà"→"Kua": "Kh" đó là cách diễn sai của くあ).
- Cờ: 963 ĐÃ SỬA (parent): JP 10u (không phải 11u như agent đếm), VN cũ romaji 11u thừa 1u → fix romaji 10u "Afuuuuuuuuuun!!!", không áp fix audit; 5 dòng gasp Ư (952, 985, 1004, 1135, 950-cuối) đã có fix trong audit — áp ở đợt thống nhất, TOML-2 giữ VN cũ là đúng mô hình amendment; 960 nói ngọng để audit.
- Lượt soát 2: 33/33 tái kiểm chứng, 0 bỏ, 1 sửa (32 của agent + 1 parent bổ sung 963; 929 bổ sung んううっ→"Nuu" bị sót lượt 1).
- JSON 33 mục dạng chuẩn, khóa string, jp/tw/old_vn khớp CSV3 33/33; khối TOML 33 khóa parse đúng, 0 sai lệch. Parent SỬA 950: giá trị fix xây trên giá trị audit (giữ "anh Soutetsu" + "Ư!" cuối của audit, chỉ đổi "Hya un"→"Hyaun").

**Tổng cộng sau file này: 25 file / 561 dòng sai (moan)** (cơ sở 24 file / 528 dòng + 33 file này) [REBASE — cơ sở lúc giao là 23/526, Hibiki h6 (2 dòng) đã gộp 21/11 ~15:05]
