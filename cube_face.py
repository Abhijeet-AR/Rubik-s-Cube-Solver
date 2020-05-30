#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:36:35 2019

@author: AR
"""

class Face:    
    def __init__(self, c, l, r, u, d, n = [0, 0]):
        self.colors = 3*[[c, c, c]]
        self.left = l
        self.right = r 
        self.up = u
        self.down = d
        self.n = n
        
        self.color = self.colors[1][1]
        
    def setSides(self, cube): 
        if self.left == 'blue': self.left = cube.blue
        elif self.left == 'red': self.left = cube.red
        elif self.left == 'green': self.left = cube.green
        elif self.left == 'orange': self.left = cube.orange
        elif self.left == 'white': self.left = cube.white
        elif self.left == 'yellow': self.left = cube.yellow
        
        if self.right == 'blue': self.right = cube.blue
        elif self.right == 'red': self.right = cube.red
        elif self.right == 'green': self.right = cube.green
        elif self.right == 'orange': self.right = cube.orange
        elif self.right == 'white': self.right = cube.white
        elif self.right == 'yellow': self.right = cube.yellow 
        
        if self.up == 'blue': self.up = cube.blue
        elif self.up == 'red': self.up = cube.red
        elif self.up == 'green': self.up = cube.green
        elif self.up == 'orange': self.up = cube.orange
        elif self.up == 'white': self.up = cube.white
        elif self.up == 'yellow': self.up = cube.yellow
        
        if self.down == 'blue': self.down = cube.blue
        elif self.down == 'red': self.down = cube.red
        elif self.down == 'green': self.down = cube.green
        elif self.down == 'orange': self.down = cube.orange
        elif self.down == 'white': self.down = cube.white
        elif self.down == 'yellow': self.down = cube.yellow
        
    def fRotateClock(self):
        '''
        temp = [0,0,0]
        
        for i,p in zip(self.colors[0], range(3)):
            temp[p] = i
       
        for i in range(3):
            self.colors[0][2-i] = self.colors[i][0]
                #colors[0][1] = colors[1][0]
                #colors[0][0] = colors[2][0]

        for i in range(1,3):
            self.colors[i][0] = self.colors[2][i]
                #colors[2][0] = colors[2][2]
       
        self.colors[2][1] = self.colors[1][2]
                #colors[0][2] = colors[1][2]
    
        for i,p in zip(temp, range(3)):
            self.colors[p][2] = i
        '''
        
        for i in range(2):
            temp = self.colors[0][i]
            self.colors[0][i] = self.colors[2-i][0]
            self.colors[2-i][0] = self.colors[2][2-i]
            self.colors[2][2-i] = self.colors[i][2]
            self.colors[i][2] = temp
    
    def eRotateClock(self):
        temp = [0,0,0]              
        
        if self.n[0] == 0:
            
            for i,p in zip(self.up.colors[self.n[1]], range(3)):
                temp[p] = i
            
            """
            if self.n[1] == 2:  
                for i in range(3):
                    self.up.colors[self.n[1]][2-i] = self.left.colors[i][2]
                
                #for i in range(3):
                    self.left.colors[i][2] = self.down.colors[self.n[1]-2][i]
                
                #for i in range(3):
                    self.down.colors[self.n[1]-2][i] = self.right.colors[2-i][0]
                
                #for i in range(3):
                    self.right.colors[2-i][0] = temp[2-i]
                    
            else:
                for i in range(3):
                    self.up.colors[self.n[1]][i] = self.left.colors[i][2]
                    
                #for i in range(3):
                    self.left.colors[i][2] = self.down.colors[self.n[1]+2][2-i]
                    
                #for i in range(3):
                    self.down.colors[self.n[1]+2][2-i] = self.right.colors[2-i][0]
                
                #for i in range(3):
                    self.right.colors[2-i][0] = temp[i]
            
            """  
            for i in range(3):
                
                if self.n[1] == 2:
                    a = 2-i
                    n = 0
                    b = i
                                        
                else:
                    a = i
                    n = 2
                    b = 2-i
                                    
                self.up.colors[self.n[1]][a] = self.left.colors[i][2]
                
                self.left.colors[i][2] = self.down.colors[n][b]
                     
                self.down.colors[n][b] = self.right.colors[2-i][0]
                
                self.right.colors[2-i][0] = temp[a]                    
            #"""  
        else:
            for i in range(3):
                temp[i] = self.up.colors[2-i][self.n[1]]
                
            '''
            if self.n[1] == 2:
                for i in range(3):
                    self.up.colors[i][self.n[1]] = self.left.colors[i][2]
                
                #for i in range(3):
                    self.left.colors[i][2] = self.down.colors[i][self.n[1]]
                
                #for i in range(3):
                    self.down.colors[i][self.n[1]] = self.right.colors[2-i][0]
                
                #for i in range(3):
                    self.right.colors[2-i][0] = temp[2-i]
                    
            else:
                for i in range(3):
                    self.up.colors[2-i][self.n[1]] = self.left.colors[i][2]
                  
                #for i in range(3):
                    self.left.colors[i][2] = self.down.colors[2-i][self.n[1]]
                    
                #for i in range(3):
                    self.down.colors[2-i][self.n[1]] = self.right.colors[2-i][0]
                    
                #for i in range(3):
                    self.right.colors[2-i][0] = temp[i]
                    
            '''
            
            for i in range(3):
                if self.n[1] == 2:
                    a = i
                    b = 2-i
                                        
                else:
                    a = 2-i
                    b = i
                                    
                self.up.colors[a][self.n[1]] = self.left.colors[i][2]
                
                self.left.colors[i][2] = self.down.colors[a][self.n[1]]
                
                self.down.colors[a][self.n[1]] = self.right.colors[2-i][0]
                
                self.right.colors[2-i][0] = temp[b] 
                
            #'''
                
    def uRotateClock(self):  
        for i in range(3):
            temp = self.up.colors[0][i]
            self.up.colors[0][i] = self.left.colors[0][i]
            self.left.colors[0][i] = self.down.colors[0][i]
            self.down.colors[0][i] = self.right.colors[0][i]
            self.right.colors[0][i] = temp
            
    def fRotateAntiClock(self):
         temp = []
         
         for i in range(2):
             temp.append(self.colors[0][i])
             self.colors[0][i] = self.colors[i][2]
             self.colors[i][2] = self.colors[2][2-i]
             self.colors[2][2-i] = self.colors[2-i][0]
             self.colors[2-i][0] = temp[i]
             
    def eRotateAntiClock(self):     
        if self.n[0] == 0:
            if self.n[1] == 2:
                for i in range(3): 
                    temp = self.up.colors[self.n[1]][i]
                    self.up.colors[self.n[1]][i] = self.right.colors[i][0]
                    self.right.colors[i][0] = self.down.colors[0][2-i]
                    self.down.colors[0][2-i] = self.left.colors[2-i][2]
                    self.left.colors[2-i][2] = temp
                                        
            else:
                 for i in range(3):    
                    temp = self.up.colors[self.n[1]][i]
                    self.up.colors[self.n[1]][i] = self.right.colors[2-i][0]
                    self.right.colors[2-i][0] = self.down.colors[2][2-i]
                    self.down.colors[2][2-i] = self.left.colors[i][2]
                    self.left.colors[i][2] = temp
                
        else:
            if self.n[1] == 2:
                for i in range(3):
                    temp = self.up.colors[i][self.n[1]]
                    self.up.colors[i][self.n[1]] = self.right.colors[2-i][0]
                    self.right.colors[2-i][0] = self.down.colors[i][2]
                    self.down.colors[i][2] = self.left.colors[i][2]
                    self.left.colors[i][2] = temp
                    
            else:
                for i in range(3):
                    temp = self.up.colors[i][self.n[1]]
                    self.up.colors[i][self.n[1]] = self.right.colors[i][0]
                    self.right.colors[i][0] = self.down.colors[i][0]
                    self.down.colors[i][0] = self.left.colors[2-i][2]
                    self.left.colors[2-i][2] = temp
       
    def uRotateAntiClock(self):  
        for i in range(3):
            temp = self.up.colors[0][i]
            self.up.colors[0][i] = self.right.colors[0][i]
            self.right.colors[0][i] = self.down.colors[0][i]
            self.down.colors[0][i] = self.left.colors[0][i]
            self.left.colors[0][i] = temp
            
    def dRotateClock(self):
        for i in range(3):
            temp = self.up.colors[2][i]
            self.up.colors[2][i] = self.left.colors[2][i]
            self.left.colors[2][i] = self.down.colors[2][i]
            self.down.colors[2][i] = self.right.colors[2][i]
            self.right.colors[2][i] = temp
     
    def dRotateAntiClock(self):  
         for i in range(3):
            temp = self.up.colors[2][i]
            self.up.colors[2][i] = self.right.colors[2][i]
            self.right.colors[2][i] = self.down.colors[2][i]
            self.down.colors[2][i] = self.left.colors[2][i]
            self.left.colors[2][i] = temp
            
    def mRotateClock(self):
        if self.n[0] == 0:
            face = self.right
            if self.n[1] == 2:
                for i in range(3):
                    temp = face.up.colors[i][1]
                    face.up.colors[i][1] = face.left.colors[i][1]
                    face.left.colors[i][1] = face.down.colors[i][1]
                    face.down.colors[i][1] = face.right.colors[2-i][1]
                    face.right.colors[2-i][1] = temp
                    
            else:
                for i in range(3):
                    temp = face.up.colors[2-i][1]
                    face.up.colors[2-i][1] = face.left.colors[i][1]
                    face.left.colors[i][1] = face.down.colors[2-i][1]
                    face.down.colors[2-i][1] = face.right.colors[2-i][1]
                    face.right.colors[2-i][1] = temp
                    
        else:
            face = self.right
            if self.n[1] == 2:
                for i in range(3):
                    temp = face.up.colors[1][i]
                    face.up.colors[1][i] = face.left.colors[i][1]
                    face.left.colors[i][1] = face.down.colors[1][2-i]
                    face.down.colors[1][2-i] = face.right.colors[2-i][1]
                    face.right.colors[2-i][1] = temp
                    
            else:
                for i in range(3):
                    temp = face.up.colors[1][i]
                    face.up.colors[1][i] = face.left.colors[2-i][1]
                    face.left.colors[2-i][1] = face.down.colors[1][2-i]
                    face.down.colors[1][2-i] = face.right.colors[i][1]
                    face.right.colors[i][1] = temp
                    
    def mRotateAntiClock(self):
        if self.n[0] == 0:
            face = self.right
            if self.n[1] == 2:
                for i in range(3):
                    temp = face.up.colors[i][1]
                    face.up.colors[i][1] = face.right.colors[2-i][1]
                    face.right.colors[2-i][1] = face.down.colors[i][1]
                    face.down.colors[i][1] = face.left.colors[i][1]
                    face.left.colors[i][1] = temp
                    
            else:
                for i in range(3):
                    temp = face.up.colors[2-i][1]
                    face.up.colors[2-i][1] = face.right.colors[2-i][1]
                    face.right.colors[2-i][1] = face.down.colors[2-i][1]
                    face.down.colors[2-i][1] = face.left.colors[i][1]
                    face.left.colors[i][1] = temp
                    
        else:
            face = self.right
            if self.n[1] == 2:
                for i in range(3):
                    temp = face.up.colors[1][i]
                    face.up.colors[1][i] = face.right.colors[2-i][1]
                    face.right.colors[2-i][1] = face.down.colors[1][2-i]
                    face.down.colors[1][2-i] = face.left.colors[i][1]
                    face.left.colors[i][1] = temp
                    
            else:
                for i in range(3):
                    temp = face.up.colors[1][i]
                    face.up.colors[1][i] = face.left.colors[2-i][1]
                    face.left.colors[2-i][1] = face.down.colors[1][2-i]
                    face.down.colors[1][2-i] = face.right.colors[i][1]
                    face.right.colors[i][1] = temp
                    
                for i in range(3):
                    temp = face.up.colors[1][i]
                    face.up.colors[1][i] = face.right.colors[i][1]
                    face.right.colors[i][1] = face.down.colors[1][2-i]
                    face.down.colors[1][2-i] = face.left.colors[2-i][1]
                    face.left.colors[2-i][1] = temp
            
