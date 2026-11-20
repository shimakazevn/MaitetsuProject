# -*- coding: utf-8 -*-
"""Generate audit-hachiroku14-hashi-REVIEW.md (§3 from JSON + hand-written reasons)."""
import json

D = json.load(open('audit-hachiroku14-hashi-wrong.json', encoding='utf-8'))
E = {e['key']: e for e in D}

REASON = {
# gasp
'1463': "Gasp cuối dòng っ bị mất — JP kết bằng ――っ！！？, TW có 啊, VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-trailing).",
'1614': "Gasp đầu dòng っ！ và gasp cuối ――っ！！？ đều bị mất — VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-trailing). そうかっ giữa dòng là っ nhấn mạnh gắn với từ nội dung, giữ nguyên theo sweep.",
'1834': "Gasp cuối dòng っ――っ! bị mất — VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-trailing).",
'1910': "Gasp nguyên dòng っ! bị mất — VN chỉ còn '!'. Áp nguyên sweep (lost-gasp-whole).",
'1911': "Gasp nguyên dòng っ!!! bị mất — VN chỉ còn '!!!'. Áp nguyên sweep (lost-gasp-whole).",
'1912': "Gasp nguyên dòng っ!!? bị mất — VN chỉ còn '!!?'. Áp nguyên sweep (lost-gasp-whole).",
'1915': "Gasp nguyên dòng っ!? bị mất — VN chỉ còn '!?'. Áp nguyên sweep (lost-gasp-whole).",
'1924': "Gasp nguyên dòng っ! ×2 (hai người cùng thốt lên) bị mất — VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-whole).",
'2195': "Gasp cuối dòng ―――っ!? bị mất — VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-trailing).",
'2398': "Gasp cuối dòng ――っ!? bị mất — VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-trailing).",
'2746': "Gasp cuối dòng ――っ! bị mất — VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-trailing).",
'1914': "Sweep đánh dấu needs-file-audit — tự giải quyết trong audit: dòng đầu là gasp nguyên dòng っ!!?, VN chỉ còn '!!?' nên thêm Ư; dòng sau JP わたくしが và TW '我去' đều cụt câu, VN 'Em sẽ' giữ đúng dạng cụt — không bịa thêm phần còn lại.",
# pronoun dialogue
'1551': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku; Hachiroku gọi Soutetsu là 'ngài Soutetsu' 双鉄様).",
'1547': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1737': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1454': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1714': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku). 'Master' giữ nguyên (thuật ngữ dự án cho マスター).",
'1541': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1508': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku). 'Em' ở đây gọi Hachiroku, đúng.",
'1509': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1684': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1523': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1735': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1481': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1856': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1701': "Soutetsu tự xưng 'Em' khi nói với cả Hibiki + Mayami (câu trước 1835 gọi cả hai, 1631 Mayami đáp, 2244 cả hai cùng cười) — 'Em' sai cả hai chiều (với Hibiki là 'anh', với Mayami là 'tôi'); dạng xưng hô nhóm dùng 'tôi' theo tiền lệ Paulette 14 key 1544.",
'1893': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1890': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1622': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1821': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1836': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1542': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1900': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku). Cả 3 lần 'anh' đều là Soutetsu tự xưng.",
'1712': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku). Cả 5 lần 'anh' đều là Soutetsu tự xưng.",
'1686': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku). Cả 3 lần 'anh' đều là Soutetsu tự xưng.",
'1719': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
'1493': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku). Cả 2 lần 'anh' đều là Soutetsu tự xưng.",
'1505': "Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).",
# pronoun monologue
'2582': "Độc thoại người kể Soutetsu dùng 'anh' — quy tắc chung độc thoại là 'tôi' ('mình' chỉ cho tự vấn nội tâm); toàn file độc thoại dùng 'tôi' ở 245/248 dòng.",
'2741': "Độc thoại người kể Soutetsu dùng 'anh' — quy tắc chung độc thoại là 'tôi'; toàn file độc thoại dùng 'tôi' ở 245/248 dòng.",
'2140': "Độc thoại người kể Soutetsu dùng 'anh' — quy tắc chung độc thoại là 'tôi'; toàn file độc thoại dùng 'tôi' ở 245/248 dòng.",
# terminology
'2927': "Gloss 機関士 dùng 'nhân viên cơ vụ' — đó là gloss của 運転士, không phải 機関士; sửa về 'thợ lái đầu máy' theo thuật ngữ đã chốt + tiền lệ 日々姫09 (9 dòng).",
'2374': "Gloss 機関士 dùng 'nhân viên cơ vụ' — đó là gloss của 運転士; sửa về 'thợ lái đầu máy' theo thuật ngữ đã chốt + tiền lệ 日々姫09.",
'2678': "Hai gloss sai trong một dòng: 機関士 'nhân viên cơ vụ' → 'thợ lái đầu máy' (thuật ngữ đã chốt); 運転体 'kíp lái' → 'thân vận hành' (tiền lệ ハチロク14_凪 3983 / 日々姫09).",
'2368': "Gloss 機関士 dùng 'nhân viên cơ vụ' — đó là gloss của 運転士; sửa về 'thợ lái đầu máy' theo thuật ngữ đã chốt + tiền lệ 日々姫09.",
'2455': "Gloss 運転体 dùng 'kíp lái' — sửa về 'thân vận hành' theo tiền lệ ハチロク14_凪 3983 / 日々姫09.",
'2514': "Gloss 整備体 dùng 'thân chính' — sửa về 'thân bảo trì' theo thuật ngữ đã chốt.",
'2910': "Gloss 整備体 dùng 'thân chính' — sửa về 'thân bảo trì' theo thuật ngữ đã chốt.",
'2940': "Gloss キハ07 viết 'Kiha 07' — sai chính tả, cách viết chính thức của JR là 'KiHa' (tiền lệ 00common07, 日々姫10).",
'2258': "術仙炭鉱廃駅 viết 'Jutsusen' — thiếu gạch nối so với dạng đã chốt 'Jutsu-sen'. Đây là dòng 術仙 duy nhất trong file.",
'1815': "Fukami gọi Seki (早瀬堰) là 'ông nội' — theo quyết định đã chốt 20/11, Seki là ông ngoại của Fukami (mẹ Fukami là Midori; 08c 2456 Seki gọi Midori là 娘, 2086 gọi Fukami là 孫娘). Đây là dòng Seki thứ 6 tìm được trong audit (sau 4 dòng đã liệt kê + ハチロク07 2679) — sửa trong audit theo đúng tiền lệ 2679. Cảnh này: Seki vừa nói với Fukami (1798), dặn gọi điện cho Midori (1668), và đáp lời xin lỗi của Fukami (1455), nên người được gọi chắc chắn là Seki.",
# terminology (decided 21/11 ~01:51)
'1733': "御一夜 (địa danh) dùng 'Ohito' — sửa về 'Ohitoyo' theo thuật ngữ đã chốt (19/11) + furigana おひとよ. Quyết theo chỉ đạo mới của Hieu 21/11 01:51 (điều tra để quyết, không park) thay vì để lại đợt thống nhất.",
'1754': "Hai thuật ngữ sai trong một dòng: 湯医 dùng 'Yui' — JP mang furigana [ゆのい,1] nên đọc là 'Yunoi' theo thuật ngữ đã chốt; 御一夜 dùng 'Ohito' — sửa về 'Ohitoyo'. Quyết theo chỉ đạo mới của Hieu 21/11 01:51 (điều tra để quyết, không park).",
'2372': "御一夜駅 dùng 'ga Ohito' — sửa về 'ga Ohitoyo' theo thuật ngữ đã chốt (19/11) + furigana おひとよ. Quyết theo chỉ đạo mới của Hieu 21/11 01:51.",
'2355': "御一夜駅 dùng 'ga Ohito' — sửa về 'ga Ohitoyo' theo thuật ngữ đã chốt (19/11) + furigana おひとよ. Quyết theo chỉ đạo mới của Hieu 21/11 01:51.",
'1696': "御一夜 (tổ chức/địa danh) dùng 'Ohito' — sửa về 'Ohitoyo' theo thuật ngữ đã chốt (19/11). Quyết theo chỉ đạo mới của Hieu 21/11 01:51. (Chỉ tên công ty 'Đường sắt Ohito' ở 2748 là giữ lại chờ Hieu quyết — xem §5.)",
'1200': "御一夜 (thị trấn) dùng 'Ohito' — sửa về 'Ohitoyo' theo thuật ngữ đã chốt (19/11) + furigana おひとよ. Quyết theo chỉ đạo mới của Hieu 21/11 01:51.",
'1777': "御一夜 dùng 'Ohito' — sửa về 'Ohitoyo' theo thuật ngữ đã chốt (19/11). Quyết theo chỉ đạo mới của Hieu 21/11 01:51.",
# meaning
'2948': "VN bịa thêm 'trong đêm tối' (JP 手探り và TW 摸索 đều không có) và dịch これは thành mảnh câu dở dang 'Thế này thì' — JP là một ý hoàn chỉnh ('đây đúng nghĩa đen là mò mẫm'). Sửa về đúng JP; 'mò mẫm' tự nó đã hàm ý dò dẫm trong tối.",
}

ORDER = sorted(E, key=lambda x: int(x))
KIND_VN = {'gasp': 'gasp', 'pronoun': 'đại từ', 'terminology': 'thuật ngữ', 'meaning': 'sai nghĩa'}

def esc(s):
    return s.replace('\\n', ' / ')

sec3 = ["## 3. Các lỗi đã sửa (59 dòng)\n"]
for k in ORDER:
    e = E[k]
    sec3.append(f"### {k} — {e['character']} — {KIND_VN[e['kind']]}")
    sec3.append(f"**JP:** {esc(e['jp'])}")
    sec3.append(f"**TW:** {esc(e['tw'])}")
    sec3.append(f"**Cũ:** {esc(e['old_vn'])}")
    sec3.append(f"**Mới:** {esc(e['fix'])}")
    sec3.append(REASON[k])
    sec3.append("")
sec3_text = "\n".join(sec3)

tomlblock = open('audit-hachiroku14-hashi-tomlblock.txt', encoding='utf-8').read().rstrip('\n')

review = f"""# Audit ハチロク14 — ハチロク14_橋.txt.toml

**Ngày kiểm toán:** 21/11/2026
**Tệp TOML:** `01_Hachiroku/#U30cf#U30c1#U30ed#U30af14_#U6a4b.txt.toml` — md5 `3d12a51d767e4c69da087e7eb161c54f`, BOM + CRLF, `[selections]` rỗng, **không có bản sao trùng** (chỉ 1 copy trong 227 tệp TOML; 11 nhóm trùng của dự án không chứa file này).
**Nguồn CSV:** "Trang tính 3" — **1 set duy nhất** (476 dòng, 0 key trùng, 0 VN rỗng) — không có bẫy dual-set. TOML khớp CSV3 tuyệt đối về key (476/476) và nội dung (203 khớp phẳng + 273 khớp sau khi chuẩn hoá `\\n`, 0 khác biệt thực chất — toàn bộ là hiện tượng gộp `\\n` trong TOML-2). CSV3 là bản chuẩn cho fix list.
**Cơ sở totals (đã kiểm chứng):** ROUTE-AUDIT.md hiện tại là **136 file / 6.200 dòng sai** — khớp đúng cơ sở 136/6.200 trong lệnh giao; snippet dùng 136/6.200 + 59 = 137/6.259.
**Kết quả: 59/476 dòng sai (12,4%), 0 dòng chưa chắc chắn, 0 dòng lệch vị trí, 0 chuỗi xoay, 0 nhiễm chéo file, 0 dòng chưa dịch, 0 key trùng.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| Đại từ Soutetsu "anh"/"em"→"tôi" với Hachiroku (thoại 26 + độc thoại 3) | 29 |
| Gasp っ bị mất | 12 |
| Thuật ngữ/gloss %l | 17 |
| Sai nghĩa/bịa thêm | 1 |
| **Tổng** | **59** |

**Theo loại dòng:** thoại 43/228 sai (18,9%), độc thoại 18/248 sai (7,3%). **Theo nhân vật:** 双鉄 (Soutetsu) 34/107, monologue 18/248, ハチロク (Hachiroku) 4/64, ふかみ (Fukami) 1/3, 日々姫 (Hibiki) 1/3, 元忠 (Mototada) 1/18; 凪, 稀咲, 蓑笠, 真闇, 早瀬堰 0 sai.

File này sạch về cấu trúc — 0 lệch vị trí, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng. Lỗi tập trung ở một lỗi hệ thống duy nhất: Soutetsu tự xưng "anh" với Hachiroku ở 29/59 dòng sai (thoại 26 + độc thoại 3) — Gemini dịch nhất quán sai quy tắc đã chốt trong toàn bộ cảnh tình cảm cuối file (từ 1454 đến 1900), trong khi phần còn lại của file Soutetsu đã dùng đúng "tôi" ở độc thoại (245/248 dòng) và gọi Hachiroku là "em" đúng ở mọi chỗ. Các lỗi còn lại: 12 gasp (11 từ sweep + 1 needs-file-audit tự giải quyết), 17 gloss thuật ngữ (機関士/運転体/整備体/KiHa/Jutsu-sen/Seki/御一夜/湯医), 1 bịa thêm. **Thay đổi trong lúc audit:** theo chỉ đạo mới của Hieu 21/11 01:51 ("điều tra để quyết, không park phán đoán cho Hieu"), 7 dòng 御一夜/湯医 đã được quyết và sửa trong audit thay vì để lại đợt thống nhất (xem §3: 1733, 1754, 2372, 2355, 1696, 1200, 1777); chỉ tên công ty "Đường sắt Ohito" ở 2748 là giữ lại vì đó là quyết định đặt tên riêng của Hieu (xem §5).

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục. TOML md5 `3d12a51d767e4c69da087e7eb161c54f`, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng trong 227 tệp.
- **CSV vs TOML:** CSV3 1 set duy nhất, 476 dòng, 0 key trùng, 0 VN rỗng. TOML script 476 khóa, khớp CSV3 476/476 về key; giá trị VN: 203 khớp tuyệt đối + 273 khớp sau khi chuẩn hoá `\\n`, 0 khác biệt thực chất. CSV3 là bản chuẩn cho fix list.
- **Sweep っ (gasp):** kiểm tra trực tiếp sweep-raw-gasp-wrong.json — file này CÓ 12 mục (11 fix + 1 needs-file-audit 1914). Áp nguyên 11 fix sweep + tự giải quyết 1914 (xem §3). Quét bổ sung toàn bộ 185 dòng JP chứa っ: **không còn gasp nào sweep bỏ sót** (khác ふかみh2 bắt thêm 7 — file này sweep đã bao đủ).
- **Thẻ %l:** số lượng thẻ JP = VN ở mọi dòng — **0 thẻ thiếu dấu `;` đóng, 0 thẻ VN tự thêm, 0 thẻ thiếu**. Gloss sai chỉ là sai từ gloss (機関士/運転体/整備体/KiHa), đã sửa trong fix list.
- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng: 0), không có VN mồ côi (orphan: 0), không có key trùng, không có VN trùng nhau trong file (0 cặp trùng — không có bằng chứng lệch vị trí/xoay). Nội dung là một cảnh liên tục duy nhất (lái 8620 vượt bão qua cầu sông Kuma, về ga Ohito) — các key tuy không theo thứ tự câu chuyện nhưng dòng chảy liền mạch, không có dấu hiệu VN của dòng khác lọt vào.
- **Đại từ:** Soutetsu gọi Hachiroku là "em" đúng ở mọi chỗ (1876, 1882, 1636, 1520, 1539, 1517, 1515, 1892; "Em ấy" ngôi thứ ba ở 1545/1790 đúng); Hachiroku tự xưng "em" nhất quán; Soutetsu tự xưng "tôi" đúng ở độc thoại 245/248 dòng (3 dòng sai đã sửa) và ở mọi thoại không nằm trong cảnh tình cảm cuối file. Kisaki tự xưng "Con" với bố Mototada (1682, 1238, 1723, 1726, 1245) và "Tớ" với cả nhóm (1721, giữ — nhóm hỗn hợp, xem §6); Nagi dùng ウチ → "em" nhất quán (1750, 1843); Fukami gọi Seki "ông nội" đã sửa thành "ông ngoại" (1815, xem §3).
- **Thuật ngữ đã chốt:** エアクラ = "Aircra" đúng (2742); レイルロオド = "Railord" đúng (1705, 1717, 2137); 砂撒き gloss "phun cát" (2682, viết thường giữa câu, giữ); 共存 = "Cộng tồn" nhất quán 2 dòng (1225, 2742); 御一夜 = "Ohitoyo" và 湯医 = "Yunoi" đã sửa trong audit ở 7 dòng (1733, 1754, 2372, 2355, 1696, 1200, 1777) theo chỉ đạo mới của Hieu 21/11 01:51 — chỉ còn tên công ty "Đường sắt Ohito" ở 2748 giữ nguyên chờ Hieu quyết (xem §5); file không có 帝鉄/コン/宮司/小畑/冥国/冥軍/駿袋/日ノ本/乗務鞄/運転鞄/乗員/マスコン/回数券/定期券; không có dòng fa/fu hay ひあ/ひゃ nào — quy tắc romaji fallback cho tiếng rên (Hieu duyệt 21/11 ~01:56) không áp dụng cho file này.
- **Chỉ đạo mới trong lúc audit (MEMORY.md cập nhật 21/11 ~01:55):** Hieu khẳng định lại việc ủy quyền quyết định cho Muse ("điều tra để quyết, không park phán đoán cho Hieu") — chỉ các mục thực sự cần kiểm tra trong game (B19) hoặc sở thích cá nhân của Hieu mới được park. Áp dụng: 7 dòng 御一夜/湯医 quyết và sửa trong audit; 2748 (tên công ty) park với lý do nêu ở §5.

{sec3_text}
## 4. Rà soát chéo với sweep gasp

- Sweep có 12 mục cho file này: 11 fix (1463, 1614, 1834, 1910, 1911, 1912, 1915, 1924, 2195, 2398, 2746) — audit xác nhận cùng giá trị 11/11, áp nguyên; 1 needs-file-audit (1914) — audit tự giải quyết (chỉ thêm Ư vào dòng gasp, giữ nguyên dòng cụt sau).
- Quét bổ sung toàn bộ 185 dòng JP chứa っ: **0 gasp sweep bỏ sót**. Các っ còn lại đều đã được diễn hoặc là っ nhấn mạnh gắn với từ nội dung (xem §6).
- Ghi chú sweep: JP của sweep cho file này khớp JP bộ tốt (không có vấn đề stale-set như ふかみh2).

## 5. Thuật ngữ chờ đợt thống nhất (ghi nhận, không tính sai)

- **Tên công ty "Đường sắt Ohito" (1 dòng, giữ nguyên — park có lý do):** 2748 "Công ty Cổ phần Đường sắt Ohito". Đây là câu hỏi đặt tên riêng: "Đường sắt Ohito" xuất hiện 215 lần toàn dự án vs "Đường sắt Ohitoyo" 5 lần — chỉ Hieu mới quyết được có đổi tên công ty đường sắt không (cf. ROUTE-AUDIT). Theo chỉ đạo mới 21/11 01:51, đây thuộc diện "sở thích cá nhân của Hieu" nên được park, với lý do này.
- **Đã quyết và sửa trong audit (không chờ thống nhất):** 御一夜 (địa danh/trạm) → "Ohitoyo" 7 dòng (1733, 1754, 2372, 2355, 1696, 1200, 1777); 湯医 → "Yunoi" 1 dòng (1754, furigana ゆのい là bằng chứng quyết định); "Kiha 07" → "KiHa 07" (2940, sai chính tả theo quyết định 19/11); "Jutsusen" → "Jutsu-sen" (2258, dạng đã chốt); Seki "ông nội" → "ông ngoại" (1815, quyết định đã chốt 20/11).

## 6. Đã kiểm tra và không tính sai

- **Thán từ っ (えっ/なっ/いやっ/うおっ/うむっ):** 1598 "Hả!?", 1475/1476 "Cái gì!?", 2627 "Không!?", 2903 "(Không)", 1592 "Ua!?", 1628 "Ừm!" — sweep phân loại raw-tsu/already-rendered (tiền lệ 共通14 1443 うおっ raw-tsu; lr h3 1307 うむっ already-rendered); VN đã diễn được thán từ, giữ nguyên.
- **あっ―― bị cắt bởi gạch ngang:** 1602 "A——", 1603 "A——A" — gạch ngang đã diễn được sự ngắt tiếng; giữ nguyên theo tiền lệ ハチロク01 2319 (không thêm Ư).
- **っ nhấn mạnh gắn với từ nội dung:** 1851/1585 くそっ, 1645 よしっ, 1490 ですがっ, 1764 油切れかっ, 1878 これはっ, 1881 こそっ/ぞっ, 2656 くるっ, 1905 様っ, 1546 ハチロクっ, 1801 馬鹿者がっ, 1744 なのにっ――, 1679/1867/1676/1688/1852 (lắp bắp, gạch ngang đã diễn), 1639 はいっ, 1529 ましたっ, 1767 はいっ, 1640 痛かっ, 1842 大阿呆がっ, 1813 父さんっ, 1816 じいちゃんっ — đều là っ nhấn mạnh/cắt câu, không phải gasp; giữ nguyên.
- **SFX đã diễn:** 2925 (ざくっ→"Phập"), 2936, 2123 (ボっ→"Phụt!"), 2916, 2922 (パンっ→"Bốp!!!"), 2923/2924, 2917 (ぽかっ→"Bộp!"), 2926 (ズォボーッツ→"Xìiiiiiiiii"), 1196 (ぅはっ→"Ư hự!"), 1620 (くっ→"hự!"), 2272 (ぐ、と→"Ưực."), 1608 (はっ→"ha", んっ→"ưm"), 2846 (ほーーーっと→"Phùuu").
- **2475 視界をっ:** JP cụt câu (thiếu động từ); VN bổ sung động từ duy nhất có thể ("che khuất tầm nhìn") — không bịa thêm nghĩa mới, giữ nguyên.
- **1816 Nagi gọi Minokasa "Ông nội!?":** Minokasa không phải Seki; quyết định 20/11 chỉ đổi các dòng Seki — giữ nguyên.
- **1495 尻を拭う → "dọn dẹp rắc rối":** làm nhẹ cách nói tục nhưng giữ đúng nghĩa ("cha lo hậu quả cho con gái"); giữ nguyên.
- **1225/2742 共存 → "Cộng tồn":** nhất quán 2 dòng, giữ nguyên.
- **1633 おっと → "Ây da!":** cách diễn hợp lệ; "Ối" chỉ là đề xuất (tiền lệ h7 861), chưa phải quyết định chốt — giữ nguyên.
- **1721 Kisaki tự xưng "Tớ":** nói với cả nhóm hỗn hợp (Hibiki, Soutetsu, mọi người), không phải riêng Soutetsu hay Paulette nên không áp quy tắc "em với Soutetsu / tôi với Paulette" — giữ nguyên.
- **"mình" trong độc thoại:** 2247 "giống như mình", 2558 "Tôi nghĩ... mình cũng đã biết", 2797 "chính mình", 2184 "theo ý mình", 2275 "gồng mình", 2552 "lao mình ra", 2489 "cơ thể mình", 2589 "tay mình" — đều là "mình" ở vị trí tân ngữ/so sánh/quán dụng, không phải đại từ chủ ngữ độc lập; giữ nguyên (chỉ sửa "mình" làm chủ ngữ độc lập).
- **1703 "E, m và":** tách lắp bắp của "Em" (わた、くし), diễn đúng JP; giữ nguyên.
- **1175 "ông cháu":** diễn chung cho 祖父・孫 (Seki–Fukami), không nêu nội/ngoại; giữ nguyên.
- **2682 砂撒き gloss "phun cát":** viết thường vì ở giữa câu, đúng thuật ngữ đã chốt; giữ nguyên.

## 7. Lượt soát 2 và khối TOML

**Lượt soát 2: 59/59 tái kiểm chứng, 0 bỏ, 1 sửa + 7 thêm.** Lỗi sửa ở lượt 2: 1900 — lần build đầu chỉ thay "Anh" hoa mà sót "anh" thường trong "Nhưng anh muốn nhiều hơn thế" (do `\\n` literal trong CSV3 làm regex quét máy bỏ sót dòng này ở lượt 1); đã sửa thành "tôi" và kiểm tra lại toàn bộ bằng quét chuẩn hoá `\\n`. 7 dòng thêm ở lượt 2: 1733, 1754, 2372, 2355, 1696, 1200, 1777 (御一夜/湯医) — quyết và sửa theo chỉ đạo mới của Hieu 21/11 01:51, mỗi dòng đã đọc lại JP/TW trước khi chốt.

**Kiểm chứng cơ học:** JSON 59 mục (khóa dạng chuỗi); jp/tw/old_vn khớp CSV3 59/59; mỗi fix chỉ khác old VN ở đúng chỗ sửa (đã kiểm tra diff từng dòng — các fix nhiều chỗ thay chỉ là "anh"→"tôi" lặp lại hoặc đổi từ gloss dài ngắn khác nhau trong cùng một thẻ %l); khối TOML dưới đây parse OK bằng tomllib, 59 khóa, 0 sai lệch giá trị so với JSON.

{tomlblock}

Kết bài
"""

with open('audit-hachiroku14-hashi-REVIEW.md', 'w', encoding='utf-8') as f:
    f.write(review)
print('review written, chars:', len(review))
# sanity: ends with Kết bài
assert review.rstrip('\n').endswith('Kết bài')
print('ends with Kết bài: OK')
