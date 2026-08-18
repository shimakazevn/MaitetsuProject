import os

translations = {
    'tw_tips_先輪.txt': '''Bánh dẫn hướng trước (Sen-rin)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Bánh xe chịu tải không động lực nằm ở phía trước các cụm bánh xe chủ động được gọi là bánh dẫn hướng trước (sen-rin) ạ. Để biết thêm chi tiết, xin vui lòng xem thêm ở mục bánh chịu tải không động lực ạ」''',

    'tw_tips_先頭車.txt': '''Toa dẫn đầu (Sento-sha)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Toa xe nằm ở phía đầu của đoàn tàu được thiết lập, hoặc tên gọi chung cho các toa xe có buồng lái hay ghế lái —— tức toa điều khiển —— được gọi là toa dẫn đầu ạ. Để biết thêm chi tiết, xin hãy xem thêm ở các mục toa điều khiển và toa giữa ạ」''',

    'tw_tips_入換.txt': '''Dồn toa (Irekae)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Hoạt động di chuyển hoặc quay đầu các toa xe đường sắt không chạy như một đoàn tàu thông thường, chủ yếu diễn ra trong phạm vi sân ga hoặc depot bằng động lực tự thân của toa xe hoặc bằng động lực của các phương tiện khác được gọi là dồn toa (irekae) ạ」

【Soutetsu】
「Tùy vào các đơn vị vận hành đường sắt mà công việc này còn được gọi là điều khiển nội bộ hay dồn dịch toa xe. Trước đây, ở gần các ga hàng hóa lớn thường có các ga dồn toa chuyên dụng được gọi là bãi dồn toa」

【Hachiroku】
「Tín hiệu sử dụng trong quá trình dồn toa là tín hiệu dồn toa. Đầu máy hoặc toa xe công trình phục vụ công tác dồn toa được gọi là đầu máy dồn toa. Để biết thêm chi tiết, xin mời tham khảo cả hai mục này ạ」''',

    'tw_tips_入換機.txt': '''Đầu máy dồn toa (Irekae-ki)
*解説
;---------------------------------------------------------------
【Olivy】
「Ví dụ như việc dồn toa có thể thực hiện trên bất kỳ phương tiện nào, nên các toa xe không tự chạy được như toa khách hay toa hàng sẽ phải nhờ phương tiện khác kéo đi đúng không nè? Phương tiện được dùng cho việc đó chính là đầu máy dồn toa đó」

【Hachiroku】
「Đầu máy chuyên dụng cho dồn toa gọi là đầu máy dồn toa. Toa xe công trình chuyên dụng cho dồn toa thì thường được gọi là xe dồn toa tự hành ạ」

【Olivy】
「Đầu máy số 9 của Olivy đã từng làm việc rất chăm chỉ với vai trò là đầu máy dồn toa ở Đường sắt Mikan đấy nhé!」''',

    'tw_tips_入鋏.txt': '''Bấm vé (Nyukyo)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Bấm vé (nyukyo) là việc dùng kìm bấm để cắt một góc trên tấm vé tàu. Đối với hành khách, đây là kỹ thuật liên quan đến đường sắt gần gũi và hào nhoáng nhất mà họ tiếp xúc ạ」

【Soutetsu】
「Hào nhoáng... sao? Cái đó á?」

【Hachiroku】
「Chắc chắn rồi ạ. Như ga Teuou thời điểm trước cuộc Đại bãi bỏ. Động tác bấm vé của các nhân viên ga được giao quản lý cửa soát vé chính lối đi trung tâm diễn ra nhanh như chớp nhoáng —— quả thực là một thần kỹ ạ」''',

    'tw_tips_共感.txt': '''Cộng cảm (Kyokan)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Cộng cảm (kyokan) là phương thức liên lạc giữa các Railord với nhau, cho phép truyền đạt thông tin, cảm giác và thậm chí cả cảm xúc ở một mức độ nhất định ạ」

【Reina】
「Cộng cảm tuy rất tiện lợi nhưng nếu khoảng cách quá xa thì sẽ không thể kết nối được đâu ạ. Hơn nữa, nếu một Railord đang rơi vào tình trạng hoảng loạn hay bất ổn thì cũng khó lòng nhận được cộng cảm từ họ lắm đó ạ」

【Hachiroku】
「Có tin đồn rằng đó là do thiết bị an toàn hoạt động để ngăn chặn sự ảnh hưởng lan rộng... nhưng thực tế là ngay cả các Railord như chúng tôi cũng không thể nắm bắt đầy đủ các chi tiết về cách hoạt động của cộng cảm ạ」''',

    'tw_tips_列車.txt': '''Tàu (Ressha)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Từ 'tàu' (ressha) mang hai ý nghĩa lớn ạ. Một là nhóm các toa xe đường sắt được nối với nhau từ hai toa trở lên. Ý nghĩa còn lại là phương tiện đường sắt đang di chuyển trên đường ray theo biểu đồ chạy tàu ạ」

【Paulette】
「Ví dụ, ngay cả khi Kiha 07 không nối thêm toa xe nào khác và chỉ chạy đơn độc một toa, nhưng nếu di chuyển trên đường ray theo đúng biểu đồ chạy tàu thì nó vẫn được coi là tàu đấy」

【Hachiroku】
「Để biết thêm chi tiết, xin hãy xem thêm ở mục ghép đoàn tàu ạ」''',

    'tw_tips_列車防護.txt': '''Phòng vệ tàu (Ressha bougo)
*解説
;---------------------------------------------------------------
【Paulette】
「Khi tàu không thể vận hành an toàn do tai nạn, sự cố, hay bất kỳ lý do nào khác, đoàn tàu đó phải được dừng lại ngay lập tức, đồng thời phải dừng tất cả các đoàn tàu đang chạy xung quanh để tránh bị cuốn vào sự cố」

【Hachiroku】
「Nói cách khác, khi đó phát sinh nghĩa vụ ngăn ngừa tai nạn liên đới. Để thực hiện nghĩa vụ này, các biện pháp nhằm dừng khẩn cấp đoàn tàu gặp sự cố và các đoàn tàu đang chạy xung quanh được gọi là phòng vệ tàu (ressha bougo) ạ」

【Paulette】
「Dù bằng bất kỳ phương pháp nào —— ống pháo hiệu, pháo hiệu nổ đường ray hay cờ đỏ —— một khi nhận được tín hiệu phòng vệ tàu, các tổ lái và Railord đều có nghĩa vụ lập tức thực hiện các biện pháp phòng vệ tàu. Để biết thêm chi tiết, các bạn hãy xem thêm ở mục ống pháo hiệu nhé」''',

    'tw_tips_制動.txt': '''Hãm phanh (Seido)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Hãm phanh (seido) là việc tác dụng lực phanh lên bánh xe chủ động để giảm tốc độ vận hành của phương tiện —— nói một cách đơn giản và dễ hiểu hơn thì chính là 'gài phanh để giảm tốc độ' ạ」''',

    'tw_tips_制御車.txt': '''Toa điều khiển (Seigyo-sha)
*解説
;---------------------------------------------------------------
【Reina】
「Toa điều khiển là toa xe đường sắt có trang bị thiết bị lái —— tức là có buồng lái hoặc ghế lái đó ạ. Nếu các bạn muốn biết chi tiết hơn thì có thể xem thêm ở các mục toa dẫn đầu hay toa giữa nữa nha」''',

    'tw_tips_制輪子.txt': '''Guốc phanh (Seirinshi)
*解説
;---------------------------------------------------------------
【Paulette】
「Guốc phanh (seirinshi) chính là bộ phận guốc hãm. Khi muốn phanh bánh xe đang chạy, người ta sẽ ép guốc phanh vào mặt lăn của bánh xe, dùng lực ma sát đó để làm giảm tốc độ quay của bánh xe」

【Hachiroku】
「Lực quán tính tác động lên phương tiện đường sắt là vô cùng khủng khiếp, nên nếu guốc phanh được làm từ vật liệu nửa vời thì sẽ hoàn toàn không có tác dụng. Thông thường, guốc phanh của đầu máy hơi nước được làm bằng gang —— loại sắt mềm hơn thép và thường được sử dụng cho việc đúc ạ」''',

    'tw_tips_前進フルギア.txt': '''Cài hết số tiến (Zenshin full gear)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Việc xoay cần đảo chiều hết cỡ theo hướng tiến lên được gọi là cài hết số tiến (zenshin full gear) ạ. Để biết thêm chi tiết, xin vui lòng xem thêm ở mục cần đảo chiều ạ」''',

    'tw_tips_力行.txt': '''Chạy kéo tải (Rikko)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Việc chạy bằng cách quay bánh xe chủ động dưới sức đẩy của hơi nước được đưa vào xi-lanh được gọi là chạy kéo tải (rikko) ạ. Ngược lại, việc chạy chỉ bằng quán tính có sẵn mà không dùng lực của hơi nước được gọi là chạy theo quán tính ạ」

【Soutetsu】
「Để biết thêm chi tiết, xin mời tham khảo thêm các mục chạy quán tính và bánh xe chủ động」''',

    'tw_tips_加減弁.txt': '''Van tiết lưu hơi (Kagen-ben)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Thiết bị dùng để điều tiết lượng hơi nước đưa vào piston và xi-lanh giúp làm quay bánh xe chủ động của đầu máy hơi nước chính là van tiết lưu hơi (kagen-ben) ạ」

【Soutetsu】
「Nếu so sánh với ô tô thì nó tương tự như chân ga. Khi kéo tay gạt van tiết lưu hơi về phía sau, lượng hơi nước được nạp vào sẽ tăng lên, giúp lực gia tốc của đầu máy mạnh hơn. Ngược lại, nếu đẩy tay gạt lên để đóng van, lượng hơi nạp vào sẽ giảm đi và dần chuyển sang chế độ chạy cắt hơi」

【Hachiroku】
「Nếu dùng hơi nước quá nhiều sẽ dẫn đến thiếu hụt, còn nếu gia tốc quá nhanh thì việc dừng tàu sẽ không còn dễ dàng nữa. Việc điều khiển van tiết lưu hơi chính là một trong những điểm cốt lõi vô cùng quan trọng khi lái đầu máy hơi nước ạ」''',

    'tw_tips_動力車.txt': '''Toa xe động lực (Doryoku-sha)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Đầu máy, toa xe tự hành, tàu điện nói chung sở hữu lực kéo —— tức là lực đẩy đường ray của bánh xe chủ động để tự di chuyển —— được gọi chung là toa xe động lực (doryoku-sha) ạ. Nói cách khác, tất cả các toa xe ở phía kéo các toa hành khách hoặc toa hàng không thể tự di chuyển đều được coi là toa xe động lực. Ngoài ra, trong trường hợp muốn chỉ định cụ thể toa xe động lực có trang bị thiết bị điều khiển lái, toa xe đó sẽ được gọi là toa xe điều khiển động lực ạ」'''
}

out_dir = r"E:\まいてつ Last Run!!\vn_patch"
for name, content in translations.items():
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote {name}")
