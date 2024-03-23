"""XIAO ESP32-C3 with ili9341 via  ST7789 240x320 display"""

from machine import Pin, SPI, SoftSPI
import st7789
import xpt2046

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
_BAUD = const(10_250_000)  # lower baud for touch
_SCK_PIN = const(8)
_MOSI_PIN = const(10)
_MISO_PIN = const(20)  # 9 SPI default if low no startup, 20 is RX
_RST_PIN = const(3)
_CS_PIN = const(5)
_DC_PIN = const(4)
_BKLT_PIN = const(2)
_HEIGHT = const(320)
_WIDTH = const(240)
_TCS_PIN = const(6)
_TIRQ_PIN = const(7)


def config(
    rotation=0,
    buffer_size=0,
    options=0,
    inversion=False,  # True for display capacitive touch
    touch_handle=None,
    softspi=False,
    verbose=False,
):
    """Configure the display using a custom_init and
    custom_rotations since the display is ili9341. The custom_init is a
    list of commands to send to the display during the init() metehod. The
    list contains tuples with a bytes object, optionally followed by a
    delay specified in ms. The first byte of the bytes object contains the
    command to send optionally followed by data bytes.
    """

    custom_init = [
        (b"\x01", 150),  # soft reset
        (b"\x11", 255),  # exit sleep
        (b"\xCB\x39\x2C\x00\x34\x02",),  # power control A
        (b"\xCF\x00\xC1\x30",),  # power control B
        (b"\xE8\x85\x00\x78",),  # driver timing control A
        (b"\xEA\x00\x00",),  # driver timing control B
        (b"\xED\x64\x03\x12\x81",),  # power on sequence control
        (b"\xF7\x20",),  # pump ratio control
        (b"\xC0\x23",),  # power control,VRH[5:0]
        (b"\xC1\x10",),  # Power control,SAP[2:0];BT[3:0]
        (b"\xC5\x3E\x28",),  # vcm control
        (b"\xC7\x86",),  # vcm control 2
        (b"\x3A\x55",),  # pixel format
        # Inversion on or off
        (b"\x21", 255) if inversion else (b"\x20", 255),
        (b"\xB1\x00\x18",),  # frameration control,normal mode full colours
        (b"\xB6\x08\x82\x27",),  # display function control
        (b"\xF2\x00",),  # 3gamma function disable
        (b"\x26\x01",),  # gamma curve selected
        # set positive gamma correction
        (b"\xE0\x0F\x31\x2B\x0C\x0E\x08\x4E\xF1\x37\x07\x10\x03\x0E\x09\x00",),
        # set negative gamma correction
        (b"\xE1\x00\x0E\x14\x03\x11\x07\x31\xC1\x48\x08\x0F\x0C\x31\x36\x0F",),
        (b"\x29", 100),  # display on
    ]

    custom_rotations = [
        (0x48, 240, 320, 0, 0),
        (0x28, 320, 240, 0, 0),
        (0x88, 240, 320, 0, 0),
        (0xE8, 320, 240, 0, 0),
    ]
    # SoftSPI(baudrate=30000000, polarity=1, sck=Pin(_SCK_PIN),
    #         mosi=Pin(_MOSI_PIN), miso=Pin(_MISO_PIN)),
    if softspi:
        spi = SoftSPI(
            baudrate=_BAUD,
            # polarity=1,
            sck=Pin(_SCK_PIN),
            mosi=Pin(_MOSI_PIN),
            miso=Pin(_MISO_PIN),
        )
    else:
        spi = SPI(
            1,
            baudrate=_BAUD,
            # polarity=1,
            sck=Pin(_SCK_PIN),
            mosi=Pin(_MOSI_PIN),
            miso=Pin(_MISO_PIN),
        )
    touchint = (touch_handle is not None) and (_TIRQ_PIN is not None)
    if verbose:
        print(
            "creating ili via st7789 {}x{}  driver rot={}".format(
                _WIDTH, _HEIGHT, rotation
            )
        )
        print(" touch interrupt = {}".format(touchint))
        print("spi created")
        print(spi)
    disp = st7789.ST7789(
        spi,
        _WIDTH,
        _HEIGHT,
        reset=Pin(_RST_PIN, Pin.OUT),
        cs=Pin(_CS_PIN, Pin.OUT),
        dc=Pin(_DC_PIN, Pin.OUT),
        backlight=Pin(_BKLT_PIN, Pin.OUT),
        custom_init=custom_init,
        rotations=custom_rotations,
        rotation=rotation,
        color_order=st7789.RGB,
        inversion=inversion,
        options=options,
        buffer_size=buffer_size,
    )
    touch = xpt2046.Touch(
        spi,
        cs=Pin(_TCS_PIN),
        int_pin=Pin(_TIRQ_PIN) if touchint else None,
        int_handler=touch_handle if touchint else None,
    )
    return disp, touch
