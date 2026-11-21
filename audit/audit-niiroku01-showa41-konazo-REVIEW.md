# Audit: ニイロク01_正和四十一年・粉蔵.txt.toml — 17/338 (5,0%)

## 0. Xác minh file

- File: `ニイロク01_正和四十一年・粉蔵.txt.toml` — route 08_Niiroku.
- TOML-2: `sources/toml2/translation_toml/08_Niiroku/#U30cb#U30a4#U30ed#U30af01_#U6b63#U548c#U56db#U5341#U4e00#U5e74#U30fb#U7c89#U8535.txt.toml`, md5 `8e7db333fcbe41b8f453b52285ffd200`, UTF-8 BOM + CRLF, 338 key script. 1 bản TOML duy nhất (không có file trùng).
- CSV3: 1 set duy nhất, 338/338 key khớp TOML; VN khớp TOML 338/338 (chỉ khác ở kiểu làm phẳng `\n`→khoảng trắng của TOML-2 — 201 dòng; CSV3 là chuẩn). Không có set stale. 0 dòng VN trống.
- `[selections]` rỗng. Tag `%l`: JP 3 = VN 5 (2 tag VN thêm — xem §3).
- Nội dung: Akai (lái tàu thử nghiệm) và Niiroku (Railord Kuha 26) trò chuyện trong phòng Akai qua trà/rượu/nấu ăn: quá khứ của Akai (gia đình Thần quan, vợ cũ, con trai, kỳ thi lái tàu thử nghiệm), lịch sử Teitetsu (năm Showa 1, Taisho 35, cắt ngân sách Showa 30, điện khí hóa toàn tuyến, chị D60 46, toa buffet), vai trò và sự ra đời của Niiroku. Nhân vật: monologue 118, 赤井 116, ニイロク 104.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. 0 còn っ thô trong VN (dưới dạng hiển thị; ッ trong ビュッフェ nằm trong term của tag %l là tiếng Nhật giữ nguyên theo quy ước tag). 2 cặp VN trùng nhau: 1474/1777 「Không sao đâu.」 (cùng JP 「構いませんよ」 — lặp hợp lệ) và 1492/1499 「!!?」 (JP khác nhau: 1492 「！！？」 vs 1499 「っ！！？」 — 1499 đã sửa thành 「Ư!!?」, hết trùng).
- Đại từ: file không có Soutetsu — chỉ Niiroku, Akai và monologue (Akai). Niiroku gọi Akai "anh" nhất quán (1416, 1431, 1436, 1456, 1480, 1561, 1632, 1635, 1663, 1840); Akai gọi Niiroku "cô" nhất quán. Không có lỗi xưng hô nào.

## 1. Phân loại (17)

- terminology 12 (1422, 1554, 1596, 1597, 1677, 1761: 帝鉄→Teitetsu ×6; 1574, 1661, 1715: 御一夜→Ohitoyo ×3; 1715, 1745, 1841, 2188: tài xế→lái tàu ×4 — 1715 gộp 2 sửa trong 1 dòng)
- mistranslation 2 (1177, 1592)
- gasp 1 (1499 — sweep, áp nguyên văn)
- SFX 1 (1510 — cười うふふっ diễn thành gasp)
- invented-completion 1 (1887 — bịa thêm "tôi xin phép" cho câu cụt)

## 2. Từng dòng sửa

### 2a. Terminology — 帝鉄→Teitetsu (6), 御一夜→Ohitoyo (3), tài xế→lái tàu (4)

- **1422** [Akai] JP: 「ですが、帝鉄史を改めて学ぶうち。\n全く別の欲望が、私の中に芽生えたのです」 / TW: 「但是，在重新學習帝國鐵路史的時候。我的心中又萌生了其他的欲望」 / Cũ: 「Nhưng, trong lúc học lại lịch sử Đường sắt Hoàng gia.\nMột khao khát hoàn toàn khác đã nảy mầm trong tôi.」 / Mới: 「Nhưng, trong lúc học lại lịch sử Teitetsu.\nMột khao khát hoàn toàn khác đã nảy mầm trong tôi.」 — 帝鉄 → "Teitetsu" theo quy tắc đã chốt (không "Đường sắt Hoàng gia").
- **1554** [Akai] JP: 「\x%l明智;#00ffc040;明智%l;#;・\x%l大詔;#00ffc040;大詔%l;#;と発展の一途を辿る帝鉄の\n最初の[つまず]躓きは、\x%l大詔;#00ffc040;大詔%l;#;三十五年に訪れました」 / TW: 「在\x%l明智;#00ffc040;明治%l;#;、\x%l大詔;#00ffc040;大正%l;#;時期迅猛發展的帝國鐵路的首次受挫，發生在\x%l大詔;#00ffc040;大正%l;#;三十五年」 / Cũ: 「Đường sắt Hoàng gia vốn đang trên đà phát triển không ngừng qua các thời kỳ \x%l明智;#00ffc040;Meiji%l;#; và \x%l大詔;#00ffc040;Taisho%l;#;,\nnhưng bước vấp ngã đầu tiên đã ập đến vào năm \x%l大詔;#00ffc040;Taisho%l;#; thứ 35.」 / Mới: 「Teitetsu vốn đang trên đà phát triển không ngừng qua các thời kỳ \x%l明智;#00ffc040;Meiji%l;#; và \x%l大詔;#00ffc040;Taisho%l;#;,\nnhưng bước vấp ngã đầu tiên đã ập đến vào năm \x%l大詔;#00ffc040;Taisho%l;#; thứ 35.」 — 帝鉄 → "Teitetsu" theo quy tắc đã chốt.
- **1574** [Akai] JP: 「電化区間が伸びればいつか、いけますよ。\n[くまもと,1]隈元-[おひとよ,2]御一夜にはきっと、特急電車が走ります」 / TW: 「如果電力化路段延長的話，遲早有一天能去的。隈元與御一夜之間一定會開行特快電車的」 / Cũ: 「Nếu đoạn đường điện hóa được mở rộng thì một ngày nào đó sẽ đi được thôi.\nChắc chắn sẽ có tàu điện tốc hành chạy tuyến Kumamoto - Ohimitera.」 / Mới: 「Nếu đoạn đường điện hóa được mở rộng thì một ngày nào đó sẽ đi được thôi.\nChắc chắn sẽ có tàu điện tốc hành chạy tuyến Kumamoto - Ohitoyo.」 — 御一夜 → "Ohitoyo" (không "Ohimitera").
- **1596** [Niiroku] JP: 「帝鉄史――」 / TW: 「帝國鐵路史——」 / Cũ: 「Lịch sử Đường sắt Hoàng gia——」 / Mới: 「Lịch sử Teitetsu——」 — 帝鉄史 → "Lịch sử Teitetsu" theo quy tắc đã chốt.
- **1597** [Akai] JP: 「帝鉄の悲願、鉄道復興のための全線電化。\nその象徴であり切り札となる、特急系電車開発」 / TW: 「帝國鐵路的夙願是全線電力化，以此來復興鐵路。其象徵與殺手鐧便是特快電車的開發」 / Cũ: 「Điện khí hóa toàn tuyến vì sự phục hưng của đường sắt, ước nguyện tha thiết của Đường sắt Hoàng gia.\nSự phát triển của tàu điện tốc hành chính là biểu tượng và cũng là con át chủ bài cho điều đó.」 / Mới: 「Điện khí hóa toàn tuyến vì sự phục hưng của đường sắt, ước nguyện tha thiết của Teitetsu.\nSự phát triển của tàu điện tốc hành chính là biểu tượng và cũng là con át chủ bài cho điều đó.」 — 帝鉄 → "Teitetsu" theo quy tắc đã chốt.
- **1661** [Akai] JP: 「御一夜を離れ、[こくら,1]粉蔵に住んで。\n実際の就職活動は、それからでした」 / TW: 「我離開了御一夜，選擇在小倉定居。參加工作是在那之後了」 / Cũ: 「Rời khỏi Ohimitera, đến sống ở Kokura.\nHoạt động tìm việc thực sự bắt đầu từ đó.」 / Mới: 「Rời khỏi Ohitoyo, đến sống ở Kokura.\nHoạt động tìm việc thực sự bắt đầu từ đó.」 — 御一夜 → "Ohitoyo" (không "Ohimitera").
- **1677** [Niiroku] JP: 「その先は、習ってる。正和三十年に、\n帝鉄関連予算が、大幅削減」 / TW: 「接下來的內容我學到過。正和三十年大幅削減了帝國鐵路的相關預算」 / Cũ: 「Phần tiếp theo thì tôi đã học rồi. Năm Showa thứ 30,\nngân sách liên quan đến Đường sắt Hoàng gia bị cắt giảm đáng kể.」 / Mới: 「Phần tiếp theo thì tôi đã học rồi. Năm Showa thứ 30,\nngân sách liên quan đến Teitetsu bị cắt giảm đáng kể.」 — 帝鉄 → "Teitetsu" theo quy tắc đã chốt.
- **1715** [Niiroku] JP: 「そうなんだ。赤井[あそ,1]阿蘇神社。[おひとよ,2]御一夜。クマ。\nこのお茶と赤井運転士の、ふるさと――（コクっ）」 / TW: 「是這樣啊。赤井阿蘇神社、御一夜、隈元。這杯茶和赤井駕駛員的故鄉——（啜一口）」 / Cũ: 「Ra là vậy. Đền Akai Aso. Ohimitera. Kuma.\nQuê hương của loại trà này, và của tài xế Akai――(Ực)」 / Mới: 「Ra là vậy. Đền Akai Aso. Ohitoyo. Kuma.\nQuê hương của loại trà này, và của lái tàu Akai――(Ực)」 — 御一夜 → "Ohitoyo"; 運転士 → "lái tàu Akai" (nhất quán với 20+ lần "lái tàu Akai" trong file).
- **1745** [Niiroku] JP: 「無い。\n赤井運転士がお茶を淹れるのを見たのも、初めて」 / TW: 「沒有。我也是第一次看到你泡茶」 / Cũ: 「Chưa.\nĐây cũng là lần đầu tiên tôi thấy tài xế Akai pha trà.」 / Mới: 「Chưa.\nĐây cũng là lần đầu tiên tôi thấy lái tàu Akai pha trà.」 — 運転士 → "lái tàu Akai" (nhất quán toàn file; "tài xế" là lái xe nói chung, không phải lái tàu).
- **1761** [Akai] JP: 「その流れに抗うため、帝鉄は大きな賭けに出ます」 / TW: 「為了抵抗衰退，帝國鐵路甚至不惜鋌而走險」 / Cũ: 「Để chống lại làn sóng đó, Đường sắt Hoàng gia đã đánh một canh bạc lớn.」 / Mới: 「Để chống lại làn sóng đó, Teitetsu đã đánh một canh bạc lớn.」 — 帝鉄 → "Teitetsu" theo quy tắc đã chốt.
- **1841** [Niiroku] JP: 「赤井運転士。クッション」 / TW: 「赤井駕駛員，坐墊」 / Cũ: 「Tài xế Akai. Đệm.」 / Mới: 「Lái tàu Akai. Đệm.」 — 運転士 → "Lái tàu Akai" (nhất quán toàn file).
- **2188** [monologue] JP: うかつなことを言ってしまったかもしれません。\n私は試験運転士。 / TW: 我或許說了不該說的話。我只是一名試車員。 / Cũ: Có lẽ tôi đã lỡ lời mất rồi.\nTôi là tài xế lái thử. / Mới: Có lẽ tôi đã lỡ lời mất rồi.\nTôi là lái tàu thử nghiệm. — 試験運転士 → "lái tàu thử nghiệm" (dạng đã chốt trong file: 1579 "Lái tàu thử nghiệm tàu điện", 1820 "Lái tàu thử nghiệm").

### 2b. Mistranslation (2)

- **1177** [Akai] JP: 「……さぁ、どうでしたか」 / TW: 「……我也不知道」 / Cũ: 「......Chà, ai biết được chứ.」 / Mới: 「......Chà, thế nào rồi?」 — JP là câu hỏi (さぁ、どうでしたか — Akai hỏi Niiroku về lần lái thử, tiếp sau 1176 "về lần lái thử tiếp theo"); VN cũ "ai biết được chứ" đảo thành khẳng định "không biết" — sai nghĩa.
- **1592** [Akai] JP: 「脈は――確かにありますが」 / TW: 「希望——確實是有的啊」 / Cũ: 「Mạch thì——đúng là có đập thật.」 / Mới: 「Hi vọng thì——đúng là có thật.」 — 脈 = triển vọng/cơ hội, không phải mạch đập: TW nhất quán 有希望 ở 1563/1593/2337; ngữ cảnh 1590 hỏi về ngày nghỉ tiếp theo của Akai; VN cũ "Mạch… có đập thật" phá vỡ chuỗi echo 1592→1593→2337 (1593 và 2337 đều "Hi vọng").

### 2c. Gasp + SFX (2)

- **1499** [Niiroku] JP: 「っ！！？」 / TW: 「啊！！？」 / Cũ: 「!!?」 / Mới: 「Ư!!?」 — Sweep lost-gasp-whole — áp nguyên văn.
- **1510** [Niiroku] JP: 「うん。……うん。うふふっ」 / TW: 「嗯……嗯，呵呵」 / Cũ: 「Ừm...... ừm. Ư fufu.」 / Mới: 「Ừm...... ừm. Ufufu.」 — うふふっ là tiếng cười — quy tắc đã chốt: cười "Fufu"/"Ufufu", không diễn thành gasp "Ư"; VN cũ "Ư fufu" tách う thành Ư (gasp) + "fufu".

### 2d. Invented-completion (1)

- **1887** [Akai] JP: 「では、と」 / TW: 「那麼……」 / Cũ: 「Vậy thì, tôi xin phép.」 / Mới: 「Vậy thì...」 — JP 「では、と」 là câu cụt (trailing off); VN cũ bịa thêm "tôi xin phép" (xin phép ra về) trong khi Akai vẫn trò chuyện tiếp (1892) — giữ dạng cụt.

## 3. Đã kiểm chứng đúng — giữ nguyên

- **Gasp sweep:** chỉ 1 mục cho file này (1499), đã áp nguyên văn; 0 nhãn "already-rendered".
- **2331** （ぐ～～～～っっ） → "(Ọt~~~~~)" — tiếng sôi bụng: "Ọt" + ~ đã diễn trọn; っっ là ngắt cuối của SFX, không phải gasp mất; sweep không liệt kê — giữ.
- **1556** （ずずっ） → "(Sụp sụp)", **1715** （コクっ） → "(Ực)" — SFX đã diễn, giữ.
- **1497** ああ―――――― → "Aaaaaa" — 6 gạch ngang JP kéo dài âm, giữ.
- **1643** "Mới ở đây" — "mới" nhấn mạnh (chính là ở đây), giữ.
- **1522** "lại nhờ cô nhé" — theo TW (下次再麻煩你了), hợp cảnh Niiroku vừa hứa nấu lại (1511), giữ.
- **2202** "Nụ cười" cho それ — đối chiếu 2127 (nụ cười) + 2075 (ánh mắt các máy thử nghiệm), giữ.
- **1563** "chị Shiro" vs **1907** "Chị D60 46" — JP viết khác nhau (シロ vs Ｄ６０　４６, ruby デロクマルのシロ), giữ theo văn bản.
- **1609/1911 — VN thêm tag %l:** 1609 thêm tag trên モハシ21試験車両 ("Toa xe thử nghiệm Mohashi 21"), 1911 thêm tag trên ビュッフェ ("quầy ăn nhẹ") mà JP không có — gloss đúng, TW cũng thêm tag tương tự ở cả hai dòng; giữ nguyên, ghi nhận — không đếm sai.
- **1911 — tag %l của JP bị hỏng phía JP:** JP có `\x%l合造車;#00ffc040;合造車%l;\n#;` (đóng tag bị tách bởi `\n`); VN đã chuẩn hóa thành tag đúng — không phải lỗi VN, không sửa.
- **1493** む → "Hứ" — giữ (hờn dỗi hợp cảnh: Akai khen trà hơn món Niiroku nấu).
- **2020** 私の器 → "giới hạn của tôi", **2055** giữ nguyên dạng cụt — giữ.
- **Các dòng cụt khác giữ nguyên dạng cụt:** 1398, 1399, 1577, 1590, 1770 — không bịa thêm.

## 4. Gasp sweep — kiểm chứng trực tiếp

- Sweep có đúng 1 mục cho file này: 1499 (lost-gasp-whole, 「っ！！？」→「Ư!!?」) — jp/tw/old_vn khớp CSV3 tuyệt đối, áp nguyên văn.
- Quét cơ học toàn bộ dòng JP có っ: 0 gasp bị bỏ sót thêm ngoài sweep (các っ còn lại đều là phụ âm đôi trong từ — って/った/しっかり… — đã diễn đúng, hoặc SFX đã diễn: 1556, 1715, 2331 — xem §3).

## 5. Kiểm chứng cơ học (sau sửa)

- JSON 17 mục (key chuỗi, list-of-dicts), khối TOML 17 khóa, 0 sai lệch giá trị so với JSON.
- jp/tw/old_vn khớp CSV3 tuyệt đối 17/17; old_vn khớp TOML-2 (trừ làm phẳng `\n`) 17/17.
- Mỗi fix chỉ khác old_vn ở đúng chỗ thay đổi mục tiêu (diff-sanity 17/17 — xem §2; các fix terminology đều xây bằng thay thế chuỗi chính xác trên old_vn gốc CSV3).

## 6. Lượt soát 2

- 17/17/0/0: đọc lại toàn bộ 17 fix với JP lần hai; 0 bỏ, 0 sửa. Lượt soát 2 xác nhận lại: 1592 (chuỗi echo 脈 1592→1593→2337 + TW 有希望 ×3), 1887 (Akai vẫn trò chuyện tiếp ở 1892 nên "tôi xin phép" là bịa thêm), 1510 (うふふっ là cười, không phải gasp), và 6+3 fix thuật ngữ đã chốt (Teitetsu/Ohitoyo).

- Parent kiểm chứng 22/11 ~03:10: sửa lại 3 fix 1177/1592/1887 — khôi phục dấu 「」 bị rơi (JP và VN cũ đều có 「」; chỉ thay đổi dấu ngoặc, nghĩa của fix giữ nguyên; số lượng fix không đổi, vẫn 17).

## 7. Khối TOML (đã kiểm chứng parse)

```toml
[script]
1177 = "「......Chà, thế nào rồi?」"
1422 = "「Nhưng, trong lúc học lại lịch sử Teitetsu.\\nMột khao khát hoàn toàn khác đã nảy mầm trong tôi.」"
1499 = "「Ư!!?」"
1510 = "「Ừm...... ừm. Ufufu.」"
1554 = "「Teitetsu vốn đang trên đà phát triển không ngừng qua các thời kỳ \\x%l明智;#00ffc040;Meiji%l;#; và \\x%l大詔;#00ffc040;Taisho%l;#;,\\nnhưng bước vấp ngã đầu tiên đã ập đến vào năm \\x%l大詔;#00ffc040;Taisho%l;#; thứ 35.」"
1574 = "「Nếu đoạn đường điện hóa được mở rộng thì một ngày nào đó sẽ đi được thôi.\\nChắc chắn sẽ có tàu điện tốc hành chạy tuyến Kumamoto - Ohitoyo.」"
1592 = "「Hi vọng thì——đúng là có thật.」"
1596 = "「Lịch sử Teitetsu——」"
1597 = "「Điện khí hóa toàn tuyến vì sự phục hưng của đường sắt, ước nguyện tha thiết của Teitetsu.\\nSự phát triển của tàu điện tốc hành chính là biểu tượng và cũng là con át chủ bài cho điều đó.」"
1661 = "「Rời khỏi Ohitoyo, đến sống ở Kokura.\\nHoạt động tìm việc thực sự bắt đầu từ đó.」"
1677 = "「Phần tiếp theo thì tôi đã học rồi. Năm Showa thứ 30,\\nngân sách liên quan đến Teitetsu bị cắt giảm đáng kể.」"
1715 = "「Ra là vậy. Đền Akai Aso. Ohitoyo. Kuma.\\nQuê hương của loại trà này, và của lái tàu Akai――(Ực)」"
1745 = "「Chưa.\\nĐây cũng là lần đầu tiên tôi thấy lái tàu Akai pha trà.」"
1761 = "「Để chống lại làn sóng đó, Teitetsu đã đánh một canh bạc lớn.」"
1841 = "「Lái tàu Akai. Đệm.」"
1887 = "「Vậy thì...」"
2188 = "Có lẽ tôi đã lỡ lời mất rồi.\\nTôi là lái tàu thử nghiệm."
```

## 8. Cờ cho Hieu

- **1592** — 脈: phán đoán của audit ("Hi vọng", không phải "Mạch") — bằng chứng TW nhất quán 有希望 ×3 (1563/1593/2337) + ngữ cảnh 1590 hỏi về ngày nghỉ; Hieu kiểm tra khi chơi tới đoạn này nếu thấy không hợp.
- **1609/1911** — VN thêm tag %l (モハシ21試験車両, ビュッフェ) mà JP không có; gloss đúng, TW cũng thêm — ghi nhận quy ước, đợt thống nhất quyết có giữ hay gỡ.
- **1563/1907** — "chị Shiro" vs "Chị D60 46": JP viết khác nhau (シロ vs Ｄ６０　４６) — ghi nhận, không phải lỗi.
- B19 vẫn park (tag %l hỏng duy nhất trong file là phía JP ở 1911, VN đã chuẩn hóa — không cần Hieu).

## Kết bài

File ニイロク01_正和四十一年・粉蔵 (338 dòng) đọc hết từng dòng với JP + TW: **17 dòng sai (5,0%)** — terminology 12, mistranslation 2, gasp 1, SFX 1, invented-completion 1. Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Sweep áp nguyên 1/1 mục; quét cơ học toàn bộ っ không tìm thêm gasp nào. Lỗi tập trung ở thuật ngữ đã chốt chưa áp dụng (帝鉄→Teitetsu ×6, 御一夜→Ohitoyo ×3, tài xế→lái tàu ×4) — đều là lỗi hệ thống, không phải lỗi hiểu nội dung. Đại từ đúng toàn file (Niiroku "anh" với Akai, Akai "cô" với Niiroku; không có Soutetsu). Chi tiết đầy đủ: `audit-niiroku01-showa41-konazo-wrong.json` (17 mục, khối TOML 17 khóa, 0 sai lệch, jp/tw/old_vn khớp CSV3 tuyệt đối 17/17; lượt soát 2: 17/17/0/0).
