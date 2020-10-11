import cv2 as cv
import numpy as np

img = cv.imread('images/messi.jpg', 1)
greyimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
temp = cv.imread('images/messi_face.png', 0)
w, h = temp.shape[::-1]
res = cv.matchTemplate(greyimg, temp, cv.TM_CCOEFF_NORMED)  # or use cv.TM_CCORR_NORMED
threshold = 0.9
loc = np.where(
    res >= threshold)  # this statement is important because in result we have 1000 points so we should give some thrshold and get respective coordinates
x = loc[1][0]
y = loc[0][0]
# for pt in loc[::-1]:
cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=1)
# print(x,y)


cv.imshow('Original', img)
# cv.imshow('Matched', res)
cv.waitKey(0)
cv.destroyAllWindows()
