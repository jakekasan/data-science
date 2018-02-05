import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image


img = cv2.imread("image.png",0)

plt.imshow(img,cmap = 'gray',interpolation = 'bicubic')
plt.xticks([])
plt.yticks([])
plt.show()

