#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 8.6
Programowanie dynamiczne
Jarosław Rymut
"""

class Cache:
    a = [[0.5]]

    def __getitem__(self, ij):
        i, j = ij
        if i <= 0 and j <= 0:
            return 0.5
        if j <= 0:
            return 0.0
        if i <= 0:
            return 1.0
        try:
            return Cache.a[i][j]
        except IndexError:
            self.__fill(i, j)
            return Cache.a[i][j]

    def __setitem__(self, ij, x):
        i, j = ij
        Cache.a[i][j] = x
        return x

    def print(self):
        for row in Cache.a:
            for item in row:
                print(f' {item:-8.4f}', end='')
            print()
    
    def __fill(self, x, y):
        if len(Cache.a) > x and len(Cache.a[x]) > y:
            return
        Cache.a += [[0.0] for i in range(1 + x - len(Cache.a))]
        Cache.a[0] += [1.0] * (1 + y - len(Cache.a[0]))
        for i in range(1, x + 1):
            old_len = len(Cache.a[i])
            if old_len <= y:
                Cache.a[i] += [None] * (1 + y - old_len)
                for j in range(old_len, y + 1):
                    Cache.a[i][j] = 0.5 * (Cache.a[i - 1][j] + Cache.a[i][j - 1])


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
    i = int(i)
    j = int(j)
    if i <= 0 and j <= 0:
        return 0.5
    if j <= 0:
        return 0.0
    if i <= 0:
        return 1.0
    return Cache()[i, j]

if __name__ == '__main__':
    print(p(2, 4))
    print('rec:', p_rec(2, 4))
    print(p(6, 1))
    print('rec:', p_rec(6, 1))
    print(p(4, 7))
    print('rec:', p_rec(4, 7))
    print(p(20, 40))
    print(p(1_000, 1_000))
    # print(p(10_000, 10_000))
    # print(p_rec(20, 40))

    import timeit

    number = 10_000

    print('timeit p(5, 7):', timeit.timeit('p(5, 7)', setup='from __main__ import p; p(5, 7)', number=number))
    print('timeit p_rec(5, 7):', timeit.timeit('p_rec(5, 7)', setup='from __main__ import p_rec', number=number))
    print('timeit p(200, 400):', timeit.timeit('p(200, 400)', setup='from __main__ import p; p(200, 400)', number=number))
