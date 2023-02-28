import socket
import csv


# open the file in the write mode
f = open('plotdata.csv', 'w')

# create the csv writer
writer = csv.writer(f)
writer.writerow("Affen")
print("Affen")
print("Affen")
print("Affen")

IPaddress = '192.168.178.108'
s = socket.socket()
s.connect((IPaddress, 12345))
#rcvdData = 'None'

def test():
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

while(1):
    test()




