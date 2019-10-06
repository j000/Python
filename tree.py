#!/usr/bin/env python3

from TreeClass import Tree

tree = Tree()
for i in [4, 2, 6, 1, 3, 5, 7]:
    print('inserting ' + str(i))
    tree.insert(i)
    tree.print()

tree = Tree()
for i in range(5, 1_000):
    if i % 100 == 0:
        print('inserting ' + str(i))
    tree.insert(i)
tree.print()
