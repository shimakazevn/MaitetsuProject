# Audit — 日々姫09_run_with_our_dreams (02_Hibiki) — 10/378 (2,6%)

File: `日々姫09_run_with_our_dreams.txt.toml` — route 02_Hibiki, 378 dòng script.
Disk: `sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59eb09_run_with_our_dreams.txt.toml` (tên file #U-escaped, đúng như trên đĩa).
Nội dung: lễ cưới của Soutetsu và Hibiki trên GAMADUS (lễ 人前式 trước mặt mọi người): lời thề, trao nhẫn, nghi thức uống rượu giao bôi San-san-kudo, bài phát biểu với họ hàng/đối tác làm ăn; Mikuro gặp lại Hachiroku; Soutetsu–Hibiki rời đi hưởng tuần trăng mật trên Navi.
Nhân vật: monologue 148, 双鉄 78, ハチロク 34, 日々姫 25, みくろ 17, ポーレット 12, 凪 11, ふかみ 11, 真闇 11, 赤井 10, 稀咲 8, れいな 7, ナビ 4, 斎藤 1, 山崎 1.

Phương pháp: đọc toàn bộ 378 dòng theo từng hàng, đối chiếu JP + TW (CSV3), kiểm tra cơ học thêm (xem §3). Key order trong TOML == CSV3 order (xáo trộn, không phải story order) — người nghe/đại từ xác định theo nội dung và dòng kề trong luồng truyện, không theo key. Cơ sở tổng cộng đã kiểm chứng lại với ROUTE-AUDIT.md trước khi viết snippet: 88 file / 4.469 dòng sai — khớp với số parent giao.

## §1. Kết quả

Sai: **10/378 (2,6%)**.

Phân loại (10):
- **sfx — tiếng cười bị dịch thành tiếng rên**: 3 (1695, 1736, 1738 — うふふ/うふふぅ bị dịch "Ư fufu"; tiếng cười là cười, KHÔNG phải gasp).
- **gasp っ (sweep, đã kiểm chứng)**: 2 (1778 lost-gasp-whole, 2478 lost-gasp-trailing — áp nguyên fix sweep).
- **sai nghĩa**: 2 (2070 — thì giả định bị dịch thành hiện tại + "Dịch vụ"; 2366 — 指を立てる "giơ ngón tay" bị cụ thể hoá thành "ngón tay cái").
- **xưng hô — độc thoại Soutetsu "anh" → "tôi"**: 2 (2390, 2735 — độc thoại kể chuyện đồng nhất "tôi" trong cả file, 2 dòng này lạc sang "anh" không có người nghe).
- **thuật ngữ — tên riêng không nhất quán trong file**: 1 (2483 — ガマダス "Gamadas", 6 dòng còn lại trong file đều dùng "GAMADUS").

Thoại 5/230 (2,2%), độc thoại 5/148 (3,4%). Theo nhân vật: monologue 5, ハチロク 2, ふかみ 2, れいな 1.

Không misaligned / không rotation / không contamination chéo file / không orphan / 0 untranslated / 0 duplicate key. Không lỗi đại từ hệ thống: Soutetsu "anh" với Hibiki xuyên suốt trong thoại (0 dòng "tôi" tự xưng trong thoại với Hibiki — đã quét toàn bộ thoại 双鉄; 2 dòng "chúng tôi" 1996/2076 là đại từ nhóm, dạng trung lập — giữ). Không chắc chắn: 0.

Sweep っ-gasp: 2 mục cho file này trong `sweep-raw-gasp-wrong.json` (1778, 2478) — đã kiểm chứng từng mục với JP và áp dụng cả 2. Audit quét thêm toàn bộ 144 dòng JP có っ và không tìm thêm gasp nào bị sót; các っ còn lại đều là nhấn mạnh gắn với từ (1920 今すぐに行くっ, 2023 もちろんっ, 1797 うむっ, 1844 はいっ, 2115 あらっ) hoặc đã diễn bằng dấu câu/âm đóng — không thêm Ư, đúng quy tắc.

Strong candidates 5 → đọc toàn bộ tìm ra 10 sai: heuristic chỉ đếm được một phần. Lưu ý: 3/5 cờ strong-candidate (1633, 1845, 2036) là CŨ — giá trị VN trong `audit-strong-candidates.json` thuộc về key khác trong cùng file (1633 lấy VN của 1752, 1845 lấy VN của 1770, 2036 lấy VN của 1781); trong CSV3/TOML cả 3 dòng đều đã đúng (1633 Kisaki "chị cũng tán thành ý kiến của Nagi" khớp JP 「ボクも、凪くんに賛成だ」; 1845 Mikuro "Vâng, Mikuro sẽ đợi ạ!!!" khớp JP; 2036 Nagi khớp JP 「そぎゃん奴らに遠慮するこたなかとばい！」). 1854 chỉ khác ngắt dòng (candidates ghi literal \\n lệch vị trí), nội dung khớp. 2125 khớp và đã đúng. Không có chuỗi xoay vòng trong file này.

## §2. Các lỗi và cách sửa

- **1695** — ハチロク: JP "「ジューンブライド。サムシングフォー。うふふっ、\n素敵な縁起を詰め込んだ。今日はまことに佳き日ですね」"; TW "「六月新娘，婚禮四寶。呵呵，象徵吉利的元素都集齊了。今天真是個大好日子」"; VN cũ: "「Cô dâu tháng Sáu. Something Four. Ư fufu,\nGói gọn những điềm lành tuyệt vời nhất. Hôm nay quả thực là một ngày tốt lành ạ.」"; Sửa: "「Cô dâu tháng Sáu. Something Four. Fufu,\nGói gọn những điềm lành tuyệt vời nhất. Hôm nay quả thực là một ngày tốt lành ạ.」" — JP うふふっ là tiếng cười; VN cũ "Ư fufu" thêm gasp "Ư" vào trước tiếng cười là sai quy tắc Hieu 22:05 (cười là cười, KHÔNG diễn thành rên). Sửa "Fufu" (cùng file, monologue 2364 ふふ → "Fufu" đã đúng).
- **1736** — ハチロク: JP "「うふふ、みくろはどう感じましたか？」"; TW "「呵呵，你感覺怎麼樣？」"; VN cũ: "「Ư fufu, Mikuro thấy thế nào?」"; Sửa: "「Fufu, Mikuro thấy thế nào?」" — như 1695: うふふ là cười, bỏ "Ư".
- **1738** — れいな: JP "「うふふぅ、おしあわせですねぇ」"; TW "「呵呵，真幸福啊」"; VN cũ: "「Ư fufu, hạnh phúc quá nhỉ~」"; Sửa: "「Fufuu, hạnh phúc quá nhỉ~」" — như 1695, bỏ "Ư"; ぅ kéo dài → thêm một u ("Fufuu", theo công thức độ dài nguyên âm).
- **1778** — ふかみ: JP "「っ！！？」"; TW "「啊？！」"; VN cũ: "「!!?」"; Sửa: "「Ư!!?」" — Sweep lost-gasp-whole — đã kiểm chứng: JP toàn dòng chỉ có っ + dấu câu; VN cũ chỉ còn dấu câu. Áp nguyên fix sweep.
- **2070** — ふかみ: JP "「クマ川くだり、それからわたしも。\nどうなってたか、わからないです」"; TW "「要是沒有你們的話，我都不知道自己會怎麼樣，更別說隈河漂流的事了」"; VN cũ: "Dịch vụ chèo thuyền trên sông Kuma, và cả em nữa.\nKhông biết giờ đã ra sao rồi."; Sửa: "Chuyến chèo thuyền trên sông Kuma, và cả em nữa.\nKhông biết mọi chuyện đã ra sao nữa rồi." — JP どうなってたか là giả định quá khứ ("không biết đã thành ra thế nào [nếu không có mọi người]"), TW xác nhận (要是沒有你們的話…都不知道自己會怎麼樣); VN cũ "Không biết giờ đã ra sao rồi" đổi thành thì hiện tại là sai nghĩa. "Dịch vụ chèo thuyền" → "Chuyến chèo thuyền": JP クマ川くだり là chuyến chèo thuyền/xuôi dòng sông Kuma, không phải "dịch vụ".
- **2366** — monologue: JP "ハチロクが笑う。みくろが手を振る。\n木本さんは会釈をし、栃木さんは指を立てる。"; TW "八六微笑致意。美玖路招手回應。木本先生微微欠身，而櫪木先生則豎起了手指。"; VN cũ: "Hachiroku cười. Mikuro vẫy tay.\nAnh Kimoto cúi chào, còn anh Tochigi thì giơ ngón tay cái lên."; Sửa: "Hachiroku cười. Mikuro vẫy tay.\nAnh Kimoto cúi chào, còn anh Tochigi thì giơ ngón tay lên." — JP 指を立てる chỉ nói "giơ ngón tay" (không ghi là ngón nào); TW cũng dịch chung "豎起了手指". VN cũ thêm "cái" (ngón cái) là cụ thể hoá không có trong JP. Sửa về dạng chung.
- **2390** — monologue: JP "愛するどころか、心を動かすことさえも。\nそれが路子に対する贖罪なのだと、感じてさえいた。"; TW "別說愛一個人了，我的內心根本不會產生一絲漣漪。我甚至認為這就是對路子的贖罪。"; VN cũ: "Đừng nói là yêu, ngay cả việc rung động anh cũng không thể.\nAnh thậm chí còn cảm thấy đó là sự chuộc tội dành cho Michiko."; Sửa: "Đừng nói là yêu, ngay cả việc rung động tôi cũng không thể.\nTôi thậm chí còn cảm thấy đó là sự chuộc tội dành cho Michiko." — Độc thoại Soutetsu kể chuyện: cả file đồng nhất "tôi" (146/148 dòng độc thoại); 2 dòng này dùng "anh" không có người nghe (đang nghĩ về Michiko) là lạc giọng. Sửa "tôi" cả 2 câu.
- **2478** — monologue: JP "頷いている。僕もまた。\n栃木さんも、木本さんも――っ！！"; TW "我也深有同感。櫪木先生和木本先生一定也一樣——！！"; VN cũ: "Tôi gật đầu. Tôi cũng vậy.\nCả anh Tochigi, cả anh Kimoto cũng vậy――!!"; Sửa: "Tôi gật đầu. Tôi cũng vậy.\nCả anh Tochigi, cả anh Kimoto cũng vậy――Ư!!" — Sweep lost-gasp-trailing — đã kiểm chứng: JP ――っ cuối câu; VN cũ giữ dấu gạch nhưng mất gasp. Áp nguyên fix sweep.
- **2483** — monologue: JP "ガマダス屋上へと駆け上がる。\n日々姫とならんで、二人一緒に、それぞれの足で。"; TW "我們一起跑上了ＧＡＭＡＤＵＳ的屋頂。我和日日姬肩並肩，齊頭並進。"; VN cũ: "Chúng tôi chạy lên sân thượng Gamadas.\nSánh bước cùng Hibiki, cả hai cùng nhau, trên chính đôi chân của mình."; Sửa: "Chúng tôi chạy lên sân thượng GAMADUS.\nSánh bước cùng Hibiki, cả hai cùng nhau, trên chính đôi chân của mình." — ガマダス trong file này: 1804, 1831, 1895, 2016, 2143, 2522, 2703 đều dịch "GAMADUS"; chỉ 2483 viết "Gamadas". Sửa cho nhất quán trong file.
- **2735** — monologue: JP "その繰り返しは、僕にも笑顔を与えてくれた。\n僕の世界を、日々姫は笑顔で、色づけてくれた。"; TW "這個不斷重複的過程也給我帶來了笑容。日日姬用笑容給我的世界刷上了色彩。"; VN cũ: "Sự lặp lại đó, cũng đã mang đến cho anh nụ cười.\nHibiki đã dùng nụ cười của mình, tô điểm cho thế giới của anh."; Sửa: "Sự lặp lại đó, cũng đã mang đến cho tôi nụ cười.\nHibiki đã dùng nụ cười của mình, tô điểm cho thế giới của tôi." — Như 2390: độc thoại Soutetsu, "anh" không có người nghe, lạc giọng so với "tôi" xuyên suốt file. Sửa "tôi" cả 2 câu.

## §3. Kiểm tra cơ học

- TOML: md5 2d9aa6b8e0b73c690a22d2a2f40c7c85; chỉ 1 bản sao trên đĩa (không thuộc nhóm 11 file trùng); BOM + CRLF giữ nguyên; 378 khóa script khớp CSV3 tuyệt đối, 0 khóa thừa/thiếu; `[selections]` rỗng (0 mục); 378/378 comment `# JP:` trong `[script]` khớp CSV3 JP tuyệt đối (25 comment `# JP:` còn lại thuộc `[characters]`/`[character_subs]`, không phải dòng script).
- CSV3 vs TOML-2: chỉ 1 khác biệt giá trị (1753) — TOML-2 làm phẳng literal `\n` thành khoảng trắng, 0 khác biệt thực sự; CSV3 là chuẩn cho fix list.
- Thẻ %l: 0 thẻ sai định dạng trong file; số thẻ VN == JP ở mọi dòng; 0 thẻ thiếu dấu `;` đóng trong file này.
- Quét っ: toàn bộ 144 dòng JP có っ đã rà soát — 2 sweep đã sửa (1778, 2478); còn lại đều là っ nhấn mạnh gắn với từ hoặc đã diễn bằng dấu câu/âm đóng (xem §4) — không thêm Ư, đúng quy tắc.
- Đại từ: quét toàn bộ thoại 双鉄 — 0 dòng "tôi" tự xưng trong thoại (1996, 2076 là "chúng tôi" nhóm, giữ); độc thoại "anh" tự xưng chỉ 2 dòng 2390/2735 (đã sửa). Kisaki 1633 "chị" với Nagi: giữ (xem §4).
- Không có chuỗi xoay vòng nội bộ: giá trị VN trùng duy nhất là "「Vậy thì.」" ở 1839 (Akai 「さて」) và 2113 (Mayami 「ほんなら」) — JP khác nhau, cùng dịch ngắn là bình thường, không phải lệch hàng. Không lệch hàng, không contamination chéo file (xem dưới), không orphan, 0 untranslated, 0 duplicate key.
- Contamination chéo file: quét toàn bộ VN của file qua chỉ mục VN dự án (CSV3) — 30 VN trùng ngắn (lời cảm thán chung như "「Ngài Soutetsu!?」", "「A.」") là trùng hợp hợp lệ; 1 VN dài trùng (2077 "「Xin lỗi vì đã để mọi người phải đợi.」" cũng có ở lr稀咲追加01 key 1163) — đã kiểm chứng: JP bên kia là 「おまたせしてすみません」 cùng nghĩa xin lỗi, trùng hợp hợp lệ, không phải contamination.
- Thuật ngữ dạng cũ (KHÔNG tính sai, chờ đợt thống nhất): 御一夜 "Ohimitera" 3 dòng (1906, 2400, 2708); 帝鉄 "Đường sắt Hoàng gia" 4 dòng (1687, 1906, 2046, 2095); 湯医 "Yui" 2 dòng (1640, 2708); 宮司 "cha xứ" 3 dòng (2636, 2699, 2751); 右田一酒造元 "Xưởng rượu Migita" thiếu "Ichi" 1 dòng (1840).

## §4. Đã kiểm tra và giữ nguyên (không tính sai)

- 1739 Fukami 「わぁぁ」 → "Oa.": giữ — "Oa" là cách diễn tiếng ngạc nhiên trong tiếng Việt, chấp nhận được theo quy tắc SFX ngẫu hứng (không dập khuôn 1:1).
- 1741 Reina 「ふわぁ。そうてつさん、かーっこいいですぅ」 → "Oa. Anh Soutetsu, ngầu quá đi ạ~": giữ — như 1739.
- 1767 Hibiki 「はうっ」 → "Hauu": giữ — diễn đủ âm はう + っ.
- 1815 Fukami 「ああ、いわれてみたら……結婚式場として作られてるわけじゃないんですよね。です」 → "…đâu nhỉ. Ạ.": giữ — "Ạ." cuối câu diễn tiếng ấp úng です thừa, hơi gượng nhưng không sai nghĩa; không sửa theo phong cách.
- 2040 Soutetsu 「――っ、っと。\nほら」 → "――Ây, da.\nĐây này.": giữ — っ đây là tiếng vấp/lúng túng, "Ây, da" diễn được.
- 2115 Hachiroku 「左様でしたらなによりです――あらっ！？」 → "Được vậy thì còn gì bằng ạ――Ây da!?": giữ — あらっ là tiếng ngạc nhiên, "Ây da" chấp nhận được.
- 2506 monologue 「僕が指輪を取ると同時に、日々姫も指輪を握りしめる。」 → "…Hibiki cũng nắm chặt lấy chiếc nhẫn còn lại.": giữ — có 2 chiếc nhẫn, Soutetsu lấy 1 chiếc thì chiếc của Hibiki là "chiếc còn lại" là suy ra hợp lý, không bịa nghĩa.
- 1633 Kisaki 「いや――みんなで、という点は置いておき、\nボクも、凪くんに賛成だ」 → "…chị cũng tán thành ý kiến của Nagi.": giữ — Kisaki tự xưng "chị" với Nagi (lớn tuổi hơn Nagi, gọi Nagi là 凪くん); quy tắc "em với Soutetsu / tôi với Paulette" không phủ trường hợp này, và "chị" là cách xưng hợp lý.
- 1996/2076 "chúng tôi" — giữ: đại từ nhóm, dạng trung lập theo brief (không theo quy tắc số ít).
- 2125 Hibiki 「ねぇねから！？」 → "Từ chị Mayami sao!?": giữ — ねぇね = chị (Mayami), đúng.
- 2439 monologue 「宝生稀咲女史」 → "Bà Houshou Kisaki": giữ — 女史 là kính ngữ trang trọng cho nữ quan chức (Phó thị trưởng), "Bà" chấp nhận được trong ngữ cảnh trang trọng.
- 1785 「んっ――」 → "Ưm——", 1801 「んっ！！！」 → "Ưm!!!", 1797 「うむっ！」 → "Ừm!", 1920 「今すぐに行くっ！」 → "Anh đến ngay đây!", 2023 「もちろん――もちろんっ！」 → "Tất nhiên――Tất nhiên rồi ạ!": giữ — っ nhấn mạnh gắn với từ, đã diễn đúng, không thêm Ư.

## §5. Khối TOML (đã kiểm chứng parse)

```toml
[script]
"1695" = "「Cô dâu tháng Sáu. Something Four. Fufu,\\nGói gọn những điềm lành tuyệt vời nhất. Hôm nay quả thực là một ngày tốt lành ạ.」"
"1736" = "「Fufu, Mikuro thấy thế nào?」"
"1738" = "「Fufuu, hạnh phúc quá nhỉ~」"
"1778" = "「Ư!!?」"
"2070" = "「Chuyến chèo thuyền trên sông Kuma, và cả em nữa.\\nKhông biết mọi chuyện đã ra sao nữa rồi。」"
"2366" = "Hachiroku cười. Mikuro vẫy tay.\\nAnh Kimoto cúi chào, còn anh Tochigi thì giơ ngón tay lên."
"2390" = "Đừng nói là yêu, ngay cả việc rung động tôi cũng không thể.\\nTôi thậm chí còn cảm thấy đó là sự chuộc tội dành cho Michiko."
"2478" = "Tôi gật đầu. Tôi cũng vậy.\\nCả anh Tochigi, cả anh Kimoto cũng vậy――Ư!!"
"2483" = "Chúng tôi chạy lên sân thượng GAMADUS.\\nSánh bước cùng Hibiki, cả hai cùng nhau, trên chính đôi chân của mình."
"2735" = "Sự lặp lại đó, cũng đã mang đến cho tôi nụ cười.\\nHibiki đã dùng nụ cười của mình, tô điểm cho thế giới của tôi."
```

Kiểm chứng: khối parse được bằng tomllib, 10 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\n` viết `\\n` nên parse ra đúng literal backslash-n của CSV3). Tất cả fix đều giữ nguyên ngắt dòng literal `\n` của VN cũ (không thêm `\n` thủ công mới). Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (1695/1736/1738 bỏ "Ư" trước tiếng cười; 1778/2478 thêm "Ư"; 2070 dịch lại 2 dòng; 2366 bỏ "cái "; 2390/2735 "anh"→"tôi"; 2483 "Gamadas"→"GAMADUS").

## §6. Ghi chú cho Hieu (cần quyết / chờ thống nhất — không tính sai trong audit này)

- Thống nhất thuật ngữ (chờ đợt thống nhất): "Ohimitera" → "Ohitoyo" (3 dòng: 1906, 2400, 2708); "Đường sắt Hoàng gia" → "Teitetsu" (4 dòng: 1687, 1906, 2046, 2095); "Yui" → "Yunoi" (2 dòng: 1640, 2708); "cha xứ Akai" → "đền chủ" (3 dòng: 2636, 2699, 2751); "Xưởng rượu Migita" → "Migita Ichi" (1 dòng: 1840).
- 2010 Fukami 「おじいちゃんのトラック！？」 → "Xe tải của ông nội!?": giữ nguyên "ông nội" — liên quan câu hỏi đang chờ Hieu chốt (08c: Seki gọi "ông nội" hay "ông ngoại"); nếu Hieu chốt "ông ngoại" thì dòng này đổi theo.
- SFX 1738 "Fufuu" và 1695/1736 "Fufu" là diễn tiếng cười theo quy tắc Hieu 22:05/22:19 — nếu Hieu muốn cách diễn khác thì đổi.
- Lượt soát 2: 10/10 tái kiểm chứng, 0 bỏ, 0 sửa lại. JSON 10 khóa chuỗi; khối TOML parse OK, 10 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 10/10.
- **Parent sửa khi gộp (20/11 ~12:45): fix 2070 của agent làm rơi cặp 「」 của câu thoại (bản nháp dịch lại 2 dòng nhưng mất dấu ngoặc) — đã khôi phục 「…。」 trong JSON và khối TOML; nội dung dịch giữ nguyên, tổng số fix không đổi (10).**

## Kết bài

File 日々姫09_run_with_our_dreams: 378 dòng đã đọc hết, **10 dòng sai (2,6%)** — 3 sfx tiếng cười bị thêm gasp, 2 gasp っ (sweep), 2 sai nghĩa, 2 xưng hô độc thoại, 1 thuật ngữ tên riêng. Không có chuỗi xoay, không lệch hàng, không contamination, không orphan — file khá sạch, lỗi tập trung ở SFX và 2 dòng độc thoại lạc giọng. JSON 10 khóa chuỗi; khối TOML parse OK, 10 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 10/10; lượt soát 2: 10/10, 0 bỏ, 0 sửa.
