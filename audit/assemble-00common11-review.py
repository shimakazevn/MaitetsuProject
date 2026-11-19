# Assemble audit-00common11-REVIEW.md from the verified JSON + hand-written narrative.
# Run: python3 ~/workspace/maitetsu-pilot/assemble-00common11-review.py
import json

J = '/home/hatch/workspace/maitetsu-pilot/audit-00common11-wrong.json'
OUT = '/home/hatch/workspace/maitetsu-pilot/audit-00common11-REVIEW.md'
BLOCK = '/tmp/f11_block.toml'

d = json.load(open(J, encoding='utf-8'))
d.sort(key=lambda x: int(x['key']))

def disp(s):
    return s.replace('\\n', '\u23ce')

entries = []
for e in d:
    entries.append(
f"### {e['key']} — {e['character']} — {e['kind']}\n\n"
f"**JP:** {disp(e['jp'])}\n\n"
f"**TW:** {disp(e['tw'])}\n\n"
f"**VN cũ:** {disp(e['old_vn'])}\n\n"
f"**Fix:** {disp(e['fix'])}\n\n"
f"{e['why']}\n")
entries_txt = '\n'.join(entries)

head = """# Audit 00_Common file 11 — 共通11_経営資源.txt.toml

**Ngày kiểm toán:** 20/11/2026
**Tệp TOML:** `00_Common/共通11_経営資源.txt.toml` — md5 `2981d5f80fa4b088f19aa89c998ccca4`, BOM, CRLF, `[selections]` rỗng, **không có bản sao trùng** (kiểm tra md5 toàn bộ 227 tệp TOML).
**Nguồn CSV:** "Trang tính 3" — bộ hàng duy nhất `00_Common` (không có bẫy dual-set ở file này), 572 hàng `[script]`.
**Kết quả: 102/572 dòng sai (17,8%), 0 dòng chưa chắc chắn, 0 dòng lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo file.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| Thuật ngữ (terminology) | 59 |
| Đại từ xưng hô (pronoun) | 30 |
| Thẻ gloss %l (tag) | 2 |
| Tiếng thở/gasp (gasp) | 6 |
| Sai nghĩa (meaning) | 5 |
| **Tổng** | **102** |

**Theo loại dòng:** thoại 69/367 sai (18,8%), độc thoại 33/205 sai (16,1%).
**Theo nhân vật:** 双鉄 (Soutetsu) 42, monologue 33, ポーレット (Paulette) 14, 赤井宮司 (Akai) 8, ハチロク (Hachiroku) 4, 真闇 (Mayami) 1.

Nhóm thuật ngữ (59) chia nhỏ: 宮司→"đền chủ" 38 dòng / 39 lần xuất hiện (2293, 2302, 2401, 2503, 2522, 2530, 2578, 2620, 2672, 2782, 2783, 2814, 2886, 3002, 3253, 3307, 3313 [×2 trong một dòng], 3332, 3390, 3444, 3445, 3470, 3529, 3542, 3559, 3567, 3589, 3611, 3792, 3829, 3830, 3832, 3833, 3834, 3835, 3836, 3837, 3838 — trong đó 9 dòng viết hoa "Cung tư tế" đầu câu/xưng hô → "Đền chủ", 29 dòng viết thường → "đền chủ"; file này nặng về Akai nên 宮司 là lỗi nhiều nhất); 御一夜→Ohitoyo 12 dòng (1828, 2525, 2535, 2753, 2817, 2818, 2937, 2960, 3434, 3562, 3758, 3836); 帝鉄→Teitetsu 10 dòng (1777, 2522, 2529, 2546, 2620, 2693, 3321, 3487, 3834, 3836); 冥国→Minh Quốc 2 dòng (2628, 2901); 廣島電気鉄道→"Đường sắt điện Hiroshima" 1 dòng (2689); chú thích romaji "(kikanshi)/(untenshi)" gỡ 1 dòng (2580); 経営資源→"tài nguyên kinh doanh" 1 dòng (2546, chung dòng với Teitetsu). Nhóm đại từ (30): Soutetsu gọi Paulette "cô"→"em" 11 dòng (1845, 2239, 2250 [×2], 2253, 2299, 2380, 2423, 2445, 2997, 3003, 2308); Soutetsu tự xưng "tôi"→"anh" với Paulette 18 dòng (1797, 2238, 2250, 2380 [×2], 2466, 2479, 2572, 2583, 2596, 2599, 2645, 2711, 2987, 2995, 2998, 3003, 3023, 3031); Soutetsu tự xưng "em"→"tôi" với Mayami 4 dòng (2450, 2612, 2839, 2842 [×2]).

File này là file 00_Common "bẩn" nhất tính đến nay (17,8%, cao hơn file 05 với 12,4%) — không phải vì lệch dòng (0 dòng lệch) mà vì mật độ thuật ngữ chưa cập nhật theo các quyết định 19–20/11 rất cao: riêng 宮司 đã 38 dòng (Akai là nhân vật trung tâm của file: 41 dòng thoại + phần lớn độc thoại đều xoay quanh ông ấy), cộng với cụm đại từ Soutetsu↔Paulette 30 dòng. Toàn bộ 102 lỗi đều sửa được tại chỗ, không cần dịch lại.

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục. TOML md5 `2981d5f80fa4b088f19aa89c998ccca4`, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng trong 227 tệp.
- **CSV vs TOML:** VN khớp tuyệt đối 215 hàng; khớp sau khi gộp ký tự xuống dòng thành khoảng trắng 357 hàng; **0 khác biệt** — CSV3 là bản chuẩn cho fix list.
- **Sweep っ (gasp):** sweep CÓ liệt kê file này — 3 mục trong sweep-raw-gasp-wrong.json (1811, 3067, 3068). Cả 3 giá trị fix của sweep đã kiểm chứng đúng với JP và được áp nguyên. Quét っ hệ thống trên toàn bộ JP của file (không chỉ dựa vào sweep) không tìm thêm gasp っ trần nào bị mất; 3016 (あのっ！ → "Ưm!") là trường hợp audit tự phát hiện — tiếng ngập ngừng, không phải っ trần nên sweep không bắt. Các fix 2396/2419/3536 là theo công thức độ dài nguyên âm, không thuộc sweep.
- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng), không có VN mồ côi (orphan), không có key trùng. Chỉ 1 hàng VN == TW là key 1816 (JP/TW/VN đều là 「……」 — dấu lặng, hợp lệ, không phải chưa dịch). Các VN trùng nhau trong file chỉ là câu cảm thán ngắn lặp lại hợp lệ (「Ồ.」×4, 「Hừm.」×3, 「Vâng.」×3, 「A.」×2 — lưu ý fix 2419 phá nhóm 「Hừm.」 thành ×2 + 「Hừừm.」).
- **Kiểm tra nhiễm chéo:** đối chiếu 102 giá trị VN cũ trong fix list qua chỉ mục VN toàn dự án — 0 trùng khớp ngoài file. Toàn bộ 572 VN đều khớp đúng JP của chính dòng mình.
- **Thứ tự dòng:** key số trong file này KHÔNG phải thứ tự truyện — các cảnh xen kẽ nhau theo key (cảnh đền Akai, cảnh xưởng rượu, cảnh đi dạo đêm nằm lẫn lộn). Vì vậy địa chỉ người nghe được xác định từ nội dung dòng + mạch hội thoại (ai nói trước/sau về cùng chủ đề), KHÔNG dùng key kề nhau theo thứ tự số. Bằng chứng: 2572 (xem ghi chú trong mục đó).

## 3. Các lỗi đã sửa (102 dòng)

"""

mid = """## 4. Kiểm tra chéo

- **Chuỗi xoay (rotation):** 0 chuỗi. Không có dòng nào mà VN đúng nằm ở key khác trong file.
- **Nhiễm chéo file:** 0. Xem §2 (0 trùng khớp ngoài file trong 102 giá trị fix).
- **Thẻ %l:** 2 tag do bản Việt tự thêm đã gỡ (2404 醸造蔵, 3076 8620 — JP chỉ có ruby [..,n], đã kiểm chứng comment `# JP:` trong TOML; không có tag nào thiếu dấu `;` đóng trong file này). Các thẻ %l còn lại đều là của JP và được giữ nguyên (1797 本屋, 2693 電車, 2753 本屋, 2580 電車).
- **Gasp っ:** sweep CÓ liệt kê file này (3 mục 1811/3067/3068, áp nguyên). Audit tự quét toàn bộ っ trong JP: không còn gasp trần nào bị mất ngoài 3 mục sweep; các っ còn lại đều đã được diễn đúng (2406 えっ→"Hả!?", 2407 あっ→"A!", 2429 あっ/そうっ→nói lắp, 2425/2631 ho "khụ", 2393/2395/2461 cười "Ufufu") hoặc là っ nhấn mạnh cuối từ (2435 いえっ, 2501 はいっ, 3006 ごちそうさまっ, 3017 ですからっ — không thêm Ư, đúng quy tắc sweep).
- **まいてつ / 市電:** file này không có dòng nào dùng 2 thuật ngữ này (0 gloss まいてつ, 0 市電) — không áp dụng quyết định mới 20/11 ở đây.
- **"Anh Akai" (2406):** đã kiểm chứng KHÔNG phải lỗi — quét toàn dự án cho thấy "Anh Akai" là cách dịch đã thiết lập của 赤井さん (Hibiki ở 日々姫08 2259, Nagayama ở P14 1524, 技工Ｂ ở ニイロク03 4 lần). Paulette dùng "Anh Akai" khớp với quy ước chung của dự án (TW dịch 赤井さん là 赤井先生, nhưng bản Việt đã thống nhất "anh Akai").
- **2409 「ああ」→「A.」:** KHÔNG phải lỗi — quét toàn dự án: 「ああ」 đứng một mình được dịch 「A.」 16 lần (so với 「Ừ.」 54, 「À.」 48); "A." là cách dịch đã có trong dự án, giữ nguyên.
- **Soutetsu "tôi" giữ nguyên (đúng):** với Akai (2590, 2576, 2636, 2906, 2701, 2999, 2609, 2848) và với Hachiroku (2337) — quan hệ trang trọng, "tôi" đúng. Số nhiều "chúng tôi" với Paulette (2886, 2287) giữ nguyên; "Bọn em" (nhóm Soutetsu+Hachiroku) với Mayami (2592) giữ nguyên — quy tắc đại từ chỉ áp cho tự xưng số ít.

## 5. Kiểm tra lần 2 (second pass)

Đọc lại toàn bộ 102 fix so với JP của từng dòng: **tổng 102 / kiểm tra lại 102 / loại bỏ 0 / sửa 1**. Lần 2 bắt được 1 lỗi chép trong bản thảo fix: 3536 viết "sự đồng ý" trong khi VN cũ là "sự đồng tình" — đã sửa lại thành "đồng tình" (chỉ thay 「A」→「Aa」). Ngoài ra, trong lúc kiểm chứng, quét regex hệ thống toàn file theo từng thuật ngữ đã quyết đã bắt thêm **2 dòng mà lần đọc theo chunk bỏ sót** (3529, 3830 — đều là 宮司), nâng tổng từ 100 lên 102; riêng 宮司 lần đọc chunk đếm 35 dòng, quét hệ thống cho ra **38 dòng / 39 lần xuất hiện** (2620 đã có trong fix list qua nhóm 帝鉄; 3529 và 3830 hoàn toàn bị sót). Parse-check riêng là chưa đủ; con số trên là từ lần đọc lại bằng mắt + đối chiếu diff từng dòng.

## 6. Các dòng cố tình KHÔNG sửa (ghi chú phán đoán)

- **2406 "Anh Akai":** xem §4 — cách dịch đã thiết lập của 赤井さん toàn dự án. Không sửa.
- **2409 「ああ」→「A.」:** xem §4 — "A." đã có 16 lần trong dự án. Không sửa.
- **2408 「おお……」→「Ồ……」:** cách diễn cảm thán đã chuẩn. Không sửa.
- **2415 "chú chó con":** Soutetsu nói nhầm 子犬 (chó con) trong khi Paulette nói 子猫 (mèo con) — lỗi nhầm của chính nhân vật, là trò đùa trong truyện; Hachiroku sửa lại cho anh ta ở 2621. Không sửa.
- **3747 "Pyon!":** SFX giữ nguyên theo quy tắc ngẫu hứng 22:05 (tiếng nhảy của Hachiroku).
- **2909 "mài ra ăn được":** thành ngữ Việt đã thiết lập cho 理想で飯が食える. Không sửa.
- **2592 "Bọn em":** nhóm Soutetsu+Hachiroku nói với Mayami — số nhiều, không thuộc quy tắc tự xưng số ít. Không sửa.
- **2623 "các cậu":** Soutetsu gọi nhóm (Soutetsu+Hachiroku) — xưng hô nhóm, giữ nguyên.
- **3314 "Watashi" và 3884 "Reina":** bản thân các từ này đang được bàn luận trong hội thoại. Không sửa.
- **2681/2753 thẻ %l của 本屋:** JP có thẻ, bản Việt giữ đúng. Không sửa.
- **2886/2287 "chúng tôi" với Paulette; 2337 "Tôi" với Hachiroku; 2590/2576/2636/2906/2701/2999/2609/2848 "tôi" với Akai/Hachiroku:** đều đúng (số nhiều / quan hệ trang trọng). Không sửa.
- **1816 「……」:** JP/TW/VN giống hệt nhau — dấu lặng, hợp lệ. Không sửa.
- **2435/3017/2429/2501/3006 (っ nhấn mạnh cuối từ):** đã diễn đúng, không thêm Ư. Không sửa.
- **2572:** fix "tôi"→"anh" được giữ (xem ghi chú trong mục đó) — địa chỉ suy từ mạch truyện (kế hoạch cho mèo là của Paulette; cô ấy nói trước 2887 và tiếp sau 2805), không chắc tuyệt đối như các dòng đi dạo đêm nhưng đủ vững.

## Kết bài

File 11 là file 00_Common "bẩn" nhất tính đến nay (102/572 = 17,8%), nhưng bẩn vì thuật ngữ và đại từ — không phải vì cấu trúc: 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 dòng chưa chắc chắn. 59 lỗi thuật ngữ (宮司 38 dòng là nhiều nhất — file xoay quanh Akai) và 30 lỗi đại từ Soutetsu↔Paulette đều là hệ quả của các quyết định 19–20/11 chưa được áp dụng vào bản dịch cũ, cộng với thói quen xưng hô cũ của dịch giả. Toàn bộ 102 fix đều sửa tại chỗ. Sau file này, Ohitoyo còn lại trong 00_Common là 76 lần (14: 30, 15: 15, 10: 14, 12: 6, 13: 3, file 01 pilot: 8 chưa chốt — file 10 đang được audit song song, parent sẽ cộng dồn khi xong). Còn lại chưa kiểm toán trong 00_Common: 10, 12, 13, 14, 15, 末尾 (7 file trừ file 01 bản nháp; file 10 đang chạy).

Khối TOML dưới đây parse được bằng tomllib, **102 key, 0 sai lệch giá trị so với JSON**. Quy tắc ký tự xuống dòng: giá trị fix nào chứa ký tự xuống dòng dạng backslash-n (2 ký tự, như trong JSON và trong TOML gốc) thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON.

```toml
"""

block = open(BLOCK, encoding='utf-8').read()
tail = "```\n"

with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write(head)
    fh.write(entries_txt)
    fh.write('\n')
    fh.write(mid)
    fh.write(block)
    fh.write('\n')
    fh.write(tail)
print('wrote', OUT)
