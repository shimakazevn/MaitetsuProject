# Audit れいなh4 — れいなh4_ふたりっきりのハロウィン.txt.toml

**Ngày kiểm toán:** 20/11/2026

**Tệp TOML:** `04_Reina/れいなh4_ふたりっきりのハロウィン.txt.toml` — md5 `43ddc25620d65d8d021ab6e6572b5caa`, 115.354 byte, BOM, CRLF (1.187 CRLF, 0 LF-only), `[selections]` rỗng, **không có bản sao trùng** (kiểm tra md5 toàn bộ 227 tệp TOML; queue ghi 1 copy).

**Nguồn CSV:** "Trang tính 3" — bộ hàng duy nhất `04_Reina` (không có bẫy dual-set ở file này), 584 hàng `[script]`, key 54–3291, 0 VN rỗng.

**Kết quả: 59/584 dòng sai (10,1%), 1 dòng chưa chắc chắn, 0 dòng lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo file.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| SFX hơi thở fa/fu (quy tắc đã chốt) | 34 |
| Gasp っ bị mất | 6 |
| Tiếng cười うふふぅ diễn thành tiếng rên | 3 |
| Sai nghĩa (meaning) | 8 |
| Thuật ngữ | 5 |
| Xưng hô | 2 |
| Lỗi nhỏ | 1 |
| **Tổng** | **59** |

Nhóm SFX (34): 46 token fa/fu trên 34 dòng — ふあっ→"phù" 17 token (16 dòng, 2459 mang 2), ふぁ→"phà" 4, ふあ không っ→"phùa" 4 (2001 mang 2), ふぇ→"phuê" 4, ふやっ/ふやぁ→"phuya" 3, ふっ→"phù" 5, ふ lẻ cuối dòng→"phù" 2 (1976, 2005); trong đó 7 token kéo dài (1894 ふぁぁっ→"phàa", 1983 ふやあああ→"Phuyaaaan", 1986 ふぁぁぁっん→"Phàaan", 2454 ふあぁ→"Phùaa", 2456 ふぁあっ→"Phàa", 2458 ふあああぁぁぁ→"Phùaaaaaa" + ふああ→"Phùaa"). Nhóm gasp (6): 5 từ sweep áp nguyên đã kiểm chứng (1963, 1990, 2022, 2972, 3095) + 1 gasp sweep bỏ sót (1962, cả dòng っ――！). Nhóm cười (3): 2099, 2104, 2111 — cùng mẫu sai, trong khi 2089/2102/2103 trong file đã đúng "Ufufu~". Sai nghĩa (8): 1958, 2040, 2263, 2276, 2313, 2545, 3056, 3156. Thuật ngữ (5): 2118, 2350 (姉妹機), 2535, 2797, 3118 (御一夜→Ohitoyo). Xưng hô (2): độc thoại Soutetsu "anh"→"tôi" (3028, 3188). Lỗi nhỏ (1): 2925.

**Theo loại dòng:** thoại 50/396 sai (12,6%), độc thoại 9/188 sai (4,8%). **Theo nhân vật:** れいな (Reina) 43, 双鉄 (Soutetsu) 7, monologue 9.

File này sạch về cấu trúc — 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng, 0 dòng chưa chắc chắn ngoài 2288. Lỗi tập trung ở một lỗi hệ thống duy nhất: toàn bộ 34 tiếng thở ふぁ/ふあ/ふぇ/ふや của Reina đều để nguyên dạng La-tinh "Fua"/"fua"/"Fe"/"Fuya" (trái quy tắc fa/fu đã chốt 19/11 và đã áp dụng ở các file h1/h2/lr-h1/lr-h2, nagih2, Mayami) + 3 tiếng cười うふふぅ bị diễn thành tiếng rên. Toàn bộ 59 lỗi đều sửa được tại chỗ, không cần dịch lại.

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục. TOML md5 `43ddc25620d65d8d021ab6e6572b5caa`, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng trong 227 tệp (file này chỉ có 1 copy).

- **CSV vs TOML:** VN khớp tuyệt đối 225 hàng; khớp sau khi gộp ký tự xuống dòng thành khoảng trắng 359 hàng; **0 khác biệt thực chất** — toàn bộ là hiện tượng gộp `\n` trong TOML-2. CSV3 là bản chuẩn cho fix list. Comment `# JP:` trong `[script]` 584/584 (4 comment `# JP:` khác nằm ở `[characters]`/`[character_subs]`, không phải dòng script).

- **Sweep っ (gasp):** kiểm tra trực tiếp sweep-raw-gasp-wrong.json — file này CÓ 5 mục, cả 5 áp nguyên đã kiểm chứng (1963, 1990, 2022, 2972, 3095). Quét bổ sung toàn bộ dòng JP chứa っ: bắt thêm 1 gasp sweep bỏ sót (1962: っ――！ cả dòng, VN chỉ còn "!"). Không còn gasp っ trần nào khác bị mất — 2901 (ためっ!) là っ nhấn mạnh cuối câu, đúng là không thêm Ư.

- **Thẻ %l:** JP 0 thẻ, VN 0 thẻ — không có thẻ nào trong file này. Thẻ ruby `[tên,1]` trên JP: 3 dòng (2150 [くまぎん,1], 2241 [ゆのい,1], 2338 [はっぱ,1]) — VN bỏ marker theo đúng lệ toàn dự án (furigana không mang sang VN); 2241 là bằng chứng mới cho đề xuất "Yunoi" (furigana ゆのい trên 湯医), xem §5.

- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng: 0), không có VN mồ côi (orphan: 0), không có key trùng (584 key duy nhất), không có hàng VN == TW.

- **Kiểm tra nhiễm chéo:** đối chiếu 59 giá trị VN cũ trong fix list + toàn bộ VN của file qua chỉ mục VN toàn dự án (91.731 dòng) — các lần trùng đều là câu ngắn thông dụng hoặc SFX lặp lại hợp lệ; 4 cặp VN trùng trong file (2506/2296 「Vậy sao.", 2022/1962 「!", 3251/3282 "（Xoẹt——xoẹt——）", 3254/3268 "（Chụt）") đều là JP giống nhau hoặc SFX ngắn hợp lệ với JP tương ứng, không phải lệch dòng. 0 lần trùng VN trong file với JP khác nhau.

- **8 ứng cử viên mạnh của queue:** heuristic chỉ là giới hạn dưới — đọc toàn bộ 584 dòng tìm ra 59 dòng sai; không dòng nào trong 8 ứng cử viên là lệch dòng (toàn bộ VN đều khớp JP/TW về nghĩa, lỗi là SFX/thuật ngữ/xưng hô).

## 3. Chi tiết từng dòng sai

Ký hiệu: ⏎ = ký tự xuống dòng dạng backslash-n trong JSON/TOML (game tự wrap, không dùng \n thật).

### 3.1. SFX hơi thở fa/fu (34 dòng)

**1784 [れいな]**
JP: 「いっしょ――いっしょ――んっ――ふあっ――⏎れいなも――いっしょ――いっしょがいい、ですぅ」
TW: 「一起……一起……蛤啊……玲奈……也想一起高潮」
Cũ: 「Cùng nhau——cùng nhau——ưm——fua——⏎Reina cũng——cùng nhau——muốn cùng nhau, ạ~」
Mới: 「Cùng nhau——cùng nhau——ưm——phù——⏎Reina cũng——cùng nhau——muốn cùng nhau, ạ~」
Lý do: Quy tắc fa/fu đã chốt: ふあっ → "phù"; bản cũ "fua" là romanisation.

**1835 [れいな]**
JP: 「きたっ――きてるっ――ふあっ――あっ――あっ！⏎あついっ――あついのっ――そうてつ――さん、の」
TW: 「來了、來了……蛤啊啊啊啊！雙鐵先生……熱熱的……啊嗯」
Cũ: 「Đến rồi——đang tới——fua——a——a!⏎Nóng quá——nóng quá——của anh——Soutetsu」
Mới: 「Đến rồi——đang tới——phù——a——a!⏎Nóng quá——nóng quá——của anh——Soutetsu」
Lý do: Quy tắc fa/fu đã chốt: ふあっ → "phù"; bản cũ "fua" là romanisation.

**1885 [れいな]**
JP: 「ひあっ――あっ――ぐりっ――って――はい、って⏎――んっ――ふあっ――あ――おなか――ずり、って」
TW: 「呀啊啊……啊……進來了……在肚子裡……摩擦著……」
Cũ: 「Hya——a——ngoáy——vào——rồi⏎——ưm——fua——a——trong bụng——cọ, cọ」
Mới: 「Hya——a——ngoáy——vào——rồi⏎——ưm——phù——a——trong bụng——cọ, cọ」
Lý do: Quy tắc fa/fu đã chốt: ふあっ → "phù"; bản cũ "fua" là romanisation.

**1890 [れいな]**
JP: 「ふぇっ」
TW: 「咦」
Cũ: 「E」
Mới: 「Phuê」
Lý do: Quy tắc fa/fu đã chốt: ふぇっ → "phuê"; bản cũ "E" sai âm — ふぇ là tiếng thở, không phải thán từ ngạc nhiên "E" (tiền lệ hibiki07 1720/1742: ふぇっ→"phuê").

**1894 [れいな]**
JP: 「ふぇ？　あ――……ふぁぁっ」
TW: 「咦？啊……哇」
Cũ: 「E? A——……fuaa」
Mới: 「Phuê? A——……phàa」
Lý do: Quy tắc fa/fu: ふぇ → "phuê"; ふぁぁっ (2 âm a) → "phàa" (tiền lệ nagih2 1273: ふぁぁうんっ→"Phàaun", giữ đủ 2 âm a, っ cuối sau nguyên âm kéo dài được bỏ).

**1936 [れいな]**
JP: 「んっ――ふっ――あっ――さき、ぽっ――んっ、⏎さきっぽ、の――ふとい――とこ――だけっ――」
TW: 「哈嗯……啊……龜頭……粗粗的部位……」
Cũ: 「Ưm——fu——a——phần, đầu——ưm,⏎phần đỉnh, của——chỗ——to——thôi——」
Mới: 「Ưm——phù——a——phần, đầu——ưm,⏎phần đỉnh, của——chỗ——to——thôi——」
Lý do: Quy tắc fa/fu: ふっ → "phù" (tiền lệ nagih2 1199).

**1938 [れいな]**
JP: 「ふぇ――ふやっ」
TW: 「哎呀……」
Cũ: 「Fe——fuya」
Mới: 「Phuê——phuya」
Lý do: Quy tắc fa/fu: ふぇ → "phuê"; ふやっ → "phuya".

**1967 [れいな]**
JP: 「や――れいな――おしっ、こ――おもら、し――⏎ふあっ――あっ――まだ――出ちゃ、う――ふやぁ」
TW: 「啊……玲奈……蛤啊……又要尿出來了……啊啊啊」
Cũ: 「A——Reina——tè, dầm——mất, rồi——⏎fua——a——vẫn——còn ra, nữa——fuya」
Mới: 「A——Reina——tè, dầm——mất, rồi——⏎phù——a——vẫn——còn ra, nữa——phuya」
Lý do: Quy tắc fa/fu: ふあっ → "phù"; ふやぁ → "phuya".

**1969 [れいな]**
JP: 「ふぁ……うしろ、から――せっ、くす――⏎セックス、する、ですかぁ？」
TW: 「啊……要從背後……做愛嗎？」
Cũ: 「Fua……từ, phía sau——làm, tình——⏎quan hệ, sao ạ~?」
Mới: 「Phà……từ, phía sau——làm, tình——⏎quan hệ, sao ạ~?」
Lý do: Quy tắc fa/fu: ふぁ (không っ) → "phà".

**1976 [れいな]**
JP: 「ぅあぁ――ぁっ――がく、がく――しちゃうっ――⏎ふぇ――あ――きもち――きもち、いいっ――ふ、あ」
TW: 「啊啊啊……身體……都發抖了……蛤啊、好舒服……好舒服……啊啊啊」
Cũ: 「Ua——a——giật, giật——mất rồi——⏎fe——a——sướng——sướng, quá——fu, a」
Mới: 「Ua——a——giật, giật——mất rồi——⏎phuê——a——sướng——sướng, quá——phù, a」
Lý do: Quy tắc fa/fu: ふぇ → "phuê"; ふ ở cuối (「ふ、あ" — hai hơi thở riêng) → "phù" như 2005.

**1978 [れいな]**
JP: 「ひゃあううんっ！　そう、てつ――しゃん――ふあ⏎――れいな、もう――もうっ！！」
TW: 「啊啊啊啊……雙鐵先生……玲奈已經……已經不行了！！」
Cũ: 「Hyaauun! Anh, Soutetsu——fua⏎——Reina, sắp——sắp rồi!!」
Mới: 「Hyaauun! Anh, Soutetsu——phùa⏎——Reina, sắp——sắp rồi!!」
Lý do: Quy tắc fa/fu: ふあ (không っ) → "phùa".

**1983 [れいな]**
JP: 「ふやあああんっ！　――ふぁ、あ、いまも――⏎ぷる、って、おっぱい、ふるえて、あせ、とろとろで」
TW: 「啊啊啊啊啊！蛤啊，現在也是……胸部在顫抖……流了好多汗」
Cũ: 「Fuyaaaan! ——Fua, a, bây giờ cũng——⏎rung lên, ngực, đang run rẩy, mồ hôi, ướt nhẹp」
Mới: 「Phuyaaaan! ——Phà, a, bây giờ cũng——⏎rung lên, ngực, đang run rẩy, mồ hôi, ướt nhẹp」
Lý do: Quy tắc fa/fu: ふやあああ (ya + 3 âm a) → "Phuyaaaan" (giữ đủ 4 âm a + ん); ふぁ → "phà".

**1986 [れいな]**
JP: 「ひゃっ！　うっ！　ふあっ！　これっ！　これっ！⏎しゅごっ――んっ――ひっ――ふぁぁぁっん！！！」
TW: 「啊啊啊！啊啊！啊啊啊！這樣……好舒服……呀啊啊！！！」
Cũ: 「Hya! Ư! Fua! Cái này! Cái này!⏎Tuyệt quá——ưm——hi——fuaaaan!!!」
Mới: 「Hya! Ư! Phù! Cái này! Cái này!⏎Tuyệt quá——ưm——hi——Phàaan!!!」
Lý do: Quy tắc fa/fu: ふあっ → "phù"; ふぁぁぁっん (3 âm a + ん) → "Phàaan" (tiền lệ nagih2 1278: giữ đủ số âm a và âm mũi ん; bản cũ "fuaaaan" thừa 1 âm a).

**1999 [れいな]**
JP: 「ひあっ――あん――んっ――べろ――さきっぽ、で、⏎ちょん、ちょんっ――って、れいな、それっ、ふぁ」
TW: 「啊嗯……嗯……舌尖……動來動去的……玲奈……啊嗯」
Cũ: 「Hya——an——ưm——lưỡi——phần đầu, đang,⏎chạm, chạm——vào, Reina, cái đó, fua」
Mới: 「Hya——an——ưm——lưỡi——phần đầu, đang,⏎chạm, chạm——vào, Reina, cái đó, phà」
Lý do: Quy tắc fa/fu: ふぁ (không っ) → "phà".

**2000 [れいな]**
JP: 「ふゆっ――んっ――ふあっ――あ――ひゅっ、⏎んっ――あ――そうてつさん――そうてつ、さぁん」
TW: 「啊嗯……嗯……蛤啊……啊，啊嗯……雙鐵先生——雙鐵先生」
Cũ: 「Fuyu——ưm——fua——a——hyu,⏎ưm——a——anh Soutetsu——anh Soutetsu」
Mới: 「Fuyu——ưm——phù——a——hyu,⏎ưm——a——anh Soutetsu——anh Soutetsu」
Lý do: Quy tắc fa/fu: ふあっ → "phù". "Fuyu" (ふゆっ) GIỮ NGUYÊN — quy tắc chỉ bao ふぁ/ふあ/ふぇ/ふや, không bao ふゆ (tiền lệ Mayami: "Funyaa"/"Fuwaaaaaaaa" giữ nguyên).

**2001 [れいな]**
JP: 「ひゃう、う――んっ――ふあ――んっ――⏎おし――りっ――んっ――ちくび、もっ――ふあ」
TW: 「啊嗯……嗯……蛤啊……屁股……哈嗯……和乳頭……蛤啊」
Cũ: 「Hyau, ư——ưm——fua——ưm——⏎mông——ưm——núm vú, nữa——fua」
Mới: 「Hyau, ư——ưm——phùa——ưm——⏎mông——ưm——núm vú, nữa——phùa」
Lý do: Quy tắc fa/fu: ふあ (không っ) → "phùa" (cả 2 chỗ).

**2004 [れいな]**
JP: 「ひゃんっ――んんっ――ふあっ――あっ――もっと、⏎もっと、おっぱい。れいな、ぜんぶ――もっとぉ」
TW: 「啊嗯……蛤啊……啊……繼續，繼續摸胸部……玲奈的全部……」
Cũ: 「Hyan——ưm——fua——a——nữa đi,⏎nữa đi, ngực. Reina, tất cả——nữa đi~」
Mới: 「Hyan——ưm——phù——a——nữa đi,⏎nữa đi, ngực. Reina, tất cả——nữa đi~」
Lý do: Quy tắc fa/fu: ふあっ → "phù".

**2005 [れいな]**
JP: 「んきゅっ――ンッ――あっ――ふっ――さきっぽ⏎――ちく、び――じんじん、して、きて――ふ、あ」
TW: 「啊嗯……蛤啊……胸部前面……乳頭……感覺酥酥麻麻的……啊嗯」
Cũ: 「Nkyu——ư——a——fu——phần đỉnh⏎——núm, vú——tê rần, lên, rồi——fu, a」
Mới: 「Nkyu——ư——a——phù——phần đỉnh⏎——núm, vú——tê rần, lên, rồi——phù, a」
Lý do: Quy tắc fa/fu: ふっ → "phù"; ふ ở cuối (「ふ、あ") → "phù" như 1976.

**2013 [れいな]**
JP: 「ひゃうんっ！　あっ――ふあっ、あっ――れいな、⏎アナル――アナル、おかしくなっちゃうですよぅ」
TW: 「啊嗯！啊……蛤啊……玲奈，肛門……肛門變得好奇怪」
Cũ: 「Hyaun! Á——fua, á——Reina,⏎hậu môn——hậu môn, trở nên kỳ lạ mất rồi ạ~」
Mới: 「Hyaun! Á——phù, á——Reina,⏎hậu môn——hậu môn, trở nên kỳ lạ mất rồi ạ~」
Lý do: Quy tắc fa/fu: ふあっ → "phù".

**2015 [れいな]**
JP: 「きゅふっ――んっ！　～～～っ！　ふっ――く――⏎んっ――だめ――ま、だっ――おまんこ、だめえっ」
TW: 「啊嗯！啊啊啊……嗚嗚……啊啊啊……小穴……還不能高潮……」
Cũ: 「Kyufu——ưm! ~~~! Fu——ku——⏎ưm——không được——vẫn, chưa——chỗ đó, chưa được」
Mới: 「Kyufu——ưm! ~~~! Phù——ku——⏎ưm——không được——vẫn, chưa——chỗ đó, chưa được」
Lý do: Quy tắc fa/fu: ふっ độc lập → "phù". "Kyufu" (きゅふっ — cả từ SFX) GIỮ NGUYÊN theo tiền lệ h6 (các tiếng thở La-tinh nguyên từ như "Fukyun!"/"Hyau!" được giữ).

**2017 [れいな]**
JP: 「ふみゅぅぅぅんっ！　ちゅうって――ふあっ――⏎そうてつ、さん、が――おまん、こ、ちゅうう、って」
TW: 「啊嗯！親上來了……蛤啊……雙鐵先生……親了小穴……」
Cũ: 「Fumyuuuun! Hôn kìa——fua——⏎anh Soutetsu——hôn, chỗ, đó, kìa」
Mới: 「Fumyuuuun! Hôn kìa——phù——⏎anh Soutetsu——hôn, chỗ, đó, kìa」
Lý do: Quy tắc fa/fu: ふあっ → "phù".

**2088 [れいな]**
JP: 「えへ、へぇ――れいな――ほめ、られ、て――ふっ⏎――ふあっ――あ――うれしい、です――よぉ――ん」
TW: 「嘿嘿……玲奈被誇獎啦……啊嗯……蛤啊、啊……好開心」
Cũ: 「Ehe, he~——Reina——được, khen——fu⏎——fua——a——vui, lắm——ạ~——ưm」
Mới: 「Ehe, he~——Reina——được, khen——phù⏎——phù——a——vui, lắm——ạ~——ưm」
Lý do: Quy tắc fa/fu: ふっ → "phù"; ふあっ → "phù".

**2134 [れいな]**
JP: 「はっ――はげっ――しっ――ふっ――んあっ――⏎れい、な――おな、か――きゅんっ、て、きゅうんて」
TW: 「好……好激烈……啊嗯，玲奈……肚子裡……動來動去……」
Cũ: 「Ha——mãnh, liệt——quá——fu——n-a——⏎bụng, của——Rei, na——đang, quặn, lại」
Mới: 「Ha——mãnh, liệt——quá——phù——n-a——⏎bụng, của——Rei, na——đang, quặn, lại」
Lý do: Quy tắc fa/fu: ふっ → "phù".

**2172 [れいな]**
JP: 「おまん、こっ――とけ――て――くっつい――て⏎――ふあっ――ずり――ずりっ――いっしょ、にっ」
TW: 「小穴……都要溶化了……肉棒緊貼著……蛤啊啊……蹭來蹭去的……」
Cũ: 「Chỗ, đó——như tan, chảy——bám chặt, lấy⏎——fua——cọ——cọ xát——cùng, nhau」
Mới: 「Chỗ, đó——như tan, chảy——bám chặt, lấy⏎——phù——cọ——cọ xát——cùng, nhau」
Lý do: Quy tắc fa/fu: ふあっ → "phù".

**2202 [れいな]**
JP: 「ゆっくり――おまん、こ――ほじって、され、て⏎――ふあっ――あっ――くびれ、てる――とこっ」
TW: 「慢慢……把小穴……撐開了……蛤啊啊……凸起的部位……」
Cũ: 「Chầm chậm——chỗ, đó——bị, đào bới⏎——fua——a——chỗ——thắt, lại」
Mới: 「Chầm chậm——chỗ, đó——bị, đào bới⏎——phù——a——chỗ——thắt, lại」
Lý do: Quy tắc fa/fu: ふあっ → "phù".

**2451 [れいな]**
JP: 「ふぁ――ダメッ――おまん、こ――まだ、だめぇ。⏎いっしょ――そうてつ、さん、と――いっしょ、に」
TW: 「蛤啊……不行……小穴……還不能高潮。要和雙鐵先生……一起……」
Cũ: 「Fua——không được——chỗ, đó——vẫn chưa, được.⏎Cùng nhau——với anh, Soutetsu——cùng, nhau」
Mới: 「Phà——không được——chỗ, đó——vẫn chưa, được.⏎Cùng nhau——với anh, Soutetsu——cùng, nhau」
Lý do: Quy tắc fa/fu: ふぁ (không っ) → "phà".

**2452 [れいな]**
JP: 「ふあっ――べろっっ――べろ、いいですよぉ――⏎んっ――おまんこ――ぜんぶ――れるれるって、して」
TW: 「蛤啊……可以舔哦……啊嗯……把小穴……全部……舔一遍吧……」
Cũ: 「Fua——lưỡi——lưỡi, sướng lắm ạ~——⏎ưm——chỗ đó——tất cả——hãy liếm láp đi ạ」
Mới: 「Phù——lưỡi——lưỡi, sướng lắm ạ~——⏎ưm——chỗ đó——tất cả——hãy liếm láp đi ạ」
Lý do: Quy tắc fa/fu: ふあっ → "phù".

**2453 [れいな]**
JP: 「ふあっ――あ――れいな――おもら、し――んっ、⏎そうてつ、さんの――おくちに――ちょく、せつっ」
TW: 「蛤啊……啊……玲奈……失禁了，直接……尿在……雙鐵先生的嘴裡了」
Cũ: 「Fua——a——Reina——tè dầm, mất——ưm,⏎trực, tiếp——vào miệng——anh, Soutetsu」
Mới: 「Phù——a——Reina——tè dầm, mất——ưm,⏎trực, tiếp——vào miệng——anh, Soutetsu」
Lý do: Quy tắc fa/fu: ふあっ → "phù".

**2454 [れいな]**
JP: 「ふあぁ――おっぱい――ちくび――なで、なで――⏎くりっ――くり――んっ！　きもち、いい、ですぅ」
TW: 「蛤啊……胸部……乳頭……摸來摸去的……好舒服」
Cũ: 「Fuaa——ngực——núm vú——vuốt, vuốt——⏎xoa——xoa——ưm! Sướng, quá, ạ~」
Mới: 「Phùaa——ngực——núm vú——vuốt, vuốt——⏎xoa——xoa——ưm! Sướng, quá, ạ~」
Lý do: Quy tắc fa/fu: ふあぁ (cơ sở phùa + 1 âm a) → "Phùaa".

**2455 [れいな]**
JP: 「ふやっ――ふあっ――そうてつ――さぁん」
TW: 「蛤啊……蛤啊……雙鐵先生」
Cũ: 「Fuya——fua——anh Soutetsu」
Mới: 「Phuya——phù——anh Soutetsu」
Lý do: Quy tắc fa/fu: ふやっ → "phuya"; ふあっ → "phù".

**2456 [れいな]**
JP: 「ふぁあっ」
TW: 「蛤啊」
Cũ: 「Fuaa」
Mới: 「Phàa」
Lý do: Quy tắc fa/fu: ふぁあっ (ぁ+あ = 2 âm a) → "Phàa".

**2457 [れいな]**
JP: 「ふあ……ぁ……ぁ……やぁ――んっ――⏎おまんこ――せいえき――あふれ――ちゃって、る」
TW: 「蛤啊啊啊、啊啊啊……小穴裡的……精液流出來了……」
Cũ: 「Fua……a……a……ya——ưm——⏎chỗ đó——tinh dịch——đang tràn——ra ngoài」
Mới: 「Phùa……a……a……ya——ưm——⏎chỗ đó——tinh dịch——đang tràn——ra ngoài」
Lý do: Quy tắc fa/fu: ふあ (không っ) → "phùa". Các ぁ lẻ sau giữ nguyên dạng "a……a……" như bản cũ.

**2458 [れいな]**
JP: 「ふあああぁぁぁ――れいな、そうてつ、さんの――⏎おくち、に――んきゅっ！？　ふああ――あんっ！！」
TW: 「蛤啊啊啊啊……玲奈……往雙鐵先生的嘴裡……啊啊啊啊！！」
Cũ: 「Fuaaaaa——Reina, vào miệng——⏎anh Soutetsu——nkyu!? Fuaa——an!!」
Mới: 「Phùaaaaaa——Reina, vào miệng——⏎anh Soutetsu——nkyu!? Phùaa——an!!」
Lý do: Quy tắc fa/fu: ふあああぁぁぁ (3 あ + 3 ぁ = 6 âm a) → "Phùaaaaaa" (ù + 6 âm a); ふああ → "Phùaa".

**2459 [れいな]**
JP: 「ふあっ！　あっ！　きもち、いっ――きもち、いい。⏎んっ――あっ――はっ――あっ――ふあっ――あっ」
TW: 「蛤啊！啊！好舒服……好舒服。啊啊啊、啊啊……蛤啊啊」
Cũ: 「Fua! A! Sướng, quá——sướng, quá.⏎Ưm——a——ha——a——fua——a」
Mới: 「Phù! A! Sướng, quá——sướng, quá.⏎Ưm——a——ha——a——phù——a」
Lý do: Quy tắc fa/fu: ふあっ → "phù" (cả 2 chỗ).

### 3.2. Gasp っ bị mất (6 dòng)

**1962 [双鉄]**
JP: 「っ――！」
TW: 「唔！」
Cũ: 「!」
Mới: 「Ư——!」
Lý do: Gasp sweep BỎ SÓT: JP cả dòng chỉ là tiếng hít っ――！, VN chỉ còn dấu "!" — mất hẳn âm. Sửa "Ư——!" theo tiền lệ các gasp cả dòng (sweep 1963/2022 cùng file).

**1963 [双鉄]**
JP: 「っ！！！」
TW: 「唔！！！」
Cũ: 「!!!」
Mới: 「Ư!!!」
Lý do: Sweep áp nguyên đã kiểm chứng: JP cả dòng っ！！！, VN chỉ còn "!!!" — chèn Ư.

**1990 [れいな]**
JP: 「はうぅぅぅ～っ！！」
TW: 「啊嗚！！」
Cũ: 「Hauuuu~!!」
Mới: 「Hauuuu~Ư!!」
Lý do: Sweep áp nguyên đã kiểm chứng: JP はうぅぅぅ～っ！！ — VN giữ đủ 5 nguyên âm "Hauuuu" nhưng mất gasp っ sau dấu ~ — chèn Ư.

**2022 [双鉄]**
JP: 「っ！」
TW: 「啊！」
Cũ: 「!」
Mới: 「Ư!」
Lý do: Sweep áp nguyên đã kiểm chứng: JP cả dòng っ！, VN chỉ còn "!" — chèn Ư.

**2972 [monologue]**
JP: 残尿までを吸いきって――っ！？
TW: 我連殘留的尿液也吸了出來——啊！？
Cũ: Hút sạch cho đến những giọt nước tiểu cuối cùng——!?
Mới: Hút sạch cho đến những giọt nước tiểu cuối cùng——Ư!?
Lý do: Sweep áp nguyên đã kiểm chứng: JP 残尿までを吸いきって――っ！？ — VN mất gasp っ sau dấu ―― — chèn Ư.

**3095 [monologue]**
JP: れいながくるりと後ろをむいてかがみこみ、⏎かわいいおしりが丸見えに――っ！！？
TW: 玲奈轉了半圈蹲下身子，可愛的屁股暴露無遺……咦！！？
Cũ: Reina xoay người lại và cúi xuống,⏎cái mông đáng yêu lộ ra hoàn toàn——!!?
Mới: Reina xoay người lại và cúi xuống,⏎cái mông đáng yêu lộ ra hoàn toàn——Ư!!?
Lý do: Sweep áp nguyên đã kiểm chứng: JP …丸見えに――っ！！？ — VN mất gasp っ sau dấu ―― — chèn Ư.

### 3.3. Tiếng cười diễn thành tiếng rên (3 dòng)

**2099 [れいな]**
JP: 「うふふぅ、れいな、おおかみおんなさんに⏎なっちゃうですねぇ。わんわん。わぉーん」
TW: 「嘿嘿，玲奈要變成小母狼了。汪汪，汪！」
Cũ: 「Ư hu hu~, Reina, sẽ biến thành⏎cô sói cái đó nha~. Gâu gâu. Awoooo~」
Mới: 「Ufufu~, Reina, sẽ biến thành⏎cô sói cái đó nha~. Gâu gâu. Awoooo~」
Lý do: Tiếng cười GIỮ NGUYÊN LÀ TIẾNG CƯỜI (quy tắc Hieu 19/11 22:05 + tiền lệ h8 bị bãi bỏ): うふふぅ là cười khúc khích, phải là "Ufufu~" như 2089/2102/2103 trong chính file này; bản cũ "Ư hu hu~" diễn thành tiếng rên.

**2104 [れいな]**
JP: 「うふふぅ。そしたらちゃあんと呼んでくださいねぇ。⏎ね？　あ・な・た」
TW: 「嘿嘿，那你就要好好叫出來呀。對吧？相·公」
Cũ: 「Ư hu hu~. Vậy thì anh hãy gọi cho đàng hoàng đi nhé.⏎Nha? Mình·ơi」
Mới: 「Ufufu~. Vậy thì anh hãy gọi cho đàng hoàng đi nhé.⏎Nha? Mình·ơi」
Lý do: Như 2099: うふふぅ → "Ufufu~" (cười, không phải rên).

**2111 [れいな]**
JP: 「うふふぅ、そうてつさんも、⏎にこにこわらってくれましたぁ」
TW: 「嘿嘿，雙鐵先生也笑出來啦」
Cũ: 「Ư hu hu~, anh Soutetsu,⏎cũng cười tươi rạng rỡ rồi ạ~」
Mới: 「Ufufu~, anh Soutetsu,⏎cũng cười tươi rạng rỡ rồi ạ~」
Lý do: Như 2099: うふふぅ → "Ufufu~" (cười, không phải rên).

### 3.4. Sai nghĩa (8 dòng)

**1958 [双鉄]**
JP: 「そんなの？」
TW: 「哪種？」
Cũ: 「Cái từ đó?」
Mới: 「Cái kiểu đó á?」
Lý do: TW 哪種？ (loại nào?) xác nhận そんなの chỉ "kiểu/cách" chứ không phải "từ" — cảnh đang bàn ý tưởng cosplay (1960: 「どこの世界のコスプレだ」). Bản cũ "Cái từ đó?" sai đối tượng.

**2040 [双鉄]**
JP: 「ああ、すまん――と、これだこれだ！　ほら」
TW: 「啊，麻煩你了……哦，就是這個！你看」
Cũ: 「À, cảm ơn em——đây rồi, đây rồi! Nhìn này.」
Mới: 「À, xin lỗi em——đây rồi, đây rồi! Nhìn này.」
Lý do: すまん = "xin lỗi" (nghĩa chính), không phải "cảm ơn"; TW 麻煩你了 (phiền bạn rồi / xin lỗi đã làm phiền) ủng hộ nghĩa xin lỗi. Cảnh: Soutetsu tìm thấy đồ, xin lỗi vì để Reina chờ rồi mới khoe.

**2263 [れいな]**
JP: 「そおですねぇ。わからないことでくよくよしてて、⏎わかる今を、しょんぼりしたらもったいないですぅ！」
TW: 「是呀。為未知的事情悶悶不樂，那就太浪費現在的時間了！」
Cũ: 「Đúng vậy nhỉ. Cứ buồn bã vì những chuyện chưa biết,⏎mà làm cho hiện tại đang hiện hữu phải u sầu thì phí lắm ạ~!」
Mới: 「Đúng vậy nhỉ. Cứ buồn bã vì những chuyện chưa biết,⏎mà làm cho hiện tại mà mình biết rõ phải u sầu thì phí lắm ạ~!」
Lý do: わかる今 = "hiện tại mà mình biết rõ" (hiện tại đã biết), không phải "hiện tại đang hiện hữu" — わかる là "biết/hiểu", không phải "tồn tại". TW 為未知的事情悶悶不樂，浪費現在的時間 ủng hộ.

**2276 [双鉄]**
JP: 「そうだな。このぬくもりをしってしまえば――⏎一人ぼっちに戻ってしまうことは、ひどく、いやだな」
TW: 「是啊。感受到了這份溫暖後……肯定很不願意回到孤單的生活吧」
Cũ: 「Đúng vậy nhỉ. Một khi đã biết đến hơi ấm này rồi——⏎thì việc phải trở lại một mình, thật sự, rất đáng sợ.」
Mới: 「Đúng vậy nhỉ. Một khi đã biết đến hơi ấm này rồi——⏎thì việc phải trở lại một mình, thật sự, rất khó chịu.」
Lý do: いやだ = "khó chịu/không muốn", không phải "đáng sợ" (đáng sợ = 怖い). TW 肯定很不願意回到孤單的生活吧 xác nhận nghĩa "không muốn".

**2313 [れいな]**
JP: 「ありますよぉ。いいこいいこってしててください」
TW: 「有呀，請摸摸我的頭吧」
Cũ: 「Có ạ~. Anh hãy vuốt ve em đi ạ」
Mới: 「Có ạ~. Anh hãy xoa đầu ngoan ngoan đi ạ」
Lý do: いいこいいこ = xoa đầu khen "bé ngoan" (TW 請摸摸我的頭吧), không phải "vuốt ve" chung chung. Chuẩn trong file: 2113 "xoa đầu ngoan ngoan", 2889 "xoa đầu ngoan ngoan".

**2545 [れいな]**
JP: 「そうてつさんが、⏎いいこいいこしてくれたおかげですよぉ」
TW: 「都是雙鐵先生的功勞，多虧你摸了我的頭」
Cũ: 「Tất cả là nhờ anh Soutetsu,⏎đã vuốt ve em đó ạ~」
Mới: 「Tất cả là nhờ anh Soutetsu,⏎đã xoa đầu ngoan ngoan cho em đó ạ~」
Lý do: Như 2313: いいこいいこしてくれた = "đã xoa đầu ngoan ngoan cho em" (TW 多虧你摸了我的頭).

**3056 [monologue]**
JP: れいなの声に、ゆえに乾きがまじり始める。⏎かわいい甘えと、小さな不満と、おんなの欲とが。
TW: 玲奈的嗓音開始有些發啞。混合著可愛的撒嬌，小小的不滿，還有身為女性的欲求。
Cũ: Giọng Reina, vì thế bắt đầu pha lẫn sự khô khát.⏎Sự nũng nịu đáng yêu, chút bất mãn nho nhỏ, và dục vọng của một người phụ nữ.
Mới: Giọng Reina, vì thế bắt đầu pha lẫn chút khàn khàn.⏎Sự nũng nịu đáng yêu, chút bất mãn nho nhỏ, và dục vọng của một người phụ nữ.
Lý do: 乾き trong giọng nói = khàn/khô giọng (TW 嗓音開始有些發啞 — giọng bắt đầu khàn), không phải "khô khát" (khát nước).

**3156 [monologue]**
JP: 赤ちゃんというか、ディフォルメされた童女な感じだ。⏎かわいらしいし、傷んでもいない。
TW: 與其說是小孩，更像是卡通化的小女孩。外形很可愛，也沒有傷痕。
Cũ: Nói là em bé thì đúng hơn là một bé gái được cách điệu hóa.⏎Rất đáng yêu, và cũng không bị trầy xước gì.
Mới: Chẳng phải em bé, mà đúng hơn là một bé gái được cách điệu hóa.⏎Rất đáng yêu, và cũng không bị trầy xước gì.
Lý do: 赤ちゃんというか、Y = "chẳng phải em bé, mà đúng hơn là Y" — bản cũ đảo chiều so sánh ("Nói là em bé thì đúng hơn là…" nghĩa là em bé đúng hơn). TW 與其說是小孩，更像是卡通化的小女孩 xác nhận chiều đúng.

### 3.5. Thuật ngữ (5 dòng)

**2118 [れいな]**
JP: 「だって、燃やされちゃったら、部品取りできなく⏎なっちゃいますよぉ。れいな、せっかくなら姉妹機に」
TW: 「因為被燒了就不能卸下部件了。玲奈覺得還不如留給姐妹機……」
Cũ: 「Tại vì, nếu bị đem đi hỏa táng, thì sẽ không thể tháo linh kiện ra⏎được nữa đâu ạ~. Nếu đã vậy thì, Reina thà để lại cho các chị em cùng dòng máy còn hơn」
Mới: 「Tại vì, nếu bị đem đi hỏa táng, thì sẽ không thể tháo linh kiện ra⏎được nữa đâu ạ~. Nếu đã vậy thì, Reina thà để lại cho các máy chị em còn hơn」
Lý do: 姉妹機 = "máy chị em" (máy móc cùng dòng), không phải "các chị em" (người). TW 姐妹機 xác nhận. "thà… còn hơn" giữ nguyên theo TW 還不如.

**2350 [れいな]**
JP: 「それでれいな、火葬して、おばけになるって。⏎でも――だけど、やっぱり部品は姉妹機に」
TW: 「然後玲奈就會被火化，變成妖怪。……但還是把部件留給姐妹機比較好吧」
Cũ: 「Nên là Reina, sẽ bị hỏa táng, rồi biến thành ma.⏎Nhưng——nhưng mà, quả nhiên linh kiện thì nên để lại cho các chị em」
Mới: 「Nên là Reina, sẽ bị hỏa táng, rồi biến thành ma.⏎Nhưng——nhưng mà, quả nhiên linh kiện thì nên để lại cho các máy chị em」
Lý do: Như 2118: 姉妹機 = "các máy chị em". Câu cụt theo đúng JP/TW (TW cũng hoàn thiện câu bằng 比較好吧) nên chỉ sửa danh từ.

**2535 [双鉄]**
JP: 「ならば、御一夜温泉駅で待ってみよう。⏎改札出口で、そのぬいぐるみと一緒にいれば」
TW: 「那我們就在御一夜溫泉站等等吧。帶著那個玩偶去檢票出口」
Cũ: 「Vậy thì, chúng ta hãy đợi ở ga Ohimitera Onsen xem sao.⏎Nếu ở cửa soát vé cùng với con thú bông đó」
Mới: 「Vậy thì, chúng ta hãy đợi ở ga Ohitoyo Onsen xem sao.⏎Nếu ở cửa soát vé cùng với con thú bông đó」
Lý do: Thuật ngữ đã chốt 19/11: 御一夜 = "Ohitoyo" (không "Ohimitera"/"Ohito"); tiền lệ nhiều file đã sửa trong file.

**2797 [monologue]**
JP: が――まさか御一夜にまで、⏎こうも早くに伝播してくるとは思わなかった。
TW: 但是我完全沒想到，居然這麼快就傳播到御一夜這裡了。
Cũ: Nhưng——không ngờ đến cả Ohimitera,⏎mà nó lại lan truyền nhanh đến vậy.
Mới: Nhưng——không ngờ đến cả Ohitoyo,⏎mà nó lại lan truyền nhanh đến vậy.
Lý do: Thuật ngữ đã chốt 19/11: 御一夜 = "Ohitoyo".

**3118 [monologue]**
JP: 御一夜鉄道の、御一夜市の知名度アップを計るため、⏎日々姫主導で作り始めた小冊子。
TW: 由日日姬主導，為了團結御一夜鐵路、御一夜市而製作的小冊子。
Cũ: Để nâng cao độ nhận diện của Đường sắt Ohito, của thành phố Ohimitera,⏎cuốn sách nhỏ được bắt đầu thực hiện dưới sự dẫn dắt của Hibiki.
Mới: Để nâng cao độ nhận diện của Đường sắt Ohitoyo, của thành phố Ohitoyo,⏎cuốn sách nhỏ được bắt đầu thực hiện dưới sự dẫn dắt của Hibiki.
Lý do: Thuật ngữ đã chốt 19/11: 御一夜 = "Ohitoyo" (cả 2 chỗ trong dòng: "Đường sắt Ohito" và "thành phố Ohimitera").

### 3.6. Xưng hô (2 dòng)

**3028 [monologue]**
JP: れいなの方が、よほど僕より詳しいようだ。⏎ならば、要点だけ伝えよう。
TW: 玲奈好像比我還了解。那我就挑重點說吧。
Cũ: Có vẻ như Reina, còn rành hơn cả tôi nữa.⏎Vậy thì, anh sẽ chỉ truyền đạt những điểm chính thôi.
Mới: Có vẻ như Reina, còn rành hơn cả tôi nữa.⏎Vậy thì, tôi sẽ chỉ truyền đạt những điểm chính thôi.
Lý do: Độc thoại Soutetsu tự xưng "anh" → "tôi" (quy tắc độc thoại: "tôi", chỉ "mình" khi tự vấn cảm xúc; tiền lệ nhiều file đã sửa độc thoại "anh"→"tôi"). Dòng này là suy nghĩ nội tâm ("要点だけ伝えよう"), không phải thoại với Reina.

**3188 [monologue]**
JP: ならば僕は、れいなの希望を、⏎なにがなんでも叶えよう。
TW: 那麼我無論如何，都要實現她的願望。
Cũ: Nếu đã vậy, nguyện vọng của Reina,⏎dù thế nào anh cũng sẽ thực hiện cho bằng được.
Mới: Nếu đã vậy, nguyện vọng của Reina,⏎dù thế nào tôi cũng sẽ thực hiện cho bằng được.
Lý do: Như 3028: độc thoại Soutetsu tự xưng "anh" → "tôi" (quyết tâm nội tâm "なにがなんでも叶えよう", không phải thoại với Reina).

### 3.7. Lỗi nhỏ (1 dòng)

**2925 [monologue]**
JP: ぷにぷにと、れいなのほっぺをつっつきまわす。⏎くすぐったがってきゃらきゃら笑って――
TW: 我戳了戳玲奈的臉蛋。她感覺癢癢的，哈哈笑了出來——
Cũ: Tôi chọc chọc vào đôi má mềm nắn bóp của Reina.⏎Cô bé nhột nhạt, cười khúc khích——
Mới: Tôi chọc chọc vào đôi má phúng phính của Reina.⏎Cô bé nhột nhạt, cười khúc khích——
Lý do: ぷにぷに = má phúng phính/mềm mại; "đôi má mềm nắn bóp" không phải tiếng Việt chuẩn (nắn bóp không làm tính từ cho má).

## 4. Những dòng đã kiểm tra và KHÔNG tính sai

- **2288 [双鉄] — CHƯA CHẮC CHẮN (1 dòng, không tính sai):** JP 「今年はハロウィンを開催するといっていたな」 — chủ ngữ của といっていた không ghi rõ; VN "Em nói là năm nay sẽ tổ chức Halloween đúng không" gán cho Reina. TW cũng không ghi chủ ngữ. Không xác định được từ file (thứ tự key không phải thứ tự truyện). Giữ nguyên VN cũ, chờ Hieu kiểm tra trong game.

- **2241 [双鉄] — 湯医 = "Yui" GIỮ NGUYÊN:** quyết định Yui/Yunoi vẫn chờ Hieu (tiền lệ nhiều file giữ "Yui"). Ghi nhận bằng chứng mới: JP dòng này mang furigana [ゆのい,1] trên 湯医 — thêm một bằng chứng cho đề xuất "Yunoi".

- **2000 [れいな] — "Fuyu" (ふゆっ) giữ nguyên:** quy tắc fa/fu chỉ bao ふぁ/ふあ/ふぇ/ふや, không bao ふゆ (tiền lệ Mayami: "Funyaa"/"Fuwaaaaaaaa"/"Nmyu" giữ nguyên).

- **2015 [れいな] — "Kyufu" (きゅふっ) giữ nguyên:** cả từ SFX La-tinh nguyên dạng, theo tiền lệ h6 ("Fukyun!"/"Hyau!" được giữ); chỉ sửa ふっ độc lập trong cùng dòng → "Phù".

- **2408 [れいな] — "Dribble dribble——cut in——shoot!" giữ nguyên:** JP là katakana tiếng Anh (ドリブル/カットイン/シュート), VN trả lại đúng dạng tiếng Anh gốc — trung thành với JP.

- **3083 "Pyokon" / 3269 "choro" giữ nguyên:** onomatopoeia La-tinh ngoài họ fa/fu, theo tiền lệ Mayami (chỉ sửa họ ふぁ/ふあ/ふぇ/ふや).

- **2403 [双鉄] — VN theo JP, không theo TW:** TW tự thêm "小穴一直在發抖" không có trong JP; VN "Tất cả đều nhỏ xíu, dễ thương lắm" theo đúng JP 「全てがこぶりで、あいらしい" — đúng, không tính sai.

- **2997 [monologue] — VN theo JP, không theo TW:** TW tự thêm "乳頭" (núm vú) vào câu về băng cá nhân; JP chỉ nói おまんこ; VN "Che kín hoàn toàn chỗ đó" theo đúng JP — đúng.

- **2118/2350 — "thà… còn hơn" / "nên để lại" giữ nguyên:** JP cụt câu (姉妹機に) nhưng TW hoàn thiện câu bằng 還不如/比較好吧, nên phần hoàn thiện có cơ sở TW — chỉ sửa danh từ 姉妹機.

- **1969 — "làm, tình——quan hệ" giữ nguyên:** cách diễn ngọng/lặp của Reina (せっ、くす――セックス) — "quan hệ" là từ đầy đủ sau khi nói lắp "làm, tình", không phải thừa.

- **2925 — chỉ sửa "mềm nắn bóp" → "phúng phính"** (tính lỗi nhỏ); phần còn lại của dòng đúng.

- **3012 [monologue] — "nụ cười rạng rỡ" giữ nguyên:** とろとろの笑顔 đã được diễn bằng động từ "tan chảy thành" trong cùng câu; tính từ "rạng rỡ" là diễn tự do, không sai nghĩa rõ ràng.

- **2899 [monologue] — "một lời kháng nghị bay thẳng vào mặt tôi" giữ nguyên:** chủ ngữ kháng nghị không ghi rõ trong JP (TW cho là miếng băng cá nhân); VN dịch sát JP, không bịa chủ ngữ.

- **2525/2541 [れいな] — "Cái từ đó" giữ nguyên:** そんなの ở đây chỉ từ xưng hô おまえ (cảnh bàn về cách gọi vợ-chồng), nên "cái từ đó" là đúng — khác với 1958 (chỉ ý tưởng cosplay) đã sửa thành "Cái kiểu đó á?".

- **Soutetsu thoại xưng "anh" với Reina: ĐÚNG, giữ nguyên** (Reina gọi "anh Soutetsu"; quy tắc "anh" với Reina đã chốt). Soutetsu độc thoại xưng "tôi" 40+ dòng; chỉ 3028/3188 lạc thành "anh" — đã sửa. Reina tự xưng "em" nhất quán; "chị Paulette"/"chị Fukami" nhất quán.

- **おまんこ → "chỗ đó" giữ nguyên toàn file:** cách nói giảm nhẹ nhất quán của dự án, không phải lỗi.

- **"Đường sắt Ohito"/"Ohimitera" ở các dòng ĐÚNG khác trong file:** sau khi sửa 2535/2797/3118, file không còn dạng cũ nào của 御一夜.

## 5. Lượt soát 2

Đọc lại toàn bộ 59 fix đối chiếu từng JP (+TW) lần thứ hai: **59 tổng / 59 tái kiểm chứng / 0 loại bỏ / 0 sửa lại.** Kiểm tra cơ học (difflib): mọi fix chỉ khác VN cũ ở chỗ sửa có chủ đích — 2 dòng có tỉ lệ thay đổi thấp (1890, 2456) đều là thay toàn bộ token SFX 1 từ, đúng thiết kế. Kiểm tra số lượng nguyên âm kéo dài: 1894 ふぁぁっ→"phàa" (2 âm a), 1983 ふやあああ→"Phuyaaaan" (4 âm a + ん), 1986 ふぁぁぁっん→"Phàaan" (3 âm a + ん; bản cũ thừa 1 âm a), 2454 ふあぁ→"Phùaa" (2 âm a), 2456 ふぁあっ→"Phàa" (2 âm a), 2458 ふあああぁぁぁ→"Phùaaaaaa" (6 âm a) + ふああ→"Phùaa" (2 âm a), 1990 はうぅぅぅ→"Hauuuu" (5 nguyên âm, đủ theo công thức 1 + số う/ぅ). JSON 59 khóa chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 59/59; khối TOML parse OK, 59 khóa, 0 sai lệch giá trị.

## 6. Khối TOML (đã kiểm chứng parse)

Khối TOML dưới đây parse được bằng tomllib, **59 key, 0 sai lệch giá trị so với JSON**. Quy tắc ký tự xuống dòng: giá trị fix nào chứa ký tự xuống dòng dạng backslash-n (2 ký tự, như trong JSON và trong TOML gốc) thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON. (46 lần backslash-n trong 59 fix.)

```toml
[script]
"1784" = "「Cùng nhau——cùng nhau——ưm——phù——\\nReina cũng——cùng nhau——muốn cùng nhau, ạ~」"
"1835" = "「Đến rồi——đang tới——phù——a——a!\\nNóng quá——nóng quá——của anh——Soutetsu」"
"1885" = "「Hya——a——ngoáy——vào——rồi\\n——ưm——phù——a——trong bụng——cọ, cọ」"
"1890" = "「Phuê」"
"1894" = "「Phuê? A——……phàa」"
"1936" = "「Ưm——phù——a——phần, đầu——ưm,\\nphần đỉnh, của——chỗ——to——thôi——」"
"1938" = "「Phuê——phuya」"
"1958" = "「Cái kiểu đó á?」"
"1962" = "「Ư——!」"
"1963" = "「Ư!!!」"
"1967" = "「A——Reina——tè, dầm——mất, rồi——\\nphù——a——vẫn——còn ra, nữa——phuya」"
"1969" = "「Phà……từ, phía sau——làm, tình——\\nquan hệ, sao ạ~?」"
"1976" = "「Ua——a——giật, giật——mất rồi——\\nphuê——a——sướng——sướng, quá——phù, a」"
"1978" = "「Hyaauun! Anh, Soutetsu——phùa\\n——Reina, sắp——sắp rồi!!」"
"1983" = "「Phuyaaaan! ——Phà, a, bây giờ cũng——\\nrung lên, ngực, đang run rẩy, mồ hôi, ướt nhẹp」"
"1986" = "「Hya! Ư! Phù! Cái này! Cái này!\\nTuyệt quá——ưm——hi——Phàaan!!!」"
"1990" = "「Hauuuu~Ư!!」"
"1999" = "「Hya——an——ưm——lưỡi——phần đầu, đang,\\nchạm, chạm——vào, Reina, cái đó, phà」"
"2000" = "「Fuyu——ưm——phù——a——hyu,\\nưm——a——anh Soutetsu——anh Soutetsu」"
"2001" = "「Hyau, ư——ưm——phùa——ưm——\\nmông——ưm——núm vú, nữa——phùa」"
"2004" = "「Hyan——ưm——phù——a——nữa đi,\\nnữa đi, ngực. Reina, tất cả——nữa đi~」"
"2005" = "「Nkyu——ư——a——phù——phần đỉnh\\n——núm, vú——tê rần, lên, rồi——phù, a」"
"2013" = "「Hyaun! Á——phù, á——Reina,\\nhậu môn——hậu môn, trở nên kỳ lạ mất rồi ạ~」"
"2015" = "「Kyufu——ưm! ~~~! Phù——ku——\\nưm——không được——vẫn, chưa——chỗ đó, chưa được」"
"2017" = "「Fumyuuuun! Hôn kìa——phù——\\nanh Soutetsu——hôn, chỗ, đó, kìa」"
"2022" = "「Ư!」"
"2040" = "「À, xin lỗi em——đây rồi, đây rồi! Nhìn này.」"
"2088" = "「Ehe, he~——Reina——được, khen——phù\\n——phù——a——vui, lắm——ạ~——ưm」"
"2099" = "「Ufufu~, Reina, sẽ biến thành\\ncô sói cái đó nha~. Gâu gâu. Awoooo~」"
"2104" = "「Ufufu~. Vậy thì anh hãy gọi cho đàng hoàng đi nhé.\\nNha? Mình·ơi」"
"2111" = "「Ufufu~, anh Soutetsu,\\ncũng cười tươi rạng rỡ rồi ạ~」"
"2118" = "「Tại vì, nếu bị đem đi hỏa táng, thì sẽ không thể tháo linh kiện ra\\nđược nữa đâu ạ~. Nếu đã vậy thì, Reina thà để lại cho các máy chị em còn hơn」"
"2134" = "「Ha——mãnh, liệt——quá——phù——n-a——\\nbụng, của——Rei, na——đang, quặn, lại」"
"2172" = "「Chỗ, đó——như tan, chảy——bám chặt, lấy\\n——phù——cọ——cọ xát——cùng, nhau」"
"2202" = "「Chầm chậm——chỗ, đó——bị, đào bới\\n——phù——a——chỗ——thắt, lại」"
"2263" = "「Đúng vậy nhỉ. Cứ buồn bã vì những chuyện chưa biết,\\nmà làm cho hiện tại mà mình biết rõ phải u sầu thì phí lắm ạ~!」"
"2276" = "「Đúng vậy nhỉ. Một khi đã biết đến hơi ấm này rồi——\\nthì việc phải trở lại một mình, thật sự, rất khó chịu.」"
"2313" = "「Có ạ~. Anh hãy xoa đầu ngoan ngoan đi ạ」"
"2350" = "「Nên là Reina, sẽ bị hỏa táng, rồi biến thành ma.\\nNhưng——nhưng mà, quả nhiên linh kiện thì nên để lại cho các máy chị em」"
"2451" = "「Phà——không được——chỗ, đó——vẫn chưa, được.\\nCùng nhau——với anh, Soutetsu——cùng, nhau」"
"2452" = "「Phù——lưỡi——lưỡi, sướng lắm ạ~——\\nưm——chỗ đó——tất cả——hãy liếm láp đi ạ」"
"2453" = "「Phù——a——Reina——tè dầm, mất——ưm,\\ntrực, tiếp——vào miệng——anh, Soutetsu」"
"2454" = "「Phùaa——ngực——núm vú——vuốt, vuốt——\\nxoa——xoa——ưm! Sướng, quá, ạ~」"
"2455" = "「Phuya——phù——anh Soutetsu」"
"2456" = "「Phàa」"
"2457" = "「Phùa……a……a……ya——ưm——\\nchỗ đó——tinh dịch——đang tràn——ra ngoài」"
"2458" = "「Phùaaaaaa——Reina, vào miệng——\\nanh Soutetsu——nkyu!? Phùaa——an!!」"
"2459" = "「Phù! A! Sướng, quá——sướng, quá.\\nƯm——a——ha——a——phù——a」"
"2535" = "「Vậy thì, chúng ta hãy đợi ở ga Ohitoyo Onsen xem sao.\\nNếu ở cửa soát vé cùng với con thú bông đó」"
"2545" = "「Tất cả là nhờ anh Soutetsu,\\nđã xoa đầu ngoan ngoan cho em đó ạ~」"
"2797" = "Nhưng——không ngờ đến cả Ohitoyo,\\nmà nó lại lan truyền nhanh đến vậy."
"2925" = "Tôi chọc chọc vào đôi má phúng phính của Reina.\\nCô bé nhột nhạt, cười khúc khích——"
"2972" = "Hút sạch cho đến những giọt nước tiểu cuối cùng——Ư!?"
"3028" = "Có vẻ như Reina, còn rành hơn cả tôi nữa.\\nVậy thì, tôi sẽ chỉ truyền đạt những điểm chính thôi."
"3056" = "Giọng Reina, vì thế bắt đầu pha lẫn chút khàn khàn.\\nSự nũng nịu đáng yêu, chút bất mãn nho nhỏ, và dục vọng của một người phụ nữ."
"3095" = "Reina xoay người lại và cúi xuống,\\ncái mông đáng yêu lộ ra hoàn toàn——Ư!!?"
"3118" = "Để nâng cao độ nhận diện của Đường sắt Ohitoyo, của thành phố Ohitoyo,\\ncuốn sách nhỏ được bắt đầu thực hiện dưới sự dẫn dắt của Hibiki."
"3156" = "Chẳng phải em bé, mà đúng hơn là một bé gái được cách điệu hóa.\\nRất đáng yêu, và cũng không bị trầy xước gì."
"3188" = "Nếu đã vậy, nguyện vọng của Reina,\\ndù thế nào tôi cũng sẽ thực hiện cho bằng được."
```

## Kết bài

File れいなh4_ふたりっきりのハロウィン.txt.toml (584 dòng) đã đọc toàn bộ từng dòng đối chiếu JP + TW: **59 dòng sai (10,1%)**, 1 dòng chưa chắc chắn (2288 — chủ ngữ といっていた không xác định được, giữ nguyên chờ Hieu kiểm tra trong game). Lỗi tập trung ở tiếng thở fa/fu La-tinh (34 dòng) và 3 tiếng cười bị diễn thành tiếng rên — đều là lỗi hệ thống đã có quy tắc chốt, sửa được tại chỗ. Không có lệch dòng, chuỗi xoay, nhiễm chéo, dòng chưa dịch hay key trùng. Bằng chứng mới cho quyết định đang chờ: 2241 mang furigana ゆのい trên 湯医 (ủng hộ "Yunoi"). Sau file này, tổng cộng **75 file / 3.992 dòng sai** (cơ sở 74 file / 3.933 + 59 file này).
