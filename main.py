#!/usr/bin/env python3
from time import sleep
#from ev3dev2.button import Button

from linefollower.linefollower import *
from server_on_ev3 import init,send
from sensor import *

#from linefollower.sensor import *
#from matplotlib.pyplot import mt
#import matplotlib.pylab as plt 
#import numpy as np

#motor_init()
#sensor_init()

# import matplotlib.pylab as plt 
# import math
# import numpy as np

# print("Hello World1")

# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

#import logging


# config logging
#logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

#logging.debug('Run robot, run!')

from ev3dev2.sound import Sound

spkr = Sound()

# Play 'bark.wav':


# Introduce yourself:
#spkr.set_volume(255)
#spkr.speak('Hallo, ich heisse Roberto Ev und wurde von Simon und Laura programmiert')
#spkr.speak('Hello, i am Roberto Ev and i was programmed by Simon and Laura')

init()
print("Main-Loop")
sens_testMode()
#while True:
    #testMotor()

while 1:
    #light=sens_Color()
    light=sens_nxt_Color()
    line_5_RAW(light)
    #print(light)
    #straight(light)
    time=send(light)
    #landr(light, time)
    #liniepd_controller_mode2(light, time)
    #gyro=sens_Gyro()
    #timing(time)
