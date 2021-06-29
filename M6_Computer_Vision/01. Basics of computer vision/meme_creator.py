'''
Level 1
1. Create a basic Meme creator with one image 
and a short line of text, using any openCV font
'''
import cv2
import numpy as np

#importing a image
img = cv2.imread('annotations.jpg')

#creating a copy
clone = img.copy()

#draw a rectangle with green color
green =(0,255,0)
cv2.rectangle(clone,(100,200),(400,500), green, 3)
cv2.imshow("nice", clone)
cv2.waitKey(0)









