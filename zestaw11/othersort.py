#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 11.5
Inne algorytmy sortowawnia
Jarosław Rymut
"""

def is_sorted(A):
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            return False
    return True

def bogosort(A, *, limit=0):
    """
    Bogosort - from bogus, meaning fake.
    Average case: O((n + 1)!)
    Best case: O(n)
    Worst case: unbounded
    """
    from random import shuffle
    while not is_sorted(A):
        shuffle(A)
        if limit > 0:
            limit -= 1
            if limit == 0:
                raise RuntimeError('Limit reached. List is not sorted yet!')

########################################

def miraclesort(A, *, timeout=60):
    """
    Miraclesort - wait for miracle.
    Best case: O(n)
    Worst case: unbounded
    Average case: ?
    """
    import time
    while not is_sorted(A):
        if timeout > 0:
            timeout -= 1
            if timeout == 0:
                raise RuntimeError('Timeout reached. Miracle did not happen. List is not sorted!')
        # wait for miracle and chceck again...
        time.sleep(1)

########################################

def stalinsort(A):
    """
    StalinSort - every element that is out of order is eliminated.
    Running time: O(n)
    """
    out = [A[0]]
    for i in A[1:]:
        if i >= out[-1]:
            out.append(i)
    del A[:]
    A.extend(out)

########################################

if __name__ == '__main__':
    from generators import *

    tmp = list(almost_sorted(15))
    print(', '.join(map(str, tmp)))
    stalinsort(tmp)
    print(', '.join(map(str, tmp)))

    tmp = list(random_order(4))
    print(', '.join(map(str, tmp)))
    bogosort(tmp, limit=20)
    print(', '.join(map(str, tmp)))

    tmp = list(random_order(4))
    print(', '.join(map(str, tmp)))
    miraclesort(tmp, timeout=10)
    print(', '.join(map(str, tmp)))
