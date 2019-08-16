import cv2
import numpy as np

img=cv2.imread("12.png")

scaled_img=cv2.resize(img,None,fx=1,fy=2)

rows,cols,ch=img.shape
print(rows)
print(cols)

matrix=np.float32([[1,0,50],[0,1,50]])
translate_img=cv2.warpAffine(img,matrix,(cols,rows))
cv2.imshow("GeoTransformation",img)
cv2.imshow("scaled",scaled_img)
cv2.imshow("translated",translate_img)


cv2.waitKey(0)
    
       
    
cv2.distroyAllWindows()