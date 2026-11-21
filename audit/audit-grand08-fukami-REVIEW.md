# Audit — グランドリライト08_ふかみ.txt.toml (07_Nagi_Fukami / 09_Grand)

- File: `グランドリライト08_ふかみ.txt.toml` — TOML-2: `sources/toml2/translation_toml/07_Nagi_Fukami/#U30b0#U30e9#U30f3#U30c9#U30ea#U30e9#U30a4#U30c808_#U3075#U304b#U307f.txt.toml` (bản sao y hệt ở `09_Grand/` — xem dưới).
- Route: 07_Nagi_Fukami theo queue. Nội dung: Fukami trở về sau 1 năm tu nghiệp ở Khách sạn Teio, trình bày ý tưởng "góc nhìn của loài kiến / góc nhìn của loài chim"; cả nhóm họp bàn thiết kế Nine Stars (lối vào chung, khoang giường nằm, vật tư/thiết bị), vốn (Quỹ My Rail, Ngân hàng Kumamoto, ngân hàng Pháp qua Maia), sự cố sụt lún hầm mỏ bỏ hoang / lấp đất gia cố, kho bảo quản rác 24h, nhân sự phục vụ, thiết bị chuyên dụng; xen kẽ cảnh Michiko ngủ mơ thấy bố mẹ, Soutetsu đánh thức con bé. Không có cảnh H.
- Đọc: **485/485 dòng** (keys 73–2999, section `script`: monologue 179, thoại 双鉄 112, ふかみ 69, 日々姫 42, 路子 29, 稀咲 22, 凪 14, ポーレット 9, ハチロク 4, れいな 4, 真闇 1), đọc từng dòng JP + TW + VN đối chiếu.
- **Sai: 16/485 (3,3%)**.
- Phân loại: gasp 5 (1772, 1801, 1822, 1845, 1846 — cả 5 từ sweep, áp nguyên), thuật ngữ 3 (1273, 1722, 2094: 冥国 "Mỹ"→"Minh Quốc"), đại từ 4 (2106 Fukami gọi Soutetsu "chị"→"anh"; 2136 Kisaki tự xưng "tôi"→"em" + sửa chủ ngữ; 2180, 2226 Fukami gọi Nagi "em"→"cậu"), dịch sai nghĩa 3 (2063, 2069 思う/思います→"Nên ạ!"; 2548 小走り→"chạy chậm bước đi"), nguyên âm 1 (1245 ああっ→"A.").
- **0 lệch dòng / 0 chuỗi xoay / 0 nhiễm chéo / 0 dòng mồ côi / 0 dòng chưa dịch / 0 khóa trùng.** JP/TW/VN khớp nhau ở mọi dòng đã đọc; không có VN nào là lời thoại của file khác. VN lặp ở 2 cặp key: (1792, 1794) cùng 「Hừm.」— JP khác nhau (むぅ vs ふむ), cùng 1 âm gằn, không phải lệch; (2063, 2069) cùng 「Nên ạ!」— cả 2 đều sai giống nhau (đã sửa cả 2 thành "Em nghĩ vậy ạ!"). Chỉ 1 dòng VN==JP/TW về dấu câu: 1222 「…………」— không tính chưa dịch. 0 dòng VN trống.
- TOML md5: `f4a758d4dba4509b768cab2644c66837` — **2 bản sao giống hệt nhau** (`07_Nagi_Fukami/` và `09_Grand/`, cùng md5); fix áp dụng cho CẢ 2 bản. `[selections]` rỗng ({}). Tag `%l`: 0 lệch (số tag JP == VN ở mọi dòng). File UTF-8 BOM + CRLF.
- Cơ sở tổng: **156 file / 6.997 dòng sai** (đã kiểm chứng trực tiếp với dòng tổng cuối của ROUTE-AUDIT.md — khớp đúng cơ sở task giao, không cần rebase).

## §0. Phát hiện quan trọng: CSV3 có 2 set cho file này — chỉ 1 set đúng (485 dòng, không phải 970)

Queue ghi file này "970 dòng script" — thực tế TOML chỉ có **485 key script**. CSV3 có 2 set cùng tên file, mỗi set 485 dòng:

- **Set 09_Grand (đúng, dùng để audit):** key khớp TOML 485/485; VN khớp TOML 485/485 sau khi chuẩn hóa khoảng trắng (153 khớp tuyệt đối, 332 dòng còn lại chỉ khác ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng — theo quy tắc, CSV3 là chuẩn cho fix list). JP trong comment `# JP:` của TOML khớp set này (đã kiểm chứng key 73, 1145, 1148, 1149, 1152).
- **Set 07_Nagi_Fukami (STALE, bỏ):** VN khớp TOML 0/485; JP khác set đúng ở 474/485 key (nội dung cảnh khác hẳn — vd. key 73 JP 「それでは双鉄様、いってまいります」vs set đúng 「レイルロオド組が部屋を出ていくと同時」). Theo quy tắc dual-set trong brief (set "home folder" là stale), bỏ set này, chỉ audit set 09_Grand. 11 key JP trùng nhau giữa 2 set (trong đó có 1693, 1703, 1790, 2484, 2626 — xem §2).
- Hệ quả: **file này chỉ audit 485 dòng** (không phải 970). Nội dung set stale (485 dòng JP khác) không có TOML tương ứng nên không audit được ở đây — ghi nhận để parent xem xét (có thể là nội dung cũ trước "Grand Rewrite", hoặc TOML-2 đã ghi đè nhầm bản 09_Grand lên cả 2 thư mục).

## §1. Đại từ — 4 dòng (SỬA)

- **2106 [ふかみ] — Fukami gọi Soutetsu "chị"→"anh".** JP 「平気です。けど、お気遣いありがとうございます」. Dòng 2105 ngay trước là Soutetsu nói trực tiếp với Fukami (「いや、聞かせてくれ、ふかみ」— "Không sao, em cứ nói đi, Fukami"), và 2108 Fukami tiếp tục đáp lại Soutetsu; người "quan tâm" (お気遣い) là Soutetsu → "cảm ơn anh đã quan tâm". VN cũ "cảm ơn chị" gán nhầm người nghe là nữ.
- **2136 [稀咲] — Kisaki tự xưng "tôi"→"em" (×2) + sửa chủ ngữ.** JP 「皆がいるところで持ち出さなかったのだから、ボクもいない方がいいね？　決まったら知らせて欲しい」. (a) Kisaki tự xưng "em" với Soutetsu (quy tắc đã khóa: Kisaki "em" với Soutetsu, "tôi" với Paulette). Người nghe là Soutetsu: TW dùng 你 ("ngươi" — ngôi 2) cho chủ ngữ 持ち出さなかった, và 2130/2131 Soutetsu vừa tự ngắt lời mình khi định nói về Paulette (「で、ポーレットは――」「そうて――っと」) — chính Soutetsu là người "không tiện nói ra trước mặt mọi người". (b) Vì vậy vế đầu VN cũ "em không tiện nói" gán sai chủ ngữ cho Kisaki → sửa thành "cậu không tiện nói" (Kisaki gọi Soutetsu là "cậu" — tiền lệ 1702, 2290 trong chính file này). VN cũ còn lẫn lộn "em" (vế đầu) và "tôi" (2 lần sau) cho cùng 1 người nói trong 1 câu. Fix: 「Vì lúc nãy có mọi người ở đây cậu không tiện nói, nên chắc em cũng không nên ở lại nhỉ? Quyết định xong thì báo cho em biết nhé.」
- **2180, 2226 [ふかみ] — Fukami gọi Nagi "em"→"cậu" (×2).** Fukami và Nagi CÙNG TUỔI — quy tắc đã khóa: Fukami→Nagi là "cậu", không bao giờ "em" (tiền lệ đã merge: file khác sửa "Fukami 'em'→'cậu' với Nagi 2453"). 2180 「ありがと、凪ちゃん。気をつけて」→ "Cảm ơn cậu, Nagi-chan. Đi cẩn thận nhé." 2226 Fukami hướng dẫn Nagi tưởng tượng ("Hãy ghi nhớ những gì cậu vừa thấy…") → "cậu".
- Kiểm chứng toàn bộ đại từ Soutetsu: thoại 双鉄 dùng "anh" ở 13 dòng (1269, 1647, 1665, 1790, 1836, 1854, 1892, 1899, 1960, 2086, 2138, 2140, 2165) — người nghe đều là Fukami/Hibiki/Michiko/nhóm (đúng quy tắc "anh"); dùng "tôi" chỉ ở 2 dòng (1997, 2146) — cả 2 đều nói với Kisaki (đúng quy tắc "tôi" với Kisaki; 1997 hỏi về "mạng lưới quan hệ… của Kisaki", 2146 đáp lại mạch "mối liên hệ lớn" của Kisaki ở 2094/2110). Soutetsu gọi Kisaki "cô" ở 2074 ("Sao sắc mặt cô tệ vậy") — ĐÚNG theo quy tắc (Soutetsu với Kisaki là "tôi" và gọi "cô"). Độc thoại Soutetsu dùng "tôi" xuyên suốt — đúng (ngôi kể); riêng 2998 độc thoại nội tâm dùng "mình" — đúng theo ngoại lệ "Soutetsu inner monologue = mình" (câu hỏi nội tâm về giấc mơ). Nagi gọi Fukami: 0 lần "chị" trong file (chỉ "chị Hachiroku" ở 1264, 1663 — đúng). Fukami tự xưng "mình": 0 dòng trong file (không có gì để sửa). Hachiroku tự xưng "tôi" (2272, 2289 — đúng, trang trọng). Mayami tự xưng "chị" ở 1902 (おねーちゃん — đúng).

## §2. Gasp っ — sweep kiểm chứng, áp nguyên cả 5 fix

Sweep có **10 mục** cho file này (đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`): **5 fix thuộc set 09_Grand, áp nguyên sau khi kiểm chứng từng giá trị vs JP** (1772 lost-gasp-trailing: でこぴん～っ → "~Ư"; 1801 lost-gasp-whole: っ！→"Ư!"; 1822 lost-gasp-whole: っ！！？→"Ư!!?"; 1845 lost-gasp-trailing: うむ？――っ！→"Hửm? ――Ư!"; 1846 lost-gasp-trailing: おお！/――っ！→"Ồ!"/"――Ư!"). **5 mục needs-file-audit mang nhãn 07_Nagi_Fukami (1693, 1703, 1790, 2484, 2626) đã kiểm chứng, KHÔNG sửa**: JP của 5 mục này trùng tuyệt đối với JP set đúng ở cùng key (thuộc 11 key JP trùng giữa 2 set); các dòng tương ứng trong set đúng đã đọc kỹ trong audit này và không có gasp nào mất (1693 Hibiki nói dài, 1703 「そうか？」→"Vậy sao?", 1790 「ああ、すまん。ついというか、思わずというか」→"A, xin lỗi. Là anh lỡ tay…", 2484 độc thoại không có っ cuối, 2626 độc thoại 「わずかに震える指先で――」không có っ).

Quét máy bổ sung toàn bộ dòng JP chứa っ: không tìm thêm gasp nào sweep bỏ sót ngoài 1245 (xem §4 — nguyên âm, không phải gasp). Các っ đã diễn đúng, giữ nguyên: 1205 にぃにっ→"Anh hai!" (っ gắn từ nội dung, "!" diễn nhấn), 1631 一週間っ→"Một tuần!!?", 1795 っ――→"Ư――", 1823 ふがっ/んにゅっ/んっ/ふぁっ/ぷはあっ→"Fuga!? Nnyu!? Ưm――Fua! Puhaa!!?", 1999 あのっ→"Anh này!", 2131 っと→"à." (tự sửa lời), 2994 （ぱちっ）→（Búng）, 2997 （むにっ）→（Bóp） (SFX ngoặc đơn diễn bằng nghĩa, theo quy ước file).

## §3. Thuật ngữ — 冥国 "Mỹ"→"Minh Quốc" (3 dòng — SỬA)

Quyết định 19/11 đã chốt: 冥国 = "Minh Quốc" (JP thắng TW 美國; furigana めいこく là cách đọc, không phải tên nước thật). Tiền lệ đã merge nhiều file: 凪ふかみ01 sửa 13 dòng 冥国→"Minh Quốc" (trong đó 1587 cùng ngữ cảnh liệt kê quốc gia: "Anh, Minh Quốc và Đức"), 00common11 sửa 2 dòng, hachiroku02, file khác sửa "Mỹ"→"Minh Quốc" ở 1741/2766, 2479, 2585/3038.

- **1273** Soutetsu: 「必要なのは、鴎州なり冥国なりへの太いパイプか」→ "…đường dây lớn nối tới Châu Âu hay Minh Quốc sao." (chỉ sửa "Mỹ"→"Minh Quốc"; 鴎州→"Châu Âu" giữ nguyên.)
- **1722** Fukami liệt kê quốc gia: [めいこく,1]冥国、[えいこく,1]詠国、[どっこく,1]髑国、フランク、[ちゅうごく,1]仲国、[かんこく,1]汗国 → "Đường ray ở các nước như Minh Quốc, Anh, Đức, Pháp, Trung Quốc, Hàn Quốc thì sao?" (chỉ sửa "Mỹ"→"Minh Quốc"; 詠国→"Anh", 髑国→"Đức", 仲国→"Trung Quốc", 汗国→"Hàn Quốc" giữ nguyên theo quy ước thế giới hư cấu đã ghi trong ROUTE-AUDIT — chỉ riêng 冥国 có quyết định chốt "Minh Quốc".)
- **2094** Kisaki: 「鴎州や冥国との、太いパイプはほとんどないね」→ "Hầu như không có mối liên hệ lớn nào với Châu Âu hay Minh Quốc."

## §4. Dịch sai nghĩa + nguyên âm (4 dòng — SỬA)

- **2063 [日々姫] + 2069 [ふかみ] — 思う/思います dịch thành "Nên ạ!" (sai nghĩa).** 2063 Hibiki 「思う！」(đáp lại Soutetsu 2062 "nghe được điều đó thật đáng mừng") và 2069 Fukami 「思います、です！」đều là "(Tôi) nghĩ vậy!" — TW cả 2 đều là 是的 ("Đúng vậy!"). VN cũ "Nên ạ!" (nên làm!) là bịa nghĩa khác hẳn. Cả 2 sửa thành "Em nghĩ vậy ạ!" (Hibiki và Fukami đều tự xưng "em").
- **2548 [monologue] — 小走り dịch thành "chạy chậm bước đi".** JP 「凪が小走りに駆け出していく」— 小走り = chạy bước nhỏ (những bước chạy ngắn, nhanh), TW 小跑著離開了 ("chạy lon ton rời đi"). VN cũ "chạy chậm bước đi" vừa tự mâu thuẫn (chạy chậm + bước đi) vừa sai nghĩa. Sửa: "Nagi chạy bước nhỏ đi."
- **1245 [稀咲] — nguyên âm.** JP 「――んっ。ああっ」— ああっ có 2 âm a; VN cũ "Ưm. A." chỉ 1 a. Sửa: "――Ưm. Aa." (dấu chấm diễn っ ngắt; tiền lệ lr_reinah1 1244 ああ――→"Aa——", 1288 ぁあ→"Aa.").

## §5. Giữ nguyên (không tính sai)

- **Đợt thống nhất (ghi nhận, KHÔNG sửa trong audit này):**
  - 日ノ本 "Hinamoto" **12 dòng**: 1648, 1948, 2008, 2017, 2032, 2044, 2271, 2289, 2553, 2634, 2746, 2966 — đúng bằng số lượng brief đã kê cho Grand 08 (×12), chờ đợt thống nhất sửa thành "Hinomoto".
  - 御一夜 dạng cũ "Ohito" **5 dòng**: 1871, 2519, 2562, 2604, 2623 — chờ đợt thống nhất sửa thành "Ohitoyo" (theo tiền lệ 日々姫08: dạng cũ không tính sai trong audit).
  - 電車姫 "ngài Denshahime" **1 dòng**: 2086 — chờ đợt thống nhất sửa thành "Công chúa Tàu điện".
  - まいてつ **3 dòng**: 2123 "giới đường sắt", 2572 + 2595 "ông trùm đường sắt" — chờ đợt thống nhất sửa thành "chủ tàu".
  - 湯医線 "Yui" **1 dòng**: 2260 "Tuyến Rail Romanesque Yui" — bổ sung vào danh mục đợt thống nhất (hiện chỉ kê P14 83, P16 2032), sửa thành "Yunoi".
  - Tổng ghi nhận đợt thống nhất: 22 dòng.
- **2947 — Seki KHÔNG sửa.** JP 「僕らとも翠さんとも堰さんたちとも」→ "Xa cách chúng tôi, cô Midori, ông Seki và mọi người." VN dùng dạng tên "ông Seki" (nhất quán với "ông Goto", "ông Mototada" trong file), không dùng "ông nội" nên không thuộc diện sửa "ông nội"→"ông ngoại" theo quyết định Seki. Đây là dòng Seki duy nhất trong file (堰 chỉ xuất hiện 1 lần).
- **2072 + 2172 — Fukami tự sửa lời 双鉄おにいさん→双鉄さん, VN diễn cả 2 vế thành "anh Soutetsu".** Sự khác biệt thanh điệu (thân mật おにいさん vs trang trọng さん) không có cách diễn tương đương gọn trong tiếng Việt; VN giữ nguyên cả 2 vế, không gộp — ghi nhận, không tính sai (tiền lệ brief: self-correction さん→くん ở file 07 là có chủ ý, không được "sửa" mất).
- **2074 — っ！？ giữa dòng giữ "!?"** (Soutetsu 「稀咲か――っ！？――どうした、その顔色は」→"Kisaki à――!? ――Sao sắc mặt cô tệ vậy."). Sweep không flag; dấu "!?" sau gạch ngang đã diễn sự ngắt đột ngột — khác 1801/1822 là cả dòng chỉ có gasp.
- **1628 / 1858 / 1895 — 帝央ホテル → "Khách sạn Teio".** Giữ nguyên: 帝央 đọc ていおう, "Teio" là phiên âm Hepburn hợp lệ cho tên riêng khách sạn (TW dịch nghĩa 帝都中央車站酒店 nhưng JP thắng TW với tên riêng; chưa có quyết định chốt nào cho 帝央).
- **1273 義父さん → "bố nuôi" — ĐÚNG, giữ nguyên.** TW ghi 養父 (cha nuôi) nên "bố nuôi" hợp lệ theo quy tắc brief (chỉ khi TW nói 養父/養母 mới được dùng "bố/mẹ nuôi"). Tương tự 2146 義父さん→"bố nuôi".
- **Các dòng chỉ khác TOML-2 làm phẳng `\n`** (332 dòng) — không phải lỗi dịch, CSV3 là chuẩn.
- **Tag `%l`:** 0 lệch (mọi dòng JP có tag thì VN có đủ tag, gloss đúng: 機関士→"Lái tàu" ở 1906; 客車→"Toa hành khách" ở 1964; 入換→"dồn toa" ở 2920; レイルロオド→"Railord" ở 73, 2761).

## §6. Chi tiết từng dòng sai (16)

### 1245 [稀咲] — vowel
- JP: 「――んっ。ああっ」
- TW: 「……呼，嗯」
- VN cũ: 「――Ưm. A.」
- **Fix:** 「――Ưm. Aa.」
- ああっ có 2 âm a, VN cũ chỉ 1 a. んっ→"Ưm" đã đúng.

### 1273 [双鉄] — terminology
- JP: 「……必要なのは、鴎州なり冥国なりへの太いパイプか。真闇姉や義父さんも、単純な知り合いならばいようが」
- TW: 「……那麼我們需要的就是歐洲、美國那邊的大人物支持。真闇姐和[父親,1]養父或許有些普通的熟人」
- VN cũ: 「……Thứ chúng ta cần là một đường dây lớn nối tới Châu Âu hay Mỹ sao.\nChị Mayami hay bố nuôi chắc cũng có người quen bình thường, nhưng mà.」
- **Fix:** 「……Thứ chúng ta cần là một đường dây lớn nối tới Châu Âu hay Minh Quốc sao.\nChị Mayami hay bố nuôi chắc cũng có người quen bình thường, nhưng mà.」
- 冥国 = "Minh Quốc" theo quyết định 19/11 (JP thắng TW 美國).

### 1722 [ふかみ] — terminology
- JP: 「もっと高く。衛星軌道にまで飛んで？　どう見える？\n[めいこく,1]冥国、[えいこく,1]詠国、[どっこく,1]髑国、フランク、[ちゅうごく,1]仲国、[かんこく,1]汗国とかの線路は」
- TW: 「再飛高點，飛上衛星軌道。美國、英國、德國、法國、仲國、韓國的線路，看起來怎麼樣？」
- VN cũ: 「Cao hơn nữa. Bay lên tận quỹ đạo vệ tinh xem? Trông như thế nào?\nĐường ray ở các nước như Mỹ, Anh, Đức, Pháp, Trung Quốc, Hàn Quốc thì sao?」
- **Fix:** 「Cao hơn nữa. Bay lên tận quỹ đạo vệ tinh xem? Trông như thế nào?\nĐường ray ở các nước như Minh Quốc, Anh, Đức, Pháp, Trung Quốc, Hàn Quốc thì sao?」
- Chỉ sửa 冥国→"Minh Quốc"; các nước còn lại giữ nguyên theo quy ước thế giới hư cấu (tiền lệ 凪ふかみ01 1587: "Anh, Minh Quốc và Đức").

### 1772 [路子] — gasp (sweep)
- JP: 「ひゃうっ！？　や、でこぴん～っ」
- TW: 「呀？！討厭，彈人家額頭」
- VN cũ: 「Hyau!? Ây, anh búng trán em~」
- **Fix:** 「Hyau!? Ây, anh búng trán em~Ư」
- Sweep lost-gasp-trailing, áp nguyên giá trị sweep. ひゃうっ→"Hyau!?" đúng quy tắc romaji họ ひゃ; っ cuối でこぴん～っ bị mất trong VN cũ.

### 1801 [双鉄] — gasp (sweep)
- JP: 「っ！」
- TW: 「啊！」
- VN cũ: 「!」
- **Fix:** 「Ư!」
- Sweep lost-gasp-whole, áp nguyên giá trị sweep. Cả dòng chỉ có gasp, VN cũ mất hẳn âm.

### 1822 [双鉄] — gasp (sweep)
- JP: 「っ！！？」
- TW: 「啊？！」
- VN cũ: 「!!?」
- **Fix:** 「Ư!!?」
- Sweep lost-gasp-whole, áp nguyên giá trị sweep.

### 1845 [双鉄] — gasp (sweep)
- JP: 「うむ？　――っ！」
- TW: 「嗯？　……啊！」
- VN cũ: 「Hửm? ――!」
- **Fix:** 「Hửm? ――Ư!」
- Sweep lost-gasp-trailing, áp nguyên giá trị sweep.

### 1846 [双鉄] — gasp (sweep)
- JP: 「おお！」\n「――っ！」
- TW: 「噢！」\n「啊！」
- VN cũ: 「Ồ!」\n「――!」
- **Fix:** 「Ồ!」\n「――Ư!」
- Sweep lost-gasp-trailing, áp nguyên giá trị sweep.

### 2063 [日々姫] — mistranslation
- JP: 「思う！」
- TW: 「是的！」
- VN cũ: 「Nên ạ!」
- **Fix:** 「Em nghĩ vậy ạ!」
- 思う = "nghĩ vậy", không phải "nên" (nên làm). Hibiki đáp lại Soutetsu 2062.

### 2069 [ふかみ] — mistranslation
- JP: 「思います、です！」
- TW: 「是的，嗯！」
- VN cũ: 「Nên ạ!」
- **Fix:** 「Em nghĩ vậy ạ!」
- 思います = "nghĩ vậy", không phải "nên". Fukami tự xưng "em".

### 2094 [稀咲] — terminology
- JP: 「鴎州や冥国との、太いパイプはほとんどないね。\n単純な知人であれば、あちらにも少しはいるけど」
- TW: 「歐洲跟美國那邊基本上沒什麼特別有地位的熟人。普通熟人倒也不是沒有」
- VN cũ: 「Hầu như không có mối liên hệ lớn nào với Châu Âu hay Mỹ.\nNếu chỉ là người quen bình thường thì bên đó cũng có một ít.」
- **Fix:** 「Hầu như không có mối liên hệ lớn nào với Châu Âu hay Minh Quốc.\nNếu chỉ là người quen bình thường thì bên đó cũng có một ít.」
- 冥国 = "Minh Quốc" theo quyết định 19/11.

### 2106 [ふかみ] — pronoun
- JP: 「平気です。けど、お気遣いありがとうございます」
- TW: 「沒事，謝謝關心」
- VN cũ: 「Em không sao ạ. Nhưng mà, cảm ơn chị đã quan tâm.」
- **Fix:** 「Em không sao ạ. Nhưng mà, cảm ơn anh đã quan tâm.」
- Người nghe là Soutetsu: dòng 2105 ngay trước là Soutetsu nói trực tiếp với Fukami; 2108 Fukami tiếp tục đáp Soutetsu. "Chị" gán nhầm người nghe.

### 2136 [稀咲] — pronoun
- JP: 「皆がいるところで持ち出さなかったのだから、ボクもいない方がいいね？　決まったら知らせて欲しい」
- TW: 「畢竟大家都在場的時候你沒提出來，那想必是我也不方便聽這件事。定好了記得通知我」
- VN cũ: 「Vì lúc nãy có mọi người ở đây em không tiện nói,\nnên chắc tôi cũng không nên ở lại nhỉ? Quyết định xong thì báo cho tôi biết nhé.」
- **Fix:** 「Vì lúc nãy có mọi người ở đây cậu không tiện nói,\nnên chắc em cũng không nên ở lại nhỉ? Quyết định xong thì báo cho em biết nhé.」
- Kisaki tự xưng "em" với Soutetsu (quy tắc đã khóa). Chủ ngữ 持ち出さなかった là Soutetsu (TW 你; 2130/2131 Soutetsu tự ngắt lời khi định nói về Paulette) → "cậu không tiện nói" (Kisaki gọi Soutetsu là "cậu", tiền lệ 1702/2290). VN cũ lẫn "em" + "tôi" cho cùng 1 người nói trong 1 câu.

### 2180 [ふかみ] — pronoun
- JP: 「ありがと、凪ちゃん。気をつけて」
- TW: 「謝謝你，小凪，小心一點」
- VN cũ: 「Cảm ơn em, Nagi-chan. Đi cẩn thận nhé.」
- **Fix:** 「Cảm ơn cậu, Nagi-chan. Đi cẩn thận nhé.」
- Fukami→Nagi là "cậu" (cùng tuổi, quy tắc đã khóa).

### 2226 [ふかみ] — pronoun
- JP: 「それが、蟻の視点。今見えたものを忘れないまま、\n今度は、鳥になって、線路の上を飛んでみて？」
- TW: 「這就是螞蟻的視角。那麼在這個視角的基礎上，你再讓自己化身飛鳥，俯瞰一下線路試試？」
- VN cũ: 「Đó là góc nhìn của loài kiến. Hãy ghi nhớ những gì em vừa thấy,\nvà lần này, thử biến thành một chú chim, bay lượn trên đường ray xem sao?」
- **Fix:** 「Đó là góc nhìn của loài kiến. Hãy ghi nhớ những gì cậu vừa thấy,\nvà lần này, thử biến thành một chú chim, bay lượn trên đường ray xem sao?」
- Fukami đang hướng dẫn Nagi tưởng tượng → người nghe là Nagi → "cậu".

### 2548 [monologue] — mistranslation
- JP: 「凪が小走りに駆け出していく。」
- TW: 「凪小跑著離開了。」
- VN cũ: 「Nagi chạy chậm bước đi.」
- **Fix:** 「Nagi chạy bước nhỏ đi.」
- 小走り = chạy bước nhỏ (bước chạy ngắn, nhanh); "chạy chậm bước đi" tự mâu thuẫn và sai nghĩa.

## Khối TOML (đã parse-verified)

```toml
[script]
"1245" = "「――Ưm. Aa.」"
"1273" = "「……Thứ chúng ta cần là một đường dây lớn nối tới Châu Âu hay Minh Quốc sao.\\nChị Mayami hay bố nuôi chắc cũng có người quen bình thường, nhưng mà.」"
"1722" = "「Cao hơn nữa. Bay lên tận quỹ đạo vệ tinh xem? Trông như thế nào?\\nĐường ray ở các nước như Minh Quốc, Anh, Đức, Pháp, Trung Quốc, Hàn Quốc thì sao?」"
"1772" = "「Hyau!? Ây, anh búng trán em~Ư」"
"1801" = "「Ư!」"
"1822" = "「Ư!!?」"
"1845" = "「Hửm? ――Ư!」"
"1846" = "「Ồ!」\\n「――Ư!」"
"2063" = "「Em nghĩ vậy ạ!」"
"2069" = "「Em nghĩ vậy ạ!」"
"2094" = "「Hầu như không có mối liên hệ lớn nào với Châu Âu hay Minh Quốc.\\nNếu chỉ là người quen bình thường thì bên đó cũng có một ít.」"
"2106" = "「Em không sao ạ. Nhưng mà, cảm ơn anh đã quan tâm.」"
"2136" = "「Vì lúc nãy có mọi người ở đây cậu không tiện nói,\\nnên chắc em cũng không nên ở lại nhỉ? Quyết định xong thì báo cho em biết nhé.」"
"2180" = "「Cảm ơn cậu, Nagi-chan. Đi cẩn thận nhé.」"
"2226" = "「Đó là góc nhìn của loài kiến. Hãy ghi nhớ những gì cậu vừa thấy,\\nvà lần này, thử biến thành một chú chim, bay lượn trên đường ray xem sao?」"
"2548" = "Nagi chạy bước nhỏ đi."
```

## Lượt soát 2

- Đã đọc lại toàn bộ 16 fix đối chiếu từng dòng JP (lượt soát 2): **16/16 re-verified, 0 bỏ, 0 sửa**.
- JSON 16 mục, khối TOML [script] 16 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 16/16; mỗi fix chỉ khác old VN ở đúng chỗ sửa (diff-sanity: tỉ lệ tương đồng 0,80–0,98; chỉ 2063/2069 là 0,50 vì cả dòng ngắn bị dịch sai toàn bộ — đã kiểm chứng trong lượt soát 2).
- 5/5 fix gasp khớp tuyệt đối giá trị sweep trong `sweep-raw-gasp-wrong.json`.

## Chờ Hieu / ghi nhận (chỉ ghi nhận, không cần quyết ngay)

- **CSV3 dual-set (§0):** set 07_Nagi_Fukami (485 dòng JP khác hẳn) không có TOML tương ứng — nội dung đó là gì (bản cũ trước Grand Rewrite, hay TOML-2 ghi đè nhầm)? Có cần tìm/audit riêng 485 dòng đó không, hay bỏ hẳn như set stale?
- **Đợt thống nhất (22 dòng, §5):** 日ノ本 "Hinamoto" 12 dòng, 御一夜 "Ohito" 5 dòng, 電車姫 "ngài Denshahime" 1 dòng, まいてつ 3 dòng, 湯医線 "Yui" 1 dòng (2260 — bổ sung vào danh mục, hiện chỉ kê P14 83, P16 2032).
- **2072/2172** tự sửa lời 双鉄おにいさん→双鉄さん: VN diễn cả 2 vế thành "anh Soutetsu" (mất khác biệt thanh điệu) — có cách diễn nào giữ được khác biệt này trong tiếng Việt không, hay chấp nhận?
- **1628/1858/1895** 帝央ホテル → "Khách sạn Teio": giữ dạng phiên âm tên riêng; TW dịch nghĩa là "Khách sạn ga trung tâm Đế đô" — có cần thống nhất 1 dạng cho 帝央 toàn dự án không?

## Kết bài

File グランドリライト08_ふかみ: 485 dòng đã đọc hết, **16 dòng sai (3,3%)** — lỗi tập trung ở gasp sweep (5 dòng), thuật ngữ 冥国 (3 dòng), đại từ (4 dòng: 1 Fukami→Soutetsu, 1 Kisaki, 2 Fukami→Nagi), dịch sai nghĩa (3 dòng) và nguyên âm (1 dòng). Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Sweep đã kiểm chứng trực tiếp: 5 fix áp nguyên, 5 mục needs-file-audit (nhãn stale) đã kiểm chứng không sửa; quét máy bổ sung toàn bộ dòng JP chứa っ — không tìm thêm gasp nào sweep bỏ sót. Lượt soát 2: 16/16, 0 bỏ, 0 sửa. Phát hiện chính ngoài lỗi dịch: CSV3 có 2 set cho file này, chỉ set 09_Grand khớp TOML (485 dòng); set 07_Nagi_Fukami là stale (0/485 khớp) và nội dung của nó không có TOML tương ứng.
