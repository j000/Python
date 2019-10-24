#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 8.3
Obliczanie PI metodą Monte Carlo
Jarosław Rymut
"""

def get_number(prompt='Podaj liczbę'):
    while True:
        line = input(f'{prompt}: ')
        try:
            return float(line)
        except (TypeError, ValueError):
            print('To nie jest liczba')

def is_int(x):
    try:
        int(x)
        return True
    except (TypeError, ValueError):
        return False

def calc_pi(n=100):
    """
    Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów.
    """
    if not is_int(n):
        raise ValueError('Liczba punktów musi być liczbą całkowitą')
    
    n = int(n)
    
    import random

    inside = 0
    for i in range(n):
        if i % 1_000_000 == 0: print(f'{i / n:.0%}')
        x = random.random()
        y = random.random()
        if x * x + y * y < 1:
            inside += 1
    return 4 * inside / n

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    n = get_number('Podaj liczbę punktów')
    print(calc_pi(n))
