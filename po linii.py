import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax = plt.axes(xlim=(-20, 20), ylim=(-20, 20))
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
plt.show()
