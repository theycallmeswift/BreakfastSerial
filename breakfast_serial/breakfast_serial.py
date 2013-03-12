import os, re, code
from pyfirmata import Arduino

class ArduinoNotFoundException(Exception):
  pass

class FirmataNotOnBoardException(Exception):
  pass

rport = re.compile('usb|acm')
ports = filter(rport.search, os.listdir('/dev'))

if len(ports) == 0:
  raise ArduinoNotFoundException

print "Connecting to /dev/%s" % ports[0]
__board__ = Arduino("/dev/%s" % ports[0])

if not __board__.get_firmata_version():
  raise FirmataNotOnBoardException
