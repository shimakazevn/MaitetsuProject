# Audit: lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」 — 22 dòng Việt sai (đã đối chiếu JP + TW)

**Kết quả: 22/441 dòng sai (5,0%)** — lệch dòng 10, sweep 6, sfx 5, nghĩa 1. 0 chưa dịch, 0 trùng key, 0 tràn file khác. Cảnh: Olivy (Generic Railord, không có cơ quan sinh dục) đến xem Hiyoko (Tiến sĩ Phoenix) và Densha Hime (Momiji) làm tình để học về "sex" — giải thích cơ quan sinh dục nam/nữ, niêm phong (sealing), dildo hai đầu, và kết thúc bằng việc Olivy nhận ra dù không làm tình được thì vẫn có thể xác nhận tình yêu.

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 441 dòng script** (lời dẫn/monologue 239, Hiyoko 116, Điện xa Cơ/電車姫 86) đối chiếu JP + TW từ CSV3 "Trang tính 3", target là TOML-2. Soutetsu không xuất hiện trong file này nên không có lỗi xưng hô Soutetsu.
- **Cột TW lệch thứ tự so với JP ở phần lớn các dòng** (đã kiểm chứng bằng đọc: TW tại 875 thuộc về JP 1513, TW 1301 thuộc về JP 1396, TW 2092 là một câu dẫn khác hẳn, TW 53 là "?*init"). Vì vậy TW KHÔNG dùng được làm nhân chứng thứ hai ở file này — mọi phán đoán đều theo JP. Ngoại lệ: trong chuỗi xoay vòng, TW xoay cùng chiều với VN (TW 1375 thuộc về JP 2093, TW 2093 thuộc về JP 1499, TW 1563 thuộc về JP 1782, TW 1782 thuộc về JP 2092, TW 1860 thuộc về JP 1563) — bằng chứng cho thấy lệch xảy ra từ sheet gốc, trước bước CSV→TOML.
- CSV3 chỉ có **1 bộ 441 dòng** cho file này (không có dual-set); key khớp TOML tuyệt đối 441/441. 285 dòng khác TOML chỉ ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng — CSV3 (literal `\n`) là chuẩn cho danh sách sửa. 0 dòng VN trống, 0 dòng VN chứa chữ Hán (chưa dịch), 0 thẻ `%l` trong VN. `[selections]` rỗng ({}). Không có file TOML trùng nội dung (md5 bdb02933933db615a0380eb3839cd6de, đã kiểm tra cả 227 file; file này chỉ có 1 bản — task ghi "1 copy" nhưng thực tế không có bản trùng nào trong toml2/).
- Phân loại lỗi: lệch dòng 10, sweep 6 (5 mục sweep áp nguyên + 1 mục sweep "needs-file-audit" 2166), sfx 5, nghĩa 1. Theo người nói: lời dẫn 14, Điện xa Cơ 5, Hiyoko 3. **Chưa chắc chắn 0 dòng.**
- Kiểm tra chuỗi xoay vòng: tìm VN đúng của mỗi dòng lệch ngay trong chính file này trước khi dịch mới (theo brief) — 9/10 dòng tìm thấy VN đúng đang nằm ở key khác trong file; chỉ 2301 không có VN đúng ở đâu trong file (cũng không có ở đâu trong toàn dự án — "Yêu đương" xuất hiện 0 lần) nên dịch mới.
- Kiểm tra tràn file khác: đối chiếu từng VN của file này với chỉ mục VN toàn dự án (CSV3) — 16 VN trùng ở file khác đều là câu ngắn chung chung ("Vâng.", "Ra vậy.", "Momiji?", các SFX "Nhóp nhép", "Chạm nhẹ", "Phập") vốn lặp lại hợp lệ; **0 dòng tràn file khác**.

## Kết luận về cơ chế lỗi

Lỗi chính ở đây là **một chuỗi xoay vòng 10 mắt xích**: VN của mỗi key bị đẩy sang key khác theo một vòng khép kín, và TW xoay cùng chiều, chứng tỏ lỗi nằm ở sheet gốc (cột VN/TW bị dán lệch so với cột JP), không phải do bước CSV→TOML.

Vòng xoay (VN đang ở key A → thuộc về key B):

- 1375 → 2093; 2093 → 1499; 1499 → 1468 (VN "A! Không phải đâu!!" đã đúng ở 1468 — mắt này là **trùng lặp**, không phải xoay tiếp); 2092 → 1375; 1782 → 2092; 1563 → 1782; 1860 → 1563; 2332 → 1860; 1874 → 2332; 2301 → 1874; và **2301 mất VN đúng** (không nằm ở đâu trong file/dự án) → dịch mới "Yêu đương! Tôi làm được đàng hoàng mà!!".

Các lỗi còn lại đều là lỗi nhỏ, rải rác: 5 mục sweep áp nguyên (mất tiếng hít っ toàn dòng), 1 mục sweep "needs-file-audit" (2166: vừa mất tiếng hít vừa tự bịa đoạn hoàn chỉnh "tốt nhất là" cho câu JP cụt), 3 SFX くちいっ/ぐちゅううっ bị dịch thành động từ ("Áp sát"/"Đút vào" — hai cách dịch khác nhau cho cùng một âm くちいっ ở 1386 và 1774, trong khi chính file này dịch くちっ thành "Nhóp nhép" ở 1867), 1 SFX ぷあっ dịch lệch ("phụt" ở 2331, trong khi 4 chỗ khác đều là "phù ah"), 1 dòng mất tiếng hít toàn dòng mà sweep bỏ sót (2426, kèm "きゅぅぅ…" bị viết thành "Cứu…" — đọc như từ "cứu", trong khi quy ước của file là "kyu"), và 1 lỗi nghĩa (1302: "ゆえ" = vì → "vì thế" = do đó, đảo chiều nhân quả).

## Chi tiết dòng sai

### Lệch dòng — chuỗi xoay vòng 10 mắt (10 dòng)

**1375 [ひよこ]** — JP 「ああ――そうですか」 nhưng VN là câu "Not for me" thuộc về JP 2093. VN đúng đang nằm ở 2092.

- JP: 「ああ――そうですか」
- TW: 「做愛這個行為無論多麼重要、多麼美妙都不適合奧莉薇，Ｎｏｔ　ｆｏｒ　ｍｅ。」
- Cũ: 「Dù làm tình có quan trọng hay tuyệt vời đến đâu đi nữa thì với Olivy?\nTôi nghĩ nó Not for me. Không dành cho Olivy đâu.」
- Sửa: 「A——vậy sao.」

**1499 [monologue]** — JP về Tiến sĩ Phoenix hiểu lầm, nhưng VN là "A! Không phải đâu!!" (bản sao của VN đúng ở 1468). VN đúng đang nằm ở 2093.

- JP: フシチョーハカセ、なんだかちょっとカンチガイしてる！\nだってお顔も声もすっごく、申し訳無さそうなんだもん。
- TW: 「啊！不是的！！」
- Cũ: 「A! Không phải đâu!!」
- Sửa: Tiến sĩ Phoenix, có vẻ như đang hiểu lầm một chút rồi!\nBởi vì cả khuôn mặt lẫn giọng nói của cô ấy đều trông vô cùng áy náy.

**1563 [monologue]** — JP 「それはね？　えっへへー」 nhưng VN là câu hỏi "Biết là…" thuộc về JP 1782. VN đúng đang nằm ở 1860.

- JP: 「それはね？　えっへへー」
- TW: 「嗯？知道什麼？」
- Cũ: 「Hửm? Biết là——rốt cuộc, là biết chuyện gì cơ?」
- Sửa: 「Đó là? Ehehe~」

**1782 [ひよこ]** — JP hỏi "cô biết ư — rốt cuộc là biết chuyện gì?" nhưng VN là "Hơn nữa nhé? Olivy cũng biết rồi mà" thuộc về JP 2092. VN đúng đang nằm ở 1563.

- JP: 「ふむ？　知っておるとは――いったい、なにをじゃ？」
- TW: 「而且呢，奧莉薇也是知道的」
- Cũ: 「Hơn nữa nhé? Olivy, cũng biết rồi mà.」
- Sửa: 「Hửm? Biết là——rốt cuộc, là biết chuyện gì cơ?」

**1860 [monologue]** — JP "Có khi Công chúa Tàu điện và Tiến sĩ Phoenix cũng không biết! Vậy thì Olivy sẽ chỉ cho!" nhưng VN là "Đó là? Ehehe~" thuộc về JP 1563. VN đúng đang nằm ở 2332.

- JP: 電車姫さまもフシチョーハカセも知らないのかも！\nなら、オリヴィが教えてあげる！！
- TW: 「這個嘛，哎嘿嘿」
- Cũ: 「Đó là? Ehehe~」
- Sửa: Có lẽ cả Công chúa Tàu điện và Tiến sĩ Phoenix đều không biết đâu!\nVậy thì, Olivy sẽ chỉ cho hai người biết!!

**1874 [monologue]** — JP "Nói ra thì rõ hơn. Ra vậy, Olivy — quả nhiên là vậy!" nhưng VN là câu Generic Railord thuộc về JP 2332. VN đúng đang nằm ở 2301.

- JP: 言ったら、もっとはっきりわかる。\nそっか、オリヴィ――オリヴィ、やっぱりそうなんだ！
- TW: 「通用型鐵路人偶雖然無法做愛，但一樣可以感受到愛」
- Cũ: 「Dù là Generic Railord không thể làm tình,\nnhưng vẫn có thể xác nhận tình yêu một cách đàng hoàng.」
- Sửa: Nói ra rồi, tôi càng hiểu rõ hơn.\nĐúng vậy, Olivy——Olivy, quả nhiên là vậy!

**2092 [monologue]** — JP "Hơn nữa nhé, Olivy cũng biết mà" nhưng VN là "A——vậy sao." thuộc về JP 1375 (và 1343). VN đúng đang nằm ở 1782.

- JP: 「それにね？　オリヴィ、知ってもいるから」
- TW: 「不死鳥博士回了一句和剛才一樣的話，但這次她的表情明顯緩和許多，那是安心的表現。」
- Cũ: 「A——vậy sao.」
- Sửa: 「Hơn nữa nhé? Olivy, cũng biết rồi mà.」

**2093 [monologue]** — JP về "Not for me" nhưng VN là câu Tiến sĩ Phoenix hiểu lầm thuộc về JP 1499. VN đúng đang nằm ở 1375.

- JP: 「大事そうで素敵そうでも、セックスのことオリヴィね？\nNot for meって思うの。オリヴィ向きじゃないなって」
- TW: 「不死鳥博士對我的話有所誤會。她的表情不知為何有些黯然神傷。」
- Cũ: Tiến sĩ Phoenix, có vẻ như đang hiểu lầm một chút rồi!\nBởi vì cả khuôn mặt lẫn giọng nói của cô ấy đều trông vô cùng áy náy.
- Sửa: 「Dù làm tình có quan trọng hay tuyệt vời đến đâu đi nữa thì với Olivy?\nTôi nghĩ nó Not for me. Không dành cho Olivy đâu.」

**2301 [monologue]** — JP "Yêu đương! Làm được đàng hoàng mà!!" nhưng VN là câu "Nói ra rồi…" thuộc về JP 1874. VN đúng KHÔNG có ở đâu trong file lẫn toàn dự án → dịch mới.

- JP: 「レンアイ！　ちゃあんと出来るって！！」
- TW: 「說出口之後更加堅定了自己的想法。是的，奧莉薇果然知道——」
- Cũ: Nói ra rồi, tôi càng hiểu rõ hơn.\nĐúng vậy, Olivy——Olivy, quả nhiên là vậy!
- Sửa: 「Yêu đương! Tôi làm được đàng hoàng mà!!」

**2332 [monologue]** — JP về Generic Railord không làm tình được nhưng vẫn xác nhận được tình yêu, nhưng VN là câu "Olivy sẽ chỉ cho" thuộc về JP 1860. VN đúng đang nằm ở 1874.

- JP: 「セックスができない、ジェネリック・レイルロオドも、\n愛をちゃあんと確かめられる」
- TW: 「電車公主和不死鳥博士可能還不清楚，那就由奧莉薇告訴她們吧。」
- Cũ: Có lẽ cả Công chúa Tàu điện và Tiến sĩ Phoenix đều không biết đâu!\nVậy thì, Olivy sẽ chỉ cho hai người biết!!
- Sửa: 「Dù là Generic Railord không thể làm tình,\nnhưng vẫn có thể xác nhận tình yêu một cách đàng hoàng.」

### Sweep っ (6 dòng)

**1301 [電車姫]** — sweep lost-gasp-whole, áp nguyên. JP whole-line gasp っ+punct; VN chỉ còn dấu câu.

- JP: 「っ！！」
- TW: 「一旦開始之後便會深陷其中無法自拔。所以一會我的眼中可能只容得下紅葉一人」
- Cũ: 「!!」
- Sửa: 「Ư!!」

**1554 [monologue]** — sweep lost-gasp-whole, áp nguyên.

- JP: 「っ！！！？」
- TW: 「嗯！」
- Cũ: 「!!!?」
- Sửa: 「Ư!!!?」

**1591 [monologue]** — sweep lost-gasp-whole, áp nguyên.

- JP: 「っ！」
- TW: 「奧莉薇女士，接下來還請你擦亮眼睛」
- Cũ: 「!」
- Sửa: 「Ư!」

**1925 [電車姫]** — sweep lost-gasp-whole, áp nguyên.

- JP: 「っ！！！」
- TW: 「首先用你最喜歡的陰蒂讓你達到高潮——」
- Cũ: 「!!!」
- Sửa: 「Ư!!!」

**2099 [monologue]** — sweep lost-gasp-trailing-mid, áp nguyên. JP trailing gasp giữa câu; VN giữ dấu gạch + dấu câu ở vị trí gasp.

- JP: 「知ってる！　男の人がおしっこする――っ！！！！？\nplease wait!! ちょっとまって！？」
- TW: 「不死鳥博士湊到我耳邊說起了悄悄話——ｗｏｗ！」
- Cũ: 「Tôi biết! Đàn ông đi tiểu——!!!!?\nplease wait!! Đợi một chút!?」
- Sửa: 「Tôi biết! Đàn ông đi tiểu——Ư!!!!?\nplease wait!! Đợi một chút!?」

**2166 [ひよこ]** — sweep "needs-file-audit": mất tiếng hít っ sau "方法を……" VÀ tự bịa đoạn hoàn chỉnh "tốt nhất là" cho câu JP cụt. Sửa cả hai: khôi phục っ → Ư, bỏ "tốt nhất là" để giữ dạng câu cụt như JP.

- JP: 「なるほど。ならば方法を……っ！\nああ、今日は丁度、[もみじ,1]紅葉が尋ねてくる日でしたか」
- TW: 「因為奧莉薇不知道什麼時候會壽終正寢，在此之前想多了解一些新鮮事物。」
- Cũ: 「Ra vậy. Nếu vậy thì cách tốt nhất là……!\nA, hôm nay vừa hay lại là ngày Momiji đến thăm nhỉ.」
- Sửa: 「Ra vậy. Nếu vậy thì cách……Ư!\nA, hôm nay vừa hay lại là ngày Momiji đến thăm nhỉ.」

### SFX (5 dòng)

**1386 [monologue]** — （くちいっ） bị dịch thành động từ "Áp sát"; cùng một âm này ở 1774 lại dịch khác ("Đút vào"). Chính file này dịch くちっ thành "Nhóp nhép" ở 1867.

- JP: （くちいっ）
- TW: 「再然後就自然而然開始這樣——」
- Cũ: （Áp sát）
- Sửa: （Nhóp nhép!）

**1418 [monologue]** — （ぐちゅううっ！！！！！） bị dịch thành "Áp sát" (trùng với 1386, âm khác hẳn); chính file này dịch ぐちゅっ thành "Nhóp nhép" ở 2087.

- JP: （ぐちゅううっ！！！！！）
- TW: 「呼——嗯——哈——啊……呼啊——（咽口水）你不是也一樣，還有功夫顧著我嗎」
- Cũ: （Áp sát!!!!!）
- Sửa: （Nhóp nhép!!!!!）

**1774 [monologue]** — （くちいっ） lần thứ hai, dịch thành "Đút vào" — khác hẳn 1386 ("Áp sát") cho cùng một âm. Thống nhất về "Nhóp nhép" như 1867.

- JP: （くちいっ）
- TW: 「紅葉？奧莉薇女士在問你的這個液體是怎麼回事」
- Cũ: （Đút vào）
- Sửa: （Nhóp nhép!）

**2331 [電車姫]** — ぷあっ cuối câu bị dịch "phụt" (âm phun), trong khi 4 chỗ khác trong file (1527, 2094, 2346, 2457) đều dịch ふぁっ/ぷあっ là "phù ah". Thống nhất theo quy ước của file.

- JP: 「ちゅっ――れるっ――じゅぶっ――ちゅぼおおおっ――\nちゅるっ――れるっ――くぷうううううっ――ぷあっ」
- TW: 「電車公主含著假陽具的同時前後搖頭……表情看過去似乎有點痛苦——但不知為何這幅景象卻美如畫。」
- Cũ: 「Chụt——rột——nhóp nhép——chụt bụp——\nChụt rột——rột——chụt rột——phụt」
- Sửa: 「Chụt——rột——nhóp nhép——chụt bụp——\nChụt rột——rột——chụt rột——phù ah」

**2426 [電車姫]** — sweep BỎ SÓT: dòng 1 là whole-line gasp 「っっ！！！？」 nhưng VN chỉ còn "!!!?"; dòng 2 "きゅぅぅ…" (tiếng ré dài) bị viết thành "Cứu…" — đọc như từ "cứu" (cứu giúp), trong khi quy ước của file là "kyu" (2452 "Ưm kyu", 2437 "Phù kyu…", 2434 "Ưm kyuuuuuuuu…").

- JP: 「っっ！！！？\nいっ！　きゅぅぅぅぅぅぅぅぅぅぅぅぅっっっっっ！！」
- TW: 「（劇烈收縮）」
- Cũ: 「!!!?\nƯ! Cứuuuuuuuuuuuuuuu!!」
- Sửa: 「Ư!!!?\nƯ! Kyuuuuuuuuuuuuu!!」

### Nghĩa (1 dòng)

**1302 [電車姫]** — "ゆえ" = vì (nguyên nhân), VN cũ "vì thế" = do đó (kết quả) — đảo chiều nhân quả.

- JP: 「よい、のっ――ひよこ――んっ、ふっ――この、ほうが\n直接、おぬしを――感じ、られ、るっ――ゆえ――あ！」
- TW: 「一開始……確實是那麼打算的——只是突然開始懷念起沒使用道具的時候」
- Cũ: 「Cũng, được——Hiyoko——ưm, phù——thế này\nCó thể, trực tiếp——cảm nhận, được cô——vì thế——a!」
- Sửa: 「Cũng, được——Hiyoko——ưm, phù——thế này\nCó thể, trực tiếp——cảm nhận, được cô——vì——a!」

## Lượt soát 2

Đọc lại toàn bộ 22 fix đối chiếu từng JP lần thứ hai: **22 tổng / 22 tái kiểm chứng / 0 loại bỏ / 0 sửa lại.** Đặc biệt kiểm tra lại: 10 mắt xích chuỗi xoay — mỗi VN sửa đều khớp JP của key đích và đều đang nằm ở đúng key nguồn trong vòng (trừ 2301 dịch mới, đã xác nhận không tồn tại trong file/dự án); 5 mục sweep áp nguyên khớp JP từng dấu; 2166 khớp JP cụt; 3 SFX くちいっ/ぐちゅううっ khớp quy ước trong file (1867, 2087); 2331 khớp 4 lần "phù ah" khác; 2426 khớp độ dài âm (きゅ + ぅ×11 → "Kyu" + 12 u); 1302 chỉ đổi "vì thế" → "vì".

## Ghi chú / chờ Hieu (không tính sai, không tự quyết)

- **Olivy độc thoại xưng "tôi" hay "mình"?** Trong 239 dòng monologue, "tôi" 12 dòng, "mình" 18 dòng (vd. 1367 "Mình cũng tự nhận thức được mà" vs 1411 "Tôi không biết…"). JP độc thoại không có đại từ nên cả hai đều đúng nghĩa; chưa có quy tắc dự án cho Olivy. Cần Hieu chốt một dạng để thống nhất sau.
- **ふあっ → "phù ah" hay "phà"/"phùa"?** File dùng "phù ah" ở 875, 899, 1359, 1368, 1527, 1697, 2094, 2145, 2146, 2238, 2279, 2331 (sau sửa), 2346, 2457, 2458 — giữ nguyên vì là cách diễn hai mora trung thực với âm Nhật; quy tắc đã chốt "phà"/"phùa" là dạng mặc định, chưa rõ có bắt buộc thay hết không. Cần Hieu xác nhận.
- **詠字新聞 → "báo Eiji"?** Dùng nhất quán 4 lần (1336, 1660, 2107, 2232), không có trong danh sách thuật ngữ đã chốt. Cần Hieu xác nhận khi có dịp.
- **SFX trong ngoặc đơn dịch thành động từ** — quy ước riêng của file này (1393 "Xoa xoa!", 1406 "Nắn bóp", 1488 "Trượt vào", 1505 "Rút ra! ——Tách ra", 1567 "Liếm nhẹ", 1590/1505 "Tách ra", 1676/1891 "Chạm nhẹ", 1715 "Cọ xát!", 1799 "Ngoáy mạnh!!", 2328 "Trượt vào!!!") — giữ nguyên, không tính sai, vì nhất quán nội bộ và âm vẫn được diễn đạt bằng hành động. Chỉ sửa 3 trường hợp mâu thuẫn nội bộ (1386/1418/1774). Nếu Hieu muốn đổi toàn bộ sang âm thanh thì làm trong đợt thống nhất sau.
- **Cột TW lệch thứ tự toàn file** (xem Phương pháp) — cảnh báo cho CSV3, không ảnh hưởng bản dịch vì audit theo JP.
- Các dòng "しゅごっ/しゅきっ" (nói ngọng của Hiyoko/Densha Hime) được dịch theo nghĩa ("tuyệt quá"/"sướng quá") thay vì giữ giọng ngọng — giữ nguyên, đây là lựa chọn dịch hợp lý, không tính sai.
- Không có lỗi đại từ Soutetsu (Soutetsu không xuất hiện); không có lỗi thuật ngữ đã chốt (Ohitoyo đã đúng dạng ở 1364 "Đường sắt Ohitoyo"; không có "Ohito" cũ, "Yui", "Migita System", "Obata", "Suntetsu", "Master Controller", "Đường sắt Hoàng gia").

## Khối TOML (đã kiểm chứng parse)


```toml
[script]
1301 = "「Ư!!」"
1302 = "「Cũng, được——Hiyoko——ưm, phù——thế này\\nCó thể, trực tiếp——cảm nhận, được cô——vì——a!」"
1375 = "「A——vậy sao.」"
1386 = "（Nhóp nhép!）"
1418 = "（Nhóp nhép!!!!!）"
1499 = "Tiến sĩ Phoenix, có vẻ như đang hiểu lầm một chút rồi!\\nBởi vì cả khuôn mặt lẫn giọng nói của cô ấy đều trông vô cùng áy náy."
1554 = "「Ư!!!?」"
1563 = "「Đó là? Ehehe~」"
1591 = "「Ư!」"
1774 = "（Nhóp nhép!）"
1782 = "「Hửm? Biết là——rốt cuộc, là biết chuyện gì cơ?」"
1860 = "Có lẽ cả Công chúa Tàu điện và Tiến sĩ Phoenix đều không biết đâu!\\nVậy thì, Olivy sẽ chỉ cho hai người biết!!"
1874 = "Nói ra rồi, tôi càng hiểu rõ hơn.\\nĐúng vậy, Olivy——Olivy, quả nhiên là vậy!"
1925 = "「Ư!!!」"
2092 = "「Hơn nữa nhé? Olivy, cũng biết rồi mà.」"
2093 = "「Dù làm tình có quan trọng hay tuyệt vời đến đâu đi nữa thì với Olivy?\\nTôi nghĩ nó Not for me. Không dành cho Olivy đâu.」"
2099 = "「Tôi biết! Đàn ông đi tiểu——Ư!!!!?\\nplease wait!! Đợi một chút!?」"
2166 = "「Ra vậy. Nếu vậy thì cách……Ư!\\nA, hôm nay vừa hay lại là ngày Momiji đến thăm nhỉ.」"
2301 = "「Yêu đương! Tôi làm được đàng hoàng mà!!」"
2331 = "「Chụt——rột——nhóp nhép——chụt bụp——\\nChụt rột——rột——chụt rột——phù ah」"
2332 = "「Dù là Generic Railord không thể làm tình,\\nnhưng vẫn có thể xác nhận tình yêu một cách đàng hoàng.」"
2426 = "「Ư!!!?\\nƯ! Kyuuuuuuuuuuuuu!!」"
```

## Kết bài

File lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」 đã đọc xong toàn bộ 441 dòng: **22 dòng sai (5,0%)**, gồm 1 chuỗi xoay vòng 10 mắt xích (9 mắt tìm lại được VN đúng trong file, 1 mắt 2301 dịch mới), 6 lỗi sweep っ, 5 lỗi SFX và 1 lỗi nghĩa. Lượt soát 2: 22/22/0/0. Không có lỗi đại từ Soutetsu, không có thuật ngữ đã chốt nào sai, không tràn file khác, không dòng chưa dịch hay trùng key. Còn chờ Hieu: Olivy độc thoại "tôi" hay "mình", "phù ah" hay "phà"/"phùa", "báo Eiji" cho 詠字新聞, và cách xử lý SFX dạng động từ trong file.
