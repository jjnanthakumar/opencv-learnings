import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# kernel is a shape used for masking
img = cv.imread('images/messi.jpg', 0)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


# canny edge detection 5 steps
# 1) Noise Reduction (using Gaussian Filter)
# 2) Gradient Calculation
# 3) Non-maximum supression
# 4) Double Threshold
# 5) Edge Tracking by Hysteresis

def none(x):
    return x


# cv.namedWindow('Tracks')
# #
# cv.createTrackbar('Threshold1', 'Tracks', 0, 400, none)
# cv.createTrackbar('Threshold2', 'Tracks', 0, 400, none)
th1, th2 = 100, 200
while 1:
    # img = cv.imread('messi.jpg', 1)

    k = cv.waitKey(1)  # use & 0xFF in 32 bit
    if k == 27:  # esc key ascii - 27
        break
    # th1 = cv.getTrackbarPos('Threshold1', 'Tracks')
    # th2 = cv.getTrackbarPos('Threshold2', 'Tracks')
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    canny = cv.Canny(img, th1, th2)
    cv.imshow('Tracks', img)
    # cv2.imshow('Tracks', img)
    titles = ['Original', 'Canny']
    images = [img, canny]
    # cv.imshow('Original',img)
    # cv.imshow('Canny',canny)
    for i in range(len(images)):
        plt.subplot(1, 2, i + 1)
        plt.imshow(images[i], 'gray')
        plt.xticks([]), plt.yticks([])
        plt.title(titles[i])
    plt.show()
    break  # put this statement if you are using only matplotlib

cv.waitKey(0)
cv.destroyAllWindows()
