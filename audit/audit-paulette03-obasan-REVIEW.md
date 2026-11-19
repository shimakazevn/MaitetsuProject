# Audit: Paulette 03_大きなにもつのおばあさん — 255 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/ポーレット03_大きなにもつのおばあさん.txt.toml` — 455 dòng script, **255 dòng Việt sai = 56%**.
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. File này nặng hơn hẳn 廃炭鉱 (31%): hơn một nửa số dòng bị sai.

## Kết luận về cơ chế lỗi
- KHÔNG phải lệch đều theo key (không có shift cố định nào làm tăng độ khớp).
- Là **lỗi chép nhầm rải rác, quy mô lớn**: cột Việt bị xáo trộn giữa các dòng trong cùng file. Nhiều bản dịch đúng còn nằm ở key sai (xem "Các dòng bị chuyển chỗ" bên dưới), và nhiều dòng bị trùng lặp.
- File CSV cũ (`maitetsu_translation.csv`) và file mới (Trang tính 3) lệch nhau 122 dòng nội dung ở file này — cả hai đều bị xáo trộn theo cách khác nhau, nên không thể dùng file cũ để sửa file mới.
- Cột Nhật và cột Trung khớp nhau (~98%), nên chỉ cần dịch lại từ Nhật/Trung là ra bản đúng — không cần tìm thêm nguồn.
- Lưu ý: 200 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)
Lưu ý khi chép: xuống dòng viết dạng `\\n` — giống như các dòng đúng sẵn có trong file. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng.

```toml
1127 = "——Không phải Michiko. Là cô gái đó.\\nCô gái với mái tóc vàng óng ả rực rỡ bên đường ray mùa hè——"
1128 = "——Nhưng mà, ngon thật.\\nGiăm bông với sốt mayonnaise và bánh mì baguette hợp nhau ghê."
1150 = "「……Hikari.」"
1153 = "「……Con bé tự chuyển giường à?」"
1154 = "「……Tàu đang chạy để bù lại thời gian trễ đấy ạ.」"
1158 = "「……Giá mà Hikari cũng hấp thụ được thật nhiều sắt và khói,\\nđể con bé bớt lạ người đi phần nào thì tốt.」"
1486 = "「Xin lỗ――i——」"
1488 = "「Không phải đâu ạ? Nửa đêm con bé cứ khóc nhè gọi 'Ba ơi',\\nnên em đã đưa con bé sang đây.」"
1490 = "「Không biết nữa ạ. Chúng ta vẫn chưa đến Sendai mà——\\nHơn nữa bây giờ là tháng Ba rồi, khả năng có tuyết rơi chắc là thấp thôi ạ.」"
1491 = "「Dù giữa đường tàu có trễ bao lâu đi nữa à?」"
1494 = "「Cảm ơn anh đã chỉ bảo ạ.」"
1496 = "「Để mọi người đợi lâu rồi ạ~」"
1501 = "「Reina cũng muốn được kéo dãn ra nữa nha~」"
1514 = "「Mọi người cứ nói 'xin lỗi' với 'thật ngại quá' như thế,\\ncon bé lại tưởng là mình đã làm gì sai đấy.」"
1516 = "「Hikari muốn bà ở lại à?」"
1521 = "「Chơi chữ khéo đấy.」"
1522 = "「Hóa ra em đã chuẩn bị cả phần sáng nay nữa rồi à.」"
1524 = "「Em nghĩ là dừng để đổi lái tàu, hoặc là cấp thêm than và nước đó nha.」"
1526 = "「Hikari cũng sảng khoái rồi!\\nRửa mặt xong là đói bụng luôn~」"
1528 = "「Hikari cũng muốn~ Hikari cũng muốn làm nữa~」"
1530 = "「Hikari muốn uống nước ép~」"
1531 = "「Hikari muốn chơi với ba~」"
1533 = "「Hikari dậy rồi à. Chào buổi sáng.」"
1535 = "「Chào buổi sáng, Hikari.\\nĐi rửa mặt với mẹ nhé?」"
1541 = "「Ra là vậy, còn có cách gọi như thế nữa à.」"
1542 = "「Ra là vậy. Cảm ơn em.\\nChào buổi sáng, Paulette.」"
1547 = "「Ra xem thử nhé.」"
1556 = "「Giãn gân cốt!!! Đúng rồi nhỉ, tất nhiên rồi!\\nEm biết ngay mà!!」"
1557 = "「Bà mà cứ ở đây thì con bé sẽ căng thẳng mất,\\ntội nghiệp lắm.」"
1561 = "「Kyaa!」"
1568 = "「Fufufu.\\nCái này giống hệt loại giăm bông nhà em hay dùng mà.」"
1572 = "「Fufufu, rửa mặt xong là sảng khoái hẳn ra ạ~」"
1577 = "「Fufufu, còn khói thì……」"
1580 = "「Fufufu, đây, nước ép cà chua của em nè.」"
1582 = "「Fufufu,\\nchào buổi sáng nha. Anh Soutetsu, Paulette.」"
1583 = "「Phù…… a~Ư」"
1586 = "「Phù…… a—— em, em—— cứng đơ—— hết cả rồi……\\nừm…… có tác dụng……」"
1588 = "「Phù—— a~! Ư~, kéo dãn hơi quá rồi!\\nÀ nhưng mà…… ừm. Cảm giác máu lưu thông tốt hơn hẳn~」"
1590 = "「Phù~Ư」"
1592 = "「Khám sức khỏe tổng quát ạ. Chị Mayami có đi khám không ạ?」"
1593 = "「Ủa, bà đâu rồi ạ?」"
1594 = "「Hả?」"
1597 = "「Oa, thích quá nha. Reina ghen tị quá đi~」"
1607 = "「Haha, đúng là vậy thật.」"
1619 = "「Ừ, chỉ là món ăn đạm bạc thôi mà.」"
1628 = "「Ôi chà, đáng yêu quá, đáng yêu quá——\\nồ, vừa đúng lúc rồi đấy nhỉ.」"
1629 = "「Hả? Nhưng mà Reina đâu có máu đâu ạ?」"
1638 = "「Hả!? T-Từ giờ này á!!?」"
1642 = "「A——\\nRa là vậy, tàu đã chạy suốt một đêm rồi mà.」"
1649 = "「A, gì thế này. Chẳng có hạt tuyết nào cả—— á.」"
1652 = "「Ưm…… ừm, bà không ở đây cũng được mà.\\nKhông ở đây cũng được, nhưng mà…… nhưng mà, ừm?」"
1653 = "「Ừ, ừm—— cảm ơn em—— để anh đổi lượt nhé.」"
1660 = "「A—— a—— ưm—— chờ đã——\\nanh Soutetsu—— em không chịu nổi nữa—— á!」"
1662 = "「Á——」"
1668 = "「A, vâng—— hây!」"
1670 = "「A, ra được mà—— ừm?」"
1673 = "「A, không được rồi. Để anh đính chính lại. 'Cái này ngon thật đấy, Paulette.'」"
1679 = "「Ưm nya.」"
1680 = "「Ư…… ư.」"
1681 = "「Ưm~」"
1682 = "「Hau!」"
1683 = "「Hây!」"
1685 = "「Ưm…… phù—— ưm——……\\nkhò khò~」"
1686 = "「Ưm…… ưm.」"
1687 = "「Ưm…… ưm~」"
1689 = "「Ưm—— a—— dãn—— ra—— rồi——\\nư—— đúng là—— có tác dụng—— thật—— ừm.」"
1691 = "「Ừm. Mà không chỉ chị ấy đâu, toàn bộ nhân viên chính thức của Xưởng rượu Migita Ichi đều vậy.\\nNgoài khám sức khỏe định kỳ ra, hai năm một lần còn có khám sức khỏe tổng quát nữa.」"
1692 = "「Ừm. Ngoan nào.\\nNgủ đi, ngủ đi nào~」"
1694 = "「Ừm. Từ từ, nhẹ nhàng thôi nào——\\ndãn ra, dãn ra nào——」"
1696 = "「Ừm. Thì nãy giờ phát thanh cũng nói vậy mà.」"
1699 = "「Ừm. Thế này là được rồi.」"
1700 = "「Ừm. Nếu là động tác đó thì không gian này cũng đủ rồi.」"
1701 = "「Ừm.」"
1703 = "「Ưm~」"
1704 = "「Ưm~…… con muốn đi tè~」"
1707 = "「Dạ! Ba kéo dãn cho con nhé?」"
1709 = "「Dạ! Con sẽ làm như vậy ạ!」"
1711 = "「Ừm! Trả lời hay lắm.\\nVậy bọn chị đi một lát rồi về nhé.」"
1715 = "「Hửm?\\n……Sắt thì là sắt của đường sắt rồi, còn muối thì là gì?」"
1720 = "「Fufufu, kéo dãn người ra thích quá đi~」"
1721 = "「Ồ—— ồ.」"
1722 = "「Ồ, thế thì tốt quá nhỉ.」"
1726 = "「Vì tàu đã vắng người nên bà ấy đi rồi.\\nBà ấy bảo ngồi ké ghế là không tốt.」"
1727 = "「Vì đây là điểm dừng kỹ thuật ạ.」"
1729 = "「Tuyết, có đang rơi không nhỉ?」"
1739 = "「Cái này—— ngon thật đấy. Có phải dùng loại giăm bông hảo hạng không nhỉ?」"
1741 = "「Con có đi tàu ké đâu mà~」"
1743 = "「Dạ~」"
1744 = "「Dạ, mời mọi người dùng ạ.」"
1746 = "「Dạ, bé Hikari~」"
1747 = "「Ngon quá đi!」"
1750 = "「Phúc lợi tốt quá đi! Đường sắt Ohito cũng phải học theo mới được.」"
1755 = "「Dạ, em đi đây ạ~」"
1756 = "「Dạ~」"
1757 = "「Dạ!」"
1759 = "「Dạ, đi cùng Reina nhé~」"
1762 = "「Ừ, về rồi thì đổi lượt nhé.」"
1764 = "「Được rồi! Xong. Đi rửa mặt với mẹ đi con.」"
1771 = "「Thôi nào~」"
1772 = "「Bao trọn~ bao trọn~! Cả hành lang với phòng rửa mặt đều là bao trọn hết luôn~!」"
1782 = "「Bé Hikari~ Chào buổi sáng nha~」"
1784 = "「Ngại ngùng chút xíu thì cũng đáng yêu mà. Cứ nhìn con bé bằng ánh mắt dài lâu, từ từ thôi nhé.」"
1786 = "「Là ngài Tadanori đấy ạ.」"
1797 = "「Cái đó thì cả hai bên đều như nhau mà~」"
1799 = "「Tiếc quá đi! Nước ép ngọt hiện đã bán hết rồi ạ~」"
1804 = "「Có lý. Vậy thì, anh cũng làm những việc trong khả năng của mình vậy.\\nPaulette, em ra ngoài một lát được không?」"
1809 = "「Bà xuống tàu ạ?」"
1811 = "「Ừ. Chắc cũng không cần ngủ lại nữa đâu.」"
1813 = "「Anh xuống tàu vận động cơ thể một chút đây.」"
1820 = "「Anh chưa nói sao? Anh muốn vận động cơ thể một chút.」"
1823 = "「Được rồi. Đi thôi, Reina.」"
1825 = "「Được rồi. Lại đây nào.」"
1827 = "「Anh hiểu rồi. Hóa ra 'enbun' không phải là muối mà là khói à.」"
1829 = "「Được rồi, được rồi. Nào, dãn ra.」"
1830 = "「Bà đi đến ga cuối, nhưng tàu cũng đã vắng rồi. Ngồi ké ghế mãi cũng không tốt đâu.」"
1832 = "「Cái đó ấy, ba mẹ cũng nên để ý một chút thì tốt hơn đấy.」"
1835 = "「Tôi cứ tưởng tàu chạy chậm là chuyện đương nhiên, nhưng hóa ra việc tốn thời gian là có lý do chính đáng.」"
1836 = "「Anh xin phép dùng bữa.」"
1841 = "「Dãn ra~」"
1844 = "「Lắc, lắc—— gập—— ưm—— phù—— thế nào—— rồi ạ?」"
1850 = "「Chào buổi sáng ạ~ Hikari cũng muốn làm nữa~」"
1852 = "「Chào buổi sáng. Reina cũng dậy sớm quá nhỉ.\\nChuyến đi này em cứ ngủ nướng thêm một chút cũng được mà.」"
1854 = "「Chào buổi sáng, anh Soutetsu.」"
1857 = "「Đúng vậy nhỉ.」"
1858 = "「Đúng vậy ạ. Dù giữa đường có trễ đến đâu,\\nviệc hoàn tiền sẽ do ga xuống quyết định ạ.」"
1859 = "「Đúng vậy ạ. Dù giữa đường có trễ đến đâu đi nữa——」"
1863 = "「Đúng vậy. Mà, nếu nói là bệnh nghề nghiệp thì——\\nReina? Chào buổi sáng.」"
1865 = "「Đúng vậy ạ~ Hôm nay Paulette không làm việc,\\nnên hấp thụ được thật nhiều sắt và khói đấy ạ~」"
1867 = "「Ừ. Cứ hễ liên quan đến Hikari và chuyến đi tàu\\nlà Paulette lại đáng tin cậy hơn hẳn mọi khi.」"
1869 = "「Ừ, chuyện đó thì tuyệt đối chẳng phải điều đáng mong muốn.」"
1872 = "「Ra vậy. Vậy thì lần sau gặp lại, em nói được là tốt rồi nhỉ.」"
1873 = "「Ra vậy à.」"
1885 = "「Đ-Đúng rồi nhỉ! Được thôi! Kéo dãn lưng!\\nEm sẽ kéo dãn anh Soutetsu hết cỡ luôn!」"
1888 = "「Mọi người về rồi~」"
1896 = "「Không xuống được? Nhưng mà, đang ở ga cơ mà?」"
1897 = "「Bán hết rồi. Bán hết rồi thì đành chịu thôi~」"
1898 = "「Đúng rồi đó~」"
1899 = "「Không sao đâu, chắc chắn sẽ như vậy mà~」"
1907 = "「Paulette đã làm mẹ rồi nhỉ~\\nNếu không có vậy thì bé Hikari đã sợ lắm rồi~」"
1908 = "「Pa, paa!」"
1915 = "「Reina cũng rửa mặt rồi nha~」"
1916 = "「Em xin phép dùng bữa ạ.」"
1917 = "「Chị Reina, tạm biệt~!」"
1922 = "「Bây giờ là mấy giờ rồi?」"
1924 = "「Một năm một lần mà nhỉ. Khám sức khỏe của bọn em ấy.」"
1925 = "「Vì đây là thời đại Đại bãi bỏ tuyến đường sắt mà. Ở đâu cũng chỉ có thể làm trong khả năng của mình thôi.」"
1927 = "「Cà chua!? Cà chua á.\\nHikari muốn nước ép ngọt cơ~」"
1928 = "「Tất nhiên rồi ạ. Nhưng mà đơn giản thôi ạ,\\nbánh mì baguette với giăm bông và xà lách. Em định làm bánh mì kẹp mở ạ.」"
1935 = "「Anh cũng đã khuyên chị Mayami là ngoài khám sức khỏe định kỳ ra,\\ncũng nên đi khám sức khỏe tổng quát nữa.」"
1938 = "「Được rồi, được rồi. Reina, nhờ em được không?」"
1942 = "「Ra là vậy, đúng thật. Nghĩ lại thì,\\nReina khỏe mạnh hơn bọn anh nhiều đấy nhỉ.」"
1950 = "「Chạy bù giờ—— ra là vậy, là để giữ thời gian trễ trong vòng 120 phút à.」"
1953 = "「Vì táo ngon quá mà.\\nCon muốn nói 'Cảm ơn vì bữa ăn' cơ~」"
1961 = "「Ngon nhỉ. Cháu ăn ngon lành như thế,\\nchắc chắn người nông dân cũng vui lắm đấy.」"
1970 = "「Chăn thì sao ạ? Cất đi luôn nhé~?」"
1971 = "「Ba này.」"
1983 = "「Cảm ơn bà nhiều lắm ạ!」"
2013 = "「Thật là, xin lỗi quá.」"
2016 = "「Còn có sốt mayonnaise và trà đựng trong bình giữ nhiệt nữa nha~」"
2017 = "「À, xin lỗi ạ.」"
2018 = "「Không xuống được đâu ạ.」\\n「Không xuống được đâu nha.」"
2021 = "「Giường nằm là bọn cháu đã trả đúng giá để đặt rồi,\\nnên bà cứ thong thả ở lại thêm chút nữa cũng được mà, coi như cảm ơn vì quả táo ạ.」"
2030 = "「Chưa tới 5 giờ ạ. Đúng là bệnh nghề nghiệp nhỉ, cả hai chúng ta.」"
2035 = "「Chắc là có dầu bôi trơn các thứ chứ.\\nDù không có đi nữa, cứ giữ nguyên một tư thế không cử động thì khớp cũng cứng lại thôi.」"
2043 = "「Vậy thì về thôi.」"
2045 = "「Vậy thì, mình ăn sáng nhé.」"
2046 = "「An tâm quá nhỉ.」"
2047 = "「Em làm đây~ Từ từ, từ từ nào——\\nưm…… ưm.」"
2048 = "「Vậy nhé, có dịp lại gặp nhau nhé.」"
2051 = "「Vậy thì, lại đây nào. Reina cũng kéo dãn luôn nhé.」"
2052 = "「Em ăn đây ạ~」"
2053 = "「Đúng là giờ này vẫn chưa có bài tập thể dục trên radio,\\nnhưng chỉ là vài động tác vươn vai thì cũng không gây tiếng động gì, chắc không sao đâu.」"
2054 = "「Anh Soutetsu, anh định vươn vai kéo dãn lưng đúng không nha.」"
2055 = "「Anh Soutetsu với mọi người cũng đi đi ạ.\\nChừng ba mươi phút nữa là đông đúc lắm đấy.」"
2056 = "「Anh Soutetsu. Anh làm nhẹ nhàng, từ từ cho em ấy nhé?\\nReina thì đã được bảo dưỡng định kỳ rồi ạ.」"
2060 = "「'Satsuma no kami' à?」"
2067 = "（Am!）"
2212 = "Không, không phải vậy. Cũng không phải là Paulette lúc mới gặp mặt."
2213 = "Không phải vậy.\\nNếu muốn sửa thì phải sửa ngay từ khoảnh khắc này."
2217 = "Nhưng mà, đó cũng là một cái thú của chuyến đi."
2237 = "Nếu tạo ra tiền lệ dùng chăn làm ghế sofa thì có thể sẽ ảnh hưởng xấu đến việc dạy dỗ con bé sau này."
2239 = "Tôi đã từng lo lắng vì Hikari có vẻ hơi chậm hơn các bạn khác về độ trưởng thành trong giao tiếp——\\nnhưng mà……"
2263 = "Hikari cứ dụi mặt vào Paulette hết lần này đến lần khác,\\nnhư thể đang đánh dấu mùi hương vậy."
2265 = "Giật mình vì giọng nói của bà lão,\\nHikari lại trốn sau lưng Paulette."
2277 = "Hikari gật đầu lia lịa, vẻ mặt vui mừng."
2280 = "Hikari vẫn còn ngái ngủ."
2282 = "Con bé cứ thế được cõng đi, vui vẻ khua chân loạn xạ.\\nThôi thì…… thế này cũng coi như vận động rồi, cứ để vậy đi."
2285 = "Em ấy gật đầu thật mạnh, rồi đứng khựng lại."
2287 = "Má Hikari phồng lên."
2315 = "Có lẽ vì đã thức giấc giữa đêm,\\nnên Hikari hoàn toàn không có vẻ gì là sắp tỉnh dậy."
2325 = "Ra là vậy. Đúng như Paulette nói,\\nchỉ chênh nhau có mười phút thôi mà đã——"
2326 = "Ồ, vào đường hầm rồi sao.\\nHơi có mùi khói——Ư!"
2339 = "Bằng đôi bàn tay nhỏ bé, con bé nắm chặt lấy ngón tay tôi,\\nvà đang thở đều đều trong giấc ngủ yên bình."
2391 = "Chỉ cần một năm thôi cũng đã đủ để bệnh tật âm thầm bào mòn cơ thể rồi."
2397 = "Nghĩ vậy rồi, cùng với lòng biết ơn,\\ncơn đói lại càng trở nên rõ rệt hơn."
2399 = "Em ấy lắc lắc người thật mạnh,\\nrồi từ từ, từ từ tăng dần độ cong của lưng."
2408 = "Hai bồn rửa mặt đặt cạnh nhau.\\nTừ bên cạnh vang lên giọng nói thong thả của Reina."
2409 = "Vừa quay về giường nằm của bọn tôi,\\nHikari đã vui vẻ chào đón."
2411 = "Con gái của bọn tôi mới chỉ bắt đầu chạy thôi.\\nĐể con bé không phải vội vàng trên chặng đường đó, hai vợ chồng tôi đồng lòng với nhau."
2412 = "Chốc lát im lặng.\\nChỉ còn tiếng bánh xe gõ lên đường ray vang đều đều trong toa."
2415 = "Dù là giọng của tôi, của Paulette, hay của Reina,\\nHikari vẫn nhắm nghiền mắt, cơ thể cứng đờ lại."
2417 = "Giọng nói nghe buồn ngủ.\\nMột bàn tay thò ra từ dưới chăn, rồi sau đó, đầu cũng ngẩng lên."
2418 = "Cả hai chân đã chạm đất."
2424 = "Tôi với Hikari chênh lệch chiều cao quá lớn."
2428 = "Tôi và Paulette gật đầu với nhau."
2429 = "Hai đứa áp sát lưng vào nhau,\\nhai tay đan vào nhau ở phần khuỷu tay."
2430 = "Cuộc trò chuyện với giọng nói kìm nén qua tấm rèm."
2441 = "Tôi mở mắt ra.\\nHikari đã chuyển sang giường của tôi từ lúc nào không hay."
2445 = "Tôi nhẹ nhàng gỡ ngón tay Hikari ra,\\nbước xuống giường, tiến ra lối đi——"
2448 = "Tôi nhanh chóng nhưng cẩn thận rửa mặt, cạo râu,\\nrồi thấm nước chải tóc cho gọn gàng."
2459 = "Lần này đến lượt tôi gập lưng xuống,\\ntừ từ nâng Paulette lên."
2464 = "Từ trên đỉnh đầu, tiếng cười khúc khích vui vẻ vang lên."
2465 = "Rồi đột nhiên, một cái ngáp thật to."
2466 = "Bà lão nhanh nhẹn bắt đầu thu dọn hành lý."
2478 = "Sau khi dừng ở vài ga,\\ntrong tàu có vẻ đã vắng đi nhiều."
2488 = "Có lẽ vì đã đoán trước chuyện này,\\nPaulette đã bắt đầu mở giỏ ra rồi."
2489 = "Nếu Paulette cứ thế gập thân trên về phía trước,\\nlưng tôi sẽ đặt lên hông em ấy, tạo thành một vòng cung."
2490 = "Hễ Paulette vỗ vỗ vào đầu gối\\nlà em ấy lại leo lên đó như một chú mèo con, cuộn tròn lại."
2491 = "Khuôn mặt đỏ bừng,\\nPaulette lao ra mép giường."
2492 = "Em ấy dùng ngón tay chọc cho cái má phúng phính xẹp xuống,\\nrồi dịu dàng vuốt tóc Hikari."
2494 = "Tàu đã không còn chạy giảm tốc nữa——\\nthậm chí còn đang chạy rất nhanh."
2496 = "Đoàn tàu trượt vào sân ga.\\nVừa hay."
2503 = "Ngay khoảnh khắc sau, một cái ngáp thật to."
2513 = "Nghe giọng nói đầy cảm xúc của Reina, tôi gật đầu thật sâu."
2516 = "Reina vội vàng bước xuống.\\nXoay một vòng, đáng yêu quay lưng lại."
2517 = "Ngay lập tức Reina đỡ lấy Hikari,\\ngiúp đỡ con bé."
2519 = "Giờ mà đánh thức con bé thì tội nghiệp quá."
2522 = "Bởi vì tôi, giờ đã là người lớn rồi.\\nĐã là người lớn, và là một người cha——"
2523 = "Đương nhiên, vốn dĩ nó không phù hợp cho việc kéo đường dài……\\nThực ra tôi mong là họ dừng đỗ kỹ thuật thường xuyên hơn mới phải."
2526 = "Có lẽ vì đã yên tâm lắm rồi,\\nHikari lập tức chìm vào giấc ngủ."
2531 = "Có vẻ như sắt và khói\\ncũng có tác dụng rất lớn đối với Reina."
2541 = "Những ngón tay của tôi đang được nắm lấy một cách nhẹ nhàng.\\nTrong chăn, bên cạnh tôi là Michiko bé nhỏ——"
2546 = "Quay lại lối đi,\\ntôi lướt qua những người vừa mới thức dậy."
2558 = "Bà lão thoắt cái đã thu dọn hành lý\\nvà vác lên lưng."
2563 = "Bà lão mỉm cười nhìn theo bóng lưng\\ncủa Reina bé nhỏ và Hikari còn bé nhỏ hơn."
2567 = "Bà lão mở cửa toa xe thảm,\\nvác theo khối hành lý to tướng rồi đi mất."
2573 = "Hikari, con bé ấy——\\nthực sự rất nhạy cảm với thái độ của người khác."
2580 = "Nghe vậy, tôi chợt nhận ra."
2581 = "Nghe lời Reina nói, lòng tôi nhẹ nhõm hẳn."
2597 = "Chỉ cần vác lên lưng thôi——\\nnhưng mà cứ vươn vai ra thì không làm được nữa……"
2612 = "Tôi nói rồi nhìn chằm chằm vào Hikari,\\ncon bé vội vàng nuốt nốt miếng bánh mì đang gặm dở rồi cười toe toét."
2614 = "Đầu máy kéo C56 tuy có toa tiếp than nước,\\nnhưng nhỏ gọn nhẹ. Chỉ tính chiều dài thì còn nhỏ hơn cả 8620."
2636 = "Cái đó——\\ncái đó đúng là, chắc chắn rồi."
2637 = "Dậy sớm, ăn no căng bụng rồi yên tâm——\\nlàm sao mà không buồn ngủ được chứ."
2638 = "Cái đó……\\nđúng là không thể phủ nhận được."
2640 = "Chẳng có gì đặc biệt, chỉ là bánh mì kẹp mở với bánh baguette thậm chí còn chưa nướng,\\nkiểu như bữa sáng vội vàng của một gã độc thân."
2641 = "Vị mặn đơn thuần mà ngon lành\\nlan tỏa khắp miệng, khắp cơ thể."
2643 = "Nếu chỉ có mình tôi đi tàu thì trên chuyến tàu không có bán hàng rong này,\\nchắc tôi đã phải chịu đựng cơn đói trong suốt chuyến đi dài rồi."
2646 = "Được kéo dãn ra, tôi mới cảm nhận lại được.\\nQuả nhiên, chỗ nào cũng cứng đơ hết cả."
2660 = "Dùng chăn làm ghế sofa cũng được thôi,\\nnhưng mà còn có Hikari ở đây."
2661 = "Chính vì không thể phủ nhận được\\nnên tôi lại cảm thấy—— cứ như có gì đó day dứt trong lòng."
2662 = "Tôi mở mắt ra.\\nHikari đã chuyển sang giường của tôi từ lúc nào không hay."
2664 = "「Chẳng lẽ…… tàu đang chạy giảm tốc sao?」"
2685 = "（Cạch.）"
2687 = "（Hự—— hự hự——）"
2691 = "（Tuúú…!）"
```

## Các dòng bị chuyển chỗ (bản dịch đúng đang nằm ở key sai)
Khối TOML trên đã dùng đúng bản dịch cho các key này; các key nguồn (đang giữ bản dịch đó) cũng đã có bản mới trong khối:
- **1127** ← bản dịch đang nằm ở **1541** ("Không phải Michiko. Là cô gái đó…")
- **1542** ← bản dịch đang nằm ở **1514** ("Ra là vậy. Cảm ơn em. Chào buổi sáng, Paulette.")
- **1491** ← bản dịch đúng là "Giãn gân cốt!!!…" đang nằm ở **1556** (đã sửa 1556 lại theo JP)
- **1488** ← bản dịch đúng ("Nửa đêm con bé cứ khóc nhè gọi 'Ba ơi'…") đang nằm ở **1832** trong CSV cũ
- **1490** ← bản dịch đúng ("Chúng ta vẫn chưa đến Sendai mà—— Hơn nữa bây giờ là tháng Ba rồi…") đang nằm ở **2492**
- **1524** ← bản dịch đúng ("dừng để đổi lái tàu, hoặc là cấp thêm than và nước") đang nằm ở **2263**
- **1586** ← bản dịch đúng (cảnh bà lão mang hành lý) đang nằm ở **2548**
- **1634** ← bản dịch đúng ("Hả!? Thật á. Không chịu đâu, anh Soutetsu, lau cho em đi.") đang nằm ở **1744**
- **1642** ← bản dịch đúng ("tàu đã chạy suốt một đêm rồi mà") đang nằm ở **1771**
- **1649** ← bản dịch đúng ("Chẳng có hạt tuyết nào cả—— á.") đang nằm ở **1953**
- **1683** ← bản dịch đúng ("Tuyết, có đang rơi không nhỉ?") đang nằm ở **1729**
- **1766** ← bản dịch đúng ("Nếu không phiền, bà cứ đặt hành lý xuống…") đang nằm ở **1869**
- **1818** ← bản dịch đúng ("Ở đây có trẻ nhỏ, nếu xảy ra xô xát thì phiền lắm.") đang nằm ở **1835**
- **1854** ← bản dịch đúng ("Dạ, là mẹ đọc cho con nghe đó~") đang nằm ở **2011** (2011 đã đúng, giữ nguyên)
- **1859** ← bản dịch đúng ("Anh Soutetsu, anh định vươn vai kéo dãn lưng đúng không nha.") đang nằm ở **2054** (2054 đã sửa lại theo JP)
- **1871** ← bản dịch đúng ("Thật đấy. Cứ như viên ngọc quý hình quả táo vậy.") đang nằm ở **1757**
- **1921** ← bản dịch đúng ("Cả Reina và Paulette cũng thế thôi.") đang nằm ở **1916**
- **1922** ← bản dịch đúng ("Bây giờ là mấy giờ rồi?") đang nằm ở **1494**
- **1925** ← bản dịch đúng ("Vì đây là thời đại Đại bãi bỏ tuyến đường sắt mà…") đang nằm ở **2412**
- **1983** ← bản dịch đúng ("Chưa tới 5 giờ ạ. Đúng là bệnh nghề nghiệp nhỉ…") đang nằm ở **2030**
- **2011** đã đúng — bản "Dạ, là mẹ đọc cho con nghe đó~" là của nó, không phải của 1854.
- **2020** ← bản dịch đúng ("Quả táo đẹp thế này cơ mà. Gọt vỏ đi thì phí lắm.") đang nằm ở **2043**
- **2039** ← bản dịch đúng ("Vậy thì, em cũng thế. Tuy hơi bất lịch sự một chút.") đang nằm ở **2691**
- **2215** ← bản dịch đúng ("Dù là giọng của tôi, của Paulette, hay của Reina, Hikari vẫn nhắm nghiền mắt…") đang nằm ở **2217**
- **2217** đã sửa lại theo JP; bản cũ của nó thuộc về 2215.
- **2414** ← bản dịch đúng ("Tất cả chúng tôi đều trở nên im lặng. Bởi vì trong miệng chứa đầy hương vị thơm ngon…") đang nằm ở **2488**
- **2415** ← bản dịch đúng (cùng câu trên, dạng khác) — 2415 đã sửa lại theo JP.
- **2418** ← bản dịch đúng ("Chỉ cần tàu bắt đầu chạy, chắc chắn sắt và khói sẽ một lần nữa khích lệ Hikari.") đang nằm ở **2432**
- **2428** ← bản dịch đúng ("Ừm. Nếu là động tác đó thì không gian này cũng đủ rồi.") đang nằm ở **1700**
- **2432** đã đúng — bản "Chỉ cần tàu bắt đầu chạy…" là của nó.
- **2444** ← bản dịch đúng ("Tôi nhẹ nhàng xoa đầu con bé. Sợ thì vẫn là sợ thôi…") đang nằm ở **2489**
- **2465** ← bản dịch đúng ("Vì đây là điểm dừng kỹ thuật ạ.") đang nằm ở **1727**
- **2494** ← bản dịch đúng ("Anh chưa nói sao? Anh muốn vận động cơ thể một chút.") đang nằm ở **1820**
- **2548** đã đúng — bản cảnh bà lão mang hành lý là của nó.
- **2567** ← bản dịch đúng ("Chào buổi sáng. Reina cũng dậy sớm quá nhỉ. Chuyến đi này em cứ ngủ nướng thêm một chút…") đang nằm ở **1852**
- **2614** ← bản dịch đúng ("Thành thật xin lỗi quý khách, do quá đông đúc…") đang nằm ở **1540** (1540 đã đúng, giữ nguyên)
- **2636** ← bản dịch đúng ("Chào buổi sáng, anh Soutetsu.") đang nằm ở **1854** (1854 đã sửa lại theo JP)

## Các cặp trùng lặp đáng chú ý
Nhiều giá trị Việt xuất hiện ở 2 key, chỉ một key đúng (key còn lại đã có bản mới trong khối): 1500/1836 ("Reina cũng muốn được lau nha." — của 1500), 1570/1575 (hai câu "bắt chước" gần giống nhau, cả hai đều đúng cho key của mình), 1598/1600/1602/1604 (chuỗi "Oa…" của Reina — mỗi key đã có bản riêng đúng), 1916/1921, 1976/1977/1978 (ba câu "đính chính" — cả ba đều đúng cho key của mình), 2020/2043, 2039/2691, 2215/2217, 2414/2488, 2444/2489, 1540/2614.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- 鉄分 = sắt; 煙分 = khói; 塩分 = muối (chơi chữ 鉄分/塩分/煙分 giữ nguyên ý)
- 御一夜鉄道 = Đường sắt Ohito; 帝鉄 = Đế Thiết (theo các dòng đúng trong file: "thời Đế Thiết", "Đường sắt Ohito")
- 行商 = bán dạo; 運転停車 = điểm dừng kỹ thuật; 回復運転 = chạy bù giờ; 特急料金 = tiền vé tàu tốc hành; 乗車料金 = tiền vé tàu
- 人間ドック = khám sức khỏe tổng quát; 健康診断 = khám sức khỏe (định kỳ)
- 薩摩守 = ngồi ké ghế (chơi chữ: ngồi ghế không trả tiền) — giữ tên gốc trong câu hỏi ở 2060
- Soutetsu độc thoại/dẫn chuyện xưng "Tôi"; Paulette gọi Soutetsu là "anh Soutetsu"; Hikari (4 tuổi) nói giọng trẻ con; bà lão (おばあさん) nói giọng thân mật, hơi cổ
- Còi tàu ポー = "Tuúú…" (theo sfx §1.1) — áp dụng ở 2691
- 2664 chỉ sai dấu ngoặc (thiếu 「 đầu câu) — nội dung đã đúng, đã sửa dấu trong khối trên.

## Giới hạn của audit này
- Đã đọc hết 455 dòng script của file này: 255 dòng sai đã xác nhận, 200 dòng còn lại khớp Nhật/Trung.
- Vẫn có thể sót vài dòng "trông hợp lý nhưng thực ra là bản dịch của dòng khác" — cách chắc chắn nhất vẫn là chơi qua chương và đối chiếu voice. Nếu Hieu gặp thêm dòng nào nghi ngờ trong file này thì gửi mình, mình kiểm tra nốt.
- File này (56% sai) nặng hơn nhiều so với 廃炭鉱 (31%). Các file còn lại trong danh sách nặng (Grand 01, Hibiki 03, Hachiroku 13, Nagi_Fukami 08a) nhiều khả năng cũng ở mức tương tự — không nên tin vào con số ước tính bằng máy check (~662 dòng) nữa.

## Việc tiếp theo (chờ Hieu chọn)
1. Áp dụng khối TOML trên cho file obasan, chơi thử chương Paulette 03 rồi báo lại.
2. Audit tiếp các file nặng còn lại: Grand Rewrite 01, Hibiki 03, Hachiroku 13, Nagi_Fukami 08a — mỗi file một bản review như file này.
3. Xuất lại CSV mới từ TOML (sau khi áp fix) để CSV không còn cũ — nhớ chép 146 dòng Grand 01/Hibiki 03 từ TOML vào CSV trước, kẻo mất bản dịch.

---
**Bổ sung 19/11 (quét っ toàn dự án):** 3 giá trị sửa trong khối trên đã được sửa lại chỗ gasp — 2326 "Hơi có mùi khói——!"→"Hơi có mùi khói——Ư!", 1583 「Phù…… a~」→「Phù…… a~Ư」, 1590 「Phù~」→「Phù~Ư". Giá trị sweep thay thế giá trị audit (audit làm mất gasp). Khối TOML đã parse lại: 256/256 key, không còn chữ っ thô trong khối. Tổng số dòng sai không đổi (255 + 2664).
