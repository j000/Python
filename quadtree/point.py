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

    def __init__(self, x, y):
        """
        Utwórz punkt o podanych współrzędnych.
        """
        self.var_x = x
        self.var_y = y

    @property
    def x(self):
        return self.var_x

    @property
    def y(self):
        return self.var_y

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
        return f'({self.var_x}, {self.var_y})'

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
        return f'Point({self.var_x}, {self.var_y})'

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
        return (self.var_x == other.var_x
            and self.var_y == other.var_y)

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
                self.var_x + other.var_x,
                self.var_y + other.var_y
            )
        return Point(
            self.var_x + other,
            self.var_y + other
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
        return Point(-self.var_x, -self.var_y)

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

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()
