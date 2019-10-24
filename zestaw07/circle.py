#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 7.5
Okręgi
Jarosław Rymut
"""

import sys
sys.path.append('../zestaw06')
from point import Point

class Circle:
    """
    Klasa reprezentująca okręgi na płaszczyźnie.
    """
    def __init__(self, center, radius, bonus = None):
        """
        Construct object.
        >>> c = Circle(Point(1, 2), 3)
        >>> c.center == Point(1, 2)
        True
        >>> c.radius == 3
        True
        >>> c = Circle(1, 2, 3)
        >>> c.center == Point(1, 2)
        True
        >>> c.radius == 3
        True
        """
        if isinstance(center, Point):
            self.center = center
            if not self.__is_number_like(radius):
                raise TypeError(f"'{radius}' is not a good radius")
            self.radius = float(radius)
            # if self.radius.is_integer():
            #     self.radius = int(self.radius)
            if radius < 0:
                raise ValueError("radius can't be negative")
        else:
            self.center = Point(center, radius)
            if bonus is None:
                raise ValueError("brak promienia")
            if not self.__is_number_like(bonus):
                raise TypeError(f"'{bonus}' is not a good radius")
            bonus = float(bonus)
            if bonus < 0:
                raise ValueError("radius can't be negative")
            self.radius = bonus

    def __repr__(self):
        """
        Get a string representation of Circle.
        >>> Circle(1, 2, 3)
        Circle(Point(1, 2), 3.0)
        >>> Circle(Point(1, 2), 3)
        Circle(Point(1, 2), 3.0)
        """
        return f'Circle({repr(self.center)}, {self.radius})'

    def __str__(self):
        """
        Get a string representation of Circle.
        >>> print(Circle(1, 2, 3))
        ((1, 2), 3.0)
        >>> print(Circle(Point(1, 2), 3))
        ((1, 2), 3.0)
        """
        return f'({str(self.center)}, {self.radius})'

    def __is_number_like(self, x):
        """
        Check if x can be converted to a number
        >>> Circle(0, 0, 0)._Circle__is_number_like(1)
        True
        >>> Circle(0, 0, 0)._Circle__is_number_like(1.1)
        True
        >>> Circle(0, 0, 0)._Circle__is_number_like('1')
        True
        >>> Circle(0, 0, 0)._Circle__is_number_like('test')
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

    def __eq__(self, other):
        """
        Test for equality.
        >>> Circle(Point(1, 2), 3) == Circle(Point(1, 2), 3)
        True
        >>> Circle(Point(42, 2), 3) == Circle(Point(1, 2), 3)
        False
        >>> Circle(Point(1, 2), 3) == Circle(Point(1, 42), 3)
        False
        >>> Circle(Point(1, 2), 42) == Circle(Point(1, 2), 3)
        False
        >>> Circle(Point(35, -100), 27) == Circle(35, -100, 27)
        True
        >>> Circle(Point(1, 2), 3) == 1
        False
        >>> Circle(Point(1, 2), 3) == 'test'
        False
        """
        if not isinstance(other, Circle):
            return False
        return self.center == other.center and self.radius == other.radius

    def __ne__(self, other):
        """
        Test for inequality.
        >>> Circle(Point(1, 2), 3) != Circle(Point(1, 2), 3)
        False
        >>> Circle(Point(42, 2), 3) != Circle(Point(1, 2), 3)
        True
        >>> Circle(Point(1, 2), 3) != Circle(Point(1, 42), 3)
        True
        >>> Circle(Point(1, 2), 42) != Circle(Point(1, 2), 3)
        True
        >>> Circle(Point(35, -100), 27) != Circle(35, -100, 27)
        False
        >>> Circle(Point(1, 2), 3) != 1
        True
        >>> Circle(Point(1, 2), 3) != 'test'
        True
        """
        return not self == other

    def area(self):
        """
        Calculate area of Circle.
        >>> '{:.5f}'.format(Circle(Point(1, 2), 3).area())
        '28.27433'
        >>> '{:.5f}'.format(Circle(Point(1, 2), 1).area())
        '3.14159'
        >>> '{:.5f}'.format(Circle(Point(3, 42), 1).area())
        '3.14159'
        """
        from math import pi
        return pi * self.radius ** 2

    def move(self, point_or_x, y = None):
        """
        Move Circle by Point.
        >>> Circle(Point(1, 2), 3).move(Point(-1, -2))
        Circle(Point(0, 0), 3.0)
        >>> Circle(Point(1, 2), 3).move(-1, -2)
        Circle(Point(0, 0), 3.0)
        >>> Circle(1, 2, 3).move(Point(-1, -2))
        Circle(Point(0, 0), 3.0)
        >>> Circle(1, 2, 3).move(-1, -2)
        Circle(Point(0, 0), 3.0)
        >>> Circle(1, 2, 3).move(-1)
        Traceback (most recent call last):
            ...
        ValueError: brak drugiej współrzędnej
        >>> Circle(1, 2, 3).move('test')
        Traceback (most recent call last):
            ...
        TypeError: can't move circle by 'test'
        >>> Circle(1, 2, 3).move(1, 'test')
        Traceback (most recent call last):
            ...
        TypeError: can't move circle by 'test'
        """
        if isinstance(point_or_x, Point):
            return Circle(self.center + point_or_x, self.radius)
        if not self.__is_number_like(point_or_x):
            raise TypeError(f"can't move circle by '{point_or_x}'")
        else:
            point_or_x = float(point_or_x)
            if point_or_x.is_integer():
                point_or_x = int(point_or_x)
        if y is None:
            raise ValueError('brak drugiej współrzędnej')
        if not self.__is_number_like(y):
            raise TypeError(f"can't move circle by '{y}'")
        else:
            y = float(y)
            if y.is_integer():
                y = int(y)
        return Circle(self.center + Point(point_or_x, y), self.radius)

    def cover(self, other):
        """
        Find circle enclosing two other circles.
        >>> Circle(Point(0, 0), 1).cover(Circle(Point(0, 0), 2))
        Circle(Point(0, 0), 2.0)
        >>> Circle(Point(0, 1), 1).cover(Circle(Point(0, 3), 1))
        Circle(Point(0.0, 2.0), 2.0)
        >>> Circle(Point(0, 3), 1).cover(Circle(Point(0, 1), 1))
        Circle(Point(0.0, 2.0), 2.0)
        >>> Circle(Point(1, 0), 1).cover(Circle(Point(3, 0), 1))
        Circle(Point(2.0, 0.0), 2.0)
        >>> Circle(Point(3, 0), 1).cover(Circle(Point(1, 0), 1))
        Circle(Point(2.0, 0.0), 2.0)
        >>> sqrt2 = 2 ** 0.5
        >>> Circle(Point(1, 1), sqrt2).cover(Circle(Point(3, 3), sqrt2)) == Circle(Point(2, 2), 2 * sqrt2)
        True
        >>> Circle(0, 0, 1).cover('test')
        Traceback (most recent call last):
            ...
        TypeError: can't calculate cover for 'test'
        """
        if not isinstance(other, Circle):
            raise TypeError(f"can't calculate cover for '{other}'")
        # common center
        if self.center == other.center:
            return Circle(self.center, max(self.radius, other.radius))

        # vector from self to other
        direction = other.center - self.center
        tmp = direction.length()
        # normalize
        direction.x /= tmp
        direction.y /= tmp

        furthest = other.center + Point(
            other.radius * direction.x,
            other.radius * direction.y
        )
        nearest = self.center + Point(
            -self.radius * direction.x,
            -self.radius * direction.y
        )
        new_center = Point(
            (furthest.x + nearest.x)/2,
            (furthest.y + nearest.y)/2
        )
        new_radius = (furthest - nearest).length() / 2
        return Circle(new_center, new_radius)

if __name__ == '__main__':
    # testy
    import doctest
    doctest.testmod()
