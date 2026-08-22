# Maitetsu: Last Run!! — Vietnamese Translation Project

Dự án Việt hóa hoàn chỉnh Visual Novel `まいてつ Last Run!!` (Maitetsu Last Run!!).

Dự án bao gồm hệ thống tự động hóa (Automated Toolchain Pipeline) giúp trích xuất, dịch thuật kịch bản `.toml`, biên dịch nhị phân `.scn` và đóng gói thành tệp lưu trữ nén `patch3.xp3` (cho PC / Mobile) hoặc `patch.xp3` (cho Steam). Tương thích với Windows, Android (Kirikiri 2 Next APK), iOS (IPA) và Steam.

---

## Tính Năng & Tối Ưu Nổi Bật

* **Tự động ngắt dòng (Auto Word-Wrap)**: Kích hoạt thuật toán ngắt dòng Latin/Việt hóa, ngăn chặn từ bị ngắt đôi ở cuối dòng.
* **Hệ Thống Font Động 3 Trạng Thái**: Tự động điều chỉnh kích cỡ font và khoảng cách dòng tùy theo độ dài câu thoại (1-3 dòng), loại bỏ hiện tượng lệch viền khung thoại.
* **Lịch Sử Thoại (Backlog) & Chọn Cảnh (SceneSel)**: Hook trực tiếp `CustomBacklog.drawTextBlock` để chữ không bị tràn vạch phân cách. Tối ưu font SceneSel bảo toàn cơ chế tự động rút gọn dấu `...`.
* **Việt Hóa Giao Diện**: Việt hóa hoàn toàn giao diện hệ thống, cài đặt gamepad và Extra mode. Tích hợp liên kết hỗ trợ của nhóm dịch Seikowo Team.
* **Nạp Patch Siêu Tốc (Fast AutoPath Indexing)**: Tối ưu hóa bảng băm đường dẫn trong C++ Core của Kirikiri 2, giảm thời gian khởi động game.
* **Tương Thích Tuyệt Đối Trên Mọi Nền Tảng (Windows, Android, iOS)**:
  - Tương thích hoàn toàn với Kirikiri 2 Next engine trên Android (ARM64/x86_64) và iOS (IPA).
  - Tự động bỏ qua các thư viện DLL dành riêng cho Windows (`lzfs.dll`, `shrinkCopy.dll`) một cách an toàn.
  - Tối ưu cơ chế phân giải chuỗi/template trong TJS2 VM (`applyInlineStringVariableExtract`) bảo vệ khỏi lỗi scope trên thiết bị di động.
  - Tự động chuyển đổi và làm mượt các thành phần menu Win32 khi chạy trên môi trường cảm ứng touch/mobile.
* **Bảo toàn E-mote**: Đồng bộ chính xác mã hiệu nhân vật (Actor ID) và layer animation E-mote riêng biệt cho từng phiên bản (DMM vs Steam), khắc phục lỗi biến mất sprite nhân vật.
* **Hỗ trợ đa nền tảng**:
  - DMM / PC Standalone / Mobile: Đóng gói `patch3.xp3` (CxEncryption).
  - Steam Release: Đóng gói `unencrypted.xp3` (Chuẩn KrkrPatch Proxy).

---

## Lưu Ý Kỹ Thuật (Dành Cho Developer)

1. **Chuẩn Mã Hóa File Hệ Thống**:
   * Tất cả file `.tjs`, `.ini`, `.csv`, `tw_tips_*.txt` trong `patch_assets/` phải mang chuẩn UTF-16 LE Single BOM (`b'\xff\xfe'`).

2. **Bố Cục Giao Diện UI (`*.csv`)**:
   * Các bảng UI CSV lấy từ nguồn gốc tại: `extracted_assets/KrkrExtract_Output/others/uipsd/tw/`. Cẩn trọng với encoding khi chỉnh sửa để tránh lỗi `Invalid argument count` ở `UIListParser`.

3. **Cấu Trúc Tệp `patch3.xp3`**:
   * `patch3.xp3` chỉ chứa các tệp ghi đè tài nguyên cụ thể. Tránh nạp thừa các tệp KAG gốc (`startup.tjs`, thư mục `data/`, `system/`) vào `patch3.xp3` vì sẽ gây xung đột phiên bản.

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
Bản Steam được tích hợp bảo vệ (KrkrSign RSA & FileHash Filter), vì vậy chúng ta áp dụng hook thông qua **KrkrPatch (`version.dll`)**:
1. Đóng gói thư mục patch thành `unencrypted.xp3`.
2. Sao chép `unencrypted.xp3` (hoặc `patch.xp3`) và `version.dll` vào thư mục game Steam (`.../steamapps/common/MaitetsuLastRun/`).
3. Khởi động game trực tiếp từ Steam. Patch sẽ tự động nạp mà vẫn giữ nguyên Steam Overlay, Achievements và Cloud Save.

---

## Hướng Dẫn Đóng Gói Patch (Build Pipelines)

### 1. Bản PC Standalone / Mobile (Android & iOS)
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
  cd steam_version_patch_vn
  python build_steam_patch.py
  ```
* **Tái tạo lại toàn bộ từ điển TIPS sạch**:
  ```bash
  python tools/scripts/rebuild_all_tips_clean.py
  ```

---

## Cấu Trúc Thư Mục Dự Án

```
MaitetsuProject/
├── .agents/                    # Bộ quy tắc dự án & hướng dẫn
├── .github/workflows/          # CI/CD Build APK (Android) & IPA (iOS)
├── docs/                       # Tài liệu, glossary, kiến trúc kỹ thuật
├── original_scn/               # 216 file kịch bản gốc nguyên bản (.scn)
├── translation_toml/           # 227 file kịch bản dịch phân theo thư mục
├── patch_assets/               # Tài nguyên UI, font, TIPS, script hệ thống (UTF-16 LE)
├── compiled_scn/               # 216 kịch bản đã biên dịch (.scn)
├── steam_version_patch_vn/     # Phân hệ Patch dành riêng cho Steam
│   ├── KrkrExtract_Output/     # Bộ Asset gốc của Steam (Backup)
│   ├── build_steam_patch.py    # Script đóng gói tự động cho Steam
│   ├── patch_assets/           # Tài nguyên UI & Script tối ưu cho Steam
│   ├── steam_original_scn/     # 216 phôi SCN gốc chuẩn của Steam
│   ├── steam_compiled_scn/     # SCN đã biên dịch trên phôi Steam
│   └── unencrypted.xp3         # Tệp patch thành phẩm cho Steam
├── tools/                      # Bộ công cụ mã hóa & trích xuất
│   ├── bin/                    # scn-script-inserter.exe, scn-script-extractor.exe
│   ├── maitetsu_crypt.py       # Bộ mã hóa Maitetsu CxEncryption
│   └── scripts/                # Scripts kiểm tra tiến độ, đối soát diff
├── build_patch.py              # Pipeline đóng gói chính cho DMM
└── README.md                   # Tài liệu hướng dẫn chính
```

---

## Bản Quyền & Giấy Phép
Dự án được thực hiện phi thương mại nhằm mục đích học tập và phục vụ cộng đồng Visual Novel Việt Nam. Bản quyền game gốc thuộc về **Lose / CIRCUS / Hikari Field**. Hãy mua bản quyền game trên Steam/DMM để ủng hộ nhà sản xuất.
