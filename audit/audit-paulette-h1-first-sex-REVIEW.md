# Audit: Paulette h1_ファーストセックス — 51 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/ポーレットh1_ファーストセックス.txt.toml` — Cảnh tỏ tình rồi lần đầu làm tình của Paulette và Soutetsu tại căn hộ nhỏ của Paulette gần ga (căn 2K bên cạnh Rail Shop): Soutetsu thú nhận đã yêu Paulette, hai người trở thành người yêu, rồi quan hệ lần đầu. 298 dòng script đã đọc hết, đối chiếu từng dòng với JP gốc và TW (nhân chứng thứ hai).

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa toàn bộ 298 dòng (thoại 143: Soutetsu 65, Paulette 78; lời dẫn 155) đối chiếu JP + TW từ CSV "Trang tính 3" và TOML-2.
- **41 dòng sai (13,8%), 0 dòng chưa chắc chắn.** Thoại sai 40/143 (28,0%), lời dẫn sai 1/155 (0,6%). Theo người nói: Soutetsu 19/65, Paulette 21/78, lời dẫn 1/155.
- Phân loại: thuật ngữ 1, xưng hô 28, sai nghĩa 3, lỗi nhỏ 9; chưa dịch 0, cắt cụt 0, chưa chắc chắn 0.
- Heuristic (dấu thoại ↔ lời dẫn): shift 0 đạt 298/298 = 1,000; các shift khác 0,980–0,990 — không có shift nào vượt trội, không có key-shift sạch. TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất; 156 khác biệt thô chỉ ở `\n`/khoảng trắng — hiện tượng mất `\n` đã biết của TOML, 59% toàn dự án).
- 0 dòng CSV trống; VN==TW 0. `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 0 thẻ — **0 thẻ thiếu dấu `;` đóng**.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục); không có bản Việt nào trên 20 ký tự trong file trùng với file khác. Các bản Việt trùng trong file: "「!」" 1007/988/983 (JP đều 「っ！」, cả 3 đều sai cùng một lỗi mất tiếng hít — đã sửa cả 3 thành "Ư!"); "「A——」" 1005/996 (JP 「っ――」/「あんっ――」, TW 「啊」, đều đúng — tiếng hít đã được dịch thành âm, không tính sai).
- Không có file trùng lặp ở thư mục khác (đã kiểm tra md5 toàn bộ 227 file TOML-2; h1 và h2 mỗi file chỉ tồn tại 1 lần; 11 nhóm trùng đã biết từ trước đều không liên quan hai file này — Grand 04 vẫn là trường hợp trùng đã biết).
- Quét xưng hô bằng máy (đã chuẩn hoá `\n` thành khoảng trắng trước khi chạy regex `\b`): Soutetsu trong thoại tự xưng "anh" 12 dòng (tất cả sai), "Tôi" 0 lần; "em" 4 lần gọi Paulette (1038, 1103, 1134, 1089) vs "cô" 0 lần — hai lần "Cô ấy" tại 1742/1732 là ngôi thứ ba trong suy nghĩ của Soutetsu, không phải cách gọi, không tính vào tally. Paulette gọi "anh Soutetsu" 1 lần (1108) vs tên trần "Soutetsu" 30 lần / 27 dòng. "mình" trong độc thoại 5 dòng (1550, 1493, 1573, 1558, 1463) — tất cả đều đúng (sở hữu/phản thân/thành ngữ). "mình" ở CHAR 双鉄H 4 dòng: 1103 (phản thân, đúng), 1742 (sở hữu phản thân, đúng), 1727 (chủ ngữ độc lập, sai), 1732 (sở hữu phản thân, đúng).
- **Viết bản sửa bằng tay, không sửa hàng loạt bằng script (quy tắc 19/11 của Hieu):** mọi bản sửa trong file này đều được viết tay từng dòng từ JP (+TW) của chính dòng đó; script chỉ dùng để lắp ráp khối TOML từ các bản sửa đã viết, kiểm tra parse TOML và đối chiếu số key. Không có bản sửa nào do script sinh ra hay sửa đổi.
- **Kiểm tra lần hai (đọc lại toàn bộ bản sửa đối chiếu JP):** sau khi lắp khối TOML, đã đọc lại cả 40 bản sửa, từng dòng đối chiếu với JP gốc để xác nhận nghĩa, người nói và dấu câu — **tổng số bản sửa: 40; đã kiểm tra lại: 40; bị loại ở vòng hai: 0.** Sau đó, rà soát chéo với đợt quét gasp っ toàn dự án phát hiện thêm 1 dòng mất gasp cuối (1015) mà audit bỏ sót — đã xác minh lại đối chiếu JP và bổ sung (vòng bổ sung: 1/1 đúng, 0 bị loại), nâng tổng số lên **41 bản sửa, đã kiểm tra lại 41, bị loại 0.** Chỉ kiểm tra parse + khớp số key là chưa đủ; vòng đọc lại này là bắt buộc theo quy tắc của Hieu.
- **Rà soát chéo với đợt quét gasp っ toàn dự án:** sweep xác nhận 5/6 bản sửa gasp っ của audit (1007, 983, 984, 988, 995 — cùng giá trị sửa) và phát hiện thêm 1 dòng (1015 — xem trên). Dòng 1008 (JP 「っっ！！？」 → "ƯƯ!!?") không có trong danh sách sweep; bản sửa của audit giữ nguyên (không có giá trị sweep nào mâu thuẫn với nó).

## Kết luận về cơ chế lỗi

File này **sạch về cấu trúc** — 0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương — khác hẳn các file Paulette 02–05 trước đó. Lỗi tập trung ở hai lựa chọn hệ thống của người dịch:

1. **Soutetsu tự xưng "anh" trong thoại (12/12 lần tự xưng, 0 lần "Tôi")**, cộng thêm 1 dòng suy nghĩ dùng "Mình" làm chủ ngữ độc lập (1727). Đây là lỗi xưng hô lớn nhất của file, đúng với mẫu đã thấy ở mọi file Paulette trước đó.
2. **Paulette gọi Soutetsu bằng tên trần (27 dòng, 30 lần)**, trong khi cả file chỉ có đúng 1 lần "anh Soutetsu" (1108). Đây là lần đầu tiên quy tắc này được áp dụng có hệ thống: docs §2.4 quy định Paulette gọi Soutetsu là "Anh Soutetsu"; các file trước (P01: 4 lần "anh Soutetsu" / 0 lần tên trần; P02 sleeper: 7/0; P15: 4/0; P08: 6/0) đều tuân thủ, chỉ P16 có 7 lần tên trần nhưng 4 trong số đó đã được tính sai vì "cậu" và 3 lần còn lại bị bỏ sót. File h1 này — cùng với h2 — là nơi lỗi tên trần bùng phát: 27 dòng trong một file.

Ngoài ra còn một lỗi nhỏ có hệ thống: **tiếng hít っ bị mất** (5 dòng thoại chỉ còn dấu "!" trơ trọi, cộng 1 dòng mất gasp cuối sau dấu ~ — 1015, do đợt quét gasp っ phát hiện khi rà soát chéo), **chữ っ còn sót nguyên trong bản Việt** (984), và **tiếng thở ふぁ/ふあ bị dịch thành động từ "phá"** (3 dòng: 987, 976, và 1065 — dòng 1065 còn bịa thêm động từ "ngập tràn rồi" nên tính vào sai nghĩa). 3 dòng sai nghĩa còn lại đều là bịa thêm hoặc sai ngôi: 1106 tự bịa mệnh lệnh "đi anh!", 1157 dùng "em ấy" (ngôi thứ ba) cho chính người nói.

### Quy tắc tên trần vs tên rên (áp dụng trong file này, để Hieu duyệt lại)

Paulette gọi Soutetsu bằng tên trần **trong một câu nói hoàn chỉnh** là sai → sửa thành "anh Soutetsu" (15 dòng trong file này). **Ngoại lệ — giữ nguyên tên trần:** tên được rên/kêu độc lập trong lúc thân mật, hoặc nằm lẫn trong tiếng rên mà không có câu nói hoàn chỉnh quanh nó (12 dòng: 1002, 1022, 1057, 1106, 1109, 1157, 1167, 1181, 1183, 1184, 1185, 1186). Lưu ý: 1106 và 1157 thuộc ngoại lệ này nhưng vẫn bị tính sai vì lỗi khác (bịa thêm mệnh lệnh / sai ngôi "em ấy") — bản sửa của hai dòng đó chỉ sửa lỗi kia, vẫn giữ tên trần. Nếu Hieu muốn sửa cả tên rên thành "anh Soutetsu" thì 12 dòng ngoại lệ này sẽ cộng thêm vào danh sách.
**Đính chính B4 19/11 22:24 (Hieu ủy quyền Muse chốt):** ngoại lệ tên rên BÃI BỎ — Paulette gọi Soutetsu bằng tên trần là sai ngay cả khi rên/kêu tên trong lúc thân mật, vì JP là 双鉄くん trong tất cả các dòng kiểm tra (không bao giờ bỏ くん, không bao giờ là さん hay tên trần). 12 dòng này nay đều đã sửa; h1 41→51.

## Chi tiết dòng sai

### Thuật ngữ (1 dòng)

**1483 [lời dẫn]** — 御一夜鉄道社長 — "Ohimitera" sai theo quyết định 19/11; đúng là "Ohitoyo".

- JP: その一室は、御一夜市長兼御一夜鉄道社長の住処とは
とても信じられないほどの、ごくごく質素な佇まいだ。
- TW: 房間裡看起來十分樸素，甚至讓人不敢相信這裡是御一夜市長兼御一夜鐵道社長的住處。
- Cũ: Căn phòng mang một vẻ ngoài vô cùng giản dị,
đến mức khó tin đây lại là nơi ở của Thị trưởng kiêm Giám đốc Đường sắt Ohimitera.
- Sửa: Căn phòng mang một vẻ ngoài vô cùng giản dị,
đến mức khó tin đây lại là nơi ở của Thị trưởng kiêm Giám đốc Đường sắt Ohitoyo.

### Xưng hô (28 dòng)

**926 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「くぱくぱ……ひくついちゃってる、ところ……が……
双鉄くんが……おちんちん、挿れる……専用の、場所っ」
- TW: 「一張一合的……那個地方…………就是專門給雙鐵君……你小雞雞的……插進去的地方」
- Cũ: 「Cái chỗ... đang mấp máy, co giật đó...
là nơi, dành riêng... để Soutetsu... đút dương vật vào.」
- Sửa: 「Cái chỗ... đang mấp máy, co giật đó...
là nơi, dành riêng... để anh Soutetsu... đút dương vật vào.」

**1036 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4; trong file Paulette vẫn xưng "anh" với Soutetsu ở các dòng khác).

- JP: 「はい。今からわたし……ええと、おくち、で……
双鉄くんのおちん、ちん。きれいきれいにします、けど」
- TW: 「嗯。現在我就用……那個，我的嘴來……把你的雞雞，來弄乾淨」
- Cũ: 「Vâng. Bây giờ em sẽ... à ừm, dùng miệng... để làm sạch,
cho cậu nhỏ của Soutetsu, nhưng mà.」
- Sửa: 「Vâng. Bây giờ em sẽ... à ừm, dùng miệng... để làm sạch,
cho cậu nhỏ của anh Soutetsu, nhưng mà.」

**1044 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「はい！　双鉄くん」
- TW: 「嗯！雙鐵君」
- Cũ: 「Vâng! Soutetsu.」
- Sửa: 「Vâng! Anh Soutetsu.」

**1047 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「あ、ですよね。
双鉄くん、そう言ってくれてたのに――」
- TW: 「嗯，是啊。既然你都這麼說了——」
- Cũ: 「A, đúng rồi nhỉ.
Soutetsu đã nói vậy mà——」
- Sửa: 「A, đúng rồi nhỉ.
Anh Soutetsu đã nói vậy mà——」

**1052 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「わたし、いきなり触っちゃったから。双鉄くん、
びっくりして射精、きっとしちゃったんですね」
- TW: 「因為我一下子摸上去了，你一定是嚇了一跳，然後就射了」
- Cũ: 「Tại em tự dưng chạm vào. Nên Soutetsu,
chắc hẳn đã giật mình và xuất tinh rồi nhỉ.」
- Sửa: 「Tại em tự dưng chạm vào. Nên anh Soutetsu,
chắc hẳn đã giật mình và xuất tinh rồi nhỉ.」

**1053 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「恋人同士がする、コト――したいって、思ったからです。
双鉄くんとの……確かな絆が、欲しくって」
- TW: 「因為我想做，男女朋友之間做的事情。我想跟你……建立起牢固的關係」
- Cũ: 「Vì em nghĩ là, em muốn làm chuyện... mà những người yêu nhau hay làm.
Em muốn có... một sự gắn kết vững chắc với Soutetsu.」
- Sửa: 「Vì em nghĩ là, em muốn làm chuyện... mà những người yêu nhau hay làm.
Em muốn có... một sự gắn kết vững chắc với anh Soutetsu.」

**1066 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「わかった」
- TW: 「好的」
- Cũ: 「Anh hiểu rồi.」
- Sửa: 「Tôi hiểu rồi.」

**1081 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「う……嬉しい、です……わたしの、おっぱい――
双鉄、くんに……気にいって、もらえ、て……んっ」
- TW: 「我……我好高興……你能喜歡……我的胸……」
- Cũ: 「Ư... em vui, lắm... ngực của, em——
được Soutetsu, thích... như vậy... ưm.」
- Sửa: 「Ư... em vui, lắm... ngực của, em——
được anh Soutetsu, thích... như vậy... ưm.」

**1084 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「僕もだ」
- TW: 「我也是」
- Cũ: 「Anh cũng vậy.」
- Sửa: 「Tôi cũng vậy.」

**1089 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi" (3 lần).

- JP: 「僕は、ポーレットが大好きだから。
ポーレットとひとつになりたい。セックス、したい」
- TW: 「我好愛你，波萊特。我想跟你合為一體，想跟你做愛」
- Cũ: 「Vì anh rất yêu Paulette.
Anh muốn hòa làm một với em. Anh muốn làm tình.」
- Sửa: 「Vì tôi rất yêu Paulette.
Tôi muốn hòa làm một với em. Tôi muốn làm tình.」

**1095 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi" (2 lần).

- JP: 「僕は、嬉しい。ポーレットの体が固いおかげで、
こんなに綺麗な姿を、目近に見られるのだから」
- TW: 「我很高興。正因為你身體這麼硬，我才能從這麼近的地方看著美妙的你」
- Cũ: 「Anh thấy vui lắm. Nhờ cơ thể Paulette hơi cứng,
mà anh mới có thể nhìn thấy dáng vẻ xinh đẹp này ở khoảng cách gần đến thế.」
- Sửa: 「Tôi thấy vui lắm. Nhờ cơ thể Paulette hơi cứng,
mà tôi mới có thể nhìn thấy dáng vẻ xinh đẹp này ở khoảng cách gần đến thế.」

**1098 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi" (2 lần).

- JP: 「ポーレットの裸を見たいと思うし、触れたいとも思う。
今まではまるで感じなかったが、今は、そう感じている」
- TW: 「我現在想看到，也想摸到你的裸體。以前我都沒有這種想法，現在我卻有了」
- Cũ: 「Anh muốn nhìn thấy cơ thể trần trụi của Paulette, cũng muốn chạm vào nó.
Trước đây anh hoàn toàn không có cảm giác này, nhưng bây giờ thì có.」
- Sửa: 「Tôi muốn nhìn thấy cơ thể trần trụi của Paulette, cũng muốn chạm vào nó.
Trước đây tôi hoàn toàn không có cảm giác này, nhưng bây giờ thì có.」

**1102 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「射精っ――する――からっ――、一緒――、一緒、にっ」
- TW: 「我要——射了，我們一起、一起」
- Cũ: 「Anh xuất tinh——đây——cùng nhau——cùng nhau, nhé.」
- Sửa: 「Tôi xuất tinh——đây——cùng nhau——cùng nhau, nhé.」

**1103 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi" (3 lần). "mình" sau "Tôi đã nhận ra" là phản thân, giữ nguyên.

- JP: 「僕は、変わったのだと思う。
ポーレット、君に恋して。恋をしてたと、自覚して」
- TW: 「我覺得我變了。波萊特，我愛上了你。我發現了自己愛上了你」
- Cũ: 「Anh nghĩ là anh đã thay đổi rồi.
Paulette, anh yêu em. Anh đã nhận ra mình đang yêu em.」
- Sửa: 「Tôi nghĩ là tôi đã thay đổi rồi.
Paulette, tôi yêu em. Tôi đã nhận ra mình đang yêu em.」

**1111 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「割れ目の、外の唇みたいな……大陰唇を、
双鉄くん――双鉄くんの指で、広げてください」
- TW: 「把縫隙的外面那層嘴唇一樣的……大陰唇，你、你用手指翻開吧」
- Cũ: 「Ở rãnh nứt, cái chỗ giống như môi bên ngoài ấy... môi lớn,
Soutetsu——anh hãy dùng ngón tay, vạch nó ra đi.」
- Sửa: 「Ở rãnh nứt, cái chỗ giống như môi bên ngoài ấy... môi lớn,
Anh Soutetsu——anh hãy dùng ngón tay, vạch nó ra đi.」

**1120 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「そうだな、僕もドキドキしている」
- TW: 「是啊，我心跳也很快」
- Cũ: 「Đúng vậy, tim anh cũng đang đập rất nhanh.」
- Sửa: 「Đúng vậy, tim tôi cũng đang đập rất nhanh.」

**1123 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「はい、わたし。
双鉄くんと、セックスしたいって思っています」
- TW: 「是的。我想跟你做愛」
- Cũ: 「Vâng. Em.
Em muốn làm tình với Soutetsu.」
- Sửa: 「Vâng. Em.
Em muốn làm tình với anh Soutetsu.」

**1133 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「ポーレット……僕は――射精――しそう」
- TW: 「波萊特……我要射了」
- Cũ: 「Paulette... anh——sắp——xuất tinh rồi.」
- Sửa: 「Paulette... tôi——sắp——xuất tinh rồi.」

**1134 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「ポーレット。
僕は、君の裸を――おっぱいを見たい」
- TW: 「波萊特。我想看你的裸體……你的胸」
- Cũ: 「Paulette.
Anh muốn nhìn thấy cơ thể trần trụi của em——muốn nhìn ngực em.」
- Sửa: 「Paulette.
Tôi muốn nhìn thấy cơ thể trần trụi của em——muốn nhìn ngực em.」

**1138 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi".

- JP: 「ポーレット――、一つに――僕と、ひとつに」
- TW: 「波萊特，跟我合為一體吧」
- Cũ: 「Paulette——, hãy hòa làm một——hòa làm một với anh nhé.」
- Sửa: 「Paulette——, hãy hòa làm một——hòa làm một với tôi nhé.」

**1139 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「きれいきれいにしやすいように、ね？　双鉄くん、
膝立ちになってくれますか？」
- TW: 「為了方便我把他弄乾淨，雙鐵君，你能跪在地上嗎？」
- Cũ: 「Để dễ dàng làm sạch hơn nhé? Soutetsu,
anh có thể quỳ gối lên được không?」
- Sửa: 「Để dễ dàng làm sạch hơn nhé? Anh Soutetsu,
anh có thể quỳ gối lên được không?」

**1145 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「それで、あの――
今日、わたしが、双鉄くんをおうちに誘ったのは、その」
- TW: 「然後，那個……今天我請你來我家，是那個……」
- Cũ: 「Và, à thì——
Hôm nay, em rủ Soutetsu về nhà là vì, chuyện đó.」
- Sửa: 「Và, à thì——
Hôm nay, em rủ anh Soutetsu về nhà là vì, chuyện đó.」

**1149 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại → "Tôi"; "người yêu của anh" → "người yêu của tôi".

- JP: 「無論だ。
僕は既に、ポーレットは僕の恋人なのだと思っている」
- TW: 「當然了。我已經把你當作我的女朋友了」
- Cũ: 「Đương nhiên rồi.
Anh đã coi Paulette là người yêu của anh rồi.」
- Sửa: 「Đương nhiên rồi.
Tôi đã coi Paulette là người yêu của tôi rồi.」

**1169 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4; cùng dòng Paulette vẫn gọi "tim anh").

- JP: 「ほんと……双鉄くん、すごく、ドキドキ、してますね」
- TW: 「還真是……你的心跳好快」
- Cũ: 「Thật này... Soutetsu, tim anh, đang đập, rất nhanh nhỉ.」
- Sửa: 「Thật này... Anh Soutetsu, tim anh, đang đập, rất nhanh nhỉ.」

**1176 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「あの、ええと、違うんです！　双鉄くん」
- TW: 「那個，呃，不是的！雙鐵君」
- Cũ: 「À, ừm, không phải đâu! Soutetsu.」
- Sửa: 「À, ừm, không phải đâu! Anh Soutetsu.」

**1178 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4; cả 2 lần trong dòng).

- JP: 「初めて……一番最初は。双鉄くんの、そのっ……精、子。
双鉄くんの分身を、子宮に、わたし、もらいたいんです」
- TW: 「開始……第一次，我想要你的……精子。我想用子宮，接納你的分身」
- Cũ: 「Lần đầu tiên... ngay từ lần đầu tiên. Em muốn nhận lấy... t, tinh trùng của Soutetsu.
Em muốn đón nhận phân thân của Soutetsu, vào trong tử cung của em.」
- Sửa: 「Lần đầu tiên... ngay từ lần đầu tiên. Em muốn nhận lấy... t, tinh trùng của anh Soutetsu.
Em muốn đón nhận phân thân của anh Soutetsu, vào trong tử cung của em.」

**1182 [Paulette]** — Paulette gọi Soutetsu bằng tên trần "Soutetsu" trong câu nói → "anh Soutetsu" (docs §2.4).

- JP: 「双鉄くん……わたしのはだか、とか――
お風呂……登呂流湯で、見てるじゃないですか」
- TW: 「雙鐵……我的裸體的話，你不是洗澡的時候……在登呂湯浴場已經看過了嗎」
- Cũ: 「Soutetsu... cơ thể khỏa thân của em... chẳng phải anh
đã thấy lúc tắm... ở Tororyu-yu rồi sao.」
- Sửa: 「Anh Soutetsu... cơ thể khỏa thân của em... chẳng phải anh
đã thấy lúc tắm... ở Tororyu-yu rồi sao.」

**1727 [Soutetsu]** — Suy nghĩ của Soutetsu dùng "Mình" làm chủ ngữ độc lập → "Tôi" (tiền lệ P02 sleeper 2339/2590, hearing 2580/2584/2586/2590).

- JP: （そうか……射精か――
僕は、ポーレットに触れられることで、射精をしたのか）
- TW: （啊……射精啊——波萊特只是摸了我一下，我就射精了）
- Cũ: （Ra vậy... xuất tinh sao——
Mình đã xuất tinh, chỉ vì được Paulette chạm vào à.）
- Sửa: （Ra vậy... xuất tinh sao——
Tôi đã xuất tinh, chỉ vì được Paulette chạm vào à.）

### Sai nghĩa (3 dòng)

**1065 [Paulette]** — Bản cũ tự bịa thêm động từ "ngập tràn rồi" — JP chỉ là danh sách từ ngắt quãng (しきゅうっ――んっ――おまんこ), không có động từ "đầy". Đồng thời "phá" (ふぁっ) là tiếng thở, không phải động từ "phá" → "phà".

- JP: 「あつ、いっ――んっ――すごい……いっぱい……
ふぁっ――しきゅ、うっ――んっ――おま、ん、こ」
- TW: 「好燙——嗯——好厲害……這麼多…………呼——在子宮裡——在小穴裡」
- Cũ: 「Nóng, quá——ưm——tuyệt quá... nhiều... thật...
phá——tử cung, ưm——âm đạo, ngập tràn rồi.」
- Sửa: 「Nóng, quá——ưm——tuyệt quá... nhiều... thật...
phà——tử cung, ưm——âm đạo.」

**1106 [Paulette]** — Bản cũ tự bịa thêm mệnh lệnh "đi anh!" — JP kết bằng tiếng hít んきゅっ, không có mệnh lệnh. Nay sửa thành "anh Soutetsu" theo quyết định B4 19/11 (ngoại lệ tên rên bãi bỏ).

- JP: 「だからッ――ん、動い、て……あ……
双鉄、くん、を――わたし、の――なか――んきゅっ！」
- TW: 「所以——嗯——動起來吧——啊……雙鐵君——在我裡面——嗯！」
- Cũ: 「Nên là——ưm, hãy di, chuyển... a...
Soutetsu, này——bên trong, em——ưm, đi anh!」
- Sửa: 「Nên là——ưm, hãy di, chuyển... a...
Soutetsu, này——bên trong, em——ưm!」

**1157 [Paulette]** — "em ấy" là ngôi thứ ba, người nói là Paulette nói về chính mình → "em". Nay sửa thành "anh Soutetsu" theo quyết định B4 19/11 (ngoại lệ tên rên bãi bỏ).

- JP: 「ぐりって――うれし、いっ――スタンプ――
双鉄くんの――ものって――わたしっ――んっ」
- TW: 「蹭到了——我好開心——被蓋上章了——我變成——雙鐵君的——東西了——嗯」
- Cũ: 「Bị cọ xát——vui, quá——như bị đóng dấu——
là đồ của——Soutetsu——em ấy——ưm.」
- Sửa: 「Bị cọ xát——vui, quá——như bị đóng dấu——
là đồ của——Soutetsu——em——ưm.」

### Lỗi nhỏ (9 dòng)

**976 [Paulette]** — JP ふああっ là tiếng thở; bản cũ "phá!!!" đọc thành động từ "phá" → "phà!!!".

- JP: 「ひゃっ――あっ――子宮っ――子宮、に――キスっ――
ふああっ！！！」
- TW: 「呀——啊——子宮——子宮——被親到了——哇啊！！！」
- Cũ: 「Hya——á——tử cung——vào, tử cung——bị hôn——
phá!!!」
- Sửa: 「Hya——á——tử cung——vào, tử cung——bị hôn——
phà!!!」

**983 [Soutetsu]** — JP chỉ là tiếng hít 「っ！」, TW có âm (呃), bản Việt chỉ còn dấu "!" — mất tiếng hít → "Ư!".

- JP: 「っ！」
- TW: 「呃！」
- Cũ: 「!」
- Sửa: 「Ư!」

**984 [Soutetsu]** — Bản Việt còn nguyên chữ っ tiếng Nhật ("~っ!") — JP 「～っ！」 là tiếng hít cuối câu → "~Ư!".

- JP: 「～っ！」
- TW: 「呃～！」
- Cũ: 「~っ!」
- Sửa: 「~Ư!」

**987 [Paulette]** — JP ふぁっ là tiếng thở; bản cũ "Phá." đọc thành động từ "phá" (đập vỡ) → "Phà.".

- JP: 「ふぁっ」
- TW: 「呼」
- Cũ: 「Phá.」
- Sửa: 「Phà.」

**988 [Soutetsu]** — JP chỉ là tiếng hít 「っ！」, TW có âm (呼), bản Việt chỉ còn dấu "!" — mất tiếng hít → "Ư!".

- JP: 「っ！」
- TW: 「呼！」
- Cũ: 「!」
- Sửa: 「Ư!」

**995 [Soutetsu]** — JP 「っ！！！」 mất tiếng hít → "Ư!!!".

- JP: 「っ！！！」
- TW: 「唔！！！」
- Cũ: 「!!!」
- Sửa: 「Ư!!!」

**1007 [Soutetsu]** — JP chỉ là tiếng hít 「っ！」, TW có âm (啊), bản Việt chỉ còn dấu "!" — mất tiếng hít → "Ư!".

- JP: 「っ！」
- TW: 「啊！」
- Cũ: 「!」
- Sửa: 「Ư!」

**1008 [Soutetsu]** — JP 「っっ！！？」 mất tiếng hít → "ƯƯ!!?".

- JP: 「っっ！！？」
- TW: 「啊！！？」
- Cũ: 「!!?」
- Sửa: 「ƯƯ!!?」

**1015 [Paulette]** — JP kết bằng tiếng hít sau dấu ~ (ん～っ); bản Việt giữ ~ nhưng mất tiếng hít → thêm Ư. Dòng này do đợt quét gasp っ toàn dự án phát hiện khi rà soát chéo (audit bỏ sót); đã xác minh lại đối chiếu JP trước khi bổ sung.

- JP: 「れるっ――れムッ――ちゅっ――ちゅむっ――ん～っ」
- TW: 「啾嚕——啾嚕——啾——啾嚕——嗯」
- Cũ: 「Liếm——ưm——chụt——chùn chụt——ưm~」
- Sửa: 「Liếm——ưm——chụt——chùn chụt——ưm~Ư」

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
926 = "「Cái chỗ... đang mấp máy, co giật đó...\nlà nơi, dành riêng... để anh Soutetsu... đút dương vật vào.」"
976 = "「Hya——á——tử cung——vào, tử cung——bị hôn——\nphà!!!」"
983 = "「Ư!」"
984 = "「~Ư!」"
987 = "「Phà.」"
988 = "「Ư!」"
995 = "「Ư!!!」"
1002 = "「A... ưm... phù——ưm——anh Soutetsu, này——\nAnh rất, thích... ngực... nhỉ.」"
1007 = "「Ư!」"
1008 = "「ƯƯ!!?」"
1015 = "「Liếm——ưm——chụt——chùn chụt——ưm~Ư」"
1022 = "「Ư——ưm——anh Soutetsu——anh Soutetsu——」"
1036 = "「Vâng. Bây giờ em sẽ... à ừm, dùng miệng... để làm sạch,\ncho cậu nhỏ của anh Soutetsu, nhưng mà.」"
1044 = "「Vâng! Anh Soutetsu.」"
1047 = "「A, đúng rồi nhỉ.\nAnh Soutetsu đã nói vậy mà——」"
1052 = "「Tại em tự dưng chạm vào. Nên anh Soutetsu,\nchắc hẳn đã giật mình và xuất tinh rồi nhỉ.」"
1053 = "「Vì em nghĩ là, em muốn làm chuyện... mà những người yêu nhau hay làm.\nEm muốn có... một sự gắn kết vững chắc với anh Soutetsu.」"
1057 = "「Vâng——anh Soutetsu, này——em——em——này」"
1065 = "「Nóng, quá——ưm——tuyệt quá... nhiều... thật...\nphà——tử cung, ưm——âm đạo.」"
1066 = "「Tôi hiểu rồi.」"
1081 = "「Ư... em vui, lắm... ngực của, em——\nđược anh Soutetsu, thích... như vậy... ưm.」"
1084 = "「Tôi cũng vậy.」"
1089 = "「Vì tôi rất yêu Paulette.\nTôi muốn hòa làm một với em. Tôi muốn làm tình.」"
1095 = "「Tôi thấy vui lắm. Nhờ cơ thể Paulette hơi cứng,\nmà tôi mới có thể nhìn thấy dáng vẻ xinh đẹp này ở khoảng cách gần đến thế.」"
1098 = "「Tôi muốn nhìn thấy cơ thể trần trụi của Paulette, cũng muốn chạm vào nó.\nTrước đây tôi hoàn toàn không có cảm giác này, nhưng bây giờ thì có.」"
1102 = "「Tôi xuất tinh——đây——cùng nhau——cùng nhau, nhé.」"
1103 = "「Tôi nghĩ là tôi đã thay đổi rồi.\nPaulette, tôi yêu em. Tôi đã nhận ra mình đang yêu em.」"
1106 = "「Nên là——ưm, hãy di, chuyển... a...\nanh Soutetsu, này——bên trong, em——ưm!」"
1109 = "「Xin hãy——đón nhận em——ưm——anh Soutetsu, này——\nHãy cho em——làm——cô dâu, của anh——nhé——ưm.」"
1111 = "「Ở rãnh nứt, cái chỗ giống như môi bên ngoài ấy... môi lớn,\nAnh Soutetsu——anh hãy dùng ngón tay, vạch nó ra đi.」"
1120 = "「Đúng vậy, tim tôi cũng đang đập rất nhanh.」"
1123 = "「Vâng. Em.\nEm muốn làm tình với anh Soutetsu.」"
1133 = "「Paulette... tôi——sắp——xuất tinh rồi.」"
1134 = "「Paulette.\nTôi muốn nhìn thấy cơ thể trần trụi của em——muốn nhìn ngực em.」"
1138 = "「Paulette——, hãy hòa làm một——hòa làm một với tôi nhé.」"
1139 = "「Để dễ dàng làm sạch hơn nhé? Anh Soutetsu,\nanh có thể quỳ gối lên được không?」"
1145 = "「Và, à thì——\nHôm nay, em rủ anh Soutetsu về nhà là vì, chuyện đó.」"
1149 = "「Đương nhiên rồi.\nTôi đã coi Paulette là người yêu của tôi rồi.」"
1157 = "「Bị cọ xát——vui, quá——như bị đóng dấu——\nlà đồ của——anh Soutetsu——em——ưm.」"
1167 = "「Vào... rồi, này——ưm——nóng, quá——\nCủa anh Soutetsu, này——vào hết——á——trong em, rồi.」"
1169 = "「Thật này... Anh Soutetsu, tim anh, đang đập, rất nhanh nhỉ.」"
1176 = "「À, ừm, không phải đâu! Anh Soutetsu.」"
1178 = "「Lần đầu tiên... ngay từ lần đầu tiên. Em muốn nhận lấy... t, tinh trùng của anh Soutetsu.\nEm muốn đón nhận phân thân của anh Soutetsu, vào trong tử cung của em.」"
1181 = "「anh Soutetsu... này——ưm——chụt——chùn chụt.」"
1182 = "「Anh Soutetsu... cơ thể khỏa thân của em... chẳng phải anh\nđã thấy lúc tắm... ở Tororyu-yu rồi sao.」"
1183 = "「Sou, tetsu——này——á——ưm——\nanh Soutetsu, này.」"
1184 = "「anh Soutetsu——này——á——yêu anh! Yêu anh lắm!」"
1185 = "「anh Soutetsu...」"
1186 = "「anh Soutetsu... anh Soutetsu.」"
1483 = "Căn phòng mang một vẻ ngoài vô cùng giản dị,\nđến mức khó tin đây lại là nơi ở của Thị trưởng kiêm Giám đốc Đường sắt Ohitoyo."
1727 = "（Ra vậy... xuất tinh sao——\nTôi đã xuất tinh, chỉ vì được Paulette chạm vào à.）"
```

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- Soutetsu gọi Paulette "em" 4 lần (1038, 1103, 1134, 1089) vs "cô" 0 lần — cộng dồn toàn dự án sau file này: **"em" 51 vs "cô" 43**. "Em" tiếp tục dẫn trước (sau P02 là 47 vs 43). Không quyết định, chỉ ghi nhận.
- 御一夜: "Ohimitera" 1 lần (1483 — đã sửa trong file này), "Ohito" 0 lần, "Ohitoyo" 0 lần. Đây là lần "Ohimitera" duy nhất còn sót trong file (không còn dòng đúng nào dùng dạng cũ để thống nhất sau).
- Không có 湯医 / 帝鉄 / コン / タブレット / 整備体 / 運転ボディ / マスコン / 宮司 / KiHa trong file này — không có bằng chứng mới cho các quyết định đang chờ đó.

## Đề xuất cập nhật context (chưa chốt)

- **Thêm quy tắc tên trần → "anh Soutetsu" với ngoại lệ tên rên vào docs §2.4 (và context_trans.md):** Paulette gọi Soutetsu bằng tên trần trong câu nói hoàn chỉnh là sai → "anh Soutetsu"; tên rên độc lập/kèm tiếng rên trong lúc thân mật giữ nguyên tên trần. Quy tắc này đã áp dụng ở h1 (15 dòng sửa + 12 dòng tên rên nay cũng sửa) và h2 (11 dòng sửa + 8 dòng tên rên nay cũng sửa); ngoại lệ đã bị bãi bỏ theo quyết định B4 19/11 (Hieu ủy quyền Muse chốt) — áp dụng cho các file h còn lại. Lưu ý: P16 còn 3 dòng tên trần chưa được tính sai (2008, 2015, 2016) — đưa vào đợt thống nhất sau.
- **Thêm quy tắc tiếng thở fa/fu vào sfx_and_emoticons.md:** ふぁ/ふあ/ふぇ là tiếng thở, dịch thành âm thở tiếng Việt ("phà", "phù", "phê", "phùa") — KHÔNG dịch thành động từ "phá", KHÔNG để nguyên dạng phiên âm La-tinh ("fuya", "fua...an"). Bằng chứng: h1 có 3 dòng "phá" (987, 976, 1065), h2 có 6 dòng cùng mẫu (932, 991, 956, 957, 923, 963).

## Đã kiểm tra và KHÔNG tính là sai

- **1005 (JP 「っ――」, TW 「啊」, VN 「A——」) và 996 (JP 「あんっ――」, VN 「A——」):** tiếng hít đã được dịch thành âm ("A"), TW xác nhận — có cách dịch, không phải mất tiếng hít.
- **1742, 1732 ("núm vú/dương vật của mình" trong suy nghĩ của Soutetsu):** sở hữu phản thân, đúng. 1103 "mình" sau "Tôi đã nhận ra" đúng mẫu "Tôi… mình…".
- **1728 (（ぱっ！） → "（Phụt!）"):** tiếng bật khi rút ra, TW 啪 (tiếng bật) không mâu thuẫn mạnh — giữ nguyên.
- **1739 (（びゅくっ！！！！） → "（Giật nảy!!!!）"):** tiếng xuất tinh dịch thành cơn giật — chấp nhận được trong ngữ cảnh, giữ nguyên.
- **1754 (（ちぃ……ぃっ） → "（Xoạch...）"):** tiếng kéo khóa — ranh giới, giữ nguyên. 1740 (（くぷっ） → "（Phập）"), 1724 (（ごりゅ！） → "（Đâm phập!）") — đều là cách dịch SFX hợp lý, giữ nguyên.
- **1000 ("âm đạo của, con gái"):** cách dịch ngắt quãng hơi vụng của おんなのこの、おまんこ nhưng nghĩa đã đủ; thì "sẽ ướt" so với 濡れる chỉ là sắc thái, không tính sai.
- **1026 ("v, âng——... lần đầu, tiên..."):** nói lắp được cách điệu, chấp nhận được.
- **1041, 1019, 1010, 1012, 1171:** SFX れろっ→"liếm", ちゅっ→"chụt", ぺろっ→"liếm" — nhất quán trong file, giữ nguyên.
- **1045 (むっ → "Hử!?"), 1042 (ああ → "Ừm!"), 1027 (ん……くっ → "Ưm... hự."):** tiếng hít đã dịch thành âm, giữ nguyên.
- **1558, 1732 (CHAR monologue/DISP Paulette nhưng góc nhìn Soutetsu; "của mình" phản thân):** đúng, không tính sai.
- **"Cô ấy" tại 1742/1732** là ngôi thứ ba trong suy nghĩ, KHÔNG phải Soutetsu gọi Paulette bằng "cô" — đã loại khỏi tally "cô" vs "em".

## Kết bài

ポーレットh1_ファーストセックス sai 51/298 dòng (17,1%) — file h đầu tiên của tuyến Paulette, và là file sạch về cấu trúc: 0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi. Lỗi tập trung ở hai lựa chọn hệ thống của người dịch: Soutetsu tự xưng "anh" trong thoại (12/12 lần tự xưng, 0 lần "Tôi") và Paulette gọi Soutetsu bằng tên trần (27 dòng, chỉ 1 lần đúng "anh Soutetsu" ở 1108) — cùng với lỗi nhỏ có hệ thống về tiếng hít っ (5 dòng mất cả dòng, 1 dòng mất gasp cuối, 1 dòng còn sót chữ っ) và tiếng thở ふぁ dịch thành động từ "phá" (3 dòng). Áp khối TOML trên sẽ sửa hết 51 dòng; không còn dòng nào chưa chắc chắn trong file này. Mọi bản sửa đều đã qua vòng đọc lại lần hai đối chiếu JP (41/41 đúng, 0 bị loại — gồm 40 bản vòng đầu và 1 bản bổ sung từ rà soát chéo với đợt quét gasp っ; 10 bản B4 bổ sung sau đó đã được Muse đối chiếu lại từng dòng với JP — xem Đính chính B4 cuối file). Quy tắc tên trần vs tên rên đã chốt theo quyết định B4 19/11 (Hieu ủy quyền Muse chốt): ngoại lệ tên rên bãi bỏ, 12 dòng tên rên nay đều sửa thành "anh Soutetsu"; h1 41→51. Bằng chứng mới cho quyết định đang chờ: Soutetsu gọi Paulette "em" 4 lần vs "cô" 0 lần — cộng dồn "em" 51 vs "cô" 43. Bước tiếp theo: audit h2 (đã xong cùng đợt này), rồi các file Paulette h3–h8 theo thứ tự mức độ nghiêm trọng.

**Đính chính B4 19/11 22:24 (Hieu ủy quyền Muse chốt):** ngoại lệ tên rên BÃI BỎ — Paulette gọi Soutetsu bằng tên trần là sai ngay cả khi rên/kêu tên trong lúc thân mật, vì JP là 双鉄くん trong tất cả các dòng kiểm tra (không bao giờ bỏ くん, không bao giờ là さん hay tên trần).