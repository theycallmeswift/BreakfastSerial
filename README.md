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

