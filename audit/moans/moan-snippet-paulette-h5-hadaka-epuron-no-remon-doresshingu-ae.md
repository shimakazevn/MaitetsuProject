# Moan-fix snippet — ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml (moan-paulette-h5-hadaka-epuron-no-remon-doresshingu-ae)

- CSV3: 1 bộ duy nhất, 305 dòng, 0 key trùng; VN khớp TOML 305/305 sau chuẩn hoá `\n`/khoảng trắng.
- Đã đọc 305/305 dòng; xét 202 dòng rên/SFX (33 dòng SFX trong ngoặc); sửa 36, giữ 166.
- Đổi 36 dòng: romaji 27 + đếm nguyên âm 6 + romaji/đếm nguyên âm 3.
- Romaji họ fa/fu → Fa/Fua/Pua (15 dòng, 17 token): 848 ふあっ→"Fua", 854 ふあっ→"Fua", 855 ふあっ→"Fua", 864 ふぁ→"Fa", 873 ふあっ→"Fua", 883 ふあっ→"Fua", 884 ふぁ→"Fa", 886 ふあっ→"Fua" ×2, 888 ぷあっ→"Pua", 890 ふぁ→"Fa", 893 ぷあっ→"Pua", 895 ふあっ→"Fa", 906 ふあっ→"Fua" ×2, 920 ふぁ→"Fa", 958 ふあっ→"Fua". Không còn dòng fa/fu nào diễn "phù" mất âm a trong file (trừ fa tách "phù, a" — xem cờ F4 h6).
- Romaji mất phụ âm mora (16 dòng): 848/880/913 やっ→"Ya", 854 やっ→"Ya" + くっ→"Ku", 856 や→"Ya" + きゅっ→"Kyu", 860 きゃっ→"Kya", 862 やあっ→"Yaa" + ああっ→"Aa", 870/883/886/940 くっ→"Ku", 921 やぁ→"Yaa", 927 や→"Ya", 949 くぅんっ→"Kuun" (+ giữ "Nkyu"), 980 ひゅいっ→"Hyui" (sửa chính tả audit "Huyi"), 1733 くっ→"Ku".
- Đếm nguyên âm (6): 846/870 んんっ→"ưm ưm", 849 んううっ→"ưm ư ư", 891 ふぁ dài 22 a→17 a (9+8, っ giữa diễn "——"), 915 ふぅんっ→"Phùù ưm", 938 んーむっ→"Ưm ưm", 1015 んうぅっ→"ưm ư ư".
- Romaji khác (3): 892 きゅううう→"Kyuuuuuuuuu" (lật audit "Siết"), 924 えろぉっ→"Eroo", 942 ちゅむっ→"chumu" (tiền lệ h3).
- 2 fix audit bị HỦY (giữ VN cũ, KHÔNG đưa vào JSON): 932 ("Kua!"), 947 ("Nkyun!!!!"). 4 fix audit bị lật/kế thừa có chỉnh trong JSON: 892, 942, 949, 980.
- Giữ 166 dòng rên/SFX: gasp Ư khóa, fa tách "phù, a", họ ちゅ→"chụt", SFX độc thoại （ ） dạng động từ Việt, ひ/ひっ→"hí", くっ grunt→"hự" (1003), 1735 p-count 14 = 14 mora đã kiểm chứng.
- Sweep: 5 mục đã kiểm chứng — cả 5 đã được audit sửa đúng thành Ư, không đụng. Không dòng "Kh" nào bị đổi.
- Lượt soát 2: tổng 36 / tái kiểm chứng 36 / bỏ 0 / sửa 1 (942 khôi phục token "liếm"). JSON 36 mục, khóa string, jp/tw/old_vn khớp CSV3 36/36. Khối TOML parse bằng tomllib: 36 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-paulette-h5-hadaka-epuron-no-remon-doresshingu-ae-REVIEW.md`; danh sách sửa: `moan-paulette-h5-hadaka-epuron-no-remon-doresshingu-ae-wrong.json`.

**Tổng cộng sau file này: 32 file / 724 dòng sai (moan)** (cơ sở 31 file / 688 dòng + 36 file này)
- FLAG (đợt thống nhất): F1 — HỦY 2 fix audit (932, 947 — giữ VN cũ); F2 — くっ "Ku" (rên) vs "Hự" (grunt) vs doc "Ư" (như h6 F3); F3 — ひ/ひっ "hí" giữ (không thuộc họ ひゃ); F4 — họ ちゅ dài kéo bằng t/m (942/924/938/1723/1722/1702/1704); F5 — 868 ぐっ→"mất" (nghĩa chưa rõ); F6 — 878 ちゅっ→"hôn" giữ (1399 khung "hôn"); F7 — nói lắp 909/959/1047 (không phải rên, audit loop xem); F8 — 1048 tên gọi kéo dài くぅん bị mất độ dài, 1231 escape `\"` TOML vs `"` CSV3; F9 — 891 っ giữa rên dài diễn "——"; F10 — 915 ふぅんっ→"Phùù ưm" tách 2 mảnh vs gộp romaji.
