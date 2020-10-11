# morphological transformations are some simple image operations based on image shape
# morphological transformations is normally performed on binary images
# two types erosion and dilation
from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

img = cv.imread('images/smarties.png', 0)
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY)
kernel = np.ones((2, 2), np.uint8)
dilate = cv.dilate(mask, kernel, iterations=4)
erode = cv.erode(mask, kernel, iterations=4)
# easymorph = cv.morphologyEx(mask,cv.MORPH_DILATE, kernel, iterations=4)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=4)  # erosion followed by dilation (open)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=4)  # opposite to open
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel, iterations=4)
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel, iterations=4)

titles = ['Original', 'masked', 'dilation', 'erosion', 'opening', 'closing', 'Gradient', 'tophat']
images = [img, mask, dilate, erode, opening, closing, mg, th]

for i in range(len(images)):
    plt.subplot(2, len(images) // 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
