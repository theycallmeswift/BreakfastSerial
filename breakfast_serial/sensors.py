from breakfast_serial import __board__
from util import setInterval

class Led(object):

  def __init__(self, pin):
    self._pin = __board__.digital[pin]
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
