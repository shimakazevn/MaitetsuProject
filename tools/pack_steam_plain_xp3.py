import os
import io
import struct
import zlib
import ctypes
from typing import List

# TVP constants
XP3_SIG = b"XP3\r\n \n\x1a\x8b\x67\x01"
TVP_XP3_FILE_PROTECTED = 0  # Standard unencrypted file
TVP_XP3_SEGM_ENCODE_RAW = 0
TVP_XP3_SEGM_ENCODE_ZLIB = 1

class Xp3Info_t(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("flags", ctypes.c_uint32),
        ("fsize", ctypes.c_int64),
        ("zsize", ctypes.c_int64),
        ("namelen", ctypes.c_uint16)
    ]

class Xp3Segm_t(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("flags", ctypes.c_uint32),
        ("offset", ctypes.c_uint64),
        ("fsize", ctypes.c_uint64),
        ("zsize", ctypes.c_uint64)
    ]

class Xp3Adlr_t(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("hash", ctypes.c_uint32)
    ]

class Xp3Entry:
    def __init__(self, name, size, hash_val, offset):
        self.name = name
        self.size = size
        self.hash = hash_val
        self.offset = offset

def update_adler32(data: bytes) -> int:
    return zlib.adler32(data) & 0xFFFFFFFF

def pack_steam_plain_xp3(indir, outpath):
    inpaths = []
    for root, dirs, files in os.walk(indir):
        rel_dir = os.path.relpath(root, indir)
        if rel_dir == "scn" or rel_dir.startswith("scn" + os.sep):
            continue
        for file in files:
            inpath = os.path.relpath(os.path.join(root, file), indir)
            inpath = inpath.replace("\\", "/").strip("/")
            inpaths.append(inpath)

    inpaths.sort()
    print(f"Packing {len(inpaths)} unencrypted files to {outpath}...")

    outio = io.BytesIO()
    
    # Write V2 Header
    outio.write(XP3_SIG)                          # 11 bytes
    outio.write(struct.pack("<q", 0x17))          # 8 bytes
    outio.write(struct.pack("<i", 1))             # 4 bytes
    outio.write(b"\x80")                          # 1 byte
    outio.write(struct.pack("<q", 0))             # 8 bytes
    
    index_pos_offset = outio.tell()
    outio.write(struct.pack("<q", 0))

    entries: List[Xp3Entry] = []
    for inpath in inpaths:
        full_path = os.path.join(indir, inpath)
        with open(full_path, "rb") as fp:
            data = fp.read()
            
        orig_size = len(data)
        adlr_hash = update_adler32(data)

        # UNENCRYPTED RAW DATA
        offset = outio.tell()
        outio.write(data)

        entry = Xp3Entry(
            name=inpath,
            size=orig_size,
            hash_val=adlr_hash,
            offset=offset
        )
        entries.append(entry)

    # Build Index Stream
    index_io = io.BytesIO()
    for entry in entries:
        info = Xp3Info_t()
        info.flags = 0  # NOT protected
        info.fsize = entry.size
        info.zsize = entry.size
        info.namelen = len(entry.name)
        
        name_bytes = entry.name.encode("utf-16le")
        info_data_bytes = bytes(info) + name_bytes
        info_chunk = b"info" + struct.pack("<q", len(info_data_bytes)) + info_data_bytes

        segm = Xp3Segm_t()
        segm.flags = TVP_XP3_SEGM_ENCODE_RAW
        segm.offset = entry.offset
        segm.fsize = entry.size
        segm.zsize = entry.size
        segm_chunk = b"segm" + struct.pack("<q", ctypes.sizeof(Xp3Segm_t)) + bytes(segm)

        adlr = Xp3Adlr_t()
        adlr.hash = entry.hash
        adlr_chunk = b"adlr" + struct.pack("<q", ctypes.sizeof(Xp3Adlr_t)) + bytes(adlr)

        sub_chunks_data = info_chunk + segm_chunk + adlr_chunk
        file_chunk = b"File" + struct.pack("<q", len(sub_chunks_data)) + sub_chunks_data
        index_io.write(file_chunk)

    raw_index = index_io.getvalue()
    comp_index = zlib.compress(raw_index, 9)
    index_offset = outio.tell()

    # Write compressed index
    outio.write(b"\x01")  # zlib compressed flag
    outio.write(struct.pack("<q", len(raw_index)))
    outio.write(struct.pack("<q", len(comp_index)))
    outio.write(comp_index)

    # Patch index offset
    outio.seek(index_pos_offset)
    outio.write(struct.pack("<q", index_offset))

    # Write output file
    with open(outpath, "wb") as fp:
        fp.write(outio.getvalue())

    print(f"[OK] Unencrypted XP3 created: {outpath} ({len(outio.getvalue()) / (1024*1024):.2f} MB)")

if __name__ == "__main__":
    staging = r"E:\MaitetsuProject\test_staging"
    out_xp3 = r"E:\SteamLibrary\steamapps\common\MaitetsuLastRun\patch.xp3"
    pack_steam_plain_xp3(staging, out_xp3)
