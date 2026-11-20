# Audit: Nagi_Fukami 08b — 凪ふかみ08b_ふかみエピローグ_赤を切る勇気.txt.toml

**Ngày kiểm toán:** 20/11/2026 (hoàn thiện từ bản nháp bị ngắt giữa chừng — xem §2)
**Tệp TOML:** `07_Nagi_Fukami/凪ふかみ08b_ふかみエピローグ_赤を切る勇気.txt.toml` — md5 `393abd804e7ab4835e9d94b92ba53a75`, 125.909 byte, BOM + CRLF (1.271 CRLF, 0 LF-only), `[selections]` rỗng, **không có bản sao trùng** (kiểm tra md5 toàn bộ 227 tệp TOML).
**Nguồn CSV:** "Trang tính 3" — bộ hàng duy nhất `07_Nagi_Fukami` (không có bẫy dual-set ở file này), 609 hàng `[script]`, 0 key trùng.
**Kết quả: 69/609 dòng sai (11,3%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo file, 0 dòng mồ côi, 0 dòng chưa dịch, 0 key trùng.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| Thuật ngữ (terminology) | 29 |
| Đại từ (pronoun) | 1 |
| Gasp っ bị mất | 2 |
| Sai nghĩa (meaning) | 1 |
| SFX fa/fu | 2 |
| Gỡ thẻ gloss %l tự thêm (tag) | 34 |
| **Tổng** | **69** |

Thuật ngữ 29 = Ohitoyo 16 (1982, 2280, 2421, 2424, 2451, 2454, 2459, 2529, 2597, 2656, 2698, 3261, 3295, 3458, 3504, 3622) + Teitetsu 2 (2411, 2522) + Yunoi 2 (2658, 2775) + Teiou 1 (2156, lỗi đánh máy Teuou) + hoán đổi gloss 機関士/運転士 9 (1967, 2047, 2144, 2228, 2259, 2287, 2675, 2698, 3146 — 2698 tính 1 lần dù mang cả Ohitoyo).

**Theo loại dòng:** thoại 48/372 sai (12,9%), độc thoại 21/237 sai (8,9%). **Theo người nói:** monologue 21, ふかみ 19, レポーター 13, 双鉄 7, ハチロク 5, 凪 3, ポーレット 1.

## 2. Phương pháp và độ tin cậy của nguồn

- **Lịch sử file này:** agent đầu tiên (vòng audit 03:59 ngày 20/11) đã đọc toàn bộ 609 dòng và chốt 100 bản sửa, nhưng bị cắt bởi timeout của cron trước khi viết REVIEW.md + snippet — chỉ còn lại `audit-nagifukami08b-wrong.json` (dạng fix-only `{key: fix}`), `build08b-out.txt` (100 bản ghi OLD/NEW) và `build-08b-fixes.py` (script build + kiểm chứng). Agent hoàn thiện này KHÔNG đọc lại toàn bộ file từ đầu; công việc là **kiểm chứng cơ học 100 bản sửa + đọc lại lần 2 (second pass) từng bản sửa đối chiếu JP + TW**, rồi viết 3 deliverables. Các con số 0 lệch/0 chuỗi xoay/0 nhiễm chéo/0 mồ côi/0 chưa dịch là kết quả đọc toàn bộ của agent đầu tiên (không có bản sửa nào thuộc các nhóm đó trong 100 bản đã chốt).
- **Kiểm chứng cơ học (100 bản sửa):** jp/tw/old_vn đối chiếu CSV3 tuyệt đối 100/100 (old_vn trong build-out khớp CSV3); số thẻ %l trong bản sửa khớp số thẻ %l trong JP ở cả 100 dòng (chỉ 2411 còn 1 thẻ — đúng thẻ 入換 của JP); số lần `\n` giữ nguyên 100/100; mỗi bản sửa chỉ khác VN cũ ở chỗ sửa có chủ đích (difflib, residual ≤ 60 ký tự sau khi gỡ thẻ ở cả hai phía). Lưu ý: script build của agent đầu tiên so sánh VN cũ đã gỡ thẻ với bản sửa CHƯA gỡ thẻ nên residual của 2 dòng giữ thẻ (2397, 2411) bị tính thừa (27/40 thay vì 3/18) — chỉ là lỗi số liệu trong log, giá trị fix không sai; kiểm chứng lần này gỡ thẻ ở cả hai phía.
- **CSV vs TOML:** VN khớp tuyệt đối 243 hàng; khớp sau khi gộp `\n` thành khoảng trắng 366 hàng; **0 khác biệt thực chất**. JP comment trong TOML khớp CSV3 609/609.
- **Sweep っ (gasp):** kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` — file này CÓ 3 mục: 2250 (lost-gasp-whole) và 2405 (raw-tsu) áp nguyên đã kiểm chứng; 2232 already-rendered (JP 「っ！！！」, VN cũ 「Á!!!」 đã diễn gasp — không sửa, đúng). Không còn mục sweep nào khác cho file này.
- **Thẻ %l:** 41/69 bản sửa gỡ thẻ gloss do Gemini tự thêm (JP không có thẻ đó); chỉ 2411 giữ lại đúng 1 thẻ 入換 mà JP có. JP không có thẻ đóng sai nào trong các dòng đã sửa.
- **Kiểm tra nhiễm chéo:** không dòng Việt sai nào trùng với các file Nagi_Fukami lân cận (08a, 08c, 07, 09) hay bất kỳ file nào khác trong dự án (đối chiếu 69 giá trị VN cũ qua chỉ mục VN toàn dự án — các lần trùng đều là câu ngắn thông dụng hoặc SFX lặp lại hợp lệ).
- **Lượt soát 2: 100 tổng / 69 tái kiểm chứng / 31 loại bỏ / 0 sửa lại.** Đọc lại toàn bộ 100 bản sửa đối chiếu JP (+TW) lần 2; 31 bản bị loại bỏ xem §3 (không phải lỗi đọc sót — đó là một tiền đề xưng hô sai của agent đầu tiên, đã chứng minh bằng JP). 0 bản sửa giá trị (không có bản nào chỉ cần chỉnh nhẹ).

## 3. Các bản sửa BỊ LOẠI BỎ (31 dòng) — tiền đề xưng hô Nagi↔Fukami sai

Agent đầu tiên đổi 31 dòng theo tiền đề "Fukami là chị lớn của Nagi": Nagi gọi Fukami "bé" → "chị" (24 dòng), Fukami tự xưng "mình" → "chị" khi nói với Nagi (5 dòng), Fukami gọi Nagi "cậu" → "em" (2 dòng, 2473 + 2655 — 2655 kèm "Mình" → "Chị"). Tiền đề này SAI — bằng chứng JP + TW:

1. **JP ふかみh2 key 1118 (Fukami nói): 「アルバムの中、日々姫さん、わたしと凪ちゃんと同じくらいの年の頃から……」** — "trong album, Hibiki-san, từ hồi trạc tuổi **em và Nagi**…" — Fukami nói Hibiki hồi đó **trạc tuổi em và Nagi**, tức Fukami và Nagi **bằng tuổi nhau**. TW đồng ý: 「跟我還有小凪年紀差不多」 ("tuổi tác gần như nhau"). Hai người bằng tuổi thì không có "chị"/"em".
2. **Trong chính file này, key 2254, Nagi nói: 「ウチとふかみちゃんとにーさんは、友達やけん！」** — "mình, Fukami-chan và anh hai là **bạn bè**!" — Nagi tự xếp mình, Fukami và Soutetsu cùng một nhóm bạn bè (ngang hàng). TW: 「咱們不是朋友嗎！」.
3. **TW gọi Fukami là 小深 ("bé Fukami") trong lời Nagi** (2103, 2302, 2355, 2437, 2525, 2595: 「小深掌棹」「小深更有威嚴」…) — bản dịch Trung (độc lập) cũng xem Fukami là "bé", không phải "chị".
4. **Đếm toàn dự án:** Nagi gọi Fukami "bé" **58 lần**, "chị" **0 lần**; trong file này "bé" 24/24 dòng, "chị" 0 lần. Fukami tự xưng trong file này: "Mình" 8 lần, "Chị" 0 lần — chính agent đầu tiên cũng giữ "Mình" ở 2451 ("Mình xen vào thì kỳ lắm") trong khi đổi 5 dòng khác sang "Chị": mâu thuẫn nội bộ file.
5. **Tài liệu dự án:** cả Nagi và Fukami đều xưng "Em" (locations_and_characters.md §2.7–2.8); không có chỗ nào ghi Fukami lớn tuổi hơn Nagi. Quy tắc xưng hô Soutetsu đã chốt cũng không chạm tới cặp Nagi↔Fukami.

Vì vậy 31 bản sửa dưới đây BỊ LOẠI — giữ nguyên VN cũ. Ghi chú cho đợt thống nhất (unification pass): nếu Hieu muốn chuẩn hoá xưng hô Nagi↔Fukami thì quyết theo bằng chứng trên ("bé"/"cậu"/"mình" là dạng ngang hàng, đúng với JP); đừng áp ngược "chị"/"em" nếu không có bằng chứng tuổi tác mới.

- **Nagi → Fukami "bé" → "chị" (24 dòng, loại bỏ):** 1520, 1536, 2000, 2029, 2040, 2103, 2138, 2167, 2254, 2302, 2355, 2388, 2390, 2392, 2394, 2397, 2399, 2437, 2519, 2525, 2561, 2595, 2699, 2713. (2394 kèm "cậu để anh ấy" → "chị để anh ấy" — cũng loại; 2397 giữ nguyên thẻ 列車防護 của JP.)
- **Fukami tự xưng "mình" → "chị" với Nagi (5 dòng, loại bỏ):** 2384, 2452, 2463, 2483, 2584. (Riêng độc thoại nội tâm Fukami xưng "mình" là quy tắc ĐÃ CHỐT 19/11 — guidelines:115, 08a 43/49 dòng; các dòng này là thoại, không phải độc thoại, nhưng "chị" vẫn sai vì hai người bằng tuổi.)
- **Fukami → Nagi "cậu" → "em" (2 dòng, loại bỏ):** 2473 ("cậu……" → "em……"), 2655 ("Cảm ơn cậu" ×5 → "Cảm ơn em"; "Mình thích cậu lắm!" → "Chị thích em lắm!"). JP cả hai dòng đều là 凪ちゃん (Nagi-chan), không có dấu hiệu vai vế trên/dưới.
- **Giữ lại 1 dòng đại từ:** 2436 Paulette → Soutetsu "Cậu Soutetsu" → "Anh Soutetsu" (khóa B4 — Paulette gọi Soutetsu là "anh Soutetsu"; JP 双鉄くん, TW 雙鐵君). "bé Fukami" trong cùng dòng GIỮ NGUYÊN (Paulette là người lớn tuổi hơn, và "bé" là dạng mặc định toàn dự án).

## 4. Các lỗi đã sửa (69 dòng)

### 1473 — monologue — tag

JP: ……実際の語源は、車掌が持つ旗。
TW: ……其實這個詞最初是源於列車長拿的旗子。
**VN cũ:** ……Nguồn gốc thực sự của từ này là lá cờ mà \x%l車掌;#00ffc040;trưởng tàu%l;#; cầm.
**Bản sửa:** ……Nguồn gốc thực sự của từ này là lá cờ mà trưởng tàu cầm.
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 1967 — ふかみ — terminology

JP: 「運転士じゃなくて、機関士なんです。\nこの客車を引っ張るのは、[ハチロクニイマル,3]8620――蒸気機関車ですから」
TW: 「不是跳過駕駛員，是跳過司機。因為拉著這列客車的，是８６２０。也就是蒸汽機車」
**VN cũ:** 「Không phải \x%l運転士;#00ffc040;người lái tàu%l;#;, mà là \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; ạ.\nBởi vì thứ kéo \x%l客車;#00ffc040;toa hành khách%l;#; này là 8620――\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#;.」
**Bản sửa:** 「Không phải nhân viên cơ vụ, mà là người lái tàu ạ.\nBởi vì thứ kéo toa hành khách này là 8620――đầu máy hơi nước.」
Lý do: 機関士/運転士: gloss hoán đổi — 機関士 → "người lái tàu", 運転士 → "nhân viên cơ vụ" (quy ước thiểu số đã chốt: guidelines:60, ROUTE-AUDIT 1638/2108, 2129/2714) Gỡ 4 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 1982 — ふかみ — terminology

JP: 「いえ、そういうのは全く。\n御一夜鉄道のお客様は、みなさん、紳士・淑女ですし」
TW: 「不，我完全沒遇到過這種事。御一夜鐵路的客人們都是紳士淑女」
**VN cũ:** 「Không, hoàn toàn không có chuyện đó ạ.\nHành khách của Đường sắt Ohito, mọi người đều là những quý ông, quý bà cả.」
**Bản sửa:** 「Không, hoàn toàn không có chuyện đó ạ.\nHành khách của Đường sắt Ohitoyo, mọi người đều là những quý ông, quý bà cả.」
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt)

### 2047 — ふかみ — terminology

JP: 「例えば。機関士が気絶して、レイルロオドも動けない。\nその状況だと……列車、どうなっちゃいますか？」
TW: 「例如在司機暈了過去，鐵路人偶也動彈不得的情況下……列車會怎樣呢？」
**VN cũ:** 「Ví dụ như. \x%l機関士;#00ffc040;Nhân viên cơ vụ%l;#; ngất xỉu, \x%lレイルロオド;#00ffc040;Railord%l;#; cũng không thể di chuyển.\nTrong tình huống đó thì……\x%l列車;#00ffc040;tàu%l;#;, sẽ ra sao ạ?」
**Bản sửa:** 「Ví dụ như. Người lái tàu ngất xỉu, Railord cũng không thể di chuyển.\nTrong tình huống đó thì……tàu, sẽ ra sao ạ?」
Lý do: 機関士/運転士: gloss hoán đổi — 機関士 → "người lái tàu", 運転士 → "nhân viên cơ vụ" (quy ước thiểu số đã chốt: guidelines:60, ROUTE-AUDIT 1638/2108, 2129/2714) Gỡ 3 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2063 — ふかみ — tag

JP: 「実はわたし。車掌になってから、\n車掌弁、まだ一度も引けたことがなくって」
TW: 「其實，在成為列車長之後，我還沒有一次拉起列車長閥的經驗」
**VN cũ:** 「Thực ra thì tôi. Từ khi trở thành \x%l車掌;#00ffc040;trưởng tàu%l;#;,\nvẫn chưa một lần nào kéo van \x%l車掌;#00ffc040;trưởng tàu%l;#; cả.」
**Bản sửa:** 「Thực ra thì tôi. Từ khi trở thành trưởng tàu,\nvẫn chưa một lần nào kéo van trưởng tàu cả.」
Lý do: Gỡ 2 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2095 — ふかみ — tag

JP: 「車掌業務で一番むつかしいこと。ですか――」
TW: 「列車長的工作當中最困難的是哪一件？」
**VN cũ:** 「Điều khó khăn nhất trong nghiệp vụ \x%l車掌;#00ffc040;trưởng tàu%l;#;. Phải không ạ――」
**Bản sửa:** 「Điều khó khăn nhất trong nghiệp vụ trưởng tàu. Phải không ạ――」
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2096 — レポーター — tag

JP: 「しゃしょうべん？」
TW: 「列車長閥？」
**VN cũ:** 「Van \x%l車掌;#00ffc040;trưởng tàu%l;#;?」
**Bản sửa:** 「Van trưởng tàu?」
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2144 — レポーター — terminology

JP: 「右田機関士。\n少し、お話しをお伺いしてもいいですか？」
TW: 「右田司機，有幾個問題能問您一下嗎？」
**VN cũ:** 「\x%l機関士;#00ffc040;Nhân viên cơ vụ%l;#; Migita.\nTôi có thể hỏi anh vài câu được không?」
**Bản sửa:** 「Người lái tàu Migita.\nTôi có thể hỏi anh vài câu được không?」
Lý do: 機関士/運転士: gloss hoán đổi — 機関士 → "người lái tàu", 運転士 → "nhân viên cơ vụ" (quy ước thiểu số đã chốt: guidelines:60, ROUTE-AUDIT 1638/2108, 2129/2714) Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2156 — ハチロク — terminology

JP: 「ふふっ、お褒めに預かり光栄です。\n実のところわたくしの出身は、帝都・[ていおう,1]帝央でございます」
TW: 「呵呵，蒙您誇獎，我很榮幸。其實我就來自帝都中央車站」
**VN cũ:** 「Fufu, được khen ngợi là vinh hạnh của tôi.\nThực ra xuất thân của tôi là ở Teuou, Đế đô đấy ạ.」
**Bản sửa:** 「Fufu, được khen ngợi là vinh hạnh của tôi.\nThực ra xuất thân của tôi là ở Teiou, Đế đô đấy ạ.」
Lý do: Teuou là lỗi đánh máy của Teiou (JP 帝央 [ていおう], TW 帝都)

### 2174 — ふかみ — sfx

JP: 「ふぁっ――」
TW: 「哇……」
**VN cũ:** 「Hả――」
**Bản sửa:** 「Phà――」
Lý do: JP ふぁっ → "Phà" (quy tắc fa/fu đã chốt 19/11; bản cũ "Hả"/"Oa" không theo quy tắc)

### 2176 — ふかみ — sfx

JP: 「ふぁっ」
TW: 「哇」
**VN cũ:** 「Oa.」
**Bản sửa:** 「Phà.」
Lý do: JP ふぁっ → "Phà" (quy tắc fa/fu đã chốt 19/11; bản cũ "Hả"/"Oa" không theo quy tắc)

### 2223 — ふかみ — tag

JP: 「あ！　車掌弁を引く――車掌が列車を\n非常停止させることを、『赤を切る』っていうんです」
TW: 「啊！列車長拉下列車長閥，讓列車緊急停車，就叫“拉紅閥”」
**VN cũ:** 「A! Kéo van \x%l車掌;#00ffc040;trưởng tàu%l;#;――việc \x%l車掌;#00ffc040;trưởng tàu%l;#; làm cho \x%l列車;#00ffc040;tàu%l;#;\ndừng khẩn cấp, được gọi là 'cắt cờ đỏ' ạ.」
**Bản sửa:** 「A! Kéo van trưởng tàu――việc trưởng tàu làm cho tàu\ndừng khẩn cấp, được gọi là 'cắt cờ đỏ' ạ.」
Lý do: Gỡ 3 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2228 — レポーター — terminology

JP: 「え～！　そうなんですね。おもしろーい。\n運転士さんじゃなくて、機関士さん」
TW: 「啊！是這樣啊，真有意思。不是跳過駕駛員，而是跳過司機」
**VN cũ:** 「Ể~! Vậy sao. Thú vị quá.\nKhông phải \x%l運転士;#00ffc040;người lái tàu%l;#;, mà là \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#;.」
**Bản sửa:** 「Ể~! Vậy sao. Thú vị quá.\nKhông phải nhân viên cơ vụ, mà là người lái tàu.」
Lý do: 機関士/運転士: gloss hoán đổi — 機関士 → "người lái tàu", 運転士 → "nhân viên cơ vụ" (quy ước thiểu số đã chốt: guidelines:60, ROUTE-AUDIT 1638/2108, 2129/2714) Gỡ 2 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2238 — ふかみ — tag

JP: 「あ、その前に、[ハチロクニイマル,3]8620――\n蒸気機関車が転車して、客車と連結します」
TW: 「啊，在這之前，８６２０……蒸汽機車會轉車，與車廂相連」
**VN cũ:** 「A, trước đó, 8620――\n\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; sẽ xoay đầu trên \x%l転車台;#00ffc040;bàn quay đầu máy%l;#;, rồi kết nối với \x%l客車;#00ffc040;toa hành khách%l;#; ạ.」
**Bản sửa:** 「A, trước đó, 8620――\nđầu máy hơi nước sẽ xoay đầu trên bàn quay đầu máy, rồi kết nối với toa hành khách ạ.」
Lý do: Gỡ 3 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2250 — 凪 — gasp

JP: 「っ！！？」
TW: 「啊？！」
**VN cũ:** 「!!?」
**Bản sửa:** 「Ư!!?」
Lý do: Sweep lost-gasp-whole: JP cả dòng chỉ là っ + dấu câu, VN cũ chỉ còn dấu câu — thêm Ư (đã kiểm chứng trực tiếp sweep-raw-gasp-wrong.json)

### 2259 — ふかみ — terminology

JP: 「です。『機関士さん』って呼びかけてあげると、\n『わかってるな』って、きっと、喜んでもらえます」
TW: 「嗯。如果開口稱呼“司機”，對方也會覺得你很內行，會很開心的」
**VN cũ:** 「Vâng. Nếu gọi là '\x%l機関士;#00ffc040;nhân viên cơ vụ%l;#;',\nhọ sẽ nghĩ 'cô hiểu biết đấy', và chắc chắn sẽ rất vui.」
**Bản sửa:** 「Vâng. Nếu gọi là 'người lái tàu',\nhọ sẽ nghĩ 'cô hiểu biết đấy', và chắc chắn sẽ rất vui.」
Lý do: 機関士/運転士: gloss hoán đổi — 機関士 → "người lái tàu", 運転士 → "nhân viên cơ vụ" (quy ước thiểu số đã chốt: guidelines:60, ROUTE-AUDIT 1638/2108, 2129/2714) Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2280 — レポーター — terminology

JP: 「あー、そうだったんですか～！　でもそれって、\n御一夜鉄道さんが、それだけ安全！　ってことですよね」
TW: 「噢，是這樣嗎！也就是說，御一夜鐵路非常安全吧」
**VN cũ:** 「A, ra là vậy sao~! Nhưng mà như thế,\nchứng tỏ Đường sắt Ohito an toàn đến mức đó! Đúng không.」
**Bản sửa:** 「A, ra là vậy sao~! Nhưng mà như thế,\nchứng tỏ Đường sắt Ohitoyo an toàn đến mức đó! Đúng không.」
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt)

### 2285 — 双鉄 — tag

JP: 「逆転機！　後進フルギア！\n――[いれかえ,1]入換！　進行！！」
TW: 「回動機，全速後退！開始調車！！」
**VN cũ:** 「\x%l逆転機;#00ffc040;Cần đảo chiều%l;#;! Cài hết số lùi!\n――\x%l入換;#00ffc040;Dồn toa%l;#;! Tiến lên!!」
**Bản sửa:** 「Cần đảo chiều! Cài hết số lùi!\n――Dồn toa! Tiến lên!!」
Lý do: Gỡ 2 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2287 — ハチロク — terminology

JP: 「ファンサアビスも、\n機関士の大事な仕事、でございます」
TW: 「回饋鐵路愛好者，也是司機重要的工作」
**VN cũ:** 「Dịch vụ fan hâm mộ (fan service) cũng là,\ncông việc quan trọng của \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; đấy ạ.」
**Bản sửa:** 「Dịch vụ fan hâm mộ (fan service) cũng là,\ncông việc quan trọng của người lái tàu đấy ạ.」
Lý do: 機関士/運転士: gloss hoán đổi — 機関士 → "người lái tàu", 運転士 → "nhân viên cơ vụ" (quy ước thiểu số đã chốt: guidelines:60, ROUTE-AUDIT 1638/2108, 2129/2714) Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2320 — 凪 — tag

JP: 「にーさん！　[いれしん,4]入換信号機！ 進行ばい！」
TW: 「大哥哥！快看調車信號燈！可以前進囉！」
**VN cũ:** 「Anh Soutetsu! Đèn tín hiệu \x%l入換;#00ffc040;dồn toa%l;#;! Cho phép tiến lên rồi!」
**Bản sửa:** 「Anh Soutetsu! Đèn tín hiệu dồn toa! Cho phép tiến lên rồi!」
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2331 — レポーター — tag

JP: 「すごい……こんなに綺麗なレイルロオド。\n帝都にだって――」
TW: 「天啊……這麼漂亮的鐵路人偶，連帝都也沒有啊」
**VN cũ:** 「Tuyệt quá……Một \x%lレイルロオド;#00ffc040;Railord%l;#; xinh đẹp thế này.\nKể cả ở Đế đô cũng――」
**Bản sửa:** 「Tuyệt quá……Một Railord xinh đẹp thế này.\nKể cả ở Đế đô cũng――」
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2405 — 凪 — gasp

JP: 「そぎゃんとが」\n「はぅぅ～～っ」
TW: 「就是這樣」\n「嗚」
**VN cũ:** 「Là vậy đó」\n「Hauuu～～っ」
**Bản sửa:** 「Là vậy đó」\n「Hauuu～～Ư」
Lý do: Sweep raw-tsu: っ thô còn sót trong VN ("Hauuu～～っ") — diễn thành Ư (đã kiểm chứng trực tiếp sweep)

### 2407 — レポーター — tag

JP: 「赤を、切る――\nその車掌弁を、ぐいっと？」
TW: 「就要拉紅閥。把列車長閥拉下來」
**VN cũ:** 「Cắt, cờ đỏ――\nKéo mạnh cái van \x%l車掌;#00ffc040;trưởng tàu%l;#; đó?」
**Bản sửa:** 「Cắt, cờ đỏ――\nKéo mạnh cái van trưởng tàu đó?」
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2411 — ハチロク — terminology

JP: 「『\x%l入換;#00ffc040;入換%l;#;が出来て初めて車掌は一人前』――\n帝鉄では、そのように言われてもおりました」
TW: 「帝國鐵路時代有這樣一句俗語，“會\x%l入換;#00ffc040;調車%l;#;的才算獨當一面的列車長”」
**VN cũ:** 「'Phải biết \x%l入換;#00ffc040;dồn toa%l;#; thì mới là một \x%l車掌;#00ffc040;trưởng tàu%l;#; thực thụ'――\nỞ Đường sắt Hoàng gia, người ta cũng từng nói như vậy ạ.」
**Bản sửa:** 「'Phải biết \x%l入換;#00ffc040;dồn toa%l;#; thì mới là một trưởng tàu thực thụ'――\nỞ Teitetsu, người ta cũng từng nói như vậy ạ.」
Lý do: 帝鉄 → "Teitetsu" (quy tắc đã chốt) Gỡ thẻ %l 車掌 do Gemini tự thêm (JP chỉ có thẻ 入換, giữ nguyên trong bản sửa)

### 2421 — レポーター — terminology

JP: 「そんな御一夜鉄道の、頼もしい美人車掌さん！\n早瀬ふかみさんには、実はもう一つの顔があるんです！」
TW: 「御一夜鐵路這位可靠的美女列車長早瀨深美，其實有不為人知的另一面！」
**VN cũ:** 「Nữ \x%l車掌;#00ffc040;trưởng tàu%l;#; xinh đẹp đáng tin cậy của Đường sắt Ohito!\nCô Hayase Fukami thực ra còn có một thân phận khác nữa!」
**Bản sửa:** 「Nữ trưởng tàu xinh đẹp đáng tin cậy của Đường sắt Ohitoyo!\nCô Hayase Fukami thực ra còn có một thân phận khác nữa!」
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt) Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2424 — レポーター — terminology

JP: 「御一夜って、美人の湯とか美形の湯とかあるんですか？\n会う人会う人、みんなすっごく顔立ちが綺麗で」
TW: 「御一夜難不成有美女溫泉、型男溫泉嗎？見到的人一個個不是漂亮就是帥氣」
**VN cũ:** 「Ở Ohito, có suối nước nóng mỹ nhân hay suối nước nóng mỹ nam gì không vậy?\nGặp ai cũng thấy nét mặt đẹp cực kỳ luôn」
**Bản sửa:** 「Ở Ohitoyo, có suối nước nóng mỹ nhân hay suối nước nóng mỹ nam gì không vậy?\nGặp ai cũng thấy nét mặt đẹp cực kỳ luôn」
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt)

### 2436 — ポーレット — pronoun

JP: 「おめでとう！　双鉄くん、ふかみちゃん！」
TW: 「恭喜你們！雙鐵君，深美！」
**VN cũ:** 「Chúc mừng nha! Cậu Soutetsu, bé Fukami!」
**Bản sửa:** 「Chúc mừng nha! Anh Soutetsu, bé Fukami!」
Lý do: Paulette → Soutetsu: 双鉄くん → "anh Soutetsu" (khóa B4); "bé Fukami" giữ nguyên (Paulette là người lớn tuổi hơn; dạng "bé" là mặc định toàn dự án)

### 2451 — ふかみ — terminology

JP: 「わたしが邪魔しちゃ、おかしい、し……それに、あ！\nそれに！　御一夜鉄道の広報にも関わることかもだし」
TW: 「我不應該打擾他的……而且，啊！而且，事關御一夜鐵路的宣傳」
**VN cũ:** 「Mình xen vào thì kỳ lắm, với lại, a!\nVới lại! Cũng có thể liên quan đến việc quảng bá của Đường sắt Ohito nữa.」
**Bản sửa:** 「Mình xen vào thì kỳ lắm, với lại, a!\nVới lại! Cũng có thể liên quan đến việc quảng bá của Đường sắt Ohitoyo nữa.」
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt)

### 2454 — 双鉄 — terminology

JP: 「僕も同意だ。このツアーばかりは御一夜鉄道ならでは。完全な独自性を持つ、大きな売りであるのだからな」
TW: 「我也贊同。這條旅行線路是御一夜鐵路獨有的。正因獨特，才有宣傳的價值」
**VN cũ:** 「Anh cũng đồng ý. Chuyến đi này là đặc sản riêng của Đường sắt Ohito.\nMang tính độc đáo hoàn toàn, là một điểm nhấn lớn mà.」
**Bản sửa:** 「Anh cũng đồng ý. Chuyến đi này là đặc sản riêng của Đường sắt Ohitoyo.\nMang tính độc đáo hoàn toàn, là một điểm nhấn lớn mà.」
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt)

### 2459 — ハチロク — terminology

JP: 「ただいま双鉄様からご紹介に預かりました、御一夜鉄道\n[ハチロクニイマルごう,4]8620号専用レイルロオド。ハチロクでございます」
TW: 「我就是剛才雙鐵少爺介紹的御一夜鐵路８６２０號專用鐵路人偶八六」
**VN cũ:** 「Tôi là \x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của đầu máy 8620 thuộc Đường sắt Ohito,\nvừa được ngài Soutetsu giới thiệu. Tôi là Hachiroku ạ.」
**Bản sửa:** 「Tôi là Railord chuyên dụng của đầu máy 8620 thuộc Đường sắt Ohitoyo,\nvừa được ngài Soutetsu giới thiệu. Tôi là Hachiroku ạ.」
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt) Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2522 — 双鉄 — terminology

JP: 「なるほど……帝鉄では長距離の列車も多かっただろうし、車掌が[いれかえ,1]入換誘導をせざるを得ないケースもありそうだが」
TW: 「是嗎……帝國鐵路時代，長距離運營的列車較多，許多時候列車長必須引導調車」
**VN cũ:** 「Ra là vậy……Ở Đường sắt Hoàng gia chắc cũng có nhiều chuyến \x%l列車;#00ffc040;tàu%l;#; đường dài, có vẻ cũng có những trường hợp \x%l車掌;#00ffc040;trưởng tàu%l;#; bắt buộc phải hướng dẫn \x%l入換;#00ffc040;dồn toa%l;#; nhỉ.」
**Bản sửa:** 「Ra là vậy……Ở Teitetsu chắc cũng có nhiều chuyến tàu đường dài, có vẻ cũng có những trường hợp trưởng tàu bắt buộc phải hướng dẫn dồn toa nhỉ.」
Lý do: 帝鉄 → "Teitetsu" (quy tắc đã chốt) Gỡ 3 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2527 — ふかみ — tag

JP: 「です。危険があるって少しでも感じたときは――\n車掌には、赤を切る義務があります」
TW: 「是的。即使只是察覺到存在些許危險，列車長也有必須拉紅閥的義務」
**VN cũ:** 「Vâng. Khi cảm thấy có chút nguy hiểm nào đó――\n\x%l車掌;#00ffc040;Trưởng tàu%l;#; có nghĩa vụ phải cắt cờ đỏ ạ.」
**Bản sửa:** 「Vâng. Khi cảm thấy có chút nguy hiểm nào đó――\nTrưởng tàu có nghĩa vụ phải cắt cờ đỏ ạ.」
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2529 — ふかみ — terminology

JP: 「はい。御一夜鉄道が[しんぞうさいせい,3]新造再生したバーベキュー客車、\nオロ31 27には、[しゃしょうべん,2]車掌弁がついてるんですけど――」
TW: 「是的。御一夜鐵路的全新改造ＢＢＱ客車Ｏｒｏ３１　２７有列車長閥……」
**VN cũ:** 「Vâng. Toa hành khách BBQ được Đường sắt Ohito tân trang lại,\nOro31 27, có trang bị van \x%l車掌;#00ffc040;trưởng tàu%l;#;――」
**Bản sửa:** 「Vâng. Toa hành khách BBQ được Đường sắt Ohitoyo tân trang lại,\nOro31 27, có trang bị van trưởng tàu――」
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt) Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2532 — ふかみ — tag

JP: 「はい。安全が損なわれてはいけませんから――\nそれは、車掌が必ず果たすべき義務となるんです」
TW: 「是的。無論如何，安全第一……保障安全，正是列車長的義務」
**VN cũ:** 「Vâng. Vì không thể để sự an toàn bị tổn hại――\nĐó trở thành nghĩa vụ mà \x%l車掌;#00ffc040;trưởng tàu%l;#; bắt buộc phải hoàn thành.」
**Bản sửa:** 「Vâng. Vì không thể để sự an toàn bị tổn hại――\nĐó trở thành nghĩa vụ mà trưởng tàu bắt buộc phải hoàn thành.」
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2533 — ふかみ — tag

JP: 「はい。機関車、8620の運転台に、走行中の客車から\n入り込むことはできません。だから、そういうときには」
TW: 「是的。行駛時我們無法從客運車廂到達８６２０機車的駕駛台，因此呢，在這種時候……」
**VN cũ:** 「Vâng. Từ \x%l客車;#00ffc040;toa hành khách%l;#; đang chạy, không thể đi vào\n\x%l運転台;#00ffc040;buồng lái%l;#; của đầu máy 8620 được. Vì vậy, những lúc như thế」
**Bản sửa:** 「Vâng. Từ toa hành khách đang chạy, không thể đi vào\nbuồng lái của đầu máy 8620 được. Vì vậy, những lúc như thế」
Lý do: Gỡ 2 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2597 — ふかみ — terminology

JP: 「困るよ！　せっかく鉄道が大きく復活するチャンスだし。\nそれに、御一夜鉄道にお客さんが来たら、川下りだって」
TW: 「當然有問題了！這可是鐵路復活的大好機會，而且，如果御一夜鐵路的客人變多了，漂流的客人也會變多的」
**VN cũ:** 「Rắc rối chứ! Khó khăn lắm đường sắt mới có cơ hội phục sinh mạnh mẽ mà.\nHơn nữa, nếu có khách đến Đường sắt Ohito, thì dịch vụ xuôi dòng sông cũng sẽ.」
**Bản sửa:** 「Rắc rối chứ! Khó khăn lắm đường sắt mới có cơ hội phục sinh mạnh mẽ mà.\nHơn nữa, nếu có khách đến Đường sắt Ohitoyo, thì dịch vụ xuôi dòng sông cũng sẽ.」
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt)

### 2613 — 双鉄 — tag

JP: 「カマはできたか」
TW: 「窯弄好了嗎？」
**VN cũ:** 「\x%l窯;#00ffc040;Lò hơi%l;#; chuẩn bị xong chưa?」
**Bản sửa:** 「Lò hơi chuẩn bị xong chưa?」
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2618 — ふかみ — tag

JP: 「簡単にいうと、非常ブレーキです。これをひけば、\n運転台での運転操作を無視して、列車を停止できます」
TW: 「簡單地來說就是緊急剎車裝置。只要拉下這個，就可以跳過駕駛台的操作，直接停車」
**VN cũ:** 「Nói đơn giản thì, nó là \x%l非常;#00ffc040;phanh khẩn cấp%l;#;. Nếu kéo cái này,\ncó thể phớt lờ thao tác lái ở \x%l運転台;#00ffc040;buồng lái%l;#; và dừng tàu lại.」
**Bản sửa:** 「Nói đơn giản thì, nó là phanh khẩn cấp. Nếu kéo cái này,\ncó thể phớt lờ thao tác lái ở buồng lái và dừng tàu lại.」
Lý do: Gỡ 2 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2656 — ふかみ — terminology

JP: 「おかげさまで、です。御一夜鉄道は開業以来、\n怪我人を出すような事故を、一件も起こしていません」
TW: 「謝謝您的誇獎。自開張以來，御一夜鐵路從未發生任何有人受傷的事故」
**VN cũ:** 「Cũng nhờ ơn mọi người ạ. Đường sắt Ohito từ khi khai trương đến nay,\nchưa từng để xảy ra một vụ tai nạn nào gây thương tích cho hành khách.」
**Bản sửa:** 「Cũng nhờ ơn mọi người ạ. Đường sắt Ohitoyo từ khi khai trương đến nay,\nchưa từng để xảy ra một vụ tai nạn nào gây thương tích cho hành khách.」
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt)

### 2658 — レポーター — terminology

JP: 「ありがとうございますー！　ここオッケー？\nじゃ、湯医まで連れてってくださーい」
TW: 「謝謝！這一段可以了嗎？好的，接下來請帶我們去湯醫吧」
**VN cũ:** 「Cảm ơn rất nhiều~! Chỗ này OK chứ?\nVậy, xin hãy đưa chúng tôi đến Yui nha~」
**Bản sửa:** 「Cảm ơn rất nhiều~! Chỗ này OK chứ?\nVậy, xin hãy đưa chúng tôi đến Yunoi nha~」
Lý do: 湯医 → "Yunoi" (quy tắc đã chốt)

### 2675 — レポーター — terminology

JP: 「運転士さん関係なしにですか？　一体、どうして」
TW: 「跳過駕駛員？怎麼辦到的？」
**VN cũ:** 「Không cần quan tâm đến \x%l運転士;#00ffc040;người lái tàu%l;#; sao? Rốt cuộc là, tại sao lại vậy?」
**Bản sửa:** 「Không cần quan tâm đến nhân viên cơ vụ sao? Rốt cuộc là, tại sao lại vậy?」
Lý do: 機関士/運転士: gloss hoán đổi — 機関士 → "người lái tàu", 運転士 → "nhân viên cơ vụ" (quy ước thiểu số đã chốt: guidelines:60, ROUTE-AUDIT 1638/2108, 2129/2714) Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2698 — レポーター — terminology

JP: 「こちらが、御一夜鉄道バーベキュー列車、\nもくもくハチロク号の、右田双鉄機関士です！」
TW: 「這位就是御一夜鐵路ＢＢＱ列車大快朵頤八六號的司機右田雙鐵先生！」
**VN cũ:** 「Đây chính là \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; Migita Soutetsu,\ncủa chuyến tàu BBQ Đường sắt Ohito, tàu Mokumoku Hachiroku!」
**Bản sửa:** 「Đây chính là người lái tàu Migita Soutetsu,\ncủa chuyến tàu BBQ Đường sắt Ohitoyo, tàu Mokumoku Hachiroku!」
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt) 機関士/運転士: gloss hoán đổi — 機関士 → "người lái tàu", 運転士 → "nhân viên cơ vụ" (quy ước thiểu số đã chốt: guidelines:60, ROUTE-AUDIT 1638/2108, 2129/2714) Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2717 — レポーター — tag

JP: 「で、ですね？　今日は、蒸気機関車について、\n簡単に教えてもらいたいんですけど」
TW: 「那、那麼，今天我們希望您能回答一些關於蒸汽機車的簡單問題」
**VN cũ:** 「Và, tiếp theo nhé? Hôm nay, về \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#;,\ntôi muốn nhờ anh giải thích một cách đơn giản được không」
**Bản sửa:** 「Và, tiếp theo nhé? Hôm nay, về đầu máy hơi nước,\ntôi muốn nhờ anh giải thích một cách đơn giản được không」
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2724 — 双鉄 — tag

JP: 「それは、この8620のレイルロオドと機関助士とが。\nハチロク！　日々姫！　下りて来てくれ」
TW: 「那些問題就由８６２０的鐵路人偶與司爐回答吧。八六！日日姬！下來吧」
**VN cũ:** 「Chuyện đó, \x%lレイルロオド;#00ffc040;Railord%l;#; và \x%l機関助士;#00ffc040;phụ lái tàu%l;#; của chiếc 8620 này sẽ lo.\nHachiroku! Hibiki! Xuống đây đi.」
**Bản sửa:** 「Chuyện đó, Railord và phụ lái tàu của chiếc 8620 này sẽ lo.\nHachiroku! Hibiki! Xuống đây đi.」
Lý do: Gỡ 2 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2732 — 双鉄 — tag

JP: 「では僕も、一足先に運転台に入っておこう」
TW: 「那我就先去駕駛台吧」
**VN cũ:** 「Vậy anh cũng vào \x%l運転台;#00ffc040;buồng lái%l;#; trước một bước đây.」
**Bản sửa:** 「Vậy anh cũng vào buồng lái trước một bước đây.」
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2735 — 双鉄 — tag

JP: 「ならば行ってこよう。……ハチロク。\nキャブを降りる時に、決まるようなセリフはあるか？」
TW: 「那我就過去了。……八六，走下駕駛台的時候有什麼合適的話可以說嗎？」
**VN cũ:** 「Vậy thì anh đi đây. ……Hachiroku.\nLúc bước xuống khỏi \x%lキャブ;#00ffc040;buồng lái%l;#;, có câu thoại nào nghe cho ngầu không?」
**Bản sửa:** 「Vậy thì anh đi đây. ……Hachiroku.\nLúc bước xuống khỏi buồng lái, có câu thoại nào nghe cho ngầu không?」
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2754 — ふかみ — meaning

JP: 「双鉄、おにー……双鉄、さん。\n――あっ――」
TW: 「雙鐵哥……雙鐵先生……啊……」
**VN cũ:** 「Anh Soutetsu……anh Soutetsu.\n――A――」
**Bản sửa:** 「Anh Soutetsu……ngài Soutetsu.\n――A――」
Lý do: Fukami tự sửa giữa câu: JP 双鉄、おにー……双鉄、さん — bản cũ lặp "anh Soutetsu" làm mất chỗ tự sửa; TW 雙鐵哥……雙鐵先生 ("anh……ngài") xác nhận

### 2761 — レポーター — tag

JP: 「それなら、『楽勝ーっ！」な感じだったり？\n車掌さんのお仕事って、案外」
TW: 「難不成列車長的工作其實挺輕鬆的？」
**VN cũ:** 「Nếu vậy, có phải cảm giác 'Dễ ợt!' không?\nCông việc của \x%l車掌;#00ffc040;trưởng tàu%l;#; ấy, không ngờ lại」
**Bản sửa:** 「Nếu vậy, có phải cảm giác 'Dễ ợt!' không?\nCông việc của trưởng tàu ấy, không ngờ lại」
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 2775 — ハチロク — terminology

JP: 「バーベキュー列車の車掌ふかみが、湯医につけば、\nすぐさまクマ川下りの船頭さんに早変わりする」
TW: 「ＢＢＱ列車的列車長深美，在抵達湯醫站之後，立刻就會變成隈河漂流的掌棹」
**VN cũ:** 「\x%l車掌;#00ffc040;Trưởng tàu%l;#; Fukami của chuyến tàu BBQ, khi đến Yui,\nsẽ ngay lập tức biến thành người chèo thuyền trên sông Kuma.」
**Bản sửa:** 「Trưởng tàu Fukami của chuyến tàu BBQ, khi đến Yunoi,\nsẽ ngay lập tức biến thành người chèo thuyền trên sông Kuma.」
Lý do: 湯医 → "Yunoi" (quy tắc đã chốt) Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3108 — monologue — tag

JP: 今日は助士二名の大所帯だが、混乱など無い。\n日々姫と凪とハチロクと僕、チームワークは出来ている。
TW: 今天有兩個司爐，但一點也不亂。日日姬、凪、八六和我配合得很默契。
**VN cũ:** Hôm nay là một đội lớn với hai \x%l機関助士;#00ffc040;phụ lái tàu%l;#;, nhưng không hề có sự hỗn loạn nào.\nHibiki, Nagi, Hachiroku và tôi, tinh thần làm việc nhóm đã được hình thành.
**Bản sửa:** Hôm nay là một đội lớn với hai phụ lái tàu, nhưng không hề có sự hỗn loạn nào.\nHibiki, Nagi, Hachiroku và tôi, tinh thần làm việc nhóm đã được hình thành.
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3146 — monologue — terminology

JP: ハチロクと似合うような、機関士像――\nそれは決して、べらべら喋るような男ではあるまい。
TW: 作為一個與八六般配的司機，我絕不能是一個喋喋不休的傢伙。
**VN cũ:** Hình tượng một \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; xứng đôi với Hachiroku――\nĐó tuyệt đối không phải là một gã đàn ông nói nhiều liến thoắng.
**Bản sửa:** Hình tượng một người lái tàu xứng đôi với Hachiroku――\nĐó tuyệt đối không phải là một gã đàn ông nói nhiều liến thoắng.
Lý do: 機関士/運転士: gloss hoán đổi — 機関士 → "người lái tàu", 運転士 → "nhân viên cơ vụ" (quy ước thiểu số đã chốt: guidelines:60, ROUTE-AUDIT 1638/2108, 2129/2714) Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3210 — monologue — tag

JP: 凪とふかみを後方に、レポーターとカメラマンとは、\nキャブから誰かが出て来るのを待ち構えている。
TW: 凪和深美身後的記者和攝影師似乎正在等什麼人從駕駛室出來。
**VN cũ:** Nagi và Fukami đứng ở phía sau, còn phóng viên và người quay phim\nđang chực chờ xem có ai bước ra từ \x%lキャブ;#00ffc040;buồng lái%l;#; không.
**Bản sửa:** Nagi và Fukami đứng ở phía sau, còn phóng viên và người quay phim\nđang chực chờ xem có ai bước ra từ buồng lái không.
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3239 — monologue — tag

JP: 運転台に戻るやいなやで、好奇心丸出しの日々姫に捕まる。
TW: 剛回到駕駛台，滿臉好奇的日日姬就問了起來。
**VN cũ:** Vừa trở lại \x%l運転台;#00ffc040;buồng lái%l;#;, tôi đã bị Hibiki với vẻ mặt đầy tò mò tóm lấy.
**Bản sửa:** Vừa trở lại buồng lái, tôi đã bị Hibiki với vẻ mặt đầy tò mò tóm lấy.
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3261 — monologue — terminology

JP: だが、これは御一夜鉄道の広報にも関わる問題で、\n僕の一存で、果たして断っていいものか――
TW: 可是事關御一夜鐵路的宣傳，我不能獨自決定。
**VN cũ:** Nhưng mà, đây là vấn đề liên quan đến việc quảng bá của Đường sắt Ohito,\nliệu tôi có nên tự ý từ chối hay không――
**Bản sửa:** Nhưng mà, đây là vấn đề liên quan đến việc quảng bá của Đường sắt Ohitoyo,\nliệu tôi có nên tự ý từ chối hay không――
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt)

### 3295 — monologue — terminology

JP: うむ。単純に否定するよりよい答えだろう。\n御一夜の温泉と、登呂流湯さんの宣伝もできた。
TW: 嗯，這個回答至少比單純的否定要好。而且還能宣傳御一夜的溫泉和登呂流浴場。
**VN cũ:** Ừm. Chắc là câu trả lời tốt hơn là chỉ đơn thuần phủ nhận.\nCũng quảng bá được cho suối nước nóng của Ohito và Nhà tắm Tororyu-yu nữa.
**Bản sửa:** Ừm. Chắc là câu trả lời tốt hơn là chỉ đơn thuần phủ nhận.\nCũng quảng bá được cho suối nước nóng của Ohitoyo và Nhà tắm Tororyu-yu nữa.
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt)

### 3338 — monologue — tag

JP: 客車最後部の車掌弁へとレポーターを案内し、\n手でひくような素振りをみせる。
TW: 她帶著記者來到客車最後方的緊急剎車系統處，作了一個拉剎車的動作。
**VN cũ:** Hướng dẫn phóng viên đến van \x%l車掌;#00ffc040;trưởng tàu%l;#; ở phía cuối \x%l客車;#00ffc040;toa hành khách%l;#;,\ncô làm động tác như đang dùng tay kéo nó.
**Bản sửa:** Hướng dẫn phóng viên đến van trưởng tàu ở phía cuối toa hành khách,\ncô làm động tác như đang dùng tay kéo nó.
Lý do: Gỡ 2 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3366 — monologue — tag

JP: そのまま列車で折り返す者も、クマ川第四橋梁で、\nふかみ操るクマ川下り舟の真上を通過できる。
TW: 如果沒有參與漂流，而是直接乘坐當次列車返回，深美的漂流船會在隈河第四大橋下方與列車交會而過。
**VN cũ:** Những người cứ thế quay về bằng \x%l列車;#00ffc040;tàu%l;#;, tại cây cầu thứ tư trên sông Kuma,\ncũng có thể đi ngang qua ngay trên chiếc thuyền xuôi dòng do Fukami điều khiển.
**Bản sửa:** Những người cứ thế quay về bằng tàu, tại cây cầu thứ tư trên sông Kuma,\ncũng có thể đi ngang qua ngay trên chiếc thuyền xuôi dòng do Fukami điều khiển.
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3451 — monologue — tag

JP: キャブの中から、\n妙に尖った視線を感じる。
TW: 感覺駕駛室那邊似乎傳來了尖銳的視線。
**VN cũ:** Từ trong \x%lキャブ;#00ffc040;buồng lái%l;#;,\ntôi cũng cảm nhận được những ánh nhìn sắc lẹm kỳ lạ.
**Bản sửa:** Từ trong buồng lái,\ntôi cũng cảm nhận được những ánh nhìn sắc lẹm kỳ lạ.
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3458 — monologue — terminology

JP: 僕らの御一夜鉄道も、昨年ようやく、\n千内まわりでの、みかん鉄道との接続を持てた。
TW: 我們御一夜鐵路也終於在去年，跟川內的橙鐵路連上了。
**VN cũ:** Đường sắt Ohito của chúng ta, năm ngoái cũng đã,\ncuối cùng có thể kết nối với Đường sắt Mikan qua ngõ Sendai.
**Bản sửa:** Đường sắt Ohitoyo của chúng ta, năm ngoái cũng đã,\ncuối cùng có thể kết nối với Đường sắt Mikan qua ngõ Sendai.
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt)

### 3504 — monologue — terminology

JP: その向こうには、まだ見ぬ御一夜鉄道のファンが、\nきっと数多く、興味深く僕らを眺めるのだろうから。
TW: 我面對的更是許許多多潛在的御一夜鐵路愛好者。他們肯定會饒有興致地打量我們。
**VN cũ:** Bởi vì ở phía bên kia, chắc chắn có rất nhiều người hâm mộ Đường sắt Ohito chưa từng gặp mặt,\nđang nhìn chúng tôi với vẻ đầy hứng thú.
**Bản sửa:** Bởi vì ở phía bên kia, chắc chắn có rất nhiều người hâm mộ Đường sắt Ohitoyo chưa từng gặp mặt,\nđang nhìn chúng tôi với vẻ đầy hứng thú.
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt)

### 3520 — monologue — tag

JP: ならばと、口を真一文字に引き締める。\n運転台からホームへと下り――
TW: 於是，我緊閉著嘴，走下駕駛台，來到站台。
**VN cũ:** Nghĩ vậy, tôi mím chặt môi thành một đường thẳng.\nBước từ \x%l運転台;#00ffc040;buồng lái%l;#; xuống sân ga――
**Bản sửa:** Nghĩ vậy, tôi mím chặt môi thành một đường thẳng.\nBước từ buồng lái xuống sân ga――
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3530 — monologue — tag

JP: 炭水車正面の手ブレーキをぐるぐると回しつつ、\n日々姫は、苦笑の混じった声をだす。
TW: 日日姬一邊轉著煤水車前面的手剎，一邊苦笑著說道。
**VN cũ:** Vừa xoay tròn \x%l手ブレーキ;#00ffc040;phanh tay%l;#; ở mặt trước của \x%l炭水車;#00ffc040;toa tiếp than nước%l;#;,\nHibiki vừa cất giọng pha chút cười khổ.
**Bản sửa:** Vừa xoay tròn phanh tay ở mặt trước của toa tiếp than nước,\nHibiki vừa cất giọng pha chút cười khổ.
Lý do: Gỡ 2 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3532 — monologue — tag

JP: キャブの窓から首を出し、\n日々姫は客車の様子をうかがう。
TW: 日日姬從駕駛室的窗戶探出腦袋，看向車廂的方向。
**VN cũ:** Thò đầu ra khỏi cửa sổ \x%l運転台;#00ffc040;buồng lái%l;#;,\nHibiki dò xét tình hình \x%l客車;#00ffc040;toa hành khách%l;#;.
**Bản sửa:** Thò đầu ra khỏi cửa sổ buồng lái,\nHibiki dò xét tình hình toa hành khách.
Lý do: Gỡ 2 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3582 — monologue — tag

JP: またガチリ。ふかみは切り替えたポイントを戻し、\nレポーターをつれ、転車台の方へと消えていく。
TW: 深美將轉轍器拉回原位，帶著記者前往轉車台。
**VN cũ:** Lại nghe tiếng 'cạch'. Fukami đưa thanh ghi vừa bẻ về vị trí cũ,\ndẫn phóng viên đi và khuất dần về phía \x%l転車台;#00ffc040;bàn quay đầu máy%l;#;.
**Bản sửa:** Lại nghe tiếng 'cạch'. Fukami đưa thanh ghi vừa bẻ về vị trí cũ,\ndẫn phóng viên đi và khuất dần về phía bàn quay đầu máy.
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3620 — monologue — tag

JP: 客車から、れいなとポーレットも出てきてくれる。\n今まで様子を見守っていてくれたのだろう。
TW: 玲奈和波萊特也從車廂裡走了出來。看來她們一直在暗中觀察。
**VN cũ:** Reina và Paulette cũng bước ra từ \x%l客車;#00ffc040;toa hành khách%l;#;.\nChắc hẳn nãy giờ hai người đã đứng quan sát mọi chuyện.
**Bản sửa:** Reina và Paulette cũng bước ra từ toa hành khách.\nChắc hẳn nãy giờ hai người đã đứng quan sát mọi chuyện.
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3622 — monologue — terminology

JP: ふかみの接客技術はもはや、\n御一夜鉄道随一となったといって、過言ではない。
TW: 現在，深美的服務水平已經堪稱御一夜鐵路第一了。
**VN cũ:** Kỹ năng phục vụ khách hàng của Fukami giờ đây,\ncó thể nói là số một của Đường sắt Ohito cũng không ngoa.
**Bản sửa:** Kỹ năng phục vụ khách hàng của Fukami giờ đây,\ncó thể nói là số một của Đường sắt Ohitoyo cũng không ngoa.
Lý do: 御一夜 → "Ohitoyo" (quy tắc đã chốt)

### 3625 — monologue — tag

JP: ホームにこのまま停車するため、\n単弁を緩ブレーキ位置へと戻し、逆転機もミッドギアへと。
TW: 由於要直接停在站台，我將單剎拉回輕度剎車檔，將回動機拉至中位檔。
**VN cũ:** Để cứ thế đỗ lại ở sân ga,\ntôi đưa \x%l単弁;#00ffc040;van hãm đơn%l;#; về vị trí nhả phanh, và \x%l逆転機;#00ffc040;cần đảo chiều%l;#; về số trung tính.
**Bản sửa:** Để cứ thế đỗ lại ở sân ga,\ntôi đưa van hãm đơn về vị trí nhả phanh, và cần đảo chiều về số trung tính.
Lý do: Gỡ 2 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3687 — monologue — tag

JP: いいながら、車掌弁のお尻をふかみは示す。\n引き手の末端の木部の色は、鮮やかな赤だ。
TW: 說著，深美指了指列車長閥的底部。木質拉手的顏色是鮮艷的紅色。
**VN cũ:** Vừa nói, Fukami vừa chỉ vào phần đuôi của van \x%l車掌;#00ffc040;trưởng tàu%l;#;.\nMàu của phần gỗ ở cuối tay kéo là một màu đỏ rực rỡ.
**Bản sửa:** Vừa nói, Fukami vừa chỉ vào phần đuôi của van trưởng tàu.\nMàu của phần gỗ ở cuối tay kéo là một màu đỏ rực rỡ.
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

### 3701 — monologue — tag

JP: 客車の外から、凪が小声で呼びかけてくる。
TW: 車廂外面，凪小聲地跟我搭話。
**VN cũ:** Từ bên ngoài \x%l客車;#00ffc040;toa hành khách%l;#;, Nagi gọi khẽ.
**Bản sửa:** Từ bên ngoài toa hành khách, Nagi gọi khẽ.
Lý do: Gỡ 1 thẻ gloss %l do Gemini tự thêm (JP có 0 thẻ, bản sửa còn 0)

## Kết bài

File 凪ふかみ08b — Fukami epilogue (Fukami làm trưởng tàu, phóng viên phỏng vấn về "cắt cờ đỏ") — có **69/609 dòng sai (11,3%)**, thoại 48/372 (12,9%), độc thoại 21/237 (8,9%). Lỗi tập trung ở 3 nhóm hệ thống: (1) thẻ gloss %l do Gemini tự thêm — 41 dòng (34 dòng chỉ gỡ thẻ + 7 dòng gỡ thẻ kèm sửa thuật ngữ); (2) thuật ngữ — Ohitoyo 16, Teitetsu 2, Yunoi 2, Teiou 1, hoán đổi gloss 機関士/運転士 9; (3) SFX/gasp/meaning lẻ — ふぁっ → "Phà" 2 dòng, gasp sweep 2 dòng, Fukami tự sửa おにー→さん 1 dòng. Không có lỗi lệch dòng, chuỗi xoay, nhiễm chéo, dòng mồ côi hay dòng chưa dịch. Điểm đáng chú ý nhất của file này không phải 69 dòng sai mà là 31 bản sửa bị loại ở lượt soát 2 (§3): tiền đề "Fukami là chị lớn của Nagi" sai với JP — hai người bằng tuổi nhau (ふかみh2 key 1118), Nagi tự gọi cả ba là "bạn bè" (2254), TW gọi Fukami là 小深. Các bản đó giữ nguyên VN cũ và ghi lại đầy đủ để đợt thống nhất quyết sau.

### Khối TOML (đã kiểm chứng parse)

```toml
[script]
"1473" = "……Nguồn gốc thực sự của từ này là lá cờ mà trưởng tàu cầm."
"1967" = "「Không phải nhân viên cơ vụ, mà là người lái tàu ạ.\\nBởi vì thứ kéo toa hành khách này là 8620――đầu máy hơi nước.」"
"1982" = "「Không, hoàn toàn không có chuyện đó ạ.\\nHành khách của Đường sắt Ohitoyo, mọi người đều là những quý ông, quý bà cả.」"
"2047" = "「Ví dụ như. Người lái tàu ngất xỉu, Railord cũng không thể di chuyển.\\nTrong tình huống đó thì……tàu, sẽ ra sao ạ?」"
"2063" = "「Thực ra thì tôi. Từ khi trở thành trưởng tàu,\\nvẫn chưa một lần nào kéo van trưởng tàu cả.」"
"2095" = "「Điều khó khăn nhất trong nghiệp vụ trưởng tàu. Phải không ạ――」"
"2096" = "「Van trưởng tàu?」"
"2144" = "「Người lái tàu Migita.\\nTôi có thể hỏi anh vài câu được không?」"
"2156" = "「Fufu, được khen ngợi là vinh hạnh của tôi.\\nThực ra xuất thân của tôi là ở Teiou, Đế đô đấy ạ.」"
"2174" = "「Phà――」"
"2176" = "「Phà.」"
"2223" = "「A! Kéo van trưởng tàu――việc trưởng tàu làm cho tàu\\ndừng khẩn cấp, được gọi là 'cắt cờ đỏ' ạ.」"
"2228" = "「Ể~! Vậy sao. Thú vị quá.\\nKhông phải nhân viên cơ vụ, mà là người lái tàu.」"
"2238" = "「A, trước đó, 8620――\\nđầu máy hơi nước sẽ xoay đầu trên bàn quay đầu máy, rồi kết nối với toa hành khách ạ.」"
"2250" = "「Ư!!?」"
"2259" = "「Vâng. Nếu gọi là 'người lái tàu',\\nhọ sẽ nghĩ 'cô hiểu biết đấy', và chắc chắn sẽ rất vui.」"
"2280" = "「A, ra là vậy sao~! Nhưng mà như thế,\\nchứng tỏ Đường sắt Ohitoyo an toàn đến mức đó! Đúng không.」"
"2285" = "「Cần đảo chiều! Cài hết số lùi!\\n――Dồn toa! Tiến lên!!」"
"2287" = "「Dịch vụ fan hâm mộ (fan service) cũng là,\\ncông việc quan trọng của người lái tàu đấy ạ.」"
"2320" = "「Anh Soutetsu! Đèn tín hiệu dồn toa! Cho phép tiến lên rồi!」"
"2331" = "「Tuyệt quá……Một Railord xinh đẹp thế này.\\nKể cả ở Đế đô cũng――」"
"2405" = "「Là vậy đó」\\n「Hauuu～～Ư」"
"2407" = "「Cắt, cờ đỏ――\\nKéo mạnh cái van trưởng tàu đó?」"
"2411" = "「'Phải biết \\x%l入換;#00ffc040;dồn toa%l;#; thì mới là một trưởng tàu thực thụ'――\\nỞ Teitetsu, người ta cũng từng nói như vậy ạ.」"
"2421" = "「Nữ trưởng tàu xinh đẹp đáng tin cậy của Đường sắt Ohitoyo!\\nCô Hayase Fukami thực ra còn có một thân phận khác nữa!」"
"2424" = "「Ở Ohitoyo, có suối nước nóng mỹ nhân hay suối nước nóng mỹ nam gì không vậy?\\nGặp ai cũng thấy nét mặt đẹp cực kỳ luôn」"
"2436" = "「Chúc mừng nha! Anh Soutetsu, bé Fukami!」"
"2451" = "「Mình xen vào thì kỳ lắm, với lại, a!\\nVới lại! Cũng có thể liên quan đến việc quảng bá của Đường sắt Ohitoyo nữa.」"
"2454" = "「Anh cũng đồng ý. Chuyến đi này là đặc sản riêng của Đường sắt Ohitoyo.\\nMang tính độc đáo hoàn toàn, là một điểm nhấn lớn mà.」"
"2459" = "「Tôi là Railord chuyên dụng của đầu máy 8620 thuộc Đường sắt Ohitoyo,\\nvừa được ngài Soutetsu giới thiệu. Tôi là Hachiroku ạ.」"
"2522" = "「Ra là vậy……Ở Teitetsu chắc cũng có nhiều chuyến tàu đường dài, có vẻ cũng có những trường hợp trưởng tàu bắt buộc phải hướng dẫn dồn toa nhỉ.」"
"2527" = "「Vâng. Khi cảm thấy có chút nguy hiểm nào đó――\\nTrưởng tàu có nghĩa vụ phải cắt cờ đỏ ạ.」"
"2529" = "「Vâng. Toa hành khách BBQ được Đường sắt Ohitoyo tân trang lại,\\nOro31 27, có trang bị van trưởng tàu――」"
"2532" = "「Vâng. Vì không thể để sự an toàn bị tổn hại――\\nĐó trở thành nghĩa vụ mà trưởng tàu bắt buộc phải hoàn thành.」"
"2533" = "「Vâng. Từ toa hành khách đang chạy, không thể đi vào\\nbuồng lái của đầu máy 8620 được. Vì vậy, những lúc như thế」"
"2597" = "「Rắc rối chứ! Khó khăn lắm đường sắt mới có cơ hội phục sinh mạnh mẽ mà.\\nHơn nữa, nếu có khách đến Đường sắt Ohitoyo, thì dịch vụ xuôi dòng sông cũng sẽ.」"
"2613" = "「Lò hơi chuẩn bị xong chưa?」"
"2618" = "「Nói đơn giản thì, nó là phanh khẩn cấp. Nếu kéo cái này,\\ncó thể phớt lờ thao tác lái ở buồng lái và dừng tàu lại.」"
"2656" = "「Cũng nhờ ơn mọi người ạ. Đường sắt Ohitoyo từ khi khai trương đến nay,\\nchưa từng để xảy ra một vụ tai nạn nào gây thương tích cho hành khách.」"
"2658" = "「Cảm ơn rất nhiều~! Chỗ này OK chứ?\\nVậy, xin hãy đưa chúng tôi đến Yunoi nha~」"
"2675" = "「Không cần quan tâm đến nhân viên cơ vụ sao? Rốt cuộc là, tại sao lại vậy?」"
"2698" = "「Đây chính là người lái tàu Migita Soutetsu,\\ncủa chuyến tàu BBQ Đường sắt Ohitoyo, tàu Mokumoku Hachiroku!」"
"2717" = "「Và, tiếp theo nhé? Hôm nay, về đầu máy hơi nước,\\ntôi muốn nhờ anh giải thích một cách đơn giản được không」"
"2724" = "「Chuyện đó, Railord và phụ lái tàu của chiếc 8620 này sẽ lo.\\nHachiroku! Hibiki! Xuống đây đi.」"
"2732" = "「Vậy anh cũng vào buồng lái trước một bước đây.」"
"2735" = "「Vậy thì anh đi đây. ……Hachiroku.\\nLúc bước xuống khỏi buồng lái, có câu thoại nào nghe cho ngầu không?」"
"2754" = "「Anh Soutetsu……ngài Soutetsu.\\n――A――」"
"2761" = "「Nếu vậy, có phải cảm giác 'Dễ ợt!' không?\\nCông việc của trưởng tàu ấy, không ngờ lại」"
"2775" = "「Trưởng tàu Fukami của chuyến tàu BBQ, khi đến Yunoi,\\nsẽ ngay lập tức biến thành người chèo thuyền trên sông Kuma.」"
"3108" = "Hôm nay là một đội lớn với hai phụ lái tàu, nhưng không hề có sự hỗn loạn nào.\\nHibiki, Nagi, Hachiroku và tôi, tinh thần làm việc nhóm đã được hình thành."
"3146" = "Hình tượng một người lái tàu xứng đôi với Hachiroku――\\nĐó tuyệt đối không phải là một gã đàn ông nói nhiều liến thoắng."
"3210" = "Nagi và Fukami đứng ở phía sau, còn phóng viên và người quay phim\\nđang chực chờ xem có ai bước ra từ buồng lái không."
"3239" = "Vừa trở lại buồng lái, tôi đã bị Hibiki với vẻ mặt đầy tò mò tóm lấy."
"3261" = "Nhưng mà, đây là vấn đề liên quan đến việc quảng bá của Đường sắt Ohitoyo,\\nliệu tôi có nên tự ý từ chối hay không――"
"3295" = "Ừm. Chắc là câu trả lời tốt hơn là chỉ đơn thuần phủ nhận.\\nCũng quảng bá được cho suối nước nóng của Ohitoyo và Nhà tắm Tororyu-yu nữa."
"3338" = "Hướng dẫn phóng viên đến van trưởng tàu ở phía cuối toa hành khách,\\ncô làm động tác như đang dùng tay kéo nó."
"3366" = "Những người cứ thế quay về bằng tàu, tại cây cầu thứ tư trên sông Kuma,\\ncũng có thể đi ngang qua ngay trên chiếc thuyền xuôi dòng do Fukami điều khiển."
"3451" = "Từ trong buồng lái,\\ntôi cũng cảm nhận được những ánh nhìn sắc lẹm kỳ lạ."
"3458" = "Đường sắt Ohitoyo của chúng ta, năm ngoái cũng đã,\\ncuối cùng có thể kết nối với Đường sắt Mikan qua ngõ Sendai."
"3504" = "Bởi vì ở phía bên kia, chắc chắn có rất nhiều người hâm mộ Đường sắt Ohitoyo chưa từng gặp mặt,\\nđang nhìn chúng tôi với vẻ đầy hứng thú."
"3520" = "Nghĩ vậy, tôi mím chặt môi thành một đường thẳng.\\nBước từ buồng lái xuống sân ga――"
"3530" = "Vừa xoay tròn phanh tay ở mặt trước của toa tiếp than nước,\\nHibiki vừa cất giọng pha chút cười khổ."
"3532" = "Thò đầu ra khỏi cửa sổ buồng lái,\\nHibiki dò xét tình hình toa hành khách."
"3582" = "Lại nghe tiếng 'cạch'. Fukami đưa thanh ghi vừa bẻ về vị trí cũ,\\ndẫn phóng viên đi và khuất dần về phía bàn quay đầu máy."
"3620" = "Reina và Paulette cũng bước ra từ toa hành khách.\\nChắc hẳn nãy giờ hai người đã đứng quan sát mọi chuyện."
"3622" = "Kỹ năng phục vụ khách hàng của Fukami giờ đây,\\ncó thể nói là số một của Đường sắt Ohitoyo cũng không ngoa."
"3625" = "Để cứ thế đỗ lại ở sân ga,\\ntôi đưa van hãm đơn về vị trí nhả phanh, và cần đảo chiều về số trung tính."
"3687" = "Vừa nói, Fukami vừa chỉ vào phần đuôi của van trưởng tàu.\\nMàu của phần gỗ ở cuối tay kéo là một màu đỏ rực rỡ."
"3701" = "Từ bên ngoài toa hành khách, Nagi gọi khẽ."
```

- Lượt soát 2: 100 tổng / 69 tái kiểm chứng / 31 loại bỏ / 0 sửa lại. JSON 69 khóa chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 69/69 (đối chiếu từ CSV3, không phải từ JSON fix-only của agent đầu tiên); khối TOML parse OK, 69 khóa, 0 sai lệch giá trị.
- Deliverables: `audit-nagifukami08b-REVIEW.md`, `audit-nagifukami08b-wrong.json` (69 mục, key dạng chuỗi, đủ jp/tw/old_vn/fix/kind/character — đã viết lại từ dạng fix-only `{key: fix}` của agent đầu tiên), `route-audit-snippet-nagifukami08b.md`.
