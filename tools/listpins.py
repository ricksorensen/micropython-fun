from machine import Pin
import sys


def get_num_pins():
    n = 0
    for i in range(200):
        try:
            _ = Pin(i)
            n = i
        except ValueError:
            break
    return n + 1


n = get_num_pins()
print(sys.implementation._machine)
print("Number of pins: {}".format(n))
if hasattr(Pin, "board"):
    print("Number of named pins: {}".format(len(Pin.board.__dict__)))
    for p, n in Pin.board.__dict__.items():
        print("{:>10s}: {}".format(p, n))
else:
    print("Pin does not have board attribute with pin list")
