import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

fig, ax = plt.subplots()
plt.title('Sheer transformation')
plt.xlabel('x')
plt.ylabel('y')
numframes = 20
xdata = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
         4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
         5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
         6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
         7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
         8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
         9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
ydata = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
         0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
         0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
         0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
         0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
         0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
         0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
         0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
         0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
         0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ln, = plt.plot([], [], 'ro', markersize=2)
plt.plot([0,30], [0,30], 'b-', linewidth=0.5, alpha=0.5)

def init():
    ax.set_ylim(0, 30)
    ax.set_xlim(0, 30)
    return ln,

def update(counter):
    newx = []
    newy = []
    counter = counter % (numframes*2)
    #Q = ax.quiver([1, 6], [5, 3], [3+counter, 3], [3+counter, 3], angles='xy', scale_units='xy', scale=1)
    if ((counter < 3) or ((counter) >= (numframes*2 - 3))): # original coordinates
        ln.set_data(xdata, ydata)
    elif (counter < numframes-2): # waxing phase
        range_magnitude = numframes-2 - 3
        scaling = ((counter-3) % range_magnitude) / (range_magnitude - 1)
        for i in range(len(xdata)):
            newx.append(xdata[i] + (xdata[i] + ydata[i])*scaling)
            newy.append((xdata[i] + ydata[i])*scaling + ydata[i])
        ln.set_data(newx, newy)
        return ln,
    elif ((counter >= numframes-2) and (counter < numframes+2)): # pause at fully transformed
        for i in range(len(xdata)):
            newx.append(xdata[i]*2 + ydata[i])
            newy.append(ydata[i]*2 + xdata[i])
        ln.set_data(newx, newy)
        return ln,
    else: # waning phase
        range_magnitude = numframes-2 - 3
        scaling = 1 - (((counter-(numframes+2)) % range_magnitude) / (range_magnitude - 1))
        for i in range(len(xdata)):
            newx.append(xdata[i] + (xdata[i] + ydata[i])*scaling)
            newy.append((xdata[i] + ydata[i])*scaling + ydata[i])
        ln.set_data(newx, newy)
        return ln,

ani = animation.FuncAnimation(fig, update, init_func=init, interval=numframes*2, frames=600, repeat=True)
plt.show()
ani.save('sheer_transform.gif')
