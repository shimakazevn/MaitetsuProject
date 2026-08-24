#pragma once
#include <mutex>
#include <thread>
#include <mutex>

class Patcher
{
    friend CompilerHelper;

public:
    static bool                 PatchSignatureCheck                     (HMODULE hModule);

    static void                 PatchXP3StreamCreation                  ();
    static void                 PatchAutoPathExports                    ();
    static void                 PatchStorageMediaRegistration           ();

private:
    static void __stdcall       CustomTVPAddAutoPath                    (const ttstr& url);
    static void __stdcall       CustomTVPRemoveAutoPath                 (const ttstr& url);

    static void __stdcall       CustomTVPRegisterStorageMedia           (iTVPStorageMedia* pMedia);
    static void __stdcall       CustomTVPUnregisterStorageMedia         (iTVPStorageMedia* pMedia);
    static tTJSBinaryStream*    CustomStorageMediaOpen                  (iTVPStorageMedia* pMedia, const ttstr& name, tjs_uint32 flags);
    static void                 WriteStreamToFile                       (tTJSBinaryStream* pStream, const std::wstring& filePath);

    static bool                 CustomGetSignatureVerificationResult    ();

    template<CompilerType TCompilerType>
    class CustomCreateStreamByIndex
    {
    public:
        static void CaptureStream(uint32_t hash, const std::wstring& name, tTJSBinaryStream* pStream)
        {
            static std::mutex mtx;
            if (!pStream || hash == 0) return;
            std::lock_guard<std::mutex> lock(mtx);
            static std::set<uint32_t> dumped;
            if (!dumped.insert(hash).second) return;
            try
            {
                if (pStream->GetSize() > 64ull * 1024 * 1024) return;
                wchar_t path[640];
                swprintf(path, 640, L"E:\\MaitetsuProject\\steam_capture\\%08X.bin", hash);
                WriteStreamToFile(pStream, path);
                Debugger::Log(L"Captured %08X (%s)", hash, name.c_str());
            }
            catch (...) { return; }
            pStream->Seek(0, SEEK_SET);
        }

        static tTJSBinaryStream* MakeRawStream(tTVPXP3Archive<TCompilerType>* pArchive, tjs_uint idx)
        {
            int itemSize = ((BYTE*)pArchive->ItemVector.end() - (BYTE*)pArchive->ItemVector.begin()) / pArchive->Count;
            auto* pItem = (typename tTVPXP3Archive<TCompilerType>::tArchiveItem*)((BYTE*)pArchive->ItemVector.begin() + idx * itemSize);
            tTVPXP3ArchiveSegment* pSegment = pItem->Segments.begin();
            auto* pStream = new CustomTVPXP3ArchiveStream(pArchive->Name, pSegment->Start, pSegment->OrgSize, pSegment->ArcSize, pSegment->IsCompressed);
            tTJSBinaryStream::ApplyWrappedVTable(pStream);
            return pStream;
        }

        static std::vector<tTVPXP3Archive<TCompilerType>*>& ArchiveList()
        {
            static std::vector<tTVPXP3Archive<TCompilerType>*> list;
            return list;
        }

        static uint32_t HashOf(tTVPXP3Archive<TCompilerType>* pArchive, tjs_uint idx)
        {
            int itemSize = ((BYTE*)pArchive->ItemVector.end() - (BYTE*)pArchive->ItemVector.begin()) / pArchive->Count;
            auto* pItem = (typename tTVPXP3Archive<TCompilerType>::tArchiveItem*)((BYTE*)pArchive->ItemVector.begin() + idx * itemSize);
            return pItem->FileHash;
        }

        static std::wstring NameOf(tTVPXP3Archive<TCompilerType>* pArchive, tjs_uint idx)
        {
            int itemSize = ((BYTE*)pArchive->ItemVector.end() - (BYTE*)pArchive->ItemVector.begin()) / pArchive->Count;
            auto* pItem = (typename tTVPXP3Archive<TCompilerType>::tArchiveItem*)((BYTE*)pArchive->ItemVector.begin() + idx * itemSize);
            return std::wstring(pItem->Name.c_str());
        }

        static void DumpWholeArchive(tTVPXP3Archive<TCompilerType>* pArchive)
        {
            if (!pArchive) return;
            Debugger::Log(L"[CAPTURE] dumping whole archive %s (%d entries)", pArchive->Name.c_str(), (int)pArchive->Count);
            for (tjs_uint i = 0; i < pArchive->Count; i++)
            {
                try
                {
                    auto* s = CompilerHelper::CallInstanceMethod<tTJSBinaryStream*, &OriginalCreateStreamByIndex, tTVPXP3Archive<TCompilerType>*, tjs_uint>(pArchive, i);
                    if (s) { CaptureStream(HashOf(pArchive, i), NameOf(pArchive, i), s); delete s; }
                }
                catch (...) {}
            }
            Debugger::Log(L"[CAPTURE] archive dump complete %s", pArchive->Name.c_str());
        }

        static void StartDumperThread()
        {
            static std::once_flag once;
            std::call_once(once, []()
            {
                std::thread([]()
                {
                    Sleep(60000);
                    auto& list = ArchiveList();
                    for (auto* pa : list)
                    {
                        DumpWholeArchive(pa);
                        Sleep(200);
                    }
                    Debugger::Log(L"[CAPTURE] ALL DONE");
                }).detach();
            });
        }

        static tTJSBinaryStream* Call(tTVPXP3Archive<TCompilerType>* pArchive, tjs_uint idx)
        {
            int itemSize = ((BYTE*)pArchive->ItemVector.end() - (BYTE*)pArchive->ItemVector.begin()) / pArchive->Count;
            auto* pItem = (typename tTVPXP3Archive<TCompilerType>::tArchiveItem*)((BYTE*)pArchive->ItemVector.begin() + idx * itemSize);
            bool isProbe = wcsstr(pArchive->Name.c_str(), L"patch.xp3") != nullptr;
            if (isProbe)
            {
                auto& list = ArchiveList();
                if (std::find(list.begin(), list.end(), pArchive) == list.end())
                    list.push_back(pArchive);
                StartDumperThread();
            }

            // probe archive: capture engine output (ciphertext), serve raw plaintext to game
            if (isProbe && pItem->FileHash != 0)
            {
                try
                {
                    auto* pTmp = CompilerHelper::CallInstanceMethod<tTJSBinaryStream*, &OriginalCreateStreamByIndex, tTVPXP3Archive<TCompilerType>*, tjs_uint>(pArchive, idx);
                    if (pTmp) { CaptureStream(pItem->FileHash, pItem->Name.c_str(), pTmp); delete pTmp; }
                }
                catch (...) {}
                return MakeRawStream(pArchive, idx);
            }

            if (pItem->FileHash != 0 || !pArchive->Name.StartsWith(L"file://"))
            {
                auto* pResult = CompilerHelper::CallInstanceMethod<tTJSBinaryStream*, &OriginalCreateStreamByIndex, tTVPXP3Archive<TCompilerType>*, tjs_uint>(pArchive, idx);
                CaptureStream(pItem->FileHash, pItem->Name.c_str(), pResult);
                return pResult;
            }
                
            Debugger::Log(L"Creating unencrypted XP3 stream for %s", pItem->Name.c_str());
            tTVPXP3ArchiveSegment* pSegment = pItem->Segments.begin();
            auto* pStream = new CustomTVPXP3ArchiveStream(pArchive->Name, pSegment->Start, pSegment->OrgSize, pSegment->ArcSize, pSegment->IsCompressed);
            tTJSBinaryStream::ApplyWrappedVTable(pStream);
            return pStream;
        }
    };

    static inline void* OriginalCreateStreamByIndex{};

    static inline void (__stdcall* OriginalTVPAddAutoPath)(const ttstr& path){};
    static inline void (__stdcall* OriginalTVPRemoveAutoPath)(const ttstr& path){};
    static inline void (__stdcall* OriginalTVPRegisterStorageMedia)(iTVPStorageMedia* pMedia){};
    static inline void (__stdcall* OriginalTVPUnregisterStorageMedia)(iTVPStorageMedia* pMedia){};
    static inline std::map<iTVPStorageMedia*, tTJSBinaryStream* (*)(iTVPStorageMedia* pMedia, const ttstr& name, tjs_uint32 flags)> OriginalStorageMediaOpen{};
};
