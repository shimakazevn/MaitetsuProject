# Audit: Paulette 11_記憶と記録 — 22 dòng Việt sai (đã đối chiếu JP + TW)

**Kết quả: 22/402 dòng sai (5,5%)** — 0 lệch vị trí, 0 chưa dịch, 0 cụt câu, 0 chưa chắc chắn. File sạch về cấu trúc, lỗi tập trung ở thuật ngữ (タブレット 9 dòng + 御一夜 3 dòng) và tiếng hít っ (7 dòng). Cảnh: cuộc họp kín về vấn đề ghi chép/ký ức của Reina — Soutetsu, Paulette, Đại tư tế Akai, chủ nhà tắm Tororyu-yu và Niiroku bàn cách xử lý thẻ bảng (tablet) của Railord.

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 402 dòng script** (thoại 200: Soutetsu 71, Paulette 45, Chủ nhà tắm Tororyu-yu 31, Đại tư tế Akai 20, Niiroku 17, Reina 16; lời dẫn 202) đối chiếu JP + TW từ CSV "Trang tính 3", target là TOML-2. TW chỉ là nhân chứng thứ hai; chỗ nào JP và TW mâu thuẫn thì theo JP (quy tắc Hieu đặt 19/11).
- Heuristic thoại↔lời dẫn báo **0 dòng** — bắt được 0/22. Toàn bộ lỗi đều là cùng-loại (thuật ngữ, xưng hô, nghĩa, lỗi nhỏ) nên heuristic không thấy được; thêm một bằng chứng nữa rằng heuristic chỉ là cận dưới.
- Không có key-shift sạch (shift 0: 402/402; các shift khác 0,97–0,99 — không có ý nghĩa vì key thưa và lỗi không phải lệch vị trí, không áp dụng).
- TOML và CSV giống hệt nhau về nội dung (284 dòng khác chỉ ở `\n`/khoảng trắng, 0 khác nội dung). Không có dòng CSV trống nào; VN==TW 1 dòng (1019 「…………」 — giống hệt nhau ở cả ba thứ tiếng, không phải chưa dịch).
- `[selections]` rỗng (0 mục). Thẻ `%l`: 47 dòng có thẻ ở cả JP và VN, không dòng nào lệch thẻ.
- Phân loại lỗi: thuật ngữ 12 dòng (タブレット 9, 御一夜 3), sai nghĩa 1 dòng (1001 theo TW sai chủ ngữ), xưng hô 2 dòng (độc thoại "mình" 2600, 2601 — 2601 kèm lỗi dùng từ "thà"), lỗi nhỏ 7 dòng (mất tiếng hít っ). Theo người nói: Soutetsu 10, Paulette 5, lời dẫn 4, Chủ nhà tắm Tororyu-yu 1, Niiroku 1, Đại tư tế Akai 1; Reina 0.
- Thoại sai 18/200 (9,0%), lời dẫn sai 4/202 (2,0%).
- Về xưng hô Soutetsu trong thoại: quét toàn bộ file bằng máy (đã chuẩn hoá `\n` thành khoảng trắng trước khi chạy regex `\b`, theo bài học Paulette 08) — "tôi/Tôi" 8 dòng, "anh/Anh" tự xưng **0 lần**, "cháu/Cháu" 18 dòng (nói với bậc trên: Đại tư tế Akai, chủ nhà tắm — đúng quy cách, trừ 1001 là hệ quả của lỗi sai nghĩa), "em" ngôi hai 2 lần (1337, 1380 — cả hai đều với Reina, không phải Paulette). File này Soutetsu không lần nào tự xưng "anh" — sạch nhất về mặt này trong các file Paulette đã audit.
- Về "mình" trong độc thoại: 11 dòng chứa "mình"/"Mình" — **9 dòng đúng, 2 dòng sai** (2600, 2601). 9 dòng đúng: sở hữu cách ("của mình", "suy nghĩ của mình"), phản thân ("tự mình"), thành ngữ ("giật mình"), và mẫu "Tôi… mình…" ("tôi không biết mình…", "tôi cảm giác mình…", "khi nghe nói mình… tôi lại cảm thấy…"). 2 dòng sai đều là "mình" làm chủ ngữ độc lập trong suy nghĩ ngoặc đơn của Soutetsu.
- Không có file trùng lặp: file này chỉ tồn tại ở 03_Paulette/ (đã kiểm tra danh sách file toàn dự án trong CSV; không có bản sao ở thư mục khác — khác Grand Rewrite 04).

## Kết luận về cơ chế lỗi

Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương, không có dòng mồ côi — đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục): 17/22 dòng sai chỉ xuất hiện đúng 1 lần trong toàn dự án, tại chính key của nó. 5 ngoại lệ đều là chuỗi gasp ngắn chung chung, không phải câu của dòng khác:

- **1771 ("「!」"), 1774 ("「!!」"), 1775 ("「!!!」"), 1776 ("「!!?」")**: các chuỗi gasp ngắn xuất hiện ở hàng chục file — cùng một lỗi nhỏ hệ thống (mất tiếng hít っ) lặp lại ở mọi file, không phải câu của dòng khác. (1772 "「!」\n「!」" chỉ trùng thêm 1 nơi: ハチロク14_橋 1924 — cũng là hai tiếng hít, cùng mẫu lỗi.)

Cơ chế lỗi ở đây là **lỗi từng dòng rải rác + thuật ngữ hệ thống (タブレット 9/22)** — giống các file Paulette 06–10 sạch về cấu trúc. Điểm đáng chú ý: đây là file đầu tiên trong route Paulette mà Soutetsu **không một lần** tự xưng "anh" trong thoại, và là file có mật độ lỗi thoại cao nhất trong nhóm sạch (9,0%) chỉ vì cụm gasp 1771–1777 (7 dòng sai liên tiếp trong một cảnh Paulette hoảng sợ).

## Chi tiết 22 dòng sai

### Thuật ngữ (12 dòng)

**998 [Soutetsu]** — タブレット = "máy tính bảng", không phải "Thẻ bảng" (tiền lệ stove 2076/2642). Thẻ %l giữ nguyên. Lưu ý: glossary trong game (context_trans.md:541) vẫn ghi "Thẻ bảng" — xem đề xuất cập nhật context.

- JP: 「\x%lタブレット;#00ffc040;タブレット%l;#;は……記録と同時に、記憶もしてしまう？
が、脳に近似しているのなら、恐らくプロセッサも――」
- TW: 「\x%lタブレット;#00ffc040;操作板%l;#;在記錄的同時……還會完成記憶？可是，既然處理器與大腦很相似，那恐怕它也——」
- Cũ: 「\x%lタブレット;#00ffc040;Thẻ bảng%l;#……không chỉ ghi chép mà còn ghi nhớ luôn sao?
Nhưng nếu nó gần giống với não bộ, thì có lẽ bộ vi xử lý cũng——」
- Sửa: 「\x%lタブレット;#00ffc040;máy tính bảng%l;#……không chỉ ghi chép mà còn ghi nhớ luôn sao? Nhưng nếu nó gần giống với não bộ, thì có lẽ bộ vi xử lý cũng——」

**1349 [Chủ nhà tắm Tororyu-yu]** — タブレット = "máy tính bảng", không phải "thẻ bảng" (tiền lệ stove 2076/2642). Thẻ %l giữ nguyên.

- JP: 「\x%lタブレット;#00ffc040;タブレット%l;#;ば交換すれば、
どん\x%lレイルロオド;#00ffc040;レイルロオド%l;#;も同一の機能ばできるようになる――」
- TW: 「只要更換\x%lタブレット;#00ffc040;操作板%l;#;，任何\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;都能夠擁有相同的功能——」
- Cũ: 「Chỉ cần thay đổi \x%lタブレット;#00ffc040;thẻ bảng%l;#,
thì bất kỳ \x%lレイルロオド;#00ffc040;Railord%l;# nào cũng có thể thực hiện được chức năng tương tự——」
- Sửa: 「Chỉ cần thay đổi \x%lタブレット;#00ffc040;máy tính bảng%l;#, thì bất kỳ \x%lレイルロオド;#00ffc040;Railord%l;# nào cũng có thể thực hiện được chức năng tương tự——」

**1463 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「わたしは――今の御一夜を……今のれいなを、
今のままをただ守りたくって――」
- TW: 「我只是——想守護現在的御一夜……守護現在的玲奈、守護現狀——」
- Cũ: 「Tôi――chỉ muốn bảo vệ Ohimitera hiện tại……bảo vệ Reina hiện tại,
bảo vệ mọi thứ như hiện tại thôi――」
- Sửa: 「Tôi――chỉ muốn bảo vệ Ohitoyo hiện tại……bảo vệ Reina hiện tại, bảo vệ mọi thứ như hiện tại thôi――」

**1528 [Niiroku]** — タブレット = "máy tính bảng", không phải "thẻ bảng". Ruby [khởi tạo,2] giữ nguyên theo file (1512/1714 cũng giữ ruby).

- JP: 「そういう意味。そうして再び走れるのなら、
自分の\x%lタブレット;#00ffc040;タブレット%l;#;を[イニシャライズ,2]初期化しても構わない」
- TW: 「是的。如果能夠再一次奔跑，就算將我的\x%lタブレット;#00ffc040;操作板%l;#;初始化也沒關係」
- Cũ: 「Ý tôi là vậy đấy. Nếu làm vậy mà có thể chạy lại được,
thì có [khởi tạo,2]khởi tạo lại \x%lタブレット;#00ffc040;thẻ bảng%l;# của tôi cũng không sao.」
- Sửa: 「Ý tôi là vậy đấy. Nếu làm vậy mà có thể chạy lại được, thì có [khởi tạo,2]khởi tạo lại \x%lタブレット;#00ffc040;máy tính bảng%l;# của tôi cũng không sao.」

**1538 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「最悪……れいなは、ディーゼルとして稼働していた……
御一夜鉄道で過ごした時間の、記憶を失う危険さえ――」
- TW: 「最壞情況下，玲奈甚至有可能失去作為\x%lディーゼル気動車;#00ffc040;柴油動車%l;#;運行的……關於御一夜鐵路的所有記憶——」
- Cũ: 「Trường hợp xấu nhất……Reina thậm chí có nguy cơ mất đi ký ức……
về khoảng thời gian hoạt động dưới dạng diesel, khoảng thời gian gắn bó với Đường sắt Ohito――」
- Sửa: 「Trường hợp xấu nhất……Reina thậm chí có nguy cơ mất đi ký ức…… về khoảng thời gian hoạt động dưới dạng diesel, khoảng thời gian gắn bó với Đường sắt Ohitoyo――」

**1550 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「例えば御一夜市の人口が、何年に幾人だった、という
数値や数値群が、データ――事実であり、資料です」
- TW: 「比方說，御一夜市在某一年有多少人口，這樣的一組或多組數值就是Ｄａｔａ——也就是事實、數據」
- Cũ: 「Ví dụ, dân số của thành phố Ohimitera vào năm nào là bao nhiêu người,
những con số hoặc nhóm con số đó chính là Data——sự thật, và là tài liệu.」
- Sửa: 「Ví dụ, dân số của thành phố Ohitoyo vào năm nào là bao nhiêu người, những con số hoặc nhóm con số đó chính là Data——sự thật, và là tài liệu.」

**1551 [Soutetsu]** — タブレット = "máy tính bảng", không phải "thẻ bảng". Thẻ %l giữ nguyên.

- JP: 「例えば、ハチロクの\x%lタブレット;#00ffc040;タブレット%l;#;を
れいなのボディに換装すると、そのボディは――」
- TW: 「比方說，若將八六的\x%lタブレット;#00ffc040;操作板%l;#;裝入玲奈的機體，那麼那個機體——」
- Cũ: 「Ví dụ, nếu lắp \x%lタブレット;#00ffc040;thẻ bảng%l;# của Hachiroku
vào cơ thể của Reina, thì cơ thể đó sẽ——」
- Sửa: 「Ví dụ, nếu lắp \x%lタブレット;#00ffc040;máy tính bảng%l;# của Hachiroku vào cơ thể của Reina, thì cơ thể đó sẽ——」

**1660 [Soutetsu]** — タブレット = "máy tính bảng", không phải "thẻ bảng". Thẻ %l giữ nguyên.

- JP: 「ひょっとして……それが、\x%lタブレット;#00ffc040;タブレット%l;#;ですか？」
- TW: 「莫非……存儲介質就是\x%lタブレット;#00ffc040;操作板%l;#;嗎？」
- Cũ: 「Không lẽ……đó chính là, \x%lタブレット;#00ffc040;thẻ bảng%l;# sao ạ?」
- Sửa: 「Không lẽ……đó chính là, \x%lタブレット;#00ffc040;máy tính bảng%l;# sao ạ?」

**1724 [Đại tư tế Akai]** — タブレット = "máy tính bảng", không phải "thẻ bảng". Thẻ %l giữ nguyên.

- JP: 「そうか……冷静に考えれば、れいなくんの\x%lタブレット;#00ffc040;タブレット%l;#;を
ニイロクに実装するのと大差ない」
- TW: 「這樣啊……冷靜下來一想，這基本上等於將玲奈的\x%lタブレット;#00ffc040;操作板%l;#;安裝到二六體內」
- Cũ: 「Vậy sao……Nghĩ kỹ lại thì, việc này chẳng khác gì
cài đặt \x%lタブレット;#00ffc040;thẻ bảng%l;# của cô bé Reina cho Niiroku cả.」
- Sửa: 「Vậy sao……Nghĩ kỹ lại thì, việc này chẳng khác gì cài đặt \x%lタブレット;#00ffc040;máy tính bảng%l;# của cô bé Reina cho Niiroku cả.」

**1754 [Soutetsu]** — タブレット = "máy tính bảng", không phải "thẻ bảng". Thẻ %l giữ nguyên.

- JP: 「なら、
他者の\x%lタブレット;#00ffc040;タブレット%l;#;をそこに実装してしまえば――」
- TW: 「那麼，如果為其安裝了他人的\x%lタブレット;#00ffc040;操作板%l;#;——」
- Cũ: 「Nếu vậy,
nếu cài đặt \x%lタブレット;#00ffc040;thẻ bảng%l;# của người khác vào đó thì——」
- Sửa: 「Nếu vậy, nếu cài đặt \x%lタブレット;#00ffc040;máy tính bảng%l;# của người khác vào đó thì——」

**2006 [lời dẫn]** — タブレット = "máy tính bảng", không phải "thẻ bảng". Thẻ %l giữ nguyên.

- JP: しかし、\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の\x%lタブレット;#00ffc040;タブレット%l;#;の場合は、
どうなのだろう？
- TW: 但如果換成\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的\x%lタブレット;#00ffc040;操作板%l;#;，又會怎麼樣呢？
- Cũ: Tuy nhiên, trong trường hợp \x%lタブレット;#00ffc040;thẻ bảng%l;# của \x%lレイルロオド;#00ffc040;Railord%l;#,
thì sẽ thế nào?
- Sửa: Tuy nhiên, trong trường hợp \x%lタブレット;#00ffc040;máy tính bảng%l;# của \x%lレイルロオド;#00ffc040;Railord%l;#, thì sẽ thế nào?

**2085 [lời dẫn]** — タブレット = "máy tính bảng", không phải "thẻ bảng". Thẻ %l giữ nguyên.

- JP: 別のボディにその\x%lタブレット;#00ffc040;タブレット%l;#;を換装すれば、
ハチロクは、即座に新しい生を得ることが出来る。
- TW: 只要將\x%lタブレット;#00ffc040;操作板%l;#;更換到其它機體中，八六便能夠重獲新生。
- Cũ: Nếu lắp \x%lタブレット;#00ffc040;thẻ bảng%l;# đó vào một cơ thể khác,
Hachiroku sẽ ngay lập tức có được một cuộc sống mới.
- Sửa: Nếu lắp \x%lタブレット;#00ffc040;máy tính bảng%l;# đó vào một cơ thể khác, Hachiroku sẽ ngay lập tức có được một cuộc sống mới.

### Sai nghĩa (1 dòng)

**1001 [Soutetsu]** — Chủ ngữ là cái thẻ bảng (chủ đề từ 998: タブレットは……記録と同時に、記憶もしてしまう？); TW đọc ngôi thứ nhất ("我似乎…") nên bản cũ theo TW, biến Soutetsu thành chủ ngữ ("cháu"). Theo quy tắc JP-trên-TW.

- JP: 「――いえ。特に区別して取り扱ってはいないようです」
- TW: 「——不。我似乎並沒有刻意去區分它們」
- Cũ: 「——Không ạ. Hình như cháu không có sự phân biệt đặc biệt nào khi xử lý chúng.」
- Sửa: 「——Không ạ. Hình như nó không có sự phân biệt đặc biệt nào khi xử lý chúng.」

### Xưng hô (2 dòng)

**2600 [lời dẫn]** — "Mình" làm chủ ngữ độc lập trong suy nghĩ ngoặc đơn của Soutetsu → "Tôi" (tiền lệ hearing 2580/2584/2586/2590).

- JP: （この笑顔を……見せてもらえなくなるかもしれんのか）
- TW: （我有可能……再也看不到這樣的笑容嗎）
- Cũ: （Liệu mình có thể……không bao giờ được nhìn thấy nụ cười này nữa không.）
- Sửa: （Liệu tôi có thể……không bao giờ được nhìn thấy nụ cười này nữa không.）

**2601 [lời dẫn]** — Hai lỗi trong một dòng: (1) "mình" làm chủ ngữ độc lập trong suy nghĩ ngoặc đơn của Soutetsu → "Tôi"; (2) "thà" là lỗi dùng từ/lỗi đánh máy — "thà… còn hơn…" không có vế sau, đúng ra là "mà gánh vác". Đã chuẩn hoá khoảng trắng quanh ―― theo quy ước.

- JP: （あるいは、僕が、決断までを――
まるごと全てを、いっそ引き受けるべきなのか）
- TW: （或許我應該將最終的決定——甚至所有的一切也一同承擔下來）
- Cũ: （Hay là, mình nên đưa ra quyết định――
thà gánh vác toàn bộ mọi thứ luôn cho rồi.）
- Sửa: （Hay là, tôi nên đưa ra quyết định――mà gánh vác toàn bộ mọi thứ luôn cho rồi.）

### Lỗi nhỏ (7 dòng)

**1008 [Soutetsu]** — JP 「――っ！！？」 là tiếng hít độc lập; bản cũ "——!!?" làm mất tiếng hít.

- JP: 「――っ！！？」
- TW: 「——！！？」
- Cũ: 「——!!?」
- Sửa: 「——Ư!!?」

**1771 [Paulette]** — JP 「っ！」 là tiếng hít độc lập; bản cũ "「!」" làm mất tiếng hít. Tiền lệ 再開発 2103.

- JP: 「っ！」
- TW: 「！」
- Cũ: 「!」
- Sửa: 「Ư!」

**1772 [Paulette]** — JP 「っ！」\n「っ！」 là hai tiếng hít độc lập; bản cũ "「!」\n「!」" làm mất cả hai. Khối TOML viết một dòng (không dùng \n thủ công, theo quy tắc của Hieu).

- JP: 「っ！」
「っ！」
- TW: 「！」
「！」
- Cũ: 「!」
「!」
- Sửa: 「Ư!」 「Ư!」

**1774 [Paulette]** — JP 「っ！！」 là tiếng hít độc lập; bản cũ "「!!」" làm mất tiếng hít.

- JP: 「っ！！」
- TW: 「！！」
- Cũ: 「!!」
- Sửa: 「Ư!!」

**1775 [Soutetsu]** — JP 「っ！！！」 là tiếng hít độc lập; bản cũ "「!!!」" làm mất tiếng hít.

- JP: 「っ！！！」
- TW: 「！！！」
- Cũ: 「!!!」
- Sửa: 「Ư!!!」

**1776 [Soutetsu]** — JP 「っ！！？」 là tiếng hít độc lập; bản cũ "「!!?」" làm mất tiếng hít.

- JP: 「っ！！？」
- TW: 「！！？」
- Cũ: 「!!?」
- Sửa: 「Ư!!?」

**1777 [Paulette]** — JP 「っ！！？」\n「ひゃわっ！！？」 — dòng đầu là tiếng hít độc lập, bản cũ "!!?" làm mất; dòng hai ひゃわっ → "Hyawa" giữ nguyên. Khối TOML viết một dòng (không dùng \n thủ công).

- JP: 「っ！！？」
「ひゃわっ！！？」
- TW: 「！！？」
「呀！！？」
- Cũ: 「!!?」
「Hyawa!!?」
- Sửa: 「Ư!!?」 「Hyawa!!?」

## Bằng chứng cho các quyết định đang chờ Hieu chốt

- **Soutetsu gọi Paulette "cô" vs "em" (thoại): "cô" 9 lần** (1280, 1312, 1381, 1399, 1485, 1488, 1567, 1568, 1722) **vs "em" 0 lần** — trong file này Soutetsu không gọi Paulette là "em" lần nào. Hai lần "em" duy nhất trong thoại Soutetsu đều là với Reina (1337, 1380). Thêm 2 lần "cô Miyamoto" (1414, 1480) — là gọi bà Miyamoto, không tính vào Paulette. Cộng dồn: Paulette 08 đề xuất "em", Paulette 09 "cô" 7 vs "em" 1, Paulette 10 "cô" 20 vs "em" 2, Paulette 11 "cô" 9 vs "em" 0 — **ba file liên tiếp nghiêng mạnh về "cô"**. **Không quyết, chỉ ghi số liệu.**
- **湯医: file này dùng "Yunoi" 1 lần** (1618 "tuyến Yunoi"), 0 lần "Yui". **Chưa chốt.**
- **タブレット = "máy tính bảng" vs "Thẻ bảng":** file này dùng "Thẻ bảng"/"thẻ bảng" ở cả 9 dòng (998 viết hoa, 8 dòng còn lại viết thường) — **đã sửa hết thành "máy tính bảng"** trong khối TOML theo tiền lệ stove 2076/2642. Nhưng lưu ý mâu thuẫn: chính glossary trong game (context_trans.md:541) ghi "Thẻ bảng (tablet)" — xem đề xuất cập nhật context bên dưới.
- **運転士 = "nhân viên cơ vụ": 2 dòng** (2412, 2511) — **không tính sai**, chỉ ghi nhận: cách dịch thiểu số đã có sẵn trong dự án (運転士 → "nhân viên cơ vụ" 9 lần toàn dự án), mâu thuẫn với docs ghi 運転士 là người lái tàu. Cùng nhóm với Paulette 10 (959, 1241, 1998).
- **整備ボディ: 1304 dịch "cơ thể bảo dưỡng"** — **không tính sai**, ghi làm bằng chứng cho đề xuất đang chờ "thân bảo trì" vs "thân vận hành" (xem đề xuất cập nhật context).
- **処理落ち = "xử lý quá tải":** file này dùng nhất quán 3/4 dòng (1403, 1432, 2158); dòng 1473 diễn đạt lại theo ngữ cảnh — không tính sai.

## Đề xuất cập nhật context

1. **Glossary trong game về タブレット (context_trans.md:541):** glossary hiện ghi "Thẻ bảng (tablet)", trong khi tiền lệ audit (stove 2076/2642) và bản sửa file này đều dùng "máy tính bảng". Nếu Hieu giữ "máy tính bảng" thì nên sửa luôn mục glossary này, nếu không lần sau dịch lại sẽ quay về "Thẻ bảng". Đề xuất: đổi glossary thành "máy tính bảng (tablet)".
2. **Ruby [tên,N] trên số hiệu (ví dụ [ニイロク,1]26 ở 1781):** file này giữ ruby ở 1512/1714 ("[Hachiroku,3]8620") và 1528 ("[khởi tạo,2]khởi tạo lại") nhưng bỏ ruby ở 1781 ("Kuha, 26."). Kiểm tra toàn dự án: với mẫu ruby [tên,N] + số, bản Việt **bỏ 306 lần, giữ 14 lần** — bỏ là chuẩn chung của dự án (furigana chỉ là hướng dẫn phát âm cho người đọc tiếng Nhật, không phải nội dung). Vì vậy **1781 không tính sai**. Nếu Hieu muốn thống nhất giữ ruby cho các số hiệu Railord thì 1781 sửa thành "「Kuha, [Niiroku,1]26.」" cho khớp 1512/1714 — nhưng đó sẽ là quyết định đi ngược chuẩn chung 306/320, cần Hieu chốt riêng.

## Những dòng đã kiểm tra và KHÔNG tính sai

- **1019**: VN==TW ("「……」") — giống hệt nhau ở cả ba thứ tiếng, không phải chưa dịch.
- **1978**: TW sai hẳn so với JP (TW viết "chắc là chuẩn bị riêng cho chúng ta" trong khi JP là Akai đặt tài liệu xuống đưa danh sách cho Paulette) — bản Việt theo đúng JP, không tính sai. Một ca JP-trên-TW điển hình.
- **1370**: えっ！？ → "Hả!?" — dịch đúng, không phải lỗi gasp.
- **2142**: "Nghĩ đến việc mình sẽ làm khuôn mặt đó u ám đi, tim tôi lại nhói đau" — "mình" nằm trong mệnh đề phụ "việc mình sẽ…" và câu có "tôi" hiển ngôn ("tim tôi") — giữ nguyên theo tinh thần mẫu "Tôi… mình…". Đây là dòng ranh giới, đã ghi rõ lý do để Hieu soát lại nếu muốn.
- **1473**: 処理落ち được diễn đạt lại theo ngữ cảnh ("biện pháp phòng ngừa việc Reina ngủ gật") — không tính sai.
- **2423**: câu trích dẫn "hôm qua tôi ở nhà đọc sách" thêm chủ ngữ "tôi" cho tự nhiên — JP gốc không có chủ ngữ nhưng đây là bản ghi giả định, thêm "tôi" là hợp lý.
- **2364**: 同情 → "đồng cảm" (vs 憐憫 → "thương hại") — chấp nhận được trong tiếng Việt, không tính sai.

## Khối TOML sửa (đã kiểm chứng: parse được, đúng 22/22 key)

```toml
998 = "「\\x%lタブレット;#00ffc040;máy tính bảng%l;#……không chỉ ghi chép mà còn ghi nhớ luôn sao? Nhưng nếu nó gần giống với não bộ, thì có lẽ bộ vi xử lý cũng——」"
1001 = "「——Không ạ. Hình như nó không có sự phân biệt đặc biệt nào khi xử lý chúng.」"
1008 = "「——Ư!!?」"
1349 = "「Chỉ cần thay đổi \\x%lタブレット;#00ffc040;máy tính bảng%l;#, thì bất kỳ \\x%lレイルロオド;#00ffc040;Railord%l;# nào cũng có thể thực hiện được chức năng tương tự——」"
1463 = "「Tôi――chỉ muốn bảo vệ Ohitoyo hiện tại……bảo vệ Reina hiện tại, bảo vệ mọi thứ như hiện tại thôi――」"
1528 = "「Ý tôi là vậy đấy. Nếu làm vậy mà có thể chạy lại được, thì có [khởi tạo,2]khởi tạo lại \\x%lタブレット;#00ffc040;máy tính bảng%l;# của tôi cũng không sao.」"
1538 = "「Trường hợp xấu nhất……Reina thậm chí có nguy cơ mất đi ký ức…… về khoảng thời gian hoạt động dưới dạng diesel, khoảng thời gian gắn bó với Đường sắt Ohitoyo――」"
1550 = "「Ví dụ, dân số của thành phố Ohitoyo vào năm nào là bao nhiêu người, những con số hoặc nhóm con số đó chính là Data——sự thật, và là tài liệu.」"
1551 = "「Ví dụ, nếu lắp \\x%lタブレット;#00ffc040;máy tính bảng%l;# của Hachiroku vào cơ thể của Reina, thì cơ thể đó sẽ——」"
1660 = "「Không lẽ……đó chính là, \\x%lタブレット;#00ffc040;máy tính bảng%l;# sao ạ?」"
1724 = "「Vậy sao……Nghĩ kỹ lại thì, việc này chẳng khác gì cài đặt \\x%lタブレット;#00ffc040;máy tính bảng%l;# của cô bé Reina cho Niiroku cả.」"
1754 = "「Nếu vậy, nếu cài đặt \\x%lタブレット;#00ffc040;máy tính bảng%l;# của người khác vào đó thì——」"
1771 = "「Ư!」"
1772 = "「Ư!」 「Ư!」"
1774 = "「Ư!!」"
1775 = "「Ư!!!」"
1776 = "「Ư!!?」"
1777 = "「Ư!!?」 「Hyawa!!?」"
2006 = "Tuy nhiên, trong trường hợp \\x%lタブレット;#00ffc040;máy tính bảng%l;# của \\x%lレイルロオド;#00ffc040;Railord%l;#, thì sẽ thế nào?"
2085 = "Nếu lắp \\x%lタブレット;#00ffc040;máy tính bảng%l;# đó vào một cơ thể khác, Hachiroku sẽ ngay lập tức có được một cuộc sống mới."
2600 = "（Liệu tôi có thể……không bao giờ được nhìn thấy nụ cười này nữa không.）"
2601 = "（Hay là, tôi nên đưa ra quyết định――mà gánh vác toàn bộ mọi thứ luôn cho rồi.）"```

## Kết bài

Paulette 11 (22/402, 5,5%) — đứng thứ 9/16 file Paulette, ngay sau Paulette 10 (5,2%). Không có lỗi cấu trúc nào: không lệch vị trí, không tràn chương, không chuỗi xoay vòng. Lỗi đáng chú ý nhất là 1001 (theo TW sai chủ ngữ — cái thẻ bảng bị biến thành Soutetsu) và 9 dòng タブレット "Thẻ bảng" hệ thống; còn lại là 7 tiếng hít っ bị mất tập trung trong một cảnh Paulette hoảng sợ (1771–1777) và 2 dòng "mình" trong suy nghĩ ngoặc đơn (2600, 2601 — 2601 kèm lỗi dùng từ "thà").

**Còn lại cho file này:** không còn gì — 22/22 dòng sai đã có bản sửa trong khối TOML trên; 0 dòng chưa chắc chắn. Hai việc chờ Hieu: (1) chốt glossary タブレット trong game (đề xuất 1 trên) để 9 dòng sửa này không bị dịch ngược lại lần sau; (2) quyết định "cô"/"em" — file này là bằng chứng thứ ba liên tiếp nghiêng về "cô" (9 vs 0).

**Bước tiếp theo:** route Paulette đã audit xong 10 và 11; các file Paulette 12 trở đi chưa audit. Tổng cộng 23 file đã audit: 1.670 dòng sai.
