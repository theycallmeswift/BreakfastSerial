#! /usr/bin/env python
"""
This is an example that demonstrates how to use a
a DC Motor with BreakfastSerial. It assumes you have 
a motor wired up to PWM pin 9.  Expected behavior is:

0 Seconds: Turn on motor to 80% speed
3 Seconds: Set speed to 50%
6 Seconds: Turn off motor
"""
from BreakfastSerial import Arduino, Motor
from time import sleep

board = Arduino()
motor = Motor(board, 9)

motor.start(80)
sleep(3)
motor.speed = 50
sleep(3)
motor.stop()

# Run an interactive shell so you can play (not required)
import code
code.InteractiveConsole(locals=globals()).interact()
