import cv2
import numpy as np
from PIL import Image
from util import get_limits
import time

yellow = (0, 255, 255)  # yellow in RGB colorspace
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open webcam.")
    exit()

object_count = 0
last_count_time = time.time()
cooldown_period = 5  # Cooldown period in seconds

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:  # when there is a yellow object
        x1, y1, x2, y2 = bbox  # location of box
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)  # type of bbox

        # Check if cooldown period has elapsed since the last count
        if time.time() - last_count_time > cooldown_period:
            object_count += 1
            last_count_time = time.time()

    cv2.putText(frame, f'Yellow Objects: {object_count}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
