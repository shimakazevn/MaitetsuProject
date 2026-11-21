# Audit: ハチロク15_家族.txt.toml (01_Hachiroku)

- File: `ハチロク15_家族.txt.toml` — route 01_Hachiroku, 417 dòng script (monologue 169, 双鉄 111, ハチロク 73, ポーレット 24, 日々姫 17, 凪 7, ふかみ 7, れいな 3, 真闇 3, 稀咲 3). Nội dung: Soutetsu tỉnh dậy sau giấc mơ về Michiko và cây cầu; cầu hôn Hachiroku, bàn chuyện kết hôn hợp pháp giữa Railord và con người với Paulette/Hibiki (kế hoạch nhà máy Aircra, tuyến đường sắt Mikan, hộ khẩu, tên mới "Suzu"); kết thúc bằng cảnh cả nhóm chúc mừng và Soutetsu — Hachiroku ra ca làm việc. Chỉ có 10 nhân vật; hầu hết thoại Soutetsu đều hướng tới Hachiroku.
- Phương pháp: đọc hết từng dòng đối chiếu JP + TW (CSV3), kiểm tra chéo sweep っ-gasp, kiểm tra cơ học (JSON/TOML/CSV3, md5, trùng lặp, thẻ %l, comment # JP, project VN index).
- **417 dòng đã đọc hết, 28 dòng sai (6,7%)** — đại từ 8, thuật ngữ 8, gasp 8, nghĩa 4. Thoại 23/248 (9,3%), độc thoại 5/169 (3,0%). Theo nhân vật: 双鉄 14/111 (12,6%), monologue 5/169 (3,0%), ハチロク 3/73 (4,1%), ポーレット 3/24 (12,5%), ふかみ 2/7 (28,6%), 日々姫 1/17 (5,9%).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, 417 dòng, 0 key trùng, 0 VN trống. TOML và CSV3 khớp tuyệt đối (chênh 221 dòng chỉ ở `\n` literal bị TOML-2 làm phẳng thành khoảng trắng — CSV3 là chuẩn; 2 dòng 2084/2088 giữ nguyên `\n` literal cả hai bên). TOML md5 `08c8467825d18e49f8e084e33525c50c`, BOM + CRLF, `[selections]` rỗng, không bản sao trùng (md5 duy nhất toàn toml2). Comment `# JP:` đủ 434/434 (417 script + 9 characters + 8 subs). Thẻ `%l`: JP = VN mọi dòng (0 thẻ thiếu dấu `;` đóng, 0 thẻ tự thêm).

## §1. Đại từ (8 dòng)

- Soutetsu "anh" → "tôi" với Hachiroku (6): 1256, 1692, 1834, 1952, 1556, 1929 — tất cả đều là thoại trực tiếp Soutetsu↔Hachiroku, kiểm chứng người nghe từ dòng kề (1256 Hachiroku vừa hỏi "Trông ngài có vẻ như đang gặp ác mộng"; 1692/1834/1952 nằm trong mạch thoại với Hachiroku; 1556/1929 tiếp nối lời Hachiroku). Áp quy tắc đã chốt ("tôi" với Hachiroku).
- "mình" → "tôi" (1): 2020 — Soutetsu nói với Hachiroku trong thoại ("mình thích em"), không phải độc thoại nội tâm nên không thuộc ngoại lệ "mình" cho tự vấn nội tâm.
- Fukami tự xưng "Chị" → "Mình" (1): 2021 — Fukami nói với Nagi; quy tắc đã chốt: Fukami tự xưng "mình", không bao giờ "chị" (cùng tuổi với Nagi, tiền lệ file 08b đã bãi bỏ 31 fix "chị"/"em" cho cặp này).
- Giữ nguyên: "anh hai" của Hibiki (1591, 2054, 2070, 2051, 2053); "anh Soutetsu" của Paulette (1881, 2062) và Reina (1602) — khóa B4; "mình" ở 2745 (độc thoại nội tâm Soutetsu, thuộc ngoại lệ) và 1776 "vợ mình" (sở hữu/phản thân, không phải tự xưng); "bé Nagi" ở 1532 (Fukami gọi Nagi bằng dạng xưng tên, không phải đại từ "em"); "chị" ở 1241/2032 (Nagi gọi Mayami — đúng, Mayami là chị lớn) và 2038 "chị Mayami" của Hibiki.

## §2. Thuật ngữ (8 dòng)

- 御一夜 → "Ohitoyo" (5 dòng): 1526 (2 chỗ trong một dòng: "Thành phố Ohimitera" và "Đường sắt Ohito" — dạng "Ohito" còn thiếu cả "yo"), 1579, 1838, 1844, 1725. Sửa trong audit vì file đang audit (không để đợt thống nhất, theo tiền lệ file 07: Ohigawa→Ohitoyo sửa trong audit).
- 湯医線 → "tuyến Yunoi" (1): 2673 — "tuyến Yui" sai tên đã chốt.
- 整備体 gloss → "thân bảo trì" (1): 80 — VN cũ "thân chính" sai thuật ngữ đã chốt.
- キハ07 gloss → "KiHa 07" (1): 74 — chính tả JR chuẩn đã chốt ("KiHa" 150× vs "Kiha" 46× toàn toml2).

## §3. Gasp っ (8 dòng — sweep áp nguyên 8/8)

Sweep có 8 mục cho file này (1651, 1660, 2075, 2076, 2077, 2078, 2088, 2368) — audit xác nhận và áp nguyên cả 8 giá trị, 0 sửa lại. Sweep không bỏ sót gasp nào trong file (đã quét cơ học toàn bộ JP có っ — các dòng còn lại đều đã diễn đúng theo quy tắc gasp đã khóa: 1668 っと→"Ối!", 1738 あっ/えっ→"A/Hả", 1678 うっ→"Ư", 2754 スパンっ→"Xoạch!"; 1981/1641/1748/1773/1869 っ gắn tên riêng/từ nội dung — không thêm Ư; 2760 涙っ — từ nội dung, không thêm Ư; 2084 んなっ đã diễn thành "Cái gì!?" — âm đã có dạng lời, không thêm Ư; 1657 あのっ→"Dạ――", 1671 よろしっ→diễn bằng dấu gạch ngang trong câu lắp bắp).

## §4. Nghĩa (4 dòng)

- 2592 (chủ ngữ sai): người giải thích bản thảo hợp đồng là Paulette (TW: 波萊特向她解釋說 — Paulette giải thích cho Hibiki), VN cũ "Tôi giải thích cho con bé" gán việc giải thích cho Soutetsu → "Paulette giải thích cho con bé rằng...".
- 2069 (đọc sai): ト trong "雛で始まってトで終わる" là "to", không phải "tte" → "chữ tte" thành "chữ to".
- 1700 (thanh điệu sai): Soutetsu nói うむ với Mayami, VN cũ "Vâng." quá lễ phép/nữ tính → "Ừ." (khớp 1701 うむ→"Ừ" ngay sau đó).
- 1895 (thêm câu hỏi đuôi): JP だろう là khẳng định ("chúng ta sẽ tiếp tục dốc sức vận hành"), VN cũ thêm "đúng không" biến thành câu hỏi xác nhận → bỏ "đúng không".

## §5. Giữ nguyên có lý do (không tính lỗi)

- 2012 "Thị trưởng Paulette" — giữ: Paulette từng là thị trưởng, chính file này xác nhận ở 2596 ("Cho đến gần đây cô ấy vẫn là thị trưởng, tức là một chính trị gia").
- 1788 "Chữ \"U\" (U uất) trong U linh" — giữ: "U uất" là nghĩa Hán-Việt của 幽, không phải bịa thêm; ý chính của câu ("nhỏ nhoi" = かすか) đúng.
- 1698 はわわ → "Oa oa oa" — giữ: theo TW 嗚哇哇; đây là tiếng luống cuống, không phải rên.
- 80 仕業検査 → "kiểm tra doanh nghiệp" — giữ: theo TW 營業檢查; thuật ngữ kỹ thuật đường sắt, không có bằng chứng JP ngược.
- 1607 cách chơi chữ 子牛/公私 (merihari) — giữ: VN diễn lại trò đùa chữ bằng chú thích romaji ("Koushi (công tư)... koushi (bê con)"), tốt hơn TW (TW nhầm thành "bờm sư tử").
- 1863 "(suzu)" — giữ: nối tên Suzu với tiếng chuông (鈴の音), không sai nghĩa.
- 1874: JP trong CSV3 sạch (つないでいける); ký tự lạ "�" chỉ là lỗi hiển thị khi đọc output, không có trong file (0 byte U+FFFD trong TOML).
- Trùng lặp trong file: JP 「ああ」×2 (1717, 1682) đều → 「À.」 — câu lặp hợp lệ; VN 「Vậy thì.」×2 (2041 「で、だ」, 1742 「さて、と」) — hai từ nối khác nhau, cùng nghĩa "vậy thì", không phải lệch dòng.
- Nhiễm chéo kiểm tra bằng project VN index: VN dài >25 ký tự trùng 0 dòng với file khác; JP trùng trong file chỉ có 「ああ」 (đã nêu trên).

## §6. Kiểm chứng

- JSON 28 mục dạng chuẩn list-of-dicts, khóa chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 28/28 (kiểm chứng cơ học).
- Khối TOML 28 khóa, parse OK bằng tomllib, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\\n` giữ nguyên 28/28, không thêm `\\n` mới).
- Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (trừ 8 dòng gasp thay toàn bộ dấu câu).
- Lượt soát 2 (đọc lại toàn bộ 28 fix đối chiếu JP + TW): **28/28 tái kiểm chứng, 0 bỏ, 0 sửa**.
- Cơ sở tổng đã kiểm chứng trong ROUTE-AUDIT.md: **144 file / 6.519 dòng sai** (khớp với cơ sở parent giao — không dùng cơ sở cũ).

## §7. Cờ cho Hieu (không tự quyết)

- B19 in-game check (Paulette 13 key 1596) vẫn park toàn dự án; file này không có thẻ %l hỏng nên không bị ảnh hưởng.
- Không có thuật ngữ mới, người nghe mơ hồ hay JP cụt cần Hieu quyết trong file này.

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
74 = "Cuộc đại tu \\x%lキハ07;#00ffc040;KiHa 07%l;#; cuối cùng cũng hoàn tất,\\nhiện tại chỉ có \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ chạy khứ hồi hai chuyến mỗi ngày."
80 = "Chắc là em ấy vừa hoàn thành \\x%l仕業検査;#00ffc040;kiểm tra doanh nghiệp%l;#; xong.\\nReina trong \\x%l整備体;#00ffc040;thân bảo trì%l;#; đang đứng đó với vẻ mặt ngạc nhiên."
1256 = "「……Trông tôi, có vẻ như đang gặp ác mộng sao?」"
1526 = "「Trúng ba đích, bốn đích luôn? Ủa? Để xem nào……\\nThành phố Ohitoyo và thành phố Sendai, Đường sắt Ohitoyo và Đường sắt Mikan――」"
1556 = "「Không phải là nhỏ nhoi, mà là rất nhiều.\\nBởi vì em, chắc chắn sẽ lấp đầy trái tim tôi」"
1579 = "「Sự thật đây là vùng đất lý tưởng nhất để mở rộng vẫn không thay đổi,\\nnhưng việc thành lập nhà máy ở Ohitoyo thì không thể thực hiện được nữa rồi.」"
1651 = "「Ư!?」"
1660 = "「Haưư～～Ư」"
1692 = "「A, ra vậy…….\\nTôi đã khóc sao」"
1700 = "「Ừ. Thành ra ồn ào mất rồi.」"
1725 = "「Trong trường hợp của Ohitoyo thì sẽ do Thị trưởng quyết định.\\nThế nên, vấn đề này cũng hoàn toàn được giải quyết.」"
1834 = "「Trông mặt tôi như vậy sao?」"
1838 = "「Hoặc là, khi ai đó nhớ về Ohitoyo.\\nCó hình bóng của chúng ta, của 8620 ở đó cũng được.」"
1844 = "「Việc xây dựng nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; ở Ohitoyo,\\nlà để làm cứ điểm mở rộng ra khu vực trung tâm Kyushu……phải không ạ?」"
1895 = "「Ví dụ như, \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ.\\nTừ nay về sau, chúng ta vẫn sẽ tiếp tục dốc sức vận hành nó.」"
1929 = "「Tất nhiên, đó là mong muốn của tôi rồi」"
1952 = "「Cái \"nhỏ nhoi\" đó, có lẽ, tôi đã buông bỏ được rồi」"
2020 = "「Tôi đã nghĩ về điều đó rồi. Từ lúc tôi nhận ra――\\ntôi thích em, một tình cảm khác hẳn với mọi người.」"
2021 = "「À ừm……Mình cũng không rõ lắm, nhưng mà――\\nkiểu như sau khi khoe khoang tình cảm xong mới nhận ra rồi thấy xấu hổ ấy?」"
2069 = "「Bắt đầu bằng chữ Hina và kết thúc bằng chữ to, là người thuê tôi và em đấy.」"
2075 = "「Ư!」"
2076 = "「Ư!!!」"
2077 = "「Ư!!?」"
2078 = "「~Ư」"
2088 = "『「Ư!!?」\\n「Ư!!?」』"
2368 = "Hachiroku mở to hai mắt――Ư!?"
2592 = "Paulette giải thích cho con bé rằng đó là bản thảo hợp đồng――giống như một bản thiết kế sơ bộ vậy."
2673 = "Nếu có thể khôi phục tuyến đường, khu vực ngoại ô ga Sendai ở tỉnh Kagoshima, nơi sẽ trở thành ga trung chuyển giữa Đường sắt Mikan và tuyến Yunoi――"
```

## Kết bài

- File ハチロク15_家族: 417 dòng đã đọc hết, **28 dòng sai (6,7%)** — đại từ 8, thuật ngữ 8, gasp 8, nghĩa 4. 0 lệch vị trí, 0 chuỗi xoay, 0 nhiễm chéo, 0 mồ côi, 0 chưa dịch, 0 trùng khóa.
- Lượt soát 2: 28/28 tái kiểm chứng, 0 bỏ, 0 sửa. JSON 28 mục, khối TOML 28 khóa parse OK, 0 sai lệch giá trị.
- Không có mục nào cần Hieu quyết trong file này; B19 vẫn park toàn dự án.

**Tổng cộng sau file này: 145 file / 6.547 dòng sai** (cơ sở 144 file / 6.519 dòng sai + 28 file này)
