#! /usr/bin/env python
"""
This is an example that demonstrates how to use
buttons to toggle an LED with BreakfastSerial. It
assumes you have and LED wired up to pin 13 and
two buttons wired up to pins 2 and 3.
"""
from BreakfastSerial import Button, Led, Arduino

board = Arduino()

led = Led(board, 13)
button1 = Button(board, 2)
button2 = Button(board, 3)

for button in [button1, button2]:
  button.up(led.toggle)
  button.down(led.toggle)

# Run an interactive shell so you can play (not required)
import code
code.InteractiveConsole(locals=globals()).interact()
