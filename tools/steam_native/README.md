# tools/steam_native — Engine-Oracle Capture cho Maitetsu Steam

Sinh ra bản `steam_version_patch_vn/patch.xp3` **mã hóa native**: engine Steam tự
giải mã như DLC chính chủ — end-user chỉ cần 1 file, **không cần version.dll**.

## Thành phần
| File | Vai trò |
|---|---|
| `capture_version.dll` | DLL capture: hook `tTVPXP3Archive::CreateStreamByIndex`, lưu output bộ lọc CX vào `steam_capture\%08X.bin`; với probe archive thì trả stream thô để game vẫn chạy; sau 60s tự dump toàn bộ entry |
| `capture_source_Patcher.h` | Nguồn `Patcher.h` đã vá (để build lại DLL — đè lên `tools/KirikiriTools/KirikiriUnencryptedArchive/Patcher.h` rồi msbuild Win32 Release) |
| `steam_native_pipeline.py` | Thư viện: assemble_staging / pack_plain / coverage_report / pack_final |

## Nguyên lý
1. Bộ lọc CX của engine áp dụng **mọi entry** và là **XOR involutive** ⇒ `F(plaintext) = ciphertext`
2. Tham số sinh tại runtime, không extract tĩnh được ⇒ dùng chính engine làm oracle
3. Archive thành phẩm: entry RAW + `info.flags |= 0x80000000` + `adlr = adler32(plaintext)`
4. Engine không yêu cầu `.sig` cho archive thiếu chữ ký (đã kiểm chứng)

## Quy tắc nội dung liên quan
- `patch_assets/custom.tjs` phải remount `patch.xp3>` (KHÔNG được tham chiếu
  `unencrypted.xp3` — sẽ gây lỗi "Cannot find storage" lúc boot).
- Toàn bộ script `.tjs/.csv/.ini` chuẩn UTF-16 LE BOM.

## Xử lý sự cố
| Triệu chứng | Nguyên nhân | Cách xử |
|---|---|---|
| Boot hiện "Cannot convert given narrow string to wide string" | Deploy nhầm bản plaintext/DMM-scheme sang Steam | Chạy lại chu kỳ capture → final |
| "Cannot find storage ...unencrypted.xp3" | custom.tjs còn remount tên cũ | Sửa custom.tjs rồi chạy lại chu kỳ |
| `[final] ABORT: thieu captures!` | Đổi nội dung file nhưng chưa capture lại | `--install-capture` → boot game → chạy default |
