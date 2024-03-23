"""XIAO RP2 with ili9341 cap touch via  ST7789 240x320 display"""

from machine import Pin, SPI, SoftI2C
import focaltouch
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
###
# T_SDA    Pin  5     Pin(6)  (D4/SDA)
# T_SCL    Pin  6     Pin(7)  (D5/SCL)
# T_RST    Pin  7     Pin(0)  (D6/TX)
# T_IRQ    Pin  8     Pin(1)  (D7/RX)

_BAUD = const(6_250_000)  # lower baud for touch
_SCK_PIN = const(2)
_MOSI_PIN = const(3)
_MISO_PIN = const(4)
_RST_PIN = const(27)
_CS_PIN = const(29)
_DC_PIN = const(28)
_BKLT_PIN = const(26)
_HEIGHT = const(320)
_WIDTH = const(240)
_TSDA_PIN = const(6)
_TnRST_PIN = const(0)
_TSCL_PIN = const(7)
_TIRQ_PIN = const(1)


# for capacitive touch ili9341 inversion should be true
def config(
    rotation=0,
    buffer_size=0,
    options=0,
    inversion=True,
    touch_handle=None,
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
        (b"\xED\x64\x03\x12\x81",),  # power on sequence control[
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
    spi = SPI(
        0,
        baudrate=_BAUD,
        # polarity=0,
        sck=Pin(_SCK_PIN),
        mosi=Pin(_MOSI_PIN),
        miso=Pin(_MISO_PIN),
    )
    touchint = (touch_handle is not None) and (_TIRQ_PIN is not None)
    if verbose:
        print(
            "creating ili via st7789 {}x{}  driver rot={} inversion={}".format(
                _WIDTH, _HEIGHT, rotation, inversion
            )
        )
        print(" touch interrupt = {}".format(touchint))
        print("spi created")
        print(spi)
    # note: if custom initialization
    #          inversion is not set during init, assumed in custom?
    #       if not in custom, need to set after init()
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
    # touch_i2c = I2C(1, scl=Pin(_TSCL_PIN), sda=Pin(_TSDA_PIN))
    rst = Pin(_TnRST_PIN, mode=Pin.OUT, value=1)  # take touch out of reset
    touch_i2c = SoftI2C(scl=Pin(_TSCL_PIN), sda=Pin(_TSDA_PIN))
    touch = focaltouch.FocalTouch(touch_i2c)
    return disp, touch


####
# no inversion(default:True), color_order(default:RGB) in initialization
# tft_init() -> madctl=0x48, fill(RED) give cyan
# inversion_mode(True) --> screen adapts immediately, to RED

#### Focaltouch:
# init: i2c, address=_FT6206_DEFAULT_I2C_ADDR, debug=False
# touched() returns number of touches currently detected
# touches() returns list of touchpont dicts{'x':xt, 'y':yt, 'it':touch#}
