import gc
from color_setup import ssd
from gui.core.colors import BLACK, BLUE, RED, GREEN, CYAN, MAGENTA, YELLOW, WHITE
from gui.core.nanogui import refresh
import time

refresh(ssd, True)
colors = [
    BLACK,
    BLUE,
    RED,
    GREEN,
    CYAN,
    MAGENTA,
    YELLOW,
    BLACK,
]
ncolors = len(colors)
wid = ssd.width
ht = ssd.height


def dolines():
    ssd.fill(0)
    for i in range(wid):
        # ssd.line(0, i, ht - 1, wid - i, colors[i % ncolors])
        ssd.line(i, 0, wid - i, ht - 1, colors[i % ncolors])
    for i in range(ht):
        # ssd.line(i, 0, ht - i, wid - 1, colors[i % ncolors])
        ssd.line(0, i, wid - 1, ht - i, colors[i % ncolors])
    ssd.show()


def dorun(niter, mcu="", cfg=""):
    n = niter
    gc.collect()
    ms = gc.mem_free()
    ts = time.ticks_us()
    while n > 0:
        dolines()
        n = n - 1
    td = time.ticks_diff(time.ticks_us(), ts)
    me = gc.mem_free()
    gc.collect()
    print(f"timelines,{mcu},nano,{cfg},{td/niter/1000000},{ms-me}")
    return td


# no viper
# dorun(5)/5000000 = 3.108595 s/iteration at 62.5 Mbit/s SPI
# mem after init, before run 142688
# mem after run 135552
# 3.108595

# viper
# mem after init, before run 142640
# mem after run 104080
# 0.1444596
