import machine

# Definir el pin GPIO
switch_pin = machine.Pin(2, machine.Pin.IN)

while True:
    if switch_pin.value() == 0:
        print("Interruptor presionado")
    else:
        print("Interruptor liberado")
