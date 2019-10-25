#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 12.6
Lider
Jarosław Rymut
"""

def lider_py(L, left, right):
    counter = {}
    for i in L[left:right]:
        counter[i] = counter.get(i, 0) + 1
    for k, v in counter.items():
        if v * 2 - 1 >= len(L):
            return k, v
    return None, None

def inc(A, *, system, index=0):
    if index >= len(A):
        A.append(1)
        return
    x = A[index] + 1
    if x < system:
        A[index] = x
        return
    A[index] = 0
    inc(A, system=system, index=(index + 1))

if __name__ == '__main__':
    N = 4
    max_len = 3

    from random import randint
    tmp = [-1]
    lider = None
    steps = -1
    while steps < N ** max_len - 1:
        inc(tmp, system=N)
        steps += 1
        lider, count = lider_py(tmp, 0, len(tmp))
        print(str(tmp) + ' => ' + str(lider))
