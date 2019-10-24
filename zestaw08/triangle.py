#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 8.4
Obliczanie pola powierzchni trójkąta
Jarosław Rymut
"""

def is_float(x):
    try:
        float(x)
        return True
    except (TypeError, ValueError):
        return False

def heron(a, b, c):
    """
    Obliczanie pola powierzchni trójkąta za pomocą wzoru Herona.
    Długości boków trójkąta wynoszą a, b, c.
    >>> heron(3, 4 ,5)
    6.0
    >>> heron(1, 2, 3)
    0.0
    >>> '{:.3f}'.format(heron(2, 3, 4))
    '2.905'
    >>> heron(3, 4, 8)
    Traceback (most recent call last):
        ...
    ValueError: To nie są brzegi trójkąta
    >>> heron('test', 4, 8)
    Traceback (most recent call last):
        ...
    ValueError: 'test' nie jest liczbą
    >>> heron(4, 'test', 8)
    Traceback (most recent call last):
        ...
    ValueError: 'test' nie jest liczbą
    >>> heron(4, 8, 'test')
    Traceback (most recent call last):
        ...
    ValueError: 'test' nie jest liczbą
    """
    if not is_float(a):
        raise ValueError(f"'{a}' nie jest liczbą")
    a = float(a)
    if not is_float(b):
        raise ValueError(f"'{b}' nie jest liczbą")
    b = float(b)
    if not is_float(c):
        raise ValueError(f"'{c}' nie jest liczbą")
    c = float(c)
    if a + b < c or a + c < b or b + c < a:
        raise ValueError('To nie są brzegi trójkąta')
    p = 0.5 * (a + b + c)
    from math import sqrt
    return sqrt(p * (p - a) * (p - b) * (p - c))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
