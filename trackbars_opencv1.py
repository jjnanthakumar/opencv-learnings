import cv2
import numpy as np


def none(x):
    return x


# img = np.zeros((512, 512, 3), np.uint8)

cv2.namedWindow('Tracks')
#
cv2.createTrackbar('CP', 'Tracks', 10, 400, none)

switch = ' color/grey '
cv2.createTrackbar(switch, 'Tracks', 0, 1, none)

while 1:
    img = cv2.imread('images/lena.jpg', 1)

    k = cv2.waitKey(1)  # use & 0xFF in 32 bit
    if k == 27:  # esc key ascii - 27
        break
    cp = cv2.getTrackbarPos('CP', 'Tracks')
    s = cv2.getTrackbarPos(switch, 'Tracks')
    if s == 0:
        cv2.imshow('Tracks', img)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.putText(img, str(cp), (10, 500), fontFace=cv2.FONT_ITALIC, fontScale=4, color=(0, 255, 255),
                thickness=3, lineType=cv2.LINE_AA)
    cv2.imshow('Tracks', img)
    # cv2.imshow('Tracks', img)
cv2.destroyAllWindows()
