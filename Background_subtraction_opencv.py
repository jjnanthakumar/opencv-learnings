import cv2 as cv
import numpy as np

cap = cv.VideoCapture('images/vtest.avi')
# fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
# fgbg = cv.bgsegm.createBackgroundSubtractorGMG()
fgbg = cv.createBackgroundSubtractorKNN(detectShadows=False)
# fgbg = cv.createBackgroundSubtractorMOG2()
# kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
while cap.isOpened():
    _, frame = cap.read()
    fgmask = fgbg.apply(frame)
    # fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel, iterations=1)
    k = cv.waitKey(1)
    if k == 27:
        break
    cv.imshow('Live', frame)
    cv.imshow('FG Mask', fgmask)
cap.release()
cv.destroyAllWindows()
