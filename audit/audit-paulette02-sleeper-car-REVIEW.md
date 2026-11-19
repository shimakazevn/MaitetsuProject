# Audit: Paulette 02_解放b寝台 — 48 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/ポーレット02_解放b寝台.txt.toml` — Đêm đầu tiên trên tàu giường nằm: Paulette, Soutetsu, Hikari và Reina lên tàu C56 "Pony", trưởng tàu kiểm vé bằng kìm soát vé, Hikari leo lên giường trên, cảnh hôn chúc ngủ ngon giữa Soutetsu và Paulette. 421 dòng script đã đọc hết, đối chiếu từng dòng với JP gốc và TW (nhân chứng thứ hai).

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa toàn bộ 421 dòng (thoại 273: Soutetsu 105, Paulette 76, Hikari 70, Reina 19, trưởng tàu 3; lời dẫn 148) đối chiếu JP + TW từ CSV "Trang tính 3" và TOML-2.
- **48 dòng sai (11,4%), 0 dòng chưa chắc chắn.** Thoại sai 29/273 (10.6%), lời dẫn sai 19/148 (12.8%). Theo người nói: 双鉄 19/105, monologue 19/148, ポーレット 7/76, ひかり 3/70.
- Phân loại: lệch vị trí 19, xưng hô 16, thuật ngữ 5, sai nghĩa 3, lỗi nhỏ 5; chưa dịch 0, cắt cụt 0, chưa chắc chắn 0.
- Heuristic (dấu thoại ↔ lời dẫn) báo 10 dòng — bắt được 10/19 dòng lệch vị trí (1624, 1797, 2432, 2450, 2459, 2519, 2531, 2646, 2662, 2681); 9 dòng lệch còn lại có dấu thoại/lời dẫn trùng với JP nên heuristic không thấy. Heuristic dấu phẩy kiểu MT báo 9 dòng — kiểm tra tay: 0 dòng trong số đó sai vì dấu phẩy.
- Không key-shift sạch (shift 0: 411/421 = 0,976; các shift khác 0,968–0,988 — không có shift nào vượt trội). TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất; 166 khác biệt thô chỉ ở `\n`/khoảng trắng).
- 0 dòng CSV trống; VN==TW 0. `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 14 thẻ (7 dòng thêm gloss mà JP không có — cùng quy ước với file stove: 1174, 1925, 2007, 2107, 2301, 2321, 2630; cả 7 gloss đều dịch đúng: 検札鋏 → "kìm soát vé", 蒸気機関車 → "đầu máy hơi nước", 喚呼 → "hô xác nhận", C56 → "C56") — **0 thẻ thiếu dấu `;` đóng** (khác Paulette 13: 5 thẻ thiếu `;`).
- **Tràn chương hai chiều với obasan (xem chi tiết dưới đây), 0 chuỗi xoay vòng trong file, 0 dòng mồ côi.** Đã kiểm tra bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục). Các bản Việt trùng lặp trong file: "「Kyaa!」" 1704/1734 (JP đều 「きゃあ！」, đều đúng), "「Ồ.」" 1817/1744/1941 (JP 「おおお」/「ああ」/「ほう」, đều đúng), "「Hửm?」" 1755 đúng (JP 「む？」) — bản sao 2646 là dòng lệch vị trí.
- Không có file trùng lặp ở thư mục khác (đã kiểm tra md5 toàn bộ 227 file TOML-2; Grand 04 vẫn là file trùng duy nhất trong dự án).
- Quét xưng hô bằng máy (đã chuẩn hoá `\n` thành khoảng trắng trước khi chạy regex `\b`, không phân biệt hoa/thường — quét lần đầu bỏ sót "Anh"/"Em" viết hoa đầu câu): Soutetsu trong thoại tự xưng "anh" 13 lần (tất cả sai), "tôi" 0 lần; "em" 15 lần (13 lần gọi Paulette, 1 lần gọi Hikari tại 1614 — sai, phải là "con", 1 lần gọi Reina tại 2002 — đúng). "mình" trong độc thoại 6 dòng — 4 dòng đúng (sở hữu/phản thân/thành ngữ "một mình"/"tự mình"), 2 dòng sai là chủ ngữ độc lập (2339, 2590).
- **Viết bản sửa bằng tay, không sửa hàng loạt bằng script (quy tắc 19/11 của Hieu):** mọi bản sửa trong file này đều được viết tay từng dòng từ JP (+TW) của chính dòng đó — kể cả 17 bản sửa khôi phục từ file obasan (đã đọc và đối chiếu JP/TW tại key obasan trước khi viết lại bằng tay); script chỉ dùng để lắp ráp khối TOML từ các bản sửa đã viết, kiểm tra parse TOML và đối chiếu số key. Không có bản sửa nào do script sinh ra hay sửa đổi.
- **Kiểm tra lần hai (đọc lại toàn bộ bản sửa đối chiếu JP):** sau khi lắp khối TOML, đã đọc lại cả 48 bản sửa, từng dòng đối chiếu với JP gốc để xác nhận nghĩa, người nói và dấu câu — **tổng số bản sửa: 48; đã kiểm tra lại: 48; bị loại ở vòng hai: 0.** Chỉ kiểm tra parse + khớp số key là chưa đủ; vòng đọc lại này là bắt buộc theo quy tắc của Hieu.

## Kết luận về cơ chế lỗi

Đây là **trường hợp tràn chương thứ ba của dự án, và là trường hợp đầu tiên tràn HAI CHIỀU**: obasan ↔ sleeper. 19 dòng trong file này mang bản Việt của obasan (đều là bản dịch đúng tại key obasan của chúng), và ngược lại 17 dòng trong obasan mang bản dịch đúng của các dòng sleeper này — hai file đã hoán đổi bản Việt cho nhau tại 17 cặp key, cộng thêm 2 dòng sleeper bị ghi đè một chiều (bản dịch đúng không còn ở đâu trong dự án). Khác hai trường hợp trước (Hachiroku 12 → 夜の嵐 một chiều 32 dòng; hearing → stove một chiều 90 dòng), ở đây **17/19 bản sửa khôi phục được từ chính file obasan** (bản dịch đúng đang nằm sai vị trí tại đó — và audit obasan đã liệt kê cả 17 key nguồn đó vào danh sách sai của nó, nên sửa hai file sẽ khớp nhau); chỉ 1892 và 2684 phải dịch mới hoàn toàn. Ngoài tràn chương, file này còn hai lựa chọn hệ thống của người dịch: Soutetsu tự xưng "anh" (13/13 lần tự xưng trong thoại, 0 lần "tôi") và 回数券 dịch thành "vé tháng" (3 lần). Không có chuỗi xoay vòng trong file, không có dòng mồ côi.

### Bảng tràn chương obasan ↔ sleeper (19 dòng)

| Key sleeper | Bản Việt hiện tại đúng tại obasan key | Bản dịch đúng của sleeper nằm tại obasan key | Trạng thái sửa |
|---|---|---|---|
| 1624 | 2676 | 1680 | Khôi phục từ obasan 1680 |
| 1712 | 2012 | 2637 (sửa 1 từ: "phần thưởng" → "bữa ăn") | Khôi phục từ obasan 2637, sửa 1 từ |
| 1760 | 1575 | 2017 | Khôi phục từ obasan 2017 |
| 1797 | 2549 | 2277 | Khôi phục từ obasan 2277 |
| 1807 | 1761 | 1704 | Khôi phục từ obasan 1704 |
| 1892 | 1978 | — (không tồn tại) | Dịch mới |
| 2053 | 1977 | 2265 | Khôi phục từ obasan 2265 |
| 2432 | 1874 | 1583 | Khôi phục từ obasan 1583 |
| 2450 | 1632 | 1628 | Khôi phục từ obasan 1628 |
| 2459 | 1570 | 1961 | Khôi phục từ obasan 1961 |
| 2519 | 1976 | 1682 | Khôi phục từ obasan 1682 |
| 2531 | 1598 | 1830 | Khôi phục từ obasan 1830 |
| 2570 | 2420 | 2517 | Khôi phục từ obasan 2517 |
| 2584 | 2664 | 2478 | Khôi phục từ obasan 2478 |
| 2646 | 1655 | 2503 | Khôi phục từ obasan 2503 |
| 2662 | 1560 | 2563 | Khôi phục từ obasan 2563 |
| 2681 | 1923 | 1809 | Khôi phục từ obasan 1809 |
| 2684 | 1135 | — (không tồn tại) | Dịch mới |
| 2688 | 2579 | 2466 | Khôi phục từ obasan 2466 |

Cả 19 bản Việt hiện tại đều đã xác minh là bản dịch đúng tại key obasan ghi trong cột 2 (đọc JP/TW tại obasan, không chỉ tra chỉ mục). Cả 17 key nguồn obasan (cột 3) đều đã nằm trong danh sách 255 dòng sai của audit obasan — tức audit obasan đã sửa chúng bằng bản dịch đúng của JP obasan, và audit này dùng chính bản Việt hiện tại (sai vị trí) tại đó làm bản sửa cho sleeper. Hai file sửa xong sẽ khớp nhau, không xung đột. Riêng 1712: bản tại obasan 2637 dịch sai 1 từ ("phần thưởng" cho ごちそうさまでした) — người dịch lẫn với dòng ご褒美 1624 ngay cạnh trong cùng cảnh — đã sửa thành "bữa ăn" theo JP/TW. Lưu ý: 10 trong 17 bản khôi phục giữ lại dấu xuống dòng `\n` theo JP/CSV gốc, trong khi bản Việt tại obasan trong TOML-2 đã mất `\n` thành khoảng trắng (hiện tượng mất `\n` đã biết của TOML, 59% toàn dự án) — khác biệt duy nhất là `\n` vs khoảng trắng, nghĩa không đổi.

## Chi tiết dòng sai

### Lệch vị trí — tràn chương từ obasan (19 dòng)

**1624 [Paulette]** — Bản Việt hiện tại là bản dịch đúng của obasan key 2676 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 1680 (obasan 1680 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: 「双鉄くんにも、頑張ってくれてるご褒美です！
（ちゅっ！）」
- TW: 「你也很努力，我也給你獎勵！（啾！）」
- Cũ: （♪~）
- Sửa: 「Cũng là phần thưởng cho anh Soutetsu vì đã vất vả nhé!
(Chụt!)」

**1712 [Paulette]** — Bản Việt hiện tại là bản dịch đúng của obasan key 2012 — tràn chương obasan → sleeper. Bản dịch đúng của dòng này nằm tại obasan 2637, nhưng có 1 từ dịch sai: "phần thưởng" cho JP ごちそうさまでした (cảm ơn vì bữa ăn; TW 多謝) — người dịch đã lẫn với dòng ご褒美 (1624) ngay cạnh trong cùng cảnh. Đã sửa 1 từ đó, còn lại giữ nguyên bản dịch tại obasan 2637.

- JP: 「うふふ、ごちそうさまでした。
これで明日も頑張れそう！　おやすみなさい、双鉄くん」
- TW: 「呵呵呵，多謝。這樣我明天也有動力了！晚安，雙鐵君」
- Cũ: 「Đây là bản nhạc biểu tượng của các chuyến tàu đường dài thời Đế Thiết cũ.
Thật vui khi họ lại chăm chút đến mức này.」
- Sửa: 「Fufufu, cảm ơn anh vì bữa ăn nha.
Thế này thì ngày mai em lại có thêm động lực rồi! Chúc ngủ ngon, anh Soutetsu.」

**1760 [Paulette]** — Bản Việt hiện tại là bản dịch đúng của obasan key 2017 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 2017 (obasan 2017 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: 「あ――――（ちゅっ）」
- TW: 「啊……（啾）」
- Cũ: 「Fufufu. Bé Hikari thích bắt chước nhỉ.」
- Sửa: 「A—— (Chụt)」

**1797 [Soutetsu]** — Bản Việt hiện tại là bản dịch đúng của obasan key 2277 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 2277 (obasan 2277 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: 「――うん。ありがとう」
- TW: 「嗯。謝謝你」
- Cũ: Phát thanh trên tàu.
Ngay khoảnh khắc âm thanh vang lên, đôi mắt Hikari càng thêm lấp lánh.
- Sửa: 「——Ừm. Cảm ơn em.」

**1807 [Soutetsu]** — Bản Việt hiện tại là bản dịch đúng của obasan key 1704 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 1704 (obasan 1704 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: 「ああ、おやすみ、ポーレット」
- TW: 「嗯，晚安，波萊特」
- Cũ: 「Vui quá, hoài niệm quá~」
- Sửa: 「Ừm, chúc ngủ ngon, Paulette.」

**1892 [Paulette]** — Bản Việt hiện tại ("Đính chính lại. Ngon quá!") là bản dịch đúng của obasan 1978 — tràn chương obasan → sleeper. Bản dịch đúng của dòng này không tồn tại ở đâu trong dự án (đã tra chỉ mục Việt toàn dự án) — dịch mới từ JP + TW (TW 回去 ủng hộ "về đây" thay vì "đi đây").

- JP: 「ですから、わたし、行きます――けど」
- TW: 「所以，我回去了——」
- Cũ: 「Đính chính lại. Ngon quá!」
- Sửa: 「Vì vậy, em về đây—— nhưng mà...」

**2053 [Soutetsu]** — Bản Việt hiện tại là bản dịch đúng của obasan key 2265 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 2265 (obasan 2265 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: 「旅の準備もなにもかも、
頑張ってくれてるお礼――というか、ご褒美だ」
- TW: 「謝謝你準備旅行，還有在各種事情上都這麼努力，所以我想獎勵你」
- Cũ: 「Không cần thêm câu đính chính đâu con~」
- Sửa: 「Cảm ơn em vì đã vất vả chuẩn bị cho chuyến đi và lo liệu mọi thứ——
Nói đúng hơn là, phần thưởng cho em đây.」

**2432 [lời dẫn]** — Bản Việt hiện tại là bản dịch đúng của obasan key 1583 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 1583 (obasan 1583 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: くっついたまま、
鼻先同士、おでこ同士をすりあわせる。
- TW: 我們仍然緊緊相擁，耳鬢廝磨著。
- Cũ: 「Là khúc dạ khúc Heykens!」
- Sửa: Cứ dính chặt lấy nhau như thế,
chúng tôi cọ mũi, cọ trán vào nhau.

**2450 [lời dẫn]** — Bản Việt hiện tại là bản dịch đúng của obasan key 1628 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 1628 (obasan 1628 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: 胸が高なり、体が騒いでしまっている。
瞳を閉じて、レールのつなぎ目の数でも数えてみよう。
- TW: 我的心卻跳個不停，身體也難以平靜下來。我閉上眼睛，試著開始數鐵軌接縫。
- Cũ: 「Hả? Mới đến Iwaki thôi sao?」
- Sửa: Tim đập rộn ràng, cơ thể rạo rực không yên.
Thôi thì nhắm mắt lại, đếm số lần bánh xe lăn qua mối nối đường ray xem sao.

**2459 [lời dẫn]** — Bản Việt hiện tại là bản dịch đúng của obasan key 1961 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 1961 (obasan 1961 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: 軽いキス。
ポーレットは幸せそうに、笑ってくれる。
- TW: 我輕輕一吻。波萊特幸福地笑了。
- Cũ: 「Fufufu, Hikari thích bắt chước mà~」
- Sửa: Một nụ hôn nhẹ nhàng.
Paulette mỉm cười đầy hạnh phúc.

**2519 [lời dẫn]** — Bản Việt hiện tại là bản dịch đúng của obasan key 1682 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 1682 (obasan 1682 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: すりっと、ポーレットの顔が僕の胸板に甘えてくる。
小さな頭を両手でつかまえ、僕へと向かせる。
- TW: 波萊特的臉又蹭了蹭我的胸口。我伸出雙手抓住她小小的頭，讓她面對著我。
- Cũ: 「Không cần thêm câu đính chính đâu con.」
- Sửa: Paulette lại cọ cọ khuôn mặt nũng nịu vào ngực tôi.
Tôi đưa hai tay ôm lấy chiếc đầu nhỏ nhắn, xoay em ấy đối diện với mình.

**2531 [lời dẫn]** — Bản Việt hiện tại là bản dịch đúng của obasan key 1830 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 1830 (obasan 1830 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: どちらにしても、それは最高の瞬間となる。
絶対、見逃したくは無い。
- TW: 無論如何，那對我來說都會是最棒的瞬間，絕對不容錯過。
- Cũ: 「Oa oa! Tiền vé tàu tốc hành được miễn phí luôn!」
- Sửa: Dù thế nào đi nữa, đó cũng sẽ là một khoảnh khắc tuyệt vời nhất.
Tuyệt đối không thể bỏ lỡ.

**2570 [lời dẫn]** — Bản Việt hiện tại là bản dịch đúng của obasan key 2517 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 2517 (obasan 2517 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: カーテンを開けてまた閉めて、
ポーレットは向かいの寝台へと戻っていく。
- TW: 簾子拉開，隨後又合上。波萊特回到了對面的鋪位。
- Cũ: Sự đáng sợ của giáo dục—— hay nói đúng hơn là sự kinh khủng của nó,
như được phơi bày rõ mồn một trước mắt tôi.
- Sửa: Rèm mở ra rồi lại đóng vào,
Paulette quay trở về chiếc giường đối diện.

**2584 [lời dẫn]** — Bản Việt hiện tại là bản dịch đúng của obasan key 2478 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 2478 (obasan 2478 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: 雪景色なら、嬉しかろう。
もしもそうならひかりにとっては、初めての雪だ。
- TW: 若是雪景，我一定會很開心。若真是雪景，那就會是光第一次見到雪。
- Cũ: Chẳng lẽ…… tàu đang chạy giảm tốc sao?」
- Sửa: Nếu là khung cảnh tuyết trắng thì thật tuyệt.
Nếu vậy, đây sẽ là lần đầu tiên Hikari được thấy tuyết.

**2646 [lời dẫn]** — Bản Việt hiện tại là bản dịch đúng của obasan key 2503 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 2503 (obasan 2503 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: 名残惜しいが、ここまでにして体を離す。
これ以上に血が熱くなれば、眠れなくなってしまうから。
- TW: 雖然很捨不得，但我倆就此分開了身體。如果再熱血上湧的話，我就睡不著了。
- Cũ: 「Hửm?」
- Sửa: Dù luyến tiếc, nhưng đến đây thì đành phải buông nhau ra thôi.
Bởi nếu máu trong người nóng lên hơn nữa thì sẽ không ngủ được mất.

**2662 [lời dẫn]** — Bản Việt hiện tại là bản dịch đúng của obasan key 2563 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 2563 (obasan 2563 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: （……あれほど軽いキスだったのにな）
- TW: （……明明那輕吻不過蜻蜓點水一般）
- Cũ: 「Chào buổi sáng quý hành khách.
Đoàn tàu sắp sửa đến ga Iwaki.」
- Sửa: （……Rõ ràng chỉ là một nụ hôn nhẹ thôi mà.）

**2681 [lời dẫn]** — Bản Việt hiện tại là bản dịch đúng của obasan key 1809 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 1809 (obasan 1809 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: （笑顔になるのか――驚いて固まってしまうかな？）
- TW: （她是會笑呢，還是會驚訝得動彈不得呢？）
- Cũ: 「Chậm hơn lịch trình dự kiến 130 phút rồi nha.」
- Sửa: （Con bé sẽ mỉm cười—— hay là ngạc nhiên đến đơ người ra nhỉ?）

**2684 [lời dẫn]** — Bản Việt hiện tại là bản dịch đúng của obasan 1135 — tràn chương obasan → sleeper. Bản dịch đúng của dòng này không tồn tại ở đâu trong dự án — dịch mới: JP （シャーっ）, TW （沙——） là âm thanh xào xạc/vù vù kéo dài (trong cảnh tàu đêm đang chạy), không phải tiếng "xình xịch" của bánh xe.

- JP: （シャーっ）
- TW: （沙——）
- Cũ: ……Một đứa trẻ 4 tuổi, rõ ràng chưa từng có cơ hội trải nghiệm,
lại cảm thấy hoài niệm về chuyến tàu đường dài thời Đế Thiết.
- Sửa: （Vù——）

**2688 [lời dẫn]** — Bản Việt hiện tại là bản dịch đúng của obasan key 2466 (đã xác minh JP/TW tại obasan) — tràn chương hai chiều obasan ↔ sleeper; bản dịch đúng của dòng này đang nằm sai vị trí tại obasan 2466 (obasan 2466 đã có trong danh sách sai của audit obasan, sẽ được sửa bằng bản dịch đúng của JP obasan).

- JP: （目が覚めたとき……どこまでたどり着けているのか）
- TW: （等我醒來的時候……不知能見到怎樣的景色呢）
- Cũ: Nghe vậy, tôi hướng mắt ra ngoài cửa sổ.
Cảnh vật trôi qua một cách chậm chạp.
- Sửa: （Khi tỉnh dậy…… không biết tàu đã đến đâu rồi nhỉ.）

### Xưng hô (16 dòng)

**1222 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói về Hikari; theo docs (locations §2.1) Soutetsu tự xưng "Tôi" ("Anh" chỉ khi nói với Hibiki).

- JP: 「……出会いは、大事だ。
その機会を、ひかりにはむざむざ失って欲しくはない」
- TW: 「……人與人的相遇，是很珍貴的。我不希望光輕易地錯過那樣的機會」
- Cũ: 「……Sự gặp gỡ rất quan trọng.
Anh không muốn Hikari đánh mất cơ hội đó một cách vô ích.」
- Sửa: 「……Sự gặp gỡ rất quan trọng.
Tôi không muốn Hikari đánh mất cơ hội đó một cách vô ích.」

**1240 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với người của Michitetsu; theo docs "Tôi".

- JP: 「……話をしてみたいものだな。みち鉄の方と」
- TW: 「……真想跟陸鐵的工作人員好好聊聊啊」
- Cũ: 「……Anh muốn nói chuyện thử xem sao. Với người của Michitetsu ấy.」
- Sửa: 「……Tôi muốn nói chuyện thử xem sao. Với người của Michitetsu ấy.」

**1248 [Soutetsu]** — Hai lỗi: (1) Soutetsu tự xưng "anh" → "Tôi"; (2) đảo chủ thể — JP 再会できて là "chúng ta gặp lại" (Soutetsu cùng Paulette/Reina gặp lại chuyến tàu), bản cũ "Khi em có thể gặp lại" gán việc gặp lại cho riêng Paulette.

- JP: 「……言い直そう。嬉しいことだな。
思い出の列車と、また新しいレールの上で、再会できて」
- TW: 「……那容我換個說法吧。能與充滿回憶的列車在新的線路上再次相遇是一件值得高興的事」
- Cũ: 「……Để anh nói lại nhé. Thật đáng mừng.
Khi em có thể gặp lại chuyến tàu kỷ niệm trên một tuyến đường ray mới.」
- Sửa: 「……Để tôi nói lại nhé. Thật đáng mừng.
Khi chúng ta có thể gặp lại chuyến tàu kỷ niệm trên một tuyến đường ray mới.」

**1604 [Soutetsu]** — Soutetsu tự xưng "anh"; theo docs "Tôi".

- JP: 「[せんだい,1]仙岱近郊となると……
それほどには雪の降らない印象もあるが」
- TW: 「不過既然她去了仙台近郊……那邊好像並不怎麼下雪」
- Cũ: 「Nếu là vùng ngoại ô Sendai thì……
Anh có ấn tượng là tuyết không rơi nhiều đến thế.」
- Sửa: 「Nếu là vùng ngoại ô Sendai thì……
Tôi có ấn tượng là tuyết không rơi nhiều đến thế.」

**1614 [Soutetsu]** — Sai người được gọi: Soutetsu khen Hikari (4 tuổi) — bản cũ "Hôm nay em đã làm rất tốt" dùng "em"; trong file Soutetsu gọi Hikari là "con" (1633, 1957).

- JP: 「良く頑張ったし。頑張っているな」
- TW: 「今天你真的很努力。真的很努力啊」
- Cũ: 「Hôm nay em đã làm rất tốt. Rất cố gắng đấy.」
- Sửa: 「Hôm nay con đã làm rất tốt. Rất cố gắng đấy.」

**1623 [Soutetsu]** — Đảo chủ thể: JP カメラを出すには早すぎる ("còn quá sớm để lấy máy ảnh ra") — Paulette định lấy máy ảnh ra, Soutetsu ngăn lại; bản cũ "Anh cũng không cần lấy máy ảnh ra" biến Soutetsu thành chủ thể. Sửa thành "Em cũng không cần..." (gọi Paulette).

- JP: 「カメラを出すには早すぎる」
- TW: 「你也不用現在就拿相機出來吧」
- Cũ: 「Anh cũng không cần lấy máy ảnh ra sớm thế đâu.」
- Sửa: 「Em cũng không cần lấy máy ảnh ra sớm thế đâu.」

**1833 [Soutetsu]** — Soutetsu tự xưng "anh" khi nói với Paulette; theo docs "Tôi". "Em" (gọi Paulette) giữ nguyên.

- JP: 「今回の旅行も、ポーレットのおかげで実現できた。
おかげで、最高に楽しめている」
- TW: 「多虧了波萊特，才有了我們這次旅行。我現在非常開心」
- Cũ: 「Chuyến du lịch lần này thực hiện được cũng là nhờ có Paulette.
Nhờ có em mà anh đang tận hưởng chuyến đi một cách tuyệt vời nhất.」
- Sửa: 「Chuyến du lịch lần này thực hiện được cũng là nhờ có Paulette.
Nhờ có em mà tôi đang tận hưởng chuyến đi một cách tuyệt vời nhất.」

**1887 [Soutetsu]** — Soutetsu tự xưng "anh" 2 lần khi nói với Paulette; theo docs "Tôi". "Em" (gọi Paulette) giữ nguyên.

- JP: 「だよなぁ。であればあのとき、
僕に声をかけてくれてもいなかっただろうし――」
- TW: 「我想也是。要不然那時候，你也不會跟我搭話的」
- Cũ: 「Anh cũng nghĩ vậy. Nếu thế thì lúc đó,
em đã chẳng bắt chuyện với anh rồi——」
- Sửa: 「Tôi cũng nghĩ vậy. Nếu thế thì lúc đó,
em đã chẳng bắt chuyện với tôi rồi——」

**1920 [Soutetsu]** — Soutetsu tự xưng "anh"; theo docs "Tôi".

- JP: 「だよなぁ。が、いつまでも箱入りにもしておけん。
やはり健やかに成長してほしい」
- TW: 「是啊。但是，我們也不能一直這樣嬌慣她。還是希望她能沐浴著外面的風雨健康成長」
- Cũ: 「Đúng vậy nhỉ. Nhưng chúng ta cũng không thể cứ giấu con bé trong tủ kính mãi được.
Anh vẫn mong con bé lớn lên khỏe mạnh.」
- Sửa: 「Đúng vậy nhỉ. Nhưng chúng ta cũng không thể cứ giấu con bé trong tủ kính mãi được.
Tôi vẫn mong con bé lớn lên khỏe mạnh.」

**1961 [Soutetsu]** — Soutetsu tự xưng "anh"; theo docs "Tôi".

- JP: 「いや、ダブルミーニングかと思ったのだ。
『湯を巡る』と、『夢を巡る』で、『ゆめぐり』かと」
- TW: 「沒什麼，我在想這個是不是雙關。這個“夢巡”的夢不光是溫泉，更是鐵路人的夢想」
- Cũ: 「Không, anh đang nghĩ đó có phải là chơi chữ không.
『Dạo quanh suối nước nóng (Yu wo meguru)』 và 『Dạo quanh những giấc mơ (Yume wo meguru)』, nên mới là 『Yumeguri』.」
- Sửa: 「Không, tôi đang nghĩ đó có phải là chơi chữ không.
『Dạo quanh suối nước nóng (Yu wo meguru)』 và 『Dạo quanh những giấc mơ (Yume wo meguru)』, nên mới là 『Yumeguri』.」

**2036 [Soutetsu]** — Soutetsu tự xưng "anh" ("Vé của anh") khi nói với Paulette; theo docs "Tôi". "Em" (gọi Paulette) giữ nguyên.

- JP: 「寝台券の方はどうなっているのだ？
僕とポーレットとれいなの分は当然だろうが――」
- TW: 「臥鋪票買好了嗎？我和波萊特還有玲奈的票當然是買了」
- Cũ: 「Vé giường nằm thế nào rồi em?
Vé của anh, em và Reina thì chắc chắn là có rồi, nhưng——」
- Sửa: 「Vé giường nằm thế nào rồi em?
Vé của tôi, em và Reina thì chắc chắn là có rồi, nhưng——」

**2037 [Soutetsu]** — Soutetsu tự xưng "anh"; theo docs "Tôi".

- JP: 「いいものだな。寝台列車は。
聞いていた話以上だ。実に良い」
- TW: 「臥鋪車真好啊。百聞不如一見。真是太棒了」
- Cũ: 「Tàu giường nằm thích thật đấy.
Tuyệt vời hơn cả những gì anh từng nghe kể. Thực sự rất tuyệt.」
- Sửa: 「Tàu giường nằm thích thật đấy.
Tuyệt vời hơn cả những gì tôi từng nghe kể. Thực sự rất tuyệt.」

**2082 [Soutetsu]** — Soutetsu tự xưng "anh"; theo docs "Tôi".

- JP: 「それは確かに落ち着かんかな。
どんな様子か見てみたい気もするが」
- TW: 「這麼說，車上可能的確會比較亂，來來往往的。好想親眼看看那個場面啊」
- Cũ: 「Thế thì chắc chắn là không thể nghỉ ngơi yên tĩnh được rồi.
Anh cũng tò mò muốn xem thử nó như thế nào.」
- Sửa: 「Thế thì chắc chắn là không thể nghỉ ngơi yên tĩnh được rồi.
Tôi cũng tò mò muốn xem thử nó như thế nào.」

**2095 [Soutetsu]** — Soutetsu tự xưng "anh" khi nhờ Reina đỡ Hikari; theo docs "Tôi".

- JP: 「そうしたら体からベッドにごろんだ。
れいな、つかまえてやってくれ」
- TW: 「那就用身體爬到床上去。玲奈，接她一下」
- Cũ: 「Thế thì con rướn người bò lên giường đi.
Reina, đỡ con bé giúp anh với.」
- Sửa: 「Thế thì con rướn người bò lên giường đi.
Reina, đỡ con bé giúp tôi với.」

**2339 [lời dẫn]** — Độc thoại của Soutetsu dùng "mình" làm chủ ngữ độc lập ("Đến cả mình cũng bao bọc..."); quy ước của file là "Tôi" (48 dòng "tôi", chỉ 2 dòng "mình" chủ ngữ độc lập sai — 2339 và 2590).

- JP: 僕まで過保護になってどうする。
ひかりがせっかく、自立心を発揮しようとしているのだ。
- TW: 可不能連我都成了過度保護孩子的家長。難得光想發揚獨立性啊。
- Cũ: Đến cả mình cũng bao bọc con quá mức thì làm sao được.
Hikari đang khó khăn lắm mới bộc lộ tính tự lập mà.
- Sửa: Đến cả tôi cũng bao bọc con quá mức thì làm sao được.
Hikari đang khó khăn lắm mới bộc lộ tính tự lập mà.

**2590 [lời dẫn]** — Độc thoại của Soutetsu dùng "mình" làm chủ ngữ độc lập ("hay là mình——"); quy ước của file là "Tôi". JP どれ、僕が―― xác nhận chủ ngữ là Soutetsu.

- JP: どれ、僕が――
- TW: 要不，我就……
- Cũ: Để xem, hay là mình——
- Sửa: Để xem, hay là tôi——

### Thuật ngữ (5 dòng)

**1819 [Soutetsu]** — 回数券 = vé lượt (vé đi nhiều lượt, TW 多次票); bản cũ "vé tháng" là vé đi theo tháng — loại vé khác. Phân biệt với 定期券 = "vé định kỳ" (2038, đúng, không sửa).

- JP: 「おお！　なるほど。そうか、回数券では、
鋏痕による乗車駅特定が必要になるか」
- TW: 「噢！確實。是這樣啊，用多次票的時候，就需要靠鉗口來區別搭車的那站了」
- Cũ: 「Ồ! Ra là vậy. Thì ra là với vé tháng, người ta cần xác định ga lên tàu dựa vào vết cắt à.」
- Sửa: 「Ồ! Ra là vậy. Thì ra là với vé lượt, người ta cần xác định ga lên tàu dựa vào vết cắt à.」

**1832 [Hikari]** — 回数券 = vé lượt (TW 多次票); bản cũ "vé tháng" — loại vé khác.

- JP: 「かいすうけんは、どっちからでものれるもーん」
- TW: 「多次票從哪裡上車都可以呀」
- Cũ: 「Vé tháng thì lên từ ga nào cũng được mà.」
- Sửa: 「Vé lượt thì lên từ ga nào cũng được mà.」

**1931 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohito".

- JP: 「ですね。御一夜と似た感じの交通難所で、その上雪深い。
最初から観光のための手段として、鉄道を残した町です」
- TW: 「是啊。那裡與御一夜差不多，交通不便，而且經常降雪。那裡也是以觀光為目的從一開始就留下鐵路的城市」
- Cũ: 「Vâng. Là một nơi giao thông khó khăn giống như Ohito, hơn nữa tuyết lại rơi dày.
Đây là thị trấn giữ lại đường sắt ngay từ đầu như một phương tiện phục vụ du lịch.」
- Sửa: 「Vâng. Là một nơi giao thông khó khăn giống như Ohitoyo, hơn nữa tuyết lại rơi dày.
Đây là thị trấn giữ lại đường sắt ngay từ đầu như một phương tiện phục vụ du lịch.」

**1946 [Paulette]** — 御一夜鉄道 = "Đường sắt Ohitoyo" (quyết định 19/11); bản cũ "Đường sắt Ohito".

- JP: 「はい。巡り合わせ次第では、うちに――
御一夜鉄道に来てくれる可能性もありました」
- TW: 「是的。原本如果有緣，她也有可能來到我們這裡——來到御一夜鐵路」
- Cũ: 「Vâng. Tùy thuộc vào duyên số, cô bé đó cũng có khả năng——
Đến với Đường sắt Ohito của chúng ta đấy ạ.」
- Sửa: 「Vâng. Tùy thuộc vào duyên số, cô bé đó cũng có khả năng——
Đến với Đường sắt Ohitoyo của chúng ta đấy ạ.」

**2560 [lời dẫn]** — 回数券 = vé lượt (TW 多次票); bản cũ "vé tháng" 2 lần — loại vé khác.

- JP: 確かにだ。回数券には、日付の記入がなされない。
ゆえ、最低料金回数券を、発駅で入鋏してもらう――
- TW: 確實。多次票上不會記錄日期。因此，只要拿著最低價的多次票，在出發站點剪一次票——
- Cũ: Đúng là vậy. Vé tháng không ghi ngày tháng.
Vì thế, chỉ cần mua vé tháng mệnh giá thấp nhất, rồi nhờ bấm vé ở ga đi——
- Sửa: Đúng là vậy. Vé lượt không ghi ngày tháng.
Vì thế, chỉ cần mua vé lượt mệnh giá thấp nhất, rồi nhờ bấm vé ở ga đi——

### Sai nghĩa (3 dòng)

**1636 [Hikari]** — Bịa thêm: JP chỉ là câu bỏ lửng ngập ngừng của Hikari (うーんと……うーんとぉ), không có động từ "chọn"; TW cũng bỏ lửng. Theo quy tắc P13 1510 / P16 1838: không bịa phần kết cho câu JP bỏ lửng.

- JP: 「ひかり……ひかり、ねぇ。
うーんと……うーんとぉ」
- TW: 「光……光要……唔……唔……」
- Cũ: 「Hikari…… Hikari chọn.
Ưm…… ưm.」
- Sửa: 「Hikari…… Hikari……
Ưm…… ưm.」

**2389 [lời dẫn]** — 誘導 = hướng dẫn/dẫn dắt; bản cũ "dụ dỗ" mang nghĩa dụ dỗ/lôi kéo (sai ngữ cảnh — Soutetsu đang dẫn dắt Hikari, TW 引導 xác nhận).

- JP: 笑顔が輝く。
これなら誘導できそうだ。
- TW: 她露出了燦爛的笑容。看來，我的引導很順利。
- Cũ: Nụ cười tỏa nắng rạng rỡ.
Thế này thì chắc là dụ dỗ được rồi.
- Sửa: Nụ cười tỏa nắng rạng rỡ.
Thế này thì chắc là dẫn dắt được rồi.

**2446 [lời dẫn]** — Sai thì: JP 自分がどんな人生を歩んでいたか là giả định quá khứ ("cuộc đời mình ĐÃ sống ra sao"); bản cũ "Tôi sẽ bước vào một cuộc đời như thế nào" dùng thì tương lai. TW 我現在會過著怎樣的人生 xác nhận đây là giả định.

- JP: 自分がどんな人生を歩んでいたか、
想像するだけでも恐ろしい。
- TW: 我甚至想都不敢想，自己現在會過著怎樣的人生。
- Cũ: Tôi sẽ bước vào một cuộc đời như thế nào đây,
chỉ tưởng tượng thôi cũng thấy đáng sợ rồi.
- Sửa: Tôi đã sống một cuộc đời như thế nào,
chỉ tưởng tượng thôi cũng thấy đáng sợ rồi.

### Lỗi nhỏ (5 dòng)

**1779 [Hikari]** — Mất tiếng hít っ: JP 「っ！！？」 chỉ còn "「!?」" — khôi phục "Ư!?".

- JP: 「っ！！？」
- TW: 「啊？！」
- Cũ: 「!?」
- Sửa: 「Ư!?」

**1781 [Paulette]** — はぅう là tiếng thở dài ngái ngủ, không phải câu hỏi; bản cũ "Hả." đọc thành câu hỏi. TW 嗚 xác nhận đây là tiếng thở ra.

- JP: 「はぅう」
- TW: 「嗚」
- Cũ: 「Hả.」
- Sửa: 「Hau.」

**2081 [Soutetsu]** — Lỗi gõ: "đối đối phó" thừa một chữ "đối".

- JP: 「ナビによる補正がかかってもなお、
対応できないほどの風が吹くのか？」
- TW: 「這裡的風這麼厲害嗎，連導航系統的調節都應對不了？」
- Cũ: 「Ngay cả khi có sự điều chỉnh của hệ thống dẫn đường, gió vẫn thổi mạnh đến mức không thể đối đối phó được sao?」
- Sửa: 「Ngay cả khi có sự điều chỉnh của hệ thống dẫn đường, gió vẫn thổi mạnh đến mức không thể đối phó được sao?」

**2402 [lời dẫn]** — Thừa dấu đóng 」: lời dẫn (không có ngoặc mở 「) nhưng cuối câu có 」 lẻ.

- JP: みっちりとした、あまりにも素晴らしすぎる秘密基地感。
ここを家族で独占できる――うむ？
- TW: 封閉的車廂有種相當真實、堪稱完美的秘密基地的感覺。而我們一家人此刻可以獨占這裡……唔？
- Cũ: Cảm giác kín đáo, giống như một căn cứ bí mật tuyệt vời.
Cả gia đình có thể độc chiếm nơi này—— hửm?」
- Sửa: Cảm giác kín đáo, giống như một căn cứ bí mật tuyệt vời.
Cả gia đình có thể độc chiếm nơi này—— hửm?

**2690 [lời dẫn]** — Sai hiệu ứng âm thanh: JP （ゴーーーーーっ） là tiếng gầm/vù kéo dài (TW 隆——), bản cũ "Xình xịch xình xịch" là tiếng lách cách của bánh xe trên mối nối (ガタンゴトン) — âm khác.

- JP: （ゴーーーーーっ）
- TW: （隆——）
- Cũ: （Xình xịch xình xịch——）
- Sửa: （Ù ù ù ù——）

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
1222 = "「……Sự gặp gỡ rất quan trọng.\nTôi không muốn Hikari đánh mất cơ hội đó một cách vô ích.」"
1240 = "「……Tôi muốn nói chuyện thử xem sao. Với người của Michitetsu ấy.」"
1248 = "「……Để tôi nói lại nhé. Thật đáng mừng.\nKhi chúng ta có thể gặp lại chuyến tàu kỷ niệm trên một tuyến đường ray mới.」"
1604 = "「Nếu là vùng ngoại ô Sendai thì……\nTôi có ấn tượng là tuyết không rơi nhiều đến thế.」"
1614 = "「Hôm nay con đã làm rất tốt. Rất cố gắng đấy.」"
1623 = "「Em cũng không cần lấy máy ảnh ra sớm thế đâu.」"
1624 = "「Cũng là phần thưởng cho anh Soutetsu vì đã vất vả nhé!\n(Chụt!)」"
1636 = "「Hikari…… Hikari……\nƯm…… ưm.」"
1712 = "「Fufufu, cảm ơn anh vì bữa ăn nha.\nThế này thì ngày mai em lại có thêm động lực rồi! Chúc ngủ ngon, anh Soutetsu.」"
1760 = "「A—— (Chụt)」"
1779 = "「Ư!?」"
1781 = "「Hau.」"
1797 = "「——Ừm. Cảm ơn em.」"
1807 = "「Ừm, chúc ngủ ngon, Paulette.」"
1819 = "「Ồ! Ra là vậy. Thì ra là với vé lượt, người ta cần xác định ga lên tàu dựa vào vết cắt à.」"
1832 = "「Vé lượt thì lên từ ga nào cũng được mà.」"
1833 = "「Chuyến du lịch lần này thực hiện được cũng là nhờ có Paulette.\nNhờ có em mà tôi đang tận hưởng chuyến đi một cách tuyệt vời nhất.」"
1887 = "「Tôi cũng nghĩ vậy. Nếu thế thì lúc đó,\nem đã chẳng bắt chuyện với tôi rồi——」"
1892 = "「Vì vậy, em về đây—— nhưng mà...」"
1920 = "「Đúng vậy nhỉ. Nhưng chúng ta cũng không thể cứ giấu con bé trong tủ kính mãi được.\nTôi vẫn mong con bé lớn lên khỏe mạnh.」"
1931 = "「Vâng. Là một nơi giao thông khó khăn giống như Ohitoyo, hơn nữa tuyết lại rơi dày.\nĐây là thị trấn giữ lại đường sắt ngay từ đầu như một phương tiện phục vụ du lịch.」"
1946 = "「Vâng. Tùy thuộc vào duyên số, cô bé đó cũng có khả năng——\nĐến với Đường sắt Ohitoyo của chúng ta đấy ạ.」"
1961 = "「Không, tôi đang nghĩ đó có phải là chơi chữ không.\n『Dạo quanh suối nước nóng (Yu wo meguru)』 và 『Dạo quanh những giấc mơ (Yume wo meguru)』, nên mới là 『Yumeguri』.」"
2036 = "「Vé giường nằm thế nào rồi em?\nVé của tôi, em và Reina thì chắc chắn là có rồi, nhưng——」"
2037 = "「Tàu giường nằm thích thật đấy.\nTuyệt vời hơn cả những gì tôi từng nghe kể. Thực sự rất tuyệt.」"
2053 = "「Cảm ơn em vì đã vất vả chuẩn bị cho chuyến đi và lo liệu mọi thứ——\nNói đúng hơn là, phần thưởng cho em đây.」"
2081 = "「Ngay cả khi có sự điều chỉnh của hệ thống dẫn đường, gió vẫn thổi mạnh đến mức không thể đối phó được sao?」"
2082 = "「Thế thì chắc chắn là không thể nghỉ ngơi yên tĩnh được rồi.\nTôi cũng tò mò muốn xem thử nó như thế nào.」"
2095 = "「Thế thì con rướn người bò lên giường đi.\nReina, đỡ con bé giúp tôi với.」"
2339 = "Đến cả tôi cũng bao bọc con quá mức thì làm sao được.\nHikari đang khó khăn lắm mới bộc lộ tính tự lập mà."
2389 = "Nụ cười tỏa nắng rạng rỡ.\nThế này thì chắc là dẫn dắt được rồi."
2402 = "Cảm giác kín đáo, giống như một căn cứ bí mật tuyệt vời.\nCả gia đình có thể độc chiếm nơi này—— hửm?"
2432 = "Cứ dính chặt lấy nhau như thế,\nchúng tôi cọ mũi, cọ trán vào nhau."
2446 = "Tôi đã sống một cuộc đời như thế nào,\nchỉ tưởng tượng thôi cũng thấy đáng sợ rồi."
2450 = "Tim đập rộn ràng, cơ thể rạo rực không yên.\nThôi thì nhắm mắt lại, đếm số lần bánh xe lăn qua mối nối đường ray xem sao."
2459 = "Một nụ hôn nhẹ nhàng.\nPaulette mỉm cười đầy hạnh phúc."
2519 = "Paulette lại cọ cọ khuôn mặt nũng nịu vào ngực tôi.\nTôi đưa hai tay ôm lấy chiếc đầu nhỏ nhắn, xoay em ấy đối diện với mình."
2531 = "Dù thế nào đi nữa, đó cũng sẽ là một khoảnh khắc tuyệt vời nhất.\nTuyệt đối không thể bỏ lỡ."
2560 = "Đúng là vậy. Vé lượt không ghi ngày tháng.\nVì thế, chỉ cần mua vé lượt mệnh giá thấp nhất, rồi nhờ bấm vé ở ga đi——"
2570 = "Rèm mở ra rồi lại đóng vào,\nPaulette quay trở về chiếc giường đối diện."
2584 = "Nếu là khung cảnh tuyết trắng thì thật tuyệt.\nNếu vậy, đây sẽ là lần đầu tiên Hikari được thấy tuyết."
2590 = "Để xem, hay là tôi——"
2646 = "Dù luyến tiếc, nhưng đến đây thì đành phải buông nhau ra thôi.\nBởi nếu máu trong người nóng lên hơn nữa thì sẽ không ngủ được mất."
2662 = "（……Rõ ràng chỉ là một nụ hôn nhẹ thôi mà.）"
2681 = "（Con bé sẽ mỉm cười—— hay là ngạc nhiên đến đơ người ra nhỉ?）"
2684 = "（Vù——）"
2688 = "（Khi tỉnh dậy…… không biết tàu đã đến đâu rồi nhỉ.）"
2690 = "（Ù ù ù ù——）"
```

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- **Soutetsu gọi Paulette "cô" vs "em": "em" 12×, "cô" 0×** — "em" tại 1248, 1623, 1627*, 1669, 1809, 1820, 1833, 1887, 1907, 1939, 2036, 2052, 2080 (*1627 người được gọi chưa rõ Paulette hay Hikari — xem mục "Không tính là sai"). 1829 có chữ "cô bé" nhưng đó là chỉ đầu máy/toa xe (Railord), không phải gọi Paulette, nên không tính. 1614 gọi Hikari là "em" (sai — đã sửa thành "con"), 2002 gọi Reina là "em" (đúng, không phải Paulette). Tally lũy kế toàn dự án: "cô" 43 vs "em" 47 (cộng 13 "em" của file này — "em" lần đầu vượt "cô").
- **湯医: 0 lần; 帝鉄: JP 帝鉄 1× (1925, dịch "Đế Thiết")** — bản Việt có "Đế Thiết" 3× (1925 đúng + 1712/2684 là bản sao lệch vị trí từ obasan). Ghi nhận, không áp dụng.
- **駿袋鉄道: 1× tại 1966, dịch "Đường sắt Suntetsu"** — khác với đề xuất "Đường sắt Suntai" (theo ruby JP すんたい). Ghi nhận thêm bằng chứng, không áp dụng (quyết định đang chờ).
- **とき鉄 → "Tokitetsu" (1928), 津っ鐵 → "Tsuttetsu" (1829, theo ruby つってつ)** — ghi nhận, không tính sai.
- **"KiHa" 1×, "Kiha" 0×** — gloss `%l` trong file này dùng "KiHa". Ghi nhận cho quyết định "KiHa" vs "Kiha" đang chờ.
- **コン: 0 lần; 宮司: 0 lần; 冥国/冥軍: 0 lần** trong file này.
- **回数券 → "vé lượt"** — xem đề xuất dưới đây (thêm vào glossary).

## Đề xuất cập nhật context (chưa chốt)

- **Thêm 回数券 → "vé lượt" vào glossary (context_trans.md):** TW 多次票 xác nhận đây là vé đi nhiều lượt, khác hẳn 定期券 = "vé định kỳ" (vé tháng/vé theo kỳ — 2038 dịch đúng, không sửa). Người dịch đã nhầm hai loại vé này tại 3 dòng (1819, 1832, 2560).

## Đã kiểm tra và KHÔNG tính là sai

- **1627 — ĐÃ QUYẾT 19/11 (xem Bổ sung ở cuối file):** Soutetsu hỏi Hikari, không phải Paulette — đã chuyển sang danh sách sửa ("Con có muốn lên trên không?").
- **"mình" trong "tự mình"/"một mình" (1633, 1911, 1957)** — thành ngữ phản thân, không phải đại từ xưng hô; "chính tay mình" tại 2477 là sở hữu thành ngữ. Không tính sai.
- **"mình" sở hữu/chung (1196 "con gái mình", 2307 "những món mình thích", 2328 "bản thân mình")** — không phải chủ ngữ độc lập. Không tính sai.
- **2002 "em" gọi Reina** — Reina nhỏ tuổi hơn, gọi "em" đúng; không phải Paulette nên không tính vào tally "cô"/"em".
- **2038 定期券 → "vé định kỳ"** — chấp nhận được, phân biệt đúng với 回数券 = "vé lượt". Không sửa.
- **2080 印籠 → "hộp ấn"** — cách dịch còn bàn được nhưng truyền đạt đúng vật (hộp đựng ấn của Mito Komon); không tính sai.
- **2381 câu trích trực tiếp bịa thêm ("Anh cản con bé lại đi")** — JP 止めて欲しいと、焦った声から伝わってくる diễn đạt ý "muốn nhờ ngăn con bé lại"; bản Việt chuyển thành lời thoại trực tiếp nhưng giữ đúng nghĩa. Không tính sai.
- **"Kyaa!" trùng 1704/1734, "Ồ." trùng 1817/1744/1941** — JP tương ứng đều là tiếng cảm thán giống nhau, đều đúng.
- **7 dòng thêm gloss `%l` mà JP không có (1174, 1925, 2007, 2107, 2301, 2321, 2630)** — cùng quy ước gloss của file stove; cả 7 gloss đều dịch đúng (検札鋏 → "kìm soát vé", 蒸気機関車 → "đầu máy hơi nước", 喚呼 → "hô xác nhận"). Không tính sai.
- **っ cuối từ tại 1642, 1762, 2679** — っ gắn vào từ (ぬぐのっ, よいしょっ, ポーっ), bản Việt đã diễn đạt được độ nhấn/kéo dài; chỉ tiếng hít độc lập 1779 bị mất mới tính sai.
- **1829 "cô bé đó"** — chỉ đầu máy/toa xe được nhượng lại từ Tsuttetsu (Railord nữ), không phải gọi Paulette; không tính vào tally "cô"/"em".
- **2107 JP** — sạch trong cả CSV3 và TOML-2 (ruby [けんさつきょう,2]検札鋏 đầy đủ); ký tự lạ thấy trong một bản trích xuất làm việc trước đó chỉ là lỗi hiển thị, không có thật trong dữ liệu.
- **Ký tự lạ trong JP của CSV3 (2339)** — cột JP của CSV "Trang tính 3" hiển thị ký tự thay thế tại 2339 ("過保護"); đã đối chiếu ghi chú `# JP:` trong TOML-2 — sạch, không có ký tự lạ. Đây là lỗi hiển thị/mã hóa của CSV, không chạm tới bản Việt, không tính sai.

## Kết bài

解放b寝台 sai 48/421 dòng (11,4%) — file Paulette 02 thứ hai, và là phát hiện quan trọng nhất của đợt audit này: **tràn chương hai chiều đầu tiên của dự án (obasan ↔ sleeper, 19 dòng)**. Khác hai vụ tràn một chiều trước, 17/19 bản sửa khôi phục được ngay từ file obasan (bản dịch đúng đang nằm sai vị trí tại đó), chỉ 2 dòng phải dịch mới — và vì audit obasan đã liệt kê cả 17 key nguồn vào danh sách sai của nó, sửa hai file sẽ khớp nhau không xung đột. Ngoài tràn chương, file này còn lỗi hệ thống Soutetsu tự xưng "anh" (13 dòng, 0 lần "tôi") và nhầm 回数券 thành "vé tháng" (3 dòng). Áp khối TOML trên sẽ sửa hết 48 dòng; không còn dòng nào chưa chắc chắn trong file này. Mọi bản sửa đều đã qua vòng đọc lại lần hai đối chiếu JP (48/48 đúng, 0 bị loại). Điểm cần lưu ý: dòng 1627 ("Em có muốn lên trên không?") — người được hỏi chưa rõ là Paulette hay Hikari, đã giữ "em" theo cách đọc Paulette; nếu Hieu đọc cảnh này thấy Soutetsu đang hỏi Hikari thì đổi thành "Con có muốn lên trên không?". Bước tiếp theo: khi sửa file obasan và file này cùng lúc thì kiểm tra chéo 17 cặp key trong bảng tràn chương để đảm bảo hai file khớp nhau; sau đó tiếp tục audit các file Paulette còn lại theo thứ tự mức độ nghiêm trọng.

---
**Bổ sung 19/11 (quyết định B1 — Hieu):** dòng 1627 chuyển từ "không tính là sai" sang danh sách sửa: Soutetsu đang hỏi Hikari (1628 Paulette quay sang Hikari chuẩn bị cho con bé leo lên; 1633 Soutetsu lo "Tự con leo thang vẫn còn nguy hiểm lắm. Mà việc con ngủ một mình [trên giường trên]..."). Bản sửa: "Em có muốn lên trên không?" → "Con có muốn lên trên không?". Tally "em" của file: 13× → 12×; cộng dồn toàn dự án "em" 85 → 84 ("cô" giữ 48).

```toml
[script]
1627 = "「Sao đây? Con có muốn lên trên không?」"
```
