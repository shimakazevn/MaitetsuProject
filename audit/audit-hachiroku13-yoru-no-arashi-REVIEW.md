# Audit: Hachiroku 13_夜の嵐 — 199 dòng Việt sai (đã đối chiếu JP + TW)

File: `01_Hachiroku/ハチロク13_夜の嵐.txt.toml` — 443 dòng script, **199 dòng Việt sai = 44,9%**.
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. Đây là file thứ 5 audit toàn bộ, sau 廃炭鉱 31%, Grand 01 45,6%, obasan 56%, Hibiki 03 86,2% — 夜の嵐 ngang Grand 01, nhưng cơ chế lỗi của nó có thêm một lớp mới (xem "Kết luận về cơ chế lỗi").

## Phương pháp và số liệu kiểm chứng
- Đã đọc **hết 443/443 dòng script** (key 91–2890, không liên tục), đối chiếu từng dòng với JP + TW theo nghĩa, người nói, thoại/lời dẫn. Không ngoại suy tổng dự án từ file này.
- Phân loại 199 dòng sai: **lệch nội dung 199**, **chưa dịch (còn nguyên tiếng Trung trong TOML) 0**, **dịch thiếu (cụt câu) 0**, **không chắc chắn 0**. Không có dòng nào mang tiếng Trung (VN==TW = 0 trong cả CSV lẫn TOML).
- Thoại sai 110/246 (44,7%); lời dẫn (monologue) sai 89/197 (45,2%) — lỗi trải đều thoại và dẫn, không tập trung vào một loại. Theo người nói: monologue 90/198, Soutetsu 51/112, Hachiroku 15/49, Hibiki 0/26 (không sai dòng nào), Paulette 18/26, Mayami 11/12, Reina 4/7, Minokasa 4/4, Akai 3/3, Kon 1/2, Suzume 0/2, Unzan 1/1, Nagayama 1/1. Hibiki là nhân vật duy nhất không sai dòng nào trong file này.
- **Không có key-shift sạch:** thử shift -5..+5 trên key, độ khớp thoại/dẫn chỉ dao động 0,753–0,777, shift 0 đã là tốt nhất (0,777) nhưng vẫn thấp — lỗi rải rác, không lệch đều. Heuristic thoại/dẫn báo 99/443 (22,3%) — chưa bằng một nửa con số thực 44,9%, vì phần lớn lỗi là lệch cùng loại (thoại→thoại sai, dẫn→dẫn sai) mà heuristic không bắt được.
- **TOML và CSV giống hệt nhau về nội dung:** 270/443 dòng khác nhau chỉ ở `\n`/khoảng trắng, 0 dòng khác nội dung thực. Không có dòng CSV trống nào trong file này.
- **Không xét lỗi định dạng `\n`:** theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng, `\n` thủ công không quan trọng. Chỉ báo lỗi nội dung. Các bản sửa trong khối TOML bên dưới viết liền một dòng (không chèn `\n` thủ công) theo đúng quyết định đó.

## Kết luận về cơ chế lỗi
- Cơ chế chính giống các file trước — **cột Việt bị xáo trộn rải rác ngay từ lúc dịch trên Sheets** — nhưng file này có thêm bằng chứng về NGUỒN của các câu sai, rõ hơn mọi file trước:
- **168 cặp trùng lặp trong cùng file:** có 167 giá trị Việt xuất hiện ở 2 key khác nhau (một giá trị xuất hiện ở 3 key), và trong mỗi cặp thì JP ở 2 key đều khác nhau — tức chỉ một key đúng, một key sai. 167 dòng sai mang câu Việt "mượn" từ một key khác trong cùng file (danh sách bên dưới). Đây là cơ chế trùng lặp lớn nhất từ trước tới nay (Hibiki 03 chỉ có 16 cặp trùng lặp được ghi nhận dạng này).
- **32 dòng sai còn lại mang câu Việt từ chương khác:** 32 dòng sai có câu Việt không trùng với bất kỳ dòng nào khác trong file này, nhưng cả 32 câu đều xuất hiện trong file chương trước — `ハチロク12_再開発.txt.toml` — và kiểm tra mẫu cho thấy chúng là bản dịch ĐÚNG của JP ở Hachiroku 12 (VD: câu Việt ở key 91 chính là bản dịch đúng của Hachiroku 12 key 3207; câu ở 1182 là của Hachiroku 12 key 2281). Tức cột Việt của file này đã bị chép đè một phần từ chương Hachiroku 12. Hệ quả cần lưu ý: Hachiroku 12 có thể cũng đã bị xáo trộn ngược lại — nên audit Hachiroku 12 sau, dù nó không nằm trong danh sách file nặng nhất theo heuristic.
- **Không dòng sai nào lấy lại được bản dịch đúng từ trong file:** đối chiếu toàn bộ 199 bản sửa mới với mọi giá trị Việt đang có trong file (sau khi chuẩn hoá thẻ `%l` và khoảng trắng) cho 0 trùng khớp có ý nghĩa — tức bản dịch đúng gốc của 199 dòng sai đã bị mất khỏi file này, phải dịch mới hoàn toàn từ JP/TW. Khối TOML bên dưới đã dịch mới đủ 199 dòng. (Ghi chú: chỉ có một trùng khớp giả do chuẩn hoá — bản sửa 1212 sau khi bỏ thẻ `%l` còn lại "「!」", trùng với câu cảm thán ngắn "「!」" ở key 2066, không phải bản dịch của 1212.)
- JP và TW khớp nhau, nên mọi dòng sai đều sửa được chỉ bằng cách dịch lại từ JP/TW, không cần thêm nguồn nào khác.
- 244 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Các cặp trùng lặp / lệch vị trí đã xác nhận (168 cặp, 167 dòng sai)
Đọc là: dòng sai `A` đang mang câu Việt đúng của dòng `B` (B đã đúng, A phải dịch mới). Ví dụ: `1173←2412` — câu Việt ở 1173 thực ra là của 2412.
1173←2412, 1187←2823, 1218←2032, 1231←2801, 1242←1848, 1467←2053, 1473←1654, 1474←2738, 1478←2009, 1489←2571, 1491←2030, 1513←1868, 1515←1639, 1528←1569, 1530←1963, 1566←2016, 1571←2336, 1608←1660, 1611←1484, 1618←2506, 1622←1667, 1624←1778, 1630←2027, 1631←2740, 1633←1684, 1641←2790, 1646←2250, 1650←1775, 1652←2317, 1657←1691, 1658←2637, 1666←2018, 1675←2589, 1679←1243, 1688←2313, 1699←1647, 1712←1635, 1714←2520, 1715←2680, 1718←1716, 1722←2243, 1738←2346, 1739←2321, 1740←2340, 1763←1812, 1768←1909, 1769←1508, 1779←2043, 1782←1613, 1784←1464, 1789←2075, 1790←1186, 1797←2818, 1799←2841, 1808←2701, 1810←2326, 1818←2635, 1823←1476, 1825←2516, 1830←1240, 1835←2461, 1839←1867, 1843←2691, 1849←1678, 1861←2763, 1870←1502, 1871←1693, 1893←2385, 1894←1833, 1901←2868, 1903←2361, 1907←2742, 1910←1841, 1915←2592, 1917←2541, 1930←2318, 1935←2890, 1953←2378, 1972←2579, 1973←2651, 1976←1873, 1998←1749, 1999←2525, 2001←2573, 2002←2619, 2006←2803, 2008←2569, 2022←1794, 2041←2035, 2042←2593, 2044←2844, 2050←2702, 2051←2270, 2052←2000, 2054←1744, 2056←2281, 2059←2047, 2068←1203, 2069←2866, 2071←1626, 2238←1719, 2254←2610, 2279←1628, 2286←1943, 2289←1785, 2303←1574, 2310←1968, 2324←1757, 2334←2774, 2383←2871, 2427←2421, 2431←1834, 2432←1510, 2438←1792, 2444←2247, 2448←2879, 2509←2575, 2529←1902, 2530←1970, 2534←2739, 2536←2446, 2539←2888, 2549←2544, 2555←1239, 2564←1787, 2576←2442, 2588←1462, 2591←2387, 2598←2284, 2607←2046, 2608←1680, 2614←1605, 2623←1753, 2640←1924, 2676←2732, 2677←2328, 2678←2585, 2679←1683, 2684←2454, 2685←2567, 2689←1872, 2698←2268, 2714←2415, 2716←1734, 2717←2063, 2719←1771, 2724←1506, 2728←2067, 2741←2695, 2744←2013, 2760←1672, 2760←1844, 2775←2288, 2778←2439, 2794←2066, 2802←1927, 2813←1210, 2826←1671, 2834←2248, 2862←2066, 2865←2436, 2873←1869, 2876←1939, 2877←1472, 2878←2414, 2882←1733, 2885←2547, 2887←1933

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- 術仙炭鉱 = "mỏ than Jutsusen" (theo các dòng đúng sẵn có trong file, VD 1713, 1740 — lưu ý: audit 廃炭鉱 trước dùng "mỏ than Jutsu-sen", khác nhau ở dấu gạch nối; giữ theo file này).
- 御一夜駅 / 御一夜側 = "ga Ohitoyo" / "phía Ohitoyo" (theo các dòng đúng sẵn có: 1240, 2281, 2695). Riêng tên thành phố 御一夜 trong 2 bản sửa (2873, 2885) dùng "Ohimitera" theo docs — **không thống nhất với "Ohitoyo" trong cùng file, xem đề xuất bên dưới**. Quyết định 19/11: 御一夜 = Ohitoyo — 2 bản sửa đã đổi sang "Ohitoyo", nay thống nhất với "ga Ohitoyo" trong file.
- 湯医 = "Yunoi" trong các bản sửa (1699, 1763, 1779, 1784, 1810) — theo đề xuất từ audit Grand 01 (furigana ゆのい) và file Thựcりの秋 dùng "Yui" ở 2102 — **chưa chốt, xem đề xuất bên dưới**.
- コン (cáo) = "Kon" — ĐÃ QUYẾT 19/11 (Hieu): JP 1929/2551 đều là コン (tên), không phải くぅ — 2 dòng đã chuyển sang danh sách sửa (xem Bổ sung ở cuối file).
- 自弁 = "van hãm tự động" (theo dòng đúng 2516); 絶気 = "cắt hơi" (theo Thựcりの秋 2212 và TW "vô hơi"); 喚呼 = "hô xác nhận" (theo Thựcりの秋 2828); 前進フルギア = "Tiến hết ga"; 換装 = "đổi thân"; 運転体 = "thân điều khiển"; 整備体 = "thân chính"; タブレット = "thẻ bảng"; 乗務鞄 = "túi phi hành đoàn" (theo các dòng đúng sẵn có).
- Soutetsu độc thoại/dẫn chuyện xưng "Tôi"; Hachiroku xưng "Em" (hoặc "Tôi" trong báo cáo), gọi Soutetsu là "Ngài Soutetsu"; Hibiki gọi Soutetsu là "Anh hai"; Paulette gọi Soutetsu là "Anh Soutetsu"; Mayami gọi Soutetsu là "Sou-chan", xưng "Chị"; Minokasa gọi Soutetsu là "Cậu Soutetsu".
- Còi tàu ポッ ở 2868 giữ dạng "Tu!" theo docs (sfx §1.1: ポー = "Tuúú…" hoặc "Uúú…", dạng "Tu!" ngắn đã có sẵn trong file).

## Dòng không chắc chắn (0 dòng)
- Không có dòng nào JP/TW mâu thuẫn nhau hay lửng tới mức không dịch được trong file này. Mọi dòng sai đều đã có bản sửa chắc chắn trong khối TOML.

## Đề xuất cập nhật context (để Hieu quyết, KHÔNG tự đổi toàn dự án)
1. **御一夜 — "Ohitoyo" hay "Ohimitera" (và "Ohito" cho 御一夜鉄道):** file này dùng "Ohitoyo" cho ga (1240, 2281, 2695) và "Ohito" cho đường sắt (theo Thựcりの秋 1694, 2535), trong khi docs quy thành phố là "Ohimitera" — và bản sửa ở 2873/2885 đã dùng "Ohimitera" cho tên thành phố theo docs. Chưa kể furigana trong Thựcりの秋 2102 ghi 御一夜 là おひとよ ("Ohitoyo"). Ba dạng đang cùng tồn tại; Hieu chốt một dạng cho tên thành phố/ga/đường sắt thì mình sẽ chuẩn hoá toàn bộ theo. Quyết định 19/11: 御一夜 = Ohitoyo — 2 bản sửa 2873/2885 đã đổi sang "Ohitoyo" (đợt sửa 19/11); các dòng đúng dùng "Ohito" cho đường sắt vẫn chờ đợt thống nhất sau.
2. **湯医 — "Yui" hay "Yunoi":** bản sửa file này dùng "Yunoi" theo furigana ゆのい (đề xuất từ Grand 01), nhưng Thựcりの秋 2102 dùng "Yui". Hieu chốt một dạng cho toàn dự án.
3. **コン — giữ "Kuu" hay đổi "Kon":** file này dùng "Kuu" nhất quán (1929, 2551). Phiên âm chuẩn của コン là "Kon" (tiếng cáo kêu "kon kon"), nhưng nếu dự án đã quen "Kuu" thì giữ nguyên cũng được — Hieu quyết.
4. **帝鉄:** file này không có dòng sai nào nhắc tới 帝鉄 nên không phát sinh thêm bằng chứng mới; quyết định cũ (docs "Đường sắt Hoàng gia" vs "Teitetsu") vẫn đang chờ Hieu, xem audit Grand 01.

## Giới hạn của audit này
- Đã đọc hết 443 dòng script của file này: 199 dòng sai đã xác nhận, 244 dòng còn lại khớp JP/TW.
- Vẫn có thể sót vài dòng "trông hợp lý nhưng thực ra là bản dịch của dòng khác" — cách chắc chắn nhất vẫn là chơi qua chương và đối chiếu voice. Nếu Hieu gặp thêm dòng nào nghi ngờ trong file này thì gửi mình, mình kiểm tra nốt.
- 32 dòng sai không thuộc 168 cặp trùng lặp trong file đều đã truy vết được sang Hachiroku 12 (xem trên) — trong đó câu ngắn 1201 ("Nếu vậy thì.") còn trùng với vài file khác nữa vì quá ngắn, nhưng nó cũng có mặt ở Hachiroku 12; bản sửa của nó đã chắc chắn theo JP.
- File này (44,9% sai) nặng ngang Grand 01 (45,6%) nhưng nhẹ hơn obasan (56%) và Hibiki 03 (86,2%).

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)
Lưu ý khi chép: các bản sửa viết liền một dòng, không chèn `\n` thủ công — theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng. Khối này đã kiểm tra bằng máy: parse được bằng tomllib, **199/199 key** khớp đúng tập dòng sai, không thừa không thiếu, giá trị sau khi parse khớp đúng bản sửa (kể cả thẻ `%l`).

```toml
91 = "\\x%l8620;#00ffc040;8620%l;#; giờ đã chậm hơn cả Paulette đang đi bộ trên sân ga nữa rồi."
1173 = "Cùng lúc với lời của chị Mayami, đường kẻ trên bản đồ dần khoanh ra một vùng lớn."
1182 = "……Mục tiêu dừng ngay trước mặt. Cứ để quán tính trôi tới là được."
1187 = "……Tôi và Hachiroku thay nhau giải thích tình hình."
1201 = "「\\x%l制動;#00ffc040;Phanh%l;#, 0,4」"
1208 = "「\\x%l自弁;#00ffc040;van hãm tự động%l;#;——vị trí lái」"
1212 = "「\\x%l階段;#00ffc040;Từng nấc%l;#;!」"
1214 = "「——Dừng xe. Mục tiêu dừng, tốt.」"
1218 = "「——Không, ra vậy. 'Ngoài \\x%lエアクラ;#00ffc040;Aircra%l;#;' sao.」"
1231 = "「……Dù có ngủ lại ở khu ký túc xá cũ thì cũng nguy hiểm đó. Ở đó có những tòa nhà sập lúc nào cũng không lạ đâu.」"
1242 = "「……Trước hết cứ kiểm tra tình hình đã. Cho tôi mượn điện thoại được không?」"
1467 = "「Không được. Đừng bay. Đây là mệnh lệnh.」"
1473 = "「À, đã sập đến mức này rồi thì ở lại, bình tĩnh rồi hãy tính thì hơn nhỉ.」"
1474 = "「Không, mấy hôm trước nó bảo 'chuẩn bị đồ để ngủ lại' rồi mang túi ngủ các thứ đi…… mà vẫn chưa mang về.」"
1478 = "「Ví dụ như, đi \\x%lエアクラ;#00ffc040;Aircra%l;#; đến phút chót rồi mới—— chẳng hạn.」"
1489 = "「Nagi hôm nay có mang đồ cắm trại đi không?」"
1491 = "「Hôm nay á? Hôm nay chỉ mang cặp sách đi học bình thường thôi——」"
1513 = "「Hibiki với Kisaki, Nagi với Fukami nữa, đúng không?」"
1515 = "「Cái gì cơ?」"
1527 = "「Hachiroku. Đến ga Ohitoyo rồi. ——Đúng giờ.」"
1528 = "「Hachiroku, em không khỏe à?」"
1530 = "「Hachiroku, kết nối \\x%l共感;#00ffc040;cộng cảm%l;#; với Navi nhé.」"
1538 = "「Hachiroku, xuống đi. Đổi \\x%lタブレット;#00ffc040;thẻ bảng%l;#; cho tôi.」"
1551 = "「Đến, 1800——đúng giờ.」"
1566 = "「Vâng ạ. Bên tôi cũng sẽ kiểm tra hết các điểm nghi ngờ—— Vâng, có gì là tôi liên lạc ngay.」"
1571 = "「Mỏ than…… mà cắm trại à. Nguy hiểm lắm đấy. Lỡ muốn sưởi ấm mà dùng lửa thì sao.」"
1608 = "「Tôi chỉ nghỉ một chút thôi. Đứng dậy thì bao nhiêu cũng được.」"
1611 = "「Xin lỗi.」"
1618 = "「Keng!」"
1622 = "「Phù…… Cảm ơn khăn ạ.」"
1624 = "「Phù wa, mưa to gió lớn quá à.」"
1630 = "「Ơ? Không phải ở buồng lái à?」"
1631 = "「Hử? Không——à, vâng. Đúng…… vậy nhỉ.」"
1633 = "「Không không, cảm ơn cô đã làm việc vất vả.」"
1641 = "「À——vâng, đúng vậy nhỉ.」"
1646 = "「À!」"
1650 = "「À, tôi xuống ngay đây.」"
1652 = "「À, là tôi đây. Xin lỗi.」"
1657 = "「Alo——hử? Gì vậy?」"
1658 = "「À, xin lỗi. Tôi là anh trai của Migita Hibiki, học sinh đang học ở trường——」"
1661 = "「Vâng. ……Vâng. Tôi đã xem kỹ rồi ạ.」"
1666 = "「Vâng. Ở khu nội trú. Vâng—— đúng vậy, nếu có thể thì cho tôi nói chuyện—— vâng, xin lỗi.」"
1675 = "「Ừ, nếu từ phía Ohitoyo thì chỗ dọc đường ray này——」"
1679 = "「Vâng, đúng vậy.」"
1688 = "「Cô Houshou Kisaki muốn được tư vấn qua đêm, nên—— bé Hibiki cứ nhất quyết đòi như vậy.」"
1699 = "「Ông Seki giờ đang ở bến thuyền Yunoi đấy ạ. Để thuyền không bị bão cuốn đi nên phải đưa thuyền lên bờ. Vì vậy——」"
1712 = "「Với đội hình đó thì là ngủ lại bên ngoài. Tức là ngủ ở khu nội trú của trường.」"
1714 = "「Navi được nhờ việc gì sao?」"
1715 = "「Không có, sao? Hibiki—— Kisaki nữa, Nagi nữa, Fukami nữa—— bốn người…… tất cả sao.」"
1718 = "「Vâng! Để tôi thử nhờ xem.」"
1722 = "「Ngoài đi bộ ra thì sao?」"
1738 = "「Kon-chan, nhờ phiên dịch giúp ạ.」"
1739 = "「Sou-chan!」"
1740 = "「Sou-chan, ở mỏ than Jutsusen phải không?」"
1763 = "「Từ đây đi bộ dọc đường ray 2km là tới gần mỏ than Jutsusen, nhưng đi bộ từ phía Yunoi thì……」"
1768 = "「Sao cơ chứ!」"
1769 = "「Sao rồi? Đứng dậy được không?」"
1773 = "「Lái xe tuyệt vời ạ, ngài Soutetsu.」"
1779 = "「Tôi cũng đã nghĩ vậy. Nhưng đó không phải là nơi có thể đi bộ từ Yunoi tới được.」"
1782 = "「Chuyện đó để tôi lo.」"
1784 = "「Công ty taxi gần Yunoi ấy ạ. Nhóm bé Hibiki, bốn người, dù đi cùng nhau hay đi riêng thì có vẻ đều không đi taxi.」"
1789 = "「Tôi cho phép là vào sáng hôm qua. Lúc đó dự báo nói bão vẫn chưa tới.」"
1790 = "「Tôi nấu cơm nắm với súp miso để phát cho mọi người nhé.」"
1797 = "「Tôi rõ rồi.」"
1799 = "「Tôi nghe rồi. Có gì giúp được thì cứ nói.」"
1808 = "「Vậy thì…… ừm, nhóm bé Hibiki——」"
1810 = "「Nếu đưa thuyền lên bờ thì—— ông Seki đang đi xe chạy xăng tới Yunoi, đúng không?」"
1818 = "「Là nhóm bé Hibiki đấy. Họ không lên \\x%l客車;#00ffc040;toa hành khách%l;#;——oa!?」"
1823 = "「Vâng—— tôi nối máy đây. Hử? À!」"
1825 = "「Vâng. Vâng—— hả!? Thật sao? Vâng! Tôi rõ rồi. Cảm ơn ạ!」"
1830 = "「Đúng vậy. Nếu gặp khí gas thì—— tệ nhất là nổ tung.」"
1835 = "「Phải không. Vậy thì—— này.」"
1839 = "「Vâng. Cô ấy nói vậy đấy.」"
1843 = "「Vậy sao.」"
1849 = "「Gần nhất thì…… khoảng sáu cây số?」"
1861 = "「Chỉ suy đoán thì khó hành động. Manh mối dễ nắm nhất là………… thuyền sao.」"
1870 = "「Vâng, mời anh. À, anh biết số điện thoại của trường không?」"
1871 = "「Quả nhiên, nếu không có phụ lái thì số lần \\x%l換装;#00ffc040;đổi thân%l;#; sẽ nhiều lên. Nên gánh nặng cũng——」"
1893 = "「Trong mỏ than dễ sinh khí gas lắm ạ. Dụng cụ cũng toàn dùng loại không phát tia lửa đấy ạ.」"
1894 = "「Nổ tung——」"
1901 = "「Reina cũng đi nhờ giúp đây ạ.」"
1903 = "「Giờ chỉ còn toa xe chạy được là 8620 thôi.」"
1907 = "「Thuyền chỉ có một chiếc—— không đủ nhỉ?」"
1910 = "「Vậy thì bốn người khả năng cao đã xuôi sông tới gần mỏ than Jutsusen.」"
1915 = "「Chị Mayami!」"
1917 = "「Chị Mayami, Paulette. Nhờ hai người một lúc nhé. Bọn tôi sẽ chuẩn bị để lúc nào cũng xuất phát được.」"
1930 = "「À không, thử hỏi công ty taxi xem. Tôi đã xác nhận là không có xe đưa đón từ nhà rồi.」"
1935 = "「Trước mắt thì tôi đang nhờ mạng liên lạc của các tín đồ thu thập thông tin.」"
1953 = "「Ông Minokasa, đúng lúc quá!」"
1972 = "「Toàn diệt rồi. Cả nhà ông Minokasa, nhà Hayase—— cả nhà Houshou cũng bảo là không có manh mối gì.」"
1973 = "「Chỉ cần xác nhận và báo lại một điểm duy nhất thôi: có thuyền ở điểm có thể cập bờ gần mỏ than Jutsusen hay không.」"
1976 = "「Cảm ơn. Vậy xin lỗi, gọi cho ông Seki giúp tôi được không?」"
1998 = "「Chịu không nổi. Làm xong việc quay đầu tàu trước đã. Chuyện sau đó nói ở rail shop.」"
1999 = "「Là bản copy mà. Cứ viết trực tiếp vào là được.」"
2001 = "「Bên này cũng vậy. Đám đàn em đang hỏi thăm khắp nơi.」"
2002 = "「Rộng thế này cơ á?」"
2006 = "「\\x%l絶気;#00ffc040;cắt hơi%l;#; tốt. \\x%l前進フルギア;#00ffc040;Tiến hết ga%l;#;」"
2008 = "「Ngủ lại á——」"
2019 = "「Vậy thì tốt quá.」"
2022 = "「Làm thì, còn lại thì…… ngoài \\x%lエアクラ;#00ffc040;Aircra%l;#; ra thì——」"
2036 = "「Giới hạn 40.」"
2041 = "「Tuy không phải là quãng đường không đi bộ được…… nhưng nghe nói cả bốn đứa đều đã đến trường đàng hoàng.」"
2042 = "「Tôi cũng nghĩ vậy nhưng——」"
2044 = "「Tôi cũng rất muốn làm vậy, nhưng tìm kiếm mà không có manh mối thì không biết sẽ mất bao lâu.」"
2050 = "「Anh Soutetsu? Được không?」"
2051 = "「Cậu Soutetsu. Nagi đã gây phiền phức cho cậu rồi.」"
2052 = "「Ngài Soutetsu——」"
2054 = "「Vậy thì, ngài Soutetsu! Đi ngay thôi.」"
2056 = "「Ngài Soutetsu, Navi đang…… dọc bờ sông ngoài vùng cấm bay.」"
2059 = "「Mọi người—— cảm ơn mọi người.」"
2068 = "「Ư!!?」"
2069 = "「!?」"
2071 = "「Nghe nói Navi đã luôn hỗ trợ ngài Soutetsu. Không chở ai cả, cũng không được nhờ việc gì.」"
2238 = "Có lẽ tôi đã phán đoán sai, cảm giác đó cũng lẫn vào, khiến tôi cứ bồn chồn không yên."
2252 = "Nếu không thì, chỉ vì tiếng mưa gió và rung động mà dao động đến mức này thì không thể nào."
2254 = "Không có phe ủng hộ hay phe phản đối việc mời nhà máy về. Trước khủng hoảng của vùng, mọi người nắm tay nhau, kết nối lại."
2266 = "Hôm nay dù sao tôi cũng muốn về sớm rồi đi ngủ. Cơ thể mệt rã rời——"
2279 = "Nói đến đó. À—— ông Minokasa khẽ rên lên."
2286 = "Nhưng, thực tế thì thời tiết thế này. Lời nói thế nào cũng thành ra như biện minh."
2289 = "Rồi điều \\x%lエアクラ;#00ffc040;Aircra%l;#; tới, di chuyển đến sát vùng cấm vào——"
2303 = "Dù mái nhà và \\x%l8620;#00ffc040;8620%l;#; đã che chắn, mưa vẫn xuyên qua khe hở, đâm vào như kim."
2310 = "Dữ liệu về vùng cấm \\x%lエアクラ;#00ffc040;Aircra%l;#; xâm nhập mà Navi có. Hachiroku đã tái hiện nó lên bản đồ cho tôi."
2323 = "Nhắm chặt mắt lại, hít một hơi vào."
2324 = "Cứ—— gật đầu, cái gật đầu chậm rãi."
2334 = "Tôi vươn tay ra. Hachiroku từ từ nắm lấy tay tôi——Ư!"
2344 = "Chuẩn xác. Nhưng Hachiroku lại không hô \\x%l喚呼;#00ffc040;hô xác nhận%l;#;."
2347 = "Giờ chỉ còn chạy bằng quán tính. Sau đó chỉ cần giảm tốc rồi dừng lại."
2348 = "Tốc độ giảm dần. Đã giảm hẳn rồi."
2383 = "Nếu có thể dựa vào mối liên kết này thì, từ đây trở đi——"
2402 = "Khác mọi khi. Hachiroku không hô \\x%l喚呼;#00ffc040;hô xác nhận%l;#; cùng tôi."
2427 = "Khi ở \\x%l運転体;#00ffc040;thân điều khiển%l;#; thì tôi không nhận ra——"
2431 = "Nếu là hai người đó thì, 'dùng sông là tới mỏ than ngay', chắc đã nhận ra từ lâu rồi——"
2432 = "Trong bốn người, lớp của Kisaki giỏi nhất, toàn bộ chương trình học kết thúc lúc hai giờ chiều."
2433 = "Đang bị thử thách sao? Chắc trước đây cũng từng có chuyện thế này—— Tôi xua đi những tạp niệm vừa dâng lên, tập trung lại vào mắt và tay."
2438 = "Đường sông trên bản đồ mà chị Mayami đang kiểm tra—— với ga mỏ than Jutsusen bỏ hoang, cách nhau chưa tới một cây số."
2444 = "Một khi đã vào gần mỏ than Jutsusen thì sẽ mất liên lạc."
2448 = "Nếu việc tìm kiếm mù quáng giữ chân nhân lực và phương tiện di chuyển thì trong thời gian tìm kiếm, các việc khác sẽ hoàn toàn bị bỏ trống."
2455 = "Cảm giác an tâm trào dâng."
2509 = "Tôi, chúng tôi—— chỉ cần làm những việc chỉ chúng tôi mới làm được."
2514 = "Tự nhủ vậy, tôi từ từ—— khẽ động tay van \\x%l自弁;#00ffc040;van hãm tự động%l;#;."
2529 = "Vừa hỏi thì Paulette đã chộp lấy ống nghe."
2530 = "Gọi vào số trên giấy nhớ Paulette đưa thì ngay lập tức có giọng trả lời bình tĩnh."
2532 = "Tôi cố gắng kiểm soát những ngón tay sắp run lên, hoàn thành biện pháp dừng xe—— cuối cùng, gọi Hachiroku."
2534 = "Trước Hachiroku và mọi người đang nhìn tôi đầy lo lắng, tôi giơ ngón cái lên ra hiệu cứ yên tâm."
2536 = "Về rail shop uống trà của Paulette, nhiệt độ cơ thể dần trở lại từ đầu ngón tay."
2539 = "Tôi như hiểu được ý đồ của Reina. Nhưng, trong mưa gió này, liệu chim sẻ có bay được không?"
2549 = "Dự cảm xấu ngày càng đậm—— rồi trong chớp mắt nó thành hiện thực."
2555 = "Tôi cất cẩn thận \\x%l運転体;#00ffc040;thân điều khiển%l;#; vào \\x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#;, đứng dậy—— thì Hachiroku vẫn chưa đứng lên."
2564 = "Một đầu của vùng cấm vào, điểm Navi hạ cánh khẩn cấp đầu tiên."
2576 = "Tôi để Hachiroku đứng dậy xuống trước, rồi tôi cũng xuống sân ga."
2580 = "Tôi thêm vào những lần hô \\x%l喚呼;#00ffc040;hô xác nhận%l;#; tỉ mỉ mà bình thường không làm để tập trung lại, rồi dần giảm độ giảm tốc."
2588 = "Trước khi tôi kịp chỉ thị, tay Hachiroku đã cầm bút——"
2591 = "Có phải vì ảnh hưởng của việc đổi thân quá nhiều không, tôi hoàn toàn không cảm nhận được hơi ấm thường ngày của Hachiroku."
2598 = "Vì vậy tôi nắm chặt tay, cố truyền hơi ấm của mình sang dù chỉ một chút."
2607 = "Chắc còn nhiều cuộc hỏi thăm khác nữa, câu trả lời cực kỳ hành chính, và vì thế nhanh chóng chính xác."
2608 = "Để hỏi xem đã về chưa, và nếu chưa về thì xin cách liên lạc với Houshou Mototada, vì vậy."
2614 = "Mưa tạt ngang lộp độp, càng lúc càng mạnh. Mạnh đến mức như muốn vỡ kính bay vào trong."
2623 = "Hachiroku lập tức nhìn xa xăm, rồi từ từ lắc đầu."
2624 = "Vậy nên tôi tự kiểm tra đồng hồ, rồi hô \\x%l喚呼;#00ffc040;hô xác nhận%l;#;."
2640 = "Hôm qua Nagi nghỉ làm phụ lái, cùng Fukami đi tiếp khách đoàn xuôi sông Kuma."
2676 = "Paulette cũng vừa soát vé xong thì phải."
2677 = "Giọng nói đầy phấn khích. Ống nghe được đặt xuống đầy mạnh mẽ."
2678 = "Ánh mắt Paulette hướng ra ngoài cửa sổ."
2679 = "Paulette lập tức chộp lấy ống nghe. Vậy thì giao bên đó cho cô ấy——"
2684 = "Thay chỗ Reina, ông Akai, trụ trì và vợ trụ trì chạy vào."
2685 = "Dù mất thời gian, ở đây phải chọn phương pháp chắc chắn hơn dù chỉ một chút."
2689 = "Thời tiết thế này mà."
2690 = "Đôi mắt nhìn lại tôi…… vẫn bình tĩnh như mọi khi."
2697 = "Chắc chắn là do mệt mỏi ảnh hưởng."
2698 = "Chị Mayami dường như cũng đã hiểu."
2714 = "Vừa nói, chị Mayami vừa trải bản đồ ra cho tôi."
2716 = "Chạy thở hổn hển vào rail shop. Với chị Mayami thì tất nhiên tôi đã gọi điện trước."
2717 = "Chị Mayami liếc nhìn Hachiroku một cái."
2719 = "Chị Mayami đứng giữa những người nói sẽ giúp đỡ, quyết định phân công nhanh nhẹn."
2724 = "Đúng vậy thật."
2728 = "Đột nhiên, Reina bất chấp mưa chạy ra ngoài cửa——"
2741 = "Được Paulette chỉ ra, tôi thẳng lưng lên."
2744 = "Giọng nói giống hệt lần trả lời đầu tiên. Tất nhiên, không phải giọng của Hibiki."
2760 = "Vừa đến rail shop, cái đầu đang cúi sâu định cúi nữa thì khựng lại."
2775 = "Mà này…… có phải tôi đã bao bọc quá mức không. Nếu có chuyện gì thì từ phía bên kia———— à!"
2778 = "Trong lúc nói chuyện, nỗi lo lắng dâng lên."
2794 = "Sớm hơn, nhẹ hơn—— phanh đầu tiên thật nhẹ, nạp lại khí nén."
2802 = "Đây là…… bản đồ từ mấy chục năm trước. Có vẻ là bản đồ thời mỏ than Jutsusen còn hoạt động."
2807 = "Đang giữ đúng tốc độ giới hạn. Giảm tốc đúng cách."
2813 = "Còn một chút nữa, thêm chút nữa—— nghĩ vậy thì ý thức cũng dần có thêm dư dả."
2825 = "Những việc như mọi khi, nhưng giờ đây, hơn hết là đáng tin cậy."
2826 = "Tìm kiếm từ trên không chắc chắn hiệu quả cao, nhưng với thời tiết xấu này—— chưa nói đến bỏ sót, còn có nguy cơ thảm họa thứ cấp."
2834 = "Điện thoại reo liên tục. Khuôn mặt quen, khuôn mặt lạ—— người ta tập trung lại liên tục."
2846 = "（――Không.）"
2862 = "（♪～）"
2865 = "（Cộc, cộc.）"
2873 = "（À…… đây mới chính là Ohitoyo.）"
2875 = "（À, không, ra vậy……）"
2876 = "（Cạch!）"
2877 = "（Cạch.）"
2878 = "（Hử?）"
2882 = "（Cái gì—— lạnh ngắt thế này.）"
2885 = "（Ohitoyo là thị trấn của sự kết nối giữa người với người——）"
2887 = "（Tách.）"
```

## Kết bài
夜の嵐 là file thứ năm được audit toàn bộ, và nó xác nhận quy luật đã thấy ở bốn file trước — cột Việt bị xáo trộn rải rác từ lúc dịch trên Sheets, gần một nửa chương (199/443 dòng, 44,9%) đang hiển thị sai lời thoại so với voice — nhưng file này còn cho thêm manh mối về nguồn gốc lỗi: 167 câu sai là bản sao của một dòng khác trong cùng file, và 32 câu còn lại là bản sao từ chương Hachiroku 12 ngay trước đó, tức lỗi không chỉ xáo trộn trong một file mà còn tràn qua lại giữa các chương. Tin tốt là JP và TW vẫn khớp nhau, nên mọi dòng sai đều sửa được chỉ bằng cách dịch lại từ JP/TW, và khối TOML trong bản này đã dịch lại đủ cả 199 dòng, kiểm tra parse 199/199.

Việc còn lại của riêng file này chỉ là hai quyết định thuật ngữ của Hieu (湯医: Yui/Yunoi; コン: Kuu/Kon) — 御一夜 đã chốt 19/11 là "Ohitoyo" và khối sửa đã đổi theo — rồi áp dụng khối TOML và chơi thử chương để nghiệm thu. Còn về tổng thể dự án, năm file đã audit xong đã có 133 + 255 + 299 + 374 + 199 = 1.260 dòng sai, và phát hiện tràn chương sang Hachiroku 12 cho thấy nên đưa Hachiroku 12 vào danh sách audit tiếp theo, cùng với file còn lại của Hachiroku 13 (実りの秋) và Nagi_Fukami 08a.

---
**Bổ sung 19/11 (quét っ toàn dự án):** 2 giá trị sửa trong khối trên đã được sửa lại chỗ gasp — 2068 「!!?」→「Ư!!?」, 2334 "…nắm lấy tay tôi——!"→"…nắm lấy tay tôi——Ư!". Giá trị sweep thay thế giá trị audit (audit làm mất gasp). Khối TOML đã parse lại: 199/199 key, khớp JSON. Tổng số dòng sai không đổi (199).

---
**Bổ sung 19/11 (quyết định B8 — Hieu):** 2 dòng "Kuu" (1929, 2551) chuyển sang danh sách sửa: JP cả hai dòng đều là コン (tên nhân vật cáo trắng), không phải くぅ — sửa thành "Kon". File này giờ sai 201/443 (was 199).

```toml
[script]
1929 = "「Cảm ơn Kon và Kato Suzume nhé. Reina, anh sẽ trả tiền. Em hãy đãi tụi nó đậu phụ rán loại thượng hạng và bánh mì thật thịnh soạn vào nhé.」"
2551 = "Tôi lao xuống sân ga như lăn, thấy Reina đi cùng Kon và Kato Suzume đang ướt sũng."
```
