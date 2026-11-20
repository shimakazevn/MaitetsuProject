# Audit — lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml

- File: `lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml` — route 02_Hibiki, 611 dòng script (223 độc thoại, 166 thoại Mikuro, 131 thoại Hibiki, 91 thoại Soutetsu).
- Nội dung: sau chuyến chạy 8620 thành công đưa 38696 trở lại đường chính, Mikuro bị đau bụng — hoá ra là 'sealing' mở ra chức năng mới; em muốn Hibiki làm Master của mình, rồi cả ba cùng làm tình lần đầu (Mikuro mất trinh), kết bằng cảnh ba người quấn quýt sau khi xuất tinh.
- **Kết quả: 82/611 dòng sai (13,4%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (611 dòng, 0 khóa trùng, 0 ô VN trống); VN khớp TOML tuyệt đối 611/611 (0 lệch). `[selections]` rỗng. Có 4 thẻ `%l` trong VN (2152, 2262, 1686, 2144 — đều là `\x%lレイルロオド;#00ffc040;Railord%l;#;`, đúng định dạng, JP có tag tương ứng) — không có thẻ sai định dạng, không có thẻ VN tự thêm.
- TOML md5 `897021b35bb2e469b516f1f0d7b4274e`; không có bản sao file này (không thuộc 11 nhóm trùng — đã kiểm tra md5 toàn bộ 227 file). File UTF-8 BOM + CRLF, 611 khóa script.
- Soutetsu 'anh' với Hibiki đúng toàn file (91 dòng thoại Soutetsu, 0 dòng 'tôi' sai đối tượng; độc thoại 223 dòng dùng 'tôi', 0 dòng dùng 'anh'). Hibiki gọi 'anh hai' (にぃにぃ), Mikuro gọi 'anh Soutetsu' — đúng quy tắc đã chốt. Không có sửa đại từ nào trong file này. Không có Kisaki trong file.
- Thuật ngữ: chỉ có 御一夜 (2 dòng: 2595, 1707 — đều sai dạng 'Ohimitera', đã sửa 'Ohitoyo'). Không có 帝鉄/帝大/宮司/日ノ本/乗務鞄/電車姫/Migita trong file nên không có gì khác chờ đợt thống nhất. 'Master' giữ nguyên toàn file (đúng — マスター). 'Railord' đúng (2152, 2262, 1686, 2144).
- 1096 và 1099 là dòng chỉ có dấu '……' — VN giống hệt JP vì chỉ là dấu câu, không phải dòng chưa dịch.

## §2. Danh sách sửa (82 dòng)

Phân loại: gasp 51 (30 từ sweep + 21 sweep bỏ sót), fa/fu 33 (trong đó 8 dòng kiêm gasp), thuật ngữ 2 (2595, 1707), bịa/dịch sai 5 (2110, 1823, 1857, 2747, 3143 — 1857 kiêm fa/fu).

### 1114 — 双鉄 — gasp
- JP: 「──っ！　っ～～～っ」
- TW: 「……！」
- VN cũ: 「──っ! っ~~~っ」
- Sửa: 「──Ư! Ư~~~Ư」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 1678 — みくろ — fa/fu
- JP: 「ひゃうっ──んっ──ふあっ──あっ──\nあっ──あっ──あっ──ああっ──」
- TW: 「呀啊——嗯——呼啊——啊——　啊——啊——啊——啊啊——」
- VN cũ: 「Hyau── ưm── fua── a──\nA── a── a── aa──」
- Sửa: 「Hyau── ưm── phùa── a──\nA── a── a── aa──」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 1680 — みくろ — gasp
- JP: 「ひゃうっ」
- TW: 「呀嗚」
- VN cũ: 「Hyau」
- Sửa: 「HyauƯ」
- Lý do: JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất).

### 1681 — みくろ — gasp
- JP: 「ひゃんっっ」
- TW: 「呀嗯」
- VN cũ: 「Hyan」
- Sửa: 「HyanƯƯ」
- Lý do: JP ひゃんっっ (2 っ cuối dòng, không dấu câu sau); VN cũ 'Hyan' làm mất cả hai — thêm 2 Ư (mỗi っ→1 Ư, tiền lệ sweep 2330).

### 1703 — 双鉄 — gasp
- JP: 「ふっ──あっ──あっ──ああっ」
- TW: 「呼——啊——啊——啊啊」
- VN cũ: 「Phù──a──a──aa.」
- Sửa: 「Phù──a──a──aaƯ.」
- Lý do: JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất).

### 1707 — 双鉄 — terminology
- JP: 「ふぅ。御一夜温泉駅、着。定刻」
- TW: 「呼。準時抵達御一夜溫泉站」
- VN cũ: 「Phù. Đến ga suối nước nóng Ohimitera. Đúng giờ.」
- Sửa: 「Phù. Đến ga suối nước nóng Ohitoyo. Đúng giờ.」
- Lý do: JP 御一夜温泉駅: VN cũ 'Ohimitera' — sai dạng tên đã chốt; sửa 'Ohitoyo'.

### 1708 — みくろ — fa/fu
- JP: 「ふえっ！？　またっ──みくろっ！　またっ！\nだって！　ぼっきっ！　だってっ！　だってぇっ！！」
- TW: 「呼哎？！又來了——美玖路又要洩了！因為！肉棒！真的！非常舒服！！」
- VN cũ: 「Fue!? Lại nữa── Mikuro! Lại nữa!\nBởi vì! Cương cứng! Bởi vì! Bởi vì!!」
- Sửa: 「Phuê!? Lại nữa── Mikuro! Lại nữa!\nBởi vì! Cương cứng! Bởi vì! Bởi vì!!」
- Lý do: JP ふえっ: VN cũ romanisation 'Fue' — sửa 'Phuê' (ふぇ/ふえ→'phuê' theo quy tắc fa/fu).

### 1711 — 日々姫 — fa/fu
- JP: 「ふあっ──やっ──にぃにっ、いきなり、指、\n二本とかぁ──ふぁうっ！！！？」
- TW: 「呼啊——呀——阿哥，怎麼突然兩根手指插進來了——呼啊！！！」
- VN cũ: 「Fua── a── anh hai, tự nhiên lại, đưa cả hai ngón tay\nvào thế── fua!!!?」
- Sửa: 「Phùa── a── anh hai, tự nhiên lại, đưa cả hai ngón tay\nvào thế── phàu!!!?」
- Lý do: JP có 2 âm fa/fu: ふあっ──→'phùa──' và ふぁうっ→'phàu' (ふぁ→'phà' + う→'u').

### 1712 — 日々姫 — gasp + fa/fu
- JP: 「ふぁっ──あっ──あっ──ああっ」
- TW: 「呼啊——啊——啊——啊啊」
- VN cũ: 「Fua── a── a── aa.」
- Sửa: 「Phà── a── a── aaƯ.」
- Lý do: JP ふぁっ──: ふぁ→'phà' theo quy tắc fa/fu. Đồng thời gasp cuối dòng: ああっ→'aaƯ.' (JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất).)

### 1714 — みくろ — fa/fu
- JP: 「ふあっ──あっ──あっ──なに、これ──\nなに、これぇっっ！！　きもちい、みくろ、気持ちいい」
- TW: 「呼啊——啊——啊——這是什麼感覺，感覺好怪啊！！美玖路變得好舒服啊」
- VN cũ: 「Fua── a── a── gì thế, này──\nGì thế, này!! Sướng quá, Mikuro, sướng quá.」
- Sửa: 「Phùa── a── a── gì thế, này──\nGì thế, này!! Sướng quá, Mikuro, sướng quá.」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 1716 — 日々姫 — fa/fu
- JP: 「ふあっ──あっ──すごっ──ふえっ！！？\nや、みくろ──ごめんっ、制服──私、汚してっっ」
- TW: 「呼啊——啊——天啊——哎？！！呀，美玖路，對不起，你的制服被我弄髒了」
- VN cũ: 「Fua── a── tuyệt quá── fue!!?\nA, Mikuro── xin lỗi, đồng phục── chị, làm bẩn mất rồi」
- Sửa: 「Phùa── a── tuyệt quá── phuê!!?\nA, Mikuro── xin lỗi, đồng phục── chị, làm bẩn mất rồi」
- Lý do: JP ふあっ── và ふえっ: VN cũ romanisation 'Fua'/'fue' — sửa 'Phùa'/'phuê' theo quy tắc fa/fu.

### 1718 — みくろ — fa/fu
- JP: 「ふあっ──あっ──すごっ──こんなにっ──あ──\nこんなに──はやくっ──つよくっ──ふか、くにっ」
- TW: 「呼啊——啊——好厲害——這麼——啊——這麼快——這麼用力——這麼深」
- VN cũ: 「Fua── a── tuyệt quá── thế này── a──\nNhanh── mạnh── sâu, thế này」
- Sửa: 「Phùa── a── tuyệt quá── thế này── a──\nNhanh── mạnh── sâu, thế này」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 1720 — みくろ — fa/fu
- JP: 「ふあっ──あっ──日々姫さんの、指……指が──\nみくろ──みくろの、クリトリス、をっ──」
- TW: 「呼啊——啊——日日姬小姐的手指……手指在撫摸美玖路、美玖路的陰核——」
- VN cũ: 「Fua── a── ngón tay của chị Hibiki…… ngón tay──\nMikuro── âm vật của Mikuro, đang──」
- Sửa: 「Phùa── a── ngón tay của chị Hibiki…… ngón tay──\nMikuro── âm vật của Mikuro, đang──」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 1722 — みくろ — fa/fu
- JP: 「ふあっ──あっ──くぱって──みくろ──\n日々姫さんに──ひらかれて、ますっ」
- TW: 「呼啊——啊——美玖路的下面張開了，被日日姬小姐撐開了」
- VN cũ: 「Fua── a── mở rộng ra── Mikuro──\nđang được chị Hibiki── vạch ra, ạ」
- Sửa: 「Phùa── a── mở rộng ra── Mikuro──\nđang được chị Hibiki── vạch ra, ạ」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 1724 — みくろ — gasp + fa/fu
- JP: 「ふあっ……あっ──しゅごっ──すごいっ──\nんっ──あっつ──はっ──きれぇ──綺麗っ……」
- TW: 「呼啊……啊——天啊——好厲害——嗯——啊——哈——好美——太美了……」
- VN cũ: 「Fua…… a── tuyệt── tuyệt quá──\nƯm── nóng── hà── đẹp── đẹp quá……」
- Sửa: 「PhùaƯ…… a── tuyệt── tuyệt quá──\nƯm── nóng── hà── đẹp── đẹp quá……」
- Lý do: JP ふあっ……: ふあ→'phùa'; っ trước …… làm mất gasp — thêm Ư (JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất).)

### 1725 — みくろ — gasp + fa/fu
- JP: 「ふあっ……あっ──日々姫、さん。\nみくろ──は、あっ──みくろ──う、んっ」
- TW: 「呼啊……啊，日日姬小姐。美玖路——啊——美玖路——唔、嗯」
- VN cũ: 「Fua…… a── chị Hibiki.\nMikuro── là, a── Mikuro── ư, ưm」
- Sửa: 「PhùaƯ…… a── chị Hibiki.\nMikuro── là, a── Mikuro── ư, ưm」
- Lý do: JP ふあっ……: ふあ→'phùa'; っ trước …… làm mất gasp — thêm Ư.

### 1727 — みくろ — gasp + fa/fu
- JP: 「ふあっ……みくろ……シーリングが解けたとこ──\nおんなのこのとこ、全部──日々姫さんにこんな近くで」
- TW: 「呼啊……美玖路……封印解除的地方——女孩子的地方，離日日姬小姐這麼近——」
- VN cũ: 「Fua…… Mikuro…… chỗ phong ấn vừa được giải trừ──\nchỗ con gái, toàn bộ── ở gần chị Hibiki thế này」
- Sửa: 「PhùaƯ…… Mikuro…… chỗ phong ấn vừa được giải trừ──\nchỗ con gái, toàn bộ── ở gần chị Hibiki thế này」
- Lý do: JP ふあっ……: ふあ→'phùa'; っ trước …… làm mất gasp — thêm Ư.

### 1728 — みくろ — gasp + fa/fu
- JP: 「ふあっ」
- TW: 「呼啊」
- VN cũ: 「Fua.」
- Sửa: 「PhùaƯ.」
- Lý do: JP ふあっ (không dấu câu sau): ふあ→'phùa'; っ mất hẳn — thêm Ư.

### 1729 — 日々姫 — fa/fu
- JP: 「ふあぁぁぁぁぁぁあああああああんっ！！！！」
- TW: 「呼啊啊啊啊啊啊啊嗯！！！！」
- VN cũ: 「Fuaaaaaaaaaaaaaaaaan!!!!」
- Sửa: 「Phùaaaaaaaaaaaaaaaaan!!!!」
- Lý do: JP ふあぁぁぁぁぁぁあああああああんっ: VN cũ romanisation 'Fua…' — sửa 'Phù…' (ふあ→'phùa', giữ nguyên số lượng a của VN cũ; xem ghi chú §4 về số lượng nguyên âm).

### 1731 — みくろ — fa/fu
- JP: 「ふやぁぁぁっぁぁぁんっ！　みくろ、好きっ！！\nこれ、しゅきっ！　ぐりゅって、されるのい、しゅきぃ」
- TW: 「呼啊啊啊啊啊啊嗯！美玖路好喜歡這樣！這樣真棒！頂來頂去的，好喜歡」
- VN cũ: 「Fuyaaaaaaan! Mikuro, thích lắm!!\nCái này, thích lắm! Được cọ xát, thích lắmmm」
- Sửa: 「Phuyaaaaaaan! Mikuro, thích lắm!!\nCái này, thích lắm! Được cọ xát, thích lắmmm」
- Lý do: JP ふやぁぁぁっぁぁぁんっ: VN cũ romanisation 'Fuya…' — sửa 'Phuya…' (ふやぁ→'phuya' theo quy tắc đã chốt; tiền lệ reinah3 1019). Giữ nguyên số lượng a của VN cũ; xem ghi chú §4.

### 1733 — みくろ — fa/fu
- JP: 「ふああっ！？　あっ──み、みくろ、いま──\nみくろの、おまた──すごく、きもちよくて」
- TW: 「呼啊啊？！啊——美、美玖路剛剛——美玖路的胯部——非常舒服」
- VN cũ: 「Fuaa!? A──Mi, Mikuro, vừa nãy──\nChỗ đó của Mikuro── sướng lắm ạ.」
- Sửa: 「Phùaa!? A──Mi, Mikuro, vừa nãy──\nChỗ đó của Mikuro── sướng lắm ạ.」
- Lý do: JP ふああっ: VN cũ romanisation 'Fuaa' — sửa 'Phùaa' (ふあ→'phùa' + giữ nguyên âm a dài).

### 1735 — みくろ — fa/fu
- JP: 「ふあっ！　あっ！　いっしょ──いっしょにぃっ！」
- TW: 「呼啊！啊！一起，我們一起！」
- VN cũ: 「Fua! A! Cùng nhau── cùng nhauuu!」
- Sửa: 「Phùa! A! Cùng nhau── cùng nhauuu!」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 1736 — 日々姫 — fa/fu
- JP: 「ふあっ　あっ！　あっ！　ああああっ！！！！！！」
- TW: 「呼啊！啊！啊！啊啊啊啊！！！！！！」
- VN cũ: 「Fua a! A! Aaaa!!!!!!」
- Sửa: 「Phùa a! A! Aaaa!!!!!!」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 1737 — 日々姫 — fa/fu
- JP: 「ふあっ！　あっ！　にぃにっ！　にぃにっ！！！！\nきょうっ！　すごっ──わたしっ──かんじてっ！」
- TW: 「呼啊！啊！阿哥！阿哥！！！！今天！你特別勇猛，我好舒服啊！」
- VN cũ: 「Fua! A! Anh hai! Anh hai!!!!\nHôm nay! Tuyệt quá── em── cảm nhận được!」
- Sửa: 「Phùa! A! Anh hai! Anh hai!!!!\nHôm nay! Tuyệt quá── em── cảm nhận được!」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 1739 — 日々姫 — fa/fu
- JP: 「ふあっ！　あっ！！　あっ──ああああっ！！！！」
- TW: 「呼啊！啊！！啊——啊啊啊啊！！！！」
- VN cũ: 「Fua! A!! A── aaaa!!!!」
- Sửa: 「Phùa! A!! A── aaaa!!!!」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 1741 — みくろ — gasp + fa/fu
- JP: 「ふやっ──なにっ、これっ──あちゅいのっ──\nおなか──おまた──どろって──ふっ──あっ」
- TW: 「呼啊，這是什麼？好熱的東西進到肚子裡面去了，胯部黏糊糊的，呼——啊」
- VN cũ: 「Fuya── gì thế, này── nóng quá──\nBụng── vùng kín── nhão nhoét── phu── a」
- Sửa: 「Phuya── gì thế, này── nóng quá──\nBụng── vùng kín── nhão nhoét── phu── aƯ」
- Lý do: JP ふやっ──: ふや→'phuya' theo quy tắc fa/fu. Đồng thời gasp cuối dòng: あっ→'aƯ' (JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất).)

### 1743 — 日々姫 — gasp + fa/fu
- JP: 「ふあっ！？　あっ──にぃにっ──あっつっ──んっ\nいっつも──より、も──あつ──くて──ふと──っ」
- TW: 「呼啊？！啊——阿哥——啊——嗯——比平時——要熱得多——而且很粗——」
- VN cũ: 「Fua!? A── anh hai── nóng quá── ưm\nHơn── mọi khi── nóng── và── to──」
- Sửa: 「Phùa!? A── anh hai── nóng quá── ưm Hơn── mọi khi── nóng── và── to──Ư」
- Lý do: Sweep っ: JP kết bằng ──/～～ + っ; VN cũ giữ dấu nhưng làm mất gasp — fix sweep thêm Ư (đã kiểm chứng vs JP). Đồng thời ふあっ→'phùa' theo quy tắc fa/fu.

### 1746 — 双鉄 — gasp
- JP: 「くはっ」
- TW: 「咕哈」
- VN cũ: 「Kuha.」
- Sửa: 「KuhaƯ.」
- Lý do: JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất).

### 1758 — みくろ — fa/fu
- JP: 「ひゅあっ！？　あ──あ……ふえっ！？」
- TW: 「咿呀？！啊——啊……呼哎？！」
- VN cũ: 「Hyua!? A── a…… fue!?」
- Sửa: 「Hyua!? A── a…… phuê!?」
- Lý do: JP ふえっ: VN cũ romanisation 'fue' — sửa 'phuê' (ふぇ/ふえ→'phuê').

### 1767 — みくろ — gasp
- JP: 「っ！　わあっ」
- TW: 「哇啊！」
- VN cũ: 「っ! Oa」
- Sửa: 「Ư! Oa」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 1771 — みくろ — gasp
- JP: 「っ！！！！！！！！」
- TW: 「哇！！！！！！！！」
- VN cũ: 「っ!!!!!!!!」
- Sửa: 「Ư!!!!!!!!」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 1773 — みくろ — fa/fu
- JP: 「はっっ──あっ──ふっ──ふあっ──」
- TW: 「哈——啊——呼——呼啊——」
- VN cũ: 「Hà── a── phu── fua──」
- Sửa: 「Hà── a── phu── phùa──」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 1774 — 日々姫 — gasp
- JP: 「はっっっ──あっ！　っ──んっ──んひゅっっっ」
- TW: 「哈——啊！——嗯——嗯唔」
- VN cũ: 「Hà── a! っ── ưm── ưm hưuuu」
- Sửa: 「Hà── a! Ư── ưm── ưm hưuuu」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 1777 — 日々姫 — gasp
- JP: 「はっ……あっ──にぃに──にぃにっ──\nそぎゃん、ずうっと──クリ、ばっかり──んあっ」
- TW: 「哈……啊——阿哥——阿哥——你一直摸陰核的話——嗯啊」
- VN cũ: 「Hà…… a── anh hai── anh hai──\nCứ thế, mãi── chỉ có âm vật── ưm a」
- Sửa: 「Hà…… a── anh hai── anh hai──\nCứ thế, mãi── chỉ có âm vật── ưm aƯ」
- Lý do: JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất).

### 1785 — 日々姫 — gasp
- JP: 「はうっ」
- TW: 「哈嗚」
- VN cũ: 「Hau.」
- Sửa: 「HauƯ.」
- Lý do: JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất).

### 1786 — みくろ — gasp + fa/fu
- JP: 「はうっ！　あっ！　あっ！　あああっ！\nふあ──っ──んっ！　んううううっ！！！」
- TW: 「哈嗚！啊！啊！啊啊啊！呼啊——嗯！嗯唔唔！！！」
- VN cũ: 「Hau! A! A! Aaa!\nFua──っ──ưm! Ưm uuuu!!!」
- Sửa: 「Hau! A! A! Aaa! Phùa──Ư──ưm! Ưm uuuu!!!」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep). Đồng thời ふあ→'phùa' theo quy tắc fa/fu.

### 1790 — 双鉄 — gasp
- JP: 「お──おっ」
- TW: 「哦——哦」
- VN cũ: 「O── o」
- Sửa: 「O── oƯ」
- Lý do: JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất).

### 1794 — 双鉄 — gasp
- JP: 「っ……ぁ」
- TW: 「唔……啊」
- VN cũ: 「っ……a.」
- Sửa: 「Ư……a.」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 1804 — 双鉄 — gasp
- JP: 「ぁ──ぅっ」
- TW: 「啊——唔」
- VN cũ: 「A──ư.」
- Sửa: 「A──ưƯ.」
- Lý do: JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất). (Phán đoán: 'ư' chỉ diễn ぅ, っ mất hẳn — thêm Ư.)

### 1811 — 日々姫 — fa/fu
- JP: 「あ……ん──ちゅっ──ちゅむっ──ちゅっ──ふ\n……ん……れるっ──れりゅっ──れろおおっ──ぷあ」
- TW: 「啊……嗯——啾——啾唔——啾——呼……嗯……咧溜——滋溜溜——噗啊」
- VN cũ: 「A……ưm──chụt──chụt──chụt──fu\n……ưm……liếm──liếm──liếmmm──pua」
- Sửa: 「A……ưm──chụt──chụt──chụt──fu\n……ưm……liếm──liếm──liếmmm──pùa」
- Lý do: JP ぷあ cuối dòng: VN cũ romanisation 'pua' — sửa 'pùa' theo tương tự nhóm fa/fu (chưa có tiền lệ trực tiếp cho ぷあ — ghi chú để Hieu xác nhận, §4).

### 1814 — 日々姫 — gasp
- JP: 「あ……にぃに──そこ──んっ──やあっ」
- TW: 「啊……阿哥——那裡——嗯——呀啊」
- VN cũ: 「A…… anh hai── chỗ đó── ưm── a」
- Sửa: 「A…… anh hai── chỗ đó── ưm── aƯ」
- Lý do: JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất).

### 1818 — 日々姫 — gasp
- JP: 「あはっ」
- TW: 「啊哈」
- VN cũ: 「Aha」
- Sửa: 「Aha.」
- Lý do: JP あはっ (tiếng cười); VN cũ 'Aha' không dấu câu — thêm '.' theo quy ước của chính dịch giả cho tiếng cười (ふふっ→'Fufu.'). Không thêm Ư vì đây là cười, không phải gasp.

### 1820 — みくろ — fa/fu
- JP: 「ふぁんっ！！」
- TW: 「啊啊嗯！！」
- VN cũ: 「Fan!!」
- Sửa: 「Phàn!!」
- Lý do: JP ふぁんっ: ふぁ→'phà' + ん→'n'; っ đã diễn bằng '!'.

### 1823 — 日々姫 — mistranslation
- JP: 「あ、ううん」
- TW: 「啊，對了」
- VN cũ: 「A, không được.」
- Sửa: 「A, không.」
- Lý do: JP あ、ううん ('à, không' — tự sửa lời); VN cũ 'không được' (cấm đoán) sai nghĩa — sửa 'A, không.' (JP hơn TW: TW '啊，對了' mâu thuẫn JP).

### 1833 — 日々姫 — gasp
- JP: 「ん──っ──え──れっ──れろおおっっ」
- TW: 「嗯——滋溜——咧溜」
- VN cũ: 「Ưm──っ──ê──liếm──liếmmmmm」
- Sửa: 「Ưm──Ư──ê──liếm──liếmmmmm」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 1857 — 日々姫 — fa/fu + mistranslation
- JP: 「んきゅ！　ふあっ！　あ──ずりゅって──ずる、って──やぁぁあっ──にぃに──ぜんぶ、いっちゃうぅ」
- TW: 「嗯唔！呼啊！啊——滋溜——滋嚕的好大聲——呀啊啊啊——阿哥——全都進來了」
- VN cũ: 「Ưm kyu! Fua! A── trượt── tuột, ra── aaaa── anh hai── ra hết, mất」
- Sửa: 「Ưm kyu! Phùa! A── trượt── tuột, ra── aaaa── anh hai── vào hết, mất」
- Lý do: JP ふあっ→'phùa' theo quy tắc fa/fu. Đồng thời: JP ぜんぶ、いっちゃうぅ ('vào hết') — TW '全都進來了' đồng ý; VN cũ 'ra hết' ngược hướng — sửa 'vào hết'.

### 1871 — みくろ — gasp
- JP: 「はい！　みくろ、そぎゃんしたいです！\nだから、みくろ──そぎゃんします！　──っ！！」
- TW: 「嗯！美玖路想親！所以，美玖路要開始親了！」
- VN cũ: 「Vâng ạ! Mikuro, muốn thế ạ!\nVì vậy, Mikuro── sẽ làm thế! ──っ!!」
- Sửa: 「Vâng ạ! Mikuro, muốn thế ạ! Vì vậy, Mikuro── sẽ làm thế! ──Ư!!」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 1901 — 日々姫 — fa/fu
- JP: 「ぷあっ──ふふっ、だって。みくろ」
- TW: 「噗啊——呵呵，阿哥是這麼說的哦。美玖路」
- VN cũ: 「Pua──fufu, anh ấy bảo thế kìa. Mikuro.」
- Sửa: 「Pùa──fufu, anh ấy bảo thế kìa. Mikuro.」
- Lý do: JP ぷあっ──: VN cũ romanisation 'Pua' — sửa 'Pùa' theo tương tự nhóm fa/fu (chưa có tiền lệ trực tiếp cho ぷあ — ghi chú để Hieu xác nhận, §4).

### 1925 — みくろ — gasp
- JP: 「きつ、いっ──ふっ──ふうううっ──はあああっ」
- TW: 「好緊——呼——呼唔唔——蛤啊啊啊」
- VN cũ: 「Chật, quá── phu── phuuuu── haaaa」
- Sửa: 「Chật, quá── phu── phuuuu── haaaaƯ」
- Lý do: JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất).

### 1928 — みくろ — fa/fu
- JP: 「はいっ！　ですっ──んっ──ひび、き──さんっ──\nふあっ──みくろも、セックス──セックス、セックス」
- TW: 「好！好的——嗯——日日姬——小姐——呼啊——美玖路也想要做愛——很想，非常想」
- VN cũ: 「Vâng ạ! Đúng vậy── ưm── chị Hibi, ki──\nFua── Mikuro cũng, làm tình── làm tình, làm tình」
- Sửa: 「Vâng ạ! Đúng vậy── ưm── chị Hibi, ki──\nPhùa── Mikuro cũng, làm tình── làm tình, làm tình」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 1942 — 双鉄 — gasp
- JP: 「そうだ。その膣に──くっ──こう、して──\n勃起を──挿入──しっ──っっっ」
- TW: 「對的。對著這個陰道——唔——像這樣——把肉棒——插進去——」
- VN cũ: 「Đúng vậy. Vào trong âm đạo đó── hự── thế này──\nđưa── dương vật cương cứng── vào──っっっ」
- Sửa: 「Đúng vậy. Vào trong âm đạo đó── hự── thế này── đưa── dương vật cương cứng── vào──ƯƯƯ」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 1961 — 双鉄 — gasp
- JP: 「どうした、日々──っ！！！」
- TW: 「怎麼了，日日——！！！」
- VN cũ: 「Sao thế, Hibi──っ!!!」
- Sửa: 「Sao thế, Hibi──Ư!!!」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 1967 — みくろ — fa/fu
- JP: 「見たいっ──ですっ──んひゅっ──ふあ──あっ、\nみたい、けど──みくろっ──なんだか、みくろぉっ」
- TW: 「想看——好想看——嗯唔——呼啊——啊真的很想看——但美玖路——感覺怪怪的」
- VN cũ: 「Muốn nhìn── ạ── ưm hưu── fua── a,\nMuốn nhìn, nhưng mà── Mikuro── sao thế này, Mikuro」
- Sửa: 「Muốn nhìn── ạ── ưm hưu── phùa── a,\nMuốn nhìn, nhưng mà── Mikuro── sao thế này, Mikuro」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 2100 — 日々姫 — gasp
- JP: 「み……くろっ──っ」
- TW: 「美……玖路——」
- VN cũ: 「Mi……kuro──っ」
- Sửa: 「Mi……kuro──Ư」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2101 — 日々姫 — gasp
- JP: 「みくろもっ──すぐ。にっ──一緒や、けん──ねっ\n──にぃにと、わたし、と──っ──三人、でっ──」
- TW: 「美玖路——你也很快——就能來了呢——到時候和阿哥還有我——我們三個一起——」
- VN cũ: 「Mikuro cũng── sẽ sớm. Cùng nhau, thôi── nhé\n──Anh hai, chị, và──っ──ba người, cùng nhau──」
- Sửa: 「Mikuro cũng── sẽ sớm. Cùng nhau, thôi── nhé ──Anh hai, chị, và──Ư──ba người, cùng nhau──」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2104 — 双鉄 — gasp
- JP: 「みく、ろ──っ──くっ──あっ──」
- TW: 「美玖路——唔——啊——」
- VN cũ: 「Miku, ro──っ──hự──a──」
- Sửa: 「Miku, ro──Ư──hự──a──」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2107 — 日々姫 — fa/fu
- JP: 「みくっ、ろっ──みて──あっ──ふあっ──\nこいっ、ばっ──セックスっ──私、と、にぃに、の」
- TW: 「美玖路——看著吧——啊——呼啊——這就是——做愛——我和阿哥的做愛」
- VN cũ: 「Miku, ro── nhìn đi── a── fua──\nCái này── làm tình── của chị, và, anh hai」
- Sửa: 「Miku, ro── nhìn đi── a── phùa──\nCái này── làm tình── của chị, và, anh hai」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 2110 — みくろ — fabrication
- JP: 「みくろ……っ──みくろ……おなか、が」
- TW: 「美玖路……美玖路……肚子」
- VN cũ: 「Mikuro…… ──Mikuro…… bụng, đau」
- Sửa: 「Mikuro…… ──Mikuro…… bụng, em…」
- Lý do: JP 'おなか、が' cụt (TW chỉ '肚子'); VN cũ tự thêm 'đau' — bịa phần hoàn thiện cho câu JP cụt. Sửa bỏ 'đau', giữ câu cụt 'bụng, em…'.

### 2125 — 双鉄 — gasp
- JP: 「みくろも、日々姫とっ──くっ──\n同じ、刺激が──好き、なのだなっ──っ！！！」
- TW: 「美玖路和日日姬——唔——都喜歡用一樣的方式來刺激的啊！！！」
- VN cũ: 「Mikuro cũng, giống như Hibiki── hự──\nThích, kiểu kích thích── này, nhỉ──っ!!!」
- Sửa: 「Mikuro cũng, giống như Hibiki── hự── Thích, kiểu kích thích── này, nhỉ──Ư!!!」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2148 — みくろ — gasp
- JP: 「見て、ます──みくろっ──っ──あっ──日々姫、\nさん──双鉄、さんも──すごく、綺麗──で、んっ！」
- TW: 「美玖路有在看——啊——日日姬、小姐——還有雙鐵先生——都非常迷人——嗯！」
- VN cũ: 「Mikuro đang, nhìn ạ── Mikuro──っ──a── chị Hibiki,\n──anh Soutetsu, cũng── rất, đẹp── ạ, ưm!」
- Sửa: 「Mikuro đang, nhìn ạ── Mikuro──Ư──a── chị Hibiki, ──anh Soutetsu, cũng── rất, đẹp── ạ, ưm!」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2180 — 双鉄 — gasp
- JP: 「僕の妻たる日々姫になら──っ！」
- TW: 「而身為我妻子的日日姬——！」
- VN cũ: 「Nhưng nếu là Hibiki, người vợ của anh thì──っ!」
- Sửa: 「Nhưng nếu là Hibiki, người vợ của anh thì──Ư!」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2198 — みくろ — fa/fu
- JP: 「いい！　ですっ──すご──くっ──ふあっ！\nみく、ろっ──これっ──しゅきいっ」
- TW: 「舒服！非常舒爽——呼啊！美玖路好喜歡這樣」
- VN cũ: 「Sướng! Lắm ạ── rất── hự── fua!\nMiku, ro── cái này── thích lắmmm」
- Sửa: 「Sướng! Lắm ạ── rất── hự── phùa!\nMiku, ro── cái này── thích lắmmm」
- Lý do: JP ふあ/ふぁ: VN cũ romanisation — sửa theo quy tắc fa/fu đã chốt (ふあ→'phùa', ふぁ→'phà'; tiền lệ reinah3).

### 2200 — みくろ — gasp
- JP: 「はあっ──ふうっ──はああっ──ふううっ」
- TW: 「蛤啊——呼——蛤啊——呼」
- VN cũ: 「Hà── phu── hà── phu」
- Sửa: 「Hà── phu── hà── phuƯ」
- Lý do: JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất).

### 2201 — みくろ — gasp
- JP: 「はあっ──ん、ふっ──はひゅっ──くっふっ」
- TW: 「蛤啊——嗯、呼——哈——唔呼」
- VN cũ: 「Hà── ưm, phu── ha hyu── kufu」
- Sửa: 「Hà── ưm, phu── ha hyu── kufuƯ」
- Lý do: JP là từ âm thanh + っ cuối dòng, không dấu câu sau; VN cũ làm mất hẳn っ — thêm Ư theo quy tắc gasp đã chốt 20/11 (っ gắn từ âm thanh là gasp; chỉ thêm khi âm っ hoàn toàn mất).

### 2250 — みくろ — gasp
- JP: 「っ──。速くて、その、強そうに見えますけど……\n双鉄さん、痛い、とかなんですか？」
- TW: 「速度好快，而且好像還很用力的樣子……雙鐵先生會不會覺得痛啊？」
- VN cũ: 「っ──. Nhanh quá, cái đó, trông có vẻ mạnh bạo nhưng……\nAnh Soutetsu, có bị đau, hay gì không ạ?」
- Sửa: 「Ư──. Nhanh quá, cái đó, trông có vẻ mạnh bạo nhưng…… Anh Soutetsu, có bị đau, hay gì không ạ?」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2292 — みくろ — gasp
- JP: 「っ！！」
- TW: 「！！」
- VN cũ: 「っ!!」
- Sửa: 「Ư!!」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2293 — 双鉄 — gasp
- JP: 「っ！！！」
- TW: 「！！！」
- VN cũ: 「っ!!!」
- Sửa: 「Ư!!!」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2294 — 双鉄 — gasp
- JP: 「っ！！！！」
- TW: 「！！！！」
- VN cũ: 「っ!!!!」
- Sửa: 「Ư!!!!」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2295 — みくろ — gasp
- JP: 「っ！！！！！」
- TW: 「！！！！！」
- VN cũ: 「っ!!!!!」
- Sửa: 「Ư!!!!!」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2311 — 日々姫 — gasp
- JP: 「（あむっ）──んっ──ん～～。\nどぎゃん？　みくろ。おいしかものじゃなかけど」
- TW: 「（啊嗚）——嗯——嗯～～美玖路，要試試看嗎？雖然味道並不怎麼樣」
- VN cũ: 「（Amu）──Ưm──ưm~~.\nThế nào? Mikuro. Dù không phải là thứ ngon lành gì.」
- Sửa: 「（AmuƯ）──Ưm──ưm~~.\nThế nào? Mikuro. Dù không phải là thứ ngon lành gì.」
- Lý do: JP （あむっ） (tiếng ngậm miệng); VN cũ '(Amu)' phiên âm, っ mất hẳn — thêm Ư (phán đoán: giữ dạng phiên âm, chỉ bổ sung Ư).

### 2316 — 日々姫 — gasp
- JP: 「///っ」
- TW: 「（害羞）」
- VN cũ: 「///」
- Sửa: 「///Ư」
- Lý do: JP ///っ (gasp sau dấu đỏ mặt); VN cũ '///' làm mất hẳn gasp — thêm Ư.

### 2321 — 双鉄 — gasp
- JP: 「っ！？」
- TW: 「？！」
- VN cũ: 「っ!?」
- Sửa: 「Ư!?」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2322 — みくろ — gasp
- JP: 「っ！？　ん……ふっ──ふっ──ぁっ──」
- TW: 「？！嗯……呼——呼——啊」
- VN cũ: 「っ!? Ưm……phu──phu──a──」
- Sửa: 「Ư!? Ưm……phu──phu──a──」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2323 — 日々姫 — gasp
- JP: 「っ！？　にぃにっ」
- TW: 「？！阿哥」
- VN cũ: 「っ!? Anh hai.」
- Sửa: 「Ư!? Anh hai.」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2325 — 双鉄 — gasp
- JP: 「っ！！！？」
- TW: 「？！！！」
- VN cũ: 「っ!!!?」
- Sửa: 「Ư!!!?」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2328 — 日々姫 — gasp
- JP: 「～～～～～～～っ」
- TW: 「～～～～～～」
- VN cũ: 「~~~~~~~っ」
- Sửa: 「~~~~~~~Ư」
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2330 — みくろ — gasp
- JP: 「～～～～～～～～～～～～～～～～っっっっっっ！」
- TW: 「～～～～～～～～～～～！」
- VN cũ: 「~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!」
- Sửa: 「~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ƯƯƯƯƯƯ!」
- Lý do: Sweep っ: JP kết bằng 6 っ liên tiếp (～×16 + っ×6); VN cũ chỉ còn dấu ~ — fix sweep 6 Ư (đã kiểm chứng vs JP; tiền lệ đa-っ 19/11).

### 2595 — monologue — terminology
- JP: 幾百──という単位ではもう足りなくなった繰り返し。\n御一夜温泉駅ホームへの、8620形での入線。
- TW: 成百上千次——這樣的描述已經無法形容這周而復始的次數。８６２０型列車再一次進站，抵達御一夜溫泉站。
- VN cũ: Hàng trăm──đơn vị đó không còn đủ để đếm số lần lặp lại nữa.\nTiến vào sân ga suối nước nóng Ohimitera trên đầu máy 8620.
- Sửa: Hàng trăm──đơn vị đó không còn đủ để đếm số lần lặp lại nữa.\nTiến vào sân ga suối nước nóng Ohitoyo trên đầu máy 8620.
- Lý do: JP 御一夜温泉駅: VN cũ 'Ohimitera' — sai dạng tên đã chốt; sửa 'Ohitoyo' (quyết định 19/11).

### 2655 — monologue — gasp
- JP: 加速していく。まずいと感じる。\nこのままいけばほどなく射精をしてしまっ──っ！！？
- TW: 抽動的速度不斷加快，我感到了一陣危機感。這樣下去射精迫在眉睫——？！！
- VN cũ: Tôi đang tăng tốc. Tôi cảm thấy không ổn rồi.\nCứ thế này thì tôi sẽ xuất tinh mất──っ!!?
- Sửa: Tôi đang tăng tốc. Tôi cảm thấy không ổn rồi. Cứ thế này thì tôi sẽ xuất tinh mất──Ư!!?
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 2747 — monologue — fabrication
- JP: 日々姫は勃起を指で撫ぜあげ、\nぱっとその手を開いてみせる。
- TW: 日日姬用手指輕輕摩挲肉棒，隨後又攤開了手掌。
- VN cũ: Hibiki dùng ngón tay vuốt dọc theo dương vật cương cứng,\nrồi xòe tay ra làm động tác phác họa.
- Sửa: Hibiki dùng ngón tay vuốt dọc theo dương vật cương cứng,\nrồi xòe tay ra cho xem.
- Lý do: JP chỉ 'xòe tay ra cho xem'; VN cũ tự thêm 'làm động tác phác họa' — bỏ phần bịa.

### 2822 — monologue — gasp
- JP: あたる。みくろの最奥に。\n勃起の全てを収めきってはくれないが──っ！！？
- TW: 經歷一番千辛萬苦我終於插到美玖路的最深處。肉棒雖然並沒有整個進去——
- VN cũ: Chạm rồi. Tận sâu nhất của Mikuro.\nDù không thể chứa hết toàn bộ dương vật cương cứng của tôi nhưng──っ!!?
- Sửa: Chạm rồi. Tận sâu nhất của Mikuro. Dù không thể chứa hết toàn bộ dương vật cương cứng của tôi nhưng──Ư!!?
- Lý do: Sweep っ: VN cũ còn っ thô của JP — fix sweep thay っ→Ư (đã kiểm chứng vs JP, nhận nguyên fix sweep).

### 3143 — monologue — SFX
- JP: （もちっ）
- TW: （輕觸）
- VN cũ: （Béo má）
- Sửa: （Mềm mại）
- Lý do: JP （もちっ） (tiếng má bị bóp mềm, mochi); TW （輕觸）. VN cũ 'Béo má' (má béo — sai nghĩa, không diễn âm) — sửa 'Mềm mại' (phán đoán).

## §3. Kiểm chứng sweep っ

- Sweep có 31 mục cho file này: 28 raw-tsu + 2 lost-gasp-trailing + 1 already-rendered (2092, VN '──!' đã diễn gasp bằng dấu cảm thán — không sửa). Nhận nguyên 30 fix sweep (đã kiểm chứng từng fix vs JP; 2 fix 1743/1786 chỉ cộng thêm fa/fu ふあ→'phùa').
- Quét máy bổ sung bắt thêm 21 gasp sweep bỏ sót (1680, 1681, 1703, 1712, 1724, 1725, 1727, 1728, 1741, 1746, 1777, 1785, 1790, 1804, 1814, 1818, 1925, 2200, 2201, 2311, 2316): đều là từ âm thanh + っ cuối dòng, không dấu câu sau, VN phiên âm làm mất hẳn っ — sweep không bắt vì mẫu liệt kê chỉ bắt っ sau ──/～～/…… hoặc っ thô còn sót trong VN.
- Lưu ý: 10 fix sweep có VN nhiều dòng (1743, 1786, 1871, 1942, 2101, 2125, 2148, 2250, 2655, 2822) làm phẳng \n thành khoảng trắng theo quy ước single-line của sweep (game tự wrap; TOML-2 vốn cũng làm phẳng \n) — chỉ thay đổi ở っ, không đổi nghĩa. Các fix tự viết trong audit này giữ nguyên \n của VN cũ.
- Các dòng っ đã kiểm mà KHÔNG sửa (đã diễn đúng, không phải gasp mất): っ gắn từ nội dung (từ nhấn mạnh: 1917 ぜんぶっ, 1982 だっっ, 1927 みくろもっっ, 1662/1967 tên + っ), っ đã diễn bằng từ SFX tiếng Việt (ちゅっ→'Chụt', くっ→'Hự', んっ→'Ưm', ごちゅっ→'Phập'), っ sau từ âm thanh có !/?/── diễn cắt ngang (1768 わあっ!→'Oa!', 1800 ふうっ!→'Hự!', 1772 はわっ!?→'Hawa!?'), tiếng cười (ふふっ/うふふ/んふふ→'Fufu'/'Ufufu'/'Ưm fufu' — cười, không phải gasp; 1818 あはっ chỉ thiếu dấu '.' nên thêm '.').

## §4. Ghi chú / phán đoán

- 1705 (ふ……ぁ → 'Phu……a'): JP tự tách ふ và ァ bằng …… — dạng tách 'phù a' này thuộc đợt thống nhất fa/fu (không sửa trong audit, chờ đợt thống nhất).
- Số lượng nguyên âm tiếng rên dài: fix giữ nguyên số lượng a của VN cũ (không chuẩn hoá nghiêm): 1729 có 17 a (JP 14 âm a), 1731 có 7 a (JP 6 âm a). Có chuẩn hoá nghiêm theo quy tắc hay không — chờ Hieu (tiền lệ reinah3 §6 mục 3).
- ぷあ→'pùa' (1901, 1811): sửa theo tương tự nhóm fa/fu; chưa có tiền lệ trực tiếp cho ぷあ — Hieu xác nhận khi gộp.
- 1711 (ふぁうっ→'phàu'): ふぁ→'phà' + う→'u' — dạng ghép, chưa có tiền lệ trực tiếp — Hieu xác nhận khi gộp.
- 2309/2308: （はむっ！） và （はみゅっ！） đều dịch '(Ngoạm!)' — hai âm khác nhau (cắn mạnh / cắn nhẹ) nhưng cùng một cách diễn; giữ nguyên (không sai nghĩa rõ rệt), ghi chú để Hieu biết.
- 2242: 潮吹き → 'squirting' (giữ nguyên tiếng Anh) — chấp nhận được trong văn phong VN hiện tại, giữ nguyên.
- 2752: độc thoại kết bằng 'ゆえっ' (câu cụt, hàm ý tiếp nối) — VN hoàn thiện thành câu đầy đủ ('việc rút ra cũng đã trở nên khó nhọc'); ý chính giữ nguyên, không sửa.
- 1804 ('A──ưƯ.') và 2311 ('(AmuƯ)'): phán đoán thêm Ư cho っ mất hẳn sau phiên âm — đã ghi rõ trong lý do từng dòng.

## §5. Khối TOML (đã parse-kiểm chứng: 82 khóa, 0 sai lệch)

```toml
"1114" = "「──Ư! Ư~~~Ư」"
"1678" = "「Hyau── ưm── phùa── a──\\nA── a── a── aa──」"
"1680" = "「HyauƯ」"
"1681" = "「HyanƯƯ」"
"1703" = "「Phù──a──a──aaƯ.」"
"1707" = "「Phù. Đến ga suối nước nóng Ohitoyo. Đúng giờ.」"
"1708" = "「Phuê!? Lại nữa── Mikuro! Lại nữa!\\nBởi vì! Cương cứng! Bởi vì! Bởi vì!!」"
"1711" = "「Phùa── a── anh hai, tự nhiên lại, đưa cả hai ngón tay\\nvào thế── phàu!!!?」"
"1712" = "「Phà── a── a── aaƯ.」"
"1714" = "「Phùa── a── a── gì thế, này──\\nGì thế, này!! Sướng quá, Mikuro, sướng quá.」"
"1716" = "「Phùa── a── tuyệt quá── phuê!!?\\nA, Mikuro── xin lỗi, đồng phục── chị, làm bẩn mất rồi」"
"1718" = "「Phùa── a── tuyệt quá── thế này── a──\\nNhanh── mạnh── sâu, thế này」"
"1720" = "「Phùa── a── ngón tay của chị Hibiki…… ngón tay──\\nMikuro── âm vật của Mikuro, đang──」"
"1722" = "「Phùa── a── mở rộng ra── Mikuro──\\nđang được chị Hibiki── vạch ra, ạ」"
"1724" = "「PhùaƯ…… a── tuyệt── tuyệt quá──\\nƯm── nóng── hà── đẹp── đẹp quá……」"
"1725" = "「PhùaƯ…… a── chị Hibiki.\\nMikuro── là, a── Mikuro── ư, ưm」"
"1727" = "「PhùaƯ…… Mikuro…… chỗ phong ấn vừa được giải trừ──\\nchỗ con gái, toàn bộ── ở gần chị Hibiki thế này」"
"1728" = "「PhùaƯ.」"
"1729" = "「Phùaaaaaaaaaaaaaaaaan!!!!」"
"1731" = "「Phuyaaaaaaan! Mikuro, thích lắm!!\\nCái này, thích lắm! Được cọ xát, thích lắmmm」"
"1733" = "「Phùaa!? A──Mi, Mikuro, vừa nãy──\\nChỗ đó của Mikuro── sướng lắm ạ.」"
"1735" = "「Phùa! A! Cùng nhau── cùng nhauuu!」"
"1736" = "「Phùa a! A! Aaaa!!!!!!」"
"1737" = "「Phùa! A! Anh hai! Anh hai!!!!\\nHôm nay! Tuyệt quá── em── cảm nhận được!」"
"1739" = "「Phùa! A!! A── aaaa!!!!」"
"1741" = "「Phuya── gì thế, này── nóng quá──\\nBụng── vùng kín── nhão nhoét── phu── aƯ」"
"1743" = "「Phùa!? A── anh hai── nóng quá── ưm Hơn── mọi khi── nóng── và── to──Ư」"
"1746" = "「KuhaƯ.」"
"1758" = "「Hyua!? A── a…… phuê!?」"
"1767" = "「Ư! Oa」"
"1771" = "「Ư!!!!!!!!」"
"1773" = "「Hà── a── phu── phùa──」"
"1774" = "「Hà── a! Ư── ưm── ưm hưuuu」"
"1777" = "「Hà…… a── anh hai── anh hai──\\nCứ thế, mãi── chỉ có âm vật── ưm aƯ」"
"1785" = "「HauƯ.」"
"1786" = "「Hau! A! A! Aaa! Phùa──Ư──ưm! Ưm uuuu!!!」"
"1790" = "「O── oƯ」"
"1794" = "「Ư……a.」"
"1804" = "「A──ưƯ.」"
"1811" = "「A……ưm──chụt──chụt──chụt──fu\\n……ưm……liếm──liếm──liếmmm──pùa」"
"1814" = "「A…… anh hai── chỗ đó── ưm── aƯ」"
"1818" = "「Aha.」"
"1820" = "「Phàn!!」"
"1823" = "「A, không.」"
"1833" = "「Ưm──Ư──ê──liếm──liếmmmmm」"
"1857" = "「Ưm kyu! Phùa! A── trượt── tuột, ra── aaaa── anh hai── vào hết, mất」"
"1871" = "「Vâng ạ! Mikuro, muốn thế ạ! Vì vậy, Mikuro── sẽ làm thế! ──Ư!!」"
"1901" = "「Pùa──fufu, anh ấy bảo thế kìa. Mikuro.」"
"1925" = "「Chật, quá── phu── phuuuu── haaaaƯ」"
"1928" = "「Vâng ạ! Đúng vậy── ưm── chị Hibi, ki──\\nPhùa── Mikuro cũng, làm tình── làm tình, làm tình」"
"1942" = "「Đúng vậy. Vào trong âm đạo đó── hự── thế này── đưa── dương vật cương cứng── vào──ƯƯƯ」"
"1961" = "「Sao thế, Hibi──Ư!!!」"
"1967" = "「Muốn nhìn── ạ── ưm hưu── phùa── a,\\nMuốn nhìn, nhưng mà── Mikuro── sao thế này, Mikuro」"
"2100" = "「Mi……kuro──Ư」"
"2101" = "「Mikuro cũng── sẽ sớm. Cùng nhau, thôi── nhé ──Anh hai, chị, và──Ư──ba người, cùng nhau──」"
"2104" = "「Miku, ro──Ư──hự──a──」"
"2107" = "「Miku, ro── nhìn đi── a── phùa──\\nCái này── làm tình── của chị, và, anh hai」"
"2110" = "「Mikuro…… ──Mikuro…… bụng, em…」"
"2125" = "「Mikuro cũng, giống như Hibiki── hự── Thích, kiểu kích thích── này, nhỉ──Ư!!!」"
"2148" = "「Mikuro đang, nhìn ạ── Mikuro──Ư──a── chị Hibiki, ──anh Soutetsu, cũng── rất, đẹp── ạ, ưm!」"
"2180" = "「Nhưng nếu là Hibiki, người vợ của anh thì──Ư!」"
"2198" = "「Sướng! Lắm ạ── rất── hự── phùa!\\nMiku, ro── cái này── thích lắmmm」"
"2200" = "「Hà── phu── hà── phuƯ」"
"2201" = "「Hà── ưm, phu── ha hyu── kufuƯ」"
"2250" = "「Ư──. Nhanh quá, cái đó, trông có vẻ mạnh bạo nhưng…… Anh Soutetsu, có bị đau, hay gì không ạ?」"
"2292" = "「Ư!!」"
"2293" = "「Ư!!!」"
"2294" = "「Ư!!!!」"
"2295" = "「Ư!!!!!」"
"2311" = "「（AmuƯ）──Ưm──ưm~~.\\nThế nào? Mikuro. Dù không phải là thứ ngon lành gì.」"
"2316" = "「///Ư」"
"2321" = "「Ư!?」"
"2322" = "「Ư!? Ưm……phu──phu──a──」"
"2323" = "「Ư!? Anh hai.」"
"2325" = "「Ư!!!?」"
"2328" = "「~~~~~~~Ư」"
"2330" = "「~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ƯƯƯƯƯƯ!」"
"2595" = "Hàng trăm──đơn vị đó không còn đủ để đếm số lần lặp lại nữa.\\nTiến vào sân ga suối nước nóng Ohitoyo trên đầu máy 8620."
"2655" = "Tôi đang tăng tốc. Tôi cảm thấy không ổn rồi. Cứ thế này thì tôi sẽ xuất tinh mất──Ư!!?"
"2747" = "Hibiki dùng ngón tay vuốt dọc theo dương vật cương cứng,\\nrồi xòe tay ra cho xem."
"2822" = "Chạm rồi. Tận sâu nhất của Mikuro. Dù không thể chứa hết toàn bộ dương vật cương cứng của tôi nhưng──Ư!!?"
"3143" = "（Mềm mại）"
```

## §6. Lượt soát 2 + Chờ Hieu

- Lượt soát 2: 82/82 fix đọc lại đối chiếu JP — 82 giữ nguyên, 0 bỏ, 0 sửa. (Lượt soát có xét lại các phán đoán: 1804 'A──ưƯ.', 2311 '(AmuƯ)', 3143 'Mềm mại', ぷあ→'pùa', ふぁうっ→'phàu' — đều giữ nguyên như đã viết, chỉ ghi chú để Hieu xác nhận.)
- Chờ Hieu (không tự quyết):
  1. 1705 — ふ……ぁ tách ('Phu……a'): chuẩn hoá 'phà' hay giữ dạng tách? (thuộc đợt thống nhất fa/fu).
  2. Số lượng nguyên âm tiếng rên dài: có chuẩn hoá nghiêm không? (1729: 17 a vs JP 14; 1731: 7 a vs JP 6).
  3. ぷあ→'pùa' (1901, 1811) và ふぁうっ→'phàu' (1711): xác nhận dạng ghép này.
  4. 2309/2308: （はむっ！） và （はみゅっ！） đều '(Ngoạm!)' — có cần phân biệt cắn mạnh/nhẹ không?

## Kết bài

File lr追加_みくろ＆日々姫h「みくろのマスター」 đã audit xong toàn bộ 611 dòng: 82 dòng sai (13,4%) — 51 gasp (30 từ sweep + 21 sweep bỏ sót), 33 fa/fu (ふあ→'phùa', ふぁ→'phà', ふぇ/ふえ→'phuê', ふやぁ→'phuya', ぷあ→'pùa'), 2 thuật ngữ (御一夜→'Ohitoyo'), 5 bịa/dịch sai (2110 hoàn thiện câu cụt, 1823 'không được'→'không', 1857 'ra hết'→'vào hết', 2747 'phác họa', 3143 'Béo má'→'Mềm mại'). Không lệch dòng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 82 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 82/82, 0 bỏ, 0 sửa. Chờ Hieu: 1705 (ふ……ぁ tách), số lượng nguyên âm rên dài, ぷあ→'pùa' và ふぁうっ→'phàu', 2309/2308 cùng '(Ngoạm!)'.
