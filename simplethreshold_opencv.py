import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/gradients.png', 1)

# Simple Thresholding Technique
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 50, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['Original', 'ThreshBinary', 'ThreshBinaryINV', 'ThreshTrunc', 'ThreshtoZero', 'ThreshtoZeroINV']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])
# cv.imshow('Frame', img)
# cv.imshow('Th1', th1)
# cv.imshow('Th2', th2)
# cv.imshow('Th3', th3)
# cv.imshow('Th4', th4)
# cv.imshow('Th5', th5)

plt.show()
# # Adoptive Thresholding
# img = cv.imread('sudoku.jpg', 0)
#
# th = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 4)
# th1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 4)

# # print(th)
# cv.imshow('th', th)
# cv.imshow('th1', th1)

# cv.waitKey(0)
# cv.destroyAllWindows()
