from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import ColorSensor


# in middel = 22
# too far right > 22
# too far left < 22

def currentColorvalue():
    colors = ColorSensor()
    light=colors.reflected_light_intensity
    print (light ,"colorsensor")
    return light