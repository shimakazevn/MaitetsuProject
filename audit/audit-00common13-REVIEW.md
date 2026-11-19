# Audit 00_Common file 13 — 共通13_勾配図.txt.toml

**Ngày kiểm toán:** 20/11/2026
**Tệp TOML:** `00_Common/共通13_勾配図.txt.toml` — md5 `db85026889f356064969c0e2745af096`, 96.458 byte, BOM, CRLF (961 CRLF, 0 LF-only), `[selections]` rỗng, **không có bản sao trùng** (kiểm tra md5 toàn bộ 227 tệp TOML).
**Nguồn CSV:** "Trang tính 3" — bộ hàng duy nhất `00_Common` (không có bẫy dual-set ở file này), 462 hàng `[script]`.
**Kết quả: 45/462 dòng sai (9,7%), 0 dòng chưa chắc chắn, 0 dòng lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo file.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| Thuật ngữ (terminology) | 12 |
| Đại từ xưng hô (pronoun) | 20 |
| Tiếng thở/gasp (gasp) | 7 |
| SFX (tiếng thở/cảm thán) | 5 |
| Sai nghĩa (meaning) | 1 |
| **Tổng** | **45** |

**Theo loại dòng:** thoại 40/276 sai (14,5%), độc thoại 5/186 sai (2,7%).
**Theo nhân vật:** 双鉄 (Soutetsu) 25, ハチロク (Hachiroku) 6, 凪 (Nagi) 5, monologue 5, ふかみ (Fukami) 4.

Nhóm thuật ngữ (12) chia nhỏ: 御一夜→Ohitoyo 3 dòng (2076, 2267, 3237 — toàn bộ "Ohimitera" trong file); 湯医/湯医線→Yunoi 3 dòng (2119, 2436, 2481 — toàn bộ "Yui" trong file); レール種別→"loại ray" 2 dòng (1550, 2538 — gloss thẻ %l); 運転体→"thân vận hành" 2 dòng (1878, 2948 — 2948 kèm khôi phục thẻ %l bị rớt); 宮司→"đền chủ" 2 dòng (2707, 2941 — biến thể "thầy Akai", như file 12 key 3038). Nhóm đại từ (20): Soutetsu gọi Hachiroku "cô"→"em" 11 dòng (1537, 1568, 1892 [×2], 1925, 2126, 2215, 2271, 2335, 2380, 2498, 2514 [×2]); Soutetsu gọi Fukami "cô"→"em" 2 dòng (1904, 1906 [×2]); Soutetsu tự xưng "anh"→"tôi" với Hachiroku 2 dòng (2218, 2333); Nagi gọi Fukami "cậu/tớ"→"chị/em" 3 dòng (2151, 2153, 2156 — theo quy tắc file 10: Nagi gọi Fukami là "chị"); Hachiroku gọi Soutetsu "cô"→"ngài" 1 dòng (2329 — cô ấy chấm điểm cho Soutetsu, gọi anh là "ngài Soutetsu" ở 2390); Hachiroku gọi Hibiki "cô ấy"→"em ấy" 1 dòng (2512 — Hibiki là ứng cử viên 機関助士). Nhóm gasp (7): toàn bộ từ sweep, áp nguyên giá trị sweep đã kiểm chứng (1874, 1927, 2028, 2533, 2534, 2535, 2810). Nhóm SFX (5): 2023 ひあっ→"Hia" (tiền lệ lr_h1 1005); 2033 ふぁ→"phà"; 2038 ふぇ→"Phuêêêêê!?"; 2052 ふうむ→"Hừừm." (công thức độ dài nguyên âm); 2432 ふぇ→"phuê". Sai nghĩa (1): 2349 のぼせてアテられた "say sóng"→"choáng váng" (TW 泡暈 xác nhận — say sóng là seasickness, sai hoàn toàn).

File này sạch hơn file 11 (17,8%) và ngang file 10 (9,3%) — lỗi tập trung ở đại từ + thuật ngữ chưa cập nhật theo các quyết định 19–20/11, không phải lỗi cấu trúc: 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo. Toàn bộ 45 lỗi đều sửa được tại chỗ, không cần dịch lại.

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục. TOML md5 `db85026889f356064969c0e2745af096`, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng trong 227 tệp.
- **CSV vs TOML:** VN khớp tuyệt đối 188 hàng; khớp sau khi gộp ký tự xuống dòng thành khoảng trắng 271 hàng; **3 khác biệt (2038, 2271, 2965) — đều là hiện tượng gộp `\n` thành khoảng trắng trong TOML, KHÔNG phải lỗi dịch**. CSV3 là bản chuẩn cho fix list.
- **Sweep っ (gasp):** sweep CÓ liệt kê file này — 8 mục trong sweep-raw-gasp-wrong.json: 7 fix (1874, 1927, 2028, 2533, 2534, 2535, 2810) + 1 already-rendered (2057, う～～っ → "Ư~~", đã kiểm chứng đúng). Cả 7 giá trị fix của sweep đã kiểm chứng đúng với JP và được áp nguyên. Quét っ hệ thống trên toàn bộ 180 dòng JP chứa っ (không chỉ dựa vào sweep) không tìm thêm gasp っ trần nào bị mất; 2038 (ふぇぇぇええっ) là っ ngắt giọng nhấn mạnh trên SFX đã diễn, không phải gasp riêng — sweep không gắn cờ là đúng.
- **Thẻ %l:** JP có 69 thẻ, VN có 68 thẻ — lệch đúng 1 thẻ, đã xác định được dòng: key 2948 (JP 1 thẻ, VN 0 thẻ — bản Việt làm rớt cả thẻ khi dịch sai thuật ngữ). Fix 2948 khôi phục thẻ với gloss "thân vận hành". Không có thẻ %l đóng sai định dạng nào trong file (kiểm tra `%l;#` không có `;` cuối: 0 dòng). (Con số 57/56 ghi trong ghi chú đầu file là đếm heuristic sơ bộ; đếm lại chính xác bằng regex `\x%l` trên toàn bộ CSV là 69/68 — lệch vẫn là 1 thẻ, cùng một dòng 2948.)
- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng), không có VN mồ côi (orphan), không có key trùng. Chỉ 1 hàng VN == TW là key 1557 (JP/TW/VN đều là 「…………」 — dấu lặng, hợp lệ, không phải chưa dịch; cùng mẫu file 11 key 1816).
- **Kiểm tra nhiễm chéo:** đối chiếu 45 giá trị VN cũ trong fix list qua chỉ mục VN toàn dự án — 1 lần trùng bề ngoài duy nhất (2959 với 日々姫05 3069) nhưng JP hai dòng gần như giống hệt nhau (わかる。僕も同じであるから / わかる。僕もおんなじだから — cùng một câu, biến thể phương ngữ), là dòng lặp lại hợp lệ, KHÔNG phải nhiễm chéo. Toàn bộ 462 VN đều khớp đúng JP của chính dòng mình.
- **Thứ tự dòng:** key số trong file này KHÔNG phải thứ tự truyện — các cảnh xen kẽ nhau theo key (cảnh tắm Tororyu-yu, cảnh đo độ dốc, mạch 考えすぎ 1869→1906→2200→2223 nằm lẫn lộn). Vì vậy địa chỉ người nghe được xác định từ nội dung dòng + mạch hội thoại (ai nói trước/sau về cùng chủ đề, TW dùng đại từ số nhiều/số ít), KHÔNG dùng key kề nhau theo thứ tự số. Bằng chứng: 1898 (xem §6 — TW 你們 số nhiều chứng minh người nghe là các cô gái, không phải Hachiroku dù Hachiroku nói ngay trước đó ở 1895).

## 3. Các lỗi đã sửa (45 dòng)

### 1537 — 双鉄 — pronoun

**JP:** 「\x%l保線;#00ffc040;[ほせん,1]保線%l;#;だ。鉄道に\x%l保線;#00ffc040;保線%l;#;は欠かせぬと」

**TW:** 「\x%l保線;#00ffc040;巡線%l;#;啊。\x%l保線;#00ffc040;巡線%l;#;就是鐵路的生命線」

**VN cũ:** 「\x%l保線;#00ffc040;Bảo trì đường ray%l;#; đấy. Cô bảo đường sắt thì không thể thiếu \x%l保線;#00ffc040;bảo trì đường ray%l;#; mà.」

**Fix:** 「\x%l保線;#00ffc040;Bảo trì đường ray%l;#; đấy. Em bảo đường sắt thì không thể thiếu \x%l保線;#00ffc040;bảo trì đường ray%l;#; mà.」

Soutetsu nói với Hachiroku (JP お前; cô ấy vừa nói về 保線). Xưng hô đúng là "em", không phải "cô".

### 1550 — ハチロク — terminology

**JP:** 「\x%l勾配千分率;#00ffc040;勾配千分率%l;#;1.6。\x%l施工基面高;#00ffc040;施工基面高%l;#;[イチニイサンテンマルキュウ,5]123.09」。⏎\x%l勾配距離;#00ffc040;勾配距離%l;#;が、149.23。\x%lレール種別;#00ffc040;レール種別%l;#;は[さんじゅっ,1]30キロままです」

**TW:** 「\x%l勾配千分率;#00ffc040;坡度千分率%l;#;１.６。\x%l施工基面高;#00ffc040;施工基面高%l;#;１２３.０９。\x%l勾配距離;#00ffc040;坡度距離%l;#;是１４９.２３。\x%lレール種別;#00ffc040;鐵軌類型%l;#;是３０公斤不變」

**VN cũ:** 「\x%l勾配千分率;#00ffc040;Độ dốc phần nghìn%l;#; 1.6. \x%l施工基面高;#00ffc040;Cao độ mặt nền đường sắt%l;#; 123.09.⏎\x%l勾配距離;#00ffc040;Chiều dài đoạn dốc%l;#; là 149.23. \x%lレール種別;#00ffc040;Loại đường sắt%l;#; vẫn là 30 ký.」

**Fix:** 「\x%l勾配千分率;#00ffc040;Độ dốc phần nghìn%l;#; 1.6. \x%l施工基面高;#00ffc040;Cao độ mặt nền đường sắt%l;#; 123.09. \x%l勾配距離;#00ffc040;Chiều dài đoạn dốc%l;#; là 149.23. \x%lレール種別;#00ffc040;Loại ray%l;#; vẫn là 30 ký.」

JP レール種別, TW 鐵軌類型 = loại ray (thanh ray 30 ký/m). "Loại đường sắt" là loại hình đường sắt — sai nghĩa.

### 1568 — 双鉄 — pronoun

**JP:** 「……お前は、物で、道具なのだな」

**TW:** 「……你真的是物品，為人所用的工具啊」

**VN cũ:** 「……Cô quả thực là một đồ vật, một công cụ nhỉ.」

**Fix:** 「……Em quả thực là một đồ vật, một công cụ nhỉ.」

Soutetsu nói với Hachiroku (JP お前). "Cô"→"em".

### 1874 — ハチロク — gasp

**JP:** 「ダメです！　完全に幹で塞がれていま――っ！！？」

**TW:** 「不行！完全被樹幹堵住了！！？」

**VN cũ:** 「Không xong rồi! Bị thân cây chắn ngang hoàn toàn rồi——!!?」

**Fix:** 「Không xong rồi! Bị thân cây chắn ngang hoàn toàn rồi——Ư!!?」

Sweep っ-gasp: JP 「…塞がれていま――っ！！？」. Áp nguyên giá trị sweep, đã kiểm chứng đúng với JP.

### 1878 — 双鉄 — terminology

**JP:** 「しかし、運転[ボディ]体のセンサーというのは大した物だな。⏎器具なしで勾配を測定できるとは」

**TW:** 「不過，沒想到駕駛體的感測器這麼厲害，沒有工具也能測量坡度」

**VN cũ:** 「Nhưng mà, cảm biến của cơ thể lái tuyệt thật đấy.⏎Không cần dụng cụ mà vẫn đo được độ dốc cơ mà.」

**Fix:** 「Nhưng mà, cảm biến của thân vận hành tuyệt thật đấy. Không cần dụng cụ mà vẫn đo được độ dốc cơ mà.」

JP 運転[ボディ]体 = 運転ボディ. Quyết định: 運転ボディ = "thân vận hành" (không phải "cơ thể lái").

### 1892 — 双鉄 — pronoun

**JP:** 「しかしハチロク、僕は僕以外の何者でもない。⏎お前の代わりに、お前の答えを考えてはやれんぞ？」

**TW:** 「但是八六，我只是我自己而已。我是沒有辦法替你找到你自己的答案的哦？」

**VN cũ:** 「Nhưng Hachiroku này, tôi không phải ai khác ngoài chính tôi.⏎Tôi không thể suy nghĩ thay cô để tìm ra câu trả lời cho cô được đâu?」

**Fix:** 「Nhưng Hachiroku này, tôi không phải ai khác ngoài chính tôi. Tôi không thể suy nghĩ thay em để tìm ra câu trả lời cho em được đâu?」

Soutetsu nói với Hachiroku (JP お前 ×2). "Cô"→"em" ×2.

### 1904 — 双鉄 — pronoun

**JP:** 「ショックではなかったのか？」

**TW:** 「你沒有覺得受到打擊嗎？」

**VN cũ:** 「Cô không thấy sốc sao?」

**Fix:** 「Em không thấy sốc sao?」

1903 Soutetsu gọi thẳng tên Fukami (しっかりしろ、ふかみ). Dòng này vẫn nói với Fukami → "em".

### 1906 — 双鉄 — pronoun

**JP:** 「お前がコントロール出来ない部分がおそらく、⏎勝手に考えてしまうがゆえの、“考えすぎ”だ」

**TW:** 「你無法控制的部分恐怕就是因為你不自覺地東想西想引起的，所以說“想太多”」

**VN cũ:** 「Những phần mà cô không thể kiểm soát có lẽ là,⏎do cô tự ý suy nghĩ, nên mới thành ra "suy nghĩ quá nhiều".」

**Fix:** 「Những phần mà em không thể kiểm soát có lẽ là, do em tự ý suy nghĩ, nên mới thành ra "suy nghĩ quá nhiều".」

Tiếp mạch 1903–1904, vẫn nói với Fukami về chứng "suy nghĩ quá nhiều" của cô ấy. "Cô"→"em" ×2.

### 1925 — 双鉄 — pronoun

**JP:** 「なぁ、ハチロク。お前がいっていたとおりだな」

**TW:** 「八六。正如你所說的那樣」

**VN cũ:** 「Này, Hachiroku. Đúng như những gì cô đã nói nhỉ.」

**Fix:** 「Này, Hachiroku. Đúng như những gì em đã nói nhỉ.」

Soutetsu nói với Hachiroku (JP なぁ、ハチロク。お前). "Cô"→"em".

### 1927 — 双鉄 — gasp

**JP:** 「ハチロクから先に――っ！」⏎「双鉄様からお先に――っ！」

**TW:** 「八六先說！」⏎「雙鐵少爺先說！」

**VN cũ:** 「Hachiroku nói trước đi——!」⏎「Ngài Soutetsu nói trước đi ạ——!」

**Fix:** 「Hachiroku nói trước đi——Ư!」⏎「Ngài Soutetsu nói trước đi ạ——Ư!」

Sweep っ-gasp: JP hai vế đều kết thúc ――っ！. Áp nguyên giá trị sweep, đã kiểm chứng đúng với JP.

### 2023 — 凪 — sfx

**JP:** 「ひあっ！？　ひあああっ！？　エラいことばいっ！！」

**TW:** 「呀！？哎呀呀！？大事不好咧！！」

**VN cũ:** 「Hya!? Hyaaa!? Chuyện lớn rồi!!」

**Fix:** 「Hia!? Hiaaa!? Chuyện lớn rồi!!」

JP ひあっ/ひあああっ — không phải ひゃ. Tiền lệ lr_h1 1005: ひあっ → "Hia".

### 2028 — 双鉄 — gasp

**JP:** 「ふ～～っ」

**TW:** 「呼～～」

**VN cũ:** 「Phù~~」

**Fix:** 「Phù~~Ư」

Sweep っ-gasp: JP 「ふ～～っ」. Áp nguyên giá trị sweep, đã kiểm chứng đúng với JP.

### 2033 — ふかみ — sfx

**JP:** 「は……ふぁ……やっぱり、ふたりって、そういう～」

**TW:** 「哈……呼……果然，他們兩位是這種～」

**VN cũ:** 「Hả…… hả…… quả nhiên, hai người, là mối quan hệ như thế~」

**Fix:** 「Hả…… phà…… quả nhiên, hai người, là mối quan hệ như thế~」

JP は……ふぁ…… — tiếng thở thứ hai là ふぁ. Quy tắc fa/fu: ふぁ → "phà".

### 2038 — ふかみ — sfx

**JP:** 「ふぇぇぇええっ！？　だいじょうぶっ！　⏎大丈夫っ！　です」

**TW:** 「哎哎哎！？沒事！沒事的！嗯」

**VN cũ:** 「Êêêêê!? Không sao đâu! ⏎Không sao đâu! Ạ.」

**Fix:** 「Phuêêêêê!? Không sao đâu! Không sao đâu! Ạ.」

JP ふぇぇぇええっ (5 ký tự kéo dài sau ふぇ). Quy tắc fa/fu: ふぇ → "phuê"; giữ 5 ê kéo dài. っ cuối là ngắt giọng nhấn mạnh trên SFX đã diễn, không phải gasp riêng — sweep không gắn cờ dòng này.

### 2052 — 双鉄 — sfx

**JP:** 「ふうむ」

**TW:** 「唔」

**VN cũ:** 「Hừm.」

**Fix:** 「Hừừm.」

JP ふうむ (1 う). Công thức độ dài nguyên âm: số nguyên âm VN = 1 + số う/ぅ = 2 → "Hừừm.".

### 2076 — 凪 — terminology

**JP:** 「あ、じいちゃん？　あのね、今ね、御一夜の駅でね」

**TW:** 「喂，爺爺？你聽咱說咧，咱現在在御一夜站」

**VN cũ:** 「A, ông ạ? Chuyện là, bây giờ cháu đang ở ga Ohimitera.」

**Fix:** 「A, ông ạ? Chuyện là, bây giờ cháu đang ở ga Ohitoyo.」

JP 御一夜. Quyết định: 御一夜 = "Ohitoyo" (không phải "Ohimitera").

### 2119 — ハチロク — terminology

**JP:** 「川沿いが基本となっているためか、⏎本当になだらかな路線ですね、湯医線は」

**TW:** 「大概是因為基本上都沿河而建吧，湯醫線真的是一段很平穩的線路」

**VN cũ:** 「Có lẽ vì cơ bản là chạy dọc theo con sông,⏎nên tuyến Yui quả thực là một tuyến đường rất thoai thoải nhỉ.」

**Fix:** 「Có lẽ vì cơ bản là chạy dọc theo con sông, nên tuyến Yunoi quả thực là một tuyến đường rất thoai thoải nhỉ.」

JP 湯医線. Quyết định: 湯医/湯医線 = "Yunoi".

### 2126 — 双鉄 — pronoun

**JP:** 「よかろう。ならばハチロク――⏎まず手始めから頼めるか？」

**TW:** 「好吧。那八六——一能拜託你先講講基本方式嗎？」

**VN cũ:** 「Được thôi. Vậy thì Hachiroku——⏎Cô có thể giúp hướng dẫn từ bước đầu tiên được không?」

**Fix:** 「Được thôi. Vậy thì Hachiroku—— Em có thể giúp hướng dẫn từ bước đầu tiên được không?」

Soutetsu nói với Hachiroku (JP ならばハチロク). "Cô"→"em".

### 2151 — 凪 — pronoun

**JP:** 「ふかみちゃん……ダメばい、⏎汗と黒いの、うつっちゃうばい」

**TW:** 「小深……別碰咱，會沾上汗和黑粉的咧……」

**VN cũ:** 「Fukami…… không được đâu,⏎mồ hôi với thứ đen đen này, dính sang cậu mất.」

**Fix:** 「Chị Fukami…… không được đâu, mồ hôi với thứ đen đen này, dính sang chị mất.」

Nagi nói với Fukami (JP ふかみちゃん). Quy tắc file 10: Nagi gọi Fukami là "chị" (Fukami lớn tuổi hơn, gọi Nagi là "bé Nagi"). "Fukami… cậu"→"Chị Fukami… chị".

### 2153 — 凪 — pronoun

**JP:** 「ふかみちゃん、背中流してあげるばいっ！」

**TW:** 「小深，咱來給你沖背後咧！」

**VN cũ:** 「Fukami, để tớ kỳ lưng cho nhé!」

**Fix:** 「Chị Fukami, để em kỳ lưng cho nhé!」

Nagi nói với Fukami (JP ふかみちゃん). "Fukami, để tớ"→"Chị Fukami, để em".

### 2156 — 凪 — pronoun

**JP:** 「ふかみちゃん、顔真っ赤ばい！　のぼせたと？」

**TW:** 「小深，臉好紅！泡暈咧？」

**VN cũ:** 「Fukami, mặt cậu đỏ bừng kìa! Bị ngâm nóng quá rồi hả?」

**Fix:** 「Chị Fukami, mặt chị đỏ bừng kìa! Bị ngâm nóng quá rồi hả?」

Nagi nói với Fukami (JP ふかみちゃん). "Fukami, mặt cậu"→"Chị Fukami, mặt chị".

### 2215 — 双鉄 — pronoun

**JP:** 「了解した！　お前はれいなを起こし続けろっ！」

**TW:** 「我知道了！你繼續試著叫醒玲奈！」

**VN cũ:** 「Rõ rồi! Cô hãy tiếp tục đánh thức Reina đi!」

**Fix:** 「Rõ rồi! Em hãy tiếp tục đánh thức Reina đi!」

Soutetsu nói với Hachiroku (JP お前はれいなを起こし続けろ). "Cô"→"em".

### 2218 — 双鉄 — pronoun

**JP:** 「もう少し、近くで見ていいか？」

**TW:** 「我能湊近些看嗎？」

**VN cũ:** 「Anh đến gần xem một chút được không?」

**Fix:** 「Tôi đến gần xem một chút được không?」

Soutetsu nói với Hachiroku (cảnh 考えすぎ; các dòng quanh đó đều là Hachiroku; 2219 cùng mạch dùng "tôi"). Tự xưng đúng là "tôi", không phải "anh".

### 2267 — ハチロク — terminology

**JP:** 「そうですね、ここから御一夜に戻る線路は⏎\x%lキハ07;#00ffc040;キハ07%l;#;の中でも確認させていただきましたが――」

**TW:** 「是啊，雖說從這裡回御一夜的線路上次在\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;裡已經確認過了——」

**VN cũ:** 「Vâng ạ, tuyến đường từ đây trở về Ohimitera⏎em cũng đã xác nhận lúc ở trong \x%lキハ07;#00ffc040;KiHa 07%l;#; rồi, nhưng mà——」

**Fix:** 「Vâng ạ, tuyến đường từ đây trở về Ohitoyo em cũng đã xác nhận lúc ở trong \x%lキハ07;#00ffc040;KiHa 07%l;#; rồi, nhưng mà——」

JP 御一夜. Quyết định: 御一夜 = "Ohitoyo".

### 2271 — 双鉄 — pronoun

**JP:** 「パワーがある、ということか？　⏎細かな部分までは気にせず踏破できるだけの」

**TW:** 「是因為有足夠的動力嗎？可以做到無視輕微的坡度變化」

**VN cũ:** 「Ý cô là sức mạnh sao? ⏎Đủ sức vượt qua mà không cần bận tâm đến những chi tiết nhỏ nhặt ấy.」

**Fix:** 「Ý em là sức mạnh sao? Đủ sức vượt qua mà không cần bận tâm đến những chi tiết nhỏ nhặt ấy.」

Soutetsu nói với Hachiroku (tiếp mạch 2267–2270, Hachiroku giải thích về động cơ). "Cô"→"em".

### 2329 — ハチロク — pronoun

**JP:** 「さっきよりは遥かに良くなっています。⏎１００点満点中、２２点は差し上げられます」

**TW:** 「比剛才好很多了。百分制打２２分吧」

**VN cũ:** 「Đã tốt hơn lúc nãy rất nhiều rồi ạ.⏎Trên thang điểm 100, em có thể cho cô 22 điểm.」

**Fix:** 「Đã tốt hơn lúc nãy rất nhiều rồi ạ. Trên thang điểm 100, em có thể cho ngài 22 điểm.」

Hachiroku chấm điểm cho Soutetsu (2390: "Đạt yêu cầu rồi ạ, ngài Soutetsu"). Cô ấy gọi Soutetsu là "ngài", không phải "cô". "cho cô 22 điểm"→"cho ngài 22 điểm".

### 2333 — 双鉄 — pronoun

**JP:** 「望むところだ。⏎厳しい指導は、よりよい成長に繋がろうから」

**TW:** 「求之不得。嚴厲的指導才能讓人成長嘛」

**VN cũ:** 「Anh đang mong thế đây.⏎Sự chỉ bảo nghiêm khắc sẽ dẫn đến sự trưởng thành tốt hơn mà.」

**Fix:** 「Tôi đang mong thế đây. Sự chỉ bảo nghiêm khắc sẽ dẫn đến sự trưởng thành tốt hơn mà.」

Soutetsu đáp lại Hachiroku (2260: cô ấy dọa sẽ "nghiêm khắc la mắng ngài Soutetsu"). Tự xưng đúng là "tôi", không phải "anh".

### 2335 — 双鉄 — pronoun

**JP:** 「そうだ。知性や……理性すら本当は制御しがたいものだ。⏎僕にとっても――恐らくは、ハチロク、お前にとっても」

**TW:** 「沒錯。智慧……還有理性，真的很難控制。我也是——八六，恐怕你也是」

**VN cũ:** 「Đúng vậy. Trí tuệ hay…… ngay cả lý trí thực chất cũng rất khó kiểm soát.⏎Đối với tôi——và có lẽ, đối với cả cô nữa, Hachiroku.」

**Fix:** 「Đúng vậy. Trí tuệ hay…… ngay cả lý trí thực chất cũng rất khó kiểm soát. Đối với tôi——và có lẽ, đối với cả em nữa, Hachiroku.」

Soutetsu nói với Hachiroku (JP ハチロク、お前にとっても). "Cô"→"em".

### 2349 — ふかみ — meaning

**JP:** 「のぼせた……う～～っ、かなり、⏎のぼせて、アテられたかも～」

**TW:** 「泡暈……嗚～～大概是泡太久了～」

**VN cũ:** 「Ngâm nóng quá…… ư~~, chắc là,⏎bị ngâm nóng quá nên say sóng luôn rồi~」

**Fix:** 「Ngâm nóng quá…… ư~~, chắc là, bị ngâm nóng quá nên choáng váng luôn rồi~」

JP のぼせてアテられた = choáng váng vì ngâm nước nóng quá lâu; TW 泡暈 xác nhận. "Say sóng" (seasickness) là sai nghĩa hoàn toàn.

### 2380 — 双鉄 — pronoun

**JP:** 「もちろん、僕も付き合おう」

**TW:** 「當然，我會陪你的」

**VN cũ:** 「Tất nhiên rồi, tôi sẽ đi cùng cô.」

**Fix:** 「Tất nhiên rồi, tôi sẽ đi cùng em.」

Soutetsu nói với Hachiroku (JP 僕も付き合おう — đi cùng cô ấy). "Cô"→"em".

### 2432 — ふかみ — sfx

**JP:** 「は……ふぇ？」

**TW:** 「蛤啊……嗯？」

**VN cũ:** 「Hả…… hả?」

**Fix:** 「Hả…… phuê?」

JP は……ふぇ？. Quy tắc fa/fu: ふぇ → "phuê" (ưa chuộng).

### 2436 — 双鉄 — terminology

**JP:** 「なければいいな、湯医まで」

**TW:** 「要是到湯醫為止都沒有陡坡就好了」

**VN cũ:** 「Đến Yui mà không có thì tốt nhỉ.」

**Fix:** 「Đến Yunoi mà không có thì tốt nhỉ.」

JP 湯医まで. Quyết định: 湯医 = "Yunoi".

### 2481 — 双鉄 — terminology

**JP:** 「そうか、ここから湯医まで。⏎なんだかんだで、未だ乗ってはいなかったのだな」

**TW:** 「這樣啊，陰差陽錯，我們還沒坐過從這裡到湯醫的部分」

**VN cũ:** 「Ra là vậy, từ đây đến Yui.⏎Tính ra thì, chúng ta vẫn chưa đi chuyến nào nhỉ.」

**Fix:** 「Ra là vậy, từ đây đến Yunoi. Tính ra thì, chúng ta vẫn chưa đi chuyến nào nhỉ.」

JP ここから湯医まで. Quyết định: 湯医 = "Yunoi".

### 2498 — 双鉄 — pronoun

**JP:** 「ならば、ハチロク。頼めるか」

**TW:** 「那就拜託你了，八六」

**VN cũ:** 「Nếu vậy thì, Hachiroku. Nhờ cô được không.」

**Fix:** 「Nếu vậy thì, Hachiroku. Nhờ em được không.」

Soutetsu nói với Hachiroku (JP ならば、ハチロク。頼めるか). "Cô"→"em".

### 2512 — ハチロク — pronoun

**JP:** 「１００キロ\x%l投炭;#00ffc040;投炭%l;#;とはいえ、連続で３セットですからね。⏎……わたくし、最後は\x%l機関助士;#00ffc040;機関助士%l;#;候補と見ておりました」

**TW:** 「雖然只是一百公斤的\x%l投炭;#00ffc040;加煤%l;#;練習，但一口氣做了三組呢。……我希望能讓她當候補\x%l機関助士;#00ffc040;司爐%l;#;」

**VN cũ:** 「Tuy chỉ là \x%l投炭;#00ffc040;xúc than%l;#; 100 ký, nhưng lại làm liên tục 3 set cơ mà.⏎……Đến cuối cùng, em đã xem cô ấy như một ứng cử viên cho vị trí \x%l機関助士;#00ffc040;phụ lái tàu%l;#; rồi đấy ạ.」

**Fix:** 「Tuy chỉ là \x%l投炭;#00ffc040;xúc than%l;#; 100 ký, nhưng lại làm liên tục 3 set cơ mà. ……Đến cuối cùng, em đã xem em ấy như một ứng cử viên cho vị trí \x%l機関助士;#00ffc040;phụ lái tàu%l;#; rồi đấy ạ.」

Hachiroku nói về Hibiki — ứng cử viên 機関助士 (1987 đã xác lập Hibiki là ứng viên). Hachiroku lớn tuổi hơn, gọi Hibiki là "em" (Hibiki gọi cô ấy là "chị"). "cô ấy"→"em ấy".

### 2514 — 双鉄 — pronoun

**JP:** 「ああ、頼む――と言いたいところではあるが、⏎今日のところは僕より凪にしてやってくれ」

**TW:** 「雖然我也很想拜託你——不過今天你就去幫凪按摩吧」

**VN cũ:** 「À, nhờ cô——tôi rất muốn nói vậy,⏎nhưng hôm nay cô hãy làm cho Nagi thay vì tôi đi.」

**Fix:** 「À, nhờ em——tôi rất muốn nói vậy, nhưng hôm nay em hãy làm cho Nagi thay vì tôi đi.」

Soutetsu nhờ Hachiroku mát-xa cho Nagi thay mình (TW: "你就去幫凪按摩吧"). "Cô"→"em" ×2.

### 2533 — 双鉄 — gasp

**JP:** 「っ！」

**TW:** 「！」

**VN cũ:** 「!」

**Fix:** 「Ư!」

Sweep っ-gasp: JP 「っ！」 — gasp cả dòng. Áp nguyên giá trị sweep, đã kiểm chứng đúng với JP.

### 2534 — 双鉄 — gasp

**JP:** 「っ！！」

**TW:** 「！！」

**VN cũ:** 「!!」

**Fix:** 「Ư!!」

Sweep っ-gasp: JP 「っ！！」 — gasp cả dòng. Áp nguyên giá trị sweep, đã kiểm chứng đúng với JP.

### 2535 — 双鉄 — gasp

**JP:** 「っ！！！！！」

**TW:** 「！！！！！」

**VN cũ:** 「!!!!!」

**Fix:** 「Ư!!!!!」

Sweep っ-gasp: JP 「っ！！！！！」 — gasp cả dòng. Áp nguyên giá trị sweep, đã kiểm chứng đúng với JP.

### 2538 — 双鉄 — terminology

**JP:** 「1.6の123.09。ここまでの\x%l勾配距離;#00ffc040;勾配距離%l;#;が149.23で、⏎\x%lレール種別;#00ffc040;レール種別%l;#;は変化なし――と」

**TW:** 「１．６、１２３．０９。到這裡的\x%l勾配距離;#00ffc040;坡度距離%l;#;是１４９.２３，\x%lレール種別;#00ffc040;鐵軌類型%l;#;不變——好了」

**VN cũ:** 「1.6 và 123.09. \x%l勾配距離;#00ffc040;Chiều dài đoạn dốc%l;#; đến đây là 149.23,⏎\x%lレール種別;#00ffc040;loại đường sắt%l;#; không đổi——xong.」

**Fix:** 「1.6 và 123.09. \x%l勾配距離;#00ffc040;Chiều dài đoạn dốc%l;#; đến đây là 149.23, \x%lレール種別;#00ffc040;loại ray%l;#; không đổi——xong.」

JP レール種別, TW 鐵軌類型 = loại ray. "Loại đường sắt" sai nghĩa (như 1550).

### 2707 — monologue — terminology

**JP:** 赤井宮司にいただいたご助言に従って、⏎今日にでも、登呂流湯に行っておくべきだろう。

**TW:** 今天應該按照赤井宮司的建議，讓她去登呂流浴場做檢查吧。

**VN cũ:** Theo lời khuyên của thầy Akai,⏎có lẽ ngay trong hôm nay, tôi nên đến nhà tắm Tororyu-yu.

**Fix:** Theo lời khuyên của Đền chủ Akai, có lẽ ngay trong hôm nay, tôi nên đến nhà tắm Tororyu-yu.

JP 赤井宮司. Quyết định 19/11: 宮司 = "đền chủ" — tiền lệ file 11: 赤井宮司 → "đền chủ Akai" ở cả 38 dòng. "Thầy Akai" là biến thể thứ ba, chuẩn hóa theo quyết định.

### 2810 — monologue — gasp

**JP:** 鼓動を呼吸を乱せばその分、速度が落ちる。⏎事故の危険を増させてしま――っ！！？

**TW:** 劇烈的心跳會攪亂呼吸，讓我的速度慢下來。這樣也就增加了事故的風險——！！？

**VN cũ:** Nếu để nhịp tim và nhịp thở rối loạn, tốc độ sẽ giảm đi tương ứng.⏎Sẽ làm tăng nguy cơ xảy ra tai nạn mất——!!?

**Fix:** Nếu để nhịp tim và nhịp thở rối loạn, tốc độ sẽ giảm đi tương ứng. Sẽ làm tăng nguy cơ xảy ra tai nạn mất——Ư!!?

Sweep っ-gasp: JP …しま――っ！！？. Áp nguyên giá trị sweep, đã kiểm chứng đúng với JP.

### 2941 — monologue — terminology

**JP:** 赤井宮司に言われたことを思い出す。⏎未来など、人にも物にも、誰にとっても手探りなのだと。

**TW:** 我想起了赤井宮司曾經對我說過的話。人也好，物也好，未來就是在黑暗中摸索。

**VN cũ:** Tôi nhớ lại những lời thầy Akai đã nói.⏎Tương lai, dù là con người hay đồ vật, dù là ai đi nữa cũng đều phải tự mình mò mẫm.

**Fix:** Tôi nhớ lại những lời Đền chủ Akai đã nói. Tương lai, dù là con người hay đồ vật, dù là ai đi nữa cũng đều phải tự mình mò mẫm.

JP 赤井宮司. Như 2707: "thầy Akai"→"Đền chủ Akai" theo quyết định 宮司 = "đền chủ".

### 2948 — monologue — terminology

**JP:** 線路にそっと\x%l運転体;#00ffc040;運転体%l;#;のハチロクを下ろしてやれば、⏎小さな顔の右頬がぴたり、レールにくっつけられる。

**TW:** 我把八六的\x%l運転体;#00ffc040;駕駛體%l;#;放了下來，只見她小小的右臉緊緊貼在鐵軌上。

**VN cũ:** Tôi nhẹ nhàng đặt cơ thể lái của Hachiroku xuống đường ray,⏎má phải trên khuôn mặt nhỏ nhắn của cô ấy áp sát vào thanh ray.

**Fix:** Tôi nhẹ nhàng đặt \x%l運転体;#00ffc040;thân vận hành%l;#; của Hachiroku xuống đường ray, má phải trên khuôn mặt nhỏ nhắn của cô ấy áp sát vào thanh ray.

JP có thẻ %l 運転体; bản Việt không chỉ dịch sai thuật ngữ ("cơ thể lái" thay vì "thân vận hành") mà còn LÀM RỚT cả thẻ (JP 1 thẻ, VN 0 thẻ — đây chính là lệch đếm %l 57 vs 56 của file). Fix khôi phục thẻ với gloss "thân vận hành".

### 3237 — monologue — terminology

**JP:** レールショップでクマ川下りの、⏎発船所では御一夜鉄道一日乗車の割引券をそれぞれ配る。

**TW:** 鐵路商店會發放隈河漂流的優惠券，而漂流發船點則會發放御一夜鐵路一日遊的優惠券。

**VN cũ:** Ở cửa hàng đường sắt thì phát vé giảm giá xuôi dòng sông Kuma,⏎còn ở bến thuyền thì phát vé giảm giá đi tàu đường sắt Ohimitera một ngày.

**Fix:** Ở cửa hàng đường sắt thì phát vé giảm giá xuôi dòng sông Kuma, còn ở bến thuyền thì phát vé giảm giá đi tàu đường sắt Ohitoyo một ngày.

JP 御一夜鉄道. Quyết định: 御一夜 = "Ohitoyo".

## 4. Kiểm tra chéo

- **Sweep っ-gasp:** 8 mục cho file này (7 fix + 1 already-rendered 2057). Cả 7 fix áp nguyên, đã kiểm chứng từng giá trị với JP. Quét bổ sung toàn bộ 180 dòng JP chứa っ: còn lại đều là っ nhấn mạnh cuối từ, っ trong từ, hoặc âm đã render đúng — không có gasp nào sweep bỏ sót.
- **Thẻ %l:** lệch duy nhất 2948 (đã khôi phục thẻ trong fix). Sau fix, số thẻ VN = số thẻ JP (69/69). Không có thẻ đóng sai định dạng.
- **Nhiễm chéo:** 0. Trùng VN duy nhất 2959/日々姫05-3069 là dòng lặp hợp lệ (xem §2).
- **Lệch dòng / chuỗi xoay:** 0. Không có dòng nào cần dịch lại từ đầu; không có chuỗi xoay; không có VN mồ côi.
- **Kiểm tra cơ học:** 45/45 fix khác VN cũ; 45/45 key dạng chuỗi, không trùng; 44/45 fix một dòng (chỉ 1927 giữ `\n` cấu trúc vì là hai câu thoại của hai người trong một dòng); ngoặc 「 」 cân bằng 45/45; thẻ %l không đổi trừ 2948 (khôi phục 1 thẻ).

## 5. Kiểm tra lần 2 (second pass)

Đọc lại toàn bộ 45 giá trị fix đối chiếu từng cái với JP gốc (đợt đọc thứ hai, độc lập với đợt đọc đầu): **tổng 45 / kiểm tra lại 45 / loại bỏ 0 / sửa lại 0**. Kiểm tra cơ học kèm theo: với mỗi fix, phần cũ cần thay đã biến mất khỏi giá trị fix, phần mới đã có mặt, và phần cũ có thật trong VN cũ (cơ sở sửa đúng).

Một phán đoán ở đợt đọc đầu đã bị loại bỏ TRƯỚC khi chốt (không tính vào 45): key 1898 "anh sẽ đứng ra"→"tôi sẽ đứng ra" — suy từ thứ tự lượt nói (Hachiroku nói ở 1895) nên tưởng người nghe là Hachiroku; kiểm tra lại thấy TW dùng 你們 (các bạn, số nhiều) và nội dung là xin phép người giám hộ — người nghe là các cô gái (Nagi/Fukami), nên "anh" là đúng. Xem §6.

## 6. Các dòng cố tình KHÔNG sửa (ghi chú phán đoán)

- **1898 "anh sẽ đứng ra":** xem §5 — người nghe là các cô gái (TW 你們 số nhiều + nội dung xin phép người giám hộ), không phải Hachiroku. "Anh" đúng. Không sửa.
- **1519 登呂流湯 → "nhà tắm Tororyu-yu":** tên riêng của nhà tắm, giữ nguyên. Không sửa.
- **1571 綺麗 → "Đẹp quá":** JP thắng TW (TW dịch nhầm thành 動作). Không sửa.
- **1566/1962/2378 凪様 → "cô Nagi":** nhất quán trong file; Hachiroku gọi Nagi là "cô Nagi". Không sửa.
- **1907 "bám vào anh đi":** người nghe là Fukami hoặc Nagi — cả hai đều gọi Soutetsu là "anh". Không sửa.
- **2057 う～～っ → "Ư~~":** sweep already-rendered, đã kiểm chứng đúng. Không sửa.
- **2096 チェストー → "Hây aaaaaaaaaaa":** tiếng hô ngẫu hứng theo quy tắc 22:05, giữ nguyên.
- **2478/2762/2792 ワンスコ → "wansuko":** giữ romaji thuật ngữ; dòng sau giải thích ngay đó là xẻng xúc than. Không sửa.
- **2503 主人 → "Bà chủ":** TW 她說 xác nhận chủ nhà tắm là nữ. Không sửa.
- **2888 蒸気排水 → "Xả nước ngưng hơi nước":** gloss kỹ thuật đúng (xả nước ngưng tụ hơi nước), chỉ hơi dài dòng. Không sửa.
- **2965 アホウ！:** một trong 3 khác biệt CSV↔TOML do gộp `\n`, không phải lỗi dịch. Không sửa.
- **3307 僕っ―― → "mày ơi":** tự nhủ (self-exhortation), diễn ngẫu hứng, giữ nguyên.
- **2749/2752/2761/2878 "cô ấy" trong độc thoại:** ngôi thứ ba trong lời kể của Soutetsu, không phải xưng hô trực tiếp — "cô ấy" chỉ Hachiroku là đúng. Không sửa.
- **1557 「…………」:** JP/TW/VN giống hệt nhau — dấu lặng, hợp lệ. Không sửa.
- **2038 っ cuối:** ngắt giọng nhấn mạnh trên SFX đã diễn (xem ghi chú ở mục 2038), không thêm Ư riêng.

## Kết bài

File 13 là file 00_Common sạch về cấu trúc (45/462 = 9,7%): 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 dòng chưa chắc chắn. Lỗi tập trung ở hai nhóm quen thuộc — đại từ xưng hô chưa cập nhật (20 dòng, chủ yếu Soutetsu↔Hachiroku "cô"→"em" 11 dòng) và thuật ngữ theo các quyết định 19–20/11 (12 dòng). Toàn bộ "Ohimitera" (3) và "Yui" (3) trong file đã được sửa hết; lệch đếm thẻ %l duy nhất của file (2948) đã được xác định và khôi phục. Toàn bộ 45 fix đều sửa tại chỗ, không cần dịch lại.

Khối TOML dưới đây parse được bằng tomllib, **45 key, 0 sai lệch giá trị so với JSON**. Quy tắc ký tự xuống dòng: giá trị fix nào chứa ký tự xuống dòng dạng backslash-n (2 ký tự, như trong JSON và trong TOML gốc) thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON. (Chỉ key 1927 chứa backslash-n, vì đó là hai câu thoại của hai người trong một dòng.)

```toml
[script]
"1537" = "「\\x%l保線;#00ffc040;Bảo trì đường ray%l;#; đấy. Em bảo đường sắt thì không thể thiếu \\x%l保線;#00ffc040;bảo trì đường ray%l;#; mà.」"
"1550" = "「\\x%l勾配千分率;#00ffc040;Độ dốc phần nghìn%l;#; 1.6. \\x%l施工基面高;#00ffc040;Cao độ mặt nền đường sắt%l;#; 123.09. \\x%l勾配距離;#00ffc040;Chiều dài đoạn dốc%l;#; là 149.23. \\x%lレール種別;#00ffc040;Loại ray%l;#; vẫn là 30 ký.」"
"1568" = "「……Em quả thực là một đồ vật, một công cụ nhỉ.」"
"1874" = "「Không xong rồi! Bị thân cây chắn ngang hoàn toàn rồi——Ư!!?」"
"1878" = "「Nhưng mà, cảm biến của thân vận hành tuyệt thật đấy. Không cần dụng cụ mà vẫn đo được độ dốc cơ mà.」"
"1892" = "「Nhưng Hachiroku này, tôi không phải ai khác ngoài chính tôi. Tôi không thể suy nghĩ thay em để tìm ra câu trả lời cho em được đâu?」"
"1904" = "「Em không thấy sốc sao?」"
"1906" = "「Những phần mà em không thể kiểm soát có lẽ là, do em tự ý suy nghĩ, nên mới thành ra \"suy nghĩ quá nhiều\".」"
"1925" = "「Này, Hachiroku. Đúng như những gì em đã nói nhỉ.」"
"1927" = "「Hachiroku nói trước đi——Ư!」\\n「Ngài Soutetsu nói trước đi ạ——Ư!」"
"2023" = "「Hia!? Hiaaa!? Chuyện lớn rồi!!」"
"2028" = "「Phù~~Ư」"
"2033" = "「Hả…… phà…… quả nhiên, hai người, là mối quan hệ như thế~」"
"2038" = "「Phuêêêêê!? Không sao đâu! Không sao đâu! Ạ.」"
"2052" = "「Hừừm.」"
"2076" = "「A, ông ạ? Chuyện là, bây giờ cháu đang ở ga Ohitoyo.」"
"2119" = "「Có lẽ vì cơ bản là chạy dọc theo con sông, nên tuyến Yunoi quả thực là một tuyến đường rất thoai thoải nhỉ.」"
"2126" = "「Được thôi. Vậy thì Hachiroku—— Em có thể giúp hướng dẫn từ bước đầu tiên được không?」"
"2151" = "「Chị Fukami…… không được đâu, mồ hôi với thứ đen đen này, dính sang chị mất.」"
"2153" = "「Chị Fukami, để em kỳ lưng cho nhé!」"
"2156" = "「Chị Fukami, mặt chị đỏ bừng kìa! Bị ngâm nóng quá rồi hả?」"
"2215" = "「Rõ rồi! Em hãy tiếp tục đánh thức Reina đi!」"
"2218" = "「Tôi đến gần xem một chút được không?」"
"2267" = "「Vâng ạ, tuyến đường từ đây trở về Ohitoyo em cũng đã xác nhận lúc ở trong \\x%lキハ07;#00ffc040;KiHa 07%l;#; rồi, nhưng mà——」"
"2271" = "「Ý em là sức mạnh sao? Đủ sức vượt qua mà không cần bận tâm đến những chi tiết nhỏ nhặt ấy.」"
"2329" = "「Đã tốt hơn lúc nãy rất nhiều rồi ạ. Trên thang điểm 100, em có thể cho ngài 22 điểm.」"
"2333" = "「Tôi đang mong thế đây. Sự chỉ bảo nghiêm khắc sẽ dẫn đến sự trưởng thành tốt hơn mà.」"
"2335" = "「Đúng vậy. Trí tuệ hay…… ngay cả lý trí thực chất cũng rất khó kiểm soát. Đối với tôi——và có lẽ, đối với cả em nữa, Hachiroku.」"
"2349" = "「Ngâm nóng quá…… ư~~, chắc là, bị ngâm nóng quá nên choáng váng luôn rồi~」"
"2380" = "「Tất nhiên rồi, tôi sẽ đi cùng em.」"
"2432" = "「Hả…… phuê?」"
"2436" = "「Đến Yunoi mà không có thì tốt nhỉ.」"
"2481" = "「Ra là vậy, từ đây đến Yunoi. Tính ra thì, chúng ta vẫn chưa đi chuyến nào nhỉ.」"
"2498" = "「Nếu vậy thì, Hachiroku. Nhờ em được không.」"
"2512" = "「Tuy chỉ là \\x%l投炭;#00ffc040;xúc than%l;#; 100 ký, nhưng lại làm liên tục 3 set cơ mà. ……Đến cuối cùng, em đã xem em ấy như một ứng cử viên cho vị trí \\x%l機関助士;#00ffc040;phụ lái tàu%l;#; rồi đấy ạ.」"
"2514" = "「À, nhờ em——tôi rất muốn nói vậy, nhưng hôm nay em hãy làm cho Nagi thay vì tôi đi.」"
"2533" = "「Ư!」"
"2534" = "「Ư!!」"
"2535" = "「Ư!!!!!」"
"2538" = "「1.6 và 123.09. \\x%l勾配距離;#00ffc040;Chiều dài đoạn dốc%l;#; đến đây là 149.23, \\x%lレール種別;#00ffc040;loại ray%l;#; không đổi——xong.」"
"2707" = "Theo lời khuyên của Đền chủ Akai, có lẽ ngay trong hôm nay, tôi nên đến nhà tắm Tororyu-yu."
"2810" = "Nếu để nhịp tim và nhịp thở rối loạn, tốc độ sẽ giảm đi tương ứng. Sẽ làm tăng nguy cơ xảy ra tai nạn mất——Ư!!?"
"2941" = "Tôi nhớ lại những lời Đền chủ Akai đã nói. Tương lai, dù là con người hay đồ vật, dù là ai đi nữa cũng đều phải tự mình mò mẫm."
"2948" = "Tôi nhẹ nhàng đặt \\x%l運転体;#00ffc040;thân vận hành%l;#; của Hachiroku xuống đường ray, má phải trên khuôn mặt nhỏ nhắn của cô ấy áp sát vào thanh ray."
"3237" = "Ở cửa hàng đường sắt thì phát vé giảm giá xuôi dòng sông Kuma, còn ở bến thuyền thì phát vé giảm giá đi tàu đường sắt Ohitoyo một ngày."
```
