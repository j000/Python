#!/usr/bin/env python3
import sys

def zeros(number):
    return str(number).count('0')

def print_zeros(number):
    print(number, ':', zeros(number))

if __name__ == '__main__':
    print_zeros(42)
    print_zeros(123456789)
    print_zeros(102030405060708090)
    print_zeros(102030405060708090102030405060708090)
