from breakfast_serial import Arduino
from util import EventEmitter, setInterval
import pyfirmata

class ArduinoNotSuppliedException(Exception):
  pass

class Sensor(EventEmitter):

  def __init__(self, board, pin):
    if not board:
      raise ArduinoNotSuppliedException

    super(Sensor, self).__init__()

    self._board = board
    self._pin = self._board.digital[pin]

class InputSensor(Sensor):

  def __init__(self, board, pin):
    super(InputSensor, self).__init__(board, pin)

    self._pin.mode = pyfirmata.INPUT
    self._pin.enable_reporting()
    self._old_value = self._pin.value

    self._board.on('data', self._update_old_value)

  def _update_old_value(self):
    value = self._pin.value

    if self._old_value != value:
      self._old_value = value
      self._handle_state_change()

  def _handle_state_change(self): pass

class Led(Sensor):

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
    self._interval = setInterval(self.toggle, millis)

class Button(InputSensor):

  def _handle_state_change(self):
    if self._pin.value == False:
      self.emit('up')
    else:
      self.emit('down')

  def down(self, cb):
    self.on('down', cb)

  def up(self, cb):
    self.on('up', cb)
