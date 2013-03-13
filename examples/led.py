#! /usr/bin/env python
"""
This is an example that demonstrates how to blink an
led using breakfast_serial.  It assumes you have an
led wired up to pin 13.
"""
from breakfast_serial import Led, Arduino

board = Arduino()
led = Led(board, 13)

led.blink(200)

# Run an interactive shell so you can play (not required)
import code
code.InteractiveConsole(locals=globals()).interact()
