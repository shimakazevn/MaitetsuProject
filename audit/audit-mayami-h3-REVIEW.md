# Audit — 真闇h3_補習授業の廃校舎 (05_Mayami) — 15/710 (2,1%)

File: `真闇h3_補習授業の廃校舎.txt.toml` — route 05_Mayami, 710 dòng script.
Disk: `sources/toml2/translation_toml/05_Mayami/#U771f#U95c7h3_#U88dc#U7fd2#U6388#U696d#U306e#U5ec3#U6821#U820e.txt.toml` (tên file #U-escaped, đúng như trên đĩa).
Nội dung: H-scene 3 của Mayami (真闇) — "lớp học bổ túc ở dãy phòng học bỏ hoang": hai người đi khảo sát trường Jutsusen bỏ hoang, roleplay chuyến dã ngoại thời học sinh (Mayami vào vai "tiền bối dịu dàng", rồi thành cô giáo dạy kèm), Soutetsu thú nhận muốn "bộc lộ bản thân", rồi các cảnh sex explicit (vuốt ve ngực, oral, quan hệ), kết thúc bằng kế hoạch biến trường cũ thành khu nghỉ dưỡng cho thuê trọn gói một nhóm/ngày.
Nhân vật: monologue 301, 真闇 223, 双鉄 186.

Phương pháp: đọc toàn bộ 710 dòng theo từng hàng, đối chiếu JP + TW (CSV3), kiểm tra cơ học thêm (xem §3). TOML order == key order (số tăng dần); CSV3 order xáo trộn; cả hai đều KHÔNG phải story order (vd. key 37 là SFX giữa H-scene nhưng nằm đầu file) — người nghe/đại từ xác định theo nội dung và dòng kề trong luồng truyện, không theo key.

## §1. Kết quả

Sai: **15/710 (2,1%)**.

Phân loại (15):
- **raw-tsu (sweep)**: 2 (1554, 2694 — っ Nhật thô còn sót trong VN).
- **lost-gasp-whole (sweep)**: 3 (2889, 2890, 2891 — cả dòng chỉ là っ + dấu câu, VN mất Ư).
- **lost-gasp-trailing (sweep)**: 3 (3114, 3264, 3965 — っ cuối sau ――, VN giữ dấu mà mất Ư).
- **SFX**: 3 (2194, 2665 — tiếng cười うふふ bị nhét Ư gasp; 2323 — onomatopoeia くに、くに đọc sai thành "cứ, cứ").
- **mistranslation**: 1 (2444 — ぶつける → "va chạm").
- **word-order/omission**: 1 (2308 — đảo thứ tự + mất ひとの).
- **nuance**: 1 (2274 — いっぱい "đầy" → "sắp đầy").
- **fabrication**: 1 (2778 — thêm "à." hỏi, JP/TW đều không có).

Theo nhân vật: 真闇 8/223 (3,6%), 双鉄 4/186 (2,2%), monologue 3/301 (1,0%).

Không misaligned / không rotation / không contamination chéo file / không orphan / 0 untranslated / 0 duplicate key. File này sạch bất thường so với các file Mayami khác — không có chuỗi xoay, không có lỗi đại từ hệ thống: Soutetsu dùng "tôi" với Mayami xuyên suốt (kể cả khi phá vỡ roleplay: 2797, 2670, 2039), dùng "em" đúng lúc làm học sinh trong roleplay (2579, 2560, 2735, 2767, 2864); Mayami gọi Soutetsu "em" đúng vai chị lớn.

Sweep っ-gasp: 8 mục cho file này trong `sweep-raw-gasp-wrong.json` — đã kiểm chứng từng mục với JP và áp dụng cả 8, 0 mục bị loại (xem §2.1). Không còn gasp sót: đã quét toàn bộ dòng JP có っ — các っ cuối câu còn lại đều là emphatic っ gắn với từ (diễn bằng thanh điệu/dấu "!" trong VN, theo quy tắc không thêm Ư) hoặc đã được diễn thành âm (á/ưm/fua…); xem §3.

Strong candidates 6 → đọc toàn bộ tìm ra 15 sai: heuristic chỉ đếm được một phần (nó không thấy lỗi SFX/nghĩa/nuance).

## §2. Các lỗi và cách sửa

### §2.1. Gasp っ — 8 hàng (toàn bộ là mục sweep, đã kiểm chứng và áp dụng)

| Hàng | Nhân vật | JP | VN cũ | Fix |
|---|---|---|---|---|
| 1554 | 双鉄 | 「……っ」 | 「……っ」 | 「……Ư」 |
| 2694 | 真闇 | 「熱かと――っ――すごい、のっ――ふあ、あっ――あっ――おちん、ちん――おなか――ぜんぶうっ！」 | 「Nóng quá――っ――tuyệt, quá――fua, á――á――dương, vật――trong bụng――toàn bộ!」 | 「Nóng quá――Ư――tuyệt, quá――fua, á――á――dương, vật――trong bụng――toàn bộ!」 |
| 2889 | 双鉄 | 「っ！」 | 「!」 | 「Ư!」 |
| 2890 | 双鉄 | 「っ！！」 | 「!!」 | 「Ư!!」 |
| 2891 | 双鉄 | 「っ！！？」 | 「!!?」 | 「Ư!!?」 |
| 3114 | monologue | 「精液全部を、真闇姉に呑んでもらえ――っ！？」 | 「Toàn bộ tinh dịch, đều đã được chị Mayami nuốt trọn――!?」 | 「Toàn bộ tinh dịch, đều đã được chị Mayami nuốt trọn――Ư!?」 |
| 3264 | monologue | 「指が、ようやく、触ってくれるが、睾丸だ――っ！？。」 | 「Cuối cùng, ngón tay, cũng chịu chạm vào, nhưng lại là tinh hoàn――!?」 | 「Cuối cùng, ngón tay, cũng chịu chạm vào, nhưng lại là tinh hoàn――Ư!?」 |
| 3965 | monologue | 「亀頭全部を呑んで貰えて、それでも速度は上がらない。じわじわ、ずるずる、真闇姉の口へ埋没し――っ！？」 | 「Toàn bộ quy đầu đã được nuốt trọn, nhưng tốc độ vẫn không tăng lên. Cứ từ từ, chầm chậm, chìm dần vào trong miệng chị Mayami――!?」 | 「Toàn bộ quy đầu đã được nuốt trọn, nhưng tốc độ vẫn không tăng lên. Cứ từ từ, chầm chậm, chìm dần vào trong miệng chị Mayami――Ư!?」 |

Ghi chú 2694: chỉ sửa っ giữa dòng (raw-tsu) theo đúng mục sweep; っ cuối "ぜんぶうっ！" là emphatic っ gắn với từ (quy tắc: không thêm Ư), VN "toàn bộ!" đã diễn bằng dấu "!" — giữ nguyên.

### §2.2. SFX — 3 hàng

- **2194** — 真闇: JP 「うふふっ」; TW 「呵呵」; VN cũ: 「Ưfufu.」; Sửa: 「Ufufu.」 — うふふ là tiếng CƯỜI, không phải gasp; っ cuối chỉ là ngắt tiếng cười. Cùng JP うふふ ở 2195 đã dịch đúng "Ufufu", 2352 んふふ → "Ufufu" — 2194 viết "Ưfufu" là lệch chuẩn, nhét Ư gasp vào tiếng cười (tiền lệ h8: 4 dòng đã sửa từ gasp về cười).
- **2665** — 真闇: JP 「先、こされちゃったねぇ。うふふ、お熱いお熱い」; TW 「比我們還快一步啊。呵呵，真親熱真親熱」; VN cũ: 「Bị hớt tay trên mất rồi nhỉ.\nƯfufu, nồng nhiệt quá đi thôi.」; Sửa: 「Bị hớt tay trên mất rồi nhỉ.\nUfufu, nồng nhiệt quá đi thôi.」 — JP うふふ không có っ, càng không có gasp; "Ưfufu" sai như 2194.
- **2323** — 真闇: JP 「ん……や……ちくび――ンッ――くに、くに――そぎゃん、と――しつこく、され、たら――」; TW 「嗯……呀……乳頭――嗯――擠、擠――別那麼――一直揉啊揉的――」; VN cũ: 「Ưm……á……núm vú――ưn――cứ, cứ――\nbị trêu chọc――dai dẳng, như thế――」; Sửa: 「Ưm……á……núm vú――ưn――bóp, bóp――\nbị trêu chọc――dai dẳng, như thế――」 — くに、くに là onomatopoeia tiếng nhào nặn/bóp (TW: 擠、擠); VN "cứ, cứ" đọc nhầm thành từ "cứ" (cứ làm tiếp), mất hẳn âm thanh. Cùng âm くにっ ở key 37 đã dịch đúng "Bóp nhẹ".

### §2.3. Nghĩa / thứ tự từ / nuance / bịa — 4 hàng

- **2444** — 真闇 (mistranslation): JP 「よかよ？　ぜぇんぶ、ぶつけてくれて」; TW 「好啊，全部都射過來吧」; VN cũ: 「Được chứ? Cứ va chạm hết vào chị đi.」; Sửa: 「Được chứ? Cứ trút hết vào chị đi.」 — ぶつける = ném/húc/trút hết vào; "va chạm" (collide) sai nghĩa. Ngữ cảnh: Mayami đáp lại lời tỏ tình muốn "làm đàn ông chủ đạo" của Soutetsu — "cứ trút hết vào chị đi" (đem tất cả của em trút vào chị) mới đúng.
- **2308** — 真闇 (word-order + omission): JP 「うあ……どろっ、どろ――んっ――（すんっ、すん）ふぁ……双ちゃんの……おとこの……ひとの……匂い」; TW 「嗚啊……黏黏糊糊的――嗯――（嗅、嗅）哇……小雙……男孩子……的氣味」; VN cũ: 「Ưa……nhớt, nhớp nháp――ưm――（khịt, khịt）\nFua……mùi của……đàn ông……của……Sou-chan.」; Sửa: 「Ưa……nhớt, nhớp nháp――ưm――（khịt, khịt）\nFua……mùi của Sou-chan……mùi đàn ông……mùi của một con người.」 — JP tự sửa dần: "mùi của Sou-chan… mùi đàn ông… mùi của một con người"; VN cũ đảo ngược thứ tự (đàn ông trước Sou-chan) và mất hẳn ひとの. Fix giữ đúng trình tự tự sửa của JP.
- **2274** — 真闇 (nuance): JP 「あああっ！　そこっ――ゆっくり、いけん、のっ！いま、いまっ、おまんこ――いっぱい、やけんっ！」; TW 「啊啊啊！　那裡――慢慢地，嗯！快、快，射滿我的――小穴！」; VN cũ: 「A a a! Chỗ đó――chậm lại, không được, đâu!\nBây giờ, bây giờ, âm hộ――sắp đầy, mất rồi!」; Sửa: 「A a a! Chỗ đó――chậm lại, không được, đâu!\nBây giờ, bây giờ, âm hộ――đầy ắp, mất rồi!」 — いっぱい = đã đầy (trạng thái), không phải "sắp đầy".
- **2778** — 真闇 (fabrication): JP 「[じゅつせん,1]術仙廃炭鉱の文化・観光遺産としての再活用」; TW 「術仙廢煤礦改建為文化、旅遊遺產」; VN cũ: 「Tái sử dụng mỏ than Jutsusen bỏ hoang làm di sản văn hóa và du lịch à.」; Sửa: 「Tái sử dụng mỏ than Jutsusen bỏ hoang làm di sản văn hóa và du lịch.」 — JP/TW đều là câu trần thuật (tên đề án); VN thêm "à." biến thành câu hỏi, không có căn cứ.

## §3. Kiểm tra cơ học và các mục đã xác minh là ĐÚNG (giữ nguyên)

- CSV3: bộ duy nhất, 710 dòng, 0 key trùng, 0 VN trống; thư mục CSV `translation_toml\05_Mayami`.
- TOML: md5 `679f382102d8ec0738d3e2eb97494730`, BOM + CRLF, [selections] rỗng, không có file trùng md5 (1 bản sao duy nhất — kiểm tra toàn bộ `sources/toml2/`).
- TOML ↔ CSV3: 710 khóa script khớp tuyệt đối, 0 khóa thừa/thiếu; VN khớp tuyệt đối 282/710, 428 khác chỉ do TOML-2 làm phẳng literal `\n` thành khoảng trắng (đã kiểm chứng: chuẩn hoá `\n`/khoảng trắng thì khớp 710/710 — CSV3 là bản chuẩn cho fix list); comment # JP trong [script] 710/710 khớp CSV3 (3 "lệch" apparent là mục [characters] 3158/3603/3946, không phải script).
- Trùng VN ở 2 key: 3 cặp, đều hợp lệ — "「A――」" (2247/2268), "「A.」" (2300/2265) là cảm thán ngắn; "（Phập――）" (4015/3967) là cùng một SFX dùng lại cho 2 âm khác nhau (ずりゅっ―― / っ――プッ――), không phải lệch hàng.
- %l tag: file này KHÔNG có tag %l nào (0 dòng JP/VN chứa %l) — sạch.
- Đại từ đã kiểm chứng theo dòng kề: Soutetsu "tôi" với Mayami mọi trường hợp (độc thoại + đối thoại phá roleplay); "em" chỉ khi làm học sinh trong roleplay; Mayami gọi Soutetsu "em" đúng vai chị lớn; 2451 双鉄さん → "anh Soutetsu" là chuyển đổi CÓ CHỦ Ý (Mayami lần đầu gọi bằng họ + さん, thừa nhận Soutetsu là đàn ông) — giữ nguyên.
- 2758 và 1592: TW bịa/sai, VN theo đúng JP — giữ nguyên. 3281 火打ち石: VN thêm "cầu may" là chú giải văn hoá đúng (đánh đá lửa khi tiễn đi cầu may) — giữ nguyên.
- 2898 (nói ngọng vì miệng đầy): JP/TW/VN đều giữ dạng âm ngọng — giữ nguyên. 2878: thứ tự từ VN lộn xộn nhưng nghĩa vẫn đủ ("tinh dịch đang tiến vào trứng của chị") — giữ nguyên, không sửa.
- 2328: っ cuối "ねっとり、して、てっ" — VN "dính, nhớp nháp, quá": "quá" ở đây đọc được như cách diễn emphatic っ (nhấn mạnh), tương tự "quá" đầu câu cho やらし — GIỮ NGUYÊN, ghi vào §6 để Hieu quyết nếu muốn chuẩn hoá thành "――Ư".
- 3967 （っ――プッ――) → "（Phập――）": gasp っ đầu bị mất trong SFX, nhưng "Phập" đã diễn プッ; độ lỏng của SFX cho phép — giữ nguyên, ghi §6.
- 4016 （つうううっ）→ "（Trượt）": TW 呲 ủng hộ nghĩa trượt — giữ nguyên.
- 37 "(Bóp nhẹ）" ngoặc mở/đóng không khớp — JP gốc "(くにっ）" cũng vậy (lỗi phía JP) — cosmetic, không tính sai. 4039 ngoặc không đóng — JP gốc cũng không đóng — cosmetic. 1578 "……." thừa một chấm — cosmetic.
- 2469 頭取 → "Giám đốc": KHÔNG tính sai — toàn dự án chưa thống nhất 頭取 (共通11 dùng "tổng giám đốc", 共通14 dùng "Chủ tịch", ハチロク01/12 cũng dùng "Giám đốc") — đưa vào đợt thống nhất (§6).

## §4. Lượt soát 2 (đọc lại toàn bộ fix)

15/15 tái kiểm chứng, 0 bỏ, 0 sửa. Từng fix đọc lại với JP của chính hàng đó: 1554 (……っ → Ư), 2194/2665 (cười → Ufufu, khớp 2195/2352), 2274 (いっぱい = đầy), 2308 (trình tự Sou-chan → đàn ông → con người), 2323 (くに、くに = bóp), 2444 (ぶつける = trút), 2694 (chỉ sửa っ giữa dòng; っ cuối là emphatic), 2778 (bỏ "à."), 2889/2890/2891 (っ cả dòng → Ư), 3114/3264/3965 (――っ → ――Ư). Không fix nào bị loại hay sửa lại ở lượt 2.

## §5. Khối TOML (đã kiểm chứng parse)

```toml
"1554" = "「……Ư」"
"2194" = "「Ufufu.」"
"2274" = "「A a a! Chỗ đó――chậm lại, không được, đâu!\\nBây giờ, bây giờ, âm hộ――đầy ắp, mất rồi!」"
"2308" = "「Ưa……nhớt, nhớp nháp――ưm――（khịt, khịt）\\nFua……mùi của Sou-chan……mùi đàn ông……mùi của một con người.」"
"2323" = "「Ưm……á……núm vú――ưn――bóp, bóp――\\nbị trêu chọc――dai dẳng, như thế――」"
"2444" = "「Được chứ? Cứ trút hết vào chị đi.」"
"2665" = "「Bị hớt tay trên mất rồi nhỉ.\\nUfufu, nồng nhiệt quá đi thôi.」"
"2694" = "「Nóng quá――Ư――tuyệt, quá――fua, á――\\ná――dương, vật――trong bụng――toàn bộ!」"
"2778" = "「Tái sử dụng mỏ than Jutsusen bỏ hoang làm di sản văn hóa và du lịch.」"
"2889" = "「Ư!」"
"2890" = "「Ư!!」"
"2891" = "「Ư!!?」"
"3114" = "Toàn bộ tinh dịch, đều đã được chị Mayami nuốt trọn――Ư!?"
"3264" = "Cuối cùng, ngón tay,\\ncũng chịu chạm vào, nhưng lại là tinh hoàn――Ư!?"
"3965" = "Toàn bộ quy đầu đã được nuốt trọn, nhưng tốc độ vẫn không tăng lên.\\nCứ từ từ, chầm chậm, chìm dần vào trong miệng chị Mayami――Ư!?"
```

Kiểm chứng: khối parse được bằng tomllib, 15 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\\n` trong khối parse về đúng literal backslash-n của CSV3).

## §6. Ghi chú cho Hieu (cần quyết / chờ thống nhất — không tính sai trong audit này)

- Thống nhất "Ohito"/"Ohimitera" → "Ohitoyo" (1543, 2524, 2608 — dạng cũ, theo tiền lệ Hibiki 06/Grand02, fix trong đợt thống nhất).
- 帝大 → "Đại học Đế quốc" (3299 dùng "Đại học Hoàng gia" — dạng cũ, chờ đợt thống nhất).
- 頭取 → "Chủ tịch/Tổng giám đốc ngân hàng" (2469 dùng "Giám đốc" — toàn dự án chưa thống nhất; 共通11 dùng "tổng giám đốc", 共通14 dùng "Chủ tịch").
- Phán đoán ít chắc (giữ nguyên, chờ Hieu kiểm tra trong game): 2328 "dính, nhớp nháp, quá" (っ cuối diễn bằng "quá" hay nên thành "――Ư"); 3967 "（Phập――）" cho （っ――プッ――) (gasp đầu bị mất); 2878 thứ tự từ lộn xộn nhưng nghĩa đủ.
- 2451 "anh Soutetsu" cho 双鉄さん — chuyển đổi có chủ ý trong truyện (Mayami thừa nhận Soutetsu là đàn ông), giữ nguyên.

## Kết bài

File 真闇h3_補習授業の廃校舎: 710 dòng đã đọc hết, **15 dòng sai (2,1%)** — 8 gasp っ (toàn bộ từ sweep, áp dụng cả 8), 3 SFX, 1 dịch sai nghĩa, 1 đảo thứ tự + thiếu từ, 1 nuance, 1 bịa thêm. Không có chuỗi xoay, không lệch hàng, không lỗi đại từ hệ thống — đây là một trong những file sạch nhất của route Mayami. JSON 15 khóa chuỗi; khối TOML parse OK, 15 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 15/15; lượt soát 2: 15/15, 0 bỏ, 0 sửa.
