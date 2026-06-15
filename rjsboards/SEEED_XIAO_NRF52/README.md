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

| baseaddr    | peripherals                          | ID | 
| --- | --- | --- |
| 0x40002000  | UARTE0                               |  2 | 
| 0x40003000  | SPIM0, SPIS0, TWI0, TWIM0, TWIS0     |  3 | 
| 0x40004000  | SPIM1, SPIS1, TWI1, TWIM1, TWIS1     |  4 | 
| 0x40023000  | SPIM2, SPIS2                         | 35 | 
| 0x4002F000  | SPIM3                                | 47 | 

1.28:
   TWI, TWI0, TWI1  enabled, TW*TWIM not enabled\
   SPIM, SPIM0, SPIM1, SPIM2, SPIM3 enabled
   PRS_BOX_0,1,2 not enabled.  Only enabled if both TWI and TWM enabled, so PRS_ENABLE is 0
   i2c(0) -> NRFX_TWI_INSTANCE(0)
   i2c(1) -> NRFX_TWI_INSTANCE(1)
   spi(0) -> NRFX_SPI_INSTANCE(0)  <- SPIM
   spi(1) -> NRFX_SPI_INSTANCE(1)  <- SPIM
   spi(2) -> NRFX_SPI_INSTANCE(2)  <- SPIM
   spi(3) -> NRFX_SPI_INSTANCE(3)  <- SPIM
   
1.29. preview 20260527
gc_free: 182736
gc_free: 183648
stack: 508 out of 7792
GC: total: 187584, used: 4000, free: 183584
 No. of 1-blocks: 53, 2-blocks: 16, max blk sz: 46, max free sz: 11092
--- Sys Info ---
  platform:        nrf52
  version:         3.4.0; MicroPython a9fc9e4458 on 2026-05-27
  implementation:  (name='micropython', version=(1, 29, 0, 'preview'), _machine='XIAO nRF52840 Sense with NRF52840', _mpy=7942, _build='SEEED_XIAO_NRF52')
  build:           MicroPython-1.29.0-preview-arm--with-newlib4.4.0
    mpy version: 6
    mpy sub-version: 3
    mpy flags: -march=armv7emsp
  path:            ['', '.frozen', '/flash', '/flash/lib']
  unique_id:       b''
--- Modules ---
__main__          binascii          hashlib           random
_asyncio          ble               heapq             re
_boot             board             io                select
array             builtins          json              struct
asyncio/__init__  cmath             machine           sys
asyncio/core      collections       math              time
asyncio/event     deflate           micropython       uasyncio
asyncio/funcs     errno             nrf               ubluepy
asyncio/lock      framebuf          os                uctypes
asyncio/stream    gc                platform          vfs
Plus any modules on the filesystem
    dir(machine)
['__class__', '__name__', 'ADC', 'DEBUG_IF_RESET', 'HARD_RESET', 'I2C', 'LOCKUP_RESET', 'LPCOMP_RESET', 'NFC_RESET', 'PWM', 'PWRON_RESET', 'Pin', 'RTCounter', 'SOFT_RESET', 'SPI', 'Signal', 'SoftI2C', 'Temp', 'Timer', 'UART', 'WDT_RESET', '__dict__', 'bootloader', 'deepsleep', 'disable_irq', 'enable_irq', 'freq', 'idle', 'info', 'lightsleep', 'mem16', 'mem32', 'mem8', 'reset', 'reset_cause', 'sleep', 'soft_reset', 'unique_id']
    dir(mcu)
['__class__', '__name__', 'Flash', '__dict__', 'dcdc', 'unused_flash_length', 'unused_flash_start']

--- /flash FileSyst: Size=262144   Free=253952   Type: vfs (default)
gc_free: 182224
gc_free: 183568


zephyr 20260526
$ mpremote dumpinfo
gc_free: 90848
gc_free: 91792
stack: 392 out of 7680
GC: total: 96000, used: 4272, free: 91728
 No. of 1-blocks: 57, 2-blocks: 17, max blk sz: 48, max free sz: 5340
--- Sys Info ---
  platform:        zephyr
  version:         3.4.0; MicroPython v1.29.0-preview.288.gdd23554591.dirty on 2026-05-26
  implementation:  (name='micropython', version=(1, 29, 0, 'preview'), _machine='zephyr-xiao_ble with nrf52840', _mpy=774, _build='ZEPHYR_XIAO_BLE', _thread='GIL')
  build:           MicroPython-1.29.0-preview-arm--with-newlib4.3.0
    mpy version: 6
    mpy sub-version: 3
    mpy flags:
  path:            ['', '.frozen', '/flash/lib']
  unique_id:      Not Available
--- Modules ---
__main__          aiorepl           errno             re
_asyncio          array             framebuf          select
_boot             asyncio/__init__  gc                struct
_thread           asyncio/core      hashlib           sys
aioble/__init__   asyncio/event     heapq             time
aioble/central    asyncio/funcs     io                uasyncio
aioble/client     asyncio/lock      json              uctypes
aioble/core       asyncio/stream    machine           upysh
aioble/device     binascii          math              vfs
aioble/l2cap      bluetooth         micropython       zephyr
aioble/peripheral builtins          os                zsensor
aioble/security   collections       platform
aioble/server     deflate           random
Plus any modules on the filesystem
    dir(machine)
['__class__', '__name__', 'ADC', 'I2C', 'PWM', 'Pin', 'SPI', 'Signal', 'SoftI2C', 'SoftSPI', 'Timer', 'UART', 'WDT', '__dict__', 'idle', 'mem16', 'mem32', 'mem8', 'reset', 'reset_cause', 'soft_reset']
    dir(mcu)
['__class__', '__name__', 'FlashArea', '__dict__', 'current_tid', 'is_preempt_thread', 'thread_analyze']

--- /flash FileSyst: Size=2097152   Free=2023424   Type: vfs (default)
gc_free: 90080
gc_free: 91616

read die temp:

`dietemp.py`:
```
from micropython import const
import machine
import time
TBASE = const(0x4000c000)
#TSTART = const(TBASE)
#TSTOP = const(TBASE+4)
TRDY = const(TBASE+0x100)
TTEMP = const(TBASE+0x508)

@micropython.native
def getDieTemp()->float:
    """ get die temperature in celsius """
    machine.mem32[TBASE] = 1        # initiate temp read/conversion
    while not machine.mem32[TRDY]:   # wait for conversion
        time.sleep(0)
    return machine.mem32[TTEMP]/4
```
