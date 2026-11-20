# Audit — 日々姫07_姉の想い。妹の想い (02_Hibiki) — 15/430 (3,5%)

File: `日々姫07_姉の想い。妹の想い.txt.toml` — route 02_Hibiki, 430 dòng script.
Disk: `sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59eb07_#U59c9#U306e#U60f3#U3044#U3002#U59b9#U306e#U60f3#U3044.txt.toml` (tên file #U-escaped, đúng như trên đĩa).
Nội dung: Hibiki trình bày thiết kế bếp + thực đơn toa ăn cho Paulette/Kisaki/Fukami/Nagi (FL cost, tiết kiệm nguyên liệu, tên "Toa ăn Kết nối"); Mayami từ chối lên tàu ("Chị, không thể lên đoàn tàu này được"), Hibiki suy sụp, Soutetsu dỗ dành và cùng em nhận ra điểm thiếu (chỉ nhìn Ohitoyo, bỏ qua các vùng khác); cả hai đến Bungomori gặp Kimoto, nghe về đầu máy 29611 + gara hình quạt, nảy ra ý "toa ăn đưa đồ tươi vào" → tên mới 『とれいん食堂』.
Nhân vật: monologue 174, 日々姫 97, 双鉄 74, 木本 25, 凪 13, ふかみ 12, ポーレット 10, 真闇 10, 稀咲 9, ハチロク 3, れいな 3.

Phương pháp: đọc toàn bộ 430 dòng theo từng hàng, đối chiếu JP + TW (CSV3), kiểm tra cơ học thêm (xem §3). Key order trong TOML == CSV3 order (xáo trộn, không phải story order) — người nghe/đại từ xác định theo nội dung và dòng kề trong luồng truyện, không theo key. Cơ sở tổng cộng đã kiểm chứng lại với ROUTE-AUDIT.md trước khi viết snippet: 84 file / 4.369 dòng sai — khớp với số parent giao.

## §1. Kết quả

Sai: **15/430 (3,5%)**.

Phân loại (15):
- **lost-gasp**: 6 (1832, 1833, 1834, 1850, 1900 — 5 mục sweep, áp nguyên sau kiểm chứng; 1431 — sweep bỏ sót, audit tự tìm).
- **thuật ngữ**: 1 (1366 — 帝鉄 → "Teitetsu").
- **xưng hô**: 2 (1859 — Fukami tự xưng "chị" → "em" (người nghe Soutetsu/Hibiki — parent sửa, agent ghi nhầm "mình" với Nagi); 1721 — Paulette tự xưng "em" → "chị" với Hibiki).
- **sai nghĩa**: 2 (2900 — 運び込む; 2982 — 高菜めし).
- **lỗi nhỏ**: 3 (1798, 2169 — dấu "Ạ" đứng riêng câu, Fukami; 2992 — còi báo dài gấp đôi JP).
- **tag**: 1 (1428 — VN tự thêm thẻ %l gloss mà JP không có).

Không misaligned / không rotation / không contamination chéo file / không orphan / 0 untranslated / 0 duplicate key. Không lỗi đại từ hệ thống: Soutetsu "anh" với Hibiki xuyên suốt và đúng (thoại "anh"/"em" gọi Hibiki, 0 dòng "tôi" trong thoại với Hibiki); độc thoại kể chuyện đồng nhất "tôi" (0 dòng monologue dùng "Anh" làm chủ ngữ). Không chắc chắn: 2 (2632, 1941 — xem §6).

Sweep っ-gasp: 5 mục cho file này trong `sweep-raw-gasp-wrong.json` — đã kiểm chứng từng mục với JP và áp dụng cả 5, 0 mục bị loại (xem §2.1). Audit quét thêm toàn bộ dòng JP có っ và tìm thêm 1 gasp sweep bỏ sót (1431).

Strong candidates 6 → đọc toàn bộ tìm ra 15 sai: heuristic chỉ đếm được một phần (nó không thấy lỗi nghĩa/đại từ/tag thêm/SFX độ dài).

## §2. Các lỗi và cách sửa

### §2.1. Gasp っ — 6 hàng (5 sweep + 1 tự tìm)

| Hàng | Nhân vật | JP | VN cũ | Fix |
|---|---|---|---|---|
| 1832 | 真闇 | 「っ！」 | 「!」 | 「Ư!」 |
| 1833 | 日々姫 | 「っ！！！」 | 「!!!」 | 「Ư!!!」 |
| 1834 | 日々姫 | 「っ！！！！」 | 「!!!!」 | 「Ư!!!!」 |
| 1850 | 双鉄 | 「っ！！？」 | 「!!?」 | 「Ư!!?」 |
| 1900 | ふかみ＆日日姬 | 「ちょ、凪ちゃん！？」\n「っ！？」 | 「Chờ đã, Nagi!?」\n「!?」 | 「Chờ đã, Nagi!?」\n「Ư!?」 |
| 1431 | 日々姫 | 「――っっ――っ――」 | 「——Ư——Ư——」 | 「——ƯƯ——Ư——」 |

Ghi chú 1431 (không có trong sweep): JP có 3 âm っ (っっ + っ), VN cũ chỉ có 2 Ư — mất 1 âm. Fix "ƯƯ" cho đoạn っっ độc lập (tiền lệ ハチロク15a 1845: っっ → "ƯƯ"; khác 1412 「ぁっ」 nơi っ gắn với tiếng kêu nên không thêm Ư — xem §4).

### §2.2. Thuật ngữ — 1 hàng

- **1366** — monologue: JP 「……副丘の[しめ]〆町で\x%l静態保存;#00ffc040;静態保存%l;#;されていた、レイルロオドを失くした\x%l蒸機;#00ffc040;蒸機%l;#;、旧帝鉄\x%l9600;#00ffc040;9600%l;#;形29611号機。」; TW 「……前帝國鐵路\x%l9600;#00ffc040;９６００%l;#;形２９６１１號\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;已失去鐵路人偶，曾在福岡志免町\x%l静態保存;#00ffc040;靜態保存%l;#;。」; VN cũ: "……Chiếc \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; cũ dòng \x%l9600;#00ffc040;9600%l;#; mang số hiệu 29611 của Đường sắt Hoàng gia đã mất đi Railord,\nđang được \x%l静態保存;#00ffc040;lưu tĩnh%l;#; ở thị trấn Shime, tỉnh Fukuoka."; Sửa: "……Chiếc \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; cũ dòng \x%l9600;#00ffc040;9600%l;#; mang số hiệu 29611 của Teitetsu cũ đã mất đi Railord,\nđang được \x%l静態保存;#00ffc040;lưu tĩnh%l;#; ở thị trấn Shime, tỉnh Fukuoka." — 帝鉄 = "Teitetsu" theo thuật ngữ đã chốt 19/11 (không phải "Đường sắt Hoàng gia" — Hoàng gia là hoàng thất, sai nghĩa; tiền lệ 日々姫08 2342). 旧 → "cũ" ("Teitetsu cũ").

### §2.3. Xưng hô — 2 hàng

- **1859** — ふかみ: JP 「うん、わたしも。朝は和定食で。お昼と夜は洋風で、帰りには逆で食べてみたい」; TW 「嗯，我也是。早上吃日式套餐，中午和晚上吃西餐。返程的時候則是想反過來吃」; VN cũ: 「Ừm, chị cũng vậy. Sáng ăn suất kiểu Nhật. Trưa và tối ăn kiểu Tây,\nlúc về chị muốn ăn ngược lại」; Sửa: 「Ừm, em cũng vậy. Sáng ăn suất kiểu Nhật. Trưa và tối ăn kiểu Tây,\nlúc về em muốn ăn ngược lại」 — Parent sửa 20/11 ~11:50: "mình" → "em". Lý do "trả lời Nagi (dòng kề trước 2111 là Nagi)" của agent là SAI — 2111 cách 1859 ~250 key, thuộc cảnh khác; dòng kề của 1859 là Soutetsu (1857 "À, làm được chứ!") và Hibiki (1856), Nagi nói gần nhất là 1848 (chuyện vòi nước, không liên quan thực đơn). Fukami tự xưng "em" với Soutetsu nhất quán (tiền lệ ふかみh2) và "em" với Hibiki trong chính file này (1831, 1841, 1798); "mình" chỉ dùng với Nagi (tiền lệ 08b: "Mình" 8× vs "Chị" 0× với Nagi). "Chị" cũ sai chắc chắn (Fukami không bao giờ xưng "chị").
- **1721** — ポーレット: JP 「安全面、設備面、メニューのことまで考えられてる、すごく素敵な厨房デザインだって思います」; TW 「不僅在安全上、設施上，連菜單都考慮進去了，我覺得這個廚房設計很完美」; VN cũ: 「Em nghĩ đây là một thiết kế nhà bếp rất tuyệt vời,\nđã cân nhắc đến cả mặt an toàn, thiết bị và thực đơn」; Sửa: 「Chị nghĩ đây là một thiết kế nhà bếp rất tuyệt vời,\nđã cân nhắc đến cả mặt an toàn, thiết bị và thực đơn」 — Paulette khen thiết kế bếp của Hibiki (người thiết kế, đang có mặt; Kimoto vừa khen Hibiki ở 1719; Hibiki đáp ở 1724) — lời khen hướng về Hibiki. Parent kiểm chứng 20/11: dẫn chứng "Hibiki đáp ngay 1874" của agent là SAI — 1874 cách 1721 ~150 key, thuộc cảnh Kisaki bàn chi phí (1872), "Cảm ơn chị!" ở đó nhiều khả năng cảm ơn Kisaki, không phải Paulette; 3 dòng "chị" (1939, 2109, 2231) là xưng hô trong cảnh nhóm (1939 đồng tình với Hibiki 1938; 2109/2231 đáp cả nhóm), không riêng với Hibiki. Fix vẫn đúng vì Paulette tự xưng "chị" với các em gái nhỏ hơn / trong cảnh nhóm, còn "em" chỉ khi 1-1 với Soutetsu (file 03: 9× "em").

### §2.4. Dịch sai nghĩa — 2 hàng

- **2900** — monologue: JP 「移送、修復の手配も済んで、あとは実際、運び込むばかりの状態とも聞く。」; TW 「聽說運送、修復的準備工作也做好了，接下來只等著運回來了。」; VN cũ: "Nghe nói việc sắp xếp di dời, phục chế cũng đã xong,\ngiờ chỉ còn chờ đưa vào thực tế thôi."; Sửa: "Nghe nói việc sắp xếp di dời, phục chế cũng đã xong,\ngiờ chỉ còn chờ vận chuyển nó vào thôi." — 運び込む = đưa/chở vào (đầu máy 29611 chờ vận chuyển vào Bungomori); "đưa vào thực tế" (put into practice) là bịa nghĩa, không có trong JP.
- **2982** — monologue: JP 「おにぎりは――ああ、高菜めしのだ。水筒からはお茶ではなくて――」; TW 「飯糰……啊，是大芥飯糰。水壺裡的不是茶……」; VN cũ: "Cơm nắm là——a, cơm trộn mù tạt.\nTrong bình nước không phải là trà mà là——"; Sửa: "Cơm nắm là——a, cơm trộn cải mù tạt muối.\nTrong bình nước không phải là trà mà là——" — 高菜めし = cơm trộn takana (lá cải mù tạt muối, đặc sản Kyushu); TW 大芥飯糰 xác nhận. "Mù tạt" không là mù tạt chấm (wasabi/mustard), sai hẳn nguyên liệu.

### §2.5. Lỗi nhỏ — 3 hàng

- **1798** — ふかみ: JP 「へぇえ、勉強になります。です！」; TW 「哇啊，我學到了！嗯」; VN cũ: 「Hê, em học hỏi được nhiều điều quá. Ạ!」; Sửa: 「Hê, em học hỏi được nhiều điều quá ạ!」 — です! đứng riêng câu của Fukami bị dịch thành "Ạ" rơi lẻ sau dấu chấm (tiền lệ file 08 key 1934); gộp "ạ" vào câu trước.
- **2169** — ふかみ: JP 「真闇さんがお墨付きをくれたら、つなげる食堂に興味をもってくれる人、きっと、もっと増えます。です」; TW 「要能讓真闇小姐看好，對紐帶食堂感興趣的人肯定會更多的」; VN cũ: 「Nếu chị Mayami đã đảm bảo, thì số người quan tâm\nđến Toa ăn Kết nối chắc chắn sẽ tăng lên nhiều hơn. Ạ」; Sửa: 「Nếu chị Mayami đã đảm bảo, thì số người quan tâm\nđến Toa ăn Kết nối chắc chắn sẽ tăng lên nhiều hơn ạ.」 — cùng mẫu 1798.
- **2992** — monologue: JP 「（ウウウウウウウウーーー）」; TW 「（嗚嗚嗚嗚嗚嗚嗚————）」; VN cũ: "（Uuuuuuuuuuuuuuuuuu———）"; Sửa: "（Uuuuuuuu———）" — còi báo trưa: JP ウ×8 + ー×3, VN cũ U×18 + —×3 — dài gần gấp đôi; sửa về 8 U theo quy tắc độ dài nguyên âm (dấu — giữ nguyên 3, khớp ー×3).

### §2.6. Tag %l thêm — 1 hàng

- **1428** — 双鉄: JP 「……[ぶんごもり,2]文庫森のボランティアさんが言っていた。[せんけい,1]扇形機関庫は、シンボルなのだと」; TW 「……豐後森的志願者也說過，扇形機車庫是豐後森的標誌」; VN cũ: 「……Tình nguyện viên ở Bungomori đã nói.\n\x%l扇形機関庫;#00ffc040;Gara đầu máy hình ngành%l;#; là một biểu tượng」; Sửa: 「……Tình nguyện viên ở Bungomori đã nói.\nGara đầu máy hình ngành là một biểu tượng」 — JP chỉ có ruby [せんけい,1] (furigana), không có thẻ %l; VN tự thêm thẻ gloss (tiền lệ 日々姫08 gỡ 4 thẻ, 08b gỡ 34 thẻ — Gemini tự thêm thẻ). Gỡ thẻ, giữ gloss làm chữ thường. (Gloss "hình ngành" giữ nguyên — xem §6.)

## §3. Kiểm tra cơ học

- TOML: md5 8ce55299b3a69fd4fb5d44de55581a19; chỉ 1 bản sao trên đĩa (không thuộc nhóm 11 file trùng); BOM + CRLF giữ nguyên; 430 khóa script khớp CSV3 tuyệt đối, 0 khóa thừa/thiếu; `[selections]` rỗng (0 mục); comment `# JP:` trong `[script]` 430/430 khớp CSV3 JP tuyệt đối.
- CSV3 vs TOML-2: 287 khác biệt giá trị đều chỉ do TOML-2 làm phẳng literal `\n` thành khoảng trắng — 0 khác biệt thực sự; CSV3 là chuẩn cho fix list.
- Thẻ %l: VN có thẻ ở 6 dòng (1366 ×3, 1892 ×2, 2575 ×2, 1428, 2263, 2609) — 5 dòng khớp JP tuyệt đối, chỉ 1428 là thẻ VN tự thêm (đã sửa §2.6); không có thẻ thiếu dấu `;` đóng trong file này.
- Quét っ: mọi dòng JP có っ đã rà soát — 5 sweep + 1431 đã sửa; còn lại đều là っ nhấn mạnh gắn với từ (2226 あのっ, 1811 えっ, 1413 んっ, 1950/1726/1753/2236/2250 けんっ cuối câu, 2991/2995 SFX đã diễn) — không thêm Ư, đúng quy tắc.
- Ohitoyo: 8 dòng dạng cũ (2247, 1962, 2840 ×2, 2166, 2604, 2605, 2512, 2402) — KHÔNG tính sai, chờ đợt thống nhất (theo tiền lệ 日々姫08: 16 dòng không tính sai, parent đã kiểm chứng 20/11). "Đường sắt Ohito" (1962, 2840) là tên công ty, cũng chờ thống nhất.
- Không có chuỗi xoay vòng nội bộ, không lệch hàng, không contamination chéo file, không orphan, 0 untranslated, 0 duplicate key.

## §4. Đã kiểm tra và giữ nguyên (không tính sai)

- 1412 「……ぁ――ぁっ」 → "……A——A": っ gắn với ぁ (tiếng nấc bị ngắt), không phải gasp độc lập — giữ nguyên (cùng lớp với ハチロク15a 1836/1837 「きゃっ(っ)」).
- 2226/2225 「あのっ！」/「あの――」 → "Cái đó!"/"Cái đó——": giữ — "cái đó" dùng được như từ đệm ngập ngừng trong tiếng Việt khi mở đầu lời nhờ vả, TW cũng dịch 那個.
- 2239 「ほんなら、ね？」 → "Vậy thì, hiểu ý chị chứ?": giữ — ね？ cầu xác nhận, VN diễn thành câu hỏi hàm ý là diễn đạt tự nhiên trong ngữ cảnh (Mayami vừa nói "chúng ta là chị em mà").
- 1789 「ふっ」 → "Hức": giữ — tiếng thở nấc của Hibiki trước khi òa khóc, TW 呼.
- 2991 （すっ――） → （Vút——）, 2995 （こつっ） → （Cộc）: giữ — SFX đã diễn đúng.
- 2126 Kisaki "tôi": giữ — nói trong cuộc họp có Paulette, theo quy tắc Kisaki "tôi" với Paulette.
- 2058 Soutetsu "cảm ơn cô" (với Paulette): giữ — bằng chứng cho quyết định cô/em đang chờ (xem §6), không tự quyết.
- 1941 Paulette "Em cũng tán thành": giữ — người nghe chưa rõ (xem §6, không chắc chắn).
- 2632 độc thoại "Tôi đã thảo luận với cô Yamazaki...": giữ — chủ ngữ JP bỏ lửng, TW cũng dùng ngôi thứ nhất (xem §6, không chắc chắn).
- 1366 "lưu tĩnh" (静態保存): giữ — dùng nhất quán 19× toàn dự án; "gara đầu máy hình ngành" (扇形機関庫, 5 dòng): giữ — thuật ngữ chung 23× toàn dự án (xem §6, câu hỏi cho Hieu).
- 1962 "Đường sắt Kurudai": giữ — theo furigana JP くるだい (TW 久大 là tên khác).
- 1358/2572 "Toa ăn Train": giữ — đã ghi chú ở 日々姫08 §6 (chờ Hieu chốt "Toa ăn Train" vs "Tàu nhà hàng").
- 1429 「収まっております」 → "ổn định": giữ; 1986/2210/2606 "nội bộ" cho 内諾: giữ — nhất quán trong file; 2752 "Tôi yêu Hibiki": giữ — 愛おしい trong ngữ cảnh tình cảm.

## §5. Khối TOML (đã kiểm chứng parse)

```toml
"1366" = "……Chiếc \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; cũ dòng \\x%l9600;#00ffc040;9600%l;#; mang số hiệu 29611 của Teitetsu cũ đã mất đi Railord,\\nđang được \\x%l静態保存;#00ffc040;lưu tĩnh%l;#; ở thị trấn Shime, tỉnh Fukuoka."
"1428" = "「……Tình nguyện viên ở Bungomori đã nói.\\nGara đầu máy hình ngành là một biểu tượng」"
"1431" = "「——ƯƯ——Ư——」"
"1721" = "「Chị nghĩ đây là một thiết kế nhà bếp rất tuyệt vời,\\nđã cân nhắc đến cả mặt an toàn, thiết bị và thực đơn」"
"1798" = "「Hê, em học hỏi được nhiều điều quá ạ!」"
"1832" = "「Ư!」"
"1833" = "「Ư!!!」"
"1834" = "「Ư!!!!」"
"1850" = "「Ư!!?」"
"1859" = "「Ừm, em cũng vậy. Sáng ăn suất kiểu Nhật. Trưa và tối ăn kiểu Tây,\\nlúc về em muốn ăn ngược lại」"
"1900" = "「Chờ đã, Nagi!?」\\n「Ư!?」"
"2169" = "「Nếu chị Mayami đã đảm bảo, thì số người quan tâm\\nđến Toa ăn Kết nối chắc chắn sẽ tăng lên nhiều hơn ạ.」"
"2900" = "Nghe nói việc sắp xếp di dời, phục chế cũng đã xong,\\ngiờ chỉ còn chờ vận chuyển nó vào thôi."
"2982" = "Cơm nắm là——a, cơm trộn cải mù tạt muối.\\nTrong bình nước không phải là trà mà là——"
"2992" = "（Uuuuuuuu———）"
```

Kiểm chứng: khối parse được bằng tomllib, 15 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; tag %l được escape đúng `\\x%l…` nên parse ra đúng giá trị `\x%l…`; `\n` viết `\\n` nên parse ra đúng literal backslash-n của CSV3). Tất cả fix đều 1 dòng, không có `\n` thủ công ngoài literal `\n` của CSV3 (game tự ngắt dòng). Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (xem log build).

## §6. Ghi chú cho Hieu (cần quyết / chờ thống nhất — không tính sai trong audit này)

- Thống nhất "Ohimitera"/"Ohito" → "Ohitoyo" (8 dòng dạng cũ: 2247 "quán cà phê ga Ohimitera", 1962 + 2840 "Đường sắt Ohito" ×3, 2166, 2604, 2605, 2512, 2402 — theo tiền lệ 日々姫08, fix trong đợt thống nhất).
- "Gara đầu máy hình ngành" (扇形機関庫): 5 dòng trong file này (1428, 1892, 2263, 2575, 2609), 23× toàn dự án — 扇形 = hình quạt (fan-shaped); "ngành" (sector-ngành nghề) có vẻ là dịch nhầm "sector" (hình quạt) thành "ngành" (lĩnh vực). Cần Hieu chốt: giữ "hình ngành" (thuật ngữ chung hiện tại) hay đổi toàn dự án sang "hình quạt"?
- Soutetsu gọi Paulette: file này "cô" 1× (2058 "cảm ơn cô", ngữ cảnh công việc) vs "em" 0× — cộng dồn P09–15: "cô" 43× vs "em" 7× (P09 7:1, P10 20:2, P11 9:0, P12 7:0, P13 0:2, P14 0:1, P15 0:1; file này +1 "cô"). Vẫn chờ Hieu chốt thống nhất "em" hay giữ "cô" theo ngữ cảnh.
- Không chắc chắn 1 — 2632 (monologue): JP 「山崎さんと、山崎さんが紹介してくれた厨房設備士さんと相談し、徹底的な検討をした。」 — chủ ngữ bỏ lửng; TW cũng dùng ngôi thứ nhất 「我找山崎小姐……」; VN cũ "Tôi đã thảo luận với cô Yamazaki..." (ngôi thứ nhất = Soutetsu, người kể chuyện). Nhưng nội dung là công việc thiết kế bếp của Hibiki (2749: Hibiki học từ cô Yamazaki trong bếp) — chủ ngữ có thể là Hibiki ("Em ấy đã thảo luận..."). Không sửa, cần Hieu kiểm tra trong game.
- Không chắc chắn 2 — 1941 (ポーレット): JP 「わたしも、賛成です。」 — VN cũ "Em cũng tán thành." Người nghe chưa rõ: Hibiki (người đề xuất tên → "chị"), Kisaki (người vừa khen tên → "tôi" theo tiền lệ file 09 key 1718), hay Soutetsu (→ "em"). Không sửa, cần Hieu kiểm tra trong game.
- Lượt soát 2: 15/15 tái kiểm chứng, 0 bỏ, 0 sửa. Parent kiểm chứng 20/11 ~11:50: 1 fix sửa lại (1859 "mình"→"em" — xem §2.3; lý do "trả lời Nagi" của agent sai, dẫn chứng 2111 không đúng); 1 dẫn chứng sửa lại (1721: bỏ "Hibiki đáp ngay 1874", xem §2.3). JSON 15 khóa chuỗi; khối TOML parse OK, 15 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 15/15.

## Kết bài

File 日々姫07_姉の想い。妹の想い: 430 dòng đã đọc hết, **15 dòng sai (3,5%)** — 6 gasp っ (5 sweep + 1 tự tìm), 1 thuật ngữ, 2 xưng hô, 2 dịch sai nghĩa, 3 lỗi nhỏ, 1 thẻ %l thêm. Không có chuỗi xoay, không lệch hàng, không lỗi đại từ hệ thống — file khá sạch, lỗi tập trung ở SFX và các chi tiết nhỏ. JSON 15 khóa chuỗi; khối TOML parse OK, 15 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 15/15; lượt soát 2: 15/15, 0 bỏ, 0 sửa.
