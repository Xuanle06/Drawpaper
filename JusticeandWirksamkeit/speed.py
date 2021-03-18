import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig, ax = plt.subplots()

x = np.arange(0, 4*np.pi, 0.01)

line, = ax.plot(x, np.sin(x+np.pi*0.5))


line2, =ax.plot(x, np.sin(x-x))
line3, =ax.plot(x, np.sin(x-x)+1)
line4, =ax.plot(x, np.sin(x-x)-1)


def animate(i):
    line.set_ydata(np.sin(x + i / 25)*np.random.uniform(0,1))
    return [line]


ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)


plt.show()