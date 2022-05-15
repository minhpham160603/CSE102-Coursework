#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:05:32 2022

@author: minhpham1606
"""

import math

def required(G, c, taken = None):
    taken = set() if taken is None else taken
    taken.add(c)
    res = 1
    for i in G[c]:
        if i not in taken:
            res += required(G, i, taken)
    return res

#print(required([[1], [2, 3], [], [2], [2]], 1))

def required_list(G, c, taken = None):
    taken = [] if taken is None else taken
    taken.append(c)
    for i in G[c]:
        if i not in taken:
            required_list(G, i, taken)
    taken.sort()
    return taken

def revert_edges(G):
    M = list_to_matrix(G)
    n = len(M)
    for i in range(n):
        for j in range(i + 1, n):
            M[i][j], M[j][i] = M[j][i], M[i][j]
    Y = matrix_to_adjlist(M)
    return Y

def matrix_to_adjlist(M):
    aout = []
    for i in range(len(M)):
        res = []
        for j in range(len(M[i])):
            if M[i][j] != 0:
                res.append(j)
        aout.append(res)
    return aout
        
def list_to_matrix(G):
    M = []
    for i in range(len(G)):
        res = [0]*len(G)
        for j in G[i]:
            res[j] = 1
        M.append(res)
    return M
        
def needed_for(G, c):
    Y = revert_edges(G)
    return required(Y, c)

