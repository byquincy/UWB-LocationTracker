import serial
import time
import cv2
import numpy as np


SECTION_TIME = 1/24
MAX_RANGE = 2000


py_serial = serial.Serial(
    port='/dev/cu.usbserial-01115E82',
    baudrate=115200,
)

image = np.zeros((1080, 1920))


showTime = time.time() + SECTION_TIME
sectionSum = 0
sectionCount = 0
while True:
    if py_serial.readable():
        # 들어온 값이 있으면 값을 한 줄 읽음 (BYTE 단위로 받은 상태)
        # BYTE 단위로 받은 response 모습 : b'\xec\x97\x86\xec\x9d\x8c\r\n'
        response = py_serial.readline()
        range = float(response.decode())
        
        # 디코딩 후, 출력 (가장 끝의 \n을 없애주기위해 슬라이싱 사용)
        # print(range)
        sectionSum += range
        sectionCount += 1
    
        if time.time() >= showTime:
            avarageRange = sectionSum/sectionCount
            whiteHeight = max( 0, min(880, int(879 - avarageRange/MAX_RANGE*880)) )

            image = np.zeros((1080, 1920))
            image[885:, :] = 255
            image[whiteHeight:880, :] = 255
            cv2.putText(
                image, 
                str(int(avarageRange)) + "Cm", 
                (50, 1030), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                3, (0, 0, 0), 3, cv2.LINE_AA
            )
            cv2.imshow("RANGE", image)
            cv2.waitKey(1)

            sectionSum = 0
            sectionCount = 0
            showTime = time.time() + SECTION_TIME