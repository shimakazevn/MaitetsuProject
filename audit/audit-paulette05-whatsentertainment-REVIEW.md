# Audit: Paulette 05_whatsentertainment — 10 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/ポーレット05_whatsentertainment.txt.toml` — 362 dòng script, **10 dòng Việt sai = 2,8%**, 0 dòng chưa chắc chắn.
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. Đây là file thứ 12 audit toàn bộ, sau 廃炭鉱 31%, obasan 56%, Grand 01 45,6%, Hibiki 03 86,2%, Hachiroku 13 夜の嵐 44,9%, 実りの秋 0,4%, Nagi_Fukami 08a 4,3%, Hachiroku 12 ムナカタ来訪 2,3%, 再開発 4,4%, Paulette 04_ヒヤリング 1,8%, stove 22,1% — **file sạch thứ tư từ trước tới nay** (sau 実りの秋 0,4%, ヒヤリング 1,8% và ムナカタ来訪 2,3%).

## Phương pháp và số liệu kiểm chứng
- Đã đọc **hết 362/362 dòng script** (key 952–2297, không liên tục), đối chiếu từng dòng với JP + TW theo nghĩa, người nói, thoại/lời dẫn, xưng hô độc thoại theo quy ước của chính file. Không ngoại suy tổng dự án từ file này.
- Phân loại 10 dòng sai: **xưng hô (pronoun) 4** (1390, 1418, 2034, 2286 — Soutetsu xưng "mình" thay vì "Tôi"), **sai nghĩa 2** (1296, 1952 — gọi nhầm giới tính "anh Miyamoto"), **lỗi nhỏ 2** (1346, 1534 — dấu "Ạ." đứng riêng câu), **thuật ngữ 2** (1490, 1903 — "Ohimitera" theo quyết định mới phải đổi thành "Ohitoyo"). Lệch vị trí 0, chưa dịch 0, cụt câu 0, không chắc chắn 0.
- Thoại sai 6/202 (3,0%); lời dẫn (monologue) sai 4/160 (2,5%). Theo người nói: monologue 4, Paulette 2, Fukami 2, Soutetsu 2; Hachiroku, Reina, Nagi 0.
- **Heuristic thoại/dẫn báo 0 dòng** — bắt được **0/10 dòng sai**: toàn bộ lỗi ở đây đều cùng loại (thoại→thoại, dẫn→dẫn) hoặc ở mức từ/câu, những lỗi heuristic không thể thấy. Đây là minh chứng nữa rằng heuristic chỉ là giới hạn dưới.
- **Không có key-shift sạch:** test shift −5..+5 tốt nhất ở shift 0 (362/362 = 1,000). Không có bằng chứng lệch đều; lỗi xác nhận bằng đọc ngữ nghĩa từng dòng + đối chiếu chỉ mục Việt toàn dự án.
- **TOML và CSV giống hệt nhau về nội dung:** kiểm tra toàn bộ 362 dòng, 0 dòng khác nội dung thực (210 dòng chỉ khác `\n`/khoảng trắng). Không có dòng CSV trống nào trong file này. VN==TW: 0 dòng.
- **Không xét lỗi định dạng `\n`:** theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng, `\n` thủ công không quan trọng. Chỉ báo lỗi nội dung. Các bản sửa trong khối TOML bên dưới viết liền một dòng.
- **[selections]:** file có tiêu đề section `[selections]` nhưng **rỗng (0 mục)** — không có lựa chọn nào để kiểm tra hay sửa.
- **Thẻ `%l`:** không có dòng nào VN thêm/thiếu thẻ so với JP. Thẻ エアクラ ở 1974 ("Aircra") và 焼なまし ở 2257 ("ủ mềm thép") đều giữ đúng. Dấu gạch —— trong bản sửa viết không khoảng trắng hai bên, theo quy ước dự án (22.055 dòng).

## Kết luận về cơ chế lỗi
- **Không có lệch vị trí trong file này:** không dòng mồ côi, không cặp chuyển chỗ, không tràn từ chương khác. 2 cặp Việt trùng nhau trong file đều đúng: 「Hửm?」 1313/1336 (JP cả hai chỗ đều là 「ふむ？」/「ん？」) và （Keng! Keng! Keng! Keng!） 2279/2282 (cùng là tiếng búa đập, JP/TW khác nhau đôi chút nhưng cùng một hiệu ứng âm thanh — giữ nguyên).
- Lỗi còn lại chỉ ở mức câu/chữ: 4 chỗ Soutetsu xưng "mình", 2 chỗ gọi nhầm giới tính, 2 chỗ dấu câu rời rạc, 2 chỗ thuật ngữ theo quyết định mới. File này sạch theo đúng nghĩa — không phải do heuristic bỏ sót ít, mà do cột Việt thực sự ít lỗi.
- 352 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Chi tiết 10 dòng sai

### A. Sai giới tính cách gọi — "anh Miyamoto" (2 dòng)
TW xác nhận ở cả hai chỗ 宮本 là nữ (宮本女士). JP 宮本さん đứng một mình không rõ giới tính, nhưng TW là chứng thứ hai rõ ràng, nên "Anh Miyamoto" là sai.
- **1296** (Paulette): JP 「え？　宮本さん？　あ、ごめんなさいっ！」 / TW 「哎？　宮本女士？啊，不好意思！」 — VN cũ "Hả? Anh Miyamoto? A, cháu xin lỗi!" → sửa thành "Hả? Cô Miyamoto? A, cháu xin lỗi!" (Paulette tự xưng "cháu" với người này nên dùng "Cô" — phụ nữ lớn tuổi).
- **1952** (monologue): JP 「宮本さん、からといっていた。ならば恐らく、非常――緊急用の着信音であるのだろう。」 / TW 「她說是宮本女士打來的。那麼這恐怕就是所謂的緊急鈴聲吧。」 — VN cũ "Cô ấy nói là từ anh Miyamoto. Nếu vậy thì có lẽ đó là nhạc chuông dùng cho trường hợp khẩn cấp——bất thường." → sửa thành "Cô ấy nói là từ cô Miyamoto. Nếu vậy thì có lẽ đó là nhạc chuông dùng cho trường hợp khẩn cấp đặc biệt." ("bất thường" cũng dịch 非常 lệch — 非常 ở đây là "đặc biệt", bổ nghĩa cho chuông khẩn cấp.)

### B. Soutetsu xưng "mình" thay vì "Tôi" (4 dòng)
Quy ước file + docs (locations §2.1): Soutetsu xưng "Tôi". Các dòng dưới đây dùng "mình" làm chủ ngữ (kể cả trong mệnh đề phụ và trong ngoặc suy nghĩ), lẫn với "Tôi" ở cùng câu/cùng file — cùng mẫu lỗi đã thấy ở pilot và ở Paulette 04_ヒヤリング (4 dòng). Các "mình" khác trong file đều không phải lỗi: thành ngữ ("một mình", "chính mình", "giật mình", "tự mình"), sở hữu ("vợ mình", "ghế của mình"), hoặc trong trích dẫn nội tâm có dấu ngoặc kép (2051 "mình không hề ở một mình" — giữ nguyên, "mình" trong ngoặc kép là giọng nội tâm tự nhiên).
- **1390** (Soutetsu): JP 「恐らく僕は、いささか遊びと離れすぎた。幼少期には、目一杯楽しんでいた気もするのだが」 — VN cũ "Có lẽ tôi đã rời xa việc vui chơi hơi lâu rồi. Dù tôi nhớ hồi nhỏ mình cũng từng chơi đùa thỏa thích." → "Dù tôi nhớ hồi nhỏ tôi cũng từng chơi đùa thỏa thích."
- **1418** (Soutetsu, tự nói với mình): JP 「信じるんだ。僕が感じた楽しさを。それをもう一度味わうために、何をしたいか考えるんだ」 — VN cũ "Phải tin tưởng. Vào niềm vui mà mình đã cảm nhận được. Để có thể nếm trải nó một lần nữa, hãy suy nghĩ xem mình muốn làm gì." → "Vào niềm vui mà tôi đã cảm nhận được. […] hãy suy nghĩ xem tôi muốn làm gì."
- **2034** (monologue): JP 「すっと一本、光の道が――進むべき道が、目の前に示されたような気になる。」 — VN cũ "Một con đường ánh sáng vụt hiện ra——Tôi có cảm giác như con đường mình nên đi đã được mở ra ngay trước mắt." → "con đường tôi nên đi".
- **2286** (monologue, ngoặc suy nghĩ): JP 「（いや、バカか僕は――“人間関係にも”と、自分で思ったばかりではないか）」 — VN cũ "（Không, mình là đồ ngốc sao——Chẳng phải mình vừa mới nghĩ "cũng áp dụng cho cả các mối quan hệ con người" sao）" → "（Không, tôi là đồ ngốc sao——Chẳng phải tôi vừa mới nghĩ "cũng áp dụng cho cả các mối quan hệ con người" sao）".

### C. Dấu "Ạ." đứng riêng một câu (2 dòng)
Cả hai đều là Fukami (です cuối câu bị tách thành một câu riêng "Ạ." — rời rạc, không tự nhiên). Gộp vào cuối câu trước.
- **1346** (Fukami): JP 「お二人なら、船酔いの心配はないですから。です」 — VN cũ "Vì là hai người, nên không phải lo chuyện say sóng đâu. Ạ." → "Vì là hai người, nên không phải lo chuyện say sóng đâu ạ."
- **1534** (Fukami): JP 「それなら、頑張った甲斐がありました。です」 — VN cũ "Nếu vậy thì, bõ công em cố gắng rồi. Ạ." → "Nếu vậy thì, bõ công em cố gắng rồi ạ."

### D. Thuật ngữ theo quyết định mới — 御一夜 = "Ohitoyo" (2 dòng)
**Quyết định 19/11 của Hieu: 御一夜 = "Ohitoyo"** (8/8 ở Hachiroku 12 再開発 + furigana おひとよ). Đây là 2 dòng duy nhất trong file có 御一夜 — cả hai đều đang dùng "Ohimitera" theo docs cũ, cần đổi để thống nhất. Sau khi áp dụng, file này không còn "Ohimitera" nào.
- **1490** (Paulette): JP 「観光振興のために、御一夜市内で人気あるスポットとか、イベントとかそういうのです」 — "thành phố Ohimitera" → "thành phố Ohitoyo".
- **1903** (monologue): JP 「廃鉱山を、御一夜を、そういう場所にしていけばいい。」 — "biến Ohimitera thành một nơi như vậy" → "biến Ohitoyo thành một nơi như vậy".

## Các cặp trùng lặp / lệch vị trí đã xác nhận
- **0 cặp chuyển chỗ, 0 dòng mồ côi, 0 tràn chương.** Không dòng Việt nào trong file khớp với key khác trong dự án ngoài 2 cặp trùng đúng đã nêu ở trên (1313/1336, 2279/2282).
- **0 bản sửa khôi phục được từ trong file** — không phải vì lỗi lệch, mà vì không có dòng nào lệch; các bản sửa đều là sửa chữ/nghĩa tại chỗ.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- Soutetsu độc thoại xưng "Tôi" (quy ước file + docs locations §2.1); khi nói với ông Minokasa xưng "cháu" + "ạ" (1400, 1414 — đúng, giữ nguyên); khi nói với Paulette xưng "anh" (1290 — đúng theo quy ước route, giữ nguyên). Paulette xưng "Tôi", gọi Soutetsu "anh Soutetsu"; Hachiroku gọi Soutetsu "Ngài Soutetsu"; Reina gọi Soutetsu "Anh Soutetsu"; Fukami xưng "Em".
- 御一夜 → **"Ohitoyo"** trong các bản sửa (1490, 1903) — **quyết định 19/11 của Hieu**.
- エアクラ = "Aircra" (1974, đúng sẵn có — không đổi thành "Aircraft"); 宗谷太郎 = "Soya Tarou" (962, 990 — theo ruby [そうや,1]宗谷); 相楽村 = "làng Sagara" (1323); 赤井阿蘇神社 = "đền Akai Aso" (1982, 2223); 隈元 = "Kuma" trong "sông Kuma" (1501, 1963); 湯医, 帝鉄, 冥国, 冥軍, 小畑, 大畑 không xuất hiện trong file này.
- かまくま không xuất hiện trong file này. Còi tàu ポー không xuất hiện trong file này.

## Đề xuất context mới
- Không có đề xuất mới từ file này. Lưu ý: lỗi "Ạ." rời rạc ở 1346/1534 cùng một mẫu (Fukami, です cuối câu) — nếu các file khác cũng có mẫu này thì đáng sửa hàng loạt khi tới lượt, không cần quyết định riêng.

## Dòng chưa chắc chắn
- Không có dòng nào chưa chắc chắn trong file này.

## Khối TOML sửa (10 dòng — đã kiểm tra parse bằng tomllib, đúng 10/10 key, giá trị khớp JSON)
```toml
1296 = "「Hả? Cô Miyamoto? A, cháu xin lỗi!」"
1346 = "「Vì là hai người, nên không phải lo chuyện say sóng đâu ạ.」"
1390 = "「Có lẽ tôi đã rời xa việc vui chơi hơi lâu rồi. Dù tôi nhớ hồi nhỏ tôi cũng từng chơi đùa thỏa thích.」"
1418 = "「Phải tin tưởng. Vào niềm vui mà tôi đã cảm nhận được. Để có thể nếm trải nó một lần nữa, hãy suy nghĩ xem tôi muốn làm gì.」"
1490 = "「Để xúc tiến du lịch, tôi đã tìm hiểu về những địa điểm nổi tiếng trong thành phố Ohitoyo, các sự kiện và những thứ tương tự.」"
1534 = "「Nếu vậy thì, bõ công em cố gắng rồi ạ.」"
1903 = "Hãy biến khu mỏ bỏ hoang, biến Ohitoyo thành một nơi như vậy. Để làm được điều đó, chỉ cần suy nghĩ từng việc một là được."
1952 = "Cô ấy nói là từ cô Miyamoto. Nếu vậy thì có lẽ đó là nhạc chuông dùng cho trường hợp khẩn cấp đặc biệt."
2034 = "Một con đường ánh sáng vụt hiện ra——Tôi có cảm giác như con đường tôi nên đi đã được mở ra ngay trước mắt."
2286 = "（Không, tôi là đồ ngốc sao——Chẳng phải tôi vừa mới nghĩ \"cũng áp dụng cho cả các mối quan hệ con người\" sao）"
```

## Kết bài
Paulette 05_whatsentertainment là file thứ mười hai được audit toàn bộ, và là file sạch thứ tư toàn dự án (2,8% sai, chỉ sau 実りの秋 0,4%, ヒヤリング 1,8% và ムナカタ来訪 2,3%): không bị xáo trộn cột Việt, không có dòng chưa dịch, không có dòng mồ côi hay tràn từ chương khác — 10 lỗi còn lại chỉ là những sai sót lẻ tẻ ở mức câu/chữ/xưng hô (4 chỗ Soutetsu xưng "mình", 2 chỗ gọi nhầm giới tính, 2 chỗ dấu câu, 2 chỗ thuật ngữ theo quyết định mới). Heuristic báo 0 dòng ở file này — bằng chứng rõ nhất rằng heuristic không thể thay thế việc đọc từng dòng.

Việc còn lại của riêng file này chỉ là áp dụng khối TOML 10 dòng và chơi thử chương để nghiệm thu (không có dòng nào chưa chắc chắn). Còn về tổng thể dự án, mười ba file đã audit xong đã có 1.454 dòng sai (tính cả file 鳴呼の町 23 dòng, xem review riêng) — và việc hai file Paulette 05 trái ngược nhau (file này 2,8%, file 鳴呼の町 5,0%) cho thấy không thể đoán độ sạch của một file từ tên chương hay file bên cạnh; vẫn phải đọc hết từng dòng.
