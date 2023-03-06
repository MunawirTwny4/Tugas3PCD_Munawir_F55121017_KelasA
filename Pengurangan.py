import cv2
import numpy as np

img1 = cv2.imread('Pengurangan1.jpg')
img1 = cv2.resize(img1, (800, 325 ))
img2 = cv2.imread('Pengurangan2.jpg')
img2 = cv2.resize(img2, (800, 325 ))

sub_img = np.subtract(img1, img2)

cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Subtracted Image", sub_img)

cv2.waitKey(0)
cv2.destroyAllWindows()