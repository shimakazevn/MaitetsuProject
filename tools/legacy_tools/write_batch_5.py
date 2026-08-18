import os

translations = {
    'tw_tips_動輪.txt': '''Bánh xe chủ động (Do-rin)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Đầu máy hơi nước vận hành bằng cách dẫn hơi nước tạo ra từ lò hơi vào xi-lanh, làm chuyển động piston tịnh tiến tiến lùi bên trong xi-lanh. Chuyển động tịnh tiến đó được đầu chữ thập biến đổi thành chuyển động quay, rồi lực quay đó được truyền đến các bánh xe qua thanh nối chính để giúp tàu chạy ạ」

【Soutetsu】
「Và chiếc bánh xe được làm cho quay bằng thanh nối chính theo cách đó —— tức bánh xe truyền lực chuyển động, được gọi là bánh xe chủ động chính. Các bánh xe chủ động còn lại sẽ quay nhờ lực truyền từ bánh chủ động chính qua thanh truyền」

【Hachiroku】
「Tất nhiên, bánh chủ động chính cũng nằm trong số các bánh xe chủ động ạ. Khi gọi chung các bánh xe chủ động này, chúng tôi thường gọi là cụm bánh xe chủ động ạ. Để biết thêm chi tiết, xin mời tham khảo thêm các mục thanh nối chính, xi-lanh, và đầu chữ thập ạ」''',

    'tw_tips_勾配変更点.txt': '''Điểm thay đổi độ dốc
*解説
;---------------------------------------------------------------
【Hachiroku】
「Độ dốc có nghĩa là độ nghiêng của mặt đất —— mức độ nghiêng của mặt dốc ạ. Điểm thay đổi độ dốc chính là vị trí mà độ nghiêng đó có sự thay đổi ạ」''',

    'tw_tips_勾配距離.txt': '''Chiều dài đoạn dốc
*解説
;---------------------------------------------------------------
【Hachiroku】
「Khoảng cách từ điểm thay đổi độ dốc A đến điểm thay đổi độ dốc tiếp theo B được gọi là chiều dài đoạn dốc giữa A và B ạ. Nói một cách đơn giản và dễ hiểu nhất thì nó chính là 'chiều dài của con dốc đó' ạ」''',

    'tw_tips_単弁.txt': '''Van hãm đơn (Tan-ben)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Van hãm đơn (tan-ben) là van hãm độc lập. Đây là chiếc van dùng để thực hiện hãm độc lập —— tức là chỉ gài phanh cho riêng toa xe được trang bị van hãm đơn này mà không gài phanh cho các toa xe khác được nối cùng ạ」

【Reina】
「Còn loại phanh có thể gài phanh cho tất cả các toa xe được nối cùng một lúc chính là van hãm tự động đó ạ. Về van hãm tự động, nếu xem mục van hãm tự động thì sẽ hiểu rõ hơn nhiều luôn đó ạ」''',

    'tw_tips_単線.txt': '''Đường đơn (Tansen)
*解説
;---------------------------------------------------------------
【Paulette】
「Giống như tuyến Yui của Đường sắt Ohito, tuyến đường sắt nối giữa ga này với ga kia —— tức đường chính chỉ có duy nhất một đường chạy thì được gọi là đường đơn. Bản chính có hai đường song song là đường đôi. Hai cặp đường đôi, tức là có bốn đường ray chạy song song là đường bốn. Ba cặp đường đôi, tức là có sáu đường ray chạy song song thì gọi là đường sáu hoặc ba đường đôi đấy」

【Hachiroku】
「Trên đường đơn, nếu cho tàu chạy xuôi và chạy ngược đồng thời, hoặc nếu tàu tốc hành muốn vượt qua tàu thường thì chắc chắn sẽ xảy ra va chạm. Để biết về những giải pháp ngăn ngừa tai nạn này, xin vui lòng xem thêm ở mục đường tránh tàu ạ」''',

    'tw_tips_台枠.txt': '''Khung gầm (Daiwaku)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Khung gầm (daiwaku) có thể được coi là phần thắt lưng của phương tiện đường sắt ạ. Nó nâng đỡ cả thân xe lẫn cụm bánh xe chủ động, là bộ phận nền tảng quan trọng nhất đòi hỏi độ bền và tính ổn định cao nhất của một toa xe ạ」

【Paulette】
「Đối với các phương tiện đường sắt đời sau đầu máy hơi nước, cấu trúc lắp bánh xe chủ động trực tiếp vào khung gầm đã được đổi sang sử dụng giá chuyển hướng, tuy vậy tầm quan trọng của khung gầm vẫn không hề thay đổi chút nào đâu」

【Hachiroku】
「Để biết thêm chi tiết, xin vui lòng xem thêm ở mục giá chuyển hướng ạ」''',

    'tw_tips_大戦.txt': '''Đại chiến (Taisen)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Cuộc đại chiến thế giới kéo dài từ năm Taisho 28 đến năm Taisho 34 —— năm cuối cùng của kỷ nguyên Taisho, chính là cuộc Đại chiến ạ. Hinamoto là nước bại trận trong cuộc Đại chiến đó, khiến toàn bộ đất nước rơi vào tình trạng suy kiệt nghiêm trọng ạ」

【Olivy】
「Trong thời kỳ Đại chiến, những Railord có xuất xứ từ Mỹ hay Anh như tụi mình bị ghẻ lạnh lắm luôn đó! Cứ bị gọi là Railord của phe địch này nọ! Nhưng suy cho cùng thì năng lực vận tải vẫn là thứ thiết yếu nhất, nên tụi mình vẫn được làm việc bình thường suốt thời gian đó đấy!」''',

    'tw_tips_大詔.txt': '''Thời kỳ Taisho (Đại Chiếu)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Theo dương lịch, vào ngày 30 tháng 7 năm 1912, Thiên hoàng Minh Trị băng hà, khép lại thời kỳ Minh Trị kéo dài 45 năm. Thời kỳ bắt đầu ngay sau đó chính là thời kỳ Taisho (Đại Chiếu) dưới sự trị vì của Thiên hoàng Taisho ạ」

【Soutetsu】
「Hachiroku cũng được chế tạo ra trong thời kỳ Taisho này nhỉ」

【Hachiroku】
「Hihi, nếu việc chế tạo mang ý nghĩa tương tự như sự ra đời thì đúng là vậy ạ. Vào ngày 8 tháng 3 năm Taisho thứ 3 (tức năm 1914 dương lịch), tôi đã chính thức xuất xưởng từ Bộ phận Cơ khí chế tạo Railord của Nhà máy Omiya thuộc Đường sắt Hoàng gia ạ」''',

    'tw_tips_客乗.txt': '''Nhân viên phục vụ trên tàu (Kyaku-jo)
*解説
;---------------------------------------------------------------
【Paulette】
「Nhân viên phục vụ trên cabin viết tắt lại là Kyaku-jo. Nói chung, nhân viên phục vụ trên tàu là những người làm việc trên tàu mà không có chứng chỉ trưởng tàu, chịu trách nhiệm thay thế hoặc hỗ trợ trưởng tàu, cũng như thực hiện việc bán hàng hóa trên tàu đấy」

【Hachiroku】
「Vào thời Đường sắt Hoàng gia, chúng tôi gọi riêng theo từng vị trí công việc như nhân viên bán hàng trên tàu, nhân viên phục vụ bàn... nhưng gần đây hình như tất cả đều được gọi chung là nhân viên phục vụ trên tàu rồi ạ」''',

    'tw_tips_客貨車区.txt': '''Khu toa khách toa hàng (Kyakka-shaku)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Khu toa khách toa hàng (kyakka-shaku) là khu vực dùng để lưu giữ các toa hành khách và toa hàng hóa bên trong depot xe lửa ạ. Xin vui lòng xem thêm ở phần giải thích về khu đầu máy để có thể dễ dàng hình dung và thấu hiểu hơn ạ」''',

    'tw_tips_客車.txt': '''Toa hành khách (Kyaku-sha)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Toa hành khách (kyaku-sha) là phương tiện đường sắt được trang bị cơ sở vật chất và không gian phục vụ hành khách ngồi ạ. Nghe nói thuở ban đầu ngành đường sắt ra đời là để vận chuyển hàng hóa, nên chỉ đến khi bắt đầu chuyên chở hành khách thì mới xuất hiện sự phân chia rõ rệt giữa toa chở hàng và toa hành khách ạ」''',

    'tw_tips_就業後検査.txt': '''Kiểm tra sau ca làm việc (Shugyo-go kensa)
*解説
;---------------------------------------------------------------
【Paulette】
「Trước đây tại Đường sắt Ohito, vì phương tiện duy trì hoạt động được chỉ có duy nhất một toa Kiha 07S, nên không thể thực hiện kiểm tra luân phiên định kỳ một cách đầy đủ được. Do đó, để tăng cường tối đa việc bảo trì kiểm tra, chúng mình đã thực hiện kiểm tra xe sau khi kết thúc một ngày vận hành」

【Reina】
「Đó chính là kiểm tra sau ca làm việc đó ạ. Nội dung công việc cần thực hiện thì hoàn toàn giống với buổi kiểm tra trước giờ vận hành vào buổi sáng luôn đó ạ」

【Hachiroku】
「A, bằng cách thực hiện đối chiếu kiểm tra hai lần giãn cách thời gian như vậy, dù trong điều kiện thiếu thốn nhân lực, mọi người vẫn nỗ lực để nâng cao độ chính xác của việc kiểm tra bảo dưỡng nhỉ. Thật là một sự sắp xếp tuyệt vời ạ」''',

    'tw_tips_帝鉄.txt': '''Đường sắt Hoàng gia (Teitetsu)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Teitetsu là tên viết tắt của Đường sắt sở hữu Hoàng gia Hinamoto ạ. Tuy mang tên gọi là 'sở hữu Hoàng gia', nhưng bản chất thực tế của nó chính là đường sắt quốc doanh, được duy trì, quản lý và vận hành hoàn toàn bằng tiền thuế của người dân ạ」''',

    'tw_tips_帝鉄貨物.txt': '''Vận tải hàng hóa Đường sắt Hoàng gia (Teitetsu kamotsu)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Sau khi các khoản nợ lũy kế khổng lồ của Đường sắt Hoàng gia trở thành mục tiêu chỉ trích của người dân, vì những lý do mà một Railord cấp thấp như tôi không thể thấu hiểu được, bộ phận vận tải hàng hóa đã được tách riêng khỏi Đường sắt Hoàng gia để hoạt động độc lập. Thực thể đó chính là Vận tải hàng hóa Đường sắt Hoàng gia ạ」''',

    'tw_tips_延.txt': '''Trễ (En)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Chữ 'En' ở đây nghĩa là trễ trong chậm trễ ạ. Khi thời gian đến hoặc đi thực tế tại các ga muộn hơn so với lịch trình định sẵn, thì số giây chênh lệch đó được gọi là số giây trễ ạ」'''
}

out_dir = r"E:\まいてつ Last Run!!\vn_patch"
for name, content in translations.items():
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote {name}")
