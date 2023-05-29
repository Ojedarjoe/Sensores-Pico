# KY-036 TOUCH

Código:

```python

#Beny Samuel Pantoja Reyes 19211703
# Touch

from machine import Pin, ADC
import utime

# Configurar el pin analógico
sensor_pin = ADC(26)

while True:
    # Leer el valor analógico del sensor
    sensor_value = sensor_pin.read_u16()

    # Imprimir el valor leído
    print("Valor del sensor:", sensor_value)

    # Esperar un segundo antes de la siguiente lectura
    utime.sleep(1)
```

# Foto

![](Touch.jpg)
