import csv
import datetime

import numpy as np

FILE = "Location-filter.csv"

previousFrame = {
    "A": 0,
    "B": 0,
    "C": 0
}
countTemp = {
    "A": 0,
    "B": 0,
    "C": 0
}

table = {
    "A": np.zeros(1594, dtype=int),
    "B": np.zeros(1594, dtype=int),
    "C": np.zeros(1594, dtype=int)
}

firstDate = datetime.datetime.strptime("18:01:02", "%H:%M:%S")

with open(FILE) as f:
    reader = csv.reader(f)

    for line in reader:
        nowDate = datetime.datetime.strptime(line[0][:8], "%H:%M:%S")
        id = line[1]
        distance = int(line[2])

        delta = (nowDate - firstDate).seconds

        if delta == previousFrame[id]:
            table[id][delta] += distance
            countTemp[id] += 1
        else:
            try:
                table[id][ previousFrame[id] ] = table[id][ previousFrame[id] ] / countTemp[id]
            except:
                print("Error")
            previousFrame[id] = delta
            countTemp[id] = 0




print("--------")

# for i in range(1594):
#     print("%10d"%table["C"][i], end=" ")
#     if i%10 == 0:
#         print()

frame = np.arange(1594, dtype=int)

dst = np.stack((
    frame,
    table["A"],
    table["B"],
    table["C"]
), axis=1)

with open("LocationStack.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerows(dst)