# zur initialisierung nötig
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank

# definition of the motors
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_B)
both = MoveTank(OUTPUT_A, OUTPUT_B)

# function to drive
def driveonlyleft (speedinpercent, rotation):
    left.on_for_rotations(SpeedPercent(speedinpercent), rotation)

def driveonlyright (speedinpercent, rotation):
    right.on_for_rotations(SpeedPercent(speedinpercent), rotation)

def drivebothtime (speedinpercentleft, speedinpercentright, time):
     both.on_for_seconds(SpeedPercent(speedinpercentleft), SpeedPercent(speedinpercentright), time)

def drivebothrot (speedinpercentleft, speedinpercentright, rotation):
    both.on_for_rotations(SpeedPercent(speedinpercentleft), SpeedPercent(speedinpercentright), rotation)

# Funktionen aufrufen:
driveonlyleft(70,4)
drivebothrot(10,10,0.2)