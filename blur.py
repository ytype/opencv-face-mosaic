import cv2
import numpy as np
import matplotlib.pylab as plt
img = cv2.imread('test.jpg')
k = 20
kernel = np.ones((k, k)) / k**2
filtering = cv2.filter2D(img, -1, kernel)
plt.imshow(filtering)
plt.show()
