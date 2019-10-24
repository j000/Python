#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jarosław Rymut
zadanie 4.4
"""

def get_number():
    while True:
        line = input('Podaj liczbę: ')
        try:
            number = int(line)
        except ValueError:
            print('To nie jest liczba')
        else:
            return number

def fibonacci(input):
    """
    Returns nth elenemt of Fibonacci's sequence

    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(6)
    8
    >>> fibonacci(14)
    377
    """
    x = 1
    y = 0
    while input > 0:
        x = x + y
        x, y = y, x
        input -= 1
    return y

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    liczba = get_number()
    print(f'{liczba}ty wyraz ciągu Fibonacciego to {fibonacci(liczba)}')
