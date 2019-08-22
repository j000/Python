#!/usr/bin/env python3
import sys

def count_words(line):
    return len(line.split())

if __name__ == "__main__":
    # testy
    assert 1 == count_words('test')
    assert 2 == count_words('test test')
    assert 2 == count_words('test  	test') # sp sp tab
    assert 2 == count_words('test 	 test') # sp tab sp
    # policz wyrazy na standardowym wejściu
    data = ''.join(sys.stdin.readlines())
    print('Wyrazy:', count_words(data))
