#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 13:26:15 2022

@author: minh.pham
"""
import datetime as dt

#naive
def catalan(n):
    if n == 0:
        return 1
    c_n = 0
    for i in range(n):
        c_n += catalan(i)*catalan(n - i - 1)
    return c_n
    
def catalan_td(n, cache = None):
    cache = {} if cache is None else cache
    if n not in cache:
        if n == 0:
            cache[n] = 1
        else:
            c_n = 0
            for i in range(n):
                c_n += catalan_td(i, cache)*catalan_td(n - i - 1, cache)
            cache[n] = c_n
    return cache[n]

#print(dt.datetime.now())
#print(catalan(15))
#print(dt.datetime.now())

def next_catalan(cs):
    n = len(cs)
    if n == 0:
        return 1
    c_n = 0
    for i in range(n):
        c_n += cs[i]*cs[n - i - 1]
    return c_n
    
def catalan_bu(k):
    cs = []
    for _ in range(k + 1):
        c_i = next_catalan(cs)
        cs.append(c_i)
    return cs[-1]

#print(dt.datetime.now())
#print(catalan_bu(100))
#print(dt.datetime.now())