import cv2
import numpy as np
import os
from datetime import datetime

live_capture = cv2.VideoCapture(0)

while True:
    s, img = live_capture.read()
    try:
        image_s = cv2.resize(img, (0,0), None, 0.25, 0.25)
    except:
        print("Camera being used somewhere else!")
    else:
        image_s = cv2.cvtColor(image_s, cv2.COLOR_BGR2RGB)
    key = cv2.waitKey(5) & 0xFF
    if key == ord("q"):
        break

    cv2.imshow('Camera', img)
    cv2.waitKey(1)