import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]])  # Corrected typo

    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    h = hsvC[0][0][0]
    lowerLimit = np.array([h - 10, 100, 100])
    upperLimit = np.array([h + 10, 255, 255])

    # Handle wrapping around the Hue range (0-179 in OpenCV)
    if lowerLimit[0] < 0:
        lowerLimit[0] = 0
    if upperLimit[0] > 179:
        upperLimit[0] = 179

    lowerLimit = np.uint8(lowerLimit)  # Corrected typo
    upperLimit = np.uint8(upperLimit)  # Corrected typo

    return lowerLimit, upperLimit
