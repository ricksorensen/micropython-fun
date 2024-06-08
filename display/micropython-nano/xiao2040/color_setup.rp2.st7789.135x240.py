# xiao rp2 with st7789 driver

# Released under the MIT License (MIT). See LICENSE.
# Copyright (c) 2021 Peter Hinch

# As written, supports:

from machine import Pin, SPI
import gc

from drivers.st7789.st7789_4bit import *

SSD = ST7789

pdc = Pin(28, Pin.OUT, value=0)  # Arbitrary pins
pcs = Pin(29, Pin.OUT, value=1)
prst = Pin(27, Pin.OUT, value=1)

gc.collect()  # Precaution before instantiating framebuf
# options ...
# disp_mode: LANDSCAPE, REFLECT, USD, PORTRAIT
# display: GENERIC(0,0,0) TDISPLAY(52,40,1) PI_PICO_LCD_2(0,0,1) DFR0995 (34,0,0)
#         x,y offset used in set_window,
#         orientation(0 or 1) if true flip portrait# Conservative low baudrate. Can go to 62.5MHz. Depending on wiring.
spi = SPI(0, 62_500_000, sck=Pin(2), mosi=Pin(3), miso=None)
ssd = SSD(
    spi,
    dc=pdc,
    cs=pcs,
    rst=prst,
    height=135,
    width=240,
    disp_mode=LANDSCAPE,
    display=TDISPLAY,
)
