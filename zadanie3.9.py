#!/usr/bin/env python3

def list_of_sums(inputs):
    return list(map(sum, inputs))

fun = [[],[4],(1,2),[3,4],(5,6,7)]

print(list_of_sums(fun))
