# Audit: Paulette 01_御一夜探し — 44 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/ポーレット01_御一夜探し.txt.toml` — Soutetsu cùng Paulette, Hachiroku, Nagi và bà Nagayama đi khảo sát các điểm tham quan của Ohitoyo để chấn hưng du lịch: di tích thành, bến chèo sông Kuma, xưởng rượu Migita, nhà máy rượu; có cảnh bánh crepe "ngựa Kiji" và cảnh đi bộ cùng Paulette. 369 dòng script đã đọc hết, đối chiếu từng dòng với JP gốc và TW (nhân chứng thứ hai).

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa toàn bộ 369 dòng (thoại 217: Soutetsu 103, Paulette 68, Nagayama 17, Mayami 7, Nagi 6, Fukami 5, Hachiroku 4, Kon 3, Hibiki 3, học sinh A 1; lời dẫn 152) đối chiếu JP + TW từ CSV "Trang tính 3" và TOML-2.
- **44 dòng sai (11,9%), 0 dòng chưa chắc chắn.** Thoại sai 37/217 (17,1%), lời dẫn sai 7/152 (4,6%). Theo người nói: Soutetsu 22, Paulette 10, lời dẫn 7, Nagi 2, Hachiroku 1, Mayami 1, Hibiki 1.
- Phân loại (47 lượt lỗi trên 44 dòng — 1914, 1927 mang cả hai lỗi thuật ngữ + xưng hô; 1683 mang cả hai lỗi thuật ngữ + sai nghĩa): thuật ngữ 24, xưng hô 15, sai nghĩa 5, lỗi nhỏ 3; lệch vị trí 1 cặp, chưa dịch 0, cắt cụt 1 (1151 — câu bị cắt nằm trong cặp lệch vị trí), chưa chắc chắn 0.
- Heuristic (dấu phẩy kiểu MT + "mình" độc lập) báo 0 dòng — bắt được 0/44.
- Không key-shift sạch (shift 0: 369/369). TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất; các khác biệt thô chỉ ở `\n`/khoảng trắng).
- 0 dòng CSV trống; VN==TW 0. `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 84 thẻ, VN có 84 thẻ — **0 thẻ thiếu dấu `;` đóng** (khác Paulette 13: 5 thẻ thiếu `;`).
- **Lệch vị trí 1 cặp, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** cặp 1151↔2196 — câu 2 của 1151 ("Không có Reina xen giữa, không dẫn Hachiroku theo.") nằm thừa ở đầu 2196; cả hai đều là lời dẫn nên heuristic không phát hiện được. Đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục); 43/44 dòng sai chỉ xuất hiện 1 lần. Ngoại lệ: 1947 "「!」" xuất hiện 206 lần (mẫu lỗi hệ thống mất tiếng hít っ). Cặp trùng trong file "「A.」" 1568/1561 đều đúng (JP đều là 「あ」).
- Không có file trùng lặp ở thư mục khác (đã kiểm tra md5 toàn bộ 227 file TOML-2; Grand 04 vẫn là file trùng duy nhất trong dự án).
- Quét xưng hô bằng máy (đã chuẩn hoá `\n` thành khoảng trắng trước khi chạy regex `\b`): Soutetsu trong thoại tự xưng "tôi/Tôi" 0 lần — **cả 15 lần tự xưng trong thoại đều là "anh"** (tất cả sai); "cháu" 4 dòng (1755, 1882, 1697, 1447 — với bà Nagayama, đúng). "mình" trong độc thoại 10 dòng — tất cả đều đúng (thành ngữ "một mình"/"giật mình", sở hữu, mẫu "Tôi… mình…").

## Kết luận về cơ chế lỗi

File này có đúng 1 lỗi cấu trúc: cặp lệch vị trí 1151↔2196 (câu 2 của 1151 bị dán thừa vào đầu 2196, khiến 1151 thành dòng cắt cụt) — cùng loại lời dẫn nên không bị heuristic phát hiện. Ngoài ra không có chuỗi xoay vòng, không có tràn chương, không có dòng mồ côi. Phần lớn lỗi còn lại là hai lựa chọn hệ thống của người dịch: (1) Soutetsu tự xưng "anh" — 15/15 lần tự xưng trong thoại, 0 lần "tôi" (file duy nhất từ trước đến nay có tỉ lệ "anh" 100%); (2) thuật ngữ 御一夜 — 25 lần xuất hiện đều là "Ohito", 0 lần "Ohitoyo". Các lỗi sai nghĩa riêng lẻ đáng chú ý: 1888 bỏ hẳn tên キジウマ (mất cả câu đùa), 1756 dịch 廃客車 thành "phế liệu". Đây là file có tỷ lệ sai cao nhất trong các file "sạch về cấu trúc" đã audit (11,9%), chỉ thấp hơn các file lệch vị trí nặng (廃炭鉱 30,9%, obasan 56%, Grand 01 45,6%, Hibiki 03 86,2%, 夜の嵐 44,9%, stove 22,1%).

## Chi tiết dòng sai

### Thuật ngữ (23 dòng)

**1524 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「何か世界一――は無理としても、日ノ本一はないかな。
クマ川なり、御一夜なりに」
- TW: 「即使做不到世界第一，但能不能以隈河、御一夜自己的方式做到日本第一呢」
- Cũ: 「Nhất thế giới thì có vẻ hơi quá sức, nhưng nhất Hinomoto thì sao.
Dù là sông Kuma hay Ohito.」
- Sửa: 「Nhất thế giới thì có vẻ hơi quá sức, nhưng nhất Hinomoto thì sao. Dù là sông Kuma hay Ohitoyo.」

**1527 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「なるほど、御一夜に観光に来るものは、
御一夜の外の人間なのだな」
- TW: 「原來如此，來御一夜旅遊的都不是御一夜本地人啊」
- Cũ: 「Quả thực, những người đến Ohito du lịch,
đều là người từ nơi khác đến.」
- Sửa: 「Quả thực, những người đến Ohitoyo du lịch, đều là người từ nơi khác đến.」

**1588 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「あ、そうですよね。だったら――
ここにいる中で、御一夜のことをまだ知らないのは」
- TW: 「啊，對呢。那麼——我們這些人當中，對御一夜還不太了解的是——」
- Cũ: 「A, đúng vậy nhỉ. Nếu thế thì——
Trong số những người ở đây, người vẫn chưa biết nhiều về Ohito là...」
- Sửa: 「A, đúng vậy nhỉ. Nếu thế thì—— Trong số những người ở đây, người vẫn chưa biết nhiều về Ohitoyo là...」

**1686 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「御一夜らしさ……」
- TW: 「御一夜特色……」
- Cũ: 「Đậm chất Ohito...」
- Sửa: 「Đậm chất Ohitoyo...」

**1691 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「も、あると思います。御一夜は、隈元市内みたいに
直接の大空襲は受けてないですけど、それでも」
- TW: 「應該也有這個原因。雖然御一夜並沒有像隈元市市區那樣直接受到大規模空襲，但仍然還是——」
- Cũ: 「Em nghĩ cũng có phần. Ohito tuy không bị không kích trực tiếp
như trung tâm thành phố Kumamoto, nhưng mà...」
- Sửa: 「Em nghĩ cũng có phần. Ohitoyo tuy không bị không kích trực tiếp như trung tâm thành phố Kumamoto, nhưng mà...」

**1693 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「実地の方は全然です、わたしも。
御一夜に来てから、政治と鉄道のことばっかりで」
- TW: 「我也幾乎沒去過實地調查。自從來到御一夜，就一直在忙政治與鐵路的事情」
- Cũ: 「Em cũng chưa đi thực tế bao giờ.
Từ lúc đến Ohito, em chỉ lo chuyện chính trị và đường sắt thôi.」
- Sửa: 「Em cũng chưa đi thực tế bao giờ. Từ lúc đến Ohitoyo, em chỉ lo chuyện chính trị và đường sắt thôi.」

**1696 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「マイナーな温泉地から一歩を踏み出す、御一夜の魅力。
それをどう周知していくか、僕らは考えねばならん」
- TW: 「我們必須思考怎樣才能使人們認識到御一夜的魅力，讓它擺脫大眾心中的“二流溫泉景區”標籤」
- Cũ: 「Sức hấp dẫn của Ohito, để thoát khỏi cái mác 'khu suối nước nóng hẻo lánh'.
Chúng ta phải suy nghĩ cách quảng bá nó.」
- Sửa: 「Sức hấp dẫn của Ohitoyo, để thoát khỏi cái mác 'khu suối nước nóng hẻo lánh'. Chúng ta phải suy nghĩ cách quảng bá nó.」

**1716 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「日々姫は御一夜に詳しかろう。
地元で、しかも看板描きで密接にかかわっている」
- TW: 「日日姬應該很熟悉御一夜吧。你是當地人，而且為了繪製招牌，經常接觸這些」
- Cũ: 「Hibiki chắc hẳn rất rành về Ohito.
Là người địa phương, lại còn vẽ biển hiệu nên có mối liên hệ rất mật thiết.」
- Sửa: 「Hibiki chắc hẳn rất rành về Ohitoyo. Là người địa phương, lại còn vẽ biển hiệu nên có mối liên hệ rất mật thiết.」

**1776 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「かもしれませんね、御一夜で一番古い場所ですし」
- TW: 「有可能呢，畢竟那裡是御一夜最古老的地方」
- Cũ: 「Có thể lắm ạ, đó là nơi lâu đời nhất ở Ohito mà.」
- Sửa: 「Có thể lắm ạ, đó là nơi lâu đời nhất ở Ohitoyo mà.」

**1786 [Hachiroku]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「まして御一夜のことを、
わたくしは詳しく知りません」
- TW: 「況且我對御一夜並不熟悉」
- Cũ: 「Hơn nữa, về Ohito,
tôi cũng không biết rõ lắm.」
- Sửa: 「Hơn nữa, về Ohitoyo, tôi cũng không biết rõ lắm.」

**1789 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「ポーレットはどうだ？　御一夜の観光については」
- TW: 「波萊特對御一夜的觀光旅遊有多了解？」
- Cũ: 「Paulette thì sao? Về việc tham quan Ohito ấy.」
- Sửa: 「Paulette thì sao? Về việc tham quan Ohitoyo ấy.」

**1820 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「現状、宿泊地に選ばれるほどの強みを持たん御一夜は、
短時間の観光で通過されてしまう……というわけか」
- TW: 「目前御一夜不具備讓遊客選擇留宿的特色，很容易被看做景區之間的中轉站而草草經過嗎」
- Cũ: 「Hiện tại, Ohito không có đủ sức hấp dẫn để được chọn làm nơi lưu trú,
nên chỉ là một điểm dừng chân chớp nhoáng rồi bị bỏ qua... ra là vậy.」
- Sửa: 「Hiện tại, Ohitoyo không có đủ sức hấp dẫn để được chọn làm nơi lưu trú, nên chỉ là một điểm dừng chân chớp nhoáng rồi bị bỏ qua... ra là vậy.」

**1846 [Mayami]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「あんね、双ちゃん。ウチも古い御一夜の人間やけん、
[よそ,1]他所の人らに、何が魅力的に見ゆるやはわからんね」
- TW: 「聽我說呀，小雙。我雖然也是御一夜土生土長的，可卻不知道在外地的人眼中，哪裡才是有魅力的地方咧」
- Cũ: 「Chị nói nghe nè, Sou-chan. Chị cũng là người Ohito gốc,
nên không biết trong mắt người xứ khác, Ohito có điểm gì hấp dẫn đâu nha.」
- Sửa: 「Chị nói nghe nè, Sou-chan. Chị cũng là người Ohitoyo gốc, nên không biết trong mắt người xứ khác, Ohitoyo có điểm gì hấp dẫn đâu nha.」

**1859 [Nagi]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「御一夜の観光ば、クマ川下りで決まりばい！
クマ川下りを前面に押し出して宣伝するばい！！」
- TW: 「要說御一夜的旅遊特色，當然是隈河漂流咧！咱們要重點宣傳隈河漂流咧！！」
- Cũ: 「Nói đến du lịch Ohito, chắc chắn phải là chèo thuyền trên sông Kuma rồi!
Chúng ta phải đẩy mạnh quảng bá chèo thuyền trên sông Kuma!!」
- Sửa: 「Nói đến du lịch Ohitoyo, chắc chắn phải là chèo thuyền trên sông Kuma rồi! Chúng ta phải đẩy mạnh quảng bá chèo thuyền trên sông Kuma!!」

**1889 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「ここが、御一夜で一番古い現存建造物とされてます。
確か……築百三十年とか百四十年とか」
- TW: 「這就是御一夜現存最古老的建築物。我記得……已經有１３０年還是１４０年的歷史了」
- Cũ: 「Đây được cho là công trình kiến trúc hiện tồn lâu đời nhất ở Ohito.
Chắc là... được xây dựng cách đây 130 hay 140 năm gì đó.」
- Sửa: 「Đây được cho là công trình kiến trúc hiện tồn lâu đời nhất ở Ohitoyo. Chắc là... được xây dựng cách đây 130 hay 140 năm gì đó.」

**1914 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito". Đồng thời Soutetsu tự xưng "anh" — trái docs (locations §2.1: "Tôi").

- JP: 「僕が最も適任となるか？　
昔も今も、ほぼ御一夜の観光をした記憶がない」
- TW: 「那麼我就是那個最佳人選吧？無論過去還是現在，我都沒有在御一夜觀光過的經歷」
- Cũ: 「Anh là người phù hợp nhất sao?
Từ trước đến nay, anh hầu như không có ký ức gì về việc đi tham quan Ohito cả.」
- Sửa: 「Tôi là người phù hợp nhất sao? Từ trước đến nay, tôi hầu như không có ký ức gì về việc đi tham quan Ohitoyo cả.」

**1927 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito". Đồng thời Soutetsu tự xưng "anh" — trái docs (locations §2.1: "Tôi").

- JP: 「ならどうだ。僕と一緒に見てみんか？　御一夜の観光を、
どのように盛りたてていけばいいかを、新しい視点で」
- TW: 「那麼，要不要和我一起去看看？　以一個全新的角度，去思考怎麼樣才能振興御一夜的旅遊業」
- Cũ: 「Vậy thì sao nào. Em có muốn cùng anh đi xem thử không?
Xem làm thế nào để thúc đẩy du lịch Ohito, dưới một góc nhìn mới.」
- Sửa: 「Vậy thì sao nào. Em có muốn cùng tôi đi xem thử không? Xem làm thế nào để thúc đẩy du lịch Ohitoyo, dưới một góc nhìn mới.」

**1936 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「御一夜[じょうし,1]城址、クマ川下り発船所の他だと、
[みぎたいちしゅぞうもと,5]右田一酒造元もそうですよね」
- TW: 「除了御一夜城址、隈河漂流發船點之外，右田一釀酒廠也是其中之一呢」
- Cũ: 「Ngoài Di tích thành Ohito và bến tàu chèo sông Kuma ra,
thì Nhà máy rượu Migita System cũng là một điểm tham quan nhỉ.」
- Sửa: 「Ngoài Di tích thành Ohitoyo và bến tàu chèo sông Kuma ra, thì Nhà máy rượu Migita System cũng là một điểm tham quan nhỉ.」

**1945 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「まずは、御一夜らしいこと。
その魅力を伝える駅弁であること」
- TW: 「首先，要有御一夜特色。您的鐵路便當需要能夠彰顯它的魅力」
- Cũ: 「Trước hết, phải mang đậm chất Ohito.
Phải là một hộp cơm truyền tải được sức hấp dẫn của nơi này.」
- Sửa: 「Trước hết, phải mang đậm chất Ohitoyo. Phải là một hộp cơm truyền tải được sức hấp dẫn của nơi này.」

**2307 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 御一夜[じょうし,1]城址をゆっくり下りれば、
すぐに市役所前に出る。
- TW: 我們慢慢地走下御一夜城址，很快走到了市政府門前。
- Cũ: Từ tốn đi xuống từ Di tích thành Ohito,
sẽ ra ngay trước Tòa thị chính.
- Sửa: Từ tốn đi xuống từ Di tích thành Ohitoyo, sẽ ra ngay trước Tòa thị chính.

**2471 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 御一夜城址、三の丸跡から一望できる御一夜の町。
正直ごくごく平凡な、一昔前の田舎町という印象だったが。
- TW: 站在御一夜城址的三之丸遺址上，便能將御一夜的街道盡收眼底。我對它的印象還停留在原本平凡而落後的小鄉村。
- Cũ: Từ tàn tích Sannomaru của thành Ohito, có thể phóng tầm mắt bao quát toàn bộ thị trấn.
Thành thật mà nói, ấn tượng của tôi về nó chỉ là một thị trấn nông thôn hết sức bình thường của ngày xưa.
- Sửa: Từ tàn tích Sannomaru của thành Ohitoyo, có thể phóng tầm mắt bao quát toàn bộ thị trấn. Thành thật mà nói, ấn tượng của tôi về nó chỉ là một thị trấn nông thôn hết sức bình thường của ngày xưa.

**2551 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: クマ川、焼酎、水、幽霊――
永山さんの「らしさ」がそこに、記されていく。
- TW: 隈河、燒酒、水、幽靈——永山女士依次寫下在她心目中的“特色”。
- Cũ: Sông Kuma, rượu shochu, nước, ma quỷ——
Những 'chất Ohito' theo suy nghĩ của cô Nagayama được ghi lại trên đó.
- Sửa: Sông Kuma, rượu shochu, nước, ma quỷ—— Những 'chất Ohitoyo' theo suy nghĩ của cô Nagayama được ghi lại trên đó.

**2556 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 鯉のぼりに車輪をつけたような御一夜伝統の木工細工は、
小さくとも大きくとも、それぞれ愛嬌に満ちている。
- TW: 雉子馬的外形類似裝了兩個輪子的鯉魚旗，是御一夜傳統的木工工藝品。有大有小，非常討人喜歡。
- Cũ: Món đồ gỗ truyền thống của Ohito, trông như chiếc cờ cá chép được gắn thêm bánh xe,
dù to hay nhỏ đều mang vẻ đáng yêu riêng.
- Sửa: Món đồ gỗ truyền thống của Ohitoyo, trông như chiếc cờ cá chép được gắn thêm bánh xe, dù to hay nhỏ đều mang vẻ đáng yêu riêng.

### Xưng hô (13 dòng)

**1196 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「……記憶にあるより、随分と近代化したのだな」
- TW: 「……與我記憶中相比，這裡已經發展了不少啊」
- Cũ: 「...Đã hiện đại hóa hơn rất nhiều so với trong ký ức của anh nhỉ.」
- Sửa: 「...Đã hiện đại hóa hơn rất nhiều so với trong ký ức của tôi nhỉ.」

**1463 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「いや、そうではない。
もしそうであれば、コンを連れても来てはいないさ」
- TW: 「不，不是的。如果我不想被打擾，就不會帶著空一起來了」
- Cũ: 「Không, không phải vậy.
Nếu thế thì anh đã chẳng mang Kon theo.」
- Sửa: 「Không, không phải vậy. Nếu thế thì tôi đã chẳng mang Kon theo.」

**1538 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「僕でよければ、この手を貸そう。
コンの手よりは、いくらか役に立つはずだ」
- TW: 「只要你不嫌棄，就讓我來幫助你吧。至少應該比空更加派得上用場」
- Cũ: 「Nếu anh có thể giúp được gì, anh sẵn sàng.
Ít ra cũng có ích hơn Kon một chút.」
- Sửa: 「Nếu tôi có thể giúp được gì, tôi sẵn sàng. Ít ra cũng có ích hơn Kon một chút.」

**1563 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「ああ、うむ。観光振興についてだが、
現状、解決すべき点はいくつもあるかと思う」
- TW: 「啊——嗯。關於旅遊業復興，我認為目前有幾點急需解決」
- Cũ: 「À, ừm. Về việc chấn hưng du lịch,
anh nghĩ hiện tại có một vài điểm cần phải giải quyết.」
- Sửa: 「À, ừm. Về việc chấn hưng du lịch, tôi nghĩ hiện tại có một vài điểm cần phải giải quyết.」

**1592 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「ああ、すまん。気やすすぎたな。
妹がいたので、ついつい」
- TW: 「啊，抱歉。這樣太過親近了啊。因為我有個妹妹，一不小心就——」
- Cũ: 「A, xin lỗi. Tự nhiên quá đà rồi.
Tại anh có em gái, nên cứ tiện tay...」
- Sửa: 「A, xin lỗi. Tự nhiên quá đà rồi. Tại tôi có em gái, nên cứ tiện tay...」

**1625 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「ああ、
蔵の一部を見学コースとして開放しているとは聞くな」
- TW: 「嗯，確實有聽說開放了一部分酒窖供遊客參觀」
- Cũ: 「À,
anh có nghe nói họ mở cửa một phần xưởng rượu cho khách tham quan.」
- Sửa: 「À, tôi có nghe nói họ mở cửa một phần xưởng rượu cho khách tham quan.」

**1633 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「ポーレットの提案を受けて、僕は考えたのだ」
- TW: 「在聽了波萊特的提議後，我在想一件事」
- Cũ: 「Nhận được đề xuất của Paulette, anh đã suy nghĩ.」
- Sửa: 「Nhận được đề xuất của Paulette, tôi đã suy nghĩ.」

**1649 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「僕の手で、もしも構わなければ――」
- TW: 「如果你不介意我來幫你的話——」
- Cũ: 「Nếu em không chê sự giúp đỡ của anh——」
- Sửa: 「Nếu em không chê sự giúp đỡ của tôi——」

**1668 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「ということで、
みなのアイディアをもらえないかと考えた」
- TW: 「就是這樣，我想請大家幫忙出主意」
- Cũ: 「Vì vậy,
anh muốn xin ý kiến của mọi người.」
- Sửa: 「Vì vậy, tôi muốn xin ý kiến của mọi người.」

**1699 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「僕とて、たまには一人になりたい時間もあるさ」
- TW: 「我偶爾也想一個人待會嘛」
- Cũ: 「Anh cũng có những lúc muốn ở một mình chứ.」
- Sửa: 「Tôi cũng có những lúc muốn ở một mình chứ.」

**1704 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「\x%l8620;#00ffc040;8620%l;#;を一度じっくり、一人で見ておきたかっただけだ。
ポーレットが来る前に、その目的は達成できていた」
- TW: 「我只是想一個人仔細觀察一下\x%l8620;#00ffc040;８６２０%l;#;，在波萊特來之前，我的目的就已經達成了」
- Cũ: 「Anh chỉ muốn ngắm \x%l8620;#00ffc040;8620%l;#; một mình thật kỹ thôi.
Trước khi Paulette đến, mục đích đó đã hoàn thành rồi.」
- Sửa: 「Tôi chỉ muốn ngắm \x%l8620;#00ffc040;8620%l;#; một mình thật kỹ thôi. Trước khi Paulette đến, mục đích đó đã hoàn thành rồi.」

**1817 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「確かに、観光振興のことを考えてでもあったな。
それが全てでもなかったが」
- TW: 「的確，我來這裡也是為了思考有關旅遊業復興的事。但這並不是全部的原因」
- Cũ: 「Đúng là anh cũng có nghĩ đến việc chấn hưng du lịch.
Dù đó không phải là tất cả lý do.」
- Sửa: 「Đúng là tôi cũng có nghĩ đến việc chấn hưng du lịch. Dù đó không phải là tất cả lý do.」

**1926 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「ならば、ポーレット。今週のスケジュールを貰えるか？
できるだけ早く動きたい」
- TW: 「那麼，波萊特。能把這週的日程表給我嗎？我想要儘快行動」
- Cũ: 「Vậy thì, Paulette. Em cho anh xem lịch trình tuần này được không?
Anh muốn tiến hành càng sớm càng tốt.」
- Sửa: 「Vậy thì, Paulette. Em cho tôi xem lịch trình tuần này được không? Tôi muốn tiến hành càng sớm càng tốt.」

### Sai nghĩa (5 dòng)

**1151 [lời dẫn]** — Dòng bị cắt cụt: JP có 2 câu, bản Việt chỉ còn 1 câu — câu 2 ("Không có Reina xen giữa, không dẫn Hachiroku theo.") đang nằm thừa ở đầu 2196 (cặp lệch vị trí 1151↔2196).

- JP: ……ポーレットと並んで歩く。
れいなを挟まず、ハチロクを連れず。
- TW: ……我與波萊特並肩同行。玲奈不在，八六也不在。
- Cũ: ……Sóng bước cùng Paulette.
- Sửa: ……Sóng bước cùng Paulette. Không có Reina xen giữa, không dẫn Hachiroku theo.

**1683 [Nagi]** — 御一夜 = "Ohitoyo"; Nagi tự xưng 凪様 (ngôi ba) — tiền lệ Paulette 08 future-rail 2277: "Bổn tiểu thư", không phải "Nagi đại nhân" (cách gọi khi Soutetsu gọi Nagi thì khác).

- JP: 「ここにいるばい！
御一夜が地元で観光に詳しい凪様がっ！」
- TW: 「御一夜出身，並且熟知當地旅遊景點的凪大小姐在此咧！」
- Cũ: 「Có em ở đây nè!
Nagi đại nhân, người bản địa Ohito, am hiểu du lịch đây!」
- Sửa: 「Có em ở đây nè! Bổn tiểu thư đây, người bản địa Ohitoyo, am hiểu du lịch đây!」

**1756 [Paulette]** — 廃客車 = toa hành khách bỏ hoang (tiền lệ 廃駅 = "ga bỏ hoang", Paulette 14 1683); bản cũ "phế liệu" — chỗ duy nhất khác trong dự án (日々姫08 3317) dùng "toa hành khách bỏ đi". Thẻ `%l` cho 客車 giữ nguyên.

- JP: 「はい。ですからわたし、廃\x%l客車;#00ffc040;客車%l;#;を譲ってくれる
\x%lまいてつ;#00ffc040;まいてつ%l;#;さんがいないか、あたってみたいと思います」
- TW: 「是的。所以我想找找看有沒有\x%lまいてつ;#00ffc040;掌車人%l;#;願意將廢棄的\x%l客車;#00ffc040;客運車廂%l;#;轉讓給我們」
- Cũ: 「Vâng. Vì vậy, em định tìm xem có \x%lまいてつ;#00ffc040;chủ tàu%l;#; nào
chịu nhượng lại \x%l客車;#00ffc040;toa hành khách%l;#; phế liệu không.」
- Sửa: 「Vâng. Vì vậy, em định tìm xem có \x%lまいてつ;#00ffc040;chủ tàu%l;#; nào chịu nhượng lại \x%l客車;#00ffc040;toa hành khách%l;#; bỏ hoang không.」

**1888 [Soutetsu]** — JP これこそ、まさにキジウマですな — bản Việt bỏ hẳn tên キジウマ (ngựa Kiji); TW "跟雉子馬一樣Ｑ" xác nhận. Câu đùa chỉ có nghĩa khi giữ tên con ngựa gỗ (Paulette bật cười ở 1627).

- JP: 「これこそ、まさにキジウマですな」
- TW: 「這可真是，跟雉子馬一樣Ｑ」
- Cũ: 「Cái này, ngon bá cháy bọ chét luôn.」
- Sửa: 「Cái này, đúng là một con ngựa Kiji mà.」

**2196 [lời dẫn]** — Dòng thừa câu đầu: câu "Không có Reina xen giữa, không dẫn Hachiroku theo." là bản dịch câu 2 của 1151, không thuộc 2196 (cặp lệch vị trí 1151↔2196).

- JP: 故にペースをあわせることなく、自然に歩ける。
歩幅が近いということが、ごく単純に心地良い。
- TW: 因此我不必顧及他人的步伐，走得很自然。兩個人的步幅相近，原來是如此令人感到舒適。
- Cũ: Không có Reina xen giữa, không dẫn Hachiroku theo.
Nên chúng tôi có thể bước đi tự nhiên, không cần phải gượng ép bắt nhịp với ai.
- Sửa: Nên chúng tôi có thể bước đi tự nhiên, không cần phải gượng ép bắt nhịp với ai.

### Lỗi nhỏ (3 dòng)

**1947 [Hibiki]** — JP 「っ！」\n「――っ」 — bản Việt mất cả hai tiếng hít (mẫu mất っ toàn dự án; tiếng hít dịch thành Ư theo quét っ 19/11).

- JP: 「っ！」
「――っ」
- TW: 「！」
「——」
- Cũ: 「!」
「——」
- Sửa: 「Ư!」 「——っ」

**1950 [Paulette]** — JP 「/////っ！！」 — bản Việt "/////!!" mất tiếng hít っ (mẫu mất っ toàn dự án).

- JP: 「/////っ！！」
- TW: 「（臉紅）！！」
- Cũ: 「/////!!」
- Sửa: 「/////Ư!!」

**2480 [lời dẫn]** — JP "――っ！？" — bản Việt "——!?" mất tiếng hít っ (mẫu mất っ toàn dự án).

- JP: ふかみと凪は――っ！？
- TW: 而深美和凪——嗯！？
- Cũ: Fukami và Nagi thì——!?
- Sửa: Fukami và Nagi thì——Ư!?

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
1151 = "……Sóng bước cùng Paulette. Không có Reina xen giữa, không dẫn Hachiroku theo."
1196 = "「...Đã hiện đại hóa hơn rất nhiều so với trong ký ức của tôi nhỉ.」"
1463 = "「Không, không phải vậy. Nếu thế thì tôi đã chẳng mang Kon theo.」"
1524 = "「Nhất thế giới thì có vẻ hơi quá sức, nhưng nhất Hinomoto thì sao. Dù là sông Kuma hay Ohitoyo.」"
1527 = "「Quả thực, những người đến Ohitoyo du lịch, đều là người từ nơi khác đến.」"
1538 = "「Nếu tôi có thể giúp được gì, tôi sẵn sàng. Ít ra cũng có ích hơn Kon một chút.」"
1563 = "「À, ừm. Về việc chấn hưng du lịch, tôi nghĩ hiện tại có một vài điểm cần phải giải quyết.」"
1588 = "「A, đúng vậy nhỉ. Nếu thế thì—— Trong số những người ở đây, người vẫn chưa biết nhiều về Ohitoyo là...」"
1592 = "「A, xin lỗi. Tự nhiên quá đà rồi. Tại tôi có em gái, nên cứ tiện tay...」"
1625 = "「À, tôi có nghe nói họ mở cửa một phần xưởng rượu cho khách tham quan.」"
1633 = "「Nhận được đề xuất của Paulette, tôi đã suy nghĩ.」"
1649 = "「Nếu em không chê sự giúp đỡ của tôi——」"
1668 = "「Vì vậy, tôi muốn xin ý kiến của mọi người.」"
1683 = "「Có em ở đây nè! Bổn tiểu thư đây, người bản địa Ohitoyo, am hiểu du lịch đây!」"
1686 = "「Đậm chất Ohitoyo...」"
1691 = "「Em nghĩ cũng có phần. Ohitoyo tuy không bị không kích trực tiếp như trung tâm thành phố Kumamoto, nhưng mà...」"
1693 = "「Em cũng chưa đi thực tế bao giờ. Từ lúc đến Ohitoyo, em chỉ lo chuyện chính trị và đường sắt thôi.」"
1696 = "「Sức hấp dẫn của Ohitoyo, để thoát khỏi cái mác 'khu suối nước nóng hẻo lánh'. Chúng ta phải suy nghĩ cách quảng bá nó.」"
1699 = "「Tôi cũng có những lúc muốn ở một mình chứ.」"
1704 = "「Tôi chỉ muốn ngắm \\x%l8620;#00ffc040;8620%l;#; một mình thật kỹ thôi. Trước khi Paulette đến, mục đích đó đã hoàn thành rồi.」"
1716 = "「Hibiki chắc hẳn rất rành về Ohitoyo. Là người địa phương, lại còn vẽ biển hiệu nên có mối liên hệ rất mật thiết.」"
1756 = "「Vâng. Vì vậy, em định tìm xem có \\x%lまいてつ;#00ffc040;chủ tàu%l;#; nào chịu nhượng lại \\x%l客車;#00ffc040;toa hành khách%l;#; bỏ hoang không.」"
1776 = "「Có thể lắm ạ, đó là nơi lâu đời nhất ở Ohitoyo mà.」"
1786 = "「Hơn nữa, về Ohitoyo, tôi cũng không biết rõ lắm.」"
1789 = "「Paulette thì sao? Về việc tham quan Ohitoyo ấy.」"
1817 = "「Đúng là tôi cũng có nghĩ đến việc chấn hưng du lịch. Dù đó không phải là tất cả lý do.」"
1820 = "「Hiện tại, Ohitoyo không có đủ sức hấp dẫn để được chọn làm nơi lưu trú, nên chỉ là một điểm dừng chân chớp nhoáng rồi bị bỏ qua... ra là vậy.」"
1846 = "「Chị nói nghe nè, Sou-chan. Chị cũng là người Ohitoyo gốc, nên không biết trong mắt người xứ khác, Ohitoyo có điểm gì hấp dẫn đâu nha.」"
1859 = "「Nói đến du lịch Ohitoyo, chắc chắn phải là chèo thuyền trên sông Kuma rồi! Chúng ta phải đẩy mạnh quảng bá chèo thuyền trên sông Kuma!!」"
1888 = "「Cái này, đúng là một con ngựa Kiji mà.」"
1889 = "「Đây được cho là công trình kiến trúc hiện tồn lâu đời nhất ở Ohitoyo. Chắc là... được xây dựng cách đây 130 hay 140 năm gì đó.」"
1914 = "「Tôi là người phù hợp nhất sao? Từ trước đến nay, tôi hầu như không có ký ức gì về việc đi tham quan Ohitoyo cả.」"
1926 = "「Vậy thì, Paulette. Em cho tôi xem lịch trình tuần này được không? Tôi muốn tiến hành càng sớm càng tốt.」"
1927 = "「Vậy thì sao nào. Em có muốn cùng tôi đi xem thử không? Xem làm thế nào để thúc đẩy du lịch Ohitoyo, dưới một góc nhìn mới.」"
1936 = "「Ngoài Di tích thành Ohitoyo và bến tàu chèo sông Kuma ra, thì Nhà máy rượu Migita System cũng là một điểm tham quan nhỉ.」"
1945 = "「Trước hết, phải mang đậm chất Ohitoyo. Phải là một hộp cơm truyền tải được sức hấp dẫn của nơi này.」"
1947 = "「Ư!」 「——Ư」"
1950 = "「/////Ư!!」"
2196 = "Nên chúng tôi có thể bước đi tự nhiên, không cần phải gượng ép bắt nhịp với ai."
2307 = "Từ tốn đi xuống từ Di tích thành Ohitoyo, sẽ ra ngay trước Tòa thị chính."
2471 = "Từ tàn tích Sannomaru của thành Ohitoyo, có thể phóng tầm mắt bao quát toàn bộ thị trấn. Thành thật mà nói, ấn tượng của tôi về nó chỉ là một thị trấn nông thôn hết sức bình thường của ngày xưa."
2480 = "Fukami và Nagi thì——Ư!?"
2551 = "Sông Kuma, rượu shochu, nước, ma quỷ—— Những 'chất Ohitoyo' theo suy nghĩ của cô Nagayama được ghi lại trên đó."
2556 = "Món đồ gỗ truyền thống của Ohitoyo, trông như chiếc cờ cá chép được gắn thêm bánh xe, dù to hay nhỏ đều mang vẻ đáng yêu riêng."
```

Khối trên đã kiểm chứng: parse được bằng tomllib, đúng 44/44 key, giá trị khớp với JSON. Các giá trị đã viết một dòng (không `\n` thủ công, theo quyết định 19/11 của Hieu: game tự xuống dòng). Dấu —— không có khoảng trắng hai bên.

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- **Soutetsu gọi Paulette "cô" vs "em":** trong file này "em" 10 lần (1845, 1503, 1649, 1928, 1916, 1812, 1651, 1661, 1927, 1926) vs "cô" 0 lần. Cộng dồn P01 + P09–16: "cô" 43 vs "em" 30. **Chương 01 nghiêng "em" 16:2 (cả hai file), trong khi P09–12 nghiêng "cô" 43:3 và P13–16 nghiêng "em" 0:11 — giả thuyết "ranh giới rạch ròi theo chương" bị phá vỡ.** Không quyết định, không thống nhất.
- **コン ("Kuu" vs "Kon"):** JP có コン 11 lần, bản Việt dùng "Kon" 10 lần (lần thứ hai ở 1594 dịch thành "em" — đúng, vì Paulette nói với Kon). "Kuu" 0 lần. Ghi nhận, không tính sai (quyết định đang chờ).
- **帝鉄:** JP có 2 lần xuất hiện trong 1 dòng (1912, thẻ `%l` có 帝鉄 ở cả khóa và hiển thị) — bản Việt đúng dạng docs "Đường sắt Hoàng gia". Không tính sai.
- **"KiHa" vs "Kiha":** 0 lần trong file này. **宮司 / 湯医 / タブレット / 操作板 / 整備体 / 運転ボディ / マスコン / マスターコントローラー / 駿袋 / 端的:** 0 lần trong JP của file này.

## Đề xuất cập nhật context (chưa chốt)

Không có đề xuất mới từ file này.

## Đã kiểm tra và KHÔNG tính là sai

- **1516 "Cô" với Hachiroku:** xưng hô trực tiếp tự nhiên trong tiếng Việt, không đổi nghĩa — đúng.
- **"bà" cho bà Nagayama trong độc thoại** (2554, 2230, 2228, 1152, 2193, 2233) vs "cô" trong thoại (1590, 1755, 1783, 1919, 1920, 1924): quy ước nhất quán trong file (lời dẫn gọi "bà ấy", thoại gọi "cô") với một phụ nữ trung niên — đúng, không tính sai.
- **1450 "%61;":** ký tự lạ này có sẵn trong JP gốc (artefact của Kirikiri), bản Việt giữ nguyên — đúng.
- **1490 "Kusatsu":** theo furigana JP くさつ (TW 草津 đọc khác) — đúng, theo quy tắc JP-trên-TW.
- **2560 "Okinawa":** theo furigana JP おきなわ — đúng, theo quy tắc JP-trên-TW.
- **1912 帝鉄 dạng docs** ("Đường sắt Hoàng gia") — đúng. **1936 "Nhà máy rượu Migita System"** — đúng dạng docs.
- **1825 Soutetsu gọi "Nagi đại nhân":** đây là cách gọi khi Soutetsu xưng hô với Nagi — đúng (chỉ có Nagi tự xưng 凪様 ở 1683 mới sai).
- **1144, 1924 まいてつ = "chủ tàu":** nhất quán với TW 掌車人 — đúng.
- **"mình" trong độc thoại** 10 dòng (2319, 2482, 2300, 2247, 2326, 1144, 2314, 2484, 2347, 2405): tất cả đúng (thành ngữ "một mình"/"giật mình", sở hữu "của mình"/"cho riêng mình", mẫu "Tôi… mình…").
- **Chữ っ cuối từ trong tiếng tượng thanh kéo dài** (1606 "Mogyuuuu~~~", 1523 "Eeeee!?") — không phải tiếng hít bị mất — đúng.
- **Cặp trùng "「A.」" 1568/1561:** JP đều là 「あ」 — đều đúng.

## Kết bài

File 御一夜探し sai 44/369 (11,9%) — file có tỷ lệ sai cao nhất trong nhóm file sạch về cấu trúc, nhưng chỉ có 1 lỗi cấu trúc duy nhất là cặp lệch vị trí 1151↔2196 (cùng loại lời dẫn, khó phát hiện). Phần còn lại là hai lựa chọn hệ thống: Soutetsu "anh" 15/15 lần tự xưng và "Ohito" 25/25 lần. Không còn dòng chưa chắc chắn nào trong file này. Sau khi dán khối TOML trên, chương 01 của tuyến Paulette coi như xong (35 + 44 = 79 dòng sai trên 788 dòng, 10,0%). Bước tiếp theo: audit Paulette 02 (2 file: 古地図, 解放b寝台).

---
**Bổ sung 19/11 (quét っ toàn dự án):** 1 giá trị sửa trong khối trên đã được sửa lại chỗ gasp — 1947 「Ư!」 「——っ」→「Ư!」 「——Ư」 (giữ dấu cách giữa 2 đoạn theo quy tắc không `\n` thủ công; sweep dùng `\n` — cùng nghĩa). Khối TOML đã parse lại: 44/44 key, khớp JSON. Tổng số dòng sai không đổi (44).
