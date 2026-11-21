# Audit: 真闇02_精髄.txt.toml (05_Mayami)

File route 05_Mayami — “tinh túy” (精髄): Soutetsu cùng Mayami nếm thử loại shochu hơi nước mới, rồi lái đầu máy 8620 chở Mayami đi một vòng để cô hiểu về hơi nước; kết bằng việc Soutetsu tìm ra mong muốn của mình: giành Grand Prix ISC bằng loại rượu này.

## 1. Kiểm chứng file

- **TOML:** md5 `7ae6ef99a0143b27886371110ff06b4b`, 1 bản duy nhất (không có bản trùng trong 227 file; 11 nhóm trùng md5 toàn dự án đều là file khác), UTF-8 BOM + CRLF, 425 key script. `[selections]` rỗng. `[characters]`/`[character_subs]` chỉ chứa key siêu dữ liệu (2175/2183/2265/2482/2548, 2236/2490/2519/2758–2760/2794) không tương ứng dòng script nào — không có gì để kiểm tra ở đó.
- **CSV3:** 1 bộ duy nhất (`translation_toml\05_Mayami\真闇02_精髄.txt.toml`), 425 dòng, 0 key trùng, 0 VN trống, 0 key thiếu ở cả hai chiều. TOML khớp CSV3 tuyệt đối sau khi chuẩn hoá `\n` literal (TOML-2 làm phẳng thành khoảng trắng; 2 dòng 2064/2072 giữ nguyên `\n` như CSV3).
- **Nhân vật:** độc thoại 170, 双鉄 124, 真闇 104, ポーレット 12, ハチロク 9, 日々姫 6. Key 31–2793 (thưa).
- **Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.** 3 cặp VN trùng nhau trong file đều là câu lặp hợp lệ (2016/1592 「それはよかった」/「そんなら、良かったぁ」; 1541/1986 cùng câu hỏi; 1638/1599 cùng “Hừm.” cho むぅぅ/ふぅむ).
- **Sweep っ:** 2 entry cho file này (2060, 2061), cả 2 đã nhận nguyên văn sau khi kiểm chứng JP — xem §8. Không có っ thô nào khác trong VN (quét máy toàn file: chỉ còn 2061, đã sửa).

## 2. Tag %l thiếu dấu `;` — 41 dòng / 64 thẻ

VN thiếu `;` đóng thẻ ở dạng `%l;#` (đúng phải là `%l;#;`) — lỗi tập trung đúng như ghi chú trong task (64 thẻ, file này nhiều nhất dự án). JP-side 0 thẻ lỗi, nên mỗi chỗ sửa đều đối chiếu được trực tiếp với JP. 3 dòng kết hợp với sửa khác (1750 đại từ, 2460 thuật ngữ, 1766 thuật ngữ) — xem §3/§4. 38 dòng còn lại chỉ sửa tag, liệt kê ở §2b; mỗi fix đã kiểm chứng bằng script: sau sửa, 0 thẻ lỗi còn lại, số thẻ mở = số thẻ đóng trong mọi dòng.

### 2a. Ba dòng kết hợp

- **1750** (加減弁, 1 thẻ) — kèm sửa đại từ, xem §3.
- **2460** (整備体, 1 thẻ) — kèm sửa thuật ngữ “thân bảo trì”, xem §4.
- **1766** (客車, 1 thẻ) — kèm sửa “Ohitoyo”, xem §4.

### 2b. 38 dòng chỉ sửa tag (JP term → gloss VN, số thẻ)

- **1113** [双鉄] (3 thẻ): ブレーキ→“Phanh”; 列車→“tàu”; ブレーキ→“phanh”
- **1119** [真闇] (1 thẻ): 減圧→“Giảm áp”
- **1452** [双鉄] (1 thẻ): 絶気運転→“chạy cắt hơi”
- **1582** [真闇] (1 thẻ): 杜氏→“trưởng hầm rượu”
- **1652** [双鉄] (1 thẻ): 絶気運転→“chạy cắt hơi”
- **1656** [双鉄] (1 thẻ): 炭水車→“toa tiếp than nước”
- **1661** [双鉄] (1 thẻ): 減圧→“giảm áp”
- **1709** [双鉄] (1 thẻ): ブレーキ→“phanh”
- **1757** [双鉄] (1 thẻ): 動輪→“bánh xe chủ động”
- **1762** [双鉄] (1 thẻ): ブレーキ→“phanh”
- **1780** [双鉄] (1 thẻ): 列車→“tàu”
- **1822** [ハチロク] (1 thẻ): 動輪→“bánh xe chủ động”
- **1844** [ハチロク] (3 thẻ): ブレーキ→“phanh”; 客車→“toa hành khách”; 貨車→“toa chở hàng”
- **1861** [双鉄] (3 thẻ): 自弁→“van hãm tự động”; 常用→“phanh thường”; ブレーキ→“phanh”
- **1933** [双鉄] (2 thẻ): ブレーキ→“phanh”; 減圧→“giảm áp”
- **1938** [双鉄] (2 thẻ): ブレーキ→“phanh”; 空気圧縮機→“máy nén khí”
- **1974** [双鉄] (2 thẻ): 逆転機→“Cần đảo chiều”; ミッドギア→“số trung tính”
- **1994** [ハチロク] (2 thẻ): 機関士→“Lái tàu”; レイルロオド→“Railord”
- **1999** [日々姫] (2 thẻ): 機関士→“Lái tàu”; 機関助士→“phụ lái tàu”
- **2003** [双鉄] (3 thẻ): 圧→“áp suất”; ブレーキ→“phanh”; ブレーキ→“phanh”
- **2033** [双鉄] (1 thẻ): 加減弁→“van tiết lưu hơi”
- **2048** [日々姫] (1 thẻ): 客車→“toa hành khách”
- **2054** [ポーレット] (3 thẻ): 客車→“toa hành khách”; 客車→“toa hành khách”; 気動車→“toa xe tự hành”
- **2239** [monologue] (1 thẻ): 喚呼→“hô xác nhận”
- **2323** [monologue] (1 thẻ): 喚呼→“hô xác nhận”
- **2335** [monologue] (1 thẻ): 火室→“buồng đốt”
- **2376** [monologue] (1 thẻ): 客車→“toa hành khách”
- **2405** [monologue] (3 thẻ): 逆転機→“cần đảo chiều”; 前進フルギア→“cài hết số tiến”; バイパス弁→“van bypass”
- **2412** [monologue] (3 thẻ): 自弁→“van hãm tự động”; 重なり位置→“vị trí giữ phanh”; ブレーキ→“phanh”
- **2422** [monologue] (2 thẻ): 自弁→“van hãm tự động”; 常用→“phanh thường”
- **2426** [monologue] (1 thẻ): バイパス弁→“van bypass”
- **2437** [monologue] (2 thẻ): 自弁→“van hãm tự động”; ブレーキ→“phanh”
- **2442** [monologue] (1 thẻ): 8620→“8620”
- **2454** [monologue] (2 thẻ): 逆転機→“cần đảo chiều”; ミッドギア→“số trung tính”
- **2470** [monologue] (1 thẻ): 8620→“8620”
- **2535** [monologue] (1 thẻ): 列車→“tàu”
- **2744** [monologue] (2 thẻ): 加減弁→“van tiết lưu hơi”; バイパス弁→“van bypass”
- **2751** [monologue] (1 thẻ): ブレーキ→“phanh”

Lưu ý: key **2003** — JP có 1 thẻ lỗi phía JP (`ブレーキ%l;` thiếu `#;`) nhưng VN đã tái cấu trúc câu nên không phụ thuộc vào thẻ đó; chỉ sửa 3 thẻ `%l;#` thiếu `;` phía VN. Key **1844** — TW có 1 thẻ lỗi (không ảnh hưởng VN).

## 3. Đại từ xưng hô — 27 dòng

Soutetsu với Mayami phải là “tôi” (quy tắc đã khóa: Mayami gọi 双ちゃん, chị gái; file lr_日々姫真闇h1 đã sửa cùng mẫu 22 dòng, parent đã kiểm chứng). File này VN cũ dùng “em” tràn lan cho Soutetsu khi nói với Mayami — 25 dòng. Thêm 1773 (Mayami tự xưng “em” → “chị”) và 1543 (Paulette gọi 双鉄くん → “anh Soutetsu”, khóa B4). Đã kiểm chứng từng dòng: “em” còn lại trong file đều đúng đối tượng (Mayami gọi Soutetsu “em”: 1124, 1497, 1501, 1520, 1541, 1705, 1723, 1986; “nhờ em” ở 1831 là Paulette; “em ấy” ở 1454/1700/1703 là Hachiroku/Michiko). Soutetsu “anh” với Paulette/Hibiki không xuất hiện sai chỗ nào (0 dòng “anh” trong thoại 双鉄 với Mayami). Độc thoại nội tâm 2786 “Mình” giữ nguyên theo ngoại lệ độc thoại nội tâm.
### Key 2013 — [双鉄] — pronoun

- JP: `「では、旨い酒ができたときには、\n僕のアイディアもその上に乗っからせて欲しい」`
- TW: `「那到時候釀出了好喝的酒的時候，麻煩把我的主意也加進去咯」`
- VN cũ: `「Vậy thì, khi nào làm ra được loại rượu ngon, \nhãy cho em đóng góp thêm ý tưởng của mình vào đó nhé.」`
- VN mới: `「Vậy thì, khi nào làm ra được loại rượu ngon, \nhãy cho tôi đóng góp thêm ý tưởng của mình vào đó nhé.」`
- Lý do: Soutetsu với Mayami phải là “tôi” (quy tắc đã khóa: Mayami gọi 双ちゃん 366×, chị gái; “em” sai đối tượng).

### Key 2041 — [双鉄] — pronoun

- JP: `「僕のことを？」`
- TW: `「關於我的事？」`
- VN cũ: `「Chuyện về em sao?」`
- VN mới: `「Chuyện về tôi sao?」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1888 — [双鉄] — pronoun

- JP: `「どうだろうか、真闇姉。忙しいことはわかっているが、\n一度、[ハチロクニイマル,3]8620に乗ってみないか？」`
- TW: `「真闇姐，我有個提議。雖然你很忙，但是要不要乘坐一次８６２０試試？」`
- VN cũ: `「Ý chị thế nào, chị Mayami. Em biết chị rất bận, \nnhưng chị có muốn thử ngồi lên chiếc \x%l8620;#00ffc040;8620%l;#; một lần không?」`
- VN mới: `「Ý chị thế nào, chị Mayami. Tôi biết chị rất bận, \nnhưng chị có muốn thử ngồi lên chiếc \x%l8620;#00ffc040;8620%l;#; một lần không?」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1616 — [双鉄] — pronoun

- JP: `「ああいや、そうではなく、キャブ――\n\x%l運転台;#00ffc040;運転台%l;#;に、乗ってみてはどうかと思っているのだ」`
- TW: `「啊不是那個意思。我的意思是，你想不想坐在駕駛室——也就是\x%l運転台;#00ffc040;駕駛台%l;#;上呢」`
- VN cũ: `「À không, không phải thế, ý em là buồng lái——\nchị có muốn thử ngồi lên \x%l運転台;#00ffc040;buồng lái%l;#; không.」`
- VN mới: `「À không, không phải thế, ý tôi là buồng lái——\nchị có muốn thử ngồi lên \x%l運転台;#00ffc040;buồng lái%l;#; không.」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1528 — [双鉄] — pronoun

- JP: `「焼酎\x%l列車;#00ffc040;列車%l;#;の案が更に深まるかもしれないし、\n僕としては、是非とも乗ってもらいたい」`
- TW: `「其實我是很希望你能來列車上坐坐的，說不定這樣一來還可以最佳化燒酒\x%l列車;#00ffc040;列車%l;#;方案」`
- VN cũ: `「Biết đâu ý tưởng về chuyến \x%l列車;#00ffc040;tàu%l;#; shochu sẽ càng sâu sắc hơn, \nvề phần em, em rất muốn chị thử lên ngồi.」`
- VN mới: `「Biết đâu ý tưởng về chuyến \x%l列車;#00ffc040;tàu%l;#; shochu sẽ càng sâu sắc hơn, \nvề phần tôi, tôi rất muốn chị thử lên ngồi.」`
- Lý do: Soutetsu với Mayami phải là “tôi” (2 chỗ trong dòng).

### Key 1896 — [双鉄] — pronoun

- JP: `「シリンダーから水を抜いたのだ。\nこのシリンダー排水弁を、開けて、閉じる」`
- TW: `「給汽缸放水。也就是把這個汽缸排水閥打開以後馬上合上」`
- VN cũ: `「Em vừa xả nước khỏi xi-lanh. \nMở van xả nước xi-lanh này ra, rồi đóng lại.」`
- VN mới: `「Tôi vừa xả nước khỏi xi-lanh. \nMở van xả nước xi-lanh này ra, rồi đóng lại.」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1750 — [双鉄] — pronoun

- JP: `「まず、\x%l加減弁;#00ffc040;加減弁%l;#;を閉じた」`
- TW: `「我首先把\x%l加減弁;#00ffc040;汽門%l;#;給關了」`
- VN cũ: `「Đầu tiên, em đóng \x%l加減弁;#00ffc040;van tiết lưu hơi%l;# lại.」`
- VN mới: `「Đầu tiên, tôi đóng \x%l加減弁;#00ffc040;van tiết lưu hơi%l;#; lại.」`
- Lý do: Soutetsu với Mayami phải là “tôi”; đồng thời sửa 1 thẻ %l thiếu “;”.

### Key 1559 — [双鉄] — pronoun

- JP: `「こそこそせねば、会えぬものかと思ってな」`
- TW: `「只怕要不是我鬼鬼祟祟的，還見不到你呢」`
- VN cũ: `「Em nghĩ nếu không lén lút thì không gặp được chị chứ sao.」`
- VN mới: `「Tôi nghĩ nếu không lén lút thì không gặp được chị chứ sao.」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1147 — [双鉄] — pronoun

- JP: `「……しかし。やはりしっくり来んのだ。\nここでの方が落ち着くし、深く話せるようにも感じて」`
- TW: `「……可是，我就是靜不下心來。總感覺到這裡來才能放空自己、和你說些更重要的話」`
- VN cũ: `「……Nhưng mà. Vẫn thấy không thoải mái. \nỞ đây yên tĩnh hơn, và em có cảm giác có thể nói chuyện sâu sắc hơn.」`
- VN mới: `「……Nhưng mà. Vẫn thấy không thoải mái. \nỞ đây yên tĩnh hơn, và tôi có cảm giác có thể nói chuyện sâu sắc hơn.」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1806 — [双鉄] — pronoun

- JP: `「ここしばらく――何故僕を――いや、\nここでこうして会い、話すことを避けていたのだ？」`
- TW: `「最近——為什麼你一直在——不對，為什麼你會避免在這裡跟我說話呢？」`
- VN cũ: `「Dạo gần đây——Tại sao chị lại tránh mặt em——À không, \ntại sao chị lại tránh việc gặp gỡ và trò chuyện ở đây như thế này?」`
- VN mới: `「Dạo gần đây——Tại sao chị lại tránh mặt tôi——À không, \ntại sao chị lại tránh việc gặp gỡ và trò chuyện ở đây như thế này?」`
- Lý do: Soutetsu với Mayami phải là “tôi” (“tránh mặt em” = tránh mặt Soutetsu).

### Key 1641 — [双鉄] — pronoun

- JP: `「うん――わかる気がする」`
- TW: `「嗯——我可以感受得到」`
- VN cũ: `「Vâng――em nghĩ là em hiểu.」`
- VN mới: `「Vâng――tôi nghĩ là tôi hiểu.」`
- Lý do: Soutetsu với Mayami phải là “tôi” (2 chỗ trong dòng).

### Key 1726 — [双鉄] — pronoun

- JP: `「大正解だと僕は思う。\nこれは……雑味ではなく、風味だ」`
- TW: `「就該這麼做。這個味道……不是雜味，是風味」`
- VN cũ: `「Em nghĩ đó là một quyết định hoàn toàn chính xác.\nĐây…… không phải là tạp vị, mà là hương vị.」`
- VN mới: `「Tôi nghĩ đó là một quyết định hoàn toàn chính xác.\nĐây…… không phải là tạp vị, mà là hương vị.」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1162 — [双鉄] — pronoun

- JP: `「……祝杯をあげたい気分だ」`
- TW: `「……真想要舉杯慶祝一番」`
- VN cũ: `「……Em đang có tâm trạng muốn nâng ly chúc mừng đây.」`
- VN mới: `「……Tôi đang có tâm trạng muốn nâng ly chúc mừng đây.」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1755 — [双鉄] — pronoun

- JP: `「僕か？　僕は――それほどには譲らなかったぞ？」`
- TW: `「我？其實——我也沒做什麼讓步啊？」`
- VN cũ: `「Em á? Em thì―― đâu có nhường nhịn đến mức đó đâu?」`
- VN mới: `「Tôi á? Tôi thì―― đâu có nhường nhịn đến mức đó đâu?」`
- Lý do: Soutetsu với Mayami phải là “tôi” (2 chỗ trong dòng).

### Key 1747 — [双鉄] — pronoun

- JP: `「どうでもいいものは譲ったが。\n本当に欲しいものなら、たとえ泣かれても譲らなかった」`
- TW: `「我確實會忍讓些無關痛癢的東西。但是就算把她弄哭我也不會把真正想要的東西讓給她」`
- VN cũ: `「Những thứ không quan trọng thì em nhường.\nNhưng nếu là thứ em thực sự muốn, thì dù có bị khóc lóc em cũng không nhường đâu.」`
- VN mới: `「Những thứ không quan trọng thì tôi nhường.\nNhưng nếu là thứ tôi thực sự muốn, thì dù có bị khóc lóc tôi cũng không nhường đâu.」`
- Lý do: Soutetsu với Mayami phải là “tôi” (3 chỗ trong dòng — lượt soát 2 phát hiện chỗ giữa “thứ em thực sự muốn” bị sót ở lần đầu, đã sửa).

### Key 1454 — [双鉄] — pronoun

- JP: `「それでも、喧嘩にはならなかったな。\nそれが僕には必要なのだと、やがて、わかってもらえて」`
- TW: `「不過就算這樣，我們也沒有吵架。到最後，她都會理解我，知道那是我的必需品」`
- VN cũ: `「Dù vậy, bọn em cũng không hề cãi vã.\nVì em ấy sẽ nhanh chóng hiểu ra rằng, đó là thứ cần thiết đối với em.」`
- VN mới: `「Dù vậy, bọn tôi cũng không hề cãi vã.\nVì em ấy sẽ nhanh chóng hiểu ra rằng, đó là thứ cần thiết đối với tôi.」`
- Lý do: Soutetsu với Mayami phải là “tôi”; dạng nhóm cũng vậy — “bọn em” → “bọn tôi” (dạng nhóm trung tính theo quy tắc; “em ấy” = Michiko giữ nguyên, đúng).

### Key 1742 — [双鉄] — pronoun

- JP: `「人間も、\x%lレイルロオド;#00ffc040;レイルロオド%l;#;も。意思を持つものには必ず、\n望みを持ち、叶える権利があると、僕は信じる」`
- TW: `「我相信不論是人還是\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，只要擁有意識，那就應該有胸懷希望，以及將其實現的權利」`
- VN cũ: `「Dù là con người, hay \x%lレイルロオド;#00ffc040;Railord%l;#;. Em tin rằng, bất cứ ai có ý chí,\nđều có quyền mang trong mình những ước muốn, và quyền được hiện thực hóa chúng.」`
- VN mới: `「Dù là con người, hay \x%lレイルロオド;#00ffc040;Railord%l;#;. Tôi tin rằng, bất cứ ai có ý chí,\nđều có quyền mang trong mình những ước muốn, và quyền được hiện thực hóa chúng.」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1741 — [双鉄] — pronoun

- JP: `「僕、が――か？」`
- TW: `「我、我——？」`
- VN cũ: `「Em, á―― sao?」`
- VN mới: `「Tôi, á―― sao?」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1740 — [双鉄] — pronoun

- JP: `「僕……僕は――」`
- TW: `「我……我——」`
- VN cũ: `「Em…… em thì――」`
- VN mới: `「Tôi…… tôi thì――」`
- Lý do: Soutetsu với Mayami phải là “tôi” (2 chỗ trong dòng).

### Key 1168 — [双鉄] — pronoun

- JP: `「……わからない、かな」`
- TW: `「……這個，我還不清楚」`
- VN cũ: `「……Chắc là, em không biết.」`
- VN mới: `「……Chắc là, tôi không biết.」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1157 — [双鉄] — pronoun

- JP: `「……僕だけではないのだな」`
- TW: `「……看來這樣的不止是我自己啊」`
- VN cũ: `「……Không chỉ có mình em nhỉ.」`
- VN mới: `「……Không chỉ có mình tôi nhỉ.」`
- Lý do: Soutetsu với Mayami phải là “tôi” (độc thoại nội tâm hướng về Mayami).

### Key 1808 — [双鉄] — pronoun

- JP: `「あった。望みが。欲しいものが」`
- TW: `「有了。我知道我想要什麼了」`
- VN cũ: `「Có rồi. Mong muốn. Thứ em muốn có.」`
- VN mới: `「Có rồi. Mong muốn. Thứ tôi muốn có.」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1973 — [双鉄] — pronoun

- JP: `「御一夜のためでも、右田のためでもなく。\n僕個人が、単純に勝ちたい。この酒で」`
- TW: `「這不是為了御一夜，也不是為了右田家。這只是我個人的意願，我想要用這酒來拿獎」`
- VN cũ: `「Không phải vì Ohimitera, cũng không phải vì nhà Migita.\nMà với tư cách cá nhân, em đơn thuần chỉ muốn chiến thắng. Bằng loại rượu này.」`
- VN mới: `「Không phải vì Ohitoyo, cũng không phải vì nhà Migita.\nMà với tư cách cá nhân, tôi đơn thuần chỉ muốn chiến thắng. Bằng loại rượu này.」`
- Lý do: Soutetsu với Mayami phải là “tôi”; đồng thời 御一夜 → “Ohitoyo” (thuật ngữ đã khóa).

### Key 1507 — [双鉄] — pronoun

- JP: `「\x%l機関士;#00ffc040;機関士%l;#;の才……か？　どうかな？\nハチロクに言われるままに動いているだけなのだが」`
- TW: `「做\x%l機関士;#00ffc040;司機%l;#;的……才能？誰知道呢？我只是按照八六的指示來做罷了」`
- VN cũ: `「Tài năng của một \x%l機関士;#00ffc040;lái tàu%l;#;……sao? Ai biết được? \nEm chỉ làm theo những gì Hachiroku bảo thôi mà.」`
- VN mới: `「Tài năng của một \x%l機関士;#00ffc040;lái tàu%l;#;……sao? Ai biết được? \nTôi chỉ làm theo những gì Hachiroku bảo thôi mà.」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1981 — [双鉄] — pronoun

- JP: `「フォローは……無論、\n出来る限りはしているのだが――」`
- TW: `「這倒不用說……我肯定會盡力幫她，不過——」`
- VN cũ: `「Việc hỗ trợ thì……tất nhiên, \nem đang cố gắng hết sức có thể nhưng——」`
- VN mới: `「Việc hỗ trợ thì……tất nhiên, \ntôi đang cố gắng hết sức có thể nhưng——」`
- Lý do: Soutetsu với Mayami phải là “tôi”.

### Key 1773 — [真闇] — pronoun

- JP: `「そしたら、次も――もっと、ずうっと欲しかったもんも、\nきっと手に入れてみせるけん」`
- TW: `「拿獎以後——咱一定也可以，把握住咱一直想要的東西唄」`
- VN cũ: `「Vậy thì, tiếp theo―― thứ mà em vẫn luôn muốn có,\nchắc chắn em cũng sẽ lấy được cho xem.」`
- VN mới: `「Vậy thì, tiếp theo―― thứ mà chị vẫn luôn muốn có,\nchắc chắn chị cũng sẽ lấy được cho xem.」`
- Lý do: Mayami tự xưng phải là “chị” (nhất quán toàn file: “chị muốn giấu em”, “chị cũng tìm thấy…”); “em” ở đây là Mayami tự chỉ mình, sai.

### Key 1543 — [ポーレット] — pronoun

- JP: `「任せてください。双鉄くんは、双鉄くんのお仕事を。\nわたしたち、チームなんですから」`
- TW: `「包在我身上。雙鐵君就專心做你該做的工作吧。畢竟我們是個團隊嘛」`
- VN cũ: `「Cứ giao cho em. Soutetsu-kun cứ lo phần việc của Soutetsu-kun đi. \nChúng ta là một đội mà.」`
- VN mới: `「Cứ giao cho em. Anh Soutetsu cứ lo phần việc của mình đi. \nChúng ta là một đội mà.」`
- Lý do: Paulette gọi 双鉄くん → “anh Soutetsu” (khóa B4, không ngoại lệ); VN cũ giữ nguyên “Soutetsu-kun”.

## 4. Thuật ngữ — 6 dòng

### Key 2460 — [monologue] — terminology

- JP: `\x%l整備体;#00ffc040;整備体%l;#;への換装を終えたハチロクと、日々姫も\nキャブから降りてくる。`
- TW: `換成\x%l整備体;#00ffc040;整備體%l;#;的八六和日日姬也都走出了駕駛室。`
- VN cũ: `Hachiroku và Hibiki sau khi thay sang \x%l整備体;#00ffc040;thân chính%l;# \ncũng bước xuống từ buồng lái.`
- VN mới: `Hachiroku và Hibiki sau khi thay sang \x%l整備体;#00ffc040;thân bảo trì%l;#; \ncũng bước xuống từ buồng lái.`
- Lý do: 整備体 = “thân bảo trì” (thuật ngữ đã khóa); “thân chính” sai; đồng thời sửa 1 thẻ %l thiếu “;”.

### Key 2538 — [monologue] — terminology

- JP: `試験運転を無事終えて御一夜駅へと降り立てば、\n満面の笑顔を浮かべたポーレットが僕らを迎えてくれる。`
- TW: `當我們安全結束了試運營回到御一夜站下到站台的時候，等在那裡的波萊特便滿臉笑容地迎了上來。`
- VN cũ: `Kết thúc chuyến chạy thử nghiệm suôn sẻ và bước xuống ga Ohimitera, \nPaulette đón chúng tôi với nụ cười rạng rỡ trên môi.`
- VN mới: `Kết thúc chuyến chạy thử nghiệm suôn sẻ và bước xuống ga Ohitoyo, \nPaulette đón chúng tôi với nụ cười rạng rỡ trên môi.`
- Lý do: 御一夜駅 = ga Ohitoyo (thuật ngữ đã khóa 御一夜 = “Ohitoyo”, không bao giờ “Ohimitera”).

### Key 1798 — [ポーレット] — terminology

- JP: `「はい。御一夜と向こうさん、\nなんだか、土地同士の昔の縁もあるみたいなんです――」`
- TW: `「是的。似乎御一夜和他們的城市之間以前有著什麼聯繫——」`
- VN cũ: `「Vâng. Giữa Ohimitera và bên đó, \nhình như có một mối duyên nợ xa xưa nào đó về đất đai thì phải——」`
- VN mới: `「Vâng. Giữa Ohitoyo và bên đó, \nhình như có một mối duyên nợ xa xưa nào đó về đất đai thì phải——」`
- Lý do: 御一夜 = “Ohitoyo” (thuật ngữ đã khóa).

### Key 1766 — [ポーレット] — terminology

- JP: `「と、いうわけで、\n二週間後には\x%l客車;#00ffc040;客車%l;#;、御一夜に到着します！」`
- TW: `「所以，按計劃兩週後\x%l客車;#00ffc040;客運車廂%l;#;就會抵達御一夜了！」`
- VN cũ: `「Vậy nên, \nhai tuần nữa \x%l客車;#00ffc040;toa hành khách%l;# sẽ đến Ohimitera!」`
- VN mới: `「Vậy nên, \nhai tuần nữa \x%l客車;#00ffc040;toa hành khách%l;#; sẽ đến Ohitoyo!」`
- Lý do: 御一夜 = “Ohitoyo” (thuật ngữ đã khóa); đồng thời sửa 1 thẻ %l thiếu “;”.

### Key 1996 — [双鉄] — terminology

- JP: `「クマ川の水と、御一夜の土と。\nそれが、ぎゅうっと詰まってる」`
- TW: `「這酒裡凝聚了隈河的水還有御一夜的土的味道」`
- VN cũ: `「Nước sông Kuma, và đất của Ohimitera. \nTất cả được cô đọng lại trong này.」`
- VN mới: `「Nước sông Kuma, và đất của Ohitoyo. \nTất cả được cô đọng lại trong này.」`
- Lý do: 御一夜の土 = đất của Ohitoyo (thuật ngữ đã khóa).

### Key 2430 — [monologue] — terminology

- JP: `もういっぱいを飲み干せば、\n御一夜の夏の焼けた風が、喉を抜けたと感じさえする。`
- TW: `我猜若是把杯中的酒一飲而盡，將會有種御一夜夏天熾熱的風順著我的咽喉直衝而下的感覺。`
- VN cũ: `Uống cạn thêm một ly nữa,\ntôi thậm chí còn cảm thấy như cơn gió rát bỏng của mùa hè Ohimitera, vừa lướt qua cuống họng.`
- VN mới: `Uống cạn thêm một ly nữa,\ntôi thậm chí còn cảm thấy như cơn gió rát bỏng của mùa hè Ohitoyo, vừa lướt qua cuống họng.`
- Lý do: 御一夜の夏 = mùa hè Ohitoyo (thuật ngữ đã khóa).

## 5. Nghĩa / cấu trúc — 7 dòng

### Key 2572 — [monologue] — meaning

- JP: `ちょっと呆れたような顔。`
- TW: `真闇姐一臉無奈的表情。`
- VN cũ: `Một khuôn mặt có chút sững sờ.`
- VN mới: `Một khuôn mặt có chút ngao ngán.`
- Lý do: 呆れた = ngao ngán/bực mình trước câu hỏi hiển nhiên, không phải “sững sờ” (choáng váng); TW 一臉無奈 (vẻ bất lực) đồng ý.

### Key 2342 — [monologue] — meaning

- JP: `ごく当然の指摘にけれど、戸惑わされる。`
- TW: `她的指正合情合理，卻讓我越來越不解。`
- VN cũ: `Mặc dù đó là một lời chỉ trích hoàn toàn hiển nhiên, nhưng tôi vẫn cảm thấy bối rối.`
- VN mới: `Mặc dù đó là một lời nhận xét hoàn toàn hiển nhiên, nhưng tôi vẫn cảm thấy bối rối.`
- Lý do: 指摘 = lời chỉ ra/nhận xét, không phải “chỉ trích” (lên án); JP nói về một nhận xét hiển nhiên.

### Key 2367 — [monologue] — meaning

- JP: `僕としては、むしろ\x%l庫内手;#00ffc040;庫内手%l;#;のスキルの方が、\nぐんぐん伸びていってる感覚さえもある。`
- TW: `就我個人而言，總感覺我一直在提升\x%l庫内手;#00ffc040;洗爐工%l;#;該有的技能。`
- VN cũ: `Về phần mình, tôi thậm chí còn có cảm giác \nkỹ năng của một \x%l庫内手;#00ffc040;máy rửa lò%l;#; đang tăng lên vùn vụt.`
- VN mới: `Về phần mình, tôi thậm chí còn có cảm giác \nkỹ năng của một \x%l庫内手;#00ffc040;thợ rửa lò%l;#; đang tăng lên vùn vụt.`
- Lý do: 庫内手 là NGƯỜI (công nhân trong nhà xưởng), không phải máy; TW 洗爐工 (thợ rửa lò). “máy rửa lò” sai loại từ.

### Key 2446 — [monologue] — meaning

- JP: `僕は、きっと、真闇姉に。\n自分の仕事を――見て、気に入ってもらいたいのだ。`
- TW: `我肯定更想讓真闇姐看到我工作時的模樣——希望她能喜歡。`
- VN cũ: `Chắc chắn tôi muốn chị Mayami. \nNhìn thấy công việc của mình——và thích nó.`
- VN mới: `Chắc chắn tôi muốn chị Mayami nhìn thấy công việc của mình——và thích nó.`
- Lý do: VN cũ ngắt câu sai cấu trúc: “tôi muốn chị Mayami.” rồi “Nhìn thấy công việc…” không chủ ngữ — JP là một câu: muốn Mayami nhìn thấy công việc của mình và thích nó.

### Key 2597 — [monologue] — meaning

- JP: `感心しきり。\nそんな、長くて熱のある息。`
- TW: `真闇姐發出了長長一聲喘息，音色中聽得出她無比佩服的感情。`
- VN cũ: `Vô cùng ngưỡng mộ. \nMột tiếng thở dài và đầy nhiệt huyết.`
- VN mới: `Vô cùng ngưỡng mộ. \nMột hơi thở dài, đầy nhiệt huyết.`
- Lý do: VN cũ “Một tiếng thở dài và đầy nhiệt huyết” lủng củng (vế sau không có chủ ngữ); JP 長くて熱のある息 = một hơi thở dài, đầy nhiệt huyết.

### Key 2717 — [monologue] — meaning

- JP: `酒が、唇をなめらかにする。`
- TW: `這酒讓我有點關不住話匣子。`
- VN cũ: `Rượu, làm cho đôi môi trở nên trơn tru.`
- VN mới: `Rượu khiến tôi nói năng trơn tru hẳn lên.`
- Lý do: 唇をなめらかにする là thành ngữ “rượu làm trơn lưỡi” (nói năng lưu loát, khó giữ mồm) — TW 關不住話匣子 đồng ý; VN cũ dịch đen “đôi môi trở nên trơn tru” sai nghĩa. Dòng sau (2194) xác nhận: Soutetsu phải cẩn thận lời nói vì rượu làm anh nói nhiều.

### Key 1691 — [真闇] — meaning

- JP: `「ハチロクちゃん、分析力と作業精度がすごかけん。\nちょっと真似できん域まで突きつめてくれたとよ」`
- TW: `「多虧了八六優秀的分析能力和操作精度咧。她的鑽研精神真是連我都學不來」`
- VN cũ: `「Bé Hachiroku, năng lực phân tích và độ chính xác trong công việc tuyệt vời lắm.\nĐã đào sâu đến mức chị cũng chẳng thể bắt chước được luôn đó.」`
- VN mới: `「Hachiroku-chan, năng lực phân tích và độ chính xác trong công việc tuyệt vời lắm.\nĐã đào sâu đến mức chị cũng chẳng thể bắt chước được luôn đó.」`
- Lý do: Mayami gọi Hachiroku là “Hachiroku-chan” ở mọi chỗ khác trong file (1456, 1501, 1826, 1925); “Bé Hachiroku” không nhất quán.

## 6. Số nguyên âm — 1 dòng

### Key 1598 — [真闇] — vowel

- JP: `「はぁぁ……細かかとこまでよぅ出来とるねぇ」`
- TW: `「唉……還做得這麼細緻啊」`
- VN cũ: `「Hàà……Thiết kế tỉ mỉ đến từng chi tiết nhỉ.」`
- VN mới: `「Hààà……Thiết kế tỉ mỉ đến từng chi tiết nhỉ.」`
- Lý do: はぁぁ = 3 a (は + ぁ + ぁ); VN cũ chỉ 2 a. Trong cùng file, 1585 cùng âm はぁぁ đã đúng “Hààà.”.

## 7. Gasp (sweep) — 2 dòng

### Key 2060 — [真闇] — gasp

- JP: `「っ！！」`
- TW: `「！！」`
- VN cũ: `「!!」`
- VN mới: `「Ư!!」`
- Lý do: Sweep lost-gasp-whole: JP cả dòng chỉ là gasp っ!!; VN cũ mất hẳn âm → “Ư!!”.

### Key 2061 — [双鉄] — gasp

- JP: `「っ！？」`
- TW: `「！？」`
- VN cũ: `「っ!?」`
- VN mới: `「Ư!?」`
- Lý do: Sweep raw-tsu: っ thô trong VN; JP gasp っ → “Ư”.

## 8. Giữ nguyên có lý do (không tính sai)

- **1151** ううむ → “Ừm”; **1153** むぅ → “Hừm”; **1599** ふぅむ → “Hừm”; **1638** むぅぅ → “Hừm” — tiếng ậm ừ suy nghĩ/bĩu môi, “Hừm/Ừm” là tương đương tự nhiên trong tiếng Việt, không phải mất âm (quy tắc đếm nguyên âm áp cho tiếng rên/gasp, không áp cho tiếng ậm ừ thường).
- **1666 / 1843 / 1757** っと cuối câu → “Á” — nhất quán toàn file (3 chỗ), âm っ đã được diễn đạt, không thêm Ư (ranh giới gasp: không diễn đạt kép).
- **1922** “Giấu em?” giữ — “em” ở đây là người bị giấu (Mayami gọi Soutetsu “em”), không phải Soutetsu tự xưng; 1520 “chị muốn giấu em” tương ứng.
- **2786** độc thoại nội tâm “Mình thực sự rất hoan nghênh” giữ theo ngoại lệ “mình” cho độc thoại nội tâm.
- **2315** 義理の兄妹 → “anh em nuôi” giữ — TW 非親生兄妹 (không phải anh em ruột) ủng hộ; Soutetsu là 養子, quan hệ không cùng huyết thống.
- **2793** （くっ――くいっ） → “（Phụt——Phụt）” giữ (ghi cờ ở §9 — tiếng kéo van diễn thành tiếng phụt, chưa chắc).
- **2239** “mắt Hachiroku khẽ động” cho ツと動く giữ — sắc thái “nhanh” bị nhẹ đi nhưng không sai nghĩa.
- **1557 / 2072** よしっ/良しっ → “Rõ!” giữ — quy ước file cho tiếng xác nhận khi lái tàu; **1098** キン → “Keng” giữ; các SFX khác (2784, 2789, 2790, 2782/2783) giữ.
- **1533** “Một giọt (Hitoshizuku)” giữ — tên rượu ひとしずく, đã có chú thích; **1988** “SL” giữ nguyên; **1691** đã sửa (xem §5).
- **1585** はぁぁ → “Hààà.” đúng (3 a) — là căn cứ để sửa 1598.
- **69 / 1926 / 1582 / 2295** 杜氏 gloss “trưởng hầm rượu” giữ (ghi cờ ở §9).
- **1113** 列車 gloss “tàu” vs **2319** “đoàn tàu” giữ (ghi cờ ở §9).
- **1989 / 1564** 麹菌 → “nấm men kōji” giữ (ghi cờ ở §9).

## 9. Cờ cho Hieu

- **麹菌 → “nấm men kōji” (1989, 1564):** 麹菌 là nấm mốc (Aspergillus), không phải nấm men; “nấm men kōji” mâu thuẫn với 酵母 = “nấm men” ở cùng câu 1564 (“không chỉ có nấm men kōji hay nấm men”). Cần Hieu chốt thuật ngữ toàn dự án: giữ “nấm men kōji” hay đổi “nấm mốc kōji” (kéo theo 種麹 “bào tử men kōji” ở 2053). Không tự quyết — đã giữ nguyên trong audit này.
- **杜氏 gloss “trưởng hầm rượu” (69, 1926, 1582, 2295):** quy tắc đã khóa “杜氏 = Toji” áp cho cách gọi (杜氏さん); ở đây 杜氏 là danh từ chỉ vai trò (bậc thầy ủ rượu) nên gloss “trưởng hầm rượu” có lý, nhưng cần Hieu chốt thống nhất toàn dự án: vai trò giữ “trưởng hầm rượu” hay dùng “Toji” mọi chỗ.
- **列車 gloss “tàu” (1113, 2535, 1780) vs “đoàn tàu” (2319):** cùng một JP term, 2 gloss khác nhau trong file — ứng viên cho đợt thống nhất.
- **2793** SFX （くっ――くいっ） → “（Phụt——Phụt）”: tiếng kéo tay gạt van, “Phụt” gợi tiếng phụt (chất lỏng) hơn tiếng kéo — có nên đổi “Kéo——Kéo” không?
- **B19 vẫn park** (kiểm tra trong game ở Paulette 13 key 1596 trước đợt quét thẻ %l toàn dự án; 64 thẻ của file này đã sửa tay từng dòng theo chỉ đạo riêng, không phải quét bulk).

## 10. Lượt soát 2

- 81/81 fix đọc lại toàn bộ giá trị đối chiếu JP (+TW khi cần); **80 tái kiểm chứng đúng, 1 sửa (1747 — lần đầu sót “thứ em thực sự muốn” ở giữa câu, đã bổ sung “thứ tôi thực sự muốn”), 0 loại bỏ.**
- Mọi fix chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm tra diff từng dòng bằng script; các dòng nhiều thẻ chỉ thêm `;`).

## 11. Kiểm chứng

- JSON 81 mục dạng chuẩn (list of dicts, khóa chuỗi, đủ trường key/jp/tw/old_vn/fix/kind/character); khối TOML 81 khóa, parse OK bằng tomllib, 0 sai lệch giá trị (so sánh chuỗi thô; `\\n` và `\\x` giữ nguyên); jp/tw/old_vn khớp CSV3 tuyệt đối 81/81.
- Cơ sở tổng đã kiểm chứng trực tiếp dòng tổng cuối ROUTE-AUDIT.md: **172 file / 7.846 dòng sai** (khớp với cơ sở được giao).
- Tag: sau sửa, 0 thẻ `%l;#` thiếu `;` còn lại trong 81 fix; số thẻ mở = số thẻ đóng ở mọi dòng.

## Khối TOML (đã kiểm chứng parse, 81 khóa)

```toml
[script]
"1113" = "「\\x%lブレーキ;#00ffc040;Phanh%l;#; tự động của \\x%l列車;#00ffc040;tàu%l;#; được nhả ra bằng cách liên tục duy trì áp suất không khí. \\nCấu tạo của nó là khi xả áp suất thì \\x%lブレーキ;#00ffc040;phanh%l;#; sẽ hoạt động.」"
"1119" = "「\\x%l減圧;#00ffc040;Giảm áp%l;#;? Không phải là tăng áp sao?」"
"1147" = "「……Nhưng mà. Vẫn thấy không thoải mái. \\nỞ đây yên tĩnh hơn, và tôi có cảm giác có thể nói chuyện sâu sắc hơn.」"
"1157" = "「……Không chỉ có mình tôi nhỉ.」"
"1162" = "「……Tôi đang có tâm trạng muốn nâng ly chúc mừng đây.」"
"1168" = "「……Chắc là, tôi không biết.」"
"1452" = "「Nhưng trong lúc \\x%l絶気運転;#00ffc040;chạy cắt hơi%l;#;, piston trong xi-lanh vẫn tiếp tục chuyển động. \\nKhi đó, không khí bên trong piston sẽ không có chỗ thoát.」"
"1454" = "「Dù vậy, bọn tôi cũng không hề cãi vã.\\nVì em ấy sẽ nhanh chóng hiểu ra rằng, đó là thứ cần thiết đối với tôi.」"
"1507" = "「Tài năng của một \\x%l機関士;#00ffc040;lái tàu%l;#;……sao? Ai biết được? \\nTôi chỉ làm theo những gì Hachiroku bảo thôi mà.」"
"1528" = "「Biết đâu ý tưởng về chuyến \\x%l列車;#00ffc040;tàu%l;#; shochu sẽ càng sâu sắc hơn, \\nvề phần tôi, tôi rất muốn chị thử lên ngồi.」"
"1543" = "「Cứ giao cho em. Anh Soutetsu cứ lo phần việc của mình đi. \\nChúng ta là một đội mà.」"
"1559" = "「Tôi nghĩ nếu không lén lút thì không gặp được chị chứ sao.」"
"1582" = "「Chị là \\x%l杜氏;#00ffc040;trưởng hầm rượu%l;#; của Migita——của xưởng rượu shochu mà.」"
"1598" = "「Hààà……Thiết kế tỉ mỉ đến từng chi tiết nhỉ.」"
"1616" = "「À không, không phải thế, ý tôi là buồng lái——\\nchị có muốn thử ngồi lên \\x%l運転台;#00ffc040;buồng lái%l;#; không.」"
"1641" = "「Vâng――tôi nghĩ là tôi hiểu.」"
"1652" = "「Đúng vậy. Kết quả là hơi nước không vào xi-lanh nữa. \\nTrạng thái này gọi là \\x%l絶気運転;#00ffc040;chạy cắt hơi%l;#;.」"
"1656" = "「Ừm. Đầu tiên, ở chiếc tender ngay phía sau buồng lái này……\\nbên trong \\x%l炭水車;#00ffc040;toa tiếp than nước%l;#; có chứa nước và than.」"
"1661" = "「Vâng, là \\x%l減圧;#00ffc040;giảm áp%l;#; mới đúng.」"
"1691" = "「Hachiroku-chan, năng lực phân tích và độ chính xác trong công việc tuyệt vời lắm.\\nĐã đào sâu đến mức chị cũng chẳng thể bắt chước được luôn đó.」"
"1709" = "「Nào, từ đây sẽ là \\x%lブレーキ;#00ffc040;phanh%l;#;.」"
"1726" = "「Tôi nghĩ đó là một quyết định hoàn toàn chính xác.\\nĐây…… không phải là tạp vị, mà là hương vị.」"
"1740" = "「Tôi…… tôi thì――」"
"1741" = "「Tôi, á―― sao?」"
"1742" = "「Dù là con người, hay \\x%lレイルロオド;#00ffc040;Railord%l;#;. Tôi tin rằng, bất cứ ai có ý chí,\\nđều có quyền mang trong mình những ước muốn, và quyền được hiện thực hóa chúng.」"
"1747" = "「Những thứ không quan trọng thì tôi nhường.\\nNhưng nếu là thứ tôi thực sự muốn, thì dù có bị khóc lóc tôi cũng không nhường đâu.」"
"1750" = "「Đầu tiên, tôi đóng \\x%l加減弁;#00ffc040;van tiết lưu hơi%l;#; lại.」"
"1755" = "「Tôi á? Tôi thì―― đâu có nhường nhịn đến mức đó đâu?」"
"1757" = "「Vì vậy, nếu lượng hơi nước bơm vào xi-lanh tăng lên, \\ntốc độ quay của \\x%l動輪;#00ffc040;bánh xe chủ động%l;#; cũng sẽ nhanh hơn, và tàu sẽ tăng tốc——Á.」"
"1762" = "「Vì vậy, việc thiết kế sao cho khi không khí thoát ra thì \\x%lブレーキ;#00ffc040;phanh%l;#; sẽ hoạt động, \\nlà để nâng cao thêm tính an toàn.」"
"1766" = "「Vậy nên, \\nhai tuần nữa \\x%l客車;#00ffc040;toa hành khách%l;#; sẽ đến Ohitoyo!」"
"1773" = "「Vậy thì, tiếp theo―― thứ mà chị vẫn luôn muốn có,\\nchắc chắn chị cũng sẽ lấy được cho xem.」"
"1780" = "「Chuyện là vậy đó. Chị Mayami có nguyện vọng gì không? \\nĐể có thể vận hành như một chuyến \\x%l列車;#00ffc040;tàu%l;#; shochu.」"
"1798" = "「Vâng. Giữa Ohitoyo và bên đó, \\nhình như có một mối duyên nợ xa xưa nào đó về đất đai thì phải——」"
"1806" = "「Dạo gần đây——Tại sao chị lại tránh mặt tôi——À không, \\ntại sao chị lại tránh việc gặp gỡ và trò chuyện ở đây như thế này?」"
"1808" = "「Có rồi. Mong muốn. Thứ tôi muốn có.」"
"1822" = "「Bên trong xi-lanh có piston. \\nChuyển động của piston đó sẽ biến thành chuyển động quay của \\x%l動輪;#00ffc040;bánh xe chủ động%l;#;.」"
"1844" = "「Là để phòng trường hợp ống \\x%lブレーキ;#00ffc040;phanh%l;#; bị hỏng, \\nhoặc \\x%l客車;#00ffc040;toa hành khách%l;#;・\\x%l貨車;#00ffc040;toa chở hàng%l;#; bị tách rời ạ.」"
"1861" = "「Bây giờ, tay gạt \\x%l自弁;#00ffc040;van hãm tự động%l;#; đang ở vị trí \\x%l常用;#00ffc040;phanh thường%l;#;——\\nlà vị trí \\x%lブレーキ;#00ffc040;phanh%l;#; sử dụng thông thường.」"
"1888" = "「Ý chị thế nào, chị Mayami. Tôi biết chị rất bận, \\nnhưng chị có muốn thử ngồi lên chiếc \\x%l8620;#00ffc040;8620%l;#; một lần không?」"
"1896" = "「Tôi vừa xả nước khỏi xi-lanh. \\nMở van xả nước xi-lanh này ra, rồi đóng lại.」"
"1933" = "「Ở vị trí này, khí nén trong \\x%lブレーキ;#00ffc040;phanh%l;#; \\nsẽ được \\x%l減圧;#00ffc040;giảm áp%l;#; 0.4kg/cm2.」"
"1938" = "「Việc duy trì \\x%lブレーキ;#00ffc040;phanh%l;#; là nhờ hoạt động của khí nén. \\nVà động lực của \\x%l空気圧縮機;#00ffc040;máy nén khí%l;#; tạo ra nó, tất nhiên cũng là hơi nước.」"
"1973" = "「Không phải vì Ohitoyo, cũng không phải vì nhà Migita.\\nMà với tư cách cá nhân, tôi đơn thuần chỉ muốn chiến thắng. Bằng loại rượu này.」"
"1974" = "「\\x%l逆転機;#00ffc040;Cần đảo chiều%l;#; này, nếu so với ô tô thì giống như cần số vậy. \\nCó thể cài đặt tiến, lùi, và \\x%lミッドギア;#00ffc040;số trung tính%l;#;——tức là Neutral.」"
"1981" = "「Việc hỗ trợ thì……tất nhiên, \\ntôi đang cố gắng hết sức có thể nhưng——」"
"1994" = "「Nếu nói vậy thì phải là em mới đúng. \\n\\x%l機関士;#00ffc040;Lái tàu%l;#; và \\x%lレイルロオド;#00ffc040;Railord%l;#; chẳng khác nào tuy hai mà một.」"
"1996" = "「Nước sông Kuma, và đất của Ohitoyo. \\nTất cả được cô đọng lại trong này.」"
"1999" = "「Nếu nói là đội thì phải là em chứ! \\n\\x%l機関士;#00ffc040;Lái tàu%l;#; và \\x%l機関助士;#00ffc040;phụ lái tàu%l;#; là một cặp bài trùng mà!」"
"2003" = "「Với phương pháp dùng khí nén để tạo \\x%l圧;#00ffc040;áp suất%l;#; \\x%lブレーキ;#00ffc040;phanh%l;#;, \\nthì khi bị tách rời, toa khách và toa hàng sẽ mất kiểm soát vì không có \\x%lブレーキ;#00ffc040;phanh%l;#;.」"
"2013" = "「Vậy thì, khi nào làm ra được loại rượu ngon, \\nhãy cho tôi đóng góp thêm ý tưởng của mình vào đó nhé.」"
"2033" = "「Nước trong lò hơi sẽ chuyển thành hơi nước nhờ sức nóng của than cháy. \\nHơi nước sinh ra, thông qua tay gạt \\x%l加減弁;#00ffc040;van tiết lưu hơi%l;#; này——」"
"2041" = "「Chuyện về tôi sao?」"
"2048" = "「Không lẽ nào, liên quan đến \\x%l客車;#00ffc040;toa hành khách%l;#;!?」"
"2054" = "「Chúng ta đã được nhượng lại \\x%l客車;#00ffc040;toa hành khách%l;#; rồi! \\nLà \\x%l客車;#00ffc040;toa hành khách%l;#; được cải tạo từ \\x%l気動車;#00ffc040;toa xe tự hành%l;#;, từ Đường sắt Suntai.」"
"2060" = "「Ư!!」"
"2061" = "「Ư!?」"
"2239" = "Sau khi xác nhận biển báo và \\x%l喚呼;#00ffc040;hô xác nhận%l;#; xong, mắt Hachiroku khẽ động. \\n……Phía trước một đoạn sẽ là khu vực trong rừng."
"2323" = "Giới hạn 60——\\nNgay khi xác nhận biển báo, tiếng \\x%l喚呼;#00ffc040;hô xác nhận%l;#; của tôi và Hachiroku vang lên đồng thanh."
"2335" = "Hibiki điều khiển chiếc xẻng xúc than một cách điêu luyện, \\ntiếp tục duy trì ngọn lửa trong \\x%l火室;#00ffc040;buồng đốt%l;#;."
"2342" = "Mặc dù đó là một lời nhận xét hoàn toàn hiển nhiên, nhưng tôi vẫn cảm thấy bối rối."
"2367" = "Về phần mình, tôi thậm chí còn có cảm giác \\nkỹ năng của một \\x%l庫内手;#00ffc040;thợ rửa lò%l;#; đang tăng lên vùn vụt."
"2376" = "Nhận được loại \\x%l客車;#00ffc040;toa hành khách%l;#; nào, và quá trình được nhượng lại ra sao."
"2405" = "Mở rồi đóng van xả nước xi-lanh, \\ngạt \\x%l逆転機;#00ffc040;cần đảo chiều%l;#; về \\x%l前進フルギア;#00ffc040;cài hết số tiến%l;#; một lần nữa, đồng thời đóng \\x%lバイパス弁;#00ffc040;van bypass%l;#; lại——"
"2412" = "Đưa \\x%l自弁;#00ffc040;van hãm tự động%l;#; về \\x%l重なり位置;#00ffc040;vị trí giữ phanh%l;#;, vừa duy trì lực \\x%lブレーキ;#00ffc040;phanh%l;#;, \\nvừa nạp lại khí nén."
"2422" = "Từ từ đưa \\x%l自弁;#00ffc040;van hãm tự động%l;#; về vị trí \\x%l常用;#00ffc040;phanh thường%l;#;."
"2426" = "Tôi gõ nhẹ ngón tay vào \\x%lバイパス弁;#00ffc040;van bypass%l;#; đang mở \\nđể chỉ cho chị ấy."
"2430" = "Uống cạn thêm một ly nữa,\\ntôi thậm chí còn cảm thấy như cơn gió rát bỏng của mùa hè Ohitoyo, vừa lướt qua cuống họng."
"2437" = "Tôi buông tay đang giữ \\x%l自弁;#00ffc040;van hãm tự động%l;#; ra một thoáng, \\nvà làm động tác cho thấy đây là thứ điều khiển \\x%lブレーキ;#00ffc040;phanh%l;#;."
"2442" = "Dù không hiểu tại sao, tôi vẫn cố gắng xoa dịu đội \\x%l8620;#00ffc040;8620%l;#; đang tỏ vẻ bất mãn, \\nvà quay lại nhìn chị Mayami."
"2446" = "Chắc chắn tôi muốn chị Mayami nhìn thấy công việc của mình——và thích nó."
"2454" = "Vừa nói, tôi vừa gạt \\x%l逆転機;#00ffc040;cần đảo chiều%l;#; về \\x%lミッドギア;#00ffc040;số trung tính%l;#;. \\nTôi thao tác chậm rãi và rõ ràng để chị ấy dễ hiểu."
"2460" = "Hachiroku và Hibiki sau khi thay sang \\x%l整備体;#00ffc040;thân bảo trì%l;#; \\ncũng bước xuống từ buồng lái."
"2470" = "Cùng với lời nói, \\x%l8620;#00ffc040;8620%l;#; từ từ giảm tốc độ."
"2535" = "Tất nhiên, ý tưởng về chuyến \\x%l列車;#00ffc040;tàu%l;#; shochu cũng rất quan trọng. \\nNhưng trước đó."
"2538" = "Kết thúc chuyến chạy thử nghiệm suôn sẻ và bước xuống ga Ohitoyo, \\nPaulette đón chúng tôi với nụ cười rạng rỡ trên môi."
"2572" = "Một khuôn mặt có chút ngao ngán."
"2597" = "Vô cùng ngưỡng mộ. \\nMột hơi thở dài, đầy nhiệt huyết."
"2717" = "Rượu khiến tôi nói năng trơn tru hẳn lên."
"2744" = "Rồi tôi từ từ đóng \\x%l加減弁;#00ffc040;van tiết lưu hơi%l;#; lại, \\nvà mở \\x%lバイパス弁;#00ffc040;van bypass%l;#; cho chị ấy xem."
"2751" = "Dù nghĩ rằng đây là một lời giải thích thừa thãi, \\nnhưng tôi vẫn tiếp tục nói về \\x%lブレーキ;#00ffc040;phanh%l;#;."
```
## Kết bài

File 真闇02_精髄.txt.toml: 425 dòng đã đọc đủ, **81 dòng sai (19,1%)** — lỗi tập trung ở đại từ Soutetsu “em” với Mayami (25 dòng + 1 Mayami tự xưng + 1 khóa B4), tag %l thiếu `;` (41 dòng / 64 thẻ, nhiều nhất dự án), thuật ngữ (御一夜 “Ohimitera” 6 dòng, 整備体 “thân chính” 1 dòng), nghĩa/cấu trúc 7 dòng, số nguyên âm 1 dòng, gasp sweep 2 dòng. Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. 4 cờ cho Hieu (麹菌, gloss 杜氏, gloss 列車, SFX 2793); B19 vẫn park.
