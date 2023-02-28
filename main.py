#!/usr/bin/env python3
from linefollower.linefollower import *
from server_on_ev3 import init,send
from sensor import *
from motor import *

from ev3dev2.stopwatch import StopWatch
my_stopwatch = StopWatch()

from ev3dev2.sensor.lego import InfraredSensor
#from ev3dev2.sound import Sound
#spkr = Sound()
# Introduce yourself:
#spkr.set_volume(255)
#spkr.speak('Hallo, ich heisse Roberto Ev und wurde von Simon und Laura programmiert')
#spkr.speak('Hello, i am Roberto Ev and i was programmed by Simon and Laura')

ir = InfraredSensor()

init()
print("Main-Loop")
sensor_col_ev3_init()
motor_init()
my_stopwatch.start()
#i_controller =0
while 1:
    sensor_col_value= ir.proximity
    time = send(sensor_col_value)
    #motor_r_speed = motor_r_speed_get()
    #motor_l_count_per_rote = motor_l_count_per_rote_get()
    #time=send(sensor_col_value,motor_r_speed)
    #time=send(sensor_col_value)
    #print(time)
    #i_controller=liniepid_control_notime(sensor_col_value)
    #susserArsch(time) 
    #liniepid_control_test(sensor_col_value)
    #linePID_controller(sensor_col_value, time)
    #liniepid_control_withtimetest(sensor_col_value,time)
    #liniepid_control_notime(sensor_col_value)
    #print(my_stopwatch.value_secs)
    # i=0
    # while(i<560):
    #     i+=1
    #print(sensor_col_value)
    #print(sensor_col_value)
    #lineP_controller(sensor_col_value)
    
    
    
    
