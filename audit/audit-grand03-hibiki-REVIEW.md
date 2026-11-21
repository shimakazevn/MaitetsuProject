# Kiểm tra bản dịch — グランドリライト03_日々姫.txt.toml (route 02_Hibiki / 09_Grand)

## Thông tin file

- **File:** `グランドリライト03_日々姫.txt.toml` — Grand Rewrite 03 — Hibiki.
- **Đường dẫn TOML (task giao):** `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/02_Hibiki/#U30b0#U30e9#U30f3#U30c9#U30ea#U30e9#U30a4#U30c803_#U65e5#U3005#U59eb.txt.toml` — **lưu ý:** file này còn có một bản sao thứ hai ở `09_Grand/` với cùng tên; cả hai bản có cùng md5 (xem dưới). Task giao đúng đường dẫn 02_Hibiki; route ghi trong queue là 02_Hibiki.
- **md5 TOML:** `638d22cb032e067b663ad42349d027a0` — bản sao trong `09_Grand/` có cùng md5 (2 bản, giống hệt nhau; fix áp dụng cho cả 2). UTF-8 BOM + CRLF.
- **CSV3 master:** `~/workspace/maitetsu-pilot/sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv` — 469 dòng cho file này, 1 set duy nhất, khóa duy nhất, 0 VN trống.
- **Kiểm tra phẳng:** VN khớp phẳng TOML 469/469 (sau khi chuẩn hoá literal `\n` thành khoảng trắng — TOML-2 làm phẳng `\n` literal; CSV3 là chuẩn theo quy tắc, không phải lỗi VN, không tính sai).
- **Nhân vật (số dòng):** monologue 158, 双鉄 153, 日々姫 138, 路子 12, ナビ 8.
- **Nội dung:** Soutetsu và Hibiki cùng làm việc cho dự án khôi phục tuyến đường — thiết kế bản đồ minh họa lưu vực sông Kuma, làm báo miễn phí, quảng bá Hibiki; Hibiki ứng cử làm 機関助士 (phụ lái tàu) trên 8620; Michiko (Railord nhí) chờ bố mẹ đến đón; Soutetsu đi viếng mộ bố mẹ, lo chuyện đền bù giải tỏa đất phân lô; xen kẽ cảnh Hibiki phối đồ/đi mua vest cho Soutetsu (áo sơ mi hãng OHITOYO). Không có H-scene.
- **`[characters]`:** 2638=Navi, 2705=Soutetsu, 2893=Hibiki, 3108=Michiko — các key này không phải key script (đánh dấu đổi nhân vật hiển thị), đã kiểm chứng không sai. **`[selections]`** rỗng.

## Kết quả tổng

- **Đã đọc: 469/469 dòng. Sai: 26 (5,5%).**
- **Phân loại (26 dòng / 27 điểm):** thuật ngữ 13 (御一夜 "Ohitera"→"Ohitoyo" 13 dòng: 1525, 2047, 2138, 2168, 2189, 2320, 2377, 2419, 2504, 2755, 2761, 2828, 3177 — 2419 mang 2 lần trong cùng 1 dòng nên tổng điểm là 27); xưng hô 6 (1975, 2118, 2241: Soutetsu "cô/tôi/mình"→"em/anh" khi nói với Hibiki; 3025, 3100, 3133: độc thoại Soutetsu "anh"→"tôi"); sai nghĩa 6 (2348, 2537, 2874, 2989, 3063, 3138); lỗi nhỏ 1 (2428: っ thô từ sweep).
- **Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.** Không có chuỗi lệch dòng: mọi VN đều là bản dịch của chính JP của nó (đã kiểm chứng bằng đọc từng dòng đối chiếu JP+TW; không có VN mồ côi, không có dòng JP nào thiếu VN).
- **Nhóm VN trùng lặp (hợp lệ, không tính sai):** 「A.」2023/2033; 「À――」2034/2051/2097/2300; 「A!」2035/2312 — đều là cảm thán ngắn mà JP cũng giống nhau.
- **Tag `%l`:** 0 lệch số lượng tag JP vs VN. Hai tag do VN tự thêm từ ruby JP — 1879 ([キャブ,2] → tag %l gloss "buồng lái") và 2959 ([サイン・デザイン,3] → tag %l gloss "Vẽ biển hiệu") — nội dung đúng, chỉ ghi nhận quan sát (tiền lệ file 10 key 2090), không tính sai.
- **Đại từ đã rà toàn file:** Soutetsu "tôi" đúng với Navi (2282, 2331) và trong độc thoại (sau khi sửa 3025, 3100, 3133); "anh" đúng trong thoại với Hibiki; "mình" chỉ còn ở mệnh đề phụ ("mình có nói chuyện được" 2193; "mình đã vội vàng" 2820; "mình vừa nằm mơ" 2859; "mình tập trung quá mức" 3149) và dạng phản thân ("tự mình" 2293/2476/2493, "chính mình" 3068, "của chính mình" 2944) — giữ nguyên theo tiền lệ Hachiroku 12; "Em ấy" trong độc thoại đều chỉ Hibiki (ngôi thứ ba), đúng; Hibiki gọi Soutetsu "anh hai" đúng toàn file; Michiko gọi "anh Soutetsu" đúng; "chị hai" 2064 là Mayami, đúng; "chị Paulette" 2077, đúng.

## Đối chiếu sweep (gasp っ)

Sweep `sweep-raw-gasp-wrong.json` có **2 mục** cho file này (nhân đôi cho cả 2 bản TOML 02_Hibiki và 09_Grand — cùng key 2428) — nhận **1/1** (cùng 1 fix), 0 mục sai, 0 mục bỏ sót:

- 2428 (raw-tsu): 「引っ張られる？　――っ！？」→「Bị kéo đi? ――Ư!?」— đúng (VN cũ còn ký tự っ thô).

Quét máy toàn bộ dòng JP chứa っ: các っ còn lại đều đã được xử lý đúng — っ trong từ (きっと, まったく, 全っ然, ひっぱられちゃう, かえっちゃう…); っ nhấn mạnh/ngắt cuối trên từ có nội dung, không phải gasp (なによりっ 2130; 任せてっ 1972; にぃにぃっ 2520; でもっ 1986); SFX đã diễn đạt (ととととっ 3158 → "Lạch cạch"; ピピピっ 3165 → "Tít tít tít"; パシャっ 3162 → "Tách!"; ゆさっ 3167 → "Lay mạnh!"); âm đã diễn đạt + dấu câu truyền tải độ ngắt (やあっ!? 1998 → "A!?"; はうっ! 2004/2005 → "Hau!"/"Hau!?"; えっ!? 2011 → "Hả!?"; うおっ!? 2022 → "Uo!?"; ああっ! 2537 → "aa!"; んっ 2054 → "Ưm"; んんっ 2505/2513 → "ưm"; うふふっ 2096 → "Ufufu" — tiếng cười, đúng quy tắc Hieu). **Không còn gasp nào sót.**

## Chuỗi lệch dòng

Không có. File này sạch lệch dòng: không chuỗi xoay, không chu trình, không VN mồ côi. Toàn bộ 26 dòng sai đều là lỗi đơn lẻ (thuật ngữ / xưng hô / sai nghĩa / gasp), không có dòng nào phải lấy fix từ dòng khác trong file; 2419 mang 2 lỗi thuật ngữ trong cùng 1 dòng (2 lần "Ohitera").

## Lưu ý / điểm tự quyết / cần Hieu

- **2201 — KHÔNG SỬA, chờ Hieu:** 「僕らのか？」 VN "Của bọn anh sao?" — đại từ nhóm; người nghe/cảnh không xác định được (thứ tự key xen kẽ cảnh), "bọn anh" cho nhóm hỗn hợp (Soutetsu+Hibiki) có thể sai, "bọn tôi" là dạng nhóm trung lập — nhưng theo skill, dạng số nhiều KHÔNG chịu quy tắc số ít, chỉ đổi khi cảnh rõ ràng thân mật/gia đình. Giữ nguyên VN cũ, **không tính sai**.
- **1519 — "Bố mẹ vẫn đang tiếp tục tìm kiếm" giữ nguyên:** JP 探し続けてくれている không nêu chủ ngữ, TW 他們; "Bố mẹ" được ngữ cảnh chứng minh (1899 Michiko: ママもパパも、みちをむかえに来てくれない — bố mẹ là người đang tìm Michi). Không tính sai.
- **2019/3141 — 義父 "bố nuôi" giữ nguyên:** Soutetsu là con nuôi nhà Migita (sự thật trong truyện: 共通10 2573 右田の家の養子になって; ポーレット04 2245 僕は、右田の養子である); TW 養父 ở 3141; toàn dự án đều dịch 義父 là "bố nuôi"/"cha nuôi". Không tính sai.
- **1879/2959 — tag %l do VN tự thêm từ ruby JP** (xem § Kết quả tổng): nội dung đúng, chỉ ghi nhận. Không tính sai.
- **2986 — "Hibiki mở ra." giữ nguyên:** JP 日々姫が開く cụt tân ngữ (sổ phác thảo, suy ra từ ngữ cảnh); VN soi gương đúng kiểu cụt của JP. Không tính sai.
- **2441 — この子 "đứa trẻ này" cho 8620 giữ nguyên:** JP gọi 8620 là この子 theo nghĩa đen; TW 讓她 xem 8620 như "cô ấy" — VN "đứa trẻ này" trung lập, chấp nhận được. Không tính sai.
- **2831 — "Anh" trong trích dẫn giữ nguyên:** 「"Anh cũng không phải đợi lâu lắm đâu." Tôi định nói vậy thì chợt nhận ra」 — đây là lời Soutetsu định NÓI với Hibiki, nên "Anh" đúng. Không tính sai.
- **2282/2331 — "tôi" với Navi giữ nguyên:** Soutetsu hỏi ý kiến Navi về trang phục (2331 ナビにひとつ相談したい) — Navi không nằm trong nhóm "anh", "tôi" đúng. Không tính sai.
- **2748 — 日ノ本 "Hinomoto" đã đúng sẵn** trong file (không phải "Hinamoto"); giữ nguyên, không tính sai.
- **2060/2491/2539/2750 — OHITOYO viết hoa giữ nguyên:** đây là tên thương hiệu áo sơ mi, không phải tên địa danh 御一夜. Không tính sai.
- **1470/1491/2475 — ruby [ハチロクニイマル,3]/[ハチロク,3] giữ nguyên dạng:** đây là marker của engine (giống hệt phía JP), không phải chữ Nhật sót trong text hiển thị. Không tính sai.
- **1493 — VN==TW 「……」 trùng nhau hiển nhiên** (cả ba đều chỉ là dấu ba chấm). Không tính sai.
- **3149 — "mình" trong mệnh đề phụ giữ nguyên** ("hay do mình tập trung quá mức") theo tiền lệ Hachiroku 12. Không tính sai.
- **2350 — VN cụt giữ nguyên có chủ ý:** JP その気持ちは、復線のために引っ越せと言われる人と cũng cụt giữa chừng (kết bằng と); VN dừng ở "những người bị yêu cầu chuyển nhà vì việc khôi phục tuyến đường" soi gương đúng kiểu cụt của JP. Không tính sai.

## Chi tiết từng dòng sai

### 1525 — thuật ngữ (双鉄)

- **JP:** 「……旧御一夜－八ツ城間・廃線めぐりイラストマップ\n――では、あまりに露骨か」
- **TW:** 「……舊御一夜到八代段·廢線沿途彩繪地圖——這個有點太露骨了嗎」
- **VN cũ:** 「……Bản đồ minh họa tham quan tuyến đường sắt phế tích cũ Ohitera - Yatsushiro\n――Nghe thế này thì có vẻ hơi quá lộ liễu nhỉ.」
- **Fix:** 「……Bản đồ minh họa tham quan tuyến đường sắt phế tích cũ Ohitoyo - Yatsushiro\n――Nghe thế này thì có vẻ hơi quá lộ liễu nhỉ.」
- **Lý do:** 旧御一夜 → Ohitoyo theo quyết định 19/11

### 1975 — xưng hô (双鉄)

- **JP:** 「なるほど――言われればそのとおりだな」
- **TW:** 「原來如此——你這麼說確實有理啊」
- **VN cũ:** 「Ra là vậy―― Nghe cô nói mới thấy đúng thật.」
- **Fix:** 「Ra là vậy―― Nghe em nói mới thấy đúng thật.」
- **Lý do:** Soutetsu nói với Hibiki → 'em', không phải 'cô'

### 2047 — thuật ngữ (双鉄)

- **JP:** 「ああ、そうか！　みかん鉄道の方々――だけでなく、\n八ツ城－御一夜間、沿線の人たちの声も集められれば」
- **TW:** 「啊，是啊！不僅限於橙鐵路，我們還必須收集八代至御一夜沿線的人們的意見」
- **VN cũ:** 「À, đúng rồi! Những người ở Đường sắt Mikan―― không chỉ vậy,\nnếu chúng ta có thể thu thập được cả tiếng nói của những người dân sống dọc tuyến đường từ Yatsushiro đến Ohitera nữa thì.」
- **Fix:** 「À, đúng rồi! Những người ở Đường sắt Mikan―― không chỉ vậy,\nnếu chúng ta có thể thu thập được cả tiếng nói của những người dân sống dọc tuyến đường từ Yatsushiro đến Ohitoyo nữa thì.」
- **Lý do:** 八ツ城－御一夜間 → Ohitoyo

### 2118 — xưng hô (双鉄)

- **JP:** 「普段の僕……と言われると――\nタイも締めずにビジネスの場というのも、どうか」
- **TW:** 「她要求的是……平常的我——可在工作場合不打領帶不太好吧」
- **VN cũ:** 「Bình thường của mình…… nói thế thì――\nĐến nơi làm việc mà không thắt cà vạt thì có ổn không nhỉ.」
- **Fix:** 「Bình thường của anh…… nói thế thì――\nĐến nơi làm việc mà không thắt cà vạt thì có ổn không nhỉ.」
- **Lý do:** Soutetsu thoại với Hibiki → 'anh', không phải 'mình'

### 2138 — thuật ngữ (双鉄)

- **JP:** 「宝生元忠は言っていた。御一夜－八ツ城間の復線買収を\n困難にしているのは、分譲された宅地だと」
- **TW:** 「寶生元忠說過。御一夜至八代區間的廢線收購的難點在於分割轉讓的土地」
- **VN cũ:** 「Houshou Mototada đã nói. Điều khiến việc đền bù giải tỏa đất trên tuyến Ohitera - Yatsushiro\ntrở nên khó khăn là do đất ở đã được phân lô bán nền.」
- **Fix:** 「Houshou Mototada đã nói. Điều khiến việc đền bù giải tỏa đất trên tuyến Ohitoyo - Yatsushiro\ntrở nên khó khăn là do đất ở đã được phân lô bán nền.」
- **Lý do:** 御一夜－八ツ城間 → Ohitoyo

### 2168 — thuật ngữ (日々姫)

- **JP:** 「広い範囲って……御一夜市から八ツ城市までって、\nいくらなんでも広すぎるけど」
- **TW:** 「往外拓展……從御一夜市到八代市，這個範圍也太廣了吧」
- **VN cũ:** 「Phạm vi rộng hơn là…… từ thành phố Ohitera đến tận thành phố Yatsushiro á,\ndù nói thế nào thì cũng rộng quá mức rồi.」
- **Fix:** 「Phạm vi rộng hơn là…… từ thành phố Ohitoyo đến tận thành phố Yatsushiro á,\ndù nói thế nào thì cũng rộng quá mức rồi.」
- **Lý do:** 御一夜市 → Ohitoyo

### 2189 — thuật ngữ (日々姫)

- **JP:** 「わたし……まだ、\n御一夜市内からしか、仕事うけたことないけん」
- **TW:** 「我……還只接到過御一夜市內的工作」
- **VN cũ:** 「Em…… vẫn chưa,\nnhận được công việc nào từ bên ngoài thành phố Ohitera cả.」
- **Fix:** 「Em…… vẫn chưa,\nnhận được công việc nào từ bên ngoài thành phố Ohitoyo cả.」
- **Lý do:** 御一夜市内 → Ohitoyo

### 2241 — xưng hô (双鉄)

- **JP:** 「素晴らしい案だと思う。\nお前はよほど、僕より世慣れているな」
- **TW:** 「我覺得這個方案很棒。社會閱歷這方面我還真比不過你啊」
- **VN cũ:** 「Một ý kiến tuyệt vời.\nCô có vẻ còn sành sỏi sự đời hơn cả tôi đấy.」
- **Fix:** 「Một ý kiến tuyệt vời.\nEm có vẻ còn sành sỏi sự đời hơn cả anh đấy.」
- **Lý do:** Soutetsu nói với Hibiki (お前): 'cô/tôi' → 'em/anh'

### 2320 — thuật ngữ (日々姫)

- **JP:** 「御一夜のシャツ？」
- **TW:** 「是御一夜的襯衫牌子？」
- **VN cũ:** 「Áo sơ mi của Ohitera sao?」
- **Fix:** 「Áo sơ mi của Ohitoyo sao?」
- **Lý do:** 御一夜のシャツ → Ohitoyo

### 2348 — sai nghĩa (路子)

- **JP:** 「みちのいばしょを？」
- **TW:** 「沒有告訴他們小路在哪嗎？」
- **VN cũ:** 「Chỗ ở của Michi á?」
- **Fix:** 「Chỗ Michi đang ở á?」
- **Lý do:** 居場所 = nơi Michi đang ở (TW 在哪), không phải 'chỗ ở' (nơi cư trú)

### 2377 — thuật ngữ (日々姫)

- **JP:** 「今は、便利なソフトとか素材とかたくさんあるけん。\nたとえば――『御一夜鉄道』っていう文字」
- **TW:** 「現在有很多方便的軟體和素材。比如說——“御一夜鐵路”這幾個字」
- **VN cũ:** 「Bây giờ có rất nhiều phần mềm và tài nguyên tiện lợi mà.\nVí dụ nhé―― Dòng chữ 『Đường sắt Ohitera』.」
- **Fix:** 「Bây giờ có rất nhiều phần mềm và tài nguyên tiện lợi mà.\nVí dụ nhé―― Dòng chữ 『Đường sắt Ohitoyo』.」
- **Lý do:** 御一夜鉄道 → Ohitoyo

### 2419 — thuật ngữ (日々姫)

- **JP:** 「意見、たくさんだといいと思う。御一夜鉄道――\nううん、御一夜の人たちだけじゃなくって」
- **TW:** 「能收集到越多意見越好。御一夜鐵路——不，不光是御一夜的人們」
- **VN cũ:** 「Em nghĩ càng có nhiều ý kiến càng tốt. Đường sắt Ohitera――\nÀ không, không chỉ những người ở Ohitera đâu.」
- **Fix:** 「Em nghĩ càng có nhiều ý kiến càng tốt. Đường sắt Ohitoyo――\nÀ không, không chỉ những người ở Ohitoyo đâu.」
- **Lý do:** 御一夜鉄道 + 御一夜の人たち → Ohitoyo ×2

### 2428 — lỗi nhỏ (双鉄)

- **JP:** 「引っ張られる？　――っ！？」
- **TW:** 「被拉下去？——啊！？」
- **VN cũ:** 「Bị kéo đi? ――っ!?」
- **Fix:** 「Bị kéo đi? ――Ư!?」
- **Lý do:** Sweep raw-tsu: っ thô trong VN → Ư (tiền lệ Hachiroku 12 2103/2537)

### 2504 — thuật ngữ (双鉄)

- **JP:** 「ならば――あの地図はどうだろう。\n御一夜市のイラストマップ。あれを、もっと広い範囲で」
- **TW:** 「那麼——你看那個地圖怎麼樣？把御一夜市的彩繪地圖再往外拓展」
- **VN cũ:** 「Nếu vậy thì―― tấm bản đồ đó thì sao.\nBản đồ minh họa thành phố Ohitera ấy. Chúng ta làm nó ở một phạm vi rộng hơn.」
- **Fix:** 「Nếu vậy thì―― tấm bản đồ đó thì sao.\nBản đồ minh họa thành phố Ohitoyo ấy. Chúng ta làm nó ở một phạm vi rộng hơn.」
- **Lý do:** 御一夜市のイラストマップ → Ohitoyo

### 2537 — sai nghĩa (日々姫)

- **JP:** 「ナビ？　ナビ！　あ――あ――ああっ！\n今の、聞こえた――聞こえてた！？」
- **TW:** 「Ｎａｖｉ？Ｎａｖｉ！啊——啊——啊啊！剛才的話你聽到了——你聽到了嗎！？」
- **VN cũ:** 「Navi? Navi! A―― a―― aa!\nLúc nãy, cô ấy nghe thấy―― đã nghe thấy sao!?」
- **Fix:** 「Navi? Navi! A―― a―― aa!\nLúc nãy, cô nghe thấy―― đã nghe thấy sao!?」
- **Lý do:** Hibiki nói TRỰC TIẾP với Navi (ナビ？ ナビ！) → ngôi thứ hai 'cô', không phải 'cô ấy'

### 2755 — thuật ngữ (monologue)

- **JP:** かつての肥颯線、八ツ城－御一夜間は、\nクマ川に沿って走っていたと。
- **TW:** 在過去的肥薩線，八代到御一夜段是沿著隈河走的。
- **VN cũ:** Tuyến Hisatsu ngày xưa, đoạn giữa Yatsushiro và Ohitera,\nchạy dọc theo dòng sông Kuma.
- **Fix:** Tuyến Hisatsu ngày xưa, đoạn giữa Yatsushiro và Ohitoyo,\nchạy dọc theo dòng sông Kuma.
- **Lý do:** 八ツ城－御一夜間 → Ohitoyo

### 2761 — thuật ngữ (monologue)

- **JP:** 画面の中に地図を広げて、\n御一夜と八ツ城との間を絞込み――
- **TW:** 她在螢幕中放大地圖，在御一夜和八代之間的仔細觀察——
- **VN cũ:** Em ấy mở bản đồ trên màn hình,\nkhoanh vùng khu vực giữa Ohitera và Yatsushiro――
- **Fix:** Em ấy mở bản đồ trên màn hình,\nkhoanh vùng khu vực giữa Ohitoyo và Yatsushiro――
- **Lý do:** 御一夜と八ツ城との間 → Ohitoyo

### 2828 — thuật ngữ (monologue)

- **JP:** 日々姫と連れ立ち、御一夜温泉駅へと向かう。\nすっかり夜だ。
- **TW:** 我們倆一起前往了御一夜溫泉站。天已經完全黑了。
- **VN cũ:** Tôi cùng Hibiki đi đến ga Suối nước nóng Ohitera.\nTrời đã tối mịt.
- **Fix:** Tôi cùng Hibiki đi đến ga Suối nước nóng Ohitoyo.\nTrời đã tối mịt.
- **Lý do:** 御一夜温泉駅 → ga Suối nước nóng Ohitoyo

### 2874 — sai nghĩa (monologue)

- **JP:** だから、描く。\n僕らの歴史を、ここから更に重ねるために。
- **TW:** 所以我要在這裡下筆。為了讓我們的歷史繼續並行下去。
- **VN cũ:** Vì thế, tôi viết.\nĐể tiếp tục dệt nên lịch sử của chúng tôi từ nơi đây.
- **Fix:** Vì thế, tôi vẽ.\nĐể tiếp tục dệt nên lịch sử của chúng tôi từ nơi đây.
- **Lý do:** 描く = vẽ (độc thoại Hibiki), không phải 'viết' (書く)

### 2989 — sai nghĩa (monologue)

- **JP:** つぶやいて。\nそして大きく、日々姫が頷く。
- **TW:** 日日姬輕輕念了一遍。然後用力點了點頭。
- **VN cũ:** Tôi lẩm bẩm.\nVà Hibiki gật đầu thật mạnh.
- **Fix:** Em ấy lẩm bẩm.\nVà Hibiki gật đầu thật mạnh.
- **Lý do:** TW: 日日姬輕輕念了一遍 — người lẩm bẩm là Hibiki, không phải Soutetsu

### 3025 — xưng hô (monologue)

- **JP:** 僕と、日々姫と、僕らみんなと。\n僕らが未だ出会っていない――未来で繋がる人たちで。
- **TW:** 由我和日日姬一起，由大家一起。跟那些我們還未遇見的——將在未來邂逅的人們一起幹出一番天地。
- **VN cũ:** Anh, Hibiki, và tất cả chúng ta.\nCùng với những người mà chúng ta chưa từng gặp gỡ―― những người sẽ kết nối với chúng ta trong tương lai.
- **Fix:** Tôi, Hibiki, và tất cả chúng ta.\nCùng với những người mà chúng ta chưa từng gặp gỡ―― những người sẽ kết nối với chúng ta trong tương lai.
- **Lý do:** Độc thoại Soutetsu → 'Tôi' (tiền lệ Grand 11 2539, Grand 13 2273)

### 3063 — sai nghĩa (monologue)

- **JP:** 納得した声。
- **TW:** 聽起來她是領悟到了。
- **VN cũ:** Giọng nói đầy vẻ thuyết phục.
- **Fix:** Giọng nói như đã hiểu ra.
- **Lý do:** 納得した声 = giọng như đã hiểu ra/đồng tình (TW 領悟到了), không phải 'thuyết phục' (説得)

### 3100 — xưng hô (monologue)

- **JP:** 鉄道に興味がなかった――むしろ憎んでいた僕だからこそ、\n同じような人たちに、魅力を伝えられるかもしれんのか。
- **TW:** 說不定只有過去對鐵路沒有興趣——甚至曾經憎恨鐵路的我，才能向跟我們一樣的人傳達鐵路的魅力吧。
- **VN cũ:** Chính vì là một kẻ không có hứng thú với đường sắt―― thậm chí từng căm ghét nó,\nnên biết đâu anh lại có thể truyền tải được sức hấp dẫn của nó đến những người giống mình chăng.
- **Fix:** Chính vì là một kẻ không có hứng thú với đường sắt―― thậm chí từng căm ghét nó,\nnên biết đâu tôi lại có thể truyền tải được sức hấp dẫn của nó đến những người giống mình chăng.
- **Lý do:** Độc thoại Soutetsu → 'Tôi'

### 3133 — xưng hô (monologue)

- **JP:** 鉄道方面、公共方面。今後僕らがレールを伸ばす、\nそうしたところと、仕事で繋がれるようにしたい。
- **TW:** 鐵路方面，公共方面。我想拓展我們的涉獵面，爭取今後在工作上跟這兩個方面接軌。
- **VN cũ:** Lĩnh vực đường sắt, lĩnh vực công cộng. Những nơi mà sau này chúng ta sẽ mở rộng tuyến đường,\nanh muốn kết nối với họ thông qua công việc.
- **Fix:** Lĩnh vực đường sắt, lĩnh vực công cộng. Những nơi mà sau này chúng ta sẽ mở rộng tuyến đường,\ntôi muốn kết nối với họ thông qua công việc.
- **Lý do:** Độc thoại Soutetsu → 'Tôi' (lưu ý: VN gốc có literal \n trước 'anh' nên quét máy thô bỏ sót)

### 3138 — sai nghĩa (monologue)

- **JP:** 小柄な機関車とハチロクは言うが、\nやはり、大きい。
- **TW:** 雖說八六說它是個頭較小的機車，但依然是個龐然大物。
- **VN cũ:** Tuy gọi là đầu máy cỡ nhỏ và Hachiroku,\nnhưng quả thực, nó rất lớn.
- **Fix:** Tuy Hachiroku gọi là đầu máy cỡ nhỏ,\nnhưng quả thực, nó rất lớn.
- **Lý do:** JP: 小柄な機関車とハチロクは言うが — chủ ngữ là Hachiroku; bản cũ 'và Hachiroku' làm Hachiroku thành tân ngữ bị gọi là đầu máy

### 3177 — thuật ngữ (monologue)

- **JP:** 御一夜市のシャツ・メイカーの\nシャツ・ブランドが、OHITOYOで。
- **TW:** ＯＨＩＴＯＹＯ是御一夜市的襯衫廠商的襯衫品牌。
- **VN cũ:** OHITOYO là thương hiệu áo sơ mi\ncủa một nhà sản xuất áo sơ mi tại thành phố Ohitera.
- **Fix:** OHITOYO là thương hiệu áo sơ mi\ncủa một nhà sản xuất áo sơ mi tại thành phố Ohitoyo.
- **Lý do:** 御一夜市のシャツ・メイカー → Ohitoyo
## Khối TOML đã kiểm chứng

Khối dưới đây đã parse được bằng tomllib: 26 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô sau khi parse `\\n` về literal `\n`).

```toml
[script]
"1525" = "「……Bản đồ minh họa tham quan tuyến đường sắt phế tích cũ Ohitoyo - Yatsushiro\\n――Nghe thế này thì có vẻ hơi quá lộ liễu nhỉ.」"
"1975" = "「Ra là vậy―― Nghe em nói mới thấy đúng thật.」"
"2047" = "「À, đúng rồi! Những người ở Đường sắt Mikan―― không chỉ vậy,\\nnếu chúng ta có thể thu thập được cả tiếng nói của những người dân sống dọc tuyến đường từ Yatsushiro đến Ohitoyo nữa thì.」"
"2118" = "「Bình thường của anh…… nói thế thì――\\nĐến nơi làm việc mà không thắt cà vạt thì có ổn không nhỉ.」"
"2138" = "「Houshou Mototada đã nói. Điều khiến việc đền bù giải tỏa đất trên tuyến Ohitoyo - Yatsushiro\\ntrở nên khó khăn là do đất ở đã được phân lô bán nền.」"
"2168" = "「Phạm vi rộng hơn là…… từ thành phố Ohitoyo đến tận thành phố Yatsushiro á,\\ndù nói thế nào thì cũng rộng quá mức rồi.」"
"2189" = "「Em…… vẫn chưa,\\nnhận được công việc nào từ bên ngoài thành phố Ohitoyo cả.」"
"2241" = "「Một ý kiến tuyệt vời.\\nEm có vẻ còn sành sỏi sự đời hơn cả anh đấy.」"
"2320" = "「Áo sơ mi của Ohitoyo sao?」"
"2348" = "「Chỗ Michi đang ở á?」"
"2377" = "「Bây giờ có rất nhiều phần mềm và tài nguyên tiện lợi mà.\\nVí dụ nhé―― Dòng chữ 『Đường sắt Ohitoyo』.」"
"2419" = "「Em nghĩ càng có nhiều ý kiến càng tốt. Đường sắt Ohitoyo――\\nÀ không, không chỉ những người ở Ohitoyo đâu.」"
"2428" = "「Bị kéo đi? ――Ư!?」"
"2504" = "「Nếu vậy thì―― tấm bản đồ đó thì sao.\\nBản đồ minh họa thành phố Ohitoyo ấy. Chúng ta làm nó ở một phạm vi rộng hơn.」"
"2537" = "「Navi? Navi! A―― a―― aa!\\nLúc nãy, cô nghe thấy―― đã nghe thấy sao!?」"
"2755" = "Tuyến Hisatsu ngày xưa, đoạn giữa Yatsushiro và Ohitoyo,\\nchạy dọc theo dòng sông Kuma."
"2761" = "Em ấy mở bản đồ trên màn hình,\\nkhoanh vùng khu vực giữa Ohitoyo và Yatsushiro――"
"2828" = "Tôi cùng Hibiki đi đến ga Suối nước nóng Ohitoyo.\\nTrời đã tối mịt."
"2874" = "Vì thế, tôi vẽ.\\nĐể tiếp tục dệt nên lịch sử của chúng tôi từ nơi đây."
"2989" = "Em ấy lẩm bẩm.\\nVà Hibiki gật đầu thật mạnh."
"3025" = "Tôi, Hibiki, và tất cả chúng ta.\\nCùng với những người mà chúng ta chưa từng gặp gỡ―― những người sẽ kết nối với chúng ta trong tương lai."
"3063" = "Giọng nói như đã hiểu ra."
"3100" = "Chính vì là một kẻ không có hứng thú với đường sắt―― thậm chí từng căm ghét nó,\\nnên biết đâu tôi lại có thể truyền tải được sức hấp dẫn của nó đến những người giống mình chăng."
"3133" = "Lĩnh vực đường sắt, lĩnh vực công cộng. Những nơi mà sau này chúng ta sẽ mở rộng tuyến đường,\\ntôi muốn kết nối với họ thông qua công việc."
"3138" = "Tuy Hachiroku gọi là đầu máy cỡ nhỏ,\\nnhưng quả thực, nó rất lớn."
"3177" = "OHITOYO là thương hiệu áo sơ mi\\ncủa một nhà sản xuất áo sơ mi tại thành phố Ohitoyo."
```

## Kết bài

File グランドリライト03_日々姫.txt.toml đã đọc hết 469/469 dòng. Sai 26 dòng (5,5%) — không có lệch dòng, không có chuỗi xoay: toàn bộ đều là lỗi đơn lẻ. Lỗi lớn nhất là cụm thuật ngữ: "Ohitera" xuất hiện 13 dòng mà không một dòng nào dùng đúng "Ohitoyo" (file này là một trong những file còn "Ohitera" nhiều nhất; sau khi sửa, file không còn "Ohitera" nào). Tiếp theo là xưng hô Soutetsu (6 dòng: 3 dòng thoại với Hibiki dùng sai "cô/tôi/mình", 3 dòng độc thoại dùng "anh" thay vì "Tôi") và sai nghĩa (6 dòng, trong đó 2874 描く→"viết" và 2989 sai chủ ngữ lẩm bẩm là hai lỗi rõ nhất). Gasp: 1 dòng っ thô từ sweep (2428, áp nguyên).

Một dòng cờ cho Hieu (không sửa, không tính sai): 2201 ("bọn anh" với nhóm hỗn hợp Soutetsu+Hibiki — người nghe/cảnh chưa rõ). Ngoài ra file có 2 tag %l do VN tự thêm từ ruby JP (1879, 2959) với nội dung đúng, chỉ ghi nhận quan sát.

Fix list và khối TOML đã kiểm chứng xong (26 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 26/26; lượt soát 2: 26 tổng / 26 tái kiểm chứng / 0 bỏ / 0 sửa). Cơ sở tổng đã xác minh lại từ ROUTE-AUDIT.md: 166 file / 7.607 dòng sai.
