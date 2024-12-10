import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

fig, ax = plt.subplots(figsize = (12, 8), dpi=200)

xnew = np.array([i-450 for i in range(0, 900)])
xnew = xnew * 23/450

for i in range(11):
    path = "/Users/georgy/Downloads/LABA-02/DATA/datawithflow%d.0.txt" % i
    data = np.loadtxt(path, dtype = int)
    data = (data -  965.65 ) *  0.17
    data = (abs(1.67*data))**0.5
    plt.plot(xnew, data, linestyle='-')

plt.ylim(0, 30)

ax.set_title("Зависимость давления от расстояния")
ax.set_ylabel("Давление, условные единицы")
ax.set_xlabel("Расстояние, условные единицы")

ax.grid(which = 'major', color = 'gray')
ax.minorticks_on()
ax.grid(which = 'major', color = 'gray', linestyle = ":")

plt.savefig("/Users/georgy/Downloads/LABA-02/Graph/test_2.png") 
