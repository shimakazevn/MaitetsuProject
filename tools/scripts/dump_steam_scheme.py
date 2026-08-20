import sys
import ctypes
import struct
import json
import re
import subprocess
from ctypes import wintypes

PROCESS_VM_READ = 0x0010
PROCESS_QUERY_INFORMATION = 0x0400

kernel32 = ctypes.windll.kernel32

class MEMORY_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ('BaseAddress', ctypes.c_void_p),
        ('AllocationBase', ctypes.c_void_p),
        ('AllocationProtect', wintypes.DWORD),
        ('RegionSize', ctypes.c_size_t),
        ('State', wintypes.DWORD),
        ('Protect', wintypes.DWORD),
        ('Type', wintypes.DWORD),
    ]

kernel32.ReadProcessMemory.argtypes = [
    wintypes.HANDLE,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t)
]
kernel32.ReadProcessMemory.restype = wintypes.BOOL

kernel32.VirtualQueryEx.argtypes = [
    wintypes.HANDLE,
    ctypes.c_void_p,
    ctypes.POINTER(MEMORY_BASIC_INFORMATION),
    ctypes.c_size_t
]
kernel32.VirtualQueryEx.restype = ctypes.c_size_t

def get_pid():
    out = subprocess.check_output('tasklist /FI "IMAGENAME eq MaitetsuLastRun.exe" /FO CSV /NH', shell=True).decode('utf-8', errors='ignore')
    for line in out.strip().splitlines():
        parts = [p.strip('"') for p in line.split(',')]
        if len(parts) >= 2 and 'Maitetsu' in parts[0]:
            return int(parts[1])
    return None

def main():
    pid = get_pid()
    if not pid:
        print("[ERROR] MaitetsuLastRun.exe is not running.", flush=True)
        sys.exit(1)

    print(f"[OK] Found MaitetsuLastRun.exe (PID: {pid})", flush=True)
    hProcess = kernel32.OpenProcess(PROCESS_VM_READ | PROCESS_QUERY_INFORMATION, False, pid)
    if not hProcess:
        print(f"[ERROR] Could not open process {pid}: {ctypes.GetLastError()}", flush=True)
        sys.exit(1)

    MEM_COMMIT = 0x1000
    PAGE_READWRITE = 0x04
    PAGE_READONLY = 0x02
    PAGE_EXECUTE_READWRITE = 0x40

    address = 0
    mbi = MEMORY_BASIC_INFORMATION()
    scanned_bytes = 0
    found_candidates = []

    print("[*] Scanning process memory with fast C-matcher...", flush=True)
    
    # 6 possible permutations of [0, 1, 2] in 32-bit ints
    prolog_patterns = [
        struct.pack('<3I', p[0], p[1], p[2])
        for p in [
            (0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0)
        ]
    ]

    while address < 0x7FFF0000:
        res = kernel32.VirtualQueryEx(hProcess, ctypes.c_void_p(address), ctypes.byref(mbi), ctypes.sizeof(mbi))
        if not res or not mbi.RegionSize:
            break

        base_addr = mbi.BaseAddress if mbi.BaseAddress is not None else address
        region_size = mbi.RegionSize

        if mbi.State == MEM_COMMIT and (mbi.Protect in [PAGE_READWRITE, PAGE_READONLY, PAGE_EXECUTE_READWRITE, 0x20]):
            buf = (ctypes.c_char * region_size)()
            nRead = ctypes.c_size_t(0)
            if kernel32.ReadProcessMemory(hProcess, ctypes.c_void_p(base_addr), ctypes.byref(buf), region_size, ctypes.byref(nRead)):
                raw = bytes(buf[:nRead.value])
                scanned_bytes += len(raw)
                
                # Fast search for prolog patterns
                for pat in prolog_patterns:
                    start_pos = 0
                    while True:
                        idx = raw.find(pat, start_pos)
                        if idx == -1:
                            break
                        start_pos = idx + 4
                        
                        # Validate next 24 bytes (Odd branch) and 32 bytes (Even branch)
                        if idx + 68 + 8192 <= len(raw):
                            odd = raw[idx+12:idx+36]
                            even = raw[idx+36:idx+68]
                            odd_ints = struct.unpack('<6I', odd)
                            even_ints = struct.unpack('<8I', even)
                            if set(odd_ints) == set(range(6)) and set(even_ints) == set(range(8)):
                                cb = raw[idx+68:idx+68+8192]
                                cb_ints = struct.unpack('<2048I', cb)
                                if len(set(cb_ints)) > 1900: # High entropy ControlBlock
                                    mask_cand = struct.unpack('<I', raw[idx-8:idx-4])[0] if idx >= 8 else 0
                                    off_cand = struct.unpack('<I', raw[idx-4:idx])[0] if idx >= 4 else 0
                                    found_candidates.append({
                                        'base_addr': hex(base_addr + idx),
                                        'm_mask': mask_cand,
                                        'm_offset': off_cand,
                                        'PrologOrder': list(struct.unpack('<3I', pat)),
                                        'OddBranchOrder': list(odd_ints),
                                        'EvenBranchOrder': list(even_ints),
                                        'ControlBlock': list(cb_ints)
                                    })

        address = base_addr + region_size

    kernel32.CloseHandle(hProcess)
    print(f"[*] Scanned {scanned_bytes / (1024*1024):.2f} MB of process memory.", flush=True)
    print(f"[+] Found {len(found_candidates)} Steam Cxdec candidate(s)!", flush=True)
    
    for i, c in enumerate(found_candidates, 1):
        print(f"\n--- Candidate #{i} at {c['base_addr']} ---", flush=True)
        print(f"  m_mask:   {c['m_mask']} (hex: {hex(c['m_mask'])})", flush=True)
        print(f"  m_offset: {c['m_offset']} (hex: {hex(c['m_offset'])})", flush=True)
        print(f"  PrologOrder:     {c['PrologOrder']}", flush=True)
        print(f"  OddBranchOrder:  {c['OddBranchOrder']}", flush=True)
        print(f"  EvenBranchOrder: {c['EvenBranchOrder']}", flush=True)
        print(f"  ControlBlock[0..4]: {c['ControlBlock'][:5]}", flush=True)
        
        out_json = r"E:\MaitetsuProject\steam_version_patch_vn\steam_maitetsu_scheme.json"
        with open(out_json, "w", encoding="utf-8") as fp:
            json.dump(c, fp, indent=2)
        print(f"  -> Saved Steam Scheme to {out_json}", flush=True)

if __name__ == "__main__":
    main()
