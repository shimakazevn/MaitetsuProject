# Audit: Paulette 02_古地図 — 41 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/ポーレット02_古地図.txt.toml` — Soutetsu cùng Paulette, Hibiki, Reina, Nagi, Fukami, Mayami đến đền gặp thầy tế Akai để tìm hiểu về bản đồ cổ, ngựa Kiji và mỏ than Jutsu-sen; có cảnh bàn về công nhận Di sản Văn hóa và hộp cơm nhà ga Ohitoyo. 385 dòng script đã đọc hết, đối chiếu từng dòng với JP gốc và TW (nhân chứng thứ hai).

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa toàn bộ 385 dòng (thoại 241: Soutetsu 88, Paulette 63, Akai 39, Hibiki 17, Reina 12, Hachiroku 8, Fukami 5, Mayami 5, Nagi 4; lời dẫn 144) đối chiếu JP + TW từ CSV "Trang tính 3" và TOML-2.
- **41 dòng sai (10,6%), 0 dòng chưa chắc chắn.** Thoại sai 34/241 (14.1%), lời dẫn sai 7/144 (4.9%). Theo người nói: 双鉄 23/88, monologue 7/144, ポーレット 4/63, 赤井宮司 4/39, 日々姫 1/17, 真闇 1/5, ふかみ 1/5.
- Phân loại: thuật ngữ 25, xưng hô 9, sai nghĩa 4, lỗi nhỏ 3; lệch vị trí 0, chưa dịch 0, cắt cụt 0, chưa chắc chắn 0.
- Heuristic (dấu thoại ↔ lời dẫn) báo 0 dòng — bắt được 0/41 (file không có lỗi lệch vị trí nên không có gì để bắt). Heuristic dấu phẩy kiểu MT báo 15 dòng — kiểm tra tay: 0 dòng trong số đó sai vì dấu phẩy (đều là dấu phẩy đúng).
- Không key-shift sạch (shift 0: 385/385; các shift khác cũng 1,000 vì dấu thoại/lời dẫn trùng khớp ở mọi shift — kiểm tra không cho thông tin thêm). TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất; 240 khác biệt thô chỉ ở `\n`/khoảng trắng).
- 0 dòng CSV trống; VN==TW 0. `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 12 thẻ, VN có 12 thẻ — **0 thẻ thiếu dấu `;` đóng** (khác Paulette 13: 5 thẻ thiếu `;`). Không có thẻ `%l` nào thừa/thiếu giữa JP và VN.
- **Lệch vị trí 0 cặp, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm tra bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục); các bản Việt trùng lặp trong file chỉ có "「Vâng。」" 1895/1728 (JP đều là 「はい」, đều đúng) và các bản Việt trùng với file khác đều là câu ngắn thông dụng, đúng với JP của mình.
- Không có file trùng lặp ở thư mục khác (đã kiểm tra md5 toàn bộ 227 file TOML-2; Grand 04 vẫn là file trùng duy nhất trong dự án).
- Quét xưng hô bằng máy (đã chuẩn hoá `\n` thành khoảng trắng trước khi chạy regex `\b`, không phân biệt hoa/thường — quét lần đầu bỏ sót "Anh" viết hoa đầu câu): Soutetsu trong thoại tự xưng "anh" 9 lần (tất cả sai), "tôi" 1 lần (1617, đúng — chỉ sai từ "cháu" làm chủ thể), "cháu" 4 lần (1635, 1826, 1832, 2030 — với thầy Akai, đúng), "em" 6 lần (1706, 1732, 1840, 1871, 1961, 2056 — đều là gọi người khác, không phải tự xưng). "mình" trong độc thoại 6 dòng — tất cả đều đúng (sở hữu "của mình", phản thân "nhốt mình", thành ngữ "giật mình"/"một mình", mệnh đề lồng "nghĩ mình đã nghe nhầm").
- **Viết bản sửa bằng tay, không sửa hàng loạt bằng script (quy tắc 19/11 của Hieu):** mọi bản sửa trong file này đều được viết tay từng dòng từ JP (+TW) của chính dòng đó; script chỉ dùng để lắp ráp khối TOML từ các bản sửa đã viết, kiểm tra parse TOML và đối chiếu số key. Không có bản sửa nào do script sinh ra hay sửa đổi.
- **Kiểm tra lần hai (đọc lại toàn bộ bản sửa đối chiếu JP):** sau khi lắp khối TOML, đã đọc lại cả 41 bản sửa, từng dòng đối chiếu với JP gốc để xác nhận nghĩa, người nói và dấu câu — **tổng số bản sửa: 41; đã kiểm tra lại: 41; bị loại ở vòng hai: 0.** Chỉ kiểm tra parse + khớp số key là chưa đủ; vòng đọc lại này là bắt buộc theo quy tắc của Hieu.

## Kết luận về cơ chế lỗi

File này không có lỗi cấu trúc nào: 0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương — trái ngược hoàn toàn với file em của nó (解放b寝台, 19 dòng tràn chương từ obasan). 41 lỗi đều là lỗi "dịch" thuần túy, tập trung vào ba lựa chọn hệ thống của người dịch: (1) Soutetsu tự xưng "anh" — 9/10 lần tự xưng trong thoại (chỉ 1 lần "tôi"); (2) thuật ngữ 御一夜 — 12 lần xuất hiện đều là "Ohito", 0 lần "Ohitoyo"; (3) thuật ngữ 術仙 — 12 lần "Jussen" (thiếu chữ "t") và 2 lần "Jussendo". Ba nhóm này chiếm 25/41 lỗi. Các lỗi sai nghĩa riêng lẻ đáng chú ý: 1617 đảo ngược chủ thể (Akai giúp Soutetsu nhận ra, không phải ngược lại), 1782 gọi sai người được nhờ ("cô" trong khi người được nhờ là Soutetsu), 2105 gọi thầy Akai là "chị", 2553 nhầm cá mắt vàng thành cá tráp đỏ. Đây là file "sạch về cấu trúc" có tỷ lệ sai cao (10,6%) — gần bằng Paulette 01 御一夜探し (11,9%) — vì lỗi thuật ngữ + xưng hô hệ thống, không phải vì lệch dòng.

## Chi tiết dòng sai

### Thuật ngữ (25 dòng)

**1582 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「ならば、
御一夜の特産としては売りが弱くなりますか」
- TW: 「不過，這也就意味著很難將其作為御一夜特產來推廣啊」
- Cũ: 「Nếu vậy,
thì sức hút của nó với tư cách là đặc sản Ohito sẽ bị giảm sút sao?」
- Sửa: 「Nếu vậy,
thì sức hút của nó với tư cách là đặc sản Ohitoyo sẽ bị giảm sút sao?」

**1683 [Hibiki]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" (thiếu chữ "t").

- JP: 「行くんですか？　兄さん。
術仙炭鉱跡の調査に」
- TW: 「哥哥，你要去調查那個術仙廢煤礦嗎？」
- Cũ: 「Anh định đi sao? Anh trai.
Đi điều tra tàn tích Mỏ than Jussen ấy.」
- Sửa: 「Anh định đi sao? Anh trai.
Đi điều tra tàn tích Mỏ than Jutsu-sen ấy.」

**1688 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「ほう、古地図か――
御一夜の……いや、もっと広域のものか」
- TW: 「哦，這是御一夜的古地圖嗎……不，應該是更大範圍的地圖」
- Cũ: 「Ồ, bản đồ cổ sao——
Của Ohito... Không, khu vực rộng hơn thế.」
- Sửa: 「Ồ, bản đồ cổ sao——
Của Ohitoyo... Không, khu vực rộng hơn thế.」

**1719 [Paulette]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" (thiếu chữ "t").

- JP: 「あ、それは術仙炭鉱の廃駅前からです。
遠足のときだけは、臨時停車することになってて」
- TW: 「啊，是從術仙煤礦廢車站那裡。只有去遠足的時候能臨時在那裡停車」
- Cũ: 「A, là từ trước nhà ga Mỏ than Jussen bị bỏ hoang ạ.
Chỉ những lúc dã ngoại, tàu mới dừng tạm ở đó.」
- Sửa: 「A, là từ trước nhà ga Mỏ than Jutsu-sen bị bỏ hoang ạ.
Chỉ những lúc dã ngoại, tàu mới dừng tạm ở đó.」

**1725 [Soutetsu]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" (thiếu chữ "t").

- JP: 「うむ。術仙炭鉱跡の周辺に、
そうした何かが残ってないか、誰かもしも」
- TW: 「嗯。有人知道術仙廢煤礦周圍的鐵路還有留下來嗎」
- Cũ: 「Ừm. Xung quanh tàn tích Mỏ than Jussen,
có ai biết liệu còn sót lại thứ gì như vậy không.」
- Sửa: 「Ừm. Xung quanh tàn tích Mỏ than Jutsu-sen,
có ai biết liệu còn sót lại thứ gì như vậy không.」

**1751 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「御一夜のこと、文化のこと。
普段から興味を持たぬ者では、ああいう話は出てこない」
- TW: 「如果不是熱愛御一夜和文化的人，是不會說出那種話的」
- Cũ: 「Chuyện về Ohito, chuyện về văn hóa.
Nếu không phải là người luôn quan tâm đến những điều đó thì sẽ không thể nói ra được những lời như vậy.」
- Sửa: 「Chuyện về Ohitoyo, chuyện về văn hóa.
Nếu không phải là người luôn quan tâm đến những điều đó thì sẽ không thể nói ra được những lời như vậy.」

**1753 [Akai]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「もし仮に、日ノ本一売れる駅弁を作れれば、
そうしたフェアの全てが御一夜の宣伝になる」
- TW: 「如果你們能發明日本第一暢銷的鐵路便當，那就相當於所有的鐵路便當博覽會都在免費宣傳御一夜了」
- Cũ: 「Giả sử các cháu có thể làm ra hộp cơm nhà ga bán chạy nhất Hinomoto,
thì tất cả những hội chợ đó sẽ trở thành nơi quảng bá cho Ohito.」
- Sửa: 「Giả sử các cháu có thể làm ra hộp cơm nhà ga bán chạy nhất Hinomoto,
thì tất cả những hội chợ đó sẽ trở thành nơi quảng bá cho Ohitoyo.」

**1826 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「御一夜らしい駅弁を、と考えています。それで、
キジ馬についてご教示いただきたくお邪魔いたしました」
- TW: 「我們想要製作有御一夜特色的鐵路便當。所以特來請教宮司有關雉子馬的事情」
- Cũ: 「Bọn cháu đang muốn làm một hộp cơm nhà ga mang đậm chất Ohito. Vì vậy,
bọn cháu đến đây để thỉnh giáo thầy về ngựa Kiji ạ.」
- Sửa: 「Bọn cháu đang muốn làm một hộp cơm nhà ga mang đậm chất Ohitoyo. Vì vậy,
bọn cháu đến đây để thỉnh giáo thầy về ngựa Kiji ạ.」

**1856 [Soutetsu]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" (thiếu chữ "t").

- JP: 「近くに無くても奥ならどうだ？
術仙炭鉱までにレールは、残ってないのか？」
- TW: 「既然廢車站那裡沒有，那深處呢？現在還有通向術仙煤礦的鐵軌嗎？」
- Cũ: 「Gần đó không có, nhưng ở sâu bên trong thì sao?
Đường ray đến tận Mỏ than Jussen, chẳng lẽ không còn sót lại chút nào sao?」
- Sửa: 「Gần đó không có, nhưng ở sâu bên trong thì sao?
Đường ray đến tận Mỏ than Jutsu-sen, chẳng lẽ không còn sót lại chút nào sao?」

**1858 [Soutetsu]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" (thiếu chữ "t").

- JP: 「宿舎がいっぱい、というほどの規模なら、
術仙炭鉱は産出量に恵まれていたのかな？」
- TW: 「既然有那麼多礦工居住的宿舍，也就是說術仙煤礦曾經產量很高囉？」
- Cũ: 「Nếu quy mô đến mức có nhiều khu nhà ở,
thì sản lượng của Mỏ than Jussen chắc phải cao lắm nhỉ?」
- Sửa: 「Nếu quy mô đến mức có nhiều khu nhà ở,
thì sản lượng của Mỏ than Jutsu-sen chắc phải cao lắm nhỉ?」

**1896 [Paulette]** — ポイント (điểm chuyển ray / ghi) bị dịch thành "công tắc" (công tắc điện) — TW 轉轍器 xác nhận đây là ghi ray, không phải công tắc điện.

- JP: 「はい！　もしも線路が状態よく残ってれば、
そことつなげて、\x%lポイント;#00ffc040;ポイント%l;#;整備するだけですから」
- TW: 「是的！　如果線路的保存狀態良好的話，只要接上那裡再整備好\x%lポイント;#00ffc040;轉轍器%l;#;就可以了」
- Cũ: 「Vâng! Nếu đường ray vẫn còn nguyên vẹn,
thì chỉ cần nối với nó và bảo dưỡng lại \x%lポイント;#00ffc040;công tắc%l;#; là được ạ.」
- Sửa: 「Vâng! Nếu đường ray vẫn còn nguyên vẹn,
thì chỉ cần nối với nó và bảo dưỡng lại \x%lポイント;#00ffc040;ghi%l;#; là được ạ.」

**1900 [Akai]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「ええ、あの方は御一夜と鉄道とを愛しておられた。
その二つを復活させるため、手を尽くしておられた」
- TW: 「是的，他一直愛著御一夜和鐵路。他也為了復興這二者而一直在拚命努力著」
- Cũ: 「Vâng, ông ấy rất yêu Ohito và đường sắt.
Ông ấy đã làm mọi cách để vực dậy hai thứ đó.」
- Sửa: 「Vâng, ông ấy rất yêu Ohitoyo và đường sắt.
Ông ấy đã làm mọi cách để vực dậy hai thứ đó.」

**1924 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「木地師文化と――
その集積地としての御一夜、赤井阿蘇神社」
- TW: 「木旋工文化的集散地——御一夜赤井阿蘇神社」
- Cũ: 「Văn hóa thợ tiện gỗ và——
Ohito, đền Akai Aso với tư cách là nơi tập trung của văn hóa đó.」
- Sửa: 「Văn hóa thợ tiện gỗ và——
Ohitoyo, đền Akai Aso với tư cách là nơi tập trung của văn hóa đó.」

**1935 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「だから、御一夜という土地にも、
多くの古いキジ馬が残されているのですか？」
- TW: 「正因如此，御一夜這片土地才會保留著很多古老的雉子馬嗎？」
- Cũ: 「Vì vậy, ở vùng đất Ohito này,
mới còn lưu giữ nhiều ngựa Kiji cổ đến vậy sao?」
- Sửa: 「Vì vậy, ở vùng đất Ohitoyo này,
mới còn lưu giữ nhiều ngựa Kiji cổ đến vậy sao?」

**2048 [Soutetsu]** — 術仙洞 = "Jutsusendo"; bản cũ "Jussendo" (thiếu chữ "t").

- JP: 「[じゅつせんどう,2]術仙洞駅――
そうか、この頃にはまだ廃駅ではないのだな」
- TW: 「術仙洞站——原來如此，那時候還沒被廢棄啊」
- Cũ: 「Ga Jussendo——
Ra vậy, thời điểm này nó vẫn chưa bị bãi bỏ.」
- Sửa: 「Ga Jutsusendo——
Ra vậy, thời điểm này nó vẫn chưa bị bãi bỏ.」

**2052 [Mayami]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" (thiếu chữ "t").

- JP: 「術仙炭鉱のあたりには、宿舎がいっぱい建っとったんよ。
さぞや栄えとったんろーねぇ」
- TW: 「術仙煤礦那裡曾經建了好多居住區。當年肯定非常繁榮吧」
- Cũ: 「Quanh Mỏ than Jussen, người ta xây nhiều khu nhà ở lắm.
Chắc hẳn ngày xưa sầm uất lắm nhỉ.」
- Sửa: 「Quanh Mỏ than Jutsu-sen, người ta xây nhiều khu nhà ở lắm.
Chắc hẳn ngày xưa sầm uất lắm nhỉ.」

**2100 [Akai]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「いえいえ、御一夜ほどに古いキジ馬が
数多く残っている土地はありません」
- TW: 「這倒不是，因為只有御一夜保留了這麼多的古老雉子馬」
- Cũ: 「Không đâu, không có vùng đất nào
lưu giữ được nhiều ngựa Kiji cổ xưa như Ohito cả.」
- Sửa: 「Không đâu, không có vùng đất nào
lưu giữ được nhiều ngựa Kiji cổ xưa như Ohitoyo cả.」

**2104 [Paulette]** — 大詔 = "Taisho" (niên hiệu Đại Chính); bản cũ "Đại Chiếu" dịch âm Hán-Việt sai — theo tiền lệ Hachiroku 12 再開発 3054.

- JP: 「\x%l大詔;#00ffc040;大詔%l;#;の頃のものでしょうかね？
[ていてつゆのいせん,4]帝鉄湯医線って、ほら、ここ」
- TW: 「這是大正時期的地圖吧？你看這裡，還寫著帝鐵湯醫線呢」
- Cũ: 「Có lẽ là từ thời \x%l大詔;#00ffc040;Đại Chiếu%l;#; nhỉ?
Tuyến Teitetsu Yui này, anh xem, ở đây.」
- Sửa: 「Có lẽ là từ thời \x%l大詔;#00ffc040;Taisho%l;#; nhỉ?
Tuyến Teitetsu Yui này, anh xem, ở đây.」

**2136 [Paulette]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" (thiếu chữ "t").

- JP: 「もう、とっくの昔に廃線されてますよ？
術仙炭鉱廃駅の近くに、そんな設備は」
- TW: 「那裡可是早就已經廢線了呀？術仙煤礦廢車站那裡已經沒有相應設備了」
- Cũ: 「Tuyến đường đó đã bị bãi bỏ từ lâu lắm rồi mà?
Gần nhà ga Mỏ than Jussen bị bỏ hoang, làm gì còn thiết bị nào...」
- Sửa: 「Tuyến đường đó đã bị bãi bỏ từ lâu lắm rồi mà?
Gần nhà ga Mỏ than Jutsu-sen bị bỏ hoang, làm gì còn thiết bị nào...」

**2394 [lời dẫn]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" (thiếu chữ "t").

- JP: 凪の言葉を因数分解すれば、
“術仙炭鉱跡＝（遠い+汚い）×２”ということになる。
- TW: 因式分解一下凪的話，就是“術仙廢煤礦＝（遠＋髒）ｘ２”。
- Cũ: Nếu phân tích nhân tử lời của Nagi,
thì sẽ thành 'Tàn tích Mỏ than Jussen = (Xa + Bẩn) x 2'.
- Sửa: Nếu phân tích nhân tử lời của Nagi,
thì sẽ thành 'Tàn tích Mỏ than Jutsu-sen = (Xa + Bẩn) x 2'.

**2414 [lời dẫn]** — 術仙炭鉱 = "mỏ than Jutsu-sen" và 術仙洞 = "Jutsusendo"; bản cũ "Jussen" + "Jussendo" (thiếu chữ "t").

- JP: 言われてみれば、術仙炭鉱駅から
術仙洞の文字の上、鉱山の地図記号へと、線がある。
- TW: 她這麼一指，我發現從術仙煤礦站到術仙洞幾個字上面的礦山地圖符號之間有一條線連接著。
- Cũ: Nghe cô ấy nói tôi mới để ý, từ ga Mỏ than Jussen
đến ký hiệu bản đồ mỏ phía trên chữ Jussendo, có một đường kẻ.
- Sửa: Nghe cô ấy nói tôi mới để ý, từ ga Mỏ than Jutsu-sen
đến ký hiệu bản đồ mỏ phía trên chữ Jutsusendo, có một đường kẻ.

**2560 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 無理もない。僕等は木地師、キジ馬、御一夜関連。
れいなは鉄道関連と、手分けして探していたのだから。
- TW: 沒辦法，畢竟我們找的是木旋工、雉子馬還有御一夜的相關書籍。而玲奈則是在找鐵路的相關書籍。
- Cũ: Cũng phải thôi. Chúng tôi đang chia nhau ra tìm, tôi và Paulette tìm về thợ tiện gỗ, ngựa Kiji, Ohito.
Còn Reina thì tìm về đường sắt mà.
- Sửa: Cũng phải thôi. Chúng tôi đang chia nhau ra tìm, tôi và Paulette tìm về thợ tiện gỗ, ngựa Kiji, Ohitoyo.
Còn Reina thì tìm về đường sắt mà.

**2670 [lời dẫn]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" (thiếu chữ "t").

- JP: 恐らくは術仙炭鉱跡。
老朽化が、急速に進んでしまっているのだ。
- TW: 術仙廢煤礦的老化正在以極快的速度進行著。
- Cũ: Có lẽ là tàn tích Mỏ than Jussen.
Sự xuống cấp đang diễn ra với tốc độ chóng mặt.
- Sửa: Có lẽ là tàn tích Mỏ than Jutsu-sen.
Sự xuống cấp đang diễn ra với tốc độ chóng mặt.

**2675 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 文化財指定を勝ち得たのなら、
赤井阿蘇神社の、ひいては御一夜市の知名度も高まろう。
- TW: 要是能獲得文化財產認定，赤井阿蘇神社就會連帶著御一夜市一起提高知名度。
- Cũ: Nếu giành được danh hiệu Tài sản văn hóa,
độ nhận diện của đền Akai Aso, và cả thành phố Ohito sẽ tăng lên đáng kể.
- Sửa: Nếu giành được danh hiệu Tài sản văn hóa,
độ nhận diện của đền Akai Aso, và cả thành phố Ohitoyo sẽ tăng lên đáng kể.

**2747 [lời dẫn]** — 術仙炭鉱 = "mỏ than Jutsu-sen"; bản cũ "Jussen" (thiếu chữ "t").

- JP: 線路は、上質の鉄材だ。誰かが、恐らくは持ち去っている。
が、術仙炭鉱付近は\x%lエアクラ;#00ffc040;エアクラ%l;#;の作動不能地帯――
- TW: 鐵軌都是用的上等鋼鐵鋪設，一般來說廢線後都會被人拿走。不過術仙煤礦附近是無法使用\x%lエアクラ;#00ffc040;空凝機%l;#;的——
- Cũ: Đường ray là loại thép chất lượng cao. Có lẽ ai đó đã lấy trộm rồi.
Nhưng khu vực Mỏ than Jussen là vùng cấm hoạt động của \x%lエアクラ;#00ffc040;Aircra%l;#;——
- Sửa: Đường ray là loại thép chất lượng cao. Có lẽ ai đó đã lấy trộm rồi.
Nhưng khu vực Mỏ than Jutsu-sen là vùng cấm hoạt động của \x%lエアクラ;#00ffc040;Aircra%l;#;——

### Xưng hô (9 dòng)

**1572 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với thầy Akai; theo docs (locations §2.1) Soutetsu tự xưng "Tôi" ("Anh" chỉ khi nói với Hibiki).

- JP: 「いや、心配ない。
僕は、むしろ充実している」
- TW: 「不必擔心我。不如說這段時間我過得很充實」
- Cũ: 「Không, đừng lo.
Anh ngược lại còn thấy rất sung mãn.」
- Sửa: 「Không, đừng lo.
Tôi ngược lại còn thấy rất sung mãn.」

**1574 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với thầy Akai; theo docs Soutetsu tự xưng "Tôi".

- JP: 「いや？　それは知っているが――」
- TW: 「不是哦？　我當然知道這點——」
- Cũ: 「Không? Chuyện đó thì anh biết, nhưng——」
- Sửa: 「Không? Chuyện đó thì tôi biết, nhưng——」

**1581 [Soutetsu]** — Soutetsu tự xưng "anh" trước cả nhóm (không phải Hibiki); theo docs Soutetsu tự xưng "Tôi".

- JP: 「しかし、文化財指定というアイディアには驚いた」
- TW: 「不過，我真沒想到還有認定文化財產這一招」
- Cũ: 「Nhưng mà, ý tưởng công nhận Di sản Văn hóa làm anh ngạc nhiên đấy.」
- Sửa: 「Nhưng mà, ý tưởng công nhận Di sản Văn hóa làm tôi ngạc nhiên đấy.」

**1598 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với "mọi người" (cả nhóm); theo docs Soutetsu tự xưng "Tôi". Quét máy bắt thêm dòng này — đọc tay đã bỏ sót.

- JP: 「今日は、その辺のことを相談したく、
みなに集まってもらったのだ」
- TW: 「今天就是為了討論這些而把大家叫來的」
- Cũ: 「Hôm nay, anh tập hợp mọi người lại,
chính là để bàn bạc về những chuyện đó.」
- Sửa: 「Hôm nay, tôi tập hợp mọi người lại,
chính là để bàn bạc về những chuyện đó.」

**1640 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với thầy Akai; theo docs "Tôi". Giữ nguyên "mình" lồng trong mệnh đề ("nghĩ mình đã hiểu") theo tiền lệ Hachiroku 12.

- JP: 「なるほど、少し理解できたように思う」
- TW: 「原來如此，我似乎有點理解你的想法了」
- Cũ: 「Ra là vậy, anh nghĩ mình đã hiểu được một chút rồi.」
- Sửa: 「Ra là vậy, tôi nghĩ mình đã hiểu được một chút rồi.」

**1763 [Soutetsu]** — Soutetsu tự xưng "anh" trước cả nhóm; theo docs Soutetsu tự xưng "Tôi".

- JP: 「状態よく残っていれば――
どうかな、面白いのではないかと考えている」
- TW: 「如果狀態良好的話——你覺得呢？　我認為是個不錯的主意」
- Cũ: 「Nếu vẫn còn nguyên vẹn——
Thế nào, anh nghĩ ý tưởng này khá thú vị đấy chứ.」
- Sửa: 「Nếu vẫn còn nguyên vẹn——
Thế nào, tôi nghĩ ý tưởng này khá thú vị đấy chứ.」

**1840 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Paulette; theo docs "Tôi" ("Anh" chỉ với Hibiki). "Em" (gọi Paulette) giữ nguyên.

- JP: 「僕は君に、聞きたいことがひとつ」
- TW: 「我有件事想問你」
- Cũ: 「Anh có một chuyện muốn hỏi em.」
- Sửa: 「Tôi có một chuyện muốn hỏi em.」

**1842 [Soutetsu]** — Soutetsu tự xưng "anh" 2 lần khi nói với Paulette; theo docs "Tôi".

- JP: 「僕などは、簡単に意見を変えてしまうからな。
ポーレットのいうしつこさが、少し眩しい」
- TW: 「我總是輕易地改變自己的意見。所以稍微有些羨慕波萊特你的固執」
- Cũ: 「Người như anh thì rất dễ dàng thay đổi ý kiến.
Sự cố chấp mà Paulette nói, đối với anh có chút chói lóa đấy.」
- Sửa: 「Người như tôi thì rất dễ dàng thay đổi ý kiến.
Sự cố chấp mà Paulette nói, đối với tôi có chút chói lóa đấy.」

**2037 [Soutetsu]** — Soutetsu tự xưng "anh" trước cả nhóm (Paulette, Akai); theo docs "Tôi".

- JP: 「僕は、面白そうだと感じているが……」
- TW: 「至少我是覺得很有意思……」
- Cũ: 「Anh thì thấy có vẻ thú vị đấy...」
- Sửa: 「Tôi thì thấy có vẻ thú vị đấy...」

### Sai nghĩa (4 dòng)

**1617 [Soutetsu]** — Nhầm chủ thể: JP/TW nói Soutetsu "nhờ [Akai] mà nhận ra" — Akai là người giúp Soutetsu nhận ra; bản cũ "Nhờ cháu mà tôi..." đảo ngược chủ thể (Soutetsu tự xưng "cháu" với thầy Akai là đúng, nhưng "cháu" không thể là người giúp Soutetsu nhận ra).

- JP: 「『良いことに気づかせてもらった』――
と解釈しておけば良いと思う」
- TW: 「你就理解為“讓我學到了新東西”就好」
- Cũ: 「『Nhờ cháu mà tôi đã nhận ra được một điều tuyệt vời』——
Cứ hiểu như vậy là được.」
- Sửa: 「『Nhờ thầy mà tôi đã nhận ra được một điều tuyệt vời』——
Cứ hiểu như vậy là được.」

**1782 [Akai]** — Sai người được gọi: Akai nói "Trăm sự nhờ cô" — nhưng trong đoạn trao đổi trực tiếp (Reina 1778 → Hibiki 1780 → Akai 1782 → Soutetsu 1784) người được nhờ là Soutetsu (trưởng nhóm điều tra, đối tác trao đổi thường xuyên của Akai trong file); "cô" không ứng với Hibiki ("cháu") hay Soutetsu ("cậu"). Sửa theo hướng Soutetsu.

- JP: 「よろしくお願いいたします。
っと――そうだ」
- TW: 「就拜託你了。對了——還有」
- Cũ: 「Trăm sự nhờ cô.
À——phải rồi.」
- Sửa: 「Trăm sự nhờ cậu.
À——phải rồi.」

**2105 [Soutetsu]** — Sai người được gọi: Soutetsu cảm ơn thầy Akai (người kể chuyện Kiji); bản cũ "cảm ơn chị" — Akai là nam, cao tuổi, chức thầy tế.

- JP: 「そうか、ありがとう。
聞かせてもらった話、とても参考になった」
- TW: 「這樣啊，謝謝各位。這些情報很有用」
- Cũ: 「Vậy ạ, cảm ơn chị.
Những chuyện chị kể, rất có giá trị tham khảo.」
- Sửa: 「Vậy ạ, cảm ơn thầy.
Những chuyện thầy kể, rất có giá trị tham khảo.」

**2553 [lời dẫn]** — キンメダイ = cá mắt vàng (splendid alfonsino, 金目鯛); bản cũ "cá tráp đỏ" là cá tráp đỏ (真鯛) — loài khác. TW 金眼鯛 xác nhận.

- JP: [ヨコカワ,1]横河のカマ飯、[ニシアカシ,2]西赤司のタコ飯、[オシャマンベ,3]御社万部のカニ飯、
[ヒタチダイゴ,3]常陸醍醐のシャモ飯、[イズデンシモダ,4]伊津電霜田のキンメダイ飯――
- TW: 橫川的釜飯、西明石的章魚飯、長萬部的螃蟹飯、常陸大子的軍雞飯、伊豆下田的金眼鯛飯——
- Cũ: Cơm thố Yokokawa, cơm bạch tuộc Nishi Akashi, cơm cua Oshamambe,
cơm gà chọi Hitachi Daigo, cơm cá tráp đỏ Izuden Shimoda——
- Sửa: Cơm thố Yokokawa, cơm bạch tuộc Nishi Akashi, cơm cua Oshamambe,
cơm gà chọi Hitachi Daigo, cơm cá mắt vàng Izuden Shimoda——

### Lỗi nhỏ (3 dòng)

**1638 [Soutetsu]** — Mất tiếng hít っ: JP 「――っ！？」 chỉ còn "——!?" — khôi phục "Ư!?".

- JP: 「なるほど。――っ！？」
- TW: 「原來如此。——啊！」
- Cũ: 「Ra là vậy. ——!?」
- Sửa: 「Ra là vậy. ——Ư!?」

**2172 [Soutetsu]** — Mất tiếng hít っ: JP 「っ！」 chỉ còn "「!」" — khôi phục "Ư!".

- JP: 「っ！」
- TW: 「！」
- Cũ: 「!」
- Sửa: 「Ư!」

**2173 [Fukami]** — Mất tiếng hít っ: JP 「っ！！！」 chỉ còn "「!!!」" — khôi phục "Ư!!!".

- JP: 「っ！！！」
- TW: 「！！！」
- Cũ: 「!!!」
- Sửa: 「Ư!!!」

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
1572 = "「Không, đừng lo.\nTôi ngược lại còn thấy rất sung mãn.」"
1574 = "「Không? Chuyện đó thì tôi biết, nhưng——」"
1581 = "「Nhưng mà, ý tưởng công nhận Di sản Văn hóa làm tôi ngạc nhiên đấy.」"
1582 = "「Nếu vậy,\nthì sức hút của nó với tư cách là đặc sản Ohitoyo sẽ bị giảm sút sao?」"
1598 = "「Hôm nay, tôi tập hợp mọi người lại,\nchính là để bàn bạc về những chuyện đó.」"
1617 = "「『Nhờ thầy mà tôi đã nhận ra được một điều tuyệt vời』——\nCứ hiểu như vậy là được.」"
1638 = "「Ra là vậy. ——Ư!?」"
1640 = "「Ra là vậy, tôi nghĩ mình đã hiểu được một chút rồi.」"
1683 = "「Anh định đi sao? Anh trai.\nĐi điều tra tàn tích Mỏ than Jutsu-sen ấy.」"
1688 = "「Ồ, bản đồ cổ sao——\nCủa Ohitoyo... Không, khu vực rộng hơn thế.」"
1719 = "「A, là từ trước nhà ga Mỏ than Jutsu-sen bị bỏ hoang ạ.\nChỉ những lúc dã ngoại, tàu mới dừng tạm ở đó.」"
1725 = "「Ừm. Xung quanh tàn tích Mỏ than Jutsu-sen,\ncó ai biết liệu còn sót lại thứ gì như vậy không.」"
1751 = "「Chuyện về Ohitoyo, chuyện về văn hóa.\nNếu không phải là người luôn quan tâm đến những điều đó thì sẽ không thể nói ra được những lời như vậy.」"
1753 = "「Giả sử các cháu có thể làm ra hộp cơm nhà ga bán chạy nhất Hinomoto,\nthì tất cả những hội chợ đó sẽ trở thành nơi quảng bá cho Ohitoyo.」"
1763 = "「Nếu vẫn còn nguyên vẹn——\nThế nào, tôi nghĩ ý tưởng này khá thú vị đấy chứ.」"
1782 = "「Trăm sự nhờ cậu.\nÀ——phải rồi.」"
1826 = "「Bọn cháu đang muốn làm một hộp cơm nhà ga mang đậm chất Ohitoyo. Vì vậy,\nbọn cháu đến đây để thỉnh giáo thầy về ngựa Kiji ạ.」"
1840 = "「Tôi có một chuyện muốn hỏi em.」"
1842 = "「Người như tôi thì rất dễ dàng thay đổi ý kiến.\nSự cố chấp mà Paulette nói, đối với tôi có chút chói lóa đấy.」"
1856 = "「Gần đó không có, nhưng ở sâu bên trong thì sao?\nĐường ray đến tận Mỏ than Jutsu-sen, chẳng lẽ không còn sót lại chút nào sao?」"
1858 = "「Nếu quy mô đến mức có nhiều khu nhà ở,\nthì sản lượng của Mỏ than Jutsu-sen chắc phải cao lắm nhỉ?」"
1896 = "「Vâng! Nếu đường ray vẫn còn nguyên vẹn,\nthì chỉ cần nối với nó và bảo dưỡng lại \\x%lポイント;#00ffc040;ghi%l;#; là được ạ.」"
1900 = "「Vâng, ông ấy rất yêu Ohitoyo và đường sắt.\nÔng ấy đã làm mọi cách để vực dậy hai thứ đó.」"
1924 = "「Văn hóa thợ tiện gỗ và——\nOhitoyo, đền Akai Aso với tư cách là nơi tập trung của văn hóa đó.」"
1935 = "「Vì vậy, ở vùng đất Ohitoyo này,\nmới còn lưu giữ nhiều ngựa Kiji cổ đến vậy sao?」"
2037 = "「Tôi thì thấy có vẻ thú vị đấy...」"
2048 = "「Ga Jutsusendo——\nRa vậy, thời điểm này nó vẫn chưa bị bãi bỏ.」"
2052 = "「Quanh Mỏ than Jutsu-sen, người ta xây nhiều khu nhà ở lắm.\nChắc hẳn ngày xưa sầm uất lắm nhỉ.」"
2100 = "「Không đâu, không có vùng đất nào\nlưu giữ được nhiều ngựa Kiji cổ xưa như Ohitoyo cả.」"
2104 = "「Có lẽ là từ thời \\x%l大詔;#00ffc040;Taisho%l;#; nhỉ?\nTuyến Teitetsu Yui này, anh xem, ở đây.」"
2105 = "「Vậy ạ, cảm ơn thầy.\nNhững chuyện thầy kể, rất có giá trị tham khảo.」"
2136 = "「Tuyến đường đó đã bị bãi bỏ từ lâu lắm rồi mà?\nGần nhà ga Mỏ than Jutsu-sen bị bỏ hoang, làm gì còn thiết bị nào...」"
2172 = "「Ư!」"
2173 = "「Ư!!!」"
2394 = "Nếu phân tích nhân tử lời của Nagi,\nthì sẽ thành 'Tàn tích Mỏ than Jutsu-sen = (Xa + Bẩn) x 2'."
2414 = "Nghe cô ấy nói tôi mới để ý, từ ga Mỏ than Jutsu-sen\nđến ký hiệu bản đồ mỏ phía trên chữ Jutsusendo, có một đường kẻ."
2553 = "Cơm thố Yokokawa, cơm bạch tuộc Nishi Akashi, cơm cua Oshamambe,\ncơm gà chọi Hitachi Daigo, cơm cá mắt vàng Izuden Shimoda——"
2560 = "Cũng phải thôi. Chúng tôi đang chia nhau ra tìm, tôi và Paulette tìm về thợ tiện gỗ, ngựa Kiji, Ohitoyo.\nCòn Reina thì tìm về đường sắt mà."
2670 = "Có lẽ là tàn tích Mỏ than Jutsu-sen.\nSự xuống cấp đang diễn ra với tốc độ chóng mặt."
2675 = "Nếu giành được danh hiệu Tài sản văn hóa,\nđộ nhận diện của đền Akai Aso, và cả thành phố Ohitoyo sẽ tăng lên đáng kể."
2747 = "Đường ray là loại thép chất lượng cao. Có lẽ ai đó đã lấy trộm rồi.\nNhưng khu vực Mỏ than Jutsu-sen là vùng cấm hoạt động của \\x%lエアクラ;#00ffc040;Aircra%l;#;——"
```

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- **Soutetsu gọi Paulette "cô" vs "em": "em" 4×, "cô" 0×** — "em" tại 1706 ("Nghe em nói mới nhớ"), 1732 ("Trăm sự nhờ em"), 1840 ("Anh có một chuyện muốn hỏi em"), 1961 ("Paulette, em thấy sao?"). 1871 gọi Hibiki là "em" (không tính vào Paulette). 2056 "Em đã từng thấy trên phim ảnh chưa?" — người được gọi không rõ (nhóm đang thảo luận chung) nên không tính. Tally lũy kế toàn dự án: "cô" 43 vs "em" 34 (cộng 4 "em" của file này).
- **湯医: "Yui" 1×, "Yunoi" 0×** — tại 2104 ("Tuyến Teitetsu Yui"). Ghi nhận, không áp dụng (quyết định đang chờ; bằng chứng mới nhất P10/P11 nghiêng về "Yunoi").
- **帝鉄: dạng trần "Teitetsu" 1×** — tại 2104 ("Tuyến Teitetsu Yui"); dạng docs "Đường sắt Hoàng gia" 0×, "Đế Thiết" 0× trong file này. Ghi nhận, không áp dụng.
- **宮司: "thầy"/"thầy tế"/"thầy tế Akai"** — JP có 宮司 tại các dòng của Akai; bản Việt dùng "thầy" và "thầy tế" (đề xuất thống nhất "đền chủ" đang chờ, không áp dụng).
- **"KiHa" 4×, "Kiha" 0×** — các gloss `%l` trong file này đều dùng "KiHa" (chính tả JR chuẩn). Ghi nhận cho quyết định "KiHa" vs "Kiha" đang chờ.
- **コン: 0 lần; 冥国/冥軍: 0 lần; 小畑/大畑: 0 lần** trong file này.
- **駿袋鉄道: 0 lần** trong file này.

## Đề xuất cập nhật context (chưa chốt)

- Không có đề xuất mới. Hai thuật ngữ trong file này theo tiền lệ đã có: ポイント → "ghi" (theo TW 轉轍器 — ghi ray, không phải công tắc điện) và 大詔 → "Taisho" (theo tiền lệ Hachiroku 12 再開発 3054).

## Đã kiểm tra và KHÔNG tính là sai

- **1816 "(gỗ)"** — Paulette nói "ngựa Kiji (gỗ)": gloss "(gỗ)" thừa nhưng vô hại và giúp người đọc hiểu Kiji = gỗ (木地); không tính sai.
- **1710 オウム** — VN "vẹt" theo đúng JP; TW đọc nhầm オウム thành 千 (một nghìn). Xác nhận JP-over-TW, không phải lỗi.
- **1829 福丘** — VN "Fukuoka" theo đúng furigana ふくおか trên 福丘; TW 福岡 đồng ý. Không phải lỗi.
- **1989 "mình"** — "những điều mình quan tâm" là đại từ chung chỉ Paulette (người được nói tới), không phải Soutetsu tự xưng. Không phải lỗi.
- **2734 "mình đã nghe nhầm"** — "mình" làm chủ ngữ mệnh đề lồng, chủ ngữ chính vẫn là "tôi" ("khiến tôi... nghĩ mình đã nghe nhầm"); theo tiền lệ Hachiroku 12, giữ nguyên.
- **"cháu" của Soutetsu (1635, 1826, 1832, 2030, 2102)** — Soutetsu tự xưng "cháu" với thầy Akai (bậc cao tuổi), đúng quy ước xưng hô theo tuổi tác/bậc. Chỉ 1617 sai vì "cháu" bị dùng làm chủ thể gây ra việc nhận ra.
- **"Vâng." trùng 1895/1728** — JP cả hai đều là 「はい」, đều đúng.
- **っ cuối từ tại 1677, 1704, 1713** — っ gắn vào từ (むごごごごっ, いえっ, ばいっ), không phải tiếng hít độc lập; bản Việt đã diễn đạt được độ nhấn, không tính sai. Chỉ 3 tiếng hít độc lập (1638, 2172, 2173) bị mất mới tính sai.
- **2104 "Tuyến Teitetsu Yui"** — dạng "Teitetsu" và "Yui" thuộc hai quyết định đang chờ (帝鉄, 湯医); ghi nhận, không tính sai.
- **宮司 dịch "thầy"/"thầy tế"** — thuộc đề xuất thống nhất "đền chủ" đang chờ; không tính sai.
- **Ký tự lạ trong JP của CSV3 (2105, 2394)** — cột JP của CSV "Trang tính 3" hiển thị ký tự thay thế tại 2105 ("とても参考になった") và 2394 ("ということになる"); đã đối chiếu ghi chú `# JP:` trong TOML-2 — cả hai đều sạch, không có ký tự lạ. Đây là lỗi hiển thị/mã hóa của CSV, không chạm tới bản Việt, không tính sai.

## Kết bài

古地図 là file sạch về cấu trúc (0 lệch vị trí) nhưng sai 41/385 dòng (10,6%) — gần như toàn bộ là lỗi hệ thống: thuật ngữ "Ohito"/"Jussen" chưa thống nhất (25 dòng) và Soutetsu tự xưng "anh" (9 dòng). Áp khối TOML trên sẽ sửa hết 41 dòng; không còn dòng nào chưa chắc chắn trong file này. Mọi bản sửa đều đã qua vòng đọc lại lần hai đối chiếu JP (41/41 đúng, 0 bị loại). Điểm cần lưu ý duy nhất là dòng 1782: người được Akai nhờ là Soutetsu ("cậu") theo mạch trao đổi trực tiếp và vai trò trưởng nhóm điều tra của Soutetsu — nếu Hieu đọc cảnh này thấy người được nhờ là Hibiki thì sửa thành "Trăm sự nhờ cháu." thay cho "Trăm sự nhờ cậu.". **Đính chính B2 19/11 22:24: Hieu ủy quyền Muse chốt — khóa "cậu" (bản sửa giữ nguyên).** Bước tiếp theo: audit các file Paulette còn lại theo thứ tự mức độ nghiêm trọng (heuristic), và khi Hieu chốt các quyết định đang chờ (湯医, 帝鉄, 宮司, "KiHa", "cô" vs "em") thì quét thống nhất toàn dự án — riêng file này sẽ đổi 1 dòng "Yui" (2104) nếu chốt "Yunoi".
