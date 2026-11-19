# Audit: Paulette 04_ヒヤリング — 7 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/ポーレット04_ヒヤリング.txt.toml` — 395 dòng script, **8 dòng Việt sai = 2,0%**, 0 dòng chưa chắc chắn.
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. Đây là file thứ 10 audit toàn bộ, sau 廃炭鉱 31%, obasan 56%, Grand 01 45,6%, Hibiki 03 86,2%, Hachiroku 13 夜の嵐 44,9%, 実りの秋 0,4%, Nagi_Fukami 08a 4,3%, Hachiroku 12 ムナカタ来訪 2,3%, 再開発 4,4% — **file sạch thứ hai từ trước tới nay** (chỉ sau 実りの秋 0,4%).

## Phương pháp và số liệu kiểm chứng
- Đã đọc **hết 395/395 dòng script** (key 1117–2603, không liên tục), đối chiếu từng dòng với JP + TW theo nghĩa, người nói, thoại/lời dẫn, xưng hô độc thoại theo quy ước của chính file. Không ngoại suy tổng dự án từ file này.
- Phân loại 8 dòng sai: **sai nghĩa 4** (1360 lệch thứ tự từ theo TW; 1607 汚名返上 dịch sai nghĩa; 2567 dấu phẩy kiểu MT làm câu gãy; 1132 — đã chốt, xem dưới), **xưng hô độc thoại 4** (2580, 2584, 2586, 2590: "mình" → "Tôi" trong suy nghĩ ngoặc của Soutetsu). Chưa dịch (còn nguyên tiếng Trung trong TOML) 0, cụt câu 0, không chắc chắn 0.
- Thoại sai 2/207 (1,0%); lời dẫn sai 5/188 (2,7%). Theo người nói: monologue 5, Paulette 2; Soutetsu thoại 0, Hibiki 0, Fukami 0, Miyamoto 0, Hachiroku 0, Nagi 0, Mayami 0, Reina 0.
- **Heuristic thoại/dẫn báo 1 dòng (2125) — đã xác minh là dương tính giả:** JP là lời dẫn có trích dẫn lồng trong ngoặc kép, VN dùng ngoặc đơn là đúng. Heuristic bắt được **0/7 lỗi thật**. Lỗi thật ở đây toàn là cùng loại (thoại→thoại sai nghĩa, dẫn→dẫn sai xưng hô) nên heuristic mù hoàn toàn.
- **Không có key-shift sạch:** test shift −5..+5 tốt nhất ở shift 0 (394/395 = 0,997). Không có bằng chứng lệch đều; lỗi xác nhận bằng đọc ngữ nghĩa từng dòng.
- **TOML và CSV giống hệt nhau về nội dung:** kiểm tra toàn bộ 395 dòng, 0 dòng khác nội dung thực (chỉ khác `\n`/khoảng trắng). Không có dòng CSV trống nào trong file này. VN==TW: 1 dòng 1160 là 「……」 — trùng hiển nhiên, không phải chưa dịch.
- **Không xét lỗi định dạng `\n`:** theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng, `\n` thủ công không quan trọng. Chỉ báo lỗi nội dung. Các bản sửa trong khối TOML bên dưới viết liền một dòng.
- **[selections]:** file có tiêu đề section `[selections]` nhưng **rỗng (0 mục)** — không có lựa chọn nào để kiểm tra hay sửa.
- **Thẻ `%l`:** không có lệch nào — JP có thẻ thì VN giữ đủ, VN không thêm thẻ nào JP thiếu.

## Kết luận về cơ chế lỗi
- File này **không bị xáo trộn cột Việt**: 0 dòng lệch vị trí, 0 dòng mồ côi, 0 dòng trùng lặp sai (2 cặp Việt trùng nhau đều là những câu cảm thán ngắn mà JP cũng giống hệt: 「Ồ.」 1463/1464, 「Ừm.」 1467/1494 — đều đúng).
- Ngược lại, **file này là NGUỒN của lỗi tràn chương**: 90 dòng Việt đúng ở đây đã bị copy sang file kề bên ポーレット04_鳴呼いきストーブ列車 (xem review stove) — và cả 90 dòng đó vẫn đứng đúng chỗ ở đây, không bị nhiễm ngược.
- Lỗi còn lại là lỗi dịch thuật lẻ tẻ ở mức câu/chữ/xưng hô, không phải lỗi hệ thống. JP và TW khớp nhau ở mọi dòng sai (trừ 1360, TW đảo thứ tự từ so với JP), nên mọi dòng sai đều sửa được chỉ bằng cách dịch lại/chuẩn hoá từ JP/TW, không cần thêm nguồn nào khác.
- 388 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Chi tiết 7 dòng sai

### A. Sai nghĩa (3 dòng)
- **1360** (Paulette): JP 「好き。違う……ん――……嫌い？　鉄道」 — Paulette nói "Thích" trước rồi mới sửa thành "Không…… Ghét?". TW đảo thứ tự thành 「不是，喜歡……嗯——……鐵路，討厭？」 và VN theo TW ("Không. Thích…… ưm——…… Ghét? Đường sắt."). Sửa theo JP: 「Thích. Không…… ưm——…… Ghét? Đường sắt.」
- **1607** (Paulette): JP 汚名返上はこれからだ — "Việc lấy lại danh dự mới bắt đầu từ đây." VN cũ "Vì vậy, từ giờ trở đi, em sẽ rửa sạch cái danh tiếng đó" sai nghĩa: 汚名 là danh xấu/ô danh cần gỡ bỏ, 返上 là lấy lại/khôi phục — "rửa sạch cái danh tiếng" vừa dùng sai từ (danh tiếng chung chung thay vì ô danh) vừa ngược sắc thái. Sửa: 「Việc lấy lại danh dự mới bắt đầu từ đây.」
- **2567** (monologue, suy nghĩ trong ngoặc): JP （だめ、だ――そんな、こと） — VN cũ "（Không, được——chuyện, đó）" là dấu phẩy kiểu MT: cắt câu thành mảnh vô nghĩa, đọc không hiểu. Sửa: （Không được rồi——chuyện đó）.

### B. Xưng hô độc thoại không nhất quán (4 dòng)
- **2580, 2584, 2586, 2590** (monologue, suy nghĩ trong ngoặc （...） của Soutetsu): cả 4 dòng dùng "mình" làm chủ ngữ, trong khi quy ước của file là "Tôi" — độc thoại Soutetsu dùng "Tôi" ở mọi chỗ khác, kể cả một suy nghĩ ngoặc khác ở 2596 ("thời gian tôi và Paulette ở riêng với nhau khá nhiều nhỉ."). Chuẩn hoá về "Tôi" theo docs (Soutetsu xưng "Tôi", locations §2.1) và quy ước của chính file. Các lần "mình" còn lại trong file đều KHÔNG phải đại từ chủ ngữ: "của mình" (1135, sở hữu), "giấc mơ mình vừa thấy" (2151, mệnh đề quan hệ), "mình vừa nhớ ra" (2247), "không biết mình có thể khẳng định" (2248), "tấm lòng của mình" (2335, sở hữu), "than mình đào được" (2385, cách nói chung) — đều là cách dùng tự nhiên trong tiếng Việt, không tính lỗi.

## Các cặp trùng lặp / lệch vị trí đã xác nhận
- **0 cặp trong file.** 2 cặp Việt trùng nhau (「Ồ.」 1463/1464, 「Ừm.」 1467/1494) đều là cảm thán ngắn mà JP cũng giống hệt — không phải lỗi.
- Ngược lại: file này là nguồn của **90 dòng copy sang file stove** — danh sách đầy đủ 90 cặp ở review `audit-paulette04-stove-train-REVIEW.md`.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- Soutetsu độc thoại xưng "Tôi" (quy ước file + docs locations §2.1); Paulette xưng "Tôi"/"Em" theo ngữ cảnh; Hachiroku gọi Soutetsu "Ngài Soutetsu"; Hibiki gọi "Anh hai"/"Anh trai"; Reina gọi "Anh Soutetsu"; Mayami xưng "Chị", gọi Soutetsu "Em trai"/"Sou-chan".
- 御一夜: các dòng đúng trong file dùng "Ohimitera" 5 lần, "Ohito" 1 lần — **chưa chốt** (Ohito/Ohimitera/Ohitoyo); không đổi trong khối sửa. 湯医 → "Yui" (2 dòng đúng: 2023, 2532) — trái với "Yunoi" ở Grand 01/Hibiki 03, **vẫn chờ Hieu chốt**. 帝鉄 không xuất hiện trong file. エアクラ = "Aircra" (2074 giữ đúng). 汚名返上 = "lấy lại danh dự" (1607).
- Còi tàu ポー không xuất hiện trong file này. Trailing "——っ" giữ nguyên theo sfx §3.

## Dòng đã chốt sau audit (1 dòng — chốt ngày 19/11 từ cột Character + ngữ cảnh)
- **1132** (monologue): JP なっていない (mảnh câu, không có chủ ngữ) vs TW 沒有. Cột Character ghi "monologue"; các dòng độc thoại xung quanh (1120, 1122) dùng 僕 — đây là độc thoại của Soutetsu nhớ lại lời ông Taito (cứu người khác mới là đền đáp vì đã không cứu được Michiko), rồi tới 1135 (tour sông Kuma vẫn cần cải thiện điểm đó). Chủ ngữ của なっていない không phải là người mà là tình trạng chung — "vẫn chưa thành (như vậy)". VN cũ "Tôi không hề." sai hai chỗ: tự thêm chủ ngữ "Tôi" và đọc thành phủ định hành động ("tôi không hề làm"). Bản sửa: `1132 = "Vẫn chưa được."` — đã đưa vào khối TOML (khối giờ 8 key). (Lưu ý: chính câu "Tôi không hề." này cũng bị copy sang file stove key 1790, đã sửa ở đó thành câu cười đúng của nó.)

## Đề xuất cập nhật context (để Hieu quyết, KHÔNG tự đổi toàn dự án)
- Không có đề xuất mới từ file này. Các quyết định đang chờ (御一夜, 湯医, 帝鉄…) vẫn giữ nguyên; file này dùng "Ohimitera" (5/6) và "Yui" (2/2) ở các dòng đúng — ghi nhận để Hieu quyết một dạng thống nhất.

## Giới hạn của audit này
- Đã đọc hết 395 dòng script của file này: 8 dòng sai đã xác nhận, 0 dòng chưa chắc chắn, 387 dòng còn lại khớp JP/TW.
- Vẫn có thể sót vài dòng "trông hợp lý nhưng thực ra là bản dịch của dòng khác" — cách chắc chắn nhất vẫn là chơi qua chương và đối chiếu voice. Nếu Hieu gặp thêm dòng nào nghi ngờ trong file này thì gửi mình, mình kiểm tra nốt.
- Tổng 10 file đã audit xong: 133 + 255 + 299 + 374 + 199 + 2 + 20 + 12 + 19 + 8 = **1.321 dòng sai**.

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)
Lưu ý khi chép: các bản sửa viết liền một dòng, không chèn `\n` thủ công — theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng. Khối này đã kiểm tra bằng máy: trích khối từ chính file review, parse bằng tomllib — **8/8 key** khớp đúng tập dòng sai, không thừa không thiếu, giá trị sau khi parse khớp đúng bản sửa.

```toml
1132 = "Vẫn chưa được."
1360 = "「Thích. Không…… ưm——…… Ghét? Đường sắt.」"
1607 = "「Việc lấy lại danh dự mới bắt đầu từ đây.」"
2567 = "（Không được rồi——chuyện đó）"
2580 = "（À, đúng rồi——chắc chắn là tôi 『làm được』.）"
2584 = "（Nếu tôi…… cứ thế này bị cán qua thì——）"
2586 = "（Tôi đã chấp nhận. Tôi đã hiểu rồi. Đó là lý do tại sao, tôi——）"
2590 = "（Gửi cho tôi sao.）"
```

## Việc tiếp theo
1. Áp dụng khối TOML trên cho file Paulette 04_ヒヤリング (8 dòng), chơi thử chương rồi báo lại.
2. Xem review file kề bên — ポーレット04_鳴呼いきストーブ列車 bị tràn 90 dòng từ chính file này.
3. Xuất lại CSV mới từ TOML (sau khi áp fix) để CSV không còn cũ — với CSV3 thì chỉ còn 2 dòng lẻ chưa dịch (lr真闇追加01/02) là cần dịch mới; 144/146 dòng chưa dịch đã có bản dịch trong các khối audit (Grand 01: 100, Hibiki 03: 44).

## Kết bài
Paulette 04_ヒヤリング là file thứ mười được audit toàn bộ, và là file sạch thứ hai toàn dự án (2,0% sai, chỉ sau 実りの秋 0,4%): không bị xáo trộn cột Việt, không có dòng chưa dịch, không có dòng mồ côi hay tràn từ chương khác — 8 lỗi còn lại chỉ là 4 chỗ sai nghĩa lẻ tẻ và 4 chỗ xưng hô "mình"/"Tôi" trong suy nghĩ ngoặc của Soutetsu. Quan trọng hơn, file này trả lời câu hỏi đã đặt ra từ chẩn đoán ban đầu của Paulette 04: **cột Việt của hearing không bị nhiễm, mà chính nó là nguồn tràn** — chiều tràn chỉ đi một chiều, từ hearing sang stove, và 90 câu Việt bị copy sang đó đều đang đứng đúng chỗ ở đây.

Việc còn lại của riêng file này chỉ là áp dụng khối TOML 8 dòng rồi chơi thử chương để nghiệm thu. Còn về tổng thể dự án, mười file đã audit xong đã có 1.321 dòng sai — và việc hai file cùng một chương 04 mà một file sạch (2,0%) một file nặng (22,1%, xem review stove) cho thấy không thể đoán độ sạch từ tên chương hay file bên cạnh; vẫn phải đọc hết từng dòng.
