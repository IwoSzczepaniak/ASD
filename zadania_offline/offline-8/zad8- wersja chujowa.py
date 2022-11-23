from zad8testy import runtests
from math import sqrt, ceil


def distance(A, i, j):
    dis = sqrt( (A[i][0] - A[j][0])**2 + (A[i][1] - A[j][1])**2 )
    return ceil(dis)


def create(A, n, graph):
    for source in range(n):
        for destination in range(n):
            if destination != source:
                tmp = (distance(A, source, destination), source, destination)
                graph.append(tmp)


class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(graph, v, e):
    i = 0
    j = 0
    highest = graph[0][0]
    while i < v-1 and j < e:
        b_parent = find(graph[i][1]) # do poprawy
        d_parent = find(graph[i][2]) # do poprawy
        if b_parent != d_parent:
            union(b_parent, d_parent)
            highest = graph[i][0]
            i += 1
        j += 1
    return highest


def highway( A ):
    v = len(A)
    graph = []
    create(A, v, graph)
    e = len(graph)
    graph.sort()

    min_r = graph[0][0]
    high_r = kruskal(graph, v, e) # pierwszy krok algorytmu

    return min_r - high_r

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )