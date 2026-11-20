# Audit — 稀咲01_金と人.txt.toml

- File: `稀咲01_金と人.txt.toml` — route 06_Kisaki, 379 dòng script (93 thoại Kisaki, 84 thoại Soutetsu, 30 thoại Hibiki, 29 thoại Mototada, 1 thoại Uragami, 142 độc thoại).
- Nội dung: Mototada đến chi nhánh ngân hàng của Kisaki; Soutetsu, Kisaki và Hibiki tranh luận về tiền bạc/niềm tin, về việc mời gọi nhà máy Aircra so với phục hưng Ohito bằng suối nước nóng–shochu–đường sắt, về nghiệp vụ đối chiếu sổ sách (cửu khứ pháp, vụ lệch 820 yên trả thành 280 yên, thiếu 81.180 yên), rồi ăn pizza ở phòng Kisaki; kết bằng lời hứa cạnh tranh công bằng giữa hai phương án phục hưng.
- **Kết quả: 178/379 dòng sai (47,0%)** — đọc đủ từng dòng đối chiếu JP + TW. Đây là file có tỉ lệ sai cao nhất từ trước đến nay trong đợt audit (trước đó cao nhất là Hibiki 03 với 86,2% — file này đứng thứ hai toàn dự án).

## §1. Kiểm tra cấu trúc

- **Chuỗi xoay lớn: 173 dòng lệch vị trí** (trong đó 165 dòng lấy lại được bản dịch đúng đang nằm ở một key khác trong cùng file, 8 dòng dịch mới vì bản dịch đúng không còn trong file — xem §3). Không có dòng mồ côi (mọi VN trong file đều tìm được đúng JP của nó, trừ 10 giá trị ngắn thừa bị loại và 3 dòng chỉ sai đại từ), không nhiễm chéo file khác, không dòng chưa dịch, không trùng khóa.
- CSV3 1 set duy nhất (379 dòng, 0 khóa trùng, 0 ô VN trống); VN khớp TOML tuyệt đối 379/379 (0 lệch thực chất — 246 dòng chỉ khác ở chỗ TOML-2 làm phẳng dấu \n thành khoảng trắng, đã biết, không phải lỗi; 2 dòng 1992/2337 TOML giữ nguyên dấu cách thay cho \n cũng cùng một hiện tượng). `[selections]` rỗng. Thẻ `%l`: 3 dòng VN có thẻ エアクラ (1232, 2291, 2334) — đều là thuật ngữ trong thẻ, không phải chữ Nhật rò; 0 thẻ sai định dạng trong VN; 4 chỗ lệch số lượng thẻ JP↔VN đều do chuỗi xoay gây ra và được sửa sạch khi trả bản dịch về đúng key (1775 nhận lại thẻ ở 2291, 2325 nhận lại thẻ ở 2334).
- TOML md5 `9701d0e61e823e0ed70f50888d83dc7a`; không có bản sao file này (không thuộc 11 nhóm trùng — đã kiểm tra md5 toàn bộ 227 file).
- Cơ sở tổng cộng đã kiểm chứng với ROUTE-AUDIT.md: **108 file / 5.009 dòng sai** (khớp với con số parent giao, không cần rebase).
- Soutetsu "tôi" với Kisaki đúng toàn file (Soutetsu xưng "tôi", gọi Kisaki "em" — nhất quán, phù hợp hướng thống nhất "cô"→"em" đang chờ). Kisaki tự xưng "em" với Soutetsu — 3 dòng sai "chị" (1612, 1757, 1805) đã sửa; các dòng "chị" còn lại đều là Hibiki gọi Kisaki hoặc Kisaki nói với Hibiki, đúng. Không có dòng Soutetsu "anh" sai đối tượng nào trong file.
- Thuật ngữ: Ohito dùng "Ohito" (không dùng "御一夜" dạng cũ), エアクラ="Aircra" đúng, 日ノ本="Hinomoto" (1579, 1987 — đang chờ Hieu chốt "Hinomoto" vs "Hinamoto", xem §6). Không có Ohitoyo/Teitetsu/Migita/Yunoi/KiHa/宮司 trong file nên không có gì khác chờ đợt thống nhất. "Chuyện đó" ở 1705 và "Hừ." ở 1852 là hai giá trị thừa bị loại (xem §6).

## §2. Danh sách sửa (178 dòng)

Phân loại: lệch dòng 173 (165 lấy lại bản dịch đúng trong file + 8 dịch mới: 1637, 1639, 1672, 1700, 1833, 1896, 1983, 1992), đại từ 3 (1612, 1757, 1805 — Kisaki "chị"→"em" với Soutetsu), gasp 2 (1618, 2063 — JP 「っ！」 cả dòng, VN cũ là câu độc thoại lệch dòng).

### 1223 — Độc thoại — lệch dòng
- JP: ……稀咲を訪ねてきた筈が、僕から熱心に話を聞いて。
- TW: ……他來這裡應該是為了找稀咲，卻熱情地聽起我的話來。
- VN cũ: Ngay sau khi tôi kể lại toàn bộ câu chuyện đã nói với Kisaki,\nHoushou Mototada thẳng thừng tuyên bố.
- Sửa: ……Đáng lẽ đến tìm Kisaki, nhưng ông ấy lại chăm chú lắng nghe tôi nói.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2341 (JP: 稀咲と話したひと通り、そのままを伝え終えればすぐさま、\n宝生元忠はズバリと言い切る。); fix là bản dịch đúng đang nằm ở key 1234.

### 1234 — Mototada — lệch dòng
- JP: 「――ふむ。\n一つ、大きな誤解がある」
- TW: 「——嗯。其實你有一個很大的誤解」
- VN cũ: ……Đáng lẽ đến tìm Kisaki, nhưng ông ấy lại chăm chú lắng nghe tôi nói.
- Sửa: 「――Hừm.\nCó một sự hiểu lầm lớn ở đây.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1223 (JP: ……稀咲を訪ねてきた筈が、僕から熱心に話を聞いて。); fix là bản dịch đúng đang nằm ở key 1634.

### 1245 — Mototada — lệch dòng
- JP: 「……言ったとおりだ。\n安くて旨い酒ならば、私も喜んで飲む」
- TW: 「……你說得沒錯。如果有便宜又好喝的酒，我也很樂意嚐嚐」
- VN cũ: Vẫn giữ nguyên ánh mắt sắc bén,\nbác Mototada quay sang Kisaki.
- Sửa: 「……Đúng như ta đã nói.\nNếu là loại rượu vừa rẻ vừa ngon, ta cũng rất sẵn lòng thưởng thức.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2210 (JP: 鋭い目つきを緩めぬままに、\n元忠氏は稀咲へと向き直る。); fix là bản dịch đúng đang nằm ở key 2297.

### 1256 — Kisaki — lệch dòng
- JP: 「……父と、頭取、どっちの立場で」
- TW: 「……您是以什麼立場來說這句話的？是父親，還是行長？」
- VN cũ: 「Là mệnh lệnh công việc. Giám đốc chi nhánh.」
- Sửa: 「……Bố đang nói với tư cách là Bố, hay là Chủ tịch vậy?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1990 (JP: 「業務命令だ。支店長」); fix là bản dịch đúng đang nằm ở key 2273.

### 1260 — Kisaki — lệch dòng
- JP: 「……ひとまずは……とにかく、数字を出させて欲しい。\nクマ焼酎というブランドを逸失してしまった場合――」
- TW: 「……首先呢……希望你能給我一個數字。用數字告訴我，失去隈燒酒這個品牌會——」
- VN cũ: （Cộc cộc）
- Sửa: 「……Trước mắt thì……tóm lại, hãy để em đưa ra những con số cụ thể.\nTrong trường hợp đánh mất thương hiệu shochu Kuma――」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2631 (JP: （ゴンッ、ゴンッ）); fix là bản dịch đúng đang nằm ở key 2506.

### 1501 — Kisaki — lệch dòng
- JP: 「済まない。父が。\nあれは……ああいう人なんだ」
- TW: 「不好意思啊。爸爸他……就是那樣的人」
- VN cũ: 「A……ừm……\nKhông sao đâu, nhỉ?」
- Sửa: 「Xin lỗi nhé. Bố em.\nÔng ấy……là người như vậy đấy.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1647 (JP: 「あ……あの……\n別に、ねぇ？」); fix là bản dịch đúng đang nằm ở key 2162.

### 1503 — Soutetsu — lệch dòng
- JP: 「すまない態度を見せてしまった。言葉の真意もわからず、\n金が大事と聞いただけで、君を守銭奴のように誤解した」
- TW: 「不好意思，剛才我太膚淺了。我沒有理解你真正的意思，聽你說金錢很重要，就把你誤解成了守財奴」
- VN cũ: 「Trái lại, em phản đối việc chỉ biết khư khư tích trữ tiền bạc đấy?\nBởi vì em nghĩ tiền chỉ thực sự là tiền khi nó được lưu thông đúng cách.」
- Sửa: 「Xin lỗi vì thái độ lúc nãy của anh. Chưa hiểu rõ ý nghĩa thực sự trong lời nói của em,\nchỉ nghe nói tiền quan trọng, anh đã hiểu lầm em là một kẻ hám tiền.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1573 (JP: 「お金をただ貯めこむことにはむしろ否定的だよ？\nお金は、正しく流通させてこそのお金だと思うから」); fix là bản dịch đúng đang nằm ở key 2571.

### 1539 — Hibiki — lệch dòng
- JP: 「でも、だけど――同じ。本物の一万円札も、\n綺麗に印刷されてはいるけど……やっぱり、紙切れ」
- TW: 「但是——其實它們是一樣的。真正的一萬日元，就算印刷得再漂亮……也只是一張紙」
- VN cũ: 「Một mảnh giấy vụn có thể được lưu thông như một loại tiền tệ, như một vật thay thế cho sức lao động――\nđó là vì có niềm tin đặt vào nó đúng không?」
- Sửa: 「Nhưng, thế nhưng――cũng giống nhau thôi. Tờ một vạn yên thật,\ndù được in ấn đẹp đẽ……thì rốt cuộc cũng chỉ là một mảnh giấy.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1809 (JP: 「ただの紙切れが通貨として、労働力の代替物として、\n通用するのは――そこに信頼があるからだよね？」); fix là bản dịch đúng đang nằm ở key 2379.

### 1540 — Soutetsu — lệch dòng
- JP: 「ですが、僕らには水を汚すメリットは無い。\n反面、すぐに見えずとも、長期的なリスクは大きい」
- TW: 「但是汙染水資源對我們一點好處都沒有。反過來說，就算短期內沒有問題，潛在的長期風險也很大」
- VN cũ: 「Lợi ích thì có đấy. Nếu thành phố Ohito suy tàn,\nthì shochu Kuma, chèo thuyền trên sông Kuma hay đường sắt cũng sẽ lụi bại theo.」
- Sửa: 「Tuy nhiên, việc làm ô nhiễm nguồn nước không mang lại lợi ích gì cho chúng cháu.\nNgược lại, dù không thấy ngay trước mắt, nhưng rủi ro về lâu dài là rất lớn.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1704 (JP: 「メリットならある。御一夜市が衰退してしまうのなら、\nクマ焼酎もクマ川下りも鉄道も衰退していく」); fix là bản dịch đúng đang nằm ở key 2302.

### 1543 — Hibiki — lệch dòng
- JP: 「けど、酒造はそれを気にします。\nそこを譲れば、なにか、大事なものが失われます」
- TW: 「但是釀酒廠會在意水資源問題。如果在這一點上我們讓步了，我們就遺失了重要的東西」
- VN cũ: Thứ bị đánh mất.\nNiềm tự hào, truyền thống――và sự tự tin được xây đắp từ những điều đó.
- Sửa: 「Nhưng, xưởng nấu rượu thì có quan tâm.\nNếu nhượng bộ điểm đó, một thứ gì đó rất quan trọng sẽ bị đánh mất.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2322 (JP: 失われるもの。\n誇り、伝統――そうしたものが支える自信。); fix là bản dịch đúng đang nằm ở key 2157.

### 1549 — Mototada — lệch dòng
- JP: 「しかしだ、御一夜は困窮している。\n安酒であれ、それがなければ渇ききるほどに」
- TW: 「但現在御一夜已經陷入窘境。哪怕是便宜酒，也比渴死要好」
- VN cũ: （Ồ.）
- Sửa: 「Nhưng mà, Ohito đang khốn khó.\nDù là rượu rẻ tiền, nếu không có nó thì sẽ chết khát mất.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2627 (JP: （おお）); fix là bản dịch đúng đang nằm ở key 2298.

### 1551 — Mototada — lệch dòng
- JP: 「それなら全てが、過去の遺物だ。\n御一夜の再生には繋がらんよ」
- TW: 「但這些東西都只是過去的遺產。和御一夜的復興並沒有聯繫」
- VN cũ: 「Nếu chỉ lấy ra từng cái một, thì có thể là vậy.\nNhưng, nếu kết hợp chúng lại, chúng ta có thể tạo ra những giá trị hoàn toàn mới.」
- Sửa: 「Nếu vậy thì tất cả đều là di vật của quá khứ.\nKhông thể dẫn đến sự phục hưng của Ohito được đâu.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1723 (JP: 「一個一個を取り上げるなら、そうであるかもしれません。\nが。連携させれば、まったく新しい価値を創出できます」); fix là bản dịch đúng đang nằm ở key 2195.

### 1557 — Kisaki — lệch dòng
- JP: 「支店長として、\nそのご意見には異議を唱えさせていただきます」
- TW: 「作為支行行長，我反對這個意見」
- VN cũ: Khoảnh khắc bị áp đảo bởi những lời lẽ mạnh mẽ đó,\nđã bị phá vỡ bởi một giọng nói lạnh lùng xen vào.
- Sửa: 「Với tư cách là Giám đốc chi nhánh,\ncháu xin phép được phản đối ý kiến đó.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2161 (JP: 強い言葉にやや気圧された一瞬を、\n涼しい声が割り込み、壊す。); fix là bản dịch đúng đang nằm ở key 1937.

### 1559 — Soutetsu — lệch dòng
- JP: 「謝られるようなこととは思わん。\n実際、良い話し合いをさせてもらった」
- TW: 「你不需要為此道歉。我們之間的交流確實很有意義」
- VN cũ: 「Không, tốt gì chứ.」
- Sửa: 「Anh không nghĩ em cần phải xin lỗi đâu.\nThực tế thì, chúng ta đã có một cuộc thảo luận rất tốt mà.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là giá trị ngắn thừa, không phải bản dịch của dòng nào trong file; fix là bản dịch đúng đang nằm ở key 1647.

### 1566 — Mototada — lệch dòng
- JP: 「これから用意するつもりかね？\n温泉と焼酎と、それに鉄道を加えて」
- TW: 「你是想說從現在開始著手準備嗎？也就是溫泉、燒酒再加上鐵路」
- VN cũ: 「Đúng như bác nói.\nĐó là định hướng cơ bản của chúng cháu.」
- Sửa: 「Cháu định từ giờ sẽ chuẩn bị sao?\nBằng cách kết hợp suối nước nóng, shochu và cả đường sắt nữa.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1852 (JP: 「仰るとおり。\nその線を基本と考えています」); fix là bản dịch đúng đang nằm ở key 2053.

### 1573 — Kisaki — lệch dòng
- JP: 「お金をただ貯めこむことにはむしろ否定的だよ？\nお金は、正しく流通させてこそのお金だと思うから」
- TW: 「倒不如說，我很反對一味存錢呀。金錢就要正確流通起來才成其為金錢」
- VN cũ: Nếu thay chữ tiền bằng chữ niềm tin, tôi cảm thấy mình có thể hiểu sâu sắc hơn\nvề giá trị quan của Houshou Kisaki――à, khoan đã.
- Sửa: 「Trái lại, em phản đối việc chỉ biết khư khư tích trữ tiền bạc đấy?\nBởi vì em nghĩ tiền chỉ thực sự là tiền khi nó được lưu thông đúng cách.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2288 (JP: お金を信頼と言い換えたなら、宝生稀咲の価値観を、\nより深く理解できそうにも――ああ、いや。); fix là bản dịch đúng đang nằm ở key 1503.

### 1579 — Kisaki — lệch dòng
- JP: 「この内の片方は日ノ本全国各地で使え、\nもう片方は誰からも、通貨として扱ってもらえない」
- TW: 「其中一張在日本全國各地都能使用，而另一張沒有任何一個人會把它當作貨幣」
- VN cũ: 「Chuyện đó……chẳng phải là đương nhiên sao.」
- Sửa: 「Một tờ có thể sử dụng ở khắp mọi nơi trên toàn quốc Hinomoto,\ncòn một tờ thì không ai coi nó là tiền tệ cả.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1985 (JP: 「そんなの……当たり前じゃないですか」); fix là bản dịch đúng đang nằm ở key 1629.

### 1584 — Soutetsu — lệch dòng
- JP: 「なるほど――それが、\n宝生稀咲にとっての、『お金の価値』か」
- TW: 「原來如此——對你而言，這就是“金錢的價值”啊」
- VN cũ: Nếu là vậy thì tôi hoàn toàn có thể đồng cảm――\nNghĩ đến đây, tôi chợt thấy xấu hổ về bản thân lúc nãy.
- Sửa: 「Ra là vậy――đó chính là,\n『giá trị của đồng tiền』 đối với Houshou Kisaki sao.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2571 (JP: そういうことなら共感できる――\n思った瞬間、さっきの自分が恥ずかしくなる。); fix là bản dịch đúng đang nằm ở key 2036.

### 1585 — Soutetsu — lệch dòng
- JP: 「お金は……なるほど。信頼か」
- TW: 「原來如此……金錢就是信任啊」
- VN cũ: 「Hả? Cái gì mà ra vậy?」
- Sửa: 「Tiền là……ra vậy. Niềm tin sao.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1633 (JP: 「え？　なにが、なるほど？」); fix là bản dịch đúng đang nằm ở key 2023.

### 1586 — Kisaki — lệch dòng
- JP: 「なるほど。\nでは、まずはそこから視察させてもらうとするかな」
- TW: 「原來如此。那麼，就讓我先去實地考察一下吧」
- VN cũ: 「Đã rõ. ――Hửm?」
- Sửa: 「Ra là vậy.\nThế thì, chắc em phải bắt đầu khảo sát từ đó thôi nhỉ.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là giá trị ngắn thừa, không phải bản dịch của dòng nào trong file; fix là bản dịch đúng đang nằm ở key 1955.

### 1604 — Mototada — lệch dòng
- JP: 「異議とは？」
- TW: 「反對？」
- VN cũ: 「Việc thành phố Ohito bị chia rẽ là điều không nên.\nChúng ta cần cố gắng đạt được sự đồng thuận từ càng nhiều người càng tốt――」
- Sửa: 「Phản đối?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1785 (JP: 「御一夜市が二分されるのは好ましくありません。\nできるかぎり多くからの同意を得られるように――」); fix là bản dịch đúng đang nằm ở key 2511.

### 1612 — Kisaki — đại từ
- JP: 「や。これはボクの言い方が良くなかったね」
- TW: 「呀，看來是我的表達方式不太對」
- VN cũ: 「Ây da. Là do cách nói của chị không tốt rồi.」
- Sửa: 「Ây da. Là do cách nói của em không tốt rồi.」
- Lý do: Đại từ Kisaki: Kisaki trả lời Soutetsu (1611 Soutetsu hỏi "pizza có dễ ăn không?"), tự xưng "em" theo quy tắc Kisaki "em" với Soutetsu; VN cũ "chị" sai (chỉ đúng khi nói với Hibiki). Nội dung câu giữ nguyên, chỉ đổi đại từ.

### 1614 — Hibiki — lệch dòng
- JP: 「ええと――あ！　そう、\n稀咲先輩に話があって来たはずなのに――えっ！？」
- TW: 「呃——啊！他來這裡明明是有事找你的，但是——哎！？」
- VN cũ: Bắt đầu từ cổ, giống như có ai đó đang phun sơn vậy.\nKhuôn mặt Kisaki dần dần, thấy rõ là đang đỏ bừng lên.
- Sửa: 「À thì――a! Đúng rồi,\nRõ ràng bác ấy đến tìm tiền bối Kisaki để nói chuyện mà――hả!?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2530 (JP: 首から順に、まるでスプレーを吹き上げるように。\n稀咲の顔が、じわじわ、目に見えて赤くなる。); fix là bản dịch đúng đang nằm ở key 1886.

### 1618 — Soutetsu — gasp
- JP: 「っ！」
- TW: 「呃！」
- VN cũ: Tôi không thể nghĩ ra lời phản bác ngay lập tức.\nĐó quả thực là――một sự thật tàn khốc.
- Sửa: 「Ư!」
- Lý do: Gasp: JP 「っ！」 cả dòng chỉ là một tiếng nấc/gasp, VN cũ là câu độc thoại đầy đủ — đó là bản dịch của 2157, đã chuyển về đúng chỗ. Fix "Ư!" theo quy tắc っ→Ư. Sweep đã cờ dòng này (already-rendered) nhưng thực chất là lệch dòng.

### 1620 — Mototada — lệch dòng
- JP: 「ははぁ、つまりはこう言いたいわけか。\n『工場誘致より優れた御一夜再生計画がある』と」
- TW: 「哈哈，你是想說“你有比讓工廠落戶更優秀的御一夜振興方案”嗎」
- VN cũ: 「Đúng hơn là――\nCháu cảm thấy việc mời gọi nhà máy không phải là một kế hoạch phục hưng xuất sắc cho lắm.」
- Sửa: 「Haha, vậy là cháu muốn nói điều này sao.\n『Cháu có một kế hoạch phục hưng Ohito xuất sắc hơn việc mời gọi nhà máy』.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1783 (JP: 「と、いうよりむしろ――\n工場誘致は、さほど優れた再生計画ではない気がします」); fix là bản dịch đúng đang nằm ở key 1775.

### 1623 — Mototada — lệch dòng
- JP: 「と――時間だ。面白い話ができた。感謝する」
- TW: 「哎——時間不早了。謝謝你跟我聊了這麼有意思的話」
- VN cũ: （Rầm）
- Sửa: 「Ồ――đến giờ rồi. Một cuộc nói chuyện thú vị. Cảm ơn nhé.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2628 (JP: （バタンっ）); fix là bản dịch đúng đang nằm ở key 2354.

### 1624 — Hibiki — lệch dòng
- JP: 「えっ！？」
- TW: 「哎！？」
- VN cũ: Hibiki tròn mắt ngạc nhiên.\nTrái ngược với con bé, vẻ nhẹ nhõm bắt đầu lan tỏa trên khuôn mặt Kisaki.
- Sửa: 「Hả!?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2391 (JP: 驚きに、日々姫の目が丸くなる。\n稀咲の顔には正反対に、安堵の色が滲み始める。); fix là bản dịch đúng đang nằm ở key 1826.

### 1629 — Hibiki — lệch dòng
- JP: 「え？」
- TW: 「哎？」
- VN cũ: 「Một tờ có thể sử dụng ở khắp mọi nơi trên toàn quốc Hinomoto,\ncòn một tờ thì không ai coi nó là tiền tệ cả.」
- Sửa: 「Hả?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1579 (JP: 「この内の片方は日ノ本全国各地で使え、\nもう片方は誰からも、通貨として扱ってもらえない」); fix là bản dịch đúng đang nằm ở key 1987.

### 1630 — Hibiki — lệch dòng
- JP: 「え？　あ、なーんも！\nなーん、んんっ、何でもないです。大丈夫」
- TW: 「哎？啊，沒事！沒事，嗯，什麼事都沒有。沒關係」
- VN cũ: Một nụ cười gượng gạo lộ liễu.\nVà rồi Hibiki liên tục thốt ra những lời lấp liếm.
- Sửa: 「Dạ? À, không có gì đâu!\nKhông, ưm, không có gì đâu ạ. Em ổn.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2261 (JP: あからさまなほどの作り笑い。\nそして日々姫は、ごまかすような言葉を重ねる。); fix là bản dịch đúng đang nằm ở key 1768.

### 1633 — Hibiki — lệch dòng
- JP: 「え？　なにが、なるほど？」
- TW: 「哎？怎麼就明白了？」
- VN cũ: 「Nếu mọi người không tin tưởng vào tiền,\nthì tiền giấy cũng chỉ là những mảnh giấy vụn mà thôi.」
- Sửa: 「Hả? Cái gì mà ra vậy?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1711 (JP: 「みながお金を信頼せねば、\n紙幣など、ただの紙切れになってしまうということだ」); fix là bản dịch đúng đang nằm ở key 1585.

### 1634 — Mototada — lệch dòng
- JP: 「ほう？」
- TW: 「哦？」
- VN cũ: 「――Hừm.\nCó một sự hiểu lầm lớn ở đây.」
- Sửa: 「Ồ?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1234 (JP: 「――ふむ。\n一つ、大きな誤解がある」); fix là bản dịch đúng đang nằm ở key 1939.

### 1636 — Mototada — lệch dòng
- JP: 「ほう、他のアイディアがあるというなら、面白い」
- TW: 「哦？我很感興趣，你還有什麼別的方案」
- VN cũ: Bác Mototada cười nhếch mép, đưa tay vuốt cằm.
- Sửa: 「Ồ, nếu cháu có ý tưởng khác thì thú vị đấy.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2211 (JP: ニヤリと笑い、元忠氏の手がその顎を撫ぜる。); fix là bản dịch đúng đang nằm ở key 2046.

### 1637 — Mototada — lệch dòng
- JP: 「ふん」
- TW: 「哼」
- VN cũ: Một tiếng thở hắt ra từ mũi.
- Sửa: 「Hừm.」
- Lý do: Dạng câu: JP 「ふん」 là lời thoại của Mototada (tiếng hừ qua mũi), VN cũ diễn thành câu trần thuật "Một tiếng thở hắt ra từ mũi." — câu trần thuật đó là bản dịch đúng của 2192, đã chuyển về đúng chỗ. Fix đưa về dạng thoại "Hừm.". Ghi chú: "Hừ." ở 1852 là giá trị thừa bị loại (xem §6).

### 1639 — Soutetsu — lệch dòng
- JP: 「むぅ……そうか」
- TW: 「唔……是嗎」
- VN cũ: Vui mừng vì đã tìm được tiếng nói chung,\ntôi có hơi vội vàng quá.
- Sửa: 「Ừm……ra vậy à.」
- Lý do: Dịch mới: JP "むぅ……そうか" (Soutetsu trầm ngâm "Ừm… ra vậy"), VN cũ là độc thoại "Vui mừng vì đã tìm được tiếng nói chung…" — đó là bản dịch của 2282, đã chuyển về đúng chỗ. Không có bản dịch đúng nào khác trong file cho dòng này.

### 1640 — Hibiki — lệch dòng
- JP: 「あ――」
- TW: 「啊——」
- VN cũ: Chỉ với vài lời.\nĐã đủ làm lung lay tận gốc rễ những lập luận của chúng tôi.
- Sửa: 「A――」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2180 (JP: ほんの数語。\nただそれだけで、論拠をガタガタに揺すられる。); fix là bản dịch đúng đang nằm ở key 1994.

### 1644 — Kisaki — lệch dòng
- JP: 「あー……そうか。なるほど。なるほど――\nそれは、譲れないところだ、ね」
- TW: 「啊……是啊。原來如此。原來如此——這確實不能讓步呢」
- VN cũ: 「Đúng vậy. Dù chỉ nhượng bộ một bước――\ncũng sẽ phá hủy đi niềm tin mà shochu Kuma đã dày công gây dựng bấy lâu nay.」
- Sửa: 「A……ra vậy. Ra là thế. Ra là thế――\nĐó là điều không thể nhượng bộ, nhỉ.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1867 (JP: 「そうだ。ただの一歩でも譲っては――\nクマ焼酎が今まで積み重ねてきた信頼を破壊してしまう」); fix là bản dịch đúng đang nằm ở key 2480.

### 1647 — Hibiki — lệch dòng
- JP: 「あ……あの……\n別に、ねぇ？」
- TW: 「啊……那個……沒關係的，是吧？」
- VN cũ: 「Anh không nghĩ em cần phải xin lỗi đâu.\nThực tế thì, chúng ta đã có một cuộc thảo luận rất tốt mà.」
- Sửa: 「A……ừm……\nKhông sao đâu, nhỉ?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1559 (JP: 「謝られるようなこととは思わん。\n実際、良い話し合いをさせてもらった」); fix là bản dịch đúng đang nằm ở key 1501.

### 1648 — Kisaki — lệch dòng
- JP: 「あ」
- TW: 「啊」
- VN cũ: Vẻ mặt như thể bị đánh trúng điểm yếu.
- Sửa: 「A.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2274 (JP: 虚を突かれたと、そんな表情。); fix là bản dịch đúng đang nằm ở key 2052.

### 1652 — Hibiki — lệch dòng
- JP: 「あ！」
- TW: 「啊！」
- VN cũ: Người đã hành động đúng như toan tính, không chỉ có mình Houshou Mototada.
- Sửa: 「A!」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2300 (JP: 思惑通りにことを運んだのは、宝生元忠一人ではない。); fix là bản dịch đúng đang nằm ở key 1689.

### 1672 — Hibiki — lệch dòng
- JP: 「んん？」
- TW: 「嗯？」
- VN cũ: Hibiki nghiêng đầu vẻ khó hiểu.
- Sửa: 「Ừm?」
- Lý do: Dịch mới: JP "んん？" (Hibiki "Ừm?"), VN cũ là độc thoại "Hibiki nghiêng đầu vẻ khó hiểu." — đó là bản dịch của 2387, đã chuyển về đúng chỗ.

### 1679 — Kisaki — lệch dòng
- JP: 「ふふ、光栄だね」
- TW: 「嘿嘿，我很高興你能這麼說」
- VN cũ: Một bàn tay trắng ngần,\nđưa thẳng về phía tôi.
- Sửa: 「Fufu, vinh hạnh thật.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2257 (JP: まっすぐに、\n真っ白い手が伸びてくる。); fix là bản dịch đúng đang nằm ở key 1945.

### 1681 — Mototada — lệch dòng
- JP: 「ほう」
- TW: 「嚯」
- VN cũ: Ánh mắt nhìn tôi sắc bén lại.
- Sửa: 「Ồ.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2193 (JP: 僕を見る目が鋭く細まる。); fix là bản dịch đúng đang nằm ở key 1783.

### 1687 — Hibiki — lệch dòng
- JP: 「だって……稀咲先輩の手書きのやつは、\n一万円って書いただけの、ただの紙切れ――あ」
- TW: 「因為……稀咲學姐你手寫的那張，只不過是一張紙上寫了一萬——啊」
- VN cũ: Dường như đã hiểu ra,\nđôi mắt Hibiki sáng long lanh và mở to.
- Sửa: 「Bởi vì……tờ giấy tiền bối Kisaki viết tay,\nchỉ là một mảnh giấy vụn có viết chữ một vạn yên――A.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2379 (JP: 理解したのか、\n日々姫の目がキラキラ輝き、丸くなってく。); fix là bản dịch đúng đang nằm ở key 1880.

### 1689 — Soutetsu — lệch dòng
- JP: 「実際に良い話だからだ。\n損が無いのは、僕らも全く同じだろう？」
- TW: 「因為這個結果實際上並不壞。對我們來說，這樣也完全沒有什麼損失，不是嗎？」
- VN cũ: 「A!」
- Sửa: 「Vì thực tế thì đó là một thỏa thuận tốt.\nViệc không bị thiệt thòi, chúng ta cũng hoàn toàn giống nhau mà?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1652 (JP: 「あ！」); fix là bản dịch đúng đang nằm ở key 2048.

### 1700 — Soutetsu — lệch dòng
- JP: 「了解だ。――む？」
- TW: 「好的——嗯？」
- VN cũ: Sao thế này, Hibiki đang phồng má giận dỗi.
- Sửa: 「Rõ rồi. ――Hửm?」
- Lý do: Dịch mới: JP "了解だ。――む？" (Soutetsu "Rõ rồi. — Hửm?"), VN cũ là độc thoại "Sao thế này, Hibiki đang phồng má giận dỗi." — đó là bản dịch của 2176, đã chuyển về đúng chỗ.

### 1702 — Kisaki — lệch dòng
- JP: 「そうですか。でしたら拝命いたします」
- TW: 「好的，謹遵您的指示」
- VN cũ: 「Ta mong chờ sự nỗ lực hết mình của con.\nĐừng làm ta thất vọng đấy nhé?」
- Sửa: 「Vậy sao. Nếu thế thì tôi xin tuân lệnh.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1793 (JP: 「全力を期待している。\n私を失望させんでくれよ？」); fix là bản dịch đúng đang nằm ở key 1990.

### 1704 — Mototada — lệch dòng
- JP: 「メリットならある。御一夜市が衰退してしまうのなら、\nクマ焼酎もクマ川下りも鉄道も衰退していく」
- TW: 「好處當然有。如果御一夜繼續衰退下去，隈燒酒、隈河漂流和鐵路也會跟著走下坡路」
- VN cũ: 「Việc ngăn chặn sự suy tàn của thành phố Ohito không liên quan trực tiếp đến việc mời gọi nhà máy.\nChúng cháu tin rằng có những cách khác để phục hưng Ohito.」
- Sửa: 「Lợi ích thì có đấy. Nếu thành phố Ohito suy tàn,\nthì shochu Kuma, chèo thuyền trên sông Kuma hay đường sắt cũng sẽ lụi bại theo.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2046 (JP: 「御一夜市の衰退を防ぐことと、工場誘致とは直結しない。\n僕らは他のやり方で御一夜を再興できると考えています」); fix là bản dịch đúng đang nằm ở key 1540.

### 1705 — Mototada — lệch dòng
- JP: 「ならば御一夜支店長。誘致は私の方で進める。\n君は外れて、別案の方に注力してくれたまえ」
- TW: 「好，御一夜支行行長，工廠落戶方案由我來推進。你就從這項方案中抽身，去全力推進別的方案」
- VN cũ: 「Chuyện đó――」
- Sửa: 「Vậy thì, Giám đốc chi nhánh Ohito. Việc mời gọi nhà máy cứ để ta lo.\nCon hãy rút lui khỏi chuyện đó, và tập trung vào phương án khác đi.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là giá trị ngắn thừa, không phải bản dịch của dòng nào trong file; fix là bản dịch đúng đang nằm ở key 1726.

### 1711 — Soutetsu — lệch dòng
- JP: 「みながお金を信頼せねば、\n紙幣など、ただの紙切れになってしまうということだ」
- TW: 「如果人不信任金錢，那麼紙幣也不過就是一張廢紙罷了」
- VN cũ: 「Hửm?」
- Sửa: 「Nếu mọi người không tin tưởng vào tiền,\nthì tiền giấy cũng chỉ là những mảnh giấy vụn mà thôi.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là giá trị ngắn thừa, không phải bản dịch của dòng nào trong file; fix là bản dịch đúng đang nằm ở key 1633.

### 1715 — Mototada — lệch dòng
- JP: 「安くて旨い酒があるなら、\n私にも飲ませて欲しいものだ」
- TW: 「如果你有便宜又好喝的酒，那我倒希望能嚐嚐」
- VN cũ: 「Cháu không thể chuẩn bị ngay lúc này được.\nNhưng――」
- Sửa: 「Nếu có loại rượu vừa rẻ vừa ngon,\nthì ta cũng muốn nếm thử xem sao.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2053 (JP: 「今すぐに用意できるものでもありません。\nが――」); fix là bản dịch đúng đang nằm ở key 2325.

### 1719 — Mototada — lệch dòng
- JP: 「一滴の水を守れぬことから、味が落ちるというのなら、\nクマ焼酎は、所詮そのレベルの酒とも言えるだろう」
- TW: 「如果因為一滴水的質量，就會導致品質下降的話，只能說隈燒酒也不過如此罷了」
- VN cũ: 「!」
- Sửa: 「Nếu chỉ vì không bảo vệ được một giọt nước mà làm giảm hương vị,\nthì shochu Kuma suy cho cùng cũng chỉ là loại rượu tầm thường thôi.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là giá trị ngắn thừa, không phải bản dịch của dòng nào trong file; fix là bản dịch đúng đang nằm ở key 2557.

### 1723 — Soutetsu — lệch dòng
- JP: 「一個一個を取り上げるなら、そうであるかもしれません。\nが。連携させれば、まったく新しい価値を創出できます」
- TW: 「如果您單獨看待它們的話，可能確實如此。但是，讓它們相輔相成的話，就能創造出全新的價值」
- VN cũ: 「Kết hợp, nhỉ.」
- Sửa: 「Nếu chỉ lấy ra từng cái một, thì có thể là vậy.\nNhưng, nếu kết hợp chúng lại, chúng ta có thể tạo ra những giá trị hoàn toàn mới.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1912 (JP: 「連携、ね」); fix là bản dịch đúng đang nằm ở key 1551.

### 1726 — Soutetsu — lệch dòng
- JP: 「稀咲さんのご助力をいただけるなら、\n極めてありがたく思います」
- TW: 「如果能得到稀咲的幫助，那當然感激不盡」
- VN cũ: 「Vậy thì, Giám đốc chi nhánh Ohito. Việc mời gọi nhà máy cứ để ta lo.\nCon hãy rút lui khỏi chuyện đó, và tập trung vào phương án khác đi.」
- Sửa: 「Nếu nhận được sự giúp đỡ của Kisaki,\ncháu sẽ vô cùng biết ơn ạ.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1705 (JP: 「ならば御一夜支店長。誘致は私の方で進める。\n君は外れて、別案の方に注力してくれたまえ」); fix là bản dịch đúng đang nằm ở key 2570.

### 1730 — Hibiki — lệch dòng
- JP: 「せ、先輩？」
- TW: 「學，學姐？」
- VN cũ: 「…………」
- Sửa: 「T-tiền bối?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là giá trị ngắn thừa, không phải bản dịch của dòng nào trong file; fix là bản dịch đúng đang nằm ở key 2530.

### 1741 — Soutetsu — lệch dòng
- JP: 「聞いてくれ、宝生稀咲」
- TW: 「寶生稀咲，你聽我說」
- VN cũ: Nhìn thẳng vào cô ấy,\ntôi truyền đạt những lời muốn nói một cách trực diện.
- Sửa: 「Nghe này, Houshou Kisaki.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2346 (JP: まっすぐに見て、\nただまっすぐに言葉を伝える。); fix là bản dịch đúng đang nằm ở key 1743.

### 1743 — Soutetsu — lệch dòng
- JP: 「そうだ……言い換えれば、ほとんど同じことなのだ」
- TW: 「對啊……換個角度來考慮的話，其實是差不多的」
- VN cũ: 「Nghe này, Houshou Kisaki.」
- Sửa: 「Đúng rồi……nói cách khác, nó gần như là một.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1741 (JP: 「聞いてくれ、宝生稀咲」); fix là bản dịch đúng đang nằm ở key 2288.

### 1749 — Soutetsu — lệch dòng
- JP: 「さっきの例えを借りるなら、『旨くはないが安い酒』。\n御一夜市民の大多数は、工場誘致をそう捉えている」
- TW: 「就用剛才的例子來說吧，大多數御一夜市民都把工廠落戶方案當作是“不好喝但便宜的酒”」
- VN cũ: Một tiếng kêu như thích thú của Kisaki.\nTrong một khoảnh khắc ngắn ngủi, Houshou Mototada nhíu mày vẻ khó chịu.
- Sửa: 「Mượn ví dụ lúc nãy của bác, thì đó là 『loại rượu không ngon nhưng rẻ』.\nĐại đa số người dân Ohito đều coi việc mời gọi nhà máy là như vậy.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2298 (JP: 面白がるような稀咲の一声。\nほんの一瞬、不愉快そうに宝生元忠の眉根が寄る。); fix là bản dịch đúng đang nằm ở key 2572.

### 1757 — Kisaki — đại từ
- JP: 「この部屋からは、一階フロアを見下ろせる。\n日々姫には、見せたことがあるよね？」
- TW: 「從這個房間可以俯瞰一樓。日日姬，我以前帶你看過吧？」
- VN cũ: 「Từ phòng này có thể nhìn xuống tầng một.\nChị từng cho Hibiki xem rồi nhỉ?」
- Sửa: 「Từ phòng này có thể nhìn xuống tầng một. Em từng cho Hibiki xem rồi nhỉ?」
- Lý do: Đại từ Kisaki: Kisaki nói với Soutetsu ("Từ phòng này có thể nhìn xuống tầng một. Em từng cho Hibiki xem rồi nhỉ?"), tự xưng "em" theo quy tắc Kisaki "em" với Soutetsu; VN cũ "chị" sai (chỉ đúng khi nói với Hibiki). Nội dung câu giữ nguyên, chỉ đổi đại từ.

### 1768 — Soutetsu — lệch dòng
- JP: 「どうした、日々姫？」
- TW: 「怎麼了，日日姬？」
- VN cũ: 「Dạ? À, không có gì đâu!\nKhông, ưm, không có gì đâu ạ. Em ổn.」
- Sửa: 「Sao vậy, Hibiki?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1630 (JP: 「え？　あ、なーんも！\nなーん、んんっ、何でもないです。大丈夫」); fix là bản dịch đúng đang nằm ở key 2172.

### 1775 — Soutetsu — lệch dòng
- JP: 「あなたの目標とて、\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致自体ではない筈だ。\n誘致はあくまで、御一夜再生、経済振興の手段ですよね」
- TW: 「您的目的應該並不是\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶這件事本身。工廠落戶，只不過是讓御一夜重獲新生、振興經濟的手段吧」
- VN cũ: 「Haha, vậy là cháu muốn nói điều này sao.\n『Cháu có một kế hoạch phục hưng Ohito xuất sắc hơn việc mời gọi nhà máy』.」
- Sửa: 「Mục tiêu của bác chắc chắn không phải là việc mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;.\nViệc mời gọi nhà máy chỉ là phương tiện để phục hưng Ohito và chấn hưng kinh tế thôi, đúng không ạ.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1620 (JP: 「ははぁ、つまりはこう言いたいわけか。\n『工場誘致より優れた御一夜再生計画がある』と」); fix là bản dịch đúng đang nằm ở key 2291.

### 1777 — Soutetsu — lệch dòng
- JP: 「確かに、ご主張の点はその通りかと思います」
- TW: 「您說的確實很有道理」
- VN cũ: Dù không có ánh mắt đó, tôi vẫn muốn đối mặt.\nTôi muốn thử thách và mài giũa bản thân bằng những lời chỉ trích sắc bén của Houshou Mototada.
- Sửa: 「Cháu nghĩ những gì bác nói hoàn toàn chính xác.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2302 (JP: それがなくとも、向き合ってみたい。\n宝生元忠の厳しい指摘で、自分を洗って、計ってみたい。); fix là bản dịch đúng đang nằm ở key 2385.

### 1783 — Soutetsu — lệch dòng
- JP: 「と、いうよりむしろ――\n工場誘致は、さほど優れた再生計画ではない気がします」
- TW: 「應該這樣說——我認為，其實工廠落戶並不是一個很好的振興計劃」
- VN cũ: 「Ồ.」
- Sửa: 「Đúng hơn là――\nCháu cảm thấy việc mời gọi nhà máy không phải là một kế hoạch phục hưng xuất sắc cho lắm.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1681 (JP: 「ほう」); fix là bản dịch đúng đang nằm ở key 1620.

### 1785 — Kisaki — lệch dòng
- JP: 「御一夜市が二分されるのは好ましくありません。\nできるかぎり多くからの同意を得られるように――」
- TW: 「我不希望將御一夜一分為二。這時候應該儘可能得到多數人的同意——」
- VN cũ: 「Tất nhiên, chúng ta cũng sẽ nỗ lực làm điều đó.\nNhưng nếu hai bên đều không chịu nhượng bộ, thì chỉ còn cách đối đầu thôi.」
- Sửa: 「Việc thành phố Ohito bị chia rẽ là điều không nên.\nChúng ta cần cố gắng đạt được sự đồng thuận từ càng nhiều người càng tốt――」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1791 (JP: 「もちろん、そうした努力も行う。\nが、譲れぬもの同士であれば、ぶつかるしかない」); fix là bản dịch đúng đang nằm ở key 1604.

### 1787 — Kisaki — lệch dòng
- JP: 「こちらこそ」
- TW: 「我也拜託你了」
- VN cũ: Một cái bắt tay ngắn ngủi.\nNhưng đầy mạnh mẽ.
- Sửa: 「Em cũng vậy.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2323 (JP: 短い握手。\n力強い。); fix là bản dịch đúng đang nằm ở key 1838.

### 1791 — Mototada — lệch dòng
- JP: 「もちろん、そうした努力も行う。\nが、譲れぬもの同士であれば、ぶつかるしかない」
- TW: 「我們當然會努力這麼做。但如果我們雙方都不肯讓步的話，只好正面交鋒了」
- VN cũ: 「Thật vậy sao?」
- Sửa: 「Tất nhiên, chúng ta cũng sẽ nỗ lực làm điều đó.\nNhưng nếu hai bên đều không chịu nhượng bộ, thì chỉ còn cách đối đầu thôi.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là giá trị ngắn thừa, không phải bản dịch của dòng nào trong file; fix là bản dịch đúng đang nằm ở key 1785.

### 1793 — Mototada — lệch dòng
- JP: 「全力を期待している。\n私を失望させんでくれよ？」
- TW: 「我希望你能全力以赴。可不要讓我失望了哦」
- VN cũ: Nói rồi, bác Mototada quay sang tôi.\nTrong ánh mắt ấy không còn sự sắc bén như lúc nãy nữa.
- Sửa: 「Ta mong chờ sự nỗ lực hết mình của con.\nĐừng làm ta thất vọng đấy nhé?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2214 (JP: 言って、元忠氏は僕へ向く。\nその目にはもう、先程までの鋭さは無い。); fix là bản dịch đúng đang nằm ở key 1702.

### 1796 — Soutetsu — lệch dòng
- JP: 「だろうと僕は確信している。すぐには影響が出なくても\nいずれは徐々に、確実に」
- TW: 「我確信如此。影響就算不會馬上發生，也一定會慢慢顯現」
- VN cũ: 「Nếu vậy……Ohito sẽ đánh mất thương hiệu shochu Kuma.\nKhoản lợi nhuận bị mất đó――đúng là không thể phớt lờ được.」
- Sửa: 「Anh tin chắc là vậy. Dù không có ảnh hưởng ngay lập tức\nnhưng dần dần, chắc chắn sẽ xảy ra.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1991 (JP: 「となると……御一夜はクマ焼酎というブランドを失う。\nその[いっしつ,1]逸失利益は――確かに無視できるものとも思えな); fix là bản dịch đúng đang nằm ở key 1864.

### 1798 — Mototada — lệch dòng
- JP: 「入っていいか？　仕事の話だ」
- TW: 「我能進來嗎？有些工作上的事」
- VN cũ: 「Khoan, khoan, đợi một chút đã――\nHiện tại đang có khách――Hibiki và Soutetsu đang ở đây.」
- Sửa: 「Ta vào được chứ? Có chuyện công việc.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1939 (JP: 「ちょ、ちょ、ちょっと待って――\nいま、来客中――日々姫と双鉄が来てるんだ」); fix là bản dịch đúng đang nằm ở key 1887.

### 1799 — Soutetsu — lệch dòng
- JP: 「一円を大事にせず、守ることが出来ぬ銀行を――\nいったい、どこの誰が使うのか、という話かとも思う」
- TW: 「我覺得這就好像——究竟會有誰會去光顧不重視一日元的銀行的道理一樣」
- VN cũ: Chậm rãi, sâu sắc.\nKisaki gật đầu.
- Sửa: 「Một ngân hàng không coi trọng và không bảo vệ nổi một yên――\nthì rốt cuộc sẽ có ai muốn sử dụng chứ, anh nghĩ chuyện này cũng tương tự như vậy.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2504 (JP: ゆっくり、深く。\n稀咲が頷く。); fix là bản dịch đúng đang nằm ở key 1867.

### 1804 — Kisaki — lệch dòng
- JP: 「で？　\n具体的に、君たちの計画はどの程度進んでいるんだい？」
- TW: 「所以呢？具體來說，你們的計劃進行到什麼地步了？」
- VN cũ: 「Rất tiếc là, hầu như chưa có gì.\nNgay cả việc tận dụng 8620――đường sắt như thế nào, cũng chưa được xác định.」
- Sửa: 「Thế? \nCụ thể thì kế hoạch của các anh tiến triển đến đâu rồi?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1955 (JP: 「残念ながら、まだほとんど。\n[ハチロクニイマル,3]8620――鉄道をどう活用するかも、確定してない状況だ」); fix là bản dịch đúng đang nằm ở key 2337.

### 1805 — Kisaki — đại từ
- JP: 「仕事の打ち合わせは口実だ。時間を取って――\nもう少し、突っ込んだ話を出来ないものかと思ってね」
- TW: 「所謂“商量工作”只是個藉口而已。我只是想多花些時間——和你們深入交流」
- VN cũ: 「Bàn bạc công việc chỉ là cái cớ thôi. Chị muốn dành thời gian――\nđể chúng ta có thể nói chuyện sâu hơn một chút.」
- Sửa: 「Bàn bạc công việc chỉ là cái cớ thôi. Em muốn dành thời gian―― để chúng ta có thể nói chuyện sâu hơn một chút.」
- Lý do: Đại từ Kisaki: Kisaki nói với Soutetsu (muốn dành thời gian nói chuyện sâu hơn với anh), tự xưng "em" theo quy tắc Kisaki "em" với Soutetsu; VN cũ "chị" sai. Nội dung câu giữ nguyên, chỉ đổi đại từ.

### 1809 — Kisaki — lệch dòng
- JP: 「ただの紙切れが通貨として、労働力の代替物として、\n通用するのは――そこに信頼があるからだよね？」
- TW: 「把一張紙當做貨幣，當做勞動力的等價物，並且全國通用——這不正是依靠信任才能做到的嗎？」
- VN cũ: 「Ra là vậy. Phiếu mua hàng cũng thế nhỉ.\nVì biết là dùng được, vì tin tưởng được nên nó không phải là giấy vụn.」
- Sửa: 「Một mảnh giấy vụn có thể được lưu thông như một loại tiền tệ, như một vật thay thế cho sức lao động――\nđó là vì có niềm tin đặt vào nó đúng không?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1830 (JP: 「なんですね。商品券とかもそうですよね。\n使えるってわかってる、信頼できるから紙切れじゃない」); fix là bản dịch đúng đang nằm ở key 1539.

### 1815 — Mototada — lệch dòng
- JP: 「逆に聞こう。クマ焼酎とは、\n水の一滴を損ねることで、壊れてしまう程度の酒かね？」
- TW: 「換個說法吧。隈燒酒是會因為一滴水的品質受損而導致質量下降的酒嗎？」
- VN cũ: 「Làm gì có chuyện đó!」
- Sửa: 「Để ta hỏi ngược lại cậu. Shochu Kuma,\nlà loại rượu dễ dàng bị hủy hoại chỉ vì một giọt nước bị vấy bẩn sao?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2000 (JP: 「そぎゃんこつあるわけなかっ！」); fix là bản dịch đúng đang nằm ở key 2287.

### 1816 — Soutetsu — lệch dòng
- JP: 「いいかえれば、発行元に対する信頼が、\n通貨の価値を担保している、ということになるか」
- TW: 「換句話說，就是用發行單位的信用，來給貨幣的價值作擔保吧」
- VN cũ: Nếu niềm tin đó bị phá vỡ――\nVí dụ như quốc gia phát hành bị phá sản, thì tiền tệ cũng sẽ sụp đổ.
- Sửa: 「Nói cách khác, niềm tin vào đơn vị phát hành\nchính là thứ bảo chứng cho giá trị của tiền tệ sao.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2285 (JP: その信頼が壊れてしまえば――\n例えば発行元の国が破綻してしまったなら、通貨も破綻だ。); fix là bản dịch đúng đang nằm ở key 1830.

### 1820 — Kisaki — lệch dòng
- JP: 「どう転んでも銀行の利益になる以上、\nボクも心置きなく、全力で君に協力しよう」
- TW: 「既然無論怎麼發展都對銀行有益，那麼我也可以毫無顧慮地盡全力幫助你了」
- VN cũ: 「Đáng tin cậy thật, trăm sự nhờ em nhé.」
- Sửa: 「Một khi đằng nào cũng mang lại lợi ích cho ngân hàng,\nem sẽ toàn tâm toàn ý, dốc hết sức hợp tác với anh.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1838 (JP: 「心強いな、よろしく頼む」); fix là bản dịch đúng đang nằm ở key 2257.

### 1826 — Soutetsu — lệch dòng
- JP: 「確かにな。どう転んでも、元忠氏は損をしない。\n僕らが上手い再建計画を立案できても、そうでなくても」
- TW: 「是啊。不論結果如何，對元忠先生都有利無害。不論我們能否成功擬定一個好的方案，對他都沒影響」
- VN cũ: 「Hả!?」
- Sửa: 「Đúng là vậy. Dù kết quả có ra sao, bác Mototada cũng không thiệt thòi.\nCho dù chúng ta có lập được kế hoạch tái thiết tốt hay không.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1624 (JP: 「えっ！？」); fix là bản dịch đúng đang nằm ở key 2527.

### 1830 — Hibiki — lệch dòng
- JP: 「なんですね。商品券とかもそうですよね。\n使えるってわかってる、信頼できるから紙切れじゃない」
- TW: 「是啊。購物卡也是一個道理。正因為知道它可以使用，信任它，它才不是一張廢紙」
- VN cũ: 「Nói cách khác, niềm tin vào đơn vị phát hành\nchính là thứ bảo chứng cho giá trị của tiền tệ sao.」
- Sửa: 「Ra là vậy. Phiếu mua hàng cũng thế nhỉ.\nVì biết là dùng được, vì tin tưởng được nên nó không phải là giấy vụn.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1816 (JP: 「いいかえれば、発行元に対する信頼が、\n通貨の価値を担保している、ということになるか」); fix là bản dịch đúng đang nằm ở key 1809.

### 1833 — Soutetsu — lệch dòng
- JP: 「そうでしょうか？」
- TW: 「是嗎？」
- VN cũ: Đối đầu với nhau, và kẻ yếu hơn sẽ bị nuốt chửng.
- Sửa: 「Vậy sao ạ?」
- Lý do: Dịch mới: JP "そうでしょうか？" (Soutetsu hỏi Mototada "Vậy sao ạ?"), VN cũ là độc thoại "Đối đầu với nhau, và kẻ yếu hơn sẽ bị nuốt chửng." — đó là bản dịch của 2599, đã chuyển về đúng chỗ.

### 1838 — Soutetsu — lệch dòng
- JP: 「心強いな、よろしく頼む」
- TW: 「有你在我就放心多了，拜託了」
- VN cũ: 「Em cũng vậy.」
- Sửa: 「Đáng tin cậy thật, trăm sự nhờ em nhé.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1787 (JP: 「こちらこそ」); fix là bản dịch đúng đang nằm ở key 1820.

### 1852 — Soutetsu — lệch dòng
- JP: 「仰るとおり。\nその線を基本と考えています」
- TW: 「正如您所說。這三樣東西就是我們的基本方針」
- VN cũ: 「Hừ.」
- Sửa: 「Đúng như bác nói.\nĐó là định hướng cơ bản của chúng cháu.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là giá trị ngắn thừa, không phải bản dịch của dòng nào trong file; fix là bản dịch đúng đang nằm ở key 1566.

### 1864 — Kisaki — lệch dòng
- JP: 「使わないね、そんな銀行。\nだから……水も守れない焼酎は、飲まれなくなる？」
- TW: 「沒有人會去那樣的銀行的。所以……也自然沒有人會喝連水質都無法保證的燒酒？」
- VN cũ: 「Anh tin chắc là vậy. Dù không có ảnh hưởng ngay lập tức\nnhưng dần dần, chắc chắn sẽ xảy ra.」
- Sửa: 「Không ai dùng đâu, một ngân hàng như thế.\nVậy nên……shochu mà không bảo vệ nổi nguồn nước, thì sẽ không còn ai uống nữa?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1796 (JP: 「だろうと僕は確信している。すぐには影響が出なくても\nいずれは徐々に、確実に」); fix là bản dịch đúng đang nằm ở key 2504.

### 1867 — Soutetsu — lệch dòng
- JP: 「そうだ。ただの一歩でも譲っては――\nクマ焼酎が今まで積み重ねてきた信頼を破壊してしまう」
- TW: 「沒錯。哪怕妥協一點點——隈燒酒都會遺失掉過去積累起來的信任」
- VN cũ: 「Một ngân hàng không coi trọng và không bảo vệ nổi một yên――\nthì rốt cuộc sẽ có ai muốn sử dụng chứ, anh nghĩ chuyện này cũng tương tự như vậy.」
- Sửa: 「Đúng vậy. Dù chỉ nhượng bộ một bước――\ncũng sẽ phá hủy đi niềm tin mà shochu Kuma đã dày công gây dựng bấy lâu nay.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1799 (JP: 「一円を大事にせず、守ることが出来ぬ銀行を――\nいったい、どこの誰が使うのか、という話かとも思う」); fix là bản dịch đúng đang nằm ở key 1644.

### 1880 — Kisaki — lệch dòng
- JP: 「何故、当たり前なのかな」
- TW: 「為什麼會是理所當然的呢」
- VN cũ: 「Bởi vì……tờ giấy tiền bối Kisaki viết tay,\nchỉ là một mảnh giấy vụn có viết chữ một vạn yên――A.」
- Sửa: 「Tại sao lại là đương nhiên chứ.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1687 (JP: 「だって……稀咲先輩の手書きのやつは、\n一万円って書いただけの、ただの紙切れ――あ」); fix là bản dịch đúng đang nằm ở key 2494.

### 1886 — Kisaki — lệch dòng
- JP: 「父が？　気になったって、一体――」
- TW: 「父親？你在意的是——」
- VN cũ: 「À thì――a! Đúng rồi,\nRõ ràng bác ấy đến tìm tiền bối Kisaki để nói chuyện mà――hả!?」
- Sửa: 「Bố em á? Tò mò chuyện gì cơ――」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1614 (JP: 「ええと――あ！　そう、\n稀咲先輩に話があって来たはずなのに――えっ！？」); fix là bản dịch đúng đang nằm ở key 1999.

### 1887 — Kisaki — lệch dòng
- JP: 「父さ――と、頭取っ！？」
- TW: 「爸——行、行長！？」
- VN cũ: 「Ta vào được chứ? Có chuyện công việc.」
- Sửa: 「Bố――à không, Chủ tịch!?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1798 (JP: 「入っていいか？　仕事の話だ」); fix là bản dịch đúng đang nằm ở key 2581.

### 1896 — Kisaki — lệch dòng
- JP: 「環境が緩めば、人は緩む。一円の誤差を許容すれば、\nそれは必ず、十円、百円となってしまう」
- TW: 「環境的鬆懈就會導致人的鬆懈。只要允許一日元的誤差，那麼一定會導致十日元、百日元的誤差」
- VN cũ: Kisaki rời mắt khỏi tầng dưới, nhìn thẳng vào tôi.
- Sửa: 「Nếu môi trường buông lỏng, con người cũng sẽ buông lỏng theo. Chỉ cần chấp nhận sai số một yên thôi, thì chắc chắn nó sẽ thành mười yên, rồi trăm yên.」
- Lý do: Dịch mới: JP "Môi trường buông lỏng thì con người buông lỏng; chấp nhận sai số 1 yên thì sẽ thành 10 yên, 100 yên" (Kisaki), VN cũ là độc thoại "Kisaki rời mắt khỏi tầng dưới…" — đó là bản dịch của 2482, đã chuyển về đúng chỗ.

### 1901 — Soutetsu — lệch dòng
- JP: 「金と……人との使い方、ですか」
- TW: 「用錢的方法……和差遣他人做事的方式嗎」
- VN cũ: 「Hãy cho ta xem đi.\nBản tính con người cháu.」
- Sửa: 「Cách sử dụng tiền bạc……và con người, sao ạ.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1961 (JP: 「見せてもらうよ。\n君という人間の、本性を」); fix là bản dịch đúng đang nằm ở key 2057.

### 1912 — Mototada — lệch dòng
- JP: 「連携、ね」
- TW: 「相輔相成啊」
- VN cũ: Đôi mắt của Houshou Mototada lại nheo lại, quan sát tôi thật kỹ.
- Sửa: 「Kết hợp, nhỉ.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2297 (JP: 宝生元忠の目がまた細まり、僕をじっくり眺め回す。); fix là bản dịch đúng đang nằm ở key 1723.

### 1931 — Mototada — lệch dòng
- JP: 「稀咲は私の自慢の娘だ。\n経営計画の立案には役に立つ」
- TW: 「稀咲是我引以為傲的女兒。她可以幫你規劃經營方案」
- VN cũ: 「Soutetsu, cháu có muốn dùng không?」
- Sửa: 「Kisaki là đứa con gái đáng tự hào của ta.\nNó sẽ giúp ích cho việc lập kế hoạch kinh doanh đấy.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2056 (JP: 「双鉄くん、使うか？」); fix là bản dịch đúng đang nằm ở key 2210.

### 1937 — Soutetsu — lệch dòng
- JP: 「闘争――」
- TW: 「競爭——」
- VN cũ: 「Với tư cách là Giám đốc chi nhánh,\ncháu xin phép được phản đối ý kiến đó.」
- Sửa: 「Một cuộc chiến――」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1557 (JP: 「支店長として、\nそのご意見には異議を唱えさせていただきます」); fix là bản dịch đúng đang nằm ở key 2008.

### 1939 — Kisaki — lệch dòng
- JP: 「ちょ、ちょ、ちょっと待って――\nいま、来客中――日々姫と双鉄が来てるんだ」
- TW: 「等、等、等一下，現在正有客人——日日姬和雙鐵在這裡」
- VN cũ: 「Ồ?」
- Sửa: 「Khoan, khoan, đợi một chút đã――\nHiện tại đang có khách――Hibiki và Soutetsu đang ở đây.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1634 (JP: 「ほう？」); fix là bản dịch đúng đang nằm ở key 1798.

### 1945 — Soutetsu — lệch dòng
- JP: 「それに加えて、宝生稀咲――君の助力まで得られるのだ。\n損得でいえば、むしろ僕らの得点の方が多いと思う」
- TW: 「而且我們還得到了你——寶生稀咲的幫助。要權衡得失的話，不如說我們反而賺多了」
- VN cũ: 「Fufu, vinh hạnh thật.」
- Sửa: 「Thêm vào đó, Houshou Kisaki――còn có được sự giúp đỡ của em nữa.\nNếu nói về được mất, anh nghĩ điểm số của chúng ta còn cao hơn đấy.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1679 (JP: 「ふふ、光栄だね」); fix là bản dịch đúng đang nằm ở key 2321.

### 1955 — Soutetsu — lệch dòng
- JP: 「残念ながら、まだほとんど。\n[ハチロクニイマル,3]8620――鉄道をどう活用するかも、確定してない状況だ」
- TW: 「說來慚愧，還沒有多少進展。我們目前還不知道應該如何發揮８６２０——發揮鐵路的優勢」
- VN cũ: 「Ra là vậy.\nThế thì, chắc em phải bắt đầu khảo sát từ đó thôi nhỉ.」
- Sửa: 「Rất tiếc là, hầu như chưa có gì.\nNgay cả việc tận dụng 8620――đường sắt như thế nào, cũng chưa được xác định.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1586 (JP: 「なるほど。\nでは、まずはそこから視察させてもらうとするかな」); fix là bản dịch đúng đang nằm ở key 1804.

### 1961 — Mototada — lệch dòng
- JP: 「見せてもらうよ。\n君という人間の、本性を」
- TW: 「讓我見識一下你這個人的本性吧」
- VN cũ: Tôi cảm nhận rõ ràng mình đang bị thử thách.\nĐồng thời, một câu hỏi tự vấn được gieo vào tâm trí tôi.
- Sửa: 「Hãy cho ta xem đi.\nBản tính con người cháu.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2338 (JP: 試されてると、強く感じる。\n同時に自問を植え付けられる。); fix là bản dịch đúng đang nằm ở key 1901.

### 1965 — Mototada — lệch dòng
- JP: 「水環境のことなど、買い手は気にせんよ。\n購買の判断基準は、旨いまずいと、高い安いとだけだ」
- TW: 「購買者根本不會在意水環境的問題。左右他們購買慾望的只有是否好喝、價格是否便宜」
- VN cũ: 「!」
- Sửa: 「Người mua không quan tâm đến môi trường nước đâu.\nTiêu chí để họ quyết định mua chỉ là ngon hay dở, đắt hay rẻ mà thôi.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là giá trị ngắn thừa, không phải bản dịch của dòng nào trong file; fix là bản dịch đúng đang nằm ở key 2341.

### 1983 — Kisaki — lệch dòng
- JP: 「それは――」
- TW: 「這——」
- VN cũ: Kisaki rõ ràng đang dao động.
- Sửa: 「Đó là――」
- Lý do: Dịch mới: JP "それは――" (Kisaki ngập ngừng), VN cũ là độc thoại "Kisaki rõ ràng đang dao động." — đó là bản dịch của 2490, đã chuyển về đúng chỗ.

### 1985 — Hibiki — lệch dòng
- JP: 「そんなの……当たり前じゃないですか」
- TW: 「這不是理所當然的嗎……」
- VN cũ: Kisaki mỉm cười đáp lại lời nói đầy vẻ hoài nghi của Hibiki.
- Sửa: 「Chuyện đó……chẳng phải là đương nhiên sao.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2494 (JP: 怪訝そうな日々姫の言葉に答える稀咲はにこやかだ。); fix là bản dịch đúng đang nằm ở key 1579.

### 1987 — Kisaki — lệch dòng
- JP: 「これは、両方とも一万円札だ。日ノ本銀行発行のものと、\n宝生稀咲、個人が発行したものと」
- TW: 「這兩張都是一萬日元紙幣。區別在於一張是日本銀行發行的，另一張是寶生稀咲個人發行的」
- VN cũ: 「Hả?」
- Sửa: 「Cả hai tờ này đều là tờ một vạn yên. Một tờ do Ngân hàng Hinomoto phát hành,\nvà một tờ do cá nhân Houshou Kisaki phát hành.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1629 (JP: 「え？」); fix là bản dịch đúng đang nằm ở key 2508.

### 1990 — Mototada — lệch dòng
- JP: 「業務命令だ。支店長」
- TW: 「這是公司命令。支行行長」
- VN cũ: 「Vậy sao. Nếu thế thì tôi xin tuân lệnh.」
- Sửa: 「Là mệnh lệnh công việc. Giám đốc chi nhánh.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1702 (JP: 「そうですか。でしたら拝命いたします」); fix là bản dịch đúng đang nằm ở key 1256.

### 1991 — Kisaki — lệch dòng
- JP: 「となると……御一夜はクマ焼酎というブランドを失う。\nその[いっしつ,1]逸失利益は――確かに無視できるものとも思えない」
- TW: 「這樣一來……御一夜就少了隈燒酒這樣一個品牌。我們確實不能眼睜睜看著這樣一塊利益消失掉」
- VN cũ: 「Vậy thì, thế nào.\nChuyện mời gọi nhà máy, em có thể xem xét lại được không.」
- Sửa: 「Nếu vậy……Ohito sẽ đánh mất thương hiệu shochu Kuma.\nKhoản lợi nhuận bị mất đó――đúng là không thể phớt lờ được.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1998 (JP: 「ならば、どうだ。\n工場誘致の件、再検討をしてもらえんか」); fix là bản dịch đúng đang nằm ở key 1796.

### 1992 — Kisaki — lệch dòng
- JP: 「いや、良い話し合いって」
- TW: 「這，很有意義嗎」
- VN cũ: 「Anh hai ngây thơ quá! \nThế này là trúng kế của ổng rồi còn gì!」
- Sửa: 「Không, anh bảo là thảo luận tốt á.」
- Lý do: Dịch mới: JP "いや、良い話し合いって" (Kisaki bắt lại cụm "cuộc thảo luận tốt" của Soutetsu ở 1559, ý "Không, anh bảo là thảo luận tốt á."), VN cũ là câu của Hibiki "Anh hai ngây thơ quá!…" — đó là bản dịch của 2050, đã chuyển về đúng chỗ.

### 1994 — Mototada — lệch dòng
- JP: 「ならば、何の問題も無い」
- TW: 「那不就沒問題了嗎」
- VN cũ: 「A――」
- Sửa: 「Vậy thì, không có vấn đề gì cả.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1640 (JP: 「あ――」); fix là bản dịch đúng đang nằm ở key 2000.

### 1998 — Soutetsu — lệch dòng
- JP: 「ならば、どうだ。\n工場誘致の件、再検討をしてもらえんか」
- TW: 「那你看這樣如何，不如重新探討一下工廠落戶方案吧」
- VN cũ: 「Đừng vội vàng thế, Soutetsu. Chuyện lớn như vậy,\nmột Giám đốc chi nhánh như em làm sao có thể quyết định ngay được.」
- Sửa: 「Vậy thì, thế nào.\nChuyện mời gọi nhà máy, em có thể xem xét lại được không.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2055 (JP: 「慌てないでくれ、双鉄。そこまでのこと、\n支店長レベルで即決できるわけがないだろう」); fix là bản dịch đúng đang nằm ở key 1991.

### 1999 — Hibiki — lệch dòng
- JP: 「ええと、ちょっと気になって――その――あっ！\nあれです、元忠さん、稀咲先輩のお父さん」
- TW: 「那個，我只是有點在意——就是——啊！就是元忠先生，稀咲學姐的父親」
- VN cũ: 「Bố em á? Tò mò chuyện gì cơ――」
- Sửa: 「À thì, em chỉ hơi tò mò――chuyện đó――a!\nChuyện bác Mototada, bố của tiền bối Kisaki ấy.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1886 (JP: 「父が？　気になったって、一体――」); fix là bản dịch đúng đang nằm ở key 2261.

### 2000 — Hibiki — lệch dòng
- JP: 「そぎゃんこつあるわけなかっ！」
- TW: 「那哪可能嘛！」
- VN cũ: 「Vậy thì, không có vấn đề gì cả.」
- Sửa: 「Làm gì có chuyện đó!」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1994 (JP: 「ならば、何の問題も無い」); fix là bản dịch đúng đang nằm ở key 1815.

### 2008 — Mototada — lệch dòng
- JP: 「ならば優劣を競おうではないか。闘争だ」
- TW: 「那我們就來競爭一下吧，看看誰的方案更加優秀」
- VN cũ: 「Một cuộc chiến――」
- Sửa: 「Vậy thì hãy cạnh tranh xem bên nào ưu việt hơn đi. Một cuộc chiến.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1937 (JP: 「闘争――」); fix là bản dịch đúng đang nằm ở key 2211.

### 2023 — Kisaki — lệch dòng
- JP: 「お金は労働の対価だと――双鉄の答えは、確かに正しい。\nその上で僕は。お金とは、信頼そのものだとも考える」
- TW: 「金錢就是勞動的對等價值——你的回答很正確。但是對我來說，金錢還代表著信任」
- VN cũ: 「Tiền là……ra vậy. Niềm tin sao.」
- Sửa: 「Tiền là thù lao cho sức lao động――câu trả lời của Soutetsu chắc chắn là đúng.\nNhưng hơn thế nữa, em cho rằng tiền chính là niềm tin.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1585 (JP: 「お金は……なるほど。信頼か」); fix là bản dịch đúng đang nằm ở key 2482.

### 2036 — Kisaki — lệch dòng
- JP: 「銀行は、お金という形の信頼を扱っている場所だ。\nだから仮に一円だろうと、それを損ねることは出来ない」
- TW: 「銀行就是處理金錢這種信用的地方。所以哪怕只有一日元偏差，也不能姑息」
- VN cũ: 「Ra là vậy――đó chính là,\n『giá trị của đồng tiền』 đối với Houshou Kisaki sao.」
- Sửa: 「Ngân hàng là nơi xử lý niềm tin dưới hình thức tiền bạc.\nThế nên, dù chỉ là một yên, cũng không thể làm tổn hại đến nó được.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1584 (JP: 「なるほど――それが、\n宝生稀咲にとっての、『お金の価値』か」); fix là bản dịch đúng đang nằm ở key 2393.

### 2046 — Soutetsu — lệch dòng
- JP: 「御一夜市の衰退を防ぐことと、工場誘致とは直結しない。\n僕らは他のやり方で御一夜を再興できると考えています」
- TW: 「阻止御一夜的衰退和工廠落戶並沒有直接聯繫。我們正在考慮其他重振御一夜的方法」
- VN cũ: 「Ồ, nếu cháu có ý tưởng khác thì thú vị đấy.」
- Sửa: 「Việc ngăn chặn sự suy tàn của thành phố Ohito không liên quan trực tiếp đến việc mời gọi nhà máy.\nChúng cháu tin rằng có những cách khác để phục hưng Ohito.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1636 (JP: 「ほう、他のアイディアがあるというなら、面白い」); fix là bản dịch đúng đang nằm ở key 1704.

### 2048 — Hibiki — lệch dòng
- JP: 「にぃに――んっ――兄さん。\nそれがわかっているなら、なんで」
- TW: 「阿哥——嗯——哥哥。你都知道是這樣了，為什麼還」
- VN cũ: 「Vì thực tế thì đó là một thỏa thuận tốt.\nViệc không bị thiệt thòi, chúng ta cũng hoàn toàn giống nhau mà?」
- Sửa: 「Anh hai――ưm――anh trai.\nAnh đã biết thế rồi, tại sao còn...」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1689 (JP: 「実際に良い話だからだ。\n損が無いのは、僕らも全く同じだろう？」); fix là bản dịch đúng đang nằm ở key 2391.

### 2050 — Hibiki — lệch dòng
- JP: 「甘かばい！　にぃに！\nあんなん、向こうの思う壺ばい！」
- TW: 「阿哥你忒天真咧！這下正中他下懷咧！」
- VN cũ: Kisaki gật đầu đồng tình với lời nói hùng hồn của Hibiki.\nTôi cũng đồng tình với điều đó.
- Sửa: 「Anh hai ngây thơ quá! \nThế này là trúng kế của ổng rồi còn gì!」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2527 (JP: 勢いこんだ日々姫の言葉に、稀咲も頷く。\n僕とて、そこには同感だ。); fix là bản dịch đúng đang nằm ở key 1992.

### 2052 — Soutetsu — lệch dòng
- JP: 「銀行にとっての一円が、\n焼酎酒造にとっては、クマ川の水の一滴なのだ」
- TW: 「隈河的一滴水對於燒酒釀酒廠的價值，就相當於一日元對於銀行的價值」
- VN cũ: 「A.」
- Sửa: 「Một yên đối với ngân hàng,\ncũng giống như một giọt nước sông Kuma đối với xưởng nấu shochu vậy.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1648 (JP: 「あ」); fix là bản dịch đúng đang nằm ở key 2346.

### 2053 — Soutetsu — lệch dòng
- JP: 「今すぐに用意できるものでもありません。\nが――」
- TW: 「雖然我沒辦法馬上拿出來。但是——」
- VN cũ: 「Cháu định từ giờ sẽ chuẩn bị sao?\nBằng cách kết hợp suối nước nóng, shochu và cả đường sắt nữa.」
- Sửa: 「Cháu không thể chuẩn bị ngay lúc này được.\nNhưng――」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1566 (JP: 「これから用意するつもりかね？\n温泉と焼酎と、それに鉄道を加えて」); fix là bản dịch đúng đang nằm ở key 1715.

### 2055 — Kisaki — lệch dòng
- JP: 「慌てないでくれ、双鉄。そこまでのこと、\n支店長レベルで即決できるわけがないだろう」
- TW: 「雙鐵，你別急。我只是一個支行行長，怎麼可能當場決定這麼大的事情呢」
- VN cũ: 「Ưm……cũng phải.」
- Sửa: 「Đừng vội vàng thế, Soutetsu. Chuyện lớn như vậy,\nmột Giám đốc chi nhánh như em làm sao có thể quyết định ngay được.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là giá trị ngắn thừa, không phải bản dịch của dòng nào trong file; fix là bản dịch đúng đang nằm ở key 1998.

### 2056 — Mototada — lệch dòng
- JP: 「双鉄くん、使うか？」
- TW: 「雙鐵，你需要她嗎？」
- VN cũ: Điều đó là đương nhiên.\nNhưng tôi vẫn cẩn thận trong cách trả lời.
- Sửa: 「Soutetsu, cháu có muốn dùng không?」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2570 (JP: 是非も無い。\nが、答え方には気をつける。); fix là bản dịch đúng đang nằm ở key 1931.

### 2057 — Mototada — lệch dòng
- JP: 「私はね、双鉄くん。その人間の本性は、\n金の使い方と、人の使い方から見えると思っている」
- TW: 「雙鐵，我覺得，從一個人用錢的方法和差遣他人做事的方式裡，就能看出他的本性」
- VN cũ: 「Cách sử dụng tiền bạc……và con người, sao ạ.」
- Sửa: 「Ta nghĩ thế này, Soutetsu. Bản tính của một con người,\ncó thể nhìn thấu qua cách họ sử dụng tiền bạc và con người.」
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1901 (JP: 「金と……人との使い方、ですか」); fix là bản dịch đúng đang nằm ở key 2214.

### 2063 — Hibiki — gasp
- JP: 「っ！」
- TW: 「！」
- VN cũ: Lại một sự thật phũ phàng nữa khó lòng phản bác.
- Sửa: 「Ư!」
- Lý do: Gasp: JP 「っ！」 cả dòng chỉ là một tiếng nấc/gasp (Hibiki), VN cũ là câu độc thoại "Lại một sự thật phũ phàng nữa khó lòng phản bác." — đó là bản dịch của 2190, đã chuyển về đúng chỗ. Fix "Ư!" theo quy tắc っ→Ư. Sweep đã cờ dòng này là "needs-file-audit" — đúng, đã xử lý.

### 2157 — Độc thoại — lệch dòng
- JP: とっさに反論を思いつけない。\nそれは確かに――、一面の強烈な真実だ。
- TW: 一時間我想不到反駁他的話語。從整體來說——這確實是事實。
- VN cũ: 「Nhưng, xưởng nấu rượu thì có quan tâm.\nNếu nhượng bộ điểm đó, một thứ gì đó rất quan trọng sẽ bị đánh mất.」
- Sửa: Tôi không thể nghĩ ra lời phản bác ngay lập tức.\nĐó quả thực là――một sự thật tàn khốc.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1543 (JP: 「けど、酒造はそれを気にします。\nそこを譲れば、なにか、大事なものが失われます」); fix là bản dịch đúng đang nằm ở key 1618.

### 2161 — Độc thoại — lệch dòng
- JP: 強い言葉にやや気圧された一瞬を、\n涼しい声が割り込み、壊す。
- TW: 一瞬間，寶生元忠強勢的語言和魄力給我帶來的壓力，被突然傳來的清澈聲音擊碎。
- VN cũ: Kisaki vẫn giữ vẻ mặt điềm nhiên,\nlặng lẽ nhìn chằm chằm vào Houshou Mototada.
- Sửa: Khoảnh khắc bị áp đảo bởi những lời lẽ mạnh mẽ đó,\nđã bị phá vỡ bởi một giọng nói lạnh lùng xen vào.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2511 (JP: 稀咲は全く変わらぬ様子で、\n宝生元忠を静かに見据える。); fix là bản dịch đúng đang nằm ở key 1557.

### 2162 — Độc thoại — lệch dòng
- JP: 一瞬の、途方にくれたような沈黙――
- TW: 一瞬間，房間裡充斥著茫然無措的沉默——
- VN cũ: 「Xin lỗi nhé. Bố em.\nÔng ấy……là người như vậy đấy.」
- Sửa: Một khoảnh khắc im lặng, như thể không biết phải làm sao――
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1501 (JP: 「済まない。父が。\nあれは……ああいう人なんだ」); fix là bản dịch đúng đang nằm ở key 2213.

### 2172 — Độc thoại — lệch dòng
- JP: ただふくれているだけでなく……\nどこか苦しげなようにも見える。
- TW: 不光是不開心……她的表情看起來甚至有些難受。
- VN cũ: 「Sao vậy, Hibiki?」
- Sửa: Không chỉ giận dỗi thôi đâu……\nTrông con bé còn có vẻ gì đó hơi đau khổ.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1768 (JP: 「どうした、日々姫？」); fix là bản dịch đúng đang nằm ở key 2176.

### 2176 — Độc thoại — lệch dòng
- JP: なんだ、日々姫がふくれてる。
- TW: 不知怎麼回事，日日姬一臉不開心。
- VN cũ: Không chỉ giận dỗi thôi đâu……\nTrông con bé còn có vẻ gì đó hơi đau khổ.
- Sửa: Sao thế này, Hibiki đang phồng má giận dỗi.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2172 (JP: ただふくれているだけでなく……\nどこか苦しげなようにも見える。); fix là bản dịch đúng đang nằm ở key 1700.

### 2180 — Độc thoại — lệch dòng
- JP: ほんの数語。\nただそれだけで、論拠をガタガタに揺すられる。
- TW: 不過三言兩語，我們的論據就已經變得搖搖欲墜。
- VN cũ: Bị dồn vào chân tường bởi chính lời nói của mình, Hibiki cứng họng,\ncon bé nhìn tôi với ánh mắt cầu cứu.
- Sửa: Chỉ với vài lời.\nĐã đủ làm lung lay tận gốc rễ những lập luận của chúng tôi.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2385 (JP: 自身の言葉に追い詰められて、絶句させられ、\n日々姫は僕にすがる視線を向けてくる。); fix là bản dịch đúng đang nằm ở key 1640.

### 2190 — Độc thoại — lệch dòng
- JP: これもまた、反論しがたい事実の指摘だ。
- TW: 他又指出了一個難以反駁的事實。
- VN cũ: Nếu lấy sự suy giảm chất lượng nước không thể đo đếm được làm cái cớ cho việc giảm sút chất lượng sản phẩm,\nthì dù có bị đánh giá là sự yếu kém và dựa dẫm của nhà sản xuất cũng đành chịu.
- Sửa: Lại một sự thật phũ phàng nữa khó lòng phản bác.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2287 (JP: 数値に出ない水の悪化を品質低下の言い訳とするのなら、\n製作者側の甘えや弱さと断じられても仕方ない。); fix là bản dịch đúng đang nằm ở key 2063.

### 2192 — Độc thoại — lệch dòng
- JP: 鼻から短く抜くような息。
- TW: 他用鼻子哼了一聲。
- VN cũ: Khi ông ấy nhún vai,\ntôi mới nhận ra đôi vai đó thật vạm vỡ, trái ngược với thân hình mảnh khảnh.
- Sửa: Một tiếng thở hắt ra từ mũi.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2195 (JP: 竦められればその肩が、\n細身によらず、分厚いものだと気付かされる。); fix là bản dịch đúng đang nằm ở key 1637.

### 2193 — Độc thoại — lệch dòng
- JP: 僕を見る目が鋭く細まる。
- TW: 他眯起眼睛打量我。
- VN cũ: Biểu cảm đó có nét gì đó giống Kisaki,\nkhiến tôi có suy nghĩ thảnh thơi rằng “Quả đúng là cha con”.
- Sửa: Ánh mắt nhìn tôi sắc bén lại.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2572 (JP: その表情が稀咲とどこか似通っていて、\n“親子なのだな”と、のんきなことを感じてしまう。); fix là bản dịch đúng đang nằm ở key 1681.

### 2195 — Độc thoại — lệch dòng
- JP: 竦められればその肩が、\n細身によらず、分厚いものだと気付かされる。
- TW: 他聳了聳瘦削的肩膀，但這個舉動卻讓我感到有種沉重的分量。
- VN cũ: 「Nếu vậy thì tất cả đều là di vật của quá khứ.\nKhông thể dẫn đến sự phục hưng của Ohito được đâu.」
- Sửa: Khi ông ấy nhún vai,\ntôi mới nhận ra đôi vai đó thật vạm vỡ, trái ngược với thân hình mảnh khảnh.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1551 (JP: 「それなら全てが、過去の遺物だ。\n御一夜の再生には繋がらんよ」); fix là bản dịch đúng đang nằm ở key 2192.

### 2210 — Độc thoại — lệch dòng
- JP: 鋭い目つきを緩めぬままに、\n元忠氏は稀咲へと向き直る。
- TW: 元忠先生保持著銳利的目光，轉向稀咲。
- VN cũ: 「Kisaki là đứa con gái đáng tự hào của ta.\nNó sẽ giúp ích cho việc lập kế hoạch kinh doanh đấy.」
- Sửa: Vẫn giữ nguyên ánh mắt sắc bén,\nbác Mototada quay sang Kisaki.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1931 (JP: 「稀咲は私の自慢の娘だ。\n経営計画の立案には役に立つ」); fix là bản dịch đúng đang nằm ở key 1245.

### 2211 — Độc thoại — lệch dòng
- JP: ニヤリと笑い、元忠氏の手がその顎を撫ぜる。
- TW: 元忠先生咧嘴一笑，伸手摸了摸下巴。
- VN cũ: 「Vậy thì hãy cạnh tranh xem bên nào ưu việt hơn đi. Một cuộc chiến.」
- Sửa: Bác Mototada cười nhếch mép, đưa tay vuốt cằm.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2008 (JP: 「ならば優劣を競おうではないか。闘争だ」); fix là bản dịch đúng đang nằm ở key 1636.

### 2213 — Độc thoại — lệch dòng
- JP: 一方的に話を打ち切り、\n来た時同様、いきなり元忠氏は部屋を出て行く。
- TW: 元忠先生突然單方面結束話題，徑直走出了房間。跟他來的時候如出一轍。
- VN cũ: Một khoảnh khắc im lặng, như thể không biết phải làm sao――
- Sửa: Đơn phương cắt đứt cuộc nói chuyện,\nbác Mototada đột ngột rời khỏi phòng y như lúc mới đến.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2162 (JP: 一瞬の、途方にくれたような沈黙――); fix là bản dịch đúng đang nằm ở key 2628.

### 2214 — Độc thoại — lệch dòng
- JP: 言って、元忠氏は僕へ向く。\nその目にはもう、先程までの鋭さは無い。
- TW: 元忠先生說完便轉向我，目光中已經沒有了先前逼人的銳氣。
- VN cũ: 「Ta nghĩ thế này, Soutetsu. Bản tính của một con người,\ncó thể nhìn thấu qua cách họ sử dụng tiền bạc và con người.」
- Sửa: Nói rồi, bác Mototada quay sang tôi.\nTrong ánh mắt ấy không còn sự sắc bén như lúc nãy nữa.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2057 (JP: 「私はね、双鉄くん。その人間の本性は、\n金の使い方と、人の使い方から見えると思っている」); fix là bản dịch đúng đang nằm ở key 1793.

### 2257 — Độc thoại — lệch dòng
- JP: まっすぐに、\n真っ白い手が伸びてくる。
- TW: 她向我伸出了雪白的手。
- VN cũ: 「Một khi đằng nào cũng mang lại lợi ích cho ngân hàng,\nem sẽ toàn tâm toàn ý, dốc hết sức hợp tác với anh.」
- Sửa: Một bàn tay trắng ngần,\nđưa thẳng về phía tôi.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1820 (JP: 「どう転んでも銀行の利益になる以上、\nボクも心置きなく、全力で君に協力しよう」); fix là bản dịch đúng đang nằm ở key 1679.

### 2261 — Độc thoại — lệch dòng
- JP: あからさまなほどの作り笑い。\nそして日々姫は、ごまかすような言葉を重ねる。
- TW: 她擠出了一副明顯是裝出來的笑容，又說起敷衍的話來。
- VN cũ: 「À thì, em chỉ hơi tò mò――chuyện đó――a!\nChuyện bác Mototada, bố của tiền bối Kisaki ấy.」
- Sửa: Một nụ cười gượng gạo lộ liễu.\nVà rồi Hibiki liên tục thốt ra những lời lấp liếm.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1999 (JP: 「ええと、ちょっと気になって――その――あっ！\nあれです、元忠さん、稀咲先輩のお父さん」); fix là bản dịch đúng đang nằm ở key 1630.

### 2273 — Độc thoại — lệch dòng
- JP: 頬をわずかに紅潮させて、\n落ち着かぬ目で僕を、元忠をじゅんじゅんに見る。
- TW: 她的臉頰上泛起一絲紅暈，用不知所措的目光來回望著我和元忠先生。
- VN cũ: 「……Bố đang nói với tư cách là Bố, hay là Chủ tịch vậy?」
- Sửa: Đôi má hơi ửng hồng,\ncô ấy nhìn tôi rồi lại nhìn bác Mototada bằng ánh mắt bất an.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1256 (JP: 「……父と、頭取、どっちの立場で」); fix là bản dịch đúng đang nằm ở key 2490.

### 2274 — Độc thoại — lệch dòng
- JP: 虚を突かれたと、そんな表情。
- TW: 她的表情似乎證實了我正好戳到點子上了。
- VN cũ: Kisaki chớp mắt vài lần,\nrồi từ từ thốt lên bằng một giọng như mất hết sức lực.
- Sửa: Vẻ mặt như thể bị đánh trúng điểm yếu.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2480 (JP: 稀咲はなんどかまばたきをして、\nそれからゆっくり、脱力したような声を出す。); fix là bản dịch đúng đang nằm ở key 1648.

### 2282 — Độc thoại — lệch dòng
- JP: 話が通じた喜びに、\nいささか焦りすぎてしまった。
- TW: 好不容易跟她講通道理，讓我不由有些冒進了。
- VN cũ: Kisaki cười khổ,\nđưa tay vân vê lọn tóc dài của mình.
- Sửa: Vui mừng vì đã tìm được tiếng nói chung,\ntôi có hơi vội vàng quá.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2506 (JP: 稀咲は苦笑し、\nその長い髪の毛先をつまんで、指先で弄る。); fix là bản dịch đúng đang nằm ở key 1639.

### 2285 — Độc thoại — lệch dòng
- JP: その信頼が壊れてしまえば――\n例えば発行元の国が破綻してしまったなら、通貨も破綻だ。
- TW: 如果信任關係崩塌了——比如發行國家破產，貨幣也就失去了作用。
- VN cũ: Những tờ tiền giấy ngày hôm qua sẽ biến thành giấy lộn, và chỉ có ngoại tệ, vàng bạc hay đá quý\nmới có thể đổi lấy một mẩu bánh mì.
- Sửa: Nếu niềm tin đó bị phá vỡ――\nVí dụ như quốc gia phát hành bị phá sản, thì tiền tệ cũng sẽ sụp đổ.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2393 (JP: 昨日までの紙幣が紙切れになり、外貨や金や宝石でしか、\nパンの一枚さえも手に入れられなくなってしまう。); fix là bản dịch đúng đang nằm ở key 1816.

### 2287 — Độc thoại — lệch dòng
- JP: 数値に出ない水の悪化を品質低下の言い訳とするのなら、\n製作者側の甘えや弱さと断じられても仕方ない。
- TW: 如果我們生產者拿無法用數字衡量的水資源惡化當做品質下降的藉口，就算被人指責思想天真、能力不足也無話可說。
- VN cũ: 「Để ta hỏi ngược lại cậu. Shochu Kuma,\nlà loại rượu dễ dàng bị hủy hoại chỉ vì một giọt nước bị vấy bẩn sao?」
- Sửa: Nếu lấy sự suy giảm chất lượng nước không thể đo đếm được làm cái cớ cho việc giảm sút chất lượng sản phẩm,\nthì dù có bị đánh giá là sự yếu kém và dựa dẫm của nhà sản xuất cũng đành chịu.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1815 (JP: 「逆に聞こう。クマ焼酎とは、\n水の一滴を損ねることで、壊れてしまう程度の酒かね？」); fix là bản dịch đúng đang nằm ở key 2190.

### 2288 — Độc thoại — lệch dòng
- JP: お金を信頼と言い換えたなら、宝生稀咲の価値観を、\nより深く理解できそうにも――ああ、いや。
- TW: 如果把金錢換成信任，那麼我也能更進一步理解寶生稀咲的價值觀——啊，對了。
- VN cũ: 「Đúng rồi……nói cách khác, nó gần như là một.」
- Sửa: Nếu thay chữ tiền bằng chữ niềm tin, tôi cảm thấy mình có thể hiểu sâu sắc hơn\nvề giá trị quan của Houshou Kisaki――à, khoan đã.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1743 (JP: 「そうだ……言い換えれば、ほとんど同じことなのだ」); fix là bản dịch đúng đang nằm ở key 1573.

### 2291 — Độc thoại — lệch dòng
- JP: そうして研磨される強さもあろうが、\n今の御一夜に求めるべきが、それであるとは思えない。
- TW: 如此磨礪而來的強大當然也有其價值，但我覺得，現在的御一夜需要的並不是它。
- VN cũ: 「Mục tiêu của bác chắc chắn không phải là việc mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;.\nViệc mời gọi nhà máy chỉ là phương tiện để phục hưng Ohito và chấn hưng kinh tế thôi, đúng không ạ.」
- Sửa: Có thể sự mạnh mẽ được rèn giũa qua đó cũng tốt,\nnhưng tôi không nghĩ đó là điều Ohito cần lúc này.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1775 (JP: 「あなたの目標とて、\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致自体ではない筈だ。\n誘致はあくまで); fix là bản dịch đúng đang nằm ở key 2599.

### 2297 — Độc thoại — lệch dòng
- JP: 宝生元忠の目がまた細まり、僕をじっくり眺め回す。
- TW: 寶生元忠再次眯起眼睛，細細打量起我。
- VN cũ: 「……Đúng như ta đã nói.\nNếu là loại rượu vừa rẻ vừa ngon, ta cũng rất sẵn lòng thưởng thức.」
- Sửa: Đôi mắt của Houshou Mototada lại nheo lại, quan sát tôi thật kỹ.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1245 (JP: 「……言ったとおりだ。\n安くて旨い酒ならば、私も喜んで飲む」); fix là bản dịch đúng đang nằm ở key 1912.

### 2298 — Độc thoại — lệch dòng
- JP: 面白がるような稀咲の一声。\nほんの一瞬、不愉快そうに宝生元忠の眉根が寄る。
- TW: 寶生元忠聽到稀咲這一聲感嘆，一瞬間將眉頭皺了起來，顯得有些不快。
- VN cũ: 「Nhưng mà, Ohito đang khốn khó.\nDù là rượu rẻ tiền, nếu không có nó thì sẽ chết khát mất.」
- Sửa: Một tiếng kêu như thích thú của Kisaki.\nTrong một khoảnh khắc ngắn ngủi, Houshou Mototada nhíu mày vẻ khó chịu.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1549 (JP: 「しかしだ、御一夜は困窮している。\n安酒であれ、それがなければ渇ききるほどに」); fix là bản dịch đúng đang nằm ở key 1749.

### 2300 — Độc thoại — lệch dòng
- JP: 思惑通りにことを運んだのは、宝生元忠一人ではない。
- TW: 對此正中下懷的，並非只有寶生元忠一個人。
- VN cũ: Cả chúng ta nữa, nếu có thể lập ra một kế hoạch tái thiết ưu việt hơn,\nthì việc mời gọi nhà máy sẽ bị rút lại――chúng ta đã có được lời hứa hẹn tương đương như vậy.
- Sửa: Người đã hành động đúng như toan tính, không chỉ có mình Houshou Mototada.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2321 (JP: 僕らとて、より優れた再生計画を立案できれば、\n工場誘致を撤回すると――それに等しい言質を得たのだ。); fix là bản dịch đúng đang nằm ở key 1652.

### 2302 — Độc thoại — lệch dòng
- JP: それがなくとも、向き合ってみたい。\n宝生元忠の厳しい指摘で、自分を洗って、計ってみたい。
- TW: 就算她沒有求助我，我也要直接面對寶生元忠。我要借他不留情面的駁斥來試探自己的能力。
- VN cũ: 「Tuy nhiên, việc làm ô nhiễm nguồn nước không mang lại lợi ích gì cho chúng cháu.\nNgược lại, dù không thấy ngay trước mắt, nhưng rủi ro về lâu dài là rất lớn.」
- Sửa: Dù không có ánh mắt đó, tôi vẫn muốn đối mặt.\nTôi muốn thử thách và mài giũa bản thân bằng những lời chỉ trích sắc bén của Houshou Mototada.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1540 (JP: 「ですが、僕らには水を汚すメリットは無い。\n反面、すぐに見えずとも、長期的なリスクは大きい」); fix là bản dịch đúng đang nằm ở key 1777.

### 2321 — Độc thoại — lệch dòng
- JP: 僕らとて、より優れた再生計画を立案できれば、\n工場誘致を撤回すると――それに等しい言質を得たのだ。
- TW: 我們也得到了他的承諾——只要我們能擬定一個更好的振興方案，就撤回工廠落戶計劃。
- VN cũ: 「Thêm vào đó, Houshou Kisaki――còn có được sự giúp đỡ của em nữa.\nNếu nói về được mất, anh nghĩ điểm số của chúng ta còn cao hơn đấy.」
- Sửa: Cả chúng ta nữa, nếu có thể lập ra một kế hoạch tái thiết ưu việt hơn,\nthì việc mời gọi nhà máy sẽ bị rút lại――chúng ta đã có được lời hứa hẹn tương đương như vậy.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1945 (JP: 「それに加えて、宝生稀咲――君の助力まで得られるのだ。\n損得でいえば、むしろ僕らの得点の方が多いと思う」); fix là bản dịch đúng đang nằm ở key 2300.

### 2322 — Độc thoại — lệch dòng
- JP: 失われるもの。\n誇り、伝統――そうしたものが支える自信。
- TW: 我們會遺失掉的，就是驕傲、傳統——以及它們帶給我們的自信。
- VN cũ: Đúng là như vậy, nhưng……
- Sửa: Thứ bị đánh mất.\nNiềm tự hào, truyền thống――và sự tự tin được xây đắp từ những điều đó.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2557 (JP: それは確かにそうなのだけれど……); fix là bản dịch đúng đang nằm ở key 1543.

### 2323 — Độc thoại — lệch dòng
- JP: 短い握手。\n力強い。
- TW: 我們短而用力地握了握手。
- VN cũ: Không biết có phải do cho quá nhiều Tabasco vào pizza không,\nnhưng tay Kisaki hơi rịn mồ hôi và ẩm ướt.
- Sửa: Một cái bắt tay ngắn ngủi.\nNhưng đầy mạnh mẽ.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2337 (JP: ピザにタバスコをかけすぎたのか、\n稀咲の手は、少し汗ばんでしっとりしている。); fix là bản dịch đúng đang nằm ở key 1787.

### 2325 — Độc thoại — lệch dòng
- JP: \x%lエアクラ;#00ffc040;エアクラ%l;#;社員――浦上の方をちらりと見れば、\n聞こえないわけもなかろうに、表情はまるで変化してない。
- TW: 我偷偷瞟了一眼在\x%lエアクラ;#00ffc040;空凝機%l;#;公司工作的浦上，從那裡不可能聽不到我們的對話——但我卻沒有看到絲毫的表情變化。
- VN cũ: 「Nếu có loại rượu vừa rẻ vừa ngon,\nthì ta cũng muốn nếm thử xem sao.」
- Sửa: Nhân viên của \x%lエアクラ;#00ffc040;Aircra%l;#;――Tôi liếc nhìn về phía anh Uragami,\nchắc chắn anh ấy nghe thấy, nhưng biểu cảm không hề thay đổi.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1715 (JP: 「安くて旨い酒があるなら、\n私にも飲ませて欲しいものだ」); fix là bản dịch đúng đang nằm ở key 2334.

### 2334 — Độc thoại — lệch dòng
- JP: 随分なことを言うなと、他人ごとながら心配になる。
- TW: 我多管閒事地心想，他這樣口無遮攔真得好嗎。
- VN cũ: Nhân viên của \x%lエアクラ;#00ffc040;Aircra%l;#;――Tôi liếc nhìn về phía anh Uragami,\nchắc chắn anh ấy nghe thấy, nhưng biểu cảm không hề thay đổi.
- Sửa: Nói nặng lời quá, dù là chuyện của người khác nhưng tôi vẫn thấy lo.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2325 (JP: \x%lエアクラ;#00ffc040;エアクラ%l;#;社員――浦上の方をちらりと見れば、\n聞こえないわけもなかろうに); fix là bản dịch đúng đang nằm ở key 2627.

### 2337 — Độc thoại — lệch dòng
- JP: ピザにタバスコをかけすぎたのか、\n稀咲の手は、少し汗ばんでしっとりしている。
- TW: 我感到稀咲的手上滲出了一些汗，難道是因為她往披薩上加太多辣椒醬了嗎。
- VN cũ: 「Thế? \nCụ thể thì kế hoạch của các anh tiến triển đến đâu rồi?」
- Sửa: Không biết có phải do cho quá nhiều Tabasco vào pizza không,\nnhưng tay Kisaki hơi rịn mồ hôi và ẩm ướt.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1804 (JP: 「で？　\n具体的に、君たちの計画はどの程度進んでいるんだい？」); fix là bản dịch đúng đang nằm ở key 2323.

### 2338 — Độc thoại — lệch dòng
- JP: 試されてると、強く感じる。\n同時に自問を植え付けられる。
- TW: 我感受到，自己在被試探。同時，這份壓力讓我不禁叩問自己。
- VN cũ: Rốt cuộc, một kẻ như tôi,\nsẽ đối xử với tiền bạc, với con người như thế nào?
- Sửa: Tôi cảm nhận rõ ràng mình đang bị thử thách.\nĐồng thời, một câu hỏi tự vấn được gieo vào tâm trí tôi.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2354 (JP: いったい、僕という人間は、\nどのようにして、金を、人を、扱うのだろう？); fix là bản dịch đúng đang nằm ở key 1961.

### 2341 — Độc thoại — lệch dòng
- JP: 稀咲と話したひと通り、そのままを伝え終えればすぐさま、\n宝生元忠はズバリと言い切る。
- TW: 我把對稀咲說的話原原本本對寶生元忠說了一遍，他便毫不猶豫地斷言道。
- VN cũ: 「Người mua không quan tâm đến môi trường nước đâu.\nTiêu chí để họ quyết định mua chỉ là ngon hay dở, đắt hay rẻ mà thôi.」
- Sửa: Ngay sau khi tôi kể lại toàn bộ câu chuyện đã nói với Kisaki,\nHoushou Mototada thẳng thừng tuyên bố.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1965 (JP: 「水環境のことなど、買い手は気にせんよ。\n購買の判断基準は、旨いまずいと、高い安いとだけだ」); fix là bản dịch đúng đang nằm ở key 1223.

### 2346 — Độc thoại — lệch dòng
- JP: まっすぐに見て、\nただまっすぐに言葉を伝える。
- TW: 我目不轉睛地直視她，將我想說的話盡數傾吐而出。
- VN cũ: 「Một yên đối với ngân hàng,\ncũng giống như một giọt nước sông Kuma đối với xưởng nấu shochu vậy.」
- Sửa: Nhìn thẳng vào cô ấy,\ntôi truyền đạt những lời muốn nói một cách trực diện.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2052 (JP: 「銀行にとっての一円が、\n焼酎酒造にとっては、クマ川の水の一滴なのだ」); fix là bản dịch đúng đang nằm ở key 1741.

### 2354 — Độc thoại — lệch dòng
- JP: いったい、僕という人間は、\nどのようにして、金を、人を、扱うのだろう？
- TW: 我這個人，到底是怎樣用錢、怎樣用人的呢？
- VN cũ: 「Ồ――đến giờ rồi. Một cuộc nói chuyện thú vị. Cảm ơn nhé.」
- Sửa: Rốt cuộc, một kẻ như tôi,\nsẽ đối xử với tiền bạc, với con người như thế nào?
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1623 (JP: 「と――時間だ。面白い話ができた。感謝する」); fix là bản dịch đúng đang nằm ở key 2338.

### 2379 — Độc thoại — lệch dòng
- JP: 理解したのか、\n日々姫の目がキラキラ輝き、丸くなってく。
- TW: 日日姬似乎理解了稀咲的意思，雙眼瞪得圓溜溜的，甚至還在閃閃發光。
- VN cũ: 「Nhưng, thế nhưng――cũng giống nhau thôi. Tờ một vạn yên thật,\ndù được in ấn đẹp đẽ……thì rốt cuộc cũng chỉ là một mảnh giấy.」
- Sửa: Dường như đã hiểu ra,\nđôi mắt Hibiki sáng long lanh và mở to.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1539 (JP: 「でも、だけど――同じ。本物の一万円札も、\n綺麗に印刷されてはいるけど……やっぱり、紙切れ」); fix là bản dịch đúng đang nằm ở key 1687.

### 2385 — Độc thoại — lệch dòng
- JP: 自身の言葉に追い詰められて、絶句させられ、\n日々姫は僕にすがる視線を向けてくる。
- TW: 日日姬被自己的話弄得無話可說，向我投來求助的目光。
- VN cũ: 「Cháu nghĩ những gì bác nói hoàn toàn chính xác.」
- Sửa: Bị dồn vào chân tường bởi chính lời nói của mình, Hibiki cứng họng,\ncon bé nhìn tôi với ánh mắt cầu cứu.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1777 (JP: 「確かに、ご主張の点はその通りかと思います」); fix là bản dịch đúng đang nằm ở key 2180.

### 2387 — Độc thoại — lệch dòng
- JP: 日々姫の首が大きく傾ぐ。
- TW: 日日姬誇張地歪了歪腦袋。
- VN cũ: Thấy vậy, Kisaki lấy ra một tờ một vạn yên từ trong ví,\nsau đó viết "Một vạn yên" lên một tờ giấy nhớ.
- Sửa: Hibiki nghiêng đầu vẻ khó hiểu.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2508 (JP: それを見、稀咲は財布から一万円札を出し、\n次いで、メモ用紙の一枚に「一万円」と書く。); fix là bản dịch đúng đang nằm ở key 1672.

### 2391 — Độc thoại — lệch dòng
- JP: 驚きに、日々姫の目が丸くなる。\n稀咲の顔には正反対に、安堵の色が滲み始める。
- TW: 日日姬驚訝得眼睛都瞪圓了。稀咲則與之相反，露出了放心的表情。
- VN cũ: 「Anh hai――ưm――anh trai.\nAnh đã biết thế rồi, tại sao còn...」
- Sửa: Hibiki tròn mắt ngạc nhiên.\nTrái ngược với con bé, vẻ nhẹ nhõm bắt đầu lan tỏa trên khuôn mặt Kisaki.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2048 (JP: 「にぃに――んっ――兄さん。\nそれがわかっているなら、なんで」); fix là bản dịch đúng đang nằm ở key 1624.

### 2393 — Độc thoại — lệch dòng
- JP: 昨日までの紙幣が紙切れになり、外貨や金や宝石でしか、\nパンの一枚さえも手に入れられなくなってしまう。
- TW: 昨天為止還能當做錢用的紙幣就會變成廢紙，哪怕一塊麵包，都只能用外幣、金子和寶石來交換。
- VN cũ: 「Ngân hàng là nơi xử lý niềm tin dưới hình thức tiền bạc.\nThế nên, dù chỉ là một yên, cũng không thể làm tổn hại đến nó được.」
- Sửa: Những tờ tiền giấy ngày hôm qua sẽ biến thành giấy lộn, và chỉ có ngoại tệ, vàng bạc hay đá quý\nmới có thể đổi lấy một mẩu bánh mì.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2036 (JP: 「銀行は、お金という形の信頼を扱っている場所だ。\nだから仮に一円だろうと、それを損ねることは出来ない」); fix là bản dịch đúng đang nằm ở key 2285.

### 2480 — Độc thoại — lệch dòng
- JP: 稀咲はなんどかまばたきをして、\nそれからゆっくり、脱力したような声を出す。
- TW: 稀咲就像突然洩了氣一樣，眨了好幾次眼睛，然後才慢慢發出聲音。
- VN cũ: 「A……ra vậy. Ra là thế. Ra là thế――\nĐó là điều không thể nhượng bộ, nhỉ.」
- Sửa: Kisaki chớp mắt vài lần,\nrồi từ từ thốt lên bằng một giọng như mất hết sức lực.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1644 (JP: 「あー……そうか。なるほど。なるほど――\nそれは、譲れないところだ、ね」); fix là bản dịch đúng đang nằm ở key 2274.

### 2482 — Độc thoại — lệch dòng
- JP: 稀咲は眼下から視線を外し、僕へと真っ直ぐ向け直す。
- TW: 稀咲抬起頭，直直地看向我。
- VN cũ: 「Tiền là thù lao cho sức lao động――câu trả lời của Soutetsu chắc chắn là đúng.\nNhưng hơn thế nữa, em cho rằng tiền chính là niềm tin.」
- Sửa: Kisaki rời mắt khỏi tầng dưới, nhìn thẳng vào tôi.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2023 (JP: 「お金は労働の対価だと――双鉄の答えは、確かに正しい。\nその上で僕は。お金とは、信頼そのものだとも考える」); fix là bản dịch đúng đang nằm ở key 1896.

### 2490 — Độc thoại — lệch dòng
- JP: 稀咲は、明らかに動揺している。
- TW: 稀咲明顯有些動搖。
- VN cũ: Đôi má hơi ửng hồng,\ncô ấy nhìn tôi rồi lại nhìn bác Mototada bằng ánh mắt bất an.
- Sửa: Kisaki rõ ràng đang dao động.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2273 (JP: 頬をわずかに紅潮させて、\n落ち着かぬ目で僕を、元忠をじゅんじゅんに見る。); fix là bản dịch đúng đang nằm ở key 1983.

### 2494 — Độc thoại — lệch dòng
- JP: 怪訝そうな日々姫の言葉に答える稀咲はにこやかだ。
- TW: 稀咲用微笑回應日日姬驚訝的話。
- VN cũ: 「Tại sao lại là đương nhiên chứ.」
- Sửa: Kisaki mỉm cười đáp lại lời nói đầy vẻ hoài nghi của Hibiki.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1880 (JP: 「何故、当たり前なのかな」); fix là bản dịch đúng đang nằm ở key 1985.

### 2504 — Độc thoại — lệch dòng
- JP: ゆっくり、深く。\n稀咲が頷く。
- TW: 稀咲緩緩地用力點頭。
- VN cũ: 「Không ai dùng đâu, một ngân hàng như thế.\nVậy nên……shochu mà không bảo vệ nổi nguồn nước, thì sẽ không còn ai uống nữa?」
- Sửa: Chậm rãi, sâu sắc.\nKisaki gật đầu.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1864 (JP: 「使わないね、そんな銀行。\nだから……水も守れない焼酎は、飲まれなくなる？」); fix là bản dịch đúng đang nằm ở key 1799.

### 2506 — Độc thoại — lệch dòng
- JP: 稀咲は苦笑し、\nその長い髪の毛先をつまんで、指先で弄る。
- TW: 稀咲苦笑起來，用指尖撥了撥長長的秀髮。
- VN cũ: 「……Trước mắt thì……tóm lại, hãy để em đưa ra những con số cụ thể.\nTrong trường hợp đánh mất thương hiệu shochu Kuma――」
- Sửa: Kisaki cười khổ,\nđưa tay vân vê lọn tóc dài của mình.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1260 (JP: 「……ひとまずは……とにかく、数字を出させて欲しい。\nクマ焼酎というブランドを逸失してしまった場合――」); fix là bản dịch đúng đang nằm ở key 2282.

### 2508 — Độc thoại — lệch dòng
- JP: それを見、稀咲は財布から一万円札を出し、\n次いで、メモ用紙の一枚に「一万円」と書く。
- TW: 稀咲見狀，從錢包中取出一張一萬日元紙幣，隨後在一張紙上寫下“一萬日元”。
- VN cũ: 「Cả hai tờ này đều là tờ một vạn yên. Một tờ do Ngân hàng Hinomoto phát hành,\nvà một tờ do cá nhân Houshou Kisaki phát hành.」
- Sửa: Thấy vậy, Kisaki lấy ra một tờ một vạn yên từ trong ví,\nsau đó viết "Một vạn yên" lên một tờ giấy nhớ.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1987 (JP: 「これは、両方とも一万円札だ。日ノ本銀行発行のものと、\n宝生稀咲、個人が発行したものと」); fix là bản dịch đúng đang nằm ở key 2387.

### 2511 — Độc thoại — lệch dòng
- JP: 稀咲は全く変わらぬ様子で、\n宝生元忠を静かに見据える。
- TW: 稀咲面不改色地靜靜注視著他。
- VN cũ: 「Phản đối?」
- Sửa: Kisaki vẫn giữ vẻ mặt điềm nhiên,\nlặng lẽ nhìn chằm chằm vào Houshou Mototada.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1604 (JP: 「異議とは？」); fix là bản dịch đúng đang nằm ở key 2161.

### 2527 — Độc thoại — lệch dòng
- JP: 勢いこんだ日々姫の言葉に、稀咲も頷く。\n僕とて、そこには同感だ。
- TW: 聽了日日姬激動的話，稀咲也點了點頭。這句話就連我也同意。
- VN cũ: 「Đúng là vậy. Dù kết quả có ra sao, bác Mototada cũng không thiệt thòi.\nCho dù chúng ta có lập được kế hoạch tái thiết tốt hay không.」
- Sửa: Kisaki gật đầu đồng tình với lời nói hùng hồn của Hibiki.\nTôi cũng đồng tình với điều đó.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1826 (JP: 「確かにな。どう転んでも、元忠氏は損をしない。\n僕らが上手い再建計画を立案できても、そうでなくても」); fix là bản dịch đúng đang nằm ở key 2050.

### 2530 — Độc thoại — lệch dòng
- JP: 首から順に、まるでスプレーを吹き上げるように。\n稀咲の顔が、じわじわ、目に見えて赤くなる。
- TW: 能夠明顯看到，紅暈慢慢從稀咲的脖子爬上了整張臉，讓她的臉越來越紅。
- VN cũ: 「T-tiền bối?」
- Sửa: Bắt đầu từ cổ, giống như có ai đó đang phun sơn vậy.\nKhuôn mặt Kisaki dần dần, thấy rõ là đang đỏ bừng lên.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1730 (JP: 「せ、先輩？」); fix là bản dịch đúng đang nằm ở key 1614.

### 2557 — Độc thoại — lệch dòng
- JP: それは確かにそうなのだけれど……
- TW: 話是這麼說沒錯，但是……
- VN cũ: 「Nếu chỉ vì không bảo vệ được một giọt nước mà làm giảm hương vị,\nthì shochu Kuma suy cho cùng cũng chỉ là loại rượu tầm thường thôi.」
- Sửa: Đúng là như vậy, nhưng……
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1719 (JP: 「一滴の水を守れぬことから、味が落ちるというのなら、\nクマ焼酎は、所詮そのレベルの酒とも言えるだろう」); fix là bản dịch đúng đang nằm ở key 2322.

### 2570 — Độc thoại — lệch dòng
- JP: 是非も無い。\nが、答え方には気をつける。
- TW: 這是自然的。但我還是字斟句酌地回答。
- VN cũ: 「Nếu nhận được sự giúp đỡ của Kisaki,\ncháu sẽ vô cùng biết ơn ạ.」
- Sửa: Điều đó là đương nhiên.\nNhưng tôi vẫn cẩn thận trong cách trả lời.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1726 (JP: 「稀咲さんのご助力をいただけるなら、\n極めてありがたく思います」); fix là bản dịch đúng đang nằm ở key 2056.

### 2571 — Độc thoại — lệch dòng
- JP: そういうことなら共感できる――\n思った瞬間、さっきの自分が恥ずかしくなる。
- TW: 這樣一來我也能理解她的想法——產生這種想法的瞬間，我就為自己剛才的態度感到難為情。
- VN cũ: 「Xin lỗi vì thái độ lúc nãy của anh. Chưa hiểu rõ ý nghĩa thực sự trong lời nói của em,\nchỉ nghe nói tiền quan trọng, anh đã hiểu lầm em là một kẻ hám tiền.」
- Sửa: Nếu là vậy thì tôi hoàn toàn có thể đồng cảm――\nNghĩ đến đây, tôi chợt thấy xấu hổ về bản thân lúc nãy.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1503 (JP: 「すまない態度を見せてしまった。言葉の真意もわからず、\n金が大事と聞いただけで、君を守銭奴のように誤解した」); fix là bản dịch đúng đang nằm ở key 1584.

### 2572 — Độc thoại — lệch dòng
- JP: その表情が稀咲とどこか似通っていて、\n“親子なのだな”と、のんきなことを感じてしまう。
- TW: 這表情和稀咲的有幾分神似，讓我不禁心想“真是有其父必有其女”。
- VN cũ: 「Mượn ví dụ lúc nãy của bác, thì đó là 『loại rượu không ngon nhưng rẻ』.\nĐại đa số người dân Ohito đều coi việc mời gọi nhà máy là như vậy.」
- Sửa: Biểu cảm đó có nét gì đó giống Kisaki,\nkhiến tôi có suy nghĩ thảnh thơi rằng “Quả đúng là cha con”.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1749 (JP: 「さっきの例えを借りるなら、『旨くはないが安い酒』。\n御一夜市民の大多数は、工場誘致をそう捉えている」); fix là bản dịch đúng đang nằm ở key 2193.

### 2581 — Độc thoại — lệch dòng
- JP: 乱暴な――叩きつけるようなノックの音。\n稀咲の肩がビクリと動く。
- TW: 門口傳來粗魯的捶門聲，嚇得稀咲肩膀一顫。
- VN cũ: 「Bố――à không, Chủ tịch!?」
- Sửa: Tiếng gõ cửa thô bạo――như thể đang đập cửa.\nVai Kisaki giật nảy lên.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 1887 (JP: 「父さ――と、頭取っ！？」); fix là bản dịch đúng đang nằm ở key 2631.

### 2599 — Độc thoại — lệch dòng
- JP: ぶつかりあって、劣った方が飲み込まれる。
- TW: 雙方互相競爭，最後劣勢的一方被吞併。
- VN cũ: Có thể sự mạnh mẽ được rèn giũa qua đó cũng tốt,\nnhưng tôi không nghĩ đó là điều Ohito cần lúc này.
- Sửa: Đối đầu với nhau, và kẻ yếu hơn sẽ bị nuốt chửng.
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2291 (JP: そうして研磨される強さもあろうが、\n今の御一夜に求めるべきが、それであるとは思えない。); fix là bản dịch đúng đang nằm ở key 1833.

### 2627 — Độc thoại — lệch dòng
- JP: （おお）
- TW: （哦哦）
- VN cũ: Nói nặng lời quá, dù là chuyện của người khác nhưng tôi vẫn thấy lo.
- Sửa: （Ồ.）
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2334 (JP: 随分なことを言うなと、他人ごとながら心配になる。); fix là bản dịch đúng đang nằm ở key 1549.

### 2628 — Độc thoại — lệch dòng
- JP: （バタンっ）
- TW: （喀噠）
- VN cũ: Đơn phương cắt đứt cuộc nói chuyện,\nbác Mototada đột ngột rời khỏi phòng y như lúc mới đến.
- Sửa: （Rầm）
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2213 (JP: 一方的に話を打ち切り、\n来た時同様、いきなり元忠氏は部屋を出て行く。); fix là bản dịch đúng đang nằm ở key 1623.

### 2631 — Độc thoại — lệch dòng
- JP: （ゴンッ、ゴンッ）
- TW: （砰、砰）
- VN cũ: Tiếng gõ cửa thô bạo――như thể đang đập cửa.\nVai Kisaki giật nảy lên.
- Sửa: （Cộc cộc）
- Lý do: Lệch dòng (chuỗi xoay): VN cũ là bản dịch của key 2581 (JP: 乱暴な――叩きつけるようなノックの音。\n稀咲の肩がビクリと動く。); fix là bản dịch đúng đang nằm ở key 1260.

## §3. Chuỗi xoay — cách các bản dịch bị xáo trộn

VN của file này không sai ngẫu nhiên mà bị xáo trộn theo chuỗi: bản dịch đúng của dòng A nằm ở dòng B, của dòng B nằm ở dòng C… Có 21 chuỗi dài ≥2, dài nhất 21 mắt xích. Các chuỗi dài nhất:
- 1586 → 1955 → 1804 → 2337 → 2323 → 1787 → 1838 → 1820 → 2257 → 1679 → 1945 → 2321 → 2300 → 1652 → 1689 → 2048 → 2391 → 1624 → 1826 → 2527 → 2050 (→ fix lấy từ 1992)
- 1503 → 2571 → 1584 → 2036 → 2393 → 2285 → 1816 → 1830 → 1809 → 1539 → 2379 → 1687 → 1880 → 2494 → 1985 → 1579 → 1629 → 1987 → 2508 → 2387 (→ fix lấy từ 1672)
- 1501 → 2162 → 2213 → 2628 → 1623 → 2354 → 2338 → 1961 → 1901 → 2057 → 2214 → 1793 → 1702 → 1990 (→ fix lấy từ 1256)
- 1223 → 1234 → 1634 → 1939 → 1798 → 1887 → 2581 → 2631 → 1260 → 2506 → 2282 (→ fix lấy từ 1639)
- 1540 → 2302 → 1777 → 2385 → 2180 → 1640 → 1994 → 2000 → 1815 → 2287 → 2190 (→ fix lấy từ 2063)
- 1549 → 2298 → 1749 → 2572 → 2193 → 1681 → 1783 → 1620 → 1775 → 2291 → 2599 (→ fix lấy từ 1833)
- 1644 → 2480 → 2274 → 1648 → 2052 → 2346 → 1741 → 1743 → 2288 (→ fix lấy từ 1573)
- 1614 → 1886 → 1999 → 2261 → 1630 → 1768 → 2172 → 2176 (→ fix lấy từ 1700)
- 165/178 fix lấy nguyên văn bản dịch đúng đang nằm ở key khác (đã kiểm chứng từng cặp fix↔JP bằng đọc tay + kiểm tra máy: fix bằng đúng VN tại key nguồn trong CSV3). 13 fix còn lại: 3 đại từ (chỉ đổi "chị"→"em", nội dung giữ nguyên), 2 gasp (Ư!), 8 dịch mới (1637, 1639, 1672, 1700, 1833, 1896, 1983, 1992 — bản dịch đúng không còn trong file).
- 13 giá trị VN cũ không được dùng làm fix cho dòng nào: 3 dòng đại từ (1612, 1757, 1805 — VN giữ nguyên, chỉ đổi đại từ) + 10 giá trị ngắn thừa bị loại: 1559 "Không, tốt gì chứ.", 1586 "Đã rõ. ――Hửm?", 1705 "Chuyện đó――", 1711 "Hửm?", 1719 "!", 1730 "…………", 1791 "Thật vậy sao?", 1852 "Hừ.", 1965 "!", 2055 "Ưm……cũng phải." — các giá trị này không phải bản dịch đúng của bất kỳ JP nào trong file (đã kiểm tra bằng quét máy: không có JP nào khớp nghĩa), nên bị bỏ chứ không gán sang dòng khác.
- Hai dòng sweep: 1618 (already-rendered) và 2063 (needs-file-audit) — cả hai thực chất đều là lệch dòng (JP chỉ là 「っ！」, VN cũ là câu độc thoại đầy đủ); đã xử lý: fix "Ư!" cho cả hai, bản dịch độc thoại chuyển về đúng key (1618→2157, 2063→2190). Sweep không có mục nào khác cho file này; quét máy bổ sung không bắt thêm gasp nào (0 dòng VN còn chữ っ thô).

## §4. Khối TOML (đã parse-kiểm chứng)

Khối `[script]` 178 khóa dưới đây đã parse bằng tomllib, 0 sai lệch giá trị so với JSON; jp/tw/old_vn khớp CSV3 tuyệt đối 178/178; 165 fix lệch dòng bằng đúng VN tại key nguồn trong CSV3.

```toml
[script]
"1223" = "……Đáng lẽ đến tìm Kisaki, nhưng ông ấy lại chăm chú lắng nghe tôi nói."
"1234" = "「――Hừm.\\nCó một sự hiểu lầm lớn ở đây.」"
"1245" = "「……Đúng như ta đã nói.\\nNếu là loại rượu vừa rẻ vừa ngon, ta cũng rất sẵn lòng thưởng thức.」"
"1256" = "「……Bố đang nói với tư cách là Bố, hay là Chủ tịch vậy?」"
"1260" = "「……Trước mắt thì……tóm lại, hãy để em đưa ra những con số cụ thể.\\nTrong trường hợp đánh mất thương hiệu shochu Kuma――」"
"1501" = "「Xin lỗi nhé. Bố em.\\nÔng ấy……là người như vậy đấy.」"
"1503" = "「Xin lỗi vì thái độ lúc nãy của anh. Chưa hiểu rõ ý nghĩa thực sự trong lời nói của em,\\nchỉ nghe nói tiền quan trọng, anh đã hiểu lầm em là một kẻ hám tiền.」"
"1539" = "「Nhưng, thế nhưng――cũng giống nhau thôi. Tờ một vạn yên thật,\\ndù được in ấn đẹp đẽ……thì rốt cuộc cũng chỉ là một mảnh giấy.」"
"1540" = "「Tuy nhiên, việc làm ô nhiễm nguồn nước không mang lại lợi ích gì cho chúng cháu.\\nNgược lại, dù không thấy ngay trước mắt, nhưng rủi ro về lâu dài là rất lớn.」"
"1543" = "「Nhưng, xưởng nấu rượu thì có quan tâm.\\nNếu nhượng bộ điểm đó, một thứ gì đó rất quan trọng sẽ bị đánh mất.」"
"1549" = "「Nhưng mà, Ohito đang khốn khó.\\nDù là rượu rẻ tiền, nếu không có nó thì sẽ chết khát mất.」"
"1551" = "「Nếu vậy thì tất cả đều là di vật của quá khứ.\\nKhông thể dẫn đến sự phục hưng của Ohito được đâu.」"
"1557" = "「Với tư cách là Giám đốc chi nhánh,\\ncháu xin phép được phản đối ý kiến đó.」"
"1559" = "「Anh không nghĩ em cần phải xin lỗi đâu.\\nThực tế thì, chúng ta đã có một cuộc thảo luận rất tốt mà.」"
"1566" = "「Cháu định từ giờ sẽ chuẩn bị sao?\\nBằng cách kết hợp suối nước nóng, shochu và cả đường sắt nữa.」"
"1573" = "「Trái lại, em phản đối việc chỉ biết khư khư tích trữ tiền bạc đấy?\\nBởi vì em nghĩ tiền chỉ thực sự là tiền khi nó được lưu thông đúng cách.」"
"1579" = "「Một tờ có thể sử dụng ở khắp mọi nơi trên toàn quốc Hinomoto,\\ncòn một tờ thì không ai coi nó là tiền tệ cả.」"
"1584" = "「Ra là vậy――đó chính là,\\n『giá trị của đồng tiền』 đối với Houshou Kisaki sao.」"
"1585" = "「Tiền là……ra vậy. Niềm tin sao.」"
"1586" = "「Ra là vậy.\\nThế thì, chắc em phải bắt đầu khảo sát từ đó thôi nhỉ.」"
"1604" = "「Phản đối?」"
"1612" = "「Ây da. Là do cách nói của em không tốt rồi.」"
"1614" = "「À thì――a! Đúng rồi,\\nRõ ràng bác ấy đến tìm tiền bối Kisaki để nói chuyện mà――hả!?」"
"1618" = "「Ư!」"
"1620" = "「Haha, vậy là cháu muốn nói điều này sao.\\n『Cháu có một kế hoạch phục hưng Ohito xuất sắc hơn việc mời gọi nhà máy』.」"
"1623" = "「Ồ――đến giờ rồi. Một cuộc nói chuyện thú vị. Cảm ơn nhé.」"
"1624" = "「Hả!?」"
"1629" = "「Hả?」"
"1630" = "「Dạ? À, không có gì đâu!\\nKhông, ưm, không có gì đâu ạ. Em ổn.」"
"1633" = "「Hả? Cái gì mà ra vậy?」"
"1634" = "「Ồ?」"
"1636" = "「Ồ, nếu cháu có ý tưởng khác thì thú vị đấy.」"
"1637" = "「Hừm.」"
"1639" = "「Ừm……ra vậy à.」"
"1640" = "「A――」"
"1644" = "「A……ra vậy. Ra là thế. Ra là thế――\\nĐó là điều không thể nhượng bộ, nhỉ.」"
"1647" = "「A……ừm……\\nKhông sao đâu, nhỉ?」"
"1648" = "「A.」"
"1652" = "「A!」"
"1672" = "「Ừm?」"
"1679" = "「Fufu, vinh hạnh thật.」"
"1681" = "「Ồ.」"
"1687" = "「Bởi vì……tờ giấy tiền bối Kisaki viết tay,\\nchỉ là một mảnh giấy vụn có viết chữ một vạn yên――A.」"
"1689" = "「Vì thực tế thì đó là một thỏa thuận tốt.\\nViệc không bị thiệt thòi, chúng ta cũng hoàn toàn giống nhau mà?」"
"1700" = "「Rõ rồi. ――Hửm?」"
"1702" = "「Vậy sao. Nếu thế thì tôi xin tuân lệnh.」"
"1704" = "「Lợi ích thì có đấy. Nếu thành phố Ohito suy tàn,\\nthì shochu Kuma, chèo thuyền trên sông Kuma hay đường sắt cũng sẽ lụi bại theo.」"
"1705" = "「Vậy thì, Giám đốc chi nhánh Ohito. Việc mời gọi nhà máy cứ để ta lo.\\nCon hãy rút lui khỏi chuyện đó, và tập trung vào phương án khác đi.」"
"1711" = "「Nếu mọi người không tin tưởng vào tiền,\\nthì tiền giấy cũng chỉ là những mảnh giấy vụn mà thôi.」"
"1715" = "「Nếu có loại rượu vừa rẻ vừa ngon,\\nthì ta cũng muốn nếm thử xem sao.」"
"1719" = "「Nếu chỉ vì không bảo vệ được một giọt nước mà làm giảm hương vị,\\nthì shochu Kuma suy cho cùng cũng chỉ là loại rượu tầm thường thôi.」"
"1723" = "「Nếu chỉ lấy ra từng cái một, thì có thể là vậy.\\nNhưng, nếu kết hợp chúng lại, chúng ta có thể tạo ra những giá trị hoàn toàn mới.」"
"1726" = "「Nếu nhận được sự giúp đỡ của Kisaki,\\ncháu sẽ vô cùng biết ơn ạ.」"
"1730" = "「T-tiền bối?」"
"1741" = "「Nghe này, Houshou Kisaki.」"
"1743" = "「Đúng rồi……nói cách khác, nó gần như là một.」"
"1749" = "「Mượn ví dụ lúc nãy của bác, thì đó là 『loại rượu không ngon nhưng rẻ』.\\nĐại đa số người dân Ohito đều coi việc mời gọi nhà máy là như vậy.」"
"1757" = "「Từ phòng này có thể nhìn xuống tầng một. Em từng cho Hibiki xem rồi nhỉ?」"
"1768" = "「Sao vậy, Hibiki?」"
"1775" = "「Mục tiêu của bác chắc chắn không phải là việc mời gọi nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;.\\nViệc mời gọi nhà máy chỉ là phương tiện để phục hưng Ohito và chấn hưng kinh tế thôi, đúng không ạ.」"
"1777" = "「Cháu nghĩ những gì bác nói hoàn toàn chính xác.」"
"1783" = "「Đúng hơn là――\\nCháu cảm thấy việc mời gọi nhà máy không phải là một kế hoạch phục hưng xuất sắc cho lắm.」"
"1785" = "「Việc thành phố Ohito bị chia rẽ là điều không nên.\\nChúng ta cần cố gắng đạt được sự đồng thuận từ càng nhiều người càng tốt――」"
"1787" = "「Em cũng vậy.」"
"1791" = "「Tất nhiên, chúng ta cũng sẽ nỗ lực làm điều đó.\\nNhưng nếu hai bên đều không chịu nhượng bộ, thì chỉ còn cách đối đầu thôi.」"
"1793" = "「Ta mong chờ sự nỗ lực hết mình của con.\\nĐừng làm ta thất vọng đấy nhé?」"
"1796" = "「Anh tin chắc là vậy. Dù không có ảnh hưởng ngay lập tức\\nnhưng dần dần, chắc chắn sẽ xảy ra.」"
"1798" = "「Ta vào được chứ? Có chuyện công việc.」"
"1799" = "「Một ngân hàng không coi trọng và không bảo vệ nổi một yên――\\nthì rốt cuộc sẽ có ai muốn sử dụng chứ, anh nghĩ chuyện này cũng tương tự như vậy.」"
"1804" = "「Thế? \\nCụ thể thì kế hoạch của các anh tiến triển đến đâu rồi?」"
"1805" = "「Bàn bạc công việc chỉ là cái cớ thôi. Em muốn dành thời gian―― để chúng ta có thể nói chuyện sâu hơn một chút.」"
"1809" = "「Một mảnh giấy vụn có thể được lưu thông như một loại tiền tệ, như một vật thay thế cho sức lao động――\\nđó là vì có niềm tin đặt vào nó đúng không?」"
"1815" = "「Để ta hỏi ngược lại cậu. Shochu Kuma,\\nlà loại rượu dễ dàng bị hủy hoại chỉ vì một giọt nước bị vấy bẩn sao?」"
"1816" = "「Nói cách khác, niềm tin vào đơn vị phát hành\\nchính là thứ bảo chứng cho giá trị của tiền tệ sao.」"
"1820" = "「Một khi đằng nào cũng mang lại lợi ích cho ngân hàng,\\nem sẽ toàn tâm toàn ý, dốc hết sức hợp tác với anh.」"
"1826" = "「Đúng là vậy. Dù kết quả có ra sao, bác Mototada cũng không thiệt thòi.\\nCho dù chúng ta có lập được kế hoạch tái thiết tốt hay không.」"
"1830" = "「Ra là vậy. Phiếu mua hàng cũng thế nhỉ.\\nVì biết là dùng được, vì tin tưởng được nên nó không phải là giấy vụn.」"
"1833" = "「Vậy sao ạ?」"
"1838" = "「Đáng tin cậy thật, trăm sự nhờ em nhé.」"
"1852" = "「Đúng như bác nói.\\nĐó là định hướng cơ bản của chúng cháu.」"
"1864" = "「Không ai dùng đâu, một ngân hàng như thế.\\nVậy nên……shochu mà không bảo vệ nổi nguồn nước, thì sẽ không còn ai uống nữa?」"
"1867" = "「Đúng vậy. Dù chỉ nhượng bộ một bước――\\ncũng sẽ phá hủy đi niềm tin mà shochu Kuma đã dày công gây dựng bấy lâu nay.」"
"1880" = "「Tại sao lại là đương nhiên chứ.」"
"1886" = "「Bố em á? Tò mò chuyện gì cơ――」"
"1887" = "「Bố――à không, Chủ tịch!?」"
"1896" = "「Nếu môi trường buông lỏng, con người cũng sẽ buông lỏng theo. Chỉ cần chấp nhận sai số một yên thôi, thì chắc chắn nó sẽ thành mười yên, rồi trăm yên.」"
"1901" = "「Cách sử dụng tiền bạc……và con người, sao ạ.」"
"1912" = "「Kết hợp, nhỉ.」"
"1931" = "「Kisaki là đứa con gái đáng tự hào của ta.\\nNó sẽ giúp ích cho việc lập kế hoạch kinh doanh đấy.」"
"1937" = "「Một cuộc chiến――」"
"1939" = "「Khoan, khoan, đợi một chút đã――\\nHiện tại đang có khách――Hibiki và Soutetsu đang ở đây.」"
"1945" = "「Thêm vào đó, Houshou Kisaki――còn có được sự giúp đỡ của em nữa.\\nNếu nói về được mất, anh nghĩ điểm số của chúng ta còn cao hơn đấy.」"
"1955" = "「Rất tiếc là, hầu như chưa có gì.\\nNgay cả việc tận dụng 8620――đường sắt như thế nào, cũng chưa được xác định.」"
"1961" = "「Hãy cho ta xem đi.\\nBản tính con người cháu.」"
"1965" = "「Người mua không quan tâm đến môi trường nước đâu.\\nTiêu chí để họ quyết định mua chỉ là ngon hay dở, đắt hay rẻ mà thôi.」"
"1983" = "「Đó là――」"
"1985" = "「Chuyện đó……chẳng phải là đương nhiên sao.」"
"1987" = "「Cả hai tờ này đều là tờ một vạn yên. Một tờ do Ngân hàng Hinomoto phát hành,\\nvà một tờ do cá nhân Houshou Kisaki phát hành.」"
"1990" = "「Là mệnh lệnh công việc. Giám đốc chi nhánh.」"
"1991" = "「Nếu vậy……Ohito sẽ đánh mất thương hiệu shochu Kuma.\\nKhoản lợi nhuận bị mất đó――đúng là không thể phớt lờ được.」"
"1992" = "「Không, anh bảo là thảo luận tốt á.」"
"1994" = "「Vậy thì, không có vấn đề gì cả.」"
"1998" = "「Vậy thì, thế nào.\\nChuyện mời gọi nhà máy, em có thể xem xét lại được không.」"
"1999" = "「À thì, em chỉ hơi tò mò――chuyện đó――a!\\nChuyện bác Mototada, bố của tiền bối Kisaki ấy.」"
"2000" = "「Làm gì có chuyện đó!」"
"2008" = "「Vậy thì hãy cạnh tranh xem bên nào ưu việt hơn đi. Một cuộc chiến.」"
"2023" = "「Tiền là thù lao cho sức lao động――câu trả lời của Soutetsu chắc chắn là đúng.\\nNhưng hơn thế nữa, em cho rằng tiền chính là niềm tin.」"
"2036" = "「Ngân hàng là nơi xử lý niềm tin dưới hình thức tiền bạc.\\nThế nên, dù chỉ là một yên, cũng không thể làm tổn hại đến nó được.」"
"2046" = "「Việc ngăn chặn sự suy tàn của thành phố Ohito không liên quan trực tiếp đến việc mời gọi nhà máy.\\nChúng cháu tin rằng có những cách khác để phục hưng Ohito.」"
"2048" = "「Anh hai――ưm――anh trai.\\nAnh đã biết thế rồi, tại sao còn...」"
"2050" = "「Anh hai ngây thơ quá! \\nThế này là trúng kế của ổng rồi còn gì!」"
"2052" = "「Một yên đối với ngân hàng,\\ncũng giống như một giọt nước sông Kuma đối với xưởng nấu shochu vậy.」"
"2053" = "「Cháu không thể chuẩn bị ngay lúc này được.\\nNhưng――」"
"2055" = "「Đừng vội vàng thế, Soutetsu. Chuyện lớn như vậy,\\nmột Giám đốc chi nhánh như em làm sao có thể quyết định ngay được.」"
"2056" = "「Soutetsu, cháu có muốn dùng không?」"
"2057" = "「Ta nghĩ thế này, Soutetsu. Bản tính của một con người,\\ncó thể nhìn thấu qua cách họ sử dụng tiền bạc và con người.」"
"2063" = "「Ư!」"
"2157" = "Tôi không thể nghĩ ra lời phản bác ngay lập tức.\\nĐó quả thực là――một sự thật tàn khốc."
"2161" = "Khoảnh khắc bị áp đảo bởi những lời lẽ mạnh mẽ đó,\\nđã bị phá vỡ bởi một giọng nói lạnh lùng xen vào."
"2162" = "Một khoảnh khắc im lặng, như thể không biết phải làm sao――"
"2172" = "Không chỉ giận dỗi thôi đâu……\\nTrông con bé còn có vẻ gì đó hơi đau khổ."
"2176" = "Sao thế này, Hibiki đang phồng má giận dỗi."
"2180" = "Chỉ với vài lời.\\nĐã đủ làm lung lay tận gốc rễ những lập luận của chúng tôi."
"2190" = "Lại một sự thật phũ phàng nữa khó lòng phản bác."
"2192" = "Một tiếng thở hắt ra từ mũi."
"2193" = "Ánh mắt nhìn tôi sắc bén lại."
"2195" = "Khi ông ấy nhún vai,\\ntôi mới nhận ra đôi vai đó thật vạm vỡ, trái ngược với thân hình mảnh khảnh."
"2210" = "Vẫn giữ nguyên ánh mắt sắc bén,\\nbác Mototada quay sang Kisaki."
"2211" = "Bác Mototada cười nhếch mép, đưa tay vuốt cằm."
"2213" = "Đơn phương cắt đứt cuộc nói chuyện,\\nbác Mototada đột ngột rời khỏi phòng y như lúc mới đến."
"2214" = "Nói rồi, bác Mototada quay sang tôi.\\nTrong ánh mắt ấy không còn sự sắc bén như lúc nãy nữa."
"2257" = "Một bàn tay trắng ngần,\\nđưa thẳng về phía tôi."
"2261" = "Một nụ cười gượng gạo lộ liễu.\\nVà rồi Hibiki liên tục thốt ra những lời lấp liếm."
"2273" = "Đôi má hơi ửng hồng,\\ncô ấy nhìn tôi rồi lại nhìn bác Mototada bằng ánh mắt bất an."
"2274" = "Vẻ mặt như thể bị đánh trúng điểm yếu."
"2282" = "Vui mừng vì đã tìm được tiếng nói chung,\\ntôi có hơi vội vàng quá."
"2285" = "Nếu niềm tin đó bị phá vỡ――\\nVí dụ như quốc gia phát hành bị phá sản, thì tiền tệ cũng sẽ sụp đổ."
"2287" = "Nếu lấy sự suy giảm chất lượng nước không thể đo đếm được làm cái cớ cho việc giảm sút chất lượng sản phẩm,\\nthì dù có bị đánh giá là sự yếu kém và dựa dẫm của nhà sản xuất cũng đành chịu."
"2288" = "Nếu thay chữ tiền bằng chữ niềm tin, tôi cảm thấy mình có thể hiểu sâu sắc hơn\\nvề giá trị quan của Houshou Kisaki――à, khoan đã."
"2291" = "Có thể sự mạnh mẽ được rèn giũa qua đó cũng tốt,\\nnhưng tôi không nghĩ đó là điều Ohito cần lúc này."
"2297" = "Đôi mắt của Houshou Mototada lại nheo lại, quan sát tôi thật kỹ."
"2298" = "Một tiếng kêu như thích thú của Kisaki.\\nTrong một khoảnh khắc ngắn ngủi, Houshou Mototada nhíu mày vẻ khó chịu."
"2300" = "Người đã hành động đúng như toan tính, không chỉ có mình Houshou Mototada."
"2302" = "Dù không có ánh mắt đó, tôi vẫn muốn đối mặt.\\nTôi muốn thử thách và mài giũa bản thân bằng những lời chỉ trích sắc bén của Houshou Mototada."
"2321" = "Cả chúng ta nữa, nếu có thể lập ra một kế hoạch tái thiết ưu việt hơn,\\nthì việc mời gọi nhà máy sẽ bị rút lại――chúng ta đã có được lời hứa hẹn tương đương như vậy."
"2322" = "Thứ bị đánh mất.\\nNiềm tự hào, truyền thống――và sự tự tin được xây đắp từ những điều đó."
"2323" = "Một cái bắt tay ngắn ngủi.\\nNhưng đầy mạnh mẽ."
"2325" = "Nhân viên của \\x%lエアクラ;#00ffc040;Aircra%l;#;――Tôi liếc nhìn về phía anh Uragami,\\nchắc chắn anh ấy nghe thấy, nhưng biểu cảm không hề thay đổi."
"2334" = "Nói nặng lời quá, dù là chuyện của người khác nhưng tôi vẫn thấy lo."
"2337" = "Không biết có phải do cho quá nhiều Tabasco vào pizza không,\\nnhưng tay Kisaki hơi rịn mồ hôi và ẩm ướt."
"2338" = "Tôi cảm nhận rõ ràng mình đang bị thử thách.\\nĐồng thời, một câu hỏi tự vấn được gieo vào tâm trí tôi."
"2341" = "Ngay sau khi tôi kể lại toàn bộ câu chuyện đã nói với Kisaki,\\nHoushou Mototada thẳng thừng tuyên bố."
"2346" = "Nhìn thẳng vào cô ấy,\\ntôi truyền đạt những lời muốn nói một cách trực diện."
"2354" = "Rốt cuộc, một kẻ như tôi,\\nsẽ đối xử với tiền bạc, với con người như thế nào?"
"2379" = "Dường như đã hiểu ra,\\nđôi mắt Hibiki sáng long lanh và mở to."
"2385" = "Bị dồn vào chân tường bởi chính lời nói của mình, Hibiki cứng họng,\\ncon bé nhìn tôi với ánh mắt cầu cứu."
"2387" = "Hibiki nghiêng đầu vẻ khó hiểu."
"2391" = "Hibiki tròn mắt ngạc nhiên.\\nTrái ngược với con bé, vẻ nhẹ nhõm bắt đầu lan tỏa trên khuôn mặt Kisaki."
"2393" = "Những tờ tiền giấy ngày hôm qua sẽ biến thành giấy lộn, và chỉ có ngoại tệ, vàng bạc hay đá quý\\nmới có thể đổi lấy một mẩu bánh mì."
"2480" = "Kisaki chớp mắt vài lần,\\nrồi từ từ thốt lên bằng một giọng như mất hết sức lực."
"2482" = "Kisaki rời mắt khỏi tầng dưới, nhìn thẳng vào tôi."
"2490" = "Kisaki rõ ràng đang dao động."
"2494" = "Kisaki mỉm cười đáp lại lời nói đầy vẻ hoài nghi của Hibiki."
"2504" = "Chậm rãi, sâu sắc.\\nKisaki gật đầu."
"2506" = "Kisaki cười khổ,\\nđưa tay vân vê lọn tóc dài của mình."
"2508" = "Thấy vậy, Kisaki lấy ra một tờ một vạn yên từ trong ví,\\nsau đó viết \"Một vạn yên\" lên một tờ giấy nhớ."
"2511" = "Kisaki vẫn giữ vẻ mặt điềm nhiên,\\nlặng lẽ nhìn chằm chằm vào Houshou Mototada."
"2527" = "Kisaki gật đầu đồng tình với lời nói hùng hồn của Hibiki.\\nTôi cũng đồng tình với điều đó."
"2530" = "Bắt đầu từ cổ, giống như có ai đó đang phun sơn vậy.\\nKhuôn mặt Kisaki dần dần, thấy rõ là đang đỏ bừng lên."
"2557" = "Đúng là như vậy, nhưng……"
"2570" = "Điều đó là đương nhiên.\\nNhưng tôi vẫn cẩn thận trong cách trả lời."
"2571" = "Nếu là vậy thì tôi hoàn toàn có thể đồng cảm――\\nNghĩ đến đây, tôi chợt thấy xấu hổ về bản thân lúc nãy."
"2572" = "Biểu cảm đó có nét gì đó giống Kisaki,\\nkhiến tôi có suy nghĩ thảnh thơi rằng “Quả đúng là cha con”."
"2581" = "Tiếng gõ cửa thô bạo――như thể đang đập cửa.\\nVai Kisaki giật nảy lên."
"2599" = "Đối đầu với nhau, và kẻ yếu hơn sẽ bị nuốt chửng."
"2627" = "（Ồ.）"
"2628" = "（Rầm）"
"2631" = "（Cộc cộc）"
```

## §5. Lượt soát 2 + Chờ Hieu

- Lượt soát 2: 178/178 fix đọc lại đối chiếu JP (+TW) — 178 giữ nguyên, 0 bỏ, 0 sửa. (Lượt soát 2 bắt được 1 dòng đọc sót ở lượt 1: 2057 — VN cũ "Cách sử dụng tiền bạc……và con người, sao ạ." là bản dịch của 1901, không phải của 2057; đã bổ sung fix cho 2057 từ 2214 trước khi chốt JSON.)
- Chờ Hieu (không tự quyết):
  1. Key 1637 "Hừm." cho ふん — giá trị "Hừ." ở 1852 bị loại là bản dịch thừa; nếu Hieu muốn thống nhất ふん→"Hừ" (không có m) thì đổi 1637 thành "Hừ.". Hiện giữ "Hừm." vì sát âm mũi ん hơn.
  2. Key 1705 "Chuyện đó――" bị loại — có thể là bản dịch của 1983 ("それは――", hiện dịch mới "Đó là――"). Nếu Hieu muốn giữ cách dịch "Chuyện đó" của bản gốc thì đổi 1983 thành "Chuyện đó――".
  3. Key 1702 "Vậy sao. Nếu thế thì tôi xin tuân lệnh." — Kisaki xưng "tôi" với Mototada (bố, kiêm chủ tịch, trong bối cảnh nhận lệnh công việc). Nếu Hieu muốn Kisaki xưng "cháu" với bố thì đổi thành "Vâng. Vậy thì cháu xin nhận lệnh.".
  4. Key 2190 "Lại một sự thật phũ phàng nữa khó lòng phản bác." cho JP "これもまた、反論しがたい事実の指摘だ。" — bản dịch hơi phóng ("phũ phàng" không có trong JP) nhưng là giá trị duy nhất trong file khớp dòng này; nếu Hieu muốn sát hơn thì đổi thành "Đây cũng là một sự thật khó lòng phản bác.".
  5. Key 1256/1987: 日ノ本 "Hinomoto" vs "Hinamoto" (đang chờ từ trước).
  6. Soutetsu gọi Kisaki "em" (nhất quán toàn file, vd. 1253, 1740) — phù hợp hướng thống nhất "cô"→"em" đang chờ; nếu đợt thống nhất quyết khác thì rà lại.

## Kết bài

File 稀咲01_金と人 đã audit xong toàn bộ 379 dòng: 178 dòng sai (47,0%) — 173 lệch dòng trong một chuỗi xoay lớn (165 lấy lại bản dịch đúng trong file, 8 dịch mới), 3 đại từ Kisaki "chị"→"em", 2 gasp 「っ！」→"Ư!". Không dòng mồ côi, không nhiễm chéo, không dòng chưa dịch, không trùng khóa. Khối TOML 178 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 178/178, 0 bỏ, 0 sửa. Chờ Hieu: "Hừm." vs "Hừ." (1637), "Chuyện đó" vs "Đó là" (1983), Kisaki "tôi" vs "cháu" với Mototada (1702), "phũ phàng" ở 2190, và "Hinomoto" vs "Hinamoto".
