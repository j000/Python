#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quadtree
Jarosław Rymut
"""

from point import Point
from collections import deque

"""
  ^
 2|3
--+->
 0|1
  |
"""
class QuadTreeNode:
    def __init__(self, *, center=Point(0.5, 0.5), halfDimension=0.5):
        self.children = [None] * 4
        self.center = center
        self.halfDimension = halfDimension
        self.searched = False

    def get_quarter(self, element):
        bucket = 0
        if isinstance(element, Point):
            if element.x > self.center.x:
                bucket += 1
            if element.y > self.center.y:
                bucket += 2
        elif isinstance(element, QuadTreeNode):
            if element.center.x > self.center.x:
                bucket += 1
            if element.center.y > self.center.y:
                bucket += 2
        return bucket

    def new_child(self, bucket):
        newHalfDimension = self.halfDimension / 2
        newCenter = self.center - newHalfDimension
        if bucket % 2:
            newCenter += Point(self.halfDimension, 0)
        if bucket > 1:
            newCenter += Point(0, self.halfDimension)
        return QuadTreeNode(
            center=newCenter,
            halfDimension=newHalfDimension
        )

    ########################################

    def __str__(self):
        leftTop = self.center - self.halfDimension
        rightBottom = self.center + self.halfDimension
        return f'Node({str(leftTop.x)}-{str(rightBottom.x)}, {str(leftTop.y)}-{str(rightBottom.y)})'

    def print_tree(self, *, file=None, _prefix=[], _last=True):
        empty = '   '
        indent = '│  '
        child = '├─ '
        last = '└─ '
        print(''.join(_prefix), end='')
        if (_last):
            print(last, end='')
            _prefix.append(empty)
        else:
            print(child, end='')
            _prefix.append(indent)
        print(str(self))

        for i, elem in enumerate(self.children):
            prefix = last if i == 3 else child
            if elem is None:
                print(''.join(_prefix) + prefix + 'x')
            elif isinstance(elem, Point):
                print(''.join(_prefix) + prefix + str(elem))
            else:
                elem.print_tree(_prefix=_prefix, _last=(i == 3))
        _prefix.pop()

########################################

class QuadTree:
    def __init__(self, n=0):
        self.root = QuadTreeNode()
        self.insert_random(n)

    def insert_random(self, n=1):
        from random import random, randint, seed
        while n > 0:
            tmp = Point(
                randint(0, 1024) / 1024,
                randint(0, 1024) / 1024
            )
            self.root.insert(tmp)
            n -= 1

    def insert(self, new_point):
        if not isinstance(new_point, Point):
            raise ValueError('Can only insert Points')
        current = self.root
        while True:
            bucket = current.get_quarter(new_point)
            if (isinstance(current.children[bucket], Point)
                and current.children[bucket] == new_point):
                return
            if current.children[bucket] is None:
                current.children[bucket] = new_point
                return
            if isinstance(current.children[bucket], Point):
                point = current.children[bucket]
                node = current.new_child(bucket)
                node.children[node.get_quarter(point)] = point
                current.children[bucket] = node
            current = current.children[bucket]

    def search(self, position, radius):
        results = []
        stack = deque([self.root])
        x0 = position.x - radius
        y0 = position.y - radius
        x3 = position.x + radius
        y3 = position.y + radius
        radius *= radius
        while stack:
            current = stack.pop()
            current.searched = True
            topLeft = current.center - current.halfDimension
            bottomRight = current.center + current.halfDimension
            if (topLeft.x > x3 
                or topLeft.y > y3
                or bottomRight.x < x0
                or bottomRight.y < y0):
                continue
            for element in current.children:
                if (isinstance(element, Point)
                    and ((element.x - position.x) ** 2
                        + (element.y - position.y) ** 2) <= radius):
                        results.append(element)
                if isinstance(element, QuadTreeNode):
                    stack.appendleft(element)
        return results

    def unmark(self):
        stack = deque([self.root])
        while stack:
            elem = stack.pop()
            if not elem.searched:
                continue
            elem.searched = False
            for i in elem.children:
                if isinstance(i, QuadTreeNode):
                    stack.appendleft(i)

    def print_tree(self):
        self.root.print_tree()

########################################

if __name__ == '__main__':
    from random import seed, randint
    x = QuadTree()
    # seed(7)
    for i in range(2500):
        tmp = Point(
            randint(0, 1024) / 1024,
            randint(0, 1024) / 1024
        )
        # print('Inserting', tmp)
        x.insert(tmp)
    x.print_tree()
    print(len(x.search(Point(0.5, 0.5), 1.5)))
    print(len(x.search(Point(0.9, 0.9), 0.17)))
    print(len(x.search(Point(0.3, 0.3), 0.05)))
