# Audit: Paulette lr_稀咲ポーレットh1_悪い大人の契約 (Kisaki Route Another — hợp đồng người lớn hư hỏng) — 85 dòng Việt sai (đã đối chiếu JP + TW)

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa từng dòng: 488 dòng (độc thoại 208, ポーレット 108, 稀咲 93, 双鉄 79), toàn bộ thuộc section `script`, đối chiếu JP + TW từ CSV3 và TOML-2.
- CSV vs TOML: 0 khác biệt thực chất (chỉ ở `\n`/khoảng trắng); tập key bằng nhau (488); `[selections]` rỗng; thẻ `%l`: 0 trong JP và 0 trong VN; không có key trùng; không có dòng VN trống; VN==TW 3 (985 `「……」`, 1902 `「～～～///」`, 964 `「——」` — cả ba đều đúng như vậy).
- md5: `342110f3930d8dcd96d8eaa574e0404a` — trùng khớp với bản sao ở `06_Kisaki/lr_稀咲ポーレットh1_悪い大人の契約.txt.toml` (nhóm trùng lặp 03_Paulette ↔ 06_Kisaki; bản sửa áp dụng cho CẢ HAI bản sao).
- Đọc toàn bộ 488 dòng phát hiện 85 dòng sai (17,4%). Thoại sai 72/280, lời dẫn sai 13/208. Theo người nói: 双鉄 30, ポーレット 29, 稀咲 13, độc thoại 13.
- Rà soát chéo với sweep gasp っ: sweep có 16 mục trong file này — 13 bản sửa (1597, 1816, 1894, 1895, 1896, 1897, 1906, 1908, 2135, 2178, 2309, 2349, 2501), audit xác nhận cả 13 cùng giá trị, không xung đột; 3 "already-rendered" (1599, 1892, 1893 — `Ư!!?`/`Ư!`/`Ư!!`), audit đồng ý, không đưa vào danh sách sửa. Audit phát hiện thêm 6 dòng gasp mà sweep BỎ SÓT trong file này (1596, 1598, 1902, 2236, 1567, 1590) — trong đó 1598 có hai っ mà cả sweep lẫn phụ lục đa-っ §9 đều bỏ sót, và 2236 là mục sweep ghi needs-file-audit, audit tự giải quyết.
- Quét máy tính bổ sung: quét xưng hô Soutetsu (chuẩn hoá `\n` thành khoảng trắng trước regex `\b`) bắt đủ 21 dòng "anh" (33 lần xuất hiện); quét `\bchu\b` toàn cột VN: 43 lần trúng — chỉ 1 lần là "chu" trần thật sự (1586, đã sửa), 42 lần còn lại là cách diễn âm tiết hợp lệ (`chu mu`, `chu pa`, `chu bu`, `chu ru`, `chu ku`, `chu ju`, `pê chu`, `Go chu`… — xem § "Đã kiểm tra"); quét mảnh La-tinh còn sót trong các dòng thở/SFX: 0 (ngoài các dòng đã sửa); kiểm tra VN trùng: 2 nhóm (xem dưới).
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ 85/85 bản sửa đối chiếu JP (đúng 85, 0 bị loại). Kiểm tra lần hai xác nhận: không có bản sửa nào thừa hưởng lỗi xưng hô của dòng cho (chỉ có 1 dòng dịch mới là 1509, xưng hô trong đó đã đúng — Paulette tự xưng "em", gọi "anh Soutetsu"); không có khoảng trắng thừa trước `\n` (bản sửa một dòng, không dùng `\n`); không có dấu 。 thay cho dấu .; các âm thở ghép viết liền một từ ("Kyaphù", "ha phù" là hai nhịp thở riêng — giữ nguyên); không còn mảnh La-tinh nào sót (`\bchu\b` = 1 lần thật đã sửa ở 1586; "pha" đứng riêng = 0; っ thô trong bản sửa = 0). **Bản sửa viết một dòng (khoảng trắng thay cho ngắt dòng), KHÔNG dùng `\n` thủ công** (như h5–h8).

## Kết luận về cơ chế lỗi

- **Không có mạng xoay vòng, không có tràn chương.** Chỉ có ĐÚNG 1 dòng lệch vị trí (1509 — VN cũ là bản sao y hệt VN của 1511; JP dòng này khác hẳn). Không có chuỗi xoay vòng, không có dòng nào phải thu hồi bản dịch từ dòng khác ngoài 1509 (dịch mới). Đây là file h "sạch về cấu trúc" như h1/h2/h4–h7 — lỗi tập trung ở xưng hô hệ thống + hơi thở + thở gấp + độ dài SFX.
- **Lỗi xưng hô hệ thống: Soutetsu tự xưng "anh" 21 dòng trong thoại (33 lần xuất hiện), "tôi" 0 lần** — cùng họ lỗi như h1–h8; độc thoại không có lần "Anh" nào sai (độc thoại dùng "tôi" đúng suốt file).
- **Hơi thở fa/fu hệ thống: 19 dòng dùng "pha"/"Pha" không dấu** — toàn bộ 19 dòng ふぁ/ふあ trong file đều sai (không có dòng nào đúng); cộng 4 dòng はぁっ dùng "Ha" thay vì "Hà". Đây là file có lỗi fa/fu dày đặc nhất từ trước tới nay (h1/h2 chỉ có 9 dòng).
- **Độ dài SFX: 6 dòng đếm thừa đúng gấp đôi** (2599, 2503, 2608, 2540, 2500, 2536) — VN cũ viết gấp đôi số âm u của JP (28 vs 8, 32 vs 16, 26 vs 13, 28 vs 14, 27 vs 13, 20 vs 10); cộng 5 dòng đếm lệch âm a/u ở các tiếng ré dài (1440, 1441, 1488, 1619) và 1 dòng 1470 thiếu 1 âm a.
- VN trùng trong file (2 nhóm) đều hợp lệ: 1509/1511 (1511 đúng, 1509 sai — xem § lệch vị trí); 2528 `(どさっ）` / 2495 `（とさっ）` cùng `（Phịch）` — cả hai đều là tiếng ngã, đúng.

## Chi tiết dòng sai

### Lệch vị trí (1 dòng)

**Key 1509 (ポーレット)**
- JP: "「はっ―あっ―はいって、くるっ―わたし―\\nわたしの、おまんこ、に―双鉄、くん、がっ―」"
- TW: "「哈——啊——進來、了——我——我的、小穴、裡——雙鐵、君，進來、了——」"
- VN cũ: "「Ha——a! A! A!! Vào rồi!\\nNóng quá——vừa nóng vừa to——đang ở bên trong, em.」"
- Sửa: "「Ha——a! A! A!! Đang vào, rồi——em——vào âm đạo, của em——anh Soutetsu——」"
- Lý do: Lệch vị trí: VN cũ là bản sao y hệt VN của 1511; JP dòng này khác hẳn (đang vào, chưa vào hẳn — "vào âm đạo, của em——anh Soutetsu——"). Dịch mới từ JP; 1511 đúng, không sửa. Nhóm trùng còn lại 2528/2495 （Phịch） đều đúng (cùng là tiếng ngã).

### Xưng hô — Soutetsu tự xưng "anh" trong thoại (21 dòng)

**Key 1786 (双鉄)**
- JP: "「状況的には、なにひとつとして。\\nむしろ僕は、稀咲の気持ちの方が気になる」"
- TW: "「畢竟情況如此。我反而更在意稀咲的心情」"
- VN cũ: "「Xét theo tình hình thì anh không thấy có gì đáng ghét cả.\\nAnh chỉ bận tâm đến cảm nhận của em thôi, Kisaki.」"
- Sửa: "「Xét theo tình hình thì tôi không thấy có gì đáng ghét cả. Tôi chỉ bận tâm đến cảm nhận của em thôi, Kisaki.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1666 (双鉄)**
- JP: "「僕―は、僕、はっ」"
- TW: "「我——哈、我、哈」"
- VN cũ: "「Anh——thì, anh, thì.」"
- Sửa: "「Tôi——thì, tôi, thì.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1708 (双鉄)**
- JP: "「僕の望みは、いつでも同じで変わらない。\\n稀咲を傷つけなるようなことだけは」"
- TW: "「我的願望一直都是一樣的。我希望不會傷害稀咲，僅此而已」"
- VN cũ: "「Mong muốn của anh, lúc nào cũng vậy, không hề thay đổi.\\nĐó là không bao giờ làm tổn thương Kisaki.」"
- Sửa: "「Mong muốn của tôi, lúc nào cũng vậy, không hề thay đổi. Đó là không bao giờ làm tổn thương Kisaki.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1694 (双鉄)**
- JP: "「僕は稀咲を愛しているし、稀咲とずっと一緒にいたい。\\nが、今は。ポーレットへの性欲を抱かずにもいられない」"
- TW: "「我愛稀咲，我想永遠和稀咲在一起。但是，現在。我忍不住對波萊特產生了性慾」"
- VN cũ: "「Anh yêu Kisaki, và muốn ở bên Kisaki mãi mãi.\\nNhưng hiện tại, anh cũng không thể kìm nén được dục vọng với Paulette.」"
- Sửa: "「Tôi yêu Kisaki, và muốn ở bên Kisaki mãi mãi. Nhưng hiện tại, tôi cũng không thể kìm nén được dục vọng với Paulette.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1415 (双鉄)**
- JP: "「この状況をお膳立てしたのが稀咲だということも、\\n僕の欲望に言い訳を与えている。流されてもいいか、と」"
- TW: "「即使製造這種狀況的是稀咲，也不能把它當成我的欲望的藉口。雖說我想隨波逐流」"
- VN cũ: "「Việc Kisaki sắp đặt tình huống này\\ncũng là một cái cớ cho dục vọng của anh. Rằng anh cứ thuận theo cũng được.」"
- Sửa: "「Việc Kisaki sắp đặt tình huống này cũng là một cái cớ cho dục vọng của tôi. Rằng tôi cứ thuận theo cũng được.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1379 (双鉄)**
- JP: "「が、流されることで稀咲に責任を負わせたくもない。\\nならば僕は、僕自身の意思で、こうと望もう」"
- TW: "「但我也不想讓稀咲因為我的隨波逐流而承擔責任。那麼，我就以我自己的意願，去期望，去做吧」"
- VN cũ: "「Nhưng, anh không muốn đổ trách nhiệm cho Kisaki vì anh đã thuận theo.\\nVậy nên, bằng chính ý chí của mình, anh mong muốn điều này.」"
- Sửa: "「Nhưng, tôi không muốn đổ trách nhiệm cho Kisaki vì tôi đã thuận theo. Vậy nên, bằng chính ý chí của mình, tôi mong muốn điều này.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1681 (双鉄)**
- JP: "「僕はポーレットともセックスしたい。その上できっと、\\n稀咲とより深く親密で強固な関係を築いていきたい」"
- TW: "「我也想和波萊特做愛。在此基礎上，我還想與稀咲建立更深入、更親密、更牢固的關係」"
- VN cũ: "「Anh cũng muốn làm tình với Paulette. Và hơn thế nữa,\\nanh muốn xây dựng một mối quan hệ sâu sắc, thân mật và bền chặt hơn với Kisaki.」"
- Sửa: "「Tôi cũng muốn làm tình với Paulette. Và hơn thế nữa, tôi muốn xây dựng một mối quan hệ sâu sắc, thân mật và bền chặt hơn với Kisaki.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1677 (双鉄)**
- JP: "「僕も―ぁっっ―くっ―んふっ―了解だ」"
- TW: "「我也——啊——嗚——嗯嗚——明白」"
- VN cũ: "「Anh cũng——a——ku——ưm fu——hiểu rồi.」"
- Sửa: "「Tôi cũng——a——ku——ưm fu——hiểu rồi.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1434 (双鉄)**
- JP: "「同意だ。なんの意義もない」"
- TW: "「同意。那些情況沒有任何意義」"
- VN cũ: "「Anh đồng ý. Không có ý kiến gì.」"
- Sửa: "「Tôi đồng ý. Không có ý kiến gì.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1689 (双鉄)**
- JP: "「我慢、している―しきれぬほどだ。\\nだから……だから、頼む―お願いだ、稀咲」"
- TW: "「我在，忍受——快忍不住了。所以……所以，求你——求求你了，稀咲」"
- VN cũ: "「Anh đang nhịn——đến mức không thể nhịn được nữa rồi.\\nVì thế……vì thế, xin em——anh xin em đấy, Kisaki.」"
- Sửa: "「Tôi đang nhịn——đến mức không thể nhịn được nữa rồi. Vì thế……vì thế, xin em——tôi xin em đấy, Kisaki.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1724 (双鉄)**
- JP: "「頼む、稀咲―最後の条項を―\\n僕らの契約に必要な、最後の条項を教えてほしい」"
- TW: "「拜託，稀咲——把最後一條——我們的合約需要的最後一條，告訴我」"
- VN cũ: "「Xin em đấy, Kisaki——điều khoản cuối cùng——\\nhãy cho anh biết điều khoản cuối cùng cần thiết cho hợp đồng của chúng ta đi.」"
- Sửa: "「Xin em đấy, Kisaki——điều khoản cuối cùng——hãy cho tôi biết điều khoản cuối cùng cần thiết cho hợp đồng của chúng ta đi.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 999 (双鉄)**
- JP: "「……誰か一人が嫌がる時点で、関係終了ということか。\\n了解だ、僕にはもちろん、なんの異論もない」"
- TW: "「……當出現一個人不願意繼續的時候，關係就結束了嗎？明白了，當然，我沒有異議」"
- VN cũ: "「……Nghĩa là chỉ cần một người không muốn nữa, mối quan hệ sẽ kết thúc sao.\\nAnh hiểu rồi, tất nhiên anh không có ý kiến gì.」"
- Sửa: "「……Nghĩa là chỉ cần một người không muốn nữa, mối quan hệ sẽ kết thúc sao. Tôi hiểu rồi, tất nhiên tôi không có ý kiến gì.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1781 (双鉄)**
- JP: "「このまま―され、たら―射精……するっ―ぁっ」"
- TW: "「照這樣——照這樣、下去的話——我會……射精——啊」"
- VN cũ: "「Cứ thế này——thì——anh sẽ……xuất tinh mất——a」"
- Sửa: "「Cứ thế này——thì——tôi sẽ……xuất tinh mất——a」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1396 (双鉄)**
- JP: "「見てくれ。これが、僕の勃起だ。\\nいまからこれで―僕は、ポーレットのことを貫く」"
- TW: "「你看。這就是我的勃起。從現在開始——我要用它貫穿波萊特」"
- VN cũ: "「Nhìn đi. Đây là dương vật đang cương cứng của anh.\\nTừ giờ trở đi——anh sẽ dùng nó, để xuyên thấu Paulette.」"
- Sửa: "「Nhìn đi. Đây là dương vật đang cương cứng của tôi. Từ giờ trở đi——tôi sẽ dùng nó, để xuyên thấu Paulette.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1700 (双鉄)**
- JP: "「ゆっくり進む。痛んだり嫌だったりしたらすぐ止める。\\nそのときは―そうだな、右手を上にあげてくれ」"
- TW: "「我會進去。如果你感到痛或者感到難受，我會馬上停止。要我停下的時候——對了，你可以把右手舉起來」"
- VN cũ: "「Anh sẽ vào từ từ. Nếu thấy đau hay khó chịu thì anh sẽ dừng lại ngay.\\nLúc đó——xem nào, em hãy giơ tay phải lên nhé.」"
- Sửa: "「Tôi sẽ vào từ từ. Nếu thấy đau hay khó chịu thì tôi sẽ dừng lại ngay. Lúc đó——xem nào, em hãy giơ tay phải lên nhé.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 970 (双鉄)**
- JP: "「―順番に、抱く。\\n気持ちの上では、ふたり同時に―三人一緒に」"
- TW: "「——我會輪流，跟你們做。在心中，我是同時和你們兩個人做——三個人同時在一起做」"
- VN cũ: "「——Anh sẽ lần lượt ôm hai người.\\nVề mặt cảm xúc, anh sẽ làm với cả hai cùng lúc——ba chúng ta cùng nhau.」"
- Sửa: "「——Tôi sẽ lần lượt ôm hai người. Về mặt cảm xúc, tôi sẽ làm với cả hai cùng lúc——ba chúng ta cùng nhau.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1731 (双鉄)**
- JP: "「だろうな……僕にも―余裕が、ない」"
- TW: "「是啊……我也——要撐、不住了」"
- VN cũ: "「Chắc vậy rồi……Anh cũng——không còn, dư dả gì.」"
- Sửa: "「Chắc vậy rồi……Tôi cũng——không còn, dư dả gì.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1737 (双鉄)**
- JP: "「なのか。わかった」"
- TW: "「是嗎？我知道了」"
- VN cũ: "「Vậy sao. Anh hiểu rồi.」"
- Sửa: "「Vậy sao. Tôi hiểu rồi.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1773 (双鉄)**
- JP: "「ポーレット―ポーレット……僕は、もう」"
- TW: "「波萊特，波萊特……我，已經」"
- VN cũ: "「Paulette——Paulette……Anh, sắp」"
- Sửa: "「Paulette——Paulette……Tôi, sắp」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1725 (双鉄)**
- JP: "「心得た」"
- TW: "「明白了」"
- VN cũ: "「Anh hiểu rồi.」"
- Sửa: "「Tôi hiểu rồi.」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

**Key 1761 (双鉄)**
- JP: "「礼をいわれるようなことは、なにも……」"
- TW: "「沒什麼值得你道謝的……」"
- VN cũ: "「Anh đâu làm gì đáng để được cảm ơn……」"
- Sửa: "「Tôi đâu làm gì đáng để được cảm ơn……」"
- Lý do: Soutetsu tự xưng "anh" trong thoại — JP 僕; quy tắc Soutetsu "Tôi" trong thoại (chỉ "Anh" với Hibiki).

### Hơi thở ふぁ/ふあ → "phà" (19 dòng)

**Key 1497 (ポーレット)**
- JP: "「わ―わ―こんなに優しく……おててでおちんちん、\\nいいこいいこってしてあげてるみたいな感じに……ふぁ」"
- TW: "「哇——哇——居然這麼溫柔……感覺就像小手手在跟小雞雞說，乖孩子乖孩子一樣……呼啊」"
- VN cũ: "「Oa——oa——dịu dàng quá……như thể đang dùng tay\\nvuốt ve khen ngợi dương vật là bé ngoan vậy……pha.」"
- Sửa: "「Oa——oa——dịu dàng quá……như thể đang dùng tay vuốt ve khen ngợi dương vật là bé ngoan vậy……phà.」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1468 (双鉄)**
- JP: "「ふぁぁあああっっ」"
- TW: "「呼啊啊啊啊啊啊」"
- VN cũ: "「Phaaaaaa」"
- Sửa: "「Phàaaaaa」"
- Lý do: JP ふぁぁあああっっ (ふぁ + あ×5 + っ×2) — VN cũ đếm đúng 6 âm a nhưng thiếu dấu huyền; sửa thành "Phàaaaaa".

**Key 1397 (ポーレット)**
- JP: "「セックス―セックス。双鉄くんと、稀咲と、セックス。\\n三人で……ふぁっ―ちゅむっ―ちゅぅぅっ―」"
- TW: "「做愛——做愛。和雙鐵君，和稀咲，一起做愛。三個人一起……呼啊——啾——啾——」"
- VN cũ: "「Làm tình——làm tình. Làm tình với anh Soutetsu và Kisaki.\\nBa người cùng nhau……pha——chu mu——chuu u——」"
- Sửa: "「Làm tình——làm tình. Làm tình với anh Soutetsu và Kisaki. Ba người cùng nhau……phà——chu mu——chuu u——」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1584 (ポーレット)**
- JP: "「ちゅううっ―ん……ちゅぱっ。ふぁ……\\nえと、稀咲…………。あの、ね？　―ありがとう」"
- TW: "「啾——嗯……啾。呼啊……呃，稀咲……。那個……　——謝謝」"
- VN cũ: "「Chuu u——ưm……chu pa. Pha……\\nƯm, Kisaki………… Nè? ——Cảm ơn em.」"
- Sửa: "「Chuu u——ưm……chu pa. Phà……Ưm, Kisaki………… Nè? ——Cảm ơn em.」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1464 (ポーレット)**
- JP: "「ふぁ―あ……セックス―。\\nセックス―わたし……したい…………んっ」"
- TW: "「呼啊——啊……做愛——做愛——我……想做…………嗯」"
- VN cũ: "「Pha——a……Làm tình——\\nLàm tình——em……muốn làm…………ưm.」"
- Sửa: "「Phà——a……Làm tình—— Làm tình——em……muốn làm…………ưm.」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1495 (ポーレット)**
- JP: "「ひゃっ！？　あ、双鉄くんの、指の、おなか―ふぁっ、\\nわたしの、おまんこ―入り口の、とこ―アウッ―」"
- TW: "「咿呀！？啊，雙鐵君的，手指的，肚子——呼啊、正在、我的——小穴的，入口——啊嗚——」"
- VN cũ: "「Hya!? A, phần bụng, ngón tay, của anh Soutetsu——pha,\\nđang ở, cửa mình——âm đạo, của em——au——」"
- Sửa: "「Hya!? A, phần bụng, ngón tay, của anh Soutetsu——phà, đang ở, cửa mình——âm đạo, của em——au——」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1472 (ポーレット)**
- JP: "「ふあっ！　あっ！　あっ！　あっ！　またっ―\\nやぁっ！　おねがい、おねがいっ―双鉄くぅんっ！」"
- TW: "「呼啊！　啊！　啊！　啊！　又來了——呀啊！　拜託，拜託了——雙鐵君！」"
- VN cũ: "「Pha! A! A! A! Lại nữa——\\nNhá! Xin anh, xin anh đấy——anh Soutetsu!」"
- Sửa: "「Phà! A! A! A! Lại nữa—— Nhá! Xin anh, xin anh đấy——anh Soutetsu!」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1481 (ポーレット)**
- JP: "「ふぁっっ！！！！！」"
- TW: "「呼啊！！！！！！」"
- VN cũ: "「Pha!!!!!」"
- Sửa: "「Phà!!!!!」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1523 (ポーレット)**
- JP: "「はっ！　あっ！？　やっ―うそっ―ふあっ―\\nいっぱい、なのに―みちみち、してて、きつい、のに」"
- TW: "「哈！　啊！不要——騙人——呼啊——明明都、滿滿的了——滿滿的、緊緊的」"
- VN cũ: "「Ha! A!? A——không thể nào——pha——\\nĐầy ắp, rồi mà——căng cứng, chật chội, thế mà.」"
- Sửa: "「Ha! A!? A——không thể nào——phà—— Đầy ắp, rồi mà——căng cứng, chật chội, thế mà.」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1641 (ポーレット)**
- JP: "「すご、いっ―やぁ―はずかしっ―わたし、だって、\\n―処女なのに―はじめてなのに―こんな、ふぁ」"
- TW: "「好厲、害——呀——好害羞——我、還是——處女——還是第一次——卻這樣、嗚啊」"
- VN cũ: "「Tuyệt, quá——a——xấu hổ quá——em, rõ ràng,\\n——vẫn còn trinh——là lần đầu tiên——vậy mà, pha.」"
- Sửa: "「Tuyệt, quá——a——xấu hổ quá——em, rõ ràng, ——vẫn còn trinh——là lần đầu tiên——vậy mà, phà.」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1480 (ポーレット)**
- JP: "「ふあっ！！　いい、いいよぉ！　相性、いいのっ―\\nふあっ！　うれし―嬉しいっ―嬉しい、嬉しいっ！」"
- TW: "「呼啊！！好，好舒服！　身體，好合適——呼啊！　好高興——好高興——好高興、好高興！」"
- VN cũ: "「Pha!! Thích, thích lắm! Hợp nhau, lắm——\\nPha! Vui——vui quá——vui quá, vui quá đi!」"
- Sửa: "「Phà!! Thích, thích lắm! Hợp nhau, lắm—— Phà! Vui——vui quá——vui quá, vui quá đi!」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1477 (ポーレット)**
- JP: "「ふあっ！　んっ！　おまんこ、おまんこっ！\\nわたしの、なに、これっ―ぎゅううって、して、ふあ」"
- TW: "「呼啊！　嗯！　小穴，小穴！！我的、小穴、怎麼——好緊、嗚啊」"
- VN cũ: "「Pha! Ưm! Âm đạo, âm đạo!\\nCủa em, gì thế, này——đang siết chặt, lấy, pha」"
- Sửa: "「Phà! Ưm! Âm đạo, âm đạo! Của em, gì thế, này——đang siết chặt, lấy, phà」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1467 (ポーレット)**
- JP: "「ふぁ……あ―ぁ……ん―（ごくっ）―いっぱい、\\nせい、えき―双鉄、くんの……溢れ、そう……」"
- TW: "「呼啊……啊——啊……嗯——（咕嘟）——滿、滿的精液——雙鐵、君的……快溢出、來了……」"
- VN cũ: "「Pha……a——a……ưm——（Ực）——đầy ắp,\\ntinh, dịch——của anh, Soutetsu……sắp tràn, ra rồi……」"
- Sửa: "「Phà……a——a……ưm——（Ực）——đầy ắp, tinh, dịch——của anh Soutetsu……sắp tràn, ra rồi……」"
- Lý do: JP ふぁ — "phà" theo quy tắc fa/fu (VN cũ "Pha"); đồng thời sửa dấu phẩy sở hữu "của anh, Soutetsu" → "của anh Soutetsu" (双鉄くんの là sở hữu, không phải xưng hô).

**Key 1536 (稀咲)**
- JP: "「ぁ―ふあっ―あっ」"
- TW: "「啊——呼啊——啊！」"
- VN cũ: "「A——pha——a」"
- Sửa: "「A——phà——a」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1475 (稀咲)**
- JP: "「ふぁっ！　あっ！　あっ！　あっ！　あっ！　あっ！\\nあっ！　あっ！　そう、てつ―双鉄ぅ―んっ！」"
- TW: "「呼啊！　啊！　啊！　啊！　啊！　啊！啊！　啊！　雙、鐵——雙鐵——嗯！」"
- VN cũ: "「Pha! A! A! A! A! A!\\nA! A! Anh, Soutetsu——anh Soutetsu——ưm!」"
- Sửa: "「Phà! A! A! A! A! A! A! A! Anh, Soutetsu——anh Soutetsu——ưm!」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1470 (稀咲)**
- JP: "「ふぁああああん！　双鉄、ね？　そうてつぅ―あっ、\\nボク、ね？　ボクっ―ボク、もう、もう、もうっ！」"
- TW: "「呼啊啊啊啊啊！　雙鐵……　雙鐵——啊、我，啊……　我——我、已經、已經、已經」"
- VN cũ: "「Pha a a a a n! Anh Soutetsu, nè? Anh Soutetsu——a,\\nem, nè? Em——em, sắp, sắp, sắp rồi!」"
- Sửa: "「Phà a a a a a n! Anh Soutetsu, nè? Anh Soutetsu——a, em, nè? Em——em, sắp, sắp, sắp rồi!」"
- Lý do: JP ふぁああああん — 6 âm a (ふぁ + あ×5); VN cũ chỉ 5 âm a ("Pha a a a a n!"); thêm một âm a + dấu huyền.

**Key 1624 (稀咲)**
- JP: "「うんっ！　うんっ！　がまん―しゅるっ―けどっ\\nだけど―ふあっ！　あっ―ボク―ボクっ！　もう」"
- TW: "「嗯！　嗯！　我會——忍的——但是——呼啊！　啊——我——我！　已經」"
- VN cũ: "「Ưm! Ưm! Em sẽ——nhịn——nhưng mà\\nnhưng mà——pha! A——em——em! Sắp」"
- Sửa: "「Ưm! Ưm! Em sẽ——nhịn——nhưng mà nhưng mà——phà! A——em——em! Sắp」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1478 (稀咲)**
- JP: "「ふあっ！　双鉄！　そうてつ、そうてつぅっ―」"
- TW: "「呼啊！　雙鐵！　雙鐵、雙鐵——」"
- VN cũ: "「Pha! Anh Soutetsu! Anh Soutetsu, anh Soutetsu——」"
- Sửa: "「Phà! Anh Soutetsu! Anh Soutetsu, anh Soutetsu——」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

**Key 1513 (稀咲)**
- JP: "「はぁ―んっ―ふぁ―あ―。そう、てつ―\\n双鉄―ふふっ―よく頑張ったね。双鉄、おいで？」"
- TW: "「哈——嗯——呼啊——啊——雙、鐵——雙鐵——呼呼——你真的很努力。雙鐵，過來吧？」"
- VN cũ: "「Ha——ưm——pha——a——. Anh, Soutetsu——\\nAnh Soutetsu——fufu——anh đã cố gắng lắm rồi. Lại đây nào, anh Soutetsu?」"
- Sửa: "「Ha——ưm——phà——a——. Anh, Soutetsu—— Anh Soutetsu——fufu——anh đã cố gắng lắm rồi. Lại đây nào, anh Soutetsu?」"
- Lý do: JP ふぁ/ふあ — theo quyết định 19/11 phải là "phà"/"Phà"; VN cũ "pha"/"Pha" không dấu (sai quy tắc fa/fu).

### Hơi thở はぁっ → "Hà" (4 dòng)

**Key 1825 (ポーレット)**
- JP: "「はぁっ―はぁっ―はぁっ―はあっ―（ごくっ）\\n―そうてつ、くん？」"
- TW: "「蛤啊——蛤啊——蛤啊——蛤啊——（咕嘟）——雙鐵、君？」"
- VN cũ: "「Ha——ha——ha——ha——（Ực）\\n——Anh Soutetsu?」"
- Sửa: "「Hà——Hà——Hà——Ha——（Ực） ——Anh Soutetsu?」"
- Lý do: JP はぁっ ×3 + はあっ ×1 — theo tiền lệ h8 2416, はぁっ phải là "Hà"; はあっ (không っ) giữ "Ha".

**Key 1824 (ポーレット)**
- JP: "「はぁっ―ぁっ―平気―ンッ―わたし―\\nおまんこ、平気―です―だから―そうてつ、くん」"
- TW: "「蛤啊——啊——沒事——嗯——我的——小穴、沒事——所以——雙鐵、君」"
- VN cũ: "「Ha——a——không sao——ưm——em——\\nâm đạo, không sao——đâu——nên là——anh Soutetsu.」"
- Sửa: "「Hà——a——không sao——ưm——em—— âm đạo, không sao——đâu——nên là——anh Soutetsu.」"
- Lý do: JP はぁっ — theo tiền lệ h8 2416 phải là "Hà"; VN cũ "Ha" (mất っ).

**Key 1826 (双鉄)**
- JP: "「はぁっ！　はあっ！　はあっ！　はあっ！」"
- TW: "「蛤啊　蛤啊！　蛤啊！　蛤啊！」"
- VN cũ: "「Ha! Ha! Ha! Ha!」"
- Sửa: "「Hà! Ha! Ha! Ha!」"
- Lý do: JP はぁっ ×1 + はあっ ×3 — はぁっ phải là "Hà" (tiền lệ h8 2416); はあっ giữ "Ha".

**Key 1569 (稀咲)**
- JP: "「ぁっ！　はあっ―あっ―あっ！！！！」"
- TW: "「啊！　哈——啊——啊！！！！」"
- VN cũ: "「A! Ha——a——a!!!!」"
- Sửa: "「A! Hà——a——a!!!!」"
- Lý do: JP はあっ — theo tiền lệ h8 2416 phải là "Hà"; VN cũ "Ha" (mất っ).

### Thở gấp っ — sweep xác nhận cùng giá trị (13 dòng)

**Key 1597 (ポーレット)**
- JP: "「っ！！！」"
- TW: "「嗚！！！」"
- VN cũ: "「!!!」"
- Sửa: "「Ư!!!」"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP 「っ！！！」 bị bỏ mất trong VN.

**Key 1816 (ポーレット)**
- JP: "「おな、か―下、はら―おまん、こ―きつ、くて\\n―ぎゅうぎゅう―わたし、いっぱい、でっ―っ！」"
- TW: "「肚子、裡——下面——小穴——好、緊——緊繃繃的——我、裝得、滿滿的——！」"
- VN cũ: "「Bụ, ng——bụng, dưới——âm, đạo——chật, quá\\n——chật ních——em, bị nhét đầy, mất——!」"
- Sửa: "「Bụ, ng——bụng, dưới——âm, đạo——chật, quá ——chật ních——em, bị nhét đầy, mất——Ư!」"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP kết bằng ―っ！ bị bỏ mất trong VN.

**Key 1894 (双鉄)**
- JP: "「っ！！！！」"
- TW: "「！！！！」"
- VN cũ: "「!!!!」"
- Sửa: "「Ư!!!!」"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP 「っ！！！！」 bị bỏ mất trong VN.

**Key 1895 (双鉄)**
- JP: "「っ！！！！！！！」"
- TW: "「！！！！！！！」"
- VN cũ: "「!!!!!!!」"
- Sửa: "「Ư!!!!!!!」"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP 「っ！！！！！！！」 bị bỏ mất trong VN.

**Key 1896 (双鉄)**
- JP: "「っ！！！！！！！！！！！」"
- TW: "「！！！！！！！！！！！」"
- VN cũ: "「!!!!!!!!!!!」"
- Sửa: "「Ư!!!!!!!!!!!」"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP 「っ！！！！！！！！！！！」 bị bỏ mất trong VN.

**Key 1897 (双鉄)**
- JP: "「っ！！！？」"
- TW: "「！！！？」"
- VN cũ: "「!!!?」"
- Sửa: "「Ư!!!?」"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP 「っ！！！？」 bị bỏ mất trong VN.

**Key 1906 (双鉄)**
- JP: "「～～～～っ！！！」"
- TW: "「～～～～嗚！！！」"
- VN cũ: "「～～～～!!!」"
- Sửa: "「～～～～Ư!!!」"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP 「～～～～っ！！！」 bị bỏ mất trong VN.

**Key 1908 (双鉄)**
- JP: "「～～～～～っ！！」"
- TW: "「～～～～～！！」"
- VN cũ: "「～～～～～!!」"
- Sửa: "「～～～～～Ư!!」"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP 「～～～～～っ！！」 bị bỏ mất trong VN.

**Key 2135 (monologue)**
- JP: "胸を僅かに押された気がして―っ！？"
- TW: "感覺胸口被輕輕按了一下——！？"
- VN cũ: "Cảm giác ngực vừa bị ấn nhẹ——!?"
- Sửa: "Cảm giác ngực vừa bị ấn nhẹ——Ư!?"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP ―っ！？ bị bỏ mất trong VN.

**Key 2178 (monologue)**
- JP: "解る。感じる。ポーレットの子宮口も僕の精液を求めてる。\\n一番奥を突く度に、控えめに甘く吸い付いてきて―っ！"
- TW: "我知道。我能感覺到。波萊特的子宮口也渴求著我的精液。每次插入最深處，那裡都會溫柔甜蜜地吸附過來——！"
- VN cũ: "Tôi biết. Tôi cảm nhận được. Cửa tử cung của Paulette cũng đang khao khát tinh dịch của tôi.\\nMỗi lần đâm vào nơi sâu nhất, nó lại khẽ khàng mút lấy một cách ngọt ngào——!"
- Sửa: "Tôi biết. Tôi cảm nhận được. Cửa tử cung của Paulette cũng đang khao khát tinh dịch của tôi. Mỗi lần đâm vào nơi sâu nhất, nó lại khẽ khàng mút lấy một cách ngọt ngào——Ư!"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP kết bằng ―っ！ bị bỏ mất trong VN.

**Key 2309 (monologue)**
- JP: "稀咲の子宮の入り口が強烈に亀頭を吸引してくる。\\n精液全部を呑み込もうとして―っ！！"
- TW: "稀咲的子宮入口強烈地吸吮著龜頭。她想要吞下我的所有精液——！！"
- VN cũ: "Cửa tử cung của Kisaki hút lấy quy đầu một cách mãnh liệt.\\nNhư muốn nuốt trọn toàn bộ tinh dịch của tôi——!!"
- Sửa: "Cửa tử cung của Kisaki hút lấy quy đầu một cách mãnh liệt. Như muốn nuốt trọn toàn bộ tinh dịch của tôi——Ư!!"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP kết bằng ―っ！！ bị bỏ mất trong VN.

**Key 2349 (monologue)**
- JP: "きゅっと。ポーレットの右手がシーツをつかむ―っ！"
- TW: "緊緊地。波萊特的右手抓住了床單——！"
- VN cũ: "Siết chặt. Bàn tay phải của Paulette túm chặt lấy ga giường——!"
- Sửa: "Siết chặt. Bàn tay phải của Paulette túm chặt lấy ga giường——Ư!"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP kết bằng ―っ！ bị bỏ mất trong VN.

**Key 2501 (monologue)**
- JP: "（なるほど、これが―\\n三人でセックスするということか―っ！！？）"
- TW: "（原來如此，這就是——三個人一起做愛的感覺——！！？）"
- VN cũ: "（Ra là vậy, đây chính là——\\nlàm tình ba người sao——!!?）"
- Sửa: "（Ra là vậy, đây chính là—— làm tình ba người sao——Ư!!?）"
- Lý do: Sweep gasp っ xác nhận (cùng giá trị): JP kết bằng ―っ！！？ bị bỏ mất trong VN.

### Thở gấp っ — sweep bỏ sót (6 dòng)

**Key 1596 (ポーレット)**
- JP: "「っ！！　―（ごくっ）」"
- TW: "「嗚！！——（吞嚥）」"
- VN cũ: "「!! ——（Ực）」"
- Sửa: "「Ư!! ——（Ực）」"
- Lý do: Gasp っ sweep BỎ SÓT: JP 「っ！！」 đầu dòng bị bỏ mất trong VN (sweep chỉ bắt các dòng っ ở cuối/cả dòng).

**Key 1598 (ポーレット)**
- JP: "「っっ！！！！！」"
- TW: "「嗚！！！！！！！」"
- VN cũ: "「Ư!!!!!」"
- Sửa: "「ƯƯ!!!!!」"
- Lý do: Gasp っ sweep BỎ SÓT (cả phụ lục đa-っ §9 cũng bỏ sót): JP 「っっ！！！！！」 có HAI っ — một Ư cho một っ, VN cũ chỉ có một Ư.

**Key 1902 (ポーレット)**
- JP: "「～～～っ///」"
- TW: "「～～～///」"
- VN cũ: "「～～～///」"
- Sửa: "「～～～Ư///」"
- Lý do: Gasp っ sweep BỎ SÓT: JP 「～～～っ///」 bị bỏ mất trong VN.

**Key 2236 (monologue)**
- JP: "ポーレットの手が僕から離れる。離れて―っ！\\nぺろりと小さく、赤い舌先で先走り汁の味をみる。"
- TW: "波萊特的手離開了我。然後——她用小巧玲瓏、紅色的舌尖品嘗著預射精液的味道。"
- VN cũ: "Tay Paulette rời khỏi người tôi. Rời khỏi——!\\nCô ấy thè chiếc lưỡi đỏ chót nhỏ xíu ra nếm thử mùi vị của nước nhờn."
- Sửa: "Tay Paulette rời khỏi người tôi. Rời khỏi——Ư! Cô ấy thè chiếc lưỡi đỏ chót nhỏ xíu ra nếm thử mùi vị của nước nhờn."
- Lý do: Gasp っ sweep ghi needs-file-audit — audit tự giải quyết: JP 離れて―っ！ bị bỏ mất trong VN.

**Key 1567 (ポーレット)**
- JP: "「っ！―射精っ！？　射精って―射精って……はぅ」"
- TW: "「啊！——射精！？射精是說——射精是說……哈嗚」"
- VN cũ: "「A! ——Xuất tinh!? Xuất tinh——xuất tinh là……hau」"
- Sửa: "「Ư! ——Xuất tinh!? Xuất tinh——xuất tinh là……hau」"
- Lý do: Gasp っ sweep BỎ SÓT: JP mở đầu bằng 「っ！」 nhưng VN cũ diễn thành "A!" — phải là "Ư!".

**Key 1590 (双鉄)**
- JP: "「っ―きさ、きっ―～～～っ！　きもち……いい」"
- TW: "「嗚——稀、咲——～～～！　好舒服……」"
- VN cũ: "「Ư——Kisa, ki——～～～! Sướng……quá」"
- Sửa: "「Ư——Kisa, ki——～～～Ư! Sướng……quá」"
- Lý do: Gasp っ sweep BỎ SÓT: JP 「～～～っ！」 giữa dòng bị bỏ mất trong VN.

### Sai nghĩa / lỗi đánh máy (8 dòng)

**Key 1386 (稀咲)**
- JP: "「イヤじゃ、ない？」"
- TW: "「你不想嗎？」"
- VN cũ: "「Anh không, ghét sao?」"
- Sửa: "「Anh không ghét sao?」"
- Lý do: JP 「イヤじゃ、ない？」 ("Anh không thích sao?") — VN cũ có dấu phẩy thừa "Anh không, ghét sao?" làm sai nhịp câu hỏi.

**Key 1502 (ポーレット)**
- JP: "「わっ！？　えっ！！？　おちん、ちんの―その、タマ\\n―えと……そんなに、ワシって―掴んでも……」"
- TW: "「哇！？哎！！？小雞、雞的——那個、蛋蛋——那個……就算這樣，一下子抓住……」"
- VN cũ: "「Oa!? Ế!!? Của dương, vật——cái đó, bi\\n——ưm……túm chặt, như thế——có sao không……」"
- Sửa: "「Oa!? Ế!!? Của dương, vật——cái đó, bi ——ưm……túm chặt, như thế——……」"
- Lý do: JP 掴んでも…… bỏ lửng (không kết thúc câu) — VN cũ tự bịa thêm phần kết "có sao không"; bỏ phần bịa, giữ dấu lửng theo JP (tiền lệ P13 1510/P16 1838).

**Key 2232 (monologue)**
- JP: "真っ赤になって歯を食いしばり、目尻に涙を一杯ためて、\\nポーレットはそれでもはっきり、僕の目を見て何度も頷く。"
- TW: "波萊特滿臉通紅，咬緊牙關，眼角含滿了淚水，但她還是看著我的眼睛，明確地點了好幾次頭。"
- VN cũ: "Đỏ bừng mặt, nghiến chặt răng, khóえ mắt đẫm lệ,\\nnhưng Paulette vẫn nhìn thẳng vào mắt tôi và gật đầu dứt khoát nhiều lần."
- Sửa: "Đỏ bừng mặt, nghiến chặt răng, khóe mắt đẫm lệ, nhưng Paulette vẫn nhìn thẳng vào mắt tôi và gật đầu dứt khoát nhiều lần."
- Lý do: Lỗi đánh máy: VN cũ lẫn ký tự Nhật "え" trong "khóえ mắt" — phải là "khóe mắt" (JP 目尻).

**Key 1644 (ポーレット)**
- JP: "「ほし、い、のっ―や、ぁ―そうてつ、く―の―\\nせいえき、せいえき―わたしの、おく、にっ！！」"
- TW: "「好想、要——呀、啊——雙鐵、君——的——精液、精液——射在、我的、裡面！！」"
- VN cũ: "「Muốn, quá——ya, a——của anh, Soutetsu——\\ntinh dịch, tinh dịch——vào sâu, bên trong, em!!」"
- Sửa: "「Muốn, quá——ya, a——của anh Soutetsu—— tinh dịch, tinh dịch——vào sâu, bên trong, em!!」"
- Lý do: Dấu phẩy sai sở hữu/xưng hô: JP 双鉄くんの là sở hữu ("tinh dịch của anh Soutetsu"); VN cũ "của anh, Soutetsu" ngắt thành xưng hô.

**Key 997 (ポーレット)**
- JP: "「……大丈夫、なら―双鉄くんが、オーケーなら、\\nセックス。凄く、してほしいです。双鉄、くんの―」"
- TW: "「……如果，不要緊的話——如果雙鐵君，沒意見的話，那麼……我非常希望，做愛。跟雙鐵君——」"
- VN cũ: "「……Nếu, không sao——nếu anh Soutetsu, OK,\\nthì em rất muốn, làm tình. Của anh, Soutetsu——」"
- Sửa: "「……Nếu, không sao——nếu anh Soutetsu, OK, thì em rất muốn, làm tình. Của anh Soutetsu——」"
- Lý do: Dấu phẩy sai sở hữu/xưng hô: JP 双鉄くんの― là sở hữu ("của anh Soutetsu"); VN cũ "Của anh, Soutetsu——" ngắt thành xưng hô.

**Key 1802 (稀咲)**
- JP: "「こんな正直な双鉄を見て。ペニスのたてる水音を聞いて。\\n雄の匂いを胸いっぱいに吸い込んで―ポーレットは」"
- TW: "「看看這麼誠實的雙鐵。聽聽陰莖發出的水聲。把雄性的氣味滿滿地吸進胸腔吧——波萊特」"
- VN cũ: "「Nhìn dáng vẻ thành thật này của anh Soutetsu đi. Nghe tiếng nước nhóp nhép từ dương vật đi.\\nHít đầy lồng ngực mùi hương của giống đực đi——Paulette, cô」"
- Sửa: "「Nhìn dáng vẻ thành thật này của anh Soutetsu đi. Nghe tiếng nước nhóp nhép từ dương vật đi. Hít đầy lồng ngực mùi hương của giống đực đi——Paulette」"
- Lý do: VN cũ thêm đuôi ", cô" không có trong JP/TW (JP/TW kết bằng tên Paulette) — bỏ đuôi thừa.

**Key 1712 (ポーレット)**
- JP: "「わらひっ！　わたしも、双鉄くん―んあっ！！\\nあっ！　だから―きて、きて、きてっ！　きてっ！！」"
- TW: "「我！　我也、雙鐵君——嗯啊！！啊！　所以——來吧、來吧、來吧！　來吧！」"
- VN cũ: "「E! Em cũng vậy, anh Soutetsu——ưm a!!\\nA! Nên là——vào đi, vào đi, vào đi! Vào đi!!」"
- Sửa: "「Ehm! Em cũng vậy, anh Soutetsu——ưm a!! A! Nên là——vào đi, vào đi, vào đi! Vào đi!!」"
- Lý do: JP わらひっ (cười ngọng) — theo tiền lệ h6 784 phải là "Ehm!"; VN cũ "E!" mất tiếng cười ngọng.

**Key 1580 (ポーレット)**
- JP: "「え！？　どうしたの？　稀咲、平気っ！？」"
- TW: "「啊！？怎麼了？　稀咲、你沒事吧！？」"
- VN cũ: "「Ế!? Sao thế? Kisaki, cậu không sao chứ!?」"
- Sửa: "「Ế!? Sao thế? Kisaki, em không sao chứ!?」"
- Lý do: Paulette gọi Kisaki "cậu" — sai quy ước file (Paulette gọi Kisaki "em", vd 1006; đây là lần "cậu" duy nhất trong file).

### Hơi thở và SFX — âm và độ dài (13 dòng)

**Key 1586 (稀咲)**
- JP: "「ぬちゅっ―れるっ―\\nぺちゃあああぁあぁぁああ―れるっっ！」"
- TW: "「啾啾——舔舔——吸吮————————舔舔！」"
- VN cũ: "「Nu chu——rê ru——\\npê cha aa aa aa aa——rê ru!」"
- Sửa: "「Nu chụt——rê ru—— pê cha aa aa aa aa——rê ru!」"
- Lý do: JP ぬちゅっ — VN cũ "Nu chu" dùng "chu" trần cho ちゅっ; theo đề xuất họ ちゅ (chỉ "chụt" cho ちゅっ) phải là "Nu chụt". Các れるっ trong dòng giữ nguyên dạng âm tiết "rê ru" (chưa có quyết "rộp" của Hieu).

**Key 1442 (稀咲)**
- JP: "「きゃふっ！！！？　あ―やだっ―双鉄っ―んっ。\\nそんな―急に―急に―こんなのっ―」"
- TW: "「呀嗚！！！？啊——不要——雙鐵——嗯。不要——太突然——突然——這樣」"
- VN cũ: "「Kya fu!!!? A——đừng——anh Soutetsu——ưm.\\nThế này——đột nhiên——đột nhiên——thế này——」"
- Sửa: "「Kyaphù!!!? A——đừng——anh Soutetsu——ưm. Thế này——đột nhiên——đột nhiên——thế này——」"
- Lý do: JP きゃふっ — theo tiền lệ h6 769 phải viết liền "Kyaphù"; VN cũ "Kya fu" tách từ + mất ふ.

**Key 1642 (ポーレット)**
- JP: "「すごい……おっきい―それに―（くんくん）―\\n匂い、濃くて―とっても―えっちで―はふぅ」"
- TW: "「好厲害……好大——而且——（聞聞）——味道，好濃烈——非常——色情——哈呼」"
- VN cũ: "「Tuyệt quá……to thật——hơn nữa——（khịt khịt）——\\nmùi, nồng quá——rất là——dâm đãng——ha phu.」"
- Sửa: "「Tuyệt quá……to thật——hơn nữa——（khịt khịt）—— mùi, nồng quá——rất là——dâm đãng——ha phù.」"
- Lý do: JP はふぅ — VN cũ "ha phu" (phiên âm không dấu); sửa thành "ha phù" (âm thở có dấu, theo quy tắc thở).

**Key 1619 (ポーレット)**
- JP: "「んきゅうううううううううっ！！！！！？」"
- TW: "「嗯嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚嗚！！！！？」"
- VN cũ: "「Ưm kyuu uu uu uu uu uu uu uu!!!!!?」"
- Sửa: "「Ưm kíuuuuuuuuuu!!!!!?」"
- Lý do: JP んきゅうううううううううっ (10 âm u) — VN cũ 16 âm u ("Ưm kyuu uu…"); thu về đúng 10 âm u: "Ưm kíuuuuuuuuuu" (quy tắc độ dài SFX).

**Key 1440 (ポーレット)**
- JP: "「きゅぁぁぁっぁぁぁぁあああああああああああんっ！」"
- TW: "「呀啊啊啊啊啊啊啊！」"
- VN cũ: "「Kyua a a a a a a a a a a a a a a a a a a n!」"
- Sửa: "「Kíua a a a a a a a a a a a a a a a a a n!」"
- Lý do: JP きゅぁぁぁっぁぁぁぁああああああああああああんっ (18 âm a) — VN cũ 19 âm a; bớt một âm a, sửa "Kyua"→"Kíua" (quy tắc độ dài SFX).

**Key 1441 (稀咲)**
- JP: "「ひゅぁぁぁぁぁぁぁあああぁぁぁぁぁんっ！！！！」"
- TW: "「呀啊啊啊啊啊啊啊！！！！」"
- VN cũ: "「Hyua a a a a a a a a a a a a a a a a n!!!!」"
- Sửa: "「Híua a a a a a a a a a a a a a a n!!!!」"
- Lý do: JP ひゅぁぁぁぁぁぁぁあああぁぁぁぁぁんっ (15 âm a) — VN cũ 17 âm a; bớt hai âm a, sửa "Hyua"→"Híua" (quy tắc độ dài SFX).

**Key 1488 (稀咲)**
- JP: "「ひゃううううぅぅぅぅぅうんっ！！！！！！」"
- TW: "「咿呀嗚嗚嗚嗚嗚嗚！！！！！！！！」"
- VN cũ: "「Hyau uu uu u u u u u u un!!!!!!」"
- Sửa: "「Hyau uu uu u u u u un!!!!!!」"
- Lý do: JP ひゃううううぅぅぅぅぅうんっ (10 âm u) — VN cũ 12 âm u; bớt hai âm u (quy tắc độ dài SFX).

**Key 2599 (monologue)**
- JP: "（ずぶううううううううっっっっっっっっっ！！！！）"
- TW: "（滋噗————————！！！！）"
- VN cũ: "（Zu buu uu uu uu uu uu uu uu uu uu uu uu uu uu!!!!）"
- Sửa: "（Zu buuuuuuuuu!!!!）"
- Lý do: JP ずぶううううううううっ (8 âm u) — VN cũ 28 âm u (gấp 3,5 lần); thu về đúng 8 âm u (quy tắc độ dài SFX).

**Key 2503 (monologue)**
- JP: "（ずりゅううううううううううううううううっ！！！）"
- TW: "（呲溜——————————！！！）"
- VN cũ: "（Zu ryuu uu uu uu uu uu uu uu uu uu uu uu uu uu uu uu!!!）"
- Sửa: "（Zu ryuuuuuuuuuuuuuuuu!!!）"
- Lý do: JP ずりゅううううううううううううううううっ (16 âm u) — VN cũ 32 âm u (gấp đôi); thu về đúng 16 âm u (quy tắc độ dài SFX).

**Key 2608 (monologue)**
- JP: "（ずぶうううううううううううううっ！　ごちゅんっ！）"
- TW: "（用力插入！　抽插！）"
- VN cũ: "（Zu buu uu uu uu uu uu uu uu uu uu uu uu uu! Go chun!）"
- Sửa: "（Zu buuuuuuuuuuuuuu! Go chun!）"
- Lý do: JP ずぶうううううううううううううっ (13 âm u) — VN cũ 26 âm u (gấp đôi); thu về đúng 13 âm u (quy tắc độ dài SFX).

**Key 2540 (monologue)**
- JP: "（ずぶううううううううううううううっ！　ごちゅっ！）"
- TW: "（啾噗！！！　咕啾！）"
- VN cũ: "（Zu buu uu uu uu uu uu uu uu uu uu uu uu uu uu! Go chu!）"
- Sửa: "（Zu buuuuuuuuuuuuuuu! Go chu!）"
- Lý do: JP ずぶううううううううううううううっ (14 âm u) — VN cũ 28 âm u (gấp đôi); thu về đúng 14 âm u (quy tắc độ dài SFX).

**Key 2500 (monologue)**
- JP: "（きゅうううううううううううううっっっ！）"
- TW: "（劇烈收縮！！！！）"
- VN cũ: "（Kyuu uu uu uu uu uu uu uu uu uu uu uu uu!）"
- Sửa: "（Kíuuuuuuuuuuuuu!）"
- Lý do: JP きゅうううううううううううううっっっ (13 âm u) — VN cũ 27 âm u (gấp đôi); thu về đúng 13 âm u: "Kíuuuuuuuuuuuuu" (quy tắc độ dài SFX).

**Key 2536 (monologue)**
- JP: "（じゅぶううううううううううっ！　ごちゅうううっ！）"
- TW: "（啾噗————！　咕啾————！）"
- VN cũ: "（Ju buu uu uu uu uu uu uu uu uu uu! Go chuu uu u!）"
- Sửa: "（Ju buuuuuuuuuuu! Go chuuuu!）"
- Lý do: JP じゅぶううううううううううっ (10 âm u) + ごちゅうううっ (3 âm u) — VN cũ 20 + 5 âm u (gấp đôi); thu về đúng 10 + 3 âm u (quy tắc độ dài SFX).

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng ngoài các dòng đã quyết)

- Soutetsu gọi Paulette "em" 1 lần (1700 — "em hãy giơ tay phải lên nhé", lúc sắp vào trong Paulette) vs "cô" 0 lần — cộng dồn toàn dự án (theo cơ sở của parent: "em" 96 vs "cô" 48): **"em" 97 vs "cô" 48**. Lưu ý: các lần "em" khác của Soutetsu trong file đều gọi KISAKI, không phải Paulette (1786, 1689 ×2, 1724) — KHÔNG tính vào đếm Paulette. (Ghi chú: ROUTE-AUDIT mục h8 ghi cộng dồn "em" 97 vs "cô" 48 — chênh 1 so với cơ sở 96 của parent, do mục h8 chưa trừ lần "em" ở sleeper 1627 đã quyết là hỏi Hikari (B1); cộng dồn ở đây dùng cơ sở 96 của parent.)
- Kisaki xưng hô theo đối tượng (quan sát, KHÔNG phải lỗi): Kisaki dùng "em" với Soutetsu (1860, 1718, 1879, 1800, 1792, 1788) và "tôi" với Paulette (1831, 1830, 1772, 1389, 1701, 1392; "chúng tôi" ở 1370/1882) — JP đều là ボク; đây là phân biệt ngôi rõ ràng theo người nghe, giữ nguyên. Kisaki gọi Paulette "cô" 10 lần (1769, 1882, 1802, 1830, 1716, 1734, 1785, 1392, 1632, 1371) — nhất quán (Paulette lớn tuổi hơn, cựu thị trưởng), không sửa. Paulette gọi Kisaki "em" 8 lần (1668, 1865, 1426, 1584, 1740, 1006, 1837, 1635) — chỉ 1580 dùng "cậu" (đã sửa).
- ふふっ → "Fufu" GIỮ NGUYÊN (không sửa thành "Ư hự"): 6 dòng trong file (1457, 1461, 1533, 1604, 1463, 1456) đều là cười khúc khích/chuckles trong ngữ cảnh trò chuyện, không phải thở gấp trong cảnh H. Ghi nhận mâu thuẫn với tiền lệ h8 2360 (ふふっ → "Ư hự" cho 4 dòng 2360/2356/2370/2402 trong cảnh H) — tiền lệ h8 có thể không đúng cho ngữ cảnh cười nói; quy tắc fa/fu đã quyết chỉ bao ふぁ/ふあ/ふぇ/ふやぁ, KHÔNG bao ふふっ. Cần Hieu chốt: ふふっ trong cảnh H là "Ư hự" hay "Fufu" — và các dòng h8 có nên sửa lại không.
- Tên trần "Soutetsu" trong câu nói: 0 lần (Paulette và Kisaki đều gọi "anh Soutetsu" đúng quy tắc). Tên rên/moaned đứng riêng: 0 lần trong file — không có gì để gắn cờ theo B4.
- Họ ちゅ: file diễn ちゅっ/ちゅう/ちゅむっ/ちゅるっ/ちゅろっ bằng âm tiết La-tinh xuyên suốt (`chuu u`, `chu mu`, `chu pa`, `chu bu`, `chu ru`…) — GIỮ NGUYÊN toàn bộ dạng âm tiết (chưa có quyết "chụt" của Hieu); chỉ sửa đúng 1 trường hợp "chu" trần (1586 ぬちゅっ → "Nu chu" → "Nu chụt"). Nếu Hieu chốt "chụt", file này cần một lượt rà soát hệ thống họ ちゅ.
- Quy ước "rộp" cho れる/るっ/れろ: file diễn れるっ bằng âm tiết "rê ru" xuyên suốt — GIỮ NGUYÊN (chưa có quyết của Hieu); chỉ ぺろ → "liếm" là quy tắc đã rõ (không có ぺろ trong file này ngoài ぺろっっ → "pê ro", dạng âm tiết, giữ nguyên).
- Hướng SFX: ずっ → "Rút" ở 2558 là ĐÚNG (rút ra trước khi dừng — khác ngữ cảnh thrust-in của h6 1586); ずりゅっ → "Trượt" ở 2505 là ĐÚNG (tiếng trượt); ぐっ → "lún" trong các khối thrust (2512, 2544, 2597) là cách diễn chuyển động nhất quán của file — giữ nguyên.

## Đề xuất cập nhật context (chưa chốt)

- Không có đề xuất mới từ file này. Các đề xuất đang chờ Hieu vẫn giữ nguyên: họ ちゅ → "chụt"; quy ước "rộp" cho れる/るっ/れろ; ふふっ trong cảnh H là "Ư hự" hay "Fufu" (mâu thuẫn h8 2360 vs file này).

## Đã kiểm tra và KHÔNG tính là sai

- 956 (tiêu đề route "——Kisaki Route Another——") — chưa có quy tắc quyết cho tiêu đề route; ghi nhận là quan sát mỹ thuật, không sửa.
- 1484 くうっ → "Kuu u!!!" — đây là ÂM THANH (tiếng kêu), KHÔNG phải tên コン — không sửa thành "Kon" (quyết định B8: chỉ コン mới là tên).
- 1675 (Paulette lắp bắp lặp lại "Anh Soutetsu——muốn làm tình! Với anh Soutetsu.") — cách diễn lắp bắp, nghĩa vẫn rõ (Paulette là người muốn), giữ nguyên.
- 1808 稀咲っ → "Kisaki." — tiếng gọi bị ngắt, dấu chấm diễn đúng sự ngắt quãng; giữ nguyên.
- 2586 しゅっ → "Shu" (khác 2585 "Sục" cho しゅっ) — cách diễn phiên âm, không nhất quán nhưng không sai nghĩa; giữ nguyên (quan sát mỹ thuật).
- 1558 (dấu phẩy sau "dương vật, của anh Soutetsu") — dấu phẩy ngắt nhịp, KHÔNG phải lỗi sở hữu/xưng hô (cụm "của anh Soutetsu" còn nguyên, không bị ngắt); khác với 1644/1467/997.
- 1582/1855 (Paulette gọi "anh Soutetsu" cuối câu) — xưng hô đúng, không phải lỗi sở hữu.
- 1822/1820 (nhóm "uu" trong các tiếng ré dài) — nằm trong quy ước nhóm âm của file, không tính là đếm sai (chỉ 6 dòng đếm gấp đôi mới sửa).
- 2558 (đếm âm u: JP 3, VN 4 sau "bu") — lệch ±1, coi là nhiễu, không sửa.
- 2508/2534 (đếm âm đã kiểm tra đúng).
- ふふっ 6 dòng (1457, 1461, 1533, 1604, 1463, 1456) — cười khúc khích, giữ "Fufu" (xem § bằng chứng).
- Các tiếng thở La-tinh còn lại (screams "Kya"/"Hya", "Ưm ku", "Ư ku", các khối SFX `(…)` phiên âm đủ âm tiết) — diễn đúng âm, không mất mát, giữ nguyên theo tiền lệ h7.
- 1599/1892/1893 (sweep "already-rendered") — audit đồng ý, không đưa vào danh sách sửa.

## Kết bài

- lr_稀咲h1 sai 85/488 (17,4%) — 0 lệch vị trí ngoài 1 dòng đơn (1509), 0 chuỗi xoay vòng, 0 tràn chương; lỗi tập trung ở xưng hô hệ thống (21) + hơi thở fa/fu (19) + thở gấp っ (19, trong đó sweep bỏ sót 6) + độ dài SFX (11) + sai nghĩa/lỗi đánh máy (8).
- Khối TOML 85 key đã parse đúng bằng tomllib; số key khớp đúng với JSON (85); giá trị JSON khớp 0 sai lệch với khối TOML; giá trị VN cũ trong JSON khớp 0 sai lệch với file TOML gốc (sau khi chuẩn hoá `\n` → khoảng trắng).
- Kiểm tra lần hai: 85/85 bản sửa đọc lại đối chiếu JP, 0 bị loại.
- Rà soát chéo sweep: 13 bản sửa sweep trong file đều được audit xác nhận cùng giá trị (không xung đột); 3 mục "already-rendered" được đồng ý; audit bắt thêm 6 dòng gasp sweep bỏ sót (1596, 1598, 1902, 2236, 1567, 1590).
- Bằng chứng mới: Soutetsu gọi Paulette "em" 1 lần (1700) vs "cô" 0 — cộng dồn "em" 97 vs "cô" 48. Ghi nhận mâu thuẫn ふふっ (file này giữ "Fufu" vs h8 2360 "Ư hự") — cần Hieu chốt.

```toml
[script]
970 = "「——Tôi sẽ lần lượt ôm hai người. Về mặt cảm xúc, tôi sẽ làm với cả hai cùng lúc——ba chúng ta cùng nhau.」"
997 = "「……Nếu, không sao——nếu anh Soutetsu, OK, thì em rất muốn, làm tình. Của anh Soutetsu——」"
999 = "「……Nghĩa là chỉ cần một người không muốn nữa, mối quan hệ sẽ kết thúc sao. Tôi hiểu rồi, tất nhiên tôi không có ý kiến gì.」"
1379 = "「Nhưng, tôi không muốn đổ trách nhiệm cho Kisaki vì tôi đã thuận theo. Vậy nên, bằng chính ý chí của mình, tôi mong muốn điều này.」"
1386 = "「Anh không ghét sao?」"
1396 = "「Nhìn đi. Đây là dương vật đang cương cứng của tôi. Từ giờ trở đi——tôi sẽ dùng nó, để xuyên thấu Paulette.」"
1397 = "「Làm tình——làm tình. Làm tình với anh Soutetsu và Kisaki. Ba người cùng nhau……phà——chu mu——chuu u——」"
1415 = "「Việc Kisaki sắp đặt tình huống này cũng là một cái cớ cho dục vọng của tôi. Rằng tôi cứ thuận theo cũng được.」"
1434 = "「Tôi đồng ý. Không có ý kiến gì.」"
1440 = "「Kíua a a a a a a a a a a a a a a a a a n!」"
1441 = "「Híua a a a a a a a a a a a a a a n!!!!」"
1442 = "「Kyaphù!!!? A——đừng——anh Soutetsu——ưm. Thế này——đột nhiên——đột nhiên——thế này——」"
1464 = "「Phà——a……Làm tình—— Làm tình——em……muốn làm…………ưm.」"
1467 = "「Phà……a——a……ưm——（Ực）——đầy ắp, tinh, dịch——của anh Soutetsu……sắp tràn, ra rồi……」"
1468 = "「Phàaaaaa」"
1470 = "「Phà a a a a a n! Anh Soutetsu, nè? Anh Soutetsu——a, em, nè? Em——em, sắp, sắp, sắp rồi!」"
1472 = "「Phà! A! A! A! Lại nữa—— Nhá! Xin anh, xin anh đấy——anh Soutetsu!」"
1475 = "「Phà! A! A! A! A! A! A! A! Anh, Soutetsu——anh Soutetsu——ưm!」"
1477 = "「Phà! Ưm! Âm đạo, âm đạo! Của em, gì thế, này——đang siết chặt, lấy, phà」"
1478 = "「Phà! Anh Soutetsu! Anh Soutetsu, anh Soutetsu——」"
1480 = "「Phà!! Thích, thích lắm! Hợp nhau, lắm—— Phà! Vui——vui quá——vui quá, vui quá đi!」"
1481 = "「Phà!!!!!」"
1488 = "「Hyau uu uu u u u u un!!!!!!」"
1495 = "「Hya!? A, phần bụng, ngón tay, của anh Soutetsu——phà, đang ở, cửa mình——âm đạo, của em——au——」"
1497 = "「Oa——oa——dịu dàng quá……như thể đang dùng tay vuốt ve khen ngợi dương vật là bé ngoan vậy……phà.」"
1502 = "「Oa!? Ế!!? Của dương, vật——cái đó, bi ——ưm……túm chặt, như thế——……」"
1509 = "「Ha——a! A! A!! Đang vào, rồi——em——vào âm đạo, của em——anh Soutetsu——」"
1513 = "「Ha——ưm——phà——a——. Anh, Soutetsu—— Anh Soutetsu——fufu——anh đã cố gắng lắm rồi. Lại đây nào, anh Soutetsu?」"
1523 = "「Ha! A!? A——không thể nào——phà—— Đầy ắp, rồi mà——căng cứng, chật chội, thế mà.」"
1536 = "「A——phà——a」"
1567 = "「Ư! ——Xuất tinh!? Xuất tinh——xuất tinh là……hau」"
1569 = "「A! Hà——a——a!!!!」"
1580 = "「Ế!? Sao thế? Kisaki, em không sao chứ!?」"
1584 = "「Chuu u——ưm……chu pa. Phà……Ưm, Kisaki………… Nè? ——Cảm ơn em.」"
1586 = "「Nu chụt——rê ru—— pê cha aa aa aa aa——rê ru!」"
1590 = "「Ư——Kisa, ki——～～～Ư! Sướng……quá」"
1596 = "「Ư!! ——（Ực）」"
1597 = "「Ư!!!」"
1598 = "「ƯƯ!!!!!」"
1619 = "「Ưm kíuuuuuuuuuu!!!!!?」"
1624 = "「Ưm! Ưm! Em sẽ——nhịn——nhưng mà nhưng mà——phà! A——em——em! Sắp」"
1641 = "「Tuyệt, quá——a——xấu hổ quá——em, rõ ràng, ——vẫn còn trinh——là lần đầu tiên——vậy mà, phà.」"
1642 = "「Tuyệt quá……to thật——hơn nữa——（khịt khịt）—— mùi, nồng quá——rất là——dâm đãng——ha phù.」"
1644 = "「Muốn, quá——ya, a——của anh Soutetsu—— tinh dịch, tinh dịch——vào sâu, bên trong, em!!」"
1666 = "「Tôi——thì, tôi, thì.」"
1677 = "「Tôi cũng——a——ku——ưm fu——hiểu rồi.」"
1681 = "「Tôi cũng muốn làm tình với Paulette. Và hơn thế nữa, tôi muốn xây dựng một mối quan hệ sâu sắc, thân mật và bền chặt hơn với Kisaki.」"
1689 = "「Tôi đang nhịn——đến mức không thể nhịn được nữa rồi. Vì thế……vì thế, xin em——tôi xin em đấy, Kisaki.」"
1694 = "「Tôi yêu Kisaki, và muốn ở bên Kisaki mãi mãi. Nhưng hiện tại, tôi cũng không thể kìm nén được dục vọng với Paulette.」"
1700 = "「Tôi sẽ vào từ từ. Nếu thấy đau hay khó chịu thì tôi sẽ dừng lại ngay. Lúc đó——xem nào, em hãy giơ tay phải lên nhé.」"
1708 = "「Mong muốn của tôi, lúc nào cũng vậy, không hề thay đổi. Đó là không bao giờ làm tổn thương Kisaki.」"
1712 = "「Ehm! Em cũng vậy, anh Soutetsu——ưm a!! A! Nên là——vào đi, vào đi, vào đi! Vào đi!!」"
1724 = "「Xin em đấy, Kisaki——điều khoản cuối cùng——hãy cho tôi biết điều khoản cuối cùng cần thiết cho hợp đồng của chúng ta đi.」"
1725 = "「Tôi hiểu rồi.」"
1731 = "「Chắc vậy rồi……Tôi cũng——không còn, dư dả gì.」"
1737 = "「Vậy sao. Tôi hiểu rồi.」"
1761 = "「Tôi đâu làm gì đáng để được cảm ơn……」"
1773 = "「Paulette——Paulette……Tôi, sắp」"
1781 = "「Cứ thế này——thì——tôi sẽ……xuất tinh mất——a」"
1786 = "「Xét theo tình hình thì tôi không thấy có gì đáng ghét cả. Tôi chỉ bận tâm đến cảm nhận của em thôi, Kisaki.」"
1802 = "「Nhìn dáng vẻ thành thật này của anh Soutetsu đi. Nghe tiếng nước nhóp nhép từ dương vật đi. Hít đầy lồng ngực mùi hương của giống đực đi——Paulette」"
1816 = "「Bụ, ng——bụng, dưới——âm, đạo——chật, quá ——chật ních——em, bị nhét đầy, mất——Ư!」"
1824 = "「Hà——a——không sao——ưm——em—— âm đạo, không sao——đâu——nên là——anh Soutetsu.」"
1825 = "「Hà——Hà——Hà——Ha——（Ực） ——Anh Soutetsu?」"
1826 = "「Hà! Ha! Ha! Ha!」"
1894 = "「Ư!!!!」"
1895 = "「Ư!!!!!!!」"
1896 = "「Ư!!!!!!!!!!!」"
1897 = "「Ư!!!?」"
1902 = "「～～～Ư///」"
1906 = "「～～～～Ư!!!」"
1908 = "「～～～～～Ư!!」"
2135 = "Cảm giác ngực vừa bị ấn nhẹ——Ư!?"
2178 = "Tôi biết. Tôi cảm nhận được. Cửa tử cung của Paulette cũng đang khao khát tinh dịch của tôi. Mỗi lần đâm vào nơi sâu nhất, nó lại khẽ khàng mút lấy một cách ngọt ngào——Ư!"
2232 = "Đỏ bừng mặt, nghiến chặt răng, khóe mắt đẫm lệ, nhưng Paulette vẫn nhìn thẳng vào mắt tôi và gật đầu dứt khoát nhiều lần."
2236 = "Tay Paulette rời khỏi người tôi. Rời khỏi——Ư! Cô ấy thè chiếc lưỡi đỏ chót nhỏ xíu ra nếm thử mùi vị của nước nhờn."
2309 = "Cửa tử cung của Kisaki hút lấy quy đầu một cách mãnh liệt. Như muốn nuốt trọn toàn bộ tinh dịch của tôi——Ư!!"
2349 = "Siết chặt. Bàn tay phải của Paulette túm chặt lấy ga giường——Ư!"
2500 = "（Kíuuuuuuuuuuuuu!）"
2501 = "（Ra là vậy, đây chính là—— làm tình ba người sao——Ư!!?）"
2503 = "（Zu ryuuuuuuuuuuuuuuuu!!!）"
2536 = "（Ju buuuuuuuuuuu! Go chuuuu!）"
2540 = "（Zu buuuuuuuuuuuuuuu! Go chu!）"
2599 = "（Zu buuuuuuuuu!!!!）"
2608 = "（Zu buuuuuuuuuuuuuu! Go chun!）"
```

---
## Đính chính 19/11 22:05 — ふふっ đã có quyết định (Hieu)

Hieu quyết: tiếng cười dịch ngẫu hứng theo tính cách nhân vật, không dập khuôn — không còn "mâu thuẫn" cần chốt. 6 dòng ふふっ trong file này giữ "Fufu" (cười khúc khích trong hội thoại) là đúng. 4 dòng h8 dịch cười thành "Ư hự" (2356/2360/2370/2402) đã được sửa lại thành tiếng cười theo quyết định này. Xem sfx_and_emoticons.md §0.
