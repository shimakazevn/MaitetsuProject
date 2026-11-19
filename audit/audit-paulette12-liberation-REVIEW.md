# Audit: Paulette 12_解放 — 7 dòng Việt sai (đã đối chiếu JP + TW)

**Kết quả: 7/194 dòng sai (3,6%)** — 0 lệch vị trí, 0 chưa dịch, 0 cụt câu, 0 chưa chắc chắn. File sạch về cấu trúc, lỗi rải rác từng dòng (thuật ngữ 1, mất tiếng hít っ 3, sai nghĩa 2, xưng hô độc thoại 1). Cảnh: cuộc điện thoại của Paulette với mẹ — Soutetsu ngồi nghe ké, Paulette hoà giải với mẹ, hai người thổ lộ và trao nhau nụ hôn đầu (1383).

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 194 dòng script** (thoại 102: Soutetsu 42, Paulette 60; lời dẫn 92) đối chiếu JP + TW từ CSV "Trang tính 3", target là TOML-2. TW chỉ là nhân chứng thứ hai; chỗ nào JP và TW mâu thuẫn thì theo JP (quy tắc Hieu đặt 19/11).
- Heuristic thoại↔lời dẫn báo **0 dòng** — bắt được 0/7. Toàn bộ lỗi đều là cùng-loại (thuật ngữ, tiếng hít, nghĩa, xưng hô) nên heuristic không thấy được; thêm một bằng chứng nữa rằng heuristic chỉ là cận dưới.
- Không có key-shift sạch (shift 0: 194/194; các shift khác 0,958–0,990 — không có ý nghĩa vì key thưa và lỗi không phải lệch vị trí, không áp dụng).
- TOML và CSV giống hệt nhau về nội dung (131 dòng khác chỉ ở `\n`/khoảng trắng, 0 khác nội dung). Không có dòng CSV trống nào; VN==TW 0 dòng.
- `[selections]` rỗng (0 mục). Thẻ `%l`: chỉ 1 dòng có thẻ (1121, エアクラ) — thẻ thiếu dấu `;` đóng (xem chi tiết 1121 và đề xuất quét toàn dự án bên dưới).
- Phân loại lỗi: thuật ngữ 1 dòng (1121 Ohimitera), lỗi nhỏ 3 dòng (mất tiếng hít っ: 822, 1161, 1162), sai nghĩa 2 dòng (1448, 1510), xưng hô 1 dòng (độc thoại "mình" 1525). Theo người nói: Soutetsu 3, Paulette 1, lời dẫn 3.
- Thoại sai 4/102 (3,9%), lời dẫn sai 3/92 (3,3%).
- Về xưng hô Soutetsu trong thoại: quét toàn bộ file bằng máy (đã chuẩn hoá `\n` thành khoảng trắng trước khi chạy regex `\b`, theo bài học Paulette 08) — "tôi/Tôi" 15 dòng, "anh/Anh" tự xưng **0 lần**, "em" ngôi hai 0 lần. File này Soutetsu không lần nào tự xưng "anh" — sạch như Paulette 11 về mặt này.
- Về "mình" trong độc thoại: 7 dòng chứa "mình" — **6 dòng đúng, 1 dòng sai** (1525). 6 dòng đúng: sở hữu cách ("của mình", "bản thân mình"), phản thân ("tự cho mình"), mệnh đề phụ ("Tôi đã nghĩ mình…", "như mình muốn"), thành ngữ ("một mình mẹ" = một mình, không phải đại từ). Chỉ 1525 là "mình" làm chủ ngữ độc lập trong suy nghĩ ngoặc đơn của Soutetsu.
- Không có file trùng lặp: file này chỉ tồn tại ở 03_Paulette/ (đã kiểm tra md5 toàn bộ 227 file TOML-2; các cặp trùng khác đều là file Grand Rewrite — không liên quan file này).

## Kết luận về cơ chế lỗi

Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương, không có dòng mồ côi — đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (81.202 mục): 7/7 dòng sai chỉ xuất hiện đúng 1 lần trong toàn dự án, tại chính key của nó. 5 ngoại lệ đều là chuỗi ngắn chung chung, không phải câu của dòng khác:

- **1011/1012 (cùng "「Hả?」")**: JP cả hai đều là 「え？」 — trùng lặp hợp lệ, không tính sai.
- **958 ("「Không, có gì đâu――」"), 1136 ("「Cảm ơn anh.」"), 1069 ("「Chắc là vậy rồi.」"), 843 ("「……Paulette.」"), 1026 ("「Vâng, anh Soutetsu.」")**: mỗi chuỗi xuất hiện ở 1–3 file khác với JP tương đương (câu chào/cảm ơn ngắn) — đều là bản dịch đúng của JP riêng nó. Hai trường hợp ngược lại đáng ghi nhận (không phải lỗi của file này): ポーレットh8 3114 có VN "「……Paulette.」" trong khi JP của nó là câu lời dẫn về ngón tay — dòng đó của file h8 có vẻ lệch vị trí; 日々姫04 2480 có VN "「Chắc là vậy rồi.」" trong khi JP là câu dài tiếng địa phương — dòng đó của file Hibiki 04 có vẻ lệch vị trí. Để lại cho audit các file đó sau.

Cơ chế lỗi ở đây là **lỗi từng dòng rải rác + 1 thuật ngữ hệ thống (Ohimitera)** — giống các file Paulette 06–11 sạch về cấu trúc. Điểm đáng chú ý: đây là file Paulette thứ hai liên tiếp mà Soutetsu không một lần tự xưng "anh" trong thoại (sau Paulette 11).

## Chi tiết 7 dòng sai

### Thuật ngữ (1 dòng)

**1121 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera". Thẻ %l của エアクラ thiếu dấu `;` đóng thẻ (JP có `%l;#;`) — sửa luôn trong cùng một dòng.

- JP: 「\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致の話が御一夜にあるって聞いて――
それでパパ、反対運動に協力することにしたんです」
- TW: 「爸爸聽說\x%lエアクラ;#00ffc040;空凝機%l;#;工廠要在御一夜落戶，就表示要去參與反對運動」
- Cũ: 「Nghe nói có chuyện mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;# đến Ohimitera――
Nên ba tôi quyết định hợp tác với phong trào phản đối.」
- Sửa: 「Nghe nói có chuyện mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; đến Ohitoyo―― Nên ba tôi quyết định hợp tác với phong trào phản đối.」

### Lỗi nhỏ — mất tiếng hít っ (3 dòng)

**822 [Soutetsu]** — JP 「――っ」 là tiếng hít độc lập sau dấu gạch; bản cũ 「――」 làm mất tiếng hít. Tiền lệ Hachiroku 12 再開発 2103/2537 và Paulette 09/11: sửa thành "Ư".

- JP: 「――っ」
- TW: 「——」
- Cũ: 「――」
- Sửa: 「――Ư」

**1161 [Soutetsu]** — JP 「っ！」 là tiếng hít độc lập; bản cũ 「!」 làm mất tiếng hít. Tiền lệ 再開発 2103/2537: sửa thành "Ư!".

- JP: 「っ！」
- TW: 「！」
- Cũ: 「!」
- Sửa: 「Ư!」

**1162 [Soutetsu]** — JP 「っ！？」 là tiếng hít độc lập; bản cũ 「!?」 làm mất tiếng hít. Tiền lệ 再開発 2103/2537: sửa thành "Ư!?".

- JP: 「っ！？　いや――僕は――」
- TW: 「！？　但是——我並沒有——」
- Cũ: 「!? Không――Tôi thì――」
- Sửa: 「Ư!? Không――Tôi thì――」

### Sai nghĩa (2 dòng)

**1448 [lời dẫn]** — ぽわっと là hơi ấm lan toả dịu dàng (cùng họ với ふわっと → "Nhẹ nhàng" trong sfx doc §1); "Phừng phực" là lửa bùng lên — sai hẳn hình ảnh. Lòng bàn tay ấm lên từ từ, không phải bốc cháy.

- JP: ぽわっと。
ポーレットの手のひらがあたたかくなる。
- TW: 波萊特的掌心，忽然燙了起來。
- Cũ: Phừng phực.
Lòng bàn tay Paulette trở nên ấm áp.
- Sửa: Ấm dần lên. Lòng bàn tay Paulette trở nên ấm áp.

**1510 [lời dẫn]** — JP là mảnh câu bỏ lửng, không có động từ "dừng lại" (――音の流れが。); TW thêm 停了下來 ("dừng lại") và bản cũ theo TW. Theo quy tắc JP-trên-TW, bỏ "đã dừng lại" (tiền lệ Paulette 08 1633).

- JP: 悲しく歌うようだった、
そぼふる雨のようだった――音の流れが。
- TW: 那宛若悲歌一般的聲音，宛若淅瀝雨點一般的聲音——停了下來。
- Cũ: Dòng âm thanh――
như một khúc ca buồn, như một cơn mưa phùn――đã dừng lại.
- Sửa: Dòng âm thanh―― như một khúc ca buồn, như một cơn mưa phùn――.

### Xưng hô (1 dòng)

**1525 [lời dẫn]** — Suy nghĩ ngoặc đơn của Soutetsu; quy ước độc thoại của file là "Tôi" (92 dòng lời dẫn còn lại đều dùng "Tôi"/không đại từ). "mình" ở đây là chủ ngữ độc lập — sửa thành "Tôi". Tiền lệ hearing 2580/2584/2586/2590.

- JP: （いや――まて、僕）
- TW: （不——等等）
- Cũ: （Không――khoan đã, mình）
- Sửa: （Không――khoan đã, tôi）

## Bằng chứng cho các quyết định đang chờ Hieu chốt

- **Soutetsu gọi Paulette "cô" vs "em" (thoại): "cô" 7 lần** (973, 1021, 1058, 1090, 1110, 1112, 1113) **vs "em" 0 lần** — trong file này Soutetsu không gọi Paulette là "em" lần nào. Cộng dồn: Paulette 08 đề xuất "em", Paulette 09 "cô" 7 vs "em" 1, Paulette 10 "cô" 20 vs "em" 2, Paulette 11 "cô" 9 vs "em" 0, Paulette 12 "cô" 7 vs "em" 0 — **bốn file liên tiếp nghiêng mạnh về "cô", cộng dồn P09–12: "cô" 43 vs "em" 3**. **Không quyết, chỉ ghi số liệu.**
- **湯医 / 帝鉄 / コン / タブレット: 0 lần xuất hiện trong file này** (cả JP lẫn VN) — không có bằng chứng mới cho các quyết định đang chờ.
- **御一夜: JP 1 lần (1121), VN cũ "Ohimitera" 1 lần** — đã sửa thành "Ohitoyo" trong khối TOML; file không còn dạng cũ nào.

## Đề xuất cập nhật context

1. **Thẻ %l thiếu dấu `;` đóng thẻ — đề xuất quét toàn dự án.** Kiểm tra toàn dự án: thẻ %l trong JP luôn đóng bằng `%l;#;` (4756/4756), nhưng bản Việt thiếu `;` ở **151 chỗ** (5003 có, 151 thiếu). File này chỉ có 1 thẻ (1121) và đã sửa trong khối TOML; Paulette 13 có 5 thẻ thiếu `;` (1397, 1366, 1596, 1637, 1641 — xem audit Paulette 13). Nếu thẻ thiếu `;` làm parser TIPS đọc sai thì 151 dòng này đều cần sửa; nếu game vẫn hiển thị đúng thì đây chỉ là lỗi thẩm mỹ. Đề xuất: Hieu kiểm tra một dòng có thẻ thiếu `;` trong game (ví dụ Paulette 12 1121) rồi quyết định có quét toàn dự án hay không.
2. **Không có đề xuất mới nào khác.** Sfx doc §3 cho phép giữ っ (`——っ`) hoặc dùng `——!`; tiền lệ audit (再開発 2103/2537, Paulette 09/11) dùng "Ư" cho tiếng hít bị mất — file này theo đúng tiền lệ đó, không cần đổi chuẩn.

## Những dòng đã kiểm tra và KHÔNG tính sai

- **1293**: "Gánh nặng vốn dĩ chia sẻ cho hai người, nay đổ dồn lên một mình mẹ." — JP không nêu chủ ngữ ("自分ひとりに"), nhưng toàn đoạn đang kể về mẹ Paulette (1120 ba tranh cử, mẹ đến giới hạn; 1303 "Mẹ của Paulette cũng không đủ sức lực mà thôi") nên "mẹ" là chủ ngữ đúng theo ngữ cảnh, không phải bịa thêm. TW giữ chung chung ("一個人") nhưng bản Việt làm rõ không sai nghĩa.
- **953 / 1080**: "Chắc chắn, tôi chỉ nghĩ…" / "chắc chắn, điều đó gần giống với sự bỏ cuộc" — きっと đọc là "chắc chắn" được (surely/certainly), không tính sai.
- **1337**: "…ngày càng thấy bất an……!?" — JP kết bằng ……っ！？ nhưng tiếng hít nằm cuối câu, không phải tiếng hít độc lập; dấu "……!?" đã truyền được vẻ giật mình bỏ lửng. Ranh giới — ghi rõ lý do để Hieu soát lại nếu muốn.
- **1011/1012**: cùng VN "「Hả?」" — JP cả hai đều là 「え？」, trùng lặp hợp lệ.
- **975**: furigana [おやこ,1]母娘 được bỏ trong bản Việt — đúng chuẩn chung của dự án (ruby là hướng dẫn phát âm, không phải nội dung).
- **1088**: "Mama……không, mẹ ơi." — Paulette tự sửa cách gọi mẹ từ "Mama" sang "okaasan" (mẹ) trong lúc nói chuyện điện thoại; bản Việt giữ đúng nhịp tự sửa đó.
- **1446**: "Phải khiến họ rút lui trước khi tiếng nói ủng hộ mời gọi trở nên sôi nổi" — 撤回させる ("khiến rút lại") dịch thoát thành "khiến họ rút lui" là chấp nhận được.

## Khối TOML sửa (đã kiểm chứng: parse được, đúng 7/7 key)

```toml
822 = "「――Ư」"
1121 = "「Nghe nói có chuyện mời gọi nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; đến Ohitoyo―― Nên ba tôi quyết định hợp tác với phong trào phản đối.」"
1161 = "「Ư!」"
1162 = "「Ư!? Không――Tôi thì――」"
1448 = "Ấm dần lên. Lòng bàn tay Paulette trở nên ấm áp."
1510 = "Dòng âm thanh―― như một khúc ca buồn, như một cơn mưa phùn――."
1525 = "（Không――khoan đã, tôi）"
```

## Kết bài

Paulette 12 (7/194, 3,6%) — đứng giữa nhóm file Paulette sạch về cấu trúc (sau hearing 2,0%, whatsentertainment và usagi 2,8%, snow inn 3,2%). Không có lỗi cấu trúc nào: không lệch vị trí, không tràn chương, không chuỗi xoay vòng. Lỗi đáng chú ý nhất là 1510 (theo TW thêm "đã dừng lại" — ca JP-trên-TW điển hình) và 1448 (ぽわっと dịch thành "Phừng phực", sai hẳn hình ảnh); còn lại là 3 tiếng hít っ bị mất rải rác và 1 dòng "mình" trong suy nghĩ ngoặc đơn.

**Còn lại cho file này:** không còn gì — 7/7 dòng sai đã có bản sửa trong khối TOML trên; 0 dòng chưa chắc chắn. Một việc chờ Hieu: quyết định có quét toàn dự án cho 151 thẻ %l thiếu dấu `;` hay không (đề xuất 1 trên) — file này chỉ là 1 trong 151 chỗ đó.

**Bước tiếp theo:** Paulette 13 đã audit xong cùng đợt (29/208, 13,9% — xem `audit-paulette13-reevaluation-REVIEW.md`). Tổng cộng 25 file đã audit: 1.706 dòng sai.
