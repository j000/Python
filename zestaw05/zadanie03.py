#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 5.2
Wielomiany
"""

class Polynomial:
    def __init__(self, *argv):
        self.a = []
        if len(argv) == 1 and isinstance(argv[0], (list, tuple)):
            self.a = argv[0]
        else:
            for arg in argv:
                self.a.append(arg)
        self.a.reverse()
        self.__collapse()

    def __str__(self):
        """
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

    def __eq__(self, other):
        """
        >>> Polynomial() == Polynomial()
        True
        >>> Polynomial(1) == Polynomial()
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
        >>> Polynomial() != Polynomial()
        False
        >>> Polynomial(1) != Polynomial()
        True
        >>> Polynomial(1) != Polynomial(1)
        False
        """
        return not (self == other)

    def __collapse(self):
        """
        Removes trailing zeros
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
        Adds two polynomials
        >>> Polynomial(1, 2) + Polynomial(3, 4) == Polynomial(4, 6)
        True
        >>> Polynomial(1) + Polynomial(0, 1) == Polynomial(2)
        True
        >>> print(Polynomial(1) + Polynomial(0, 1))
        2
        >>> print(Polynomial(1, 1) + Polynomial(1, 0))
        2x + 1
        >>> print(Polynomial(1, 2) + Polynomial(3, 4))
        4x + 6
        """
        out = Polynomial()
        x1 = len(self.a)
        x2 = len(other.a)
        x3 = min(x1, x2)

        from operator import add
        # at least one of them will be empty
        out.a = list(map(add, self.a[:x3], other.a[:x3])) + self.a[x3:] + other.a[x3:]
        return out.__collapse()

    def __neg__(self):
        """
        Negates polynomial
        >>> print(-Polynomial(-1, -2, -3))
        1x^2 + 2x + 3
        >>> print(-Polynomial(0))
        0
        """
        tmp = Polynomial()
        tmp.a = [-a for a in self.a]
        return tmp

    def __sub__(self, other):
        """
        Subtracts two polynomials
        >>> Polynomial(1, 1) - Polynomial(1, 0) == Polynomial(1)
        True
        """
        return self + -other

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod() # (extraglobs={'poly': Polynomial()})

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
