#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jarosław Rymut
zadanie 4.6
"""

def  sum_seq(sequence):
    """
    Returns sum of numbers in (nested) sequence
    >>> sum_seq([1])
    1
    >>> sum_seq([])
    0
    >>> sum_seq([1, [2, [3]]])
    6
    >>> sum_seq((1, 2))
    3
    >>> sum_seq([1,(2,3),[],[4,(5,6,7)],8,[9]])
    45
    """
    out = 0
    stack = [sequence]
    while len(stack):
        tmp = stack.pop()
        if isinstance(tmp, (list, tuple)):
            stack.extend(tmp)
        else:
            out += tmp
    return out

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
    # [1,2,3,4,5,6,7,8,9]
    print(f'{seq} => {sum_seq(seq)}')
