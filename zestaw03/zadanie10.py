#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 3.10
"""

numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

def roman2int(input):
    input = input.strip()
    dlugosc = len(input)
    out = 0
    for i in range(dlugosc):
        if i+1 < dlugosc and numerals[input[i]] < numerals[input[i+1]]:
            out -= numerals[input[i]]
        else:
            out += numerals[input[i]]
    return out

if __name__ == '__main__':
    for i in ('I', 'II', 'XL', 'MCMLXXXVII', 'MMMCMLXXXVI', 'MMMM'):
        print(i, ':', roman2int(i))
