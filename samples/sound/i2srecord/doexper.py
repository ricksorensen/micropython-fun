import recordnf_16k as rec
import time


def doexper(filestart, rest):
    fnbase = f"{filestart}"
    ai2s = None
    print("Start run1.wav")
    ai2s = rec.doit(fnbase + "run1.wav", sampbfr=10000, deinit=True, audio_in=ai2s)
    time.sleep(rest)
    print("Start run2.wav")
    ai2s = rec.doit(fnbase + "run2.wav", sampbfr=10000, deinit=True, audio_in=ai2s)
    time.sleep(rest)
    print("Start run3.wav")
    ai2s = rec.doit(fnbase + "run3.wav", sampbfr=10000, deinit=False, audio_in=ai2s)
    time.sleep(rest)
    print("Start run4.wav")
    ai2s = rec.doit(fnbase + "run4.wav", sampbfr=10000, deinit=False, audio_in=ai2s)
    time.sleep(rest)
    print("Start ru51.wav")
    ai2s = rec.doit(fnbase + "run5.wav", sampbfr=10000, deinit=True, audio_in=ai2s)
    print("Finished")
