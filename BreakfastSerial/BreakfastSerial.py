import os, re, code, threading, pyfirmata
from time import sleep

def find_arduino():
  rport = re.compile('usb|acm', re.IGNORECASE)
  ports = filter(rport.search, os.listdir('/dev'))

  if len(ports) == 0:
    raise ArduinoNotFoundException

  print "Connecting to /dev/%s" % ports[0]
  return "/dev/%s" % ports[0]

class ArduinoNotFoundException(Exception):
  pass

class FirmataNotOnBoardException(Exception):
  pass

class Arduino(pyfirmata.Arduino):

  def __init__(self, *args, **kwargs):
    # If no port was supplied, auto detect the arduino
    if len(args) >= 1:
      super(Arduino, self).__init__(*args, **kwargs)
    else:
      newargs = (find_arduino(),)
      super(Arduino, self).__init__(*newargs)

    if not self.get_firmata_version():
      raise FirmataNotOnBoardException

    self._observers = {}

    # Register a new handler for digital messages so we can tell sensors to update
    self.add_cmd_handler(pyfirmata.DIGITAL_MESSAGE, self._handle_digital_message_interceptor)
    self.add_cmd_handler(pyfirmata.ANALOG_MESSAGE, self._handle_analog_message_interceptor)
    self._monitor = Monitor(self)

  def _handle_digital_message_interceptor(self, port_nr, lsb, msb):
    self._handle_digital_message(port_nr, lsb, msb)
    self.emit('data') # TODO: Make less generic

  def _handle_analog_message_interceptor(self, port_nr, lsb, msb):
    self._handle_analog_message(port_nr, lsb, msb)
    self.emit('data') # TODO: Make less generic

  # TODO: Make generic eventemitter class and inherit
  def on(self, event, cb):
    if event not in self._observers:
      self._observers[event] = [cb,]
    else:
      if cb not in self._observers[event]:
        self._observers[event].append(cb)
      else:
        raise ValueError("Observer is already registered to event: ", event)

  def off(self, event, cb):
    if event not in self._observers:
      raise KeyError("No observers are registered for the event: ", event)
    else:
      if cb not in self._observers[event]:
        raise ValueError("Observer is not registered for the event: ", event)
      else:
        self._observers[event].remove(cb)

  def emit(self, event, *args):
    if event in self._observers:
      for observer in self._observers[event]:
        observer(*args)

class Monitor(threading.Thread):

  def __init__(self, board):
    threading.Thread.__init__(self)

    self.board = board
    self._shouldContinue = True

    self.setDaemon(True)
    self.start()

  def run(self):
    while 1:
      while self.board.bytes_available():
        self.board.iterate()

      sleep(0.004)

      if not self._shouldContinue:
        break

  def stop(self):
    self._shouldContinue = False
