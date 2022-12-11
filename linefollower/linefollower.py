#Init Motor
from ev3dev2.motor import LargeMotor, OUTPUT_A,OUTPUT_B, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM,MoveTank,MoveSteering

error_old=0
integral=0
time_old=0

print("Motor/Sensor-Init")
MSteering2 = MoveSteering(left_motor_port=OUTPUT_A,right_motor_port=OUTPUT_B,motor_class=LargeMotor)
#MLeft = LargeMotor(OUTPUT_A)
#MRight = LargeMotor(OUTPUT_B)

def straight(current_Sensor_Val):
    MSteering2.on(speed=-10,steering=0)


def landr(current_Sensor_Val, time):
    if(time< 5):
        MSteering2.on(speed=-10,steering=0) 
    else:
        MSteering2.on(speed=-10,steering=50)
    
L = LargeMotor(OUTPUT_A)   
def testMotor():
    L.on(speed=100)
    
    #print(MSteering2)
    #attr=vars(MSteering2)
    #attr=vars(L)
    #print(', '.join("%s: %s" % item for item in attr.items()))
    #print(L.duty_cycle, L.count_per_rot, L.position,L.speed_sp,L._position_sp)
    #print(L.commands)
    print(L.count_per_rot,L.duty_cycle,L.position,L.speed,L.polarity,L.state)

#an = Animal()
#attrs = vars(an)
# {'kids': 0, 'name': 'Dog', 'color': 'Spotted', 'age': 10, 'legs': 2, 'smell': 'Alot'}
# now dump this in some way or another
#print(', '.join("%s: %s" % item for item in attrs.items()))

    
# zur initialisierung nötig
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank

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

# Funktionen aufrufen:
#driveonlyleft(70,4)
#drivebothrot(10,10,0.2)
    
    




def linie_2(current_Sensor_Val):
    limit=33
    if(limit <= current_Sensor_Val):
        MSteering2.on(speed=-30,steering=-40)
    elif(limit== current_Sensor_Val):
        MSteering2.on(speed=-30,steering=0)
    else:
        MSteering2.on(speed = -30, steering= 40)

def linie_3(current_Sensor_Val):
    upperlimit = 35
    lowerlimit = 20
    if(lowerlimit <= current_Sensor_Val <= upperlimit):
        MSteering2.on(speed=-50,steering=0)
    elif(lowerlimit > current_Sensor_Val):
            MSteering2.on(speed = -30, steering= 40)
    else:
            MSteering2.on(speed = -30, steering= -40)

def linie_5(current_Sensor_Val):
    upperlimit = 35
    lowerlimit = 20
    full_white = 56
    full_black = 15
    speed_r = -50
    speed_n = -40
    speed_k = -30
    if(lowerlimit <= current_Sensor_Val <= upperlimit):
        MSteering2.on(speed= speed_r,steering=0)
    else:
        if(full_white<current_Sensor_Val):
            MSteering2.on(speed = speed_k, steering= -87)
        elif(full_black > current_Sensor_Val):
            MSteering2.on(speed = speed_k, steering= +87)
        elif(lowerlimit > current_Sensor_Val):
            MSteering2.on(speed = speed_n, steering= 40)
        else:
            MSteering2.on(speed = speed_n, steering= -40)

def linie_5_mode2(current_Sensor_Val):
    upperlimit = 550
    lowerlimit = 480
    full_white = 440
    full_black = 580
    speed_r = -50
    speed_n = -40
    speed_k = -30
    if(lowerlimit <= current_Sensor_Val <= upperlimit):
        MSteering2.on(speed= speed_r,steering=0)
    else:
        if(full_white > current_Sensor_Val):
            MSteering2.on(speed = speed_k, steering= -87)
        elif(full_black < current_Sensor_Val):
            MSteering2.on(speed = speed_k, steering= +87)
        elif(lowerlimit < current_Sensor_Val):
            MSteering2.on(speed = speed_n, steering= 40)
        else:
            MSteering2.on(speed = speed_n, steering= -40)

def liniep_controller_mode2(current_Sensor_Val):
   kp=0.8
   calibration= 530
   #kp=0.8
   #calibration= 546
   newsteering= kp* (calibration-current_Sensor_Val)
   if(newsteering>100):
        newsteering=100
   elif(newsteering<-100):
        newsteering=-100
   MSteering2.on(speed=-25,steering=-newsteering)

def liniep_controller(current_Sensor_Val):
   kp=3.3
   calibration= 33
   newsteering= kp* (calibration-current_Sensor_Val)
   if(newsteering>100):
        newsteering=100
   elif(newsteering<-100):
        newsteering=-100
   MSteering2.on(speed=-20,steering=newsteering)


def liniepd_controller_mode2(current_Sensor_Val, time):
   global error_old
   global time_old
   kp=2
   kd=0
   calibration= 530
   sampletime= time-time_old
   time_old=time
   error=calibration-current_Sensor_Val
   differential= (error - error_old)/sampletime
   error_old=error
   newsteering= kp* error+ kd*differential
   if(newsteering>100):
        newsteering=100
   elif(newsteering<-100):
        newsteering=-100
   MSteering2.on(speed=-24,steering=-newsteering)
  

def liniepd_controller(current_Sensor_Val, time):
   global error_old
   global time_old
   kp=2.91
   kd=0.96
   calibration= 30
   sampletime= time-time_old
   time_old=time
   error=calibration-current_Sensor_Val
   differential= (error - error_old)/sampletime
   error_old=error
   newsteering= kp* error+ kd*differential
   if(newsteering>100):
        newsteering=100
   elif(newsteering<-100):
        newsteering=-100
   MSteering2.on(speed=-24,steering=newsteering)

    
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
   MSteering2.on(speed=-30,steering=newsteering)




	
            
    
    
    


        
    
