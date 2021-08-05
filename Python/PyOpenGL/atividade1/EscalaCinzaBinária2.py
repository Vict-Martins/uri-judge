#Diversas escalas de Cinza

import cv2
import numpy as np

img = cv2.imread(r'C:\Program Files\Python\helena.jfif',0)

adp1 = cv2.adaptiveThreshold(img, 256, cv2.ADAPTIVE_THRESH_MEAN_C, \
                             cv2.THRESH_BINARY, 11, 15)
adp2 = cv2.adaptiveThreshold(img, 256, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                             cv2.THRESH_BINARY, 11, 15)
adp3 = cv2.adaptiveThreshold(img, 256, cv2.ADAPTIVE_THRESH_MEAN_C, \
                             cv2.THRESH_BINARY, 11, 0)
adp4 = cv2.adaptiveThreshold(img, 256, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                             cv2.THRESH_BINARY, 11, 0)
cv2.imshow("original", img)
cv2.imshow("limiarizacao adp media", adp1)
cv2.imshow("limiarizacao adp gaussiana", adp2)
cv2.imshow("limiarizacao adp media 1", adp3)
cv2.imshow("limiarizacao adp gaussiana 2", adp4)

cv2.waitKey(0)
cv2.destroyAllWindows()


