import matplotlib.pyplot as plot
from matplotlib.animation import FuncAnimation


plot.style.use('fivethirtyeight')
fig = plot.figure(num=None, figsize=[10, 7])
ax = fig.add_subplot(111)

x = []
y = []
def animate(i):  #rcvdDatalist? wie einfügen?

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

def meckerschlumpf():
    ani = FuncAnimation(plot.gcf(), animate, interval=1)
    plot.show() 



