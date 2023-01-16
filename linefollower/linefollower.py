from motor import *

error_old=0
integral=0
time_old=0
sum_deviation = 0

old_time=0
old_integral=0

def straight():
    motor_movesteering.on(speed=-10,steering=0)

def line_2_RAW(current_Sensor_Val):
    limit=534
    if(limit < current_Sensor_Val):                 # schwarz
        motor_movesteering.on(speed=-30,steering=-40)
    elif(limit== current_Sensor_Val):               # optimal: Soll-Wert
        motor_movesteering.on(speed=-30,steering=0)
    else:
        motor_movesteering.on(speed = -30, steering= 40)     # weiß

def line_3_RAW(current_Sensor_Val):
    upperlimit=560
    lowerlimit = 490
    speed = -30
    if(lowerlimit <= current_Sensor_Val <= upperlimit):                 # optimaler Bereich
        motor_movesteering.on(speed= speed,steering=0)
    elif(upperlimit < current_Sensor_Val):                              # schwarz
        motor_movesteering.on(speed= speed,steering=-40)
    else:
        motor_movesteering.on(speed= speed, steering= 40)                         # weiß

def line_5_RAW(current_Sensor_Val):
    full_black = 615
    upperlimit = 560
    lowerlimit = 490
    full_white = 430
    speed = -15
    speedslow = -15
    if(lowerlimit <= current_Sensor_Val <= upperlimit):
        motor_movesteering.on(speed= speed,steering=0)                           # straight on
    else:
        if(full_white > current_Sensor_Val):
            motor_movesteering.on(speed= speedslow, steering= 90)                # full white
        elif(full_black < current_Sensor_Val):
            motor_movesteering.on(speed= speedslow, steering= -90)               # full black
        elif(lowerlimit > current_Sensor_Val):
            motor_movesteering.on(speed = speed, steering= 40)                   # more white
        else:
            motor_movesteering.on(speed= speed, steering= -40)                   # more black

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
    motor_movesteering.on(speed=-15,steering=newsteering)

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
    motor_movesteering.on(speed=-15,steering=newsteering)

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
   motor_movesteering.on(speed=-15,steering=newsteering)	
            
    
    
    


        
    
