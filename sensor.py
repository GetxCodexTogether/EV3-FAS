from ev3dev2.sensor import INPUT_1,Sensor
from ev3dev2.sensor.lego import ColorSensor, GyroSensor

from ev3dev2.button import Button   # EV3 Button
from ev3dev2.display import Display 

S_EV3= ColorSensor()
#SGyro= GyroSensor()
#SGyro.calibrate()
SNxtColor = ColorSensor()#Sensor(address='in1')

btn = Button()  

# Write your program here
    #IR_sense = ColorSensor(Port.S1)

    
    #brick = Display()
    #brick.sound.beep()


def sens_Color():
    return S_EV3.reflected_light_intensity

def sens_testMode():
    print(S_EV3.modes,'\t1',S_EV3.mode,'\t2',S_EV3.num_values,"\t3",S_EV3.value())

def sens_Gyro():
    return SGyro.rate

def sens_nxt_Color():
    print(SNxtColor.modes,' \t',SNxtColor.num_values,SNxtColor.mode)
    print(SNxtColor.value())
    #return SNxtColor.value[6]

#while not btn.any():
    #if brick ? dann def close