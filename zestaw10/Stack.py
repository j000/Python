#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 10.3
Stack
Jarosław Rymut
"""

class Stack:
    def __init__(self, size=5):
        """
        Initialize stack.
        >>> x = Stack(5)
        >>> x.n
        5
        >>> len(x.dups)
        5
        >>> x = Stack(1024)
        >>> x.n
        1024
        >>> len(x.dups)
        1024
        """
        self.n = size
        self.stack = []
        self.dups = [0 for i in range(size)]

    def __len__(self):
        """
        Count elements on stack.
        >>> x = Stack()
        >>> len(x)
        0
        >>> x.stack.append(5)
        >>> len(x)
        1
        """
        return len(self.stack)

    def push(self, x):
        """
        Push new element to the stack. Ignore duplicates.
        >>> x = Stack(2)
        >>> x.push(2)
        Traceback (most recent call last):
            ...
        ValueError: This stack does not accept values above 2
        >>> x.push(1)
        >>> len(x)
        1
        >>> x.push(0)
        >>> len(x)
        2
        >>> x.push(1)
        >>> len(x)
        2
        """
        if x < 0:
            raise ValueError('This stack does not accept negative values')
        if x >= self.n:
            raise ValueError(f'This stack does not accept values above {self.n}')
        if self.dups[x]:
            return
        self.dups[x] = 1
        self.stack.append(x)

    def pop(self):
        """
        Pop element from Stack.
        >>> x = Stack(2)
        >>> x.push(0)
        >>> len(x)
        1
        >>> x.push(0)
        >>> x.pop()
        0
        >>> len(x)
        0
        >>> x.push(0)
        >>> x.push(1)
        >>> x.pop()
        1
        >>> x.push(1)
        >>> x.pop()
        1
        >>> x.pop()
        0
        """
        if len(self.stack) == 0:
            raise RuntimeError('Can\'t pop from empty stack')
        out = self.stack.pop()
        self.dups[out] = 0
        return out

    def is_empty(self):
        """
        Check if stack is empty.
        >>> Stack().is_empty()
        True
        >>> x = Stack()
        >>> x.push(0)
        >>> x.is_empty()
        False
        """
        return len(self.stack) == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
