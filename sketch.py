import cv2
import numpy as np

img_rgb = cv2.imread("images/zoumarou.jpg")
#img_rgb = cv2.imread("images/kerekou.jpg")
#img_rgb = cv2.imread("images/yayi.jpg")
#img_rgb = cv2.imread("images/talon.jpg")
#img_rgb = cv2.imread("images/sagbohan.jpeg")
#img_rgb = cv2.imread("images/zeynab.jpeg")
#img_rgb = cv2.imread("images/sessime.jpg")
#img_rgb = cv2.imread("images/young-girl.jpg")
#img_rgb = cv2.imread("images/paturelhonvoh_Iwaria.jpeg")
#img_rgb = cv2.imread("images/dassa_benin.jpg")

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

img_gray_inv = 255 - img_gray
img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(19, 19),sigmaX=0, sigmaY=0)

def penciler(image, mask):
    return cv2.divide(image, 255-mask, scale=256)

img_blend = penciler(img_gray, img_blur)
cv2.imshow("Pencil sketch", img_blend)
cv2.waitKey(0)
cv2.destroyAllWindows()

