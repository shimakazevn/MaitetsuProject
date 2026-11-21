## ハチロク16_春 — ハチロク16_春.txt.toml — 22/412 (5,3%)

- File: `ハチロク16_春.txt.toml` — route 01_Hachiroku, 412 dòng script (độc thoại 166, ハチロク 71, 双鉄 69, 日々姫 37, こだま 18, 宗方 18, 電車姫 14, ポーレット 6, ひよこ 4, のぞみ 4, れいな 3, 真闇 2). Nội dung: buổi sáng mùa xuân trên tuyến — Kodama ra mắt, chuẩn bị chuyến tàu của cô bé; Soutetsu và Hachiroku nhớ Olivy, ngắm cảnh qua cửa sổ ở Okoba/Yatsushiro, Hibiki lái 8620 leo dốc Yatake; Munakata từ chối làm Master của Kodama; Công chúa Tàu điện xuất hiện qua màn hình.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, 412 dòng, 0 VN trống. TOML md5 `f8506b4cc0b92e50a202aa8435022314`, 1 bản duy nhất, BOM + CRLF, `[selections]` rỗng. TOML khớp CSV3 tuyệt đối sau chuẩn hoá `\n` literal (183 dòng khớp tuyệt đối, 229 dòng chỉ khác flatten, 0 dòng khác nội dung). 1 cặp VN trùng là câu lặp hợp lệ (1733/1766 cùng "A.").
- Phân loại (22): thuật ngữ 6 (1294 冥国→"Minh Quốc"; 1611, 1995, 2298, 2307, 2509 gloss タブレット "thẻ bảng"→"máy tính bảng"), gasp 10 (1721, 1725, 1744, 1746, 1808, 1932, 2052, 2380, 2783 từ sweep + 1689 sweep bỏ sót), sai nghĩa 5 (1730 "chưa"→"không"; 2081 bỏ "Một trong"; 2283 đảo chủ ngữ; 2377 mất phủ định; 2735 "gấp vạn lần"→"gấp bội"), số nguyên âm 1 (2817 ポー 12→9 u).
- Sweep kiểm chứng: 9 entry cho file, nhận cả 9 sau khi đối chiếu JP; audit tìm thêm 1 gasp sweep bỏ sót (1689). Quét máy toàn bộ dòng っ không còn gasp sót.
- Đại từ đã kiểm chứng: Soutetsu "tôi" với Hachiroku giữ nguyên đúng chỗ; 1999 "Anh" không chắc người nghe — giữ nguyên (cờ cho Hieu); Paulette "anh Soutetsu" đúng khóa B4.
- Chi tiết đầy đủ: `audit-hachiroku16-haru-REVIEW.md`; danh sách sửa: `audit-hachiroku16-haru-wrong.json` (22 mục, khối TOML 22 khóa, 0 sai lệch giá trị, jp/tw/old_vn khớp CSV3 tuyệt đối 22/22; lượt soát 2: 22/22, 0 bỏ, 1 sửa).
- Chờ Hieu: (1) 1999 "Anh" chưa xác định người nghe — giữ nguyên; (2) Munakata "tôi" không có 俺 tường minh 6 dòng (1297, 1306, 1637, 1903, 2050, 2070) — "tao" áp toàn bộ hay chỉ dòng có 俺?; (3) [characters] 2791 "Densha Hime" / [character_subs] 2789 "電車公主" có đổi theo "Công chúa Tàu điện"?; (4) B19 vẫn park.
- Đợt thống nhất (§4 review, không tính sai): "Ohimitera" ×3 (1803, 1839, 1845), "Đường sắt Ohito" ×3 (1221, 1884, 2070), "tuyến Yui" ×4 (1622, 1987, 2403, 2587), "Densha Hime" ×3 (2692, 2706, 2790), gloss 帝鉄 "Đường sắt Hoàng gia" ×1 (2338), Munakata 俺/おれ→"tao" ×4 (1301, 1884, 1910, 2025). "Hinamoto": 0 dòng trong file (cả 4 dòng 日ノ本 đã đúng "Hinomoto").

```toml

"1294" = "「……Em ấy từng kể cho chúng ta nghe rồi nhỉ.\\nCâu chuyện về khu mỏ than bỏ hoang ở Minh Quốc hiện vẫn đang bốc cháy.」"
"1611" = "「Hình như là 『Từ \\x%lタブレット;#00ffc040;máy tính bảng%l;#; của một \\x%lレイルロオド;#00ffc040;Railord%l;#; đã hoạt động hơn một trăm năm,\\nmột Lõi Railord hoàn toàn mới đã được tinh chế ra』 thì phải?」"
"1689" = "「Ư!!?」「Ư!!?」\\n「Hảảả!?」"
"1721" = "「Ư!!」"
"1725" = "「Ư!」"
"1730" = "「À――không.」"
"1744" = "「Ư!!」\\n「A――」"
"1746" = "「Ư!!?」\\n「Kya!」"
"1808" = "「Nặng quá~! Nặng quá đi mất~Ư!」"
"1932" = "「Hibiki, sao thế? Có bị thương không――Ư!!!」"
"1995" = "「Tất nhiên là tôi muốn tự tay nuôi dưỡng con bé rồi. Dù sao đây cũng là một trường hợp vô cùng quý giá,\\ntinh chế ra hai Lõi Railord từ một \\x%lタブレット;#00ffc040;máy tính bảng%l;#; duy nhất cơ mà.」"
"2052" = "「Ư!!!!」"
"2081" = "「Anh hai và Hachiroku đã từng thấy chưa?\\nBa khung cảnh qua cửa sổ đẹp nhất Hinomoto ấy, cùng với Olivy.」"
"2283" = "Bị ba người ôm chầm lấy cùng một lúc, tất nhiên là cô bé sẽ ngạc nhiên rồi.\\nNhưng mà, cô bé không thể thoát ra được."
"2298" = "Nói cách khác, nó giống như là “linh hồn” của \\x%lレイルロオド;#00ffc040;Railord%l;#; vậy.\\nThứ đó, đã được tinh chế từ \\x%lタブレット;#00ffc040;máy tính bảng%l;#; của Olivy――"
"2307" = "Lõi Railord. Thứ làm cho \\x%lタブレット;#00ffc040;máy tính bảng%l;#; trở thành \\x%lタブレット;#00ffc040;máy tính bảng%l;#;\\nlàm cho \\x%lレイルロオド;#00ffc040;Railord%l;#; trở thành \\x%lレイルロオド;#00ffc040;Railord%l;#;……"
"2377" = "Chỉ có một điều duy nhất, chỉ có một điều duy nhất, chỉ có một điều duy nhất.\\nTrong tâm trí tôi lúc này, chẳng có lời nào hiện lên cả."
"2380" = "Có lẽ vì sốt ruột trước bài diễn văn dài dòng của Tiến sĩ Phượng Hoàng,\\ncô bé sốt sắng bước lên phía trước――Ư!!"
"2509" = "Việc tinh chế từ \\x%lタブレット;#00ffc040;máy tính bảng%l;#; có lẽ đồng nghĩa với việc chức năng đã ngừng hoạt động,\\nnhưng dù vậy, chúng tôi vẫn có thể tự mình kết nối với tương lai."
"2735" = "Điều đó, khiến tôi cảm thấy vui sướng.\\nHơn cả sự cô đơn, gấp bội, gấp chục lần, gấp trăm lần."
"2783" = "Dù biết đó là chuyện không tưởng,\\nnhưng tôi vẫn bất giác đưa mắt tìm kiếm hình bóng ấy giữa đám đông――Ư!!!"
"2817" = "（Tuúúúúúúúú!）"
```

**Tổng cộng sau file này: 180 file / 8.111 dòng sai** (cơ sở 179 file / 8.089 dòng sai + 22 file này)
