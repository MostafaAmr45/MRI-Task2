import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


# function to create the rotation matrix
def rotMatrix(angle):
    c = np.cos(np.radians(angle))
    s = np.sin(np.radians(angle))
    return np.array([[c, -s], [s, c]])


flag = 0
random = []  # a list to store the nonuniform magnetic field


def data_gen(num):
    """Data generation"""

    global flag
    global random
    if num == 90 and flag == 0:
        flag = 1
    elif num == 180 and flag == 1:
        flag = 0

    z = num / 18

    if flag == 0 and not z == 10:
        ax.cla()
        ax.quiver(0, 0, 0, z, 0, (5 - z), pivot="tail", color="red")

    elif flag == 1 and not z == 10:
        z = z - 5
        v = np.array([0, (5 - z)])

        random = np.random.randint(16, 18, 90)
        v30 = rotMatrix(num * (random[num-90])).dot(v)
        ax.cla()
        ax.quiver(0, 0, 0, v30[0], v30[1], z, pivot="tail", color="red")

    ax.quiver(0, 0, 0, 0, 0, 5, pivot="tail", color="black",
              linestyle="dashed")

    ax.set_xlim3d([-5, 5])
    ax.set_xlabel('X')

    ax.set_ylim3d([-5, 5])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-5, 5])
    ax.set_zlabel('Z')

    ax.set_title('3D Test')


gyromag_ratio = 42.6  # gyromagnetic ratio for the Hydrogen atoms
r = np.random.randint(16, 18, 90)
print(r * gyromag_ratio)  # List of different angular frequencies in MHz

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
data_gen(0)
ani = animation.FuncAnimation(fig, data_gen, 181, interval=1, blit=False)
# ani.save('animated_gif1.gif', writer=animation.PillowWriter(fps=30))
plt.show()