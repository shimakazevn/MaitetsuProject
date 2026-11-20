# Audit — 凪ふかみ05_凪の開眼！？.txt.toml

- File: `凪ふかみ05_凪の開眼！？.txt.toml` — route 07_Nagi_Fukami, 478 dòng script (343 thoại, 135 độc thoại).
- Người nói: 凪 141, monologue 135, ハチロク 55, 稀咲 48, ふかみ 37, 双鉄 29, れいな 13, ポーレット 10, 車椅子の方 7, 鈴木 3.
- Nội dung: ngày "mở mắt" của Nagi — giúp bà lão xe lăn qua đường ray (Fukami mở đường bằng kinh nghiệm thuyền xuôi dòng, tìm được tấm thẻ lấp lánh trong khe ghế); thi xúc than với Soutetsu (55 xẻng/2 phút); Hachiroku dạy chỉnh trang/cư xử; Kisaki dạy TPO, kính ngữ và đổi "bai"→"desu"; kết bằng chuyến tu học cùng "anh hai" làm mục tiêu trở thành "người phụ nữ tuyệt vời".
- **Kết quả: 18/478 dòng sai (3,8%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (478 dòng, 0 khóa trùng, 0 ô VN trống); VN khớp TOML tuyệt đối 478/478 (0 lệch thực chất). `[selections]` rỗng.
- Thẻ `%l`: 13 thẻ trong VN — 6 thẻ JP có sẵn đều đúng (3040, 3156, 3167, 3276, 3079, 3069; chỉ sai chính tả Kiha ở 2 thẻ), 7 dòng VN tự thêm thẻ (2214, 2215, 2391, 2479, 2522, 2475, 2989 — xem §2). Không có thẻ `%l` sai định dạng (thiếu `;`) trong file.
- TOML md5 `0596fd7ef8f679f40a5822decef70eec`; không có bản sao file này (không thuộc 11 nhóm trùng — đã kiểm tra md5 toàn bộ 227 file).
- Nagi→Fukami "bé"/Fukami tự xưng "mình"/Fukami→Nagi "cậu": kiểm tra toàn file — không có dòng nào dùng sai "chị"/"em" cho cặp này (Fukami với Nagi dùng "tớ"/"cậu" nhất quán: 2301, 2431, 2443; Nagi gọi Fukami bằng tên). Soutetsu "anh" với Nagi/Fukami đúng toàn file (2183, 2380, 1935...); "tôi" với Hachiroku đúng (không có "anh" sai đối tượng).

## §2. Danh sách sửa (18 dòng)

Phân loại: xưng hô/đại từ 2 (2578, 2648), thuật ngữ 4 (2228, 2960, 3167, 3276), thẻ %l VN tự thêm 7 (2214, 2215, 2391, 2479, 2522, 2475, 2989), gasp 1 (2058, từ sweep), SFX 4 (1970, 2039, 2068, 3264).

### 1970 — ハチロク — SFX
- JP: 「帽子をあみだに被るから、汗で髪も乱れてしまって……\nふぅ。まずは身だしなみから、ですね」
- TW: 「你帽子戴得靠後，頭髮都被汗水沾濕了，亂糟糟的……唉，首先整理好儀容儀表吧」
- VN cũ: 「Đội mũ lệch ra sau nên tóc tai đẫm mồ hôi bù xù hết cả lên rồi này……\nPhù. Bắt đầu từ việc chỉnh trang lại vẻ ngoài trước nhé.」
- Sửa: 「Đội mũ lệch ra sau nên tóc tai đẫm mồ hôi bù xù hết cả lên rồi này……\nPhùù. Bắt đầu từ việc chỉnh trang lại vẻ ngoài trước nhé.」
- Lý do: JP ふぅ (1 ぅ) → VN cần 2 nguyên âm theo công thức (1 + số う/ぅ); VN cũ "Phù." thiếu 1 nguyên âm. Tiền lệ Hibiki05 key 1509 (ふぅ "Phù."→"Phùù.").

### 2039 — 凪 — SFX
- JP: 「ひゃっ」
- TW: 「呀」
- VN cũ: 「Á.」
- Sửa: 「Hya.」
- Lý do: JP ひゃっ — tiếng kêu giật mình của Nagi khi lược lạnh chạm vào đầu. VN cũ "Á." làm mất âm ひゃ; cùng âm này ở key 2095 đã dịch đúng là "Hya!" — sửa cho nhất quán trong file.

### 2058 — 凪 — gasp っ
- JP: 「ふぃ～～っ」
- TW: 「呼～～」
- VN cũ: 「Phù~~」
- Sửa: 「Phù~~Ư」
- Lý do: Sweep (lost-gasp-trailing): JP 「ふぃ～～っ」 — gasp っ sau dấu kéo dài; VN giữ dấu ~~ nhưng bỏ mất gasp. Áp nguyên giá trị sweep "Phù~~Ư" (đã kiểm chứng với JP).

### 2068 — 凪 — SFX
- JP: 「うち……はうっ――私。\n全然、大人じゃなかった――です」
- TW: 「咱……呃……我呀。完全算不上……大人」
- VN cũ: 「Tớ…… hauu——em.\nHoàn toàn chưa phải là người lớn——desu.」
- Sửa: 「Tớ…… hau——em.\nHoàn toàn chưa phải là người lớn——desu.」
- Lý do: JP はうっ (1 う + っ ngắt) → VN cần 2 nguyên âm theo công thức; VN cũ "hauu" có 3 nguyên âm (dài ra, ngược với っ ngắt). Đối chiếu key 2085: はうう (2 う) → "Hauu" đúng 3 nguyên âm.

### 2214 — 凪 — thẻ %l VN tự thêm (gỡ)
- JP: 「逆転機、ミッドギア！！　ばい！」
- TW: 「回動機調至中位檔！！　好嘞！」
- VN cũ: 「\x%l回動機;#00ffc040;Cần đảo chiều%l;#;, \x%l中位檔;#00ffc040;tầm trung%l;#;!! Xong!」
- Sửa: 「Cần đảo chiều, tầm trung!! Xong!」
- Lý do: JP không có thẻ %l nào — VN tự thêm 2 thẻ gloss, lại lấy từ TW làm từ JP (回動機/中位檔 là từ của TW, JP nói 逆転機/ミッドギア). Tiền lệ file 09 (gỡ 4 thẻ VN tự thêm) và file 11 (gỡ 3 thẻ): gỡ thẻ, giữ lại nghĩa gloss đúng bằng chữ thường.

### 2215 — 凪 — thẻ %l VN tự thêm (gỡ)
- JP: 「逆転機！　前進フルギアー！！！」
- TW: 「回動機！　滿檔前進！！！」
- VN cũ: 「\x%l回動機;#00ffc040;Cần đảo chiều%l;#;! \x%l滿檔前進;#00ffc040;Cài hết số tiến%l;#;!!!」
- Sửa: 「Cần đảo chiều! Cài hết số tiến!!!」
- Lý do: Như 2214: JP không có thẻ %l — VN tự thêm 2 thẻ với từ JP lấy từ TW (回動機/滿檔前進; JP nói 逆転機/前進フルギアー). Gỡ thẻ, giữ nghĩa gloss.

### 2228 — ハチロク — thuật ngữ
- JP: 「床をくまなく探していたのですが――\n運転体のセンサー類をもってしても、全くダメです」
- TW: 「地上每塊地方都找過了……但就算用駕駛體的感測器也完全找不到」
- VN cũ: 「Tôi đã lục tung cả sàn xe rồi nhưng――\ndù có dùng cảm biến của cơ thể lái cũng không thấy gì cả.」
- Sửa: 「Tôi đã lục tung cả sàn xe rồi nhưng――\ndù có dùng cảm biến của thân vận hành cũng không thấy gì cả.」
- Lý do: 運転体 → "thân vận hành" (thuật ngữ đã chốt; tiền lệ Hachiroku14 key 3983 và file 00_Common11: 運転体→"thân vận hành" 5 dòng). VN cũ "cơ thể lái" sai nghĩa (đây là THÂN vận hành, không phải cơ thể người lái).

### 2391 — 双鉄 — thẻ %l VN tự thêm (gỡ)
- JP: 「ブロア[とめべん,1]止弁開け、注水――よし！」
- TW: 「打開風管止回閥，注水——完畢！」
- VN cũ: 「Mở van ngắt \x%l風管;#00ffc040;thiết bị thổi gió%l;#;, bơm nước―― xong!」
- Sửa: 「Mở van ngắt thiết bị thổi gió, bơm nước―― xong!」
- Lý do: JP chỉ có ruby [とめべん,1], không có thẻ %l — VN tự thêm thẻ với từ JP lấy từ TW (風管; JP nói ブロア止弁). Gỡ thẻ, giữ nghĩa "thiết bị thổi gió" (ブロア = blower).

### 2475 — ハチロク — thẻ %l VN tự thêm (gỡ)
- JP: 「単純なものだけに、怠ればすぐに綻んでしまう。\n……双鉄さまは、本物の機関士になられましたね」
- TW: 「正因為是簡單的工作，所以一懈怠就會出現問題。……雙鐵少爺已經成為一名真正的司機了呢」
- VN cũ: 「Chính vì đơn giản, nên nếu lơ là sẽ lập tức xảy ra sơ suất.\n……Ngài Soutetsu, đã trở thành một \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; thực thụ rồi nhỉ.」
- Sửa: 「Chính vì đơn giản, nên nếu lơ là sẽ lập tức xảy ra sơ suất.\n……Ngài Soutetsu, đã trở thành một thợ lái đầu máy thực thụ rồi nhỉ.」
- Lý do: JP không có thẻ %l — VN tự thêm thẻ (tiền lệ file 09/11: gỡ). Đồng thời gloss sai: 機関士 "nhân viên cơ vụ" → "thợ lái đầu máy" (thuật ngữ đã chốt). Gỡ thẻ, thay bằng chữ thường đúng thuật ngữ.

### 2479 — 凪 — thẻ %l VN tự thêm (gỡ)
- JP: 「シリンダー圧――よかばい！\nバイパス弁、シリンダー排水弁、かいほー！」
- TW: 「汽缸壓——正常！打開旁路閥和汽缸排水閥！」
- VN cũ: 「Áp suất xi lanh―― ổn rồi!\n\x%l旁路閥;#00ffc040;Van bypass%l;#;, van xả xi lanh, mở!」
- Sửa: 「Áp suất xi lanh―― ổn rồi!\nVan bypass, van xả xi lanh, mở!」
- Lý do: JP không có thẻ %l — VN tự thêm thẻ với từ JP lấy từ TW (旁路閥; JP nói バイパス弁). Gỡ thẻ, giữ nghĩa "Van bypass".

### 2522 — ハチロク — thẻ %l VN tự thêm (gỡ)
- JP: 「それはもう、\nわたくしの大事な機関士さんのことですので」
- TW: 「當然，您可是我重要的司機」
- VN cũ: 「Tất nhiên rồi,\nvì ngài là \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; quan trọng của em mà.」
- Sửa: 「Tất nhiên rồi,\nvì ngài là thợ lái đầu máy quan trọng của em mà.」
- Lý do: JP không có thẻ %l — VN tự thêm thẻ (tiền lệ file 09/11: gỡ). Đồng thời gloss sai: 機関士 "nhân viên cơ vụ" → "thợ lái đầu máy" (thuật ngữ đã chốt). Gỡ thẻ, thay bằng chữ thường đúng thuật ngữ.

### 2578 — ふかみ — xưng hô/đại từ
- JP: 「少しだけお待ちください。\nすぐに、もうひとり係員を呼んで参ります」
- TW: 「請您稍等。我馬上再叫一名工作人員過來」
- VN cũ: 「Xin quý khách vui lòng chờ một chút.\nEm sẽ gọi thêm một nhân viên nữa đến ngay ạ.」
- Sửa: 「Xin quý khách vui lòng chờ một chút.\nCháu sẽ gọi thêm một nhân viên nữa đến ngay ạ.」
- Lý do: Fukami nói với bà lão ngồi xe lăn (người nghe là bà lão, bà gọi Fukami là "cháu"). VN cũ tự xưng "Em" — không nhất quán với chính file này: key 2489 "Cháu sẽ quay lại" và key 2665 "chúng cháu" đều dùng "cháu" với cùng bà lão. Sửa "Em"→"Cháu". (Các "Em" khác của Fukami với Paulette/Reina/Soutetsu vẫn đúng, không động.)

### 2648 — 鈴木 — xưng hô/đại từ
- JP: 「[みのかさ,1]蓑笠さんにもお願いします。\n忘れ物捜索、手間取ってるみたいで」
- TW: 「那也麻煩蓑笠小姐了。她們那邊尋找失物好像費了很大勁」
- VN cũ: 「Nhờ cả em Minokasa nữa nhé.\nCó vẻ như việc tìm đồ thất lạc đang gặp khó khăn.」
- Sửa: 「Nhờ cả ông Minokasa nữa nhé.\nCó vẻ như việc tìm đồ thất lạc đang gặp khó khăn.」
- Lý do: Đối tượng là ông lão Minokasa (蓑笠老人 — bằng chứng file 09: Soutetsu xưng "tôi/cháu" và gọi "Ông" với Minokasa, key 2464/2760; "Phu nhân Minokasa" theo TW đã bị bác ở file 09 key 2326). VN cũ "em Minokasa" đi theo TW 蓑笠小姐 (TW nữ hóa Minokasa — cùng lỗi TW như ở 2326; JP chỉ nói 蓑笠さん trung tính). Sửa "em"→"ông".

### 2960 — monologue — thuật ngữ
- JP: 機関士席にかけたまんまで、運転体のハチロクば、\nだっこして、膝の上に座らすみたいに落ち着ける。
- TW: 咱坐在駕駛座上，把駕駛體的八六抱起來放在腿上。
- VN cũ: Tớ vẫn ngồi trên ghế lái tàu, bế cơ thể vận hành của Hachiroku lên\nvà đặt ngồi yên vị trên đùi tớ.
- Sửa: Tớ vẫn ngồi trên ghế lái tàu, bế thân vận hành của Hachiroku lên\nvà đặt ngồi yên vị trên đùi tớ.
- Lý do: 運転体 → "thân vận hành" (như key 2228; tiền lệ Hachiroku14 key 3983). VN cũ "cơ thể vận hành" vẫn sai thuật ngữ đã chốt ("thân", không phải "cơ thể").

### 2989 — monologue — thẻ %l VN tự thêm (gỡ)
- JP: 助士のときとは全然違う、左運転台から見る景色。\nばってん、なんも言われんでも自然とできる。
- TW: 在左駕駛台看到的景色與司爐完全不同。但就算沒受到任何指令，咱也自然而然能做到了。
- VN cũ: Cảnh vật nhìn từ buồng lái bên trái hoàn toàn khác so với lúc làm \x%l司爐;#00ffc040;phụ lái tàu%l;#;.\nNhưng mà, không cần ai nhắc nhở mình vẫn tự nhiên làm được.
- Sửa: Cảnh vật nhìn từ buồng lái bên trái hoàn toàn khác so với lúc làm phụ lái tàu.\nNhưng mà, không cần ai nhắc nhở mình vẫn tự nhiên làm được.
- Lý do: JP không có thẻ %l — VN tự thêm thẻ với từ JP lấy từ TW (司爐; JP nói 助士). Gỡ thẻ, giữ nghĩa "phụ lái tàu" (khớp key 3243 "hồi làm phụ lái" cho 助士のとき).

### 3167 — monologue — thuật ngữ
- JP: おばちゃん、迎えの人ば来ると思うてホームで待ってて。そん間に、\x%lキハ07s;#00ffc040;キハ07s%l;#;は機関庫にはいっちゃって。
- TW: 老婆婆以為會有人來接她，就一直在站台等。等著等著，\x%lキハ07s;#00ffc040;Ｋｉｈａ０７Ｓ%l;#;就進機車庫裡去了。
- VN cũ: Bà lão nghĩ là người đến đón sẽ tới nên cứ đợi ở sân ga. Trong lúc đó, \x%lキハ07s;#00ffc040;Kiha 07S%l;#; đã đi vào xưởng đầu máy mất rồi.
- Sửa: Bà lão nghĩ là người đến đón sẽ tới nên cứ đợi ở sân ga. Trong lúc đó, \x%lキハ07s;#00ffc040;KiHa 07S%l;#; đã đi vào xưởng đầu máy mất rồi.
- Lý do: Thuật ngữ đã chốt: KiHa (chính tả JR). VN cũ "Kiha 07S" trong gloss của thẻ %l — sửa chính tả, giữ nguyên thẻ (JP có thẻ này).

### 3264 — monologue — SFX
- JP: （しゅっ、しゅっ、しゅっ、しゅっ）
- TW: （咻、咻、咻、咻）
- VN cũ: （Xình xịch, xình xịch, xình xịch, xình xịch）
- Sửa: （Xoẹt, xoẹt, xoẹt, xoẹt）
- Lý do: JP （しゅっ×4) là tiếng xẻng xúc than (cảnh xúc than; TW 咻 = tiếng vút). VN cũ "Xình xịch" là tiếng tàu chạy — sai hẳn âm thanh của hành động. Sửa "Xoẹt" (tiếng xẻng vút).

### 3276 — monologue — thuật ngữ
- JP: 今は、8620も\x%lキハ07s;#00ffc040;キハ07s%l;#;も機関庫。\n留置線にも出とらんけん、他ん列車がくるはずもなか。
- TW: ８６２０和\x%lキハ07s;#00ffc040;Ｋｉｈａ０７Ｓ%l;#;現在都在機車庫裡。沒從存車線裡出來，其他列車也不可能過來。
- VN cũ: Hiện tại, cả 8620 và \x%lキハ07s;#00ffc040;Kiha 07S%l;#; đều đang ở trong xưởng đầu máy.\nCũng không ra ngoài đường lưu đỗ, nên chắc chắn không có chuyến tàu nào khác tới đâu.
- Sửa: Hiện tại, cả 8620 và \x%lキハ07s;#00ffc040;KiHa 07S%l;#; đều đang ở trong xưởng đầu máy.\nCũng không ra ngoài đường lưu đỗ, nên chắc chắn không có chuyến tàu nào khác tới đâu.
- Lý do: Như key 3167: "Kiha 07S" → "KiHa 07S" trong gloss thẻ %l (JP có thẻ này).

## §3. Sweep gasp kiểm chứng

- Sweep có 3 mục cho file này: 2058 (lost-gasp-trailing) — nhận, sửa thành "Phù~~Ư" (JP 「ふぃ～～っ」); 2142 (already-rendered: JP 「っ！」→ VN "A!") — giữ nguyên, đã diễn gasp bằng câu cảm thán; 2160 (needs-file-audit: JP 「っ！！？」→ VN "Ế!!?") — giữ nguyên: "Ế" đã diễn tiếng kêu giật mình có dấu hỏi, tương đương tiền lệ 2142, không phải dòng lệch (VN chỉ là thán từ, không phải câu đầy đủ ở dòng khác như sweep lo ngại).
- Sweep bỏ sót 3 gasp/SFX trong file này (đã bắt ở §2): 1970 (ふぅ thiếu nguyên âm), 2068 (はうっ thừa nguyên âm), 3264 không phải gasp mà là SFX xúc than bị dịch sai.

## §4. Lượt soát 2 (bắt buộc, đọc lại toàn bộ fix theo JP)

- Tổng 18 / đã kiểm chứng lại 18 / bỏ 0 / sửa 0.
- Kiểm tra cơ học: mỗi fix chỉ đổi đúng chỗ nhắm tới (assert count==1 cho từng chuỗi thay thế); 0 fix có ký tự xuống dòng thật; 0 fix làm mất thẻ JP có sẵn; khối TOML 18 khóa, 0 sai lệch giá trị so với JSON.

## §5. Khối TOML (đã parse-kiểm chứng: 18 khóa, 0 sai lệch)

```toml
[script]
"1970" = "「Đội mũ lệch ra sau nên tóc tai đẫm mồ hôi bù xù hết cả lên rồi này……\\nPhùù. Bắt đầu từ việc chỉnh trang lại vẻ ngoài trước nhé.」"
"2039" = "「Hya.」"
"2058" = "「Phù~~Ư」"
"2068" = "「Tớ…… hau——em.\\nHoàn toàn chưa phải là người lớn——desu.」"
"2214" = "「Cần đảo chiều, tầm trung!! Xong!」"
"2215" = "「Cần đảo chiều! Cài hết số tiến!!!」"
"2228" = "「Tôi đã lục tung cả sàn xe rồi nhưng――\\ndù có dùng cảm biến của thân vận hành cũng không thấy gì cả.」"
"2391" = "「Mở van ngắt thiết bị thổi gió, bơm nước―― xong!」"
"2475" = "「Chính vì đơn giản, nên nếu lơ là sẽ lập tức xảy ra sơ suất.\\n……Ngài Soutetsu, đã trở thành một thợ lái đầu máy thực thụ rồi nhỉ.」"
"2479" = "「Áp suất xi lanh―― ổn rồi!\\nVan bypass, van xả xi lanh, mở!」"
"2522" = "「Tất nhiên rồi,\\nvì ngài là thợ lái đầu máy quan trọng của em mà.」"
"2578" = "「Xin quý khách vui lòng chờ một chút.\\nCháu sẽ gọi thêm một nhân viên nữa đến ngay ạ.」"
"2648" = "「Nhờ cả ông Minokasa nữa nhé.\\nCó vẻ như việc tìm đồ thất lạc đang gặp khó khăn.」"
"2960" = "Tớ vẫn ngồi trên ghế lái tàu, bế thân vận hành của Hachiroku lên\\nvà đặt ngồi yên vị trên đùi tớ."
"2989" = "Cảnh vật nhìn từ buồng lái bên trái hoàn toàn khác so với lúc làm phụ lái tàu.\\nNhưng mà, không cần ai nhắc nhở mình vẫn tự nhiên làm được."
"3167" = "Bà lão nghĩ là người đến đón sẽ tới nên cứ đợi ở sân ga. Trong lúc đó, \\x%lキハ07s;#00ffc040;KiHa 07S%l;#; đã đi vào xưởng đầu máy mất rồi."
"3264" = "（Xoẹt, xoẹt, xoẹt, xoẹt）"
"3276" = "Hiện tại, cả 8620 và \\x%lキハ07s;#00ffc040;KiHa 07S%l;#; đều đang ở trong xưởng đầu máy.\\nCũng không ra ngoài đường lưu đỗ, nên chắc chắn không có chuyến tàu nào khác tới đâu."
```

## §6. Chờ Hieu (không tự quyết)

- Đợt thống nhất (không tính sai): "Ohito"/"Ohimitera" 4 dòng (2483 "Đường sắt Ohito", 3222 "ga Ohimitera", 2367 "Về tới Ohimitera", 2266 "Người phụ nữ tuyệt vời nhất Ohimitera"); "Yui" (湯医) 2 dòng (1979, 2972) → "Yunoi" chờ đợt thống nhất.
- Key 3161: Nagi nhắc じーちゃん → VN "ông nội". Toàn dự án đều dùng "ông nội"; câu hỏi "ông nội hay ông ngoại" đang chờ Hieu chốt (từ file 08c, về Seki/Midori) — dòng này giữ nguyên, ghi chú để Hieu xem có áp dụng chung không.
- Key 2679 vs 1981: Nagi gọi Hachiroku "cô" ("N... nhờ cô nha.") ở 2679 nhưng "chị Hachiroku" ở 1981. Không tính sai (ngữ cảnh 2679 là nhờ "cô giáo Hachiroku" dạy dỗ, 2667) — Hieu xem có cần thống nhất "chị Hachiroku" không.
- Key 3268/3269: SFX （ずぼっ！）→"(Sột!)" và （ずるっ）→"(Roạt)" — giữ nguyên (phán đoán SFX theo ngữ cảnh; không chắc chắn đủ để sửa).
- Key 2022: Soutetsu gọi Hachiroku là "em" ("Gì vậy Hachiroku, em biết sao?") — giữ nguyên: quy tắc chỉ chốt đại từ TỰ xưng của Soutetsu ("tôi" với Hachiroku), không chốt cách gọi; Hachiroku mang hình dáng bé gái nên "em" hợp lý.

## Kết bài

File 凪ふかみ05_凪の開眼！？ đã audit xong toàn bộ 478 dòng: 18 dòng sai (3,8%) — 2 đại từ, 4 thuật ngữ, 7 thẻ %l VN tự thêm (gỡ theo tiền lệ file 09/11), 1 gasp từ sweep, 4 SFX. Không lệch dòng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 18 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 18/18, 0 bỏ, 0 sửa. Chờ Hieu: đợt thống nhất Ohito/Yui (6 dòng), câu hỏi "ông nội hay ông ngoại" (3161), và cách gọi Nagi→Hachiroku "cô" hay "chị" (2679/1981).
