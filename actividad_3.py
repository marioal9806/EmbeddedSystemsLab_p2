import time
from grovepi import *
from grove_rgb_lcd import *
import math

# Sensor A0
sensor = 0

# Port for buzzer
buzzer_pin = 2

# Port for button
button = 4

pinMode(buzzer_pin, "OUTPUT")
pinMode(button, "INPUT")

while True:
    try:
        button_status = digitalRead(button)
        if button_status:
            setRGB(0, 255, 0)
            curr_temp = temp(sensor, '1.1')
            setText(f"Temp = {curr_temp} C")
        else:
            setRGB(255, 0, 0)
            setText("Presiona el boton")
    except KeyboardInterrupt:
        break
    except (IOError, TypeError) as e:
        print("Error")