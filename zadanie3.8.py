#!/usr/bin/env python3
import random

def common(seq1, seq2):
    return list(set(seq1) & set(seq2))

def all(seq1, seq2):
    return list(set(seq1 + seq2))

def random_list():
    return [random.randint(0, 9) for _ in range(random.randint(1, 10))]

data1 = random_list()
data2 = random_list()

print(data1)
print(data2)
print('Common elements:', common(data1, data2))
print('All elements:', all(data1, data2))
