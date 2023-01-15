#!/usr/bin/env python3
from ev3dev2.stopwatch import StopWatch
from ev3dev2.sound import Sound
from time import sleep
import socket

my_stopwatch = StopWatch()
client_connection = socket.socket()
sound = Sound()

def init():
    global to_client
    port = 12345
    client_connection.bind(('', port))
    client_connection.listen(1)
    print('Waiting for connection...')
    sound.speak('waiting')
    #brick.display.text('Waiting for connection')
    #brick.display.text('    with computer...')
    to_client, addr = client_connection.accept()
    sound.speak('connected')
    #brick.sound.beep(1500, 200)
    #brick.display.clear()
    #brick.display.text('Connection successful!')
    #sleep(0.5)
    my_stopwatch.reset()
    #print(my_stopwatch.value_secs)
    my_stopwatch.start()
    #print(my_stopwatch.value_secs)

def send(value):   
    mystr = str(my_stopwatch.value_secs)+',' +str(value)
    #print(mystr)
    to_client.send(mystr.encode())
    str(to_client.recv(1024).decode())
    return my_stopwatch.value_secs
    
def close():
    mystr = 'end'
    to_client.send(mystr.encode())
    to_client.close()
    #sleep(0.7)
