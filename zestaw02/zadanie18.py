#!/usr/bin/env python3
"""
zadanie 2.18
"""
import sys

def zeros(number):
    """
    Returns number of zeros in number.

    >>> zeros(0)
    1
    >>> zeros(1)
    0
    >>> zeros(10)
    1
    >>> zeros(101010101010)
    6
    """
    return str(number).count('0')

def print_zeros(number):
    """
    Prints number and count of zeros.
    """
    print(number, ':', zeros(number))

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    print_zeros(42)
    print_zeros(123456789)
    print_zeros(102030405060708090)
    print_zeros(102030405060708090102030405060708090)
