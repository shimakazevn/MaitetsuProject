# 🚂 Maitetsu: Last Run!! — Vietnamese Translation Project
<div align="center">

![Version](https://img.shields.io/badge/Patch_Version-v1.0.0-blue.svg?style=for-the-badge)
![Progress](https://img.shields.io/badge/Translation_Progress-100%25-brightgreen.svg?style=for-the-badge)
![Platforms](https://img.shields.io/badge/Platform-Windows_%7C_Android_%7C_iOS_%7C_Steam-orange.svg?style=for-the-badge)
![Engine](https://img.shields.io/badge/Engine-Kirikiri_2_/_KAG3-lightgrey.svg?style=for-the-badge)

**Dự án Việt hóa hoàn chỉnh Visual Novel đỉnh cao `まいてつ Last Run!!` (Maitetsu Last Run!!)**

[📖 Hướng Dẫn Cài Đặt](#-hướng-dẫn-cài-đặt) • [🛠️ Cách Đóng Gói Patch](#-cách-đóng-gói-patch-1-click) • [📂 Cấu Trúc Dự Án](#-cấu-trúc-thư-mục-dự-án) • [⚠️ Quy Tắc Bất Di Bất Dịch](#-quy-tắc-bất-di-bất-dịch-về-mã-nguồn--patch-assets) • [📚 Tài Liệu Kỹ Thuật](#-tài-liệu-kỹ-thuật)

</div>

---

## 🌟 Tổng Quan Dự Án
Dự án được xây dựng với hệ thống tự động hóa cao (Automated Toolchain Pipeline) giúp trích xuất, dịch thuật kịch bản `.toml`, biên dịch nhị phân `.scn` và đóng gói thành tệp lưu trữ nén `patch3.xp3` (bản Standalone / PC / Mobile) hoặc `patch.xp3` (bản Steam) tương thích 100% trên cả **PC Windows**, **Android (Kirikiri 2 Next APK)**, **iOS (IPA)** và **Steam**.

### ✨ Các Tính Năng & Tối Ưu Nổi Bật:
* 🔤 **Tự động ngắt dòng thông minh (Auto Word-Wrap)**: Kích hoạt thuật toán ngắt dòng Latin/Việt hóa (`word_break: 0`), ngăn chặn triệt để tình trạng từ bị ngắt đôi ở cuối dòng.
* 📐 **Hệ Thống Font Động 3 Trạng Thái (3-State Dynamic Font Architecture)**:
  - **Trạng thái 1 (1-2 Dòng tiêu chuẩn)**: Cỡ chữ 100% (26px), line-spacing 7px, căn giữa `oy = 60px` (Margin Trên 35px / Dưới 36px).
  - **Trạng thái 2 (2-3 Dòng trung gian)**: Cỡ chữ 91% (23.5px), line-spacing 5px, căn giữa `oy = 64px` (Margin Trên 39px / Dưới 39px).
  - **Trạng thái 3 (3 Dòng mở rộng)**: Tự động bung khung thoại `base.textmax` (`102px`), cỡ chữ 82% (21px), line-spacing 4px, căn giữa `oy = 51px` (Margin Trên 26px / Dưới 29px), loại bỏ hoàn toàn hiện tượng lệch viền trên/dưới.
* 📜 **Lịch Sử Thoại (Backlog) & Chọn Cảnh (SceneSel) Hoàn Thiện**:
  - Hook trực tiếp `CustomBacklog.drawTextBlock` co font `19px` và khoảng cách dòng `2px` cho câu 3 dòng, không bị tràn qua vạch phân cách.
  - Tối ưu kích thước font SceneSel `21px` bảo toàn cơ chế tự động rút gọn dấu 3 chấm (`...`) tích hợp sẵn của game.
* 🌐 **Tích Hợp Menu & Việt Hóa Giao Diện Hệ Thống**:
  - Menu Trợ Giúp tích hợp 3 liên kết chính thức của nhóm dịch **Seikowo Team** (Trang chủ Patch, Fanpage, Discord).
  - Việt hóa 100% hộp thoại Cài đặt nút tay cầm chơi game (Gamepad) và giao diện Extra mode.
* ⚡ **Nạp Patch Siêu Tốc (Fast AutoPath Indexing)**: Tối ưu hóa bảng băm đường dẫn trong C++ Core của Kirikiri 2, giảm thời gian khởi động game từ **>60 giây xuống <1 giây**.
* 🎨 **Bảo toàn E-mote 2K Native**: Đồng bộ chính xác mã hiệu nhân vật (Actor ID) và layer animation E-mote riêng biệt cho từng phiên bản (DMM vs Steam), loại bỏ hoàn toàn lỗi biến mất sprite nhân vật.
* 🎮 **Hỗ trợ đa phiên bản độc lập**:
  - **DMM / PC Standalone / Mobile**: Đóng gói `patch3.xp3` (Mã hóa Maitetsu CX Encryption).
  - **Steam Release**: Đóng gói `unencrypted.xp3` (Chuẩn KrkrPatch Proxy / Native Pack Setting).


---

## ⚠️ QUY TẮC BẤT DI BẤT DỊCH VỀ MÃ NGUỒN & PATCH ASSETS (DÀNH CHO AI & DEVELOPER)

> [!IMPORTANT]
> Đây là các nguyên tắc cốt lõi đã được kiểm thử thực tế 100% trên engine Kirikiri 2 của Maitetsu Last Run!!. Bất kỳ thay đổi nào làm sai lệch các nguyên tắc dưới đây đều sẽ gây crash engine (`Syntax error`, `Invalid argument count`, hoặc `Member does not exist`):

1. **Sự Khác Biệt Bytecode Giữa Bản DMM và Bản Steam**:
   * **CẤM** dùng chung file nhị phân `.scn` giữa DMM và Steam! Bản Steam có mã opcode và ánh xạ chỉ số E-mote actor khác DMM. Nếu lấy `.scn` của DMM bỏ vào Steam, nhân vật (Nagi, Hibiki...) sẽ bị mất hiển thị trên màn hình.
   * **Quy chuẩn**: Khi biên dịch SCN cho Steam, luôn dùng phôi gốc Steam (`steam_original_scn/`) kết hợp với `scn-script-inserter.exe`.

2. **Chuẩn Mã Hóa File Hệ Thống (UTF-16 LE Single BOM)**:
   * Tất cả file `.tjs`, `.ini`, `.csv`, `tw_tips_*.txt` trong `patch_assets/` **BẮT BUỘC** phải mang đúng 1 BOM UTF-16 LE duy nhất (`b'\xff\xfe'`).
   * **CẤM** decode bằng `raw.decode('utf-16le')` rồi cộng thêm `b'\xff\xfe'` khi ghi ra (sẽ bị double BOM `\ufeff\ufeff` $\rightarrow$ Kirikiri báo `Member "\ufeff..." does not exist` hoặc `Syntax error`).
   * **Quy chuẩn xử lý**: Luôn dùng `raw.decode('utf-16')` (tự động bóc BOM) $\rightarrow$ `txt.lstrip('\ufeff')` $\rightarrow$ `b'\xff\xfe' + txt.encode('utf-16le')`.

3. **Thứ Tự Nạp AutoPath Tối Cao Trong `custom.tjs`**:
   * Để patch đè lên các tệp `patch_append*.xp3` và `others.xp3`, dòng đầu tiên của `custom.tjs` **BẮT BUỘC** phải là:
     - Với DMM: `Storages.addAutoPath(System.exePath + "patch3.xp3>");`
     - Với Steam: `Storages.addAutoPath(System.exePath + "unencrypted.xp3>");`

4. **Bảo Toàn 17 Bảng Bố Cục Giao Diện UI (`*.csv`)**:
   * Tuyệt đối không tự ý sinh lại hoặc convert nhầm encoding các bảng CSV. Nguồn chuẩn gốc 100% nằm tại: `extracted_assets/KrkrExtract_Output/others/uipsd/tw/`.
   * Nếu bảng CSV bị hỏng encoding, `UIListParser` sẽ không đọc được nút bấm và quăng ngoại lệ `Invalid argument count` khi khởi tạo QuickMenu.

5. **Chữ Ký Hàm TJS & Tham Số Mặc Định**:
   * Các hàm tiện ích override như `DrawTopMenuText` phải có giá trị mặc định cho tham số tùy chọn: `function DrawTopMenuText(lay, ui, ref, tag, exp = "")` để tránh lỗi `Invalid argument count` khi engine gọi 4 tham số.

6. **Cấu Trúc Tệp `patch3.xp3` Gọn Sạch (825 Tệp Chuẩn)**:
   * `patch3.xp3` chỉ chứa các tệp ghi đè tài nguyên cụ thể (tổng cộng 825 files: `custom.tjs`, `Config.tjs`, các file danh sách `.tjs`, bảng UI `.csv`, tệp `tw_tips_*.txt`, ảnh `.png`, và các kịch bản `.scn`).
   * **CẤM** nạp thừa các tệp KAG gốc (`startup.tjs`, `Initialize.tjs`, `MainWindow.tjs`, thư mục `data/`, `system/`) vào `patch3.xp3` vì sẽ gây xung đột phiên bản giữa KAG 1.0 và KAG 2.0 (`patch2.xp3`).

---

## 📊 Tiến Độ Dịch Thuật

Chạy lệnh `check_progress.bat` (hoặc `python tools/scripts/check_progress.py`) để xem thống kê thời gian thực:

| Tuyến Cốt Truyện (Route) | Thư Mục | Số File | Đã Dịch | Tiến Độ |
| :--- | :--- | :---: | :---: | :---: |
| **Common Route** (Tuyến Chung) | `00_Common` | 16 | 16 | **100.0%** |
| **Hachiroku Route** | `01_Hachiroku` | 46 | 46 | **100.0%** |
| **Hibiki Route** | `02_Hibiki` | 37 | 37 | **100.0%** |
| **Paulette Route** | `03_Paulette` | 37 | 37 | **100.0%** |
| **Reina Route** | `04_Reina` | 13 | 13 | **100.0%** |
| **Mayami Route** | `05_Mayami` | 12 | 12 | **100.0%** |
| **Kisaki Route** | `06_Kisaki` | 13 | 13 | **100.0%** |
| **Nagi & Fukami Route** | `07_Nagi_Fukami` | 28 | 28 | **100.0%** |
| **Niiroku Route** | `08_Niiroku` | 5 | 5 | **100.0%** |
| **Grand Route** | `09_Grand` | 11 | 11 | **100.0%** |
| **Chikuni (China) Route** | `10_Chikuni` | 8 | 8 | **100.0%** |
| **Extra / Other** | `11_Other` | 1 | 1 | **100.0%** |
| **TỔNG CỘNG** | **TOÀN BỘ GAME** | **227** | **227** | **100.0%** |

---

## 📖 Hướng Dẫn Cài Đặt Patch

### 1. Bản PC Gốc Nhật (DMM / DLsite / DVD) & Mobile (Android / iOS)
* **PC Windows**: Sao chép tệp `patch3.xp3` vào thư mục cài đặt game (cùng cấp với `まいてつ Last Run!!.exe`).
* **Android (Kirikiri 2 Next)**: Sao chép tệp `patch3.xp3` vào thư mục chứa dữ liệu game trên điện thoại.
* *Lưu ý:* Bản DMM/Mobile sử dụng cơ chế giải mã gốc **Maitetsu CxEncryption** nên hoạt động 100% độc lập, không cần thêm bất kỳ tệp DLL can thiệp nào.

### 2. Bản Steam (Hikari Field / Maitetsu: Last Run!!)
Do bản Steam được tích hợp thêm 2 lớp bảo vệ chống sửa đổi (**KrkrSign RSA Digital Signature** và **Dynamic FileHash Filter**), bản patch tiếng Việt áp dụng giải pháp hook chuẩn quốc tế qua **KrkrPatch (`version.dll`)**:
1. Đóng gói thư mục patch thành `unencrypted.xp3` (hoặc chạy `build_steam_patch.py`).
2. Sao chép `unencrypted.xp3` (hoặc `patch.xp3`) và `version.dll` vào thư mục game Steam (`.../steamapps/common/MaitetsuLastRun/`).
3. Khởi động game trực tiếp từ Steam. Patch sẽ tự động nạp mà vẫn giữ nguyên **Steam Overlay**, **Steam Achievements (Thành tựu)** và **Cloud Save**.

---

## 📊 Tiến Độ Dịch Thuật

Chạy lệnh `check_progress.bat` (hoặc `python tools/scripts/check_progress.py`) để xem thống kê thời gian thực:

| Tuyến Cốt Truyện (Route) | Thư Mục | Số File | Đã Dịch | Tiến Độ |
| :--- | :--- | :---: | :---: | :---: |
| **Common Route** (Tuyến Chung) | `00_Common` | 16 | 16 | **100.0%** |
| **Hachiroku Route** | `01_Hachiroku` | 46 | 46 | **100.0%** |
| **Hibiki Route** | `02_Hibiki` | 37 | 37 | **100.0%** |
| **Paulette Route** | `03_Paulette` | 37 | 37 | **100.0%** |
| **Reina Route** | `04_Reina` | 13 | 13 | **100.0%** |
| **Mayami Route** | `05_Mayami` | 12 | 12 | **100.0%** |
| **Kisaki Route** | `06_Kisaki` | 13 | 13 | **100.0%** |
| **Nagi & Fukami Route** | `07_Nagi_Fukami` | 28 | 28 | **100.0%** |
| **Niiroku Route** | `08_Niiroku` | 5 | 5 | **100.0%** |
| **Grand Route** | `09_Grand` | 11 | 11 | **100.0%** |
| **Chikuni (China) Route** | `10_Chikuni` | 8 | 8 | **100.0%** |
| **Extra / Other** | `11_Other` | 1 | 1 | **100.0%** |
| **TỔNG CỘNG** | **TOÀN BỘ GAME** | **227** | **227** | **100.0%** |

---

## 🚀 Hướng Dẫn Đóng Gói Patch (Build Pipelines)

### 1. Bản PC Standalone / Mobile (Android & iOS)
* **Build Toàn Bộ & Đóng Gói `patch3.xp3`**:
  ```bash
  python build_patch.py
  # Hoặc nhấp đúp file: build_patch.bat
  ```
* **Chỉ Đóng Gói Lại XP3 (Bỏ qua biên dịch SCN)**:
  ```bash
  python build_patch.py --pack-only
  ```

### 2. Bản Steam Release
* **Đóng gói patch cho Steam (Tự động sync)**:
  ```bash
  cd steam_version_patch_vn
  python build_steam_patch.py
  ```
* **Tái tạo toàn bộ từ điển TIPS sạch**:
  ```bash
  python tools/scripts/rebuild_all_tips_clean.py
  ```

---

## 📂 Cấu Trúc Thư Mục Dự Án (Chuẩn & Tinh Gọn)

```
MaitetsuProject/
├── .agents/                    # Bộ quy tắc dự án & hướng dẫn AI pair-programming
├── .github/workflows/          # CI/CD Build APK (Android) & IPA (iOS)
├── docs/                       # Toàn bộ tài liệu, glossary, kiến trúc kỹ thuật & dữ liệu
│   ├── ARCHITECTURE.md         # Giải thích cơ chế CxEncryption, AutoPath, TJS Hooks
│   ├── TRANSLATION_GUIDE.md    # Hướng dẫn quy chuẩn dịch thuật TOML
│   └── GLOSSARY.md             # Từ điển danh xưng và thuật ngữ đường sắt
├── original_scn/               # 216 file kịch bản gốc nguyên bản (.scn)
├── translation_toml/           # 227 file kịch bản dịch phân theo thư mục Route
├── patch_assets/               # Tài nguyên UI, font, TIPS, script hệ thống sạch (UTF-16 LE)
├── compiled_scn/               # 216 kịch bản đã biên dịch (.scn)
├── steam_version_patch_vn/         # Phân hệ Patch dành riêng cho Steam
│   ├── KrkrExtract_Output/         # Bộ Asset gốc sạch 100% của Steam (Backup)
│   ├── build_steam_patch.py        # Script đóng gói tự động cho Steam
│   ├── patch_assets/               # Tài nguyên UI & Script đã tối ưu cho Steam
│   ├── steam_original_scn/         # 216 phôi SCN gốc chuẩn của Steam
│   ├── steam_compiled_scn/         # SCN đã biên dịch trên phôi Steam
│   └── unencrypted.xp3             # Tệp patch thành phẩm cho Steam
│
├── tools/                          # Bộ công cụ mã hóa & trích xuất
│   ├── bin/                        # scn-script-inserter.exe, scn-script-extractor.exe
│   ├── maitetsu_crypt.py           # Bộ mã hóa Maitetsu CxEncryption (Adler32/ControlBlock)
│   └── scripts/                    # Scripts kiểm tra tiến độ, đối soát diff
│
├── build_patch.py                  # Pipeline đóng gói chính cho DMM
└── README.md                       # Tài liệu hướng dẫn chính
```

---

## ⚖️ Bản Quyền & Giấy Phép
Dự án được thực hiện phi thương mại nhằm mục đích học tập và phục vụ cộng đồng Visual Novel Việt Nam. Bản quyền game gốc thuộc về **Lose / CIRCUS / Hikari Field**. Hãy mua game bản quyền trên Steam/DMM để ủng hộ nhà sản xuất!
