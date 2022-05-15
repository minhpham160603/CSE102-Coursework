#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:31:47 2022

@author: minhpham1606
"""



def tap_uint16(x, i):
    """ Return 1 or 0 depending on whether the ith-least significant bit
        of x is 1 or 0.
    """
    return (x>>i) & 1


"""print(time.time())
print(tap_uint16(43234, 3))
print(time.time())

print(time.time())
print(slowtap_uint16(43234, 3))
print(time.time())"""

def polytap_uint16(x, I):
    """ Tap x at all the positions in I (which is a list of tap
        positions) and return the xor of all of these tapped values.
    """
    res = 0
    for i in I:
        res = res ^ tap_uint16(x, i)
    return res

print(polytap_uint16(44257, [0, 2, 3, 5]))

def lfsr_uint16(x, I):
    """Return the successor of x in an LFSR based on tap positions I"""
    fbit = polytap_uint16(x, I)
    return (x >> 1) | (fbit << 15)

def test_lfsr_uint16(seed):
    I = [0, 2, 3, 5, 15]
    xs = [seed]
    for _ in range(10):
        xs.append(lfsr_uint16(xs[-1], I))
    return xs

assert test_lfsr_uint16(42) == [42, 21, 10, 32773, 49154,
                                57345, 28672, 14336, 7168,
                                3584, 1792]