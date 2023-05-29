# KY-033

Código:

```python

#Beny Samuel Pantoja Reyes 19211703
# KY-033

from machine import Pin
import utime

sensor = Pin(18, Pin.IN)
utime.sleep(2)

while True:
# Se imprime un mensaje en función del valor del sensor
    if sensor.value() == 1:
        print("No detectada")
    else:
        print("Línea detectada")
    utime.sleep(0.5)

```

# Foto

![](KY033.jpg)
