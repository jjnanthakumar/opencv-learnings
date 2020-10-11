import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# kernel is a shape used for masking
img = cv.imread('images/messi.jpg', 0)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)  # ddept is datatype supports neg number
lap = np.uint8(np.absolute(lap))
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1)
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
sobelcombined = cv.bitwise_or(sobelx, sobely)
titles = ['Original', 'laplace', 'SobelX', 'SobelY','SobelCombined']
images = [img, lap, sobelx, sobely, sobelcombined]

for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
