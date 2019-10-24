#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 5.2
Wielomiany
"""

def __collapse(poly):
    """
    Remove useless zeros.
    >>> __collapse([0])
    []
    >>> __collapse([1])
    [1]
    >>> __collapse([1, 0, 0, 0])
    [1]
    """
    for i in reversed(poly):
        if i == 0:
            del poly[-1]
        else:
            break
    return poly

def add_poly(poly1, poly2):
    """
    Add two polynomials.
    >>> add_poly([1, 2], [3, 4])
    [4, 6]
    >>> add_poly([1], [0, 1])
    [1, 1]
    >>> add_poly([1, 2], [0, 0, 3, 4])
    [1, 2, 3, 4]
    >>> add_poly([1, 2], [-1, -2])
    []
    """
    l = min(len(poly1), len(poly2))
    from operator import add
    return __collapse(
        list(map(add, poly1[:l], poly2[:l]))
        # at least one of them will be empty
        + poly1[l:]
        + poly2[l:]
    )

def negate(poly):
    """
    Negate polynomial.
    >>> negate([1])
    [-1]
    >>> negate([1, 2])
    [-1, -2]
    >>> negate([0])
    []
    >>> negate([0, 0, 0])
    []
    >>> negate([-1, 0, 0, 0])
    [1]
    """
    # return list([-a for a in poly])
    return __collapse([-a for a in poly])

def sub_poly(poly1, poly2):
    """
    Subtract two polynomials.
    >>> sub_poly([2], [1])
    [1]
    >>> sub_poly([2, 3], [1, 2])
    [1, 1]
    >>> sub_poly([1, 2, 3], [1, 2, 3])
    []
    """
    return add_poly(poly1, negate(poly2))

def mul_poly(poly1, poly2):
    """
    Multiply two polynomials.
    >>> mul_poly([0, 0, 1], [1, 2])
    [0, 0, 1, 2]
    >>> mul_poly([1, 2], [4, 6])
    [4, 14, 12]
    >>> mul_poly([1, 2], [])
    []
    >>> mul_poly([1, 2, 3], [2])
    [2, 4, 6]
    >>> mul_poly([2], [1, 2, 3])
    [2, 4, 6]
    """
    out = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            out[i + j] += poly1[i] * poly2[j]
    return __collapse(out)

def is_zero(poly):
    """
    >>> is_zero([])
    True
    >>> is_zero([0])
    True
    >>> is_zero([0, 0])
    True
    >>> is_zero([0, 1])
    False
    >>> is_zero([1, 0])
    False
    >>> is_zero([1])
    False
    """
    for a in poly:
        if a != 0:
            return False
    return True

def cmp_poly(poly1, poly2):
    """
    Test for equality.
    >>> cmp_poly([1], [1])
    True
    >>> cmp_poly([1, 2], [1, 2])
    True
    >>> cmp_poly([0], [])
    True
    >>> cmp_poly([0, 0, 0], [0])
    True
    >>> cmp_poly([1, 2], [1, 2, 0, 0])
    True
    """
    l = min(len(poly1), len(poly2))
    for i in range(l):
        if poly1[i] != poly2[i]:
            return False
    for i in range(l, len(poly1)):
        if poly1[i]:
            return False
    for i in range(l, len(poly2)):
        if poly2[i]:
            return False
    return True

def eval_poly(poly, x):
    """
    Evaluate polynomial.
    >>> eval_poly([3], 1)
    3
    >>> eval_poly([3, 3], -1)
    0
    >>> eval_poly([4, 0, -1], 2)
    0
    >>> eval_poly([1], 2)
    1
    >>> eval_poly([0, 1], 2)
    2
    >>> eval_poly([0, 0, 1], 2)
    4
    >>> eval_poly([0, 0, 0, 1], 2)
    8
    """
    out = 0
    for a in reversed(poly):
        out = a + x * out
    return out

def combine_poly(poly1, poly2):
    """
    Combine polynomials.
    >>> combine_poly([1, 2, 3], [1])
    [6]
    >>> combine_poly([1, 2, 3], [1, 2])
    [6, 16, 12]
    >>> combine_poly([1, 2, 3], [1, 2, 3])
    [6, 16, 36, 36, 27]
    """
    out = [0]
    for a in reversed(poly1):
        out = add_poly([a], mul_poly(poly2, out))
    return out

def pow_poly(poly, n):
    """
    Return polynomial to the power of other.
    >>> pow_poly([1], 0)
    [1]
    >>> pow_poly([1, 2, 3], 0)
    [1]
    >>> pow_poly([], 2)
    []
    >>> pow_poly([], 255)
    []
    >>> pow_poly([0], 255)
    []
    >>> pow_poly([2], 3)
    [8]
    >>> pow_poly([0, 2], 3)
    [0, 0, 0, 8]
    >>> pow_poly([1, 2], 2)
    [1, 4, 4]
    >>> pow_poly([1, 2], 3)
    [1, 6, 12, 8]
    >>> pow_poly([1, 2, 3], 2)
    [1, 4, 10, 12, 9]
    >>> pow_poly([1, 2, 3], 3)
    [1, 6, 21, 44, 63, 54, 27]
    """
    try:
        x = int(n)
    except ValueError:
        raise ValueError(f'{n} is not an integer.')
    t = poly
    out = [1]
    while x:
        if x & 1:
            out = mul_poly(out, t)
        t = mul_poly(t, t)
        x >>= 1
    return __collapse(out)

def diff_poly(poly):
    """
    Return differential of a polynomial.
    >>> diff_poly([1])
    []
    >>> diff_poly([1, 2])
    [2]
    >>> diff_poly([1, 2, 3])
    [2, 6]
    >>> diff_poly([0, 0, 1])
    [0, 2]
    >>> diff_poly([1, 0, 0])
    []
    """
    out = poly[1:]
    for i in range(len(out)):
        out[i] *= i + 1
    return __collapse(out)

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()
