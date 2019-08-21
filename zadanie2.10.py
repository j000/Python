#!/usr/bin/env python3
import sys

data = sys.stdin.readlines()
print('Naliczyłem', len(''.join(data).split()), 'wyrazów.')
