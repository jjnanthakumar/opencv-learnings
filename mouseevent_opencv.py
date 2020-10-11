import cv2
import numpy as np


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        strXY = str(x) + ', ' + str(y)
        # img = np.zeros((512, 512, 3), np.uint8)
        img = cv2.imread('images/lena.jpg', 1)
        cv2.putText(img, strXY, (x, y), cv2.FONT_ITALIC, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        img = cv2.imread('images/lena.jpg', 1)
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        strbgr = f"{str(blue)},{str(green)},{str(red)}"
        cv2.putText(img, strbgr, (x, y), cv2.FONT_ITALIC, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('images/lena.jpg', 1)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
