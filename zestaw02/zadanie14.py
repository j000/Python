#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jarosław Rymut
zadanie 2.14
"""
import sys

def longest_word(line):
    """
    Returns length and longest word in line.
    >>> longest_word('test')
    (4, 'test')
    >>> longest_word('test numer dwa')
    (5, 'numer')
    """
    (max_len, max_word) = (0, '')
    for i in line.split():
        if len(i) > max_len:
            max_len = len(i)
            max_word = i
    return (max_len, max_word)

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
                (length, word) = longest_word(f.read())
                print(f'{filename}: Najdłuższy wyraz: "{word}" (length: {length} )')
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        (length, word) = longest_word(data)
        print(f'Najdłuższy wyraz: {word} ({length} liter)')
