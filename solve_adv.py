#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:17:06 2019

@author: AR
"""

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
        self.count = 1
        
    def solve_cross(self):  
        base = self.down.color
        face = self.blue
#        cmd = ['R', 'U', 'R1']
        
        def solveEdge(face):
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
                    
                    
        while  base != self.down.colors[0][1] or base != self.down.colors[1][0] or base != self.down.colors[1][2] or base != self.down.colors[2][1]: 
            #for i in range(10):
               solveEdge(face)
               face = face.right
                                   
                    
    def solve_2rows(self):
     down_color = self.down.color
     top = self.up

     def check_f2l(face):
         return face.colors[1][0] == face.color and face.colors[2][0] == face.color
     
#         def direct():
#             down_color = down.color
#             if top.colors[0][1] != top.color and top.up.colors[0][1] != top.color:
#                 top_color = top.colors[0][1]
#                 side_color = top.up.colors[0][1]
#                 if top.colors[0][0] == top_color:
#                     if top.up.colors[0][2] == down_color:

     def search_edge(adj1, adj2):
         face = self.blue
         
         while not ((face.colors[1][2] == adj1 and face.right.colors[1][0] == adj2) or 
                    (face.colors[1][2] == adj2 and face.right.colors[1][0] == adj1)):
             face = face.right
             
         return face
             
                       
     def top_white():        
         def solve():
            adj1 = top.up.colors[0][2]
            adj2 = top.left.colors[0][0]
             
            if((adj1 == top.colors[0][1] and adj2 == top.up.colors[0][1]) or 
               (adj2 == top.colors[0][1] and adj1 == top.up.colors[0][1])):
                 side_color = top.up.colors[0][1]
                 if adj1 == top.right.color:
                     face = top.down
                     self.shift(face, ['U1'])
                 
                 else:
                     face = top.up
                     while face.color != adj2:
                         face = face.left
                         
                     while face.colors[0][0] != adj2:
                         self.shift(face, ['U'])
                     
                 self.shift(face, ['F1', 'U', 'F'])
                 if face.right.color == side_color:
                     face = face.right
                     self.shift(face, ['U'] + ['F', 'U', 'F1', 'U', 'F', 'U1', 'F1'])
                     
                 elif face.color == side_color:
                     self.shift(face, 2*['U'] + ['F1', 'U', 'U', 'F', 'U1', 'F1', 'U', 'F'])
              
            elif((adj1 == top.colors[1][0] and adj2 == top.left.colors[0][1]) or 
                 (adj2 == top.colors[1][0] and adj1 == top.left.colors[0][1])):
                 side_color = top.left.colors[0][1]
                 if adj1 == top.right.color:
                     face = top.right
                     self.shift(face, ['U'])
                         
                 else:
                     face = top.up
                     while face.color != adj1:
                         face = face.right
                         
                     while face.colors[0][2] != adj1:
                         self.shift(face, ['U1'])    
                
                 self.shift(face, ['F', 'U1', 'F1'])
                 if face.left.color == side_color:
                     face = face.left
                     self.shift(face, ['U1'] + ['F1', 'U1', 'F', 'U1', 'F1', 'U', 'F'])
                     
                 elif face.color == side_color:
                     self.shift(face, 2*['U'] + ['F', 'U', 'U', 'F1', 'U', 'F', 'U1', 'F1'])
                 
            elif((adj1 == top.colors[1][2] and adj2 == top.right.colors[0][1]) or 
                 (adj2 == top.colors[1][2] and adj1 == top.right.colors[0][1])):
                side_color = top.right.colors[0][1]
                top_color = top.colors[1][2]
                
                if side_color == top.up.color:
                    face = top.up
                    self.shift(face, ['U1'])
                    
                else:
                    face = top.right
                    while face.color != side_color:
                        face = face.left
                        
                    while adj2 != face.right.right.colors[0][0] or adj1 != face.right.colors[0][2]:
                        self.shift(face, ['U'])
                    
                if face.left.color == top_color:
                    self.shift(face, ['F', 'U', 'F1', 'U', 'F', 'U1', 'F1'])
                
                else:
                    self.shift(face, ['F1', 'U', 'U', 'F', 'U1', 'F1', 'U', 'F'])
                    
            elif((adj1 == top.colors[2][1] and adj2 == top.down.colors[0][1]) or 
                 (adj2 == top.colors[2][1] and adj1 == top.down.colors[0][1])):
                side_color = top.down.colors[0][1]
                top_color = top.colors[2][1]
                                
                if side_color == top.right.color:
                    face = top.up
                    self.shift(face, ['U1'])
                    
                else:
                    face = top.down
                    while face.color != side_color:
                        face = face.left
                        
                    while adj2 != face.left.colors[0][0] or adj1 != face.left.left.colors[0][2]:
                        self.shift(face, ['U'])
                    
                if face.left.color == top_color:
                    self.shift(face, ['F', 'U', 'U', 'F1', 'U', 'F', 'U1', 'F1'])
                
                else:
                    self.shift(face, ['F1', 'U1', 'F', 'U1', 'F1', 'U', 'F'])
                    
                
            else:
                 face = search_edge(adj1, adj2)
                 
                 flag = (face.colors[0][2] == adj1 and face.right.colors[0][0] == adj2)
                 
                 if ((face.colors[0][0] == adj1 and face.left.colors[0][2] == adj2) or
                     (face.colors[0][0] == adj2 and face.left.colors[0][2] == adj1)):
                    self.shift(face, ['R', 'U', 'R1'])
                 
                 else: 
                    self.shift(face, ['R', 'U1', 'R1'])
                    
                 if flag:
                     if top.right.colors[0][0] == down_color and top.down.colors[0][2] == adj2:
                         self.shift(top.down, ['U'])
                         
                     else:
                         while top.down.colors[0][0] != down_color or top.left.colors[0][2] != adj2:
                             self.shift(top.down, ['U1'])
                             
                     left_side_white()
                             
                 else:
                     if top.colors[0][2] == down_color and top.right.colors[0][2] == adj1:
                         self.shift(face, ['U1'])
                         
#                     else:
#                         while top.colors[0][0] != down_color or top.up.colors[0][2] != adj1:
#                             self.shift(face, ['U'])
                             
                     solve()
                 
                    
#                 if (top.colors[0][2] == down_color and
#                     top.right.colors[0][2] == adj1 and
#                     top.up.colors[0][0] == adj2):
#                     self.shift(face, ['U1'])
#                 
#                 while not (top.colors[0][0] == down_color and
#                            top.up.colors[0][2] == adj1 and
#                            top.left.colors[0][0] == adj2):
#                     self.shift(face, ['U'])
                    
                 top_white()
                 
         if top.colors[0][2] == down_color:
             self.shift(self.blue, ['U1'])
             solve()
             print()
             self.count += 1

         if top.colors[2][0] == down_color:
            self.shift(self.blue, ['U'])
            solve()
            print()
            self.count += 1
            
         if top.colors[2][2] == down_color:
            self.shift(self.blue, 2*['U'])
            solve()
            print()
            self.count += 1
         
         if top.colors[0][0] == down_color:
            solve()
            print()
            self.count += 1
            
       
     def left_side_white():
        def solve():
            adj1 = top.colors[2][0]
            adj2 = top.left.colors[0][2]
            
#            print(adj1, adj2)
                                    
            if ((adj1 == top.colors[1][0] and adj2 == top.left.colors[0][1]) or 
                (adj2 == top.colors[1][0] and adj1 == top.left.colors[0][1])):
                if adj1 == top.left.color:
                    face = top.up
                    self.shift(face, ['U'])
                    
                else:    
                    face = top.up
                    while adj2 != face.color:
                        face = face.left
                        
                    while face.right.colors[0][0] != down_color or face.colors[0][2] != adj2:
                        self.shift(face, ['U1'])
                        
                if face.colors[0][1] == adj2:
                    self.shift(face, ['U1', 'F1', 'U', 'F'])
                 
                else:
                    self.shift(face, ['R', 'U', 'U', 'R1'])
                    self.shift(face, ['U', 'U', 'R', 'U', 'U', 'R1', 'U', 'U', 'R', 'U1', 'R1'])
                
            elif ((adj1 == top.colors[2][1] and adj2 == top.down.colors[0][1]) or 
                  (adj2 == top.colors[2][1] and adj1 == top.down.colors[0][1])): 
                 if adj1 == top.down.color:
                     face = top.left
                     self.shift(face, ['U1'])
                     
                 else:
                     face = top.left
                     while adj1 != face.color:
                         face = face.right
                         
                     while face.right.colors[0][0] != down_color or face.colors[0][2] != adj2:
                         self.shift(face, ['U'])
                     
                     face = face.left
                         
                 self.shift(face, ['R', 'U1', 'R1'])
                 
                 if face.left.colors[0][1] == adj2:
                     self.shift(face, ['U', 'U', 'F1', 'U', 'U', 'F', 'U', 'U', 'F1', 'U', 'F'])
                 
                 else:
                     self.shift(face, ['U', 'R', 'U', 'R1'])
                     
            elif ((adj1 == top.colors[0][1] and adj2 == top.up.colors[0][1]) or 
                  (adj2 == top.colors[0][1] and adj1 == top.up.colors[0][1])):
                if adj1 == top.down.color:
                    face = top.up
                    self.shift(face, ['U'])
                    
                else:
                    face = top.down                    
                    while adj2 != face.color:
                        face = face.right
                        
                    while face.colors[0][0] != down_color or face.left.colors[0][2] != adj2:
                        self.shift(face, ['U1'])
                        
                    face = face.left
                    
                if face.left.colors[0][1] == adj2:
                    self.shift(face, ['R1', 'U1', 'R'])
                    self.shift(face, ['U', 'U', 'R1', 'U', 'R'])
                    
                else:
                    self.shift(face, ['R1', 'U', 'R', 'U1'])
                    self.shift(face.right, ['R', 'U', 'R1'])
                        
            elif ((adj1 == top.colors[1][2] and adj2 == top.right.colors[0][1]) or 
                  (adj2 == top.colors[1][2] and adj1 == top.right.colors[0][1])):
                if adj1 == top.down.color:
                    face = top.up
                    self.shift(face, ['U'])
                    
                else:
                    face = top.down                    
                    while adj2 != face.color:
                        face = face.right
                        
                    while face.colors[0][0] != down_color or face.left.colors[0][2] != adj2:
                        self.shift(face, ['U1'])
                        
                    face = face.left
                    
                if face.left.left.colors[0][1] == adj2:
                    self.shift(face, ['R1', 'U', 'U', 'R'])
                    self.shift(face, ['U', 'U', 'R1', 'U', 'R'])
                    
                else:
                    self.shift(face.right, ['U1', 'R', 'U', 'R1'])
             
            else:
                face = search_edge(adj1, adj2)
                
                flag = (face.colors[0][2] == adj2 and face.right.colors[0][0] == down_color)
                
                if face.colors[0][0] == down_color and face.left.colors[0][2] == adj2:
                     self.shift(face, ['R', 'U', 'R1'])    
                     
                else:
                    self.shift(face, ['R', 'U1', 'R1'])
                
                if flag:
                    if top.left.colors[0][2] == down_color and top.colors[2][0] == adj2:
                         self.shift(face, ['U1'])
                    
                    else:
                        while top.down.colors[0][2] != down_color or top.colors[2][2] != adj2:
                            self.shift(face, ['U'])
                         
                    right_side_white()
                    
                else:
                    if top.right.colors[0][0] == down_color and top.colors[2][2] == adj1:
                        self.shift(face, ['U1'])
                        
                    else:
                        while top.down.colors[0][0] != down_color or top.colors[2][0] != adj1:
                            self.shift(face, ['U'])
                 
                    solve()
                
                
        if top.down.colors[0][0] == down_color:
            solve()
            print()
            self.count+=1
            
        if top.right.colors[0][0] == down_color:
            self.shift(top.right, ['U'])
            solve()
            print()
            self.count+=1
                
        if top.left.colors[0][0] == down_color:
            self.shift(top.left, ['U1'])
            solve()
            print()
            self.count+=1
            
        if top.up.colors[0][0] == down_color:
            self.shift(top.up, 2*['U'])
            solve()
            print()
            self.count+=1
        
                
     def right_side_white():         
         def solve():
             adj1 = top.colors[2][2]
             adj2 = top.right.colors[0][0]
                          
             if ((adj1 == top.colors[1][2] and adj2 == top.right.colors[0][1]) or 
                 (adj2 == top.colors[1][2] and adj1 == top.right.colors[0][1])): 
                 flag = (top.colors[1][2] == adj2)
                                
                 if adj1 == top.up.color:
                    face = top.up
                    self.shift(face, ['U'])
                
                 else:
                    face = top.down                    
                    while adj2 != face.color:
                        face = face.right
                        
                    while face.colors[0][2] != down_color or face.right.colors[0][0] != adj2:
                        self.shift(face, ['U1'])
                        
                    face = face.left
                
                 if flag:
                    self.shift(face, ['R', 'U', 'U', 'R1'])
                    self.shift(face, ['U', 'F1', 'U1', 'F'])
                    
                    
                 else:
                    self.shift(face, ['U', 'U', 'R', 'U1', 'R1'])
                    
             elif ((adj1 == top.colors[2][1] and adj2 == top.down.colors[0][1]) or 
                   (adj2 == top.colors[2][1] and adj1 == top.down.colors[0][1])): 
                 if adj1 == top.down.color:
                     face = top.left
                     self.shift(face, ['U'])
                     
                 else:
                     face = top.down
                     
                     while adj1 != face.right.color:
                         face = face.right
                         
                     while face.colors[0][2] != down_color or face.right.colors[0][0] != adj2:
                         self.shift(face, ['U1'])
                         
                     
                 self.shift(face, ['R1', 'U', 'R'])
                 if face.left.colors[0][1] == adj2:
                     self.shift(face.right, ['U', 'U', 'R', 'U', 'U', 'R1', 'U', 'U', 'R', 'U1', 'R1'])
                     
                 else:
                     self.shift(face, ['U1', 'R1', 'U1', 'R'])
        
           
             elif ((adj1 == top.colors[0][1] and adj2 == top.up.colors[0][1]) or 
                   (adj2 == top.colors[0][1] and adj1 == top.up.colors[0][1])):
                if adj1 == top.up.color:
                    face = top.up
                    self.shift(face, ['U'])
                    
                else:
                    face = top.down
                    
                    while adj2 != face.color:
                        face = face.right
                        
                    while face.colors[0][2] != down_color or face.right.colors[0][0] != adj2:
                        self.shift(face, ['U1'])
                        
                    face = face.left
                    
                if face.left.colors[0][1] == adj2:
                    self.shift(face, ['R', 'U', 'R1'])
                    self.shift(face, ['U', 'U', 'R', 'U1', 'R1'])
                    
                else:
                    self.shift(face, ['R', 'U1', 'R1'])
                    self.shift(face, ['U', 'F1', 'U1', 'F'])
                
             elif ((adj1 == top.colors[1][0] and adj2 == top.left.colors[0][1]) or 
                   (adj2 == top.colors[1][0] and adj1 == top.left.colors[0][1])):
                 if adj2 == top.left.color:
                     face = top.up
                     self.shift(face, ['U'])
                     
                 else:
                     face = top.down
                     
                     while adj2 != face.color:
                         face = face.right
                         
                     while face.colors[0][2] != down_color or face.right.colors[0][0] != adj2:
                        self.shift(face, ['U1'])
                        
                     face = face.left
                     
                 if face.colors[0][1] == adj2:
                     self.shift(face, ['R', 'U', 'U', 'R1'])
                     self.shift(face, ['U', 'U', 'R', 'U1', 'R1'])
                     
                 else:
                     self.shift(face, ['U', 'F1', 'U1', 'F'])
                     
             else:
                 face = search_edge(adj1, adj2)
                 
                 flag = (face.colors[0][2] == down_color and face.right.colors[0][0] == adj2)
                 
                 if face.left.colors[0][2] == down_color and face.colors[0][0] == adj2:
                     self.shift(face, ['R', 'U', 'R1'])
                     
                 else:
                     self.shift(face, ['R', 'U1', 'R1'])
                     
                 if flag:
                     if top.colors[2][0] == down_color and top.down.colors[0][0] == adj1:
                         self.shift(face, ['U'])
                         
                     while top.colors[0][0] != down_color or top.left.colors[0][0] != adj1:
                         self.shift(face, ['U1'])
                         
                     top_white()
                         
                 else:
                     if top.left.colors[0][2] == down_color and top.colors[2][0] == adj1:
                         self.shift(face, ['U1'])
                     else:    
                         while top.down.colors[0][2] != down_color or top.colors[2][2] != adj1:
                             self.shift(face, ['U'])
                         
                     solve()
                     
         if top.down.colors[0][2] == down_color:
             solve()
             print()
             self.count+=1
                         
         if top.right.colors[0][2] == down_color:
             self.shift(top.right, ['U'])
             solve()
             print()
             self.count+=1
             
         if top.left.colors[0][2] == down_color:
             self.shift(top.left, ['U1'])
             solve()
             print()
             self.count+=1
             
         if top.up.colors[0][2] == down_color:
             self.shift(top.up, 2*['U'])
             solve()
             print()
             self.count+=1
             
         
     def is_row2solved():
         face = top.down
         print()
         while (all(list(map(lambda col: col == face.color, [face.colors[1][2], face.colors[2][2]]))) and
                all(list(map(lambda col: col == face.right.color, [face.right.colors[1][0], face.right.colors[2][0]])))):
             face = face.right
             if face.color == top.down.color:
                 return (True, face)
             
         return (False, face)
                                         
     for i in range(5):  
         self.count = 1
         while self.count != 0:    
           self.count = 0 
           top_white()    
           left_side_white()    
           right_side_white()
           
         (cond, face) = is_row2solved() 
           
         if cond:
             break
         
         self.shift(face, ['R', 'U', 'R1'])
             
             
         
    def solve_toprow(self):
        top = self.up
        def form_plus():
            if all(list(map(lambda col : col == top.color, [top.colors[0][1], top.colors[1][0], top.colors[1][2], top.colors[2][1]]))):
                return
            
            if top.colors[1][0] == top.color:
                if top.colors[0][1] == top.color:
                     self.shift(top.up, ['f', 'U', 'L', 'U1', 'L1', 'f1'])
                     
                elif top.colors[2][1] == top.color:
                    self.shift(top.left, ['f', 'U', 'L', 'U1', 'L1', 'f1'])
                    
                else:
                    self.shift(top.down, ['F', 'R', 'U', 'R1', 'U1', 'F1'])
                    
                    
            elif top.colors[1][2] == top.color:
                if top.colors[0][1] == top.color:
                    self.shift(top.right, ['f', 'U', 'L', 'U1', 'L1', 'f1'])
                    
                elif top.colors[2][1] == top.color:
                    self.shift(top.down, ['f', 'U', 'L', 'U1', 'L1', 'f1'])
 
            elif top.colors[0][1] == top.color and top.colors[2][1] == top.color:
                self.shift(top.right, ['F', 'R', 'U', 'R1', 'U1'])
                
            else:
                self.shift(top.down, ['F', 'R', 'U', 'R1', 'U1', 'F1', 'f', 'U', 'L', 'U1', 'L1', 'f1'])
        
        def sune(face):
            self.shift(face, ['R', 'U', 'R1', 'U', 'R', 'U', 'U', 'R1'])
            
        def anti_sune(face):
            self.shift(face, ['R1', 'U1', 'R', 'U1', 'R1', 'U1', 'U1', 'R'])
            
        def car(face):
            self.shift(face, ['F'] + 3*['R', 'U', 'R1', 'U1'] + ['F1'])
            
        def blinker(face):
            self.shift(face, ['R', 'U', 'U', 'R', 'R', 'U1', 'R', 'R', 'U1', 'R', 'R', 'U', 'U', 'R'])
        
        def headlights(face):
            self.shift(face, ['R', 'R', 'D', 'R1', 'U', 'U', 'R', 'D1', 'R1', 'U', 'U', 'R1'])
        
        def chameleon(face):
            self.shift(face, ['L', 'F', 'R1', 'F1', 'L1', 'F', 'R', 'F1'])
            
        def bow_tie(face):
            self.shift(face, ['F1', 'L', 'F', 'R1', 'F1', 'L1', 'F', 'R'])
        
        def solve():
            corners = [top.colors[0][0], top.colors[0][2], top.colors[2][0], top.colors[2][2]]
            
            if all(list(map(lambda col: col!=top.color, corners))):
                if all(list(map(lambda col: col==top.color, [top.down.colors[0][0], top.down.colors[0][2]]))):
                    if all(list(map(lambda col: col==top.color, [top.up.colors[0][0], top.up.colors[0][2]]))): 
                        car(top.down)
                        
                    else:
                        blinker(top.right)
                        
                elif all(list(map(lambda col: col==top.color, [top.left.colors[0][0], top.left.colors[0][2]]))):
                    if all(list(map(lambda col: col==top.color, [top.right.colors[0][0], top.right.colors[0][2]]))):  
                        car(top.right)
                        
                    else:
                        blinker(top.down)
                        
                elif all(list(map(lambda col: col==top.color, [top.up.colors[0][0], top.up.colors[0][2]]))):
                    if all(list(map(lambda col: col==top.color, [top.left.colors[0][2], top.right.colors[0][0]]))): 
                        blinker(top.left)
                        
                        
                elif all(list(map(lambda col: col==top.color, [top.right.colors[0][0], top.right.colors[0][2]]))):
                    if all(list(map(lambda col: col==top.color, [top.down.colors[0][0], top.up.colors[0][2]]))): 
                        blinker(top.up)
                    
            
            elif top.colors[0][0] == top.color:
                if top.colors[0][2] == top.color:
                    if all(list(map(lambda col: col==top.color, [top.down.colors[0][0], top.down.colors[0][2]]))):
                        headlights(top.down)
                        
                    else:
                        chameleon(top.right)
                        
                elif top.colors[2][0] == top.color:
                    if all(list(map(lambda col: col==top.color, [top.right.colors[0][0], top.right.colors[0][2]]))):
                        headlights(top.right)
                        
                    else:
                        chameleon(top.up)
                        
                elif top.colors[2][2] == top.color:
                    if top.left.colors[0][2] == top.color:
                        face = top.left
                        
                    else:
                        face = top.right
                        
                    bow_tie(face)
                
                elif top.colors[0][2] != top.color and top.colors[2][0] != top.colors and top.colors[2][2] != top.color:
                    face = top.up
                    count_s = 0
                    count_as = 0
                    
                    for i in range(4):
                        if face.colors[0][2] == top.color:
                            count_s+=1
                            
                        if face.colors[0][0] == top.color:
                            count_as+=1
                            
                        face = face.right
                            
                    if count_s == 3:
                        sune(top.up)
                     
                    elif count_as == 3:
                        anti_sune(top.down)
                        
                
                        
            elif top.colors[0][2] == top.color:
                if top.colors[2][0] == top.color:
                    if top.down.colors[0][2] == top.color:
                        face = top.down
                        
                    else:
                        face = top.up
                        
                    bow_tie(face)
                    
                if top.colors[2][2] == top.color:
                    print()
                
                if top.colors[0][0] != top.color and top.colors[2][0] != top.colors and top.colors[2][2] != top.color:
                    face = top.up
                    count_s = 0
                    count_as = 0
                    
                    for i in range(4):
                        if face.colors[0][2] == top.color:
                            count_s+=1
                            
                        if face.colors[0][0] == top.color:
                            count_as+=1
                            
                        face = face.right
                            
                    if count_s == 3:
                        sune(top.right)
                     
                    elif count_as == 3:
                        anti_sune(top.left)
                        
            
            elif top.colors[2][2] == top.color:
                if top.colors[0][2] == top.color:
                    if all(list(map(lambda col: col==top.color, [top.left.colors[0][0], top.left.colors[0][2]]))):
                        headlights(top.left)
                        
                    else:
                        chameleon(top.down)
                        
                elif top.colors[0][2] == top.color:
                    if all(list(map(lambda col: col==top.color, [top.up.colors[0][0], top.up.colors[0][2]]))):
                        headlights(top.up)
                        
                    else:
                        chameleon(top.left)
                        
                        
                elif top.colors[2][0] == top.color:
                    if all(list(map(lambda col: col==top.color, [top.up.colors[0][0], top.up.colors[0][2]]))):
                        headlights(top.up)
                        
                    else:
                        chameleon(top.left)
                        
                elif top.colors[0][0] != top.color and top.colors[2][0] != top.colors and top.colors[0][2] != top.color:
                    face = top.up
                    count_s = 0
                    count_as = 0
                    
                    for i in range(4):
                        if face.colors[0][2] == top.color:
                            count_s+=1
                            
                        if face.colors[0][0] == top.color:
                            count_as+=1
                            
                        face = face.right
                            
                    if count_s == 3:
                        sune(top.down)
                     
                    elif count_as == 3:
                        anti_sune(top.up)     
                        
                        
            elif top.colors[2][0] == top.color:
                if top.colors[0][0] != top.color and top.colors[0][2] != top.colors and top.colors[2][2] != top.color:
                    face = top.up
                    count_s = 0
                    count_as = 0
                    
                    for i in range(4):
                        if face.colors[0][2] == top.color:
                            count_s+=1
                            
                        if face.colors[0][0] == top.color:
                            count_as+=1
                            
                        face = face.right
                            
                    if count_s == 3:
                        sune(top.left)
                     
                    elif count_as == 3:
                        anti_sune(top.right)
                    
        form_plus()
        print('Plus Formed')
        if top.colors != 3*[[top.color, top.color, top.color]]:
            solve()
        
        
    
    def solve_3rd_row(self):      
        def search_headlights_face():
            for i in [self.blue.color, self.red.color, self.green.color, self.orange.color]:
                face = self.blue
                for j in range(4):
                    if face.colors[0][0] == i and face.colors[0][2] == i:
                        return (True, face)
                    
                    face = face.right
                    
            return (False, face)
        
        def search_pref_face():
            face = self.blue
            
            for i in range(4):
                if face.colors[0][1] == face.color and face.colors[0][0] == face.color:
                    return (True, face)
                
                face = face.right
                
            return (False, face)
        
        (cond, face) = search_headlights_face()
        
        if cond:
            self.shift(face.right, ['R', 'U', 'R1', 'U1', 'R1', 'F', 'R', 'R', 'U1', 'R1', 'U1', 'R', 'U', 'R1', 'F1'])
            
        else:
            self.shift(face, ['F', 'R', 'U1', 'R1', 'U1', 'R', 'U', 'R1', 'F1', 'R', 'U', 'R1', 'U1', 'R1', 'F', 'R', 'F1'])
        
        if face.left.colors[0][0] == face.color:
            self.shift(face, ['U1'])
        
        while face.colors[0][0] != face.color:
            self.shift(face, ['U'])
            
        (cond, face) = search_pref_face()
        
        if cond:
            if face.right.colors[0][1] == face.left.color:
                self.shift(face.right.right, ['R', 'R', 'U', 'R', 'U', 'R1', 'U1', 'R1', 'U1', 'R1', 'U', 'R1'])
                
#            elif face.left.colors[0][1] == face.right.color:
            else:
                self.shift(face.right.right, ['R', 'U1', 'R', 'U', 'R', 'U', 'R', 'U1', 'R1', 'U1', 'R', 'R'])
            
        
        if face.colors[0][1] == face.right.color:
            face = face.right
            
        elif face.colors[0][1] == face.left.color:
            self.shift(face, ['M', 'M', 'U1', 'M', 'M', 'U1', 'M1', 'U', 'U', 'M', 'M', 'U', 'U', 'M1', 'U', 'U'])
            
        else:
            self.shift(face, ['M', 'M', 'U1', 'M', 'M', 'U', 'U', 'M', 'M', 'U1', 'M', 'M'])
            
            
        
        
                    
        
                
                    
                    
            
        
                         
                 
                 
                     
                 
                 
                 
                 
             
                
                
                
                
                    
                    
             
             
             
             
             
             
             
             
             
             
             