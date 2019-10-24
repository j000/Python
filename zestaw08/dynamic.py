#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 8.6
Programowanie dynamiczne
Jarosław Rymut
"""

class Cache:
    a = []

    def __getitem__(self, ij):
        i, j = ij
        try:
            return Cache.a[i][j]
        except IndexError:
            return None

    def __setitem__(self, ij, x):
        i, j = ij
        if len(Cache.a) <= i:
            Cache.a = Cache.a + [[]] * (1 + i - len(Cache.a))
        tmp = Cache.a[i]
        if len(tmp) <= j:
            tmp += [None] * (1 + j - len(tmp))
        Cache.a[i][j] = x
        return x

def p_rec(i, j):
    if i > 10 or j > 10 or i + j > 15:
        raise ValueError('Chyba żartujesz...')
    if i <= 0 and j <= 0:
        return 0.5
    if j <= 0:
        return 0.0
    if i <= 0:
        return 1.0
    return 0.5 * (p_rec(i - 1, j) + p_rec(i, j - 1))

def p(i, j):
    i = float(i)
    j = float(j)
    if i <= 0 and j <= 0:
        return 0.5
    if j <= 0:
        return 0.0
    if i <= 0:
        return 1.0
    tmp1 = Cache()[i - 1, j]
    if tmp1 is None:
        tmp1 = Cache()[i - 1, j] = p(i - 1, j)
    tmp2 = Cache()[i, j - 1]
    if tmp2 is None:
        tmp2 = Cache()[i, j - 1] = p(i, j - 1)
    return 0.5 * (tmp1 + tmp2)

if __name__ == '__main__':
    print(p(2, 4))
    print(p_rec(2, 4))
    print(p(20, 40))
    # print(p_rec(20, 40))

    import timeit

    print('timeit p(5, 7):', timeit.timeit('p(5, 7)', setup='from __main__ import p; p(5, 7)', number=10_000))
    print('timeit p_rec(5, 7):', timeit.timeit('p_rec(5, 7)', setup='from __main__ import p_rec', number=10_000))
    print('timeit p(200, 400):', timeit.timeit('p(200, 400)', setup='from __main__ import p; p(200, 400)', number=10_000))
