import csv
import datetime

import cv2
import numpy as np

LENGTH = 1594

FILE = "LocationDensity-filter.csv"

def applyData(data, uwbID, seconds, img):
    print(seconds)
    if uwbID == "A":
        img[0:359, seconds] = data
    elif uwbID == "B":
        img[360:719, seconds] = data
    elif uwbID == "C":
        img[720:1079, seconds] = data


img = np.zeros((1080, LENGTH))
img = cv2.convertScaleAbs(img)
firstFrame = datetime.datetime.strptime("18:01:02", "%H:%M:%S")

aLog = np.zeros(LENGTH, dtype=int)
bLog = np.zeros(LENGTH, dtype=int)
cLog = np.zeros(LENGTH, dtype=int)

with open(FILE) as f:
    reader = csv.reader(f)

    for line in reader:
        nowDate = datetime.datetime.strptime(line[1][:8], "%H:%M:%S")
        delta = (nowDate - firstFrame).seconds
        print(line[0])
        
        if line[0] == "A":
            aLog[delta] += 1
        elif line[0] == "B":
            bLog[delta] += 1
        elif line[0] == "C":
            cLog[delta] += 1

aLog = aLog*255 / 15
bLog = bLog*255 / 15
cLog = cLog*255 / 15

for i in range(LENGTH):
    applyData(aLog[i], "A", i, img)
    applyData(bLog[i], "B", i, img)
    applyData(cLog[i], "C", i, img)



dst = cv2.applyColorMap(img, cv2.COLORMAP_JET)
cv2.imwrite("Density.png", dst)
# cv2.imshow("DENSITY", dst)
# cv2.waitKey(0)