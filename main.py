#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

# TODO: Add code here
print("Start World")
m = LargeMotor(OUTPUT_A)
m.on_for_rotations(SpeedPercent(75), 5)
sound = Sound()
sound.speak('Welcome to the E V 3 dev project!')

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)

#drive in a turn for 5 rotations of the outer motor
#the first two parameters can be unit classes or percentages.
tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(75), 10)

#drive in a different turn for 3 seconds
tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 3)


print("Ende World1")
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
print("Hello World")