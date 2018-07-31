import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	ret, frame = cap.read()
	cv2.imshow("webcam Feed", frame)
	if cv2.waitKey(20)==32:
		break

cap.release()
