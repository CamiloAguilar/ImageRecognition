import cv2
import numpy as np

img = cv2.imread('./images/playa.jpg', 0)

edges1 = cv2.Canny(img, 50, 150)
edges2 = cv2.Canny(img, 150, 200)

cv2.imshow('Original image', img)
cv2.imshow('Canny Edges with thresh(50, 150)', edges1)
cv2.imshow('Canny Edges with thresh(150, 200)', edges2)

cv2.waitKey()