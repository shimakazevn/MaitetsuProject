# Audit: れいな03_しゅっぱつしんこう.txt.toml (04_Reina)

- File: `れいな03_しゅっぱつしんこう.txt.toml` — route 04_Reina, 373 dòng script (monologue 150, 双鉄 90, れいな 61, ポーレット 53, ハチロク 19). Nội dung: cuộc gọi từ Công ty Cổ phần Đường sắt Kurogane — một công ty đường sắt mới đang tái cơ cấu các tuyến chở hàng/khai thác mỏ quanh mỏ than Chikuho thành tuyến vòng lớn, và ý tưởng SL du lịch chở cả khách lẫn hàng của Soutetsu đã được chọn làm biểu tượng phục hưng; Hachiroku xin đổi bố trí — nguyện vọng duy nhất của em là giảm gánh nặng cho Soutetsu chứ không phải gọi anh quay lại lái 8620; Soutetsu nhận ra mình muốn ở bên Reina; Reina được nhờ đi Yahata chọn toa xe tự hành (気動車) được nhượng lại; Soutetsu hiểu lầm là chia xa dài hạn, rồi cầu hôn Reina; Paulette sẽ nhận Reina làm con nuôi để làm hộ khẩu; "phong ấn" (シーリング) của Reina mở ra (đau bụng dưới); cả hai thu xếp hành lý và lên đường đi Yahata, kết bằng tiếng hô xuất phát của Reina.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, 373 dòng, 0 key trùng, 0 VN trống. TOML và CSV3 khớp tuyệt đối (208 dòng chênh chỉ ở `\\n` literal bị TOML-2 làm phẳng thành khoảng trắng — CSV3 là chuẩn, 0 chênh ngoài flatten). TOML md5 `f3f5d2ac9459591cb254ea25bdaf9766`, BOM + CRLF, `[selections]` rỗng, không bản sao trùng (chỉ 1 file khớp tên trong toàn toml2). Comment `# JP:` đủ 382/382 (373 script + 9 characters/subs... đếm thực tế: 373 script + 9 mục characters/subs = 382). Thẻ `%l`: JP = VN mọi dòng, 0 thẻ hỏng (1 dị thường phía JP ở 2221 — VN đã chuẩn hóa, không phải lỗi VN, xem §7).
- Phân loại (26): đại từ 12, gasp 6, SFX 6, thuật ngữ 1, nghĩa 1. Thoại 24/223 (10,8%), độc thoại 2/150 (1,3%). Theo nhân vật: 双鉄 14/90 (15,6%), ポーレット 4/53 (7,5%), れいな 5/61 (8,2%), ハチロク 1/19 (5,3%), monologue 2/150 (1,3%).

## 1. Gasp 6 (5 từ sweep + 1 sweep bỏ sót)

- Sweep 5 mục, áp nguyên 5/5, 0 sửa lại: 1395 (ええ～っ…… → "Ể~Ư..."), 1631 (――――っ!? → "――――Ư!?"), 1766 (っ!!? → "Ư!!?"), 1767 (っ!? → "Ư!?"), 2432 (（っ!）→（Ư!）). Tất cả kiểm chứng theo JP: っ cuối câu/đứng riêng, VN cũ chỉ giữ dấu câu/gạch ngang mà mất tiếng gasp.
- Sweep bỏ sót 1 (audit tự tìm): 995 双鉄 「っ――」 → VN cũ 「――」 → "Ư――". Tiền lệ sweep: グランドリライト10 1188, ハチロクh7 477, ハチロクh9 1354, ポーレットh3 935, lrれいな追加03 1079 đều sửa 「っ――」→「Ư――」. Đây là gasp toàn dòng của Soutetsu ngay trước cảnh hôn (2234 Reina nâng cằm → 995 → 2076 "muốn cứ hôn thế này mãi").
- Sweep không bỏ sót gasp nào khác: đã quét cơ học toàn bộ 148 dòng JP có っ → 39 ứng viên ngoài 5 mục sweep: 6 áp dụng (5 sweep + 995) + còn lại đều không phải gasp — っ nhấn mạnh gắn từ có nội dung (1634 ざーんねんっ!, 1404 やだっ!, 1674 くださいっ, 1722 さんっ, 1638 くてっ――), âm đã diễn (32 かちゃっ→"Cạch", 2423 とさっ→"Phịch", 2426 ぷにっ→"Chọc", 1370 んっ→"ưm", 1372 こほんっ→"E hèm", 1407/1408 んっ――→"Ưm――", 1428 うむっ!→"ừm!", 1685 っと――→"Rồi――", 2047 スリっと→"cọ cọ", 2249 ぎゅうっと→"nhíu chặt", 2291 ホっ→"thở phào"), hoặc っ trong từ (ちょっと, しっかり...). Riêng 1393 えええっ!? → "Ể!?" giữ nguyên: sweep không gắn cờ, tiền lệ ハチロク13 1846 giữ ええっ!? → "Hả!?"; 1423 ぁっ → "A" giữ nguyên: tiền lệ sweep 凪ふかみ03 2274 giữ ぁっ → "A." (âm cắt gọn đã diễn bằng âm tiết cụt + dấu câu).

## 2. SFX 6 (cười 5 + rên 1)

- Cười bị diễn thành gasp "Ư hự" 5 dòng — vi phạm quy tắc Hieu 19/11 (tiếng cười là tiếng cười, KHÔNG diễn thành tiếng rên; tiền lệ h8 đã bãi bỏ; tiền lệ đã merge: えへへぇ → "Ehehe~", うふふ → "Ufufu"):
  - 1484 ハチロク 「うふふっ」 → "Ư hự hự" → "Ufufu".
  - 1397 れいな 「えへへぇ」 → "Ư hự hự" → "Ehehe~".
  - 1396 れいな 「えへへぇ」 → "Ư hự hự~" → "Ehehe~".
  - 1399 れいな 「えへへぇ～」 → "Ư hự hự~" → "Ehehe~".
  - 1601 ポーレット 「うふふふふ」 → "ư hự hự hự" → "Ufufufufu" (U + 4×"fu", khớp JP うふふふふ).
- Rên 1: 1371 れいな 「ふぁ……あっ」 → VN cũ "Phù……a" → "Phà……aƯ". ふぁ→"Phù" sai nguyên âm so với dạng khóa ふぁ→"phà" (tiền lệ moan ふかみh1 987: ふぁっ→"Phù" sai, đề nghị xét lại thành "Fa"); あっ cuối dòng mất tiếng cắt → thêm Ư ("aƯ" đã có tiền lệ 6× trong moan JSON). Cảnh hôn, không phải file H — áp luật romaji-fallback/luật gasp trực tiếp trong audit.

## 3. Đại từ 12 (Soutetsu 10 + Paulette tự xưng 2)

Quy tắc đã chốt: Soutetsu "anh" với Paulette/Reina (gọi Paulette là "em"), "tôi" với Hachiroku. Tiền lệ kiểm chứng: 日々姫05 2120 ("Tôi đây"→"Anh đây", "cô đọc"→"em đọc" với Paulette).

- Soutetsu gọi Paulette "cô"→"em" 3 + tự xưng "tôi"→"anh" với Paulette 7:
  - 1691 (nói với Paulette, đáp lời cảm ơn): "Cảm ơn cô. Tôi rất vui." → "Cảm ơn em. Anh rất vui."
  - 1520 (nói với Paulette, xin lỗi vì hôn ở nơi công cộng): "tôi đã hoàn toàn quên béng mất." → "anh đã hoàn toàn quên béng mất."
  - 1417 (hỏi Paulette về hôn nhân pháp lý; Paulette đáp 1620): "Ý tôi là" → "Ý anh là".
  - 1298 (quay sang Paulette, 2260; nói về hộ khẩu): "mẹ vợ của tôi nhỉ." → "mẹ vợ của anh nhỉ."
  - 1626 (hỏi Paulette đang chảy máu mũi): "Cô sao vậy!" → "Em sao vậy!"
  - 1443 (hỏi Paulette): "cô đang chảy máu mũi kìa?" → "em đang chảy máu mũi kìa?"
  - 1538 (hỏi Paulette có manh mối gì không): "cô biết nguyên nhân sao?" → "em biết nguyên nhân sao?"
  - 1555 (đáp đề xuất của Paulette 1672): "Nếu là tôi thì tôi sẽ đi" → "Nếu là anh thì anh sẽ đi".
  - 1552 (đáp Paulette ngắt lời 1406, tuyên bố với Paulette/Reina): "Tôi muốn ở bên Reina... tôi cũng sẽ đi" → "Anh muốn ở bên Reina... anh cũng sẽ đi".
  - 1522 (tuyên bố quyết tâm trong mạch đối thoại với Paulette): "tôi cũng không bận tâm." → "anh cũng không bận tâm."
  - Ghi chú về 1552/1555/1522: người nghe là Paulette (trả lời trực tiếp Paulette, Reina chỉ nghe cùng) — tiền lệ giữ "Anh" khi trả lời trực tiếp Paulette dù nhóm có mặt (ROUTE-AUDIT 846: 2477); tiền lệ nhóm Paulette 14:1544 chỉ áp khi xưng hô cả nhóm (みんな/全員), không áp ở đây. Cùng cảnh đã dùng "anh" ở 1692/1562/1577/1735.
- Paulette tự xưng 2 (quy ước đã chốt qua kiểm chứng của parent: Paulette "em" với Soutetsu, "chị" với Reina):
  - 1547 (nói về Reina ở ngôi ba trong cảnh cầu hôn, người nghe là Soutetsu): "Tôi cũng vui lắm." → "Em cũng vui lắm."
  - 1489 (người nghe là Reina, không phải Soutetsu — parent sửa từ "em" thành "chị": 1490 cùng mạch nói Paulette tự xưng "chị" và trấn an Reina "Yên tâm đi"): "Nên tôi nghĩ" → "Nên chị nghĩ".
  - 1438 "tôi hiểu rồi" giữ nguyên: Paulette đang nghe điện thoại với người gọi từ Kurogane, không phải Soutetsu.
- Parent loại 2 fix Paulette (giữ nguyên VN cũ "tôi", ghi cờ không chắc người nghe — xem §10): 1386 (agent viện "đáp Soutetsu hỏi 1626" — 1626 cách 240 key, không liên quan; người nghe không xác định được từ dòng kề) và 1644 (agent viện "trả lời câu hỏi pháp lý của Soutetsu 1417" — 1417 không liên quan; người nghe Soutetsu hay Reina đều có thể).
- Đối chứng: Soutetsu "tôi" với Hachiroku giữ nguyên đúng 5 dòng (1557, 1700, 1508, 1723, 1603); Soutetsu "anh" với Reina giữ nguyên đúng 9 dòng (1735, 1551, 1368, 1692, 1562, 1449, 1577, 1284, 1554). Ngôi ba "cô ấy" chỉ Paulette giữ nguyên 5 dòng (1472 thoại, 2054/2057/2214/2385 độc thoại) — tiền lệ: ngôi ba không tính là gọi trực tiếp (Paulette 13 1163; 2604 "cô ấy chỉ Paulette ngôi thứ ba trang trọng với Akai" giữ nguyên).

## 4. Thuật ngữ 1

- 2387 độc thoại: gloss 機関士 "lái tàu" → "thợ lái đầu máy". Tiền lệ đã merge: gloss 機関士 trong độc thoại dùng dạng đầy đủ "thợ lái đầu máy" (2 dòng, độc thoại); "lái tàu" chỉ là dạng rút gọn trong thoại. Các gloss 機関士 trong thoại của Hachiroku (1564, 1281, 1591) giữ nguyên "lái tàu" theo đúng dạng rút gọn. Gloss 運転士 ở 1963 ("lái tàu") giữ nguyên — 運転士 là thuật ngữ khác, chưa có dạng chốt.

## 5. Nghĩa 1

- 1438 ポーレット (kết thúc cuộc gọi với Kurogane): JP 「はい、それでは」 / TW 「嗯，再見」 — VN cũ "Vâng, chào anh." tự thêm "anh" (giới tính người gọi không có trong JP/TW) → "Vâng, chào tạm biệt." (chỉ đổi phần chào cuối; "tôi hiểu rồi / Xin cảm ơn" giữ nguyên).

## 6. Mục thuộc đợt unification (không sửa trong audit)

- "Ohimitera" dạng cũ 7 dòng → "Ohitoyo": 1337, 1300, 1455, 1474, 2431, 2160, 2223.
- Gloss 帝鉄 1659 "Đường sắt Hoàng gia" → "Teitetsu" (dạng cũ chờ đợt thống nhất, không tính sai — tiền lệ ROUTE-AUDIT 1118).

## 7. Giữ nguyên có lý do (không tính sai)

- 1393 えええっ!? → "Ể!?" (xem §1); 1423 ぁっ → "A" (xem §1); 1444 くあっ!? → "Kua!?"; 1383 はうっ!? → "hau!?"; 1374 ひゃっ → "Hya."; 1486 ぷぁあ → "Puaa..."; 1384 ふふっ → "Fufu."; 1370 ふ……んっ―― → "Phù……ưm――" (ふ đứng riêng giữ "Phù" theo luật moan); 1446 んーーー → "Ưm―――"; 1634 ざーんねんっ! → "Tiếc quá!" (っ nhấn mạnh gắn từ có nội dung); 1722 さんっ, 1638 くてっ――, 1404 ティッシュっ―――― (っ cắt từ có nội dung, gạch ngang đã diễn); 1447 う……む → "Ừ……m." (diễn tách nhịp, tiền lệ moan 1223/1379/1458 "Fu, a"); 1373 ふわぁ → "Oa... phù oa." (diễn ngẫu hứng, chưa rõ sai); 992 gloss 9600 "9600 (Kyuroku)" rút gọn (thẻ còn đủ, chỉ thiếu phần mô tả "Teitetsu 9600 class" — ghi nhận, chưa tính sai); 2221 JP tự mang thẻ %l lỗi (thẻ đầu đóng `%l;` thiếu `#`, thẻ sau dư `#;`) — VN đã chuẩn hóa đúng cả hai thẻ, không phải lỗi VN; 2241 喚呼 gloss "xác nhận" giữ (nghĩa gọi-xác nhận trong đường sắt, TW 復誦); 2317/2128 義父/養子 → "cha nuôi/con nuôi" đúng (TW 養父/養子 xác nhận); 1298/1516 義母 → "mẹ vợ"/"Mẹ" đúng (TW 岳母/媽 xác nhận); 1601 "con rể" đúng (TW 女婿); 2135 路子 → "Michiko" đúng; 1303/1575 "công ty" là dương tính giả của quét "cô".

## 8. Cờ cho Hieu

- Không có cờ mới trong file này. B19 vẫn park (kiểm tra trong game ở Paulette 13 key 1596 trước đợt quét thẻ %l).

## 9. Lượt soát 2

- Agent: 28/28 tái kiểm chứng, 0 bỏ, 0 sửa. Parent kiểm chứng lại: loại 2 (1386, 1644 — người nghe không xác định được), sửa 1 (1489 "em"→"chị") → **26 fix**. Mọi fix chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm tra diff từng dòng bằng difflib: gasp 6 đều chỉ thêm "Ư"; SFX 6 chỉ đổi phần âm thanh; đại từ 12 chỉ đổi xưng hô; thuật ngữ 1 chỉ đổi gloss; nghĩa 1 chỉ đổi phần chào cuối).

## 10. Kiểm chứng

- JSON 26 mục dạng chuẩn (list of dicts, khóa chuỗi, đủ trường key/jp/tw/old_vn/fix/kind/character); khối TOML 26 khóa, parse OK bằng tomllib, 0 sai lệch giá trị (so sánh chuỗi thô; `\\n` giữ nguyên); jp/tw/old_vn khớp CSV3 tuyệt đối 26/26; mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa.
- Parent kiểm chứng 21/11 ~11:00: JSON 26 mục, TOML 26 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 26/26. Đại từ kiểm chứng theo dòng kề: 10 fix Soutetsu đều đúng dù người nghe là Paulette hay Reina (Soutetsu đều xưng "anh" với cả hai); 1547 "em" đúng (nói về Reina ở ngôi ba, người nghe Soutetsu); 1489 sửa "em"→"chị" (người nghe Reina, chứng cứ 1490 "chị" cùng mạch); loại 1386/1644 (người nghe không xác định được; citation của agent cho cả hai đều sai). Cờ cho Hieu: 1386/1644 giữ nguyên VN cũ, chờ xác định người nghe.
- Chi tiết đầy đủ: `audit-reina03-shuppatsu-shinkou-REVIEW.md`; danh sách sửa: `audit-reina03-shuppatsu-shinkou-wrong.json` (28 mục).

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
1395 = "「Ể~Ư...\\nNgười khác là sao chứ, tự nhiên lại...」"
1631 = "「Paulette! Thế này là――――Ư!?」"
1766 = "「Ư!!?」"
1767 = "「Ư!?」"
2432 = "（Ư!）"
995 = "「Ư――」"
1484 = "「Ufufu, Ngài Soutetsu biểu cảm phong phú hơn rồi nhỉ.\\nCứ như biến thành một người khác so với lúc mới gặp vậy.」"
1397 = "「Ehehe~, trò chơi gia đình thành sự thật mất rồi ạ~」"
1396 = "「Ehehe~」"
1399 = "「Ehehe~」"
1601 = "「Ra vậy, đúng thế nhỉ――đúng là vậy.\\nAnh Soutetsu…… là con rể…… của mình…… Ufufufufu.」"
1371 = "「Phà……aƯ」"
1691 = "「Cảm ơn em. Anh rất vui.」"
1520 = "「Xin lỗi, Paulette. Chuyện đây là nơi công cộng,\\nanh đã hoàn toàn quên béng mất.」"
1417 = "「À…… ừm, chuyện đó――về mặt pháp lý thì có được công nhận không?\\nÝ anh là cuộc hôn nhân giữa con người và \\x%lレイルロオド;#00ffc040;Railord%l;#; ấy.」"
1298 = "「Nhưng mà, nếu vậy thì trên hộ khẩu,\\nPaulette sẽ trở thành mẹ vợ của anh nhỉ.」"
1626 = "「Pa, Paulette!? Em sao vậy!」"
1443 = "「Mà khoan…… em đang chảy máu mũi kìa? Không sao chứ?」"
1538 = "「Gì chứ, em biết nguyên nhân sao?」"
1555 = "「Nếu là anh thì anh sẽ đi, cùng với Reina.」"
1552 = "「Anh muốn ở bên Reina. Muốn nhìn thấy nụ cười của Reina.\\nVì điều đó, dù là Yahata hay Teppohata, anh cũng sẽ đi bất cứ đâu.」"
1522 = "「Dù có phải bất nghĩa với nhà Migita,\\ndù có bị từ mặt đi chăng nữa, anh cũng không bận tâm.」"
1489 = "「Khu công nghiệp Bắc Kyushu cũng đã ảm đạm suốt một thời gian dài mà.\\nNên chị nghĩ dự án này mới được đánh giá cao và chấp nhận.」"
1547 = "「Em cũng vui lắm. Tình cảm của Reina,\\nkhông ngờ lại đơm hoa kết trái theo một cách tuyệt vời thế này.」"
2387 = "Ngay cả bây giờ, khi Hibiki đang trưởng thành nhanh chóng,\\nHachiroku vẫn công nhận tôi là người \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#; xuất sắc nhất."
1438 = "「Vâng. Vậy sao ạ, tôi hiểu rồi.\\nXin cảm ơn.――Vâng, chào tạm biệt.」"

```
## Kết bài

File れいな03_しゅっぱつしんこう.txt.toml: 373 dòng đã đọc đủ, 26 dòng sai (7,0%) — lỗi tập trung ở xưng hô hệ thống (Soutetsu gọi Paulette "cô"/tự xưng "tôi", Paulette tự xưng "tôi": 12 dòng) và SFX (tiếng cười bị diễn thành gasp "Ư hự": 5 dòng; rên ふぁ sai nguyên âm: 1 dòng), cộng 6 gasp っ bị mất (5 từ sweep + 1 sweep bỏ sót), 1 gloss thuật ngữ độc thoại và 1 câu bịa thêm giới tính người gọi. Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. 7 dòng "Ohimitera" + 1 gloss 帝鉄 chờ đợt unification. Không có cờ mới cho Hieu; B19 vẫn park.
