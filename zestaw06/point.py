#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 6.2
Punkt
"""

class Point:
    """
    Klasa reprezentująca punkty na płaszczyźnie.
    """

    def __init__(self, x, y):
        """
        Utwórz punkt o podanych współrzędnych.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Get a string representation of Point.
        >>> str(Point(0, 0))
        '(0, 0)'
        >>> str(Point(7, 42))
        '(7, 42)'
        >>> str(Point(0.0, 0.0))
        '(0.0, 0.0)'
        """
        return f'({self.x}, {self.y})'

    def __repr__(self):
        """
        Get a string representation of Point.
        >>> repr(Point(0, 0))
        'Point(0, 0)'
        >>> repr(Point(7, 42))
        'Point(7, 42)'
        >>> repr(Point(0.0, 0.0))
        'Point(0.0, 0.0)'
        """
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        """
        Check for equivalence.
        >>> Point(0, 0) == Point(0, 0)
        True
        >>> Point(0.0, 0.0) == Point(0, 0)
        True
        >>> Point(1, 2) == Point(1, 2)
        True
        >>> Point(1, 1) == Point(1, 2)
        False
        >>> Point(2, 1) == Point(1, 1)
        False
        >>> Point(2, 1) == Point(1, 2)
        False
        """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """
        Check for inequality.
        >>> Point(0, 0) != Point(0, 0)
        False
        >>> Point(0.0, 0.0) != Point(0, 0)
        False
        >>> Point(1, 2) != Point(1, 2)
        False
        >>> Point(1, 1) != Point(1, 2)
        True
        >>> Point(2, 1) != Point(1, 1)
        True
        >>> Point(2, 1) != Point(1, 2)
        True
        """
        return not self == other

    def __add__(self, other):
        """
        Add two Points.
        >>> Point(0, 0) + Point(0, 0)
        Point(0, 0)
        >>> Point(1, 0) + Point(0, 0)
        Point(1, 0)
        >>> Point(0, 1) + Point(0, 0)
        Point(0, 1)
        >>> Point(1, 1) + Point(0, 0)
        Point(1, 1)
        >>> Point(-1, -1) + Point(1, 1)
        Point(0, 0)
        """
        return Point(self.x + other.x, self.y + other.y)

    def __neg__(self):
        """
        Negates Point.
        >>> -Point(0, 0)
        Point(0, 0)
        >>> -Point(1, 1)
        Point(-1, -1)
        >>> -Point(-1, -1)
        Point(1, 1)
        """
        return Point(-self.x, -self.y)

    def __sub__(self, other):
        """
        Subtracts two Points.
        >>> Point(0, 0) - Point(0, 0)
        Point(0, 0)
        >>> Point(2, 2) - Point(1, 1)
        Point(1, 1)
        >>> Point(1, 1) - Point(-1, -1)
        Point(2, 2)
        """
        return self + -other

    def __mul__(self, other):
        """
        Calculate dot product.
        >>> Point(1, 2) * Point(2, 1)
        4
        >>> Point(2, 4) * Point(2, 4)
        20
        """
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """
        Calculate cross product.
        >>> Point(1, 0).cross(Point(0, 1))
        1
        >>> Point(1, 2).cross(Point(1, 2))
        0
        >>> Point(1, 0).cross(Point(1, 0))
        0
        """
        return self.x * other.y - self.y * other.x

    def length(self):
        """
        Return length of vector.
        >>> Point(0, 0).length()
        0.0
        >>> Point(1, 0).length()
        1.0
        >>> Point(0, 1).length()
        1.0
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()
