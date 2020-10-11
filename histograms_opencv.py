import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# histogram is a graph (intensity distribution of image)

img = cv.imread('images/lena.jpg', 1)

b,g,r= cv.split(img)
# print(b.ravel())
# # img = np.zeros((200, 200), np.uint8)
# plt.hist(b.ravel(),256, [0, 256])
# plt.hist(g.ravel(),256, [0, 256])
# plt.hist(r.ravel(),256, [0, 256])
# cv.imshow('B', b)
# cv.imshow('G', g)
# cv.imshow('R', r)
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
