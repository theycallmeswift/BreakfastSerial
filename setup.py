from setuptools import setup, find_packages

setup(
    name = "BreakfastSerial",
    version = "0.0.9",
    description = "Python Framework for interacting with Arduino",
    author = "Swift",
    author_email = "theycallmeswift@gmail.com",
    packages = find_packages(),
    install_requires=['pyfirmata'],
    url = "http://github.com/theycallmeswift/BreakfastSerial/",
    keywords = ["arduino","firmata"],
    long_description = """\
    Firmata based framework for interacting with Arduino
    ----------------------------

    DESCRIPTION
    BreakfastSerial makes it easy to interact with Arduino boards over serial by using
    the Firmata protocol.  See http://www.github.com/theycallmeswift/BreakfastSerial
    for more information.
    """ )
