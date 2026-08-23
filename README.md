# Maitetsu: Last Run!! — Vietnamese Translation Project

Dự án Việt hóa hoàn chỉnh Visual Novel `まいてつ Last Run!!` (Maitetsu Last Run!!).

Dự án bao gồm hệ thống tự động hóa (Automated Toolchain Pipeline) giúp trích xuất, dịch thuật kịch bản `.toml`, biên dịch nhị phân `.scn` và đóng gói thành tệp lưu trữ nén `patch3.xp3` (cho PC DMM / Mobile) hoặc `unencrypted.xp3` (cho Steam). Tương thích mượt mà với Windows, Android (Kirikiri 2 Next APK), iOS (IPA) và Steam.

---

## Tính Năng & Tối Ưu Nổi Bật

* **Hệ Thống Phông Chữ Native (Chính Quy)**:
  - Tích hợp chuẩn xác vào hệ thống nạp phông nhúng của engine (`embfontlist.tjs` & `Config.tjs`) thay vì can thiệp inject thô bạo.
  - Hỗ trợ đầy đủ **5 biến thể độ dày (Weights)** của phông Signika Negative: `Regular`, `Bold`, `SemiBold`, `Medium`, `Light`.
  - Chuẩn hóa bảng tên OpenType/TTF Name Table, giúp Windows GDI và FreeType nhận diện chính xác từng biến thể phông trong menu Cài đặt và hiển thị đúng nét Đậm (Bold) / Bán đậm (SemiBold) theo lựa chọn của người chơi.
* **Động Cơ Co Giãn Chữ 3 Trạng Thái (3-State Dynamic Auto Font Scaling)**:
  - Đồng bộ hoàn hảo trên cả bản DMM và Steam qua `CustomMsgwinRender`.
  - **State 1 (1–2 dòng chuẩn)**: Giữ cỡ chữ 100% (26px), khoảng cách dòng 7px, cân giữa hoàn hảo.
  - **State 2 (2 dòng dài)**: Tự động thu nhỏ 91% (~23.5px), khoảng cách dòng 5px.
  - **State 3 (3 dòng thoại)**: Tự động thu nhỏ 82% (~21px), khoảng cách dòng 4px, mở rộng khung chữ 102px và tự động nâng tọa độ trục `oy` (`_orig_oy - 12`) để chữ trải đều, không bị chạm đáy hay đè lên biểu tượng click.
  - **State 4 (Dự phòng cho câu siêu dài)**: Thu nhỏ linh hoạt xuống tới 60%.
* **Tự Động Ngắt Dòng (Auto Word-Wrap)**: Kích hoạt thuật toán ngắt dòng Latin/Việt hóa (`word_break: 0`), ngăn chặn từ ngữ bị ngắt đôi ở cuối dòng.
* **Lịch Sử Thoại (Backlog) & Chọn Cảnh (SceneSel)**: Hook trực tiếp `CustomBacklog.drawTextBlock` với 3 cấp độ chữ thu nhỏ động theo độ dài câu thoại để không tràn vạch phân cách. Tối ưu phông SceneSel bảo toàn cơ chế tự động rút gọn dấu `...`.
* **Việt Hóa Giao Diện Toàn Diện**: Việt hóa hoàn toàn giao diện hệ thống, cài đặt gamepad, Extra mode và từ điển TIPS ngữ cảnh.
* **Nạp Patch Siêu Tốc (Fast AutoPath Indexing)**: Tối ưu hóa bảng băm đường dẫn trong C++ Core của Kirikiri 2, tự động re-mount patch ưu tiên cao nhất mà không gây nghẽn khởi động.
* **Tương Thích Tuyệt Đối Trên Mọi Nền Tảng (Windows, Android, iOS, Steam)**:
  - Tương thích hoàn toàn với Kirikiri 2 Next engine trên Android (ARM64/x86_64) và iOS (IPA).
  - Tự động bỏ qua các thư viện DLL dành riêng cho Windows (`lzfs.dll`, `shrinkCopy.dll`) một cách an toàn.
  - Khắc phục lỗi đứng game khi hiển thị kịch bản: Bổ sung lớp bọc an toàn `getLinkNames()` / `getLinkRects()` và `_guardTipsLinkHitLayer` trong `lose_tips.tjs`.
* **Bảo Toàn E-mote**: Đồng bộ chính xác mã hiệu nhân vật (Actor ID) và layer animation E-mote riêng biệt cho từng phiên bản (DMM vs Steam).
* **Đóng gói chuyên biệt**:
  - DMM / PC Standalone / Mobile: Đóng gói `patch3.xp3` (CxEncryption, tự động re-mount AutoPath).
  - Steam Release: Đóng gói `unencrypted.xp3` (Chuẩn KrkrPatch Proxy qua `version.dll`).

---

## Lưu Ý Kỹ Thuật (Dành Cho Developer)

1. **Chuẩn Mã Hóa File Hệ Thống**:
   * Tất cả file `.tjs`, `.ini`, `.csv`, `tw_tips_*.txt` trong `patch_assets/` và `steam_version_patch_vn/patch_assets/` bắt buộc phải mang chuẩn **UTF-16 LE Single BOM** (`b'\xff\xfe'`). Tuyệt đối không để Double-BOM (`\ufeff`).

2. **Bố Cục Giao Diện UI (`*.csv`)**:
   * Các bảng UI CSV lấy từ nguồn gốc tại: `extracted_assets/KrkrExtract_Output/others/uipsd/tw/`. Cẩn trọng với encoding khi chỉnh sửa để tránh lỗi `Invalid argument count` ở `UIListParser`.

3. **Cấu Trúc Tệp `patch3.xp3` & `unencrypted.xp3`**:
   * Patch chỉ chứa các tệp ghi đè tài nguyên cụ thể. Tránh nạp thừa các tệp KAG gốc (`startup.tjs`, thư mục `data/`, `system/`) vào patch để tránh xung đột phiên bản.

---

## Kế Hoạch Phiên Bản Di Động Siêu Nhẹ (Mobile Optimized Edition — Future Plan)

> [!NOTE]
> **Hiện trạng kỹ thuật**: Dự án mã nguồn mở `krkr2_next` vốn hỗ trợ nền tảng Kirikiri 2 cũ, trong khi engine của *Maitetsu: Last Run!!* là phiên bản KrKr2 hiện đại với rất nhiều tùy biến chuyên sâu (hệ thống E-mote C++ riêng biệt, TextRender đa luồng, xử lý thẻ TIPS động `%l`, CxEncryption...). Do đó, **ưu tiên số 1 hiện tại là duy trì độ ổn định cao nhất của core engine**.
>
> **Kế hoạch tương lai (Sau khi hoàn thiện độ ổn định)**: Bản cài đặt PC gốc của game nặng tới **~20GB** (quá nặng cho thiết bị di động). Sau khi ổn định core engine, dự án sẽ lên kế hoạch xây dựng bộ công cụ đóng gói riêng **Maitetsu Mobile Edition** siêu nén:
> 1. **Tối ưu Âm thanh (Voice & BGM)**: Chuyển đổi kho thoại ~10GB sang định dạng **Opus / OGG tối ưu bitrate** (64–96 kbps cho voice, 128 kbps cho BGM), giảm ~70% dung lượng âm thanh.
> 2. **Tối ưu Đồ họa (Background & CG)**: Nén kho ảnh sang định dạng **WebP / nén GPU**, giảm 60–75% dung lượng ảnh mà độ nét trên màn hình điện thoại hoàn toàn không đổi.
> 3. **Tối ưu I/O & Tốc độ nạp cảnh**: Giảm tổng dung lượng game từ **20GB xuống chỉ còn ~4 – 6GB**, giúp nạp cảnh tức thì.

---

## Tiến Độ Dịch Thuật

Chạy lệnh `check_progress.bat` (hoặc `python tools/scripts/check_progress.py`) để xem thống kê thời gian thực:

| Tuyến Cốt Truyện (Route) | Thư Mục | Số File | Đã Dịch |
| :--- | :--- | :---: | :---: |
| Common Route (Tuyến Chung) | `00_Common` | 16 | 100% |
| Hachiroku Route | `01_Hachiroku` | 46 | 100% |
| Hibiki Route | `02_Hibiki` | 37 | 100% |
| Paulette Route | `03_Paulette` | 37 | 100% |
| Reina Route | `04_Reina` | 13 | 100% |
| Mayami Route | `05_Mayami` | 12 | 100% |
| Kisaki Route | `06_Kisaki` | 13 | 100% |
| Nagi & Fukami Route | `07_Nagi_Fukami` | 28 | 100% |
| Niiroku Route | `08_Niiroku` | 5 | 100% |
| Grand Route | `09_Grand` | 11 | 100% |
| Chikuni (China) Route | `10_Chikuni` | 8 | 100% |
| Extra / Other | `11_Other` | 1 | 100% |
| **TỔNG CỘNG** | **TOÀN BỘ GAME** | **227** | **100%** |

---

## Hướng Dẫn Cài Đặt Patch

### 1. Bản PC Gốc Nhật (DMM / DLsite / DVD) & Mobile (Android / iOS)
* **PC Windows**: Sao chép tệp `patch3.xp3` vào thư mục cài đặt game.
* **Android (Kirikiri 2 Next)**: Sao chép tệp `patch3.xp3` vào thư mục chứa dữ liệu game trên điện thoại.

### 2. Bản Steam (Hikari Field / Maitetsu: Last Run!!)
Bản Steam được tích hợp bảo vệ (KrkrSign RSA & FileHash Filter), áp dụng hook thông qua **KrkrPatch (`version.dll`)**:
1. Đóng gói thư mục patch thành `unencrypted.xp3`.
2. Sao chép `unencrypted.xp3` và `version.dll` vào thư mục game Steam (`.../steamapps/common/MaitetsuLastRun/`).
3. Khởi động game trực tiếp từ Steam. Patch sẽ tự động nạp mà vẫn giữ nguyên Steam Overlay, Achievements và Cloud Save.

---

## Hướng Dẫn Đóng Gói Patch (Build Pipelines)

### 1. Bản PC Standalone / Mobile (DMM, Android & iOS)
* **Build toàn bộ & đóng gói `patch3.xp3`**:
  ```bash
  python build_patch.py
  # Hoặc nhấp đúp file: build_patch.bat
  ```
* **Chỉ đóng gói lại XP3 (bỏ qua biên dịch SCN)**:
  ```bash
  python build_patch.py --pack-only
  ```

### 2. Bản Steam Release
* **Đóng gói patch cho Steam**:
  ```bash
  python steam_version_patch_vn/build_steam_patch.py
  ```
* **Tái tạo lại toàn bộ từ điển TIPS sạch**:
  ```bash
  python tools/scripts/rebuild_all_tips_clean.py
  ```

---

## Cấu Trúc Thư Mục Dự Án

```
MaitetsuProject/
├── .agents/                    # Bộ quy tắc dự án & hướng dẫn ngữ cảnh
├── .github/workflows/          # CI/CD Build APK (Android) & IPA (iOS)
├── docs/                       # Tài liệu, glossary, kiến trúc kỹ thuật
├── original_scn/               # 216 file kịch bản gốc nguyên bản (.scn)
├── translation_toml/           # 227 file kịch bản dịch phân theo thư mục
├── patch_assets/               # Tài nguyên UI, font, TIPS, script hệ thống DMM (UTF-16 LE)
├── compiled_scn/               # 216 kịch bản đã biên dịch (.scn)
├── steam_version_patch_vn/     # Phân hệ Patch dành riêng cho Steam
│   ├── KrkrExtract_Output/     # Bộ Asset gốc của Steam (Backup)
│   ├── build_steam_patch.py    # Script đóng gói tự động cho Steam
│   ├── patch_assets/           # Tài nguyên UI & Script tối ưu cho Steam (UTF-16 LE)
│   ├── steam_original_scn/     # 216 phôi SCN gốc chuẩn của Steam
│   ├── steam_compiled_scn/     # SCN đã biên dịch trên phôi Steam
│   └── unencrypted.xp3         # Tệp patch thành phẩm cho Steam
├── tools/                      # Bộ công cụ mã hóa & trích xuất
│   ├── bin/                    # scn-script-inserter.exe, scn-script-extractor.exe
│   ├── maitetsu_crypt.py       # Bộ mã hóa Maitetsu CxEncryption
│   └── scripts/                # Scripts kiểm tra tiến độ, dọn dẹp BOM, tạo custom.tjs
├── build_patch.py              # Pipeline đóng gói chính cho DMM
└── README.md                   # Tài liệu hướng dẫn chính
```

---

## Bản Quyền & Giấy Phép
Dự án được thực hiện phi thương mại nhằm mục đích học tập và phục vụ cộng đồng Visual Novel Việt Nam. Bản quyền game gốc thuộc về **Lose / CIRCUS / Hikari Field**. Hãy mua bản quyền game trên Steam/DMM để ủng hộ nhà sản xuất.
