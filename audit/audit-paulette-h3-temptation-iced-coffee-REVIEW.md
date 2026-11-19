# Audit: Paulette h3_誘惑アイスコーヒー — 69 dòng Việt sai (đã đối chiếu JP + TW)

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa từng dòng: 279 dòng (độc thoại 157, Paulette 75, Soutetsu H 47), đối chiếu JP + TW từ CSV3 và TOML-2.
- CSV vs TOML: 0 khác biệt thực chất (155 khác biệt thô chỉ ở `\n`/khoảng trắng); tập key bằng nhau (279); `[selections]` rỗng; thẻ `%l`: 0 hỏng; không có key trùng; không có dòng VN trống; VN==TW 0.
- md5: `884568f018ff870371ba906804c8651c` — không trùng với bất kỳ file nào trong 227 file TOML (không có bản sao; bản sửa áp dụng cho 1 file duy nhất).
- Heuristic dấu thoại ↔ lời dẫn: shift 0 đạt 246/279 — 33 dòng không khớp loại (thoại/lời dẫn/SFX) là dấu hiệu đầu tiên của cụm lệch vị trí; 12 dòng lệch còn lại là lệch cùng loại (thoại↔thoại, lời dẫn↔lời dẫn, SFX↔SFX) nên heuristic không bắt được, phải tra chỉ mục Việt mới tìm ra.
- Đọc lần đầu phát hiện 30/69 dòng; các kiểm tra hệ thống phát hiện thêm 39 dòng: cờ cấu trúc (dấu thoại/ngoặc không khớp) + quét từ khóa 30 dòng lệch, tra chỉ mục Việt toàn dự án 4 dòng (900, 1011, 1676, 1682), heuristic shift-0 1 dòng (1658), rà soát chéo với đợt quét gasp っ 4 dòng thở gấp (934, 935, 954, 1639).
- Rà soát chéo với sweep gasp っ: sweep xác nhận 6/6 bản sửa thở gấp của audit (907, 908, 934, 935, 954, 1639 — cùng giá trị sửa); audit không phát hiện thêm dòng gasp nào mà sweep bỏ sót trong file này.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ 69/69 bản sửa đối chiếu JP (đúng 69, 0 bị loại). Trong kiểm tra lần hai đã sửa lại: bản Việt phục hồi tại 1026 mang lỗi xưng hô gốc ("Anh cũng / anh vẫn muốn" → "Tôi cũng / tôi vẫn muốn", JP 僕); 10 bản sửa có khoảng trắng thừa trước `\n`; 15 bản sửa dùng dấu 。 thay cho dấu . của bản cũ — tất cả đã sửa về đúng dạng bản cũ, chỉ đổi đúng phần lỗi.

## Kết luận về cơ chế lỗi

- Lệch vị trí là lỗi chủ đạo: 45/279 (16,1%) — nặng nhất trong các file Paulette h từ trước tới nay, và là chuỗi xoay vòng nội bộ thứ tư của dự án (sau narukonotown và hai file Paulette 05). Không phải một lần dịch chuyển đơn giản: các mắt xích có độ lệch khác nhau, tạo thành 6 chuỗi + 1 nhánh + 1 dòng riêng lẻ. 38/45 đã phục hồi từ chính file này (bản Việt đúng của JP đó đang nằm ở một key khác trong cùng file); 7 dòng không tìm thấy bản dịch đúng trong file nên dịch mới từ JP (982, 1461, 1641, 1658, 1673, 1676, 1682).
- Các chuỗi (mũi tên đọc từ phải sang trái là dòng chảy của bản dịch bị lệch; key ở đầu chuỗi là dòng được dịch mới):
  - Chuỗi A — 15 mắt, đầu 1676 dịch mới: 1676 → 1362 → 1500 → 1664 → 904 → 1366 → 1349 → 1011 → 1006 → 1018 → 1235 → 1495 → 890 → 1356 → 1536 → 1052.
  - Chuỗi B — 10 mắt, đầu 1641 dịch mới, nhánh 1642 ← 919: 1641 → 900 → 1026 → 1643 → 972 → 1468 → 937 → 1369 → 1454 → 1645 → 919.
  - Chuỗi C — 4 mắt, đầu 1673 dịch mới: 1673 → 995 → 1376 → 1306 → 1062.
  - Chuỗi D — 2 mắt, đầu 1682 dịch mới: 1682 → 1494 → 703.
  - Chuỗi E — 2 mắt, đầu 982 dịch mới: 982 → 1359 → 1488.
  - Chuỗi F — 2 mắt, đầu 1461 dịch mới, nhánh 899 ← 1650 ← 872: 1461 → 1293 → 872.
  - Riêng lẻ: 1658 (dịch mới, không có mắt nối).
- Cụm lệch tập trung ở 4 khoảng: 870–1070 (thoại ↔ lời dẫn), 1230–1380 (lời dẫn), 1450–1500 (lời dẫn), 1640–1690 (cụm SFX).
- 7 bản Việt mồ côi không có JP tương ứng trong file (VN tại 703, 899, 1052, 1062, 1488, 1642, 1658) — nguồn gốc ngoài file chưa tra; ghi nhận để kiểm tra sau. Không có bằng chứng tràn chương từ file khác vào h3.
- Xưng hô hệ thống: Soutetsu tự xưng "anh" trong thoại/H 15/15 lần (0 lần "Tôi" trước khi sửa; toàn bộ thoại Soutetsu chỉ có 1 lần "tôi" duy nhất) — cùng lỗi hệ thống như h1/h2. Paulette gọi Soutetsu bằng tên trần trong câu nói: 3 dòng (986, 1016, 1071).
- Thở gấp: 6 dòng mất tiếng hít っ (907, 908, 934, 935, 954, 1639) — 4/6 do sweep bắt được khi rà soát chéo.

### Quy tắc tên trần vs tên rên — tinh chỉnh từ h3 (áp dụng trong file này, để Hieu duyệt lại)

- 986 và 1071 KHÔNG phải tên rên: 986 là câu cảm ơn nói hoàn chỉnh ("cảm ơn Soutetsu nhé!"), 1071 là câu hỏi mở đầu bằng cách gọi tên ("Soutetsu... Anh vẫn nhớ...?") — cả hai đều đã sửa thành "anh Soutetsu". Ngoại lệ "tên rên giữ nguyên" chỉ áp dụng cho tên bị rên/thở gấp trong lúc thân mật (tên đứng một mình kèm tiếng rên), không áp dụng cho cách gọi tên trong câu nói giao tiếp bình thường. h3 có 0 dòng tên rên giữ nguyên.

## Chi tiết dòng sai

### Lệch vị trí (45 dòng)

**Key 703 (monologue)**
- JP: `……だから意識が、引き寄せられる。\nもう一箇所の、震えヒクつくピンクのかわいいすぼまりに。`
- TW: `……所以我的意識被另一個地方吸引了。我看上了另一個不安分的可愛小洞。`
- VN cũ: `（Mơn trớnnnnn）`
- Sửa: `……Thế nên ý thức của tôi bị thu hút.\nVào một nơi khác, một lỗ nhỏ màu hồng dễ thương đang co giật run rẩy.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1494 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 872 (ポーレット)**
- JP: `「双鉄、くんの――精液――子宮、に――んっ――\nおまん、こに――もらう、のが――、一番、だからっ――」`
- TW: `「你的精液——還是用子宮——來收下——最好——」`
- VN cũ: `（Phập!）`
- Sửa: `「Tinh dịch——của anh Soutetsu——nhận vào, tử cung——ưm——\nVào cô bé——vẫn là, tuyệt nhất, nên là——」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1293 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 890 (ポーレット)**
- JP: `「やっっ――あっ――ンッッ――わたしの、アナ、ル――\n双鉄、くんに――広げ……られ、て――んうっっ――」`
- TW: `「呀——啊——嗯——我的屁眼——被你撐開了——嗯——」`
- VN cũ: `Tôi kéo nhẹ phần thịt xung quanh,\nnong rộng lỗ hậu dễ thương ra một chút.`
- Sửa: `「Á——a——ưm——lỗ, hậu, của em——\nBị anh Soutetsu——nong……rộng, ra——ưm——」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1495 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 899 (ポーレット)**
- JP: `「ひゃああああああんっ！！」`
- TW: `「呀啊！！」`
- VN cũ: `（Siếttttttt!）`
- Sửa: `「Hyaaaaaaa!!」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1650 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 900 (ポーレット)**
- JP: `「くひゅっ！」`
- TW: `「呀！」`
- VN cũ: `「Đúng vậy nhỉ——Anh cũng——, tuyệt nhất là——\nTuyệt nhất là——anh vẫn muốn làm thế——」`
- Sửa: `「Á!」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1641 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 904 (ポーレット)**
- JP: `「ひゃっ！？　あっ――お尻――んっ――アナ、ル――\nわ、わたし――自分で、したこと――なく、て――んっ」`
- TW: `「呀！？啊——屁股——嗯——屁眼——我自己——沒有摸過——嗯——」`
- VN cũ: `Ngón tay không đút vào.\nCũng chưa chạm trực tiếp vào hậu môn.`
- Sửa: `「Á!? A——mông——ưm——lỗ, hậu——\nE, em——chưa từng, tự làm——bao giờ——ưm」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1664 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 919 (ポーレット)**
- JP: `「ふあっ――あっ――ふか、いっ――これっ――\nんっ――すごい――おな、か――ささる、みたい、でっ」`
- TW: `「呼啊——啊——好深啊——這樣——嗯——好厲害——好像——刺到肚子裡」`
- VN cũ: `（Phập! Phập! Phập! Nhóp nhép!）`
- Sửa: `「Phù——a——sâu, quá——thế này——\nƯm——sướng quá——cảm giác, như đâm, vào tận bụng, vậy」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1645 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 937 (ポーレット)**
- JP: `「ぁっ――双鉄くん、のっ――いつも、よりっ――\nふあっ――ふと、くてっ――めくれ、てっ――あっ」`
- TW: `「啊——你的——比平常——呼啊——還要粗大——在裡面挖著——啊」`
- VN cũ: `Dù vậy, hông tôi vẫn không dừng lại.`
- Sửa: `「A——của anh Soutetsu——to hơn, bình thường——\nPhù——to, quá——bị nong rộng, ra——a」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1468 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 972 (ポーレット)**
- JP: `「はいっ――してっ！　してっ、くださ――んっ――\nわたしの――、一番――おく、にっ――精、液っ」`
- TW: `「嗯——來吧！來吧，給我吧——在我身體最深處——射出精液——」`
- VN cũ: `Không biết có phải do kích thích lỗ hậu hay không,\nâm đạo của Paulette trơn ướt và quấn chặt hơn bình thường.`
- Sửa: `「Vâng——làm đi! Hãy làm, đi ạ——ưm——\nBắn tinh dịch——vào sâu, nhất——bên trong, em đi」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1643 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 982 (ポーレット)**
- JP: `「くひゅんっ！　ふやっ――」`
- TW: `「嗯啊！呼呀——」`
- VN cũ: `Thử dập hông vào sâu hơn,\ncơ thể Paulette lại run lên bần bật.`
- Sửa: `「Hí——phù——」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; không tìm thấy bản dịch đúng của JP này trong file (đã tra toàn bộ chỉ mục Việt) — dịch mới từ JP.

**Key 995 (双鉄H)**
- JP: `「痛っ――」`
- TW: `「好疼」`
- VN cũ: `Đầu ngón tay vừa thử đút vào,\nđã bị hậu môn siết chặt dữ dội như muốn đẩy ra.`
- Sửa: `「Đau——」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1673 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1006 (双鉄H)**
- JP: `「お尻でも、性の快感を得ることは出来るのだな」`
- TW: `「屁股也能獲得性快感」`
- VN cũ: `「Thì……em cũng có nghe——người ta, nói, vậy——ưm——\nNhưng, mà——thực tế——lại đến mức này, thì——a——á」`
- Sửa: `「Ngay cả ở mông, cũng có thể đạt được khoái cảm tình dục nhỉ.」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1011 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1011 (ポーレット)**
- JP: `「知らない――です――だから――こん、なのっ――\nふっ――あっ――おし、りっ――こんなに、感じる、の」`
- TW: `「我不知道——這樣——呼――啊――屁股——也能這麼舒服——」`
- VN cũ: `「Ngay cả ở mông, cũng có thể đạt được khoái cảm tình dục nhỉ.」`
- Sửa: `「Em không biết——đâu——nên là——như thế này——\nPhù——a——mông——lại có cảm giác, như vậy」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1349 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1018 (ポーレット)**
- JP: `「って……話では――聞いて、た、けど――んっ――\nだけ、ど――実際――これほど、だと――かっ――あっ」`
- TW: `「我是……聽說過——嗯——但是——沒想到——實際會——這麼刺激——啊」`
- VN cũ: `Lỗ hậu môn đang co bóp nhấp nháy.`
- Sửa: `「Thì……em cũng có nghe——người ta, nói, vậy——ưm——\nNhưng, mà——thực tế——lại đến mức này, thì——a——á」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1006 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1026 (双鉄H)**
- JP: `「そうだな――僕も――、一番はっ――\n一番は――やはり、そうしたいっ――」`
- TW: `「是啊——我也覺得最好——最好還是這樣——」`
- VN cũ: `（Phập——phập——nhóp——nhép——）`
- Sửa: `「Đúng vậy nhỉ——Tôi cũng——, tuyệt nhất là——\nTuyệt nhất là——tôi vẫn muốn làm thế——」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 900 trong cùng file — phục hồi từ đó, đồng thời sửa xưng hô gốc "Anh cũng / anh vẫn muốn" → "Tôi cũng / tôi vẫn muốn" (JP 僕).

**Key 1052 (双鉄H)**
- JP: `「アナルで……セックスしてみるか？」`
- TW: `「要不要試試……用後門做愛？」`
- VN cũ: `（Phụt）`
- Sửa: `「Có muốn thử làm tình……bằng lỗ hậu không?」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1536 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1062 (ポーレット)**
- JP: `「あの……アナルも――わたし、興味……\nいきなり、すごく――出てきちゃった――です、けど」`
- TW: `「那個……屁眼——我也突然……有點興趣了——但是」`
- VN cũ: `（Siếtttt!）`
- Sửa: `「Cái đó……lỗ hậu——tự nhiên, em……\nCũng cảm thấy rất có hứng thú——nhưng mà」`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1306 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1235 (monologue)**
- JP: `アナルが、ぱくぱく動いてる。`
- TW: `可愛的菊穴一張一合。`
- VN cũ: `Trông như thể nó đang đòi hỏi ngón tay tôi,\nđang cầu xin tôi đút vào vậy.`
- Sửa: `Lỗ hậu môn đang co bóp nhấp nháy.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1018 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1293 (monologue)**
- JP: `顔を真っ赤に染めながら、\n体で、言葉で、ポーレットは僕に伝えてくれる。`
- TW: `她紅著臉用身體的動作和語言向我表達著想法。`
- VN cũ: `「Tinh dịch——của anh Soutetsu——nhận vào, tử cung——ưm——\nVào cô bé——vẫn là, tuyệt nhất, nên là——」`
- Sửa: `Khuôn mặt đỏ bừng,\nPaulette truyền đạt cho tôi bằng cả cơ thể lẫn lời nói.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1461 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1306 (monologue)**
- JP: `今のが、僕の勃起なら――\n思えばひゅんと、玉が縮こまってしまいさえする。`
- TW: `如果這是把肉棒插進去——光是想想，我的睪丸就不禁嚇得縮了一下。`
- VN cũ: `「Cái đó……lỗ hậu——tự nhiên, em……\nCũng cảm thấy rất có hứng thú——nhưng mà」`
- Sửa: `Nếu vừa rồi là dương vật của tôi thì——\nNghĩ đến thôi cũng khiến hai hòn bi sun lại.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1376 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1349 (monologue)**
- JP: `ただただひたすら、一番すぼまる部分のまわりを、\n回すように、揉み込むようにして刺激していく。`
- TW: `我只是在肉洞周圍劃來劃去，按壓著施加刺激。`
- VN cũ: `「Em không biết——đâu——nên là——như thế này——\nPhù——a——mông——lại có cảm giác, như vậy」`
- Sửa: `Chỉ đơn thuần kích thích xung quanh phần lõm vào nhất,\nnhư thể đang xoa tròn, nắn bóp.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1366 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1356 (monologue)**
- JP: `周辺の肉を引くようにして、\nかわいいアナルをわずかに広げる。`
- TW: `我抓著可愛菊穴周圍的臀肉把它稍稍撐開。`
- VN cũ: `Có vẻ như độ co giãn khá tốt.\nHơn nữa, nó còn đang ngọ nguậy như thèm khát——`
- Sửa: `Tôi kéo nhẹ phần thịt xung quanh,\nnong rộng lỗ hậu dễ thương ra một chút.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 890 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1359 (monologue)**
- JP: `腰を突き出し抉ってみれば、\nポーレットはまたぶるりと大きく体を震わす。`
- TW: `我用力向上一頂，波萊特的身體又劇烈痙攣了一下。`
- VN cũ: `Cứ thế cô ấy lả đi, mất hết sức lực.\nCó vẻ như chỉ việc chống đỡ cơ thể mình thôi cũng đã tốn hết sức rồi.`
- Sửa: `Thử dập hông vào sâu hơn,\ncơ thể Paulette lại run lên bần bật.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 982 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1362 (monologue)**
- JP: `おまんこの蜜を絡めた指で尻穴の周りを撫ぜれば、\nポーレットの膣がきゅうっと締まる。`
- TW: `我用沾滿蜜汁的手指輕撫菊穴的附近，波萊特的蜜道馬上收緊了一下。`
- VN cũ: `Thật dễ chịu——và cũng thật thú vị.\nGiọng nói của Paulette cũng không chỉ đơn thuần là kinh ngạc.`
- Sửa: `Dùng ngón tay thấm đẫm mật ngọt từ cô bé vuốt ve quanh lỗ hậu,\nâm đạo của Paulette lập tức co thắt lại.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1676 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1366 (monologue)**
- JP: `指は、挿れない。\n肛門そのものにもまだ触れてない。`
- TW: `我的手指並沒有插進去，而且也沒有碰到肛門本身。`
- VN cũ: `Chỉ đơn thuần kích thích xung quanh phần lõm vào nhất,\nnhư thể đang xoa tròn, nắn bóp.`
- Sửa: `Ngón tay không đút vào.\nCũng chưa chạm trực tiếp vào hậu môn.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 904 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1369 (monologue)**
- JP: `それでも、腰は止まらない。`
- TW: `我的活塞運動已經停不下來。`
- VN cũ: `Hơi thở của tôi và Paulette,\nnhịp điệu của cả hai dần hòa làm một.`
- Sửa: `Dù vậy, hông tôi vẫn không dừng lại.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 937 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1376 (monologue)**
- JP: `試みにいれた指先を、\nけれど肛門は強烈な締めで排除しようと試みてくる。`
- TW: `我試著把手指插進去，然而肛門馬上就強烈收縮，試圖排除異物。`
- VN cũ: `Nếu vừa rồi là dương vật của tôi thì——\nNghĩ đến thôi cũng khiến hai hòn bi sun lại.`
- Sửa: `Đầu ngón tay vừa thử đút vào,\nđã bị hậu môn siết chặt dữ dội như muốn đẩy ra.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 995 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1454 (monologue)**
- JP: `ポーレットと僕、ふたりの呼吸が、\nリズムが徐々に、一致していく。`
- TW: `波萊特和我的呼吸和節奏漸漸同步起來。`
- VN cũ: `（Nhóp! Nhép! Nhóp! Nhép!!）`
- Sửa: `Hơi thở của tôi và Paulette,\nnhịp điệu của cả hai dần hòa làm một.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1369 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1461 (monologue)**
- JP: `ポーレットの腰が大きく動く。`
- TW: `波萊特用力動了一下腰。`
- VN cũ: `Khuôn mặt đỏ bừng,\nPaulette truyền đạt cho tôi bằng cả cơ thể lẫn lời nói.`
- Sửa: `Hông Paulette chuyển động mạnh.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; không tìm thấy bản dịch đúng của JP này trong file (đã tra toàn bộ chỉ mục Việt) — dịch mới từ JP.

**Key 1468 (monologue)**
- JP: `アナルを刺激したせいなのか、\nポーレットの膣はいつもよりぬらつき、絡みついてくる。`
- TW: `波萊特的蜜道更加濕潤更加緊緻了，不知道是不是因為我剛才刺激了她的菊穴。`
- VN cũ: `「A——của anh Soutetsu——to hơn, bình thường——\nPhù——to, quá——bị nong rộng, ra——a」`
- Sửa: `Không biết có phải do kích thích lỗ hậu hay không,\nâm đạo của Paulette trơn ướt và quấn chặt hơn bình thường.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 972 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1488 (monologue)**
- JP: `そのままくったり、力が抜ける。\n自分の体を支えるだけで、精一杯な様子に見える。`
- TW: `然後她的身體漸漸脫力，光是支撐著自己似乎就已經很費力了。`
- VN cũ: `（Thế này thì——）`
- Sửa: `Cứ thế cô ấy lả đi, mất hết sức lực.\nCó vẻ như chỉ việc chống đỡ cơ thể mình thôi cũng đã tốn hết sức rồi.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1359 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1494 (monologue)**
- JP: `体勢的に、僕から大きくは動けない。\n快感の波が落ち着くまでは、ポーレットも動けそうにない。`
- TW: `現在的姿勢的話我的活動範圍很小。波萊特在快感減弱之前大概也不會動起來了。`
- VN cũ: `……Thế nên ý thức của tôi bị thu hút.\nVào một nơi khác, một lỗ nhỏ màu hồng dễ thương đang co giật run rẩy.`
- Sửa: `Với tư thế này, tôi không thể cử động mạnh được.\nCho đến khi cơn sóng khoái cảm dịu xuống, Paulette có lẽ cũng không thể nhúc nhích.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1682 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1495 (monologue)**
- JP: `指が欲しいと、挿れてほしいと、\nおねだりしているようにも見える。`
- TW: `看起來就像是在求我的手指插進去。`
- VN cũ: `「Á——a——ưm——lỗ, hậu, của em——\nBị anh Soutetsu——nong……rộng, ra——ưm——」`
- Sửa: `Trông như thể nó đang đòi hỏi ngón tay tôi,\nđang cầu xin tôi đút vào vậy.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1235 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1500 (monologue)**
- JP: `気持ちがいい――し、面白い。\nポーレットの声も、驚いているだけじゃない。`
- TW: `真的是很爽快又有趣。波萊特的嬌喘中也不只帶著驚訝之意。`
- VN cũ: `（Nhóp——nhép——trơn——tuột——）`
- Sửa: `Thật dễ chịu——và cũng thật thú vị.\nGiọng nói của Paulette cũng không chỉ đơn thuần là kinh ngạc.`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1362 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1536 (monologue)**
- JP: `柔軟性は、相当ありそうな印象だ。\nそれに、欲しそうにうごめいてるし――`
- TW: `菊穴看起來相當柔軟。而且它還在蠢蠢欲動——`
- VN cũ: `「Có muốn thử làm tình……bằng lỗ hậu không?」`
- Sửa: `Có vẻ như độ co giãn khá tốt.\nHơn nữa, nó còn đang ngọ nguậy như thèm khát——`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1356 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1641 (monologue)**
- JP: `（ずんっ！）`
- TW: `（啪）`
- VN cũ: `「Á!」`
- Sửa: `（Thịch!）`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; không tìm thấy bản dịch đúng của JP này trong file (đã tra toàn bộ chỉ mục Việt) — dịch mới từ JP.

**Key 1642 (monologue)**
- JP: `（ぱぢゅっ！　ぱちゅっ！　ぱちゅんっ！　じゅぶっ！）`
- TW: `（啾啪！啾啪！啾噗！啾噗！）`
- VN cũ: `「A——không được——em——lại——\nLại——ra——ra mất!!」`
- Sửa: `（Phập! Phập! Phập! Nhóp nhép!）`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 919 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1643 (monologue)**
- JP: `（ずっ――ずぶっ――ぶじゅ――じゅぶっ――）`
- TW: `（啾噗——啾噗——啾啪——啾啪——）`
- VN cũ: `「Vâng——làm đi! Hãy làm, đi ạ——ưm——\nBắn tinh dịch——vào sâu, nhất——bên trong, em đi」`
- Sửa: `（Phập——phập——nhóp——nhép——）`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1026 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1645 (monologue)**
- JP: `（じゅぶっ！　じゅっ！　じゅずっ！　じゅぶっ！！）`
- TW: `（啾噗！啾噗！啾嚕！啾嚕！）`
- VN cũ: `「Phù——a——sâu, quá——thế này——\nƯm——sướng quá——cảm giác, như đâm, vào tận bụng, vậy」`
- Sửa: `（Nhóp! Nhép! Nhóp! Nhép!!）`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1454 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1650 (monologue)**
- JP: `（くぷっ）`
- TW: `（噗呲）`
- VN cũ: `「Hyaaaaaaa!!」`
- Sửa: `（Phập!）`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 872 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1658 (monologue)**
- JP: `（ずりゅうううっ！）`
- TW: `（夾緊）`
- VN cũ: `Hông Paulette giật mạnh.`
- Sửa: `（Sụttt!）`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; không tìm thấy bản dịch đúng của JP này trong file (đã tra toàn bộ chỉ mục Việt) — dịch mới từ JP.

**Key 1664 (monologue)**
- JP: `（ぬろっ――ぬとっ――ぬるっ――ぬるるっ――）`
- TW: `（摸來摸去）`
- VN cũ: `「Á!? A——mông——ưm——lỗ, hậu——\nE, em——chưa từng, tự làm——bao giờ——ưm」`
- Sửa: `（Nhóp——nhép——trơn——tuột——）`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; bản dịch đúng của JP này đang nằm ở key 1500 trong cùng file (đã đối chiếu JP/TW) — phục hồi từ đó.

**Key 1673 (monologue)**
- JP: `（ギチチチチチチっ！）`
- TW: `（箍緊）`
- VN cũ: `「Đau——」`
- Sửa: `（Kítttttt!）`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; không tìm thấy bản dịch đúng của JP này trong file (đã tra toàn bộ chỉ mục Việt) — dịch mới từ JP.

**Key 1676 (monologue)**
- JP: `（ぬろおおおおっ）`
- TW: `（輕撫）`
- VN cũ: `Dùng ngón tay thấm đẫm mật ngọt từ cô bé vuốt ve quanh lỗ hậu,\nâm đạo của Paulette lập tức co thắt lại.`
- Sửa: `（Trơn tuộtttt）`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; không tìm thấy bản dịch đúng của JP này trong file (đã tra toàn bộ chỉ mục Việt) — dịch mới từ JP.

**Key 1682 (双鉄H)**
- JP: `（これは――）`
- TW: `（這樣的話——）`
- VN cũ: `Với tư thế này, tôi không thể cử động mạnh được.\nCho đến khi cơn sóng khoái cảm dịu xuống, Paulette có lẽ cũng không thể nhúc nhích.`
- Sửa: `（Đây là——）`
- Lý do: Lệch vị trí: bản Việt hiện tại thuộc về dòng khác; không tìm thấy bản dịch đúng của JP này trong file (đã tra toàn bộ chỉ mục Việt) — dịch mới từ JP.

### Xưng hô (18 dòng)

**Key 705 (双鉄H)**
- JP: `「――僕のミルクを、好きなだけ絞り出すといい」`
- TW: `「——我的牛奶，你想榨多少就榨多少吧」`
- VN cũ: `「——Em cứ vắt bao nhiêu sữa của anh tùy thích.」`
- Sửa: `「——Em cứ vắt bao nhiêu sữa của tôi tùy thích.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 864 (双鉄H)**
- JP: `「いや、\n礼をいわれるべきは僕ではなく、汰斗さんだろう」`
- TW: `「不用，要謝的不是我，而是汰斗先生吧」`
- VN cũ: `「Không,\nngười đáng được cảm ơn không phải là anh, mà là ông Taito chứ.」`
- Sửa: `「Không,\nngười đáng được cảm ơn không phải là tôi, mà là ông Taito chứ.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 980 (双鉄H)**
- JP: `「ああ。具体的には、僕の視線を自覚しつつも、\n偶然を装って誘惑をかける、そんな姿を見てみたい」`
- TW: `「嗯。具體來說，就是你一邊在意著我的視線，一邊裝作是偶然來誘惑我，我想看這樣的你」`
- VN cũ: `「Ừ. Cụ thể là, anh muốn xem cái dáng vẻ em vừa ý thức được ánh nhìn của anh,\nvừa giả vờ như tình cờ để quyến rũ anh ấy.」`
- Sửa: `「Ừ. Cụ thể là, tôi muốn xem cái dáng vẻ em vừa ý thức được ánh nhìn của tôi,\nvừa giả vờ như tình cờ để quyến rũ tôi.」`
- Lý do: Soutetsu tự xưng "anh" (JP 僕) → "Tôi"; đồng thời "quyến rũ anh ấy" sai ngôi — JP 誘惑をかける hướng về chính Soutetsu (người nhìn) nên phải là "quyến rũ tôi".

**Key 986 (ポーレット)**
- JP: `「あ、それっぽい。見せてください。……うんっ！　これ、\nこれです！　助かった～、ありがとう、双鉄くん！」`
- TW: `「嗯，好像是這個。讓我看一下。……嗯！是這個，就是這個！真是幫大忙了，謝謝你，雙鐵君！」`
- VN cũ: `「A, có vẻ là nó đấy. Cho em xem với. ...Đúng rồi! Cái này,\nchính là nó! May quá~, cảm ơn Soutetsu nhé!」`
- Sửa: `「A, có vẻ là nó đấy. Cho em xem với. ...Đúng rồi! Cái này,\nchính là nó! May quá~, cảm ơn anh Soutetsu nhé!」`
- Lý do: Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

**Key 987 (双鉄H)**
- JP: `「ああ。僕も、ポーレットのおまんこが欲しい」`
- TW: `「嗯，我也想插入你的小穴」`
- VN cũ: `「Ừ. Anh cũng muốn cô bé của Paulette.」`
- Sửa: `「Ừ. Tôi cũng muốn cô bé của Paulette.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 988 (双鉄H)**
- JP: `「ああ、僕もだ」`
- TW: `「嗯，我也想要」`
- VN cũ: `「Ừ, anh cũng vậy.」`
- Sửa: `「Ừ, tôi cũng vậy.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 989 (双鉄H)**
- JP: `「ああ、思う」`
- TW: `「嗯，我想看」`
- VN cũ: `「Ừ, anh muốn.」`
- Sửa: `「Ừ, tôi muốn.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 996 (双鉄H)**
- JP: `「わかった」`
- TW: `「好的」`
- VN cũ: `「Anh hiểu rồi.」`
- Sửa: `「Tôi hiểu rồi.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 999 (双鉄H)**
- JP: `「できれば、そこも……リラックスさせてやってほしい」`
- TW: `「如果可以的話，我想讓那裡也放鬆一下」`
- VN cũ: `「Nếu được thì, anh cũng muốn em……làm cho chỗ đó được thư giãn.」`
- Sửa: `「Nếu được thì, tôi cũng muốn em……làm cho chỗ đó được thư giãn.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 1009 (双鉄H)**
- JP: `「少しどころか、大いに見たい。パンツを、ではなく、\nポーレットの魅力的な姿を見たい」`
- TW: `「我不僅是有點想看，而是特別想看。我想看的不僅是內褲，而是魅力四射的你」`
- VN cũ: `「Đâu chỉ một chút, anh rất muốn xem là đằng khác. Không phải xem quần lót,\nmà là muốn ngắm nhìn dáng vẻ quyến rũ của Paulette.」`
- Sửa: `「Đâu chỉ một chút, tôi rất muốn xem là đằng khác. Không phải xem quần lót,\nmà là muốn ngắm nhìn dáng vẻ quyến rũ của Paulette.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 1016 (ポーレット)**
- JP: `「わかりました。双鉄くんのご希望なら、\nわたし、頑張ってみます」`
- TW: `「我明白了。既然你想看，我就努力一下」`
- VN cũ: `「Em hiểu rồi. Nếu đó là mong muốn của Soutetsu,\nthì em sẽ cố gắng thử xem.」`
- Sửa: `「Em hiểu rồi. Nếu đó là mong muốn của anh Soutetsu,\nthì em sẽ cố gắng thử xem.」`
- Lý do: Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

**Key 1034 (双鉄H)**
- JP: `「ポーレット……僕は、君とセックスしたい」`
- TW: `「波萊特……我想跟你做愛」`
- VN cũ: `「Paulette……Anh muốn làm tình với em.」`
- Sửa: `「Paulette……Tôi muốn làm tình với em.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 1045 (双鉄H)**
- JP: `「白い肌に、紺の下着がとても映えてる。\n全部を脱いでしまうのは、もったいないと、僕は思う」`
- TW: `「白色的肌膚和藍色的內衣非常搭。我覺得全部脫掉有點浪費」`
- VN cũ: `「Đồ lót màu xanh đen cực kỳ tôn lên làn da trắng của em.\nAnh nghĩ cởi hết ra thì phí lắm.」`
- Sửa: `「Đồ lót màu xanh đen cực kỳ tôn lên làn da trắng của em.\nTôi nghĩ cởi hết ra thì phí lắm.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 1050 (双鉄H)**
- JP: `「おっぱいもだが――お尻もだとは気づかずにいた。\nポーレットの体は、どこもかしこも最高なのだな」`
- TW: `「胸當然很棒，但我之前一直忽視了屁股。你的身體真是不管哪裡都好棒」`
- VN cũ: `「Anh biết ngực em đẹp rồi——nhưng không ngờ mông em cũng vậy.\nCơ thể Paulette, chỗ nào cũng tuyệt vời hết.」`
- Sửa: `「Tôi biết ngực em đẹp rồi——nhưng không ngờ mông em cũng vậy.\nCơ thể Paulette, chỗ nào cũng tuyệt vời hết.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 1054 (双鉄H)**
- JP: `「出る――射精――射精、するっ――」`
- TW: `「要射了——要射了——」`
- VN cũ: `「Ra mất——xuất tinh——anh xuất tinh mất——」`
- Sửa: `「Ra mất——xuất tinh——tôi xuất tinh mất——」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 1067 (双鉄H)**
- JP: `「無論だ。\n僕にとっては衝撃的な事実を教えてもらったのだから」`
- TW: `「那當然。對於我來說這是一個很讓人震驚的事實」`
- VN cũ: `「Đương nhiên rồi.\nBởi vì em đã dạy cho anh một sự thật mang tính chấn động đối với anh mà.」`
- Sửa: `「Đương nhiên rồi.\nBởi vì em đã dạy cho tôi một sự thật mang tính chấn động đối với tôi mà.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 1068 (双鉄H)**
- JP: `「何故集めたのか――そこは僕には理解できんが、\nしかし実際、このコレクションに大いに助けられている」`
- TW: `「雖然我不知道他為什麼收集了這些數據——但是這些東西真是幫了大忙了」`
- VN cũ: `「Tại sao ông ấy lại thu thập những thứ này——anh không thể hiểu nổi,\nnhưng thực tế là bộ sưu tập này đã giúp ích rất nhiều.」`
- Sửa: `「Tại sao ông ấy lại thu thập những thứ này——tôi không thể hiểu nổi,\nnhưng thực tế là bộ sưu tập này đã giúp ích rất nhiều.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 1071 (ポーレット)**
- JP: `「双鉄くん……\nわたしが前いったこと、覚えててくれたんですね？」`
- TW: `「雙鐵君……你記得我之前告訴你的事啊」`
- VN cũ: `「Soutetsu...\nAnh vẫn nhớ những gì em từng nói sao?」`
- Sửa: `「Anh Soutetsu...\nAnh vẫn nhớ những gì em từng nói sao?」`
- Lý do: Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

### Thở gấp (6 dòng)

**Key 907 (双鉄H)**
- JP: `「っ！」`
- TW: `「呃」`
- VN cũ: `「!」`
- Sửa: `「Ư!」`
- Lý do: Mất tiếng hít っ (JP có っ, bản Việt bỏ mất) → "Ư" (quy tắc gasp; sweep toàn dự án xác nhận cùng giá trị sửa).

**Key 908 (双鉄H)**
- JP: `「っ！」`
- TW: `「呃！」`
- VN cũ: `「っ!」`
- Sửa: `「Ư!」`
- Lý do: Mất tiếng hít っ (JP có っ, bản Việt bỏ mất) → "Ư" (quy tắc gasp; sweep toàn dự án xác nhận cùng giá trị sửa).

**Key 934 (双鉄H)**
- JP: `「っ！」`
- TW: `「唔！」`
- VN cũ: `「っ!」`
- Sửa: `「Ư!」`
- Lý do: Mất tiếng hít っ (JP có っ, bản Việt bỏ mất) → "Ư" (quy tắc gasp; sweep toàn dự án xác nhận cùng giá trị sửa).

**Key 935 (双鉄H)**
- JP: `「っ――」`
- TW: `「啊——」`
- VN cũ: `「っ——」`
- Sửa: `「Ư——」`
- Lý do: Mất tiếng hít っ (JP có っ, bản Việt bỏ mất) → "Ư" (quy tắc gasp; sweep toàn dự án xác nhận cùng giá trị sửa).

**Key 954 (双鉄H)**
- JP: `「っ！」`
- TW: `「啊！」`
- VN cũ: `「っ!」`
- Sửa: `「Ư!」`
- Lý do: Mất tiếng hít っ (JP có っ, bản Việt bỏ mất) → "Ư" (quy tắc gasp; sweep toàn dự án xác nhận cùng giá trị sửa).

**Key 1639 (双鉄H)**
- JP: `（っ！？）`
- TW: `（啊！？）`
- VN cũ: `（!?）`
- Sửa: `（Ư!?）`
- Lý do: Mất tiếng hít っ (JP có っ, bản Việt bỏ mất) → "Ư" (quy tắc gasp; sweep toàn dự án xác nhận cùng giá trị sửa).

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
[script]
703 = "……Thế nên ý thức của tôi bị thu hút.\\nVào một nơi khác, một lỗ nhỏ màu hồng dễ thương đang co giật run rẩy."
705 = "「——Em cứ vắt bao nhiêu sữa của tôi tùy thích.」"
864 = "「Không,\\nngười đáng được cảm ơn không phải là tôi, mà là ông Taito chứ.」"
872 = "「Tinh dịch——của anh Soutetsu——nhận vào, tử cung——ưm——\\nVào cô bé——vẫn là, tuyệt nhất, nên là——」"
890 = "「Á——a——ưm——lỗ, hậu, của em——\\nBị anh Soutetsu——nong……rộng, ra——ưm——」"
899 = "「Hyaaaaaaa!!」"
900 = "「Á!」"
904 = "「Á!? A——mông——ưm——lỗ, hậu——\\nE, em——chưa từng, tự làm——bao giờ——ưm」"
907 = "「Ư!」"
908 = "「Ư!」"
919 = "「Phù——a——sâu, quá——thế này——\\nƯm——sướng quá——cảm giác, như đâm, vào tận bụng, vậy」"
934 = "「Ư!」"
935 = "「Ư——」"
937 = "「A——của anh Soutetsu——to hơn, bình thường——\\nPhù——to, quá——bị nong rộng, ra——a」"
954 = "「Ư!」"
972 = "「Vâng——làm đi! Hãy làm, đi ạ——ưm——\\nBắn tinh dịch——vào sâu, nhất——bên trong, em đi」"
980 = "「Ừ. Cụ thể là, tôi muốn xem cái dáng vẻ em vừa ý thức được ánh nhìn của tôi,\\nvừa giả vờ như tình cờ để quyến rũ tôi.」"
982 = "「Hí——phù——」"
986 = "「A, có vẻ là nó đấy. Cho em xem với. ...Đúng rồi! Cái này,\\nchính là nó! May quá~, cảm ơn anh Soutetsu nhé!」"
987 = "「Ừ. Tôi cũng muốn cô bé của Paulette.」"
988 = "「Ừ, tôi cũng vậy.」"
989 = "「Ừ, tôi muốn.」"
995 = "「Đau——」"
996 = "「Tôi hiểu rồi.」"
999 = "「Nếu được thì, tôi cũng muốn em……làm cho chỗ đó được thư giãn.」"
1006 = "「Ngay cả ở mông, cũng có thể đạt được khoái cảm tình dục nhỉ.」"
1009 = "「Đâu chỉ một chút, tôi rất muốn xem là đằng khác. Không phải xem quần lót,\\nmà là muốn ngắm nhìn dáng vẻ quyến rũ của Paulette.」"
1011 = "「Em không biết——đâu——nên là——như thế này——\\nPhù——a——mông——lại có cảm giác, như vậy」"
1016 = "「Em hiểu rồi. Nếu đó là mong muốn của anh Soutetsu,\\nthì em sẽ cố gắng thử xem.」"
1018 = "「Thì……em cũng có nghe——người ta, nói, vậy——ưm——\\nNhưng, mà——thực tế——lại đến mức này, thì——a——á」"
1026 = "「Đúng vậy nhỉ——Tôi cũng——, tuyệt nhất là——\\nTuyệt nhất là——tôi vẫn muốn làm thế——」"
1034 = "「Paulette……Tôi muốn làm tình với em.」"
1045 = "「Đồ lót màu xanh đen cực kỳ tôn lên làn da trắng của em.\\nTôi nghĩ cởi hết ra thì phí lắm.」"
1050 = "「Tôi biết ngực em đẹp rồi——nhưng không ngờ mông em cũng vậy.\\nCơ thể Paulette, chỗ nào cũng tuyệt vời hết.」"
1052 = "「Có muốn thử làm tình……bằng lỗ hậu không?」"
1054 = "「Ra mất——xuất tinh——tôi xuất tinh mất——」"
1062 = "「Cái đó……lỗ hậu——tự nhiên, em……\\nCũng cảm thấy rất có hứng thú——nhưng mà」"
1067 = "「Đương nhiên rồi.\\nBởi vì em đã dạy cho tôi một sự thật mang tính chấn động đối với tôi mà.」"
1068 = "「Tại sao ông ấy lại thu thập những thứ này——tôi không thể hiểu nổi,\\nnhưng thực tế là bộ sưu tập này đã giúp ích rất nhiều.」"
1071 = "「Anh Soutetsu...\\nAnh vẫn nhớ những gì em từng nói sao?」"
1235 = "Lỗ hậu môn đang co bóp nhấp nháy."
1293 = "Khuôn mặt đỏ bừng,\\nPaulette truyền đạt cho tôi bằng cả cơ thể lẫn lời nói."
1306 = "Nếu vừa rồi là dương vật của tôi thì——\\nNghĩ đến thôi cũng khiến hai hòn bi sun lại."
1349 = "Chỉ đơn thuần kích thích xung quanh phần lõm vào nhất,\\nnhư thể đang xoa tròn, nắn bóp."
1356 = "Tôi kéo nhẹ phần thịt xung quanh,\\nnong rộng lỗ hậu dễ thương ra một chút."
1359 = "Thử dập hông vào sâu hơn,\\ncơ thể Paulette lại run lên bần bật."
1362 = "Dùng ngón tay thấm đẫm mật ngọt từ cô bé vuốt ve quanh lỗ hậu,\\nâm đạo của Paulette lập tức co thắt lại."
1366 = "Ngón tay không đút vào.\\nCũng chưa chạm trực tiếp vào hậu môn."
1369 = "Dù vậy, hông tôi vẫn không dừng lại."
1376 = "Đầu ngón tay vừa thử đút vào,\\nđã bị hậu môn siết chặt dữ dội như muốn đẩy ra."
1454 = "Hơi thở của tôi và Paulette,\\nnhịp điệu của cả hai dần hòa làm một."
1461 = "Hông Paulette chuyển động mạnh."
1468 = "Không biết có phải do kích thích lỗ hậu hay không,\\nâm đạo của Paulette trơn ướt và quấn chặt hơn bình thường."
1488 = "Cứ thế cô ấy lả đi, mất hết sức lực.\\nCó vẻ như chỉ việc chống đỡ cơ thể mình thôi cũng đã tốn hết sức rồi."
1494 = "Với tư thế này, tôi không thể cử động mạnh được.\\nCho đến khi cơn sóng khoái cảm dịu xuống, Paulette có lẽ cũng không thể nhúc nhích."
1495 = "Trông như thể nó đang đòi hỏi ngón tay tôi,\\nđang cầu xin tôi đút vào vậy."
1500 = "Thật dễ chịu——và cũng thật thú vị.\\nGiọng nói của Paulette cũng không chỉ đơn thuần là kinh ngạc."
1536 = "Có vẻ như độ co giãn khá tốt.\\nHơn nữa, nó còn đang ngọ nguậy như thèm khát——"
1639 = "（Ư!?）"
1641 = "（Thịch!）"
1642 = "（Phập! Phập! Phập! Nhóp nhép!）"
1643 = "（Phập——phập——nhóp——nhép——）"
1645 = "（Nhóp! Nhép! Nhóp! Nhép!!）"
1650 = "（Phập!）"
1658 = "（Sụttt!）"
1664 = "（Nhóp——nhép——trơn——tuột——）"
1673 = "（Kítttttt!）"
1676 = "（Trơn tuộtttt）"
1682 = "（Đây là——）"
```

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- Soutetsu gọi Paulette "em" 8 lần trong thoại/H (705, 980, 999, 1006, 1034, 1045, 1050, 1067) vs "cô" 0 lần — cộng dồn toàn dự án: "em" 65 vs "cô" 43 (sau h3; +5 nữa ở h4 thành 70 vs 43). "Cô bé" tại 987 là danh từ chỉ bộ phận, không phải cách xưng hô. Độc thoại dùng "cô ấy" 18 lần (ngôi thứ ba trong lời dẫn, không tính vào "cô").
- 御一夜 "Ohimitera" 2 lần trong các dòng đúng (1255, 1347), "Ohito" 0, "Ohitoyo" 0 — ghi nhận cho đợt thống nhất sau.
- "mình" trong độc thoại: 5 lần, trong đó 1 lần (1359) nằm trong bản Việt lệch vị trí (đã sửa); 4 lần còn lại đều đúng (sở hữu/phản thân: 1268, 1477, 1401, 1566).
- Dòng chưa chắc chắn mới: 1683 (Soutetsu H, JP 僕 → VN "mình" ở cả hai vế: "vẫn chưa có tình cảm với mình" và "do mình 'không thèm nhìn'"). Hai ứng viên: (a) sửa thành "tôi" theo quy tắc Soutetsu tự xưng "Tôi" (docs §2.1, đã áp dụng nhất quán cho "anh"→"Tôi" trong h1/h2/h3/h4); (b) giữ "mình" vì đây là giọng nghĩ thầm trong đầu, "mình" là cách nói tự nhiên của tiếng Việt khi nghĩ về bản thân. Chưa quyết — cần Hieu chọn.
- Không có 湯医/帝鉄/コン/宮司/マスコン/KiHa/整備体/運転ボディ/機関士-gloss/駿袋 trong file.

## Đề xuất cập nhật context (chưa chốt)

- Tinh chỉnh quy tắc tên trần vs tên rên (xem trên): ngoại lệ chỉ áp dụng cho tên rên trong lúc thân mật, không áp dụng cho cách gọi tên trong câu giao tiếp.
- h3 là file Paulette h nặng nhất về lệch vị trí (45 dòng) — khi rebuild TOML từ CSV3, phải áp dụng khối sửa này trước, nếu không lỗi lệch sẽ quay lại.

## Đã kiểm tra và KHÔNG tính là sai

- 901 "Hyan!!" (ひゃんっ → "Hya", theo tiền lệ h1/h2 giữ "Hya" cho ひゃ).
- 923 (ずりゅう → "Sụt" — SFX, っっ hấp thụ theo quy ước của file).
- 1271, 1451 (勃起の割れ目/くびれ → "rãnh quy đầu" — cách diễn tự do hợp lệ).
- 1490 (指摘 = "chỉ ra", không phải ngón tay).
- 1578 (おっぱい → "đôi gò bồng đảo").
- Các bản Việt trùng trong file chỉ là tiếng rên/SFX ngắn lặp lại hợp lệ.
- 1683 — dòng chưa chắc chắn (xem trên), không tính vào 69 dòng sai.

## Kết bài

- h3 sai 69/279 (24,7%) — nặng nhất trong các file Paulette h từ trước tới nay (h1 13,8%, h2 13,7%), và là file lệch vị trí nặng nhất kể từ obasan/sleeper. Lỗi chủ đạo là chuỗi xoay vòng nội bộ 45 dòng (38 phục hồi trong file, 7 dịch mới), cộng với xưng hô hệ thống "anh" (15) + tên trần (3) và thở gấp (6).
- Khối TOML 69 key đã parse đúng; áp dụng khối này sẽ sửa hết 69 dòng. Còn lại 1 dòng chưa chắc chắn (1683) và 7 bản Việt mồ côi chưa tra nguồn — cần Hieu quyết trước khi rebuild.
