#!/usr/bin/env python3

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

print(roman2int('I'))
print(roman2int('II'))
print(roman2int('XL'))
print(roman2int('MCMLXXXVII'))
print(roman2int('MMMCMLXXXVI'))
print(roman2int('MMMM'))
