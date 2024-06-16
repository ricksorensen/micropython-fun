import gc
import st7789
import tft_config
import time
import random


tft = tft_config.config(0, verbose=True)


wid = tft.width()
ht = tft.height()


def dolines(n=1000):
    tft.fill(0)
    while n > 0:
        n = n - 1
        c = st7789.color565(
            random.getrandbits(8), random.getrandbits(8), random.getrandbits(8)
        )
        tft.line(
            random.randint(0, wid),
            random.randint(0, ht),
            random.randint(0, wid),
            random.randint(0, ht),
            c,
        )
        width = random.randint(0, wid // 2)
        height = random.randint(0, ht // 2)
        col = random.randint(0, wid - width)
        row = random.randint(0, ht - height)
        tft.fill_rect(
            col,
            row,
            width,
            height,
            st7789.color565(
                random.getrandbits(8), random.getrandbits(8), random.getrandbits(8)
            ),
        )


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
    print(f"boxlines,{mcu},st7789,{cfg},{td/niter/1000000},{ms-me}")
    return td


# dorun(5)/5000000 = 15.32231 s/iteration at 80 Mbit/s SPI
# mem after init, before run 195088
# mem after run 195088
# 15.32231
