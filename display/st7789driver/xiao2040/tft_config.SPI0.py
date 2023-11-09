"""Waveshare Pico LCD 1.14 inch display"""

from machine import Pin, SPI
import st7789

TFA = 40  # top free area when scrolling
BFA = 40  # bottom free area when scrolling
# XIAO RP2040 Pins
# SCK      Pin  9     Pin(2)
# MOSI     Pin 11     Pin(3)
# MISO     Pin 10     Pin(4) unused
# RST      Pin  2     Pin(27) (D1)
# CS       Pin  4     Pin(29) (D3)
# DC       Pin  3     Pin(28) (D2)
# BKLT     Pin  1     Pin(26) (D0)


def config(rotation=0, buffer_size=0, options=0):
    return st7789.ST7789(
        # SoftSPI(baudrate=30000000, polarity=1, sck=Pin(2), mosi=Pin(3), miso=Pin(4)),
        SPI(0, baudrate=62500000, polarity=1, sck=Pin(2), mosi=Pin(3), miso=Pin(4)),
        135,
        240,
        reset=Pin(27, Pin.OUT),
        cs=Pin(29, Pin.OUT),
        dc=Pin(28, Pin.OUT),
        backlight=Pin(26, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size=buffer_size,
    )
