import cv2
import numpy as np

testblack = np.zeros([100, 100], dtype=np.uint8)
testwhite = np.ones([100, 100], dtype=np.uint8) * 255

print(testblack)
print(testwhite)

print(testblack.shape)
print(testblack.size)
print(testblack.dtype)
print(testblack[50, 50])

for i in range(40, 60):
    for j in range(40, 60):
        testblack[i, j] = 255

cv2.imshow('black', testblack)
cv2.imshow('white', testwhite)

testgray = np.zeros([100,100], dtype = np.uint8)
cv2.addWeighted(testwhite, 0.5, testblack, 0.5, 0, testgray)
#cv2.imshow('gray', testgray)
#print(testgray[50, 50])
