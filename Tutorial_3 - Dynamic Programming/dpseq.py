#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 13:54:27 2022

@author: minh.pham
"""

def next_seq(alphas, us):
    res = 0
    for i in range(len(us)):
        res += alphas[i]*us[i]
    return res

def u(alphas, us, n):
    if n < len(us):
        return us[n]
    for _ in range(n - len(us) + 1):
        unext = next_seq(alphas, us)
        us.append(unext)
        us = us[1:]
    return us[-1]