#!/usr/bin/env python3

def get_number(prompt='Podaj liczbę'):
    while True:
        line = input(f'{prompt}: ')
        try:
            number = int(line)
        except ValueError:
            print('To nie jest liczba')
        else:
            return number

width = get_number('Podaj szerokość')
height = get_number('Podaj wysokość')

edge = '+' + width * (3 * '-' + '+')
middle = '|' + width * (3 * ' ' + '|')

out = edge + ("\n" + middle + "\n" + edge) * height

print(out)
