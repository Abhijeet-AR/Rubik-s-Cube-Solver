#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:28:51 2019

@author: AR
"""


class Face:    
    def __init__(self, c, l, r, u , d, n = [0, 0]):
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
            
                

class Cube:    
    def __init__(self):
        self.noOfSteps = 0
        self.colorCount = [0, 0, 0, 0, 0, 0]
        #self.edges = [[0, 1], [1, 0], [1, 2], [2, 1]]
        #self.corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
        
        self.blue = Face('b', 'orange', 'red', 'yellow', 'white', [0, 2])
        self.red = Face('r', 'blue', 'green','yellow', 'white', [1, 2])
        self.green = Face('g', 'red', 'orange','yellow', 'white', [0, 0])
        self.orange = Face('o', 'green', 'blue','yellow', 'white', [1, 0])
        self.white = Face('w', 'orange', 'red', 'blue', 'green', [0, 2])
        self.yellow = Face('y', 'orange', 'red', 'green', 'blue', [0, 0])  
        
        self.blue.setSides(self)
        self.red.setSides(self)
        self.green.setSides(self)
        self.orange.setSides(self)
        self.white.setSides(self)
        self.yellow.setSides(self)
        
        self.up = self.yellow
        self.down = self.white
        
    def sendScramble(self, blueFace, redFace, greenFace, orangeFace, whiteFace, yellowFace):
        
        self.blue.colors = blueFace
        self.red.colors = redFace
        self.green.colors = greenFace
        self.orange.colors = orangeFace
        self.white.colors = whiteFace
        self.yellow.colors = yellowFace
        
        if not self.perfectCube():
            self.display()
            print('Not a Perfect Cube, resetting......')
            self.reset()
            
    def reset(self):
        self.blue.colors = 3*[['b', 'b', 'b']]
        self.red.colors = 3*[['r', 'r', 'r']]
        self.green.colors = 3*[['g', 'g', 'g']]
        self.orange.colors = 3*[['o', 'o', 'o']]
        self.white.colors = 3*[['w', 'w', 'w']]
        self.yellow.colors = 3*[['y', 'y', 'y']]
        
    def perfectCube(self):
        self.colorCount = [0, 0, 0, 0, 0, 0]
        
        self.faceColorCount(self.blue.colors)
        self.faceColorCount(self.red.colors)
        self.faceColorCount(self.green.colors)
        self.faceColorCount(self.orange.colors)
        self.faceColorCount(self.white.colors)
        self.faceColorCount(self.yellow.colors)
        #print(self.colorCount)
        return self.colorCount == 6*[9]
            
    def faceColorCount(self, face):
        for row in face:
            for color in row:
                if color == 'b':
                    self.colorCount[0] += 1
            
                elif color == 'r':
                    self.colorCount[1] += 1
                
                elif color == 'g':
                    self.colorCount[2] += 1
                
                elif color == 'o':
                    self.colorCount[3] += 1
                
                elif color == 'w':
                    self.colorCount[4] += 1
                
                elif color == 'y':
                    self.colorCount[5] += 1
                
    
    def display(self):
    
        print('Blue Face : ')
        for i in self.blue.colors:
            print(i)
        
        print()
    
        print('Red Face : ')    
        for i in self.red.colors:
            print(i)
        
        print()
     
        print('Green Face : ')
        for i in self.green.colors:
            print(i)
        
        print()
     
        print('Orange Face : ')
        for i in self.orange.colors:
            print(i)
        
        print()
    
        print('White Face : ')
        for i in self.white.colors:
            print(i)
        
        print()
     
        print('Yellow Face : ')
        for i in self.yellow.colors:
            print(i)
        
        print()

    
    
    def shift(self, face, steps):
        
        print(face.color, steps)
        for s in steps:
            self.noOfSteps += 1
            if s == 'R':
                face.right.eRotateClock()
                face.right.fRotateClock()
            
            elif s == 'L':
                face.left.eRotateClock()
                face.left.fRotateClock()
                
            elif s == 'U':
                face.up.uRotateClock()
                face.up.fRotateClock()
            
            elif s == 'R1':
                face.right.fRotateAntiClock()
                face.right.eRotateAntiClock()
            
            elif s == 'L1':
                face.left.fRotateAntiClock()
                face.left.eRotateAntiClock()
            
            elif s == 'U1':
               face.up.fRotateAntiClock()
               face.up.uRotateAntiClock()
               
            elif s == 'D':
                face.down.fRotateClock()
                face.down.dRotateClock()
    
            elif s =='D1':
                face.down.fRotateAntiClock()
                face.down.dRotateAntiClock()
                
            elif s == 'F':
                face.fRotateClock()
                face.eRotateClock()
                
            elif s == 'F1':
                face.fRotateAntiClock()
                face.eRotateAntiClock()
                
                
    def isSolved(self):
        count  = 0
        
        if self.blue.colors == 3*[['b', 'b', 'b']]:
            count = count+1
        if self.red.colors == 3*[['r', 'r', 'r']]:
            count = count+1
        if self.green.colors == 3*[['g', 'g', 'g']]:
            count = count+1
        if self.orange.colors == 3*[['o', 'o', 'o']]:
            count = count+1
        if self.white.colors == 3*[['w', 'w', 'w']]:
            count = count+1
        if self.yellow.colors == 3*[['y', 'y', 'y']]:
            count = count+1
            
        return count == 6
    
    def solve(self):
        self.solveRow1()
        #c.display()

        self.solveRow2()
        #c.display()
        
        self.solveRow3()
        #c.display()
        print('Done')
        
    def solveRow1(self):  
        base = self.down.color
        face = self.blue
        cmd = ['R', 'U', 'R1']
        
        while  base != self.down.colors[0][1] or base != self.down.colors[1][0] or base != self.down.colors[1][2] or base != self.down.colors[2][1]: 
        #for i in range(10):
           self.searchEdge(face)
           face = face.right
           
        print('Cross Solved')
        
        down = self.down
        
        self.solveCorners()
               
        if down.up.colors[2][2] != down.up.color:
            self.shift(down.up, cmd)
            self.cornerUp(down.left)
                
        if down.right.colors[2][2] != down.right.color:
            self.shift(down.right, cmd)
            self.cornerUp(down.up)
          
        if down.down.colors[2][2] != down.down.color: 
            self.shift(down.down, cmd)
            self.cornerUp(down.right)
            
        if down.left.colors[2][2] != down.left.color:
            self.shift(down.left, cmd)
            self.cornerUp(down.down)
                
        self.solveCorners()
                  
        print('1st Row Solved')
        
           
    def solveCorners(self):
        base = self.down.color
        face = self.blue
        while base != self.down.colors[0][0] or base != self.down.colors[0][2] or base != self.down.colors[2][0] or base != self.down.colors[2][2]:
        #for i in range(20):
            self.searchCorner(face)  
            face = face.right
            
    def searchEdge(self, face):
        base = self.down.color
        
        if face.colors[0][1] == base:
            if face.n[0] == 0:
                adj = face.up.colors[face.n[1]][1]
                
            else:
                adj = face.up.colors[1][face.n[1]]
                
            if face.left.color == adj:
                self.shift(face, ['F1', 'L'])
                if face.right.colors[1][0] == base and face.colors[1][2] == face.color:
                    self.shift(face, ['F'])
                             
            elif face.right.color == adj:
                self.shift(face, ['F', 'R1'])
                if face.left.colors[1][2] == base and face.colors[1][0] == face.color:
                    self.shift(face, ['F1'])
                    
            elif face.color == adj:
                self.shift(face, ['U1', 'R1', 'F'])
                if face.right.right.colors[1][0] == base and face.right.colors[1][2] == face.right.color:
                    self.shift(face, ['R'])
                    
            else:
                self.shift(face, ['U1', 'R'])
                self.shift(face.right, ['R1'])
                
                if face.colors[1][2] == base and face.right.colors[1][0] == face.right.color:
                     self.shift(face, ['R1'])                 
                     
        if face.colors[1][0] == base:
            adj = face.left.colors[1][2]
            
            if face.left.color == adj:
                self.shift(face, ['L'])
                
            elif face.right.color == adj:
                self.shift(face, 2*['F']+['R1'])
                if face.colors[0][1] == face.color:
                    if (face.n[0] == 0 and face.up.colors[face.n[1]][1] == base) or (face.n[0] == 1 and face.up.colors[1][face.n[1]] == base):
                        self.shift(face, 2*['F1'])
                        
            elif face.color == adj:
                self.shift(face, ['L1', 'U1'])
                if face.colors[1][0] == base and face.left.colors[1][2] == face.left.color:
                    self.shift(face, ['L'])
                    
                self.shift(face, 2*['F'])
                    
            else:
                self.shift(face, ['L1', 'U'])
                if face.colors[1][0] == base and face.left.colors[1][2] == face.left:
                    self.shift(face, ['L'])
                    
                self.shift(face.right, 2*['R'])
                
        if face.colors[1][2] == base:
            adj = face.right.colors[1][0]
            
            if face.right.color == adj:
                self.shift(face, ['R1'])
                
            elif face.left.color == adj:
                self.shift(face, 2*['F1']+['L'])
                if face.colors[0][1] == face.color:
                    if (face.n[0] == 0 and face.up.colors[face.n[1]][1] == base) or (face.n[0] == 1 and face.up.colors[1][face.n[1]] == base):
                        self.shift(face, 2*['F1'])
                        
            elif face.color == adj:
                self.shift(face, ['R', 'U'])
                if face.colors[1][2] == base and face.right.colors[1][0] == face.right.color:
                    self.shift(face, ['R1'])
                        
                self.shift(face, 2*['F'])
                    
            else:
                self.shift(face, ['R', 'U1'])
                if face.colors[1][2] == base and face.right.colors[1][0] == face.right.color:
                    self.shift(face, ['R1'])
                    
                self.shift(face.right, 2*['R'])
                
        if (face.n[0] == 0 and face.up.colors[face.n[1]][1] == base) or (face.n[0] == 1 and face.up.colors[1][face.n[1]] == base):
            adj = face.colors[0][1]
            
            if face.color == adj:
                self.shift(face, 2*['F'])
                
            elif face.right.color == adj:
                self.shift(face, ['U1'] + 2*['R'])
                
            elif face.left.color == adj:
                self.shift(face, ['U'] + 2*['L'])
                
            else:
                self.shift(face, 2*['U'])
                self.shift(face.right, 2*['R'])
               
        if face.colors[2][1] == base:
            self.shift(face, 2*['F']+['U1', 'R1', 'F'])
            if face.right.colors[1][2] == face.right.color and face.right.right.colors[1][0] == base:
                self.shift(face, ['R'])
            
    def searchCorner(self, face):
        base = face.down.color
        if face.colors[2][2] == base:
            self.shift(face, ['F1', 'U1', 'F', 'U'])
            self.cornerUp(face)
            
        if face.colors[2][0] == base:
            self.shift(face, ['F', 'U', 'F1', 'U1'])
            self.cornerUp(face)
            
        top = face.up 
        if top.colors[0][0] == base:
            adj = top.left.colors[0][0]
            if adj == top.up.color:
                self.shift(top.up, ['R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
            if adj == top.left.color:
                self.shift(top.left, ['U1', 'R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
            if adj == top.right.color:
                self.shift(top.right, ['U', 'R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
            if adj == top.down.color:
                self.shift(top.down, ['U', 'U', 'R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
        if top.colors[0][2] == base:
            adj = top.up.colors[0][0]
            if adj == top.up.color:
                self.shift(top.up, ['U1', 'R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
            if adj == top.left.color:
                self.shift(top.left, ['U', 'U', 'R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
            if adj == top.right.color:
                self.shift(top.right, ['R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
            if adj == top.down.color:
                self.shift(top.down, ['U', 'R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
        if top.colors[2][0] == base:
            adj = top.down.colors[0][0]
            if adj == top.up.color:
                self.shift(top.up, ['U', 'R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
            if adj == top.left.color:
                self.shift(top.left, ['R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
            if adj == top.right.color:
                self.shift(top.right, ['U', 'U', 'R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
            if adj == top.down.color:
                self.shift(top.down, ['U1', 'R', 'U', 'U', 'R1'])
                self.cornerUp(face)     
                
        if top.colors[2][2] == base:
            adj = top.right.colors[0][0]
            if adj == top.up.color:
                self.shift(top.up, ['U', 'U', 'R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
            if adj == top.left.color:
                self.shift(top.left, ['U', 'R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
            if adj == top.right.color:
                self.shift(top.right, ['U1', 'R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
            if adj == top.down.color:
                self.shift(top.down, ['R', 'U', 'U', 'R1'])
                self.cornerUp(face)
                
        self.cornerUp(face)
        
                
    def cornerUp(self, face):
        base = face.down.color
        
        if face.colors[0][0] == base:
            adj = face.left.colors[0][2]
            if adj == face.color:
                self.shift(face, ['U', 'F1']+2*['U']+['F'])
                
            elif adj == face.left.color:
                 self.shift(face, ['U1', 'L1', 'U', 'L'])
                 
                 
            elif adj == face.right.color:
                 self.shift(face, ['R1']+2*['U']+['R'])
                 
            else:
                self.shift(face.left, ['L1', 'U', 'L'])
        
        if face.colors[0][2] == base:
            adj = face.right.colors[0][0]
            if adj == face.color:
                self.shift(face, 2*['U']+ ['F', 'U1', 'F1'])
                
            elif adj == face.left.color:
                self.shift(face, ['L'] + 2*['U']+ ['L1'])
                
            elif adj == face.right.color:
                self.shift(face, ['U', 'R', 'U1', 'R1'])
                
            else:
                self.shift(face.right, ['R', 'U1', 'R1'])
            
            
        
    def solveRow2(self):
        # = self.up.color
        
        self.searchF2U()
                
        while not self.checkRow2():
            self.searchF2U()
        
        print('Row 2 Solved')
            
    def checkRow2(self):
        
        count = 0        
        face = self.blue;
        
        for i in range(4):
            if face.colors[1][2] != face.color:
                self.shift(face, ['U', 'R', 'U1', 'R1', 'U1', 'F1', 'U', 'F'])
                
            else:
                count += 1
                
            face = face.right
        
        return count == 4
        
    def searchF2U(self):
        top = self.up
        topColor = top.color
        
        left = ['U1', 'L1', 'U', 'L', 'U', 'F', 'U1', 'F1']
        right = ['U', 'R', 'U1', 'R1', 'U1', 'F1', 'U', 'F']
        
        for i in range(10):
            count = 0
            
            color = top.colors[0][1]
            adj = top.up.colors[0][1]
            if color != topColor and adj != topColor:      
                if adj == top.up.color:
                    if color == top.left.color:
                        self.shift(top.up, right)
                        
                    else:
                        self.shift(top.up, left)
                        
                elif adj == top.left.color:
                    if color == top.up.color:
                        self.shift(top.left, ['U1']+left)
                        
                    else:
                        self.shift(top.left, ['U1']+right)
                    
                elif adj == top.right.color:
                    if color == top.up.color:
                        self.shift(top.right, ['U']+right)
                        
                    else:
                        self.shift(top.right, ['U']+left)
                        
                else:
                    if color == top.right.color:
                        self.shift(top.down, 2*['U']+right)
                        
                    else:
                        self.shift(top.down, 2*['U']+left)
            
            else:
                count+=1
                
            
            color = top.colors[1][0]
            adj = top.left.colors[0][1]
            if color != topColor and adj != topColor:
                
                if adj == top.left.color:
                    if color == top.down.color:
                        self.shift(top.left, right)
                        
                    else:
                        self.shift(top.left, left)
                        
                elif adj == top.down.color:
                    if color == top.left.color:
                        self.shift(top.down, ['U1']+left)
                        
                    else:
                        self.shift(top.down, ['U1']+right)
                    
                elif adj == top.up.color:
                    if color == top.left.color:
                        self.shift(top.up, ['U']+right)
                        
                    else:
                        self.shift(top.up, ['U']+left)
                        
                else:
                    if color == top.up.color:
                        self.shift(top.right, 2*['U']+right)
                        
                    else:
                        self.shift(top.right, 2*['U']+left)
            else:
                count+=1
                
            color = top.colors[1][2]
            adj = top.right.colors[0][1]
            if color != topColor and adj != topColor:
                
                if adj == top.right.color:
                    if color == top.up.color:
                        self.shift(top.right, right)
                        
                    else:
                        self.shift(top.right, left)
                        
                elif adj == top.up.color:
                    if color == top.right.color:
                        self.shift(top.up, ['U1']+left)
                        
                    else:
                        self.shift(top.up, ['U1']+right)
                    
                elif adj == top.down.color:
                    if color == top.right.color:
                        self.shift(top.down, ['U']+right)
                        
                    else:
                        self.shift(top.down, ['U']+left)
                        
                else:
                    if color == top.down.color:
                        self.shift(top.left, 2*['U']+right)
                        
                    else:
                        self.shift(top.left, 2*['U']+left)
            else:
                count+=1
                
            color = top.colors[2][1]
            adj = top.down.colors[0][1]
            if color != topColor and adj != topColor:
                if adj == top.down.color:
                    if color == top.right.color:
                        self.shift(top.down, right)
                        
                    else:
                        self.shift(top.down, left)
                        
                elif adj == top.right.color:
                    if color == top.down.color:
                        self.shift(top.right, ['U1']+left)
                        
                    else:
                        self.shift(top.right, ['U1']+right)
                    
                elif adj == top.left.color:
                    if color == top.down.color:
                        self.shift(top.left, ['U']+right)
                        
                    else:
                        self.shift(top.left, ['U']+left)
                        
                else:
                    if color == top.left.color:
                        self.shift(top.up, 2*['U']+right)
                        
                    else:
                        self.shift(top.up, 2*['U']+left)
            else:
                count+=1
                
            if count == 4:
                break;
                
        
    def solveRow3(self):
        self.solvePlus()
        print('Plus Solved')
        self.solveEdges()
        print('Edges Solve')
        self.matchCorners()
        print('Corners Matched')
        
        if self.isSolved():
            return
        
        face = self.blue
        
        for i in range(4):
            if face.colors[0][0] != face.colors[0][1]:
                break
            
            face = face.right
        
        for i in range(4):        
            while face.colors[0][0] != face.colors[0][1] or face.left.colors[0][2] != face.left.colors[0][1]:
                self.shift(face, ['L', 'D', 'L1', 'D1'])
            
            self.shift(face, ['U'])
            
    def solvePlus(self):
        top = self.up
        topColor = top.color
                
        if top.colors[0][1] == topColor and top.colors[1][0] == topColor and top.colors[1][2] == topColor and top.colors[2][1] == topColor:
            return
        
        if top.colors[1][0] == topColor:
            if top.colors[0][1] == topColor:
                self.shift(top.down, ['F']+ 2*['R', 'U', 'R1', 'U1'] +['F1'])
                return 
            
            elif top.colors[1][2] == topColor:
                self.shift(top.down, ['F', 'R', 'U', 'R1', 'U', 'F1'])
                return

        if top.colors[2][1] == topColor:
            if top.colors[1][0] == topColor:
                self.shift(top.right, ['F']+ 2*['R', 'U', 'R1', 'U1'] +['F1'])
                return
            
            elif top.colors[0][1] == topColor:
                self.shift(top.right, ['F', 'R', 'U', 'R1', 'U1', 'F1'])
                return
            
        if top.colors[1][2] == topColor:
            if top.colors[2][1] == topColor:
                self.shift(top.up, ['F']+ 2*['R', 'U', 'R1', 'U1'] +['F1'])
                return
            
            elif top.colors[1][0] == topColor:
                self.shift(top.up, ['F', 'R', 'U', 'R1', 'U1', 'F1'])
                return
            
        if top.colors[0][1] == topColor:
            if top.colors[1][2] == topColor:
                self.shift(top.left, ['F']+ 2*['R', 'U', 'R1', 'U1'] +['F1'])
                return
            
            elif top.colors[2][1] == topColor:
                self.shift(top.left, ['F', 'R', 'U', 'R1', 'U1', 'F1'])
                return
            
        if top.colors[0][1] == topColor and top.colors[1][0] == topColor and top.colors[1][2] == topColor and top.colors[2][1] == topColor:
            return
        
        self.shift(self.blue, ['F', 'R', 'U', 'R1', 'U1', 'F1'])
        self.solvePlus()
    
    '''    
    def searchEdges(self):        
        while self.blue.color != self.blue.colors[0][1] and self.red.color != self.red.colors[0][1] and self.green.color != self.green.colors[0][1] and self.orange.color != self.orange.colors[0][1]:
            print(self.blue.color == self.blue.colors[0][1], self.red.color == self.red.colors[0][1], self.green.color == self.green.colors[0][1], self.orange.color == self.orange.colors[0][1])
            self.shift(self.blue, ['U'])
            
        face = self.blue
        count = [0, 0, 0, 0]
        sumCount = 0
        
        for i in range(4):
            if face.colors[0][1] == face.color:
                count[i]+=1
                sumCount+=1
                
            face = face.right
            
        if sumCount == 1:
            self.solveEdge1(count)
            
        elif sumCount == 2:
            self.solveEdge2(count)
            
    def solveEdge1(self, count):
        
        steps = ['R', 'U', 'R1', 'U', 'R', 'U', 'U', 'R1', 'U']
        
        if count[0] == 1:
            face = self.green
            
        elif count[1] == 1:
            face = self.orange
            
        elif count[2] == 1:
            face = self.blue
            
        else:
            face = self.red
            
        self.shift(face, steps)
        self.shift(face.right, steps)
    
    '''
     
    def solveEdges(self):
        face = self.blue
        centre = self.blue
        steps = ['R', 'U', 'R1', 'U', 'R', 'U', 'U', 'R1', 'U']
        
        def solveAdjEdges():
            while centre.colors[0][1] != centre.color:
                self.shift(centre, ['U'])
        
            self.shift(centre.left, steps)
            
        def solveOppEdges():
            while centre.colors[0][1] != centre.color:
                self.shift(centre, ['U'])
                
            self.shift(centre.left, steps)
            self.shift(centre.left.left, steps)
            self.shift(centre.left, steps)
            
        count = 0
        for i in range(4):
            if face.colors[0][1] == centre.color:
                count+=1
                
            face = face.right
            centre = centre.right
                
        if count == 4:
            return
        
        for i in range(4):
            for j in range(4):
                if [face.colors[0][1], face.right.colors[0][1]] == [centre.color, centre.right.color]:
                    solveAdjEdges()
                    return
                
                elif [face.colors[0][1], face.right.right.colors[0][1]] == [centre.color, centre.right.right.color]:
                    solveOppEdges()
                    return
                
                centre = centre.right
           
            face = face.right
        
    def matchCorners(self):
        top = self.up
        cmd = ['U', 'R', 'U1', 'L1', 'U', 'R1', 'U1', 'L']
        
        def matchAll(face):
            while checkCorners():
                self.shift(face, cmd)
        
        def checkCorners():
            count = 0
            corners = [top.up.color, top.left.color]
            if top.colors[0][0] in corners:
                if top.up.colors[0][2] in corners or top.left.colors[0][0] in corners:
                    count+=1
                    
            if top.colors[0][0] == top.color:
                if top.up.colors[0][2] == top.up.color:
                    count+=1     
            
            corners = [top.up.color, top.right.color]
            if top.colors[0][2] in corners:
                if top.up.colors[0][0] in corners or top.right.colors[0][2] in corners:
                    count+=1
                    
            if top.colors[0][2] == top.color:
                 if top.up.colors[0][0] == top.up.color:
                     count+=1
        
            corners = [top.down.color, top.left.color]        
            if top.colors[2][0] in corners:
                if top.down.colors[0][0] in corners or top.left.colors[0][2] in corners:
                    count+=1
            
            if top.colors[2][0] == top.color:
                if top.down.colors[0][0] == top.down.color:
                    count+=1                    
                                
            corners = [top.down.color, top.right.color]           
            if top.colors[2][2] in corners:
                if top.down.colors[0][2] in corners or top.right.colors[0][0] in corners:
                    count+=1
            
            if top.colors[2][2] == top.color:
                if top.down.colors[0][2] == top.down.color:
                    count+=1
            
            return count!=4       
                    
        
        def searchCorner():
            corners = [top.up.color, top.left.color]
            if top.colors[0][0] in corners:
                if top.up.colors[0][2] in corners or top.left.colors[0][0] in corners:
                    matchAll(top.up)
                    return False
# =============================================================================
#          
#         if top.colors[0][0] == top.color:
#             if top.up.colors[0][2] in corners and top.left.colors[0][0] in corners:
#                 matchAll(top.up)
#                 return
#         
# =============================================================================

            if top.colors[0][0] == top.color:
                if top.up.colors[0][2] == top.up.color:
                    matchAll(top.up)
                    return False       
            
                        
            corners = [top.up.color, top.right.color]
            if top.colors[0][2] in corners:
                if top.up.colors[0][0] in corners or top.right.colors[0][2] in corners:
                    matchAll(top.right)
                    return False
            
# =============================================================================
#         if top.colors[0][2] == top.color:
#             if top.up.colors[0][0] in corners and top.right.colors[0][2] in corners:
#                 matchAll(top.right)
#                 return
# =============================================================================
        
            if top.colors[0][2] == top.color:
                 if top.up.colors[0][0] == top.up.color:
                     matchAll(top.right)
                     return False
            
            corners = [top.down.color, top.left.color]        
            if top.colors[2][0] in corners:
                if top.down.colors[0][0] in corners or top.left.colors[0][2] in corners:
                    matchAll(top.left)
                    return False
            
# =============================================================================
#         if top.colors[2][0] == top.color:
#             if top.down.colors[0][0] in corners and top.left.colors[0][2] in corners:
#                 matchAll(top.left)
#                 return
# =============================================================================
         
            if top.colors[2][0] == top.color:
                if top.down.colors[0][0] == top.down.color:
                    matchAll(top.left)
                    return False
                
            corners = [top.down.color, top.right.color]           
            if top.colors[2][2] in corners:
                if top.down.colors[0][2] in corners or top.right.colors[0][0] in corners:
                    matchAll(top.down)
                    return False
          
 # =============================================================================
 #         if top.colors[2][2] == top.color:
 #             if top.down.colors[0][2] in corners and top.right.colors[0][0] in corners:
 #                 matchAll(top.down)
 #                 return
 # =============================================================================
            if top.colors[2][2] == top.color:
                if top.down.colors[0][2] == top.down.color:
                    matchAll(top.down)
                    return False
                
            return True
        
        while searchCorner():
            self.shift(self.blue, cmd)


def main():    
    #cubeDisplay() 
    c = Cube()
    
    #cmd = ['R', 'U', 'R1', 'U', 'R', 'U', 'U', 'R1', 'U', 'F']
    
    '''
    blueColors = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
    redColors = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
    greenColors = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
    orangeColors = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
    whiteColors = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
    yellowColors = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
    '''
    
    # =============================================================================
    # #No.of Steps : 131
    # blueColors = [['r', 'y', 'b'], 
    #               ['g', 'b', 'y'], 
    #               ['o', 'g', 'w']]
    # 
    # redColors = [['w', 'o', 'b'], 
    #              ['b', 'r', 'w'], 
    #              ['o', 'y', 'o']]
    # 
    # greenColors = [['r', 'w', 'g'], 
    #                ['b', 'g', 'w'], 
    #                ['g', 'o', 'o']]
    # 
    # orangeColors = [['r', 'b', 'y'], 
    #                 ['g', 'o', 'r'], 
    #                 ['w', 'r', 'b']]
    # 
    # whiteColors = [['y', 'o', 'b'], 
    #                ['y', 'w', 'o'], 
    #                ['g', 'b', 'y']]
    # 
    # yellowColors = [['w', 'r', 'y'], 
    #                 ['r', 'y', 'w'], 
    #                 ['g', 'g', 'r']]
    # 
    # =============================================================================
    # =============================================================================
    # 
    # #No.of Steps: 184
    # blueColors = [['o', 'r', 'w'], 
    #               ['w', 'b', 'g'], 
    #               ['g', 'y', 'w']]
    # 
    # redColors = [['b', 'r', 'o'], 
    #              ['o', 'r', 'w'], 
    #              ['b', 'o', 'y']]
    # 
    # greenColors = [['b', 'g', 'r'], 
    #                ['r', 'g', 'y'], 
    #                ['o', 'b', 'r']]
    # 
    # orangeColors = [['g', 'b', 'w'], 
    #                 ['o', 'o', 'b'], 
    #                 ['b', 'w', 'r']]
    # 
    # whiteColors = [['w', 'g', 'r'], 
    #                ['o', 'w', 'b'], 
    #                ['y', 'y', 'g']]
    # 
    # yellowColors = [['y', 'w', 'y'], 
    #                 ['r', 'y', 'y'], 
    #                 ['g', 'g', 'o']]
    # =============================================================================
    
    
    #blueColors = [['r', 'y', 'b'], 
    #              ['g', 'b', 'y'], 
    #              ['o', 'g', 'w']]
    #
    #redColors = [['w', 'o', 'b'], 
    #             ['b', 'r', 'w'], 
    #             ['o', 'y', 'o']]
    #
    #greenColors = [['r', 'w', 'g'], 
    #               ['b', 'g', 'w'], 
    #               ['g', 'o', 'o']]
    #
    #orangeColors = [['r', 'b', 'y'], 
    #                ['g', 'o', 'r'], 
    #                ['w', 'r', 'b']]
    #
    #whiteColors = [['y', 'o', 'b'], 
    #               ['y', 'w', 'o'], 
    #               ['g', 'b', 'y']]
    #
    #yellowColors = [['w', 'r', 'y'], 
    #                ['r', 'y', 'w'], 
    #                ['g', 'g', 'r']]
    
    
    cd = Color_Detect()
    
    (blueColors, redColors, greenColors, orangeColors, whiteColors, yellowColors) = cd.get_faces()
    
    
    c.sendScramble(blueColors, redColors, greenColors, orangeColors, whiteColors, yellowColors)
    '''
    cmd = ['R', 'U', 'R1', 'U1']
    c.shift(c.green, 6*cmd)
    
    
    '''
    c.display()
    
    c.solve()
    if not c.perfectCube():
        print('Not a Perfect Cube, resetting......')
        c.reset()
        
    print('No.of Steps : ', c.noOfSteps)
    
    c.display()   
    
    if c.isSolved():
        print('Cube Solved')  
    
    
if __name__ == '__main__':
    from ColorDetect import Color_Detect
    main()
































