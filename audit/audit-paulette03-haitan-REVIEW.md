# Audit: Paulette 03_廃炭鉱 — 132 dòng Việt sai (đã đối chiếu JP + TW, CSV3)

File: `03_Paulette/ポーレット03_廃炭鉱.txt.toml` — 430 dòng script, **132 dòng Việt sai = 30,7%** (bản audit 19/11 ghi 133; kiểm chứng lại 22/11 đối chiếu CSV3: loại 4, sửa 5, thêm 3 — xem §0).
Ngày audit: 19/11/2026; kiểm chứng lại 22/11/2026 đối chiếu CSV3 Trang tính 3 (KHÔNG dùng CSV cũ `maitetsu_translation.csv` nữa — xem §0). Nguồn đối chiếu: CSV3 (cột JP Original + TW Original/Current) và TOML-2.

## §0 — Kiểm chứng lại 22/11/2026 (đối chiếu CSV3 Trang tính 3, KHÔNG dùng CSV cũ)
- Bản audit 19/11 dùng `maitetsu_translation.csv` (CSV cũ, đã lỗi thời). Kiểm chứng lại toàn bộ 133 bản sửa đối chiếu CSV3: jp/tw khớp tuyệt đối 132/132 (0 lệch); old_vn trong JSON cũ khớp CSV cũ 132/132 nhưng KHÁC CSV3 ở 36 dòng (nội dung) + 38 dòng (chỉ khác vị trí `\n`/khoảng trắng) — tức CSV cũ và CSV3/TOML xếp cột Việt khác nhau ở 40/430 dòng. JSON chuẩn mới dùng old_vn = VN hiện tại trong CSV3 (= TOML, 0 lệch chuẩn hoá trên cả 430 dòng).
- Lệch 132-vs-133: JSON cũ (`audit-haitan-wrong-full.json`, 132 mục) thiếu key **2483** (có trong khối TOML của review, không có trong JSON) — đã bổ sung vào JSON chuẩn (JP 『わかる』『見える』...; bản sửa đổi "những người" → "cảm giác", đúng JP hơn). JSON cũ giữ nguyên trên đĩa làm bản gốc.
- LOẠI 4 bản sửa (dòng đã đúng trong file hiện tại, bản sửa chỉ là viết lại tương đương): **2466, 2856, 3000** (bản sửa trùng khớp VN hiện tại sau chuẩn hoá — chỉ khác vị trí `\n`; VN hiện tại đã là bản dịch đúng của JP) và **2690** (VN hiện tại đã dịch đúng hoàn toàn JP 遠足組...宿舎跡...; bản sửa chỉ đổi cách diễn đạt).
- SỬA 5 bản sửa trong lượt soát 2: **1382, 1383** (khôi phục dấu 「」 của JP — bản sửa cũ làm mất dấu thoại); **2002** (khôi phục 「」; chỉ bỏ "đấy" thêm); **2442** (khôi phục tag %l của 圧: `\x%l圧;#00ffc040;Áp lực%l;#;` — bản sửa cũ làm mất tag); **2674** ("ông bà" → "ông ngoại" theo quy tắc Seki đã chốt 20/11: 堰 là ông ngoại của Fukami).
- THÊM 3 dòng sai mới phát hiện khi kiểm chứng: **1345** (sweep raw-tsu: VN còn nguyên 「っ///////!」 → 「Ư///////!」), **2155** (sweep lost-gasp-whole: 「!!!」 → 「Ư!!!」), **2752** (VN hiện tại "「Chị Reina, bái bai!」" hoàn toàn sai JP — tay Paulette quay bánh xe sắt như bánh lái; bản dịch mới dùng tag 舵輪 gloss "bánh lái"; chuỗi "Chị Reina, bái bai!" không khớp JP nào trong toàn bộ CSV3 — dòng Việt mồ côi).
- Kiểm chứng ngoài 133: 3 dòng VN khác nhau giữa CSV cũ và CSV3 ngoài danh sách sửa — **1948, 2106** (chỉ khác vị trí `\n`, VN hiện tại dịch đúng — không sai), **2752** (sai, đã thêm ở trên). **1791** GIỮ (っ cuối rendered "ơ", TW 啊 ủng hộ; không mất âm). **2042** GIỮ "Hả." cho はぁっ (xem Cờ ở snippet — っ đã thể hiện qua "Hả." + dấu chấm).
- Lượt soát 2: 133 / 124 giữ nguyên / 4 loại / 5 sửa (+3 thêm). Tổng cuối: **132/430 = 30,7%**. Khối TOML trong review đã thay bằng khối cuối 132 khóa (parse-kiểm chứng, 0 sai lệch). JSON chuẩn mới: `audit-paulette03-haitan-wrong.json` (list-of-dicts, key chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 132/132).
- Nguồn: TOML một bản duy nhất, md5 `56047b5be8ac3a038931f0aa94d43117`, không có bản trùng (11 nhóm trùng trong toml2, file này không thuộc nhóm nào). CSV3 1 bộ duy nhất, 430 dòng, 0 key trùng, 0 dòng chưa dịch, 0 dòng JP trống. Chỉ 1 cặp VN trùng giá trị trong file hiện tại (1779/2388 "「Vâng ạ.」") — bản sửa giải quyết cả hai. `[selections]` rỗng.
- Cơ chế lỗi (sửa lại kết luận 19/11): KHÔNG có shift cố định; là lệch rải rác — NHƯNG bản đồ lệch của CSV cũ và của TOML hiện tại KHÁC NHAU (40 dòng VN khác nhau). Các cặp "chuyển chỗ" nêu ở § dưới (2466←3000, 3000←2410, 2856←2690) là của CSV cũ, KHÔNG còn đúng với file hiện tại: trong TOML hiện tại 2466/2856/3000 đã đúng, 2002 gần đúng (chỉ thừa "đấy"). Các dòng Việt "Hikari/ăn sáng/khám sức khỏe/kéo dãn" không khớp JP nào trong toàn bộ CSV3 — dòng Việt mồ côi, không phải tràn từ file Maitetsu khác (đã tìm toàn CSV3, chỉ có trong file này).

## Kết luận về cơ chế lỗi
- KHÔNG phải lệch đều theo key (không có shift cố định nào làm tăng độ khớp).
- Là **lỗi chép nhầm rải rác**: cột Việt bị xáo trộn giữa các dòng trong cùng file, nhiều dòng bị trùng lặp (16 giá trị Việt xuất hiện 2 lần), và một số bản dịch đúng còn nằm ở key sai (xem "Các dòng bị chuyển chỗ" bên dưới).
- Cột Nhật và cột Trung khớp nhau (~98%), nên chỉ cần dịch lại từ Nhật/Trung là ra bản đúng — không cần tìm thêm nguồn.

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)
Lưu ý khi chép: tag viết dạng `\\x%l...%l;#;`, xuống dòng viết dạng `\\n`, dấu `"` trong câu viết dạng `\"` — giống như các dòng đúng sẵn có trong file. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng.

```toml
75 = "\\x%lタイフォン;#00ffc040;còi Typhon%l;#; vang lên nhẹ nhàng, \\x%lキハ07;#00ffc040;Kiha 07%l;#; thả chúng tôi xuống rồi chạy vụt đi."
1330 = "……Nói một lời thôi thì là chẳng có chút thi vị nào.\\nKhông, phải nói là ngoài “gió” ra thì thật sự chẳng còn gì cả."
1340 = "……Tại sao Paulette, người yêu đường sắt đến vậy, lại chẳng tỏ ra mấy hứng thú với ga bỏ hoang này nhỉ——"
1345 = "「Ư///////!」"
1357 = "「——Ừm.」"
1377 = "「……Em hiểu rồi. Nếu đã vậy thì」"
1382 = "「……Di tích tuyến đường sắt bỏ hoang, quả nhiên quanh đây không có nhỉ.」"
1383 = "「……Chắc hẳn nơi này từng phồn thịnh lắm.」"
1630 = "「Cơ bản mà nói, dù Reina có bị xử lý chậm đi nữa, chỉ cần làm đúng theo chỉ dẫn của Hachiroku thì hoàn toàn không có vấn đề gì.」"
1632 = "「Không.」"
1640 = "「Không cần phải hoảng loạn đâu.\\nViệc cần làm bây giờ, chỉ là chăm chú nhìn về phía trước mà thôi.」"
1645 = "「Không có gì đâu ạ.」"
1652 = "「Nhưng mà, chỉ cần tận mắt chứng kiến cách xử lý trong tình huống khẩn cấp một lần ở đây, Hibiki sẽ hiểu sâu hơn về các chỉ dẫn lúc khẩn cấp.」"
1653 = "「Nhưng mà, vẫn có khả năng cực kỳ thấp là Hibiki sẽ tự mình kéo \\x%lブレーキ;#00ffc040;phanh%l;#; theo phán đoán của em ấy.」"
1656 = "「Nói cách khác, trong trường hợp đó, khi phải dừng khẩn cấp gần ga bỏ hoang mỏ than Jutsu-sen, chỉ cần Hibiki đi bộ đến ga bỏ hoang là xong, phải không?」"
1674 = "「Nhưng mà……」"
1691 = "「Xuất phát! Tiến lên!」"
1696 = "「Khi chuyển số, hãy đạp bàn đạp ly hợp này, ở phía dưới \\x%l運転台;#00ffc040;buồng lái%l;#; ấy.」"
1723 = "「Trừ khi thời tiết cực kỳ xấu, dọc tuyến Yui, chỗ duy nhất không có sóng điện thoại là khu vực quanh ga bỏ hoang mỏ than Jutsu-sen thôi.」"
1728 = "「Chừng nào chúng tôi còn ở trên này, \\x%l8620;#00ffc040;8620%l;#; sẽ không chạy.\\nToàn bộ tuyến này sẽ trở thành khu vực \\x%l閉塞;#00ffc040;phong tỏa%l;#; độc quyền của \\x%lキハ07;#00ffc040;Kiha 07%l;#;.」"
1738 = "「Hả!? Sao lại—— chỗ này, đâu phải ga, cũng đâu phải ga bỏ hoang gì đâu.」"
1740 = "「Hả!? Em, em đâu có như vậy đâu!」"
1743 = "「Hả? Nhưng mà, cơ hội luyện tập chỉ có đúng lần này thôi đó?」"
1749 = "「Vậy nhé, anh hai, chị Paulette, cẩn thận nhé!」"
1758 = "「Ừm, \\x%lバラスト;#00ffc040;đá dăm%l;#; sao——」"
1779 = "「A!」"
1790 = "「A, xin lỗi! Tại em hoảng quá.」"
1803 = "「Ừm. Em hiểu rồi——em hiểu rồi ạ.」"
1804 = "「Ừm.」"
1805 = "「Vâng! À, vâng ạ. Cảm ơn nhiều lắm ạ!」"
1807 = "「Vâng!」"
1811 = "「Ừ, bọn anh đi một lát rồi về.」"
1834 = "「Được rồi, vậy thì.」"
1840 = "「Những lúc như vậy, đừng do dự, đừng hoảng loạn, hãy làm như thế này.」"
1882 = "「Không thể yên tâm được.\\nSự yên tâm lúc nào cũng là nguồn gốc của tai nạn.」"
1885 = "「Tôi cứ nghĩ nếu có liên lạc thì quanh đây hẳn phải còn dấu vết gì đó——\\nnhưng hoàn toàn chẳng có gì cả.」"
1889 = "「Vì thứ tôi thích là đường sắt còn đang sống……\\nnên về khoản đó tôi không rõ lắm.」"
1901 = "「Đã gạt số về phía trước rồi.\\nGiờ chỉ cần nối ly hợp là xe sẽ \\x%l力行;#00ffc040;chạy%l;#;.」"
1909 = "「Theo bản đồ cũ, tuyến Yui với bên này từng liên thông……\\nkhả năng từng chạy thẳng qua nhau khá cao đấy ạ.」"
1922 = "「Hibiki cũng vậy. Mong em lái tàu an toàn là trên hết.」"
1925 = "「Đúng là, cơ hội để Hibiki quan sát chị Paulette học cách vận hành, chỉ có đúng “lần này” thôi.」"
1944 = "「Vâng. Cứ đợi ở đó, khi bọn em quay lại gặp nhau, em sẽ lái tàu đưa mọi người về đến ga Ohitoyo.」"
1956 = "「Với Hibiki thì, học bằng mắt……\\nnhìn rồi nhớ sẽ nhanh hơn——phải không ạ?」"
1961 = "「Yên tâm rồi à?」"
1982 = "「Không tốt chút nào! Đến cả biển báo giới hạn tốc độ còn chẳng buồn nhìn, thì việc nhắc lại như vẹt có ý nghĩa gì chứ!」"
1984 = "「Đúng vậy.」"
1986 = "「Đúng rồi. Cứ như vậy nhé.」"
2002 = "「Sự khác biệt trong cách cảm nhận giữa “mọi người” và Paulette.\\nĐó có lẽ chính là thứ gọi là tố chất của một nhà lãnh đạo.」"
2003 = "「Paulette. Nếu được, em có thể cho Hibiki xem mẫu cách dừng tạm thời ở ga mỏ than Jutsu-sen không?」"
2004 = "「Paulette, em làm mẫu cho con bé xem được không?\\nDù sao thì, Hibiki mỗi khi học cái gì cũng——」"
2010 = "「Sau đó đương nhiên là dấu vết của đường ray. Có lẽ……\\nthứ còn sót lại nhiều khả năng nhất là \\x%lバラスト;#00ffc040;đá dăm%l;#; đấy.」"
2016 = "「Dù sao thì, tốt nhất là đừng bao giờ có cơ hội để Hibiki phải thao tác \\x%lブレーキ;#00ffc040;phanh%l;#;.」"
2031 = "「Khi đã dừng hẳn, nhớ gài cả \\x%lブレーキ;#00ffc040;phanh tay%l;#; nữa nhé.」"
2042 = "「Hả.」"
2045 = "「Di tích tuyến đường sắt bỏ hoang, người ta tìm ra bằng cách nào vậy?」"
2083 = "「Đây là…… ga bỏ hoang mỏ than Jutsu-sen sao.」"
2086 = "「Đây là mẫu cho việc cần làm trong trường hợp khẩn cấp.」"
2087 = "「Nếu được như vậy, dù là chuyến dừng đúng giờ ở Yui và Ohitoyo, hay chuyến dừng tạm buổi chiều để đón bọn anh, độ an toàn cũng sẽ cao hơn.」"
2088 = "「Như vậy là đã dừng lại an toàn rồi——\\ngiờ hãy gọi điện cho anh Hayase, hoặc chị Mayami để cầu cứu.」"
2105 = "「Dạ, em cũng muốn nhờ chị làm mẫu cho em xem ạ.」"
2111 = "「Vậy thì, làm mẫu đến đây là đủ rồi chứ?」"
2117 = "「Trong trường hợp đó, chắc phải có không gian và thiết bị để dỡ hàng từ \\x%l貨車;#00ffc040;toa chở hàng%l;#; xuống, hay để chuyển container——」"
2127 = "「Nhưng mà, nếu dừng ở chỗ không có sóng thì sao ạ?」"
2131 = "「Vậy thì, nếu như không liên lạc thì sao?」"
2136 = "「Gi-giới hạn tốc độ, 50! Được rồi!」"
2137 = "「Hết giới hạn tốc độ. Được rồi!」"
2138 = "「Giới hạn tốc độ. 50!」"
2150 = "「Trước tiên…… hãy coi cần số này tương đương với \\x%l逆転機;#00ffc040;cần đảo chiều%l;#; của \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#;.」"
2154 = "「Ư!」"
2155 = "「Ư!!!」"
2367 = "Đôi mắt xanh nãy giờ vẫn đang quan sát đường ray tuyến Yui rồi mặt đất xung quanh, ngẩng lên."
2368 = "Không chỉ nhà ga bỏ hoang, mà xung quanh nó cũng——chẳng còn lại thứ gì."
2376 = "Dù sao thì, thành quả huấn luyện cũng đã thể hiện ra.\\nLúc khởi hành trơn tru như trượt đi, lúc tăng tốc cũng không cảm nhận được rung lắc."
2388 = "Thời tiết hôm nay quang đãng.\\nNhìn qua cửa sổ, bầu trời chẳng có lấy một gợn mây."
2395 = "Nhìn kỹ lại…… ấn tượng hoàn toàn khác với \\x%l運転台;#00ffc040;buồng lái%l;#; của \\x%l8620;#00ffc040;8620%l;#;."
2400 = "Những người đó thì có thể điều xe chạy xăng đến, còn chị Mayami thì chắc chắn lúc nào cũng nghĩ ra cách đối phó tốt nhất."
2401 = "Nhưng mà, giọng đáp lại ngay lập tức lại căng thẳng trở lại."
2405 = "Chẳng thấy thiết bị gì đâu, nhưng không gian thì thừa thãi."
2410 = "Thế nhưng, tố chất hiếm có ấy, trực giác ấy.\\nCả về đường sắt lẫn chính trị, Paulette hiện tại đều chưa phát huy được hết."
2430 = "Hachiroku gật đầu thật sâu."
2432 = "Giọng nói của Hachiroku đầy vẻ cảm phục."
2438 = "Vẻ gồng cứng đã hoàn toàn biến mất."
2442 = "\\x%l圧;#00ffc040;Áp lực%l;#; dồn lên \\x%lブレーキ;#00ffc040;phanh%l;#; đương nhiên sẽ từ từ làm giảm tốc độ \\x%l列車;#00ffc040;đoàn tàu%l;#;——rồi cuối cùng dừng hẳn lại."
2464 = "Chỉ cần lấy lại được bình tĩnh, thì nhất định sẽ không bỏ sót mục tiêu nào đâu."
2483 = "Vì cảm giác “hiểu” và “nhìn thấu” quá rõ ràng, nên chắc em ấy chẳng thể tưởng tượng nổi cảm giác “không hiểu” và “không nhìn thấu”."
2484 = "Nói cách khác, là vì đúng lúc đến lượt Reina thao tác \\x%lブレーキ;#00ffc040;phanh%l;#; thì em ấy lại bị xử lý chậm——ngủ gật, mà Paulette lại không có mặt."
2489 = "Đồng thời với việc Reina bị xử lý chậm, khả năng Hachiroku gặp sự cố cũng không phải là bằng không."
2492 = "Trong lúc hướng dẫn huấn luyện, chắc Hachiroku cũng đã hiểu ra.\\nKhả năng học hỏi của Hibiki tỏa sáng nhất là khi em ấy học bằng cách nhìn rồi bắt chước."
2497 = "Nghe có tiếng thở phào nhẹ nhõm.\\nTừ Paulette đang ngồi ở ghế bên cạnh tôi."
2521 = "Vừa nghiêm nghị, gọn gàng, mà lại cho ấn tượng vô cùng mềm mại và nhẹ nhàng."
2522 = "Dáng đứng khiến người ta liên tưởng đến từ “khỏe khoắn”.\\nSau khi Reina xác nhận an toàn, Hibiki nhẹ nhàng đưa tay ra."
2526 = "Đó là một nhận xét hoàn toàn chính xác.\\nSau chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; tạm thời lúc sáng sớm này, chuyến tiếp theo sẽ là chuyến \\x%l列車;#00ffc040;đoàn tàu%l;#; đi học đúng giờ buổi sáng."
2539 = "Em ấy đã sửa lại thật chuẩn chỉ trong một lần.\\nĐúng là Hibiki——đôi mắt của một họa sĩ."
2550 = "Đưa cần gạt trông như nấc số về lại, ngắt ly hợp, tắt số.\\nRồi dồn lực vào tay cầm \\x%lブレーキ;#00ffc040;phanh%l;#;."
2576 = "Ngay cả siêu thị hay thứ gì đó, chủ sở hữu của bãi đỗ xe ấy, cũng đã rút đi, rồi dần dần người ta, xe cộ, mọi thứ đều rời khỏi nơi này."
2577 = "Từ \\x%l運転台;#00ffc040;buồng lái%l;#;, vang lên tiếng “à” đầy vẻ đồng tình của Hibiki."
2624 = "Tôi cũng có chút nghi ngờ, nhưng khi ra ngoài nhà ga nhìn tận mắt vật thật ở cự ly gần, tôi đã hiểu lý do."
2627 = "Cái nào là \\x%l自弁;#00ffc040;phanh tự động%l;#;, cái nào là \\x%l単弁;#00ffc040;phanh đơn%l;#;, đến cả chuyện đó tôi cũng hoàn toàn không phân biệt nổi."
2651 = "Nếu nói đây là cơ hội luyện tập được Paulette trực tiếp hướng dẫn, thì quả thực đây sẽ là lần đầu tiên và cũng là lần cuối cùng.\\nNhưng mà——"
2654 = "Việc nơi này trở thành bãi đỗ xe có nghĩa là, ngay cả sau khi trở thành ga bỏ hoang, nơi đây vẫn còn giữ được chức năng đô thị."
2668 = "Hibiki gật đầu.\\nMạnh đến mức dù chỉ nhìn thấy lưng em ấy, tôi cũng nhận ra rõ ràng."
2670 = "Mỗi lần gật đầu, khuôn mặt Hibiki lại dần dần dịu lại."
2672 = "Vai Hibiki khẽ động, tôi cảm nhận được em ấy thở phào nhẹ nhõm."
2674 = "“Anh Hayase” trong trường hợp này, không phải là Fukami, mà là ông ngoại của Fukami——nhà Seki đó."
2688 = "Với tôi thì đúng như dự đoán, nhưng Paulette lại dừng lại với vẻ mặt bối rối."
2702 = "Chỉ với chừng ấy hướng dẫn, Hibiki đã thay đổi không chỉ bên trong, mà cả tư thế nữa."
2733 = "Giống như tôi, chắc chắn Paulette cũng không rời mắt khỏi \\x%l運転台;#00ffc040;buồng lái%l;#; dù chỉ một khoảnh khắc."
2739 = "Chân Paulette di chuyển, đồng thời tay phải em ấy thao tác cần số."
2742 = "Cười nhẹ nhàng, Paulette buông tay khỏi các tay cầm.\\nHibiki cứ thế đón lấy chúng vào tay mình."
2743 = "Vừa nói, Paulette vừa chỉ vào tuyến chính của tuyến Yui."
2748 = "Từng lời từng chữ của Paulette, chắc sẽ gỡ bỏ được nỗi bất an của em ấy."
2749 = "Dáng đứng của Paulette, gương mặt nghiêng thỉnh thoảng lại liếc thấy, không sao diễn tả được vẻ đẹp ấy."
2752 = "Tay Paulette quay vòng vòng chiếc bánh xe sắt lớn như \\x%l舵輪;#00ffc040;bánh lái%l;#;."
2756 = "Paulette lặng lẽ đứng dậy, tiến về phía \\x%l運転台;#00ffc040;buồng lái%l;#;."
2782 = "Để tránh xảy ra tình huống như vậy, hãy giảm bớt lo lắng dù chỉ một chút——à, phải rồi."
2794 = "Khi xảy ra sự cố nghiêm trọng thì chỉ cần dừng lại là được.\\nNhư vậy sẽ đảm bảo an toàn."
2796 = "Đúng vậy.\\nBọn anh hoàn toàn chẳng hề nghĩ đến chuyện đó——"
2814 = "Trong \\x%l運転台;#00ffc040;buồng lái%l;#; của \\x%lキハ07;#00ffc040;Kiha 07%l;#; mà em còn chưa quen, Hibiki lúc này không phải \\x%l機関助士;#00ffc040;phụ lái%l;#; cũng không phải \\x%l機関士;#00ffc040;Người lái tàu%l;#;, mà đang đóng vai trò \\x%l運転士;#00ffc040;người lái%l;#;."
2817 = "Nhờ vào chỉ dẫn quá rõ ràng ấy, cơ thể Hibiki vốn đang co rúm lại cũng thấy nhẹ nhõm hơn."
2855 = "Nếu ở đây mà căng thẳng quá, để rồi việc điều tra bị lơ là thì đúng là đặt xe trước ngựa."
2895 = "Đã thiếu một \\x%l運転士;#00ffc040;lái tàu%l;#; chính thức, lại còn sắp phải dừng ở ga bỏ hoang mỏ than Jutsu-sen, nơi bình thường vẫn chạy thẳng qua."
2898 = "Xung quanh rộng thênh thang quá mức, đến mức tôi chẳng biết phải nhìn đâu, nhìn thế nào nữa."
2921 = "Có thể sẽ có mưa rào buổi chiều, nhưng trong vài giờ tới thì chắc sẽ không có cơn mưa lớn cực đoan nào đâu."
2924 = "Dù đã tập luyện kỹ càng cùng Hachiroku, nhưng Hibiki vẫn căng thẳng đến cứng đờ cả người."
2928 = "Dù chỉ cần làm theo chỉ dẫn của Hachiroku là được, nhưng việc Hibiki không giấu nổi sự dao động cũng là điều dễ hiểu."
2955 = "Giọng Hibiki vang lên từ buồng lái, mắt vẫn không rời khỏi phía trước."
2978 = "（Nhưng mà…… chuyện này có khi lại không hay rồi.）"
2981 = "（Khác hẳn rồi.\\nChỉ cần có hướng dẫn phù hợp——không, chỉ cần có một “tấm gương”, là Hibiki đã có thể học được đến mức này bằng mắt sao.）"
2987 = "（Kịch, cạch——kịch, cạch——）"
2991 = "（À…… đúng là tư thế tự nhiên——\\ndáng vẻ của một chuyên gia dày dạn kinh nghiệm.）"
2992 = "（À——）"
3004 = "（Bụp!）"
```

## Các dòng bị chuyển chỗ (bản dịch đúng đang nằm ở key sai)
> Sửa 22/11: các cặp dưới đây là của CSV CŨ, không còn đúng với TOML hiện tại (xem §0). Trong file hiện tại, 2466/2856/3000 đã đúng, 2002 gần đúng — cả 4 đã loại khỏi danh sách sửa. Giữ lại § này làm hồ sơ gốc của bản audit 19/11.
Mấy trường hợp này không cần dịch lại, chỉ cần chuyển về đúng key — khối TOML trên đã dùng đúng bản đó:
- **2466** ← bản dịch đang nằm ở **3000**: "Ngay khi tôi cảm thấy "đã truyền đạt được rồi", điều đó lập tức biến thành một sự thấu hiểu mới về Paulette."
- **3000** ← bản dịch đang nằm ở **2410**: "(Quả nhiên Paulette…… với tư cách là một chính trị gia, em ấy cũng sở hữu tố chất xuất chúng.)"
- **2856** ← bản dịch đang nằm ở **2690**: "(Nếu xung quanh không thấy, thì chỉ còn cách đi bộ tìm thôi.)"
- **2002** ← bản dịch đang nằm ở **2483**: "Sự khác biệt trong cách cảm nhận giữa "mọi người" và Paulette. Đó có lẽ chính là thứ gọi là tố chất của một nhà lãnh đạo."

## Các cặp trùng lặp (cả hai key đều sai — bản đúng không nằm trong file này)
> Sửa 22/11: con số 16 cặp dưới đây là của CSV CŨ. Trong TOML hiện tại chỉ còn 1 cặp VN trùng giá trị (1779/2388 "「Vâng ạ.」") — bản sửa giải quyết cả hai. Giữ lại § này làm hồ sơ gốc của bản audit 19/11.
16 giá trị Việt xuất hiện 2 lần; ví dụ: 1959/2466 ("Ra là…… vậy sao." — chỉ 1959 đúng), 1630/2430 ("Kyaa!"), 2088/2674 ("Ừm. Thế này là ổn rồi."), 2127/1723 ("Vậy chúng ta về thôi."), 1656/1944 ("Paulette ra dáng làm mẹ…"), 2748/2670 ("Tôi gật đầu đồng tình sâu sắc…"), 1645/2742 ("Chính xác nha."), 1922/1807 ("Vậy thì chúng ta ăn sáng nhé."), 2924/2376 ("Chúng tôi áp sát lưng vào nhau…"), 2539/2464 ("(Hự—— hự hự hự——)"), 1758/2010 ("A, không được. Để anh đính chính lại…"), 2117/2405 ("Fufufu. Giống hệt loại nhà mình hay dùng thôi ạ?"), 2627/1696 ("Với ba sao."). Tất cả các key này đều đã có bản dịch mới trong khối TOML trên.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- 術仙炭鉱 = mỏ than Jutsu-sen; 湯医線 = tuyến Yui; 御一夜 = Ohimitera; キハ07 = Kiha 07; 8620 giữ nguyên [Quyết định 19/11: 御一夜 = Ohitoyo — 2 bản sửa 1944/2087 đã đổi sang "Ohitoyo"; các dòng đúng trong file vẫn dùng "Ohimitera", chờ đợt thống nhất sau. Quyết định 21/11: "Jutsu-sen" → "Jutsusen", "tuyến Yui" → "tuyến Yunoi" — cũng chờ đợt thống nhất; khối TOML cuối giữ nguyên dạng cũ trong các bản sửa để nhất quán với file.]
- 運転台 = buồng lái; 運転士 = lái tàu / người lái; 機関士 = Người lái tàu; 機関助士 = phụ lái
- ブレーキ = phanh; 手ブレーキ = phanh tay; バラスト = đá dăm; 貨車 = toa chở hàng; 列車 = đoàn tàu
- 力行 = chạy (áp lực kéo); 逆転機 = cần đảo chiều; 蒸気機関車 = đầu máy hơi nước; 自弁 = phanh tự động; 単弁 = phanh đơn; 閉塞 = phong tỏa
- Soutetsu độc thoại/dẫn chuyện xưng "Tôi"; Paulette gọi Soutetsu là "anh Soutetsu"; Hachiroku gọi "ngài Soutetsu" (đã giữ theo các dòng đúng trong file)

## Giới hạn của audit này
- Đã đọc hết 430 dòng script của file này (không chỉ dựa vào máy check): 132 dòng sai đã xác nhận (kiểm chứng lại 22/11 đối chiếu CSV3), 298 dòng còn lại khớp Nhật/Trung.
- Vẫn có thể sót vài dòng "trông hợp lý nhưng thực ra là bản dịch của dòng khác" (kiểu như 2483) — cách chắc chắn nhất vẫn là chơi qua chương và đối chiếu voice. Nếu Hieu gặp thêm dòng nào nghi ngờ trong file này thì gửi mình, mình kiểm tra nốt.
- Số ~662 dòng nghi lệch toàn dự án (ước tính bằng máy check thoại/dẫn) là **đánh giá thấp**: riêng file này máy chỉ bắt được 44/133 dòng sai. Các file nặng khác (Grand 01, Hibiki 03, Paulette 03 obasan, Hachiroku 13, Nagi_Fukami 08a) cần audit đọc hết từng dòng như file này thì mới có con số thật.

## Việc tiếp theo (chờ Hieu chọn)
1. Xuất lại CSV mới từ TOML hiện tại (để CSV không còn cũ, tránh build_patch.bat ghi đè mất bản dịch Mayami).
2. Audit tiếp các file nặng: Grand Rewrite 01 (~71+ dòng nghi), Hibiki 03, Paulette 03 obasan, Hachiroku 13, Nagi_Fukami 08a — mỗi file một bản review như file này.
3. Hoặc Hieu áp dụng khối TOML trên trước, chơi thử chương Paulette 03 rồi báo lại.
