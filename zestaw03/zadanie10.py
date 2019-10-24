#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jarosław Rymut
zadanie 3.10
"""

def roman2int(input):
    """
    Converts roman numerals into ints

    >>> roman2int('I')
    1
    >>> roman2int('II')
    2
    >>> roman2int('XL')
    40
    >>> roman2int('MCMLXXXVII')
    1987
    >>> roman2int('MMMCMLXXXVI')
    3986
    >>> roman2int('MMMM')
    4000
    >>> roman2int('DCLXVI')
    666
    """
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    input = input.strip()
    dlugosc = len(input)
    out = 0
    for i in range(dlugosc):
        if i+1 < dlugosc and numerals[input[i]] < numerals[input[i+1]]:
            out -= numerals[input[i]]
        else:
            out += numerals[input[i]]
    return out

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    for i in ('I', 'II', 'XL', 'MCMLXXXVII', 'MMMCMLXXXVI', 'MMMM'):
        print(i, ':', roman2int(i))
