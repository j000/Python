#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 2.12
"""
import sys

def first_chars(line):
    """
    Returns string made of first characters of every word in line.

    >>> first_chars('Nobody is calculating expressions.')
    'Nice'
    >>> first_chars('Lorem ipsum dolor sit amet')
    'Lidsa'
    """
    out = ''
    for i in line.split():
        out += list(i)[0]
    return out

def last_chars(line):
    """
    Returns string made of last characters of every word in line.

    >>> last_chars('Lorem ipsum dolor sit amet')
    'mmrtt'
    """
    out = ''
    for i in line.split():
        out += list(i)[-1]
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
                print(f'{filename}:', first_chars(f.read()))
                print(f'{filename}:', last_chars(f.read()))
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        print(first_chars(data))
        print(last_chars(data))
