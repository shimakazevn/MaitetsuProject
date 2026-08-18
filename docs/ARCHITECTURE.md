# 🏛️ Maitetsu Last Run!! — Technical Architecture & Engine Hooks

Tài liệu này giải thích chi tiết kiến trúc kỹ thuật của hệ thống patch Việt hóa, cơ chế giải mã archive XP3, thứ tự ưu tiên AutoPath, và các hook can thiệp vào Kirikiri 2 engine.

---

## 1. Cơ Chế Đóng Gói & Mã Hóa Archive (`patch3.xp3`)

### 1.1 Định dạng XP3 V2 Header
Game sử dụng định dạng XP3 V2 với cấu trúc header như sau:
```
XP3_SIG (11 bytes): "XP3\r\n \n\x1a\x8b\x67\x01"
Header length (8 bytes int64): 0x17
Index Flag (4 bytes int32): 1
Reserved (1 byte): 0x80
File Count / Offset (8 bytes int64): 0
Index Position Offset (8 bytes int64): Vị trí bảng index cuối file
```

### 1.2 Thuật toán CxEncryption (`TVP_XP3_SEGM_ENCODE_RAW`)
Mỗi tệp tin trong archive (trừ bảng index) được mã hóa bằng thuật toán XOR dựa trên giá trị Adler32 hash của nội dung gốc:
1. Tính `adler32(data) & 0xFFFFFFFF`.
2. Tạo key seed từ hash thông qua bảng biến đổi `MaitetsuCxEncryption`.
3. XOR từng byte dữ liệu `data[i] ^= key_byte`.
4. Đặt cờ `flags |= 0x80000000` trong bảng index file `info` chunk.

---

## 2. Thứ Tự Nạp Archive & Runtime AutoPath Priority

### 2.1 Vấn đề Nạp Đè Archive
Theo thứ tự nạp bảng chữ cái của Kirikiri engine:
`patch.xp3` -> `patch2.xp3` -> `patch3.xp3` -> `patch_append*.xp3` -> `patch_data2.xp3`
Do ký tự `_` đứng sau chữ số `3` trong bảng mã ASCII, `patch_data2.xp3` được nạp sau `patch3.xp3` và sẽ ghi đè các file trùng tên trong `patch3.xp3`.

### 2.2 Giải Pháp Dynamic AutoPath Re-mounting
Trong file [custom.tjs](file:///E:/MaitetsuProject/patch_assets/custom.tjs), dòng lệnh đầu tiên:
```tjs
Storages.addAutoPath(System.exePath + "patch3.xp3>");
```
Lệnh này đưa `patch3.xp3>` lên đỉnh bảng tìm kiếm `AutoPath` tại runtime, đảm bảo mọi file trong `patch3.xp3` luôn có độ ưu tiên cao nhất tuyệt đối.

---

## 3. Quy Chuẩn Bảng Mã (Encoding Rules)
* **Quy Tắc Vàng**: **Toàn bộ tệp script text (`.tjs`, `.ks`, `.csv`, `.ini`, `.txt`) trong `patch_assets/` BẮT BUỘC phải lưu ở định dạng UTF-16 LE có BOM (`\xff\xfe`)**.
* **Lý do**: Trên Windows PC, engine Kirikiri 2 không hỗ trợ UTF-8 cho script text. Nếu gặp file UTF-8 không có BOM `\xff\xfe`, engine sẽ gọi `MultiByteToWideChar` theo bảng mã ANSI/Shift-JIS và gây crash với lỗi:
  ```
  Cannot convert given narrow string to wide string
  ```

---

## 4. Tự Động Ngắt Dòng (Auto Word-Wrap) & Layout 3 Dòng

### 4.1 Auto Word-Wrap cho tiếng Việt
Trong [custom.tjs](file:///E:/MaitetsuProject/patch_assets/custom.tjs):
```tjs
if (typeof global.SystemConfig != "undefined") {
    if (typeof SystemConfig.multiLangParamsMap == "undefined" || SystemConfig.multiLangParamsMap === void)
        SystemConfig.multiLangParamsMap = %[];
    SystemConfig.multiLangParamsMap["tw"] = %[word_break: 0, width_time_scale: 1];
    
    if (typeof SystemConfig.multiLangSingleFontScaleMap == "undefined" || SystemConfig.multiLangSingleFontScaleMap === void)
        SystemConfig.multiLangSingleFontScaleMap = %[];
    SystemConfig.multiLangSingleFontScaleMap["tw"] = 0.70;
}
if (typeof global.LanguageWordBreaks == "Object") {
    global.LanguageWordBreaks["tw"] = 0;
}
```
* `word_break: 0`: Kích hoạt thuật toán ngắt dòng Latin (Kinsoku / Word-Wrap), bẻ dòng tại khoảng trắng thay vì giữa chừng từ ngữ.
* `multiLangSingleFontScaleMap["tw"] = 0.70`: Thu nhỏ font tỉ lệ 0.70 để khung thoại 3 dòng hiển thị thoáng đẹp và không đè lên biểu tượng điều hướng.

### 4.2 Tự Động Kích Hoạt Khung Thoại 3 Dòng (`CustomMsgwinRender`)
Kích hoạt directive `@if (1)` trong `custom.tjs`:
```tjs
@if (1)
&RenderMsgwinPlugin.MsgwinRender = CustomMsgwinRender;
class CustomMsgwinRender extends MsgwinRender {
    // Tự động nhận diện câu dài và mở rộng sang rect base.textmax (chiều cao 102px - 3 dòng)
}
@endif
```
