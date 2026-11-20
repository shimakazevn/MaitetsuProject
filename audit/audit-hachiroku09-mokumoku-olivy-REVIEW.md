# Audit — ハチロク09_もくもくオリヴィ.txt.toml (01_Hachiroku)

- File: `ハチロク09_もくもくオリヴィ.txt.toml` — route 01_Hachiroku, 1 bản duy nhất.
- Disk: `sources/toml2/translation_toml/01_Hachiroku/#U30cf#U30c1#U30ed#U30af09_#U3082#U304f#U3082#U304f#U30aa#U30ea#U30f4#U30a3.txt.toml`
- md5: `a7aaca57dba45044b12d131baa097422` — không có file trùng (đã quét md5 toàn bộ 227 file TOML).
- Nội dung: chuyến tàu BBQ đầu tiên của Đầu máy số 9 mang tên Olivy — lễ tại ga suối nước nóng Ohitoyo, Soutetsu và Hachiroku đi tàu với tư cách vợ chồng (riêng tư), nướng thịt bò Aka-ou, bé Yuu (Misato Yuu) — đứa trẻ hay vẫy tay ở trạm chắn, Fukami đọc thông báo lần đầu, tới ga Yunoi, cảnh nhà tắm Tororyu-yu, chuyện về Hiyoko "Phượng Hoàng Lửa" ở Bảo tàng Đường sắt Omiya, kết bằng cảnh đêm hai người nắm tay nhau ngủ.
- Phương pháp: đọc từng dòng 477/477 đối chiếu JP + TW (CSV3), kiểm chứng sweep gasp, kiểm tra %l, kiểm tra trùng khóa / lệch dòng / mồ côi / chưa dịch.

## 1. Tổng quan

- Dòng script: **477** (độc thoại 169, Soutetsu 99, Hachiroku 86, Olivy 39, Fukami 19, bé Yuu 15, Niiroku 13, Nagi 13, Akai 10, Hibiki 9, mẹ của bé 5).
- CSV3: 1 set duy nhất, 477 khóa, 0 trùng khóa, 0 VN trống. TOML parse được, 477 khóa khớp CSV3 tuyệt đối về khóa.
- TOML vs CSV3: 276 dòng VN chỉ khác ở chỗ TOML-2 làm phẳng `\n` (literal) thành khoảng trắng — đã biết, CSV3 là chuẩn (đã kiểm chứng cơ học: 276/276 đều đúng dạng này, 0 lệch khác).
- `[selections]`: rỗng `{}`. Không có thẻ `%l` sai định dạng. Không có dòng VN nào bằng TW ngoài key 1071 (chỉ là dấu `――`/`——`, không phải chưa dịch).
- **Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.**

## 2. Kết quả: 34/477 (7,1%)

Phân loại (34):

- Thuật ngữ (đã quyết trong dự án): **20** — Ohimitera→Ohitoyo 7 (1037, 2029, 2835, 1521, 1819, 2698, 2116); Yui→Yunoi 5 (1771, 2831, 2030, 1572, 1006; 2698 mang cả hai lỗi); Đường sắt Hoàng gia→Teitetsu 4 (2028, 1645, 1482, 1481); Densha Hime→Công chúa Tàu điện 2 (2100, 1724); Minh Quốc (Nước Mỹ)→Meriken 1 (1606, furigana メリケン); thân máy bảo dưỡng→thân bảo trì 1 (1031).
- Dịch sai nghĩa: **8** — "cô bé"→"đứa bé" cho bé Yuu 5 (1925, 1628, 1670, 2631, 2556); 2870 "Rất muốn làm theo"→"Rất muốn lên tiếng nhắc nhở"; 1053 "cho tôi xem"→"cho chúng tôi xem" (TW 我們); 1951 "từ lâu rồi" bịa thêm (既に chỉ là "đã").
- Gasp (sweep): **3** — 1648, 1675, 1678.
- Lỗi chính tả: **2** — 1946 "chúng chúng ta", 1599 "Q-Quả"→"Qu-Quả".
- Gloss thừa (JP không có): **1** — 1508 bỏ "(Người phụ nữ Nhật Bản truyền thống)".

20 dòng thuật ngữ sửa trực tiếp trong audit (theo tiền lệ ハチロク07/ハチロク10) — KHÔNG thêm lại các key này vào hàng đợi thống nhất.

## 3. Danh sách sửa (34)

### 3.1. Thuật ngữ

**Key 1031 [monologue] — thuật ngữ.** JP: `……整備ボディをなくしたの。いまさらだけど――` / TW: `……可我的整備體已經遺失了。` — Cũ: `……Mình đã mất đi thân máy bảo dưỡng rồi. […]` → Mới: `……Mình đã mất đi thân bảo trì rồi. […]` (整備体/整備ボディ = "thân bảo trì" đã quyết.)

**Key 1771 [ハチロク] — thuật ngữ.** JP: `湯医線に関して` — Cũ: `Về Tuyến Yui,` → Mới: `Về Tuyến Yunoi,`.

**Key 1037 [monologue] — thuật ngữ.** JP: `御一夜温泉駅への入線も` — Cũ: `ga Suối nước nóng Ohimitera` → Mới: `ga Suối nước nóng Ohitoyo`.

**Key 2029 [ふかみ] — thuật ngữ.** JP: `御一夜鉄道バーベキュートレイン` — Cũ: `Đường sắt Ohimitera` → Mới: `Đường sắt Ohitoyo`.

**Key 2835 [monologue] — thuật ngữ.** JP: `御一夜鉄道職員としては` — Cũ: `Đường sắt Ohimitera` → Mới: `Đường sắt Ohitoyo`.

**Key 1521 [ハチロク] — thuật ngữ.** JP: `御一夜鉄道の車内で` — Cũ: `Đường sắt Ohimitera` → Mới: `Đường sắt Ohitoyo`.

**Key 1819 [双鉄] — thuật ngữ.** JP: `御一夜鉄道の車内でも` — Cũ: `Đường sắt Ohimitera` → Mới: `Đường sắt Ohitoyo`.

**Key 2698 [monologue] — thuật ngữ (2 lỗi trong 1 dòng).** JP: `御一夜－湯医は平坦路線` — Cũ: `đoạn Ohimitera - Yui` → Mới: `đoạn Ohitoyo - Yunoi`.

**Key 2831 [monologue] — thuật ngữ.** JP: `湯医線はまわっていく` — Cũ: `Tuyến Yui` → Mới: `Tuyến Yunoi`.

**Key 2030 [ふかみ] — thuật ngữ.** JP: `終点、湯医に到着します` — Cũ: `ga cuối, ga Yui` → Mới: `ga cuối, ga Yunoi`.

**Key 1572 [ふかみ] — thuật ngữ.** JP: `列車は、[ゆのい,1]湯医、終点湯医に到着いたします` — Cũ: `ga Yui, ga cuối Yui` → Mới: `ga Yunoi, ga cuối Yunoi`.

**Key 1006 [monologue] — thuật ngữ.** JP: `列車は湯医に着く` — Cũ: `ga Yui` → Mới: `ga Yunoi`.

**Key 2116 [双鉄] — thuật ngữ.** JP: `御一夜鉄道だって` — Cũ: `Đường sắt Ohimitera` → Mới: `Đường sắt Ohitoyo`.

**Key 1606 [ふかみ] — thuật ngữ.** JP: `[メリケン,1]冥国って感じ` (furigana メリケン — đọc thành tiếng) / TW: `更有美國的感覺` — Cũ: `cảm giác Minh Quốc (Nước Mỹ) hơn` → Mới: `cảm giác Meriken hơn`. (Theo quyết: メリケン nói thành tiếng thì giữ "Meriken"; khác key 1674 ruby めいこく thì giữ "Minh Quốc" — xem §5.)

**Key 2100 [オリヴィ] — thuật ngữ.** JP: `電車姫がいってた` — Cũ: `Densha Hime` → Mới: `Công chúa Tàu điện`.

**Key 1724 [双鉄] — thuật ngữ.** JP: `電車姫様がおっしゃっていた` — Cũ: `Densha Hime` → Mới: `Công chúa Tàu điện`.

**Key 2028 [双鉄] — thuật ngữ.** JP: `帝鉄時代は` — Cũ: `Thời Đường sắt Hoàng gia` → Mới: `Thời Teitetsu`.

**Key 1645 [ハチロク] — thuật ngữ.** JP: `帝鉄時代、でございますか？` — Cũ: `Thời Đường sắt Hoàng gia` → Mới: `Thời Teitetsu`.

**Key 1482 [オリヴィ] — thuật ngữ.** JP: `帝鉄のサイゴをみとった` — Cũ: `của Đường sắt Hoàng gia!` → Mới: `của Teitetsu!`.

**Key 1481 [ハチロク] — thuật ngữ.** JP: `帝鉄の最後を看取った` — Cũ: `của Đường sắt Hoàng gia——` → Mới: `của Teitetsu——`.

### 3.2. Dịch sai nghĩa

**Key 2870 [monologue] — dịch sai nghĩa.** JP: `（注意。すごくしたがってる。けど――待ってる――自分たちで気づくの――あっ！）` / TW: `（很明顯，她很想開口提醒。然而——她仍在等待——直到她們自己發現——啊！）` — Cũ: `（Cảnh báo. Rất muốn làm theo. […]` → Mới: `（Chú ý. Cô ấy rất muốn lên tiếng nhắc nhở. […]`. したがる = muốn (nói/làm điều gì đó); TW xác nhận Olivy "rất muốn mở miệng nhắc nhở", không phải "muốn làm theo". 注意 ở đây là Niiroku tự ghi chú, nên "Chú ý" đúng hơn "Cảnh báo".

**Key 1925 [双鉄] — dịch sai nghĩa (giới tính).** JP: `君はよく、踏切やさんのところで手をふってくれているこか` / TW: `那個經常在道口商店那邊朝我們揮手的就是你吧` (không giới tính) — Cũ: `Cháu là cô bé thường hay vẫy tay` → Mới: `Cháu là đứa bé thường hay vẫy tay`. JP こ = đứa trẻ (trung tính); Soutetsu lúc này chưa biết giới tính của Yuu (xem độc thoại 2373: "cậu bé……không, cô bé chứ?") — VN cũ đoán trước là gái, mâu thuẫn với sự mơ hồ có chủ ý của tác giả.

**Key 1628 [ハチロク] — dịch sai nghĩa (giới tính).** JP: `あのこ、先程の――ゆうちゃん` — Cũ: `Cô bé đó, là bé Yuu` → Mới: `Đứa bé đó, là bé Yuu`. (Cùng lý do 1925.)

**Key 1670 [ハチロク] — dịch sai nghĩa (giới tính).** JP: `あのこも言っていましたね` — Cũ: `cô bé đó cũng đã nói` → Mới: `đứa bé đó cũng đã nói`. (Cùng lý do 1925.)

**Key 2631 [monologue] — dịch sai nghĩa (giới tính).** JP: `車窓にながれる『もくもく』を期待してくれていたのなら` — Cũ: `khiến cô bé hài lòng` → Mới: `khiến đứa bé hài lòng`. (Cùng lý do 1925; "cô bé" ở đây vẫn là Yuu.)

**Key 2556 [monologue] — dịch sai nghĩa (giới tính).** JP: `おちびさんの瞳がきらきら輝く` / TW: `孩子的眼中閃著欣喜的光芒` — Cũ: `Đôi mắt của cô bé sáng long lanh.` → Mới: `Đôi mắt của đứa bé sáng long lanh.`. (Cùng lý do 1925.)

**Key 1053 [monologue] — dịch sai nghĩa.** JP: `あの日、父が見せようとしてくれた景色は` / TW: `那天，父親本想讓我們看的景色` (我們 = chúng tôi) — Cũ: `cha đã muốn cho tôi xem` → Mới: `cha đã muốn cho chúng tôi xem`. TW làm chứng số nhiều; JP 見せようとしてくれた không giới hạn ở một mình Soutetsu.

**Key 1951 [双鉄] — dịch sai nghĩa (bịa thêm).** JP: `僕とハチロクとの教導は、既に終わっていますから` (既に = đã rồi) — Cũ: `đã kết thúc từ lâu rồi.` → Mới: `đã kết thúc rồi.`. "Từ lâu rồi" (lâu rồi) không có trong JP.

### 3.3. Gasp (sweep)

**Key 1648 [ハチロク] — gasp (sweep #160, lost-gasp-whole).** JP: `「っ！」` / TW: `「唔！」` — Cũ: `「!」` → Mới: `「Ư!」`. Nhận fix sweep, đã kiểm chứng đúng JP.

**Key 1675 [双鉄] — gasp (sweep #161, lost-gasp-whole).** JP: `「っ！？」\n「きゃっ！？」` — Cũ: `「!?」\n「Á!?」` → Mới: `「Ư!?」\n「Á!?」`. Chỉ dòng 1 mất gasp; dòng 2 `きゃっ` đã có "Á". Nhận fix sweep.

**Key 1678 [双鉄] — gasp (sweep #1307, needs-file-audit — đã xử lý).** JP: `「っ！？\nな、なんと、もうか！？　あっという間だな」` — Cũ: `「!?\nCái, cái gì, đã đến rồi sao!? Mới chớp mắt một cái thôi mà.」` → Mới: `「Ư!?」\n「Cái, cái gì, đã đến rồi sao!? Mới chớp mắt một cái thôi mà.」`. Kết luận audit: VN dòng 2 KHÔNG lệch dòng (dịch đúng dòng 2 của JP); chỉ dòng 1 mất gasp, và VN cũ còn thiếu dấu `」` đóng ở dòng 1 — fix này bổ sung cả hai.

### 3.4. Lỗi chính tả

**Key 1946 [ハチロク] — lỗi chính tả.** JP: `明日もずっと、わたくしたちは一緒なのですから` — Cũ: `chúng chúng ta cũng sẽ luôn ở bên nhau` → Mới: `chúng ta cũng sẽ luôn ở bên nhau`. Thừa một "chúng".

**Key 1599 [ハチロク] — lỗi chính tả.** JP: `ま、まことに左様ですねっ！` (nói lắp ま、ま) — Cũ: `Q-Quả đúng là vậy nhỉ!` → Mới: `Qu-Quả đúng là vậy nhỉ!`. "Q-" đứng một mình không đọc được; lắp âm đầu "Qu-" mới đúng.

### 3.5. Gloss thừa

**Key 1508 [オリヴィ] — gloss thừa (JP không có).** JP: `ニイロクもヒノモトナデシコなんだね～！` (không có thẻ %l, không có chú thích) — Cũ: `Niiroku cũng là Yamato Nadeshiko (Người phụ nữ Nhật Bản truyền thống) nhỉ~!` → Mới: `Niiroku cũng là Yamato Nadeshiko nhỉ~!`. Chú thích trong ngoặc là thêm vào, không có cơ sở JP; cùng thuật ngữ ở key 1879 cũng không có gloss.

## 4. Sweep kiểm chứng

- Sweep có 3 mục cho file này (160, 161, 1307) — đã kiểm chứng cả 3, nhận cả 3 (1648, 1675, 1678). Không có mục sweep nào sai.
- Quét máy bổ sung các dòng VN chỉ còn dấu câu: 1668 `「！」`, 1649 `「！」「！！？」`, 1638 `「！！！」` — JP tương ứng cũng chỉ có dấu câu, không có っ → giữ nguyên, không phải gasp mất.
- Các っ khác đã được diễn đạt sẵn, không thêm Ư (theo quy tắc gasp đã khóa + tiền lệ ハチロク01 2319): 1651 `～～っ`→"~~", 1671 `あっ/あのっ`→"A/Cái đó", 1612 `あれっ`→"Ủa", 1680 `ばいっ`→"nè", 1667 `あはっ`→"Aha", 1666 `あははっ`→"Ahaha", 1747 `ふぁっ`→"Oáp." (ngáp), 1902 `（ちゅっ）`→"（Chụt）", 2866 `（ガクンッ！）`→"（Kịch!）", 2867 `（がっ！　がっ！）`→"（Cộc! Cộc!）", 2871 `（くるっ！）`→"（Lật!）", 2519 `ビッ！`→"Vút!", 2162 `ぱたぱた`→"Phạch phạch", 1644 `あむっ`→"Amu~", 1630 `ぱくっ`→"Paku~!".

## 5. Đã kiểm tra nhưng GIỮ NGUYÊN (không phải lỗi)

- **Soutetsu "anh" với Hachiroku (12 dòng: 1702, 1688, 1859, 2028, 1802, 1073, 1724, 1883, 1578, 1734, 1861, 1545; thêm 1891, 2116 dùng "anh"/"em") — GIỮ.** Từ key 1491 trở đi, hai người đóng vai vợ chồng trong chuyến đi riêng tư: Hachiroku gọi Soutetsu là だんなさま ("phu quân"), Soutetsu gọi cô là すず; 1819 khẳng định "hôm nay hoàn toàn là không gian riêng tư". Trong register vợ chồng, "anh/em" là đúng tiếng Việt. Trước cảnh này Soutetsu vẫn "tôi" với Hachiroku (1951: "tôi và Hachiroku") — VN tự chuyển register đúng lúc, có chủ ý. Không áp dụng máy móc quy tắc "tôi với Hachiroku" vào cảnh này. (Xem §7 — vẫn để Hieu xác nhận phạm vi.)
- **Key 2118 [ゆい,1]由衣 → "vùng Yui" — GIỮ, KHÔNG đổi thành Yunoi.** Đây là địa danh 由衣 (Yui), khác với 湯医 (Yunoi). Đã kiểm chứng: 7 dòng VN chứa "Yui" thì 6 dòng là 湯医 (đã sửa) và chỉ 2118 là 由衣.
- **Key 1674 [めいこく,1]冥国 → "Minh Quốc (Nước Mỹ)?" — GIỮ.** Furigana là めいこく (không phải メリケン), TW là 美國 — gloss "(Nước Mỹ)" khớp TW. Khác key 1606 (furigana メリケン → "Meriken", đã sửa).
- **Key 1482 "(Fushichou)" — GIỮ.** Olivy nói フシチョウ bằng katakana trong JP; gloss giữ lại từ cô ấy nói ra, không phải chú thích thêm.
- **Key 1891 thẻ %l — GIỮ.** JP gắn thẻ ở 蒸機, VN gắn ở 蒸気機関車, gloss "Đầu máy hơi nước" dịch đúng cả hai từ (cùng nghĩa "đầu máy hơi nước"). VN chỉ chuẩn hoá tên trong thẻ, không sai nghĩa — theo brief, trường hợp VN đã chuẩn hoá thì không chạm.
- **Key 1832 "thà nhìn" — GIỮ, KHÔNG phải lỗi đánh máy.** Đã kiểm chứng bằng codepoint: VN viết "thà nhìn từ buồng lái" — "thà" diễn むしろ (rather, "thà… còn hơn"), hoàn toàn đúng nghĩa JP `むしろ運転台からの方がおもしろかろうな`.
- **Key 2601 độc thoại Soutetsu "mình" — GIỮ.** Độc thoại nội tâm tự vấn ("…đã che chở cho cô ấy sao") — thuộc trường hợp ngoại lệ "Soutetsu inner monologue = mình" trong brief. Các "mình" khác trong độc thoại của Niiroku (1031, 2546, 2622, 2701) cũng giữ — brief không quy định đại từ độc thoại của Niiroku, và "mình" nhất quán trong độc thoại của cô.
- **Key 1071 VN==TW — không phải chưa dịch.** Chỉ là dấu `――` (JP) vs `——` (TW); VN khớp JP.
- **Key 1091/1042 罐屋 → "thợ máy" — GIỮ.** TW đều là 大車; "thợ máy" là cách dịch hợp lý và nhất quán cả 2 dòng, không có bằng chứng sai.
- **Key 2077 Akai gọi Soutetsu "anh Migita" — GIỮ.** Akai xưng 右田さん; "anh Migita" phù hợp.
- **Key 2537 "cô bé" — GIỮ.** "Cô bé" ở đây là Olivy (đã quay lại phòng), không phải Yuu — đúng giới tính.
- **Key 2373 "cậu bé……không, cô bé chứ?" — GIỮ.** Đây là sự mơ hồ có chủ ý của tác giả về giới tính Yuu; VN giữ đúng.

## 6. Lượt soát 2 (second pass)

- Tổng: **34** / đã soát lại từng fix đối chiếu JP: **34** / bỏ: **0** / sửa lại: **0**.
- JSON: 34 mục, key dạng chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 34/34; mỗi fix chỉ khác old VN đúng chỗ thay đổi có chủ đích (đã kiểm chứng cơ học bằng thay thế chuỗi chính xác 1 lần).
- Khối TOML: 34 khóa, parse được bằng tomllib, 0 sai lệch giá trị so với JSON (tomllib parse `\\n` về đúng literal backslash-n; đã đối chiếu raw string).

## 7. Chờ Hieu (không tự quyết)

- **Phạm vi "anh" của Soutetsu với Hachiroku ở nửa sau file:** các dòng "anh" trong cảnh tắm (1073, 1724, 1883, 1578, 1734) và cảnh đêm trên giường (1861, 1545, 1891, 2116) — chuyến đi đã kết thúc nhưng register vợ chồng vẫn tiếp tục trong VN. Audit giữ nguyên theo mạch cảnh; Hieu xác nhận có muốn giữ toàn bộ "anh" ở nửa sau, hay chỉ trong cảnh hẹn hò trên tàu.
- **Key 2027 "bác Seki":** Soutetsu gọi 堰さん là "bác Seki" (cùng dòng còn "anh Nagare", "anh Osamu"). Quyết định Seki = "ông ngoại" có áp dụng cho cách xưng hô của Soutetsu với Seki không, hay chỉ áp dụng cho quan hệ huyết thống phía Fukami?
- **Key 1508/1879 日ノ本撫子 → "Yamato Nadeshiko":** đã bỏ gloss giải thích ở 1508, giữ nguyên cụm "Yamato Nadeshiko" ở cả hai dòng. Hieu có muốn đổi thành "Hinomoto Nadeshiko" theo quyết định 日ノ本 = Hinomoto không?
- **Key 1848 詠国 → "Vịnh Quốc":** giữ theo lối phiên âm như Minh Quốc; TW là 英國 (nước Anh). Hieu có muốn chuẩn hoá thành "Anh Quốc" không?
- **Key 1599 "Qu-Quả":** cách diễn nói lắp — nếu Hieu có quy ước khác cho nói lắp thì báo lại.

## 8. Khối TOML (đã parse-verified)

```toml
"1006" = "——Và rồi, con tàu đã đến ga Yunoi."
"1031" = "……Mình đã mất đi thân bảo trì rồi. Giờ nói ra thì đã muộn màng——\\nKhông. Chuyện đó. Thực sự, đã quá muộn rồi."
"1037" = "……Việc tiến vào ga Suối nước nóng Ohitoyo, buổi lễ,\\nvà cả việc tiếp đón hành khách, đều được thực hiện vô cùng bài bản."
"1053" = "……Cảnh sắc mà ngày hôm đó, cha đã muốn cho chúng tôi xem.\\nTuyệt vời đến mức đó sao."
"1481" = "「Phượng Hoàng Lửa……chứng kiến giây phút cuối cùng của Teitetsu——」"
"1482" = "「Phượng Hoàng Lửa (Fushichou)! Tớ biết! Nổi tiếng lắm đó nha!\\n\\x%lレイルロオド;#00ffc040;Railord%l;#; đã chứng kiến giây phút cuối cùng của Teitetsu!」"
"1508" = "「Niiroku cũng là Yamato Nadeshiko nhỉ~!\\nThích thật đấy, tóc đen! Ghen tị quá đi!!」"
"1521" = "「Hôm nay, em sẽ là Suzu sao ạ? Rõ ràng là đang ở trên tàu của Đường sắt Ohitoyo,\\nhơn nữa, lại còn có cả cô Fukami ở đây nữa.」"
"1572" = "「Chân thành cảm ơn quý khách đã đồng hành cùng chúng tôi trên chặng đường dài.\\nTàu sắp đến ga Yunoi, ga cuối Yunoi ạ.」"
"1599" = "「Qu-Quả đúng là vậy nhỉ!\\nNếu còn mười phút nữa, thì, ừm, chúng ta phải chuẩn bị xuống tàu thôi.」"
"1606" = "「Và để bày tỏ sự tôn kính với quê hương của Đầu máy số 9 ạ.\\nThế này sẽ mang lại cảm giác Meriken hơn, quý khách có thấy vậy không ạ?」"
"1628" = "「Oa. Đứa bé đó, là bé Yuu——lúc nãy.」"
"1645" = "「Ưm.\\n……Thời Teitetsu, sao ạ?」"
"1648" = "「Ư!」"
"1670" = "「A! Nhắc mới nhớ, đứa bé đó cũng đã nói nhỉ.\\n『Nghi ngút khói vẫn chưa đủ』.」"
"1675" = "「Ư!?」\\n「Á!?」"
"1678" = "「Ư!?」\\nCái, cái gì, đã đến rồi sao!? Mới chớp mắt một cái thôi mà.」"
"1724" = "「Ừm. Chuyện về 『Kẻ kỳ quặc』,\\nmà Công chúa Tàu điện đã nhắc đến, anh đã nghe được rồi.」"
"1771" = "「Olivy-chan đã hoàn hảo rồi ạ. Về Tuyến Yunoi,\\nkhông còn gì tôi có thể dạy cho cô bé nữa đâu.」"
"1819" = "「Dù là trên tàu của Đường sắt Ohitoyo, nhưng hôm nay hoàn toàn là không gian riêng tư.\\nVé cũng đã mua đàng hoàng rồi.」"
"1925" = "「Ra là vậy——Cháu là đứa bé thường hay vẫy tay\\nở chỗ cửa hàng gần trạm chắn tàu đúng không?」"
"1946" = "「Không sao đâu ạ. Ngài Soutetsu.\\nVì ngày mai, chúng ta cũng sẽ luôn ở bên nhau mà.」"
"1951" = "「Không đâu, dù không có chuyện này thì chúng tôi cũng định đón khoảnh khắc này ở \\x%l客車;#00ffc040;toa hành khách%l;#; mà.\\nVì việc huấn luyện của tôi và Hachiroku, đã kết thúc rồi.」"
"2028" = "「Cái đó——ở Đế Đô thì sao?\\nThời Teitetsu, em đã từng nhìn thấy những cảnh sắc tuyệt vời nào qua cửa sổ?」"
"2029" = "「Kính thưa quý khách, cảm ơn quý khách hôm nay đã lên chuyến tàu BBQ của Đường sắt Ohitoyo,\\n『Olivy Nghi Ngút Khói』 ạ.」"
"2030" = "「Kính thưa quý khách, cảm ơn quý khách đã đồng hành cùng chuyến đi.\\nKhoảng mười phút nữa, tàu sẽ đến ga cuối, ga Yunoi ạ.」"
"2100" = "「Gì ấy nhỉ~, cái mà, Công chúa Tàu điện đã nói ấy.」"
"2116" = "「Tất nhiên rồi. Những \\x%lレイルロオド;#00ffc040;Railord%l;#; xuất sắc như em hay Olivy,\\nĐường sắt Ohitoyo chắc chắn cũng không muốn đánh mất đâu.」"
"2556" = "Đôi mắt của đứa bé sáng long lanh."
"2631" = "Nếu như mong đợi sự 『nghi ngút khói』 bay qua cửa sổ,\\nthì điểm đó, chắc chắn sẽ không thể khiến đứa bé hài lòng được."
"2698" = "Tuy lúc xuất phát có hơi đáng lo, nhưng đoạn Ohitoyo - Yunoi là một tuyến đường bằng phẳng.\\nHơn nữa, giữa chừng không hề dừng đỗ, Đầu máy số 9 cũng không chạy với tốc độ cao."
"2831" = "Vui mừng là vậy, nhưng mặt khác, tôi cũng cảm thấy có chút cô đơn.\\nDù không có chúng tôi, Tuyến Yunoi vẫn sẽ tiếp tục hoạt động."
"2835" = "Dù vô cùng thoải mái, nhưng với tư cách là nhân viên của Đường sắt Ohitoyo,\\ntôi vẫn hơi bận tâm việc các ghế không được lấp đầy."
"2870" = "（Chú ý. Cô ấy rất muốn lên tiếng nhắc nhở.\\nNhưng mà——đang chờ đợi——để họ tự nhận ra——a!）"
```

## Kết bài

File ハチロク09_もくもくオリヴィ.txt.toml: 477 dòng đã đọc hết, **34 dòng sai (7,1%)** — không có lệch dòng, không có chuỗi xoay, không có nhiễm chéo, không có dòng mồ côi, không có dòng chưa dịch, không có trùng khóa. Lỗi tập trung ở thuật ngữ đã quyết chưa được áp dụng (20 dòng: Ohitoyo, Yunoi, Teitetsu, Công chúa Tàu điện, Meriken, thân bảo trì) và 5 dòng gọi bé Yuu là "cô bé" trong khi giới tính của bé được tác giả cố tình để mơ hồ. Cảnh hẹn hò vợ chồng của Soutetsu–Hachiroku giữ nguyên register "anh/em" có chủ ý; 4 câu hỏi nhỏ để Hieu quyết ở §7 (phạm vi "anh" sau chuyến đi, "bác Seki", "Yamato Nadeshiko" vs "Hinomoto Nadeshiko", "Vịnh Quốc" vs "Anh Quốc"). Lượt soát 2: 34/34, 0 bỏ, 0 sửa. Khối TOML 34 khóa đã parse-verified, 0 sai lệch.

Kết bài
