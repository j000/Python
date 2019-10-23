#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 3.5
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

def miarka(rozmiar):
    """
    Returns ruler of given size

    >>> miarka(3)
    '|....|....|....|\\n0    1    2    3'
    >>> miarka(0)
    '|\\n0'
    >>> miarka(12)
    '|....|....|....|....|....|....|....|....|....|....|....|....|\\n0    1    2    3    4    5    6    7    8    9   10   11   12'
    """
    out = '|' + '....|' * rozmiar + "\n" + str(0)
    for i in range(rozmiar):
        out += str(i + 1).rjust(5)
    return out

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    rozmiar = get_number()
    print(miarka(rozmiar))
