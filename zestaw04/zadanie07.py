#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jarosław Rymut
zadanie 4.7
"""

def flatten_recursive(sequence):
    """
    Returns flattened sequence - recursive version
    >>> flatten_recursive([1, [2, [3]]])
    [1, 2, 3]
    >>> flatten_recursive([])
    []
    """
    out = []
    for i in sequence:
        if isinstance(i, (list, tuple)):
            out += flatten_recursive(i)
        else:
            out.append(i)
    return out

def flatten(sequence):
    """
    Returns flattened sequence
    >>> flatten([1, [2, [3]]])
    [1, 2, 3]
    >>> flatten([])
    []
    """
    out = []
    stack = [sequence]
    while len(stack):
        tmp = stack.pop()
        if isinstance(tmp, (list, tuple)):
            stack.extend(tmp)
        else:
            out.append(tmp)
    out.reverse()
    return out

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
    # [1,2,3,4,5,6,7,8,9]
    print(f'{seq} => {flatten(seq)}')
    print(f'{seq} => {flatten_recursive(seq)}')
