# Bibliothek Ev3dev for motors
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank

from time import sleep, time

from Linienfolger.sensor import currentColorvalue
# definition of the motors
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_B)
both = MoveTank(OUTPUT_A, OUTPUT_B)


# function to drive
def driveonlyleft (speedinpercent, rotation):
    left.on_for_rotations(SpeedPercent(speedinpercent), rotation)

def driveonlyright (speedinpercent, rotation):
    right.on_for_rotations(SpeedPercent(speedinpercent), rotation)

def drivebothtime (speedinpercentleft, speedinpercentright, time):
     both.on_for_seconds(SpeedPercent(speedinpercentleft), SpeedPercent(speedinpercentright), time)

def drivebothrot (speedinpercentleft, speedinpercentright, rotation):
    both.on_for_rotations(SpeedPercent(speedinpercentleft), SpeedPercent(speedinpercentright), rotation)

def driveforever ():
    left.speed_sp = 1000
    left.run_forever()

def outleftmotor():
    if(currentColorvalue()> 30):
        left.stop(stop_action="hold")
 
   
    
    
    


        
    
