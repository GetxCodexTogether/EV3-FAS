#!/usr/bin/env python3
from Linienfolger.motor import*
from Linienfolger.sensor import*

from time import sleep

from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

# TODO: Add code here
print("Start World")
# driveonlyleft(70,4)
driveforever()
while(1):
    outleftmotor()
    print("jaa")
    
# while(1):
#     drivebothrot(10,10,0.2)




# sound = Sound()
# sound.speak('Welcome to the E V 3 dev project!')



# print("Ende World1")
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
# fib(1000)
# print("Hello World")