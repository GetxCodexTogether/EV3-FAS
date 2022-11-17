from time import sleep
from ev3dev2.sensor.lego import ColorSensor

print("init")
btn = Button()
lmL=LargeMotor(OUTPUT_B)
LMR= LargeMotor(OUTPUT_A)


Name.on_for_degrees(speed=50,degrees=5)


cl = ColorSensor() 
# Do something when state of any button changes:
  
def left(state):
    if state:
        print('Left button pressed')
        lmL.on_for_degrees(speed=40,degrees=5)
    else:
        print('Left button released')
    
def right(state):  # neater use of 'if' follows:
    print('Right button pressed' if state else 'Right button released')
    
def up(state):
    print('Up button pressed' if state else 'Up button released')
    
def down(state):
    print('Down button pressed' if state else 'Down button released')
    
def enter(state):
    if state: 
        print('Enter button pressed' )
        #lmL.on(speed=45)
        lmL.on_for_degrees(speed=40,degrees=200)
    else:
        print('Enter button released')
        #lmL.on(speed=100)
        

    
btn.on_left = left
btn.on_right = right
btn.on_up = up
btn.on_down = down
btn.on_enter = enter
# This loop checks button states continuously (every 0.01s). 
# If the new state differs from the old state then the appropriate
# button event handlers are called.

while 1:
    for element in range(1, 170):
        #lmL.on_for_degrees(speed=10,degrees=1,block=False)
        lmL.on_for_degrees(speed=-100,degrees=1000,block=False)
        LMR.on_for_degrees(speed=100,degrees=1000,block=False)
        #MID.on_for_degrees(degrees=-10,speed=10)
    # MID.on_for_degrees(degrees=20,speed=10)
        #LMR.on(speed=5,block=False)
        #lmL.on(speed=5,block=False)
        print(cl.reflected_light_intensity)
        
        btn.process()
        #sleep(0.01)