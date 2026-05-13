def setup_fs():
    import gc
    import vfs
    import sys
    import nrf
    import os

    newfs = False
    fs_type = getattr(
        vfs, "VfsLfs2", getattr(vfs, "VfsLfs1", getattr(vfs, "VfsFat", None))
    )
    try:
        bdev = nrf.Flash()
        vfs.mount(bdev, "/flash")
    except:
        newfs = True
        if fs_type is not None:
            try:
                fs_type.mkfs(bdev)
                vfs.mount(bdev, "/flash")
            except:
                return

    os.chdir("/flash")
    sys.path.append("/flash")
    sys.path.append("/flash/lib")

    gc.collect()
    return newfs


def data_fs():
    import os
    import gc
    from flashbdev import FlashBdev
    from spiflash import SPIflash
    from machine import SPI, Pin

    # wp = Pin("QSPI_D2", Pin.OUT, value=1)
    # hold = Pin("QSPI_D3", Pin.OUT, value=1)
    cs = Pin("QSPI_CS", Pin.OUT, value=1)
    spi = SPI(
        3,
        sck=Pin("QSPI_SCK"),
        mosi=Pin("QSPI_D0"),
        miso=Pin("QSPI_D1"),
        baudrate=32_000_000,
    )
    newfs = False
    flash = FlashBdev(SPIflash(spi, cs))
    try:
        vfs = os.VfsLfs2(flash, progsize=256)
    except OSError as e:
        print("data directory Mount failed with error", e)
        print("Recreate the file system")  # Previous content is lost!
        os.VfsLfs2.mkfs(flash, progsize=256)
        newfs = True
        vfs = os.VfsLfs2(flash, progsize=256)
    os.mount(vfs, "/data")
    gc.collect()
    return newfs


ffs = setup_fs()
dfs = data_fs()
del setup_fs
del data_fs
