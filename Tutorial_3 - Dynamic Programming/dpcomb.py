#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 14:25:41 2022

@author: minh.pham
"""

import datetime as dt

def binom_td(n, k, cache = None):
    cache = {} if cache is None else cache
    if (n, k) in cache:
        return cache[n, k]
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        cache[n, k] = binom_td(n - 1, k, cache) + binom_td(n - 1, k - 1, cache)
    return cache[n, k]

#Upper bound recursive calls: n - 1 -> k, n - 2 -> k - 1, ..., n - k -> 0: k.(n - k + 1) times
def parts_td(n, k = None, cache = None):
    cache = {} if cache is None else cache 
    if k is None:
        p_n = 0
        for i in range(1, n + 1):
            p_n += parts_td(n, i, cache)
        return p_n
    if (n, k) in cache:
        return cache[n, k]
    if k == 1:
        return 1
    if k > n:
        return 0
    res = parts_td(n - 1, k - 1, cache) + parts_td(n - k, k, cache)
    cache[n, k] = res
    return cache[n, k]
"""print(dt.datetime.now())
print(parts_td(1000))
print(dt.datetime.now())"""

def parts_bu(n):
    cache = [[0 for _ in range(n+1)] for _ in range(n+1)]
    # if the last element of the last line of the matrix is not 0. minus 1 from it and add to the 
    # smallers one on the left. Do that until only 1 element left.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i >= j:
                if j == 1:
                    cache[i][j] = 1
                else:
                    cache[i][j] = cache[i - 1][j - 1] + cache[i - j][j]
            else:
                break
    return sum(cache[n])
            
"""print(dt.datetime.now())
print(parts_bu(1000))
print(dt.datetime.now())"""

"""
Runtime of parts_td(1000) = 1s
Runtime of parts_bu(1000) = 0.2s
parts_bu() is much faster parts_td()
"""