"""EPS32C3 XIAO with ST7789 240x320 display"""

# XIAO ESP32C3
from machine import Pin, SPI
import st7789

TFA = 0
BFA = 0
# XIAO ESP32C3 Pins
# SCK      Pin  9     Pin(8)
# MOSI     Pin 11     Pin(10)
# MISO     Pin 10     Pin(9) unused
# RST      Pin  2     Pin(3) (D1)
# CS       Pin  4     Pin(5) (D3)
# DC       Pin  3     Pin(4) (D2)
# BKLT     Pin  1     Pin(2) (D0)
_BAUD = const(62_500_000)
_SCK_PIN = const(8)
_MOSI_PIN = const(10)
_MISO_PIN = const(9)
_RST_PIN = const(3)
_CS_PIN = const(5)
_DC_PIN = const(4)
_BKLT_PIN = const(2)
_HEIGHT = const(320)
_WIDTH = const(240)


def config(rotation=0, buffer_size=0, options=0, verbose=False):
    spi = SPI(1, baudrate=_BAUD, sck=Pin(_SCK_PIN), mosi=Pin(_MOSI_PIN))
    if verbose:
        print(
            "creating via st7789 {}x{}  driver rot={}".format(_WIDTH, _HEIGHT, rotation)
        )
        print("spi created")
        print(spi)

    return st7789.ST7789(
        spi,
        _WIDTH,
        _HEIGHT,
        reset=Pin(_RST_PIN, Pin.OUT),
        cs=Pin(_CS_PIN, Pin.OUT),
        dc=Pin(_DC_PIN, Pin.OUT),
        backlight=Pin(_BKLT_PIN, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size=buffer_size,
    )
