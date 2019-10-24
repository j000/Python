#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jarosław Rymut
zadanie 3.8
"""

def common(seq1, seq2):
    """
    Returns list of elemests that exist in both seq1 and seq2

    >>> common([0], [1])
    []
    >>> common([1], [1])
    [1]
    >>> common([0, 1], [1])
    [1]
    >>> common([0], [])
    []
    >>> common([], [])
    []
    """
    return list(set(seq1) & set(seq2))

def all(seq1, seq2):
    """
    Returns list of elemests from seq1 and seq2

    >>> all([0], [1])
    [0, 1]
    >>> all([1], [1])
    [1]
    >>> all([0, 1], [1])
    [0, 1]
    >>> all([0], [])
    [0]
    >>> all([], [])
    []
    """
    return list(set(seq1 + seq2))

def random_list():
    import random
    return [random.randint(0, 9) for _ in range(random.randint(1, 10))]

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    data1 = random_list()
    data2 = random_list()

    print(data1)
    print(data2)
    print('Common elements:', common(data1, data2))
    print('All elements:', all(data1, data2))
