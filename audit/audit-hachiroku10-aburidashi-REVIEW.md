# Audit — ハチロク10_炙り出し.txt.toml

- File: `ハチロク10_炙り出し.txt.toml` — route 01_Hachiroku, 380 dòng script.
- Nội dung: Paulette báo tin 日ノ本車輌 đồng ý gửi 台枠 của 58623; bàn chuyện vận chuyển 甲種/乙種/丙種 với Hachiroku và kỹ sư Fuchi (cựu nhân viên nhà máy Toyokawa, người phản đối việc tháo dỡ 58623 vì đó là kỷ niệm của Koharu); Soutetsu chụp ảnh quá trình hơ dầu trên 台枠, mùi khét gợi lại tai nạn; rồi cơn ác mộng gặp Michiko trong toa hành khách — cô em gái song sinh chất vấn anh về việc có phải anh thích Hachiroku chỉ vì muốn quên đi quá khứ.
- **Kết quả: 12/380 dòng sai (3,2%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (380 dòng, 0 khóa trùng, 0 ô VN trống). VN khớp TOML tuyệt đối 380/380 (0 lệch thực chất — 251 dòng chỉ khác ở chỗ TOML-2 làm phẳng dấu \n thành khoảng trắng, đã biết, không phải lỗi). `[selections]` rỗng.
- TOML md5 `f57f3dacab6be00e16b0d5e7bf9c6a7a`; không có bản sao file này (không thuộc 11 nhóm trùng — đã kiểm tra md5 toàn bộ 227 file).
- Thẻ %l: cân bằng tuyệt đối mọi dòng (số mở \x%l = số đóng %l;#; cả JP lẫn VN); thuật ngữ trong thẻ khớp JP↔VN (chỉ khác thứ tự ở 79 do đảo trật tự câu tiếng Việt, không phải lỗi). 1 thẻ VN tự thêm ở 1849 (帝鉄→"Teitetsu", JP chỉ có ruby [ていてつ,1]) — gloss là thuật ngữ đã chốt, đúng nội dung, giữ nguyên, không tính sai.
- Đại từ Soutetsu: "anh" đúng với Hibiki (1648) và Michiko (1900, 1397, 1688, 1916, 1886); "anh" trong độc thoại 2390 là câu hỏi hướng về Michiko trong giấc mơ — đúng; "cháu" với Fuchi (1706, 1885, 1979, 2023, 2102) đúng; "mình" trong độc thoại nội tâm (2857, 2867, 2376, 2860, 2870) đúng ngoại lệ đã chốt; "cô" với Paulette (1795, 1965, 1976) giữ nguyên theo quy ước file. 6 dòng "anh" sai với Hachiroku đã sửa (§2).
- Thuật ngữ: Hinamoto ×4 (1930, 1793, 1868, 2801) — đúng 4 dòng như brief ghi, để đợt thống nhất, KHÔNG sửa ở đây. Ohimitera ×1 (2434) đã sửa trong-audit theo tiền lệ. Teitetsu (1849, 2054), まいてつ→"chủ tàu" (1911), Railord, KiHa không có vấn đề. 静態保存→"lưu tĩnh" (2872) giữ nguyên — dạng chủ đạo toàn dự án (17× vs "bảo quản tĩnh" 1×), xem cờ §4.
- 2 dòng VN==TW đều chỉ là dấu câu, không phải chưa dịch: 1386 JP 「――」→「——" đúng; 1395 JP 「っ" đã sửa gasp (§2).
- Sweep: 3 mục cho file này (2105, 2110, 2513) — cả 3 đều đúng, đã nhận. Sweep bỏ sót 1 mục (1395) — đã sửa mới. Quét lại toàn bộ っ trong file: các っ còn lại đều đã được diễn (SFX, gạch ngang cắt câu, "hửm?", "Suỵt", "Á", "Bịch"...) hoặc là っ trong từ / っ nhấn mạnh cuối câu gắn với từ nội dung (1858 こん臭いっ — theo quy tắc đã chốt không thêm Ư).

## §2. Danh sách sửa (12 dòng)

Phân loại: đại từ 6 (1789, 2069, 2018, 1895, 1733, 1966 — Soutetsu "anh"→"tôi" với Hachiroku), gasp 4 (2105, 2110, 2513 từ sweep + 1395 sweep bỏ sót), thuật ngữ 1 (2434 Ohimitera→Ohitoyo), dịch sai 1 (2411 "phi hành đoàn"→"nhân viên tàu").

### 1789 — 双鉄 — pronoun
- JP: 「ふむ。自分の車輪で――とあえていうなら。わかった。\n乙種は、\x%l貨車;#00ffc040;貨車%l;#;か何かにまるごと乗せての輸送だな？」
- TW: 「嗯。甲種是依靠自身車輪的話——我懂了。乙種就是用\x%l貨車;#00ffc040;貨運車廂%l;#;承載整輛車的方法？」
- VN cũ: 「Ừm. Cố tình nhấn mạnh là bằng chính bánh xe của nó——thì anh hiểu rồi.\nLoại Ất là đặt toàn bộ lên \x%l貨車;#00ffc040;toa chở hàng%l;#; hay gì đó để vận chuyển đúng không?」
- Sửa: 「Ừm. Cố tình nhấn mạnh là bằng chính bánh xe của nó——thì tôi hiểu rồi.\nLoại Ất là đặt toàn bộ lên \x%l貨車;#00ffc040;toa chở hàng%l;#; hay gì đó để vận chuyển đúng không?」
- Lý do: Soutetsu trả lời Hachiroku — cô ấy vừa giải thích 甲種輸送 là gì (1384, 1836). Theo quy tắc đại từ đã sửa, Soutetsu là "tôi" với Hachiroku; "anh" ở đây sai.

### 2069 — 双鉄 — pronoun
- JP: 「ならば、お前を撮らせてくれ。\nガスランプをひとつ、借りてこれるか？」
- TW: 「還是讓我拍你吧。你能借來一盞噴燈嗎？」
- VN cũ: 「Vậy thì, hãy để anh chụp em.\nEm có thể mượn một cái đèn khò đến đây được không?」
- Sửa: 「Vậy thì, hãy để tôi chụp em.\nEm có thể mượn một cái đèn khò đến đây được không?」
- Lý do: Soutetsu nói với Hachiroku (JP お前; câu sau "Em có thể mượn một cái đèn khò..."). "anh"→"tôi" theo quy tắc đã sửa.

### 2018 — 双鉄 — pronoun
- JP: 「わからないんだ。いい夢だったような気もする。\n路子の――妹の夢だったから」
- TW: 「說不清楚。我感覺也能說是一場好夢，因為在夢裡見到了我的妹妹——路子」
- VN cũ: 「Anh không biết nữa. Cảm giác như đó là một giấc mơ đẹp.\nVì đó là giấc mơ về Michiko——về em gái anh.」
- Sửa: 「Tôi không biết nữa. Cảm giác như đó là một giấc mơ đẹp.\nVì đó là giấc mơ về Michiko——về em gái tôi.」
- Lý do: Soutetsu trả lời Hachiroku (1861 Hachiroku hỏi "Ngài đã gặp ác mộng sao ạ?"). Cả hai chỗ "anh" đều là tự xưng với Hachiroku → "tôi" (kể cả "em gái anh"→"em gái tôi", vì đó cũng là tự xưng sở hữu).

### 1895 — 双鉄 — pronoun
- JP: 「路子と僕は、ふたごだった。\nだから、あれはきっと、路子の姿をした僕だった」
- TW: 「我和路子是雙胞胎兄妹。所以，那一定是化成路子模樣的我自己」
- VN cũ: 「Michiko và anh là anh em sinh đôi.\nVì vậy, đó chắc chắn là anh trong hình hài của Michiko.」
- Sửa: 「Michiko và tôi là anh em sinh đôi.\nVì vậy, đó chắc chắn là tôi trong hình hài của Michiko.」
- Lý do: Soutetsu nói với Hachiroku sau cơn ác mộng. Cả hai chỗ "anh" đều là tự xưng với Hachiroku → "tôi".

### 1733 — 双鉄 — pronoun
- JP: 「揺り戻しが、少し来ただけだ。\nそれで、不安に……いささか、不安定になってしまった」
- TW: 「只是突然回憶起了過去而已。只是因為這個……稍微變得有些不安、情緒波動而已」
- VN cũ: 「Chỉ là một chút ký ức dội lại thôi.\nVì thế nên, anh mới thấy bất an……hơi bất ổn một chút.」
- Sửa: 「Chỉ là một chút ký ức dội lại thôi.\nVì thế nên, tôi mới thấy bất an……hơi bất ổn một chút.」
- Lý do: Soutetsu nói với Hachiroku. "anh"→"tôi" theo quy tắc đã sửa.

### 1966 — 双鉄 — pronoun
- JP: 「いいや、平気だ。\n夢ごときで、お前を煩わせたくもない」
- TW: 「沒事，我沒關係的。我可不想因為一場夢而勞煩你傷神」
- VN cũ: 「Không sao, anh ổn mà.\nAnh không muốn làm phiền em chỉ vì một giấc mơ.」
- Sửa: 「Không sao, tôi ổn mà.\nTôi không muốn làm phiền em chỉ vì một giấc mơ.」
- Lý do: Soutetsu nói với Hachiroku (JP お前). Cả hai chỗ "anh" đều là tự xưng với Hachiroku → "tôi".

### 2434 — monologue — terminology
- JP: "蒸気のふるさと御一夜”を浸透させ、\nひいては、大九洲ＳＬ構想を成立させる。
- TW: 將“蒸汽之鄉御一夜”的概念灌輸給大家，進而發展大九州蒸汽機車事業。
- VN cũ: Khắc sâu hình ảnh "Quê hương của hơi nước Ohimitera" vào tâm trí mọi người,\ntừ đó, hiện thực hóa khái niệm Đại Kyushu SL.
- Sửa: Khắc sâu hình ảnh "Quê hương của hơi nước Ohitoyo" vào tâm trí mọi người,\ntừ đó, hiện thực hóa khái niệm Đại Kyushu SL.
- Lý do: 御一夜 = "Ohitoyo" theo thuật ngữ đã chốt. VN cũ "Ohimitera" là dạng cũ (tiền lệ sửa trong-audit ở 仲国02, ハチロク03, 稀咲02).

### 2411 — monologue — mistranslation
- JP: 乗客乗員の全滅を防ぐそのために――\n犠牲を抑えるそのために、あえての事故を起こしたことを。
- TW: 她是為了避免讓所有乘客與列車工作人員遇難——為了把犧牲降到最低才造成了這場事故。
- VN cũ: Để ngăn chặn việc toàn bộ hành khách và phi hành đoàn bị diệt vong——\nĐể hạn chế thương vong, cô ấy đã cố tình gây ra tai nạn đó.
- Sửa: Để ngăn chặn việc toàn bộ hành khách và nhân viên tàu bị diệt vong——\nĐể hạn chế thương vong, cô ấy đã cố tình gây ra tai nạn đó.
- Lý do: JP 乗員 = nhân viên trên tàu (TW xác nhận: 列車工作人員). VN cũ "phi hành đoàn" là thuật ngữ hàng không — sai hẳn ngữ cảnh đường sắt; cùng lớp lỗi đã chốt ở 乗務鞄→"túi công tác" (không dùng từ hàng không).

### 2105 — 双鉄 — gasp
- JP: 「っ！」
- TW: 「！」
- VN cũ: 「!」
- Sửa: 「Ư!」
- Lý do: Sweep lost-gasp-whole: JP 「っ！」 cả dòng là gasp, VN chỉ còn "!" — gasp mất hẳn. Thêm Ư theo tiền lệ sweep.

### 2110 — 日々姫 — gasp
- JP: 『「っ！？」\n「きゃっ――ごめんなさいっ――って、あ、にぃに」』
- TW: 『「！？」\n「呀——不好意思——呃，啊，阿哥」』
- VN cũ: 『「!?」\n「Á——em xin lỗi——ơ, a, anh hai.」』
- Sửa: 『「Ư!?」\n「Á——em xin lỗi——ơ, a, anh hai.」』
- Lý do: Sweep lost-gasp-whole: dòng đầu 『「っ！？」』 gasp bị mất — thêm Ư. Dòng 2 giữ nguyên: きゃっ→"Á" đã diễn, ごめんなさいっ đã diễn bằng dấu gạch ngang (không thêm Ư kép theo quy tắc ranh giới gasp).

### 2513 — monologue — gasp
- JP: 心の中にもハチロクを、\nしっかりと焼き付けられるよう――っ！？
- TW: 我想就這樣把八六的模樣印在我心中——嗯！？
- VN cũ: Để có thể khắc sâu hình ảnh Hachiroku,\nvào tận trong tim mình——!?
- Sửa: Để có thể khắc sâu hình ảnh Hachiroku,\nvào tận trong tim mình——Ư!?
- Lý do: Sweep lost-gasp-trailing: JP kết ――っ！？, VN giữ dấu gạch ngang nhưng làm mất gasp — thêm Ư sau gạch ngang.

### 1395 — 双鉄 — gasp
- JP: 「っ」
- TW: 「……」
- VN cũ: 「……」
- Sửa: 「Ư……」
- Lý do: Sweep BỎ SÓT (không có mục nào cho key này trong sweep-raw-gasp-wrong.json): JP 「っ」 cả dòng, VN 「……" chép TW làm mất hẳn tiếng gasp. Soutetsu nghẹn lời sau câu của Fuchi (1904), rồi cúi đầu ở 2529 — đây là tiếng nấc nghẹn. Thêm Ư, giữ "……" vì nó diễn khoảng lặng sau tiếng nấc (tiền lệ bare-っ→"Ư" ở lr_ハチロクh2 1414, ニイロク04 1265; ở đây giữ dấu … vì cảnh hỗ trợ).

## §3. Lượt soát 2 (bắt buộc)
- Đọc lại toàn bộ 12 giá trị fix đối chiếu từng dòng JP: **12/12/0/0** (tổng / xác minh lại / loại bỏ / sửa lại). Không có fix nào bị loại hay sửa lại ở lượt 2.
- Kiểm tra cơ học JSON vs CSV3: jp/tw/old_vn khớp tuyệt đối 12/12; khối TOML parse được (tomllib), 12 khóa, 0 sai lệch giá trị so với JSON.

## §4. Cờ chờ Hieu (không tự quyết)
1. **1825 — Soutetsu "tôi"**: "Đương nhiên, tôi cũng định sẽ chụp lại toàn bộ quá trình vận chuyển và bảo dưỡng." Người nghe là Paulette (nối tiếp câu 1965 "Cô đã cho một gợi ý rất hay" — nếu tính là nói với Paulette thì phải là "anh" theo quy tắc) hay cả nhóm Paulette + Hachiroku (Hachiroku vỗ tay và đáp ngay ở 1769 — nếu tính là nói với nhóm thì giữ "tôi" theo tiền lệ Paulette 14 key 1544)? Giữ nguyên "tôi", chờ Hieu quyết.
2. **2694 — gloss 機関士 "người lái tàu"**: toàn dự án đang chia 3 dạng — "lái tàu" 102× / "người lái tàu" 50× / "nhân viên cơ vụ" 33× — còn "thợ lái đầu máy" (thuật ngữ đã chốt trong brief) là 0 lần trong toàn bộ VN. Sửa lẻ 1 dòng này sẽ gây lệch thay vì thống nhất. Cần quyết định toàn dự án (đợt thống nhất).
3. **Hinamoto ×4** (1930, 1793, 1868, 2801) — đợt thống nhất đã duyệt (日ノ本→"Hinomoto").
4. **2411 có "anh em"**: 日々姫03 key 2834 cũng dịch 乗員→"phi hành đoàn" — ghi chú để file đó bắt khi tới lượt audit (không sửa chéo file).
5. **2872 静態保存 "lưu tĩnh"** — giữ nguyên (dạng chủ đạo 17× vs "bảo quản tĩnh" 1×). Nếu Hieu muốn "bảo quản tĩnh" thì đưa vào đợt thống nhất.

## §5. Khối TOML (đã kiểm chứng parse)

```toml
[script]
"1789" = "「Ừm. Cố tình nhấn mạnh là bằng chính bánh xe của nó——thì tôi hiểu rồi.\\nLoại Ất là đặt toàn bộ lên \\x%l貨車;#00ffc040;toa chở hàng%l;#; hay gì đó để vận chuyển đúng không?」"
"2069" = "「Vậy thì, hãy để tôi chụp em.\\nEm có thể mượn một cái đèn khò đến đây được không?」"
"2018" = "「Tôi không biết nữa. Cảm giác như đó là một giấc mơ đẹp.\\nVì đó là giấc mơ về Michiko——về em gái tôi.」"
"1895" = "「Michiko và tôi là anh em sinh đôi.\\nVì vậy, đó chắc chắn là tôi trong hình hài của Michiko.」"
"1733" = "「Chỉ là một chút ký ức dội lại thôi.\\nVì thế nên, tôi mới thấy bất an……hơi bất ổn một chút.」"
"1966" = "「Không sao, tôi ổn mà.\\nTôi không muốn làm phiền em chỉ vì một giấc mơ.」"
"2434" = "Khắc sâu hình ảnh \"Quê hương của hơi nước Ohitoyo\" vào tâm trí mọi người,\\ntừ đó, hiện thực hóa khái niệm Đại Kyushu SL."
"2411" = "Để ngăn chặn việc toàn bộ hành khách và nhân viên tàu bị diệt vong——\\nĐể hạn chế thương vong, cô ấy đã cố tình gây ra tai nạn đó."
"2105" = "「Ư!」"
"2110" = "『「Ư!?」\\n「Á——em xin lỗi——ơ, a, anh hai.」』"
"2513" = "Để có thể khắc sâu hình ảnh Hachiroku,\\nvào tận trong tim mình——Ư!?"
"1395" = "「Ư……」"
```

## Kết bài
File ハチロク10_炙り出し: 380 dòng đã đọc hết, 12 dòng sai (3,2%) — 6 đại từ Soutetsu với Hachiroku, 4 gasp っ (3 sweep + 1 sweep bỏ sót), 1 thuật ngữ Ohitoyo, 1 dịch sai "phi hành đoàn". Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. 5 cờ chờ Hieu ở §4 (1825, 2694, Hinamoto ×4, 日々姫03 2834, 2872). Lượt soát 2: 12/12/0/0. Khối TOML 12 khóa parse được, 0 sai lệch giá trị.