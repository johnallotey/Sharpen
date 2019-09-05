import numpy as np
import cv2
# import dateutil
# from matplotlib import pyplot as plt
# print cv2.__version__
img = cv2.imread('wall.png')
# median = cv2.medianBlur(img,5)
dst = cv2.fastNlMeansDenoisingColored(img,img,8,8,7,21)
cv2.imwrite('new2.png',dst)
# cv2.imshow('image',img)
# print dst
# kernel = np.ones((5,5),np.float32)/25
# dst = cv2.filter2D(img,-1,kernel)
# blur = cv2.blur(img,(5,5))
# plt.subplot(121),plt.imshow(img)
# plt.subplot(122),plt.imshow(dst)
# plt.show()