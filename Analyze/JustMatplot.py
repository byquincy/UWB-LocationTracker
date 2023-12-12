import csv
import numpy as np

import matplotlib.pyplot as plt

# FILE = "LocationStack.csv"
FILE = "LocationFinal.csv"

x = np.arange(1594, dtype=int)
y1 = np.zeros(1594, dtype=int)
y2 = np.zeros(1594, dtype=int)
y3 = np.zeros(1594, dtype=int)

dataNum = 1400

with open(FILE) as f:
    rdr = csv.reader(f)

    for line in rdr:
        cusor = int(line[0])
        y1[ cusor ] = int(line[1])
        y2[ cusor ] = int(line[2])
        y3[ cusor ] = int(line[3])

        


# Export CSV
plt.plot(x[:dataNum], y1[:dataNum], color='red')
plt.plot(x[:dataNum], y2[:dataNum], color='green')
plt.plot(x[:dataNum], y3[:dataNum], color='blue')
plt.show()