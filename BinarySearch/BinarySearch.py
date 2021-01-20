#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:54:31 2021

@author: kamzon
"""

def Binary_search(Array , item):
    
    Low = 0
    high = len(Array)-1
    
    while (Low<=high):
        
        mid = Low + (high-Low)//2
        
        if(Array[mid]==item):
            return mid
        
        elif(Array[mid]<item):
            Low= mid+1
            
        else: 
            high = mid-1
            
    retun -1
    
    
L= [-6,-5,-4,-3,-2,-1,0,1,2]

print(Binary_search(L,-5))