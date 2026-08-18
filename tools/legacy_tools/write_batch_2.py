import os

translations = {
    'tw_tips_スイッチバック.txt': '''Đường vòng zigzag (Switchback)
*解説
;---------------------------------------------------------------
【Paulette】
「Các phương tiện đường sắt cơ bản là rất khó để leo lên những dốc đứng. Tuy vậy, khi buộc phải vượt qua những con dốc cao như thế, người ta sẽ cải tiến đường ray để giúp tàu leo dốc dễ dàng hơn —— cơ chế đó chính là đường vòng zigzag (switchback) đấy ạ」

【Hachiroku】
「Cụ thể là chúng tôi thiết kế những đường ray zigzag có độ dốc thoai thoải, để đoàn tàu di chuyển tiến, lùi rồi lại tiến trên đó, nhờ vậy có thể đưa tàu leo lên vị trí cao hơn ạ」''',

    'tw_tips_スクレイパー.txt': '''Dao cạo xỉ than (Scraper)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Một loại bay kim loại dùng để cạo hoặc gạt sạch xỉ than bám cứng hoặc cháy khét được gọi là dao cạo xỉ than (scraper) ạ」''',

    'tw_tips_ストーブ客車.txt': '''Toa xe sưởi ấm (Stove kyaku-sha)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Toa xe sưởi ấm đúng như tên gọi của nó, là toa hành khách được lắp đặt bếp lò sưởi bên trong ạ. Nó chủ yếu được sử dụng ở những vùng lạnh giá để giúp hành khách tránh được cái lạnh buốt của mùa đông ạ」''',

    'tw_tips_タイフォン.txt': '''Còi hơi (Typhon)
*解説
;---------------------------------------------------------------
【Reina】
「Âm thanh còi báo động vang lên 'Poooon!' từ các phương tiện không sử dụng hơi nước làm động lực chính là còi hơi Typhon đó ạ」

【Paulette】
「Nếu còi hơi nước đúng như tên gọi của nó là loại còi phát ra âm thanh bằng hơi nước, thì Typhon là loại còi khí nén được phát ra bằng khí nén đấy」''',

    'tw_tips_タブレット.txt': '''Thẻ bảng (Tablet)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Thẻ bảng (tablet) là thiết bị cần thiết để khởi động Railord (búp bê đường sắt), đồng thời cũng đóng vai trò là phương tiện lưu trữ thông tin thu thập được khi Railord đang hoạt động ạ」

【Reina】
「Giữa cơ thể vận hành và cơ thể bảo trì, chỉ cần lắp thẻ bảng vào cơ thể cần vận hành là cơ thể đó có thể hoạt động với đầy đủ kiến thức và thông tin đã ghi chép từ trước đến nay rồi đó ạ」''',

    'tw_tips_ターミナル駅.txt': '''Ga đầu mối (Terminal station)
*解説
;---------------------------------------------------------------
【Paulette】
「Ý nghĩa gốc của nó là 'ga nằm ở cuối một tuyến đường sắt', tức là nhà ga vừa là điểm khởi đầu vừa là điểm kết thúc. Tuy nhiên ở Nhật Bản, nó thường được dùng để chỉ 'nhà ga nơi hành khách có thể chuyển sang các tuyến tàu khác' đấy」''',

    'tw_tips_ダイアグラム.txt': '''Biểu đồ chạy tàu (Diagram)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Nhờ sự cộng cảm giữa các Railord (búp bê đường sắt) với nhau, dù trên một tuyến đơn hay giữa nhiều tuyến khác nhau, chúng tôi có thể điều phối vận hành tàu một cách hiệu quả nhất theo các biến động thực tế ạ」

【Reina】
「Nhưng mà, nếu chúng ta không nghĩ đến việc vận hành của công ty đường sắt hay sự tiện lợi của khách hàng, thì tuyến đường sắt sẽ không dễ dàng được mọi người lựa chọn sử dụng đâu ạ. Vì vậy, việc cùng nhau thảo luận và cân nhắc mọi yếu tố để xây dựng chính là biểu đồ chạy tàu (diagram) —— kế hoạch vận hành của tàu đó ạ」

【Hachiroku】
「Trong điều kiện bình thường, đoàn tàu sẽ vận hành theo biểu đồ thường lệ. Tuy nhiên, vào những mùa du lịch cao điểm hay khi xảy ra sự cố, biểu đồ tạm thời sẽ được lập ra để ứng phó với sự thay đổi. Để biết thêm chi tiết, xin vui lòng xem thêm ở mục kế hoạch vận hành ạ」''',

    'tw_tips_ディーゼルトレーラー.txt': '''Xe rơ-moóc diesel (Diesel trailer)
*解説
;---------------------------------------------------------------
【Paulette】
「Nói một cách nghiêm ngặt, rơ-moóc chỉ bộ phận kéo được kéo sau đầu kéo. Tuy nhiên, thông thường người ta gọi cả bộ gồm đầu kéo và rơ-moóc là 'xe rơ-moóc'. Và khi động cơ của xe đầu kéo sử dụng dầu diesel thì nó được gọi là xe rơ-moóc diesel đấy」

【Hachiroku】
「Vì việc vận chuyển hàng siêu trường siêu trọng bằng động cơ Aerocraft là vô cùng khó khăn, nên từ xưa đến nay, nhân vật chính trong việc vận chuyển đường bộ các toa xe đường sắt khi không sử dụng đường ray vẫn luôn là xe rơ-moóc diesel ạ」''',

    'tw_tips_ディーゼル気動車.txt': '''Toa xe diesel tự hành
*解説
;---------------------------------------------------------------
【Reina】
「Toa xe diesel tự hành là loại toa xe tự hành chạy bằng động cơ diesel giống như Kiha 07S đó ạ」

【Paulette】
「Để biết thêm chi tiết, các bạn hãy xem thêm ở phần toa xe tự hành nhé」''',

    'tw_tips_トレインマーク.txt': '''Biểu trưng tàu (Train mark)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Các đoàn tàu tốc hành, tàu đặc biệt hay tàu tạm thời cho sự kiện thường được đặt các tên thân mật như 'Tsubame' (Chim én), 'Hato' (Chim bồ câu). Biểu trưng được gắn lên các toa xe để hiển thị những tên thân mật đó gọi là biểu trưng tàu (train mark) ạ」

【Paulette】
「Biểu trưng được gắn ở phía mũi của toa xe đầu tiên được gọi là biểu trưng đầu tàu (headmark). Biểu trưng gắn ở phía sau cùng của đoàn tàu được gọi là biểu trưng đuôi tàu (tailmark). Nhiều thiết kế trông rất dễ thương nên móc khóa hay đồ lưu niệm in biểu trưng tàu từng bán rất chạy ngày xưa đấy」''',

    'tw_tips_ドカ停.txt': '''Đỗ tàu lâu (Doka-tei)
*解説
;---------------------------------------------------------------
【Soutetsu】
「Doka-tei là thuật ngữ chỉ việc tàu khách đỗ lại trong khoảng thời gian dài khi đã vào sân ga. Mặc dù không có quy chuẩn tuyệt đối nào, nhưng bất kỳ lần đỗ nào kéo dài trên một tiếng đồng hồ đều có thể được xem là đỗ kéo dài lâu (doka-tei)」''',

    'tw_tips_ドラフト.txt': '''Hút gió lò hơi (Draft)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Ở đầu máy hơi nước, việc đảm bảo thông gió là cần thiết để đốt cháy than. Thiết bị thực hiện việc này được gọi là quạt hút lò hơi (blower), và việc xả hơi nước trong lò hơi qua ống khói để quạt hút hoạt động được gọi là hút gió lò hơi (draft) ạ」

【Soutetsu】
「Tiếng kêu 'bịch, bịch' phát ra khi đầu máy hơi nước hoạt động chính là âm thanh được tạo ra trong quá trình hút gió lò hơi —— tức tiếng draft. Đối với tiếng kêu 'xình, xịch' (tiếng blast) thường được nhắc đến song hành với tiếng draft, hãy tham khảo mục khí thải xi lanh (blast)」''',

    'tw_tips_ドレンコック.txt': '''Van xả nước ngưng (Drain cock)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Hơi nước sử dụng trong đầu máy hơi nước một khi nguội đi tất nhiên sẽ ngưng tụ thành nước. Nước này được gọi là nước ngưng (drain water). Và chiếc van dùng để mở van xả thải nước đó chính là van xả nước ngưng (drain cock) ạ」

【Soutetsu】
「Để biết thêm chi tiết, xin hãy xem thêm ở mục xả nước ngưng hơi nước」''',

    'tw_tips_バラスト.txt': '''Đá ba-lát (Ballast)
*解説
;---------------------------------------------------------------
【Hachiroku】
「Đá ba-lát là loại đá dăm, được rải dưới các thanh tà vẹt. Cùng với tà vẹt, nó có tác dụng giảm chấn động mà đường ray phải chịu từ đoàn tàu đang chạy qua ạ」

【Soutetsu】
「Ngược lại, đá ba-lát cũng giúp giảm thiểu độ rung và tiếng ồn đối với đoàn tàu đang chạy. Dù chỉ là những viên đá nhỏ bé, nhưng hiệu quả đóng góp lại vô cùng to lớn, đúng nghĩa là những người hùng thầm lặng sau ánh hào quang」''',

    'tw_tips_ビュッフェ.txt': '''Quầy ăn nhẹ (Buffet)
*解説
;---------------------------------------------------------------
【Soutetsu】
「Quầy ăn nhẹ (buffet) là trang thiết bị trên tàu dùng để bán đồ ăn thức uống nhẹ. Hiện tại, có vẻ như việc bố trí quầy ăn nhẹ thay thế cho toa ăn trên các đoàn tàu du lịch là khá phổ biến」'''
}

out_dir = r"E:\まいてつ Last Run!!\vn_patch"
for name, content in translations.items():
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8-sig") as f:
        f.write(content.strip() + "\n")
    print(f"Wrote {name}")
