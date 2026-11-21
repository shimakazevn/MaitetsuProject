# Audit: ハチロク16_春.txt.toml (01_Hachiroku) — 22/412 (5,3%)

- File: `ハチロク16_春.txt.toml` — route 01_Hachiroku, 412 dòng script (thoại 246, độc thoại 166: Hachiroku 71, Soutetsu 69, Hibiki 37, Kodama 18, Munakata 18, Công chúa Tàu điện 14, Paulette 6, Hiyoko 4, Nozomi 4, Reina 3, Mayami 2). Nội dung: buổi sáng mùa xuân trên tuyến — Kodama ra mắt, chuẩn bị cho chuyến tàu của cô bé; Soutetsu và Hachiroku nhớ lại Olivy, ngắm cảnh qua cửa sổ ở Okoba/Yatsushiro, Hibiki lái 8620 leo dốc Yatake; Munakata từ chối làm Master của Kodama; Công chúa Tàu điện xuất hiện qua màn hình.
- Đã đọc: 412/412 dòng, đối chiếu từng dòng với JP + TW (CSV3).
- **Sai: 22 dòng (5,3%)** — thuật ngữ 6, gasp 10, sai nghĩa 5, số nguyên âm 1.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, 412 dòng, 0 VN trống, 0 trùng key. TOML md5 `f8506b4cc0b92e50a202aa8435022314`, 1 bản duy nhất, BOM + CRLF, `[selections]` rỗng, `[info]` rỗng. TOML khớp CSV3 tuyệt đối sau chuẩn hoá `\n` literal (183 dòng khớp tuyệt đối, 229 dòng chỉ khác ở flatten `\n`→khoảng trắng, 0 dòng khác nội dung). 1 cặp VN trùng là câu lặp hợp lệ (1733/1766 cùng JP 「あ」→「A.」).
- Sweep gasp: 9 mục — nhận cả 9 sau khi đối chiếu JP; audit tìm thêm 1 gasp sweep bỏ sót (1689, 2 dòng っ nguyên dòng). Quét máy toàn bộ dòng っ: không còn gasp sót khác (các っ còn lại đã được diễn bằng dấu câu/âm cuối, xem §5).
- Cơ sở tổng: **179 file / 8.089 dòng sai** (đã kiểm chứng lại với ROUTE-AUDIT.md — cơ sở 178/8.083 trong nhiệm vụ đã cũ vì file 日々姫11 gộp xong lúc ~23:30, +6).

## §1. Danh sách sửa (22)

### Thuật ngữ (6)
- 1294 (Soutetsu): JP 冥国 / TW 美國. VN cũ "nước Mỹ" → "Minh Quốc". Quy tắc đã chốt 19/11: 冥国="Minh Quốc" (chỉ giữ "Meriken" khi furigana メリケン là lời thoại). Tiền lệ file 真闇03 sửa 冥国→"Minh Quốc" trong audit (parent kiểm chứng).
- 1611 (Công chúa Tàu điện), 1995 (Hiyoko), 2298, 2307, 2509 (độc thoại): gloss タブレット "thẻ bảng" → "máy tính bảng". Quy tắc đã chốt: 操作板/タブレット="máy tính bảng". Tiền lệ nhiều file đã sửa trong audit (vd. file 1610: 1706, 2113). 2307 sửa cả 2 gloss trong cùng dòng.

### Gasp — っ bị mất (10)
- Sweep (9, nhận nguyên giá trị sau khi đối chiếu JP): 1721 「っ！！」→"Ư!!"; 1725 「っ！」→"Ư!"; 1744 「っ！！」→"Ư!!" (dòng 2 「ああ――」→"A――" giữ nguyên); 1746 「っ！！？」→"Ư!!?" (dòng 2 きゃっ→"Kya!" giữ nguyên — dấu !? đã diễn tiếng ngắt); 1808 trailing と～っ → "~Ư!"; 1932 trailing か――っ → "――Ư!!!"; 2052 「っ！！！！」→"Ư!!!!"; 2380 trailing 前に出て――っ → "――Ư!!"; 2783 trailing 探してしま――っ → "――Ư!!!".
- Sweep bỏ sót (1): 1689 — hai dòng 「っ！！？」 VN chỉ còn "!!?" (mất hẳn tiếng gasp, cùng mẫu lost-gasp-whole của sweep) → "Ư!!?" ×2; dòng 3 えええっ→"Hảảả!?" GIỮ (nguyên âm đã diễn, !? diễn tiếng ngắt — cùng lý do giữ 1761, xem §5).

### Sai nghĩa (5)
- 1730 (Soutetsu): JP 「ああ――いや」/ TW 「啊——沒有」. VN cũ "À――chưa." → "À――không." — いや = "không", không phải "chưa".
- 2081 (Hibiki): JP 日ノ本三大車窓 / TW 日本三大車窗絕景. VN cũ "Một trong ba khung cảnh..." (thêm "Một trong" không có trong JP) → "Ba khung cảnh qua cửa sổ đẹp nhất Hinomoto ấy, cùng với Olivy."
- 2283 (độc thoại): JP 「三人に一度に抱きしめられては…けれど、離れることができない」/ TW 「她嚇了一大跳。但是，卻沒有掙脫的意思」. VN cũ đổi chủ ngữ sang người kể ("tôi không thể buông tay ra được") → "Nhưng mà, cô bé không thể thoát ra được." (chủ ngữ là cô bé bị ôm, theo JP + TW).
- 2377 (độc thoại): JP 「こころに、言葉が浮かんでこない」/ TW 「我大腦一片空白」. VN cũ bỏ mất phủ định ("Hiện lên trong tâm trí tôi lúc này.") → "Trong tâm trí tôi lúc này, chẳng có lời nào hiện lên cả."
- 2735 (độc thoại): JP 何倍も、何十倍も、何百倍も / TW 幾倍、幾十倍、幾百倍. VN cũ "gấp vạn lần" (bịa thêm "vạn" = 10.000) → "gấp bội". Cùng cụm ở 2643 đã dịch đúng "gấp bội".

### Số nguyên âm (1)
- 2817 (độc thoại, SFX): JP （ポーーーーーーーーっ！！）= ポ + 8 dấu ー = 9 mora; VN cũ "Tuúúúúúúúúúúú!" = 12 nguyên âm u → "Tuúúúúúúúú!" (9 nguyên âm, theo công thức độ dài). Tiền lệ file 真闇03 sửa 1912 はぁあ thừa 1 a trong audit.

## §2. Kiểm tra cấu trúc
- Lệch vị trí 0 — không có dòng VN nào ngồi sai key (đã rà chuỗi: JP/TW/VN khớp từng key; không có cặp dời chỗ).
- Chuỗi xoay 0, nhiễm chéo 0 (đã kiểm tra các dòng nghi ngờ; 3 ca nhiễm đã biết toàn dự án không liên quan file này), mồ côi 0 (mọi VN đều có JP tương ứng trong file), chưa dịch 0 (0 VN trống), trùng khóa 0 (CSV3 412 key duy nhất, TOML 412 key khớp 1–1).
- Thẻ %l: số thẻ JP = VN ở mọi dòng (0 lệch đếm); không có thẻ VN tự thêm, không có thẻ JP bị rớt; không có thẻ thiếu `;` trong file này.
- 1 cặp VN trùng là câu lặp hợp lệ: 1733/1766 cùng JP 「あ」→「A.」 (cùng Soutetsu, 2 thời điểm khác nhau).

## §3. Đại từ đã kiểm chứng
- Soutetsu "tôi" với Hachiroku giữ nguyên đúng chỗ (vd. 1674, 1729, 1789, 2016, 2322, 2513); "anh" với Hibiki không xuất hiện sai chỗ trong file này.
- Munakata: 4 dòng 俺/おれ (1301, 1884, 1910, 2025) + 6 dòng "tôi" không có 俺 tường minh trong JP (1297, 1306, 1637, 1903, 2050, 2070) — xem §4 (chờ đợt thống nhất, không sửa trong audit).
- 1999 Soutetsu "Anh cũng thấy..." — KHÔNG CHẮC người nghe (cảnh tập thể trên tàu; nếu nói với Hibiki thì "anh" đúng, nếu với Hiyoko/Hachiroku thì phải là "tôi") — GIỮ NGUYÊN, cờ cho Hieu (§6).
- Các "anh Munakata" của Soutetsu (1821, 1823, 2015, 2086) là cách gọi Munakata, không phải tự xưng — giữ nguyên, nhất quán toàn file.
- Paulette gọi Soutetsu: 1755 "anh sẽ tham gia" đúng (khóa B4: 双鉄くん→"anh Soutetsu"); không có "cậu" nào trong file này.
- Hachiroku tự xưng "em", gọi Soutetsu "Ngài Soutetsu" — nhất quán toàn file.

## §4. Thuật ngữ — chờ đợt thống nhất (không sửa trong audit)
Theo tiền lệ mới nhất đã được parent kiểm chứng — file 日々姫11 (gộp 21/11 ~23:30), review §4 "Thuật ngữ — chờ đợt thống nhất (không sửa trong audit)": các mục dưới đây để đợt thống nhất một lần, KHÔNG tính vào số sai của audit. (Quyết định đổi tên công ty 21/11 ~17:30 cũng ghi rõ "queued with the unification pass".)
- "Ohimitera" (địa danh, JP 御一夜) 3 dòng → "Ohitoyo": 1803, 1839, 1845.
- Tên công ty "Đường sắt Ohito" (JP 御一夜鉄道/御鉄) 3 dòng → "Đường sắt Ohitoyo": 1221, 1884, 2070. (1884 đồng thời có おれ→"tao" của Munakata — cũng để đợt thống nhất, xem dưới.)
- "tuyến Yui" (JP 湯医線/湯医) 4 dòng → "tuyến Yunoi": 1622, 1987, 2403, 2587.
- "Densha Hime" (JP 電車姫様) 3 dòng → "Công chúa Tàu điện": 2692, 2706, 2790.
- Gloss 帝鉄 "Đường sắt Hoàng gia" 1 dòng → "Teitetsu": 2338. (Dạng đầy đủ "Đường sắt Đế quốc" chỉ dùng trong tooltip %l lần đầu — dòng này là độc thoại, không tooltip.)
- Giọng Munakata 俺/おれ → "tao" 4 dòng (quyết định 21/11 ~17:30, queued with unification): 1301 ("Tao không biết"), 1884 ("Tao không phải là Master"), 1910 ("Đã bảo tao không phải là Master mà"), 2025 ("Tao không phải là Master của Kodama"). Giá trị đề xuất đã ghi rõ để đợt thống nhất áp dụng.
- 日ノ本: đã kiểm tra toàn file — 0 dòng "Hinamoto"; cả 4 dòng 日ノ本 (1254, 1646, 1810, 2081) đã đúng "Hinomoto" sẵn. (Nhiệm vụ có nhắc: file này không có "Hinamoto" nào — không cần sửa.)
- Gloss 投炭 "xúc than" (2688): giữ nguyên — mục "投炭 gloss split" đã có trong hàng chờ thống nhất.

## §5. Đã kiểm tra và giữ nguyên (không tính sai)
- 1761 はうっ→"Hau!?": giữ — っ đã được diễn bằng "!?" theo sau (ranh giới gasp đã khóa: chỉ thêm Ư khi っ hoàn toàn mất; tiền lệ giữ "Hau" ở các file trước; file 日々姫11 sửa はうっ→"hấuƯ" ở 1907 vì dòng đó KHÔNG có dấu câu theo sau).
- 1689 dòng 3 えええっ→"Hảảả!?": giữ (nguyên âm đã diễn, !? diễn tiếng ngắt).
- 1708 はははっ→"Hahaha."; 1709 あらっ→"Ôi."; 1712 っと→"Á!"; 1732 あ……あっ――→"A……a――" (―― diễn tiếng ngắt, không diễn trùng); 1750 こだまっっ; 1753 ごめんっ; 1769 うんっ/ただいまっ; 2090 あっっ — đều là っ nhấn mạnh dính từ nội dung/tên riêng, không phải gasp (quy tắc: っ cuối câu nhấn mạnh dính từ nội dung thì không thêm Ư).
- 1696/1785 うふふぅ→"Fufu": giữ — tiếng cười, diễn ngẫu hứng theo nhân vật (quy tắc SFX 19/11); không áp công thức đếm nguyên âm cho tiếng cười.
- 1751 んんっ→"ừm.": giữ (âm cuối "m" + dấu chấm đã diễn tiếng ngắt, tiền lệ ハチロク01 2319).
- 1306 JP cụt câu (「その節は、大変申し訳無いことを」) — VN hoàn thiện tự nhiên theo TW, giữ nguyên.
- 1651 「こだまは電車！」→"Kodama thích tàu điện!": giữ, theo TW 「小玉想要電車」.
- 1755 câu Paulette cụt câu (kết bằng と) — VN hoàn thiện theo TW, giữ nguyên.
- 1974 ba dạng おかえりっ/おかえり/おかえりなさいっ → VN phân biệt bằng dấu câu (!/. /!) — giữ nguyên.
- 2021 旺宮→"Omiya", 夕針→"Yubari": giữ, theo TW 大宮/夕張.
- 2070 "các cô cậu": giữ — cách nói khẩu ngữ ("từ phía Đường sắt Ohito các cô cậu") chấp nhận được; phần "Đường sắt Ohito" để đợt thống nhất (§4).
- 2780 「消し去ってもらっている」→"nó luôn bị xóa nhòa": giữ — diễn đạt bị động, lược tác nhân nhưng không đổi nghĩa chính (TW cũng diễn theo hướng chủ động đè nén).
- 95 屋岳→"Yatake": giữ — theo TW 矢岳 (cùng cách đọc).
- 1180 「まっすぐ日々姫に向けられる」→"hướng thẳng về phía Hibiki": giữ — độc thoại, lược chủ ngữ chấp nhận được.
- 1249 「そうてつ、さま」→"Ngài... Soutetsu.": giữ — dấu "..." đối chiếu vị trí ngắt của JP.
- Các SFX dài khác trong file đều đã đúng số lượng (1741 あああ→"Aaa", 1689 えええ→"Hảảả"); 2817 đã sửa (xem §1).

## §6. Lượt soát 2 + cờ cho Hieu
- Lượt soát 2: đọc lại toàn bộ 37 giá trị fix ứng cử với JP; 22 giữ trong audit (22/22 xác minh lại, 0 bỏ, 1 sửa: 2283 bỏ "cũng" thừa — JP không có "cũng"); 15 chuyển sang §4 chờ đợt thống nhất theo tiền lệ file 日々姫11 §4 (không phải lỗi đọc lại — quyết định phạm vi, đã ghi rõ giá trị đề xuất).
- Kiểm chứng cơ học: JSON 22 mục dạng chuẩn list-of-dicts, key chuỗi; khối TOML 22 khóa, 0 sai lệch giá trị (tomllib parse); jp/tw/old_vn khớp CSV3 tuyệt đối 22/22; mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (diff-sanity đã chạy — xem §1).
- Cờ cho Hieu (không quyết thay):
  1. 1999 Soutetsu "Anh cũng thấy khung cảnh qua cửa sổ ở đây rất tuyệt." — người nghe chưa xác định (cảnh tập thể trên tàu; Hibiki → "anh" đúng, Hiyoko/Hachiroku → phải "tôi") — giữ nguyên "Anh".
  2. Munakata: 6 dòng "tôi" không có 俺 tường minh trong JP (1297, 1306, 1637, 1903, 2050, 2070) — "tao" có áp cho toàn bộ lời thoại của Munakata, hay chỉ 4 dòng có 俺/おれ tường minh (§4)? Chờ quyết phạm vi (đợt thống nhất hoặc Hieu).
  3. [characters] key 2791 = "Densha Hime" và [character_subs] key 2789 = "電車公主" — có đổi tên hiển thị nhân vật theo quy tắc "Công chúa Tàu điện" không? Ngoài khối sửa [script] nên chỉ ghi nhận, không sửa.
  4. B19 vẫn park (kiểm tra trong game tại Paulette 13 key 1596 trước khi chạy sweep thẻ %l).
- Không có câu hỏi thuật ngữ mới nào khác cần Hieu quyết.

## Khối TOML (đã kiểm chứng parse)

```toml

"1294" = "「……Em ấy từng kể cho chúng ta nghe rồi nhỉ.\\nCâu chuyện về khu mỏ than bỏ hoang ở Minh Quốc hiện vẫn đang bốc cháy.」"
"1611" = "「Hình như là 『Từ \\x%lタブレット;#00ffc040;máy tính bảng%l;#; của một \\x%lレイルロオド;#00ffc040;Railord%l;#; đã hoạt động hơn một trăm năm,\\nmột Lõi Railord hoàn toàn mới đã được tinh chế ra』 thì phải?」"
"1689" = "「Ư!!?」「Ư!!?」\\n「Hảảả!?」"
"1721" = "「Ư!!」"
"1725" = "「Ư!」"
"1730" = "「À――không.」"
"1744" = "「Ư!!」\\n「A――」"
"1746" = "「Ư!!?」\\n「Kya!」"
"1808" = "「Nặng quá~! Nặng quá đi mất~Ư!」"
"1932" = "「Hibiki, sao thế? Có bị thương không――Ư!!!」"
"1995" = "「Tất nhiên là tôi muốn tự tay nuôi dưỡng con bé rồi. Dù sao đây cũng là một trường hợp vô cùng quý giá,\\ntinh chế ra hai Lõi Railord từ một \\x%lタブレット;#00ffc040;máy tính bảng%l;#; duy nhất cơ mà.」"
"2052" = "「Ư!!!!」"
"2081" = "「Anh hai và Hachiroku đã từng thấy chưa?\\nBa khung cảnh qua cửa sổ đẹp nhất Hinomoto ấy, cùng với Olivy.」"
"2283" = "Bị ba người ôm chầm lấy cùng một lúc, tất nhiên là cô bé sẽ ngạc nhiên rồi.\\nNhưng mà, cô bé không thể thoát ra được."
"2298" = "Nói cách khác, nó giống như là “linh hồn” của \\x%lレイルロオド;#00ffc040;Railord%l;#; vậy.\\nThứ đó, đã được tinh chế từ \\x%lタブレット;#00ffc040;máy tính bảng%l;#; của Olivy――"
"2307" = "Lõi Railord. Thứ làm cho \\x%lタブレット;#00ffc040;máy tính bảng%l;#; trở thành \\x%lタブレット;#00ffc040;máy tính bảng%l;#;\\nlàm cho \\x%lレイルロオド;#00ffc040;Railord%l;#; trở thành \\x%lレイルロオド;#00ffc040;Railord%l;#;……"
"2377" = "Chỉ có một điều duy nhất, chỉ có một điều duy nhất, chỉ có một điều duy nhất.\\nTrong tâm trí tôi lúc này, chẳng có lời nào hiện lên cả."
"2380" = "Có lẽ vì sốt ruột trước bài diễn văn dài dòng của Tiến sĩ Phượng Hoàng,\\ncô bé sốt sắng bước lên phía trước――Ư!!"
"2509" = "Việc tinh chế từ \\x%lタブレット;#00ffc040;máy tính bảng%l;#; có lẽ đồng nghĩa với việc chức năng đã ngừng hoạt động,\\nnhưng dù vậy, chúng tôi vẫn có thể tự mình kết nối với tương lai."
"2735" = "Điều đó, khiến tôi cảm thấy vui sướng.\\nHơn cả sự cô đơn, gấp bội, gấp chục lần, gấp trăm lần."
"2783" = "Dù biết đó là chuyện không tưởng,\\nnhưng tôi vẫn bất giác đưa mắt tìm kiếm hình bóng ấy giữa đám đông――Ư!!!"
"2817" = "（Tuúúúúúúúú!）"
```

## Kết bài

File ハチロク16_春.txt.toml đã đọc đủ 412/412 dòng. **Sai: 22 dòng (5,3%)** — thuật ngữ 6 (1294, 1611, 1995, 2298, 2307, 2509), gasp 10 (1689, 1721, 1725, 1744, 1746, 1808, 1932, 2052, 2380, 2783), sai nghĩa 5 (1730, 2081, 2283, 2377, 2735), số nguyên âm 1 (2817). Không có lệch vị trí, chuỗi xoay, nhiễm chéo, mồ côi, chưa dịch hay trùng khóa. 15 dòng thuật ngữ/đại từ khác đã ghi rõ giá trị đề xuất ở §4 để đợt thống nhất áp dụng một lần (theo tiền lệ file 日々姫11). 1 dòng không chắc chắn (1999) và 3 cờ khác đã ghi ở §6, chờ Hieu. Khối TOML 22 khóa đã parse-verified, 0 sai lệch giá trị so với JSON; jp/tw/old_vn khớp CSV3 tuyệt đối 22/22; lượt soát 2: 22/22 xác minh lại, 0 bỏ, 1 sửa.
