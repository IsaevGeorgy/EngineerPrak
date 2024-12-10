import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

fig, ax = plt.subplots(figsize = (12, 8), dpi=200)

xnew = np.array([i-450 for i in range(0, 900, 5)])
xnew = xnew * 23/450

h = [360, 340, 304, 280, 260, 224, 214, 200, 190, 180, 170]
CARR = []

for i in range(11):
    path = "/Users/georgy/Downloads/LABA-02/DATA/datawithflow%d.0.txt" % i
    data = np.loadtxt(path, dtype = int)
    data50 = []
    for j in range(0, len(data)):
        if j % 5 ==0:
            if j < h[i] or j > 900-h[i]:
                data[j] = 965.65
            data50.append(data[j])
    data5 = np.array(data50)
    data5 = (data5 -  965.65) *  0.17
    data5 = (abs(1.67*data5))**0.5
    
    X_Y_Spline = make_interp_spline(xnew, data5)
    x_smooth = np.linspace(xnew.min(), xnew.max(), 900)
    data5_smooth = X_Y_Spline(x_smooth)
    

    C = 0
    for j in range(0, 899):
       C += 0.5*abs((data5_smooth[j]*x_smooth[j]+data5_smooth[j+1]*x_smooth[j+1])*(x_smooth[j+1]-x_smooth[j]))
    C = 1.2*C*np.pi/1000
    CARR.append(C)
    plt.plot(x_smooth, data5_smooth, linestyle='-', label=f"Q ({i}0 мм) = {round(C, 2)} [г/с]")
plt.ylim(0, 30)

plt.legend()

ax.set_title("Зависимость скорости потока воздуха в сечении от расстояния")
ax.set_ylabel("Скорость воздуха, м/с")
ax.set_xlabel("Расстояние от сопла, мм")

ax.grid(which = 'major', color = 'gray')
ax.minorticks_on()
ax.grid(which = 'major', color = 'gray', linestyle = ":")

plt.savefig("/Users/georgy/Downloads/LABA-02/Graph/test_3.png") 

fig, ax = plt.subplots(figsize = (12, 8), dpi=200)

plt.plot([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0], CARR)

plt.ylim(0, 6)

ax.set_title("Зависимость расхода потока воздуха в сечении от расстояния")
ax.set_ylabel("Расход воздуха, г/с")
ax.set_xlabel("Расстояние от центра, мм")

ax.grid(which = 'major', color = 'gray')
ax.minorticks_on()
ax.grid(which = 'major', color = 'gray', linestyle = ":")

plt.savefig("/Users/georgy/Downloads/LABA-02/Graph/test_4.png") 

fig, ax = plt.subplots(figsize=(8, 10))