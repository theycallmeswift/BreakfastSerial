from breakfast_serial import __version__
from setuptools import setup, find_packages

with open('README.md') as f:
  long_description = f.read()

setup(
    name = "breakfast_serial",
    version = __version__,
    description = "Python Framework for interacting with Arduino",
    author = "Swift",
    author_email = "theycallmeswift@gmail.com",
    packages = find_packages(),
    install_requires=['pyfirmata'],
    url = "http://github.com/theycallmeswift/breakfast_serial/",
    keywords = ["arduino","firmata"],
    long_description = long_description )
