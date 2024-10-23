import holiday
import everyday
import mqttquick
import halloween
import runleds
import time
import os
import gc
import config
import machine


try:
    import esp32

    def check_sleep(pix, dosleep=0.25, start=None, stop=23, everydayu=None):
        dsleept = dosleep if dosleep is not None else 0.25
        dt = holiday.rjslocaltime(tzoff=-6)  # time.localtime()
        hrsleep = int(dsleept * 3600 * 1000)
        hrnow = dt[3] + (dt[4] / 60)
        stime = mqttquick.getstart_time(start)
        print(f" {dt}.   DS {stime}")
        if hrnow < stime:
            hrsleep = int(min(dsleept, stime - hrnow) * 3600 * 1000)
        elif hrnow < stop:  # assumes stop not past midnight
            hrsleep = 0
        temp = None
        if pix is not None:
            pix.fill((0, 0, 0))
            if everydayu is not None:
                c, temp = everydayu.getTempColor(b=0.3)
                print("Setting day temp  ", c)
                lp = len(pix) - 60
                for i in range(lp, len(pix)):
                    pix[i] = c
            else:
                print("no everydayu passed")
            if hrsleep > 0:
                pix.write()
        if (dosleep is not None) and (hrsleep > 0):
            print(f"deepsleep active {hrsleep} {temp}")
            mqttquick.msgalert(hrsleep, hrnow, temp=temp, addtopic="x")
            time.sleep(0.2)
            machine.deepsleep(hrsleep)
        else:
            print(f"deepsleep request {dosleep} {hrsleep} {temp}")
            return hrsleep

    # esp32.RMT.bitstream_channel(0)  # default is 1
    # esp32.RMT.bitstream_channel(None)  # use bitbanging
    haveTemp = True
except ImportError:
    haveTemp = False

    def check_sleep(pix, dosleep=False, start=None, stop=23, everydayu=None):
        return 0


if config._USE_NETWORK:
    import netconnect
    import ntptime


endstat = []


def start(interruptStart=True, delayStart=0, force_date=None, fixtemp=None):
    if interruptStart:
        print("time start up interrupt")
        time.sleep(60)
    allokay = True
    if config._USE_NETWORK:
        print("starting webrepl ", config._IP_ADDR)
        allokay = netconnect.dowrepl(myIP=config._IP_ADDR)
        # allokay = netconnect.doviperide(myIP=config._IP_ADDR)
        print("net status: ", allokay)
        while delayStart > 0 and os.dupterm(None) is None:
            print("wait for WebREPL connection")
            time.sleep(30)
            delayStart = delayStart - 1
    print("starting lights")
    print("initial memory ", gc.mem_free())
    if allokay:
        if force_date is None and config._USE_DATE is None:
            if config._USE_NETWORK:
                time.sleep(5)
                ntptime.settime()
            dt = holiday.rjslocaltime(tzoff=-6)
        else:
            import machine

            r = machine.RTC()
            if force_date is None:
                force_date = config._USE_DATE
            r.datetime(
                (
                    force_date[0],
                    force_date[1],
                    force_date[2],
                    0,
                    0,
                    0,
                    0,
                    0,
                )
            )
            dt = time.localtime()
        print(dt)
        hardsleep = config._DEEPSLEEP  # should read from config.py
        stoptime = config._DSLEEP_STOP if hasattr(config, "_DSLEEP_STOP") else 23
        pix = runleds.test_setup(
            config._NUM_PIX, pin=config._NEOPIN, swaprgb=config._SWAPRGB
        )
        if haveTemp:
            tmcu = esp32.mcu_temperature()
            tmcu = esp32.mcu_temperature()
            print("temp ", tmcu)
        else:
            print("no temperature available")

        hanukkah = holiday.Hanukkah(
            pix,
            dur=config._HAN_DUR,
            nrandom=(
                (len(pix) // config._RANDOM_RATIO)
                if config._RANDOM_RATIO is not None
                else None
            ),
        )
        valentine = holiday.Valentine(
            pix,
            dur=config._HAN_DUR,
            nrandom=None,
        )
        stpats = holiday.SaintPatrick(
            pix,
            dur=config._HAN_DUR,
            nrandom=None,
        )
        christmas = holiday.Christmas(
            pix,
            dur=config._LONG_DUR,
            nrandom=(
                (len(pix) // config._RANDOM_RATIO)
                if config._RANDOM_RATIO is not None
                else None
            ),
        )
        birthday = holiday.Birthday(pix, dur=config._LONG_DUR)
        halloeve = halloween.Halloween(pix)
        fallback = everyday.Everyday(
            pix,
            dur=config._LONG_DUR,
            fixtemp=fixtemp,
            nrandom=(
                (len(pix) // config._RANDOM_RATIO)
                if config._RANDOM_RATIO is not None
                else None
            ),
        )
        if (
            check_sleep(
                pix,
                dosleep=hardsleep,
                start=config._DSLEEP_START,
                stop=stoptime,
                everydayu=fallback,
            )
            > 0
        ):
            time.sleep(10)
        print(" Allocate memory :", gc.mem_free())
        try:
            while True:
                didholiday = (
                    birthday.chkDate(dt=dt, run=True)
                    or hanukkah.chkDate(dt=dt, run=True)
                    or valentine.chkDate(dt=dt, run=True)
                    or christmas.chkDate(dt=dt, run=True)
                    or stpats.chkDate(dt=dt, run=True)
                    or halloeve.chkDate(dt=dt, run=True)
                    or fallback.run(
                        correct=config._TEMP_CORRECT,
                    )
                )
                print("free mem: ", gc.mem_free())
                if haveTemp:
                    print("temp: ", esp32.mcu_temperature())
                gc.collect()
                if (
                    check_sleep(
                        pix,
                        dosleep=hardsleep,
                        start=config._DSLEEP_START,
                        stop=stoptime,
                        everydayu=fallback,
                    )
                    > 0
                ):
                    time.sleep(10)
        except Exception as unexpected:
            import sys

            endstat.append("Unexpected Exception")
            endstat.append(unexpected)
            sys.print_exception(unexpected)
    else:
        print("Not All OKAY")
        endstat.append("Not ALL OKAY")
    return endstat
