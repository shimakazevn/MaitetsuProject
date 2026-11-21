# Moan-fix snippet — ポーレットh6_あなたとふたりの学園エッチ.txt.toml (moan-paulette-h6-gakuen-ecchi)

- File: `ポーレットh6_あなたとふたりの学園エッチ.txt.toml` — route 03_Paulette, 304 dòng script, audit trước đó 36 sai.
- TOML md5: `1a184880b82bce1ce58a67cbb3a5f923` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 304 dòng, 0 key trùng; VN khớp TOML 304/304 sau chuẩn hoá `\n`/khoảng trắng.
- Đã đọc 304/304 dòng; xét 193 dòng rên/SFX (44 dòng SFX trong ngoặc); sửa 35, giữ 158.
- Đổi 35 dòng: romaji 28 + đếm nguyên âm 5 + sai âm 2.
- Romaji họ fa/fu → Fa/Fua/Pa/Pua (12): 775 ふぁっ→"Fa", 777 ぷあっ→"Pua" + ふあっっ→"Fua", 788 ふぁ→"Fa", 807/815/833/850 ふあっ→"Fua", 838 ふぁ→"Fa" + ぷぁぁ→"Puaa", 853/859 ぷあっ→"Pua", 854 ふあっ→"Fua" + ぷあっ→"Pua", 944 ふぁんっ→"Fan". Không còn dòng fa/fu nào diễn "phù" mất âm a trong file (trừ fa tách giữ "phù, a" — xem cờ F4).
- Romaji mất phụ âm mora (15): 762 ひゃんっ→"Hyan", 764/766 や→"Ya", 767 あんっ→"An", 769 きゃふっ→"Kyafu", 770 ひゃふっ→"Hyafu", 772 くっ→"Ku", 796 きゃっ→"Kya", 801 くぅ→"Kuu", 805 やふっ→"Yafu" + んきゅんっ→"Nkyun", 806 くあっ→"Kua", 836 んきゅっ→"Nkyu", 868 んきゅっっ→"Nkyu", 1348 かはっ→"Kaha", 792 うぁっ→"Wa".
- Đếm nguyên âm (5): 778 んううっ→"ưm ư ư", 789 ぁあっ→"Aa" (+ gỡ dấu 」 thừa), 840/842/870 んうっ→"ưm ư"; gộp mảnh rời: 854 あああっ→"Aaa", 1561 ああ→"Aa"; 775/788 はぁ→"hàà"/"Hàà", 916 ふぅっ→"Phùu", 836 ふ(16 u)→"F"+16u (VN cũ 11 u).
- Sai âm (2): 916 しょっ→"Sho" ("hự" sai phụ âm), 1600 ぐっ→"hự" ("ưm" mất hẳn âm g).
- 4 fix audit bị HỦY (giữ VN cũ, KHÔNG đưa vào JSON): 768 ("Kíuuuuuuuuun" → giữ "Kyuuuuuuuuun"), 800/818 ("Ư a" → giữ "Kua"), 869 ("Ưm" → giữ "Nkyun!"). 5 fix xây trên giá trị audit (770, 815, 840, 850, 868 — chỉ đổi đúng token rên). 2 fix lật giá trị audit (806, 944). 27 dòng mới so với audit.
- Giữ 158 dòng rên/SFX: gasp Ư khóa (771, 774, 814, 816, 817, 819, 1271, 1290, 1377), hơi ngắn ふっ/ぷっ→"phù", fa tách "phù, a"/"phù——a" (786, 790), họ ちゅ→"chụt", nói ngọng (784, 835, 858), SFX độc thoại （ ） dạng nghĩa Việt, んくっ→"ưm" (859), 871 "Ưm ư ư".
- Sweep: 11 mục đã kiểm chứng — 10 fix gasp Ư không đụng, 1 already-rendered (833) chỉ đổi token fa. Không dòng "Kh" nào bị đổi (file không có token "Kh" độc lập).
- Lượt soát 2: tổng 35 / tái kiểm chứng 35 / bỏ 0 / sửa 0. JSON 35 mục, khóa string, jp/tw/old_vn khớp CSV3 35/35. Khối TOML parse bằng tomllib: 35 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-paulette-h6-gakuen-ecchi-REVIEW.md`; danh sách sửa: `moan-paulette-h6-gakuen-ecchi-wrong.json`.

**Tổng cộng sau file này: 30 file / 681 dòng sai (moan)** (cơ sở 29 file / 646 dòng + 35 file này)
- FLAG (đợt thống nhất): F1 — HỦY 4 fix audit (768, 800, 818, 869 — giữ VN cũ, xem REVIEW §4); F2 — んきゅ "Nkyu" vs audit "Ưm"; F3 — くっ "Ku" (772) vs "Hự" (851) vs doc "Ư"; F4 — fa tách "phù, a" (786, 790) vs h9 "Fu, a"; F5 — họ ちゅう "chụt" vs h3 "chụụụt"; F6 — SFX độc thoại （ ） chưa áp công thức đếm (1541, 1543, 1552/1558/1560, 1597); F7 — んうっ→"ưm ư" (TW 1 âm 嗯 vs 2 âm 嗯啊); F8 — 916 "Sho", 1348 "Kaha" (phán đoán mới); F9 — 789 gỡ dấu 」 thừa; F10 — 793 "Uây!" giữ.
