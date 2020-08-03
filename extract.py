#program to extract roll numbers from ss
import cv2
import pytesseract
from pytesseract import Output
import glob
#import numpy as np

def send_details():
    path = glob.glob("images/*")
    details = []
    for file in path:
        print("glob-file = ", file)
        image = cv2.imread(file)
        custom_config = r'--oem 3 --psm 6'
        dict1 = pytesseract.image_to_data(image, output_type=Output.DICT, config=custom_config, lang='eng')
        details.append(dict1['text'])

    #print(details)
    return details

'''

#RECTANGULAR BOXES AROUND TEXT

n_boxes = len(details['text'])
for i in range(n_boxes):
    if int(details['conf'][i]) > 60:
        (x, y, w, h) = (details['left'][i], details['top'][i], details['width'][i], details['height'][i])
        img = cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)

img = cv2.resize(img, (500,800)) # w,h

print(*details['text'], sep="\n")
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''



'''

#IMAGE THRESHOLDING

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
result = 255 - close

result = cv2.resize(result, (1280, 900))
cv2.imshow('sharpen', sharpen)
cv2.imshow('thresh', thresh)
cv2.imshow('close', close)

cv2.imshow('result', result)
cv2.waitKey()
cv2.destroyAllWindows()

'''