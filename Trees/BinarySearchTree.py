#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:18:07 2021

@author: kamzon
"""

class Node:
    
    def __init__(self,val):
        
        self.l_child = None
        self.r_child = None
        self.data = val
        
        
        
        
""" insert node into BST"""


def insert(root, node):
    
    if (root is None):
        root= node
    
    if(root.data > node.data):
        
        if(root.l_child is None):
            
            root.l_child = node
            
        else:
            
            insert(root.l_child,node)
            
    else:
        
        if(root.r_child == None):
            
            root.r_child = node
            
        else: 
            
            insert(root.r_child,node)
    
        
    
""" in order print"""

def in_order_print(root):
    
    if not root:
        return
    
    in_order_print(root.l_child)
    print(root.data)
    in_order_print(root.r_child)
    
    
""" pre-order print"""

def pre_order_print(root):
    
    if not root:
        return
    print(root.data)
    pre_order_print(root.l_child)
    
    pre_order_print(root.r_child)
    
    
    
""" example"""

tree = Node(10)

in_order_print(tree)

insert(tree, Node(5))

insert(tree, Node(1))

in_order_print(tree)
pre_order_print(tree)

insert(tree, Node(15))
insert(tree, Node(12))

in_order_print(tree)
pre_order_print(tree)