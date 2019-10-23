#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 2.13
"""
import sys

def count_letters(line):
    """
    Returns sum of lengths of all words in line.

    >>> count_letters('first test')
    9
    >>> count_letters('Lorem ipsum dolor sit amet')
    22
    """
    return sum(map(len, line.split()))

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
                print(f'{filename}: Liter: {count_letters(f.read())}')
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        print(f'Liter: {count_letters(data)}')
