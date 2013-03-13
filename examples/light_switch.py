#! /usr/bin/env python
"""
This is an example that demonstrates how to use a
button to control an led with BreakfastSerial. It
assumes you have an button wired up to pin 8 and an
led wired to pin 13.
"""
from BreakfastSerial import Arduino, Led, Button

board = Arduino()
button = Button(board, 8)
led = Led(board, 13)

button.down(led.toggle)

# Run an interactive shell so you can play (not required)
import code
code.InteractiveConsole(locals=globals()).interact()
