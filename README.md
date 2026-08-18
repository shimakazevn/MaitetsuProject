# 🚂 Maitetsu: Last Run!! — Vietnamese Translation Project
<div align="center">

![Version](https://img.shields.io/badge/Patch_Version-v1.0.0-blue.svg?style=for-the-badge)
![Progress](https://img.shields.io/badge/Translation_Progress-99.1%25-brightgreen.svg?style=for-the-badge)
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
* 📜 **Khung thoại 3 dòng chuẩn (3-Line Layout)**: Tự động bung khung thoại `base.textmax` (`102px`) và scale font `0.70` cho các câu thoại dài, tạo trải nghiệm đọc thoáng đãng như bản tiếng Anh chính thức.
* ⚡ **Nạp Patch Siêu Tốc (Fast AutoPath Indexing)**: Tối ưu hóa bảng băm đường dẫn trong C++ Core của Kirikiri 2, giảm thời gian khởi động game từ **>60 giây xuống <1 giây**.
* 🎨 **Bảo toàn E-mote 2K**: Hỗ trợ đầy đủ bộ khung hình động mượt mà của nhân vật trên tất cả các nền tảng.
* 🎮 **Hỗ trợ đa phiên bản**: Module độc lập cho bản **Last Run!! Standalone** (`patch3.xp3`) và **Steam Release** (`steam_version_patch_vn/`).

---

## ⚠️ QUY TẮC BẤT DI BẤT DỊCH VỀ MÃ NGUỒN & PATCH ASSETS (DÀNH CHO AI & DEVELOPER)

> [!IMPORTANT]
> Đây là các nguyên tắc cốt lõi đã được kiểm thử thực tế 100% trên engine Kirikiri 2 của Maitetsu Last Run!!. Bất kỳ thay đổi nào làm sai lệch các nguyên tắc dưới đây đều sẽ gây crash engine (`Syntax error`, `Invalid argument count`, hoặc `Member does not exist`):

1. **Chuẩn Mã Hóa File Hệ Thống (UTF-16 LE Single BOM)**:
   * Tất cả file `.tjs`, `.ini`, `.csv`, `tw_tips_*.txt` trong `patch_assets/` **BẮT BUỘC** phải mang đúng 1 BOM UTF-16 LE duy nhất (`b'\xff\xfe'`).
   * **CẤM** decode bằng `raw.decode('utf-16le')` rồi cộng thêm `b'\xff\xfe'` khi ghi ra (sẽ bị double BOM `\ufeff\ufeff` $\rightarrow$ Kirikiri báo `Member "\ufeff..." does not exist` hoặc `Syntax error`).
   * **Quy chuẩn xử lý**: Luôn dùng `raw.decode('utf-16')` (tự động bóc BOM) $\rightarrow$ `txt.lstrip('\ufeff')` $\rightarrow$ `b'\xff\xfe' + txt.encode('utf-16le')`.

2. **Bảo Toàn 17 Bảng Bố Cục Giao Diện UI (`*.csv`)**:
   * Tuyệt đối không tự ý sinh lại hoặc convert nhầm encoding các bảng CSV. Nguồn chuẩn gốc 100% nằm tại: `extracted_assets/KrkrExtract_Output/others/uipsd/tw/`.
   * Nếu bảng CSV bị hỏng encoding, `UIListParser` sẽ không đọc được nút bấm và quăng ngoại lệ `Invalid argument count` khi khởi tạo QuickMenu.

3. **Chữ Ký Hàm TJS & Tham Số Mặc Định**:
   * Các hàm tiện ích override như `DrawTopMenuText` phải có giá trị mặc định cho tham số tùy chọn: `function DrawTopMenuText(lay, ui, ref, tag, exp = "")` để tránh lỗi `Invalid argument count` khi engine gọi 4 tham số.

4. **Cấu Trúc Tệp `patch3.xp3` Gọn Sạch (825 Tệp Chuẩn)**:
   * `patch3.xp3` chỉ chứa các tệp ghi đè tài nguyên cụ thể (tổng cộng 825 files: `custom.tjs`, `Config.tjs`, các file danh sách `.tjs`, bảng UI `.csv`, tệp `tw_tips_*.txt`, ảnh `.png`, và các kịch bản `.scn`).
   * **CẤM** nạp thừa các tệp KAG gốc (`startup.tjs`, `Initialize.tjs`, `MainWindow.tjs`, thư mục `data/`, `system/`) vào `patch3.xp3` vì sẽ gây xung đột phiên bản giữa KAG 1.0 và KAG 2.0 (`patch2.xp3`).

---

## 📊 Tiến Độ Dịch Thuật

Chạy lệnh `check_progress.bat` (hoặc `python tools/scripts/check_progress.py`) để xem thống kê thời gian thực:

| Tuyến Cốt Truyện (Route) | Thư Mục | Số File | Đã Dịch | Tiến Độ |
| :--- | :--- | :---: | :---: | :---: |
| **Common Route** (Tuyến Chung) | `00_Common` | 16 | 15 | **93.8%** |
| **Hachiroku Route** | `01_Hachiroku` | 46 | 46 | **100.0%** |
| **Hibiki Route** | `02_Hibiki` | 37 | 37 | **100.0%** |
| **Paulette Route** | `03_Paulette` | 37 | 37 | **100.0%** |
| **Reina Route** | `04_Reina` | 13 | 13 | **100.0%** |
| **Mayami Route** | `05_Mayami` | 12 | 12 | **100.0%** |
| **Kisaki Route** | `06_Kisaki` | 13 | 13 | **100.0%** |
| **Nagi & Fukami Route** | `07_Nagi_Fukami` | 28 | 27 | **96.4%** |
| **Niiroku Route** | `08_Niiroku` | 5 | 5 | **100.0%** |
| **Grand Route** | `09_Grand` | 11 | 11 | **100.0%** |
| **Chikuni (China) Route** | `10_Chikuni` | 8 | 8 | **100.0%** |
| **Extra / Other** | `11_Other` | 1 | 1 | **100.0%** |
| **TỔNG CỘNG** | **TOÀN BỘ GAME** | **227** | **225** | **99.1%** |

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
* **Đóng gói ra `patch.xp3` cho Steam**:
  ```bash
  cd steam_version_patch_vn
  python build_steam_patch.py --target "Đường_dẫn_thư_mục_Steam" --name "patch.xp3"
  ```

---

## 📂 Cấu Trúc Thư Mục Dự Án (Chuẩn & Tinh Gọn)

```
MaitetsuProject/
├── .github/workflows/          # CI/CD Build APK (Android) & IPA (iOS)
├── docs/                       # Toàn bộ tài liệu, glossary, kiến trúc kỹ thuật & dữ liệu
│   ├── ARCHITECTURE.md         # Giải thích cơ chế CxEncryption, AutoPath, TJS Hooks
│   ├── TRANSLATION_GUIDE.md    # Hướng dẫn quy chuẩn dịch thuật TOML
│   ├── GLOSSARY.md             # Từ điển danh xưng và thuật ngữ đường sắt
│   └── legacy_data/            # Dữ liệu bảng tính sao lưu cũ
├── original_scn/               # 216 file kịch bản gốc nguyên bản (.scn)
├── translation_toml/           # 227 file kịch bản dịch phân theo thư mục Route
├── patch_assets/               # 609 tài nguyên UI, font, TIPS, script hệ thống sạch (UTF-16 LE)
├── compiled_scn/               # 216 kịch bản đã biên dịch (.scn)
├── steam_version_patch_vn/     # Module đóng gói bản patch dành riêng cho Steam
│   ├── patch_assets/          # Script & UI tối ưu riêng cho Steam
│   └── build_steam_patch.py   # Script build patch Steam
├── tools/                      # Bộ công cụ biên dịch, mã hóa & đóng gói
│   ├── bin/                    # scn-script-inserter.exe, tjs2Compiler.exe, v.v.
│   ├── maitetsu_crypt.py       # Bộ mã hóa/giải mã CxEncryption
│   ├── make_patch3_maitetsu.py # Bộ đóng gói XP3 V2 tương thích 100%
│   └── scripts/                # check_progress.py, toml_to_csv.py, extract_toml.py, v.v.
├── krkr2_next/                 # Mã nguồn C++ Engine Kirikiri 2 Next (Cross-platform)
├── build_patch.py              # Script Build Pipeline chính (Standalone/Mobile)
├── build_patch.bat             # Shortcut Build trên Windows
├── check_progress.bat          # Shortcut kiểm tra tiến độ
└── README.md                   # Tài liệu tổng quan dự án
```

---

## ⚖️ Bản Quyền & Giấy Phép
Dự án được thực hiện phi thương mại nhằm mục đích học tập và phục vụ cộng đồng Visual Novel Việt Nam. Bản quyền game gốc thuộc về **Lose / CIRCUS**. Hãy mua game bản quyền trên Steam/DMM để ủng hộ nhà sản xuất!
