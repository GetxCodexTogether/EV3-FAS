from ev3dev2.motor import LargeMotor, OUTPUT_A,OUTPUT_B, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM,MoveTank,MoveSteering

#def motor_init():
print("Motor-Init")
MLeft = LargeMotor(OUTPUT_A)
MRight = LargeMotor(OUTPUT_B)
MSteering = MoveSteering(left_motor_port=OUTPUT_A,right_motor_port=OUTPUT_B,motor_class=LargeMotor)

def linie(current_Sensor_Val):
    upperlimit = 35
    lowerlimit = 25
    full_white = 52
    full_black = 15
    if(lowerlimit <= current_Sensor_Val <= upperlimit):
        MSteering.on(speed=-30,steering=0)
    else:
        if(full_white<current_Sensor_Val):
            MSteering.on(speed = -30, steering= -80)
        elif(full_black > current_Sensor_Val):
            MSteering.on(speed = -30, steering= +80)
        elif(lowerlimit > current_Sensor_Val):
            MSteering.on(speed = -30, steering= 40)
        else:
            MSteering.on(speed = -30, steering= -40)


            
    
    
    


        
    
