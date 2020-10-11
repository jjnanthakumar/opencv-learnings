import numpy as np
import cv2 as cv

img = cv.imread('images/smarties.png')
out = img.copy()
grey = cv.cvtColor(out, cv.COLOR_BGR2GRAY)
blur = cv.medianBlur(grey, 3)
circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT, 1, 20, param1=40, param2=45, maxRadius=0, minRadius=0)
detected = np.uint16(np.around(circles))
# print(detected)
for x, y, r in detected[0]:
    cv.circle(img, (x, y), r, (0, 255, 0), thickness=4)
cv.imshow('Output', img)
cv.waitKey(0)
cv.destroyAllWindows()
