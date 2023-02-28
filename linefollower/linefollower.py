from motor import *
from control import *
motor_speed=-18

error_old=0
integral=0
time_old=0
sum_deviation = 0
old_deviation=0

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
    kp = 0.47 #0.49 # 0.5 bei v=-15
    reference = 475
    deviation = reference-current_Sensor_Val
    newsteering = kp * deviation
    #print(newsteering)
    # i=0
    # while(i<1400):
    #     i+=1
     # consideration of the limits
    if(newsteering>100):
        newsteering=100
    elif(newsteering<-100):
        newsteering=-100
    motor_movesteering.on(speed=motor_speed,steering=newsteering)

def linePID_controller(current_Sensor_Val, current_time):
    global old_integral
    global old_time
    global sum_deviation
    global old_deviation

    reference = 475 #534 #31
    kp = 0.294           # 0.49       #0.8958 # 0.2
    ki = 0.7644          # 0.023
    kd = 0.0282692          #1.2 #1.8
    deviation = reference-current_Sensor_Val
    sampling_time= 0.069776 #current_time-old_time
    old_time = current_time
    #old_Sensor_Val= current_Sensor_Val

    # P-Controller
    p_controller = kp * deviation 

    # D-controller
    #differential = current_Sensor_Val-old_Sensor_Val
    differential=deviation-old_deviation
    d_controller = differential+kd/sampling_time
    
    old_deviation=deviation

    # # I-Controller
    # integral = ki * deviation * sampling_time 

    # # if(deviation==0):
    # #     old_integral=0
    # # elif(((deviation>0) and  (old_deviation<0)) or((deviation<0) and  (old_deviation>0))):
    # #     old_integral=0

    # i_controller = integral+ 0.66*old_integral
    # old_integral = integral

    integral = 0.66 * old_integral + deviation
    old_integral = integral
    i_controller = ki * sampling_time * integral

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
    motor_movesteering.on(speed=motor_speed,steering=newsteering)

    return i_controller

def liniepid_control_notime(current_Sensor_Val):
   global error_old
   global integral
   kp = 0.282#0.294              # 0.49       #0.8958 # 0.2
   ki = 0.0511#0.0533367          # 0.023
   kd =0.3886# 0.4051 
   calibration= 475

   error=calibration-current_Sensor_Val

   differential= error - error_old

   integral= 0.66*integral +error

   error_old=error
   newsteering= kp* error+ kd*differential+ ki*integral

   if(newsteering>100):
        newsteering=100
   elif(newsteering<-100):
        newsteering=-100
   motor_movesteering.on(speed=motor_speed,steering=newsteering)

   return integral	

def liniepid_control_withtime(current_Sensor_Val,time):
   global error_old
   global integral
   global time_old
   kp = 0.282             # 0.49       #0.8958 # 0.2
   ki = 0.7644         # 0.023
   kd = 0.03
   #sampling_time= 0.0376
   sampling_time = time-time_old
   time_old=time
   calibration= 475
   kdd=kd/sampling_time
   kii=ki*sampling_time
   
   error=calibration-current_Sensor_Val

   differential= error - error_old

   integral= 0.66*integral +error
   old_integral

   error_old=error
   newsteering= kp * error+ kdd*differential+ kii*integral

   if(newsteering>100):
        newsteering=100
   elif(newsteering<-100):
        newsteering=-100
   motor_movesteering.on(speed=motor_speed,steering=newsteering)

   return integral

def liniepid_control_withtimetest(current_Sensor_Val,time):
   global error_old
   global integral
   global time_old
#    kp = 0.282             # 0.49       #0.8958 # 0.2
#    ki = 0.7644         # 0.023
#    kd = 0.03
   #sampling_time= 0.0376
   sampling_time = time-time_old
   time_old=time
   calibration= 475
   kp=getkp()
   kd=getkd(sampling_time)
   ki=getki(sampling_time)
   kdd=kd/sampling_time
   kii=ki*sampling_time
   print(kd)
   error=calibration-current_Sensor_Val

   differential= error - error_old

   integral= 0.66*integral +error
   old_integral

   error_old=error
   newsteering= kp * error+ kdd*differential+ kii*integral

   if(newsteering>100):
        newsteering=100
   elif(newsteering<-100):
        newsteering=-100
   motor_movesteering.on(speed=motor_speed,steering=newsteering)

   return integral

def susserArsch(time):
    if time <=2:
        motor_movesteering.on(speed = motor_speed, steering = 0)
    else:
        motor_movesteering.on(speed = motor_speed, steering = -100)
    

    
    
    
    


        
    
