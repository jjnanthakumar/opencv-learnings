import cv2 as cv
import numpy as np

# pyramid is multiscale repeated smoothing and subsamplings
# 1) Gaussian Pyramid
# 2) Laplace Pyramid ( formed from gaussian pyramid )
img = cv.imread('images/lena.jpg')
lr = img.copy()
gp = [lr]
# hr = cv.pyrUp(lr)
cv.imshow('Original', img)
for i in range(5):
    lr = cv.pyrDown(lr)  # gaussian
    gp.append(lr)
    # cv.imshow(f'Pyr Down{i}', lr)
# cv.imshow('Upper Level Gausss pyramid', gp[-1])
for i in range(5, 0, -1):
    gauss_ext = cv.pyrUp(gp[i])
    laplace = cv.subtract(gp[i - 1], gauss_ext)  # laplacian pyramid
    cv.imshow(f'Laplace_extended{i}', laplace)
cv.waitKey(0)
cv.destroyAllWindows()
