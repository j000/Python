#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 2.16
"""
import sys

def fix(line):
    """
    Replaces text 'GvR' to 'Guido van Rossum' in line.

    >>> fix('')
    ''
    >>> fix('test')
    'test'
    >>> fix('test GvR')
    'test Guido van Rossum'
    >>> fix('"testGvR"')
    '"testGuido van Rossum"'
    >>> fix('GvR test GvR')
    'Guido van Rossum test Guido van Rossum'
    """
    return line.replace('GvR', 'Guido van Rossum')

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
                print(f'{filename}: {fix(f.read())}')
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        print(fix(data))
