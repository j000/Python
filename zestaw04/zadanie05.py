#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 4.5
"""

def odwracanie(L, left, right):
    """
    Return list L with L[left:right+1] reversed
    >>> odwracanie([1, 2, 3, 4], 1, 2)
    [1, 3, 2, 4]
    >>> odwracanie([1, 2, 3, 4], 0, 1)
    [2, 1, 3, 4]
    >>> odwracanie([1, 2, 3, 4], 2, 3)
    [1, 2, 4, 3]
    >>> odwracanie([1, 2, 3, 4], 0, 3)
    [4, 3, 2, 1]
    >>> odwracanie([1, 2], 0, 0)
    [1, 2]
    >>> odwracanie([1, 2], 2, 3)
    [1, 2]
    """
    # return L[:left] + L[right:left-1:-1] + L[right+1:]
    return L[:left] + L[left:right+1][::-1] + L[right+1:]

def odwracanie_rec(L, left, right):
    """
    Return list L with L[left:right+1] reversed - recursive version
    >>> odwracanie_rec([1, 2, 3, 4], 1, 2)
    [1, 3, 2, 4]
    >>> odwracanie_rec([1, 2, 3, 4], 0, 1)
    [2, 1, 3, 4]
    >>> odwracanie_rec([1, 2, 3, 4], 2, 3)
    [1, 2, 4, 3]
    >>> odwracanie_rec([1, 2, 3, 4], 0, 3)
    [4, 3, 2, 1]
    >>> odwracanie_rec([1, 2], 0, 0)
    [1, 2]
    >>> odwracanie_rec([1, 2], 2, 3)
    [1, 2]
    """
    if left >= right or left >= len(L) or right <= 0:
        return L
    L[left], L[right] = L[right], L[left]
    return odwracanie_rec(L, left + 1, right - 1)

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()
