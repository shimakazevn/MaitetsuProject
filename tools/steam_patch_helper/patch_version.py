with open(r'E:\MaitetsuProject\tools\steam_patch_helper\version_hijack.cpp', 'r', encoding='utf-8') as f:
    code = f.read()

log_code = '''
#include <stdio.h>
void Log(const char* fmt, ...) {
    FILE* f = fopen("E:\\\\MaitetsuProject\\\\version_hijack.log", "a");
    if (!f) return;
    va_list args;
    va_start(args, fmt);
    vfprintf(f, fmt, args);
    va_end(args);
    fclose(f);
}
'''
code = code.replace('#include "hashes.h"', log_code + '\n#include "hashes.h"')

# Add Log to HookedGetProcAddress
code = code.replace(
'''    if (lpProcName && (DWORD_PTR)lpProcName > 0xFFFF) {
        if (strcmp(lpProcName, "V2Link") == 0) {''',
'''    if (lpProcName && (DWORD_PTR)lpProcName > 0xFFFF) {
        if (strcmp(lpProcName, "V2Link") == 0) {
            Log("HookedGetProcAddress: V2Link requested for module.\\n");'''
)
code = code.replace(
'''            if (strstr(modName, "packinone")) {
                g_RealPackinOneV2Link = (tV2Link)g_RealGetProcAddress(hModule, lpProcName);''',
'''            if (strstr(modName, "packinone")) {
                Log("HookedGetProcAddress: Intercepted PackinOne V2Link!\\n");
                g_RealPackinOneV2Link = (tV2Link)g_RealGetProcAddress(hModule, lpProcName);'''
)
code = code.replace(
'''    if (fdwReason == DLL_PROCESS_ATTACH) {
        DisableThreadLibraryCalls(hinstDLL);
        InstallIATHook();
    }''',
'''    if (fdwReason == DLL_PROCESS_ATTACH) {
        Log("version.dll loaded! Installing IAT hook.\\n");
        DisableThreadLibraryCalls(hinstDLL);
        InstallIATHook();
    }'''
)
code = code.replace(
'''        if (exporter->QueryFunctionsByNames(names, funcs, 2)) {
            TVPSetXP3ArchiveExtractionFilter_func = (tTVPSetXP3ArchiveExtractionFilter)funcs[0];''',
'''        Log("HookedPackinOneV2Link: Querying functions...\\n");
        if (exporter->QueryFunctionsByNames(names, funcs, 2)) {
            Log("HookedPackinOneV2Link: Successfully queried TVPSetXP3ArchiveExtractionFilter.\\n");
            TVPSetXP3ArchiveExtractionFilter_func = (tTVPSetXP3ArchiveExtractionFilter)funcs[0];'''
)

code = code.replace(
'''    if (std::binary_search(std::begin(g_WhitelistHashes), std::end(g_WhitelistHashes), info->FileHash)) {
        return;
    }''',
'''    if (std::binary_search(std::begin(g_WhitelistHashes), std::end(g_WhitelistHashes), info->FileHash)) {
        Log("SmartSteamExtractionFilter: Bypassing file hash 0x%08X (size %u)\\n", info->FileHash, info->BufferSize);
        return;
    }
    //Log("SmartSteamExtractionFilter: Delegating file hash 0x%08X (size %u)\\n", info->FileHash, info->BufferSize);
'''
)


with open(r'E:\MaitetsuProject\tools\steam_patch_helper\version_hijack.cpp', 'w', encoding='utf-8') as f:
    f.write(code)
