# Audit — 凪ふかみ02_凪の大会初挑戦！.txt.toml

- File: `凪ふかみ02_凪の大会初挑戦！.txt.toml` — route 07_Nagi_Fukami, 517 dòng script (115 thoại Nagi, 102 thoại Fukami, 83 thoại Soutetsu, 5 thoại Nakamura, 3 thoại trọng tài, 209 độc thoại — toàn bộ độc thoại là góc nhìn Fukami).
- Nội dung: Nagi dự giải kiếm đạo lần đầu — Soutetsu làm huấn luyện viên, Fukami kể chuyện/hỗ trợ hậu cần (hộp cứu thương, chanh mật ong, nước uống). Xung đột chính: Thể Xá Lưu (dùng cả thể thuật, đòn vật, chém chéo 袈裟懸け) bị luật kiếm đạo cấm (cấm thể thuật, cấm đâm, cấm chém chéo dưới cấp Trung học; chỉ được dùng tư thế Trung Đoạn/Chính Nhãn), Nagi phải thắng bằng "tâm" trong khuôn khổ luật; xen kẽ cảnh tập luyện trong bụi tre (chém tre bằng kiếm gỗ, sát khí, 殺気). Không có H-scene.
- **Kết quả: 32/517 dòng sai (6,2%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. Bằng chứng: không có giá trị VN nào lặp lại ở 2 key có JP khác nhau (quét toàn file — 4 cặp VN trùng đều là JP lặp lại thật: 1470/1471 「――っ」, 2012/2054, 2169/2170 「はいっ！」, 2105/2106 tiếng hô チェスト); mọi VN đều khớp nghĩa JP của chính key đó; kiểm tra nhiễm chéo toàn dự án: chỉ 3 dòng có VN trùng với dòng JP khác ở file khác (2105, 2106, 2401) và cả 3 đều là SFX hô/thở lặp lại hợp lệ, không phải dòng bị chép nhầm. CSV3 1 set duy nhất (517 dòng, 0 khóa trùng, 0 ô VN trống, 0 ô JP trống, 0 dòng VN == TW).
- VN khớp TOML tuyệt đối 517/517 key (0 lệch thực chất — 287 dòng chỉ khác ở chỗ TOML-2 làm phẳng dấu `\n` thành khoảng trắng, đã biết, không phải lỗi). `[selections]` rỗng (0 mục). Số thẻ `%l` JP vs VN bằng nhau ở mọi dòng (0 lệch); không có thẻ VN tự thêm, không có thẻ sai định dạng.
- TOML md5 `25803e1c333ba074a159e5e9f7d60aa1`; không có bản sao file này (chỉ 1 file trùng tên mẫu trong toàn bộ 227 file — không thuộc 11 nhóm trùng).
- Đại từ: Soutetsu "anh" với Nagi/Fukami đúng toàn file trừ 3 dòng "tôi" đã sửa (1508, 2243, 2248 — cả 3 đều nói với Nagi/Fukami, không có Hachiroku trong cảnh). Soutetsu gọi Nagi/Fukami là "em" đúng. Nagi gọi Fukami "cậu" (4 lần: 2039, 2056, 2165, 2412 — dạng ngang hàng, đúng theo tiền lệ 凪ふかみ01); không có "chị" cho Fukami ở đâu. Fukami tự xưng "tớ" với Nagi (3 dòng) và "mình" (nhiều dòng) — cả hai đều là dạng ngang hàng đúng, giữ nguyên (tiền lệ 01: "Fukami tự xưng 'tớ' với Nagi — đúng"; 08b: "mình" là dạng đúng). Độc thoại Fukami dùng "mình" 37 dòng, chỉ 18 dòng lạc sang "tôi" (đã sửa, §2 — cùng cách xử lý như 08a: 13 dòng độc thoại Fukami "tôi"→"mình").
- Thuật ngữ: バイ捨流→"Thể Xá Lưu" đúng ở mọi dòng trừ 2 dòng "phái Taisha" đã sửa (1962, 2482); 正眼→"Chính Nhãn" đúng (2153, 2255, 3224) trừ 1 dòng "Seigan" đã sửa (2429); 日ノ本→"Hinomoto" 1/1 đúng (2287); 残心→"tàn tâm" đúng (2479 — khớp tiền lệ 08a 2403 "thế tàn tâm"); 投炭→"xúc than" nhất quán toàn file; 忠等部 là lỗi chính tả trong JP gốc (2134, 2331 — TW viết đúng 中等部, VN dịch đúng "trung học cơ sở", không sửa).

## §2. Danh sách sửa (32 dòng)

Phân loại: pronoun 21 (Soutetsu "tôi"→"anh" 3 dòng: 1508, 2243, 2248; độc thoại Fukami "tôi"→"mình" 18 dòng: 2674, 2686, 2857, 2880, 2941, 2942, 2997, 3001, 3011, 3024, 3026, 3083, 3151, 3201, 3205, 3212, 3220, 3230), gasp 5 (1470, 1471, 2082, 2688, 2771 — cả 5 từ sweep, đã kiểm chứng JP), terminology 3 (1962, 2482 "Taisha"→"Thể Xá Lưu"; 2429 "Seigan"/"Daijodan"→"Chính Nhãn"/"Đại Thượng Đoạn"), sfx 2 (2042, 2852), consistency 1 (1511 "kami"→"kami-chan").

### 1470 — Nagi — gasp
- JP: 「――っ」
- TW: 「——」
- VN cũ: 「——」
- Sửa: 「——Ư」
- Lý do: Sweep lost-gasp-trailing: っ cuối tuyệt đối, không còn dấu câu nào sau nó — âm gasp mất hoàn toàn trong VN cũ. Đã kiểm chứng khớp sweep.

### 1471 — Nagi — gasp
- JP: 「――っ」
- TW: 「——呼」
- VN cũ: 「——」
- Sửa: 「——Ư」
- Lý do: Như 1470 (sweep lost-gasp-trailing). TW còn có 呼 (hơi thở) — VN cũ mất cả hai.

### 1508 — Soutetsu — pronoun
- JP: 「……なんだ、僕だけ仲間はずれか」
- TW: 「……好像只有我被排擠在外啊」
- VN cũ: 「……Gì đây, chỉ có mình tôi bị cho ra rìa sao.」
- Sửa: 「……Gì đây, chỉ có mình anh bị cho ra rìa sao.」
- Lý do: Soutetsu nói to với cả nhóm (Nagi + Fukami đang ăn cùng, 1506 はむっ) — theo quy tắc đã chốt, "anh" với Nagi/Fukami. "Tôi" chỉ đúng với Hachiroku/Mayami/Minokasa/Kisaki, không ai trong số đó có mặt ở cảnh này.

### 1511 — Nagi — consistency
- JP: 「……かみちゃん？　ふかみちゃーん！！」
- TW: 「……小深？　小深！！」
- VN cũ: 「……kami? Fukami ơiii!!」
- Sửa: 「……kami-chan? Fukami-chan ơiii!!」
- Lý do: Cùng một câu JP với 1473 ("kami-chan? Fukami-chan~") nhưng VN cũ bỏ "-chan" ở cả hai chỗ. かみちゃん đứng độc lập chỉ xuất hiện 2 lần trong toàn dự án, cả hai đều ở file này — chuẩn hoá theo 1473.

### 1962 — Soutetsu — terminology
- JP: 「今のところはまずまずだが、さっきの二本目は、\nバイ捨流の癖が出た。振り上げを右肩に担いだぞ」
- TW: 「剛才還算馬馬虎虎，但是第二局時你又表現出體舍流的習慣，舉劍時竹刀舉到右肩上方了」
- VN cũ: 「Hiện tại thì cũng tạm ổn, nhưng ở hiệp thứ hai vừa nãy,\nthói quen của phái Taisha đã bộc lộ. Em đã vác kiếm lên vai phải khi vung đấy.」
- Sửa: 「Hiện tại thì cũng tạm ổn, nhưng ở hiệp thứ hai vừa nãy,\nthói quen của phái Thể Xá Lưu đã bộc lộ. Em đã vác kiếm lên vai phải khi vung đấy.」
- Lý do: JP バイ捨流, TW 體舍流. File này dùng "Thể Xá Lưu" ở mọi chỗ khác (1491, 1822, 2138, 2153, 2163, 2279, 2280, 2283, 2287, 2483) — "phái Taisha" là phiên âm lạc, không nhất quán nội bộ.

### 2042 — Nagi — sfx
- JP: 「ぴきゃうっ！！」\n「双鉄おにいさん！」
- TW: 「哇！！」\n「雙鐵哥哥！」
- VN cũ: 「Ái da!!」\n「Anh Soutetsu!」
- Sửa: 「Á!!」\n「Anh Soutetsu!」
- Lý do: JP ぴきゃうっ là tiếng kêu thất thanh vì giật mình (TW 哇), không phải vì đau. VN cũ "Ái da" mang nghĩa đau — sai sắc thái. "Á!!" khớp tiếng kêu giật mình.

### 2082 — Fukami — gasp
- JP: 「っ！！」
- TW: 「啊！！」
- VN cũ: 「!!」
- Sửa: 「Ư!!」
- Lý do: Sweep lost-gasp-whole: cả dòng chỉ là một tiếng gasp っ, VN cũ mất hoàn toàn. Đã kiểm chứng khớp sweep.

### 2243 — Soutetsu — pronoun
- JP: 「僕はかまわん。\n――ナビも、喜んでといっている」
- TW: 「我不介意。——Ｎａｖｉ也說很樂意」
- VN cũ: 「Tôi không phiền đâu.\n——Navi cũng nói là rất sẵn lòng đấy.」
- Sửa: 「Anh không phiền đâu.\n——Navi cũng nói là rất sẵn lòng đấy.」
- Lý do: Soutetsu trả lời Nagi (hỏi mượn Navi) — người nghe là Nagi/Fukami → "anh" theo quy tắc đã chốt. Các dòng Soutetsu xung quanh cùng cảnh đều dùng "anh" (2247, 2250, 2252, 2255, 2256, 2258).

### 2248 — Soutetsu — pronoun
- JP: 「うむ。これから凪と稽古をするのだが――」
- TW: 「我們今後要練習劍道——」
- VN cũ: 「Ừm. Từ giờ tôi sẽ luyện tập với Nagi, nhưng mà——」
- Sửa: 「Ừm. Từ giờ anh sẽ luyện tập với Nagi, nhưng mà——」
- Lý do: Soutetsu báo với Fukami (hoặc Nagi) về việc sẽ luyện tập với Nagi — dù người nghe là ai trong hai người thì cũng là "anh" theo quy tắc đã chốt. Không có Hachiroku/Mayami/Minokasa/Kisaki trong cảnh.

### 2429 — Soutetsu — terminology
- JP: 「踏み出しにあわせ、正眼から振りかぶって大上段。\nそのまま止まらずに面打ちならば、凪の剣は活きる」
- TW: 「踏步時從正眼上撩轉為大上段架勢，接著直接擊面。這樣一來就能讓凪的劍法施展出來」
- VN cũ: 「Kết hợp với bước chân, từ thế Seigan vung kiếm lên Daijodan.\nRồi không dừng lại mà đánh thẳng vào mặt thì kiếm của Nagi mới phát huy được.」
- Sửa: 「Kết hợp với bước chân, từ thế Chính Nhãn vung kiếm lên Đại Thượng Đoạn.\nRồi không dừng lại mà đánh thẳng vào mặt thì kiếm của Nagi mới phát huy được.」
- Lý do: File này dịch tên thế kiếm bằng Hán-Việt ở mọi chỗ khác: 正眼→"Chính Nhãn" (2153, 2255, 3224), 中段→"Trung Đoạn" (2153) — "Seigan"/"Daijodan" phiên âm là lạc quy ước nội bộ. 大上段 là thế thượng đoạn lớn → "Đại Thượng Đoạn". (大上段 chỉ xuất hiện 1 lần trong toàn dự án, ở dòng này.)

### 2482 — Soutetsu — terminology
- JP: 「バイ捨流の基本にして究極は右半開からの袈裟懸けだ。\nしかし、それは禁じ手ゆえに、凪の剣筋は制限される」
- TW: 「體舍流的基礎以及最強的一招，就是右半開後的斜劈斬。但這卻是禁止使用的招數，所以凪的劍法會受到限制」
- VN cũ: 「Căn bản và cũng là tuyệt kỹ của phái Taisha là chém chéo từ tư thế mở nửa người sang phải.\nNhưng vì đó là đòn cấm, nên đường kiếm của Nagi bị hạn chế.」
- Sửa: 「Căn bản và cũng là tuyệt kỹ của phái Thể Xá Lưu là chém chéo từ tư thế mở nửa người sang phải.\nNhưng vì đó là đòn cấm, nên đường kiếm của Nagi bị hạn chế.」
- Lý do: Như 1962 — JP バイ捨流, TW 體舍流; "phái Taisha" lạc với toàn file.

### 2674 — monologue (Fukami) — pronoun
- JP: けど、今ならわかる。
- TW: 但我現在理解了。
- VN cũ: Nhưng bây giờ thì tôi đã hiểu.
- Sửa: Nhưng bây giờ thì mình đã hiểu.
- Lý do: Độc thoại Fukami — quy ước của chính file này là "mình" (37 dòng "mình" vs 18 dòng "tôi"; JP không có đại từ nhưng mạch cảnh là Fukami, dòng trước 2672 đã dùng "mình"). Cùng cách xử lý như 08a (13 dòng độc thoại Fukami "tôi"→"mình").

### 2686 — monologue (Fukami) — pronoun
- JP: そしたら、怖いのがパアって消える。\n今、何が起きたのか……おっかない、けど、知りたくなる。
- TW: 先前的恐懼立刻就消散了。雖然很害怕，但我又好奇起剛才發生了什麼事。
- VN cũ: Thế rồi, nỗi sợ hãi tan biến đi mất.\nBây giờ, chuyện gì vừa xảy ra……dù sợ, nhưng tôi vẫn muốn biết.
- Sửa: Thế rồi, nỗi sợ hãi tan biến đi mất.\nBây giờ, chuyện gì vừa xảy ra……dù sợ, nhưng mình vẫn muốn biết.
- Lý do: Độc thoại Fukami (mạch tiếp sau 2684 "con đường mình đang đi") → "mình" theo quy ước file.

### 2688 — monologue (Fukami) — gasp
- JP: 一気に大きく振りかぶって、そのまま相手に――っ！？
- TW: 全力將竹刀舉起，直接將對手——！？
- VN cũ: Một mạch vung kiếm lên cao, rồi cứ thế lao vào đối thủ——!?
- Sửa: Một mạch vung kiếm lên cao, rồi cứ thế lao vào đối thủ——Ư!?
- Lý do: Sweep lost-gasp-trailing: っ cuối câu bị mất trong VN cũ. Đã kiểm chứng khớp sweep.

### 2771 — monologue (Fukami) — gasp
- JP: はんかいって、多分、半分ひらく、なんだと思う。\n凪ちゃんの体、名前の通り半身になって――っ！
- TW: 半開指的應該就是半敞開身體。小凪現在就如同架勢名稱一樣，將身體半側向一邊——
- VN cũ: Bán khai, chắc có nghĩa là mở một nửa.\nCơ thể của Nagi, đúng như cái tên, xoay nửa người lại——!
- Sửa: Bán khai, chắc có nghĩa là mở một nửa.\nCơ thể của Nagi, đúng như cái tên, xoay nửa người lại——Ư!
- Lý do: Sweep lost-gasp-trailing: っ cuối câu bị mất trong VN cũ. Đã kiểm chứng khớp sweep. (Lưu ý: giá trị fix của sweep dùng khoảng trắng thay cho `\n` của CSV3 — bản sửa này giữ nguyên `\n` theo CSV3, chỉ thêm Ư.)

### 2852 — monologue (Fukami) — sfx
- JP: 凪ちゃんはびっくりした顔して、\nそれからけらけら笑い出す。
- TW: 她吃了一驚，然後大大剌剌地笑起來。
- VN cũ: Nagi làm vẻ mặt giật mình,\nrồi cười khúc khích.
- Sửa: Nagi làm vẻ mặt giật mình,\nrồi cười ha hả.
- Lý do: JP けらけら là cười lớn, sảng khoái không kìm nén (TW 大大剌剌地笑 — cười thoải mái, bộc trực). VN cũ "cười khúc khích" là cười khúc khích nhỏ, nhẹ — yếu hẳn so với JP/TW.

### 2857 — monologue (Fukami) — pronoun
- JP: その横顔に、一瞬、みとれる。\n静かで、綺麗で――汗の粒さえ、宝石みたい。
- TW: 她恬靜秀麗的側臉不禁讓我看呆了，就連汗珠都像寶石一樣閃耀。
- VN cũ: Góc nghiêng ấy, khiến tôi thoáng chốc mê mẩn.\nThật tĩnh lặng, thật xinh đẹp——ngay cả những giọt mồ hôi cũng lấp lánh như ngọc vậy.
- Sửa: Góc nghiêng ấy, khiến mình thoáng chốc mê mẩn.\nThật tĩnh lặng, thật xinh đẹp——ngay cả những giọt mồ hôi cũng lấp lánh như ngọc vậy.
- Lý do: Độc thoại Fukami ngắm góc nghiêng của Nagi (TW 讓我看呆了 — "làm tôi nhìn đến ngẩn ra", người nhìn là Fukami) → "mình" theo quy ước file.

### 2880 — monologue (Fukami) — pronoun
- JP: 今日の凪ちゃんを見るまえだったら、\n“安全対策？”って、きっとなってた。
- TW: 如果沒有看到小凪今天這副樣子，我一定會對這個主意感到疑惑。
- VN cũ: Nếu chưa nhìn thấy Nagi-chan của ngày hôm nay,\nchắc chắn tôi đã thắc mắc "Biện pháp an toàn á?".
- Sửa: Nếu chưa nhìn thấy Nagi-chan của ngày hôm nay,\nchắc chắn mình đã thắc mắc "Biện pháp an toàn á?".
- Lý do: Độc thoại Fukami (TW 我一定會 — "tôi nhất định sẽ", người thắc mắc là Fukami) → "mình" theo quy ước file.

### 2941 — monologue (Fukami) — pronoun
- JP: 凪ちゃんが嫌がってたこと、審判の人が離してくれて――\nこれで勝てるってきっと思った。
- TW: 小凪當時很煩躁，裁判將二人分開後，我以為比賽已經十拿九穩。
- VN cũ: Nagi-chan vốn rất khó chịu với điều đó, nhưng trọng tài đã tách họ ra——\nNên tôi đinh ninh rằng thế này là nắm chắc phần thắng rồi.
- Sửa: Nagi-chan vốn rất khó chịu với điều đó, nhưng trọng tài đã tách họ ra——\nNên mình đinh ninh rằng thế này là nắm chắc phần thắng rồi.
- Lý do: Độc thoại Fukami (TW 我以為 — "tôi tưởng rằng") → "mình" theo quy ước file.

### 2942 — monologue (Fukami) — pronoun
- JP: 返事なんてない。できるわけない。\nけど、ちゃんと、凪ちゃんにも聞こえてるってわかる。
- TW: 小凪當然沒有餘力回答，但她一定聽到了雙鐵哥哥的指點。
- VN cũ: Không có tiếng đáp lại. Làm sao mà trả lời được cơ chứ.\nNhưng tôi biết, Nagi-chan vẫn nghe thấy rất rõ.
- Sửa: Không có tiếng đáp lại. Làm sao mà trả lời được cơ chứ.\nNhưng mình biết, Nagi-chan vẫn nghe thấy rất rõ.
- Lý do: Độc thoại Fukami nghĩ về Nagi (disp=凪 chỉ là tên hiển thị của cảnh, còn người kể vẫn là Fukami — TW "她一定聽到了" nói về Nagi ở ngôi thứ ba) → "mình" theo quy ước file.

### 2997 — monologue (Fukami) — pronoun
- JP: しゃがんじゃう！\n何か来るって思って怖くて、体が動かなくなる！
- TW: 我不知道發生了什麼事，嚇得原地蹲下不敢動彈。
- VN cũ: Tôi ngồi thụp xuống!\nSợ hãi vì nghĩ có thứ gì đó sắp tới, cơ thể tôi cứng đờ không cử động nổi!
- Sửa: Mình ngồi thụp xuống!\nSợ hãi vì nghĩ có thứ gì đó sắp tới, cơ thể mình cứng đờ không cử động nổi!
- Lý do: Độc thoại Fukami (TW 我嚇得原地蹲下 — "tôi sợ đến ngồi thụp xuống") → "mình" theo quy ước file. Cả hai đại từ "tôi" trong dòng đều đổi.

### 3001 — monologue (Fukami) — pronoun
- JP: わたしも、した。\nホっとしちゃった。
- TW: 我也一樣，當時懸著的心都放下來了。
- VN cũ: Tôi cũng vậy.\nTôi đã thở phào nhẹ nhõm.
- Sửa: Mình cũng vậy.\nMình đã thở phào nhẹ nhõm.
- Lý do: JP わたし (Fukami) → "mình" theo quy ước file. Cả hai đại từ đều đổi.

### 3011 — monologue (Fukami) — pronoun
- JP: 凪ちゃんとパって目が合う。\n頷きあう。
- TW: 我和小凪四目相對，點了點頭。
- VN cũ: Tôi và Nagi-chan chợt chạm mắt nhau.\nCùng gật đầu.
- Sửa: Mình và Nagi-chan chợt chạm mắt nhau.\nCùng gật đầu.
- Lý do: Độc thoại Fukami (TW 我和小凪 — "tôi và Nagi") → "mình" theo quy ước file.

### 3024 — monologue (Fukami) — pronoun
- JP: 双鉄おにいさんの声にも、感じる。\nこれって、やっぱり、チャンスなんだ！！
- TW: 我聽得出雙鐵哥哥的高興的聲音，這一定就是取勝的機會！！
- VN cũ: Qua giọng nói của anh Soutetsu, tôi cũng cảm nhận được.\nQuả nhiên, đây chính là cơ hội!!
- Sửa: Qua giọng nói của anh Soutetsu, mình cũng cảm nhận được.\nQuả nhiên, đây chính là cơ hội!!
- Lý do: Độc thoại Fukami (TW 我聽得出 — "tôi nghe ra được") → "mình" theo quy ước file.

### 3026 — monologue (Fukami) — pronoun
- JP: わたしに出来るお手伝い。\n救急箱と、レモンの蜂蜜づけと、スポーツドリンク。
- TW: 我能幫上的忙……就是帶好急救箱、蜂蜜檸檬、運動飲料。
- VN cũ: Việc mà tôi có thể giúp.\nHộp cứu thương, chanh ngâm mật ong, và nước uống thể thao.
- Sửa: Việc mà mình có thể giúp.\nHộp cứu thương, chanh ngâm mật ong, và nước uống thể thao.
- Lý do: JP わたし (Fukami) → "mình" theo quy ước file.

### 3083 — monologue (Fukami) — pronoun
- JP: どんなに小さなことだって、\nわたしもできるお手伝い、絶対あるって思うから。
- TW: 無論是多麼微不足道的小事，一定會有我幫得上忙的地方。
- VN cũ: Dù là việc nhỏ nhặt đến đâu,\ntôi tin chắc chắn cũng có việc tôi có thể giúp được.
- Sửa: Dù là việc nhỏ nhặt đến đâu,\nmình tin chắc chắn cũng có việc mình có thể giúp được.
- Lý do: JP わたし (Fukami) → "mình" theo quy ước file. Cả hai đại từ đều đổi.

### 3151 — monologue (Fukami) — pronoun
- JP: 対策……とか言われちゃうと、\nなんだか、すごくヤな感じがする。
- TW: 聽雙鐵哥哥說被針對了……我忽然有種不好的預感。
- VN cũ: Bị nói là bắt bài...\nlàm tôi có cảm giác rất không lành.
- Sửa: Bị nói là bắt bài...\nlàm mình có cảm giác rất không lành.
- Lý do: Độc thoại Fukami (TW 我忽然有種不好的預感 — "tôi bỗng có dự cảm không lành") → "mình" theo quy ước file.

### 3201 — monologue (Fukami) — pronoun
- JP: ざっ、って。枯れ葉を踏むみたいな音。\nふうって、息が抜ける音。わたしの耳になじむ音。
- TW: 這時耳邊傳來踩踏枯葉的聲音，以及早已聽慣的呼氣聲。
- VN cũ: Xoạt, âm thanh như dẫm lên lá khô.\nPhù, tiếng thở hắt ra. Những âm thanh quen thuộc với đôi tai tôi.
- Sửa: Xoạt, âm thanh như dẫm lên lá khô.\nPhù, tiếng thở hắt ra. Những âm thanh quen thuộc với đôi tai mình.
- Lý do: JP わたしの耳 (tai của Fukami) → "mình" theo quy ước file.

### 3205 — monologue (Fukami) — pronoun
- JP: その位は、わたしも知ってる。\n手のこと、手首のこと――けどっ！
- TW: 這詞的意思連我也知道，指的是擊打手腕……可是不應該會這樣啊！
- VN cũ: Chừng đó thì, tôi cũng biết.\nLà nói về tay, về cổ tay——Nhưng mà!
- Sửa: Chừng đó thì, mình cũng biết.\nLà nói về tay, về cổ tay——Nhưng mà!
- Lý do: JP わたしも (Fukami) → "mình" theo quy ước file.

### 3212 — monologue (Fukami) — pronoun
- JP: 怖いし、一瞬でも遅れたらバシってされるし、\nわたしだったら、絶対できない。
- TW: 那太恐怖了，而且哪怕只慢了一瞬間都會被擊中，如果是我就絕對做不到。
- VN cũ: Rất đáng sợ, chỉ cần chậm một giây thôi là sẽ bị đánh trúng,\nnếu là tôi, tuyệt đối không thể làm được.
- Sửa: Rất đáng sợ, chỉ cần chậm một giây thôi là sẽ bị đánh trúng,\nnếu là mình, tuyệt đối không thể làm được.
- Lý do: JP わたしだったら (nếu là Fukami) → "mình" theo quy ước file.

### 3220 — monologue (Fukami) — pronoun
- JP: 専門用語はわからないけど、\n凪ちゃんが綺麗だったの、わたしにもすごくわかる！
- TW: 雖然聽不懂這些專業術語，但我能明白小凪的表現非常精彩！
- VN cũ: Dù không hiểu các thuật ngữ chuyên môn,\nnhưng tôi cũng thấy rõ Nagi-chan đánh rất đẹp mắt!
- Sửa: Dù không hiểu các thuật ngữ chuyên môn,\nnhưng mình cũng thấy rõ Nagi-chan đánh rất đẹp mắt!
- Lý do: JP わたしにも (Fukami) → "mình" theo quy ước file.

### 3230 — monologue (Fukami) — pronoun
- JP: さすが、双鉄おにいさん。\nわかった気がする。わたしにも。
- TW: 雙鐵哥哥真是厲害，連我也明白了其中深意。
- VN cũ: Quả không hổ danh là anh Soutetsu.\nHình như tôi cũng hiểu ra rồi.
- Sửa: Quả không hổ danh là anh Soutetsu.\nHình như mình cũng hiểu ra rồi.
- Lý do: JP わたしにも (Fukami, disp=深美) → "mình" theo quy ước file.

## §3. Lượt soát 2 (đọc lại toàn bộ 32 giá trị sửa đối chiếu JP)

- Tổng: 32 / đã kiểm chứng lại: 32 / bỏ: 0 / sửa: 0.
- Kiểm tra bổ sung trong lượt 2: mỗi bản sửa chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm chứng bằng máy: mọi diff đều là chèn Ư, đổi "tôi"→"mình"/"anh", đổi "Taisha"→"Thể Xá Lưu", đổi "Seigan"/"Daijodan", thêm "-chan", đổi SFX — không có dòng nào bị viết lại lớn); 2771 giữ nguyên `\n` của CSV3 (giá trị fix của sweep dùng khoảng trắng đã được sửa lại cho khớp CSV3).
- Sweep: 5 mục cho file này (1470, 1471, 2082, 2688, 2771), áp nguyên cả 5 sau khi kiểm chứng JP; tự quét toàn bộ っ trong file không phát hiện gasp nào sweep bỏ sót (các っ còn lại đều đã được diễn đạt: きゃっ→"Á!", えええっ→"Hảảả!", ふうっ→"Phù——", v.v.).

## §4. Ghi chú kiểm chứng (không tính sai)

- **Đính chính về Seki / key 2299:** nhiệm vụ giao ghi key 2299 của file này phải dùng "ông ngoại" (Seki là ông ngoại của Fukami). Kiểm chứng trực tiếp: file này KHÔNG có dòng nào nhắc tới Seki (堰) hay ông nội/ông ngoại — key 2299 của file này là thoại Soutetsu 「意味がどうかはわからんが、結果を示せなくなるのは、確かだ」 (không liên quan tới ông). Dòng Seki "ông nội"→"ông ngoại" thật sự nằm ở file **凪ふかみ02_命の重さ.txt.toml key 2299** (monologue: 「ふかみの祖父とそのご兄弟、堰さんたち…」 — VN cũ "ông nội Fukami… ông Seki"). Ghi chú trong brief bị gán nhầm file (cả hai file đều tên 凪ふかみ02). Không có gì để áp dụng trong file này; việc sửa "ông ngoại" thuộc về file 命の重さ khi tới lượt audit nó.
- **忠等部 (2134, 2331):** JP gốc viết sai thành 忠等部 (đúng ra 中等部); TW viết đúng 中等部, VN dịch đúng "trung học cơ sở" — lỗi của JP gốc, không phải lỗi VN, không sửa.
- **Nagi tự xưng trong thoại — giữ nguyên biến thể:** Nagi dùng "mình" (13 lần), "tớ" (7 lần: 2026, 2034, 2123, 2193, 2205, 2360, 2363) và "em" (9 lần, chủ yếu với Soutetsu nhưng có 1862 với Fukami) — không có quy tắc đã chốt cho tự xưng thoại của Nagi; tiền lệ 凪ふかみ01 giữ nguyên biến thể và để Hieu quyết có thống nhất về "tớ"/"mình" hay không. File này làm theo tiền lệ đó: không sửa dòng nào trong nhóm này.
- **Fukami tự xưng trong thoại — giữ nguyên biến thể:** "tớ" với Nagi (2168, 2225, 2451) và "mình" (nhiều dòng) đều là dạng ngang hàng đúng; chỉ độc thoại mới chuẩn hoá về "mình" (§2).
- **次元流 (2280, 2377, 3109) — KHÔNG sửa, chờ Hieu (xem §5):** JP viết 次元流 với furigana じげん, TW dùng 示現流 (trường phái Jigen-ryū có thật, đúng với mô tả "một nhát chém hạ gục đối thủ"), VN cũ dịch theo mặt chữ Hán thành "Thứ Nguyên Lưu". Cả 3 dòng 次元流 trong toàn dự án đều ở file này, không có tiền lệ chéo để đối chiếu.
- **バキーン → "Bốp" (key 30, 3279):** giữ nguyên — SFX va chạm, file dùng nhất quán cả hai chỗ, không sai rõ nghĩa.
- **1491 (Fukami, 「バイ捨流を使えるのなら――って」 → "Nếu có thể sử dụng Thể Xá Lưu——sao."):** đuôi って bỏ lửng, VN cũ thêm "sao." thành câu hỏi — có thể là lệch sắc thái nhẹ, nhưng chưa đủ chắc để tính sai. Ghi lại để Hieu xem, không đưa vào khối sửa.
- **2079 (Nagi nói ngọng vì ngậm thức ăn, 「ふぁむっ――もむもむ――へへ、ほんはほはえほはは、ひふへもはいはんへいはい」 → "Ngoạm——nhóp nhép—— Hehe, trả đũa lại nè, há miệng ra nào."):** câu nói ngọng không giải mã chắc chắn được từ JP/TW (TW chỉ diễn ý "cũng xem chiêu này của tôi") — giữ nguyên VN cũ, không đoán.

## §5. Chờ Hieu quyết

1. **次元流 → "Thứ Nguyên Lưu" hay "Thị Hiện Lưu"?** (2280, 2377, 3109 — cả 3 dòng trong file này, cũng là cả 3 dòng trong toàn dự án.) JP viết 次元流, đọc じげん; TW viết 示現流; VN cũ "Thứ Nguyên Lưu" dịch theo mặt chữ. Nếu theo TW/trường phái thật thì đổi thành "Thị Hiện Lưu" (Hán-Việt của 示現流); nếu giữ mặt chữ game thì giữ "Thứ Nguyên Lưu".
2. **Nagi tự xưng trong thoại: có thống nhất "tớ"/"mình"/"em" không?** (như tiền lệ 01 key 1517 — 1862 "em" với Fukami, các dòng "tớ" 2026/2034/2123/2193/2205/2360/2363.) Hiện giữ nguyên biến thể.
3. **1491:** đuôi って bỏ lửng — "——sao." có giữ hay đổi thành "——thì…"?
4. **2079:** câu nói ngọng của Nagi — VN cũ "trả đũa lại nè, há miệng ra nào" có giữ không, hay cần nghe voice trong game để xác nhận?

## Khối TOML (đã parse-kiểm chứng, 32 khóa, 0 sai lệch giá trị)

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

## Kết bài

File 凪ふかみ02_凪の大会初挑戦！ đã audit xong toàn bộ 517 dòng: **32 dòng sai (6,2%)** — pronoun 21 (độc thoại Fukami "tôi"→"mình" 18, Soutetsu "tôi"→"anh" 3), gasp 5 (sweep, đã kiểm chứng), terminology 3, sfx 2, consistency 1. Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 32 khóa đã parse-kiểm chứng, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 32/32; lượt soát 2: 32/32, 0 bỏ, 0 sửa. File này sạch hơn mức trung bình của route Nagi-Fukami (08a 4,3% là sạch nhất, 01 là 9,5%). Còn chờ Hieu 4 mục (§5), trong đó quan trọng nhất là 次元流 (3 dòng, toàn dự án chỉ có 3 dòng này).
