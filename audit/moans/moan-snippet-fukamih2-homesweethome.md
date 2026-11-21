# Moan-fix snippet — ふかみh2_homesweethome.txt.toml (moan-fukamih2-homesweethome)

- File: `ふかみh2_homesweethome.txt.toml` — route 07_Nagi_Fukami, 301 dòng script, TOML md5 `5dee3edcf2470621aa4f3b78c9c0a43b` (khớp md5 audit), không có bản trùng.
- CSV3: 2 bộ, bộ tốt là thư mục `11_Other` (flat-match 301/301; bộ `07_Nagi_Fukami` stale, chỉ khớp 12/301); TOML vs CSV3 khớp 301/301.
- Đọc 301/301 dòng, xét 112 dòng rên/SFX (67 thoại + 45 độc thoại/SFX), sửa 19 dòng (13 romaji + 4 âm sai/mất phụ âm + 2 đếm nguyên âm), giữ 93 dòng.
- Romaji họ fa/fu (6 dòng): 973 Fua, 981 Fua, 982 Pua, 1025 Fa/Fa/Fan, 1034 Fahi/Fan, 1043 Pua — thay thế ghi chú đợt thống nhất "→ phà/phùa" (quyết 21/11 ~01:55) bằng romaji theo fallback Hieu duyệt 21/11 ~01:56.
- Romaji họ ひゃ/ひゅ/ひあ (2 dòng): 975 Hia (cho ひあっ "Hi ah"), 988 hihyu (ひひゅっ bị dịch sai thành "ưm").
- Romaji khác (5 dòng): 983 Paa/Yaa, 990 Ku (く→"Ư" sai âm), 993 Kyun (khôi phục ん cuối), 999 Kyu/Fu (khôi phục きゅ/ふ bị mất), 1032 Puha (ぷはっ mất は).
- Âm sai/mất phụ âm (4 dòng): 1003 ưm mu (んむっ mất む), 1004 Ưm gu (ぐ→"mu" sai), 1013 ha (はっ mất h), 1022 Ha ư (はうっ mất h).
- Đếm nguyên âm (2 dòng): 1011 "A…… aa…… aa~—— aaa~~!" (1+2+2+3=8a), 1555 "Aan~" (あーん = 2a+n).
- Không đụng fix audit nào (0 key trùng audit — gasp Ư 995/996/1007/1024/1172/1442/1520/1566/1591/1735, đếm 1044/1767, SFX 1562, は 1776 giữ nguyên); không dòng "Kh" nào bị đổi (989/997/1017/1731/1739 giữ); không đụng thẻ %l đã bỏ (1050/1073/1096×2).
- Lượt soát 2: 19/19 re-verified, 0 bị loại, 0 được sửa.
- Cờ cho đợt thống nhất: F1 fa/fu 6 dòng đã sửa romaji (cập nhật mục thống nhất); F2 あっ "A"/"Ah"/"Á"/"a" không nhất quán; F3 んぐっ "Ưm gu" vs paulette-h7 "Ngu"; F4 んうっ "ưm" (1003) vs "ưm ư" (1033); F5 SFX （ ） chưa áp công thức đếm (1740, 1768, 1726, 1741); F6 970 って→"mất" (nghi bịa ý, cần kiểm tra nghĩa); F7 1026 "A!?" giữ; F8 1744 số lượng p.
- Chi tiết đầy đủ: `moan-fukamih2-homesweethome-REVIEW.md`; danh sách sửa: `moan-fukamih2-homesweethome-wrong.json`.

**Tổng cộng sau file này: 40 file / 981 dòng sai (moan)** (cơ sở 39 file / 962 dòng + 19 file này — cơ sở đã kiểm chứng trực tiếp dòng tổng cuối của ROUTE-MOANS.md)
