# Unification batch U12b — §3 M14 descriptive-SFX counting + M19 re-checks

**Phạm vi:** 2 mục mới (M14, M19) / **298 dòng** trong 53 file. Chỉ sửa （ ） SFX miêu tả (số lượng kéo dài, loại chữ kéo). Không động vào token ĐỐI THOẠI ("Ku"/"Fuya"/"Ya" — đó là batch U12a chạy song song). M14: 298 dòng sửa (17 M14a + 2 M14b + 279 M14c, trong đó 9 dòng SPACED). M19: 0 dòng sửa — 3 dòng kiểm lại, giữ nguyên cả 3 (xem §4).

**Nguồn:** CSV3 good-set (87.833 dòng; đã loại 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`), `audit-*-wrong.json`, `moans/moan-*-wrong.json`, các đợt unification đã gộp (đối chiếu trùng lặp §5, F9 — 0 trùng), báo cáo điều tra F1 (`investigation-open-moan-questions-REPORT.md`, đọc các mục M14/M19 và tiền lệ). Mọi dòng trong đợt này đều có trong CSV3 — không dòng nào phải lấy JP/old_vn từ TOML-2 (riêng lr_凪h2 1803 đối chiếu thêm TOML-2 để kiểm token katakana, xem §3.3).

## 1. Phương pháp

- **Liệt kê:** script chỉ dùng để liệt kê/đếm (`_u12b_enum.py` → `_u12b_worklist.txt`, 1.501 dòng, đã đọc toàn bộ; `_u12b_enum2.py`, `_u12b_enum3.py` tinh chỉnh định nghĩa token dài: marks ≥2, hoặc cùng-nguyên-âm chạy ≥3, hoặc liquid chạy ≥3; loại chạy っ và lặp âm tiết CV). Mọi giá trị fix đều do đọc JP (+TW) rồi viết tay; JP thắng TW. Không sửa bulk bằng script.
- **Đếm bằng máy theo từng token (`_u12b_engine.py`):** đếm う/ぅ/ー, liquid-run (る/ろ), long-vowel-run trong từng token JP; đếm chữ kéo trong VN để đối chiếu. Liệt kê LOST (JP dài mà VN không có chữ kéo nào): **306 token / 298 dòng** (xem §5, F1 — khác xa ước tính ~122 của F1). SPACED (kéo bằng chữ cách nhau): 21 token / 20 dòng. DASHES (kéo bằng gạch dài): 9 dòng. DAI-WORD (kéo bằng từ "dài"): 6 dòng. HAS-RUN (VN đã có chữ kéo): 344 token / 320 dòng.
- **old_vn:** giá trị hiện tại = fix moan nếu có trong bất kỳ `moan-*-wrong.json`, nếu không thì fix audit nếu có trong bất kỳ `audit-*-wrong.json`, nếu không thì fix unification nếu có trong bất kỳ `unification-*-wrong.json` ĐÃ GỘP, nếu không thì VN của CSV3 good-set. (Chú ý hiệu chỉnh thứ tự 22/11 ~11:35 — unification-đã-gộp > moan > audit > CSV3 — xem §5, F9: đợt này không dòng nào bị ảnh hưởng, 0 trùng lặp, 0 dòng moan-layer.)
- **Lắp ráp/kiểm chứng cơ học (`_u12b_assemble.py` + `_u12b_verify.py` v3):** script chỉ ráp các cặp thay thế đã viết tay và kiểm chứng: (1) mọi `old_seg` xuất hiện đúng 1 lần trong `old_vn` lấy từ engine (298/298, 0 lỗi); (2) đếm chữ kéo bằng máy trong từng `new_seg` theo quy tắc §2 (298/298); (3) đối chiếu 298/298 cặp (file, key) với các fix unification đã gộp — 0 trùng; (4) khối TOML parse-verified 53 file / 298 key, 0 lệch (giá trị `\n` chữ trong fix được viết `\\n` trong khối; xem §7).
- **Lượt soát 2 (`_u12b_secondpass.py` + đối chiếu JP độc lập):** xem §6.

## 2. Quyết định áp dụng (coordinator quyết 22/11 ~11:30, theo ủy quyền của Hieu)

- **M14 （ ） SFX:** GIỮ hệ của từng file (romaji ở 真闇h2/ハチロクh3/日々姫h4/lr稀咲追加h; động từ VN ở các file còn lại — KHÔNG đổi hệ của file). THỐNG NHẤT CÁCH ĐẾM: **tổng số chữ kéo dài (tính cả chữ gốc) = 1 + số dấu kéo dài う/ぅ/ー trong token JP.** Romaji: tổng số nguyên âm = 1 + số う/ぅ (vd. きゅううううううっ = 7 u → "Kyuuuuuuu"). Động từ VN: tổng số chữ cái kéo = 1 + số う/ぅ (vd. ずぶ+15う → "Phập" + 14 p = 15 p tổng; きゅううううっ (4う) → "chặtttt" = 4 t tổng; きゅううっ (2う) → "lạiii" = 3 i tổng). っ cuối KHÔNG cộng thêm chữ kéo (っ diễn bằng "!" hoặc chữ chặn trong từ gốc).
- **Quy tắc đã hòa giải (khớp TẤT CẢ tiền lệ đã kiểm chứng của F1 — 日々姫h2 1797 4う→"chặtttt" đúng; 1798 3う→"chặtttt" +1; 1787 5う→"Trượtttttt" +1; 1810 9う→"raaaaaaaaaa" 10a đúng; 1818 13う→10a −3; ハチロクh3 1836 6う→"Kyuuuuuuu" 7u đúng):** (a) **chữ kéo là phụ âm cuối** (t trong "chặt"/"tuốt"/"Siết", p trong "Phập"/"nhép", m trong "Liếm", n trong "nặn"…): **tổng số lần xuất hiện của chữ đó TRONG TỪ VN = stretch size** (số marks). (b) **chữ kéo là nguyên âm cuối** (i trong "lại", a trong "ra", o trong "vào"/"sâu"/"Véo", e trong "ve"/"nhẹ", y trong "Đẩy"/"Xoáy"/"ngoáy"): **tổng = 1 + stretch size.** (c) **Stretch size = max(số marks う/ぅ/ー, số lần lặp nguyên âm dài, số lần lặp liquid る/ろ).** Kéo chữ CUỐI của token VN (cụm nhiều từ thì kéo từ cuối; với từ dạng "tuột"/"nặn" thì tổng đếm cả chữ đầu + chữ cuối).
- **Đếm chữ có phân biệt hoa/thường (quyết trong đợt này, theo ví dụ của coordinator):** đếm chữ kéo đúng như nó được viết — từ gốc viết hoa chỉ đóng góp chữ thường ở cuối của nó ("Phập" = 1 p, "Trượt" = 1 t); từ gốc viết thường đóng góp cả chữ đầu + chữ cuối ("tuột" = 2 t, "nắn" = 2 n). Đây chính là ví dụ của coordinator ("Phập + 14 p = 15 p tổng") và cách đếm của F1 ở 1787 ("Trượtttttt" +1). Các ghi chú "tuốt" trong list (a) viết theo kiểu đếm cả T đầu — những từ đó đều viết thường ở đầu ("tuố…" sau gạch nối) nên hai cách đếm trùng nhau, không dòng nào bị ảnh hưởng; chỉ 1768 là theo đúng ví dụ của coordinator (run 14). Xem §5, F4.
- **Hàng SPACED (kéo bằng chữ cách nhau, vd. "phụt t t", "Tè e e e"):** số chữ cách nhau = số marks (chữ kéo cộng thêm trên từ gốc; "Tè" 1 + 18 chữ e cách nhau = 19 tổng = 1+18).
- **KHÔNG đổi:** dòng diễn độ dài bằng từ dài "dài" (vd. ハチロクh7 1878 "liếm dài"); dòng diễn bằng gạch dài ——— (9 dòng); dòng diễn bằng lặp từ ("Vù vù", "phập" ×4, "rào" ×10…); dòng diễn bằng dấu ~~~~~ (lr_ふかみh2 1737); token れろ dài thuộc M68 (日々姫h3 1857 — chuyển cho batch M68); parenthetical văn xuôi (không phải SFX).
- **M19 じゅぶっ:** quy tắc theo file thắng quy tắc theo chuỗi (thrust→"Phập!", mouth→"Chu mút", romaji-system→"Jubu" chỉ là tie-breaker). Cả 3 dòng kiểm lại đều giữ nguyên (§4).
- **Ba chỗ số liệu của F1 được sửa trong đợt này:** (a) 1679: JP い×1 (không phải ×2 như task ghi) → "Kéé" (2 è tổng). (b) 1681: JP い×6 (không phải ×7) → "Xoèèèèèèè" (7 è tổng). (c) 1797 lr_日々姫h1: máy đếm 15ぅ → đích 16 i (F1 đếm tay 14 marks, nói lệch −1, ngụ ý đích 15 — máy đếm 15 governs; xem §5, F3). (d) 1810 đã đúng sẵn (9う → 10 a), giữ nguyên.

## 3.1. M14a — các dòng đếm sai đã liệt kê (17 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| 凪h1_ふたりっきりのデート.txt.toml | 1768 | （ずぶうううううううううううううううっ！！！） | （呲！！！） | （Phập pppppppppppppppppppp!!!） | （Phập pppppppppppppp!!!） | M14a: ずぶ+15u -> p total 15 ('Phập' 1 + run 14) |
| 凪h1_ふたりっきりのデート.txt.toml | 1794 | （ずっ――るぅぅぅぅううううううっ） | （插……） | （Trượt——tuốtttttt） | （Trượt——tuốttttttttt） | M14a: る+10 marks -> 'tuốt' total t 10 (final run 9; earlier draft had run 8 = 9 total) |
| 凪h1_ふたりっきりのデート.txt.toml | 1797 | （ずるうううううううううっ！！！） | （插！！！） | （Trượt tuốtttttttttt!!!） | （Trượt tuốtttttttt!!!） | M14a: ずる+9u -> 'tuốt' total t 9 (final run 8) |
| 凪h1_ふたりっきりのデート.txt.toml | 1808 | （きゅうううううううううんっ！！！） | （緊！！！） | （Siết chặttttttttttttt!!!） | （Siết chặttttttttt!!!） | M14a: きゅ+9u -> 'chặt' t total 9 |
| lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml | 1909 | （じゅぶうううううううううううっ！！――ごっ！） | （劇烈抽插） | （Phậpppppppppppp!! ——Cộc!） | （Phậppppppppppp!! ——Cộc!） | M14a: じゅぶ+11u -> p total 11 |
| lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml | 1966 | （ぼぢゅうううううっ！！！！――ごつ！　ごりゅっ！） | （直衝頂峰） | （Phậppppppp!!!! ——Cộc! Ngoáy!） | （Phậppppp!!!! ——Cộc! Ngoáy!） | M14a: ぼぢゅ+5u -> p total 5 |
| lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml | 1983 | （ぢゅぶうううううううううううううっ！！！！） | （長驅直入） | （Phậpppppppppppp!!!!） | （Phậppppppppppppp!!!!） | M14a: ぢゅぶ+13u -> p total 13 |
| lr_日々姫h2_デザートは食事の前に.txt.toml | 1666 | （びゅっ！　ぶりゅっ！　びゅぶっ！　ぶびゅうう！） | （咻咻、咻咻！！） | （Phụt! Bắn ra! Phụt! Phụtttt!） | （Phụt! Bắn ra! Phụt! Phụtt!） | M14a: ぶびゅ+2u token4 -> t total 2 |
| lr_日々姫h2_デザートは食事の前に.txt.toml | 1668 | （どりゅうう！　ぶりゅうっ！　びゅぶっ！　ぶりゅ！） | （咻咻！咻咻！） | （Phụttttt! Phụt! Bắn ra! Phụt!） | （Phụtt! Phụt! Bắn ra! Phụt!） | M14a: どりゅ+2u token1 -> t total 2; token2 ぶりゅ+1u 'Phụt!' already total 1, kept |
| lr_日々姫h1_鏡の中日々姫.txt.toml | 1773 | （きゅっ！　きゅきゅ！　きゅううっ！　きゅるんっ！） | （啾！　啾啾！　啾嗚嗚！　啾嚕！） | （Siết! Siết chặt! Siết lạiiii! Xoắn lại!） | （Siết! Siết chặt! Siết lạiii! Xoắn lại!） | M14a: きゅ+2u token3 -> 'lại' vowel i total 3 |
| lr_日々姫h1_鏡の中日々姫.txt.toml | 1795 | （きゅん！　きゅううううっ！　くきゅっ！　きゅっ！） | （收縮！收縮！咕啾！啾！） | （Siết! Siết chặt lạiiii! Co thắt! Siết!） | （Siết! Siết chặt lạiiiii! Co thắt! Siết!） | M14a: きゅ+4u token2 -> 'lại' vowel i total 5 |
| lr_日々姫h1_鏡の中日々姫.txt.toml | 1797 | （きゅぅぅぅぅっぅぅぅぅぅぅぅぅぅぅぅんんっ！！） | （收縮！！！！！！！！！！！！） | （Thắt chặt lạiiiiiiiiiiiiii!!） | （Thắt chặt lạiiiiiiiiiiiiiiii!!） | M14a: きゅ+15 small-u (machine) -> 'lại' vowel i total 16; F1 said target 15 (hand-counted 14 marks) — machine count 15 governs |
| lr_日々姫h1_鏡の中日々姫.txt.toml | 1818 | （ずっ――りゅっ――うううううううううううううっ） | （滋溜——嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚） | （Trượt——rút raaaaaaaaaa） | （Trượt——rút raaaaaaaaaaaaaa） | M14a: 13u token3 -> 'ra' vowel a total 14 |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 2467 | （ずりゅううううううううううっっっっ！！！！！！） | （滋溜！！！！！！） | （Trơn tuột!!!!!!） | （Trơn tuộttttttttt!!!!!!） | M14a: ずりゅ+10u -> 'tuột' total t 10 (final run 9) |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 2468 | （ずりゅうううううっっっっっっっっ！！！！） | （滋溜！！！！） | （Trơn tuộtttttttt!!!!） | （Trơn tuộtttt!!!!） | M14a: ずりゅ+5u -> 'tuột' total t 5 (final run 4) |
| 日々姫h2_洗って大丈夫なスーツ.txt.toml | 1787 | （ずるうううううっっ！！！） | （抽插） | （Trượtttttt!!!） | （Trượttttt!!!） | M14a: ずる+5u -> t total 5 |
| 日々姫h2_洗って大丈夫なスーツ.txt.toml | 1798 | （きゅんっ――きゅうううんっ） | （收縮壓迫） | （Co thắt——Siết chặtttt） | （Co thắt——Siết chặttt） | M14a: きゅ+3u token2 -> t total 3 |

## 3.2. M14b — loại chữ kéo: kéo nguyên âm, không kéo t (2 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr_日々姫h2_デザートは食事の前に.txt.toml | 1679 | （ぎいっ） | （嘎吱） | （Kétttt） | （Kéé） | M14b: ぎい (i x1, machine) -> vowel e total 2; was stretching t |
| lr_日々姫h2_デザートは食事の前に.txt.toml | 1681 | （ちいいいいいいっ） | （拉開） | （Xoètttttt） | （Xoèèèèèèè） | M14b: ちいx6 (machine, task said x7) -> vowel e total 7; was stretching t |

## 3.3. M14c — thêm chữ kéo cho các dòng bị mất độ dài (270 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr_ふかみh2_セックスの意味.txt.toml | 1732 | （ぢゅぼぉぉぉぉぉぉぉぉぉぉぉぉ――ごりゅぅっ！！） | （咕啾咕啾，啾嚕嚕！！） | （Nhóp nhép—— Cọ xát!!） | （Nhóp nhépppppppppppp—— Cọ xát!!） | ぢゅぼぉx12 -> 'nhép' final p total 12 |
| lr_ふかみh2_セックスの意味.txt.toml | 1739 | （ぼびゅっ！　びゅるるるっ！　ぶりゅっ！　どびゅ！） | （咻咻、咻咻！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụttt! Phụt! Phụt!） | びゅるるる (ru x3) token2 -> t total 3 |
| lr_ふかみh2_セックスの意味.txt.toml | 1756 | （じゅりゅうううううううっっっっっっっっっっ！！！） | （啾嚕嚕嚕嚕嚕嚕！！！） | （Phụt!!!!!!!） | （Phụttttttt!!!!!!!） | じゅりゅ+7u -> t total 7 |
| lr_ふかみh2_セックスの意味.txt.toml | 1761 | （ずりゅううううっっっっっっっっっっ！！！！！） | （插入！！！！！） | （Phập!!!!!!!） | （Phậpppp!!!!!!!） | ずりゅ+4u -> p total 4 |
| lr_ふかみh2_セックスの意味.txt.toml | 1772 | （きゅううううううううんっっっっっっ！！！！！） | （縮緊！！！！！） | （Co thắt!!!!!!!） | （Co thắttttttt!!!!!!!） | きゅ+8u -> 'thắt' t total 8 |
| lr_ふかみh2_セックスの意味.txt.toml | 1774 | （ぴちぃぃぃぃぃぃぃぃぃぃぃっっっっっ！！） | （縮緊！！） | （Co thắt!!!!!!!!!!） | （Co thắtttttttttt!!!!!!!!!!） | ぴちぃx11 -> 'thắt' t total 11 |
| lr_れいなh1_レディ・れいな.txt.toml | 1888 | （きゅうううっ） | （握緊） | （Siết chặt） | （Siết chặttt） | きゅ+3u -> t total 3 |
| lr_れいなh1_レディ・れいな.txt.toml | 1908 | （きゅっ！　きゅううっ！　きゅきゅっ！！） | （緊！！緊繃！緊繃繃！） | （Thắt! Siết chặt! Thắt chặt!!） | （Thắt! Siết chặtt! Thắt chặt!!） | きゅ+2u token2 -> t total 2 |
| lr_ハチロクh2_新しい服。新しい旅.txt.toml | 2166 | （じゅっ――ずりゅっ――じゅぶっ――ずりゅうううっ） | （上下舞動） | （Phập——phập——phập——phập） | （Phập——phập——phập——phậpp） | ずりゅ+3u token4 -> p total 3 |
| lr_ハチロクh2_新しい服。新しい旅.txt.toml | 2178 | （とろおおおおおおおおおっ） | （噗啾） | （Phụt） | （Phụttttttttt） | とろおx9 -> t total 9 |
| lr_ポーレットh1_家族旅行の最終日の夜.txt.toml | 1662 | （きゅううううううっっっ！！！） | （劇烈收縮！！！） | （Co thắt dữ dội!!!） | （Co thắttttt dữ dội!!!） | きゅ+6u -> 'thắt' t total 6; 'dữ dội' kept |
| lr_ポーレットh1_家族旅行の最終日の夜.txt.toml | 1676 | （ぶびゅっ！　びゅぶっ！　ぶっ！　びゅううう！！） | （噗咻！咻噗！噗！咻嚕嚕嚕！！） | （Phụt! Phụt! Phụt! Phụt!!） | （Phụt! Phụt! Phụt! Phụttt!!） | びゅ+3u token4 -> t total 3 |
| lr_ポーレットh1_家族旅行の最終日の夜.txt.toml | 1684 | （じゅぶっ――ぐうううっ――――ごちゅっ！！！） | （抽出——推入——到底！！！） | （Rút ra——đẩy vào――――lút cán!!!） | （Rút ra——đẩy vàoooo――――lút cán!!!） | ぐ+3u token2 -> 'vào' vowel o total 4 |
| lr_ポーレットh1_家族旅行の最終日の夜.txt.toml | 1694 | （ぐちゅっ――ぶっ――ごちゅっ！\\nぐくっ――じゅぶううっ――どちゅっ！！） | （插入——抽出——插入！磨蹭——抽出——插入！！） | （Đâm vào——rút ra——đâm vào!\\nCọ xát——rút ra——đâm vào!!） | （Đâm vào——rút ra——đâm vào!\\nCọ xát——rút raaa——đâm vào!!） | じゅぶ+2u line2 token2 -> 'ra' vowel a total 3 |
| lr_ポーレットh1_家族旅行の最終日の夜.txt.toml | 1699 | （じゅっ――ろろおおおおっ――ごちゅっ！\\nぷっ――ぢゅううううううっっ――ばちゅっ！） | （插入——推進——到底！抽出——推進——到底！） | （Đâm vào——đẩy tới——lút cán!\\nRút ra——đẩy tới——lút cán!） | （Đâm vào——đẩy tớiiiii——lút cán!\\nRút ra——đẩy tớiiiiiii——lút cán!） | ろろおx4 -> 'tới' i total 5; ぢゅ+6u -> 'tới' i total 7 |
| lr_ポーレットh1_家族旅行の最終日の夜.txt.toml | 1709 | （きゅ！　きゅっ！　きゅううううううううっっ） | （收緊！收緊！劇烈收縮！） | （Siết! Siết! Siết chặt!） | （Siết! Siết! Siết chặtttttttt!） | きゅ+8u token3 -> t total 8 |
| lr_ポーレットh1_家族旅行の最終日の夜.txt.toml | 1728 | （ぎゅうううううっ） | （緊緊抱住） | （Ôm chặt） | （Ôm chặttttt） | ぎゅ+5u -> t total 5 |
| lr_ポーレットh1_家族旅行の最終日の夜.txt.toml | 1729 | （きゅっ――くきゅうううっっっんっ！！） | （緊縮——劇烈收縮！！） | （Siết chặt——co thắt kịch liệt!!） | （Siết chặt——co thắtt kịch liệt!!） | くきゅ+3u token2 -> 'thắt' t total 3 |
| lr_ポーレットh2_デコレーション＆ミルク.txt.toml | 1178 | 「達したいだけ、達すればいい――\\n（はぷっ！　ちゅううううううううううううううっ！）」 | 「想高潮的話就儘管高潮吧——（含住！用力吸吮——！）」 | 「Muốn lên đỉnh bao nhiêu, thì cứ lên đỉnh bấy nhiêu——\\n（Ngậm lấy! Mút mát mãnh liệt!）」 | 「Muốn lên đỉnh bao nhiêu, thì cứ lên đỉnh bấy nhiêu——\\n（Ngậm lấy! Mút mátttttttttttttt mãnh liệt!）」 | ちゅ+14u -> 'mát' t total 14 |
| lr_ポーレットh2_デコレーション＆ミルク.txt.toml | 1707 | （きゅうううっ――きゅむっ――にゅううっ――きゅん） | （劇烈收縮——縮緊——擠壓——抽搐） | （Co thắt dữ dội——siết chặt——ép chặt——co rút） | （Co thắtt dữ dội——siết chặt——ép chặtt——co rút） | きゅ+3u -> t total 3; にゅ+2u -> 'chặt' t total 2 |
| lr_ポーレットh2_デコレーション＆ミルク.txt.toml | 1708 | （きゅううううううううううううっっっっっ！！！） | （劇烈收縮！！！） | （Co thắt dữ dội!!!） | （Co thắttttttttttt dữ dội!!!） | きゅ+12u -> 'thắt' t total 12 |
| lr_ポーレットh2_デコレーション＆ミルク.txt.toml | 1718 | （びゅるっ！　びゅっ！　びゅううっ！　びゅっ！！） | （咻嚕！咻！咻唔唔！咻！！） | （Phụt! Phụt! Phụt! Phụt!!） | （Phụt! Phụt! Phụtt! Phụt!!） | びゅ+2u token3 -> t total 2 |
| lr_ポーレットh2_デコレーション＆ミルク.txt.toml | 1721 | （ぴゅっ！　ぴゅうっ――じゅわっ――ぴゅううっっ） | （咻！咻唔——咻哇——咻嚕嚕） | （Phụt! Phụt——tí tách——phụt） | （Phụt! Phụt——tí tách——phụtt） | ぴゅ+2u token4 -> t total 2 |
| lr_ポーレットh2_デコレーション＆ミルク.txt.toml | 1725 | （びゅっっ！　ぶびゅっ！　びゅるっ！　びゅううっ！） | （咻！噗咻！咻嚕！咻嚕嚕！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụt! Phụt! Phụtt!） | びゅ+2u token4 -> t total 2 |
| lr_ポーレットh2_デコレーション＆ミルク.txt.toml | 1757 | （ずりゅううっ！！！） | （擠壓！！！） | （Siết chặt!!!） | （Siết chặtt!!!） | ずりゅ+2u -> t total 2 |
| lr_ポーレットh2_デコレーション＆ミルク.txt.toml | 1775 | （きゅううっ） | （貼緊） | （Siết chặt） | （Siết chặtt） | きゅ+2u -> t total 2 |
| lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1778 | （びゅっ！　びゅううっ！　びゅぶっ！　びゅるっ！） | （咻！咻！咻！咻！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụtt! Phụt! Phụt!） | びゅ+2u token2 -> t total 2 |
| lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1784 | （じゅぶうううううううううううううっ！　ごちゅっ！） | （啾！啾！） | （Phập! Phập!） | （Phậppppppppppppp! Phập!） | じゅぶ+13u token1 -> p total 13 |
| lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1786 | （きゅうううううっ！！！　ちゅん！） | （啾！！！啾！） | （Siết!!! Chụt!） | （Siếttttt!!! Chụt!） | きゅ+5u token1 -> 'Siết' t total 5 |
| lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1800 | （もみゅっ！　ぶぢゅううううつっっっ！　ごちゅっ！） | （揉！按！捏！） | （Nắn! Bóp! Phập!） | （Nắn! Bópppp! Phập!） | ぶぢゅ+4u token2 -> 'Bóp' p total 4 |
| lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1801 | （くにっ！　もみゅ！　もみっ！　きゅううっ！） | （揉！按！搓！擦！） | （Nắn! Xoa! Vò! Siết!） | （Nắn! Xoa! Vò! Siếtt!） | きゅ+2u token4 -> t total 2 |
| lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1816 | （くにいいいいいいいっ！！） | （撐！！） | （Banh ra!!） | （Banh raaaaaaaa!!） | くにいx7 -> 'ra' vowel a total 8 |
| lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1819 | （ぐいいいいっ！！　くりゅ！　しにゅっ！　むちゅっ） | （撫！擦！點！轉！） | （Đẩy mạnh!! Vê! Ép! Chụt） | （Đẩyyyyy mạnh!! Vê! Ép! Chụt） | ぐいx4 token1 -> 'Đẩy' final y total 5 (judgement: stretch sound-word, not 'mạnh') |
| lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1834 | （きゅううううっ！！！！！） | （箍！！！！！） | （Siết!!!!!） | （Siếtttt!!!!!） | きゅ+4u -> t total 4 |
| lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1835 | （きゅううううっっ！！！） | （箍！！！） | （Siết!!!） | （Siếtttt!!!） | きゅ+4u -> t total 4 |
| lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1836 | （きゅうううううんっっつ！） | （箍！） | （Siết!） | （Siếttttt!） | きゅ+5u -> t total 5 |
| lr_凪h2_虎さんの交尾.txt.toml | 1803 | （ぞりゅう――ジュルウウッ――プッ――ちゅううっ） | （吸溜，啾，啾） | （Liếm——mút——phụt——chụt） | （Liếm——mútt——phụt——chụtt） | ちゅ+2u token4 -> t total 2; ジュル+2u token2 -> 'mút' t total 2 (katakana token verified genuine in TOML-2, not mojibake — corrected in second pass) |
| lr_凪h2_虎さんの交尾.txt.toml | 1804 | （にゅぶうううっ――れるっ――れろおお――くりゅ） | （吸溜，啾，啾，啾） | （Nhóp nhép——liếm——liếm——ngoáy） | （Nhóp nhéppp——liếm——liếm——ngoáy） | にゅぶ+3u token1 -> 'nhép' p total 3; token3 れろお (2 o) 'liếm' left for M68 scope note |
| lr_凪h2_虎さんの交尾.txt.toml | 1808 | （はむっ！　ちゅうううっ！　ちゅるっ！　れるっ！） | （咬！吻！吸！舔！） | （Ngoạm! Chụt! Mút! Liếm!） | （Ngoạm! Chụttt! Mút! Liếm!） | ちゅ+3u token2 -> t total 3 |
| lr_凪h2_虎さんの交尾.txt.toml | 1809 | （びゅっ――ぶびゅっ――びゅっ――びゅううっ……） | （咻……咻……咻……咻……） | （Phụt——phụt——phụt——phụt……） | （Phụt——phụt——phụt——phụtt……） | びゅ+2u token4 -> t total 2 |
| lr_凪h2_虎さんの交尾.txt.toml | 1815 | （じゅるううううううううううううっ！　ごちゅっ！） | （啾！啾！） | （Phập! Phập!） | （Phậpppppppppppp! Phập!） | じゅる+12u token1 -> p total 12 |
| lr_凪h2_虎さんの交尾.txt.toml | 1816 | （じゅぶうううっ！！！！） | （啾！！！！） | （Phập!!!!） | （Phậppp!!!!） | じゅぶ+3u -> p total 3 |
| lr_凪h2_虎さんの交尾.txt.toml | 1825 | （ずるううっ！　じゅぶっ！　ずりゅっ！　ばちゅっ！） | （拉！插！拉！插！） | （Trượt! Phập! Trượt! Phập!） | （Trượtt! Phập! Trượt! Phập!） | ずる+2u token1 -> t total 2 |
| lr_凪h2_虎さんの交尾.txt.toml | 1831 | （じゅぶううっっっっっっっっ！！――ごりゅんっ！！） | （插！！轉！！） | （Phập!!——Ngoáy!!） | （Phậpp!!——Ngoáy!!） | じゅぶ+2u token1 -> p total 2 |
| lr_凪h2_虎さんの交尾.txt.toml | 1833 | （じゅぶううううううううううっ！！！！　ごりゅっ！） | （插！！！！按！） | （Phập!!!! Phập!） | （Phậpppppppppp!!!! Phập!） | じゅぶ+10u token1 -> p total 10 |
| lr_凪h2_虎さんの交尾.txt.toml | 1834 | （ずぶううううううううっ！！！！！！！） | （插！！！！！） | （Phập!!!!!!!） | （Phậpppppppp!!!!!!!） | ずぶ+8u -> p total 8 |
| lr_凪h2_虎さんの交尾.txt.toml | 1844 | （きゅゅううううううううっっっっっっっっっ！！！） | （緊！！！） | （Siết!!!） | （Siếtttttttt!!!） | きゅ+8u -> t total 8 |
| lr_凪h2_虎さんの交尾.txt.toml | 1848 | （れるううっっっ！　くりゅんっ！！！！！！） | （舔！轉！！！） | （Liếm! Ngoáy!!!!!!） | （Liếmm! Ngoáy!!!!!!） | れる+2u token1 -> 'Liếm' m total 2 |
| lr_凪ふかみh1_じぇいけい！.txt.toml | 2297 | （ずぼっおおお！） | （吐出！） | （Phụt!） | （Phụttt!） | ずぼおx3 -> t total 3 |
| lr_凪ふかみh1_じぇいけい！.txt.toml | 2305 | （きゅうううううっ！！！） | （夾緊！！！） | （Siết!!!） | （Siếttttt!!!） | きゅ+5u -> t total 5 |
| lr_凪ふかみh1_じぇいけい！.txt.toml | 2314 | （ずううううううっ――じゅぶうううう！　ごちゅっ！） | （抽……插！捅！） | （Trượt——Phập! Phập!） | （Trượtttttt——Phậpppp! Phập!） | ず+6u -> 'Trượt' t total 6; じゅぶ+4u -> p total 4 |
| lr_凪ふかみh1_じぇいけい！.txt.toml | 2323 | （ずぼぉぉぉぉぉぉぉぉぉぉぉっ！　ごっ！　りゅっ！） | （插！轉！頂！） | （Phập! Phập! Phập!） | （Phậppppppppppp! Phập! Phập!） | ずぼおx11 token1 -> p total 11 |
| lr_凪ふかみh1_じぇいけい！.txt.toml | 2325 | （ずぶうううううううううううっ！！！　ごちゅっ！） | （插！！插！） | （Phập!!! Phập!） | （Phậppppppppppp!!! Phập!） | ずぶ+11u token1 -> p total 11 |
| lr_凪ふかみh1_じぇいけい！.txt.toml | 2326 | （ずぶうううううううううううううっっっっ！！） | （插！！） | （Phập!!!!） | （Phậppppppppppppp!!!!） | ずぶ+13u -> p total 13 |
| lr_凪ふかみh1_じぇいけい！.txt.toml | 2327 | （じゅるううううううううううっっっっっっつ！！） | （插！） | （Phập!!） | （Phậpppppppppp!!） | じゅる+10u -> p total 10 |
| lr_凪ふかみh1_じぇいけい！.txt.toml | 2340 | （きゅうううううううううううっっっっ！！！） | （緊！！！） | （Siết!!!） | （Siếttttttttttt!!!） | きゅ+11u -> t total 11 |
| lr_凪ふかみh1_じぇいけい！.txt.toml | 2341 | （きゅうううううんっ！！！） | （緊！！） | （Siết!!!） | （Siếttttt!!!） | きゅ+5u -> t total 5 |
| lr_凪ふかみh1_じぇいけい！.txt.toml | 2349 | （ぐちゅっ――ずぶううううううううっ！　ごちゅっ！） | （頂，插！捅！） | （Nhóp nhép——Phập! Phập!） | （Nhóp nhép——Phậpppppppp! Phập!） | ずぶ+8u token2 -> p total 8 |
| lr_日々姫h2_デザートは食事の前に.txt.toml | 1659 | （きゅんっ！　きゅううっ！　にゅるっ！　にゅむっ） | （咕啾、咕啾） | （Siết! Siết chặt! Trượt! Nhóp nhép） | （Siết! Siết chặtt! Trượt! Nhóp nhép） | きゅ+2u token2 -> t total 2 |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 2425 | （ぶぢゅうううううううううっっっっ！　ごちゅっ！！） | （噗啾！！！！！！　咕啾！！） | （Phập!!!!!!!! Cộc!!） | （Phậppppppppp!!!!!!!! Cộc!!） | ぶぢゅ+9u token1 -> p total 9 |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 2434 | （ぎゅむっ！　ぐいいいいいっ！！！！） | （套弄！套弄！！！！） | （Bóp chặt! Tuốt mạnh!!!!） | （Bóp chặt! Tuốttttt mạnh!!!!） | ぐいx5 token2 -> 'Tuốt' lowercase t total 5 (capital T does not count; run is 5 lowercase t) |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 2457 | （ずぶうううううううううっっっっ――ぶ　ちゅん！！） | （滋噗——噗啾！！） | （Phập――――bạch!!） | （Phậppppppppp――――bạch!!） | ずぶ+9u token1 -> p total 9 |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 2458 | （ずぶううっ！　ごちゅっ！　ずりゅっ！　ばちゅっ！） | （滋噗！咕溜！滋溜！啪啾！） | （Phập! Cộc! Trơn tuột! Bạch!） | （Phậpp! Cộc! Trơn tuột! Bạch!） | ずぶ+2u token1 -> p total 2 |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 2459 | （ずぶうううううううううっっっっっっ！　ごちゅっ！） | （滋噗！！！！　咕啾！） | （Phập! Cộc!） | （Phậppppppppp! Cộc!） | ずぶ+9u token1 -> p total 9 |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 2473 | （ぎゅうううううううううううっっ！　ごちゅっ！！！） | （用力！！！抽插！！！） | （Phập! Cộc!!!） | （Phậppppppppppp! Cộc!!!） | ぎゅ+11u token1 -> p total 11 |
| lr_日々姫真闇h1_三人家族.txt.toml | 2368 | （ぶううっ！　びゅるっ！　びゅぶっ！　ぶぢゅっ！！） | （噗咕咕！咻嚕！咻噗！噗咻！！） | （Pẹt! Phụt! Phụt! Phụt!!） | （Pẹtt! Phụt! Phụt! Phụt!!） | ぶ+2u token1 -> 'Pẹt' t total 2 |
| lr_日々姫真闇h1_三人家族.txt.toml | 2432 | （ずぶううううううっっ！　――ぷつっ！　ずりゅっっ） | （漸漸擠入！——頂破！滑入） | （Phập! ――Bụp! Trơn tuột） | （Phậpppppp! ――Bụp! Trơn tuột） | ずぶ+6u token1 -> p total 6 |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 1612 | （ずにゅうううううううっっっっっっっ！！！） | 「揉——————————！！！」 | （Nhào nặn!!!） | （Nhào nặnnnnnn!!!） | ずにゅ+7u -> 'nặn' total n 7 (initial n + final run 6) |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 1613 | （みゅにゅうううっっっっ！　べちゅっ！！） | 「揉—————！　舔舔！！） | （Nhào nặn! Chụt!!） | （Nhào nặnn! Chụt!!） | みゅにゅ+3u token1 -> 'nặn' total n 3 (final run 2) |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 2107 | （きゅううううううっ！！！！） | （劇烈收縮！！！） | （Siết chặt!!!!） | （Siết chặtttttt!!!!） | きゅ+6u -> t total 6 |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 2133 | （びゅううっ！　ぶっ！　びゅるっ！　びゅぶっ） | （噗咻！　噗！　咻嚕！　咻噗） | （Phụt! Phụt! Phụt! Phụt） | （Phụtt! Phụt! Phụt! Phụt） | びゅ+2u token1 -> t total 2 |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 2137 | （ずにゅうううっ！！！！） | （噗滋————！！！！） | （Nhào nặn!!!!） | （Nhào nặnn!!!!） | ずにゅ+3u -> 'nặn' total n 3 (final run 2) |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 2143 | （びゅう！　んびゅ――びゅううっ…………ぴるっ） | （噗！　嗯噗——噗嗚…………噗） | （Phụt! Phụt——phụt…………phụt） | （Phụt! Phụt——phụtt…………phụt） | びゅ+2u token3 -> t total 2 |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 2165 | （むぎゅうううううううううううっっっっ！） | （擠壓————————————！） | （Ép chặt!） | （Ép chặttttttttttt!） | むぎゅ+11u -> t total 11 |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 2166 | （にゅっ！　ぶううううううううううっ！　べちゅっ！） | （擠壓！　揉——————！！　噗滋！） | （Trơn tuột! Chụt! Chụt!） | （Trơn tuột! Chụtttttttttt! Chụt!） | ぶ+10u token2 -> t total 10 |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 2167 | （むきゅううううううううううっっっっっ） | （擠壓！！！） | （Ép chặt!!!!!） | （Ép chặtttttttttt!!!!!） | むきゅ+10u -> t total 10 |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 2170 | （むにいいいいっ！　もみゅううううううっ！） | （柔軟————！！　揉揉————————！） | （Nhào nặn! Xoa bóp!） | （Nhào nặnnn! Xoa bópppppp!） | むにいx4 token1 -> 'nặn' total n 4 (final run 3); もみゅ+6u token2 -> 'bóp' p total 6 |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 2175 | （ずっ――ごちゅんっ！　きゅうううっ！　きゅりゅ！） | （滋——抽插！　緊繃！！　啾！） | （Phập——rầm! Siết chặt! Xoay!） | （Phập——rầm! Siết chặttt! Xoay!） | きゅ+3u token3 -> t total 3 |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 2186 | （きゅむっ！　きゅううんっ！） | （緊繃！　緊繃！） | （Siết chặt! Siết chặt!） | （Siết chặt! Siết chặtt!） | きゅ+2u token2 -> t total 2 |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 2187 | （きゅううっ） | （緊繃） | （Siết chặt） | （Siết chặtt） | きゅ+2u -> t total 2 |
| lr_稀咲h1_おしおきとごほうび.txt.toml | 1710 | （つーーーーっ） | （戳） | （Chọc――） | （Chọcccc――） | つーx4 -> 'Chọc' final c total 4; dashes kept |
| lr_稀咲h1_おしおきとごほうび.txt.toml | 1712 | （ぎゅうううううううっ！！！！！） | （掐住！！！！！） | （Véo mạnh!!!!!） | （Véoooooooo mạnh!!!!!） | ぎゅ+7u -> 'Véo' o total 8 |
| lr_稀咲h1_おしおきとごほうび.txt.toml | 1713 | （ぎゅううううううううううっ！！！！） | （掐住！！！！） | （Véo mạnh!!!!） | （Véooooooooooo mạnh!!!!） | ぎゅ+10u -> 'Véo' o total 11 |
| lr_稀咲h1_おしおきとごほうび.txt.toml | 1715 | （ぎううううううううううううううっ） | （掐住） | （Véo mạnh） | （Véooooooooooooooo mạnh） | ぎ+14u -> 'Véo' o total 15 |
| lr_稀咲h1_おしおきとごほうび.txt.toml | 1717 | （ぎゅうううううううっっっ！！） | （掐緊！！） | （Véo mạnh!!） | （Véoooooooo mạnh!!） | ぎゅ+7u -> 'Véo' o total 8 |
| lr_稀咲h1_おしおきとごほうび.txt.toml | 1718 | （ぎうううううううううっ！！！！！！） | （掐！！！！！！） | （Véo mạnh!!!!!!） | （Véoooooooooo mạnh!!!!!!） | ぎ+9u -> 'Véo' o total 10 |
| lr_稀咲h1_おしおきとごほうび.txt.toml | 1719 | （ぎうううううぅぅぅぅぅぅぅっっっっっっっ！！！！） | （掐！！！！） | （Véo mạnh!!!!） | （Véooooooooooooo mạnh!!!!） | ぎ marks=12 -> 'Véo' o total 13 |
| lr_稀咲h1_おしおきとごほうび.txt.toml | 1727 | （ぎゅうううううううっ！！！！！） | （用力掐住！！！！！） | （Véo mạnh!!!!!） | （Véoooooooo mạnh!!!!!） | ぎゅ+7u -> 'Véo' o total 8 |
| lr_稀咲h1_おしおきとごほうび.txt.toml | 1728 | （ぎううううううううううっっっ！　ぎにっ！！） | （用力猛掐！！） | （Véo mạnh! Xoắn!!） | （Véooooooooooo mạnh! Xoắn!!） | ぎ+10u token1 -> 'Véo' o total 11 |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 2505 | （ずりゅっ―ぐいいいっ―こしゅんっ―じゅぶぅ） | （呲溜——刺入——抽插——撲哧） | （Trượt——đâm sâu——cọ xát——ju bu） | （Trượt——đâm sâuuuu——cọ xát——ju bu） | ぐいx3 token2 -> 'sâu' vowel u total 4; 'ju bu' romaji kept |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 2567 | （さわっ―さすっ―つうううっ……さすっ） | （摩擦——撫摸——摸摸摸——摩擦） | （Chạm——miết——vuốt……miết） | （Chạm——miết——vuốttt……miết） | つ+3u token3 -> 'vuốt' t total 3 |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 2590 | （きゅううううっ） | （收縮） | （Siết chặt） | （Siết chặtttt） | きゅ+4u -> t total 4 |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 2607 | （きゅうううううっっ！！） | （用力吮吸！！） | （Mút mạnh!!） | （Múttttt mạnh!!） | きゅ+5u -> 'Mút' t total 5; 'mạnh' (TW 用力) kept — stretch the verb only |
| lr真闇追加h_赤ちゃん、欲しか.txt.toml | 1813 | （ずりゅっ！　ばちゅっ！　ぐいっ！　ぐりゅうう！） | （反覆抽插） | （Trượt! Phập! Thọc! Xoáy!） | （Trượt! Phập! Thọc! Xoáyyy!） | ぐりゅ+2u token4 -> 'Xoáy' y total 3 |
| lr真闇追加h_赤ちゃん、欲しか.txt.toml | 1826 | （びゅううう！　どびゅっ！　ぶびゅっ　びゅるるっ！） | （噴湧而出） | （Phụt! Phụt! Phụt! Phụt!） | （Phụttt! Phụt! Phụt! Phụt!） | びゅ+3u token1 -> t total 3 |
| lr真闇追加h_赤ちゃん、欲しか.txt.toml | 1827 | （むにゅうううっ！！） | （大力揉搓！！） | （Nhào nặn!!） | （Nhào nặnn!!） | むにゅ+3u -> 'nặn' total n 3 (final run 2) |
| lr真闇追加h_赤ちゃん、欲しか.txt.toml | 1877 | （れろっ――ちゅっ――ちゅうっ――れるうううっっ） | （舔來舔去） | （Liếm——chụt——chùn chụt——liếm liếm） | （Liếm——chụt——chùn chụt——liếm liếmmm） | れる+3u token4 -> last 'liếm' m total 3 |
| lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml | 1418 | （ぐちゅううっ！！！！！） | 「呼——嗯——哈——啊……呼啊——（咽口水）你不是也一樣，還有功夫顧著我嗎」 | （Nhóp nhép!!!!!） | （Nhóp nhépp!!!!!） | ぐちゅ+2u -> 'nhép' p total 2 (old_vn is audit value) |
| lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml | 1589 | （ずじゅううううっっ！！！！） | 「奧莉薇女士。性快感最終會到達怎樣的一個巔峰，還請你拭目以待」 | （Phập!!!!!!!!） | （Phậpppp!!!!!!!!） | ずじゅ+4u -> p total 4 |
| ふかみh1_ともはり練習.txt.toml | 1651 | （じゅるっ――じゅううっ！　じゅぶうっ！　ごくっ！） | （啾……啾！啾！噗！） | （Rột——chụt! Nhóp nhép! Ực!） | （Rột——chụtt! Nhóp nhép! Ực!） | じゅ+2u token2 -> t total 2 |
| ふかみh1_ともはり練習.txt.toml | 1656 | （きゅううううっ！） | （啾！） | （Co thắt!） | （Co thắttt!） | きゅ+4u -> t total 4 |
| ふかみh1_ともはり練習.txt.toml | 1664 | （きゅうううううううっ！！！） | （抖！！！） | （Co thắt!!!!!!!!） | （Co thắtttttt!!!!!!!!） | きゅ+7u -> t total 7 |
| ふかみh1_ともはり練習.txt.toml | 1673 | （ぐいいいっ！！！） | （插！！！） | （Đâm sâu!!!） | （Đâm sâuuuu!!!） | ぐいx3 -> 'sâu' vowel u total 4 |
| ふかみh1_ともはり練習.txt.toml | 1675 | （ざっぼーーーーーーーーんっ！！！） | （撲通！！！） | （Tõm——!!!） | （Tõmmmmmmmm——!!!） | ざっぼーx8 -> 'Tõm' m total 8; dashes kept |
| ふかみh2_homesweethome.txt.toml | 1736 | （ぐいいいっ！） | （按！） | （Ấn mạnh!） | （Ấnnn mạnh!） | ぐいx3 -> 'Ấn' total n 3 |
| ふかみh2_homesweethome.txt.toml | 1768 | （きゅううううううううううっっ） | （緊） | （Siết chặt） | （Siết chặtttttttttt） | きゅ+10u -> t total 10 |
| ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3881 | （びゅうううっ！　びゅる！　びゅぶっ！　びゅうっ！） | （咻！咻！咻！咻！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụttt! Phụt! Phụt! Phụt!） | びゅ+3u token1 -> t total 3 |
| ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3892 | （ずりゅうううううううっ！） | （抽！） | （Rút ra!） | （Rút raaaaaaaa!） | ずりゅ+7u -> 'ra' vowel a total 8 |
| ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3896 | （ぐりっ――ぐりゅんっ！　ぐ――ぐううっ） | （插……插！插，插） | （Ngoáy—— ngoáy! Ngoáy—— ngoáy） | （Ngoáy—— ngoáy! Ngoáy—— ngoáyyy） | ぐ+2u token3 -> 'ngoáy' y total 3 |
| ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3898 | （ずぶううううううううっ！　ごつんっ！！！） | （插！插！！） | （Phập! Cộc!!!） | （Phậpppppppp! Cộc!!!） | ずぶ+8u token1 -> p total 8 |
| ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3899 | （ずるうううっ！　ばちゅっ！　ずうっ！　ごつっ！） | （插！擦！插！擦！） | （Rút ra! Bạch! Phập! Cộc!） | （Rút raaaa! Bạch! Phập! Cộc!） | ずる+3u token1 -> 'ra' vowel a total 4 |
| ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3900 | （ずりゅうううううううっ！！！！） | （插！！！！） | （Rút ra!!!!） | （Rút raaaaaaaa!!!!） | ずりゅ+7u -> 'ra' vowel a total 8 |
| ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3902 | （ぐううううううっ！） | （插！） | （Nhấn sâu!） | （Nhấn sâuuuuuuu!） | ぐ+6u -> 'sâu' vowel u total 7 |
| ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3921 | （きゅううううううっ） | （緊） | （Siết chặt） | （Siết chặtttttt） | きゅ+6u -> t total 6 |
| れいなh1_おかあさんのレッスン.txt.toml | 2324 | （みちいいいいいいいいいいいっ！！） | （咕啾！！） | （Phập phập phập phập!!） | （Phập phập phập phậpppppppppp!!） | みちいx11 -> final 'phập' p total 11 (repetition + stretch) |
| れいなh2_おもらし防止大作戦.txt.toml | 1744 | （んびゅっ！　びゅううっ！　どびゅっ！　びゅぶる！） | （咻咻！咻咻！！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụtt! Phụt! Phụt!） | びゅ+2u token2 -> t total 2 |
| れいなh3_おもらし自由化大作戦.txt.toml | 1730 | （びゅっ！　びゅるっ！　びゅううっ！　どびゅ！） | （咻咻！咻咻！咻咻！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụt! Phụtt! Phụt!） | びゅ+2u token3 -> t total 2 |
| れいなh4_ふたりっきりのハロウィン.txt.toml | 3268 | （ちゅぷううっ） | （啾） | （Chụt） | （Chụtt） | ちゅぷ+2u -> t total 2 |
| れいなh4_ふたりっきりのハロウィン.txt.toml | 3273 | （ずぶううううううううううううっ！　ごっ！！） | （插入！！） | （Phập! Rầm!!） | （Phậpppppppppppp! Rầm!!） | ずぶ+12u token1 -> p total 12 |
| れいなh4_ふたりっきりのハロウィン.txt.toml | 3279 | （くぱあああっ） | （撐開） | （Tách ra） | （Tách raaaa） | くぱあx3 -> 'ra' vowel a total 4 |
| れいなh4_ふたりっきりのハロウィン.txt.toml | 3289 | （きゅううううううんっ！！！） | （縮緊！！！） | （Siết chặt!!!） | （Siết chặtttttt!!!） | きゅ+6u -> t total 6 |
| ハチロクh1_契り.txt.toml | 2140 | （ちぃぃぃぃっ） | （唰啦） | （Xoạt） | （Xoạtttt） | ちぃx4 -> 'Xoạt' t total 4 |
| ハチロクh1_契り.txt.toml | 2177 | （ずっ――ぬっ――ずぶううううっ！――プツっ） | （緩緩插入——戳破） | （Phập——phập——phập phập phập!——Bục） | （Phập——phập——phập phập phậppp!——Bục） | ずぶ+4u token3 -> final 'phập' p total 4 (repetition + stretch) |
| ハチロクh1_契り.txt.toml | 2184 | （ずるううううううっ！） | （長驅直入） | （Phập phập phập!） | （Phập phập phậppppp!） | ずる+6u -> final 'phập' p total 6 (repetition + stretch) |
| ハチロクh2_お勉強の成果.txt.toml | 1738 | （びゅっ！　びゅるっ！　びゅぶっ！　びゅううっ！！） | （嗖！嗖！嗖！嗖嗚！！） | （Phụt! Phụt! Phụt! Phụt!!） | （Phụt! Phụt! Phụt! Phụtt!!） | びゅ+2u token4 -> t total 2 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1651 | （ギュウううううっ！） | （吱唔——！） | （Siết chặt!） | （Siết chặtttt!） | ギュウ+4u -> t total 4 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1653 | （きゅん、きゅううっ） | （吱，吱嗚） | （Siết, siết chặt） | （Siết, siết chặtt） | きゅ+2u token2 -> t total 2 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1662 | （ずぶううううううううううっっ！！！） | （呲噗——！！！） | （Phập!!!） | （Phậpppppppppp!!!） | ずぶ+10u -> p total 10 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1666 | （ずるるるるるるるるっ） | （呲嚕——） | （Trượt trượt trượt trượt trượt） | （Trượt trượt trượt trượt trượttttttt） | ずるx8 -> final 'trượt' t total 8 (repetition + stretch) |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1669 | （ずろおおおおおおっ！） | （呲溜——！） | （Trượt!!!） | （Trượtttttt!!!） | ずろおx6 -> t total 6 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1674 | （ぐいいいっ！） | （咕吱！） | （Nhấc bổng!） | （Nhấc bổnggg!） | ぐいx3 -> 'bổng' final g total 3 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1685 | （ぬろおおおおおおおおっ！！） | （哧溜——！！） | （Trượt ra!!!） | （Trượt raaaaaaaaa!!!） | ぬろおx8 -> 'ra' vowel a total 9 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1691 | （きゅんっ！　きゅうううっっ！！） | （啾！啾——！！） | （Siết! Siết chặt!!） | （Siết! Siết chặttt!!） | きゅ+3u token2 -> t total 3 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1697 | （びゅっ！　びゅるっ！　どびゅっ！　びゅううっ！） | （噗！噗！咕噗！噗嚕！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụt! Phụt! Phụtt!） | びゅ+2u token4 -> t total 2 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1699 | （びゅるっ！　びゅっ！　びゅうううっ！　びゅううっ） | （噗！噗！噗嚕！噗嚕） | （Phụt! Phụt! Phụt! Phụt） | （Phụt! Phụt! Phụttt! Phụtt） | びゅ+3u token3 -> t total 3; びゅ+2u token4 -> t total 2 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1705 | （にゅるっ――きゅううっ――ざわわっ） | （扭——吱嗚——沙瓦） | （Trượt——siết chặt——râm ran） | （Trượt——siết chặtt——râm ran） | きゅ+2u token2 -> t total 2 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1713 | （きゅうううううううんっ！） | （插——！） | （Siết chặt!） | （Siết chặttttttt!） | きゅ+7u -> t total 7 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1714 | （きゅううううううううっ！！） | （插入！！） | （Thít chặt!!） | （Thít chặtttttttt!!） | きゅ+8u -> t total 8 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1716 | （さすううううっ） | （撫摸） | （Vuốt ve） | （Vuốt veeeee） | さす+4u -> 've' vowel e total 5 |
| ハチロクh5_おだいどこしごと.txt.toml | 1691 | （くちゅううううっっ） | （咕啾——） | （Nhóp nhép） | （Nhóp nhépppp） | くちゅ+4u -> 'nhép' p total 4 |
| ハチロクh5_おだいどこしごと.txt.toml | 1697 | （ちょろっ――ちょっ――ちょおおおおっ） | （咻嚕——咻——啾——） | （Róc rách——róc——róc rách!） | （Róc rách——róc——róc ráchhhh!） | ちょおx4 token3 -> 'rách' final h total 4 |
| ハチロクh5_おだいどこしごと.txt.toml | 1702 | （ちょおおおおお） | （啾——） | （Róc rách） | （Róc ráchhhhh） | ちょおx5 -> 'rách' final h total 5 |
| ハチロクh5_おだいどこしごと.txt.toml | 1706 | （ちゅろっ――ちょおおおおおっ！） | （啾嚕——啾——！） | （Chụt——róc rách!） | （Chụt——róc ráchhhhh!） | ちょおx5 token2 -> 'rách' final h total 5 |
| ハチロクh5_おだいどこしごと.txt.toml | 1708 | （きゅんっ！　きゅううううううんっ！！） | （啾！吱嗚——！！） | （Thít! Siết chặt!!） | （Thít! Siết chặtttttt!!） | きゅ+6u token2 -> t total 6 |
| ハチロクh5_おだいどこしごと.txt.toml | 1712 | （んびゅっ！　ぐいっ！　びゅっ！　ずぶううっ！） | （嗯噗！咕嚕！噗！呲噗！） | （Phụt! Phập! Phụt! Phập!） | （Phụt! Phập! Phụt! Phậpp!） | ずぶ+2u token4 -> p total 2 |
| ハチロクh5_おだいどこしごと.txt.toml | 1721 | （びゅるるっ！　びゅっ！　びゅううっ！　どびゅる！） | （噗嚕！噗！噗嚕！咕噗！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụt! Phụtt! Phụt!） | びゅ+2u token3 -> t total 2 |
| ハチロクh5_おだいどこしごと.txt.toml | 1730 | （ずるううううううっ！） | （抽出） | （Rút ra!） | （Rút raaaaaaa!） | ずる+6u -> 'ra' vowel a total 7 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 1929 | （ぎゅうううっ） | （吱嗚——） | （Ôm chặt） | （Ôm chặttt） | ぎゅ+3u -> t total 3 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 1931 | （きゅうっ！　きゅきゅっ！　くううっ！　きゅぽっ！） | （吱嗚！嗯呀！咕嗚！啾啵！） | （Thít! Siết chặt! Ưm! Chụt!） | （Thít! Siết chặt! Ưmm! Chụt!） | く+2u token3 (groan in parens) -> 'Ưm' m total 2 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 1935 | （ずっ――ずうううっ――こっ！） | （呲——嗚嗚——咕！） | （Phập——phập——cộc!） | （Phập——phậpp——cộc!） | ず+3u token2 -> p total 3 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 1938 | （ずうう――りゅんっ！！！） | （呲——嚕！！！） | （Trượt——mạnh!!!） | （Trượtt——mạnh!!!） | ず+2u token1 -> t total 2 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 1944 | （ずううううううううううっっ！！！！） | （呲嗚嗚嗚嗚嗚嗚嗚嗚嗚！！！！） | （Phập!!!!） | （Phậpppppppppp!!!!） | ず+10u -> p total 10 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 1953 | （くちゅぅぅぅっ） | （咕啾） | （Nhóp nhép） | （Nhóp nhéppp） | くちゅぅx3 -> 'nhép' p total 3 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 1970 | （きゅうう、きゅきゅんっ！） | （啾——，啾啾！） | （Thít chặt, siết chặt!） | （Thít chặtt, siết chặt!） | きゅ+2u token1 -> t total 2 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 1984 | （きゅっ！　きゅむううううううううっ！！！） | （嗯呀！嗯嗚——！！！） | （Thít! Siết chặt!!!） | （Thít! Siết chặtttttttt!!!） | きゅむ+8u token2 -> t total 8 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 1990 | （くぷうううっ！　くぽおおおおっ！） | （噗嗚嗚！唔噗——！） | （Phập phập! Phập phập!） | （Phập phậpp! Phập phậppp!） | くぷ+3u token1 -> tail 'phập' p total 3; くぽおx4 token2 -> tail 'phập' p total 4 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 1995 | （びゅっ！　ぶびゅっ！　びゅるるっ！　びゅううっ！） | （噗！呲噗！噗嚕！噗嚕！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụt! Phụt! Phụtt!） | びゅ+2u token4 -> t total 2 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 2006 | （びゅっ！　びゅるっ！　びゅううっ！　びゅっ！） | （噗！噗！噗嚕！噗！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụt! Phụtt! Phụt!） | びゅ+2u token3 -> t total 2 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 2023 | （きゅうううううううううっっ！！） | （插入——！！） | （Thít chặt!!） | （Thít chặttttttttt!!） | きゅ+9u -> t total 9 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 2024 | （きゅううううううううううっ！） | （插入——！） | （Siết chặt!） | （Siết chặtttttttttt!） | きゅ+10u -> t total 10 |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 2036 | （みゅりいいいいいいいいいいいいっっ！！！） | （緊——！！！） | （Ép chặt!!!） | （Ép chặtttttttttttt!!!） | みゅりいx12 -> t total 12 |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 1880 | （れろっ――はむっ――ちゅうう――きゅぽっ！） | （嗯——哈姆——啾嗚——咕啵！） | （Liếm——ngoạm——chùn chụt——bật ra!） | （Liếm——ngoạm——chùn chụtt——bật ra!） | ちゅ+2u token3 -> t total 2 |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 1883 | （きゅっ！　きゅうううっ！　にゅるっ！　にゅううっ） | （嗯呀！啾——！扭！扭嗚） | （Thít! Siết chặt! Trơn tuột! Lún sâu） | （Thít! Siết chặttt! Trơn tuột! Lún sâuuu） | きゅ+3u token2 -> t total 3; にゅ+2u token4 -> 'sâu' u total 3 |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 1896 | （びゅっ！　びゅるっ！！　びゅううっ！　びゅっ！！） | （噗！噗！！噗嚕！噗！！） | （Phụt! Phụt!! Phụt! Phụt!!） | （Phụt! Phụt!! Phụtt! Phụt!!） | びゅ+2u token3 -> t total 2 |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 1903 | （きちぃぃぃぃぃ！） | （好緊！） | （Khít quá!） | （Khít quáaaaaa!） | きちぃx5 -> 'quá' vowel a total 6 |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 1928 | （むにいいいっ） | （揉搓） | （Nắn bóp） | （Nắn bóppp） | むにいx3 -> 'bóp' p total 3 |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 1929 | （きゅううううううううんっ！！！） | （插入——！！！） | （Thít chặt!!!） | （Thít chặtttttttt!!!） | きゅ+8u -> t total 8 |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 1931 | （きゅんっ！　きゅうううううっ！　きゅきゅっ！） | （插入！插入——！插入！） | （Thít! Siết chặt! Co thắt!） | （Thít! Siết chặttttt! Co thắt!） | きゅ+5u token2 -> t total 5 |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 1932 | （きゅううううううっ！！！） | （插入！！！） | （Siết chặt!!!） | （Siết chặtttttt!!!） | きゅ+6u -> t total 6 |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 1933 | （きゅうううううっ！） | （插入） | （Siết chặt!） | （Siết chặttttt!） | きゅ+5u -> t total 5 |
| ハチロクh8_桜色のひめごと.txt.toml | 1550 | （ちょ――ちょっ――ちょおおおっ！） | （哧——哧——哧！） | （Tí tách——tí tách——tuôn trào!） | （Tí tách——tí tách——tuôn tràoooo!） | ちょおx3 token3 -> 'trào' vowel o total 4 |
| ハチロクh8_桜色のひめごと.txt.toml | 1556 | （きゅん！　きゅむううっ！　むにゅん！　もみゅん！） | （啾！啾嗯——！嗯扭！揉！） | （Kyun! Siết chặt! Mềm mại! Nắn bóp!） | （Kyun! Siết chặtt! Mềm mại! Nắn bóp!） | きゅむ+2u token2 -> t total 2 |
| ハチロクh8_桜色のひめごと.txt.toml | 1577 | （びゅるっ！　どびゅっ！　びゅううっ！　びゅるっ！） | （噗！咕噗！噗嚕！噗！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụt! Phụtt! Phụt!） | びゅ+2u token3 -> t total 2 |
| ポーレットh1_ファーストセックス.txt.toml | 1722 | （ちゅうううっ！） | （吸緊） | （Mút chặt!） | （Mút chặttt!） | ちゅ+3u -> t total 3 |
| ポーレットh1_ファーストセックス.txt.toml | 1730 | （ずぶううう――すぱんっ！） | （啾嚕——啪！） | （Đâm phập——chát!） | （Đâm phậpp——chát!） | ずぶ+3u token1 -> 'phập' p total 3 |
| ポーレットh1_ファーストセックス.txt.toml | 1756 | （きゅうううううっっっ！） | （猛烈箍禁） | （Siết chặt!） | （Siết chặttttt!） | きゅ+5u -> t total 5 |
| ポーレットh1_ファーストセックス.txt.toml | 1774 | （ずるううううううううっ！！） | （長驅直入） | （Rút ra——đâm vào!!） | （Rút ra——đâm vàooooooooo!!） | ずる+8u -> 'vào' vowel o total 9 |
| ポーレットh4_クリーム＆クリーム.txt.toml | 1593 | （ぬぽおおおっ） | （塗抹） | （Bôi trơn） | （Bôi trơnnn） | ぬぽおx3 -> 'trơn' total n 3 |
| ポーレットh4_クリーム＆クリーム.txt.toml | 1600 | （くぱああああっ！） | （扒開） | （Tách ra!） | （Tách raaaaa!） | くぱあx4 -> 'ra' vowel a total 5 |
| ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml | 1699 | （ちょっ――ちょおおおおおおおっ） | （嘩啦啦） | （Róc——róc rách róc rách róc rách） | （Róc——róc rách róc rách róc ráchhhhhhh） | ちょおx7 token2 -> final 'rách' h total 7 (repetition + stretch) |
| ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml | 1725 | （ぬるっ――にゅるっ――ぬっ――ぬとおおおっ――） | （用力擠壓） | （Trơn tuột——trơn tuột——rút——nhóp nhép——） | （Trơn tuột——trơn tuột——rút——nhóp nhéppp——） | ぬとおx3 token4 -> 'nhép' p total 3 |
| ポーレットh6_あなたとふたりの学園エッチ.txt.toml | 1552 | （びゅっ！　びゅるるっ！　びゅっ！　どびゅううっ！） | （噗噗！噗噗！噗嚕！噗嚕！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụt! Phụt! Phụtt!） | どびゅ+2u token4 -> t total 2 |
| ポーレットh6_あなたとふたりの学園エッチ.txt.toml | 1566 | （きゅううううううっっ！！！） | （夾緊！！！） | （Siết chặt!!!） | （Siết chặtttttt!!!） | きゅ+6u -> t total 6 |
| ポーレットh6_あなたとふたりの学園エッチ.txt.toml | 1567 | （みちちっ！　みちっ！　きゅううっ！　きゅんっ！！） | （夾緊） | （Co bóp! Co bóp! Siết chặt! Siết chặt!!） | （Co bóp! Co bóp! Siết chặtt! Siết chặt!!） | きゅ+2u token3 -> t total 2 |
| ポーレットh6_あなたとふたりの学園エッチ.txt.toml | 1577 | （きゅううううううっ！！！） | （抵上） | （Siết chặt!!!） | （Siết chặtttttt!!!） | きゅ+6u -> t total 6 |
| ポーレットh7_残業エッチもyシャツで.txt.toml | 1649 | （ずぶっ！　ずばっ！　ずじゅっ！　じゅぶううっ！） | （啾噗！啾噗！啾啪！啾啪！） | （Phập! Phập! Chụt! Chụt!） | （Phập! Phập! Chụt! Chụtt!） | じゅぶ+2u token4 -> t total 2 |
| ポーレットh7_残業エッチもyシャツで.txt.toml | 1664 | （にちぃぃぃぃぃぃっ！） | （夾緊） | （Nhóp nhép!） | （Nhóp nhépppppp!） | にちぃx6 -> 'nhép' p total 6 |
| ポーレットh7_残業エッチもyシャツで.txt.toml | 1670 | （もみゅっ！　くにゅっ！　くりっ！　くいいいいっ！） | （按壓揉搓） | （Nắn! Bóp! Xoa! Mạnh lên!） | （Nắn! Bóp! Xoa! Mạnh lênnnn!） | くいx4 token4 -> 'lên' total n 4 |
| ポーレットh7_残業エッチもyシャツで.txt.toml | 1692 | （れるううううっ） | （舔舐） | （Liếm） | （Liếmmmm） | れる+4u -> m total 4 |
| ポーレットh7_残業エッチもyシャツで.txt.toml | 1695 | （きゅんっ！　きゅきゅううううううっっ！） | （蠕動夾緊） | （Siết! Siết chặt!!） | （Siết! Siết chặtttttt!!） | きゅきゅ+6u token2 -> t total 6 |
| ポーレットh7_残業エッチもyシャツで.txt.toml | 1696 | （じゅるるるるうううううううううううううっ！！！） | （蠕動） | （Rột rột rột!!!） | （Rột rột rộttttttttttttt!!!） | じゅるx4 + 13u -> size max(13,4)=13 -> final 'rột' t total 13 |
| ポーレットh8_気動車の国のアリス.txt.toml | 3732 | （じゅりゅううっ！　ごっ！　ずゆっ！　ごつっ！） | （啾噗！啾噗！啾啪！啾啪！） | （Rột rột! Cộp! Phập! Cộp!） | （Rột rộtt! Cộp! Phập! Cộp!） | じゅりゅ+2u token1 -> tail 'rột' t total 2 |
| ポーレットh8_気動車の国のアリス.txt.toml | 3748 | （つううううっ） | （插入） | （Trượt） | （Trượtttt） | つ+4u -> t total 4 |
| ポーレットh8_気動車の国のアリス.txt.toml | 3765 | （つうううううっ） | （輕撫） | （Vuốt ve） | （Vuốt veeeeee） | つ+5u -> 've' vowel e total 6 |
| 凪h1_ふたりっきりのデート.txt.toml | 1767 | （びゅっ！　びゅるううっ！　びゅぶっ！　びゅっ！） | （呲！呲！呲！呲！） | （Phụt! Phụt phụt! Phụt! Phụt!） | （Phụt! Phụt phụtt! Phụt! Phụt!） | びゅる+2u token2 -> tail 'phụt' t total 2 |
| 凪h1_ふたりっきりのデート.txt.toml | 1773 | （きゅんっ！　きゅううううっ！） | （啾！啾！） | （Thắt tim! Siết chặt!） | （Thắt tim! Siết chặtttt!） | きゅ+4u token2 -> t total 4 |
| 凪ふかみh1_修学旅行の夜.txt.toml | 2030 | （つうううっ） | （壓） | （Ép mạnh） | （Éppp mạnh） | つ+3u -> 'Ép' p total 3 |
| 凪ふかみh1_修学旅行の夜.txt.toml | 2038 | （ぐりいいいいいいいいいいいいいっ！） | （挺！） | （Thúc mạnh!） | （Thúccccccccccccc mạnh!） | ぐりいx13 -> 'Thúc' final c total 13 |
| 凪ふかみh1_修学旅行の夜.txt.toml | 2040 | （きゅうううっ――きゅっ――ぎゅうううっ） | （插……插……插） | （Siết chặt——siết——ép chặt） | （Siết chặttt——siết——ép chặttt） | きゅ+3u token1 -> t total 3; ぎゅ+3u token3 -> t total 3 |
| 凪ふかみh1_修学旅行の夜.txt.toml | 2056 | （きゅきゅうううっ！） | （緊！） | （Siết chặt!） | （Siết chặttt!） | きゅきゅ+3u -> t total 3 |
| 凪ふかみh1_修学旅行の夜.txt.toml | 2058 | （うにゅうっ） | （蠕動） | （Nhu động） | （Nhuuu động） | うにゅう (marks 2) -> 'Nhu' vowel u total 3 |
| 凪ふかみh2_みずあそび.txt.toml | 2155 | （ずぬうううううううううっ！） | （插！） | （Phập!） | （Phậppppppppp!） | ずぬ+9u -> p total 9 |
| 凪ふかみh2_みずあそび.txt.toml | 2160 | （うにゅうううううううううううっ！！） | （摩擦！！） | （Nhu động!!） | （Nhuuuuuuuuuuuuu động!!） | うにゅう (marks 12) -> 'Nhu' vowel u total 13 |
| 凪ふかみh2_みずあそび.txt.toml | 2170 | （にゅろおおおおん――ずぽおっ！！） | （滋溜！！） | （Trơn tuột——phập!!） | （Trơn tuộttt——phập!!） | にゅろおx4 token1 -> 'tuột' total t 4 (base 2, final run 3) |
| 凪ふかみh2_みずあそび.txt.toml | 2174 | （ぬろおおおおおおおっ！） | （硬！） | （Trơn tuột!） | （Trơn tuộtttttt!） | ぬろおx7 -> 'tuột' total t 7 (final run 6) |
| 凪ふかみh2_みずあそび.txt.toml | 2179 | （きゅううっ） | （緊） | （Siết chặt） | （Siết chặtt） | きゅ+2u -> t total 2 |
| 凪ふかみh2_みずあそび.txt.toml | 2182 | （ずろおおおおおおおおおおっ！） | （舔！） | （Trượt vào!） | （Trượt vàooooooooooo!） | ずろおx10 -> 'vào' vowel o total 11 |
| 日々姫h1_マッサージの続き.txt.toml | 1883 | （びゅううっ！　びゅるるっ！　どびゅっ！　びゅう！） | （噗噗！噗嚕！噗噗！噗噗！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụtt! Phụt! Phụt! Phụt!） | びゅ+2u token1 -> t total 2 |
| 日々姫h2_洗って大丈夫なスーツ.txt.toml | 1771 | （びゅるっ！　んびゅ！　びゅうう！　どびゅ！！） | （噗嚕！噗噗！噗噗！噗嚕！！） | （Phụt! Phụt! Phụt! Phụt!!） | （Phụt! Phụt! Phụtt! Phụt!!） | びゅ+2u token3 -> t total 2 |
| 日々姫h3_汚れてしまった制服で.txt.toml | 1794 | （じゅるるるるうぅぅぅぅぅっ！） | （吸溜） | （Chùn chụt!） | （Chùn chụtttttt!） | じゅるx4 + marks 6 -> size max(6,4)=6 -> t total 6 |
| 日々姫h3_汚れてしまった制服で.txt.toml | 1796 | （じゅるるるるるっ！） | （咕啾） | （Chùn chụt!） | （Chùn chụttttt!） | じゅるx5 -> t total 5 |
| 日々姫h3_汚れてしまった制服で.txt.toml | 1800 | （じゅぶうううううううううううっ！） | （啾噗） | （Phập!） | （Phậppppppppppp!） | じゅぶ+11u -> p total 11 |
| 日々姫h3_汚れてしまった制服で.txt.toml | 1802 | （じゅるるるるるうっっっっ！） | （啾嚕） | （Chùn chụt!） | （Chùn chụttttt!） | じゅるx5 + 1u -> size max(1,5)=5 -> t total 5 |
| 日々姫h3_汚れてしまった制服で.txt.toml | 1804 | （ずぶうううううううううううっ！） | （噗哧） | （Phập!） | （Phậppppppppppp!） | ずぶ+11u -> p total 11 |
| 日々姫h3_汚れてしまった制服で.txt.toml | 1811 | （びゅるっ――びゅううっ――びゅっ！　ぷっ！） | （噗嚕――噗嚕――噗噗！噗噗！） | （Phụt——Phụt——Phụt! Phụt!） | （Phụt——Phụtt——Phụt! Phụt!） | びゅ+2u token2 -> t total 2 |
| 日々姫h3_汚れてしまった制服で.txt.toml | 1813 | （びゅっ！　びゅるっ！　びゅううっ！　びゅっ！） | （噗嚕！噗嚕！噗噗！噗噗！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụt! Phụtt! Phụt!） | びゅ+2u token3 -> t total 2 |
| 日々姫h3_汚れてしまった制服で.txt.toml | 1814 | （どびゅっ！　びゅぶっ！　びゅるるっ！　びゅううう） | （噗嚕！噗嚕！噗噗！噗噗） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụt! Phụt! Phụttt!） | びゅ+3u token4 -> t total 3 |
| 日々姫h3_汚れてしまった制服で.txt.toml | 1832 | （ぬるうううううううううううううっっっ！） | （抽出） | （Trượt ra!） | （Trượt raaaaaaaaaaaaaa!） | ぬる+13u -> 'ra' vowel a total 14 |
| 日々姫h3_汚れてしまった制服で.txt.toml | 1844 | （きゅうううっ！！！） | （收縮壓迫） | （Thắt chặt!!!） | （Thắt chặttt!!!） | きゅ+3u -> t total 3 |
| 日々姫h3_汚れてしまった制服で.txt.toml | 1852 | （てろおおおおおおおっ） | （滴下） | （Chảy xuống） | （Chảy xuốnggggggg） | てろおx7 -> 'xuống' final g total 7 |
| 日々姫h3_汚れてしまった制服で.txt.toml | 1854 | （ずろおおおおおおおおおおおおおおっっ！！） | （用力插入） | （Phập!!!） | （Phậpppppppppppppp!!!） | ずろおx14 -> p total 14 |
| 日々姫h4_いもうとタオル.txt.toml | 1747 | （ねとおおおっ） | （咕嚕） | （Nhớt nháp） | （Nhớt nháppp） | ねとおx3 -> 'nháp' p total 3 |
| 日々姫h4_いもうとタオル.txt.toml | 1773 | （きゅううっ） | （夾住） | （Kẹp chặt） | （Kẹp chặtt） | きゅ+2u -> t total 2 |
| 日々姫h4_いもうとタオル.txt.toml | 1774 | （むにいいいっ） | （夾緊） | （Kẹp chặt） | （Kẹp chặttt） | むにいx3 -> t total 3 |
| 日々姫h4_いもうとタオル.txt.toml | 1781 | （むにいいいっ） | （揉搓） | （Bóp nhẹ） | （Bóp nhẹeee） | むにいx3 -> 'nhẹ' vowel e total 4 |
| 日々姫h4_いもうとタオル.txt.toml | 1790 | （きゅっ――きゅうううっ） | （收縮壓迫） | （Siết——Siết chặt） | （Siết——Siết chặttt） | きゅ+3u token2 -> t total 3 |
| ハチロクh8_桜色のひめごと.txt.toml | 1531 | （ぞりゅんっ！　ずろろろっ！　ごちゅっ！　ずりゅ！） | （呲溜！呲嚕！啾！呲溜！） | （Trơn tuột! Trơn tuột! Nhóp nhép! Trơn tuột!） | （Trơn tuột! Trơn tuộtt! Nhóp nhép! Trơn tuột!） | ずろろx3 token2 -> 'tuột' total t 3 (base 2, final run 2) |
| 日々姫h4_いもうとタオル.txt.toml | 1794 | （ずっっっっっ――――ごりゅううううっつ！！！） | （用力插入！！！） | （Thúc mạnh――――Nghiến chặt!!!） | （Thúc mạnh――――Nghiến chặtttt!!!） | ごりゅ+4u token2 -> 'chặt' t total 4 (old_vn is audit value) |
| 日々姫h4_いもうとタオル.txt.toml | 1796 | （とろおおおおおっ） | （精液滴下） | （Chảy xuống） | （Chảy xuốnggggg） | とろおx5 -> 'xuống' final g total 5 |
| 日々姫h5_白濁絵の具の射精会.txt.toml | 2056 | （ずぶんっ！　ずりゅっ！　ごちゅっ！　ずりゅううつ） | （啾噗！啾噗！噗啾！噗啾！） | （Phập! Phập! Thúc! Phập!） | （Phập! Phập! Thúc! Phậpp!） | ずりゅ+2u token4 -> p total 2 |
| 日々姫h5_白濁絵の具の射精会.txt.toml | 2058 | （じゅぶううううっっっ！！！！） | （啾噗！！！！） | （Phập!!!!） | （Phậpppp!!!!） | じゅぶ+4u -> p total 4 |
| 日々姫h5_白濁絵の具の射精会.txt.toml | 2062 | （ちゅむううううっ！！！） | （啾嚕！！！） | （Chùn chụt!!!） | （Chùn chụtttt!!!） | ちゅむ+4u -> t total 4 |
| 日々姫h5_白濁絵の具の射精会.txt.toml | 2091 | （ずにゅううううううっ！！） | （插入！！） | （Xuyên thấu!!） | （Xuyên thấuuuuuuu!!） | ずにゅ+6u -> 'thấu' vowel u total 7 |
| 日々姫h5_白濁絵の具の射精会.txt.toml | 2096 | （きゅん！　きゅんっ！　きゅううううううんっ！） | （收縮壓迫） | （Siết! Siết! Siết chặt!） | （Siết! Siết! Siết chặtttttt!） | きゅ+6u token3 -> t total 6 |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 3712 | （びゅっ！　びゅぶるっ！　びゅううっ！　びゅっ！） | （噗噗！噗嚕！噗噗！噗嚕！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụt! Phụtt! Phụt!） | びゅ+2u token3 -> t total 2 |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 3714 | （どびゅるっ！！！！！　びゅううううっ！） | （噗嚕！！！！！噗噗！） | （Phụt!!!!! Phụt!） | （Phụt!!!!! Phụtttt!） | びゅ+4u token2 -> t total 4 |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 3722 | （ぐうううっ） | （抱緊） | （Ôm chặt） | （Ôm chặttt） | ぐ+3u -> t total 3 |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 3723 | （ちいいい） | （拉拉鏈） | （Kéo khóa） | （Kéo khóaaaa） | ちいx3 -> 'khóa' vowel a total 4 |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 3729 | （きゅううううううんっ！） | （收縮壓迫） | （Siết chặt!） | （Siết chặtttttt!） | きゅ+6u -> t total 6 |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 3735 | （じゅにゅうううううううううっ！　ごんっ！！） | （用力抽插） | （Xuyên thấu! Thúc mạnh!!） | （Xuyên thấuuuuuuuuuu! Thúc mạnh!!） | じゅにゅ+9u token1 -> 'thấu' vowel u total 10 |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 3736 | （ずぶうううううういううううっ！　ごんっ！） | （用力插入） | （Phập! Thúc mạnh!） | （Phậpppppppppp! Thúc mạnh!） | ずぶ marks=10 token1 -> p total 10 |
| 真闇h1_長期熟成.txt.toml | 1824 | （きゅううううううううっ！！！） | （壓！！！） | （Ép chặt!!!） | （Ép chặtttttttt!!!） | きゅ+8u -> t total 8 |
| 真闇h1_長期熟成.txt.toml | 1833 | （とろおおおおおおおおおっ） | （滴下） | （Nhỏ tong tỏng） | （Nhỏ tong tỏnggggggggg） | とろおx9 -> 'tỏng' final g total 9 |
| 真闇h2_無濾過.txt.toml | 1821 | （ずぬるるるるるるっ！！！） | （吱溜！！！） | （Trượt tuột!!!） | （Trượt tuộttttt!!!） | ずぬるx6 -> 'tuột' total t 6 (final run 5); file is romaji-system but this row's existing system is VN-verb (cf. 1822 6x 'Siết') — system kept, stretch added |
| 真闇h2_無濾過.txt.toml | 1860 | （びゅっ！　びゅるっ！　びゅぶっ！　びゅううっ） | （噗！　噗嚕！　咻噗！　噗） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụt! Phụt! Phụtt!） | びゅ+2u token4 -> t total 2 |
| 真闇h2_無濾過.txt.toml | 1893 | （ぐいっ――ずるうううっ！） | （頂――吱溜！） | （Ngoáy――tuột!） | （Ngoáy――tuộtt!） | ずる+3u token2 -> 'tuột' total t 3 (final run 2) |
| 真闇h3_補習授業の廃校舎.txt.toml | 4014 | （ずりゅうううううううう――――ばぢゅんっ！！） | （呲溜――啵啾！！） | （Phập――――bạch!!） | （Phậpppppppp――――bạch!!） | ずりゅ+8u token1 -> p total 8 |
| 真闇h3_補習授業の廃校舎.txt.toml | 4016 | （つうううっ） | （呲） | （Trượt） | （Trượttt） | つ+3u -> t total 3 |
| 真闇h3_補習授業の廃校舎.txt.toml | 4042 | （きゅうううううんんっ！！） | （壓嗯！！） | （Siết chặt!!） | （Siết chặttttt!!） | きゅ+5u -> t total 5 |
| 真闇h3_補習授業の廃校舎.txt.toml | 4043 | （きゅううううううううっ！） | （壓！） | （Siết chặt!） | （Siết chặtttttttt!） | きゅ+8u -> t total 8 |
| 稀咲h1_性生活.txt.toml | 2042 | （ずぶうううううううううううっ――ごっ！！！） | （吱噗――咚！！！） | （Phập――bịch!!!） | （Phậppppppppppp――bịch!!!） | ずぶ+11u token1 -> p total 11 |
| 稀咲h1_性生活.txt.toml | 2045 | （ずるううううううううううううっ！！） | （吱溜！！） | （Phập!!） | （Phậpppppppppppp!!） | ずる+12u -> p total 12 |
| 稀咲h1_性生活.txt.toml | 2055 | （きゅうううううっ！） | （哧溜！） | （Siết chặt!） | （Siết chặttttt!） | きゅ+5u -> t total 5 |
| 稀咲h1_性生活.txt.toml | 2064 | （むちいいいいいいっ） | （噗嗤） | （Phụt） | （Phụtttttt） | むちいx6 -> t total 6 |
| 稀咲h1_性生活.txt.toml | 2067 | （びゅるっ！　びゅううっ！　びゅっ！　どびゅっ！） | （噗嚕！　噗！　噗！　咚噗！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụtt! Phụt! Phụt!） | びゅ+2u token2 -> t total 2 |
| 稀咲h1_性生活.txt.toml | 2070 | （びゅっ！　どびゅっ！　どびゅうう！　びゅるるっ！） | （噗！　咚噗！　咚噗！　噗嚕！） | （Phụt! Phụt! Phụt! Phụt!） | （Phụt! Phụt! Phụtt! Phụt!） | どびゅ+2u token3 -> t total 2 |
| 稀咲h1_性生活.txt.toml | 2072 | （びゅっ！　びゅうううっ！　びゅるっ！　びゅるんっ） | （噗！　噗！　噗嚕！　噗嚕） | （Phụt! Phụt! Phụt! Phụt） | （Phụt! Phụttt! Phụt! Phụt） | びゅ+3u token2 -> t total 3 |
| 稀咲h1_性生活.txt.toml | 2074 | （くいいいっ） | （嚓――） | （Kéo——） | （Kéoooo——） | くいx3 -> 'Kéo' vowel o total 4 |
| 稀咲h2_プライベートルーム.txt.toml | 1932 | （ずっ――ずるうううううううっ） | （吱――吱溜） | （Phập――phập） | （Phập――phậpppppp） | ずる+7u token2 -> p total 7 |
| 稀咲h2_プライベートルーム.txt.toml | 1933 | （ずぶううううっ！　ずばんっ！！！） | （吱噗！　呲啪！！！） | （Phập! Phập!!!） | （Phậpppp! Phập!!!） | ずぶ+4u token1 -> p total 4 |
| 稀咲h2_プライベートルーム.txt.toml | 1934 | （ずぶううううううううううっ！！） | （吱噗！！） | （Phập!!） | （Phậpppppppppp!!） | ずぶ+10u -> p total 10 |
| 稀咲h2_プライベートルーム.txt.toml | 1935 | （ずるうううううっっっ――） | （吱溜――） | （Phập――） | （Phậppppp――） | ずる+5u -> p total 5 |
| 稀咲h2_プライベートルーム.txt.toml | 1936 | （ずるうううううううっ！！！） | （吱溜！！！） | （Phập!!!） | （Phậppppppp!!!） | ずる+7u -> p total 7 |
| 稀咲h2_プライベートルーム.txt.toml | 1942 | （ぐううっ！　――――きゅんっ！） | （咕！　――――啾！） | （Gừ! ――――Kyun!） | （Gừừừ! ――――Kyun!） | ぐ+2u token1 -> 'Gừ' vowel ừ total 3 |
| 稀咲h2_プライベートルーム.txt.toml | 1955 | （びゅるるるるうぅぅっ！！！） | （噗嚕！！！） | （Phụt!!!） | （Phụtttt!!!） | びゅるx4 + marks 3 -> size max(3,4)=4 -> t total 4 (task's own example) |
| 稀咲h2_プライベートルーム.txt.toml | 1963 | （きゅううううっ！） | （壓！） | （Siết chặt!） | （Siết chặtttt!） | きゅ+4u -> t total 4 |
| 稀咲h3_チャイナドレスでおもてなし.txt.toml | 3751 | （にゅるううううっ） | （倏溜） | （Trơn tuột） | （Trơn tuộttt） | にゅる+4u -> 'tuột' total t 4 (final run 3) |
| 稀咲h3_チャイナドレスでおもてなし.txt.toml | 3754 | （ずぶううううううっ！！！！） | （吱噗！！！！） | （Phập!!!!） | （Phậpppppp!!!!） | ずぶ+6u -> p total 6 |
| 稀咲h3_チャイナドレスでおもてなし.txt.toml | 3757 | （きゅううううううんんっ！！！） | （吱！！！） | （Thít chặt!!!） | （Thít chặtttttt!!!） | きゅ+6u -> t total 6 |
| 稀咲h3_チャイナドレスでおもてなし.txt.toml | 3784 | （ぐいいいっ） | （唔） | （Kéo mạnh） | （Kéoooo mạnh） | ぐいx3 -> 'Kéo' vowel o total 4 |

## 3.4. M14c — hàng SPACED: sửa số chữ cách nhau (9 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr_れいなh1_レディ・れいな.txt.toml | 1860 | （ちょおおおおおおおおおおおおおおおおおおっっ） | （哧溜溜——————————） | （Tè e e e e e e e e e e e e e e e e e e e） | （Tè e e e e e e e e e e e e e e e e e e） | SPACED: ちょおx18 -> 18 spaced e (was 19; 'Tè' 1 + 18 = 19 total = 1+18) |
| lr_れいなh1_レディ・れいな.txt.toml | 1866 | （じゅぎゅうううううううううっっっ！　ごっ！！！） | （啾咕————————！咕！！！） | （Chu siết t t t t t t t t t t! Ực!!!） | （Chu siết t t t t t t t t t! Ực!!!） | SPACED: じゅぎゅ+9u -> 9 spaced t (was 10) |
| lr_れいなh1_レディ・れいな.txt.toml | 1869 | （じゅぼおおおおおおおっっっっっ――ごちゅっっ！） | （啾嗚——————————咕啾！） | （Chu mút t t t t t t t t t t t t t t t——cạch!） | （Chu mút t t t t t t t——cạch!） | SPACED: じゅぼおx7 -> 7 spaced t (was 15) |
| lr_れいなh1_レディ・れいな.txt.toml | 1913 | （こつんっ！　――きゅうううううっっっっつ！！） | （頂！——緊繃繃～～～～～！」 | （Cạch! ——Siết chặt t t t t t t!!） | （Cạch! ——Siết chặt t t t t t!!） | SPACED: きゅ+5u -> 5 spaced t (was 6) |
| ふかみh1_ともはり練習.txt.toml | 1647 | （びゅうううっ！　びゅるっ！　どびゅうううっ！！） | （呲！呲！呲！！） | （Phụt! Phụt! Phụt t t t t!!） | （Phụt t t t! Phụt! Phụt t t t!!） | SPACED: token1 びゅ+3u had no stretch -> 3 spaced t; token3 どびゅ+3u had 4 -> 3 spaced t |
| ふかみh1_ともはり練習.txt.toml | 1671 | （ずんんんっ！　ぐりいいいいいいいっ！！！） | （插！插！！！） | （Phập p p p! Ngoáy y y y y y y y y y y y!!!） | （Phập p p p! Ngoáy y y y y y y y!!!） | SPACED: ぐりいx7 -> 7 spaced y (was 11); 'Phập p p p' for ずんんん (3n) kept |
| ふかみh1_ともはり練習.txt.toml | 1674 | （ずるうううううううっ！） | （插！） | （Trượt sâu u u u u u!） | （Trượt sâu u u u u u u u!） | SPACED: ずる+7u -> 7 spaced u (was 5) |
| ふかみh1_ともはり練習.txt.toml | 1683 | （ぬろおおおおおおおっ！！！） | （舔！！！） | （Liếm m m m m m m m m!!!） | （Liếm m m m m m m m!!!） | SPACED: ぬろおx7 -> 7 spaced m (was 8) |
| ふかみh2_homesweethome.txt.toml | 1739 | （っぐっ――グイいいいいいいいいいいっ！） | （插……插！） | （Kh——Phập p p p p p p p p p!） | （Kh——Phập p p p p p p p p p p!） | SPACED: グイいx10 -> 10 spaced p (was 9) |

## 3.5. M19 — kiểm lại 3 dòng (0 dòng sửa)

lr_れいなh1 1896/1867 ("Chu mút") và lr_ハチロクh3 1935 ("Phập!" ×4) đều giữ nguyên — xem bảng §4. Lý do đầy đủ trong ghi chú từng dòng.

## 4. Đã kiểm chứng, giữ nguyên (không sửa)

| File | Key | Ghi chú |
|---|---|---|
| lr_ふかみh2_セックスの意味.txt.toml | 1737 | KEEP: length rendered by '~~~~~' (tilde convention for ～ + long token); not converted to letter stretch |
| lr_れいなh1_レディ・れいな.txt.toml | 1864 | KEEP: spaced-letter convention, 'phụt t t' = 2 spaced t for 2u (stretch letters = marks) — count correct |
| lr_れいなh1_レディ・れいな.txt.toml | 1867 | KEEP (M19 re-check): 'Chu mút' correct — same per-file uniformity as 1896 (chain has ばちゅっ/ぐりゅっ but file never uses 'Phập!' for じゅぶっ) |
| lr_れいなh1_レディ・れいな.txt.toml | 1896 | KEEP (M19 re-check): 'Chu mút' correct — file is uniformly 'Chu mút' for じゅぶっ in ALL rows incl. thrust chains (1882: ずぼっ->'Phập!' but じゅぶっ stays 'Chu mút'); per-file rule wins over chain rule |
| lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml | 1935 | KEEP (M19 re-check): 'Phập!' x4 correct — chain contains ばちゅっ x2 (thrust), so thrust rule gives 'Phập!'; F1's machine 'mouth' classification was wrong (missed ばちゅっ) |
| lr_凪h2_虎さんの交尾.txt.toml | 1836 | KEEP (corrected in verification): ずりゅ+2u token3 -> p total 2 already satisfied by base 'phập' (2 lowercase p); no change needed |
| lr_日々姫h1_鏡の中日々姫.txt.toml | 1810 | KEEP (M14a listed row, already correct): 9u -> 'ra' vowel a total 10 = 1+9 |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 2623 | KEEP: prose parenthetical (これは―あるいは―…), not SFX — flagged token is prose, no stretch applies |
| ふかみh2_homesweethome.txt.toml | 1769 | KEEP: spaced-romaji convention, 'kyu u u' = 2 spaced u for 2u (total u 3 = 1+2) — count correct |
| ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3879 | KEEP: length rendered by word repetition 'Vù vù' (2 words for びゅ+2u) |
| ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3880 | KEEP: length rendered by word repetition 'Vù vù' (2 words for ひゅ+2u) |
| ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3885 | KEEP: length rendered by word repetition, 'rào' x10 for ざぁぁあx10 |
| れいなh2_おもらし防止大作戦.txt.toml | 1760 | KEEP: length rendered by word repetition, 'Róc rách' x6 for ちょろx12 |
| ハチロクh2_お勉強の成果.txt.toml | 1717 | KEEP: length rendered by word repetition, 'phập' x4 for うx6 |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1683 | KEEP: spaced rendering 'Ư ư ư' (3 words for みりりり, 3 ru) — count matches |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 1986 | KEEP (corrected in verification): ず+2u token3 -> p total 2 already satisfied by base 'phập'; no change needed |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 2028 | KEEP: prose parenthetical, not SFX — flagged token is prose, no stretch applies |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 2038 | KEEP: prose parenthetical, not SFX — flagged token is prose, no stretch applies |
| ハチロクh8_桜色のひめごと.txt.toml | 1532 | KEEP (corrected in verification): ぞりゅ+2u -> 'tuột' total t 2 already satisfied by base word; no change needed (earlier draft wrongly added a t) |
| ハチロクh8_桜色のひめごと.txt.toml | 1539 | KEEP (corrected in verification): ぞりゅ+2u token2 -> 'tuột' total t 2 already satisfied by base word; no change needed |
| ポーレットh2_制服変更？.txt.toml | 1642 | KEEP: length rendered by word repetition, 'rào' x5 for ちょおx4 |
| ポーレットh4_クリーム＆クリーム.txt.toml | 1610 | KEEP: 'nắn' total n already 2 = marks (2u); no visible change under total-count rule |
| ポーレットh7_残業エッチもyシャツで.txt.toml | 1672 | KEEP: 'tuột' total t already 2 = marks (2u) |
| 凪ふかみh2_みずあそび.txt.toml | 2143 | KEEP: length rendered by spaced repetition 'Ồ ồ ồ' (3 words for おx3) |
| 日々姫h3_汚れてしまった制服で.txt.toml | 1847 | KEEP: prose parenthetical, not SFX — flagged token is prose, no stretch applies |
| 稀咲h1_性生活.txt.toml | 2039 | KEEP (corrected in verification): る+2u token4 -> p total 2 already satisfied by base 'phập'; no change needed |

**Giữ nguyên khác (không nằm trong bảng trên — quy ước của file, không chuyển sang kéo chữ):**
- **DASHES (9 dòng):** độ dài diễn bằng gạch dài — lr_れいなh1 1861 ("Xoạch————"), 1898, 1899; lr_真闇h1 2108, 2122 ("Trượt dài——————————"), 2136; ふかみh2 1740 ("Phập——————Bịch!!!"); ハチロクh7 1818 ("Trượt dài————phập!"), 1868 ("Mút mạnh————bật ra!!").
- **DAI-WORD (6 dòng):** độ dài diễn bằng từ "dài" — ハチロクh7 1878 ("liếm dài"), lr_日々姫h2 1692 ("Trượt dài"), 日々姫h4 1768 ("Trượt dài"), 1788 ("Trượt dài!"), 日々姫h5 2095 ("Trượt dài"), 日々姫h6 3706 ("Trượt dài!"). (ハチロクh7 1840 KHÔNG thuộc nhóm này — VN là "Rerooooo——", romaji + gạch, thuộc M68/DASHES.)
- **M68 (1 dòng, chuyển batch khác):** 日々姫h3 1857 （れろおおおおおっっ → "Liếm láp") — token れろ dài, thuộc M68 Group 1, không sửa ở đây.
- **Văn xuôi (2 dòng):** lr_ハチロクh3 1901 và lr_稀咲ポーレットh1 2623 là parenthetical văn xuôi, không phải SFX.
- **Đã đúng sẵn (2 dòng trong bảng §4):** 1532/1539/1610/1672/1836/1986/2039 — "tuột"/"nắn"/"phập" đã đủ tổng chữ = số marks, không cần thay đổi thấy được.

## 5. Cờ cho coordinator

- **(F1) Đối chiếu số lượng 306 vs ~122:** liệt kê bằng máy tìm **306 token / 298 dòng** LOST (JP dài mà VN không có chữ kéo nào), cao hơn nhiều so với ước tính ~122 của F1. Đã thử hòa giải bằng các ngưỡng khác (marks ≥3, kiểm run trên toàn VN, lọc văn xuôi) mà không tái tạo được 122 — đợt này tiến hành theo liệt kê máy và báo số thực: **292 dòng sửa được (toàn SFX) + 6 dòng hỗn hợp** (2 dòng 凪ふかみh1 2058 / 凪ふかみh2 2160 sửa phần SFX, giữ phần còn lại; 1 dòng M68; 1 dòng văn xuôi; 2 dòng prose).
- **(F2) HAS-RUN mismatch scan — ứng viên batch follow-up, KHÔNG sửa ở đây:** quét máy trên 320 dòng HAS-RUN (VN đã có chữ kéo) cờ **134 token / 126 dòng** có chênh lệch số lượng ظاهر. Quét này nhiễu (đếm dấu — ù vs u, ố vs o; lệch vị trí; cụm nhiều token) nên không sửa ngoài phạm vi task (a); đề xuất batch follow-up kiểm tay từng dòng đó.
- **(F3) Sửa số liệu F1:** 1679 い×1 (task ghi ×2); 1681 い×6 (task ghi ×7); 1797 lr_日々姫h1 máy đếm 15ぅ → đích 16 i (F1 đếm tay 14, ngụ ý đích 15); 1810 đã đúng sẵn. Ngoài ra 1794 凪h1: ghi chú gốc "final run 8" sai số học (tổng 9, không phải 10) — đã sửa thành run 9; 1797 凪h1 ghi "final run 7" → 8.
- **(F4) Quy ước đếm "Phập" (hoa/thường):** ví dụ của coordinator ("Phập + 14 p = 15") đếm "Phập" là 1 p; các ghi chú "tuốt" trong list (a) đếm cả T đầu. Đợt này áp dụng đếm đúng như viết (hoa/thường phân biệt) — hai cách chỉ khác nhau ở từ gốc viết hoa; 1768 theo đúng ví dụ (run 14). Nếu coordinator muốn đếm không phân biệt hoa/thường thì chỉ 1768 và các dòng "Phậppp…" viết hoa cần rà lại (danh sách đầy đủ trong file kiểm chứng `_u12b_verify.py` — v3 đã kiểm 298/298 theo quy ước này).
- **(F5) Ranh giới U12a:** (i) lr_ポーレットh2 1178 — dòng vừa có dialogue ngoài （ ） vừa có （ ） SFX phải sửa; đợt này chỉ sửa phần （ ）, dialogue để U12a. (ii) ハチロクh8 1561 (cờ F8 của U12a: んくっ trong （ ）) là token đối thoại (んくっ → "Ưn ku"), không có token dài — đúng ra ngoài phạm vi U12b, không có trong đợt này.
- **(F6) M68:** 日々姫h3 1857 chuyển batch M68 follow-up (xem §4).
- **(F7) 真闇h2 1821 — hệ file vs hệ dòng:** file là hệ romaji nhưng dòng này đang dùng động từ VN ("Trượt tuột", cùng kiểu với 1822 "Siết" ×6); đợt này GIỮ hệ VN của dòng, chỉ thêm chữ kéo (t tổng 6). Nếu coordinator muốn chuyển sang romaji cho token dài này thì đó là quyết riêng.
- **(F8) Hiệu chỉnh ghi chép:** 1610 thuộc ポーレットh4 (không phải ハチロクh8), 1672 thuộc ポーレットh7 — cả hai đều đã giữ nguyên đúng ("nắn"/"tuột" đủ tổng 2).
- **(F9) Hiệu chỉnh thứ tự old_vn (22/11 ~11:35, coordinator CONFIRMED):** unification-đã-gộp > moan > audit > CSV3 (không phải moan > audit > unification như brief gốc). Đã kiểm lại toàn bộ 298 dòng theo thứ tự đúng: **0 dòng bị ảnh hưởng** — 0 trùng lặp với bất kỳ file unification đã gộp nào, 0 dòng moan-layer; 4 dòng audit-layer (lr追加_ひよこ 1418, ふかみh1 1651, ふかみh1 1675, 日々姫h4 1794 — old_vn lấy từ audit fix).
- **(F10) Hàng "dài" kéo dài (lr真闇追加h 1815/1850/1858/1859/1863 — "Trượt dàiiiiiiiii"):** là dòng HAS-RUN, nằm trong bucket quét mismatch (F2), không sửa ở đây.

## 6. Lượt soát 2 (bắt buộc — đọc lại toàn bộ fix theo JP)

- **Tổng: 303 dòng xét / tái kiểm chứng: 298 / loại: 5 / sửa: 43.** (303 = 298 fix cuối + 5 dòng loại sang giữ nguyên trong quá trình kiểm chứng. Riêng lượt đọc lại lần 2 từ đầu: 298/298 tái kiểm chứng, 0 loại, 1 sửa — lr_凪h2 1803 khôi phục stretch cho token2 katakana sau khi đối chiếu TOML-2; 42 sửa còn lại phát hiện ở vòng kiểm chứng bằng máy trước đó.)
- **5 dòng loại:** ハチロクh8 1532/1539, lr_凪h2 1836, ハチロクh6 1986, 稀咲h1 2039 — "tuột"/"phập" đã đủ tổng chữ = số marks, không cần thay đổi (phát hiện khi kiểm chứng bằng máy: fix thảo ban đầu cộng thừa 1 chữ).
- **43 dòng sửa trong kiểm chứng:** 41 dòng sai lệch ±1 chữ do đếm tay khi viết fix (chủ yếu dòng "co thắt"/"Phập"/"Véo"/"Trượt"/"tuốt" — chữ đầu của từ gốc bị đếm nhầm hoặc sót), 1 dòng 1794 凪h1 sai số học trong ghi chú, 1 dòng lr_凪h2 1803 (lượt soát 2). Trong đó 2567 sửa 2 lần, hiệu ròng bằng 0 (lần đầu sửa theo lỗi của verifier v2 — verifier chưa tách dấu …; đã hoàn lại giá trị gốc đúng).
- **Kiểm chứng cơ học:** (1) mọi `old_seg` xuất hiện đúng 1 lần trong `old_vn` (298/298); (2) đếm chữ kéo bằng máy trong từng `new_seg` theo quy tắc §2, tách sub-token trên gạch/… và đếm đúng như viết (298/298, `_u12b_verify.py` v3); (3) đối chiếu JP độc lập: đích size trong ghi chú khớp với token JP thật trong dòng (8 cờ, tất cả đều là lỗi parse ghi chú — đã giải thích từng cái: 1696 size = max(13,4) = 13; 2058/2160 ghi "(marks N)"; 1794 日々姫h3 size = max(6,4) = 6; 1794 凪h1 "+10 marks"; 1797 lr_日々姫h1 "+15 small-u"; 1818 "13u token3"; 1679 い×1 thuộc M14b); (4) đối chiếu script vị trí JP↔VN: 192 mục, tất cả đều do tokenization (cụm VN nhiều từ cho 1 token JP; chuỗi nối gạch; dòng rút gọn như 1909/1966/1787; hàng SPACED) — 6 dòng đọc tay riêng (1651, 1730, 2040, 2170, 1679, 2607) đều đúng, riêng 2607 khôi phục trạng từ "mạnh" (TW 用力) bị bỏ sót khi sửa ("Múttttt mạnh!!").
- **Diff cơ học:** mỗi fix chỉ khác `old_vn` đúng ở span （ ） cần sửa (298/298) — ngoại lệ duy nhất: 2607 rút gọn "Mút mạnh!!" → "Múttttt mạnh!!" (giữ "mạnh", chỉ kéo "Mút"); không fix nào động vào dialogue ngoài （ ） (trừ 1178 đã cờ ở F5).
- **Khối TOML:** 53 file / 298 key parse-verified, 0 lệch (giá trị `\n` chữ trong fix được viết `\\n` trong khối; xem §7).

## 7. Khối TOML (parse-verified, theo file)

# lr_ふかみh2_セックスの意味.txt.toml
[script]
"1732" = "（Nhóp nhépppppppppppp—— Cọ xát!!）"
"1739" = "（Phụt! Phụttt! Phụt! Phụt!）"
"1756" = "（Phụttttttt!!!!!!!）"
"1761" = "（Phậpppp!!!!!!!）"
"1772" = "（Co thắttttttt!!!!!!!）"
"1774" = "（Co thắtttttttttt!!!!!!!!!!）"

# lr_れいなh1_レディ・れいな.txt.toml
[script]
"1860" = "（Tè e e e e e e e e e e e e e e e e e e）"
"1866" = "（Chu siết t t t t t t t t t! Ực!!!）"
"1869" = "（Chu mút t t t t t t t——cạch!）"
"1888" = "（Siết chặttt）"
"1908" = "（Thắt! Siết chặtt! Thắt chặt!!）"
"1913" = "（Cạch! ——Siết chặt t t t t t!!）"

# lr_ハチロクh2_新しい服。新しい旅.txt.toml
[script]
"2166" = "（Phập——phập——phập——phậpp）"
"2178" = "（Phụttttttttt）"

# lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml
[script]
"1909" = "（Phậppppppppppp!! ——Cộc!）"
"1966" = "（Phậppppp!!!! ——Cộc! Ngoáy!）"
"1983" = "（Phậppppppppppppp!!!!）"

# lr_ポーレットh1_家族旅行の最終日の夜.txt.toml
[script]
"1662" = "（Co thắttttt dữ dội!!!）"
"1676" = "（Phụt! Phụt! Phụt! Phụttt!!）"
"1684" = "（Rút ra——đẩy vàoooo――――lút cán!!!）"
"1694" = "（Đâm vào——rút ra——đâm vào!\\nCọ xát——rút raaa——đâm vào!!）"
"1699" = "（Đâm vào——đẩy tớiiiii——lút cán!\\nRút ra——đẩy tớiiiiiii——lút cán!）"
"1709" = "（Siết! Siết! Siết chặtttttttt!）"
"1728" = "（Ôm chặttttt）"
"1729" = "（Siết chặt——co thắtt kịch liệt!!）"

# lr_ポーレットh2_デコレーション＆ミルク.txt.toml
[script]
"1178" = "「Muốn lên đỉnh bao nhiêu, thì cứ lên đỉnh bấy nhiêu——\\n（Ngậm lấy! Mút mátttttttttttttt mãnh liệt!）」"
"1707" = "（Co thắtt dữ dội——siết chặt——ép chặtt——co rút）"
"1708" = "（Co thắttttttttttt dữ dội!!!）"
"1718" = "（Phụt! Phụt! Phụtt! Phụt!!）"
"1721" = "（Phụt! Phụt——tí tách——phụtt）"
"1725" = "（Phụt! Phụt! Phụt! Phụtt!）"
"1757" = "（Siết chặtt!!!）"
"1775" = "（Siết chặtt）"

# lr_凪h1_痛いの痛いの飛んでけばい.txt.toml
[script]
"1778" = "（Phụt! Phụtt! Phụt! Phụt!）"
"1784" = "（Phậppppppppppppp! Phập!）"
"1786" = "（Siếttttt!!! Chụt!）"
"1800" = "（Nắn! Bópppp! Phập!）"
"1801" = "（Nắn! Xoa! Vò! Siếtt!）"
"1816" = "（Banh raaaaaaaa!!）"
"1819" = "（Đẩyyyyy mạnh!! Vê! Ép! Chụt）"
"1834" = "（Siếtttt!!!!!）"
"1835" = "（Siếtttt!!!）"
"1836" = "（Siếttttt!）"

# lr_凪h2_虎さんの交尾.txt.toml
[script]
"1803" = "（Liếm——mútt——phụt——chụtt）"
"1804" = "（Nhóp nhéppp——liếm——liếm——ngoáy）"
"1808" = "（Ngoạm! Chụttt! Mút! Liếm!）"
"1809" = "（Phụt——phụt——phụt——phụtt……）"
"1815" = "（Phậpppppppppppp! Phập!）"
"1816" = "（Phậppp!!!!）"
"1825" = "（Trượtt! Phập! Trượt! Phập!）"
"1831" = "（Phậpp!!——Ngoáy!!）"
"1833" = "（Phậpppppppppp!!!! Phập!）"
"1834" = "（Phậpppppppp!!!!!!!）"
"1844" = "（Siếtttttttt!!!）"
"1848" = "（Liếmm! Ngoáy!!!!!!）"

# lr_凪ふかみh1_じぇいけい！.txt.toml
[script]
"2297" = "（Phụttt!）"
"2305" = "（Siếttttt!!!）"
"2314" = "（Trượtttttt——Phậpppp! Phập!）"
"2323" = "（Phậppppppppppp! Phập! Phập!）"
"2325" = "（Phậppppppppppp!!! Phập!）"
"2326" = "（Phậppppppppppppp!!!!）"
"2327" = "（Phậpppppppppp!!）"
"2340" = "（Siếttttttttttt!!!）"
"2341" = "（Siếttttt!!!）"
"2349" = "（Nhóp nhép——Phậpppppppp! Phập!）"

# lr_日々姫h1_鏡の中日々姫.txt.toml
[script]
"1773" = "（Siết! Siết chặt! Siết lạiii! Xoắn lại!）"
"1795" = "（Siết! Siết chặt lạiiiii! Co thắt! Siết!）"
"1797" = "（Thắt chặt lạiiiiiiiiiiiiiiii!!）"
"1818" = "（Trượt——rút raaaaaaaaaaaaaa）"

# lr_日々姫h2_デザートは食事の前に.txt.toml
[script]
"1659" = "（Siết! Siết chặtt! Trượt! Nhóp nhép）"
"1666" = "（Phụt! Bắn ra! Phụt! Phụtt!）"
"1668" = "（Phụtt! Phụt! Bắn ra! Phụt!）"
"1679" = "（Kéé）"
"1681" = "（Xoèèèèèèè）"

# lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml
[script]
"2425" = "（Phậppppppppp!!!!!!!! Cộc!!）"
"2434" = "（Bóp chặt! Tuốttttt mạnh!!!!）"
"2457" = "（Phậppppppppp――――bạch!!）"
"2458" = "（Phậpp! Cộc! Trơn tuột! Bạch!）"
"2459" = "（Phậppppppppp! Cộc!）"
"2467" = "（Trơn tuộttttttttt!!!!!!）"
"2468" = "（Trơn tuộtttt!!!!）"
"2473" = "（Phậppppppppppp! Cộc!!!）"

# lr_日々姫真闇h1_三人家族.txt.toml
[script]
"2368" = "（Pẹtt! Phụt! Phụt! Phụt!!）"
"2432" = "（Phậpppppp! ――Bụp! Trơn tuột）"

# lr_真闇h1_僕のおねえちゃん.txt.toml
[script]
"1612" = "（Nhào nặnnnnnn!!!）"
"1613" = "（Nhào nặnn! Chụt!!）"
"2107" = "（Siết chặtttttt!!!!）"
"2133" = "（Phụtt! Phụt! Phụt! Phụt）"
"2137" = "（Nhào nặnn!!!!）"
"2143" = "（Phụt! Phụt——phụtt…………phụt）"
"2165" = "（Ép chặttttttttttt!）"
"2166" = "（Trơn tuột! Chụtttttttttt! Chụt!）"
"2167" = "（Ép chặtttttttttt!!!!!）"
"2170" = "（Nhào nặnnn! Xoa bópppppp!）"
"2175" = "（Phập——rầm! Siết chặttt! Xoay!）"
"2186" = "（Siết chặt! Siết chặtt!）"
"2187" = "（Siết chặtt）"

# lr_稀咲h1_おしおきとごほうび.txt.toml
[script]
"1710" = "（Chọcccc――）"
"1712" = "（Véoooooooo mạnh!!!!!）"
"1713" = "（Véooooooooooo mạnh!!!!）"
"1715" = "（Véooooooooooooooo mạnh）"
"1717" = "（Véoooooooo mạnh!!）"
"1718" = "（Véoooooooooo mạnh!!!!!!）"
"1719" = "（Véooooooooooooo mạnh!!!!）"
"1727" = "（Véoooooooo mạnh!!!!!）"
"1728" = "（Véooooooooooo mạnh! Xoắn!!）"

# lr_稀咲ポーレットh1_悪い大人の契約.txt.toml
[script]
"2505" = "（Trượt——đâm sâuuuu——cọ xát——ju bu）"
"2567" = "（Chạm——miết——vuốttt……miết）"
"2590" = "（Siết chặtttt）"
"2607" = "（Múttttt mạnh!!）"

# lr真闇追加h_赤ちゃん、欲しか.txt.toml
[script]
"1813" = "（Trượt! Phập! Thọc! Xoáyyy!）"
"1826" = "（Phụttt! Phụt! Phụt! Phụt!）"
"1827" = "（Nhào nặnn!!）"
"1877" = "（Liếm——chụt——chùn chụt——liếm liếmmm）"

# lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml
[script]
"1418" = "（Nhóp nhépp!!!!!）"
"1589" = "（Phậpppp!!!!!!!!）"

# ふかみh1_ともはり練習.txt.toml
[script]
"1647" = "（Phụt t t t! Phụt! Phụt t t t!!）"
"1651" = "（Rột——chụtt! Nhóp nhép! Ực!）"
"1656" = "（Co thắttt!）"
"1664" = "（Co thắtttttt!!!!!!!!）"
"1671" = "（Phập p p p! Ngoáy y y y y y y y!!!）"
"1673" = "（Đâm sâuuuu!!!）"
"1674" = "（Trượt sâu u u u u u u u!）"
"1675" = "（Tõmmmmmmmm——!!!）"
"1683" = "（Liếm m m m m m m m!!!）"

# ふかみh2_homesweethome.txt.toml
[script]
"1736" = "（Ấnnn mạnh!）"
"1739" = "（Kh——Phập p p p p p p p p p p!）"
"1768" = "（Siết chặtttttttttt）"

# ふかみh3_夏休みの最後の日の、前の日.txt.toml
[script]
"3881" = "（Phụttt! Phụt! Phụt! Phụt!）"
"3892" = "（Rút raaaaaaaa!）"
"3896" = "（Ngoáy—— ngoáy! Ngoáy—— ngoáyyy）"
"3898" = "（Phậpppppppp! Cộc!!!）"
"3899" = "（Rút raaaa! Bạch! Phập! Cộc!）"
"3900" = "（Rút raaaaaaaa!!!!）"
"3902" = "（Nhấn sâuuuuuuu!）"
"3921" = "（Siết chặtttttt）"

# れいなh1_おかあさんのレッスン.txt.toml
[script]
"2324" = "（Phập phập phập phậpppppppppp!!）"

# れいなh2_おもらし防止大作戦.txt.toml
[script]
"1744" = "（Phụt! Phụtt! Phụt! Phụt!）"

# れいなh3_おもらし自由化大作戦.txt.toml
[script]
"1730" = "（Phụt! Phụt! Phụtt! Phụt!）"

# れいなh4_ふたりっきりのハロウィン.txt.toml
[script]
"3268" = "（Chụtt）"
"3273" = "（Phậpppppppppppp! Rầm!!）"
"3279" = "（Tách raaaa）"
"3289" = "（Siết chặtttttt!!!）"

# ハチロクh1_契り.txt.toml
[script]
"2140" = "（Xoạtttt）"
"2177" = "（Phập——phập——phập phập phậppp!——Bục）"
"2184" = "（Phập phập phậppppp!）"

# ハチロクh2_お勉強の成果.txt.toml
[script]
"1738" = "（Phụt! Phụt! Phụt! Phụtt!!）"

# ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml
[script]
"1651" = "（Siết chặtttt!）"
"1653" = "（Siết, siết chặtt）"
"1662" = "（Phậpppppppppp!!!）"
"1666" = "（Trượt trượt trượt trượt trượttttttt）"
"1669" = "（Trượtttttt!!!）"
"1674" = "（Nhấc bổnggg!）"
"1685" = "（Trượt raaaaaaaaa!!!）"
"1691" = "（Siết! Siết chặttt!!）"
"1697" = "（Phụt! Phụt! Phụt! Phụtt!）"
"1699" = "（Phụt! Phụt! Phụttt! Phụtt）"
"1705" = "（Trượt——siết chặtt——râm ran）"
"1713" = "（Siết chặttttttt!）"
"1714" = "（Thít chặtttttttt!!）"
"1716" = "（Vuốt veeeee）"

# ハチロクh5_おだいどこしごと.txt.toml
[script]
"1691" = "（Nhóp nhépppp）"
"1697" = "（Róc rách——róc——róc ráchhhh!）"
"1702" = "（Róc ráchhhhh）"
"1706" = "（Chụt——róc ráchhhhh!）"
"1708" = "（Thít! Siết chặtttttt!!）"
"1712" = "（Phụt! Phập! Phụt! Phậpp!）"
"1721" = "（Phụt! Phụt! Phụtt! Phụt!）"
"1730" = "（Rút raaaaaaa!）"

# ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml
[script]
"1929" = "（Ôm chặttt）"
"1931" = "（Thít! Siết chặt! Ưmm! Chụt!）"
"1935" = "（Phập——phậpp——cộc!）"
"1938" = "（Trượtt——mạnh!!!）"
"1944" = "（Phậpppppppppp!!!!）"
"1953" = "（Nhóp nhéppp）"
"1970" = "（Thít chặtt, siết chặt!）"
"1984" = "（Thít! Siết chặtttttttt!!!）"
"1990" = "（Phập phậpp! Phập phậppp!）"
"1995" = "（Phụt! Phụt! Phụt! Phụtt!）"
"2006" = "（Phụt! Phụt! Phụtt! Phụt!）"
"2023" = "（Thít chặttttttttt!!）"
"2024" = "（Siết chặtttttttttt!）"
"2036" = "（Ép chặtttttttttttt!!!）"

# ハチロクh7_レトロモダンメイクラヴ.txt.toml
[script]
"1880" = "（Liếm——ngoạm——chùn chụtt——bật ra!）"
"1883" = "（Thít! Siết chặttt! Trơn tuột! Lún sâuuu）"
"1896" = "（Phụt! Phụt!! Phụtt! Phụt!!）"
"1903" = "（Khít quáaaaaa!）"
"1928" = "（Nắn bóppp）"
"1929" = "（Thít chặtttttttt!!!）"
"1931" = "（Thít! Siết chặttttt! Co thắt!）"
"1932" = "（Siết chặtttttt!!!）"
"1933" = "（Siết chặttttt!）"

# ハチロクh8_桜色のひめごと.txt.toml
[script]
"1531" = "（Trơn tuột! Trơn tuộtt! Nhóp nhép! Trơn tuột!）"
"1550" = "（Tí tách——tí tách——tuôn tràoooo!）"
"1556" = "（Kyun! Siết chặtt! Mềm mại! Nắn bóp!）"
"1577" = "（Phụt! Phụt! Phụtt! Phụt!）"

# ポーレットh1_ファーストセックス.txt.toml
[script]
"1722" = "（Mút chặttt!）"
"1730" = "（Đâm phậpp——chát!）"
"1756" = "（Siết chặttttt!）"
"1774" = "（Rút ra——đâm vàooooooooo!!）"

# ポーレットh4_クリーム＆クリーム.txt.toml
[script]
"1593" = "（Bôi trơnnn）"
"1600" = "（Tách raaaaa!）"

# ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml
[script]
"1699" = "（Róc——róc rách róc rách róc ráchhhhhhh）"
"1725" = "（Trơn tuột——trơn tuột——rút——nhóp nhéppp——）"

# ポーレットh6_あなたとふたりの学園エッチ.txt.toml
[script]
"1552" = "（Phụt! Phụt! Phụt! Phụtt!）"
"1566" = "（Siết chặtttttt!!!）"
"1567" = "（Co bóp! Co bóp! Siết chặtt! Siết chặt!!）"
"1577" = "（Siết chặtttttt!!!）"

# ポーレットh7_残業エッチもyシャツで.txt.toml
[script]
"1649" = "（Phập! Phập! Chụt! Chụtt!）"
"1664" = "（Nhóp nhépppppp!）"
"1670" = "（Nắn! Bóp! Xoa! Mạnh lênnnn!）"
"1692" = "（Liếmmmm）"
"1695" = "（Siết! Siết chặtttttt!!）"
"1696" = "（Rột rột rộttttttttttttt!!!）"

# ポーレットh8_気動車の国のアリス.txt.toml
[script]
"3732" = "（Rột rộtt! Cộp! Phập! Cộp!）"
"3748" = "（Trượtttt）"
"3765" = "（Vuốt veeeeee）"

# 凪h1_ふたりっきりのデート.txt.toml
[script]
"1767" = "（Phụt! Phụt phụtt! Phụt! Phụt!）"
"1768" = "（Phập pppppppppppppp!!!）"
"1773" = "（Thắt tim! Siết chặtttt!）"
"1794" = "（Trượt——tuốttttttttt）"
"1797" = "（Trượt tuốtttttttt!!!）"
"1808" = "（Siết chặttttttttt!!!）"

# 凪ふかみh1_修学旅行の夜.txt.toml
[script]
"2030" = "（Éppp mạnh）"
"2038" = "（Thúccccccccccccc mạnh!）"
"2040" = "（Siết chặttt——siết——ép chặttt）"
"2056" = "（Siết chặttt!）"
"2058" = "（Nhuuu động）"

# 凪ふかみh2_みずあそび.txt.toml
[script]
"2155" = "（Phậppppppppp!）"
"2160" = "（Nhuuuuuuuuuuuuu động!!）"
"2170" = "（Trơn tuộttt——phập!!）"
"2174" = "（Trơn tuộtttttt!）"
"2179" = "（Siết chặtt）"
"2182" = "（Trượt vàooooooooooo!）"

# 日々姫h1_マッサージの続き.txt.toml
[script]
"1883" = "（Phụtt! Phụt! Phụt! Phụt!）"

# 日々姫h2_洗って大丈夫なスーツ.txt.toml
[script]
"1771" = "（Phụt! Phụt! Phụtt! Phụt!!）"
"1787" = "（Trượttttt!!!）"
"1798" = "（Co thắt——Siết chặttt）"

# 日々姫h3_汚れてしまった制服で.txt.toml
[script]
"1794" = "（Chùn chụtttttt!）"
"1796" = "（Chùn chụttttt!）"
"1800" = "（Phậppppppppppp!）"
"1802" = "（Chùn chụttttt!）"
"1804" = "（Phậppppppppppp!）"
"1811" = "（Phụt——Phụtt——Phụt! Phụt!）"
"1813" = "（Phụt! Phụt! Phụtt! Phụt!）"
"1814" = "（Phụt! Phụt! Phụt! Phụttt!）"
"1832" = "（Trượt raaaaaaaaaaaaaa!）"
"1844" = "（Thắt chặttt!!!）"
"1852" = "（Chảy xuốnggggggg）"
"1854" = "（Phậpppppppppppppp!!!）"

# 日々姫h4_いもうとタオル.txt.toml
[script]
"1747" = "（Nhớt nháppp）"
"1773" = "（Kẹp chặtt）"
"1774" = "（Kẹp chặttt）"
"1781" = "（Bóp nhẹeee）"
"1790" = "（Siết——Siết chặttt）"
"1794" = "（Thúc mạnh――――Nghiến chặtttt!!!）"
"1796" = "（Chảy xuốnggggg）"

# 日々姫h5_白濁絵の具の射精会.txt.toml
[script]
"2056" = "（Phập! Phập! Thúc! Phậpp!）"
"2058" = "（Phậpppp!!!!）"
"2062" = "（Chùn chụtttt!!!）"
"2091" = "（Xuyên thấuuuuuuu!!）"
"2096" = "（Siết! Siết! Siết chặtttttt!）"

# 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml
[script]
"3712" = "（Phụt! Phụt! Phụtt! Phụt!）"
"3714" = "（Phụt!!!!! Phụtttt!）"
"3722" = "（Ôm chặttt）"
"3723" = "（Kéo khóaaaa）"
"3729" = "（Siết chặtttttt!）"
"3735" = "（Xuyên thấuuuuuuuuuu! Thúc mạnh!!）"
"3736" = "（Phậpppppppppp! Thúc mạnh!）"

# 真闇h1_長期熟成.txt.toml
[script]
"1824" = "（Ép chặtttttttt!!!）"
"1833" = "（Nhỏ tong tỏnggggggggg）"

# 真闇h2_無濾過.txt.toml
[script]
"1821" = "（Trượt tuộttttt!!!）"
"1860" = "（Phụt! Phụt! Phụt! Phụtt!）"
"1893" = "（Ngoáy――tuộtt!）"

# 真闇h3_補習授業の廃校舎.txt.toml
[script]
"4014" = "（Phậpppppppp――――bạch!!）"
"4016" = "（Trượttt）"
"4042" = "（Siết chặttttt!!）"
"4043" = "（Siết chặtttttttt!）"

# 稀咲h1_性生活.txt.toml
[script]
"2042" = "（Phậppppppppppp――bịch!!!）"
"2045" = "（Phậpppppppppppp!!）"
"2055" = "（Siết chặttttt!）"
"2064" = "（Phụtttttt）"
"2067" = "（Phụt! Phụtt! Phụt! Phụt!）"
"2070" = "（Phụt! Phụt! Phụtt! Phụt!）"
"2072" = "（Phụt! Phụttt! Phụt! Phụt）"
"2074" = "（Kéoooo——）"

# 稀咲h2_プライベートルーム.txt.toml
[script]
"1932" = "（Phập――phậpppppp）"
"1933" = "（Phậpppp! Phập!!!）"
"1934" = "（Phậpppppppppp!!）"
"1935" = "（Phậppppp――）"
"1936" = "（Phậppppppp!!!）"
"1942" = "（Gừừừ! ――――Kyun!）"
"1955" = "（Phụtttt!!!）"
"1963" = "（Siết chặtttt!）"

# 稀咲h3_チャイナドレスでおもてなし.txt.toml
[script]
"3751" = "（Trơn tuộttt）"
"3754" = "（Phậpppppp!!!!）"
"3757" = "（Thít chặtttttt!!!）"
"3784" = "（Kéoooo mạnh）"

Kết bài: đợt U12b hoàn tất 2 mục mới M14 (298 dòng) + M19 (0 dòng sửa, 3 dòng kiểm lại). Quy tắc đếm đã thống nhất theo ví dụ của coordinator và hòa giải với mọi tiền lệ F1 đã kiểm chứng; 306-vs-122 và quét HAS-RUN mismatch (126 dòng) để lại cho coordinator quyết follow-up (F1, F2). File JSON + REVIEW này là đầu vào để gộp theo thứ tự đã định; không gửi gì cho Hieu.