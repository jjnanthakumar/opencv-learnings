import cv2


# import mouseevent_opencv

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        strXY = str(x) + ', ' + str(y)
        cv2.imshow('image', img)

        # img = np.zeros((512, 512, 3), np.uint8)
        # img = cv2.imread('messi.jpg', 1)
        cv2.putText(img, strXY, (x, y), cv2.FONT_ITALIC, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)


img = cv2.imread('images/messi.jpg', 1)
# print(img.shape)
# print(img.size)
# print(img.dtype)
# b, g, r = cv2.split(img)
# print(b, g, r)
# img = cv2.merge([b, g, r])
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
img2 = cv2.imread('images/lena.jpg', 1)
img2 = cv2.resize(img2, (512, 512))
img = cv2.resize(img, (512, 512))
print(img.shape)
# img = cv2.add(img, img2)
img = cv2.addWeighted(img, 0.9, img2, 0.3, 10)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
# ROI ( region of interests )
