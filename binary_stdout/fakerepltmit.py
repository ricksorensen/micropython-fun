import sys
import time


def send(d):
    sys.stdout.write(bytes(d))


#    sys.stdout.write(bytes(d))


n = 0
dh = [0x41, 0x42, 0x43, 0x44]
ds = [0x00, 0x00, 0x61, 0x62, 0x63, 0x64]
df = [0xFE, 0xFF]

while True:
    ds[0] = (n >> 8) & 0xFF
    ds[1] = n & 0xFF
    n = (n + 1) & 0xFFFF
    send(dh)
    send(ds)
    send(df)
    time.sleep(1.0)
