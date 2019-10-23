#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 2.15
"""
import sys

def supernumber(list):
    """
    Returns string made of numbers from list.

    >>> supernumber([42])
    '42'
    >>> supernumber([4, 2])
    '42'
    >>> supernumber([])
    ''
    """
    out = ''
    for i in list:
        out += str(i)
    return out

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            if filename.startswith('-'):
                continue
            with open(filename) as f:
                print(f'{filename}: {supernumber(map(chr, list(f.read())))}')
    else:
        # na standardowym wejściu
        data = map(ord, list(sys.stdin.read().rstrip()))
        print(supernumber(data))
