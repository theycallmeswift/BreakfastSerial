#! /usr/bin/env python
"""
This is an example that demonstrates how to blink an
led using breakfast_serial.  It assumes you have an
led wired up to pin 13.
"""
from breakfast_serial import Led

led = Led(13)
led.blink(200)

import code
code.InteractiveConsole(locals=globals()).interact()
