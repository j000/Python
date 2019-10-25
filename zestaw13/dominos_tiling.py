#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 13.6
Parkiet
Jarosław Rymut
"""

class Board:
    CLEAR = ' '

    def __init__(self, size=4):
        self.size = size
        self.board = [[self.CLEAR for x in range(self.size)] for y in range(self.size)]

    def set(self, pos, *args):
        if not self.is_allowed(pos):
            return
        (x, y) = pos
        if len(args) > 0:
            val = args[0]
        else:
            val = self.CLEAR
        self.board[y][x] = val

    def is_allowed(self, pos):
        (x, y) = pos
        return 0 <= x < self.size and 0 <= y < self.size

    def is_clear(self, pos):
        (x, y) = pos
        return self.is_allowed(pos) and self.board[y][x] == self.CLEAR

    def is_full(self):
        return not any(any(self.CLEAR == elem for elem in row) for row in self.board)
    
    def copy(self):
        tmp = Board(self.size)
        tmp.board = [row[:] for row in self.board]
        return tmp

    def next_free(self, pos):
        x, y = pos
        while not self.is_clear((x, y)):
            x += 1
            if x >= self.size:
                x = 0
                y += 1
            if y >= self.size:
                return
        yield (x, y)

    def __str__(self):
        return '\n'.join([
            ''.join([
                str(element)
                for element in row
            ])
            for row in self.board
        ])

class Solutions:
    def __init__(self, size=4):
        self.board = Board(size)
        self.solutions = []
        self.__try_layout((0, 0))

    def __iter__(self):
        return iter(self.solutions)

    def __try_layout(self, pos):
        if self.board.is_full():
            self.solutions.append(self.board.copy())
            return
        for x, y in self.board.next_free(pos):
            if self.board.is_clear((x + 1, y)):
                self.board.set((x, y), '-')
                self.board.set((x + 1, y), '-')
                self.__try_layout(pos)
                self.board.set((x, y))
                self.board.set((x + 1, y))
            if self.board.is_clear((x, y + 1)):
                self.board.set((x, y), '|')
                self.board.set((x, y + 1), '|')
                self.__try_layout(pos)
                self.board.set((x, y))
                self.board.set((x, y + 1))


if __name__ == '__main__':
    tmp = Solutions(4)
    print(f'{len(tmp.solutions)} solutions for 4x4 (36 from Wikipedia)')
    for solution in tmp:
        print()
        print(solution)

    tmp = Solutions(6)
    print(f'{len(tmp.solutions)} solutions for 6x6 (6728 from Wikipedia)')
