#Jose Jaime Ojeda Rodriguez
import machine
import time

# Definir el pin ADC
adc_pin = machine.ADC(26)

while True:
    # Leer el valor analógico del sensor
    adc_value = adc_pin.read_u16()

    # Convertir el valor analógico a temperatura
    voltage = adc_value * 3.3 / 65535  # Convertir el valor a voltaje (0-3.3V)
    temperature = (voltage - 0.5) * 100  # Calcular la temperatura en grados Celsius

    # Mostrar la temperatura
    print("Temperatura: {:.2f} °C".format(temperature))

    # Esperar un segundo antes de leer nuevamente
    time.sleep(1)
