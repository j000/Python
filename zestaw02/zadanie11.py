#!/usr/bin/env python3
"""
zadanie 2.11
"""
import sys

def improve(line):
    """Funkcja rodziela znaki wstawiając znak '_'

    >>> improve('ab')
    'a_b'
    >>> improve('abc')
    'a_b_c'
    >>> improve('__')
    '___'
    >>> improve('a')
    'a'
    >>> improve('  ')
    ' _ '
    """
    return "_".join(list(line))

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
                print(f'{filename}: {improve(f.read())}')
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        print(improve(data))
