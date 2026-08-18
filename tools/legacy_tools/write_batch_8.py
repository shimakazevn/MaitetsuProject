import os

translations = {
    'tw_tips_種車.txt': '''Toa xe nguyên bản (Tanesha)
*解説
;---------------------------------------------------------------
【Hibiki】
「Nếu mà đóng mới một đoàn tàu thì sẽ tốn cực kỳ nhiều tiền bạc và thời gian luôn ấy, cho nên người ta cũng thường hay tiến hành cải tạo nâng cấp những toa xe hiện có cho phù hợp với mục đích sử dụng mới đấy」

【Hachiroku】
「Và toa xe dùng làm phôi gốc để thực hiện công tác cải tạo đó chính là toa xe nguyên bản (tanesha) ạ」''',

    'tw_tips_絶気.txt': '''Cắt hơi (Zekki)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Cắt hơi (zekki) là trạng thái không dẫn hơi nước vào xi-lanh nữa. Nói cách khác là không cung cấp thêm lực đẩy mới cho bánh xe chủ động. Việc vận hành tàu trong trạng thái cắt hơi này được gọi là chạy cắt hơi —— tức là tàu chạy chỉ bằng đà quán tính sẵn có từ trước đến nay, hay còn gọi là chạy quán tính (dako) ạ」

【Olivy】
「Ngược lại, việc dẫn hơi nước vào xi-lanh để dùng lực đó làm quay bánh xe chủ động giúp tàu chạy thì gọi là chạy kéo tải (rikko) đó!」

【Hachiroku】
「Để biết thêm chi tiết, xin mời tham khảo thêm các mục chạy kéo tải và chạy quán tính ạ」''',

    'tw_tips_絶気運転.txt': '''Chạy cắt hơi (Zekki unten)
*解説
;---------------------------------------------------------------
【Hachiroku】
「シリンダー、ピストンに蒸気を流さず、絶気したままに運転をすることを、絶気運転と申します。[:蒸気機関車:]以外の鉄道車両では、同じく動力を与えず慣性の力だけで走行することを、[惰性]走行――[:惰行][惰行][:]とも呼んでおります」''',

    'tw_tips_緑旗.txt': '''Cờ xanh lá (Ryokki)
*解説
;---------------------------------------------------------------
【Paulette】
「Đối với đoàn tàu không có trưởng tàu đi cùng, ga trưởng cần trực tiếp phát tín hiệu báo cho người lái tàu biết rằng: 'Đoàn tàu có thể xuất phát được rồi'. Và lá cờ được vẫy để gửi tín hiệu đó chính là cờ xanh lá đấy」''',

    'tw_tips_編成.txt': '''Ghép đoàn tàu (Hensei)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Ghép đoàn tàu (hensei) là thuật ngữ chỉ việc kết nối các toa xe đường sắt thành một đoàn tàu hoàn chỉnh ạ. Một đoàn tàu được liên kết và thiết lập từ sáu toa xe được gọi là đoàn tàu ghép 6 toa. Còn trường hợp đoàn tàu chỉ bao gồm một toa xe độc nhất thì được gọi là đoàn tàu ghép 1 toa ạ」

【Paulette】
「Nói thêm một chút, đoàn tàu được định nghĩa là phương tiện đường sắt đang di chuyển trên đường ray theo đúng biểu đồ chạy tàu. Những toa xe dù được liên kết nối với nhau nhưng không di chuyển thì không được coi là đoàn tàu, ngược lại dù chỉ là một toa xe đơn lẻ nhưng nếu chạy trên ray theo đúng biểu đồ chạy tàu thì vẫn được coi là một đoàn tàu đấy」

【Hachiroku】
「Để biết thêm chi tiết, xin hãy xem thêm ở mục đoàn tàu ạ」''',

    'tw_tips_縦断面図.txt': '''Bản đồ mặt cắt dọc (Judammenzu)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Bản đồ mặt cắt dọc (judammenzu) is bản vẽ mặt cắt được phác họa theo giả định cắt dọc địa hình nơi tuyến đường sắt được trải dài theo chiều thẳng đứng ạ. Để biết thêm chi tiết, xin vui lòng xem thêm ở mục bản đồ độ dốc ạ」''',

    'tw_tips_缶掴み棒.txt': '''Tay vịn lò hơi (Kantsukamibou)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Thanh tay vịn dài chạy dọc hông thân lò hơi song song với đường ray để làm điểm vịn tay được gọi là tay vịn lò hơi (kantsukamibou) ạ. Khi đi lại trên bệ bước chân hành lang, việc nắm chắc tay vịn lò hơi là vô cùng quan trọng để đảm bảo an toàn ạ」''',

    'tw_tips_翼端.txt': '''Đầu cánh (Yokutan)
*解説
;---------------------------------------------------------------
【Navi】
「Đầu cánh (yokutan) là hai đầu ngoài cùng —— đầu bên phải và đầu bên trái của cánh chính ạ」''',

    'tw_tips_脱線転覆.txt': '''Trật bánh lật tàu (Dassen tempuku)
*解説
;---------------------------------------------------------------
【Reina】
「Việc bánh xe của phương tiện đường sắt văng ra khỏi đường ray thì gọi là trật bánh đó ạ. Còn lật tàu là việc toa xe bị đổ nhào chổng vó lên luôn. Sự cố trật bánh rồi dẫn đến lật nhào cả toa xe thì được gọi là trật bánh lật tàu đó ạ!」''',

    'tw_tips_自弁.txt': '''Van hãm tự động (Jiben)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Jiben là van hãm tự động. Nói một cách chính xác hơn thì đây là van hãm khí nén tự động, thiết bị dùng để điều khiển phanh có thể tác động đồng thời lên tất cả các toa xe được liên kết nối thành một đoàn tàu ạ」

【Soutetsu】
「Giả sử chúng ta có một đoàn tàu gồm: đầu máy - toa khách - toa khách. Nếu thao tác bằng van hãm đơn, tức van hãm độc lập, lực phanh hãm chỉ có tác dụng đối với riêng đầu máy xe lửa mà thôi. Nhưng nếu dùng van hãm tự động, lực phanh hãm của cả hai toa hành khách đi kèm phía sau cũng sẽ hoạt động đồng thời」''',

    'tw_tips_舟運.txt': '''Vận tải đường thủy (Shuun)
*解説
;---------------------------------------------------------------
【Fukami】
「Vận tải đường thủy (shuun) là việc sử dụng thuyền bè để chuyên chở hành khách hoặc hàng hóa... ạ」

【Nagi】
「Vậy thì hoạt động xuôi dòng sông Kuma cũng là vận tải đường thủy đúng không chị? Chúng ta chở hành khách đi thuyền xuôi dòng từ bến đi đến bến đỗ mà!」

【Fukami】
「A, nghe em nói thì đúng là thế thật đấy, Nagi. Hóa ra chúng ta không chỉ làm trong ngành du lịch, mà còn là những nhà vận tải đường thủy nữa cơ đấy」''',

    'tw_tips_艤装.txt': '''Trang thiết bị nội ngoại thất (Giso)
*解説
;---------------------------------------------------------------
【Paulette】
「Các phụ kiện đi kèm trên thân của phương tiện đường sắt ngoài bản thân khung sườn vỏ xe —— ví dụ như ghế ngồi, vải bọc đệm ghế, hệ thống dây điện, kính cửa sổ, cũng như khu vực buồng lái và các thiết bị điều khiển lái, tất cả được gọi chung là trang thiết bị nội ngoại thất (giso) đấy」''',

    'tw_tips_蒸気排水.txt': '''Xả nước ngưng hơi nước
*解説
;---------------------------------------------------------------
【Hachiroku】
「Hơi nước sử dụng để vận hành động cơ hơi nước một khi nguội đi tất nhiên sẽ ngưng tụ lại thành nước ạ. Ở một số đầu máy hơi nước có trang bị thiết bị ngưng tụ hơi nước, lượng nước đó sẽ được tuần hoàn tái sử dụng, nhưng ở dòng 8620, chúng tôi xả bỏ lượng nước này trực tiếp ra ngoài sau khi sử dụng ạ」

【Soutetsu】
「Lượng hơi nước nguội đi ngưng tụ lại thành nước đó được gọi là nước ngưng, và lượng nước ngưng được xả thải ra đó chính là xả nước ngưng hơi nước. Thật ra nghĩa của nó hoàn toàn đúng như mặt chữ thôi」''',

    'tw_tips_蒸気機関車.txt': '''Đầu máy hơi nước (Joki kikansha)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Đầu máy xe lửa (kikansha) là tên gọi chung của phương tiện đường sắt sở hữu nguồn động lực nằm bên trong nó, chuyên dùng để kéo các toa hàng hoặc toa khách ạ. Trong đó, loại đầu máy vận hành bằng động cơ hơi nước chính là đầu máy hơi nước ạ. Nó còn được viết tắt là SL —— steam locomotive ạ」''',

    'tw_tips_補機.txt': '''Đầu máy phụ (Hoki)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Các phương tiện đường sắt thường rất yếu khi leo dốc cao dốc đứng ạ. Vì thế, khi đi qua những con dốc cao mà chỉ một đầu máy đơn độc không thể vượt qua nổi, bên cạnh đầu máy kéo chính thức —— tức đầu máy chính —— người ta thường nối thêm đầu máy khác để hỗ trợ cho đầu máy chính. Đầu máy được nối thêm với mục đích hỗ trợ này gọi là đầu máy phụ (hoki), là từ viết tắt của đầu máy hỗ trợ ạ」

【Reina】
「Tại Đường sắt Ohito, toa xe tự hành Kiha 07S của Reina cũng thường xuyên tham gia hỗ trợ làm đầu máy phụ cho xe 8620 của chị Hachiroku đó ạ. Lúc đó, dù là xe tự hành hỗ trợ nhưng tụi mình vẫn gọi chung là đầu máy phụ chứ không đổi tên gọi khác đâu ạ!」'''
}

out_dir = r"E:\まいてつ Last Run!!\vn_patch"
for name, content in translations.items():
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote {name}")
