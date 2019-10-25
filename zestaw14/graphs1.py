#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zadanie 14.1
zadanie 14.5
Jarosław Rymut
"""

def add_node(graph, node):
    """Wstawia wierzchołek do grafu."""
    if node not in graph:
        graph[node] = []

def add_edge_directed(graph, edge):
    """Dodaje krawędź do grafu skierowanego."""
    source, target = edge
    add_node(graph, source)
    add_node(graph, target)
    # # Możemy wykluczyć pętle.
    # if source == target:
    #     raise ValueError("pętle są zabronione")
    if target not in graph[source]:
        graph[source].append(target)

def add_edge_undirected(graph, edge):
    """Dodaje krawędź do grafu nieskierowanego."""
    source, target = edge
    add_node(graph, source)
    add_node(graph, target)
    # # Możemy wykluczyć pętle.
    # if source == target:
    #     raise ValueError("pętle są zabronione")
    if target not in graph[source]:
        graph[source].append(target)
    if source not in graph[target]:
        graph[target].append(source)

########################################

def list_nodes(graph):
    """Zwraca listę wierzchołków grafu."""
    return graph.keys()

def list_edges(graph):
    """Zwraca listę krawędzi (2-krotek) grafu skierowanego bez wag."""
    L = []
    for source in graph:
        for target in graph[source]:
            L.append((source, target))
    return L

def count_nodes(graph):
    return len(graph)

def count_edges(graph):
    count = 0
    for source in graph:
        count += len(graph[source])
    return count

########################################

def make_complete(n):
    graph = {}
    for i in range(1, n):
        for j in range(i):
            add_edge_undirected(graph, (j, i))
    return graph

def make_cyclic(n):
    graph = {}
    for i in range(1, n):
        add_edge_directed(graph, (i - 1, i))
    add_edge_directed(graph, (n - 1, 0))
    return graph

def make_tree(n):
    graph = {}
    v = list(range(n))
    from random import (shuffle, randint)
    shuffle(v)
    for i in range(1, n):
        add_edge_undirected(graph, (v[i], v[randint(0, i-1)]))
    return graph


########################################

if __name__ == '__main__':
    tmp = {}
    add_edge_undirected(tmp, (1, 2))
    add_edge_undirected(tmp, (1, 3))
    add_edge_undirected(tmp, (2, 3))
    print(tmp)
    print(count_nodes(tmp))
    print(count_edges(tmp))
    add_edge_undirected(tmp, (4, 5))
    print(count_nodes(tmp))
    print(count_edges(tmp))
    add_edge_undirected(tmp, (3, 5))
    print(count_nodes(tmp))
    print(count_edges(tmp))

    print()
    print(make_complete(3))
    print(make_complete(4))

    print()
    print(make_cyclic(3))
    print(make_cyclic(4))

    print()
    tmp = make_tree(5)
    print(tmp)
    print('nodes:', count_nodes(tmp))
    print('edges:', count_edges(tmp))
