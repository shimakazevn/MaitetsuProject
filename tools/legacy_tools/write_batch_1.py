import os

translations = {
    'tw_tips_9600.txt': '''9600 (Kyuroku)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Đầu máy hơi nước chở hàng nội địa đầu tiên có thể gọi là chị em trực tiếp của dòng 8620 chúng tôi chính là dòng 9600 (Kyuroku).
Chúng là những người em gái làm việc chăm chỉ, bền bỉ và là niềm tự hào của tôi」

【Paulette】
「Bị dòng D51 'ngay cả trẻ con đang khóc cũng phải nín' đuổi kịp, chúng đã bị đẩy sang các tuyến nhánh trên khắp Nhật Bản —— nhưng cũng chính vì thế mà chúng là những đầu máy hơi nước tiếp tục hoạt động cho đến những ngày cuối cùng của Đường sắt Hoàng gia nhỉ」

【Hachiroku】
「Đúng như vậy ạ. Nói một cách rộng rãi thì tất cả các đầu máy hơi nước nội địa đều là em gái của tôi —— nhưng trong số đó, đối tượng mà tôi yêu quý và tự hào nhất không ai khác ngoài dòng 9600」''',

    'tw_tips_DL.txt': '''DL
*解説
;---------------------------------------------------------------
【Reina】
「DL là tên viết tắt của đầu máy diesel đó ạ.
Lấy các chữ cái đầu của cụm từ Diesel Locomotive thì ta được DL nha」''',

    'tw_tips_EL.txt': '''EL
*解説
;---------------------------------------------------------------
【Niiroku】
「EL là tên viết tắt của đầu máy điện.
Lấy các chữ cái đầu của cụm từ Electric Locomotive thì chính là EL」''',

    'tw_tips_HSMK.txt': '''HSMK
*解説
;---------------------------------------------------------------
【Paulette】
「HSMK là ký hiệu phương tiện mà Đường sắt Hisatsu Mikan đặt cho các toa xe tự hành của họ. Nghe nói là ghép các chữ cái đầu của cụm từ HiSatsu Mikan Kidousha để tạo thành HSMK đấy」''',

    'tw_tips_Nゲージ.txt': '''N-gauge
*解説
;---------------------------------------------------------------
【Paulette】
「N-gauge là mô hình đường sắt có thể chạy bằng điện」

【Soutetsu】
「Gauge có nghĩa là khổ đường —— tức là chiều rộng của đường ray đúng không?
Vậy thì chữ N trong N-gauge rốt cuộc là...」

【Paulette】
「Nine ạ. Vì khoảng cách giữa hai thanh ray là 9mm nên được gọi là Nine Gauge —— tức N-gauge đó ạ」''',

    'tw_tips_お召し列車.txt': '''Tàu ngự dụng (Omeshi ressha)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Đoàn tàu được triệu dụng làm phương tiện di chuyển cho Thiên hoàng được gọi là tàu ngự dụng.
Thông thường, những đoàn tàu được triệu dụng này đều là những phương tiện tốt nhất từ các khu đầu máy tốt nhất, do những người lái tàu xuất sắc nhất điều khiển ạ」''',

    'tw_tips_もろみ.txt': '''Cơm rượu (Moromi)
*解説
;---------------------------------------------------------------
【Mayami】
「Chúng ta cấy nấm men Koji vào gạo nấu rượu để tạo thành bánh men. Rồi thêm men và nước vào bánh men cho lên men, sản phẩm tạo ra chính là cơm rượu Moromi đó em. Chưng cất cơm rượu Moromi sẽ tạo ra rượu nguyên chất, nên tên gọi khác của cơm rượu lên men lần một là mẹ của rượu, hay còn gọi là men cái rượu đó」''',

    'tw_tips_イロ.txt': '''Iro
*解説
;---------------------------------------------------------------
【Hachiroku】
「'I' biểu thị toa hành khách hạng nhất. 'Ro' biểu thị toa hành khách hạng hai.
Do đó, 'Iro' là ký hiệu phân loại biểu thị cho toa xe kết hợp cả hạng nhất và hạng hai ạ」''',

    'tw_tips_エアクラ.txt': '''Aerocraft
*解説
;---------------------------------------------------------------
【Kisaki】
「Động cơ do công ty Aero-Craftech phát triển, sử dụng năng lượng từ ánh sáng mặt trời và địa từ để tạo ra động lực, thường được gọi là động cơ Aerocraft.
Vì thế, các phương tiện sử dụng động cơ Aerocraft nói chung đều được gọi là Aerocraft đó」''',

    'tw_tips_カマ.txt': '''Kama (Lò hơi)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Kama có nghĩa là lò hơi. Nói hẹp thì nó chỉ toàn bộ phần từ buồng đốt đến nồi hơi, nói rộng thì nó là từ viết tắt —— đúng hơn là tên thân mật của bản thân đầu máy hơi nước. Khi đầu máy hơi nước hoạt động không tốt, người ta thường dùng cách nói như 'Tâm trạng lò hơi không được tốt' ạ」''',

    'tw_tips_キハ07s.txt': '''Kiha 07S
*解説
;---------------------------------------------------------------
【Reina】
「Kiha 07S của Reina thực chất ban đầu là Kiha 07-2 của Đường sắt Katakami, là chiếc ở giữa trong số ba toa xe tự hành cùng loại với mẫu Kiha 07 của Đường sắt Hoàng gia do Đường sắt mỏ Katakami tự đặt hàng riêng đó ạ」

【Paulette】
「Khi Đường sắt mỏ Katakami ngừng hoạt động, mình đã tha thiết yêu cầu đón em ấy về Đường sắt Ohito. Kể từ khi Densha Hime giúp đỡ chúng mình lúc đó, mối quan hệ hữu nghị giữa chúng mình vẫn luôn duy trì tốt đẹp」

【Reina】
「Mặc dù chỉ là chị em họ, nhưng trong số các chị em Kiha 07 của Đường sắt Hoàng gia, có những chiếc được dùng để thử nghiệm động cơ tuabin khí, có chiếc trở thành xe kiểm tra điện, có chiếc trở thành xe cứu hộ, và họ đã tỏa sáng trên nhiều sân khấu khác nhau đó ạ. Thực ra mẫu Kiha 07 cũng là một mẫu xe khá danh tiếng đấy ạ!」''',

    'tw_tips_ギャレー.txt': '''Galley (Bếp trên tàu)
*解説
;---------------------------------------------------------------
【Hibiki】
「Galley là một từ tiếng Anh, ban đầu dùng để chỉ thuyền galley —— loại thuyền buồm mà chúng ta thường thấy trong phim ảnh, tuy có buồm nhưng vẫn cần rất nhiều người chèo ấy. Từ đó, nó dần chuyển sang mang nghĩa là 'bếp trên các phương tiện giao thông' đấy」

【Hachiroku】
「Ở Nhật Bản cũng tương tự như vậy, galley dùng để chỉ các thiết bị nhà bếp trên toa ăn hoặc tàu thủy. Đó là nơi chế biến các món ăn ạ」''',

    'tw_tips_クハ26.txt': '''Kuha 26
*解説
;---------------------------------------------------------------
【Niiroku】
「Là đoàn tàu tốc hành chạy điện tiên tiến nhất vào thời kỳ cuối của Đường sắt Hoàng gia, đáng lẽ ra đã trở thành đoàn tàu điện thương mại đầu tiên hoạt động ở Kyushu. Đó chính là Kuha 26. Không hơn không kém. Tất cả giờ chỉ là chuyện quá khứ mà thôi」''',

    'tw_tips_クロスヘッド.txt': '''Đầu chữ thập (Crosshead)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Để quay bánh xe chủ động, chuyển động tịnh tiến lên xuống của piston nhờ sức đẩy của hơi nước phải được biến đổi thành chuyển động quay của bánh xe chủ động.
Bộ phận đảm nhận vai trò chuyển đổi đó chính là đầu chữ thập ạ」''',

    'tw_tips_グランビー鉱車.txt': '''Toa chở quặng Granby
*解説
;---------------------------------------------------------------
【Reina】
「Toa chở quặng Granby là một loại toa chở hàng chuyên dụng dùng để vận chuyển quặng đó ạ. Nhờ sử dụng đường ray dẫn hướng, nó có thể tự nghiêng thùng xe để quặng tự động lăn ra ngoài, là một loại toa chở quặng vô cùng tiện lợi luôn đó ạ」'''
}

out_dir = r"E:\まいてつ Last Run!!\vn_patch"
for name, content in translations.items():
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote {name}")
