from machine import I2S, Pin
import time
import gc
import wavtool
from myconfig import SCK_PIN, WS_PIN, SD_PIN, I2S_ID, BUFFER_LENGTH_IN_BYTES


def grabmono(
    nsamp=20000,
    enc="<",
    sr=16000,
    filename="testit.wav",
    deinit=True,
    audio_in=None,
    initdelay=None,
    verbose=False,
):
    #    import array
    import struct

    gc.collect()
    bfr = bytearray(nsamp * 2)
    bfr_mv = memoryview(bfr)
    if not audio_in:
        audio_in = I2S(
            I2S_ID,
            sck=Pin(SCK_PIN),
            ws=Pin(WS_PIN),
            sd=Pin(SD_PIN),
            mode=I2S.RX,
            bits=16,  # WAV_SAMPLE_SIZE_IN_BITS,
            format=I2S.MONO,
            rate=sr,
            ibuf=BUFFER_LENGTH_IN_BYTES,
        )
        if initdelay:
            time.sleep(initdelay)
        if verbose:
            print(f"    i2s:{audio_in}")

    nread = audio_in.readinto(bfr_mv)
    if deinit:
        audio_in.deinit()
        audio_in = None
    #   dout = array.array("h", bfr_mv[:nread])
    gc.collect()
    try:
        dout = struct.unpack(f"{enc}{nread//2}h", bfr_mv[:nread])
    except MemoryError:
        gc.collect()
        print("low on memory")
        dout = None
    # print(dout)
    wavhdr = wavtool.create_wav_header(sr, 16, 1, nsamp)
    wavtool.writewav(bfr[:nread], wavhdr, filename)
    gc.collect()
    if verbose:
        print(f"audiograb.grabmono: file={filename}")
        print(f"    nsamp={nsamp}   samprate={sr}     initdelay={initdelay}")
        print(f"    bytes read={nread}")
    return dout, bfr[:nread], audio_in


def grabstereo(
    nsamp=20000,
    enc="<",
    sr=16000,
    filename="testit.wav",
    deinit=True,
    audio_in=None,
    initdelay=None,
    verbose=False,
):
    #    import array
    import struct

    gc.collect()
    bfr = bytearray(nsamp * 4)
    bfr_mv = memoryview(bfr)
    if not audio_in:
        audio_in = I2S(
            I2S_ID,
            sck=Pin(SCK_PIN),
            ws=Pin(WS_PIN),
            sd=Pin(SD_PIN),
            mode=I2S.RX,
            bits=16,  # WAV_SAMPLE_SIZE_IN_BITS,
            format=I2S.STEREO,
            rate=sr,
            ibuf=BUFFER_LENGTH_IN_BYTES,
        )
        if initdelay:
            time.sleep(initdelay)
        if verbose:
            print(f"    i2s:{audio_in}")

    nread = audio_in.readinto(bfr_mv)
    if deinit:
        audio_in.deinit()
        audio_in = None
    #   dout = array.array("h", bfr_mv[:nread])
    gc.collect()
    try:
        dout = struct.unpack(f"{enc}{nread//2}h", bfr_mv[:nread])
    except MemoryError:
        gc.collect()
        print("low on memory")
        dout = None
    # print(dout)
    wavhdr = wavtool.create_wav_header(sr, 16, 2, nsamp)
    wavtool.writewav(bfr[:nread], wavhdr, filename)
    gc.collect()
    if verbose:
        print(f"audiograb.grabsterei: file={filename}")
        print(f"    nsamp={nsamp}   samprate={sr}     initdelay={initdelay}")
        print(f"    bytes read={nread}")
    return dout, bfr[:nread], audio_in
