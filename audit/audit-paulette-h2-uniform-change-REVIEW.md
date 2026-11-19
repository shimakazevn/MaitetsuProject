# Audit: Paulette h2_制服変更？ — 47 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/ポーレットh2_制服変更？.txt.toml` — Bữa tối tại nhà Paulette (món Bœuf Bourguignon, rượu vang): Hibiki nhờ Soutetsu hỏi khéo Paulette về việc thay đổi thiết kế đồng phục; Paulette thử đồng phục trước gương; cảnh chuyển sang thân mật (chạm qua đồng phục/tất, kích thích âm vật, tai nạn tè dầm, rồi cởi đồ quan hệ). 292 dòng script đã đọc hết, đối chiếu từng dòng với JP gốc và TW (nhân chứng thứ hai).

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa toàn bộ 292 dòng (thoại 140: Soutetsu 56, Paulette 84; lời dẫn 152) đối chiếu JP + TW từ CSV "Trang tính 3" và TOML-2.
- **40 dòng sai (13,7%), 0 dòng chưa chắc chắn.** Thoại sai 38/140 (27,1%), lời dẫn sai 2/152 (1,3%). Theo người nói: Soutetsu 18/56, Paulette 20/84, lời dẫn 2/152.
- Phân loại: thuật ngữ 1, xưng hô 28, sai nghĩa 0, lỗi nhỏ 11; chưa dịch 0, cắt cụt 0, chưa chắc chắn 0.
- Heuristic (dấu thoại ↔ lời dẫn): shift 0 đạt 292/292 = 1,000; các shift khác 0,986–0,993 — không có shift nào vượt trội, không có key-shift sạch. TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất; 135 khác biệt thô chỉ ở `\n`/khoảng trắng — hiện tượng mất `\n` đã biết của TOML, 59% toàn dự án).
- 0 dòng CSV trống; VN==TW 0. `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 0 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục). 7 bản Việt trên 20 ký tự trùng với file khác — tất cả đều là cụm ngắn/SFX/gasp dùng chung, không phải tràn chương: "Có vẻ, là vậy nhỉ." (1087 — trùng れいなh3 1148, JP の、ようだな, cụm cảm thán chung), "Sao vậy? Paulette." (1048 — trùng グランドリライト08 2871, JP どうした？ポーレット, câu hỏi chung), "（Rào rào rào rào rào）" (1672/1642 trong cùng file — hai SFX nước khác nhau trong cùng cảnh tè dầm, cùng cách dịch tiếng nước, giữ nguyên), "（Phụt! Phụt! Phụt! Phụt!）" (1636/1634 trong cùng file và nhiều file h khác — SFX xuất tinh chuẩn của dự án), "Ưm hyuuuuuuuuuuuuuu!!!" (1021 — trùng lr稀咲追加h 1159, JP んひゅううううううううううっ, tiếng rên chung). Các bản Việt trùng trong file: "「À——」" 951/1018 (JP khác nhau nhưng cùng là tiếng cảm thán, đều đúng), "（Rào rào rào rào rào）" 1672/1642 và "（Phụt! Phụt! Phụt! Phụt!）" 1636/1634 (đã nêu trên).
- Không có file trùng lặp ở thư mục khác (đã kiểm tra md5 toàn bộ 227 file TOML-2; h1 và h2 mỗi file chỉ tồn tại 1 lần; 11 nhóm trùng đã biết từ trước đều không liên quan hai file này).
- Quét xưng hô bằng máy (đã chuẩn hoá `\n` thành khoảng trắng trước khi chạy regex `\b`): Soutetsu trong thoại tự xưng "anh" 15 dòng (tất cả sai), "Tôi" 0 lần; độc thoại "anh" 2 dòng (1253, 1427 — cả hai sai); "em" 6 lần gọi Paulette (1119, 903, 1655, 894, 1082, 960) vs "cô" 0 lần — "Em ấy" tại 1040 là Hibiki (ngôi thứ ba), không tính vào tally. Paulette gọi "anh Soutetsu" 0 lần vs tên trần "Soutetsu" 20 lần / 19 dòng. "mình" trong độc thoại 9 dòng (1318, 1381, 1326, 1406, 1377, 1470, 1471, 1514, 1490) — tất cả đều đúng (sở hữu/phản thân/thành ngữ "tự mình"). "mình" ở CHAR 双鉄H 1 dòng: 1127 (mệnh đề lồng "không nghĩ mình hiểu biết", phản thân, đúng).
- **Viết bản sửa bằng tay, không sửa hàng loạt bằng script (quy tắc 19/11 của Hieu):** mọi bản sửa trong file này đều được viết tay từng dòng từ JP (+TW) của chính dòng đó; script chỉ dùng để lắp ráp khối TOML từ các bản sửa đã viết, kiểm tra parse TOML và đối chiếu số key. Không có bản sửa nào do script sinh ra hay sửa đổi.
- **Kiểm tra lần hai (đọc lại toàn bộ bản sửa đối chiếu JP):** sau khi lắp khối TOML, đã đọc lại cả 37 bản sửa, từng dòng đối chiếu với JP gốc để xác nhận nghĩa, người nói và dấu câu — **tổng số bản sửa: 37; đã kiểm tra lại: 37; bị loại ở vòng hai: 0.** Sau đó, rà soát chéo với đợt quét gasp っ toàn dự án phát hiện thêm 3 dòng mất gasp cuối (1135, 950, 985) mà audit bỏ sót — đã xác minh lại từng dòng đối chiếu JP và bổ sung (vòng bổ sung: 3/3 đúng, 0 bị loại), nâng tổng số lên **40 bản sửa, đã kiểm tra lại 40, bị loại 0.** Chỉ kiểm tra parse + khớp số key là chưa đủ; vòng đọc lại này là bắt buộc theo quy tắc của Hieu.
- **Rà soát chéo với đợt quét gasp っ toàn dự án:** sweep xác nhận 2/2 bản sửa gasp っ của audit (1004, 952 — cùng giá trị sửa) và phát hiện thêm 3 dòng (1135, 950, 985 — xem trên).

## Kết luận về cơ chế lỗi

File này **sạch về cấu trúc** — 0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương — giống h1. Lỗi tập trung ở hai lựa chọn hệ thống của người dịch, cùng mẫu với h1:

1. **Soutetsu tự xưng "anh" trong thoại (15/15 lần tự xưng, 0 lần "Tôi")**, cộng thêm 2 dòng độc thoại dùng "anh" (1253, 1427). File này là file đầu tiên có lỗi xưng hô trong độc thoại ở mức 2 dòng (h1: 0 dòng độc thoại sai ngoài 1483 thuật ngữ).
2. **Paulette gọi Soutetsu bằng tên trần (19 dòng, 20 lần)**, trong khi cả file không có lần nào "anh Soutetsu" — tệ hơn h1 (27 dòng nhưng còn 1 lần đúng). Quy tắc tên trần vs tên rên áp dụng như h1 (xem h1): 11 dòng sửa, 8 dòng ngoại lệ giữ nguyên (1000, 1009, 1096, 1128, 1001, 950, 983, 995 — tên rên độc lập/kèm tiếng rên trong lúc thân mật).
**Đính chính B4 19/11 22:24 (Hieu ủy quyền Muse chốt):** ngoại lệ tên rên BÃI BỎ — Paulette gọi Soutetsu bằng tên trần là sai ngay cả khi rên/kêu tên trong lúc thân mật, vì JP là 双鉄くん trong tất cả các dòng kiểm tra (không bao giờ bỏ くん, không bao giờ là さん hay tên trần). 8 dòng này nay đều đã sửa (950 đã có trong danh sách nên tổng file 40→47).

Điểm khác biệt của file này so với h1 là **lỗi nhỏ về SFX**: 6/11 lỗi nhỏ là tiếng thở/gasp bị dịch sai — 2 dòng để nguyên dạng phiên âm La-tinh của tiếng thở dài (923 "fuaaaaaaaaaaan", 963 "Afuuuuuuuuuuun"), 1 dòng phiên âm sai nguyên âm kèm La-tinh (957 "Phu... fuyahaaa"), 1 dòng sai nguyên âm + từ không tự nhiên (956 "phu... phúa"), và 2 dòng "phá" (932, 991 — cùng mẫu với h1). Đối chiếu trong cùng file: 929 dịch đúng ふえっ→"phuê", ふやぁっ→"phuya" và 1008 dịch đúng ふあっ→"phù" — chứng tỏ cách dịch đúng đã có sẵn, 6 dòng sai là do người dịch không nhất quán. 5 lỗi nhỏ còn lại đều là mất tiếng hít っ: 2 dòng mất cả dòng (1004, 952) và 3 dòng mất gasp cuối sau gạch/dấu ~ (1135, 950, 985 — cả 3 do đợt quét gasp っ phát hiện khi rà soát chéo).

## Chi tiết dòng sai

### Thuật ngữ (1 dòng)

**889 [Paulette]** — 新生御一夜鉄道 — "Ohimitera" sai theo quyết định 19/11; đúng là "Ohitoyo".

- JP: 「けど……いいアイディアかも、って直感では思います。
低コストで、新生御一夜鉄道をアピールできる……かも」
- TW: 「但是……我感覺這是個不錯的主意。成本又低，還能宣傳一下新生的御一夜鐵道……」
- Cũ: 「Nhưng mà... trực giác mách bảo em đó có thể là một ý tưởng hay.
Vừa ít tốn kém, lại có thể quảng bá cho Đường sắt Ohimitera mới... có lẽ vậy.」
- Sửa: 「Nhưng mà... trực giác mách bảo em đó có thể là một ý tưởng hay.
Vừa ít tốn kém, lại có thể quảng bá cho Đường sắt Ohitoyo mới... có lẽ vậy.」

### Xưng hô (28 dòng)

**891 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「しかし、現に僕は――」
- TW: 「但是我已經——」
- Cũ: 「Nhưng, thực tế là anh đang——」
- Sửa: 「Nhưng, thực tế là tôi đang——」

**894 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「謝ることは、何もない。ここはポーレットの部屋だし、
掃除であれば、僕も手伝う」
- TW: 「你不用道歉。這裡是你的房間，如果要打掃的話我也來幫忙」
- Cũ: 「Em không có gì phải xin lỗi cả. Đây là phòng của Paulette mà,
nếu phải dọn dẹp thì anh cũng sẽ giúp một tay.」
- Sửa: 「Em không có gì phải xin lỗi cả. Đây là phòng của Paulette mà,
nếu phải dọn dẹp thì tôi cũng sẽ giúp một tay.」

**900 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「双鉄くんの好きな家庭料理って、なんですか？」
- TW: 「你喜歡什麼家常菜呢？」
- Cũ: 「Soutetsu thích món ăn gia đình nào vậy?」
- Sửa: 「Anh Soutetsu thích món ăn gia đình nào vậy?」

**925 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「よかったぁ。双鉄くんのお口にあって」
- TW: 「合你的口味就好」
- Cũ: 「May quá. Hợp khẩu vị của Soutetsu là tốt rồi.」
- Sửa: 「May quá. Hợp khẩu vị của anh Soutetsu là tốt rồi.」

**948 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu hỏi nói ra (ngạc nhiên) → "anh Soutetsu" (docs §2.4). Đây không phải tên rên trong lúc thân mật nên không thuộc ngoại lệ.

- JP: 「ひゃっ！？　って、え？　双鉄、くん？」
- TW: 「呀！？哎？雙鐵君？」
- Cũ: 「Hya!? Khoan, ơ? Soutetsu, này?」
- Sửa: 「Hya!? Khoan, ơ? Anh Soutetsu, này?」

**960 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi". JP là lời nói ngọng (miệng đang bận); bản Việt giải mã thành lời rõ — giữ nguyên cách giải mã, chỉ sửa xưng hô.

- JP: 「やふほふほひは――ほうひを、へふらふほ」
- TW: 「呼唔呼唔——呼唔呼唔」
- Cũ: 「Anh đang dọn dẹp——giúp em mà.」
- Sửa: 「Tôi đang dọn dẹp——giúp em mà.」

**1014 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「うん。わたしも……そうして、ほしい。
おもらしおまんこ……双鉄くんに、栓して、欲しい」
- TW: 「嗯。我也……想讓你這樣。我想讓你……把我失禁的小穴塞上」
- Cũ: 「Vâng. Em cũng... muốn anh làm vậy.
Âm đạo tè dầm này... em muốn, Soutetsu bịt nó lại.」
- Sửa: 「Vâng. Em cũng... muốn anh làm vậy.
Âm đạo tè dầm này... em muốn, anh Soutetsu bịt nó lại.」

**1017 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「うむ。僕もタイミングがつかめずに、
結局は、こんなにも直球で尋ねることになってしまった」
- TW: 「嗯。所以我找不到時機，最後也只能這樣直接問了」
- Cũ: 「Ừm. Anh cũng không nắm bắt được thời cơ,
nên rốt cuộc lại phải hỏi thẳng thừng thế này đây.」
- Sửa: 「Ừm. Tôi cũng không nắm bắt được thời cơ,
nên rốt cuộc lại phải hỏi thẳng thừng thế này đây.」

**1031 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói có nội dung (giải thích về rượu vang/thay đồ) → "anh Soutetsu" (docs §2.4). Không thuộc ngoại lệ tên rên.

- JP: 「お、押す……から――双鉄、くんっ――
ワイン、わたし……だって――そのまま、お着替えっ」
- TW: 「因為你……這樣一按——我就、我就……因為我是直接換的衣服」
- Cũ: 「T, tại anh ấn... vào——Soutetsu, này——
Rượu vang, em... bởi vì——cứ thế, thay đồ luôn.」
- Sửa: 「T, tại anh ấn... vào——anh Soutetsu, này——
Rượu vang, em... bởi vì——cứ thế, thay đồ luôn.」

**1040 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi". "Em ấy" là Hibiki (ngôi thứ ba), giữ nguyên — không tính vào tally "em" gọi Paulette.

- JP: 「ポーレットにさりげなく聞いておいて欲しいと言われた。
制服のデザインを変更する予定が無いかどうかを」
- TW: 「她讓我隨口問你一句，問你有沒有更改制服樣式的計劃」
- Cũ: 「Em ấy bảo anh hỏi khéo Paulette xem.
Có dự định thay đổi thiết kế đồng phục hay không.」
- Sửa: 「Em ấy bảo tôi hỏi khéo Paulette xem.
Có dự định thay đổi thiết kế đồng phục hay không.」

**1046 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu xin lỗi có nội dung → "anh Soutetsu" (docs §2.4). Không thuộc ngoại lệ tên rên.

- JP: 「ごめっ――ごめんなさい――双鉄くんっ――んっ」
- TW: 「對不起——對不起——雙鐵君――嗯」
- Cũ: 「Xin——xin lỗi anh——Soutetsu——ưm.」
- Sửa: 「Xin——xin lỗi anh——anh Soutetsu——ưm.」

**1051 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「僕がしておく。
ポーレットは、シャワーを浴びて着替えた方が」
- TW: 「我來打掃。你就去沖澡換衣服」
- Cũ: 「Để anh làm cho.
Paulette đi tắm rồi thay đồ đi.」
- Sửa: 「Để tôi làm cho.
Paulette đi tắm rồi thay đồ đi.」

**1055 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi" (2 lần).

- JP: 「と、思ったが、判断材料がまだ足りん。
耐久性も、チェックしておくべきかと思う」
- TW: 「我本來是這麼想的，但是判斷的依據還不夠。我覺得還要檢查一下耐磨性」
- Cũ: 「Anh nghĩ vậy, nhưng dữ kiện đánh giá vẫn chưa đủ.
Anh nghĩ cũng nên kiểm tra cả độ bền nữa.」
- Sửa: 「Tôi nghĩ vậy, nhưng dữ kiện đánh giá vẫn chưa đủ.
Tôi nghĩ cũng nên kiểm tra cả độ bền nữa.」

**1059 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「わかって、るっ――だからっ――
次――こそ――いっしょ――にっ――」
- TW: 「我知道——下一次——我們一起——」
- Cũ: 「Anh biết, mà——nên là——
lần này——nhất định——cùng, nhau——」
- Sửa: 「Tôi biết, mà——nên là——
lần này——nhất định——cùng, nhau——」

**1060 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「聞く以上、日々姫にデザイナーのアテがあるのだと思う。
よければ、話を進めてみるか？」
- TW: 「我聽日日姬的意思，她好像能拿出新設計。不介意的話，我就讓她推進這件事嗎？」
- Cũ: 「Đã cất công hỏi thế này, anh nghĩ Hibiki có quen biết nhà thiết kế nào đó.
Nếu được, chúng ta thử triển khai chuyện này xem sao nhé?」
- Sửa: 「Đã cất công hỏi thế này, tôi nghĩ Hibiki có quen biết nhà thiết kế nào đó.
Nếu được, chúng ta thử triển khai chuyện này xem sao nhé?」

**1061 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「変更した方がいいかどうか、
実物を見て、双鉄くんに検討して貰う方がいいと思って」
- TW: 「我覺得要不要更改，還是讓你來看看實物來討論一下比較好」
- Cũ: 「Em nghĩ là xem thực tế rồi để Soutetsu cân nhắc
xem có nên thay đổi hay không thì sẽ tốt hơn.」
- Sửa: 「Em nghĩ là xem thực tế rồi để anh Soutetsu cân nhắc
xem có nên thay đổi hay không thì sẽ tốt hơn.」

**1072 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「大丈夫だ。すぐに拭くから」
- TW: 「沒事的，我來擦乾淨」
- Cũ: 「Không sao đâu. Anh sẽ lau sạch ngay đây.」
- Sửa: 「Không sao đâu. Tôi sẽ lau sạch ngay đây.」

**1073 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi" (2 lần).

- JP: 「ああいや、思い出したのだ。
日々姫に頼まれごとをしていたと」
- TW: 「沒事，我就是忽然想起來了。日日姬拜託了我一件事」
- Cũ: 「À không, anh chợt nhớ ra.
Hibiki có nhờ anh một chuyện.」
- Sửa: 「À không, tôi chợt nhớ ra.
Hibiki có nhờ tôi một chuyện.」

**1082 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「ポーレット。拭くより、栓で――
おまんこを、僕は塞いでしまいたい」
- TW: 「波萊特。比起給你擦，我想用栓塞——把你的小穴給堵上」
- Cũ: 「Paulette. Thay vì lau sạch, anh muốn dùng nút bịt——
bịt kín âm đạo của em lại.」
- Sửa: 「Paulette. Thay vì lau sạch, tôi muốn dùng nút bịt——
bịt kín âm đạo của em lại.」

**1111 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「この制服は……ここまで性的なものだったのか。
今まで、全く気づかなかったが――」
- TW: 「這件制服……原來是這麼性感的嗎。我之前完全都沒有注意到」
- Cũ: 「Bộ đồng phục này... gợi dục đến mức này sao.
Cho đến giờ, anh hoàn toàn không hề nhận ra đấy——」
- Sửa: 「Bộ đồng phục này... gợi dục đến mức này sao.
Cho đến giờ, tôi hoàn toàn không hề nhận ra đấy——」

**1114 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「それは、わたしたちが恋人同士で、ふたりっきりで。
わたしが、双鉄くんを誘惑。しちゃってるからですよ」
- TW: 「這是因為我們是情侶，還是兩人獨處。而我就在誘惑你啦」
- Cũ: 「Đó là vì chúng ta là người yêu của nhau, và chỉ có hai người.
Là do em đang quyến rũ Soutetsu đấy ạ.」
- Sửa: 「Đó là vì chúng ta là người yêu của nhau, và chỉ có hai người.
Là do em đang quyến rũ anh Soutetsu đấy ạ.」

**1120 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「あのっ！　わたし！　わたしも――
その味覚えたいです。双鉄くんのおうちの肉じゃが」
- TW: 「那個，我也想！我也想——學會做這個。我也想學你家的馬鈴薯燉肉」
- Cũ: 「À này! Em! Em cũng muốn——
học được hương vị đó. Món thịt hầm khoai tây của nhà Soutetsu.」
- Sửa: 「À này! Em! Em cũng muốn——
học được hương vị đó. Món thịt hầm khoai tây của nhà anh Soutetsu.」

**1127 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi". "mình" trong mệnh đề lồng ("không nghĩ mình hiểu biết") là phản thân, giữ nguyên.

- JP: 「僕に、服飾のことがわかるとも思えん。が――」
- TW: 「雖然我不太懂服飾一類的東西——」
- Cũ: 「Anh không nghĩ mình hiểu biết về trang phục đâu. Nhưng mà——」
- Sửa: 「Tôi không nghĩ mình hiểu biết về trang phục đâu. Nhưng mà——」

**1129 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「双鉄くん？　制服……どうしよ？
デザイン変更、した方がいい？」
- TW: 「雙鐵君，制服……怎麼辦？樣式要改嗎？」
- Cũ: 「Soutetsu? Đồng phục... tính sao đây?
Có nên thay đổi thiết kế không anh?」
- Sửa: 「Anh Soutetsu? Đồng phục... tính sao đây?
Có nên thay đổi thiết kế không anh?」

**1130 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「双鉄くん？　どうかしました？」
- TW: 「雙鐵君？怎麼了？」
- Cũ: 「Soutetsu? Có chuyện gì sao anh?」
- Sửa: 「Anh Soutetsu? Có chuyện gì sao anh?」

**1253 [lời dẫn]** — Độc thoại của Soutetsu dùng "anh" → "Tôi" (docs §2.1).

- JP: だが、いい。
個人的には、問答無用で、極めてよろしい。
- TW: 不過這樣很棒。從個人角度來說，她穿成這樣非常誘人。
- Cũ: Nhưng mà, đẹp lắm.
Theo ý kiến cá nhân anh thì không cần phải bàn cãi, vô cùng xuất sắc.
- Sửa: Nhưng mà, đẹp lắm.
Theo ý kiến cá nhân tôi thì không cần phải bàn cãi, vô cùng xuất sắc.

**1427 [lời dẫn]** — Độc thoại của Soutetsu dùng "anh" → "Tôi". "em" là Paulette ở ngôi thứ ba trong độc thoại, giữ nguyên.

- JP: それが希望なら、従おう。
- TW: 既然她希望這樣的話，我就照辦吧。
- Cũ: Nếu em đã muốn thế, thì anh sẽ chiều ý.
- Sửa: Nếu em đã muốn thế, thì tôi sẽ chiều ý.

**1655 [Soutetsu]** — Suy nghĩ của Soutetsu dùng "Anh" làm chủ ngữ → "Tôi". "em" là Paulette (người được trêu), giữ nguyên.

- JP: （焦らしているつもりは無いのだがな）
- TW: （我其實沒打算挑逗她）
- Cũ: （Anh đâu có định trêu chọc em đâu.）
- Sửa: （Tôi đâu có định trêu chọc em đâu.）

### Lỗi nhỏ (11 dòng)

**923 [Paulette]** — JP ふああああああああああんっっっっ để nguyên dạng phiên âm La-tinh "fuaaaaaaaaaaan" — không phải tiếng Việt → "phuàààààààààn!".

- JP: 「けどっ――けどぉっ――わたしっ――わらひぃっ――
あっ――ふああああああああああんっっっっ！」
- TW: 「可是——可是——我已經——我已經——啊——呼啊啊啊！」
- Cũ: 「Nhưng mà——nhưng mà——em——em——
á——fuaaaaaaaaaaan!」
- Sửa: 「Nhưng mà——nhưng mà——em——em——
á——phuàààààààààn!」

**932 [Paulette]** — JP ふあっ là tiếng thở; bản cũ "phá" đọc thành động từ "phá" → "phà".

- JP: 「ひゃあっ――んっ――おまん、こ――おそうじ――
ふあっ――ていねいに、おそうじ――らめ、なのぉっ」
- TW: 「呀——嗯——小穴——被清理了——呼啊——清理得——好仔細——不要啦」
- Cũ: 「Hya——ưm——âm, đạo——đang được dọn dẹp——
phá——dọn dẹp, cẩn thận quá——đừng, mà.」
- Sửa: 「Hya——ưm——âm, đạo——đang được dọn dẹp——
phà——dọn dẹp, cẩn thận quá——đừng, mà.」

**950 [Paulette]** — JP kết bằng tiếng hít sau gạch (くんっ――っ！); bản Việt giữ gạch nhưng mất tiếng hít → thêm Ư. Tên "Soutetsu" giữ nguyên theo ngoại lệ tên rên — chỉ sửa gasp. Dòng này do đợt quét gasp っ toàn dự án phát hiện khi rà soát chéo (audit bỏ sót); đã xác minh lại đối chiếu JP trước khi bổ sung.

- JP: 「ひゃうんっ！？　き、きたないっ――だって、
おしっこ――んっ――そうてつ、くんっ――っ！」
- TW: 「呀！？很、很髒的——因為——有尿——嗯——雙鐵——嗯！」
- Cũ: 「Hya un!? B, bẩn lắm——bởi vì,
có nước tiểu——ưm——Soutetsu, này——!」
- Sửa: 「Hya un!? B, bẩn lắm——bởi vì,
có nước tiểu——ưm——Soutetsu, này——Ư!」

**952 [Soutetsu]** — JP 「っ！」 mất tiếng hít → "Ư!".

- JP: 「っ！」
- TW: 「呃！」
- Cũ: 「!」
- Sửa: 「Ư!」

**956 [Paulette]** — JP ふ……ふぇ……ふあ là ba tiếng thở: ふ→"Phù" đúng, nhưng ふぇ (fe) dịch thành "phu" sai nguyên âm, ふあ dịch thành "phúa" (không phải tiếng Việt tự nhiên; cùng file dịch đúng ふあっ thành "phù" ở 1008) → "Phù... phê... phùa.".

- JP: 「ふ……ふぇ……ふあ」
- TW: 「呼……呼……呼啊」
- Cũ: 「Phù... phu... phúa.」
- Sửa: 「Phù... phê... phùa.」

**957 [Paulette]** — JP ふぇ (fe) dịch thành "Phu" sai nguyên âm; ふやぁぁぁあ để nguyên dạng phiên âm La-tinh "fuyahaaa" — không phải tiếng Việt → "Phê... a... phuyaaa." (đối chiếu 929 trong cùng file: ふえっ→"phuê", ふやぁっ→"phuya").

- JP: 「ふぇ……あ……ふやぁぁぁあ」
- TW: 「呼……啊……啊呀」
- Cũ: 「Phu... a... fuyahaaa.」
- Sửa: 「Phê... a... phuyaaa.」

**963 [Paulette]** — JP あふうううううううううんっ để nguyên dạng phiên âm La-tinh "Afuuuuuuuuuuun" — không phải tiếng Việt → "À phùuuuuuuuuun!!!".

- JP: 「あふうううううううううんっ！！！」
- TW: 「呼啊啊啊！！！」
- Cũ: 「Afuuuuuuuuuuun!!!」
- Sửa: 「À phùuuuuuuuuun!!!」

**985 [Soutetsu]** — JP 「あっ――っ！」 kết bằng tiếng hít sau gạch; bản Việt giữ gạch nhưng mất tiếng hít → "Á——Ư!". Dòng này do đợt quét gasp っ toàn dự án phát hiện khi rà soát chéo (audit bỏ sót); đã xác minh lại đối chiếu JP trước khi bổ sung.

- JP: 「あっ――っ！」
- TW: 「啊——！」
- Cũ: 「Á——!」
- Sửa: 「Á——Ư!」

**991 [Paulette]** — JP ふぁ là tiếng thở; bản cũ "phá" đọc thành động từ "phá" → "phà".

- JP: 「あ……ひあ……あっ――ふぁ――あっ――あっ――あ」
- TW: 「啊……呀……啊——呼——啊——啊——啊」
- Cũ: 「A... hia... á——phá——á——á——a.」
- Sửa: 「A... hia... á——phà——á——á——a.」

**1004 [Soutetsu]** — JP 「っ！！？」 mất tiếng hít → "ƯƯ!!?".

- JP: 「っ！！？」
- TW: 「啊！！？」
- Cũ: 「!!?」
- Sửa: 「ƯƯ!!?」

**1135 [Paulette]** — JP 「～～～～～～～～っ！！！」 kết bằng tiếng hít sau dãy ~; TW thêm 啊; bản Việt chỉ giữ ~~~ — mất tiếng hít → thêm Ư. Dòng này do đợt quét gasp っ toàn dự án phát hiện khi rà soát chéo; đã xác minh lại đối chiếu JP trước khi bổ sung. (Đảo quyết định kiểm tra lần đầu: lúc đầu cho rằng ~~~ đã là tiếng rên, nhưng quy tắc B2 — JP kết bằng ～っ, VN kết bằng ~ không có âm — và TW có 啊 cho thấy cần thêm Ư.)

- JP: 「～～～～～～～～っ！！！」
- TW: 「～～～～～～～～啊！！！」
- Cũ: 「~~~~~~~~!!!」
- Sửa: 「~~~~~~~~Ư!!!」

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
889 = "「Nhưng mà... trực giác mách bảo em đó có thể là một ý tưởng hay.\nVừa ít tốn kém, lại có thể quảng bá cho Đường sắt Ohitoyo mới... có lẽ vậy.」"
891 = "「Nhưng, thực tế là tôi đang——」"
894 = "「Em không có gì phải xin lỗi cả. Đây là phòng của Paulette mà,\nnếu phải dọn dẹp thì tôi cũng sẽ giúp một tay.」"
900 = "「Anh Soutetsu thích món ăn gia đình nào vậy?」"
923 = "「Nhưng mà——nhưng mà——em——em——\ná——phuàààààààààn!」"
925 = "「May quá. Hợp khẩu vị của anh Soutetsu là tốt rồi.」"
932 = "「Hya——ưm——âm, đạo——đang được dọn dẹp——\nphà——dọn dẹp, cẩn thận quá——đừng, mà.」"
948 = "「Hya!? Khoan, ơ? Anh Soutetsu, này?」"
950 = "「Hya un!? B, bẩn lắm——bởi vì,\ncó nước tiểu——ưm——anh Soutetsu, này——Ư!」"
952 = "「Ư!」"
956 = "「Phù... phê... phùa.」"
957 = "「Phê... a... phuyaaa.」"
960 = "「Tôi đang dọn dẹp——giúp em mà.」"
963 = "「À phùuuuuuuuuun!!!」"
983 = "「Á——cậu, nhỏ——ưm——\ncậu, nhỏ——của anh Soutetsu——ưm.」"
985 = "「Á——Ư!」"
991 = "「A... hia... á——phà——á——á——a.」"
995 = "「A... ưm——anh Soutetsu, này——」"
1000 = "「A... anh Soutetsu, này——nhé——\ntrực tiếp... ngực đi anh.」"
1001 = "「A... anh Soutetsu, này——anh Soutetsu.」"
1004 = "「ƯƯ!!?」"
1009 = "「Ưm... a——anh Soutetsu... tay anh, lớn quá——\nưm——」"
1014 = "「Vâng. Em cũng... muốn anh làm vậy.\nÂm đạo tè dầm này... em muốn, anh Soutetsu bịt nó lại.」"
1017 = "「Ừm. Tôi cũng không nắm bắt được thời cơ,\nnên rốt cuộc lại phải hỏi thẳng thừng thế này đây.」"
1031 = "「T, tại anh ấn... vào——anh Soutetsu, này——\nRượu vang, em... bởi vì——cứ thế, thay đồ luôn.」"
1040 = "「Em ấy bảo tôi hỏi khéo Paulette xem.\nCó dự định thay đổi thiết kế đồng phục hay không.」"
1046 = "「Xin——xin lỗi anh——anh Soutetsu——ưm.」"
1051 = "「Để tôi làm cho.\nPaulette đi tắm rồi thay đồ đi.」"
1055 = "「Tôi nghĩ vậy, nhưng dữ kiện đánh giá vẫn chưa đủ.\nTôi nghĩ cũng nên kiểm tra cả độ bền nữa.」"
1059 = "「Tôi biết, mà——nên là——\nlần này——nhất định——cùng, nhau——」"
1060 = "「Đã cất công hỏi thế này, tôi nghĩ Hibiki có quen biết nhà thiết kế nào đó.\nNếu được, chúng ta thử triển khai chuyện này xem sao nhé?」"
1061 = "「Em nghĩ là xem thực tế rồi để anh Soutetsu cân nhắc\nxem có nên thay đổi hay không thì sẽ tốt hơn.」"
1072 = "「Không sao đâu. Tôi sẽ lau sạch ngay đây.」"
1073 = "「À không, tôi chợt nhớ ra.\nHibiki có nhờ tôi một chuyện.」"
1082 = "「Paulette. Thay vì lau sạch, tôi muốn dùng nút bịt——\nbịt kín âm đạo của em lại.」"
1096 = "「Ngực... khác quá... ưm——so với tự mình, làm, thì——\nphù, á... tay của, anh Soutetsu——sướng, hơn——á.」"
1111 = "「Bộ đồng phục này... gợi dục đến mức này sao.\nCho đến giờ, tôi hoàn toàn không hề nhận ra đấy——」"
1114 = "「Đó là vì chúng ta là người yêu của nhau, và chỉ có hai người.\nLà do em đang quyến rũ anh Soutetsu đấy ạ.」"
1120 = "「À này! Em! Em cũng muốn——\nhọc được hương vị đó. Món thịt hầm khoai tây của nhà anh Soutetsu.」"
1127 = "「Tôi không nghĩ mình hiểu biết về trang phục đâu. Nhưng mà——」"
1128 = "「anh Soutetsu... ưm.」"
1129 = "「Anh Soutetsu? Đồng phục... tính sao đây?\nCó nên thay đổi thiết kế không anh?」"
1130 = "「Anh Soutetsu? Có chuyện gì sao anh?」"
1135 = "「~~~~~~~~Ư!!!」"
1253 = "Nhưng mà, đẹp lắm.\nTheo ý kiến cá nhân tôi thì không cần phải bàn cãi, vô cùng xuất sắc."
1427 = "Nếu em đã muốn thế, thì tôi sẽ chiều ý."
1655 = "（Tôi đâu có định trêu chọc em đâu.）"
```

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- Soutetsu gọi Paulette "em" 6 lần (1119, 903, 1655, 894, 1082, 960) vs "cô" 0 lần — cộng dồn toàn dự án sau hai file h1+h2: **"em" 57 vs "cô" 43**. "Em" tiếp tục dẫn trước (sau P02 là 47 vs 43; sau h1 là 51 vs 43). Không quyết định, chỉ ghi nhận.
- 御一夜: "Ohimitera" 1 lần (889 — đã sửa trong file này), "Ohito" 0 lần, "Ohitoyo" 0 lần.
- Không có 湯医 / 帝鉄 / コン / タブレット / 整備体 / 運転ボディ / マスコン / 宮司 / KiHa trong file này — không có bằng chứng mới cho các quyết định đang chờ đó.

## Đề xuất cập nhật context (chưa chốt)

- Xem đề xuất ở audit h1 (quy tắc tên trần vs tên rên; quy tắc tiếng thở fa/fu) — hai đề xuất đó dựa trên bằng chứng của cả hai file h1+h2, không lặp lại ở đây.

## Đã kiểm tra và KHÔNG tính là sai

- **1671 (（ぐっ――） → "（Nhấc lên——）"):** TW ghi 放下 (đặt xuống) nhưng cảnh là Soutetsu nhấc Paulette lên bàn viết (乗せる) — tiếng rên gắng sức ぐっ có thể đọc theo cả hai hướng (nhấc lên / đặt xuống), giữ nguyên.
- **1135 — đảo quyết định:** lúc đầu không tính sai (cho rằng dãy ~~~ đã là tiếng rên), nhưng rà soát chéo với đợt quét gasp っ cho thấy JP kết bằng ～っ và TW có 啊 — đây là mất gasp cuối theo quy tắc B2 — đã chuyển sang danh sách sai (xem mục Lỗi nhỏ).
- **960 (JP là lời nói ngọng やふほふほひは, TW 呼唔呼唔, VN "Anh đang dọn dẹp——giúp em mà."):** bản Việt giải mã lời ngọng thành lời rõ — giữ nguyên cách giải mã (người chơi cần hiểu câu), chỉ sửa xưng hô "Anh" → "Tôi".
- **Gasp phiên âm ngắn ("Hya", "Hyu", "Kya", "Hian", "hyua"):** 941, 955, 964, 1021, 1022, 1023, 1026, 929 ("phuê"/"phuya" — đúng), 1008 ("phù" cho ふあっ — đúng) — theo tiền lệ sleeper 1781 ("Hau." được chấp nhận làm cách dịch tiếng thở), các âm thở ngắn phiên âm theo vần Việt được chấp nhận; chỉ tính sai khi là dạng La-tinh nguyên vẹn (923, 963, 957) hoặc thành từ có nghĩa sai ("phá") hoặc sai nguyên âm (956).
- **1115 (Bœuf Bourguignon giữ nguyên tiếng Pháp):** đúng — tên món ăn Pháp giữ nguyên.
- **1069 ("chị Mayami" cho 真闇姉):** đúng theo quy ước dự án.
- **882 ("Để anh phải đợi rồi."), 1044 ("quá anh ơi"):** "anh" là cách gọi Soutetsu, đúng — không phải tự xưng.
- **1413/1326/1430 ("cô ấy" trong độc thoại):** ngôi thứ ba chỉ Paulette, đúng.
- **1674 (（くいっ） → "（Nghiêng người）"), 1666 (（しゅるっ） → "（Xột xoạt）"), 1645 (（くちいっ） → "（Nhóp nhép）"), 1667 (（すりっ） → "（Cọ xát）"):** SFX dịch thành động tác, giữ nguyên.
- **943 (ひあんっ → "Hian!!"), 1019 (んひゅっ → "Ưm hyu!"):** tiếng rên đã dịch thành âm, giữ nguyên.
- **1672/1642 ("（Rào rào rào rào rào）"):** hai SFX nước khác nhau trong cùng cảnh tè dầm — cùng cách dịch tiếng nước, giữ nguyên (không phải tràn chương: cả hai đều khớp JP của chính dòng đó).

## Kết bài

ポーレットh2_制服変更？ sai 47/292 dòng (16,1%) — file h thứ hai của tuyến Paulette, sạch về cấu trúc như h1: 0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi. Lỗi tập trung ở hai lựa chọn hệ thống của người dịch: Soutetsu tự xưng "anh" trong thoại (15/15 lần tự xưng, 0 lần "Tôi") cộng 2 dòng độc thoại dùng "anh" (1253, 1427), và Paulette gọi Soutetsu bằng tên trần (19 dòng, cả file không có lần nào "anh Soutetsu"). Điểm riêng của file này là lỗi nhỏ về SFX: 6 dòng tiếng thở/gasp bị dịch sai (phiên âm La-tinh nguyên vẹn, sai nguyên âm, hoặc thành động từ "phá") trong khi cùng file đã có cách dịch đúng (929, 1008) — chứng tỏ người dịch không nhất quán chứ không phải không biết cách. Áp khối TOML trên sẽ sửa hết 47 dòng; không còn dòng nào chưa chắc chắn trong file này. Mọi bản sửa đều đã qua vòng đọc lại lần hai đối chiếu JP (40/40 đúng, 0 bị loại — gồm 37 bản vòng đầu và 3 bản bổ sung từ rà soát chéo với đợt quét gasp っ; 7 bản B4 bổ sung sau đó đã được Muse đối chiếu lại từng dòng với JP — xem Đính chính B4 cuối file). Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 6 lần vs "cô" 0 lần — cộng dồn "em" 57 vs "cô" 43. Hai file h1+h2 cộng lại sai 98/590 dòng (16,6%). Bước tiếp theo: audit các file Paulette h3–h8, rồi lr_h1/lr_h2/lr_稀咲h1/れいな02, theo thứ tự mức độ nghiêm trọng.

**Đính chính B4 19/11 22:24 (Hieu ủy quyền Muse chốt):** ngoại lệ tên rên BÃI BỎ — Paulette gọi Soutetsu bằng tên trần là sai ngay cả khi rên/kêu tên trong lúc thân mật, vì JP là 双鉄くん trong tất cả các dòng kiểm tra (không bao giờ bỏ くん, không bao giờ là さん hay tên trần).