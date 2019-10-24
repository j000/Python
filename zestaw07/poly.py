#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 7.2
Wielomiany
"""

class Poly:
    """Klasa reprezentująca wielomiany."""

    # wg Sedgewicka - tworzymy wielomian c*x^n
    def __init__(self, c=0, n=0):
        """
        Construct polynomial
        >>> Poly()
        Poly([])
        >>> Poly(3, 1)
        Poly([0, 3])
        >>> Poly(n=2, c=4)
        Poly([0, 0, 4])
        >>> Poly([1, 2])
        Poly([1, 2])
        >>> Poly([0, 1]).a
        [0.0, 1.0]
        >>> Poly('test', 1)
        Traceback (most recent call last):
            ...
        ValueError: could not convert string to float: 'test'
        >>> Poly(1, 0.5)
        Traceback (most recent call last):
            ...
        TypeError: list indices must be integers or slices, not float
        """
        self.a = []
        if isinstance(c, (tuple, list)):
            self.a = [float(x) for x in c]
            self.__collapse()
            return
        if c == 0:
            return
        self.a = (int(n) + 1) * [0.0]
        self.a[n] = float(c)

    def __str__(self):
        """
        Get a string representation of Polynomial.
        >>> str(Poly(1, 2))
        '[0.0, 0.0, 1.0]'
        >>> str(Poly(1, 1))
        '[0.0, 1.0]'
        >>> str(Poly(1, 0))
        '[1.0]'
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
        # return f'Poly({self.a})'
        return 'Poly([' + ', '.join([f'{x:g}' for x in self.a]) + '])'

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

    def __is_number_like(self, x):
        """
        Check if x can be converted to a number
        >>> Poly()._Poly__is_number_like(1)
        True
        >>> Poly()._Poly__is_number_like(1.1)
        True
        >>> Poly()._Poly__is_number_like('1')
        True
        >>> Poly()._Poly__is_number_like('test')
        False
        """
        try:
            float(x)
            return True
        except (TypeError, ValueError):
            try:
                int(x)
                return True
            except (TypeError, ValueError):
                return False

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
        >>> Poly([1, 2]) + 1
        Poly([2, 2])
        >>> 1 + Poly([1, 2])
        Poly([2, 2])
        >>> Poly([1]) + 'test'
        Traceback (most recent call last):
            ...
        TypeError: can't add 'test' to a polynomial
        >>> 'test' + Poly([1])
        Traceback (most recent call last):
            ...
        TypeError: can't add 'test' to a polynomial
        """
        if isinstance(other, Poly):
            l = min(len(self.a), len(other.a))
            from operator import add
            return Poly(
                list(map(add, self.a[:l], other.a[:l]))
                # at least one of them will be empty
                + self.a[l:]
                + other.a[l:]
            ).__collapse()
        if not self.__is_number_like(other):
            raise TypeError(f"can't add '{other}' to a polynomial")
        return self + Poly([other])

    __radd__ = __add__

    def __sub__(self, other):
        """
        Subtract two polynomials or number from polynomial.
        >>> Poly([2]) - Poly([1])
        Poly([1])
        >>> Poly([2, 3]) - Poly([1, 2])
        Poly([1, 1])
        >>> Poly([1, 2, 3]) - Poly([1, 2, 3])
        Poly([])
        >>> Poly([2]) - 1
        Poly([1])
        >>> Poly([1]) - 'test'
        Traceback (most recent call last):
            ...
        TypeError: can't subtract 'test' from a polynomial
        """
        if not self.__is_number_like(other) and not isinstance(other, Poly):
            raise TypeError(f"can't subtract '{other}' from a polynomial")
        return self + -other

    def __rsub__(self, other):
        """
        Subtract pomynomial from number.
        >>> 2 - Poly([1])
        Poly([1])
        >>> 2 - Poly([1, 3])
        Poly([1, -3])
        >>> Poly([2]) - Poly([1, 3])
        Poly([1, -3])
        >>> 'test' - Poly([1])
        Traceback (most recent call last):
            ...
        TypeError: can't subtract a polynomial from 'test'
        """
        if not self.__is_number_like(other) and not isinstance(other, Poly):
            raise TypeError(f"can't subtract a polynomial from '{other}'")
        return -self + other

    def __mul__(self, other):
        """
        Multiply two polynomials or a polynomial and a number.
        >>> Poly([0, 0, 1]) * Poly([1, 2])
        Poly([0, 0, 1, 2])
        >>> Poly([1, 2]) * Poly([4, 6])
        Poly([4, 14, 12])
        >>> Poly([1, 2]) * Poly([])
        Poly([])
        >>> Poly([1, 2, 3]) * Poly([2])
        Poly([2, 4, 6])
        >>> Poly([2]) * Poly([1, 2, 3])
        Poly([2, 4, 6])
        >>> Poly([1, 2, 3]) * 2
        Poly([2, 4, 6])
        >>> 2 * Poly([1, 2, 3])
        Poly([2, 4, 6])
        >>> 'test' * Poly([2])
        Traceback (most recent call last):
            ...
        TypeError: can't multiply a polynomial and 'test'
        >>> Poly([2]) * 'test'
        Traceback (most recent call last):
            ...
        TypeError: can't multiply a polynomial and 'test'
        """
        if isinstance(other, Poly):
            out = [0] * (len(self.a) + len(other.a) - 1)
            for i in range(len(self.a)):
                for j in range(len(other.a)):
                    out[i + j] += self.a[i] * other.a[j]
            return Poly(out).__collapse()
        if not self.__is_number_like(other):
            raise TypeError(f"can't multiply a polynomial and '{other}'")
        return Poly([other * x for x in self.a]).__collapse()

    __rmul__ = __mul__

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
        >>> Poly([1]) == 1
        True
        >>> 2 == Poly([2])
        True
        >>> 'str' == Poly([2])
        False
        """
        if isinstance(other, Poly):
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
        if self.__is_number_like(other):
            return self == Poly([other])
        return False

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
        >>> Poly([1]) != 1
        False
        >>> 2 != Poly([2])
        False
        >>> 'str' != Poly([2])
        True
        """
        return not self == other

    def eval(self, x):
        """
        Evaluate polynomial.
        >>> Poly([3]).eval(1)
        3.0
        >>> Poly([3, 3]).eval(-1)
        0.0
        >>> Poly([4, 0, -1]).eval(2)
        0.0
        >>> Poly([1]).eval(2)
        1.0
        >>> Poly([0, 1]).eval(2)
        2.0
        >>> Poly([0, 0, 1]).eval(2)
        4.0
        >>> Poly([0, 0, 0, 1]).eval(2)
        8.0
        """
        if not self.__is_number_like(x):
            return TypeError(f"can't evaluate polynomial for {x}")
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
        >>> Poly([1, 2, 3]).combine('test')
        Traceback (most recent call last):
            ...
        TypeError: can't combine a polynomial and 'test'
        """
        if not isinstance(other, Poly):
            raise TypeError(f"can't combine a polynomial and '{other}'")
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
        >>> Poly([2]) ** 2.4
        Traceback (most recent call last):
            ...
        ValueError: "2.4" is not an integer
        >>> Poly([2]) ** 'test'
        Traceback (most recent call last):
            ...
        TypeError: "test" is not a number
        """
        if not self.__is_number_like(n):
            raise TypeError(f'"{n}" is not a number')
        if not isinstance(n, int):
            raise ValueError(f'"{n}" is not an integer')
        x = int(n)
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
        Return integral of a polynomial.
        >>> Poly().integrate()
        Poly([])
        >>> Poly([1]).integrate()
        Poly([0, 1])
        >>> Poly([0, 2]).integrate()
        Poly([0, 0, 1])
        >>> Poly([1, 2]).integrate()
        Poly([0, 1, 1])
        >>> Poly([1, 2, 3]).integrate()
        Poly([0, 1, 1, 1])
        >>> Poly([0, 0, 0, 0, 5]).integrate()
        Poly([0, 0, 0, 0, 0, 1])
        """
        out = self.a.copy()
        for i in range(len(out)):
            out[i] /= i + 1
        out.insert(0, 0)
        return Poly(out)

    def __len__(self):
        """
        Return length of a polynomial.
        >>> len(Poly())
        0
        >>> len(Poly([2]))
        1
        >>> len(Poly([3, 0, 0, 0]))
        1
        """
        return len(self.a)

    def __getitem__(self, i):
        """
        Return ith coefficient.
        >>> Poly([1, 2, 3])[0]
        1.0
        >>> Poly([1, 2, 3])[2]
        3.0
        >>> Poly()[0]
        Traceback (most recent call last):
            ...
        IndexError: list index out of range
        >>> Poly()['str']
        Traceback (most recent call last):
            ...
        TypeError: list indices must be integers or slices, not str
        """
        return self.a[i]

    def __setitem__(self, i, value):
        """
        Set ith coefficient to value.
        >>> x = Poly([1, 2, 1])
        >>> x[0] = 3
        >>> x
        Poly([3, 2, 1])
        >>> x = Poly([1, 2, 1])
        >>> x[2] = 3
        >>> x
        Poly([1, 2, 3])
        >>> Poly()[0] = 3
        Traceback (most recent call last):
            ...
        IndexError: list assignment index out of range
        >>> Poly([1])[0] = 'test'
        Traceback (most recent call last):
            ...
        TypeError: coefficients must be numbers, not 'test'
        >>> Poly()['str'] = 4
        Traceback (most recent call last):
            ...
        TypeError: list indices must be integers or slices, not str
        """
        if not self.__is_number_like(value):
            raise TypeError(f"coefficients must be numbers, not '{value}'")
        self.a[i] = value
    
    def __call__(self, x):
        """
        Evaluate or combine polynomials.
        >>> Poly([1, 2])(2)
        5.0
        >>> Poly([1, 2, 3])(Poly([1]))
        Poly([6])
        >>> Poly([1, 2, 3])(1)
        6.0
        >>> Poly([1, 2, 3, 4])('test')
        Traceback (most recent call last):
            ...
        TypeError: call is not possible for test
        """
        if isinstance(x, Poly):
            return self.combine(x)
        if self.__is_number_like(x):
            return self.eval(x)
        raise TypeError(f'call is not possible for {x}')

    def __bool__(self):
        """
        Return false for an empty polynomial.
        >>> bool(Poly())
        False
        >>> bool(Poly([1]))
        True
        >>> bool(Poly([1, 2, 3]))
        True
        """
        for a in self.a:
            if a != 0:
                return True
        return False

    def __int__(self):
        """
        Cast to int if it's possible.
        >>> int(Poly(3, 0))
        3
        >>> int(Poly([3]))
        3
        >>> int(Poly([1, 2]))
        Traceback (most recent call last):
            ...
        ValueError: can't cast Poly([1, 2]) to int
        """
        if len(self.a) == 0:
            return 0
        if len(self.a) != 1:
            raise ValueError(f"can't cast {repr(self)} to int")
        return int(self.a[0])

    def __float__(self):
        """
        Cast to float if it's possible.
        >>> float(Poly(3, 0))
        3.0
        >>> float(Poly([3]))
        3.0
        >>> float(Poly([1, 2]))
        Traceback (most recent call last):
            ...
        ValueError: can't cast Poly([1, 2]) to float
        """
        if len(self.a) == 0:
            return 0.0
        if len(self.a) != 1:
            raise ValueError(f"can't cast {repr(self)} to float")
        return float(self.a[0])

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
        return not self.__bool__()

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()
