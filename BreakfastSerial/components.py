from BreakfastSerial import Arduino
from util import EventEmitter, setInterval, debounce
import pyfirmata, re, threading

class ArduinoNotSuppliedException(Exception):
  pass

class ServoOutOfRangeException(Exception):
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

    self._pin.mode = pyfirmata.INPUT
    self._pin.enable_reporting()

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

class Buzzer(Led):
  pass

class Button(Sensor):

  def __init__(self, board, pin):
    super(Button, self).__init__(board, pin)
    self._old_value = self.value
    self._timeout = None

    self._board.on('data', self._handle_data)

  def _handle_data(self):
    value = self.value

    if self._old_value != value:
      self._old_value = value
      self._handle_state_changed()

  @debounce(0.005)
  def _handle_state_changed(self):
    self.emit('change')
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
