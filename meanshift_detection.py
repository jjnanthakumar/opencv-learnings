import cv2 as cv
import numpy as np

cap = cv.VideoCapture('images/slow_traffic_small.mp4')
_, frame = cap.read()
x, y, w, h = 300, 200, 100, 50
track_window = (x, y, w, h)
roi = frame[y:y + h, x:x + w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
# kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
# give histogram back protected image
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])

cv.normalize(roi_hist, roi_hist, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
# termination criteria for mean shift is either 10 iterations or move atleast by 1 pt
term = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
while cap.isOpened():
    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # back projection
    dst = cv.calcBackProject([hsv]
                             , [0], roi_hist, [0, 180], 1)
    # apply meanshift
    # ret, track_window = cv.meanShift(dst, track_window, term)
    ret, track_window = cv.CamShift(dst, track_window, term)
    pts = np.int0(cv.boxPoints(ret))
    finalimage = cv.polylines(frame, [pts], True, 255, 3)
    # x, y, w, h = track_window
    # finalimage = cv.rectangle(frame, (x, y), (x + w, y + h), 255, 3)
    cv.imshow('final', finalimage)
    k = cv.waitKey(1)
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
