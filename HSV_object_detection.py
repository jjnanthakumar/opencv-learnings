# HSV ( Hue Saturation Value)

# Hue from 0 - 360 ( diff colors )
# saturation (dominace from 0 - 100%) - depth of pigment
# Value is brightness of the color

import cv2
import numpy as np


def none(x):
    return x


# img = np.zeros((512, 512, 3), np.uint8)
cap = cv2.VideoCapture(0)
cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, none)
cv2.createTrackbar('LS', 'Tracking', 0, 255, none)
cv2.createTrackbar('LV', 'Tracking', 0, 255, none)
cv2.createTrackbar('UH', 'Tracking', 255, 255, none)
cv2.createTrackbar('US', 'Tracking', 255, 255, none)
cv2.createTrackbar('UV', 'Tracking', 255, 255, none)

while 1:
    # img = cv2.imread('smarties.png', 1)
    _, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    l_hue = cv2.getTrackbarPos('LH', 'Tracking')
    l_sat = cv2.getTrackbarPos('LS', 'Tracking')
    l_val = cv2.getTrackbarPos('LV', 'Tracking')
    u_hue = cv2.getTrackbarPos('UH', 'Tracking')
    u_sat = cv2.getTrackbarPos('US', 'Tracking')
    u_val = cv2.getTrackbarPos('UV', 'Tracking')
    l_b = np.array([l_hue, l_sat, l_val])
    h_b = np.array([u_hue, u_sat, u_val])

    mask = cv2.inRange(hsv, l_b, h_b)

    res = cv2.bitwise_and(img, img, mask=mask)

    k = cv2.waitKey(1)  # use & 0xFF in 32 bit
    if k == 27:  # esc key ascii - 27
        break

    cp = cv2.getTrackbarPos('CP', 'Tracks')
    cv2.imshow('Tracks', mask)
    cv2.imshow('Tracks1', img)
    cv2.imshow('Tracks2', res)
    # cv2.imshow('Tracks', img)
cap.release()
cv2.destroyAllWindows()
