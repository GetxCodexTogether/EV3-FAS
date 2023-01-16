#!/usr/bin/env python3
from linefollower.linefollower import *
from server_on_ev3 import init,send
from sensor import *
from motor import *

#from ev3dev2.sound import Sound
#spkr = Sound()
# Introduce yourself:
#spkr.set_volume(255)
#spkr.speak('Hallo, ich heisse Roberto Ev und wurde von Simon und Laura programmiert')
#spkr.speak('Hello, i am Roberto Ev and i was programmed by Simon and Laura')

init()
print("Main-Loop")
sensor_col_ev3_init()
motor_init()

while 1:
    sensor_col_value=sensor_col_ev3_value()
    time=send(sensor_col_value)
    linePID_controller(sensor_col_value, time)
   
    
    
    
