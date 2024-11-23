import cv2
import numpy as np

imagen = cv2.imread('C:/Users/manue/Downloads/python/media/circulos.jpg')
cv2.imshow('Imagen original', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()