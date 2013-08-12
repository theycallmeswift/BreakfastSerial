#! /usr/bin/env python
"""
This is an example that demonstrates how to use a
button with BreakfastSerial.  It assumes you have an
button wired up to pin 8.
"""
from BreakfastSerial import Button, Arduino

board = Arduino()
button = Button(board, 8)

def down_cb():
  print "button down"

def up_cb():
  print "button up"

button.down(down_cb)
button.up(up_cb)

# Run an interactive shell so you can play (not required)
import code
code.InteractiveConsole(locals=globals()).interact()
