# Using Numpy with open cv
import cv2

img = cv2.imread('images/lena.jpg', 1)  # or
# img = np.zeros(shape=[512,512,3], dtype=np.uint8)
# img = cv2.line(img, (0, 0), (255, 255), color=(0, 0, 255), thickness=5)
# img = cv2.arrowedLine(img, (300, 0), (255, 400), color=(0, 0, 255), thickness=5)
# img = cv2.rectangle(img, (400, 100), (100, 384), color=(0, 255, 255), thickness=3)
img = cv2.circle(img, radius=100, center=(300, 300), color=(0, 0, 255), thickness=3)
img = cv2.putText(img, 'OpenCV Practice', (10, 500), fontFace=cv2.FONT_ITALIC, fontScale=4, color=(0, 255, 255),
                  thickness=3, lineType=cv2.LINE_AA)
cv2.imshow('someframe', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
