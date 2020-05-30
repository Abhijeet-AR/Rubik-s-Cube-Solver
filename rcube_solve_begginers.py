#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:38:10 2019

@author: AR
"""

#from rubiks_cube import Cube

class Solve:      
    def __init__(self, blue, red, green, orange, white, yellow, shift, isSolved):
        self.blue = blue
        self.red = red
        self.green = green
        self.orange = orange 
        self.white = white
        self.yellow = yellow
        
        self.shift = shift
        self.isSolved = isSolved
        
        self.up = yellow
        self.down = white
        
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