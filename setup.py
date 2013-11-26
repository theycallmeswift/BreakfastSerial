from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="BreakfastSerial",
    version="0.0.9",
    description="Python Framework for interacting with Arduino",
    author="Swift",
    author_email="theycallmeswift@gmail.com",
    packages=find_packages(),
    install_requires=['pyfirmata'],
    url="http://github.com/theycallmeswift/BreakfastSerial/",
    keywords=["arduino", "firmata"],
    long_description=readme()
)
