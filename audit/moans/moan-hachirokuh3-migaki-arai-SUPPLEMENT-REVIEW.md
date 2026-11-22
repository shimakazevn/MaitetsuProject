# Bổ sung moan-fix — ハチロクh3_磨き洗い.txt.toml (8 dòng sót từ bản nháp mồ côi)

## §0. Phạm vi và xác minh file

- File: `01_Hachiroku/ハチロクh3_磨き洗い.txt.toml` — 312 dòng, audit sai 44.
- TOML md5 `beac73e26039824c4868e4f3a22cc212` (khớp md5 trong REVIEW đã gộp), 312 khóa script, giá trị TOML khớp CSV3 (trừ quy tắc đã biết: TOML-2 dẹp literal `\n` thành khoảng trắng).
- CSV3: 1 bộ duy nhất, 312 dòng, 0 key trùng.
- Bản moan đã gộp: `moan-hachirokuh3-migaki-arai-wrong.json` 24 mục (đã parent-verified, gộp 58/1,399). 8 khóa trong nhiệm vụ này KHÔNG nằm trong 24 mục đó (đã kiểm tra bằng máy).
- Bản nháp mồ côi `moans/moan-hachiroku-h3-migaki-arai-wrong.json` (23 mục, không REVIEW, chưa gộp) chỉ dùng làm manh mối — giá trị fix của nó KHÔNG được tin mặc định (đã biết sai ở 1029 "Kuaaaaaa!" và 1063 14u; bản gộp "Kuaa Aaaa!" và 15u mới đúng). Mọi verdict dưới đây đều tự kiểm chứng từ JP + TW + quy tắc đã chốt.
- Kiểm tra sweep trực tiếp cho 8 khóa: 1007 `lost-gasp-whole`, 1039 `lost-gasp-whole`, 1066 `already-rendered`, 1106 `raw-tsu`, 1149 `raw-tsu`, 1678 `lost-gasp-whole` ×2 + `needs-file-audit` (xem §3 — 2 mục 1678 là lỗi của sweep).

## §1. Kết quả — 4 FIX, 4 KEEP

| Khóa | JP (âm rên) | VN cũ | Verdict | VN mới |
|---|---|---|---|---|
| 963 | んくっ | "ưm" | **FIX** | "Nku" |
| 1007 | ひゃうんっ！ | "Hya ưm!" | **FIX** | "Hyaun!" |
| 1039 | うあっ！ | "Ư a!" | **FIX** | "Ua!" |
| 1067 | んくっ―― | "Ưm——" | **FIX** | "Nku——" |
| 1066 | んううっ～っ | "Ưm ưm～" | KEEP | — |
| 1106 | んふっ!! (cuối dòng) | "ưm hưm!!" | KEEP | — |
| 1149 | ひぇ / んう / もっ | "Hye, ưm——ưm ư" | KEEP | — |
| 1678 | ああん (mô tả) | "A an" | KEEP | — |

Tổng sau file bổ sung này: 64 file / 1.512 dòng sai (moan) — cơ sở 64/1.508 + 4 dòng này (số file không đổi).

## §2. Các dòng FIX (4)

### 963 — んくっ → "Nku" (mất phụ âm k)

- JP: 「いえ――そういうわけでもございませんが――\nんくっ」 | TW: 「不是的——不過——嗯嗯」 | VN cũ: 「Không ạ——cũng không hẳn là vậy——\nưm」
- Nhân vật: ハチロク (Suzu, đang nói, kết bằng tiếng nghẹn ở cổ họng).
- Lỗi: んくっ = ん + く + っ — VN "ưm" chỉ giữ ん, làm mất hoàn toàn mora く. Tiền lệ đã gộp: 凪h1 1067 くっ→"Ku" (đối thoại), 1218 んきゅっ→"Nkyu" trong chính file này, 日々姫h4 んく→"Nku". Quy tắc "không để mất âm".
- Fix: 「Không ạ——cũng không hẳn là vậy——\nNku」 — chỉ đổi token rên cuối dòng; っ cuối trên moan romaji ngắn là ngầm hiểu (quy tắc 3b), không thêm "!".
- Đếm nguyên âm bằng máy: "Nku" có 1 u = JP く 1 u ✓.

### 1007 — ひゃうんっ！ → "Hyaun!" (diễn đạt trộn 2 hệ)

- JP: 「ひゃうんっ！」 | TW: 「呀嗯！」 | VN cũ: 「Hya ưm!」
- Nhân vật: ハチロク.
- Lỗi: ひゃうんっ là MỘT âm liền (ひゃ + う + ん + っ) nhưng VN cũ tách thành "Hya" (romaji) + "ưm" (tiếng Việt) — trộn 2 hệ diễn đạt trong một token, vi phạm quy tắc 3 (một dòng = một cách diễn đạt). Sweep cũng gắn cờ `lost-gasp-whole` cho dòng này (っ không được diễn đạt). Quy tắc 3b họ ひゃ → romaji.
- Fix: 「Hyaun!」 — Hepburn đầy đủ: ひゃ "Hya" + う "u" + ん "n", っ ngầm hiểu, "!" giữ từ JP.
- Đếm nguyên âm bằng máy: "Hyaun" có a=1, u=1 = JP ひゃ 1a + う 1u ✓. (Bản nháp mồ côi cũng đưa "Hyaun!" — trùng khớp độc lập, nhưng giá trị này tự suy ra từ JP.)
- Lưu ý: REVIEW đã gộp từng liệt 1007 vào mục "họ ひゃ đã romaji đúng" — nhận xét đó chỉ đúng cho phần ひゃ, không xét phần tách "ưm".

### 1039 — うあっ！ → "Ua!" (っ trên từ-âm bị mất)

- JP: 「うあっ！」 | TW: 「嗚啊！」 | VN cũ: 「Ư a!」
- Nhân vật: 双鉄H (Soutetsu).
- Lỗi: うあっ là từ-âm (sound-word) + っ. Quyết định đã chốt 20/11 (仲国05): っ gắn vào từ-âm LÀ gasp, phải được diễn đạt (tiền lệ "A――A――A――AƯ."). VN cũ "Ư a!" chỉ có "!" — dấu câu, không phải cách diễn đạt âm thanh — nên っ bị mất hoàn toàn. Sweep gắn cờ `lost-gasp-whole` cho dòng này, khớp với nhận định này. Tiền lệ rên ngắn 2 mora → romaji, っ ngầm hiểu: 凪h1 1054 いっ→"Í".
- Fix: 「Ua!」 — romaji đầy đủ: う "U" + あ "a", っ ngầm hiểu, "!" giữ từ JP. Không chọn "Ư aƯ!" (diễn đạt thuần Việt có Ư cho っ) vì nghe ngượng và có 2 Ư liền nhau; romaji sạch hơn và có tiền lệ.
- Đếm nguyên âm bằng máy: "Ua" có u=1, a=1 = JP う 1u + あ 1a ✓.
- Lưu ý: REVIEW đã gộp từng liệt 1039 vào mục "hơi thở ngắn đã đúng" — nhận xét đó bỏ sót cờ sweep và quy tắc 仲国05; verdict FIX này là sửa lại nhận xét đó, có bằng chứng.

### 1067 — んくっ―― → "Nku——" (mất phụ âm k)

- JP: 「んくっ――」 | TW: 「嗯嗯——」 | VN cũ: 「Ưm——」
- Nhân vật: 双鉄H (Soutetsu, tiếng nghẹn ngắn trong H-scene).
- Lỗi: giống hệt 963 — んくっ mất mora く trong VN "Ưm". Cùng tiền lệ như 963 (凪h1 1067 くっ→"Ku"; 1218 んきゅっ→"Nkyu"). TW 「嗯嗯」 cũng bỏ k, nhưng JP thắng TW khi xung đột.
- Fix: 「Nku——」 — giữ nguyên "――" từ VN cũ.
- Đếm nguyên âm bằng máy: "Nku" có 1 u = JP く 1 u ✓.
- Lưu ý: REVIEW đã gộp từng liệt 1067 vào mục "hơi thở ngắn đã đúng" — nhận xét đó sai ở chỗ không kiểm tra phụ âm k; verdict FIX này là sửa lại nhận xét đó.

## §3. Các dòng KEEP (4) — đã xét kỹ, không sửa

### 1066 — んううっ～っ → "Ưm ưm～" KEEP

- JP: 「んううっ～っ」 | TW: 「嗯嗚～」 | VN: 「Ưm ưm～」
- Không mất âm: ん→"Ưm", うう→"ưm", ～→"～". Đếm nguyên âm u bằng máy: VN có 2 nguyên âm u (Ư trong "Ưm" + ư trong "ưm") = JP 2 mora う ✓. Sweep gắn loại `already-rendered` (đã diễn đạt) — khớp. っ trong âm hơi thở này đã được diễn đạt qua cách đọc, không rơi vào trường hợp "mất hoàn toàn". VN "Ưm ưm～" tự nhiên, không ngượng — không đủ điều kiện áp romaji fallback. Bản nháp mồ côi đề xuất "Nuu～" — cũng diễn đạt đủ âm, nhưng không có quy tắc nào bắt buộc đổi một cách diễn đạt VN đúng sang romaji.
- REVIEW đã gộp giữ dòng này với cùng lý do — đồng ý.

### 1106 — raw っ đã sửa bởi audit; "ưm hưm!!" giữ nguyên KEEP

- JP (cuối dòng): ……子宮に、ちゅって、キス、して――くれ――んふっ！！ | TW: ……親一親我的子宮吧——呼！！ | VN CSV3: 「Quy đầu, em thíchっ——……ưm hưm!!」
- Raw っ trong "em thíchっ" của CSV3 LÀ lỗi thật — nhưng audit đã sửa rồi: audit fix 1106 là 「Quy đầu, em thích——……ưm hưm!!」 (bỏ っ, không còn raw っ). Vì vậy không còn việc gì cho đợt moan ở đây.
- Phần rên còn lại んふっ→"ưm hưm!!": ん→"ưm", ふ→"hưm" (f→h là cách chuyển chuẩn sang tiếng Việt), "!!" diễn đạt độ ngắt của っ. Hai mora → hai nhịp, tự nhiên, không ngượng. Không áp romaji "Nfu!!" như bản nháp mồ côi đề xuất — không có cơ sở quy tắc (ふ ngắn, không thuộc họ fa/fu dài, không ngượng).
- Base old_vn cho dòng này (nếu có sửa) phải là giá trị audit, không phải CSV3 — ghi chú để đợt thống nhất khỏi nhầm.

### 1149 — audit đã sửa cả hai lỗi; "Hye" + "ưm ư" giữ nguyên KEEP

- JP: 「めったな――ことでは――ンッ――つかいま――\nひぇ、んっ――んう――ただ、どう、して、もっ――」 | TW: 「沒什麼——嗯——事情——會用上，嗯——嗚——只是，怎樣，也——」 | VN CSV3: 「Hiếm khi——lắm mới——ưm——dùng đến——\nHi a, ưm——ưm ư——chỉ khi, thế nào, cũng khôngっ——」
- CSV3 có 2 lỗi: "Hi a" (tách âm ひぇ) và raw っ cuối dòng ("khôngっ——"). Audit đã sửa CẢ HAI: audit fix 1149 là 「Hiếm khi——lắm mới——ưm——dùng đến——\nHye, ưm——ưm ư——chỉ khi, thế nào, cũng không——」. "Hye" là Hepburn đúng của ひぇ ✓. んう→"ưm ư" giữ đủ 2 mora ✓. もっ cuối dòng là っ nhấn mạnh gắn từ nội dung (も = "cũng"), không phải gasp — audit bỏ đúng.
- Bản nháp mồ côi đề xuất đổi "ưm ư"→"ưm" — SAI, làm mất mora う (んう có 2 mora, "ưm" chỉ còn 1). Không áp dụng.
- Không còn lỗi moan nào sau audit — KEEP.

### 1678 — ああん = 2 a, "A an" đúng số lượng KEEP (tiền đề "3 a" trong brief là SAI)

- JP (monologue mô tả): 'ああん、と、すずが大きく口を開いてみせる。' | TW: '鈴張大了嘴。' | VN: 'Suzu há to miệng, phát ra tiếng "A an".'
- **Đếm ký tự bằng máy: JP có đúng 2 chữ あ (あ, あ, ん) — KHÔNG phải 3 a như brief ghi.** "A an" có 2 nguyên âm a (A + a) = khớp chính xác JP. Bản nháp mồ côi đề xuất "Aaan" (3 a) là SAI — thêm 1 nguyên âm không có trong JP.
- Sweep gắn 3 cờ cho khóa này (`lost-gasp-whole` ×2, `needs-file-audit`) — cả 3 đều sai: JP ああん KHÔNG có っ nào, nên không thể có gasp bị mất. Đây là lỗi của sweep (kiểu như mục 1613 mang JP của khóa 1681) — ghi chú để khỏi ai "sửa" theo cờ sweep.
- Dấu cách trong "A an" là phong cách ngắt nhịp (tiền lệ 1034 "A a a a a a" đã gộp giữ nguyên phong cách cách khoảng) — không phải lỗi.
- KEEP, không sửa gì.

## §4. Cờ cho đợt thống nhất (không quyết ở đây)

- F-S1: 1007 và 1039 đều là trường hợp REVIEW đã gộp liệt vào mục "đã đúng" nhưng xét kỹ lại thì sai (1007 tách hệ diễn đạt, 1039 mất っ). Đợt thống nhất không cần làm gì thêm với 2 dòng này sau khi gộp bản bổ sung — chỉ ghi chú để khỏi ai revert theo REVIEW cũ.
- F-S2: 1066 "Ưm ưm～" vs "Nuu～" (bản nháp) — nếu đợt thống nhất muốn chuẩn hoá mọi hơi thở dài sang romaji thì xem lại; hiện tại giữ VN vì không ngượng, không mất âm.
- F-S3: 1106/1149 — giá trị hiện hành sau audit (không raw っ) là base đúng; đợt dựng TOML phải áp audit fix trước rồi mới áp moan fix (không có moan fix cho 2 dòng này).
- F-S4: sweep có mục sai cho 1678 (3 cờ trên JP không có っ) — sweep không phải nguồn đáng tin tuyệt đối; mỗi mục phải đối chiếu JP trước khi áp.

## §5. Lượt soát 2 (đọc lại toàn bộ fix so với JP)

- Tổng số fix: 4. Tái kiểm chứng: 4/4. Bỏ: 0. Sửa trong lượt soát 2: 0.
- Kiểm tra bằng máy (lượt 2): JSON 4 mục = khối TOML 4 khóa, 0 sai lệch; jp/tw/old_vn/character khớp CSV3 chính xác 4/4; diff mỗi fix chỉ chạm token rên (963 "ưm"→"Nku"; 1007 " ưm"→"un"; 1039 "Ư "→"U"; 1067 "Ưm"→"Nku"); đếm nguyên âm từng fix khớp mora JP (963/1067 "Nku" 1u; 1007 "Hyaun" a=1 u=1; 1039 "Ua" u=1 a=1); không có giá trị nào chứa newline thật (963 giữ literal `\n` dạng `\\n` trong khối TOML).
- Đọc lại bằng mắt lượt 2 (từng fix so JP): 963 んくっ→"Nku" ✓ (k khôi phục); 1007 ひゃうんっ→"Hyaun!" ✓ (một cách diễn đạt duy nhất, romaji); 1039 うあっ→"Ua!" ✓ (っ trên từ-âm được diễn đạt qua romaji, theo quy tắc 仲国05 + tiền lệ "Í"); 1067 んくっ→"Nku——" ✓ (k khôi phục, giữ "――").
- 4 dòng KEEP cũng đọc lại lượt 2: 1066 đủ 2 nguyên âm u + ～ giữ ✓; 1106 audit đã bỏ raw っ, "ưm hưm!!" đủ âm ✓; 1149 audit đã sửa "Hye" + bỏ raw っ, "ưm ư" đủ 2 mora ✓; 1678 JP chỉ có 2 あ, "A an" đúng ✓.

## Khối TOML (đã parse-check: 4 khóa, 0 sai lệch)

```toml
963 = "「Không ạ——cũng không hẳn là vậy——\\nNku」"
1007 = "「Hyaun!」"
1039 = "「Ua!」"
1067 = "「Nku——」"
```

Kết bài

- 8 dòng sót đã xét xong từng dòng với JP + TW + sweep + tiền lệ: 4 FIX (963, 1007, 1039, 1067 — đều là mất âm: k, tách hệ diễn đạt, っ trên từ-âm) và 4 KEEP (1066, 1106, 1149, 1678 — 2 dòng audit đã sửa xong, 1 dòng diễn đạt đủ âm, 1 dòng tiền đề brief đếm sai số a).
- 2 phát hiện ngoài phạm vi 8 dòng: (1) brief ghi 1678 "3 a" là sai — JP chỉ có 2 あ (đếm bằng máy), nên "A an" đúng và "Aaan" của bản nháp là sai; (2) sweep có 3 cờ sai cho 1678 trên JP không có っ.
- Lượt soát 2: 4/4 tái kiểm chứng, 0 bỏ, 0 sửa. JSON + khối TOML đã parse-check. Không chạm ROUTE-MOANS.md, file đã gộp, MEMORY.md, hay bản nháp mồ côi.
