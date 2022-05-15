#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:35:08 2022

@author: minhpham1606
"""

def uint16_to_bitstring(x):
    """int to binary rep"""
    l = [0]*16
    while x > 0:
        i = 0
        while 2**(i+1) <= x:
            i += 1
        l[- i - 1] = 1
        x -= 2**i
    return l
        
def bitstring_to_uint16(bs):
    """binary to int"""
    res = 0
    for i in range(len(bs)):
        if bs[-i-1] == 1:
            res += 2**i
    return res
        
def mod_pow2(x, k):
    bi_x = uint16_to_bitstring(x)
    l = [0]*16
    for i in range(k):
        l[-i-1] = bi_x[-i-1]
    return bitstring_to_uint16(l)

def is_pow2(x):
    bi_x = uint16_to_bitstring(x)
    n = bi_x.count(1)
    if n != 1:
        return False
    return True

def set_bit(w, k):
    """set the k'th bit of w to 1"""
    return w | (1 << k)

def set_mask(w, m):
    """set every bit position which is 1 in m, to 1 in w"""
    return w | m

def toggle_mask(w, m):
    """toggle every bit position which is 1 in m, in w"""
    return w ^ m

def clear_mask(w, m):
    """set every bit position which is 1 in m, to 0 in w"""
    return w & (~m)