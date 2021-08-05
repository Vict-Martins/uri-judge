#Escala de Cinza

import cv2
import numpy as np
from matplotlib import pyplot as plt

import matplotlib
matplotlib.use('TkAgg')
img = cv2.imread(r'C:\Program Files\Python\helena.jfif', 0)# abrir a imagem
media_imagem = int(img.mean()) #tirando e média

# transformando em cinza
for i in range(0, len(img)):
    for l in range(0, len(img[i])):
        if img[i][l] < media_imagem:
            img[i][l] = 0
        else:
            img[i][l] = 255

cv2.imshow('ImagemBinária',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
