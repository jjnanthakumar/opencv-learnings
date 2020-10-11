import cv2
import numpy as np


def none(x):
    return x


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Tracks')
cv2.imshow('Tracks', img)

cv2.createTrackbar('B', 'Tracks', 0, 255, none)
cv2.createTrackbar('G', 'Tracks', 0, 255, none)
cv2.createTrackbar('R', 'Tracks', 0, 255, none)

switch = ' 0 : OFF\n 1: ON '
cv2.createTrackbar(switch, 'Tracks', 0, 1, none)

while 1:
    cv2.imshow('Tracks', img)
    k = cv2.waitKey(1)  # use & 0xFF in 32 bit
    if k == 27:  # esc key ascii - 27
        break
    b = cv2.getTrackbarPos('B', 'Tracks')
    g = cv2.getTrackbarPos('G', 'Tracks')
    r = cv2.getTrackbarPos('R', 'Tracks')
    s = cv2.getTrackbarPos(switch, 'Tracks')
    if s == 0:
        continue
    img[:] = [b, g, r]
    # cv2.imshow('Tracks', img)
cv2.destroyAllWindows()
