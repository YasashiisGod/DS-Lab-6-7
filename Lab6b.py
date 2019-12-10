#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on day 12/0/2019
Course: CS 2302 - Data Structures
Author: Brian Perez
Assignment: Lab #6b
Instructor: Diego Aguirre 
D.O.L.M.: 12/09/19 
"""
 
class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight

#Class to represent a graph 
class GraphAL:
    # Constructor
    def __init__(self, vertices, weighted=False, directed=False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.al)

    def insert_vertex(self):
        self.al.append([])

        return len(self.al) - 1  # Return id of new vertex

    def insert_edge(self, source, dest, weight=1):
        if not self.is_valid_vertex(source) or not self.is_valid_vertex(dest):
            print('Error, vertex number out of range')
        elif weight != 1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest, weight))
            if not self.directed:
                self.al[dest].append(Edge(source, weight))

    def delete_edge(self, source, dest):
        if source >= len(self.al) or dest >= len(self.al) or source < 0 or dest < 0:
            print('Error, vertex number out of range')
        else:
            deleted = self._delete_edge(source, dest)
            if not self.directed:
                deleted = self._delete_edge(dest, source)
            if not deleted:
                print('Error, edge to delete not found')

    def _delete_edge(self, source, dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i += 1
        return False

    def num_vertices(self):
        return len(self.al)

    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        for edge in self.al[src]:
            reachable_vertices.add(edge.dest)

        return reachable_vertices

    def display(self):
        print('[', end='')
        for i in range(len(self.al)):
            print('[', end='')
            for edge in self.al[i]:
                print('(' + str(edge.dest) + ',' + str(edge.weight) + ')', end='')
            print(']', end=' ')
        print(']')
                
        
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
def topological_sort(graph): 
    all_in_degrees = compute_indegree_every_vertex(graph) 
    sort_result = [] 
    q = Queue() 
    
    for i in range(len(all_in_degrees)): 
        if all_in_degrees[i] == 0: 
            q.put(i) # enqueue 
            
    while not q.is_empty(): 
        u = q.put() # dequeue 
        sort_result.append(u) 
        for adj_vertex in graph.get_adj_vertices(u): 
            all_in_degrees[adj_vertex] -= 1 
    
        if all_in_degrees[adj_vertex] == 0: 
            q.put(adj_vertex) 
    
    if len(sort_result) != graph.num_vertices: # Cycle found 
        return None 
    
    return sort_result 

def compute_indegree_every_vertex(graph):
    
    return 

def get_adj_vertices(vertex): 
    return

myGraph = GraphAL(5, weighted=False, directed=True)    
myGraph.insert_edge(0, 1, weight=1)
myGraph.insert_edge(0, 2, weight=1)
myGraph.insert_edge(1, 2, weight=1)
myGraph.insert_edge(2, 1, weight=1)



topological_sort(myGraph)

    