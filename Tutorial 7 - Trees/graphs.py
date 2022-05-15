#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 09:36:03 2022

@author: minhpham1606
"""

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
        

def is_symmetric(G):
    M = list_to_matrix(G)
    n = len(M)
    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j] != M[j][i]:
                return False
    return True
            
def revert_edges(G):
    M = list_to_matrix(G)
    n = len(M)
    for i in range(n):
        for j in range(i + 1, n):
            M[i][j], M[j][i] = M[j][i], M[i][j]
    Y = matrix_to_adjlist(M)
    return Y