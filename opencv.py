import numpy as np
import cv2
from matplotlib import pyplot as plt

objImg = cv2.imread("pato.jpeg", 0)

objImg = cv2.cvtColor(objImg, cv2.COLOR_BGR2RGB)

plt.imshow(objImg)
plt.show()


