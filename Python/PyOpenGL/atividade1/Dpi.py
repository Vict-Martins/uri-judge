import cv2
import numpy as np
from matplotlib import pyplot as plt

import matplotlib
matplotlib.use('TkAgg')

#Abrindo a imagem cinza e tirando a mÃ©dia dos pixels
img = cv2.imread(r'C:\Program Files\Python\helena.jfif', 0)
new_img = cv2.imread(r'C:\Program Files\Python\helena.jfif', 0)

media = 0

linha = len(img)
coluna = len(img[0])

for i in range(0, linha):
    for l in range(0, coluna):
        #Primeira linha e primeira coluna
        if (i == 0 and l == 0):
            media = (int(img[i][l]) + int(img[i][l+1]) + int(img[i+1][l]))/3

        #Primeira linha e ultima coluna
        elif (i == 0 and l == coluna-1):
            media = (int(img[i][l]) + int(img[i][l-1]) + int(img[i+1][l]))/3

        #Ultima linha e primeira coluna
        elif (i == linha-1 and l == 0):
            media = (int(img[i][l]) + int(img[i][l+1]) + int(img[i-1][l]))/3

        #Ultima linha e ultima coluna
        elif (i == linha-1 and l == coluna-1):
            media = (int(img[i][l]) + int(img[i-1][l]) + int(img[i][l-1]))/3

        #Primeira linha
        elif (i == 0 and not(l == 0)):
            media = (int(img[i][l]) + int(img[i][l+1]) + int(img[i][l-1]) + int(img[i+1][l]))/4

        #Ultima linha
        elif (i == linha-1 and not(l == 0)):
            media = (int(img[i][l]) + int(img[i][l+1]) + int(img[i][l-1]) + int(img[i-1][l]))/4

        #Primeira coluna
        elif (not(l==0) and l == coluna):
            media = (int(img[i][l]) + int(img[i+1][l]) + int(img[i-1][l]) + int(img[i][l+1]))/4

        #Ultima coluna
        elif (not(i == 0) and l == coluna-1):
            media = (int(img[i][l]) + int(img[i+1][l]) + int(img[i-1][l]) + int(img[i][l-1]))/4

        #Resto
        else: 
            media = (int(img[i][l]) + int(img[i][l+1]) + int(img[i][l-1]) + int(img[i+1][l]) + int(img[i-1][l]))/5
        
        new_img[i][l] = int(media)


cv2.imshow('image',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
