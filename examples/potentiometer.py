#! /usr/bin/env python
"""
This is an example that demonstrates how to use a
potentiometer with BreakfastSerial.  It assumes you 
have an potentiometer wired up to pin A0.
"""
from BreakfastSerial import Sensor, Arduino

board = Arduino()
sensor = Sensor(board, "A0")

def print_value():
  print sensor.value

sensor.change(print_value)

# Run an interactive shell so you can play (not required)
import code
code.InteractiveConsole(locals=globals()).interact()

