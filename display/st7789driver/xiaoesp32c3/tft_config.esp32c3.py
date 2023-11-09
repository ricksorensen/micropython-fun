"""Generic ESP32 with ST7789 240x320 display"""

# XIAO ESP32C3
from machine import Pin, SPI
import st7789

TFA = 40  # RP2 was 40, using 0 leaves noise on scrolls
BFA = 40  # RP2 was 40, using 0 leaves noise on scrolls
# XIAO ESP32C3 Pins
# SCK      Pin  9     Pin(8)
# MOSI     Pin 11     Pin(10)
# MISO     Pin 10     Pin(9) unused
# RST      Pin  2     Pin(3) (D1)
# CS       Pin  4     Pin(5) (D3)
# DC       Pin  3     Pin(4) (D2)
# BKLT     Pin  1     Pin(2) (D0)


def config(rotation=0, buffer_size=0, options=0):
    return st7789.ST7789(
        SPI(1, baudrate=31250000, sck=Pin(8), mosi=Pin(10)),
        135,
        240,
        reset=Pin(3, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(4, Pin.OUT),
        backlight=Pin(2, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size=buffer_size,
    )
