import os

translations = {
    'tw_tips_醸造蔵.txt': '''Nhà xưởng ủ rượu (Jozo-gura)
*解説
;---------------------------------------------------------------
【Mayami】
「Nhà xưởng ủ rượu (jozo-gura) là nơi dùng để chưng cất rượu shochu —— tức là phòng xưởng để lên men gạo nấu rượu rồi chế biến thành rượu shochu đó. Nói nôm na thì nó giống như là bụng mẹ, nơi mà rượu shochu trải qua trước khi được sinh ra vậy đó nha」''',

    'tw_tips_錘付転換機.txt': '''Cần bẻ ghi có đối trọng (Daruma)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Daruma là biệt danh đáng yêu của cần bẻ ghi có đối trọng —— tức là cần gạt dùng để chuyển hướng đường ray có gắn thêm một quả cân đối trọng ạ」

【Olivy】
「Nhưng Munakata bảo rằng không phải vì cái cần gạt đâu, mà là vì phần bệ đỡ nâng đỡ cần gạt trông tròn tròn giống búp bê Daruma nên người ta mới gọi thế đó!」

【Hachiroku】
「Hơn nữa, trong số các thiết bị có cùng chức năng chuyển hướng đường ray, loại thủ công thường được gọi là cần bẻ ghi, còn loại máy móc tự động thường được gọi là thiết bị bẻ ghi ạ. Để biết thêm chi tiết, xin vui lòng xem thêm ở mục thiết bị bẻ ghi ạ」''',

    'tw_tips_長大編成.txt': '''Đoàn tàu siêu dài (Chodai hensei)
*解説
;---------------------------------------------------------------
【Paulette】
「Đoàn tàu siêu dài (chodai hensei) đúng như tên gọi của nó, dùng để chỉ đoàn tàu có số lượng toa ghép lại rất dài. Về việc ghép từ bao nhiêu toa xe trở lên thì được coi là đoàn tàu siêu dài thì có lẽ quy định của mỗi đơn vị vận hành đường sắt sẽ khác nhau, nhưng Hiệp hội Đường sắt Tư nhân Hinamoto thì định nghĩa đó là 'đoàn tàu có số toa vượt quá 8 toa' đấy」''',

    'tw_tips_除煙板.txt': '''Tấm chắn khói (Joenban)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Ngoài thiết bị gom khói ra, còn có một số giải pháp thiết kế khác giúp ngăn ngừa khói tràn vào buồng lái hay toa hành khách ạ. Một trong số đó là tấm chắn khói (joenban), hay còn gọi bằng tên khác là deflector ạ」

【Soutetsu】
「Đó chính là hai tấm thép được lắp đặt ở phần trước thân xe đầu máy hơi nước, ốp dọc hai bên thân lò hơi để kẹp ống khói ở giữa」

【Hachiroku】
「Mặc dù có cấu tạo vô cùng đơn giản, nhưng thiết bị này lại mang lại hiệu quả to lớn và là một thiết kế hết sức ưu việt đó ạ」''',

    'tw_tips_階段.txt': '''Nhả phanh từng nấc (Kaidan)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Kaidan ở đây nghĩa là nhả phanh từng nấc ạ. Đây là một trong những kỹ thuật điều khiển phanh hãm. Nói một cách đơn giản nhất, đó là phương pháp xả nhả dần dần lực phanh vốn được gài mạnh từ trước sao cho phù hợp với tốc độ giảm tốc thực tế của tàu ạ」''',

    'tw_tips_集煙装置.txt': '''Thiết bị gom khói (Shuen sochi)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Khói của đầu máy hơi nước sẽ trở nên cực kỳ nguy hiểm khi đi vào trong hầm đường sắt ạ. Bởi vì nếu khói tràn vào tích tụ bên trong buồng lái, người lái tàu và phụ lái tàu có nguy cơ bị ngạt thở, không thể tiến hành các thao tác điều khiển bình thường được nữa ạ」

【Soutetsu】
「Ngay cả khi ở ngoài hầm, cũng từng có những trường hợp tàn lửa lẫn trong khói than bay ra gây hỏa hoạn dọc đường ray đấy nhỉ」

【Hachiroku】
「Dạ đúng vậy ạ. Do đó, người ta đã phát triển một thiết bị dùng để gom khói và định hướng luồng khói xả —— bằng cách thiết kế một cửa xả phía sau có nắp đậy phía trên ống khói, khi cần thiết sẽ đóng nắp lại để chỉ cho khói thoát ra phía sau. Thực thể đó chính là thiết bị gom khói (shuen sochi) ạ」''',

    'tw_tips_電車.txt': '''Tàu điện (Densha)
*解説
;---------------------------------------------------------------
【Niroku】
「Tàu điện thông thường là loại phương tiện đường sắt vận hành theo dạng một đoàn tàu ghép gồm nhiều toa xe. Bằng cách thu nhận nguồn điện cấp từ đường dây tiếp điện trên cao —— tức là lấy điện, động cơ của các toa động lực trong đoàn tàu sẽ quay, sử dụng lực đó để kéo toàn bộ đoàn tàu hoạt động」

【Denshahime】
「Tàu điện nội đô —— tức xe điện mặt đất thì cũng có nhiều trường hợp chỉ chạy dạng đơn toa. Tuy nhiên, ở các khu vực trung tâm đô thị thời Đường sắt Hoàng gia cũ, vẫn có những đoàn tàu điện siêu dài chạy ghép trên 8 toa hoạt động. Trong đoàn tàu như vậy sẽ có nhiều toa động lực —— tức là nguồn động lực được phân bổ rải rác khắp đoàn tàu, do đó hình thức vận hành của tàu điện được gọi là phương thức động lực phân tán đó」

【Niroku】
「Ngược lại, phương thức chỉ sử dụng một vài phương tiện động lực rất ít như đầu máy để kéo các toa hành khách hoặc toa chở hàng đi sau thì gọi là phương thức động lực tập trung. Cả hai phương thức này đều có những ưu điểm và nhược điểm riêng biệt」''',

    'tw_tips_駅名標.txt': '''Biển hiệu nhà ga (Ekimeihyou)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Các biển hiệu, bảng hiệu được lắp đặt tại nhà ga đường sắt nhằm thể hiện tên của nhà ga đó được gọi chung là biển hiệu nhà ga (ekimeihyou) ạ」

【Paulette】
「Dù là tấm bảng lớn hiển thị tên ga trước và ga sau, hay bảng dọc thanh mảnh gắn trên cột chỉ có tên ga, hoặc tấm bảng khổng lồ trang trí uy nghi tại lối vào nhà ga, tất cả đều được gọi chung là biển hiệu nhà ga hết đấy」''',

    'tw_tips_駐機.txt': '''Đỗ tàu bay (Chuki)
*解説
;---------------------------------------------------------------
【Navi】
「Đỗ tàu bay (chuki) nghĩa là việc đỗ giữ máy bay cố định tại một vị trí quy định tùy ý nào đó ạ」''',

    'tw_tips_麹.txt': '''Men kōji (Kouji)
*解説
;---------------------------------------------------------------
【Mayami】
`Men kōji (kouji) là chất được tạo ra từ gạo nấu rượu ở ngay bước đầu tiên của quá trình sản xuất rượu shochu, đây là nguồn gốc cốt lõi của rượu shochu đó nha. Trộn bào tử men kōji vào gạo đã hấp chín, đảo đều và kiểm soát nhiệt độ cẩn thận —— men kōji tạo ra như vậy sẽ trở thành cơm rượu lên men, rồi sau khi chưng cất sẽ biến thành rượu shochu thơm ngon tuyệt hảo đó`''',

    'tw_tips_５号機関車.txt': '''Đầu máy số 5 (Gogo kikansha)
*解説
;---------------------------------------------------------------
【Paulette】
「À —— về chiếc đầu máy số 5 của Đường sắt Tobu ấy —— nó không phải dòng 6200 của Đường sắt Hoàng gia cũ mà thực chất là dòng 5500 cũ đấy! Em đã hoàn toàn nhầm lẫn mất rồi, thật lòng xin lỗi mọi người nhiều lắm! Dòng 5500 cũng được chế tạo bởi hãng Beyer, Peacock & Co. nữa」

【Hachiroku】
「Chà —— đầu máy hơi nước dòng 5500 này chỉ có kích thước khác biệt so với dòng 6200 (đầu máy của chị gái tôi), còn lại thì hình dáng bên ngoài thật sự rất giống nhau đấy chứ」

【Paulette】
「Em mới chỉ được nhìn thấy chiếc đầu máy số 5 của Tobu qua ảnh chụp chứ chưa từng thấy tận mắt ngoài đời bao giờ, thế nên cứ bị nhầm lẫn suốt bấy lâu nay! Thật sự vô cùng xin lỗi mọi người ạ!!」'''
}

out_dir = r"E:\まいてつ Last Run!!\vn_patch"
for name, content in translations.items():
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote {name}")
