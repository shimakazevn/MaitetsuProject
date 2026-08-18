import os

translations = {
    'tw_tips_機関士.txt': '''Người lái tàu (Kikanshi)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Người lái tàu (kikanshi) là người chịu trách nhiệm cao nhất tại hiện trường trong việc điều khiển và vận hành đầu máy xe lửa. Đó là người thực hiện công việc lái và chỉ huy hoạt động của đầu máy xe lửa ạ」

【Soutetsu】
「Đối với đầu máy hơi nước, việc xử lý động cơ hơi nước và thao tác lái tàu gần như liên kết trực tiếp với nhau. Tăng công suất động cơ để tàu chạy, khi muốn dừng thì giảm công suất và kết hợp thao tác gài phanh —— đó là nội dung công việc khái quát của người lái chính」

【Hachiroku】
「Ngoài ra, trong các trường hợp khẩn cấp, người lái chính cũng có thể thay thế thực hiện công việc của phụ lái tàu. Railord xét cho cùng cũng chỉ đóng vai trò hỗ trợ người lái tàu mà thôi. Thực thể thực sự là bộ não của đầu máy xe lửa vĩnh viễn vẫn luôn là người lái tàu ạ」''',

    'tw_tips_機関推力.txt': '''Lực đẩy động cơ (Kikan suiryoku)
*解説
;---------------------------------------------------------------
【Navi】
「Lực đẩy động cơ (kikan suiryoku) là lực đẩy phương tiện về phía trước được tạo ra bởi động cơ Aero-Craftech. Đối với các phương tiện sử dụng động cơ Aerocraft, lực do động cơ tạo ra được quy định biểu thị bằng lực đẩy động cơ chứ không phải bằng mã lực đâu ạ」''',

    'tw_tips_歩き板.txt': '''Bệ bước chân (Aruki-ita)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Bệ bước chân (aruki-ita) là tấm bệ bước dùng để di chuyển ở phần bên hông hoặc phần phía trên nóc của toa xe đường sắt ạ. Nó còn được gọi là tấm ván bước hoặc thanh bệ bước hành lang ạ」''',

    'tw_tips_汽笛.txt': '''Còi hơi nước (Kiteki)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Còi phát ra âm thanh bằng hơi nước chính là còi hơi nước (kiteki) ạ. Nó được kéo còi để làm tín hiệu xuất phát, tín hiệu cảnh báo, chào người hâm mộ đường sắt, hoặc dùng làm tín hiệu để phối hợp thời điểm khi đầu máy chạy ghép đôi ạ. Âm sắc của còi hơi nước có sự khác biệt rất lớn tùy thuộc vào từng đầu máy đó ạ」''',

    'tw_tips_減圧.txt': '''Giảm áp (Gen-atsu)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Giảm áp (gen-atsu) là việc làm giảm áp suất của khí nén bên trong ống phanh ạ. Nói cách khác, điều này sẽ làm gia tăng lực phanh. Khi mức độ giảm tốc không đủ, việc tiếp tục giảm thêm áp suất để tăng thêm lực phanh được gọi là giảm áp bổ sung ạ」''',

    'tw_tips_溶栓.txt': '''Nút chảy an toàn (Tokesen)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Đầu máy hơi nước vận hành nhờ vào than, lửa, khí ga cháy do lửa tạo ra, cùng với hơi nước sinh ra từ việc đun sôi nước ạ. Do đó, nó luôn đi kèm với nguy cơ cháy bất thường hoặc phát nổ lò hơi ạ」

【Soutetsu】
「Vài một trong những giải pháp để phòng ngừa nguy hiểm đó chính là nút chảy an toàn (tokesen). Nó được làm từ kim loại dễ nóng chảy như đồng hoặc hợp kim của đồng và thiếc, dùng để bịt kín lỗ khoét trên trần của buồng đốt」

【Hachiroku】
「Bình thường, nút chảy an toàn luôn nằm chìm hoàn toàn trong nước ở phần trên của lò hơi. Tuy nhiên, khi mực nước lò hơi bị hạ thấp khiến nút chảy bị lộ ra ngoài nước, nó sẽ nhanh chóng bị nóng chảy và rơi ra. Khi đó, hơi nước từ buồng đốt sẽ tràn ra buồng lái, giúp tổ lái có thể nhận biết bất thường ngay lập tức ạ」''',

    'tw_tips_焼なまし.txt': '''Ủ mềm thép (Yakinamashi)
*解説
;---------------------------------------------------------------
【Nagi】
「Nung nóng thép lên rồi giữ cho nó nóng hổi một thời gian, sau đó cho nhiệt độ hạ xuống thật là chậm rãi chính là ủ mềm thép (yakinamashi) đó nha! Thép được ủ mềm sẽ trở nên dẻo dai hơn, dễ gõ đập tạo hình và kéo dài hơn nhiều luôn đó!」''',

    'tw_tips_煙室.txt': '''Buồng khói (Enshitsu)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Buồng khói (enshitsu)... rất khó để giải thích một cách đơn giản, nhưng nếu tóm tắt một cách dễ hiểu nhất thì nó là 'khoang thực hiện nhiệm vụ rút khí đốt ra khỏi các ống lò hơi và xả chúng ra ngoài qua ống khói' —— tôi nghĩ có thể hiểu như vậy ạ」

【Soutetsu】
「Nhờ việc xả khí thải ra khỏi ống khói mà luồng không khí trong lành mới có thể tràn vào bên trong buồng đốt đúng không?」

【Hachiroku】
「Đúng như vậy ạ. Do đó, việc dọn dẹp vệ sinh sạch sẽ buồng khói để duy trì tình trạng thông gió tốt cũng là một công đoạn vô cùng quan trọng để giúp đầu máy hơi nước hoạt động đạt hiệu suất cao ạ. Xin vui lòng xem thêm ở mục thiết bị thổi gió để đối chiếu hiểu thêm ạ」''',

    'tw_tips_煙室戸.txt': '''Cửa buồng khói (Enshitsudo)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Nằm ở phần trước nhất của đầu máy hơi nước, ngay phía dưới đèn pha đầu tàu, cánh cửa sắt dày cộp được trang trí bằng tay nắm cửa buồng khói lấp lánh sắc vàng chính là cửa buồng khói (enshitsudo) hay còn gọi là cửa buồng khói ạ. Đó là lối vào phục vụ cho việc vệ sinh làm sạch bên trong buồng khói ạ」''',

    'tw_tips_特殊軌道.txt': '''Khổ đường sắt đặc biệt (Tokushu kido)
*解説
;---------------------------------------------------------------
【Paulette】
「Khoảng cách giữa hai thanh ray —— tức khổ đường sắt, có kích thước hẹp hơn khổ tiêu chuẩn 1067mm của Nhật Bản thì được gọi là khổ đường sắt đặc biệt (tokushu kido). Loại khổ này thường xuất hiện nhiều ở các tuyến đường sắt khai thác mỏ hay đường sắt lâm nghiệp đấy」

【Hachiroku】
「Để biết thêm chi tiết, xin vui lòng xem thêm ở mục khổ đường sắt ạ」''',

    'tw_tips_現示.txt': '''Tín hiệu hiển thị (Genji)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Tín hiệu hiển thị (genji) là nội dung thông tin hiện tại mà cột tín hiệu đang biểu thị ạ. Ví dụ, đối với cột tín hiệu cánh, trạng thái cánh tín hiệu chỉ chéo xuống 45 độ biểu thị cho lệnh 'hành trình tiến lên' —— tức là đang ở chế độ tín hiệu cho phép chạy ạ」''',

    'tw_tips_甲種輸送.txt': '''Vận chuyển loại Giáp (Koshu yuso)
*解説
;---------------------------------------------------------------
【Paulette】
「Vận chuyển loại Giáp (koshu yuso) là một trong những phương pháp vận chuyển các toa xe đường sắt. Đây là phương thức vận chuyển bằng cách cho đầu máy hàng kéo toa xe cần vận chuyển lăn bánh bằng chính bánh xe của nó trên đường ray, phương thức này cực kỳ thu hút sự chú ý của những người thích chụp ảnh tàu đấy」

【Hachiroku】
「Vận chuyển loại Ất là phương pháp đặt toàn bộ toa xe cần vận chuyển lên trên một toa hàng chuyên dụng để chở đi ạ. Còn vận chuyển loại Bính là phương pháp vận chuyển toa xe bằng xe tải hoặc tàu thủy mà không sử dụng đường ray chạy tàu ạ」''',

    'tw_tips_発報.txt': '''Phát tín hiệu báo động (Happo)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Phát tín hiệu báo động (happo) là hành động truyền phát tín hiệu dừng khẩn cấp cho các đoàn tàu đang chạy xung quanh thông qua tín hiệu vô tuyến của tổ lái hoặc qua sự cộng cảm của Railord đi cùng khi đoàn tàu gặp phải sự cố khẩn cấp ạ」''',

    'tw_tips_石造機関庫.txt': '''Xưởng đầu máy bằng đá (Sekizo kikanko)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Đúng như tên gọi của nó, đây là xưởng đầu máy được xây dựng bằng vật liệu đá là chủ yếu ạ」''',

    'tw_tips_硬上鉱山鉄道.txt': '''Đường sắt mỏ Katakami
*解説
;---------------------------------------------------------------
【Reina】
「Đường sắt mỏ Katakami là nơi Reina từng làm việc đầu tiên, là tuyến đường sắt khai thác mỏ tại quê hương của Reina đó ạ」

【Paulette】
「Kiha 07S của Reina vốn ban đầu là xe số 2 Kiha 07 của Đường sắt mỏ Katakami. Nó không phải xe xuất xứ từ Đường sắt Hoàng gia, mà là chiếc Kiha 07 được chế tạo theo đơn đặt hàng riêng của Đường sắt mỏ Katakami đấy」

【Reina】
「Katakami là mỏ quặng sắt pyrit đó ạ. Vào thời kỳ hoàng kim, bản thân khu mỏ giống như một thị trấn sầm uất luôn, và Reina cùng các chị em đã vận chuyển người cùng hàng hóa để giúp đỡ cuộc sống của mọi người ở đó đó ạ!」'''
}

out_dir = r"E:\まいてつ Last Run!!\vn_patch"
for name, content in translations.items():
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote {name}")
