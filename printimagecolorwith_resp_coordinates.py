import cv2
import numpy as np


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        coloronly = np.zeros((512, 512, 3), np.uint8)
        # coloronly[:] = [blue, green, red]
        # print(coloronly)
        cv2.imshow('color', [blue, green, red] + coloronly)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('images/lena.jpg', 1)
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)
k = cv2.waitKey(0)
while k == ord('c'):
    points = []
    img = cv2.imread('images/lena.jpg', 1)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    if cv2.waitKey(0) == ord('q'):
        break
    cv2.destroyAllWindows()
cv2.destroyAllWindows()
