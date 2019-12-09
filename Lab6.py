#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on day 12/02/2019
Course: CS 2302 - Data Structures
Author: Brian Perez
Assignment: Lab #6
Instructor: Diego Aguirre 
D.O.L.M.: 12/05/19 
"""
class Graph: 
  
    def __init__(self, vertices): 
        self.v = vertices 
        self.graph = []  
   
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 

    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 

    def union(self, parent, priority, x, y): 
        x_root = self.find(parent, x) 
        y_root = self.find(parent, y) 

        if priority[x_root] < priority[y_root]: 
            parent[x_root] = y_root 
        elif priority[x_root] > priority[y_root]: 
            parent[y_root] = x_root 
  
        else : 
            parent[y_root] = x_root 
            priority[x_root] += 1

    def KruskalMST(self): 
  
        result =[] 
  
        i = 0 
        e = 0 

        self.graph =  sorted(self.graph,key= lambda item: item[2]) 
  
        parent = [] ; priority = [] 
  
        for node in range(self.v): 
            parent.append(node) 
            priority.append(0) 
      
        while e < self.v -1 : 
  
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 

            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, priority, x, y)             
  
        print ("Following are the edges in the constructed MST")  
        for u,v,weight  in result: 

            print ("%d -- %d == %d" % (u,v,weight))
            
def test():

    g = Graph(4) 
    g.addEdge(0, 1, 10) 
    g.addEdge(0, 2, 6) 
    g.addEdge(0, 3, 5) 
    g.addEdge(1, 3, 15) 
    g.addEdge(2, 3, 4) 
  
    g.KruskalMST() 
    
test()
