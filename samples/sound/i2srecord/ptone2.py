# The MIT License (MIT)
# Copyright (c) 2022 Mike Teachman
# https://opensource.org/licenses/MIT

# Purpose:  Play a pure audio tone out of a speaker or headphones
#
# - write audio samples containing a pure tone to an I2S amplifier or DAC module
# - tone will play continuously in a loop until
#   a keyboard interrupt is detected or the board is reset
#
# Blocking version
# - the write() method blocks until the entire sample buffer is written to I2S
# https://github.com/miketeachman/micropython-i2s-examples/tree/master/examples
import math
import struct
import time
from machine import I2S
from machine import Pin


def make_tone(rate, bits, frequency):
    # create a buffer containing the pure tone samples
    samples_per_cycle = int(rate // frequency)
    sample_size_in_bytes = bits // 8
    samples = bytearray(samples_per_cycle * sample_size_in_bytes)
    volume_reduction_factor = 32
    range = pow(2, bits) // 2 // volume_reduction_factor

    if bits == 16:
        format = "<h"
    else:  # assume 32 bits
        format = "<l"

    for i in range(samples_per_cycle):
        sample = range + int(
            (range - 1) * math.sin(2 * math.pi * i / samples_per_cycle)
        )
        struct.pack_into(format, samples, i * sample_size_in_bytes, sample)

    return samples


# ======= I2S CONFIGURATION =======
SCK_PIN = 6  # 26
WS_PIN = 7  # 27
SD_PIN = 26  # 6
I2S_ID = 0
BUFFER_LENGTH_IN_BYTES = 2000
# ======= I2S CONFIGURATION =======


# ======= AUDIO CONFIGURATION =======
TONE_FREQUENCY_IN_HZ = 440
SAMPLE_SIZE_IN_BITS = 16
FORMAT = I2S.MONO  # only MONO supported in this example
SAMPLE_RATE_IN_HZ = 44_100
# ======= AUDIO CONFIGURATION =======


def dotone(f=TONE_FREQUENCY_IN_HZ):
    flist = f
    if type(f) is not list:
        flist = [f]
    samples = []
    for x in flist:
        samples.append(make_tone(SAMPLE_RATE_IN_HZ, SAMPLE_SIZE_IN_BITS, x))
    audio_out = I2S(
        0,
        sck=Pin(6),
        ws=Pin(7),
        sd=Pin(26),
        mode=I2S.TX,
        bits=16,
        format=I2S.MONO,
        rate=44_100,
        ibuf=2000,
    )

    print(audio_out)
    print("sample size:", len(samples))
    # continuously write tone sample buffer to an I2S DAC
    print(f"==========  START PLAYBACK f={f} ==========")
    try:
        while True:
            for s in samples:
                ct = time.ticks_ms()
                while time.ticks_diff(time.ticks_ms(), ct) < 500:
                    _ = audio_out.write(s)

    except (KeyboardInterrupt, Exception) as e:
        print("caught exception {} {}".format(type(e).__name__, e))

    # cleanup
    audio_out.deinit()
    print("Done")
