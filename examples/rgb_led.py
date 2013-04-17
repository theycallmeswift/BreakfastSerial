#! /usr/bin/env python
"""
This is an example that demonstrates how to use an
RGB led with BreakfastSerial.  It assumes you have an
RGB led wired up with red on pin 10, green on pin 9,
and blue on pin 8.
"""
from BreakfastSerial import RGBLed, Arduino
from time import sleep

board = Arduino()
led = RGBLed(board, { "red": 10, "green": 9, "blue": 8 })

# Red (R: on, G: off, B: off)
led.red()
sleep(1)

# Green (R: off, G: on, B: off)
led.green()
sleep(1)

# Blue (R: off, G: off, B: on)
led.blue()
sleep(1)

# Yellow (R: on, G: on, B: off)
led.yellow()
sleep(1)

# Cyan (R: off, G: on, B: on)
led.cyan()
sleep(1)

# Purple (R: on, G: off, B: on)
led.purple()
sleep(1)

# White (R: on, G: on, B: on)
led.white()
sleep(1)

# Off (R: off, G: off, B: off)
led.off()

# Run an interactive shell so you can play (not required)
import code
code.InteractiveConsole(locals=globals()).interact()
