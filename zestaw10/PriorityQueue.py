#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 10.7
PriorityQueue
Jarosław Rymut
"""

class PriorityQueue:
    def __init__(self, cmpfunc=lambda x, y: x > y):
        self.queue = []
        self.cmpfunc = cmpfunc

    def is_empty(self):
        """
        Check if queue is empty.
        >>> PriorityQueue().is_empty()
        True
        >>> x = PriorityQueue()
        >>> x.insert(1)
        >>> x.is_empty()
        False
        """
        return len(self.queue) == 0

    def is_full(self):
        """
        Check if queue is full.
        >>> PriorityQueue().is_full()
        False
        """
        return False

    def insert(self, data):
        """
        Insert element into queue.
        >>> x = PriorityQueue()
        >>> x.insert(1)
        >>> x.queue
        [1]
        >>> x.insert(2)
        >>> x.queue
        [1, 2]
        """
        self.queue.append(data)

    def remove(self):
        """
        Remove element with highest priority
        >>> x = PriorityQueue()
        >>> x.insert(1)
        >>> x.queue
        [1]
        >>> x.insert(2)
        >>> x.queue
        [1, 2]
        >>> x.remove()
        2
        >>> x.remove()
        1
        >>> x.remove()
        Traceback (most recent call last):
            ...
        RuntimeError: Can't remove from empty queue
        >>> x = PriorityQueue()
        >>> x.insert(2)
        >>> x.insert(3)
        >>> x.insert(4)
        >>> x.insert(1)
        >>> x.remove()
        4
        >>> x.remove()
        3
        >>> x.remove()
        2
        >>> x.remove()
        1
        >>> x.is_empty()
        True
        >>> x = PriorityQueue(lambda x, y: x < y)
        >>> x.insert(2)
        >>> x.insert(3)
        >>> x.insert(4)
        >>> x.insert(1)
        >>> x.remove()
        1
        >>> x.remove()
        2
        >>> x.remove()
        3
        >>> x.remove()
        4
        >>> x.is_empty()
        True
        """
        if len(self.queue) == 0:
            raise RuntimeError('Can\'t remove from empty queue')
        maxi = 0
        for i in range(len(self.queue)):
            if self.cmpfunc(self.queue[i], self.queue[maxi]) > 0:
                maxi = i
        data = self.queue[maxi]
        self.queue[maxi] = self.queue[-1]
        self.queue.pop()
        return data

if __name__ == '__main__':
    import doctest
    doctest.testmod()
