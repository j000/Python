#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 3.9
"""

def list_of_sums(inputs):
    return list(map(sum, inputs))

if __name__ == '__main__':
    fun = [[],[4],(1,2),[3,4],(5,6,7)]

    print(list_of_sums(fun))
