# Audit: Paulette 04_鳴呼いきストーブ列車 — 101 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/ポーレット04_鳴呼いきストーブ列車.txt.toml` — 457 dòng script, **101 dòng Việt sai = 22,1%**, 0 dòng chưa chắc chắn.
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. Đây là file thứ 11 audit toàn bộ, sau 廃炭鉱 31%, obasan 56%, Grand 01 45,6%, Hibiki 03 86,2%, Hachiroku 13 夜の嵐 44,9%, 実りの秋 0,4%, Nagi_Fukami 08a 4,3%, Hachiroku 12 ムナカタ来訪 2,3%, 再開発 4,4%, Paulette 04_ヒヤリング 1,8% — **file nặng thứ sáu từ trước tới nay** (sau Hibiki 03 86,2%, obasan 56%, Grand 01 45,6%, 夜の嵐 44,9%, 廃炭鉱 31%).

## Phương pháp và số liệu kiểm chứng
- Đã đọc **hết 457/457 dòng script** (key 1249–2853, không liên tục), đối chiếu từng dòng với JP + TW theo nghĩa, người nói, thoại/lời dẫn, xưng hô độc thoại theo quy ước của chính file. Không ngoại suy tổng dự án từ file này.
- Phân loại 101 dòng sai: **lệch vị trí 99** (90 copy từ file hearing kề bên + 1 dòng nguồn không xác định được duy nhất 2252 + 7 mảnh vỡ mồ côi + 1 trùng lặp nội bộ 2140←2104), **lỗi gloss 2** (2076, 2642: タブレット → "Thẻ bảng"). Chưa dịch (còn nguyên tiếng Trung trong TOML) 0, cụt câu 0, không chắc chắn 0.
- Lời dẫn (monologue, theo cột Character) sai 35/144 (24,3%); thoại sai 66/313 (21,1%). Theo người nói: monologue 35, Soutetsu 24, Hikari 21, Paulette 16, Reina 3, bà cụ 2; Tourist Association, Passenger C/D, Conductor, Station staff 0.
- Phân bố lỗi theo đoạn: key 1249–1825: 25 dòng; 1827–2013: 22 dòng; 2014–2235: 18 dòng; 2238–2671: 26 dòng; 2672–2853: 10 dòng — lỗi rải đều cả file, không tập trung một cảnh.
- **Heuristic thoại/dẫn báo 48 dòng** (toàn bộ là JP thoại/VN dẫn) — bắt được tối đa 48/101 dòng sai, sót ít nhất 53 dòng (52,5%): toàn bộ là các dòng copy cùng loại (thoại→thoại, dẫn→dẫn), lỗi gloss và mảnh vỡ — những lỗi heuristic không thể thấy. Đây là minh chứng nữa rằng heuristic chỉ là giới hạn dưới.
- **Không có key-shift sạch:** test shift −5..+5 tốt nhất ở shift 0 (409/457 = 0,895). Không có bằng chứng lệch đều; lỗi xác nhận bằng đọc ngữ nghĩa từng dòng + đối chiếu chỉ mục Việt toàn dự án.
- **TOML và CSV giống hệt nhau về nội dung:** kiểm tra toàn bộ 457 dòng, 0 dòng khác nội dung thực (chỉ khác `\n`/khoảng trắng). Không có dòng CSV trống nào trong file này. VN==TW: 0 dòng.
- **Không xét lỗi định dạng `\n`:** theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng, `\n` thủ công không quan trọng. Chỉ báo lỗi nội dung. Các bản sửa trong khối TOML bên dưới viết liền một dòng.
- **[selections]:** file có tiêu đề section `[selections]` nhưng **rỗng (0 mục)** — không có lựa chọn nào để kiểm tra hay sửa.
- **Thẻ `%l`:** VN thêm thẻ gloss ở 7 dòng mà JP gốc không có thẻ (1780 接続, 1811 車販, 2028 車掌, 2050 車掌, 2076 タブレット, 2698 接続, 2816 車販) — bản dịch vẫn đúng nghĩa, chỉ thêm thẻ; ghi như một quan sát hệ thống, **KHÔNG tính là lỗi** (trừ 2076: gloss trong thẻ sai, đã tính là lỗi; và 2028: bản thân dòng đã sai do copy). Không có dòng nào VN làm mất thẻ `%l` của JP. Xem đề xuất context số 2.

## Kết luận về cơ chế lỗi
- **Tràn chương từ file kề bên hearing → stove: 90 dòng (19,7% cả file).** Đây là trường hợp tràn chương thứ hai trong dự án, sau Hachiroku 12 → 夜の嵐 (32 dòng) — nhưng khác ở chỗ hai file này cùng một chương số 04 trong cùng route Paulette, và quy mô lớn hơn gần gấp ba. Chiều tràn chỉ đi một chiều: file hearing sạch (1,8% sai) và cả 90 câu đều dịch đúng JP tại key gốc ở đó; không có tràn ngược vào hearing.
- Cơ chế giống hệt các file nặng trước: cột Việt bị dán nhầm theo từng dòng rời rạc (không có key-shift sạch), có cả thoại→thoại, dẫn→dẫn, thoại→dẫn và dẫn→thoại — nên heuristic chỉ thấy được một phần.
- **7 mảnh vỡ mồ côi** (1816, 1887, 1922, 2014, 2020, 2518, 2536): những mảnh câu ngắn ("Không——", "Nhưng mà——", "Ừm!", "Hibiki.", "Này nhé.", "Ồ.", "Ư, ừm.") không khớp dòng nào trong toàn dự án (kiểm tra qua chỉ mục Việt 81.202 mục) — khả năng cao là phần còn sót của những dòng copy bị cắt cụt; bản dịch đúng phải viết mới hoàn toàn.
- **1 trùng lặp nội bộ** (2140 ← 2104): câu thông báo ga của nhân viên ga bị dán đè lên câu cảm ơn của Paulette; chỉ 2104 đúng.
- **1 dòng nguồn không xác định được duy nhất** (2252 "Anh Soutetsu."): câu ngắn thông dụng xuất hiện ở 12 file trong dự án (trong đó có hearing key 1822) — không truy vết được một nguồn duy nhất, nhưng chắc chắn không phải bản dịch của JP ở đây (Reina hỏi "có nặng không?").
- **2 lỗi gloss** (2076, 2642): タブレット (máy tính bảng) bị ghi gloss thành "Thẻ bảng" — cùng một lỗi ở hai chỗ.
- **0/101 bản sửa khôi phục được trong file:** không có cặp chuyển chỗ nội bộ nào (không dòng nào mà bản dịch đúng của nó đang nằm ở key khác trong cùng file) — mọi dòng sai đều phải dịch mới từ JP/TW. JP và TW khớp nhau ở mọi dòng sai, nên không cần thêm nguồn nào khác.
- 356 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Chi tiết 101 dòng sai

### A. Copy từ file hearing kề bên (90 dòng)
Mỗi dòng dưới đây, bản Việt cũ là bản dịch đúng của key hearing ghi sau mũi tên — đã xác minh bằng chỉ mục Việt toàn dự án (khớp chính xác từng ký tự, kể cả `\n`). Chi tiết đầy đủ từng dòng (JP/TW/VN cũ/bản sửa) ở file JSON `audit-paulette04-stove-train-wrong.json`.
- 1251←2381, 1297←1755, 1299←2116, 1300←2281, 1670←1493, 1671←1415, 1673←2141, 1675←2159, 1687←1745, 1703←1135, 1712←2295, 1728←1401, 1729←1712, 1734←2420, 1753←1586, 1760←1365, 1763←2004, 1769←2177, 1771←1727, 1787←2137, 1790←1132, 1803←1585, 1813←1607, 1821←2392
- 1834←1801, 1841←2385, 1847←2268, 1861←2079, 1863←1517, 1866←1460, 1867←1687, 1870←1566, 1888←2162, 1913←2468, 1917←1400, 1931←2271, 1944←2176, 1945←2589, 1952←1987, 1979←1139, 1990←2052, 1998←1399, 2004←1358, 2012←1462
- 2028←1620, 2049←2387, 2057←1569, 2071←2601, 2074←1795, 2078←2124, 2087←2503, 2101←2465, 2181←1478, 2185←1483, 2205←2198, 2211←1377, 2214←2007, 2228←2516
- 2247←2294, 2470←2364, 2472←1547, 2485←1147, 2490←2335, 2496←2596, 2503←2125, 2512←1775, 2542←1791, 2544←1581, 2555←1999, 2562←2534, 2583←2021, 2589←1589, 2614←1430, 2616←2336, 2621←1992, 2630←1647, 2647←1709, 2648←1520, 2653←1479, 2671←2379
- 2673←2248, 2676←1997, 2681←2348, 2696←1679, 2728←1692, 2745←2238, 2747←1515, 2792←2164, 2808←1741, 2840←1506

Một vài ví dụ điển hình (đọc để thấy rõ kiểu lỗi):
- **1251** (monologue): JP là lời dẫn về bà cụ đã cho táo ("――リンゴをくださった、あのおばあさんだ。ご当人からのアドバイスに気を配りつつ、言葉を選ぶ。") nhưng VN cũ là câu dẫn của hearing 2381 ("Sau đó em ấy từ từ mở mắt ra và nhìn tôi.").
- **1297** (Paulette): JP 「……すごくなんてないです。全然」 ("Em chẳng tuyệt vời gì đâu") nhưng VN cũ là câu của hearing 1755 về "Tài trợ và tuyên truyền… mô hình win-win".
- **2490** (monologue): JP là Hikari ôm chầm lấy Paulette rồi ôm chặt Soutetsu, nhưng VN cũ là câu của hearing 2335 ("Hibiki đang hướng tấm lòng của mình về phía chúng tôi.").
- **2673** (monologue): JP là Paulette đặt Hikari xuống ghế với nụ cười tự hào, nhưng VN cũ là câu của hearing 2248 ("Nhưng tôi lại băn khoăn không biết mình có thể khẳng định chắc nịch như vậy không.").
- **2181** (Soutetsu): VN cũ "À, không có gì——" trùng cả hearing 1478 lẫn Paulette 07_うさぎ 1955 — hai nguồn có thể, nhưng hearing là file kề bên nên khả năng cao nhất; JP ở đây là 「投炭1000杯の方が重いさ」 ("Xúc 1000 xẻng than vẫn nặng hơn.").
- **1813** (Reina): VN cũ là câu của hearing 1607 — mà chính 1607 ở hearing cũng là một dòng sai (汚名返上, xem review hearing): lỗi chồng lên lỗi, copy cả bản dịch sai sang file này.

### B. Mảnh vỡ mồ côi (7 dòng)
- **1816** (Reina): JP 「わあああ、すっごくいい席ですねぇ！」 ("Chỗ ngồi này tuyệt quá!") — VN cũ chỉ còn 「Không——」.
- **1887** (Hikari): JP 「えへへへ～！」 — VN cũ chỉ còn "Nhưng mà——".
- **1922** (Hikari): JP 「あったかいのー」 ("Ấm quá đi~") — VN cũ chỉ còn 「Ừm!」.
- **2014** (Soutetsu): JP là lời dẫn dài về việc nghĩ tới Hikari từ trước khi con bé ra đời — VN cũ chỉ còn 「Hibiki.」.
- **2020** (Paulette): JP là câu dài về việc nhờ bạn bè maitetsu xếp hàng mua vé hộ — VN cũ chỉ còn 「Này nhé.」.
- **2518** (monologue): JP là câu dài về Paulette nói "Sẽ mua" — VN cũ chỉ còn 「Ồ.」.
- **2536** (monologue): JP là câu về ngồi xuống gần lò sưởi — VN cũ chỉ còn "Ư, ừm.".
- Cả 7 mảnh đều không khớp dòng nào trong toàn dự án (chỉ mục Việt 81.202 mục) — quá ngắn để truy vết chắc chắn, nhưng chắc chắn không phải bản dịch của JP ở đây. Bản sửa viết mới hoàn toàn từ JP/TW.

### C. Trùng lặp nội bộ (1 dòng)
- **2140** (Paulette): JP 「本当に、ありがとうございました」 ("Thật sự cảm ơn rất nhiều ạ.") — VN cũ trùng y hệt key 2104 trong cùng file (câu thông báo "Đường sắt Yukemuri, toa xe sưởi ấm đi Naruko đang ở tuyến số 2!…"). Chỉ 2104 đúng; 2140 sửa mới.

### D. Nguồn không xác định được duy nhất (1 dòng)
- **2252** (Reina): JP 「双鉄さぁん、おもくないですかぁ」 ("Anh Soutetsu ơi, như vậy có nặng không ạ~") — VN cũ "Anh Soutetsu." là câu ngắn thông dụng xuất hiện ở 12 file trong dự án (trong đó có hearing key 1822). Không truy vết được một nguồn duy nhất.

### E. Lỗi gloss (2 dòng)
- **2076** (Hikari): JP 「よめるのー！　たぶれっと！！」 — thẻ `%l` cho タブレット ghi gloss "Thẻ bảng" (sai: タブレット ở đây là máy tính bảng mà Hikari đang đọc). Sửa gloss thành "máy tính bảng", giữ nguyên cấu trúc thẻ.
- **2642** (monologue): JP タブレット、エクスプレスは読めるのに、『ブレスレット』は読めない。 — cùng lỗi: "Đọc được Thẻ bảng, Express…" → sửa thành "Đọc được máy tính bảng, Express…".

## Các cặp trùng lặp / lệch vị trí đã xác nhận
- **90 cặp hearing → stove** (mục A, danh sách đầy đủ ở trên; chi tiết từng dòng ở file JSON). Không có cặp nào ngược chiều (0 dòng Việt của stove bị copy sang hearing).
- **1 cặp nội bộ: 2140 ← 2104** (mục C).
- **0 cặp chuyển chỗ nội bộ:** không dòng nào mà bản dịch đúng của nó đang nằm ở key khác trong cùng file — mọi dòng sai đều dịch mới, không khôi phục được từ trong file.
- 2 cặp Việt trùng nhau còn lại trong file đều đúng: 「Rút thăm trúng thưởng!!」 1696/2041 (JP cả hai chỗ đều là くじびきー！！) và 「Đường sắt Yukemuri…」 2104/2140 — chỉ 2140 sai (xem mục C).

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- Soutetsu độc thoại xưng "Tôi" (quy ước file + docs locations §2.1); Paulette xưng "Tôi"/"Em" theo ngữ cảnh; Hikari gọi Soutetsu "Ba"/"Papa" (パパ → "Ba" theo các dòng đúng trong file); Reina gọi Soutetsu "Anh Soutetsu"; bà cụ (おばあさん) xưng "lão bà"/"tôi" theo các dòng đúng sẵn có.
- 御一夜 → **"Ohitoyo"** trong các bản sửa (1913, 1990, 2028, 2648) — **Quyết định 19/11: 御一夜 = Ohitoyo** (đợt sửa 19/11 đổi từ "Ohimitera"); các dòng đúng trong file dùng lẫn "Ohito" (2604) và "Ohimitera" (2809), chờ đợt thống nhất sau. 御一夜鉄道 = "Đường sắt Ohitoyo" trong các bản sửa.
- 湯煙鉄道 = "Đường sắt Yukemuri" (2104 đúng sẵn có; 2140 là bản sao sai của câu này). 湯医 không xuất hiện trong file. 帝鉄 không xuất hiện trong các dòng sai (dòng đúng 2604 dùng "Teitetsu" — giữ nguyên, không đổi).
- 術仙炭鉱 = "mỏ than Jutsu-sen" (2696, khớp chuẩn audit 廃炭鉱); 運転台 = "buồng lái" (2792, khớp chuẩn audit 廃炭鉱); 8620 giữ nguyên; 炭水車 = "toa tiếp than nước"; 気動車改造客車 = "toa xe khách cải tạo từ xe động cơ"; 客車 = "toa xe khách"; ストーブ列車 = "tàu sưởi ấm"/"toa xe sưởi ấm"; マイントレジャー = "Mine Treasure" (2116 đúng sẵn có); タブレット = "máy tính bảng" (sửa gloss 2076/2642); エアクラ = "Aircra" (2617 đúng sẵn có); 津鐵 = "Đường sắt Tsugaru" (1300, khớp 1853 đúng sẵn có).
- 駿袋鉄道 (2071): JP có ruby すんたい → "Đường sắt Suntai" — TW viết 駿遠 (Sun'en), khác JP; bản sửa theo JP (ruby là bằng chứng trực tiếp). Xem đề xuất context số 3.
- 2228: JP cụt câu giữa chừng ("…平均77人のお客様は安全にマイントレジャーまで"), TW hoàn thiện thành câu hỏi — bản sửa theo TW.
- Còi tàu ポー không xuất hiện trong file này.

## Dòng không chắc chắn
- **Không có dòng nào chưa chắc chắn trong file này.** Mọi dòng sai đều sửa được từ JP+TW (JP và TW khớp nhau ở mọi dòng sai).

## Đề xuất cập nhật context (để Hieu quyết, KHÔNG tự đổi toàn dự án)
1. **御一夜 — Ohito / Ohimitera / Ohitoyo:** file này dùng lẫn "Ohito" (2604) và "Ohimitera" (2809) ở các dòng đúng; các bản sửa dùng "Ohimitera" cho nhất quán với Grand 01/Hibiki 03. Quyết định chung vẫn đang chờ Hieu; file 再開発 dùng nhất quán "Ohitoyo" (8/8 dòng) vẫn là bằng chứng mạnh nhất cho "Ohitoyo". Quyết định 19/11: 御一夜 = Ohitoyo — 4 bản sửa (1913, 1990, 2028, 2648) đã đổi sang "Ohitoyo" (đợt sửa 19/11).
2. **Thẻ gloss `%l` thêm vào:** 6 dòng đúng gắn thẻ gloss mà JP không có (1780, 1811, 2050, 2076, 2698, 2816 — 2028 đã sai nên không tính) — giống mô hình 31 thẻ 機関士 ở munakata. Hieu chọn một trong hai: (a) giữ nguyên như một quy ước gloss của file, (b) gỡ 6 thẻ để giống hệt bản gốc. (Riêng 2076 giữ thẻ, chỉ sửa gloss thành "máy tính bảng".)
3. **駿袋鉄道 → "Suntai":** JP ruby すんたい vs TW 駿遠 — đã sửa theo JP; nếu Hieu muốn theo TW thì đổi thành "Sun'en".

## Giới hạn của audit này
- Đã đọc hết 457 dòng script của file này: 101 dòng sai đã xác nhận, 356 dòng còn lại khớp JP/TW.
- Vẫn có thể sót vài dòng "trông hợp lý nhưng thực ra là bản dịch của dòng khác" — cách chắc chắn nhất vẫn là chơi qua chương và đối chiếu voice. Nếu Hieu gặp thêm dòng nào nghi ngờ trong file này thì gửi mình, mình kiểm tra nốt.
- Tổng 11 file đã audit xong: 133 + 255 + 299 + 374 + 199 + 2 + 20 + 12 + 19 + 7 + 101 = **1.421 dòng sai**.

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)
Lưu ý khi chép: các bản sửa viết liền một dòng, không chèn `\n` thủ công — theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng. Ngoại lệ duy nhất: dòng 2076 giữ nguyên thẻ `%l` (chỉ sửa gloss bên trong). File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng. Khối này đã kiểm tra bằng máy: trích khối từ chính file review, parse bằng tomllib — **101/101 key** khớp đúng tập dòng sai, không thừa không thiếu, giá trị sau khi parse khớp đúng bản sửa.

```toml
1251 = "——Đó là bà cụ đã cho chúng ta táo. Tôi vừa để ý đến lời khuyên của chính bà ấy, vừa lựa chọn lời nói."
1297 = "「……Em chẳng tuyệt vời gì đâu. Hoàn toàn không.」"
1299 = "「……Lúc đó Hikari vẫn chưa được sinh ra.」"
1300 = "「……Đồ tốt đấy nhỉ. Nghe nói là thứ từng được dùng trên Đường sắt Tsugaru.」"
1670 = "「Không đâu. Để chở khách đến Mine Treasure thì toa xe khách cải tạo từ xe động cơ của nhà mình vẫn thích hợp hơn.」"
1671 = "「Không.」"
1673 = "Không chỉ có thế, con bé còn thông minh, đáng yêu, là niềm tự hào của chúng tôi, là cô con gái tuyệt vời nhất thế giới."
1675 = "「Xin lỗi nhé~. Lần này cũng lại làm ồn ào rồi.」"
1687 = "「Không đâu, cùng nhau đấy. Để không phạm sai lầm, Hikari cũng đã hỗ trợ phán đoán của mama một cách đàng hoàng.」"
1703 = "「Quả nhiên. Tuyệt vời thật, hoàn toàn chính xác.」"
1712 = "「Cháu có biết bây giờ, tàu 『SL Mine Treasure』 trung bình có bao nhiêu hành khách không?」"
1728 = "「Hikari, giỏi lắm cơ~」"
1729 = "「Quả nhiên là vậy sao~」"
1734 = "「Bên này tốt hơn cơ~!!」"
1753 = "「Đến nơi rồi~!」"
1760 = "「Là giúp đỡ lẫn nhau nhỉ. Tuyệt vời thật.」"
1763 = "Ồ, hóa ra còn có thể nhờ người ta mua vé hộ nữa sao."
1769 = "「Người tuyệt vời là mama—— Paulette đấy.」"
1771 = "「Số liệu năm ngoái là bảy mươi bảy người~! Và ngày đông nhất là chín mươi hai người!」"
1787 = "「Ufu~」"
1790 = "「Fufufu~n」"
1803 = "「Wawa!」"
1813 = "「Fuwaa~, lửa đã cháy rồi này. Ấm áp quá đi~」"
1816 = "「Oaaaa, chỗ ngồi này tuyệt quá đi!!」"
1821 = "À à à, để mọi người phải chờ rồi, xin lỗi nhé. Đến tuổi này rồi thì không chạy nổi nữa."
1834 = "「Hừm~?」"
1841 = "「A!」"
1847 = "「Aaaa, là người lúc nãy!」"
1861 = "「Ê~, tại sao ạ~」"
1863 = "「Ư~! Nếu chưa được sinh ra thì không được ở cùng nhau sao~?」"
1866 = "「Ừm. Đúng là như vậy. Vì đứa trẻ sẽ được sinh ra vào một ngày nào đó. Vì ngày tôi trở thành mẹ——tôi đã nghĩ như vậy.」"
1867 = "「Ừm.」"
1870 = "「Ừm! Hikari giỏi lắm!」"
1887 = "「Ehehehe~!」"
1888 = "「Ồ.」"
1913 = "Với tư cách là thị trưởng, với tư cách là giám đốc. Em ấy đã đưa ra phán đoán tốt nhất cho Ohitoyo mà không chút do dự. Đó là một điều vô cùng đáng nể."
1917 = "「Tuyệt quá đi! Ngay cạnh lò sưởi này~!」"
1922 = "「Ấm quá đi~」"
1931 = "「Vâng! Lại đây, Hikari. Bế nào!」"
1944 = "「Mama, giỏi quá đi~」"
1945 = "「Bế con đi~!」"
1952 = "「Đúng vậy. Ghế hộp đã khiến lối đi chật hẹp, lại còn có cả lò sưởi nữa. Toa xe này chỉ có thể vận hành với điều kiện mọi hành khách đều có chỗ ngồi.」"
1979 = "「Vì là từ 2A đến 2D, nên là hộp ghế này đúng không ạ?」"
1990 = "Toa xe khách của Đường sắt Ohitoyo cần phải vận chuyển số hành khách đông đảo đến thế một cách an toàn và nhanh chóng."
1998 = "「Quả táo vừa nãy được nhận, thật sự rất ngon. Cảm ơn bà vì bữa ăn, cảm ơn bà rất nhiều.」"
2004 = "「Anh quá lời rồi.」"
2012 = "「Trước hết hãy ngồi xuống đã. Paulette, chỗ ngồi của chúng ta ở đâu?」"
2014 = "Từ trước cả khi Hikari được sinh ra, chúng tôi đã nghĩ về Hikari. Vì vậy chúng tôi mới có thể kéo đường ray đến tận đây mà không chút do dự."
2020 = "「Tôi đã nhờ bạn bè maitetsu ở đây xếp hàng ở quầy vé giúp mà. Đúng kiểu đánh trúng mục tiêu đấy.」"
2028 = "「Vì vậy, đối với Đường sắt Ohitoyo hiện nay, Oha014. Toa xe khách cải tạo từ xe động cơ hiện hành mới là đáp án tối ưu.」"
2049 = "「Ra là vậy ạ~. Ba giỏi quá đi!!」"
2057 = "「À——」"
2071 = "「Vâng. Thời điểm chiếc xe đó được chuyển nhượng, đúng vào khoảng thời gian chúng ta được bên Đường sắt Suntai chuyển nhượng lại toa xe khách.」"
2074 = "「Toa xe sưởi ấm~!」"
2076 = "「Con đọc được nè~! \\x%lタブレット;#00ffc040;máy tính bảng%l;#;!!」"
2078 = "「Có ba, có Reina——còn Hikari thì sao ạ~?」"
2087 = "Đúng là như vậy. Từ trước cả khi tôi kết duyên cùng Paulette. Chúng tôi đã nghĩ về tương lai."
2101 = "「Paulette, để tôi cõng Reina nhé.」"
2140 = "「Thật sự cảm ơn rất nhiều ạ.」"
2181 = "「Xúc 1000 xẻng than vẫn nặng hơn.」"
2185 = "「Không làm được đâu~. Hành khách, 77 người không lên được đâu~」"
2205 = "Nếu vậy thì tôi hiểu rồi. Vì mục đích chạy tàu không phải là ngắm cảnh dọc tuyến, mà là 『vận chuyển đến Mine Treasure』."
2211 = "「Đó là cho đi và nhận lại đấy ạ. Khi cô ấy muốn đi tàu ở Kyushu, tôi sẽ giúp cô ấy mua vé ở quầy, kiểu như vậy~」"
2214 = "Ra vậy. Vậy nên, cũng có khả năng là toa xe này đã về với chúng ta—— Là như vậy sao."
2228 = "Vậy thì, nếu thay toa xe khách hiện hành bằng toa xe sưởi ấm này thì sao? Làm thế nào để đưa trung bình 77 hành khách đến Mine Treasure một cách an toàn đây."
2247 = "「Vì tôi không chỉ có một mình.…… Vì có ba, có Reina, có mọi người ở bên, nên tôi mới không phạm sai lầm mà thôi.」"
2252 = "「Anh Soutetsu ơi, như vậy có nặng không ạ~」"
2470 = "Nhưng mà, ngay trước lò sưởi là lối đi. Trong tình huống này, đó không phải là nơi có thể đứng lại được."
2472 = "Thế nhưng, Paulette chỉ mỉm cười dịu dàng, bao bọc lấy lời khen ngợi của chúng tôi."
2485 = "Hikari lén lút nhìn quanh, rồi trả lời bằng một giọng nói rất nhỏ."
2490 = "Hikari ôm chầm lấy Paulette, rồi ngay sau đó cũng ôm chặt lấy tôi."
2496 = "Cảm nhận của Hikari rất thẳng thắn."
2503 = "Tóc của Hikari thật mềm mại. Nó cứ dính lấy lòng bàn tay tôi, có chút ẩm ẩm."
2512 = "Không phải vậy. Câu trả lời của tôi, nói cách khác, chỉ là câu trả lời muộn——đơn thuần là xác nhận lại tình hình hiện tại mà thôi."
2518 = "Chỉ cần Paulette nói một câu 『Sẽ mua』, thì chắc đã chẳng có ai phản đối. Thế mà——"
2536 = "Ngồi xuống, hơi nóng lại gần hơn. Thế nhưng, tuyệt đối không cảm thấy quá nóng."
2542 = "Chắc là cô ấy đang muốn dành vinh dự cho tôi, với tư cách là một người cha, một maitetsu."
2544 = "Nhìn chằm chằm vào khuôn mặt của Hikari, rồi từ từ, từ từ, xoa đầu con bé hết lần này đến lần khác."
2555 = "Có lò sưởi. Trong toa xe khách——hơn nữa, lại còn là trong toa xe khách bằng gỗ nữa."
2562 = "Cho dù có nhồi nhét đến 77 người lên tàu đi chăng nữa, hành khách gần lò sưởi cũng sẽ không tránh khỏi bị bỏng."
2583 = "Vừa nói, chân vừa bước những bước dài."
2589 = "Tôi đưa tay ra. Đến bàn tay của người vợ yêu dấu của tôi. Và rồi, đến đầu của cô con gái yêu dấu."
2614 = "Nếu tôi xoa đầu con bé mạnh tay, Hikari sẽ dụi đầu vào lòng bàn tay tôi như muốn nói 『nữa đi』."
2616 = "Tôi tuyệt đối sẽ không chen lên tàu vào phút chót, nhưng với việc chờ nối chuyến bị chậm trễ đến mức này, với tư cách là cùng một đơn vị kinh doanh đường sắt, tôi muốn lên tàu càng sớm càng tốt."
2621 = "Tôi để Reina ngồi xuống ghế, rồi cuối cùng tôi cũng đặt được hành lý xuống."
2630 = "Con bé ôm Reina còn lâu hơn cả ôm tôi. Rồi lại ngồi xuống bên cạnh Paulette với vẻ mặt mãn nguyện."
2642 = "Đọc được máy tính bảng, Express, nhưng lại không đọc được 『Bracelet』 (Vòng tay)."
2647 = "Toa xe sưởi ấm. Xét về mặt phong tình thì gần như thuộc hàng mạnh nhất, và vì tính mới lạ nên khả năng thu hút khách cũng mạnh. Nhưng——"
2648 = "Toa xe sưởi ấm chất chứa đầy kỷ niệm với người cha đã khuất. Mùa đông ở Ohitoyo rất lạnh, và thỉnh thoảng cũng có tuyết rơi."
2653 = "Người ngay từ đầu đã đưa ra giả định không chút sai lầm, và dẫn đến đáp án đúng một cách chuẩn xác là——"
2671 = "Paulette ngẩng mặt lên với vẻ ngạc nhiên."
2673 = "Vừa đặt Hikari xuống ghế ngồi, Paulette vừa nở một nụ cười tràn đầy niềm tự hào."
2676 = "Paulette ôm chặt lấy Hikari."
2681 = "Reina và Hikari vươn tay ra trong vòng tay của chúng tôi. Một khung cảnh khiến cả trái tim cũng ấm áp."
2696 = "Đúng là vậy. “Một ngày nào đó anh có muốn trở thành cha không?” Câu hỏi của Paulette vào ngày hôm đó, tại mỏ than Jutsu-sen——"
2728 = "Khi tôi quay mặt về phía giọng nói của Reina——"
2745 = "Reina đang được tôi cõng trên lưng cầm lấy hành lý của tôi, còn tôi thì nhận lấy hành lý của Paulette."
2747 = "Được ôm chặt, Hikari kêu lên một tiếng vui sướng, rồi đột nhiên, con bé cất lên một giọng nói hơi buồn."
2792 = "Không khí bên trong hoàn toàn khác với trong buồng lái. Tôi không ngờ than lại có thể cháy một cách dịu dàng đến thế."
2808 = "Hikari nghiêng đầu thắc mắc, nhưng Paulette và Reina thì mỉm cười gật đầu."
2840 = "（À……）"
```

## Việc tiếp theo
1. Áp dụng khối TOML trên cho file Paulette 04_鳴呼いきストーブ列車 (nhớ quyết 3 đề xuất context ở trên trước, để khỏi sửa đi sửa lại), chơi thử chương rồi báo lại.
2. Áp dụng khối TOML 7 dòng cho file hearing cùng lúc — hai file này là một cặp tràn, nên sửa cả hai cùng một đợt để khỏi lẫn.
3. Xuất lại CSV mới từ TOML (sau khi áp fix) để CSV không còn cũ — với CSV3 thì chỉ còn 2 dòng lẻ chưa dịch (lr真闇追加01/02) là cần dịch mới; 144/146 dòng chưa dịch đã có bản dịch trong các khối audit (Grand 01: 100, Hibiki 03: 44).
4. Tiếp tục audit các file còn lại theo thứ tự nặng trước — Paulette 04 đã xong cả hai file; ứng viên tiếp theo: Paulette 05, Grand Rewrite 04, hoặc các file còn lại trong danh sách heuristic.

## Kết bài
Paulette 04_鳴呼いきストーブ列車 là file thứ mười một được audit toàn bộ và là file nặng thứ sáu (22,1% sai): 99/101 lỗi là lệch vị trí, trong đó 90 dòng là bản dịch đúng của file hearing kề bên bị copy sang — mô hình tràn chương thứ hai trong dự án, sau Hachiroku 12 → 夜の嵐, và cũng một chiều như vậy (hearing sạch 1,8%, không bị nhiễm ngược). 7 mảnh vỡ mồ côi, 1 trùng lặp nội bộ, 1 dòng nguồn không xác định và 2 lỗi gloss hoàn tất bức tranh: cột Việt của file này đã bị xáo trộn nặng ở cả thoại lẫn lời dẫn, rải đều từ đầu đến cuối file — nhưng mọi dòng sai đều sửa được chỉ bằng cách dịch mới từ JP/TW, không cần thêm nguồn nào khác, và không có dòng nào chưa chắc chắn.

Việc còn lại của riêng file này là quyết 3 đề xuất context (御一夜, thẻ gloss, 駿袋鉄道), áp dụng khối TOML 101 dòng và chơi thử chương để nghiệm thu. Tổng 11 file đã audit: 1.421 dòng sai — và việc hai file cùng một chương 04 mà một file sạch (1,8%) một file nặng (22,1%) cho thấy không thể đoán độ sạch từ tên chương hay file bên cạnh; vẫn phải đọc hết từng dòng.
