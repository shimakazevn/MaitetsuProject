# REVIEW — Unification U14a: §7 OPEN O4–O19 (pronoun/addressee, group A)

- Batch: **U14a** — `unification-s7-open-pronouns-a`
- Items: **O4–O19** (16 mục, §7 UNIFICATION-LIST.md)
- Fix list: `unification-s7-open-pronouns-a-wrong.json` — **10 dòng, 4 file**
- Items có dòng sửa: **5** (O4, O6, O7, O11, O13) · Items 0 dòng (giữ nguyên có lý do): **11** (O5, O8, O9, O10, O12, O14, O15, O16, O17, O18, O19)
- Cơ sở rebase: chuỗi hiện tại **100 mục / 2.686 dòng** (queue.json, U13b đã gộp 22/11 ~13:00) → sau đợt này **105 mục / 2.696 dòng** (xem snippet)

## §1. Phạm vi + phương pháp

- Đọc §7 O4–O19 (toàn §7 để lấy ngữ cảnh), UNIFICATION-BRIEF.md, AUDIT-BRIEF.md, MOAN-BRIEF.md, LOGIC-DICH-VA-SUA.md (master của Hieu), MEMORY.md (quyết định 19–22/11), ROUTE-UNIFICATION.md (quyết định coordinator E2/F1/F5, quy tắc ひゃ-family, quy tắc đại từ).
- Nguồn số liệu: CSV3 good-set **87.833 dòng** (đã bỏ 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`); map old_vn = unification (gộp sau thắng, theo thứ tự gộp trong queue) > moan (1.516) > audit (9.140) > CSV3 VN. Map unification: 2.653 (file,key) duy nhất từ 22 file `unification-*-wrong.json` đã gộp.
- Mỗi dòng ứng viên đều đọc JP (+TW) và 3–8 dòng kề **theo thứ tự dòng của CSV3 (script order)**. Lưu ý quan trọng rút ra trong đợt này: **key số KHÔNG phải thứ tự cảnh** — các key kề nhau về số có thể thuộc các cảnh khác nhau (bằng chứng O17: key 1853/1855/1857 nằm ở vị trí file-order 189/282/341, cách xa 1858 ở vị trí 87; bằng chứng O18: key 2356 của 仲国04 là độc thoại khác hẳn key 2356 của 仲国02). Mọi kết luận người nghe trong đợt này đều dựa trên file-order, không dựa trên key-order.
- Quy tắc áp dụng: đại từ theo **NGƯỜI NGHE**, không theo người được nhắc tới (P1); nhóm hỗn hợp → "tôi" (tiền lệ Paulette 14 key 1544, Grand 02 key 1493); JP thắng TW; không đụng dòng gasp Ư hay dòng "Kh" (không có dòng nào trong đợt này thuộc hai loại đó); không sửa lại dòng đã đúng.
- Hiệu chỉnh trích dẫn trong list (ghi lại để coordinator sửa list): O16 key 2155 thuộc **日々姫04_同乗** (không phải カフェキッチン); O18 key 2356 thuộc **仲国02_北琴の鉄道** (không phải 仲国04); O7 key 2557 thuộc **ハチロク05_レイルロオドたち** (không phải ハチロク03/10); O11 key 2684 thuộc **凪ふかみ03_みかんの旅** (không phải 三人いっしょ — file đó không có key 2684 trong CSV3); O9 có **4** dòng "cô" (1250/1366/1243/**1616**), list chỉ ghi 3; O4 "em ấy" độc thoại đếm lại là **6** dòng (không phải 8×).

## §2. Quyết định từng mục OPEN (theo uỷ quyền của Hieu)

### O4. Cụm đại từ Olivy ↔ Soutetsu (ハチロク15b) — 1 dòng sửa
- **1566 SỬA "anh" → "cháu".** Soutetsu nói với Munakata; JP 僕, TW 宗方先生. Tiền lệ ハチロク12_ムナカタ来訪 áp đảo: Soutetsu → Munakata là "cháu"/"chú" ở 9 dòng (1826/1732/1919/1909/1903/1882/1941/1685/1808 — "Cảm ơn chú…", "Cháu định…", "Xin mời chú…"). 1566 là dòng duy nhất Soutetsu → Munakata xưng "anh" toàn dự án. "Ngài Munakata" giữ nguyên (宗方さん trang trọng).
- **1654 GIỮ "chị".** Olivy nói với Munakata, JP không có đại từ tự xưng tường minh; VN "Chị, quên——" là tự xưng của Olivy. "Chị" là tự xưng NHẤT QUÁN của Olivy trong toàn file 15b (1589 "Chị muốn xem", 1576 "vào lưng, chị", 1808 "giúp chị nhé", 1640 "chị đã hiểu", 1699 "chị rất nhiều", 1839 "Anh còn đưa chị đến Omiya", 1583 "Ôm chị", 1522 "nghe, chị nói") — không phải lỗi riêng ở 1654. Cô tự đặt mình ở vai chị lớn an ủi mọi người trong cảnh từ biệt; người khác vẫn gọi cô là "em" (Munakata 1315 "Em đánh giá anh quá cao rồi"; Hachiroku audit 2340 "Chị Olivy" — Hachiroku gọi Olivy là "chị", khớp vai này).
- **Độc thoại "em ấy" GIỮ (6 dòng: 2219/2280/2130/2211/2100/2036).** Tất cả đều chỉ Olivy đang yếu dần (cuộn tròn trên đùi ngài Munakata, không ngồi dậy được…); "em ấy" là cách Soutetsu gọi Olivy trong độc thoại, đúng (Olivy là "em" với Soutetsu — P24 đã chốt Soutetsu → Olivy "anh").
- **1685 GIỮ "anh".** Soutetsu → Olivy ("Anh, đã làm được gì đâu chứ"); Olivy đáp ngay sau đó 1542 "Anh đã làm rồi…" — đúng P24.

### O5. Soutetsu "anh" với Hachiroku — ハチロク09_もくもくオリヴィ — GIỮ TOÀN BỘ, 0 dòng
- Quyết: **giữ tất cả "anh" trong nửa sau của file** — không giới hạn ở cảnh hẹn hò trên tàu. Toàn bộ file là MỘT chuyến đi riêng tư liên tục (tàu BBQ → nhà tắm Tororyu-yu → cảnh đêm nắm tay ngủ); Hachiroku gọi Soutetsu "phu quân" (2072), Soutetsu gọi cô "Suzu" (1545); trước chuyến đi Soutetsu vẫn "tôi" (1951, theo audit). Register vợ chồng bao phủ cả ba chặng, không chỉ cảnh hẹn hò.
- Đã kiểm chứng từng dòng kept: 1073/1724/1883/1578/1734 (cảnh tắm — người nghe Hachiroku, 1724/1883/1734 có Olivy cùng nghe nhưng Soutetsu → Olivy cũng là "anh" theo P24 nên "anh" đúng với cả hai người nghe); 1861/1545/1891/2116 (cảnh đêm — Hachiroku đáp trực tiếp); 1702/1688/1859/2028/1802 (cảnh tàu BBQ — Hachiroku đáp trực tiếp; 1702 "chị Mayami" chỉ là nhắc tên người thứ ba). 2027 "anh Nagare" là gọi tên người thứ ba, không phải tự xưng — không đụng.

### O6. "Anh Migita" vs "ngài Migita" — 5 dòng sửa
- Quyết: **phân biệt theo hậu tố JP: 右田氏 → "ngài Migita"; 右田さん → "anh Migita".**
- Bằng chứng: Hiyoko dùng 右田氏 ở CẢ 11 dòng trong ハチロク10, nhưng VN tách làm hai: "ngài Migita" 6 dòng (2195/2477/2500/2592/2870/2931) vs "Anh Migita" 5 dòng (2092/2197/2198/2201/2277). Cùng một hậu tố 氏, cùng một người nói, cùng một file — phải thống nhất một dạng. "Ngài" thắng vì: (a) trong cùng câu 2092, ハチロク氏 đã dịch "cô Hachiroku" (trang trọng) mà 右田氏 lại dịch "anh Migita" — lệch chuẩn trong một câu; (b) 2477 "cả ngài Migita và cô Hachiroku" cho thấy cặp trang trọng song song; (c) tiền lệ người lạ trang trọng dùng "ngài Migita" nhất quán (Jiang 5 dòng: 1708/2740/2022/2155/1863; Hiyoko 6 dòng), còn "anh Migita" là dạng của người ngang hàng (Kisaki, Mima, Akai, Hibiki, nghị sĩ).
- **GIỮ "anh Migita" ở hội đồng:** 1937 (女性議員, JP 右田さん), 2449 (浦上, JP 右田さん), 1825 (không có tên, "anh là người hiểu rõ hiện trường nhất" — cùng người nói, cùng phiên điều trần, cùng dạng さん). 2198 sửa cả hai token "Anh" trong dòng (chủ ngữ + hô ngữ) thành "Ngài" cho nhất quán trong câu.

### O7. Soutetsu ↔ Olivy: "cậu" vs "em" / "cậu" vs "anh" — 1 dòng sửa
- **2304 SỬA "cậu" → "em"** (ハチロク10). Soutetsu → Olivy: "Ồ. Cậu biết sao Olivy." Dòng kề ngay trước 2302 cùng cảnh, cùng người nghe: "À, em bảo anh xem cái đó sao." — "em" là dạng Soutetsu → Olivy trong file này (2042 ハチロク03 "Olivy, em từng làm nhiệm vụ…" cũng "em"). 2304 là dòng duy nhất Soutetsu → Olivy xưng "cậu" toàn dự án (đã rà toàn dự án).
- **GIỮ Olivy → Soutetsu "cậu" (2680) và "anh" (2589/2663)** — đây là một cung register có chủ ý trong ハチロク03: Olivy gặp lần đầu dùng ソーテツサマ (2417/2589 "Ngài Soutetsu"), Soutetsu bảo bỏ "-sama" (2327 "Không cần thêm chữ ngài đâu"), Olivy hỏi nên gọi thế nào (2663 — câu hỏi LIỆT KÊ các phương án, "Anh Soutetsu?" là một phương án được đề xuất, không được đổi), rồi hai bên thống nhất gọi tên trần (2709 "gọi là Soutetsu và Hibiki nha!"), sau đó Olivy dùng "cậu" (2680, ハチロク10 2212/2328, ハチロク06 2499/2764/2382). Đổi 2589/2663 thành "cậu" sẽ phá cung này.
- **GIỮ Hachiroku → Olivy "cậu" (ハチロク05 2557, JP あなた).** Dạng "cậu" tương hỗ là chuẩn của cặp Hachiroku ↔ Olivy ở 05/06/14 (Olivy → Hachiroku "cậu": ハチロク06 2322, ハチロク14 2500/3077). Dạng "em" của Olivy → Hachiroku chỉ xuất hiện trong 15b, thuộc register "chị" từ biệt của file đó (xem O4).
- Cờ cho U15 (không sửa trong đợt này): Soutetsu → Olivy "cô" ở ハチロク14 2427 ("Olivy, cô có thể tiếp tục nghe ngóng…") và 2986 ("xin cô hãy đánh cược…") — cả hai đều là ngữ cảnh công việc trang trọng; có phải register công việc có chủ ý hay cần thống nhất về "em"? (xem §6).

### O8. Hachiroku tự xưng "Tôi" vs "em" (ハチロク10) — GIỮ, 0 dòng
- 2321/2451/2890 đều là Hachiroku nói với **Hiyoko** (người lạ, tiến sĩ trang trọng), JP わたくし ở 2451/1589-dạng (tự giới thiệu trang trọng). "Tôi" là dạng trang trọng đúng với người lạ; "em" của Hachiroku chỉ dùng với Soutetsu (thân mật) và — theo audit H10 2289 — với Hiyoko ở vai "em" khi được khen (ngữ cảnh khác). Cả ba dòng đều không phải nói với Soutetsu nên không mâu thuẫn với chuẩn "em" với Soutetsu.

### O9. 日々姫13: Kisaki gọi Hibiki "cô" + 2515 "mình" — GIỮ, 0 dòng
- **"Cô" GIỮ ở cả 4 dòng (1250/1366/1243/1616).** Kisaki → Hibiki là "em" ở MỌI file khác (20+ dòng: 日々姫01 1795, 日々姫02 2190/2206/2266, 日々姫05 2018/2073, 日々姫07 1642/1933/2147, 日々姫10 2843, 日々姫14 1836, 稀咲01 1698…; cô thậm chí tự xưng "chị" với Hibiki ở 1933/2147). "Cô" CHỈ xuất hiện trong file tranh luận công khai này (4/4 dòng), nơi Kisaki ở chế độ ứng cử viên thị trưởng trên sân khấu, tự xưng "tôi" nhất quán cả file (chế độ công việc/quyết đoán theo P5). Đây là register trang trọng công khai có chủ ý, song song với quy tắc ngữ cảnh của P5 — không phải lỗi ngẫu nhiên. (List ghi 3 dòng; dòng thứ tư 1616 "Cảm ơn cô, Hibiki" cũng thuộc cùng register.)
- **2515 GIỮ fix audit "tôi".** Độc thoại narration (さて、僕も動かねば) — quyết tâm hành động plain, không phải tự vấn nội tâm đầy cảm xúc nên không thuộc ngoại lệ "mình" của P19; giọng narration trong file này là "tôi" xuyên suốt. Khác với O15 (nói thành tiếng một mình, xem dưới).

### O10. Grand 02: Hachiroku "Tôi" vs "em" — GIỮ, 0 dòng
- 1195 "em" (xin đi cùng — lời nài nỉ thân mật, JP không có わたくし) vs 1785/1589 "Tôi" (xin lỗi trang trọng + chào từ biệt trang trọng, JP đều mở đầu bằng わたくし tường minh). Đây là chuyển register có chủ ý trong một cảnh: nài nỉ thân mật → bị từ chối → rút vào lễ nghi trang trọng. Tiền lệ: Hachiroku dùng "Tôi" trong các speech act trang trọng (tự giới thiệu ハチロク10 2451, Common02 2180/2182) dù Soutetsu có mặt. Quyết này là quyết gây tranh cãi nhất đợt (tương tự cờ T60 của E1) — nếu Hieu muốn thống nhất "em" với Soutetsu mọi ngữ cảnh thì lật 2 dòng 1785/1589.

### O11. 凪ふかみ03 2684 — 1 dòng sửa
- **SỬA "Anh" → "Tôi".** Soutetsu: "Cảm ơn hai người. Anh đi đây." Người nghe là CẢ Hachiroku ("tôi") lẫn Hibiki ("anh") — cả hai cùng đáp ngay sau (Hachiroku 2371 "Ngài đi cẩn thận nhé, ngài Soutetsu"; Hibiki 2177 "Anh đi á, đi đâu vậy?"). TW "謝謝你們" (cảm ơn các bạn — số nhiều) xác nhận địa chỉ nhóm. Tiền lệ chính xác: Grand 02 1493, cùng cặp người nghe Hachiroku+Hibiki, audit đã sửa "anh" → "tôi" (tiền lệ P17/Paulette 14 1544). File đúng là みかんの旅; 三人いっしょ không có key 2684.

### O12. Grand 09: 1128 + 2663 — GIỮ, 0 dòng
- **1128 GIỮ "anh".** "Người nghe không rõ" đã giải quyết được: người nghe là **Nagi** — toàn bộ đoạn là tâm sự với Nagi (Nagi đáp 2032 "anh hai vẫn là anh hai mà?", 1515 "Bây giờ anh hết sợ rồi hả?", 1567 "anh hai kì lạ quá nè"; Soutetsu 1441/1782/1838 đều "anh" với Nagi). Soutetsu → Nagi "anh" đúng P1.
- **2663 GIỮ fix audit.** JP cụt giữa chừng (monologue narration về Mikuro/D51) — audit đã sửa thành dạng cụt tương ứng ("Từ phía nhà xưởng bảo dưỡng vang lên tiếng nói. Hôm nay cũng như mọi hôm, Mikuro với D51 1031――"). Không có vấn đề đại từ; không sửa thêm.

### O13. Grand 10: 2006 + 1158 — 2 dòng sửa
- **1158 SỬA "Anh" → "Tôi".** "——Anh thay đồ đây, hai người định đứng xem à?" Người nghe là cả Hachiroku ("tôi") lẫn Hibiki ("anh") — monologue kề xác nhận cả hai cùng nhìn chằm chằm ("ハチロク・日々姫は何故かはしらん、変わらず僕を見つめたままだ"). Địa chỉ nhóm hỗn hợp → "tôi" (tiền lệ P17 như O11).
- **2006 SỬA "anh" → "tôi"** (độ tin cậy Trung bình-cao). Cảnh mơ: Soutetsu mơ thấy cha/mẹ/Michiko đã mất, một bàn tay gia đình vuốt tóc anh ("家族の手ではあるけれど" — cố ý không ghi rõ là ai). "Anh" chỉ đúng nếu bàn tay là Michiko (sinh đôi, Soutetsu "anh" với Michiko); nếu là mẹ thì "anh" sai hẳn. Không có bằng chứng nào phân biệt được — và toàn bộ đoạn mơ còn lại dùng giọng "tôi"/"mình" (độc thoại 2679/2799/2563/2535 "tôi"; tự nhủ 1551/1197 "mình"), 2006 là "anh" duy nhất trong đoạn. "Tôi" là dạng trung tính an toàn cho người nghe không xác định trong mơ, khớp giọng đoạn mơ. Ghi chú: nếu Hieu xác nhận bàn tay là Michiko thì hoàn lại "anh".

### O14. Grand 05: 2025/2032/2035 "Anh" với Reina — GIỮ, 0 dòng
- Cả ba dòng đều nói với Reina/Michiko, không phải Akai: 2025 Reina đáp trực tiếp (1848 "được nói chuyện thật nhiều với anh Soutetsu"); 2035 trả lời câu hỏi của Reina (2097 "muốn biết cảm nhận của anh Soutetsu"); 2032 Michiko đáp (1750). Akai CÓ mặt trong file (nhiều dòng 1811–2141, vị trí file-order 277–311) nhưng ở cảnh khác — các dòng 2025/2032/2035 nằm ở vị trí file-order 79/14/440, không cùng cảnh với Akai. Đại từ theo NGƯỜI NGHE: Reina/Michiko → "anh" đúng P1. Sự hiện diện của Akai trong phòng không đổi dạng xưng hô với người nghe chính.

### O15. Grand 07: 2022 "mình" — GIỮ, 0 dòng
- Soutetsu nói thành tiếng MỘT MÌNH trong phòng trống ("Khi tỉnh giấc, chỉ có một mình"; Hachiroku đã đi làm nhiệm vụ từ trước — 3537/1496), tự nhủ về việc nên nghỉ phép ("Một tháng——thì hơi khó, nhưng có lẽ khoảng hai tháng một lần, mình nên chủ động xin nghỉ phép…"). Đây là tự vấn nội tâm nói thành tiếng, thuộc ngoại lệ "mình" của P19 (chỉ dùng khi tự vấn nội tâm đầy cảm xúc; quy tắc chung vẫn "tôi"). Khác với O9-2515 (narration voice, quyết tâm plain → "tôi"). Việc parent gỡ fix audit ở dòng này là đúng — giữ "mình".

### O16. 日々姫04 2155 "Cảm ơn cô." — ĐÃ SỬA Ở U6, 0 dòng mới
- Key 2155 thuộc **日々姫04_同乗** (JP 「ありがとう」, TW 「謝謝」), không phải カフェキッチン. Cảnh: Paulette vừa chào tạm biệt kiểu chào nghiêm (2127 "Chúc anh có một chuyến đi tốt đẹp"), Soutetsu đáp lễ (2653) rồi cảm ơn — người nghe là **Paulette**. Giá trị hiện tại đã là "「Cảm ơn em.」" (unif U6/P2, `unification-s2-paulette-pronouns-wrong.json`) — đúng P2. Không còn gì để sửa.

### O17. 仲国04 1858 — GIỮ, 0 dòng (người nghe đã xác định được)
- "Anh biết rồi, anh sẽ giữ hộ." Ghi chú của parent ở audit review nghi ngờ người nghe (dựa trên key kề 1857 hỏi Jiang / 1855 Zhihuan khen tranh) — nghi ngờ đó dựa trên **key-order, không phải scene-order**. Theo file-order (script order): 1927 Jiang hỏi vé → 1822 Soutetsu "Hachiroku. Hibiki. Đưa vé đây." → **1798 Hibiki "anh lấy giúp em với. Nó ở trong túi nhỏ của em ấy."** → **1858 Soutetsu "わかった、預かるぞ"** → 2001 Hachiroku đưa vé → 2049 Soutetsu đưa vé cho Jiang. 1858 trả lời TRỰC TIẾP yêu cầu của Hibiki ở 1798 ("anh lấy giúp em" → "anh sẽ giữ hộ") — người nghe là Hibiki, "anh" đúng. Các key 1853/1855/1857 nằm ở vị trí file-order 189/282/341 — các cảnh khác hẳn. Audit §5 đã xếp 1858 vào nhóm "Với Hibiki" là đúng.

### O18. 仲国02 2356: Jiang "cô" vs Zhihuan "cậu" — GIỮ "cậu", 0 dòng
- Key 2356 thuộc **仲国02** (không phải 仲国04 — ở 仲国04 key 2356 là độc thoại không có đại từ). Cảnh quyết định Zhihuan đi cùng đoàn khảo sát: Jiang đề xuất (2572 "tôi muốn để cậu ấy đi cùng"), Soutetsu hoan nghênh (2412), Hibiki đồng ý (2375), Hachiroku nói với Zhihuan (2701 "Rất mong được anh giúp đỡ. Anh Zhihuan."), rồi Soutetsu 2356 "Vậy là quyết định rồi nhé. Trăm sự nhờ cậu." — "cậu" là **Zhihuan** (người vừa được quyết định cho đi cùng; Suika mừng rỡ ngay sau đó 3238 vì Zhihuan được đi). Đối chứng: ngay sau đó Soutetsu nói với Jiang bằng "cô" (2293 "Rất mong được cô giúp đỡ") — cặp "cậu" (Zhihuan) / "cô" (Jiang) phân biệt rạch ròi trong cùng cảnh. "Cậu" đúng.

### O19. 仲国02 2182 — GIỮ fix audit "em", 0 dòng
- "Haha. Đúng là làm em bối rối thật rồi… Được chứ? Hibiki." JP gọi thẳng tên 日々姫 ở cuối câu ("いいな？ 日々姫"), TW xác nhận; Hibiki đáp ngay sau (2596 "Em hiểu rồi!"). Hachiroku KHÔNG có mặt trong cảnh (người nói quanh đó: Jiang, Zhihuan, Suika, Hibiki). Tiền đề "người nghe Hachiroku ('cô')" của list là VOID. Fix audit "cậu" → "em" đứng vững.

## §3. Danh sách sửa (10 dòng / 4 file)

### ハチロク15b_さよなら列車.txt.toml — O4 (1 dòng)
| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1566 | 「あいにく、僕もこの細腕だ。\n宗方さん。よろしければ、お願いできますか？」 | 「可惜我力氣也不算大。宗方先生，能拜託您嗎？」 | 「Tiếc là, cánh tay của anh cũng mỏng manh lắm.\nNgài Munakata. Nếu được, nhờ ngài có được không?」 | 「Tiếc là, cánh tay của cháu cũng mỏng manh lắm.\nNgài Munakata. Nếu được, nhờ ngài có được không?」 | Soutetsu → Munakata "cháu"/"chú" (tiền lệ ハチロク12 ×9); 1566 là "anh" duy nhất với Munakata. |

### ハチロク10_旺宮鉄道歴史館.txt.toml — O6 (5 dòng) + O7 (1 dòng)
| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2092 | 「そのご反応。なるほど、右田氏はハチロク氏にとって、『最良のマスター』であるようですな」 | 「依你這番態度，不難看出，右田先生於你是"最般配的司機"」 | 「Phản ứng đó. Ra là vậy, đối với cô Hachiroku, anh Migita\ncó vẻ như là một 『Master tốt nhất』 nhỉ.」 | 「Phản ứng đó. Ra là vậy, đối với cô Hachiroku, ngài Migita\ncó vẻ như là một 『Master tốt nhất』 nhỉ.」 | Hiyoko: 右田氏 → "ngài Migita" (cùng câu đã có "cô Hachiroku" cho ハチロク氏). |
| 2197 | 「良いアプローチですな。右田氏」 | 「右田先生這番考量實屬周到啊」 | 「Một hướng tiếp cận rất tốt đấy. Anh Migita.」 | 「Một hướng tiếp cận rất tốt đấy. Ngài Migita.」 | Như trên (氏). |
| 2198 | 「その方が私に似合うと思いませんかな？ 右田氏」 | 「右田先生，你不覺得這個名字與我更加般配嗎？」 | 「Anh không thấy cái tên đó hợp với tôi hơn sao? Anh Migita.」 | 「Ngài không thấy cái tên đó hợp với tôi hơn sao? Ngài Migita.」 | Như trên (氏); sửa cả chủ ngữ + hô ngữ trong câu cho nhất quán. |
| 2201 | 「質の高い考察ですな。右田氏」 | 「右田先生，你的眼光著實獨到」 | 「Một sự suy xét rất chất lượng đấy. Anh Migita.」 | 「Một sự suy xét rất chất lượng đấy. Ngài Migita.」 | Như trên (氏). |
| 2277 | 「[もみじ,1]紅葉がなぜ、右田氏にことさら目をかけているのかも、\nふむ――多少は理解できました」 | 「為什麼紅葉特別看重右田先生，我大概也能理解」 | 「Tại sao Momiji lại đặc biệt để mắt đến anh Migita,\nhừm——tôi cũng phần nào hiểu được rồi.」 | 「Tại sao Momiji lại đặc biệt để mắt đến ngài Migita,\nhừm——tôi cũng phần nào hiểu được rồi.」 | Như trên (氏). |
| 2304 | 「ほう。知っているのかオリヴィ」 | 「噢，奧莉薇你知道這公司啊」 | 「Ồ. Cậu biết sao Olivy.」 | 「Ồ. Em biết sao Olivy.」 | Soutetsu → Olivy "em" (kề 2302 cùng cảnh "em bảo anh xem"; 2304 là "cậu" duy nhất của Soutetsu → Olivy). |

### 凪ふかみ03_みかんの旅.txt.toml — O11 (1 dòng)
| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2684 | 「ありがとう。行ってくる」 | 「謝謝你們，我現在要出去一趟」 | 「Cảm ơn hai người. Anh đi đây.」 | 「Cảm ơn hai người. Tôi đi đây.」 | Địa chỉ nhóm Hachiroku ("tôi") + Hibiki ("anh"); TW số nhiều; tiền lệ Grand 02 1493 cùng cặp người nghe. |

### グランドリライト10_ハチロク.txt.toml — O13 (2 dòng)
| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1158 | 「――着替えるのだが、見学するのか？」 | 「——我要更衣了，想參觀嗎？」 | 「——Anh thay đồ đây, hai người định đứng xem à?」 | 「——Tôi thay đồ đây, hai người định đứng xem à?」 | Địa chỉ nhóm Hachiroku + Hibiki (monologue kề: cả hai cùng nhìn chằm chằm). |
| 2006 | 「大丈夫だ……僕は、大丈夫」 | 「沒事的……我沒事」 | 「Không sao đâu……anh, không sao」 | 「Không sao đâu……tôi, không sao」 | Cảnh mơ, bàn tay gia đình không xác định (mẹ vs Michiko); đoạn mơ còn lại toàn "tôi"/"mình"; "tôi" trung tính. Độ tin cậy Trung bình-cao. |


## §4. Giữ nguyên có lý do (đã xét, 0 dòng)

| Mục | Dòng | Quyết |
|---|---|---|
| O4 | 15b 1654 "chị" (Olivy→Munakata) | Giữ — tự xưng "chị" nhất quán toàn file 15b |
| O4 | 15b monologue "em ấy" ×6 (2219/2280/2130/2211/2100/2036) | Giữ — đều chỉ Olivy, đúng P24 |
| O4 | 15b 1685 "anh" (Soutetsu→Olivy) | Giữ — đúng P24 |
| O5 | ハチロク09_もくもく 14 dòng "anh"/"em" (1073/1724/1883/1578/1734/1861/1545/1891/2116/1702/1688/1859/2028/1802) | Giữ — register vợ chồng bao phủ toàn bộ chuyến đi riêng tư |
| O6 | 採決 1937/2449 + 1825 "anh Migita" | Giữ — JP 右田さん (không phải 氏) |
| O7 | ハチロク03 2589/2663 "anh" (Olivy→Soutetsu); 2680 "cậu" | Giữ — cung register trước/sau thỏa thuận gọi tên trần (2709) |
| O7 | ハチロク05 2557 "cậu" (Hachiroku→Olivy) | Giữ — dạng "cậu" tương hỗ 05/06/14 |
| O8 | ハチロク10 2321/2451/2890 "Tôi" | Giữ — nói với Hiyoko (người lạ, trang trọng) |
| O9 | 日々姫13 1250/1366/1243/1616 "cô" | Giữ — register tranh luận công khai (Kisaki "tôi" cả file) |
| O9 | 日々姫13 2515 "tôi" (fix audit) | Giữ fix — narration quyết tâm plain, không thuộc ngoại lệ P19 |
| O10 | Grand 02 1195 "em" + 1785/1589 "Tôi" | Giữ — chuyển register nài nỉ → lễ nghi (JP わたくし ở 2 dòng "Tôi") |
| O11 | (không có dòng giữ khác) | — |
| O12 | Grand 09 1128 "anh" | Giữ — người nghe là Nagi (đã xác định) |
| O12 | Grand 09 2663 (fix audit) | Giữ fix — JP cụt, đã diễn cụt tương ứng |
| O13 | — | (cả 2 dòng đều sửa) |
| O14 | Grand 05 2025/2032/2035 "Anh" | Giữ — người nghe Reina/Michiko; Akai ở cảnh khác |
| O15 | Grand 07 2022 "mình" | Giữ — tự nhủ một mình, thuộc ngoại lệ P19 |
| O16 | 日々姫04_同乗 2155 "Cảm ơn em." | Đã đúng (U6/P2 sửa "cô" → "em") — 0 dòng mới |
| O17 | 仲国04 1858 "anh" | Giữ — người nghe Hibiki (file-order: đáp trực tiếp 1798) |
| O18 | 仲国02 2356 "cậu" | Giữ — người nghe Zhihuan (quyết định cho đi cùng); đối chứng 2293 "cô" với Jiang |
| O19 | 仲国02 2182 "em" (fix audit) | Giữ fix — JP gọi thẳng 日々姫; Hachiroku vắng mặt |

## §5. Khối TOML (đã kiểm chứng parse — xem §7)

```toml
[script]
1566 = "「Tiếc là, cánh tay của cháu cũng mỏng manh lắm.\\nNgài Munakata. Nếu được, nhờ ngài có được không?」"
```
```toml
[script]
2092 = "「Phản ứng đó. Ra là vậy, đối với cô Hachiroku, ngài Migita\\ncó vẻ như là một 『Master tốt nhất』 nhỉ.」"
2197 = "「Một hướng tiếp cận rất tốt đấy. Ngài Migita.」"
2198 = "「Ngài không thấy cái tên đó hợp với tôi hơn sao? Ngài Migita.」"
2201 = "「Một sự suy xét rất chất lượng đấy. Ngài Migita.」"
2277 = "「Tại sao Momiji lại đặc biệt để mắt đến ngài Migita,\\nhừm——tôi cũng phần nào hiểu được rồi.」"
2304 = "「Ồ. Em biết sao Olivy.」"
```
```toml
[script]
2684 = "「Cảm ơn hai người. Tôi đi đây.」"
```
```toml
[script]
1158 = "「——Tôi thay đồ đây, hai người định đứng xem à?」"
2006 = "「Không sao đâu……tôi, không sao」"
```

## §6. Cờ cho coordinator / U15 (không sửa trong đợt này)

- **F-O7-1 (mới):** Soutetsu → Olivy "cô" ở ハチロク14_冬 2427 ("Olivy, cô có thể tiếp tục nghe ngóng thêm được không?") và 2986 ("xin cô hãy đánh cược vào khả năng kéo dài tuổi thọ") — cả hai đều là ngữ cảnh công việc trang trọng (điều tra qua điện thoại / lời khẩn cầu). Có phải register công việc có chủ ý (như O9/O10) hay cần thống nhất về "em" theo P24? Cần một quyết chung cho dạng "cô" công việc của Soutetsu → Olivy (và có thể cả dạng "cô" của Soutetsu → Hachiroku 27 dòng đã cờ ở U6 §5 — cùng một câu hỏi lớn hơn).
- **F-O10-1:** O10 là quyết gây tranh cãi nhất đợt — nếu Hieu muốn Hachiroku "em" với Soutetsu trong MỌI ngữ cảnh thì lật Grand 02 1785/1589 sang "em". Ghi lại để Hieu/coordinator có thể đảo ngược.
- **F-O13-1:** O13-2006 (mơ) độ tin cậy Trung bình-cao — nếu xác nhận bàn tay trong mơ là Michiko thì hoàn lại "anh".
- **Hiệu chỉnh list (đề nghị sửa trong UNIFICATION-LIST.md):** O16 file đúng 日々姫04_同乗; O18 file đúng 仲国02; O7 2557 file đúng ハチロク05; O11 file đúng みかんの旅; O9 thêm key 1616; O4 "em ấy" đếm lại 6 (không phải 8×).

## §7. Lượt soát 2 (second pass) + kiểm chứng cơ học

- **Lượt soát 2: 10/10 tái kiểm chứng, 0 loại bỏ, 0 sửa lại.** Mỗi fix đã đọc lại đối chiếu JP (+TW) sau khi viết: 1566 (僕 + 宗方さん → "cháu" theo tiền lệ ハチロク12); 2092/2197/2198/2201/2277 (右田氏 ×5 → "ngài Migita"); 2304 (cùng cảnh 2302 "em"); 2684 (TW số nhiều + tiền lệ Grand 02 1493); 1158 (monologue kề xác nhận 2 người nghe); 2006 (giọng đoạn mơ "tôi"/"mình", người nghe không xác định).
- Kiểm chứng cơ học (script `_u14a_build.py`, chạy lại sau khi ghi JSON): JSON 10 mục, đủ 8 trường, key là chuỗi; jp/tw khớp CSV3 tuyệt đối modulo U+3000→space (10/10); old_vn khớp map precedence (csv3 10/10 — không dòng nào trùng merged batch, 0 dòng GHÉP); 0 fix == old_vn; 0 ký tự xuống dòng thật; 0 double backslash-n.
- Khối TOML §5: trích từ REVIEW và parse lại bằng tomllib — mọi block value đều bằng đúng fix trong JSON (10/10, 4 file). Chi tiết parse: xem log của `_u14a_verify.py`.

## Kết bài

- Đợt U14a quyết xong **16/16 mục O4–O19** (không park mục nào cho Hieu — mọi mục đều quyết được từ JP+TW+ngữ cảnh+dòng kề theo uỷ quyền; chỉ có 3 quyết ghi rõ độ tin cậy thấp hơn để coordinator/Hieu có thể đảo ngược: O10, O13-2006, và cờ F-O7-1).
- **10 dòng sửa mới / 4 file** (O4: 1; O6: 5; O7: 1; O11: 1; O13: 2). **11 mục giữ nguyên 0 dòng** với lý do ghi ở §4 (chủ yếu là register có chủ ý: tranh luận công khai, lễ nghi trang trọng, chuyến đi vợ chồng, cung đổi cách gọi của Olivy).
- 3 hiệu chỉnh trích dẫn quan trọng cho các đợt sau: người nghe xác định bằng **file-order** (không phải key-order) — O17/O18 đều đảo ngược kết luận cũ nhờ đó; và 3 mục list ghi sai file (O16/O18/O7-2557).
- File: `unification-s7-open-pronouns-a-REVIEW.md` + `unification-s7-open-pronouns-a-wrong.json` (10 mục, kind="unification").

**Tổng cộng sau đợt này: 105 mục / 2.696 dòng sai (unification)** (cơ sở 100 mục / 2.686 dòng + đợt U14a 5 mục / 10 dòng mới — đối chiếu `unification/queue.json` 22/11 ~13:00)
