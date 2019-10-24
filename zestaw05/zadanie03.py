#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 5.2
Wielomiany
"""

class Polynomial:
    def __init__(self, *argv):
        """
        Create polynomial.
        """
        self.a = []
        if len(argv) < 1:
            return
        if isinstance(argv[0], (list, tuple)):
            self.a = argv[0]
        else:
            for arg in argv:
                self.a.append(arg)
            self.a.reverse()
        self.__collapse()

    def to_list(self):
        """
        Return polynomial as a list.
        """
        return self.a.copy()

    def __str__(self):
        """
        Return string representation.
        >>> Polynomial().__str__()
        '0'
        >>> Polynomial(1).__str__()
        '1'
        >>> Polynomial(2, 1).__str__()
        '2x + 1'
        >>> Polynomial(3, 2, 1).__str__()
        '3x^2 + 2x + 1'
        >>> Polynomial(3, 0, 1).__str__()
        '3x^2 + 1'
        >>> Polynomial(3, 0, 0).__str__()
        '3x^2'
        >>> Polynomial(0, 0, 3).__str__()
        '3'
        """
        if len(self.a) == 0:
            return '0'
        tmp = []
        if self.a[0] != 0:
            tmp.append(str(self.a[0]))
        if len(self.a) >= 2 and self.a[1] != 0:
            tmp.append(str(self.a[1]) + 'x')
        for i in range(2, len(self.a)):
            if i != 0:
                tmp.append(f'{self.a[i]}x^{i}')
        tmp.reverse()
        return ' + '.join(tmp)

    def __repr__(self):
        """
        Return debug representation.
        >>> Polynomial()
        Polynomial([])
        >>> Polynomial(0, 0, 0, 0)
        Polynomial([])
        >>> Polynomial(1)
        Polynomial([1])
        >>> Polynomial(1, 0)
        Polynomial([0, 1])
        >>> Polynomial(0, 1, 0)
        Polynomial([0, 1])
        >>> Polynomial(1, 0, 0, 0)
        Polynomial([0, 0, 0, 1])
        >>> Polynomial(0, 0, 0, 1, 0, 0, 0)
        Polynomial([0, 0, 0, 1])
        """
        return f'Polynomial({self.a})';

    def __eq__(self, other):
        """
        Test for equality.
        >>> Polynomial() == Polynomial()
        True
        >>> Polynomial(1) == Polynomial()
        False
        >>> Polynomial() == Polynomial(1)
        False
        >>> Polynomial(1) == Polynomial(1)
        True
        """
        if len(self.a) != len(other.a):
            return False
        for i in range(len(self.a)):
            if self.a[i] != other.a[i]:
                return False
        return True

    def __ne__(self, other):
        """
        Return negated polynomial.
        >>> Polynomial() != Polynomial()
        False
        >>> Polynomial(1) != Polynomial()
        True
        >>> Polynomial() != Polynomial(1)
        True
        >>> Polynomial(1) != Polynomial(1)
        False
        >>> Polynomial(1, 2) != Polynomial(1, 2)
        False
        """
        return not (self == other)

    def __collapse(self):
        """
        Remove useless zeros.
        >>> print(Polynomial(0, 0))
        0
        >>> print(Polynomial(1))
        1
        >>> print(Polynomial(0, 0, 1))
        1
        >>> Polynomial(0, 0, 1) == Polynomial(1)
        True
        >>> print(Polynomial(3, 0, 0))
        3x^2
        """
        for i in reversed(self.a):
            if i == 0:
                del self.a[-1]
            else:
                break
        return self

    def __add__(self, other):
        """
        Add two polynomials.
        >>> Polynomial(1, 2) + Polynomial(3, 4) == Polynomial(4, 6)
        True
        >>> Polynomial(1) + Polynomial(0, 1) == Polynomial(2)
        True
        >>> Polynomial(1, 2, 0, 0) + Polynomial(3, 4) == Polynomial(1, 2, 3, 4)
        True
        >>> print(Polynomial(1) + Polynomial(0, 1))
        2
        >>> print(Polynomial(1, 1) + Polynomial(1, 0))
        2x + 1
        >>> print(Polynomial(1, 2) + Polynomial(3, 4))
        4x + 6
        """
        l = min(len(self.a), len(other.a))
        from operator import add
        return Polynomial(
            list(map(add, self.a[:l], other.a[:l]))
            # at least one of them will be empty
            + self.a[l:]
            + other.a[l:]
        )

    def __neg__(self):
        """
        Negate polynomial.
        >>> print(-Polynomial(-1, -2, -3))
        1x^2 + 2x + 3
        >>> print(-Polynomial(0))
        0
        >>> Polynomial() == -Polynomial()
        True
        >>> Polynomial(1) == -Polynomial(-1)
        True
        """
        return Polynomial([-a for a in self.a])

    def __sub__(self, other):
        """
        Subtract two polynomials.
        >>> Polynomial(1, 1) - Polynomial(1, 0) == Polynomial(1)
        True
        >>> Polynomial(7, 4, 12) - Polynomial(8, 13, -7) == Polynomial(-1, -9, 19)
        True
        """
        return self + -other

    def __mul__(self, other):
        """
        Multiply two polynomials.
        >>> Polynomial(0, 0, 1) * Polynomial(1, 2) == Polynomial(0, 0, 1, 2)
        True
        >>> Polynomial(2, 1) * Polynomial(6, 4) == Polynomial(12, 14, 4)
        True
        >>> Polynomial(2, 1) * Polynomial() == Polynomial(0)
        True
        >>> print(Polynomial(1, 0, 1) * Polynomial(1, 1, 0))
        1x^4 + 1x^3 + 1x^2 + 1x
        """
        out = [0] * (len(self.a) + len(other.a) - 1)
        for i in range(len(self.a)):
            for j in range(len(other.a)):
                out[i + j] += self.a[i] * other.a[j]
        return Polynomial(out)

    def __pow__(self, other):
        """
        Return polynomial to the power of other.
        >>> Polynomial() ** 0 == Polynomial(1)
        True
        >>> Polynomial() ** 2 == Polynomial()
        True
        >>> Polynomial() ** 255 == Polynomial()
        True
        >>> Polynomial(1) ** 255 == Polynomial(1)
        True
        >>> Polynomial(2) ** 3 == Polynomial(8)
        True
        >>> Polynomial(2, 0) ** 3 == Polynomial(8, 0, 0, 0)
        True
        >>> Polynomial(2, 1) ** 2 == Polynomial(4, 4, 1)
        True
        >>> Polynomial(2, 1) ** 3 == Polynomial(8, 12, 6, 1)
        True
        >>> Polynomial(3, 2, 1) ** 2 == Polynomial(9, 12, 10, 4, 1)
        True
        >>> Polynomial(3, 2, 1) ** 3 == Polynomial(27, 54, 63, 44, 21, 6, 1)
        True
        """
        t = self
        out = Polynomial(1)
        while other:
            if other & 1:
                out *= t
            t *= t
            other >>= 1
        return out

    def is_zero(self):
        """
        Check if polynomial is a zero.
        >>> Polynomial().is_zero()
        True
        >>> Polynomial(0).is_zero()
        True
        >>> Polynomial(0, 0).is_zero()
        True
        >>> Polynomial(1).is_zero()
        False
        >>> Polynomial(0, 1).is_zero()
        False
        """
        if len(self.a) == 0:
            return True
        return False

    def diff(self):
        """
        Return differential of a polynomial.
        >>> Polynomial().diff() == Polynomial()
        True
        >>> Polynomial(1).diff() == Polynomial()
        True
        >>> Polynomial(2, 1).diff() == Polynomial(2)
        True
        >>> Polynomial(3, 2, 1).diff() == Polynomial(6, 2)
        True
        """
        out = self.a
        for i in range(len(out)):
            out[i] *= i
        return Polynomial(out[1:])

    def __call__(self, x):
        """
        Evaluate polynomial.
        >>> Polynomial(3)(1)
        3
        >>> Polynomial(3, 3)(-1)
        0
        >>> Polynomial(-1, 0, 4)(2)
        0
        >>> Polynomial(1)(2)
        1
        >>> Polynomial(1, 0)(2)
        2
        >>> Polynomial(1, 0, 0)(2)
        4
        >>> Polynomial(1, 0, 0, 0)(2)
        8
        """
        out = 0
        for a in reversed(self.a):
            out = a + x * out
        return out

def to_polynomial(x):
    if isinstance(x, Polynomial):
        return x
    return Polynomial(x)

def add_poly(poly1, poly2):
    return (to_polynomial(poly1) + to_polynomial(poly2)).to_list()

def sub_poly(poly1, poly2):
    return (to_polynomial(poly1) - to_polynomial(poly2)).to_list()

def mul_poly(poly1, poly2):
    return (to_polynomial(poly1) * to_polynomial(poly2)).to_list()

def is_zero(poly):
    return to_polynomial(poly).is_zero()

def cmp_poly(poly1, poly2):
    return to_polynomial(poly1) == to_polynomial(poly2)

def eval_poly(poly, x):
    return to_polynomial(poly)(x)

def combine_poly(poly1, poly2): pass

def pow_poly(poly, n): pass

def diff_poly(poly): pass

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()

    # 1
    x = Polynomial(1)
    print(x)
    # x^2
    x = Polynomial(1, 0, 0)
    print(x)
    # x+2
    y = Polynomial([1, 2])
    print(y)
    # x^2 + x + 2
    print(x + y)
