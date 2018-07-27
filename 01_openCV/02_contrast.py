import cv2
import numpy as np

img = cv2.imread("./images/whale8.jpg", 0)

cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.imwrite('./images/whale8_gray.png',img)

#Min max stretch
imgstretched = np.zeros(np.shape(img), dtype=np.uint8)
cv2.normalize(img, imgstretched, 0, 255, cv2.NORM_MINMAX)
cv2.imshow("Min max stretch", imgstretched)
cv2.waitKey(0)

## Histogram equalization
histeqimg = cv2.equalizeHist(img)
cv2.imshow("Histogram Equalization", histeqimg)
cv2.waitKey(0)



cv2.destroyAllWindows()