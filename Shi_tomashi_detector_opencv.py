import cv2 as cv
import numpy as np
img = cv.imread('images/shapes.jpg')
# cv.imshow('Original', img)
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grey1',grey)
det = cv.goodFeaturesToTrack(grey, 60, 0.008, 3)
det = np.int0(det)  # int0 is an alias for int64
for i in det:
    x, y = i.ravel()
    cv.circle(img, (x, y), 10, (0, 255, 0), 2)
cv.imshow('Corners', img)
cv.waitKey(0)
cv.destroyAllWindows()
