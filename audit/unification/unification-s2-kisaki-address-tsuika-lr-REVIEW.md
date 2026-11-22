# Unification U7b — §2 P4: Kisaki → Soutetsu, bare "Soutetsu" (tsuika + lr files)

## §0. Phạm vi

Mục §2 P4 (DECIDED 21/11 ~19:45, Muse theo uỷ quyền): Kisaki gọi Soutetsu bằng tên trần **"Soutetsu"**, không bao giờ "anh Soutetsu". Kisaki là senpai của Soutetsu (sếp ngân hàng cũ, senpai của Hibiki, giám đốc chi nhánh Kumagin); JP là 双鉄 trần trong mọi dòng đã kiểm chứng.

**File trong phạm vi đợt này (6 file):**
- `lr稀咲追加01_仲国視察の誘い.txt.toml` (06_Kisaki) — 3 dòng sửa
- `lr稀咲追加02_仲国視察.txt.toml` (06_Kisaki) — 4 dòng sửa
- `lr稀咲追加03_新事業案.txt.toml` (06_Kisaki) — 0 dòng (4 dòng "anh Soutetsu" đã sửa sẵn trong audit, xem §3)
- `lr_稀咲h1_おしおきとごほうび.txt.toml` (06_Kisaki) — 0 dòng (đã đúng dạng trần "Soutetsu" toàn file)
- `lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml` (06_Kisaki) — 23 dòng sửa
- `lr_稀咲ポーレットh1_悪い大人の契約.txt.toml` (03_Paulette) — 21 dòng sửa

**Ngoài phạm vi (không đụng):** file 03_Paulette / 06_Kisaki tuyến chính (稀咲01/02/03, 稀咲h1/h2/h3, グランドリライト06_稀咲, lr_日々姫10...) thuộc batch U7a; file 09_Grand thuộc batch khác. 11_Other: KHÔNG có dòng nào của Kisaki (đã kiểm chứng toàn folder — 0 dòng Character 稀咲), nên không có file 11_Other nào trong đợt này.

**Tổng cộng đợt này: 51 dòng sửa (60 lần xuất hiện "anh Soutetsu"), 4 file.**

## §1. Phương pháp

1. Liệt kê bằng script trên CSV3 good set (87.833 dòng — đã loại 3.898 dòng stale theo `dual-csv-sets.md`): mọi dòng trong 6 file phạm vi mà Character = 稀咲 và giá trị HIỆN TẠI chứa "anh Soutetsu" (không phân biệt hoa/thường). Được **62 dòng ứng viên**.
2. Giá trị hiện tại (old_vn) tính theo quy ước: fix unification đã gộp > fix moan > fix audit > VN CSV3. Map xây bằng script: audit 9.146 cặp (1 file không resolve được — `audit-nagifukami07-bunki-sentakushi-wrong.json`, 1 dòng, ngoài phạm vi), moan 1.516 cặp, unification đã gộp 998 cặp (tính tới lúc chạy). Nguồn old_vn của 51 dòng sửa: CSV3 42, moan 5, audit 1, unification đã gộp 3 (tsuika02 1629 — fix T56; lr_稀咲ポーレットh1 1470 — fix M16; 1513 — fix M1 — 2 dòng GHÉP bởi coordinator 22/11, xem ghi chú §8).
3. Đọc từng dòng ứng viên: JP (+TW) + 3–5 dòng kề để xác định người nói (Character 稀咲) và NGƯỜI NGHE. Nguyên tắc áp dụng (theo task): SỬA khi Soutetsu là người nghe (hô gọi, hỏi trực tiếp, sở hữu của người nghe, nói với anh về chính anh); GIỮ khi là ngôi ba (Kisaki nói VỀ Soutetsu với người khác — Paulette/Suika/Khương — hoặc nêu tên cặp "Soutetsu và Paulette" trong điều khoản).
4. JP thắng TW. **Cột TW của lr稀咲追加01 đã SHIFT (lệch dòng) — bằng chứng TW từ file này là VOID**; 3 dòng tsuika01 quyết theo JP + dòng kề. TW trong bảng dưới vẫn ghi đúng giá trị CSV3 (có dấu †) để đối chiếu, không dùng làm bằng chứng. Không dòng nào thiếu khỏi CSV3 (0 dòng lấy từ TOML-2).
5. Fix = old_vn thay đúng chuỗi "anh Soutetsu"/"Anh Soutetsu" → "Soutetsu", giữ nguyên phần còn lại (kể cả đại từ "anh" trần — đó là mục P6, không đụng). Dạng tách tên "Anh, Soutetsu" / "Anh Sou, tetsu" (JP そう、てつ tách âm) KHÔNG chứa chuỗi "anh Soutetsu" nên không sửa theo chữ của task — ghi cờ F-P4-1 (§4).
6. Trùng lặp với batch đã gộp: chỉ 1 dòng (tsuika02 1629, T56) — old_vn đã lấy giá trị sau T56, fix đợt này chồng lên trên, không đè. 0 dòng trùng với U1/U2/U6/U10.

## §2. Bảng sửa (51 dòng)

Cột TW có † = TW CSV3 đã SHIFT (tsuika01), không dùng làm bằng chứng.

### lr_稀咲ポーレットh1_悪い大人の契約.txt.toml

| Key | JP | TW | old_vn | Fix | Lý do |
|---|---|---|---|---|---|
| 1000 | 「……話すこともダルそうだね。いまは双鉄。\n何も考えずに休むといいよ」 | 「……看來連說話都很累吧。現在，雙鐵。什麼都別想，好好休息吧」 | 「……Có vẻ anh mệt đến mức không buồn nói chuyện nữa rồi. Bây giờ anh Soutetsu\nhãy nghỉ ngơi đi, đừng suy nghĩ gì cả.」 | 「……Có vẻ anh mệt đến mức không buồn nói chuyện nữa rồi. Bây giờ Soutetsu\nhãy nghỉ ngơi đi, đừng suy nghĩ gì cả.」 | P4 — trực tiếp với Soutetsu ("いまは双鉄。何も考えずに休むといいよ"). "Có vẻ anh mệt" (đại từ trần) KHÔNG đụng. |
| 1442 | 「きゃふっ！！！？　あ―やだっ―双鉄っ―んっ。\nそんな―急に―急に―こんなのっ―」 | 「呀嗚！！！？啊——不要——雙鐵——嗯。不要——太突然——突然——這樣」 | 「Kyafu!!!? A——đừng——anh Soutetsu——ưm. Thế này——đột nhiên——đột nhiên——thế này——」 | 「Kyafu!!!? A——đừng——Soutetsu——ưm. Thế này——đột nhiên——đột nhiên——thế này——」 | P4 — hô gọi ("あ―やだっ―双鉄っ"). old_vn = fix moan. |
| 1456 | 「フフッ―おつかれさま、双鉄」 | 「呵呵——辛苦了，雙鐵」 | 「Fufu——anh vất vả rồi, anh Soutetsu.」 | 「Fufu——anh vất vả rồi, Soutetsu.」 | P4 — trực tiếp với Soutetsu ("おつかれさま、双鉄"). |
| 1459 | 「ふふっ、そんなに真剣な瞳でお礼をいわれるなんて。\nポーレットは、よほど双鉄のおちんちんが欲しいんだね」 | 「呵呵，你居然會眼神這麼認真地向我道謝。看來波萊特真的非常想要雙鐵的小雞雞」 | 「Fufu, không ngờ lại được cảm ơn bằng ánh mắt nghiêm túc thế kia.\nCó vẻ Paulette rất khao khát dương vật của anh Soutetsu nhỉ.」 | 「Fufu, không ngờ lại được cảm ơn bằng ánh mắt nghiêm túc thế kia.\nCó vẻ Paulette rất khao khát dương vật của Soutetsu nhỉ.」 | P4 — sở hữu của người nghe ("双鉄のおちんちん"); cô nói với Soutetsu ("được cảm ơn bằng ánh mắt nghiêm túc" = Soutetsu cảm ơn cô). |
| 1470 | 「ふぁああああん！　双鉄、ね？　そうてつぅ―あっ、\nボク、ね？　ボクっ―ボク、もう、もう、もうっ！」 | 「呼啊啊啊啊啊！　雙鐵……　雙鐵——啊、我，啊……　我——我、已經、已經、已經」 | 「Faaaaan! Anh Soutetsu, nè? Anh Soutetsu——a, em, nè? Em——em, sắp, sắp, sắp rồi!」 | 「Faaaaan! Soutetsu, nè? Soutetsu——a, em, nè? Em——em, sắp, sắp, sắp rồi!」 | P4 — hô gọi, ×2 ("双鉄、ね？ そうてつぅ"). old_vn = fix moan. |
| 1475 | 「ふぁっ！　あっ！　あっ！　あっ！　あっ！　あっ！\nあっ！　あっ！　そう、てつ―双鉄ぅ―んっ！」 | 「呼啊！　啊！　啊！　啊！　啊！　啊！啊！　啊！　雙、鐵——雙鐵——嗯！」 | 「Fa! A! A! A! A! A! A! A! Anh, Soutetsu——anh Soutetsu——ưm!」 | 「Fa! A! A! A! A! A! A! A! Anh, Soutetsu——Soutetsu——ưm!」 | P4 — hô gọi ("そう、てつ―双鉄ぅ"). Chỉ sửa chuỗi đúng "anh Soutetsu"; dạng tách "Anh, Soutetsu" giữ nguyên, xem cờ F-P4-1. |
| 1478 | 「ふあっ！　双鉄！　そうてつ、そうてつぅっ―」 | 「呼啊！　雙鐵！　雙鐵、雙鐵——」 | 「Fua! Anh Soutetsu! Anh Soutetsu, anh Soutetsu——」 | 「Fua! Soutetsu! Soutetsu, Soutetsu——」 | P4 — hô gọi, ×3 ("双鉄！ そうてつ、そうてつぅっ"). old_vn = fix moan. |
| 1513 | 「はぁ―んっ―ふぁ―あ―。そう、てつ―\n双鉄―ふふっ―よく頑張ったね。双鉄、おいで？」 | 「哈——嗯——呼啊——啊——雙、鐵——雙鐵——呼呼——你真的很努力。雙鐵，過來吧？」 | 「Ha——ưm——Fa——a——. Anh, Soutetsu—— Anh Soutetsu——fufu——anh đã cố gắng lắm rồi. Lại đây nào, anh Soutetsu?」 | 「Ha——ưm——Fa——a——. Anh, Soutetsu—— Soutetsu——fufu——anh đã cố gắng lắm rồi. Lại đây nào, Soutetsu?」 | P4 — hô gọi, ×2 chuỗi đúng ("双鉄―…双鉄、おいで？"). Dạng tách "Anh, Soutetsu" giữ nguyên, xem cờ F-P4-1. old_vn = fix audit. |
| 1534 | 「あ―らめっ！　これっ！　くるっ！　きちゃうっ！\nすごいのっ！　そう、てつっ―そうてつぅ！！！」 | 「啊——不行了！　我！　要來了！　要來了！好厲害！　雙、鐵——雙鐵！！！」 | 「A——không được! Thế này! Đến mất! Đến mất thôi!\nTuyệt quá! Anh, Soutetsu——anh Soutetsu!!!」 | 「A——không được! Thế này! Đến mất! Đến mất thôi!\nTuyệt quá! Anh, Soutetsu——Soutetsu!!!」 | P4 — hô gọi ("そう、てつっ―そうてつぅ"). Chỉ sửa chuỗi đúng "anh Soutetsu"; dạng tách "Anh, Soutetsu" giữ nguyên, xem cờ F-P4-1. JP không có 双鉄 (dùng そうてつ tách âm) nhưng đối tượng là Soutetsu, TW "雙鐵" xác nhận. |
| 1542 | 「ぁっ―んふ、ふっ―ありがと、双鉄。ボクとも\nちゃんと―ちゃんと―セックス、してくれて」 | 「啊——嗯呼、呼——謝謝、雙鐵。謝謝你能和我——好好——做愛」 | 「A——ưm fu, fu——cảm ơn anh, anh Soutetsu. Vì đã\nđàng hoàng——đàng hoàng——làm tình, với em nữa.」 | 「A——ưm fu, fu——cảm ơn anh, Soutetsu. Vì đã\nđàng hoàng——đàng hoàng——làm tình, với em nữa.」 | P4 — cảm ơn trực tiếp Soutetsu ("ありがと、双鉄"). |
| 1573 | 「かはっ！　ちょっ―双鉄っ―んっ―\nこんな―いき、なりっ―あんっ―あっ」 | 「啊！　等——雙鐵——嗯——不要——太突、然了——啊嗯——啊」 | 「A! Khoan——anh Soutetsu——ưm——\nthế này——đột, ngột quá——a ưm——a」 | 「A! Khoan——Soutetsu——ưm——\nthế này——đột, ngột quá——a ưm——a」 | P4 — hô gọi ("双鉄っ"). |
| 1601 | 「んっ―はっ！　あっ！　双鉄、双鉄―ボクは―\n次で―二番目で、今日は、いいから―ポーレットを」 | 「嗯——哈！　啊！　雙鐵，雙鐵——我是——下一個，今天，就不用了——波萊特才」 | 「Ưm——ha! A! Anh Soutetsu, anh Soutetsu——em thì——\nlần sau——hôm nay, em là người thứ hai, cũng được——hãy làm với Paulette đi.」 | 「Ưm——ha! A! Soutetsu, Soutetsu——em thì——\nlần sau——hôm nay, em là người thứ hai, cũng được——hãy làm với Paulette đi.」 | P4 — hô gọi, ×2 ("双鉄、双鉄"). |
| 1604 | 「ん……ふふっ―どおお、双鉄？　おまんこの感触―\nんっ―ボクと、ポーレットで、結構違う？」 | 「嗯……呼呼——怎麼樣，雙鐵？？　小穴的觸感——嗯——我和波萊特的小穴，很不一樣嗎？」 | 「Ưm……fufu——sao nào, anh Soutetsu? Cảm giác của âm đạo——\nưm——của em, và của Paulette, có khác nhau nhiều không?」 | 「Ưm……fufu——sao nào, Soutetsu? Cảm giác của âm đạo——\nưm——của em, và của Paulette, có khác nhau nhiều không?」 | P4 — hỏi trực tiếp Soutetsu ("どおお、双鉄？"). |
| 1606 | 「うん。―来て？　双鉄」 | 「嗯。——來吧？　雙鐵」 | 「Ừm. ——Vào đi? Anh Soutetsu.」 | 「Ừm. ——Vào đi? Soutetsu.」 | P4 — hô gọi ("来て？ 双鉄"). |
| 1673 | 「ボク……も、だ―双鉄……んっ―はっ―あっ―\n今日は―なん、だかっ―いっつも、より、もっ―」 | 「我……也、是——雙鐵……嗯——哈——啊——今天——總、覺得——比平時、更——」 | 「Em……cũng, vậy——anh Soutetsu……ưm——ha——a——\nHôm nay——sao, nhỉ——cảm giác, hơn hẳn, mọi khi——」 | 「Em……cũng, vậy——Soutetsu……ưm——ha——a——\nHôm nay——sao, nhỉ——cảm giác, hơn hẳn, mọi khi——」 | P4 — trực tiếp với Soutetsu ("ボク……も、だ―双鉄……"). |
| 1800 | 「ボクに責任を押し付けるようにもとれる言動を、\nボクの大好きな双鉄にされるのは少し、悲しいかな」 | 「看到我最喜歡的雙鐵，只想著把責任推給我的言行舉止，是不是有點悲哀呢」 | 「Thấy người em yêu thương nhất là anh Soutetsu lại có những lời nói và hành động\nnhư muốn đùn đẩy trách nhiệm cho em, em thấy hơi buồn đấy.」 | 「Thấy người em yêu thương nhất là Soutetsu lại có những lời nói và hành động\nnhư muốn đùn đẩy trách nhiệm cho em, em thấy hơi buồn đấy.」 | P4 — nói trực tiếp VỚI Soutetsu về hành vi của chính anh ("ボクの大好きな双鉄にされるのは少し、悲しいかな" — bị động される, tác nhân là Soutetsu người nghe). Đối chiếu 1802 (nói với Paulette) thì GIỮ. |
| 1814 | 「はじめてのときに膣内で感じるとかって無理だから。\nね？　双鉄―クリトリス、もしも出来たら」 | 「第一次的時候陰道是很難有感覺的。對吧？　雙鐵——如果可以的話，刺激的陰蒂」 | 「Lần đầu tiên mà đòi có cảm giác bên trong âm đạo thì khó lắm.\nNè? Anh Soutetsu——nếu được thì kích thích âm vật đi.」 | 「Lần đầu tiên mà đòi có cảm giác bên trong âm đạo thì khó lắm.\nNè? Soutetsu——nếu được thì kích thích âm vật đi.」 | P4 — hô gọi + nhờ trực tiếp Soutetsu ("ね？ 双鉄―クリトリス、もしも出来たら"). |
| 1815 | 「だって？　それで、双鉄はどう思うの？\n何を望むの？　今のポーレットの言葉を聞いて」 | 「聽到了嗎？　那麼，雙鐵怎麼想？你想要怎麼辦？　聽到剛剛波萊特說的話」 | 「Nghe thấy chưa? Vậy anh Soutetsu nghĩ sao?\nAnh muốn thế nào? Sau khi nghe những lời vừa rồi của Paulette.」 | 「Nghe thấy chưa? Vậy Soutetsu nghĩ sao?\nAnh muốn thế nào? Sau khi nghe những lời vừa rồi của Paulette.」 | P4 — hỏi trực tiếp Soutetsu ("それで、双鉄はどう思うの？"). |
| 1864 | 「ボクはね？　双鉄」 | 「那我呢？　雙鐵」 | 「Em thì sao? Anh Soutetsu.」 | 「Em thì sao? Soutetsu.」 | P4 — hô gọi ("ボクはね？ 双鉄", cùng mẫu "X? 双鉄" như 1687/1218/1606). |
| 1876 | 「双鉄は―」 | 「雙鐵——」 | 「Anh Soutetsu thì——」 | 「Soutetsu thì——」 | P4 — "双鉄は―" cụt, cùng mạch gọi Soutetsu với 1877 ("そうてつ、そうてつぅ―ね？ まだ？"). |
| 1877 | 「そうてつ、そうてつぅ―ね？　まだ？　まだ、なのっ\n―あっ！　ボク―もう―ボク、がまん―んっ！」 | 「雙鐵、雙鐵——？　還沒好嗎？　還沒、好嗎？——啊！　我——已經——我忍不、住了！」 | 「Anh Soutetsu, anh Soutetsu——nè? Chưa sao? Vẫn chưa, sao\n——A! Em——sắp——em, không nhịn được——ưm!」 | 「Soutetsu, Soutetsu——nè? Chưa sao? Vẫn chưa, sao\n——A! Em——sắp——em, không nhịn được——ưm!」 | P4 — hô gọi, ×2 ("そうてつ、そうてつぅ"). JP không có 双鉄 (dùng そうてつ tách âm) nhưng đối tượng là Soutetsu, TW "雙鐵、雙鐵" xác nhận. |

### lr稀咲追加01_仲国視察の誘い.txt.toml

| Key | JP | TW | old_vn | Fix | Lý do |
|---|---|---|---|---|---|
| 1488 | 「準備のほんの一部分。双鉄は閃くタイプじゃないか。\n予想外の事態を、むしろ発展のチャンスにできる」 | 「竟是這樣的準備啊」 † | 「Chỉ là một phần nhỏ của sự chuẩn bị thôi. Anh Soutetsu thuộc tuýp người hay nảy ra ý tưởng bất chợt mà.\nAnh có thể biến những tình huống ngoài dự kiến thành cơ hội phát triển.」 | 「Chỉ là một phần nhỏ của sự chuẩn bị thôi. Soutetsu thuộc tuýp người hay nảy ra ý tưởng bất chợt mà.\nAnh có thể biến những tình huống ngoài dự kiến thành cơ hội phát triển.」 | P4 — trực tiếp với Soutetsu (câu sau "Anh có thể biến..." là ngôi 2); quyết định 22/11 ~03:32 liệt kê đích danh 1488/1687/1783. TW cột đã SHIFT (xem §1) nên chỉ dùng JP + dòng kề. |
| 1687 | 「なぁに？　双鉄」 | 剛想盡情擁抱稀咲，轉念一想現在在哪裡，就停了下來。 † | 「Sao vậy? Anh Soutetsu.」 | 「Sao vậy? Soutetsu.」 | P4 — hô gọi trực tiếp ("なぁに？ 双鉄"). |
| 1783 | 「けど、姜さんが“ボクにあうやり方”を教えてくれた。\nその一番の成果物なら、キミだよ？　双鉄」 | 我清晰地感受到了稀咲的心跳。不得不承認，稀咲的雙峰又有所成長。 † | 「Nhưng, cô Khương đã dạy tôi 'cách làm phù hợp với bản thân'.\nThành quả lớn nhất của điều đó, chính là anh đấy? Anh Soutetsu.」 | 「Nhưng, cô Khương đã dạy tôi 'cách làm phù hợp với bản thân'.\nThành quả lớn nhất của điều đó, chính là anh đấy? Soutetsu.」 | P4 — trực tiếp với Soutetsu (キミだよ？ 双鉄). "anh đấy" (キミ) là mục P6, KHÔNG đụng. |

### lr稀咲追加02_仲国視察.txt.toml

| Key | JP | TW | old_vn | Fix | Lý do |
|---|---|---|---|---|---|
| 1084 | 「ニワトリタマゴになってるよ？　双鉄。\n建築限界が何かを、ボクに説明してくれてるんだよね」 | 「先有雞還是先有蛋囉？雙鐵。應該先給我解釋一下建築限界是什麼才對吧」 | 「Anh đang bị vòng luẩn quẩn 'con gà hay quả trứng có trước' rồi đấy? Anh Soutetsu.\nAnh đang định giải thích cho tôi giới hạn kiến trúc là gì cơ mà.」 | 「Anh đang bị vòng luẩn quẩn 'con gà hay quả trứng có trước' rồi đấy? Soutetsu.\nAnh đang định giải thích cho tôi giới hạn kiến trúc là gì cơ mà.」 | P4 — trực tiếp với Soutetsu (hô gọi "双鉄" + "ボクに説明してくれてるんだよね"). |
| 1258 | 「過去のボクなら、どんなに綺麗な列車がデザインされた\nとしても、乗りたいとは思わなかったかな。双鉄は？」 | 「如果在以前，不管列車的設計再優美，我也不會萌生想要乘坐的念頭，雙鐵你呢？」 | 「Nếu là tôi của quá khứ, dù có thiết kế ra một chuyến tàu đẹp đến đâu,\nchắc tôi cũng không muốn đi đâu. Còn anh Soutetsu thì sao?」 | 「Nếu là tôi của quá khứ, dù có thiết kế ra một chuyến tàu đẹp đến đâu,\nchắc tôi cũng không muốn đi đâu. Còn Soutetsu thì sao?」 | P4 — hỏi trực tiếp Soutetsu ("双鉄は？"). |
| 1353 | 「っていうか、双鉄？　なんだい、その……\nオイランシャ？　っていうのは」 | 「所以說，雙鐵？那個……是叫花魁車？是什麼啊」 | 「Mà này, anh Soutetsu? Cái đó là gì vậy……\nXe Oiran? ấy.」 | 「Mà này, Soutetsu? Cái đó là gì vậy……\nXe Oiran? ấy.」 | P4 — hỏi trực tiếp Soutetsu ("双鉄？"). |
| 1629 | 「なら僕たちが次に視察するべきは、\n『仲国国鉄の現状そのもの』かな？　どう思う？　双鉄」 | 「那我們接下來該考察的，就是“仲國國鐵的現狀本身”了吧？你覺得呢，雙鐵？」 | 「Vậy thì thứ tiếp theo chúng ta cần khảo sát,\ncó lẽ là 'chính hiện trạng của Đường sắt Quốc gia Trung Quốc' nhỉ? Anh thấy sao? Anh Soutetsu.」 | 「Vậy thì thứ tiếp theo chúng ta cần khảo sát,\ncó lẽ là 'chính hiện trạng của Đường sắt Quốc gia Trung Quốc' nhỉ? Anh thấy sao? Soutetsu.」 | P4 — hỏi trực tiếp Soutetsu ("どう思う？ 双鉄"). old_vn = fix T56 đã gộp (Trọng Quốc→Trung Quốc); chỉ đổi phần "anh Soutetsu". |

### lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml

| Key | JP | TW | old_vn | Fix | Lý do |
|---|---|---|---|---|---|
| 811 | 「……ううん。からかわれてるわけじゃないよね。\nだって双鉄――そういうの、全然知識なかったんだし」 | 「……嗯。看來你不是在開我的玩笑。畢竟你——完全沒有這方面的知識」 | 「……Ừm. Anh không phải đang trêu tôi đâu nhỉ.\nTại vì anh Soutetsu——hoàn toàn không có kiến thức về mấy chuyện đó mà.」 | 「……Ừm. Anh không phải đang trêu tôi đâu nhỉ.\nTại vì Soutetsu——hoàn toàn không có kiến thức về mấy chuyện đó mà.」 | P4 — nói trực tiếp với Soutetsu về chính anh ("だって双鉄――そういうの、全然知識なかったんだし"). |
| 1059 | 「もっと！　してっ！　リズム、このままっ――\nボクの、ヴァギナっ――双鉄の――ペニス、でっ！！」 | 「再來！繼續！保持這個節奏——用你的陰莖——插入我的陰道裡！！」 | 「Làm! Nữa đi! Cứ giữ nguyên, nhịp điệu này——\nÂm đạo, của tôi——Bằng dương vật——của anh Soutetsu!!」 | 「Làm! Nữa đi! Cứ giữ nguyên, nhịp điệu này——\nÂm đạo, của tôi——Bằng dương vật——của Soutetsu!!」 | P4 — sở hữu của người nghe ("双鉄のペニス", nói với Soutetsu). |
| 1077 | 「やぁあっ――双鉄――ボク。こんな格好――\n恥ずかしいっ――マンぐりがえし――とかっ――」 | 「呀啊——雙鐵——我、這個姿勢——好害羞——竟然是——打樁機姿勢——」 | 「Yaaa——Anh Soutetsu——Tôi. Tư thế này——\nXấu hổ lắm——Giống tư thế đóng cọc——quá——」 | 「Yaaa——Soutetsu——Tôi. Tư thế này——\nXấu hổ lắm——Giống tư thế đóng cọc——quá——」 | P4 — hô gọi giữa lúc rên ("双鉄"). old_vn = fix audit. |
| 1087 | 「はぁっ――はあっ――はあっ――はあっ――。\nん……うん。わかったよ。双鉄」 | 「呼啊——呼啊——呼啊——呼啊。嗯……嗯，好啦，雙鐵」 | 「Haa——Haa——Haa——Haa——.\nƯm…… Ừm. Tôi hiểu rồi. Anh Soutetsu.」 | 「Haa——Haa——Haa——Haa——.\nƯm…… Ừm. Tôi hiểu rồi. Soutetsu.」 | P4 — hô gọi ("わかったよ。双鉄"). |
| 1104 | 「あっ――んっ――ふ、ぁ――ごめん、ごめんね、双鉄。\nだよね――これ、洗いっこ……だった、ね――んっ」 | 「啊——嗯——呼、啊——對不起、對不起，雙鐵。你說的對——我們是在互相洗來著——嗯」 | 「A——Ưm——Fu, a——Xin lỗi, xin lỗi anh nhé, anh Soutetsu.\nĐúng nhỉ——Chúng ta đang, tắm rửa cho nhau…… mà, nhỉ——Ưm.」 | 「A——Ưm——Fu, a——Xin lỗi, xin lỗi anh nhé, Soutetsu.\nĐúng nhỉ——Chúng ta đang, tắm rửa cho nhau…… mà, nhỉ——Ưm.」 | P4 — xin lỗi trực tiếp Soutetsu ("ごめん、ごめんね、双鉄"). "xin lỗi anh nhé" (đại từ "anh" trần) KHÔNG đụng. |
| 1112 | 「あ……ふっ――ふあっ――ね、双鉄――乳首――んっ\n――乳首……それ、ね？　もっと――もっと、して？」 | 「啊……呼——呼啊——我說，雙鐵——乳頭——嗯……那個，你多摸一摸——好嗎」 | 「A……Fu――Fua――Này, anh Soutetsu――Nhũ hoa――Ưm\n――Nhũ hoa……Cái đó, nhé? Thêm nữa――Làm thêm nữa đi?」 | 「A……Fu――Fua――Này, Soutetsu――Nhũ hoa――Ưm\n――Nhũ hoa……Cái đó, nhé? Thêm nữa――Làm thêm nữa đi?」 | P4 — hô gọi ("ね、双鉄"). old_vn = fix moan. |
| 1114 | 「あ……はっ――ん。おっぱい――\n双鉄の手、ぬらぬらで――んうっ！！」 | 「啊……哈——嗯。胸部——你的手——滑滑的——嗯！！」 | 「A……Hà――Ưm. Ngực――\nTay của anh Soutetsu, trơn tuột――Nu!!」 | 「A……Hà――Ưm. Ngực――\nTay của Soutetsu, trơn tuột――Nu!!」 | P4 — sở hữu của người nghe ("双鉄の手"). old_vn = fix moan. |
| 1132 | 「あっ！　あっ！！！　双鉄っ！！！！\nそれっ！　それっ！　それっ！　しょれええええっ！」 | 「啊！啊！！！雙鐵！！！！就是這樣！就是這樣！就是這樣！就是這樣！」 | 「A! A!!! Anh Soutetsu!!!!\nĐúng rồi! Đúng rồi! Đúng rồi! Đúng rồi ôi ôi ôi!」 | 「A! A!!! Soutetsu!!!!\nĐúng rồi! Đúng rồi! Đúng rồi! Đúng rồi ôi ôi ôi!」 | P4 — hô gọi ("双鉄っ！！！！"). |
| 1149 | 「うん……っ――あったかくなってきた。\nそれに――双鉄もあっという間に熱くなった」 | 「嗯……啊——暖和起來了。而且——你身體也這麼燙了」 | 「Ưm……――Bắt đầu ấm lên rồi.\nHơn nữa――anh Soutetsu cũng nóng bừng lên trong chớp mắt kìa.」 | 「Ưm……――Bắt đầu ấm lên rồi.\nHơn nữa――Soutetsu cũng nóng bừng lên trong chớp mắt kìa.」 | P4 — nói trực tiếp với Soutetsu về cơ thể anh ("双鉄もあっという間に熱くなった"). |
| 1165 | 「んんっ！　――だめっ――だよ、双鉄っ――\n双鉄が動いたら――ボクっ――すべっちゃう――からっ」 | 「嗯嗯！——不行啦——雙鐵——你要是動的話——我要滑下去了」 | 「Ưm! ——Không được——đâu, anh Soutetsu——\nNếu anh Soutetsu mà cử động——tôi——sẽ bị trượt mất——đấy.」 | 「Ưm! ——Không được——đâu, Soutetsu——\nNếu Soutetsu mà cử động——tôi——sẽ bị trượt mất——đấy.」 | P4 — trực tiếp với Soutetsu, ×2 ("だめっ――だよ、双鉄っ――双鉄が動いたら"). |
| 1167 | 「うん、そうだよ。ボクいつだって頑張ってる。\n今も、そう――双鉄とボクの、赤ちゃん、ほしくて」 | 「嗯，是啊。我做事總是非常努力。現在也一樣——我想要一個、你和我的小寶寶」 | 「Ừm, đúng vậy đấy. Lúc nào tôi cũng cố gắng hết sức.\nBây giờ, cũng vậy——Tôi muốn có, em bé, của anh Soutetsu và tôi.」 | 「Ừm, đúng vậy đấy. Lúc nào tôi cũng cố gắng hết sức.\nBây giờ, cũng vậy——Tôi muốn có, em bé, của Soutetsu và tôi.」 | P4 — sở hữu chung với người nghe ("双鉄とボクの、赤ちゃん"). |
| 1170 | 「ふふっ、双鉄は真面目だね。\nラブローションで食レポする人、珍しいんじゃないかな」 | 「嘻嘻，你可真是一本正經。沒有多少人會對愛情潤滑液做美食評論吧」 | 「Fufu, anh Soutetsu nghiêm túc thật đấy.\nNgười đi review ẩm thực bằng Love Lotion, chắc là hiếm lắm đấy.」 | 「Fufu, Soutetsu nghiêm túc thật đấy.\nNgười đi review ẩm thực bằng Love Lotion, chắc là hiếm lắm đấy.」 | P4 — trực tiếp với Soutetsu ("双鉄は真面目だね"). |
| 1173 | 「んふふっ――これ、なら――一緒に――洗える――\n双鉄の――ペニ、スと――僕の――ヴァギナ、をっ――」 | 「嘿嘿——這樣的話——就能一起洗了。你的陰莖——還有——我的、陰道」 | 「Nfufu——Nếu thế này——thì có thể rửa——cùng nhau rồi——\nDương vật——của anh Soutetsu——và âm đạo——của tôi——」 | 「Nfufu——Nếu thế này——thì có thể rửa——cùng nhau rồi——\nDương vật——của Soutetsu——và âm đạo——của tôi——」 | P4 — sở hữu của người nghe ("双鉄のペニス"). |
| 1175 | 「ふふっ。双鉄もアレに気づいてたんだ」 | 「嘿嘿，你也發現了啊」 | 「Fufu. Anh Soutetsu cũng nhận ra cái đó rồi à.」 | 「Fufu. Soutetsu cũng nhận ra cái đó rồi à.」 | P4 — trực tiếp với Soutetsu ("双鉄もアレに気づいてたんだ"). |
| 1195 | 「みたい――だね――そう、てつの――ペニス――すごい。\n完全にガチガチで――ふ――あっ――触れる、だけでも」 | 「好像——是這樣的——雙鐵你的——陰莖——好厲害。已經硬得不行了——呼——啊——只是這樣輕輕撫摸——」 | 「Có vẻ——như vậy nhỉ——Dương vật——của anh Soutetsu——tuyệt quá.\nCứng ngắc hoàn toàn rồi——Fu——A——Chỉ cần, chạm vào thôi.」 | 「Có vẻ——như vậy nhỉ——Dương vật——của Soutetsu——tuyệt quá.\nCứng ngắc hoàn toàn rồi——Fu——A——Chỉ cần, chạm vào thôi.」 | P4 — sở hữu của người nghe; JP dùng てつ (rút gọn của 双鉄) nhưng đối tượng là Soutetsu, TW "雙鐵你的陰莖" xác nhận. |
| 1200 | 「ね？　双鉄――双鉄は、どう？　気持ち、いい？――ん、おててと――ローション――ぬるぬる――こしゅこしゅ」 | 「對吧？你覺得——怎麼樣？舒服嗎？嗯、用手——還有潤滑液——濕濕的——搓來搓去」 | 「Này? Anh Soutetsu——Anh Soutetsu, thấy sao? Sướng, không? ——Ưm, dùng tay——với lotion——trơn tuột——cọ xát cọ xát.」 | 「Này? Soutetsu——Soutetsu, thấy sao? Sướng, không? ——Ưm, dùng tay——với lotion——trơn tuột——cọ xát cọ xát.」 | P4 — hỏi trực tiếp Soutetsu, ×2 ("双鉄――双鉄は、どう？"). |
| 1218 | 「なんだい？　双鉄」 | 「怎麼了？雙鐵」 | 「Gì vậy? Anh Soutetsu.」 | 「Gì vậy? Soutetsu.」 | P4 — hô gọi ("なんだい？ 双鉄"). |
| 1232 | 「ボク……ね？　ずっと、思ってるんだ。\n双鉄との赤ちゃんが欲しい、って」 | 「我呢……一直在想……想要一個我們的孩子」 | 「Tôi…… nhé? Lúc nào cũng, nghĩ rằng.\nMuốn có em bé với anh Soutetsu.」 | 「Tôi…… nhé? Lúc nào cũng, nghĩ rằng.\nMuốn có em bé với Soutetsu.」 | P4 — trực tiếp với Soutetsu ("双鉄との赤ちゃんが欲しい"). |
| 1234 | 「双鉄と……プライベートの、話――するように、なって。\nだんだん、ボク――双鉄のこと――ほしいって、思って」 | 「我和你……開始聊起私人生活的時候。我就漸漸地……想要你了」 | 「Kể từ khi…… bắt đầu nói chuyện, riêng tư——với anh Soutetsu.\nDần dần, tôi——đã nghĩ rằng——mình muốn, anh Soutetsu.」 | 「Kể từ khi…… bắt đầu nói chuyện, riêng tư——với Soutetsu.\nDần dần, tôi——đã nghĩ rằng——mình muốn, Soutetsu.」 | P4 — trực tiếp với Soutetsu, ×2 ("双鉄と……双鉄のこと――ほしい"). |
| 1307 | 「おっぱいも――乳首――も……双鉄――んっ――あ、\nすごく――大事に――甘く――愛して、くれる――よね」 | 「胸部——還有乳頭——你都……嗯——啊，非常愛惜——非常疼愛——」 | 「Cả ngực——lẫn đầu nhũ hoa——cũng…… anh Soutetsu——ưm——a,\nanh đều rất——nâng niu——ngọt ngào——yêu thương, chúng——nhỉ.」 | 「Cả ngực——lẫn đầu nhũ hoa——cũng…… Soutetsu——ưm——a,\nanh đều rất——nâng niu——ngọt ngào——yêu thương, chúng——nhỉ.」 | P4 — trực tiếp với Soutetsu ("双鉄――んっ――あ、すごく――大事に――甘く――愛して、くれる"). "anh đều rất" (đại từ trần) KHÔNG đụng. |
| 1328 | 「せっかくあったまったのに、湯冷めするのもイヤだし。\nね、双鉄。体温、ちょっともらうね？　ん……」 | 「身體好不容易暖起來了，受涼就不好了。那個，雙鐵，我借你一點體溫。嗯……」 | 「Mất công làm ấm người rồi, tôi không muốn bị lạnh lại đâu.\nNày, anh Soutetsu. Cho tôi xin chút thân nhiệt nhé? Ưm……」 | 「Mất công làm ấm người rồi, tôi không muốn bị lạnh lại đâu.\nNày, Soutetsu. Cho tôi xin chút thân nhiệt nhé? Ưm……」 | P4 — hô gọi ("ね、双鉄"). |
| 1349 | 「ダメ……なのっ――双鉄。だって――体位。\nこの体位だと……んっ――精液、こぼれ、やすいから」 | 「這樣……不行——雙鐵。因為——體位。這個體位的話……嗯——精液容易漏出來」 | 「Không được…… đâu——Anh Soutetsu. Tại vì——tư thế.\nTư thế này thì…… ưm——tinh dịch, rất dễ, bị tràn ra ngoài.」 | 「Không được…… đâu——Soutetsu. Tại vì——tư thế.\nTư thế này thì…… ưm——tinh dịch, rất dễ, bị tràn ra ngoài.」 | P4 — hô gọi ("ダメ……なのっ――双鉄"). |
| 1361 | 「双鉄――そう、てつ――ね、ボク――ボク――もうっ、\nもう――ねっ――イキ――そうっ――んっ――ぁあっ」 | 「雙鐵——雙鐵——我——我已經——嗯——要洩了——啊」 | 「Anh Soutetsu——Anh Sou, tetsu——Này, tôi——tôi——sắp,\nsắp——này——lên đỉnh——rồi——ưm——aa.」 | 「Soutetsu——Anh Sou, tetsu——Này, tôi——tôi——sắp,\nsắp——này——lên đỉnh——rồi——ưm——aa.」 | P4 — hô gọi ("双鉄――そう、てつ"). Chỉ sửa đúng chuỗi "Anh Soutetsu"; dạng tách "Anh Sou, tetsu" giữ nguyên, xem cờ F-P4-1. |

## §3. Giữ nguyên (không sửa)

### §3a. Ứng viên Kisaki nhưng ngôi ba — 11 dòng

| File | Key | Lý do giữ |
|---|---|---|
| lr稀咲追加02_仲国視察.txt.toml | 1233 | ngôi ba — Kisaki nói với Suika (từ chối được hộ tống: "Vì đã có anh Soutetsu hộ tống tôi rồi mà"); Soutetsu không phải người nghe, JP 双鉄が…エスコートしてくれる (nói về Soutetsu với người khác). |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1389 | ngôi ba — Kisaki nói với Paulette ("Cô cứ hỏi trực tiếp đi"); "không biết tình trạng thực tế của anh Soutetsu" là bàn về Soutetsu với Paulette. |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1632 | ngôi ba — Kisaki nói với Paulette ("cô có muốn tận mắt chứng kiến cảnh anh Soutetsu xuất tinh dưới bàn tay chúng ta không"); Soutetsu là đối tượng được bàn tới. |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1722 | ngôi ba (ranh giới) — 1716–1720 đều hướng về Paulette; "ふたりで―双鉄、とっ" = kể với Paulette về điều cô và Soutetsu đã tìm ra cùng nhau, "với anh Soutetsu" là nhắc tới Soutetsu với Paulette. Giữ theo nguyên tắc "không đụng ngôi ba"; nếu coordinator đọc người nghe là Soutetsu thì đổi sang fix. |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1772 | ngôi ba (ranh giới) — điều khoản hợp đồng nêu tên cặp "Soutetsu và Paulette" như một đơn vị bị cấm ("chỉ có anh Soutetsu và Paulette... là bị cấm"), không phải gọi trực tiếp Soutetsu; nhất quán với 1844 (cùng dạng nêu tên cặp). |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1792 | ngôi ba — Kisaki nói với Paulette ("Tất nhiên, em tin tưởng anh Soutetsu. Nhưng con người mà..."); giải thích lý do điều khoản với Paulette. |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1802 | ngôi ba — Kisaki nói với Paulette ("Nhìn dáng vẻ thành thật này của anh Soutetsu đi... — Paulette"); Soutetsu là đối tượng được chỉ cho Paulette xem. |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1804 | ngôi ba — Kisaki nói với Paulette ("Thấy chưa, Paulette? Anh Soutetsu cứng đờ người ra rồi kìa?"). |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1844 | ngôi ba — Kisaki nói với Paulette ("Tùy thuộc vào ý định của chính Paulette và anh Soutetsu"); nêu tên cặp như đối tượng thứ ba. |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1845 | ngôi ba — Kisaki nói với Paulette (tiếp mạch 1844, giải thích bước chuẩn bị); "anh Soutetsu lại ỉu xìu" là nhắc tới Soutetsu với Paulette. |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1879 | ngôi ba (ranh giới) — Kisaki nói với Paulette (1881–1882 tiếp tục hướng về Paulette); "lời nói của anh Soutetsu" / "đặt anh Soutetsu lên hàng đầu" là bàn về Soutetsu với người khác. Giữ theo nguyên tắc; nếu coordinator đọc người nghe là cả nhóm thì đổi sang fix. |

### §3b. "anh Soutetsu" của người nói khác — 55 dòng (P4 chỉ áp cho Kisaki nói)

- `lr稀咲追加02` — 16 dòng: 西瓜 Suika 11 (1098/1251/1266/1327/1401/1457/1509/1510/1656/1657/1660), 姜 Khương 5 (1224/1291/1342/1424/1655). Họ gọi Soutetsu là "anh Soutetsu" đúng vai (người ngoài, nhỏ tuổi hơn) — không đụng.
- `lr稀咲追加03` — 1 dòng: 姜 1038.
- `lr_稀咲h1` — 1 dòng: 双鉄 Soutetsu tự nói 1033 (old_vn = fix audit).
- `lr_稀咲ポーレットh1` — 37 dòng của Paulette (997/1397/1467/1472/1490/1495/1499/1505/1509/1515/1531/1539/1554/1556/1558/1576/1582/1591/1609/1635/1644/1650/1668/1675/1678/1683/1692/1706/1712/1713/1740/1824/1825/1837/1855/1858/1878). Paulette gọi Soutetsu là "anh Soutetsu" theo quy tắc B4/P14 — không đụng.

### §3c. Đã đúng sẵn (không cần sửa)

- `lr稀咲追加03`: 4 dòng "anh Soutetsu" trong CSV3 (938/1294/1433/1434) đã được audit sửa thành "Soutetsu" trần (old_vn = fix audit, ví dụ 938 "Soutetsu lại càng trở nên thiển cận——\ncậu có xu hướng..."). Không sửa trùng.
- `lr_稀咲h1`: toàn file đã dùng "Soutetsu" trần (vd. 1072/1107/1298/986 "Sou, tetsu" tách âm đã trần). 0 dòng "anh Soutetsu".
- `lr稀咲追加01`: các dòng Kisaki khác đã trần (vd. 1341 "A, Soutetsu", 1516 "Không đâu, Soutetsu").

## §4. Cờ (flags — không sửa trong đợt này)

- **F-P4-1 — dạng tách tên "Anh, Soutetsu" / "Anh Sou, tetsu" (JP そう、てつ / そうてつ tách âm), 8 dòng:** trong dòng sửa — lr稀咲追加h 1361 ("Anh Sou, tetsu"), lr_稀咲ポーレットh1 1475/1513/1534 ("Anh, Soutetsu"); ngoài dòng sửa — lr稀咲追加h 1025/1074/1137/1355 ("Anh Sou, tetsu", 1355 ×2), lr_稀咲ポーレットh1 1364 ("anh, Soutetsu"). Các dạng này vẫn mang "Anh" + tên Soutetsu nhưng không chứa chuỗi "anh Soutetsu" nên ngoài chữ của task; list P4 cũng đếm "Anh Sou…" riêng (稀咲h2: 12 dòng). Cần quyết định chung (U7a/U15): có bỏ "Anh" ở dạng tách tên không, hay giữ vì đó là cách diễn rên tách âm. Đề xuất của đợt này: bỏ "Anh" cho nhất quán với P4 ("không bao giờ 'anh Soutetsu'"), nhưng KHÔNG tự áp vì task chỉ định chuỗi đúng.
- **F-P4-2 — Grand 08 key 1702 (ngoài phạm vi, để coordinator):** đã kiểm chứng trực tiếp CSV3 — Kisaki nói, JP 「キミは、それで――」, TW 「你確定要……」, VN 「Cậu, như vậy thì――」. KHÔNG có "anh Soutetsu" — không phải dòng P4; ghi chú "Kisaki speaking" trong list/U6 là đúng về người nói nhưng dòng này không cần sửa gì. Không có hành động nào cần làm.
- **F-P4-3 — ranh giới ngôi ba (3 dòng giữ có thể đảo ngược):** 1722, 1772, 1879 (xem §3a) — nếu coordinator đọc người nghe là Soutetsu (hoặc cả nhóm) thì chuyển sang fix "Soutetsu".

## §5. Quyết định trong đợt (theo uỷ quyền)

- **Nguyên tắc ngôi 2 / ngôi 3:** P4 áp cho mọi cách Kisaki nhắc tới Soutetsu KHI Soutetsu là người nghe — kể cả dạng sở hữu ("dương vật của Soutetsu", "tay của Soutetsu", "em bé của Soutetsu và tôi") và dạng "người em yêu thương nhất là Soutetsu" nói thẳng với anh (1800, bị động される — tác nhân là Soutetsu người nghe). Ngược lại, khi Kisaki nói VỀ Soutetsu với Paulette/Suika/Khương thì "anh Soutetsu" là nhắc ngôi ba, giữ nguyên (tiền lệ U6 giữ Grand 01 2468/2557 ngôi ba).
- **1488 (tsuika01):** sửa theo quyết định 22/11 ~03:32 liệt kê đích danh 1488/1687/1783; câu sau "Anh có thể biến..." là ngôi 2, củng cố người nghe là Soutetsu (TW shift nên không dùng).
- **1195 (lr稀咲追加h):** JP dùng てつ (rút gọn) nhưng TW "雙鐵你的陰莖" xác nhận đối tượng là Soutetsu người nghe — sửa dạng tên theo P4.
- **1534/1877 (lr_稀咲ポーレットh1):** JP không có 双鉄 (dùng そうてつ tách âm) nhưng TW "雙鐵" và mạch rên gọi tên xác nhận đối tượng là Soutetsu — sửa chuỗi đúng "anh Soutetsu", giữ dạng tách (cờ F-P4-1).

## §6. Lượt soát 2 (second pass)

- Đọc lại toàn bộ 51 fix so với JP (+TW, trừ tsuika01 TW shift) và dòng kề: **51/51 tái kiểm chứng, 0 loại bỏ, 0 sửa lại.**
- Kiểm chứng máy: mỗi fix = old_vn thay đúng chuỗi `(?i)anh soutetsu` → `Soutetsu`, không thay đổi nào khác (assert trong script build); fix không còn chứa "anh Soutetsu" (case-insensitive); 60 lần xuất hiện đã thay (tsuika01 3, tsuika02 4, lr稀咲追加h 26, lr_稀咲ポーレットh1 27).
- old_vn đã đối chiếu máy với map hiện tại (moan > audit > CSV3, cộng unification đã gộp): 42 CSV3 / 5 moan / 1 audit / 3 unification (T56 + M16 + M1 — 2 dòng GHÉP bởi coordinator).
- Không đụng dòng gasp Ư hay dòng "Kh" nào; không đụng đại từ "anh" trần (mục P6) hay tự xưng Kisaki (mục P5).

## §7. Khối TOML (parse-verified)

4 file / 51 key. Giá trị `\n` trong khối là literal backslash-n (theo quy ước brief); parse bằng tomllib cho đúng giá trị fix trong JSON.

### lr_稀咲ポーレットh1_悪い大人の契約.txt.toml

```toml
[script]
"1000" = "「……Có vẻ anh mệt đến mức không buồn nói chuyện nữa rồi. Bây giờ Soutetsu\\nhãy nghỉ ngơi đi, đừng suy nghĩ gì cả.」"
"1442" = "「Kyafu!!!? A——đừng——Soutetsu——ưm. Thế này——đột nhiên——đột nhiên——thế này——」"
"1456" = "「Fufu——anh vất vả rồi, Soutetsu.」"
"1459" = "「Fufu, không ngờ lại được cảm ơn bằng ánh mắt nghiêm túc thế kia.\\nCó vẻ Paulette rất khao khát dương vật của Soutetsu nhỉ.」"
"1470" = "「Faaaaan! Soutetsu, nè? Soutetsu——a, em, nè? Em——em, sắp, sắp, sắp rồi!」"
"1475" = "「Fa! A! A! A! A! A! A! A! Anh, Soutetsu——Soutetsu——ưm!」"
"1478" = "「Fua! Soutetsu! Soutetsu, Soutetsu——」"
"1513" = "「Ha——ưm——Fa——a——. Anh, Soutetsu—— Soutetsu——fufu——anh đã cố gắng lắm rồi. Lại đây nào, Soutetsu?」"
"1534" = "「A——không được! Thế này! Đến mất! Đến mất thôi!\\nTuyệt quá! Anh, Soutetsu——Soutetsu!!!」"
"1542" = "「A——ưm fu, fu——cảm ơn anh, Soutetsu. Vì đã\\nđàng hoàng——đàng hoàng——làm tình, với em nữa.」"
"1573" = "「A! Khoan——Soutetsu——ưm——\\nthế này——đột, ngột quá——a ưm——a」"
"1601" = "「Ưm——ha! A! Soutetsu, Soutetsu——em thì——\\nlần sau——hôm nay, em là người thứ hai, cũng được——hãy làm với Paulette đi.」"
"1604" = "「Ưm……fufu——sao nào, Soutetsu? Cảm giác của âm đạo——\\nưm——của em, và của Paulette, có khác nhau nhiều không?」"
"1606" = "「Ừm. ——Vào đi? Soutetsu.」"
"1673" = "「Em……cũng, vậy——Soutetsu……ưm——ha——a——\\nHôm nay——sao, nhỉ——cảm giác, hơn hẳn, mọi khi——」"
"1800" = "「Thấy người em yêu thương nhất là Soutetsu lại có những lời nói và hành động\\nnhư muốn đùn đẩy trách nhiệm cho em, em thấy hơi buồn đấy.」"
"1814" = "「Lần đầu tiên mà đòi có cảm giác bên trong âm đạo thì khó lắm.\\nNè? Soutetsu——nếu được thì kích thích âm vật đi.」"
"1815" = "「Nghe thấy chưa? Vậy Soutetsu nghĩ sao?\\nAnh muốn thế nào? Sau khi nghe những lời vừa rồi của Paulette.」"
"1864" = "「Em thì sao? Soutetsu.」"
"1876" = "「Soutetsu thì——」"
"1877" = "「Soutetsu, Soutetsu——nè? Chưa sao? Vẫn chưa, sao\\n——A! Em——sắp——em, không nhịn được——ưm!」"
```

### lr稀咲追加01_仲国視察の誘い.txt.toml

```toml
[script]
"1488" = "「Chỉ là một phần nhỏ của sự chuẩn bị thôi. Soutetsu thuộc tuýp người hay nảy ra ý tưởng bất chợt mà.\\nAnh có thể biến những tình huống ngoài dự kiến thành cơ hội phát triển.」"
"1687" = "「Sao vậy? Soutetsu.」"
"1783" = "「Nhưng, cô Khương đã dạy tôi 'cách làm phù hợp với bản thân'.\\nThành quả lớn nhất của điều đó, chính là anh đấy? Soutetsu.」"
```

### lr稀咲追加02_仲国視察.txt.toml

```toml
[script]
"1084" = "「Anh đang bị vòng luẩn quẩn 'con gà hay quả trứng có trước' rồi đấy? Soutetsu.\\nAnh đang định giải thích cho tôi giới hạn kiến trúc là gì cơ mà.」"
"1258" = "「Nếu là tôi của quá khứ, dù có thiết kế ra một chuyến tàu đẹp đến đâu,\\nchắc tôi cũng không muốn đi đâu. Còn Soutetsu thì sao?」"
"1353" = "「Mà này, Soutetsu? Cái đó là gì vậy……\\nXe Oiran? ấy.」"
"1629" = "「Vậy thì thứ tiếp theo chúng ta cần khảo sát,\\ncó lẽ là 'chính hiện trạng của Đường sắt Quốc gia Trung Quốc' nhỉ? Anh thấy sao? Soutetsu.」"
```

### lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml

```toml
[script]
"811" = "「……Ừm. Anh không phải đang trêu tôi đâu nhỉ.\\nTại vì Soutetsu——hoàn toàn không có kiến thức về mấy chuyện đó mà.」"
"1059" = "「Làm! Nữa đi! Cứ giữ nguyên, nhịp điệu này——\\nÂm đạo, của tôi——Bằng dương vật——của Soutetsu!!」"
"1077" = "「Yaaa——Soutetsu——Tôi. Tư thế này——\\nXấu hổ lắm——Giống tư thế đóng cọc——quá——」"
"1087" = "「Haa——Haa——Haa——Haa——.\\nƯm…… Ừm. Tôi hiểu rồi. Soutetsu.」"
"1104" = "「A——Ưm——Fu, a——Xin lỗi, xin lỗi anh nhé, Soutetsu.\\nĐúng nhỉ——Chúng ta đang, tắm rửa cho nhau…… mà, nhỉ——Ưm.」"
"1112" = "「A……Fu――Fua――Này, Soutetsu――Nhũ hoa――Ưm\\n――Nhũ hoa……Cái đó, nhé? Thêm nữa――Làm thêm nữa đi?」"
"1114" = "「A……Hà――Ưm. Ngực――\\nTay của Soutetsu, trơn tuột――Nu!!」"
"1132" = "「A! A!!! Soutetsu!!!!\\nĐúng rồi! Đúng rồi! Đúng rồi! Đúng rồi ôi ôi ôi!」"
"1149" = "「Ưm……――Bắt đầu ấm lên rồi.\\nHơn nữa――Soutetsu cũng nóng bừng lên trong chớp mắt kìa.」"
"1165" = "「Ưm! ——Không được——đâu, Soutetsu——\\nNếu Soutetsu mà cử động——tôi——sẽ bị trượt mất——đấy.」"
"1167" = "「Ừm, đúng vậy đấy. Lúc nào tôi cũng cố gắng hết sức.\\nBây giờ, cũng vậy——Tôi muốn có, em bé, của Soutetsu và tôi.」"
"1170" = "「Fufu, Soutetsu nghiêm túc thật đấy.\\nNgười đi review ẩm thực bằng Love Lotion, chắc là hiếm lắm đấy.」"
"1173" = "「Nfufu——Nếu thế này——thì có thể rửa——cùng nhau rồi——\\nDương vật——của Soutetsu——và âm đạo——của tôi——」"
"1175" = "「Fufu. Soutetsu cũng nhận ra cái đó rồi à.」"
"1195" = "「Có vẻ——như vậy nhỉ——Dương vật——của Soutetsu——tuyệt quá.\\nCứng ngắc hoàn toàn rồi——Fu——A——Chỉ cần, chạm vào thôi.」"
"1200" = "「Này? Soutetsu——Soutetsu, thấy sao? Sướng, không? ——Ưm, dùng tay——với lotion——trơn tuột——cọ xát cọ xát.」"
"1218" = "「Gì vậy? Soutetsu.」"
"1232" = "「Tôi…… nhé? Lúc nào cũng, nghĩ rằng.\\nMuốn có em bé với Soutetsu.」"
"1234" = "「Kể từ khi…… bắt đầu nói chuyện, riêng tư——với Soutetsu.\\nDần dần, tôi——đã nghĩ rằng——mình muốn, Soutetsu.」"
"1307" = "「Cả ngực——lẫn đầu nhũ hoa——cũng…… Soutetsu——ưm——a,\\nanh đều rất——nâng niu——ngọt ngào——yêu thương, chúng——nhỉ.」"
"1328" = "「Mất công làm ấm người rồi, tôi không muốn bị lạnh lại đâu.\\nNày, Soutetsu. Cho tôi xin chút thân nhiệt nhé? Ưm……」"
"1349" = "「Không được…… đâu——Soutetsu. Tại vì——tư thế.\\nTư thế này thì…… ưm——tinh dịch, rất dễ, bị tràn ra ngoài.」"
"1361" = "「Soutetsu——Anh Sou, tetsu——Này, tôi——tôi——sắp,\\nsắp——này——lên đỉnh——rồi——ưm——aa.」"
```

## **Ghi chú điều phối (coordinator, 22/11 ~12:10 — 2 dòng ghép):** 1470 trùng U11a (M16) và 1513 trùng U11a (M1) ở token khác nhau — đã GHÉP theo quy tắc composition: old_vn := fix U11a, fix := giá trị kết hợp (1470 = fix M16 bỏ "Anh " trước Soutetsu ×2; 1513 = fix M1 bỏ "Anh Soutetsu" ×2, giữ dạng tách "Anh, Soutetsu" theo cờ F-P4-1). Mỗi giá trị ghép kiểm chứng 2 chiều (bằng fix U11a + đổi P4, và bằng fix đợt này + đổi M16/M1) — cả hai chiều trùng nhau tuyệt đối. Dòng 1629 KHÔNG cần sửa: old_vn đã đúng = fix U13a (T56) từ đầu.

Kết bài

Đợt U7b sửa xong 51/62 dòng ứng viên Kisaki "anh Soutetsu" trong 4 file tsuika/lr (60 lần xuất hiện), còn 11 dòng giữ vì ngôi ba (nói về Soutetsu với Paulette/Suika) và 55 dòng của người nói khác giữ nguyên. JP xác nhận 双鉄 trần ở 59/62 dòng ứng viên (3 dòng dùng そうてつ/てつ tách âm nhưng đối tượng là Soutetsu, TW xác nhận). Nợ lại: quyết định chung về dạng tách tên "Anh, Soutetsu"/"Anh Sou, tetsu" (8 dòng, cờ F-P4-1) và 3 dòng ranh giới ngôi ba (1722/1772/1879) chờ coordinator; Grand 08 key 1702 đã kiểm chứng không phải dòng P4. File còn lại của P4 (03_Paulette/06_Kisaki tuyến chính + 09_Grand) thuộc U7a và batch sau.
