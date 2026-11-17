"""Remove Extraction-only delivery volumes from a cooked native non-Extraction variant.

Requires scctpkg on PYTHONPATH. Leaves export indices and every other object body intact.
"""
from pathlib import Path
import argparse
import hashlib
import struct
import uuid
import zlib

from scctpkg.package import Package, Reader, _encode_compact


def actors(package, level):
    reader = package.export_reader(level)
    assert reader.name() == "None"
    count, capacity = reader.i32(), reader.i32()
    assert 0 < count <= capacity <= 100000
    start = reader.p
    refs = [reader.compact() for _ in range(count)]
    return refs, start, reader.p


def patch(source, output, mode):
    package = Package.load(source)
    level, = [entry for entry in package.exports if entry.class_name == "Level"]
    refs, start, end = actors(package, level)
    zones = {ref for ref in refs if ref > 0 and package.exports[ref - 1].class_name == "SFlagDropZone"}
    if mode == "Extraction" or not zones:
        return len(zones)
    assert mode in ("Neutralization", "Sabotage")
    assert not any(ref > 0 and package.exports[ref - 1].class_name == "SFlag" for ref in refs)
    old = package.data
    body = old[level.offset:level.offset + level.size]
    expected = [0 if ref in zones else ref for ref in refs]
    replacement = body[:start] + b"".join(map(_encode_compact, expected)) + body[end:]
    data = bytearray(old)
    data[level.offset:level.offset + level.size] = replacement.ljust(level.size, b"\0")
    # Keep subsequent offsets fixed. Shrink only the serialized Level export size.
    table = Reader(old, struct.unpack_from("<i", old, 24)[0], package)
    for entry in package.exports:
        table.compact()
        table.compact()
        table.i32()
        table.name()
        table.u32()
        pos = table.p
        assert table.compact() == entry.size
        if entry == level:
            size = _encode_compact(len(replacement))
            assert len(size) == table.p - pos
            data[pos:table.p] = size
            break
        if entry.size:
            table.compact()
    data[36:52] = uuid.uuid5(uuid.NAMESPACE_URL, "SCCT-Maps/dropoffs/" + hashlib.sha256(old).hexdigest()).bytes
    raw = source.read_bytes()
    chunk_size = struct.unpack_from("<I", raw)[0] if package.compressed else 0
    packed = bytearray()
    if chunk_size:
        for offset in range(0, len(data), chunk_size):
            chunk = data[offset:offset + chunk_size]
            compressed = zlib.compress(chunk, 9)
            packed.extend(struct.pack("<II", len(chunk), len(compressed)) + compressed)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(packed or data)
    verified = Package.load(output)
    assert actors(verified, verified.exports[level.index])[0] == expected
    for entry, revised in zip(package.exports, verified.exports, strict=True):
        actual = verified.data[revised.offset:revised.offset + revised.size]
        assert actual == (replacement if entry == level else old[entry.offset:entry.offset + entry.size])
    return len(zones)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("mode", choices=["Neutralization", "Sabotage", "Extraction"])
    args = parser.parse_args()
    print(patch(args.source, args.output, args.mode))
