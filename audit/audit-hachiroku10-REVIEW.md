# Audit — ハチロク10_旺宮鉄道歴史館.txt.toml (01_Hachiroku)

## Tổng quan

- File: `ハチロク10_旺宮鉄道歴史館.txt.toml` — route 01_Hachiroku, **572 dòng script** (độc thoại 196, Soutetsu 124, ひよこ 117, Hachiroku 99, Olivy 36).
- Nội dung: Soutetsu, Hachiroku và Olivy thăm Bảo tàng Lịch sử Đường sắt Oukyou (旺宮鉄道歴史館), gặp tiến sĩ Fushicho (不死鳥博士, biệt danh 'Hiyoko') — bà là giám đốc thực chất của bảo tàng/viện nghiên cứu. Bà giải thích về タブレット, 共感 (cộng cảm) ở mức độ mở hoàn toàn, lịch sử Stephenson/Trevithick, Đại bãi bỏ tuyến đường sắt (大廃線), sự kiện Ueyama, và đề nghị Soutetsu–Hachiroku trình diễn cộng cảm toàn phần cùng cân nhắc giúp khởi động lại Toyo đang đóng băng; Olivy được kiểm tra có ý thức. Xen kẽ: đầu máy Toyo (Porter, Minh Trị 12), Cow Catcher, tuyến đường sắt Isumi.
- Phương pháp: đọc từng dòng đối chiếu JP + TW từ CSV3 (Trang tính 3), kiểm chứng chéo sweep っ, kiểm tra cơ học trùng khóa/trùng VN/thẻ %l/dòng chưa dịch/dòng VN==TW.
- **Kết quả: 572 dòng đọc, 65 dòng sai (11,4%).**
- Phân loại (65): thuật ngữ 36 (タブレット 19: 1479, 1488, 2113, 2146, 2184, 2190, 2238, 2416, 2493, 2507, 2551, 2564, 2606, 2636, 2731, 2866, 2894, 3241, 3266; Ohitoyo 5: 2152, 2328, 2451, 2644, 2916; Teitetsu 3: 2315, 2632, 3705; 電車姫 4: 2233, 3463, 3633, 3759; 冥国 2: 2222, 2532; 運転体 2: 2146, 3209; 整備体 3: 2146, 3209, 3510; 宮司 1: 3510; 機関士 1: 2465 — 2146/3209/3510 mang nhiều lỗi thuật ngữ trong một dòng), đại từ 9 (Soutetsu 'anh'→'tôi' 7: 2007, 2010, 2187, 2460, 2462, 2547, 2842; Hachiroku 2: 2289, 2340), gasp っ 9 (8 từ sweep: 2062, 2205, 2206, 2241, 2259, 2839, 3447, 3663; 1 sweep phân loại sai: 2488), SFX 6 (tiếng cười diễn thành tiếng rên 5: 2208, 2283, 2284, 2292, 2759; くすっ 1: 2943), dịch sai 3 (2019, 2181, 3475), thẻ %l 1 (2816), lỗi đánh máy 1 (3581).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất (không có set trùng/stale). VN khớp TOML sau chuẩn hoá `\n` (354 dòng chênh lệch chỉ là `\n` bị TOML-2 dẹp thành khoảng trắng — đã biết, CSV3 là chuẩn). `[selections]` có tiêu đề nhưng rỗng (0 mục). Không có bản sao của file này (md5 `4326168a59b6c3b615098e40471f3923`, không trùng md5 với file nào khác trong sources/toml2).
- Đại từ đã kiểm chứng toàn file: Soutetsu 'tôi' đúng với Hachiroku (2230, 2280, 2311, 2352, 2436, 2441, 2465, 2542, 2584) và với tiến sĩ Fushicho (toàn bộ các dòng đối thoại với bác sĩ), 'anh' đúng với Olivy (2275, 2302 — tiền lệ file ハチロク05 đã duyệt: Soutetsu→Olivy 'anh'/'em'); Hachiroku tự xưng 'em' nhất quán (trừ 2289 đã sửa); Hachiroku gọi tiến sĩ Fushicho 'cô' (2496); Olivy gọi Soutetsu 'cậu' giữ nguyên (2328, tiền lệ đã duyệt); độc thoại Soutetsu xưng 'Tôi' nhất quán.

## Kiểm chứng sweep っ

- Sweep có **9 mục** cho file này trong `sweep-raw-gasp-wrong.json`: 8 fix (2062, 2205, 2206, 2241, 2259, 2839, 3447, 3663) + 1 already-rendered (2488). Cả 8 fix đều kiểm chứng đúng với JP, đã nhận nguyên văn.
- Sweep **phân loại sai 1 mục**: key 2488 (JP 「活躍――っ！」) bị ghi already-rendered, nhưng cùng mẫu っ cuối sau dấu gạch như 3447/3663 trong chính file này (sweep sửa cả hai thành ——Ư!); VN '——!' chỉ giữ dấu câu vốn đã có trong JP, không diễn tiếng gasp っ — đã sửa thành '——Ư!' và ghi chú để parent kiểm chứng.
- Các っ còn lại trong file đã rà bằng máy (JP chứa っ mà VN không có Ư): toàn bộ là っ trong từ (～ている, ちょっと, すっ, ぱっと…), っ cuối nhấn mạnh gắn với từ nội dung (さまっ 2249, ごめんっ 2264, あのっ 2762 — không thêm Ư theo quy tắc), hoặc あっ/ぁぁっ đã diễn thành 'A'/'A a' theo đúng quy ước của sweep (mục 1195, 2282, 2461). Không còn gasp nào bị mất.
- Thẻ %l: số lượng `%l` JP = VN ở mọi dòng trừ 2816 (đã sửa — xem chi tiết). Không có thẻ thiếu dấu `;` hay thẻ lệch nào trong file này.
- Trùng VN: 9 nhóm VN trùng nhau trong file đều là câu ngắn lặp lại hợp lệ (「Ồ.」×4, 「A——」×3, 「Ừm.」×2, 「!」×2, （Vút）×2, 「Oa.」×2, 「Hư hừ hừ hừ.」×2 — là 2208 + 2284, đã sửa khác nhau, 「Vâng.」×2, 'Hachiroku khẽ gật đầu một cái.'×2 cho 2 JP gần giống nhau) — không phải lệch dòng.

## Chi tiết từng dòng sai (65)

### key 1479 — 双鉄 — terminology

- JP: 「\x%lタブレット;#00ffc040;タブレット%l;#;の――魂の自己複製。ないしは繁殖の機能。\nそこに為された封印を、開封するためなのではないかと」
- TW: 「\x%lタブレット;#00ffc040;操作板%l;#;具備——複製靈魂，或者是繁衍後代的能力。而封印也或許正是為此而設的」
- VN cũ: 「Khả năng tự sao chép của \x%lタブレット;#00ffc040;thẻ bảng%l;#;——của linh hồn. Hoặc là chức năng sinh sản.\nChẳng phải là để giải trừ phong ấn được đặt trên đó sao.」
- VN mới: 「Khả năng tự sao chép của \x%lタブレット;#00ffc040;máy tính bảng%l;#;——của linh hồn. Hoặc là chức năng sinh sản.\nChẳng phải là để giải trừ phong ấn được đặt trên đó sao.」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 1488 — ひよこ — terminology

- JP: 「\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の各種法定検査は、\n全て\x%lタブレット;#00ffc040;タブレット%l;#;を外され、非・起動状態で行われますな」
- TW: 「\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的各項法定檢查，均要取下\x%lタブレット;#00ffc040;操作板%l;#;，於關機狀態實行」
- VN cũ: 「Các loại kiểm tra theo luật định của \x%lレイルロオド;#00ffc040;Railord%l;#;,\ntất cả đều được tiến hành trong trạng thái tháo \x%lタブレット;#00ffc040;thẻ bảng%l;#;, tức là trạng thái không khởi động.」
- VN mới: 「Các loại kiểm tra theo luật định của \x%lレイルロオド;#00ffc040;Railord%l;#;,\ntất cả đều được tiến hành trong trạng thái tháo \x%lタブレット;#00ffc040;máy tính bảng%l;#;, tức là trạng thái không khởi động.」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 2007 — 双鉄 — pronoun

- JP: 「いや、そこを謙遜されては寂しい。ハチロクがいて、\n僕がいて――僕らはふたりで、ここまで来たのだから」
- TW: 「不不，你如此謙虛反倒見外了，這一切都是你我——我們共同努力的成果」
- VN cũ: 「Không đâu, em khiêm tốn như vậy làm anh buồn đấy. Có Hachiroku,\nvà có anh——hai chúng ta đã cùng nhau, đi đến tận bước đường này mà.」
- VN mới: 「Không đâu, em khiêm tốn như vậy làm tôi buồn đấy. Có Hachiroku,\nvà có tôi——hai chúng ta đã cùng nhau, đi đến tận bước đường này mà.」
- Lý do: Soutetsu tự xưng 'anh' với Hachiroku — sai quy tắc đã sửa: Soutetsu là 'tôi' với Hachiroku (cô gọi cậu là 双鉄様 / 'ngài Soutetsu'). Dòng kề 2006 Hachiroku đang nói với Soutetsu; gọi Hachiroku 'em' giữ nguyên.

### key 2010 — 双鉄 — pronoun

- JP: 「いや、その発言もどうかと思うぞ」
- TW: 「不不，你這話問題也不小」
- VN cũ: 「Không, anh thấy câu nói đó của em cũng có vấn đề đấy.」
- VN mới: 「Không, tôi thấy câu nói đó của em cũng có vấn đề đấy.」
- Lý do: Soutetsu tự xưng 'anh' với Hachiroku (câu này đáp lời Hachiroku ở 2006–2007) → 'tôi' theo quy tắc đã sửa; 'em' cho Hachiroku giữ nguyên.

### key 2019 — オリヴィ — meaning

- JP: 「ほしいもなにも、一度みたらわすれっこないよー！\nよろしくね、ドクター・フェニックス！」
- TW: 「不用說，奧莉薇就是想忘也忘不掉啦！請多關照，Ｄｏｃｔｏｒ　Ｐｈｏｅｎｉｘ！」
- VN cũ: 「Chiếu cố gì chứ, nhìn thấy một lần là không thể nào quên được luôn đó~!\nMong được giúp đỡ nha, Doctor Phoenix!」
- VN mới: 「Dù muốn hay không, nhìn thấy một lần là không thể nào quên được luôn đó~!\nMong được giúp đỡ nha, Doctor Phoenix!」
- Lý do: ほしいもなにも = 'dù muốn hay không' — VN cũ 'Chiếu cố gì chứ' bịa nghĩa, không có trong JP (よろしくね chỉ có ở câu sau, đã dịch đúng 'Mong được giúp đỡ nha').

### key 2062 — 双鉄 — gasp

- JP: 「っ！！？」\n「！！」
- TW: 「什麼！！？」\n「這！！」
- VN cũ: 「!!?」\n「!!」
- VN mới: 「Ư!!?」\n「!!」
- Lý do: Sweep lost-gasp (whole/trailing), đã kiểm chứng đúng JP/TW — nhận nguyên văn fix của sweep.

### key 2113 — ひよこ — terminology

- JP: 「世界中、全ての\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の\x%lタブレット;#00ffc040;タブレット%l;#;は、\nただ一箇所の工場から出荷されていました」
- TW: 「全世界，一切\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的\x%lタブレット;#00ffc040;操作板%l;#;，均產自同一座工廠」
- VN cũ: 「Trên toàn thế giới, \x%lタブレット;#00ffc040;thẻ bảng%l;#; của tất cả các \x%lレイルロオド;#00ffc040;Railord%l;#;,\nđều được xuất xưởng từ một nhà máy duy nhất.」
- VN mới: 「Trên toàn thế giới, \x%lタブレット;#00ffc040;máy tính bảng%l;#; của tất cả các \x%lレイルロオド;#00ffc040;Railord%l;#;,\nđều được xuất xưởng từ một nhà máy duy nhất.」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 2146 — ひよこ — terminology

- JP: 「\x%l運転体;#00ffc040;運転体%l;#;からも\x%l整備体;#00ffc040;整備体%l;#;からも\x%lタブレット;#00ffc040;タブレット%l;#;を外し、安置。\nその状態が、もう……かれこれ四年以上になりますかな」
- TW: 「卸下\x%lタブレット;#00ffc040;操作板%l;#;，並與\x%l運転体;#00ffc040;駕駛體%l;#;和\x%l整備体;#00ffc040;整備體%l;#;一同進行了封存處置，掐指算來……迄今已四年有餘」
- VN cũ: 「Tháo \x%lタブレット;#00ffc040;thẻ bảng%l;#; ra khỏi cả \x%l運転体;#00ffc040;kíp lái%l;#; lẫn \x%l整備体;#00ffc040;thân chính%l;#;, rồi đem đi cất giữ.\nTrạng thái đó, đã……kéo dài được hơn bốn năm rồi thì phải.」
- VN mới: 「Tháo \x%lタブレット;#00ffc040;máy tính bảng%l;#; ra khỏi cả \x%l運転体;#00ffc040;thân vận hành%l;#; lẫn \x%l整備体;#00ffc040;thân bảo trì%l;#;, rồi đem đi cất giữ.\nTrạng thái đó, đã……kéo dài được hơn bốn năm rồi thì phải.」
- Lý do: Một dòng 3 lỗi thuật ngữ: タブレット 'thẻ bảng' → 'máy tính bảng'; 運転体 'kíp lái' → 'thân vận hành' (kíp lái là kíp người, đây là thân thể — tiền lệ file 09: "'kíp lái' sai, đó là thân thể không phải kíp người"); 整備体 'thân chính' → 'thân bảo trì' (thuật ngữ đã chốt).

### key 2152 — 双鉄 — terminology

- JP: 「なるほど、その一面はあるかもしれんな。\nそれがひいては、御一夜鉄道の社風にも育っていった」
- TW: 「原來如此，可能是有這層關係，並且這些觀念也進一步發揚光大，成為御一夜鐵路的風氣」
- VN cũ: 「Ra là vậy, có lẽ cũng có khía cạnh đó đấy.\nĐiều đó cuối cùng, đã nuôi dưỡng nên văn hóa công ty của Đường sắt Ohimitera.」
- VN mới: 「Ra là vậy, có lẽ cũng có khía cạnh đó đấy.\nĐiều đó cuối cùng, đã nuôi dưỡng nên văn hóa công ty của Đường sắt Ohitoyo.」
- Lý do: 御一夜 'Ohimitera' → 'Ohitoyo' theo quyết định 19/11 (furigana おひとよ).

### key 2181 — ハチロク — meaning

- JP: 「行い得ない。――得ないのでしたら、一般的な\nエアクラナビは、魂……的なものを有していない？」
- TW: 「只能——如此表述也就意味著，一般的空凝機導航……就不具備類似於靈魂的意識？」
- VN cũ: 「Chỉ có thể thực hiện. ——Nếu đã như vậy, thì các Navi Aircra thông thường,\nkhông sở hữu thứ gì đó……giống như linh hồn sao ạ?」
- VN mới: 「Không thể thực hiện được. ——Nếu đã như vậy, thì các Navi Aircra thông thường,\nkhông sở hữu thứ gì đó……giống như linh hồn sao ạ?」
- Lý do: 行い得ない = 'không thể thực hiện được' — VN cũ 'Chỉ có thể thực hiện' đảo ngược nghĩa (得ない = không thể). TW 只能 cũng lệch theo hướng đó, nhưng JP thắng TW.

### key 2184 — 双鉄 — terminology

- JP: 「逆算すればいい。『\x%lタブレット;#00ffc040;タブレット%l;#;は、知られすぎると、\n排除される性質をもつ』ということになるだろう？」
- TW: 「只需從結果反推便是。換言之，就是寧肯中止使用\x%lタブレット;#00ffc040;操作板%l;#;，也不可令其廣為人知」
- VN cũ: 「Chỉ cần suy ngược lại là được. Rằng 『\x%lタブレット;#00ffc040;Thẻ bảng%l;#; mang một bản chất\nsẽ bị loại bỏ nếu được biết đến quá rộng rãi』 đúng không?」
- VN mới: 「Chỉ cần suy ngược lại là được. Rằng 『\x%lタブレット;#00ffc040;Máy tính bảng%l;#; mang một bản chất\nsẽ bị loại bỏ nếu được biết đến quá rộng rãi』 đúng không?」
- Lý do: Gloss %l của タブレット là 'Thẻ bảng' (viết hoa đầu câu) — thuật ngữ đã chốt 'máy tính bảng'.

### key 2187 — 双鉄 — pronoun

- JP: 「とはいえ、僕はまだまだ未熟極まる。\n実際のところ、カウキャッチャーも知らなかったし」
- TW: 「可我依然多有不周到之處，就比如說剛才，我連防撞梁都不知道是什麼」
- VN cũ: 「Dù vậy, anh vẫn còn vô cùng thiếu kinh nghiệm.\nThực tế thì, anh cũng đâu biết gì về Cow Catcher.」
- VN mới: 「Dù vậy, tôi vẫn còn vô cùng thiếu kinh nghiệm.\nThực tế thì, tôi cũng đâu biết gì về Cow Catcher.」
- Lý do: Soutetsu 'anh' — dòng này nối tiếp 2184 trong cuộc thảo luận với tiến sĩ Fushicho (bác sĩ gọi Soutetsu là 右田氏; Hachiroku và Olivy chỉ nghe) → 'tôi'. 'Cow Catcher' chỉ là ví dụ cậu tự nêu về sự thiếu kinh nghiệm của mình, không phải đang nói với Olivy.

### key 2190 — 双鉄 — terminology

- JP: 「にもかかわらず、\x%lタブレット;#00ffc040;タブレット%l;#;を除去したのならば。\n大廃線の目的は――\x%lタブレット;#00ffc040;タブレット%l;#;を滅ぼすことに」
- TW: 「可現實卻是大多數空凝機導航均沒有安裝\x%lタブレット;#00ffc040;操作板%l;#;。由此可以推斷，大廢線的真正目的在於——銷毀所有\x%lタブレット;#00ffc040;操作板%l;#;」
- VN cũ: 「Vậy mà, nếu như họ đã loại bỏ \x%lタブレット;#00ffc040;thẻ bảng%l;#;.\nThì mục đích của Đại bãi bỏ chính là——tiêu diệt \x%lタブレット;#00ffc040;thẻ bảng%l;#;.」
- VN mới: 「Vậy mà, nếu như họ đã loại bỏ \x%lタブレット;#00ffc040;máy tính bảng%l;#;.\nThì mục đích của Đại bãi bỏ chính là——tiêu diệt \x%lタブレット;#00ffc040;máy tính bảng%l;#;.」
- Lý do: Gloss %l của タブレット 'thẻ bảng' → 'máy tính bảng' (2 lần trong một dòng).

### key 2205 — ハチロク — gasp

- JP: 「――っ」
- TW: 「呃——」
- VN cũ: 「——」
- VN mới: 「——Ư」
- Lý do: Sweep lost-gasp (whole/trailing), đã kiểm chứng đúng JP/TW — nhận nguyên văn fix của sweep.

### key 2206 — 双鉄 — gasp

- JP: 「っ！！？」
- TW: 「呃！！？」
- VN cũ: 「!!?」
- VN mới: 「Ư!!?」
- Lý do: Sweep lost-gasp (whole/trailing), đã kiểm chứng đúng JP/TW — nhận nguyên văn fix của sweep.

### key 2208 — ひよこ — sfx

- JP: 「んふふふふ」
- TW: 「呵呵呵呵」
- VN cũ: 「Hư hừ hừ hừ.」
- VN mới: 「Nfufufufu.」
- Lý do: んふふふふ là tiếng cười (ん + 4 ふ) — VN cũ 'Hư hừ hừ hừ' diễn thành tiếng rên, trái quy tắc 22:05 (tiếng cười diễn thành tiếng cười, không thành tiếng rên). Trong chính file này 2286/2288 đã dịch đúng 'Nfufufufufu'/'Nfufufufufufu' — sửa theo mẫu đó.

### key 2222 — オリヴィ — terminology

- JP: 「うぇぇー、めっずらしい！\n[メリケン,2]冥国式\x%lレイルロオド;#00ffc040;レイルロオド%l;#;より、よっぽどレアだよー！」
- TW: 「哇，真稀罕哎！你這種人可比[Ａｍｅｒｉｃａｎ,2]美國式\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;少見多了！」
- VN cũ: 「Uây~, hiếm thấy thật đấy!\nCòn hiếm hơn cả \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc (Mỹ) nhiều đó nha~!」
- VN mới: 「Uây~, hiếm thấy thật đấy!\nCòn hiếm hơn cả \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Meriken nhiều đó nha~!」
- Lý do: 冥国 có furigana メリケン (lời nói) → giữ 'Meriken' theo quy tắc đã chốt (furigana メリケン spoken = 'Meriken'; tiền lệ file ハチロク05 key 2605). VN cũ 'Minh Quốc (Mỹ)' dịch theo chữ Hán, mất cách đọc.

### key 2233 — ひよこ — terminology

- JP: 「ああ、今の名前はアキでしたな。毛利安芸。\nんふふっ。ま、世にいうところの電車姫ですな」
- TW: 「哦，她現在的名字是毛利安芸。嘻嘻，也就是受世人景仰的電車公主了」
- VN cũ: 「À, tên bây giờ là Aki nhỉ. Mouri Aki.\nNfufu. Mà, người đời thường gọi là Densha Hime đấy.」
- VN mới: 「À, tên bây giờ là Aki nhỉ. Mouri Aki.\nNfufu. Mà, người đời thường gọi là Công chúa Tàu điện đấy.」
- Lý do: 電車姫 → 'Công chúa Tàu điện' theo quyết định 20/11 (không dùng 'Densha Hime'/'công chúa Densha').

### key 2238 — ひよこ — terminology

- JP: 「ボディ新造をしようがなにをしようが、\n\x%lタブレット;#00ffc040;タブレット%l;#;は必ず老衰し、やがて、不可避の死を迎える」
- TW: 「哪怕更換身體，亦或是採取其他延壽手段，終究無法避免\x%lタブレット;#00ffc040;操作板%l;#;的衰老乃至死亡」
- VN cũ: 「Dù có chế tạo một cơ thể mới hay làm bất cứ điều gì đi chăng nữa,\n\x%lタブレット;#00ffc040;thẻ bảng%l;#; cũng chắc chắn sẽ già yếu đi, và cuối cùng, sẽ phải đối mặt với cái chết không thể tránh khỏi.」
- VN mới: 「Dù có chế tạo một cơ thể mới hay làm bất cứ điều gì đi chăng nữa,\n\x%lタブレット;#00ffc040;máy tính bảng%l;#; cũng chắc chắn sẽ già yếu đi, và cuối cùng, sẽ phải đối mặt với cái chết không thể tránh khỏi.」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 2241 — 双鉄 — gasp

- JP: 「っ！！？」\n「！！！」
- TW: 「唔！！？」\n「呃！！！」
- VN cũ: 「!!?」\n「!!!」
- VN mới: 「Ư!!?」\n「!!!」
- Lý do: Sweep lost-gasp (whole/trailing), đã kiểm chứng đúng JP/TW — nhận nguyên văn fix của sweep.

### key 2259 — ハチロク — gasp

- JP: 「っ！！！」
- TW: 「啊！！！」
- VN cũ: 「!!!」
- VN mới: 「Ư!!!」
- Lý do: Sweep lost-gasp (whole/trailing), đã kiểm chứng đúng JP/TW — nhận nguyên văn fix của sweep.

### key 2283 — ひよこ — sfx

- JP: 「んふふっ」
- TW: 「嘻嘻」
- VN cũ: 「Hư hừ.」
- VN mới: 「Nfufu.」
- Lý do: んふふっ (ん + 2 ふ + っ) là tiếng cười → 'Nfufu' (っ trong tiếng cười không thêm âm — mẫu 2286 trong file). VN cũ 'Hư hừ' là tiếng rên.

### key 2284 — ひよこ — sfx

- JP: 「んふふふっ」
- TW: 「嘻嘻嘻嘻」
- VN cũ: 「Hư hừ hừ hừ.」
- VN mới: 「Nfufufu.」
- Lý do: んふふふっ (ん + 3 ふ + っ) là tiếng cười → 'Nfufufu'. VN cũ 'Hư hừ hừ hừ' là tiếng rên.

### key 2289 — ハチロク — pronoun

- JP: 「うふふっ、お褒めいただき光栄です。\nけれど、全ては双鉄さまのご適正とご努力によっての」
- TW: 「嘻嘻，很榮幸獲得你這般讚賞，但雙鐵少爺能有這番成就，全是得益於過人的天分以及不懈的努力」
- VN cũ: 「Ufufu, được em khen ngợi chị thấy rất vinh hạnh.\nNhưng mà, tất cả đều là nhờ vào năng lực và sự nỗ lực của ngài Soutetsu đấy.」
- VN mới: 「Ufufu, được cô khen ngợi em thấy rất vinh hạnh.\nNhưng mà, tất cả đều là nhờ vào năng lực và sự nỗ lực của ngài Soutetsu đấy.」
- Lý do: Hachiroku tự xưng 'chị' và gọi người khen là 'em' — ngược: Hachiroku tự xưng 'em' với tiến sĩ Fushicho (tiền lệ 2350 'Em xin phép', 2364 'cho em hỏi'); bác sĩ được gọi 'cô' (tiền lệ 2496 'cô đã nhìn thấu'). Người khen ở dòng kề 2286 là tiến sĩ Fushicho.

### key 2292 — ひよこ — sfx

- JP: 「んふふっ、それで結構ですよ、ハチロク氏。\nでしたら、こちらも依頼内容を変更いたしましょうかな」
- TW: 「嘻嘻，無妨無妨。那我就另有一事有求於二位了」
- VN cũ: 「Hư hừ, vậy cũng được thôi, cô Hachiroku.\nNếu vậy, tôi cũng sẽ thay đổi nội dung yêu cầu nhé.」
- VN mới: 「Nfufu, vậy cũng được thôi, cô Hachiroku.\nNếu vậy, tôi cũng sẽ thay đổi nội dung yêu cầu nhé.」
- Lý do: んふふっ là tiếng cười → 'Nfufu'. VN cũ 'Hư hừ' là tiếng rên.

### key 2315 — ひよこ — terminology

- JP: 「帝鉄全盛期。\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は消耗保安部品。\n長寿命化など考える者もいなかった時期の、論文ですな」
- TW: 「在帝國鐵路全盛時期，\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;被定性為安全組件耗材，當時沒有人關注延長其使用壽命，而這篇論文就是那時發表的」
- VN cũ: 「Thời kỳ hoàng kim của Đường sắt Hoàng gia. \x%lレイルロオド;#00ffc040;Railord%l;#; chỉ là linh kiện bảo đảm an toàn tiêu hao.\nLà luận văn vào cái thời mà chẳng có ai nghĩ đến việc kéo dài tuổi thọ cho các cô cả.」
- VN mới: 「Thời kỳ hoàng kim của Teitetsu. \x%lレイルロオド;#00ffc040;Railord%l;#; chỉ là linh kiện bảo đảm an toàn tiêu hao.\nLà luận văn vào cái thời mà chẳng có ai nghĩ đến việc kéo dài tuổi thọ cho các cô cả.」
- Lý do: 帝鉄 → 'Teitetsu' theo thuật ngữ đã chốt; 'Đường sắt Hoàng gia' dịch sai (帝 = đế, không phải hoàng gia; tiền lệ file khác 'Đường sắt Hoàng gia → Teitetsu').

### key 2328 — オリヴィ — terminology

- JP: 「えええ！？　双鉄、マニアじゃないの！？\nなのにまいてつで、\x%l機関士;#00ffc040;機関士%l;#;してるの！？」
- TW: 「天啊！？原來你不是鐵路迷！？那你還願意當掌車人和\x%l機関士;#00ffc040;司機%l;#;！？」
- VN cũ: 「Ể!? Soutetsu, cậu không phải là fan cuồng đường sắt sao!?\nThế mà cậu lại làm \x%l機関士;#00ffc040;Lái tàu%l;#; cho Maitetsu (Đường sắt Ohimitera) á!?」
- VN mới: 「Ể!? Soutetsu, cậu không phải là fan cuồng đường sắt sao!?\nThế mà cậu lại là chủ tàu, rồi còn làm \x%l機関士;#00ffc040;Lái tàu%l;#; nữa á!?」
- Lý do: まいてつ = 'chủ tàu' theo quyết định đã chốt; TW 掌車人 xác nhận. VN cũ dịch まいてつ thành tên công ty 'Maitetsu (Đường sắt Ohimitera)' là sai — 御一夜鉄道 mới là công ty, và tên đó cũng sai thành 'Ohimitera' → 'Ohitoyo'.

### key 2340 — ハチロク — pronoun

- JP: 「オリヴィちゃんは……\nそこまで、悪いのでございますか？」
- TW: 「奧莉薇的情況……已經嚴重到這個地步了嗎？」
- VN cũ: 「Bé Olivy……\nđã tồi tệ đến mức đó rồi sao ạ?」
- VN mới: 「Chị Olivy……\nđã tồi tệ đến mức đó rồi sao ạ?」
- Lý do: Hachiroku gọi Olivy 'Bé Olivy' — sai: Olivy lớn tuổi hơn Hachiroku (bằng chứng ハチロク06 key 3455 'オリヴィは…ハチロクよりも古いのだ'; Hachiroku gọi Olivy 先輩) nên Hachiroku gọi Olivy là 'chị' (tiền lệ file ハチロク06 sửa 7 dòng Hachiroku↔Olivy).

### key 2416 — ひよこ — terminology

- JP: 「結構。では、ハチロク氏の\x%lタブレット;#00ffc040;タブレット%l;#;は\n解析・複製させてもらってかまわないかな？」
- TW: 「很好。那麼我需要解析並複製八六女士的\x%lタブレット;#00ffc040;操作板%l;#;，你們對此沒有異議吧？」
- VN cũ: 「Tốt lắm. Vậy thì, tôi có thể tiến hành phân tích và sao chép\n\x%lタブレット;#00ffc040;thẻ bảng%l;#; của cô Hachiroku được chứ?」
- VN mới: 「Tốt lắm. Vậy thì, tôi có thể tiến hành phân tích và sao chép\n\x%lタブレット;#00ffc040;máy tính bảng%l;#; của cô Hachiroku được chứ?」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 2451 — ハチロク — terminology

- JP: 「わたくしは、御一夜鉄道8620専用\x%lレイルロオド;#00ffc040;レイルロオド%l;#;、\nハチロクです。どうぞ、よろしくお願いいたします」
- TW: 「我是御一夜鐵路８６２０專用\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，名為八六，請您多多關照」
- VN cũ: 「Tôi là \x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của 8620 thuộc Đường sắt Ohimitera,\nHachiroku. Xin được chiếu cố ạ.」
- VN mới: 「Tôi là \x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của 8620 thuộc Đường sắt Ohitoyo,\nHachiroku. Xin được chiếu cố ạ.」
- Lý do: 御一夜 'Ohimitera' → 'Ohitoyo' theo quyết định 19/11 (furigana おひとよ).

### key 2460 — 双鉄 — pronoun

- JP: 「お前の判断を、僕は信じる。\nお前とオリヴィとの最善を、お前自身に考えて欲しい」
- TW: 「我相信你的判斷，希望你能完全以自己的觀點，為你和奧莉薇做出最妥當的選擇」
- VN cũ: 「Anh tin vào phán đoán của em.\nAnh muốn chính em hãy suy nghĩ xem điều gì là tốt nhất cho em và Olivy.」
- VN mới: 「Tôi tin vào phán đoán của em.\nTôi muốn chính em hãy suy nghĩ xem điều gì là tốt nhất cho em và Olivy.」
- Lý do: Soutetsu nói với Hachiroku (お前 = Suzu; dòng kề 2457 Hachiroku vừa thổ lộ) — tự xưng 'anh' sai → 'tôi'; gọi Hachiroku 'em' giữ nguyên.

### key 2462 — 双鉄 — pronoun

- JP: 「その可能性は、きっとあると、僕は思う。\n僕とハチロク――いや、すず――お前との間に」
- TW: 「我相信這個可能性一定不是零。八六——不，鈴，我們可以對此寄予希望」
- VN cũ: 「Anh nghĩ, chắc chắn là có khả năng đó.\nGiữa anh và Hachiroku——không, Suzu——giữa anh và em.」
- VN mới: 「Tôi nghĩ, chắc chắn là có khả năng đó.\nGiữa tôi và Hachiroku——không, Suzu——giữa tôi và em.」
- Lý do: Soutetsu nói với Hachiroku (すず = Suzu, tên thật của Hachiroku) — tự xưng 'anh' sai → 'tôi'; gọi Hachiroku 'em' giữ nguyên.

### key 2465 — 双鉄 — terminology

- JP: 「人の形は、緊急時には\x%l機関士;#00ffc040;機関士%l;#;、\x%l機関助士;#00ffc040;機関助士%l;#;の代役を\nつとめられるようにではないかと、考えます」
- TW: 「我認為人類之軀的意義可能在於，能夠在緊急狀況下替\x%l機関士;#00ffc040;司機%l;#;和\x%l機関助士;#00ffc040;司爐%l;#;履行職責」
- VN cũ: 「Hình hài con người, tôi nghĩ là để trong trường hợp khẩn cấp có thể\nđóng vai trò thay thế cho \x%l機関士;#00ffc040;người lái tàu%l;#; và \x%l機関助士;#00ffc040;phụ lái tàu%l;#;.」
- VN mới: 「Hình hài con người, tôi nghĩ là để trong trường hợp khẩn cấp có thể\nđóng vai trò thay thế cho \x%l機関士;#00ffc040;Lái tàu%l;#; và \x%l機関助士;#00ffc040;phụ lái tàu%l;#;.」
- Lý do: Gloss %l của 機関士 là 'người lái tàu' — không phải dạng đã chốt ('thợ lái đầu máy'; dạng ngắn trong thoại là 'lái tàu'). Trong file này 2328/2896/2916 đều dùng 'Lái tàu' nên thống nhất theo dạng đó. 機関助士 'phụ lái tàu' giữ nguyên (chưa có thuật ngữ chốt).

### key 2488 — 双鉄 — gasp

- JP: 「\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は優れたものだ。実際、今の日ノ本では、\nあらゆる場所で、引退した\x%lレイルロオド;#00ffc040;レイルロオド%l;#;が活躍――っ！」
- TW: 「按說\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;著實是性能優異，即使在當今日本，也有不少離開崗位的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;在各行各業——！」
- VN cũ: 「\x%lレイルロオド;#00ffc040;Railord%l;#; là một sự tồn tại ưu việt. Thực tế là ở Hinamoto hiện tại,\ncác \x%lレイルロオド;#00ffc040;Railord%l;#; đã nghỉ hưu đang hoạt động sôi nổi ở khắp mọi nơi——!」
- VN mới: 「\x%lレイルロオド;#00ffc040;Railord%l;#; là một sự tồn tại ưu việt. Thực tế là ở Hinamoto hiện tại,\ncác \x%lレイルロオド;#00ffc040;Railord%l;#; đã nghỉ hưu đang hoạt động sôi nổi ở khắp mọi nơi——Ư!」
- Lý do: Sweep ghi 'already-rendered' nhưng là phân loại sai: JP 「活躍――っ！」 cùng mẫu っ cuối sau dấu gạch như 3447/3663 trong chính file này (sweep sửa cả hai thành ——Ư!). VN '——!' chỉ giữ dấu câu của JP (! vốn đã có trong JP), không diễn tiếng gasp っ — sửa theo mẫu sweep, ghi chú để parent kiểm chứng.

### key 2493 — ひよこ — terminology

- JP: 「言い換えるなら、\x%lタブレット;#00ffc040;タブレット%l;#;はただ一箇所――\nいや、より厳密にいうのであれば、恐らくは」
- TW: 「換句話講，就只有一個地方——不，嚴格來講，恐怕是——」
- VN cũ: 「Nói cách khác, \x%lタブレット;#00ffc040;thẻ bảng%l;#; chỉ có ở một nơi duy nhất——\nkhông, nếu nói một cách chính xác hơn, thì có lẽ là」
- VN mới: 「Nói cách khác, \x%lタブレット;#00ffc040;máy tính bảng%l;#; chỉ có ở một nơi duy nhất——\nkhông, nếu nói một cách chính xác hơn, thì có lẽ là」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 2507 — 双鉄 — terminology

- JP: 「ならば、\x%lタブレット;#00ffc040;タブレット%l;#;をエアクラナビから\n除去する必要は全くなかった。にもかかわらず」
- TW: 「既然如此，那就更加沒有理由——或者應該說沒有任何理由不為空凝機導航安裝\x%lタブレット;#00ffc040;操作板%l;#;，可現實卻是——」
- VN cũ: 「Nếu vậy, hoàn toàn không cần thiết phải\nloại bỏ \x%lタブレット;#00ffc040;thẻ bảng%l;#; khỏi Navi Aircra. Vậy mà」
- VN mới: 「Nếu vậy, hoàn toàn không cần thiết phải\nloại bỏ \x%lタブレット;#00ffc040;máy tính bảng%l;#; khỏi Navi Aircra. Vậy mà」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 2532 — 双鉄 — terminology

- JP: 「冥国\x%l蒸機;#00ffc040;蒸機%l;#;ですか」
- TW: 「是美國式\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;嗎」
- VN cũ: 「Là \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; của nước Meikoku sao.」
- VN mới: 「Là \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; của Minh Quốc sao.」
- Lý do: 冥国 (không furigana) dịch 'nước Meikoku' (phiên âm romaji) — trái thuật ngữ đã chốt 'Minh Quốc' (tiền lệ 3 dòng 'Meikoku' → 'Minh Quốc').

### key 2547 — 双鉄 — pronoun

- JP: 「やはりそうか。教えてくれてありがとう」
- TW: 「果然是這個啊，謝謝你為我科普」
- VN cũ: 「Quả nhiên là vậy sao. Cảm ơn em đã cho anh biết.」
- VN mới: 「Quả nhiên là vậy sao. Cảm ơn cô đã cho tôi biết.」
- Lý do: Soutetsu cảm ơn người đã giải thích giả thuyết — đó là tiến sĩ Fushicho (Hachiroku ở 2536 chỉ đặt câu hỏi, không cung cấp thông tin; Olivy không nói gì từ 2382) → 'tôi'/'cô'.

### key 2551 — 双鉄 — terminology

- JP: 「さっきもいったが、エアクラナビと\x%lタブレット;#00ffc040;タブレット%l;#;は、\n本来は共存してしかるべきものと考える」
- TW: 「正如剛才所言，我認為按理來說，空凝機導航和\x%lタブレット;#00ffc040;操作板%l;#;原本屬於互惠互利，共同發展的關係」
- VN cũ: 「Như tôi đã nói lúc nãy, Navi Aircra và \x%lタブレット;#00ffc040;thẻ bảng%l;#;,\nvốn dĩ nên là những thứ cùng tồn tại với nhau.」
- VN mới: 「Như tôi đã nói lúc nãy, Navi Aircra và \x%lタブレット;#00ffc040;máy tính bảng%l;#;,\nvốn dĩ nên là những thứ cùng tồn tại với nhau.」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 2564 — ハチロク — terminology

- JP: 「\x%lタブレット;#00ffc040;タブレット%l;#;に、宿るものなのでしょうか？」
- TW: 「正是源自這\x%lタブレット;#00ffc040;操作板%l;#;是嗎？」
- VN cũ: 「Là thứ trú ngụ bên trong \x%lタブレット;#00ffc040;thẻ bảng%l;#; sao ạ?」
- VN mới: 「Là thứ trú ngụ bên trong \x%lタブレット;#00ffc040;máy tính bảng%l;#; sao ạ?」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 2606 — 双鉄 — terminology

- JP: 「けれど、実際には\x%lタブレット;#00ffc040;タブレット%l;#;は排除された。\nどころか、その唯一の供給源も、閉ざされてしまった」
- TW: 「然而結果卻是\x%lタブレット;#00ffc040;操作板%l;#;沒有被採用，甚至連其唯一的供應渠道也被切斷」
- VN cũ: 「Thế nhưng, thực tế là \x%lタブレット;#00ffc040;thẻ bảng%l;#; đã bị loại bỏ.\nThậm chí, nguồn cung cấp duy nhất của nó cũng đã bị đóng lại.」
- VN mới: 「Thế nhưng, thực tế là \x%lタブレット;#00ffc040;máy tính bảng%l;#; đã bị loại bỏ.\nThậm chí, nguồn cung cấp duy nhất của nó cũng đã bị đóng lại.」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 2632 — オリヴィ — terminology

- JP: 「だって、むかしはさ？　帝鉄とかはオヤカタヒノモトで、\nアンテー求めて鉄道にって人、いたみたいだけど」
- TW: 「畢竟以前在帝國鐵路之類的地方工作都還算公務員待遇，當時有人只是想來鐵路尋個鐵飯碗」
- VN cũ: 「Tại vì, ngày xưa ấy? Những nơi như Đường sắt Hoàng gia là doanh nghiệp nhà nước,\nnên có vẻ cũng có những người tìm đến đường sắt vì muốn sự ổn định.」
- VN mới: 「Tại vì, ngày xưa ấy? Những nơi như Teitetsu là doanh nghiệp nhà nước,\nnên có vẻ cũng có những người tìm đến đường sắt vì muốn sự ổn định.」
- Lý do: 帝鉄 → 'Teitetsu' theo thuật ngữ đã chốt; 'Đường sắt Hoàng gia' dịch sai (帝 = đế, không phải hoàng gia; tiền lệ file khác 'Đường sắt Hoàng gia → Teitetsu').

### key 2636 — ひよこ — terminology

- JP: 「当然、\x%lレイルロオド;#00ffc040;レイルロオド%l;#;・タブレット社も廃業・解体だ。\n\x%lタブレット;#00ffc040;タブレット%l;#;の製造技術が、完全に途絶したのだからね」
- TW: 「當然生產\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;操作板的公司也只有破產解散。畢竟製造\x%lタブレット;#00ffc040;操作板%l;#;的技術等於已經徹底失傳」
- VN cũ: 「Đương nhiên, công ty \x%lレイルロオド;#00ffc040;Railord%l;#; Tablet cũng bị đóng cửa và giải thể.\nBởi vì công nghệ chế tạo \x%lタブレット;#00ffc040;thẻ bảng%l;#; đã hoàn toàn bị thất truyền.」
- VN mới: 「Đương nhiên, công ty \x%lレイルロオド;#00ffc040;Railord%l;#; Tablet cũng bị đóng cửa và giải thể.\nBởi vì công nghệ chế tạo \x%lタブレット;#00ffc040;máy tính bảng%l;#; đã hoàn toàn bị thất truyền.」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 2644 — ひよこ — terminology

- JP: 「トロルユ――　[とろ,1]登呂元[ぎかん,1]技官！\nああ、そういえばあの方は[おひとよ,2]御一夜にご在住でしたな」
- TW: 「登呂流浴場——是說登呂前高級技工嗎！對哦，說來她確實是定居在御一夜了」
- VN cũ: 「Tororyu-yu——Cựu kỹ quan Toro!\nÀ, nhắc mới nhớ, bà ấy đang sống ở Ohimitera nhỉ.」
- VN mới: 「Tororyu-yu——Cựu kỹ quan Toro!\nÀ, nhắc mới nhớ, bà ấy đang sống ở Ohitoyo nhỉ.」
- Lý do: 御一夜 'Ohimitera' → 'Ohitoyo' theo quyết định 19/11 (furigana おひとよ).

### key 2731 — ひよこ — terminology

- JP: 「第一世代以降には無い機構。\nすなわち、\x%lタブレット;#00ffc040;タブレット%l;#;を内包するエアクラ・ナビ、と」
- TW: 「要說從第一代以後的不同之處，便在於後來的空凝機不再內建\x%lタブレット;#00ffc040;操作板%l;#;」
- VN cũ: 「Một cơ chế không hề có từ thế hệ thứ nhất trở đi.\nNói cách khác, là Navi Aircra có chứa \x%lタブレット;#00ffc040;thẻ bảng%l;#; bên trong.」
- VN mới: 「Một cơ chế không hề có từ thế hệ thứ nhất trở đi.\nNói cách khác, là Navi Aircra có chứa \x%lタブレット;#00ffc040;máy tính bảng%l;#; bên trong.」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 2759 — ひよこ — sfx

- JP: 「ふふん？」
- TW: 「說說看？」
- VN cũ: 「Hư hừ?」
- VN mới: 「Fufun?」
- Lý do: ふふん？ là tiếng cười khẽ (chuckle) — VN cũ 'Hư hừ?' diễn thành tiếng gắt/rên. Sửa 'Fufun?' theo mẫu tiếng cười trong file (Nfufu/Ufufu).

### key 2816 — ハチロク — tag

- JP: 「旧式の冥国\x%l蒸機;#00ffc040;蒸機%l;#;に特有の、尖って突き出た前方[はいしょうき,2]排障器。\nこれが、カウ・キャッチャアでございます」
- TW: 「這個是舊式美國\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;特有的以尖角造型向車體正面凸出的排障器，也就是剛才說的防撞梁」
- VN cũ: 「Là \x%l排障器;#00ffc040;bộ gạt vật cản%l;#; nhô nhọn ra phía trước, đặc trưng của \x%l蒸気機関車;#00ffc040;Đầu máy hơi nước%l;#; kiểu cũ của Minh Quốc.\nĐó chính là Cow Catcher ạ.」
- VN mới: 「Là bộ gạt vật cản nhô nhọn ra phía trước, đặc trưng của \x%l蒸機;#00ffc040;Đầu máy hơi nước%l;#; kiểu cũ của Minh Quốc.\nĐó chính là Cow Catcher ạ.」
- Lý do: Hai lỗi thẻ %l: (1) VN tự thêm thẻ %l cho 排障器 — JP chỉ có ruby [はいしょうき,2], không có thẻ %l (tiền lệ file 09: gỡ thẻ VN tự thêm khi JP chỉ có ruby) → gỡ thẻ, giữ gloss 'bộ gạt vật cản' dạng text thường. (2) Thuật ngữ trong thẻ bị đổi: JP gắn thẻ cho 蒸機 nhưng VN ghi 蒸気機関車 → sửa về 蒸機 (mẫu key 1994 trong file: \x%l蒸機…đầu máy hơi nước%l;#;).

### key 2839 — ハチロク — gasp

- JP: 「っ！！！？」
- TW: 「這！！！？」
- VN cũ: 「!!!?」
- VN mới: 「Ư!!!?」
- Lý do: Sweep lost-gasp (whole/trailing), đã kiểm chứng đúng JP/TW — nhận nguyên văn fix của sweep.

### key 2842 — 双鉄 — pronoun

- JP: 「僕は見てきた。日々姫の仕事を。デザインとは、\n不可能に思える配置を整頓で可能にするものなのだと」
- TW: 「通過親眼見證日日姬完成的工作，我明白那正是能通過巧妙配置，實現看似不可行的組合」
- VN cũ: 「Anh đã chứng kiến. Công việc của Hibiki. Thiết kế là,\nbiến những cách bố trí tưởng chừng như không thể thành có thể thông qua việc sắp xếp lại.」
- VN mới: 「Tôi đã chứng kiến. Công việc của Hibiki. Thiết kế là,\nbiến những cách bố trí tưởng chừng như không thể thành có thể thông qua việc sắp xếp lại.」
- Lý do: Soutetsu nói về công việc của Hibiki — người nghe là tiến sĩ Fushicho/nhóm (chuỗi đối thoại với bác sĩ: 2837→2842→2866→2874 đều hướng về bác sĩ), không phải Hibiki (cô không có mặt) → 'tôi'.

### key 2866 — 双鉄 — terminology

- JP: 「\x%lタブレット;#00ffc040;タブレット%l;#;を外す前には、稼働していた？」
- TW: 「那她在取下\x%lタブレット;#00ffc040;操作板%l;#;之前依然處於啟動狀態？」
- VN cũ: 「Trước khi tháo \x%lタブレット;#00ffc040;thẻ bảng%l;#; ra, cô ấy vẫn đang hoạt động sao?」
- VN mới: 「Trước khi tháo \x%lタブレット;#00ffc040;máy tính bảng%l;#; ra, cô ấy vẫn đang hoạt động sao?」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 2894 — 双鉄 — terminology

- JP: 「ならば、タブレットレベルとは――文字通り、\n\x%lタブレット;#00ffc040;タブレット%l;#;の中身全て――全領域の\x%l共感;#00ffc040;共感%l;#;、か？」
- TW: 「那麼核心級\x%l共感;#00ffc040;共鳴%l;#;的意思也很明顯，是對包括人偶核——也就是\x%lタブレット;#00ffc040;操作板%l;#;的全部領域實行\x%l共感;#00ffc040;共鳴%l;#;，對嗎？」
- VN cũ: 「Nếu vậy, mức độ mở hoàn toàn là——đúng như nghĩa đen,\ntất cả những gì bên trong \x%lタブレット;#00ffc040;thẻ bảng%l;#;——\x%l共感;#00ffc040;cộng cảm%l;#; toàn bộ lĩnh vực, sao?」
- VN mới: 「Nếu vậy, mức độ mở hoàn toàn là——đúng như nghĩa đen,\ntất cả những gì bên trong \x%lタブレット;#00ffc040;máy tính bảng%l;#;——\x%l共感;#00ffc040;cộng cảm%l;#; toàn bộ lĩnh vực, sao?」
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 2916 — ハチロク — terminology

- JP: 「双鉄さまは、御一夜のため。そうして、いくらかは\nわたくしのため――蒸気\x%l機関士;#00ffc040;機関士%l;#;になって下さったのです」
- TW: 「雙鐵少爺之所以成為蒸汽機車\x%l機関士;#00ffc040;司機%l;#;，是為守護御一夜，同時也有幾分理由與我有關」
- VN cũ: 「Ngài Soutetsu là vì Ohimitera. Và, một phần nào đó,\nlà vì em——nên mới trở thành \x%l機関士;#00ffc040;Lái tàu%l;#; hơi nước ạ.」
- VN mới: 「Ngài Soutetsu là vì Ohitoyo. Và, một phần nào đó,\nlà vì em——nên mới trở thành \x%l機関士;#00ffc040;Lái tàu%l;#; hơi nước ạ.」
- Lý do: 御一夜 'Ohimitera' → 'Ohitoyo' theo quyết định 19/11 (furigana おひとよ).

### key 2943 — オリヴィ — sfx

- JP: 「ドっ――ドク、ター……フェニ、くすっ」
- TW: 「Ｄｏｃｔｏｒ……Ｐｈｏｅｎｉｘ」
- VN cũ: 「Do——Doc, tor……Phoe, nix. Phụt.」
- VN mới: 「Do——Doc, tor……Phoe, nix. Hì hì.」
- Lý do: くすっ là tiếng cười nén (giggle) — VN cũ 'Phụt.' diễn thành tiếng phụt/khạc. Tiền lệ đã duyệt: くすっ → 'Hì hì'.

### key 3209 — monologue — terminology

- JP: \x%l運転体;#00ffc040;運転体%l;#;稼働時にも、\x%l整備体;#00ffc040;整備体%l;#;を必ずキャブ内に安置するのは、\nその端的な証明だろう。
- TW: 並且在使用\x%l運転体;#00ffc040;駕駛體%l;#;時一定要將\x%l整備体;#00ffc040;整備體%l;#;安放於駕駛室，或許也能從側面證實我的推論。
- VN cũ: Ngay cả khi vận hành \x%l運転体;#00ffc040;kíp lái%l;#;, việc bắt buộc phải đặt \x%l整備体;#00ffc040;thân chính%l;#; bên trong buồng lái,\nchính là minh chứng rõ ràng nhất cho điều đó.
- VN mới: Ngay cả khi vận hành \x%l運転体;#00ffc040;thân vận hành%l;#;, việc bắt buộc phải đặt \x%l整備体;#00ffc040;thân bảo trì%l;#; bên trong buồng lái,\nchính là minh chứng rõ ràng nhất cho điều đó.
- Lý do: 運転体 'kíp lái' → 'thân vận hành'; 整備体 'thân chính' → 'thân bảo trì' (như key 2146).

### key 3241 — monologue — terminology

- JP: が、シーリング開放がキーであるなら。\n今は不可能という\x%lタブレット;#00ffc040;タブレット%l;#;の複製なり、創造なりが――
- TW: 但是通過解除封印這一機能，迄今為止對於\x%lタブレット;#00ffc040;操作板%l;#;一直未能實現的複製，乃至於創造，或許就能成為現實——
- VN cũ: Nhưng, nếu việc giải trừ phong ấn là chìa khóa.\nThì việc sao chép, hay sáng tạo ra \x%lタブレット;#00ffc040;thẻ bảng%l;#; vốn được cho là bất khả thi hiện nay——
- VN mới: Nhưng, nếu việc giải trừ phong ấn là chìa khóa.\nThì việc sao chép, hay sáng tạo ra \x%lタブレット;#00ffc040;máy tính bảng%l;#; vốn được cho là bất khả thi hiện nay——
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 3266 — monologue — terminology

- JP: ハチロクの指が自分の胸を――\n\x%lタブレット;#00ffc040;タブレット%l;#;の上を、つかむようにして押さえる。
- TW: 八六就若有所思地抓住自己胸口上的\x%lタブレット;#00ffc040;操作板%l;#;，並緊緊按住。
- VN cũ: Những ngón tay của Hachiroku đưa lên trước ngực——\nnhư đang bấu chặt lấy \x%lタブレット;#00ffc040;thẻ bảng%l;#; của mình.
- VN mới: Những ngón tay của Hachiroku đưa lên trước ngực——\nnhư đang bấu chặt lấy \x%lタブレット;#00ffc040;máy tính bảng%l;#; của mình.
- Lý do: Gloss %l của タブレット là 'thẻ bảng' — thuật ngữ đã chốt là 'máy tính bảng' (tiền lệ file hearing/stove 2076/2642: タブレット → 'máy tính bảng'). Chỉ đổi gloss, giữ nguyên phần còn lại của câu.

### key 3447 — monologue — gasp

- JP: 帝鉄初代総裁が、雨の真夜中、轢死体となって発見された。\nそれが事件か、事故なのか、その真実は今もって――っ！
- TW: 帝國鐵路首任總裁於一個雨夜被人發現遭碾壓身亡，究竟是意外還是被人謀害，至今未能查明真相——莫非！
- VN cũ: Tổng tài đầu tiên của Teitetsu được phát hiện đã tử vong do bị tàu cán vào một đêm mưa giữa khuya.\nĐó là một vụ án mạng, hay chỉ là một tai nạn, sự thật đó cho đến nay vẫn——!
- VN mới: Tổng tài đầu tiên của Teitetsu được phát hiện đã tử vong do bị tàu cán vào một đêm mưa giữa khuya.\nĐó là một vụ án mạng, hay chỉ là một tai nạn, sự thật đó cho đến nay vẫn——Ư!
- Lý do: Sweep lost-gasp (whole/trailing), đã kiểm chứng đúng JP/TW — nhận nguyên văn fix của sweep.

### key 3463 — monologue — terminology

- JP: 僕やハチロクの情報はすでにかなり細かいものまで、\n恐らくは電車姫様から、伝わっているのであろう。
- TW: 想必是電車公主殿下事前已將我和八六的各種情況告知給不死鳥博士了，而且可以說是面面俱到。
- VN cũ: Những thông tin về tôi và Hachiroku, cho đến cả những chi tiết khá nhỏ nhặt,\ncó lẽ đã được công chúa Densha truyền đạt lại rồi.
- VN mới: Những thông tin về tôi và Hachiroku, cho đến cả những chi tiết khá nhỏ nhặt,\ncó lẽ đã được Công chúa Tàu điện truyền đạt lại rồi.
- Lý do: 電車姫 → 'Công chúa Tàu điện' theo quyết định 20/11 (không dùng 'Densha Hime'/'công chúa Densha').

### key 3475 — monologue — meaning

- JP: 薄暗く、冷えた地下フロア。\n格納庫……いや、倉庫という方が相応しかろうか。
- TW: 我們來到陰暗寒冷的地下，這裡似乎是車庫……不對，稱之為倉庫應當更為貼切。
- VN cũ: Một tầng hầm mờ tối và lạnh lẽo.\nNhà chứa máy bay……không, gọi là nhà kho thì đúng hơn.
- VN mới: Một tầng hầm mờ tối và lạnh lẽo.\nNhà chứa xe……không, gọi là nhà kho thì đúng hơn.
- Lý do: 格納庫 = nhà chứa xe (TW 車庫); VN cũ 'Nhà chứa máy bay' bịa thêm 'máy bay' — đây là nhà chứa phương tiện đường sắt, không có máy bay nào. Vế tự sửa '……không, gọi là nhà kho thì đúng hơn' giữ nguyên.

### key 3510 — monologue — terminology

- JP: 赤井宮司の\x%lレイルロオド;#00ffc040;レイルロオド%l;#;――ニイロクのことを思い出す。\n\x%l整備体;#00ffc040;整備体%l;#;を失っている、という話を聞いたが――
- TW: 我突然想到赤井宮司的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;二六，之前聽說她是已經沒有了\x%l整備体;#00ffc040;整備體%l;#;。
- VN cũ: Tôi nhớ đến \x%lレイルロオド;#00ffc040;Railord%l;#; của đền trưởng Akai——Niiroku.\nNghe nói cô ấy đã đánh mất \x%l整備体;#00ffc040;thân chính%l;#; của mình——
- VN mới: Tôi nhớ đến \x%lレイルロオド;#00ffc040;Railord%l;#; của đền chủ Akai——Niiroku.\nNghe nói cô ấy đã đánh mất \x%l整備体;#00ffc040;thân bảo trì%l;#; của mình——
- Lý do: 宮司 'đền trưởng' → 'đền chủ' (thuật ngữ đã chốt); 整備体 'thân chính' → 'thân bảo trì'.

### key 3581 — monologue — typo

- JP: だが鉄道はトゥーレシビックの想像よりも\n遥かに発展していった。
- TW: 然而鐵路事業的迅猛發展，卻是令特里維西克始料未及的。
- VN cũ: Nhưng đường sắt đã phát triển\nxo xa so với những gì Trevithick tưởng tượng.
- VN mới: Nhưng đường sắt đã phát triển\nvượt xa so với những gì Trevithick tưởng tượng.
- Lý do: Lỗi đánh máy: 'xo xa' không có nghĩa — JP 遥かに = 'vượt xa' (TW 迅猛發展 = phát triển vượt bậc).

### key 3633 — monologue — terminology

- JP: 本当の名前。それは、電車姫さまから教えていただいた、\n『ひよこ』という名前のことだろう。
- TW: 而電車公主殿下之前告知我們的“雛”這個名字，理應就是她口中多有不滿的真名。
- VN cũ: Tên thật. Chắc hẳn là cái tên mà Densha Hime đã cho chúng tôi biết,\ncái tên 『Hiyoko』.
- VN mới: Tên thật. Chắc hẳn là cái tên mà Công chúa Tàu điện đã cho chúng tôi biết,\ncái tên 『Hiyoko』.
- Lý do: 電車姫 → 'Công chúa Tàu điện' theo quyết định 20/11 (không dùng 'Densha Hime'/'công chúa Densha').

### key 3663 — monologue — gasp

- JP: 呆然――愕然――いや、そんな言葉よりも更に虚ろな――\nああ、そうか。魂が抜けたような表情――っ！！？
- TW: 詫異、驚愕，都不對，那種呆滯的狀態——對了，就像是靈魂出竅一樣！！？
- VN cũ: Sững sờ——kinh ngạc——không, còn trống rỗng hơn cả những từ ngữ đó——\nA, đúng rồi. Một biểu cảm như người mất hồn——!!?
- VN mới: Sững sờ——kinh ngạc——không, còn trống rỗng hơn cả những từ ngữ đó——\nA, đúng rồi. Một biểu cảm như người mất hồn——Ư!!?
- Lý do: Sweep lost-gasp (whole/trailing), đã kiểm chứng đúng JP/TW — nhận nguyên văn fix của sweep.

### key 3705 — monologue — terminology

- JP: その文字列が、そのまま帝鉄式の\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の扱いだと、\nここしばらくで、僕もいくらかは理解できてきた。
- TW: 這個名詞直接代表了在帝國鐵路制度中\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的待遇，通過這段時間的所見所聞，我也對此有了一定認知。
- VN cũ: Chuỗi ký tự đó, chính là cách đối xử với \x%lレイルロオド;#00ffc040;Railord%l;#; theo kiểu Đường sắt Hoàng gia,\ntrong một thời gian gần đây, tôi cũng đã phần nào hiểu được.
- VN mới: Chuỗi ký tự đó, chính là cách đối xử với \x%lレイルロオド;#00ffc040;Railord%l;#; theo kiểu Teitetsu,\ntrong một thời gian gần đây, tôi cũng đã phần nào hiểu được.
- Lý do: 帝鉄 → 'Teitetsu' theo thuật ngữ đã chốt; 'Đường sắt Hoàng gia' dịch sai (帝 = đế, không phải hoàng gia; tiền lệ file khác 'Đường sắt Hoàng gia → Teitetsu').

### key 3759 — monologue — terminology

- JP: （ああ。ならばさっきの『もみじ』というのも――\n電車姫様の異名のようなものなのか？）
- TW: （哦，那麼剛才她口中的“紅葉”——或許也屬於電車公主殿下的外號之類？）
- VN cũ: （A. Nếu vậy thì cái tên 『Momiji』 lúc nãy——\ncũng giống như một biệt danh của Densha Hime sao?）
- VN mới: （A. Nếu vậy thì cái tên 『Momiji』 lúc nãy——\ncũng giống như một biệt danh của Công chúa Tàu điện sao?）
- Lý do: 電車姫 → 'Công chúa Tàu điện' theo quyết định 20/11 (không dùng 'Densha Hime'/'công chúa Densha').

## Lượt soát 2 (bắt buộc)

- Đã đọc lại toàn bộ 65 bản sửa đối chiếu từng JP (+TW khi cần): **65/65 giữ nguyên, 0 bỏ, 0 sửa**. Không bản sửa nào bị loại hay sửa lại ở lượt soát 2.
- Kiểm tra cơ học sau lượt soát 2: JSON 65 mục, khóa là chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 65/65; khối TOML 65 khóa, parse được bằng tomllib, 0 sai lệch giá trị so với JSON; không fix nào chứa ký tự xuống dòng thật (mọi `\n` đều là backslash-n literal như CSV3); mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (đã kiểm tra diff từng dòng).

## Khối TOML (đã kiểm chứng parse)

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

## Chờ Hieu / quan sát (không tính sai)

- 日ノ本 'Hinomoto' vs 'Hinamoto' (câu hỏi toàn dự án, chưa chốt): file này dùng lẫn 'Hinomoto' 5 dòng (1507, 2375, 2730, 3431, 3480) và 'Hinamoto' 3 dòng (1529, 1994, 2488) — giữ nguyên cả 8 dòng, chờ Hieu chốt một cách viết chung.
- Soutetsu gọi Olivy 'cậu' (2304: 'Cậu biết sao Olivy') vs 'em' (2302: 'em bảo anh xem') — cách gọi Soutetsu→Olivy ('em'/'cô'/'cậu') đã được ghi chờ Hieu ở file ハチロク05; giữ nguyên 2304, không tính sai.
- Hachiroku tự xưng 'Tôi' 3 dòng (2321 'Tôi nhớ là', 2451 'Tôi là Railord…', 2890 'Tôi nhớ') vs 'em' ở toàn bộ các dòng còn lại — 'Tôi là' trong câu tự giới thiệu có thể là cố ý (cách giới thiệu trang trọng), giữ nguyên cả 3, cần quyết định chung cho わたくし của Hachiroku.
- Tiến sĩ Fushicho gọi Soutetsu 'Anh Migita' 3 dòng (2092, 2197, 2198) vs 'ngài Migita' 5 dòng (2477, 2500, 2592, 2870, 2931) — giữ nguyên, có thể là khác biệt ngữ điệu (lúc đùa cợt vs lúc trang trọng).
- 2093 「あえていいましょう。"[ごと]如き"、と」 → VN 'Tôi xin mạn phép nói rằng. Là "cỡ như".' — dịch yếu/vague nhưng không sai hẳn (JP cũng là câu bỏ lửng tu từ); giữ nguyên.
- 2645 câu cụt của Hachiroku được VN hoàn thiện ('nghĩ cho Railord chúng em') theo TW 關懷備至 — giữ nguyên (theo TW, không phải bịa).
- Gloss '(Mỹ)'/'(Nước Mỹ)' thêm sau 'Minh Quốc' ở 2024, 3480 (2222 đã sửa thành 'Meriken') — gloss giải thích thêm, giữ nguyên.
- 上山/Ueyama (2004, 2752, 3156) giữ theo furigana JP うえやま (TW viết 下山/Shimoyama — JP thắng TW, đây là tên hư cấu hoá của sự kiện có thật).
- ポルタル社 → 'công ty Porter' (1999, 2574, 2835, 2946) giữ theo TW (Porter).
- 3757 （さささささっ） → '(Lạch cạch lạch cạch)' giữ nguyên (tiếng bước chân; TW cũng chỉ ghi 'một tràng tiếng bước chân').
- 3412 câu độc thoại về tên thật 'Hiyoko' không hợp vẻ ngoài trí thức — thứ tự từ hơi rối nhưng đủ nghĩa; giữ nguyên.
- 2578 'người mà em từng gặp, chỉ có mỗi ngài Toyo' — Toyo là đầu máy nhưng được xưng 様 nên nhân hoá thành 'người' là chấp nhận được; giữ nguyên.

## Kết bài

File ハチロク10_旺宮鉄道歴史館.txt.toml: 572 dòng đọc, 65 dòng sai (11,4%) — lỗi tập trung ở thuật ngữ đã chốt nhưng bản dịch cũ chưa theo (タブレット 19 dòng, Ohitoyo 5, Teitetsu 3, 電車姫 4, 冥国 2, 運転体/整備体/宮司/機関士) và đại từ Soutetsu 'anh'→'tôi' (7 dòng) cùng gasp/SFX bị mất hoặc diễn sai (15 dòng). Không có lệch dòng, xoay chuỗi, nhiễm chéo hay dòng mồ côi. 8 dòng chờ Hieu đã liệt kê ở trên, không tính vào tổng sai. Khối TOML 65 khóa đã parse-kiểm chứng, sẵn sàng để gộp.

Kết bài