import cv2 as cv
import numpy as np

img = cv.imread('images/shapes.jpg')
# img = cv.resize(img, (512,512))
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

print(img.shape)
_, thresh = cv.threshold(grey, 240, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    apprx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    cv.drawContours(img, [contour], 0, (0, 0, 255), thickness=3)
    x = apprx.ravel()[0]
    y = apprx.ravel()[1]-5
    # print(x, y)
    if len(apprx) == 3:
        cv.putText(img, "Triangle", (x, y), fontFace=cv.FONT_ITALIC, fontScale=1, color=(0, 0, 0),
                   thickness=2, lineType=cv.LINE_AA)
    elif len(apprx) == 4:
        x, y, w, h = cv.boundingRect(apprx)
        aspectRatio = float(w) / h
        if aspectRatio >= .95 and aspectRatio <= 1.05:
            cv.putText(img, "Square", (x, y), fontFace=cv.FONT_ITALIC, fontScale=1, color=(0, 0, 0),
                       thickness=2, lineType=cv.LINE_AA)
        else:
            cv.putText(img, "Rectangle", (x, y), fontFace=cv.FONT_ITALIC, fontScale=1, color=(0, 0, 0),
                       thickness=2, lineType=cv.LINE_AA)
    elif len(apprx) == 5:
        cv.putText(img, "Pentagon", (x, y), fontFace=cv.FONT_ITALIC, fontScale=1, color=(0, 0, 0),
                   thickness=2, lineType=cv.LINE_AA)
    elif len(apprx) == 10:
        cv.putText(img, "Star", (x, y), fontFace=cv.FONT_ITALIC, fontScale=1, color=(0, 0, 0),
                   thickness=2, lineType=cv.LINE_AA)
    else:
        cv.putText(img, "Circle", (x, y), fontFace=cv.FONT_ITALIC, fontScale=1, color=(0, 0, 0),
                   thickness=2, lineType=cv.LINE_AA)
cv.imshow('Shapes', img)
cv.waitKey(0)
cv.destroyAllWindows()
