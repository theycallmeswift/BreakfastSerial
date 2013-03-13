# breakfast_serial

A Firmata based framework for interacting with Arduinos over serial.

## Arduino Setup

In order to use breakfast_serial, you need to have an arduino running the
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
pip install breakfast_serial
```

#### From Source

``` bash
git clone git://github.com/theycallmeswift/breakfast_serial.git && cd breakfast_serial

python setup.py install
```

## Getting Started

The breakfast_serial library provides a simple abstraction for a number of
common components.  Make sure your arduino is plugged in and is running firmata.

### Board

If you create a `Board` object without any parameters, it will attempt to auto discover 
the serial port that the Arduino is attached to and connect automatically.  Optionally,
you can supply the path to a serial port (Ex. `"/dev/tty.usbmodem4111"`).

``` python
from breakfast_serial import Board
board = Arduino() # This will autodiscover the device
```

### Blink an LED

To use the led object, import Led from `breakfast_serial`.  The constructor takes an
Arduino object and a pin number as its arguments.

``` python
from breakfast_serial import Arduino, Led
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
from breakfast_serial import Button, Arduino

board = Arduino()
button = Button(board, 8)

def down_cb():
  print "button down"

def up_cb():
  print "button up"

button.down(down_cb)
button.up(up_cb)
```

The `down` and `up` functions are just nice wrappers around the underlying event emitter.  The `Button`
component emits the following events:

 - `down` - The button is pressed
 - `up` - The button is not being pressed
 
### Read a sensor
 
The `Sensor` component let's us read in data from a sensor (analog or digital).  The constructor takes in
an Arduino object and a pin number.
 
``` python
from breakfast_serial import Arduino, Sensor
from time import sleep

board = Arduino()
sensor = Sensor(board, "A0")

for i in range(40):
  print sensor.value
  sleep(0.5)
```

The `value` property of a `Sensor` object is the value of the underlying pin.

### Moar!

There are a bunch of examples in the `examples/` folder.  Additional components
will be added over time, so be sure to check back regularly.
