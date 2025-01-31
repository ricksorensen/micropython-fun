import os


def mountsd(baud=25_000_000, misop=None, soft=False):
    if os.uname().machine.count("XIAO RP2040"):
        from machine import SoftSPI, SPI, Pin
        from sdcard import SDCard

        #    CS  xpin3   D2   P28
        #   SCK  xpin9   SCK  P2
        #  MISO  xpin10  MISO P4
        #  MOSI  xpin11  MOSI P3
        mip = 4 if misop is None else misop
        if soft:
            spi = SoftSPI(
                baudrate=1_000_000,
                polarity=0,
                phase=0,
                bits=8,
                firstbit=SPI.MSB,
                sck=Pin(2),
                mosi=Pin(3),
                miso=Pin(mip),
            )
        else:
            spi = SPI(
                0,
                baudrate=1_000_000,
                polarity=0,
                phase=0,
                bits=8,
                firstbit=SPI.MSB,
                sck=Pin(2),
                mosi=Pin(3),
                miso=Pin(mip),
            )
        sd = SDCard(spi, Pin(28, Pin.OUT))
        sd.init_spi(baud)
        os.mount(sd, "/sd")
        print("RP2040")
        print(spi)
        print(os.listdir("/sd"))
    elif os.uname().machine.count("ESP32S3") and os.uname().machine.count("XIAO"):
        from machine import SoftSPI, SPI, Pin  # SDCard not sure how this works
        from sdcard import SDCard  # so use micropython sdcard

        #    CS  xpin3   D2   GPIO3
        #   SCK  xpin9   SCK  GPIO7
        #  MISO  xpin10  MISO GPIO8
        #  MOSI  xpin11  MOSI GPIO9
        mip = 8 if misop is None else misop
        if soft:
            spi = SoftSPI(
                baudrate=1_000_000,
                polarity=0,
                phase=0,
                bits=8,
                firstbit=SPI.MSB,
                sck=Pin(7),
                mosi=Pin(9),
                miso=Pin(mip),
            )
        else:
            spi = SPI(
                1,
                baudrate=1_000_000,
                polarity=0,
                phase=0,
                bits=8,
                firstbit=SPI.MSB,
                sck=Pin(7),
                mosi=Pin(9),
                miso=Pin(mip),
            )

        sd = SDCard(spi, Pin(3))
        sd.init_spi(baud)
        os.mount(sd, "/sd")
        print("ESP32S3")
        print(spi)
        print(os.listdir("/sd"))
    elif os.uname().machine.count("ESP32C3") and os.uname().machine.count("XIAO"):
        from machine import SoftSPI, SPI, Pin  # SDCard not sure how this works
        from sdcard import SDCard  # so use micropython sdcard

        #    CS  xpin3   D2   GPIO4
        #   SCK  xpin9   SCK  GPIO8
        #  MISO  xpin10  MISO GPIO9 --> GPIO20 (RX) for strappin
        #  MOSI  xpin11  MOSI GPIO10
        mip = 9 if misop is None else misop
        if soft:
            spi = SoftSPI(
                baudrate=1_000_000,
                polarity=0,
                phase=0,
                bits=8,
                firstbit=SPI.MSB,
                sck=Pin(8),
                mosi=Pin(10),
                miso=Pin(mip),
            )
        else:
            spi = SPI(
                1,
                baudrate=1_000_000,
                polarity=0,
                phase=0,
                bits=8,
                firstbit=SPI.MSB,
                sck=Pin(8),
                mosi=Pin(10),
                miso=Pin(mip),
            )

        sd = SDCard(spi, Pin(4))
        sd.init_spi(baud)
        os.mount(sd, "/sd")
        print("ESP32C3")
        print(spi)
        print(os.listdir("/sd"))
    else:
        print("unknown sd config")
