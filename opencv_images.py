# Working with images
import cv2, os

img = cv2.imread('images/lena.jpg', 0)
print(img)
cv2.imshow('test', img)

k = cv2.waitKey(0)  # & 0xFF ( if doesn't work) use this mask
if k == ord('0'):
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('images/lena_grey.png', img) if not os.path.isfile('images/lena_grey.png') else print("File name already exists!")
    cv2.destroyAllWindows()
