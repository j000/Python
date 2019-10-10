#!/usr/bin/env python3
import sys

def fun(line):
    tmp = line.split()
    print(sorted(tmp))
    print(sorted(tmp, key=len))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            with open(filename) as f:
                print(f'{filename}:')
                fun(f.read())
                f.close()
    else:
        # na standardowym wejściu
        fun(sys.stdin.read())
