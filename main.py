#!/usr/bin/env python3
#fileimport
"""Check Doxstring"""
from python.python import * 
from linefollower.motor import*
from linefollower.sensor import*
# Bibimport


from time import sleep #

testPy()


from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound


print("Start World")

motorstart()
while(1):
    outoflinemotor(currentColorvalue())
    print("jaa")
    







