import cv2 as cv
import numpy as np
cap = cv.VideoCapture('images/vtest.avi')
ret, frame1 = cap.read()
ret, frame2 = cap.read()
while cap.isOpened():
    # ret, frame = cap.read()
    diff = cv.absdiff(frame1, frame2)
    grey = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(grey, (5, 5), 0)
    _, thr = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thr, None, iterations=3)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        if cv.contourArea(contour) < 2000:
            continue
        cv.rectangle(frame1, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
        cv.putText(frame1, "Status : Movement", (10, 20), fontFace=cv.FONT_ITALIC, fontScale=1, color=(0, 255, 255),
                   thickness=3, lineType=cv.LINE_AA)
    # cv.drawContours(frame1, contours, -1, (0, 255, 0), thickness=2)
    cv.imshow('Video', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    k = cv.waitKey(40)
    if k == 27:
        break

cv.destroyAllWindows()

cap.release()
