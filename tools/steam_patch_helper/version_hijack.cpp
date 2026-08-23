// version_hijack.cpp - Based on KirikiriTools + direct global patching
// The key insight: PackinOne.dll stores the exporter at a fixed global offset.
// We patch that global AFTER V2Link runs to redirect all calls through our proxy.

// Forward export pragmas for version.dll proxy
#pragma comment(linker, "/export:GetFileVersionInfoA=C:\\Windows\\System32\\version.GetFileVersionInfoA")
#pragma comment(linker, "/export:GetFileVersionInfoByHandle=C:\\Windows\\System32\\version.GetFileVersionInfoByHandle")
#pragma comment(linker, "/export:GetFileVersionInfoExA=C:\\Windows\\System32\\version.GetFileVersionInfoExA")
#pragma comment(linker, "/export:GetFileVersionInfoExW=C:\\Windows\\System32\\version.GetFileVersionInfoExW")
#pragma comment(linker, "/export:GetFileVersionInfoSizeA=C:\\Windows\\System32\\version.GetFileVersionInfoSizeA")
#pragma comment(linker, "/export:GetFileVersionInfoSizeExA=C:\\Windows\\System32\\version.GetFileVersionInfoSizeExA")
#pragma comment(linker, "/export:GetFileVersionInfoSizeExW=C:\\Windows\\System32\\version.GetFileVersionInfoSizeExW")
#pragma comment(linker, "/export:GetFileVersionInfoSizeW=C:\\Windows\\System32\\version.GetFileVersionInfoSizeW")
#pragma comment(linker, "/export:GetFileVersionInfoW=C:\\Windows\\System32\\version.GetFileVersionInfoW")
#pragma comment(linker, "/export:VerFindFileA=C:\\Windows\\System32\\version.VerFindFileA")
#pragma comment(linker, "/export:VerFindFileW=C:\\Windows\\System32\\version.VerFindFileW")
#pragma comment(linker, "/export:VerInstallFileA=C:\\Windows\\System32\\version.VerInstallFileA")
#pragma comment(linker, "/export:VerInstallFileW=C:\\Windows\\System32\\version.VerInstallFileW")
#pragma comment(linker, "/export:VerLanguageNameA=C:\\Windows\\System32\\version.VerLanguageNameA")
#pragma comment(linker, "/export:VerLanguageNameW=C:\\Windows\\System32\\version.VerLanguageNameW")
#pragma comment(linker, "/export:VerQueryValueA=C:\\Windows\\System32\\version.VerQueryValueA")
#pragma comment(linker, "/export:VerQueryValueW=C:\\Windows\\System32\\version.VerQueryValueW")

#include <windows.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <algorithm>

// ============================================================
// Logging
// ============================================================
void Log(const char* fmt, ...) {
    FILE* f = fopen("E:\\MaitetsuProject\\version_hijack.log", "a");
    if (!f) return;
    va_list args;
    va_start(args, fmt);
    vfprintf(f, fmt, args);
    va_end(args);
    fclose(f);
}

// ============================================================
// PackinOne memory dumper (scheme reflection for native patch)
// ============================================================
static HMODULE g_PackinOneMod = NULL;

static void DumpPackinOneImage(const char* tag) {
    if (!g_PackinOneMod) return;
    char path[MAX_PATH];
    snprintf(path, sizeof(path), "E:\\MaitetsuProject\\steam_packinone_dump_%s.bin", tag);
    HANDLE f = CreateFileA(path, GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    if (f == INVALID_HANDLE_VALUE) { Log("Dump %s: CreateFile failed", tag); return; }
    PIMAGE_DOS_HEADER dos = (PIMAGE_DOS_HEADER)g_PackinOneMod;
    PIMAGE_NT_HEADERS nt = (PIMAGE_NT_HEADERS)((BYTE*)g_PackinOneMod + dos->e_lfanew);
    DWORD imgSize = nt->OptionalHeader.SizeOfImage;
    DWORD written = 0;
    WriteFile(f, (LPCVOID)g_PackinOneMod, imgSize, &written, NULL);
    CloseHandle(f);
    Log("Dump %s: wrote %lu / %lu bytes", tag, written, imgSize);
}

// ============================================================
// XP3 Extraction Filter types
// ============================================================
#include "hashes.h"

struct tTVPXP3ExtractionFilterInfo {
    uint32_t SizeOfSelf;
    uint64_t Offset;
    void *   Buffer;
    uint32_t BufferSize;
    uint32_t FileHash;
};

typedef void (__cdecl *tTVPXP3ArchiveExtractionFilter)(tTVPXP3ExtractionFilterInfo *info);
typedef void (__cdecl *tTVPSetXP3ArchiveExtractionFilter)(tTVPXP3ArchiveExtractionFilter filter);

static tTVPSetXP3ArchiveExtractionFilter g_TVPSetXP3ArchiveExtractionFilter = NULL;
static tTVPXP3ArchiveExtractionFilter    g_OriginalFilter = NULL;

void __cdecl SmartSteamExtractionFilter(tTVPXP3ExtractionFilterInfo *info) {
    if (!info || !info->Buffer || info->BufferSize == 0) return;
    static bool dumped_at_extract = false;
    if (!dumped_at_extract) {
        dumped_at_extract = true;
        Log("First extraction -> dumping PackinOne image (extract)\n");
        DumpPackinOneImage("extract");
    }
    if (std::binary_search(std::begin(g_WhitelistHashes), std::end(g_WhitelistHashes), info->FileHash)) {
        Log("Filter: Bypassing 0x%08X (patch3 file)\n", info->FileHash);
        return;
    }
    if (g_OriginalFilter) g_OriginalFilter(info);
}

void __cdecl FakeTVPSetXP3ArchiveExtractionFilter(tTVPXP3ArchiveExtractionFilter filter) {
    Log("FakeTVPSetXP3: PackinOne registered filter %p\n", filter);
    g_OriginalFilter = filter;
    Log("Filter registered -> dumping PackinOne image (filter)\n");
    DumpPackinOneImage("filter");
    if (g_TVPSetXP3ArchiveExtractionFilter) {
        Log("FakeTVPSetXP3: Installing SmartSteamExtractionFilter\n");
        g_TVPSetXP3ArchiveExtractionFilter(SmartSteamExtractionFilter);
    }
}

// ============================================================
// iTVPFunctionExporter - TJS_INTF_METHOD = __cdecl !
// ============================================================
struct iTVPFunctionExporter {
    virtual bool __cdecl QueryFunctions(const wchar_t** name, void** function, unsigned int count) = 0;
    virtual bool __cdecl QueryFunctionsByNarrowString(const char** name, void** function, unsigned int count) = 0;
};

// ============================================================
// ProxyFunctionExporter
// Intercepts TVPSetXP3ArchiveExtractionFilter queries
// ============================================================
class ProxyFunctionExporter : public iTVPFunctionExporter {
public:
    iTVPFunctionExporter* real;
    ProxyFunctionExporter(iTVPFunctionExporter* r) : real(r) {}

    bool __cdecl QueryFunctions(const wchar_t** name, void** function, unsigned int count) override {
        bool res = real->QueryFunctions(name, function, count);
        if (res) {
            for (unsigned int i = 0; i < count; i++) {
                if (!name[i]) continue;
                Log("QF: %S -> %p\n", name[i], function[i]);
                if (wcsstr(name[i], L"TVPSetXP3ArchiveExtractionFilter")) {
                    Log("QF: Intercepted! real=%p\n", function[i]);
                    if (!g_TVPSetXP3ArchiveExtractionFilter)
                        g_TVPSetXP3ArchiveExtractionFilter = (tTVPSetXP3ArchiveExtractionFilter)function[i];
                    function[i] = (void*)FakeTVPSetXP3ArchiveExtractionFilter;
                }
            }
        }
        return res;
    }

    bool __cdecl QueryFunctionsByNarrowString(const char** name, void** function, unsigned int count) override {
        bool res = real->QueryFunctionsByNarrowString(name, function, count);
        if (res) {
            for (unsigned int i = 0; i < count; i++) {
                if (!name[i]) continue;
                Log("QFN: %s -> %p\n", name[i], function[i]);
                if (strstr(name[i], "TVPSetXP3ArchiveExtractionFilter")) {
                    Log("QFN: Intercepted! real=%p\n", function[i]);
                    if (!g_TVPSetXP3ArchiveExtractionFilter)
                        g_TVPSetXP3ArchiveExtractionFilter = (tTVPSetXP3ArchiveExtractionFilter)function[i];
                    function[i] = (void*)FakeTVPSetXP3ArchiveExtractionFilter;
                }
            }
        }
        return res;
    }
};

static ProxyFunctionExporter* g_Proxy = NULL;

// ============================================================
// KrkrSign Signature Bypass
// vtable[4] = GetSignatureVerificationResult (per KirikiriTools)
// ============================================================
static bool __cdecl FakeGetSignatureVerificationResult() {
    Log("KrkrSign: bypass!\n");
    return true;
}

static void PatchKrkrSign(HMODULE hDll) {
    if (!hDll) return;
    PIMAGE_DOS_HEADER dos = (PIMAGE_DOS_HEADER)hDll;
    if (dos->e_magic != IMAGE_DOS_SIGNATURE) return;
    PIMAGE_NT_HEADERS nt = (PIMAGE_NT_HEADERS)((BYTE*)hDll + dos->e_lfanew);
    BYTE* base = (BYTE*)hDll;
    DWORD imageSize = nt->OptionalHeader.SizeOfImage;

    // MSVC RTTI decorated name for KrkrSign::VerifierImpl
    const char* patterns[] = {
        ".?AVVerifierImpl@KrkrSign@@",
        "KrkrSign::VerifierImpl",
        NULL
    };

    BYTE* rttiName = NULL;
    for (int p = 0; patterns[p] && !rttiName; p++) {
        size_t len = strlen(patterns[p]);
        for (DWORD i = 0; i + len < imageSize; i++) {
            if (memcmp(base + i, patterns[p], len) == 0) {
                rttiName = base + i;
                Log("KrkrSign: Found RTTI '%s' at %p (offset 0x%X)\n", patterns[p], rttiName, i);
                break;
            }
        }
    }

    if (!rttiName) {
        Log("KrkrSign: RTTI not found in %p\n", hDll);
        return;
    }

    // TypeDescriptor is at rttiName - 8 (x86 MSVC: [vtable_ptr(4)][spare(4)][name...])
    DWORD* pTypeDesc = (DWORD*)(rttiName - 8);
    DWORD typeDescAddr = (DWORD)pTypeDesc;
    Log("KrkrSign: TypeDescriptor at %p (0x%08X)\n", pTypeDesc, typeDescAddr);

    // Find CompleteObjectLocator that has pTypeDescriptor == typeDescAddr
    // COL x86: [sig(4)][offset(4)][cdOffset(4)][pTypeDescriptor(4)][pClassHierarchyDescriptor(4)]
    void** pVTable = NULL;
    for (DWORD i = 0; i + 4 <= imageSize; i += 4) {
        if (*(DWORD*)(base + i) != typeDescAddr) continue;
        // Candidate: base+i might be COL.pTypeDescriptor (at offset 0x0C in COL)
        if (i < 12) continue;
        DWORD* pCOL = (DWORD*)(base + i - 12); // go back to start of COL
        DWORD colAddr = (DWORD)pCOL;
        // Find vtable where vtable[-1] == colAddr
        for (DWORD j = 4; j + 4 <= imageSize; j += 4) {
            DWORD* p = (DWORD*)(base + j);
            if (*(p - 1) == colAddr) {
                // Verify it looks like a vtable (all entries are code pointers)
                if (p[0] >= (DWORD)base && p[0] < (DWORD)base + imageSize) {
                    pVTable = (void**)p;
                    Log("KrkrSign: Found vtable at %p\n", pVTable);
                    break;
                }
            }
        }
        if (pVTable) break;
    }

    if (!pVTable) {
        Log("KrkrSign: vtable not found\n");
        return;
    }

    Log("KrkrSign: vtable[4]=%p -> patching with FakeGetSignatureVerificationResult\n", pVTable[4]);
    DWORD op;
    VirtualProtect(&pVTable[4], sizeof(void*), PAGE_READWRITE, &op);
    pVTable[4] = (void*)FakeGetSignatureVerificationResult;
    VirtualProtect(&pVTable[4], sizeof(void*), op, &op);
    Log("KrkrSign: Patched!\n");
}

// ============================================================
// PackinOne global patching
// After V2Link runs, PackinOne stores the exporter at:
//   [PackinOneBase + 0x945E0]
// We overwrite that global to point to our ProxyFunctionExporter.
// ============================================================
static void PatchPackinOneExporterGlobal(HMODULE hPackinOne) {
    if (!hPackinOne || !g_Proxy) return;
    
    // The global that holds the exporter pointer
    // RVA 0x945E0 confirmed by disassembly of sub_10055390
    const DWORD EXPORTER_GLOBAL_RVA = 0x945E0;
    
    iTVPFunctionExporter** pGlobal = (iTVPFunctionExporter**)((BYTE*)hPackinOne + EXPORTER_GLOBAL_RVA);
    
    Log("PatchPackinOne: Global at %p currently = %p\n", pGlobal, *pGlobal);
    
    if (*pGlobal && !g_Proxy->real) {
        g_Proxy->real = *pGlobal;
    }
    
    DWORD op;
    VirtualProtect(pGlobal, sizeof(void*), PAGE_READWRITE, &op);
    *pGlobal = g_Proxy;
    VirtualProtect(pGlobal, sizeof(void*), op, &op);
    
    Log("PatchPackinOne: Global patched -> %p (ProxyFunctionExporter)\n", *pGlobal);
}

// ============================================================
// V2Link hook
// ============================================================
typedef HRESULT(__stdcall *tV2Link)(iTVPFunctionExporter*);
static tV2Link   g_RealV2Link   = NULL;

static HRESULT __stdcall HookedV2Link(iTVPFunctionExporter* exporter) {
    Log("HookedV2Link: exporter=%p\n", exporter);
    
    // Create proxy wrapping the real exporter
    if (!g_Proxy) {
        g_Proxy = new ProxyFunctionExporter(exporter);
        Log("HookedV2Link: Created ProxyFunctionExporter %p\n", g_Proxy);
    }
    
    // Call the real V2Link with the ORIGINAL exporter
    // (PackinOne will store it in its global)
    HRESULT hr = g_RealV2Link(exporter);
    Log("HookedV2Link: g_RealV2Link returned 0x%08X\n", hr);
    
    // NOW patch PackinOne's internal global to use our proxy
    if (g_PackinOneMod) {
        PatchPackinOneExporterGlobal(g_PackinOneMod);
    }
    
    return hr;
}

// ============================================================
// GetProcAddress and LoadLibrary hooks
// ============================================================
typedef FARPROC(WINAPI *tGetProcAddress)(HMODULE, LPCSTR);
typedef HMODULE(WINAPI *tLoadLibraryA)(LPCSTR);
typedef HMODULE(WINAPI *tLoadLibraryW)(LPCWSTR);
typedef HMODULE(WINAPI *tLoadLibraryExA)(LPCSTR, HANDLE, DWORD);
typedef HMODULE(WINAPI *tLoadLibraryExW)(LPCWSTR, HANDLE, DWORD);

static tGetProcAddress g_RealGetProcAddress = NULL;
static tLoadLibraryA   g_RealLoadLibraryA   = NULL;
static tLoadLibraryW   g_RealLoadLibraryW   = NULL;
static tLoadLibraryExA g_RealLoadLibraryExA = NULL;
static tLoadLibraryExW g_RealLoadLibraryExW = NULL;

static void OnDllLoaded(HMODULE hDll) {
    if (!hDll) return;
    char name[MAX_PATH] = {};
    GetModuleFileNameA(hDll, name, MAX_PATH);
    for (int i = 0; name[i]; i++) name[i] = (char)tolower((unsigned char)name[i]);
    Log("DllLoaded: %s\n", name);
    if (strstr(name, "krkrsign")) {
        Log("OnDllLoaded: Found KrkrSign, patching!\n");
        PatchKrkrSign(hDll);
    }
}

FARPROC WINAPI HookedGetProcAddress(HMODULE hModule, LPCSTR lpProcName) {
    if (lpProcName && (DWORD_PTR)lpProcName > 0xFFFF) {
        if (strcmp(lpProcName, "V2Link") == 0) {
            char modName[MAX_PATH] = {};
            GetModuleFileNameA(hModule, modName, MAX_PATH);
            for (int i = 0; modName[i]; i++) modName[i] = (char)tolower((unsigned char)modName[i]);
            Log("GetProcAddress V2Link from: %s\n", modName);
            if (strstr(modName, "packinone")) {
                FARPROC real = g_RealGetProcAddress(hModule, lpProcName);
                g_RealV2Link = (tV2Link)real;
                g_PackinOneMod = hModule;
                Log("Intercepting PackinOne V2Link! real=%p, hMod=%p\n", real, hModule);
                return (FARPROC)HookedV2Link;
            }
        }
    }
    return g_RealGetProcAddress(hModule, lpProcName);
}

HMODULE WINAPI HookedLoadLibraryA(LPCSTR f)                      { HMODULE h = g_RealLoadLibraryA(f);           OnDllLoaded(h); return h; }
HMODULE WINAPI HookedLoadLibraryW(LPCWSTR f)                     { HMODULE h = g_RealLoadLibraryW(f);           OnDllLoaded(h); return h; }
HMODULE WINAPI HookedLoadLibraryExA(LPCSTR f, HANDLE h2, DWORD fl){ HMODULE h = g_RealLoadLibraryExA(f,h2,fl);  OnDllLoaded(h); return h; }
HMODULE WINAPI HookedLoadLibraryExW(LPCWSTR f, HANDLE h2, DWORD fl){ HMODULE h = g_RealLoadLibraryExW(f,h2,fl); OnDllLoaded(h); return h; }

// ============================================================
// IAT Patcher
// ============================================================
static void PatchIAT(HMODULE hExe, const char* dllName, const char* funcName, void* newFunc, void** oldFunc) {
    PIMAGE_DOS_HEADER dos = (PIMAGE_DOS_HEADER)hExe;
    PIMAGE_NT_HEADERS nt  = (PIMAGE_NT_HEADERS)((BYTE*)hExe + dos->e_lfanew);
    DWORD rva = nt->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT].VirtualAddress;
    if (!rva) return;
    PIMAGE_IMPORT_DESCRIPTOR imp = (PIMAGE_IMPORT_DESCRIPTOR)((BYTE*)hExe + rva);
    for (; imp->Name; imp++) {
        if (_stricmp((char*)((BYTE*)hExe + imp->Name), dllName) != 0) continue;
        PIMAGE_THUNK_DATA orig = (PIMAGE_THUNK_DATA)((BYTE*)hExe + imp->OriginalFirstThunk);
        PIMAGE_THUNK_DATA iat  = (PIMAGE_THUNK_DATA)((BYTE*)hExe + imp->FirstThunk);
        for (; orig->u1.AddressOfData; orig++, iat++) {
            if (orig->u1.Ordinal & IMAGE_ORDINAL_FLAG) continue;
            PIMAGE_IMPORT_BY_NAME ibn = (PIMAGE_IMPORT_BY_NAME)((BYTE*)hExe + orig->u1.AddressOfData);
            if (strcmp(ibn->Name, funcName) == 0) {
                if (oldFunc) *oldFunc = (void*)(DWORD_PTR)iat->u1.Function;
                DWORD op; VirtualProtect(&iat->u1.Function, 4, PAGE_READWRITE, &op);
                iat->u1.Function = (DWORD_PTR)newFunc;
                VirtualProtect(&iat->u1.Function, 4, op, &op);
                Log("PatchIAT: %s!%s -> %p\n", dllName, funcName, newFunc);
                return;
            }
        }
    }
}

void InstallHooks() {
    HMODULE hExe = GetModuleHandle(NULL);
    PatchIAT(hExe, "KERNEL32.dll", "GetProcAddress",  (void*)HookedGetProcAddress,  (void**)&g_RealGetProcAddress);
    PatchIAT(hExe, "KERNEL32.dll", "LoadLibraryA",    (void*)HookedLoadLibraryA,    (void**)&g_RealLoadLibraryA);
    PatchIAT(hExe, "KERNEL32.dll", "LoadLibraryW",    (void*)HookedLoadLibraryW,    (void**)&g_RealLoadLibraryW);
    PatchIAT(hExe, "KERNEL32.dll", "LoadLibraryExA",  (void*)HookedLoadLibraryExA,  (void**)&g_RealLoadLibraryExA);
    PatchIAT(hExe, "KERNEL32.dll", "LoadLibraryExW",  (void*)HookedLoadLibraryExW,  (void**)&g_RealLoadLibraryExW);
    if (!g_RealGetProcAddress) g_RealGetProcAddress = GetProcAddress;
    if (!g_RealLoadLibraryA)   g_RealLoadLibraryA   = LoadLibraryA;
    if (!g_RealLoadLibraryW)   g_RealLoadLibraryW   = LoadLibraryW;
    if (!g_RealLoadLibraryExA) g_RealLoadLibraryExA = LoadLibraryExA;
    if (!g_RealLoadLibraryExW) g_RealLoadLibraryExW = LoadLibraryExW;
}

// ============================================================
// DllMain
// ============================================================
BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved) {
    if (fdwReason == DLL_PROCESS_ATTACH) {
        DisableThreadLibraryCalls(hinstDLL);
        Log("version.dll loaded!\n");
        InstallHooks();
        HMODULE hSign = GetModuleHandleA("KrkrSign.dll");
        if (hSign) { Log("KrkrSign already loaded\n"); PatchKrkrSign(hSign); }
    }
    return TRUE;
}
