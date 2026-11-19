# Audit: Paulette h5_裸エプロンのレモンドレッシング和え — 30 dòng Việt sai (đã đối chiếu JP + TW)

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa từng dòng: 305 dòng (độc thoại 169, Paulette 84, Soutetsu 52), đối chiếu JP + TW từ CSV3 và TOML-2.
- CSV vs TOML: 0 khác biệt thực chất (197 khác biệt thô chỉ ở `\n`/khoảng trắng); tập key bằng nhau (305); `[selections]` rỗng; thẻ `%l`: 0 hỏng; không có key trùng; không có dòng VN trống; VN==TW 1 (631, `「…………」` — cả ba thứ tiếng đều là dấu lặng, đúng).
- md5: `ba0e02364d99fd8aa8f08daea04428b2` — không trùng với bất kỳ file nào trong 227 file TOML (không có bản sao; bản sửa áp dụng cho 1 file duy nhất).
- Đọc lần đầu phát hiện 29/30 dòng; rà soát chéo (quét romanisation + sweep gasp) bắt thêm 1 dòng (942, ちゅむっ→"chu", tìm ra nhờ quét `\bchu\b` toàn file).
- Rà soát chéo với sweep gasp っ: sweep có 5 mục trong file này (904, 905, 935, 953, 1228) — audit xác nhận cả 5 cùng giá trị sửa; audit không phát hiện thêm dòng gasp nào mà sweep bỏ sót trong file này.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ 30/30 bản sửa đối chiếu JP (đúng 30, 0 bị loại). Kiểm tra lần hai cũng xác nhận: không có bản sửa nào thừa hưởng lỗi xưng hô của dòng khác (không có dòng lệch vị trí), không có khoảng trắng thừa trước `\n`, không có dấu 。 thay cho dấu ., các âm thở ghép viết liền một từ.
- Quy ước bản sửa: bản sửa viết MỘT DÒNG (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công — theo quyết định 19/11 của Hieu (game tự ngắt dòng, `\n` thủ công không quan trọng). Điểm này KHÁC với h1–h4 (vốn giữ `\n` trong bản sửa). File TOML gốc cũng lưu các giá trị này một dòng với khoảng trắng, nên khối TOML dưới đây dán vào khớp đúng dạng đó.

## Kết luận về cơ chế lỗi

- Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương: file sạch về cấu trúc. Chỉ số VN trùng trong file (2 nhóm: `「!!!」` ×2, `「っ!」` ×3) đều hợp lệ — `「っ!」` ×3 là cùng một JP `「っ！」` ở 3 key (904/905/953); `「!!!」` ×2 gồm 935 (JP có っ, sai) và 1053 (JP `「！！！」` không có っ, đúng).
- Lỗi chủ đạo là xưng hô hệ thống: Soutetsu tự xưng "anh" 10/10 lần trong thoại (chỉ có 2 lần "tôi" đúng trước khi sửa: 1718, 1634) và "Anh" 1 lần trong độc thoại (1401) — cùng lỗi hệ thống như h1/h2/h3/h4/h6.
- Cụm lỗi SFX: ちゅ→"chu" không nhất quán (942: ちゅむっ→"chu"; 1723: ちゅっ→"Chu") trong khi file dịch ちゅっ/ちゅるっ/ちゅむっ là "chụt" ở mọi chỗ khác (938, 942 là ngoại lệ duy nhất còn lại); ぐいっ bị dịch sai hai kiểu trái ngược nhau (1713: "Hự" — tiếng rên; 1717: "Thóp bụng!" — bịa động tác theo TW); にゅぶうっ bị dịch "nhép" trong khi họ ぬぶ là rút ra (quy tắc h4).
- Tiếng thở La-tinh: 5 dòng (んきゅ×2, くあ×1, ひゅい×1, きゅう dài×1) — cùng họ lỗi như h1/h2/h3/h4/h6.
- Sai nghĩa: 1 dòng (1290: 我が身→"lý trí", phải là "thể xác").

## Chi tiết dòng sai

### Xưng hô (11 dòng)

**Key 635 (双鉄)**
- JP: `「……言っていたな。さっき。\nここは、僕のためにごはんを作ってくれるところだと」`
- TW: `「……你剛才說過，這裡是給我做飯吃的地方」`
- VN cũ: `「……Lúc nãy, em có nói nhỉ.\nĐây là nơi em nấu cơm cho anh ăn.」`
- Sửa: `「……Lúc nãy, em có nói nhỉ. Đây là nơi em nấu cơm cho tôi ăn.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP 僕のために) → "Tôi" (docs §2.1).

**Key 839 (双鉄)**
- JP: `「聞かせてくれ。\n聞かせてくれねば、僕には助けようもない」`
- TW: `「你說吧。你要是不說，我也沒辦法幫你」`
- VN cũ: `「Nói cho anh nghe đi.\nNếu em không nói, anh cũng chẳng biết giúp thế nào.」`
- Sửa: `「Nói cho tôi nghe đi. Nếu em không nói, tôi cũng chẳng biết giúp thế nào.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP 僕には) → "Tôi".

**Key 950 (双鉄)**
- JP: `「ああ、約束した。ポーレットがそれを汚れと思うなら、\n僕が必ず、受け止めようと」`
- TW: `「嗯，我跟你約好了。如果你覺得那是髒東西的話，我就一定會全部接下」`
- VN cũ: `「Ừ, anh đã hứa rồi. Nếu Paulette nghĩ đó là sự bẩn thỉu,\nanh nhất định, sẽ hứng trọn lấy nó.」`
- Sửa: `「Ừ, tôi đã hứa rồi. Nếu Paulette nghĩ đó là sự bẩn thỉu, tôi nhất định, sẽ hứng trọn lấy nó.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP 僕が必ず) → "Tôi".

**Key 961 (双鉄)**
- JP: `「汚れであると、ポーレットが感じてしまうというのなら。\n僕が必ず。その汚れさえ受け止めるから」`
- TW: `「如果你覺得髒的話，我也一定會把所有的髒東西都接下」`
- VN cũ: `「Nếu Paulette cảm thấy đó là thứ bẩn thỉu.\nThì anh nhất định. Sẽ hứng trọn cả sự bẩn thỉu đó.」`
- Sửa: `「Nếu Paulette cảm thấy đó là thứ bẩn thỉu. Thì tôi nhất định. Sẽ hứng trọn cả sự bẩn thỉu đó.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP 僕が必ず) → "Tôi".

**Key 965 (双鉄)**
- JP: `「すまん。気づくのが遅れてしまった」`
- TW: `「對不起，我發現得太晚了」`
- VN cũ: `「Xin lỗi em. Anh nhận ra hơi muộn.」`
- Sửa: `「Xin lỗi em. Tôi nhận ra hơi muộn.」`
- Lý do: Soutetsu tự xưng "Anh" trong thoại (JP 気づくのが遅れてしまった, chủ ngữ là Soutetsu) → "Tôi".

**Key 976 (双鉄)**
- JP: `「しかし、見ずには受け止められぬ」`
- TW: `「我不看起來可就接不住了」`
- VN cũ: `「Nhưng nếu không nhìn thì sao anh hứng được.」`
- Sửa: `「Nhưng nếu không nhìn thì sao tôi hứng được.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP 見ずには受け止められぬ, chủ ngữ là Soutetsu) → "Tôi".

**Key 979 (双鉄)**
- JP: `「さっきも言ったが汚れなどせん。\nポーレットの体から出るものなのだから」`
- TW: `「我剛才也說過，一點因為不髒。只要是你身體裡出來都不髒」`
- VN cũ: `「Anh đã nói rồi, không bẩn đâu.\nĐó là thứ tiết ra từ cơ thể Paulette mà.」`
- Sửa: `「Tôi đã nói rồi, không bẩn đâu. Đó là thứ tiết ra từ cơ thể Paulette mà.」`
- Lý do: Soutetsu tự xưng "Anh" trong thoại (JP さっきも言ったが) → "Tôi".

**Key 984 (双鉄)**
- JP: `「これを使って、僕が必ず受け止めよう。\nシンクには、一滴たりともこぼさぬように」`
- TW: `「我會用這個全部接住的。我不會水槽沾到一滴」`
- VN cũ: `「Dùng cái này, anh nhất định sẽ hứng lấy.\nSẽ không để vương vãi ra bồn rửa dù chỉ một giọt.」`
- Sửa: `「Dùng cái này, tôi nhất định sẽ hứng lấy. Sẽ không để vương vãi ra bồn rửa dù chỉ một giọt.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP 僕が必ず受け止めよう) → "Tôi".

**Key 986 (双鉄)**
- JP: `「緊張をさせてしまったか？」`
- TW: `「是我讓你太緊張了嗎？」`
- VN cũ: `「Anh làm em căng thẳng à?」`
- Sửa: `「Tôi làm em căng thẳng à?」`
- Lý do: Soutetsu tự xưng "Anh" trong thoại (JP 緊張をさせてしまったか？) → "Tôi".

**Key 1045 (双鉄)**
- JP: `「ならば、遠慮無く――」`
- TW: `「那我就不客氣了」`
- VN cũ: `「Vậy thì, anh không khách sáo đâu nhé——」`
- Sửa: `「Vậy thì, tôi không khách sáo đâu nhé——」`
- Lý do: Soutetsu tự xưng "anh" trong thoại (JP ならば、遠慮無く) → "Tôi".

**Key 1401 (monologue)**
- JP: `わかってる。\n僕とてゴンゴン、最奥へ亀頭を叩きつけたい。`
- TW: `我知道的。我也想用龜頭盡情頂一頂她的花芯。`
- VN cũ: `Anh biết chứ.\nAnh cũng muốn đâm sầm sập, đập mạnh quy đầu vào nơi sâu nhất.`
- Sửa: `Tôi biết chứ. Tôi cũng muốn đâm sầm sập, đập mạnh quy đầu vào nơi sâu nhất.`
- Lý do: Soutetsu độc thoại tự xưng "Anh" ×2 (JP 僕とて) → "Tôi" ×2 (docs §2.1).

### Thở gấp っ bị bỏ mất (5 dòng)

**Key 904 (双鉄)**
- JP: `「っ！」`
- TW: `「唔」`
- VN cũ: `「っ!」`
- Sửa: `「Ư!」`
- Lý do: JP 「っ！」 bị bỏ mất trong VN (bản Việt còn nguyên っ) — sweep đã sửa, giá trị khớp (sweep-confirmed).

**Key 905 (双鉄)**
- JP: `「っ！」`
- TW: `「唔！」`
- VN cũ: `「っ!」`
- Sửa: `「Ư!」`
- Lý do: JP 「っ！」 bị bỏ mất trong VN (bản Việt còn nguyên っ) — sweep đã sửa, giá trị khớp (sweep-confirmed).

**Key 935 (ポーレット)**
- JP: `「っ！！！」`
- TW: `「啊！！！」`
- VN cũ: `「!!!」`
- Sửa: `「Ư!!!」`
- Lý do: JP 「っ！！！」 bị bỏ mất trong VN ("!!!" không có tiếng nấc) — sweep đã sửa, giá trị khớp (sweep-confirmed).

**Key 953 (双鉄)**
- JP: `「っ！」`
- TW: `「嘿」`
- VN cũ: `「っ!」`
- Sửa: `「Ư!」`
- Lý do: JP 「っ！」 bị bỏ mất trong VN (bản Việt còn nguyên っ) — sweep đã sửa, giá trị khớp (sweep-confirmed).

**Key 1228 (monologue)**
- JP: `これほどみっちり締められてなお、\nポーレットの肉が柔らかすぎて――っ！`
- TW: `即使波萊特的蜜肉夾得很緊，但實在還是太軟了。`
- VN cũ: `Dù bị siết chặt đến nhường này,\nnhưng phần thịt của Paulette lại quá mềm mại——!`
- Sửa: `Dù bị siết chặt đến nhường này, nhưng phần thịt của Paulette lại quá mềm mại——Ư!`
- Lý do: JP trailing ――っ！ bị bỏ mất trong VN ("——!") — sweep đã sửa, giá trị khớp (sweep-confirmed).

### Tiếng thở/tiếng rên để nguyên dạng La-tinh (5 dòng)

**Key 892 (ポーレット)**
- JP: `「ふっ――きゅううううううううっっ！！！」`
- TW: `「呼啊啊啊啊！！！」`
- VN cũ: `「Phù——kyuuuuuuuuu!!!」`
- Sửa: `「Phù——Siếttttttttt!!!」`
- Lý do: JP きゅううううううううっっ (tiếng siết dài) bị phiên âm "kyuuuuuuuuu" — theo tiền lệ h2 ("fuaaaaaaaaaaan" là lỗi) và chính file (きゅっ→"siết" ở 856): Việt hoá thành "Siếttttttttt" (kéo dài).

**Key 932 (双鉄)**
- JP: `「くあっ！」`
- TW: `「啊！」`
- VN cũ: `「Kua!」`
- Sửa: `「Ư a!」`
- Lý do: JP くあっ bị phiên âm "Kua!" — theo quyết định くぁ/くあ→"Ư a" (h6 800, 818; sfx doc くっ→"Hự"/"Ư").

**Key 947 (ポーレット)**
- JP: `「んきゅんっ！！！！」`
- TW: `「嗯呀！！！！」`
- VN cũ: `「Nkyun!!!!」`
- Sửa: `「Ưm!!!!」`
- Lý do: JP んきゅんっ bị phiên âm "Nkyun" — theo tiền lệ h4 (んきゅ→"Ưm") và h6 805 ("ưm").

**Key 949 (ポーレット)**
- JP: `「んきゅっ！　あっ――双鉄――くぅんっ！　んっ、\nもっと――ふか、くてっ――へい、きっ――わたしっ」`
- TW: `「嗯！啊——雙鐵！嗯——再深一點——我也——沒關係」`
- VN cũ: `「Nkyu! A——anh Soutetsu! Ưm,\nSâu——hơn nữa——em không, sao——đâu」`
- Sửa: `「Ưm! A——anh Soutetsu! Ưm, Sâu——hơn nữa——em không, sao——đâu」`
- Lý do: JP んきゅっ bị phiên âm "Nkyu" — theo tiền lệ h4 (んきゅ→"Ưm").

**Key 980 (ポーレット)**
- JP: `「わか、るつ――ぷくっ、て！　双鉄、くん――の――\nおちん――ひゅいっ！　あっ――おちん、ちんぅ」`
- TW: `「我感覺得到——漲大了！雙鐵君——你的雞雞——啊！啊——雞雞漲大了」`
- VN cũ: `「Em cảm, nhận được——đang phồng, lên! Của anh——Soutetsu——\nDương vật——hyui! A——dương, vật」`
- Sửa: `「Em cảm, nhận được——đang phồng, lên! Của anh——Soutetsu—— Dương vật——Huyi! A——dương, vật」`
- Lý do: JP ひゅいっ bị phiên âm "hyui" — Việt hoá thành "Huyi" (theo tiền lệ ひゃ→"Hya" ở h1/h2).

### Âm hiệu (SFX) (8 dòng)

**Key 826 (ポーレット)**
- JP: `「いえ――あの――そのっ――緊張、とかじゃなく。\nわたし……え……と……はうっ！」`
- TW: `「不是——那個——我沒有緊張——我……呃……啊……唔！」`
- VN cũ: `「Không——ừm——chuyện đó——không phải căng thẳng, đâu ạ.\nEm……ờ……thì……hự!」`
- Sửa: `「Không——ừm——chuyện đó——không phải căng thẳng, đâu ạ. Em……ờ……thì……Hau!」`
- Lý do: JP はうっ bị dịch "hự!" — theo tiền lệ sleeper 1781 và chính file này (974/897): はうっ→"Hau!".

**Key 942 (ポーレット)**
- JP: `「んっ……ちゅっ――ちゅむっ――ちゅうう――ちゅっ\n――ぷ、あっ――ん――れろっ――れるっ――れろおっ」`
- TW: `「嗯……啾——啾嚕——啾啾——啾嚕——呼、啊——嗯——啾嚕——啾嚕——啾噗」`
- VN cũ: `「Ưm……chụt——chu——chụtttt——chụt\n——Phù, a——ưm——liếm——liếm——liếmmmm」`
- Sửa: `「Ưm……chụt——chụt——chụtttt——chụt ——Phù, a——ưm——liếm——liếm——liếmmmm」`
- Lý do: JP ちゅむっ bị dịch "chu" — không nhất quán với chính file (h6 842: ちゅむっ→"chụt") và docs (ちゅっ→"Chụt").

**Key 1023 (ポーレット)**
- JP: `「わた、しの――おまん、こ――膣で、子宮、で――精液、\nびゅうびゅう――たくさん、おもらし――して、下さい」`
- TW: `「請在我的——小穴裡——陰道裡——子宮裡——射出好多精液——在裡面尿出來吧——」`
- VN cũ: `「Vào cô bé——của em——vào âm đạo, vào tử cung——\nHãy tè dầm——thật nhiều, tinh dịch——vào trong em, đi ạ」`
- Sửa: `「Vào cô bé——của em——vào âm đạo, vào tử cung—— Hãy tè dầm——thật nhiều, tinh dịch——phụt phụt——vào trong em, đi ạ」`
- Lý do: JP びゅうびゅう (tinh dịch phun ra) bị bỏ mất trong VN — bổ sung "phụt phụt" sau "tinh dịch" (đúng thứ tự JP: 精液、びゅうびゅう).

**Key 1691 (monologue)**
- JP: `（とんっ！）`
- TW: `（咚）`
- VN cũ: `（Bụp!）`
- Sửa: `（Cốc nhẹ!）`
- Lý do: JP とんっ bị dịch "Bụp!" — theo docs, とんっ→"Cốc nhẹ"/"Vỗ nhẹ".

**Key 1694 (monologue)**
- JP: `（ずっ――ずりゅっ――ぬっ――にゅぶうっ――）`
- TW: `（啾噗——啾噗——啾啪——啾啪——）`
- VN cũ: `（Phập——nhóp——rút——nhép——）`
- Sửa: `（Phập——nhóp——rút——rútttt——）`
- Lý do: JP にゅぶうっ bị dịch "nhép" — sai hướng: ぬぶ-family là rút ra (quy tắc h4), phải là "rútttt" (kéo dài theo っ).

**Key 1713 (monologue)**
- JP: `（ぐ、ぐいっ！　ぐっ――ずりりゅ――ぬるっ！？）`
- TW: `（拔出）`
- VN cũ: `（Hự, hự! Hự——tuột——tuột!?）`
- Sửa: `（Hự, Giật mạnh! Hự——tuột——tuột!?）`
- Lý do: JP ぐいっ (một cú giật/túm) bị dịch "Hự" (tiếng rên) — theo docs, ぐいっ→"Giật mạnh"/"Dứt khoát".

**Key 1717 (monologue)**
- JP: `（ぐいっ！）`
- TW: `（收腹）`
- VN cũ: `（Thóp bụng!）`
- Sửa: `（Giật mạnh!）`
- Lý do: JP ぐいっ bị dịch "Thóp bụng!" — bịa thêm động tác hóp bụng, chạy theo TW （收腹） mà bỏ JP/docs (ぐいっ→"Giật mạnh").

**Key 1723 (monologue)**
- JP: `（ちゅるう！　ちゅっ！　ぢゅずずっ！　れろおおっ！）`
- TW: `（用力吸吮）`
- VN cũ: `（Chụt! Chu! Sụtttt! Liếmmmmm!）`
- Sửa: `（Chụt! Chụt! Sụtttt! Liếmmmmm!）`
- Lý do: JP ちゅっ bị dịch "Chu" — không nhất quán với chính file (938, 942: ちゅっ→"chụt") và docs (ちゅっ→"Chụt").

### Sai nghĩa (1 dòng)

**Key 1290 (monologue)**
- JP: `考えてしまっては、果たせなくなる。\nただ、愛だけに――我と我が身を任せればいい。`
- TW: `如果仔細去想的話，那就沒有止境了。所以我只要把自己全盤交給心中的愛意來主導就好。`
- VN cũ: `Nếu cứ suy nghĩ thì sẽ chẳng làm được gì.\nChỉ cần, phó mặc bản thân và lý trí——cho tình yêu là đủ.`
- Sửa: `Nếu cứ suy nghĩ thì sẽ chẳng làm được gì. Chỉ cần, phó mặc bản thân và thể xác——cho tình yêu là đủ.`
- Lý do: JP 我が身 (thân thể của mình) bị dịch "lý trí" — sai nghĩa; phải là "thể xác" (我→"bản thân" đã đúng).

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
[script]
635 = "「……Lúc nãy, em có nói nhỉ. Đây là nơi em nấu cơm cho tôi ăn.」"
826 = "「Không——ừm——chuyện đó——không phải căng thẳng, đâu ạ. Em……ờ……thì……Hau!」"
839 = "「Nói cho tôi nghe đi. Nếu em không nói, tôi cũng chẳng biết giúp thế nào.」"
892 = "「Phù——Siếttttttttt!!!」"
904 = "「Ư!」"
905 = "「Ư!」"
932 = "「Ư a!」"
935 = "「Ư!!!」"
942 = "「Ưm……chụt——chụt——chụtttt——chụt ——Phù, a——ưm——liếm——liếm——liếmmmm」"
947 = "「Ưm!!!!」"
949 = "「Ưm! A——anh Soutetsu! Ưm, Sâu——hơn nữa——em không, sao——đâu」"
950 = "「Ừ, tôi đã hứa rồi. Nếu Paulette nghĩ đó là sự bẩn thỉu, tôi nhất định, sẽ hứng trọn lấy nó.」"
953 = "「Ư!」"
961 = "「Nếu Paulette cảm thấy đó là thứ bẩn thỉu. Thì tôi nhất định. Sẽ hứng trọn cả sự bẩn thỉu đó.」"
965 = "「Xin lỗi em. Tôi nhận ra hơi muộn.」"
976 = "「Nhưng nếu không nhìn thì sao tôi hứng được.」"
979 = "「Tôi đã nói rồi, không bẩn đâu. Đó là thứ tiết ra từ cơ thể Paulette mà.」"
980 = "「Em cảm, nhận được——đang phồng, lên! Của anh——Soutetsu—— Dương vật——Huyi! A——dương, vật」"
984 = "「Dùng cái này, tôi nhất định sẽ hứng lấy. Sẽ không để vương vãi ra bồn rửa dù chỉ một giọt.」"
986 = "「Tôi làm em căng thẳng à?」"
1023 = "「Vào cô bé——của em——vào âm đạo, vào tử cung—— Hãy tè dầm——thật nhiều, tinh dịch——phụt phụt——vào trong em, đi ạ」"
1045 = "「Vậy thì, tôi không khách sáo đâu nhé——」"
1228 = "Dù bị siết chặt đến nhường này, nhưng phần thịt của Paulette lại quá mềm mại——Ư!"
1290 = "Nếu cứ suy nghĩ thì sẽ chẳng làm được gì. Chỉ cần, phó mặc bản thân và thể xác——cho tình yêu là đủ."
1401 = "Tôi biết chứ. Tôi cũng muốn đâm sầm sập, đập mạnh quy đầu vào nơi sâu nhất."
1691 = "（Cốc nhẹ!）"
1694 = "（Phập——nhóp——rút——rútttt——）"
1713 = "（Hự, Giật mạnh! Hự——tuột——tuột!?）"
1717 = "（Giật mạnh!）"
1723 = "（Chụt! Chụt! Sụtttt! Liếmmmmm!）"
```

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- Soutetsu gọi Paulette "em" 8 lần trong thoại (635, 836, 838, 839, 965, 972, 986, 1026) vs "cô" 0 lần — cộng dồn toàn dự án: "em" 78 vs "cô" 43 (sau h5). Lưu ý: 1718 có "em ấy" nhưng là ngôi thứ ba trong độc thoại ("là do tôi ép em ấy phải nhịn sao"), KHÔNG tính là cách gọi. "Cô bé" tại 1023 là danh từ chỉ bộ phận (おまんこ), không phải cách xưng hô.
- "mình" trong độc thoại: 6 lần (1365, 1382, 1484, 1499, 1500, 1605) — tất cả đều đúng (1365 là danh từ "cửa mình"; còn lại là sở hữu/phản thân).
- Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói: 0 lần (mọi lần đều có "anh" trước tên).
- 御一夜: không xuất hiện trong file (0 lần cả 4 dạng Ohimitera/Ohito/Ohitoyo/御一夜).
- Không có 湯医/帝鉄/コン/宮司/マスコン/KiHa/整備体/運転ボディ/駿袋/Migita/オコジョ trong file.
- Paulette gọi Soutetsu "cậu": 0 lần. "Thẻ bảng": 0 lần.

## Đề xuất cập nhật context (chưa chốt)

- Quy tắc ちゅ-family: ちゅっ/ちゅう/ちゅるっ/ちゅむっ/ちゅろっ đều → "chụt" (theo docs + đa số trong file); "chu" là dạng sót, không phải biến thể có chủ ý — khi gặp ở file chưa audit, sửa về "chụt".
- Quy tắc hướng SFX (đã có từ h4, file này củng cố thêm): ぬぶ-family = rút ra ("Rút"), ず/ずぶ-family = đâm vào ("Phập") — đối chiếu JP từng âm, không đoán theo ngữ cảnh (1694: にゅぶうっ→"rútttt").

## Đã kiểm tra và KHÔNG tính là sai

- Các dòng ひゃ→"Hya" (849, 855, 859, 864, 992) — giữ theo tiền lệ h1/h2 (ひゃ là tiếng ré, giữ nguyên dạng phiên âm).
- 944 (ふぁんっ→"phù"): bỏ đuôi ん được chấp nhận theo tiền lệ h4 (ひゃん→"Hya"/"Hyan" đều được dung thứ).
- 954 (ふっ→"Phụt"): TW 噗 ủng hộ; đây là tiếng nổ ngắn, khác với ふっ hơi thở →"phù".
- 1019 (おしっこ→"Đi tè."): JP mơ hồ, ngữ cảnh ủng hộ dạng mệnh lệnh.
- 1047 ("sao" cuối câu): tiểu từ nhẹ cuối câu, không phải bịa thêm phần kết.
- 850/852/854 ("Ahyun"/"Hyaun"/"Hyakyu"): âm ghép viết liền một từ theo quy ước "Hyafu"/"Phuyan" đã chấp nhận.
- 631 (VN==TW `「…………」`): cả ba thứ tiếng đều là dấu lặng, đúng.
- Các bản Việt trùng trong file chỉ là tiếng rên/SFX ngắn lặp lại hợp lệ (xem trên).

## Kết bài

- h5 sai 30/305 (9,8%) — ngang mức trung bình của route Paulette, nhẹ hơn h3 (24,7%) và h4 (8,7%) thì nhỉnh hơn một chút. File sạch về cấu trúc; lỗi tập trung ở xưng hô hệ thống (11) + SFX (8) + thở gấp (5) + tiếng thở La-tinh (5) + sai nghĩa (1).
- Khối TOML 30 key đã parse đúng; áp dụng khối này sẽ sửa hết 30 dòng. Không có dòng chưa chắc chắn nào trong file này.
