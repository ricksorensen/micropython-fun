"""NRF with ST7789 240x320 display"""

# XIAO NRF
from machine import Pin, SPI
import st7789

TFA = 0  # RP2 was 40, using 0 leaves noise on scrolls
BFA = 0  # RP2 was 40, using 0 leaves noise on scrolls
# XIAO NRF52840 Pins
# SCK      Pin  9     Pin(45) P1.13
# MOSI     Pin 11     Pin(47) P1.15
# MISO     Pin 10     Pin(46) P1.14
# RST      Pin  2     Pin(3) (D1)  P0.03
# CS       Pin  4     Pin(29) (D3) P0.29
# DC       Pin  3     Pin(28) (D2) P0.28
# BKLT     Pin  1     Pin(2) (D0)  P0.02

_WID = 240
_HT = 320


def config(rotation=0, buffer_size=0, options=0, verbose=False):
    spi = SPI(
        0, baudrate=62500000, sck=Pin(45), mosi=Pin(47), miso=Pin(46)
    )  # miso=Pin(46)
    if verbose:
        print(f"size {_WID}w x {_HT}h    rotation={rotation}")
        print(spi)

    return st7789.ST7789(
        spi,
        width=_WID,
        height=_HT,
        reset=Pin(3, Pin.OUT),
        cs=Pin(29, Pin.OUT),
        dc=Pin(28, Pin.OUT),
        backlight=Pin(2, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size=buffer_size,
    )
