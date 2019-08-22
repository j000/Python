#!/usr/bin/env python3
import sys

def count_words(line):
    return len(line.split())

if __name__ == '__main__':
    # testy
    assert 1 == count_words('test')
    assert 2 == count_words('test test')
    assert 2 == count_words('test  \ttest')
    assert 2 == count_words('test \t test')
    assert 2 == count_words('test\t  test')
    assert 2 == count_words('test  \ntest')
    assert 2 == count_words('test \n test')
    assert 2 == count_words('test\n  test')
    # policz wyrazy na standardowym wejściu
    data = ''.join(sys.stdin.readlines())
    print('Wyrazy:', count_words(data))
