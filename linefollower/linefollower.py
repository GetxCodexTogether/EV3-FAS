#Init Motor
from ev3dev2.motor import LargeMotor, OUTPUT_A,OUTPUT_B, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM,MoveTank,MoveSteering

error_old=0
integral=0
time_old=0
sum_deviation = 0

old_time=0
old_integral=0


print("Motor/Sensor-Init")
MSteering2 = MoveSteering(left_motor_port=OUTPUT_A,right_motor_port=OUTPUT_B,motor_class=LargeMotor)
MSteering = MoveSteering(left_motor_port=OUTPUT_A,right_motor_port=OUTPUT_B,motor_class=LargeMotor)
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

def liniep_contr(current_Sensor_Val):
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

def straight(current_Sensor_Val):
    MSteering.on(speed=-10,steering=0)

def line_2_RAW(current_Sensor_Val):
    limit=534
    if(limit < current_Sensor_Val):                 # schwarz
        MSteering.on(speed=-30,steering=-40)
    elif(limit== current_Sensor_Val):               # optimal: Soll-Wert
        MSteering.on(speed=-30,steering=0)
    else:
        MSteering.on(speed = -30, steering= 40)     # weiß

def line_3_RAW(current_Sensor_Val):
    upperlimit=560
    lowerlimit = 490
    speed = -30
    if(lowerlimit <= current_Sensor_Val <= upperlimit):                 # optimaler Bereich
        MSteering.on(speed= speed,steering=0)
    elif(upperlimit < current_Sensor_Val):                              # schwarz
        MSteering.on(speed= speed,steering=-40)
    else:
        MSteering.on(speed= speed, steering= 40)                         # weiß

def line_5_RAW(current_Sensor_Val):
    full_black = 615
    upperlimit = 560
    lowerlimit = 490
    full_white = 430
    speed = -15
    speedslow = -15
    if(lowerlimit <= current_Sensor_Val <= upperlimit):
        MSteering.on(speed= speed,steering=0)                           # straight on
    else:
        if(full_white > current_Sensor_Val):
            MSteering.on(speed= speedslow, steering= 90)                # full white
        elif(full_black < current_Sensor_Val):
            MSteering.on(speed= speedslow, steering= -90)               # full black
        elif(lowerlimit > current_Sensor_Val):
            MSteering.on(speed = speed, steering= 40)                   # more white
        else:
            MSteering.on(speed= speed, steering= -40)                   # more black

def lineP_controller(current_Sensor_Val):
    kp = 0.2
    reference = 475
    deviation = reference-current_Sensor_Val
    newsteering = kp * deviation

     # consideration of the limits
    if(newsteering>100):
        newsteering=100
    elif(newsteering<-100):
        newsteering=-100
    MSteering.on(speed=-15,steering=newsteering)

def linePID_controller(current_Sensor_Val, current_time):
    global old_integral
    global old_time
    global sum_deviation

    reference = 475 #534 #31
    kp = 0.3 #0.8958 # 0.2
    ki = 0.023
    kd = 1.2 #1.8
    deviation = reference-current_Sensor_Val
    sampling_time= current_time-old_time
    old_Sensor_Val= current_Sensor_Val

    # P-Controller

    p_controller = kp * deviation 

    # D-controller
    differential = current_Sensor_Val-old_Sensor_Val
    d_controller = (kd*differential)/sampling_time

    # I-Controller
    integral= ki * deviation * sampling_time 
    i_controller = integral+ old_integral
    old_integral = integral
    #sum_deviation= sum_deviation + deviation
    #i_controller = ki * sampling_time* sum_deviation 
    

    # PID-controller
    newsteering= p_controller + d_controller + i_controller
   
    # consideration of the limits
    if(newsteering>100):
        newsteering=100
    elif(newsteering<-100):
        newsteering=-100
    print(newsteering, i_controller, p_controller )
    MSteering.on(speed=-15,steering=newsteering)

def liniepid_control_notime(current_Sensor_Val):
   global error_old
   global integral
   kp = 0.8958
   ki = 2.3268
   kd = 0.08622
   calibration= 534

   error=calibration-current_Sensor_Val

   differential= error - error_old

   integral= integral +error

   error_old=error
   newsteering= kp* error+ kd*differential+ ki*integral

   if(newsteering>100):
        newsteering=100
   elif(newsteering<-100):
        newsteering=-100
   MSteering2.on(speed=-15,steering=newsteering)	
            
    
    
    


        
    
