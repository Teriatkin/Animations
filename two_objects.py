from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
from celluloid import Camera
from tkinter import *
import math
import numpy as np
import time


def gui():
    global sc, sd, length, run
    root = Tk()
    root.geometry('300x200+1100+100')
    root.title("TeriatkinOnishuk")
    sc = IntVar()  # від 1 до 10
    sc.set(3)
    sd = IntVar()  # від 1 до 10
    sd.set(4)
    length = IntVar()  # від 1 до 20
    length.set(10)
    run = IntVar()
    run.set(50)
    sc_label = Label(text="Швидкість кота:")
    sc_entry = Entry(textvariable=sc)
    sd_label = Label(text="Швидкість собаки:")
    sd_entry = Entry(textvariable=sd)
    length_label = Label(text="Відстань між котом та собакою:")
    length_entry = Entry(textvariable=length)
    run_label1 = Label(text="!!!Уповільнення!!!")
    run_entry = Entry(textvariable=run)
    sd_entry = Entry(textvariable=sd)
    b = Button(text="Оновити", command=start)
    sc_label.pack()
    sc_entry.pack()
    sd_label.pack()
    sc_entry.pack()
    sd_entry.pack()
    length_label.pack()
    length_entry.pack()
    run_label1.pack()
    run_entry.pack()
    b.pack()
    root.mainloop()


def start():
    fig = plt.figure()
    camera = Camera(fig)
    static = plt.axes(xlim=(-20, 20), ylim=(-20, 20))
    ax = fig.add_subplot(111, sharex=static, sharey=static)

    dog = "C:\\Users\\teria\\Downloads\\1.png"
    cat = "C:\\Users\\teria\\Downloads\\2.png"

    def po_line():
        line, = ax.plot([], [], lw=1)
        line.set_data([], [])
        xdata, ydata = [], []
        for i in range(720):
            R = 15
            m = 6.5
            x = R * (math.cos(math.radians(i)) - math.cos(m * math.radians(i)) / m)
            y = R * (math.sin(math.radians(i)) - math.sin(m * math.radians(i)) / m)

            xdata.append(x)
            ydata.append(y)
        line.set_data(xdata, ydata)
        time.sleep(10)

    def imscatter(x, y, image, ax, zoom=1):
        if ax is None:
            ax = plt.gca()
        try:
            image = plt.imread(image)
        except TypeError:
            # Likely already an array...
            pass
        im = OffsetImage(image, zoom=zoom)
        x, y = np.atleast_1d(x, y)
        artists = []
        for x0, y0 in zip(x, y):
            ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False)
            artists.append(ax.add_artist(ab))
        ax.update_datalim(np.column_stack([x, y]))
        # ax.autoscale()
        return artists

    for t in range(720):
        R = 15
        m = 6.5
        x = R * (math.cos(math.radians(t * sc.get()) + (np.pi / 10 * length.get())) - math.cos(
            m * math.radians(sc.get() * t) + (np.pi / 10 * length.get())) / m)
        y = R * (math.sin(math.radians(sc.get() * t) + (np.pi / 10 * length.get())) - math.sin(
            m * math.radians(sc.get() * t) + (np.pi / 10 * length.get())) / m)
        x1 = R * (math.cos(math.radians(t * sd.get())) - math.cos(m * math.radians(t * sd.get())) / m)
        y1 = R * (math.sin(math.radians(t * sd.get())) - math.sin(m * math.radians(t * sd.get())) / m)
        imscatter(x, y, cat, ax=ax, zoom=1)
        imscatter(x1, y1, dog, ax=ax, zoom=1)
        ax.scatter([float(x), float(x1)], [float(y), float(y1)], s=20, c='#1f77b4', alpha=0.5)
        camera.snap()

    animation = camera.animate(interval=run.get())

    plt.show()


gui()
