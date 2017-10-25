# Ecuadorean Bottle Recognition
This repositorty contains a Python interface to make a Nano Pi M1 show a GUI to take pictures from a webcam, control a servo and communicate with a REST API to take decisions based on that response.
This is part of my thesis project. The baseline is to use Convolutional Neural Networks in object recognition to determine the class of one out of ten classes of bottles. This repository contains the code to make the controller on the machine that takes pictures work. It's job is to take the picture, send it to the recognition server and with it's response determine if it should accept the bottle or not. Server can be found on <link to server code>

## Libraries used

This proyect is built using Python 3

I'll try to keep this space updated with the libraries that I will be using on this interface.

1. [Tkinter](https://wiki.python.org/moin/TkInter) - This library normally comes with python distributions
2. [FirendlyARM's WiringNP](https://github.com/friendlyarm/WiringNP/tree/nanopi-m1) - This library is built on C++. I controll it throuhg [Python's Subprocess Module](https://docs.python.org/3/library/subprocess.html#module-subprocess)
3. [Open CV](https://pypi.python.org/pypi/opencv-python) - Using this through it's python interface to take the picture and resize it.
4. [Request](http://www.python-requests.org/en/latest/) and [Json](https://docs.python.org/2/library/json.html) - This ones handle communication with the REST API.
