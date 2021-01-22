#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:21:22 2021

@author: kamzon
"""
import numpy as np

class Graph:
    
    def __init__(self,v,e):
        
        self.vertices = v
        self.edges = e
        m =[]
        
        
        for i in range(v):
            l=[]
            for j in range(v):
                l.append(0)
            m.append(l)
        
        self.AdjMatrix = m
    
            
        
def Adjacency_Matrix():
        
        
        v = int(input("Enter the number of vertices :"))

        e = int(input("Enter the number of edges :"))
    
        i=0
        
        graph = Graph(v, e)
        
        while(i<graph.edges):
            to = int(input("to node :"))
            From = int(input("from node :"))

            graph.AdjMatrix[From-1][to-1]=1
            i+=1
            
        return graph