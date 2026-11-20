# Audit — 日々姫09_静かなる開戦 (02_Hibiki) — 15/401 (3,7%)

File: `日々姫09_静かなる開戦.txt.toml` — route 02_Hibiki, 401 dòng script.
Disk: `sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59eb09_#U9759#U304b#U306a#U308b#U958b#U6226.txt.toml` (tên file #U-escaped, đúng như trên đĩa).
Nội dung: họp báo từ chức của Paulette (báo chí chất vấn về kiêm nhiệm thị trưởng + Đường sắt Ohitoyo, trái phiếu đường sắt); Hibiki quyết định ứng cử thị trưởng; kế hoạch "chắp vá" toa xe phế liệu (8620 + KiHa 07S) trình bày trước các chủ trái phiếu; họp báo đối đầu của Kisaki trên TV; Hibiki sốt cao, cảnh Soutetsu bôi thuốc hạ sốt; Hibiki vượt qua căng thẳng, cất tiếng trước đám đông.
Nhân vật: monologue 198, 日々姫 64, 双鉄 61, ハチロク 20, ポーレット 16, 真闇 12, 赤井宮司 6, 債権者Ｂ 5, れいな 5, 債権者Ａ 5, 稀咲 3, 凪 2, ふかみ 2, 蓑笠 1, 記者Ａ 1.

Phương pháp: đọc toàn bộ 401 dòng theo từng hàng, đối chiếu JP + TW (CSV3), kiểm tra cơ học thêm (xem §3). Key order trong TOML == CSV3 order (xáo trộn, không phải story order) — người nghe/đại từ xác định theo nội dung và dòng kề trong luồng truyện, không theo key. Cơ sở tổng cộng đã kiểm chứng lại với ROUTE-AUDIT.md trước khi viết snippet: 86 file / 4.425 dòng sai — khớp với số parent giao.

## §1. Kết quả

Sai: **15/401 (3,7%)**.

Phân loại (15):
- **sfx/gasp っ**: 11 (1459, 1558, 1579, 1604, 1918, 1919, 1920 — 7 mục sweep, áp nguyên sau kiểm chứng; 1240, 1560, 1565, 1607 — 4 mục sweep bỏ sót, audit tự tìm).
- **xưng hô**: 1 (1715 — Soutetsu tự xưng "em" với Hibiki → "anh").
- **bịa thêm**: 2 (1205 — "Xin," không có trong JP; 1904 — Hibiki gọi "anh Soutetsu", JP không có tên).
- **sai nghĩa**: 1 (2679 — 素直 "ngoan ngoãn" → "thẳng thắn").

Không misaligned / không rotation / không contamination chéo file / không orphan / 0 untranslated (1235 chỉ là dấu ……; xem §4) / 0 duplicate key. Không lỗi đại từ hệ thống: Soutetsu "anh" với Hibiki xuyên suốt (thoại "anh"/"em" gọi Hibiki, 0 dòng "tôi" tự xưng trong thoại với Hibiki — đã quét toàn bộ thoại 双鉄); độc thoại kể chuyện đồng nhất "tôi". Không chắc chắn: 0.

Sweep っ-gasp: 8 mục cho file này trong `sweep-raw-gasp-wrong.json` — đã kiểm chứng từng mục với JP và áp dụng 7, 1 mục không sửa (1580 already-rendered, xem §4). Audit quét thêm toàn bộ dòng JP có っ và tìm thêm 4 gasp sweep bỏ sót (1240, 1560, 1565, 1607).

Strong candidates 6 → đọc toàn bộ tìm ra 15 sai: heuristic chỉ đếm được một phần. Lưu ý: 4/6 cờ strong-candidate (2139, 2567, 2601, 2737) là CŨ — tính từ CSV cũ; trong CSV3 cả 4 dòng đều đã đúng (2139 "Hachiroku hoảng hốt đến mức quên cả thêm chữ 'ngài'." khớp JP 「"様"をつけることさえ忘れるほどに」; 2567, 2601, 2737 cũng khớp JP/TW). Không có chuỗi xoay vòng trong file này.

## §2. Các lỗi và cách sửa

- **1205** — ポーレット: JP "「――は、\\n会見にお集まりいただきありがとうございます」"; TW "「——感謝各位前來參加本次發布會」"; VN cũ: "「――Xin,\\ncảm ơn mọi người đã đến dự buổi họp báo.」"; Sửa: "「――Cảm ơn mọi người đã đến dự buổi họp báo.」" — JP "――は、" là mảnh câu mở đầu (có thể là "はじめに" bị cắt ngang); VN cũ thêm "Xin," không có cơ sở trong JP. TW cũng bỏ qua "は". Sửa: bỏ "Xin,".
- **1240** — 日々姫: JP "「……あっ」"; TW "「……啊」"; VN cũ: "「……A.」"; Sửa: "「……Á!」" — JP 「……あっ」 là tiếng kêu ngắn, sắc (っ); VN cũ "……A." mất hẳn âm っ và thêm dấu chấm cuối câu (câu cảm thành câu trần thuật). Sửa "……Á!".
- **1459** — 債権者Ａ: JP "「複数輌をまとめてってよ、\\n御一夜鉄道にゃそぎゃんと多か車輌の必要――っ！」"; TW "「一次搬運複數車輛？御一夜鐵路要這麼多車輛——！」"; VN cũ: "「Bảo là di chuyển cùng lúc nhiều toa xe,\\nchứ Đường sắt Ohimitera đâu cần nhiều toa xe đến thế——!」"; Sửa: "「Bảo là di chuyển cùng lúc nhiều toa xe,\\nchứ Đường sắt Ohimitera đâu cần nhiều toa xe đến thế——Ư!」" — Sweep lost-gasp-trailing — đã kiểm chứng với JP (――っ): VN giữ dấu gạch nhưng mất gasp. Áp nguyên fix sweep; giữ "Ohimitera" (dạng cũ, chờ đợt thống nhất).
- **1558** — 日々姫: JP "「ひゃっ」"; TW "「呀」"; VN cũ: "「Hyaっ」"; Sửa: "「HyaƯ」" — Sweep raw-tsu — đã kiểm chứng: JP 「ひゃっ"; VN cũ giữ nguyên っ trong chữ hiển thị. Sửa "HyaƯ" (tiền lệ Hachiroku 12 再開発 2103/2537).
- **1560** — 日々姫: JP "「えっ――あっ――あのっ」"; TW "「呃……那、那個」"; VN cũ: "「Ơ——a——cái đó.」"; Sửa: "「Ớ——á——cái đó」" — JP có 3 tiếng えっ/あっ/あのっ; VN cũ "Ơ——a——cái đó." — "a" trần mất っ, thêm dấu chấm cuối câu không có trong JP. Sửa "Ớ——á——cái đó" (dấu sắc diễn っ của 2 tiếng cảm thán đầu; "cái đó" giữ nguyên cho あのっ ngập ngừng).
- **1565** — 日々姫: JP "「はぁっ――あっ――はぁッ――はぁっ」"; TW "「哈——啊——哈——哈」"; VN cũ: "「Hà――a――hà――hà.」"; Sửa: "「Hà――á――hà――hà」" — JP có 4 tiếng はぁっ/あっ/はぁッ/はぁっ; VN cũ "Hà――a――hà――hà." — "a" trần mất っ, dấu chấm cuối bịa thêm (JP kết bằng っ, không dấu câu). Sửa "Hà――á――hà――hà".
- **1579** — 日々姫: JP "「ふぁ～、生き返る～～っ」"; TW "「啊～活過來了～～」"; VN cũ: "「Phù~, sống lại rồi~~」"; Sửa: "「Phù~, sống lại rồi~~Ư」" — Sweep lost-gasp-trailing — đã kiểm chứng: JP 「ふぁ～、生き返る～～っ"; VN cũ giữ ~~ nhưng mất っ cuối. Sửa thêm Ư. (ふぁ → "Phù" đã có sẵn trong VN cũ, giữ — đúng quy tắc fa/fu.)
- **1604** — 双鉄: JP "「新聞か？　――っ」"; TW "「報紙——」"; VN cũ: "「Báo à? ——っ」"; Sửa: "「Báo à? ——Ư」" — Sweep raw-tsu — đã kiểm chứng: JP 「新聞か？　――っ"; VN cũ giữ nguyên っ. Sửa "——Ư".
- **1607** — 日々姫: JP "「むっ――あうっ、背中っ！\\nやっぱり、背中にぬってもらえますか？」"; TW "「塗在胸——唔，後背！還是後背吧。能幫我塗到後背上嗎？」"; VN cũ: "「Ngực――à không, lưng!\\nAnh bôi lên lưng cho em được không?」"; Sửa: "「Mừ――áu, ngực――à không, lưng!\\nAnh bôi lên lưng cho em được không?」" — JP 「むっ――あうっ、背中っ！」 — VN cũ bỏ hẳn 2 tiếng むっ (rên nghẹn) và あうっ (kêu đau), chỉ giữ "ngực――à không, lưng!". Thêm "Mừ――áu" (diễn ngẫu hứng theo nhân vật + ngữ cảnh, quy tắc Hieu 22:05). "Ngực――à không" GIỮ NGUYÊN: TW ghi rõ "塗在胸——唔，後背！" và ngữ cảnh (Soutetsu đang bôi thuốc, Hibiki chỉnh lại "lưng!") chứng tỏ có sự đối chiếu ngực→lưng; JP "背中っ！" nhấn mạnh cũng hàm ý sửa vị trí.
- **1715** — 双鉄: JP "「僕には、普通の会見に思えたが」"; TW "「我看不出記者會有什麼特別的地方」"; VN cũ: "「Với em thì, đó chỉ là một buổi họp báo bình thường thôi mà.」"; Sửa: "「Với anh thì, đó chỉ là một buổi họp báo bình thường thôi mà.」" — Soutetsu nói với Hibiki (Hibiki vừa nói 1713/1714, Soutetsu đáp ngay sau); JP 「僕には" — VN cũ "Với em thì" tự xưng "em" là sai: Soutetsu với Hibiki là "anh" (quy tắc đã chốt 20/11). Sửa "Với anh thì".
- **1904** — 日々姫: JP "「にぃに――兄さん。あの――ええと、\\nそろそろ会見の時間なのでは？」"; TW "「阿哥——哥哥。那個……是不是快到發表會的時間了？」"; VN cũ: "「Anh hai――anh Soutetsu. Dạ――ờm,\\nchắc sắp đến giờ họp báo rồi phải không ạ?」"; Sửa: "「Anh hai――anh. Dạ――ờm,\\nchắc sắp đến giờ họp báo rồi phải không ạ?」" — Hibiki gọi Soutetsu là にぃに/兄さん; JP không có tên "Soutetsu"; VN cũ "anh Soutetsu" là thêm tên bịa. TW cũng chỉ có 阿哥——哥哥. Sửa "Anh hai――anh."
- **1918** — 双鉄: JP "「っ！」"; TW "「！」"; VN cũ: "「!」"; Sửa: "「Ư!」" — Sweep lost-gasp-whole — đã kiểm chứng: JP toàn dòng chỉ có っ + dấu câu; VN cũ chỉ còn dấu câu. Sửa thêm Ư.
- **1919** — 双鉄: JP "「っ！！！」"; TW "「！！！」"; VN cũ: "「!!!」"; Sửa: "「Ư!!!」" — Sweep lost-gasp-whole — đã kiểm chứng: JP 「っ！！！"; VN cũ chỉ còn "!!!" Sửa "Ư!!!"
- **1920** — 双鉄: JP "「っ！？」\\n「っ！！」"; TW "「！？」\\n「！！」"; VN cũ: "「!?」\\n「!!」"; Sửa: "「Ư!?」\\n「Ư!!」" — Sweep lost-gasp-whole — đã kiểm chứng: JP 2 dòng っ + dấu câu; VN cũ chỉ còn dấu câu. Sửa thêm Ư cả 2 dòng.
- **2679** — monologue: JP "不満気な声を出しながら、\\nそれでも日々姫はやはり日々姫で、つまりは素直だ。"; TW "雖然日日姬在發牢騷，可她畢竟是個率直的女孩子。"; VN cũ: "Dù phát ra giọng điệu bất mãn,\\nnhưng Hibiki vẫn là Hibiki, tức là rất ngoan ngoãn."; Sửa: "Dù phát ra giọng điệu bất mãn,\\nnhưng Hibiki vẫn là Hibiki, tức là vẫn rất thẳng thắn." — JP 素直だ = thẳng thắn/trung thực (TW 率直 "thẳng thắn"); VN cũ "ngoan ngoãn" (vâng lời) lệch nghĩa. Sửa "vẫn rất thẳng thắn" ("vẫn" giữ sắc thái "やはり … vẫn là Hibiki").

## §3. Kiểm tra cơ học

- TOML: md5 bae1d4f5f013e11921d11475c235d70e; chỉ 1 bản sao trên đĩa (không thuộc nhóm 11 file trùng); BOM + CRLF giữ nguyên; 401 khóa script khớp CSV3 tuyệt đối, 0 khóa thừa/thiếu; `[selections]` rỗng (0 mục); 401/401 comment `# JP:` trong `[script]` khớp CSV3 JP tuyệt đối (26 comment `# JP:` còn lại thuộc `[characters]`/`[character_subs]`, không phải dòng script).
- CSV3 vs TOML-2: 255 khác biệt giá trị đều chỉ do TOML-2 làm phẳng literal `\n` thành khoảng trắng — 0 khác biệt thực sự; CSV3 là chuẩn cho fix list.
- Thẻ %l: 0 thẻ sai định dạng trong file (kiểm tra theo mẫu `\x%lTERM;#00ffc040;GLOSS%l;#;`); số thẻ VN == JP ở mọi dòng; 1899 thứ tự thẻ đảo do đảo câu (Railord trước 8620), gloss khớp đúng term — không lỗi. Không có thẻ thiếu dấu `;` đóng trong file này.
- Quét っ: mọi dòng JP có っ đã rà soát — 7 sweep + 4 tự tìm đã sửa; còn lại đều là っ nhấn mạnh gắn với từ (1907 起きてっ, 1798 これっ, 1588 うむっ, 1666 出ていますっ, 1638 凪ちゃんっ, 1460 ばいっ, 1889 社長っ) hoặc đã diễn bằng dấu câu/âm đóng (xem §4) — không thêm Ư, đúng quy tắc.
- Đại từ: quét toàn bộ thoại 双鉄 — 0 dòng "tôi" tự xưng; "em" tự xưng duy nhất 1715 (đã sửa); các "em" còn lại đều là gọi Hibiki (1467, 1499, 1509, 1512, 1517, 1749, 1751, 1789 — đúng). Hibiki "chúng tôi" 2 dòng (1685, 1856) là đại từ nhóm, dạng trung lập — giữ.
- Ohimitera: 17 dòng dạng cũ (1721, 2586, 1777, 1694, 1662, 2333, 1459, 1892, 1723, 1690, 1548, 1672, 1775, 1557, 2068, 1499, 1749) — KHÔNG tính sai, chờ đợt thống nhất (1459 đã sửa gasp nhưng giữ "Ohimitera").
- Không có chuỗi xoay vòng nội bộ (0 giá trị VN trùng nhau), không lệch hàng, không contamination chéo file, không orphan, 0 untranslated, 0 duplicate key. 1 dòng VN==TW (1235, chỉ dấu "……" — không tính, xem §4).

## §4. Đã kiểm tra và giữ nguyên (không tính sai)

- 1235 「…………」 → "…………": giữ — chỉ dấu lặng, không cần dịch; VN==TW không phải lỗi chưa dịch.
- 1580 (sweep already-rendered): JP 「ぅ～～ぁ～～っ」 → "Ư～～a～～" — gasp đã diễn, sweep cũng ghi không sửa.
- 1619 「痛……た、た……」 → "Đau…… đau quá……": giữ — "đau" lặp diễn tiếng lắp "た、た"; "quá" diễn mức độ nhấn, không phải bịa nghĩa.
- 1460 「八度！　三十八度ばいっ！」 → "Tám độ! Ba mươi tám độ lận đó!": giữ — Hibiki nói nhầm 8 độ rồi sửa thành 38; TW bỏ 八度 nhưng VN giữ đúng JP.
- 1685/1856 "chúng tôi" — giữ: đại từ nhóm, dạng trung lập theo brief (không theo quy tắc số ít).
- 1791 Hachiroku 「れいな、力をかしますよぉ！」 → "Reina, sẽ giúp một tay nha~!": giữ — "Reina" đọc dạng hô gọi (vocative), chủ ngữ lược là Hachiroku ("tôi sẽ giúp"), đúng JP.
- 2456 "慌てる指" — giữ: JP không nói rõ tay ai; VN giữ bỏ lửng đúng JP (TW nói tay Soutetsu nhưng JP bỏ lửng).
- 1199 "toàn bộ cấu trúc" cho 車輌全体 — giữ: toa xe được xem như một cấu trúc nguyên khối trong ngữ cảnh.
- 1555 "chính quyền bù nhìn" cho [レームダック,2]死に体 — giữ: diễn "lame duck" (bất lực, kéo dài) bằng "bù nhìn" là chấp nhận được; TW 跛腳鴨.
- 1620 「痛っ！？」 → "Đau!?": giữ — "!?" đã diễn độ sắc của っ.
- 1583 「んふっ――んっ――冷たッ―― / あうっ――気持ちっ――いいっ――」 → "Ưm――ưm――lạnh quá―― / Auu――cảm giác――thích quá――": giữ — các っ đã diễn bằng âm đóng ("Ưm") và từ nhấn ("quá").
- 1564 「こく、こく、こくっ――」 → "Ực, ực, ực――": giữ — âm "c" cuối diễn っ.
- 1907 「起きて、起きてっ！！」 → "Dậy đi, dậy đi!!": giữ — "!!" diễn っ nhấn mạnh.
- 2720–2725 SFX mô tả (ぺとっ→"Chạm nhẹ", ぬりっ→"thoa thoa", にゅるんっ→"trơn trượt", びしりっ→"Bốp!", かぽっ→"Cụp", シャーーーッ→"Vùuuu!", がつっ→"Cộp", ちゃぽん→"Tí tách") — giữ: diễn tả bằng nghĩa, nhất quán trong cảnh.
- 1607 "Ngực――à không" — giữ (xem §2.2/§2, mục 1607: TW + ngữ cảnh chứng tỏ có đối chiếu ngực→lưng).

## §5. Khối TOML (đã kiểm chứng parse)

```toml
"1205" = "「――Cảm ơn mọi người đã đến dự buổi họp báo.」"
"1240" = "「……Á!」"
"1459" = "「Bảo là di chuyển cùng lúc nhiều toa xe,\\nchứ Đường sắt Ohimitera đâu cần nhiều toa xe đến thế——Ư!」"
"1558" = "「HyaƯ」"
"1560" = "「Ớ——á——cái đó」"
"1565" = "「Hà――á――hà――hà」"
"1579" = "「Phù~, sống lại rồi~~Ư」"
"1604" = "「Báo à? ——Ư」"
"1607" = "「Mừ――áu, ngực――à không, lưng!\\nAnh bôi lên lưng cho em được không?」"
"1715" = "「Với anh thì, đó chỉ là một buổi họp báo bình thường thôi mà.」"
"1904" = "「Anh hai――anh. Dạ――ờm,\\nchắc sắp đến giờ họp báo rồi phải không ạ?」"
"1918" = "「Ư!」"
"1919" = "「Ư!!!」"
"1920" = "「Ư!?」\\n「Ư!!」"
"2679" = "Dù phát ra giọng điệu bất mãn,\\nnhưng Hibiki vẫn là Hibiki, tức là vẫn rất thẳng thắn."
```

Kiểm chứng: khối parse được bằng tomllib, 15 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\n` viết `\\n` nên parse ra đúng literal backslash-n của CSV3). Tất cả fix đều giữ nguyên ngắt dòng literal `\n` của VN cũ (không thêm `\n` thủ công mới). Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (xem log build).

## §6. Ghi chú cho Hieu (cần quyết / chờ thống nhất — không tính sai trong audit này)

- Thống nhất "Ohimitera" → "Ohitoyo" (17 dòng dạng cũ, liệt kê §3 — theo tiền lệ các file trước, fix trong đợt thống nhất).
- "thầy cúng Akai" (宮司) 5 dòng (1790, 2579, 2644, 2645, 2660) → "đền chủ" theo thuật ngữ đã chốt — chờ đợt thống nhất (không tính sai trong audit này).
- "xưởng rượu Migita" 1690 thiếu "Ichi" (JP 右田一酒造, TW giữ 一) — thuật ngữ đã chốt là "Migita Ichi"; ghi chú cho đợt thống nhất (không tính sai trong audit này).
- SFX 1607 "Mừ――áu", 1560 "Ớ——á", 1565 "Hà――á――hà――hà" là diễn ngẫu hứng theo quy tắc Hieu 22:05 — nếu Hieu muốn cách diễn khác thì đổi.
- Lượt soát 2: 15/15 tái kiểm chứng, 0 bỏ, 4 sửa lại (1205 khôi phục dấu 「」; 1459 + 2679 khôi phục ngắt dòng literal `\n` của VN cũ; 1240 khôi phục dấu 「」). JSON 15 khóa chuỗi; khối TOML parse OK, 15 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 15/15.

## Kết bài

File 日々姫09_静かなる開戦: 401 dòng đã đọc hết, **15 dòng sai (3,7%)** — 11 sfx/gasp っ (7 sweep + 4 tự tìm), 1 xưng hô, 2 bịa thêm, 1 sai nghĩa. Không có chuỗi xoay, không lệch hàng, không lỗi đại từ hệ thống — file khá sạch, lỗi tập trung ở SFX (đặc biệt các tiếng thở/gasp ngắn của Hibiki trong cảnh sốt + bôi thuốc). JSON 15 khóa chuỗi; khối TOML parse OK, 15 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 15/15; lượt soát 2: 15/15, 0 bỏ, 4 sửa.
