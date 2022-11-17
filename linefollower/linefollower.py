#Init Motor
from ev3dev2.motor import LargeMotor, OUTPUT_A,OUTPUT_B, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM,MoveTank,MoveSteering
#Init Sensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor

print("Motor/Sensor-Init")
SColor= ColorSensor()
MSteering = MoveSteering(left_motor_port=OUTPUT_A,right_motor_port=OUTPUT_B,motor_class=LargeMotor)
#MLeft = LargeMotor(OUTPUT_A)
#MRight = LargeMotor(OUTPUT_B)


def linie():
    current_Sensor_Val =SColor.reflected_light_intensity
    upperlimit = 35
    lowerlimit = 25
    full_white = 52
    full_black = 15
    if(lowerlimit <= current_Sensor_Val <= upperlimit):
        MSteering.on(speed=-50,steering=0)
    else:
        if(full_white<current_Sensor_Val):
            MSteering.on(speed = -30, steering= -80)
        elif(full_black > current_Sensor_Val):
            MSteering.on(speed = -30, steering= +80)
        elif(lowerlimit > current_Sensor_Val):
            MSteering.on(speed = -30, steering= 40)
        else:
            MSteering.on(speed = -30, steering= -40)

def liniep_controller():
   current_Sensor_Val = SColor.reflected_light_intensity
   kp=-2.8
   calibration= 30
   newsteering= kp* (current_Sensor_Val-calibration)
   if(newsteering>100):
        newsteering=100
   elif(newsteering<-100):
        newsteering=-100
   MSteering.on(speed=-50,steering=newsteering)

    

            
    
    
    


        
    
