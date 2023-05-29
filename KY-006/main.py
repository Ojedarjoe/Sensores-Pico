#Beny Samuel Pantoja Reyes 19211703
# KY-006 Passive Buzzer

import machine
import utime

buzzer_pin = machine.Pin(0, machine.Pin.OUT)

def play_buzzer():
    buzzer_pin.on()
    utime.sleep_ms(500)
    buzzer_pin.off()
    utime.sleep_ms(500)

while True:
    play_buzzer()