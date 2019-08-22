#!/usr/bin/env python3
import sys

def count_words(line):
    return len(line.split())

data = ''.join(sys.stdin.readlines())
print('Wyzrazy:', count_words(data))
