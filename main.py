#!/usr/bin/env python3
from time import sleep
from ev3dev2.button import Button

from linefollower.motor import *
from linefollower.sensor import *
#from matplotlib.pyplot import mt
#import matplotlib.pylab as plt 
#import numpy as np

#motor_init()
sensor_init()

# import matplotlib.pylab as plt 
# import math
# import numpy as np

# print("Hello World1")

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

import logging


# config logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

logging.debug('Run robot, run!')

print("Main-Loop")
while 1:
    linie(current_color_value())
    