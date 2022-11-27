#Init Motor
from ev3dev2.motor import LargeMotor, OUTPUT_A,OUTPUT_B, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM,MoveTank,MoveSteering

error_old=0
integral=0

print("Motor/Sensor-Init")
MSteering = MoveSteering(left_motor_port=OUTPUT_A,right_motor_port=OUTPUT_B,motor_class=LargeMotor)
#MLeft = LargeMotor(OUTPUT_A)
#MRight = LargeMotor(OUTPUT_B)

def straight(current_Sensor_Val):
    MSteering.on(speed=-10,steering=0)



def linie_2(current_Sensor_Val):
    limit=33
    if(limit <= current_Sensor_Val):
        MSteering.on(speed=-30,steering=-40)
    elif(limit== current_Sensor_Val):
        MSteering.on(speed=-30,steering=0)
    else:
        MSteering.on(speed = -30, steering= 40)

def linie_3(current_Sensor_Val):
    upperlimit = 35
    lowerlimit = 20
    if(lowerlimit <= current_Sensor_Val <= upperlimit):
        MSteering.on(speed=-50,steering=0)
    elif(lowerlimit > current_Sensor_Val):
            MSteering.on(speed = -30, steering= 40)
    else:
            MSteering.on(speed = -30, steering= -40)

def linie_5(current_Sensor_Val):
    upperlimit = 35
    lowerlimit = 20
    full_white = 56
    full_black = 15
    speed_r = -50
    speed_n = -40
    speed_k = -30
    if(lowerlimit <= current_Sensor_Val <= upperlimit):
        MSteering.on(speed= speed_r,steering=0)
    else:
        if(full_white<current_Sensor_Val):
            MSteering.on(speed = speed_k, steering= -87)
        elif(full_black > current_Sensor_Val):
            MSteering.on(speed = speed_k, steering= +87)
        elif(lowerlimit > current_Sensor_Val):
            MSteering.on(speed = speed_n, steering= 40)
        else:
            MSteering.on(speed = speed_n, steering= -40)

def liniep_controller(current_Sensor_Val):
   kp=3.3
   calibration= 33
   newsteering= kp* (calibration-current_Sensor_Val)
   if(newsteering>100):
        newsteering=100
   elif(newsteering<-100):
        newsteering=-100
   MSteering.on(speed=-20,steering=newsteering)

    
def liniepd_controller(current_Sensor_Val):
   global error_old
   kp=2.91
   kd=0.96
   calibration= 30
   error=calibration-current_Sensor_Val
   differential= error - error_old
   error_old=error
   newsteering= kp* error+ kd*differential
   if(newsteering>100):
        newsteering=100
   elif(newsteering<-100):
        newsteering=-100
   MSteering.on(speed=-24,steering=newsteering)

    
def liniepid_controller(current_Sensor_Val):
   global error_old
   global integral
   kp=3.3
   kd=0.9
   ki= 0.2
   calibration= 30

   error=calibration-current_Sensor_Val

   differential= error - error_old

   integral= integral +error

   error_old=error
   newsteering= kp* error+ kd*differential+ ki*integral
   if(newsteering>100):
        newsteering=100
   elif(newsteering<-100):
        newsteering=-100
   MSteering.on(speed=-30,steering=newsteering)

    

            
    
    
    


        
    
