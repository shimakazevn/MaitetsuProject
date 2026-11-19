# Audit: Paulette h4_クリーム＆クリーム — 23 dòng Việt sai (đã đối chiếu JP + TW)

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa từng dòng: 265 dòng (độc thoại 155, Paulette 70, Soutetsu H 39, Soutetsu 1), đối chiếu JP + TW từ CSV3 và TOML-2.
- CSV vs TOML: 0 khác biệt thực chất (146 khác biệt thô chỉ ở `\n`/khoảng trắng); tập key bằng nhau (265); `[selections]` rỗng; thẻ `%l`: 0 hỏng; không có key trùng; không có dòng VN trống; VN==TW 0.
- md5: `64abe8098966360371870067cd0d2843` — không trùng với bất kỳ file nào trong 227 file TOML (không có bản sao; bản sửa áp dụng cho 1 file duy nhất).
- Heuristic dấu thoại ↔ lời dẫn: shift 0 đạt 265/265 = 1,000 — không có lệch vị trí.
- Đọc lần đầu phát hiện 18/23 dòng; rà soát chéo với đợt quét (pronoun sweep + gasp sweep) bắt thêm 5 dòng (xưng hô 906, 973, 984, 998; thở gấp 941).
- Rà soát chéo với sweep gasp っ: sweep xác nhận 3/3 bản sửa thở gấp của audit (941, 1030, 1632 — cùng giá trị sửa); audit không phát hiện thêm dòng gasp nào mà sweep bỏ sót trong file này.
- Viết bản sửa bằng tay + kiểm tra lần hai đọc lại toàn bộ 23/23 bản sửa đối chiếu JP (đúng 23, 0 bị loại). Trong kiểm tra lần hai đã sửa lại: 8 bản sửa có khoảng trắng thừa trước `\n`; 2 bản sửa dùng dấu 。 thay cho dấu . của bản cũ; 3 âm ghép (881, 882, 914) viết tách từ, đã gộp lại thành một từ theo quy ước của file ("Hyafu"/"Phuyan"). Tất cả đã sửa về đúng dạng bản cũ, chỉ đổi đúng phần lỗi.

## Kết luận về cơ chế lỗi

- Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương: file sạch về cấu trúc (shift 0 = 1,000).
- Lỗi chủ đạo là tiếng thở/tiếng rên để nguyên dạng La-tinh: 10/23 dòng (43%). File này đã Việt hoá nhất quán ひゃ→"Hya" nhưng lại bỏ sót cả họ âm きゃふ/ふにゃ/んきゅ/ふひゃ và lời nói ngọng (ほーへふふん, そうへふ). Quy tắc fa/fu từ h1/h2 (ふぁ/ふあ/ふぇ → "phà/phù/phê/phùa") cần mở rộng sang cả họ âm này (xem đề xuất).
- Xưng hô hệ thống: Soutetsu tự xưng "anh" 8/8 lần trong thoại/H (0 lần "Tôi" trước khi sửa; toàn bộ thoại Soutetsu chỉ có 1 lần "tôi" duy nhất) — cùng lỗi hệ thống như h1/h2/h3.
- Sai nghĩa 2 dòng, trong đó 1609 sai hướng (ぬぶ = rút ra, dịch thành "Phập" = đâm vào) — lỗi hướng SFX, cần đối chiếu JP từng âm.
- Thở gấp: 3 dòng (941, 1030, 1632), 1 do sweep bắt được.

### Quy tắc tiếng thở mở rộng (áp dụng trong file này, để Hieu duyệt lại)

- ひゃ→"Hya" giữ nguyên (tiền lệ h1/h2). Nhưng きゃふ→"Kyaphù", ふにゃ→"phunya", んきゅ→"Ưm", ふひゃ→"Phùhya" — tức là họ âm きゃ/ふ/ん + nguyên âm phải Việt hoá, không để nguyên dạng La-tinh. Lời nói ngọng (mồm đầy, nói lắp) dịch theo cách của chính file này: giữ lại âm ngọng bằng chính tả Việt ("Hôu-hê-hu", "hạnh phúh… hỉu mấh"), không dịch thành tiếng Việt chuẩn và không để nguyên La-tinh.
- Âm ghép viết liền một từ, theo quy ước của file ("Hyafu", "Phuyan") — không tách thành "Kya phù", "Phù hya".

## Chi tiết dòng sai

### Xưng hô (8 dòng)

**Key 702 (双鉄H)**
- JP: `「……欲しいっ――欲しいっ――ポーレットがっ」`
- TW: `「……我要你——我想要你——波萊特」`
- VN cũ: `「……Anh muốn——anh muốn——Paulette」`
- Sửa: `「……Tôi muốn——tôi muốn——Paulette」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 853 (双鉄H)**
- JP: `「いや、僕が急に呼び出したのだ。\nこちらこそすまなかったな、こんな時間に」`
- TW: `「不會，是我突然叫你出來的。應該是我說對不起，這麼晚還叫你出來」`
- VN cũ: `「Không, là do anh đột nhiên gọi em ra mà.\nAnh mới phải xin lỗi, giờ này rồi còn……」`
- Sửa: `「Không, là do tôi đột nhiên gọi em ra mà.\nTôi mới phải xin lỗi, giờ này rồi còn……」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 906 (双鉄H)**
- JP: `「ぷあっ――あっ――ポーレット――\n好きだ――愛してる――大好きだっ」`
- TW: `「呼啊——啊——波萊特――我喜歡你——我愛你——我好愛你」`
- VN cũ: `「Phù——a——Paulette——\nAnh thích em——Anh yêu em——Yêu em nhiều lắm.」`
- Sửa: `「Phù——a——Paulette——\nTôi thích em——Tôi yêu em——Yêu em nhiều lắm.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 973 (双鉄H)**
- JP: `「僕の精液――その他にない」`
- TW: `「就只能是我的精液」`
- VN cũ: `「Là tinh dịch của anh——không gì khác.」`
- Sửa: `「Là tinh dịch của tôi——không gì khác.」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 984 (双鉄H)**
- JP: `「先に帰した。と、いうのもだな――」`
- TW: `「我讓她先回去了。說起來——」`
- VN cũ: `「Anh để em ấy về trước rồi. Với lại, chuyện là thế này——」`
- Sửa: `「Tôi để em ấy về trước rồi. Với lại, chuyện là thế này——」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 998 (双鉄H)**
- JP: `「ポーレット――僕もっ――僕も、だっ！」`
- TW: `「波萊特――我也——我要射了！」`
- VN cũ: `「Paulette——Anh cũng——anh cũng, sắp rồi!」`
- Sửa: `「Paulette——Tôi cũng——tôi cũng, sắp rồi!」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 1021 (双鉄H)**
- JP: `「体をほぐした方がよかろう。\n僕に、洗わせてもらえるか？」`
- TW: `「還是先舒展一下身體吧。能讓我洗一下嗎？」`
- VN cũ: `「Nên thả lỏng cơ thể trước đã.\nCho phép anh tắm cho em nhé?」`
- Sửa: `「Nên thả lỏng cơ thể trước đã.\nĐể tôi tắm cho em nhé?」`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

**Key 1207 (monologue)**
- JP: `好きに洗っていいと言われた――\n言葉の価値を、ようやく僕も理解する。`
- TW: `她剛才說可以隨我的心意給她洗，現在我理解她這句話的價值了。`
- VN cũ: `Em bảo anh cứ tắm theo ý thích——\nCuối cùng tôi cũng hiểu được giá trị của câu nói ấy.`
- Sửa: `Em bảo tôi cứ tắm theo ý thích——\nCuối cùng tôi cũng hiểu được giá trị của câu nói ấy.`
- Lý do: Soutetsu tự xưng "anh" trong thoại/độc thoại (JP 僕) → "Tôi" (docs §2.1).

### Tiếng thở để nguyên dạng La-tinh (10 dòng)

**Key 859 (ポーレット)**
- JP: `「ひゃにっ？！　ひえっ！？　ま、まだっ――\nんきゅ！　ふあっ――あっ――あっ――んひゅっ！」`
- TW: `「什麼？！哎！？又、又來了——嗯！呼啊——啊——啊——嗯！」`
- VN cũ: `「Cái gì?! Hả!? V, vẫn còn——\nNkyu! Phù——a——a——ưm hya!」`
- Sửa: `「Cái gì?! Hả!? V, vẫn còn——\nƯm! Phù——a——a——ưm hya!」`
- Lý do: Âm thở/tiếng rên để nguyên dạng La-tinh (Nkyu/Kyafu/funya/Houhehu) → diễn bằng tiếng Việt theo tiền lệ h1/h2 (ふぁ/ふあ/ふぇ/ふや → phà/phù/phê/phùa/phuya; んきゅ → Ưm; lời nói ngọng → diễn bằng tiếng Việt).

**Key 881 (ポーレット)**
- JP: `「きゃふううううううううううっっ！！！」`
- TW: `「呀啊啊啊啊啊！！！」`
- VN cũ: `「Kyafuuuuuuuuuuuu!!!」`
- Sửa: `「KyaphùùùùùùùùùùùƯƯ!!!」`
- Lý do: Âm thở/tiếng rên để nguyên dạng La-tinh (Nkyu/Kyafu/funya/Houhehu) → diễn bằng tiếng Việt theo tiền lệ h1/h2 (ふぁ/ふあ/ふぇ/ふや → phà/phù/phê/phùa/phuya; んきゅ → Ưm; lời nói ngọng → diễn bằng tiếng Việt).

**Key 882 (ポーレット)**
- JP: `「きゃふあっ！？」`
- TW: `「呀啊！？」`
- VN cũ: `「Kyafua!?」`
- Sửa: `「KyaphùaƯ!?」`
- Lý do: Âm thở/tiếng rên để nguyên dạng La-tinh (Nkyu/Kyafu/funya/Houhehu) → diễn bằng tiếng Việt theo tiền lệ h1/h2 (ふぁ/ふあ/ふぇ/ふや → phà/phù/phê/phùa/phuya; んきゅ → Ưm; lời nói ngọng → diễn bằng tiếng Việt).

**Key 884 (ポーレット)**
- JP: `「んきゅっ！！」`
- TW: `「呀！！」`
- VN cũ: `「Nkyu!!」`
- Sửa: `「Ưm!!」`
- Lý do: Âm thở/tiếng rên để nguyên dạng La-tinh (Nkyu/Kyafu/funya/Houhehu) → diễn bằng tiếng Việt theo tiền lệ h1/h2 (ふぁ/ふあ/ふぇ/ふや → phà/phù/phê/phùa/phuya; んきゅ → Ưm; lời nói ngọng → diễn bằng tiếng Việt).

**Key 901 (ポーレット)**
- JP: `「は……あっ――ふにゃあっ――」`
- TW: `「呼……啊——呼喵——」`
- VN cũ: `「Hà……a——funya——」`
- Sửa: `「Hà……a——phunyaaƯ——」`
- Lý do: Âm thở/tiếng rên để nguyên dạng La-tinh (Nkyu/Kyafu/funya/Houhehu) → diễn bằng tiếng Việt theo tiền lệ h1/h2 (ふぁ/ふあ/ふぇ/ふや → phà/phù/phê/phùa/phuya; んきゅ → Ưm; lời nói ngọng → diễn bằng tiếng Việt).

**Key 903 (ポーレット)**
- JP: `「ふやんっ――くあっ――んっ――ひうっ――んっ！」`
- TW: `「呼啊——啊——嗯——呀——嗯！」`
- VN cũ: `「Phuyan——a——ưm——hí——ưm!」`
- Sửa: `「PhuyanƯ——a——ưm——hí——ưm!」`
- Lý do: Âm thở/tiếng rên để nguyên dạng La-tinh (Nkyu/Kyafu/funya/Houhehu) → diễn bằng tiếng Việt theo tiền lệ h1/h2 (ふぁ/ふあ/ふぇ/ふや → phà/phù/phê/phùa/phuya; んきゅ → Ưm; lời nói ngọng → diễn bằng tiếng Việt).

**Key 911 (ポーレット)**
- JP: `「ふやああああああああああんっ！！」`
- TW: `「呼啊啊啊啊啊！！」`
- VN cũ: `「Phuyaaaaaaaaaa!!」`
- Sửa: `「PhuyaaaaaaaaaaanƯ!!」`
- Lý do: Âm thở/tiếng rên để nguyên dạng La-tinh (Nkyu/Kyafu/funya/Houhehu) → diễn bằng tiếng Việt theo tiền lệ h1/h2 (ふぁ/ふあ/ふぇ/ふや → phà/phù/phê/phùa/phuya; んきゅ → Ưm; lời nói ngọng → diễn bằng tiếng Việt).

**Key 914 (ポーレット)**
- JP: `「ふひゃっ――そうへふ、ふん――\nわらひ、ひあわへれ……のほへちゃいまひはぁ」`
- TW: `「呼喵——雙鐵——我幸福得……暈過去啦」`
- VN cũ: `「Fuhya——anh Houhehu——\nEm, hạnh phúh quá……nên hỉu mấh rồi」`
- Sửa: `「PhùhyaƯ——anh Hôu-hê-hu——\nEm, hạnh phúh quá……nên hỉu mấh rồi」`
- Lý do: Âm thở/tiếng rên để nguyên dạng La-tinh (Nkyu/Kyafu/funya/Houhehu) → diễn bằng tiếng Việt theo tiền lệ h1/h2 (ふぁ/ふあ/ふぇ/ふや → phà/phù/phê/phùa/phuya; んきゅ → Ưm; lời nói ngọng → diễn bằng tiếng Việt).

**Key 952 (ポーレット)**
- JP: `「んきゅっ――あっ――ふあっ――んうっ――\nあなる――おしりっ――なかっ――ぐりって――んっ」`
- TW: `「嗯——啊——呼啊——嗯——屁眼——屁股——裡面——被鑽到了——嗯」`
- VN cũ: `「Nkyu——a——phù——ưm——\nLỗ hậu——mông——bên trong——bị ngoáy——ưm」`
- Sửa: `「Ưm——a——phù——ưm——\nLỗ hậu——mông——bên trong——bị ngoáy——ưm」`
- Lý do: Âm thở/tiếng rên để nguyên dạng La-tinh (Nkyu/Kyafu/funya/Houhehu) → diễn bằng tiếng Việt theo tiền lệ h1/h2 (ふぁ/ふあ/ふぇ/ふや → phà/phù/phê/phùa/phuya; んきゅ → Ưm; lời nói ngọng → diễn bằng tiếng Việt).

**Key 970 (ポーレット)**
- JP: `「ひゃい……ほーへふふん……ふにゃあ」`
- TW: `「好呀……嘿嘿……呼喵」`
- VN cũ: `「Vâng ạ……anh Houhehu……funya」`
- Sửa: `「Vâng ạ……Hừm hừm hừm……phunyaa」`
- Lý do: Âm thở/tiếng rên để nguyên dạng La-tinh (Nkyu/Kyafu/funya/Houhehu) → diễn bằng tiếng Việt theo tiền lệ h1/h2 (ふぁ/ふあ/ふぇ/ふや → phà/phù/phê/phùa/phuya; んきゅ → Ưm; lời nói ngọng → diễn bằng tiếng Việt).

### Thở gấp (3 dòng)

**Key 941 (双鉄)**
- JP: `「っ！」`
- TW: `「啊！」`
- VN cũ: `「っ!」`
- Sửa: `「Ư!」`
- Lý do: Mất tiếng hít っ (JP có っ, bản Việt bỏ mất) → "Ư" (quy tắc gasp; sweep toàn dự án xác nhận cùng giá trị sửa).

**Key 1030 (ポーレット)**
- JP: `「～～～～～～～～～っ！！」`
- TW: `「～～～～～～～～～啊！！」`
- VN cũ: `「～～～～～～～～～!!」`
- Sửa: `「～～～～～～～～～Ư!!」`
- Lý do: Mất tiếng hít っ (JP có っ, bản Việt bỏ mất) → "Ư" (quy tắc gasp; sweep toàn dự án xác nhận cùng giá trị sửa).

**Key 1632 (双鉄H)**
- JP: `（これ……は――気持ち良すぎる――\n頭まで――全部っ――泡だって――しまう、ほど――っ）`
- TW: `（這個……實在是太舒服了——就連腦子裡——都要全變成泡沫了）`
- VN cũ: `（Cái này……thì——sướng quá——\nĐến mức——đầu óc——cũng nổi bọt——mất thôi——）`
- Sửa: `（Cái này……thì——sướng quá——\nĐến mức——đầu óc——cũng nổi bọt——mất thôi——Ư）`
- Lý do: Mất tiếng hít っ (JP có っ, bản Việt bỏ mất) → "Ư" (quy tắc gasp; sweep toàn dự án xác nhận cùng giá trị sửa).

### Sai nghĩa (2 dòng)

**Key 1466 (monologue)**
- JP: `ネコ……か、オコジョかなにかだろうか？`
- TW: `這海綿也不知道是貓型還是白貂型。`
- VN cũ: `Mèo……hay là chồn hương gì đây nhỉ?`
- Sửa: `Mèo……hay là chồn trắng gì đây nhỉ?`
- Lý do: Sai tên loài: JP オコジョ là chồn ermine/chồn trắng (TW 白貂), bản Việt "chồn hương" là cầy hương — loài khác.

**Key 1609 (monologue)**
- JP: `（ぬぶうううううううっ！！！）`
- TW: `（插入）`
- VN cũ: `（Phập!!!!）`
- Sửa: `（Rúttttttt!!!）`
- Lý do: Sai hướng âm thanh: JP （ぬぶうううううううっ） là tiếng rút ra (ぬぶ = kéo ra), bản Việt "Phập" là đút vào — ngược nghĩa; file này tại 1604 và h3 926 đều dịch ぬぶっ là "rút ra".

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
[script]
702 = "「……Tôi muốn——tôi muốn——Paulette」"
853 = "「Không, là do tôi đột nhiên gọi em ra mà.\\nTôi mới phải xin lỗi, giờ này rồi còn……」"
859 = "「Cái gì?! Hả!? V, vẫn còn——\\nƯm! Phù——a——a——ưm hya!」"
881 = "「KyaphùùùùùùùùùùùƯƯ!!!」"
882 = "「KyaphùaƯ!?」"
884 = "「Ưm!!」"
901 = "「Hà……a——phunyaaƯ——」"
903 = "「PhuyanƯ——a——ưm——hí——ưm!」"
906 = "「Phù——a——Paulette——\\nTôi thích em——Tôi yêu em——Yêu em nhiều lắm.」"
911 = "「PhuyaaaaaaaaaaanƯ!!」"
914 = "「PhùhyaƯ——anh Hôu-hê-hu——\\nEm, hạnh phúh quá……nên hỉu mấh rồi」"
941 = "「Ư!」"
952 = "「Ưm——a——phù——ưm——\\nLỗ hậu——mông——bên trong——bị ngoáy——ưm」"
970 = "「Vâng ạ……Hừm hừm hừm……phunyaa」"
973 = "「Là tinh dịch của tôi——không gì khác.」"
984 = "「Tôi để em ấy về trước rồi. Với lại, chuyện là thế này——」"
998 = "「Paulette——Tôi cũng——tôi cũng, sắp rồi!」"
1021 = "「Nên thả lỏng cơ thể trước đã.\\nĐể tôi tắm cho em nhé?」"
1030 = "「～～～～～～～～～Ư!!」"
1207 = "Em bảo tôi cứ tắm theo ý thích——\\nCuối cùng tôi cũng hiểu được giá trị của câu nói ấy."
1466 = "Mèo……hay là chồn trắng gì đây nhỉ?"
1609 = "（Rúttttttt!!!）"
1632 = "（Cái này……thì——sướng quá——\\nĐến mức——đầu óc——cũng nổi bọt——mất thôi——Ư）"
```

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- Soutetsu gọi Paulette "em" 5 lần trong thoại/H (853, 863, 906, 984, 1021) vs "cô" 0 lần — cộng dồn toàn dự án: "em" 70 vs "cô" 43 (sau h3+h4). Lưu ý sửa số liệu: bản tóm tắt trước đó ghi h4 là 6 lần, nhưng đếm lại chính xác là 5 — ứng viên thứ 6 (1207, độc thoại "Em bảo tôi...") là lời Paulette được thuật lại (đại từ "Em" là Paulette tự xưng), không phải Soutetsu gọi Paulette. "Cô bé" tại 1005 là danh từ chỉ bộ phận, không phải cách xưng hô. Độc thoại dùng "cô ấy" 11 lần (ngôi thứ ba trong lời dẫn, không tính vào "cô").
- 御一夜: không xuất hiện trong file (0 lần cả 4 dạng Ohimitera/Ohito/Ohitoyo/御一夜).
- "mình" trong độc thoại: 4 lần (1328, 1294, 1303, 1259) — tất cả đều đúng (thành ngữ "ngâm mình", sở hữu/phản thân).
- Không có 湯医/帝鉄/コン/宮司/マスコン/KiHa/整備体/運転ボディ/機関士-gloss/駿袋 trong file.

## Đề xuất cập nhật context (chưa chốt)

- Mở rộng quy tắc fa/fu sang họ âm きゃふ/ふにゃ/んきゅ/ふひゃ (xem trên).
- Quy tắc hướng SFX: ぬぶ = rút ra ("Rút"), ずぶ/ずぶっ = đâm vào ("Phập") — đối chiếu JP từng âm, không đoán theo ngữ cảnh.

## Đã kiểm tra và KHÔNG tính là sai

- Các dòng ひゃ→"Hya"/"Hyan" (871, 873, 878, 880, 883, 887, 891, 912, 961, 965) — giữ theo tiền lệ h1/h2; 878 "Hyafu" là âm ghép ranh giới, ghi nhận; 912 (かひゅっ→"Hya!") là cách diễn lỏng nhưng nhất quán với quy ước rên của file.
- Tên rên giữ nguyên theo ngoại lệ: 899, 1003.
- 1311 (chủ ngữ — TW và VN đồng ý là Soutetsu; JP không có chủ ngữ tường minh).
- 856, 989 ("bà ấy" chỉ bà chủ nhà tắm — nhất quán).
- 1465 ("ở riêng bên nhau"); 1334 ("trơn/tuột"); 1407 (mảnh lời thề); 1437 ("không cắn chặt"); 1565 ("Hử" cho ぬ); 1573 ("Tí tách").
- Các bản Việt trùng trong file chỉ là tiếng rên/SFX ngắn lặp lại hợp lệ.

## Kết bài

- h4 sai 23/265 (8,7%) — nhẹ hơn nhiều so với h3 (24,7%) và ngang mức trung bình của route Paulette. File sạch về cấu trúc; lỗi tập trung ở tiếng thở La-tinh (10) + xưng hô hệ thống (8) + thở gấp (3) + sai nghĩa (2).
- Khối TOML 23 key đã parse đúng. Không có dòng chưa chắc chắn nào trong file này.
