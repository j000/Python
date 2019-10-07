#!/usr/bin/env python3
import sys

def first_chars(line):
    out = ''
    for i in line.split():
        out += list(i)[0]
    return out

def last_chars(line):
    out = ''
    for i in line.split():
        out += list(i)[-1]
    return out

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            with open(filename) as f:
                print(f'{filename}:', first_chars(f.read()))
                print(f'{filename}:', last_chars(f.read()))
                f.close()
    else:
        # na standardowym wejściu
        data = sys.stdin.read()
        print(first_chars(data))
        print(last_chars(data))
