import socket
import sys
import matplotlib.pyplot as plot
from matplotlib.animation import FuncAnimation
import csv

# open the file in the write mode
f = open('plotdata.csv', 'w')

# create the csv writer
writer = csv.writer(f)
writer.writerow("Affen")
print("Affen")
print("Affen")
print("Affen")

IPaddress = '192.168.178.33'

s = socket.socket()
s.connect((IPaddress, 12345))

plot.style.use('fivethirtyeight')
fig = plot.figure(num=None, figsize=[10, 7])
ax = fig.add_subplot(111)
rcvdData = 'None'
x = []
y = []
def animate(i):
    rcvdData = s.recv(1024).decode()
    if rcvdData != 'end':
        print(rcvdData)
        rcvdDatalist = rcvdData.split(',')
        rcvdDatalist[0] = float(rcvdDatalist[0])
        rcvdDatalist[1] = float(rcvdDatalist[1])
        
        x.append(rcvdDatalist[0])
        
        y.append(rcvdDatalist[1])
        plot.cla()
        plot.plot(x, y)

        
        with open('plotdata.csv', 'a',newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([float(rcvdDatalist[0]), float(rcvdDatalist[1])])

        # Back to Server
        sendData = 'received data!'
        s.send(sendData.encode())
        
        
        #PLOT
        plot.scatter(rcvdDatalist[0], rcvdDatalist[1], s = 500, color='green', marker="X")
        plot.xlabel('Time (seconds)')
        plot.ylabel('Sensor-Wert')
        ax.set_xlim(left=rcvdDatalist[0]-15, right=rcvdDatalist[0]+15)
        ax.set_ylim(bottom=300, top=700)
    else:
        sendData = 'ending process...'
        s.send(sendData.encode())
        s.close()
        sys.exit('Connection ended!')


ani = FuncAnimation(plot.gcf(), animate, interval=10)
plot.show()




