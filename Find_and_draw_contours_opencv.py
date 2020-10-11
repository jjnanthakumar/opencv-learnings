import cv2 as cv
import numpy as np

# Contours
# curve joining all continuous points along the boundaries having same color or intensity ( used for object detection, shape analysis)
img = cv.imread('images/opencv-logo.png', 1)
imggrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thr = cv.threshold(imggrey, 127, 255, 0)
countours, hierarchy = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("Number of Contours: ", len(countours))
# print("Number of Heirarchy: ", len(hierarchy))

cv.drawContours(img, countours, 9, (0, 255, 255), thickness=3)
cv.imshow('Orginal', img)
cv.imshow('Grey', imggrey)
# cv.imshow('Thresh', thr)

cv.waitKey(0)
cv.destroyAllWindows()
