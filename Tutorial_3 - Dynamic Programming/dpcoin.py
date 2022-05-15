#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 17:18:50 2022

@author: minhpham1606
"""
import datetime as dt

def transacts_num(n):
    """
    Bottom - up
    given n
    check transacts_nums of n - 1, n - 3, n - 7, n - 9
    take the minimum
    """
    cache = [0 for _ in range(0, n + 1)]
    for i in range(1, n + 1):
        cache[i] = 1 + min([cache[i -j] for j in [1, 3, 7, 9] if i >= j])
    return cache[n]
    
    
    
"""print(dt.datetime.now())
print(transacts_num(10000))
print(dt.datetime.now())"""

def transact(n):
    cache = {1: 1, 3: 1, 7: 1, 9: 1}
    res = 0
    for i in range(1, n + 1):
        res = transactdp(i, cache)
    return res
    
def transactdp(n, cache):
    if n in cache:
        return cache[n]
    l = []
    for i in [1, 3, 7, 9]:
        if n - i >= 0:
            l.append(transactdp(n - i, cache))
    cache[n] = 1 + min(l)
    #print(cache)
    return cache[n]

"""print(dt.datetime.now())
print(transact(10000))
print(dt.datetime.now())"""

def transacts_list(n):
    """save the route in the cache"""
    cache = [[0, []] for _ in range(0, n + 1)]
    for i in range(1, n + 1):
        optimal = cache[i - 1]
        z = 1
        for j in [3, 7, 9]:
            if i >= j:
                if cache[i - j][0] < optimal[0]:
                    optimal = cache[i - j]
                    z = j
        cache[i][0] = 1 + optimal[0]
        cache[i][1] = optimal[1] + [z]
    return cache[n][1]