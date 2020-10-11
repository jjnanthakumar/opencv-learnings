from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

img = cv.imread('images/lena.jpg', 1)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
titles = ['Original']
images = [img]

for i in range(1):
    plt.subplot(1, 1, i + 1)
    plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
