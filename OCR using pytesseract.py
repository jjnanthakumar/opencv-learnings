import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # your path may be different


def remove_noise(img):
    return cv.medianBlur(img, 5)


def thresholding(img):
    return cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]


def getstring(img):
    return pytesseract.image_to_string(img)


def getgray(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


img = cv.imread('images/text.jpg')
# grey = getgray(img)
img = getgray(img)
# img = thresholding(img)
# img = remove_noise(img)
data = getstring(img)
print(type(data))
print(data.replace('\n',''))
