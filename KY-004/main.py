
#Beny Samuel Pantoja Reyes 19211703
# Button

from machine import Pin
from time import sleep

push_button = Pin(14, Pin.IN)  # Pin 14 pal button

while True:
  logic_state = push_button.value()
  if logic_state == True:
      print("Presionado")
  else:
      print("No Presionado")