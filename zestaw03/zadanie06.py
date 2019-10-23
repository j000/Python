#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 3.6
"""

def get_number(prompt='Podaj liczbę'):
    while True:
        line = input(f'{prompt}: ')
        try:
            number = int(line)
        except ValueError:
            print('To nie jest liczba')
        else:
            return number

# stałe
drawing_chars = ('+-', '| ')
window_size = (3, 1)

def okno(width, height):
    edge = drawing_chars[0][0] + width * (window_size[0] * drawing_chars[0][1] + drawing_chars[0][0])
    middle = drawing_chars[1][0] + width * (window_size[0] * drawing_chars[1][1] + drawing_chars[1][0])
    out = edge + (window_size[1] * ('\n' + middle) + '\n' + edge) * height
    return out

if __name__ == '__main__':
    width = get_number('Podaj szerokość')
    height = get_number('Podaj wysokość')
    print(okno(width, height))
