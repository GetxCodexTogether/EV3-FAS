from ev3dev2.motor import LargeMotor, OUTPUT_A,OUTPUT_B, MediumMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM,MoveTank,MoveSteering

print("Motor/Sensor-Init")
MSteering = MoveSteering(left_motor_port=OUTPUT_A,right_motor_port=OUTPUT_B,motor_class=LargeMotor)
MLeft = LargeMotor(OUTPUT_A)
MRight = LargeMotor(OUTPUT_B)

#sprung:
def go_on():
    MSteering.on(speed=-100,steering=0)
def turn_on(direction):
    MSteering.on(speed=-100*direction,steering=-100)

def timing(time):
    if (time<10):
        go_on()
    elif(time < 6):
        #MSteering.off()
        turn_on(1)
    elif(time<8):
        turn_on(-1)
    else:
        MSteering.off()