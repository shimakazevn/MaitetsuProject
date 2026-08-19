import ctypes
import os
import sys
import psutil

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
PAGE_READWRITE = 0x04

dll_path = r'E:\SteamLibrary\steamapps\common\MaitetsuLastRun\KrkrExtract.Core.dll'
if not os.path.exists(dll_path):
    print(f'Error: {dll_path} not found!')
    sys.exit(1)

target_proc = None
for proc in psutil.process_iter(['pid', 'name']):
    if 'MaitetsuLastRun.exe' in proc.info['name']:
        target_proc = proc
        break

if not target_proc:
    print('MaitetsuLastRun.exe is not running. Please start the game from Steam first!')
    sys.exit(0)

pid = target_proc.pid
print(f'Found MaitetsuLastRun.exe (PID={pid})')

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
if not h_process:
    print(f'OpenProcess failed: error code {ctypes.get_last_error()}')
    sys.exit(1)

dll_bytes = dll_path.encode('utf-16le') + b'\x00\x00'
arg_address = kernel32.VirtualAllocEx(h_process, None, len(dll_bytes), MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE)
if not arg_address:
    print(f'VirtualAllocEx failed: error code {ctypes.get_last_error()}')
    sys.exit(1)

written = ctypes.c_size_t(0)
kernel32.WriteProcessMemory(h_process, arg_address, dll_bytes, len(dll_bytes), ctypes.byref(written))

load_library_w = kernel32.GetProcAddress(kernel32.GetModuleHandleW('kernel32.dll'), b'LoadLibraryW')
h_thread = kernel32.CreateRemoteThread(h_process, None, 0, load_library_w, arg_address, 0, None)
if not h_thread:
    print(f'CreateRemoteThread failed: error code {ctypes.get_last_error()}')
    sys.exit(1)

print('[SUCCESS] Injected KrkrExtract.Core.dll into MaitetsuLastRun.exe!')
kernel32.WaitForSingleObject(h_thread, 5000)
kernel32.CloseHandle(h_thread)
kernel32.CloseHandle(h_process)
