import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# kernel is a shape used for masking
img = cv.imread('images/salt_pepper_noise.png', 1)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
kernel = np.ones((5, 5), np.float) / 25
filters = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5, 5))
gblur = cv.GaussianBlur(img, (5, 5), 0)
medblur = cv.medianBlur(img, 3)  # ksize must be odd if 1 then original image printed # it removes salt and pepper noise effectively
bilateralfilter = cv.bilateralFilter(img, 10, 105, 105)
titles = ['Original', '2D Convolution', 'Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral']
images = [img, filters, blur, gblur, medblur, bilateralfilter]

for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
