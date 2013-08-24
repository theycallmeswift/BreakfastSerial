#! /usr/bin/env python
"""
This is an example that demonstrates how to use a
potentiometer to change the blink speed of an LED
with BreakfastSerial.  It assumes you have a
potentiometer wired up to pin A0 and a LED on pin 13.
"""
from BreakfastSerial import Arduino, Sensor, Led
from time import sleep

board = Arduino()
sensor = Sensor(board, "A0")
led = Led(board, 13)

while True:
  led.on()
  sleep(sensor.value)
  led.off()
  sleep(sensor.value)
