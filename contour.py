import cv2
import numpy as np

img=cv2.imread('village.png')
img=cv2.resize(img, (300,300))
cv2.imshow("original", img)
imggray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imggray,50,255,0)
contour,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #TO FIND CONTOUR
print("NUMBER OF CONTOURS="+str(len(contour))) #print the total no. of contours found in image
print(contour[0])#to print the contours coordinates
cv2.drawContours(img,contour,-1,(0,0,255),2)#to draw contour on original image
cv2.imshow("contour", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
