"""XIAO RP2 with  ST7789 240x320 display"""

from machine import Pin, SPI
import st7789

TFA = 0  # top free area when scrolling
BFA = 0  # bottom free area when scrolling
# XIAO RP2040 Pins
# SCK      Pin  9     Pin(2)
# MOSI     Pin 11     Pin(3)
# MISO     Pin 10     Pin(4) unused
# RST      Pin  2     Pin(27) (D1)
# CS       Pin  4     Pin(29) (D3)
# DC       Pin  3     Pin(28) (D2)
# BKLT     Pin  1     Pin(26) (D0)
_BAUD = const(62_500_000)  # lower baud for touch
_SCK_PIN = const(2)
_MOSI_PIN = const(3)
_MISO_PIN = const(4)
_RST_PIN = const(27)
_CS_PIN = const(29)
_DC_PIN = const(28)
_BKLT_PIN = const(26)
_HEIGHT = const(320)
_WIDTH = const(240)
_TCS_PIN = const(6)
_TIRQ_PIN = const(7)


def config(rotation=0, buffer_size=0, options=0, verbose=False):
    # spi = SoftSPI(baudrate=_BAUD, sck=Pin(_SCK_PIN), mosi=Pin(_MOSI_PIN), miso=Pin(_MISO_PIN))

    spi = SPI(
        0,
        baudrate=_BAUD,
        # polarity=0,
        sck=Pin(_SCK_PIN),
        mosi=Pin(_MOSI_PIN),
        miso=None,
    )
    if verbose:
        print("creating  st7789 {}x{}  driver rot={}".format(_WIDTH, _HEIGHT, rotation))
        print("  TFA: {}   BFA {}".format(TFA, BFA))
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
