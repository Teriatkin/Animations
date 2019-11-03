import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Імпорт Axes3D має побічні ефекти, він дозволяє використовувати projection = '3d' у add_subplot
from tkinter import *
import numpy as np
from numpy import sin, cos
import matplotlib.animation as animation
import time


def figura():
    l = 4  # довжина (length)
    w = 3  # ширина (width)
    h = 5  # висота (height)
    color_prism = "black"  # колір призми
    lw = 0.5  # товщина граней
    # задаємо відрізки для призми
    x = [[0, 0], [0, 0], [l, l], [l, l], [0, 0], [0, 0], [l, l], [l, l], [0, l], [0, l], [0, l], [0, l]]
    y = [[0, 0], [w, w], [0, 0], [w, w], [0, w], [0, w], [0, w], [0, w], [0, 0], [0, 0], [w, w], [w, w]]
    z = [[0, h], [0, h], [0, h], [0, h], [h, h], [0, 0], [h, h], [0, 0], [0, 0], [h, h], [0, 0], [h, h]]

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set()  # facecolor="w")
    fig.set()  # facecolor="w")

    def ox(cant_x):
        for i in range(12):
            aa = [x[i][0], y[i][0] * cos(cant_x) - z[i][0] * sin(cant_x), y[i][0] * sin(cant_x) + z[i][0] * cos(cant_x)]
            bb = [x[i][1], y[i][1] * cos(cant_x) - z[i][1] * sin(cant_x), y[i][1] * sin(cant_x) + z[i][1] * cos(cant_x)]
            ax.plot(*zip(aa, bb), color=color_prism, linewidth=lw)

    def oy(cant_y):
        for i in range(12):
            aa = [x[i][0] * cos(cant_y) + z[i][0] * sin(cant_y), y[i][0],
                  -x[i][0] * sin(cant_y) + z[i][0] * cos(cant_y)]
            bb = [x[i][1] * cos(cant_y) + z[i][1] * sin(cant_y), y[i][1],
                  -x[i][1] * sin(cant_y) + z[i][1] * cos(cant_y)]
            ax.plot(*zip(aa, bb), color=color_prism, linewidth=lw)

    def oz(cant_z):
        for i in range(12):
            aa = [x[i][0] * cos(cant_z) - y[i][0] * sin(cant_z), x[i][0] * sin(cant_z) + y[i][0] * cos(cant_z), z[i][0]]
            bb = [x[i][1] * cos(cant_z) - y[i][1] * sin(cant_z), x[i][1] * sin(cant_z) + y[i][1] * cos(cant_z), z[i][1]]
            ax.plot(*zip(aa, bb), color=color_prism, linewidth=lw)

    def oxy(cant_xy):
        for i in range(12):
            aa = [x[i][0], y[i][0] * cos(cant_xy) - z[i][0] * sin(cant_xy),
                  y[i][0] * sin(cant_xy) + z[i][0] * cos(cant_xy)]
            bb = [x[i][1], y[i][1] * cos(cant_xy) - z[i][1] * sin(cant_xy),
                  y[i][1] * sin(cant_xy) + z[i][1] * cos(cant_xy)]
            s = [aa[0] * cos(cant_xy) + aa[2] * sin(cant_xy), aa[1], -aa[0] * sin(cant_xy) + aa[2] * cos(cant_xy)]
            e = [bb[0] * cos(cant_xy) + bb[2] * sin(cant_xy), bb[1], -bb[0] * sin(cant_xy) + bb[2] * cos(cant_xy)]
            ax.plot(*zip(s, e), color=color_prism, linewidth=lw)

    def change(cant):
        if var.get() == 0:
            ox(cant)
        elif var.get() == 1:
            oy(cant)
        elif var.get() == 2:
            oz(cant)
        elif var.get() == 3:
            oxy(cant)

    def animate(i):
        ax.clear()
        m_xyz = max(l, w, h)
        ax.set_xlim(-m_xyz, m_xyz)
        ax.set_ylim(-m_xyz, m_xyz)
        ax.set_zlim(-m_xyz, m_xyz)
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        cant = np.radians(i)
        change(cant)


    run_animation = animation.FuncAnimation(fig, animate, interval=10000 / speed.get())

    plt.show()


def gui():
    global var, speed
    root = Tk()
    root.geometry('300x200+1100+100')
    root.title("TeriatkinOnishuk")
    var = IntVar()
    var.set(0)
    speed = IntVar()
    speed.set(100)
    x_button = Radiobutton(text="X", variable=var, value=0)
    y_button = Radiobutton(text="Y", variable=var, value=1)
    z_button = Radiobutton(text="Z", variable=var, value=2)
    xy_button = Radiobutton(text="XY", variable=var, value=3)
    sp_label = Label(text="Speed\n[1 - 1000]")
    sp_entry = Entry(textvariable=speed)
    button = Button(text="RUN animations", command=figura)
    label = Label(width=20, height=10)
    x_button.pack()
    y_button.pack()
    z_button.pack()
    xy_button.pack()
    sp_label.pack()
    sp_entry.pack()
    button.pack()
    label.pack()
    root.mainloop()


gui()
