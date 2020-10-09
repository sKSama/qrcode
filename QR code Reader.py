import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    suc, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        print (obj.data)
        #print("Data", obj.data)
        qrdata = str(obj.data)
        qrdata = qrdata[2:-1]
        cv2.putText(frame, qrdata, (50, 50), font, 2,
                    (255, 255, 255), 3)

    cv2.imshow("sksama", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break   
