# Unification batch U15a — §4 gloss OPEN (G12/G15/G16) + §3 moan leftovers + standing leftovers

**Phạm vi:** 60 mục đã quyết / **418 dòng** trong 104 file. Gồm §4 gloss OPEN (G12/G15/G16), §3 moan leftovers (M18, M20, M21, M23, M24, M25, M26, M27, M28, M29, M32, M33, M34, M35, M36, M37, M38, M39, M40, M41, M42, M43, M44, M45, M46, M47, M48, M49, M50, M51, M52, M53, M54, M55, M56, M57, M59, M60, M61, M62, M63, M64, M65, M67, M69, M71, M72) và các standing leftovers (M3 scream boundary, Grand 11 2485, P03 1728, F-T56-1, M7 59 "Hự" follow-up, M15 ~154 split-form rows, HAS-RUN 126 rows, P07 2311 G1). U15b (flags sweep) và U16 (P1/P5) chạy song song — dòng nào trùng (file,key) với batch khác thì coordinator GHÉP khi gộp (xem §5).

**Nguồn:** CSV3 good-set (87.833 dòng; đã loại 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`), `audit-*-wrong.json` (9.243 mục), `moans/moan-*-wrong.json` (1.516 mục), các đợt unification đã gộp (2.698 dòng, theo thứ tự gộp — xem `queue.json` status=merged). Mọi dòng trong đợt này đều có trong CSV3 — không dòng nào phải lấy JP/old_vn từ TOML-2.

## 1. Phương pháp

- **Liệt kê:** script chỉ dùng để liệt kê/đếm/kiểm chứng (enumeration, counting, verification). Mọi giá trị fix đều do đọc JP (+TW + dòng kề) rồi viết tay; JP thắng TW. Không sửa bulk bằng script.
- **old_vn:** giá trị hiện tại theo thứ tự ưu tiên: fix unification đã gộp (theo thứ tự gộp) > fix moan > fix audit > VN của CSV3 good-set. Nguồn old_vn đợt này: CSV3 280 / audit 64 / moan 40 / unification đã gộp 34. Dòng nào 2 đợt gộp cùng chạm thì old_vn = fix gộp SAU, fix đợt này GHÉP lên trên (không ghi đè).
- **Chuẩn hóa khi so khớp:** CSV3 dùng khoảng trắng ideographic U+3000, JSON dùng khoảng trắng ASCII — so khớp sau khi chuẩn hóa U+3000→space cả 2 phía. 202 giá trị cur lưu newline thật (từ các layer audit/moan cũ); JSON đợt này chuẩn hóa về literal `\n` theo quy tắc của task (4 dòng trong đợt này: ハチロクh6 852/924/937/941). Các file wrong.json đã gộp trước đây có chứa newline thật (vd. U12a ハチロクh6 816) — quy tắc literal-`\n` áp dụng cho file đợt này.
- **Quy tắc chung:** một dòng = một cách diễn (VN hoặc romaji, không trộn) cho moan; công thức độ dài nguyên âm: tổng số mora Hepburn — khi mora gốc ĐÃ là nguyên âm thì KHÔNG đếm đôi (んう×6 = 6u, không phải 7u); ん không đóng góp nguyên âm (んうっ = 1u → "Nu"); tổng số chữ kéo dài = 1 + số う/ぅ/ー (M14). Token romaji SFX viết hoa ở mọi vị trí (F5). Cười là cười, không phải rên (Hieu 19/11 22:05).
- **Kiểm chứng cơ học:** (1) build script kiểm tra 418/418 mục: đủ 8 trường, key là string, jp/tw khớp CSV3 (modulo U+3000), old_vn khớp precedence map, 0 fix==old_vn, 0 newline thật, 0 `\\n` kép; (2) phân tích lại HAS-RUN bằng logic của scan `_u12b_mismatch.py` trên (JP, fix) — 98 token, chỉ còn 1 "lệch" đã giải thích (1860, xem §6); (3) kiểm tra M15 (0 dạng tách còn lại; số nguyên âm token dài đúng hết), M24 (0 token cười thường còn lại), M7 (mọi fix chứa "Ku"), G15 (0 markup [x,n] còn lại); (4) diff old_vn→fix cho toàn bộ 418 dòng — đọc từng diff, chỉ token cần sửa được đổi (xem §6); (5) khối TOML parse-verified 104 file / 418 key, 0 lệch.

## 2. Quyết định áp dụng

- **M7 くっ (F1, coordinator 22/11 ~11:30):** token đối thoại H-scene → "Ku". Đợt này áp dụng follow-up 59 dòng "Hự" còn lại của U12a — thực tế đếm lại được **60 dòng** (U12a bỏ sót lr_日々姫h2 1159 do có `\n` trước くっ). 7 dòng （ ） miêu tả và 15 dòng đối thoại non-H "hự" KHÔNG đổi trong đợt này (cờ §5). ふかみh2 989 "Kh" giữ (khóa Kh thắng M7).
- **M15 ん+phụ âm (F1):** H-scene → romaji 1 token (Nkyu/Nku/Nfu/Nhyu/Na/Nu/Ngu/Nbu/Npu/Ngyu/Nchu/Mugu; "Nnfu" cho んんふっ; "Nhyun"/"Nkyun" cho んひゅん/んきゅん). っ bỏ, không thêm Ư. Giữ: "Ưm, X" (dấu phẩy = khoảng nghỉ, không phải tách token), JP có 、/…… tách token (quy ước M16), ん(っ) trần → "ưm", んん → "nn"/"mm", ポーレットh4 878 ぅんっ→"ưn".
- **M24 token cười (Hieu 19/11 22:05 + F5):** んふふ→"Nfufu", うふふ→"Ufufu", ふふ→"Fufu" — viết hoa chữ đầu ở mọi vị trí. Trường hợp "Ưm fufu"/"ưm fufu" (JP んふふっ) GỘP thành "Nfufu" (không phải "Ưm Fufu"); うっふふ → "Ufufu". Token tách riêng (JP có ――/、) chỉ viết hoa, không gộp.
- **HAS-RUN (M14, U12b):** sửa số chữ kéo dài còn lệch sau U12b. Scan `_u12b_mismatch.py` có 3 lỗi hệ thống đã xác nhận: (1) target romaji dùng 1+marks, đếm thiếu gốc đa âm tiết (tổng đúng = nguyên âm gốc + marks); (2) tổng VN chỉ đếm chữ không dấu, đếm thiếu nguyên âm có dấu (ù/ộ…); (3) căn token theo vị trí nên có thể ghép sai (vd. 2536) hoặc nối token qua ―. Mọi mục đã kiểm tay lại theo quy tắc đúng trên CUR hiện tại (không dùng snapshot cũ của scan).
- **M3 (21/11 ~11:55):** chỉ áp dụng cho moan trong H-scene (ひゃ/ひゅ/ひあ/きゃ → romaji). Ranh giới scream: tiếng thét giật mình (きゃっ ngoài H-scene, nhất là ngạc nhiên phi tình dục) GIỮ "Á" — không mở rộng M3 sang 175 dòng scream non-H (xem §4).
- **G15 ruby [x,n]:** BỎ markup ruby ở mọi chỗ (quy ước của dự án: bỏ 306 lần vs giữ 14 lần). Engine render [x,n] thành furigana trên n ký tự sau, nên dòng VN không được chứa markup JP — kể cả dạng đã dịch trong ngoặc "[…]". Ngoại lệ duy nhất: 日々姫05 1909 (G16) — tag là cố ý của audit để giữ trò đùa 下→ゲ, giữ nguyên.
- **G12 %l gloss do VN thêm:** GIỮ hết — gloss giải thích đúng, TW cũng thêm tag trong trường hợp タブレット; các tag đã bị audit gỡ (ハチロク06) thì không còn gì để làm.
- **F5 (coordinator 22/11 ~12:50):** token romaji SFX viết hoa ở mọi vị trí (đầu dòng và giữa dòng) trong các fix MỚI. Sweep F5 rộng hơn thuộc về U15b; đợt này chỉ sửa 4 dòng được giao (lr_ニイロクh 1322/1387, lr_日々姫真闇h1 1445, 真闇h2 1084).

## 3. Bảng sửa theo mục
## 3.1. M7 — くっ đối thoại H-scene → "Ku" (60 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr_ふかみh1_ふかみうさぎのたまご | 1257 | 「っ――っ、くっ――ほぼ、間違いなく――\n膣内で――射精、してしまうのだがっ」 | 「唔……這樣下去……肯定會射在裡面的」 | 「Ư――Ư, hự——gần như, chắc chắn——\nanh sẽ——bắn tinh, vào bên trong mất thôi.」 | 「Ư――Ư, Ku——gần như, chắc chắn——\nanh sẽ——bắn tinh, vào bên trong mất thôi.」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_ふかみh1_ふかみうさぎのたまご | 1259 | 「っ！ くっ！！」 | 「唔！！」 | 「Ư! Hự!!」 | 「Ư! Ku!!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_ふかみh1_ふかみうさぎのたまご | 1307 | 「んっ――くっ――あ――。\n……一番、濃い、僕の匂いは――いったい、どんな」 | 「嗯……嗯啊……我最濃烈的味道……到底是……」 | 「Ưm——hự——a——.\n……Mùi hương, đậm nhất, của anh——rốt cuộc, là mùi như thế nào.」 | 「Ưm——Ku——a——.\n……Mùi hương, đậm nhất, của anh——rốt cuộc, là mùi như thế nào.」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_ポーレットh1_家族旅行の最終日の夜 | 1003 | 「ひゃうっ！？ あっ――んっ！ くっ――ふぁっ！\nんあっ！！」 | 「呀唔！？啊——嗯！咕——呼啊！嗯啊！！」 | 「Hyau!? A――ưm! Hự――Fa! Ưm a!!」 | 「Hyau!? A――ưm! Ku――Fa! Na!!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). GHÉP M7+M15: くっ→"Ku" và んあっ→"Na" trong 1 dòng (item M7). |
| lr_ポーレットh2_デコレーション＆ミルク | 1116 | 「んっ――んぷっ――ぷっ――くっ――んっ」 | 「嗯——嗯噗——噗——咕——嗯」 | 「Ưm——ưm bụp——bụp——hự——ưm」 | 「Ưm——ưm bụp——bụp——Ku——ưm」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_ポーレットh2_デコレーション＆ミルク | 1133 | 「んぷっ！？ ぷっ――くっ―\n―こほっ――うぇっ――ごくっ――んむっ」 | 「嗯噗！》噗——呃——咳咳——嘔——咕嘟——嗯唔」 | 「Ưm bụp!? Bụp——hự—— Khụ——uệ——ực——ưm mự」 | 「Ưm bụp!? Bụp——Ku—— Khụ——uệ——ực——ưm mự」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_凪h1_痛いの痛いの飛んでけばい | 1165 | 「ぁ……くっ――くはっ――こんな状況に陥れば――\n知能指数をどんどんと――精液に溶かすものなのだ」 | 「啊……唔……啊……陷入這種情況之後……感覺智商都化成精液了」 | 「A……hự――kuha――rơi vào tình huống thế này――\nchỉ số IQ sẽ dần dần――hòa tan vào tinh dịch mất」 | 「A……Ku――kuha――rơi vào tình huống thế này――\nchỉ số IQ sẽ dần dần――hòa tan vào tinh dịch mất」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_凪h1_痛いの痛いの飛んでけばい | 1305 | 「どう、ダメ――なの、だ？ んっ――くっ――あっ――\nおっぱいと――おまんこ、を――同時に、され、ると」 | 「會……怎麼廢掉？嗯……呃……啊……胸部和下面……同時被那什麼」 | 「Sao lại, không chịu nổi——chứ? Ưm——hự——a——\nKhi cả ngực——và cô bé——bị làm, cùng lúc, thì sao?」 | 「Sao lại, không chịu nổi——chứ? Ưm——Ku——a——\nKhi cả ngực——và cô bé——bị làm, cùng lúc, thì sao?」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_凪h2_虎さんの交尾 | 1215 | 「ん――くっ！ あっ！！」 | 「唔……呃！啊！！」 | 「Ưm——hự! A!!」 | 「Ưm——Ku! A!!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_凪h2_虎さんの交尾 | 1219 | 「くっ！」 | 「唔！」 | 「Hự!」 | 「Ku!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_凪h2_虎さんの交尾 | 1231 | 「くっ――うっ――」 | 「啊……唔……」 | 「Hự——ư——」 | 「Ku——ư——」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_凪h2_虎さんの交尾 | 1339 | 「勃起ちんちんを膣口にいれる――っ、くっ――\nこれで――あっている、かな？」 | 「將勃起的雞雞塞進去……唔，這樣做，沒錯吧？」 | 「Cho cậu nhỏ đang cương cứng vào cửa âm đạo——hự——\nThế này——đã đúng, chưa?」 | 「Cho cậu nhỏ đang cương cứng vào cửa âm đạo——Ư, Ku——\nThế này——đã đúng, chưa?」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_凪h2_虎さんの交尾 | 1373 | 「大丈夫だ――くっ――壊れる――ときはっ――\n僕も――一緒、だっ――」 | 「沒事。唔……到時候……我陪你……一起瘋掉」 | 「Không sao đâu——hự——khi nào hỏng——thì——\nanh cũng——sẽ hỏng cùng em——」 | 「Không sao đâu——Ku——khi nào hỏng——thì——\nanh cũng——sẽ hỏng cùng em——」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_凪ふかみh1_じぇいけい！ | 1395 | 「それほど――貪欲に――もとめず、ともっ――くっ！\n次の――精液が――もうっ――こみ、あげてっ――っ」 | 「你……沒必要……這麼貪心……唔！下次……射精……已經……快了……啊」 | 「Không cần——phải đòi hỏi——tham lam, đến vậy, đâu——hự!\nĐợt tinh dịch——tiếp theo——sắp——trào ra, rồi——」 | 「Không cần——phải đòi hỏi——tham lam, đến vậy, đâu——Ku!\nĐợt tinh dịch——tiếp theo——sắp——trào ra, rồi——」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_凪ふかみh1_じぇいけい！ | 1446 | 「凪をっ――受精――させたかも、しれんっ――くっ！\n精液、まみれの――性器をっ――そのっ、ままっ」 | 「凪可能受精了……唔！現在我將沾滿精液的傢伙……直接插入」 | 「Có khi anh——đã làm Nagi——thụ tinh, rồi cũng nên——hự!\nBộ phận sinh dục——đẫm, tinh dịch——cứ thế, mà cắm vào」 | 「Có khi anh——đã làm Nagi——thụ tinh, rồi cũng nên——Ku!\nBộ phận sinh dục——đẫm, tinh dịch——cứ thế, mà cắm vào」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_凪ふかみh1_じぇいけい！ | 1546 | 「いきなり、では、ない――ふかみもとっくに――\nこんなにっ――くっ――濡らして――どろどろ、でっ」 | 「哪裡突然了，你早就……濕成……唔……這個樣子了」 | 「Không hề, đột ngột, đâu——Fukami cũng từ lâu đã——\nướt đẫm——hự——nhớp nháp, thế này rồi, mà」 | 「Không hề, đột ngột, đâu——Fukami cũng từ lâu đã——\nướt đẫm——Ku——nhớp nháp, thế này rồi, mà」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_凪ふかみh1_じぇいけい！ | 1559 | 「くっ――ぁっ！」 | 「唔……啊！」 | 「Hự——a!」 | 「Ku——a!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_日々姫h2_デザートは食事の前に | 697 | 「……ァっ――くっ！」 | 「……唔！」 | 「……A——hự!」 | 「……A——Ku!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_日々姫h2_デザートは食事の前に | 948 | 「くっ――あっ――あっ！ あっ！！！」 | 「呃啊！！！」 | 「Hự——a——a! A!!!」 | 「Ku——a——a! A!!!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_日々姫h2_デザートは食事の前に | 968 | 「ん――くっ」 | 「唔……」 | 「Ưm——hự.」 | 「Ưm——Ku.」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_日々姫h2_デザートは食事の前に | 970 | 「と、いうか――くっ――あっ――僕も、だっ――」 | 「唔……我也很舒服……」 | 「Mà phải nói là——hự——a——anh cũng, thế——」 | 「Mà phải nói là——Ku——a——anh cũng, thế——」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr_日々姫h2_デザートは食事の前に | 1159 | 「生命、の――危機に――瀕して、いる、ならっ――\nくっ――生物、は――本能、として――子孫、を――」 | 「瀕臨……生命危機的時候……唔……生物……就會依照本能……留下後代」 | 「Nếu đang, đứng trước——nguy hiểm——đến tính, mạng——\nHự——thì sinh vật——theo bản, năng——sẽ muốn để lại, hậu duệ——」 | 「Nếu đang, đứng trước——nguy hiểm——đến tính, mạng——\nKu——thì sinh vật——theo bản, năng——sẽ muốn để lại, hậu duệ——」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). U12a bỏ sót do có \n trước くっ; dòng này là dòng thứ 60 (F1 ghi 59). |
| lr稀咲追加h_お風呂は日ノ本式に限るね | 778 | 「――っ――くっっ――妊娠、する――にはっ」 | 「——啊——唔——為了——讓你懷孕」 | 「——Ư——Hự——Để, mang thai——thì.」 | 「——Ư——Ku——Để, mang thai——thì.」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr稀咲追加h_お風呂は日ノ本式に限るね | 780 | 「――っ――くっ――ぁっ――ぉっ」 | 「——嗯——呼——啊——啊」 | 「——Ư——Hự——A——O.」 | 「——Ư——Ku——A——O.」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr稀咲追加h_お風呂は日ノ本式に限るね | 1130 | 「くっ！」 | 「啊！」 | 「Hự!」 | 「Ku!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr稀咲追加h_お風呂は日ノ本式に限るね | 1148 | 「ん……くっ」 | 「嗯……唔」 | 「Ưm…… Hự.」 | 「Ưm…… Ku.」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1801 | 「くっ！ んっ！！！」 | 「唔！嗯！！！」 | 「Hự! Ưm!!!」 | 「Ku! Ưm!!!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1802 | 「くっ！！！！」 | 「唔！！！！」 | 「Hự!!!!」 | 「Ku!!!!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| れいなh1_おかあさんのレッスン | 1528 | 「ふあっ――あっ――\nんっ――くっ――」 | 「蛤啊……啊……啊嗯……」 | 「Fua――a――\nƯm――hự――」 | 「Fua――a――\nƯm――Ku――」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| ハチロクh1_契り | 1239 | 「くっ――あっ――」 | 「唔——啊——」 | 「Hự——a——」 | 「Ku——a——」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| ハチロクh3_磨き洗い | 1089 | 「おちんちんの、先は――なっ――くっ、あ――\n亀頭と――、一般には、言う――そう、だっ」 | 「小雞雞的，前頭——嗯，啊——龜頭——就是一般稱呼——嗎」 | 「Phần đỉnh, của cậu bé——là——hự, a——\ngọi là——quy đầu——người ta thường nói, vậy đấy」 | 「Phần đỉnh, của cậu bé——là——Ku, a——\ngọi là——quy đầu——người ta thường nói, vậy đấy」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| ポーレットh1_ファーストセックス | 1027 | 「ん……くっ」 | 「嗯……唔」 | 「Ưm... hự.」 | 「Ưm... Ku.」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| ポーレットh2_制服変更？ | 909 | 「もう――少し――くっ――あっ――\nイクなら――、一緒にっ――」 | 「再等一會——呃——啊——要丟的話——就一起——」 | 「Một chút——nữa thôi——hự——á——\nNếu ra——, thì cùng nhau——」 | 「Một chút——nữa thôi——Ku——á——\nNếu ra——, thì cùng nhau——」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| ポーレットh2_制服変更？ | 978 | 「ぉ――くっ――」 | 「啊——呃——」 | 「Ồ——hự——」 | 「Ồ——Ku——」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| ポーレットh4_クリーム＆クリーム | 892 | 「くっ――っ――」 | 「呃——啊——」 | 「Hự——Ư——」 | 「Ku——Ư——」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| ポーレットh4_クリーム＆クリーム | 894 | 「くっ！」 | 「呃！」 | 「Hự!」 | 「Ku!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| ポーレットh4_クリーム＆クリーム | 921 | 「くっ――んっ」 | 「唔——嗯」 | 「Hự——ưm」 | 「Ku——ưm」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| ポーレットh4_クリーム＆クリーム | 951 | 「っ――くっ――」 | 「嗯——唔——」 | 「Ư——hự——」 | 「Ư——Ku——」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| ポーレットh5_裸エプロンのレモンドレッシング和え | 1003 | 「ポーレット！ もっとだ――くっ！\nもっと――深く、にっ」 | 「波萊特！更深一點！更深的地方」 | 「Paulette! Nữa đi——hự!\nHơn nữa——vào sâu, hơn nữa」 | 「Paulette! Nữa đi——Ku!\nHơn nữa——vào sâu, hơn nữa」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| ポーレットh7_残業エッチもyシャツで | 900 | 「う――くっ」 | 「嗯——唔」 | 「Ư——hự」 | 「Ư——Ku」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| ポーレットh8_気動車の国のアリス | 2241 | 「はきゅっ！？ くっ――ふうううううっ」」 | 「啊呀！？啊——呼啊」 | 「Hakyu!? Hự——phuuuuuu」 | 「Hakyu!? Ku——phuuuuuu」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7).  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| ポーレットh8_気動車の国のアリス | 2273 | 「ん――くっ――」 | 「嗯——唔——」 | 「Ưm——hự——」 | 「Ưm——Ku——」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| ポーレットh8_気動車の国のアリス | 2275 | 「ん――くっ――（ごくっ）」 | 「嗯——唔——（嚥下）」 | 「Ưm——hự——（ực）」 | 「Ưm——Ku——（ực）」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 凪ふかみh1_修学旅行の夜 | 1229 | 「ん……くっ――」 | 「呃……」 | 「Ưm……hự――」 | 「Ưm……Ku――」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 凪ふかみh1_修学旅行の夜 | 1230 | 「っ――くっ」 | 「呃……呃」 | 「Ư——hự」 | 「Ư——Ku」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h3_汚れてしまった制服で | 1037 | 「ひゃはっ！？ あっ――あっ――は――くっ――」 | 「呀！？啊――啊――呼――呃――」 | 「Hyaha!? A――a――Hà――hự――」 | 「Hyaha!? A――a――Hà――Ku――」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h3_汚れてしまった制服で | 1108 | 「んっ――くっ――あっ――\n日々姫！ 日々姫！ 日々姫！！」 | 「嗯――呃――啊――日日姬！日日姬！日日姬！！」 | 「Ưm――hự――a――\nHibiki! Hibiki! Hibiki!!」 | 「Ưm――Ku――a――\nHibiki! Hibiki! Hibiki!!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h5_白濁絵の具の射精会 | 1163 | 「っ――くっ！」 | 「呃――！」 | 「Ư――hự!」 | 「Ư――Ku!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h5_白濁絵の具の射精会 | 1166 | 「くっ――っ！」 | 「呃！」 | 「Hự――!」 | 「Ku――!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h5_白濁絵の具の射精会 | 1171 | 「けふっ――えほっ――む、くっ――ふ――んっ！！\nフッ――ちゅろっ、じゅるっ！ じゅろっ！ じゅぶっ」 | 「呼――咳――唔――呼――嗯！！呼――啾嚕、啾嚕！啾嚕！啾嚕」 | 「Kefu――eho――ưm, hự――phù――ưm!!\nPhù――chụt, chùn chụt! Chụt! Chùn chụt」 | 「Kefu――eho――ưm, Ku――phù――ưm!!\nPhù――chụt, chùn chụt! Chụt! Chùn chụt」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h5_白濁絵の具の射精会 | 1187 | 「ふ……ふぁ……ん――にぃにの――お筆っ――\nん……はっ――熱く、て――んっ――くっ！」 | 「呼……呼……嗯――阿哥的――畫筆――嗯……呼――熱熱的――嗯――唔！」 | 「Phù……Fa……ưm――Chiếc cọ――của anh hai――\nƯm……hà――Nóng, quá――ưm――hự!」 | 「Phù……Fa……ưm――Chiếc cọ――của anh hai――\nƯm……hà――Nóng, quá――ưm――Ku!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h5_白濁絵の具の射精会 | 1190 | 「ふあ……ぁ……ア……ん……くっ――あ――\nはぁっ――はあっ――はあっ……ふ、ぁ――あっ」 | 「呼……啊……啊……嗯……唔――啊――呼――呼――呼……呼、啊――啊」 | 「Fua……a……a……ưm……hự――a――\nHà――hà――hà……Fu, a――a」 | 「Fua……a……a……ưm……Ku――a――\nHà――hà――hà……Fu, a――a」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h5_白濁絵の具の射精会 | 1202 | 「くっ――」 | 「唔――」 | 「Hự――」 | 「Ku――」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h5_白濁絵の具の射精会 | 1219 | 「くっ！！？」 | 「啊！！？」 | 「Hự!!?」 | 「Ku!!?」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h5_白濁絵の具の射精会 | 1241 | 「ん――ん――くっ！ むっ――あっ――んむ～ん……\nん――んんっ――ふっ――んっ――ん～～～っ」 | 「嗯――嗯――唔！唔――啊――嗯唔～嗯……嗯――嗯嗯――呼――嗯――嗯～～～」 | 「Ưm――ưm――hự! Ưm――a――ưm mu~n……\nƯm――ưm ưm――phù――ưm――ưm~~~」 | 「Ưm――ưm――Ku! Ưm――a――ưm mu~n……\nƯm――ưm ưm――phù――ưm――ưm~~~」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h5_白濁絵の具の射精会 | 1249 | 「ん……くっ――」 | 「嗯……唔――」 | 「Ưm……hự――」 | 「Ưm……Ku――」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h5_白濁絵の具の射精会 | 1353 | 「どう、 ――おちんぽ、が――くっ――\nすごい――ん――だ？」 | 「雞雞――怎麼個――厲害法？」 | 「Chim, của anh――hự――\ntuyệt――ưm――như thế nào?」 | 「Chim, của anh――Ku――\ntuyệt――ưm――như thế nào?」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h6_オリエンテーリング借り物競走（ペア） | 2138 | 「ぇえっ――ゆっくり――ん……くっ――\nは、あっ――ん――ふあっ！」 | 「哎――慢慢的――嗯……唔――呼、啊――嗯――呼啊！」 | 「Ể――từ từ――ưm……hự――\nHà, a――ưm――Fua!」 | 「Ể――từ từ――ưm……Ku――\nHà, a――ưm――Fua!」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h6_オリエンテーリング借り物競走（ペア） | 2240 | 「んっ――くっ――ごくっ――ん――ずううっ――\nちゅっ――ちゅむっ――ごくっ」 | 「嗯――唔――咕――嗯――噗滋――啾――啾嚕――咕嚕」 | 「Ưm――hự――ực――ưm――chụt――\nChụt――chùn chụt――ực」 | 「Ưm――Ku――ực――ưm――chụt――\nChụt――chùn chụt――ực」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |
| 日々姫h6_オリエンテーリング借り物競走（ペア） | 2709 | 「に――にぃにの――ンッ――くい、こんで――\nきて――ふあっ――あっ……くっ――ふぅっ」 | 「阿――阿哥――嗯――陷進來了――呼啊――啊……唔――呼」 | 「A――Của anh hai――ưm――lún sâu, vào――\nrồi――Fua――a……hự――phù」 | 「A――Của anh hai――ưm――lún sâu, vào――\nrồi――Fua――a……Ku――phù」 | くっ đối thoại H-scene → "Ku" (quyết F1/M7). |

## 3.2. M15 — ん+phụ âm H-scene → romaji (113 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr_ふかみh1_ふかみうさぎのたまご | 1277 | 「んひゅんっ！！！」 | 「啊啊啊！！！」 | 「Ưm hyun!!!」 | 「Nhyun!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ふかみh1_ふかみうさぎのたまご | 1304 | 「んきゅううっ！！」 | 「嗚嗚嗚！！」 | 「Ưm kyuuu!!」 | 「Nkyuuu!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んきゅ+う×2 → 3u. |
| lr_ふかみh1_ふかみうさぎのたまご | 1305 | 「んきゅっ！！！」 | 「嗚！！！」 | 「Ưm kyu!!!」 | 「Nkyu!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ふかみh2_セックスの意味 | 1126 | 「んひゅううううううううううううううっっっっっ！！」 | 「嗚嗚嗚嗚嗚！！」 | 「Ưm hyuuuuuuuuuuuuuuuƯƯƯƯƯ!!」 | 「Nhyuuuuuuuuuuuuuuu!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んひゅ+う×14 → 15u; bỏ 5 Ư cuối (っ không render trong token romaji). |
| lr_ふかみh2_セックスの意味 | 1220 | 「お手入れ、ちゃあんと――出来て、いる、のか――\n双鉄、おにいさんに――確かめて――ほしっ――んあ！」 | 「有沒有……做好保養……雙鐵哥哥就來……確認一下吧……啊嗯！」 | 「Bảo dưỡng, cẩn thận——đã làm, xong chưa——\nmuốn anh Soutetsu——kiểm tra, giúp em——ưm a!」 | 「Bảo dưỡng, cẩn thận——đã làm, xong chưa——\nmuốn anh Soutetsu——kiểm tra, giúp em——Na!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ニイロクh_誓い。約束 | 1354 | 「んあっ！！？」 | 「嗯啊！！？」 | 「Ưm a!!?」 | 「Na!!?」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ハチロクh2_新しい服。新しい旅 | 1496 | 「んひゅうううううううっっっっ！！！」 | 「嗯嗚————！！！」 | 「Ưm hyuuuuuuu!!!!」 | 「Nhyuuuuuuuu!!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ハチロクh3_通販失敗いたしましたにゃん | 1195 | 「ひゃうっ！ ひゃっ！ ぃっ！ そうへふ、はわっ\nあっ！ んぐっ！ ひへっ――きてっ――んきゅう」 | 「呀！呀！嗯！雙鐵，少爺，啊！嗯嗚！啊，射吧……嗯嗚」 | 「Hyau! Hya! I! Ngài Soutetsu, hawa\nA! Ưm gu! Hihe——đến đây——ưm kyuu」 | 「Hyau! Hya! I! Ngài Soutetsu, hawa\nA! Ngu! Hihe——đến đây——Nkyuu」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ハチロクh3_通販失敗いたしましたにゃん | 1197 | 「ひあっ！ あっ！ んんっ！ んあっ！\nあっ！ あっ！ あっ！ あああっ！！！」 | 「呀！啊！嗯嗯！嗯啊！啊！啊！啊！啊啊啊！！！」 | 「Hya! A! Ưm! Ưm a!\nA! A! A! Aaa!!!」 | 「Hya! A! Ưm! Na!\nA! A! A! Aaa!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ハチロクh3_通販失敗いたしましたにゃん | 1199 | 「ひあっ！ んっ！ んきゅっ！ ふあっ！\nわらく、ひっ、すず、はっ！ すずはっ！ もうっ――」 | 「呀！嗯！嗯嗚！呼啊！我，我已經！我已經，不行——！」 | 「Hya! Ưm! Ưm kyu! Fua! Em, Suzu, ha! Suzu! Hết——」 | 「Hya! Ưm! Nkyu! Fua! Em, Suzu, ha! Suzu! Hết——」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ポーレットh1_家族旅行の最終日の夜 | 1096 | 「んきゅっ――ふぁっ――あっ、これ――しゅきっ――\nっっ――ふっ――ねっ――このまま――もっと」 | 「嗯呀——呼啊——啊，這個——好棒——唔——呼——來——就這樣——繼續」 | 「Ưm kyu——Fa——a, thế này——thích quá—— ư ư——Phu——nè——cứ thế này——nữa đi」 | 「Nkyu——Fa——a, thế này——thích quá—— ư ư——Phu——nè——cứ thế này——nữa đi」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ポーレットh1_家族旅行の最終日の夜 | 1097 | 「んきゅっ！！？」 | 「嗯呀！！？」 | 「Ưm kyu!!?」 | 「Nkyu!!?」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ポーレットh1_家族旅行の最終日の夜 | 1184 | 「そん、なに……っ――はっ――あっ――んっ――\nんふっ――きもち……いい……です、か？――ぁ」 | 「有這麼……哈——啊——嗯——嗯呼——舒服……嗎？——啊」 | 「Đến, mức đó……ưm――hà――a――ưm―― Ưm phù――sướng……lắm……sao?――a」 | 「Đến, mức đó……ưm――hà――a――ưm―― Nfu――sướng……lắm……sao?――a」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ポーレットh2_デコレーション＆ミルク | 1024 | 「ふあっ！ あっ！ あっ！ あっ！ ちょっ！ んあ！\nまっ――あっ――んぁっ！ ふぁああっっ！！！」 | 「呼啊！啊！啊！啊！等！嗯啊！一下——啊－嗯啊！呼啊啊啊！！！」 | 「Fua! A! A! A! Khoan! Ưm a!\nKhoan đã——a——ưm a! Faaa!!!」 | 「Fua! A! A! A! Khoan! Na!\nKhoan đã——a——Na! Faaa!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ポーレットh2_デコレーション＆ミルク | 1079 | 「ぁ――ぁ――ぁ――んっ――ね？ そうてつ、くん――\nそうてつ――くぁ――ふっ――んっ――んうっ！」 | 「啊——啊——啊——嗯——我說，雙鐵君——雙鐵——君——唔——嗯——嗯唔！」 | 「A——a——a——ưm——nè? Anh Soutetsu——\nanh Soutetsu——a——phu——ưm——ưm uu!」 | 「A——a——a——ưm——nè? Anh Soutetsu——\nanh Soutetsu——a——phu——ưm——Nu!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んうっ = 1u → "Nu" (ん không đóng góp nguyên âm). |
| lr_ポーレットh2_デコレーション＆ミルク | 1124 | 「んきゅうっ！！ ん～～～～～～～～～～～っ！！」 | 「嗯呀！！嗯～～～～～～～！！」 | 「Ưm kyuu!! Ưm～～～～～～～～～～～Ư!!」 | 「Nkyuu!! Ưm～～～～～～～～～～～Ư!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ポーレットh2_デコレーション＆ミルク | 1125 | 「んきゅんっ！！！」 | 「嗯呀！！！」 | 「Ưm kyun!!!」 | 「Nkyun!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ポーレットh2_デコレーション＆ミルク | 1127 | 「んふっ！！！」 | 「嗯呼！！！」 | 「Ưm phù!!!」 | 「Nfu!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_ポーレットh2_デコレーション＆ミルク | 1131 | 「んうううっ！」 | 「嗯唔唔唔！」 | 「Ưm uu u!」 | 「Nuuu!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んうううっ = 3u → "Nuuu". |
| lr_ポーレットh2_デコレーション＆ミルク | 1299 | 「双鉄くん！ んあっ！！！？」 | 「雙鐵君！嗯啊！！！？」 | 「Anh Soutetsu! Ưm a!!!?」 | 「Anh Soutetsu! Na!!!?」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_凪h1_痛いの痛いの飛んでけばい | 1158 | 「んくっ！ ふあ――あっ――んっ――（はむっ！）\nじゅるっ――ちゅぶっ！ じゅる！ じゅばっ！！」 | 「唔！啊……啊……嗯……（含！）啾……啾！啾！啾！！」 | 「Ưm ku! Fua――á――ưm――（Ngoạm!）\nJuru――chụt! Juru! Juba!!」 | 「Nku! Fua――á――ưm――（Ngoạm!）\nJuru――chụt! Juru! Juba!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_凪h1_痛いの痛いの飛んでけばい | 1159 | 「んくっ！ んっ――\nごきゅっっ！ ごくっ！ ごくっ！ こくんっ！」 | 「唔！嗯……咕咚，咕咚！咕咚！咕咚！」 | 「Ưm ku! Ưm――\nGokyu! Ực! Ực! Ực!」 | 「Nku! Ưm――\nGokyu! Ực! Ực! Ực!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_凪h1_痛いの痛いの飛んでけばい | 1162 | 「んくっ！？ ぷっ――ふぁっ――ンッ――じゅる！\nじゅぼっ！ じゅぶっ！ じゅばっ！ ちゅううっ」 | 「唔？！噗……啊……嗯……啾！啾！啾！啾！啾」 | 「Ưm ku!? Pu――Fa――ưm――Juru!\nJubo! Jubu! Juba! Chụụụt」 | 「Nku!? Pu――Fa――ưm――Juru!\nJubo! Jubu! Juba! Chụụụt」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_凪h1_痛いの痛いの飛んでけばい | 1240 | 「んっ！ んくっ！ ごくっ！ こくっ！！！」 | 「嗯！唔！咕咚！咕咚！！！」 | 「Ưm! Ưm ku! Ực! Ực!!!」 | 「Ưm! Nku! Ực! Ực!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_稀咲ポーレットh1_悪い大人の契約 | 1546 | 「あ―平気―あのっ―んふっ―あっ！！！」 | 「啊——沒事——那個——嗯嗚——啊！！！」 | 「A——không sao——cái đó——ưm fu——a!!!」 | 「A——không sao——cái đó——Nfu——a!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_稀咲ポーレットh1_悪い大人の契約 | 1617 | 「んぐっ！！！！！」 | 「嗯咕！！！！！」 | 「Ưm gu!!!!!」 | 「Ngu!!!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_稀咲ポーレットh1_悪い大人の契約 | 1620 | 「んくっ！」 | 「嗯嗚！」 | 「Ưm ku!」 | 「Nku!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_稀咲ポーレットh1_悪い大人の契約 | 1621 | 「んくっ！！」 | 「嗯嗚！！」 | 「Ưm ku!!」 | 「Nku!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_稀咲ポーレットh1_悪い大人の契約 | 1622 | 「んくっ！！！」 | 「嗯嗚！！！！」 | 「Ưm ku!!!」 | 「Nku!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_稀咲ポーレットh1_悪い大人の契約 | 1677 | 「僕も―ぁっっ―くっ―んふっ―了解だ」 | 「我也——啊——嗚——嗯嗚——明白」 | 「Tôi cũng——a——ku——ưm fu——hiểu rồi.」 | 「Tôi cũng——a——ku——Nfu——hiểu rồi.」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr_稀咲ポーレットh1_悪い大人の契約 | 1712 | 「わらひっ！ わたしも、双鉄くん―んあっ！！\nあっ！ だから―きて、きて、きてっ！ きてっ！！」 | 「我！ 我也、雙鐵君——嗯啊！！啊！ 所以——來吧、來吧、來吧！ 來吧！」 | 「Ehm! Em cũng vậy, anh Soutetsu——ưm a!! A! Nên là——vào đi, vào đi, vào đi! Vào đi!!」 | 「Ehm! Em cũng vậy, anh Soutetsu——Na!! A! Nên là——vào đi, vào đi, vào đi! Vào đi!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1677 | 「ひゃうううっ！ しゅご、いっ──んうっ！！！\nおなか──おまたっ──ごちゅって、かき回されてっ」 | 「呀唔唔！好厲害——嗯唔！！！肚子裡面——胯部裡面——被頂來頂去的」 | 「Hyauuu! Tuyệt, quá── ưm u!!!\nBụng── vùng kín── bị đâm vào, bị khuấy đảo」 | 「Hyauuu! Tuyệt, quá── Nu!!!\nBụng── vùng kín── bị đâm vào, bị khuấy đảo」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んうっ = 1u → "Nu". |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1777 | 「はっ……あっ──にぃに──にぃにっ──\nそぎゃん、ずうっと──クリ、ばっかり──んあっ」 | 「哈……啊——阿哥——阿哥——你一直摸陰核的話——嗯啊」 | 「Hà…… a── anh hai── anh hai──\nCứ thế, mãi── chỉ có âm vật── ưm aƯ」 | 「Hà…… a── anh hai── anh hai──\nCứ thế, mãi── chỉ có âm vật── Na」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んあっ→"Na"; bỏ Ư cuối. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1786 | 「はうっ！ あっ！ あっ！ あああっ！\nふあ──っ──んっ！ んううううっ！！！」 | 「哈嗚！啊！啊！啊啊啊！呼啊——嗯！嗯唔唔！！！」 | 「Hau! A! A! Aaa! Fua──Ư──ưm! Ưm uuuu!!!」 | 「Hau! A! A! Aaa! Fua──Ư──ưm! Nuuuu!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んううううっ = 4u → "Nuuuu". |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1840 | 「ん……（ごくっ）んふっ──ふふっ。わかる？ みくろ。\nそれがセックス。男と女が、一番ふかくつながる方法」 | 「嗯……（咽口水）嗯呼——呼呼。明白了嗎？美玖路。這個就叫做愛。也是男女在身體深處互相結合的方法」 | 「Ưm…… （Ực） Ưm fu──fufu. Em hiểu chưa? Mikuro.\nĐó chính là làm tình. Cách kết nối sâu sắc nhất giữa đàn ông và phụ nữ.」 | 「Ưm…… （Ực） Nfu──Fufu. Em hiểu chưa? Mikuro.\nĐó chính là làm tình. Cách kết nối sâu sắc nhất giữa đàn ông và phụ nữ.」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. GHÉP M15+M24: んふっ→"Nfu" và ふふっ→"Fufu" trong 1 dòng (item M15). |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1853 | 「んふっ──ん……ふっ──うぇ──べとおおおぉぉっ」 | 「嗯呼——嗯……呼——滋溜」 | 「Ưm fu──ưm……fu──uê──liếmmmmm」 | 「Nfu──ưm……fu──uê──liếmmmmm」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1855 | 「んひゅううううううううっっっっ！」 | 「嗯唔唔——！」 | 「Ưm Hyuuuuuuuuu!」 | 「Nhyuuuuuuuuu!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んひゅ+う×8 → 9u. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1857 | 「んきゅ！ ふあっ！ あ──ずりゅって──ずる、って──やぁぁあっ──にぃに──ぜんぶ、いっちゃうぅ」 | 「嗯唔！呼啊！啊——滋溜——滋嚕的好大聲——呀啊啊啊——阿哥——全都進來了」 | 「Ưm kyu! Fua! A── trượt── tuột, ra── Aaaa── anh hai── vào hết, mất」 | 「Nkyu! Fua! A── trượt── tuột, ra── Aaaa── anh hai── vào hết, mất」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1858 | 「んきゅっ！！！」 | 「嗯唔！！！」 | 「Ưm kyu!!!」 | 「Nkyu!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1859 | 「んひゅ！？ はうっ！ あたった、ときに──\nぐりって──され、るの──好きっ──みくろっ」 | 「嗯唔？！哈唔！頂進來的時候，攪弄的感覺非常舒服，美玖路很喜歡」 | 「Ưm hyu!? Hau! Khi, chạm vào──\nBị cọ xát── Mikuro── thích lắm──」 | 「Nhyu!? Hau! Khi, chạm vào──\nBị cọ xát── Mikuro── thích lắm──」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1865 | 「んきゅうっ！！！ ひゅあっ！ あっ！ あっ！！\n回路っ──いま──みくろ、一瞬──焼けた、みたいに」 | 「嗯嗚！！！嗯啊！啊！啊！！電路剛剛就好像一瞬間被燒斷了一樣」 | 「Ưm kyuu!!! Hyua! A! A!!\nMạch điện── vừa nãy── Mikuro, trong chốc lát── như bị, cháy vậy」 | 「Nkyuu!!! Hyua! A! A!!\nMạch điện── vừa nãy── Mikuro, trong chốc lát── như bị, cháy vậy」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1866 | 「んきゅうううううううううううううっ！！！！！！！」 | 「嗯嗚！！！！！！」 | 「Ưm kyuuuuuuuuuuuuuu!!!!!!!」 | 「Nkyuuuuuuuuuuuuuu!!!!!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んきゅ+う×13 → 14u. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1868 | 「はいっ！ はいっ！ みくろ、動いてほしいです──\nんうっ！！！」 | 「嗯！好！美玖路也想讓雙鐵先生動起來——嗯唔！！！」 | 「Vâng ạ! Vâng ạ! Mikuro, muốn anh cử động ạ──\nƯm u!!!」 | 「Vâng ạ! Vâng ạ! Mikuro, muốn anh cử động ạ──\nNu!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ふかみh1_ともはり練習 | 1042 | 「んきゅっ――ひっ――イっ――んんん～～んっ！\nんくっ――ごくっ――じゅううっ――ごきゅっ」 | 「嗯……呀……呀……嗯……嗯！呃……咕咚……啾……嗚」 | 「Ưm kyu——hi——lên——ưm ưm ưm~~ưm!\nƯm kh——ực——chụt——ực」 | 「Nkyu——hi——lên——ưm ưm ưm~~ưm!\nNku——ực——chụt——ực」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んきゅっ+んくっ ("Ưm kh"→"Nku"); グッ→"hự" giữ (ぐっ, không phải くっ). |
| ふかみh1_ともはり練習 | 1055 | 「んひゅっ！ おくっ！ 奥っ！ 子宮っ！\n子、宮っっ――ごっ――って――ん、ごつん、って！！」 | 「嗯！裡面！裡面！子宮！子宮……捅……嗯，捅到裡面了！！」 | 「Ưm hyu! Sâu quá! Bên trong! Tử cung!\nTử, cung——phập——ưm, đâm trúng, rồi!!」 | 「Nhyu! Sâu quá! Bên trong! Tử cung!\nTử, cung——phập——ưm, đâm trúng, rồi!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ふかみh1_ともはり練習 | 1057 | 「んきゅぅっ！！」 | 「嗯！！」 | 「Ưm kyuu!!」 | 「Nkyuu!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んきゅぅっ→"Nkyuu". |
| ふかみh2_homesweethome | 977 | 「ひゃっ！？ \n双鉄さん、い、今の大丈夫なっ！？――んぐっ！？」 | 「呀？！雙鐵先生，剛、剛才的沒事吧？！唔？！」 | 「Hya!?\nAnh Soutetsu, v, vừa rồi không sao chứ ạ!?——Ưm gu!?」 | 「Hya!?\nAnh Soutetsu, v, vừa rồi không sao chứ ạ!?——Ngu!?」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ふかみh2_homesweethome | 993 | 「んきゅんっ！」 | 「唔！」 | 「Ưm kyun!」 | 「Nkyun!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んきゅんっ→"Nkyun". |
| ふかみh2_homesweethome | 994 | 「んぐっ！ んっ――んっ――ふううっ――んっ――\nングッ――んっ――ふうっ――んっ――んっ――ふうっ」 | 「唔！嗯，嗯，唔，嗯，唔，嗯，唔，嗯，嗯，唔」 | 「Ưm gu! Ưm——ưm——phù u u——ưm——\nƯm gu——ưm——phù ư——ưm——ưm——phù ư」 | 「Ngu! Ưm——ưm——phù u u——ưm——\nNgu——ưm——phù ư——ưm——ưm——phù ư」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ふかみh2_homesweethome | 999 | 「んきゅっ――ん――グッ――んふっ――んっっ！ む」 | 「唔，唔，唔，呼，嗯！唔」 | 「Ưm kyu——ưm——hự——ưm fu——ưm! Ưm」 | 「Nkyu——ưm——hự——Nfu——ưm! Ưm」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ふかみh2_homesweethome | 1000 | 「ふぐっ――ぐっ――んぷっ――んっ――ふっ――んっ\nふうっ――んっ――んぎゅっ――ちゅっ――ちゅうう！」 | 「唔，唔，唔，嗯，唔，嗯，唔，嗯，嗯，啾，啾！」 | 「Phù gu——gu——ưm pu——ưm——phù——ưm\nPhù ư——ưm——ưm gyu——chụt——chụt u u!」 | 「Phù gu——gu——Npu——ưm——phù——ưm\nPhù ư——ưm——Ngyu——chụt——chụt u u!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ふかみh2_homesweethome | 1004 | 「むぐっ！！！？」 | 「唔？！」 | 「Ưm gu!!!?」 | 「Mugu!!!?」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. むぐっ→"Mugu" (cùng họ ん+phụ âm). |
| ふかみh2_homesweethome | 1033 | 「ん……ぷっ……んぷっ――んっ――んうっ――\nん～～っ――んっ！ こくっ――こくっ――ごくっ」 | 「嗯……噗……唔，嗯，唔，嗯……嗯！咕咚，咕咚，咕咚」 | 「Ưm……pu……ưm pu——ưm——ưm ư——\nƯm~~~——ưm! Ực——ực——ực」 | 「Ưm……pu……Npu——ưm——Nu——\nƯm~~~——ưm! Ực——ực——ực」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ふかみh2_homesweethome | 1044 | 「んぷっ！！？ んっ！ ふぅぅぅぅぅぅぅんっ！！！」 | 「噗？！嗯！唔！！！」 | 「Ưm pu!!? Ưm! Phù u u u u u u u n!!!」 | 「Npu!!? Ưm! Phù u u u u u u u n!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| れいなh2_おもらし防止大作戦 | 1053 | 「んきゅっ――ふっ――あっ――れいな――れいなぁ――\nおしっこの、あな――つんつん、ぺろぺろ――され、て」 | 「啊嗯……蛤啊……啊……玲奈……玲奈……尿尿的洞……被舔著……」 | 「Ưm kyu——phù——a——Reina——Reina——\nlỗ tiểu——bị chọc chọc, liếm liếm——rồi」 | 「Nkyu——phù——a——Reina——Reina——\nlỗ tiểu——bị chọc chọc, liếm liếm——rồi」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| れいなh3_おもらし自由化大作戦 | 1071 | 「んきゅっ！ ふっ――やっっ――そこっ――\nれいな――そこで――ぐりゅって、されるの――んっ！」 | 「啊嗯！啊……那裡……玲奈……那裡……被插到了……啊嗯！」 | 「Ưm kyu! Phù——ya——chỗ đó……Reina……chỗ đó……\nbị đâm vào……a ưm!」 | 「Nkyu! Phù——ya——chỗ đó……Reina……chỗ đó……\nbị đâm vào……a ưm!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| れいなh3_おもらし自由化大作戦 | 1073 | 「んきゅっ！ ふあっ――あっ――あっ！！」 | 「啊嗯！蛤啊、啊啊啊啊！！」 | 「Ưm kyu! Fua——a——a!!」 | 「Nkyu! Fua——a——a!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| れいなh3_おもらし自由化大作戦 | 1095 | 「んきゅううっ！」 | 「嗚嗚嗚！」 | 「Ưm kyuu!」 | 「Nkyuuu!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んきゅ+う×2 → 3u. |
| ハチロクh1_契り | 1219 | 「や……双鉄……様っ……んっ――\nわたくし、の――胸……など……んふっ」 | 「呀……雙鐵少爺……嗯——我、的胸———有什……嗯唔」 | 「A……Ngài……Soutetsu……ưm――\nNgực――của em……thì có gì……Ưm fu.」 | 「A……Ngài……Soutetsu……ưm――\nNgực――của em……thì có gì……Nfu.」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh1_契り | 1229 | 「ひあっ！？ あ――双鉄様――双鉄さま、がっ――\nんっ！ わたくし、の――おまんまん――を――んふっ」 | 「呀！？啊——雙鐵少爺——雙鐵少爺——嗯！舌頭——伸進——我的妹妹——嗯嗚」 | 「Hia!? A――Ngài Soutetsu――Ngài Soutetsu――\nƯm! Bướm――của, em――Ưm fu.」 | 「Hia!? A――Ngài Soutetsu――Ngài Soutetsu――\nƯm! Bướm――của, em――Nfu.」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh1_契り | 1282 | 「んきゅううううっ！！」 | 「嗯呀——！！」 | 「Ưm kyuuuuu!!」 | 「Nkyuuuuu!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んきゅ+う×4 → 5u. |
| ハチロクh2_お勉強の成果 | 1036 | 「んっ――んふっ――ふ、あっ」 | 「嗯——呼——呼，啊」 | 「Ưm——ưm fu——Fu, a」 | 「Ưm——Nfu——Fu, a」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh2_お勉強の成果 | 1039 | 「ん――こくっ――んくっ――ごくっ」 | 「嗯——嗚——嗯——嗯」 | 「Ưm——ực——ưm ku——ực」 | 「Ưm——ực——Nku——ực」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh2_お勉強の成果 | 1051 | 「んふっ！」 | 「嗯呼！」 | 「Ưm fu!」 | 「Nfu!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh2_お勉強の成果 | 1056 | 「んああっ！ おちん、ちんっ――ごりって、\nおまんまん、して、くれる、おちんちん、もっ！」 | 「嗯嗯！雞，雞——鑽進來，我也喜歡肯插入我小妹妹的雞雞！」 | 「Ưm aa! Cậu, bé——cậu bé đang, ngoáy mạnh\ntrong cô bé, của em, em cũng thích!」 | 「Naa! Cậu, bé——cậu bé đang, ngoáy mạnh\ntrong cô bé, của em, em cũng thích!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh4_ゼリー・シリンジ・コンドーム | 1013 | 「いっ――あっ――知らない――こんなのっ――あっ――\n入ってる――のにっ――深、い――のにっ――んくっ」 | 「在——啊——我都不知道——這樣——啊——進來了——這麼深——嗯」 | 「A——a——em không biết——cảm giác này——a——\nđang cắm vào——vậy mà——sâu, quá——vậy mà——ưm ku」 | 「A——a——em không biết——cảm giác này——a——\nđang cắm vào——vậy mà——sâu, quá——vậy mà——Nku」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて | 852 | 「はっ――あっ――まだ――ふとっ――んっ――\nんっ――ふあっ――んくっ！！！」 | 「哈——啊——還——嗚嗯——嗯——呼啊——嗯！！！」 | 「Hà——a——vẫn còn——to——ưm——\nưm——Fua——ưm ku!!!」 | 「Hà——a——vẫn còn——to——ưm——\nưm——Fua——Nku!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて | 885 | 「ンッ――ふっ――ふっ！ ふっ！ んふっ！ んっ――\nふっ！ ふっ！ ふっ！ ふううっ！！！」 | 「嗯——呼——呼！呼！嗯呼！嗯——呼！呼！呼！呼！！！」 | 「Ưm——phù——phù! Phù! Ưm phù! Ưm——\nphù! Phù! Phù! Phù ư ư!!!」 | 「Ưm——phù——phù! Phù! Nfu! Ưm——\nphù! Phù! Phù! Phù ư ư!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて | 887 | 「んっ――ふっ――れるっ――るっ――んっ――\nちゅっ――んくっ――ふっ――ふううっ！」 | 「嗯——呼——咻嚕——嚕——啾——嗯——呼——呼！」 | 「Ưm——phù——rộp——rộp——ưm——\nchụt——ưm ku——phù——phù ư ư!」 | 「Ưm——phù——rộp——rộp——ưm——\nchụt——Nku——phù——phù ư ư!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて | 889 | 「んっ――ふうっ――んっ！ んっ！ れるっ――\nじゅっ！ ふっ――んふっ――んっ！ んんっ！！」 | 「嗯——呼——！嗯！咻嚕——呲啾！呼——呼——！嗯嗯！！」 | 「Ưm——phù——ưm! Ưm! Mút——\nchụt! Phù——ưm phù——ưm! Ưm ưm!!」 | 「Ưm——phù——ưm! Ưm! Mút——\nchụt! Phù——Nfu——ưm! Ưm ưm!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて | 924 | 「んひゅっ――んっ――んゅっ――んん～――\nふっ――んふっ――ふっ――ふぅ～っ――」 | 「嗯咻——嗯——嗯嗯～——呼——呼——呼——嗚～——」 | 「Nhyu——ưm——Nyu——ưm ưm~——\nphù——ưm phù——phù——phù~——」 | 「Nhyu——ưm——Nyu——ưm ưm~——\nphù——Nfu——phù——phù~——」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて | 935 | 「んくっ！！！！」 | 「嗯嗯！！！！」 | 「Ưm ku!!!!」 | 「Nku!!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて | 937 | 「んくっ！？ かひゅっ――あっ？ そう、てつ、さまっ\n――わた、くし――おく――もう、一番――お、くぅっ」 | 「嗯嗯！？咻——啊？雙鐵少爺——我——裡面——最裡面的——地方」 | 「Ưm ku!? Kahyu——a? Ngài, Soutetsu\n——của, em——bên trong——đã đến, nơi——sâu, nhất rồi.」 | 「Nku!? Kahyu——a? Ngài, Soutetsu\n——của, em——bên trong——đã đến, nơi——sâu, nhất rồi.」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて | 941 | 「んっ！ ふっ！ ふっ！ んっ！ ふっ！ ふあっ！\nんっ！ んくっ！ んっ！！！」 | 「嗯！呼！呼！嗯！呼！呼啊！嗯！嗯嗯！嗯！！！」 | 「Ưm! Phù! Phù! Ưm! Phù! Fua!\nƯm! Ưm ku! Ưm!!!」 | 「Ưm! Phù! Phù! Ưm! Phù! Fua!\nƯm! Nku! Ưm!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh7_レトロモダンメイクラヴ | 754 | 「ひっ――あっ――またっ！ やっ――わたっ――くし、\nまたっ――んきゅっ――くるっ――しゅごい、のっ！！」 | 「咿——啊——又！哎——我——我，又——來了——好爽！！」 | 「Hi——a——lại nữa! A——em——\nlại nữa——ưn kyu——đến rồi——sướng, quá!!」 | 「Hi——a——lại nữa! A——em——\nlại nữa——Nkyu——đến rồi——sướng, quá!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh7_レトロモダンメイクラヴ | 759 | 「ひあっ！ んっ――お尻――ふあっ――お尻、も……\nです、から――今、は……んっ――んくぅぅぅ～～っ」 | 「咿啊！嗯——屁股——呼啊——屁股，也……——所以現在……嗯嗯——啾嗚～～」 | 「Hí a! Ưm——mông——Fua——mông, cũng……\nmà——bây giờ, thì……ưm——ưm kuuuu~~Ư」 | 「Hí a! Ưm——mông——Fua——mông, cũng……\nmà——bây giờ, thì……ưm——Nkuuuu~~」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んくぅぅぅ～～っ → "Nkuuuu~~" (4u); bỏ Ư cuối. |
| ハチロクh7_レトロモダンメイクラヴ | 783 | 「あっ――ひっ――しょっ――くっ――んあっ――\nゆっく――りっ――され、りゅっ――と――んぅ～っ！」 | 「啊——哈——嗚——嗯——啊——慢——慢一點！」 | 「A——hi——ức——khục——ưm a——\nchậm——chậm——lại, đi——ưm~Ư!」 | 「A——hi——ức——khục——Na——\nchậm——chậm——lại, đi——ưm~Ư!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh7_レトロモダンメイクラヴ | 840 | 「んぐぐっ！」 | 「嗯唔！」 | 「Ưm gugu!」 | 「Ngugu!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh7_レトロモダンメイクラヴ | 841 | 「んぐっ！！？」 | 「嗯唔！！？」 | 「Ưm gu!!?」 | 「Ngu!!?」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh7_レトロモダンメイクラヴ | 970 | 「双鉄さまっ！ だんな、さまっ――んあっ！！！」 | 「雙鐵少爺！夫君——啊！！！」 | 「Ngài Soutetsu! Phu quân——ưm a!!!」 | 「Ngài Soutetsu! Phu quân——Na!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh8_桜色のひめごと | 732 | 「ふあっ！？ そこっ！ あっ――あっ――んっ――！\nんく～～～～～～～～～～～～～～～～～っ！！！」 | 「呼啊！？那裡！啊——啊——！嗯～～～～～～～～～～～～～～～～～！！！」 | 「Fua!? Chỗ đó! A——a——ưm——!\nƯn ku~~~~~~~~~~~~~~~~~!!!」 | 「Fua!? Chỗ đó! A——a——ưm——!\nNku~~~~~~~~~~~~~~~~~!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んく+～×17 → "Nku"+17~. |
| ハチロクh8_桜色のひめごと | 737 | 「ひあっ！ あっ――ア――んくっ！！ ふっ！」 | 「咿啊！啊——啊——嗯！！呼！」 | 「Hia! A——a——ưn ku!! Phù!」 | 「Hia! A——a——Nku!! Phù!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh8_桜色のひめごと | 836 | 「んきゅうううううううううううっっっっっ！！！！」 | 「嗯嗚——！！！！」 | 「Ưn kyuuuuuuuuuuuu!!!!」 | 「Nkyuuuuuuuuuuuu!!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んきゅ+う×11 → 12u (CUR có 13u, sai 1). |
| ハチロクh8_桜色のひめごと | 837 | 「んうっ」 | 「嗯嗚」 | 「Ưm u」 | 「Nu」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh8_桜色のひめごと | 839 | 「んくっ――ごくっ――ごきゅ――ごきゅん――じゅる」 | 「嗯嗯——嗯——咕嚕——啾嚕」 | 「Ưn ku——ực——ực——ực——chóp chép」 | 「Nku——ực——ực——ực——chóp chép」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh8_桜色のひめごと | 855 | 「しょこ――しゅご――んっ――ふあっ――すご――\nすご――すぎって――んうっ――わたく、し――回路っ」 | 「好棒——好棒——呼啊——好棒啊——太厲害了——嗚——我的——迴路」 | 「Chỗ đó——tuyệt quá——ưm——Fua——tuyệt quá——\ntuyệt quá——mất——ưm u——em——mạch điện」 | 「Chỗ đó——tuyệt quá——ưm——Fua——tuyệt quá——\ntuyệt quá——mất——Nu——em——mạch điện」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh9_コノフクハキルコト | 2135 | 「じゅるうううううっ！ ぢゅぼおっ――んくっ！？」 | 「啾嚕嗚嗚嗚嗚！啾啵——嗯！？」 | 「Juruuuuu! Juboo——ưm ku!?」 | 「Juruuuuu! Juboo——Nku!?」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh9_コノフクハキルコト | 2177 | 「んひゅふぅぅぅっ！！？」 | 「嗯嗚——！！？」 | 「Ưm hyu phuuuu!!?」 | 「Nhyufuuuu!!?」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んひゅふぉぅぅっ→"Nhyufuuuu" (5u). |
| ハチロクh9_コノフクハキルコト | 2179 | 「んぶっ！！！！？」 | 「嗯嗚！！！！？」 | 「Ưm bu!!!!?」 | 「Nbu!!!!?」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh9_コノフクハキルコト | 2180 | 「んっきゅっ！！？\nふああぁぁぁぁぁぁっぁぁぁぁっぁああああっ！！」 | 「嗯嗚！！？呼、嗯啊啊——！！」 | 「Ưm kyu!!?\nFuaaaaaaaaaaaaaaaaa!!」 | 「Nkyu!!?\nFuaaaaaaaaaaaaaaaaa!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ハチロクh9_コノフクハキルコト | 2181 | 「んぶっ！？ んっ――\nごくっ、ごくっ、ごくっ、ごくっ」 | 「嗯嗚！？嗯——嗯，嗯，嗯，嗯」 | 「Ưm bu!? Ưm——\n（Ực, ực, ực, ực）」 | 「Nbu!? Ưm——\n（Ực, ực, ực, ực）」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ポーレットh1_ファーストセックス | 1026 | 「ん……ふっ……は、い――こんなに、\nドキドキ――するの――はじめ、てっ……んふっ」 | 「嗯……呼……嗯……我是第一次……心跳這麼快……嗯呼」 | 「Ưm... phù... v, âng——Tim đập,\nnhanh——thế này——là lần đầu, tiên... ưm phù.」 | 「Ưm... phù... v, âng——Tim đập,\nnhanh——thế này——là lần đầu, tiên... Nfu.」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ポーレットh1_ファーストセックス | 1041 | 「んんふっ！ ちょく、せつっ――あっ――すごいっ」 | 「嗯呼！直接……啊，好厲害」 | 「Ưm phù! Trực, tiếp——á——tuyệt quá.」 | 「Nnfu! Trực, tiếp——á——tuyệt quá.」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んんふっ→"Nnfu". |
| ポーレットh1_ファーストセックス | 1106 | 「だからッ――ん、動い、て……あ……\n双鉄、くん、を――わたし、の――なか――んきゅっ！」 | 「所以——嗯——動起來吧——啊……雙鐵君——在我裡面——嗯！」 | 「Nên là——ưm, hãy di, chuyển... a...\nanh Soutetsu, này——bên trong, em——ưm kyu!」 | 「Nên là——ưm, hãy di, chuyển... a...\nanh Soutetsu, này——bên trong, em——Nkyu!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| ポーレットh5_裸エプロンのレモンドレッシング和え | 856 | 「や！ あっ――やわらかっ――んっ――んあっ！\nぬめっ、って――あったか――ふっ、きゅっ――ふうっ」 | 「呀！啊――軟軟的——嗯——嗯！滑滑的——熱熱的——呼——呼啊」 | 「Ya! A——mềm quá——ưm——ưm a! Trơn tuột——ấm quá——phù, Kyu——Phùù」 | 「Ya! A——mềm quá——ưm——Na! Trơn tuột——ấm quá——phù, Kyu——Phùù」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 凪h2_おとなの水着 | 2489 | 「くっ――ふっ――んひゅっ――んんん～っ！」 | 「唔……嗯……嗯……嗯！」 | 「Ku——Phù——Ưm hứ——Ưmmm~!!」 | 「Ku——Phù——Nhyu——Ưmmm~!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 凪ふかみh2_みずあそび | 1297 | 「んふっ――んんっ――えうううっ――べろおっ」 | 「呼……嗯……嗚……啾」 | 「Ưm phù——ưm——Euuu——liếm」 | 「Nfu——ưm——Euuu——liếm」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 凪ふかみh2_みずあそび | 1369 | 「んんっ――ふっ――ふっ！ んふっ！」 | 「嗯……呼……呼！ 呼！」 | 「Ưm——phù——phù! Ưm phù!」 | 「Ưm——phù——phù! Nfu!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 日々姫h5_白濁絵の具の射精会 | 1150 | 「ひあっ――あ――あっ――熱いのっ――来てっ――るっ\n――んあっ――にぃに――の――えの、ぐっ――がっ」 | 「呀――啊――啊――熱熱的――射進來了――――嗯啊――阿哥的――顏料――」 | 「Hia――a――a――Nóng quá――đang vào――rồi\n――ưm a――Màu, vẽ――của――anh hai――」 | 「Hia――a――a――Nóng quá――đang vào――rồi\n――Na――Màu, vẽ――của――anh hai――」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 日々姫h5_白濁絵の具の射精会 | 1182 | 「ふあっ――んふっ――ふっ――は――うれしかぁ――\nにぃにの、かわゆか声ば――聞いちゃった♪」 | 「呼――嗯――呼――呼――我好開心――能聽到阿哥發出――這麼可愛的聲音♪」 | 「Fua――ưm phù――phù――hà――Vui quá――\nĐược nghe thấy――giọng nói dễ thương, của anh hai rồi♪」 | 「Fua――Nfu――phù――hà――Vui quá――\nĐược nghe thấy――giọng nói dễ thương, của anh hai rồi♪」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 日々姫h5_白濁絵の具の射精会 | 1265 | 「んぶうううううっっっっ！！？」 | 「嗯啊！！？」 | 「Ưm buuuuuu!!!!?」 | 「Nbuuuuuu!!!!?」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. んぶ+う×5 → 6u. |
| 日々姫h6_オリエンテーリング借り物競走（ペア） | 2100 | 「はぁっ――はぁっ――これ……かたち……すごく、\nわかる――おちん、ちん――の――んっ――んあ！」 | 「呼――呼――這樣……能……感覺到……――雞雞的――形狀――非常清楚――嗯！」 | 「Hà――hà――Thế này……hình dáng……rất,\nrõ ràng――chim――của anh――ưm――ưm a!」 | 「Hà――hà――Thế này……hình dáng……rất,\nrõ ràng――chim――của anh――ưm――Na!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 真闇h1_長期熟成 | 1056 | 「ちゅっ――んっ……んちゅっ――れるっ――れろっ\n――ん……んふっ……ふっ」 | 「啾――嗯……嗯啾――舔――舔――嗯……嗯唔……呼」 | 「Chụt――ưm……ưm chụt――rộp――liếm\n――ưm……ưm fu……Fu」 | 「Chụt――ưm……Nchu――rộp――liếm\n――ưm……Nfu……Fu」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 稀咲h1_性生活 | 1306 | 「んきゅ――くはっ――んあっ――～～～っ！！！」 | 「嗯呀――嗚啊――嗯啊――～～～！！！」 | 「Ưm kyu――kuha――ưm a――~~~Ư!!!」 | 「Nkyu――kuha――Na――~~~Ư!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 稀咲h2_プライベートルーム | 1152 | 「ひゃあうっ！ ――んうっ！！？」 | 「呀啊！ ――嗯唔！！？」 | 「Hyaa u! ――Ưm u!!?」 | 「Hyaa u! ――Nu!!?」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 稀咲h2_プライベートルーム | 1190 | 「あ……んふっ――強引だね、双鉄。\nそれほど、ボクが――」 | 「啊……嗯哼――好強硬啊，雙鐵。就這麼想和我――」 | 「A…… ưm fu――Anh mạnh bạo quá đấy, Soutetsu.\nĐến mức đó, em đã――」 | 「A…… Nfu――Anh mạnh bạo quá đấy, Soutetsu.\nĐến mức đó, em đã――」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 稀咲h2_プライベートルーム | 1219 | 「んきゅっ――っ――はっ――～～～～～っ！！！」 | 「嗯唔――哈――～～～～～！！！」 | 「Ưm kyu――Ư――ha――~~~~~Ư!!!」 | 「Nkyu――Ư――ha――~~~~~Ư!!!」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 稀咲h2_プライベートルーム | 1220 | 「んふっ――あっ――」 | 「嗯唔――啊――」 | 「Ưm fu――a――」 | 「Nfu――a――」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 稀咲h2_プライベートルーム | 1221 | 「んふっ」 | 「嗯唔」 | 「Ưm fuƯ」 | 「Nfu」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. Bỏ Ư cuối (っ không render trong token romaji). |
| 稀咲h3_チャイナドレスでおもてなし | 2207 | 「ぷぁ。んふっ……」 | 「哈，嗯唔……」 | 「Pua. Ưm fu……」 | 「Pua. Nfu……」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 稀咲h3_チャイナドレスでおもてなし | 2265 | 「ん……ふっ――んっ――ちゅっ――ちゅむっ――\nちゅるっ――ちゅっ――んちゅっ――ふ……あ――」 | 「嗯……呼――嗯――啾――啾唔――啾――啾――嗯啾――呼……啊――」 | 「Ưm…… Fu――ưm――chụt――chu mu――\nchu ru――chụt――ưm chu――Fu…… a――」 | 「Ưm…… Fu――ưm――chụt――chu mu――\nchu ru――chụt――Nchu――Fu…… a――」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 稀咲h3_チャイナドレスでおもてなし | 2268 | 「ん……ぷっ……んっ――ごくっ――\nちゅずっ――んっ――ごく――ごくんっ――んふっ」 | 「嗯……唔……嗯――咕嘟――咕啾――嗯――咕嚕――咕嚕――嗯唔」 | 「Ưm…… phu…… ưm――ực――\nchu zu――ưm――ực――ực――ưm fu」 | 「Ưm…… phu…… ưm――ực――\nchu zu――ưm――ực――ực――Nfu」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |
| 稀咲h3_チャイナドレスでおもてなし | 2278 | 「んきゅっ！？」 | 「嗯呀！？」 | 「Ưm kyu!?」 | 「Nkyu!?」 | ん+phụ âm thành 1 token → romaji N… (quyết F1/M15); っ bỏ, không thêm Ư. |

## 3.3. M24 — token cười viết hoa theo F5 (97 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr_ポーレットh1_家族旅行の最終日の夜 | 1088 | 「ん――ふふっ――双鉄くんも、声……\nっ――漏らしちゃってるじゃ、ない、ですか――ん」 | 「嗯——呵呵——雙鐵君不也……沒忍住，叫聲嘛——嗯」 | 「Ưm――fufu――Anh Soutetsu cũng, phát ra……\ntiếng――rên rỉ rồi, còn, gì――ưm」 | 「Ưm――Fufu――Anh Soutetsu cũng, phát ra……\ntiếng――rên rỉ rồi, còn, gì――ưm」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Chỉ viết hoa, KHÔNG gộp (JP có ―― tách token: ん――ふふっ). |
| lr_ポーレットh1_家族旅行の最終日の夜 | 1181 | 「です、うふふっ。お宿のお風呂のシャンプーですから、\nきっと、双鉄くんも、ひかりもれいなも今日はおんなじ」 | 「是的，唔呵呵。這是旅館的浴室的洗髮精，你們三個今天用的肯定也是這個」 | 「Vâng, ufufu. Vì là dầu gội trong phòng tắm của nhà trọ mà,\nchắc chắn hôm nay anh Soutetsu, Hikari và cả Reina đều dùng chung một loại」 | 「Vâng, Ufufu. Vì là dầu gội trong phòng tắm của nhà trọ mà,\nchắc chắn hôm nay anh Soutetsu, Hikari và cả Reina đều dùng chung một loại」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr_ポーレットh2_デコレーション＆ミルク | 1018 | 「ふふっ――ふふふっ！ うふふふふっ！！！」 | 「呵呵——呵呵呵！唔呵呵呵呵！！！」 | 「Fufu——fufufu! Ufufufufu!!!」 | 「Fufu——Fufufu! Ufufufufu!!!」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Chỉ viết hoa token 2 (JP có 、 tách token). |
| lr_ポーレットh2_デコレーション＆ミルク | 1075 | 「あ――うふふっ」 | 「啊——唔呵呵」 | 「A——ufufu」 | 「A——Ufufu」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr_凪h2_虎さんの交尾 | 1258 | 「ふぁ……（ごくっ）――あ！ ふ、ふふふーん！！\nにーさん、凪さまに興奮――発情しちゃったと？」 | 「啊……（咕咚）……啊！哼哼！！大哥哥看本小姐看得興奮，看得發情了吧？」 | 「Fa……（Ực）——A! Fu, fufufu-n!!\nAnh Soutetsu, hưng phấn với Nagi——đến phát tình rồi sao?」 | 「Fa……（Ực）——A! Fu, Fufufu-n!!\nAnh Soutetsu, hưng phấn với Nagi——đến phát tình rồi sao?」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Chỉ viết hoa (JP có 、 tách token).  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| lr_凪h2_虎さんの交尾 | 1391 | 「気持ちよくって――ふふっ、こぎゃんふーにと？」 | 「舒服……嘻嘻，就像這樣嗎？」 | 「Sung sướng sao——fufu, như thế này hả?」 | 「Sung sướng sao——Fufu, như thế này hả?」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr_凪ふかみh1_じぇいけい！ | 1611 | 「！！！！ じぇ、じぇいけいの双鉄おにいさん――\n制服……スカート……うふふふふっ」 | 「啊！！！！Ｊ、ＪＫ雙鐵哥哥……校服……裙子……嘿嘿嘿嘿嘿」 | 「!!!! J, anh Soutetsu JK——\nĐồng phục……váy……ufufufufu」 | 「!!!! J, anh Soutetsu JK——\nĐồng phục……váy……Ufufufufu」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr_凪ふかみh1_じぇいけい！ | 1616 | 「あ、うふふ。そういうことですねぇ。わかりました。\nえっとね？ 凪ちゃん、多分――――――こうっ！？」 | 「啊，嘻嘻嘻……是這樣呀。好的。聽我說，小凪，大概……是這樣的！」 | 「A, ufufu. Ra là vậy nhỉ. Em hiểu rồi.\nƯm nè? Nagi, chắc là——————thế này!?」 | 「A, Ufufu. Ra là vậy nhỉ. Em hiểu rồi.\nƯm nè? Nagi, chắc là——————thế này!?」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên.  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| lr_日々姫h2_デザートは食事の前に | 980 | 「ぁ……んふふ。わかったとー。\nにぃにの美味しい匂いはね？ たぶん～ ここから！！」 | 「啊……嘿嘿，我知道了。阿哥身上這股好聞的氣味，就是從這裡來的！！」 | 「A…… nfufu. Em biết rồi.\nMùi ngon lành của anh hai ấy à? Chắc là~ từ đây!!」 | 「A…… Nfufu. Em biết rồi.\nMùi ngon lành của anh hai ấy à? Chắc là~ từ đây!!」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr_日々姫h2_デザートは食事の前に | 1035 | 「ぺろっっ――ふふっ、ちょこっとしょっぱいチーズ味？\nクセばあるけど――これはこれで――ん～～れろおおっ」 | 「啾嚕……嘿嘿，感覺像鹹鹹的起司味。味道挺特別的，不過也不錯……嗯……啾嚕嚕」 | 「Liếm——fufu, vị phô mai hơi mặn mặn?\nHơi kén người ăn đấy——nhưng thế này cũng——ưm~~ rerooo」 | 「Liếm——Fufu, vị phô mai hơi mặn mặn?\nHơi kén người ăn đấy——nhưng thế này cũng——ưm~~ rerooo」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr_日々姫h2_デザートは食事の前に | 1051 | 「ん……ちゅっ――ちゅむっ――ちゅるっ――れるっ――\nちゅっ――ん――ぷあっ――んふふ、ごちそうさまっ」 | 「嗯……啾……啾……啾嚕……啾……嗯……噗哈……嘿嘿，多謝招待」 | 「Ưm…… chụt——chụt——churu——liếm——\nChụt——ưm——pua——nfufu, cảm ơn vì bữa ăn.」 | 「Ưm…… chụt——chụt——churu——liếm——\nChụt——ưm——pua——Nfufu, cảm ơn vì bữa ăn.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr_日々姫ふかみh1_凪ちゃんの代わり | 1438 | 「ぁ……うふふっ――わたし――にぃにと――\nにぃにとキスば――しちゃったと！」 | 「啊……唔呵呵——我——和阿哥—— 和阿哥接吻——接吻了！」 | 「A…… ufufu――em――với anh hai――\nđã hôn――anh hai rồi!」 | 「A…… Ufufu――em――với anh hai――\nđã hôn――anh hai rồi!」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr_日々姫ふかみh1_凪ちゃんの代わり | 1440 | 「あっ……うふふっ！\n双鉄おにいさん、おっきくなってきちゃいましたねぇ」 | 「啊……唔呵呵！雙鐵哥哥，你變大了呀」 | 「A…… ufufu!\nAnh Soutetsu, nó to lên rồi kìa.」 | 「A…… Ufufu!\nAnh Soutetsu, nó to lên rồi kìa.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên.  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| lr_日々姫ふかみh1_凪ちゃんの代わり | 1457 | 「あ、うふふっ。ビクビクしてきたぁ。\n双鉄おにいさん、射精、もうすぐなんですか？」 | 「啊，唔呵呵。一抖一抖的。雙鐵哥哥，馬上就要射了嗎？」 | 「A, ufufu. Nó đang giật giật kìa.\nAnh Soutetsu, sắp xuất tinh rồi sao?」 | 「A, Ufufu. Nó đang giật giật kìa.\nAnh Soutetsu, sắp xuất tinh rồi sao?」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr_日々姫ふかみh1_凪ちゃんの代わり | 1459 | 「ぁ、やめなくっても平気ですよ？ 今の声は、うふふっ、\nめちゃくちゃ気持ちよすぎてびっくりしちゃった声」 | 「啊，用不著停下來的。剛才的聲音表示，唔呵呵，雙鐵哥哥舒服得嚇了一跳」 | 「A, không cần dừng lại đâu. Tiếng vừa rồi, ufufu,\nlà tiếng kêu vì sướng quá nên giật mình đấy.」 | 「A, không cần dừng lại đâu. Tiếng vừa rồi, Ufufu,\nlà tiếng kêu vì sướng quá nên giật mình đấy.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr_稀咲h1_おしおきとごほうび | 986 | 「ふ……うふふっ――そう、てつ――んっ……\nだらしない顔……溶け出しそうな顔を――して、るよ？」 | 「哈嗯……雙、雙鐵……你現在……一副享受的表情……像要溶化了一樣」 | 「Phù……ufufu――Sou, tetsu――ưm……\nCái bản mặt lôi thôi……như sắp tan chảy ra――kìa?」 | 「Phù……Ufufu――Sou, tetsu――ưm……\nCái bản mặt lôi thôi……như sắp tan chảy ra――kìa?」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr_稀咲h1_おしおきとごほうび | 1160 | 「こんなの――ボク……ばかみたい、嫉妬なんて……\nこんなに――うふふっ――双鉄、僕に、夢中なのに」 | 「我……簡直就是個傻瓜……居然會嫉妒……嘿嘿……雙鐵明明這麼愛我」 | 「Thế này thì――em……giống như đồ ngốc vậy, lại đi ghen tuông……\nTrong khi――ufufu――Soutetsu, lại say đắm em đến thế này.」 | 「Thế này thì――em……giống như đồ ngốc vậy, lại đi ghen tuông……\nTrong khi――Ufufu――Soutetsu, lại say đắm em đến thế này.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr_稀咲ポーレットh1_悪い大人の契約 | 1513 | 「はぁ―んっ―ふぁ―あ―。そう、てつ―\n双鉄―ふふっ―よく頑張ったね。双鉄、おいで？」 | 「哈——嗯——呼啊——啊——雙、鐵——雙鐵——呼呼——你真的很努力。雙鐵，過來吧？」 | 「Ha——ưm——Fa——a——. Anh, Soutetsu—— Anh Soutetsu——fufu——anh đã cố gắng lắm rồi. Lại đây nào, anh Soutetsu?」 | 「Ha——ưm——Fa——a——. Anh, Soutetsu—— Anh Soutetsu——Fufu——anh đã cố gắng lắm rồi. Lại đây nào, anh Soutetsu?」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên.  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| lr_稀咲ポーレットh1_悪い大人の契約 | 1604 | 「ん……ふふっ―どおお、双鉄？ おまんこの感触―\nんっ―ボクと、ポーレットで、結構違う？」 | 「嗯……呼呼——怎麼樣，雙鐵？？ 小穴的觸感——嗯——我和波萊特的小穴，很不一樣嗎？」 | 「Ưm……fufu——sao nào, Soutetsu? Cảm giác của âm đạo——\nưm——của em, và của Paulette, có khác nhau nhiều không?」 | 「Ưm……Fufu——sao nào, Soutetsu? Cảm giác của âm đạo——\nưm——của em, và của Paulette, có khác nhau nhiều không?」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên.  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| lrれいな追加02_花嫁修業の先生たち | 2017 | 真闇姉がなにか囁いた瞬間に、\nれいながうふふうと笑いを零す。 | 真闇姐輕聲耳語之後，玲奈便禁不住笑了起來。 | Khoảnh khắc chị Mayami thì thầm điều gì đó,\nReina bật cười khúc khích ufufu. | Khoảnh khắc chị Mayami thì thầm điều gì đó,\nReina bật cười khúc khích Ufufu. | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr真闇追加01_新婚旅行のリクエスト | 1086 | 「んふふっ、面白そう。ほんならガイドさん。\nいまゆーたん、ぜぇんぶコースにいれてもらえますか？」 | 「呵呵，聽起來很有趣。嚮導小姐，剛才我們說的能全加入到路線裡嗎？」 | 「Ưm fufu, nghe thú vị đấy. Vậy thì cô hướng dẫn viên ơi.\nCó thể cho hết mấy cái vừa nói vào lịch trình được không?」 | 「Nfufu, nghe thú vị đấy. Vậy thì cô hướng dẫn viên ơi.\nCó thể cho hết mấy cái vừa nói vào lịch trình được không?」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr真闇追加01_新婚旅行のリクエスト | 1144 | 「ああ――うふふっ。そうね、絶対。\nぽーちゃん、過保護そうだものねぇ」 | 「啊——呵呵。是啊，一定是這樣。畢竟波萊特很溺愛她」 | 「A——ufufu. Đúng thế, chắc chắn rồi.\nPau-chan, có vẻ bao bọc quá mức nhỉ」 | 「A——Ufufu. Đúng thế, chắc chắn rồi.\nPau-chan, có vẻ bao bọc quá mức nhỉ」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr真闇追加01_新婚旅行のリクエスト | 1194 | 「んふふっ、ようやく、もうすぐよねぇ。\nごめんね？ おねえちゃんが待たせる形になっちゃって」 | 「嘻嘻，終於快要到了。對不起啦，要讓你等一等了」 | 「Ưm fufu, cuối cùng, cũng sắp đến rồi nhỉ.\nXin lỗi em nhé? Chị lại bắt em phải chờ đợi rồi」 | 「Nfufu, cuối cùng, cũng sắp đến rồi nhỉ.\nXin lỗi em nhé? Chị lại bắt em phải chờ đợi rồi」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr真闇追加02_御一夜新婚旅行 | 1215 | 「うっふふー、そうてつさんの投炭性格診断、\nおおあたりですねぇ」 | 「呵呵——雙鐵先生的加煤性格診斷，真的好準」 | "「Ưfufu, chẩn đoán tính cách qua cách xúc than của anh Soutetsu,\ntrúng phóc luôn đó nha~」" | "「Ufufu, chẩn đoán tính cách qua cách xúc than của anh Soutetsu,\ntrúng phóc luôn đó nha~」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. うっふふ→"Ufufu" (gộp như んふふ). Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加02_御一夜新婚旅行 | 1217 | 「んふふっ。れーちゃんが楽しんでくれて、\nおねえちゃんもうれしか」 | 「呵呵。小玲能開心，姐姐也高興」 | 「Ưm fufu. Thấy bé Reina vui vẻ,\nchị cũng vui lắm」 | 「Nfufu. Thấy bé Reina vui vẻ,\nchị cũng vui lắm」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr真闇追加02_御一夜新婚旅行 | 1218 | 「んふふっ。わかった。れーちゃん？ はい、チーズ」 | 「呵呵。我知道了。小玲，茄子」 | "「Ưm fufu. Chị hiểu rồi. Rei-chan? Nào, cười lên.」" | "「Nfufu. Chị hiểu rồi. Rei-chan? Nào, cười lên.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加02_御一夜新婚旅行 | 1222 | 「んふふっ、性格よねぇ」 | 「呵呵，因為你們的性格嘛」 | "「Ưm fufu, do tính cách cả mà.」" | "「Nfufu, do tính cách cả mà.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加02_御一夜新婚旅行 | 1223 | 「んふふ、ありがと。\nね？ ひーちゃん、双ちゃん。れーちゃんも」 | 「呵呵，謝謝。乾杯吧，小日，小雙。還有小玲」 | "「Ưm fufu, cảm ơn em.\nNào? Hi-chan, Sou-chan. Cả Rei-chan nữa.」" | "「Nfufu, cảm ơn em.\nNào? Hi-chan, Sou-chan. Cả Rei-chan nữa.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加02_御一夜新婚旅行 | 1224 | 「んふふっ、ありがと、れーちゃん」 | 「呵呵，謝謝你，小玲」 | "「Ưm fufu, cảm ơn em nha, Rei-chan.」" | "「Nfufu, cảm ơn em nha, Rei-chan.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加02_御一夜新婚旅行 | 1280 | 「んふふっ、冗談。\nそんなん、気がつくわけないでしょお」 | 「哼哼，別逗我了。她倆怎麼可能會看到我呢」 | "「Ưm fufu, em đùa à.\nLàm sao mà hai đứa nó nhận ra chị được chứ.」" | "「Nfufu, em đùa à.\nLàm sao mà hai đứa nó nhận ra chị được chứ.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加02_御一夜新婚旅行 | 1283 | 「んふふっ、れーちゃん、上手ねぇ」 | 「哼哼，小玲幹得真好」 | "「Ưm fufu, Rei-chan làm giỏi quá ta.」" | "「Nfufu, Rei-chan làm giỏi quá ta.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加02_御一夜新婚旅行 | 1285 | 「んふふっ、それじゃあれーちゃんは何に変装すると？」 | 「哼哼，那麼小玲要喬裝成什麼人？」 | "「Ưm fufu, vậy thì Rei-chan sẽ cải trang thành gì nào?」" | "「Nfufu, vậy thì Rei-chan sẽ cải trang thành gì nào?」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加02_御一夜新婚旅行 | 1370 | 「うっふふー、ガイドさんって、\nとーってもたのしいお仕事ですねぇ」 | 「嘿嘿嘿，導遊真是個特別有趣的工作」 | 「Ưfufu~, làm hướng dẫn viên,\nđúng là một công việc cực kỳ thú vị nhỉ~」 | 「Ufufu~, làm hướng dẫn viên,\nđúng là một công việc cực kỳ thú vị nhỉ~」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. うっふふ→"Ufufu" (gộp như んふふ). |
| lr真闇追加02_御一夜新婚旅行 | 1382 | 「んふふっ、ありがと！ そいば最高の褒めことば！！」 | 「嘿嘿，謝謝！這是最棒的誇獎！！」 | "「Ưm fufu, cảm ơn em! Đó là lời khen tuyệt vời nhất đấy!!」" | "「Nfufu, cảm ơn em! Đó là lời khen tuyệt vời nhất đấy!!」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加02_御一夜新婚旅行 | 1680 | 「！ あらまぁ、ふふふっ、まっことねぇ」 | 「！哎呀，哈哈哈，確實很準！」 | "「! Ôi chà, fufu, đúng là vậy nhỉ.」" | "「! Ôi chà, Fufu, đúng là vậy nhỉ.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加03_ブルートレインの夜 | 1125 | 「んふふっ、そぉなんねぇ」 | 「呵呵，也對」 | "「Ưm fufu, ra là vậy.」" | "「Nfufu, ra là vậy.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加03_ブルートレインの夜 | 1127 | 「んふふっ、よかね。男の子って感じ」 | 「呵呵，好啊。很有男子氣概」 | "「Ưm fufu, được đấy. Đúng kiểu con trai nhỉ.」" | "「Nfufu, được đấy. Đúng kiểu con trai nhỉ.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加03_ブルートレインの夜 | 1128 | 「んふふっ、れーちゃん、\nおねえちゃんにあわせてくれとったんかも」 | 「呵呵，小玲她可能只是在配合我」 | "「Ưm fufu, có khi Rei-chan\nđã nương theo chị cũng nên.」" | "「Nfufu, có khi Rei-chan\nđã nương theo chị cũng nên.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加03_ブルートレインの夜 | 1130 | 「んふふっ、了解。\n背中綺麗に、よろしくね？」 | 「呵呵，明白。就麻煩你把我的後背洗得乾乾淨淨啦」 | "「Ưm fufu, đã rõ.\nNhờ em kỳ cho lưng chị thật sạch nhé?」" | "「Nfufu, đã rõ.\nNhờ em kỳ cho lưng chị thật sạch nhé?」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加03_ブルートレインの夜 | 1132 | 「んふふっ、そうね。あのこの趣味ばずーっと変わらん。\n日常そのものの顔して、ちょこっとだけおしゃれいうか」 | 「呵呵，是啊。她的興趣一直都沒變。平時也是那副表情，就只會稍稍打扮一下」 | 「Ưm fufu, đúng vậy. Sở thích của đứa trẻ đó không hề thay đổi.\nKhuôn mặt vẫn là của thường ngày, chỉ là thêm chút xíu điệu đà thôi」 | 「Nfufu, đúng vậy. Sở thích của đứa trẻ đó không hề thay đổi.\nKhuôn mặt vẫn là của thường ngày, chỉ là thêm chút xíu điệu đà thôi」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr真闇追加03_ブルートレインの夜 | 1182 | 「んふふ、新婚旅行やもんねぇ」 | 「嗯哼哼，畢竟是新婚旅行嘛」 | 「Ưm fufu, là tuần trăng mật mà lị」 | 「Nfufu, là tuần trăng mật mà lị」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr真闇追加03_ブルートレインの夜 | 1264 | 「そ。ベッドから見えるお部屋の全部を。\nだけじゃなく……んふふっ、おねえちゃんの寝顔とかも」 | 「對，從床上看到的屋內的全部景象。不僅如此……呵呵，還包括我的睡臉之類的」 | 「Đúng. Toàn bộ căn phòng nhìn từ trên giường.\nKhông chỉ thế đâu……ưm fufu, cả khuôn mặt lúc ngủ của chị nữa」 | 「Đúng. Toàn bộ căn phòng nhìn từ trên giường.\nKhông chỉ thế đâu……Nfufu, cả khuôn mặt lúc ngủ của chị nữa」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr真闇追加h_赤ちゃん、欲しか | 1132 | 「ああ、やっぱりこいば気持ちよかとね。ほんなら――\nんふふ、おねえちゃん、もーっとしつこくしたげるけん」 | 「啊，果然這樣會很舒服啊。嘻嘻，姐姐再多給你揉揉」 | "「A, quả nhiên làm thế này thì sướng lắm nhỉ. Vậy thì——\nƯm fufu, chị sẽ làm dai dẳng hơn nữa cho em nhé.」" | "「A, quả nhiên làm thế này thì sướng lắm nhỉ. Vậy thì——\nNfufu, chị sẽ làm dai dẳng hơn nữa cho em nhé.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加h_赤ちゃん、欲しか | 1181 | 「んふふっ、いいこ、まっこといいこ。\nかわいいかわいい、おねーちゃんの赤ちゃん」 | 「嘻嘻，真乖，真是個乖寶寶。姐姐的小寶寶真可愛」 | "「Ưm fufu, ngoan lắm, thực sự rất ngoan.\nĐáng yêu quá, em bé đáng yêu của chị.」" | "「Nfufu, ngoan lắm, thực sự rất ngoan.\nĐáng yêu quá, em bé đáng yêu của chị.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加h_赤ちゃん、欲しか | 1183 | 「んふふっ、今度はとっても素直。\n気持ちよかとねー。いいこ、いいこ」 | 「嘻嘻，這次倒是非常誠實。很舒服吧，好乖、好乖」 | "「Ưm fufu, lần này thì ngoan ngoãn lắm.\nSướng lắm đúng không. Ngoan lắm, ngoan lắm.」" | "「Nfufu, lần này thì ngoan ngoãn lắm.\nSướng lắm đúng không. Ngoan lắm, ngoan lắm.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加h_赤ちゃん、欲しか | 1187 | 「はぁい。んふふっ。ほんなら、どーぞ」 | 「好。嘻嘻，來，那就開始」 | "「Vâng ạ. Ưm fufu. Vậy thì, xin mời.」" | "「Vâng ạ. Nfufu. Vậy thì, xin mời.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr真闇追加h_赤ちゃん、欲しか | 1283 | 「いいこ、いいこ。なでなで、くりくり。\nんふふっ、びくびく、気持ちよかとねー」 | 「真乖，真乖。摸一摸，搓一搓。呵呵，一抖一抖的，很舒服吧」 | "「Ngoan lắm, ngoan lắm. Vuốt vuốt, xoa xoa.\nƯm fufu, giật giật rồi kìa, sướng lắm đúng không.」" | "「Ngoan lắm, ngoan lắm. Vuốt vuốt, xoa xoa.\nNfufu, giật giật rồi kìa, sướng lắm đúng không.」" | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Giữ nguyên dấu "…" bao dòng (văn bản thật — có trong CSV3 và TOML gốc). |
| lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」 | 2323 | 「ん、ふふっ？ さっきまでの――余裕は、どう、した？、\nいまっ、おぬし――んっ――軽く、イったで――あろ？」 | 陰蒂完全裸露出來，二者不斷輕輕摩擦。房間內開始變得燥熱，耳邊傳來響亮的水聲，濃厚的氣味直衝鼻腔。 | 「Ưm, fufu? Vẻ thong dong——vừa nãy, đâu, rồi?,\nBây giờ, cô——ưm——vừa lên đỉnh, nhẹ——đúng không?」 | 「Ưm, Fufu? Vẻ thong dong——vừa nãy, đâu, rồi?,\nBây giờ, cô——ưm——vừa lên đỉnh, nhẹ——đúng không?」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Chỉ viết hoa (JP có 、 tách token). |
| lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」 | 2347 | 「ヘタレのひよこが――ふふっ――\nよぉがんばったの――（ちゅっ！）」 | 電車公主緩緩挪動自己的身體，將假陽具從體內抽了出來—— | 「Hiyoko nhút nhát——fufu——\nLàm tốt lắm——(Chụt!)」 | 「Hiyoko nhút nhát——Fufu——\nLàm tốt lắm——(Chụt!)」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」 | 2350 | 「ひよこ……ひよこ……ふふっ。愛しておるぞ」 | 電車公主輕輕吻向不死鳥博士，隨後為她取出了假陽具—— | 「Hiyoko……Hiyoko……fufu. Ta yêu cô.」 | 「Hiyoko……Hiyoko……Fufu. Ta yêu cô.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1690 | 「んふふっ」 | 「呵呵」 | 「Ưm fufu.」 | 「Nfufu.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1691 | 「んふふっ、かわい」 | 「呵呵，真可愛」 | 「Ưm fufu, đáng yêu quá.」 | 「Nfufu, đáng yêu quá.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1692 | 「んふふっっ──かわい。とっても綺麗。\nもっと気持ちよくしてあげたくなっちゃう」 | 「呵呵，真可愛，而且好漂亮。看著就想讓它變舒服起來 」 | 「Ưm fufu── dễ thương quá. Đẹp lắm.\nLàm chị muốn làm cho em sướng hơn nữa.」 | 「Nfufu── dễ thương quá. Đẹp lắm.\nLàm chị muốn làm cho em sướng hơn nữa.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1702 | 「んふふっ──よかとね？ にぃにも、みくろも」 | 「呵呵，阿哥和美玖路都很舒服吧？」 | 「Ưm fufu── Sướng lắm đúng không? Cả anh hai và Mikuro.」 | 「Nfufu── Sướng lắm đúng không? Cả anh hai và Mikuro.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1861 | 「んむっ！？ ん……ふっ──んふふっ──」 | 「嗯唔？！嗯……呼——嗯呼呼——」 | 「Ưm!? Ưm……phu──ưm fufu──」 | 「Ưm!? Ưm……phu──Nfufu──」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 1901 | 「ぷあっ──ふふっ、だって。みくろ」 | 「噗啊——呵呵，阿哥是這麼說的哦。美玖路」 | 「Pua──fufu, anh ấy bảo thế kìa. Mikuro.」 | 「Pua──Fufu, anh ấy bảo thế kìa. Mikuro.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên.  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 2313 | 「（ちゅっ──ちゅむっ！） んふふっ。そぎゃんね。\nセックスの方がひとりでするより、ずうっとよかと」 | 「（啾——啾唔！）呵呵，這樣啊。比起一個人自慰，一起做愛要舒服多了」 | 「（Chụt──chụt!） Ưm fufu. Vậy sao.\nLàm tình sướng hơơơn hẳn tự làm một mình nhỉ.」 | 「（Chụt──chụt!） Nfufu. Vậy sao.\nLàm tình sướng hơơơn hẳn tự làm một mình nhỉ.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| ふかみh3_夏休みの最後の日の、前の日 | 2478 | 「はい、うふふっ。いただきまぁす」 | 「好的。嘻嘻嘻，我不客氣了」 | 「Vâng, ufufu. Em xin phép ạ」 | 「Vâng, Ufufu. Em xin phép ạ」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| れいなh3_おもらし自由化大作戦 | 1092 | 「ンぶっ――むううっ――んっ――ふっ――んっ――\n（スヒっ）――（スヒっ）――んふふぅぅぅ～」 | 「嗚……嗯……啊嗯……啊……呼……呼……」 | 「Nbu——muuu——ưm——phù——ưm——\n（Suhi）——（Suhi）——nfufuuuu~」 | 「Nbu——muuu——ưm——phù——ưm——\n（Suhi）——（Suhi）——Nfufuuuu~」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên.  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| グランドリライト06_稀咲 | 1378 | 「会える時間、か――うふふ、いいね。\nそう言ってもらえて、嬉しいよ」 | 「“我們能見面的時間”……呵呵，真不錯。聽到你這麼說，我很開心」 | 「Thời gian gặp được, sao——ufufu, hay đấy.\nNghe cậu nói vậy, em vui lắm.」 | 「Thời gian gặp được, sao——Ufufu, hay đấy.\nNghe cậu nói vậy, em vui lắm.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| ニイロク02_御一夜旅行 | 1571 | 「っ！！！ うん。うん！ 『いってらっしゃい』。\nふっ……うふふ――うふふふふ」 | 「啊！！！嗯、嗯！“一路順風”啊。哼哼……哼哼哼」 | 「Ư!!! Ừm. Ừm! 'Đi đường bình an'.\nHừm...... ư fufu――ư fufufufu.」 | 「Ư!!! Ừm. Ừm! 'Đi đường bình an'.\nHừm...... Ufufu――Ufufufufu.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Gộp "ư fufu"→"Ufufu"; token 2 うふふふふ→"Ufufufufu". |
| ニイロク02_御一夜旅行 | 1592 | 「うん。うん。……うふふふふふ」 | 「嗯、嗯……嗚呵呵呵呵呵」 | 「Ừm. Ừm. ......Ư fufufufufu.」 | 「Ừm. Ừm. ......Ufufufufufu.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Gộp "Ư fufufufufu"→"Ufufufufufu". |
| ハチロク03_冥国式レイルロオド | 2212 | 「は、はい。うれしいです。それでは――うふふっ。\nオリヴィちゃん、と呼ばせていただきますね？」 | 「啊，好的，我好高興呀。那恭敬不如從命，我就叫你奧莉薇了」 | 「V-Vâng. Em rất vui ạ. Vậy thì——ufufu.\nCho phép em gọi chị là bé Olivy nhé?」 | 「V-Vâng. Em rất vui ạ. Vậy thì——Ufufu.\nCho phép em gọi chị là bé Olivy nhé?」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| ハチロク04_小畑越え | 2489 | 「あらまぁ、うふふふ。\nきっと、エビがはいっているからでしょうね」 | 「這樣的嗎，嘻嘻。想必是因為放了蝦進去吧」 | 「Ái chà, ufufufu.\nChắc chắn là vì có tôm ở trong đó rồi ạ.」 | 「Ái chà, Ufufufu.\nChắc chắn là vì có tôm ở trong đó rồi ạ.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| ハチロク06_のぞみ | 2321 | 「はむっ――ぺろっ――んふふふっ～\nでさ、溶けたらやだから、食べながらでいいんだけどさ」 | 「啊嗚——（抹嘴）——嗯呵呵～不過，雖然在路上邊走邊吃是總比化了要好」 | 「Ngoạm――liếm――nfufufu~\nNè, Olivy không muốn kem bị chảy đâu, nên cứ vừa đi vừa ăn cũng được nha.」 | 「Ngoạm――liếm――Nfufufu~\nNè, Olivy không muốn kem bị chảy đâu, nên cứ vừa đi vừa ăn cũng được nha.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| ハチロク06_のぞみ | 2322 | 「あむっ――ん、うふっ――えと、さ。ハチロク。\nなんですぐ、オリヴィのこと赤ちゃんみたいに扱うの？」 | 「啊嗚……嗯，嘻嘻——就是那個，八六，你為什麼動不動就要把奧莉薇當成小寶寶那樣看待呢？」 | 「Ngoạm――ưm, ufufu――à ừm, nè. Hachiroku.\nTại sao lúc nào cậu cũng đối xử với Olivy như em bé vậy?」 | 「Ngoạm――ưm, Ufu――à ừm, nè. Hachiroku.\nTại sao lúc nào cậu cũng đối xử với Olivy như em bé vậy?」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. JP 「ん、うふっ」 — うふっ = 2 mora → "Ufu" (không phải "Ufufu"). |
| ハチロク09_もくもくオリヴィ | 1608 | 「あら、うふふ。左様ですね」 | 「呀，嘻嘻。您說得沒錯」 | 「Ây da, ufufu. Đúng là vậy nhỉ.」 | 「Ây da, Ufufu. Đúng là vậy nhỉ.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| ハチロク09_もくもくオリヴィ | 2011 | 「それに……うふふっ、わたくしたち実は、\n\x%l客車;#00ffc040;客車%l;#;乗車を、とても楽しみにしております」 | 「而且……嘻嘻，我們其實，也很期待在\x%l客車;#00ffc040;客運車廂%l;#;搭車的感受」 | 「Hơn nữa……ufufu, thực ra chúng tôi,\ncũng đang rất mong chờ được ngồi ở \x%l客車;#00ffc040;toa hành khách%l;#; ạ.」 | 「Hơn nữa……Ufufu, thực ra chúng tôi,\ncũng đang rất mong chờ được ngồi ở \x%l客車;#00ffc040;toa hành khách%l;#; ạ.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| ハチロク14_冬 | 2643 | 「んふふっ」 | 「嘿嘿」 | 「Ưfufu.」 | 「Nfufu.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. んふふ bị dịch sai thành "Ưfufu" → "Nfufu". |
| ハチロク15b_さよなら列車 | 1571 | 「ふぁ……うふふっ――えへへ～。\nね？ おいしー、でしょ？」 | 「呼……唔呼呼——哎嘿嘿～好喝吧？」 | 「Phà……ufufu——ehehe~.\nThấy chưa? Ngon, đúng không?」 | 「Phà……Ufufu——ehehe~.\nThấy chưa? Ngon, đúng không?」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| ハチロクh3_磨き洗い | 1677 | 僕の手の中、すずはほうっと幸せそうな息を吐き、\nやがて、うふふと小さく微笑む。 | 鈴在我的懷抱中幸福地呼氣，不久，又輕輕地微笑起來。 | Trong vòng tay tôi, Suzu khẽ thở hắt ra một hơi hạnh phúc,\nrồi mỉm cười "ufufu" nhỏ nhẹ. | Trong vòng tay tôi, Suzu khẽ thở hắt ra một hơi hạnh phúc,\nrồi mỉm cười "Ufufu" nhỏ nhẹ. | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên.  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| ハチロクh5_おだいどこしごと | 1602 | 言えば、うふふとすずが微笑む。 | 鈴銀鈴般地笑了。 | Nghe tôi nói vậy, Suzu khẽ cười ufufu. | Nghe tôi nói vậy, Suzu khẽ cười Ufufu. | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| ポーレット01_ポーレット退任 | 2547 | ぽわんとした声。\nポーレットもうふふと笑いをもらす。 | 玲奈的聲音還是一如既往軟軟的，引得波萊特也笑了。 | Giọng nói mềm mại, êm ái.\nPaulette cũng khẽ bật cười ufufu. | Giọng nói mềm mại, êm ái.\nPaulette cũng khẽ bật cười Ufufu. | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| ポーレット07_うさぎ | 1644 | 「うふふぅう～、うふふぅう～」 | 「呵呵呵呵呵」 | 「Ufufu~, ufufu~」 | 「Ufufu~, Ufufu~」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| ポーレットh8_気動車の国のアリス | 2370 | 「んふふ、ははひはひはぁ」 | 「嘿嘿，真沒辦法」 | 「Ừm fufu, haha hihi haa」 | 「Nfufu, haha hihi haa」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 仲国04_z49列車 | 2014 | 「まことにたのしうございます！\n横になりながら、うふふっ、列車の旅を楽しめるなんて」 | 「能邊舒服地躺著邊享受列車旅行，嘻嘻，真的是非常開心！」 | 「Thực sự rất vui ạ!\nVừa nằm, ufufu, vừa tận hưởng chuyến du lịch bằng tàu hỏa thế này.」 | 「Thực sự rất vui ạ!\nVừa nằm, Ufufu, vừa tận hưởng chuyến du lịch bằng tàu hỏa thế này.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 仲国06_聖都とパンダとハチロクと | 2513 | 感心すれば、ふふっ、とハチロクは小さく笑う。 | 看到我發出感慨，八六“嘻嘻”地笑了起來。 | Thấy tôi trầm trồ, Hachiroku khẽ cười fufu. | Thấy tôi trầm trồ, Hachiroku khẽ cười Fufu. | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 共通03_ハチロクとナビ | 1546 | 「確かに……ふふっ、とても有意な周辺情報を、\nわたくしは偶然、受け取りました」 | 「確實……嘻嘻，我“偶然”收到了“不尋常”的周邊訊息呢」 | 「Quả thực……fufu, em đã tình cờ,\nnhận được một thông tin xung quanh rất có ý nghĩa.」 | 「Quả thực……Fufu, em đã tình cờ,\nnhận được một thông tin xung quanh rất có ý nghĩa.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 共通06_8620を探せ | 2760 | 懐かしそうに目を細め、\nそれからふふ、と、ハチロクは幸せそうに微笑む。 | 八六懷念地眯起眼睛，接著幸福地發出了“呵呵”的微笑聲。 | Cô ấy nheo mắt lại đầy hoài niệm,\nrồi fufu mỉm cười hạnh phúc. | Cô ấy nheo mắt lại đầy hoài niệm,\nrồi Fufu mỉm cười hạnh phúc. | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 凪h2_おとなの水着 | 2477 | 「んふふ～ それじゃ今度は、\nにーさんに気持ちよくしてもらうばんたい！」 | 「哼哼……那這次就輪到大哥哥讓咱舒服了！」 | 「Ưm fufu~ Vậy thì lần này,\nđến lượt anh hai làm em sướng á!」 | 「Nfufu~ Vậy thì lần này,\nđến lượt anh hai làm em sướng á!」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 凪h2_おとなの水着 | 2479 | 「んふふ――にーさん、かわゆか声ばい」 | 「哼哼哼，大哥哥的聲音好可愛」 | 「Ưm fufu——Anh hai, giọng đáng yêu ghê á」 | 「Nfufu——Anh hai, giọng đáng yêu ghê á」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 凪h2_おとなの水着 | 2540 | 「あ、おちんちんビクビクしたばい！\nんふふっ、気持ちよくなりたかとー？」 | 「啊，雞巴抖了幾下！嘿嘿，想舒服嗎？」 | 「A, dương vật giật giật rồi á!\nƯm fufu, muốn được sướng không á?」 | 「A, dương vật giật giật rồi á!\nNfufu, muốn được sướng không á?」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 凪ふかみ01_凪の成長、ふかみの成長 | 1833 | 「困ったときはお互いさまだよ、凪ちゃん。\nそれに……うふふ、ナビちゃんにも乗れたし、役得っ」 | 「有困難的時候就要互相幫助，小凪。而且……嘻嘻，我還坐上了Ｎａｖｉ，賺到了」 | 「Lúc khó khăn thì phải giúp đỡ lẫn nhau chứ, Nagi.\nHơn nữa……fufufu, tớ còn được cưỡi Navi nữa, lời to rồi.」 | 「Lúc khó khăn thì phải giúp đỡ lẫn nhau chứ, Nagi.\nHơn nữa……Ufufu, tớ còn được cưỡi Navi nữa, lời to rồi.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. うふふ bị dịch sai thành "fufu" → "Ufufu". |
| 凪ふかみ01_流れ | 2252 | 何が違うか、わからない。\nふかみはうふふと、楽しげに微笑し言葉をつなぐ。 | 我不知道這兩個有什麼區別。深美則顯得很高興地微笑著繼續說道： | Tôi không hiểu có gì khác biệt.\nFukami cười fufufu, vui vẻ mỉm cười và tiếp lời. | Tôi không hiểu có gì khác biệt.\nFukami cười Ufufu, vui vẻ mỉm cười và tiếp lời. | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. うふふ bị dịch sai thành "fufu" → "Ufufu". |
| 凪ふかみ07_少しずつ、大人に | 2758 | 凪の、ハチロクの、日々姫の顔がうふふと緩む。\n恐らく僕も、似たような顔をしているだろう。 | 凪、八六、日日姬跟著露出了笑容。大概我也是這副表情吧。 | Gương mặt Nagi, Hachiroku và Hibiki giãn ra với nụ cười 'ufufu'.\nCó lẽ tôi cũng đang làm vẻ mặt tương tự. | Gương mặt Nagi, Hachiroku và Hibiki giãn ra với nụ cười 'Ufufu'.\nCó lẽ tôi cũng đang làm vẻ mặt tương tự. | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. うふふ bị dịch sai thành "fufu" → "Ufufu". |
| 凪ふかみ08a_凪エピローグ_一番ほしい、一番 | 1707 | 「ふ……うふふっ！ うふふふふふふっ！」 | 「嘿……嘿嘿嘿！嘿嘿嘿嘿嘿嘿！」 | 「Phư…… ufufu! Ufufufufufu!」 | 「Phư…… Ufufu! Ufufufufufu!」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 凪ふかみ08a_凪エピローグ_一番ほしい、一番 | 2585 | 凪ちゃんがびくんっ！ って背筋を伸ばす。\n双鉄おにいさんが、ふふって笑う。 | 小凪身子一抖，站得筆直。雙鐵哥哥呵呵地笑了。 | Nagi giật bắn mình! Vươn thẳng lưng lên.\nAnh Soutetsu bật cười fufu. | Nagi giật bắn mình! Vươn thẳng lưng lên.\nAnh Soutetsu bật cười Fufu. | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 凪ふかみ08b_ふかみエピローグ_赤を切る勇気 | 3388 | ふかみちゃんがふふって笑うと、\nにーさんの顔もにこってゆるむ。 | 小深呵呵笑著，大哥哥的嘴角也翹了起來。 | Khi bé Fukami cười fufu,\nkhuôn mặt anh hai cũng giãn ra thành một nụ cười. | Khi bé Fukami cười Fufu,\nkhuôn mặt anh hai cũng giãn ra thành một nụ cười. | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 日々姫02_文庫森 | 1691 | 「んふふっ」 | 「嗯呵呵」 | 「Ưm fufu.」 | 「Nfufu.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 稀咲02_新事業案 | 1900 | 「ああ――ふふっ、なんだ、\nボクの食生活をそこまで心配してくれたんだ」 | 「啊——呵呵，原來你這麼擔心我的飲食呀」 | 「A——fufu, gì chứ,\nhóa ra anh lại lo lắng cho chế độ ăn uống của tôi đến thế sao.」 | 「A——Fufu, gì chứ,\nhóa ra anh lại lo lắng cho chế độ ăn uống của tôi đến thế sao.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên.  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| 稀咲02_新事業案 | 1930 | 「ん……これは――リズムがつかめると……\nふふ、体がかなりキツイけれども――少し、楽しい」 | 「嗯……這樣子——抓准節奏後……呵呵，雖然身體會很累——但有點開心呢」 | 「Ưm…… cái này——một khi đã nắm được nhịp độ thì……\nfufu, mặc dù cơ thể khá mỏi——nhưng lại thấy, hơi vui vui.」 | 「Ưm…… cái này——một khi đã nắm được nhịp độ thì……\nFufu, mặc dù cơ thể khá mỏi——nhưng lại thấy, hơi vui vui.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 稀咲02_新事業案 | 2238 | 「それはそれは……\nうふふ、本当においしかったよ？ 大したものだ」 | 「真沒想到……呵呵，真得很好吃。了不起」 | 「Thật không ngờ……\nfufu, thực sự rất ngon đấy? Giỏi quá đi.」 | 「Thật không ngờ……\nUfufu, thực sự rất ngon đấy? Giỏi quá đi.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. うふふ bị dịch sai thành "fufufu" → "Ufufu". |
| 稀咲03_純白のレール | 1821 | 「ん――ふふっ、やっとだ！ 言わせた！\n我慢するの大変だったよ。ボクから先にいうとこだった」 | 「嗯——嘻嘻，終於！終於讓你說出口了！忍得我可辛苦了，差點就先說出口了」 | 「Ưm——fufu, cuối cùng cũng chịu nói! Bắt anh phải nói ra!\nEm đã phải nhẫn nhịn vất vả lắm đấy. Suýt chút nữa là em đã nói ra trước mất rồi.」 | 「Ưm——Fufu, cuối cùng cũng chịu nói! Bắt anh phải nói ra!\nEm đã phải nhẫn nhịn vất vả lắm đấy. Suýt chút nữa là em đã nói ra trước mất rồi.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. Chỉ viết hoa (JP có ―― tách token). |
| 稀咲h1_性生活 | 1466 | 「なんだ……おっぱい……も――初めて……なの、か――\nんっ――んふふっ――ふっ――んっ――ふあっ――あっ」 | 「這樣啊……胸部……也是――第一次……體驗吧――嗯――嗯唔――呼――嗯――呼啊――啊」 | 「Vậy sao…… sờ ngực…… cũng――là lần đầu tiên…… à――\nƯm――ưm fufu――fu――ưm――fua――a」 | 「Vậy sao…… sờ ngực…… cũng――là lần đầu tiên…… à――\nƯm――Nfufu――fu――ưm――fua――a」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên. |
| 稀咲h1_性生活 | 1473 | 「気持よく……そうか、ふふふ。\n双鉄は、気持ちよく、目覚めたんだね」 | 「醒來的感覺嗎……這樣啊，呵呵。你這麼想就好了」 | 「Tâm trạng sảng khoái…… vậy sao, fufu.\nSoutetsu, thức dậy với tâm trạng sảng khoái nhỉ.」 | 「Tâm trạng sảng khoái…… vậy sao, Fufu.\nSoutetsu, thức dậy với tâm trạng sảng khoái nhỉ.」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên.  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| 稀咲h1_性生活 | 1482 | 「先走り……の……汁……んっ――ふふっ、\n双鉄のペニスは、ボクの髪のこと――好き、みたいだね」 | 「預射……液……嗯――呵呵、雙鐵的陰莖好像很喜歡――我的頭髮啊」 | 「Dịch…… nhờn rỉ ra…… ưm――fufu,\nDương vật của Soutetsu có vẻ――rất thích mái tóc của em nhỉ」 | 「Dịch…… nhờn rỉ ra…… ưm――Fufu,\nDương vật của Soutetsu có vẻ――rất thích mái tóc của em nhỉ」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên.  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| 稀咲h3_チャイナドレスでおもてなし | 2465 | 「普通は、体を見ると思う。男でも、女でさえも。\nでも、双鉄は真っ先にボクの顔を見て――うふふっ」 | 「我覺得一般人都會瞅著身體看，無論男女。但是你就只盯著我的臉看――呵呵」 | 「Bình thường thì, người ta sẽ nhìn vào cơ thể. Dù là đàn ông, hay thậm chí là phụ nữ.\nNhưng mà, Soutetsu lại nhìn vào mặt em đầu tiên――ufufu」 | 「Bình thường thì, người ta sẽ nhìn vào cơ thể. Dù là đàn ông, hay thậm chí là phụ nữ.\nNhưng mà, Soutetsu lại nhìn vào mặt em đầu tiên――Ufufu」 | Token cười viết hoa theo F5 (んふふ→Nfufu, うふふ→Ufufu, ふふ→Fufu); cười là cười, không phải rên.  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|

## 3.4. HAS-RUN — sửa số chữ kéo dài theo M14 (99 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr_ニイロクh_誓い。約束 | 2047 | （ずりゅううううううううううううんっ！！！！！！） | （滑動） | （Trượtttttttttttttttttttttttttttttttttttttttttttttttttt!!!!!!） | （Trượttttttttttt!!!!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_ニイロクh_誓い。約束 | 2048 | （びゅぶっ！ ぶっ！ びゅるっ！！！ びゅううっ！） | （猛烈射精） | （Phụt! Phụt! Phụtttt!!! Phụttttt!） | （Phụt! Phụt! Phụtttt!!! Phụtt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_ハチロクh1_今ひとたびの契り | 2000 | （ずぶうううううううううううっ！ ごつっ！！！） | （緩慢抽出，而後猛然插入） | （Phậppppppppppp! Gotsu!!!） | （Phậpppppppppp! Gotsu!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. Dạng đã đổi bởi đợt gộp trước (romaji → dạng VN "Phậ…"), nay lệch 1 — sửa dạng mới; giữ nguyên token 2 "Gotsu!!!". |
| lr_ハチロクh3_通販失敗いたしましたにゃん | 1909 | （じゅぶうううううううううううっ！！――ごっ！） | （劇烈抽插） | （Phậppppppppppp!! ——Cộc!） | （Phậpppppppppp!! ——Cộc!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_ハチロクh3_通販失敗いたしましたにゃん | 1956 | （ずりゅううううっ！ ごっ！！！\nずりゅううっ――ぐっ――くりゅっ――） | （深淺交錯） | （Phậppppp! Cộc!!!\nPhậpppp——ưm——phập——） | （Phậppp! Cộc!!!\nPhậpp——ưm——phập——） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. Dòng 2 token — sửa cả 2 trong 1 mục (T=4 và T=2). |
| lr_ハチロクh3_通販失敗いたしましたにゃん | 1961 | （じゅぼっ！ ばちゅ！ ぐりゅうううっ！ ごつ！！） | （用力抽送） | （Phập! Phập! Ngoáyyyyy! Cộc!!） | （Phập! Phập! Ngoáyyy! Cộc!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_ハチロクh3_通販失敗いたしましたにゃん | 1965 | （ずぶううううううううううっ！！！！！！） | （直插到底） | （Phậpppppppppp!!!!!!） | （Phậppppppppp!!!!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_ハチロクh3_通販失敗いたしましたにゃん | 1966 | （ぼぢゅうううううっ！！！！――ごつ！ ごりゅっ！） | （直衝頂峰） | （Phậppppp!!!! ——Cộc! Ngoáy!） | （Phậpppp!!!! ——Cộc! Ngoáy!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_凪h1_痛いの痛いの飛んでけばい | 1802 | （こしゅっ！ ぐにっ！ ぬにゅっ！ ぐにゅううっ！） | （揉！捻！按！擦！） | （Chà! Nắn! Xoa! Épppp!） | （Chà! Nắn! Xoa! Épp!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_凪h1_痛いの痛いの飛んでけばい | 1825 | （くりゅっ！ ぐういいいいいいいいいいっっっっ！！） | （擦！捏！！） | （Vê! Đẩyyyyyyyyyyyyyyy!!） | （Vê! Đẩyyyyyyyyyy!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_凪h1_痛いの痛いの飛んでけばい | 1827 | （ずりゅううううううううううううううっっっっ！） | （滋溜！） | （Trượttttt!） | （Trượttttttttttttt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_凪h2_虎さんの交尾 | 1822 | （ずりゅうううううううううううっっっっっっ！！！） | （抽！！！） | （Trượttttt!!!） | （Trượtttttttttt!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_凪h2_虎さんの交尾 | 1826 | （ずりゅうううううううううううううううううっ！！） | （拉！！） | （Trượttttt!!） | （Trượtttttttttttttttt!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_凪ふかみh1_じぇいけい！ | 2299 | （びゅっ！ びゅうう――ずりゅううううううううっ！） | （咻！咻……滋溜！） | （Phụt! Phụt——Trượttttt!） | （Phụt! Phụtt——Trượttttttt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. Dòng 2 token — sửa token2 (T=2) và token3 (T=8) trong 1 mục. |
| lr_凪ふかみh1_じぇいけい！ | 2316 | （ぼっ！ ずるうううううううううううううっっっ！！） | （拔出！！） | （Bộp! Tuộtttttt!!） | （Bộp! Tuộtttttttttttt!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_凪ふかみh1_じぇいけい！ | 2317 | （ずりゅうううううううううううううううっ！！！） | （拔！！！） | （Trượttttt!!!） | （Trượtttttttttttttt!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_日々姫h2_デザートは食事の前に | 1070 | 「うん。結構匂うとよ？ けどね？ にぃにの匂いやけん。\n（すーーーーーーーーーーーーーーーーーーっ）」 | 「嗯，味道挺大的。不過這是阿哥的味道嘛。（深呼吸）」 | 「Vâng. Khá là nặng mùi đấy? Nhưng mà nhé? Là mùi của anh hai mà.\n（Híttttttttttttttttttt）」 | 「Vâng. Khá là nặng mùi đấy? Nhưng mà nhé? Là mùi của anh hai mà.\n（Hítttttttttttttttttt）」 | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_日々姫ふかみh1_凪ちゃんの代わり | 2411 | （びゅぶっ！ ぶっ！ びゅるっ！ びゅううっ！） | （咻噗！噗！咻嚕！咻！） | （Phụt! Phụt! Phụt! Phụtttt!） | （Phụt! Phụt! Phụt! Phụtt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_日々姫ふかみh1_凪ちゃんの代わり | 2416 | （びゅっ！ どびゅっ！！ どびゅる！ びゅううう！） | （咻！咻！咻！咻！） | （Phụt! Phụt!! Phụt! Phụtttt!） | （Phụt! Phụt!! Phụt! Phụttt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_日々姫ふかみh1_凪ちゃんの代わり | 2436 | （ずりゅううううううううううううううううっっっ！） | （套弄！！！！！！！！！！！） | （Tuốtttttttttt!） | （Tuốttttttttttttttt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_日々姫真闇h1_三人家族 | 2366 | （びゅううっ！ ぶっ！ びゅるるっ！ びゅううっ！） | （咻嚕嚕！噗！咻嚕嚕！咻嚕嚕！） | （Phụt! Phụt! Phụt! Phụtttt!） | （Phụt! Phụt! Phụt! Phụtt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. Sửa token4 びゅううっ (scan nhầm token1 do ― nối token). |
| lr_日々姫真闇h1_三人家族 | 2376 | （ぶびっ！ びゅるっ！ びゅううっ！ どびゅっ！） | （噗咻！嗶嚕！咻嚕嚕！嘟咻！） | （Phụt! Phụt! Phụtttt! Phụt!） | （Phụt! Phụt! Phụtt! Phụt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_日々姫真闇h1_三人家族 | 2388 | （さすうううううっ――なでええええええええっっ） | （戳弄——撫摸——） | （Vuốtttttt――Xoa xoa） | （Vuốttttt――Xoa xoa） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_日々姫真闇h1_三人家族 | 2417 | （ずりゅうううううううっ！！！ んごきゅつううう！）\n（さすっ――さわっ――なぜっ――さしゅっ） | （擠壓！磨蹭！！）（輕觸——戳弄——磨蹭——撫摸——） | （Trơn tuộttttttt!!! Ngokyutsuuuu!）\n（Vuốt――Chạm――Xoa――Vuốt） | （Trơn tuộtt!!! Ngokyutsuuuu!）\n（Vuốt――Chạm――Xoa――Vuốt） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_日々姫真闇h1_三人家族 | 2428 | （ぶりゅううううううううううっっ！ ごぢゅううっ！） | （深深滑入！擠壓！） | （Phập! Cộcccc!） | （Phập! Cộc!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_日々姫真闇h1_三人家族 | 2440 | （ぞにゅううううううう！！ ごっぢゅううううん！！） | （用力擠壓！！用力刮蹭！！） | （Phậppppp!! Cộcccc!!） | （Phậpppppp!! Cộccc!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. Dòng 2 token — sửa cả 2 trong 1 mục (T=7 và T=4). |
| lr_日々姫真闇h1_三人家族 | 2441 | （ぶぢゅうううううううううううっ！！！ ごりゅっ！） | （用力頂入！！！磨蹭！） | （Phậppppp!!! Goryu!） | （Phậpppppppppp!!! Goryu!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_真闇h1_僕のおねえちゃん | 2121 | （びゅるっ！ びゅぶっ！ びゅうう！ ぶびゅっっ！） | （咻嚕！ 噗！！ 噗嗚！ 噗滋） | （Rột! Phụt! Phụttt! Phụt!） | （Rột! Phụt! Phụtt! Phụt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_真闇h1_僕のおねえちゃん | 2145 | （びゅぶうううううううううっっっっっ！ ごちゅん！） | （射出————————！ 咕啾！） | （Phụttttttttttt! Ục!） | （Phụttttttttt! Ục!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr_稀咲h1_おしおきとごほうび | 1705 | （ずぶううううううううううっっ！！！ ごちゅっ！！） | （啾嚕嚕嚕嚕嚕！！！咕啾！！） | （Phậpppppppppp!!! Gochu!!） | （Phậppppppppp!!! Gochu!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. Dạng đã đổi bởi đợt gộp trước, nay lệch 1 — sửa dạng mới; giữ nguyên token 2 "Gochu!!". |
| lr_稀咲ポーレットh1_悪い大人の契約 | 2500 | （きゅうううううううううううううっっっ！） | （劇烈收縮！！！！） | （Kíuuuuuuuuuuuuu!） | （Kíuuuuuuuuuuuuuu!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr真闇追加h_赤ちゃん、欲しか | 1803 | （ぶヂュううううううううううううっせ――ごちゅっ！） | （一鼓作氣） | （Phậpppppppppppppppppppppppppp——bập!） | （Phậppppppppppp——bập!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr真闇追加h_赤ちゃん、欲しか | 1824 | （きゅううううううううううううううううっっ！！！） | （咬緊） | （Siếtttttttttttttttttttttttttttttttttt!!!） | （Siếtttttttttttttttt!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr真闇追加h_赤ちゃん、欲しか | 1828 | （むにいいいいいいいいいいいいいいいっっっっっ） | （大力揉搓） | （Bópppppppppppppppppppppppppppppppppppppppp） | （Bóppppppppppppppp） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr真闇追加h_赤ちゃん、欲しか | 1860 | （ずりゅおおおおおっ！ ごりゅ！ ぐちゅううぅっ！\nぬぢゅうううううっ！ ごちゅっ！ ぐりゅりゅうっ！） | （猛烈抽插） | （Trượtttttttttttt! Xoáy! Phậppppp!\nLún sâubuuuuuu! Bập! Xoáy xoáy!） | （Trượtttt! Xoáy! Phậpp!\nLún sâubuuuuuu! Bập! Xoáy xoáy!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. Dòng 2 token — sửa token1 (T=5) và token3 (T=3) trong 1 mục; token giữa "Lún sâubuuuuuu!" ĐÚNG (7u), không sửa. |
| lr真闇追加h_赤ちゃん、欲しか | 1883 | （ずろおおおおおおおおおおおおおおおおおおっっ） | （艱難拔出） | （Trượtttttttttttttttttttttttttttttttttt） | （Trượttttttttttttttttt） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 2315 | 「（じゅびゅぅぅぅぅぅぅぅぅぅぅぅぅぅっっっっ！）」 | 「（啾嗶溜——）」 | （Chụtttttttttttttttttttttttttttttttttttttttttttttt!） | （Chụttttttttttttt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 2317 | 「（ずじゅううううぅぅぅぅぅぅぅぅぅぅぅぅぅぅ！）」 | 「（滋啾——）」 | （Chụtttttttttttttttttttttttttttttttttttttttttttttt!） | （Chụtttttttttttttttttt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 3051 | （きゅうううううううううっっ！！！！） | （劇烈收縮） | （Siếtttttttttttttttttttttttttttttttttttttttttttttt!!!!） | （Siếttttttttt!!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 3053 | （びゅぶっ！ どびゅっ！ びゅうう！ ぶひゅ！） | （勢如破竹） | （Phụt! Phụt! Phụttttt! Phụt!） | （Phụt! Phụt! Phụtt! Phụt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 3057 | （ぐりいいいいいっっ！！ ずりゅっ！ ごちゅっ！） | （反覆頂弄） | （Cọọọọọọọọọ!! Trượt! Phập!） | （Cọọọọọọ!! Trượt! Phập!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 3060 | （すうううううううううううっ） | （吸氣） | （Trượtttttttttttttttttttttttt） | （Trượtttttttttt） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 3102 | （ちいいいいいいっ） | （拉開拉鏈） | （Xoètttttttt） | （Xoètttttt） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 3106 | （きゅうううんっっ） | （收緊） | （Siếtttttttttttt） | （Siếttt） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 3107 | （ぎゅりゅうううううううううっっっっっっっっ！！） | （收縮） | （Phậpppppppppppppppppppppppppppppppppppppppppppppppp!!） | （Phậpppppppp!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 3111 | （ごりゅうううううううっ！ ずりゅっ！ ばちゅん！） | （橫衝直撞） | （Phậpppppppppppppppp! Trượt! Phập!） | （Phậpppppp! Trượt! Phập!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 3118 | （ずりゅうううううぅぅぅぅぅぅぅぅぅぅぅぅぅっっ） | （滋溜溜溜溜溜） | （Trượtttttttttttttttttttttttttt） | （Trượttttttttttttttttt） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 3126 | （ずびゅううううううううううううっっ！ ばちんっ！） | （直搗黃龍） | （Phậpppppppppppppppppppppppppppp! Chát!） | （Phậppppppppppp! Chát!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| lr追加_みくろ＆日々姫h「みくろのマスター」 | 3130 | （きゅっ！ ぎゅううううう！！！ きゅきゅんんっ！） | （緊緊包裹） | （Siết! Siếtttttttt!!! Siết chặt!） | （Siết! Siếttttt!!! Siết chặt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| れいなh1_おかあさんのレッスン | 2328 | （んびゅっ――びゅるっ――びゅううっ――びゅっ――） | （咻咻……咻咻……咻咻……咻咻……） | （Phụt――phụt――phụttttt――phụt――） | （Phụt――phụt――phụtt――phụt――） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| れいなh1_おかあさんのレッスン | 2345 | （ずぶううううううううっ！――ごつっ！） | （啾嚕嚕嚕！） | （Phậpppppppp!——Bạch!） | （Phậppppppp!——Bạch!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| れいなh1_おかあさんのレッスン | 2346 | （にゅろおおおおおおおおっ！！！） | （啾嚕！！！） | （Sụttttttttttt!!!） | （Sụtttttttt!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| れいなh2_おもらし防止大作戦 | 1734 | （ずぶううううううっ！ ずんっ！ ごつっ！） | （咕啾、咕啾！） | （Phậpppppp! Phập! Bạch!） | （Phậppppp! Phập! Bạch!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| れいなh2_おもらし防止大作戦 | 1737 | （ずろおおおおおっ！ ぐっ！ ぞり！ ぞりゅりゅ！） | （咕啾！咕啾！咕啾！！） | （Phậpppppp! Phập! Rột! Rột!） | （Phậpppp! Phập! Rột! Rột!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| れいなh2_おもらし防止大作戦 | 1758 | （れりゅうううううううううううっ――つぷっ！） | （啾嚕嚕嚕嚕！） | （Chụtttttt——chụt!） | （Chụttttttttttt——chụt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| れいなh2_おもらし防止大作戦 | 1764 | （ぐいいいいいいいいっ！！） | （插入！！） | （Phậpppppp!!） | （Phậppppppp!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| れいなh3_おもらし自由化大作戦 | 1721 | （ずりゅううううううっ！ ずぶんっ！！） | （咕啾、咕啾！！） | （Nhópppppppp! Phậpppppp!!） | （Nhópppppp! Phậpppppp!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| れいなh3_おもらし自由化大作戦 | 1738 | （ぞろおおおおおおおおおおおおおおおおおおっ！！！） | （啾嚕嚕嚕！！！） | （Rộtttttttttttttttttttttttttttttttttttttttt!!!） | （Rộtttttttttttttttttt!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| れいなh3_おもらし自由化大作戦 | 1740 | （ぷしゃあああああああああああああっ！） | （嘩啦啦啦！） | （Àooooooooooooooo!） | （Àoooooooooooooo!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| れいなh3_おもらし自由化大作戦 | 1747 | （ずぶうううううううっ！！！！） | （插入！！！！） | （Phậpppppppppppp!!!!） | （Phậpppppp!!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ハチロクh3_磨き洗い | 1835 | （ずぶうううううううううううっ！） | （插——！） | （Phậppppppppppp!!!） | （Phậpppppppppp!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. Dạng đã đổi bởi đợt gộp trước, nay lệch 1 — sửa dạng mới. |
| ハチロクh7_レトロモダンメイクラヴ | 1811 | （みちいいいいいいいいいいいいいいいいいっ！！！！） | （吱嚕——！！！！） | （Phậpppppppppppppppppppppp!!!!） | （Phậpppppppppppppppp!!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ハチロクh7_レトロモダンメイクラヴ | 1820 | （ずぶううううううううううううううううっ！！！） | （呲噗——！！！） | （Phậpppppppppppppppppppp!!!） | （Phậppppppppppppppp!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ハチロクh7_レトロモダンメイクラヴ | 1824 | （つぷうぅぅ） | （呲噗） | （Phậpppp） | （Phậpp） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ハチロクh7_レトロモダンメイクラヴ | 1826 | （ずろおおおおおおおおおお！！！） | （呲嚕——！！！） | （Phậppppppppppp!!!） | （Phậppppppppp!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ハチロクh7_レトロモダンメイクラヴ | 1844 | （くぽっっ――ちゅうううううっ――ぷりゅんっ！） | （唔哦——啾嗚嗚嗚——噗嚕！） | （Mút——chùn chụttttt——bật nảy!） | （Mút——chùn chụtttt——bật nảy!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ハチロクh8_桜色のひめごと | 1528 | （ずぶううううううううううっ！！！ ごっ！！） | （呲噗——！！！！！） | （Phậpppppppppp!!! Cộc!!） | （Phậppppppppp!!! Cộc!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ハチロクh8_桜色のひめごと | 1558 | （ごきゅんっ！！ ――ちゅううううううううううっ！） | （啾！！——啾嗚——！） | （Ực!! ——Chụtttttttttttttttt!） | （Ực!! ——Chụtttttttttt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ハチロクh8_桜色のひめごと | 1572 | （びゅううう！ びゅっ！ びゅる！ びゅるんつ） | （噗嚕嗚！噗！噗！噗） | （Phụtttt! Phụt! Phụt! Phụt） | （Phụttt! Phụt! Phụt! Phụt） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ハチロクh8_桜色のひめごと | 1581 | （にゅぼぉぉぉぉぉぉぉぉぉぉぉぉっっっ！） | （扭啵——！） | （Thọcccccccccccccccccccc!） | （Thọcccccccccccc!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ハチロクh9_コノフクハキルコト | 3502 | （びゅううっ！ びゅっ！ びゅるるっ！ びゅうっ！） | （噗嚕！噗！噗嚕！噗嚕！） | （Phụttt! Phụt! Phụt phụt! Phụttt!） | （Phụtt! Phụt! Phụt phụt! Phụttt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ポーレットh3_誘惑アイスコーヒー | 1655 | （びゅっ！ びゅるっ！ びゅむっ！ びゅううっ！） | （噗嚕！噗噗！噗噗！噗嚕！） | （Phụt! Phụt! Phụt! Phụtttt!） | （Phụt! Phụt! Phụt! Phụtt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ポーレットh4_クリーム＆クリーム | 1590 | （びゅううっ！ びゅろっ！） | （噗噗！噗嚕！） | （Phụtttt! Phụt!） | （Phụtt! Phụt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ポーレットh4_クリーム＆クリーム | 1624 | （にゅろおおおっ） | （舔來舔去） | （Liếmmmmm） | （Liếmmm） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ポーレットh4_クリーム＆クリーム | 1627 | （きゅっ！ きゅううううんっ！！） | （蜜道箍緊） | （Siết! Siếtttttt!!） | （Siết! Siếtttt!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ポーレットh4_クリーム＆クリーム | 1638 | （ぐりゅううううっ！！） | （頂到深處） | （Ngoáyyyyyyy!!） | （Ngoáyyyy!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ポーレットh5_裸エプロンのレモンドレッシング和え | 1722 | （ずちゅううっ！！！！） | （猛吸） | （Mútttttttt!!!!） | （Mútt!!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ポーレットh5_裸エプロンのレモンドレッシング和え | 1735 | （ずぶうううううううううううっ！！！） | （長驅直入） | （Phậppppppppppppp!!!） | （Phậpppppppppp!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ポーレットh6_あなたとふたりの学園エッチ | 1558 | （びゅっ――びゅううっ――びゅるっ！ どびゅっっ！） | （噗嚕——噗嚕——噗嚕！噗噗！） | （Phụt——phụtttt——phụt! Phụtttt!） | （Phụt——phụtt——phụt! Phụtt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ポーレットh6_あなたとふたりの学園エッチ | 1560 | （びゅっ！ びゅるっ！ びゅううっ！ びゅっ！！！） | （噗嚕！噗嚕！噗噗！噗噗！！！） | （Phụt! Phụt! Phụtttt! Phụt!!!） | （Phụt! Phụt! Phụtt! Phụt!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ポーレットh6_あなたとふたりの学園エッチ | 1580 | （ずるううう――ぐんっ！） | （抽動） | （Trượttttt——dập!） | （Trượtt——dập!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ポーレットh8_気動車の国のアリス | 3751 | （つぷうううううっ――ぞりゅっ） | （撓撓） | （Phậppppppp——rột） | （Phậpppp——rột） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| ポーレットh8_気動車の国のアリス | 3770 | （ずりゅううっ――ずっ――ぬぢゅううっ――ずるっ） | （頂來頂去） | （Thọc sâuuuuu——thọc——rút raaaaa——rút） | （Thọc sâuuuuu——thọc——rút raaa——rút） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 凪h2_おとなの水着 | 4010 | （びゅぶっ！ びゅっ！ びゅるううっ！ びゅぶっ！） | （咻！咻！咻！咻！） | （Phụt! Phụt! Phụttt! Phụt!） | （Phụt! Phụt! Phụtt! Phụt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 凪h2_おとなの水着 | 4040 | （ぶちゅううううううっ！！！ ごんんっ！！！！） | （插！！！插！） | （Phậppppppppppp!!! Bụp!!!!） | （Phậppppp!!! Bụp!!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 凪h2_おとなの水着 | 4064 | （じゅるうううっっ！！） | （緊！！） | （Sụttttttt!!） | （Sụttt!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 凪ふかみh2_みずあそび | 2132 | （びゅっ！ びゅるうううっ！ びゅぶっ！ びゅっ！） | （呲！呲！呲！呲！） | （Phụt! Phụttttt! Phụt! Phụt!） | （Phụt! Phụttt! Phụt! Phụt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 凪ふかみh2_みずあそび | 2133 | （ぶっ！ ぶびゅうっ！ びゅっ！ びゅううっ） | （呲！呲！呲！呲） | （Phụt! Phụtttt! Phụt! Phụtttt） | （Phụt! Phụtttt! Phụt! Phụtt） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 凪ふかみh2_みずあそび | 2149 | （ずるうううううううううううっ！！） | （拔！！） | （Rútttt!!） | （Rúttttttttttt!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 凪ふかみh2_みずあそび | 2150 | （ずるうううううううううっ！） | （拔！） | （Rúttttt!） | （Rúttttttttt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 凪ふかみh2_みずあそび | 2154 | （ずばっ！ ずばんっ！ ずぱっ！ ずぶううっ！） | （插！插！插！插！） | （Phập! Phập! Phập! Phậppppp!） | （Phập! Phập! Phập! Phập!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 凪ふかみh2_みずあそび | 2163 | （ばっしゃーーーーーん！） | （撲通！） | （Ùmmmm!） | （Ùmmmmm!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 日々姫h1_マッサージの続き | 1892 | （ずりゅうううううううううっ！！！！） | （插入！！！！） | （Phậppppppppp!!!!） | （Phậpppppppp!!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 日々姫h2_洗って大丈夫なスーツ | 1787 | （ずるうううううっっ！！！） | （抽插） | （Trượttttt!!!） | （Trượtttt!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 日々姫h4_いもうとタオル | 1757 | （ずぶうううううううううっ！！！） | （噗呲！！！） | （Phậppppppppp!!!） | （Phậpppppppp!!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. Dạng đã đổi bởi đợt gộp trước, nay lệch 1 — sửa dạng mới. |
| 真闇h2_無濾過 | 1820 | （ずぶうううううううっ！） | （吱噗！） | （Phậppppppp!） | （Phậpppppp!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. Dạng đã đổi bởi đợt gộp trước, nay lệch 1 — sửa dạng mới. |
| 真闇h2_無濾過 | 1884 | （ずろおおおおおおおおっっっ！） | （蹭！） | （Trượttttttttt!） | （Trượttttttt!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 稀咲h3_チャイナドレスでおもてなし | 3786 | （じゅるううううううっ！！） | （啾嚕！！ ） | （Chụttttt!!） | （Chụtttttt!!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |
| 稀咲h3_チャイナドレスでおもてなし | 3819 | （ずろおおおおおおっ！） | （蹭！） | （Cọooooo!） | （Cọoooooo!） | Sửa số chữ kéo dài theo M14 (tổng = 1 + số dấu dài trong JP); giá trị CUR lệch so với target. |

## 3.5. M10 — ふえっ trong chuỗi rên → "Fue" (2 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| ポーレットh2_制服変更？ | 929 | 「ひゃっ――あっ！\nんううっ――ふえっ――ふやぁっ」 | 「呀——啊！嗯——呼——呀」 | 「Hya——á!\nNuu——phuê——Fuyaa.」 | 「Hya——á!\nNuu——Fue——Fuyaa.」 | ふえっ trong chuỗi rên → "Fue" (quyết M10, quy tắc 1). |
| ポーレットh2_制服変更？ | 957 | 「ふぇ……あ……ふやぁぁぁあ」 | 「呼……啊……啊呀」 | 「Phuê... a... Fuyaaaaa.」 | 「Fue... a... Fuyaaaaa.」 | ふえっ trong chuỗi rên → "Fue" (quyết M10, quy tắc 1). |

## 3.6. M18 — くぅん → "Kuuun" (1 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr_ポーレットh2_デコレーション＆ミルク | 1084 | 「はっ――あうっ――ふぁんっ――んっ――くぅんっ――\nん。これ――ゆっくり――はっ――ゆっくぃ、らのにぃ」 | 「啊——啊唔——呼啊——嗯——咕嗯——嗯。這樣——慢慢擺動——哈——明明動作那麼慢」 | 「Ha——au——Fan——ưm——kuuun——\nƯm. Thế này——chậm rãi——ha——chậm rãi, thế mà」 | 「Ha——au——Fan——ưm——Kuuun——\nƯm. Thế này——chậm rãi——ha——chậm rãi, thế mà」 | くぅん → "Kuuun" viết hoa theo F5 (token romaji giữa dòng).  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|

## 3.7. M27 — （ふわっ) → "Fuwa" (1 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| ハチロクh7_レトロモダンメイクラヴ | 1831 | （ふわっ） | （呼哇） | （Nhẹ nhàng） | （Fuwa） | （ふわっ) là âm thở (TW 呼哇); "Nhẹ nhàng" là trạng từ, mất âm → romaji "Fuwa". |

## 3.8. M28 — （ぷぁん！) → "Bụp!" (1 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| 凪ふかみ04_ふかみの決意 | 3294 | （ぷぁん！） | （砰！） | （Tuýt!） | （Bụp!） | （ぷぁん！) + TW 砰 = tiếng nổ/bụp, không phải huýt sáo → "Bụp!". |

## 3.9. M37 — んちゅうっ → "Nchuu" (1 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| 真闇h1_長期熟成 | 1058 | 「ちゅるるっ――ちゅっ――れりゅっ――んちゅうっ」 | 「啾嚕――啾――舔――嗯啾」 | 「Chururu――chụt――rột――ưm chuu.」 | 「Chururu――chụt――rột――Nchuu.」 | んちゅうっ → "Nchuu" theo F1/M15 (1 âm = 1 cách diễn). |

## 3.10. M47 — bỏ "ưm" bịa thêm (がっ) (1 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| れいなh1_おかあさんのレッスン | 1534 | 「は……ぁっ――んっ――きて、るっ――\n来てるっ――双鉄、くん――がっ――」 | 「蛤啊……嗯……進來了……雙鐵君……」 | 「Ha……a——ưm——vào, rồi——\nVào rồi——anh Soutetsu——ưm——」 | 「Ha……a——ưm——vào, rồi——\nVào rồi——anh Soutetsu——」 | がっ là trợ từ が + っ cắt câu, không phải token âm; bỏ "ưm" bịa thêm ở cuối dòng. |

## 3.11. M51 — độ dài ふー (1 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr_凪h2_虎さんの交尾 | 1313 | 「えへへっ！ 嬉しかっ――\nふーーっ、ふーっ、ふーーーっ、ふーーーーっ」 | 「嘿嘿嘿！好開心……呼，呼……呼……呼……」 | 「Ehehe! Vui quá——\nPhù——phù——phù——phù——」 | 「Ehehe! Vui quá——\nPhùuu——phùu——phùuuu——phùuuuu——」 | Độ dài ふー theo M14: 3/2/4/5u → "Phùuu——phùu——phùuuu——phùuuuu——". |

## 3.12. M61 — "phụ——t" → "Phụtt" (1 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr_日々姫h2_デザートは食事の前に | 1665 | （びゅっ！ ぶびゅうっ！ びゅっ――びゅ――りゅっ） | （咻咻……咻咻……） | （Phụt! Bắn ra! Phụt——phụ——t） | （Phụt! Bắn ra! Phụt——Phụtt） | "phụ——t" là lỗi tách giữa từ; quy ước của file cho びゅ kéo dài là "Phụtt". |

## 3.13. M62 — むちゅっ → "Muchu" (2 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| ハチロクh9_コノフクハキルコト | 2035 | 「ふっ……あっ――んっ――れるるっ――ちゅっ――\nれろっ――れりゅうっ――るっ――ん――むちゅっ」 | 「呼……啊——咻嚕——啾——嗯——嗚啾嗚——嚕——姆啾」 | 「Hu……a——ưm——rộp——chụt——\nliếm láp——mút mát——rộp——ưm——mu chu」 | 「Hu……a——ưm——rộp——chụt——\nliếm láp——mút mát——rộp——ưm——Muchu」 | むちゅっ → "Muchu" (tiền lệ ポーレットh4 930). |
| 稀咲h2_プライベートルーム | 1199 | 「ちゅっ――ちゅうっ――ちゅっ――むちゅっ――」 | 「啾――啾――啾――唔啾――」 | 「Chụt――chụt――chụt――mu chu――」 | 「Chụt――chụt――chụt――Muchu――」 | むちゅっ → "Muchu" (tiền lệ ポーレットh4 930). |

## 3.14. M63 — khôi phục "Ư" đầu dòng (1 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| 稀咲h2_プライベートルーム | 912 | 「っ――あ――…………うむ。\n呼吸や顔が変わっていたとは、気付かなかったが」 | 「――啊――…………嗯。我都沒注意到自己表情和呼吸的變化」 | 「A――ờ――………… ừm.\nTôi không nhận ra là hơi thở hay nét mặt của mình đã thay đổi đâu」 | 「Ư――A――ờ――………… ừm.\nTôi không nhận ra là hơi thở hay nét mặt của mình đã thay đổi đâu」 | っ đầu dòng bị mất hẳn trong CUR; khôi phục "Ư" theo M5. |

## 3.15. F5 — viết hoa token romaji SFX (4 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| lr_ニイロクh_誓い。約束 | 1322 | 「！ ならっ、これ、愛撫っ──ンっ──こしゅ。こしゅ、\nで──気持ち、よく、して、くれてるの──ふあっ」 | 「啊！那這個、愛撫——嗯——摸來摸去——讓我這麼、舒服——呼啊」 | 「! Vậy, cái này, ái ân vuốt ve──ưm──cọ. Cọ,\nthế này──là đang làm cho tôi, sướng──fua.」 | 「! Vậy, cái này, ái ân vuốt ve──ưm──cọ. Cọ,\nthế này──là đang làm cho tôi, sướng──Fua.」 | Token romaji SFX viết hoa ở mọi vị trí (quyết F5, coordinator 22/11 ~12:50).  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| lr_ニイロクh_誓い。約束 | 1387 | 「しゅごい、のっ！ ぜんぶっ──ふあっ！ あっ！\nなか、ねっ！ おんなのこっ ちつ、が──ちつない！」 | 「好厲害！全部都——呼啊！啊！進來了！女孩子的、陰道的——裡面！」 | 「Tuyệt, quá! Tất cả──fua! A!\nBên trong, nè! Bé gái, âm đạo──bên trong âm đạo!」 | 「Tuyệt, quá! Tất cả──Fua! A!\nBên trong, nè! Bé gái, âm đạo──bên trong âm đạo!」 | Token romaji SFX viết hoa ở mọi vị trí (quyết F5, coordinator 22/11 ~12:50).  [GHÉP — đã gộp ở U15b/U16, bỏ khỏi JSON gộp; xem Phụ lục gộp cuối REVIEW.]|
| lr_日々姫真闇h1_三人家族 | 1445 | 「ひあっつ！？ あっ――やあっ！ こぎゃんっ――\nこぎゃんっ――つよ、かと――おねえちゃん――知らん」 | 「呀啊！？啊——呀啊！這樣弄——這樣弄——太強烈了——姐姐可——不管了」 | 「Hiat!? A――ya! Thế này――\nThế này――mạnh, quá――chị――không biết đâu.」 | 「Hiat!? A――Ya! Thế này――\nThế này――mạnh, quá――chị――không biết đâu.」 | Token romaji SFX viết hoa ở mọi vị trí (quyết F5, coordinator 22/11 ~12:50). |
| 真闇h2_無濾過 | 1084 | 「きゅっ！ ふっ――やっ――ぁっ――ぁあっ、んっ！」 | 「啾！ 呼――呀――啊――啊啊、嗯！」 | 「Kyu! Phư――ya――a――aa, ưm!」 | 「Kyu! Phư――Ya――a――aa, ưm!」 | Token romaji SFX viết hoa ở mọi vị trí (quyết F5, coordinator 22/11 ~12:50). |

## 3.16. G15 — bỏ markup ruby [x,n] rò rỉ (29 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| グランドリライト03_日々姫 | 1470 | 「――『[ハチロクニイマル,3]8620運転台通信』」 | 「——“８６２０駕駛台通信”」 | 「――『Bản tin Buồng lái [ハチロクニイマル,3]8620』」 | 「――『Bản tin Buồng lái 8620』」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| グランドリライト03_日々姫 | 1491 | 「『[ハチロク,3]8620運転台通信！』\nよかね！ よか！ まっこと良かとよ！！」 | 「“８６２０駕駛台通信！”好啊！好極了！真的太好了！！」 | 「『Bản tin Buồng lái [ハチロク,3]8620!』\nTuyệt quá! Tuyệt lắm! Thật sự rất tuyệt luôn đó!」 | 「『Bản tin Buồng lái 8620!』\nTuyệt quá! Tuyệt lắm! Thật sự rất tuyệt luôn đó!」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| グランドリライト03_日々姫 | 2475 | 「[ハチロクニイマル,3]8620のこと。にぃ――\n兄さんと二人だけで見るのって、初めてですね」 | 「這是第一次跟阿哥——跟哥哥兩個人一起看８６２０呢」 | 「Về [ハチロクニイマル,3]8620. Anh――\nĐây là lần đầu tiên hai anh em mình cùng nhau ngắm nó nhỉ.」 | 「Về 8620. Anh――\nĐây là lần đầu tiên hai anh em mình cùng nhau ngắm nó nhỉ.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| グランドリライト09_凪 | 1489 | 「それでも、思い切って来てよかったです！\n[うちのこ,4]38696もきっと、園のみんなと喜んでくれてます！」 | 「但是，下定決心來這裡真是太好了！[那孩子,4]３８６９６和動物園的朋友們肯定都會很高興！」 | 「Dù vậy, em quyết tâm đến đây thật là tốt quá!\nChắc chắn [đứa bé đó,4]38696 cũng đang cùng mọi người trong sở thú vui mừng cho em!」 | 「Dù vậy, em quyết tâm đến đây thật là tốt quá!\nChắc chắn 38696 cũng đang cùng mọi người trong sở thú vui mừng cho em!」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| グランドリライト09_凪 | 1716 | 「お姉様に来てもらえるの、嬉しいです！\n[うちのこ,4]38696の、なにより素敵なご褒美になります！」 | 「姐姐大人能來大牟田，美玖路真是太開心了！這對[那孩子,4]３８６９６來說就是最棒的獎勵！」 | 「Chị hai có thể đến, em vui lắm ạ!\nĐó sẽ là phần thưởng tuyệt vời hơn bất cứ thứ gì dành cho [đứa bé đó,4]38696!」 | 「Chị hai có thể đến, em vui lắm ạ!\nĐó sẽ là phần thưởng tuyệt vời hơn bất cứ thứ gì dành cho 38696!」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| グランドリライト09_凪 | 1884 | 「[うちのこ,4]38696を置いてくの、[おおむた,2]雄武田を離れるの、\nみくろ、ほんとに不安だったんですけど――」 | 「留下[那孩子,4]３８６９６，離開大牟田，美玖路真的覺得好擔心——」 | 「Để [đứa bé đó,4]38696 lại, rời khỏi Omuta,\nMikuro, thực sự đã rất bất an, nhưng mà――」 | 「Để 38696 lại, rời khỏi Omuta,\nMikuro, thực sự đã rất bất an, nhưng mà――」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| グランドリライト10_ハチロク | 1181 | 「……[わたくしたち,1]列車は、止まれていたのです。\nあの十四秒があれば。\x%l脱線転覆;#00ffc040;脱線転覆%l;#;などさせずとも」 | 「……[我們,1]列車就能停下來的。有了那十四秒，就能避免發生\x%l脱線転覆;#00ffc040;脫軌傾覆%l;#;事故了」 | 「……[わたくしたち,1]Đoàn tàu, đã có thể dừng lại.\nNếu có mười bốn giây đó. Dù không cần phải \x%l脱線転覆;#00ffc040;trật bánh lật tàu%l;#; đi chăng nữa」 | 「……Đoàn tàu, đã có thể dừng lại.\nNếu có mười bốn giây đó. Dù không cần phải \x%l脱線転覆;#00ffc040;trật bánh lật tàu%l;#; đi chăng nữa」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| ハチロク04_煙には煙を | 2166 | 「承りました。[マイ・マスター,2]双鉄様」 | 「明白。[我的主人,3]雙鐵少爺」 | 「Em đã hiểu. Thưa ngài Soutetsu, [マイ・マスター,2]Master của em.」 | 「Em đã hiểu. Thưa ngài Soutetsu, Master của em.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| ハチロク05_軋み | 1437 | 「違かとよ。御一夜商店会の中からのクレームじゃなか。\nおかげで繁盛しとるけん、こっちはむしろ\x%l8620;#00ffc040;[ハチロク,3]8620%l;#;様様」 | 「不是咧。不是御一夜商店協會裡的人投訴的哦。那邊生意興隆，他們感謝\x%l8620;#00ffc040;[八六,3]８６２０%l;#;還來不及」 | 「Không phải đâu. Không phải là khiếu nại từ bên trong Hiệp hội Thương mại Ohitoyo đâu.\nNhờ có nó mà buôn bán phát đạt, bên này còn đang phải cảm tạ \x%l8620;#00ffc040;[Hachiroku,3]8620%l;#; ấy chứ.」 | 「Không phải đâu. Không phải là khiếu nại từ bên trong Hiệp hội Thương mại Ohitoyo đâu.\nNhờ có nó mà buôn bán phát đạt, bên này còn đang phải cảm tạ \x%l8620;#00ffc040;8620%l;#; ấy chứ.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| ハチロク06_のぞみ | 2671 | 「例えば……[オクシデント・エクスプレス,3]西方急行みたいな、\n超豪華観光周遊列車を日ノ本にも走らせるとか」 | 「比方說……就學[Ｏｃｃｉｄｅｎｔ·Ｅｘｐｒｅｓｓ,3]西方快車那種，在日本也開闢一條超豪華觀光周遊列車線路」 | 「Ví dụ như…… chạy một chuyến tàu du lịch vòng quanh siêu sang trọng\nnhư [Occident Express,3]Tàu tốc hành Phương Tây ở Hinomoto chẳng hạn」 | 「Ví dụ như…… chạy một chuyến tàu du lịch vòng quanh siêu sang trọng\nnhư Tàu tốc hành Phương Tây ở Hinomoto chẳng hạn」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| ハチロク15a_痛みとの決別 | 1436 | 「[タブレット・レベル,2]全開放……」 | 「[核心級,1]全面……」 | 「[タブレット・レベル,2]Mở khóa toàn bộ……」 | 「Mở khóa toàn bộ……」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| ハチロク15a_痛みとの決別 | 2049 | 「そんな、ことない！ オリヴィ、[メリケン,2]冥国製、だけど、\nマスター、\x%lレイルロオド;#00ffc040;レイルロオド%l;#;、じゃ、ない、けどっ」 | 「才沒有！奧莉薇，雖然是美國製造的，雖然和你，不是定組的，司機，和，\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;」 | 「Không, có chuyện đó đâu! Olivy, dù được sản xuất tại [メリケン,2]Meriken,\ndù anh không phải là Master, hay \x%lレイルロオド;#00ffc040;Railord%l;#;, đi chăng nữa」 | 「Không, có chuyện đó đâu! Olivy, dù được sản xuất tại Meriken,\ndù anh không phải là Master, hay \x%lレイルロオド;#00ffc040;Railord%l;#;, đi chăng nữa」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| ハチロク15a_痛みとの決別 | 2178 | 「[じくじゅう,1]軸重！！ 8620よりも、ずうっと軸重の軽かけん！！\nⅨ号！ Ⅸ号機関車ば走らせればよかとよ！！！」 | 「軸重！！九號的軸重可比８６２０輕老多了！！讓九號機車上不就行了嘛！！！」 | 「[じくじゅう,1]Tải trọng trục!! Nhẹ hơn 8620 rất nhiều!!\nĐầu máy số 9! Cứ cho đầu máy số 9 chạy là được mà!!!」 | 「Tải trọng trục!! Nhẹ hơn 8620 rất nhiều!!\nĐầu máy số 9! Cứ cho đầu máy số 9 chạy là được mà!!!」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| ハチロク15a_痛みとの決別 | 2199 | 「では、まずは[フォースリブート,4]強制再起動から試みますか」 | 「那就先從強制重啟開始試試」 | 「Vậy thì, trước tiên hãy thử [フォースリブート,4]khởi động lại bắt buộc xem sao」 | 「Vậy thì, trước tiên hãy thử khởi động lại bắt buộc xem sao」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| ハチロク15b_さよなら列車 | 1683 | 「俺も驚いた。しかも、[やつしろ,2]八ツ城行きの乗務――\n本線を、Ⅸ号で走るとはな」 | 「我也很驚訝。而且這趟車是去八代方向的，沒想到能用九號跑這條幹線」 | 「Tao cũng bất ngờ lắm. Hơn nữa lại còn là chuyến tàu đi [やつしろ,2]Yatsushiro——\nKhông ngờ lại được chạy đầu máy số 9 trên tuyến chính đấy」 | 「Tao cũng bất ngờ lắm. Hơn nữa lại còn là chuyến tàu đi Yatsushiro——\nKhông ngờ lại được chạy đầu máy số 9 trên tuyến chính đấy」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| ハチロク15b_さよなら列車 | 1689 | 「御一夜鉄道、\x%l車掌;#00ffc040;車掌%l;#;の早瀬です。あの――増結、\n[けいきゃくしゃ,2]軽客車を二両増結できるかって、駅長さんから」 | 「我叫早瀨，是御一夜鐵路\x%l車掌;#00ffc040;列車長%l;#;。請問——站長問能不能加掛兩節輕型客車」 | 「Tôi là Hayase, \x%l車掌;#00ffc040;trưởng tàu%l;#; của Đường sắt Ohitoyo. Dạ——Trưởng ga hỏi là,\ncó thể ghép thêm hai [けいきゃくしゃ,2]toa hành khách nhẹ nữa không ạ」 | 「Tôi là Hayase, \x%l車掌;#00ffc040;trưởng tàu%l;#; của Đường sắt Ohitoyo. Dạ——Trưởng ga hỏi là,\ncó thể ghép thêm hai toa hành khách nhẹ nữa không ạ」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて | 958 | 「妹たちのことも――共感のことの、なにも、かも――\n[わたくしの半身,3]8620のことさえも、つながってる時、消えて、しまって」 | 「妹妹們的事——同感的事、一切的一切——連我[半身,3]8620的事，在於你相連的時候，全都消失了」 | 「Cả chuyện của các em gái——chuyện cộng cảm, mọi thứ——\nngay cả chuyện của [nửa kia của em,3]8620, khi kết nối với ngài, cũng tan biến, mất.」 | 「Cả chuyện của các em gái——chuyện cộng cảm, mọi thứ——\nngay cả chuyện của 8620, khi kết nối với ngài, cũng tan biến, mất.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| ポーレット11_記憶と記録 | 1512 | 「ならば、[ハチロク,3]8620でも構わんでしょう」 | 「既然如此，換成[八六,3]８６２０也一樣吧」 | 「Nếu vậy, dùng [Hachiroku,3]8620 cũng được mà đúng không.」 | 「Nếu vậy, dùng 8620 cũng được mà đúng không.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| ポーレット11_記憶と記録 | 1528 | 「そういう意味。そうして再び走れるのなら、\n自分の\x%lタブレット;#00ffc040;タブレット%l;#;を[イニシャライズ,2]初期化しても構わない」 | 「是的。如果能夠再一次奔跑，就算將我的\x%lタブレット;#00ffc040;操作板%l;#;初始化也沒關係」 | 「Ý tôi là vậy đấy. Nếu làm vậy mà có thể chạy lại được, thì có [khởi tạo,2]khởi tạo lại \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# của tôi cũng không sao.」 | 「Ý tôi là vậy đấy. Nếu làm vậy mà có thể chạy lại được, thì có khởi tạo lại \x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# của tôi cũng không sao.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| ポーレット11_記憶と記録 | 1714 | 「それは……本当にそうなんですよね。\n[ハチロク,3]8620だけを中心にした観光振興ならいざしらず――」 | 「這……的確是這樣呢。如果旅遊業復興是單獨圍繞[八六,3]８６２０展開的，那倒還好——」 | 「Điều đó……đúng là vậy nhỉ.\nNếu chỉ lấy [Hachiroku,3]8620 làm trung tâm để chấn hưng du lịch thì không nói làm gì――」 | 「Điều đó……đúng là vậy nhỉ.\nNếu chỉ lấy 8620 làm trung tâm để chấn hưng du lịch thì không nói làm gì――」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| 仲国05_真夜中の餐車 | 1605 | 「……ですね。[このからだ,2]整備体でもわかりますから、\n決して小さくはない勾配です」 | 「……的確。即便是[這副身體,2]整備體我也能確定，而且這明顯不是個緩坡」 | 「……Đúng vậy. Ngay cả với [cơ thể này] thân bảo trì cũng có thể nhận ra,\nchắc chắn độ dốc không hề nhỏ.」 | 「……Đúng vậy. Ngay cả với thân bảo trì cũng có thể nhận ra,\nchắc chắn độ dốc không hề nhỏ.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| 共通02_日々姫と真闇と人形と | 1895 | 「ああ、いや。変わったな。\n[ひびき,2]日々姫は確かに、大きく変わった」 | 「不，不是說你啊。日日姬，你當然變了。確實是，大有不同啦」 | 「À, không. Có thay đổi chứ.\n[ひびき,2]Hibiki chắc chắn đã thay đổi rất nhiều.」 | 「À, không. Có thay đổi chứ.\nHibiki chắc chắn đã thay đổi rất nhiều.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| 凪ふかみ02_命の重さ | 1448 | 「わたくしの方は大丈夫です。\n[この子,3]8620にも、幸いにして異状はございませんでしたので」 | 「我不要緊。[這孩子,3]８６２０幸好也沒什麼異常」 | 「Phía tôi không sao ạ.\nMay mắn là [đứa trẻ này,3]8620 cũng không có dấu hiệu bất thường nào.」 | 「Phía tôi không sao ạ.\nMay mắn là 8620 cũng không có dấu hiệu bất thường nào.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| 凪ふかみ08c_新しい家族 | 2413 | 「当たり前です！\n[わ  た  し  た  ち  の  な  か,7]初恋の人のお願いじゃないですか」 | 「當然了！[我   們   可   是   朋   友   啊,13]畢竟是初戀情人拜託自己的事情」 | 「Tất nhiên rồi!\nĐó là lời thỉnh cầu của [trong số chúng ta,7]tình đầu mà.」 | 「Tất nhiên rồi!\nĐó là lời thỉnh cầu của tình đầu mà.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| 日々姫05_御一夜ステーションカフェ | 2143 | 「まぁ、[あのこ,3]8620の写真も」 | 「嗯，也有[那孩子,3]８６２０的照片」 | 「Chà, có cả ảnh của [đứa bé đó,3]8620 nữa.」 | 「Chà, có cả ảnh của 8620 nữa.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| 日々姫06_みくろ、来訪 | 2249 | 「だから、[うちのこ,4]38696を整備できないこと、みんな気にしてて。\nそれがみくろ、かえって申し訳なくて」 | 「所以，對於[我家的孩子,4]３８６９６無法維護的事，大家都很擔心。這反倒讓美玖路很過意不去」 | 「Vì vậy, mọi người đều rất bận tâm chuyện không thể bảo dưỡng cho [đứa bé nhà Mikuro,4]38696.\nĐiều đó lại càng khiến Mikuro cảm thấy áy náy hơn.」 | 「Vì vậy, mọi người đều rất bận tâm chuyện không thể bảo dưỡng cho 38696.\nĐiều đó lại càng khiến Mikuro cảm thấy áy náy hơn.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| 日々姫06_みくろ、来訪 | 2421 | 「みくろ、[うちのこ,4]38696と一緒に、\n動物園に引き取ってもらえてよかったって思ってます」 | 「美玖路在想啊，能和[我家的孩子,4]３８６９６一起被動物園收留真是太好了」 | 「Mikuro nghĩ, được sở thú nhận nuôi\ncùng với [đứa bé nhà Mikuro,4]38696 thật là tốt quá.」 | 「Mikuro nghĩ, được sở thú nhận nuôi\ncùng với 38696 thật là tốt quá.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| 日々姫08_開きかけのつぼみ | 2254 | 「いいってことです。\n[わたしたちのなか,3]幼なじみじゃないですか」 | 「沒什麼。我們可是[好朋友,3]青梅竹馬啊」 | 「Không có gì đâu ạ.\nChúng ta là [bạn thanh mai trúc mã,3]bạn từ thuở nhỏ mà.」 | 「Không có gì đâu ạ.\nChúng ta là bạn từ thuở nhỏ mà.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |
| 日々姫09_run_with_our_dreams | 1825 | 「人間の前、なので[じんぜんしき,2]人前式。神様に誓う結婚式は、\n[しんぜんしき,2]神前式、とよばれるようですね」 | 「在人面前宣誓就叫人前式。在神面前宣誓的好像叫神前式」 | 「Vì thề trước mặt con người, nên gọi là lễ cưới [nhân tiền,2]trước mặt mọi người. Lễ cưới thề trước thần linh,\ncó vẻ được gọi là lễ cưới [thần tiền,2]trước mặt thần linh ạ.」 | 「Vì thề trước mặt con người, nên gọi là lễ cưới trước mặt mọi người. Lễ cưới thề trước thần linh,\ncó vẻ được gọi là lễ cưới trước mặt thần linh ạ.」 | Bỏ markup ruby [x,n] rò rỉ vào dòng VN (engine render [x,n] thành furigana; dòng VN không được chứa markup JP). |

## 3.17. Grand 11 2485 — khôi phục 御一夜 (の) (1 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| グランドリライト11_ナインスターズ！ | 2485 | 「御一夜の……御一夜鉄道を支えてくれたみんなは。\n嬉しかとよね。こん晴れの舞台での、そん並び」 | 「御一夜的……支撐著御一夜鐵路的各位，要是能並肩站在這盛大的舞台上的話，肯定都老高興了吧」 | 「Mọi người... những người đã ủng hộ Đường sắt Ohitoyo.\nChắc hẳn sẽ rất vui nhỉ. Khi thấy đội hình đó trên sân khấu rực rỡ này.」 | 「Mọi người của Ohitoyo... những người đã ủng hộ Đường sắt Ohitoyo.\nChắc hẳn sẽ rất vui nhỉ. Khi thấy đội hình đó trên sân khấu rực rỡ này.」 | Khôi phục 御一夜 (の) đầu dòng bị U1c bỏ mất → "của Ohitoyo". |

## 3.18. P03 1728 — gloss 閉塞 → "Đóng đường" (1 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| ポーレット03_廃炭鉱 | 1728 | 「わたくしたちが乗っている以上、\x%l8620;#00ffc040;8620%l;#;は走行しない。\nこの全線が、\x%lキハ07;#00ffc040;キハ07%l;#;の\x%l閉塞;#00ffc040;[へいそく,1]閉塞%l;#;・専有区間となるのですから」 | 「只要我們都在這裡，\x%l8620;#00ffc040;８６２０%l;#;就不會開動。整個路段就是只屬於\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;的\x%l閉塞;#00ffc040;閉塞%l;#;專有路段」 | 「Chừng nào chúng tôi còn ở trên này, \x%l8620;#00ffc040;8620%l;#; sẽ không chạy.\nToàn bộ tuyến này sẽ trở thành khu vực \x%l閉塞;#00ffc040;phong tỏa%l;#; độc quyền của \x%lキハ07;#00ffc040;KiHa 07%l;#;.」 | 「Chừng nào chúng tôi còn ở trên này, \x%l8620;#00ffc040;8620%l;#; sẽ không chạy.\nToàn bộ tuyến này sẽ trở thành khu vực \x%l閉塞;#00ffc040;Đóng đường%l;#; độc quyền của \x%lキハ07;#00ffc040;KiHa 07%l;#;.」 | Gloss 閉塞 "phong tỏa" → "Đóng đường" (quyết T24). |

## 3.19. F-T56-1 — 仲国08 2823 → "Trung Quốc" (1 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| 仲国08_謝謝再見！ | 2823 | （僕も、日々姫も、ハチロクさえも。誰ひとり――\n日仲のレールを繋ぐなど、夢見てさえもいなかった） | （我也好，日日姬也好，八六也罷，恐怕我們都做夢也無法想像，自己能夠參與到連接日仲兩國軌道的事業中） | (Cả tôi, Hibiki, hay thậm chí là Hachiroku. Không một ai——\ntừng mơ đến việc kết nối tuyến đường ray giữa Hinomoto và Trọng Quốc.) | (Cả tôi, Hibiki, hay thậm chí là Hachiroku. Không một ai——\ntừng mơ đến việc kết nối tuyến đường ray giữa Hinomoto và Trung Quốc.) | 仲国 → "Trung Quốc" (quyết T56); 日仲 = 日ノ本 + 仲国. |

## 3.20. P07 2311 — gloss 列車 → "đoàn tàu" (1 dòng)

| File | Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|---|
| ポーレット07_支線 | 2311 | 戻りの\x%l列車;#00ffc040;列車%l;#;を御一夜にまで運んだあとで、\n\x%l8620;#00ffc040;8620%l;#;は転車し、術仙洞廃駅で待っててくれる。 | 回程的\x%l列車;#00ffc040;列車%l;#;會在御一夜放下客人，然後\x%l8620;#00ffc040;８６２０%l;#;進行轉車，前往術仙煤礦廢車站等我們。 | Sau khi đưa \x%l列車;#00ffc040;chuyến tàu%l;#; chiều về đến Ohitoyo,\n\x%l8620;#00ffc040;8620%l;#; sẽ quay đầu và đợi chúng tôi ở ga bỏ hoang Jutsusen. | Sau khi đưa \x%l列車;#00ffc040;đoàn tàu%l;#; chiều về đến Ohitoyo,\n\x%l8620;#00ffc040;8620%l;#; sẽ quay đầu và đợi chúng tôi ở ga bỏ hoang Jutsusen. | Gloss 列車 "chuyến tàu" → "đoàn tàu" (G1 đã khóa). |

## 4. Đã kiểm chứng, giữ nguyên (không sửa)

- **M20:** ハチロクh3 1801 （ぐりゅっ！ ぐりゅっ！ ぎゅっ！ ぶりゅん！）→ "（Ngoáy! Ngoáy! Siết! Phập!）" — "Phụt" sẽ đụng SFX xuất tinh trong file.
- **M21:** ハチロクh3 1810 （ちゅぷっ――にゅるっ――にゅっ――こしゅっ――）→ "（Chụt——trượt——ngoáy——sột sột——）" — "trượt" là động từ VN trong chuỗi （ ） miêu tả, không phải token romaji; F5 chỉ áp dụng cho token romaji SFX.
- **M23:** あー: 日々姫06 2021 あー → "A——" (thở dài cuối câu) và 2026 あー！ → "Aaa!" (thán) — cả 2 đều đúng theo sắc thái, không phải moan H-scene; 3 dòng あー toàn dự án có số a ≠ 2 đều đúng hoặc chấp nhận được (ん bỏ trong "aaah" nói thường, giữ "n" trong moan). Trích dẫn れいなh3 2529 không tồn tại.
- **M25:** 日々姫02_文庫森 1629 「ひえ！？…」→ "Hí!? A——ưm, …" — "Hí" hợp với thán giật mình bối rối; "Hử" hợp với tiếng ừ hỏi, không phải ひえ. Quét toàn dự án: hầu hết ひえ đã là romaji "Hie!?"/"Hieee!"; 2 "Hí!!?" (lr_ふかみh1 1234, 共通13 2040); 3 "Hả" non-H.
- **M26:** lrれいな追加h_夜の花嫁修業 1163 「ん、ひょっ」 TW 「嗯，嘿咻」 (tiếng rặn gắng sức) → "Ưm, hự." — "hự" hợp TW 嘿咻; "Hyawa" thuộc về ひゃわっ, token khác. ハチロク02_8620運転台通信 1849 「ひゃわっ！？…」→ "Hyawa!? Hả? A——vâng, …" giữ.
- **M29:** ぐっ diễn theo vị trí: đối thoại H-scene → romaji "Gu" (ハチロクh7_レトロモダンメイクラヴ 745); （ ） miêu tả → hệ VN của file ("Gừ"/"hự" — 稀咲h2_プライベートルーム 1961, 凪ふかみh1 2033/2041). Không thống nhất toàn dự án.
- **M32:** lr_ニイロクh_誓い。約束 1356 「んきゅっ！ んうっ！ ふ、ゅっ──みゅっ──…」→ "Nkyu! Ưm! Fu, yu──Myu──…" — moan pass đã quyết romaji; dòng duy nhất có ふ、ゅっ toàn dự án.
- **M33:** "kư" chỉ có ở lr_稀咲h1 (1190, 1260, 972, 974) — F1 đã quyết GIỮ "kư" cho file này. ハチロクh4 1020/1096/1121 "kư fưn"/"kư ha a"/"kư hi i i i ưm" là cụm くふ/くは/くひ, không phải くっ trần — giữ theo quy ước file. Trích dẫn lr_ハチロクh2 1837 sai file (dòng đó là narration, không có くっ).
- **M34:** lr_稀咲h1_おしおきとごほうび 1720 （ぎゅりっ――ぃぃぃぃぃぃぃぃぃぃぃぃっ！！！）→ "（Véo――iiiiiiiiiiiii!!!）" — hệ của file: động từ VN "Véo" + kéo dài nguyên âm romaji (13 i = 13 ぃ, đếm đúng); cả file dùng "Véo" cho các cú siết dài ぎゅ/ぎう (1712–1728). Đổi sang romaji thuần sẽ phá hệ siết của file.
- **M35:** 真闇h1_長期熟成 1014 「ひゃっ！？ あ……んっ――」 (giữa nụ hôn) → "Hya!? A……ưm――" — giữ. ふかみh1 1014 là dòng khác (không có ひゃっ; trích dẫn sai).
- **M36:** 真闇h1 1089 「んぶっ！？ んっ――ごくっ――ぷえっ――あっ――…ごくんっ――ごくっ」→ "Nbu!? Ưm――ực――Pue――a――…ực――ực――ực." — giữ "ực". ふかみh1 1089 không tồn tại ở file đó.
- **M38:** lr_ニイロクh 1297 「はっ──あっ──ふうっ、ん──…」→ "Hà──a──phùu, ưm──…" — giữ "phùu" (2u, đếm đúng cho ふうっ). ふう là token thở/dài, KHÔNG phải token moan fa/fu (quyết U11a trên 凪ふかみh2 1271); "phù" là cách diễn VN đã khóa cho ふう toàn dự án. 真闇h2_無濾過 1005 「…んっ――ふうっ」→ "…ưm――phuu." giữ.
- **M39:** lr_ニイロクh 2051 （ぐちゅっ──くいっ──ぐりゅっ──ずぢゅっ）→ "（Nhóp nhép──giật──rột──phập）" — giữ "giật" (くいっ = giật mạnh; "Kéo" là kéo đều, đã quyết cho ngữ cảnh khác ở 真闇02 2793).
- **M40:** そうてつさま ở lr_ハチロクh1 là hệ nhất quán, không phải mâu thuẫn: hiragana lắp bắp そうてつさま (có 、/――/そ、) → romaji ("Sou, tetsu, sama", "S-Soutetsu-sama." ở 1416); trôi chảy/kanji → "Ngài Soutetsu" (1192, 1262, 1419/1420/1421). 日々姫h5 không có dòng そうてつさま nào (cờ audit ở đó vô hiệu).
- **M41:** 凪ふかみh2_みずあそび 1276 「ふきゅっ！ それ、しゅごっ――…」→ "Fukyu! Cái đó, tuyệt quá——…" — giữ. Tiền lệ: 3 file giữ "Fukyu".
- **M42:** lr稀咲追加h_お風呂は日ノ本式に限るね 1091 「ふああんっ！？」→ "Fuaan!?" — giữ (fa dài giữ romaji; ふああん = f-u-a-a-n → "Fuaan", 2a đúng). Trích dẫn lr_ハチロクh3 1064/1170 không tồn tại.
- **M43:** lrれいな追加h_夜の花嫁修業 1064 「ふおっ！！？」→ "Fuo!!?" và 1170 「ふひゅんんんんっ！！！！」→ "Fuhyunnnn!!!!" — giữ cả 2 (dạng moan-pass, đếm đúng).
- **M44:** lr_れいなh1_レディ・れいな 1240 「あっ――あっ！ ――ひっ、あっ――ふか、いっ――\nおくっ――もうちょっと――もうちょっとで――んっ！」→ "A——a! ——Hí, a——sâu, quá——\nbên trong——một chút nữa——một chút nữa thôi——ưm!" — giữ "sâu, quá" (TW 好、深 ủng hộ cách đọc nhấn mạnh/tích cực; "quá" là cường điệu tự nhiên của VN; いっ là mảnh của いい, độ tin cậy thấp — đã ghi chú).
- **M45:** lr_れいなh1 1225 「くっ！！！」 đã là "Ku!!!" (U12a M7, đã gộp).
- **M46:** 凪h1_ふたりっきりのデート 1118 「ん……ちゅっ――…れるっ――…ぷあっ」→ "Ưm……Chụt——…Rộp——…Pua" — đã giải quyết bởi T77 (coordinator): れるっ → "rộp", KHÔNG phải "Chụt".
- **M48:** れいなh1 1420 「い"っ！？」 TW 「好痛！？」→ "Í!?" — giữ; moan pass đã quyết cách diễn; mục này nói về dị thường dữ liệu, không phải lỗi sửa.
- **M49:** れいなh1 1282 「はふぇふぇっ？\nはんは、ほおほおひへはふひょほ？」→ "Hafefe?\nHanha, hoohoohihehafuhyoho?" và 1341 「ぷっ――んっ――ほーへふはんほ――…」→ "Pụt――ưm――hoohefuhanho――hanrafa――sụt――ưm――pufu――he――sụt." — baby-talk bịt miệng đã diễn bằng romaji.
- **M50:** lrれいな追加h_夜の花嫁修業 1011 「い、いや――気持ちいい、と――いう、かっ」→ "Kh, không——sướng, thì——đúng, nhưng" — giữ "Kh," (diễn khởi âm glottal lắp bắp của い; M6 khóa các dòng "Kh"). Trích dẫn 1164 không tồn tại ở れいなh1/lr_れいなh1.
- **M52:** lr_れいなh1 1253 「あああああっ！」 TW 「啊啊啊啊啊！」→ "A a a a a!" — giữ; nhất quán với quy ước "A" cách của chính file (1131 「ああああああ」→"A a a a a a"); "Aaaaa!" sẽ phá nhất quán file.
- **M53:** しゅごっ = すごい nói ngọng (tuyệt vời) — "tuyệt quá" đúng: lr_れいなh1 1171/1185, れいなh4 1986. Trích dẫn れいなh1 1244 sai (dòng đó là đối thoại thường, không có しゅごっ).
- **M54:** 7 dòng đã xác định file qua ROUTE-MOANS.md — giữ hết: れいなh4 2021 「んひゃんっっっ！！！」→"Nhyan!!!" (2n + っっっ→"!!!"); ハチロクh2 1020 「じゅにゅるるるるるるるるっ！！」→"Junyururururururururu!!" (romaji giữ chuỗi る×8 + khởi にゅ); ハチロクh2 976/1011 「ああっ」→"a a!"/"A a——" (theo tiền lệ spaced-a kisaki-h3); 日々姫h1 1040 「んーーーーーっ」→"Ưm—————"; 凪ふかみh2 1299 baby-talk 「ひゃふぁ……んにゅ……にゃに、ひゃん――…」 giữ "ưm" cho âm ん bịt miệng; lr_ふかみh2 1770 （まるで――卵を温める母鳥の羽――っ！！？） giữ bỏ っ (dấu cắt cuối câu, đã diễn bằng "——!!?"; thêm "Ư" sẽ chèn âm không có trong JP).
- **M55:** KHÔNG TÁI HIỆN: không có あんひゃ / あん、ひゃ / あん――ひゃ ở đâu toàn dự án; trích dẫn lr_ハチロクh3 1063 là んふう…→"Nfuuuu…". Cờ cho coordinator.
- **M56:** KHÔNG TÁI HIỆN: không có dòng 15a+2u ở ハチロクh3; không tìm thấy mẫu JP nào có số a ≥15 + số u = 2. Cờ cho coordinator.
- **M57:** 真闇h1 1080 「ん……双ちゃん――あっ――太っ――――んふっ」→ "Ưm……Sou-chan――a――to quá――――Nfu." — đã giải quyết bởi F1/U12a M15.
- **M59:** 日々姫h3_汚れてしまった制服で 1010 「やっ――あっ――私の――おもらし――パン、つ――\nにぃにが、ベロで――ちゅう、って――んううっ！！！」→ "Ya――a――…Nuu!!!" — moan pass đã áp dụng phán đoán.
- **M60:** 日々姫h3 1136 「ふっふーん」 TW 「嘿嘿」 (cười khúc khích) → "Hừ hừm." — tiếng hừ tự mãn, không phải moan; cách diễn VN tự nhiên; romaji "Fuffuun" không có cơ sở.
- **M64:** ふかみh1_ともはり練習 990 「うぉっ！？」→ "Uoa!?" — cách diễn đã khóa cho うぉっ; đa dạng theo file/nhân vật (ハチロク01 1759 "Oa.", ポーレットh3 929 "Uo!?", ポーレットh6 793 "Uây!", 共通10 2371 "Uầy!?", 凪ふかみ08c 2017 "Uoa!?") là ngẫu hứng theo tính cách (quy tắc Hieu 19/11 22:05), không phải lỗi cần thống nhất.
- **M65:** ふかみh1 1553 （れるっ！ れろっ――じゅうううっ――はむっ！」 (ngoặc （...」 lệch) → "（Rộp! Liếm——chụt——ngoạm!）" — audit đã chuẩn hóa thành （...）.
- **M67:** 日々姫h4_いもうとタオル 1746 （ぷりゅんっ！）→ "（Puryun!）" — giữ.
- **M69:** 日々姫h4 1782 （ずんっっっっっ！！！）→"（Thúc mạnh!!!）" và 1794 （ずっっっっっ――――ごりゅううううっつ！！！）→"（Thúc mạnh――――Nghiến chặtttt!!!）" — っ×5 diễn mức nhấn bằng "Thúc mạnh" (đẩy mạnh), khác với っ đơn "Phập" (1743 ずんっ→"Phập"); phân biệt nhất quán trong file.
- **M71:** 真闇h2_無濾過 1861 （ぱくっ！）→ "（Phập!）" — giữ theo ngữ cảnh (ngậm/đóng sập; "Ngoạm" ở h3 là cắn, ngữ cảnh khác).
- **M72:** 日々姫h2: hệ spurt "Phụt"/"Bắn ra!" xen kẽ để đa dạng nhịp trong chuỗi spurt (1666: Phụt/Bắn ra/Phụt/Phụtt; 1667: Phụt/Phụt/Bắn ra/Phụt; 1668: Phụtt/Phụt/Bắn ra/Phụt — không có mẫu theo họ token; xen kẽ là thiết bị đa dạng có chủ ý). Áp một dạng sẽ làm phẳng. Chỉ token lỗi dạng 1665 được sửa (M61).
- **G12:** Gloss %l do VN thêm: GIỮ hết. ニイロク01 1609/1911 (gloss "Toa xe thử nghiệm Mohashi 21"/"Toa xe hỗn hợp" đúng, TW cũng thêm tag); ポーレット04 1780/1811/2050/2698/2816 + ヒヤリング 2076 (gloss giải thích thật: 接続 "kết nối chuyển tàu", 車販 "nhân viên bán hàng"/"bán hàng trên tàu", 車掌 "trưởng tàu", タブレット đã sửa bởi U5 thành "Thẻ bảng (Tablet)"); ハチロク06 1556/1710/1784 (audit ĐÃ gỡ tag — không còn gì làm). U5-4 (7 dòng P04: 1780/1811/2028/2050/2076/2698/2816): kiểm lại, giữ hết — 2028 JP có ruby [ぜろいちよん,2]014, CUR bỏ đúng ("Oha014."); 2642 (audit-review đọc sai, không phải dòng G12): タブレット→"Thẻ bảng" ✓, ブレスレット giữ "Bracelet" + gloss "(Vòng tay)" ✓ (nhân vật không đọc được từ ngoại).
- **G16:** 日々姫05_御一夜ステーションカフェ 1909 (trích dẫn ハチロク14_冬 1909 sai file): JP 「…下の下の下の下。[ゲゲゲ,2]下下下の[ゲ]下だわ」 TW 「不合格哦…差評差評差評。ＸＸＸ的差評啊」→ "…tệ của tệ của tệ của tệ. [Gegege,2]Tệ tệ tệ của [Ge]tệ đấy." — tag là audit KHÔI PHỤC có chủ ý để giữ trò đùa 下→ゲ (nơi duy nhất ruby tự nó mang trò đùa); engine render [x,n] thành ruby trên n ký tự sau, nên "Gegege" nằm trên "Tệ " đúng như ゲゲゲ nằm trên 下下 trong JP. Giữ nguyên.
- **M3-boundary:** ふかみh1_ともはり練習 995 「えっ！？ あっ！ 双鉄さん、今こっちに来ちゃっ――\nきゃっ！？ わあああああっ！？」 TW 「哎！？啊！雙鐵先生…呀！？哇！？」→ "Hả!? A! Anh Soutetsu, khoan hẵng qua đây——\nÁ!? Oa a a a a a a a!?" — giữ. Ranh giới: M3 chỉ bao moan trong H-scene; tiếng thét giật mình (きゃっ là tiếng thét ngạc nhiên, nhất là ngạc nhiên phi tình dục) giữ "Á". Mở rộng M3 sang scream sẽ kéo theo 175 dòng scream non-H — KHÔNG làm. Tiền lệ scream toàn dự án (共通05 2262, 共通07 1754/1755, theo cờ U11b).
- **M15-keep:** lr_稀咲ポーレットh1 1542 んふ、ふっ (JP có 、 tách) → giữ "ưm fu, fu"; れいなh3 1061 んっうっ → giữ "ưm u" (đọc 2 token chấp nhận được).
- **M24-keep:** 真闇h2 1027/1029/1031 (んふふ→"Nfufu") đã đúng — giữ. 日々姫h4 1052 「んふふっ――れろおおおっ」→ "Nfufu――Reroooo" đã đúng — giữ (không phải dòng M24).
- **HAS-RUN-keep:** v2 tái kiểm: 28 KEEP. 4 mục v2-FIX bị ghi đè thành KEEP sau khi đọc tay: 1716 (token "Nụtọooo" tự nó đã đủ 4 o = target; "rộp" là token riêng nối bằng —), 2536 (scan ghép sai token; token đầu じゅぶううううううううううっ có 10 う, không phải 9 — tổng 12 u = VN "Ju buuuuuuuuuuu!" 12 u ✓; ごちゅうううっ → "Go chuuuu!" 5 nguyên âm ✓), 2546 (dạng cách "Byuu u!" = 3 u ✓), 1708 (token kiểu romaji đa âm tiết; tổng đúng = gốc 9 + marks 7 = 16 = CUR ✓). Các dòng đã được đợt gộp trước sửa đúng sau snapshot của scan (2060 "Reroooooo" 7 nguyên âm, 1715 "Rộộộộộộộp" 7, 1668 "Phụtt!" 2t, 1873 "Rộộộộộộp!" 6, 1772 "Reroooo!" 5) và các KEEP romaji/VN khác (1959/1992/1687/1703/1707/1709/1819/1857/1828/1829/1832/1088/1823/1834, 1651 "Chúuuuuuuuuuut!" 11u, 3820, 1252 ×3, 1379 ×4).

## 5. Cờ cho coordinator

- M18 — KHÔNG mở rộng "append Kuuun": ~25 dòng Paulette gọi "Soutetsu-kuuun" (tên + くぅん) giữ nguyên cách bỏ whine — whine là kéo dài của kính ngữ くん, không có đối ứng VN; gắn "Kuuun" sau "anh Soutetsu" sẽ trộn 2 hệ trong 1 hơi thở. Cần quyết dự án nếu muốn mở rộng.
- M55/M56 — KHÔNG TÁI HIỆN (đã chạy tìm kiếm toàn dự án, xem §4). Cần diễn đạt lại chính xác trước khi xử lý lại.
- M7 — 7 dòng （ ） miêu tả có "Hự" (lr_ふかみh1 1959, lr_ポーレットh2 1774 — false positive: "khựng" chứa "hự" — lr_凪h1 1787, lr_凪h2 1821, ハチロクh3 1787, ポーレットh5 1733 — くっ đã là "Ku", "Hự" diễn ぐッ — 日々姫h3 1840): F1 nói （ ） くっ → "Ư" nhưng U12a cố ý để nguyên （ ）; cần quyết coordinator. 15 dòng đối thoại non-H "hự" (lr_凪h1 1641, lr_日々姫ふかみh1 1967, ハチロク01 2093, ハチロク10 2821, ポーレット07 1191, ポーレット12 1487, ポーレットh4 1464, 凪ふかみ08b 2063/2570, 日々姫01 3012, 日々姫04 1912, ポーレット14 1513, 凪ふかみ06 1741, 凪ふかみ07 2052, ハチロク14 1620): KHÔNG đổi (phạm vi U12a M7 chỉ file H; "non-H giữ Ư" của F1 còn mơ hồ). lr_ふかみh1 1365 "nhự" (JP 「…\nくっ、は――…」→ "…nhự, ha——…") — "nhự" KHÔNG phải "Hự"; cần quyết ("Ku, ha" theo M7, hay giữ "nhự"?).
- F5 sweep rộng hơn thuộc về U15b; các token romaji thường còn sót trong dòng đợt này đã thấy: lr_日々姫h2 1035 "rerooo", 真闇h1 1056 "fu" cuối dòng, ふかみh2 1033 "pu", 稀咲h1 1306 "kuha", lr_凪h1 1165 "kuha", lr_稀咲ポーレットh1 1677 "ku".
- ふかみh2 1000 "chụt u u" cho ちゅうう (họ chū) — ngoài phạm vi M15, ghi nhận là dị thường.
- T75/T77/T78 appendix misses và mục tên địa danh 帝央 ("Teio" đa số ~15 dòng vs "Teiou" 共通06 2112, ニイロク03 1570 vs "Trung tâm Hoàng gia" 仲国05 2032) — KHÔNG thuộc batch này (cờ từ U13b); chỉ ghi nhận.
- HAS-RUN quan sát ngoài phạm vi (không sửa): token 1-う diễn 2–4 t không nhất quán (3502 token4 びゅうっ→"Phụttt!", 2133 token2 ぶびゅうっ→"Phụtttt!", 2048 token3 びゅるっ→"Phụtttt!!!", 1558 token4 どびゅっっ→"Phụtttt!", 2366 token1 びゅううっ→"Phụt!" 1t); stretch LOST scan không cờ (2417 token1 ずりゅううううううううっ→"Trơn", 2388 token2 なでええええええええっっ→"Xoa xoa", 3770 token1 ずりゅううっ→"sâuuuuu" 5u vs target 4).
- Trùng lặp có thể với U15b/U16 (coordinator GHÉP khi gộp): lr_ポーレットh1 1003 (M7+M15 đã GHÉP trong đợt này), lr追加_みくろ 1840 (M15+M24 đã GHÉP trong đợt này) — nếu batch khác cũng chạm 2 dòng này thì GHÉP theo thứ tự gộp.
- Cờ U14c/U14b/U14a KHÔNG thuộc batch này (chỉ ghi nhận): O52 (れいな01 2415 JP cell hỏng, chứa text VN; TW là dòng khác — kiểm comment `# JP:` của TOML-2 trước khi sửa); O46/O48 KHÔNG TÁI HIỆN (không có mẫu "N" ở ハチロク15a; key 2054 không tồn tại) — cần diễn đạt lại chính xác; U14b F-O25-1 (lr_凪ふかみh1 1616/1687/1737 cùng lỗi P9 như O25 nhưng chưa đặt tên); U14a (Soutetsu→Olivy "cô" trong ngữ cảnh công việc, ハチロク14 2427/2986).
- M24 — 日々姫h4 1052 đã đúng ("Nfufu") — không phải dòng M24 (ghi chú để khỏi đếm trùng).

## 6. Lượt soát 2 (bắt buộc — đọc lại toàn bộ fix theo JP)

**Tổng: 418 dòng / tái kiểm chứng 418 / loại 0 / sửa 55.**

Quy trình soát 2 gồm 3 lớp, chạy SAU khi viết tay toàn bộ fix:

1. **Phân tích lại bằng máy (HAS-RUN):** chạy lại logic `analyze()` của scan trên (JP CSV3, fix của đợt này) cho 99 dòng HAS-RUN — 98 token được kiểm, ban đầu còn 35 lệch. 34 lệch là lỗi đếm tay của chính người viết (quên chữ cái đầu của token đã tính trong tổng: "Phậ" = P + run, "Trượ" = T + run, "Chụ"/"Siết"/"Rú" = run thuần — xem §6.1); 1 lệch còn lại là artifact của trình kiểm (1860: scan gộp 2 token qua `\n` thành 1 target vô nghĩa 8; từng thành phần đã kiểm tay: "Trượtttt!" = 5 ✓, "Phậpp!" = 3 ✓, "Lún sâubuuuuuu!" = 7u ✓). Sau sửa: 0 lệch thật.
2. **Diff old_vn→fix cho toàn bộ 418 dòng** (đọc từng diff): phát hiện 21 lỗi nữa — 19 dòng M24 bị rớt dấu ngoặc kép `"…"` bao dòng (văn bản thật: có trong CSV3 VÀ trong giá trị TOML gốc, vd. lr真闇追加02 1215) và 2 dòng HAS-RUN bị rớt token cuối (2000 " Gotsu!!!", 1705 " Gochu!!"). Cả 21 đã sửa và kiểm lại bằng diff lần 2: 0 lần xóa `"` còn lại, 0 lần xóa "Gotsu"/"Gochu" còn lại; mọi diff còn lại chỉ chạm đúng token cần sửa (run chữ, "Ưm "→"N", viết hoa, bỏ markup [x,n], chèn/bỏ theo quyết định).
3. **Kiểm tra theo mục:** M15 — 0 dạng tách còn lại, số nguyên âm token dài đúng hết (15u/14u/12u/9u/8u/6u/5u/4u/3u/2u/1u + 17~ ở 732); M24 — 0 token cười thường còn lại (ngoại lệ có chủ ý duy nhất: ハチロク06 2322 "Ufu", JP うふっ = 2 mora); M7 — mọi fix chứa "Ku", "Hự" chỉ còn ở 2 dòng ぐっ đã biết (ふかみh1 1042, ポーレットh5 1733); G15 — 0 markup [x,n] còn lại trong fix.

### 6.1. Bài học đếm (ghi lại để đợt sau khỏi lặp)

Lỗi đếm tay phổ biến nhất đợt này: với token "Phậ"/"Trượ"/"Tuộ"/"Cộ", chữ cái ĐẦU (P/T/C) đã tính trong tổng — tổng = 1 + run; với token "Chụ"/"Siết"/"Rú"/"Phụ"/"Sụ"/"Mú", gốc KHÔNG chứa chữ run — tổng = run. Vd. target 5 cho "Phậ" = "Phậpppp" (P + 4p), không phải "Phậppppp". 34/35 lỗi lệch ban đầu là dạng này; đã sửa hết và kiểm lại bằng máy (mỗi token mới được đếm lại bằng script đếm chữ trước khi ghi).

## 7. Khối TOML (parse-verified, theo file — 402 key sau gộp; xem Phụ lục gộp)
# lr_ふかみh1_ふかみうさぎのたまご.txt.toml
[script]
"1257" = "「Ư――Ư, Ku——gần như, chắc chắn——\\nanh sẽ——bắn tinh, vào bên trong mất thôi.」"
"1259" = "「Ư! Ku!!」"
"1277" = "「Nhyun!!!」"
"1304" = "「Nkyuuu!!」"
"1305" = "「Nkyu!!!」"
"1307" = "「Ưm——Ku——a——.\\n……Mùi hương, đậm nhất, của anh——rốt cuộc, là mùi như thế nào.」"

# lr_ふかみh2_セックスの意味.txt.toml
[script]
"1126" = "「Nhyuuuuuuuuuuuuuuu!!」"
"1220" = "「Bảo dưỡng, cẩn thận——đã làm, xong chưa——\\nmuốn anh Soutetsu——kiểm tra, giúp em——Na!」"

# lr_ニイロクh_誓い。約束.txt.toml
[script]
"1354" = "「Na!!?」"
"2047" = "（Trượttttttttttt!!!!!!）"
"2048" = "（Phụt! Phụt! Phụtttt!!! Phụtt!）"

# lr_ハチロクh1_今ひとたびの契り.txt.toml
[script]
"2000" = "（Phậpppppppppp! Gotsu!!!）"

# lr_ハチロクh2_新しい服。新しい旅.txt.toml
[script]
"1496" = "「Nhyuuuuuuuu!!!!」"

# lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml
[script]
"1195" = "「Hyau! Hya! I! Ngài Soutetsu, hawa\\nA! Ngu! Hihe——đến đây——Nkyuu」"
"1197" = "「Hya! A! Ưm! Na!\\nA! A! A! Aaa!!!」"
"1199" = "「Hya! Ưm! Nkyu! Fua! Em, Suzu, ha! Suzu! Hết——」"
"1909" = "（Phậpppppppppp!! ——Cộc!）"
"1956" = "（Phậppp! Cộc!!!\\nPhậpp——ưm——phập——）"
"1961" = "（Phập! Phập! Ngoáyyy! Cộc!!）"
"1965" = "（Phậppppppppp!!!!!!）"
"1966" = "（Phậpppp!!!! ——Cộc! Ngoáy!）"

# lr_ポーレットh1_家族旅行の最終日の夜.txt.toml
[script]
"1003" = "「Hyau!? A――ưm! Ku――Fa! Na!!」"
"1088" = "「Ưm――Fufu――Anh Soutetsu cũng, phát ra……\\ntiếng――rên rỉ rồi, còn, gì――ưm」"
"1096" = "「Nkyu——Fa——a, thế này——thích quá—— ư ư——Phu——nè——cứ thế này——nữa đi」"
"1097" = "「Nkyu!!?」"
"1181" = "「Vâng, Ufufu. Vì là dầu gội trong phòng tắm của nhà trọ mà,\\nchắc chắn hôm nay anh Soutetsu, Hikari và cả Reina đều dùng chung một loại」"
"1184" = "「Đến, mức đó……ưm――hà――a――ưm―― Nfu――sướng……lắm……sao?――a」"

# lr_ポーレットh2_デコレーション＆ミルク.txt.toml
[script]
"1018" = "「Fufu——Fufufu! Ufufufufu!!!」"
"1024" = "「Fua! A! A! A! Khoan! Na!\\nKhoan đã——a——Na! Faaa!!!」"
"1075" = "「A——Ufufu」"
"1079" = "「A——a——a——ưm——nè? Anh Soutetsu——\\nanh Soutetsu——a——phu——ưm——Nu!」"
"1116" = "「Ưm——ưm bụp——bụp——Ku——ưm」"
"1124" = "「Nkyuu!! Ưm～～～～～～～～～～～Ư!!」"
"1125" = "「Nkyun!!!」"
"1127" = "「Nfu!!!」"
"1131" = "「Nuuu!」"
"1133" = "「Ưm bụp!? Bụp——Ku—— Khụ——uệ——ực——ưm mự」"
"1299" = "「Anh Soutetsu! Na!!!?」"

# lr_凪h1_痛いの痛いの飛んでけばい.txt.toml
[script]
"1158" = "「Nku! Fua――á――ưm――（Ngoạm!）\\nJuru――chụt! Juru! Juba!!」"
"1159" = "「Nku! Ưm――\\nGokyu! Ực! Ực! Ực!」"
"1162" = "「Nku!? Pu――Fa――ưm――Juru!\\nJubo! Jubu! Juba! Chụụụt」"
"1165" = "「A……Ku――kuha――rơi vào tình huống thế này――\\nchỉ số IQ sẽ dần dần――hòa tan vào tinh dịch mất」"
"1240" = "「Ưm! Nku! Ực! Ực!!!」"
"1305" = "「Sao lại, không chịu nổi——chứ? Ưm——Ku——a——\\nKhi cả ngực——và cô bé——bị làm, cùng lúc, thì sao?」"
"1802" = "（Chà! Nắn! Xoa! Épp!）"
"1825" = "（Vê! Đẩyyyyyyyyyy!!）"
"1827" = "（Trượttttttttttttt!）"

# lr_凪h2_虎さんの交尾.txt.toml
[script]
"1215" = "「Ưm——Ku! A!!」"
"1219" = "「Ku!」"
"1231" = "「Ku——ư——」"
"1313" = "「Ehehe! Vui quá——\\nPhùuu——phùu——phùuuu——phùuuuu——」"
"1339" = "「Cho cậu nhỏ đang cương cứng vào cửa âm đạo——Ư, Ku——\\nThế này——đã đúng, chưa?」"
"1373" = "「Không sao đâu——Ku——khi nào hỏng——thì——\\nanh cũng——sẽ hỏng cùng em——」"
"1391" = "「Sung sướng sao——Fufu, như thế này hả?」"
"1822" = "（Trượtttttttttt!!!）"
"1826" = "（Trượtttttttttttttttt!!）"

# lr_凪ふかみh1_じぇいけい！.txt.toml
[script]
"1395" = "「Không cần——phải đòi hỏi——tham lam, đến vậy, đâu——Ku!\\nĐợt tinh dịch——tiếp theo——sắp——trào ra, rồi——」"
"1446" = "「Có khi anh——đã làm Nagi——thụ tinh, rồi cũng nên——Ku!\\nBộ phận sinh dục——đẫm, tinh dịch——cứ thế, mà cắm vào」"
"1546" = "「Không hề, đột ngột, đâu——Fukami cũng từ lâu đã——\\nướt đẫm——Ku——nhớp nháp, thế này rồi, mà」"
"1559" = "「Ku——a!」"
"1611" = "「!!!! J, anh Soutetsu JK——\\nĐồng phục……váy……Ufufufufu」"
"2299" = "（Phụt! Phụtt——Trượttttttt!）"
"2316" = "（Bộp! Tuộtttttttttttt!!）"
"2317" = "（Trượtttttttttttttt!!!）"

# lr_日々姫h2_デザートは食事の前に.txt.toml
[script]
"697" = "「……A——Ku!」"
"948" = "「Ku——a——a! A!!!」"
"968" = "「Ưm——Ku.」"
"970" = "「Mà phải nói là——Ku——a——anh cũng, thế——」"
"980" = "「A…… Nfufu. Em biết rồi.\\nMùi ngon lành của anh hai ấy à? Chắc là~ từ đây!!」"
"1035" = "「Liếm——Fufu, vị phô mai hơi mặn mặn?\\nHơi kén người ăn đấy——nhưng thế này cũng——ưm~~ rerooo」"
"1051" = "「Ưm…… chụt——chụt——churu——liếm——\\nChụt——ưm——pua——Nfufu, cảm ơn vì bữa ăn.」"
"1070" = "「Vâng. Khá là nặng mùi đấy? Nhưng mà nhé? Là mùi của anh hai mà.\\n（Hítttttttttttttttttt）」"
"1159" = "「Nếu đang, đứng trước——nguy hiểm——đến tính, mạng——\\nKu——thì sinh vật——theo bản, năng——sẽ muốn để lại, hậu duệ——」"
"1665" = "（Phụt! Bắn ra! Phụt——Phụtt）"

# lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml
[script]
"1438" = "「A…… Ufufu――em――với anh hai――\\nđã hôn――anh hai rồi!」"
"1457" = "「A, Ufufu. Nó đang giật giật kìa.\\nAnh Soutetsu, sắp xuất tinh rồi sao?」"
"1459" = "「A, không cần dừng lại đâu. Tiếng vừa rồi, Ufufu,\\nlà tiếng kêu vì sướng quá nên giật mình đấy.」"
"2411" = "（Phụt! Phụt! Phụt! Phụtt!）"
"2416" = "（Phụt! Phụt!! Phụt! Phụttt!）"
"2436" = "（Tuốttttttttttttttt!）"

# lr_日々姫真闇h1_三人家族.txt.toml
[script]
"1445" = "「Hiat!? A――Ya! Thế này――\\nThế này――mạnh, quá――chị――không biết đâu.」"
"2366" = "（Phụt! Phụt! Phụt! Phụtt!）"
"2376" = "（Phụt! Phụt! Phụtt! Phụt!）"
"2388" = "（Vuốttttt――Xoa xoa）"
"2417" = "（Trơn tuộtt!!! Ngokyutsuuuu!）\\n（Vuốt――Chạm――Xoa――Vuốt）"
"2428" = "（Phập! Cộc!）"
"2440" = "（Phậpppppp!! Cộccc!!）"
"2441" = "（Phậpppppppppp!!! Goryu!）"

# lr_真闇h1_僕のおねえちゃん.txt.toml
[script]
"2121" = "（Rột! Phụt! Phụtt! Phụt!）"
"2145" = "（Phụttttttttt! Ục!）"

# lr_稀咲h1_おしおきとごほうび.txt.toml
[script]
"986" = "「Phù……Ufufu――Sou, tetsu――ưm……\\nCái bản mặt lôi thôi……như sắp tan chảy ra――kìa?」"
"1160" = "「Thế này thì――em……giống như đồ ngốc vậy, lại đi ghen tuông……\\nTrong khi――Ufufu――Soutetsu, lại say đắm em đến thế này.」"
"1705" = "（Phậppppppppp!!! Gochu!!）"

# lr_稀咲ポーレットh1_悪い大人の契約.txt.toml
[script]
"1546" = "「A——không sao——cái đó——Nfu——a!!!」"
"1617" = "「Ngu!!!!!」"
"1620" = "「Nku!」"
"1621" = "「Nku!!」"
"1622" = "「Nku!!!」"
"1677" = "「Tôi cũng——a——ku——Nfu——hiểu rồi.」"
"1712" = "「Ehm! Em cũng vậy, anh Soutetsu——Na!! A! Nên là——vào đi, vào đi, vào đi! Vào đi!!」"
"2500" = "（Kíuuuuuuuuuuuuuu!）"

# lrれいな追加02_花嫁修業の先生たち.txt.toml
[script]
"2017" = "Khoảnh khắc chị Mayami thì thầm điều gì đó,\\nReina bật cười khúc khích Ufufu."

# lr真闇追加01_新婚旅行のリクエスト.txt.toml
[script]
"1086" = "「Nfufu, nghe thú vị đấy. Vậy thì cô hướng dẫn viên ơi.\\nCó thể cho hết mấy cái vừa nói vào lịch trình được không?」"
"1144" = "「A——Ufufu. Đúng thế, chắc chắn rồi.\\nPau-chan, có vẻ bao bọc quá mức nhỉ」"
"1194" = "「Nfufu, cuối cùng, cũng sắp đến rồi nhỉ.\\nXin lỗi em nhé? Chị lại bắt em phải chờ đợi rồi」"

# lr真闇追加02_御一夜新婚旅行.txt.toml
[script]
"1215" = "\"「Ufufu, chẩn đoán tính cách qua cách xúc than của anh Soutetsu,\\ntrúng phóc luôn đó nha~」\""
"1217" = "「Nfufu. Thấy bé Reina vui vẻ,\\nchị cũng vui lắm」"
"1218" = "\"「Nfufu. Chị hiểu rồi. Rei-chan? Nào, cười lên.」\""
"1222" = "\"「Nfufu, do tính cách cả mà.」\""
"1223" = "\"「Nfufu, cảm ơn em.\\nNào? Hi-chan, Sou-chan. Cả Rei-chan nữa.」\""
"1224" = "\"「Nfufu, cảm ơn em nha, Rei-chan.」\""
"1280" = "\"「Nfufu, em đùa à.\\nLàm sao mà hai đứa nó nhận ra chị được chứ.」\""
"1283" = "\"「Nfufu, Rei-chan làm giỏi quá ta.」\""
"1285" = "\"「Nfufu, vậy thì Rei-chan sẽ cải trang thành gì nào?」\""
"1370" = "「Ufufu~, làm hướng dẫn viên,\\nđúng là một công việc cực kỳ thú vị nhỉ~」"
"1382" = "\"「Nfufu, cảm ơn em! Đó là lời khen tuyệt vời nhất đấy!!」\""
"1680" = "\"「! Ôi chà, Fufu, đúng là vậy nhỉ.」\""

# lr真闇追加03_ブルートレインの夜.txt.toml
[script]
"1125" = "\"「Nfufu, ra là vậy.」\""
"1127" = "\"「Nfufu, được đấy. Đúng kiểu con trai nhỉ.」\""
"1128" = "\"「Nfufu, có khi Rei-chan\\nđã nương theo chị cũng nên.」\""
"1130" = "\"「Nfufu, đã rõ.\\nNhờ em kỳ cho lưng chị thật sạch nhé?」\""
"1132" = "「Nfufu, đúng vậy. Sở thích của đứa trẻ đó không hề thay đổi.\\nKhuôn mặt vẫn là của thường ngày, chỉ là thêm chút xíu điệu đà thôi」"
"1182" = "「Nfufu, là tuần trăng mật mà lị」"
"1264" = "「Đúng. Toàn bộ căn phòng nhìn từ trên giường.\\nKhông chỉ thế đâu……Nfufu, cả khuôn mặt lúc ngủ của chị nữa」"

# lr真闇追加h_赤ちゃん、欲しか.txt.toml
[script]
"1132" = "\"「A, quả nhiên làm thế này thì sướng lắm nhỉ. Vậy thì——\\nNfufu, chị sẽ làm dai dẳng hơn nữa cho em nhé.」\""
"1181" = "\"「Nfufu, ngoan lắm, thực sự rất ngoan.\\nĐáng yêu quá, em bé đáng yêu của chị.」\""
"1183" = "\"「Nfufu, lần này thì ngoan ngoãn lắm.\\nSướng lắm đúng không. Ngoan lắm, ngoan lắm.」\""
"1187" = "\"「Vâng ạ. Nfufu. Vậy thì, xin mời.」\""
"1283" = "\"「Ngoan lắm, ngoan lắm. Vuốt vuốt, xoa xoa.\\nNfufu, giật giật rồi kìa, sướng lắm đúng không.」\""
"1803" = "（Phậppppppppppp——bập!）"
"1824" = "（Siếtttttttttttttttt!!!）"
"1828" = "（Bóppppppppppppppp）"
"1860" = "（Trượtttt! Xoáy! Phậpp!\\nLún sâubuuuuuu! Bập! Xoáy xoáy!）"
"1883" = "（Trượttttttttttttttttt）"

# lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml
[script]
"778" = "「——Ư——Ku——Để, mang thai——thì.」"
"780" = "「——Ư——Ku——A——O.」"
"1130" = "「Ku!」"
"1148" = "「Ưm…… Ku.」"

# lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml
[script]
"2323" = "「Ưm, Fufu? Vẻ thong dong——vừa nãy, đâu, rồi?,\\nBây giờ, cô——ưm——vừa lên đỉnh, nhẹ——đúng không?」"
"2347" = "「Hiyoko nhút nhát——Fufu——\\nLàm tốt lắm——(Chụt!)」"
"2350" = "「Hiyoko……Hiyoko……Fufu. Ta yêu cô.」"

# lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml
[script]
"1677" = "「Hyauuu! Tuyệt, quá── Nu!!!\\nBụng── vùng kín── bị đâm vào, bị khuấy đảo」"
"1690" = "「Nfufu.」"
"1691" = "「Nfufu, đáng yêu quá.」"
"1692" = "「Nfufu── dễ thương quá. Đẹp lắm.\\nLàm chị muốn làm cho em sướng hơn nữa.」"
"1702" = "「Nfufu── Sướng lắm đúng không? Cả anh hai và Mikuro.」"
"1777" = "「Hà…… a── anh hai── anh hai──\\nCứ thế, mãi── chỉ có âm vật── Na」"
"1786" = "「Hau! A! A! Aaa! Fua──Ư──ưm! Nuuuu!!!」"
"1801" = "「Ku! Ưm!!!」"
"1802" = "「Ku!!!!」"
"1840" = "「Ưm…… （Ực） Nfu──Fufu. Em hiểu chưa? Mikuro.\\nĐó chính là làm tình. Cách kết nối sâu sắc nhất giữa đàn ông và phụ nữ.」"
"1853" = "「Nfu──ưm……fu──uê──liếmmmmm」"
"1855" = "「Nhyuuuuuuuuu!」"
"1857" = "「Nkyu! Fua! A── trượt── tuột, ra── Aaaa── anh hai── vào hết, mất」"
"1858" = "「Nkyu!!!」"
"1859" = "「Nhyu!? Hau! Khi, chạm vào──\\nBị cọ xát── Mikuro── thích lắm──」"
"1861" = "「Ưm!? Ưm……phu──Nfufu──」"
"1865" = "「Nkyuu!!! Hyua! A! A!!\\nMạch điện── vừa nãy── Mikuro, trong chốc lát── như bị, cháy vậy」"
"1866" = "「Nkyuuuuuuuuuuuuuu!!!!!!!」"
"1868" = "「Vâng ạ! Vâng ạ! Mikuro, muốn anh cử động ạ──\\nNu!!!」"
"2313" = "「（Chụt──chụt!） Nfufu. Vậy sao.\\nLàm tình sướng hơơơn hẳn tự làm một mình nhỉ.」"
"2315" = "（Chụttttttttttttt!）"
"2317" = "（Chụtttttttttttttttttt!）"
"3051" = "（Siếttttttttt!!!!）"
"3053" = "（Phụt! Phụt! Phụtt! Phụt!）"
"3057" = "（Cọọọọọọ!! Trượt! Phập!）"
"3060" = "（Trượtttttttttt）"
"3102" = "（Xoètttttt）"
"3106" = "（Siếttt）"
"3107" = "（Phậpppppppp!!）"
"3111" = "（Phậpppppp! Trượt! Phập!）"
"3118" = "（Trượttttttttttttttttt）"
"3126" = "（Phậppppppppppp! Chát!）"
"3130" = "（Siết! Siếttttt!!! Siết chặt!）"

# ふかみh1_ともはり練習.txt.toml
[script]
"1042" = "「Nkyu——hi——lên——ưm ưm ưm~~ưm!\\nNku——ực——chụt——ực」"
"1055" = "「Nhyu! Sâu quá! Bên trong! Tử cung!\\nTử, cung——phập——ưm, đâm trúng, rồi!!」"
"1057" = "「Nkyuu!!」"

# ふかみh2_homesweethome.txt.toml
[script]
"977" = "「Hya!?\\nAnh Soutetsu, v, vừa rồi không sao chứ ạ!?——Ngu!?」"
"993" = "「Nkyun!」"
"994" = "「Ngu! Ưm——ưm——phù u u——ưm——\\nNgu——ưm——phù ư——ưm——ưm——phù ư」"
"999" = "「Nkyu——ưm——hự——Nfu——ưm! Ưm」"
"1000" = "「Phù gu——gu——Npu——ưm——phù——ưm\\nPhù ư——ưm——Ngyu——chụt——chụt u u!」"
"1004" = "「Mugu!!!?」"
"1033" = "「Ưm……pu……Npu——ưm——Nu——\\nƯm~~~——ưm! Ực——ực——ực」"
"1044" = "「Npu!!? Ưm! Phù u u u u u u u n!!!」"

# ふかみh3_夏休みの最後の日の、前の日.txt.toml
[script]
"2478" = "「Vâng, Ufufu. Em xin phép ạ」"

# れいなh1_おかあさんのレッスン.txt.toml
[script]
"1528" = "「Fua――a――\\nƯm――Ku――」"
"1534" = "「Ha……a——ưm——vào, rồi——\\nVào rồi——anh Soutetsu——」"
"2328" = "（Phụt――phụt――phụtt――phụt――）"
"2345" = "（Phậppppppp!——Bạch!）"
"2346" = "（Sụtttttttt!!!）"

# れいなh2_おもらし防止大作戦.txt.toml
[script]
"1053" = "「Nkyu——phù——a——Reina——Reina——\\nlỗ tiểu——bị chọc chọc, liếm liếm——rồi」"
"1734" = "（Phậppppp! Phập! Bạch!）"
"1737" = "（Phậpppp! Phập! Rột! Rột!）"
"1758" = "（Chụttttttttttt——chụt!）"
"1764" = "（Phậppppppp!!）"

# れいなh3_おもらし自由化大作戦.txt.toml
[script]
"1071" = "「Nkyu! Phù——ya——chỗ đó……Reina……chỗ đó……\\nbị đâm vào……a ưm!」"
"1073" = "「Nkyu! Fua——a——a!!」"
"1095" = "「Nkyuuu!」"
"1721" = "（Nhópppppp! Phậpppppp!!）"
"1738" = "（Rộtttttttttttttttttt!!!）"
"1740" = "（Àoooooooooooooo!）"
"1747" = "（Phậpppppp!!!!）"

# グランドリライト03_日々姫.txt.toml
[script]
"1470" = "「――『Bản tin Buồng lái 8620』」"
"1491" = "「『Bản tin Buồng lái 8620!』\\nTuyệt quá! Tuyệt lắm! Thật sự rất tuyệt luôn đó!」"
"2475" = "「Về 8620. Anh――\\nĐây là lần đầu tiên hai anh em mình cùng nhau ngắm nó nhỉ.」"

# グランドリライト06_稀咲.txt.toml
[script]
"1378" = "「Thời gian gặp được, sao——Ufufu, hay đấy.\\nNghe cậu nói vậy, em vui lắm.」"

# グランドリライト09_凪.txt.toml
[script]
"1489" = "「Dù vậy, em quyết tâm đến đây thật là tốt quá!\\nChắc chắn 38696 cũng đang cùng mọi người trong sở thú vui mừng cho em!」"
"1716" = "「Chị hai có thể đến, em vui lắm ạ!\\nĐó sẽ là phần thưởng tuyệt vời hơn bất cứ thứ gì dành cho 38696!」"
"1884" = "「Để 38696 lại, rời khỏi Omuta,\\nMikuro, thực sự đã rất bất an, nhưng mà――」"

# グランドリライト10_ハチロク.txt.toml
[script]
"1181" = "「……Đoàn tàu, đã có thể dừng lại.\\nNếu có mười bốn giây đó. Dù không cần phải \\x%l脱線転覆;#00ffc040;trật bánh lật tàu%l;#; đi chăng nữa」"

# グランドリライト11_ナインスターズ！.txt.toml
[script]
"2485" = "「Mọi người của Ohitoyo... những người đã ủng hộ Đường sắt Ohitoyo.\\nChắc hẳn sẽ rất vui nhỉ. Khi thấy đội hình đó trên sân khấu rực rỡ này.」"

# ニイロク02_御一夜旅行.txt.toml
[script]
"1571" = "「Ư!!! Ừm. Ừm! 'Đi đường bình an'.\\nHừm...... Ufufu――Ufufufufu.」"
"1592" = "「Ừm. Ừm. ......Ufufufufufu.」"

# ハチロク03_冥国式レイルロオド.txt.toml
[script]
"2212" = "「V-Vâng. Em rất vui ạ. Vậy thì——Ufufu.\\nCho phép em gọi chị là bé Olivy nhé?」"

# ハチロク04_小畑越え.txt.toml
[script]
"2489" = "「Ái chà, Ufufufu.\\nChắc chắn là vì có tôm ở trong đó rồi ạ.」"

# ハチロク04_煙には煙を.txt.toml
[script]
"2166" = "「Em đã hiểu. Thưa ngài Soutetsu, Master của em.」"

# ハチロク05_軋み.txt.toml
[script]
"1437" = "「Không phải đâu. Không phải là khiếu nại từ bên trong Hiệp hội Thương mại Ohitoyo đâu.\\nNhờ có nó mà buôn bán phát đạt, bên này còn đang phải cảm tạ \\x%l8620;#00ffc040;8620%l;#; ấy chứ.」"

# ハチロク06_のぞみ.txt.toml
[script]
"2321" = "「Ngoạm――liếm――Nfufufu~\\nNè, Olivy không muốn kem bị chảy đâu, nên cứ vừa đi vừa ăn cũng được nha.」"
"2322" = "「Ngoạm――ưm, Ufu――à ừm, nè. Hachiroku.\\nTại sao lúc nào cậu cũng đối xử với Olivy như em bé vậy?」"
"2671" = "「Ví dụ như…… chạy một chuyến tàu du lịch vòng quanh siêu sang trọng\\nnhư Tàu tốc hành Phương Tây ở Hinomoto chẳng hạn」"

# ハチロク09_もくもくオリヴィ.txt.toml
[script]
"1608" = "「Ây da, Ufufu. Đúng là vậy nhỉ.」"
"2011" = "「Hơn nữa……Ufufu, thực ra chúng tôi,\\ncũng đang rất mong chờ được ngồi ở \\x%l客車;#00ffc040;toa hành khách%l;#; ạ.」"

# ハチロク14_冬.txt.toml
[script]
"2643" = "「Nfufu.」"

# ハチロク15a_痛みとの決別.txt.toml
[script]
"1436" = "「Mở khóa toàn bộ……」"
"2049" = "「Không, có chuyện đó đâu! Olivy, dù được sản xuất tại Meriken,\\ndù anh không phải là Master, hay \\x%lレイルロオド;#00ffc040;Railord%l;#;, đi chăng nữa」"
"2178" = "「Tải trọng trục!! Nhẹ hơn 8620 rất nhiều!!\\nĐầu máy số 9! Cứ cho đầu máy số 9 chạy là được mà!!!」"
"2199" = "「Vậy thì, trước tiên hãy thử khởi động lại bắt buộc xem sao」"

# ハチロク15b_さよなら列車.txt.toml
[script]
"1571" = "「Phà……Ufufu——ehehe~.\\nThấy chưa? Ngon, đúng không?」"
"1683" = "「Tao cũng bất ngờ lắm. Hơn nữa lại còn là chuyến tàu đi Yatsushiro——\\nKhông ngờ lại được chạy đầu máy số 9 trên tuyến chính đấy」"
"1689" = "「Tôi là Hayase, \\x%l車掌;#00ffc040;trưởng tàu%l;#; của Đường sắt Ohitoyo. Dạ——Trưởng ga hỏi là,\\ncó thể ghép thêm hai toa hành khách nhẹ nữa không ạ」"

# ハチロクh1_契り.txt.toml
[script]
"1219" = "「A……Ngài……Soutetsu……ưm――\\nNgực――của em……thì có gì……Nfu.」"
"1229" = "「Hia!? A――Ngài Soutetsu――Ngài Soutetsu――\\nƯm! Bướm――của, em――Nfu.」"
"1239" = "「Ku——a——」"
"1282" = "「Nkyuuuuu!!」"

# ハチロクh2_お勉強の成果.txt.toml
[script]
"1036" = "「Ưm——Nfu——Fu, a」"
"1039" = "「Ưm——ực——Nku——ực」"
"1051" = "「Nfu!」"
"1056" = "「Naa! Cậu, bé——cậu bé đang, ngoáy mạnh\\ntrong cô bé, của em, em cũng thích!」"

# ハチロクh3_磨き洗い.txt.toml
[script]
"1089" = "「Phần đỉnh, của cậu bé——là——Ku, a——\\ngọi là——quy đầu——người ta thường nói, vậy đấy」"
"1835" = "（Phậpppppppppp!!!）"

# ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml
[script]
"1013" = "「A——a——em không biết——cảm giác này——a——\\nđang cắm vào——vậy mà——sâu, quá——vậy mà——Nku」"

# ハチロクh5_おだいどこしごと.txt.toml
[script]
"1602" = "Nghe tôi nói vậy, Suzu khẽ cười Ufufu."

# ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml
[script]
"852" = "「Hà——a——vẫn còn——to——ưm——\\nưm——Fua——Nku!!!」"
"885" = "「Ưm——phù——phù! Phù! Nfu! Ưm——\\nphù! Phù! Phù! Phù ư ư!!!」"
"887" = "「Ưm——phù——rộp——rộp——ưm——\\nchụt——Nku——phù——phù ư ư!」"
"889" = "「Ưm——phù——ưm! Ưm! Mút——\\nchụt! Phù——Nfu——ưm! Ưm ưm!!」"
"924" = "「Nhyu——ưm——Nyu——ưm ưm~——\\nphù——Nfu——phù——phù~——」"
"935" = "「Nku!!!!」"
"937" = "「Nku!? Kahyu——a? Ngài, Soutetsu\\n——của, em——bên trong——đã đến, nơi——sâu, nhất rồi.」"
"941" = "「Ưm! Phù! Phù! Ưm! Phù! Fua!\\nƯm! Nku! Ưm!!!」"
"958" = "「Cả chuyện của các em gái——chuyện cộng cảm, mọi thứ——\\nngay cả chuyện của 8620, khi kết nối với ngài, cũng tan biến, mất.」"

# ハチロクh7_レトロモダンメイクラヴ.txt.toml
[script]
"754" = "「Hi——a——lại nữa! A——em——\\nlại nữa——Nkyu——đến rồi——sướng, quá!!」"
"759" = "「Hí a! Ưm——mông——Fua——mông, cũng……\\nmà——bây giờ, thì……ưm——Nkuuuu~~」"
"783" = "「A——hi——ức——khục——Na——\\nchậm——chậm——lại, đi——ưm~Ư!」"
"840" = "「Ngugu!」"
"841" = "「Ngu!!?」"
"970" = "「Ngài Soutetsu! Phu quân——Na!!!」"
"1811" = "（Phậpppppppppppppppp!!!!）"
"1820" = "（Phậppppppppppppppp!!!）"
"1824" = "（Phậpp）"
"1826" = "（Phậppppppppp!!!）"
"1831" = "（Fuwa）"
"1844" = "（Mút——chùn chụtttt——bật nảy!）"

# ハチロクh8_桜色のひめごと.txt.toml
[script]
"732" = "「Fua!? Chỗ đó! A——a——ưm——!\\nNku~~~~~~~~~~~~~~~~~!!!」"
"737" = "「Hia! A——a——Nku!! Phù!」"
"836" = "「Nkyuuuuuuuuuuuu!!!!」"
"837" = "「Nu」"
"839" = "「Nku——ực——ực——ực——chóp chép」"
"855" = "「Chỗ đó——tuyệt quá——ưm——Fua——tuyệt quá——\\ntuyệt quá——mất——Nu——em——mạch điện」"
"1528" = "（Phậppppppppp!!! Cộc!!）"
"1558" = "（Ực!! ——Chụtttttttttt!）"
"1572" = "（Phụttt! Phụt! Phụt! Phụt）"
"1581" = "（Thọcccccccccccc!）"

# ハチロクh9_コノフクハキルコト.txt.toml
[script]
"2035" = "「Hu……a——ưm——rộp——chụt——\\nliếm láp——mút mát——rộp——ưm——Muchu」"
"2135" = "「Juruuuuu! Juboo——Nku!?」"
"2177" = "「Nhyufuuuu!!?」"
"2179" = "「Nbu!!!!?」"
"2180" = "「Nkyu!!?\\nFuaaaaaaaaaaaaaaaaa!!」"
"2181" = "「Nbu!? Ưm——\\n（Ực, ực, ực, ực）」"
"3502" = "（Phụtt! Phụt! Phụt phụt! Phụttt!）"

# ポーレット01_ポーレット退任.txt.toml
[script]
"2547" = "Giọng nói mềm mại, êm ái.\\nPaulette cũng khẽ bật cười Ufufu."

# ポーレット03_廃炭鉱.txt.toml
[script]
"1728" = "「Chừng nào chúng tôi còn ở trên này, \\x%l8620;#00ffc040;8620%l;#; sẽ không chạy.\\nToàn bộ tuyến này sẽ trở thành khu vực \\x%l閉塞;#00ffc040;Đóng đường%l;#; độc quyền của \\x%lキハ07;#00ffc040;KiHa 07%l;#;.」"

# ポーレット07_うさぎ.txt.toml
[script]
"1644" = "「Ufufu~, Ufufu~」"

# ポーレット07_支線.txt.toml
[script]
"2311" = "Sau khi đưa \\x%l列車;#00ffc040;đoàn tàu%l;#; chiều về đến Ohitoyo,\\n\\x%l8620;#00ffc040;8620%l;#; sẽ quay đầu và đợi chúng tôi ở ga bỏ hoang Jutsusen."

# ポーレット11_記憶と記録.txt.toml
[script]
"1512" = "「Nếu vậy, dùng 8620 cũng được mà đúng không.」"
"1528" = "「Ý tôi là vậy đấy. Nếu làm vậy mà có thể chạy lại được, thì có khởi tạo lại \\x%lタブレット;#00ffc040;Thẻ bảng (Tablet)%l;# của tôi cũng không sao.」"
"1714" = "「Điều đó……đúng là vậy nhỉ.\\nNếu chỉ lấy 8620 làm trung tâm để chấn hưng du lịch thì không nói làm gì――」"

# ポーレットh1_ファーストセックス.txt.toml
[script]
"1026" = "「Ưm... phù... v, âng——Tim đập,\\nnhanh——thế này——là lần đầu, tiên... Nfu.」"
"1027" = "「Ưm... Ku.」"
"1041" = "「Nnfu! Trực, tiếp——á——tuyệt quá.」"
"1106" = "「Nên là——ưm, hãy di, chuyển... a...\\nanh Soutetsu, này——bên trong, em——Nkyu!」"

# ポーレットh2_制服変更？.txt.toml
[script]
"909" = "「Một chút——nữa thôi——Ku——á——\\nNếu ra——, thì cùng nhau——」"
"929" = "「Hya——á!\\nNuu——Fue——Fuyaa.」"
"957" = "「Fue... a... Fuyaaaaa.」"
"978" = "「Ồ——Ku——」"

# ポーレットh3_誘惑アイスコーヒー.txt.toml
[script]
"1655" = "（Phụt! Phụt! Phụt! Phụtt!）"

# ポーレットh4_クリーム＆クリーム.txt.toml
[script]
"892" = "「Ku——Ư——」"
"894" = "「Ku!」"
"921" = "「Ku——ưm」"
"951" = "「Ư——Ku——」"
"1590" = "（Phụtt! Phụt!）"
"1624" = "（Liếmmm）"
"1627" = "（Siết! Siếtttt!!）"
"1638" = "（Ngoáyyyy!!）"

# ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml
[script]
"856" = "「Ya! A——mềm quá——ưm——Na! Trơn tuột——ấm quá——phù, Kyu——Phùù」"
"1003" = "「Paulette! Nữa đi——Ku!\\nHơn nữa——vào sâu, hơn nữa」"
"1722" = "（Mútt!!!!）"
"1735" = "（Phậpppppppppp!!!）"

# ポーレットh6_あなたとふたりの学園エッチ.txt.toml
[script]
"1558" = "（Phụt——phụtt——phụt! Phụtt!）"
"1560" = "（Phụt! Phụt! Phụtt! Phụt!!!）"
"1580" = "（Trượtt——dập!）"

# ポーレットh7_残業エッチもyシャツで.txt.toml
[script]
"900" = "「Ư——Ku」"

# ポーレットh8_気動車の国のアリス.txt.toml
[script]
"2273" = "「Ưm——Ku——」"
"2275" = "「Ưm——Ku——（ực）」"
"2370" = "「Nfufu, haha hihi haa」"
"3751" = "（Phậpppp——rột）"
"3770" = "（Thọc sâuuuuu——thọc——rút raaa——rút）"

# 仲国04_z49列車.txt.toml
[script]
"2014" = "「Thực sự rất vui ạ!\\nVừa nằm, Ufufu, vừa tận hưởng chuyến du lịch bằng tàu hỏa thế này.」"

# 仲国05_真夜中の餐車.txt.toml
[script]
"1605" = "「……Đúng vậy. Ngay cả với thân bảo trì cũng có thể nhận ra,\\nchắc chắn độ dốc không hề nhỏ.」"

# 仲国06_聖都とパンダとハチロクと.txt.toml
[script]
"2513" = "Thấy tôi trầm trồ, Hachiroku khẽ cười Fufu."

# 仲国08_謝謝再見！.txt.toml
[script]
"2823" = "(Cả tôi, Hibiki, hay thậm chí là Hachiroku. Không một ai——\\ntừng mơ đến việc kết nối tuyến đường ray giữa Hinomoto và Trung Quốc.)"

# 共通02_日々姫と真闇と人形と.txt.toml
[script]
"1895" = "「À, không. Có thay đổi chứ.\\nHibiki chắc chắn đã thay đổi rất nhiều.」"

# 共通03_ハチロクとナビ.txt.toml
[script]
"1546" = "「Quả thực……Fufu, em đã tình cờ,\\nnhận được một thông tin xung quanh rất có ý nghĩa.」"

# 共通06_8620を探せ.txt.toml
[script]
"2760" = "Cô ấy nheo mắt lại đầy hoài niệm,\\nrồi Fufu mỉm cười hạnh phúc."

# 凪h2_おとなの水着.txt.toml
[script]
"2477" = "「Nfufu~ Vậy thì lần này,\\nđến lượt anh hai làm em sướng á!」"
"2479" = "「Nfufu——Anh hai, giọng đáng yêu ghê á」"
"2489" = "「Ku——Phù——Nhyu——Ưmmm~!!」"
"2540" = "「A, dương vật giật giật rồi á!\\nNfufu, muốn được sướng không á?」"
"4010" = "（Phụt! Phụt! Phụtt! Phụt!）"
"4040" = "（Phậppppp!!! Bụp!!!!）"
"4064" = "（Sụttt!!）"

# 凪ふかみ01_凪の成長、ふかみの成長.txt.toml
[script]
"1833" = "「Lúc khó khăn thì phải giúp đỡ lẫn nhau chứ, Nagi.\\nHơn nữa……Ufufu, tớ còn được cưỡi Navi nữa, lời to rồi.」"

# 凪ふかみ01_流れ.txt.toml
[script]
"2252" = "Tôi không hiểu có gì khác biệt.\\nFukami cười Ufufu, vui vẻ mỉm cười và tiếp lời."

# 凪ふかみ02_命の重さ.txt.toml
[script]
"1448" = "「Phía tôi không sao ạ.\\nMay mắn là 8620 cũng không có dấu hiệu bất thường nào.」"

# 凪ふかみ04_ふかみの決意.txt.toml
[script]
"3294" = "（Bụp!）"

# 凪ふかみ07_少しずつ、大人に.txt.toml
[script]
"2758" = "Gương mặt Nagi, Hachiroku và Hibiki giãn ra với nụ cười 'Ufufu'.\\nCó lẽ tôi cũng đang làm vẻ mặt tương tự."

# 凪ふかみ08a_凪エピローグ_一番ほしい、一番.txt.toml
[script]
"1707" = "「Phư…… Ufufu! Ufufufufufu!」"
"2585" = "Nagi giật bắn mình! Vươn thẳng lưng lên.\\nAnh Soutetsu bật cười Fufu."

# 凪ふかみ08b_ふかみエピローグ_赤を切る勇気.txt.toml
[script]
"3388" = "Khi bé Fukami cười Fufu,\\nkhuôn mặt anh hai cũng giãn ra thành một nụ cười."

# 凪ふかみ08c_新しい家族.txt.toml
[script]
"2413" = "「Tất nhiên rồi!\\nĐó là lời thỉnh cầu của tình đầu mà.」"

# 凪ふかみh1_修学旅行の夜.txt.toml
[script]
"1229" = "「Ưm……Ku――」"
"1230" = "「Ư——Ku」"

# 凪ふかみh2_みずあそび.txt.toml
[script]
"1297" = "「Nfu——ưm——Euuu——liếm」"
"1369" = "「Ưm——phù——phù! Nfu!」"
"2132" = "（Phụt! Phụttt! Phụt! Phụt!）"
"2133" = "（Phụt! Phụtttt! Phụt! Phụtt）"
"2149" = "（Rúttttttttttt!!）"
"2150" = "（Rúttttttttt!）"
"2154" = "（Phập! Phập! Phập! Phập!）"
"2163" = "（Ùmmmmm!）"

# 日々姫02_文庫森.txt.toml
[script]
"1691" = "「Nfufu.」"

# 日々姫05_御一夜ステーションカフェ.txt.toml
[script]
"2143" = "「Chà, có cả ảnh của 8620 nữa.」"

# 日々姫06_みくろ、来訪.txt.toml
[script]
"2249" = "「Vì vậy, mọi người đều rất bận tâm chuyện không thể bảo dưỡng cho 38696.\\nĐiều đó lại càng khiến Mikuro cảm thấy áy náy hơn.」"
"2421" = "「Mikuro nghĩ, được sở thú nhận nuôi\\ncùng với 38696 thật là tốt quá.」"

# 日々姫08_開きかけのつぼみ.txt.toml
[script]
"2254" = "「Không có gì đâu ạ.\\nChúng ta là bạn từ thuở nhỏ mà.」"

# 日々姫09_run_with_our_dreams.txt.toml
[script]
"1825" = "「Vì thề trước mặt con người, nên gọi là lễ cưới trước mặt mọi người. Lễ cưới thề trước thần linh,\\ncó vẻ được gọi là lễ cưới trước mặt thần linh ạ.」"

# 日々姫h1_マッサージの続き.txt.toml
[script]
"1892" = "（Phậpppppppp!!!!）"

# 日々姫h2_洗って大丈夫なスーツ.txt.toml
[script]
"1787" = "（Trượtttt!!!）"

# 日々姫h3_汚れてしまった制服で.txt.toml
[script]
"1037" = "「Hyaha!? A――a――Hà――Ku――」"
"1108" = "「Ưm――Ku――a――\\nHibiki! Hibiki! Hibiki!!」"

# 日々姫h4_いもうとタオル.txt.toml
[script]
"1757" = "（Phậpppppppp!!!）"

# 日々姫h5_白濁絵の具の射精会.txt.toml
[script]
"1150" = "「Hia――a――a――Nóng quá――đang vào――rồi\\n――Na――Màu, vẽ――của――anh hai――」"
"1163" = "「Ư――Ku!」"
"1166" = "「Ku――!」"
"1171" = "「Kefu――eho――ưm, Ku――phù――ưm!!\\nPhù――chụt, chùn chụt! Chụt! Chùn chụt」"
"1182" = "「Fua――Nfu――phù――hà――Vui quá――\\nĐược nghe thấy――giọng nói dễ thương, của anh hai rồi♪」"
"1187" = "「Phù……Fa……ưm――Chiếc cọ――của anh hai――\\nƯm……hà――Nóng, quá――ưm――Ku!」"
"1190" = "「Fua……a……a……ưm……Ku――a――\\nHà――hà――hà……Fu, a――a」"
"1202" = "「Ku――」"
"1219" = "「Ku!!?」"
"1241" = "「Ưm――ưm――Ku! Ưm――a――ưm mu~n……\\nƯm――ưm ưm――phù――ưm――ưm~~~」"
"1249" = "「Ưm……Ku――」"
"1265" = "「Nbuuuuuu!!!!?」"
"1353" = "「Chim, của anh――Ku――\\ntuyệt――ưm――như thế nào?」"

# 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml
[script]
"2100" = "「Hà――hà――Thế này……hình dáng……rất,\\nrõ ràng――chim――của anh――ưm――Na!」"
"2138" = "「Ể――từ từ――ưm……Ku――\\nHà, a――ưm――Fua!」"
"2240" = "「Ưm――Ku――ực――ưm――chụt――\\nChụt――chùn chụt――ực」"
"2709" = "「A――Của anh hai――ưm――lún sâu, vào――\\nrồi――Fua――a……Ku――phù」"

# 真闇h1_長期熟成.txt.toml
[script]
"1056" = "「Chụt――ưm……Nchu――rộp――liếm\\n――ưm……Nfu……Fu」"
"1058" = "「Chururu――chụt――rột――Nchuu.」"

# 真闇h2_無濾過.txt.toml
[script]
"1084" = "「Kyu! Phư――Ya――a――aa, ưm!」"
"1820" = "（Phậpppppp!）"
"1884" = "（Trượttttttt!）"

# 稀咲02_新事業案.txt.toml
[script]
"1930" = "「Ưm…… cái này——một khi đã nắm được nhịp độ thì……\\nFufu, mặc dù cơ thể khá mỏi——nhưng lại thấy, hơi vui vui.」"
"2238" = "「Thật không ngờ……\\nUfufu, thực sự rất ngon đấy? Giỏi quá đi.」"

# 稀咲03_純白のレール.txt.toml
[script]
"1821" = "「Ưm——Fufu, cuối cùng cũng chịu nói! Bắt anh phải nói ra!\\nEm đã phải nhẫn nhịn vất vả lắm đấy. Suýt chút nữa là em đã nói ra trước mất rồi.」"

# 稀咲h1_性生活.txt.toml
[script]
"1306" = "「Nkyu――kuha――Na――~~~Ư!!!」"
"1466" = "「Vậy sao…… sờ ngực…… cũng――là lần đầu tiên…… à――\\nƯm――Nfufu――fu――ưm――fua――a」"

# 稀咲h2_プライベートルーム.txt.toml
[script]
"912" = "「Ư――A――ờ――………… ừm.\\nTôi không nhận ra là hơi thở hay nét mặt của mình đã thay đổi đâu」"
"1152" = "「Hyaa u! ――Nu!!?」"
"1190" = "「A…… Nfu――Anh mạnh bạo quá đấy, Soutetsu.\\nĐến mức đó, em đã――」"
"1199" = "「Chụt――chụt――chụt――Muchu――」"
"1219" = "「Nkyu――Ư――ha――~~~~~Ư!!!」"
"1220" = "「Nfu――a――」"
"1221" = "「Nfu」"

# 稀咲h3_チャイナドレスでおもてなし.txt.toml
[script]
"2207" = "「Pua. Nfu……」"
"2265" = "「Ưm…… Fu――ưm――chụt――chu mu――\\nchu ru――chụt――Nchu――Fu…… a――」"
"2268" = "「Ưm…… phu…… ưm――ực――\\nchu zu――ưm――ực――ực――Nfu」"
"2278" = "「Nkyu!?」"
"3786" = "（Chụtttttt!!）"
"3819" = "（Cọoooooo!）"

Kết bài

Đợt U15a quyết **60 mục / 418 dòng mới** trong 104 file: M7 follow-up 60 dòng "Hự"→"Ku" (thực tế 60, không phải 59 — U12a bỏ sót lr_日々姫h2 1159); M15 sweep 113 dòng dạng tách → romaji N… (gồm 2 dòng GHÉP: lr_ポーレットh1 1003 với M7, lr追加_みくろ 1840 với M24); M24 97 dòng token cười viết hoa (98 ứng viên − 1 dòng GHÉP vào M15); HAS-RUN 99 dòng sửa số chữ kéo dài (v2: 106 FIX entries / 28 KEEP; 103 dòng unique − 4 ghi đè thành KEEP sau khi đọc tay = 99); G15 29 dòng bỏ markup ruby [x,n] rò rỉ; M10 2 dòng ふえっ→"Fue"; F5 4 dòng viết hoa token romaji; các dòng lẻ M18/M27/M28/M37/M47/M51/M61/M62×2/M63; và 4 dòng lẻ Grand11-2485/P03-1728/F-T56-1/P07-2311. 39 mục còn lại quyết GIỮ NGUYÊN 0 dòng (xem §4), trong đó M3 scream boundary: M3 KHÔNG mở rộng sang 175 dòng scream non-H; M55/M56 KHÔNG TÁI HIỆN. Lượt soát 2: 418/418 tái kiểm chứng, 0 loại, 55 sửa (34 lỗi đếm HAS-RUN + 19 dấu ngoặc kép M24 + 2 token rơi HAS-RUN). Khối TOML 104 file / 418 key parse-verified. Còn nợ coordinator: các cờ §5 (M18 mở rộng "Kuuun", M7 （ ）/non-H/"nhự", sweep F5 rộng, ふかみh2 1000, T75/T77/T78 appendix + 帝央, HAS-RUN quan sát ngoài phạm vi, cờ U14).

## Phụ lục — Ghi chú gộp của coordinator (22/11 ~14:40)

Worker giao 418 dòng; file JSON gộp còn **402 dòng** (395 dòng mới + 7 dòng GHÉP). Chuỗi tổng sau đợt này: **235 mục / 3.610 dòng** (cơ sở 180/3.215 + 55 mục mới / 395 dòng mới — xem snippet).

**23 dòng trùng với batch song song (21 với U15b + 2 với U16):**
- 16 dòng BỎ khỏi JSON gộp (giá trị GHÉP = fix của batch gộp trước — giữ lại sẽ ghi đè ngược):
- lr_ニイロクh_誓い。約束.txt.toml 1322
- lr_ニイロクh_誓い。約束.txt.toml 1387
- lr_ポーレットh2_デコレーション＆ミルク.txt.toml 1084
- lr_凪h2_虎さんの交尾.txt.toml 1258
- lr_凪ふかみh1_じぇいけい！.txt.toml 1616
- lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml 1440
- lr_稀咲ポーレットh1_悪い大人の契約.txt.toml 1513
- lr_稀咲ポーレットh1_悪い大人の契約.txt.toml 1604
- lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml 1901
- れいなh3_おもらし自由化大作戦.txt.toml 1092
- ハチロクh3_磨き洗い.txt.toml 1677
- ポーレットh8_気動車の国のアリス.txt.toml 2241
- 稀咲02_新事業案.txt.toml 1900
- 稀咲h1_性生活.txt.toml 1473
- 稀咲h1_性生活.txt.toml 1482
- 稀咲h3_チャイナドレスでおもてなし.txt.toml 2465
  Trong đó 10 dòng fix giống hệt U15b (1322, 1387, 1258, 1440, 1604, 1901, 1677, 1473, 1482, 2465); 5 dòng U15a đổi token đã có sẵn trong fix U15b (1084 "Kuuun", 2241 "Ku", 1616 "Ufufu", 1513 "Fufu", 1092 "Nfufuuuu~"); 1 dòng đổi token đã có sẵn trong fix U16 (1900 "Fufu" + "em").
- 7 dòng GHÉP (giữ lại, old_vn = fix batch gộp trước, fix = giá trị GHÉP — mỗi giá trị đã kiểm chứng bằng 2 cách dựng độc lập):
- lr_ポーレットh1_家族旅行の最終日の夜.txt.toml 1096: old_vn = '「Ưm kyu——Fa——a, thế này——thích quá—— ư ư——Phu——nè——cứ thế này——nữa đi」' → fix gộp = '「Nkyu——Fa——a, thế này——thích quá—— ư ư——Phu——nè——cứ thế này——nữa đi」'
- lr_凪h1_痛いの痛いの飛んでけばい.txt.toml 1162: old_vn = '「Ưm ku!? Pu――Fa――ưm――Juru!\\nJubo! Jubu! Juba! Chụụụt」' → fix gộp = '「Nku!? Pu――Fa――ưm――Juru!\\nJubo! Jubu! Juba! Chụụụt」'
- lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml 1855: old_vn = '「Ưm Hyuuuuuuuuu!」' → fix gộp = '「Nhyuuuuuuuuu!」'
- lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml 1857: old_vn = '「Ưm kyu! Fua! A── trượt── tuột, ra── Aaaa── anh hai── vào hết, mất」' → fix gộp = '「Nkyu! Fua! A── trượt── tuột, ra── Aaaa── anh hai── vào hết, mất」'
- 真闇h1_長期熟成.txt.toml 1056: old_vn = '「Chụt――ưm……ưm chụt――rộp――liếm\\n――ưm……ưm fu……Fu」' → fix gộp = '「Chụt――ưm……Nchu――rộp――liếm\\n――ưm……Nfu……Fu」'
- 稀咲h2_プライベートルーム.txt.toml 912: old_vn = '「A――ờ――………… ừm.\\nTôi không nhận ra là hơi thở hay nét mặt của mình đã thay đổi đâu」' → fix gộp = '「Ư――A――ờ――………… ừm.\\nTôi không nhận ra là hơi thở hay nét mặt của mình đã thay đổi đâu」'
- 稀咲h3_チャイナドレスでおもてなし.txt.toml 2265: old_vn = '「Ưm…… Fu――ưm――chụt――chu mu――\\nchu ru――chụt――ưm chu――Fu…… a――」' → fix gộp = '「Ưm…… Fu――ưm――chụt――chu mu――\\nchu ru――chụt――Nchu――Fu…… a――」'
  Xung đột 1855 đã quyết ở đợt U15b: M15 thắng — "Nhyuuuuuuuuu!" (gộp tách "Ưm hyu"→"Nhyu"); "Ưm Hyuuuuuuuuu!" của U15b bị thay thế.
  old_vn của U15a ở 1513 CŨ (trước fix U7b: "Anh Soutetsu—— Anh Soutetsu——…——anh Soutetsu?") — old_vn đúng theo thứ tự gộp là fix U15b; dòng này đã bỏ (xem trên).

**Hiệu chỉnh old_vn 1339 (M7):** old_vn worker ghi "——Ư, hự——" KHÔNG khớp bất kỳ layer nào (CSV3 "——hự——"; không có fix audit/moan/unif nào cho dòng này — "Ư," là worker tự thêm). old_vn gộp = giá trị CSV3 "「Cho cậu nhỏ đang cương cứng vào cửa âm đạo——hự——\nThế này——đã đúng, chưa?」"; fix giữ nguyên "Ư, Ku" (JP "――っ、くっ――": っ → "Ư" theo quy tắc gasp + くっ → "Ku" theo M7 — giá trị fix đúng, chỉ old_vn sai).

**Hiệu chỉnh số mục:** worker ghi 60 mục; 5 mục đã tính ở batch trước nên không cộng lại: M7 + M10 + M15 (U12a), M3 (U11b), F5 (U15b). Mục mới đợt này = 55. (Kết bài worker ghi "39 mục giữ nguyên" là slip — §4 liệt kê đủ 40 mục giữ: 20 mục §3 có dòng + 40 mục giữ = 60.)

**Kiểm chứng lại sau gộp (coordinator, từ disk):** JSON 402 dòng — jp/tw khớp CSV3 0 lệch, old_vn khớp map đã gộp 0 lệch, 0 fix==old_vn, 0 newline thật, 0 trùng (file,key); khối TOML §7 402 key = JSON 402/402. Các "problem" trong `_u15a_verify_m.py` đều là artifact của script kiểm, không phải lỗi fix: ハチロク06 2322 "Ufu" (JP うふっ = 2 mora, ngoại lệ có chủ ý); ハチロクh7 759 "Nkuuuu~~" đúng (JP んくぅぅぅ～～っ = 4u + ~~; script kiểm đếm thừa 1u); 日々姫h5 1265 tồn tại (file đúng là 白濁絵の具の射精会, script kiểm ghi sai tên file お留守番デート; "Nbuuuuuu" = 6u đúng JP んぶうううううっ).
