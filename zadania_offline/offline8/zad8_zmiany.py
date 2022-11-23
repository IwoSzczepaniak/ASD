from zad8testy import runtests
from math import sqrt


def distance(A, i, j):
    dis = sqrt( (A[i][0] - A[j][0])**2 + (A[i][1] - A[j][1])**2 )
    return int(dis) + 1


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


def kruskal(graph, v, e, l, r):
    i = 0
    j = 0
    coherent = False
    begin_min = 10**10
    destiny_max = -12
    #wynik = []
    vertex = []
    for x in range(v):
        vertex.append(x)
        vertex[x] = Node(x)

    while i < v-1 and j < e:
        begin = graph[j][1]
        destiny = graph[j][2]
        value = graph[j][0]

        if l <= value <= r:
            b_parent = find(vertex[begin])
            d_parent = find(vertex[destiny])
            if b_parent != d_parent:
                union(b_parent, d_parent)
                #wynik.append((begin, destiny, graph[j][0] ))
                begin_min = min(value, begin_min)
                destiny_max = max(value, destiny_max)
                i += 1
        j += 1

    if i == v-1:
        coherent = True

    return begin_min, destiny_max, coherent


def highway( A ):
    v = len(A)
    graph = []
    create(A, v, graph)
    e = len(graph)
    graph.sort()

    last = graph[-1][0]
    a = 0
    b = last
    wynik = 10**10

    while a <= b:
        tiema = kruskal(graph, v, e, a + 1, last)
        if tiema[2]:
            wynik = min(wynik, tiema[1] - tiema[0])
            ret_a = a
        a += 1



    ret = wynik
    return ret, (ret_a, last)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )