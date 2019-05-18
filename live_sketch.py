import cv2
import numpy as np

def penciler(image, mask):
    return cv2.divide(image, 255-mask, scale=256)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_gray_inv = 255 - img_gray
    img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(21, 21),sigmaX=0, sigmaY=0)
    img_blend = penciler(img_gray, img_blur)
    cv2.imshow('Our Live Sketcher', img_blend)
    if cv2.waitKey(1) == 13: #13 signifie qu'il faut appuyer sur entrer pour terminer
        break
        
# Release camera and close windows
cap.release()
cv2.destroyAllWindows()    

