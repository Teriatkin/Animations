import matplotlib.pyplot as plt
import math


R = 15
m = 6.5
b = 360
fig = plt.figure(figsize=[6, 5], dpi=100, edgecolor="red", frameon=False)

for t in range(b):
	x = R * (math.cos(math.radians(t * 2)) - math.cos(m * math.radians(t * 2)) / m)
	y = R * (math.sin(math.radians(t * 2)) - math.sin(m * math.radians(t * 2)) / m)

	fig = plt.scatter(x, y, s=2, c='#1f77b4')

plt.show()




