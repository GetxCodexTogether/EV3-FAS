from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import ColorSensor
SColor= ColorSensor()

def sensor_init():
    print("Sensor-Init")
    

def current_color_value():
    return SColor.reflected_light_intensity