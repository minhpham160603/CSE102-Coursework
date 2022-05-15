#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 11:26:57 2022

@author: minhpham1606
"""
import math

def shortest_route_len(G, s, t):
    if s == t:
        return 0
    if G[s] == []:
        return math.inf
    if t in G[s]:
        return 1
    visited = {s}
    aout = [math.inf]*(len(G))
    aout[s] = 0
    queue = []
    current = s
    while len(visited) != len(G):
        for i in G[current]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
                aout[i] = G[s] + 1
        

    
def shortest_route(G, s, t, cache = None):
    cache = {s} if cache is None else cache
    if s == t:
        return 0
    if G[s] == []:
        return math.inf
    if t in G[s]:
        return 1
    check = []
    for l in G[s]:
        if l not in cache:
            cache.add(l)
            check.append(l)
    out = []
    for l in check:
        out.append(shortest_route_len(G, l, t, cache))
    if out == []:
        return 1
    return 1 + min(out)