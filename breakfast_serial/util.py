import threading
from time import sleep

class setInterval(threading.Thread):

  def __init__(self, func, millis):
    threading.Thread.__init__(self)
    self.event = threading.Event()
    self.func = func
    self.seconds = millis / 1000.0
    self.shouldRun = True

    self.setDaemon(True)
    self.start()

  def run(self):
    self.func()
    sleep(self.seconds)

    if self.shouldRun:
      self.run()

  def clear(self):
    self.shouldRun = False
