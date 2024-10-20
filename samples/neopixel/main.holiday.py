import os

if "nostart" not in os.listdir():
    import machine
    import startholiday as sh

    delaystart = 0
    if machine.reset_cause() != machine.DEEPSLEEP_RESET:
        delaystart = 6
    sh.start(delayStart=delaystart, interruptStart=False)
