#!/usr/bin/env python3

L = [3, 5, 4] ; L = L.sort()
## okej

# x, y = 1, 2, 3
## nie okej: za dużo wartości, za mało zmiennych

# X = 1, 2, 3 ; X[1] = 4
## nie okej: tupli nie można modyfikować

# X = [1, 2, 3] ; X[3] = 4
## nie okej: zapis poza listą

# X = "abc" ; X.append("d")
## nie okej: obiekt str nie ma metody append

# map(pow, range(8))
## nie okej: pow przyjmuje 2 argumenty
