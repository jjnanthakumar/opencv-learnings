# Hough transform is a tech to detect any shape, represent shapes in a mathematical form
# eg: lines can be respresented in mathematical form as given below
# In cartesian coordinate y = mx + c
# In polar Coordinate xcos0 + ysin0 = r
# Hough transformation Algorithm
# 1. Edge detection, e.g. using the Canny edge detector.
# 2. Mapping of edge points to the Hough space and
# storage in an accumulator.
# 3. Interpretation of the accumulator to yield lines of
# infinite length. The interpretation is done by thresholding
# and possibly other constraints.
# 4. Conversion of infinite lines to finite lines.
# standard Hough line transform ( HoughLines method )
# probabilistic Hough line transform ( HoughLinesP method )
import cv2 as cv
import numpy as np

img = cv.imread('images/sudoku.jpg')
greyimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gblur = cv.GaussianBlur(greyimg, (7, 7), 0)  # used to remove some noises in image
# medblur = cv.medianBlur(greyimg, 3)
edgeimg = cv.Canny(gblur, 50, 150,
                   apertureSize=3)  # threshold values are image intensity set manually done only on greyscale images
# houghlines = cv.HoughLines(edgeimg, 1, np.pi / 180, 200)
houghlines = cv.HoughLinesP(edgeimg, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
for line in houghlines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), thickness=2)
# for line in houghlines:
#     rho, theta = line[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a * rho
#     y0 = b * rho
#     x1 = int(x0 + 1000 * (-b))  # r * cos(theta) - 1000 * sin(theta)
#     y1 = int(y0 + 1000 * (a))  # r * sin(theta) + 1000 * cos(theta)
#     x2 = int(x0 - 1000 * (-b))  # r * cos(theta) + 1000 * sin(theta)
#     y2 = int(y0 - 1000 * (a))  # r * sin(theta) - 1000 * cos(theta)
#     cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), thickness=2)
cv.imshow('Canny', edgeimg)
cv.imshow('Lines', img)
cv.waitKey(0)
cv.destroyAllWindows()
