from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep

btn = Button()
sound = Sound()

if(0):
    while True:
        if btn.any():    # Checks if any button is pressed.
            sound.beep()  # Wait for the beep to finish.
            exit()  # Stop the program.
        else:
            sleep(0.01)  # Wait 0.01 second


from ev3dev2.power import PowerSupply

power = PowerSupply()
print("amps",power.measured_amps)
print("volts",power.measured_volts)
print("type",power.type)
print("max_voltage",power.max_voltage)
print("min_voltage",power.min_voltage)
print("measured voltage",power.measured_voltage)
print("measured current",power.measured_current)