# breakfast_serial

breakfast_serial is a Firmata based framework for interacting with Arduinos over
serial.

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

## Usage

The breakfast_serial library provides a simple abstraction for a number of
common components.  Make sure your arduino is plugged in and is running firmata.

### LED

To use the led object, import Led from `breakfast_serial`.  The constructor takes a pin
number as its only argument.

``` python
from breakfast_serial import Led
    
pin = 13
led = Led(pin)
```

#### Turing an led on and off

Turning an led on or off is as simple as calling the `on` and `off` methods.

``` python
led.on()
sleep(1)
led.off()
```

If you don't already know the state or don't feel like keeping track of it, just use
the `toggle` method instead.

``` python
led.toggle()
```

#### Blinking an led

The blink method is a convenient method to strobe an led.  It takes one argument for the
blink frequency (in milliseconds).

``` python
millis = 200
led.blink(200)
```
