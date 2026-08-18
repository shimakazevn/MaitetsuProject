import os

translations = {
    'tw_tips_ピット.txt': '''Hố kiểm tra (Pit)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Trên các đường ray bên trong gara đầu máy hoặc những khu vực tương tự, có những đoạn được đào khoét sâu xuống phía dưới đường ray tạo thành một khoảng lõm thấp. Khoảng lõm đó được gọi là hố kiểm tra (pit) ạ」

【Paulette】
「Việc kiểm tra và bảo dưỡng gầm toa xe sẽ dễ dàng thực hiện hơn khi đi xuống hố kiểm tra và ngước nhìn lên phía dưới gầm xe. Đó chính là vai trò của hố kiểm tra đấy」''',

    'tw_tips_フランジ.txt': '''Gờ bánh xe (Flange)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Khi lực ly tâm tác động lên phương tiện đường sắt, thân xe sẽ bị lắc lư và có nguy cơ gây ra trật bánh. Do đó, để ngăn bánh xe không bị văng ra khỏi đường ray dưới tác động của lực ly tâm này, người ta thiết kế một phần nhô ra có độ dốc nằm ở phía trong của cả hai bánh xe bên trái và bên phải để kẹp sát vào đường ray —— bộ phận đó gọi là gờ bánh xe (flange) ạ」

【Paulette】
「Ví dụ, khi rẽ phải, thân xe và phần phía sau của đoàn tàu sẽ bị lực ly tâm đẩy lệch sang phía bên trái, nếu không có gì cản lại thì tàu sẽ văng ra khỏi đường ray. Lúc này, gờ bánh xe nằm ở phía trong của bánh xe bên trái sẽ tì sát vào mặt trong của thanh ray bên trái, từ đó ngăn chặn tình trạng trật bánh xảy ra đấy」

【Hachiroku】
「Do vai trò đảm nhận như vậy, gờ bánh xe là một bộ phận rất dễ bị hao mòn. Vì thế, gờ bánh xe của những đầu máy xe lửa thường xuyên di chuyển đường dài thường được tôi nhiệt luyện để gia tăng độ cứng, đồng thời luôn được bảo trì kỹ lưỡng để giữ nguyên hình dạng tiêu chuẩn khi vận hành ạ」''',

    'tw_tips_ブロワー.txt': '''Thiết bị thổi gió (Blower)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Thiết bị thổi gió (blower) là thiết bị dùng để đảm bảo thông gió bên trong buồng đốt nhằm giúp than cháy tốt hơn ạ. Khi kích hoạt thiết bị thổi gió, lượng khí thải từ xi-lanh sẽ được xả ra khi tàu chạy, và hơi nước trong lò hơi sẽ được xả ra từ ống khói khi tàu dừng ạ」

【Soutetsu】
「Khi đó, không gian gọi là buồng khói được kết nối với buồng đốt thông qua các ống lò hơi sẽ tạm thời rơi vào trạng thái gần như chân không. Để bù đắp lại khoảng chân không đó, một lực hút không khí mạnh mẽ sẽ xuất hiện, khiến một lượng lớn không khí trong lành ùa vào bên trong buồng đốt」

【Hachiroku】
「Blower là tên của thiết bị vừa được giải thích ở trên ạ. Hành động vận hành blower vào bất kỳ thời điểm nào để nó hoạt động được gọi là thông gió (blow). Chiếc van dùng để mở thông gió được gọi là van thông gió ạ」''',

    'tw_tips_ヘッドマーク.txt': '''Biểu trưng đầu tàu (Headmark)
*解説
;---------------------------------------------------------------
【Paulette】
「Biểu trưng tàu được hiển thị ở toa xe đầu tiên của đoàn tàu chính là biểu trưng đầu tàu (headmark). Để biết thêm chi tiết, các bạn hãy xem thêm ở mục biểu trưng tàu nhé」''',

    'tw_tips_モハシ21試験車両.txt': '''Toa xe thử nghiệm Mohashi 21
*解説
;---------------------------------------------------------------
【Niiroku】
「Mohashi 21 là toa xe kết hợp giữa toa hạng phổ thông và quầy ăn nhẹ, được bổ sung thử nghiệm vào đoàn tàu cơ bản gồm 4 toa Kuha 26 vốn được thử nghiệm dưới thời Đường sắt Hoàng gia trước đây. Nếu Đường sắt Hoàng gia không bị xóa sổ bởi đợt đại bãi bỏ các tuyến đường sắt, thì chắc chắn nó đã được đưa thẳng vào vận hành thương mại rồi」''',

    'tw_tips_モーターカー.txt': '''Toa xe công trình (Motor car)
*解説
;---------------------------------------------------------------
【Paulette】
「Toa xe công trình là loại thiết bị máy móc có thể tự chạy trên đường ray bằng động cơ của chính mình, nhưng lại không có đăng ký xe —— tức là không được quản lý như một phương tiện đường sắt thông thường, chủ yếu được sử dụng cho các công tác dồn toa hoặc bảo trì đường ray」

【Reina】
「Mặc dù có tên gọi tiếng Anh chứa từ 'motor', nhưng hầu hết các toa xe công trình này lại chạy bằng động cơ diesel chứ không phải động cơ điện đâu ạ」''',

    'tw_tips_ループ線.txt': '''Đường ray vòng tròn (Loop line)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Các phương tiện đường sắt rất khó di chuyển trên các dốc dựng đứng. Do đó, để tránh độ dốc quá lớn, đôi khi người ta áp dụng phương pháp thiết kế đường ray vòng quanh liên tục như một vòng tròn lớn với độ dốc thoai thoải, nhờ đó tích lũy độ cao dần dần ạ」

【Paulette】
「Đường ray có độ dốc thoai thoải chạy vòng tròn quanh núi đó được gọi là đường ray vòng tròn (loop line). Thông thường, để giải quyết vấn đề vượt qua các dốc dựng đứng, người ta sẽ chọn xây dựng đường ray vòng tròn hoặc đường vòng zigzag (switchback) đấy」''',

    'tw_tips_レイルロオド.txt': '''Railord (Búp bê đường sắt)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Là các thực thể dạng người hoặc mô-đun hình nhân được chế tạo đồng bộ với các phương tiện đường sắt có buồng lái hoặc ghế lái, nhằm hỗ trợ việc vận hành và bảo dưỡng các phương tiện đường sắt đó. Đó chính là các Railord ạ」

【Reina】
「Giữa các Railord với nhau có thể liên lạc thông qua sự cộng cảm. Vì thế, cơ chế này cực kỳ tiện lợi cho việc ngăn ngừa tai nạn đường sắt và lập biểu đồ chạy tàu đó ạ」

【Hachiroku】
「Để biết thêm chi tiết, xin vui lòng xem thêm ở các mục cộng cảm và biểu đồ chạy tàu ạ」''',

    'tw_tips_ロック.txt': '''Bó bánh (Lock)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Bó bánh (lock) là thuật ngữ chỉ việc tạm thời dừng tăng áp suất phanh hoặc nới lỏng áp suất phanh đã áp dụng nhằm tránh nguy cơ trượt bánh (quay trơn) ạ. Để biết thêm chi tiết, xin hãy tham khảo thêm các mục áp suất, phanh, và trượt bánh (quay trơn) ạ」''',

    'tw_tips_一等二等併設客車.txt': '''Toa xe ghép hạng nhất hạng hai (Itto nito heisetsu kyaku-sha)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Đúng như tên gọi của nó, đây là loại toa hành khách có bố trí cả ghế hạng nhất và ghế hạng hai trong cùng một toa xe ạ. Tên gọi chính thức hơn của nó là toa xe hỗn hợp hạng nhất - hạng hai ạ」

【Paulette】
「Tại Đường sắt Ohito, khoang đặc biệt của đoàn tàu du lịch được xem là toa hạng nhất. Hạng hai là vé đặt trước (chỉ định ghế). Vé tự do được tính là toa thường đấy」''',

    'tw_tips_中間車.txt': '''Toa giữa (Chukan-sha)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Mặc dù trên thực tế có những cách phân loại chi tiết hơn, nhưng trong hoạt động thường ngày của Đường sắt Ohito, chúng tôi gọi những toa xe có buồng lái hoặc ghế lái nằm ở hai đầu của đoàn tàu là toa đầu hành trình. Những toa xe nằm trong sơ đồ ghép của đoàn tàu và không nằm ở hai đầu —— tức không phải toa đầu, được gọi là toa giữa ạ」

【Paulette】
「Vì vậy, ngay cả đối với toa xe có buồng lái hoặc ghế lái —— tức toa điều khiển, nếu nó nằm ở giữa đoàn tàu thì vẫn được coi là toa giữa đấy」

【Hachiroku】
「Các toa điều khiển nằm ở vị trí toa giữa rất hữu ích khi cần chia nhỏ đoàn tàu. Ví dụ, một đoàn tàu 6 toa gồm: toa điều khiển - toa giữa - toa điều khiển - toa điều khiển - toa giữa - toa điều khiển có thể dễ dàng tách thành hai đoàn tàu 3 toa độc lập ạ」''',

    'tw_tips_乗り鉄.txt': '''Người thích đi tàu (Nori-tetsu)
*解説
;---------------------------------------------------------------
【Paulette】
「Nori-tetsu là những người hâm mộ đường sắt có sở thích thích ngồi tàu xe để đi lại. Nghĩ lại thì, mình cũng tự coi mình là một người thích đi tàu ở mức độ nhẹ đấy」''',

    'tw_tips_保線部長.txt': '''Trưởng bộ phận bảo trì đường ray (Hosen buchou)
*解説
;---------------------------------------------------------------
【Soutetsu】
「Tại Đường sắt Ohito, công việc bảo trì đường ray —— chủ yếu là các hoạt động bảo dưỡng và kiểm tra để đảm bảo an toàn cho đường ray —— sẽ do Bộ phận bảo trì phụ trách. Trưởng bộ phận, người chịu trách nhiệm chính chính là Trưởng bộ phận bảo trì đường ray」''',

    'tw_tips_信号炎管.txt': '''Ống pháo hiệu (Shingo enkan)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Sứ mệnh lớn nhất của ngành đường sắt là an toàn. Trong trường hợp an toàn không được đảm bảo, chúng tôi bắt buộc phải lập tức dừng toàn bộ các đoàn tàu xung quanh để đảm bảo an toàn ạ」

【Paulette】
「Ống pháo hiệu là thiết bị phát tín hiệu đặc biệt dùng để bảo đảm an toàn. Khi được kích hoạt, ống pháo hiệu sẽ bùng lên ngọn lửa màu đỏ để phát tín hiệu báo động, thông báo cho các đoàn tàu xung quanh biết có chướng ngại gây nguy hiểm đến việc vận hành an toàn đang xảy ra đấy」''',

    'tw_tips_先台車.txt': '''Giá chuyển hướng trước (Sen-daisha)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Những phương tiện đường sắt có cấu trúc lắp bánh xe chủ động trực tiếp trên khung gầm dạng tấm giống như dòng 8620 sẽ không có khả năng ôm cua tốt ở những khúc cua gấp. Do đó, người ta thiết kế một giá chuyển hướng hoạt động độc lập ở phía trước và lắp bánh xe không có động cơ vào đó để đóng vai trò dẫn hướng khi đi vào khúc cua ạ」

【Soutetsu】
「Giá chuyển hướng đó chính là giá chuyển hướng trước (sen-daisha). Bánh xe được lắp trên giá chuyển hướng trước được gọi là bánh dẫn hướng」

【Hachiroku】
「Để biết thêm chi tiết, xin hãy tham khảo thêm các mục khung gầm, hộp trục, giá chuyển hướng, và bánh xe chủ động ạ」'''
}

out_dir = r"E:\まいてつ Last Run!!\vn_patch"
for name, content in translations.items():
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote {name}")
