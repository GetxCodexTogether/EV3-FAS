#from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, MoveSteering 
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Color, ImageFile, SoundFile

def motor_init():
    global  motor_r,  motor_l
    motor_l = Motor(Port.A) 
    motor_r = Motor(Port.B)

motor_movesteering = MoveSteering(left_motor_port=OUTPUT_A,right_motor_port=OUTPUT_B,motor_class=LargeMotor) 

def motor_r_speed_get():
    motor_r_speed = motor_r.speed
    return motor_r_speed

def motor_l_speed_get():
    motor_l_speed = motor_l.speed
    return motor_l_speed

def motor_r_count_per_rote_get():
    motor_r_count_per_rot = motor_r.count_per_rot
    return motor_r_count_per_rot

def motor_l_count_per_rote_get():
    motor_l_count_per_rot = motor_l.count_per_rot
    return motor_l_count_per_rot


