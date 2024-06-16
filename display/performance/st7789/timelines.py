import gc
import st7789
import tft_config
import time

tft = tft_config.config(1, verbose=True)


colors = [
    st7789.BLACK,
    st7789.BLUE,
    st7789.RED,
    st7789.GREEN,
    st7789.CYAN,
    st7789.MAGENTA,
    st7789.YELLOW,
    st7789.WHITE,
]
ncolors = len(colors)
wid = tft.width()
ht = tft.height()

print(f"width:{wid}  height:{ht}")


def dolines():
    tft.fill(0)
    for i in range(wid):
        tft.line(0, i, ht - 1, wid - i, colors[i % ncolors])
        # tft.line(i, 0, wid - i, ht - 1, colors[i % ncolors])
    for i in range(ht):
        tft.line(i, 0, ht - i, wid - 1, colors[i % ncolors])
        # tft.line(0, i, wid - 1, ht - i, colors[i % ncolors])


def dorun(niter, mcu="", cfg=""):
    n = niter
    tft.init()
    gc.collect()
    ms = gc.mem_free()
    ts = time.ticks_us()
    while n > 0:
        dolines()
        n = n - 1
    td = time.ticks_diff(time.ticks_us(), ts)
    me = gc.mem_free()
    gc.collect()
    print(f"timelines,{mcu},st7789,{cfg},{td/niter/1000000},{ms-me}")
    return td


# dorun(5)/5000000 = 17.21323 s/iteration at 80 Mbit/s SPI
# mem after init, before run 195136
# mem after run 195136
# 17.21323
