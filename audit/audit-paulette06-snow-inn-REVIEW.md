# Audit: Paulette 06_雪の宿 — 14 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/ポーレット06_雪の宿.txt.toml` — 432 dòng script, **14 dòng Việt sai = 3,2%**, 0 dòng chưa chắc chắn.
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. Đây là file thứ 16 audit toàn bộ, sau 廃炭鉱 31%, obasan 56%, Grand 01 45,6%, Hibiki 03 86,2%, Hachiroku 13 夜の嵐 44,9%, 実りの秋 0,4%, Nagi_Fukami 08a 4,3%, Hachiroku 12 ムナカタ来訪 2,3%, 再開発 4,4%, Paulette 04_ヒヤリング 1,8%, stove 22,1%, Paulette 05_whatsentertainment 2,8%, 鳴呼の町 5,0%, Grand Rewrite 04 3,9%, Paulette 06_おひとよマイントレジャー 6,8%.

## Phương pháp và số liệu kiểm chứng
- Đã đọc **hết 432/432 dòng script** (key 1293–2863), đối chiếu từng dòng với JP + TW theo nghĩa, người nói, thoại/lời dẫn, xưng hô độc thoại theo quy ước của chính file. Không ngoại suy tổng dự án từ file này.
- Phân loại 14 dòng sai: **xưng hô 8** (1331, 1854, 1879, 1954, 1997, 2048, 2070, 2132), **sai nghĩa 3** (1736, 2158, 2159), **lỗi nhỏ 3** (1835, 1846, 2672). Lệch vị trí 0, chưa dịch 0, cụt câu 0, không chắc chắn 0.
- Thoại sai 13/273 (4,8%); lời dẫn (monologue) sai 1/159 (0,6%). Theo người nói: Soutetsu 8, Paulette 3, Hikari 2, monologue 1; Reina, nhân viên phục vụ (仲居) 0.
- Phân bố lỗi theo đoạn: key 1331–1997: 8 dòng; 2048–2159: 5 dòng; 2672: 1 dòng — lỗi rải đều cả file, không tập trung một cảnh nào.
- **Heuristic thoại/dẫn báo 0 dòng** — bắt được **0/14 dòng sai (0%)**: toàn bộ lỗi đều ở mức xưng hô, từ/câu hoặc tiếng kêu ngắn, những thứ heuristic không thể thấy. Heuristic cũng báo 0 dòng ở Grand 04; file treasure kề trước báo 2 dòng nhưng chỉ 1 là lỗi thật và vì lý do khác (xem audit file kia).
- **Không có key-shift sạch:** test shift −2..+2 trên dấu thoại/dẫn, shift 0 khớp hoàn hảo (432/432 = 1,000). Không có bằng chứng lệch đều; lỗi xác nhận bằng đọc ngữ nghĩa từng dòng + đối chiếu chỉ mục Việt toàn dự án.
- **TOML và CSV giống hệt nhau về nội dung:** kiểm tra toàn bộ 432 dòng, 0 dòng khác nội dung thực (250 dòng chỉ khác `\n`/khoảng trắng — theo quyết định của Hieu ngày 19/11, `\n` thủ công không quan trọng vì game tự xuống dòng). Không có dòng CSV trống nào trong file này. VN==TW: 0 dòng.
- **Không xét lỗi định dạng `\n`:** chỉ báo lỗi nội dung. Các bản sửa trong khối TOML bên dưới viết liền một dòng.
- **[selections]:** file có tiêu đề section `[selections]` nhưng **rỗng (0 mục)** — không có lựa chọn nào để kiểm tra hay sửa.
- **Thẻ `%l`:** 1 dòng VN thêm thẻ so với JP — 2045 (Paulette thêm thẻ gloss Aircra cho エアクラ mà JP không có thẻ; chữ hiển thị đúng, theo tiền lệ ở Nagi 08a và stove thì chỉ ghi nhận quan sát, không tính lỗi). Không có dòng nào VN làm mất thẻ của JP. Dấu gạch ―― trong bản sửa viết không khoảng trắng hai bên, theo quy ước dự án.
- **Không trùng file:** file này chỉ xuất hiện một lần trong zip, chỉ trong thư mục `03_Paulette/` — không có bản sao y hệt ở thư mục khác như Grand Rewrite 04.

## Kết luận về cơ chế lỗi
- **Không có lệch vị trí nào trong file này** — file thứ ba liên tiếp (sau Grand 04 và treasure) hoàn toàn không có dòng nào bị dán nhầm. 0 dòng mồ côi, 0 cặp chuyển chỗ, 0 tràn chương. Mọi câu Việt sai đều đứng đúng key của nó, chỉ sai ở mức xưng hô/từ/câu.
- **8/14 lỗi là xưng hô, và 5 trong số đó là một mẫu duy nhất: Soutetsu tự xưng "anh" khi nói với Paulette** (1854, 1954, 2048, 2070, 2132). File này Soutetsu dùng cả "tôi" (8 chỗ trong thoại, vd 1984, 1993) lẫn "anh" (5 chỗ) khi nói với cùng một người nghe là Paulette — không có cách phân biệt theo người nghe hay theo cảnh, nên "anh" ở đây là không nhất quán, không phải quy ước riêng của file. Theo docs (locations §2.1) Soutetsu xưng "Tôi", chỉ dùng "Anh" khi nói với em gái Hibiki (Hibiki không xuất hiện trong file này). Lưu ý: ở file treasure cùng chương 06, Soutetsu gọi Paulette "cô" (2047) còn ở file này gọi "em" (1738, 1742, 2226) — xem mục Đề xuất context mới.
- **3 lỗi xưng hô còn lại đều là lỗi "địa chỉ" (gọi sai người):** 1331 Hikari gọi ba mình là "cậu", 1879 Paulette gọi con gái mình là "bạn ấy", 1997 Paulette tự xưng "chị" trước mặt Soutetsu/Hikari — cả ba đều là những chỗ dịch giả chọn đại từ mà không kiểm tra quan hệ người nói–người nghe trong cảnh. Ngược lại, những chỗ khó tương tự trong file đều dịch đúng sẵn có: Hikari gọi Soutetsu "ba" (1768, 1772), Soutetsu gọi Hikari "con" (2208), Reina gọi Paulette "chị Paulette" (1818, 2105), Paulette xưng "mẹ" trước Hikari (1929, 2210, 2221).
- **Lỗi nghĩa đáng chú ý nhất là cặp 2158/2159 (端的):** cả từ cần giải thích lẫn từ lặp lại của Hikari đều bị dịch sai thành "Thẳng thắn" — trong khi chính câu giải thích trong dòng ("nói một cách đơn giản") và TW (簡而言之, "nói ngắn gọn") đều chỉ ra nghĩa đúng là "Ngắn gọn". Đây là lỗi dịch từ mà không đối chiếu với phần giải nghĩa ngay trong câu.
- 418 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Chi tiết 14 dòng sai

### A. Xưng hô (8 dòng)
Quy ước docs (locations §2.1): Soutetsu xưng "Tôi" (chỉ dùng "Anh" khi nói với em gái Hibiki); Paulette xưng "Tôi"/"Em" (xưng "mẹ" trước Hikari).
- **1331** (Soutetsu, đang thuật lại tâm trạng của Hikari): JP 「……『悪いのは人間なんだって、一緒に責めて欲しかった』」 / TW 「……"我想讓你認為，錯的一直都是人類，希望你跟我一起責備人類"」 — Soutetsu đang nói hộ điều Hikari muốn: cô bé muốn ba cùng mình đổ lỗi cho con người. VN cũ "Mình đã muốn **cậu** cùng mình đổ lỗi" — "cậu" là cách gọi bạn ngang hàng, trong khi Hikari gọi Soutetsu là "ba" suốt file này (1768 "Ba nè", 1772 "Đừng hỏi ba"). Sửa thành "Mình đã muốn **ba** cùng mình đổ lỗi".
- **1854** (Soutetsu, nói với Paulette): JP 「うん。驚いたからな。すれ違いから、僕らは絆を結べたのだと、知って」 — "Vì **anh** đã rất ngạc nhiên mà" — tự xưng "anh" với Paulette, trong khi file này Soutetsu cũng xưng "tôi" với Paulette ở 1984 ("Tôi cũng đoán vậy") và 1993 ("Tôi không định bắt bẻ đâu"). Sửa thành "Vì **tôi** đã rất ngạc nhiên mà".
- **1879** (Paulette, hỏi về điều Hikari vừa nói): JP 「ね？　今なんていってたの？ママにもおしえて」 / TW 「嗯？你們剛才說什麼啦？跟媽媽也說說吧」 — người vừa nói là Hikari (1870), Paulette hỏi lại với tư cách mẹ. VN cũ "**Thấy chưa?** Lúc nãy **bạn ấy** nói gì vậy?" — "bạn ấy" là cách gọi bạn bè, một người mẹ không gọi con gái mình như vậy; "Thấy chưa?" cũng lệch nghĩa ね？ (tag "này/right?"). Sửa thành "**Nè?** Lúc nãy **con bé** nói gì vậy?"
- **1954** (Soutetsu, nói với Paulette): JP 「怖くて、面白くて、難しい。けれど、一番大事なことは、ひとつだと思う」 — "Nhưng, **anh nghĩ** điều quan trọng nhất chỉ có một thôi" — tự xưng "anh" với Paulette. Sửa thành "Nhưng, **tôi nghĩ**...".
- **1997** (Paulette): JP 「れいなは……とっても上手だと思う。『相手に伝わるように伝える』の」 — Paulette đang nói về Reina với Soutetsu (câu tiếp 1998 "con bé" = Reina). VN cũ "**Chị nghĩ**... Reina làm việc đó rất giỏi" — tự xưng "chị": nói với Soutetsu thì phải là "em", nói với Hikari thì phải là "mẹ"; "chị" sai với cả hai người nghe có thể. Sửa thành "**Em nghĩ**...".
- **2048** (Soutetsu, nói với Paulette): JP 「だったと思うし、そうがんばった。けれどお互い、自分にとって都合がいいよう誤解した」 — "**Anh nghĩ** là vậy" — tự xưng "anh" với Paulette. Sửa thành "**Tôi nghĩ** là vậy".
- **2070** (Soutetsu, chúc Paulette ngủ ngon): JP 「おやすみ、僕のポーレット」 / TW 「晚安，我的波萊特」 — "Ngủ ngon nhé, Paulette **của anh**" — sở hữu cách "của anh" cũng là tự xưng "anh" với Paulette. Sửa theo docs thành "Paulette **của tôi**". (Lưu ý: "của anh" nghe tự nhiên hơn trong tiếng Việt vợ chồng — nếu Hieu muốn giữ sắc thái thân mật thì đây là một câu hỏi về docs, xem mục Đề xuất context mới.)
- **2132** (Soutetsu): JP 「僕もだが、ポーレットもいっそう子供だったろう。一目惚れだなんだというには――」 — VN cũ "**Anh thì không nói**, nhưng Paulette lúc đó còn rất nhỏ mà" — vừa tự xưng "anh" với Paulette, vừa dịch 僕もだが ("tôi cũng vậy") thành thành ngữ "anh thì không nói" gây khó hiểu. Sửa thành "**Tôi cũng vậy thôi**, nhưng Paulette lúc đó còn rất nhỏ mà."

### B. Sai nghĩa (3 dòng)
- **1736** (Paulette): JP 「でも、そのいつかを、少しでも早めてあげたいですよね。だって、こんなに素敵なんだから」 / TW 「但是，我希望那一天能早日到來。因為，與他人的交流是如此美好」 — chủ ngữ là Paulette (cô muốn ngày đó đến sớm hơn — nói về việc Hikari sẽ có ngày như vậy). VN cũ "Nhưng mà, **anh cũng muốn** ngày đó đến sớm hơn một chút đúng không" — gán mong muốn sang cho Soutetsu ("anh") và biến câu thành câu hỏi. Sửa thành "Nhưng mà, **em muốn** ngày đó đến sớm hơn một chút, đúng không."
- **2158** (Soutetsu): JP 「端的とは、『簡単にいうと』、ということだな」 / TW 「簡而言之，就是"用簡單的方法來說"的意思」 — 端的 (tanteki) nghĩa là "ngắn gọn, súc tích", không phải "thẳng thắn" (thẳng thắn = 率直/素直, frank). VN cũ "**Thẳng thắn** tức là, 『nói một cách đơn giản』 ấy mà" — từ đầu mục sai, trong khi chính phần giải nghĩa trong câu ("nói một cách đơn giản") đã đúng. Sửa thành "**Ngắn gọn** tức là, 『nói một cách đơn giản』 ấy mà".
- **2159** (Hikari): JP 「たんてきー？」 / TW 「簡而言之？」 — Hikari lặp lại từ Soutetsu vừa nói. VN cũ "**Thẳng thắn** ớ?" — cùng lỗi với 2158. Sửa thành "**Ngắn gọn** ớ?".

### C. Lỗi nhỏ (3 dòng)
- **1835** (Hikari): JP 「っ！！！」 / TW 「啊！！！」 — VN cũ "!!!" — mất hẳn tiếng hít っ (tiếng há hốc ngạc nhiên). Tiền lệ ở Hachiroku 12: mất tiếng hít っ tính là lỗi nhỏ. Sửa thành "Á!!!".
- **1846** (Soutetsu): JP 「ああ――」 (hai chữ あ) / TW 「嗯——」 — VN cũ "A――" (một chữ A) — độ dài tiếng kêu sai: 1827 trong cùng file là 「あ――」 (một あ) dịch đúng "A――", còn đây là hai あ nên phải là "Aa――". Sửa thành "Aa――".
- **2672** (monologue): JP 「だから、単純な恩返しだ。今度は僕が教えよう」 / TW 「所以，這只是單純的報恩。這次，就由我來教給光吧」 — độc thoại Soutetsu viết như lời nói trực tiếp với Hikari: "Lần này **để ba dạy cho con nhé**" — trái quy ước độc thoại "tôi" của chính file (159 dòng độc thoại còn lại đều dùng "tôi", vd 2469 "Hikari đã dựa dẫm vào tôi"). Sửa thành "Lần này **tôi sẽ dạy cho con bé**."

## Các cặp trùng lặp / lệch vị trí đã xác nhận
- **0 cặp chuyển chỗ, 0 dòng mồ côi, 0 tràn chương.** Đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục): mọi câu Việt sai đều chỉ xuất hiện ở đúng key của chúng, không phải bản dịch đúng của key khác.
- **2 cặp trùng lặp nội bộ:** "「A――」" 1827/1846 — chỉ 1827 đúng (JP 「あ――」 một あ); 1846 sai (JP 「ああ――」 hai あ, xem mục C). "（Tõm）" 2854/2859 — JP ちゃぷっ (2854) và ちゃぽん (2859) là hai tiếng nước gần như giống nhau, "Tõm" là cách dịch hợp lý cho cả hai nên **không tính lỗi**, chỉ ghi nhận.
- **0 dòng Việt nào copy từ file khác:** các câu ngắn trùng với file khác (tiếng kêu, "Ồ.", "Ừm.") đều đúng với JP của chính chúng.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- Soutetsu độc thoại xưng "Tôi" (159 dòng; chỉ 2672 xưng "ba" — sửa); Soutetsu thoại xưng "Tôi" trừ 5 dòng "anh" đã sửa (1854, 1954, 2048, 2070, 2132); Soutetsu gọi Paulette "em" (1738, 1742, 2226) và gọi Hikari "con" (2208); Soutetsu gọi nhân viên phục vụ "cô" (2127, 2230).
- Paulette xưng "em" trước Soutetsu (1981, 1983, 1985, 1999, 2003) và xưng "mẹ" trước Hikari (1929, 2210, 2221); Paulette gọi Soutetsu "anh" (1981, 2009, 2138) hoặc gọi tên trần "Soutetsu" (2071, 2228, 2229 — gọi tên trần là tình trạng chung cả dự án, 267 "anh Soutetsu" so với 338 gọi trần, không tính lỗi ở file này); Hikari gọi Soutetsu "ba" (1768, 1772) và Paulette "mẹ"; Reina gọi Paulette "chị Paulette" (1818, 2105).
- 共感 = **"cộng cảm"** khi là năng lực liên kết của Railord (1887, 2035, 2427 — đúng theo glossary team; khác với 共感 giữa người với người ở Grand 04 2112/2114 dịch "đồng cảm" là đúng — phân biệt theo ngữ cảnh, không phải theo từ).
- 端的 = **"Ngắn gọn"** (2158, 2159 — thuật ngữ mới ghi nhận từ file này; xem mục Đề xuất).
- レイルロオド = **"Railord"** (2049, 2196 — đúng chính tả 1 chữ "l"); エアクラ = **"Aircra"** (2045 — đúng); 日ノ本 = "Hinomoto" (2030, 2140); 鳴呼 = "Naruko" (2222); 二人羽織 giữ nguyên dạng La-tinh "Nininbaori" (2552 — ghi nhận, không tính lỗi vì dự án giữ nguyên nhiều tên văn hoá Nhật dạng này, vd "Hinomoto").
- 御一夜, 術仙, 帝鉄, 湯医, 冥国, 冥軍, 小畑, 大畑, コン không xuất hiện trong file này.

## Đề xuất context mới
- **Soutetsu gọi Paulette "cô" hay "em"?** (Cùng câu hỏi với file treasure — xem audit file kia.) Trong file này Soutetsu gọi Paulette "em" (1738, 1742, 2226, ngữ cảnh gia đình đi chơi), nhưng ở file treasure cùng chương 06 anh gọi cô "cô" (2047, ngữ cảnh công việc). Hai cách đều nhất quán trong từng file, nên không tính là lỗi — nhưng cần Hieu chốt: phân biệt theo ngữ cảnh (công việc "cô" / gia đình "em") hay thống nhất một cách cho cả dự án. Nếu thống nhất "em", file treasure có 1 dòng cần đổi (2047); nếu phân biệt theo ngữ cảnh thì giữ nguyên cả hai.
- **端的 = "Ngắn gọn":** ghi nhận làm thuật ngữ chuẩn cho các file sau (đừng dùng "Thẳng thắn" cho 端的 nữa). JP 端的 = 簡潔 (ngắn gọn, súc tích); "Thẳng thắn" là 率直/素直 (frank).
- **2070 "Paulette của tôi":** bản sửa theo đúng docs ("Tôi") nhưng nghe kém thân mật hơn "Paulette của anh" trong tiếng Việt vợ chồng. Nếu Hieu muốn giữ "của anh" ở những chỗ sở hữu cách thân mật thì docs cần ghi rõ ngoại lệ — còn không thì giữ bản sửa này.

## Khối TOML sửa (14 dòng — đã kiểm tra parse bằng tomllib, đúng 14/14 key, giá trị khớp JSON)
```toml
1331 = "「...『Mình đã muốn ba cùng mình đổ lỗi, rằng kẻ xấu xa chính là con người cơ』」"
1736 = "「Nhưng mà, em muốn ngày đó đến sớm hơn một chút, đúng không. Bởi vì, nó tuyệt vời đến thế cơ mà」"
1835 = "「Á!!!」"
1846 = "「Aa――」"
1854 = "「Ừ. Vì tôi đã rất ngạc nhiên mà. Khi biết rằng, chính từ sự hiểu lầm đó mà chúng ta đã kết nối được với nhau」"
1879 = "「Nè? Lúc nãy con bé nói gì vậy? Kể cho mẹ nghe với」"
1954 = "「Đáng sợ, thú vị, và khó khăn. Nhưng, tôi nghĩ điều quan trọng nhất chỉ có một thôi」"
1997 = "「Em nghĩ... Reina làm việc đó rất giỏi. Việc 『truyền đạt sao cho đối phương hiểu được』 ấy」"
2048 = "「Tôi nghĩ là vậy, và chúng ta đã cố gắng như thế. Nhưng cả hai đều hiểu lầm theo hướng có lợi cho bản thân mình」"
2070 = "「Ngủ ngon nhé, Paulette của tôi」"
2132 = "「Tôi cũng vậy thôi, nhưng Paulette lúc đó còn rất nhỏ mà. Nói là tiếng sét ái tình thì――」"
2158 = "「Ngắn gọn tức là, 『nói một cách đơn giản』 ấy mà」"
2159 = "「Ngắn gọn ớ?」"
2672 = "Thế nên, đây chỉ là một sự trả ơn đơn giản. Lần này tôi sẽ dạy cho con bé."
```

## Kết bài
Paulette 06_雪の宿 là file thứ mười sáu được audit toàn bộ (14/432 = 3,2% sai): một file sạch về cấu trúc — 0 dòng lệch vị trí, 0 dòng mồ côi, 0 tràn chương, 0 dòng chưa chắc chắn — và heuristic báo 0 dòng (bắt được 0/14), giống Grand 04. Lỗi tập trung ở xưng hô (8/14), nổi bật là mẫu Soutetsu tự xưng "anh" với Paulette (5 dòng) và ba lỗi gọi sai người (1331, 1879, 1997). Hai file cùng chương 06 trái ngược nhau về bản chất lỗi: file treasure nặng về thuật ngữ (16/25 dòng), file tuyết nặng về xưng hô (8/14 dòng) — thêm một bằng chứng không thể đoán chất lượng hay loại lỗi từ file bên cạnh, vẫn phải đọc hết từng dòng.

Việc còn lại của riêng file này là áp dụng khối TOML 14 dòng và chơi thử chương để nghiệm thu. Tổng 16 file đã audit: 1.512 dòng sai. Câu hỏi mở từ cặp file chương 06: Soutetsu gọi Paulette "cô" hay "em" — chờ Hieu chốt (xem mục Đề xuất context mới).
