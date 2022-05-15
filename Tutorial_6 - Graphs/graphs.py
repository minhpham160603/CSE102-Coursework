#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 08:40:09 2022

@author: minhpham1606
"""
import math

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def bst_str(node):
    if node is None:
        return '.'
    return "{}[L={}, R={}]".format(node.value, bst_str(node.left), bst_str(node.right))
        
        
def size(root):
    if root is None:
        return 0
    aout = 1
    if root.left is not None:
        aout += size(root.left)
    if root.right is not None:
        aout += size(root.right)
    return aout

def sum_values(root):
    if root is None:
        return 0
    aout = root.value
    if root.left is not None:
        aout += sum_values(root.left)
    if root.right is not None:
        aout += sum_values(root.right)
    return aout

def height(root):
    if root is None:
        return -1
    h = 1 + max(height(root.left), height(root.right))
    return h
    
def mirrored(lroot, rroot):
    if lroot is None and rroot is None:
        return True
    if lroot is None or rroot is None:
        return False
    if lroot.value != rroot.value:
        return False
    return mirrored(lroot.left, rroot.right) and mirrored(lroot.right, rroot.left)

def check_symmetry(root):
    if root is None:
        return True
    return mirrored(root.left, root.right)

#Question 6
def aux1(root, f):
    res = root.value
    if root.left is not None:
        res = f(res, aux1(root.left, f))
    if root.right is not None:
        res = f(res, aux1(root.right, f))
    return res

def accumulate(root, f, start):
    if root is None:
        return start
    return f(aux1(root, f), start)

#Question 7
"""compute the min leaves and delete it from the tre"""
def findmin(root, exc, k = 0):
    if k == 0:
        global mins
        if root not in exc:
            mins = [root.value, root]
        else:
            mins = [math.inf, None]
    else:
        if root.value < mins[0] and root not in exc:
            mins = [root.value, root]
    if root.left is not None:
        findmin(root.left, exc, 1)
    if root.right is not None:
        findmin(root.right, exc, 1)
    if k == 0:
        return mins
    
def second_min(root):
    if root is None:
        return math.inf
    if root.left is None and root.right is None:
        return math.inf
    first_min = findmin(root, exc = {})
    second_min = findmin(root, exc = {first_min[1]})
    return second_min[0]


def check(root, minv = - math.inf, maxv = math.inf):
    if root is None:
        return True
    if minv > root.value or root.value > maxv:
        return False
    return check(root.left, minv , root.value) and check(root.right, root.value, maxv)
     
def check_BST(root):
    return check(root)
    
def min_BST(root):
    if root is None:
        return math.inf
    if root.left is None:
        return root.value
    return min_BST(root.left)
    
"""def min_diff(root):
    l, r = math.inf, math.inf
    if root is None: 
        return math.inf
    if root.left is not None:
        res = abs(root.value - root.left.value)
        l =  min(res, min_diff(root.left))
        print(l)
    if root.right is not None:
        res= abs(root.value - root.right.value)
        r = min(res, min_diff(root.right))
        print(r)
    return min(l, r)"""

def count_distinct(root, pre = math.inf):
    if root is None:
        return 0
    res = 0
    if root.value != pre:
        res = 1
    if root.left is not None:
        res += count_distinct(root.left, root.value)
    if root.right is not None:
        res += count_distinct(root.right, root.value)
    return res

