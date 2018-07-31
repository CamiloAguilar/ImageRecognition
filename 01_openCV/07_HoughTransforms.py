## hay otros algorítmos llamados halftones (tonos medios), el cual es utilizado para encontrar
## ciertas formas en las imagenes 

#**********************
## Hough transforms
#**********************

## Detecta formas como lineas y círculos en imágenes
## Basado en un método voting
## GEneralizado para cualquier forma

import cv2
import numpy as np

img = cv2.imread('./images/ajedrez.jpg')
imgcolor = img.copy()
cv2.imshow('Hough Lines image', imgcolor)
cv2.waitKey()

imgcolor = cv2.cvtColor(imgcolor, cv2.COLOR_GRAY2BGR)

edges = cv2.Canny(img, 50, 150, apertureSize = 3)

lines = cv2HoughLinesP(edges, 1, np.pi/180, 25, 25, 10)

for line in lines:
	cv2.line(imgcolor, (line[0][0], line[0][1]), (line[0][2], line[0][3]), (0, 255, 0), 2)

cv2.imshow('Original image', img)
cv2.imshow('Canny image', edges)
cv2.imshow('Hough Lines image', imgcolor)