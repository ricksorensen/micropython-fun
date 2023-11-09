"""Generic ESP32 with ST7789 240x320 display"""

# XIAO NRF
from machine import Pin, SoftSPI
import st7789

TFA = 0  # RP2 was 40
BFA = 0  # RP2 was 40
# XIAO ESP32C3 Pins
# SCK      Pin  9     Pin(45)
# MOSI     Pin 11     Pin(47)
# MISO     Pin 10     Pin(46) unused
# RST      Pin  2     Pin(3) (D1)
# CS       Pin  4     Pin(29) (D3)
# DC       Pin  3     Pin(28) (D2)
# BKLT     Pin  1     Pin(2) (D0)


def config(rotation=0, buffer_size=0, options=0):
    return st7789.ST7789(
        SoftSPI(baudrate=31250000, sck=Pin(45), mosi=Pin(47), miso=Pin(46)),
        135,
        240,
        reset=Pin(3, Pin.OUT),
        cs=Pin(29, Pin.OUT),
        dc=Pin(28, Pin.OUT),
        backlight=Pin(2, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size=buffer_size,
    )
