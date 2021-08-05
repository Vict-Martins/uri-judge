#Gerando Histograma da imagem

import cv2
import numpy as np
from matplotlib import pyplot as pl


img = cv2.imread(r'C:\Program Files\Python\helena.jfif',0)# abre o arquivo
pl.hist(img.ravel(), 256, [0, 256]) # img.ravel() retorna um matriz da imagem, img.hist() retorna um histograma, com parametros limitadores que no caso é 0, 256
cv2.imshow("Imagem Original", img) #abre a imagem original
pl.show() # abre o histograma
