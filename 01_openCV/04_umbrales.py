## Umbral es útil para separar sujetos del fondo

import numpy as np
import cv2

img = cv2.imread("./images/leopard.jpeg", 0)
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 20)
ret2, th3 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("Original Image", img)
cv2.imshow("Global Thresholding", th1)
cv2.imshow("Adaptive Thresholding", th2)

cv2.waitKey(0)




