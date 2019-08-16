import matplotlib.pyplot as plt

import cv2
import numpy as np
img =cv2.imread('12.png',0)
_,mask=cv2.threshold(img,220,250,cv2.THRESH_BINARY_INV)#THIS IS OUR MASK THEN LOAD TO THE MATPLOT LIB
kernel=np.ones((5,5),np.uint8)

dilation=cv2.dilate(mask,kernel,iterations=2)
erosion=cv2.erode(mask,kernel,iterations=1)
opening =cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
closign =cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

titles=['images','mask','dilation','erosion','opening','closing']
images=[img,mask,dilation,erosion,opening,closign]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.xticks([])
    plt.yticks([])
    plt.title(titles[i])
plt.show()






