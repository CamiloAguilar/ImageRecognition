import cv2
import numpy as np

testblack = np.zeros([100, 100], dtype=np.uint8)
testwhite = np.ones([100, 100], dtype=np.uint8)*255

print(testblack.shape)
print(testblack.size)
print(testblack.dtype)
print(testblack[50, 50])


