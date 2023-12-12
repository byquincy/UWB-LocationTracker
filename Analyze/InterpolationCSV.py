import csv
import numpy as np

FILE = "LocationStack.csv"

def apollon(array, startCusor, endCusor):
    startNumber = array[startCusor]
    endNumber = array[endCusor]
    step = (endNumber - startNumber) / (endCusor - startCusor)

    i = 1
    for cusor in range(startCusor+1, endCusor):
        array[cusor] = startNumber + (step*i)
        i += 1

locationStack = np.zeros((3, 1594), dtype=np.int64)
startCusorSilo = [-1, -1, -1]

with open("LocationStack.csv") as f:
    rdr = csv.reader(f)

    i = 0
    for line in rdr:
        locationStack[0][i] = int(line[1])
        locationStack[1][i] = int(line[2])
        locationStack[2][i] = int(line[3])

        # Check Cusor
        for j in range(3):
            if startCusorSilo[j] == -1:
                if locationStack[j][i] == 0:
                    startCusorSilo[j] = i-1
            elif  locationStack[j][i] != 0:
                if locationStack[j][i] >= 20000:
                    continue
                apollon(locationStack[j], startCusorSilo[j], i)
                startCusorSilo[j] = -1

        i += 1

# for i in range(1594):
#     print("%10d"%locationStack[2][i], end=" ")
#     if i%10 == 0:
#         print()


# Export CSV
frame = np.arange(1594, dtype=int)
locationStack = np.vstack([frame, locationStack])

with open("LocationFinal.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerows(locationStack.T)