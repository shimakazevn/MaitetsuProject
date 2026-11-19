# Audit: Hibiki 03_湯富院 — 374 dòng Việt sai (đã đối chiếu JP + TW)

File: `02_Hibiki/日々姫03_湯富院.txt.toml` — 434 dòng script, **374 dòng Việt sai = 86,2%**.
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. Đây là file nặng nhất trong 4 file đã audit toàn bộ tới nay: 廃炭鉱 31%, Grand 01 45,6%, obasan 56% — và Hibiki 03 lên tới 86,2%. Chỉ còn 60/434 dòng đúng.

## Phương pháp và số liệu kiểm chứng
- Đã đọc **hết 434/434 dòng script** (key 1396–3027, không liên tục), đối chiếu từng dòng với JP + TW theo nghĩa, người nói, thoại/lời dẫn. Không ngoại suy tổng dự án từ file này.
- Phân loại 374 dòng sai: **lệch nội dung 330**, **chưa dịch (còn nguyên tiếng Trung trong TOML) 44**, **dịch thiếu (cụt câu) 0**, **không chắc chắn 0** (xem ghi chú 2158 bên dưới — dòng đó có bản dịch đúng đã xác nhận bằng chuyển chỗ, chỉ còn câu hỏi về cách gọi 冥軍).
- Thoại sai 241/286 (84,3%); lời dẫn (monologue) sai 133/148 (89,9%). Lỗi gần như bao phủ toàn bộ chương, không chừa cảnh nào: Soutetsu sai 107/123 (87,0%), Hibiki sai 78/87 (89,7%), **Mikuro sai 34/34 (100% — không một dòng thoại nào của Mikuro đúng)**, Thị trưởng Yufuin sai 22/42 (52,4% — nhân vật ít sai nhất trong file), lời dẫn sai 133/148.
- **Không có key-shift sạch:** thử shift -5..+5 trên key, độ khớp thoại/dẫn chỉ dao động khoảng 0,59–0,62, không shift nào cải thiện rõ rệt so với shift 0 (0,59). Heuristic thoại/dẫn báo 160/390 dòng không trống (41%) — cao gấp gần 4 lần Grand 01 (~11%) — và đó vẫn là đánh giá thấp so với con số thực 86,2%, vì phần lớn lỗi là lệch cùng loại (thoại→thoại sai, dẫn→dẫn sai) mà heuristic không bắt được.
- **44 dòng "chưa dịch" chính là 44 dòng CSV để trống:** kiểm tra chéo cho thấy TOML VN == TW ở đúng 44/44 dòng này — tức trong TOML chúng không phải bản dịch Việt mà là câu tiếng Trung giữ làm placeholder. Giống Grand 01 (100/100): **không có bản dịch nào để mất ở 44 dòng này — việc cần làm là dịch mới từ JP/TW**, và khối TOML bên dưới đã xử lý cả 44 dòng (17 dòng trong số đó lấy lại được bản dịch đúng đang nằm sai chỗ ở key khác, 27 dòng còn lại dịch mới). Với kết quả này, toàn bộ 146 dòng chưa dịch của "Trang tính 3" đã được xác nhận: Grand 01: 100 + Hibiki 03: 44 + 2 dòng lẻ (lr真闇追加01/02) — tất cả đều là placeholder tiếng Trung, không dòng nào có bản dịch Việt để mất.
- **Tự kiểm tra độ sót:** sau khi đối chiếu xong, đã kiểm tra lại toàn bộ các dòng cho là đúng bằng cách đọc trực tiếp giá trị CSV của từng dòng nghi vấn ngắn (VD: 2340 "Xe ngựa du lịch... tuyệt thật đấy" và 2574 "Giọng điệu của ông ấy vẫn luôn tươi sáng và nhẹ nhàng" — hai dòng ban đầu suýt đánh dấu sai, thực ra khớp JP nên đã chuyển sang đúng). 60 dòng đúng còn lại không còn dòng nào mang tiếng Trung (VN==TW trong TOML chỉ xảy ra đúng ở 44 dòng đã nêu).
- **Không xét lỗi định dạng `\n`:** theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng, `\n` thủ công không quan trọng. Chỉ báo lỗi nội dung. Khối TOML bên dưới viết `\n` ở vị trí ngắt dòng theo đúng JP/TW gốc, giống các dòng đúng sẵn có trong file.

## Kết luận về cơ chế lỗi
- Giống 3 file trước: **lỗi chép nhầm rải rác, quy mô lớn nhất từ trước tới nay** — cột Việt bị xáo trộn giữa các dòng trong cùng file. JP và TW khớp nhau (~98%), nên chỉ cần dịch lại từ JP/TW là ra bản đúng.
- **120 cặp lệch vị trí đã xác nhận** (gấp gần 1,7 lần Grand 01): bản dịch đúng của một key đang nằm ở key khác (danh sách bên dưới). Trong lần rà soát thứ hai, tìm thêm được 49 cặp so với lần đọc đầu (71 cặp) — vì nhiều bản dịch bị chuyển tới key rất xa trong file (VD: VN ở 1403 là bản dịch của 2152; VN ở 3025 là bản dịch của 2076). Không có cặp nào tạo thành vòng tròn hai chiều — mỗi cặp chỉ đúng theo một hướng.
- 210 dòng lệch còn lại mang nội dung của cảnh khác trong chương — nhiều nhất là lời dẫn cảnh lái tàu/thực hành (van tiết lưu, phanh, ga cuối) rơi vào giữa cảnh họp bàn và cảnh tắm, và các câu đáp ngắn ("Đã rõ.", "Hả!?", "Ừm?") bị đặt nhầm chỗ — chưa truy vết được từng dòng về đúng key gốc của nó, xem "Giới hạn" bên dưới.
- Có một số giá trị Việt lặp lại trong file (xem "Trùng lặp"). Không có key trùng (File, Section, Key) trong CSV3 ở file này.
- 60 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)
Lưu ý khi chép: xuống dòng viết dạng `\n` — giống như các dòng đúng sẵn có trong file. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng. Khối này đã kiểm tra bằng máy: parse được bằng tomllib, **374/374 key** khớp đúng tập dòng sai, không thừa không thiếu, giá trị sau khi parse khớp đúng bản sửa (kể cả thẻ `%l` và `\n`).

```toml
1401 = "……Sở thú Omuta hình như đang khốn đốn lắm vì lượng khách vào xem ngày càng giảm."
1403 = "……Quả thật là vậy. Chưa nói đến Hachiroku, còn có tấm biển vàng của giới đầu máy hơi nước Đông Hinomoto, Railord Ran của D51 840."
1409 = "……D51 1031 sau khi nghỉ hưu trong đợt Đại bãi bỏ, đã được thị trấn Yufu cũ tiếp nhận, cùng với toa ngủ, làm khách sạn đầu máy hơi nước."
1413 = "「――Ừm.」"
1414 = "「――Có sống sót được không?」"
1416 = "「――Đúng như vậy nhỉ.」"
1436 = "「……Ừ. Em hơi, nghĩ ngợi một chút.」"
1437 = "「……Ừ.」"
1439 = "「……Tôi đã học được những điểm cần lưu ý đặc trưng của toa ăn.\n……Cũng được cho thấy một trong những hình mẫu lý tưởng của điểm du lịch.」"
1441 = "「……Dù có nghĩ ra, cũng khó mà thực hiện được. Mikuro đúng là người rất tích cực và hành động.」"
1442 = "「...Nên em đã nhường những phụ tùng khác,\ncho những đứa trẻ có nồi hơi khỏe mạnh sao?」"
1445 = "「……'Chưa phải là chuyện tháo dỡ ngay', thị trưởng Yufuin đã nói vậy nhỉ.」"
1450 = "「...Lấy phụ tùng. Ở những cỗ máy đang hoạt động——ưm, có sự thiếu hụt phụ tùng,\nnếu cứ để vậy, sẽ có những đứa trẻ không thể chạy được nữa.」"
1804 = "「Lúc đầu, Railord của D51 1031 đã chăm sóc nó mà——」"
1805 = "「Chốt lại vậy. Với toa tự hành cải tạo hạng 18 mét, không đủ không gian để làm toa ăn lý tưởng như chúng ta muốn hiện nay.」"
1808 = "「Không. Đứa bé này cũng chạy lại được mà.」"
1812 = "「Không chỉ tàu ăn, mà còn rất nhiều tàu du lịch nữa. Anh hai đúng là tuyệt thật, em đã nghĩ vậy đó.」"
1817 = "「Nhưng mà, ngay cả ở Yufuin như vậy——\nvẫn còn bóng dáng của quá khứ.」"
1818 = "「Nhưng mà, dù là trên đài phát thanh hay trong 『Bản tin buồng lái』,\nnhững hoạt động của chị ấy, em đều theo dõi rất sát sao ạ.」"
1819 = "「Không! Không có chuyện đó đâu?」"
1822 = "「Không ạ, Mikuro ở Omuta.\nTừ lúc nghỉ hưu đến giờ, em làm việc ở sở thú Omuta ạ.」"
1826 = "「Không phải ạ, Mikuro là,\nRailord của đầu máy hơi nước loại 8620, số hiệu 38696 thuộc Đường sắt Hoàng gia cũ ạ.」"
1831 = "「Không—— nói là ý của tôi thì đúng hơn, đó là mắt nhìn của Hibiki và kinh nghiệm của thị trưởng Yufuin hợp lại mà thành.」"
1832 = "「Không, làm được.\nĐể làm được điều đó, lần này hãy thử nghĩ ngược lại xem.」"
1839 = "「Hô hô—」"
1845 = "「Nhân cơ hội khôi phục tuyến đường này, Yufuin đang bắt đầu mơ ước\n——\"sự tĩnh lặng mới của Yufuin\". Về hình dáng tương lai đó.」"
1847 = "「Nhưng mà, không dùng được đầu máy—— à, vậy thì, dùng hai toa tự hành kẹp toa khách với toa nguồn vào giữa—— thì sao?」"
1849 = "「Ngược lại, đã gây họa mất rồi. Chính vì đã dồn quá nhiều tình yêu vào việc bảo dưỡng mà ra.」"
1854 = "「Mọi người đã lập ra một kế hoạch đô thị dài hạn bám sát theo chủ đề.\n...Đây không phải là điều có thể dễ dàng thực hiện được nhỉ.」"
1856 = "「Nghĩ gì vậy?」"
1857 = "「Cậu là……」"
1859 = "「Em là, Railord của đầu máy xe lửa này sao?」"
1863 = "「Cứ đi mà cúi gầm mặt xuống như thế,\nthì sẽ bỏ lỡ những thứ cần xem đấy.」"
1864 = "「Dù biết vậy——dù biết vậy mà vẫn」"
1875 = "「Trái tim—— theo ý trái tim em.」"
1876 = "「Hai người,\nbiết chị Hachiroku sao ạ?」"
1877 = "「Hachiroku.」"
1880 = "「Cái đó…… tôi hoàn toàn không có chút tự tin nào trong việc chọn quà. Nếu được thì ngày mai Hibiki đi chọn cùng tôi nhé.」"
1887 = "「Không phải chơi chữ, đúng là 'bức tranh' đấy. Hibiki lúc nào cũng biến cảm xúc của ai đó thành tranh.」"
1890 = "「Em nói là đang làm việc ở sở thú Omuta——đúng không.\nVậy thì, chiếc 38696 cũng được bảo tồn ở đó sao?」"
1891 = "「Lúc nãy, cậu——」"
1895 = "「Nói đến sở thú, thì đó là cơ sở có thu phí vào cửa đúng không?\nĐược bảo tồn ở trong đó, tại sao lại trở nên tơi tả như vậy?」"
1896 = "「Hình ảnh càng tốt... thì khi bị phá vỡ——\nƯm——sẽ không dễ dàng gì——」"
1897 = "「Ra là vậy.」"
1903 = "「Học…… học cái gì cơ?」"
1905 = "「'Hình dáng mới của toa ăn lý tưởng của chúng ta' đấy. Lý tưởng hiện tại của chúng ta, cũng chỉ là nghe kể về hình dáng xưa mà thôi.」"
1908 = "「Nhìn ngược lại, việc 'làm gì đó' với D51 1031. Bản thân nỗ lực đó——」"
1909 = "「Ngược lại, nếu làm sạch thì mọi người sẽ lại nhìn. Như vậy đứa bé này chắc chắn sống sót được.」"
1912 = "「Nếu học được những kiến thức đó, có lẽ sẽ có gì đó áp dụng được cho tàu ăn.」"
1917 = "「Nhưng nếu chỉ nhìn vào đó, mà đánh mất người dùng đầu tiên là 'bản thân', thì chắc chắn sẽ bỏ lỡ cái sâu nhất.」"
1931 = "「Oa! Chị vui lắm khi biết em có nghe đài đó!\nVậy là, bé Mikuro cũng sống ở quanh khu vực Kumamoto sao?」"
1932 = "「Waa! Được giúp như vậy thì mừng quá. Biết được lý do bị bỏ mặc thì sẽ dễ tìm cách hơn nhỉ!」"
1933 = "「Ư！！」"
1935 = "「Hả.」"
1937 = "「Chà... trên đời này thực sự có tồn tại nhỉ.\nThiên tài——đấy.」"
1944 = "「Hả!?」"
1945 = "「Hả!?」"
1946 = "「Hả!? Hachiroku á——\nVậy là, em gái của Hachiroku sao!!?」"
1948 = "「À.」"
1950 = "「Ồ, cháu vẽ xong rồi sao?」"
1951 = "「Hử?」"
1953 = "「Vậy là được—— mà, những gì làm được bây giờ, chắc…… cũng chỉ đến thế là hết sức, à!」"
1954 = "「Ư……ừm.」"
1955 = "「Ừm?」"
1956 = "「Uốp!」"
1957 = "「À——」"
1958 = "「À……」"
1962 = "「Aaaa!」"
1964 = "「À! Cái này, như kiểu biểu tượng của kế hoạch ấy.」"
1967 = "「A! Xin lỗi, đã làm hai người giật mình.」"
1968 = "「À! Đúng rồi nhỉ. Chị Hibiki là thị trưởng thành phố Ohitoyo mà. Với thị trưởng Yufuin thì chắc chắn——」"
1970 = "「A! Vâng, đúng vậy ạ. Đứa bé này cũng vậy, chắc chắn sẽ thêm một lần nữa.\nCó thể chạy trong tâm trí, trong những ký ức.」"
1972 = "「À, là xe ngựa sao ạ?」"
1974 = "「A, Mikuro nghe trên internet ạ.\nTừ trang web của Đường sắt Ohitoyo.」"
1976 = "「Hau!?」"
1978 = "「Ê!? Vậy thì không làm được nữa.」"
1979 = "「Ừm——」"
1980 = "「À—— không.」"
1982 = "「Ưm... vẽ, cái gì cơ ạ——\nÀ không!? Cháu nên vẽ cái gì đây ạ?」"
1984 = "「Ừ—— ừ! Chỗ đó dù hẹp, vẫn nấu những món thật ngon mang ra mà!」"
1985 = "「À——… đúng nhỉ. Ừm—— quay lại chuyện đó… thì——」"
1987 = "「Ừ. Nhưng em cũng chẳng có cảm giác định làm gì cả. Hoàn toàn không biết phải xử lý ra sao…」"
1989 = "「Ừm. Đúng rồi. Chị là Hibiki.\nNhưng mà, \"giọng\" là sao?」"
1991 = "「Ừ. Có thể đấy.」"
1993 = "「Ừm. Vậy Hibiki, làm theo cảm giác đó thì sao——」"
1994 = "「Ừm.」"
1995 = "「Ừ!」"
1996 = "「Ừ! Ý đó, em thấy rất hay. Vì bản thân Mikuro-chan cũng là đứa trẻ đẹp như tranh vậy.」"
1998 = "「Ừ!!」"
2000 = "「À, không phải từ thiết kế toa ăn, mà từ mặt chức năng—— tức là, từ cách dùng bếp hẹp mà học.」"
2006 = "「Vâng, đúng vậy ạ.」"
2007 = "「À, kiểu không vượt được dốc— ưư… nhưng vẫn muốn không gian～」"
2009 = "「Ừm, không ngờ trong một công viên giữa lòng thành phố thế này lại có——mà nói đúng hơn là...」"
2011 = "「Ừ, nghe em nói mới để ý——\nRa vậy, các nét trên khuôn mặt rất giống Hachiroku.」"
2013 = "「À, ừm.」"
2014 = "「Ừm?」"
2015 = "「Hử? Được mà—」"
2016 = "「Hử? À.」"
2018 = "「Ừm? Vừa nãy chúng ta mới đi qua trước Seikyo mà——」"
2023 = "「À!」"
2025 = "「Hô hô? Cảm giác thế nào?」"
2030 = "「Vì từ khi còn nhỏ, mãi cho đến giờ. Điều vui nhất đối với em là anh hai trở về.」"
2031 = "「Đã có một thời kỳ như vậy đấy.\nẢnh hưởng của việc bại trận là rất lớn.」"
2032 = "「Trong tâm trí, trong những ký ức.」"
2035 = "「Sau khi đứa bé đó ngừng hoạt động—— không ai chạm tay vào…… không thể chạm vào được, mà」"
2036 = "「Chạy trong tâm trí, sao.」"
2041 = "「Ưu tiên và xử lý công việc. Trong lúc bị cuốn theo những thứ đó, Hibiki và tôi, có phải lại sắp đánh mất nữa không nhỉ.」"
2049 = "「Nói Omuta là tỉnh Fukuoka nhỉ. Sóng của đài nhỏ mà bay xa thật đấy.」"
2054 = "「À.」"
2056 = "「Tuyệt quá! Không ngờ lại gặp được ở đây. Đài Maitetsu radio, Mikuro lúc nào cũng nghe hết đó ạ!」"
2058 = "「Nếu chỉ chạy tuyến Yunoi bằng phẳng thì được thôi. Nhưng Đường sắt Kurudai—— từ Hita trở đi, tôi cảm thấy không được.」"
2060 = "「Nếu làm được như vậy, nếu thành công. Chắc chắn, chính quyền thành phố Omuta và mọi người dân, sẽ chú ý đến 38696.」"
2067 = "「Đúng không? Chị thì tỏa sáng, còn em gái thì bị đối xử như đồ thừa.」"
2068 = "「Đúng không! Là đầu máy xe lửa đúng không!?」"
2069 = "「À! Đúng rồi, chính là nó! Đúng là bếp của quán Gamadasu Cafe!」"
2070 = "「Đúng thật nhỉ. Cảm ơn chị Kisaki nhiều lắm. Quà thì phải mua thật xịn mới được.」"
2074 = "「Góc nhìn của người dân, góc nhìn người dùng. Dĩ nhiên là quan trọng.」"
2076 = "「Phát triển khu nghỉ dưỡng. Những câu chuyện như thu hút sân golf lúc nào cũng\nchia rẽ thị trấn, chưa kể còn xảy ra một trận động đất lớn nữa.」"
2079 = "「Ra là giúp việc à. Nếu có thời gian rảnh thì có lẽ được đấy. Thực tế, tôi với Hibiki đến cửa hàng——」"
2085 = "「Quản lý Yamazaki là do chị Kisaki giới thiệu. Tham quan cũng thoải mái, thực tế có thể giúp việc được.」"
2088 = "「Nối các nơi lại, hoặc cho chạy các đoàn tàu du lịch đi vòng quanh các nơi. Lấy toàn bộ Kyushu làm một mặt, làm cho du lịch đường sắt tỏa sáng.」"
2093 = "「Tiếc là, đừng nói chạy cùng, em còn chưa từng gặp chị ấy nữa cơ.」"
2095 = "「Vui quá. Cái gọi là 'lời khen từ tận đáy lòng' đấy.」"
2101 = "「Thành phố Ohitoyo——Đường sắt Ohitoyo!\nPhụ lái tàu của chị Hachiroku, chiếc xe số 1!」"
2106 = "「Không thể chuyện thành phố Yufuin can thiệp chính sự thành phố Ohitoyo. Nhưng đề xuất chia sẻ thông tin thì không khó.」"
2110 = "「Không thể nào, đến ga vẫn còn hơn mười phút nữa cơ mà——hửm!?」"
2118 = "「Là trận động đất lớn Oita vào năm \\x%l正和;#00ffc040;Showa%l;#; thứ 30 đúng không ạ?」"
2125 = "「Thu hoạch bất ngờ—— hay, liệu cái đó có thành thu hoạch không nhỉ.」"
2128 = "「Có đắm chìm cũng được mà? Trong khả năng, tôi cũng sẽ ủng hộ, giúp đỡ.」"
2132 = "「Tôi cũng vậy? Chắc chắn, lúc đó—— vết thương, còn lại trong tim.」"
2134 = "「Nào, sao nhỉ. Chỉ là vừa chợt nghĩ ra, chi tiết thì phải nhờ chuyên gia xem xét——」"
2137 = "「Điều cần xem trước nhất là trái tim của chính chúng ta. Nếu chỗ đó mờ đục thì mọi thứ nhìn thấy cũng mờ.」"
2138 = "「Dù sao, hãy lấy thông tin chính xác đã.」"
2139 = "「Cảm thấy nhẹ nhõm hẳn luôn! Đến đây thật là tốt! Cả Bungo Mori lẫn Yufuin!!」"
2143 = "「Với hai cháu thì có thể nói chuyện được. Không—— chính hai cháu mới là người nên vẽ.」"
2145 = "「Tôi là chủ sở hữu, Master của Hachiroku,\nvà là người lái tàu.」"
2146 = "「Dĩ nhiên, không có ý đắm chìm đâu? Thiết kế và chính sự ưu tiên mà. Nhưng mà, dù vậy, một chút.」"
2148 = "「Chỗ đó cũng, thử bàn bạc một lần cũng được đấy. Nhưng——」"
2149 = "「Quả nhiên, 2 toa DMU 18 mét thì chật. Muốn toa ăn thép 20 mét với toa nguồn.」"
2152 = "「Tức là, sự tĩnh lặng của Yufuin luôn được cập nhật và duy trì.\nCháu cảm nhận được đó là một sự tĩnh lặng luôn được tái sinh mỗi ngày.」"
2153 = "「Này, anh hai. Quanh đây có siêu thị hay gì đó không?」"
2158 = "「Ngay sau khi bại trận, Yufuin đã bị\nbiến thành căn cứ và cơ sở nghỉ dưỡng của Minh Quân.」"
2160 = "「Nên… cứ bị coi là đồ thừa rồi bị tháo dỡ. ——Dù biết là cảm thương, nhưng đau lòng, nghĩ vậy.」"
2161 = "「Nên, theo ý trái tim muốn, trong phạm vi không quá sức, cứ theo đuổi, thử hành động cũng được.」"
2164 = "「Nên trước hết, nhờ cung cấp thông tin về D51 1031 này. Nếu được phía Yufuin đồng ý thì sẽ báo cho Mikuro.」"
2166 = "「Vì vậy Yufuin hoan nghênh kích thích mới. Để đưa 'sự tĩnh lặng thủ công' lên tầm cao hơn.」"
2168 = "「Thế là trở thành Yufuin (湯布院) sao ạ!」"
2169 = "「Vì vậy Mikuro đã suy nghĩ rất nhiều. Ví dụ như, nếu biến D51 thành điểm du lịch, liệu có nổi bật không nhỉ.」"
2171 = "「Vì vậy, Mikuro, muốn chúng chạy tiếp.\nVì 38696 đã nghỉ hưu do hỏng nồi hơi rồi, nên hãy chạy thay cho cả phần của Mikuro nữa.」"
2174 = "「Thủ công... vâng.」"
2177 = "「Cũng được nghe về \\x%l扇形機関庫;#00ffc040;nhà chứa đầu máy hình quạt%l;#; của Bungo Mori…\nvà đã chia sẻ được tầm nhìn dài hạn!」"
2180 = "「Nhờ anh hai gắn kết lại thành hình. Quả nhiên anh hai giỏi thật!」"
2181 = "「——Lấy phụ tùng.」"
2183 = "「Rồi, tranh chấp tên gọi là sao?」"
2184 = "「Tấm gương?」"
2192 = "「Vì sau này mới gấp rút thêm bếp vào, nên phần đó giao trọn cho nhà thầu chuyên nghiệp.」"
2197 = "「Hibiki.」"
2198 = "「Hibiki, cho xem được không?」"
2202 = "「Đúng nhỉ. Nên— cũng vì ý nghĩa đó, đứa bé đó, D51 1031. Tôi muốn làm gì đó cho nó.」"
2204 = "「Đúng nhỉ. Hibiki— cho mượn lưng một chút được không?」"
2205 = "「Đúng. Bỏ mặc chỗ đó mà làm branding đường sắt thì… cứ cảm giác để lại vết mờ hay vết thương.」"
2207 = "「Đúng vậy.」"
2209 = "「Đúng vậy ạ! Nếu tơi tả đến mức này,\nthì mọi người sẽ không muốn nhìn nó nữa đâu ạ.」"
2210 = "「Hô.」"
2214 = "「Đúng vậy. Phía bên kia đưa ra ý kiến là nên lấy tên thị trấn Yunohira.\nCuối cùng, mọi chuyện đã ổn thỏa bằng một cái tên mới để làm mới hình ảnh.」"
2216 = "「Đúng. Cũng thành dịp đổi tâm trạng— và từ đó có thể có gì đó kết nối.」"
2217 = "「Vâng.」"
2219 = "「Vâng! Việc chăm sóc động vật hay dọn dẹp công viên,\ndù cánh tay máy có hơi trục trặc một chút thì vẫn có thể hoàn thành được ạ.」"
2220 = "「Có thể, vận chuyển được chăng. Nếu làm được thì dòng chảy chắc chắn sẽ lan đến Omuta— đến 38696 của Mikuro.」"
2226 = "「Kết quả, làm ra bếp rất hẹp khó dùng. Nhưng thành ra thế này… có lẽ cũng là an bài của trời.」"
2228 = "「Cỗ xe ngựa này... bởi vì... đẹp đến nhường này...\nXe ngựa cũng vậy... tất cả mọi thứ của thị trấn——đều là biểu tượng của... Yufuin——」"
2230 = "「Có gì khiến cháu cảm nhận được không?」"
2231 = "「Không phải là sự tĩnh lặng tương đối, giống như một khu nhà phụ của Beppu.\nMà hướng tới một 'sự tĩnh lặng thủ công' tận dụng thiên nhiên và môi trường.」"
2233 = "「Ra là vậy.」"
2234 = "「Hình dáng tương lai…… hình dáng tương lai.」"
2240 = "「Quả nhiên là vậy! Giống hệt nhau luôn mà! Nhỉ! Anh hai!」"
2242 = "「Đúng vậy đấy. Dù là thời thị trấn Yufuin hay khi đã trở thành thành phố Yufuin,\ntài chính lúc nào cũng trong tình trạng báo động. Đời sống của người dân cũng chẳng khá khẩm hơn.」"
2244 = "「Chính xác. Ngay cả sau khi cơ sở bị dỡ bỏ, lượng khách vẫn không phục hồi,\nrơi vào tình trạng khó khăn kinh tế đến mức xuất hiện cả kế hoạch xây dựng đập thủy điện.」"
2247 = "「Đúng vậy. Thậm chí còn có tin đồn là Yufuin đã bị hủy diệt.\nThứ được cho chạy để bác bỏ tin đồn đó——chính là cái này đây.」"
2252 = "「Mỗi khi tiếp xúc với những tin tức như vậy, Mikuro cũng cảm thấy như,\nmình đang được cùng chị ấy chạy trong tâm trí, vui lắm ạ.」"
2257 = "「À không, cháu cảm thấy mọi thứ dường như đã kết nối với nhau. Cảnh tượng này, và\n\"sự sôi động\" mà Thị trưởng vừa nhắc đến lúc nãy.」"
2259 = "「Đúng. Đã cho xe ngựa Tsuji chạy. Và nó đến giờ, vẫn nối tiếp lịch sử với tư cách xe ngựa du lịch.」"
2264 = "「Đổ mồ hôi sướng thật~」"
2272 = "「Sự tĩnh lặng của Yufuin không phải là sự tĩnh lặng do bị bỏ mặc.\nNói cách khác——đó là sự tĩnh lặng hài hòa với sự sôi động, đúng không ạ?」"
2273 = "「——Để trở thành điểm du lịch được so sánh với danh thắng thế giới, branding toàn bộ 'Kyushu'.」"
2274 = "「Để vẽ ra bản đồ tương lai đó, trước hết là thiết kế tàu ăn resort.」"
2275 = "「Để khiến họ rút lại kế hoạch đó——mới phải sáp nhập sao ạ?」"
2276 = "「Làm sao đây.」"
2280 = "「Cả Mikuro-chan lẫn 38696 của Mikuro-chan— cả D51 1031 ở công viên, đều là em gái mà.」"
2284 = "「Còn lại đấy. Vết thương.」"
2285 = "「Bởi vì là cơ sở nghỉ dưỡng của nước thắng trận đặt tại nước bại trận mà.\nHọ chẳng thèm bận tâm đến an ninh trật tự đâu. Du lịch coi như nát bét.」"
2286 = "「Thu hoạch đấy, thu hoạch! Còn nối đến nhiều thông tin như SL hotel.」"
2290 = "「Cái này—— không bao giờ chạy lại được nữa.」"
2291 = "「Chỗ kia——anh hai, là đầu máy xe lửa kìa!」"
2301 = "「Đúng thật. Tầm nhìn của thị trưởng Yufuin làm tôi ngạc nhiên. 'Đối thủ là London và Paris' à.」"
2303 = "「Chắc là vậy.」"
2304 = "「Ra là, ngày đầu chỉ là 'du lịch' thôi, nên những thứ như vậy cũng cần thiết.」"
2307 = "「Quà—— à.」"
2308 = "「Quà quan trọng lắm— dù đi công tác cũng vậy! Không mua thì cứ thấy buồn buồn.」"
2311 = "「Tiền… quả nhiên thị trưởng nói, tài chính luôn khó khăn.」"
2314 = "「Chị Hachiroku—— mọi người của Đường sắt Ohitoyo ạ. Nhìn thấy chị, em đã nghĩ có lẽ em cũng làm được.」"
2317 = "「Cứ thế này thì sẽ ngày càng khốn quẫn, Mikuro đã nhận ra.」"
2318 = "「Mikuro không giỏi đến thế đâu. Chỉ là vì ngưỡng mộ— muốn lấy làm tấm gương thôi ạ.」"
2321 = "「Chiếc 38696 của Mikuro cũng... là một cỗ máy bảo tồn khá tơi tả ạ.\nPhụ tùng các thứ, bị thiếu hụt nhiều lắm rồi.」"
2322 = "「Có tin đồn về việc tháo dỡ ạ. Đứa bé này.\nHơn nữa, còn ở mức độ là ngân sách tháo dỡ sắp được đệ trình rồi.」"
2324 = "「Nói thẳng, tôi có cảm giác như họ xem nó là đồ phiền phức.」"
2326 = "「Còn em là phụ lái tàu.\nHôm nay bọn em đến từ thành phố Ohitoyo để thị sát đó.」"
2327 = "「Nghe nói là không có tiền. Dù sửa chữa, tháo dỡ hay di dời.」"
2330 = "「Chuyến thị sát học được nhiều thế này, cũng hiếm đấy.」"
2331 = "「Nếu vậy thì thật vinh hạnh. Nếu có gì chúng tôi giúp được thì cứ nói.」"
2333 = "「Xin mời, nếu ngài không phiền.」"
2336 = "「Có thứ tự cả ạ. Mikuro, đã suy nghĩ rồi.\nDù có cố gắng thế nào ở sở thú, thì cũng không ai đến xem 38696 đâu ạ.」"
2346 = "「Chính xác là vậy. Bởi vì mọi thứ của thị trấn, đến từng ngóc ngách đều là \"Yufuin\",\nnên thị trấn này mới có thể toát lên sự tĩnh lặng đến nhường này.」"
2347 = "「Cứ gọi em là Mikuro đi ạ. Nếu anh là Master của chị Hachiroku,\nthì đối với Mikuro, anh cũng là một người quan trọng và đáng kính trọng ạ.」"
2348 = "「Xin hỏi... Hachiroku mà hai người nhắc đến,\ncó phải là chị Hachiroku, chiếc xe số 1 của loại 8620 không ạ?」"
2351 = "「Cảm ơn anh hai! Em đang bế tắc mà tự nhiên thông suốt hẳn!」"
2375 = "「Đánh mất thì…… đánh mất cái gì?」"
2383 = "「Nhìn ngược lại?」"
2385 = "「Không phải vết thương, là huân chương. Từ tận đáy lòng tôi nghĩ vậy. Giờ cũng vậy, xưa cũng vậy.」"
2386 = "「Cái này……」"
2387 = "「Cái đó làm được sao!?」"
2388 = "「Đứa bé này... tơi tả quá.\nCửa buồng khói bị thủng lỗ chỗ luôn rồi.」"
2389 = "「Vì lý do gì mà đứa bé này bị bỏ lại ở đây? Sao không ai chăm sóc nó?」"
2391 = "「Vinh hạnh.」"
2392 = "「Ra vậy~, thế thì, em cũng biết giọng của Hachiroku nhỉ.\nA! Hay là, hồi còn đương chức hai người từng chạy cùng nhau?」"
2393 = "「Dĩ nhiên sẽ cho xem—— hử?」"
2394 = "「Cái này——thật tuyệt vời. Trong khoảng thời gian ngắn như vậy——\nmà cháu có thể vẽ được một \"Yufuin\" rộng lớn và đa dạng đến thế này.」"
2395 = "「Là để thoát khỏi tình trạng khó khăn kinh tế bao gồm tất cả những điều đó.\nBởi vì những khách du lịch rời bỏ nơi này đã đổ dồn về Yunohira.」"
2396 = "「Vậy ra, tôi trong quá khứ đã luôn khiến Hibiki cảm thấy cô đơn sao.」"
2397 = "「Đã từng bóng loáng lắm đó ạ! Cả 38696 và Mikuro. Luôn luôn.\nNhưng mà——ưm——」"
2402 = "「Vậy thì, cứ gọi như vậy đi. Lúc nãy Mikuro nói 'đứa bé này cũng chạy lại được' mà.」"
2407 = "「Vậy thì, chổi với túi rác! Tôi đi mua ngay đây!」"
2409 = "「Nếu vậy chẳng lẽ, chị là——Phụ lái tàu Migita Hibiki\n——đúng không ạ. Vì đây không phải là giọng của Phụ lái tàu Minokasa Nagi.」"
2410 = "「Nếu vậy, chẳng phải nên ưu tiên cho chiếc 38696 \"khá tơi tả\" kia,\nđể nó có thể \"chạy trong ký ức\" sao?」"
2411 = "「Và, về chuyện quà phải mang về——」"
2412 = "「Anh hai. Cho xem tay?」"
2414 = "「Anh hai.」"
2415 = "「Anh hai!」"
2418 = "「Bao nhiêu cũng được mà—, tất cả của tôi, đều là của anh hai.」"
2419 = "「Cùng với đó, phương hướng xây dựng thị trấn cũng được thống nhất.」"
2423 = "「Học được rất nhiều, nhưng cũng thấy rõ những điều còn thiếu.」"
2428 = "「Nếu là một chuyến tàu chạy trong ký ức, thì chắc chắn nó sẽ rất tỏa sáng.\nChính vì thế, ngược lại——」"
2432 = "「Quán Gamadasu Cafe!」"
2433 = "「～～Ư」"
2564 = "Giọng nói cứng đắn bất ngờ của Hibiki, người nãy giờ vẫn im lặng lắng nghe.\nTuy nhiên, Mikuro vẫn mỉm cười đáp lại như không có chuyện gì xảy ra."
2565 = "「Không ổn. Hibiki dễ thương quá. Nhưng dù bao trọn, đây là bồn tắm của quán trọ. Là nơi công cộng.」"
2575 = "「Nhưng ở chỗ thực sự nguy hiểm, tình cờ gặp được ánh mắt Mikuro. Có lẽ đã được cứu bởi đôi mắt mất màu nhưng dịu dàng ấy.」"
2576 = "Không hẳn là u ám,\nmà chỉ đơn thuần là có vẻ bối rối."
2577 = "「Nhưng dù vậy vẫn có thể tưởng tượng. Vì trên đường đến đây đã thị sát kỹ.」"
2578 = "「Nhưng bản thân không thể ngờ tới, có lẽ điều này, đã lệch đi rồi.」"
2579 = "「Nhưng Hibiki mỉm cười dịu dàng. Nụ cười như trào ra từ sâu trong tim.」"
2580 = "Nhưng chính vì thế...\ntôi càng cảm thấy tình trạng hiện tại thật khắc nghiệt."
2591 = "「Để đường sắt hoạt động, cảm thấy việc hợp tác giữa người và Railord là bắt buộc.」"
2595 = "Đột nhiên bị chỉ vào sàn xe...\nTôi mất vài giây mới hiểu được ý của ông ấy."
2600 = "「Cảm giác tội lỗi khi nhìn thấy điều đó, khách đến sở thú chắc chắn không thích.」"
2611 = "Những thắc mắc từ cái nhìn đầu tiên,\ntôi quyết định nói ra vào lúc này."
2616 = "Ra vậy, Mikuro không muốn đề cập đến chuyện đó——\nNên em ấy mới cố gắng lựa chọn những \"từ ngữ dễ gây hiểu lầm\" sao."
2624 = "Một cỗ xe ngựa chạy từ quá khứ đến hiện tại,\ngiữa một thị trấn nơi nét cổ kính và sự mới mẻ hòa quyện vào nhau."
2628 = "Bởi vì nếu tạo ra cơ chế để mọi người tận hưởng hết mình chuyến du ngoạn Kyushu, thì nhiều điểm du lịch có thể cùng lúc trở thành người chiến thắng."
2629 = "「Nếu khiến họ chọn 'Kyushu', thế giới thu hẹp lại sẽ có lợi.」"
2633 = "「Kêu gọi tình nguyện viên dọn sạch, hồi sinh thành trạng thái đẹp, làm điểm tập trung khách du lịch.」"
2634 = "「Nhưng sức của Hibiki và tôi hiện đã gần đến giới hạn. Không muốn kỳ vọng quá lớn thành gánh nặng cho Hibiki.」"
2646 = "Dù đó là việc bảo quản toa xe đường sắt không còn chạy được nữa—— dù là \\x%l静態保存;#00ffc040;bảo quản tĩnh%l;#; cũng vậy."
2651 = "Ngay cả sự quý phái toát ra từ dáng vẻ nghiêng đầu,\nchắc chắn cũng là được thừa hưởng từ Hachiroku."
2653 = "「À— nụ cười ấm áp biết bao.」"
2654 = "Chapun, tiếng nước. Hibiki múc nước bằng tay, nhẹ nhàng rửa mặt mình."
2657 = "Dù cầm chổi bằng cả hai tay, nhưng bàn tay trái vẫn mở ra và chỉ đặt hờ lên\n——bởi vì em ấy không hề nắm lấy cán chổi."
2658 = "Nghỉ hưu do hỏng nồi hơi... một câu nói thật xót xa.\nBởi vì sự xuống cấp, lão hóa của nồi hơi chính là vết thương chí mạng của đầu máy hơi nước."
2662 = "「Nhờ lặp lại việc quét dọn buổi sáng ở nhà máy rượu Migita, Hibiki và tôi đã học được điều đó là sự thật.」"
2663 = "「Cho đến khi về phòng phải tự kiềm chế—— ngay khi nghĩ vậy, phương sách cũng hiện ra.」"
2666 = "「Thời kỳ khổ sở trong chiến dịch bầu cử. Hibiki và tôi đã hoàn toàn đánh mất chỗ đó.」"
2668 = "Theo ý tưởng ban đầu của Gamadasu— bản thiết kế đầu tiên của Hibiki, toàn bộ Gamadasu được làm thành sân chơi cho trẻ em."
2671 = "「Đi thật nhiều, gặp thật nhiều, lắng nghe, nhìn, vẽ.」"
2676 = "「Đáng yêu biết bao, yêu thương biết bao. Hibiki hiện tại và Hibiki thuở nhỏ chồng lên nhau.」"
2678 = "\"Đài phát thanh Maitetsu Đường sắt Ohitoyo\" do Paulette bắt đầu phát sóng\nnhằm mục đích quảng bá và thông báo cho Đường sắt Ohitoyo."
2681 = "「Phải chăng bản thân nhỏ bé yếu đuối ngày đó đã chồng lên hình ảnh máy bảo quản tơi tả bị bỏ mặc.」"
2682 = "Dù nhìn từ góc độ nào cũng là một Railord. Nhưng có gì đó không đúng.\nNhìn kỹ thì thấy bộ dạng có chút kỳ lạ."
2684 = "「Vết thương chạy ở gốc ngón cái. Ngón tay Hibiki cứ vuốt ve mãi.」"
2686 = "Đèn pha ở cổ bị thiếu mất,\nmàu mắt hai bên cũng khác nhau rõ rệt——A!"
2687 = "Về mặt hình ảnh, không phải là tôi không hiểu em ấy muốn nói gì."
2690 = "Nếu chỉ nghĩ đến việc \"duy trì thương hiệu\" một cách đơn thuần,\nthì ngược lại có thể sẽ bị đánh giá tiêu cực."
2694 = "「Bổ sung kiến thức đến mức này cho cảm quan và sức tưởng tượng của Hibiki. Nếu vậy mà vẫn không giải quyết được——」"
2696 = "Nằm lặng lẽ như một điểm mù giữa khu du lịch sầm uất.\nKhông biết đó có phải là một tai họa hay không——"
2698 = "「Ngượng ngùng, vui mừng, sốt ruột. Muốn ôm chặt Hibiki ngay lập tức.」"
2701 = "「——Mà, đúng rồi, từ lúc đó, có vẻ như đã rất để tâm…」"
2702 = "「Tôi nhỏ bé ngày đó, không bảo vệ được ai, cả sự yếu đuối đó—— như muốn bao bọc tất cả.」"
2705 = "「Dù có dọn sạch xung quanh cỗ máy tơi tả đến mấy, cũng chỉ càng làm nổi bật sự tơi tả của cỗ máy mà thôi——」"
2707 = "Tung bọt nước lớn, Hibiki tiến về phía tôi."
2708 = "「Có lẽ thị trưởng nghĩ rằng em ấy đã miệt mài phác thảo một bức tranh.」"
2712 = "Cảm nhận được Hachiroku được yêu mến đến nhường nào,\nngay cả tôi cũng cảm thấy tự hào và hạnh phúc lây."
2721 = "Ngước mắt lên theo giọng nói của Hibiki,\ntôi có thể hiểu ngay ý nghĩa của \"sự tĩnh lặng thủ công\" chỉ trong một cái nhìn."
2724 = "Giật mình vì giọng nói, chúng tôi quay lại.\nVà lại thêm một chút ngạc nhiên trước sự hiện diện đang đứng đó."
2727 = "Việc khôi phục tuyến đường, sự hồi sinh của Bungomori, sự gia tăng dân di cư kéo theo đó,\nthậm chí cả kế hoạch toa ăn nghỉ dưỡng..."
2731 = "Cách duy nhất để đối phó với tình trạng có thể dẫn đến nổ nồi hơi đó,\nlà chế tạo một chiếc nồi hơi mới, và điều đó thì không tương xứng với chi phí bỏ ra."
2736 = "Từ câu \"vẽ xong rồi\",\ntôi nhận ra Thị trưởng Yufuin đang hiểu lầm."
2737 = "Tôi đưa tay phải ra. Hibiki nhận lấy và mở ra."
2740 = "「Kìm nén cảm giác muốn ôm chặt, ngón tay chạy trên lưng.」"
2742 = "「Với tư cách lái tàu, tôi cũng đã tích lũy kinh nghiệm. Vì vậy có thể khẳng định.」"
2744 = "Tôi nhận lấy cuốn sổ phác thảo mà Hibiki đưa ra,\nrồi lấy cuốn mới từ trong cặp ra đổi cho em ấy."
2746 = "「Vừa nói, vừa vuốt nhẹ mái tóc xõa, Hibiki dần dần thả lỏng.」"
2749 = "Bại trận——Nếu là sự thất bại của \\x%l大戦;#00ffc040;Đại chiến%l;#; trước đây,\nthì đó là năm \\x%l大詔;#00ffc040;Taisho%l;#; thứ 35. Tức là năm đầu tiên của thời kỳ \\x%l正和;#00ffc040;Showa%l;#;."
2752 = "「Vì vậy, cứ theo chuyện mà nói cùng, Hibiki cười khúc khích tinh nghịch.」"
2754 = "「Những gì hấp thu được, đã trao đổi với kỹ sư già, cựu đầu bếp toa ăn, thị trưởng Yufuin, và cả Railord.」"
2760 = "「Rồi từ từ, lại ngước nhìn D51 1031 trong công viên——」"
2761 = "Và rồi, \"A\",\ncái miệng nhỏ nhắn há ra vì ngạc nhiên."
2769 = "『Nếu vậy, em muốn tìm hiểu về Yufuin dù chỉ một chút』,\nmặc dù chúng tôi đã cố tình chọn cách đi bộ để trở về——"
2805 = "「Hibiki ngày xưa. Luôn bị so sánh với chị Mayami, bị coi là đứa không làm được——」"
2806 = "Hibiki đã hoàn toàn chìm đắm vào câu chuyện."
2807 = "「Hibiki đột nhiên cứng người lại. Cùng biểu cảm như khi nghe chuyện Mikuro.」"
2810 = "「Hibiki gật đầu một cách cẩn trọng.」"
2813 = "「Từ khoảng cách 0, Hibiki ngước nhìn tôi lên. Ánh mắt, hơi thở hòa làm một.」"
2814 = "「Hibiki ôm chầm lấy tôi.」"
2816 = "Vì Hibiki cũng thỉnh thoảng đảm nhận vai trò người dẫn chương trình,\nnên Mikuro mới biết đến em ấy sao."
2819 = "「Lồng ngực áp sát, tốc độ nhịp tim cho biết. Hibiki không chút tà niệm—— vui vẻ một cách chân thành, ôm lấy.」"
2821 = "「Nhịp tim Hibiki đột nhiên nhanh lên. Đang nhớ lại—— cả tôi và Hibiki.」"
2824 = "「Ngón tay Hibiki rời khỏi tay tôi. Vết thương còn lại trên cơ thể tôi. Vô số vết thương. Vuốt ve dấu vết tai nạn.」"
2826 = "Chỉ trong chốc lát, nét bút của Hibiki dừng lại."
2828 = "「Giọng Hibiki vẫn cứng. Vội nhìn thì biểu cảm cũng cứng lại.」"
2829 = "Những gì em ấy thực sự nghĩ trong lòng——\nNhững gì lọt vào mắt Hibiki, cứ thế được nói ra thành lời——!"
2833 = "「Khuôn mặt cứng đờ của Hibiki đột nhiên dịu lại.」"
2835 = "「Mỉm cười, Hibiki từ từ thả mình vào nước bồn tắm.」"
2837 = "「Nhiệt từ đầu ngón tay chạm vào Hibiki cho biết, những lời đó trào ra từ tận đáy lòng.」"
2840 = "「Để sắp xếp, viết là tốt nhất. Dòng chảy hôm qua, lấy lưng Hibiki làm sổ ghi chép.」"
2856 = "「Không có thu nhập thì cũng không có tiền để bảo dưỡng máy bảo quản. Dù Mikuro vẫn đang cố gắng dọn dẹp xung quanh……」"
2857 = "Đúng vậy.\nHibiki hiện tại không còn tâm trí đâu mà nói những lời nịnh nọt nữa."
2858 = "「À, với Hibiki thì, đó là điều đương nhiên—— đương nhiên mà, giờ lại thấy hơi ngượng.」"
2884 = "Công viên Thiếu nhi Trung tâm Yufuin.\nMột công viên nằm lệch ra khỏi con đường được gọi là trục đường chính."
2886 = "「Mỗi lần lật từng trang, ánh mắt thị trưởng Yufuin càng chăm chú.」"
2887 = "「Thị trưởng Yufuin nhìn tôi, rồi nhìn Hibiki chăm chú.」"
2888 = "「Nếu thị trưởng Yufuin, người đã suy nghĩ và tạo ra đến vậy, cố tình bỏ mặc đầu máy này, hẳn phải có lý do chắc chắn.」"
2889 = "Thị trưởng Yufuin vẫn giữ nụ cười không đổi.\nNhưng đến giờ tôi mới nhận ra, ánh sáng trong đôi mắt ấy vô cùng mạnh mẽ."
2891 = "「Sao Mikuro có thể mỉm cười. Cảm giác ngạc nhiên, dần dần, dẫn đến nhận ra, thấu hiểu.」"
2898 = "Khi tôi nhận ra điều đó và chuyển hướng câu chuyện,\nvẻ mặt Mikuro nhanh chóng từ bối rối trở lại nụ cười."
2900 = "Thấy tôi nín thở, vẻ mặt Mikuro càng thêm bối rối.\nVì vậy, tôi đã nhận ra."
2904 = "「Trước giọng điệu nghiêm túc và ánh mắt của thị trưởng Yufuin, Hibiki giật mình thẳng lưng.」"
2906 = "Và rồi, ánh mắt ấy ngước lên.\nGiọng nói khẽ run rẩy."
2911 = "「Ra là vậy, làm thế cũng không tệ. 'Nếu dọn dẹp, sẽ thấy bóng dáng người qua lại'.」"
2912 = "「Ra là vậy, đây là——」"
2914 = "「Sự phát triển của công nghệ Aircra đã khiến thế giới chắc chắn thu hẹp lại.」"
2923 = "「Dù nói là tiếc, Mikuro lại mỉm cười trông vô cùng hạnh phúc.」"
2925 = "「Kế hoạch mà Mikuro đưa ra, chính là phiên bản khác của những gì chúng ta đã làm cho đến nay, lấy Hachiroku làm biểu tượng cho việc khôi phục và kéo dài tuyến đường.」"
2928 = "Bỏ mặc tôi, chủ sở hữu, Master kiêm người lái tàu,\nánh mắt của Mikuro hoàn toàn chỉ hướng về phía Hibiki."
2930 = "「Trong tay Mikuro, một cây chổi nhỏ. Vậy thì, Mikuro—— chỉ một mình——」"
2932 = "「Mikuro trông thật lạc quan— hay nói đúng hơn, có vẻ như tính cách mơ mộng.」"
2934 = "「Lần đầu tiên, nụ cười của Mikuro biến mất.」"
2936 = "「Bản thân Mikuro cũng có thể có tổn thương hơn những gì nhìn thấy.」"
2937 = "「Mikuro kể cho nghe. 'D51 du lịch' — trước hết, thu hút sự chú ý vào D51 1031 của Yufuin này.」"
2938 = "Cỗ máy đang hoạt động——là cả Railord và \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; sao.\nMikuro đã, lấy phụ tùng của chính mình, cánh tay máy..."
2944 = "「Sự ngu ngốc đó, chúng ta suýt nữa lại lặp lại——」"
2946 = "Đối với ý tưởng đó, đã nhận được yêu cầu từ các nhân viên thành phố là những người mẹ. 'Nhất định hãy tạo ra một không gian để các bà mẹ nghỉ ngơi'."
2948 = "「Nghe vậy mới thấy, quả thật là thắc mắc. 'Sự tĩnh lặng thủ công'— sự trầm lắng và náo nhiệt của Yufuin này.」"
2949 = "Bị nhắc nhở, Hibiki giật mình ngẩng mặt lên,\nvươn thẳng lưng, nhìn quanh với điệu bộ hơi kịch cỡm——"
2950 = "Nghe em ấy nói vậy,\ntôi mới lờ mờ hiểu ra vấn đề."
2951 = "「Giọng nói đầy khó xử. Nhưng âm hưởng gần như tuyệt vọng trước chuyến đi đã biến mất.」"
2953 = "Railord tự xưng là Mikuro,\ntừ từ nghiêng cái đầu nhỏ nhắn của mình."
2954 = "Nơi đó đã đổi lấy hàng lỗi của đầu máy đang hoạt động bị hỏng— với sự quyết tâm— thực chất là đã hiến tặng sao."
2956 = "「SL Hotel phá sản, Yufu và Yunohira sáp nhập, toa xe bị tháo dỡ— chỉ đầu máy bị bỏ mặc nguyên.」"
2958 = "「Vượt qua khung Kyushu, trong nước, đến các điểm du lịch nổi tiếng nước ngoài. Phải phát triển thành tồn tại sánh ngang đó mới sống sót được.」"
2974 = "「Nếu trân trọng ký ức, ngược lại, người ta sẽ quay mắt đi trước hiện trạng như vậy.」"
2983 = "「Không thể không nhớ lại bản thân quá khứ, người vốn không có ý nghĩ mua quà lưu niệm.」"
2984 = "Không phải là sự tĩnh lặng vì không có chuyện gì xảy ra,\nmà là sự tĩnh lặng vì mọi chuyển động đều hài hòa và cân bằng bên trong nó."
2985 = "「Một câu nói khiến người ta cảm nhận được sự thật.」"
2986 = "Đó cũng là việc mà chúng tôi đã bắt đầu làm thường xuyên.\nNhưng khi nghe từ miệng \"người bị lấy mất phụ tùng\"——"
2987 = "Khu phố không chỉ có những công trình cổ kính. Những tòa nhà mới——thậm chí cả\ntiệm làm móng cũng có, nhưng tất cả đều hòa hợp một cách hoàn hảo."
2989 = "「Một câu nói hoàn toàn ngoài dự đoán.」"
2993 = "「Cỗ máy D51 công nghệ cao thường gọi, dù không phải số 1, nhưng nhìn từ 1031 thì chắc chắn là chị.」"
2995 = "「Lấy ví dụ thành công làm biểu tượng, lan truyền nó ra xung quanh. Cách suy nghĩ này, tôi rất hiểu, và cũng rất hợp ý tôi.」"
2996 = "Một sự tồn tại từng được yêu mến, nay đã sụp đổ một cách thảm hại."
3000 = "Đó là những bức phác họa nhanh bắt trọn những cảnh vật lướt qua\ntrong lúc lắc lư trên xe ngựa. Cuốn sổ phác thảo tràn ngập những đường nét giản dị."
3006 = "Mặc dù khí chất bên ngoài khá khác biệt,\nnhưng khi để ý kỹ, thì chỉ có \"khí chất bên ngoài\" là khác thôi."
3008 = "Ra là vậy, hẳn là hợp gu tôi."
3014 = "「Trước hết, nếu nét bút đầu tiên không quyết định được, thì bất kỳ ý tưởng nào cũng không hoàn thành được.」"
3024 = "（Ào!）"
3025 = "（Tõm!）"
```

## Các dòng bị chuyển chỗ (bản dịch đúng đang nằm ở key sai)
Đọc là: key bên trái cần bản dịch đang nằm ở key bên phải. 120 cặp:

- **1442** ← bản dịch đúng đang nằm ở **2412**
- **1450** ← bản dịch đúng đang nằm ở **2819**
- **1818** ← bản dịch đúng đang nằm ở **2220**
- **1822** ← bản dịch đúng đang nằm ở **2698**
- **1826** ← bản dịch đúng đang nằm ở **2411**
- **1845** ← bản dịch đúng đang nằm ở **2216**
- **1854** ← bản dịch đúng đang nằm ở **2911**
- **1859** ← bản dịch đúng đang nằm ở **2663**
- **1863** ← bản dịch đúng đang nằm ở **2671**
- **1864** ← bản dịch đúng đang nằm ở **2383**
- **1876** ← bản dịch đúng đang nằm ở **2177**
- **1890** ← bản dịch đúng đang nằm ở **2946**
- **1895** ← bản dịch đúng đang nằm ở **1984**
- **1896** ← bản dịch đúng đang nằm ở **2932**
- **1931** ← bản dịch đúng đang nằm ở **2837**
- **1937** ← bản dịch đúng đang nằm ở **2074**
- **1946** ← bản dịch đúng đang nằm ở **2951**
- **1950** ← bản dịch đúng đang nằm ở **2681**
- **1967** ← bản dịch đúng đang nằm ở **2197**
- **1970** ← bản dịch đúng đang nằm ở **2387**
- **1972** ← bản dịch đúng đang nằm ở **2956**
- **1974** ← bản dịch đúng đang nằm ở **2205**
- **1982** ← bản dịch đúng đang nằm ở **2161**
- **1989** ← bản dịch đúng đang nằm ở **2088**
- **2009** ← bản dịch đúng đang nằm ở **2304**
- **2011** ← bản dịch đúng đang nằm ở **1979**
- **2031** ← bản dịch đúng đang nằm ở **2888**
- **2032** ← bản dịch đúng đang nằm ở **2134**
- **2036** ← bản dịch đúng đang nằm ở **2274**
- **2068** ← bản dịch đúng đang nằm ở **2578**
- **2076** ← bản dịch đúng đang nằm ở **3025**
- **2101** ← bản dịch đúng đang nằm ở **2958**
- **2110** ← bản dịch đúng đang nằm ở **2989**
- **2118** ← bản dịch đúng đang nằm ở **2125**
- **2145** ← bản dịch đúng đang nằm ở **2301**
- **2152** ← bản dịch đúng đang nằm ở **1403**
- **2158** ← bản dịch đúng đang nằm ở **2311**
- **2168** ← bản dịch đúng đang nằm ở **1994**
- **2171** ← bản dịch đúng đang nằm ở **2085**
- **2174** ← bản dịch đúng đang nằm ở **2153**
- **2181** ← bản dịch đúng đang nằm ở **2351**
- **2209** ← bản dịch đúng đang nằm ở **2694**
- **2214** ← bản dịch đúng đang nằm ở **1993**
- **2219** ← bản dịch đúng đang nằm ở **2054**
- **2228** ← bản dịch đúng đang nằm ở **2591**
- **2231** ← bản dịch đúng đang nằm ở **2833**
- **2240** ← bản dịch đúng đang nằm ở **2740**
- **2242** ← bản dịch đúng đang nằm ở **2662**
- **2244** ← bản dịch đúng đang nằm ở **2634**
- **2247** ← bản dịch đúng đang nằm ở **2286**
- **2252** ← bản dịch đúng đang nằm ở **3014**
- **2257** ← bản dịch đúng đang nằm ở **2701**
- **2272** ← bản dịch đúng đang nằm ở **2746**
- **2275** ← bản dịch đúng đang nằm ở **2106**
- **2285** ← bản dịch đúng đang nằm ở **2138**
- **2291** ← bản dịch đúng đang nằm ở **2307**
- **2321** ← bản dịch đúng đang nằm ở **2432**
- **2322** ← bản dịch đúng đang nằm ở **1956**
- **2326** ← bản dịch đúng đang nằm ở **2914**
- **2333** ← bản dịch đúng đang nằm ở **2375**
- **2336** ← bản dịch đúng đang nằm ở **2132**
- **2346** ← bản dịch đúng đang nằm ở **2646**
- **2347** ← bản dịch đúng đang nằm ở **2149**
- **2348** ← bản dịch đúng đang nằm ở **2391**
- **2388** ← bản dịch đúng đang nằm ở **2985**
- **2392** ← bản dịch đúng đang nằm ở **2202**
- **2394** ← bản dịch đúng đang nằm ở **1991**
- **2395** ← bản dịch đúng đang nằm ở **2164**
- **2397** ← bản dịch đúng đang nằm ở **1912**
- **2409** ← bản dịch đúng đang nằm ở **2628**
- **2410** ← bản dịch đúng đang nằm ở **2824**
- **2419** ← bản dịch đúng đang nằm ở **2810**
- **2428** ← bản dịch đúng đang nằm ở **2007**
- **2564** ← bản dịch đúng đang nằm ở **3024**
- **2576** ← bản dịch đúng đang nằm ở **2814**
- **2580** ← bản dịch đúng đang nằm ở **2058**
- **2595** ← bản dịch đúng đang nằm ở **1409**
- **2611** ← bản dịch đúng đang nằm ở **2226**
- **2616** ← bản dịch đúng đang nằm ở **2414**
- **2624** ← bản dịch đúng đang nằm ở **1849**
- **2651** ← bản dịch đúng đang nằm ở **1439**
- **2657** ← bản dịch đúng đang nằm ở **2668**
- **2658** ← bản dịch đúng đang nằm ở **2813**
- **2678** ← bản dịch đúng đang nằm ở **2180**
- **2682** ← bản dịch đúng đang nằm ở **1880**
- **2686** ← bản dịch đúng đang nằm ở **2565**
- **2687** ← bản dịch đúng đang nằm ở **2577**
- **2690** ← bản dịch đúng đang nằm ở **2067**
- **2696** ← bản dịch đúng đang nằm ở **2308**
- **2712** ← bản dịch đúng đang nằm ở **2148**
- **2721** ← bản dịch đúng đang nằm ở **2018**
- **2724** ← bản dịch đúng đang nằm ở **2676**
- **2727** ← bản dịch đúng đang nằm ở **2280**
- **2731** ← bản dịch đúng đang nằm ở **2821**
- **2736** ← bản dịch đúng đang nằm ở **2128**
- **2744** ← bản dịch đúng đang nằm ở **2805**
- **2749** ← bản dịch đúng đang nằm ở **2327**
- **2761** ← bản dịch đúng đang nằm ở **2418**
- **2769** ← bản dịch đúng đang nằm ở **2139**
- **2806** ← bản dịch đúng đang nằm ở **2835**
- **2816** ← bản dịch đúng đang nằm ở **2433**
- **2826** ← bản dịch đúng đang nằm ở **1953**
- **2829** ← bản dịch đúng đang nằm ở **2324**
- **2857** ← bản dịch đúng đang nằm ở **1987**
- **2884** ← bản dịch đúng đang nằm ở **2752**
- **2889** ← bản dịch đúng đang nằm ở **2264**
- **2898** ← bản dịch đúng đang nằm ở **2702**
- **2900** ← bản dịch đúng đang nằm ở **2385**
- **2906** ← bản dịch đúng đang nằm ở **2575**
- **2928** ← bản dịch đúng đang nằm ở **2629**
- **2938** ← bản dịch đúng đang nằm ở **2684**
- **2949** ← bản dịch đúng đang nằm ở **2330**
- **2950** ← bản dịch đúng đang nằm ở **1985**
- **2953** ← bản dịch đúng đang nằm ở **2204**
- **2984** ← bản dịch đúng đang nằm ở **1436**
- **2986** ← bản dịch đúng đang nằm ở **2013**
- **2987** ← bản dịch đúng đang nằm ở **2407**
- **2996** ← bản dịch đúng đang nằm ở **1978**
- **3000** ← bản dịch đúng đang nằm ở **2666**
- **3006** ← bản dịch đúng đang nằm ở **2840**

- 4 bản dịch chuyển chỗ có mang theo dấu ruby thừa từ file gốc, đã làm sạch trong khối trên: **1826** (từ 2411, bỏ `[Đường sắt Hoàng gia cũ, 4]`), **2348** (từ 2391, bỏ `[8620, 4]`), **1937** (từ 2074, bỏ `[Một người như vậy, 1]`), **2388** (từ 2985, bỏ `[Cửa buồng khói, 2]`). Các thẻ `%l` trong bản dịch chuyển chỗ được giữ nguyên (2118, 2749, 2938).

## Các cặp trùng lặp đáng chú ý
- `「Đã rõ.」` xuất hiện 10 lần trong file và **cả 10 đều sai** (JP gốc của chúng là các câu khác nhau, không phải 「了解」/「心得た」). Toàn dự án có 54 lần xuất hiện `「Đã rõ.」`, phần lớn là đúng ở file khác — riêng file này thì 10/10 sai, cho thấy câu này đã bị dán bừa vào đây.
- `「Cảm ơn cô…」` ở 1845 (sai) và 1876 (sai) — cả hai đều không phải bản dịch của key mình; bản dịch đúng của 1845 nằm ở 2216.
- Câu dẫn về van tiết lưu ("Tôi từ từ kéo van tiết lưu… 8620…") ở 1857 và 2392 — cả hai đều sai, và **không có JP nào trong toàn dự án khớp với câu này** (đây là lời dẫn cảnh lái tàu từ file/chương khác, rơi lạc vào đây). Tương tự: `「Ngài Soutetsu, ngài đã sẵn sàng chưa ạ?」` (1413, 2056), câu xuất phát ("Vậy thì, chúng ta xuất phát thôi ạ. Xin hãy kéo còi.") (1931, 1954), câu còi tàu (1967, 2049), `「Vâng. Chúng ta hãy cùng nhau cố gắng nhé.」` (2326, 2806) — đều là bản dịch của cảnh lái tàu, không có JP tương ứng trong file này.
- `「Không có chi ạ. Đó là nhiệm vụ của tôi mà.」` (2014, 2891) — chỉ có một lần xuất hiện khác trong toàn dự án (日々姫16_夢を乗せて 2010) mà JP ở đó (`どういたしまして。こちらこそ`) cũng không khớp — coi như câu mồ côi, cả hai key đều dịch mới trong khối trên.

## Dòng cần Hieu xác nhận (1 dòng)
- **2158** (Thị trưởng Yufuin) — ĐÃ CHỐT 19/11 theo quyết định của Hieu: JP là `[めいぐん,1]冥軍` = "Minh Quân", nghĩa đen là đội quân cõi âm / quân đội ma (tín ngưỡng dân gian Đài Loan, tiên hiệp/kỳ ảo) — KHÔNG phải quân đội Mỹ. TW viết 美軍 (quân Mỹ) là diễn giải lại, không theo. Bản dịch đúng của dòng này đã xác nhận bằng chuyển chỗ (đang nằm ở 2311); khối trên đã sửa thành "Minh Quân" thay cho "quân đội Mỹ".

## Đề xuất cập nhật context (để Hieu quyết, KHÔNG tự đổi toàn dự án)
1. **帝鉄:** chỉ xuất hiện ở 1 dòng sai trong file này (1826). Bản sửa dùng theo docs: "Đường sắt Hoàng gia cũ" ("Railord của đầu máy hơi nước loại 8620 của Đường sắt Hoàng gia cũ, số hiệu 38696"). Vẫn chờ Hieu chốt giữa "Đường sắt Hoàng gia" (docs) và "Teitetsu" (dạng ngắn trong file Grand 01).
2. **御一夜鉄道:** xuất hiện ở 1 dòng sai (2101). Bản sửa dùng "Đường sắt Ohimitera" theo đề xuất của audit Grand 01 (nhất quán với tên thành phố Ohimitera), chưa phải quyết định cuối — Hieu chọn giữa "Ohito" (file obasan) và "Ohimitera" (Grand 01 + file này). Quyết định 19/11: 御一夜 = Ohitoyo — bản sửa 2101 đã đổi sang "Đường sắt Ohitoyo" (đợt sửa 19/11).
3. **湯医線:** xuất hiện ở 1 dòng sai (2058, furigana ゆのい). Bản sửa dùng "tuyến Yunoi" theo đề xuất của audit Grand 01, thay cho "tuyến Yui" của audit 廃炭鉱. Trong cùng dòng này còn có 来大鉄道 (furigana くるだい) → "Đường sắt Kurudai" và 肥田 → "Hita" (theo furigana ひた, khớp với Hita thật ở Kyushu).
4. Không có đề xuất cập nhật context mới phát sinh từ file này ngoài 3 quyết định đang chờ trên — các quy tắc docs còn lại đều áp dụng được trơn tru.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- Soutetsu độc thoại/dẫn chuyện xưng "Tôi"; Hibiki gọi Soutetsu là "anh hai"; Hachiroku gọi Soutetsu là "ngài Soutetsu"; Mikuro gọi Soutetsu là "ngài Soutetsu", xưng "em"; Thị trưởng Yufuin xưng "Tôi"
- 帝鉄 = Đường sắt Hoàng gia (theo docs; xem đề xuất 1); 御一夜鉄道 = Đường sắt Ohitoyo (Quyết định 19/11; xem đề xuất 2); 湯医線 = tuyến Yunoi (xem đề xuất 3); 来大鉄道 = Đường sắt Kurudai; 肥田 = Hita; 由布院 / 湯布院 / 湯富院 = Yufuin (giữ theo cách viết của từng thời kỳ trong JP: 湯富院 là tên hiện tại sau sáp nhập)
- エアクラ = Aircra (không đổi thành Aircraft); 機関士 = lái tàu / người lái tàu; 機関助士 = phụ lái tàu; レイルロオド = Railord; 8620 = 8620 (giữ nguyên số hiệu); D51 1031 = D51 1031; 38696 = 38696
- 湯富院市長 = Thị trưởng Yufuin; 御一夜市 = thành phố Ohitoyo (Quyết định 19/11; các dòng đúng trong file vẫn dùng "Ohimitera", chờ đợt thống nhất sau); 雄武田 = Omuta; 湯之比良 = Yunohira; 湯平 = Yunohira (làng cũ); 由布院 = Yufuin (tên cũ)
- ポー (còi tàu) = "Tuúú…" (theo sfx §1.1; các dòng còi trong file này đều đã có sẵn dạng đúng ở key gốc, không cần sửa thêm)
- 扇形機関庫 = nhà chứa đầu máy hình quạt (giữ thẻ %l); 静態保存 = bảo quản tĩnh (giữ thẻ %l); 大戦 = Đại chiến, 大詔 = Taisho, 正和 = Showa (giữ thẻ %l ở 2749)
- Gamadasu Cafe = quán Gamadasu Cafe (giữ nguyên tên riêng như các dòng đúng trong file); SLホテル = SL Hotel; てづくりの静謐 = "sự tĩnh lặng thủ công" (theo cách gọi đã dùng trong file)
- Các câu cảm thán ngắn dịch tiếng hít っ thành Ư (sửa theo quét っ toàn dự án 19/11; trước đây audit giữ nguyên dạng JP): 「——Ư」, 「Ư!」, 「Ư――」

## Giới hạn của audit này
- Đã đọc hết 434 dòng script của file này: 374 dòng sai đã xác nhận, 60 dòng còn lại khớp JP/TW.
- Vẫn có thể sót vài dòng "trông hợp lý nhưng thực ra là bản dịch của dòng khác" — cách chắc chắn nhất vẫn là chơi qua chương và đối chiếu voice. Nếu Hieu gặp thêm dòng nào nghi ngờ trong file này thì gửi mình, mình kiểm tra nốt.
- 210/330 dòng lệch chưa truy vết được về đúng key gốc của chúng (chỉ xác nhận được 120 cặp). Chúng đều là câu Việt có nghĩa, thuộc cảnh khác trong chương — không phải câu vô nghĩa hay câu "mồ côi" không có nguồn. Muốn truy vết hết cần đối chiếu từng câu với toàn bộ JP của chương, việc này làm được nếu Hieu cần.
- File này (86,2% sai) nặng nhất trong 4 file đã audit: 廃炭鉱 133 (31%), obasan 255 (56%), Grand 01 299 (45,6%), Hibiki 03 374 (86,2%). Tổng 4 file: **1.061 dòng sai** — con số ~662 dòng sai toàn dự án ước tính bằng máy check trước đây giờ đã bị vượt xa, và chỉ mới audit 4/216 file.

## Việc tiếp theo
1. Áp dụng khối TOML trên cho file Hibiki 03 (nhớ quyết 3 đề xuất context ở trên trước, để khỏi sửa đi sửa lại), chơi thử chương Hibiki 03 rồi báo lại.
2. Audit tiếp các file nặng còn lại: Hachiroku 13, Nagi_Fukami 08a — mỗi file một bản review như file này.
3. Xuất lại CSV mới từ TOML (sau khi áp fix) để CSV không còn cũ — với CSV3 thì Mayami đã đủ, chỉ còn 2 dòng lẻ chưa dịch (lr真闇追加01/02) là cần dịch mới; 144/146 dòng chưa dịch đã có bản dịch trong các khối audit (Grand 01: 100, Hibiki 03: 44).

## Kết bài
Hibiki 03 là file thứ tư được audit toàn bộ, và là file nặng nhất từ trước tới nay: 374/434 dòng (86,2%) đang hiển thị sai lời thoại so với voice — gần như toàn bộ chương, trong đó Mikuro không có một dòng thoại nào đúng (34/34 sai) và 44 dòng còn nguyên tiếng Trung chưa dịch. Cơ chế lỗi vẫn như các file trước — cột Việt bị xáo trộn rải rác ngay từ lúc dịch trên Sheets, không lệch đều theo key — nhưng mức độ ở đây cho thấy gần như toàn bộ file đã bị xáo trộn trong một lần dán nhầm lớn, chứ không phải vài lỗi lẻ tẻ. Tin tốt vẫn như cũ: JP và TW khớp nhau, nên mọi dòng sai đều sửa được chỉ bằng cách dịch lại từ JP/TW hoặc lấy lại bản dịch đúng đang nằm sai chỗ — và khối TOML trong bản này đã xử lý đủ cả 374 dòng, kiểm tra parse 374/374, trong đó 120 dòng lấy lại từ bản dịch chuyển chỗ, 254 dòng dịch mới.

Việc còn lại của riêng file này chỉ là ba quyết định context đang chờ chung cho cả dự án (帝鉄, 御一夜鉄道, 湯医線) — còn 冥軍 ở 2158 thì Hieu đã chốt 19/11 là "Minh Quân" theo nghĩa đen của JP, không theo TW; sau đó là áp dụng khối TOML và chơi thử chương để nghiệm thu. Còn về tổng thể dự án, bốn file đã audit xong đã có 1.061 dòng sai — con số ước tính cũ ~662 giờ đã bị vượt gần gấp đôi chỉ với 4 file — nên bước tiếp theo hợp lý nhất vẫn là audit Hachiroku 13 rồi Nagi_Fukami 08a, hai file nặng còn lại trong danh sách, trước khi tính tới việc rebuild toàn bộ từ CSV3.

---
**Bổ sung 19/11 (quét っ toàn dự án):** 2 giá trị sửa trong khối trên đã được sửa lại chỗ gasp — 1933 「っ！！」→「Ư！！」, 2433 「～～っ」→「～～Ư」. Giá trị sweep thay thế giá trị audit (audit giữ nguyên dạng JP của tiếng hít). Khối TOML đã parse lại: 374/374 key, khớp JSON (trừ khác biệt `\n` đã biết ở 2158). Tổng số dòng sai không đổi (374).
