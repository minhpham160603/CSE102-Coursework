#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 21:02:49 2022

@author: minhpham1606
"""

def factorial(n):
    if n <= 1:
        return 1
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac

def fibs():
    r0, r1 = 0, 1
    while True:
        yield r0
        r0, r1 = r1, r0 + r1
        
def prefix_sums(k):
    r0, r1 = k, k + 1
    while True:
        yield r0
        r0 += r1
        r1 += 1
        
def choose_gen(S, k):
    signs = [0]*len(S)
    for i in range(k):
        signs[i] = 1
    
    while True:
        temp = []
        for i in range(len(S)):
            if signs[i] == 1:
                temp.append(S[i])
        yield temp
        last = len(signs) - 1
        num1 = 0
        while signs[last] == 1 and last >= 0:
            signs[last] = 0
            last -= 1
            num1 += 1
        if last == len(S)-k-1:
            break
        first = last
        while signs[first] == 0:
            first -= 1
        signs[first] = 0
        for i in range(num1+1):
            signs[first + 1 + i] = 1
        print(signs)