# Audit: Paulette 08_未来へのレール — 22 dòng Việt sai (đã đối chiếu JP + TW)

**Kết quả: 22/466 dòng sai (4,7%)** — 0 lệch vị trí, 0 chưa dịch, 0 cụt câu, 0 chưa chắc chắn. File sạch về cấu trúc (không có dòng nào mang bản dịch của dòng khác), nhưng mang hai lỗi hệ thống quen thuộc: Soutetsu tự xưng "anh"/"em" trong thoại (10 dòng) và 御一夜 dịch sai theo quyết định mới (8 dòng). Đây là file Paulette 08 thứ nhất (cảnh lễ tốt nghiệp / tương lai của đường sắt Ohitoyo: Soutetsu, Hikari 4 tuổi, Hachiroku, Hibiki, Paulette, Kisaki; Soutetsu suy ngẫm về chuyện làm cha và tương lai của tuyến đường).

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 466 dòng script** (thoại 308, lời dẫn 158) đối chiếu JP + TW từ CSV "Trang tính 3", target là TOML-2. TW chỉ là nhân chứng thứ hai; chỗ nào JP và TW mâu thuẫn thì theo JP (quy tắc Hieu đặt 19/11).
- Heuristic thoại↔lời dẫn báo **0 dòng** — bắt được 0/22. Toàn bộ lỗi đều là cùng-loại (xưng hô, thuật ngữ, nghĩa) nên heuristic không thấy được; thêm một bằng chứng nữa rằng heuristic chỉ là cận dưới.
- Không có key-shift sạch (shift −5..+5 đều ~1,000 — không có ý nghĩa vì key thưa và lỗi không phải lệch vị trí, không áp dụng).
- TOML và CSV giống hệt nhau về nội dung (244 dòng khác chỉ ở `\n`/khoảng trắng, 0 khác nội dung). Không có dòng CSV trống nào; VN==TW 0 dòng.
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Thẻ `%l`: chỉ 1 dòng có thẻ (2090 — xem ghi chú quan sát), không dòng nào lệch thẻ.
- Phân loại lỗi: xưng hô 10 dòng, thuật ngữ 8 dòng (御一夜), nghĩa 4 dòng. Theo người nói: Soutetsu 13, Kisaki 3, Hibiki 1, Nagi 1, lời dẫn 4; Hachiroku 0, Paulette 0, Mayami 0, Hikari 0.
- Về xưng hô Soutetsu trong thoại: quét toàn bộ file bằng máy — "anh" tự xưng 11 lần (8 lần sai + 3 lần đúng khi nói với Hibiki: 1901, 2346, 2347), "em" tự xưng 2 lần (2027, 2264 — đều sai), "tôi" chỉ 1 lần (2024). Tức là trong file này Soutetsu tự xưng "anh"/"em" 13 lần so với "tôi" 1 lần — lựa chọn hệ thống của người dịch, trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).
- Về "mình" trong độc thoại: file có 4 dòng lời dẫn chứa "mình" (2831, 2841, 2968, 3041) — tất cả đều đúng (sở hữu cách: "của mình", "chỉ mình tôi"; thành ngữ "hết sức mình") — không tính sai dòng nào.
- Không có file trùng lặp: file này chỉ tồn tại ở 03_Paulette/ (đã kiểm tra danh sách file toàn dự án trong CSV; không có bản sao ở thư mục khác).

## Kết luận về cơ chế lỗi

Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương, không có trùng lặp nội bộ sai — đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.381 mục): mỗi dòng sai trong file này chỉ xuất hiện đúng 1 lần trong toàn dự án, tại chính key của nó. Cơ chế lỗi ở đây không phải lỗi dán nhầm dòng, mà là **hai lựa chọn dịch hệ thống của người dịch, trái với docs/quyết định đã chốt**, cộng thêm 4 lỗi nghĩa lẻ:

1. **Soutetsu xưng "anh"/"em" trong thoại** (10/10 lần tự xưng sai đều đổi sang "Tôi"; 3 lần "anh" đúng khi nói với Hibiki được giữ nguyên). Khác với 支線 (17/17 "anh"), file này còn có 2 lần Soutetsu tự xưng "em" (2027 "thư gửi cho em", 2264 "lúc đó em cũng đang lâng lâng") — cùng một kiểu sai: người dịch chọn xưng hô thân mật thay vì "Tôi" của docs.
2. **御一夜 dịch "Ohimitera" (7 lần) và "Ohito" (1 lần)** — trái quyết định 19/11 ("Ohitoyo"). Cả 8 dòng đều phải đổi sang "Ohitoyo". Sau khi sửa, file không còn "Ohimitera"/"Ohito" nào.
3. **4 lỗi nghĩa lẻ** (2220 thêm động từ "Tiếp nhận", 2277 đảo chiều tự xưng ngôi ba của Nagi, 2917 thêm từ "khen ngợi", 3119 dịch sai ナッパ服) — đều là lỗi dịch từng dòng, không theo mẫu hệ thống.

## Chi tiết 22 dòng sai

### A. Xưng hô — Soutetsu tự xưng "anh"/"em" thay vì "Tôi" (10 dòng)

**1490 [双鉄]** — Soutetsu tự xưng "Anh" với Hachiroku; docs: "Tôi" ("Anh" chỉ với Hibiki).

- JP: 「……自覚はない、が。\nハチロクがいうなら、そうなのだろうな」
- TW: 「……其實我自己倒沒什麼感覺。不過既然八六這麼說，那就一定是這樣吧」
- Cũ: 「……Anh không tự nhận thức được, nhưng mà.\nNếu Hachiroku đã nói vậy thì chắc là thế rồi」
- Sửa: 「……Tôi không tự nhận thức được, nhưng mà. Nếu Hachiroku đã nói vậy thì chắc là thế rồi」

**1946 [双鉄]** — Soutetsu tự xưng "Anh" với Hachiroku; docs: "Tôi". "em" trong câu là Hachiroku (ngôi hai) — giữ nguyên.

- JP: 「そんな心細いことを言わんでくれ。ひかりのことを、\nお前とれいなに、できれば末永く守って欲しい」
- TW: 「別說這種令人難過的話了。如果可能的話，我希望你和玲奈能永遠守護著光」
- Cũ: 「Đừng nói những lời nghe cô đơn như vậy chứ. Anh muốn em\nvà Reina, nếu có thể, hãy mãi mãi bảo vệ Hikari」
- Sửa: 「Đừng nói những lời nghe cô đơn như vậy chứ. Tôi muốn em và Reina, nếu có thể, hãy mãi mãi bảo vệ Hikari」

**1979 [双鉄]** — Soutetsu tự xưng "Anh" với Hachiroku; docs: "Tôi".

- JP: 「ひかりが居れば、いつか、そのときが来たとしても。\n僕はハチロク、お前を置き去りにしないで済む」
- TW: 「只要有光在，哪怕我離開的日子終將來臨，也不會留下你獨自一人在這世上了」
- Cũ: 「Nếu có Hikari, dù một ngày nào đó khoảnh khắc ấy có đến.\nAnh cũng sẽ không phải bỏ lại Hachiroku một mình」
- Sửa: 「Nếu có Hikari, dù một ngày nào đó khoảnh khắc ấy có đến. Tôi cũng sẽ không phải bỏ lại Hachiroku một mình」

**2027 [双鉄]** — Soutetsu tự xưng "em" (thư gửi cho chính mình); docs: "Tôi".

- JP: 「む？　今さらこの家に僕あての手紙か？」
- TW: 「唔？現在還有給我的信寄到這裡？」
- Cũ: 「Hửm? Giờ này mà còn có thư gửi cho em đến nhà này sao?」
- Sửa: 「Hửm? Giờ này mà còn có thư gửi cho tôi đến nhà này sao?」

**2058 [双鉄]** — Soutetsu tự xưng "Anh" với Mayami; docs: "Tôi".

- JP: 「ああ。そうあってほしいものだな」
- TW: 「嗯。我也算如願以償了」
- Cũ: 「Ừ. Anh cũng mong là như vậy」
- Sửa: 「Ừ. Tôi cũng mong là như vậy」

**2068 [双鉄]** — Soutetsu tự xưng "anh" với Mayami; docs: "Tôi".

- JP: 「うむ。では出迎えにいってくる」
- TW: 「嗯。那我去接她了」
- Cũ: 「Ừm. Vậy anh đi đón cô ấy đây」
- Sửa: 「Ừm. Vậy tôi đi đón cô ấy đây」

**2188 [双鉄]** — Soutetsu tự xưng "Anh"; docs: "Tôi".

- JP: 「成長？　僕がか？」
- TW: 「成長？是指我嗎？」
- Cũ: 「Trưởng thành? Anh á?」
- Sửa: 「Trưởng thành? Tôi á?」

**2199 [双鉄]** — Soutetsu tự xưng "Anh" (chào về nhà, nói với cả nhà gồm Hikari); docs: "Tôi".

- JP: 「ただいま」
- TW: 「我回來了」
- Cũ: 「Anh về rồi đây」
- Sửa: 「Tôi về rồi đây」

**2210 [双鉄]** — Soutetsu tự xưng "anh"; docs: "Tôi".

- JP: 「毎日、毎日がとても嬉しい。幸せだ。\n生きていることが喜びなのだと、教えてもらえた」
- TW: 「我的每天都非常快樂、非常幸福。你們教會了我，活著是一件非常值得高興的事」
- Cũ: 「Mỗi ngày, mỗi ngày đều rất vui. Thật hạnh phúc.\nMọi người đã dạy cho anh biết, được sống chính là một niềm vui sướng.」
- Sửa: 「Mỗi ngày, mỗi ngày đều rất vui. Thật hạnh phúc. Mọi người đã dạy cho tôi biết, được sống chính là một niềm vui sướng.」

**2264 [双鉄]** — Soutetsu tự xưng "em"; docs: "Tôi".

- JP: 「うっかりとこちらの住所を書いてしまったか。\nははっ、僕も、よほど浮かれていたのだな」
- TW: 「是我不小心寫錯了地址吧。哈哈，可能我當時心情有點太激動了」
- Cũ: 「Chắc là lỡ tay viết địa chỉ bên này rồi.\nHa ha, lúc đó em cũng đang lâng lâng lắm mà」
- Sửa: 「Chắc là lỡ tay viết địa chỉ bên này rồi. Ha ha, lúc đó tôi cũng đang lâng lâng lắm mà」

### B. Thuật ngữ theo quyết định mới — 御一夜 = "Ohitoyo" (8 dòng)

**2041 [稀咲]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohito".

- JP: 「あー、御一夜鉄道のみなさん？\nセレモニーは、終わったのだけれど」
- TW: 「啊，御一夜鐵路的各位，典禮已經結束了」
- Cũ: 「A, mọi người bên Đường sắt Ohito ơi?\nBuổi lễ, đã kết thúc rồi đấy ạ.」
- Sửa: 「A, mọi người bên Đường sắt Ohitoyo ơi? Buổi lễ, đã kết thúc rồi đấy ạ.」

**2123 [双鉄]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera". "ba và Paulette" giữ nguyên — Soutetsu nói với con gái Hikari nên tự xưng "ba" là đúng.

- JP: 「御一夜鉄道の存続がなければ、僕とポーレットは\n出会えなかった。ひかりも、産まれていなかった」
- TW: 「如果御一夜鐵路關門了，我與波萊特就不會相遇。光也不會出生」
- Cũ: 「Nếu Đường sắt Ohimitera không tồn tại, ba và Paulette\nđã không gặp nhau. Hikari cũng sẽ không được sinh ra」
- Sửa: 「Nếu Đường sắt Ohitoyo không tồn tại, ba và Paulette đã không gặp nhau. Hikari cũng sẽ không được sinh ra」

**2363 [双鉄]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera". "Học viện Yui" giữ nguyên — quyết định 湯医 (Yui vs Yunoi) chưa chốt.

- JP: 「湯医学園は、一年生になったらひかりが通う学園だ。\n湯医学園があったから、御一夜鉄道は存続できた」
- TW: 「等光升上一年級，就要到湯醫學園上學了。有湯醫學園維持，御一夜鐵路才能存續下去」
- Cũ: 「Học viện Yui là ngôi trường mà Hikari sẽ theo học khi lên lớp một.\nNhờ có Học viện Yui mà Đường sắt Ohimitera mới có thể tồn tại được」
- Sửa: 「Học viện Yui là ngôi trường mà Hikari sẽ theo học khi lên lớp một. Nhờ có Học viện Yui mà Đường sắt Ohitoyo mới có thể tồn tại được」

**2380 [稀咲]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 「この晴れの日を、御一夜市長として迎えられますことを、卒業生の一人として、大きな誇りに感じます」
- TW: 「能作為御一夜市長迎來這個可喜可賀的日子，身為校友的一員，我感到無上光榮」
- Cũ: 「Với tư cách là Thị trưởng Ohimitera, tôi cảm thấy vô cùng tự hào khi được chào đón ngày trọng đại này với tư cách là một cựu học sinh」
- Sửa: 「Với tư cách là Thị trưởng Ohitoyo, tôi cảm thấy vô cùng tự hào khi được chào đón ngày trọng đại này với tư cách là một cựu học sinh」

**2391 [稀咲]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 「未来の新入生代表。そして、未来の御一夜鉄道代表。\n右田ひかりちゃんからお願いします」
- TW: 「請未來的新生代表，同時也是未來的御一夜鐵路代表，右田光小朋友獻花」
- Cũ: 「Đại diện học sinh mới tương lai. Và, đại diện Đường sắt Ohimitera tương lai.\nXin mời bé Migita Hikari」
- Sửa: 「Đại diện học sinh mới tương lai. Và, đại diện Đường sắt Ohitoyo tương lai. Xin mời bé Migita Hikari」

**2438 [日々姫]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: 「なら！　まかせて！！\n投炭だったら、わたし、御一夜で一番上手やけん！！」
- TW: 「那好！交給我吧！！我可是御一夜最擅長加煤的人！！」
- Cũ: 「Nếu vậy! Cứ để em lo!!\nNói về xúc than thì em là người giỏi nhất Ohimitera đó nha!!」
- Sửa: 「Nếu vậy! Cứ để em lo!! Nói về xúc than thì em là người giỏi nhất Ohitoyo đó nha!!」

**2672 [monologue]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera". "Học viện Yui" giữ nguyên — quyết định 湯医 chưa chốt.

- JP: 御一夜鉄道の存続を支え続けてくれたのは、\n間違いなく湯医学園の通学生だ。
- TW: 不用說，支持御一夜鐵路存續的乘客，便是湯醫學園的學生。
- Cũ: Những người đã liên tục hỗ trợ sự tồn tại của Đường sắt Ohimitera,\nchắc chắn là các học sinh đi lại của Học viện Yui.
- Sửa: Những người đã liên tục hỗ trợ sự tồn tại của Đường sắt Ohitoyo, chắc chắn là các học sinh đi lại của Học viện Yui.

**2900 [monologue]** — 御一夜 = "Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: そもそも御一夜鉄道には、貨物列車も走っていないし、\nこの重そうな機関車に、30kgレールは耐えられなかろう。
- TW: 御一夜鐵路上沒有貨運列車，而且以目前的３０公斤鐵軌，應該也沒有辦法承載這輛看起來十分沉重的機車吧。
- Cũ: Vốn dĩ Đường sắt Ohimitera không có tàu chở hàng chạy,\nvà đường ray 30kg cũng không thể chịu được chiếc đầu máy có vẻ nặng nề này.
- Sửa: Vốn dĩ Đường sắt Ohitoyo không có tàu chở hàng chạy, và đường ray 30kg cũng không thể chịu được chiếc đầu máy có vẻ nặng nề này.

### C. Nghĩa (4 dòng)

**2220 [ハチロク]** — Bản cũ thêm động từ "Tiếp nhận" không có trong JP/TW. JP chỉ hỏi "Cái gì cơ?".

- JP: 「なにを、でしょうか？」
- TW: 「扎根的，是什麼？」
- Cũ: 「Tiếp nhận điều gì cơ ạ?」
- Sửa: 「Cái gì cơ ạ?」

**2277 [凪]** — JP 凪さま là Nagi tự xưng ngôi ba (TW 本小姐 "bổn tiểu thư" xác nhận); bản cũ dịch thành hô ngữ "Nagi đại nhân!" — đảo chiều câu (biến chủ ngữ thành người được gọi).

- JP: 「凪さま！　呼びにいってくるばい！！」
- TW: 「本小姐這就去叫她嘞！！」
- Cũ: 「Nagi đại nhân! Sẽ đi gọi liền đây!!」
- Sửa: 「Bổn tiểu thư sẽ đi gọi liền đây!!」

**2917 [monologue]** — Bản cũ thêm từ "khen ngợi" không có trong JP/TW.

- JP: 自然と、言葉がこぼれ出す。
- TW: 我不由得脫口而出。
- Cũ: Lời khen ngợi tự nhiên thốt ra.
- Sửa: Lời nói tự nhiên thốt ra.

**3119 [monologue]** — ナッパ服 = "đồ da nappa" (tiền lệ Grand 01); bản cũ "trang phục làm việc". TW 彩頁服 là đọc sai (彩頁 = trang màu), không theo.

- JP: 止める間もなく、凪が全速で駆けていく。\nが、日々姫も今はナッパ服、僕と同じく炭塵まみれだ。
- TW: 還沒等我阻止，凪就全速飛奔出去。但是日日姬現在還穿著彩頁服，跟我一樣渾身煤灰呢。
- Cũ: Chưa kịp ngăn lại, Nagi đã chạy đi với tốc độ tối đa.\nNhưng Hibiki bây giờ cũng đang mặc trang phục làm việc, dính đầy bụi than giống như tôi.
- Sửa: Chưa kịp ngăn lại, Nagi đã chạy đi với tốc độ tối đa. Nhưng Hibiki bây giờ cũng đang mặc đồ da nappa, dính đầy bụi than giống như tôi.

## Các cặp trùng lặp / lệch vị trí đã xác nhận

**0 cặp.** Không có dòng nào bị lệch vị trí, không có chuỗi xoay vòng, không có dòng nào mang bản dịch của dòng khác (kiểm chứng bằng chỉ mục Việt toàn dự án: mỗi dòng sai chỉ xuất hiện đúng 1 lần, tại chính key của nó). Không có giá trị Việt trùng lặp nội bộ trong file (0 cặp trùng).

## Dòng chưa chắc chắn

**0 dòng.** Mọi lỗi đều đã có bản sửa.

## Ghi chú quan sát (không tính lỗi, không đưa vào khối TOML)

- **2090 [双鉄]:** bản Việt thêm thẻ `%l` cho 2D3 và 4-8-6 trong khi JP chỉ có dấu ruby [せんりん,1] / [にーでーさん,2] — nhưng nội dung hiển thị đúng và khớp với thẻ của TW, nên không tính lỗi. Thẻ được giữ nguyên như cũ.
- **2836 [monologue]:** "KiHa 07S" viết liền trong câu (không phải thẻ) — đúng dạng tên xe, không sửa.
- **湯医 (bằng chứng cho quyết định đang chờ):** JP ở 2306 có furigana ゆのい trên 湯医 — thêm một bằng chứng cho đề xuất "tuyến Yunoi" (đã có ở Grand 01, Hachiroku 13 夜の嵐). 9 dòng "Yui" trong file (1888, 1910, 2301, 2306, 2363, 2447, 2672, 3042, 3043) KHÔNG tính sai — chờ Hieu chốt Yui hay Yunoi rồi thống nhất toàn dự án.
- **帝鉄:** 2 dòng trong file (2384, 2777) dùng đúng dạng docs "Đường sắt Hoàng gia" — không sửa; quyết định tổng thể vẫn đang chờ.
- **Soutetsu xưng "anh" ĐÚNG (giữ nguyên):** 1901, 2346, 2347 — cả ba đều nói với Hibiki, đúng docs ("Anh" chỉ với Hibiki). 2024 là lần duy nhất Soutetsu xưng "tôi" trong thoại của file.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)

- 御一夜 → "Ohitoyo" trong các bản sửa (quyết định 19/11; sau khi sửa file không còn "Ohimitera"/"Ohito" nào).
- ナッパ服 → "đồ da nappa" (tiền lệ Grand 01).
- 湯医 → "Yui" giữ nguyên trong các dòng đúng (quyết định chưa chốt — xem trên).
- 帝鉄 → "Đường sắt Hoàng gia" (dạng docs, có sẵn trong file ở 2384, 2777).
- 冥軍, 冥国, 小畑, コン, 駿袋鉄道, 整備体/運転ボディ không xuất hiện trong file này.
- Soutetsu gọi Hachiroku bằng "em" (ngôi hai, đúng — 1946 sau khi sửa); gọi Hibiki bằng "em" và xưng "anh" với cô (1901, 2346, 2347 — đúng, giữ nguyên).

## Đề xuất cập nhật context (chưa quyết định — cần Hieu chốt)

Không có đề xuất mới từ file này. Các quyết định đang chờ (帝鉄, 湯医 Yui vs Yunoi, コン, Fukami "mình" vs "Tôi", Soutetsu gọi Paulette "cô" vs "em") không có thêm bằng chứng mới ở đây, trừ bằng chứng furigana ゆのい ở 2306 (xem ghi chú quan sát) — ủng hộ đề xuất "tuyến Yunoi" đã có từ trước.

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)

Lưu ý khi chép: các bản sửa viết liền một dòng, không chèn `\n` thủ công — theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng. Khối này đã kiểm tra bằng máy: trích khối từ chính file review, parse bằng tomllib — **22/22 key** khớp đúng tập dòng sai, không thừa không thiếu, giá trị sau khi parse khớp đúng bản sửa.

```toml
1490 = "「……Tôi không tự nhận thức được, nhưng mà. Nếu Hachiroku đã nói vậy thì chắc là thế rồi」"
1946 = "「Đừng nói những lời nghe cô đơn như vậy chứ. Tôi muốn em và Reina, nếu có thể, hãy mãi mãi bảo vệ Hikari」"
1979 = "「Nếu có Hikari, dù một ngày nào đó khoảnh khắc ấy có đến. Tôi cũng sẽ không phải bỏ lại Hachiroku một mình」"
2027 = "「Hửm? Giờ này mà còn có thư gửi cho tôi đến nhà này sao?」"
2041 = "「A, mọi người bên Đường sắt Ohitoyo ơi? Buổi lễ, đã kết thúc rồi đấy ạ.」"
2058 = "「Ừ. Tôi cũng mong là như vậy」"
2068 = "「Ừm. Vậy tôi đi đón cô ấy đây」"
2123 = "「Nếu Đường sắt Ohitoyo không tồn tại, ba và Paulette đã không gặp nhau. Hikari cũng sẽ không được sinh ra」"
2188 = "「Trưởng thành? Tôi á?」"
2199 = "「Tôi về rồi đây」"
2210 = "「Mỗi ngày, mỗi ngày đều rất vui. Thật hạnh phúc. Mọi người đã dạy cho tôi biết, được sống chính là một niềm vui sướng.」"
2220 = "「Cái gì cơ ạ?」"
2264 = "「Chắc là lỡ tay viết địa chỉ bên này rồi. Ha ha, lúc đó tôi cũng đang lâng lâng lắm mà」"
2277 = "「Bổn tiểu thư sẽ đi gọi liền đây!!」"
2363 = "「Học viện Yui là ngôi trường mà Hikari sẽ theo học khi lên lớp một. Nhờ có Học viện Yui mà Đường sắt Ohitoyo mới có thể tồn tại được」"
2380 = "「Với tư cách là Thị trưởng Ohitoyo, tôi cảm thấy vô cùng tự hào khi được chào đón ngày trọng đại này với tư cách là một cựu học sinh」"
2391 = "「Đại diện học sinh mới tương lai. Và, đại diện Đường sắt Ohitoyo tương lai. Xin mời bé Migita Hikari」"
2438 = "「Nếu vậy! Cứ để em lo!! Nói về xúc than thì em là người giỏi nhất Ohitoyo đó nha!!」"
2672 = "Những người đã liên tục hỗ trợ sự tồn tại của Đường sắt Ohitoyo, chắc chắn là các học sinh đi lại của Học viện Yui."
2900 = "Vốn dĩ Đường sắt Ohitoyo không có tàu chở hàng chạy, và đường ray 30kg cũng không thể chịu được chiếc đầu máy có vẻ nặng nề này."
2917 = "Lời nói tự nhiên thốt ra."
3119 = "Chưa kịp ngăn lại, Nagi đã chạy đi với tốc độ tối đa. Nhưng Hibiki bây giờ cũng đang mặc đồ da nappa, dính đầy bụi than giống như tôi."
```

## Việc tiếp theo

- Không có dòng nào chưa chắc chắn trong file này — mọi lỗi đều đã có bản sửa.
- Sau khi áp 22 bản sửa, file coi như xong, trừ việc chờ Hieu chốt các quyết định đang chờ (đặc biệt 湯医 Yui vs Yunoi — file này có 9 dòng "Yui" sẽ cần thống nhất nếu chốt "Yunoi").
- File Paulette 08 thứ hai (線から面へ) đã được kiểm tra riêng — xem `audit-paulette08-line-to-plane-REVIEW.md`.

## Kết bài

File 未来へのレール là một file sạch về cấu trúc nhưng nặng về xưng hô hệ thống theo kiểu đã thấy ở 支線: người dịch nhất quán dùng "anh"/"em" cho Soutetsu trong thoại (13 lần tự xưng thân mật so với chỉ 1 lần "tôi") và nhất quán dùng "Ohimitera"/"Ohito" cho 御一夜. Hai sự nhất quán này đều trái với docs/quyết định đã chốt, nên 18/22 bản sửa là sửa cơ học, không có chỗ nào phải đắn đo về nghĩa. 4 lỗi nghĩa còn lại đều là lỗi lẻ từng dòng (thêm từ, đảo chiều tự xưng, dịch sai một thuật ngữ). Không có lệch vị trí nào — khác hẳn các file "rối" như 廃炭鉱 hay 夜の嵐 — nên file này không cần lần đọc thứ hai về cấu trúc. Sau khi áp 22 bản sửa (và chờ chốt 湯医), file coi như xong. Hai file Paulette 08 cùng nhau cho thấy một quy luật đã lặp lại: hai file cùng một chương có thể khác nhau về bản chất lỗi — 未来へのレール nặng về xưng hô của Soutetsu trong thoại, 線から面へ nặng hơn về thuật ngữ và có thêm cả lỗi xưng hô trong độc thoại.
