"""Builds "TSQ Free Warp": fast travel without the Large Zonai Charge that The Second Quest asks for every warp.

usage: python build.py --romfs <game romfs folder> --out <output mod folder>

The Second Quest replaces the game's warp event (Event/EventFlow/DmF_SY_WarpIn.110.bfevfl.zs) with one that takes a
Large Zonai Charge before each warp and refuses it without one. This mod is that file as the game ships it, taken from
your own RomFS, so it holds nothing of the game or the mod: load it with a higher priority than The Second Quest and the
warp is free again. Everything else of The Second Quest stays as it is.

--romfs is the game's RomFS (version 1.4.3): the folder that holds Event/, Pack/ and the rest. A TotK PC Recomp
install's romfs folder (romfs.bin + index.json) works too. Standard library only.
"""
import argparse
import hashlib
import json
from pathlib import Path

FILE = 'Event/EventFlow/DmF_SY_WarpIn.110.bfevfl.zs'


def read(romfs, path):
    root = Path(romfs)
    if (root / 'index.json').exists() and (root / 'romfs.bin').exists():   # TotK PC Recomp install
        f = {e['path']: e for e in json.load(open(root / 'index.json', encoding='utf-8'))['files']}[path]
        with open(root / 'romfs.bin', 'rb') as fh:
            fh.seek(f['offset'])
            return fh.read(f['size'])
    return (root / path).read_bytes()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--romfs', required=True, help="the game's RomFS folder (1.4.3)")
    ap.add_argument('--out', required=True, help='output mod folder, e.g. <mods>/TSQ Free Warp')
    a = ap.parse_args()
    data = read(a.romfs, FILE)
    dst = Path(a.out) / 'romfs' / FILE
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(data)
    print(f'{dst}: {len(data)} bytes, sha256 {hashlib.sha256(data).hexdigest()[:16]}')


if __name__ == '__main__':
    main()
