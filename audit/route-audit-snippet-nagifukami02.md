## 凪ふかみ02 — 凪ふかみ02_凪の大会初挑戦！.txt.toml — 32/517 (6,2%)

- File: `凪ふかみ02_凪の大会初挑戦！.txt.toml` — route 07_Nagi_Fukami, 517 dòng script (115 thoại Nagi, 102 thoại Fukami, 83 thoại Soutetsu, 5 thoại Nakamura, 3 thoại trọng tài, 209 độc thoại Fukami). Nội dung: Nagi dự giải kiếm đạo lần đầu — Soutetsu huấn luyện, Fukami kể chuyện/hỗ trợ hậu cần; xung đột Thể Xá Lưu vs luật kiếm đạo (cấm thể thuật, cấm đâm, cấm chém chéo; chỉ được Trung Đoạn/Chính Nhãn); tập luyện trong bụi tre, sát khí.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối 517/517 (287 dòng chỉ khác ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng). `[selections]` rỗng. Thẻ `%l` JP vs VN bằng nhau ở mọi dòng, 0 lệch. Không có bản sao file này (md5 `25803e1c333ba074a159e5e9f7d60aa1`).
- Phân loại (32): pronoun 21 (độc thoại Fukami "tôi"→"mình" 18 dòng: 2674, 2686, 2857, 2880, 2941, 2942, 2997, 3001, 3011, 3024, 3026, 3083, 3151, 3201, 3205, 3212, 3220, 3230; Soutetsu "tôi"→"anh" 3 dòng: 1508, 2243, 2248), gasp 5 (1470, 1471, 2082, 2688, 2771 — cả 5 từ sweep), terminology 3 (1962, 2482 "Taisha"→"Thể Xá Lưu"; 2429 "Seigan"/"Daijodan"→"Chính Nhãn"/"Đại Thượng Đoạn"), sfx 2 (2042 ぴきゃうっ "Ái da"→"Á!!", 2852 けらけら "cười khúc khích"→"cười ha hả"), consistency 1 (1511 "kami"→"kami-chan", khớp 1473).
- Sweep kiểm chứng: 5 mục cho file (1470, 1471, 2082, 2688, 2771), áp nguyên cả 5 sau khi kiểm chứng JP (lưu ý: fix của sweep cho 2771 dùng khoảng trắng thay cho `\n` của CSV3 — bản sửa đã giữ nguyên `\n` theo CSV3); tự quét toàn bộ っ không phát hiện gasp nào sweep bỏ sót.
- Soutetsu "anh" với Nagi/Fukami đúng toàn file trừ 3 dòng "tôi" đã sửa. Nagi gọi Fukami "cậu" (4 lần), không có "chị". Fukami tự xưng "tớ"/"mình" trong thoại giữ nguyên biến thể (tiền lệ 01/08b). 日ノ本→"Hinomoto" 1/1 đúng (2287); 残心→"tàn tâm" khớp tiền lệ 08a; 忠等部 là lỗi chính tả trong JP gốc (2134, 2331), VN dịch đúng, không sửa.
- Chi tiết đầy đủ: `audit-nagifukami02-REVIEW.md`; danh sách sửa: `audit-nagifukami02-wrong.json` (32 mục, khối TOML 32 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 32/32; lượt soát 2: 32/32, 0 bỏ, 0 sửa).

**Tổng cộng sau file này: 119 file / 5.581 dòng sai** (cơ sở 118 file / 5.549 dòng sai + 32 file này)

- Chờ Hieu: 次元流 → "Thứ Nguyên Lưu" hay "Thị Hiện Lưu"? (2280, 2377, 3109 — cả 3 dòng 次元流 trong toàn dự án đều ở file này; JP viết 次元流 đọc じげん, TW dùng 示現流); Nagi tự xưng trong thoại có thống nhất "tớ"/"mình"/"em" không (1862 "em" với Fukami; các dòng "tớ" 2026/2034/2123/2193/2205/2360/2363); 1491 đuôi って bỏ lửng ("——sao." hay "——thì…"); 2079 câu nói ngọng của Nagi (có giữ VN cũ "trả đũa lại nè, há miệng ra nào" không).
- Đính chính: ghi chú "Seki key 2299 dùng 'ông ngoại'" trong brief bị gán nhầm file — dòng Seki thật sự nằm ở file **凪ふかみ02_命の重さ.txt.toml key 2299**, không phải file này (file này không có dòng nào nhắc tới Seki; key 2299 ở đây là thoại Soutetsu không liên quan tới ông). Việc sửa "ông ngoại" thuộc về file 命の重さ khi tới lượt audit nó.

```toml
[script]
"1470" = "「——Ư」"
"1471" = "「——Ư」"
"1508" = "「……Gì đây, chỉ có mình anh bị cho ra rìa sao.」"
"1511" = "「……kami-chan? Fukami-chan ơiii!!」"
"1962" = "「Hiện tại thì cũng tạm ổn, nhưng ở hiệp thứ hai vừa nãy,\\nthói quen của phái Thể Xá Lưu đã bộc lộ. Em đã vác kiếm lên vai phải khi vung đấy.」"
"2042" = "「Á!!」\\n「Anh Soutetsu!」"
"2082" = "「Ư!!」"
"2243" = "「Anh không phiền đâu.\\n——Navi cũng nói là rất sẵn lòng đấy.」"
"2248" = "「Ừm. Từ giờ anh sẽ luyện tập với Nagi, nhưng mà——」"
"2429" = "「Kết hợp với bước chân, từ thế Chính Nhãn vung kiếm lên Đại Thượng Đoạn.\\nRồi không dừng lại mà đánh thẳng vào mặt thì kiếm của Nagi mới phát huy được.」"
"2482" = "「Căn bản và cũng là tuyệt kỹ của phái Thể Xá Lưu là chém chéo từ tư thế mở nửa người sang phải.\\nNhưng vì đó là đòn cấm, nên đường kiếm của Nagi bị hạn chế.」"
"2674" = "Nhưng bây giờ thì mình đã hiểu."
"2686" = "Thế rồi, nỗi sợ hãi tan biến đi mất.\\nBây giờ, chuyện gì vừa xảy ra……dù sợ, nhưng mình vẫn muốn biết."
"2688" = "Một mạch vung kiếm lên cao, rồi cứ thế lao vào đối thủ——Ư!?"
"2771" = "Bán khai, chắc có nghĩa là mở một nửa.\\nCơ thể của Nagi, đúng như cái tên, xoay nửa người lại——Ư!"
"2852" = "Nagi làm vẻ mặt giật mình,\\nrồi cười ha hả."
"2857" = "Góc nghiêng ấy, khiến mình thoáng chốc mê mẩn.\\nThật tĩnh lặng, thật xinh đẹp——ngay cả những giọt mồ hôi cũng lấp lánh như ngọc vậy."
"2880" = "Nếu chưa nhìn thấy Nagi-chan của ngày hôm nay,\\nchắc chắn mình đã thắc mắc \"Biện pháp an toàn á?\"."
"2941" = "Nagi-chan vốn rất khó chịu với điều đó, nhưng trọng tài đã tách họ ra——\\nNên mình đinh ninh rằng thế này là nắm chắc phần thắng rồi."
"2942" = "Không có tiếng đáp lại. Làm sao mà trả lời được cơ chứ.\\nNhưng mình biết, Nagi-chan vẫn nghe thấy rất rõ."
"2997" = "Mình ngồi thụp xuống!\\nSợ hãi vì nghĩ có thứ gì đó sắp tới, cơ thể mình cứng đờ không cử động nổi!"
"3001" = "Mình cũng vậy.\\nMình đã thở phào nhẹ nhõm."
"3011" = "Mình và Nagi-chan chợt chạm mắt nhau.\\nCùng gật đầu."
"3024" = "Qua giọng nói của anh Soutetsu, mình cũng cảm nhận được.\\nQuả nhiên, đây chính là cơ hội!!"
"3026" = "Việc mà mình có thể giúp.\\nHộp cứu thương, chanh ngâm mật ong, và nước uống thể thao."
"3083" = "Dù là việc nhỏ nhặt đến đâu,\\nmình tin chắc chắn cũng có việc mình có thể giúp được."
"3151" = "Bị nói là bắt bài...\\nlàm mình có cảm giác rất không lành."
"3201" = "Xoạt, âm thanh như dẫm lên lá khô.\\nPhù, tiếng thở hắt ra. Những âm thanh quen thuộc với đôi tai mình."
"3205" = "Chừng đó thì, mình cũng biết.\\nLà nói về tay, về cổ tay——Nhưng mà!"
"3212" = "Rất đáng sợ, chỉ cần chậm một giây thôi là sẽ bị đánh trúng,\\nnếu là mình, tuyệt đối không thể làm được."
"3220" = "Dù không hiểu các thuật ngữ chuyên môn,\\nnhưng mình cũng thấy rõ Nagi-chan đánh rất đẹp mắt!"
"3230" = "Quả không hổ danh là anh Soutetsu.\\nHình như mình cũng hiểu ra rồi."
```
