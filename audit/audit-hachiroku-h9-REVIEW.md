# Audit ハチロクh9 — ハチロクh9_コノフクハキルコト.txt.toml

**Ngày kiểm toán:** 20/11/2026

**Tệp TOML:** `01_Hachiroku/ハチロクh9_コノフクハキルコト.txt.toml` — md5 `bcbf02a0308ddac5d5aca3ac1cd717ce`, 119.546 byte, BOM, CRLF (1.248 CRLF, 0 LF-only), `[selections]` rỗng, **không có bản sao trùng** (kiểm tra md5 toàn bộ 227 tệp TOML; queue ghi 1 copy).

**Nguồn CSV:** "Trang tính 3" — bộ hàng duy nhất `01_Hachiroku` (không có bẫy dual-set ở file này), 613 hàng `[script]`, key 1339–3520, 0 VN rỗng.

**Kết quả: 69/613 dòng sai (11,3%), 1 dòng chưa chắc chắn, 0 dòng lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo file.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| Xưng hô Soutetsu "anh"→"tôi" (quy tắc đã sửa 20/11) | 28 |
| Gasp っ trần trong VN (sweep raw-tsu, áp nguyên) | 23 |
| Thuật ngữ (御一夜→Ohitoyo 6, 帝鉄→Teitetsu 1) | 7 |
| Gasp っ bị mất (lost-gasp-trailing 4 + whole 1) | 5 |
| Sai nghĩa (meaning) | 4 |
| Gasp っ trần — っ nhấn mạnh cuối câu, bỏ っ (không thêm Ư) | 2 |
| **Tổng** | **69** |

Nhóm xưng hô (28): toàn bộ là Soutetsu tự xưng "anh" trong thoại/độc thoại với Hachiroku/Suzu — 1399, 1413 (độc thoại), 1883, 1933, 1940, 1958, 1975, 2074, 2205, 2294, 2306, 2323, 2324, 2325, 2328, 2342, 2345, 2348, 2357, 2389, 2435, 2447, 2467, 2494, 2572, 2574, 2576, 3174 (độc thoại). Đây là lỗi hệ thống duy nhất của file: Gemini dịch 僕 thành "anh" mặc định, trong khi quy tắc đã sửa 20/11 chốt Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu" 753× 双鉄様). Nhóm thuật ngữ (7): 1380, 2020, 2264, 2269, 2418, 2578 (御一夜→Ohitoyo) + 2258 (帝鉄→Teitetsu). Nhóm gasp (30): 23 raw-tsu áp nguyên từ sweep + 2 raw-tsu sửa khác sweep (2428, 2588 — っ nhấn mạnh, bỏ っ thay vì thêm Ư) + 5 lost-gasp (2625 whole; 2815, 3131, 3250, 3256 trailing). Sai nghĩa (4): 1362, 1889, 2455 (chuỗi 誇る), 2927 (chủ ngữ).

**Theo loại dòng:** thoại 63/372 sai (16,9%), độc thoại 6/241 sai (2,5%). **Theo nhân vật:** 双鉄 (Soutetsu) 32, ハチロク (Hachiroku) 31, monologue 6.

File này sạch về cấu trúc — 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng, 0 dòng mồ côi. Lỗi tập trung ở 2 lỗi hệ thống đã có quy tắc chốt (xưng hô Soutetsu với Hachiroku + gasp っ) và 6 dòng thuật ngữ Ohitoyo/Teitetsu cũ.

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục. TOML md5 `bcbf02a0308ddac5d5aca3ac1cd717ce`, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng trong 227 tệp (file này chỉ có 1 copy; 11 nhóm trùng md5 của dự án đều là file khác).

- **CSV vs TOML:** 613 key khớp tuyệt đối, **0 khác biệt giá trị** giữa CSV3 và TOML-2 (sau khi chuẩn hoá ký tự xuống dòng literal `\n`). CSV3 là bản chuẩn cho fix list. Comment `# JP:` trong `[script]` 613/613.

- **Sweep っ (gasp):** kiểm tra trực tiếp sweep-raw-gasp-wrong.json — file này CÓ 31 mục (25 raw-tsu, 1 lost-gasp-whole, 4 lost-gasp-trailing, 1 already-rendered). 28 mục áp nguyên đã kiểm chứng; 2 mục raw-tsu BỊ BÁC phần fix (2428, 2588 — xem §3.4); 1 mục already-rendered (2178: きゅくぅぅぅぅ～～～っ → "Ưm ưưưư~~~!!" đã diễn đúng, không sửa). Quét bổ sung toàn bộ dòng JP chứa っ: không còn gasp nào sweep bỏ sót — các っ còn lại đều là SFX đã diễn bằng từ khác (chụt/Phụt/Rầm…), っ nhấn mạnh gắn với từ (すずっ!, 双鉄様っ!, イクっ! — đúng là không thêm Ư), hoặc đã có Ư/ưm trong VN.

- **Thẻ %l:** JP 0 thẻ, VN 0 thẻ — không có thẻ %l nào trong file này. Thẻ ruby `[tên,1]` trên JP: 11 dòng (vd. 1894 [おんまえ,1]御前, 1909 [でもの,1]出物, 2070 [ひともじ,2]一文字グルグル, 2418 [ゆのい,1]湯医) — VN bỏ marker theo đúng lệ toàn dự án (furigana không mang sang VN); 2418 là bằng chứng cho "Yunoi" (furigana ゆのい trên 湯医, đã chốt).

- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng: 0), không có VN mồ côi (orphan: 0), không có key trùng (613 key duy nhất), không có hàng VN == TW (0).

- **Kiểm tra nhiễm chéo:** đối chiếu toàn bộ VN của file qua chỉ mục VN toàn dự án — chỉ 1 giá trị VN trùng JP khác nhau: 「Ưm」 cho cả 「むぅ」 (2470) lẫn 「む」 (2169) — đều là tiếng ậm ừ ngắn hợp lệ, không phải nhiễm chéo. 0 lần trùng VN trong file với JP khác nhau ngoài cặp này.

- **6 ứng cử viên mạnh của queue:** heuristic chỉ là giới hạn dưới — đọc toàn bộ 613 dòng tìm ra 69 dòng sai; 6 ứng cử viên đều nằm trong nhóm xưng hô/gasp (không dòng nào là lệch dòng).

## 3. Chi tiết từng dòng sai

Ký hiệu: ⏎ = ký tự xuống dòng dạng backslash-n trong JSON/TOML (game tự wrap, không dùng \n thật).

### 3.1. Xưng hô Soutetsu "anh"→"tôi" (28 dòng)

**1399 [双鉄]**
JP: 「…………大丈夫だ、すず。何事もない」
TW: 「……不要緊，鈴。我沒事」
Cũ: 「……Anh không sao đâu, Suzu. Không có chuyện gì đâu.」
Mới: 「……Tôi không sao đâu, Suzu. Không có chuyện gì đâu.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**1413 [双鉄]**
JP: 「……資料の山に圧倒されて、⏎どうも、気持ちまで埋めてしまっていたようだ」
TW: 「……我被資料大山壓倒，感覺心情都被埋在了山底」
Cũ: 「……Bị áp đảo bởi núi tài liệu,⏎có vẻ như đến cả tâm trạng của anh cũng bị chôn vùi theo rồi.」
Mới: 「……Bị áp đảo bởi núi tài liệu,⏎có vẻ như đến cả tâm trạng của tôi cũng bị chôn vùi theo rồi.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: trong độc thoại không có đối tượng, Soutetsu tự xưng "tôi" (chỉ độc thoại tự vấn cảm xúc mới dùng "mình"); bản cũ dùng "anh" là sai.

**1883 [双鉄]**
JP: 「い――や――僕がっ、んんっ――⏎騒がせてしまったせいだ」
TW: 「不對——是我，嗯嗯——不穩重的緣故」
Cũ: 「Kh——ông——là do anh, ưm——⏎đã làm ầm ĩ lên thôi.」
Mới: 「Kh——ông——là do tôi, ưm——⏎đã làm ầm ĩ lên thôi.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**1933 [双鉄]**
JP: 「大事なお前だ。当然守るし――⏎それにより僕が傷つけば、お前も傷つくと知っている」
TW: 「你是最寶貴的人，我當然要保護——而且如果我真受傷了，你也會心裡受傷的」
Cũ: 「Em là người quan trọng của anh mà. Đương nhiên anh phải bảo vệ em rồi——⏎Anh biết nếu anh bị thương, em cũng sẽ đau lòng.」
Mới: 「Em là người quan trọng của tôi mà. Đương nhiên tôi phải bảo vệ em rồi——⏎Tôi biết nếu tôi bị thương, em cũng sẽ đau lòng.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**1940 [双鉄]**
JP: 「僕とともに？」
TW: 「你跟我一起？」
Cũ: 「Cùng với anh sao?」
Mới: 「Cùng với tôi sao?」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**1958 [双鉄]**
JP: 「ハチロク。こちらの準備は整ったぞ」
TW: 「八六。我這邊準備好了」
Cũ: 「Hachiroku. Bên anh chuẩn bị xong rồi đấy.」
Mới: 「Hachiroku. Bên tôi chuẩn bị xong rồi đấy.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**1975 [双鉄]**
JP: 「なるほどな。それは大変にありがたい――では、⏎僕はその服を、汰斗さんの指示通りに破棄しよう」
TW: 「原來如此，那我就太感激了——那我就遵照汰斗老爺的命令，丟棄那套衣服」
Cũ: 「Ra là vậy. Thế thì thật đáng cảm kích——vậy thì,⏎anh sẽ vứt bỏ bộ trang phục này theo đúng chỉ thị của ông Taito.」
Mới: 「Ra là vậy. Thế thì thật đáng cảm kích——vậy thì,⏎tôi sẽ vứt bỏ bộ trang phục này theo đúng chỉ thị của ông Taito.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2074 [双鉄]**
JP: 「無様ではなく、かわいかった。⏎正直、その……僕は性的にを興奮した」
TW: 「哪有什麼露糗，你可愛極了。其實我都有點性衝動了……」
Cũ: 「Không hề khó coi đâu, em rất đáng yêu.⏎Thành thật mà nói, ừm……anh đã cảm thấy hưng phấn.」
Mới: 「Không hề khó coi đâu, em rất đáng yêu.⏎Thành thật mà nói, ừm……tôi đã cảm thấy hưng phấn.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2205 [双鉄]**
JP: 「僕の前では、着てくれるのか」
TW: 「在我面前就肯穿嗎」
Cũ: 「Em sẽ mặc nó, khi ở trước mặt anh sao?」
Mới: 「Em sẽ mặc nó, khi ở trước mặt tôi sao?」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2294 [双鉄]**
JP: 「僕が離れているときとて同じだろう。⏎ハチロクが制服を着乱しているのなど見たこともない」
TW: 「我不在你身邊的時候也一樣，就沒看到你穿亂過制服」
Cũ: 「Ngay cả khi anh không ở bên cạnh cũng vậy thôi.⏎Anh chưa từng thấy Hachiroku mặc đồng phục xộc xệch bao giờ.」
Mới: 「Ngay cả khi tôi không ở bên cạnh cũng vậy thôi.⏎Tôi chưa từng thấy Hachiroku mặc đồng phục xộc xệch bao giờ.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2306 [双鉄]**
JP: 「動転したのだ。言葉を正しく使えぬほどに。⏎僕以外の誰にも見せたくないと思ったがゆえ」
TW: 「我很慌，慌到語無倫次了。我只是不想讓其他任何人看到」
Cũ: 「Anh đã rất bối rối. Đến mức không thể sử dụng từ ngữ cho chính xác.⏎Vì anh không muốn ai khác ngoài anh nhìn thấy nó.」
Mới: 「Tôi đã rất bối rối. Đến mức không thể sử dụng từ ngữ cho chính xác.⏎Vì tôi không muốn ai khác ngoài tôi nhìn thấy nó.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2323 [双鉄]**
JP: 「僕の性的興奮を――⏎すず。お前に……僕の妻に、鎮めてほしい」
TW: 「我的性衝動——鈴，就請你——我的妻子，幫我平息吧」
Cũ: 「Sự hưng phấn tình dục của anh——⏎Suzu. Anh muốn em……vợ của anh, xoa dịu nó.」
Mới: 「Sự hưng phấn tình dục của tôi——⏎Suzu. Tôi muốn em……vợ của tôi, xoa dịu nó.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2324 [双鉄]**
JP: 「どれどれ、ふむ――」
TW: 「我看看，嗯——」
Cũ: 「Đâu để anh xem, hừm——」
Mới: 「Đâu để tôi xem, hừm——」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2325 [双鉄]**
JP: 「ポーレットには、僕の方から電話をしておく。⏎ハチロクも、なにか準備があれば整えておいてくれ」
TW: 「我給波萊特先打個電話。八六，你先坐下準備吧」
Cũ: 「Anh sẽ gọi điện báo cho Paulette.⏎Hachiroku cũng chuẩn bị những thứ cần thiết đi nhé.」
Mới: 「Tôi sẽ gọi điện báo cho Paulette.⏎Hachiroku cũng chuẩn bị những thứ cần thiết đi nhé.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2328 [双鉄]**
JP: 「僕は、お前の“わたくしごと”の一部であることを、⏎本当に嬉しく光栄に思う」
TW: 「我能成為你心裡的一部分，真是光榮極了」
Cũ: 「Anh cảm thấy thực sự vui và vinh dự,⏎khi được là một phần trong "chuyện cá nhân" của em.」
Mới: 「Tôi cảm thấy thực sự vui và vinh dự,⏎khi được là một phần trong "chuyện cá nhân" của em.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2342 [双鉄]**
JP: 「ゆえ、自分の身も大切にするさ。⏎が――今回の場合は、それ以前の部分で軽率だった」
TW: 「所以你也要愛護好自己。——不過這次你好像事先就有粗心大意吧」
Cũ: 「Vì thế, anh cũng sẽ trân trọng bản thân mình.⏎Nhưng——trong trường hợp này, anh đã bất cẩn từ trước đó rồi.」
Mới: 「Vì thế, tôi cũng sẽ trân trọng bản thân mình.⏎Nhưng——trong trường hợp này, tôi đã bất cẩn từ trước đó rồi.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2345 [双鉄]**
JP: 「それで、ハチロクは怒っていたのか。⏎僕に無様を晒したと、そう誤解してしまったが故」
TW: 「所以你才生氣的嗎？以為自己露糗了」
Cũ: 「Vậy ra, Hachiroku tức giận là vì thế sao.⏎Vì hiểu lầm rằng em đã phơi bày bộ dạng khó coi trước mặt anh.」
Mới: 「Vậy ra, Hachiroku tức giận là vì thế sao.⏎Vì hiểu lầm rằng em đã phơi bày bộ dạng khó coi trước mặt tôi.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2348 [双鉄]**
JP: 「ゆえ、疲労を回復するために――⏎熱量を、お互いに補給しあいたいのだが」
TW: 「所以為了恢復精力——我想跟你互相補充一下熱量」
Cũ: 「Vì vậy, để xua tan mệt mỏi——⏎Anh muốn chúng ta cùng nhau bổ sung nhiệt lượng.」
Mới: 「Vì vậy, để xua tan mệt mỏi——⏎Tôi muốn chúng ta cùng nhau bổ sung nhiệt lượng.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2357 [双鉄]**
JP: 「すまなかった」
TW: 「抱歉」
Cũ: 「Anh xin lỗi.」
Mới: 「Tôi xin lỗi.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2389 [双鉄]**
JP: 「ああ、いつもだ。それを僕はとても好ましく思い、⏎同時に、見習いたいとも感じている」
TW: 「是啊，一直都是。我非常喜歡這樣的你，同時也會學習你」
Cũ: 「Ừ, lúc nào cũng vậy. Anh rất thích điều đó ở em,⏎và đồng thời, anh cũng muốn học hỏi theo.」
Mới: 「Ừ, lúc nào cũng vậy. Tôi rất thích điều đó ở em,⏎và đồng thời, tôi cũng muốn học hỏi theo.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2435 [双鉄]**
JP: 「そんなことはなかろう。ハチロクもれいなも、⏎僕やポーレットの決定に大いに影響を及ぼしている」
TW: 「沒有那種事。八六和玲奈你們都很影響我和波萊特的決定」
Cũ: 「Làm gì có chuyện đó. Cả Hachiroku và Reina,⏎đều đang ảnh hưởng rất lớn đến quyết định của anh và Paulette đấy thôi.」
Mới: 「Làm gì có chuyện đó. Cả Hachiroku và Reina,⏎đều đang ảnh hưởng rất lớn đến quyết định của tôi và Paulette đấy thôi.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2447 [双鉄]**
JP: 「どんなときでも、お前と、僕だ」
TW: 「無論任何時候，你和我」
Cũ: 「Dù trong hoàn cảnh nào, cũng là em, và anh.」
Mới: 「Dù trong hoàn cảnh nào, cũng là em, và tôi.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2467 [双鉄]**
JP: 「かがみこみ、胸の先まで――服の奥までが見え。⏎僕は性的に興奮したゆえに、まずいと思った」
TW: 「看你趴下身子，隔著衣服就能看到你的胸口，我就有了色色的念頭。我感覺真糟糕」
Cũ: 「Khi em cúi người xuống, anh có thể nhìn thấy tận sâu bên trong áo——đến tận đầu ngực.⏎Anh đã cảm thấy hưng phấn, nên mới nghĩ là không ổn.」
Mới: 「Khi em cúi người xuống, tôi có thể nhìn thấy tận sâu bên trong áo——đến tận đầu ngực.⏎Tôi đã cảm thấy hưng phấn, nên mới nghĩ là không ổn.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2494 [双鉄]**
JP: 「正直言って、まったくやりたいことではない。⏎けれど――すまん。他に方法が思いつかない」
TW: 「老實說，我也不是完全不想做。但是——抱歉。我想不出其他方法」
Cũ: 「Thành thật mà nói, anh hoàn toàn không muốn làm thế chút nào.⏎Nhưng mà——xin lỗi. Anh không nghĩ ra cách nào khác.」
Mới: 「Thành thật mà nói, tôi hoàn toàn không muốn làm thế chút nào.⏎Nhưng mà——xin lỗi. Tôi không nghĩ ra cách nào khác.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2572 [双鉄]**
JP: 「それは嬉しい。⏎が――同じであるなら、些かの疲労もあるはずだ」
TW: 「那太好了。——不過正因為一樣，也會有些疲勞」
Cũ: 「Nghe vậy anh rất vui.⏎Nhưng——nếu cùng cảm nhận, thì chắc hẳn em cũng phải thấy đôi chút mệt mỏi chứ.」
Mới: 「Nghe vậy tôi rất vui.⏎Nhưng——nếu cùng cảm nhận, thì chắc hẳn em cũng phải thấy đôi chút mệt mỏi chứ.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2574 [双鉄]**
JP: 「なら貸してくれ。姿勢はそのまま、動かさず」
TW: 「那就借我一下，你保持這個姿勢別動」
Cũ: 「Vậy cho anh mượn. Giữ nguyên tư thế đó, đừng cử động nhé.」
Mới: 「Vậy cho tôi mượn. Giữ nguyên tư thế đó, đừng cử động nhé.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**2576 [双鉄]**
JP: 「ならば、そのときを楽しみに、⏎今は公私の公に励むか」
TW: 「那就把期待留到那時候，現在要把公事干好」
Cũ: 「Nếu vậy, anh sẽ mong chờ đến lúc đó,⏎còn bây giờ thì tập trung vào việc công thôi nhỉ.」
Mới: 「Nếu vậy, tôi sẽ mong chờ đến lúc đó,⏎còn bây giờ thì tập trung vào việc công thôi nhỉ.」
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: Soutetsu là "tôi" với Hachiroku (cô ấy gọi anh là "ngài Soutetsu"), không phải "anh". Đối tượng đã xác minh từ các dòng xung quanh: toàn bộ cảnh này Soutetsu nói với Hachiroku/Suzu.

**3174 [monologue]**
JP: 僕はお前を求めていると、⏎少女そのもののフリルの上から、強く伝える。
TW: 我渴求著你——隔著少女風情的褶邊，我向她傳達著這個訊號。
Cũ: Để truyền đạt mạnh mẽ rằng anh đang khao khát em,⏎xuyên qua lớp bèo nhún mang đậm vẻ thiếu nữ.
Mới: Để truyền đạt mạnh mẽ rằng tôi đang khao khát em,⏎xuyên qua lớp bèo nhún mang đậm vẻ thiếu nữ.
Lý do: Quy tắc xưng hô Soutetsu đã sửa 20/11: trong độc thoại không có đối tượng, Soutetsu tự xưng "tôi" (chỉ độc thoại tự vấn cảm xúc mới dùng "mình"); bản cũ dùng "anh" là sai.


### 3.2. Thuật ngữ (7 dòng)

**1380 [ハチロク]**
JP: 「『御一夜機関区機関車配置表』⏎――間違いございませんね」
TW: 「“御一夜機務段機車配置表”——沒有弄錯」
Cũ: 「"Bảng bố trí đầu máy Khu cơ vụ Ohimitera"⏎——Không sai vào đâu được.」
Mới: 「"Bảng bố trí đầu máy Khu cơ vụ Ohitoyo"⏎——Không sai vào đâu được.」
Lý do: Thuật ngữ đã chốt 19/11: 御一夜 = "Ohitoyo", không phải "Ohimitera"/"Ohito".

**2020 [ハチロク]**
JP: 「うふふっ――さて、お客様。本日は御一夜鉄道、⏎『特別[ビール,1]麦酒列車』へのご乗車、ありがとうございます」
TW: 「呵呵——客人。感謝您今天搭乘御一夜鐵路“特別啤酒列車”」
Cũ: 「Ufufu——Thưa quý khách. Cảm ơn quý khách đã lên chuyến⏎"Tàu bia đặc biệt" của Đường sắt Ohimitera ngày hôm nay ạ.」
Mới: 「Ufufu——Thưa quý khách. Cảm ơn quý khách đã lên chuyến⏎"Tàu bia đặc biệt" của Đường sắt Ohitoyo ngày hôm nay ạ.」
Lý do: Thuật ngữ đã chốt 19/11: 御一夜 = "Ohitoyo", không phải "Ohimitera"/"Ohito".

**2258 [ハチロク]**
JP: 「そのような営業努力があってはじめて、⏎[ていてつ,1]帝鉄の最盛期は、花開いたのです」
TW: 「就是靠這種行銷方式，才拉開了帝鐵光輝時期的序幕」
Cũ: 「Chính nhờ có những nỗ lực kinh doanh như vậy,⏎thời kỳ hoàng kim của Đường sắt Hoàng gia (Teitetsu) mới được nở rộ ạ.」
Mới: 「Chính nhờ có những nỗ lực kinh doanh như vậy,⏎thời kỳ hoàng kim của Teitetsu mới được nở rộ ạ.」
Lý do: Thuật ngữ đã chốt 19/11: 帝鉄 = "Teitetsu"; không dùng dạng đầy đủ "Đường sắt Hoàng gia" (dạng đầy đủ đúng nếu dùng là "Đường sắt Đế quốc", chỉ trong tooltip %l lần đầu).

**2264 [ハチロク]**
JP: 「ほんの数十年前には、まことに栄えていたのですね、⏎御一夜機関区は」
TW: 「幾十年前居然真的興隆過啊，御一夜機務段」
Cũ: 「Chỉ vài chục năm trước thôi, Khu cơ vụ Ohimitera⏎đã từng rất phồn vinh ngài nhỉ.」
Mới: 「Chỉ vài chục năm trước thôi, Khu cơ vụ Ohitoyo⏎đã từng rất phồn vinh ngài nhỉ.」
Lý do: Thuật ngữ đã chốt 19/11: 御一夜 = "Ohitoyo", không phải "Ohimitera"/"Ohito".

**2269 [ハチロク]**
JP: 「御一夜鉄道が例外――⏎特別というだけの話でございます」
TW: 「御一夜鐵路是例外——是特別的而已」
Cũ: 「Đường sắt Ohimitera là ngoại lệ——⏎Chỉ là một trường hợp đặc biệt thôi ạ.」
Mới: 「Đường sắt Ohitoyo là ngoại lệ——⏎Chỉ là một trường hợp đặc biệt thôi ạ.」
Lý do: Thuật ngữ đã chốt 19/11: 御一夜 = "Ohitoyo", không phải "Ohimitera"/"Ohito".

**2418 [ハチロク]**
JP: 「この列車は、御一夜発、[ゆのい,1]湯医行きです。湯医では、⏎ドアを開かぬ折返しとなり、下車はいただけません」
TW: 「本列車由御一夜開往湯醫，抵達湯醫就會直接折返，不會開啟車門，無法下車」
Cũ: 「Chuyến tàu này xuất phát từ Ohimitera, đi Yunoi. Tại Yunoi,⏎tàu sẽ quay đầu mà không mở cửa, nên quý khách không thể xuống tàu được ạ.」
Mới: 「Chuyến tàu này xuất phát từ Ohitoyo, đi Yunoi. Tại Yunoi,⏎tàu sẽ quay đầu mà không mở cửa, nên quý khách không thể xuống tàu được ạ.」
Lý do: Thuật ngữ đã chốt 19/11: 御一夜 = "Ohitoyo", không phải "Ohimitera"/"Ohito".

**2578 [双鉄]**
JP: 「ならば、そのようにしてみるか。[かいしゃ,4]御一夜鉄道の⏎業務終了後に、客車を一両使わせてもらって」
TW: 「那就這麼設定吧，就當作御一夜鐵路業務結束後，借用一輛客車」
Cũ: 「Nếu vậy, chúng ta thử làm thế xem sao. Sau khi Đường sắt Ohimitera⏎kết thúc giờ làm việc, chúng ta sẽ mượn một toa hành khách.」
Mới: 「Nếu vậy, chúng ta thử làm thế xem sao. Sau khi Đường sắt Ohitoyo⏎kết thúc giờ làm việc, chúng ta sẽ mượn một toa hành khách.」
Lý do: Thuật ngữ đã chốt 19/11: 御一夜 = "Ohitoyo", không phải "Ohimitera"/"Ohito".


### 3.3. Sai nghĩa (4 dòng)

**1362 [ハチロク]**
JP: 「――左様、ですね。⏎それではわたくし、双鉄様を、誇りましょう」
TW: 「——是啊，那我就誇獎您吧，雙鐵少爺」
Cũ: 「——Đúng là, như vậy nhỉ.⏎Vậy thì, em sẽ tự hào về Ngài Soutetsu.」
Mới: 「——Đúng là, như vậy nhỉ.⏎Vậy thì, em sẽ khen ngợi Ngài Soutetsu.」
Lý do: 誇る = khen ngợi, bị dịch thành "tự hào về" (đó là 誇りに思う). TW xác nhận: 誇獎 = khen ngợi. Dòng này nối với mảnh câu 2455 (cùng một câu 誇りましょう).

**1889 [ハチロク]**
JP: 「いえ――双鉄様。自分で申すのも悲しいのですが⏎……この胸ですよ？　その、人間の方々が好むのは」
TW: 「不會的，雙鐵少爺。說來難過的是……這樣的胸，哪有多少人類會喜歡呢」
Cũ: 「Không đâu——Ngài Soutetsu. Tự mình nói ra điều này cũng thật đáng buồn,⏎……nhưng ngực em thế này cơ mà? Chắc chắn, con người sẽ thích những bộ ngực」
Mới: 「Không đâu——Ngài Soutetsu. Tự mình nói ra điều này cũng thật đáng buồn,⏎……nhưng ngực em thế này cơ mà? Cái mà con người ta thích là…」
Lý do: JP bỏ lửng ở 「その、人間の方々が好むのは" ("cái mà con người ta thích là…"); TW diễn thành câu hỏi tu từ ("có bao nhiêu người sẽ thích bộ ngực thế này"). Bản cũ tự hoàn thiện câu theo hướng ngược lại ("Chắc chắn, con người sẽ thích…") — sửa về dạng bỏ lửng đúng JP.

**2455 [ハチロク]**
JP: 「わたくしを見つけ出してくださって、⏎世界一美しく花開かせてくださった、愛しいあなたを」
TW: 「發掘了我，讓世界第一美麗的花盛開的，是我心愛的您」
Cũ: 「Tự hào về người đã tìm ra em,⏎đã giúp em nở rộ thành bông hoa đẹp nhất thế gian, người em yêu dấu.」
Mới: 「Người đã tìm ra em,⏎đã giúp em nở rộ thành bông hoa đẹp nhất thế gian, người em yêu dấu.」
Lý do: Mảnh câu nối với 1362 (đối tượng của 誇りましょう). Bản cũ thêm động từ "Tự hào về" (sai động từ cho 誇る); sửa về dạng mảnh câu không động từ, đúng JP/TW.

**2927 [monologue]**
JP: 口内にまだこびりついている精液を、⏎指先で丁寧にぬぐいとる。
TW: 口內還黏著精液，她用指尖認真地擦掉。
Cũ: Tôi dùng đầu ngón tay cẩn thận lau đi vệt tinh dịch⏎vẫn còn vương lại trong khoang miệng cô ấy.
Mới: Cô ấy dùng đầu ngón tay cẩn thận lau đi vệt tinh dịch⏎vẫn còn vương lại trong khoang miệng.
Lý do: Chủ ngữ sai: TW xác nhận là Hachiroku tự lau (她用指尖…); JP không nêu chủ ngữ rõ nhưng TW làm chứng. Bản cũ đổi thành Soutetsu ("Tôi… trong khoang miệng cô ấy").


### 3.4. Gasp っ — sweep áp nguyên (28 dòng)

**1354 [ハチロク]**
JP: 「っ――」
TW: 「——」
Cũ: 「っ——」
Mới: 「Ư——」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**1868 [ハチロク]**
JP: 「どうか――いっしょに――せいえき、くだ、さいっ⏎わたくし――もう――んっ、げんかい、これ、もう！」
TW: 「一定要——跟我一起——對我射精，我——已經——嗯、到極限了！」
Cũ: 「Xin ngài——hãy cùng nhau——ban cho em, tinh dịchっ⏎Em——đã——ưm, đến giới hạn, rồi, sắp!」
Mới: 「Xin ngài——hãy cùng nhau——ban cho em, tinh dịchƯ Em——đã——ưm, đến giới hạn, rồi, sắp!」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**1896 [ハチロク]**
JP: 「がまん、いらない――ぴゅうって、して、してっ。⏎わたくし――だって――わたくし、もう、もうっ！」
TW: 「不需要忍耐——射、射進來，射進來。我——也——我，已經、已經——！」
Cũ: 「Không cần, nhịn đâu——bắn ra, bắn ra điっ.⏎Em——cũng——em, sắp, sắp rồi!」
Mới: 「Không cần, nhịn đâu——bắn ra, bắn ra điƯ. Em——cũng——em, sắp, sắp rồi!」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2017 [ハチロク]**
JP: 「やんっ――逃げては、いけませんっ――んっ――あ、⏎だめ――です――おちんちん――双鉄様、のっ」
TW: 「呀——不許逃跑——啊，不行——小雞雞——雙鐵少爺的」
Cũ: 「A——không được, trốn đâuっ——ưm——a,⏎không được——đâu ạ——dương vật——của ngài Soutetsuっ」
Mới: 「A——không được, trốn đâuƯ——ưm——a, không được——đâu ạ——dương vật——của ngài SoutetsuƯ」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2041 [ハチロク]**
JP: 「ひゅゅあ！！　あっ――はいった！　はいった、らっ⏎ん、あっ――だめっ――こし、わたくし、はしたないっ」
TW: 「咻啊！！啊——進來了！進來了，啊、嗯，啊——不行——我、我好下流」
Cũ: 「Hyuua!! A——vào rồi! Vào rồi, a⏎Ưm, a——không được——cái eo, em, lẳng lơ quáっ」
Mới: 「Hyuua!! A——vào rồi! Vào rồi, a Ưm, a——không được——cái eo, em, lẳng lơ quáƯ」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2046 [ハチロク]**
JP: 「はひっ！？　ひっ――しゅごっ――すご、いっ！⏎きゅふっ！　わた、く、し――おちん、ちん、にっ」
TW: 「咿！？咿——好棒——好棒啊！嗯呀！我——被小雞雞——」
Cũ: 「Hahi!? Hi——tuyệt quá——tuyệt, quá!⏎Kyuhu! Em——đang bị, dương vậtっ」
Mới: 「Hahi!? Hi——tuyệt quá——tuyệt, quá! Kyuhu! Em——đang bị, dương vậtƯ」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2055 [ハチロク]**
JP: 「はっ、はあっ――はあっ――はあっ――⏎おまん、まんの、奥っ――あと、もう、少し、で」
TW: 「哈，啊——啊——啊——小妹妹的，裡頭——還差一點點了」
Cũ: 「Hà, hà——hà——hà——⏎Sâu bên trong, cô béっ——chỉ còn, một chút, nữa thôi」
Mới: 「Hà, hà——hà——hà—— Sâu bên trong, cô béƯ——chỉ còn, một chút, nữa thôi」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2082 [ハチロク]**
JP: 「かっ――ふあ――だめっ――ですっ――ちか、らっ⏎もう――はいら、ないっ――からだ――ガク、って」
TW: 「啊——呼啊——不行——力氣已經——使不上了——身子——好僵」
Cũ: 「A——phù a——không được——đâu ạ——sức lực⏎không còn——nữa rồiっ——cơ thể——cứng đờ, mất rồi」
Mới: 「A——phù a——không được——đâu ạ——sức lực không còn——nữa rồiƯ——cơ thể——cứng đờ, mất rồi」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2086 [ハチロク]**
JP: 「あ――あっあっ――あああっ――双鉄、さまの、⏎わかり、ますっ――びくって、がまんっ――ん、あ」
TW: 「啊——啊啊——啊啊——雙鐵少爺的，我明白——您還在忍耐吧——嗯、啊」
Cũ: 「A——a a——a a a——của ngài Soutetsu,⏎em hiểu, rồiっ——đang giật giật, đang nhịnっ——ưm, a」
Mới: 「A——a a——a a a——của ngài Soutetsu, em hiểu, rồiƯ——đang giật giật, đang nhịnƯ——ưm, a」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2089 [ハチロク]**
JP: 「あ――はいっ、はいっ――さよう、ですね、⏎双鉄、さまっ――んっ――ふっ――ふあっ――あ」
TW: 「啊——是，是——這樣啊，雙鐵少爺——呼——呼啊——啊」
Cũ: 「A——vâng, vâng——đúng vậy, nhỉ,⏎Ngài Soutetsuっ——ưm——phù——phù a——a」
Mới: 「A——vâng, vâng——đúng vậy, nhỉ, Ngài SoutetsuƯ——ưm——phù——phù a——a」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2097 [ハチロク]**
JP: 「はぁあっ――あっ――きもち、い――あっ、おいし、⏎おいしいっ――ん――双鉄、さまの――おちん、ちん」
TW: 「啊啊——啊——好，舒服——啊，好吃，好吃——雙鐵少爺的——雞，雞」
Cũ: 「Hàa——a——sướng, quá——a, ngon,⏎ngon lắmっ——ưm——dương vật——của ngài Soutetsu」
Mới: 「Hàa——a——sướng, quá——a, ngon, ngon lắmƯ——ưm——dương vật——của ngài Soutetsu」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2106 [ハチロク]**
JP: 「は、ぅ……それ――は――双鉄、さまのっ――⏎おちん、ちんを――なで、なで――ん、して、るっ」
TW: 「啊嗚……就是——雙鐵少爺的——雞雞——在撫摸的——那裡」
Cũ: 「A, ư……Đó——là——nơi đang——⏎vuốt ve, vuốt ve——ưm, dương vật——của ngài Soutetsuっ」
Mới: 「A, ư……Đó——là——nơi đang—— vuốt ve, vuốt ve——ưm, dương vật——của ngài SoutetsuƯ」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2109 [ハチロク]**
JP: 「はぁ！　あ！　すきっ！　しゅき！　双鉄さまっ！⏎そうてつ、さまっ――ふ、あっ――だんな、さまっ」
TW: 「啊！啊！喜歡！捋來！雙鐵少爺！雙鐵少爺——呼，啊——夫君」
Cũ: 「Hà! A! Thích quá! Thích quá! Ngài Soutetsu!⏎Ngài Soutetsuっ——phù, a——phu quânっ」
Mới: 「Hà! A! Thích quá! Thích quá! Ngài Soutetsu! Ngài SoutetsuƯ——phù, a——phu quânƯ」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2144 [ハチロク]**
JP: 「んっ――ふっ――あっ――んっ、く――んうっ、⏎双鉄、さま――双鉄、さまの――おちん、ちんっ」
TW: 「嗯——呼——啊——嗯——嗚，雙鐵少爺——雙鐵少爺的——雞雞」
Cũ: 「Ưm——phù——a——ưm, ư——ưm ư,⏎Ngài Soutetsu——của ngài Soutetsu——dương vậtっ」
Mới: 「Ưm——phù——a——ưm, ư——ưm ư, Ngài Soutetsu——của ngài Soutetsu——dương vậtƯ」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2151 [ハチロク]**
JP: 「ん――よい、しょっ。双鉄様の、おおきくて――⏎ふ……あ……お窓から出すだけ――でもっ」
TW: 「嗯——好了。雙鐵少爺，您的好大——呼……啊……從小窗裡取出來就這麼——但是」
Cũ: 「Ưm——xong, rồi. Của ngài Soutetsu, to quá——⏎Phù……a……chỉ lấy ra từ cửa sổ thôi——mà cũngっ」
Mới: 「Ưm——xong, rồi. Của ngài Soutetsu, to quá—— Phù……a……chỉ lấy ra từ cửa sổ thôi——mà cũngƯ」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2176 [ハチロク]**
JP: 「んう――っ――」
TW: 「嗯嗚——」
Cũ: 「Ưm ư——っ——」
Mới: 「Ưm ư——Ư——」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2223 [ハチロク]**
JP: 「きゅうっ――んっ――あっ――あっ――ここ、好きっ、⏎おちんちん、ぺろって、おまん、まん――舐め、てっ」
TW: 「好緊——啊——啊——這裡，喜歡，小雞雞，舔到了，小妹妹的——」
Cũ: 「Kyuu——ưm——a——a——chỗ này, thích lắm,⏎dương vật, đang liếm, cô bé——của emっ」
Mới: 「Kyuu——ưm——a——a——chỗ này, thích lắm, dương vật, đang liếm, cô bé——của emƯ」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2251 [ハチロク]**
JP: 「おまん、まんっ――ン――いっぱい、いっぱい、⏎そうてつ、さま、に――つきあげ、られ、てっ――」
TW: 「小妹妹——嗯——好滿、滿噹噹的，被雙鐵少爺的——往上頂——」
Cũ: 「Cô bé——ưm——đang bị ngài Soutetsu——⏎đâm thốc lên——đầy ắp, đầy ắp rồiっ——」
Mới: 「Cô bé——ưm——đang bị ngài Soutetsu—— đâm thốc lên——đầy ắp, đầy ắp rồiƯ——」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2319 [ハチロク]**
JP: 「わた、くしの――おまん、まんっ――ふっ、あっ、⏎こん、なに――よだれ、たくさん――たら、してっ」
TW: 「我的——小妹妹——呼，啊，這麼多——涎水——淌了出來」
Cũ: 「Cô bé——của em——phù, a,⏎đang chảy——rất nhiều——nước dãi——thế nàyっ」
Mới: 「Cô bé——của em——phù, a, đang chảy——rất nhiều——nước dãi——thế nàyƯ」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2329 [ハチロク]**
JP: 「まい、――り。ます――ね？　双鉄、さまっ――⏎んっ――んうううううううっ！！！」
TW: 「我要——來了——哦？雙鐵少爺——嗯——嗯嗚——！！！」
Cũ: 「Em, sắp——ra. Rồi——nhé? Ngài Soutetsuっ——⏎Ưm——ưm ư ư ư ư ư ư ư!!!」
Mới: 「Em, sắp——ra. Rồi——nhé? Ngài SoutetsuƯ—— Ưm——ưm ư ư ư ư ư ư ư!!!」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2613 [ハチロク]**
JP: 「おちん――ちん――んっ。ふと、いっ――ふ、あっ、⏎ぼこっって、した――とこ――おまん、まん、にっ」
TW: 「雞——雞——嗯。好粗——呼，啊，粗粗的——部位——進了小妹妹」
Cũ: 「Dương vật——ưm. Thật to——phù, a,⏎phần——nhô ra——đã vào trong——cô bé, rồiっ」
Mới: 「Dương vật——ưm. Thật to——phù, a, phần——nhô ra——đã vào trong——cô bé, rồiƯ」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2614 [ハチロク]**
JP: 「おちん、ちん――双鉄、さま、のっ――⏎わたくし、の――おく――いちばん、おく、までっ」
TW: 「雞雞——雙鐵少爺的——插進我的——深處——最深的位置」
Cũ: 「Dương vật——của ngài Soutetsuっ——⏎đến tận——bên trong——sâu nhất, của emっ」
Mới: 「Dương vật——của ngài SoutetsuƯ—— đến tận——bên trong——sâu nhất, của emƯ」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2624 [双鉄]**
JP: 「っ！」
TW: 「！」
Cũ: 「っ!」
Mới: 「Ư!」
Lý do: Sweep っ: tiếng gasp っ trong JP còn sót nguyên dạng Nhật trong VN; diễn thành Ư theo quy tắc đã chốt (tiền lệ Hachiroku 12 再開発 2103/2537).

**2625 [双鉄]**
JP: 「っ！！！」
TW: 「！！！」
Cũ: 「!!!」
Mới: 「Ư!!!」
Lý do: Sweep: cả dòng JP chỉ là gasp っ + dấu chấm than; VN chỉ còn dấu chấm than — thêm Ư.

**2815 [monologue]**
JP: いかん、バランス――っ！！！？
TW: 不行，平衡要——！！！？
Cũ: Không xong rồi, mất thăng bằng——!!!?
Mới: Không xong rồi, mất thăng bằng——Ư!!!?
Lý do: Sweep: JP kết bằng gasp っ sau dấu gạch ngang; VN giữ gạch ngang nhưng mất gasp — thêm Ư sau gạch ngang.

**3131 [monologue]**
JP: 名を呼べば、すずは全身の力を抜いて、⏎僕に全てを預け――っ！？
TW: 我叫她的名字，她便全身脫力，把自己交給了我——！？
Cũ: Khi tôi gọi tên, Suzu buông lỏng toàn thân,⏎giao phó tất cả cho tôi——!?
Mới: Khi tôi gọi tên, Suzu buông lỏng toàn thân, giao phó tất cả cho tôi——Ư!?
Lý do: Sweep: JP kết bằng gasp っ sau dấu gạch ngang; VN giữ gạch ngang nhưng mất gasp — thêm Ư sau gạch ngang.

**3250 [monologue]**
JP: ハチロクの不安げな顔をほぐすため、⏎飲み慣れぬビールをさらにごくりと――っ！？
TW: 為了讓八六臉上不再那麼擔心，我更是一口悶了喝不習慣的啤酒——
Cũ: Để làm dịu vẻ mặt bất an của Hachiroku,⏎tôi lại ực thêm một ngụm bia vốn không quen uống——!?
Mới: Để làm dịu vẻ mặt bất an của Hachiroku, tôi lại ực thêm một ngụm bia vốn không quen uống——Ư!?
Lý do: Sweep: JP kết bằng gasp っ sau dấu gạch ngang; VN giữ gạch ngang nhưng mất gasp — thêm Ư sau gạch ngang.

**3256 [monologue]**
JP: 伝えたいことも、してやりたいことも――っ！
TW: 無論是想說的話，還是想讓她做的事——！
Cũ: Những điều muốn nói, những điều muốn làm cho em——!
Mới: Những điều muốn nói, những điều muốn làm cho em——Ư!
Lý do: Sweep: JP kết bằng gasp っ sau dấu gạch ngang; VN giữ gạch ngang nhưng mất gasp — thêm Ư sau gạch ngang.


### 3.5. Gasp っ — っ nhấn mạnh, bác fix sweep (2 dòng)

**2428 [双鉄]**
JP: 「望む――ところだっ」
TW: 「正合我意——」
Cũ: 「Đúng như――tôi mong muốnっ」
Mới: 「Đúng như――tôi mong muốn」
Lý do: っ cuối câu gắn với だ là っ NHẤN MẠNH, không phải gasp (tiền lệ mục 1474 sweep đã loại). Bản sweep đề xuất thêm Ư là SAI — sửa bằng cách bỏ っ trần khỏi VN, không thêm Ư.

**2588 [双鉄]**
JP: 「すず――いくぞっ」
TW: 「鈴——我要來了」
Cũ: 「Suzu——tôi ra đâyっ」
Mới: 「Suzu——tôi ra đây」
Lý do: っ cuối câu gắn với ぞ (いくぞっ) là っ NHẤN MẠNH, không phải gasp (tiền lệ mục 1474 sweep đã loại). Bản sweep đề xuất thêm Ư là SAI — sửa bằng cách bỏ っ trần khỏi VN, không thêm Ư.


## 4. Kiểm tra sweep và các mục đã xử lý

- Sweep có 31 mục cho file này: 25 raw-tsu + 1 lost-gasp-whole + 4 lost-gasp-trailing + 1 already-rendered (2178). Đã áp nguyên 28 mục sau khi kiểm chứng từng giá trị với JP; 2 mục raw-tsu bị bác phần fix (2428, 2588 — っ nhấn mạnh cuối câu, xem §3.5); 1 mục already-rendered giữ nguyên (2178).
- Quét bổ sung toàn bộ dòng JP chứa っ (ngoài sweep): không còn gasp nào bị sót. Các っ còn lại đều hợp lệ: SFX đã diễn bằng từ khác (chụt/Phụt/Rầm/Co thắt…), っ nhấn mạnh gắn với từ (すずっ!, 双鉄様っ!, イクっ!, すず, すず…), hoặc đã có Ư/ưm trong VN (1355 「く――あっ」→「Ư——a」, 1356, 2019 「きゃっ」→「Kya」, 2048, 2062, 2112, 3296 「腰を引きっ――」→「rút hông——」 — っ ngắt câu, giữ dấu gạch ngang là đủ).
- っ trong từ và SFX đã diễn (ぺろっ→"pero", ちゅっ→"chụt", ごくっ→"Ực") không thuộc diện sweep, giữ nguyên.

## 5. Lượt soát 2, phán đoán ghi chú và dòng chưa chắc chắn

Đọc lại toàn bộ 69 fix đối chiếu từng JP (+TW) lần thứ hai: **69 tổng / 69 tái kiểm chứng / 0 loại bỏ / 2 sửa lại** (2927 và 3174 — bản fix nháp vô tình thêm dấu 「」 vào 2 dòng độc thoại vốn không có ngoặc kép; đã bỏ). Kiểm tra cơ học (difflib): mọi fix chỉ khác VN cũ ở chỗ sửa có chủ đích, không có viết lại lớn (tỉ lệ tương đồng thấp nhất vẫn trên 0,5; các fix sweep 1 dòng gộp ký tự xuống dòng thành khoảng trắng theo đúng lệ fix 1 dòng). JSON 69 khóa chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 69/69; khối TOML parse OK, 69 khóa, 0 sai lệch giá trị.

- **Phán đoán ghi chú (giữ nguyên, không sửa):** 2053 — lời nói ngọng khi miệng đầy (らいふき→"dai suki", れふっ→"re hu") giữ nguyên dạng La-tinh vì đó là cách diễn âm ngọng, không phải lỗi rò rỉ ngoại ngữ (khác vụ rò tiếng Hàn ở file 12); 1410 — 正和十年代 dịch "những năm đầu thời Chính Hòa" giữ nguyên (chưa đủ rõ là sai để sửa); 1870 — "cùng nhau ra nhé" giữ nguyên (bổ sung ngữ cảnh trong cảnh H, TW không phản đối); 3274 — 被相続人 dịch "người thừa kế hợp pháp" giữ nguyên theo TW ("cả căn phòng do tôi thừa kế"), dù theo nghĩa đen 被相続人 là người đã khuất — đây là cách dùng lỏng của chính JP gốc, không phải lỗi VN.
- **Dòng chưa chắc chắn (1):** 2053 (nêu trên) — cách diễn lời ngọng bằng La-tinh hay phiên âm Việt ("đại sư kì") cần Hieu chốt nếu muốn đổi; hiện giữ nguyên.
- **Cần Hieu quyết (đã có trong danh sách chờ, không quyết thay):** phạm vi/timing đợt thống nhất (67 dòng Ohitoyo cũ trong các file đã audit — file này có 6 dòng Ohitoyo + 1 dòng Teitetsu sẽ thuộc đợt đó nếu Hieu muốn chuẩn hoá cả dạng cũ; riêng 2258 đã sửa về "Teitetsu" theo quyết định đã chốt 19/11).

## 6. Khối TOML (đã kiểm chứng parse)

Khối TOML dưới đây parse được bằng tomllib, **69 key, 0 sai lệch giá trị so với JSON**. Quy tắc ký tự xuống dòng: giá trị fix nào chứa ký tự xuống dòng dạng backslash-n (2 ký tự, như trong JSON và trong TOML gốc) thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON.

```toml
[script]
1354 = "「Ư——」"
1362 = "「——Đúng là, như vậy nhỉ.\\nVậy thì, em sẽ khen ngợi Ngài Soutetsu.」"
1380 = "「\"Bảng bố trí đầu máy Khu cơ vụ Ohitoyo\"\\n——Không sai vào đâu được.」"
1399 = "「……Tôi không sao đâu, Suzu. Không có chuyện gì đâu.」"
1413 = "「……Bị áp đảo bởi núi tài liệu,\\ncó vẻ như đến cả tâm trạng của tôi cũng bị chôn vùi theo rồi.」"
1868 = "「Xin ngài——hãy cùng nhau——ban cho em, tinh dịchƯ Em——đã——ưm, đến giới hạn, rồi, sắp!」"
1883 = "「Kh——ông——là do tôi, ưm——\\nđã làm ầm ĩ lên thôi.」"
1889 = "「Không đâu——Ngài Soutetsu. Tự mình nói ra điều này cũng thật đáng buồn,\\n……nhưng ngực em thế này cơ mà? Cái mà con người ta thích là…」"
1896 = "「Không cần, nhịn đâu——bắn ra, bắn ra điƯ. Em——cũng——em, sắp, sắp rồi!」"
1933 = "「Em là người quan trọng của tôi mà. Đương nhiên tôi phải bảo vệ em rồi——\\nTôi biết nếu tôi bị thương, em cũng sẽ đau lòng.」"
1940 = "「Cùng với tôi sao?」"
1958 = "「Hachiroku. Bên tôi chuẩn bị xong rồi đấy.」"
1975 = "「Ra là vậy. Thế thì thật đáng cảm kích——vậy thì,\\ntôi sẽ vứt bỏ bộ trang phục này theo đúng chỉ thị của ông Taito.」"
2017 = "「A——không được, trốn đâuƯ——ưm——a, không được——đâu ạ——dương vật——của ngài SoutetsuƯ」"
2020 = "「Ufufu——Thưa quý khách. Cảm ơn quý khách đã lên chuyến\\n\"Tàu bia đặc biệt\" của Đường sắt Ohitoyo ngày hôm nay ạ.」"
2041 = "「Hyuua!! A——vào rồi! Vào rồi, a Ưm, a——không được——cái eo, em, lẳng lơ quáƯ」"
2046 = "「Hahi!? Hi——tuyệt quá——tuyệt, quá! Kyuhu! Em——đang bị, dương vậtƯ」"
2055 = "「Hà, hà——hà——hà—— Sâu bên trong, cô béƯ——chỉ còn, một chút, nữa thôi」"
2074 = "「Không hề khó coi đâu, em rất đáng yêu.\\nThành thật mà nói, ừm……tôi đã cảm thấy hưng phấn.」"
2082 = "「A——phù a——không được——đâu ạ——sức lực không còn——nữa rồiƯ——cơ thể——cứng đờ, mất rồi」"
2086 = "「A——a a——a a a——của ngài Soutetsu, em hiểu, rồiƯ——đang giật giật, đang nhịnƯ——ưm, a」"
2089 = "「A——vâng, vâng——đúng vậy, nhỉ, Ngài SoutetsuƯ——ưm——phù——phù a——a」"
2097 = "「Hàa——a——sướng, quá——a, ngon, ngon lắmƯ——ưm——dương vật——của ngài Soutetsu」"
2106 = "「A, ư……Đó——là——nơi đang—— vuốt ve, vuốt ve——ưm, dương vật——của ngài SoutetsuƯ」"
2109 = "「Hà! A! Thích quá! Thích quá! Ngài Soutetsu! Ngài SoutetsuƯ——phù, a——phu quânƯ」"
2144 = "「Ưm——phù——a——ưm, ư——ưm ư, Ngài Soutetsu——của ngài Soutetsu——dương vậtƯ」"
2151 = "「Ưm——xong, rồi. Của ngài Soutetsu, to quá—— Phù……a……chỉ lấy ra từ cửa sổ thôi——mà cũngƯ」"
2176 = "「Ưm ư——Ư——」"
2205 = "「Em sẽ mặc nó, khi ở trước mặt tôi sao?」"
2223 = "「Kyuu——ưm——a——a——chỗ này, thích lắm, dương vật, đang liếm, cô bé——của emƯ」"
2251 = "「Cô bé——ưm——đang bị ngài Soutetsu—— đâm thốc lên——đầy ắp, đầy ắp rồiƯ——」"
2258 = "「Chính nhờ có những nỗ lực kinh doanh như vậy,\\nthời kỳ hoàng kim của Teitetsu mới được nở rộ ạ.」"
2264 = "「Chỉ vài chục năm trước thôi, Khu cơ vụ Ohitoyo\\nđã từng rất phồn vinh ngài nhỉ.」"
2269 = "「Đường sắt Ohitoyo là ngoại lệ——\\nChỉ là một trường hợp đặc biệt thôi ạ.」"
2294 = "「Ngay cả khi tôi không ở bên cạnh cũng vậy thôi.\\nTôi chưa từng thấy Hachiroku mặc đồng phục xộc xệch bao giờ.」"
2306 = "「Tôi đã rất bối rối. Đến mức không thể sử dụng từ ngữ cho chính xác.\\nVì tôi không muốn ai khác ngoài tôi nhìn thấy nó.」"
2319 = "「Cô bé——của em——phù, a, đang chảy——rất nhiều——nước dãi——thế nàyƯ」"
2323 = "「Sự hưng phấn tình dục của tôi——\\nSuzu. Tôi muốn em……vợ của tôi, xoa dịu nó.」"
2324 = "「Đâu để tôi xem, hừm——」"
2325 = "「Tôi sẽ gọi điện báo cho Paulette.\\nHachiroku cũng chuẩn bị những thứ cần thiết đi nhé.」"
2328 = "「Tôi cảm thấy thực sự vui và vinh dự,\\nkhi được là một phần trong \"chuyện cá nhân\" của em.」"
2329 = "「Em, sắp——ra. Rồi——nhé? Ngài SoutetsuƯ—— Ưm——ưm ư ư ư ư ư ư ư!!!」"
2342 = "「Vì thế, tôi cũng sẽ trân trọng bản thân mình.\\nNhưng——trong trường hợp này, tôi đã bất cẩn từ trước đó rồi.」"
2345 = "「Vậy ra, Hachiroku tức giận là vì thế sao.\\nVì hiểu lầm rằng em đã phơi bày bộ dạng khó coi trước mặt tôi.」"
2348 = "「Vì vậy, để xua tan mệt mỏi——\\nTôi muốn chúng ta cùng nhau bổ sung nhiệt lượng.」"
2357 = "「Tôi xin lỗi.」"
2389 = "「Ừ, lúc nào cũng vậy. Tôi rất thích điều đó ở em,\\nvà đồng thời, tôi cũng muốn học hỏi theo.」"
2418 = "「Chuyến tàu này xuất phát từ Ohitoyo, đi Yunoi. Tại Yunoi,\\ntàu sẽ quay đầu mà không mở cửa, nên quý khách không thể xuống tàu được ạ.」"
2428 = "「Đúng như――tôi mong muốn」"
2435 = "「Làm gì có chuyện đó. Cả Hachiroku và Reina,\\nđều đang ảnh hưởng rất lớn đến quyết định của tôi và Paulette đấy thôi.」"
2447 = "「Dù trong hoàn cảnh nào, cũng là em, và tôi.」"
2455 = "「Người đã tìm ra em,\\nđã giúp em nở rộ thành bông hoa đẹp nhất thế gian, người em yêu dấu.」"
2467 = "「Khi em cúi người xuống, tôi có thể nhìn thấy tận sâu bên trong áo——đến tận đầu ngực.\\nTôi đã cảm thấy hưng phấn, nên mới nghĩ là không ổn.」"
2494 = "「Thành thật mà nói, tôi hoàn toàn không muốn làm thế chút nào.\\nNhưng mà——xin lỗi. Tôi không nghĩ ra cách nào khác.」"
2572 = "「Nghe vậy tôi rất vui.\\nNhưng——nếu cùng cảm nhận, thì chắc hẳn em cũng phải thấy đôi chút mệt mỏi chứ.」"
2574 = "「Vậy cho tôi mượn. Giữ nguyên tư thế đó, đừng cử động nhé.」"
2576 = "「Nếu vậy, tôi sẽ mong chờ đến lúc đó,\\ncòn bây giờ thì tập trung vào việc công thôi nhỉ.」"
2578 = "「Nếu vậy, chúng ta thử làm thế xem sao. Sau khi Đường sắt Ohitoyo\\nkết thúc giờ làm việc, chúng ta sẽ mượn một toa hành khách.」"
2588 = "「Suzu——tôi ra đây」"
2613 = "「Dương vật——ưm. Thật to——phù, a, phần——nhô ra——đã vào trong——cô bé, rồiƯ」"
2614 = "「Dương vật——của ngài SoutetsuƯ—— đến tận——bên trong——sâu nhất, của emƯ」"
2624 = "「Ư!」"
2625 = "「Ư!!!」"
2815 = "Không xong rồi, mất thăng bằng——Ư!!!?"
2927 = "Cô ấy dùng đầu ngón tay cẩn thận lau đi vệt tinh dịch\\nvẫn còn vương lại trong khoang miệng."
3131 = "Khi tôi gọi tên, Suzu buông lỏng toàn thân, giao phó tất cả cho tôi——Ư!?"
3174 = "Để truyền đạt mạnh mẽ rằng tôi đang khao khát em,\\nxuyên qua lớp bèo nhún mang đậm vẻ thiếu nữ."
3250 = "Để làm dịu vẻ mặt bất an của Hachiroku, tôi lại ực thêm một ngụm bia vốn không quen uống——Ư!?"
3256 = "Những điều muốn nói, những điều muốn làm cho em——Ư!"
```

## Kết bài

File ハチロクh9_コノフクハキルコト.txt.toml (613 dòng) đã đọc toàn bộ từng dòng đối chiếu JP + TW: **69 dòng sai (11,3%)**, 1 dòng chưa chắc chắn (2053 — lời ngọng diễn bằng La-tinh, giữ nguyên chờ Hieu chốt). Lỗi tập trung ở 2 lỗi hệ thống đã có quy tắc chốt: Soutetsu tự xưng "anh" với Hachiroku (28 dòng) và gasp っ trần/mất (30 dòng, trong đó 2 mục sweep bị bác vì っ nhấn mạnh) — đều sửa được tại chỗ — cộng 7 dòng thuật ngữ Ohitoyo/Teitetsu cũ và 4 dòng sai nghĩa (chuỗi 誇る 1362/2455, câu bỏ lửng 1889, chủ ngữ 2927). Không có lệch dòng, chuỗi xoay, nhiễm chéo, dòng chưa dịch hay key trùng. Sau file này, tổng cộng **79 file / 4.186 dòng sai** (cơ sở 78 file / 4.117 + 69 file này — cơ sở đã kiểm chứng lại với ROUTE-AUDIT.md trước khi viết, khớp với số parent giao).
