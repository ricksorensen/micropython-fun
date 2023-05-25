import serial
import time
import sys
import argparse


def doarguments(args):
    parser = argparse.ArgumentParser(
        description="Read serial from Arduino monitor (Uno)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "ofile",
        type=str,
        nargs="?",
        default=None,
        help="Output file name for collected strings",
    )
    parser.add_argument(
        "-b",
        "--baud",
        dest="baud",
        type=int,
        default=115200,
        help="Serial baud rate",
    )
    parser.add_argument(
        "-t",
        "--timelimit",
        dest="tlimit",
        type=int,
        default=120,
        help="Max time to collect data (in seconds)",
    )
    parser.add_argument(
        "-l",
        "--linelimit",
        dest="llimit",
        type=int,
        default=10000,
        help="Max number of lines",
    )
    parser.add_argument(
        "-e",
        "--echo",
        dest="doecho",
        action="store_true",
        help="enable echoing of received data",
    )
    parser.add_argument(
        "-D",
        "--debug",
        dest="debug",
        action="store_true",
        help="enable debug",
    )
    r = parser.parse_args(args)
    return r


def dump(db):
    for d in db:
        print(f"{d:02x},", end="")
    print()


def domain(args):
    r = doarguments(args)
    ser = serial.Serial("/dev/ttyACM0", timeout=5)
    time.sleep(5)  # wait for serial to connect
    n = 0
    # hdr = "#Start: baud={}  tlimit={}".format(r.baud, r.tlimit)
    hdr = f"#Start: baud={r.baud}  tlimit={r.tlimit}"
    print(hdr)
    print(ser)
    ser.reset_input_buffer()
    ts = time.time()
    dt = 0.0
    while (dt < r.tlimit) and (n < r.llimit):
        try:
            ser_bytes = ser.read(12)
            dump(ser_bytes)
            dt = time.time() - ts
            n = n + 1
        except Exception as e:
            print(e)
    print("#Done")


if __name__ == "__main__":
    domain(sys.argv[1:])
