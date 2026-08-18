import os
import io
import sys
import zlib
import struct
import ctypes
from typing import List

# Add current folder to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from maitetsu_crypt import MaitetsuCxEncryption

# TVP constants
XP3_SIG = b"XP3\r\n \n\x1a\x8b\x67\x01"
TVP_XP3_FILE_PROTECTED = 1 << 31
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
    def __init__(self, name, size, hash_val, is_encrypted, offset):
        self.name = name
        self.size = size
        self.hash = hash_val
        self.is_encrypted = is_encrypted
        self.offset = offset

def update_adler32(data: bytes) -> int:
    return zlib.adler32(data) & 0xFFFFFFFF

def pack_maitetsu_xp3(indir, outpath, scheme_path=None):
    print("=" * 60)
    print(f"Packing (Deduplicated & 100% Compatible) {indir} → {outpath}")
    print("=" * 60)

    dec = MaitetsuCxEncryption(scheme_path)

    # Find all files, skipping duplicate scn/ subfolder if present
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
    print(f"Found {len(inpaths)} files to pack.")

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
    for i, inpath in enumerate(inpaths):
        full_path = os.path.join(indir, inpath)
        with open(full_path, "rb") as fp:
            data = fp.read()
            
        orig_size = len(data)
        adlr_hash = update_adler32(data)

        # Encrypt contents with CxEncryption (TVP_XP3_SEGM_ENCODE_RAW)
        mutable_data = bytearray(data)
        dec.encrypt_buffer(adlr_hash, 0, mutable_data, 0, len(mutable_data))
        data = bytes(mutable_data)

        offset = outio.tell()
        outio.write(data)

        entry = Xp3Entry(
            name=inpath,
            size=orig_size,
            hash_val=adlr_hash,
            is_encrypted=True,
            offset=offset
        )
        entries.append(entry)

    # Build Index Stream
    index_io = io.BytesIO()
    for entry in entries:
        info = Xp3Info_t()
        info.flags = TVP_XP3_FILE_PROTECTED
        info.fsize = entry.size
        info.zsize = entry.size
        info.namelen = len(entry.name)
        
        name_bytes = entry.name.encode("utf-16le")
        info_data_bytes = bytes(info) + name_bytes
        info_chunk = b"info" + struct.pack("<q", len(info_data_bytes)) + info_data_bytes

        segm = Xp3Segm_t()
        segm.flags = TVP_XP3_SEGM_ENCODE_RAW # RAW encoding for Maitetsu CxEncryption compatibility
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

    # Write compressed index
    index_pos = outio.tell()
    outio.getbuffer()[index_pos_offset : index_pos_offset + 8] = struct.pack("<q", index_pos)

    unpacked_index_size = index_io.tell()
    compressed_index = zlib.compress(index_io.getvalue(), level=9)
    compressed_index_size = len(compressed_index)

    outio.write(b"\x01")
    outio.write(struct.pack("<Q", compressed_index_size))
    outio.write(struct.pack("<Q", unpacked_index_size))
    outio.write(compressed_index)

    with open(outpath, "wb") as fp:
        fp.write(outio.getvalue())

    print(f"\n[OK] Compatible XP3 created: {outpath} ({os.path.getsize(outpath) / (1024*1024):.2f} MB)")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("indir", help="Directory to pack")
    parser.add_argument("outpath", help="Path to output .xp3 file")
    args = parser.parse_args()
    pack_maitetsu_xp3(args.indir, args.outpath)
