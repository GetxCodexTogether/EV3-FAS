from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button   # EV3 Button


from ev3dev2.display import Display 

SColor= ColorSensor()
SGyro= GyroSensor()
btn = Button()  
SGyro.calibrate()

# Write your program here
    #IR_sense = ColorSensor(Port.S1)

    
    #brick = Display()
    #brick.sound.beep()


def sens_Color():
    return SColor.reflected_light_intensity

def sens_Gyro():
    return SGyro.rate


#while not btn.any():
    #if brick ? dann def close