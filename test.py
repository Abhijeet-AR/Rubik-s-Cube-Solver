#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:54:30 2019

@author: AR
"""

import cv2
import numpy as np

def get_color(image):
    image = image.reshape(image.shape[0]*image.shape[1],3)
    clf = cv2.kmeans(n_clusters = 1)
    labels = clf.fit_predict(image)
    
    counts = cv2.Counter(labels)
    
    center_colors = clf.cluster_centers_
    
    ordered_colors = [center_colors[i]/255 for i in counts.keys()]
    rgb_colors = [ordered_colors[i]*255 for i in counts.keys()]
    
    print(rgb_colors)

img = cv2.imread('/Users/AR/Desktop/Screenshot 2019-04-27 at 9.45.14 PM.png', cv2.IMREAD_COLOR)
#img = cv2.resize(img, (1280,800))
font = cv2.FONT_HERSHEY_SIMPLEX
#roi = img[110:340, 95:300]
#
#print(roi)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

green_lower = np.array([40,40,40])
green_upper = np.array([80,255,255])
green = cv2.inRange(hsv, green_lower, green_upper)

blue_lower = np.array([97, 100, 117])
blue_upper = np.array([117,255,255])
blue = cv2.inRange(hsv, blue_lower, blue_upper)

white_lower = np.array([0,0,230])
white_upper = np.array([255,15,255])
white = cv2.inRange(hsv, white_lower, white_upper)

_,contours_green,_=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
_,contours_blue,_=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#_,contours,_=cv2.findContours(white,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#for contour in contours:
#    area = cv2.contourArea(contour)
#    if area>300 and area<3000:
#        x,y,w,h = cv2.boundingRect(contour)     
#        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)  

#for contour in contours_blue:
#    area = cv2.contourArea(contour)
#    if area>300:
#        approx = cv2.approxPolyDP(contour, 0.05*cv2.arcLength(contour, True), True)
#        cv2.drawContours(img, [approx], -1, (0,0,255), 5)   
#        x = approx.ravel()[0]
#        y = approx.ravel()[1]
#        if len(approx) == 4:
#            cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
            
for contour in contours_green:
    area = cv2.contourArea(contour)
    if area>300:
        approx = cv2.approxPolyDP(contour, 0.1*cv2.arcLength(contour, True), True)
        
        if len(approx) == 4:
                (x, y, w, h) = cv2.boundingRect(approx)
                ar = w/float(h)
                if ar >= 0.8 and ar <= 1.2:
                    cv2.putText(img, "Green", (x, y), font, 1, (255,255,255))
                    cv2.drawContours(img, [approx], 0, (0,255,0), 60)
                    x = int(x)
                    y = int(y)
                    cube = img[y-20:y+20, x-20:x+20]
#                    cube = cv2.resize(cube, (10,10))
#                    cube = cv2.cvtColor(cube, cv2.COLOR_BGR2YUV)
                    cv2.imshow('cube', cube)
                    (Y,U,V,DA)= cv2.mean(cube)
                    print((Y,U,V,DA))
                    if Y > 120 and float(U/V)>0.9 :	   
                        print('W')
                    elif U > 130 and U > V and float (U/Y)> 1.15:
                    	   print("B")	   
                    elif float(U/V) > 1.1 and float(U/V) < 2:
                    	   print("G")
                    elif V > 120 and float (U/Y) > 0.7:
                        if float(U/Y) < 1.9:
                            print("O")
                        else:
                            print('R')
                            
                    elif Y > 110 and float(V/U)>0.95:
                        print('Y')
                    
                    


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()







