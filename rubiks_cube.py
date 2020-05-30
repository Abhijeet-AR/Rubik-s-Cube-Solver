#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:28:51 2019

@author: AR
"""

from cube_face import Face     
#from rcube_solve_begginers import Solve   
from solve_adv import Solve           
        

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
                
            elif s == 'f':
                face.right.right.fRotateClock()
                face.right.right.eRotateClock()
            
            elif s == 'f1':
                face.right.right.fRotateAntiClock()
                face.right.right.eRotateAntiClock()
                
            elif s == 'M':
                face.mRotateClock()
            
            elif s == 'M1':
                face.mRotateAntiClock()
                
                
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
#        s = Solve(self.blue, self.red, self.green, self.orange, self.white, self.yellow, self.shift, self.isSolved)
#        s.solveRow1()
#        #c.display()
#
#        s.solveRow2()
#        #c.display()
#        
#        s.solveRow3()
#        #c.display()
#        print('Done')
        
        a = Solve(self.blue, self.red, self.green, self.orange, self.white, self.yellow, self.shift, self.isSolved)
        a.solve_cross()
        print('Cross Solved')
#        self.display()
        
        a.solve_2rows()
        print('2 Rows Solved')
        self.display()
        
        a.solve_toprow()
        print('Top Row Solved')
        self.display()
        
        if self.isSolved():
            return
        
        a.solve_3rd_row()
        print('3rd Row Solved')
#        self.display()
        
        


def main():    
    #cubeDisplay() 
    c = Cube()
    
    #cmd = ['R', 'U', 'R1', 'U', 'R', 'U', 'U', 'R1', 'U', 'F']
    
    #blueColors = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
    #redColors = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
    #greenColors = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
    #orangeColors = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
    #whiteColors = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
    #yellowColors = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]

    
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
     
    #No.of Steps: 184
    
#    blueColors = [['o', 'r', 'w'],
#                   ['w', 'b', 'g'], 
#                   ['g', 'y', 'w']]
#     
#    redColors = [['b', 'r', 'o'], 
#                  ['o', 'r', 'w'], 
#                  ['b', 'o', 'y']]
#     
#    greenColors = [['b', 'g', 'r'], 
#                    ['r', 'g', 'y'], 
#                    ['o', 'b', 'r']]
#     
#    orangeColors = [['g', 'b', 'w'], 
#                     ['o', 'o', 'b'], 
#                     ['b', 'w', 'r']]
#     
#    whiteColors = [['w', 'g', 'r'], 
#                    ['o', 'w', 'b'], 
#                    ['y', 'y', 'g']]
#     
#    yellowColors = [['y', 'w', 'y'], 
#                     ['r', 'y', 'y'], 
#                     ['g', 'g', 'o']]
    
    
#    blueColors = [['o', 'o', 'b'],
#                  ['b', 'b', 'b'],
#                  ['b', 'b', 'b']]
#    
#    redColors = [['r', 'b', 'o'],
#                 ['r', 'r', 'r'],
#                 ['r', 'r', 'r']]
#    
#    greenColors = [['b', 'g', 'r'],
#                   ['g', 'g', 'g'],
#                   ['g', 'g', 'g']]
#    
#    orangeColors = [['g', 'r', 'g'],
#                    ['o', 'o', 'o'],
#                    ['o', 'o', 'o']]
#    
#    whiteColors = [['w', 'w', 'w'],
#                   ['w', 'w', 'w'],
#                   ['w', 'w', 'w']]
#    
#    yellowColors = [['y', 'y', 'y'],
#                    ['y', 'y', 'y'],
#                    ['y', 'y', 'y']]
    
    
    cd = Color_Detect()
    
    try:
        (blueColors, redColors, greenColors, orangeColors, whiteColors, yellowColors) = cd.get_faces()
    
    except TypeError:
        file = open('cube_faces.txt', 'rb')

        blueColors = pickle.load(file)
        redColors = pickle.load(file)
        greenColors = pickle.load(file)
        orangeColors = pickle.load(file)
        whiteColors = pickle.load(file)
        yellowColors = pickle.load(file)

        file.close()

    file =  open('cube_faces.txt', 'wb')

    pickle.dump(blueColors, file)
    pickle.dump(redColors, file)
    pickle.dump(greenColors, file)
    pickle.dump(orangeColors, file)
    pickle.dump(whiteColors, file)
    pickle.dump(yellowColors, file)

    file.close()
    
    c.sendScramble(blueColors, redColors, greenColors, orangeColors, whiteColors, yellowColors)
    '''
    cmd = ['R', 'U', 'R1', 'U1']
    c.shift(c.green, 6*cmd)
    
    
    '''   
    c.display()
    
#    c.shift(c.blue, ['M1'])
    
#    c.shift(c.blue, ['F1', 'L', 'F', 'R1', 'F1', 'L1', 'F', 'R'])
    
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
    import pickle
    
    main()
































