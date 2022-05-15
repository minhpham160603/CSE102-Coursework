#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 15:50:58 2022

@author: minhpham1606
"""
        
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left  = left
        self.right = right

def huffman_stats(s):
    res = dict()
    for i in range(len(s)):
        if s[i] not in res:
            count = 0
            for j in range(i, len(s)):
                if s[j] == s[i]:
                    count += 1
            res[s[i]] = count/len(s)
    return res

def two_min(d):
    l = list(d)
    l = sorted(l, key = lambda x: x[1])
    return l[0], l[1]

def huffman_tree(d):
    #node set
    s = set()
    for i in d:
        s.add((Node(i), d[i]))
    while len(s) > 1:
        #find the two smallest
        m1, m2 = two_min(s)
        outnode = Node( m1[1] + m2[1], m1[0], m2[0])
        s.add((outnode, outnode.value))
        s.remove(m1)
        s.remove(m2)
    return s.pop()[0]
        
    
#x = input("Type your message here: ")
#z = huffman_stats(x)
#r = huffman_tree(z)
#r = (Node(None, Node(None, Node(None, Node('i', None, None), Node(None, Node('m', None, None), Node('o', None, None))), Node(None, Node('e', None, None), Node(None, Node(None, Node(None, Node(None, Node('f', None, None), Node(None, Node('E', None, None), Node('g', None, None))), Node('l', None, None)), Node('p', None, None)), Node('n', None, None)))), Node(None, Node(None, Node(None, Node('r', None, None), Node('u', None, None)), Node(' ', None, None)), Node(None, Node(None, Node(None, Node('c', None, None), Node(None, Node(None, Node(None, Node('.', None, None), Node(None, Node('b', None, None), Node(',', None, None))), Node('h', None, None)), Node(None, Node('q', None, None), Node(None, Node('v', None, None), Node('x', None, None))))), Node('a', None, None)), Node(None, Node('t', None, None), Node(None, Node('s', None, None), Node('d', None, None)))))), 'Elit non eiusmod amet cupidatat amet incididunt magna pariatur aliqua voluptate exercitation eiusmod irure laborum nisi eiusmod commodo consequat qui anim ut aute reprehenderit ex eiusmod sunt officia et consectetur pariatur, in reprehenderit anim commodo esse aute tempor incididunt ad amet proident eu ea veniam quis nisi reprehenderit pariatur deserunt cillum esse.')

#r.display()

def huffman_codes(tree, d = None, path = None, k = 0):
    d = dict() if d is None else d
    path = "" if path is None else path
    if tree.left is None and tree.right is None: 
        d[tree.value] = path
    else:
        huffman_codes(tree.left, d, path + "0", 1)
        huffman_codes(tree.right, d, path + "1", 1)
    if k == 0:
        return d
    
#r.display()
#print(huffman_codes(r))

def huffman_encode(tree, s):
    d = huffman_codes(tree)
    res = ""
    for i in s:
        res += d[i]
    return res

#y = huffman_encode(r, x)
#print("Your compressed code is: ", y)

def huffman_decode(tree, s):
    d = huffman_codes(tree)
    res = ""
    while len(s) > 0:
        for i in d:
            for j in range(len(d[i])):
                if len(d[i]) > len(s) or d[i][j] != s[j]:
                    break
                if j == len(d[i]) - 1:
                    res += i
                    s = s[len(d[i]):]
    return res
                
#s = huffman_decode(r, y)

#print("Your decoded message is: ", s)

def huffman_compress(s):
    z = huffman_stats(s)
    r = huffman_tree(z)
    y = huffman_encode(r, s)
    return (r, y, 8*len(s)/len(y))

#print(huffman_compress(x))