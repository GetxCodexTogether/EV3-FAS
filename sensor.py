from ev3dev2.sensor import INPUT_1,Sensor
from ev3dev2.sensor.lego import ColorSensor, GyroSensor

from ev3dev2.button import Button   # EV3 Button
from ev3dev2.display import Display 
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import Sensor

#du bist manchmal süß und die andere Zeit hot

def init_sensor_col_ev3():
    print("Sensor-Init")
    global sensor_col_ev3
    sensor_col_ev3 = ColorSensor()
    #sensor_col_ev3._ensure_mode()
    sensor_col_ev3._ensure_mode('REF-RAW')
   

def init_sensor_col_ht():
    print("Sensor-Init")
    global sensor_col_ht
    sensor_col_ht = Sensor()
    sensor_col_ht._ensure_mode('RAW')


def sensor_col_ev3_value():
    print(sensor_col_ev3.modes,'\t1',sensor_col_ev3.mode,'\t2',sensor_col_ev3.num_values,"\t3",sensor_col_ev3.value())
    print(sensor_col_ev3.value(0),sensor_col_ev3.value(1))
    return sensor_col_ev3.value(0)
    #return SColor.reflected_light_intensity not needed


def sensor_col_ht_value():
    print(sensor_col_ht.modes,' \t',sensor_col_ht.num_values,sensor_col_ht.mode)
    print(sensor_col_ht.value())
    return sensor_col_ht.value()
    #return sensor_col_ht.value[6]

