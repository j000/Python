#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jarosław Rymut
zadanie 4.3
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

def silnia(input):
    out = 1
    while input > 1:
        out *= input
        input -= 1
    return out

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    liczba = get_number()
    print(f'Silnia z liczby {liczba} to {silnia(liczba)}')
