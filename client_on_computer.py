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

IPaddress = '192.168.178.54'
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
        #print(rcvdDatalist[1])
        #mypoint = "("+str(rcvdDatalist[0])+", "+str(rcvdDatalist[1])+")"
        # x-axis values
        x.append(rcvdDatalist[0])
        # y-axis values
        y.append(rcvdDatalist[1])
        plot.cla()
        plot.plot(x, y)

        #EXCEL
        test=str(rcvdDatalist[0])+","+str(rcvdDatalist[1])
        writer.writerow(test)
        with open('plotdata.csv', 'a',newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([float(rcvdDatalist[0]), float(rcvdDatalist[1])])

        # Back to Server
        sendData = 'received data!'
        s.send(sendData.encode())
        
        
        #PLOT
        plot.scatter(rcvdDatalist[0], rcvdDatalist[1], s = 500, color='green', marker="X")
        plot.xlabel('Time (seconds)')
        plot.ylabel('Distance (%)')
        ax.set_xlim(left=rcvdDatalist[0]-15, right=rcvdDatalist[0]+15)
        #ax.set_ylim(bottom=currenty-50, top=currenty+50)
        ax.set_ylim(bottom=0, top=110)
    else:
        sendData = 'ending process...'
        s.send(sendData.encode())
        s.close()
        sys.exit('Connection ended!')


ani = FuncAnimation(plot.gcf(), animate, interval=1)
plot.show()





sendData = 'ending process...'
s.send(sendData.encode())
s.close()
sys.exit('Connection ended!')

# close the file
f.close()