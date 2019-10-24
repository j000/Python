#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jarosław Rymut
zadanie 2.19
"""
import sys
import random

def fun(list):
    """
    Returns string made of numbers from list.
    >>> fun([1])
    '001'
    >>> fun([1, 2])
    '001002'
    """
    return ''.join(
        map(
            lambda x: str.zfill(str(x), 3),
            list
            )
        )

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    tmp = [
        random.randint(0,999) for _ in range(random.randint(10,20))
    ]
    print(f'{tmp} => \n{fun(tmp)}')
