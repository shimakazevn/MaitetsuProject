#include <windows.h>
#include <stdint.h>
#include <stdio.h>
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

class iTVPFunctionExporter {
public:
    virtual bool __stdcall QueryFunctionsByNames(const char **names, void **functions, unsigned int count) = 0;
    virtual bool __stdcall QueryFunctionsByUncompressedIndices(const unsigned int *indices, void **functions, unsigned int count) = 0;
};

static tTVPSetXP3ArchiveExtractionFilter TVPSetXP3ArchiveExtractionFilter_func = NULL;
static tTVPXP3ArchiveExtractionFilter g_OriginalFilter = NULL;
static FILE* g_LogFile = NULL;

void LogMessage(const char* fmt, ...) {
    if (!g_LogFile) {
        g_LogFile = fopen("E:\\MaitetsuProject\\maitetsu_filter_log.txt", "w");
    }
    if (g_LogFile) {
        va_list args;
        va_start(args, fmt);
        vfprintf(g_LogFile, fmt, args);
        va_end(args);
        fflush(g_LogFile);
    }
    
    char buf[256];
    va_list args2;
    va_start(args2, fmt);
    vsnprintf(buf, sizeof(buf), fmt, args2);
    va_end(args2);
    OutputDebugStringA(buf);
}

void __cdecl SmartSteamExtractionFilter(tTVPXP3ExtractionFilterInfo *info) {
    if (!info || !info->Buffer || info->BufferSize == 0) return;

    LogMessage("Filter called for Hash=0x%08x, Size=%u\n", info->FileHash, info->BufferSize);

    // Call original filter unconditionally for testing, but log it
    if (g_OriginalFilter) {
        g_OriginalFilter(info);
    }
}

extern "C" __declspec(dllexport) HRESULT __stdcall V2Link(iTVPFunctionExporter *exporter) {
    if (!exporter) return S_OK;

    LogMessage("V2Link called!\n");

    const char *names[] = {
        "void ::TVPSetXP3ArchiveExtractionFilter(tTVPXP3ArchiveExtractionFilter)",
        "tTVPXP3ArchiveExtractionFilter ::TVPGetXP3ArchiveExtractionFilter()"
    };
    void *funcs[2] = { NULL, NULL };

    if (exporter->QueryFunctionsByNames(names, funcs, 2)) {
        TVPSetXP3ArchiveExtractionFilter_func = (tTVPSetXP3ArchiveExtractionFilter)funcs[0];
        typedef tTVPXP3ArchiveExtractionFilter (__cdecl *tTVPGetXP3ArchiveExtractionFilter)();
        tTVPGetXP3ArchiveExtractionFilter getFilter = (tTVPGetXP3ArchiveExtractionFilter)funcs[1];
        if (getFilter) {
            g_OriginalFilter = getFilter();
            LogMessage("Got OriginalFilter = %p\n", g_OriginalFilter);
        }
        if (TVPSetXP3ArchiveExtractionFilter_func) {
            TVPSetXP3ArchiveExtractionFilter_func(SmartSteamExtractionFilter);
            LogMessage("Hooked SmartSteamExtractionFilter!\n");
        }
    }
    return S_OK;
}

extern "C" __declspec(dllexport) HRESULT __stdcall V2Unlink() {
    if (TVPSetXP3ArchiveExtractionFilter_func && g_OriginalFilter) {
        TVPSetXP3ArchiveExtractionFilter_func(g_OriginalFilter);
    }
    if (g_LogFile) {
        fclose(g_LogFile);
        g_LogFile = NULL;
    }
    return S_OK;
}

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved) {
    return TRUE;
}
