from holiday import Holiday
import runleds
import colorsupport
import onewire
import ds18x20
import esp32
import config
import machine


def get_temp(tmin, tmax, correct=0, tempsens=None):
    extt = None
    tmcu = min(max(esp32.mcu_temperature() - correct, tmin), tmax)
    if tempsens is not None:
        import time

        tempsens[0].convert_temp()
        time.sleep_ms(750)
        extt = min(max(tempsens[0].read_temp(tempsens[1]), tmin), tmax)
    return (extt, tmcu)


def mapRange(value, inMin, inMax, outMin, outMax):
    return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))


# fade saturation for hsv0 from 1 to 0, fixed brightness (value)
def fadeHue(h, nstep=10, b=0.25, swaprg=True, reverse=True):
    fwd = []
    for i in range(nstep):
        np = colorsupport.colorHSVfloat(h / 360, (1 - i / nstep), b)
        fwd.append(np)
    alld = []
    for x in fwd:
        if swaprg:
            alld.extend([x[1], x[0], x[2]])
        else:
            alld.extend(x)
    if reverse:
        bkwd = fwd.copy()
        bkwd.reverse()

        for x in bkwd:
            if swaprg:
                alld.extend([x[1], x[0], x[2]])
            else:
                alld.extend(x)
    return bytearray(alld)


class Everyday(Holiday):
    def __init__(self, pix, *, dur=100, nrandom=None, bright=0.1, sf=None):
        self.data = None
        self.tmin = -5
        self.tmax = 35
        self.tempsens = None
        try:
            temppin = config._TEMP_PIN
            tsens = ds18x20.DS18X20(onewire.OneWire(machine.Pin(temppin)))
            rs = tsens.scan()
            if len(rs) == 0:
                print("no tempsensor found")
                self.tempsens = None
            else:
                self.tempsens = (tsens, rs[0])
        except:
            self.tempsens = None
            print("exception while checking temp sensor")
        # if nrandom is None:
        #    nrandom = len(pix) // 3
        super().__init__(pix, dur=dur, nrandom=nrandom, bright=bright)

    def run(self, *, sf=None, choice=None, correct=0, swaprg=True):
        try:
            tout, tmcu = get_temp(self.tmin, self.tmax, correct, tempsens=self.tempsens)
            t = tout if tout is not None else tmcu
            # h = (168 - 4.8 * t)/360*65536
            temphue = mapRange(t, self.tmin, self.tmax, 220, 0)
            self.data = fadeHue(temphue, nstep=(len(self.pix) // 2 - 10), swaprg=swaprg)
            nrand = self.nrandom
        except ImportError:
            self.data = None
            t = None
            nrand = len(self.pix) // 3

        print("everyday t={}, texternal={}, tmcu={}+{}".format(t, tout, tmcu, correct))
        runleds.loop_led_time(
            self.pix,
            self.data,
            tdur_secs=self.dur,
            sclr=True,
            nrandom=nrand,
            bright=self.bright,
        )
        return t
