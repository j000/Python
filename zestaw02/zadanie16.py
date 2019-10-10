#!/usr/bin/env python3
import sys

def fix(line):
    return line.replace('GvR', 'Guido van Rossum')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            with open(filename) as f:
                print(f'{filename}:', fix(f.read()), end='')
                f.close()
    else:
        # na standardowym wejściu
        print(fix(sys.stdin.read()), end='')
