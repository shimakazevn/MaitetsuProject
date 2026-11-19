# Audit: Paulette lr_ポーレットh1_家族旅行の最終日の夜 (Đêm cuối cùng của chuyến du lịch gia đình) — 64 dòng Việt sai (đã đối chiếu JP + TW)

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa từng dòng: 303 dòng (độc thoại 140, 双鉄 65, ポーレット 98), toàn bộ thuộc section `script`, đối chiếu JP + TW từ CSV3 và TOML-2. Tên file đã kiểm chứng khớp CSV3 và TOML-2: `03_Paulette/lr_ポーレットh1_家族旅行の最終日の夜.txt.toml`.
- CSV vs TOML: 0 khác biệt thực chất (chỉ ở `\n`/khoảng trắng); tập key bằng nhau (303, key 697–1745); `[selections]` rỗng; thẻ `%l`: 0 trong JP và VN (không có thẻ hỏng); không có key trùng; không có dòng VN trống; VN==TW 1 (705 — đã sửa trong sweep gasp).
- md5: `bd55bd0643350b7396121d5161727c21` — không trùng với bất kỳ file nào trong 227 file TOML (không có bản sao; bản sửa áp dụng cho 1 file duy nhất).
- Đọc toàn bộ 303 dòng phát hiện 64 dòng sai (21,1%). Rà soát chéo với sweep gasp っ và quét máy tính (pronoun sweep với `\n` chuẩn hoá trước, quét `\bchu\b` và các mảnh La-tinh còn sót, kiểm tra VN trùng và JP trùng) bắt thêm các dòng ngoài lần đọc đầu.
- Rà soát chéo với sweep gasp っ: sweep có 16 mục trong file này — 13 bản sửa + 3 "already-rendered" (1016, 1044, 1045). Audit xác nhận 10 bản sửa của sweep giống hệt (705, 997, 1014, 1035, 1046, 1061, 1078, 1079, 1080, 1196). Audit THAY THẾ 3 bản sửa của sweep bằng bản đọc kỹ hơn: 1005 (sweep giữ "Hya", audit "Hia" theo h8 2136), 1083 (sweep giữ các mảnh La-tinh, audit Việt hoá toàn bộ), 998 (sweep "Kyufu", audit "Kíuphù" theo h8 2142). Audit PHÁT HIỆN thêm 1 dòng gasp mà sweep BỎ SÓT (1077: JP `っ！――ポーレット` — gasp đầu dòng bị mất). Audit KHÔNG ĐỒNG Ý với sweep "already-rendered" ở 1044 và 1045 (mỗi dòng mất 1 tiếng っ — xem chi tiết); đồng ý "already-rendered" ở 1016.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ 64/64 bản sửa đối chiếu JP (đúng 64, 0 bị loại). Kiểm tra lần hai bắt và sửa 5 bản sửa: 1711 (số nguyên âm kéo dài 6 → 5), 1721 (4 → 3), 1042/1083/1089 (ちゅうっ còn "chụt" không kéo dài → "chụụt"). Ngoài ra kiểm tra lần hai xác nhận: không có bản sửa nào thừa hưởng lỗi xưng hô của dòng cho; không có khoảng trắng thừa trước `\n` (bản sửa một dòng, không dùng `\n`); không có dấu 。 thay cho dấu .; các âm thở ghép viết liền một từ ("Kíuphù", "Hiau", "Hia", "Ưm kyu"); không còn mảnh La-tinh nào sót (`\bchu\b` = 0 sau bản sửa — chỉ còn 1530 "chu lên" là từ Việt thật, nghĩa "bĩu môi"; "phu" ở 1026/1072 là hơi thở bị cắt cụt, đã chấp nhận). Quy ước số nguyên âm kéo dài đã chốt trong lần kiểm tra này: **số nguyên âm trong VN = 1 (âm gốc của âm tiết) + số ký tự う/ぅ viết trong JP** — bằng chứng: h7 1651 JP う×10 → bản sửa 11 chữ u; mọi token kéo dài trong 2 file này đều khớp quy tắc này (xem chi tiết từng dòng).
- Quy ước bản sửa: bản sửa viết MỘT DÒNG (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công — theo quyết định 19/11 của Hieu (game tự ngắt dòng, `\n` thủ công không quan trọng). File TOML gốc cũng lưu các giá trị này một dòng với khoảng trắng, nên khối TOML dưới đây dán vào khớp đúng dạng đó. Các khoảng trắng quanh —— trong bản sửa đều là vị trí ngắt dòng cũ (VN cũ có `\n` tại đúng vị trí đó) — không phải khoảng trắng mới; riêng 1220 "A! ——Ưm" giữ nguyên khoảng trắng đã có sẵn trong VN cũ.
- Ghi chú về ký tự gạch: VN cũ của file này trộn lẫn U+2015 HORIZONTAL BAR (―, 366 lần) và U+2014 EM DASH (—, 496 lần); toàn file TOML-2 (kể cả chú thích JP) có U+2015 1233 lần. Bản sửa dùng U+2014 thống nhất — theo quy ước tiếng Việt của dự án (h8 dùng U+2014).

## Kết luận về cơ chế lỗi

- **Không lệch vị trí, không xoay vòng, không tràn chương.** Toàn bộ 64 dòng sai đều là lỗi tại chỗ (xưng hô, hơi thở/âm thanh còn La-tinh, gasp bị bỏ) — không có dòng nào cần thu hồi bản dịch từ dòng khác, không có VN mồ côi. Đây là file "sạch" về cấu trúc, giống h7/h8 ở mức độ nhẹ hơn.
- Lỗi xưng hô hệ thống: Soutetsu tự xưng "anh" 18 dòng trong thoại (cùng lỗi hệ thống như h1–h8; độc thoại không có lần "Anh" nào sai). Trước bản sửa, Soutetsu không có lần nào tự xưng "tôi" trong thoại của file này. 979 KHÔNG tính là lỗi: "anh" ở đó là lời Paulette thuật lại, xưng hô với Soutetsu, không phải Soutetsu tự xưng.
- Lỗi hơi thở/âm thanh La-tinh: 37 dòng thoại + 5 dòng độc thoại — họ lỗi lớn nhất của file. Các âm ちゅ/ぢゅ/じゅ/ず/れる/りゅ/れろ/にゅ còn nguyên dạng La-tinh ("chu", "ju", "rê ru", "rê ryu") hoặc bị Việt hoá sai hướng (にゅぶっ → "Nhóp nhép" ở 1082 là sai nghĩa — phải là "Bụp" trong chuỗi miệng; xem quy ước SFX dưới đây).
- Gasp bị bỏ: 3 dòng (1044, 1045, 1077) — trong đó 1077 là sweep bỏ sót.
- Nghĩa sai: 1 dòng (732 — Paulette nói "họ sẽ…" nhưng ý là "chúng mình sẽ…" — cô ấy nói về mình và Soutetsu).
- "em" vs "cô" (Soutetsu gọi Paulette): **"em" 9 vs "cô" 0** trong file này. Cộng dồn sau file này: **"em" 106 vs "cô" 49** (cơ số sau h8 là 96 theo bản tóm tắt của parent — ROUTE-AUDIT ghi 97 là lệch 1; lr_稀咲h1 +1 "em" → 97, れいな02 +1 "cô" → 49, rồi file này +9 "em"). 979 không tính (lời thuật lại — "Em" là Paulette tự xưng, không phải Soutetsu gọi cô ấy).
- Tên gọi trần B4: **0 dòng** — không có tên "Soutetsu" nào bị rên/gọi trần trong file này (1218 "Anh, Soutetsu" là cách gọi có dấu phẩy ngắt nhịp, không phải tên trần).

## Chi tiết dòng sai

### Xưng hô (18 dòng)

**Key 707 (双鉄)**
- JP: `「――家族旅行の穏やかな夜を壊したくない。\nしっかり声を抑えてくれよ？」`
- TW: `「——我不想破壞家庭旅行之夜的安穩。你可要努力控制好音量」`
- VN cũ: `「――Anh không muốn phá hỏng đêm yên bình của chuyến du lịch gia đình đâu.\nEm phải cố gắng kìm nén giọng nói đấy nhé?」`
- Sửa: `「――Tôi không muốn phá hỏng đêm yên bình của chuyến du lịch gia đình đâu. Em phải cố gắng kìm nén giọng nói đấy nhé?」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi" (độc thoại và thoại đều dùng "tôi"; "anh" chỉ đúng khi nói với Hibiki).
**Key 712 (双鉄)**
- JP: `「『ごまかしやすい』。だな？　心得た」`
- TW: `「“才容易解釋”。對吧？我明白了」`
- VN cũ: `「『Dễ che giấu hơn』. Đúng không? Anh hiểu rồi」`
- Sửa: `「『Dễ che giấu hơn』. Đúng không? Tôi hiểu rồi」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 953 (双鉄)**
- JP: `「してほしいのではないなら――なんだ？」`
- TW: `「不想做的話——那是想怎樣呢？」`
- VN cũ: `「Nếu không phải là muốn anh làm――thì là gì?」`
- Sửa: `「Nếu không phải là muốn tôi làm――thì là gì?」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 967 (双鉄)**
- JP: `「なにを、してほしいんだ？」`
- TW: `「你想要我做什麼？」`
- VN cũ: `「Em muốn, anh làm gì?」`
- Sửa: `「Em muốn, tôi làm gì?」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 984 (双鉄)**
- JP: `「それでもひとつだけはわかる」`
- TW: `「即便如此，有件事我可以肯定」`
- VN cũ: `「Nhưng có một điều anh chắc chắn.」`
- Sửa: `「Nhưng có một điều tôi chắc chắn.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1108 (双鉄)**
- JP: `「ああ、それをまた履くのはイヤなものだろうな。\nすまん。着たままするにはこれが一番良いかと思って」`
- TW: `「嗯，那樣的話確實不會想要再穿回去。對不起。我以為要穿著做的話這個方式是最合適的」`
- VN cũ: `「À, vậy thì mặc lại cũng khó chịu thật nhỉ.\nXin lỗi em. Anh cứ nghĩ làm trong lúc mặc đồ thì cách này là tốt nhất」`
- Sửa: `「À, vậy thì mặc lại cũng khó chịu thật nhỉ. Xin lỗi em. Tôi cứ nghĩ làm trong lúc mặc đồ thì cách này là tốt nhất」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1122 (双鉄)**
- JP: `「素敵だった。最高だった。\nポーレット――好きだ。愛してる――んっ」`
- TW: `「太美妙太完美了。波萊特——我喜歡你。我愛你——嗯」`
- VN cũ: `「Tuyệt lắm. Hoàn hảo lắm.\nPaulette——Anh thích em. Anh yêu em——ưm」`
- Sửa: `「Tuyệt lắm. Hoàn hảo lắm. Paulette——Tôi thích em. Tôi yêu em——ưm」`
- Lý do: Soutetsu tự xưng "anh" 2 lần — sửa thành "tôi".
**Key 1137 (双鉄)**
- JP: `「僕の勃起が、えぐって、こすって、ノックして。\n精子をびゅうびゅう、溢れるほどに注ぎ込んで」`
- TW: `「就由我的勃起來搗弄、來刮蹭、來叩門。讓裡面灌滿我的精子」`
- VN cũ: `「Dương vật của anh, sẽ khoét sâu, cọ xát, và gõ cửa.\nRót tinh trùng vào tràn trề, ồ ạt」`
- Sửa: `「Dương vật của tôi, sẽ khoét sâu, cọ xát, và gõ cửa. Rót tinh trùng vào tràn trề, ồ ạt」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1140 (双鉄)**
- JP: `「無理に広げるつもりはないさ。\nただ――」`
- TW: `「我並不是硬要撐開。只不過——」`
- VN cũ: `「Anh không định mở rộng nó ra bằng sức mạnh đâu.\nChỉ là――」`
- Sửa: `「Tôi không định mở rộng nó ra bằng sức mạnh đâu. Chỉ là――」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1144 (双鉄)**
- JP: `「ここからなのだ、と思ってな。\nひかりの生命のすべてがここから産まれたのだと」`
- TW: `「我只是在感嘆而已。光的整個生命就是從這裡誕生的啊」`
- VN cũ: `「Anh chỉ nghĩ, là từ nơi này.\nToàn bộ sinh mệnh của Hikari đã được sinh ra từ nơi này」`
- Sửa: `「Tôi chỉ nghĩ, là từ nơi này. Toàn bộ sinh mệnh của Hikari đã được sinh ra từ nơi này」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1149 (双鉄)**
- JP: `「わかっている、ポーレット。溜まりに溜まった精液を、\n注ぎ込みたい先ならば、ただ一箇所しかありえない」`
- TW: `「我明白，波萊特。我這積蓄已久的精液，不可能存在其他的宣洩之處」`
- VN cũ: `「Anh biết mà, Paulette. Nơi duy nhất anh muốn rót trào\nlượng tinh dịch đã dồn nén bấy lâu nay, chỉ có thể là một chỗ mà thôi」`
- Sửa: `「Tôi biết mà, Paulette. Nơi duy nhất tôi muốn rót trào lượng tinh dịch đã dồn nén bấy lâu nay, chỉ có thể là một chỗ mà thôi」`
- Lý do: Soutetsu tự xưng "anh" 2 lần — sửa thành "tôi".
**Key 1151 (双鉄)**
- JP: `「風呂に誘って浴衣に着替えて……\nなどとも考えていたのだがな」`
- TW: `「我本打算邀你換上浴衣一起去泡澡的……」`
- VN cũ: `「Anh đã định rủ em đi tắm rồi thay yukata……\nvà vài chuyện khác nữa cơ」`
- Sửa: `「Tôi đã định rủ em đi tắm rồi thay yukata…… và vài chuyện khác nữa cơ」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1155 (双鉄)**
- JP: `「動くぞ。ポーレット」`
- TW: `「我要動了。波萊特」`
- VN cũ: `「Anh chuyển động đây. Paulette」`
- Sửa: `「Tôi chuyển động đây. Paulette」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1169 (双鉄)**
- JP: `「だな。そのたびに――僕も強烈に絞られている」`
- TW: `「是啊。每次頂到花心——我也有種被死死勒住的感覺」`
- VN cũ: `「Đúng vậy. Mỗi lần chạm vào đó——anh cũng bị siết chặt dữ dội.」`
- Sửa: `「Đúng vậy. Mỗi lần chạm vào đó——tôi cũng bị siết chặt dữ dội.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1172 (双鉄)**
- JP: `「だよな。以前よりずっと気持ちいい。\n肌と肌とが、吸いあっているような気さえする」`
- TW: `「是啊。比之前還要舒服得多。我都覺得皮膚之間好像產生了吸力一樣」`
- VN cũ: `「Đúng vậy nhỉ. Sướng hơn trước kia rất nhiều.\nAnh thậm chí còn có cảm giác như da thịt chúng ta đang hút chặt lấy nhau vậy」`
- Sửa: `「Đúng vậy nhỉ. Sướng hơn trước kia rất nhiều. Tôi thậm chí còn có cảm giác như da thịt chúng ta đang hút chặt lấy nhau vậy」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1190 (双鉄)**
- JP: `「大丈夫。僕に上等な代案がある」`
- TW: `「沒關係。我有個更好的方案」`
- VN cũ: `「Không sao. Anh có một phương án thay thế tuyệt vời.」`
- Sửa: `「Không sao. Tôi có một phương án thay thế tuyệt vời.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1212 (双鉄)**
- JP: `「初めて肌を重ねたときに、\nこれほどの快感がこの世にあるのかと驚愕したが」`
- TW: `「第一次肌膚相親之時，我絕對不會料到將來的某天晚上能收穫到如此強烈的快感」`
- VN cũ: `「Lần đầu tiên chúng ta ân ái,\nanh đã kinh ngạc không ngờ trên đời này lại có thứ khoái cảm nhường này, nhưng」`
- Sửa: `「Lần đầu tiên chúng ta ân ái, tôi đã kinh ngạc không ngờ trên đời này lại có thứ khoái cảm nhường này, nhưng」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".
**Key 1223 (双鉄)**
- JP: `「さぁ。どうだろうな。\nそれは僕にはわからない」`
- TW: `「誰知道呢。這種事我也不知道」`
- VN cũ: `「Chà. Ai mà biết được.\nChuyện đó thì anh chịu thôi.」`
- Sửa: `「Chà. Ai mà biết được. Chuyện đó thì tôi chịu thôi.」`
- Lý do: Soutetsu tự xưng "anh" — sửa thành "tôi".

### Nghĩa sai (1 dòng)

**Key 732 (ポーレット)**
- JP: `「……こんな夜、には、こっそり、声を、抑えながら――\nそれでも、きっと……、エッチ――エッチ、を――んっ」`
- TW: `「……在這樣的，夜晚裡，壓低著聲音——偷偷地……做——做愛——嗯」`
- VN cũ: `「……Vào một đêm như thế này, họ sẽ lén lút, kìm nén giọng nói――\nNhưng chắc chắn……họ sẽ làm tình――làm tình――ưm」`
- Sửa: `「……Vào một đêm như thế này, chúng mình sẽ lén lút, kìm nén giọng nói―― Nhưng chắc chắn……chúng mình sẽ làm tình――làm tình――ưm」`
- Lý do: Paulette nói về chính mình + Soutetsu ("chúng mình"), không phải "họ" — JP không có chủ ngữ chỉ người khác; TW cũng là hành động của hai người.

### Gasp (tiếng っ bị bỏ) (3 dòng)

**Key 1044 (ポーレット)**
- JP: `「っ！　っ！　っ！　～～～～～っ！！！」`
- TW: `「唔！唔！唔！唔～～～～～！！！」`
- VN cũ: `「Ư! Ư! Ư! ～～～～～!!!」`
- Sửa: `「Ư! Ư! Ư! ～～～～～Ư!!!」`
- Lý do: Sweep đánh dấu already-rendered nhưng còn mất 1 tiếng っ (JP 4 tiếng っ, VN chỉ có 3 tiếng Ư) — bổ sung Ư sau ～～～～～.
**Key 1045 (ポーレット)**
- JP: `「っ！！！　～～～っ！！　っ――ぁっ――っ！！！」`
- TW: `「唔！！！唔～～～！！唔——啊——唔！！！」`
- VN cũ: `「Ư!!! ～～～!! Ư——a——ư!!!」`
- Sửa: `「Ư!!! ～～～Ư!! Ư——a——ư!!!」`
- Lý do: Sweep đánh dấu already-rendered nhưng còn mất 1 tiếng っ (JP ～～～っ, VN chỉ có ～～～) — bổ sung Ư.
**Key 1077 (双鉄)**
- JP: `「っ！　――ポーレット」`
- TW: `「啊！——波萊特」`
- VN cũ: `「! ――Paulette」`
- Sửa: `「Ư! ――Paulette」`
- Lý do: Gasp sweep bỏ sót: JP っ！ đầu dòng, VN chỉ còn "!" — sửa thành "Ư!".

### Hơi thở / âm thanh (thoại) (37 dòng)

**Key 998 (ポーレット)**
- JP: `「きゅっふっ！！！？　～～～～～～～っ！！！！」`
- TW: `「呀呼！！！？哇～～～～～！！！！」`
- VN cũ: `「Kyufu!!!? ~~~~~~~!!!!」`
- Sửa: `「Kíuphù!!!? ~~~~~~~Ư!!!!」`
- Lý do: きゅっふっ còn La-tinh "Kyufu" — sửa thành "Kíuphù" (きゅ→"Kíu" theo tiền lệ h8 2142); gasp cuối đã có trong sweep (xác nhận).
**Key 1000 (ポーレット)**
- JP: `「ひゃうっ――んっ――ふあっ――ふっ――\n指、かたいとこ――かんせつ――こしゅ、れてっ」`
- TW: `「呀唔——嗯——呼啊——呼——手指的——關節——硬硬的，蹭到了」`
- VN cũ: `「Hya――ưm――phù――phù――\nChỗ cứng của, ngón tay――khớp xương――đang cọ, xát」`
- Sửa: `「Hiau――ưm――phà――phù―― Chỗ cứng của, ngón tay――khớp xương――đang cọ, xát」`
- Lý do: ひゃうっ còn "Hya" — sửa thành "Hiau" (ひゃう→"Hiau" theo tiền lệ h8 2137); ふあっ→"phà" theo quyết định fa/fu 19/11.
**Key 1002 (ポーレット)**
- JP: `「ひゃうっ！！　けどっ―きもちいっ――んっ――\nそうてつ、くっ――んっ――しょこっ――そこっ」`
- TW: `「呀唔！！但是——好舒服——嗯雙鐵君——嗯——好棒——那裡」`
- VN cũ: `「Hya!! Nhưng mà――sướng quá――ưm――\nAnh Soutetsu――ưm――chỗ đó――chỗ đó」`
- Sửa: `「Hiau!! Nhưng mà――sướng quá――ưm―― Anh Soutetsu――ưm――chỗ đó――chỗ đó」`
- Lý do: ひゃうっ còn "Hya" — sửa thành "Hiau".
**Key 1003 (ポーレット)**
- JP: `「ひゃうっ！？　あっ――んっ！　くっ――ふぁっ！\nんあっ！！」`
- TW: `「呀唔！？啊——嗯！咕——呼啊！嗯啊！！」`
- VN cũ: `「Hyau!? A――ưm! Hự――phù!\nƯm a!!」`
- Sửa: `「Hiau!? A――ưm! Hự――phà! Ưm a!!」`
- Lý do: ひゃうっ còn "Hyau" — sửa thành "Hiau"; くふっ→"Khự"; ふぁっ→"phà".
**Key 1005 (ポーレット)**
- JP: `「ひあっ！　ぁ――うっ――～～～～～っ！\nけどっ――これっ――ごちゅってなると――声、勝手に」`
- TW: `「呀啊！啊——唔～～～～！可是——這個——一被頂到花心——就會不由自主地，叫出來」`
- VN cũ: `「Hya! A——ư——～～～～～!\nNhưng mà——thế này——cứ đâm lút cán là——em lại không kiềm được tiếng rên.」`
- Sửa: `「Hia! A——ư——～～～～～Ư! Nhưng mà——thế này——cứ đâm lút cán là——em lại không kiềm được tiếng rên.」`
- Lý do: ひあっ còn "Hya" — sửa thành "Hia" (sweep chỉ sửa gasp, giữ "Hya" — audit thay bằng "Hia"); gasp ～～～～～っ đã có trong sweep (xác nhận).
**Key 1007 (ポーレット)**
- JP: `「ひあっ！　あっ！！　これっ！　しゅきっ！」`
- TW: `「呀啊！啊！！這樣！好喜歡！」`
- VN cũ: `「Hya! A!! Thế này! Em thích lắm!」`
- Sửa: `「Hia! A!! Thế này! Em thích lắm!」`
- Lý do: ひあっ còn "Hya" — sửa thành "Hia".
**Key 1011 (ポーレット)**
- JP: `「ひあっ！　あっ――きもちい――きもちい、よぉ――\nん――そうてつくんの、指――わたし――乳首――あっ」`
- TW: `「呀！啊——好舒服——好舒服啊——嗯——雙鐵君的，手指——把我的——乳頭——啊」`
- VN cũ: `「Hyaa! A――Sướng quá――sướng quá, đi――\nƯm――Ngón tay, của anh Soutetsu――núm vú――của em――a」`
- Sửa: `「Hia! A――Sướng quá――sướng quá, đi―― Ưm――Ngón tay, của anh Soutetsu――núm vú――của em――a」`
- Lý do: ひあっ còn "Hyaa" (thừa 1 chữ a + "Hya") — sửa thành "Hia".
**Key 1019 (ポーレット)**
- JP: `「ふぁっ――あっ――あっ――あっ――」`
- TW: `「呼啊——啊——啊——啊——」`
- VN cũ: `「Phù――a――a――a――」`
- Sửa: `「Phà――a――a――a――」`
- Lý do: ふぁっ còn "Phù" — sửa thành "Phà" theo quyết định fa/fu.
**Key 1020 (ポーレット)**
- JP: `「ふあっ――あっ――ねっ――ふあっ――もっと――\nそうてつ、くんっ――おまんこ――もっと――」`
- TW: `「呼啊——啊——我說——呼啊——繼續——雙鐵君——小穴——還要更多——」`
- VN cũ: `「Pha——a——nè——pha——nữa đi——\nAnh Soutetsu——âm đạo——nữa đi——」`
- Sửa: `「Phà——a——nè——phà——nữa đi—— Anh Soutetsu——âm đạo——nữa đi——」`
- Lý do: ふあっ còn "Pha"/"pha" — sửa thành "Phà"/"phà".
**Key 1022 (ポーレット)**
- JP: `「ふぁっ――あっ――指より――わた、しっ――んっ――\nおちん、ちん――そうてつくん、の、ほしい、のにっっ」`
- TW: `「呼啊——啊——比起手指——我——嗯——明明——更想要，你的，肉棒呀」`
- VN cũ: `「Phù――a――Hơn cả ngón tay――em――ưm――\nMuốn, chim――của anh Soutetsu, cơ」`
- Sửa: `「Phà――a――Hơn cả ngón tay――em――ưm―― Muốn, chim――của anh Soutetsu, cơ」`
- Lý do: ふぁっ còn "Phù" — sửa thành "Phà".
**Key 1023 (ポーレット)**
- JP: `「ふあっ――あっ！　あっ！　あっ！\nはっ！　あっ――んうっ――くふっ――あっ！」`
- TW: `「呼啊——啊！啊！啊！哈！啊——嗯唔——咕呼——啊！」`
- VN cũ: `「Phù――a! A! A!\nHà! A――ưm――kufu――a!」`
- Sửa: `「Phà――a! A! A! Hà! A――ưm――Khự――a!」`
- Lý do: ふぁっ còn "Phù" — sửa thành "Phà"; くふっ còn "kufu" — sửa thành "Khự".
**Key 1025 (ポーレット)**
- JP: `「ふぁっ――ンッ――（こくっ）――チュむっ――ちゅ\nれるっ――れりゅううっ――ぢゅるっ――ちゅううっ」`
- TW: `「呼啊——嗯——（吞嚥）——啾唔——啾滋溜——滋嚕嚕——啾嚕——啾唔唔」`
- VN cũ: `「Phù――ưm――（ực）――chùn chụt――chụt\nLiếm――liếm――chùn chụt――chùn chụt」`
- Sửa: `「Phà――ưm――（ực）――chụt――chụt Rộp――rộộộp――rột——chụụụt」`
- Lý do: ふぁっ→"Phà"; れるっ/れりゅううっ còn "Liếm"/"chùn chụt" — sửa thành "rộp"/"rộôôp" (họ れる→"rộp", れりゅううっ = 3 tiếng u: りゅ+う×2); ぢゅるっ→"rột"; ちゅううっ→"chụụụt" (3 tiếng u: ちゅ+う×2).
**Key 1040 (ポーレット)**
- JP: `「っ――～～～っ――っ！　ぁっ――んむっ――\nチュッ――ちゅうううっ――ヂュルッ――（ごくっ）」`
- TW: `「唔——嗯～～～唔——！啊——嗯唔——啾——啾唔唔唔——啾嚕——（吞嚥）」`
- VN cũ: `「Ư——～～～——! A——ưm——\nchụt——chụt——chu ru——（Ực）」`
- Sửa: `「Ư——～～～Ư——Ư! A——ưm—— chụt——chụụụụt——rột——（Ực）」`
- Lý do: Còn mất 2 tiếng っ (～～～っ và っ！) — bổ sung Ư; ちゅうううっ còn "chụt" không kéo dài — sửa thành "chụụụụt" (4 tiếng u: ちゅ+う×3); ヂュルッ còn "chu ru" — sửa thành "rột".
**Key 1042 (ポーレット)**
- JP: `「っっ～～！　っ――チュッ――ちゅうっ――はっ――\nジュルっ――チュッ――っ～～チュズッ――（ごくっ）」`
- TW: `「唔唔～～！——啾——啾唔——哈——啾嚕——啾——唔～～啾茲——（吞嚥）」`
- VN cũ: `「Ư～～! Ư——chụt——chụt——ha——\nchu ru——chụt——ư～～chu zu——（Ực）」`
- Sửa: `「ƯƯ～～! Ư——chụt——chụụt——ha—— rột——chụt——ư～～chụt——（Ực）」`
- Lý do: っっ đầu dòng chỉ có 1 tiếng Ư — sửa thành "ƯƯ" (1 Ư cho mỗi っ); ちゅうっ còn "chụt" không kéo dài — sửa thành "chụụt" (2 tiếng u: âm gốc + う×1); ジュルっ còn "chu ru" — sửa thành "rột"; っ～～チュズッ còn "ư～～chu zu" — sửa thành "ư～～chụt".
**Key 1043 (ポーレット)**
- JP: `「んむっ！？！　んっ――ちゅっ――じゅりゅっ――\nりゅっ――れるっ――ちゅぷっ――ちゅむっ――ぷぁ」`
- TW: `「唔嗯！？！嗯——啾——啾溜——溜——滋溜——啾噗——啾嗯——噗啊」`
- VN cũ: `「Ưm!?! Ưm——chụt——chu ryu——\nryu——rê ru——chu pu——chu mu——pha」`
- Sửa: `「Ưm!?! Ưm——chụt——rột—— rộp——rộp——chụt——chụt——phà」`
- Lý do: じゅりゅっ/りゅっ/れるっ/ちゅぷっ/ちゅむっ còn La-tinh — sửa thành "rột"/"rộp"/"rộp"/"chụt"/"chụt"; ぷぁ còn "pha" — sửa thành "phà".
**Key 1049 (ポーレット)**
- JP: `「ぁっ――っ――ふあ――あっ――おくっ――おちんちん\n――きとう――あたると――頭も、ごちゅっって――」`
- TW: `「啊——唔——呼啊——啊——裡面——肉棒——龜頭——頂到之後——腦袋也，像被頂開了花——」`
- VN cũ: `「A——ư——pha——a——bên trong——dương vật\n——quy đầu——chạm vào——đầu em cũng, như muốn nổ tung——」`
- Sửa: `「A——ư——phà——a——bên trong——dương vật ——quy đầu——chạm vào——đầu em cũng, như muốn nổ tung——」`
- Lý do: ふあ còn "pha" — sửa thành "phà" (tiếng っ giữa đã có "ư" trong VN cũ, giữ nguyên).
**Key 1056 (ポーレット)**
- JP: `「ぁっ――チュむっ――ちゅ！　れりゅうううっ！\nりゅっ！　にゅる！　チュルルっ――ちゅむううっ！」`
- TW: `「啊——啾唔——啾！滋嚕嚕嚕嚕！嚕！啾嚕！啾嚕嚕——啾嗯嗯嗯！」`
- VN cũ: `「A——chu mu——chụt! Rê ryu uu!\nRyu! Nyu ru! Chu ru ru——chu mu uu!」`
- Sửa: `「A——chụt——chụt! Rộộộộp! Rộp! Trơn tuột! Chụt——chụụụt!」`
- Lý do: チュむっ còn "chu mu" — sửa thành "chụt"; れりゅうううっ còn "Rê ryu uu" — sửa thành "Rộôôôp" (4 tiếng u: âm gốc + う×3); りゅっ→"Rộp"; にゅる→"Trơn tuột" (quy ước riêng của file); チュルルっ→"chụt"; ちゅむううっ→"chụụụt" (3 tiếng u: âm gốc + う×2).
**Key 1058 (ポーレット)**
- JP: `「あっ――うんっ――けどっ――ふあっ、あっ――\nけど、ね？　そうてつくぅん」`
- TW: `「啊——嗯——可是——呼啊，啊——可是啊，雙鐵君」`
- VN cũ: `「A——ưm——nhưng mà——pha, a——\nnhưng mà, anh Soutetsu」`
- Sửa: `「A——ưm——nhưng mà——phà, a—— nhưng mà, anh Soutetsu」`
- Lý do: ふあっ còn "pha" — sửa thành "phà".
**Key 1060 (ポーレット)**
- JP: `「っぁっ――ンッ――れるっ――ちゅむっ！\nちゅっ！　ちゅうう！　ちゅっ！　れりゅっ！！」`
- TW: `「啊——嗯——滋溜——啾嗯！啾！啾唔唔！啾！滋嚕！！」`
- VN cũ: `「A——ưm——rê ru——chu mu!\nChụt! Chụt! Chụt! Rê ryu!!」`
- Sửa: `「A——ưm——rộp——chụt! Chụt! Chụụụt! Chụt! Rộp!!」`
- Lý do: れるっ còn "rê ru" — sửa thành "rộp"; ちゅむっ còn "chu mu" — sửa thành "chụt"; ちゅうう còn "Chụt" không kéo dài — sửa thành "chụụụt" (3 tiếng u: ちゅ+う×2); れりゅっ còn "Rê ryu" — sửa thành "rộp".
**Key 1062 (ポーレット)**
- JP: `「ぁ……チュッ――ちゅっ――んっ――ふぁっ。\nん……えへへっ――わたしも、愛しています。双鉄くん」`
- TW: `「啊……啾——啾——嗯——呼啊。嗯……哎嘿嘿——我也愛你。雙鐵君」`
- VN cũ: `「A……chụt——chụt——ưm——pha.\nƯm……ehehe——em cũng yêu anh. Anh Soutetsu」`
- Sửa: `「A……chụt——chụt——ưm——phà. Ưm……ehehe——em cũng yêu anh. Anh Soutetsu」`
- Lý do: ふぁっ còn "pha" — sửa thành "phà" (cười "ehehe" giữ nguyên — chờ quyết định).
**Key 1065 (ポーレット)**
- JP: `「あ……。ん――ちゅっ――ちゅむっ――ちゅっ、\nちゅぶっ――ちゅぱっ――ぷぁ――れろっ――にゅるっ」`
- TW: `「啊……嗯——啾——啾嗯——啾，啾噗——啾啪——噗啊——滋溜——啾嚕」`
- VN cũ: `「A……. Ưm――chụt――chùn chụt――chụt,\nchụt――chụt――phù――liếm――trơn tuột」`
- Sửa: `「A……. Ưm――chụt――chụt――chụt, chụt――chụt――phà――rộp――trơn tuột」`
- Lý do: ちゅむっ còn "chùn chụt" — sửa thành "chụt"; ぷぁ còn "phù" — sửa thành "phà"; れろっ còn "liếm" — sửa thành "rộp".
**Key 1072 (ポーレット)**
- JP: `「ぁんっ――ちゅっ――ちゅるっ――にゅむるっ――\nにゅっ――ちゅっ――ヂュるるるる～っ――（こくっ）」`
- TW: `「啊嗯——啾——啾嚕——滋嚕——滋——啾——啾嚕嚕嚕嚕～（吞嚥）」`
- VN cũ: `「A――chụt――chùn chụt――nyumuru――\nNyu――chụt――jurururu~――（ực）」`
- Sửa: `「A――chụt――chụt――rột―― rột――chụt――rột~――（ực）」`
- Lý do: ちゅるっ còn "chùn chụt" — sửa thành "chụt"; にゅむるっ/にゅっ/ヂュるるるる～っ còn La-tinh — sửa thành "rột"/"rột"/"rột~".
**Key 1073 (ポーレット)**
- JP: `「あんっ」`
- TW: `「啊嗯」`
- VN cũ: `「A」`
- Sửa: `「An」`
- Lý do: あんっ còn "A" (mất âm mũi n) — sửa thành "An".
**Key 1074 (ポーレット)**
- JP: `「あんっ！」`
- TW: `「啊嗯！」`
- VN cũ: `「A!」`
- Sửa: `「An!」`
- Lý do: あんっ！ còn "A!" — sửa thành "An!".
**Key 1075 (ポーレット)**
- JP: `「あんっ！！」`
- TW: `「啊嗯！！」`
- VN cũ: `「A!!」`
- Sửa: `「An!!」`
- Lý do: あんっ！！ còn "A!!" — sửa thành "An!!".
**Key 1082 (ポーレット)**
- JP: `「ちゅっ――ちゅむっ――ぢゅるるうっ――りゅっ――\nにゅぶっ――ちゅくっ――ちゅううっ――ちゅぶっつ」`
- TW: `「啾——啾嗯——啾嚕嚕——溜——滋噗——啾咕——啾唔唔——啾噗」`
- VN cũ: `「Chụt――chùn chụt――jururuu――ryu――\nNhóp nhép――chụt――chùn chụt――chụt」`
- Sửa: `「Chụt——chụt——rột——rộp—— Bụp——chụt——chụụụt——chụt」`
- Lý do: ちゅむっ còn "chùn chụt" — sửa thành "chụt"; ぢゅるるうっ còn "jururuu" — sửa thành "rột"; りゅっ còn "ryu" — sửa thành "rộp"; にゅぶっ còn "Nhóp nhép" (tiếng nhai, sai) — sửa thành "Bụp"; ちゅううっ còn "chùn chụt" — sửa thành "chụụụt" (3 tiếng u: ちゅ+う×2).
**Key 1083 (ポーレット)**
- JP: `「ちゅっ――んっ――ちゅうっ――チュッ――れるっ――\nリュッ――じゅるっ――じゅろっ――ちゅむ――っ！？」`
- TW: `「啾——嗯——啾唔——啾——滋溜——溜——滋溜——滋溜——啾嗯——！？」`
- VN cũ: `「Chụt——ưm——chụt——chụt——rê ru——\nryu——chu ru——chu ro——chu mu——!?」`
- Sửa: `「Chụt——ưm——chụụt——chụt——rộp—— rộp——rột——rột——chụt——Ư!?」`
- Lý do: Sweep chỉ sửa gasp cuối, giữ nguyên các mảnh La-tinh — audit Việt hoá toàn bộ: ちゅうっ còn "chụt" không kéo dài — sửa thành "chụụt" (2 tiếng u: âm gốc + う×1); れるっ→"rộp", リュッ→"rộp", じゅるっ→"rột", じゅろっ→"rột", ちゅむ→"chụt".
**Key 1085 (ポーレット)**
- JP: `「ぢゅるるうっ――（こくっ）――チュッ――ちゅむっ、\nちゅるっ――チュッ――れるるうっ――ちゅずっ」`
- TW: `「啾嚕嚕嚕——（吞嚥）——啾——啾嗯，啾嚕——啾——滋嚕嚕——啾茲」`
- VN cũ: `「Chu ru ru——（Ực）——chụt——chu mu,\nchu ru——chụt——rê ru ru——chu zu」`
- Sửa: `「Rột——（Ực）——chụt——chụt, chụt——chụt——rộp——chụt」`
- Lý do: ぢゅるるうっ còn "Chu ru ru" — sửa thành "rột"; ちゅむっ/ちゅるっ/ちゅずっ còn La-tinh — sửa thành "chụt"/"chụt"/"chụt"; れるるうっ còn "rê ru ru" — sửa thành "rộp".
**Key 1089 (ポーレット)**
- JP: `「ンッ――チュッ――っ――はっ――チュむっ――\nちゅうっ――れりゅ――れろっ――れろっ――ちゅぶっ」`
- TW: `「嗯——啾——唔——哈——啾唔——啾——滋溜——滋溜——滋溜——啾噗」`
- VN cũ: `「Ưm——chụt——ư——ha——chu mu——\nchụt——rê ryu——rê ro——rê ro——chu bu」`
- Sửa: `「Ưm——chụt——ư——ha——chụt—— chụụt——rộp——rộp——rộp——chụt」`
- Lý do: チュむっ còn "chu mu" — sửa thành "chụt"; ちゅうっ còn "chụt" không kéo dài — sửa thành "chụụt" (2 tiếng u: âm gốc + う×1); れりゅ/れろっ còn "rê ryu"/"rê ro" — sửa thành "rộp"/"rộp"; ちゅぶっ còn "chu bu" — sửa thành "chụt" (tiếng っ giữa đã có "ư" trong VN cũ, giữ nguyên).
**Key 1096 (ポーレット)**
- JP: `「んきゅっ――ふぁっ――あっ、これ――しゅきっ――\nっっ――ふっ――ねっ――このまま――もっと」`
- TW: `「嗯呀——呼啊——啊，這個——好棒——唔——呼——來——就這樣——繼續」`
- VN cũ: `「Ưm——pha——a, thế này——thích quá——\nư——phu——nè——cứ thế này——nữa đi」`
- Sửa: `「Ưm kyu——phà——a, thế này——thích quá—— ư ư——phu——nè——cứ thế này——nữa đi」`
- Lý do: んきゅっ còn "Ưm" (mất "kyu") — sửa thành "Ưm kyu" (theo tiền lệ h7); ふぁっ còn "pha" — sửa thành "phà"; っっ chỉ có 1 tiếng "ư" — sửa thành "ư ư" (1 tiếng cho mỗi っ).
**Key 1100 (ポーレット)**
- JP: `「んっ！　――ふぁっっ――やぁんっ――指っ――んっ！\nいきなりっ――に、ほんっ――ひ――ぁっ――」`
- TW: `「嗯！——呼啊——呀嗯——手指——嗯！一上來就——兩根——呀——啊——」`
- VN cũ: `「Ưm! ――Phù――A――Ngón tay――ưm!\nĐột nhiên――hai, ngón――hi――a――」`
- Sửa: `「Ưm! ――Phà――A――Ngón tay――ưm! Đột nhiên――hai, ngón――hi――a――」`
- Lý do: ふぁっっ còn "Phù" — sửa thành "phà".
**Key 1113 (ポーレット)**
- JP: `「ぷあっ！　あっ――はっ――あっ――しゅごっ――\nおまんこ――しきゅう――すごい――こい、のっ」`
- TW: `「噗啊！啊——哈——啊——好厲害——小穴——子宮——好多——濃濃的」`
- VN cũ: `「Pha! A——ha——a——tuyệt quá——\nâm đạo——tử cung——nhiều quá——đặc quá」`
- Sửa: `「Phà! A——ha——a——tuyệt quá—— âm đạo——tử cung——nhiều quá——đặc quá」`
- Lý do: ぷあっ còn "Pha" — sửa thành "Phà".
**Key 1124 (ポーレット)**
- JP: `「はい……っ――ふあっ――たくさん、たくさん――\n精子、わたし――そうてつくんから――受け取って」`
- TW: `「好的……呼啊——雙鐵君——要給我很多，很多——精子」`
- VN cũ: `「Vâng……ưm――phù――Thật nhiều, thật nhiều――\nTinh trùng, em――sẽ nhận lấy――từ anh Soutetsu」`
- Sửa: `「Vâng……ưm――phà――Thật nhiều, thật nhiều―― Tinh trùng, em――sẽ nhận lấy――từ anh Soutetsu」`
- Lý do: ふあっ còn "phù" — sửa thành "phà".
**Key 1184 (ポーレット)**
- JP: `「そん、なに……っ――はっ――あっ――んっ――\nんふっ――きもち……いい……です、か？――ぁ」`
- TW: `「有這麼……哈——啊——嗯——嗯呼——舒服……嗎？——啊」`
- VN cũ: `「Đến, mức đó……ưm――hà――a――ưm――\nƯm fu――sướng……lắm……sao?――a」`
- Sửa: `「Đến, mức đó……ưm――hà――a――ưm―― Ưm phù――sướng……lắm……sao?――a」`
- Lý do: んふっ còn "Ưm fu" — sửa thành "Ưm phù".
**Key 1201 (ポーレット)**
- JP: `「れりゅっ――りゅっ！　じゅるるるるっ――（ごくっ）\nぷあっ――ね、双鉄くん――ンッ――ちゅ、ちゅむっ！」`
- TW: `「滋嚕——嚕！滋嚕嚕嚕嚕——（吞嚥）噗啊——雙鐵君——嗯——啾、啾唔！」`
- VN cũ: `「Rê ryu——ryu! Chu ru ru ru——（Ực）\nPha——nè, anh Soutetsu——ưm——chu, chu mu!」`
- Sửa: `「Rộp——rộp! Rột——（Ực） Phà——nè, anh Soutetsu——ưm——chụt, chụt!」`
- Lý do: れりゅっ/りゅっ/じゅるるるるっ còn La-tinh — sửa thành "rộp"/"rộp"/"rột"; ぷあっ còn "Pha" — sửa thành "Phà"; ちゅ/ちゅむっ còn "chu"/"chu mu" — sửa thành "chụt"/"chụt".
**Key 1203 (ポーレット)**
- JP: `「れるっ――れろっ――りゅううっ――ニュルッ――\nちゅっ――ちゅむっ――ずじゅ――ずゅ――（こくっ）」`
- TW: `「滋溜——滋溜——溜嚕嚕——啾嚕——啾——啾嗯——滋溜——滋——（吞口水）」`
- VN cũ: `「Liếm――liếm――liếm――trơn tuột――\nChụt――chùn chụt――zuju――zu――（ực）」`
- Sửa: `「Rộp——rộp――rộộộp――trơn tuột―― Chụt――chụt――rột――rột——（ực）」`
- Lý do: れるっ/れろっ còn "Liếm" — sửa thành "rộp"/"rộp"; りゅううっ còn "liếm" — sửa thành "rộôôp" (3 tiếng u: りゅ+う×2); ちゅむっ còn "chùn chụt" — sửa thành "chụt"; ずじゅ/ずゅ còn "zuju"/"zu" — sửa thành "rột"/"rột".
**Key 1220 (ポーレット)**
- JP: `「はああっ！　あっ！　――んムッ！？　ちゅっ――\nれるっ――れりゅっ――ジュルっ――チュッ――ちゅう」`
- TW: `「蛤啊啊！啊！——嗯唔！？啾——滋溜——滋嚕——啾嚕——啾——啾唔」`
- VN cũ: `「Haaa! A! ——Ưm!? Chụt——\nrê ru——rê ryu——chu ru——chụt——chụt」`
- Sửa: `「Haaa! A! ——Ưm!? Chụt—— rộp——rộp——rột——chụt——chụụt」`
- Lý do: れるっ/れりゅっ còn "rê ru"/"rê ryu" — sửa thành "rộp"/"rộp"; ジュルっ còn "chu ru" — sửa thành "rột"; ちゅう cuối còn "chụt" không kéo dài — sửa thành "chụụt" (2 tiếng u: ちゅ+う).

### Âm thanh (độc thoại) (5 dòng)

**Key 1592 (monologue)**
- JP: `（ちゅっ――ぽっ）`
- TW: `（——拔出）`
- VN cũ: `（Chụt——Phụt）`
- Sửa: `（Chụt——Bụp）`
- Lý do: ぽっ là tiếng "bụp" (môi tách ra), không phải "phụt" (phun) — sửa thành "Bụp".
**Key 1610 (monologue)**
- JP: `（ぐいっ）`
- TW: `（ぐいっ）`
- VN cũ: `（Nhấc bổng）`
- Sửa: `（Giật mạnh）`
- Lý do: ぐいっ → "Giật mạnh" theo tài liệu SFX; "Nhấc bổng" sai nghĩa.
**Key 1711 (monologue)**
- JP: `（じゅぶううううっ！！！　ごちゅっ！！）`
- TW: `（深深一插！！！觸底！！）`
- VN cũ: `（Phập!!! Thúc mạnh!!）`
- Sửa: `（Phậậậậập!!! Thúc mạnh!!）`
- Lý do: じゅぶううううっ còn "Phập" không kéo dài — sửa thành "Phậậậập" (5 tiếng u: âm gốc + う×4); ごちゅっ→"Thúc mạnh" giữ nguyên (đúng).
**Key 1716 (monologue)**
- JP: `（にゅ、るっ――ぬ、るっ――にゅ、る――く、ちゅっ）`
- TW: `（滑來，滑去，蹭來，蹭去）`
- VN cũ: `（Trơn, tuột——Trượt, dài——Trơn, láng——Nhóp, nhép）`
- Sửa: `（Trơn, tuột——Trượt, trơn——Trơn, láng——Nhóp, nhép）`
- Lý do: "Trượt, dài" bịa thêm "dài" (JP không có) — sửa thành "Trượt, trơn".
**Key 1721 (monologue)**
- JP: `（ずゅぶっぅぅっ！！！）`
- TW: `（猛插！！！）`
- VN cũ: `（Phập!!!）`
- Sửa: `（Phậậập!!!）`
- Lý do: ずゅぶっぅぅっ còn "Phập" không kéo dài — sửa thành "Phậậập" (3 tiếng u: âm gốc + ぅ×2).

## Khối TOML để dán vào file (đã kiểm chứng parse được)

Khối dưới đây đã kiểm chứng parse được bằng tomllib, đúng 64 key, giá trị khớp đúng JSON bản sửa. Dán vào section `[script]` của file `03_Paulette/lr_ポーレットh1_家族旅行の最終日の夜.txt.toml` (ghi đè đúng 64 key này, giữ nguyên mọi key khác).

```toml
[script]
707 = "「――Tôi không muốn phá hỏng đêm yên bình của chuyến du lịch gia đình đâu. Em phải cố gắng kìm nén giọng nói đấy nhé?」"
712 = "「『Dễ che giấu hơn』. Đúng không? Tôi hiểu rồi」"
732 = "「……Vào một đêm như thế này, chúng mình sẽ lén lút, kìm nén giọng nói―― Nhưng chắc chắn……chúng mình sẽ làm tình――làm tình――ưm」"
953 = "「Nếu không phải là muốn tôi làm――thì là gì?」"
967 = "「Em muốn, tôi làm gì?」"
984 = "「Nhưng có một điều tôi chắc chắn.」"
998 = "「Kíuphù!!!? ~~~~~~~Ư!!!!」"
1000 = "「Hiau――ưm――phà――phù―― Chỗ cứng của, ngón tay――khớp xương――đang cọ, xát」"
1002 = "「Hiau!! Nhưng mà――sướng quá――ưm―― Anh Soutetsu――ưm――chỗ đó――chỗ đó」"
1003 = "「Hiau!? A――ưm! Hự――phà! Ưm a!!」"
1005 = "「Hia! A——ư——～～～～～Ư! Nhưng mà——thế này——cứ đâm lút cán là——em lại không kiềm được tiếng rên.」"
1007 = "「Hia! A!! Thế này! Em thích lắm!」"
1011 = "「Hia! A――Sướng quá――sướng quá, đi―― Ưm――Ngón tay, của anh Soutetsu――núm vú――của em――a」"
1019 = "「Phà――a――a――a――」"
1020 = "「Phà——a——nè——phà——nữa đi—— Anh Soutetsu——âm đạo——nữa đi——」"
1022 = "「Phà――a――Hơn cả ngón tay――em――ưm―― Muốn, chim――của anh Soutetsu, cơ」"
1023 = "「Phà――a! A! A! Hà! A――ưm――Khự――a!」"
1025 = "「Phà――ưm――（ực）――chụt――chụt Rộp――rộộộp――rột——chụụụt」"
1040 = "「Ư——～～～Ư——Ư! A——ưm—— chụt——chụụụụt——rột——（Ực）」"
1042 = "「ƯƯ～～! Ư——chụt——chụụt——ha—— rột——chụt——ư～～chụt——（Ực）」"
1043 = "「Ưm!?! Ưm——chụt——rột—— rộp——rộp——chụt——chụt——phà」"
1044 = "「Ư! Ư! Ư! ～～～～～Ư!!!」"
1045 = "「Ư!!! ～～～Ư!! Ư——a——ư!!!」"
1049 = "「A——ư——phà——a——bên trong——dương vật ——quy đầu——chạm vào——đầu em cũng, như muốn nổ tung——」"
1056 = "「A——chụt——chụt! Rộộộộp! Rộp! Trơn tuột! Chụt——chụụụt!」"
1058 = "「A——ưm——nhưng mà——phà, a—— nhưng mà, anh Soutetsu」"
1060 = "「A——ưm——rộp——chụt! Chụt! Chụụụt! Chụt! Rộp!!」"
1062 = "「A……chụt——chụt——ưm——phà. Ưm……ehehe——em cũng yêu anh. Anh Soutetsu」"
1065 = "「A……. Ưm――chụt――chụt――chụt, chụt――chụt――phà――rộp――trơn tuột」"
1072 = "「A――chụt――chụt――rột―― rột――chụt――rột~――（ực）」"
1073 = "「An」"
1074 = "「An!」"
1075 = "「An!!」"
1077 = "「Ư! ――Paulette」"
1082 = "「Chụt——chụt——rột——rộp—— Bụp——chụt——chụụụt——chụt」"
1083 = "「Chụt——ưm——chụụt——chụt——rộp—— rộp——rột——rột——chụt——Ư!?」"
1085 = "「Rột——（Ực）——chụt——chụt, chụt——chụt——rộp——chụt」"
1089 = "「Ưm——chụt——ư——ha——chụt—— chụụt——rộp——rộp——rộp——chụt」"
1096 = "「Ưm kyu——phà——a, thế này——thích quá—— ư ư——phu——nè——cứ thế này——nữa đi」"
1100 = "「Ưm! ――Phà――A――Ngón tay――ưm! Đột nhiên――hai, ngón――hi――a――」"
1108 = "「À, vậy thì mặc lại cũng khó chịu thật nhỉ. Xin lỗi em. Tôi cứ nghĩ làm trong lúc mặc đồ thì cách này là tốt nhất」"
1113 = "「Phà! A——ha——a——tuyệt quá—— âm đạo——tử cung——nhiều quá——đặc quá」"
1122 = "「Tuyệt lắm. Hoàn hảo lắm. Paulette——Tôi thích em. Tôi yêu em——ưm」"
1124 = "「Vâng……ưm――phà――Thật nhiều, thật nhiều―― Tinh trùng, em――sẽ nhận lấy――từ anh Soutetsu」"
1137 = "「Dương vật của tôi, sẽ khoét sâu, cọ xát, và gõ cửa. Rót tinh trùng vào tràn trề, ồ ạt」"
1140 = "「Tôi không định mở rộng nó ra bằng sức mạnh đâu. Chỉ là――」"
1144 = "「Tôi chỉ nghĩ, là từ nơi này. Toàn bộ sinh mệnh của Hikari đã được sinh ra từ nơi này」"
1149 = "「Tôi biết mà, Paulette. Nơi duy nhất tôi muốn rót trào lượng tinh dịch đã dồn nén bấy lâu nay, chỉ có thể là một chỗ mà thôi」"
1151 = "「Tôi đã định rủ em đi tắm rồi thay yukata…… và vài chuyện khác nữa cơ」"
1155 = "「Tôi chuyển động đây. Paulette」"
1169 = "「Đúng vậy. Mỗi lần chạm vào đó——tôi cũng bị siết chặt dữ dội.」"
1172 = "「Đúng vậy nhỉ. Sướng hơn trước kia rất nhiều. Tôi thậm chí còn có cảm giác như da thịt chúng ta đang hút chặt lấy nhau vậy」"
1184 = "「Đến, mức đó……ưm――hà――a――ưm―― Ưm phù――sướng……lắm……sao?――a」"
1190 = "「Không sao. Tôi có một phương án thay thế tuyệt vời.」"
1201 = "「Rộp——rộp! Rột——（Ực） Phà——nè, anh Soutetsu——ưm——chụt, chụt!」"
1203 = "「Rộp——rộp――rộộộp――trơn tuột―― Chụt――chụt――rột――rột——（ực）」"
1212 = "「Lần đầu tiên chúng ta ân ái, tôi đã kinh ngạc không ngờ trên đời này lại có thứ khoái cảm nhường này, nhưng」"
1220 = "「Haaa! A! ——Ưm!? Chụt—— rộp——rộp——rột——chụt——chụụt」"
1223 = "「Chà. Ai mà biết được. Chuyện đó thì tôi chịu thôi.」"
1592 = "（Chụt——Bụp）"
1610 = "（Giật mạnh）"
1711 = "（Phậậậậập!!! Thúc mạnh!!）"
1716 = "（Trơn, tuột——Trượt, trơn——Trơn, láng——Nhóp, nhép）"
1721 = "（Phậậập!!!）"
```

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- **B4 — tên rên trần:** file này có **0 dòng** tên "Soutetsu" bị rên/gọi trần. Không có bằng chứng mới cho B4 từ file này.
- **Cười khúc khích (đề xuất mới):** 3 dòng trong file này còn giữ dạng La-tinh cho tiếng cười — 1062 `えへへ` → "ehehe", 1088 `ふふっ` → "fufu", 1181 `うふふ` → "ufufu". h8 từng dùng "Ư hự" cho ふふっ (2360) nhưng đó là quy ước riêng của file h8 (các dòng đúng trong h8 dùng "Ư hự hự" cho うふふ) và "Ư hự" là tiếng gằn, không phải tiếng cười — KHÔNG áp dụng ở đây. Cần Hieu quyết: giữ nguyên dạng La-tinh, hay dùng "phì phì"/"hì hì". ("Ahaha" là tiếng cười chuẩn trong tiếng Việt; "Ehehe" cũng được dùng trong văn bản Việt để chỉ cười khúc khích.)
- **Quy ước độ dài âm kéo dài (đã chốt trong lần kiểm tra này):** số nguyên âm VN = 1 (âm gốc) + số ký tự う/ぅ trong token JP. Bằng chứng: h7 1651 (う×10 → 11 chữ u); mọi token trong 2 file lr đều khớp. h7 1684 (う×8 → 8 chữ u) là ngoại lệ, nhiều khả năng là lỗi đếm của h7 — không theo. Các dòng đã sửa theo quy tắc này trong file này: 1711 (じゅぶううううっ: う×4 → 5 nguyên âm "Phậậậậập"), 1721 (ずゅぶっぅぅっ: ぅ×2 → 3 nguyên âm "Phậậập"), 1042/1083/1089 (ちゅうっ: う×1 → 2 nguyên âm "chụụt").
- **Quy ước họ SFX áp dụng trong file này:** âm hôn ちゅ/ぢゅ đầu → "chụt"; âm đâm/trượt じゅ/ず → "rột" (trượt) hoặc "Phập" (đâm vào, với ず đầu); âm lưỡi れる/りゅ/れろ/れりゅ → "rộp"; にゅる/ニュル → "Trơn tuột!" (quy ước riêng của file — các dòng đúng trong file đều dùng vậy); にゅむる/にゅっ → "rột"; にゅぶっ → "Bụp" trong chuỗi miệng (1082), nhưng "Đâm vào" trong chuỗi đâm độc thoại khi TW ghi 插入 (1696/1735 — theo ngữ cảnh, có TW chứng); ぢゅぼ/ぢゅば → "Bụp"; ぐちゅ/ごちゅ → "Rột"; ぼちゅ → "Chụt"; ぽっ → "Bụp"; ぐいっ → "Giật mạnh" (theo tài liệu SFX); ぱくっ → "Ngoạm" (theo tài liệu SFX); くっ → "Hự"; んくっ → "Ưm hự"; んふっ → "Ưm phù"; んぷっ → "ưm bụp"; ぷっ → "Bụp"; んむっ → "ưm mự"; んひっ → "ưm hì"; くふっ → "Khự"; くひゅっ → "Khíu"; おうふっ → "Ồ phù"; ぷあっ/ぷぁ → "Phà"; ふぁんっ → "phàn"; はぷっ → "Hà bụp"; ぷはっ → "Bụp ha"; ひあ → "Hia" (không phải "Hya", theo h8 2136); ひゃう → "Hiau" (không phải "Hya", theo h8 2137); きゅ → "Kíu" (theo h8 2142); あんっ → "An" (giữ phụ âm mũi ん — VN cũ bỏ mất). Hơi thở cụt "phu" (bị cắt bởi ――) được chấp nhận (1026). はっ → "Hà"/"Ha" đều chấp nhận (chỉ khác sắc thái, không tính sai). Phạm vi kéo dài: chỉ kéo dài từ âm đơn tiết (chụt, rột, rộp, Phập) và từ miêu tả rõ ràng kéo dài được (sâu); KHÔNG kéo dài cụm miêu tả hai từ (rút ra, đẩy vào, lút cán) hay tiếng trượt đa âm tiết chỉ có một う cuối (ぢゅるるうっ → "rột", không kéo dài).

## Đề xuất cập nhật context (chưa chốt)

- **Tiếng cười khúc khích:** cần quyết định chung cho toàn dự án — các dòng ふふ/うふふ/えへへ/あはは đang bị La-tinh hoá ở nhiều file (file này 3 dòng, lr_h2 8 dòng). Ứng viên: giữ La-tinh, hoặc "phì phì"/"hì hì".
- **Quy tắc độ dài âm kéo dài:** ghi vào context — số nguyên âm VN = 1 + số ký tự う/ぅ trong token JP (bằng chứng h7 1651 + toàn bộ token lr). h7 1684 là ngoại lệ cần ghi chú.

## Đã kiểm tra và KHÔNG tính là sai

- 1015: っ trần → "Ưm" — cách xử lý hợp lý, không tính sai.
- 1018/1098: ふえっ → "Hả!?" — thán từ ngạc nhiên, hợp lý.
- 1026: "phu" — hơi thở bị cắt cụt bởi ――, chấp nhận.
- 1086: はっ → "hà" — chỉ khác sắc thái, không tính sai.
- 1097: んきゅっ → "Ưm kyu" — đúng theo h7.
- 1062/1088/1181: tiếng cười La-tinh — ghi vào đề xuất (xem trên), không tính là sai trong audit này.
- VN trùng trong file đều hợp lý, JP khác nhau: 「A」1068/1073, 「Ừ」1094/1175, 「Ưm!」1099/1102.
- 1215 "Giọng em kìa" — cách dịch tự do chấp nhận được.
- 1218 "Anh, Soutetsu" — dấu phẩy ngắt nhịp, không phải tên trần.
- 1706: chỉ là ghi chú mỹ thuật về ngoặc (JP có cả ngoặc nửa độ rộng và đầy độ rộng `(とさっ）`, VN `(Đè xuống)`) — ghi nhận ở đây, KHÔNG đưa vào khối sửa.
- Độc thoại xưng "cô ấy"/"em ấy" (1427, 1459, 1531) là ngôi thứ ba, không phải cách gọi — không tính sai.
- "mình" trong độc thoại 1455/1457/1469/1472/1526 đều là phản thân/sở hữu — đúng.
- 979: "anh" là lời Paulette thuật lại (cô ấy xưng hô với Soutetsu), không phải Soutetsu tự xưng — không tính sai, không tính vào đếm "em"/"cô".

## Kết bài

File lr_h1: 303 dòng đã đọc, 64 dòng sai (21,1%) — 18 xưng hô, 1 nghĩa sai, 3 gasp, 37 hơi thở/âm thanh thoại, 5 âm thanh độc thoại. Không lệch vị trí, không xoay vòng, không tràn chương — toàn bộ lỗi đều tại chỗ và đã có bản sửa viết tay, kiểm tra lần hai đầy đủ. Hai họ lỗi chính là Soutetsu tự xưng "anh" (18 dòng, lỗi hệ thống quen thuộc) và âm thanh/hơi thở còn La-tinh (42 dòng, họ lỗi lớn nhất của file). Quy tắc độ dài âm kéo dài đã được chốt bằng bằng chứng h7 1651 và toàn bộ token trong file: số nguyên âm VN = 1 + số ký tự う/ぅ trong JP. Tiếng cười khúc khích (3 dòng) và quy tắc độ dài âm là hai đề xuất mới cần Hieu quyết. Cùng với lr_h2, 03_Paulette đã audit xong toàn bộ (lr_稀咲h1 và れいな02 đã được audit song song — xem ROUTE-AUDIT).
