#! /usr/bin/env python
"""
This is an example that demonstrates how to use a
photoresistor to control a buzzer (piezo element)
using BreakfastSerial.  It assumes you have an
photoresistor (or some equivalent analog input) 
wired up to pin A0 and a buzzer on pin 8.
"""
from BreakfastSerial import Arduino, Buzzer, Sensor, setInterval
from time import sleep

board = Arduino()
buzzer = Buzzer(board, "8")
sensor = Sensor(board, "A0")

def loop():
  value = sensor.value or 1 # value is initially None
  value = value / 2

  buzzer.on()
  sleep(value)
  buzzer.off()
  sleep(value)

setInterval(loop, 0)

# Run an interactive shell so you can play (not required)
import code
code.InteractiveConsole(locals=globals()).interact()
