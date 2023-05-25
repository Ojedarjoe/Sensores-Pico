#Beny Samuel Pantoja Reyes 19211703
# IR EMISSION

from ir_tx.nec import NEC
import utime

sensorIR = machine.Pin(17, machine.Pin.OUT)

nec = NEC(sensorIR)

while True:
    nec.transmit(0x0000, 0x09) #trasfiero este valor
    utime.sleep_ms(100)
