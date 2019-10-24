#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 5.1
Jarosław Rymut
"""

import sys
sys.path.insert(0, '../zestaw04')

####################

from zadanie04 import fibonacci
print(*[fibonacci(x) for x in range(12)],'…')

####################

def silnia(n):
    return 1
print(*[silnia(x) for x in range(5)])
from zadanie03 import silnia
print(*[silnia(x) for x in range(5)])
