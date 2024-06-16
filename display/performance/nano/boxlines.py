import gc
from color_setup import ssd, SSD
from gui.core.colors import BLACK, BLUE, RED, GREEN, CYAN, MAGENTA, YELLOW, WHITE
from gui.core.nanogui import refresh
import time
import random

refresh(ssd, True)

wid = ssd.width
ht = ssd.height


def dolines(n=1000):
    ssd.fill(0)
    while n > 0:
        n = n - 1
        c = SSD.rgb(random.getrandbits(8), random.getrandbits(8), random.getrandbits(8))
        ssd.line(
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
        ssd.fill_rect(
            col,
            row,
            width,
            height,
            SSD.rgb(
                random.getrandbits(8), random.getrandbits(8), random.getrandbits(8)
            ),
        )
    ssd.show()


def dorun(niter, mcu="", cfg=""):
    n = niter
    gc.collect()
    ms = gc.mem_free()
    ts = time.ticks_ms()
    while n > 0:
        dolines()
        n = n - 1
    td = time.ticks_diff(time.ticks_ms(), ts)
    me = gc.mem_free()
    gc.collect()
    print(f"boxlines,{mcu},nano,{cfg},{td/niter/1000},{ms-me}")
    return td


# no viper
# dorun(5)/5000000 = 67.16926  s/iteration at 62.5 Mbit/s SPI with show on each draw
#
#
#

# dorun(5)/5000000 = 3.240551 s/iteration at 62.5 Mbit/s SPI with show at end
# mem after init, before run 142528
# mem after run 101872
# 3.240551

# viper
# show on each draw
# mem after init, before run 142784
# mem after run 85088
# 76.85363

# show at end
# mem after init, before run 142784
# mem after run 104224
# 0.2851456
