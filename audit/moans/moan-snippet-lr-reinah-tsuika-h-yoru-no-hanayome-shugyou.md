# Moan-fix snippet — lr_れいな追加h_夜の花嫁修業.txt.toml (moan-lr-reinah-tsuika-h-yoru-no-hanayome-shugyou)

- File: `lrれいな追加h_夜の花嫁修業.txt.toml` — route 04_Reina, 365 dòng script, audit trước đó 33 sai.
- TOML md5: `b6d6a52b2213d8bc98351a0f14d5ae91` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 365 dòng, 0 key trùng; VN khớp TOML 365/365 sau chuẩn hoá `\n`/khoảng trắng.
- Đã đọc 365/365 dòng; xét 161 dòng rên/SFX; sửa 47, giữ 114.
- Đổi 47 dòng: romaji 42 + mất âm 5.
- Romaji họ fa/fu → Fa/Fua/Pua/Fuya/Fuo/Fukyun (32 dòng): 724 ぷあ→Pua + ふ、あ→Fu, a; 736/1061/1067/1068/1069/1071/1073/1074/1081/1294/1474 ふぁ/ふあ→Fua; 1064 ふお→Fuo; 1065 ふや→Fuya + やぁ→Yaa; 1075 ふあ…ん (7 a) →FuaaaaaaanƯƯƯ; 1076 (4 a) →Fuaaaa; 1077 (6 a) →FuaaaaaanƯƯƯƯ; 1078 (9 a) →Fuaaaaaaaaa; 1080 ふや… (6 a) →Fuyaaaaaa; 1102/1162/1177/1188 ぷあ→Pua/Puaa; 1156 ふきゅん→Fukyun; 1170 ふひゅんんんん→Fuhyunnnn; dạng tách ふ、/ふ――→Fu (724, 1073, 1202, 1211, 1283).
- Romaji họ hya/hyu/hia (11 dòng): 1049 ひゅあ…→Hyuaaaa; 1051/1090/1104 ひゃう→Hyau; 1087 ひあ→Hia + ふあ→Fua ×2; 1092 ひゅあ→Hyua (+Ư audit); 1133 ひゅあ… (18 a) →Hyua…an; 1164/1172 んひゅん→Nhyun; 1168 んひゅ→Nhyu (VN cũ "hyun" thừa 1 n) + ふ、ぁ→Fu, a; 1166 んゆ→Nyu; 1178 �んゆう→Nyuu.
- Mất âm (5): 723 っふ→phù ("ưm" mất f); 1116 ふくっ→Fuku; 1118 うあっ→Ua; 1123 く、→Ku; 1221 んくっ→Ư hự (thống nhất trong file với 1169/1173/1120).
- Lật/xây trên audit (6 key): 1060 audit "ư aƯ"→"Kua" (tiền lệ h6 806); 723/1075/1077/1092/1133 giữ giá trị audit (gasp Ư / số nguyên âm) chỉ đổi token rên.
- Giữ 114 dòng rên/SFX: hơi ngắn ふっ/ぷっ→"phù", cười audit "Ufufu~"/"Nfufu~" (1056/1059/1185/1186/1251), 10 dòng sweep-gasp + fix gasp audit, đếm nguyên âm audit đã đúng (1063 8u, 1157 6u, 1189 18u, 1117 3a), くっ→"Hự"/"Ư hự", SFX （ ） dạng nghĩa Việt, ふわあっ→"Oa", nói ngọng (không phải rên).
- Sweep: 10 mục đã kiểm chứng — 0 trùng key moan. Không dòng "Kh" nào bị đổi.
- Lượt soát 2: tổng 47 / tái kiểm chứng 47 / bỏ 0 / sửa 0. JSON 47 mục, khóa string, jp/tw/old_vn khớp CSV3 47/47. Khối TOML parse bằng tomllib: 47 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-reinah-tsuika-h-yoru-no-hanayome-shugyou-REVIEW.md`; danh sách sửa: `moan-lr-reinah-tsuika-h-yoru-no-hanayome-shugyou-wrong.json`.

**Tổng cộng sau file này: 32 file / 735 dòng sai (moan)** (cơ sở 31 file / 688 dòng + 47 file này)
- FLAG (đợt thống nhất): F1 — くっ/くあっ "Hự" vs "Ku"/"Kua" vs "Ư"; F2 — ふきゅん "Fukyun" vs "Hukyun" (h7 750); F3 — ひあ "Hia" vs "Hya" (共通13) vs "Hí a"; F4 — SFX （ ） chưa áp công thức đếm (1832/1833/1854/1861/1878/1881/1893/1894/1900/1925); F5 — 1048 やぁあ→"Đừng"; F6 — 1189 geminate ひっきゅ ("Hi kyu" vs "Hikkyu"); F7 — 1177 っ sau ~~~~ (audit đã quyết: đã diễn); F8 — 1064 "Fuo" + 1170 "Fuhyunnnn" lần đầu trong dự án; F9 — fa/fu audit đã cờ cho thống nhất, moan chuyển romaji theo quy tắc duyệt 21/11; F10 — 1060/1092 chồng audit.
