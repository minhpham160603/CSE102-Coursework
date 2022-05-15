#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 13:26:29 2022

@author: minh.pham
"""

def binom(n, k):
    if k == 0:
        return 1
    if k > n:
        return 0
    return binom(n - 1, k) + binom(n - 1, k - 1)

def choose(s, k):
    if k == 0:
        return [[]]
    elif k == len(s):
        return [s]
    elif k > len(s):
        return None
    else:
        l1 = choose(s[:-1], k)
        l2 = choose(s[:-1], k - 1)
        if l2 == []:
            l2 = [[s[-1]]]
        else:
            for i in range(len(l2)):
                l2[i].append(s[-1])
        return l1 + l2

def permutations(l):
    n = len(l)
    if n == 0:
        return [[]]
    elif n == 1:
        return [l]
    else:
        out = []
        l1 = permutations(l[:-1])
        for i in range(len(l1)):
            for j in range(len(l1[i]) + 1):
                tmp = l1[i].copy()
                tmp.insert(j, l[-1])
                out.append(tmp)
        return out
    
def not_angry(n):
    ways = 0
    for i in range(n + 1):
        ways += binom(n - i + 1, i)
    return ways