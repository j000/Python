#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jarosław Rymut
zadanie 3.8
"""

def is_hashable(sequence):
    """
    Checks if all elements of sequence can be hashed

    >>> is_hashable([1, 2])
    True
    >>> is_hashable([(1), (2)])
    True
    >>> is_hashable([[1], [2]])
    False
    >>> is_hashable([{1: '1'}])
    False
    """
    from collections.abc import Hashable
    for i in sequence:
        if not isinstance(i, Hashable):
            return False
    return True

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
    >>> common([[1], [2]], [[1]])
    [[1]]
    >>> common([(1)], [[1]])
    []
    >>> common([0, 1], [1, 0])
    [0, 1]
    """
    if is_hashable(seq1) and is_hashable(seq2):
        return list(set(seq1) & set(seq2))
    out = []
    for i in seq1:
        for j in seq2:
            if str(i) == str(j):
                out.append(i)
                break

    return out

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
    >>> all([[1]], [[1]])
    [[1]]
    >>> all([[1], [2]], [[1]])
    [[1], [2]]
    >>> all([(1)], [[1]])
    [(1), [1]]
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
