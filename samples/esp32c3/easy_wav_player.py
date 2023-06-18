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


if os.uname().machine.count("XIAO"):
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

wp = WavPlayer(
    id=I2S_ID,
    sck_pin=Pin(SCK_PIN),
    ws_pin=Pin(WS_PIN),
    sd_pin=Pin(SD_PIN),
    ibuf=BUFFER_LENGTH_IN_BYTES,
    root="/",
)

wp.play("music-16k-16bits-stereo.wav", loop=False)
# wait until the entire WAV file has been played
while wp.isplaying() == True:
    # other actions can be done inside this loop during playback
    pass

wp.play("music-16k-16bits-mono.wav", loop=False)
time.sleep(10)  # play for 10 seconds
wp.pause()
time.sleep(5)  # pause playback for 5 seconds
wp.resume()  # continue playing to the end of the WAV file
