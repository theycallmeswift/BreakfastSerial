import threading
from time import sleep

class EventEmitter(object):

  def __init__(self, *args, **kwargs):
    self._observers = {}

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

def debounce(wait):
  """ Decorator that will postpone a functions
      execution until after wait seconds
      have elapsed since the last time it was invoked. """
  def decorator(fn):
    def debounced(*args, **kwargs):
      def call_it():
        fn(*args, **kwargs)
      try:
        debounced.t.cancel()
      except(AttributeError):
        pass
      debounced.t = threading.Timer(wait, call_it)
      debounced.t.start()
    return debounced
  return decorator

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
    while self.shouldRun:
      self.func()
      sleep(self.seconds)

  def clear(self):
    self.shouldRun = False
