#!/usr/bin/env python3
"""
zadanie 2.10
"""
import sys

def count_words(line):
    """Funkcja liczy wyrazy w podanym stringu

    >>> count_words('test')
    1
    >>> count_words('test test')
    2
    >>> count_words('test \
    test')
    2
    >>> count_words('one, two, three words here')
    5
    """
    return len(line.split())

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
                print(f'{filename}: Wyrazy: {count_words(f.read())}')
    else:
        # na standardowym wejściu
        data = sys.stdin.read().rstrip()
        print('Wyrazy:', count_words(data))
