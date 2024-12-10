import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize = (12, 8), dpi=200)

data = np.loadtxt("/Users/georgy/Downloads/LABA-02/DATA/data0.txt", dtype = int)
avg_flow0 = np.average(data)
data = np.loadtxt("/Users/georgy/Downloads/LABA-02/DATA/datawithflow.txt", dtype = int)
avg_flow1 = np.average(data)
plt.ylim(0, 80)
ax.set_title("Калибровочный график зависимости показаний АЦП от давления.")
ax.set_ylabel("Давление ПА")
ax.set_xlabel("Отсчеты АЦП")

x = [avg_flow0, avg_flow1]

y = [0, 77.3]

plt.plot(x, y, linestyle='-')

ax.grid(which = 'major', color = 'gray')
ax.minorticks_on()
ax.grid(which = 'major', color = 'gray', linestyle = ":")

plt.savefig("/Users/georgy/Downloads/LABA-02/Graph/pressure-calibration.png")

print('(x - ', avg_flow0, ") * ", (77.3)/(avg_flow1-avg_flow0))



