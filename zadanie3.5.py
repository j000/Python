#!/usr/bin/env python3

def get_number():
    while True:
        line = input('Podaj liczbę: ')
        try:
            number = int(line)
        except ValueError:
            print('To nie jest liczba')
        else:
            return number

rozmiar = get_number()
out = '|' + '---|' * rozmiar + "\n" + str(0)
for i in range(1, rozmiar+1):
    out += str(i).rjust(4)

print(out)
