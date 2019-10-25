#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 13.1
Wyszukiwanie binarne
Jarosław Rymut
"""

def moves(pos):
    (x, y) = pos
    tmp = [
        (x + 1, y - 2),
        (x + 2, y - 1),
        (x + 2, y + 1),
        (x + 1, y + 2),
        (x - 1, y + 2),
        (x - 2, y + 1),
        (x - 2, y - 1),
        (x - 1, y - 2)
    ];
    from random import shuffle
    shuffle(tmp)
    for i in tmp:
        yield i;

class Board:
    CLEAR = 0

    def __init__(self, *, size=6):
        self.size = size
        self.board = []
        for x in range(self.size):
            self.board.append([])
            for y in range(self.size):
                self.board[x].append(self.CLEAR)

    def set(self, pos, *args):
        if not self.is_allowed(pos):
            return
        (x, y) = pos
        if len(args) > 0:
            val = args[0]
        else:
            val = self.CLEAR
        self.board[x][y] = val

    def is_allowed(self, pos):
        (x, y) = pos
        return 0 <= x < self.size and 0 <= y < self.size

    def is_clear(self, pos):
        (x, y) = pos
        return self.is_allowed(pos) and self.board[x][y] == self.CLEAR

    def __str__(self):
        return '\n'.join([
            ' '.join([
                '%2d' % element if element else ' .'
                for element in row
                ])
            for row in self.board
            ])

def knight(board, pos, *, step=None):
    if step is None:
        if not board.is_clear(pos):
            raise ValueError(f'Position {pos} is not clear')
        out = knight(board, pos, step=1)
        if out:
            return board
        raise ValueError(f'It\'s not possible from {pos}')

    board.set(pos, step)
    if step >= board.size * board.size:
        return True
    for i in moves(pos):
        if not board.is_clear(i):
            continue
        out = knight(board, i, step=step + 1)
        if out:
            return board
    board.set(pos)
    return None

if __name__ == '__main__':
    N = 6
    for x in range(N):
        for y in range(N):
            print(f'({x}, {y}):')
            try:
                plansza = Board(size=N)
                print(knight(plansza, (x, y)))
            except ValueError:
                print(f'Brak rozwiązań dla ({x}, {y})')
