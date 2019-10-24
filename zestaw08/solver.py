#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 8.1
Równanie liniowe
Jarosław Rymut
"""

def get_number(prompt='Podaj liczbę'):
    while True:
        line = input(f'{prompt}: ')
        try:
            return float(line)
        except (TypeError, ValueError):
            print('To nie jest liczba')

def solve1(a, b, c):
    """
    Rozwiąż równanie liniowe a * x + b * y + c = 0.
    >>> solve1(0, 0, 0)
    Rozwiązaniem 0 * x + 0 * y + 0 = 0 jest:
    cała płaszczyzna
    >>> solve1(0, 0, 1)
    Rozwiązaniem 0 * x + 0 * y + 1 = 0 jest:
    brak rozwiązań
    >>> solve1(0, 1, 0)
    Rozwiązaniem 0 * x + 1 * y + 0 = 0 jest:
    prosta y = 0.0
    >>> solve1(0, 1, 1)
    Rozwiązaniem 0 * x + 1 * y + 1 = 0 jest:
    prosta y = -1.0
    >>> solve1(1, 0, 0)
    Rozwiązaniem 1 * x + 0 * y + 0 = 0 jest:
    prosta x = 0.0
    >>> solve1(1, 0, 1)
    Rozwiązaniem 1 * x + 0 * y + 1 = 0 jest:
    prosta x = -1.0
    >>> solve1(1, 1, 0)
    Rozwiązaniem 1 * x + 1 * y + 0 = 0 jest:
    prosta y = -1.0 * x
    >>> solve1(1, 1, 1)
    Rozwiązaniem 1 * x + 1 * y + 1 = 0 jest:
    prosta y = -1.0 * x + -1.0
    >>> solve1(0, 0, 8)
    Rozwiązaniem 0 * x + 0 * y + 8 = 0 jest:
    brak rozwiązań
    >>> solve1(0, 4, 0)
    Rozwiązaniem 0 * x + 4 * y + 0 = 0 jest:
    prosta y = 0.0
    >>> solve1(0, 4, 8)
    Rozwiązaniem 0 * x + 4 * y + 8 = 0 jest:
    prosta y = -2.0
    >>> solve1(2, 0, 0)
    Rozwiązaniem 2 * x + 0 * y + 0 = 0 jest:
    prosta x = 0.0
    >>> solve1(2, 0, 8)
    Rozwiązaniem 2 * x + 0 * y + 8 = 0 jest:
    prosta x = -4.0
    >>> solve1(2, 4, 0)
    Rozwiązaniem 2 * x + 4 * y + 0 = 0 jest:
    prosta y = -0.5 * x
    >>> solve1(2, 4, 8)
    Rozwiązaniem 2 * x + 4 * y + 8 = 0 jest:
    prosta y = -0.5 * x + -2.0
    """
    # print(f'https://www.wolframalpha.com/input/?i={a}*x%2B{b}*y%2B{c}%3D0')
    print(f'Rozwiązaniem {a} * x + {b} * y + {c} = 0 jest:')

    if b == 0:
        if a == 0:
            if c == 0:
                return print('cała płaszczyzna')
            return print('brak rozwiązań')
        return print(f'prosta x = {-c / a}')
    a, b = -a / b, -c / b
    if a and b:
        print(f'prosta y = {a} * x + {b}')
    elif a:
        print(f'prosta y = {a} * x')
    else:
        print(f'prosta y = {b}')

if __name__ == '__main__':
    # testy
    import doctest
    if doctest.testmod()[0] > 0:
        quit(1)

    print('Rozwiązywanie równania liniowego a * x + b * y + c = 0.')
    a = get_number('Podaj a')
    b = get_number('Podaj b')
    c = get_number('Podaj c')
    solve1(a, b, c)
