#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:53:29 2019

@author: AR
"""

import cv2
import numpy as np
import sys

class Color_Detect:
    def __init__(self):
        self.blue_face = None
        self.red_face = None
        self.green_face = None
        self.orange_face = None
        self.white_face = None
        self.yellow_face = None
        
        self.no_faces = 0
    
    def set_face(self, face):   
        color = face[1][1]
        
        if color == 'b':
            self.blue_face = face
            
        elif color == 'r':
            self.red_face = face
            
        elif color == 'g':
            self.green_face = face
            
        elif color == 'o':
            self.orange_face = face
            
        elif color == 'w':
            self.white_face = face
            
        else:
            self.yellow_face = face
            
        self.no_faces += 1
     
    def check_face(self, face):
        color = face[1][1]
        
        if color == 'b':
            return self.blue_face == None
            
        elif color == 'r':
            return self.red_face == None
            
        elif color == 'g':
            return self.green_face == None
            
        elif color == 'o':
            return self.orange_face == None
            
        elif color == 'w':
            return self.white_face == None
            
        else:
            return self.yellow_face == None
            
    
    def get_faces(self):
        cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        font2 = cv2.FONT_HERSHEY_SIMPLEX

        
        blue_lower = np.array([97, 100, 117])
        blue_upper = np.array([117,255,255])
            
        yellow_lower = np.array([22,60,200])
        yellow_upper = np.array([60,255,255])
        
        green_lower = np.array([40,40,40])
        green_upper = np.array([80,255,255])
        
        white_lower = np.array([0,0,230])
        white_upper = np.array([255,15,255])
        
        lower_red1 = np.array([0,50,125])
        upper_red1 = np.array([10,255,255])
        
        lower_red2 = np.array([170,50,125])
        upper_red2 = np.array([180,255,255])
        
        
        orange_lower = np.array([10, 150, 150])
        orange_upper = np.array([25, 255, 255])
        
        #    black_lower = np.array([0, 0, 0])
        #    black_upper = np.array([255, 255, 255])
        #    black = cv2.inRange(hsv, black_lower, black_upper)
#        prev_colors = ['e','e','e','e','e','e','e','e','e']
        
        while True:
            loc = []
#            curr_colors = []
            count = 0
            _, frame = cap.read()
            
#            blur_frame = cv2.GaussianBlur(frame, (25, 25), 0)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            blue = cv2.inRange(hsv, blue_lower, blue_upper)
            yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
            green = cv2.inRange(hsv, green_lower, green_upper)
            white = cv2.inRange(hsv, white_lower, white_upper)   
            mask0 = cv2.inRange(hsv, lower_red1, upper_red1)
            mask1 = cv2.inRange(hsv, lower_red2, upper_red2)
            red = mask1 + mask0
            orange = cv2.inRange(hsv, orange_lower, orange_upper)
            
        #    allColors = blue + red + green + orange + yellow + white
            
            _,contours,_=cv2.findContours(orange,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area = cv2.contourArea(contour)
                if area>2000:
                    approx = cv2.approxPolyDP(contour, 0.1*cv2.arcLength(contour, True), True)
                    
                    if len(approx) == 4:
                        (x, y, w, h) = cv2.boundingRect(approx)
                        ar = w/float(h)
                        if ar >= 0.8 and ar <= 1.2:
                            cv2.drawContours(frame, [approx], 0, (0,0,255), 5)
                            cv2.putText(frame, "Orange", (x, y), font, 0.75, (255,255,255))
                            loc.append([y+(h/2), x+(w/2), 'o'])
                            count+=1
               
        
                     
            _,contours,_=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area = cv2.contourArea(contour)
                if area>2000:
                    approx = cv2.approxPolyDP(contour, 0.1*cv2.arcLength(contour, True), True)
                    
                    if len(approx) == 4:
                        (x, y, w, h) = cv2.boundingRect(approx)
                        ar = w/float(h)
                        if ar >= 0.9 and ar <= 1.1:
                            cv2.drawContours(frame, [approx], 0, (0,0,255), 5)
                            cv2.putText(frame, "Red", (x, y), font, 0.75, (255,255,255))
                            loc.append([y+(h/2), x+(w/2), 'r'])
                            count+=1
        
                    
            _,contours,_=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area = cv2.contourArea(contour)
                if area>2000:
                    approx = cv2.approxPolyDP(contour, 0.1*cv2.arcLength(contour, True), True)
                    
                    if len(approx) == 4:
                        (x, y, w, h) = cv2.boundingRect(approx)
                        ar = w/float(h)
                        if ar >= 0.8 and ar <= 1.2:
                            cv2.drawContours(frame, [approx], 0, (0,0,255), 5)
                            cv2.putText(frame, "Yellow", (x, y), font, 0.75, (255,255,255))
                            loc.append([y+(h/2), x+(w/2), 'y'])
                            count+=1
        
                    
            _,contours,_=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area = cv2.contourArea(contour)
                if area>2000:
                    approx = cv2.approxPolyDP(contour, 0.1*cv2.arcLength(contour, True), True)
                    
                    if len(approx) == 4:
                        (x, y, w, h) = cv2.boundingRect(approx)
                        ar = w/float(h)
                        if ar >= 0.8 and ar <= 1.2:
                            cv2.drawContours(frame, [approx], 0, (0,0,255), 5)
                            cv2.putText(frame, "Green", (x, y), font, 0.75, (255,255,255))
                            loc.append([y+(h/2), x+(w/2), 'g'])
                            count+=1
                    
                    
            _,contours,_=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area = cv2.contourArea(contour)
                if area>2000:
                    approx = cv2.approxPolyDP(contour, 0.1*cv2.arcLength(contour, True), True)
                    
                    if len(approx) == 4:
                        (x, y, w, h) = cv2.boundingRect(approx)
                        ar = w/float(h)
                        if ar >= 0.8 and ar <= 1.2:
                            cv2.drawContours(frame, [approx], 0, (0,0,255), 5)
                            cv2.putText(frame, "Blue", (x, y), font, 0.75, (255,255,255))
                            loc.append([y+(h/2), x+(w/2), 'b'])
                            count+=1
                    
                    
            _,contours,_=cv2.findContours(white,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area = cv2.contourArea(contour)
                if area>2000:
                    approx = cv2.approxPolyDP(contour, 0.1*cv2.arcLength(contour, True), True)
                    
                    if len(approx) == 4:
                        (x, y, w, h) = cv2.boundingRect(approx)
                        ar = w/float(h)
                        if ar >= 0.8 and ar <= 1.2:
                            cv2.drawContours(frame, [approx], 0, (0,0,255), 5)
                            cv2.putText(frame, "White", (x, y), font, 0.75, (255,255,255))
                            loc.append([y+(h/2), x+(w/2), 'w'])
                            count+=1
            
            
        #    _,contours,_=cv2.findContours(allColors,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #    for contour in contours:
        #        area = cv2.contourArea(contour)
        #        if area>2000:
        #            approx = cv2.approxPolyDP(contour, 0.1*cv2.arcLength(contour, True), True)
        #            
        #            if len(approx) == 4:
        #                (x, y, w, h) = cv2.boundingRect(approx)
        #                ar = w/float(h)
        #                if ar >= 0.8 and ar <= 1.2:
        #                    cv2.putText(frame, "White", (x, y), font, 1, (255,255,255))
        #                    cv2.drawContours(frame, [approx], 0, (0,0,255), 5)
        #    
            
            
            cv2.putText(frame, 'Blue' if self.blue_face != None else 'None', (50, 50), font2 , 1, (0,0,0))
            cv2.putText(frame, 'Red' if self.red_face != None else 'None', (50, 80), font2, 1, (0,0,0))
            cv2.putText(frame, 'Green' if self.green_face != None else 'None', (50, 110), font2, 1, (0,0,0))
            cv2.putText(frame, 'Orange' if self.orange_face != None else 'None', (50, 140), font2, 1, (0,0,0))
            cv2.putText(frame, 'White' if self.white_face != None else 'None', (50, 170), font2, 1, (0,0,0))
            cv2.putText(frame, 'Yellow' if self.yellow_face != None else 'None', (50, 200), font2, 1, (0,0,0))
            
            if count == 9:
                loc.sort()
                top_row = []
                mid_row = []
                bot_row = []
                
        #        count = 0
        #        for (y,x,c) in loc:
        #            if count < 3:
        #                top_row.append([x,y,c])
        #                top_row.sort()
        #                
        #            elif count < 6:
        #                mid_row.append([x,y,c])
        #                mid_row.sort()
        #                
        #            elif count < 9:
        #                bot_row.append([x,y,c])
        #                bot_row.sort()
        #                
        #            count+=1
                for (y,x,c) in loc[0:3]:
                    top_row.append([x,y,c])
                    top_row.sort()
                 
                for (y,x,c) in loc[3:6]:
                    mid_row.append([x,y,c])
                    mid_row.sort()
                
                for (y,x,c) in loc[6:9]:
                    bot_row.append([x,y,c])
                    bot_row.sort()
                                        
                face = [list(map(lambda x: top_row[x][2] , [0,1,2])), 
                        list(map(lambda x: mid_row[x][2] , [0,1,2])),
                        list(map(lambda x: bot_row[x][2] , [0,1,2]))]
                
                if self.check_face(face):
                    self.set_face(face)
                    
#                if prev_colors[4] != curr_colors[4]:
#                    print(curr_colors)
#                prev_colors = curr_colors
            
            
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(20)
            if key == 27 or self.no_faces == 6:
                cap.release()
                cv2.destroyAllWindows()
                if self.no_faces != 6:
                    return None
                    
                return (self.blue_face, 
                        self.red_face, 
                        self.green_face, 
                        self.orange_face, 
                        self.white_face, 
                        self.yellow_face)
            
    def abc(self):
        blueColors = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
        redColors = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
        greenColors = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
        orangeColors = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
        whiteColors = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
        yellowColors = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
        return (blueColors, redColors, greenColors, orangeColors, whiteColors, yellowColors)
      
def main():
    c = Cube()
    
    cd = Color_Detect()

    (blueColors, redColors, greenColors, orangeColors, whiteColors, yellowColors) = cd.get_faces()
    
    
    c.sendScramble(blueColors, redColors, greenColors, orangeColors, whiteColors, yellowColors)
    c.display()
    
if __name__ == '__main__':
    from rubiks_cube import Cube
    main()