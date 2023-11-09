"""tinys3 NRF with ST7789 135x240 display"""

# TINY S3
from machine import Pin, SPI
import st7789

TFA = 40  # RP2 was 40, using 0 leaves noise on scrolls
BFA = 40  # RP2 was 40, using 0 leaves noise on scrolls
# TINY S3 Pins  SPI_SS is GPIO34 slave select sent by master, paired with CS?
# SCK      Pin  3     Pin(36) SPI_SCK
# MOSI     Pin  1     Pin(35) SPI_MOSI
# MISO     Pin  2     Pin(37) SPI_MISO
# RST      Pin  5     Pin(9)  I2C_SDA  labled wrong?
# CS       Pin  6     Pin(8)  I2C_SCL  labled wrong?
# DC       Pin  7     Pin(7)
# BKLT     Pin  8     Pin(6)


# works (after fonts are loaded!) ... see hellox.py
#    spi = SPI(2, baudrate=31250000, sck=Pin(5), mosi=Pin(4), miso=None)
#    spi = SPI(1, baudrate=31250000, sck=Pin(5), mosi=Pin(4), miso=None)
#    spi=SPI(1) : SPI(id=1, baudrate=500000, polarity=0, phase=0, bits=8, firstbit=0, sck=36, mosi=35, miso=37)
#    spi = SPI(1, baudrate=40000000, sck=Pin(36), mosi=Pin(35), miso=Pin(37))
# doesnt work ... SPI0 does not exist
#    spi = SPI(0, baudrate=31250000, sck=Pin(5), mosi=Pin(4), miso=None)


def config(rotation=0, buffer_size=0, options=0):
    print("creating driver rot={}".format(rotation))
    # spi = SPI(2, baudrate=31250000, sck=Pin(36), mosi=Pin(35), miso=Pin(37))
    spi = SPI(1, baudrate=40000000, sck=Pin(36), mosi=Pin(35), miso=Pin(37))
    print("spi created")
    print(spi)
    return st7789.ST7789(
        spi,
        135,
        240,
        reset=Pin(9, Pin.OUT),
        cs=Pin(8, Pin.OUT),
        dc=Pin(7, Pin.OUT),
        backlight=Pin(6, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size=buffer_size,
    )
