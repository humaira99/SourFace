from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import calculate as calculate
import numpy as np

import matplotlib.pyplot as plt
import csv

# AU1 = 6
"""
for each AU, plot graph with fitting - work out n for polynomial
"""

row = 1
bitters = []
sours = []
saltys = []
sweets = []
umamis = []
au1 = []
au2 = []
au4 = []
au5 = []
au6 = []
au7 = []
au9 = []
au10 = []
au12 = []
au14 = []
au15 = []
au17 = []
au20 = []
au23 = []
au25 = []
au26 = []
au45 = []


with open('../GUI/files/viktoria_gui.csv', 'r') as f:
    data = [row for row in csv.reader(f)]

with open('../GUI/files/viktoria_gui.csv', 'r') as f:
    rows = sum(1 for line in f)

    while row < rows:
        au1.append(float(data[row][5]))
        au2.append(float(data[row][6]))
        au4.append(float(data[row][7]))
        au5.append(float(data[row][8]))
        au6.append(float(data[row][9]))
        au7.append(float(data[row][10]))
        au9.append(float(data[row][11]))
        au10.append(float(data[row][12]))
        au12.append(float(data[row][13]))
        au14.append(float(data[row][14]))
        au15.append(float(data[row][15]))
        au17.append(float(data[row][16]))
        au20.append(float(data[row][17]))
        au23.append(float(data[row][18]))
        au25.append(float(data[row][19]))
        au26.append(float(data[row][20]))
        au45.append(float(data[row][21]))

        row += 1


def graph(au, name, fig):
    plt.figure(fig)
    x = range(0, rows - 1)
    y = au

    train_x = np.array(x)
    train_y = np.array(y)

    polyModel = PolynomialFeatures(degree=6)
    xpol = polyModel.fit_transform(train_x.reshape(-1, 1))
    preg = polyModel.fit(xpol, train_y)

    linearModel = LinearRegression(fit_intercept=True)
    linearModel.fit(xpol, train_y[:, np.newaxis])
    polyfit = linearModel.predict(preg.fit_transform(train_x.reshape(-1, 1)))

    plt.title('' + name)
    plt.xlabel('Frame')
    plt.ylabel('Intensity')
    plt.axis([0, rows - 1, -1, 5])
    plt.scatter(x, y)
    plt.plot(x, polyfit, color='red')


graph(au1, 'AU01: Inner Brow Raiser', 1)
graph(au2, 'AU02: Outer Brow Raiser', 2)
graph(au4, 'AU04: Brow Lowerer', 3)
graph(au5, 'AU05: Upper Lid Raiser', 4)
graph(au6, 'AU06: Cheek Raiser', 5)
graph(au7, 'AU07: Lid Tightener', 6)
graph(au10, 'AU10: Upper Lip Raiser ', 7)
graph(au12, 'AU12: Lip Corner Puller', 8)
graph(au14, 'AU14: Dimpler', 9)
graph(au15, 'AU15: Lip Corner Depressor ', 10)
graph(au17, 'AU17: Chin Raiser', 11)
graph(au20, 'AU20: Lip Stretcher', 12)
graph(au23, 'AU23: Lip Tightener', 13)
graph(au25, 'AU25: Lips Part', 14)
graph(au26, 'AU26: Jaw Drop', 15)
graph(au45, 'AU45: Blink', 16)

plt.show()



