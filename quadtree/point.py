#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Punkt
Jarosław Rymut
"""

class Point:
    """
    Klasa reprezentująca punkty na płaszczyźnie.
    """

    from collections import namedtuple
    Coords = namedtuple('Coords', ['x', 'y'])

    def __init__(self, x, y):
        """
        Utwórz punkt o podanych współrzędnych.
        """
        self.coords = Point.Coords(x, y)

    @property
    def x(self):
        return self.coords.x

    @property
    def y(self):
        return self.coords.y

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
        return f'({self.coords.x}, {self.coords.y})'

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
        return f'Point({self.coords.x}, {self.coords.y})'

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
        if not isinstance(other, Point):
            return False
        return self.coords.x == other.coords.x \
            and self.coords.y == other.coords.y

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
        if isinstance(other, Point):
            return Point(
                self.coords.x + other.coords.x,
                self.coords.y + other.coords.y
            )
        if isinstance(other, Point.Coords):
            return Point(
                self.coords.x + other.x,
                self.coords.y + other.y
            )
        return Point(
            self.coords.x + other,
            self.coords.y + other
        )

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
        return Point(-self.coords.x, -self.coords.y)

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
        Calculate dot product or multiply coordinates by number.
        >>> Point(1, 2) * Point(2, 1)
        4
        >>> Point(2, 4) * Point(2, 4)
        20
        >>> Point(2, 4) * 2
        Point(4, 8)
        """
        if isinstance(other, Point):
            return (self.coords.x * other.coords.x
                + self.coords.y * other.coords.y)
        if isinstance(other, Point.Coords):
            return (self.coords.x * other.x
                + self.coords.y * other.y)
        return Point(self.coords.x * other, self.coords.y * other)

    def __truediv__(self, other):
        """
        Divide coordinates by numer.
        >>> Point(2, 4) / 2
        Point(1.0, 2.0)
        """
        return Point(self.coords.x / other, self.coords.y / other)

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
        return (self.coords.x * other.coords.y
            - self.coords.y * other.coords.x)

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
        return (self.coords.x ** 2
            + self.coords.y ** 2) ** 0.5

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()
