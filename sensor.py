#from ev3dev2.sensor import INPUT_1,Sensor  noch ersetzten
#from ev3dev2.sensor.lego import ColorSensor
from pybricks.ev3devices import  ColorSensor
from pybricks.parameters import Port
from pybricks.iodevices import Ev3devSensor

#du bist manchmal süß und die andere Zeit hot :*

def sensor_col_ev3_init():
    print("Sensor-Init")
    global sensor_col_ev3
    sensor_col_ev3 = Ev3devSensor(Port.S1)
    #pybricks
    #sensor_col_ev3.read('REF-RAW')
    #sensor_col_ev3._ensure_mode('REF-RAW')
    #sensor_col_ev3._ensure_mode('COL-REFLECT')

# def sensor_col_ht_init():
#     print("Sensor-Init")
#     global sensor_col_ht
#     sensor_col_ht = Sensor()
#     sensor_col_ht._ensure_mode('NORM')

def sensor_col_ev3_value():
    #print(sensor_col_ev3.modes,'\t1',sensor_col_ev3.mode,'\t2',sensor_col_ev3.num_values,"\t3",sensor_col_ev3.value())
    #print(sensor_col_ev3.value(0),sensor_col_ev3.value(1))
    #return  sensor_col_ev3.value(0)
    sensor_value = sensor_col_ev3.read('REF-RAW')
    print(sensor_value[1])
    return  sensor_value[1]
   
def sensor_col_ht_value():
    #print(sensor_col_ht.modes,' \t',sensor_col_ht.num_values,sensor_col_ht.mode)
    return sensor_col_ht.value()
    #return sensor_col_ht.value[6]

