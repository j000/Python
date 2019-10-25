#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 12.2
Wyszukiwanie binarne
Jarosław Rymut
"""

def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    if L[left] == y:
        return left
    if L[right] == y:
        return right
    if left + 1 >= right:
        return None
    index = (left + right) // 2
    if L[index] == y:
        return index
    elif L[index] > y:
        return binarne_rek(L, left + 1, index - 1, y)
    else:
        return binarne_rek(L, index + 1, right - 1, y)

if __name__ == '__main__':
    for N in range(1, 302):
        lista = list(range(N))
        for i in range(N):
            if binarne_rek(lista, 0, len(lista) - 1, i) != i:
                print(lista)
                print(f'binarne_rek(lista, 0, {len(lista) - 1}, {i}) == {binarne_rek(lista, 0, len(lista) - 1, i)}')
                quit(1)
        for i in [-1, N, N // 2 + 0.5]:
            if binarne_rek(lista, 0, len(lista) - 1, i) != None:
                print(lista)
                print(f'binarne_rek(lista, 0, {len(lista) - 1}, {i}) == {binarne_rek(lista, 0, len(lista) - 1, i)}')
                quit(1)
