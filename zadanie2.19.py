#!/usr/bin/env python3
import sys
import random

def fun(list):
    return map(lambda x: str.zfill(str(x), 3), list)

if __name__ == '__main__':
    print(', '.join(fun([random.randint(0,999) for _ in range(random.randint(10,20))])))
