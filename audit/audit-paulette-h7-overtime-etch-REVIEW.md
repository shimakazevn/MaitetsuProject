# Audit: Paulette h7_残業エッチもyシャツで — 24 dòng Việt sai (đã đối chiếu JP + TW)

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa từng dòng: 326 dòng (độc thoại 174, Paulette 96, Soutetsu 56), đối chiếu JP + TW từ CSV3 và TOML-2.
- CSV vs TOML: 0 khác biệt thực chất; tập key bằng nhau (326); `[selections]` rỗng; thẻ `%l`: JP 0, VN 0 — **0 thẻ thiếu dấu `;` đóng**; không có key trùng; không có dòng VN trống; VN==TW 1 (562 `「…………」` — đúng, chỉ là dấu câu).
- md5: `6cd9aaebbdca88cdc9df37e560158f60` — không trùng với bất kỳ file nào trong 227 file TOML (không có bản sao; bản sửa áp dụng cho 1 file duy nhất).
- Đọc toàn bộ 326 dòng phát hiện 24 dòng sai. Rà soát chéo với sweep gasp っ và quét máy tính (pronoun sweep với `\n` chuẩn hoá trước, quét `\bchu\b`, quét mảnh La-tinh trong các dòng thở/SFX, kiểm tra VN trùng và chỉ số VN toàn dự án) bắt thêm các dòng ngoài lần đọc đầu.
- Rà soát chéo với sweep gasp っ: sweep có 10 mục trong file này — 6 bản sửa (1233, 1271, 1285, 1331, 1380, 1270), 3 already-rendered (879, 899, 896), 1 needs-file-audit (816). Audit xác nhận cùng giá trị cả 6 bản sửa của sweep; đồng ý 879 và 896 không cần sửa; 899 đồng ý về gasp nhưng sửa thêm lỗi きゃふ riêng; 816 audit tự giải quyết (xem chi tiết). Audit phát hiện thêm 1 gasp sweep BỎ SÓT (912: っ ở đầu dòng, 2 っ chỉ còn 1 Ư).
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ 24/24 bản sửa đối chiếu JP (đúng 24, 0 bị loại). Kiểm tra lần hai cũng xác nhận: không có bản sửa nào thừa hưởng lỗi xưng hô của dòng khác (không có dòng lệch vị trí), không có khoảng trắng thừa trước `\n`, không có dấu 。 thay cho dấu ., các âm thở ghép viết liền một từ ("Kyaphù", "Hyafu", "kíphúuuun"), không còn mảnh La-tinh sót ("chu", "phá") — lần quét "phá" ở 977 là dương tính giả ("phát đau").
- Quy ước bản sửa: bản sửa viết MỘT DÒNG (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công — theo quyết định 19/11 của Hieu (game tự ngắt dòng, `\n` thủ công không quan trọng). File TOML gốc cũng lưu các giá trị này một dòng với khoảng trắng, nên khối TOML dưới đây dán vào khớp đúng dạng đó.

## Kết luận về cơ chế lỗi

- Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương: file sạch về cấu trúc. Chỉ số VN trùng trong file (6 nhóm) đều hợp lệ — `「Ưm」` ×2 (859: JP `「んぷっ」`; 917: JP `「む」` — hai tiếng rên mũi khác nhau, cùng diễn "Ưm" là chấp nhận được); `「Ưm!」` ×2 (922: JP `「んっ！」`; 839: JP `「んくっ！」`); `（Phụt! Phụt! Phụt! Phụt!）` ×3 (1659, 1660, 1662 — ba đoạn xuất tinh, cùng SFX); `「Đúng vậy」` ×2 (976: JP `「だな」`; 979: JP `「そのとおりだ」`); `（Cộp!）` ×2 (1648: JP `（ごっ！）`; 1665: JP `（ごつっ！）`); `（Phập! Phập! Chụt! Chụt!）` ×2 (1649, 1650 — cùng mẫu SFX).
- Chỉ số VN toàn dự án: 41 dòng h7 có VN trùng với file khác, tất cả đều là câu ngắn/SFX chung (`「A」`, `「Ưm」`, `（Phụt!）`…) — không có dòng nào là tràn chương. Hai trùng đáng chú ý: 1684 `（Thọc sâu!!!）` trùng h6 1591 nhưng JP khác (h6 là `（ずんっ！！！）` ngắn — đúng ở đó; h7 là `（ずぶううううううううっ！）` dài — lỗi độ dài ở đây, xem 1684); 861 `「Ốp」` trùng h8 2179 (cùng JP `「おっと」` — lỗi tương tự còn chờ audit ở h8).
- Lỗi chủ đạo là thở gấp/SFX: 20/24 (gasp 8 + breath 6 + SFX 6) — cùng họ lỗi như h1–h6, nhưng file này sạch hơn hẳn về xưng hô (chỉ 3 dòng, so với 11–12 dòng ở h5/h6).
- Xưng hô: Soutetsu tự xưng "anh" chỉ 2 lần trong thoại (959, 969) — 4 lần "tôi" đúng; Paulette tự xưng "em" 15 lần, chỉ 1 lần "tôi" sai (977). "mình" trong độc thoại: 3 lần — tất cả đều đúng (1334 "chính mình", 1266 "tự mình", 1400 "mình tôi" — thành ngữ/phản thân).
- Bằng chứng mới cho quyết định đang chờ: file này NGHIÊNG VỀ "cô" — Soutetsu gọi Paulette "em" 1 lần (907) vs "cô" 5 lần (560, 953×2, 954, 1015) — lần đầu tiên một file h nghiêng về "cô" kể từ Paulette 02. Cộng dồn toàn dự án: **"em" 85 vs "cô" 48**. 御一夜 0 lần. Không có 湯医/帝鉄/コン trong file.
- **Đề xuất mới: quy tắc độ dài âm SFX** — âm dài trong JP (う kéo dài) phải được kéo dài tương ứng trong VN (tiền lệ trong file: 1700/1701 `ずぶう…`→"sâuuuuuuuu" 8 chữ u); 1684 và 1651 vi phạm.
- Ghi chú về 897: JP `「はうっ」` (không có "!") → VN "Hau" — KHÔNG sửa. Tiền lệ h5 826 là `はうっ！` (có "!") → "Hau!"; toàn dự án `はうっ` trần được dịch "Hau" 9 lần, "Hau!" 4 lần — "Hau" ở đây khớp đúng dấu câu JP.

### Ghi chú về các điểm sweep khác audit (816, 912, 899, 1380)

- 816: sweep ghi needs-file-audit vì "không đặt được gasp chắc chắn". Audit đọc ngữ nghĩa: JP đoạn 1 = `ひあっ！　あっ――めくれっ――んっ――ひっぱ――っ`, VN đoạn 1 = "Hya! A——bị lộn, ngược——ưm——bị kéo, ra——" — các đoạn khớp nhau, っ cuối đoạn 1 (sau ――) bị mất, cùng mẫu B2 như 1233/1271 → thêm Ư.
- 912: sweep bỏ sót — JP `ん……っっ` ở ĐẦU dòng (2 っ), VN chỉ còn 1 "ư". Mẫu B1/B2 của sweep yêu cầu っ sau gạch/ngã nên dòng này lọt; audit bắt được khi đọc ngữ nghĩa.
- 899: sweep xếp "already-rendered" (các gasp っ trong dòng đã được diễn: んっ→"Ưm", っ→"ưm"). Audit đồng ý về gasp, nhưng きゃふっ→"kya" là lỗi RIÊNG (mất ふ) — theo tiền lệ h6 769, sửa thành "Kyaphù".
- 1380: JP có 2 っ (`揉みしだくっ――っ`) — chỉ っ sau ―― là gasp; っ đầu gắn với động từ しだくっ là nhấn mạnh, không thêm Ư. Sweep và audit đồng ý (1 Ư).

## Chi tiết dòng sai

### Xưng hô (3 dòng)

**Key 959 (双鉄)**
- JP: `「僕もだ――僕も、気持ちいい――」`
- TW: `「我也——我也很舒服——」`
- VN cũ: `「Anh cũng vậy——anh cũng, sướng lắm——」`
- Sửa: `「Tôi cũng vậy——tôi cũng, sướng lắm——」`
- Lý do: Soutetsu tự xưng "anh" ×2 trong thoại (JP 僕もだ) → "Tôi" ×2.

**Key 969 (双鉄)**
- JP: `「いくぞ」`
- TW: `「我要進去了」`
- VN cũ: `「Anh vào nhé」`
- Sửa: `「Tôi vào nhé」`
- Lý do: Soutetsu tự xưng "Anh" trong thoại (JP いくぞ) → "Tôi".

**Key 977 (ポーレット)**
- JP: `「おちんちん、ですっ！　バキバキにこわばっちゃってて、\nつらそうで――だから、わたし――せ、責任、とって」`
- TW: `「是雞雞！看它已經完全硬起來了，好像很難受。所以我來負起責任」`
- VN cũ: `「Là dương vật! Nó cương cứng đến phát đau,\ntrông khổ sở quá——nên, tôi sẽ——chịu, chịu trách nhiệm」`
- Sửa: `「Là dương vật! Nó cương cứng đến phát đau, trông khổ sở quá——nên, em sẽ——chịu, chịu trách nhiệm」`
- Lý do: Paulette tự xưng "tôi" — phá vỡ quy ước file (Paulette tự xưng "em" 15 lần, chỉ 1 lần "tôi" ở đây) → "em".

### Thở gấp っ bị bỏ mất (8 dòng)

**Key 816 (ポーレット)**
- JP: `「ひあっ！　あっ――めくれっ――んっ――ひっぱ――っ\n――あっ――おま、んこっ――ひっ――しゅご――んっ」`
- TW: `「呀！啊——被掀翻了——嗯——被拉出來了——啊——小穴——呀——好刺激——嗯」`
- VN cũ: `「Hya! A——bị lộn, ngược——ưm——bị kéo, ra——\n——a——âm, đạo——hi——dữ, dội——ưm」`
- Sửa: `「Hya! A——bị lộn, ngược——ưm——bị kéo, ra——Ư ——a——âm, đạo——hi——dữ, dội——ưm」`
- Lý do: っ cuối đoạn 1 sau ―― bị mất (sweep ghi needs-file-audit, audit tự giải quyết — xem ghi chú trên).

**Key 912 (ポーレット)**
- JP: `「ん……っっ――ふぁ――あっ――ずぼ、ずぼ――んっ、\nされ、ると――ひ――あ――あつい、の――たまっ、て」`
- TW: `「嗯……嗯——呼——啊——被捅到的話——呀——熱——熱熱的——就攢起來了」`
- VN cũ: `「Ưm……ư——phù——a——thọc, thọc——ưm,\nbị, thế——hi——a——nóng, quá——tích tụ, lại」`
- Sửa: `「Ưm……ưư——phù——a——thọc, thọc——ưm, bị, thế——hi——a——nóng, quá——tích tụ, lại」`
- Lý do: JP `ん……っっ` có HAI っ nhưng VN chỉ có một "ư" — theo quy tắc một Ư cho một っ, thêm một "ư". Sweep BỎ SÓT dòng này (っ ở đầu dòng). "hi" giữ nguyên (tiếng rên một âm tiết, theo quy ước file).

**Key 1233 (monologue)**
- JP: `その上竿がぬめるおっぱいに挟み込まれて、\n油断をすれば、今すぐにでも射精しそ――っ！？`
- TW: `再加上肉竿被夾在了乳肉之中，我感覺一不留神就要射出來了——`
- VN cũ: `Thêm vào đó, phần thân bị kẹp chặt giữa bầu ngực ướt đẫm,\nnếu lơ là, tôi có thể xuất tinh ngay lập tức——!?`
- Sửa: `Thêm vào đó, phần thân bị kẹp chặt giữa bầu ngực ướt đẫm, nếu lơ là, tôi có thể xuất tinh ngay lập tức——Ư!?`
- Lý do: JP kết bằng しそ――っ！？ nhưng VN chỉ còn "——!?" — gasp cuối bị mất (sweep xác nhận cùng giá trị).

**Key 1270 (monologue)**
- JP: `どんなに呆けた表情で、これほど単調に動物的に、\n僕の射精を、精液を、一心不乱に求め――っっ！！？`
- TW: `她現在的表情是有多不堪，才能像一隻沒有智慧的動物一樣，這麼死命地索求著我的精液——`
- VN cũ: `Với vẻ mặt ngây dại thế nào, mà lại khao khát sự xuất tinh,\ntinh dịch của tôi một cách đơn điệu, đầy tính động vật đến vậy——!!?`
- Sửa: `Với vẻ mặt ngây dại thế nào, mà lại khao khát sự xuất tinh, tinh dịch của tôi một cách đơn điệu, đầy tính động vật đến vậy——ƯƯ!!?`
- Lý do: JP kết bằng 求め――っっ！！？ (hai っ) nhưng VN chỉ còn "——!!?" — mất cả hai gasp (sweep phụ lục đa-っ xác nhận cùng giá trị "——ƯƯ!!?").

**Key 1271 (monologue)**
- JP: `もどかしかろう。そういう風に責めて――っ！？`
- TW: `她當然會心急了。我就這麼刺激著她——`
- VN cũ: `Khó chịu lắm phải không. Cứ thế mà kích thích——!?`
- Sửa: `Khó chịu lắm phải không. Cứ thế mà kích thích——Ư!?`
- Lý do: JP kết bằng 責めて――っ！？ nhưng VN chỉ còn "——!?" — gasp cuối bị mất (sweep xác nhận cùng giá trị).

**Key 1285 (monologue)**
- JP: `イカせたことには大満足だが、\nその蠢きを感じてしまえばいっそうの射精欲求――っ！？`
- TW: `她達到高潮讓我非常滿意，但是這蠕動也讓我的射精欲膨脹得越來越厲害了。`
- VN cũ: `Việc làm cô ấy lên đỉnh khiến tôi rất mãn nguyện,\nnhưng cảm nhận được sự cựa quậy đó lại càng kích thích khao khát xuất tinh——!?`
- Sửa: `Việc làm cô ấy lên đỉnh khiến tôi rất mãn nguyện, nhưng cảm nhận được sự cựa quậy đó lại càng kích thích khao khát xuất tinh——Ư!?`
- Lý do: JP kết bằng 射精欲求――っ！？ nhưng VN chỉ còn "——!?" — gasp cuối bị mất (sweep xác nhận cùng giá trị).

**Key 1331 (monologue)**
- JP: `アナルへ再び指を挿れられ、\nポーレットは大きく震えてしま――っ！！`
- TW: `我又一次把手指插入菊穴，她就狠狠地抖了一下！`
- VN cũ: `Bị nhét ngón tay vào lỗ hậu lần nữa,\nPaulette run lên bần bật——!!`
- Sửa: `Bị nhét ngón tay vào lỗ hậu lần nữa, Paulette run lên bần bật——Ư!!`
- Lý do: JP kết bằng 震えてしま――っ！！ nhưng VN chỉ còn "——!!" — gasp cuối bị mất (sweep xác nhận cùng giá trị).

**Key 1380 (monologue)**
- JP: `だから、思いっきり密着し、\nポーレットの胸を揉みしだくっ――っ！？`
- TW: `所以我就用力貼緊她，盡情揉搓她的大奶——`
- VN cũ: `Nên tôi áp sát hết sức,\nvà vò nát bầu ngực của Paulette——!?`
- Sửa: `Nên tôi áp sát hết sức, và vò nát bầu ngực của Paulette——Ư!?`
- Lý do: JP kết bằng 揉みしだくっ――っ！？ nhưng VN chỉ còn "——!?" — gasp cuối (っ sau ――) bị mất (sweep xác nhận cùng giá trị; っ đầu gắn với động từ しだくっ là nhấn mạnh, không phải gasp).

### Tiếng thở La-tinh / mất âm ふ (6 dòng)

**Key 818 (ポーレット)**
- JP: `「ひあっ！　あっ！　はっ！　あっ！　ふあっ！\nあっ――んゆっ――ひゃふっ！！」`
- TW: `「呀！啊！啊！啊！呼啊！啊——嗯——呀啊！！」`
- VN cũ: `「Hya! A! Hà! A! Phù!\nA——ưm——hya!!」`
- Sửa: `「Hya! A! Hà! A! Phù! A——ưm——hyafu!!」`
- Lý do: ひゃふっ bị dịch "hya", mất ふ — theo tiền lệ h6 770: ひゃふっ→"Hyafu".

**Key 821 (ポーレット)**
- JP: `「きゃふっ！　んくっ――あっ――やっ――はッ――\nんっ――きもち――きゃう――あ――きもち、いいっ」`
- TW: `「呀！嗯——啊——呀——呼——嗯——好舒服——啊——好舒服」`
- VN cũ: `「Kya! Ưm——a——á——hà——\nưm——sướng——kya——a——sướng, quá」`
- Sửa: `「Kyaphù! Ưm——a——á——hà—— ưm——sướng——kya——a——sướng, quá」`
- Lý do: きゃふっ bị dịch "Kya", mất ふ — theo tiền lệ h6 769: きゃふっ→"Kyaphù". きゃう→"kya" giữ nguyên (tiếng rên dài, theo tiền lệ ré).

**Key 834 (ポーレット)**
- JP: `「んきゅんっ！？　んっ――ふあっ！？　らめっ、\nイクっ！　ふあっ！　あっ！　あっ！　あっ！！」`
- TW: `「呀！？嗯——呼啊！？不行，丟了！不行！呼啊！啊！啊！啊！！！」`
- VN cũ: `「Ưm kyun!? Ưm——phù!? Không được,\nlên đỉnh mất! Phù! A! A! A!!」`
- Sửa: `「Ưm!? Ưm——phù!? Không được, lên đỉnh mất! Phù! A! A! A!!」`
- Lý do: んきゅんっ bị dịch "Ưm kyun" — theo tiền lệ h6 869, họ âm んきゅ gộp thành "Ưm", bỏ đuôi La-tinh.

**Key 899 (ポーレット)**
- JP: `「んっ――きゃふっ――あっ！　かっ――き、きつ――っ\n――ンッ――はっ、あ――いきな、りっ――んうっ！」」`
- TW: `「嗯——呀——啊！啊——好粗——嗯——呼——啊——突然就——嗯！」」`
- VN cũ: `「Ưm——kya——a! C-chật, chật quá——\n——ưm——hà, a——đột ngột, quá——ưm!」`
- Sửa: `「Ưm——Kyaphù——a! C-chật, chật quá—— ——ưm——hà, a——đột ngột, quá——ưm!」`
- Lý do: きゃふっ bị dịch "kya", mất ふ — theo tiền lệ h6 769: きゃふっ→"Kyaphù". (Sweep xếp dòng này "already-rendered" vì các gasp っ đã được diễn; lỗi きゃふ là vấn đề khác, audit phát hiện.)

**Key 918 (ポーレット)**
- JP: `「んきゅんっ！！！」`
- TW: `「嗯呀！！！」`
- VN cũ: `「Ưm kyun!!!」`
- Sửa: `「Ưm!!!」`
- Lý do: んきゅんっ bị dịch "Ưm kyun" — theo tiền lệ h6 869, họ âm んきゅ gộp thành "Ưm".

**Key 921 (ポーレット)**
- JP: `「んきゅっ！　ふああっ！！！」`
- TW: `「嗯啊！呼啊！！！」`
- VN cũ: `「Ưm kyu! Phù a!!!」`
- Sửa: `「Ưm! Phù a!!!」`
- Lý do: んきゅっ bị dịch "Ưm kyu" — theo tiền lệ h6 869, họ âm んきゅ gộp thành "Ưm".

### SFX — sai âm / mất độ dài (6 dòng)

**Key 826 (ポーレット)**
- JP: `「ひあっ！？　きゅ――きゅふうううんっ！！！」`
- TW: `「呀！？呀——呀啊啊啊！！！」`
- VN cũ: `「Hya!? Kyu——kyufuuuun!!!」`
- Sửa: `「Hya!? Kíu——kíphúuuun!!!」`
- Lý do: Tiếng ré dài きゅ――きゅふうううんっ bị để phiên âm La-tinh — theo tiền lệ h6 768 (tiếng ré dài きゅう…→"Kíuuuuuuuuun"), viết lại bằng chính tả Việt có dấu.

**Key 860 (ポーレット)**
- JP: `「いっ――きゅううううううううううううぅぅんっ！！」`
- TW: `「咿——嗯啊啊啊啊啊！！」`
- VN cũ: `「I——kyuuuuuuuuuuuuuuuuuun!!」`
- Sửa: `「I——Kíuuuuuuuuuuuuuuuuuun!!」`
- Lý do: Tiếng ré dài きゅう…ぅぅんっ bị để phiên âm La-tinh — theo tiền lệ h6 768, viết lại bằng chính tả Việt có dấu, giữ nguyên độ dài (18 chữ u như bản cũ).

**Key 894 (ポーレット)**
- JP: `「ちゅうっ――ちゅつ――ちゅむっ――ちゅるっ――んっ\n――ちゅるうっ――ちゅっ――ずじゅっ――ずりゅりゅ」`
- TW: `「啾嚕——啾嚕——啾噗——啾噗——嗯——啾嚕——啾嚕——啾噗——啾噗」`
- VN cũ: `「Chụt——chụt——chụt——chụt——ưm\n——chụt——chụt——chụt——chụt」`
- Sửa: `「Chụt——chụt——chụt——chụt——ưm ——chụt——chụt——chụt——rột」`
- Lý do: ずりゅりゅ (tiếng liếm/rột) bị dịch "chụt" — theo quy ước nội bộ file (じゅるうっ→"Rột" ở 895), sửa thành "rột".

**Key 895 (ポーレット)**
- JP: `「れろっ！　れるっ！　れろろっ！　にゅるっ！！\nずっ！　じゅっ――じゅううううっ！　じゅるうっ！」`
- TW: `「啾嚕！啾嚕！啾嚕！啾嚕！！啾噗！啾嚕！啾噗！！」`
- VN cũ: `「Rộp! Liếm! Rộp! Tuột!!\nThọc! Chụt——chụt! Rột!」`
- Sửa: `「Rộp! Rộp! Rộp! Tuột!! Thọc! Chụt——chụt! Rột!」`
- Lý do: れるっ bị dịch "Liếm", phá vỡ quy ước nội bộ file (れるっ→"rộp" ở 910/911/872) — sửa thành "rộp".

**Key 1651 (双鉄)**
- JP: `（じゅぶううううううううううっ！）`
- TW: `（啾噗！）`
- VN cũ: `（Chụt!）`
- Sửa: `（Chúuuuuuuuuuut!）`
- Lý do: Tiếng mút dài じゅぶううううううううううっ (10 âm う) bị dịch gọn thành "Chụt!" — mất độ dài; theo tiền lệ 1701 trong file (ずぶう…→"sâuuuuuuuu"), kéo dài thành "Chúuuuuuuuuuut!".

**Key 1684 (monologue)**
- JP: `（ずぶううううううううっ！）`
- TW: `（插入）`
- VN cũ: `（Thọc sâu!!!）`
- Sửa: `（Thọc sâuuuuuuuu!）`
- Lý do: Tiếng đâm dài ずぶううううううううっ (8 âm う) bị dịch gọn thành "Thọc sâu!!!" — mất độ dài; trong file 1700/1701 cùng mẫu ずぶう… đều viết "sâuuuuuuuu" (8 chữ u).

### Khác (1 dòng)

**Key 861 (双鉄)**
- JP: `「おっと」`
- TW: `「哎」`
- VN cũ: `「Ốp」`
- Sửa: `「Ối」`
- Lý do: おっと ("Ối chà/Ui") bị dịch "Ốp" — sai nghĩa hoàn toàn. (Cùng lỗi còn ở h8 2179 — chờ audit file đó.)

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
[script]
816 = "「Hya! A——bị lộn, ngược——ưm——bị kéo, ra——Ư ——a——âm, đạo——hi——dữ, dội——ưm」"
818 = "「Hya! A! Hà! A! Phù! A——ưm——hyafu!!」"
821 = "「Kyaphù! Ưm——a——á——hà—— ưm——sướng——kya——a——sướng, quá」"
826 = "「Hya!? Kíu——kíphúuuun!!!」"
834 = "「Ưm!? Ưm——phù!? Không được, lên đỉnh mất! Phù! A! A! A!!」"
860 = "「I——Kíuuuuuuuuuuuuuuuuuun!!」"
861 = "「Ối」"
894 = "「Chụt——chụt——chụt——chụt——ưm ——chụt——chụt——chụt——rột」"
895 = "「Rộp! Rộp! Rộp! Tuột!! Thọc! Chụt——chụt! Rột!」"
899 = "「Ưm——Kyaphù——a! C-chật, chật quá—— ——ưm——hà, a——đột ngột, quá——ưm!」"
912 = "「Ưm……ưư——phù——a——thọc, thọc——ưm, bị, thế——hi——a——nóng, quá——tích tụ, lại」"
918 = "「Ưm!!!」"
921 = "「Ưm! Phù a!!!」"
959 = "「Tôi cũng vậy——tôi cũng, sướng lắm——」"
969 = "「Tôi vào nhé」"
977 = "「Là dương vật! Nó cương cứng đến phát đau, trông khổ sở quá——nên, em sẽ——chịu, chịu trách nhiệm」"
1233 = "Thêm vào đó, phần thân bị kẹp chặt giữa bầu ngực ướt đẫm, nếu lơ là, tôi có thể xuất tinh ngay lập tức——Ư!?"
1270 = "Với vẻ mặt ngây dại thế nào, mà lại khao khát sự xuất tinh, tinh dịch của tôi một cách đơn điệu, đầy tính động vật đến vậy——ƯƯ!!?"
1271 = "Khó chịu lắm phải không. Cứ thế mà kích thích——Ư!?"
1285 = "Việc làm cô ấy lên đỉnh khiến tôi rất mãn nguyện, nhưng cảm nhận được sự cựa quậy đó lại càng kích thích khao khát xuất tinh——Ư!?"
1331 = "Bị nhét ngón tay vào lỗ hậu lần nữa, Paulette run lên bần bật——Ư!!"
1380 = "Nên tôi áp sát hết sức, và vò nát bầu ngực của Paulette——Ư!?"
1651 = "（Chúuuuuuuuuuut!）"
1684 = "（Thọc sâuuuuuuuu!）"
```

## Kết bài

- Tổng kết: đọc toàn bộ 326 dòng (độc thoại 174, Paulette 96, Soutetsu 56) — sai **24 dòng (7,4%)**: thoại sai 17/152 (Soutetsu 4/56, Paulette 13/96), lời dẫn sai 7/174. Phân loại: xưng hô 3, thở gấp っ 8, tiếng thở 6, SFX 6, khác 1. 0 dòng chưa chắc chắn.
- File sạch về cấu trúc: 0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương (chỉ số VN trùng trong file và chỉ số VN toàn dự án đều hợp lệ; heuristic thoại↔lời dẫn đạt 326/326 ở shift 0; JP/TW lệch loại 0).
- Bảy file h1–h7 cộng lại sai 263/2.069 dòng (12,7%). Còn lại trong 03_Paulette: h8 (1 file), lr_h1/lr_h2/lr_稀咲h1/れいな02 (4 file).
- Bằng chứng cho quyết định đang chờ: Soutetsu gọi Paulette "em" 1 lần (907) vs "cô" 5 lần (560, 953×2, 954, 1015) — cộng dồn toàn dự án: "em" 85 vs "cô" 48. Đây là file đầu tiên nghiêng về "cô" kể từ Paulette 02 — giả thuyết "em" đã thắng có thể cần xem lại khi audit tiếp h8 và các file lr.
- Đề xuất mới cho Hieu: quy tắc độ dài âm SFX — âm dài trong JP (う kéo dài) phải được kéo dài tương ứng trong VN (tiền lệ trong file: 1700/1701); 1684 và 1651 là hai dòng vi phạm.
- Khối TOML 24 key đã parse đúng; áp dụng khối này sẽ sửa hết 24 dòng. Không có dòng chưa chắc chắn nào trong file này. Các điểm khác sweep (816 đã giải quyết, 912 sweep bỏ sót, 899 sửa thêm lỗi きゃふ) đã ghi rõ lý do ở trên để đối chiếu khi gộp với sweep.
