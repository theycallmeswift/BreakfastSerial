#! /usr/bin/env python
"""
This is an example that demonstrates how to use a
potentiometer to fade an LED with BreakfastSerial.
It assumes you have an potentiometer wired up to
pin A0 and a LED on pin 9.
"""
from BreakfastSerial import Arduino, Sensor, Led

board = Arduino()
sensor = Sensor(board, "A0")
led = Led(board, 9)

def change_led_brightness():
  led.brightness(100 * sensor.value)

sensor.change(change_led_brightness)

# Run an interactive shell so you can play (not required)
import code
code.InteractiveConsole(locals=globals()).interact()
