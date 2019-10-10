#!/usr/bin/env python3
import sys

def longest_word(line):
    (max_len, max_word) = (0, '')
    for i in line.split():
        if len(i) > max_len:
            max_len = len(i)
            max_word = i
    return (max_len, max_word)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # w podanych plikach
        for filename in sys.argv[1:]:
            with open(filename) as f:
                (length, word) = longest_word(f.read())
                print(f'{filename}: Najdłuższy wyraz:', word, '(', length, 'liter )')
                f.close()
    else:
        # na standardowym wejściu
        data = sys.stdin.read()
        (length, word) = longest_word(data)
        print('Najdłuższy wyraz:', word, '(', length, 'liter )')
