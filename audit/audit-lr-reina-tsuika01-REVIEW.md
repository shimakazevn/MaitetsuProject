# Audit: 04_Reina lrれいな追加01 — はじめての冬.txt.toml

**Tệp TOML:** `04_Reina/lrれいな追加01_はじめての冬.txt.toml` — md5 `91bbc47d045eb6f41187c89c5fd5255d`, 71.437 byte, BOM + CRLF (666 CRLF, 0 LF-only), `[selections]` rỗng, **không có bản sao trùng** (chỉ 1 tệp lrれいな追加01 trong 227 tệp TOML; 1 copy theo audit-queue.json).

**Nội dung:** Mùa đông đầu tiên của Reina — Soutetsu và Reina ngồi sưởi sàn (ゆかだんぼ) ăn quýt, xem album ảnh cũ của bác Denjirou và cô Kayoko (thời mỏ than Katakami, lớp bổ túc ban đêm 夜学), bàn chuyện khóa tu dưỡng tân nương (花嫁修業) và nhờ chị Mayami làm giáo viên; Mayami ghé qua, mệt sau một ngày làm ở xưởng rượu.

## 1. Tổng quan

**15/322 dòng sai (4,7%)** — thoại 14/233 (6,0%), độc thoại 1/89 (1,1%). File dịch khá sạch; lỗi tập trung ở tiếng cười bị diễn thành tiếng rên (7/15) và đại từ Soutetsu (4/15).

Phân loại (15): SFX-tiếng cười 7 (977, 1111, 1168, 1170, 1174, 1177, 1178 — うふふ/うっふふ "Ư phu phu"→"Ufufu"), đại từ 4 (Soutetsu tự xưng "tôi"→"anh" với Reina 2: 975, 1285; "em"→"anh" 2: 1155, 1312), fa/fu 2 (1097 ふあぁーあ "Phu a~ a"→"Phùa~ a"; 1101 ふぁ "Phu a"→"Phà"), bịa thêm nghĩa 1 (1051 "những di sản quý giá"), thuật ngữ 1 (1594 "Đường sắt Ohito"→"Đường sắt Ohitoyo").

- Lệch dòng (misaligned): **0**. Chuỗi xoay (rotation chain): **0**. Tràn từ chương khác (contamination): **0**. Dòng mồ côi (orphan VN): **0**. Dòng chưa dịch: **0**. Trùng key: **0**. Dòng chưa chắc chắn (uncertain): **0**.

## 2. Kiểm tra nguồn và cấu trúc

- CSV3 bộ duy nhất: 322 dòng, section `script` toàn bộ, 0 key trùng, 0 VN trống. Dòng duy nhất VN==TW là 656 「……」 (dấu ba chấm, không phải chưa dịch).
- CSV3↔TOML: 322/322 key khớp; VN khớp tuyệt đối 124 dòng + 198 dòng chỉ khác ở chỗ TOML-2 gộp `\n` thành khoảng trắng (đã kiểm chứng cơ học: sau khi thay `\n` bằng khoảng trắng thì 0 khác biệt thực chất).
- Comment `# JP:` trong khối `[script]`: 322/322 khớp đúng JP CSV3.
- Thẻ %l: số lượng `%l` trong VN bằng đúng JP ở mọi dòng (0 dòng lệch); không có thẻ thiếu dấu `;` đóng, không có thẻ thừa. Không có っ thô trong VN.
- Sweep っ: **0 mục cho file này** — đã kiểm tra trực tiếp trong sweep-raw-gasp-wrong.json theo đúng tên file (không có mục nào; 1 kết quả khớp tên khi tìm mờ thuộc file Mayami lr真闇追加01 key 1657, không phải file này).
- TOML md5 91bbc47d045eb6f41187c89c5fd5255d, BOM + CRLF, `[selections]` rỗng, không bản sao trùng.

## 3. Lỗi sai (chi tiết 15 dòng)

### 3.1 Đại từ (4 dòng)

**975 — 双鉄 (Soutetsu nói với Reina) — "tôi"→"anh"**

- JP: 「僕がというより、僕らがだろうが――そうか。僕らの結婚が、きっかけの一つになったのだなぁ」
- TW: 「也不是我，其實是我們——也對，我們的婚事其實也是原因之一」
- Cũ: 「Nói là tôi thì đúng hơn là chúng ta chứ——vậy sao.\nViệc chúng ta kết hôn đã trở thành một trong những lý do nhỉ.」
- Mới: 「Nói là anh thì đúng hơn là chúng ta chứ——vậy sao.\nViệc chúng ta kết hôn đã trở thành một trong những lý do nhỉ.」
- Lý do: tự xưng số ít của Soutetsu với Reina là "anh" (quy tắc đã chốt; Reina đáp ngay ở 977). "Chúng ta" (僕ら) giữ nguyên — đại từ nhóm không theo quy tắc số ít.

**1155 — 双鉄 (Soutetsu nói với Reina) — "em"→"anh" (+ "Vâng"→"Ừm")**

- JP: 「うむ。甘すぎて、場をわきまえずに食べすぎてしまうところであった」
- TW: 「嗯，太甜了，一不小心就吃了太多」
- Cũ: 「Vâng. Ngọt quá,\nnên suýt chút nữa em đã ăn quá nhiều mà không biết giữ ý tứ.」
- Mới: 「Ừm. Ngọt quá,\nnên suýt chút nữa anh đã ăn quá nhiều mà không biết giữ ý tứ.」
- Lý do: người nói là Soutetsu (char=双鉄, kề 1153 và 1156 đều là Soutetsu), JP/TW đều không có đại từ — VN cũ tự thêm "em" làm đại từ tự xưng cho Soutetsu là sai; với Reina phải là "anh". "Vâng"→"Ừm" cho nhất quán với cách file này dịch うむ ở 1156/1160/1161 ("Ừm").

**1285 — 双鉄 (Soutetsu nói với Reina) — "tôi"→"anh"**

- JP: 「だな。畳敷き専用の床暖房を入れたとのことだ。僕も、帰ってきたときには驚いた」
- TW: 「是的，使用了榻榻米房間專用的地暖。我剛回來的時候也覺得很驚訝」
- Cũ: 「Đúng vậy. Nghe nói họ đã lắp hệ thống sưởi sàn chuyên dụng cho phòng trải chiếu tatami.\nLúc mới về, tôi cũng ngạc nhiên lắm.」
- Mới: 「Đúng vậy. Nghe nói họ đã lắp hệ thống sưởi sàn chuyên dụng cho phòng trải chiếu tatami.\nLúc mới về, anh cũng ngạc nhiên lắm.」
- Lý do: Soutetsu nói với Reina (1284 Reina hỏi, 1289 Reina đáp) — tự xưng "anh".

**1312 — 双鉄 (Soutetsu nói với Reina) — "Em"→"Anh"**

- JP: 「真闇姉に、たってのお願いがあるんだ」
- TW: 「有件事，我們想拜託你」
- Cũ: 「Em có một việc nhất định phải nhờ chị Mayami.」
- Mới: 「Anh có một việc nhất định phải nhờ chị Mayami.」
- Lý do: Soutetsu nói với Reina (1306 Reina gọi "そうてつさん"; 1318 "僕かられいなにお願いさせてくれ" — anh nói với Reina về việc nhờ Mayami; Mayami chưa vào cảnh — lần đầu lên tiếng ở 1387, Soutetsu chào chị ở 1362–1363) nên tự xưng "anh". Đại từ theo NGƯỜI NGHE, không theo người được nhắc tới.
- **Parent sửa 20/11 ~06:07:** bản agent "Tôi" SAI — agent áp quy tắc "tôi với Mayami" theo người được nhắc (真闇姉) thay vì người nghe (Reina). Bằng chứng: 1318 "僕かられいなにお願いさせてくれ" (anh xin phép hỏi Reina), 1306/1319 Reina đáp lời; Mayami chỉ xuất hiện từ 1362. Sửa "Tôi"→"Anh", giữ nguyên số lượng 15.

### 3.2 Tiếng cười bị diễn thành tiếng rên (7 dòng)

Quy tắc Hieu 19/11: tiếng cười (ふふっ/うふふ/んふふ) diễn thành tiếng cười, KHÔNG diễn thành tiếng rên ("Ư hự"/"Ư phu phu"). Cả 7 dòng đều là Reina/Mayami cười, VN cũ viết "Ư phu phu" (âm rên).

**977 — れいな — うふふぅ→"Ufufu~"**

- JP: 「ですねぇ。それに――うふふぅ。ゆかだんぼより、もっとぽかぽかあったかですねぇ、そうてつさんだんぼ」
- TW: 「也對。而且……嘿嘿，這裡坐著比地暖還暖，是不是可以叫雙鐵暖呢」
- Cũ: 「Đúng vậy ạ~. Với lại——ư phu phu~. Còn ấm áp hơn cả\nsưởi sàn nữa nha~, sưởi Soutetsu á~」
- Mới: 「Đúng vậy ạ~. Với lại——Ufufu~. Còn ấm áp hơn cả\nsưởi sàn nữa nha~, sưởi Soutetsu á~」
- Lý do: うふふぅ là tiếng cười của Reina (TW 嘿嘿); "sưởi Soutetsu" (そうてつさんだんぼ) giữ nguyên.

**1111 — 真闇 — うふふっ→"Ufufu"**

- JP: 「あらまぁ。うふふっ」
- TW: 「哎呀」
- Cũ: 「Trời đất. Ư phu phu.」
- Mới: 「Trời đất. Ufufu.」
- Lý do: Mayami cười (うふふっ), không phải rên.

**1168 — れいな — うふふぅ→"Ufufu~"**

- JP: 「うふふぅ。れいな、がんばっちゃいますねぇ」
- TW: 「嘻嘻，玲奈會努力的」
- Cũ: 「Ư phu phu~. Reina sẽ cố gắng hết mình nha~」
- Mới: 「Ufufu~. Reina sẽ cố gắng hết mình nha~」
- Lý do: như 977.

**1170 — れいな — うっふふぅ→"Uffufu~"**

- JP: 「うっふふぅ。ほんとうですねぇ。れいなおみかん、すっかり大好きになっちゃいましたぁ」
- TW: 「嘻嘻，確實。玲奈徹底喜歡上橘子了」
- Cũ: 「Ư phu phu~. Đúng vậy nha~.\nReina hoàn toàn thích mê quýt luôn rồi ạ~」
- Mới: 「Uffufu~. Đúng vậy nha~.\nReina hoàn toàn thích mê quýt luôn rồi ạ~」
- Lý do: như 977; giữ phụ âm đôi (っ) thành "Uffufu" để không mất âm.

**1174 — れいな — うふふぅ→"Ufufu~"**

- JP: 「うふふぅ。おねえちゃんのネットワークなら一番安心ですねぇ」
- TW: 「嘿嘿，姐姐的人際網肯定值得依賴」
- Cũ: 「Ư phu phu~.\nNếu là mạng lưới của chị Mayami thì an tâm nhất rồi nha~」
- Mới: 「Ufufu~.\nNếu là mạng lưới của chị Mayami thì an tâm nhất rồi nha~」
- Lý do: như 977.

**1177 — れいな — うふふぅ→"Ufufu~"**

- JP: 「うふふぅ。ですねぇ」
- TW: 「嘿嘿，是的」
- Cũ: 「Ư phu phu~. Đúng vậy nha~」
- Mới: 「Ufufu~. Đúng vậy nha~」
- Lý do: như 977.

**1178 — れいな — うふふぅ→"Ufufu~"**

- JP: 「うふふぅ。きっとそうですねぇ」
- TW: 「嘿嘿，肯定是的」
- Cũ: 「Ư phu phu~. Chắc chắn là vậy rồi nha~」
- Mới: 「Ufufu~. Chắc chắn là vậy rồi nha~」
- Lý do: như 977.

### 3.3 Fa/fu romanised (2 dòng)

Quy tắc đã chốt: ふぁ/ふあ → "phà"/"phùa", không romanisation (tiền lệ lr_凪h2: 38 dòng fa/fu).

**1097 — 真闇 — ふあぁーあ→"Phùa~ a"**

- JP: 「ふあぁーあ。疲れた疲れた」
- TW: 「呼，累死嘍累死嘍」
- Cũ: 「Phu a~ a. Mệt quá mệt quá.」
- Mới: 「Phùa~ a. Mệt quá mệt quá.」
- Lý do: Mayami ngáp dài sau một ngày làm việc (ふあぁーあ); "Phu a" là romanisation, theo quy tắc là "Phùa".

**1101 — れいな — ふぁ→"Phà"**

- JP: 「ふぁ」
- TW: 「哇」
- Cũ: 「Phu a.」
- Mới: 「Phà.」
- Lý do: như 1097; ふぁ đơn → "Phà".

### 3.4 Bịa thêm nghĩa (1 dòng)

**1051 — 双鉄 — "những di sản quý giá" (bịa)**

- JP: 「伝次郎さんは、たくさんを、れいなに伝え、そうして残してくださったのだな」
- TW: 「傳次郎爺爺教了你很多，也為你留下了很多啊」
- Cũ: 「Bác Denjirou đã truyền đạt rất nhiều điều cho Reina,\nvà để lại cho em những di sản quý giá nhỉ.」
- Mới: 「Bác Denjirou đã truyền đạt rất nhiều điều cho Reina,\nvà để lại cho em những điều đó nhỉ.」
- Lý do: JP chỉ nói "truyền đạt rất nhiều (たくさん) và để lại" — không có "di sản" (遺産) và không có "quý giá". VN cũ bịa thêm cả hai từ, kiểu bịa điển hình của Gemini.

### 3.5 Thuật ngữ (1 dòng)

**1594 — monologue — "Đường sắt Ohito"→"Đường sắt Ohitoyo"**

- JP: 「ポーレットの前。御一夜鉄道移籍前。硬上鉱山時代。素直に気になる。れいなをもっと知りたくなる。」
- TW: 「在波萊特之前，在來到御一夜鐵路前，在片上礦山鐵路時的駕駛員。我很好奇。我想更深入地了解玲奈。」
- Cũ: 「Trước thời của Paulette. Trước khi chuyển đến Đường sắt Ohito. Thời còn ở mỏ than Katakami.\nThực sự tôi rất tò mò. Tôi muốn biết nhiều hơn về Reina.」
- Mới: 「Trước thời của Paulette. Trước khi chuyển đến Đường sắt Ohitoyo. Thời còn ở mỏ than Katakami.\nThực sự tôi rất tò mò. Tôi muốn biết nhiều hơn về Reina.」
- Lý do: 御一夜 = "Ohitoyo" (đã chốt); "Ohito" là dạng cũ. Sửa trong đợt audit này theo tiền lệ file 凪ふかみ08b (sửa 16 dòng Ohito→Ohitoyo trong audit). Đây là lần "Ohito" duy nhất trong file.

## 4. Kiểm tra lệch dòng / chuỗi xoay / nhiễm chéo

- **Lệch dòng 0:** đã đọc toàn bộ 322 dòng đối chiếu JP + TW; không có dòng VN nào là lời thoại khác hẳn JP của nó. Hai dòng gần-bịa (1051 "di sản quý giá", 1541 "đáng yêu lắm" — xem §6.3) vẫn bám sát JP của chính dòng đó, không phải lệch dòng.
- **Chuỗi xoay 0:** không có cặp dòng nào mà bản dịch đúng nằm ở key sai trong file. Đã kiểm tra bằng cách tìm VN đúng của mỗi dòng sai trong cùng file trước khi dịch mới (theo bộ lọc chuỗi xoay): không dòng sai nào có bản dịch đúng ở key khác.
- **Nhiễm chéo 0:** 3 ca nhiễm đã biết toàn dự án (Hachiroku 12→夜の嵐, hearing→stove, obasan↔sleeper) không xuất hiện ở đây; không có VN nào trùng với dòng file khác.
- **Dòng mồ côi 0 / chưa dịch 0 / trùng key 0:** mọi VN đều có nguồn JP/TW tương ứng; không có VN trống; không có key trùng. Cặp VN trùng duy nhất là 1134 và 1450 đều là 「!」 — hai tiếng kêu ngắn giống nhau hợp lệ, không phải xoay dòng.
- **Không có dòng tiếng Trung chưa dịch:** dòng VN==TW duy nhất là 656 「……」.

## 5. Lượt soát 2

Đọc lại toàn bộ 15 bản sửa đối chiếu từng JP (bao gồm kiểm tra lại người nghe ở các dòng đại từ: 975/1285/1155/1312 nghe là Reina — kề 977/1289/1164/1318): **15 tổng / 15 tái kiểm chứng / 0 loại bỏ / 0 sửa lại**. Kiểm chứng cơ học: JSON 15 khóa chuỗi, đủ 7 trường (key, jp, tw, old_vn, fix, kind, character); khối TOML parse OK, 15 khóa, 0 sai lệch giá trị; diff-sanity 15/15 chỉ khác ở chỗ sửa có chủ đích (tỉ lệ tương đồng 0,71–0,99; thấp nhất 1101 vì cả dòng chỉ có một tiếng "Phu a."→"Phà."). Quét bổ sung sau lượt 1: toàn bộ dòng thoại của Soutetsu chứa "tôi"/"em" đã rà lại — các "em" còn lại đều là gọi Reina (đúng), không còn "tôi" tự xưng sai nào; toàn bộ "Ư phu phu"/"Phu a" trong file (9 chỗ) đều đã nằm trong 9 bản sửa SFX/fa-fu, không còn chỗ sót.

## 6. Ghi chú / phán đoán cần Hieu (không tự quyết)

- **6.1 Key 1008 — hoàn thiện câu cụt của JP, giữ nguyên.** JP 「……きちんとしなかった場合の夫婦は」 cụt ở は; VN 「……Vậy những cặp vợ chồng không tu dưỡng đàng hoàng thì sao?」 thêm "thì sao?" để thành câu hỏi. Đây là cách hoàn thiện tối thiểu một câu cụt, không bịa thêm nội dung — giữ nguyên, ghi chú để Hieu biết.
- **6.2 Key 1103 — ふわわわ giữ "Oa oa oa", không sửa.** JP 「ふわわわ。それはたいへんですねぇ」, TW 哇哇, VN 「Oa oa oa. Vậy thì vất vả lắm nhỉ~」. Âm ふ đầu là onset mềm của tiếng bối rối "fuwa wa wa"; TW cũng chỉ diễn "wa wa". Giữ nguyên theo TW.
- **6.3 Key 1541 — "đáng yêu lắm" hoàn thiện chỗ lửng, giữ nguyên.** JP 「小さなころのれいなはさぞや、と思ってしまい、苦笑する。」 lửng ở さぞや (không nói rõ tính từ); VN 「Tôi lỡ nghĩ đến cảnh Reina lúc nhỏ chắc hẳn sẽ đáng yêu lắm, rồi lại cười gượng.」 thêm "đáng yêu". Đây là cách đọc hợp lý của さぞや trong ngữ cảnh (tưởng tượng Reina lúc nhỏ + cười gượng), TW cũng để lửng ("會是什麼樣"). Giữ nguyên, ghi chú để Hieu biết.
- **6.4 Key 1130 — んふー giữ "Ưm phu~!", không sửa.** JP 「あーーーーん。はむっ――。………………。んふー！」, VN 「A~~~~. Am~——. ………………. Ưm phu~!」. んふー là tiếng thỏa mãn khi nếm (mùi/vị dầu diesel thượng hạng); "Ưm phu" diễn đủ âm mũi + phụ âm, không mất âm.
- **6.5 "Cha nuôi"/"mẹ nuôi" giữ nguyên (đúng theo quy tắc).** 649 義父 (TW 養父) → "cha nuôi"; 1747 義父も義母も (TW 養父養母) → "cha nuôi, mẹ nuôi". Theo brief: 義父/義母 được dịch "bố nuôi/mẹ nuôi" khi TW nói 養父/養母 — đúng cả hai dòng.
- **6.6 Các dòng đã kiểm tra và giữ nguyên (không tính sai):** 653 ハイオク/軽油 — VN "xăng chỉ số octane cao và dầu diesel" đúng theo JP (TW dịch sai "普通汽油" cho 軽油, không theo TW); 679 ロールバック → "khôi phục lại dữ liệu" chấp nhận được; 1008 xem §6.1; 1182/1241/1734 câu cụt JP — VN cũng cụt tương ứng, không bịa thêm; 1210 少等部 (JP viết 少, TW 小學) → "trường tiểu học" đúng nghĩa; 1397 正和貝石油 → "Dầu mỏ Showakai" + X-Power đúng ruby しょうわかいせきゆ; 1624 薄皮 → "lớp vỏ lụa" (màng mỏng của múi quýt) chấp nhận được; 1680 焦げ付く → "cháy bỏng" là ẩn dụ, giữ nguyên; 1543 真似び → "học hỏi bắt chước" đúng.

## 7. Mục chờ thống nhất (không tính vào 15 dòng sai)

- **Không có.** Đã quét toàn file: không còn dạng cũ nào khác — không có "Migita System", "Obata", "Yui", "Master Controller", "Suntetsu", "Đường sắt Hoàng gia", "Ohimitera", 宮司, hay "cô"→"em" nào cần thống nhất. Dạng "Ohito" duy nhất (1594) đã sửa thẳng trong audit này (§3.5).

## Kết bài

File lrれいな追加01 — "Mùa đông đầu tiên" — có **15/322 dòng sai (4,7%)**, thoại 14/233 (6,0%), độc thoại 1/89 (1,1%). File dịch khá sạch: không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi hay chưa dịch. Lỗi tập trung ở tiếng cười bị diễn thành tiếng rên (7/15 — うふふ/うっふふ của Reina và Mayami đều bị viết thành "Ư phu phu"), đại từ Soutetsu (4/15 — "tôi"/"em" sai với Reina), fa/fu romanised (2/15), bịa thêm nghĩa (1/15) và thuật ngữ Ohito (1/15). Lượt soát 2: 15 tổng / 15 tái kiểm chứng / 0 loại bỏ / 0 sửa lại. Không có phán đoán nào cần Hieu quyết — chỉ ghi chú 4 dòng giữ nguyên có hoàn thiện/bối rối nhẹ (§6.1–6.4) và 1 dòng Ohito đã sửa (§3.5).

### Khối TOML (đã kiểm chứng parse)

```toml
[script]
"975" = "「Nói là anh thì đúng hơn là chúng ta chứ——vậy sao.\\nViệc chúng ta kết hôn đã trở thành một trong những lý do nhỉ.」"
"977" = "「Đúng vậy ạ~. Với lại——Ufufu~. Còn ấm áp hơn cả\\nsưởi sàn nữa nha~, sưởi Soutetsu á~」"
"1051" = "「Bác Denjirou đã truyền đạt rất nhiều điều cho Reina,\\nvà để lại cho em những điều đó nhỉ.」"
"1097" = "「Phùa~ a. Mệt quá mệt quá.」"
"1101" = "「Phà.」"
"1111" = "「Trời đất. Ufufu.」"
"1155" = "「Ừm. Ngọt quá,\\nnên suýt chút nữa anh đã ăn quá nhiều mà không biết giữ ý tứ.」"
"1168" = "「Ufufu~. Reina sẽ cố gắng hết mình nha~」"
"1170" = "「Uffufu~. Đúng vậy nha~.\\nReina hoàn toàn thích mê quýt luôn rồi ạ~」"
"1174" = "「Ufufu~.\\nNếu là mạng lưới của chị Mayami thì an tâm nhất rồi nha~」"
"1177" = "「Ufufu~. Đúng vậy nha~」"
"1178" = "「Ufufu~. Chắc chắn là vậy rồi nha~」"
"1285" = "「Đúng vậy. Nghe nói họ đã lắp hệ thống sưởi sàn chuyên dụng cho phòng trải chiếu tatami.\\nLúc mới về, anh cũng ngạc nhiên lắm.」"
"1312" = "「Anh có một việc nhất định phải nhờ chị Mayami.」"
"1594" = "Trước thời của Paulette. Trước khi chuyển đến Đường sắt Ohitoyo. Thời còn ở mỏ than Katakami.\\nThực sự tôi rất tò mò. Tôi muốn biết nhiều hơn về Reina."
```
