import os

translations = {
    'tw_tips_絶気運転.txt': '''Chạy cắt hơi (Zekki unten)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Việc điều khiển tàu chạy trong trạng thái cắt hơi —— tức là không dẫn hơi nước vào xi-lanh và piston —— được gọi là chạy cắt hơi (zekki unten) ạ. Đối với các phương tiện đường sắt khác ngoài đầu máy hơi nước, việc chạy tàu chỉ bằng lực quán tính mà không cung cấp thêm động lực như vậy cũng được gọi là chạy tính quán tính ạ」''',

    'tw_tips_貨車.txt': '''Toa chở hàng (Ka-sha)
*解説
;---------------------------------------------------------------
【Reina】
「Toa xe được chế tạo nhằm vận chuyển hàng hóa chứ không phải chuyên chở hành khách chính là toa chở hàng đó ạ. Loại có trần che chắn đàng hoàng được gọi là toa hàng có mái che. Còn loại không có trần hay tường chắn, khiến hàng hóa lộ thiên hoàn toàn thì gọi là toa hàng không mái che đó ạ」''',

    'tw_tips_走行部.txt': '''Bộ phận chuyển động (Sokobu)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Bánh xe chủ động, trục bánh xe, thanh nối chính, thanh truyền, hộp trục và giá dẫn hướng hộp trục, tập hợp một chuỗi các thiết bị phục vụ cho việc di chuyển của xe lửa được gọi chung là bộ phận chuyển động (sokobu) ạ. Có lẽ ngày nay cách gọi thiết bị chuyển động phổ biến hơn đúng không ạ」''',

    'tw_tips_跨線橋.txt': '''Cầu vượt đường sắt (Kosenkyo)
*解説
;---------------------------------------------------------------
【Paulette】
「Chiếc cầu được xây dựng bắc ngang qua đường ray xe lửa chính là cầu vượt đường sắt (kosenkyo). Nó không chỉ đóng vai trò làm đường xe chạy hay lối đi bộ, mà đôi khi còn phục vụ làm đường dẫn lên ga trên cao —— tức nhà ga được xây dựng ngay trên cầu vượt đường sắt đó đấy」''',

    'tw_tips_踏面.txt': '''Mặt lăn bánh xe (Tomen)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Mặt lăn bánh xe (tomen) là bề mặt tiếp xúc trực tiếp với đường ray của bánh xe phương tiện đường sắt ạ」

【Soutetsu】
「Diện tích tiếp xúc giữa đường ray và bánh xe là vô cùng nhỏ. Do đó, việc duy trì trạng thái tốt nhất có thể cho mặt lăn bánh xe chính là điều kiện tiên quyết tuyệt đối để đảm bảo an toàn vận hành」

【Hachiroku】
「Giả sử nếu chạm bàn tay có dính dầu mỡ vào mặt lăn bánh xe, chỉ bấy nhiêu thôi cũng đủ khiến cự ly hãm phanh của toa xe đó bị kéo dài ra gấp nhiều lần. Mặt lăn bánh xe là bộ phận nhạy cảm và quan trọng đến như vậy đó ạ」''',

    'tw_tips_車両鉄.txt': '''Người sành toa xe (Sharyo-tetsu)
*解説
;---------------------------------------------------------------
【Paulette】
「Sharyo-tetsu là những người hâm mộ đường sắt có sự quan tâm vô cùng sâu sắc đối với chính bản thân các toa xe đường sắt. Kiến thức sâu rộng và khả năng phân tích tỉ mỉ của họ thậm chí khiến những người trong ngành cũng phải trầm trồ thán phục, nên họ thường được gọi là 'tín đồ đường sắt chuyên sâu nhất' đấy」''',

    'tw_tips_車掌.txt': '''Trưởng tàu (Shasho)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Cùng với người lái tàu và nhân viên điều khiển, thành viên tổ lái thực hiện nhiệm vụ bảo đảm vận hành an toàn cho đoàn tàu —— chính là trưởng tàu (shasho) ạ. Dưới thời Đường sắt Hoàng gia trước đây, họ còn được gọi tắt là Rechi ạ」

【Paulette】
「Nhiệm vụ của trưởng tàu bao quát hầu như toàn bộ các công việc liên quan đến hành khách hoặc hàng hóa. Từ xác nhận an toàn khi đóng mở cửa toa xe, hướng dẫn cho hành khách và hàng hóa, soát vé trên tàu, vận hành van trưởng tàu trên toa hãm phanh —— cho đến việc đại diện thực hiện chức trách của ga trưởng tại các ga không có nhân viên đấy」

【Hachiroku】
「Tức là xác nhận tín hiệu xuất phát và phát lệnh xuất phát ạ. Công việc của trưởng tàu đa dạng và quan trọng như vậy, cho nên khi chạy đường dài, sự đồng hành của một trưởng tàu xuất sắc sẽ giúp người lái tàu và Railord cảm thấy vô cùng an tâm ạ」''',

    'tw_tips_車掌車.txt': '''Toa xe trưởng tàu (Shasho-sha)
*解説
;---------------------------------------------------------------
【Paulette】
「Toa xe trưởng tàu (shasho-sha) là toa xe đường sắt chuyên dụng làm nơi làm việc cho trưởng tàu —— phân loại chính xác thì nó là một loại toa chở hàng công vụ. Trên toa xe trưởng tàu luôn được trang bị thiết bị phanh hãm để sử dụng trong các trường hợp khẩn cấp đấy」''',

    'tw_tips_車輌検査.txt': '''Kiểm tra toa xe (Sharyo kensa)
*解説
;---------------------------------------------------------------
【Paulette】
「Sứ mệnh lớn nhất của ngành đường sắt là an toàn. Trong Luật Đường sắt Hinamoto cũng quy định rõ rằng: 'Không được đưa phương tiện vào sử dụng trừ khi nó đang trong trạng thái có thể vận hành an toàn'」

【Reina】
「Vì vậy, trước khi cho tàu chạy, hoặc sau khi tàu đã đi được quãng đường hay thời gian quy định, người ta sẽ tiến hành kiểm tra xem tàu có bị hỏng hóc hay gặp sự cố gì không. Đó chính là kiểm tra toa xe đó ạ」''',

    'tw_tips_軌間.txt': '''Khổ đường sắt (Kikan)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Khoảng cách giữa hai thanh ray bên phải và bên trái cấu thành nên đường ray xe lửa được gọi là khổ đường sắt (kikan) ạ. Nói một cách chính xác, khổ đường sắt được quy định là khoảng cách ngắn nhất giữa hai thanh ray đo tại vị trí trong vòng 14mm tính từ đỉnh ray xuống ạ」''',

    'tw_tips_転轍機.txt': '''Thiết bị bẻ ghi (Tentetsuki)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Thiết bị bẻ ghi (tentetsuki) là thiết bị cơ khí dùng để chuyển hướng các tấm ghi bẻ ghi đường sắt ạ. Thiết bị thủ công có chức năng tương tự thì được gọi là cần bẻ ghi thủ công. Để biết thêm chi tiết, xin mời tham khảo thêm các mục cần bẻ ghi và bẻ ghi đường sắt ạ」''',

    'tw_tips_軸箱.txt': '''Hộp trục (Jiku-bako)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Thanh trục tròn nối giữa hai bánh xe chủ động trái phải với nhau được gọi là trục bánh xe ạ. Hộp trục (jiku-bako) nói một cách đơn giản chính là thiết bị đảm nhận vai trò đỡ lấy trục bánh xe đó ạ」

【Soutetsu】
「Đối với dòng 8620, bánh xe chủ động trái phải và trục bánh xe —— tức cụm bánh xe trục bánh được lắp trực tiếp vào khung gầm làm bệ đỡ thân xe, và được nâng đỡ từ cả hai phía trái phải bằng một cặp hộp trục kẹp chất lấy —— cấu trúc được thiết kế như vậy」

【Paulette】
「Tóm lại, hộp trục có thể được coi là chiếc hộp đóng vai trò cố định, giữ cho thanh trục nối giữa các bánh xe không bị tuột hoặc lệch ra ngoài đấy」''',

    'tw_tips_軸箱守.txt': '''Giá dẫn hướng hộp trục (Jikuhakomori)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Khi phương tiện di chuyển, hộp trục nâng đỡ bánh xe chủ động và trục bánh xe phải chịu những lực tác động rất mạnh từ nhiều hướng: trên dưới, trái phải, trước sau ạ. Đồng thời, để lắp đặt hộp trục, người ta bắt buộc phải khoét một lỗ có kích thước tương đương trên khung gầm dạng tấm ạ」

【Soutetsu】
「Nói cách khác, cả hộp trục và khung gầm đều phải gánh chịu tải trọng vô cùng lớn. Để ngăn ngừa nứt gãy do tải trọng này gây ra, người ta lắp đặt các bộ phận bằng thép để gia cố cường lực. Bộ phận gia cố đó chính là giá dẫn hướng hộp trục (jikuhakomori) đúng như tên gọi của nó」

【Hachiroku】
「Bên cạnh việc gia cố bằng giá dẫn hướng hộp trục, các bộ phận giảm chấn lò xo khác nhau cũng được bố trí để giảm bớt tải trọng tác động ạ. Tuy vậy, đôi khi các sự cố hư hỏng vẫn phát sinh, điều đó cho thấy tải trọng tác động lên các bộ phận khi tàu chạy là cực kỳ khổng lồ ạ」''',

    'tw_tips_運転台.txt': '''Buồng lái (Untendai)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Trên các loại đầu máy xe lửa, khu vực nơi người lái tàu làm việc và thực hiện các thao tác vận hành điều khiển được gọi là buồng lái (untendai) hay còn gọi là cab cabin ạ」

【Reina】
「Đối với các loại toa xe tự hành hay tàu điện có khoang lái và ghế hành khách được bố trí chung trên cùng một toa xe, người ta thường gọi là ghế lái chứ không gọi là buồng lái đâu ạ」''',

    'tw_tips_運転整備重量.txt': '''Khối lượng chỉnh bị vận hành (Unten seibi juryou)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Khối lượng chỉnh bị vận hành (unten seibi juryou) là trọng lượng của đầu máy khi ở trạng thái thực tế sẵn sàng hoạt động. Ví dụ như đối với dòng 8620, trọng lượng khi đã nạp đầy đủ nước và than cần thiết để chạy chính là khối lượng chỉnh bị vận hành ạ」'''
}

out_dir = r"E:\まいてつ Last Run!!\vn_patch"
for name, content in translations.items():
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote {name}")
