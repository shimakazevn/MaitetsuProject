import os

translations = {
    'tw_tips_形式称号.txt': '''Kí hiệu loại toa xe (Keishiki shogo)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Kí hiệu loại toa xe (keishiki shogo) là tên viết tắt được thiết lập nhằm thể hiện một cách ngắn gọn và đầy đủ về loại hình —— hay nói cách khác là mục đích sử dụng —— của toa xe đó ạ」

【Reina】
「Kiha 07S của Reina được ghép từ chữ 'Ki' biểu thị cho toa xe tự hành, và chữ 'Ha' đại diện cho toa hành khách hạng phổ thông, ghép lại thành 'Kiha' đó ạ」

【Hachiroku】
「Đầu máy hơi nước thời đại của chúng tôi ban đầu có kí hiệu loại toa xe chỉ gồm các con số như 8620 hay 9600, nhưng sau đó quy tắc đã đổi sang sử dụng chữ cái C cho loại có 3 trục bánh chủ động, chữ D cho loại có 4 trục bánh chủ động. Đầu máy hơi nước thùng nước được đánh số từ 1 đến 49, và đầu máy hơi nước chở than nước được đánh số từ 50 đến 99 ạ. Vì thế, ví dụ khi nhìn thấy kí hiệu D51, ta có thể biết ngay đó là đầu máy hơi nước chở than nước có 4 trục bánh chủ động ạ」''',

    'tw_tips_待避線.txt': '''Đường tránh tàu (Taihisen)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Tuyến đường sắt nối giữa các ga với nhau mà chỉ có duy nhất một đường chính thì được gọi là đường đơn ạ」

【Paulette】
「On đường đơn, nếu cho tàu chạy xuôi và tàu chạy ngược hoạt động cùng lúc thì sẽ xảy ra va chạm trực diện. Còn nếu tàu tốc hành muốn vượt qua tàu thường thì sẽ xảy ra va chạm từ phía sau. Để ngăn ngừa những sự cố đó, một trong hai đoàn tàu phải đi tránh sang một bên đúng không nào」

【Hachiroku】
「Vài đường ray được rẽ nhánh ra từ đường chính phục vụ cho việc tránh tàu đó chính là đường tránh tàu (taihisen) ạ」''',

    'tw_tips_従輪.txt': '''Bánh xe chịu tải không động lực (Jurin)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Bánh xe nhận lực truyền trực tiếp từ động cơ để tự quay gọi là bánh xe chủ động ạ. Bánh xe chịu tải không động lực (jurin) là bánh xe quay theo chuyển động chạy của đoàn tàu vốn được kéo đi nhờ lực quay của bánh chủ động —— nói cách khác là bánh xe không nhận truyền động trực tiếp từ động cơ ạ」

【Soutetsu】
「Hơn nữa, bánh chịu tải cũng có những cách phân loại chi tiết hơn. Bánh chịu tải không động lực đặt ở phía trước cụm bánh chủ động được gọi là bánh dẫn hướng trước. Bánh chịu tải đặt ở phía sau cụm bánh chủ động được gọi là bánh chịu tải sau. Tùy vào đơn vị vận hành đường sắt mà bánh chịu tải sau này cũng thường được gọi đơn giản là bánh chịu tải」

【Hachiroku】
「Cách bố trí số lượng bánh dẫn hướng trước, bánh chủ động và bánh chịu tải sau được gọi là cách bố trí trục bánh xe ạ. Sơ đồ trục của dòng 8620 là 2-6-0. Có một cặp bánh dẫn hướng trước và ba cặp bánh chủ động tương đương với chữ C trong ABC, do đó sơ đồ trục này còn được gọi là 1C ạ」''',

    'tw_tips_惰行.txt': '''Chạy quán tính (Dako)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Trạng thái đầu máy hơi nước chạy nhờ hơi nước được dẫn vào làm quay bánh xe chủ động được gọi là chạy kéo tải (rikko) ạ」

【Reina】
「Đối với toa xe tự hành hay tàu điện cũng vậy ạ, trạng thái bánh xe quay dưới lực truyền từ động cơ hay mô-tơ chính là chạy kéo tải (rikko) đó ạ. Và khi không có lực truyền động nào tác động lên bánh xe, tàu chỉ chạy bằng đà quán tính sẵn có từ trước thì gọi là chạy quán tính (dako) —— tức chạy trôi tự do ạ」

【Paulette】
「Vì lực ma sát giữa đường ray và bánh xe là cực kỳ nhỏ, nên thông thường không cần thiết phải duy trì chạy kéo tải liên tục làm gì cả. Các phương tiện đường sắt nói chung thường chạy quán tính với tần suất khá lớn đấy」''',

    'tw_tips_指差喚呼.txt': '''Chỉ tay hô xác nhận (Shisa kanko)
*解説
;---------------------------------------------------------------
【Paulette】
「Khi thực hiện hô xác nhận, hành động chỉ tay vào mục tiêu đang kiểm tra —— ví dụ như chỉ tay vào đèn tín hiệu xuất phát khi đang kiểm tra nó —— đồng thời hô lớn xác nhận là điều được khuyến khích. Sự kết hợp giữa chỉ tay và hô lớn này được gọi là chỉ tay hô xác nhận (shisa kanko) đấy」

【Reina】
「Về việc hô xác nhận, các bạn hãy xem thêm ở mục hô xác nhận nhé ạ」''',

    'tw_tips_掛け紙.txt': '''Giấy gói cơm hộp (Kakegami)
*解説
;---------------------------------------------------------------
【Paulette】
「Đó chính là tờ giấy bọc bên ngoài hộp cơm bento ga tàu đấy. Cách gọi cổ xưa là kakegami cho đến nay vẫn là tên gọi phổ biến trong ngành đường sắt. Việc sưu tầm các tờ giấy gói kakegami làm kỷ niệm cho những chuyến du lịch bằng tàu hỏa có vẻ là một sở thích khá phổ biến đấy」''',

    'tw_tips_接続.txt': '''Kết nối chuyển tàu (Setsuzoku)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Tại một nhà ga quy định, việc thiết kế thời gian dừng đỗ trùng nhau giữa một đoàn tàu này và một đoàn tàu khác để hành khách có thể trung chuyển đổi chuyến qua lại trong khoảng thời gian dừng đỗ đó được gọi là kết nối chuyển tàu (setsuzoku) ạ」

【Paulette】
「Nó thường được sử dụng trong các câu thông báo kiểu như: 'Đoàn tàu này sẽ kết nối đổi chuyến với tàu số hiệu 8620 khởi hành lúc 17 giờ 00 phút đi Yui tại ga Ohito' đấy」''',

    'tw_tips_撮り鉄.txt': '''Người thích chụp ảnh tàu (Tori-tetsu)
*解説
;---------------------------------------------------------------
【Paulette】
「Những người hâm mộ đường sắt có mục đích chính là chụp ảnh các toa xe lửa và các nội dung liên quan đến đường sắt được gọi là Tori-tetsu đấy」

【Hachiroku】
「Vào thời Đường sắt Hoàng gia, từ buồng lái nhìn ra, chúng tôi có thể bắt gặp bóng dáng họ ở khắp mọi nơi. Gần đây, xung quanh Đường sắt Ohito chúng tôi cũng bắt đầu nhìn thấy họ xuất hiện lác đác rồi ạ」''',

    'tw_tips_改軌.txt': '''Cải khổ đường ray (Kaiki)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Khoảng cách giữa hai thanh ray của đường sắt được gọi là khổ đường ray hoặc gauge ạ. Cải khổ đường ray là việc cải tạo điều chỉnh lại khổ đường ray của tuyến đường sắt sẵn có. Ví dụ như việc thay đổi từ khổ 900mm sang khổ 1067mm ạ」''',

    'tw_tips_施工基面高.txt': '''Cao độ mặt nền đường sắt
*解説
;---------------------------------------------------------------
【Hachiroku】
「Mặt nền thi công trong ngành đường sắt có nghĩa là bề mặt đất tiếp xúc trực tiếp bên dưới đường ray ạ. Cao độ mặt nền đường sắt chính là thông số hiển thị mặt nền thi công đó nằm ở độ cao bao nhiêu mét so với mực nước biển ạ」''',

    'tw_tips_明智.txt': '''Thời kỳ Meiji (Minh Trị)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Thời kỳ ngay trước thời Taisho chính là thời kỳ Meiji (Minh Trị) kéo dài hơn 44 năm dưới sự trị vì của Thiên hoàng Meiji. Tính theo dương lịch, thời kỳ này bắt đầu từ tháng 1 năm 1868 đến tháng 7 năm 1912 ạ」

【Olivy】
「Đó chính là thời kỳ đường sắt phát triển bùng nổ trên toàn thế giới luôn đó! Olivy và đầu máy số 9 xuất xưởng vào tháng 6 năm 1912, tính theo cách gọi ở Hinamoto thì vừa kịp bắt lấy phần đuôi của thời đại đầu máy hơi nước Meiji đấy!」''',

    'tw_tips_架線.txt': '''Đường dây tiếp điện trên cao (Gasen)
*解説
;---------------------------------------------------------------
【Paulette】
「Để cung cấp lượng điện cần thiết cho tàu điện hoạt động, đường dây điện được chăng trên không trung phía trên đường ray chính là đường dây tiếp điện trên cao (gasen). Nghe nói tên gọi chính thức của nó là 'Đường dây điện trên cao', nghe có vẻ ngầu hơn nhiều đúng không nào?」''',

    'tw_tips_検修庫.txt': '''Xưởng bảo dưỡng (Kenshuko)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Vì là nhà kho dùng để kiểm tra và sửa chữa nên gọi là xưởng bảo dưỡng (kenshuko) ạ. Đúng như tên gọi, đây là tòa nhà phục vụ công tác tu sửa và bảo dưỡng tự thân của đơn vị vận hành đường sắt ạ」

【Paulette】
「Tại Đường sắt Ohito, xưởng đầu máy bằng đá chính là xưởng bảo dưỡng. Ngoài ra, tụi mình vẫn đang duy trì vận hành một xưởng bảo dưỡng nhỏ hơn vốn được sử dụng trước khi xây dựng xưởng đầu máy bằng đá đấy」

【Reina】
「Kiha 07S của Reina thường nằm ở xưởng bảo dưỡng nhỏ hơn đó đó ạ!」''',

    'tw_tips_検札鋏.txt': '''Kìm soát vé (Kensatsukyo)
*解説
;---------------------------------------------------------------
【Paulette】
「Việc trưởng tàu kiểm tra xem vé tàu —— tức vé hành khách —— của hành khách trên tàu có còn hiệu lực hay không được gọi là soát vé. Và kìm soát vé (kensatsukyo) chính là chiếc kìm dùng để đóng dấu chứng nhận 'đã soát vé xong' lên tấm vé đó đấy」

【Hachiroku】
「Dù gọi là kìm bấm, nhưng thực tế có rất nhiều hình thức khác nhau tùy thuộc vào đơn vị vận hành đường sắt, chẳng hạn như kìm bấm tạo lỗ tròn nhỏ, dụng cụ đóng dấu chìm, hoặc thậm chí là con dấu mực ạ. Việc soát vé này cũng là một trải nghiệm khá thú vị đó ạ」''',

    'tw_tips_機関助士.txt': '''Phụ lái tàu (Kikan joshi)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Phụ lái tàu (kikan joshi) là người chịu trách nhiệm xúc than vào lò đầu máy hơi nước, liên tục quản lý mực nước lò hơi, áp suất hơi nước và thông gió. Có thể nói nhiệm vụ lớn nhất của họ là duy trì quá trình cháy và nguồn cấp hơi nước liên tục không bị gián đoạn ạ」

【Soutetsu】
「Đúng như tên gọi phụ tá, một phụ lái tàu lành nghề sẽ giúp công việc của người lái chính —— tức các thao tác điều khiển lái tàu —— trở nên vô cùng mượt mà và trôi chảy. Họ hoàn toàn không đơn thuần là trợ lý hỗ trợ người lái chính, mà là những người song hành, gánh vác vai trò vô cùng quan trọng giúp vận hành đầu máy」'''
}

out_dir = r"E:\まいてつ Last Run!!\vn_patch"
for name, content in translations.items():
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote {name}")
