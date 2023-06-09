#Beny Samuel Pantoja Reyes 19211703
# IR RECEIVER

import time
from machine import Pin
from ir_rx import NEC_16

def callback(data, addr, ctrl):
    if data > 0:  # NEC protocol sends repeat codes.
        print('Data {:02x} Addr {:04x}'.format(data, addr))

ir = NEC_16(Pin(18, Pin.IN), callback)
