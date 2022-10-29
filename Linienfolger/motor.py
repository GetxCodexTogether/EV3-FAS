from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank

left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_B)
both = MoveTank(OUTPUT_A, OUTPUT_B)

def driveonlyleft (speedinpercent, rotation):
    left.on_for_rotations(SpeedPercent(speedinpercent), rotation)

def drivebothtime (speedinpercentleft, speedinpercentright, time):
     both.on_for_seconds(SpeedPercent(speedinpercentleft), SpeedPercent(speedinpercentright), time)

def drivebothrot (speedinpercentleft, speedinpercentright, rotation):
    both.on_for_rotations(SpeedPercent(speedinpercentleft), SpeedPercent(speedinpercentright), rotation)