#!/usr/bin/env python3
import sys

def count_letters(line):
    return sum(map(len, line.split()))

if __name__ == '__main__':
    # testy
    assert 4 == count_letters('test')
    # policz litery
    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            with open(filename) as f:
                print(f'{filename}: Liter:', count_letters(f.read()))
                f.close()
    else:
        # na standardowym wejściu
        data = sys.stdin.read()
        print('Liter:', count_letters(data))
