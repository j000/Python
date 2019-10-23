#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 3.3
"""

def wypisz_liczby_niepodzielne_przez_3():
    print(*[x for x in range(30) if (x % 3 != 0)])

if __name__ == '__main__':
    wypisz_liczby_niepodzielne_przez_3()
