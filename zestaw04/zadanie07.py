#!/usr/bin/env python3

def flatten(sequence):
    out = []
    for i in sequence:
        if isinstance(i, (list, tuple)):
            out += flatten(i)
        else:
            out.append(i)
    return out

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
# [1,2,3,4,5,6,7,8,9]
print(flatten(seq))
