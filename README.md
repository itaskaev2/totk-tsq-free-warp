# TSQ Free Warp

A tiny add-on for **The Second Quest**, a mod for *The Legend of Zelda: Tears of the Kingdom* (version 1.4.3). It makes fast travel free again.

The Second Quest takes one **Large Zonai Charge** for every warp, and refuses the warp when you have none. This add-on puts back the game's own warp event, so warps cost nothing. Everything else of The Second Quest stays as it is.

## What it changes

One file: `Event/EventFlow/DmF_SY_WarpIn.110.bfevfl.zs`, the warp event. The Second Quest ships its own version of it. The add-on uses the original one from the game.

The repository holds no game or mod files. `build.py` copies that one file out of **your own** game dump.

## Build

You need Python 3 (standard library only) and your game's RomFS, version 1.4.3.

```
python build.py --romfs "<your TotK 1.4.3 romfs>" --out "TSQ Free Warp"
```

- `--romfs` is the dumped RomFS folder, the one that holds `Event/`, `Pack/` and the rest.
- A [TotK PC Recomp](https://github.com/valentderah/totk-pc-recomp) install's `romfs` folder (`romfs.bin` + `index.json`) works too.

The output folder is a ready mod: `TSQ Free Warp/romfs/Event/EventFlow/DmF_SY_WarpIn.110.bfevfl.zs`.

## Install

Load it **with a higher priority than The Second Quest**, so its file wins.

- **TotK PC Recomp:** put the folder into `mods/` and list it first:
  ```
  [mods]
  mods_order = TSQ Free Warp|The Second Quest
  ```
  (other mods can follow).
- **Emulators:** add it as a mod and place it above The Second Quest in the load order.

## Notes

- Tested on TotK PC Recomp 0.3.13 with The Second Quest for 1.4.3: the mod is served and the warp event loads. A full warp in game was not tested.
- Remove the add-on to get The Second Quest's paid warps back.
- *The Legend of Zelda: Tears of the Kingdom* belongs to Nintendo. The Second Quest belongs to its authors. This is an unofficial fan add-on.

Licence: MIT (the script).
