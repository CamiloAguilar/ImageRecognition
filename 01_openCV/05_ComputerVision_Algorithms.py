import cv2
import numpy as np

img = cv2.imread('./images/playa.jpg', 0)
#cv2.imshow('original image', img)
#cv2.waitKey(0)

## SIFT feature detector
siftimg = np.zeros(np.shape(img), dtype=np.uint8)
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(img, None)
siftimg = cv2.drawKeypoints(img, kp, siftimg)

## Harrtis Corner Detector
imgf = np.float32(img)
dst = cv2.cornerHarris(img, 2, 3, 0.04)

Harrising = img.copy()

Harrising = cv2.cvtColor(Harrising, cv2.COLOR_GRAY2BGR)
# Threshold for an optimal value, it may vary depending on 
Harrising[dst>0.02*dst.max()] = [0, 0, 255]

cv2.imshow('original image', img)
cv2.imshow('Harris', Harrising)

cv2.waitKey(0)


