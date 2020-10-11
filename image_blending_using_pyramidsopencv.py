import cv2 as cv
import numpy as np

# pyramid is multiscale repeated smoothing and subsamplings
# 1) Gaussian Pyramid
# 2) Laplace Pyramid ( formed from gaussian pyramid )
apple = cv.imread('images/apple.jpg')
orange = cv.imread('images/orange.jpg')
# print(apple.shape)
# print(orange.shape)
# generate gauss pyramid for apple and orange
apple_gauss = apple.copy()
orange_gauss = orange.copy()
g_apples, g_oranges = [apple_gauss], [orange_gauss]
for i in range(6):
    apple_gauss = cv.pyrDown(apple_gauss)
    g_apples.append(apple_gauss)
for i in range(6):
    orange_gauss = cv.pyrDown(orange_gauss)
    g_oranges.append(orange_gauss)

# generate Laplace pyramid
ap_lap = [g_apples[-2]]
or_lap = [g_oranges[-2]]
for i in range(5, 0, -1):
    apples_extend = cv.pyrUp(g_apples[i])
    a_laplace = cv.subtract(g_apples[i - 1], apples_extend)
    # cv.imshow(str(i)+'apple', a_laplace)
    ap_lap.append(a_laplace)
for i in range(5, 0, -1):
    oranges_extend = cv.pyrUp(g_oranges[i])
    o_laplace = cv.subtract(g_oranges[i - 1], oranges_extend)
    # cv.imshow(str(i)+'orange', o_laplace)
    or_lap.append(o_laplace)
# cv.imshow('apple', apple)
# cv.imshow('orange', orange)
# add left and right half images in each level
apple_orange_pyramid = []
# n = 0
for apple_lap, orange_lap in zip(ap_lap, or_lap):
    cols, row, ch = apple_lap.shape
    # print(cols)
    app_orange = np.hstack((apple_lap[:, :int(cols/ 2)], orange_lap[:, int(cols/ 2):]))
    apple_orange_pyramid.append(app_orange)

# now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]

for i in range(1, 6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i], apple_orange_reconstruct)

# app_oran = np.hstack((apple[:, :apple.shape[1] // 2], orange[:, orange.shape[1] // 2:]))
cv.imshow('apple-orange', apple_orange_reconstruct)
cv.waitKey(0)
cv.destroyAllWindows()
