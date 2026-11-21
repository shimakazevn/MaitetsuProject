## ハチロク02 — ハチロク02_8620運転台通信.txt.toml — 17/336 (5,1%)

- File: `ハチロク02_8620運転台通信.txt.toml` — route 01_Hachiroku, 336 dòng script (độc thoại 132, Soutetsu 63, Hachiroku 46, Điện xa Công chúa 31, Fukami 22, Nagi 21, Hibiki 14, Paulette 4, Reina 2, chim sẻ 1). Nội dung: họp trực tuyến với Điện xa Công chúa Mouri Aki — đặt mua dài hạn bản tin '8620運転台通信' (miễn phí trọn đời), hứa tặng một toa hành khách trong 2 tuần, mời cả nhóm đến Hiroshima; xen kẽ giải thích kỹ thuật buồng đốt/ống lò hơi/thân lò/buồng khói, bữa ăn Nagi–Fukami mang đến, và vụ nhầm 'chop' với 'chip' (tiền tip).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 336/336 (sau chuẩn hoá `\n`). `[selections]` rỗng. Không có bản sao file này (md5 `9ffb338bd09ef4a09ec44ee58a3ab01a`).
- Phân loại (17): thuật ngữ 5 (71, 1917 市電 gloss 'nguồn điện chính'→'tàu điện thành phố' + 町 'thành phố'→'thị trấn'; 1741, 2766 冥国 'nước Mỹ'→'Minh Quốc'; 2535 整備ボディ 'thân chính'→'thân bảo trì'), gasp っ 5 (1465 sweep sót — 「っ――」→'Ư——'; 1837, 2261, 2272, 2282 từ sweep, nhận nguyên văn), đại từ 2 (1951 Paulette 双鉄くん 'cậu Soutetsu'→'anh Soutetsu' theo khóa B4; 2230 Soutetsu 'tôi'→'anh' — trả lời Fukami key 2009), dịch sai 2 (1906 体育会系ノリ 'động chân động tay… chủ nghĩa thể thao'→'đáp lễ kiểu dân thể thao'; 2222 bỏ 'ái chà' bịa thêm sau さくさく――っと), bỏ sót 1 (1940 [うちの子,3] → thêm 'nhà mình'), lỗi chính tả 1 (1945 'trĩu trĩt'→'trĩu trịt'), SFX 1 (2415 けらけら 'cười khúc khích'→'cười ha hả').
- Sweep kiểm chứng: 4 mục cho file này (1837, 2261, 2272, 2282) đều đúng, đã nhận; sweep sót 1 mục (1465). Không còn っ thô trong VN; thẻ %l cân bằng JP = VN ở mọi dòng.
- Đại từ đúng toàn file: Soutetsu 'anh' với Hibiki/Nagi/Fukami, 'tôi' với Điện xa Công chúa; Hachiroku tự xưng 'em' nhất quán; Nagi→Fukami 'bé' đúng (1954).
- Chi tiết đầy đủ: `audit-hachiroku02-REVIEW.md`; danh sách sửa: `audit-hachiroku02-wrong.json` (17 mục, khối TOML 17 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 17/17; lượt soát 2: 17/17, 0 bỏ, 7 sửa — khôi phục dấu 「」 bị mất ở 1741, 1906, 1940, 1945, 1951, 2222, 2230).

**Tổng cộng sau file này: 114 file / 5.308 dòng sai** (cơ sở 113 file / 5.291 dòng sai + 17 file này)
- REBASE: cơ sở giao lúc spawn là 112 file / 5.258 dòng sai đã cũ — trong lúc audit, file 凪ふかみ01 đã gộp xong (+33) nên ROUTE-AUDIT.md hiện kết ở 113/5.291; snippet dùng cơ sở này (đã kiểm chứng trực tiếp với ROUTE-AUDIT.md).

- Chờ Hieu: 1849 ひゃわっ 'Hyawa' (xung đột ひあ/ひゃ toàn dự án); 1952 Soutetsu 'anh' vs 'tôi' (địa chỉ mơ hồ: Hachiroku hay nhóm Nagi/Fukami); 1960 Nagi 'ông nội' (câu hỏi ông nội/ông ngoại đang chờ chốt); 2049 Fukami 'Chào em' (người được chào không rõ). Lưu ý: 2 dòng 市電 71/1917 đã sửa tại đây nên gạch khỏi danh sách chờ đợt thống nhất.

```toml
[script]
"71" = "Nếu là \\x%l市電;#00ffc040;tàu điện thành phố%l;#;, thì đường ray chắc chắn sẽ chạy len lỏi giữa các khu phố.\\nKhói do \\x%l8620;#00ffc040;8620%l;#; nhả ra sẽ nhuộm đen cả thị trấn mất."
"1465" = "「Ư——」"
"1741" = "「Tuy nhiên, Minh Quốc sau chiến tranh đã trở thành một quốc gia tuyệt vời.\\nTổng thống của đất nước đó là một người xuất chúng ạ.」"
"1837" = "「Ư!」"
"1906" = "「Hô. Ở phương Tây cũng có kiểu——\\nđáp lễ kiểu dân thể thao à.」"
"1917" = "「Là do muội than——khói mù mịt thải ra từ ống khói ạ.\\nVì em được biết Đường sắt Điện Hiroshima là \\x%l市電;#00ffc040;tàu điện thành phố%l;#; ạ.」"
"1940" = "「Nếu cứ lặp đi lặp lại như vậy, mọi người sẽ biết đến 8620 nhà mình,\\nmột cách rộng rãi và sâu sắc hơn nhỉ.」"
"1945" = "「Sẽ còn đen hơn nữa cơ ạ, ngài Soutetsu. Rồi sẽ đến lúc, trên những ô cửa sổ cao kia,\\nđàn chim sẻ đen như nhuộm mực sẽ đậu trĩu trịt cho xem.」"
"1951" = "「Nhắc mới nhớ, anh Soutetsu.\\nCông chúa đang gọi anh đấy.」"
"2222" = "「Công nhận……ngon thật.\\nBánh mì thì dai mềm, thịt cốt lết thì giòn rụm——.」"
"2230" = "「Không phải đồ trang trí đâu. Tay cầm đó dùng để vặn mở đấy.\\nLần đầu tiên nhìn thấy, anh cũng ngạc nhiên lắm.」"
"2261" = "「Ư!!」"
"2272" = "『「Hả~~Ư!」\\n「Hả~~Ư!」』"
"2282" = "『「Ư!!?」\\n「A.」』"
"2415" = "Chẳng hiểu sao, Nagi lại cười ha hả.\\nCòn Fukami thì lấy hai tay che miệng, mắt sáng rực nhìn chúng tôi."
"2535" = "Từ trong màn hình được chia nhỏ, tôi bị Hibiki với khuôn mặt đen thui giống mình,\\nvà Hachiroku vừa thay thân bảo trì trắng trẻo mắng mỏ."
"2766" = "Một bà cụ người Minh Quốc hay người Anh,\\nlại đi tặng \"cú chặt\" để tỏ ý khen ngợi sao——"
```
