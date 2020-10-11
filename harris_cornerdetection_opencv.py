import cv2 as cv
import numpy as np

img = cv.imread('images/chess.jpg')
cv.imshow('Original', img)
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grey1',grey)
# harris corner detection takes grey image in float32 format
grey = np.float32(grey)
corners = cv.cornerHarris(grey, 2, 3, 0.04)  # ksize (aperture parameter) sobel derivative

img[corners > 0.01 * corners.max()] = [0, 0, 255]
cv.imshow('Corners', img)
cv.waitKey(0)
cv.destroyAllWindows()
