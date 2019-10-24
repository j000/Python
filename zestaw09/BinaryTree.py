#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 9.6
BinaryTree
Jarosław Rymut
"""

class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

########################################

def print_stack(top):
    if top is None:
        return
    stack = list()
    level = 0
    while True:
        while top:
            stack.append((top, level))
            top = top.left
            level += 1
        if not stack:
            return
        top, level = stack.pop()
        print('{}{}'.format('    ' * level, top.data))
        top = top.right
        level += 1

def pprint_tree(node, file=None, _prefix='', _last=True):
    print(_prefix, '`-- ' if _last else '|-- ', node.data, sep='', file=file)
    _prefix += '    ' if _last else '|   '
    if node.left:
        pprint_tree(node.left, file, _prefix, not node.right)
    if node.right:
        pprint_tree(node.right, file, _prefix, True)

def print_dot(root):
    ####################
    # działa u mnie, potrzeba dodatkowego pliku
    return
    ####################
    if root is None:
        return

    import subprocess
    import os

    stack = [root]
    out = 'digraph graphname {\n'
    while stack:
        node = stack.pop()
        out += f'"{id(node)}" [label="{node.data}"];\n'
        if node.left:
            out += f'"{id(node)}" -> "{id(node.left)}";\n'
            stack.append(node.left)
        if node.right:
            out += f'"{id(node)}" -> "{id(node.right)}";\n'
            stack.append(node.right)
    out += '}\n'
    if os.path.exists('./tree.gv'):
        p1 = subprocess.Popen('dot', stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        p2 = subprocess.Popen('gvpr -c -ftree.gv'.split(), stdin=p1.stdout, stdout=subprocess.PIPE, universal_newlines=True)
        p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
        print(out, file=p1.stdin)
        p3 = subprocess.Popen('neato -n -Tx11'.split(), stdin=p2.stdout, universal_newlines=True)
        p2.stdout.close()
    else:
        subprocess.run(('dot', '-Tx11'), text=True, input=out, universal_newlines=True)

def insert_bst(root, element):
    if not isinstance(element, Node):
        element = Node(element)
    while True:
        if root.data < element.data:
            if not root.right:
                root.right = element
                return
            root = root.right
        else:
            if not root.left:
                root.left = element
                return
            root = root.left

def halving_range(start):
    import math
    while start >= 2:
        yield start
        start = math.ceil(start / 2)

########################################

def count_leafs(root):
    if root is None:
        raise ValueError('there is no tree')
    stack = list()   # stos symulujemy przez listę Pythona
    stack.append(root)
    counter = 0
    while stack:
        root = stack.pop()
        if not root.right and not root.left:
            counter += 1
            continue
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return counter

def count_total(root):
    if root is None:
        raise ValueError('there is no tree')
    stack = list()   # stos symulujemy przez listę Pythona
    stack.append(root)
    sum = 0
    while stack:
        root = stack.pop()
        sum += root.data
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return sum

########################################

if __name__ == '__main__':
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    assert(count_leafs(root) == 2)
    assert(count_total(root) == 6)

    for i in range(1, 8, 2):
        root = Node(2)
        insert_bst(root, Node(4))
        insert_bst(root, Node(6))
        insert_bst(root, Node(i))
        pprint_tree(root)
        assert(count_leafs(root) == 1 + (i < 4))

    for i in range(1, 8, 2):
        root = Node(6)
        insert_bst(root, Node(4))
        insert_bst(root, Node(2))
        insert_bst(root, Node(i))
        pprint_tree(root)
        assert(count_leafs(root) == 1 + (i > 4))

    for i in range(1, 8, 2):
        root = Node(4)
        insert_bst(root, Node(2))
        insert_bst(root, Node(6))
        insert_bst(root, Node(i))
        pprint_tree(root)
        assert(count_leafs(root) == 2)

    max = 2 ** 4
    root = Node(int(max / 2))
    for i in halving_range(int(max / 2)):
        for x in range(int(i / 2), max, i):
            insert_bst(root, x)
    print_stack(root)
    print_dot(root)
    assert(count_leafs(root) == max / 2)
    assert(count_total(root) == (max * (max - 1) / 2))
