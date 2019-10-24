#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 6.6
Wielomiany
"""

class Poly:
    """Klasa reprezentująca wielomiany."""

    # wg Sedgewicka - tworzymy wielomian c*x^n
    def __init__(self, c=0, n=0):
        self.a = []
        if isinstance(c, (tuple, list)):
            self.a = list(c)
            self.__collapse()
            return
        if c == 0:
            return
        self.a = (n + 1) * [0]
        self.a[n] = c

    def __str__(self):
        """
        Get a string representation of Polynomial.
        >>> str(Poly(1, 2))
        '[0, 0, 1]'
        >>> str(Poly(1, 1))
        '[0, 1]'
        >>> str(Poly(1, 0))
        '[1]'
        """
        return str(self.a)

    def __repr__(self):
        """
        Get a string representation of Polynomial.
        >>> repr(Poly(1, 2))
        'Poly([0, 0, 1])'
        >>> repr(Poly(1, 1))
        'Poly([0, 1])'
        >>> repr(Poly(1, 0))
        'Poly([1])'
        """
        return f'Poly({self.a})'

    def __collapse(self):
        """
        Remove useless zeros.
        >>> Poly([0])._Poly__collapse()
        Poly([])
        >>> Poly([1])._Poly__collapse()
        Poly([1])
        >>> Poly([1, 0, 0, 0])._Poly__collapse()
        Poly([1])
        """
        for i in reversed(self.a):
            if i == 0:
                del self.a[-1]
            else:
                break
        return self

    def __add__(self, other):
        """
        Adds two polynomials.
        >>> Poly(1, 2) + Poly(1, 3)
        Poly([0, 0, 1, 1])
        >>> Poly([1, 2]) + Poly([3, 4])
        Poly([4, 6])
        >>> Poly([1]) + Poly([0, 1])
        Poly([1, 1])
        >>> Poly([1, 2]) + Poly([0, 0, 3, 4])
        Poly([1, 2, 3, 4])
        >>> Poly([1, 2]) + Poly([-1, -2])
        Poly([])
        """
        l = min(len(self.a), len(other.a))
        from operator import add
        return Poly(
            list(map(add, self.a[:l], other.a[:l]))
            # at least one of them will be empty
            + self.a[l:]
            + other.a[l:]
        ).__collapse()

    def __sub__(self, other):
        """
        Subtract two polynomials.
        >>> Poly([2]) - Poly([1])
        Poly([1])
        >>> Poly([2, 3]) - Poly([1, 2])
        Poly([1, 1])
        >>> Poly([1, 2, 3]) - Poly([1, 2, 3])
        Poly([])
        """
        return self + -other

    def __mul__(self, other):
        """
        Multiply two polynomials.
        >>> Poly([0, 0, 1]) * Poly([1, 2])
        Poly([0, 0, 1, 2])
        """
        """
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
        out = [0] * (len(self.a) + len(other.a) - 1)
        for i in range(len(self.a)):
            for j in range(len(other.a)):
                out[i + j] += self.a[i] * other.a[j]
        return Poly(out).__collapse()

    def __pos__(self):
        """
        Do nothing.
        >>> +Poly([1])
        Poly([1])
        """
        return self

    def __neg__(self):
        """
        Negate polynomial.
        >>> -Poly([1])
        Poly([-1])
        >>> -Poly([1, 2])
        Poly([-1, -2])
        >>> -Poly([0])
        Poly([])
        >>> -Poly([0, 0, 0])
        Poly([])
        >>> -Poly([-1, 0, 0, 0])
        Poly([1])
        """
        return Poly([-x for x in self.a])

    def __eq__(self, other):
        """
        Test for equality.
        >>> Poly([1]) == Poly([1])
        True
        >>> Poly([1, 2]) == Poly([1, 2])
        True
        >>> Poly([0]) == Poly([])
        True
        >>> Poly([0, 0, 0]) == Poly([0])
        True
        >>> Poly([1, 2]) == Poly([1, 2, 0, 0])
        True
        >>> Poly([1, 1]) == Poly([1, 2])
        False
        """
        l = min(len(self.a), len(other.a))
        for i in range(l):
            if self.a[i] != other.a[i]:
                return False
        for i in range(l, len(self.a)):
            if self.a[i]:
                return False
        for i in range(l, len(other.a)):
            if other.a[i]:
                return False
        return True

    def __ne__(self, other):
        """
        Test for inequality.
        >>> Poly([1]) != Poly([1])
        False
        >>> Poly([1, 2]) != Poly([1, 2])
        False
        >>> Poly([0]) != Poly([])
        False
        >>> Poly([0, 0, 0]) != Poly([0])
        False
        >>> Poly([1, 2]) != Poly([1, 2, 0, 0])
        False
        >>> Poly([1, 1]) != Poly([1, 2])
        True
        """
        return not self == other

    def eval(self, x):
        """
        Evaluate polynomial.
        >>> Poly([3]).eval(1)
        3
        >>> Poly([3, 3]).eval(-1)
        0
        >>> Poly([4, 0, -1]).eval(2)
        0
        >>> Poly([1]).eval(2)
        1
        >>> Poly([0, 1]).eval(2)
        2
        >>> Poly([0, 0, 1]).eval(2)
        4
        >>> Poly([0, 0, 0, 1]).eval(2)
        8
        """
        out = 0
        for a in reversed(self.a):
            out = a + x * out
        return out

    def combine(self, other):
        """
        Combine polynomials.
        >>> Poly([1, 2, 3]).combine(Poly([1]))
        Poly([6])
        >>> Poly([1, 2, 3]).combine(Poly([1, 2]))
        Poly([6, 16, 12])
        >>> Poly([1, 2, 3]).combine(Poly([1, 2, 3]))
        Poly([6, 16, 36, 36, 27])
        """
        out = Poly()
        for a in reversed(self.a):
            out = Poly([a]) + other * out
        return out

    def __pow__(self, n):
        """
        Return polynomial to the power of other.
        >>> Poly([1]) ** 0
        Poly([1])
        >>> Poly([1, 2, 3]) ** 0
        Poly([1])
        >>> Poly([]) ** 2
        Poly([])
        >>> Poly([]) ** 255
        Poly([])
        >>> Poly([0]) ** 255
        Poly([])
        >>> Poly([2]) ** 3
        Poly([8])
        >>> Poly([0, 2]) ** 3
        Poly([0, 0, 0, 8])
        >>> Poly([1, 2]) ** 2
        Poly([1, 4, 4])
        >>> Poly([1, 2]) ** 3
        Poly([1, 6, 12, 8])
        >>> Poly([1, 2, 3]) ** 2
        Poly([1, 4, 10, 12, 9])
        >>> Poly([1, 2, 3]) ** 3
        Poly([1, 6, 21, 44, 63, 54, 27])
        """
        try:
            x = int(n)
        except ValueError:
            raise ValueError(f'{n} is not an integer.')
        t = self
        out = Poly([1])
        while x:
            if x & 1:
                out = out * t
            t = t * t
            x >>= 1
        return out.__collapse()

    def diff(self):
        """
        Return differential of a polynomial.
        >>> Poly([1]).diff()
        Poly([])
        >>> Poly([1, 2]).diff()
        Poly([2])
        >>> Poly([1, 2, 3]).diff()
        Poly([2, 6])
        >>> Poly([0, 0, 1]).diff()
        Poly([0, 2])
        >>> Poly([1, 0, 0]).diff()
        Poly([])
        """
        out = self.a[1:]
        for i in range(len(out)):
            out[i] *= i + 1
        return Poly(out)

    def integrate(self):
        """
        Return inegral of a polynomial.
        >>> Poly().integrate()
        Poly([])
        >>> Poly([1]).integrate()
        Poly([0.0, 1.0])
        >>> Poly([0, 2]).integrate()
        Poly([0.0, 0.0, 1.0])
        >>> Poly([1, 2]).integrate()
        Poly([0.0, 1.0, 1.0])
        >>> Poly([1, 2, 3]).integrate()
        Poly([0.0, 1.0, 1.0, 1.0])
        >>> Poly([0, 0, 0, 0, 5]).integrate()
        Poly([0.0, 0.0, 0.0, 0.0, 0.0, 1.0])
        """
        out = self.a.copy()
        for i in range(len(out)):
            out[i] /= i + 1
        out.insert(0, 0.0)
        return Poly(out)

    def is_zero(self):
        """
        >>> Poly().is_zero()
        True
        >>> Poly([0]).is_zero()
        True
        >>> Poly([0, 0]).is_zero()
        True
        >>> Poly([0, 1]).is_zero()
        False
        >>> Poly([1, 0]).is_zero()
        False
        >>> Poly([1]).is_zero()
        False
        """
        for a in self.a:
            if a != 0:
                return False
        return True

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()
