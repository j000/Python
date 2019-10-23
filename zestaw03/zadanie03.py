#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 3.3
"""

def wypisz_liczby_niepodzielne_przez_3():
    """
    >>> wypisz_liczby_niepodzielne_przez_3()
    1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 23 25 26 28 29
    """
    print(*[x for x in range(30) if (x % 3 != 0)])

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    wypisz_liczby_niepodzielne_przez_3()
