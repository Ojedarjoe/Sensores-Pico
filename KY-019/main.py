#Beny Samuel Pantoja Reyes 19211703
# KY-019


import machine
import time


relay_pin = machine.Pin(7, machine.Pin.OUT) # Configura el pin del rele como salida

while True:
    relay_pin.on() # Enciende el rele
    print("Relé encendido")
    time.sleep(1) # Espera 1 segundo

    relay_pin.off() # Apaga el rele
    print("Relé apagado")
    time.sleep(1) # Espera 1 segundo