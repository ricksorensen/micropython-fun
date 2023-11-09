# The MIT License (MIT)
# Copyright (c) 2022 Mike Teachman
# https://opensource.org/licenses/MIT
#
# Purpose:  Play a WAV audio file out of a speaker or headphones
#
# https://github.com/miketeachman/micropython-i2s-examples/tree/master/examples
import os
import time
from machine import Pin

from wavplayer import WavPlayer

# I2S Signals
#   SCK (BCK) Signal Clock AKA bit clock
#   WS (LRCK) word select AKA left right clock, sometimes LCK
#   SD (DIN)  serial data ADA data in
machinename = os.uname().machine
if "XIAO" in machinename:
    # from machine import SDCard

    # ======= SD CARD CONFIGURATION =======
    # sd = SDCard(slot=2)  # sck=18, mosi=23, miso=19, cs=5
    # os.mount(sd, "/sd")
    # ======= SD CARD CONFIGURATION =======

    # ======= I2S CONFIGURATION =======
    SCK_PIN = 6  # XIAO Pin5/SDA
    WS_PIN = 7  # XIAO Pin6/SCL
    # GPIO8 (XIAO Pin9/SCK) conflicts with SD Card SPI
    SD_PIN = 3  # XIAO Pin 2/A1
    I2S_ID = 0
    BUFFER_LENGTH_IN_BYTES = 40000
    # ======= I2S CONFIGURATION =======
elif "TinyS3" in machinename:
    # from machine import SDCard

    # ======= SD CARD CONFIGURATION =======
    # sd = SDCard(slot=2)  # sck=18, mosi=23, miso=19, cs=5
    # os.mount(sd, "/sd")
    # ======= SD CARD CONFIGURATION =======

    # ======= I2S CONFIGURATION =======
    SCK_PIN = 6
    WS_PIN = 7
    SD_PIN = 8
    I2S_ID = 0
    BUFFER_LENGTH_IN_BYTES = 40000
    # ======= I2S CONFIGURATION =======
elif "Generic ESP32S3" in machinename:
    # WROOM: machine = 'ESP32S3 module (spiram octal) with ESP32S3'
    # from machine import SDCard

    # ======= SD CARD CONFIGURATION =======
    # sd = SDCard(slot=2)  # sck=18, mosi=23, miso=19, cs=5
    # os.mount(sd, "/sd")
    # ======= SD CARD CONFIGURATION =======

    # ======= I2S CONFIGURATION =======
    SCK_PIN = 6
    WS_PIN = 7
    SD_PIN = 8
    I2S_ID = 0
    BUFFER_LENGTH_IN_BYTES = 40000
    # ======= I2S CONFIGURATION =======
else:
    print("Warning: program not tested with this board")

print("Machine: ", machinename)
print("  SCK:{} WS:{} SD:{}".format(SCK_PIN, WS_PIN, SD_PIN))

wp = WavPlayer(
    id=I2S_ID,
    sck_pin=Pin(SCK_PIN),
    ws_pin=Pin(WS_PIN),
    sd_pin=Pin(SD_PIN),
    ibuf=BUFFER_LENGTH_IN_BYTES,
    root="/",
)

# try mono first
# wp.play("music-16k-16bits-mono.wav", loop=False)
# while wp.isplaying():
#    pass

time.sleep(10)

wp.play("music-16k-16bits-stereo.wav", loop=False)
# wait until the entire WAV file has been played
while wp.isplaying():
    # other actions can be done inside this loop during playback
    pass

wp.play("music-16k-16bits-mono.wav", loop=False)
time.sleep(10)  # play for 10 seconds
wp.pause()
time.sleep(5)  # pause playback for 5 seconds
wp.resume()  # continue playing to the end of the WAV file
