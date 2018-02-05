import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('image.png',cv2.IMREAD_GRAYSCALE)

plt.imshow(img,cmap = 'gray',interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.plot([200,300,400],[100,200,300],'c',linewidth=5)
plt.show()

cv2.imwrite('MyIDgray.png',img)
