#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jarosław Rymut
zadanie 3.4
"""

def wczytaj_i_wypisz_liczbe():
    import sys
    while True:
        line = input('Podaj liczbę: ')
        if line == 'stop':
            break
        try:
            number = float(line)
        except ValueError:
            print('To nie jest liczba')
        else:
            print(number, number ** 3)

if __name__ == '__main__':
    wczytaj_i_wypisz_liczbe()
