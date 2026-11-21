# Audit (hợp nhất): ハチロクh7_レトロモダンメイクラヴ.txt.toml (01_Hachiroku)

- File: `ハチロクh7_レトロモダンメイクラヴ.txt.toml` — route 01_Hachiroku, 435 dòng script (monologue 267, ハチロク 107, 双鉄 61). Nội dung: cảnh H (Hachiroku route) — Soutetsu và Hachiroku trong trang phục lễ hội hoài cổ Taisho (レトロフェスタ), xen kẽ độc thoại hồi tưởng về vụ tai nạn, về "khoảng thời gian bị đóng băng" của Hachiroku và lời hứa ngày mai nắm tay nhau bước tiếp. Chỉ có 2 nhân vật + độc thoại Soutetsu; người nghe của mọi câu thoại Soutetsu đều là Hachiroku.
- **BẢN HỢP NHẤT — không audit lại từ đầu.** Hai audit song song cùng file đã được đối chiếu từng dòng với CSV3/JP và gộp thành một bộ duy nhất: A ("meikuravu", 29 mục) + B ("love", 58 mục) → hợp nhất **65 mục**. Trùng nhau 22 key (10 khác fix), chỉ A có 7 key, chỉ B có 36 key. Mọi xung đột đã giải quyết theo JP (+TW khi cần), xem §1. Ba file của B đã đổi tên thành `.superseded-by-unified` sau khi bộ hợp nhất được kiểm chứng cơ học.
- Phương pháp: đọc lại toàn bộ 65 fix đối chiếu JP + TW (CSV3), kiểm tra chéo sweep gasp, kiểm tra cơ học đại từ / thuật ngữ / ký tự lạ / số lượng nguyên âm rên, đối chiếu TOML ↔ CSV3.
- Cơ sở tổng: **141 file / 6.385 dòng sai** (đã tự kiểm chứng lại từ ROUTE-AUDIT.md, dòng tổng cuối — khớp với cơ sở được giao).

## 1. Tổng quan

**65/435 dòng sai (14,9%)** — thoại 49/168 (29,2%), độc thoại 16/267 (6,0%).

| Loại | Số dòng | Keys |
|---|---|---|
| Romaji fallback (rên) | 13 | 732, 737, 738, 739, 741, 745, 753, 760, 761, 777, 787, 827, 856 |
| Sai nghĩa (meaning) | 13 | 757, 765, 802, 1222, 1321, 1349, 1364, 1410, 1429, 1836, 1878, 1909, 1944 |
| Gasp っ (sweep) | 12 | 477, 783, 804, 807, 814, 974, 975, 976, 978, 1433, 1444, 1842 |
| fa/fu | 6 | 731, 743, 796, 816, 823, 971 |
| Đại từ (pronoun) | 5 | 799, 863, 865, 881, 947 |
| Đếm vần (vowel) | 4 | 819, 843, 844, 845 |
| Độ dài SFX | 3 | 1820, 1824, 1844 |
| Hỗn hợp (2–3 lỗi/dòng) | 7 | 692 (typo+fa-fu), 736 (romaji+vowel), 759 (fa-fu+vowel+gasp), 763 (fa-fu+gasp), 812 (fa-fu+vowel), 813 (fa-fu+meaning), 842 (romaji+vowel) |
| Thuật ngữ (terminology) | 1 | 1371 |
| Lỗi gõ (typo) | 1 | 1382 |

Theo nhân vật: ハチロク 36/107 (33,6%), 双鉄 13/61 (21,3%), monologue 16/267 (6,0%). Lỗi tập trung ở thoại rên/thở của Hachiroku trong H-scene (mất âm, sai phụ âm đầu, sai số lượng nguyên âm) và gasp っ.

## 2. Đối chiếu hai audit — giải quyết từng xung đột

Quy tắc chung: fix **giữ nguyên `\n` literal của VN cũ** (CSV3 là chuẩn; brief cấm thêm `\n` mới, không cấm giữ ngắt dòng sẵn có — tiền lệ các file đã gộp đều giữ `\n`, 123/123). B giữ đúng `\n` của VN cũ trong 29/30 fix có ngắt dòng (856 là ngoại lệ do lỗi đọc "nha" của B); A viết 1 dòng, bỏ `\n`. Parent đã khôi phục `\n` ở 30 fix khi kiểm chứng gộp (24 lấy từ bản B, 6 khôi phục theo vị trí trong VN cũ: 757, 763, 856, 865, 881, 1429) — xem ghi chú parent ở mục Kiểm chứng. JP/TW/old_vn của cả hai bộ đều khớp CSV3 tuyệt đối nên không có mục nào bị loại vì sai nguồn.

### 2.1. Mười key trùng nhau nhưng khác fix

- **692** — Giữ B (có sửa): A chỉ sửa typo "Khônh!"→"Không!" và giữ "huaa!"; B sửa thêm ふあっ→"phùa!". JP là ふあっ (không phải ふぁっ) nên "phùa" đúng quy tắc đã chốt (ふあ→"phùa"). Fix hợp nhất: 「Không! Không được——đâu——Ngài Soutetsu——phùa!\nEo ngài, cứ ngoáy, ngoáy——mông em——em, bị nong rộng ra, mất」 (giữ `\n` của VN cũ).
- **736** — Giữ B: A "Hí gư!?", B "Higyu!?". JP ひぎゅっ = higyu; tiền lệ ngay trong file: 734 「ひぎゅっ！！！？」→「Higyu!!!?」 (VN cũ đã dùng "Higyu"). Số u: きゅぅ×7 → 8 u, cả hai đồng ý ("kiuuuuuuuu"). Fix: 「Higyu!? A——hí, kiuuuuuuuu!!」.
- **759** — Giữ B (có sửa): A giữ "phù a" và không thêm Ư; B sửa ふあっ→"phùa", んくぅぅぅ "kuuu"→"kuuuu" (4 u = 1+3) và thêm Ư cuối. JP kết bằng んくぅぅぅ～～っ — っ cuối tuyệt đối, không dấu câu sau: ~~ chỉ diễn ～～, っ mất hẳn nên theo quy tắc gasp đã khóa phải thêm Ư (sweep xếp "already-rendered" là sai ở điểm này). Fix: 「Hí a! Ưm——mông——phùa——mông, cũng……\nmà——bây giờ, thì……ưm——ưm kuuuu~~Ư」 (giữ `\n` của VN cũ).
- **763** — Sửa cả hai: A "Hu——a", B "Fu——a". JP ふ――あっ! — cùng mảnh JP này xuất hiện ở 837 (ふ――あっ! → "Phù——a!") và 968 (ふ――あっ! → "Phù——a!"), và dạng tách ふ――あ trong file hầu hết đã là "phù——a" (821, 837, 968; 485 "phù……a"). Fix hợp nhất theo tiền lệ trong file: 「Hiu!? Phù——a!? Ng, Ngài Soutetsu!\nĐợi——đợi——đợi đã——! ~~~~ƯƯ!!!」 (っっ cuối → ƯƯ, cả hai đồng ý).
- **796** — Giữ B: A "Phù a", B "Phà". JP ふぁっ — quy tắc đã chốt ふぁ→"phà" (khác ふあ→"phùa"). VN cũ "A" mất hẳn âm ふ. Fix: 「Phà」.
- **842** — Giữ B: A "Ưm——aaaaaAAAAAAaaaaAAA!", B "Nyu——aaaAAAAaaaaaaAAAAA!". JP んゅ――ぁぁぁああああぁぁぁぁぁぁあああああっ: đếm được ぁ×9 + あ×9 = 18 âm a; B vừa đủ 18 a vừa mirror đúng nhóm hoa/thường theo ぁ/あ (3+4+6+5), A đủ 18 a nhưng nhóm không khớp (5+6+4+3); B còn khôi phục ゅ bị mất ("Ưm"→"Nyu"). Fix: 「Nyu——aaaAAAAaaaaaaAAAAA!」.
- **844** — Giữ B: A "Ưm kiuuu ưm ưm!!!", B "Ưm kiuuu ưm ưm ưm!!!". JP んきゅううんんんっ: きゅうう → 3 u (cả hai đồng ý) và ん đầu + んんん cuối = 4 âm mũi; B đủ 4 "ưm", A chỉ 3. Fix B.
- **1382 / 1433 / 1444** — Giữ nội dung chung của A và B, giữ `\n` literal của VN cũ theo bản B (A đã bỏ `\n`; parent khôi phục khi kiểm chứng gộp).
- Các key trùng còn lại giống hệt nhau (477, 804, 807, 814, 843, 845, 974, 975, 976, 978, 1371, 1842) — giữ nguyên.

### 2.2. Bảy key chỉ A có — giữ nguyên cả 7

- **757** (meaning): ひまっ là tiếng rên trong chuỗi rên ngắt quãng (ひあっ/らめっ/れすぅ), không phải 今 ("bây giờ") — VN cũ dịch trùng 2 lần "Bây giờ" (ひまっ và い、いま). Fix: ひまっ→"Hí ma" (theo quy ước ひあ→"Hí a"). TW thêm "那裡" không có cơ sở JP — JP thắng TW.
- **799, 863, 865, 881, 947** (pronoun): Soutetsu "anh"→"tôi" với Hachiroku, theo quy tắc đã chốt ("tôi" với Hachiroku/Mayami/Minokasa/Kisaki). B giữ nguyên 5 dòng này và cờ chờ chốt toàn dự án (thanh ghi vợ chồng 旦那様/おまえ/妻; 947 "anh" kề ngay 948 "tôi"). Đối chiếu lại theo chỉ đạo: không có dòng nào trong 5 dòng này có dấu hiệu JP chứng minh "anh" thân mật có chủ đích — JP đều dùng 僕 như các dòng "tôi" cùng người nói/người nghe (700, 878, 879, 948); 879 nói thẳng "お前が僕の妻" (em là vợ của tôi) mà vẫn dùng "tôi", nên thanh ghi vợ chồng không tách được "anh" khỏi "tôi". Áp quy tắc đã chốt cho cả 5 dòng: 799 "Anh sẽ xuất tinh"→"Tôi sẽ xuất tinh"; 863 "Cả anh"→"Cả tôi"; 865 "Anh mới là"→"Tôi mới là" (giữ `\n` của VN cũ); 881 "làm anh xuất tinh… của anh"→"làm tôi xuất tinh… của tôi" (2 chỗ; giữ `\n` của VN cũ); 947 "Anh yêu em"→"Tôi yêu em" (kề ngay 948 "tôi cũng vậy" — nhất quán).
- **1429** (meaning): JP 味わわずにいた là phản thực tại quá khứ — "lẽ ra tôi đã mãi mãi không được nếm trải (khoảnh khắc này)". VN cũ dịch ngược thành tương lai "sẽ vĩnh viễn không bao giờ được tận hưởng". TW cũng sai hướng này — JP thắng TW. Chỉ sửa câu đầu; câu sau giữ nguyên.

### 2.3. Ba mươi sáu key chỉ B có — kiểm chứng lại từng key, giữ nguyên 35, sửa 1 (856)

Tất cả 36 key đã đối chiếu lại với CSV3/JP: jp/tw/old_vn khớp tuyệt đối 36/36; mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (trừ 5 dòng rên ngắn thay toàn bộ — xem §5).

- **Romaji fallback (13):** 732 きゅあっ→"Kyua" ("Á a" mất âm kyua); 737 きゃふぅっ→"Kyafuu" (1+1=2 u); 738 ひゃぎゅっ→"Hyagyu" ("Á hự" mất âm); 739 ひゃん→"Hyan", ふぁん→"Fuan" (khôi phục ん); 741 ひゃっ→"Hya"; 745 か→"Ka" (tiền lệ 凪h2 2409 "Kahyu"); 753 ふああっ→"Fuaa" (2 a); 760 ひあんっ→"Hian" (khôi phục ん); 761 いぎゅっ→"Igyu" ("Í aaaaaa" bịa âm a; dấu `"` thừa sau い là lỗi phía JP); 777 くおっ→"Kuo" ("Ư ô" mất k); 787 か→"Ka"; 827 ぷあっ→"Pua" (ぷ là p, "phù" sai phụ âm đầu); 856 かっ→"ka" (xem dưới).
- **fa/fu (6):** 731 ふあっ→"phùa"; 743 ふあっ×2→"phùa" (2 chỗ); 812 ふぁっ→"Phà" + んううっ "ưm ư"→"ưm ưư" (2 ư); 813 ふぁ→"Phà" + あれほど "rõ ràng, là"→"đến mức đó……" (TW 「剛才——那麼的」 đồng ý; JP cụt câu, giữ …… không bịa phần kết); 816 dạng tách ふ――ぁ――ん "hu——a——ưm"→"phù——a——ưm" (theo quy ước "phù" cho hơi thở ふ trong file: 787, 812, 819, 821, 837, 968); 823 ふぁ cuối dòng→"phà"; 971 ふあっ cuối→"phùa" (ふっ――あっ giữa dòng giữ "phù——a" dạng tách).
- **Đếm vần (1 trong nhóm này, còn lại xem §2.1):** 819 ふぁああああん: 5 a đã đúng, chỉ phục hồi ん cuối ("phù a a a a a"→"phù a a a a an"), giữ dạng tách "phù".
- **Sai nghĩa (10, không tính 757/1429 ở §2.2):** 765 "trong" là bịa (てっ chỉ là âm ngắt, không phải "trong") + くぅ→"Kuu" (1+1=2 u); 802 もぉっ = もう "đã rồi" (TW 已經) — "cũng" lần 2 sai, "rồi" đúng; 1222 じくじく = đau âm ỉ/thốn, không phải "rỉ máu" (TW 備受折磨); 1321 愛しい = thân thương/đáng yêu, không phải "đáng thương" (đáng tội nghiệp); 1349 グラインド = xoay nghiến (grind), không phải "nắc" (TW 摩擦); 1364 くぱくぱ = mở ra khép lại liên hồi (TW 一張一合), không phải "mút mát"; 1410 わわ = bập bẹ/líu ríu (TW 口齒不清), không chỉ "đáp lại"; 1836 ちゅぷっ = tiếng hôn/bật môi → "Chụt", không phải "Bóp"; 1878/1944 れるっ = tiếng liếm (cùng họ れろっ đã dịch "liếm" trong file), không phải "mút"; 1909 にゅっ = tiếng siết/nhóp, không phải "Ngoạm" (tiền lệ 1869 にゅっ→"Siết").
- **Độ dài SFX (3):** 1820 （ずぶううううううううううううううううっ） 16 âm う mà VN cũ "Phập" không kéo dài gì — ngoại lệ duy nhất trong cụm ず (1811: 17い→22p; 1826: 10お→11p; 1829: 2お→4p đều kéo dài) → "Phậpppppppppppppppppppp" (20 p, tỉ lệ 1,25× trong khoảng 1,1–1,5× của cụm; con số là ước lượng theo cụm, không phải công thức chính xác). 1824 （つぷうぅぅ） đuôi 3 nguyên âm mất hẳn → "Phậpppp" (4 p, theo 1829 2お→4p). 1844 ちゅううううう (5 âm う) không kéo dài → "chùn chụttttt" (5 t cố định, theo 1854/1857).
- **Gasp (1):** 783 — JP kết んぅ～っ!: っ cuối tuyệt đối, ~~ chỉ diễn ～～, っ mất hẳn → thêm Ư ("ưm~ !"→"ưm~Ư!"). A đã không sửa dòng này (cho rằng diễn rên lỏng lẻo là đủ); B sửa gasp cuối là đúng theo quy tắc gasp đã khóa, và nhất quán với 759 (cùng mẫu ～～っ cuối dòng → Ư). Các っ giữa dòng giữ nguyên theo tiền lệ ハチロク01 2319.
- **856 — SỬA LẠI FIX CỦA B (lỗi của B, bắt được khi đối chiếu):** B đọc "nha" trong VN cũ và sửa thành "ka". Nhưng VN cũ không có từ "nha" nào: chuỗi ký tự là `…haa——\nha——ha…` — chữ "n" đó là chữ n của ký tự ngắt dòng literal `\n`, tiếp theo là "ha" (はっ). B đã thay chuỗi con "nha"→"ka" ngay trên biểu diễn đó, để lại fix chứa dấu backslash thừa: `haa——\ka——ha` (backslash + "ka" — nếu áp nguyên sẽ lọt ký tự `\` vào game). Ý đồ của B thì đúng một nửa: JP dòng 2 là かっ――はっ―― (2 tiếng gasp), VN cũ diễn cả hai thành "ha——ha" — tiếng đầu (かっ) sai phụ âm đầu, tiếng sau (はっ) đúng. Fix đã sửa: thay tiếng "ha" đầu dòng 2 (かっ) bằng "ka", giữ tiếng "ha" sau (はっ), giữ ngắt dòng của VN cũ: 「Sướng——quá, nóng——quá——haa——\nka——ha——bụng——tử cung——bị chạm, vào」. Đã kiểm chứng: fix chỉ còn đúng 1 backslash, là ký tự ngắt dòng literal `\n` của VN cũ (không còn backslash thừa); độ tương đồng với VN cũ 0,98.

## 3. Chi tiết từng bản sửa (bảng đầy đủ)

Mỗi dòng: key — nhân vật — JP (rút gọn) — VN cũ → VN mới. Toàn văn fix nằm trong JSON + khối TOML (§7).

### 3.1. Gasp っ (12)

| Key | Nhân vật | JP | Cũ → Mới |
|---|---|---|---|
| 477 | 双鉄 | 「っ――」 | 「っ——」 → 「Ư——」 |
| 783 | ハチロク | …んぅ～っ！ | …ưm~ ! → …ưm~Ư! |
| 804 | 双鉄 | 「っ！」 | 「っ!」 → 「Ư!」 |
| 807 | ハチロク | 「っ！！！！！！！！！！」 | 「っ!!!!!!!!!!」 → 「Ư!!!!!!!!!!」 |
| 814 | ハチロク | 「っ！（ごくっ）」 | 「っ! （Ực）」 → 「Ư! （Ực）」 |
| 974 | 双鉄 | 「っ！」 | 「!」 → 「Ư!」 |
| 975 | 双鉄 | 「っ！！」 | 「っ!!」 → 「Ư!!」 |
| 976 | ハチロク | 「っ！！！」 | 「っ!!!」 → 「Ư!!!」 |
| 978 | 双鉄 | 「っ！？」 | 「っ!?」 → 「Ư!?」 |
| 1433 | monologue | …欲望が――っ！？ | …đó——!? → …đó——Ư!? |
| 1444 | monologue | …無――っ！！ | …tôi——!! → …tôi——Ư!! |
| 1842 | 双鉄 | （…あるものか――っ！） | （…chứ——!） → （…chứ——Ư!） |

### 3.2. Romaji fallback + fa/fu + đếm vần (13 + 6 + 4 + 7 hỗn hợp)

- 731 (fa-fu): ふあっ "phù a"→"phùa". 732 (romaji): きゅあっ "Á a"→"Kyua". 736 (romaji+vowel): ひぎゅっ "Hí gư"→"Higyu", きゅぅ×7 "kiuuuuuuu"→"kiuuuuuuuu" (8 u). 737: きゃふぅっ "Á phù"→"Kyafuu". 738: ひゃぎゅっ "Á hự"→"Hyagyu". 739: ひゃん "Á"→"Hyan", ふぁん "phù……a"→"Fuan". 741: ひゃっ "Á"→"Hya". 743 (fa-fu): ふあっ×2 "Huaa…huaa"→"phùa…phùa". 745: か "A"→"Ka". 753: ふああっ "huaa"→"Fuaa". 759 (fa-fu+vowel+gasp): ふあっ "phù a"→"phùa", んくぅぅぅ "kuuu"→"kuuuu" (4 u), thêm Ư cuối. 760: ひあんっ "Hí a"→"Hian". 761: いぎゅっ "Í aaaaaa"→"Igyu". 763 (fa-fu+gasp): ふ――あっ "Hu——a"/"Fu——a"→"Phù——a" (tiền lệ 837/968), thêm ƯƯ cuối. 777: くおっ "Ư ô"→"Kuo". 787: か "A"→"Ka". 796 (fa-fu): ふぁっ "A"→"Phà". 812 (fa-fu+vowel): ふぁっ "Phù a"→"Phà", んううっ "ưm ư"→"ưm ưư". 813 (fa-fu+meaning): ふぁ "Phù"→"Phà", あれほど "rõ ràng, là"→"đến mức đó……". 816 (fa-fu): ふ――ぁ――ん "hu——a——ưm"→"phù——a——ưm". 819 (vowel): ふぁああああん "phù a a a a a"→"phù a a a a an" (phục hồi ん). 823 (fa-fu): ふぁ cuối dòng "phù."→"phà.". 827 (romaji): ぷあっ "phù a"→"Pua". 842 (romaji+vowel): んゅ "Ưm"→"Nyu", 18 âm a mirror đúng nhóm ぁ/あ (3+4+6+5). 843 (vowel): 31 u→17 u (1+16). 844 (vowel): きゅうう "kiuu"→"kiuuu" (3 u), ん×4 "Ưm ưm ưm"→đủ 4 (Ưm + 3×ưm). 845 (vowel): んゆぅ "yuuuu"→"yuu" (2 u). 856 (romaji): かっ "ha" (đầu dòng 2)→"ka" (xem §2.3). 971 (fa-fu): ふあっ cuối "phù a"→"phùa".

### 3.3. Đại từ (5) — xem §2.2

799, 863, 865, 881, 947: Soutetsu "anh"→"tôi" với Hachiroku.

### 3.4. Sai nghĩa (13) — xem §2.2, §2.3

757 (ひまっ→"Hí ma"), 765 (bỏ "trong" bịa, くぅ→"Kuu"), 802 (もぉっ "cũng"→"rồi"), 1222 (じくじく "rỉ máu"→"âm ỉ"), 1321 (愛しい "đáng thương"→"thân thương"), 1349 (グラインド "nắc"→"xoay nghiến"), 1364 (くぱくぱ "mút mát"→"mở ra khép lại"), 1410 (わわ "đáp lại"→"líu ríu đáp lại"), 1429 (phản thực tại, xem §2.2), 1836 (ちゅぷっ "Bóp"→"Chụt"), 1878/1944 (れるっ "mút"→"liếm"), 1909 (にゅっ "Ngoạm"→"Siết").

### 3.5. Thuật ngữ + typo (2)

- 1371: 御一夜 "Ohimitera"→"Ohitoyo" (lần duy nhất 御一夜 trong file).
- 1382: ký tự Hán 烈 lọt vào VN "mãnh烈"→"mãnh liệt" (quét cơ học: chỉ 1 ký tự CJK trong VN toàn file).

### 3.6. Độ dài SFX (3)

1820 (16う→20p), 1824 (3 âm→4p), 1844 (ちゅううううう→"chùn chụttttt", 5 t) — xem §2.3.

## 4. Rà soát chéo với sweep gasp

Sweep có đúng 14 mục cho file này (đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`):

| Key | Loại sweep | Kết quả hợp nhất |
|---|---|---|
| 1433, 1444, 1842, 763 (phần cuối) | lost-gasp-trailing | Áp nguyên (4 dòng) |
| 477, 804, 807, 814, 975, 976, 978 | raw-tsu | Áp nguyên (7 dòng) |
| 974 | lost-gasp-whole | Áp nguyên (1 dòng) |
| 759 | already-rendered | Sửa lại: っ cuối sau ～～ mất hẳn → thêm Ư (xem §2.1) |
| 783 | needs-file-audit | Sửa gasp cuối (thêm Ư) sau khi kiểm không lệch dòng (xem §2.3) |

Tổng: 12/12 fix sweep áp nguyên sau kiểm chứng + 2 mục sweep sửa lại theo quy tắc gasp đã khóa. Audit tìm thêm 51 dòng sweep không có (65 − 14 mục sweep).

## 5. Đã kiểm tra, giữ nguyên (không sai)

- **Đại từ Soutetsu:** đã quét toàn file (chuẩn hoá `\n`): chỉ 5 dòng "anh" tự xưng, đã sửa hết (§2.2). "Em" trong thoại Soutetsu đều là gọi Hachiroku — đúng. Độc thoại "tôi" nhất quán; "mình" trong độc thoại đều là phản thân/sở hữu/thành ngữ ("tự mình" 1443, "của chính mình" 1466, "bằng môi mình" 1527, "của mình" 1495/1558, "một mình" 1404/1488, "ngâm mình" 1648, "tắm mình" 1700) hoặc "mình" số nhiều trong mệnh đề phụ (1580) — giữ. Ngoại lệ đúng quy tắc: 1845 「（ああ……僕は――泣いているのか）」 → "（Aa……mình đang——khóc sao）" — tự vấn cảm xúc trong nội tâm, đúng ngoại lệ "mình". 1402 "mình lại khóc" giữ: JP không nêu chủ ngữ, TW mơ hồ, Soutetsu có khóc trong cảnh này (1660) — không đủ căn cứ đổi thành "em".
- **885 — hoàn thiện câu cụt, giữ:** JP cụt ở tiểu từ を; "em muốn ngài" là cách hoàn thiện suy từ ngữ cảnh, không phải bịa thêm nghĩa mới.
- **694/773/813 — câu cụt giữ (trừ phần 813 đã sửa ở §3.2):** 694 「一人で――イク、など」 → "lên đỉnh——một mình, thì."; 773 「はしたなくっ」 → "thế này." — đều là cách diễn câu JP cụt, không sai nghĩa rõ ràng.
- **939 — "vú em" giữ:** JP mơ hồ (ngực của ai), nhưng Soutetsu là nam, Hachiroku là nữ — "đang chùn chụt——vú em" là cách đọc duy nhất hợp lý.
- **783 (phần còn lại):** しょっ→"ức" và りゅっ bị lược là cách diễn rên ngắt quãng lỏng lẻo, khớp TW ("慢——慢一點!") — giữ, chỉ sửa gasp cuối.
- **"huaa" (692, 743) — đã xử lý trong audit này:** 692 → "phùa" (§2.1); 743 → "phùa"×2 (§3.2). Không còn dòng "huaa" tồn đọng trong bộ hợp nhất.
- **SFX trong ngoặc đơn — các dòng đã kéo dài đúng tỉ lệ giữ nguyên:** 1811 (17い→22p), 1826 (10お→11p), 1829 (2お→4p), 1854/1857 (ちゅうう→5t cố định), 1866 (2お→5t), 1930/1941 (kéo dài đúng) — giữ.
- **761** — dấu `"` thừa sau い là lỗi phía JP, không phải lỗi VN.
- **Lỗi phía JP khác (không tính sai):** 1596 ももはや (lỗi đánh máy JP: も+もはや). 1457/1662 ký tự �� chỉ xuất hiện trong CSV3/work-file, TOML JP sạch nên VN đúng.
- **Trùng VN SFX:** （Phập）×3, （Chụt）×2, （Siết chặt!）×2, 「Khục!」×2, （Phụt! Phụt! Phụt! Phụt!）×2, （Tuốt——tuốt——tuốt——tuốt——）×2 — đều là cùng 1 từ SFX cho các JP khác nhau nhưng cùng âm thanh, không phải lệch dòng hay nhiễm chéo.
- **Diff-sanity:** mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa; 5 ngoại lệ có lý do (toàn bộ dòng rên ngắn bị mất âm, thay cả dòng): 737 「Á phù!!!」→「Kyafuu!!!」 (0,48), 761 「Í aaaaaa!?」→「Igyu!?」 (0,40), 777 「Ư ô!!」→「Kuo!!」 (0,57), 796 「A」→「Phà」 (0,50), 1820 「（Phập!!!）」→「（Phậpppppppppppppppppppp!!!）」 (0,49, kéo dài theo cụm ず). Không có fix viết lại lớn nào khác.

## 6. Cấu trúc

- **0 lệch vị trí, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng mồ côi, 0 chưa dịch, 0 trùng khóa.** JP/TW đồng ý tốt toàn file (chỉ 2 chỗ JP thắng TW: 757, 1429).
- CSV3: 1 set duy nhất cho file này (435 dòng, 0 trùng key, 0 VN trống, 0 VN==TW). TOML `[script]` 435 khóa khớp CSV3 435/435, giá trị VN khớp phẳng 435/435 (sau chuẩn hoá `\n` ↔ khoảng trắng).
- TOML md5 `826355d088615a39f35716717fda637e`; 1 bản duy nhất toàn dự án (không có file trùng md5). UTF-8 BOM + CRLF (889 dòng). `[info]` rỗng, `[selections]` rỗng, `[characters]` {1128: Hachiroku, 1244: Soutetsu}. Không thẻ %l, không [ruby] trong file.
- Không thuật ngữ đã chốt nào khác trong JP (đã quét: 0 帝鉄/湯医/電車姫/乗務鞄/運転鞄/運転士鞄/乗員/日ノ本/宮司/整備体/運転ボディ/まいてつ/市電/エアクラ/砂撒き/帝大/小畑/杜氏/堰).

## Kiểm chứng

- JSON 65 mục dạng chuẩn (list of dicts, khóa chuỗi: key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn/character khớp CSV3 tuyệt đối 65/65 (lấy trực tiếp từ CSV3; hai bộ gốc cũng khớp tuyệt đối nên không mục nào bị loại vì sai nguồn).
- Khối TOML `[script]` 65 khóa, parse OK bằng tomllib, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; fix giữ `\n` literal của VN cũ, không thêm `\n` mới; backslash chỉ xuất hiện trong `\n` ngắt dòng — xem ghi chú parent bên dưới).
- Lượt soát 2 (đối chiếu hợp nhất): **65/65 tái kiểm chứng, 0 bỏ, 1 sửa nội dung** (763: "Hu——a"/"Fu——a" → "Phù——a" theo tiền lệ 837/968) + **1 sửa lỗi kỹ thuật của B** (856: fix chứa backslash thừa `\ka` → "\nka", giữ ngắt dòng của VN cũ). Không có dòng nào không chắc cần chờ Hieu ngoài các cờ ở dưới.
- **Ghi chú parent (kiểm chứng gộp 21/11 ~06:35):** agent đối chiếu đã chuẩn hoá sai — chuyển `\n` literal của VN cũ thành khoảng trắng trong 30 fix, trái brief (CSV3 là chuẩn cho fix list; "không dùng `\n` thủ công" nghĩa là không thêm ngắt dòng mới, không phải xoá ngắt dòng sẵn có) và trái tiền lệ các file đã gộp (giữ `\n` 123/123). Parent đã khôi phục `\n` ở cả 30 fix: 24 lấy nguyên fix của B (B giữ đúng `\n` của VN cũ; đã kiểm chứng fix hợp nhất trước đó == fix B sau khi đổi `\n`→khoảng trắng, số lượng `\n` khớp VN cũ), 6 khôi phục theo vị trí trong VN cũ (757, 763, 856, 865, 881, 1429 — mỗi dòng đúng 1 `\n`, vị trí không mơ hồ). Khối TOML đã build lại từ JSON đã sửa (65 khóa, parse OK, 0 sai lệch). Sau khôi phục, mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (trừ 5 dòng rên ngắn thay toàn bộ đã nêu ở §5). Không sửa nào bị loại; tổng số vẫn 65.

## Cờ cho Hieu (không tự quyết)

- **Họ れる/るっ/れろ (1878, 1944 → "liếm" theo file):** đề xuất "rộp" cho họ này vẫn đang chờ Hieu — nếu chốt "rộp" thì 2 dòng này + các dòng れろっ/れるっ trong file sẽ đổi theo (đợt thống nhất).
- **Độ dài lặp phụ âm SFX (1820: 20 p):** con số 20 p là ước lượng theo cụm ず trong file (tỉ lệ 1,1–1,5×), không phải công thức chính xác như công thức nguyên âm — vòng moan-fix có thể rà lại.
- **Các dòng fa/fu và ひあ/ひゃ đã sửa bằng romaji trong audit này** (732, 737, 738, 739, 741, 753, 760, 761, 777, 827, 856; 731, 743, 796, 816, 823, 971 giữ "phà"/"phùa") thuộc diện đợt thống nhất rà lại theo quy tắc romaji fallback 21/11 — đã áp đúng quy tắc từng dòng, không cần quyết thêm.
- B19 in-game check (Paulette 13 key 1596) vẫn park toàn dự án; file này không có thẻ %l nên không bị ảnh hưởng.

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
477 = "「Ư——」"
692 = "「Không! Không được——đâu——Ngài Soutetsu——phùa!\\nEo ngài, cứ ngoáy, ngoáy——mông em——em, bị nong rộng ra, mất」"
731 = "「Hí a——a——a——phùa——a!!」"
732 = "「Kyua! A, ưm——vú——a\\nsướng……lắm, ạ——phu, quân——」"
736 = "「Higyu!? A——hí, kiuuuuuuuu!!」"
737 = "「Kyafuu!!!」"
738 = "「Hyagyu!? A——khít——khít quá——ưm, a!!\\nCô, bé——hà, a——bị khoét, bị khoét sâu quá!」"
739 = "「Hyan! Lại nữa——Fuan!!! Ưm……\\nvú……tê rần——tê dại——sướng, quá.」"
741 = "「Hya!」"
743 = "「Hya! A! Ưm!! phùa——hakyu——\\nphù——phùa! A! A! Aaa!!!!」"
745 = "「Ka……ha……a——ư——ưm——như——vậy,\\nđột, nhiên——đột——nhiên——ưn kyuuu!!?」"
753 = "「Hí——kyu——Fuaa! A! Mông, mông em!\\nCháy, mất——chặt——quá——nóng——phù!」"
757 = "「Hí a——a——a——không——được đâu!\\nHí ma——b, bây giờ——vẫn còn——rất nhạy cảm, ạ!」"
759 = "「Hí a! Ưm——mông——phùa——mông, cũng……\\nmà——bây giờ, thì……ưm——ưm kuuuu~~Ư」"
760 = "「Hian!!!」"
761 = "「Igyu!?」"
763 = "「Hiu!? Phù——a!? Ng, Ngài Soutetsu!\\nĐợi——đợi——đợi đã——! ~~~~ƯƯ!!!」"
765 = "「Hí!? A——tai——ưm——tai của, em——\\nlưỡi của phu, quân——đang,……đút vào——Kuu.」"
777 = "「Kuo!!」"
783 = "「A——hi——ức——khục——ưm a——\\nchậm——chậm——lại, đi——ưm~Ư!」"
787 = "「Ka……phù——a!」"
796 = "「Phà」"
799 = "「Aa——Tôi sẽ xuất tinh——vào sâu nhất——vào tử cung——của em」"
802 = "「A kiu! Ưm! Hà——sướng quá! Phù, a——\\nvú, cũng——cô, bé——rồi!!!!」"
804 = "「Ư!」"
807 = "「Ư!!!!!!!!!!」"
812 = "「Phà……phù……hà……a……mông, cũng……bây giờ, thì\\n……vừa mới……lên đỉnh……xong……nên rất nhạy cảm……ưm ưư!」"
813 = "「Phà……a——như thế……dễ……chịu quá……\\nlưỡi……của ngài……Soutetsu……ban nãy——đến mức đó……」"
814 = "「Ư! （Ực）」"
816 = "「Ưm——a……Ngài……Soutetsu……phù——a——ưm,\\nKhông sao……đâu……ạ? Ngoan nào……nhé? Ngoan nào……」"
819 = "「Ưm……kiu——phù a a a a an!!!」"
823 = "「Ưm……a——lưỡi……ấm quá……ưm——\\na……sau, gáy……ưm——nhột quá——phà.」"
827 = "「Ưm……chụt——Pua——a……Ngài Soutetsu?」"
842 = "「Nyu——aaaAAAAaaaaaaAAAAA!」"
843 = "「Ưn kyuuuuuuuuuuuuuuuuu!!」"
844 = "「Ưm kiuuu ưm ưm ưm!!!」"
845 = "「Ưm yuu!!!!」"
856 = "「Sướng——quá, nóng——quá——haa——\\nka——ha——bụng——tử cung——bị chạm, vào」"
863 = "「Bây giờ không sao rồi. Cả tôi, và cả em nữa」"
865 = "「Ép buộc em phải trả lời——\\nTôi mới là một gã đàn ông đê tiện và dâm đãng hơn nhiều đấy.」"
881 = "「Hãy dùng bàn tay đó, làm tôi xuất tinh đi.\\nHãy vắt kiệt——toàn bộ sự vẩn đục của tôi ra đi」"
947 = "「Suzu——Tôi yêu em——yêu em——yêu em!!」"
971 = "「Ngài Soutetsu? ——Ưm!? A……chụt——ưm——\\nphù——a——ưm——a——phùa! A!」"
974 = "「Ư!」"
975 = "「Ư!!」"
976 = "「Ư!!!」"
978 = "「Ư!?」"
1222 = "Vì vậy, đôi khi, vết thương lại xé toạc lớp vảy,\\nvà âm ỉ hành hạ chúng tôi."
1321 = "Đáng yêu, thân thương, xinh đẹp.\\nChính vì thế, tôi càng muốn làm em rối tung lên."
1349 = "Sự siết chặt vẫn mãnh liệt như vậy, và dù là thế,\\nem vẫn tiếp nhận trọn vẹn những cú xoay nghiến của tôi."
1364 = "Lỗ hậu siết chặt mãnh liệt đến mức chỉ cần đầu ngón tay cũng cảm thấy đau,\\nđang siết chặt lấy phần côn thịt của tôi, mở ra khép lại liên hồi."
1371 = "Lễ hội hoài cổ Taisho Ohitoyo."
1382 = "Vừa nghĩ đến đó, tình yêu trong tôi lại càng bùng cháy mãnh liệt.\\nThật đáng yêu."
1410 = "Dù đã biết trước sự trao đổi đó, nhưng Suzu vẫn trông thật hạnh phúc,\\nthật hạnh phúc——với khuôn mặt tan chảy, em líu ríu đáp lại tôi!"
1429 = "Khoảnh khắc ngọt ngào này, có lẽ tôi đã mãi mãi chẳng bao giờ được nếm trải.\\nNhững thứ đã mất đi……dù cho vết thương có mãi mãi không thể phai mờ, nhưng——"
1433 = "Tôi muốn cứ thế này mà chìm đắm mãi. Tôi muốn trở thành em bé của Suzu.\\nCái ham muốn ngu ngốc đó——Ư!?"
1444 = "Tôi không thể đút côn thịt vào tiểu huyệt quen thuộc một cách trơn tru.\\nSuzu đang lên đỉnh thậm chí còn chẳng còn tâm trí để dẫn dắt tôi——Ư!!"
1820 = "（Phậpppppppppppppppppppp!!!）"
1824 = "（Phậpppp）"
1836 = "（Nhóp nhép! Phập! Chụt! Chụt!）"
1842 = "（Làm gì có chuyện——đột nhiên chứ——Ư!）"
1844 = "（Mút——chùn chụttttt——bật nảy!）"
1878 = "（Liếm——liếm——liếm dài——ngoạm!）"
1909 = "（Siết——phập——phập, phập——phập）"
1944 = "（Liếm——liếm——liếm——liếm）"
```

## Kết bài

File ハチロクh7_レトロモダンメイクラヴ.txt.toml: 435 dòng đã đọc hết (qua hai audit song song), **65 dòng sai (14,9%)** sau khi hợp nhất — romaji 13, sai nghĩa 13, gasp 12, fa/fu 6, đại từ 5 (Soutetsu "anh"→"tôi" với Hachiroku, áp quy tắc đã chốt), đếm vần 4, độ dài SFX 3, hỗn hợp 7, thuật ngữ 1 (Ohimitera→Ohitoyo), typo 1 (ký tự Hán 烈 lọt vào VN). Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Hai audit gốc khớp nhau 22 key, khác fix 10 key — đã giải quyết từng key theo JP/TW và tiền lệ trong file; phát hiện và sửa 1 lỗi kỹ thuật của audit B (856: fix chứa backslash thừa do đọc nhầm ký tự ngắt dòng `\n` thành từ "nha"). Lượt soát 2 (đối chiếu hợp nhất): 65/65, 0 bỏ, 1 sửa nội dung (763) + 1 sửa lỗi kỹ thuật (856) + parent khôi phục `\n` ở 30 fix (xem mục Kiểm chứng). JSON + khối TOML đã kiểm chứng parse, 0 sai lệch. Cờ cho Hieu: đề xuất "rộp" cho họ れる/るっ/れろ (1878, 1944) vẫn đang chờ; số 20 p ở 1820 là ước lượng theo cụm, vòng moan-fix có thể rà lại.
