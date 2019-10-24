#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Jarosław Rymut

#
x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;
## poprawny kod w python2
## poprawny kod w python3
print(result)

# for i in "qwerty": if ord(i) < 100: print(i)
## w pythonie tak nie wolno. Python jest bardzo rozwlekły

## poprawny kod w python2
# for i in "axby": print ord(i) if ord(i) < 100 else i
## niepoprawny kod w python3 - brak nawiasow przy print()
# for i in "axby": print(ord(i) if ord(i) < 100 else i)
