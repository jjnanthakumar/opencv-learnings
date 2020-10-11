import cv2
import numpy as np

img1 = np.zeros((512, 512, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread('images/lena.jpg', 1)
cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
# bitand = cv2.bitwise_and(img1,img2)
# cv2.imshow('bit',bitand)
# bitor = cv2.bitwise_or(img1, img2)
# cv2.imshow('bit',bitor)
# bitXor = cv2.bitwise_xor(img1, img2)
# cv2.imshow('bit', bitXor)
bitnot = cv2.bitwise_not(img1)
bitnot1 = cv2.bitwise_not(img2)
cv2.imshow('bit', bitnot)
cv2.imshow('bit1', bitnot1)
cv2.waitKey(0)
cv2.destroyAllWindows()

