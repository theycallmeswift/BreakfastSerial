#! /usr/bin/env python
"""
This is an example that demonstrates how to use a
servo with BreakfastSerial. It assumes you have a 
servo wired up to pin 10.
"""
from BreakfastSerial import Arduino, Servo
from time import sleep

board = Arduino()
servo = Servo(board,10)

servo.set_position(180)
sleep(2)
servo.move(-135)
sleep(2)
servo.center()
sleep(2)
servo.reset()

# Run an interactive shell so you can play (not required)
import code
code.InteractiveConsole(locals=globals()).interact()
