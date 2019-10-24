#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 10.8
RandomQueue
Jarosław Rymut
"""

class RandomQueue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        """
        Count elements in queue.
        >>> x = RandomQueue()
        >>> len(x)
        0
        >>> x.insert(1)
        >>> len(x)
        1
        >>> x.insert(2)
        >>> len(x)
        2
        >>> x.insert(3)
        >>> len(x)
        3
        >>> x.clear()
        >>> len(x)
        0
        """
        return len(self.queue)

    def insert(self, item):
        """
        Insert element into random position.
        >>> x = RandomQueue()
        >>> x.insert(5)
        >>> x.queue
        [5]
        >>> x.insert(1)
        >>> len(x)
        2
        """
        from random import randrange

        self.queue.append(item)
        i = randrange(len(self.queue))
        self.queue[i], self.queue[-1] = self.queue[-1], self.queue[i]

    def remove(self):
        """
        Remove element from queue.
        >>> x = RandomQueue()
        >>> x.insert(5)
        >>> x.remove()
        5
        >>> x.insert(2)
        >>> x.insert(2)
        >>> x.insert(2)
        >>> x.remove()
        2
        >>> x.remove()
        2
        >>> x.remove()
        2
        """
        # let python handle errors
        return self.queue.pop()

    def is_empty(self):
        """
        Check if queue is empty.
        >>> x = RandomQueue()
        >>> x.is_empty()
        True
        >>> x.insert(1)
        >>> x.is_empty()
        False
        >>> x.clear()
        >>> x.is_empty()
        True
        """
        return len(self) == 0

    def is_full(self):
        """
        Check if queue is full.
        >>> RandomQueue().is_full()
        False
        """
        return False

    def clear(self):
        """
        Clear queue.
        >>> x = RandomQueue()
        >>> x.insert(4)
        >>> x.insert(2)
        >>> x.clear()
        >>> x.queue
        []
        """
        self.queue = []

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    x = RandomQueue()
    print(x.queue)
    x.insert(5)
    x.insert(1)
    x.insert(3)
    x.insert(4)
    x.insert(2)
    print(x.queue)
    for i in range(5):
        print(x.remove())
