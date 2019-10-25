#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 11.1
Generators
Jarosław Rymut
"""

def random_order(N):
    from random import shuffle
    out = list(range(N))
    shuffle(out)
    return out

def almost_sorted(N):
    from random import randint, shuffle
    start = 0
    max_step = max(3, round(N * 0.1))
    while start < N:
        step = randint(1, max_step)
        if (start + step >= N):
            step = N - start
        tmp = list(range(start, start + step))
        shuffle(tmp)
        for i in tmp:
            yield i
        start += step

def reversed_almost_sorted(N):
    from random import randint, shuffle
    start = N - 1
    max_step = max(4, round(N * 0.1))
    while start >= 0:
        step = randint(1, max_step)
        if (start - step < 0):
            step = start + 1
        tmp = list(range(start, start - step, -1))
        shuffle(tmp)
        for i in tmp:
            yield i
        start -= step

def gauss(N, *, mu=1.0, sigma=1.0):
    from random import gauss as g
    while N > 0:
        yield g(mu, sigma)
        N -= 1

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def with_repeats(N):
    from random import randint
    max = isqrt(N)
    while N > 0:
        yield randint(0, max)
        N -= 1

########################################

if __name__ == '__main__':
    def hamming_distance(list):
        return sum(el != i for i, el in enumerate(list))

    def distance(list):
        return sum(abs(el - i) for i, el in enumerate(list))

    import random
    r = random.random()
    N = 26
    if r < 0.2:
        tmp = list(almost_sorted(N))
    elif r < 0.4:
        tmp = list(random_order(N))
    elif r < 0.6:
        tmp = list(reversed_almost_sorted(N))
    elif r < 0.8:
        tmp = list(reversed(range(N)))
    else:
        tmp = list(with_repeats(N))
    print(', '.join(map(lambda x: str.format('{:2}', x), tmp)), end='    ')
    # print(f'{hamming_distance(tmp):2d}')
    print(f'{distance(tmp):3d}')
