# Kiểm tra bản dịch — 02_Hibiki 日々姫06_みくろ、来訪.txt.toml

File: `日々姫06_みくろ、来訪.txt.toml` — route 02_Hibiki, Mikuro đến thăm Ohitoyo: xin phép dọn dẹp D51 1031, Soutetsu–Hibiki–Mikuro cùng bọn trẻ và du khách dọn dẹp, ăn trưa ở quán cà phê (SL cà ri, gà rán than đá).
Đây là kiểm tra ĐẦY ĐỦ (full audit) — đọc toàn bộ 482 dòng script đối chiếu JP + TW.

## §1. Tổng quan

- Tổng số dòng script: **482** (monologue 153, hội thoại 329: 双鉄 133, 日々姫 86, みくろ 75, còn lại 35).

- Số dòng sai: **14/482 (2,9%)** — hội thoại 13/329 (4,0%), độc thoại 1/153 (0,7%).

- Phân loại: pronoun 6 (1849, 1860, 2013, 2212, 2224, 2471), mistranslation 3 (1973, 2436, 2971), gasp 3 (1986, 2015, 2035), sfx 1 (2062), terminology 1 (2146).

- TOML md5: `33e2c2ee430466994c1bd6fc71b85376` (bản duy nhất — không có file trùng; kiểm tra md5 toàn bộ 227 file toml2: 11 nhóm trùng của dự án không chứa file này).

- CSV↔TOML: 482/482 key khớp tuyệt đối, VN khớp 0 khác biệt thực chất. CSV3 là bộ đơn (single-set), không có bộ đôi; 0 ô VN trống.

- Thẻ `%l`: 5 dòng có thẻ (1890, 2222, 2232, 2458, 3059) — tất cả đều đóng thẻ đúng, JP↔VN khớp tag. Không có thẻ %l hỏng trong file này.

- **Rotation: 0 chuỗi xoay** — không có dòng lệch hàng nào: 14 lỗi đều là sai tại chỗ (đại từ, dịch sai, gasp, SFX, thuật ngữ), không có bản dịch đúng nằm ở key khác trong file (đã kiểm tra: 0/14 fix trùng với VN cũ ở key khác). Đã kiểm tra trùng lặp VN: chỉ 3 cặp trùng là các câu ngắn hợp lệ ("Vâng." ×3 ở 2069/2132/2317, "Vâng!" ×2 ở 2072/2330, "A——" ×2 ở 2020/2021).

- **0 contamination có nghĩa** / **0 orphan** / **0 untranslated** (0 ô VN trống) / **0 duplicate key**. (4 giá trị cũ là câu cực ngắn — "!!?", "!", "っ!!", "Cảm ơn em." — cũng xuất hiện ở file khác, nhưng đó là các câu ngắn trùng nhau một cách độc lập, không phải nội dung bị đẩy chéo file.)

- **1 dòng uncertain** (1877 — xem §5; đã giữ nguyên bản cũ, không tính sai).

- Ohitoyo trong file: 7 dòng còn dạng cũ "Ohimitera" (1877, 1890, 1922, 2099, 2374, 2439, 2504 — tổng 9 chỗ dùng) + 1 dòng 帝鉄 dạng cũ "Đường sắt Hoàng gia" (3128) — **không sửa trong audit này, để dành cho đợt thống nhất thuật ngữ** (chờ Hieu).

- Sweep っ: file có 3 mục trong sweep-raw-gasp-wrong.json (1986, 2015, 2035) — cả 3 đều đúng, đã áp nguyên. Không phát hiện thêm gasp nào sweep bỏ sót (VN chỉ còn đúng 1 ký tự っ thô là 2035).

- Strong candidates: queue ghi 9 dòng (không ghi key) — đọc toàn bộ tìm ra 14 dòng sai; con số heuristic chỉ là cận dưới, đọc từng dòng mới là chuẩn.


## §2. Bảng fix (14 dòng)

### 1849 — 双鉄 — đại từ xưng hô

- JP: 「すまぬ。少し考え事をしていた」

- TW: 「不好意思，想事情想得走神了」

- Cũ: 「Xin lỗi. Anh đang mải nghĩ ngợi một chút.」

- Mới: 「Xin lỗi. Tôi đang mải nghĩ ngợi một chút.」

- Lý do: Soutetsu nói với Mikuro: dòng kề trước 1848 là Mikuro xin lỗi, dòng kề sau 1852 Soutetsu xưng "tôi" và gọi Mikuro là "cô" trong cùng đoạn hội thoại. Bản cũ "Anh" lạc khỏi cách xưng hô Soutetsu→Mikuro trong cả file ("tôi"/"cô" ở 1846, 2004, 2009, 2231, 2441, 2447, 2451, 2528, 2545).


### 1860 — 双鉄 — đại từ xưng hô

- JP: 「いや、雄武田での地元告知ではなく、ここでの――\nD51 1031の地元、湯富院での告知の話だ」

- TW: 「不，我不是指大牟田地區的通告，而是指這裡的——Ｄ５１　１０３１的所在地，在湯布院的通告」

- Cũ: 「Không, không phải thông báo ở Omuta, mà là ở đây cơ——\nTôi đang hỏi về việc thông báo ở Yufuin, quê hương của chiếc D51 1031 này.」

- Mới: 「Không, không phải thông báo ở Omuta, mà là ở đây cơ——\nAnh đang nói về việc thông báo ở Yufuin, quê hương của chiếc D51 1031 này.」

- Lý do: Soutetsu trả lời trực tiếp Hibiki (1858 Hibiki nói, 1860 Soutetsu đáp) → với Hibiki Soutetsu xưng "anh" theo quy tắc đã chốt. Bản cũ sai 2 chỗ: đại từ "Tôi" và động từ "đang hỏi về" — JP 「〜の話だ」 là "đang nói về", không phải "đang hỏi về".


### 1973 — サッカー少年Ａ — dịch sai

- JP: 「おわっ！　すごいっちゃ！　真っ黒になったっちゃ」

- TW: 「哇！真拉風！變得黑漆漆的了」

- Cũ: 「Oa! Đỉnh quá! Đen bóng lên rồi kìa.」

- Mới: 「Oa! Đỉnh quá! Đen thui rồi kìa.」

- Lý do: JP 「真っ黒になったっちゃ」 chỉ nói "đen thui"; TW 「變得黑漆漆的了" cũng vậy. Bản cũ thêm "bóng" (bóng loáng) không có trong JP/TW — bịa thêm tính chất. Đối chứng 2392: ở đó JP có ツヤツヤ nên "đen bóng" mới đúng.


### 1986 — 双鉄 — mất tiếng gasp っ

- JP: 「っ！！？」

- TW: 「哎！？！」

- Cũ: 「!!?」

- Mới: 「Ư!!?」

- Lý do: Sweep lost-gasp-whole: JP 「っ！！？」 là tiếng gasp nguyên dòng, VN cũ chỉ còn dấu câu. Áp nguyên giá trị sweep ("Ư!!?").


### 2013 — 双鉄 — đại từ xưng hô

- JP: 「うむ。\nそこは完全に僕も同意だ」

- TW: 「唔。這點我也完全同意」

- Cũ: 「Ừm.\nĐiểm đó thì anh hoàn toàn đồng ý.」

- Mới: 「Ừm.\nĐiểm đó thì tôi hoàn toàn đồng ý.」

- Lý do: Soutetsu nói với Mikuro: cùng mạch với 2009/2011 ("đưa cho cô", "không thể giữ cô lại được") → "anh" sai, phải "tôi".


### 2015 — 双鉄 — mất tiếng gasp っ

- JP: 「っ！」

- TW: 「唔！」

- Cũ: 「!」

- Mới: 「Ư!」

- Lý do: Sweep lost-gasp-whole: JP 「っ！」 nguyên dòng, VN cũ chỉ còn "!". Áp nguyên giá trị sweep ("Ư!").


### 2035 — 双鉄 — mất tiếng gasp っ

- JP: 「っ！！」

- TW: 「啊！！」

- Cũ: 「っ!!」

- Mới: 「Ư!!」

- Lý do: Sweep raw-tsu: JP 「っ！！", VN cũ còn để nguyên っ. Áp nguyên giá trị sweep ("Ư!!").


### 2062 — 日々姫 — SFX

- JP: 「うぇぇ、煙室戸の中、濡れ落ち葉でいっぱい～～、\nこんなのが入る隙間なんて――あ！　煙突からか」

- TW: 「嗚呃呃，煙室門裡有好多濕漉漉的落葉。居然會有縫隙讓這種東西進來……啊！是從煙囪進來的啊」

- Cũ: 「Uwaa, bên trong cửa buồng khói đầy lá khô ướt nhẹp~~\nSao lại có khe hở cho mấy thứ này chui vào chứ——a! Từ ống khói sao.」

- Mới: 「Uêê, bên trong cửa buồng khói đầy lá khô ướt nhẹp~~\nSao lại có khe hở cho mấy thứ này chui vào chứ——a! Từ ống khói sao.」

- Lý do: JP うぇぇ là tiếng khó chịu/ghê tởm (TW 嗚呃呃), không phải tiếng ngạc nhiên うわぁ. Bản cũ "Uwaa" diễn sai âm. Sửa thành "Uêê" (giữ nguyên phần còn lại, kể cả dấu ~~ ASCII của bản cũ).


### 2146 — 双鉄 — thuật ngữ

- JP: 「汚れについては、服を貸し出す。\n『ナッパ服を着る』は、僕らにはもう当然のことだが」

- TW: 「如果擔心弄髒，我們可以租賃服裝。雖然“穿彩頁服”這事對我們來說稀鬆平常…」

- Cũ: 「Về chuyện sợ bẩn thì chúng ta sẽ cho thuê quần áo.\nViệc 『Mặc đồng phục màu』 đối với chúng ta đã là chuyện đương nhiên, nhưng mà...」

- Mới: 「Về chuyện sợ bẩn thì chúng ta sẽ cho thuê quần áo.\nViệc 『Mặc đồ bảo hộ』 đối với chúng ta đã là chuyện đương nhiên, nhưng mà...」

- Lý do: ナッパ服 = quần áo bảo hộ lao động. Toàn dự án dùng "đồ bảo hộ" (Grand 11 2330/2748/3918, ふかみh3 2306 "Trang phục bảo hộ", 凪ふかみ04 2876 "đồng phục bảo hộ"); "đồng phục màu" là dịch theo TW 彩頁服 — TW dịch sai ナッパ→彩頁 ("trang màu").


### 2212 — 日々姫 — đại từ xưng hô

- JP: 「わかるっ！」

- TW: 「我懂！」

- Cũ: 「Chị hiểu!」

- Mới: 「Em hiểu!」

- Lý do: Hibiki nói với Soutetsu: dòng kề trước 2210 Hibiki xưng "Em muốn làm thử!" trong cùng mạch; không có bé trai nào nói trước 2212 để Hibiki xưng "chị" với. Bản cũ "Chị hiểu!" sai người nghe.


### 2224 — 双鉄 — đại từ xưng hô

- JP: 「意外か？　僕の評価が」

- TW: 「我的評價讓你很意外嗎？」

- Cũ: 「Bất ngờ lắm sao? Về đánh giá của anh ấy.」

- Mới: 「Bất ngờ lắm sao? Về đánh giá của anh.」

- Lý do: JP 「僕の評価」 = "đánh giá của tôi/anh" — chính Soutetsu nói về đánh giá của mình. Bản cũ "đánh giá của anh ấy" biến thành ngôi thứ ba — sai hẳn. Người nghe là Hibiki nên tự xưng "anh".


### 2436 — みくろ — dịch sai

- JP: 「いただきます」

- TW: 「美玖路開動了」

- Cũ: 「Mikuro xin phép.」

- Mới: 「Mikuro xin phép ăn đây ạ.」

- Lý do: JP いただきます trước bữa ăn = bắt đầu ăn; TW 「美玖路開動了". Bản cũ "Mikuro xin phép." mất hẳn nghĩa ăn uống. Tiền lệ trong chính file này: 2238 Hibiki いただきます → "Mời mọi người!".


### 2471 — 双鉄 — đại từ xưng hô

- JP: 「ありがとう」

- TW: 「謝謝你」

- Cũ: 「Cảm ơn em.」

- Mới: 「Cảm ơn cô.」

- Lý do: Soutetsu cảm ơn Mikuro (2470 Mikuro vừa nói "xin gửi vào điện thoại của Mikuro"; 2473 Mikuro đáp lại) → gọi "cô" như mọi chỗ khác trong file (1846, 2004, 2441, 2451...). Bản cũ "em" sai.


### 2971 — monologue — dịch sai

- JP: そうするだけの手応えを――\n僕らは、たしかに掴んでいる。

- TW: 此時此刻，我們的確收穫到了令人莞爾的幸福感。

- Cũ: Cảm giác thành tựu khiến chúng tôi muốn làm như vậy——\nChắc chắn chúng tôi đã nắm bắt được rồi.

- Mới: Cảm giác thành quả chỉ từ việc làm như vậy thôi——\nChắc chắn chúng tôi đã nắm bắt được rồi.

- Lý do: JP 「そうするだけの手応えを――僕らは、たしかに掴んでいる」 = "chúng tôi đã nắm được cảm giác thành quả chỉ từ việc làm như vậy thôi". Bản cũ đảo nhân quả: "Cảm giác thành tựu khiến chúng tôi muốn làm như vậy" (cảm giác → muốn làm), ngược hẳn JP. TW cũng diễn lỏng ("thu hoạch được cảm giác hạnh phúc"), lấy JP làm chuẩn.


## §3. Second pass (đọc lại toàn bộ fix đối chiếu JP)

- Đã đọc lại: **14/14 fix** đối chiếu trực tiếp từng giá trị fix với JP (và TW khi cần). **0 loại bỏ, 0 sửa lại.**

- Kiểm tra diff cơ học: mỗi fix chỉ khác bản cũ ở đúng vùng cần sửa (đại từ, từ sai, hoặc chèn Ư) — đã xác nhận bằng diff từng cặp old_vn/fix; không có thay đổi ngoài ý muốn (đặc biệt 2062: giữ nguyên dấu `~~` ASCII và không có dấu phẩy của bản cũ, chỉ đổi "Uwaa"→"Uêê").

- Lưu ý: ứng viên 3059 (gloss 扇形機関庫 "gara đầu máy hình ngành" → "hình quạt") đã LOẠI TRƯỚC second pass: kiểm tra toàn dự án cho thấy gloss này dùng ở ~20 dòng (日々姫02/07/08) — là thuật ngữ thống nhất của dự án, không tự đổi 1 file; chuyển sang §5 để Hieu quyết.


## §4. Các điểm đã kiểm tra và giữ nguyên (không sửa)

- **Soutetsu xưng "anh" với Hibiki là đúng** (1838, 2003, 2218, 2228, 2229, 2285, 2297, 2304) và **"tôi"/"cô" với Mikuro là đúng** (1846, 2004, 2009, 2231, 2441, 2447, 2451, 2528, 2545); **"tôi" ở ngữ cảnh nhóm** là đúng (2036, 2312, 2530, 2543 — tiền lệ Paulette 14 key 1544); **"chú" với bọn trẻ** là đúng (2141, 2185, 2222, 2262, 2382); **"cậu" với nhân viên 職員Ａ** giữ nguyên (giả định nhân viên là nam — xem §5).

- **Mikuro gọi Soutetsu là "anh"** (1978, 2138, 2177, 2413, 2417, 2473, 2536, 2562) — nhất quán với việc cô tự xưng "em" ở 1844; Soutetsu gọi cô là "cô" là cách xưng hô bất đối xứng nhưng ổn định trong cả file, không sửa.

- **静態保存 → "lưu tĩnh" (2458) giữ nguyên**: gloss này dùng ở ~15 dòng toàn dự án (ハチロク08/09/10, Grand 09) — là thuật ngữ đã thống nhất của dự án.

- **粉蔵 = Kokura (1889, 2047) giữ nguyên**: JP 2047 có ruby [こくら,1] cho 粉蔵, TW cũng dịch 小倉 — VN "Kokura" theo đúng ruby + TW (đây là cách viết ateji của 小倉, không phải lỗi).

- **文庫森 → "Bunkomori" (2489) giữ nguyên theo JP** (xem §5: TW chuẩn hoá thành 豐後森/Bungo-Mori).

- **JP cụt được hoàn thiện theo TW (2315, 2897) giữ nguyên**: 2315 "ミーティングのあととかに、園のみんなと" (VN "hay đi cùng mọi người trong sở thú"), 2897 "僕のうかつな発言は、みくろのかつてのマスターのことを。" (VN "đã gợi nhớ đến Master cũ của Mikuro") — cả hai đều theo hướng hoàn thiện của TW, không bịa thêm sự kiện mới.

- **"Đen bóng" ở 2392 giữ nguyên**: ở đó JP có ツヤツヤ (bóng loáng) nên "đen bóng lộn" là đúng — khác với 1973 (JP chỉ có 真っ黒, đã sửa).

- **Các tiếng SFX khác giữ nguyên**: cười うふふ/えへへ → "Fufu"/"He he" (1965, 2081) đúng quy tắc cười là cười; っと cuối câu nhấn mạnh không thêm Ư (1935 "すげっ"→"Đỉnh thật", 2054 "よっと"→"Hây dô"); (ちゅっ！) 2571 → "(Chụt!)"; (ぎいいいっ) 3161 → "(Kétttt)".

- **1997: VN theo JP, không theo TW**: JP "そんなの前からしとる" = "chuyện đó em làm từ lâu rồi"; TW dịch khác hẳn ("我一直都為你感到自豪" — "anh luôn tự hào về em") — lấy JP làm chuẩn, bản cũ đúng.


## §5. Ghi chú cho Hieu (cần quyết, không tự quyết)

- **1877 (uncertain, không tính sai)**: Soutetsu "Cô ấy cất công đến tận Ohimitera tìm tôi à." — "tìm tôi" có thể sai thành "tìm anh" NẾU người nghe là Hibiki (1869 Hibiki vừa báo cáo xong), nhưng người nghe không xác định chắc chắn từ dòng kề (cũng có thể là nhân viên/người lạ → "tôi" đúng). Giữ nguyên bản cũ; cần Hieu xác nhận ngữ cảnh cảnh quay.

- **Thống nhất thuật ngữ (chờ đợt thống nhất)**: "Ohimitera" → "Ohitoyo" (7 dòng, 9 chỗ dùng: 1877, 1890, 1922, 2099 ×2, 2374 ×2, 2439, 2504); 帝鉄 → "Teitetsu" (3128 "Railord kiểu Đường sắt Hoàng gia cũ"); gloss 扇形機関庫 "gara đầu máy hình ngành" (3059; toàn dự án ~20 dòng — "hình ngành" có vẻ là cách diễn không chuẩn của 扇形 "hình quạt", nhưng đã thống nhất toàn dự án nên cần Hieu quyết có đổi hàng loạt không).

- **2489 文庫森**: VN "Bunkomori" theo đúng JP; TW chuẩn hoá thành 豐後森 (Bungo-Mori — địa danh thật ở Oita, xưởng đầu máy nổi tiếng). Hieu quyết có chuẩn hoá theo địa danh thật không.

- **Giả định "cậu" cho nhân viên 職員Ａ** (2136, 2143, 2340, 2503): JP không cho biết giới tính nhân viên; bản dịch dùng "cậu" nhất quán cả file. Nếu nhân viên là nữ thì phải sửa — cần Hieu xác nhận (hoặc để nguyên nếu trong game là nam).


## §6. Khối TOML (14 khóa, đã parse-kiểm chứng: 0 sai lệch giá trị)


```toml
[script]
"1849" = "「Xin lỗi. Tôi đang mải nghĩ ngợi một chút.」"
"1860" = "「Không, không phải thông báo ở Omuta, mà là ở đây cơ——\\nAnh đang nói về việc thông báo ở Yufuin, quê hương của chiếc D51 1031 này.」"
"1973" = "「Oa! Đỉnh quá! Đen thui rồi kìa.」"
"1986" = "「Ư!!?」"
"2013" = "「Ừm.\\nĐiểm đó thì tôi hoàn toàn đồng ý.」"
"2015" = "「Ư!」"
"2035" = "「Ư!!」"
"2062" = "「Uêê, bên trong cửa buồng khói đầy lá khô ướt nhẹp~~\\nSao lại có khe hở cho mấy thứ này chui vào chứ——a! Từ ống khói sao.」"
"2146" = "「Về chuyện sợ bẩn thì chúng ta sẽ cho thuê quần áo.\\nViệc 『Mặc đồ bảo hộ』 đối với chúng ta đã là chuyện đương nhiên, nhưng mà...」"
"2212" = "「Em hiểu!」"
"2224" = "「Bất ngờ lắm sao? Về đánh giá của anh.」"
"2436" = "「Mikuro xin phép ăn đây ạ.」"
"2471" = "「Cảm ơn cô.」"
"2971" = "Cảm giác thành quả chỉ từ việc làm như vậy thôi——\\nChắc chắn chúng tôi đã nắm bắt được rồi."
```


**Tổng cộng sau file này: 73 file / 3.911 dòng sai** (cơ sở 72 file / 3.897 + 14 file này)


## Kết bài


File 日々姫06_みくろ、来訪.txt.toml (02_Hibiki, 482 dòng) đã kiểm tra xong toàn bộ: **14 dòng sai (2,9%)** — thấp hơn hẳn mức trung bình dự án, chủ yếu là lỗi đại từ xưng hô của Soutetsu (6/14: 2 lần "anh" nhầm với Mikuro 1849/2013, 1 lần "tôi" nhầm với Hibiki 1860, 1 lần "chị" của Hibiki 2212, 1 lần "anh ấy" ngôi thứ ba 2224, 1 lần "em" với Mikuro 2471) và 3 tiếng gasp っ theo sweep. 3 lỗi dịch sai tại chỗ: 1973 bịa thêm "bóng", 2436 いただきます mất nghĩa ăn uống, 2971 đảo nhân quả 手応え. 1 lỗi SFX (2062 うぇぇ→"Uwaa" sai âm) và 1 lỗi thuật ngữ (2146 ナッパ服 theo TW sai thành "đồng phục màu"). Không có dòng lệch hàng, không có chuỗi xoay, không có dòng mồ côi hay chưa dịch. Second pass: 14/14 đã đọc lại, 0 loại bỏ, 0 sửa lại. Khối TOML 14 khóa đã parse-kiểm chứng, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 14/14. Còn chờ Hieu: thống nhất "Ohimitera" (7 dòng) + 帝鉄 (1 dòng) + gloss 扇形機関庫, xác nhận người nghe của 1877, xác nhận giới tính nhân viên 職員Ａ, và quyết có chuẩn hoá 文庫森 thành Bungo-Mori không.
