## lr_ハチロクh2 — lr_ハチロクh2_新しい服。新しい旅.txt.toml — 63/327 (19,3%)

- File: `lr_ハチロクh2_新しい服。新しい旅.txt.toml` — route 01_Hachiroku, 327 dòng script (107 thoại Hachiroku, 89 thoại Soutetsu, 131 độc thoại). Nội dung: cảnh h Hachiroku — bộ quần áo mới đưa hai người vào "chuyến đi mới" ngay trong phòng quen thuộc; cô mặc đồ mới, ân ái nhiều lượt, kết bằng cảnh Soutetsu nằm nghỉ còn Hachiroku chuẩn bị bữa cơm.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất. 173 lệch TOML/CSV3 đều chỉ là `\n` bị flatten thành khoảng trắng trong TOML-2. `[selections]` rỗng. Không có thẻ `%l` nào trong file. Không có bản sao file này (md5 `7b0a3c5d1db89046c9b50bee2ff0e6f5`).
- Phân loại (63): xưng hô 22 (Soutetsu tự xưng "anh" 22/24 dòng thoại với Hachiroku — 1361, 1402 quét máy bắt thêm; chỉ 2 dòng "tôi" đúng sẵn 1364, 1579; 2 dòng gộp gasp 1557, 1681), thở gấp 29 chỗ (17 từ sweep + 12 mới: 1105, 1407, 1408, 1410, 1411, 1429, 1433, 1463, 1470, 1472, 1486, 1527 — っ cuối tuyệt đối trên từ âm thanh theo quyết định 仲国05), tiếng cười 7 (1423, 1424, 1447, 1508, 1511, 1547, 1606 — cười diễn thành rên, sửa về Nfufu/Ufufu/Fufu), sai nghĩa 3 (1436 はまっ=さま không phải "sâu", わらくっ="Em" không phải "Của em"; 1593 chủ ngữ quần áo; 1836 お仕置きして欲しい ngược hướng + gỡ ngoặc tự thêm), SFX 3 (1714 ぐぽ→"(Gupoooooooo)"; 1716 ぬと/れる/じゅるるるる→"(Nụtọooo——liếm——Chùn chụt)"; 1718 じゅぶううっ→"Chụụụt!"), thuật ngữ 1 (1440 タブレット→"máy tính bảng").
- Sweep kiểm chứng: 20 mục cho file, nhận 17 fix + 1 already-rendered (1104) + 2 needs-audit giải quyết xong không sửa (1720 "~~~~~~~~ưm", 2103 "ư" mềm — đều không lệch dòng).
- Chi tiết đầy đủ: `audit-lr-hachirokuh2-REVIEW.md`; danh sách sửa: `audit-lr-hachirokuh2-wrong.json` (63 mục, khối TOML 63 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 63/63; lượt soát 2: 63/63, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 116 file / 5.436 dòng sai** (cơ sở 115 file / 5.373 dòng sai + 63 file này)

- Chờ Hieu: đợt thống nhất fa/fu (14 dòng: 1410, 1424, 1425, 1427, 1428, 1429, 1432, 1433, 1434, 1436, 1438, 1440, 1442, 1443 — ふぁ/ふあ→"Haa"); mâu thuẫn ひあ/ひゃ (1410 "Hya" giữ); ranh giới gasp giữa dòng (~11 dòng / ~25 token っ giữa dòng, chủ yếu trong chuỗi rên 1410–1443); mâu thuẫn tiền lệ Hibiki 03 key 2360 (ふふっ→"Ư hự" ngược quy tắc cười); "Tablet" còn 16 dòng toàn dự án; 1121 Hachiroku gọi Soutetsu "anh" cho あなた (giữ — xem §8 review).

```toml
[script]
1105 = "「——AƯ」"
1120 = "「——Làm tôi cháy bỏng, làm tôi khao khát. Rằng tôi muốn em, muốn ôm lấy em.\\nĐã khiến tôi nóng bỏng và hưng phấn đến nhường này.」"
1358 = "「Cho dù có hỏng đi chăng nữa——tôi nhất định, sẽ sửa lại cho em」"
1361 = "「Là em đấy, Suzu. Cơ thể em khi tôi ngước nhìn từ đây.\\nSức nóng của em, và cả mùi cơ thể lẽ ra không tồn tại——」"
1402 = "「Cô bé của em, vẫn giống hệt như lần đầu tiên tôi nhìn thấy.\\nVẫn cho tôi thấy vẻ thanh khiết tột cùng không đổi thay」"
1407 = "「HyauƯ!!!!」"
1408 = "「HyauuuƯ!!!?」"
1410 = "「Hya! Ưm! Haa! YuunƯ!!!」"
1411 = "「HyauƯ!!!!」"
1414 = "「Ư」"
1415 = "「Ư!!!」"
1416 = "「Ư!!!!」"
1417 = "「Ư!?」"
1418 = "「Ư——a——Suzu, Suzu!」"
1423 = "「Nfufu」"
1424 = "「Haa——a……a……ưm——.\\nHư——Ufu——Ufufufufu」"
1429 = "「Haa! A! Ahi! AhyuƯ!!!」"
1433 = "「Haa! A! A! AƯ!!!」"
1436 = "「Haa! A! Sướng quá——ngài Soutetsu!\\nƯm! Em, em, cái này, sướng quá——!」"
1440 = "「Haa! Chết mất, máy tính bảng, kỳ lạ hết rồi——\\nTrắng xóa mất, ưm! Chớp nháy, liên tục」"
1447 = "「Trời ạ, ngài Soutetsu thật là. Nhưng mà——đúng vậy nhỉ. Fufu」"
1456 = "「Ư!!!!」"
1457 = "「Ư!!!!!!」"
1458 = "「Ư!!!!!!!!」"
1459 = "「Ư!!!?」"
1462 = "「A——a——Ư——」"
1463 = "「A, a, a, aƯ」"
1470 = "「AaaaaaƯ」"
1472 = "「HauƯ.」"
1474 = "「A~~~~Ư」"
1483 = "「Ư——!!!!」"
1486 = "「Ưm——ư——aƯ!」"
1507 = "「Aa, tôi biết rồi. Tôi cũng cùng em」"
1508 = "「Nfufu. Em uống ngoan chứ」"
1511 = "「Ufufu, đương nhiên rồi ạ? Vì là của hai người mà.\\nVì là chuyến đi của ngài Soutetsu và em mà」"
1513 = "「Linh hồn của em, thứ mà tôi yêu thương nhất,\\nđây là một vỏ bọc vô cùng xinh đẹp, hoàn toàn hài hòa với nội tâm đó.」"
1516 = "「Trong mắt tôi thì là vậy.\\nNgay cả những bóng đen vô cùng nhỏ bé được vẽ ra.」"
1527 = "「AaƯ!」"
1539 = "「Ừ, tôi đang cương cứng.」"
1547 = "「Đúng không ạ, Ufufu」"
1557 = "「Tôi cũng vậy, Suzu. Thế nên——Ư!!!?」"
1560 = "「Tôi cũng vậy. Tôi rất yêu em」"
1566 = "「Vì chúng ta là vợ chồng, là bạn đời, là đối tác.\\nCùng với em, như một người phụ nữ, tôi muốn cả hai cùng nhau thay đổi」"
1574 = "「Bộ phận sinh dục của em. Cô bé của em ấy.\\nĐã đón nhận tôi hết lần này đến lần khác và hoàn toàn mang hình dáng của tôi」"
1578 = "「Mong muốn của tôi là——mong muốn không bao giờ thay đổi là——cùng với em——」"
1583 = "「Em! Không——a ư——giới hạn, giới hạn rồi!\\nƯ——nhưng mà——cùng, cùng nhau, nhé, cùng nhau」"
1593 = "「Lần tới ngài muốn em mặc bộ quần áo nào, và muốn có chuyến đi mới như thế nào.\\nNhỉ? Ngài Soutetsu. Ngài đang nghĩ gì vậy?」"
1595 = "「Nếu vậy, Suzu. Hãy hiểu mong muốn của tôi」"
1599 = "「Dù bên trong đã thay đổi thành của một người phụ nữ——trưởng thành hoàn toàn,\\nthành bộ phận sinh dục nữ dành riêng cho tôi」"
1606 = "「Vâng. Ufufu. Thế nên em, bộ quần áo này.\\nEm thích nó hơn ngày hôm qua rồi」"
1619 = "「Nhỉ. Đương nhiên rồi.\\nVì là chuyến đi mà tôi và em, cùng nhau trải qua mà」"
1623 = "「Nhưng mà, ngay cả vẻ bề ngoài, tôi vẫn luôn,\\nbị tan chảy và mê hoặc đấy.」"
1624 = "「Tất nhiên tôi biết rất rõ, cơ thể của em——\\nCòn làm tôi tan chảy hơn cả vẻ bề ngoài của nó.」"
1648 = "「Tôi đã có một trải nghiệm mới, một chuyến đi trong căn phòng này.\\nNếu em cũng vậy thì——」"
1669 = "「Ngay bây giờ ở đây——tắm trên người tôi là được.」"
1671 = "「Giống như tôi thôi」"
1681 = "「Su, zu. Không được đâu.\\n——Cứ thế này thì, tôi——Ư!?」"
1714 = "「（Gupoooooooo）——ưm……ưm!」"
1716 = "「（Nụtọooo——liếm——Chùn chụt）\\nChụt! Phụt! Chụt! Phụt!」"
1718 = "「Vì thế……ưm.\\nChụụụt! Chụt! Chụt! Chụt!」"
1836 = "Mặc dù tôi cũng rất muốn cứ thế này mà được em ấy trừng phạt——\\nnhưng tôi không muốn ân ái với Suzu trong khi em ấy vẫn còn hiểu lầm."
2009 = "Một hành động vô cùng dâm đãng, nhưng lại được tô điểm bằng nụ cười ngây thơ——Ư!!"
2109 = "Chuyển động của Suzu trở nên đơn điệu. Chỉ để thúc giục tôi xuất tinh——\\nsự thẳng thừng, đơn giản, bạo lực, mang tính động vật và máy móc này——Ư!?"
```
