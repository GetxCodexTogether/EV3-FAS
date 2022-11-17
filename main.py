#!/usr/bin/env python3
<<<<<<< HEAD
from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep

lm = LargeMotor()

'''
This will run the large motor at 50% of its
rated maximum speed of 1050 deg/s.
50% x 1050 = 525 deg/s
'''
lm.on_for_seconds(speed = 50, seconds=3)
sleep(1)

'''
speed and seconds are both POSITIONAL
arguments which means
you don't have to include the parameter names as
long as you put the arguments in this order 
(speed then seconds) so this is the same as
the previous command:
'''
lm.on_for_seconds(50, 3)
sleep(1)

'''
This will run at 500 degrees per second (DPS).
You should be able to hear that the motor runs a
little slower than before.
'''
lm.on_for_seconds(speed=SpeedDPS(500), seconds=3)
sleep(1)

# 36000 degrees per minute (DPM) (rarely useful!)
lm.on_for_seconds(speed=SpeedDPM(36000), seconds=3)
sleep(1)

# 2 rotations per second (RPS)
lm.on_for_seconds(speed=SpeedRPS(2), seconds=3)
sleep(1)

# 100 rotations per minute(RPM)
lm.on_for_seconds(speed=SpeedRPM(100), seconds=3)
=======
from time import sleep
#from ev3dev2.button import Button

from linefollower.linefollower import *
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

print("Main-Loop")
while 1:
    liniep_controller()
    
>>>>>>> 727373bf98529acd799c9c61b8cda09fc25f69a3
