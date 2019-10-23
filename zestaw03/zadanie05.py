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
    out = '|' + '....|' * rozmiar + "\n" + str(0)
    for i in range(rozmiar):
        out += str(i + 1).rjust(5)
    return out

if __name__ == '__main__':
    rozmiar = get_number()
    print(miarka(rozmiar))
