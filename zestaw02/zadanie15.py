#!/usr/bin/env python3
import sys

def supernumber(line):
    out = ''
    for i in line:
        out += str(i)
    return out

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            with open(filename) as f:
                print(f'{filename}:', supernumber(map(chr, list(f.read()))))
                f.close()
    else:
        # na standardowym wejściu
        data = map(ord, list(sys.stdin.read()))
        print(supernumber(data))
