#!/usr/bin/env pybricks-micropython
from linefollower.linefollower import *
from server_on_ev3 import init,send
from sensor import *#
from motor import *
from pybricks.ev3devices import *

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
    motor_l_speed = motor_l_speed_get()
    motor_l_count_per_rote = motor_l_count_per_rote_get()
    time=send(sensor_col_value,motor_l_speed, motor_l_count_per_rote)
    susserArsch(time) 

   
    linePID_controller(sensor_col_value, time)
   
    
    
    
