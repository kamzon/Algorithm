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
    
    
""" Delete node from tree"""

def delete_node(root, data):
    
    if (root is None):
        return root
        
    elif(root.data>data):
        root.l_child = delete_node(root.l_child, data)
    elif(root.data<data):
        root.r_child = delete_node(root.r_child, data)
        
    else: 
        
        # case 1 : leaf node
        if(root.l_child is None and root.r_child is None):
            root=None
            
        # case 2: node has one child
        elif(root.r_child is None):
            root.data = root.l_child.data
            root.l_child = None
            
        elif(root.l_child is None):
            root.data = root.r_child.data
            root.r_child = None
  
        # case 3: node has both children
        
        else:
            temp = root.r_child
            
            while(temp.l_child != None):
                temp = temp.l_child
                
            root.data=temp.data
            root.r_child = delete_node(root.r_child, temp.data)


    return root



    
""" example"""

tree = Node(10)

#in_order_print(tree)

insert(tree, Node(5))

insert(tree, Node(1))

#in_order_print(tree)
#pre_order_print(tree)

insert(tree, Node(15))
insert(tree, Node(12))
insert(tree, Node(13))
insert(tree, Node(14))
insert(tree, Node(11))
insert(tree, Node(12.5))

in_order_print(tree)
#pre_order_print(tree)
print("delete 12")
delete_node(tree, 12)
in_order_print(tree)