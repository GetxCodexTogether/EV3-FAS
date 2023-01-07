from ev3dev2.sensor import INPUT_1,Sensor
from ev3dev2.sensor.lego import ColorSensor, GyroSensor

from ev3dev2.button import Button   # EV3 Button
from ev3dev2.display import Display 
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import Sensor

#du bist manchmal süß und die andere Zeit hot
#hitechnic sensor
#from ev3dev2.sensor import *
#from ev3dev2.auto import *
#chitechnic = Sensor(address='in1', driver_name='ht-nxt-color-v2')
#chitechnic = Sensor(address=INPUT_1, driver_name='ht-nxt-color-v2')
#c1= Sensor('in1:i2c1')
#chitechnic = Sensor(address=INPUT_1, name_pattern='ht-nxt-color-v2')

#SColor= ColorSensor()

def sensor_init():
    print("Sensor-Init")



def current_color_value():
    return SColor.reflected_light_intensity

S_EV3 = ColorSensor()
#SGyro= GyroSensor()
#SGyro.calibrate()
#sensor_col_ht = Sensor()
#sensor_col_ht = ColorSensor() #Sensor(address='in1')

btn = Button()  

# Write your program here
    #IR_sense = ColorSensor(Port.S1)

    
    #brick = Display()
    #brick.sound.beep()


def sens_Color():
    print(S_EV3.modes,'\t1',S_EV3.mode,'\t2',S_EV3.num_values,"\t3",S_EV3.value())
    print(S_EV3.value(0),S_EV3.value(1))
    return S_EV3.value(0)

def sens_testMode():
    #S_EV3._ensure_mode()
    S_EV3._ensure_mode('REF-RAW')
    #sensor_col_ht._ensure_mode('RAW')

def sens_Gyro():
    return SGyro.rate

def sens_nxt_Color():
    print(sensor_col_ht.modes,' \t',sensor_col_ht.num_values,sensor_col_ht.mode)
    print(sensor_col_ht.value())
    return sensor_col_ht.value()
    #return sensor_col_ht.value[6]

#while not btn.any():
    #if brick ? dann def close