#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 2.17
"""
import sys

def fun(line):
    """
    Returns sorted words from line. First sorted alphabe:

    >>> fun('test')
    (['test'], ['test'])
    >>> fun('Lorem ipsum dolor sit amet')
    (['Lorem', 'amet', 'dolor', 'ipsum', 'sit'], ['sit', 'amet', 'Lorem', 'ipsum', 'dolor'])
    """
    tmp = line.split()
    return (sorted(tmp), sorted(tmp, key=len))

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
                (alpha, length) = fun(f.read())
                print(f'{filename}:\n{alpha}\n{length}')
    else:
        # na standardowym wejściu
        (alpha, length) = fun(sys.stdin.read())
        print(f'{alpha}\n{length}')
