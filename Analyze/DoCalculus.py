import csv
import numpy as np

import matplotlib.pyplot as plt

FILE = "LocationFinal.csv"

x = np.arange(1595, dtype=int)
y1 = np.zeros(1595, dtype=int)
y2 = np.zeros(1595, dtype=int)
y3 = np.zeros(1595, dtype=int)

dataNum = 1400

temp = [0, 0, 0]
with open(FILE) as f:
    rdr = csv.reader(f)

    for line in rdr:
        cusor = int(line[0])

        y1[ cusor+1 ] = abs(int(line[1]) - temp[0])
        y2[ cusor+1 ] = abs(int(line[2]) - temp[1])
        y3[ cusor+1 ] = abs(int(line[3]) - temp[2])

        temp[0] = int(line[1])
        temp[1] = int(line[2])
        temp[2] = int(line[3])

y1[1] = 0
y2[1] = 0
y3[1] = 0
        


# Export CSV
# plt.plot(x[:dataNum], y1[:dataNum], color='red')
# plt.plot(x[:dataNum], y2[:dataNum], color='green')
plt.plot(x[:dataNum], y3[:dataNum], color='black')
plt.show()