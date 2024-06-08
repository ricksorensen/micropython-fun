# xiao esp32c3 with st7789 driver 

# Released under the MIT License (MIT). See LICENSE.
# Copyright (c) 2023 Peter Hinch

# As written, supports:

from machine import Pin, SPI, freq
import gc

# this is slow. no native support for RISC-V yet
from drivers.st7789.st7789_4bit_uplcopy import *

SSD = ST7789

# https://github.com/Bodmer/TFT_eSPI/discussions/2757
# on S3-  GPIO 26-37 are used by SPI0/1 for (Q)SPI PSRAM/Flash connections

pdc = Pin(4, Pin.OUT, value=0)  # Arbitrary pins 
prst = Pin(3, Pin.OUT, value=1)
pcs = Pin(5, Pin.OUT, value=1)
pbl = Pin(2, Pin.OUT, value=1)
gc.collect()  # Precaution before instantiating framebuf
spi = SPI(1, 40_000_000, sck=Pin(8), mosi=Pin(10), miso=Pin(9))  # No need to wire MISO.
# freq(160_000_000)   # this is default
# options ...
# disp_mode: LANDSCAPE, REFLECT, USD, PORTRAIT
# display: GENERIC(0,0,0) TDISPLAY(52,40,1) PI_PICO_LCD_2(0,0,1) DFR0995 (34,0,0)
#         x,y offset used in set_window,
#         orientation(0 or 1) if true flip portrait

gc.collect()  # Precaution before instantiating framebuf
ssd = SSD(
    spi,
    cs=pcs,
    dc=pdc,
    rst=prst,
    height=135,
    width=240,
    disp_mode=LANDSCAPE,  # REFLECT,USD, PORTRAIT
    display=TDISPLAY,  # (xoff,yoff,orient)
)
gc.collect()  # Precaution before instantiating framebuf
