# Audit — lrれいな追加03_れいなとのレール (04_Reina) — "Đường ray cùng Reina"

- File: `lrれいな追加03_れいなとのレール.txt.toml` — route 04_Reina, **304 dòng script**, 5 strong candidates.
- Nội dung: Soutetsu và Reina hẹn hò tham quan Ohitoyo — luyện xúc than dồn toa (投炭), đi thuyền sông Kuma, làm dao, tham quan xưởng rượu Migita; Reina nhận ra mình muốn cùng Soutetsu mở rộng thế giới; bàn về gia đình (cha mẹ, Michiko, Paulette, Denjiro, Kayoko, Mayami, Hibiki, Hachiroku), về việc không thể có con (Railord), và về ước mơ nối đường sắt tới Katakami, Moji, Hiroshima — "trở thành đường ray, chở theo giấc mơ của mọi người".
- Phương pháp: đọc hết 304/304 dòng theo JP + TW (CSV3), đối chiếu TOML-2. Không lấy mẫu.

## §1. Kết quả

**7 dòng sai / 304 (2,3%)** — file khá sạch; lỗi rải rác, không tập trung một loại.

- Lệch vị trí (misaligned) **0**, chuỗi xoay (rotation) **0**, nhiễm chéo file khác **0**, dòng mồ côi (orphan) **0**, chưa dịch **0**, trùng khóa **0**.
- Phân loại (7): sai nghĩa 3 (1122, 1534, 1732), bịa thêm (fabrication) 2 (1633, 1674), SFX 1 (659), gasp 1 (1079, từ sweep).
- `[selections]` rỗng (0 mục). Không có thẻ `%l` nào trong file (0/304) — không có thẻ sai định dạng.
- Không có bản sao file này (md5 duy nhất trong toàn bộ TOML-2; 1 copy, không áp fix 2 nơi).

## §2. Chi tiết từng dòng sai

### Sai nghĩa (3 dòng)

- **1122** (双鉄). JP: 「ふむ？　レモンを、僕が？」 — Soutetsu ngạc nhiên: "Hửm? Chanh — anh (đã ăn) sao?". TW xác nhận: 「嗯？我吃的是檸檬汁嗎？」 ("Anh đã ăn nước chanh sao?"). Ngữ cảnh: Reina vừa tiết lộ đã đổi thanh yên trong công thức thành chanh (1224), và Soutetsu vốn rất thích chanh, vắt chanh 100% khi ăn đồ chiên (1240, 1246) — câu này là anh ngạc nhiên vì mình đã ăn chanh mà không nhận ra. VN cũ: "Hửm? **Anh thích chanh á?**" (dịch thành hỏi sở thích, sai ý). → **"Hửm? Chanh á? Anh ăn chanh sao?"**
- **1534** (monologue). JP: 「思いもかけぬ素朴な問いかけ。僕より長くを生き抜いてきたれいなの言葉とも……いや。」 — 小助詞 とも = "hay là / hoặc là" (đưa ra khả năng khác), không phải "cùng với". VN cũ: "Một câu hỏi mộc mạc không ngờ tới. **Cùng với** lời nói của Reina, người đã sống lâu hơn tôi……không." (đọc nhầm とも thành "cùng với"). → **"Một câu hỏi mộc mạc không ngờ tới. Hay là lời nói của Reina, người đã sống lâu hơn tôi……không."**
- **1732** (monologue). JP: 「――強く主張することこそなかったが、右田家同居をれいなが望んでいることは、結婚前から伝わってきた。」 — 主張する = đòi hỏi/khẳng định, ngược hẳn với 反対 (phản đối). TW xác nhận: 「雖然她沒有強烈要求」 ("tuy cô ấy không mạnh mẽ đòi hỏi"). VN cũ: "——Tuy **không phản đối mạnh mẽ**, nhưng việc Reina muốn sống chung với gia đình Migita đã được truyền đạt từ trước khi kết hôn." (**đảo nghĩa: không đòi hỏi → không phản đối**). → **"——Tuy Reina chưa bao giờ mạnh mẽ đòi hỏi điều đó, nhưng việc em ấy muốn sống chung với gia đình Migita đã được truyền đạt từ trước khi kết hôn."**

### Bịa thêm — thêm nghĩa/chi tiết không có trong JP (2 dòng)

- **1633** (monologue). JP: 「意外な一言に尋ね返せば、れいなはますます鼻からの排気を強くする。」 — chỉ nói Reina thở hắt ra bằng mũi mạnh hơn; TW đồng ý (「玲奈鼻孔裡傳出的氣更重了」). VN cũ thêm "vẻ đầy tự hào" không có căn cứ trong JP: "…Reina càng thở hắt ra bằng mũi mạnh hơn, **vẻ đầy tự hào**." → **"…Reina càng thở hắt ra bằng mũi mạnh hơn."**
- **1674** (monologue). JP: 「すりすり――ぐいぐい。れいなに頭を擦り付けられる。」 — chỉ nói Reina dụi đầu vào (người) anh; JP không chỉ bộ phận nào, TW nói mặt dụi vào mặt (「玲奈的臉在我的臉上磨蹭」), không nói ngực. VN cũ tự thêm "ngực": "Cọ cọ——dúi dúi. Reina dụi đầu vào **ngực** tôi." → **"Cọ cọ——dúi dúi. Reina dụi đầu vào người tôi."**

### SFX (1 dòng)

- **659** (れいな). JP: 「……ふぁ」 — tiếng thở nhẹ. Quy tắc đã chốt: ふぁ/ふあ → "phà"/"phùa", không dùng "phá". VN cũ: 「……**Phá~**」 (sai thanh điệu). → **「……Phà~」**

### Gasp — sweep (1 dòng)

- **1079** (双鉄). JP: 「っ――」, TW: 「啊……」 — gasp cả dòng. Sweep `raw-tsu` đã liệt kê đúng. VN cũ còn nguyên ký tự Nhật: 「**っ**——」 → **「Ư——」**
- Sweep chỉ có đúng 1 mục cho file này (1079); đã kiểm chứng trực tiếp trong `sweep-raw-gasp-wrong.json`. Các っ còn lại trong JP đều là っ trong từ (ちょっと, すっごく…) hoặc っ nhấn mạnh gắn vào từ (1074 よっ―― → "Dô——" đã diễn, giữ) — không phải gasp bị mất.

## §3. Thuật ngữ dạng cũ — chờ đợt thống nhất, KHÔNG tính sai

- "Ohimitera" (御一夜 → "Ohitoyo" đã chốt): **4 dòng** — 675, 981, 1182, 1578.
- "Đường sắt Ohito" (御一夜鉄道 → "Đường sắt Ohitoyo"): **1 dòng** — 1319.
- Tổng 5 dòng dạng cũ, ghi chú chờ đợt thống nhất theo tiền lệ các file trước.

## §4. Các dòng đã kiểm tra kỹ và GIỮ NGUYÊN (không sửa)

- **Xưng hô Soutetsu — sạch.** 0 dòng thoại nào của Soutetsu dùng "tôi" khi nói với Reina; "anh" dùng nhất quán với Reina (664, 668, 673, 681, 986, 1086, 1094, 1202, 1222…). Monologue dùng "tôi" (628, 1596, 1600…) và "mình" ở 2 dòng độc thoại nội tâm cảm xúc (1197, 1306) — đúng ngoại lệ monologue đã chốt. Reina gọi "anh Soutetsu" nhất quán, không có "cậu Soutetsu".
- **1074** 「よっ――」 → "Dô——" — giữ (っ nhấn mạnh gắn vào よ, không phải gasp; tiền lệ "sentence-final emphatic っ attached to a word is NOT a gasp").
- **1071** 「ははっ」 → "Haha", **1034** 「ふふっ」 → "Hư hư." — giữ (tiếng cười đã diễn; cười là cười, không thành tiếng rên).
- **1082** 「あーーーん。あむっ。はふっ！　んっ――。ん。…………うむっ！」 → "A~~~~. Ngoạm. Háp! Ưm——. Ưm. …………Ngon!" — giữ (うむっ khi nếm món = hài lòng "Ngon!", đúng ngữ cảnh ăn uống).
- **1103 / 1168** 「それっ！」 → "Lên nào!" / "Thế này!" — giữ (tiếng hô khi nhấc/làm gì đó, diễn ngẫu hứng hợp ngữ cảnh).
- **1007 / 1009** — TW viết nhầm 100杯 thành 一千分 (1000); VN theo JP đúng (100 xẻng). JP thắng TW.
- **1240** — TW diễn sai (nói Soutetsu "không kén" nước thanh yên/sudachi); VN theo JP đúng (chanh thì vắt 100%, thanh yên/sudachi thì hầu như không vắt). JP thắng TW.
- **1357** — JP có dấu "?" (ký tự không đọc được trong nguồn: 「門次港までを?いで」); VN hoàn thiện theo TW ("抵達門司港") thành "nối đến cảng Moji" — giữ (nghĩa rõ từ ngữ cảnh nối tuyến).
- **1315** ヘリコニア → "hoa Thiên điểu" — giữ (tên thường gọi chấp nhận được của heliconia).
- **1293** 八ツ城/隈元 → "Yatsushiro, Kumamoto", **1265** 丘山 → "Okayama" — giữ (tên địa danh hư cấu, diễn theo TW).
- **1107 / 1170 / 1206** — ruby [やわた,1]矢幡 → "Yahata", [さんよう,1]讃陽/[さんいん,1]讃陰 → "San'yo"/"San'in", [キログラム,1]kg → "1kg" — giữ (quy ước nhất quán trong file: diễn cách đọc ruby thành tên).
- **1258** 「ずうっと」 → "mã-ãi" — giữ (cách diễn kéo dài theo phong cách, không sai nghĩa; các dòng khác dùng "mãi mãi").
- **1619** スキットル → "bình tông" — giữ (flask; JP/TW đồng ý là rót từ can xăng vào bình).
- **1541** 溺愛 → "mù quáng" — giữ (yêu say đắm hệ thống đường sắt; hơi mạnh nhưng đúng sắc thái).
- **1291** いただきまぁす → "Mời anh ạ" — giữ (Reina mời ăn, đúng ngữ cảnh dọn món).
- **1213 / 1242** VN trùng nhau 「Đúng vậy.」 — giữ (JP đều là 「だな」/「だなぁ」, câu ngắn lặp là bình thường, không phải chuỗi xoay).
- **0 VN trùng nhau khác trong file** (không có chuỗi xoay); **0 khóa trùng** trong CSV3 và TOML (304 khóa duy nhất); CSV3 VN khớp TOML tuyệt đối (187 chênh lệch chỉ là TOML-2 làm phẳng literal `\n` thành khoảng trắng — đã kiểm chứng: 0 khác biệt thực chất).

## §5. Kiểm chứng cơ học

- CSV3: 304 dòng, 1 set duy nhất (không có dual-set), 0 khóa trùng, 0 VN trống, 0 JP trống. Nhân vật: 双鉄 117, れいな 104, monologue 83.
- TOML-2: 304 khóa `[script]`, md5 `5b7c95e2aabe736363e7db442831ed9a`, không có file trùng nội dung trong toàn bộ TOML-2 (1 copy duy nhất). `[selections]` rỗng.
- JSON: 7 mục, khóa chuỗi, dạng chuẩn list-of-dicts (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 7/7.
- Khối TOML: parse được bằng tomllib, 7 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\n` viết `\\n` nên parse ra đúng literal backslash-n của CSV3). Tất cả fix giữ nguyên ngắt dòng literal `\n` của VN cũ (không thêm `\n` thủ công mới). Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa.
- Lượt soát 2: **7/7 tái kiểm chứng, 0 bỏ, 0 sửa** — soát lại toàn bộ 7 fix so với JP (+TW) lần 2: 659 (ふぁ→"phà" theo quy tắc), 1079 (sweep đã kiểm chứng), 1122 (TW "ăn nước chanh" + ngữ cảnh 1240/1246), 1534 (とも="hay là"), 1633 (JP không có "tự hào"), 1674 (JP/TW không có "ngực"), 1732 (TW "không mạnh mẽ đòi hỏi" + 主張≠反対).

## §6. Khối TOML (đã kiểm chứng parse)

```toml
"659" = "「……Phà~」"
"1079" = "「Ư——」"
"1122" = "「Hửm? Chanh á? Anh ăn chanh sao?」"
"1534" = "Một câu hỏi mộc mạc không ngờ tới.\\nHay là lời nói của Reina, người đã sống lâu hơn tôi……không."
"1633" = "Trước câu nói bất ngờ đó, tôi hỏi lại,\\nReina càng thở hắt ra bằng mũi mạnh hơn."
"1674" = "Cọ cọ——dúi dúi. Reina dụi đầu vào người tôi.\\nTuy có hơi đau một chút, nhưng cảm giác đó lại vô cùng dễ chịu."
"1732" = "——Tuy Reina chưa bao giờ mạnh mẽ đòi hỏi điều đó, nhưng việc em ấy\\nmuốn sống chung với gia đình Migita đã được truyền đạt từ trước khi kết hôn."
```

Kiểm chứng: khối parse được bằng tomllib, 7 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\n` viết `\\n` nên parse ra đúng literal backslash-n của CSV3). Tất cả fix đều giữ nguyên ngắt dòng literal `\n` của VN cũ (không thêm `\n` thủ công mới). Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (xem log §5).

## §7. Ghi chú cho Hieu (cần quyết / chờ thống nhất — không tính sai trong audit này)

- Thống nhất "Ohimitera" → "Ohitoyo" (4 dòng: 675, 981, 1182, 1578) + "Đường sắt Ohito" → "Đường sắt Ohitoyo" (1 dòng: 1319) — theo tiền lệ các file trước, fix trong đợt thống nhất.
- 1258 "mã-ãi" cho ずうっと — cách diễn kéo dài theo phong cách; nếu Hieu muốn thống nhất thành "mãi mãi" thì đổi trong đợt thống nhất.
- 1357 JP gốc có dấu "?" (ký tự không đọc được trong nguồn) — bản Việt hoàn thiện theo TW; không phải lỗi dịch, chỉ ghi chú.
- Không có câu hỏi xưng hô hay thuật ngữ mới nào cần Hieu chốt trong file này.

## Kết bài

File lrれいな追加03_れいなとのレール: 304 dòng đã đọc hết, **7 dòng sai (2,3%)** — 3 sai nghĩa (1122: "thích chanh" → "ăn chanh sao"; 1534: とも "cùng với" → "hay là"; 1732: đảo nghĩa "không phản đối" → "không đòi hỏi"), 2 bịa thêm (1633: bỏ "vẻ đầy tự hào"; 1674: bỏ "ngực"), 1 SFX (659: ふぁ "Phá~" → "Phà~"), 1 gasp (1079: 「Ư——」, sweep). Không có chuỗi xoay, không lệch hàng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch. JSON 7 khóa chuỗi; khối TOML parse OK, 7 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 7/7; lượt soát 2: 7/7, 0 bỏ, 0 sửa.
