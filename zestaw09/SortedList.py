#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 9.4
Lista stale posortowana
Jarosław Rymut
"""

# Skopiowana klasa.
class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

    def __repr__(self):
        return f'Node({self.data})'

class SortedList:
    def __init__(self, *list):
        """
        Construct SortedList.
        """
        self.head = None
        self.len = len(list)
        for x in sorted(list, reverse=False):
            self.head = Node(x, next=self.head)

    def __len__(self):
        """
        Return length of SortedList.
        >>> len(SortedList())
        0
        >>> len(SortedList().insert(5))
        1
        >>> len(SortedList(5))
        1
        """
        return self.len;

    def __str__(self):
        """
        Represent SortedList as a string.
        >>> str(SortedList())
        '[]'
        >>> str(SortedList().insert(5))
        '[5]'
        >>> str(SortedList().insert(5).insert(6))
        '[6, 5]'
        >>> str(SortedList().insert(6).insert(5))
        '[6, 5]'
        >>> str(SortedList(6, 5))
        '[6, 5]'
        """
        out = '['
        tmp = self.head
        if tmp:
            out += str(tmp)
            tmp = tmp.next
        while not tmp is None:
            out += ', ' + str(tmp)
            tmp = tmp.next
        out += ']'
        return out

    def __repr__(self):
        """
        Represent SortedList as a string.
        >>> SortedList()
        SortedList()
        >>> SortedList().insert(5)
        SortedList(5)
        >>> SortedList().insert(5).insert(6)
        SortedList(6, 5)
        >>> SortedList(6, 5)
        SortedList(6, 5)
        """
        out = 'SortedList('
        tmp = self.head
        if tmp:
            out += str(tmp)
            tmp = tmp.next
        while not tmp is None:
            out += ', ' + str(tmp)
            tmp = tmp.next
        out += ')'
        return out

    def is_empty(self):
        """
        Check if SortedList is empty.
        >>> SortedList().is_empty()
        True
        >>> SortedList().insert('x').is_empty()
        False
        """
        return self.head is None

    def insert(self, node):
        """
        Insert new element into SortedList.
        >>> SortedList().insert(5)
        SortedList(5)
        >>> SortedList().insert(Node(5, Node(6)))
        SortedList(5)
        >>> SortedList().insert(1).insert(2).insert(3)
        SortedList(3, 2, 1)
        >>> SortedList().insert(1).insert(3).insert(2)
        SortedList(3, 2, 1)
        >>> SortedList().insert(2).insert(1).insert(3)
        SortedList(3, 2, 1)
        >>> SortedList().insert(3).insert(1).insert(2)
        SortedList(3, 2, 1)
        >>> SortedList().insert(3).insert(2).insert(1)
        SortedList(3, 2, 1)
        >>> x = SortedList()
        >>> x.insert(1)
        SortedList(1)
        >>> x.insert(2)
        SortedList(2, 1)
        >>> x.insert(0)
        SortedList(2, 1, 0)
        >>> len(x)
        3
        """
        if not node is Node: # SortedList().insert(5)
            node = Node(node)
        else: # just in case
            node.next = None
        if self.is_empty(): # empty list
            self.head = node
            self.len = 1
            return self
        self.len += 1
        if self.head.data < node.data: # node is a new head
            node.next = self.head
            self.head = node
            return self
        bigger = self.head
        while not (bigger.next is None or bigger.next.data < node.data):
            bigger = bigger.next
        node.next = bigger.next
        bigger.next = node
        return self

    push = insert

    def remove(self, returnNode=True):
        """
        Remove and return node with the biggest value.
        >>> SortedList().remove()
        Traceback (most recent call last):
            ...
        RuntimeError: SortedList is empty
        >>> SortedList(5).remove()
        Node(5)
        >>> SortedList(5, 4).remove()
        Node(5)
        >>> SortedList(5, 6).remove()
        Node(6)
        >>> x = SortedList(0, 1, 2)
        >>> x.remove()
        Node(2)
        >>> x.remove()
        Node(1)
        >>> x.remove()
        Node(0)
        >>> x.remove()
        Traceback (most recent call last):
            ...
        RuntimeError: SortedList is empty
        """
        if self.is_empty():
            raise RuntimeError('SortedList is empty')
        tmp, self.head = self.head, self.head.next
        self.len -= 1
        tmp.next = None
        return tmp

    def pop(self):
        """
        Remove and return the biggest element in the list.
        >>> SortedList().pop()
        Traceback (most recent call last):
            ...
        RuntimeError: SortedList is empty
        >>> SortedList(5).pop()
        5
        >>> SortedList(5, 4).pop()
        5
        >>> SortedList(5, 6).pop()
        6
        >>> x = SortedList(0, 1, 2)
        >>> x.pop()
        2
        >>> x.pop()
        1
        >>> x.pop()
        0
        >>> x.pop()
        Traceback (most recent call last):
            ...
        RuntimeError: SortedList is empty
        """
        return self.remove(returnNode=False).data

    def merge(self, other):
        """
        Merge two sorted lists.
        >>> x = SortedList(1)
        >>> y = SortedList(2)
        >>> x.merge(y)
        SortedList(2, 1)
        >>> y
        SortedList()
        >>> SortedList().merge(SortedList(5))
        SortedList(5)
        >>> SortedList().merge(SortedList())
        SortedList()
        >>> SortedList(5).merge(SortedList())
        SortedList(5)
        >>> SortedList(1).merge(SortedList(2))
        SortedList(2, 1)
        >>> SortedList(2).merge(SortedList(1))
        SortedList(2, 1)
        >>> import itertools
        >>> for perm in itertools.permutations([1, 2, 3, 4]):
        ...     SortedList(*perm[:2]).merge(SortedList(*perm[2:]))
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        SortedList(4, 3, 2, 1)
        """
        if other.is_empty():
            return self
        if self.is_empty():
            self.head = other.head
            self.len = other.len
            other.head = None
            other.len = 0
            return self
        curr = self.head
        ocurr = other.head
        other.head = None
        while not ocurr is None:
            if curr.data < ocurr.data: # insert ocurr before curr
                # swap data
                curr.data, ocurr.data = ocurr.data, curr.data
                # and insert after
                tmp = ocurr.next
                ocurr.next = curr.next
                curr.next = ocurr
                ocurr = tmp
                self.len += 1
                other.len -= 1
                continue
            if curr.next is None: # we finished list
                curr.next = ocurr
                self.len += other.len
                other.len = 0
                return self
            curr = curr.next
        return self

    def clear(self):
        """
        Clear list.
        >>> SortedList().clear()
        SortedList()
        >>> SortedList(1, 2, 3).clear()
        SortedList()
        >>> SortedList(*range(10_000)).clear()
        SortedList()
        """
        self.head = None
        self.len = 0
        return self

if __name__ == '__main__':
    import doctest
    doctest.testmod()
