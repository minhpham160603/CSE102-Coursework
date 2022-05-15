#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:24:15 2022

@author: minhpham1606
"""

#Exercise 1
def binary_search(l, a):
    if len(l) == 0:
        return -1
    else:
        i, j = 0, len(l)
        while i < j:
            mid = (i + j)//2
            if l[mid] == a:
                return mid
            elif l[mid] < a:
                i = mid + 1
            else:
                j = mid
        if l[i] == a:
            return i
        return -1

######################
#Exercise 2
def merge(l1, l2):
    i1, i2 = 0, 0
    l = []
    while i1 < len(l1) and i2 < len(l2):
            if l1[i1] <= l2[i2]:
                l.append(l1[i1])
                i1 += 1
            else:
                l.append(l2[i2])
                i2 += 1
    if i1 == len(l1):
        l += l2[i2:]
    if i2 == len(l2):
        l += l1[i1:]
    return l

def merge_sort(l):   
    if len(l) <= 1:
        return l
    mid = len(l)//2
    l1, l2 = [], []
    for i in range(len(l)):
        if i < mid:
            l1.append(l[i])
        else:
            l2.append(l[i])
    l1 = merge_sort(l1)
    l2 = merge_sort(l2)
    return merge(l1, l2)
    
######################
#Exercise 3
def insert_sort(l):
    n = len(l)
    if n <= 1:
        pass
    else:
        for i in range(1, n):
            j = i - 1
            while j >= 0 and l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
                i -= 1
                j -= 1
    print(l)

######################
#Exercise 4
def partioning(l, b, e):
    #pivot = l[e]
    p = b
    i = b
    while i < e:
        if l[i] < l[e]:
            l[i], l[p] = l[p], l[i]
            p += 1
        i += 1
    l[p], l[e] = l[e], l[p]
    return p
        
def qsortRec(l, b, e):
    if e - b <= 1:
        return
    p = partioning(l, b, e)
    qsortRec(l, b, p - 1)
    qsortRec(l, p + 1, e)
            
        
def quicksort (l):
    qsortRec (l , 0 , len ( l ) -1)
    
######################
#Exercise 5
def hpartition(l, b, e):
    pivot = l[b + (e-b+1)//2]
    i, j = b, e
    while i < j:
        while l[i] < pivot:
            i += 1
        while l[j] > pivot:
            j -= 1
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
    if j == e:
        p = e - 1
    else:
        p = j
    return p

def hquicksort_rec(l, b, e):
    if b < e:
        pivot = hpartition(l, b, e)
        hquicksort_rec(l, b, pivot)
        hquicksort_rec(l, pivot + 1, e)
    
def hquicksort(l):
    hquicksort_rec(l, 0, len(l) - 1)
    
def counting_sort(l, k):
    tmp = [0]*k
    for i in range(k):
        count = 0
        for x in l:
            if x == i:
                count += 1
        tmp[i] = count
    j = 0
    while j < len(tmp):
        if tmp[j] > 0:
            for i in range(tmp[j]):
                l[j + i] = j
        j += 1