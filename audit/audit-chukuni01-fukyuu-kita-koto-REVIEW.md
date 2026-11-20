# Audit — 仲国01_副丘→北琴.txt.toml

- File: `仲国01_副丘→北琴.txt.toml` — route 10_Chikuni, 349 dòng script (độc thoại 128, thoại Soutetsu 85, Hachiroku 76, Hibiki 52, CA 6, loa phát thanh 2).
- Nội dung: chuyến bay 248 của Hãng hàng không Quốc tế Trung Quốc từ Fukuoka (Phụ Khâu) đến Bắc Cầm (Bắc Cầm): Soutetsu, Hibiki và Hachiroku lần đầu ra nước ngoài — điền thẻ nhập cảnh, đăng ký dấu vân tay, bữa ăn trên máy bay (Hachiroku được phục vụ than antraxit), và bàn về vai trò của mỗi người trong chuyến khảo sát "Nine Stars phiên bản Trung Quốc".
- **Kết quả: 22/349 dòng sai (6,3%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (349 dòng, 0 khóa trùng, 0 ô VN trống); VN khớp TOML tuyệt đối 349/349 sau khi chuẩn hoá \n (242 dòng chỉ khác ở chỗ TOML-2 làm phẳng dấu \n thành khoảng trắng, đã biết, không phải lỗi). `[selections]` rỗng. File là 1 bản duy nhất, không thuộc 11 nhóm trùng.
- TOML md5 `ecae81ef3a0b3b46296df859a3c01807` (UTF-8 BOM + CRLF); không có bản sao (đã kiểm tra md5 toàn bộ 227 file TOML — chỉ 1 bản trùng md5 này).
- Thẻ %l: 0 thẻ sai định dạng. 8 dòng VN có thẻ %l, khớp JP ở các dòng JP có tag; 5 dòng VN tự thêm tag gloss cho thuật ngữ (1706, 1722, 2085, 2113, 2185 — タブレット/共感/整備体) — đây là quy ước gloss thuật ngữ có khắp dự án (toàn dự án: 共感 13 dòng, 整備体 9 dòng, タブレット 2 dòng VN tự thêm tag khi JP không có), không phải lỗi riêng của file; gloss đã sửa về thuật ngữ đã chốt ở §2. Không có thẻ %l nào VN tự thêm cho từ không phải thuật ngữ.
- Đại từ Soutetsu: "anh" đúng với Hibiki và khi nói với cả nhóm (1400, 1704, 1838, 1846, 2110); 6 dòng "anh" sai vì địa chỉ chỉ có Hachiroku (1356 là số nhiều, 1744, 1943, 1999, 2162, 2173) — đã sửa thành "tôi". Soutetsu gọi Hachiroku "em" đúng toàn file; Hachiroku gọi Soutetsu "ngài Soutetsu" đúng toàn file.
- Thuật ngữ: Ohitoyo 1 dòng sai (2013); タブレット gloss "thẻ bảng" 2 dòng (1706, 2113); 定期券 "vé tháng" 3 dòng (1790, 2035, 2091); 整備体 gloss "thân chính" 1 dòng (2085). 日ノ本 dịch "Hinomoto" nhất quán toàn file — câu hỏi "Hinomoto" vs "Hinamoto" đang chờ Hieu, không tự đổi. 運転体 2011 ("thân lái") không tính sai — xem §6.

## §2. Danh sách sửa (22 dòng)

Phân loại: đại từ 6 (1356, 1744, 1943, 1999, 2162, 2173 — Soutetsu "anh"→"tôi" với Hachiroku; 1356 là số nhiều "các em"), thuật ngữ 7 (1706, 1790, 2013, 2035, 2085, 2091, 2113), dịch sai 5 (1329, 1403, 1834, 1888, 2137), gasp 2 (1776, 1803 — はうっ→"HaƯ"; 1803 thêm lỗi 綺麗な顔→"mặt sạch"), SFX 1 (2207), dấu câu 1 (2407).

### 1329 — Độc thoại — mistranslation
- JP: ……話を振ったつもりであったが、\nあいにく何の反応もない。
- TW: ……本想找個話題打破一下沉悶的氣氛，但邊上的兩人卻對此毫無反應。
- VN cũ: ……Tôi định bắt chuyện với em ấy,\nnhưng tiếc là chẳng có phản ứng gì.
- Sửa: ……Tôi định bắt chuyện với hai người,\nnhưng tiếc là chẳng có phản ứng gì.
- Lý do: JP 「話を振ったつもりであったが、あいにく何の反応もない」— Soutetsu định bắt chuyện nhưng không ai đáp lại; TW nói rõ 「邊上的兩人」 (hai người bên cạnh) không có phản ứng. VN cũ "với em ấy" (số ít, một người) sai số lượng người nghe. Sửa "với hai người" theo TW.

### 1356 — Soutetsu — pronoun
- JP: 「……すまんな。ありがとう。\n僕も日々姫を、ハチロクを。補えるように努めよう」
- TW: 「……不好意思，謝謝。我也會努力做到能夠幫上日日姬和八六的」
- VN cũ: 「……Xin lỗi em. Cảm ơn em.\nAnh cũng sẽ cố gắng để bù đắp cho Hibiki, cho Hachiroku.」
- Sửa: 「……Xin lỗi các em. Cảm ơn các em.\nAnh cũng sẽ cố gắng để bù đắp cho Hibiki, cho Hachiroku.」
- Lý do: JP nêu đích danh cả 日々姫 lẫn ハチロク trong cùng một dòng (「僕も日々姫を、ハチロクを」), Soutetsu đang nói với cả hai cô gái. VN cũ "Xin lỗi em. Cảm ơn em." (số ít) sai số lượng người nghe. Sửa "các em". Dòng sau "Anh cũng sẽ…" giữ "Anh" vì Hibiki có mặt trong cảnh (đại từ "anh" với Hibiki đúng).

### 1403 — Soutetsu — mistranslation
- JP: 「……搭乗までの大騒ぎが、ウソのようだな」
- TW: 「……看著她們現在的樣子，誰能想到登機前的那種折騰勁」
- VN cũ: 「……Sự ồn ào trước khi lên máy bay, cứ như là nói dối vậy.」
- Sửa: 「……Sự ồn ào trước khi lên máy bay, giờ cứ như chưa từng xảy ra vậy.」
- Lý do: JP 「搭乗までの大騒ぎが、ウソのようだな」— "uống như một lời nói dối" = cảm giác như chưa từng có thật. VN cũ "cứ như là nói dối vậy" là calque từng chữ: chủ ngữ "sự ồn ào" không thể "nói dối". Sửa "giờ cứ như chưa từng xảy ra vậy" (TW: 「誰能想到登機前的那種折騰勁」 — ai ngờ được sự ồn ào trước khi lên máy bay).

### 1706 — Hachiroku — terminology
- JP: 「で、ございましょうね。レイルロオドの個体認証なら、\nこれはタブレットが絶対確実でございますから」
- TW: 「似乎確實如此呢。其實要識別鐵路人偶的身份的話，檢查一下操作板就萬無一失了」
- VN cũ: 「Có lẽ là vậy ạ. Nếu là xác thực cá nhân của Railord,\nthì \x%lタブレット;#00ffc040;thẻ bảng%l;#; này mới là thứ chắc chắn tuyệt đối ạ.」
- Sửa: 「Có lẽ là vậy ạ. Nếu là xác thực cá nhân của Railord,\nthì \x%lタブレット;#00ffc040;máy tính bảng%l;#; này mới là thứ chắc chắn tuyệt đối ạ.」
- Lý do: Thuật ngữ đã chốt: 操作板/タブレット = "máy tính bảng". VN cũ gloss "thẻ bảng" sai thuật ngữ; trong chính file này, các dòng không tag (2076, 2138) đều dùng "máy tính bảng". Sửa gloss cho nhất quán với thuật ngữ đã chốt và với chính file.

### 1744 — Soutetsu — pronoun
- JP: 「なるほどな。教えてくれてありがとう」
- TW: 「原來如此。謝謝你解釋得這麼詳細」
- VN cũ: 「Ra là vậy. Cảm ơn em đã chỉ cho anh.」
- Sửa: 「Ra là vậy. Cảm ơn em đã chỉ cho tôi.」
- Lý do: Đại từ Soutetsu: địa chỉ là Hachiroku — dòng ngay trước (1743) là Hachiroku giải thích về đường truyền Internet, Soutetsu cảm ơn cô ấy ("教えてくれてありがとう"). Theo quy tắc đã sửa, Soutetsu là "tôi" với Hachiroku, không phải "anh". Sửa "chỉ cho anh" → "chỉ cho tôi".

### 1776 — Hachiroku — gasp
- JP: 「はうっ！？　わたくし、あのっ、そのっ」
- TW: 「哇！？我……我哪有……」
- VN cũ: 「Hả!? Em, dạ, chuyện đó.」
- Sửa: 「HaƯ!? Em, dạ, chuyện đó.」
- Lý do: JP 「はうっ！？」— っ gắn với từ-âm はう là gasp theo phán quyết 20/11 (っ trên từ-âm ああ/はう → thêm Ư; tiền lệ 仲国05 2254 "haƯ"). VN cũ "Hả!?" làm mất gasp. Sửa "HaƯ!?".

### 1790 — Hachiroku — terminology
- JP: 「ああ、仲国でいんたあねっと線に乗るには、\n仲国の事業者の定期券が必要となるわけですね？」
- TW: 「哦，如果要乘仲國網路線路的話，就需要仲國的公司的定期票了，對吧？」
- VN cũ: 「A, vậy là để đi tuyến Internet ở Trung Quốc,\nthì cần phải có vé tháng của nhà cung cấp ở Trung Quốc đúng không ạ?」
- Sửa: 「A, vậy là để đi tuyến Internet ở Trung Quốc,\nthì cần phải có vé định kỳ của nhà cung cấp ở Trung Quốc đúng không ạ?」
- Lý do: Thuật ngữ đã chốt: 定期券 = "vé định kỳ". VN cũ "vé tháng" sai thuật ngữ. Sửa.

### 1803 — Hibiki — gasp
- JP: 「はうっ！？　き、綺麗な顔って……うれしかと。\nあっ！？　違くて、そうじゃなくって――あ！」
- TW: 「唔哇！？說我臉蛋漂亮……好開心哦。啊！？不對，不是說那個……啊！」
- VN cũ: 「Hả!? M, mặt sạch……em vui lắm.\nA!? Không phải, không phải ý đó——a!」
- Sửa: 「HaƯ!? M, mặt xinh đẹp……em vui lắm.\nA!? Không phải, không phải ý đó——a!」
- Lý do: Hai lỗi trong một dòng. (1) JP 「はうっ！？」— gasp, như 1776: "Hả!?" → "HaƯ!?". (2) JP 「き、綺麗な顔って……うれしかと」— Hibiki vui vì được khen có "khuôn mặt xinh đẹp"; TW 「說我臉蛋漂亮」. VN cũ "mặt sạch" dịch sai 綺麗 (đẹp → sạch). Sửa "mặt xinh đẹp". "A!?" cuối dòng giữ nguyên (あっ là cảm thán ngắn, không phải gasp).

### 1834 — Hibiki — mistranslation
- JP: 「ん……っしょ――うん……っと！\nはい！　こいばお手本！！」
- TW: 「嗯……這樣——嗯……好！妥咧！就照這個填吧！！」
- VN cũ: 「Ưm……hầy——ưm……rồi!\nĐây! Đây là mẫu nè!!」
- Sửa: 「Ưm……như vậy——ưm……rồi!\nĐây! Đây là mẫu nè!!」
- Lý do: JP 「ん……っしょ――うん……っと！」— っしょ là dạng rút gọn của でしょ (Hibiki đang điền mẫu đơn: "ừm… là thế này — ừm… xong!"); TW 「嗯……這樣——嗯……好！」 xác nhận "như vậy". VN cũ "hầy" là phiên âm vô nghĩa. Sửa "như vậy".

### 1888 — Hibiki — mistranslation
- JP: 「わかった！　ってか、にぃにたちも準備して！\nまだわたしたち、[アライバルカード,4]入境許可証も書いとらんけん！！」
- TW: 「好噠！等等，阿哥你們倒是也準備一下啦！咱們的入境登記卡還沒填吶！！」
- VN cũ: 「Em biết rồi! Mà này, anh hai cũng chuẩn bị đi!\nChúng ta vẫn chưa điền thẻ nhập cảnh nữa đó!!」
- Sửa: 「Em biết rồi! Mà này, anh hai, mọi người cũng chuẩn bị đi!\nChúng ta vẫn chưa điền thẻ nhập cảnh nữa đó!!」
- Lý do: JP 「にぃにたちも準備して！」— にぃにたち là số nhiều (Soutetsu và mọi người); TW 「阿哥你們倒是也準備一下啦」 ("các anh/em"). VN cũ "anh hai cũng chuẩn bị đi!" (số ít) sai số lượng. Sửa "anh hai, mọi người cũng chuẩn bị đi!".

### 1943 — Soutetsu — pronoun
- JP: 「僕らには捉え得ぬ、『仲国のレイルロオドから見た\n仲国の鉄路』を。ハチロク。お前には捉えてほしい」
- TW: 「我們難以了解到的“仲國鐵路人偶眼中的仲國鐵路”，就全部交給你負責了，八六」
- VN cũ: 「Thứ mà chúng ta không thể nắm bắt được, 『Tuyến đường sắt Trung Quốc\nqua góc nhìn của Railord Trung Quốc』. Hachiroku. Anh muốn em nắm bắt điều đó.」
- Sửa: 「Thứ mà chúng ta không thể nắm bắt được, 『Tuyến đường sắt Trung Quốc\nqua góc nhìn của Railord Trung Quốc』. Hachiroku. Tôi muốn em nắm bắt điều đó.」
- Lý do: Đại từ Soutetsu: địa chỉ là Hachiroku — JP gọi đích danh 「ハチロク。お前には捉えてほしい」. Theo quy tắc đã sửa, Soutetsu là "tôi" với Hachiroku. Sửa "Anh muốn em" → "Tôi muốn em".

### 1999 — Soutetsu — pronoun
- JP: 「日々姫の目に見えず、僕の耳にも聞こえぬものを、\nお前だけは捉えられる。それはつまりは――」
- TW: 「日日姬所看不到的，我所聽不到的，但你卻能注意到的，也就是說——」
- VN cũ: 「Những thứ Hibiki không nhìn thấy, anh không nghe thấy,\nchỉ có mình em nắm bắt được. Đó chính là——」
- Sửa: 「Những thứ Hibiki không nhìn thấy, tôi không nghe thấy,\nchỉ có mình em nắm bắt được. Đó chính là——」
- Lý do: Đại từ Soutetsu: địa chỉ là Hachiroku — JP 「お前だけは捉えられる」 (chỉ mình em nắm bắt được), "お前" = Hachiroku. Theo quy tắc đã sửa, Soutetsu là "tôi" với Hachiroku. Sửa "anh không nghe thấy" → "tôi không nghe thấy".

### 2013 — Soutetsu — terminology
- JP: 「ああ。まず、稀咲を通じてこの話が御一夜鉄道へと\nやってきたのが、三ヶ月前――八月だった」
- TW: 「是啊。首先，這消息通過稀咲傳到御一夜鐵路，是在三個月前——也就是八月份」
- VN cũ: 「Ừ. Đầu tiên, chuyện này được truyền đến Đường sắt Ohimitera\nthông qua Kisaki là vào ba tháng trước——tháng Tám.」
- Sửa: 「Ừ. Đầu tiên, chuyện này được truyền đến Đường sắt Ohitoyo\nthông qua Kisaki là vào ba tháng trước——tháng Tám.」
- Lý do: Thuật ngữ đã chốt: 御一夜 = "Ohitoyo" (không bao giờ "Ohimitera"/"Ohito"). VN cũ "Đường sắt Ohimitera" sai thuật ngữ. Sửa "Đường sắt Ohitoyo".

### 2035 — Hibiki — terminology
- JP: 「そそ。で。レンタルwifiがレンタル定期券で――\nVPNば、仲国では使えない車内設備を使えるチケット！」
- TW: 「沒錯。所以，隨身Ｗｉ－Ｆｉ就是租借式的定期票，而ＶＰＮ則相當於使用那些在仲國不能使用的車內設施的票啦！」
- VN cũ: 「Đúng đúng. Và wifi thuê chính là vé tháng cho thuê——\nCòn VPN là vé cho phép sử dụng các trang thiết bị trên tàu mà bình thường không dùng được ở Trung Quốc!」
- Sửa: 「Đúng đúng. Và wifi thuê chính là vé định kỳ cho thuê——\nCòn VPN là vé cho phép sử dụng các trang thiết bị trên tàu mà bình thường không dùng được ở Trung Quốc!」
- Lý do: Thuật ngữ đã chốt: 定期券 = "vé định kỳ" (như 1790). VN cũ "vé tháng cho thuê" sai thuật ngữ. Sửa "vé định kỳ cho thuê".

### 2085 — Hachiroku — terminology
- JP: 「それにわたくし、[このからだ,2]整備体でもございますから。\n視覚情報も、どうしても限られてしまいますし」
- TW: 「而且我現在用的是[這副身體,2]整備體，能夠獲取到的視覺訊息也相當有限」
- VN cũ: 「Hơn nữa em đang ở trong \x%l整備体;#00ffc040;thân chính%l;#; mà.\nThông tin thị giác dù sao cũng bị hạn chế đi nhiều ạ.」
- Sửa: 「Hơn nữa em đang ở trong \x%l整備体;#00ffc040;thân bảo trì%l;#; mà.\nThông tin thị giác dù sao cũng bị hạn chế đi nhiều ạ.」
- Lý do: Thuật ngữ đã chốt: 整備体 = "thân bảo trì". VN cũ gloss "thân chính" sai thuật ngữ. Sửa gloss "thân bảo trì" (tag %l giữ nguyên cấu trúc, chỉ đổi gloss).

### 2091 — Soutetsu — terminology
- JP: 「列車に乗るためには、事業者の定期券が必要だ。\n日々姫の定期は、日ノ本の会社のものだから――」
- TW: 「而要乘坐這些列車，就需要相應公司的定期票。日日姬的定期票，是日本的公司的，所以——」
- VN cũ: 「Để lên tàu, cần phải có vé tháng của nhà cung cấp.\nVé tháng của Hibiki là của công ty ở Hinomoto nên——」
- Sửa: 「Để lên tàu, cần phải có vé định kỳ của nhà cung cấp.\nVé định kỳ của Hibiki là của công ty ở Hinomoto nên——」
- Lý do: Thuật ngữ đã chốt: 定期券 = "vé định kỳ" (cả hai chỗ trong dòng: "vé tháng của nhà cung cấp" và "Vé tháng của Hibiki"). Sửa cả hai.

### 2113 — Hachiroku — terminology
- JP: 「パスポオト。身の安全とタブレットの次に大事で、\n肌身離さず携行するもの」
- TW: 「護照，保證了自身和操作板的安全以後，最重要的就是它了。我一定會片刻不離隨身攜帶」
- VN cũ: 「Hộ chiếu. Là thứ quan trọng thứ ba sau sự an toàn của bản thân và \x%lタブレット;#00ffc040;thẻ bảng%l;#;,\nphải luôn mang theo bên người không được rời nửa bước.」
- Sửa: 「Hộ chiếu. Là thứ quan trọng thứ ba sau sự an toàn của bản thân và \x%lタブレット;#00ffc040;máy tính bảng%l;#;,\nphải luôn mang theo bên người không được rời nửa bước.」
- Lý do: Thuật ngữ đã chốt: タブレット = "máy tính bảng" (như 1706). VN cũ gloss "thẻ bảng" sai thuật ngữ. Sửa gloss.

### 2137 — Soutetsu — mistranslation
- JP: 「いや……綺麗な顔だぞ？\n特段拭くべきような何物もついてはいない」
- TW: 「這個……你的臉蛋漂亮而且乾淨啊，哪有什麼需要擦的東西啊」
- VN cũ: 「Không……mặt em sạch mà?\nCó dính gì cần lau đâu.」
- Sửa: 「Không……mặt em vừa xinh vừa sạch mà?\nCó dính gì cần lau đâu.」
- Lý do: JP 「いや……綺麗な顔だぞ？特段拭くべきような何物もついてはいない」— Soutetsu khen Hibiki "khuôn mặt xinh đẹp", rồi mới nói không có gì cần lau; TW nói rõ cả hai nghĩa 「臉蛋漂亮而且乾淨」. VN cũ "mặt em sạch mà?" chỉ giữ nghĩa "sạch", làm mất lời khen "xinh đẹp" (cùng lỗi 綺麗な顔→"mặt sạch" như 1803). Sửa "mặt em vừa xinh vừa sạch mà?".

### 2162 — Soutetsu — pronoun
- JP: 「ゆえに僕は、マスターとして、\nレイルロオド・ハチロクに命じよう」
- TW: 「那就暫且把右田家人的關係放一放，我以司機的身份命令鐵路人偶八六」
- VN cũ: 「Vì vậy, với tư cách là Master,\nanh sẽ ra lệnh cho Railord Hachiroku.」
- Sửa: 「Vì vậy, với tư cách là Master,\ntôi sẽ ra lệnh cho Railord Hachiroku.」
- Lý do: Đại từ Soutetsu: địa chỉ là Hachiroku — JP 「レイルロオド・ハチロクに命じよう」 (ra lệnh cho Railord Hachiroku). Theo quy tắc đã sửa, Soutetsu là "tôi" với Hachiroku. Sửa "anh sẽ ra lệnh" → "tôi sẽ ra lệnh".

### 2173 — Soutetsu — pronoun
- JP: 「では、ハチロクは僕の分を確かめてくれ」
- TW: 「那我的就由八六來檢查吧」
- VN cũ: 「Vậy, Hachiroku kiểm tra phần của anh đi.」
- Sửa: 「Vậy, Hachiroku kiểm tra phần của tôi đi.」
- Lý do: Đại từ Soutetsu: địa chỉ là Hachiroku — JP 「ハチロクは僕の分を確かめてくれ」 (nhờ Hachiroku kiểm tra phần của mình). Theo quy tắc đã sửa, Soutetsu là "tôi" với Hachiroku. Sửa "phần của anh" → "phần của tôi".

### 2207 — Hachiroku — sfx
- JP: 「（ばりっ！　ぼりっ！　ごりっ！　がりっ！）\n……ふぅ。ご馳走様でした。大変おいしうございました」
- TW: 「（喀嚓！喀啦！咕嚕！）……呼。多謝款待。真是太好吃了」
- VN cũ: 「(Rào rào! Rộp rộp! Rào rào! Rộp rộp!)\n……Phù. Cảm ơn vì bữa ăn. Ngon tuyệt vời luôn ạ.」
- Sửa: 「(Rốp rốp! Rộp rộp! Rốp rốp! Rộp rộp!)\n……Phù. Cảm ơn vì bữa ăn. Ngon tuyệt vời luôn ạ.」
- Lý do: JP 「（ばりっ！ぼりっ！ごりっ！がりっ！）」— bốn tiếng nhai/giòn khi Hachiroku ăn than (TW 「喀嚓！喀啦！」). VN cũ "Rào rào! Rộp rộp! Rào rào! Rộp rộp!" — "Rào rào" là tiếng xào xạc/rào rào, không phải tiếng nhai giòn; chỉ "Rộp rộp" đúng. Sửa toàn bộ thành tiếng nhai giòn "(Rốp rốp! Rộp rộp! Rốp rốp! Rộp rộp!)".

### 2407 — Độc thoại — punctuation
- JP: ああ、これこそがハチロクの目だ――\n瀝青炭を燃やすが如き、赤いきらめきが輝いている。
- TW: 啊，這才是八六的眼神應有的樣子啊——如煤炭燃燒般灼熱，閃爍著奪目的紅光。
- VN cũ: 「A, đây mới chính là ánh mắt của Hachiroku——\nLấp lánh sắc đỏ rực rỡ như than bitum đang bùng cháy.」
- Sửa: A, đây mới chính là ánh mắt của Hachiroku——\nLấp lánh sắc đỏ rực rỡ như than bitum đang bùng cháy.
- Lý do: Dòng độc thoại (monologue), JP không có 「」. VN cũ tự thêm 「」 quanh cả dòng, không nhất quán với toàn bộ các dòng độc thoại khác trong file (đều không có 「」) và làm độc thoại trông như thoại. Bỏ 「」.

## §3. Sweep っ-gasp kiểm chứng

- Đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`: **0 mục cho file này** (sweep có mục cho các file Chikuni khác: 仲国02/04/05/07 — sweep đã liệt kê route này, không phải bỏ sót file).
- 2 fix gasp trong file này (1776, 1803 — はうっ→"HaƯ") đều là sweep bỏ sót, theo phán quyết 20/11: っ trên từ-âm はう là gasp → thêm Ư (tiền lệ 仲国05 2254 "haƯ").
- Các っ cuối dòng còn lại đã rà soát bằng script và giữ nguyên: あらっ→"Ôi." (1769), えっ！？→"Hả!?" (1772, 1774, 1799), え、いえっ→"Hả, dạ không!?" (1729), はいっ→"Vâng!" (1890), ちょっ→"Khoan!?" (1829), むっ→"hửm" (1938) — っ nhấn mạnh trên thán từ, không phải gasp; あっ cuối 1803 → "A!?" giữ nguyên (cảm thán ngắn).
- Không còn っ thô trong VN (2 lần khớp ッ đều là chữ ッ trong thuật ngữ JP タブレット được giữ nguyên trong tag %l, không phải lỗi).

## §4. Các dòng đã kiểm tra kỹ nhưng giữ nguyên (không tính sai)

- 1677 「誤作動は――確かに恐ろしく思います」→ "Hoạt động sai ——quả thật là rất đáng sợ ạ." — "Hoạt động sai" hơi cứng nhưng diễn đúng nghĩa trục trặc/malfunction; TW cũng diễn giải theo hướng can nhiễu gây trục trặc. Giữ nguyên (ghi chú biên, không tính sai).
- 1828 + 2089 橙汁 → "Trừng trấp" — giữ nguyên: đây là cách đọc Hán-Việt có chủ ý của dạng chữ Hán 橙汁, nhất quán cả hai dòng trong file; riêng 2089 câu đùa chính là về dạng chữ viết ("Nước cam mà gọi là 『Trừng trấp』, thú vị ghê nhỉ~"). Nếu Hieu muốn "nước cam" thì đổi ở đợt thống nhất — xem §6.
- 1377 Hachiroku gọi Hibiki "chị" ("Em kiểm tra giúp chị được không?") — giữ nguyên; file 06 có các dòng Hachiroku→Hibiki dùng "cô" đang chờ Hieu quyết ở đợt thống nhất — xem §6.
- 1964/1965/2165 いただきます → "Mời mọi người" — thành ngữ quy ước trong file, nhất quán cả ba dòng. Giữ nguyên.
- 2185 「共感ならば、仲国のレイルロオドと通じあえる」→ "nếu là cộng cảm, thì có lẽ em sẽ giao tiếp được với các Railord của Trung Quốc đấy" — chủ ngữ là Hachiroku (cô ấy là người dùng 共感 để giao tiếp); "em" đúng. Giữ nguyên.
- 1400/1704/1838/1846/2110 Soutetsu dùng "anh" khi nói với Hibiki hoặc cả nhóm (có Hibiki) — đúng quy tắc. Giữ nguyên.
- 2011 運転体 → "thân lái" — không tính sai (xem §6): thuật ngữ chưa chốt; dạng chủ đạo toàn dự án là "kíp lái", nhưng "thân lái" diễn đúng nghĩa, để đợt thống nhất quyết.

## §5. Khối TOML (đã parse-kiểm chứng: 22 khóa, 0 sai lệch)

```toml
[script]
"1329" = "……Tôi định bắt chuyện với hai người,\\nnhưng tiếc là chẳng có phản ứng gì."
"1356" = "「……Xin lỗi các em. Cảm ơn các em.\\nAnh cũng sẽ cố gắng để bù đắp cho Hibiki, cho Hachiroku.」"
"1403" = "「……Sự ồn ào trước khi lên máy bay, giờ cứ như chưa từng xảy ra vậy.」"
"1706" = "「Có lẽ là vậy ạ. Nếu là xác thực cá nhân của Railord,\\nthì \\x%lタブレット;#00ffc040;máy tính bảng%l;#; này mới là thứ chắc chắn tuyệt đối ạ.」"
"1744" = "「Ra là vậy. Cảm ơn em đã chỉ cho tôi.」"
"1776" = "「HaƯ!? Em, dạ, chuyện đó.」"
"1790" = "「A, vậy là để đi tuyến Internet ở Trung Quốc,\\nthì cần phải có vé định kỳ của nhà cung cấp ở Trung Quốc đúng không ạ?」"
"1803" = "「HaƯ!? M, mặt xinh đẹp……em vui lắm.\\nA!? Không phải, không phải ý đó——a!」"
"1834" = "「Ưm……như vậy——ưm……rồi!\\nĐây! Đây là mẫu nè!!」"
"1888" = "「Em biết rồi! Mà này, anh hai, mọi người cũng chuẩn bị đi!\\nChúng ta vẫn chưa điền thẻ nhập cảnh nữa đó!!」"
"1943" = "「Thứ mà chúng ta không thể nắm bắt được, 『Tuyến đường sắt Trung Quốc\\nqua góc nhìn của Railord Trung Quốc』. Hachiroku. Tôi muốn em nắm bắt điều đó.」"
"1999" = "「Những thứ Hibiki không nhìn thấy, tôi không nghe thấy,\\nchỉ có mình em nắm bắt được. Đó chính là——」"
"2013" = "「Ừ. Đầu tiên, chuyện này được truyền đến Đường sắt Ohitoyo\\nthông qua Kisaki là vào ba tháng trước——tháng Tám.」"
"2035" = "「Đúng đúng. Và wifi thuê chính là vé định kỳ cho thuê——\\nCòn VPN là vé cho phép sử dụng các trang thiết bị trên tàu mà bình thường không dùng được ở Trung Quốc!」"
"2085" = "「Hơn nữa em đang ở trong \\x%l整備体;#00ffc040;thân bảo trì%l;#; mà.\\nThông tin thị giác dù sao cũng bị hạn chế đi nhiều ạ.」"
"2091" = "「Để lên tàu, cần phải có vé định kỳ của nhà cung cấp.\\nVé định kỳ của Hibiki là của công ty ở Hinomoto nên——」"
"2113" = "「Hộ chiếu. Là thứ quan trọng thứ ba sau sự an toàn của bản thân và \\x%lタブレット;#00ffc040;máy tính bảng%l;#;,\\nphải luôn mang theo bên người không được rời nửa bước.」"
"2137" = "「Không……mặt em vừa xinh vừa sạch mà?\\nCó dính gì cần lau đâu.」"
"2162" = "「Vì vậy, với tư cách là Master,\\ntôi sẽ ra lệnh cho Railord Hachiroku.」"
"2173" = "「Vậy, Hachiroku kiểm tra phần của tôi đi.」"
"2207" = "「(Rốp rốp! Rộp rộp! Rốp rốp! Rộp rộp!)\\n……Phù. Cảm ơn vì bữa ăn. Ngon tuyệt vời luôn ạ.」"
"2407" = "A, đây mới chính là ánh mắt của Hachiroku——\\nLấp lánh sắc đỏ rực rỡ như than bitum đang bùng cháy."
```

## §6. Lượt soát 2 + Chờ Hieu

- Lượt soát 2: 22/22 fix đọc lại đối chiếu JP — 22 giữ nguyên, 0 bỏ, 0 sửa.
- Chờ Hieu (không tự quyết):
  1. 日ノ本 "Hinomoto" vs "Hinamoto" — toàn file dùng "Hinomoto" (nhất quán); câu hỏi đang chờ từ file 稀咲. Hieu chốt một dạng cho toàn dự án.
  2. Key 2011 — 運転体: VN hiện tại "thân lái"; dạng chủ đạo toàn dự án là "kíp lái" (đa số các file), ngoài ra còn "thân chính"/"cơ thể lái"/"cơ thể vận hành" rải rác. Chưa có thuật ngữ đã chốt cho 運転体 (chỉ có 運転ボディ = "thân vận hành"). Hieu chốt một dạng cho đợt thống nhất.
  3. Hachiroku→Hibiki: file này dùng "chị" (1377), file 06 dùng "cô" ở 3 dòng (1954, 2225, 2393, đang chờ đợt thống nhất). Hieu chốt một dạng.
  4. 橙汁 (1828, 2089): giữ "Trừng trấp" (Hán-Việt, có chủ ý) hay đổi thành "nước cam" cho dễ đọc? Hieu quyết.

## Kết bài

File 仲国01_副丘→北琴 đã audit xong toàn bộ 349 dòng: 22 dòng sai (6,3%) — 6 đại từ (Soutetsu "anh"→"tôi" với Hachiroku, trong đó 1356 là số nhiều "các em"), 7 thuật ngữ (Ohitoyo 1, タブレット→"máy tính bảng" 2, 定期券→"vé định kỳ" 3, 整備体→"thân bảo trì" 1), 5 dịch sai, 2 gasp (はうっ→"HaƯ", sweep bỏ sót cả hai), 1 SFX (tiếng nhai than), 1 dấu câu (bỏ 「」 thừa ở độc thoại 2407). Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 22 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 22/22, 0 bỏ, 0 sửa. Chờ Hieu: 日ノ本 "Hinomoto" vs "Hinamoto"; 運転体 2011 ("thân lái" vs "kíp lái"); Hachiroku→Hibiki "chị" vs "cô"; 橙汁 "Trừng trấp" vs "nước cam".
