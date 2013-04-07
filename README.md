# BreakfastSerial

A Firmata based framework for interacting with Arduinos over serial.

## Arduino Setup

In order to use BreakfastSerial, you need to have an arduino running the
standard firmata.

1. Download the Arduino IDE from the arduino website
  - [OSX](http://arduino.googlecode.com/files/arduino-1.0-macosx.zip)
  - [Linux 32 bit](http://arduino.googlecode.com/files/arduino-1.0-linux.tgz)
  - [Linux 64 bit](http://arduino.googlecode.com/files/arduino-1.0-linux64.tgz)
  - Windows support coming soon.
2. Plug in your Arduino or Arduino compatible microcontroller via USB
3. Open the Arduino IDE, select: File > Examples > Firmata > StandardFirmata
4. Click the "Upload" button.

## Installation

Using PyPi

``` bash
pip install BreakfastSerial
```

#### From Source

``` bash
git clone git://github.com/theycallmeswift/BreakfastSerial.git && cd BreakfastSerial

python setup.py install
```

## Getting Started

The BreakfastSerial library provides a simple abstraction for a number of
common components.  Make sure your arduino is plugged in and is running firmata.

### Arduino

If you create a `Arduino` object without any parameters, it will attempt to auto discover 
the serial port that the Arduino is attached to and connect automatically.  Optionally,
you can supply the path to a serial port (Ex. `"/dev/tty.usbmodem4111"`).

``` python
from BreakfastSerial import Arduino
board = Arduino() # This will autodiscover the device
```

### Blink an LED

To use the led object, import Led from `BreakfastSerial`.  The constructor takes an
Arduino object and a pin number as its arguments.

``` python
from BreakfastSerial import Arduino, Led
from time import sleep

board = Arduino()
pin = 13
led = Led(board, pin)

led.on()
sleep(2)
led.off()
sleep(2)
```

You can also use the `blink` method and pass it a number of milliseconds to automate the blinking process

``` python
millis = 200
led.blink(millis)
```

### Push a button

The `Button` component has a number of helper methods that make it easy to work with buttons.
The constructor takes an Arduino object and a pin number as its arguments.

``` python
from BreakfastSerial import Button, Arduino

board = Arduino()
button = Button(board, 8)

def down_cb():
  print "button down"

def up_cb():
  print "button up"

def hold_cb():
  print "button held"

button.down(down_cb)
button.up(up_cb)
button.hold(hold_cb)
```

The `down` and `up` functions are just nice wrappers around the underlying event emitter.  The `Button`
component emits the following events:

 - `change` - The button value changed
 - `down` - The button is pressed
 - `up` - The button is not being pressed
 - `hold` - The button was held for at least 1 second
 
### Read a sensor
 
The `Sensor` component let's us read in data from a sensor (analog or digital).  The constructor takes in
an Arduino object and a pin number.
 
``` python
from BreakfastSerial import Arduino, Sensor
from time import sleep

board = Arduino()
sensor = Sensor(board, "A0")

for i in range(40):
  print sensor.value
  sleep(0.5)
```

The `value` property of a `Sensor` object is the value of the underlying pin.

### Control a servo
 
The `Servo` component let's us control a servo.  The constructor takes in
an Arduino object and a pin number.
 
``` python
from BreakfastSerial import Arduino, Servo
from time import sleep

board = Arduino()
servo = Servo(board, "10")

servo.set_position(180)
sleep(2)
servo.move(-135)
sleep(2)
servo.center()
sleep(2)
servo.reset()
```

The `value` property of a `Servo` object is the current position of the servo in degrees

### Moar!

There are a bunch of examples in the `examples/` folder.  Additional components
will be added over time, so be sure to check back regularly.
