# Bibliothek Ev3dev for motors
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank


# definition of the motors
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_B)

def motorstart():
    left.speed_sp = 100
    left.run_forever()
    right.speed_sp = 100
    right.run_forever()

def driveleft (speed):
    left.speed_sp = speed
    left.run_forever()

def driveright(speed):
    right.speed_sp = speed
    right.run_forever()

def outoflinemotor(currentcolor):
    print(currentcolor)
    if(currentcolor> 30):
        left.stop(stop_action="hold")
        driveleft(50)
    elif(currentcolor < 20):
        right.stop(stop_action="hold")
        driveright(50)
    else:
        motorstart()

 
   
    
    
    


        
    
