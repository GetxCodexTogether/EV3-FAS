import socket
import csv
import matplotlib.pyplot as plot
from matplotlib.animation import FuncAnimation


plot.style.use('fivethirtyeight')
fig = plot.figure(num=None, figsize=[10, 7])
ax = fig.add_subplot(111)

x = []
y = []

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
#rcvdData = 'None'

def animate(i):
    global rcvdDatalist
    rcvdData = s.recv(1024).decode()
    if rcvdData != 'end':
        #print(rcvdData)
        rcvdDatalist = rcvdData.split(',')
        rcvdDatalist[0] = float(rcvdDatalist[0])
        rcvdDatalist[1] = float(rcvdDatalist[1])
        #rcvdDatalist[2] = float(rcvdDatalist[2])
        

        with open('plotdata.csv', 'a',newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([float(rcvdDatalist[0]), float(rcvdDatalist[1])])

        # Back to Server
        sendData = 'received data!'
        s.send(sendData.encode())
        x.append(rcvdDatalist[0])
        y.append(rcvdDatalist[1])
        plot.cla()
        plot.plot(x, y)
        #PLOT
        plot.scatter(rcvdDatalist[0], rcvdDatalist[1], s = 500, color='green', marker="X")
        plot.xlabel('Time (seconds)')
        plot.ylabel('Distance (%)')
        ax.set_xlim(left=rcvdDatalist[0]-15, right=rcvdDatalist[0]+15)
        ax.set_ylim(bottom=-500, top= 500)

ani = FuncAnimation(plot.gcf(), animate, interval=1)
plot.show() 




