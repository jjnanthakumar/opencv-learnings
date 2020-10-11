import cv2
import numpy as np


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, radius=3, center=(x, y), color=(255, 0, 255), thickness=-1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('image', img)


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
