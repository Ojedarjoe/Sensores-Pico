# KY-017 Tilt Switch

Código:

```python

#Beny Samuel Pantoja Reyes 19211703
# Tilt Switch

from machine import Pin

# Configurar el pin del interruptor
switch_pin = Pin(14, Pin.IN)

while True:
    # Leer el estado del interruptor
    switch_state = switch_pin.value()

    if switch_state == 0:
        print("Interruptor activado")
    else:
        print("Interruptor desactivado")

```

# Foto

![](TSwitch.jpg)
