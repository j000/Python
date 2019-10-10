#!/usr/bin/env python3
import sys

def improve(line):
    return "_".join(list(line))

if __name__ == '__main__':
    # testy
    assert 't' == improve('t');
    assert 't_t' == improve('tt');
    # popraw
    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            with open(filename) as f:
                print(f'{filename}:', improve(f.read()))
                f.close()
    else:
        # na standardowym wejściu
        data = sys.stdin.read()
        print(improve(data))
