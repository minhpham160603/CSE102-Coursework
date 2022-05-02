#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 13:23:44 2022

@author: minhpham1606
"""
import random
import math

def is_prime(n, k = 32):
    """Check if an integer is prime using Rabin-Miller algorithm"""
    if n <= 3:
        if n >= 2:
            return True
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for i in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True
        
def genprime(l):
    """Generate a large prime number of roughly l bits"""
    out = 1 + 2**(l - 1)
    for i in range(1, l - 1):
        out += random.randint(0, 1)*2**i
    for i in range(out):
        tmp = out + 2*i
        if is_prime(tmp):
            return tmp
        
def egcd(b, a):
    """Extended Eculidean algorithm to find the gcd(b, a)"""
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0

def genmod(p, q):
    """Generate public and private key from 2 prime number p and q"""
    phi = (p - 1)*(q - 1)
    r, e = 0, 0
    while r != 1:
        e = random.randint(2, phi - 1)
        r, u, v = egcd(e, phi)
    if u < 0:
        k = math.ceil((2 - u)/phi)
        u = u + k*phi
    return ((p*q, e), u)

def keygen(l):
    """Generate a pair of keys of length l bits"""
    p, q = genprime(l//2), genprime(l//2)
    return genmod(p, q)
    
def enc(m, pkey):
    """Encryption with public key
        c = (m**e) mod M"""
    M, e = pkey
    return pow(m, e, M)

def dec(c, pkey, skey):
    """Dencryption with public and private keys
    c = (c**d) mod M"""
    M = pkey[0]
    return pow(c, skey, M)

def encmsg(s, pkey):
    """Encrypt a byte buffer message"""
    res = []
    for c in s:
        res.append(enc(int(c), pkey))
    return res

def decmsg(a, pkey, skey):
    """Decrypt the byte buffer message"""
    res = b''
    for i in a:
        x = dec(i, pkey, skey)
        res += x.to_bytes(1, 'big')
    return res
    
    
    