from machine import Pin
import sys

print(sys.implementation._machine)
if hasattr(Pin, "board"):
    for p, n in Pin.board.__dict__.items():
        print("{:>10s}: {}".format(p, n))
else:
    print("Pin does not have board attribute with pin list")
