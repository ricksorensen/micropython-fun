2 hard I2C busses (0,1)

4 hard SPI busses (0,1,2,3)

cannot use 0 id for both I2C and SPI at the same time

SPI id 3 is used for QSPI flash drive

File system size in `mpconfigboard.mk` set to 128KB.

ROMFS size in `nrfrjs_romfs.ld` set to 64KB


_head_size     0x00027000
_blotloader_head_size   0x00001000
_bootloader_tail_size   0x0000c000
_flash_size    0x00100000
_fs_start      0x000d4000
_fs_end        0x000f4000
_fs_size       0x00020000
_app_start     0x00027000
_app_size      0x0009d000

_micropy_hw_romfs_part0_size        0x00010000
_micropy_hw_romfs_part0_start       0x000c4000

| Addr | code | size | note |
| --- | --- | --- | --- |
| `0c00000000` | head | `0x00027000` | bootloader|
| `0x00027000` |   app  | `0x0009d000`| size= flash_size - head_size - part0_size - fs_size - bootloader_tail-size<br> abc |
| `0x000c4000` | romfs_part0 | `0x00010000` |
| `0x000d4000` |   fs | `0x00020000` |
| `0x000f4000` |  tail | `0x0000c000` |bootloader 
