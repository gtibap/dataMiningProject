import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([1], [1], 'ro') #, lw=2

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(t):
    #x = np.linspace(0, 2, 1000)
    x = 1 + 0.8*np.sin(2 * np.pi * (0.01 * t))
    y = 0 + 1*np.sin(2 * np.pi * (0.01 * t))
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=30, blit=True)


plt.show()
