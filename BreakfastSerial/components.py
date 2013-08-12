from BreakfastSerial import Arduino
from util import EventEmitter, setInterval, debounce
import pyfirmata, re, threading

class ArduinoNotSuppliedException(Exception):
  pass

class ServoOutOfRangeException(Exception):
  pass

class InvalidPercentageException(Exception):
  pass

class Component(EventEmitter):

  def __init__(self, board, pin):
    if not board:
      raise ArduinoNotSuppliedException

    super(Component, self).__init__()

    self._board = board

    analog_regex = re.compile('A(\d)')
    match = analog_regex.match(str(pin))

    if match:
      self._pin = self._board.analog[int(match.group(1))]
    else:
      self._pin = self._board.digital[int(pin)]

  @property
  def value(self): return self._pin.value

class Sensor(Component):

  def __init__(self, board, pin):
    super(Sensor, self).__init__(board, pin)

    self.threshold = 0.01

    self._pin.mode = pyfirmata.INPUT
    self._pin.enable_reporting()

    self._old_value = self.value
    self._board.on('data', self._handle_data)

  def _handle_data(self):
    value = self.value or 0
    high_value = value + self.threshold
    low_value = value - self.threshold

    if self._old_value < low_value or self._old_value > high_value:
      self._old_value = value
      self._handle_state_changed()

  @debounce(0.005)
  def _handle_state_changed(self):
    self.emit('change')

  def change(self, cb):
    self.on('change', cb)

class Led(Component):

  def __init__(self, board, pin):
    super(Led, self).__init__(board, pin)
    self._isOn = False
    self._interval = None

  def on(self):
    self._pin.write(1)
    self._isOn = True
    return self

  def off(self, clear=True):
    self._pin.write(0)
    self._isOn = False

    if self._interval and clear:
      self._interval.clear()

    return self

  def toggle(self):
    if self._isOn:
      return self.off(clear=False)
    else:
      return self.on()

  def blink(self, millis):
    if self._interval:
      self._interval.clear()

    self._interval = setInterval(self.toggle, millis)

  def brightness(self, value):
    if int(value) > 100 or int(value) < 0:
      raise InvalidPercentageException

    if self._pin.mode != pyfirmata.PWM:
      self._pin.mode = pyfirmata.PWM

    _new_value = value / 100.0

    if _new_value == 0:
      self._isOn = False
    else:
      self.isOn = True

    self._pin.write(_new_value)
    return self

class RGBLed(EventEmitter):

  def __init__(self, board, pins):
    if not board:
      raise ArduinoNotSuppliedException

    # TODO: Check that pins is dict

    super(RGBLed, self).__init__()

    self._red = Led(board, pins["red"])
    self._green = Led(board, pins["green"])
    self._blue = Led(board, pins["blue"])

  def off(self):
    self._red.off(); self._green.off(); self._blue.off()
    return self

  def red(self):
    self._red.on(); self._green.off(); self._blue.off()
    return self

  def green(self):
    self._red.off(); self._green.on(); self._blue.off()
    return self

  def blue(self):
    self._red.off(); self._green.off(); self._blue.on()
    return self

  def yellow(self):
    self._red.on(); self._green.on(); self._blue.off()
    return self

  def cyan(self):
    self._red.off(); self._green.on(); self._blue.on()
    return self

  def purple(self):
    self._red.on(); self._green.off(); self._blue.on()
    return self

  def white(self):
    self._red.on(); self._green.on(); self._blue.on()
    return self

class Buzzer(Led):
  pass

class Button(Sensor):

  def __init__(self, board, pin):
    super(Button, self).__init__(board, pin)
    self._old_value = False
    self._timeout = None

    self.change(self._emit_button_events)

  def _handle_data(self):
    value = self.value

    if self._old_value != value:
      self._old_value = value
      # This sucks, wish I could just call Super
      self._handle_state_changed()

  def _emit_button_events(self):
    if self.value == False:
      if(self._timeout):
        self._timeout.cancel()

      self.emit('up')
    elif self.value == True:
      def emit_hold():
        self.emit('hold')

      self._timeout = threading.Timer(1, emit_hold)
      self._timeout.start()

      self.emit('down')

  def down(self, cb):
    self.on('down', cb)

  def up(self, cb):
    self.on('up', cb)

  def hold(self, cb):
    self.on('hold', cb)

class Servo(Component):

  def __init__(self, board, pin):
    super(Servo, self).__init__(board, pin)
    self._pin.mode = pyfirmata.SERVO

  def set_position(self, degrees):
    if int(degrees) > 180 or int(degrees) < 0:
      raise ServoOutOfRangeException
    self._pin.write(degrees)

  def move(self, degrees):
    self.set_position(self.value + int(degrees))

  def center(self):
    self.set_position(90)

  def reset(self):
    self.set_position(0)

class Motor(Component):

  def __init__(self, board, pin):
    super(Motor, self).__init__(board, pin)
    self._speed = 0
    self._pin.mode = pyfirmata.PWM

  def start(self, speed=50):
    self.speed = speed

  def stop(self):
    self.speed = 0

  @property
  def speed(self):
    return self._speed

  @speed.setter
  def speed(self, speed):
    if int(speed) > 100 or int(speed) < 0:
      raise InvalidPercentageException

    self._speed = speed
    self._pin.write(speed / 100.0)
    self.emit('change', speed)
