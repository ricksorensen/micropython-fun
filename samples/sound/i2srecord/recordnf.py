# The MIT License (MIT)
# Copyright (c) 2022 Mike Teachman
# https://opensource.org/licenses/MIT

# Purpose: Read audio samples from an I2S microphone and write to SD card
#
# - read 32-bit audio samples from I2S hardware, typically an I2S MEMS Microphone
# - convert 32-bit samples to specified bit size
# - write samples to a SD card file in WAV format
# - samples will be continuously written to the WAV file
#   until a keyboard interrupt (ctrl-c) is detected
#
# Blocking version
# - the readinto() method blocks until
#   the supplied buffer is filled

import os
from machine import Pin
from machine import I2S
import gc
import time
from myconfig import SCK_PIN, WS_PIN, SD_PIN, I2S_ID, BUFFER_LENGTH_IN_BYTES

# ======= AUDIO CONFIGURATION =======
WAV_FILE = "mic.wav"
RECORD_TIME_IN_SECONDS = 20
WAV_SAMPLE_SIZE_IN_BITS = 16  # 248 invalid
FORMAT = I2S.MONO
SAMPLE_RATE_IN_HZ = 22_050
# ======= AUDIO CONFIGURATION =======

format_to_channels = {I2S.MONO: 1, I2S.STEREO: 2}
NUM_CHANNELS = format_to_channels[FORMAT]
WAV_SAMPLE_SIZE_IN_BYTES = WAV_SAMPLE_SIZE_IN_BITS // 8
RECORDING_SIZE_IN_BYTES = (
    RECORD_TIME_IN_SECONDS * SAMPLE_RATE_IN_HZ * WAV_SAMPLE_SIZE_IN_BYTES * NUM_CHANNELS
)

# SPDX-License-Identifier: CC0-1.0


def create_wav_header(sampleRate, bitsPerSample, num_channels, num_samples):
    datasize = num_samples * num_channels * bitsPerSample // 8
    o = bytes("RIFF", "ascii")  # (4byte) Marks file as RIFF
    o += (datasize + 36).to_bytes(
        4, "little"
    )  # (4byte) File size in bytes excluding this and RIFF marker
    o += bytes("WAVE", "ascii")  # (4byte) File type
    o += bytes("fmt ", "ascii")  # (4byte) Format Chunk Marker
    o += (16).to_bytes(4, "little")  # (4byte) Length of above format data
    o += (1).to_bytes(2, "little")  # (2byte) Format type (1 - PCM)
    o += (num_channels).to_bytes(2, "little")  # (2byte)
    o += (sampleRate).to_bytes(4, "little")  # (4byte)
    o += (sampleRate * num_channels * bitsPerSample // 8).to_bytes(
        4, "little"
    )  # (4byte)
    o += (num_channels * bitsPerSample // 8).to_bytes(2, "little")  # (2byte)
    o += (bitsPerSample).to_bytes(2, "little")  # (2byte)
    o += bytes("data", "ascii")  # (4byte) Data Chunk Marker
    o += (datasize).to_bytes(4, "little")  # (4byte) Data size in bytes
    return o


wav_header = create_wav_header(
    SAMPLE_RATE_IN_HZ,
    WAV_SAMPLE_SIZE_IN_BITS,
    NUM_CHANNELS,
    SAMPLE_RATE_IN_HZ * RECORD_TIME_IN_SECONDS,
)


def writewav(buf, fname):
    with open(fname, "wb") as fo:
        nbw = fo.write(wav_header)
        nbw += fo.write(buf)


def grab(nsamp=20000, enc="<"):
    #    import array
    import struct

    gc.collect()
    bfr = bytearray(nsamp)
    bfr_mv = memoryview(bfr)
    audio_in = I2S(
        I2S_ID,
        sck=Pin(SCK_PIN),
        ws=Pin(WS_PIN),
        sd=Pin(SD_PIN),
        mode=I2S.RX,
        bits=WAV_SAMPLE_SIZE_IN_BITS,
        format=FORMAT,
        rate=SAMPLE_RATE_IN_HZ,
        ibuf=BUFFER_LENGTH_IN_BYTES,
    )

    nread = audio_in.readinto(bfr_mv)
    print(f"{nread} bytes read")
    audio_in.deinit()
    #   dout = array.array("h", bfr_mv[:nread])
    dout = struct.unpack(f"{enc}{nread//2}h", bfr_mv[:nread])
    # print(dout)
    writewav(bfr[:nread], "testit.wav")
    return dout, bfr[:nread]


def doit(
    wavfile,
    delaywrite=False,
    sampbfr=100000,
    dlast=None,
    deinit=True,
    audio_in=None,
    delay=None,
):
    wav = None
    print("doit start: ", gc.mem_free())
    if not delaywrite and (wavfile is not None):
        wav = open(wavfile, "wb")
        # create header for WAV file and write to SD card
        num_bytes_written = wav.write(wav_header)
    print("doit after wav header: ", gc.mem_free())

    if not audio_in:
        audio_in = I2S(
            I2S_ID,
            sck=Pin(SCK_PIN),
            ws=Pin(WS_PIN),
            sd=Pin(SD_PIN),
            mode=I2S.RX,
            bits=WAV_SAMPLE_SIZE_IN_BITS,
            format=FORMAT,
            rate=SAMPLE_RATE_IN_HZ,
            ibuf=BUFFER_LENGTH_IN_BYTES,
        )
        print("new audio_in I2S created")
    print("doit after I2S: ", gc.mem_free())

    # allocate sample arrays
    # memoryview used to reduce heap allocation in while loop
    mic_samples = bytearray(sampbfr)
    mic_samples_mv = memoryview(mic_samples)
    print("doit bytearray: ", gc.mem_free())

    num_sample_bytes_written_to_wav = 0
    num_bytes_to_write = 0
    print(os.uname().machine)
    print("Recording size: {} bytes\n I2S:".format(RECORDING_SIZE_IN_BYTES))
    # print(audio_in)
    if delay:
        time.sleep_ms(delay)  # no flush on print for upy ... rp2 with internal file
    print("mic_samples size: ", len(mic_samples))
    print("wav file: ", wavfile)
    gc.collect()
    print("mem_free: ", gc.mem_free())

    print("==========  START RECORDING ==========")
    # time.sleep(0.5)
    try:
        gc.collect()
        while num_sample_bytes_written_to_wav < RECORDING_SIZE_IN_BYTES:
            # read a block of samples from the I2S microphone
            num_bytes_read_from_mic = audio_in.readinto(mic_samples_mv)
            if num_bytes_read_from_mic > 0:
                num_bytes_to_write = min(
                    num_bytes_read_from_mic,
                    RECORDING_SIZE_IN_BYTES - num_sample_bytes_written_to_wav,
                )
                if wav is not None:
                    # write samples to WAV file
                    num_bytes_written = wav.write(mic_samples_mv[:num_bytes_to_write])
                    num_sample_bytes_written_to_wav += num_bytes_written
                else:
                    num_sample_bytes_written_to_wav += num_bytes_to_write  # RJS no file
                # print("totnew: ", num_bytes_read_from_mic)
            else:
                print("no bytes read")
        print("==========  DONE RECORDING ==========")
        print("mem_free after record: ", gc.mem_free())
    except (KeyboardInterrupt, Exception) as e:
        print("caught exception {} {}".format(type(e).__name__, e))
    finally:
        if deinit:
            audio_in.deinit()
            print("I2S deinit complete")
            audio_in = None
    # cleanup
    gc.collect()
    print("mem_free before close:", gc.mem_free())
    if wav is not None:
        wav.close()
        print("file closed")
        gc.collect()
        print("mem_free after file close:", gc.mem_free())
    elif delaywrite and (wavfile is not None):
        nbo = min(RECORDING_SIZE_IN_BYTES, len(mic_samples))
        writewav(mic_samples_mv[:nbo], wavfile)
        ostr = f"{wavfile} wrote buffer len {nbo}"
        if nbo < RECORDING_SIZE_IN_BYTES:
            ostr = (
                ostr + f" .... incomplete delayed recording < {RECORDING_SIZE_IN_BYTES}"
            )
        print(ostr)
    elif delaywrite:
        print("dumparray")
        import array

        gc.collect()
        ix = 0
        while ix < RECORDING_SIZE_IN_BYTES:
            print(array.array("h", mic_samples_mv[ix : ix + 2])[0])
            ix = ix + 2
    gc.collect()
    if dlast is not None:
        #  import struct
        import array

        lb = max(0, num_bytes_to_write - dlast)
        nb = num_bytes_to_write - lb
        print("last bytes:")
        print(mic_samples_mv[lb:num_bytes_to_write].hex())
        print(f"dump last {nb}  [{lb}:]")
        # print(struct.unpack(f"<{nb//2}h", mic_samples_mv[lb:]))
        dx = array.array("h", mic_samples[lb:num_bytes_to_write])
        print(dx)
    return audio_in
