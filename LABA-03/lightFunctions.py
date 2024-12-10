import numpy as np
import matplotlib.pyplot as plt
import imageio
from cycler import cycler
import matplotlib.ticker as ticker


def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.imread(photoName) # чтение фото
    background = photo[480:1030, 1130:1385, 0:3].swapaxes(0, 1) # поворот изображения

    cut = photo[480:1030, 1170:1350, 0:3].swapaxes(0, 1) # обрезание изображения (x->y; y->x)
    rgb = np.mean(cut, axis=(0)) # среднее арифметическое массива обрезанного изображения
    # коэффициенты для красного, синего, зелёного
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig = plt.figure(figsize=(10, 5), dpi=200) # создание изображения

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')

    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'w', label='I')
    plt.legend()

    plt.imshow(background, origin='lower')

    plt.savefig(plotName)

    return luma

names = ['white', 'red', 'green', 'blue', 'yellow']
m = [0] * 6
path = '/Users/georgy/Downloads/LABA-03/'
for i in range(len(names)):
    m[i] = readIntensity(path+'photo/'+names[i]+'2.png', path+'graph/'+names[i]+'_result.png', "лампа накаливания + ртутная", names[i])

m[5] = readIntensity(path+'photo/'+names[0]+'.png', path+'graph/'+names[0]+'_result1.png', "лампа ртутная", names[i])

k = -0.46
b = 646
x = [k * i + b for i in range(len(m[5]))]

fig, ax = plt.subplots(figsize=(9, 7), dpi=500)
#Включаем видимость сетки и делений (вводим их параметры ниже(сверху нельзя)
ax.minorticks_on()
#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
#Устанавливаем параметры подписей делений: https://pyprog.pro/mpl/mpl_axis_ticks.html
ax.tick_params(axis = 'both', which = 'major', labelsize = 15, pad = 2, length = 10)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15, pad = 2, length = 5)
#название графика с условием для переноса строки и центрированием
ax.set_title('Отражённая интенсивность излучения лампы накаливания', fontsize = 20, loc = 'center')
#сетка основная и второстепенная
ax.grid(which='major', color = 'gray')
ax.grid(which='minor', color = 'gray', linestyle = '--')
#подпись осей
ax.set_ylabel("Яркость", fontsize = 16)
ax.set_xlabel("Длина волны [нм]", fontsize = 16)
ax.patch.set_facecolor('0.8')
ax.plot(x, m[3], 'b', label = "Синий лист")
ax.plot(x, m[2], 'g', label = "Зелёный лист")
ax.plot(x, m[1], 'r', label = "Красный лист")
ax.plot(x, m[0], 'white', label = "Белый лист")
ax.plot(x, m[4], 'y', label = "Жёлтый лист")
ax.legend()
fig.savefig("/Users/georgy/Downloads/LABA-03/Graph/intensites.png")
fig.clf()

ba = np.divide(m[3],m[0])
ra = np.divide(m[1],m[0])
ga = np.divide(m[2],m[0])
ya = np.divide(m[4],m[0])
wa = [1 for i in range(len(m[0]))]

fig, ax = plt.subplots(figsize=(9, 7), dpi=500)
#Включаем видимость сетки и делений (вводим их параметры ниже(сверху нельзя)
ax.minorticks_on()
#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#Устанавливаем параметры подписей делений: https://pyprog.pro/mpl/mpl_axis_ticks.html
ax.tick_params(axis = 'both', which = 'major', labelsize = 15, pad = 2, length = 10)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15, pad = 2, length = 5)
#название графика с условием для переноса строки и центрированием
ax.set_title('Альбедо поверхностей', fontsize = 20, loc = 'center')
#сетка основная и второстепенная
ax.grid(which='major', color = 'gray')
ax.grid(which='minor', color = 'gray', linestyle = '--')
#подпись осей
ax.set_ylabel("Альбедо", fontsize = 16)
ax.set_xlabel("Длина волны [нм]", fontsize = 16)
ax.patch.set_facecolor('0.85')
ax.plot(x, ba, 'b', label = "Синий лист")
ax.plot(x, ga, 'g', label = "Зелёный лист")
ax.plot(x, ra, 'r', label = "Красный лист")
ax.plot(x, wa, 'white', label = "Белый лист")
ax.plot(x, ya, 'y', label = "Жёлтый лист")
ax.legend()
fig.savefig("/Users/georgy/Downloads/LABA-03/Graph/albedo.png")
fig.clf()