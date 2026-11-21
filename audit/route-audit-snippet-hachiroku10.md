## ハチロク10 — ハチロク10_旺宮鉄道歴史館.txt.toml — 65/572 (11,4%)

- File: `ハチロク10_旺宮鉄道歴史館.txt.toml` — route 01_Hachiroku, 572 dòng script (độc thoại 196, Soutetsu 124, ひよこ 117, Hachiroku 99, Olivy 36). Nội dung: thăm Bảo tàng Lịch sử Đường sắt Oukyou, gặp tiến sĩ Fushicho (Hiyoko) — giải thích タブレット, cộng cảm toàn phần, lịch sử Stephenson/Trevithick, Đại bãi bỏ, sự kiện Ueyama; Olivy được kiểm tra có ý thức.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 572/572 (sau chuẩn hoá `\n`). `[selections]` rỗng. Không có bản sao file này (md5 `4326168a59b6c3b615098e40471f3923`).
- Phân loại (65): thuật ngữ 36 (タブレット 19, Ohitoyo 5, Teitetsu 3, 電車姫 4, 冥国 2, 運転体 2, 整備体 3, 宮司 1, 機関士 1 — 2146/3209/3510 mang nhiều lỗi trong một dòng), đại từ 9 (Soutetsu 'anh'→'tôi' 7: 2007, 2010, 2187, 2460, 2462, 2547, 2842; Hachiroku 2: 2289, 2340), gasp っ 9 (8 từ sweep + 2488 sweep phân loại sai), SFX 6 (tiếng cười thành tiếng rên 5: 2208, 2283, 2284, 2292, 2759; くすっ 1: 2943), dịch sai 3 (2019, 2181, 3475), thẻ %l 1 (2816), lỗi đánh máy 1 (3581 'xo xa'→'vượt xa').
- Sweep kiểm chứng: 9 mục cho file này (8 fix đều đúng, nhận nguyên văn; 2488 already-rendered bị phân loại sai — cùng mẫu っ cuối sau dấu gạch như 3447/3663 trong file, đã sửa thành ——Ư!). Không còn っ thô trong VN; thẻ %l cân bằng JP = VN ở mọi dòng sau khi sửa 2816.
- Đại từ đúng toàn file: Soutetsu 'tôi' với Hachiroku và tiến sĩ Fushicho, 'anh' với Olivy (2275, 2302 — tiền lệ ハチロク05); Hachiroku tự xưng 'em' nhất quán; Olivy gọi Soutetsu 'cậu' giữ nguyên.
- Chi tiết đầy đủ: `audit-hachiroku10-REVIEW.md`; danh sách sửa: `audit-hachiroku10-wrong.json` (65 mục, khối TOML 65 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 65/65; lượt soát 2: 65/65, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 115 file / 5.373 dòng sai** (cơ sở 114 file / 5.308 dòng sai + 65 file này)
- REBASE: cơ sở giao lúc spawn là 114 file / 5.308 dòng sai — đã kiểm chứng trực tiếp với ROUTE-AUDIT.md (dòng tổng cuối), khớp, không cần rebase.

- Chờ Hieu: 日ノ本 'Hinomoto' (1507, 2375, 2730, 3431, 3480) vs 'Hinamoto' (1529, 1994, 2488); Soutetsu gọi Olivy 'cậu' (2304) vs 'em' (2302); Hachiroku tự xưng 'Tôi' (2321, 2451, 2890) vs 'em'; tiến sĩ Fushicho gọi Soutetsu 'Anh Migita' (2092, 2197, 2198) vs 'ngài Migita'.

```toml
[script]
"1479" = "「Khả năng tự sao chép của \\x%lタブレット;#00ffc040;máy tính bảng%l;#;——của linh hồn. Hoặc là chức năng sinh sản.\\nChẳng phải là để giải trừ phong ấn được đặt trên đó sao.」"
"1488" = "「Các loại kiểm tra theo luật định của \\x%lレイルロオド;#00ffc040;Railord%l;#;,\\ntất cả đều được tiến hành trong trạng thái tháo \\x%lタブレット;#00ffc040;máy tính bảng%l;#;, tức là trạng thái không khởi động.」"
"2007" = "「Không đâu, em khiêm tốn như vậy làm tôi buồn đấy. Có Hachiroku,\\nvà có tôi——hai chúng ta đã cùng nhau, đi đến tận bước đường này mà.」"
"2010" = "「Không, tôi thấy câu nói đó của em cũng có vấn đề đấy.」"
"2019" = "「Dù muốn hay không, nhìn thấy một lần là không thể nào quên được luôn đó~!\\nMong được giúp đỡ nha, Doctor Phoenix!」"
"2062" = "「Ư!!?」\\n「!!」"
"2113" = "「Trên toàn thế giới, \\x%lタブレット;#00ffc040;máy tính bảng%l;#; của tất cả các \\x%lレイルロオド;#00ffc040;Railord%l;#;,\\nđều được xuất xưởng từ một nhà máy duy nhất.」"
"2146" = "「Tháo \\x%lタブレット;#00ffc040;máy tính bảng%l;#; ra khỏi cả \\x%l運転体;#00ffc040;thân vận hành%l;#; lẫn \\x%l整備体;#00ffc040;thân bảo trì%l;#;, rồi đem đi cất giữ.\\nTrạng thái đó, đã……kéo dài được hơn bốn năm rồi thì phải.」"
"2152" = "「Ra là vậy, có lẽ cũng có khía cạnh đó đấy.\\nĐiều đó cuối cùng, đã nuôi dưỡng nên văn hóa công ty của Đường sắt Ohitoyo.」"
"2181" = "「Không thể thực hiện được. ——Nếu đã như vậy, thì các Navi Aircra thông thường,\\nkhông sở hữu thứ gì đó……giống như linh hồn sao ạ?」"
"2184" = "「Chỉ cần suy ngược lại là được. Rằng 『\\x%lタブレット;#00ffc040;Máy tính bảng%l;#; mang một bản chất\\nsẽ bị loại bỏ nếu được biết đến quá rộng rãi』 đúng không?」"
"2187" = "「Dù vậy, tôi vẫn còn vô cùng thiếu kinh nghiệm.\\nThực tế thì, tôi cũng đâu biết gì về Cow Catcher.」"
"2190" = "「Vậy mà, nếu như họ đã loại bỏ \\x%lタブレット;#00ffc040;máy tính bảng%l;#;.\\nThì mục đích của Đại bãi bỏ chính là——tiêu diệt \\x%lタブレット;#00ffc040;máy tính bảng%l;#;.」"
"2205" = "「——Ư」"
"2206" = "「Ư!!?」"
"2208" = "「Nfufufufu.」"
"2222" = "「Uây~, hiếm thấy thật đấy!\\nCòn hiếm hơn cả \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Meriken nhiều đó nha~!」"
"2233" = "「À, tên bây giờ là Aki nhỉ. Mouri Aki.\\nNfufu. Mà, người đời thường gọi là Công chúa Tàu điện đấy.」"
"2238" = "「Dù có chế tạo một cơ thể mới hay làm bất cứ điều gì đi chăng nữa,\\n\\x%lタブレット;#00ffc040;máy tính bảng%l;#; cũng chắc chắn sẽ già yếu đi, và cuối cùng, sẽ phải đối mặt với cái chết không thể tránh khỏi.」"
"2241" = "「Ư!!?」\\n「!!!」"
"2259" = "「Ư!!!」"
"2283" = "「Nfufu.」"
"2284" = "「Nfufufu.」"
"2289" = "「Ufufu, được cô khen ngợi em thấy rất vinh hạnh.\\nNhưng mà, tất cả đều là nhờ vào năng lực và sự nỗ lực của ngài Soutetsu đấy.」"
"2292" = "「Nfufu, vậy cũng được thôi, cô Hachiroku.\\nNếu vậy, tôi cũng sẽ thay đổi nội dung yêu cầu nhé.」"
"2315" = "「Thời kỳ hoàng kim của Teitetsu. \\x%lレイルロオド;#00ffc040;Railord%l;#; chỉ là linh kiện bảo đảm an toàn tiêu hao.\\nLà luận văn vào cái thời mà chẳng có ai nghĩ đến việc kéo dài tuổi thọ cho các cô cả.」"
"2328" = "「Ể!? Soutetsu, cậu không phải là fan cuồng đường sắt sao!?\\nThế mà cậu lại là chủ tàu, rồi còn làm \\x%l機関士;#00ffc040;Lái tàu%l;#; nữa á!?」"
"2340" = "「Chị Olivy……\\nđã tồi tệ đến mức đó rồi sao ạ?」"
"2416" = "「Tốt lắm. Vậy thì, tôi có thể tiến hành phân tích và sao chép\\n\\x%lタブレット;#00ffc040;máy tính bảng%l;#; của cô Hachiroku được chứ?」"
"2451" = "「Tôi là \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của 8620 thuộc Đường sắt Ohitoyo,\\nHachiroku. Xin được chiếu cố ạ.」"
"2460" = "「Tôi tin vào phán đoán của em.\\nTôi muốn chính em hãy suy nghĩ xem điều gì là tốt nhất cho em và Olivy.」"
"2462" = "「Tôi nghĩ, chắc chắn là có khả năng đó.\\nGiữa tôi và Hachiroku——không, Suzu——giữa tôi và em.」"
"2465" = "「Hình hài con người, tôi nghĩ là để trong trường hợp khẩn cấp có thể\\nđóng vai trò thay thế cho \\x%l機関士;#00ffc040;Lái tàu%l;#; và \\x%l機関助士;#00ffc040;phụ lái tàu%l;#;.」"
"2488" = "「\\x%lレイルロオド;#00ffc040;Railord%l;#; là một sự tồn tại ưu việt. Thực tế là ở Hinamoto hiện tại,\\ncác \\x%lレイルロオド;#00ffc040;Railord%l;#; đã nghỉ hưu đang hoạt động sôi nổi ở khắp mọi nơi——Ư!」"
"2493" = "「Nói cách khác, \\x%lタブレット;#00ffc040;máy tính bảng%l;#; chỉ có ở một nơi duy nhất——\\nkhông, nếu nói một cách chính xác hơn, thì có lẽ là」"
"2507" = "「Nếu vậy, hoàn toàn không cần thiết phải\\nloại bỏ \\x%lタブレット;#00ffc040;máy tính bảng%l;#; khỏi Navi Aircra. Vậy mà」"
"2532" = "「Là \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; của Minh Quốc sao.」"
"2547" = "「Quả nhiên là vậy sao. Cảm ơn cô đã cho tôi biết.」"
"2551" = "「Như tôi đã nói lúc nãy, Navi Aircra và \\x%lタブレット;#00ffc040;máy tính bảng%l;#;,\\nvốn dĩ nên là những thứ cùng tồn tại với nhau.」"
"2564" = "「Là thứ trú ngụ bên trong \\x%lタブレット;#00ffc040;máy tính bảng%l;#; sao ạ?」"
"2606" = "「Thế nhưng, thực tế là \\x%lタブレット;#00ffc040;máy tính bảng%l;#; đã bị loại bỏ.\\nThậm chí, nguồn cung cấp duy nhất của nó cũng đã bị đóng lại.」"
"2632" = "「Tại vì, ngày xưa ấy? Những nơi như Teitetsu là doanh nghiệp nhà nước,\\nnên có vẻ cũng có những người tìm đến đường sắt vì muốn sự ổn định.」"
"2636" = "「Đương nhiên, công ty \\x%lレイルロオド;#00ffc040;Railord%l;#; Tablet cũng bị đóng cửa và giải thể.\\nBởi vì công nghệ chế tạo \\x%lタブレット;#00ffc040;máy tính bảng%l;#; đã hoàn toàn bị thất truyền.」"
"2644" = "「Tororyu-yu——Cựu kỹ quan Toro!\\nÀ, nhắc mới nhớ, bà ấy đang sống ở Ohitoyo nhỉ.」"
"2731" = "「Một cơ chế không hề có từ thế hệ thứ nhất trở đi.\\nNói cách khác, là Navi Aircra có chứa \\x%lタブレット;#00ffc040;máy tính bảng%l;#; bên trong.」"
"2759" = "「Fufun?」"
"2816" = "「Là bộ gạt vật cản nhô nhọn ra phía trước, đặc trưng của \\x%l蒸機;#00ffc040;Đầu máy hơi nước%l;#; kiểu cũ của Minh Quốc.\\nĐó chính là Cow Catcher ạ.」"
"2839" = "「Ư!!!?」"
"2842" = "「Tôi đã chứng kiến. Công việc của Hibiki. Thiết kế là,\\nbiến những cách bố trí tưởng chừng như không thể thành có thể thông qua việc sắp xếp lại.」"
"2866" = "「Trước khi tháo \\x%lタブレット;#00ffc040;máy tính bảng%l;#; ra, cô ấy vẫn đang hoạt động sao?」"
"2894" = "「Nếu vậy, mức độ mở hoàn toàn là——đúng như nghĩa đen,\\ntất cả những gì bên trong \\x%lタブレット;#00ffc040;máy tính bảng%l;#;——\\x%l共感;#00ffc040;cộng cảm%l;#; toàn bộ lĩnh vực, sao?」"
"2916" = "「Ngài Soutetsu là vì Ohitoyo. Và, một phần nào đó,\\nlà vì em——nên mới trở thành \\x%l機関士;#00ffc040;Lái tàu%l;#; hơi nước ạ.」"
"2943" = "「Do——Doc, tor……Phoe, nix. Hì hì.」"
"3209" = "Ngay cả khi vận hành \\x%l運転体;#00ffc040;thân vận hành%l;#;, việc bắt buộc phải đặt \\x%l整備体;#00ffc040;thân bảo trì%l;#; bên trong buồng lái,\\nchính là minh chứng rõ ràng nhất cho điều đó."
"3241" = "Nhưng, nếu việc giải trừ phong ấn là chìa khóa.\\nThì việc sao chép, hay sáng tạo ra \\x%lタブレット;#00ffc040;máy tính bảng%l;#; vốn được cho là bất khả thi hiện nay——"
"3266" = "Những ngón tay của Hachiroku đưa lên trước ngực——\\nnhư đang bấu chặt lấy \\x%lタブレット;#00ffc040;máy tính bảng%l;#; của mình."
"3447" = "Tổng tài đầu tiên của Teitetsu được phát hiện đã tử vong do bị tàu cán vào một đêm mưa giữa khuya.\\nĐó là một vụ án mạng, hay chỉ là một tai nạn, sự thật đó cho đến nay vẫn——Ư!"
"3463" = "Những thông tin về tôi và Hachiroku, cho đến cả những chi tiết khá nhỏ nhặt,\\ncó lẽ đã được Công chúa Tàu điện truyền đạt lại rồi."
"3475" = "Một tầng hầm mờ tối và lạnh lẽo.\\nNhà chứa xe……không, gọi là nhà kho thì đúng hơn."
"3510" = "Tôi nhớ đến \\x%lレイルロオド;#00ffc040;Railord%l;#; của đền chủ Akai——Niiroku.\\nNghe nói cô ấy đã đánh mất \\x%l整備体;#00ffc040;thân bảo trì%l;#; của mình——"
"3581" = "Nhưng đường sắt đã phát triển\\nvượt xa so với những gì Trevithick tưởng tượng."
"3633" = "Tên thật. Chắc hẳn là cái tên mà Công chúa Tàu điện đã cho chúng tôi biết,\\ncái tên 『Hiyoko』."
"3663" = "Sững sờ——kinh ngạc——không, còn trống rỗng hơn cả những từ ngữ đó——\\nA, đúng rồi. Một biểu cảm như người mất hồn——Ư!!?"
"3705" = "Chuỗi ký tự đó, chính là cách đối xử với \\x%lレイルロオド;#00ffc040;Railord%l;#; theo kiểu Teitetsu,\\ntrong một thời gian gần đây, tôi cũng đã phần nào hiểu được."
"3759" = "（A. Nếu vậy thì cái tên 『Momiji』 lúc nãy——\\ncũng giống như một biệt danh của Công chúa Tàu điện sao?）"
```
