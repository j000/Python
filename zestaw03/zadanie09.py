#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 3.9
"""

def list_of_sums(inputs):
    """
    Returns list of sums of all lists inside inputs

    >>> list_of_sums([[3]])
    [3]
    >>> list_of_sums([[],[4],(1,2),[3,4],(5,6,7)])
    [0, 4, 3, 7, 18]
    >>> list_of_sums([(2, 4), [3, 6], [3, 5, 5, 7, 7, 3, 2, 4, 6]])
    [6, 9, 42]
    """
    return list(map(sum, inputs))

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    fun = [[],[4],(1,2),[3,4],(5,6,7)]
    print(f'{fun} => {list_of_sums(fun)}')
