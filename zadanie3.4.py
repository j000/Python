#!/usr/bin/env python3
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
